from math import log10

def power(base,result):
    power=log10(result)/log10(base)
    # print(base**power)
    return power

def main():
    base=int(input("Enter the base value: "))
    result=int(input("Enter the result value here: "))
    x=power(base,result)
    print(x)



if __name__=="__main__":
    main()