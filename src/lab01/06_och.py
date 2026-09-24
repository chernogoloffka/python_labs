n = int(input())
ochniy = 0
zaochniy = 0
for _ in range(n):
    line = input().split()
    form = line[-1]          
    if form == 'True':
        ochniy += 1
    else:
        zaochniy += 1
print(ochniy, zaochniy)