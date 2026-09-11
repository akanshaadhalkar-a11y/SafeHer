# 🛡️ SafeHer - Women Safety Web Application

> A Django-based women safety web application designed to provide quick emergency assistance through SOS alerts, emergency contacts, and location sharing.

---

## 📌 About the Project

**SafeHer** is a web-based women safety application developed using **Python and Django**.

The main purpose of this project is to provide a simple and accessible platform that can help a user quickly contact trusted emergency contacts during an unsafe or emergency situation.

The application allows users to register their emergency contacts and trigger an emergency alert. The alert can include the user's current location through a Google Maps location link, helping trusted contacts identify where assistance may be needed.

---

## 🎯 Problem Statement

Women may face unsafe situations while travelling, walking alone, or being in unfamiliar places. During an emergency, contacting multiple people and explaining the exact location can take valuable time.

SafeHer aims to simplify this process by providing:

* 🚨 Quick emergency alert functionality
* 📍 Location sharing
* 👥 Emergency contact management
* 📧 Email-based emergency notifications
* 📝 Emergency alert history
* 🔐 User authentication
* 🌐 Simple and user-friendly interface

---

## ✨ Key Features

### 🚨 Emergency SOS Alert

The user can trigger an emergency alert when immediate assistance is required.

The system sends an emergency notification to the user's registered emergency contacts.

### 📍 Live Location Sharing

The application generates a location link that can be shared with emergency contacts.

The location link can be opened using Google Maps to help contacts identify the user's location.

### 👥 Emergency Contacts

Users can register trusted people as emergency contacts.

The application stores the required contact information so that alerts can be sent quickly during an emergency.

### 📧 Email Emergency Notification

SafeHer uses email functionality to send emergency alerts to registered contacts.

The notification can contain important information such as:

* 🚨 Emergency message
* 📍 User location
* 🗺️ Google Maps location link

### 🔐 User Authentication

The application provides user authentication functionality so that users can securely access their account and manage their safety information.

### 📝 Emergency History

Users can view their previous emergency alert activity and maintain a history of alerts generated through the application.

### ℹ️ About / Information Section

The application also provides information about the purpose of SafeHer and how the system can help users during emergency situations.

---

## 🛠️ Technology Stack

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| 🐍 Python       | Backend programming       |
| 🌐 Django       | Web application framework |
| 🗄️ SQLite      | Database                  |
| 🎨 HTML5        | Web page structure        |
| 🎨 CSS3         | User interface styling    |
| ⚡ JavaScript    | Client-side functionality |
| 📧 SMTP / Email | Emergency email alerts    |
| 🗺️ Google Maps | Location sharing          |
| 🔧 Git          | Version control           |
| 🐙 GitHub       | Source code management    |

---

## 🏗️ Project Architecture

```text
SafeHer
│
├── manage.py
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── safeher_project/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── .gitignore
│
└── README.md
```

> **Note:** The exact folder structure may vary depending on the latest version of the project.

---

## 🔄 Application Workflow

```text
             ┌──────────────────┐
             │      User        │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Register / Login │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Add Emergency    │
             │    Contacts      │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │   SafeHer Home   │
             └────────┬─────────┘
                      │
                 Emergency?
                   /     \
                 No       Yes
                 │         │
                 │         ▼
                 │  ┌────────────────┐
                 │  │ Trigger SOS    │
                 │  └───────┬────────┘
                 │          │
                 │          ▼
                 │  ┌────────────────┐
                 │  │ Get Location   │
                 │  └───────┬────────┘
                 │          │
                 │          ▼
                 │  ┌────────────────┐
                 │  │ Generate Maps  │
                 │  │ Location Link  │
                 │  └───────┬────────┘
                 │          │
                 │          ▼
                 │  ┌────────────────┐
                 │  │ Send Emergency │
                 │  │ Email Alert    │
                 │  └───────┬────────┘
                 │          │
                 │          ▼
                 │  ┌────────────────┐
                 │  │ Save Alert     │
                 │  │ History        │
                 │  └────────────────┘
                 │
                 ▼
             Normal Usage
```

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/akanshaadhalkar-a11y/SafeHer.git
```

### 2. Navigate to the Project

```bash
cd SafeHer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not included in the repository, install Django manually:

```bash
pip install django
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Open the Application

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

## 📧 Email Configuration

The emergency alert functionality requires email configuration.

For security reasons, sensitive credentials such as:

* Email password
* SMTP credentials
* Secret keys
* API keys

should **not** be uploaded to GitHub.

Use environment variables or a local configuration file for sensitive information.

Example:

```text
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_app_password
```

Add sensitive configuration files to `.gitignore`.

---

## 🖥️ Main Modules

### 1. Authentication Module

Responsible for:

* User registration
* User login
* User logout
* User authentication

### 2. Emergency Contact Module

Responsible for:

* Adding emergency contacts
* Managing trusted contacts
* Using registered contacts for emergency alerts

### 3. SOS Module

Responsible for:

* Triggering emergency alerts
* Preparing emergency messages
* Sending alerts to registered contacts

### 4. Location Module

Responsible for:

* Obtaining the user's location
* Creating a location link
* Sharing the location through the emergency alert

### 5. History Module

Responsible for:

* Recording emergency events
* Displaying previous emergency activity

---

## 🔒 Security Considerations

SafeHer handles information that may be sensitive, especially emergency contact and location information.

The project follows basic security practices such as:

* 🔐 Django authentication
* 🔑 Protected credentials
* 🚫 Sensitive files excluded using `.gitignore`
* 🛡️ Django's built-in security mechanisms
* 📧 Secure email configuration
* 🔒 Avoiding hard-coded passwords and secrets

> **Important:** SafeHer is an educational/project implementation and should not be considered a replacement for official emergency services.

---

## 📱 Example Use Case

### Scenario

A user is travelling alone and suddenly feels unsafe.

### Steps

1. The user opens SafeHer.
2. The user activates the emergency SOS function.
3. SafeHer prepares an emergency alert.
4. The user's location is converted into a map link.
5. The emergency notification is sent to registered contacts.
6. Trusted contacts can open the location link and take appropriate action.
7. The event can be recorded in the user's emergency history.

---

## 🚀 Future Scope

The project can be further improved by adding:

* 📍 Real-time location tracking
* 📱 Progressive Web App (PWA) support
* 📞 Direct emergency calling
* 💬 SMS emergency alerts
* 🤖 AI-based danger detection
* 🎙️ Voice-triggered SOS
* 📳 Shake detection
* 🗺️ Safety heat maps
* 🏥 Nearby police stations and hospitals
* 👮 Emergency service integration
* 📊 Safety analytics dashboard
* 🔔 Push notifications
* 📱 Dedicated Android application

---

## 📸 Screenshots

Add screenshots of the application here.

Recommended screenshots:

1. 🏠 Home / Dashboard
2. 🔐 Login Page
3. 📝 Registration Page
4. 👥 Emergency Contact Page
5. 🚨 SOS / Emergency Page
6. 📍 Location Sharing
7. 📋 Emergency History
8. ℹ️ About Page

Example:

```

### 🏠 Home Page

[Home Page]<img width="1763" height="844" alt="image" src="Screenshot_11-9-2026_211627_127.0.0.1" />


### 🔐 Login Page



### 🚨 Emergency Alert



### 📍 Location Sharing


```

---

## 🧪 Testing

The application should be tested for:

* User registration
* User login/logout
* Emergency contact creation
* SOS functionality
* Email delivery
* Location generation
* Alert history
* Invalid user input
* Authentication restrictions
* Mobile responsiveness

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Python programming
* Django web development
* Django project structure
* Database integration
* User authentication
* HTML/CSS/JavaScript
* Form handling
* Email integration
* Location-based functionality
* Git and GitHub
* Debugging and problem solving
* Building a real-world problem-solving application

---

## 🌱 Project Impact

SafeHer demonstrates how web technologies can be used to address a real-world safety problem.

The project focuses on reducing the time required to communicate an emergency and share useful location information with trusted contacts.

---

## 👩‍💻 Developer

**Akansha Dnyanoba Adhalkar**

🎓 B.Tech Computer Science & Engineering

📍 Maharashtra, India

### GitHub

🔗 https://github.com/akanshaadhalkar-a11y

### Project Repository

🔗 https://github.com/akanshaadhalkar-a11y/SafeHer

---

## 📄 License

This project is created for educational and academic purposes.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

### 🛡️ SafeHer

**Technology for safety. Technology for faster help.**
