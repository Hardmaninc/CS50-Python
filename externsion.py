def get_media_type(file_name):
    file_ext = file_name.split('.')[-1].lower().strip(" ")

    if file_ext in ("jpg"):
        return 'image/jpeg'

    elif file_ext in ("jpeg"):
        return 'image/jpeg'

    elif file_ext in ("png"):
        return 'image/png'

    elif file_ext in ("gif"):
        return 'image/gif'

    elif file_ext in ("pdf"):
        return 'application/pdf'

    elif file_ext in ("txt"):
        return "text/plain"

    elif file_ext in ("zip"):
        return 'application/zip'

    else:
        return 'application/octet-stream'

file_name = input("File name: ")
print(get_media_type(file_name))