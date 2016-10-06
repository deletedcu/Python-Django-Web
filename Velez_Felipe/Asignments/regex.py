import re

def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

	return [word for word in words if re.search(regex, word)]

# all words that contain a "v"
print (get_matching_words(r'v'))

print ('\n')

# All words that contain a doble "s"
print (get_matching_words(r'ss'))

print ('\n')

# All words that end with an "e"
print (get_matching_words (r'.e$'))

print ('\n')

# All word that contain an "b", any character, then another "b"

print (get_matching_words (r'.*b.b'))

# All words that contain an "b", at least one caracter, then another "b"
print (get_matching_words (r'.*b.+b'))

print ('\n')

# All words that contain an "b", any number of characters (including zero), then another "b"
print (get_matching_words (r'.*b.*b'))

print ("\n")

# All words that include all five vowels in order
print (get_matching_words (r'.*a.*e.*i.*o.*u.*'))
print ("\n")
# All words that only use the letters in "regular expresion" (each letter can appear any number of times)
print (get_matching_words (r'^[regularexpresion]*$'))
print ("\n")
# all words that contain a double letter
print (get_matching_words (r'.*(.)\1.*'))