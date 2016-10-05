#regex commands

#All words that contain a “v”
	re.search(r"v.*", word)
#All words that contain a double-“s”
	re.search(r"ss.*", word)
#All words that end with an “e”
	re.search(r"e$", word)
#All words that contain an “b”, any character, then another “b”
	re.search(r"b.b", word)
#All words that contain an “b”, at least one character, then another “b”
	re.search(r"b..*b", word)
#All words that contain an “b”, any number of characters (including zero), then another “b”
	re.search(r"b.*b", word)
#All words that include all five vowels in order
	re.search(r"a.*e.*i.*o.*u", word)
#All words that only use the letters in “regular expression” (each letter can appear any number of times)
	re.search(r"^[regulaxpsion]+$", word)
#All words that contain a double letter
	re.search(r"(.)\1", word)