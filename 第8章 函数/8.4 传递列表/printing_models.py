# 8.4.1 在函数中修改列表
# 将列表传递给函数后，函数就可对其进行修改。
# 在函数中对这个列表所做的任何修改都是永久性的，
# 这让你能够高效地处理大量的数据。

# # 不使用函数的情况下
# # 首先创建一个列表，其中包含一些要打印的设计
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表completed_models中
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # 模拟根据设计制作3D打印模型的过程
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#
# # 显示打印好的所有模型
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# 使用函数
# 重新组织这些代码，我们可编写两个函数，每个都做一件具体的工作。
# 大部分代码都与原来相同，只是效率更高。
# 第一个函数将负责处理打印设计的工作，
def print_models(unprinted_models, completed_models):
    """模拟打印每个设计，都将其移到列表completed_models中"""
    while unprinted_models:
        current_model = unprinted_models.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Priting models: " + current_model)
        completed_models.append(current_model)


# 而第二个将概述打印了哪些设计：
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# print_models(unprinted_models, completed_models)
# show_completed_models(completed_models)

# 8.4.2 禁止函数修改列表
# 向函数传递列表的副本而不是原件；
# 这样函数所做的任何修改都只影响副本，而丝毫不影响原件。
print_models(unprinted_models[:], completed_models)
print(unprinted_models, completed_models)
# 虽然向函数传递列表的副本可保留原始列表的内容，
# 但除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数，
# 因为让函数使用现成列表可避免花时间和内存创建副本，从而提高效率，
# 在处理大型列表时尤其如此。

