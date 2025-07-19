import hm_ascii_art as hm_module
import random

def get_random_word(word_list):
  """ This function returns a random string from the passed list of strings."""
  word_index = random.randint(0, len(word_list) - 1)
  return word_list[word_index]

# print(get_random_word(hm_module.words))

