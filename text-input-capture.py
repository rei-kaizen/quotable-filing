#open mylife.txt file with the write method
file = open("mylife.txt", "w" )
#put a title
#display the output like a hanging frame on the wall
file.write("           ================== \n"      )
file.write("           + MY LIFE QUOTES +  \n"     )
file.write("           ================== \n"      )
file.write("          /                  \ \n"     )
file.write("         /                    \ \n"    )
file.write("        /                      \ \n"   )
#..........========================================


#use a while loop to keep asking for user text input and store in file until stopped
while True:
    #ask for user input
    text = input("Enter line: ")
    #add quotation mark
    quote = f' "{text}" '
    #create borders around the quote
    top_border = "====" * 10 + "\n"
    bottom_border = "\n" + "====" * 10 + "\n"
    #............ ========================================
    side_border = "|                                      |\n"
    frame = top_border + quote + bottom_border + side_border
    #write it over to the file
    file.write(frame)
    #if there are more line of text to input, type y for yes/continue and n for no/stop
    option = input("Are there more lines (y/n)? ")
    #continue the loop until the user terminate the loop
    if option.lower() == "n":
        break 

#file close
file.close() 

