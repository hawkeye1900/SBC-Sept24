
# Installing Python and Dependencies

## Step 1: Downloading Python
- Visit [python.org](https://www.python.org).
- Choose the latest version suitable for your OS (Windows, macOS, Linux).
- Run the installer (Ensure to check "Add Python to PATH" on Windows).

## Step 2: Installing Python
- Run the installer and follow the setup process.
- Verify the installation:
  ```bash
  python --version
  ```

## Step 3: Installing pip (Package Manager)
- pip comes pre-installed with Python 3.4+.
- Verify pip installation:
  ```bash
  pip --version
  ```
- Use pip to install libraries:
  ```bash
  pip install <package-name>
  ```

## Step 4: Setting Up Virtual Environments
- Create a virtual environment:
  ```bash
  python -m venv myenv
  ```
- Activate the environment:
  - Windows: `myenv\Scripts\activate`
  - macOS/Linux: `source myenv/bin/activate`
- Deactivate:
  ```bash
  deactivate
  ```

## Step 5: Managing Dependencies
- Create `requirements.txt` file:
  ```bash
  pip freeze > requirements.txt
  ```
- Install dependencies from `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```

## Step 6: Choosing a Python IDE
- Popular IDEs:
  - VS Code
  - PyCharm
  - Sublime Text
- Features: Syntax highlighting, debugging, integrated terminal

## Step 7: Running Your First Python Script
- Create a new Python file `hello.py`:
  ```python
  print("Hello, World!")
  ```
- Run the script:
  ```bash
  python hello.py
  ```

## Troubleshooting
- **Python not recognized?** Add it to PATH.
- **pip not working?** Reinstall with `get-pip.py`. -> use this command : `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` -> Once you've downloaded get-pip.py, you can install pip by running the following command in the terminal: `python get-pip.py` -> After running the script, verify that pip was installed correctly : `pip --version`


# Creating an Account on PythonAnywhere and Adding Me as Your Teacher

## Step 1: Signing Up
- Visit [PythonAnywhere](https://www.pythonanywhere.com/).
- Click **Create a Free Account**.
- Fill in your username, email, and password.
- Click **Register**.

## Step 2: Verifying Your Email
- Check your email for a verification link from PythonAnywhere.
- Click on the link to verify your account.

## Step 3: Accessing Your Dashboard
- Once verified, log in to your PythonAnywhere account.
- You will be redirected to the **Dashboard** where you can manage your Python environment.

## Step 4: Adding Me as a Teacher
- On the top-right corner of your Dashboard, click **Account**.
- Under the **Teacher** section, click **Enter your teacher's name**.
- Enter the teacher's username: **SaiNikhith**.
- Click **Submit** to add the teacher.

## Step 5: Start Using PythonAnywhere
- Explore the platform to create new files, run Python scripts, and manage your projects.