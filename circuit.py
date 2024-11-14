t = int(input())
for _ in range(t):
    n = int(input())
    switches = list(map(int, input().split()))
    
    # Count the number of "on" switches
    o = switches.count(1)
    
    # Calculate minimum and maximum lights that can be on
    min_lights_on = max(0, o - n)
    max_lights_on = min(o, n)
    
    # Output the results
    print(min_lights_on, max_lights_on)
