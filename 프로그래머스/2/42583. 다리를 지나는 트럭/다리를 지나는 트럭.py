def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    bridge_weights = 0
    
    while(bridge):
        time += 1
        bridge.pop(0)
        bridge_weights = sum(bridge)
        if len(truck_weights) > 0:
            if bridge_weights + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        
    return time
            
    