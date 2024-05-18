import heapq

def min_cost_to_connect_cables(cable_lengths):
    if not cable_lengths:
        return 0

    heapq.heapify(cable_lengths)
    
    total_cost = 0

  
    while len(cable_lengths) > 1:
       
        first_min = heapq.heappop(cable_lengths)
        second_min = heapq.heappop(cable_lengths)
        
        
        current_cost = first_min + second_min
        total_cost += current_cost
        
       
        heapq.heappush(cable_lengths, current_cost)
    
    return total_cost


cable_lengths = [4, 3, 2, 6]
print(min_cost_to_connect_cables(cable_lengths))  