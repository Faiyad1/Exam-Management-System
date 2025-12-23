# Test Case Designs
Complete the given tables with details of your test case design for each question type.
State the values to initalize appropriate `Question` objects required for the test case.

Column descriptions:
* Test ID - Test case identification number
* Description - Type of testcase and brief explanation of test case details
* Inputs - Arguments into the method
* Expected Output - Return values of the method
* Status - pass/fail

Table 1: Summary of test cases for method `mark_response` for question type `short`

| Test ID | Description                         | Inputs  | Expected Output | Status |
| ------- | -----------                         | ------  | --------------- | ------ |
|    1    | Positive Case: Valid str            | '3Hi3'  | 0.0             |  Pass  |
|    2    | Positive Case: Valid answer         | 'Bob'   | 1.0             |  Pass  |
|    3    | Negative Case: Empty str            | ''      | 0.0             |  Pass  |
|    4    | Negative Case: Invalid type         |('A','B')| 0.0             |  Pass  |
|    5    | Edge Case: length one               | 'Z'     | 0.0             |  Pass  |
|    6    | Edge Case: int in str               | '1'     | 0.0             |  Pass  |


Table 2: Summary of test cases for method `mark_response` for question type `single`

| Test ID | Description                                    | Inputs | Expected Output | Status |
| ------- | -----------                                    | ------ | --------------- | ------ |
|    1    |Positive Case: Valid string option of length one| 'B'    | 1.0             |  Pass  |
|    2    |Positive Case: Valid string option of length one| 'C'    | 0.0             |  Pass  |
|    3    |Negative Case: Invalid type                     | 4      | 0.0             |  Pass  |
|    4    |Negative Case: Invalid length of str            | 'A, B' | 0.0             |  Pass  |
|    5    |Edge Case: Valid string option for A to D       | 'A'    | 0.0             |  Pass  |
|    6    |Edge Case: Valid string option for A to D       | 'D'    | 0.0             |  Pass  |


Table 3: Summary of test cases for method `mark_response` for question type `multiple`

| Test ID | Description                                  | Inputs      | Expected Output | Status |
| ------- | -----------                                  | ------      | --------------- | ------ |
|    1    |Positive Case: Valid string with valid options| 'A, B'      | 2.0             |  Pass  |
|    2    |Positive Case: Valid string with valid option | 'A'         | 1.0             |  Pass  |
|    3    |Negative Case: Invalid type                   | ['A, B']    | 0.0             |  Pass  |
|    4    |Negative Case: Invalid options                | 'E, F'      | 0.0             |  Pass  |
|    5    |Edge Case: Contains unnecessary values        |'A, B, E, :)'| 2.0             |  Pass  |
|    6    |Edge Case: Putting correct option twice       |'B, B, C, D' | 1.0             |  Pass  |

#
