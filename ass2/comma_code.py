def comma_code(a_list):
    first = ', '.join(str(x) for x in a_list[:(len(a_list)-1)]) + ' and ' + a_list[len(a_list)-1]
    print first

comma_code(['apple', 'banana', 'orange'])
