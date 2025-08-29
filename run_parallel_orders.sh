#!/bin/bash

# Create logs directory if it doesn't exist
mkdir -p logs

# Clear any existing log files
rm -f logs/order_*.log

echo "Starting 10 parallel instances of order_connect.py..."
echo "Logs will be saved in the 'logs' folder"
echo "================================================"

# Record start time
start_time=$(date +%s)
start_time_readable=$(date)

# Array to store process IDs
pids=()

# Start 10 parallel processes
for i in {1..10}; do
    echo "Starting instance $i..."
    python3 order_connect.py > logs/order_instance_$i.log 2>&1 &
    pids+=($!)
done

echo "All 10 instances started. PIDs: ${pids[@]}"
echo "Waiting for all processes to complete..."

# Wait for all background processes to complete
for pid in "${pids[@]}"; do
    wait $pid
    echo "Process $pid completed"
done

# Record end time
end_time=$(date +%s)
end_time_readable=$(date)

# Calculate execution time and RPS
execution_time=$((end_time - start_time))
total_requests=150  # 10 instances * 15 requests each
rps=$(echo "scale=2; $total_requests / $execution_time" | bc -l)

echo "================================================"
echo "All instances completed!"
echo "Execution Summary:"
echo "- Start time: $start_time_readable"
echo "- End time: $end_time_readable"
echo "- Total execution time: ${execution_time} seconds"
echo "- Total requests: $total_requests"
echo "- Requests per second (RPS): $rps"
echo "================================================"
echo "Check the logs folder for individual instance outputs:"
ls -la logs/

# Optional: Create a summary log
echo "Creating summary log..."
echo "Summary of all parallel order creation attempts" > logs/summary.log
echo "Generated at: $(date)" >> logs/summary.log
echo "================================================" >> logs/summary.log
echo "EXECUTION STATISTICS:" >> logs/summary.log
echo "- Start time: $start_time_readable" >> logs/summary.log
echo "- End time: $end_time_readable" >> logs/summary.log
echo "- Total execution time: ${execution_time} seconds" >> logs/summary.log
echo "- Total requests: $total_requests (10 instances × 15 requests each)" >> logs/summary.log
echo "- Requests per second (RPS): $rps" >> logs/summary.log
echo "================================================" >> logs/summary.log

for i in {1..10}; do
    echo "" >> logs/summary.log
    echo "=== Instance $i ===" >> logs/summary.log
    if [ -f "logs/order_instance_$i.log" ]; then
        cat logs/order_instance_$i.log >> logs/summary.log
    else
        echo "Log file not found for instance $i" >> logs/summary.log
    fi
done

echo "Summary log created at logs/summary.log"
echo "Individual logs available at logs/order_instance_[1-10].log"

# Display summary log content in terminal
echo ""
echo "================================================"
echo "SUMMARY LOG CONTENT:"
echo "================================================"
cat logs/summary.log