def half_string(S):
    string1 = ''
    if len(S)%2==0:
        for i in range (0,(len(S)//2)):
            char=S[i]
            string1 += char
    else:
        for i in range (0,((len(S)//2) +1)):
            char=S[i]
            string1 += char
    return string1



def main():
    S=input("Enter the string here: ")
    string1=half_string(S)
    print (string1)


if __name__=="__main__":
    main()