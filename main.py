def reverse():
    word = list(input("Enter the word to be reversed."))
    rev = []
    for i in range(len(word) -1):
        if len(word) != 1:
            rev.append(word.pop(-1))
        if len(word) == 1:
            rev.append(word.pop(0))

    rev = ''.join(rev)
    print(rev)

reverse()

# list = [1, 2, 3, 4]
# list = [1]