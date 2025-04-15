def modify_content(text):
    # Example modification: convert to uppercase
    return text.upper()

def main():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, "r") as infile:
            content = infile.read()
            modified = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified)
        
        print(f"✅ Modified content written to '{new_filename}' successfully.")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
def modify_content(text):
    # Example modification: convert to uppercase
    return text.upper()

def main():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, "r") as infile:
            content = infile.read()
            modified = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified)
        
        print(f"✅ Modified content written to '{new_filename}' successfully.")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
