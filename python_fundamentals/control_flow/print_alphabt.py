#!/usr/bin/python3  


for letter in "abcdefghijklmnopqrstuvwxyz":
	if letter != 'e' and letter != 'q':
		print(letter, end="\n" if letter == 'z' else "")
