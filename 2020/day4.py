def main():
    fs = open("day4.data",'r')  
    contents = list(map(lambda line: line.strip(), fs.readlines()))
    
    part1 = passport_counter(contents, True)
    print(part1)

def passport_counter(input, print_rows=False):    
    start_new_passport = True
    passport = ""
    valid_count = 0
    row_count = 0
    for row in input:
        if row_count > 0 and row == "":              # An empty row starts a new passport
            start_new_passport = True 
            if is_valid_passport(passport): 
                valid_count += 1    
        else:
            start_new_passport = False   
                
        if start_new_passport:
            passport = row
        else:
            passport += "\n" + row

        row_count += 1 

    if is_valid_passport(passport):  # Count the last one!
        valid_count += 1 

    return valid_count


def is_valid_passport(passport):
    rows = passport.split("\n")

    fields = []
    for row in rows:
        key_values = list(str(row).split())
        keys = list(map(lambda key_value: key_value.split(":")[0], key_values))    
        for key in keys:
            fields.append(key)

    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_fields = ["cid"]

    for field in mandatory_fields:
        if field not in fields:
            return False

    return True
    

def replace_str_at(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

main()