def noOfC(s):
    unique_chars = []
    lscount = []
    for char in s:
        if char in unique_chars:
            index = unique_chars.index(char)
            lscount[index]+=1
        else:
            unique_chars.append(char)
            lscount.append(1)
    max_count=max(lscount)
    max_char=unique_chars[lscount.index(max_count)]
    return max_char,max_count

def main():
    s=input("Enter the string: ").lower()
    if len(s) == 0:
        print("Please enter a non-empty string.")
        return

    c,count=noOfC(s)
    print(f"Highest occurring character {c}, occurrence: {count}")

if __name__=="__main__":
    main()