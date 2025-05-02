import keyboard as k, time as t, pyautogui as py

active = False

def toggle(e):
    global active

    active = not active
    print(f'Condicao = {active}')

def auto():
    while True:
        if active:
            while active:
                k.press("Shift")
                k.press_and_release("a") or k.press_and_release("b") or k.press_and_release("c") or k.press_and_release("d") or k.press_and_release("e") or k.press_and_release("f") or k.press_and_release("g") or k.press_and_release("h") or k.press_and_release("i") or k.press_and_release("j") or k.press_and_release("k") or k.press_and_release("l") or k.press_and_release("m") or k.press_and_release("n") or k.press_and_release("o") or k.press_and_release("p") or k.press_and_release("q") or k.press_and_release("r") or k.press_and_release("s") or k.press_and_release("t") or k.press_and_release("u") or k.press_and_release("v") or k.press_and_release("w") or k.press_and_release("x") or k.press_and_release("y") or k.press_and_release("z")
                k.release("Shift")
                k.press_and_release("0") or k.press_and_release("1") or k.press_and_release("2") or k.press_and_release("3") or k.press_and_release("4") or k.press_and_release("5") or k.press_and_release("6") or k.press_and_release("7") or k.press_and_release("8") or k.press_and_release("9")
                t.sleep(0.1)
        else:
            ()

k.on_press_key('F4', toggle)
auto()

