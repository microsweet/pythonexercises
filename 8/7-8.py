sandwich_orders = ['a', 'b', 'c']
finished_sandwiches = []
i = 3
while i > 0:
    sandwich = sandwich_orders.pop()
    print('I made your ' + sandwich + ' sandwich')
    finished_sandwiches.append(sandwich)
    i -= 1

print('sandwich_orders: ' + str(sandwich_orders))
print('finished_sandwiches' + str(finished_sandwiches))
