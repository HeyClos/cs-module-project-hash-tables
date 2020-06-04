class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.item_count = 0
        self.storage = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.capacity)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # items in storage / capacity
        # # number of things stored in the hash table / number of slots in the array

        # When computing the load, keep track of the number of items in the hash table as
        # you go.

        # * When you put a new item in the hash table, increment the count
        # * When you delete an item from the hash table, decrement the count

        # When is the hash table overloaded?

        # * It's overloaded when load factor > 0.7
        # * It's underloaded when load factor < 0.2 (Stretch)
        return self.item_count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
            return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Follow the pointer strategy!
        # new.next = current.head
        # current.head = new.value
        # once more than one value goes into one key, it becomes a LL

        # Find the slot for the key
        current_index = self.hash_index(key)
        # Search the linked list for the key
        key_in_LL = self.storage[current_index]
        # If found, update it
        while key_in_LL is not None and key_in_LL != key:
            key_in_LL = key_in_LL.next

        if key_in_LL is not None:
            key_in_LL.value = value
            
        # If not found, make a new HashTableEntry and add it to the list
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[current_index]
            self.storage[current_index] = new_entry
            self.item_count = +1
            
            if self.get_load_factor() > 0.7:
                self.resize(self.storage * 2)
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # Follow the pointer strategy!

        # Find the slot for the key
        # Search the linked list for the key
        # If found, delete it from the linked list, then return the deleted value
        # If not found, return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # Find the slot for the key
        # Search the linked list for the key
        # If found, return the value
        # If not found, return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity

        # In a nutshell, take everything out of the old hash table array, and put it in a
        # new, resized array.

        # 1. Allocate a new array of bigger size, typically double the previous size
        # (or half the size if resizing down, down to some minimum)

        # 2. Traverse the old hash table -- O(n) over the number of elements in the hash
        # table

        # For each of the elements:
        #     Figure it's slot in the bigger (or smaller), new array
        #     Put it there
        # for x in
        # Automatically do this when the hash table is overloaded, or underloaded
        # (stretch).



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
