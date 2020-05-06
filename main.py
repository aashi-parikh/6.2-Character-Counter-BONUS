char_string = "The sky above the port was the color of television, tuned to a dead channel."



def char_counter(my_string):
    '''takes in a string, my_string and creates a dictionary that counts the number of times each character appears in my_string. Returns the created dictionary'''
    counter_dict = {}
    for char in my_string:
    	if char.lower() in counter_dict:
    		counter_dict[char.lower()] += 1
    	else:
    		counter_dict[char.lower()] = 1
    return counter_dict

print(char_counter(char_string))

def traverse_keys(dictionary):
	keys_list = []
	for key in dictionary.keys():
		keys_list.append(key)
	return keys_list

print(traverse_keys(char_counter(char_string)))

def traverse_values(dictionary):
	values_list = []
	for value in dictionary.keys():
		values_list.append(dictionary[value])
	return values_list

print(traverse_values(char_counter(char_string)))

def tuple_converter(dictionary):
	list_tuple = []
	vals = traverse_values(char_counter(char_string))
	keys = traverse_keys(char_counter(char_string))
	for i in range(len(dictionary)):
		tuple = (keys[i], vals[i])
		list_tuple.append(tuple)
		
	return list_tuple
	
print(tuple_converter(char_counter(char_string)))

	
# Test your program.

# Create a docstringbelow.

# Pass the docstring into char_counter 
# and print the return value.