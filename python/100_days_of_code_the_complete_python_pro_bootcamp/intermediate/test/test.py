file_path = "/Users/ferdinand.sanjaya/Documents/Course/python/100_days_of_code_the_complete_python_pro_bootcamp/intermediate/test/file.txt"

with open(file_path,mode = 'a') as file:
    # contents = file.read()
    # print(contents)
    file.write("\nnew_text")


