
def main():
    num_records = int(input())

    errors = []

    for _ in range(num_records):
        data = input().split(" ")
        
        if data[1] == "false":
            errors.append(data[2])

    if len(errors) == 0:
        print("Yes")
    else:
        print("No")
        for i in range(len(errors)):
            if i == len(errors) - 1:
                print(errors[i], end="")
            else:
                print(errors[i], end=" ")
            
        print()

    
main()