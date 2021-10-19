def flights(*args):
    flights = {}
    finish_index = args.index('Finish')
    for i in range(0, finish_index, 2):
        k, v = args[i], args[i+1]
        if k in flights:
            flights[k] += v
        else:
            flights[k] = v
    return flights

# test
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))