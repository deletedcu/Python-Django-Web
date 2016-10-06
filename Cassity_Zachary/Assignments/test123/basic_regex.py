import re

def get_matching_words():
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
 print [word for word in words if re.search(r'.*v',word)] #1
 print [word for word in words if re.search(r'.*ss',word)] #2
 print [word for word in words if re.search(r'.*e$',word)] #3
 print [word for word in words if re.search(r'.*b.b',word)] #4
 print [word for word in words if re.search(r'.*b.+b',word)] #5
 print [word for word in words if re.search(r'.*b.*b',word)] #6
 print [word for word in words if re.search(r'.*a.*e.*i.*o.*u',word)] #7
 print [word for word in words if re.search(r'^[regularxpsion]+$',word)] #8
 print [word for word in words if re.search(r'.*v',word)] #9
get_matching_words()
