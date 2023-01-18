from excel_generator import *

#----- ENTER DESIRED RUN HERE -----# 
desired_row = 5

#----- ENTER FILE NAMES HERE -----# 
input_file = "example_input.txt"
header_file = "header.txt"
output_file = "output.txt"

generate_txt_file_of_run(desired_row, f"input/{input_file}", f"output/{output_file}")
