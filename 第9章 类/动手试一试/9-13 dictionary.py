from collections import OrderedDict
python_dictionary = OrderedDict()
python_dictionary['URL'] = 'the address of a web page on the world wide web'
python_dictionary['sort'] = 'arrange in groups'
python_dictionary['gigabyte'] = 'a unit of information equal to one billion (1,073,741,824) bytes or 1024 megabytes'
python_dictionary['editor'] = 'a program designed to perform such editorial functions as rearrangement or modification or deletion of data'
python_dictionary['timer'] = 'a regulator that activates or deactivates a mechanism at set times'
python_dictionary['offspring'] = 'something that comes into existence as a result'
for key, value in python_dictionary.items():
    print(key + ":\n\t" + value)
# print("URL:\n\t" + python_dictionary['URL'])
# print("sort:\n\t" + python_dictionary['sort'])
# print("gigabyte:\n\t" + python_dictionary['gigabyte'])
# print("editor:\n\t" + python_dictionary['editor'])
# print("timer:\n\t" + python_dictionary['timer'])
