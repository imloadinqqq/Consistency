CreateTable = """DROP TABLE IF EXISTS habits;
                CREATE TABLE habits (
                    id INT AUTOINCREMENT PRIMARY KEY,
                    Task VARCHAR(255),
                    Desc VARCHAR(255),
                    Freq VARCHAR(255)
                );
                """
AddTask = "INSERT INTO habits (Task, Description, Frequency) VALUES (%s, %s, %s);"
DeleteTask = "DELETE FROM habits WHERE id=%s"
ShowTasks = "SELECT * FROM habits"
