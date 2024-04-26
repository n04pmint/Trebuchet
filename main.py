

def main():

    input_path = "input/input.txt"
    text = get_input_path(input_path)
    l_nums = extract_integer(text)
    #num_words = get_num_words(e)
    parsed_num = parse_num(l_nums)
    total = get_total(parsed_num)
    
    print(f"The total is {total}")
    
    # new_dict = []
    # print(l_nums)
    # # l_split = l_nums.split()

    # for each in range(0, len(l_nums)):
    #     if len(l_nums) > 2:
    #         new_dict.append({"word": l_nums[each]})
    #         new_dict.append({"number": parsed_num[each]})
    
    # for each in new_dict:
    #     print(each)
    
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

def get_num_words(input):
    return len(input)

def get_total(list):
    return sum(int(item) for item in list)

def extract_integer(text):

    words = text.split()
    lists_of_num = []
    for word in words:
        num = []
        for char in word:
            if char.isdigit() == True:
                num.append(char)
        num = "".join(num)
        lists_of_num.append(num)

    return lists_of_num
            


def get_input_path(path):
    with open(path) as f:
        return f.read()


main()
