import keyboard as k, time as t, pyautogui as py

active = False
clique = k.press_and_release

def toggle(e):
    global active

    active = not active
    print(f'Condicao = {active}')

def auto():
    while True:
        if active:
            while active:
                k.press("Shift")
                clique("a") or clique("b") or clique("c") or clique("d") or clique("e") or clique("f") or clique("g") or clique("h") or clique("i") or clique("q") or clique("r") or clique("s") or clique("t") or clique("u") or clique("v") or clique("w") or clique("x") or clique("y") or clique("z") or clique("_")
                k.release("Shift")
                clique("0") or clique("1") or clique("2") or clique("3") or clique("4") or clique("5") or clique("6") or clique("7") or clique("8") or clique("9") or clique("-")
                t.sleep(0.1)
                clique("Tab")
                clique("Enter")
        else:
            ()

k.on_press_key('F4', toggle)
auto()
