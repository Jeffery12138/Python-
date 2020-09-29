# 鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
# 向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同；
# 也可使用关键字实参，其中每个实参都由变量名和值组成；
# 还可使用列表和字典。

# 8.2.1 位置实参
# 调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
# 为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
# 1.调用函数多次
describe_pet('dog', 'willie')
# 2.位置参数的顺序很重要
describe_pet('harry', 'hamster')

# 8.2.2 关键字参数
describe_pet(animal_type='hamster', pet_name='harry')
# 关键字实参的顺序无关紧要，因为Python知道各个值该存储到哪个形参中。
describe_pet(pet_name='harry', animal_type='hamster')

# 8.2.3 默认值
# 编写函数时，可给每个形参指定默认值。
# 在调用函数中给形参提供了实参时，Python将使用指定的实参值；
# 否则，将使用形参的默认值。

# 这里修改了函数describe_pet()的定义，
# 在其中给形参animal_type指定了默认值'dog'。
# 这样，调用这个函数时，如果没有给animal_type指定值，
# Python将把这个形参设置为'dog'：


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
# 这个实参将关联到函数定义中的第一个形参——pet_name
describe_pet('willie')
# 如果要描述的动物不是小狗，可使用类似于下面的函数调用：
describe_pet(pet_name='harry', animal_type='hamster')

# 注意　使用默认值时，在形参列表中必须先列出没有默认值的形参，
# 再列出有默认值的形参。这让Python依然能够正确地解读位置实参。

# 8.2.4 等效的函数调用
# 鉴于可混合使用位置实参、关键字实参和默认值，
# 通常有多种等效的函数调用方式。

# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# 注意　使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。
# 使用对你来说最容易理解的调用方式即可。

# 8.2.5 避免实参错误
