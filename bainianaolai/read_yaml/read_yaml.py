import yaml
def read_yaml():
    list=[]
    filename="./bainianaolai/data/data.yaml"
    with open(filename, "r",encoding="utf-8") as f:
        data = yaml.load(f)
        for i in data.values():
            list.append((i.get("username"),i.get("pwd")))
        return list