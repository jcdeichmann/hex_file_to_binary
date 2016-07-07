

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
            #print(new_line, end="")
            output_file.write(new_line)

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
        if file_array[index][:3] != "000":
            print("line #" + str(index) + " multiplication is here!")


def find_all_operators_in(num_of_msb,binary_filename):
    file = open(binary_filename, 'r')
    file_array = []
    for line in file:
        file_array.append(line.strip())
    file.close()

    output_filename = binary_filename + "_unique_instructions.txt"
    output_file = open(output_filename, "w")
    unique_instructions_set = set()
    for index in range(len(file_array)):
        instruction = file_array[index][:num_of_msb]
        unique_instructions_set.add(instruction+"\n")
    for instruction in unique_instructions_set:
        output_file.write(instruction)
        
       
def machine_to_assembly_in(binary_filename):
    file = open(binary_filename, 'r')
    file_array = []
    for line in file:
        file_array.append(line.strip())
    file.close()
    
    output_filename = binary_filename + "_assembly_instructions.txt"
    output_file = open(output_filename, "w")
    asm_mul_dict = {"000": "MUL_NOP", "001": "MUL_CLR", "010": "MUL_SFT",
                    "100": "MUL_ACC_00", "101": "MUL_ACC_01", "110": "MUL_ACC_10",
                    "111": "MUL_ACC_11"}
    
    asm_add_dict = {"0000": "ADD_NOP", "0001": "ADD_I", "0010": "SUB_I",
                    "0011": "ADD_ACC", "0100": "SUB_ACC", "0101": "ADD_RED_1",
                    "0110": "ADD_RED_2", "0111": "ADD_RED", "1000": "SUB_RED"}
    for index in range(len(file_array)):
        mult_key = file_array[index][:3]
        add_load_key = file_array[index][3]
        add_key = file_array[index][4:8]
        write_key = file_array[index][8]
        addra_key = file_array[index][9:17]
        addrb_key = file_array[index][17:]
        
        asm_string = []

        asm_string.append(file_array[index].ljust(30))
        
        #figure out if it is a write or read
        if write_key == "1":
            asm_string.append("W".ljust(3))
        else:
            asm_string.append("R".ljust(3))

        if add_load_key == "1":
            asm_string.append("L_".rjust(3))
        else:
            asm_string.append("".rjust(3))
        
        #append the mutliplier ASM
        asm_string.append(asm_mul_dict.get(mult_key).ljust(15))
        
        #append the addition ASM
        asm_string.append(asm_add_dict.get(add_key).ljust(15))
        
        #append the two addresses
        asm_string.append(hex(int(addra_key,2)).ljust(5))
        asm_string.append(hex(int(addrb_key,2)).ljust(5))
        
        #add newline character
        asm_string.append("\n")
        
        output_file.write(''.join(asm_string))
    output_file.close()
        
       

print("trying to work!")

binary_filename = hex_to_binary("prog_code", ".coe")
machine_to_assembly_in(binary_filename)
#find_multiplication(binary_filename)
find_all_operators_in(8,binary_filename)




