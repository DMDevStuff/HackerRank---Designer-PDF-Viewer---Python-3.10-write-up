##    https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
##
##    There is a list of 26 character heights aligned by index to their letters.
##    For example, 'a' is at index 0 and 'z' is at index 25. There will also be a
##    string. Using the letter heights given, determine the area of the
##    rectangle highlight in mm**2 assuming all letters are 1mm wide.

##### ##### ##### #####

#   O(n)
#   n is the number of character in word.
#   Algo:
#   we iterate through the given word and for each character
#   we have to find its index in h. this could be done either by
#   implementing our own data structure or by using the built-in
#   ord().  ord() gives us the ascii index for our character in constant time,
#   which happens to be 97 higher than we want it, so we subtract 97.
#   This gives us the correct index in h for our character.
#   We then check its value against the largest value found so far
#   and store it if it is larger.  After checking every character
#   in word we find the area by multiplying the largest height found
#   by the length of the given word.

def designerPdfViewer(h, word):
    
    max_height = 0
    
    for character in word:
        
        character_index = ord(character) - 97
        
        if h[character_index] > max_height:
            
            max_height = h[character_index]
            
    return max_height * len(word)
