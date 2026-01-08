class Solution:
    def bestClosingTime(self, customers: str) -> int:
        totalY = customers.count('Y')
        
        open_no_customer = 0
        remaining_customers = totalY
        
        min_penalty = totalY  
        best_hour = 0
        
        for hour in range(len(customers)):
            if customers[hour] == 'Y':
                remaining_customers -= 1
            else:
                open_no_customer += 1
            
            penalty = open_no_customer + remaining_customers
            
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = hour + 1
        
        return best_hour
