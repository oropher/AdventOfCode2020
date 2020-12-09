with open('02/input','r') as f:
    data = [line.strip() for line in f]
    valid_count = 0
    for d in data:
        min = int(d.split('-')[0])
        max = int(d.split('-')[1].split(' ')[0])
        letter = d.split('-')[1].split(' ')[1].split(':')[0]
        input = d.split('-')[1].split(' ')[2].strip()
        if input.count(letter) >= min and input.count(letter) <= max :
            valid_count += 1
    print("Validos: ", valid_count)