#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
names_to_send = []       
new_letter_names = []

with open("Input/Names/invited_names.txt") as names:
    for i in names:
        i.strip()
        names_to_send.append(i)

with open("Input/Letters/starting_letter.txt", "r") as letter:
    lines = letter.readlines()
    line_to_change = lines[0]
    
    
    for u in range(len(names_to_send)):
        replace_with = names_to_send[u]
        new_letter_name = line_to_change.replace("[name]", replace_with)
        new_letter_names.append(new_letter_name)

        replace_first_line = line_to_change.replace("Dear [name]", new_letter_name)
        
        with open(f"Output/ReadyToSend{u}", "w") as output:
            output.write(replace_first_line)
  
            for x in range(1, 7):
                output.write(lines[x])
        

print(new_letter_names)
    
    
    
print(line_to_change)