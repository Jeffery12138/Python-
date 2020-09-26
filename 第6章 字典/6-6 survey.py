favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
survey_people = ['jen', 'tom', 'lucy', 'phil']
for name in survey_people:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for taking the survey.")
    else:
        print(name.title() + ", welcome to take the survey.")