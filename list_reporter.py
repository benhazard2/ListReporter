import ast
import sys

def analyse_list(input_list):
    total = 0
    string_list = []
    multi_string = []
    for inner_list in input_list:
        index = -1
        for string in inner_list:
            index += 1
            total += 1
            if string not in string_list:
                string_list.append(string)
            else:
                if string not in inner_list[0:index]:
                    if string not in multi_string:
                        multi_string.append(string)
    result = 'Strings appearing in multiple lists: ' + str(', '.join(repr(string) for string in multi_string)) + '\nNumber of unique strings: ' + str(len(string_list)) + '\nTotal number of strings processed: ' + str(total)
    return result

if __name__== "__main__":
    if len(sys.argv) == 1:
        sys.exit('Please supply a list that you would like to anaylse')
    print(analyse_list(ast.literal_eval(sys.argv[1])))
