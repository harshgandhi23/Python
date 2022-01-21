#Program to print smallest positive missing number


var = int(input("NO. of elements :- "))
li = []
num = -1
for i in range(var):
    t = int(input())
    li.append(t)
for i in range(1, var+1):
    if i not in li:
        num = i
        break
if num <= var and num != -1:
    print("Output : ", num)
else:
    print("Output :", var+1)