def quicksort(arr):

    if len(arr)<=1:
        return arr
    
    pivot = arr[len(arr)//2]

    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

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

    new_order_nums = quicksort(nums)

    
    print(f'Lista ordenada: {new_order_nums} se ordenaron {len(new_order_nums)} elementos')

if __name__  == "__main__":
    main()