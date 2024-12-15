import requests


# function to downlaod the file
def download_file(url, filename= ''):
    response = requests.get(url, stream= True)
    # pass a new filename or maitain the default
    if filename :
        pass
    else:
        filename = url.split('/')[-1]

    # store the file
    with open(filename, 'wb') as file:
        # download the file in small chunks
        for chunk in response.iter_content(chunk_size= 8192):
            file.write(chunk)
    
# run the script
if __name__ == '__main__':
    download_url = input("Enter the url: ").strip()
    save_name = input("Enter a save name (leave blank for default): ").strip()
    save_to = save_name if save_name else None


    download_file(download_url, save_to)
