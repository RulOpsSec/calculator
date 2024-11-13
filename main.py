from sum import *
from subtract import *
from multiply import *
from divide import *
from advanced_sum import *


while True:
    print()
    print('*****Open Source Calculator*****')
    print('         + Sum      ')
    print('         - Subtract ')
    print('         * Multiply ')
    print('         / Divide   ')
    print('        ++ Advanced Sum')
    print('********************************')
    print()
    opt = str(input(' Option: '))
    print()

    match opt:
        case "+":
            sum()
        case "-":
            sub()
        case "*":
            mult()
        case "/":
            div()
        case "++":
            adv_sum()
        case "_":
            print('Unkown Option')
            break