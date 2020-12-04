import re

def main():
    fs = open("day4.data",'r')  
    contents = list(map(lambda line: line.strip(), fs.readlines()))
    
    part1 = valid_passport_counter(contents)
    print(part1)

    part2 = valid_passport_counter(contents, True)
    print(part2)

def valid_passport_counter(input, validate_values = False):    
    start_new_passport = True
    passport = ""
    valid_count = 0
    row_count = 0
    for row in input:
        if row_count > 0 and row == "":              # An empty row starts a new passport
            start_new_passport = True 
            if is_valid_passport(passport, validate_values): 
                valid_count += 1    
        else:
            start_new_passport = False   
                
        if start_new_passport:
            passport = row
        else:
            passport += "\n" + row

        row_count += 1 

    if is_valid_passport(passport, validate_values):  # Count the last one!
        valid_count += 1 

    return valid_count


def is_valid_passport(passport, validate_values):
    rows = passport.split("\n")

    passport_keys = []
    passport_values = []
    for row in rows:
        key_values = list(str(row).split())
        keys = list(map(lambda key_value: key_value.split(":")[0], key_values))    
        values = list(map(lambda key_value: key_value.split(":")[1], key_values))

        # Get the keys and the values
        for key in keys:
            passport_keys.append(key)
            
        for value in values:
            passport_values.append(value)

    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_fields = ["cid"]

    for field in mandatory_fields:
        if field not in passport_keys:
            return False

    if validate_values:
        for index, key in enumerate(passport_keys):
            value = passport_values[index]
            if key == "byr": 
                if len(value) != 4 or int(value) < 1920 or int(value) > 2002:
                    return False
            if key == "iyr": 
                if len(value) != 4 or int(value) < 2010 or int(value) > 2020:
                    return False
            if key == "eyr": 
                if len(value) != 4 or int(value) < 2020 or int(value) > 2030:
                    return False
            if key == "hgt": 
                if value.endswith("cm"): 
                    num = int(value.replace("cm", ""))
                    if num < 150 or num > 193:
                        return False
                elif value.endswith("in"):
                    num = int(value.replace("in", "")) 
                    if num < 59 or num > 76:
                        return False
                else:
                    return False
            if key == "hcl":
                if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value):
                    return False
            if key == "ecl":
                if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    return False
            if key == "pid":
                if not re.search(r'^\d{9}$', value):
                    return False

    return True
    

def replace_str_at(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

main()