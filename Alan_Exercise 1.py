def sum_of_nat_numbers(N):
    sum=(((N*(N+1)*(2*N+1))/6))
    return sum

def main():
    N=int(input("Enter the number here:"))
    sum=sum_of_nat_numbers(N)
    print("Sum of first",N,"natural numbers is",sum)

if __name__=="__main__":
    main()