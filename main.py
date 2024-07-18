from word_counter_functions import (
  load_word_list,
  name_the_file,
  get_input,
  write_to_file,
  count_words,
  count_unique_words
)

def main():
    english_words = load_word_list()
    file_name = name_the_file()
    content = get_input()
    write_to_file(file_name, content)
    word_count = count_words(file_name)
    unique_word_count = count_unique_words(file_name, english_words)
    
    print(f"\nYour file '{file_name}' contains {word_count} words.")
    print('\n'+'Unique words and their counts: ')
    print('\n')
    for word, count in unique_word_count.items():
        print(f"{word}: {count}")

  if __name__ == "__main__":
    main()
