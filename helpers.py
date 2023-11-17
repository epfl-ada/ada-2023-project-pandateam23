def get_path(file_url):
    # Extract file ID from the Google Drive URL
    file_id = file_url.split('/')[-2]

    # Construct the download link
    download_link = f"https://drive.google.com/uc?id={file_id}"

    # Return the download link
    return download_link