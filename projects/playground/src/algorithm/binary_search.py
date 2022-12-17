def binary_search(data, key):
  start = 0
  end = len(data)  -1
  steps = 1

  while start <= end:
    middle = (start + end) // 2
    
    if data[middle] == key:
      return steps, middle
    elif data[middle] < key:
      start = middle + 1
    else:
      end = middle - 1
    
    steps += 1
  
  return steps, -1

def search(title, data, func):
  print(title)
  max_steps = 1
  
  for key in data:
    steps, pos = func(data, key)
    if max_steps < steps:
      max_steps = steps
    
    print("key:{} position:{} steps:{}".format(key, pos, steps))
  
  print("最大ステップ数:{}\n".format(max_steps))

if __name__ == '__main__':
  data = [1, 3, 7, 13, 17, 21, 74]
  length = len(data)
  print("探索データ:{}\n長さ:{}\n".format(data, length))
  search('二分探索', data, binary_search)
  