def phone_route_cost_check(filename, number):
    open_file = open(filename, 'r')
    data = open_file.readlines()

    number_cost = []
    for line in data:
        for i in range(0, len(line)):
            if line[i] == ',':
                print(i)
                number = line[0:i]
                price = line[i+1:-1]
                number_cost.append((number, price))
    # print( number_cost)
    open_file.close()

# print out the number of the phone numbers

phone_route_cost_check("route-costs-106000.txt", '+1412340')
# routefile = open("route-costs-106000.txt").read().split("\n")
# phonenum = "+861721532"
# print("Looking for", phonenum)
