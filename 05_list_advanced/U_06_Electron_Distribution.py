electron_number = int(input())
result = []
shell = 1
while electron_number != 0:
    electron_per_shell = 2 * (shell ** 2)
    if electron_per_shell <= electron_number:
        result.append(electron_per_shell)
        electron_number -= electron_per_shell
        shell += 1
    else:
        result.append(electron_number)
        break

print(result)
