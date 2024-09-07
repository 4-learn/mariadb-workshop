## 解答

##### **步驟 1：建立資料庫**
```sql
CREATE DATABASE class_grades;
```

##### **步驟 2：創建資料表**
```sql
USE class_grades;

CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  subject VARCHAR(50),
  grade INT
);
```

##### **步驟 3：新增三筆資料**
```sql
INSERT INTO students (id, name, subject, grade) 
VALUES 
(1, 'Student A', 'Math', 85),
(2, 'Student B', 'English', 90),
(3, 'Student C', 'Science', 75);
```

##### **步驟 4：更新第二筆資料的成績**
```sql
UPDATE students 
SET grade = 95 
WHERE id = 2;
```

##### **步驟 5：新增 `bonus_points` 欄位**
```sql
ALTER TABLE students 
ADD bonus_points INT DEFAULT 0;
```

##### **步驟 6：刪除資料表**
```sql
DROP TABLE students;
```

##### **步驟 7：刪除資料庫**
```sql
DROP DATABASE class_grades;
```
