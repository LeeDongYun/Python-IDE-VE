lst = ['C/C++', 'JAVA', 'C#', 'python']

try:
    print(lst[0])
except Exception as e:
    print('에외 발생 이름:{}'.format(type(e)))
    print('예외 발생 이유:{}'.format(e))
else:
    print('잘 실행되었습니다')
finally:
    print('예외처리가 잘되는군요')