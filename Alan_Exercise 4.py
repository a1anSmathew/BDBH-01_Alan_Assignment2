def char_2_num(N):
    binary_list=[]
    for char in N:
        num=int(char)
        binary_list.append(num)
    return binary_list

def binary2decimal(binary_list):
    sum = 0
    power = 0
    for n in range (len(binary_list) -1, -1 ,-1):
    #length of list starts from 1, so when we take index we must reduce 1 as index starts from 0
    #the second -1 is where the loop stops, ie one element befoe -1 ie 0
    #the third -1 tells that the index decrement after each iteration
        value=binary_list[n] * 2 ** power
        sum += value
        power += 1
    return sum


def main():
    N=input("Enter the binary form of number here:")
    binaryList=char_2_num(N)
    decimal_no=binary2decimal(binaryList)
    print(binaryList)
    print(decimal_no)


if __name__=="__main__":
    main()