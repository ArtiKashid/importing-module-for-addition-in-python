import module1 as a
def main():
    no1=int(input("Enter the first number"))
    no2=int(input("enter the second number"))
    ret=a.Addition(no1,no2)
    print("The addition of two numbers is",ret)

if __name__=="__main__":
    main()