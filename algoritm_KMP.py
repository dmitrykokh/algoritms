search_part = "лилила"

p = [0]*len(search_part) #вспомогательный массив
j = 0
i = 1

while i < len(search_part):
    if search_part[j] == search_part[i]:
        p[i] = j+1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

print(p)

a = "лилилось лилилась"
search_len = len(search_part)
example_len = len(a)

i = 0
j = 0
while i < example_len:
    if a[i] == search_part[j]:
        i += 1
        j += 1
        if j == search_len:
            print("образ найден")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1

if i == example_len and j != search_len:
    print("образ не найден")
