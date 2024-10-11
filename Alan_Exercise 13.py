def string_2_list(S,):
    S_list=[]
    for i in S:
        S_list.append(i)
    return S_list

def replace(S_list,c,d):
    for i in range(0,len(S_list)):
        if S_list[i] == c.upper():
            S_list[i]=d.upper()
        elif S_list[i]==c:
            S_list[i]=d
    return S_list

def list_2_string(Replaced_list):
    Replaced_str=""
    for i in Replaced_list:
        Replaced_str += i
    return Replaced_str

def main():
    S=input("Enter the string here: ")
    c=input("Enter the character you want to replace: ")
    d=input("Enter the character you want to replace it with: ")
    S_list=string_2_list(S)
    Replaced_list=replace(S_list,c,d)
    print(list_2_string(Replaced_list))

if __name__=="__main__":
    main()