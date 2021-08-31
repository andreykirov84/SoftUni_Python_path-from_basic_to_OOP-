def recursive_power(number, power, counter=0):
    if counter == power:
        return
    number = number * number
    counter += 1
    recursive_power(number, power, counter)
    return number


print(recursive_power(2, 10))
