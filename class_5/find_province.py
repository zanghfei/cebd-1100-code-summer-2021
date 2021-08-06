# Ask user what is the province code, then display the full province name.

provinces = {"QC": "Québec", "BC": "British Columbia", "ON": "Ontario"}

province_code = input("What is the province code? >")
province_name = None

if province_code.upper() in provinces:
    province_name = provinces[province_code]
    print("The province name is {}".format(province_name))
else:
    print("The province code was not found.")


