while True:
    try:
        number = int(input("Введите натуральное число: "))
        if number < 10**7:
            break
        print("Число должно быть меньше 10^7 (10,000,000). Попробуйте снова.")
    except ValueError:
        print("Ошибка: введите целое число! Попробуйте снова.")

def digit_root(num):    
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    if sum > 9:
        return digit_root(sum)
    return sum

print(digit_root(number))