def anagrams(S1,S2):
    if len(S1)!=len(S2):
        print("The two words are not anagrams")
        exit()
    if sorted(S1.lower())==sorted(S2.lower()):
        anagrams=True
    else:
        anagrams=False
    return anagrams

    #This piece of code doesnt check for repeated letters
    # anagrams=False
    # for i in range (len(S1)):
    #     for j in range (len(S2)):
    #         if S1[i].lower()==S2[j].lower():
    #             anagrams=True
    #         else:
    #             continue
    # return anagrams



def main():
    S1=input("Enter the first word here: ")
    S2=input("Enter the second word here: ")
    print(anagrams(S1,S2))
if __name__=="__main__":
    main()
