def center_point(x1, y1, x2, y2):
    result = []
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        if x1 < y1:
            result.append(x1)
            result.append(y1)
        else:
            result.append(y1)
            result.append(x1)
    else:
        if x2 < y2:
            result.append(x2)
            result.append(y2)
        else:
            result.append(y2)
            result.append(x2)
    formatted_result = '(' + str(result[0]) + ', ' + str(result[1]) + ')'
    return formatted_result


print(center_point(int(input()), int(input()), int(input()), int(input())))
