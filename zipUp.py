import os
import zipfile

def compress_with_password():
    # Prompt the user to enter the path of the file to compress
    source_file_path = input("Enter the path of the file to compress: ")

    # Prompt the user to enter the password for encryption
    password = input("Enter the password to encrypt the file: ")

    # Get the original file name without the extension
    file_name = os.path.splitext(os.path.basename(source_file_path))[0]

    # Create a new ZipFile object with mode 'w' to write to a new zip file
    with zipfile.ZipFile(f"{file_name}.zip", mode='w') as zip_file:
        # Add the source file to the zip file
        zip_file.write(source_file_path, arcname=f"{file_name}", compress_type=zipfile.ZIP_DEFLATED)
        # Set the password for the zip file
        zip_file.setpassword(password.encode('utf-8'))

    print(f"File compressed and encrypted successfully as {file_name}.zip with password {password}!")

# Call the function to execute it
compress_with_password()

