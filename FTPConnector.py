from ftplib import FTP


def download_matching_files_from_ftp(ftp_server, username, password, file_prefix, local_directory, directory=None):
    try:

        ftp = FTP(ftp_server)
        ftp.login(user=username, passwd=password)
        print(f"Connected to FTP server: {ftp_server}")

        if directory:
            ftp.cwd(directory)
            print(f"Changed to directory: {directory}")

        files = ftp.nlst()
        matching_files = [
            file for file in files if file.startswith(file_prefix)]
        print(
            f"Found {len(matching_files)} files matching '{file_prefix}': {matching_files}")

        for remote_file in matching_files:
            local_file_path = f"{local_directory}/{remote_file}"
            with open(local_file_path, 'wb') as local_file:
                ftp.retrbinary(f"RETR {remote_file}", local_file.write)
                print(f"Downloaded '{remote_file}' to '{local_file_path}'")

        ftp.quit()
        print("FTP connection closed.")

    except Exception as e:
        print(f"An error occurred: {e}")


ftp_server = ""
username = ""
password = ""
file_prefix = ""
local_directory = ""
directory = None

download_matching_files_from_ftp(
    ftp_server, username, password, file_prefix, local_directory, directory)
