def minimum_shots(test_cases):
    results = []
    for case in test_cases:
        n, k, heights = case
        # If fewer than 3 players in total (including Gi-Hun and Ali), no players need to be removed.
        if n < 1:
            results.append(0)
        else:
            # Count players taller than Gi-Hun and Ali (height > k)
            shots = sum(1 for h in heights if h > k)
            results.append(shots)
    return results

# Example usage
if __name__ == "__main__":
    test_cases = [
        (4, 10, [2, 13, 4, 16]),  # Ali's height: 10
        (5, 8, [9, 3, 8, 8, 4]),  # Ali's height: 8
        (4, 6, [1, 2, 3, 4]),     # Ali's height: 6
        (0, 10, [])               # No players between Gi-Hun and Ali
    ]
    results = minimum_shots(test_cases)
   
for res in results:
    print(res)
