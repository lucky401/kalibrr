import sys

sys.setrecursionlimit(999999999)

def binary_search(array, value, low, high):
  """
  Given a sorted array, find the index of the value in the array
  
  :param array: the array to search
  :param value: the value we're searching for
  :param low: The lowest index in the array that we're considering
  :param high: The highest index in the array
  :return: The index of the value in the array.
  """
    if high < low:
        return -1
    else:
        mid = (low + high)//2;
        if array[mid] > value:
            return binary_search(array, value, low, mid-1)
        elif array[mid] < value:
            return binary_search(array, value, mid+1, high)
        else:
            return mid

inputFile = open('binary_search_input.txt')
content = inputFile.readlines()

array = []
for i in range(10000):
  array.append(int(content[i]));

value = []
for i in range(10000):
  value.append(int(content[i+10000]));

for i in range(10000):
  answer = binary_search(array, value[i], 0, len(array)-1)
  with open('binary_search_output.txt', 'a') as f:
    f.write(str(answer) + '\n')
