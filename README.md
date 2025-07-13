# Jenkins Test Project 🚀

This project is created to **test the integration between GitHub and Jenkins** using a simple Python script.

---

## 📌 What is Jenkins?

[Jenkins](https://www.jenkins.io/) is an open-source automation server used for **Continuous Integration (CI)** and **Continuous Delivery (CD)**. It automates repetitive tasks involved in building, testing, and deploying software.

With Jenkins, you can:
- Fetch code from GitHub or other repositories
- Automatically build and test your project
- Deploy your application to servers or cloud
- Monitor every stage of the development lifecycle

---

## 🔗 Jenkins + GitHub Integration

This project demonstrates how Jenkins can:

1. Connect to a GitHub repository  
2. Clone the source code  
3. Run a build job (in this case, a Python script)

---

## 🗂 Project Structure

jenkins-test-project/
├── hello_jenkins.py   # Python script executed by Jenkins
└── README.md          # Project documentation

---

## 🐍 About `hello_jenkins.py`

This is a simple Python script that:

- Prints a welcome message  
- Verifies that Jenkins successfully pulled the code from GitHub  
- Confirms successful script execution in the Jenkins console  

---

## ▶️ How to Use This Project

1. **Clone or fork** this repository: https://github.com/Jasleen-8904/jenkins-test-project

2. **In Jenkins**:
- Create a new **Freestyle Project**
- In **Source Code Management**, select **Git** and paste the repo URL
- In the **Build** section, add a step:
  ```bash
  python hello_jenkins.py
  ```

3. **Click “Build Now”**

4. Check the **Console Output** for successful execution

---

## 💡 Why This is Useful

This mini-project helps you:

- Confirm Jenkins is correctly pulling code from GitHub  
- Validate that Jenkins is executing scripts as expected  
- Serve as a base for future CI/CD pipelines and automation workflows

---

## 👤 Author

**Jasleen Kaur**  
GitHub: [@Jasleen-8904](https://github.com/Jasleen-8904)

---

## 🛠️ License

This project is open-source and free to use for learning and testing purposes.
