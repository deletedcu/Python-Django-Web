import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    return [word for word in words if re.search(regex, word)]

# 1. All words that contain a 'v'
print get_matching_words(r"v")
# 2. All words that contain a double-'s'
print get_matching_words(r"ss")
# 3. All words that end with an 'e'
# note to self: the '\w*' allows word characters in front of "e" and the '\b' ensures that "e" is at the end of the word
# remember that the '*' indicates that the pattern preceeding the '*' can appear any number of times, including none
#########print get_matching_words(r"\w*e\b")
# the '$' indicate end of a word
print get_matching_words(r"e$")
# 4. All words that contain a 'b', any character, then another 'b'
print get_matching_words(r"b.b")
# 5. All words that contain a 'b', at least one character, then another 'b'
print get_matching_words(r"b.+b")
# 6. All words that contain a 'b', any number of characters(including zero), then another 'b'
print get_matching_words(r"b.*b")
# 7. All words taht include all five vowels in order
print get_matching_words(r"a.*e.*i.*o.*u.*") #this is returning sacrilegious which follows trend but also doesn't

# 8. All words that only use the letters in 'regular expression' (each letter can appear any # of times)
# \b  --> Assert position at a word boundary
# [regularexpression] --> Match a single character present in the list 'regularexpression'
# + --> BEtween one and unlimited times, as many times as possible, giving back as needed (greedy)
# \b --> Assert position at a word boundary
# (?! --> Assert that it is impossible to match the regex below starting at this position (negative lookahead)
# [,] --> Match the character ','
# )
########print get_matching_words(r"\b[regularexpression]+\b(?![,])")
# '^' matches at the beginning of the string and '$' matches end
# '[]' used to indicate a set of characters. Characters can be listed individually, e.g. [amk] will match 'a', 'm', or 'k'
# '+' ensures that any of those letters we're searching for can be repeated any number of times (as opposed to only once)
print get_matching_words(r"^[regulaxpsion]+$")

# 9. All words that contain a double letter
# the below looks for '.' as a group, denoted by the () and sees if it's repeated one more time by the \1
print get_matching_words(r"(.)\1")
