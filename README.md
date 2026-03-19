# Algorithm Efficiency and Performance Study

## Project Overview
This research project evaluates how different sorting algorithms perform as the amount of data increases. By testing Bubble Sort, Insertion Sort, and Merge Sort, this study identifies where code slows down and compares real-world results with theoretical Big O time complexity models.

## Technical Stack
* Language: Python 3.x
* Libraries: 
    * Matplotlib (Performance Visualization)
    * Time (Execution Timing)
    * Random (Dataset Generation)
* Environment: IDLE / Local Interpreter

## Research Methodology
* Performance Testing: Conducted precise timing of algorithms across different list sizes (from n=100 to n=2000).
* Data Type Analysis: Tested algorithms against "Random" and "Nearly Sorted" data to find the exact point where one algorithm becomes faster than another.
* Visualization: Generated performance graphs to clearly show the difference between O(n^2) and O(n log n) speed trends.

## Core Analysis Questions
1. Which algorithm is the fastest for large datasets?
   - Ans: Merge Sort. Its speed stays consistent even as the data size increases.
2. Which algorithm is the slowest as data size grows?
   - Ans: Bubble Sort. Its execution time rises very sharply, showing a clear curved line on the graph.
3. Does the type of data affect performance?
   - Ans: Yes. Insertion Sort is much faster on "Nearly Sorted" data compared to "Random" data.

## How to Run
1. Ensure matplotlib is installed: pip install matplotlib
2. Execute the script: python Sorting_Algorithm_Analysis.py
3. View the generated graph to see the speed comparison results.
