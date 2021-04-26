import math


def rad_to_deg_converter(radian):
    deg = math.floor(radian * 180 / math.pi)
    return deg


number = float(input())
print(rad_to_deg_converter(number))