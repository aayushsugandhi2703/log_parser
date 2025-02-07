This file has all the basic concept related to this project 

Scope of Project : To get the understanding about parsing the logs and converting it into JSON format
                
Concepts involved - String manipulation 
                  - file handling
                  - working with list and dictonaries
                  - converting the data to JSON format

1. Starting with the basics of String manipulation
These are you do extraxt, modify and format the String

(a) split(): used to break the string into multiple parts
        ex: 
            log = "[10-10-2000] info : user 'name' ip 1.1.1.1"
            parts = log.split("] ")
            print(parts)            
            # Output: ['[10-10-2000', 'INFO: User \'name\' IP 1.1.1.1']
            so it will divide the string into two parts one will be date and other will be info

            divide = parts[0][1:]  # Remove the starting "[" and goes till "]"
            print(divide)
            #Output: 10-10-2000

(b) strip(), lstrip(), rstrip(): Removing unwanted character
        strip() : removes leading & trailing spaces or specific characters.
        lstrip(): removes leading (left-side) spaces.        
        rstrip(): removes trailing (right-side) spaces.
        ex:
            text = "  ERROR: Something went wrong  "
            clean_text = text.strip()  # Removes extra spaces
            print(clean_text)  # Output: "ERROR: Something went wrong"

(c) find(), index(): used to check if a word exist in a string
        index() raises an error if the substring is not found. So we usually use it in try and except block
        find() returns -1 if the substring is not found.    
        ex: 
            # Using index() - will raise an error if not found
            try:
                pos = log.index("ERROR")
            except ValueError:
                print("Substring not found!")  # Output: Substring not found!

            # Using find() - will return -1 if not found
            pos = log.find("ERROR")
            print(pos)  # Output: -1

(d) slice(): used to extract the specific portion of string
        ex:
            log = "[2025-02-07 12:30:15] INFO: User logged in"
            timestamp = log[1:20]  # Extracts characters from index 1 to 20
            print(timestamp)  # Output: 2025-02-07 12:30:15

(e) replace(): used to replace parts of a string
        ex:
            log = "[2025-02-07 12:30:15] INFO: User logged in"
            clean_log = log.replace("[", "").replace("]", "")  # Remove brackets
            print(clean_log)
            # Output: 2025-02-07 12:30:15 INFO: User logged in
