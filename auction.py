from art import hammer



bid_dic = {}
on = True



while on:
    print(hammer)
    name = str(input("What is your name? \n"))
    bid = str(input("What is your bid \n"))

    bid_dic.update({name: bid})
    question = (input("Is there another bid \n").lower())
    if question == "no":
        highest_bid = max(bid_dic, key=bid_dic.get)

        print(f"{highest_bid} won!")
        on = False
    else:
        print("\n" * 20)

    
