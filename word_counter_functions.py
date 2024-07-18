# to load the word list
def load_word_list():
    with open('words.txt', 'r') as f:
        english_words = set(word.strip().lower() for word in f)
    return english_words

# name the file you will use
def name_the_file():
    file_name = input('Please enter a name for your new text file: ')
    return file_name

# generate the text for your file
def get_input():
  
    # input text into the file (which allows you to enter multiple lines
    print("Enter your text (to stop, press enter when the box is blank):")
    lines = []
    
    while True:
        line = input('new line: ')
        if line == "":
            break
        lines.append(line)
    return '\n'.join(lines)

# add the text to the file
def write_to_file(file_name,content):
    with open(file_name,'w') as f:
        f.write(content)

# count the total words in the file
def count_words(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    words = content.split()
    return len(words)

# count the unique words
def count_unique_words(file_name, words_no_punc):
    with open(file_name, 'r') as f:
        content = f.read()
    words = content.split()

    # get rid of any punctuation
    words_no_punc = [word.lower().strip(".,!?\"'") for word in words]
    word_count = {}
    for word in words_no_punc:
    # Check if the word is in the list of English words
        if word in words_no_punc:  
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count





















