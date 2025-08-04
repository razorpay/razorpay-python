#!/bin/bash

# Create logs directory if it doesn't exist
mkdir -p logs

# Clear any existing log files
rm -f logs/order_*.log

echo "Starting 10 parallel instances of order_connect.py..."
echo "Logs will be saved in the 'logs' folder"
echo "================================================"

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

echo "================================================"
echo "All instances completed!"
echo "Check the logs folder for individual instance outputs:"
ls -la logs/

# Optional: Create a summary log
echo "Creating summary log..."
echo "Summary of all parallel order creation attempts" > logs/summary.log
echo "Generated at: $(date)" >> logs/summary.log
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