ex = ' vvalley the word for bo0000bby in assassin the aeiou regular regula'
import re
# re.search(pattern, string) finds the first thing that passes what you're looking for and stops there. you use print match.group() to see what you got
#re.findall(patter, string) finds all instances that match your search paramter and returns them in a list, use print [variable name] to see the list
match = re.search(r'v',ex)
# searches for the first instance of a single v
# if there is a v, it is stored inside match, this if statement checks if match is true or has anything in it, then you can print whatever match has with that function, if it was just one instance
match2 = re.findall(r's{2}',ex)
# searches for double s right next to each other, all instances, the curly braces specifically only searches for 2
match3 = re.findall(r'e\b',ex)
#searches for an e that is at the end of the word, the \b counts as the boundary between a world and non word so both a space and the end of the string can count, all instances
match4 = re.findall(r'b.b',ex)
# searches for a b with any character except a new line \n and another b. the period stands for any character except new line, all instances
match5 = re.findall(r'b.b',ex)
# the same thing as four
match6 = re.findall(r'b.*b',ex)
# searches for anything that has one b followed by any character besides new line(.) and any number of characters between the first b and a second b(*), all instances
match7 = re.findall(r'aeiou',ex)
# searches for the 5 vowels in order in any words
match8 = re.findall(r'[regula]+',ex)

match = re.findall(r'(.)\2',ex)
