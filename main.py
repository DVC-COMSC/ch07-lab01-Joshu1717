
# ******************************
# Make your Code
# ******************************
def main():
    total = 0
    

    num = list(map(int, input("Enter 5 numbers:").split()))
    print (min(num))
    print (max(num))

    for ele in range(0, len(num)):
        total = total + num[ele]
    
    total = total - min(num) - max(num)

    print("Sum of all numbers minus the smallest and largest numbers: ", total)

main()