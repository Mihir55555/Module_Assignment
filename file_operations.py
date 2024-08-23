## 15

"""Read data from the file."""

def read_from_file(file_path):
    
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

"""Write data to the file (overwriting existing content)."""
        
def write_to_file(file_path, data):
   
    try:
        with open(file_path, 'w') as file:
            file.write(data)
            print(f"Data written to '{file_path}' successfully.")

    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")

"""Append data to the end of the file."""

def append_to_file(file_path, data):
    
    try:
        with open(file_path, 'a') as file:
            file.write(data)
            print(f"Data appended to '{file_path}' successfully.")
    
    except IOError as e:
        print(f"Error appending to file '{file_path}': {e}")