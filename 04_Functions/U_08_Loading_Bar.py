def loading_bar(percents):
    result = percents + '%'
    level = int(int(percents) / 10)
    if level == 10:
        result += ' Complete!\n'
        result += '['
        for _ in range(level):
            result += '%'
        result += ']'

    else:
        result += ' ['
        for _ in range(level):
            result += '%'
        for _ in range(10 - level):
            result += '.'
        result += ']\nStill loading...'

    return result


print(loading_bar(input()))
