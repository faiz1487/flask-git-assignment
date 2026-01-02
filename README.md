# Flask Git Assignment Report

**Student Name:** Faizan Kaishar  
**Project:** Flask Git & Branching Assignment  
**Repository Name:** flask-git-assignment  
**GitHub Repository Link:**  https://github.com/faiz1487/flask-git-assignment.git 

---

## Objective
The objective of this assignment is to demonstrate hands-on understanding of Git and GitHub workflows including:
- Repository creation
- Branching strategy
- Merging and conflict resolution
- Git reset and rebasing
- Frontend and backend feature integration using Flask and MongoDB

---

## Project Structure
```
flask-git-assignment/
│── app.py
│── data.json
│── requirements.txt
│── templates/
│   ├── form.html
│   └── success.html
```

---

## Part 1: Repository Setup & Initial Merge

### Steps Performed
1. Created a new GitHub repository named `flask-git-assignment`.
2. Generated SSH key and added it to GitHub for secure authentication.
3. Cloned the repository using SSH.
4. Created a branch named `faizan-kaishar`.
5. Added Flask project files to the branch.
6. Committed the changes and merged them into the `main` branch.

### Commands Used
```bash
git clone git@github.com:faizan-kaishar/flask-git-assignment.git
cd flask-git-assignment
git checkout -b faizan-kaishar
git add .
git commit -m "Added initial Flask project"
git checkout main
git merge faizan-kaishar
git push origin main
```

---

## Part 2: JSON Update Branch

### Steps Performed
1. Created a new branch `faizan-kaishar_new`.
2. Updated the `data.json` file used in the `/api` route.
3. Committed the changes.
4. Merged the branch into the `main` branch.

### Commands Used
```bash
git checkout -b faizan-kaishar_new
nano data.json
git add data.json
git commit -m "Updated API JSON data"
git checkout main
git merge faizan-kaishar_new
git push origin main
```

---

## Part 3: Feature Development Using Multiple Branches

### Branch Creation
```bash
git checkout -b master_1
git checkout main
git checkout -b master_2
```

### master_1: Frontend To-Do Page
- Created a To-Do form with fields:
  - Item Name
  - Item Description

```bash
git add templates/form.html
git commit -m "Added To-Do frontend form"
```

### master_2: Backend API
- Created a backend route `/submittodoitem`.
- Accepted POST data and stored it in MongoDB.

```bash
git add app.py
git commit -m "Added /submittodoitem API"
```

### Merging to Main Branch
```bash
git checkout main
git merge master_1
git merge master_2
git push origin main
```

---

## Part 4: Enhancing To-Do Form and Advanced Git Operations

### Sequential Commits in master_1
1. **Added Item ID field**
2. **Added Item UUID field**
3. **Added Item Hash field**

```bash
git commit -m "Added Item ID field"
git commit -m "Added Item UUID field"
git commit -m "Added Item Hash field"
```

### Merge to Main
```bash
git checkout main
git merge master_1
```

### Git Reset (Soft Reset)
- Rolled back to the commit where only Item ID field existed.
- Used soft reset to keep changes staged.

```bash
git reset --soft <commit-hash>
git commit -m "Reverted to Item ID only"
```

### Git Rebase
- Rebased changes from `main` back into `master_1`.
- Preserved individual commits.

```bash
git checkout master_1
git rebase main
```

---

## Conclusion
This assignment provided hands-on experience with real-world Git workflows including branching strategies, merge conflict handling, reset, and rebasing. It also demonstrated full-stack development using Flask for backend APIs, HTML for frontend forms, and MongoDB for data storage.

---

**Submission Includes:**
- GitHub repository link
- Screenshots of commands and outputs
- This detailed report

