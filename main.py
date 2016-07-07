

def hex_to_binary(in_filename, extension ):
    """

    :param in_filename: String of the filename
    :param extension:  String of the original extension
    :return:
    """

    file = open(in_filename + extension, 'r')
    file_array = []
    for line in file:
        file_array.append(line.strip())

    file.close()
    output_filename = in_filename + "_binary.txt"
    output_file = open(output_filename, "w")
    for line in file_array:
        try:
            new_line = bin(int(line, 16))[2:].zfill(25) + "\n"
            print(new_line, end="")
            output_file.write(new_line)

            #Hello world

        except ValueError:
            pass
    return output_filename

def find_multiplication(binary_filename):
    file = open(binary_filename, 'r')
    file_array = []
    for line in file:
        file_array.append(line.strip())
    file.close()

    multiplication_code_dictionary = {"100": True, "101": True, "110": True, "111": True}

    for index in range(len(file_array)):
        if file_array[index][:3] in multiplication_code_dictionary:
            print("line #" + str(index) + " multiplication is here!")


print("trying to work!")

binary_filename = hex_to_binary("prog_code", ".coe")
find_multiplication(binary_filename)




