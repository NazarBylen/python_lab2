from complex_class import *

class stack_funcs():

    global stack
    stack=[]

    def add_element(self, new_elem) -> stack:
        stack.append(new_elem)
        return stack

    def find_by_key(self, element_num: int) -> None:
        for index in range(len(stack)):
            if index == element_num:
                print(f'element under this number is : {stack[index]}')

    def print_element_data(self, element_num: int) -> None:
        for index in range(len(stack)):
            if index == element_num:
                print(stack[index].real)
                print(stack[index].nreal)

    def delete_by_key(self, element_num: int) -> None:
        for index in range(len(stack)):
            if index == element_num:
                stack.pop(index)

    def print_all(self) -> None:
        for index in range(len(stack)):
            print(stack[index])

    def delete_stack(self) -> None:
        return stack.clear()

    def sum_stack_elemets(self) -> str:
        result_array = []
        for index in range(len(stack)):
            if index == len(stack) - 2:
                result_array.append(stack[index].__str__())
            if index == len(stack) - 1:
                result_array.append(stack[index].__str__())

        result = result_array[0] + result_array[1]
        print(result_array)
        return result

    def find_element(self, element: str) -> str:
        for index in range(len(stack)):
            if element == stack[index].__str__():
                print(f'element found, its number is {index}')

    def find_stack_size(self) -> int:
        size = stack.__sizeof__()
        print(size)
        return size