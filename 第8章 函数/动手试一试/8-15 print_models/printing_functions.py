def print_models(unprinted_models, completed_models):
    """模拟打印每个设计，都将其移到列表completed_models中"""
    while unprinted_models:
        current_model = unprinted_models.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Priting models: " + current_model)
        completed_models.append(current_model)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)