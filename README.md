
# Assignment Report
## Flask API and MongoDB Atlas Integration

**Student Name:** Faizan Kaishar  
**Assignment Title:** Flask Application with API and MongoDB Integration  
**Technology Used:** Python, Flask, MongoDB Atlas, HTML  
**IDE:** Visual Studio Code  
**Operating System:** Windows

---

## 1. Introduction
This assignment demonstrates the development of a Flask-based web application integrated with MongoDB Atlas. The application exposes an API endpoint to return JSON data from a backend file and provides a frontend form to collect user input and store it in MongoDB.

---

## 2. Objective
- Create a Flask application with an `/api` route
- Read data from a backend JSON file
- Return the data as a JSON response
- Build a frontend form for user input
- Insert form data into MongoDB Atlas
- Display a success message on successful submission
- Show error messages on the same page if submission fails

---

## 3. Project Structure
```
flask_assignment/
│
├── app.py
├── data.json
├── requirements.txt
│
├── templates/
│   ├── form.html
│   └── success.html
```

---

## 4. Tools and Technologies Used
- **Python** – Backend programming language
- **Flask** – Web framework
- **MongoDB Atlas** – Cloud-based NoSQL database
- **PyMongo** – MongoDB driver for Python
- **HTML** – Frontend development
- **VS Code** – Development environment

---

## 5. Backend Data File
### data.json
The backend file stores data in JSON format. This data is read by the Flask API and returned as a JSON response.

Example content:
```json
[
  {"id": 1, "name": "Faizan"},
  {"id": 2, "name": "Developer"}
]
```

---

## 6. Flask Application Overview
The Flask application handles:
- MongoDB Atlas connection using PyMongo
- API route to return JSON data
- Rendering of HTML templates
- Form submission and data insertion
- Error handling during database operations

---

## 7. API Route Description
### `/api`
- Reads data from `data.json`
- Converts data to JSON format
- Sends JSON response to the client

---

## 8. Frontend Form Functionality
The form allows users to:
- Enter name and email
- Submit data via POST request
- View error messages if insertion fails
- Get redirected to a success page on successful submission

---

## 9. Success Page
On successful data insertion, the user is redirected to a page displaying:

**"Data submitted successfully"**

---

## 10. MongoDB Atlas Integration
- Database Name: `assignment_db`
- Collection Name: `users`
- Data inserted using `insert_one()` method

---

## 11. Dependency Management
Dependencies are listed in `requirements.txt`:
```
flask
pymongo
```
Installed using:
```bash
pip install -r requirements.txt
```

---

## 12. Execution Steps
1. Open the project folder in VS Code
2. Install required dependencies
3. Run the application using:
   ```bash
   python app.py
   ```
4. Access the application in the browser:
   - API Route: `http://127.0.0.1:5000/api`
   - Form Page: `http://127.0.0.1:5000/`

---

## 13. Error Handling
- Database insertion errors are handled using try-except blocks
- Error messages are displayed on the same page
- No redirection occurs when an error is encountered

---

## 14. Output Screenshots
(Screenshots to be attached)
- Program execution in VS Code terminal
- API JSON output
- Form submission page
- Success message page
- MongoDB Atlas data view

---

## 15. Conclusion
This project successfully implements a Flask application with file-based data handling and MongoDB Atlas integration. It demonstrates API creation, frontend-backend interaction, database insertion, and effective error handling.

---

**End of Report**

