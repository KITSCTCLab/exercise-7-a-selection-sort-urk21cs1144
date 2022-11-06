from typing import List

def selectionSort(array, size) -> List[int]:  
  for indexo in range(size-1):
    small_index = indexo
    for index in range(indexo + 1,size):
      if array[index] < array[small_index]:
        small_index = index
    array[indexo], array[small_index] = array[small_index], array[indexo]
  return array     
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
