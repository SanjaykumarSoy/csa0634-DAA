def calculate_race_strategy(num_laps, pit_stop_time):
  
    good_lap_time = 61 
    worn_lap_time = 63  

    # Create a DP array to store minimum times
    dp = [0] * (num_laps + 1)
    
    # Create a list to track pit stops
    pit_stops = [False] * (num_laps + 1)

    # Base case: 0 laps takes 0 time
    dp[0] = 0

    # Calculate minimum time for each lap
    for i in range(1, num_laps + 1):
        # Option 1: No pit stop (using worn tires)
        no_pit_stop = dp[i - 1] + worn_lap_time

        # Option 2: Pit stop (using good tires)
        pit_stop = (dp[i - 1] + good_lap_time + pit_stop_time) if i > 1 else (good_lap_time + pit_stop_time)

        # Choose the minimum time for this lap
        if pit_stop < no_pit_stop:
            dp[i] = pit_stop
            pit_stops[i] = True  # Mark this lap as a pit stop
        else:
            dp[i] = no_pit_stop

    # Display results
    print(f"Minimum Race Time: {dp[num_laps]} seconds")

    # Track and display pit stop laps
    pit_stop_laps = [lap for lap in range(1, num_laps + 1) if pit_stops[lap]]
    print(f"Pit Stops at Laps: {', '.join(map(str, pit_stop_laps))}")
num_laps = int(input("Enter the number of laps: "))
pit_stop_time = int(input("Enter the pit stop time (seconds): "))
calculate_race_strategy(num_laps, pit_stop_time)
