# define the capacity of the cache
capacity = int(input("Enter the capacity of the cache: "))

# initialize an empty cache and a list to track the order of keys
cache = {}
key_order = []

while True:
    # get the user's input
    user_input = input("Enter a key (or 'quit' to exit): ")
    
    # exit the loop if the user enters 'quit'
    if user_input == 'quit':
        break
    
    # check if the key is in the cache
    if user_input in cache:
        # if the key is in the cache, update its order in the key_order list
        key_order.remove(user_input)
        key_order.append(user_input)
        print("Value of key '" + user_input + "': " + str(cache[user_input]))
    else:
        # if the key is not in the cache, add it to the cache and the key_order list
        if len(cache) < capacity:
            # if the cache is not full, add the key and its value to the cache and the key_order list
            cache[user_input] = input("Enter the value for key '" + user_input + "': ")
            key_order.append(user_input)
        else:
            # if the cache is full, remove the least recently used key from the cache and the key_order list
            lru_key = key_order.pop(0)
            del cache[lru_key]
            # add the new key and its value to the cache and the key_order list
            cache[user_input] = input("Enter the value for key '" + user_input + "': ")
            key_order.append(user_input)

# print the final state of the cache
print("Final state of cache: " + str(cache))
