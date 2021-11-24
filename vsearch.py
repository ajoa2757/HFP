def search_for_letters(phrase:str, letters:str = 'aeiou') -> set:
    letters_set = set(letters)
    return letters_set.intersection(set(phrase))



    
         
       
