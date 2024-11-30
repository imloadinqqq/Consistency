# Consistency
- [Consistency](#consistency)
    - [Description](#description)
    - [Needs](#needs)
    - [Commands](#commands)
    - [Tech Stack](#tech-stack)
  - [Database](#database)
    - [DB Layout](#db-layout)
    - [Queries](#queries)
    - [Example Output](#example-output)

### Description
* The aim of this project is to create an application that tracks habits and creates *consistency*.

The lack of habit tracking applications that fit my needs has prompted me to start developing my own.
****
### Needs
- Simple command prompts to add/retrieve info
- Very lightweight and maintainable
- Suited for myself
****
### Commands
Task is accessed with it's 'id'  
Basic CRUD operations 

`consistency add 'task'`  
`consistency del 'task'`    
`consistency update 'task'`  
`consistency show [task]`
****
### Tech Stack
Database - MySQL  
Language - Python  
## Database
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
### Example Output
Command: `consistency show`  
Output:
<table border="1">
  <thead>
    <tr>
      <th>id</th>
      <th>M</th>
      <th>T</th>
      <th>W</th>
      <th>TH</th>
      <th>F</th>
      <th>S</th>
      <th>SU</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>x</td>
      <td>o</td>
      <td>x</td>
      <td>x</td>
      <td>o</td>
      <td>o</td>
      <td>x</td>
    </tr>
    <tr>
      <td>2</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>o</td>
      <td>x</td>
      <td>o</td>
      <td>o</td>
    </tr>
    <tr>
      <td>3</td>
      <td>o</td>
      <td>o</td>
      <td>o</td>
      <td>o</td>
      <td>o</td>
      <td>x</td>
      <td>o</td>
    </tr>
  </tbody>
</table>

