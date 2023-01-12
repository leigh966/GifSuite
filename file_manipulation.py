def remove_extension(filename):
    filename_parts = filename.split('.')
    output = ''
    for index in range(0,len(filename_parts)-1):
        output += filename_parts[index]
    return output

def get_extension(filename):
    filename_parts = filename.split('.')
    return filename_parts[-1]
