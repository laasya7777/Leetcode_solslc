class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = []
        for row in bank:
            count = row.count('1')
            if count > 0:
                devices.append(count)
        
        total = 0
        for i in range(1, len(devices)):
            total += devices[i] * devices[i - 1]
        
        return total
