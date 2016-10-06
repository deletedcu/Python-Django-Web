import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", 
 	"belladonna", "cannonball", "crybaby", "denver", "embraceable", 
 	"facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", 
 	"issue", "kebab", "kilo", "laundered", "mattress", "millennia", 
 	"natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", 
 	"sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 return [word for word in words if re.search(regex, word)]

print '1', get_matching_words(r"v")
print '2', get_matching_words(r"s{2}")
print '3', get_matching_words(r"e$")
print '4', get_matching_words(r"b*b")
print '5', get_matching_words(r"b.b")
print '6', get_matching_words(r"b+")
print '7', get_matching_words(r"a.*e.*i.*o.*u.*")
print '8', get_matching_words(r"r|e|g|u|l|a|r|e|x|p|r|e|s|s|i|o|n")
print '9', get_matching_words(r"(.)\1")

