from complex_class import *

class stack_funcs():

    global stack
    stack=[]

    def add_elem(self, new_elem) -> stack:
        stack.append(new_elem)
        return stack

    def find_by_key(self, elem_num: int) -> None:
        for i in range(len(stack)):
            if i == elem_num:
                print(f'element under this number is : {stack[i]}')

    def print_elem_data(self, elem_num: int) -> None:
        for i in range(len(stack)):
            if i == elem_num:
                print(stack[i].real)
                print(stack[i].nreal)

    def delete_by_key(self, elem_num: int) -> None:
        for idx in range(len(stack)):
            if idx == elem_num:
                stack.pop(idx)

    def print_all(self) -> None:
        for idx in range(len(stack)):
            print(stack[idx])

    def delete_stack(self) -> None:
        return stack.clear()

    def sum_stack(self) -> str:
        result_array = []
        for i in range(len(stack)):
            if i == len(stack) - 2:
                result_array.append(stack[i].__str__())
            if i == len(stack) - 1:
                result_array.append(stack[i].__str__())

        result = result_array[0] + result_array[1]
        print(result_array)
        return result

    def find_elem(self, elem: str) -> str:
        for i in range(len(stack)):
            if elem == stack[i].__str__():
                print(f'elem found, its number is {i}')

    def find_stack_size(self) -> int:
        size = stack.__sizeof__()
        print(size)
        return size