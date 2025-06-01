# count words

def get_num_words(file_contents):
    word_split = file_contents.split()
    word_count = len(word_split)
    return word_count

# count letters

def get_num_characters(file_contents):
    
    character_dict = {}
    character_list = []

    for i in range(0,len(file_contents)): #adds letters to list
        character_list.append(file_contents[i].lower())
    for letter in character_list: #adds list to dictionary
        if letter not in character_dict:
            character_dict[letter] = 1 
        elif letter in character_dict: #increases character count
            character_dict[letter] += 1
    return character_dict

# create sort key

def sort_on(dict):
    return dict["num"]

# create sorted list of dictionaries

def sort_characters(character_dict):
    
    dictionary_list = []
    
    for letter in character_dict:
        sorted_dict = {"char": None, "num": None}
        sorted_dict["char"] = letter
        sorted_dict["num"] = character_dict[letter]
        dictionary_list.append(sorted_dict)
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
    
        