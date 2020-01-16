class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + "\n")
        print(self.cuisine_type)

    def open_restaurant(self):
        print("is open")


ss = Restaurant('jhon', 'cn')
ss.describe_restaurant()
ss.open_restaurant()
