Test fibonacci generator (do this for both recursive and non-recursive functions)

| Input | Output           |
|-------|------------------|
| 0     | 0                |
| 1     | 1                |
| 2     | 1                |
| 3     | 2                |
| 10    | 55               |
| 40    | 102334155        |
| 2.5   | raise ValueError |
| -10   | raise ValueError |
| -1    | raise ValueError |
| -1.5  | raise ValueError |

Test that a user must correctly input the recursive option 

| Input | Output                     |
|-------|----------------------------|
| y     | true                       |
| yes   | true                       |
| Y     | true                       |
| YES   | true                       |
| n     | false                      |
| no    | false                      |
| N     | false                      |
| NO    | false                      |
| apple | raise RecursiveOptionError |
| never | raise RecursiveOptionError |
| yorp  | raise RecursiveOptionError |

Test that a user must input a correct number

| Input | Output                 |
|-------|------------------------|
| 13    | return 13              |
| apple | raise FibNumValueError |
| four  | raise FibNumValueError |
| 10.5  | raise FibNumValueError |
| -5    | raise FibNumValueError |
