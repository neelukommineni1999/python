CREATE TABLE employee_project (
    employee_id INT,
    project_id INT,
    assigned_date DATE,
    role VARCHAR(50),
    PRIMARY KEY (employee_id, project_id)
);