class HashTable:
    def __init__(self, size: int = 53):
        self.keyMap = [[] for _ in range(size)]

    def _Hash(self, key: str) -> int:
        total = 0
        WEIRD_PRIME = 31

        for i in range(min(len(key), 100)):
            charCode = ord(key[i]) - 96
            total = (total + charCode * WEIRD_PRIME) % len(self.keyMap)
        return total

    def Set(self, key: str, value: any) -> list:
        index = self._Hash(key)
        if not self.keyMap[index]:
            self.keyMap[index] = []

        self.keyMap[index].append([key, value])

        return self.keyMap

    def Get(self, key: str) -> any:
        index = self._Hash(key)
        elements = self.keyMap[index]

        if elements:
            for element in elements:
                if element[0] == key:
                    return element[1]
        return None

    @property
    def Keys(self) -> list[str]:
        keys = []
        for bucket in self.keyMap:
            if bucket:
                for element in bucket:
                    keys.append(element[0])
        return keys

    @property
    def Values(self) -> list:
        values = set()
        for bucket in self.keyMap:
            if bucket:
                for element in bucket:
                    values.add(element[1])
        return list(values)
