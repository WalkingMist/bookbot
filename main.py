def read_file(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def count_alphabet_frequency(text_to_be_counted):
  alphabet_freq_counter = {}

  for character in text_to_be_counted:
    if(character in alphabet_freq_counter):
      alphabet_freq_counter[character] += 1
    else:
      alphabet_freq_counter[character] = 1

  return alphabet_freq_counter

def count_words(text_to_be_counter):
  tokens = text_to_be_counter.split()
  return len(tokens)

def main():
  book_path = "books/frankenstein.txt"
  book_text = read_file(book_path)
  word_count = count_words(book_text)
  alpha_freq = count_alphabet_frequency(book_text.lower())

  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document")
  print()
  for key in alpha_freq.keys():
    if(key.isalpha()):
      print(f"The '{key}' character was found {alpha_freq[key]} times")

  print("--- End report ---")

main()