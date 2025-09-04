import typing
def binarysearch(arr: list[int], target: int)->int:

    left, right = 0, len(arr)-1

    while left <=right:
        middle = (left+right)//2
        if target == arr[middle]:
            return middle
        elif target>arr[middle]:
            left = middle+1
        elif target < arr[middle]:
            right = middle - 1

    return -1

# Usando recursividad
def recursive_binarysearch(arr: list[int], 
                           target: int, left = 0, right=None)->int:

    if not right:
        right = len(arr)-1

    if left > right:
        return -1
    
    middle = (left + right)//2
    if target == arr[middle]:
        return middle
    elif target > arr[middle]:
        return recursive_binarysearch(arr, target, middle+1, right)
    elif target < arr[middle]:
        return recursive_binarysearch(arr, target, left, middle-1)

def get_nums():
    print("Inserte los elementos de la lista: , (0 para Salir...)")
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
    print(f"Lista con todos los elementos: {original}. ")
    
    print('Elemento a buscar: ')
    elem = int(input())
    new_order_nums = recursive_binarysearch(nums, elem)

    
    print(f"El elemento es: {original[new_order_nums]}")

if __name__  == "__main__":
    main()
    