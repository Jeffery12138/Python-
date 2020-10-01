import printing_functions as pf

unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# pf.print_models(unprinted_models, completed_models)
# pf.show_completed_models(completed_models)

# 8.4.2 禁止函数修改列表
# 向函数传递列表的副本而不是原件；
# 这样函数所做的任何修改都只影响副本，而丝毫不影响原件。
pf.print_models(unprinted_models[:], completed_models)
print(unprinted_models, completed_models)

