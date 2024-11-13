def adv_sum ():
    t = 0

    while True:
        x = int(input(' n: '))
        t += x

        if x == 0:
            break

        print(f' Total: {t}')
    return t