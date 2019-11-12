##
## Doesn't work for negative numbers yet
##


import copy

file = "test.LAS"
file_export = "export\\test_out.LAS"
data_type = "MD"


def load_file(in_file):
    with open(in_file, "r") as input_data:

        content = input_data.read().splitlines()

        for counter, line in enumerate(content):
            if line.split()[0] == "~A":
                data_line = counter + 1
                data_list = line
                break

        actual_data = content[data_line:]

    return content, data_list, actual_data, data_line


def find_data_column(find_type, in_header):
    for counter, typ in enumerate(in_header.split()):
        if find_type == typ:
            return counter


def modify_value(fn, in_num_data, col):

    mod_data = copy.deepcopy([i.split() for i in in_num_data])

    for line_index, line in enumerate(in_num_data):
        for val_index, split_vals in enumerate(line.split()):
            if (val_index + 1) == col:
                if float(split_vals) < 0:
                    #print("WARNING: Values less than 0. Ignored line of data.")
                    continue

                mod_data[line_index][val_index] = get_format(fn(split_vals))


    return mod_data


def print_final(al1, updated, out_file):
    with open(out_file, "w") as out:
        for line in al1:
            out.write(line + "\n")
            if line.split()[0] == "~A":
                break

        for line2 in updated:
            out_line = ""

            for item in line2:
                if float(item) < 0:
                    out_line += "  " + item
                else:
                    out_line += "   " + item

            out.write(out_line + "  \n")


def applyCalc(val):
    return float(val) / 0.3048


def get_format(in_for_check):

    num_check = float(in_for_check)
    if float(num_check) < 1:
        return str("{:.{}f}".format(num_check, '7'))
    elif float(num_check) < 10:
        return str("{:.{}f}".format(num_check, '6'))
    elif float(num_check) < 100:
        return str("{:.{}f}".format(num_check, '5'))
    elif float(num_check) < 1000:
        return str("{:.{}f}".format(num_check, '4'))
    elif float(num_check) < 10000:
        return str("{:.{}f}".format(num_check, '3'))
    else:
        return str("{:.{}f}".format(num_check, '2'))


### These lines don't need changing
all_data, data_header, num_data, first_line = load_file(file)
column_number = find_data_column(data_type, data_header)


### This line can be modified as required
output_data = modify_value(applyCalc, num_data, column_number)


### This line doesn't need changing
print_final(all_data, output_data, file_export)

