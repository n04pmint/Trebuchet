def main():
    input_path = "input/input.txt"
    inputs = get_input_path(input_path)
    results = eval_inputs(inputs)
    print(f"Total is : {results}")
    
def check_string(string):
    if "oneight" in string:
        string = string.replace("oneight", "oneeight")
    if "eightwo" in string:
        string = string.replace("eightwo", "eighttwo")
    if "twone" in string:
        string = string.replace("twone", "twoone")
    return string

def eval_inputs(input):
    split_input = input.split()
    lists = []

    #check for "oneight" or "eightwo"
    special_cases = []
    
    for each in split_input:
        #print(each)
        each = check_string(each)
        result = extract_number(each)
        lists.append(result)
        print(f"{each} = {result}")
        
    
    extracted_numbers = extract_int(lists)
    parsed_numbers = parse_num(extracted_numbers)
    return get_total(parsed_numbers)
    
def extract_number(string):
    # Define the mapping between written-out numbers and digits
    number_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    # Iterate over the mapping and replace each occurrence in the string
    for word, digit in number_mapping.items():
        string = string.replace(word, digit)
    
    return string

    
def parse_num(list):
    new_list = []
    for number in list:
        if len(number) > 2:
            num = []
            num.append(number[0])
            num.append(number[len(number)-1])
            num = "".join(num)
            new_list.append(num)
        elif len(number) == 1:
            num = []
            num.append(number[0])
            num.append(number[0])
            num = "".join(num)
            new_list.append(num)
        else:
            new_list.append(number)
    return new_list

def get_total(list):
    return sum(int(item) for item in list)

def extract_int(input):
    #string = input.split()
    num_list = []
    for word in input:
        num = []
        for char in word:
            if char.isdigit() == True:
                num.append(char)
        num = "".join(num)
        num_list.append(num)
    return num_list

#Get the path of the input text file.
def get_input_path(path):
    with open(path) as f:
        return f.read()







main()