# The whole system plan and documentation

1) Documentation implementation for the system

2) Ability to do statistical Analysis using Data Science Libraries

3) Rendering PDF

4) Manipulating Excel software

5) Messaging Framework

6) Social Media Site

7) Authentication Middle

8) Payment Gateway

9) Billing System

10) Track the student attendance

11) Send Text Messages to Multiple Parents with a single click

12) Access Student Biographical and contact at any given time

13) Enter assesment result via system

14) Parent can login and access student acadamic record and fee balance

_______________________________________________________________________________________________________
/                                                   /
    /                                           /
        /                                   /
            /Symotedz Analytics System/

________________________________________________________________________________________________________
________________________________________________________________________________________________________
/                                                       /
    /                                                      /    ===============systemarchitect.md
        /   SYSTEMS DESIGN AND ARCHITECTURE  /
________________________________________________________________________________________________________

+++++++++++++++++++SYSTEMS PACKAGES PLAN


using xhtml2pdf to generate pdfs automatically
Using built in csv module from python to generate csv files
Using data science libraries to read uploaded csv files and Analyze them:::specifically(numpy, pandas)

## modules:

- Student Management Module: This module manages all aspects of student data, including admissions, enrollments, attendance, grades, and transcripts.
- Staff Management Module: This module manages all aspects of staff data, including hiring, payroll, benefits, and performance reviews.
- Curriculum Management Module: This module manages all aspects of the curriculum, including courses, schedules, and assignments.
- Attendance Management Module: This module tracks student attendance and generates attendance reports.
- Grading Management Module: This module records student grades and generates grade reports.
- Fee Management Module: This module manages student fees and generates fee statements.
- Communication Management Module: This module sends notifications to students, parents, and staff.
- Reporting Module: This module generates reports on various aspects of the school, such as student performance, staff attendance, and financial performance.

# issues on the system 
1) - api super admin - # issues on transportation request
2) - Api super admin - # issue on school block
3) - API parent - # issue on transportaion request
4) - 


## authentication system
### The interfaces:::
- Super Admin
- Admin
- Teacher
- Accountant
- Librarian
- Student
- Parent

- Generating admin form in the super-admin and admin interface that will input the password
- And Then other interfaces will login to the portal using username and password provided.
- Admin will be provided login credentials from super-admin portal
- There is one user login form only,,so depending on the input credential system should know the user, and redirect him/her to her interface
- portal.
- Login, Logout, Cookies, LocalStorage(indexedDB)
- Implementing JWT(json web token)
- Hashing the password and adding the salt 


