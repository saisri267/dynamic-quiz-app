Dynamic Quiz Application
Project Summary

This project is a Dynamic Quiz Application developed using PHP, HTML, CSS, and JavaScript. The application allows users to select quiz categories and difficulty levels, attempt time-based questions, and receive a detailed result analysis at the end. The system is designed to provide both learning and assessment by showing explanations for incorrect answers. Selenium WebDriver is used to automate testing and validate application functionality.

Landing Page Description

The landing page is the entry point of the application where users can select the quiz category (such as Web Technologies or Computer Networking) and difficulty level (Easy, Medium, or Hard). This page ensures users customize their quiz experience before starting. The interface is simple, user-friendly, and responsive across devices.

Question Display Page

After starting the quiz, questions are displayed one at a time along with multiple-choice options. Each question has a countdown timer that limits the time available to answer. Users can select an option and move to the next question using the Next button. If no option is selected, a warning message is shown to guide the user.

Result and Analysis Page

Once the quiz is completed, a result page is displayed showing the total score, percentage, and a progress bar representing performance. The page also provides a detailed analysis of each question, showing the user’s answer, the correct answer, and an explanation for wrong answers. A congratulatory message is displayed at the end to motivate users.

Frontend Code (HTML, CSS, JavaScript)

HTML is used to structure the web pages, including forms, buttons, and question containers. CSS is used to design an attractive and responsive user interface with proper layouts, colors, animations, and progress bars. JavaScript handles the core quiz logic such as loading questions dynamically, managing the timer, validating answers, displaying warnings, calculating scores, and generating the result analysis.

Backend (PHP)

PHP is used as the backend to handle page navigation and user selections. It processes the selected category and difficulty level and loads the quiz page dynamically using URL parameters. PHP acts as a lightweight server-side layer without using a database, keeping the application simple while ensuring smooth integration between pages.

Features Implemented

Category and difficulty selection to customize the quiz experience.

Dynamic loading of questions and options using JavaScript.

Countdown timer for each question with automatic navigation when time expires.

Warning message for negative cases when no option is selected.

Automatic movement to the next question after answer selection or timeout.

Dynamic score calculation based on correct answers.

Progress bar showing overall performance percentage.

Detailed result analysis with explanations for wrong answers.

Responsive UI compatible with desktop, tablet, and mobile devices.

Selenium-based automation testing covering positive and negative scenarios.

Automation Strategy

Automation testing is implemented using Selenium WebDriver with Python. The automation script verifies the landing page, quiz start, first question loading, negative case handling, random answer selection, and result verification. Screenshots are captured for important test cases such as landing page, warning display, question answering, and result page to provide visual proof of test execution.

Test Cases Summary

The application is tested using multiple test cases including landing page verification, quiz start and first question load, negative scenario validation when no option is selected, positive flow by answering questions, and result and score verification. These test cases ensure that the application behaves correctly for both valid and invalid user actions.

Deployment

The project is deployed using a PHP-supported hosting platform such as InfinityFree or Render (via Docker). Render is used with a Dockerfile that runs Apache and PHP, enabling server-side PHP execution in a production-like environment. GitHub is used for version control and deployment integration.

Technologies Used

HTML, CSS, JavaScript

PHP

Python & Selenium WebDriver

XAMPP (Local Server)

Git & GitHub

Render / InfinityFree (Deployment)

Final Result

The final outcome is a fully functional dynamic quiz application with category-based questions, timer functionality, detailed result analysis, and automation testing support. The project successfully demonstrates frontend development, backend integration using PHP, and automated testing using Selenium, making it suitable for academic submission and practical learning.
