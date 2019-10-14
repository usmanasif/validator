1) Assumptions:
  1. id: a string.
  2. name: can be one of these [’Sales Tax’, ‘Income Tax’, ‘Value Added Tax’]
  3. rate: a float, less 100 and greater than 0.
  4. Inclusion type: can be one of these [‘INCLUSIVE’, ‘EXCLUSIVE’]
  5. is_custom_amount: a boolean
  6. applied_money:  should not null
  7. amount: should be greater than 0.
  8. currency: should be any of given [‘JOD’, ‘USD’, ‘GBP'] 

2) How to run:
  python3 validate.py transaction.json 