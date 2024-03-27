def merge_lists_to_dict(first_list,second_list):
    zipped_lists = zip(first_list,second_list)
    result = dict(zipped_lists)
    return result
a = ['Uzbekistan', 'Russia','USA','GER']
b = ['Tashkent','Moscow','Washington','Berlin']
merge_lists_to_dict(a,b)





















