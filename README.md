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
- [Workflow](#workflow)
- [Output](#output)
- [Tests](#tests)
- [Programs](#programs)
- [File Formats](#file-formats)
- [Project Structure](#project-structure)
- [Notes](#notes)

## Features

- **Versatile Question Types:**
  - *Single Choice:* Standard multiple-choice (one correct answer).
  - *Multiple Choice:* Select all that apply.
  - *Short Answer:* Text-based input.
- **Candidate Verification:** Secure login using Student IDs (SID) validated against a class roster.
- **Randomization:** Optional shuffling of answer choices to prevent copying.
- **Auto-Grading:** Immediate marking and score calculation upon completion.
- **Audit Logging:** All exam attempts and answers are logged to individual submission files.

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

The system is split into three programs representing different stages of the exam administration process.

### 1. Setup & Preview
**Script:** `program_one.py`

Parses the exam questions and allows an administrator to check if they are loaded correctly.

```bash
python program_one.py <exam_dir> <duration_minutes> [-r]
```
- `-r`: (Optional) Enable randomized answer shuffling.

**Example:**
```bash
python program_one.py info1110_test_1 60 -r
```

### 2. Assign & View
**Script:** `program_two.py`

Assigns the exam instance to candidates loaded from `students.csv`. Allows previewing the exam exactly as a specific student would see it.

```bash
python program_two.py <exam_dir> <duration_minutes> [-r]
```

**Interactive Controls:**
- Enter a **9-digit SID** to preview that student's specific exam paper.
- Enter `-a` to list all assigned candidates.
- Enter `-q` to quit and finish assignment.

### 3. Run Exam
**Script:** `program_final.py`

The final application used by students to take the exam. It combines setup, assignment, and execution.

```bash
python program_final.py <exam_dir> <duration_minutes> [-r]
```

## Workflow

1. Administrator launches the script.
2. System loads exam and candidates.
3. **Important:** Administrator must enter `-q` to exit the preview mode and switch to "Exam Mode".
4. Students enter their SID to log in and take the exam.
5. Results are saved to `<exam_dir>/submissions/<SID>.txt`.

## Output

Exam attempts are logged to `submissions/<SID>.txt` inside the exam directory.

## Tests

Run the manual test script for `Question.mark_response`:

```bash
python test_program.py
```

Compare the output against the expected results in `test_plan.md`.

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
├── question.py               # Question class with different types
├── exam.py                   # Exam class for managing exams
├── candidate.py              # Candidate class for exam takers
├── setup.py                  # File parsing and sorting helpers
├── program_one.py            # Setup and preview
├── program_two.py            # Candidate assignment
├── program_final.py          # Full exam workflow
├── info1110_test_1/          # Valid sample exam data
├── info1110_invalid_test/    # Invalid sample data for error handling
├── samples/                  # Example question formats
├── test_plan.md              # Test plan documentation
├── test_program.py           # Manual tests for Question.mark_response
└── README.md
```

## Notes

- When running `program_final.py`, you must quit the preview step with `-q` before candidate login begins.
