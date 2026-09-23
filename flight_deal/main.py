#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from dotenv import load_dotenv
import os
from telegram import Update
from data_manager import DataManager
from datetime import datetime

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

load_dotenv()

API  = str(os.getenv("x-app-key"))
TOKEN = str(os.getenv("api_telegram"))
TOKEN_sheets = str(os.getenv("api_sheet"))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data.clear()
    
    now = datetime.now()
    standard_format = now.strftime("%d-%m-%Y %H:%M:%S")
    
    context.user_data["time"] = standard_format
        
    await update.message.reply_text(
        "Enter Your Departure Airport IATA Code:"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user_input = update.message.text.strip().upper()

    # INPUT 1: Departure
    if "departure" not in context.user_data:
        
 
        context.user_data["departure"] = user_input

        await update.message.reply_text(
            "Enter Your Arrival Airport IATA Code:"
        )

        return


    # INPUT 2: Arrival
    if "arrival" not in context.user_data:

        context.user_data["arrival"] = user_input

        await update.message.reply_text(
            "Enter 1 for Round Trip, 2 for One Way:"
        )

        return


    # INPUT 3: Type
    if "type_" not in context.user_data:

        if user_input not in ["1", "2"]:
            await update.message.reply_text(
                "Please enter 1 for Round Trip or 2 for One Way:"
            )
            return

        context.user_data["type_"] = user_input

        await update.message.reply_text(
            "Enter Your Username:"
        )

        return


    # INPUT 4: Username
    if "Username" not in context.user_data:

        context.user_data["Username"] = update.message.text.strip()

        await update.message.reply_text(
            "Enter Your Email:"
        )

        return


    # INPUT 5: Email
    if "Email" not in context.user_data:

        context.user_data["Email"] = update.message.text.strip()

        # Get all inputs
        depart = context.user_data["departure"]
        arrival = context.user_data["arrival"]
        type_ = context.user_data["type_"]
        username = context.user_data["Username"]
        email = context.user_data["Email"]
        standard_format = context.user_data["time"]
     
    
        
        searcher = FlightSearch(departure=depart, arrival=arrival, API_KEY=API, type=type_)
            
        raw_json = searcher.touch()

        flight_info = FlightData(raw_json)

        text = flight_info.return_data()
        
        manager = DataManager(departure=depart, arrival=arrival, type_=type_, time=standard_format, logs=text, username=username, email=email, api=TOKEN_sheets)
        
        result = manager.something()

        await update.message.reply_text(text)

        context.user_data.clear()
        
        return


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))


app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    )
)
print("Bot is running...")

app.run_polling()





