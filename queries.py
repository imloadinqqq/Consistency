CreateTable = """DROP TABLE IF EXISTS habits;
                CREATE TABLE habits (
                    id INT PRIMARY KEY,
                    Task VARCHAR(255),
                    Desc VARCHAR(255),
                    Freq VARCHAR(255)
                );
                """
AddTask = "INSERT INTO habits VALUES (id, task, desc, freq)"
DeleteTask = "DELETE FROM habits WHERE id=input"
ShowTasks = "SELECT * FROM habits"
