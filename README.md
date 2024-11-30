# Consistency
- [Consistency](#consistency)
    - [Description](#description)
    - [Needs](#needs)
    - [Tech Stack](#tech-stack)
    - [DB Layout](#db-layout)
    - [Queries](#queries)

### Description
* The aim of this project is to create an application that tracks habits and creates *consistency*.

The lack of habit tracking applications that fit my needs has prompted me to start developing my own.
****
### Needs
- Simple command prompts to add/retrieve info
- Very lightweight and maintainable
- Suited for myself
****
### Tech Stack
Database - MySQL
### DB Layout
| id       | Task          | Desc                 | Freq    |
| -------- | ------------- | -------------------- | ------- |
| 1        | Bible Reading | daily bible reading  | Daily
| 2        | Work Out      | push pull legs split | Daily
| 3        | Clean Room    |""                    | Weekly
### Queries
<u>AddTask</u> `INSERT INTO Habits VALUES (id, task, desc, freq)`  
<u>DeleteTask</u> `DELETE FROM Habits WHERE id=input`  
<u>ShowTasks</u> `SELECT * FROM Habits`