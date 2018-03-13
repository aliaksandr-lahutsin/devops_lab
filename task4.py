print('Enter person count: ')
s = int(input())
count = 0
m_count = 0
dictionary_list = {}
men_dictionary_list = []
while (count < s):
    print('The count is:', count)
    print('Enter person age: ')
    age = int(input())
    print('Enter person gender: ')
    dictionary_list.update({age: gender})
    count = count + 1
for age, gender in dictionary_list.items():
    if (gender == 1):
        men_dictionary_list.append(age)
    m_count += 1
    else:
        if (m_count == 0):
            print('-1')
m = max(men_dictionary_list)
counter = [i for i in range(
       len(men_dictionary_list)) if (men_dictionary_list[i] == m]
       ):
    print(counter)
