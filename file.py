# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as f:
            f.write("Welcome to Bosco Marketing Agency.\n")
            f.write("We offer exemplary sercices in tech and digital marketing.\n")
            f.write("We impact the community like youths by nurturing and supporting talents through content creation.\n")
    except Exception as e:
        print("Error:", e)
    else:
        print("File 'my_file.txt' created successfully.")

# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as f:
            content = f.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read 'my_file.txt'.")
    except Exception as e:
        print("Error:", e)

# File Appending
def append_to_file():
    try:
        with open("my_file.txt", "a") as f:
            f.write("We look forward to onboard:\n")
            f.write("1. Micro Small and Medium-Sized Enterprises\n")
            f.write("2. Organizations such as NGOs\n")
            f.write("3. Vibrant individuals like politicians\n")
    except Exception as e:
        print("Error:", e)
    else:
        print("Content appended to 'my_file.txt'.")

# Main function
def main():
    create_file()
    print("\nReading 'my_file.txt'...\n")
    read_file()
    print("\nAppending to 'my_file.txt'...\n")
    append_to_file()
    print("\nReading 'my_file.txt' after appending...\n")
    read_file()

if __name__ == "__main__":
    main()
