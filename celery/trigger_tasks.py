# trigger_tasks.py
from celery_app import add
import random
import time

time.sleep(20)  # Wait for RabbitMQ and workers to be ready

# Store task results for later retrieval
results = []

# Trigger the `add` task 100 times with random values
for i in range(100):
    x = random.randint(1, 10)  # Random integer between 1 and 10
    y = random.randint(1, 10)  # Random integer between 1 and 10
    result = add.delay(x, y)
    results.append((i+1, x, y, result))  # Store task info and result reference
    print(f"Task {i+1} submitted: add({x}, {y})")

# Optionally, wait some time before checking results
time.sleep(20)

# Retrieve and print task results as they complete
for task_id, x, y, result in results:
    try:
        # Get the result with a timeout to avoid blocking indefinitely
        output = result.get(timeout=10)
        print(f"Task {task_id}: add({x}, {y}) = {output}")
    except Exception as e:
        print(f"Task {task_id}: add({x}, {y}) failed with error: {e}")

