palabra=input('Word: ')
letra=input('Letter to count: ')


def count(word,letter):
    count = 0
    for letter in word:
            if letter == letra:
                count = count + 1
    print(count)

count(palabra,letra)
    
