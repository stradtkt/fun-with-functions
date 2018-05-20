def odd_even():
  for i in range(1,2000):
    if i % 2 == 0:
      print("Number {}, This is an even number".format(i))
    elif i % 2 != 0:
      print("Number {}, This is an odd number".format(i))
odd_even()

def multiply(my_list, n):
  for i in range(0, len(my_list)):
    my_list[i] *= n
  return my_list

a = [2,4,10,16]
b = multiply(a, 5)
print(b)


def layered_multiples(my_list):
  final = []
  for x in my_list:
    added_list = []
    for i in range(0,x):
      added_list.append(1)
    final.append(added_list)
  return final

x = layered_multiples(multiply([2,4,5],3))
print(x)
