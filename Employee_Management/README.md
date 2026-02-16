# 📌 Employee Management System

A Django-based Employee Management System that allows adding, updating, deleting, and viewing employee records in a structured format.

# 📜 Features

* ✅ Employee Registration – Add new employees with name, email, and password.
* ✅ Update Employee Details – Modify existing employee information.
* ✅ Delete Employee – Remove employee records when necessary.
* ✅ View Employee List – Display all employee records in a tabular format.
* ✅ User Authentication – Secure login and logout functionality.
* ✅ Modern UI – Built using Bootstrap for responsiveness and user-friendly experience.

# 🛠️ Tech Stack
- **Backend: Django (Python) 🐍**
- **Frontend: HTML, CSS, Bootstrap 🎨**
- **Database: SQLite (default) or PostgreSQL**
- **Version Control: Git & GitHub**

# 📂 Project Structure
```
Employee_Management/
│── app1/                  
│   ├── migrations/     
│   ├── static/            
│   ├── templates/          
│   │   ├── app1/           
│   │   │   ├── base.html  
│   │   │   ├── index.html  
│   │   │   ├── update.html 
│   │   │   ├── about.html  
│   │   │   ├── services.html  
│   ├── models.py          
│   ├── views.py           
│   ├── forms.py           
│   ├── urls.py            
│── Employee_Management/   
│   ├── settings.py        
│   ├── urls.py            
│── manage.py              
│── README.md              
│── requirements.txt       
```
# 🚀 Installation & Setup

### 🔹 Clone the Repository
```bash
git clone https://github.com/your-username/Employee_Management_System.git
cd Employee_Management_System
```
### 🔹 Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```
### 🔹 Install Dependencies

    pip install -r requirements.txt

### 🔹 Run Migrations

    python manage.py makemigrations
    python manage.py migrate

### 🔹 Create Superuser (Optional)

    python manage.py createsuperuser

### 🔹 Run the Server

    python manage.py runserver

Now, open http://127.0.0.1:8000/ in your browser. 🎉

### 📌 Screenshots

### 🏠 Home Page

### 📝 Employee List

### ➕ Add Employee

# 🎯 Usage
* Visit the homepage to view the list of employees.
* Use the form to register a new employee.
* Click on the Edit icon ✏️ to update employee details.
* Click on the Delete icon ❌ to remove an employee.
* Navigate to the About & Services pages for additional details.

# 📜 License

This project is open-source and available under the MIT License.

## 📬 Contact
- **Developer:** Abdullah Nazmus-Sakib
- **GitHub:** [AbdullahRFA](https://github.com/AbdullahRFA)
- **Portfolio:** [abdullah-nazmus-sakib-rfa.netlify.app](https://abdullah-nazmus-sakib-rfa.netlify.app/)
- **Email:** [shakibrybmn@gmail.com)](mailto:shakibrybmn@gmail.com)

### Developed with ❤️ using Django.
