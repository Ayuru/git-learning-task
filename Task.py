shopping_list = {
    "warzywniak" : ["chleb", "pączek", "bułki"],
    "piekarnia" : ["marchew", "seler", "rukola"]
}

result = "Lista zakupów:" \

counter = 0

for shop, products in shopping_list.items():
    print(shop.capitalize())
    capitalized_list = []
    for product in products:
        capitalized_list.append(product.capitalize())
        counter += 1

    result += "\nIdę do " + shop.capitalize() +", kupuję tu następujące rzeczy: " + str(capitalized_list) + "."

result += "\nW sumie kupuję " + str(counter) + " produktów."

print(result)
