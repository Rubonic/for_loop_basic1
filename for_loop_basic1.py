# For Loops: Basic 1

# 1.Basic
for x in range(151):
    print(x)

# 2 Multiples of Five
for x in range(5,1001,5):
    print(x)

# 3 Counting, the Dojo Way
for x in range(1,101):
    if x % 10 == 0:
        print('Coding Dojo')
        continue
    if x % 5 == 0:
        print("Coding")
        continue
    else:
        print(x)

# 4. Whoa. That Sucker's Huge
sum = 0
for x in range(0, 500000):
    if x % 2 != 0:
        print(x)
        sum = sum + x
print(sum)
        

# 5. Countdown by Fours
for x in range(2018,0,-4):
    print(x)

# 6. Flexible Counter
lowNum = 7
highNum = 20
mult = 4

for x in range(lowNum,highNum+1):
    if x % mult == 0:
        print(x)

