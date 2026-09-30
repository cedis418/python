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

if __name__ == "__main__":
    str_time = input("Zadej cas v S:")
    time = int(str_time)

    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = time % 60

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")