# Python script to read, process, and extract file data

input_file_path = "input_data.txt"
output_file_path = "extracted_output.txt"

# 1. Open the input file to read data
with open(input_file_path, "r") as infile:
    # readlines() loads every line of the file into a list
    lines = infile.readlines()

# 2. Perform line counting
total_lines = len(lines)
print(f"Total number of lines in the file: {total_lines}")

# 3. Extract the first two lines
first_two_lines = lines[:2]

# 4. Write the extracted data into a new file
with open(output_file_path, "w") as outfile:
    # writelines() saves our extracted list back to a text format
    outfile.writelines(first_two_lines)

print(f"Successfully saved the first two lines to: {output_file_path}")
