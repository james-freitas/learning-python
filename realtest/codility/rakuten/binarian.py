import math


def binarian(array_input):
    sum_elements_powered = sum([pow(2, x) for (x) in array_input])

    base_exponent = math.trunc(math.sqrt(sum_elements_powered))

    powered_second = pow(2, base_exponent)
    result = 1
    counter = base_exponent - 1

    while powered_second != sum_elements_powered:
        powered_second += pow(2, counter)

        if powered_second <= sum_elements_powered:
            result += 1
        else:
            powered_second -= pow(2, counter)
        counter -= 1

        pass
    return result

userInput = [0, 2, 2, 0, 0, 1]

print binarian(userInput)



