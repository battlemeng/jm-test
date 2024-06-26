import yaml
def get_data_links(key):
    dir_path = './config/data_links.yaml'
    f = open(dir_path, encoding="utf8")
    data = yaml.safe_load(f)
    return data[key]
