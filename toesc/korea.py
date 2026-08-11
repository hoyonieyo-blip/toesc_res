import keyboard as kb

def end_process():
    print('\n종료하려면 \'esc\'를 누르세요...', end='')
    kb.wait('esc')