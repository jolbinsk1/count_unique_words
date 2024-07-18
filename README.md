# Word Counter Script

This repository contains a Python script which counts the both the total and the unique words contained in a text file that the user writes themselves. It uses a comprehensive list of English words to identify unique words.

## Setup

1) Clone the repository (if applicable) or download the script files directly.
```bash
git clone https://github.com/jolbinsk1/count_unique_words.git
```

2) Download the English Words List:
- navigate to the following repository and download the words.txt file, which contains a comprehensive list of English words:
- https://github.com/dwyl/english-words/blob/master/words.txt

4) Move the words.txt File:

Move the downloaded words.txt file to your current working directory.

## Script Functions

The script contains several functions, each with a specific purpose:

`load_word_list()`: Loads the list of English words from words.txt.
`name_the_file()`: Prompts the user to enter a name for the new text file.
`get_input()`: Allows the user to input multiple lines of text.
`write_to_file(file_name, content)`: Writes the user-generated content to a file.
`count_words(file_name)`: Counts the total number of words in the file.
`count_unique_words(file_name, words_no_punc)`: Counts the unique words in the file, using the English words list for reference.

## How to Use

## Run the Script:

Execute the main.py script:

```bash
Copy code
python main.py
Follow the Prompts:

Enter a name for your new text file when prompted.
Input your text (you can enter multiple lines, and press Enter on a blank line to finish).
The script will write your input to the specified file, count the total number of words, and count the unique words, displaying the results in the console.

```
Example

Here's an example of using the script:

Run the script:

```bash
Copy code
python main.py
Enter a name for your text file, e.g., my_new_text_file.txt.

Enter your text (press Enter on a blank line to finish):
...
new line: Hello world
new line: Testing, one two.
new line:
The script will output:

...
Your file 'my_text_file.txt' contains 5 words.

Unique words and their counts:

hello: 1
world: 1
testing: 1
one: 1
two: 1
```

## Files

- `main.py`: The main script to run.
- `word_counter_functions.py`: Contains the functions used by the main script.
- `words.txt`: The comprehensive list of English words (downloaded separately).
