def build_message(expected, actual, message):
    message_array = message.split("'")
    for i in range(1, len(message_array), 2):
        if message_array[i].lower() == "actual":
            message_array[i] = str(actual)
        elif message_array[i].lower() == "expected":
            message_array[i] = str(expected)
    return "".join(message_array)

def compare_values_equal(expected, actual, message):
    if expected != actual:
        raise ValueError(build_message(expected, actual, message))

def compare_values_in_range(min, max, actual, message):
    if actual < min or actual > max:
        raise ValueError(build_message("", actual, message))