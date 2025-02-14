# Restaurant POS System - Setup

Follow the steps below to set up and run the Restaurant POS System on your local machine.

<br><br><br>
## 1. Clone the Repository

Clone the repository using the command below:

```bash
git clone [repository_url]
cd [repository_directory]
```

> Replace `[repository_url]` and `[repository_directory]` with the actual values for your project.

## 2. Set Up a Virtual Environment (Recommended)

### For Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

This will create and activate a virtual environment for the project, ensuring that dependencies are managed separately.

## 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This command will install all necessary Python packages listed in the `requirements.txt` file.

## 4. Database Configuration

### Create the Database
Using SQL Server Management Studio (SSMS) or your preferred SQL client, run the following command to create the database:

```sql
CREATE DATABASE RestaurantPOS;
```

### Update Connection String
Open the `database.py` or `config.py` file and update the connection string with your database details:

```python
connection_string = (
    r'DRIVER={ODBC Driver 18 for SQL Server};'
    r'SERVER=your_server_name;'
    r'DATABASE=RestaurantPOS;'
    r'UID=your_username;'
    r'PWD=your_password;'
    r'TrustServerCertificate=yes;'
)
```

> **Note:** Replace `your_server_name`, `your_username`, and `your_password` with the appropriate values for your SQL Server.

### Execute SQL Script
Run the `database_setup.sql` script in SSMS or your SQL client to set up the necessary tables and schema for the POS system.

## 5. Run the Application

Finally, run the application using the following command:

```bash
python main.py  # Or python restaurant_pos.py
```

This will start the POS system, and you should be able to access it locally.

---

### Additional Notes:
- **Virtual Environment**: It’s recommended to use a virtual environment to avoid conflicts with system packages.
- **Database**: Make sure your SQL Server instance is running and accessible when setting up the connection.
- **Running the App**: Ensure all the dependencies are installed before running the application to avoid missing modules or errors.

---

This structure uses clear headers for each section, with detailed steps for setup, ensuring it's easy to follow. The syntax highlighting is set for code blocks (e.g., `bash` for shell commands and `python` for Python code) for better readability. 

Would you like to add any more specific sections or additional information?
