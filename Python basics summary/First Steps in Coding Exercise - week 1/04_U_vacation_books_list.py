def literature(pages, pages_per_hour, days):
    result = pages / pages_per_hour / days
    return result


print(literature(int(input()), int(input()), int(input())))
