def Prime_numbers(N):
    if N==1:
        print("1 is a unique number")
        exit()
    prime = True
    for i in range (2,(N//2)):
        if N % i == 0:
            prime=False
            break
        else:
            prime=True
    return prime


def main():
    N=int(input("Enter the number here: "))
    prime=Prime_numbers(N)
    print("The number",N,"is a prime number:",prime)


if __name__=="__main__":
    main()