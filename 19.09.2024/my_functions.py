def my_function(text: str):
    result = ""

    if (len(text) <= 5):
        result = "too short"
    else:
        if(len(text) >= 10):
            result = "too long"
        else:
            result = "just right"
    return result

def my_other_function(one: bool, two: bool):
    result = ""

    if(one):
        result = "one is true"
        if(two):
            result = result + ", two is true"
        else:
            result = "one is false"
            if(two):
                result = result + ", two is true"
            else:
                result = result + ", two is false"
    return result


