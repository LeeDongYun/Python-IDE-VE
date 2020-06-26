import os

try: 
    with open('c:/work/pyfile.txt', mode='w')as file:
        file.write('파일 이름 수정과 삭제')

    os.rename('c:/work/pyfile.txt','파일수정삭제.txt')
    os.remove('./파일수정삭제.txt')
except Exception as e:
    print('예외 발생: ',e)
else:
    print('파일 수정 삭제 성공!')

dname = os.getcwd()
print('현재 폴더:', dname)

fs = os.listdir(dname)
for f in fs:
    if os.path.isfile(f):
        print('\t파일',f)
    elif os.path.isdir(f):
        print('\t폴더:',f)