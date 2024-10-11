def concatenation(s1,s2):
    s3=s1 + " " + s2
    return s3

def main():
    s1=input("Enter the first string: ")
    s2=input("Enter the second string: ")
    s3=concatenation(s1,s2)
    print(s3)
if __name__=="__main__":
    main()