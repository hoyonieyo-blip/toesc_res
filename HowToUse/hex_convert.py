import toesc.english as eng, typeinput as ti

# 일단 처음에 모드 판별 | Determine the mode first
MODE = ti.intinput(
    'mode\n'
    '1 : encode\n'
    '2 : decode\n'
    '> '
)

# 인코딩 | Encoding
if MODE == 1:
    alpha = input('string : ')

    # 두 개 만들고 둘 다 출력 | Create two outputs and print both
    bravo = bytes.hex(alpha).upper()
    charlie = ''
    for part in alpha:
        charlie += (
            part
                .encode()
                .hex()
                .upper()
         ) + ' '

    print(bravo)
    print(charlie)

# 디코딩 | Decoding
elif MODE == 2:
    alpha = input('string : ')

    # bytes.hex() : 16진수로 만들기 | bytes.hex() : Convert to hexadecimal
    # bytes.fromhex() : 16진수를 문자열로 | bytes.fromhex() : Convert hexadecimal to a string
    bravo = alpha.encode().fromhex().decode()

    print(bravo)

# 아니면 오류 | Otherwise, raise an error
else:
    raise ValueError(
        'mode %s is not defined' % MODE
    )

eng.end_process()
