def age_assignment(*args, **kwargs):
    result = {}
    for first_letter in kwargs.keys():
        for name in args:
            if first_letter in name:
                result.update({name:kwargs[first_letter]})

    return result


print(age_assignment("Peter", "George", G=26, P=19))