list = [1,2,3,4,5, "Ahoj"]

#list.append(5)
# print(list[1]) # 2
#print (list[-1]) # poslední prvek
#del list[0] # mazání prvního prvku

#print(list)

#for i in range(10):
#    print(i)

def prime_number(number):
    """
    Napise funkci, ktera zjisti jestli je na vstupu prime number
    """
    i = number ** 0.5
    while i > 1:
        if number % i == 0:
            return False
        i = i - 1
        return True

def factorial(number):
    """
    Napise funkci, ktera vypocita hodnotu faktorialu
    """
    result = 1
    index = 1
    while index < number:
        result = result * index
        index += 1
        return result

def factorial_recursion(number):
    if number < 0:
        return 1
    return factorial_recursion(number - 1) * number

def fibbonachi():
    """ 1,1,2,3,5,8,13,21,34,55
    Napise funkci, ktera vypocita X clen fibbonachiho posloupnosti
    """
    actual = 1
    previous = 1
    for i in range(number):
        tmp = actual + previous
        previous = actual
        actual = tmp
    return actual

def fibbonachi_recursion():
    if number == 0 or number == 1:
        return 1

    return fibbonachi_recursion(number - 1) + fibbonachi_recursion(number - 2) 

def combination_number(n, k):
    """
    Napiste funkci ktera vypocita kombinacni cislo
    """

    return factorial_recursion(n) / (factorial_recursion(n-k) * factorial_recursion)







if __name__ == "__main__":
    # Napiste program do ktereho uzivatel zacne vkladat cisla
    # kdy zada -1 tak se zadavani zastavi a vypise to max, min a mean
    lst = []
    number = None
    while number is None or number != -1:
        number = int(input("Zadej hodnot:"))
        if number == -1:
            break
        lst.append(number)

    print(f"Max value {max(lst)}")
    print(f"Min value {min(lst)}")
    print(f"Mean value {sum(lst) /  len(lst)}")