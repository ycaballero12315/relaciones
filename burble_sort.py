def bubble_sort(arr: list)->list:
    n = len(arr)
    flag = False

    for i in range(n):

        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True

        if not flag:
            break

    return arr
    
if __name__ == "__main__":
    arr = []
    while True:
    
        num = int(input("Digame los numeros que vas a digital si desea salir '0': "))
        if num == 0:
            break
        arr.append(num)
    if arr:
        arr = set(arr)
        arr = list(arr)
        print(bubble_sort(arr))
    else:
        print('Lista vacia!!!')   