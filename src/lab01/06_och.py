n = int(input("in_1:"))
ochniy = 0
zaochniy = 0
for i in range(n):
    line = input(f"in_{i + 2}:").split()
    form = line[-1]
    if form == 'True':
        ochniy += 1
    else:
        zaochniy += 1
print("out:", ochniy, zaochniy)