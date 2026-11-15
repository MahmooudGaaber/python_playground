CREATE DATABASE IF NOT EXISTS attendance_db;

USE attendance_db;

CREATE TABLE IF NOT EXISTS students (
      roll_no INT UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
      email VARCHAR(255) NOT NULL UNIQUE 
        CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'),
      student_name VARCHAR(255) NOT NULL ,
      ci_absences INT UNSIGNED NOT NULL DEFAULT 0,
      python_absences INT UNSIGNED NOT NULL DEFAULT 0,
      ds_absences INT UNSIGNED NOT NULL DEFAULT 0
      );
