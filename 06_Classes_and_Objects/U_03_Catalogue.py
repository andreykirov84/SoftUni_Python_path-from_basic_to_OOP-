class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)

    def get_by_letter(self, first_letter):
        result = []
        for product in self.products:
            if list(product)[0] == first_letter:
                result.append(product)
        return result

    def __repr__(self):
        final_repr = "Items in the {name} catalogue:\n"
        self.products.sort()
        for i in range(len(self.products) - 1):
            final_repr += f'{self.products[i]}\n'
        final_repr += f'{self.products[-1]}'
        return final_repr


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)


