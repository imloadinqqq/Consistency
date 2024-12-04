CreateTable = """USE habits;
                DROP TABLE IF EXISTS tasks;
                CREATE TABLE tasks (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    Task VARCHAR(255),
                    Des VARCHAR(255),
                    Freq VARCHAR(255)
                );
                """
AddTask = "INSERT INTO tasks (Task, Des, Freq) VALUES (%s, %s, %s);"
DeleteTask = "DELETE FROM tasks WHERE id=%s"
ShowTasks = "SELECT * FROM tasks"
