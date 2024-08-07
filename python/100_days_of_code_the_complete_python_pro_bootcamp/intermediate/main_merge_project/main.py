PLACEHOLDER = "[name]"

with open("/Users/ferdinand.sanjaya/Documents/Course/python/100_days_of_code_the_complete_python_pro_bootcamp/intermediate/main_merge_project/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("/Users/ferdinand.sanjaya/Documents/Course/python/100_days_of_code_the_complete_python_pro_bootcamp/intermediate/main_merge_project/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER,strip_name)
        with open(f'/Users/ferdinand.sanjaya/Documents/Course/python/100_days_of_code_the_complete_python_pro_bootcamp/intermediate/main_merge_project/Output/ReadyToSend/letter_for_{strip_name}.txt',mode = "w") as letter:
            letter.write(new_letter)

    