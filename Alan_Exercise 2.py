def decimal_to_binary(N):
    binary_form=[]
    while N > 1:
        r=N%2
        binary_form.insert(0,r)
        q=N//2
        N=q
    binary_form.insert(0,N)
    binary_str=''
    for elem in binary_form:
        binary_str += str(elem)

    return binary_form,binary_str



def main():
    N=int(input("Enter the decimal number here:"))
    binary_form,binary_str=decimal_to_binary(N)
    # print(binary_form)
    print("The decimal number",N,"in binary form is",binary_str)

if __name__=="__main__":
    main()