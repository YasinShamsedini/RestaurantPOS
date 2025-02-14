# Restaurant POS System 🍽️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-2017+-red)](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)

## Overview 📝

The Restaurant POS System is a Python-based application designed to streamline restaurant operations, focusing on ease of use and intuitive design. This project, developed collaboratively with AI assistance over approximately 25 hours, leverages Tkinter/CustomTkinter for a user-friendly GUI and SQL Server for persistent data storage. The primary goal was to create a system that is both accessible and easy to learn, minimizing any potential friction for users.

## Key Features ✨

*   **Ordering:** ✍️ Create, modify, and track customer orders with efficient selection of customer, waiter, and table details. Automatic calculation of order totals, including modifiers.
*   **Table Management:** 🪑 Manage table availability, status (Available, Occupied, Reserved), and capacity.
*   **Menu Management:** 🍔 Easily add, edit, and remove menu items (food and drinks) with descriptions and pricing. Image upload and viewing capabilities are integrated.
*   **Modifier Support:** 🌶️ Add modifiers to menu items (e.g., "Extra Cheese," "No Onions") with associated pricing.
*   **Discount Application:** 💰 Predefined discount rules can be applied to orders or individual items.
*   **Customer Management:** 🧑‍🤝‍🧑 Maintain customer information (name, phone number, email) and track party sizes.
*   **Waiter Management:** 🤵 Manage waiter information and track active status.
*   **Reporting:** 📊 Transfer order details to a report page for comprehensive tracking and analysis.
*   **CRUD Functionality:** ⚙️ Complete Create, Read, Update, and Delete (CRUD) operations for all managed entities (tables, menu items, discounts, users, etc.).
*   **Order Item Management**: 🗑️ Automatic removal of orders or single items, with capability to transfer or remove from customer order list.

<br><br>

![Alt Text](https://github.com/YasinShamsedini/RestaurantPOS/blob/main/images/orderingpos.JPG)
<br><br>
![Alt Text](https://github.com/YasinShamsedini/RestaurantPOS/blob/main/images/reportpos.JPG)
<br><br>
![Alt Text](https://github.com/YasinShamsedini/RestaurantPOS/blob/main/images/managementpos.JPG)
<br><br>

## Technologies Used 💻

*   **Python:** Programming language for the application logic.
*   **Tkinter/CustomTkinter:** GUI framework for creating the user interface.
*   **SQL Server:** Relational database management system for storing application data.
*   **pyodbc:** Python library for connecting to SQL Server databases.
*   **Pillow (PIL):** Python Imaging Library for handling images in the GUI.

## Installation ⚙️

1.  **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd [repository_directory]
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the database:**
    *   Ensure you have SQL Server installed and running.
    *   Create a database named `RestaurantPOS`.
    *   Update the database connection string in the `Database` class (or a configuration file) with your SQL Server credentials.
    *   Run the SQL script (`database_setup.sql`) to create the tables and insert sample data.  You can use SQL Server Management Studio (SSMS) or another SQL client.

5.  **Run the application:**

    ```bash
    python main.py  # Or python restaurant_pos.py, depending on your entry point
    ```

## Database Setup 🗄️

A SQL script (`database_setup.sql`) is provided to create the necessary tables and insert sample data into the `RestaurantPOS` database. Follow these steps to set up the database:

1.  Open SQL Server Management Studio (SSMS) or another SQL client.
2.  Connect to your SQL Server instance.
3.  Create a new database named `RestaurantPOS`.
4.  Open the `database_setup.sql` file.
5.  Execute the script to create the tables and insert sample data.

## Usage 🚀

1.  **Launch the application:** Run `python main.py` (or the appropriate entry point).
2.  **Navigate the interface:** Use the menu on the left to switch between Ordering and Management modes.
3.  **Ordering:**
    *   Select a customer, waiter, and table.
    *   Choose food and drink items from the dropdown menus.
    *   Add modifiers and notes as needed.
    *   Click "Add to Order" to add items to the order.
    *   Review the order in the table on the right.
    *   Click "Place Order" to submit the order.
4.  **Management:**
    *   Use the Management menu to manage tables, menu items, discounts, and user accounts.
    *   Generate reports on sales data.

## Future Enhancements 🛠️

*   **Inventory Management:** Integrate inventory management to automatically update stock counts as orders are placed. This would help track ingredient levels and prevent stockouts.
*   **Advanced Discounting:** Implement more sophisticated discounting rules, such as percentage-based discounts, time-based discounts (e.g., happy hour), and discounts based on customer loyalty.
*   **Payment Gateway Integration:** Integrate with payment gateways (e.g., Stripe, PayPal) to enable online ordering and payment processing.
*   **Online Ordering:** Allow customers to place orders online through a web interface or mobile app.
*   **Kitchen Display System (KDS):** Implement a KDS to display orders in the kitchen, improving communication and efficiency.

## Contributing 🤝

We welcome contributions to this project! If you'd like to contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Write tests to ensure your changes are working correctly.
5.  Submit a pull request.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

*   Special thanks to the [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) team for providing a modern and customizable Tkinter framework.
*   Thanks to the open-source community for providing valuable resources and libraries.

## Contact 📧

If you have any questions or feedback, please feel free to contact me at [Email](yasin.shamsedini@gmail.com).
