import toesc.english as eng

string = input('string : ')
for char in string:
    print(ord(char), hex(ord(char)))

eng.end_process()