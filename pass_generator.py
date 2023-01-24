import random

def get_upper_letters() -> str:
     return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_lower_letters() -> str:
    return get_upper_letters().lower()
    
def get_digits() -> str:
    return "0123456789"
    
def get_special_chars() -> str:
    return "!§$%&/=?^\\'*+@~;."
    
def get_brackets() -> str:
    brackets = "()}{<>[]"
    return brackets

def get_minus() -> str:
    return "-"
    
def get_underline() -> str:
    return "_"

def get_full_collection(upper, lower, numbers, specials, brackets, minus, underline) -> str:
    full_collection = ""
    if upper:
        full_collection += get_upper_letters()
    if lower: 
        full_collection += get_lower_letters()
    if numbers:
        full_collection += get_digits()
    if specials:
        full_collection += get_special_chars()
    if brackets:
        full_collection += get_brackets()
    if minus:
        full_collection += get_minus()
    if underline:
        full_collection += get_underline()
    return full_collection

def main() -> None:
    upper = True
    lower = True
    number = True
    special = True
    bracket = True
    minus = True
    underline = True
    complete_collection = get_full_collection(upper, lower, number, 
                            special, bracket, minus, underline)
    length = 32
    password = "".join(random.sample(complete_collection, length))
    print(password)

if __name__ == "__main__":
    main()
