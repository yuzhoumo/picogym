def decode(message):
    res = []
    for n in message:
        n %= 37
        if n == 36:
            res.append('_')
        elif (n>=26) and (n<=35):
            res.append(str(n-26))
        else:
            res.append(chr(ord('A') + n))
    
    return ''.join(res)


with open('message.txt', 'r') as f:
    message = [int(w) for w in f.read().strip().split()]
    print(message)
    print('picoCTF{'+decode(message)+'}')
