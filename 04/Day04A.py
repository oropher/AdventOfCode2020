import re

with open('04/input','r') as f:
    data = dict()
    
    validation_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    count = 0

    lines = [line for line in f]
    for line in lines:
        if line != '\n':
            temp = line.strip().split(' ')
            #print(temp)
            for t in temp:
                #print(t.split(':'))
                data[t.split(':')[0]] = t.split(':')[1]
        else :
            #print(data)
            is_valid = True
            for vl in  validation_list:
                #print("Validando", vl)
                if vl not in data:
                    #print(vl, "no estaba")
                    is_valid = False
            if is_valid:
                
                for vl in  validation_list:
                    #print(vl, data[vl])
                    if vl == 'byr':
                        byr = int(data[vl])
                        if not (byr >= 1920 and byr <= 2002):
                            is_valid = False
                    if vl == 'iyr':
                        iyr = int(data[vl])
                        if not (iyr >= 2010 and iyr <= 2020):
                            is_valid = False
                    if vl == 'eyr':
                        eyr = int(data[vl])
                        if not (eyr >= 2020 and eyr <= 2030):
                            is_valid = False
                    if vl == 'hgt':
                        if data[vl].endswith("cm"):
                           val = int(data[vl][:-2])
                           if not (val >= 150 and val <= 193):
                               is_valid = False
                        else:
                            if data[vl].endswith("in"):
                                val = int(data[vl][:-2])
                                if not (val >= 59 and val <= 76):
                                    is_valid = False
                            else:
                                is_valid = False
                    if vl == 'hcl':
                        if not re.match(r"^#[0-9a-f]{6}$", data[vl]):
                            is_valid = False
                    if vl == 'ecl':
                        if data[vl] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                            is_valid = False
                    if vl == 'pid':
                        if not re.match(r"^\d{9}$", data[vl]):
                            is_valid = False
                if is_valid:
                    print("valid!!!")
                    count += 1
            data = dict()
            print()

    print("Validos", count)






