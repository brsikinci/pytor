from collections import deque


def encode(data):
    if isinstance(data, int):
        return b"i" + str(data).encode() + b"e"


def decode(data):
    if not isinstance(data, deque):
        tokenizedData = deque(data)
    else:
        tokenizedData = data
    token = tokenizedData.popleft()

    if token == "i":
        token = tokenizedData.popleft()
        num = ""
        while token != "e":
            num += token
            token = tokenizedData.popleft()
        print(num)
        return int(num)

    elif token == "l":
        token = tokenizedData.popleft()
        list = []
        while token != "e":
            tokenizedData.append(token)
            list.append(decode(tokenizedData))
            token = tokenizedData.popleft()
        return list

    elif token == "d":
        token = tokenizedData.popleft()
        dict = {}
        while token != "e":
            tokenizedData.append(token)


print(decode(b"i42e"))
