import ast
import sys

def analyse_list(input_list):
    total_strings = 0
    unique_strings = []
    repeated_strings = []
    for inner_list in input_list:
        index = -1
        for string in inner_list:
            index += 1
            total_strings += 1
            if string not in unique_strings:
                unique_strings.append(string)
            else:
                if string not in inner_list[0:index]:
                    if string not in repeated_strings:
                        repeated_strings.append(string)
    result = 'Strings appearing in multiple lists: ' + str(', '.join(repr(string) for string in repeated_strings)) + '\nNumber of unique strings: ' + str(len(unique_strings)) + '\nTotal number of strings processed: ' + str(total_strings)
    return result

if __name__== "__main__":
    if len(sys.argv) == 1:
        sys.exit('Please supply a list, in quotes, that you would like to anaylse')
    print(analyse_list(ast.literal_eval(sys.argv[1])))
