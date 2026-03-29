# sql table

CREATE TABLE Teacher (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NOT NULL,
    birthday DATE,
    jmbg VARCHAR(13) UNIQUE,
    address VARCHAR(50) NOT NULL,
    subject VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE Student (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NOT NULL,
    birthday DATE,
    jmbg VARCHAR(13) UNIQUE,
    address TEXT,
    index_number VARCHAR(20) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE Subject (
    id SERIAL PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE Class (
    id SERIAL PRIMARY KEY,
    class_name VARCHAR(50),
    teacher_id INT REFERENCES Teacher(id),
    subject_id INT REFERENCES Subject(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE Student_in_class (
    id SERIAL PRIMARY KEY,
    class_id INT REFERENCES Class(id),
    student_id INT REFERENCES Student(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE Grade_in_class (
    id SERIAL PRIMARY KEY,
    class_id INT REFERENCES Class(id),
    student_id INT REFERENCES Student(id),
    teacher_id INT REFERENCES Teacher(id),
    grade_value INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);