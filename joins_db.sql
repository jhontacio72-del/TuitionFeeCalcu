CREATE DATABASE joins_db
USE joins_db;
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_number VARCHAR(30) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    year_level INT NOT NULL
);

CREATE TABLE Instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    department VARCHAR(100) NOT NULL
);

CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_code VARCHAR(20) NOT NULL UNIQUE,
    course_title VARCHAR(100) NOT NULL,
    units INT NOT NULL,
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    semester VARCHAR(20) NOT NULL,
    school_year VARCHAR(20) NOT NULL,
    grade DECIMAL(5,2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

INSERT INTO Students (student_number, first_name, last_name, email, year_level)
VALUES
('2026-01', 'Jhon Patrick', 'Tacio', 'jhon.tacio@email.com', 1),
('2026-02', 'Keverne', 'Bunnag', 'keverne.bunnag@email.com', 2),
('2026-03', 'Vic', 'Estrada', 'vic.estrada@email.com', 3),
('2026-04', 'Anna', 'Lopez', 'anna.lopez@email.com', 1);

INSERT INTO Instructors (first_name, last_name, email, department)
VALUES
('Benedict', 'Pascua', 'benedict.pascua@email.com', 'Computer Science'),
('Dwight', 'Pascua', 'dwight.p@email.com', 'Information Technology'),
('Carlos', 'Mendoza', 'c.mendoza@email.com', 'Engineering');

INSERT INTO Courses (course_code, course_title, units, instructor_id)
VALUES
('CS101', 'Introduction to Programming', 3, 1),
('IT202', 'Database Systems', 3, 2),
('ENG301', 'Software Engineering', 3, 3),
('IT303', 'Cyber Security', 3, 2);

INSERT INTO Enrollments (student_id, course_id, enrollment_date, semester, school_year, grade)
VALUES
(1, 1, '2024-08-15', '1st Semester', '2024-2025', 90),
(2, 2, '2024-08-16', '1st Semester', '2024-2025', 88),
(3, 3, '2025-01-10', '2nd Semester', '2024-2025', 75);

SELECT 
    CONCAT(s.first_name, ' ', s.last_name) AS StudentName,
    c.course_title AS CourseName,
    e.grade AS Grade
FROM Enrollments e
INNER JOIN Students s ON e.student_id = s.student_id
INNER JOIN Courses c ON e.course_id = c.course_id;

SELECT 
    CONCAT(s.first_name, ' ', s.last_name) AS StudentName,
    c.course_title AS CourseName,
    e.grade AS Grade
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
LEFT JOIN Courses c ON e.course_id = c.course_id;

SELECT 
    CONCAT(s.first_name, ' ', s.last_name) AS StudentName,
    c.course_title AS CourseName,
    e.grade AS Grade
FROM Enrollments e
RIGHT JOIN Courses c ON e.course_id = c.course_id
LEFT JOIN Students s ON e.student_id = s.student_id;

SELECT 
    CONCAT(s.first_name, ' ', s.last_name) AS StudentName,
    c.course_title AS CourseName,
    CONCAT(i.first_name, ' ', i.last_name) AS Instructor,
    e.grade AS Grade
FROM Enrollments e
JOIN Students s ON e.student_id = s.student_id
JOIN Courses c ON e.course_id = c.course_id
JOIN Instructors i ON c.instructor_id = i.instructor_id;

SELECT 
    CONCAT(s.first_name, ' ', s.last_name) AS StudentName,
    c.course_title AS CourseName,
    e.grade AS Grade
FROM Enrollments e
JOIN Students s ON e.student_id = s.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE c.course_title = 'Database Systems'
AND e.grade > 85;

SELECT 
    CONCAT(s.first_name, ' ', s.last_name) AS StudentName,
    c.course_title AS CourseName,
    e.grade AS Grade
FROM Enrollments e
JOIN Students s ON e.student_id = s.student_id
JOIN Courses c ON e.course_id = c.course_id
ORDER BY e.grade DESC;