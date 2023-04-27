#open mylife.txt file with the write method
file = open("mylife.txt", "w" )
text = input("Enter line: ")
file.write(text)
file.close()

#use a while loop to keep asking for user text input and store in file until stopped
##ask for user input
##write it over to the file
##if there are more line of text to input, tyoe y for yes/continue and n for no/stop
##continue the loop until the user terminate the loop
#file close 