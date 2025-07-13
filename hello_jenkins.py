"""
hello_jenkins.py
-----------------

This script is a test file to verify Jenkins is correctly set up and connected with GitHub.

What is Jenkins?
----------------
Jenkins is an open-source automation server widely used for continuous integration (CI) and continuous delivery (CD).
It allows developers to automate tasks like:
- Fetching code from repositories
- Running builds
- Performing tests
- Deploying applications

How Jenkins Works with GitHub:
------------------------------
1. Jenkins is configured to monitor a GitHub repository.
2. Whenever a build is triggered manually or by a GitHub webhook:
    - Jenkins clones the repository
    - Executes the configured script or job
3. This integration helps automate software development workflows and reduce manual work.

This script is designed to print a simple message to verify:
- The GitHub repository was successfully cloned by Jenkins
- The script ran successfully inside the Jenkins job

"""

def main():
    print("✅ Jenkins is successfully connected to GitHub!")
    print("🚀 This script was cloned from GitHub and executed by Jenkins.")
    print("📁 Repo: https://github.com/Jasleen-8904/jenkins-test-project")
    print("🎉 Hello from Jenkins + GitHub 🎉")


if __name__ == "__main__":
    main()
