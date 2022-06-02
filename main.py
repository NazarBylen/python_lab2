from complex_class import *
from stack_funcs import *

complex1 = complex_num('ab', 'bi')
complex2 = complex_num('b', 'abi')
complex3 = complex_num('a', 'bi')

new_stack = stack_funcs()

new_stack.add_elem(complex1)
new_stack.add_elem(complex2)



def main():
    new_stack.add_elem(complex3)
    #new_stack.find_by_key(1)
    #new_stack.print_elem_data(2)
    #new_stack.delete_by_key(2)
    #new_stack.delete_stack()
    #new_stack.sum_stack()
    #new_stack.find_elem('a + bi')
    #new_stack.find_stack_size()
    new_stack.print_all()

if __name__ == '__main__':
    main()
