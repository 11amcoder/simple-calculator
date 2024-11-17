print('-'*80)
print("                                   CALCULATOR                                   ")
print("-"*80)

while True:
    try:
        user = float(input("Enter a number: ")) 
        op = input("Choose the operator: ['add','sub','div','mod','mul','xor','exp']:  ")

        if op not in ("xor" , "add" , "exp" , "sub" , "div" , "mod" , "mul") or (user < 0 and op == "xor"):
            print("Invalid Operator! Please choose a valid operator from ['add','sub','div','mod','mul','xor','exp']: ")
            continue  

        numb = float(input("Enter another number: "))

        if op == "xor" and (user <0 or numb < 0):
            print("Please enter positive valid number for bitwise XOR operation: ")
            continue
        break
    
    except ValueError:
        print("Please enter valid number:  ")

    
user = int(user)
numb = int(numb)



usercopy = user
numbcopy = numb

addition = user + numb
subtraction = user - numb
multiplication = user * numb
division = user/numb
mod = user % numb
exp = abs(user) ** abs(numb)

if op == "add":
    print(addition)
elif op == "sub":
    print(subtraction)
elif op == "div":
    print(division)
elif op == "mul":
    print(multiplication)
elif op == "mod":
    print(mod)
elif op == "exp":
    print(exp)

bin = []
while True:
    rem = int(user%2)
    bin.append(rem)
    user = int(user/2)
    if user == 0:
        break

bin.reverse()
binary_string1 = ''.join(map(str,bin))


bin2 = []
while True:
    rem2 = int(numb%2)
    bin2.append(rem2)
    numb = int(numb/2)
    if numb == 0:
        break

bin2.reverse()
binary_string2 = ''.join(map(str,bin2))


max_binary_length = max(len(binary_string1),len(binary_string2))
binary_string1_padding = binary_string1.zfill(max_binary_length)
binary_string2_padding = binary_string2.zfill(max_binary_length)

if op == "xor":
    print(f"Binary conversion for {usercopy} is {binary_string1_padding}") #this is string
    print(f"Binary conversion for {numbcopy} is {binary_string2_padding}") #this is string


newbitwisebin = []

for x1, x2 in zip(binary_string1_padding,binary_string2_padding):
    x1 = int(x1)
    x2 = int(x2)

    if x1 == x2:
        newbitwisebin.append(0)
    elif x1 != x2:
        newbitwisebin.append(1)




decimal_number = 0
length = len(newbitwisebin)


for x in range(length):
    decimal_number += newbitwisebin[x] * (2 ** (length-1-x))
if op == "xor":
    print(f"Based on XOR Truth Table, binary number for {binary_string1_padding} and {binary_string2_padding} is {newbitwisebin}")
    print(f"After the XOR operation, decimal number which is equal to {newbitwisebin} is {decimal_number}")
