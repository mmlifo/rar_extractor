import os
import rarfile

def extract_rar_file():
    # Get the RAR file path from user input
    rar_path = input("Enter the path to your RAR file (e.g., archive.rar): ").strip()

    # Check if the file actually exists before proceeding
    if not os.path.exists(rar_path):
        print(f"Error: File '{rar_path}' not found. Please check the path and try again.")
        return

    # Get the password from user input (hidden input is also possible, but standard input is used here)
    rar_password = input("Enter the password for the RAR file: ")

    # Define the destination extraction folder
    extract_path = "./extracted_files/"

    try:
        # Open the RAR file using RarFile
        with rarfile.RarFile(rar_path) as rf:

            # Check if the archive is encrypted and set the password
            if rf.needs_password():
                rf.setpassword(rar_password)

            print("Extracting files, please wait...")
            # Extract all contents to the target path
            rf.extractall(path=extract_path)
            print(f"Files extracted successfully to '{extract_path}'!")

    except rarfile.BadRarFile:
        print("Error: The file is corrupted, incomplete, or not a valid RAR archive.")

    except rarfile.RarWrongPassword:
        print("Error: The password provided is incorrect.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    extract_rar_file()
