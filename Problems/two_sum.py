def two_sum(arr, target):
    dic={}
    for i, num in enumerate(arr):
        complement=target-num;
        if complement in dic:
            return [dic[complement],i]
        else:
            dic[num]=i
    return []
def main():
    print("Wel come to two sum solution")
    try:
        num_str=input("Enter the element of an array separated by space==>> ")
        arr=[int(num) for num in num_str.split()]
        target=int(input("Enter the target number==>> "))
        indices=two_sum(arr,target)
        if indices:
            print(indices, "  These are the indices of targeted number ")
        else:
            print("Not found")
    except ValueError:
        print("Invalid input")


if "__name__ =__main__":
    main()