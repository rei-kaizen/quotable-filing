# Quotable Filing
 Using a file to store inputted quotes with hanging frame style 

This is a Python program that writes multiple lines of text into a text file named `mylife.txt`. The user is prompted to enter more lines of text until they decide to stop

**See sample output:**
```
Enter line: Beautiful is better than ugly.
Are there more lines y/n? y
Enter line: Explicit is better than implicit.
Are there more lines y/n? y
Enter line: Simple is better than complex.
Are there more lines y/n? n
```
Then the program displays their input in the said file in a format that resembles a hanging frame on a wall (see `myliufe.txt` for a demonstration). 
<br>

# How to use
1. Run the program in a Python environment. <br>
2. Follow the prompt to enter your line of text. <br>
3. If you want to enter more lines, type y and hit enter. <br>
4. If you're done entering quotes, type n and hit enter. <br>
5. The quotes will be saved in a file named mylife.txt in the same directory as the program.
6. The quote will be displayed in a hanging frame in the said file. <br>

# Additional information
1. The file is opened in `write` mode, so any previous content in `mylife.txt` will be overwritten.<br>
2. The program uses a `while` loop to allow the user to enter multiple line of text.<br>
3. The program uses the `input()` function to prompt the user for input.<br>
4. The hanging frame is created using ASCII characters.<br>
5. The file is closed using the `close()` method to prevent data loss.<br>


# Usage
This program may be used as a tool for keeping visually appealing quotes, notes, and archives.
