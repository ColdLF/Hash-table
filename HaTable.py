class LinearMap(object):
    def __init__(self):
        self.items = []

    def add(self, k, v):
        self.items.append((k, v))

    def get(self, k):
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError


class BetterMap(object):
    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)


class HashMap(object):
    def __init__(self):

        self.maps = BetterMap(2)
        self.num = 0

    def get(self, k):
        return self.maps.get(k)

    def add(self, k, v):

        if self.num == len(self.maps.maps):
            self.resize()

        self.maps.add(k, v)
        self.num += 1

    def resize(self):

        new_maps = BetterMap(self.num * 2)

        for m in self.maps.maps:
            for k, v in m.items:
                new_maps.add(k, v)

        self.maps = new_maps


if __name__ == "__main__":
    table = BetterMap()
    pricedata = [("Hohner257", 257),
                 ("SW1664", 280),
                 ("SCX64", 1090),
                 ("SCX48", 830),
                 ("Super64", 2238),
                 ("CX12", 1130),
                 ("Hohner270", 620),
                 ("F64C", 9720),
                 ("S48", 1988)]

    for item, price in pricedata:
        table.add(k=item, v=price)

    print(table.get("CX12"))
    # >>> 1130
    print(table.get("QIMEI1248"))
    # >>> raise KeyError
