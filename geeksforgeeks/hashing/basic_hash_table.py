'''
reference link
http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/

https://www.geeksforgeeks.org/hashing-set-1-introduction/
'''

country_code = [(25, 'USA'), (20, 'India'), (10, 'Nepal'), (56, 'Australia')]

hash_table = [None] * 10

def search(hash_table, key):
    return hash_table[hash_func(key)]
        
def hash_func(key):
    return key % len(hash_table)

def insert_hash_table(hash_table, key, value):
    hash_key = hash_func(key)
    hash_table[hash_key] = value

insert_hash_table(hash_table, 20, 'India')    
insert_hash_table(hash_table, 25, 'USA')
insert_hash_table(hash_table, 56, 'Australia')
print(search(hash_table, 56))
print(hash_table)