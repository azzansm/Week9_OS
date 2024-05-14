cylinder_max = 5000

def read_requests(filename):
    requests = []
    with open(filename, 'r') as file:
        for line in file:
            requests.append(int(line.strip()))
    return requests

def calculate_total_movement(arr, initial_pos):
    total_movement = abs(initial_pos - arr[0])
    for i in range(1, len(arr)):
        total_movement += abs(arr[i] - arr[i - 1])
    return total_movement

def fcfs(req, initial_pos):
    original_movement = calculate_total_movement(req, initial_pos)
    optimized_movement = abs(initial_pos - req[-1])
    return original_movement, optimized_movement

def optimized_fcfs(req, initial_pos):
    req.sort()
    return fcfs(req, initial_pos)

def scan(req, initial_pos):
    sorted_requests = sorted(req)
    start_index = 0
    while start_index < len(req) and sorted_requests[start_index] < initial_pos:
        start_index += 1
    total_movement = abs(initial_pos - sorted_requests[start_index % len(req)])
    for i in range(start_index, len(req) - 1):
        total_movement += abs(sorted_requests[i + 1] - sorted_requests[i])
    total_movement += abs(sorted_requests[-1] - sorted_requests[0])
    for i in range(0, start_index - 1):
        total_movement += abs(sorted_requests[i + 1] - sorted_requests[i])
    optimized_movement = abs(initial_pos - sorted_requests[start_index % len(req)])
    for i in range(start_index, len(req) - 1):
        optimized_movement += abs(sorted_requests[i + 1] - sorted_requests[i])
    return total_movement, optimized_movement

def cscan(req, initial_pos):
    sorted_requests = sorted(req)
    start_index = 0
    while start_index < len(req) and sorted_requests[start_index] < initial_pos:
        start_index += 1
    total_movement = abs(initial_pos - sorted_requests[start_index % len(req)])
    for i in range(start_index, len(req) - 1):
        total_movement += abs(sorted_requests[i + 1] - sorted_requests[i])
    total_movement += abs(cylinder_max - 1 - sorted_requests[-1])
    total_movement += cylinder_max - 1
    total_movement += sorted_requests[0]
    for i in range(0, start_index - 1):
        total_movement += abs(sorted_requests[i + 1] - sorted_requests[i])
    optimized_movement = abs(initial_pos - sorted_requests[start_index % len(req)])
    for i in range(start_index, len(req) - 1):
        optimized_movement += abs(sorted_requests[i + 1] - sorted_requests[i])
    optimized_movement += abs(cylinder_max - 1 - sorted_requests[-1])
    optimized_movement += cylinder_max - 1
    return total_movement, optimized_movement

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage:", sys.argv[0], "<initial head position> <file name>")
        sys.exit(1)
    initial_pos = int(sys.argv[1])
    requests = read_requests(sys.argv[2])
    fcfs_original, fcfs_optimized = fcfs(requests, initial_pos)
    scan_original, scan_optimized = scan(requests, initial_pos)
    cscan_original, cscan_optimized = cscan(requests, initial_pos)

    print("Task 1")
    print("FCFS total head movements:", fcfs_original)
    print("SCAN total head movements:", scan_original)
    print("C-SCAN total head movements:", cscan_original)
    
    print("Task 2")
    print("FCFS optimized total head movements:", fcfs_optimized)    
    print("SCAN optimized total head movements:", scan_optimized)
    print("C-SCAN optimized total head movements:", cscan_optimized)
