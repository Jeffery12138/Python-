def make_sandwich(*addings):
    """概述顾客点的三明治"""
    print("\nMaking a sandwich with the following addings:")
    for adding in addings:
        print("- "+adding)


make_sandwich('beef')
make_sandwich('beef', 'mushrooms', 'banana')
make_sandwich('chicken', 'green pepper')