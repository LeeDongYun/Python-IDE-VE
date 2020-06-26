try:
    data= int('3.67')
except Exception as e:
    print('예외발생 이름:{}'.format(type(e)))
    print('예외발생 이유:{}'.format(e))