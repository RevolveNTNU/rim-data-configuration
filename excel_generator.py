import numpy as np
from column_configuration import *


desired_row_configuration = ["IF", "IB", "CS", "ID", "IC", "OC", "OD", "OB", "OF"] 


def generate_txt_file_of_run(run_number, input_txt_file, output_txt_file):
    """ Enter desired run number, and generate arranged .txt-file from that row"""
    
    # All run numbers are on the third column, counting from 0
    column_number = 2

    with open(input_txt_file, "r") as f:
        
        # Make a list of all the run numbers from run column 
        run_column = [line.split()[column_number] for line in f]

        # Find which row has the desired run number
        desired_row_index = run_column.index(str(run_number))
        
        # Reset index pointer in file
        f.seek(0)
        
        # Save the row correlating to the desired run
        desired_run_row = f.readlines()[desired_row_index] 
    
    # Make .txt-file from desired row
    make_final_txt_file_from_desired_row(desired_run_row, output_txt_file)
        
    # Fix padding in file so that all columns are vertically aligned
    awful_way_to_fix_padding_in_file(output_txt_file)
    

def make_final_txt_file_from_desired_row(run_row, output_txt_file):
    """ From the row of all info correlated to the desired run, 
        generate a .txt-file from that row """

    top_matrix = create_top_matrix(run_row)
    middle_row = create_middle_row(run_row)
    bottom_matrix = create_bottom_matrix(run_row)
    
    with open(output_txt_file, "w") as f:
        # Write the header row to file
        np.savetxt(f, [desired_row_configuration], fmt='%s', delimiter='\t\t\t\t')
        
        # Write the top matrix to file
        for line in top_matrix:
            np.savetxt(f, line, fmt='%s', delimiter='\t')
        
        # Write the middle row to file
        np.savetxt(f, [middle_row], fmt='%s', delimiter='\t\t')
        
        # Write the bottom matrix to file
        for line in bottom_matrix:
            np.savetxt(f, line, fmt='%s', delimiter='\t\t')


def create_top_matrix(run_row):
    """ From the row of all info correlated to the desired run, 
        create the top matrix """
        
    # Collect all info for the top matrix in lists 
    IF_list_wrong_order = list(map(int, run_row.split()[IF_index_start:IF_index_start+12]))
    IB_list_wrong_order = list(map(int, run_row.split()[IB_index_start:IB_index_start+12]))
    CS_list_wrong_order = list(map(int, run_row.split()[CS_index_start:CS_index_start+12]))
    ID_list_wrong_order = list(map(int, run_row.split()[ID_index_start:ID_index_start+12]))
    IC_list_wrong_order = list(map(int, run_row.split()[IC_index_start:IC_index_start+12]))
    OC_list_wrong_order = list(map(int, run_row.split()[OC_index_start:OC_index_start+12]))
    OD_list_wrong_order = list(map(int, run_row.split()[OD_index_start:OD_index_start+12]))
    OB_list_wrong_order = list(map(int, run_row.split()[OB_index_start:OB_index_start+12]))
    OF_list_wrong_order = list(map(int, run_row.split()[OF_index_start:OF_index_start+12]))
    
    
    # Correct order of lists from [1, 10, 11, 12, 2, 3, 4, 5, 6, 7, 8, 9]
    # to [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] using sliced lists
    IF_list_ordered = [IF_list_wrong_order[0]] + IF_list_wrong_order[4:] + IF_list_wrong_order[1:4]
    IB_list_ordered = [IB_list_wrong_order[0]] + IB_list_wrong_order[4:] + IB_list_wrong_order[1:4]
    CS_list_ordered = [CS_list_wrong_order[0]] + CS_list_wrong_order[4:] + CS_list_wrong_order[1:4]
    ID_list_ordered = [ID_list_wrong_order[0]] + ID_list_wrong_order[4:] + ID_list_wrong_order[1:4]
    IC_list_ordered = [IC_list_wrong_order[0]] + IC_list_wrong_order[4:] + IC_list_wrong_order[1:4]
    OC_list_ordered = [OC_list_wrong_order[0]] + OC_list_wrong_order[4:] + OC_list_wrong_order[1:4]
    OD_list_ordered = [OD_list_wrong_order[0]] + OD_list_wrong_order[4:] + OD_list_wrong_order[1:4]
    OB_list_ordered = [OB_list_wrong_order[0]] + OB_list_wrong_order[4:] + OB_list_wrong_order[1:4]
    OF_list_ordered = [OF_list_wrong_order[0]] + OF_list_wrong_order[4:] + OF_list_wrong_order[1:4]

    # Make top matrix
    top_matrix = np.matrix(
        [np.array(IF_list_ordered),
        np.array(IB_list_ordered),
        np.array(CS_list_ordered),
        np.array(ID_list_ordered),
        np.array(IC_list_ordered),
        np.array(OC_list_ordered),
        np.array(OD_list_ordered),
        np.array(OB_list_ordered),
        np.array(OF_list_ordered)]).T

    return top_matrix


def create_middle_row(run_row):
    """ From the row of all info correlated to the desired run, 
        create the middle row """

    # Collect all info for the middle row 
    n_IF = run_row.split()[n_IF_index]
    n_IB = run_row.split()[n_IB_index]
    n_CS = run_row.split()[n_CS_index]
    n_ID = run_row.split()[n_ID_index]
    n_IC = run_row.split()[n_IC_index]
    n_OC = run_row.split()[n_OC_index]
    n_OD = run_row.split()[n_OD_index]
    n_OB = run_row.split()[n_OB_index]
    n_OF = run_row.split()[n_OF_index]
    
    # Make middle row list
    middle_row = [
        n_IF,
        n_IB,
        n_CS,
        n_ID,
        n_IC,
        n_OC,
        n_OD,
        n_OB,
        n_OF
    ]

    return middle_row


def create_bottom_matrix(run_row):
    """ From the row of all info correlated to the desired run, 
        create the bottom matrix """
        
    # Collect all info for the bottom matrix in lists 
    M_IF_list_wrong_order = list(map(int, run_row.split()[M_IF_index_start:M_IF_index_start+11])) #M_IF_11 is not in the file
    M_IB_list_wrong_order = list(map(int, run_row.split()[M_IB_index_start:M_IB_index_start+12]))
    M_CS_list_wrong_order = list(map(int, run_row.split()[M_CS_index_start:M_CS_index_start+12]))
    M_ID_list_wrong_order = list(map(int, run_row.split()[M_ID_index_start:M_ID_index_start+12]))
    M_IC_list_wrong_order = list(map(int, run_row.split()[M_IC_index_start:M_IC_index_start+12]))
    M_OC_list_wrong_order = list(map(int, run_row.split()[M_OC_index_start:M_OC_index_start+12]))
    M_OD_list_wrong_order = list(map(int, run_row.split()[M_OD_index_start:M_OD_index_start+12]))
    M_OB_list_wrong_order = list(map(int, run_row.split()[M_OB_index_start:M_OB_index_start+12]))
    M_OF_list_wrong_order = list(map(int, run_row.split()[M_OF_index_start:M_OF_index_start+12]))
    
    # Correct order of lists from [1, 10, 11, 12, 2, 3, 4, 5, 6, 7, 8, 9]
    # to [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] using sliced lists
    M_IF_list_ordered = [M_IF_list_wrong_order[0]] + M_IF_list_wrong_order[3:] + [M_IF_list_wrong_order[1]] + ["X"] + [M_IF_list_wrong_order[2]]
    M_IB_list_ordered = [M_IB_list_wrong_order[0]] + M_IB_list_wrong_order[4:] + M_IB_list_wrong_order[1:4]
    M_CS_list_ordered = [M_CS_list_wrong_order[0]] + M_CS_list_wrong_order[4:] + M_CS_list_wrong_order[1:4]
    M_ID_list_ordered = [M_ID_list_wrong_order[0]] + M_ID_list_wrong_order[4:] + M_ID_list_wrong_order[1:4]
    M_IC_list_ordered = [M_IC_list_wrong_order[0]] + M_IC_list_wrong_order[4:] + M_IC_list_wrong_order[1:4]
    M_OC_list_ordered = [M_OC_list_wrong_order[0]] + M_OC_list_wrong_order[4:] + M_OC_list_wrong_order[1:4]
    M_OD_list_ordered = [M_OD_list_wrong_order[0]] + M_OD_list_wrong_order[4:] + M_OD_list_wrong_order[1:4]
    M_OB_list_ordered = [M_OB_list_wrong_order[0]] + M_OB_list_wrong_order[4:] + M_OB_list_wrong_order[1:4]
    M_OF_list_ordered = [M_OF_list_wrong_order[0]] + M_OF_list_wrong_order[4:] + M_OF_list_wrong_order[1:4]

    # Make bottom matrix
    bottom_matrix = np.matrix(
        [np.array(M_IF_list_ordered),
        np.array(M_IB_list_ordered),
        np.array(M_CS_list_ordered),
        np.array(M_ID_list_ordered),
        np.array(M_IC_list_ordered),
        np.array(M_OC_list_ordered),
        np.array(M_OD_list_ordered),
        np.array(M_OB_list_ordered),
        np.array(M_OF_list_ordered)]).T

    return bottom_matrix


def awful_way_to_fix_padding_in_file(fix_this_file):
    """
    ChatGPT fixed this for me hehe
    """
  # Open the file in read mode
    with open(fix_this_file, "r") as f:
        # Read the entire file into a list of lines
        lines = f.readlines()

    # Split each line into a list of columns
    columns = [line.split() for line in lines]

    # Calculate the maximum width of each column, taking into account the decimal point and negative sign
    max_widths = [max(len(column) for column in column_list) for column_list in zip(*columns)]

    # Open the file in write mode
    with open(fix_this_file, "w") as f:
        # Iterate over the lines in the list
        for line in lines:
            # Split the line into a list of columns
            column_list = line.split()
            # Format the line with the calculated column widths, taking into account the decimal point and negative sign
            formatted_line = " ".join("{:>{}}".format(column, width) for column, width in zip(column_list, max_widths))
            # Write the formatted line to the file
            f.write(formatted_line + "\n")






def find_all_start_indices(header_file):
    """
    Print all start indices of all column items in top and bottom matrix, and in middle row.
    They are all to be put in column_configuration.py
    """
    
    # enumerate() only worked with files, had to create own file with transposed header
    
    all_start_indices = np.array([[0,0]])
    
    with open(header_file, 'r') as f:
        for i, line in enumerate(f):
            if line.endswith('_1\n') or line.startswith('n_'):
                index_start = [line, i+3] # +3 because the first three columns are irrelevant
                all_start_indices = np.vstack([all_start_indices, index_start])
    
    print(f"Here are all start indices, put them in column_configuration.py yourself bitch:\n {all_start_indices}")