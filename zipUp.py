import zipfile

#prompt user for file path to zip
file_path = input("Enter the path to the file you want to zip: ")

#prompt user for password to encrypt
password = input("Enter the password you want to use for encryption: ")

#create ZipFile object with the given file path
zip_file = zipfile.ZipFile(file_path + ".zip", mode="w", compression=zipfile.ZIP_DEFLATED)

#write the file to the ZipFile object
zip_file.write(file_path, arcname="file_name")

#set the password for encryption
zip_file.setpassword(password.encode())

#close the ZipFile object
zip_file.close()

#display success message
print("The file has been zipped and encrypted successfully.")
