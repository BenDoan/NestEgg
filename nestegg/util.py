import calendar

def load_index():
    with open("templates/index.html") as f:
        return "".join(f.readlines())

def month_name_to_num(name):
    return list(calendar.month_abbr).index(name)

def month_num_to_name(num):
    return calendar.month_abbr[num]
