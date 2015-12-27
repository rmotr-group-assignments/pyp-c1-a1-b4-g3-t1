Test fibonacci generator (do this for both recursive and non-recursive functions)

| Input | Output           |
|-------|------------------|
| 0     | 0                |
| 1     | 1                |
| 2     | 1                |
| 3     | 2                |
| 10    | 55               |
| 40    | 102334155        |

Test that a user must correctly input the recursive option 

| Input | Output                     |
|-------|----------------------------|
| y     | true                       |
| Y     | true                       |
| n     | false                      |
| N     | false                      |
| apple | raise ValueError |
| never | raise ValueError |
| yorp  | raise ValueError |

Test that a user must input a correct number

| Input | Output                 |
|-------|------------------------|
| 13    | return 13              |
| apple | raise ValueError |
| four  | raise ValueError |
| 10.5  | raise ValueError |
| -5    | raise ValueError |
