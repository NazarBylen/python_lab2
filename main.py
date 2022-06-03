from complex_class import *
from stack_functionality import *

complex1 = complex_num('ab', 'bi')
complex2 = complex_num('b', 'abi')
complex3 = complex_num('a', 'bi')

new_stack = stack_functionality()

new_stack.add_element(complex1)
new_stack.add_element(complex2)



def main():
    new_stack.add_element(complex3)
    #new_stack.find_by_key(1)
    #new_stack.print_element_data(2)
    #new_stack.delete_by_key(2)
    #new_stack.delete_stack()
    #new_stack.sum_stack_elemets()
    #new_stack.find_element('a + bi')
    #new_stack.find_stack_size()
    new_stack.print_all()

if __name__ == '__main__':
    main()
