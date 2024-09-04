from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products = file.read()
        return products
    def add(self, *products):
        with open(self.__file_name, 'a') as file:
            for product in products:
                if self.check_if_product_exists(product.name):
                    file.write(f'{product}\n')
                else:
                    print(f'Продукт {product.name} уже в магазине')
    def check_if_product_exists(self, name):
        with open(self.__file_name, 'r') as file:
            for line in file:
                if name in line:
                    return False
                else:
                    return True

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())