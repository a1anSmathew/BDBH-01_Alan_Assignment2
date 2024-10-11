def decimal_to_binary(N):
    binary_form=[]
    while N > 1:
        r=N%2
        binary_form.insert(0,r)
        q=N//2
        N=q
    binary_form.insert(0,N)
    binary_str=''
    ones=0
    for elem in binary_form:
        binary_str += str(elem)
        if elem==1:
            ones += 1

    return binary_form,binary_str,ones

def main():
    N=int(input("Enter the decimal number here:"))
    binary_form,binary_str,ones=decimal_to_binary(N)
    print("The decimal number",N,"in binary form is",binary_str)
    print("The number of 1's in the binary representation of",N,"is",ones)

if __name__=="__main__":
    main()