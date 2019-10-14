from glob import glob
import sys
import json

sample_validation = [ 
                      {
                        "id": str,
                        "name": str,
                        "rate": float,
                        "inclusion_type": str,
                        "is_custom_amount": bool,
                        "applied_money": {
                          "amount": int,
                          "currency": str
                        }
                      }
                    ]

name_list = ['Sales Tax', 'Income Tax', 'Value Added Tax']
inclusion_type_list = ['INCLUSIVE', 'EXCLUSIVE']
currency_list = ['JOD', 'USD', 'GBP']

def validate_structure(validation_string, input_json):
  if isinstance(validation_string, dict) and isinstance(input_json, dict):
    # validation string is a dict of data types
    return all(k in input_json and check_validation(k, input_json[k]) and validate_structure(validation_string[k], input_json[k]) for k in validation_string)
  if isinstance(validation_string, list) and isinstance(input_json, list):
    # validate string is list in the form [data type or dict]
    return all(validate_structure(validation_string[0], c) for c in input_json)
  elif isinstance(validation_string, type):
    # validation string is the data type of input_json
    return isinstance(input_json, validation_string)
  else:
    # validation string is neither a dict, nor list, not type
    return False

def check_validation(k, v):
  if k == "id":
    if not (isinstance(v, str)):
      print("id should be string!")
      return False
  elif k == "name":
    if not (v in name_list):
      print("name not found!")
      return False
  elif k == "rate":
    if not (isinstance(v, float) and (0 <= v <= 100)):
      print("rate should be float and between 0-100!")
      return False
  elif k == "inclusion_type":
    if not (v in inclusion_type_list):
      print("inclusion_type not found!")
      return False
  elif k == "is_custom_amount":
    if not (isinstance(v, bool)):
      print("is_custom_amount should be boolean!")
      return False
  elif k == "applied_money":
    if not (isinstance(v, dict)):
      print("applied_money should be dict!")
      return False
  elif k == "amount":
    if not (isinstance(v, int) and (0 <= v <= 100)):
      print("amount should be integer and between 0-100!")
      return False
  elif k == "currency":
    if not (v in currency_list):
      print("currency not found!")
      return False
  return True    

def validate_json(file):
  input_str = None
  with open(file) as f:
    input_str = f.read()
    parsed_json = json.loads(input_str)
    result = validate_structure(sample_validation, parsed_json["taxes"])
    return result

for arg in sys.argv[1:]:
  for filename in glob(arg):
    if filename.lower().endswith('.json'):
      if validate_json(filename):
        print ("%s is valid" % filename)
      else:
        print ("%s is NOT valid" % filename)

