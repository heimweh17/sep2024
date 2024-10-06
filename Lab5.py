def binary_string_decode(binary):
    a=binary
    k=-1
    n=len(a)
    if(a[0]=="0"):
        if(a[1]=="b" or a[1]=="B"):
            k=1
    j=0
    sum=0
    for i in range(n-1,k,-1):
        sum=sum+(ord(a[i])-48)*2**j
        j=j+1
    return sum

def hex_char_decode(digit):
    a=digit
    if(ord(a)>=65 and ord(a)<=70):
        return ord(a)-55
    if(ord(a)>=97 and ord(a)<=102):
        return ord(a)-87
    return ord(a)-48

def hex_string_decode(hex):
    a=hex
    k = -1
    n = len(a)
    if (a[0] == "0"):
        if (a[1] == "x" or a[1] == "X"):
            k = 1
    j = 0
    sum = 0
    for i in range(n-1,k,-1):
        sum=sum+hex_char_decode(a[i])*16**j
        j=j+1
    return sum
def binary_to_hex(binary):
    a=binary
    b=""
    if (a[0] == "0"):
        if (a[1] == "b" or a[1] == "B"):
            a=a.replace("0","",1)
            a=a.replace("b","",1)
    if(len(a)%4!=0):
        a=(4-len(a)%4)*"0"+a
    for i in range(0,len(a),4):
        p=""
        p1=0
        for j in range(i,i+4):
            p=p+a[j]
        p1=binary_string_decode(p)
        if(p1>=10 and p1<16):
            b=b+chr(p1+55)
        else:
            b=b+chr(p1+48)
    return b
if __name__ == "__main__":
    while(True):
        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit")
        a=input("Please enter an option: ")
        if(a=="1"):
            b=input("Please enter the numeric string to convert: ")
            print(f"Result: {hex_string_decode(b)}")
        elif(a=="2"):
            b = input("Please enter the numeric string to convert: ")
            print(f"Result: {binary_string_decode(b)}")
        elif(a=="3"):
            b = input("Please enter the numeric string to convert: ")
            print(f"Result: {binary_to_hex(b)}")
        elif(a=="4"):
            print("Goodbye!")
            break