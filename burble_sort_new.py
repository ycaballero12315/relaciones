def burble_sort(arr):
    cant = len(arr)

    if cant <= 1:
        return arr

    for i in range(cant):
        swapped = False
        for j in range(cant-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

def get_nums():
    print("Inserte los numeros para organizar, (0 para Salir...)")
    nums = []
    while True:
        try:
            num = int(input('Inserte el numero: '))
            if num == 0:
                break
            nums.append(num)
        except ValueError as e:
            print('Error: Por favor ingrese un valor entero valido:' + e)
        except KeyboardInterrupt:
            print('\n Introducido por el user')
            break

    return nums

def main():
    nums = get_nums()
    if not nums:
        return 'Lista vacia'
    
    original = nums.copy()
    print(f"Lista desordenada: {original}. ")

    new_order_nums = burble_sort(nums)

    
    print(f'Lista ordenada: {new_order_nums} se ordenaron {len(new_order_nums)} elementos')

if __name__  == "__main__":
    main()


    
        
