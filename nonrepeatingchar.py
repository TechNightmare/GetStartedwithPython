#non repeating charachters

#In this task you should implement an algorithm which finds the first letter in a character
#sequence which is not repeating. This algorithmic problem is a typical problem which 
#can be solved in multiple ways. Some are easy to understand and some are complex 
#but very efficient. Maybe yours is efficient and also easy to understand?

def find_first_non_repeated_char(sequence: str):
    array = [0] * 256
    #using the ASCII value of the characters
    normsequence = sequence.lower()		#normalize the letters
    
    #count number of times the characters is used in string
    for character in normsequence:
    	array[ord(character)] += 1


    index = -1		#index of the non repeating character with -1 to handle special cases
    count = 0
    for character in sequence:
    	if character.isupper():
    		if (array[ord(character)+32] == 1):
    			index = count
    			break
    	else:
    		if(array[ord(character)] == 1):
    			index = count
    			break

    	count += 1
    
    if(index < 0):
    	return(None)
    else:
    	return(sequence[index])

    raise NotImplementedError