print("Enter filename to read: ")
input_filename = input().strip()
try:  
    with open(input_filename, 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
finally:    
    print("Reading a file with expection handling completed.")
