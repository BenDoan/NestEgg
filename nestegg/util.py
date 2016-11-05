def load_index():
    with open("templates/index.html") as f:
        return "".join(f.readlines())
