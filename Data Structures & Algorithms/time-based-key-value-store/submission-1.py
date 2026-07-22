class Node:
    def __init__(self, value="", timestamp=-1, nextv=None):
        self.value = value
        self.timestamp = timestamp
        self.nextv = nextv


class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = Node()  # dummy head

        dummy = self.timemap[key]
        prev = dummy
        curr = dummy.nextv

        # Find the correct sorted position
        while curr and curr.timestamp < timestamp:
            prev = curr
            curr = curr.nextv

        # Replace the value if this timestamp already exists
        if curr and curr.timestamp == timestamp:
            curr.value = value
            return

        # Insert between prev and curr
        new_node = Node(
            value=value,
            timestamp=timestamp,
            nextv=curr
        )
        prev.nextv = new_node

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        curr = self.timemap[key].nextv
        result = ""

        while curr and curr.timestamp <= timestamp:
            result = curr.value
            curr = curr.nextv

        return result