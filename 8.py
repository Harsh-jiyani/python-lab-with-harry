def main():
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
    
    total = a + b
    print(f"The sum of {a} and {b} is: {total}")
    
    if a > b:
        print(f"{a} is the biggest number.")
    elif b > a:
        print(f"{b} is the biggest number.")
    else:
        print("Both numbers are equal.")

if __name__ == "__main__":
    main()
