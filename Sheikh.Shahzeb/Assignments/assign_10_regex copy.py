import re
def get_matching_words():
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
	print [word for word in words if re.search(r".*v", word)]
	print [word for word in words if re.search(r".*ss", word)]
	print [word for word in words if re.search(r"e$", word)]
	print [word for word in words if re.search(r".*b.*b", word)]
	print [word for word in words if re.search(r".*b.b", word)]
	print [word for word in words if re.search(r".*b.*b", word)]
	print [word for word in words if re.search(r"\a\e\i\o\u", word)]
	print [word for word in words if re.search(r".r.e.g.u.l.a.r .e.x.p.r.e.s.s.i.o.n", word)]
	print [word for word in words if re.search(r"\w\w", word)]







get_matching_words()