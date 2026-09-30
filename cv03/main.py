# aritmicke op.

## and or
# prirazovaci
## =, +=, -=, *=, /=
# bitovy
## &, |, ^, <<, >>, ~

# A = 0b10100111
# B = 0b10011010
 
# A & B = 0b10000010
# A | B = 0b10111111
# A ^ B = 0b00111101
# ~A = 0b01011000
# A << 4 = 0b01110000
# B >> 4 = 0b00001001

## Nactete INT ze vstupu a naformatujte ho na hh:mm:ss

## 360 -> 00:06:00
"""
if __name__ == "__main__":
    str_time = input("Zadej cas v S:")
    time = int(str_time)

    hour = time // 3600
    minut = (time % 3600) // 60
    second = (time % 3600) % 60

    print(f"{hour}:{minut}:{second}")
"""

if __name__ == "__main__":
    #Vytvorte automat, který vam rozmeni castku X na:
    # 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1      
    value = int(input("Zadej castku: "))
    money = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for item in money:
        x = value // item
        value = value - (x * item)
        print(f"{x} x {item}")
    
    print(f"{x_5000}x5000")
    print(f"{x_2000}x2000")
    print(f"{x_1000}x1000")
    print(f"{x_500}x500")
    print(f"{x_200}x200")
    print(f"{x_100}x100")
    print(f"{x_50}x50")
    print(f"{x_20}x20")
    print(f"{x_10}x10")
    print(f"{x_5}x5")
    print(f"{x_2}x2")
    print(f"{x_1}x1")
