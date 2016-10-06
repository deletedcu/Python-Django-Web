

import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]

 # 1 All Words that contain v
print(get_matching_words(r'.*v'))
print
#2 All words that contain a double-"s"
print(get_matching_words(r's{2}'))
print
#3 all words that end with an "e"
print(get_matching_words(r'e$'))
print
#4 all words that contain a 'b' and any than another'b'
print(get_matching_words(r'b.b+'))
print(get_matching_words(r'b\wb+'))
print
#5 all words that contain a 'b' at least one character any than another'b'
print(get_matching_words(r'b.*b'))
print
#6 all words that contain a 'b' any number of character (including zero) than another b
print(get_matching_words(r'b{0}b'))
print
# 7 All words that incldes the five vowell in order
print(get_matching_words(r'a.*e.*i.*o.*u.*'))
print
#8 All words that only use the letter in Regular Expression <- Could not come uo with th answer
print(get_matching_words(r'.*r.*e.*g.*u.*l.*a.*x.*p.*r.*s.*i.*o.*n'))

#9 All words that contain a double letter<- Could not come uo with th answer
print(get_matching_words(r'\w{0,}\w'))
print
