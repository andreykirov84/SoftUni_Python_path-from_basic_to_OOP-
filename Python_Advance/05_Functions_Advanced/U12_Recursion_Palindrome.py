# Solution without recursion
# def palindrome(word, index=0):
#     if word == word[::-1]:
#         return f"{word} is a palindrome"
#     else:
#         return f"{word} is not a palindrome"

# Solution with recursion
def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"
    elif word[idx] != word[len(word) - 1 - idx]:
        return f"{word} is not a palindrome"
    return palindrome(word, idx + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))

