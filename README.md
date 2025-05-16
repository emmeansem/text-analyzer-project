Course: Introduction to Programming
Semester: Spring 2025
This is a simple Python project that analyzes the text of a newspaper article and provides useful statistics, such as:

- The number of **unique words**
- The number of **vowels** and **consonants**
- The **10 most frequent words** in the article

## Article Used
The article analyzed is one of the latest ones from BBC:  
"The camera tech propelling shows like Adolescence"

## How It Works

The script (`text_analyzer.py`) performs the following steps:

1. Loads the text from `article.txt`
2. Cleans the text (removes punctuation, converts to lowercase)
3. Splits the text into words
4. Uses a **set** to count unique words
5. Uses a **dictionary** to count word frequencies
6. Counts **vowels** and **consonants**
7. Displays the 10 most frequent words in the text

## How to run
Either on your intalled Python 3 or
Go to https://replit.com/
-Create a free account.
-Create a new Python project.
-Copy and paste:
-The content of text_analyzer.py into main.py
-The article into a new file named article.txt
-Click "Run" at the top.
