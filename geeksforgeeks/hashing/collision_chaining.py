country_code = [(25, 'USA'), (20, 'India'), (10, 'Nepal'), (56, 'Australia')]

'''
While inserting a new element into the hash table, we first search if the key already exists in the hash table.

If the key is already present in the hash table, then we update its value with the new one.
Otherwise, we insert a new key-value pair into the hash table.
'''

hash_table = [[] for _ in range(10)]
#print(hash_table)

#generate hash key
def hash_func(key):
    return key % len(hash_table)

#insert into hash table
def insert_hash_table(hash_table, key, value):
    hash_key = hash_func(key)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if(key == k):
            print("&&&&&&")
            key_exists = True
            break;
    if key_exists:
        print("********")
        bucket[i] = ((key, value))
    else:
        print("####")
        bucket.append((key, value))

#search from hash table
def search(hash_table, key):
    hash_key = hash_func(key)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if(key == k):
            return v


#delete from hash table

def delete(hash_table, key):
    hash_key = hash_func(key)
    bucket = hash_table[hash_key]
    key_exists = False
    for i, kv in enumerate(bucket):
        k, v = kv
        if(key == k):
            key_exists = True
            break;
    if key_exists:
        del bucket[i]
        print('{} deleted'.format(key))
    else:
        print('{} key does not exists'.format(key))



insert_hash_table(hash_table, 20, 'India')
print(hash_table)
insert_hash_table(hash_table, 10, 'Nepal')
print(hash_table)
insert_hash_table(hash_table, 20, 'India')
print(hash_table)

print(search(hash_table, 20))

delete(hash_table, 10)
print(hash_table)



