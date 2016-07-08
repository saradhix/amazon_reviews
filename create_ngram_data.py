import json
import sys
import math
import re
import string

def process_review_text(review):
  chars_to_replace = ['!','?']
  review = string.replace(review, '!', '.')
  review = string.replace(review, '?', '.')
  review = string.replace(review, "'", '')
  review = string.replace(review, "(", '')
  review = string.replace(review, ")", '')
  review = string.replace(review, "@", '')
  review = string.replace(review, "$", '')
  review = string.replace(review, "%", '')
  review = string.replace(review, "^", '')
  review = string.replace(review, "&", '')
  review = string.replace(review, "-", '')
  review = string.replace(review, "=", '')
  review = string.replace(review, "*", '')
  review = string.replace(review, "+", '')
  review = string.replace(review, "-", '')
  review = review.strip()
  review = review.lower()
  review = re.sub('\d+','', review)
  review = re.sub(' +',' ', review)
  return review

def process_words(words):
  stop_words=['a','an','the', 'i', 'as', 'is', 'to', 'in', 'with','for','it',
    'and', 'off', 'my','your', 'which', 'of']
  for word in words:
    if word in stop_words:
      words = filter(lambda a: a!=word, words) #Remove all occurences of the stop word
  return words

def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

filename = 'reviews_Cell_Phones_and_Accessories_5.json'

num_grams = 4

fp = open(filename, 'r')
max_num_words = 0
min_num_words = 5000

#Process each line in the file
for line in fp:
  json_obj = json.loads(line)
  #print json_obj
  review_text = json_obj['reviewText']
  overall = json_obj['overall']

  review_text = process_review_text(review_text)
  sentences = review_text.split('.')
  #Process each sentence in the review
  for sentence in sentences:
    sentence = sentence.strip()
    if len(sentence) == 0: continue
    #print "Sentence = ", sentence
    words = sentence.split(' ')
    words = process_words(words)
    num_words = len(words)
    if num_words == 0: continue
    if max_num_words < num_words:
      max_num_words = num_words
    if min_num_words > num_words:
      min_num_words = num_words

    if num_words < num_grams:
      factor = int(math.ceil(num_grams / num_words))
      temp_words = []
      for i in range(factor):
        temp_words.extend(words)
      words = temp_words
      #print words

    ngrams = find_ngrams(words, num_grams)
    #print ngrams
    for ngram in ngrams:
      print ngram, overall
sys.exit()


print "Max num words", max_num_words
print "Min num words", min_num_words

sys.exit()
