def char_occurrence(S,F):
    if len(F)==1 and F.isalpha():
        for char in S:
            if char==F:
                index1=S.index(char)
                return index1
                exit()
    

def main():
    S=input("Enter the string here: ")
    F=input("Which character occurrence do you want to find: ")
    index1=char_occurrence(S,F)
    print(index1)

if __name__=="__main__":
    main()