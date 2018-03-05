def accountment(a,b):
    if '-' in a or '-' in b:
      a = a.replace('-', '')
      b = b.replace('-', '')
      #
      new_a = make_max_number(a)
      new_b = make_max_number(b)
      #
      if (int(new_a) + int(new_b) > int(new_b) + int(new_a)):
        return int(new_a) + int(new_b)
      else: return int(new_b) + int(new_a)
    else:
      #
      new_a = make_max_number(a)
      new_b = make_max_number(b)
      #
      if (int(new_a) - int(new_b) > int(new_b) - int(new_a)):
        return int(new_a) - int(new_b)
      else: return int(new_b) - int(new_a)
      #
      print(int(a), int(b))

def make_max_number(number):
  temp_number = []
  for symbol in number:
    temp_number += symbol
    temp_number.sort(reverse=True)
  return ''.join(temp_number)
  
a = input()
b = input()
print(accountment(a,b))
