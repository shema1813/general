CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    subject VARCHAR(50),
    grade INT
);

INSERT INTO Students (student_id, name, age, subject, grade)
VALUES
(1, 'John', 20, 'Mathematics', 85),
(2, 'Sarah', 21, 'Biology', 92),
(3, 'Mike', 19, 'Physics', 78),
(4, 'Emma', 22, 'Chemistry', 88),
(5, 'David', 20, 'History', 95);

SELECT * FROM Students;

SELECT *
FROM Students
WHERE subject = 'Mathematics';

SELECT name, subject, grade
FROM Students
WHERE grade > 85;
