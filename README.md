# Exam Management System

**INFO1110 - Introduction to Programming**  
The University of Sydney  
26 October 2023

<mark>**Academic Integrity:** The use of AI tools is not permitted for this assignment.</mark>

A text-based exam system for setting up exams, assigning them to candidates, and administering with auto-marking.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Output](#output)
- [Tests](#tests)
- [Programs](#programs)
- [File Formats](#file-formats)
- [Project Structure](#project-structure)
- [Notes](#notes)

## Features

- Support for multiple question types:
  - **Single choice** - One correct answer from four options
  - **Multiple choice** - Multiple correct answers from four options
  - **Short answer** - Free-form text responses
- Candidate management with SID verification
- Answer shuffling for randomized exams
- Automatic grading and mark calculation
- Exam submission logging

## Requirements

- Python 3.11
- No third-party packages

## Quick Start

Sample exam directories (`info1110_test_1/`, `samples/`) are included. Run directly:

```bash
python program_final.py info1110_test_1 60
```

For custom exams, create a directory with `questions.txt` and `students.csv`.

## Usage

```bash
python program_one.py info1110_test_1 60
python program_two.py info1110_test_1 69 -r
python program_final.py info1110_test_1 70
```

Interactive preview controls in `program_two.py`:
- Enter a 9-digit SID to preview one candidate
- `-a` to preview all candidates
- `-q` to quit preview mode

## Output

Exam attempts are logged to `submissions/<SID>.txt` inside the exam directory.

## Tests

Run the manual test script for `Question.mark_response`:

```bash
python test_program.py
```

Compare the output against the expected results in `test_plan.md`.

## Programs

- `program_one.py <exam_dir> <duration_minutes> [-r]` - Setup and optional exam preview.
- `program_two.py <exam_dir> <duration_minutes> [-r]` - Assign the exam and preview candidate views.
- `program_final.py <exam_dir> <duration_minutes> [-r]` - Full workflow, verifies candidates, runs the exam, writes submissions.

## File Formats

### questions.txt

Each question is separated by a blank line. Required fields:

```
Question - <Single|Multiple|Short>
<question text>
Possible Answers:
A. <option>
B. <option>
C. <option>
D. <option>
Expected Answer: <A|B|C|D|comma list|text>
Marks: <integer>
```

Notes:
- `Possible Answers` is required for Single and Multiple and must list A through D.
- Short questions omit the `Possible Answers` block.
- `Expected Answer` and `Marks` are required for all non-end questions.

### students.csv

Header row: `SID,Name,Extra Time`
- SID is a 9-digit number.
- Extra Time is in minutes and may be blank or 0.

Example:
```
SID,Name,Extra Time
500010347,Damian Carroll,
500594412,Morgan Valencia,10
```

## Project Structure

```
├── question.py           # Question class with different types
├── exam.py               # Exam class for managing exams
├── candidate.py          # Candidate class for exam takers
├── setup.py              # File parsing and sorting helpers
├── program_one.py        # Setup and preview
├── program_two.py        # Candidate assignment
├── program_final.py      # Full exam workflow
├── info1110_test_1/      # Valid sample exam data
├── info1110_invalid_test/# Invalid sample data for error handling
├── samples/              # Example question formats
├── test_plan.md          # Test plan documentation
└── test_program.py       # Manual tests for Question.mark_response
```

## Notes

- When running `program_final.py`, you must quit the preview step with `-q` before candidate login begins.
