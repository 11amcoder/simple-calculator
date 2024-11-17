print('-'*80) #draws hyphen for 80 character spaces length
print("                                   CALCULATOR                                   ") #makes 10 characters of text "CALCULATOR" with 70 white spaces
print("-"*80)

while True:   #this loop runs untill the user enters valid number
    try:
        user = float(input("Enter a number: ")) 
        op = input("Choose the operator: ['add','sub','div','mod','mul','xor','exp']:  ")

        if op not in ("xor" , "add" , "exp" , "sub" , "div" , "mod" , "mul") or (user < 0 and op == "xor"):  #if user enters spelling mistake or anyother thing apart from the selection, then it asks to enter a proper option from the following again.
            print("Invalid Operator! Please choose a valid operator from ['add','sub','div','mod','mul','xor','exp']: ")
            continue         # and restart the loop again 

        numb = float(input("Enter another number: "))

        if op == "xor" and (user <0 or numb < 0):    #checks if operator is xor, and both the numbers are not negative
            print("Please enter positive valid number for bitwise XOR operation: ") #if improper, shows warning
            continue   #and restart the loop again
        break  #if user enters correct number and opreator, then loop breaks
    
    except ValueError:
        print("Please enter valid number:  ")   # in while loop, if user enters invalid number, it shows warning.

    
user = int(user) #converting to int
numb = int(numb) 



usercopy = user #copying the original input to use it later
numbcopy = numb

# Block of arithmetic operations
addition = user + numb
subtraction = user - numb
multiplication = user * numb
division = user/numb
mod = user % numb
exp = abs(user) ** abs(numb)

#conditions for arithmetic operations
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

#bitwise XOR operation starts
bin = []
while True:
    rem = int(user%2)  #getting remainder of the user input
    bin.append(rem)  #storing it somewhere to use it later
    user = int(user/2) #updating user input by diviision
    if user == 0:  #if user input has become 0, then the loop breaks as that's where we should stop while computing binary
        break

bin.reverse() #reverse the list
binary_string1 = ''.join(map(str,bin)) #convert it into strings


bin2 = []
while True:
    rem2 = int(numb%2)
    bin2.append(rem2)
    numb = int(numb/2)
    if numb == 0:
        break

bin2.reverse()
binary_string2 = ''.join(map(str,bin2))


max_binary_length = max(len(binary_string1),len(binary_string2))  #getting the maximum length of binary list
binary_string1_padding = binary_string1.zfill(max_binary_length) #padding up the empty slots with 0's
binary_string2_padding = binary_string2.zfill(max_binary_length)

if op == "xor":
    print(f"Binary conversion for {usercopy} is {binary_string1_padding}") #this is string
    print(f"Binary conversion for {numbcopy} is {binary_string2_padding}") #this is string


newbitwisebin = [] 

for x1, x2 in zip(binary_string1_padding,binary_string2_padding): #iterate through both the binary lists 
    x1 = int(x1)   #making them convert to integer from str
    x2 = int(x2)

    if x1 == x2:       #implementing the xor truth table logic, if both values have 0 or 1, then it will be 0
        newbitwisebin.append(0)
    elif x1 != x2:     #if both values have different values, then it will be 1
        newbitwisebin.append(1)



# Binary to number conversion
decimal_number = 0 
length = len(newbitwisebin) #calculating the length of binary number of xor

#iterates through all the elements of binary number
for x in range(length):
    decimal_number += newbitwisebin[x] * (2 ** (length-1-x))  # each element of binary list multiplied by 2**0,1,... (i.e., calculates the powe of 2 for each current element of the binary list}
if op == "xor":       #if user selects the  operator as xor , then 
    print(f"Based on XOR Truth Table, binary number for {binary_string1_padding} and {binary_string2_padding} is {newbitwisebin}") #prints binary number according to xor
    print(f"After the XOR operation, decimal number which is equal to {newbitwisebin} is {decimal_number}") #prints decimal connversion of that xor binary number
