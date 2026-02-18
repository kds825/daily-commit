import os

#현재 폴더 내 txt 파일 쓰기
with open('sample.txt', 'w') as f:
    f.write('Hello, world!')

#현재 폴더 내 txt 파일 읽기
with open('sample.txt', 'r') as f:
    content = f.read()
    print(content)
    
