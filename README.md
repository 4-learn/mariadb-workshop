## 解答:

##### **步驟 1：創建資料庫**
```sql
CREATE DATABASE class_grades;
```

##### **步驟 2：創建資料表**
```sql
USE class_grades;

CREATE TABLE students_scores (
  student_id INT PRIMARY KEY,
  student_name VARCHAR(50),
  subject VARCHAR(50),
  score INT
);
```

##### **步驟 3：新增五筆學生資料**
```sql
INSERT INTO students_scores (student_id, student_name, subject, score) 
VALUES 
(1, 'Student A', 'Math', 85),
(2, 'Student B', 'English', 78),
(3, 'Student C', 'Science', 92),
(4, 'Student D', 'Math', 67),
(5, 'Student E', 'English', 88);
```

##### **步驟 4：查詢數學科目成績超過 80 分的學生**
```sql
SELECT * FROM students_scores
WHERE subject = 'Math' AND score > 80;
```

##### **步驟 5：計算每門科目的平均成績**
```sql
SELECT subject, AVG(score) AS average_score
FROM students_scores
GROUP BY subject;
```

##### **步驟 6：查詢每門課的最高分和最低分**
```sql
SELECT subject, MAX(score) AS highest_score, MIN(score) AS lowest_score
FROM students_scores
GROUP BY subject;
```

##### **步驟 7：刪除英文成績低於 80 的記錄**
```sql
DELETE FROM students_scores
WHERE subject = 'English' AND score < 80;
```
