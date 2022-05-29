from complex_class import *

complex1 = complex_num('ab', 'bi')
complex2 = complex_num('b', 'abi')
complex3 = complex_num('a', 'bi')

stack = []

stack.append(complex1)
stack.append(complex2)

def add_elem(new_elem : complex_num)->stack:
    stack.append(new_elem)
    return stack

def find_by_key(elem_num : int)->None:
    for i in range(len(stack)):
        if i==elem_num:
            print(f'element under this number is : {stack[i]}')

def print_elem_data(elem_num : int)->None:
    for i in range(len(stack)):
        if i==elem_num:
            print(stack[i].real)
            print(stack[i].nreal)


def delete_by_key(elem_num : int)->None:
    for i in range(len(stack)):
        if i==elem_num:
            stack.pop(i)

def print_all()->None:
    for i in range(len(stack)):
        print(stack[i])

def delete_stack()-> None:
    return stack.clear()

def sum_stack()->str:
    arr = []
    result=''
    for i in range(len(stack)):
        if i == len(stack)-2:
            arr.append(stack[i].__str__())
        if i == len(stack)-1:
            arr.append(stack[i].__str__())

    result = arr[0]+arr[1]
    print(arr)
    return result

def find_elem(elem : str)->str:
    for i in range(len(stack)):
        if elem==stack[i].__str__():
            print(f'elem found, its number is {i}')

def find_stack_size()->int:
    size=stack.__sizeof__()
    print(size)
    return size

def main():
    add_elem(complex3)
    #find_by_key(1)
    #print_elem_data(2)
    #delete_by_key(2)
    #print_all()
    #delete_stack()
    #sum_stack()
    #find_elem('a + bi')
    #find_stack_size()
    #print_all()

if __name__ == '__main__':
    main()
