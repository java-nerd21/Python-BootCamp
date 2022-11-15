def format_name(f_name, l_name):
    """Take a first and last name and format it
     to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formatedl_name = l_name.title()
    return f"{formated_f_name} {formatedl_name}"

result = format_name(f_name="", l_name="haYes")
print(result)