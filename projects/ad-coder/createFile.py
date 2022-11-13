import os

print('問題の番号を入力してください。例)abc085_c >>>', end="")

contest, task = input().split('_')

create_dir_path = f'{os.getcwd()}/src/{contest}'

if not os.path.isdir(create_dir_path):
  os.mkdir(create_dir_path)

create_file_path = f'{create_dir_path}/{task}.py'

if not os.path.isfile(create_file_path):
  with open(create_file_path, 'w') as new_file:
    header_text = f'# https://atcoder.jp/contests/{contest}/tasks/{contest}_{task}'
    new_file.write(header_text)
