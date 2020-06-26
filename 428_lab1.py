while True:
    try:
        base = int(input('입력할 정수의 진수(base)는? [2, 8, 10, 16중의 하나]'))
        if not base in (2, 8, 10, 16):
            raise ValueError('2, 8, 10, 16 중의 하나를 입력하시오')
    except Exception as e:
        print('예외 발생 원인: %s\n' % e)
    else:
        print()
        break

chech  = {2:'01', 8:'01234567', 10:'0123456789', 16:'0123456789abcdefABCDEF'}
while True:
    try:
        invar = input(str(base))
        for dict in invar:
            if digit not in check[base]:
                raise ValueError('%진수를 입력하세요' % base)
    except Exception as e:
        print('예외 발생 원인: %s' % e)
    else:
        print()
        break
data = int(invar, base)

print('2진수',bin(data))
print('8진수',oct(data))
print('10진수',data)
print('16진수',hex(data))