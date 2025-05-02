import keyboard as k, time as t, pyautogui as py

t.sleep(5)

for i in range(9):
    k.press_and_release("backspace")
    k.write(") or k.press_and_release(")
    k.press_and_release("Delete")
    for i in range(4):
        k.press_and_release("Right")
