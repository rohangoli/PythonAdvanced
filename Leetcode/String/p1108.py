## 1108. Defangind an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))