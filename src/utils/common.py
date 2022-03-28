import yaml

def read_yaml(filepath):
    with open(filepath, 'r') as f:
        content = yaml.safe_load(f)
    return content