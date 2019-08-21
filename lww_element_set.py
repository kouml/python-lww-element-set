class LwwElementSet:
    def __init__(self):
        self.addition_set = {}
        self.removal_set = {}

    def add(self, value, timestamp):
        if value in self.addition_set:
            prev_timestamp = self.addition_set[value]
            if timestamp >= prev_timestamp:
                self.addition_set[value] = timestamp
        else:
            self.addition_set[value] = timestamp

    def remove(self, value, timestamp):
        if value in self.removal_set:
            prev_timestamp = self.removal_set[value]
            if timestamp >= prev_timestamp:
                self.removal_set[value] = timestamp
        else:
            self.removal_set[value] = timestamp

    def merge(self, other_lww):
        for v, t in other_lww.addition_set.items():
            if v in self.addition_set:
                if t >= self.addition_set[v]:
                    self.addition_set[v] = t
            else:
                self.addition_set[v] = t
        for v, t in other_lww.removal_set.items():
            if v in self.removal_set:
                if t >= self.removal_set[v]:
                    self.removal_set[v] = t
            else:
                self.removal_set[v] = t

    def get_all(self):
        elements = []
        for v, t in self.addition_set.items():
            if v in self.removal_set:
                if t >= self.removal_set[v]:
                    elements.append(v)
            else:
                elements.append(v)
        return elements

    def get_element_with_timestamp(self, v):
        if v in self.addition_set and v in self.removal_set:
            if self.addition_set[v] < self.removal_set[v]:
                return None
            else:
                return self.addition_set[v]

        if v in self.addition_set:
            return self.addition_set[v]
        else:
            return None
