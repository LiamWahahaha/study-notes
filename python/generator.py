def index_word(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

def main():
    address = 'Four score and seven years ago...'
    result = index_word(address)
    print(result)

    result = list(index_words_iter(address))
    print(result)

if __name__ == '__main__':
    main()
