def occurrences(S,W):
    S_list=S.lower().split(" ")
    W=W.lower()
    word=0
    for i in range (len(S_list)):
        if S_list[i]==W:
            word += 1
    return word

def main():
    S=input("Enter the sentence here: ")
    W=input("Enter the word here: ")
    print(occurrences(S,W))

if __name__=="__main__":
    main()