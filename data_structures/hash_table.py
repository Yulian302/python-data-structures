class HashTable(object):
    def __init__(self):
        self.table = []
        self.hash_funcs: dict[str:function] = {
            "one": self.hash_one,
            "two": self.hash_two,
        }

    def add(self, key: int, hash_func_name: str = "one"):
        if not hash_func_name in self.hash_funcs:
            raise Exception("No hash func found!")
        hashed = self.hash_funcs[hash_func_name](key)
        self.table.append(hashed)

    def find(self, key: int, hash_func_name: str = "one"):
        if not hash_func_name in self.hash_funcs:
            raise Exception("No hash func found!")
        idx = self.hash_funcs[hash_func_name](key)
        if idx < len(self.table):
            return self.table[idx]
        return None

    def hash_one(self, key: int, m: int = 5):
        return key % m

    def hash_two(self, key: int, m: int = 5):
        return key % m


hash_table = HashTable()
hash_table.add(10, hash_func_name="two")
print(hash_table.table)
print(hash_table.find(10, hash_func_name="two"))
