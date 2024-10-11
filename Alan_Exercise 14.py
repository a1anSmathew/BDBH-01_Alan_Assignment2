def leading_space(S):
    Str=S.lstrip()
    return Str

def main():
    S=input("Enter the string here: ")
    print(leading_space(S))

if __name__=="__main__":
    main()