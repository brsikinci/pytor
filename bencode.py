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

    if token == ord("i"):
        token = tokenizedData.popleft()
        num = ""
        while token != ord("e"):
            num += chr(token)
            token = tokenizedData.popleft()
        return int(num)

    elif token == ord("l"):
        token = tokenizedData.popleft()
        list = []
        while token != ord("e"):
            tokenizedData.appendleft(token)
            list.append(decode(tokenizedData))
            token = tokenizedData.popleft()
        return list

    elif token == ord("d"):
        token = tokenizedData.popleft()
        dict = {}
        while token != ord("e"):
            tokenizedData.appendleft(token)
            key = decode(tokenizedData)
            dict[key] = decode(tokenizedData)
            token = tokenizedData.popleft()
        return dict

    elif chr(token) in "0123456789":
        strLength = int(chr(token))
        token = tokenizedData.popleft()
        if token != ord(":"):
            raise TypeError("Invalid input")
        str = ""
        for i in range(0, strLength):
            token = tokenizedData.popleft()
            str += chr(token)
        if len(str) != strLength:
            raise TypeError("Invalid input")
        return str

    raise TypeError("Invalid input")
