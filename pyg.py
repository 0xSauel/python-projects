#!/usr/bin/python2

pyg = "ay~"
original = raw_input('Enter your word to translate: ')

if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	new_word = word + first + pyg
	print new_word[1:len(new_word)
else:
	print "Enter any real word."
