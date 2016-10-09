import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]

print get_matching_words(r'v')
print get_matching_words(r's{2}')
print get_matching_words(r'b.*e\b')
print get_matching_words(r'b.b')
print get_matching_words(r'b..*b')
print get_matching_words(r'b+')
print get_matching_words(r'a.*e.*i.*o.*u')
print get_matching_words(r'^[regulaxpsion]+$')
print get_matching_words(r'(.)\1')
