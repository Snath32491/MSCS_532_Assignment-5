Quicksort Algorithm: Implementation, Analysis, and Randomization

Overview
This project demonstrates the Quicksort algorithm in two versions:
- Deterministic Quicksort (with median-of-three pivot selection)
- Randomized Quicksort (random pivot selection)

The implementation includes:
- Detailed time and space complexity analysis.
- Empirical performance comparison across different input distributions (random, sorted, reverse-sorted).
- Graphical representation of runtime performance.

Files
- `deterministic_quicksort.py` – Implements deterministic Quicksort using median-of-three pivot selection.
- `randomized_quicksort.py` – Implements randomized Quicksort where the pivot is chosen randomly.
- `quicksort_analysis.py` – Runs both algorithms on different input sizes and distributions, measures runtime, and plots performance graphs.
- `Quicksort_Report.docx` – Detailed report including theoretical analysis, results, and discussion.
- `README.md` – This file.


How to Run
1. Clone the Repository
```bash
git clone https://github.com/Snath32491/MSCS_532_Assignment 5/quicksort-analysis.git
cd quicksort-analysis
```

2. Install Requirements
This project uses Python 3 and requires `matplotlib`:
```bash
pip install matplotlib
```

3. Run Analysis
Run the empirical analysis and generate graphs:
```bash
python quicksort_analysis.py
```


Empirical Results
The algorithms were tested on:
- Input sizes: `1,000`, `5,000`, `10,000`, `20,000`
- Distributions: random, sorted, reverse-sorted

Key Findings:
- Deterministic Quicksort is efficient on random data but performs poorly on sorted and reverse-sorted data (approaching O(n²)).
- Randomized Quicksort maintains performance close to O(n log n) across all distributions.
- Space usage matches theoretical predictions: O(log n) on average, O(n) in the worst case.


 Theoretical Complexity
| Case        | Time Complexity | Space Complexity |
|-------------|-----------------|------------------|
| Best Case   | O(n log n)      | O(log n)        |
| Average Case| O(n log n)      | O(log n)        |
| Worst Case  | O(n²)           | O(n)            |



