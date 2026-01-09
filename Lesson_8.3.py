m = int(input()) # Масса которую выдерживает лодка
n = int(input()) # Количество рыбаков
l = []

for i in range(n):
    l.append(int(input()))
    
l.sort()

left = 0
right = n - 1 
boats = 0   
    
while left <= right:
    if left == right:
        boats += 1
        break
    if l[left] + l[right] <= m:
        left += 1
        right -= 1
    else:
        right -= 1
    boats += 1

print(boats)                    