# SQL Project: Employee Management System Analysis

This project contains SQL scripts that perform various data analysis tasks on an employee management system. The database schema involves tables related to employees, departments, projects, rewards, qualifications, and performance. The project demonstrates the use of SQL for data retrieval, aggregation, nested queries, and joins, providing valuable insights into the employee management system.

## Table of Contents

- [Project Overview](#project-overview)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Conclusion](#conclusion)

## Project Overview

The objective of this project is to analyze data in an employee management system using SQL. The database contains multiple tables, including `EMPLOYEE`, `DEPARTMENT`, `PROJECT`, `REWARD`, `QUALIFICATION`, `PERFORMANCE`, and `GOAL`. The analysis involves various SQL operations such as:

- Simple data retrieval
- Aggregate functions for summarizing data
- Nested queries for complex data filtering
- Join operations for combining data from multiple tables

## Database Schema

The project uses the following database schema:

- **EMPLOYEE**: Employee details like ID, name, mail ID, hire date, job title, and performance ID.
- **LEAVE**: Employee leave records, including leave ID, start and end dates, reason, and associated employee ID.
- **PROJECT**: Details of projects, including project ID, title, and associated department ID.
- **DEPARTMENT**: Information on various departments.
- **PROJECT_ASSIGNMENT**: Links projects to departments.
- **WORKS_ON**: Links employees to project assignments.
- **QUALIFICATION**: Employee qualifications.
- **UG, PG, PhD**: Detailed tables for specific qualification types (Undergraduate, Postgraduate, PhD).
- **QUALIFIED**: Links employees to their qualifications.
- **REWARD**: Rewards given to employees.
- **MONETARY, NON_MONETARY**: Detailed reward types.
- **PERFORMANCE**: Employee performance scores.
- **GOAL**: Goals associated with employee performance.

## Getting Started

To run the SQL scripts provided in this project, you will need access to a SQL database. The project assumes you are familiar with basic SQL operations and have an environment set up for executing SQL queries.

## How to Use

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/keshiarun01/sql-employee-management.git
   ```

2. Open the SQL file in your preferred SQL client.

3. Execute the queries step-by-step to perform the analysis.

## Conclusion

This project provides a comprehensive overview of SQL capabilities in analyzing employee management data. It showcases various SQL techniques such as data retrieval, aggregation, nested queries, and joins to provide meaningful insights from the data.

Feel free to contribute by adding more queries or optimizing the existing ones!
