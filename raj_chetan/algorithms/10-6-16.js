# Parentheses Valid

function ParensValid(str){
	var open = 0;
	var close = 0;
	for (var i = 0; i < str.length; i++){
		switch(str[i]){
			case '(':
				open += 1;
				break;
			case ')':
				close += 1;
				break;
		}
		if (close > open){
			return false
		}
	}
	if (open == close){
		return true;
	}
	else{
		return false;
	}
}

# Braces Valid

function bracesValid(str){
	var open_par = 0;
	var open_curl = 0;
	var open_square = 0;
	var close_par = 0;
	var close_curl = 0;
	var close_square = 0;
	for (var i =0; i<str.length; i++){
		switch (str[i]){
			case '(': open_par +=1; break;
			case '{': open_curl +=1; break;
			case '[': open_square +=1; break;
			case ')': close_par +=1; break;
			case '}': close_curl +=1; break;
			case ']': close_square +=1; break;
		}
	}
	if(open_par == close_par && open_curl == close_curl && open_square == close_square){
		return true;
	}
	else{
		return false;
	}
}