
from tokenizer import JSONTokenizer
from parserN import JSONParser



def read_json_from_file(filename):
    with open(filename, "r") as file:
        return file.read()

if __name__ == "__main__":
    json_string = read_json_from_file("input.txt")
    
    tokenizer = JSONTokenizer(json_string)
    tokens = tokenizer.get_tokens()
    
    parser = JSONParser(tokens)
    python_dict_object = parser.parse()
    
    print(python_dict_object)
    print("type of object printed", type(python_dict_object))
