def count_repeat_symbols(string):
    char_list = list(string)
    char_set = set(char_list)
    char_count = list()
  
    for char in char_set:
        char_count.append(string.count(char))
  
    char_count.sort()
    char_count.reverse()
    char_count = char_count[0:3]
  
    char_new_list = list()
    for char in char_set:
        if char_list.count(char) in char_count:
            char_new_list.append(char)
  
    char_new_list.sort()
  
    for char in char_new_list:
        print (char, char_list.count(char))

string = input()
print(count_repeat_symbols(string))


