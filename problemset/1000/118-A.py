w = input("")
vowels = 'aoyeui' #why is Y a vowel???????????????????
res = ''

for i in range(len(w)):
    if w[i].lower() not in vowels:
        res += '.'
        res += w[i].lower()

print(res)
