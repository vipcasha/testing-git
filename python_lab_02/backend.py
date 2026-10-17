words_count = {}
text = input('Введите текст: ')
for i in ',:?.-': text = text.replace(i, '')
for i in text.split():
    words_count[i.lower()] = words_count.get(i.lower(), 0) + 1
print(len(words_count))

ask, res = input('Порядок (1 - убыв., 2 - возр.)'), 0

if ask == '2':
    new_sl = dict(sorted(words_count.items(), key=lambda x: x[1]))
    for key, value in new_sl.items():
        print(f'{key} - {value}')
        res += 1
        if res == 5:
            break
        
elif ask == '1':
    new_sl = dict(sorted(words_count.items(), key=lambda x: x[1])[::-1])
    for key, value in new_sl.items():
        print(f'{key} - {value}')
        res += 1
        if res == 5:
            break
            
