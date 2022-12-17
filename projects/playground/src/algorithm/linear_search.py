# 線形探索
def linear_search(data, key):
  position = 0
  end = len(data) - 1
  steps = 1

  while position <= end:
    if data[position] == key:
      return steps, position
    
    steps += 1
    position += 1

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
  search('線形探索', data, linear_search)
  