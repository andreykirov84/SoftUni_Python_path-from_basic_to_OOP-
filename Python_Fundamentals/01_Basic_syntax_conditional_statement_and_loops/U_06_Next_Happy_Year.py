def check_if_duplicates(list_of_elements):
    """ Check if given list contains any duplicates """
    if len(list_of_elements) == len(set(list_of_elements)):
        return False
    else:
        return True


number = int(input())

while check_if_duplicates(list(str(number))):
    number += 1

print(number)
