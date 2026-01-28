# **Dynamic Quiz Application**

## **Project Summary**
This project is a **Dynamic Quiz Application** developed using **PHP, HTML, CSS, and JavaScript**. The application allows users to select quiz **categories** and **difficulty levels**, attempt **time-based multiple-choice questions**, and view a **detailed result analysis** at the end. The project also includes **Selenium automation testing** to validate functionality.

---

## **Landing Page**
The **landing page** is the entry point of the application where users can select the **quiz category** (Web Technologies or Computer Networking) and **difficulty level** (Easy, Medium, Hard). This page ensures users customize their quiz experience before starting. The interface is **clean, responsive, and user-friendly**.

---

## **Question Display Page**
After starting the quiz, questions are displayed **one at a time** along with **multiple-choice options**. Each question includes a **countdown timer** that limits the time available to answer. If the user clicks **Next** without selecting an option, a **warning message** is displayed, preventing accidental skipping.

---

## **Result and Analysis Page**
After completing the quiz, a **result page** is displayed showing the **total score**, **percentage**, and a **progress bar** representing performance. The page also provides a **detailed analysis** of each question, including the **user’s answer**, **correct answer**, and **explanation** for wrong answers. A **congratulatory message** is shown at the end.

---

## **Frontend Code (HTML, CSS, JavaScript)**
**HTML** is used to structure the web pages, including forms, buttons, and question containers.  
**CSS** is used to design an **attractive and responsive UI**, including layouts, colors, animations, and progress bars.  
**JavaScript** handles the **core quiz logic**, such as dynamic question loading, timer control, validation, score calculation, warning messages, and result generation.

---

## **Backend (PHP)**
**PHP** is used as the backend to handle **page navigation** and **user selections**. It processes the selected category and difficulty level using **URL parameters** and dynamically loads the quiz page. The backend is kept lightweight and does not use a database, ensuring simplicity and smooth integration with JavaScript.

---

## **Features Implemented**
1. **Category and difficulty selection** to customize the quiz experience.  
2. **Dynamic question loading** using JavaScript arrays.  
3. **Timer-based questions** with automatic navigation on timeout.  
4. **Negative case handling** with warning message when no option is selected.  
5. **Automatic question navigation** after answer selection or timer expiry.  
6. **Dynamic score calculation** based on correct answers.  
7. **Progress bar visualization** showing performance percentage.  
8. **Detailed result analysis** with explanations for wrong answers.  
9. **Responsive UI design** for desktop, tablet, and mobile devices.  
10. **Selenium automation testing** covering positive and negative scenarios.

---

## **Automation Strategy**
Automation testing is implemented using **Selenium WebDriver with Python**. The automation script verifies the **landing page**, **quiz start**, **first question load**, **negative case validation**, **random answer selection**, and **result verification**. Screenshots are captured at critical stages to provide **visual proof of execution**.

---

## **Test Cases Summary**
The application is tested using multiple test cases, including **landing page verification**, **quiz start and first question display**, **negative scenario handling**, **positive flow of answering questions**, and **result and score verification**. These test cases ensure the application behaves correctly for both valid and invalid user actions.

---

## **Deployment**
The project is deployed on **PHP-supported hosting platforms** such as **InfinityFree** or **Render (using Docker)**. Render uses a **Dockerfile** to run **Apache with PHP**, enabling server-side PHP execution. **GitHub** is used for version control and deployment integration.

---

## **Technologies Used**
- **HTML, CSS, JavaScript**  
- **PHP**  
- **Python & Selenium WebDriver**  
- **XAMPP (Local Server)**  
- **Git & GitHub**  
- **Render (Deployment)**  

---

## **Final Result**
The final result is a **fully functional Dynamic Quiz Application** with category-based questions, timer functionality, detailed result analysis, and automation testing support. The project successfully demonstrates **frontend development**, **PHP backend integration**, and **automated testing**, making it suitable for **academic submission and practical learning**.



---
