# Fetching-with-Threads
This Python script is designed to generate JSON data concurrently using multiple threads. It fetches product information from a dummy API (https://dummyjson.com/products/) and writes the JSON data to a file.

# Features:
Utilizes threading to improve performance by fetching and writing JSON data concurrently.
Distributes the workload evenly among threads, ensuring efficient processing.
Appends fetched JSON data to a file, handling the addition of commas and removing the last unnecessary comma.
Allows customization of the number of threads and the total number of loads (products) to generate.
Fetches product information from a dummy API for testing and demonstration purposes.
