variable = input('enter the orginal string:')
def string_rev(str1):
    reverse_string = ''
    index = len(str1)
    while index > 0:
        reverse_string += str1[index -1]
        index = index -1
    return reverse_string
variable_2 = string_rev(variable)
print('reversed version of the element:',variable_2)