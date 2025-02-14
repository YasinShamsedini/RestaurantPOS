import tkinter as tk
from tkinter import ttk, messagebox, font
import tkinter.ttk as ttk
import customtkinter as ctk
import pyodbc
from decimal import Decimal
import json 
import datetime
from PIL import Image, ImageTk 





class Database:
    def __init__(self):
        self.conn = self.get_db_connection()
        if not self.conn:
            messagebox.showerror("Error", "Database connection failed!")

    def get_db_connection(self):
        try:
            connection_string = (
                r'DRIVER={ODBC Driver 18 for SQL Server};'
                r'SERVER=.\SQLEXPRESS;'
                r'DATABASE=RestaurantPOS;'
                r'TrustServerCertificate=yes;'
                r'Authentication=ActiveDirectoryIntegrated;'
            )
            conn = pyodbc.connect(connection_string)
            return conn
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Database connection error: {sqlstate}")
            messagebox.showerror("Error", f"Database connection error: {sqlstate}") # show DB error.
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            messagebox.showerror("Error", f"An unexpected error occurred: {e}") # show generic error.
            return None

    def fetch_table(self, table_id):
      """Fetches a single table from the database by its ID."""
      if self.conn:
          try:
              cursor = self.conn.cursor()
              cursor.execute("SELECT TableID, TableNumber, Capacity, Status FROM Tables WHERE TableID = ?", (table_id,))
              table = cursor.fetchone()
              return table # returns a tuple or None

          except pyodbc.Error as ex:
              sqlstate = ex.args[0]
              print(f"Database error: {sqlstate}")
              messagebox.showerror("Error", f"Database error: {sqlstate}") # Display error message
              return None
          finally:
              if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                  cursor.close()
      return None  # Returns None if no connection

    def update_table_status(self, table_id, new_status):
        """Updates the table status in the database."""
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("UPDATE Tables SET Status = ? WHERE TableID = ?", (new_status, table_id))
                self.conn.commit()
                return True  # Return True if update successful
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Database error: {sqlstate}")
                messagebox.showerror("Error", f"Database error: {sqlstate}")  # Display the error
                self.conn.rollback() # rollback uncommitted changes to prevent data corruption.
                return False  # Return False if update failed
            finally:
                if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                    cursor.close()
        return False

    def fetch_tables(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT TableID, TableNumber, Capacity, Status FROM Tables")
                return cursor.fetchall()
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Database error: {sqlstate}")
                messagebox.showerror("Error", f"Database error: {sqlstate}")  # Show error message
                return []  # Return empty list in case of error
            finally:
                if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                    cursor.close()
        return []

    def fetch_discounts(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT DiscountID, DiscountName, DiscountType, DiscountValue, ApplicableTo FROM Discounts")
                return cursor.fetchall()
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Database error: {sqlstate}")
                messagebox.showerror("Error", f"Database error: {sqlstate}")  # Show error message
                return []  # Return empty list in case of error
            finally:
                if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                    cursor.close()
        return []

    def fetch_drinks(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT DrinkID, Name, Description, Price FROM Drinks")
                return cursor.fetchall()  # Fetch all rows from Drinks table
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Database error: {sqlstate}")
                messagebox.showerror("Error", f"Database error: {sqlstate}")  # Show error message
                return []  # Return empty list in case of error
            finally:
                if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                    cursor.close()
        return []

    def fetch_food_items(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT FoodID, Name, Description, Price FROM MainFood")
                return cursor.fetchall()  # Fetch all rows from MainFood table
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Database error: {sqlstate}")
                messagebox.showerror("Error", f"Database error: {sqlstate}")  # Show error message
                return []  # Return empty list in case of error
            finally:
                if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                    cursor.close()
        return []

    def fetch_modifiers(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT ModifierID, Name, Description, Price FROM Modifiers")
                return cursor.fetchall()  # Fetch all rows from Modifiers table
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Database error: {sqlstate}")
                messagebox.showerror("Error", f"Database error: {sqlstate}")  # Show error message
                return []  # Return empty list in case of error
            finally:
                if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                    cursor.close()
        return []

    def fetch_waiters(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT WaiterID, FirstName, LastName, IsActive FROM Waiters")
                return cursor.fetchall()  # Fetch all rows from Waiters table
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Database error: {sqlstate}")
                messagebox.showerror("Error", f"Database error: {sqlstate}")
                return []  # Return empty list in case of error
            finally:
                if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                    cursor.close()
        return []


    def fetch_customers(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT CustomerID, Name, PhoneNumber, Email, PartySize FROM Customers")
                return cursor.fetchall()
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Database error: {sqlstate}")
                messagebox.showerror("Error", f"Database error: {sqlstate}")
                return []
            finally:
                if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                    cursor.close()
        return []

    def fetch_reports(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                # Query to fetch data from the Reports table
                cursor.execute("SELECT ReportID, TableNumber, OrderView, CustomerName, WaiterName, PartySize, TotalPrice, Status, ReportDate FROM Reports")
                return cursor.fetchall()  # Fetch all results as a list of tuples
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Database error: {sqlstate}")
                messagebox.showerror("Error", f"Database error: {sqlstate}")
                return []  # Return an empty list if there is an error
            finally:
                if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                    cursor.close()  # Make sure to close the cursor after use
        return []




    def execute_query(self, query, params=()):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(query, params)
                self.conn.commit()  # Commit changes (e.g., INSERT, UPDATE, DELETE)
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Database error: {sqlstate}")
                messagebox.showerror("Error", f"Database error: {sqlstate}")  # Show error message
            finally:
                if hasattr(locals(), 'cursor') and hasattr(cursor, 'close') and callable(cursor.close):
                    cursor.close()

    def close(self):
        if self.conn:
            self.conn.close()









class RestaurantPOS(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        self.title("Restaurant POS System")
        self.geometry("1300x640")

        # Configure the main grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # Left-side Menu Frame
        self.menu_frame = ctk.CTkFrame(self, width=250, corner_radius=0, fg_color="#34495e")
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        # Load and display image in the menu frame
        self.load_and_display_image(self.menu_frame, "D:/Users/BLACK-RAYANE/Downloads/Cartoon-female-chef-on-transparent-background-PNG.png")


        # Ordering Button
        self.ordering_button = ctk.CTkButton(self.menu_frame, text="ORDERING", command=self.show_ordering_frame,
                                           fg_color="#3498db", text_color="black", hover_color="#2980b9", corner_radius=8)
        self.ordering_button.pack(pady=15, padx=15)

        # Management Button
        self.management_button = ctk.CTkButton(self.menu_frame, text="MANAGEMENT", command=self.show_management_frame,
                                             fg_color="#3498db", text_color="black", hover_color="#2980b9", corner_radius=8)
        self.management_button.pack(pady=15, padx=15)

        # Right-side Content Frame
        self.content_frame = ctk.CTkFrame(self, fg_color="white")
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        self.active_frame = None
        self.show_ordering_frame()

    def load_and_display_image(self, frame, image_path):
        """Loads an image and displays it in the specified frame."""
        try:
            # Load the image using Pillow
            self.pil_image = Image.open(image_path)
            self.ctk_image = ctk.CTkImage(self.pil_image, size=(200, 180)) # Adjust size as needed - smaller for the menu

            # Create a label to hold the image
            self.image_label = ctk.CTkLabel(frame, image=self.ctk_image, text="") # Keep text="" to only show the image
            self.image_label.pack(pady=10, padx=10)  # Adjust padding as needed

        except FileNotFoundError:
            print(f"Error: Image file not found at {image_path}")
            error_label = ctk.CTkLabel(frame, text=f"Image not found: {image_path}")
            error_label.pack()
        except Exception as e:
            print(f"Error loading image: {e}")
            error_label = ctk.CTkLabel(frame, text=f"Error loading image: {e}")
            error_label.pack()


    def show_ordering_frame(self):
        self.clear_content_frame()
        # Assuming OrderingFrame is already defined to work with CTk
        self.ordering_frame = OrderingFrame(self.content_frame, self)
        self.ordering_frame.pack(fill="both", expand=True)
        self.active_frame = self.ordering_frame


    def show_management_frame(self):
        self.clear_content_frame()
        # Assuming ManagementFrame is already defined to work with CTk
        self.management_frame = ManagementFrame(self.content_frame, self)
        self.management_frame.pack(fill="both", expand=True)
        self.active_frame = self.management_frame


    def show_management_detail(self, frame_name):
        self.clear_content_frame()

        if frame_name == "WAITER MANAGMENT":
            frame = WaiterManagementFrame(self.content_frame, self)
        elif frame_name == "TABLE MANAGMENT":
            frame = TableManagementFrame(self.content_frame, self)
        elif frame_name == "DISCOUNT MANAGMENT":
            frame = DiscountManagementFrame(self.content_frame, self)
        elif frame_name == "DRINKS MANAGMENT":
            frame = DrinksManagementFrame(self.content_frame, self)
        elif frame_name == "MAIN FOOD MANAGMENT":
            frame = MainFoodManagementFrame(self.content_frame, self)
        elif frame_name == "MODIFIERS MANAGMENT":
            frame = ModifiersManagementFrame(self.content_frame, self)
        elif frame_name == "RECEPIES MANAGMENT":
            frame = RecipesManagementFrame(self.content_frame, self)
        elif frame_name == "REPORT":
            frame = ReportFrame(self.content_frame, self)
        elif frame_name == "USER MANAGEMENT": #Add the following lines
            frame = CustomerManagementFrame(self.content_frame, self) #Create customer frame here
        else:
            frame = ctk.CTkFrame(self.content_frame)
            ctk.CTkLabel(frame, text="Invalid Frame").pack()

        frame.pack(fill="both", expand=True)
        self.active_frame = frame


    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def clear_menu_frame(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        # Load and display the image again after clearing the menu frame
        self.load_and_display_image(self.menu_frame, "D:/Users/BLACK-RAYANE/Downloads/Cartoon-female-chef-on-transparent-background-PNG.png")






class OrderingFrame(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        # Assuming Database class is defined elsewhere
        self.db = Database()  # You will need to define this class
        # --- Data structures ---
        self.order_items = []
        self.selected_food = None
        self.selected_drink = None
        self.selected_modifier = None
        self.customer_id = None
        self.waiter_id = None
        self.table_id = None

        # --- Styles and Configuration ---
        self.dark_background = "#9c98f9"  # Define a consistent dark background color.  CHANGED HERE!
        self.dark_foreground = "black"  # CHANGED HERE: so the text can be more readable
        self.border_color = "white"  # Color for the border
        self.border_width = 2  # Width for the border

        self.style = ttk.Style()
        self.style.configure("Ordering.TFrame",
                             background=self.dark_background)  # CHANGED HERE:  Use self.dark_background
        self.configure(style="Ordering.TFrame")

        # Define label fonts
        self.title_font = ("Arial", 20)  # Larger font size for title
        self.label_font = ("Arial", 15)  # Font for standard Labels (Bordered)

        # Button Style
        self.style.configure("TButton", font=("Arial", 12),
                             background="#444444", foreground="black", padding=2)
        self.style.map("TButton",
                       background=[("active", "#555555"), ("pressed", "#333333")])  # Optional hover/press effects

        # Label Style
        self.style.configure("TLabel", font=("Arial", 14), foreground=self.dark_foreground,
                             background=self.dark_background, padding=3)  # Keep at 14 because these label are `ttk.Label`

        # Combobox Style
        self.style.configure("TCombobox", font=("Arial", 12), padding=5,
                             background='black', foreground='black')
        self.style.map("TCombobox",
                       background=[("active", "#555555"), ("focus", "'black")],
                       foreground=[("readonly", 'black')])

        # Treeview Style
        self.style.configure("Treeview", background="#4d4d4d",
                             foreground="white", fieldbackground="#333333")
        self.style.map("Treeview",
                       background=[('selected', '#0056b3')],
                       foreground=[('selected', 'white')])

        # Apply styles to headings (critical!)
        self.style.configure("Treeview.Heading", background="red",  # CHANGED HERE for readability
                             foreground="black", font=("Arial", 12))  # Changed for blue color.

        # --- GUI elements ---
        ttk.Label(self, text="Ordering Frame", font=self.title_font, background=self.dark_background).grid(
            row=0, column=0, columnspan=4, pady=30)  # Span 4 columns

        # Treeview and Calculation Frames moved to row 1, column 2
        self.order_tree_frame = ttk.Frame(
            self, style="Ordering.TFrame")  # Apply style for background
        self.order_tree_frame.grid(
            row=1, column=2, rowspan=10, sticky="nsew", padx=5, pady=5)

        self.order_tree = ttk.Treeview(self.order_tree_frame,
                                        columns=("Item", "Price", "Quantity",
                                                 "Modifiers", "Notes"),
                                        show="headings", style="Treeview")  # Apply the style here!
        self.order_tree.heading("Item", text="Item")
        self.order_tree.heading("Price", text="Price")
        self.order_tree.heading("Quantity", text="Quantity")
        self.order_tree.heading("Modifiers", text="Modifiers")
        self.order_tree.heading("Notes", text="Notes")

        self.order_tree.column("Item", width=120)
        self.order_tree.column("Price", width=80, anchor="center")
        self.order_tree.column("Quantity", width=70, anchor="center")
        self.order_tree.column("Modifiers", width=150)
        self.order_tree.column("Notes", width=300)

        self.order_tree.pack(fill="both", expand=True, pady=30)

        # --- Calculation Labels ---
        self.calculation_frame = ttk.Frame(
            self, style="Ordering.TFrame")  # Apply style for background
        self.calculation_frame.grid(
            row=11, column=2, sticky="ew", padx=5, pady=5)  # Adjusted row for placement below Treeview

        ttk.Label(self.calculation_frame, text="Subtotal:",
                  background=self.dark_background).grid(row=0, column=0, sticky="w")
        self.subtotal_label = ttk.Label(
            self.calculation_frame, text="0.00", background=self.dark_background)
        self.subtotal_label.grid(row=0, column=1, sticky="e")

        ttk.Label(self.calculation_frame, text="Total:",
                  background=self.dark_background).grid(row=1, column=0, sticky="w")
        self.total_label = ttk.Label(
            self.calculation_frame, text="0.00", background=self.dark_background)
        self.total_label.grid(row=1, column=1, sticky="e")

        # --- Menu Items section (left side) ---
        ttk.Label(self, text="Menu Items", font=("Arial", 14), background=self.dark_background).grid(
            row=1, column=0, sticky="w", padx=5)
        self.selection_frame = ttk.Frame(
            self, style="Ordering.TFrame")  # Apply style for background
        self.selection_frame.grid(
            row=2, column=0, columnspan=1, sticky="ew", padx=5, pady=5)

        ttk.Label(self.selection_frame, text="Customer:", font=("Arial", 14),
                  background=self.dark_background).grid(row=0, column=0, sticky="w")
        self.customer_combo = ttk.Combobox(
            self.selection_frame, values=self.get_customer_names(), state="readonly")
        self.customer_combo.grid(row=0, column=1, sticky="w", pady=5)
        self.customer_combo.bind("<<ComboboxSelected>>", self.customer_selected)
        self.customer_button = ttk.Button(
            self.selection_frame, text="Add/Edit Customer", command=self.open_customer_dialog)
        self.customer_button.grid(
            row=0, column=2, sticky="w", padx=10, columnspan=2)

        ttk.Label(self.selection_frame, text="Waiter:", font=("Arial", 14),
                  background=self.dark_background).grid(row=1, column=0, sticky="w", padx=15)
        self.waiter_combo = ttk.Combobox(
            self.selection_frame, values=self.get_waiter_names(), state="readonly")
        self.waiter_combo.grid(row=1, column=1, sticky="w", pady=5)
        self.waiter_combo.bind("<<ComboboxSelected>>", self.waiter_selected)

        ttk.Label(self.selection_frame, text="Table:", font=("Arial", 14),
                  background=self.dark_background).grid(row=2, column=0, sticky="w", padx=15)
        self.table_combo = ttk.Combobox(
            self.selection_frame, values=self.get_table_numbers(), state="readonly")
        self.table_combo.grid(row=2, column=1, sticky="w", pady=5)
        self.table_combo.bind("<<ComboboxSelected>>", self.table_selected)

        # --- Labels with borders ---
        self.food_label = tk.Label(self, text="Food", background=self.dark_background, foreground=self.dark_foreground,
                                   highlightbackground=self.border_color, highlightthickness=self.border_width, relief="solid", font=self.label_font)
        self.food_label.grid(row=3, column=0, sticky="w", padx=30, pady=30)
        self.food_combo = ttk.Combobox(
            self, values=self.get_food_names(), state="readonly")
        self.food_combo.grid(row=3, column=0, padx=1, pady=30)
        self.food_combo.bind("<<ComboboxSelected>>", self.food_selected)

        self.drink_label = tk.Label(self, text="Drinks", background=self.dark_background, foreground=self.dark_foreground,
                                    highlightbackground=self.border_color, highlightthickness=self.border_width, relief="solid", font=self.label_font)
        self.drink_label.grid(row=5, column=0, sticky="w", padx=25, pady=30)
        self.drink_combo = ttk.Combobox(
            self, values=self.get_drink_names(), state="readonly")
        self.drink_combo.grid(row=5, column=0, padx=1, pady=30)
        self.drink_combo.bind("<<ComboboxSelected>>", self.drink_selected)

        self.modifier_label = tk.Label(self, text="Modifiers", background=self.dark_background, foreground=self.dark_foreground,
                                       highlightbackground=self.border_color, highlightthickness=self.border_width, relief="solid", font=self.label_font)
        self.modifier_label.grid(row=7, column=0, sticky="w", padx=20, pady=30)
        self.modifier_combo = ttk.Combobox(
            self, values=self.get_modifier_names(), state="readonly")
        self.modifier_combo.grid(row=7, column=0, padx=5, pady=30)
        self.modifier_combo.bind("<<ComboboxSelected>>", self.modifier_selected)

        self.quantity_label = tk.Label(self, text="Quantity", background=self.dark_background, foreground=self.dark_foreground,
                                       highlightbackground=self.border_color, highlightthickness=self.border_width, relief="solid", font=self.label_font)
        self.quantity_label.grid(row=9, column=0, sticky="w", padx=20, pady=30)
        self.quantity_entry = ttk.Entry(self, width=16, font=('Arial, 13'))
        self.quantity_entry.grid(row=9, column=0, padx=10, pady=30)
        self.quantity_entry.insert(0, "1")

        self.notes_label = tk.Label(self, text="Notes", background=self.dark_background, foreground=self.dark_foreground,
                                    highlightbackground=self.border_color, highlightthickness=self.border_width, relief="solid", font=self.label_font)
        self.notes_label.grid(row=11, column=0, sticky="w", padx=30)
        self.notes_entry = ttk.Entry(self, width=20, font=('Arial', 13))
        self.notes_entry.grid(row=11, column=0, padx=50, pady=30)

        # Add to Order Button
        self.add_to_order_button = ttk.Button(
            self, text="Add to Order →", command=self.add_item_to_order, width=30)
        self.add_to_order_button.grid(
            row=14, column=0, pady=1, padx=15, sticky="ew")

        # Empty Column - this pushes the Treeview to the right
        self.grid_columnconfigure(
            1, weight=1)  # Allow the empty column to expand

        # --- Order Actions ---
        self.order_actions_frame = ttk.Frame(
            self, style="Ordering.TFrame")  # Apply style for background
        # Moved to row 10
        self.order_actions_frame.grid(
            row=14, column=2, columnspan=1, sticky="ew", padx=5, pady=1)

        self.remove_item_button = ttk.Button(
            self.order_actions_frame, text="Remove Item", command=self.remove_selected_item)
        self.remove_item_button.pack(side="left", padx=5)

        self.place_order_button = ttk.Button(
            self.order_actions_frame, text="Place Order", command=self.place_order)
        self.place_order_button.pack(side="right", padx=5)

        # Initial Data Loading
        self.load_initial_data()

    # --- Additional Methods ---

    def check_table_status(self):
        """Checks if the selected table's status is valid for placing an order.
           Modify this according to your database schema and status values.
        """
        if not self.table_id:
            messagebox.showerror("Error", "No table selected.")
            return False

        table = self.db.fetch_table(self.table_id)  # Assuming a method like this
        if not table:
            messagebox.showerror("Error", "Table not found in database.")
            return False

        table_status = table[2]  # Assuming table status is in the 3rd column.  Adjust as needed.

        # Example Status Checks:
        if table_status == "Occupied":
            messagebox.showerror("Error", "Table is already occupied.  Clear it first.")
            return False
        elif table_status == "Reserved":  # Possibly disallow reserved tables
            messagebox.showerror("Error", "Cannot place order for a reserved table.")
            return False
        #add additional conditional logic to disallow placing orders based on status
        return True  # Status is okay

    def update_table_status(self, new_status):
        """Updates the table status in the database.

        Args:
            new_status (str): The new status to set for the table.
        """
        if not self.table_id:
            messagebox.showerror("Error", "No table selected.")
            return False

        try:
            self.db.update_table_status(self.table_id, new_status)  # Assuming a db method like this
            messagebox.showinfo("Success", f"Table status updated to {new_status}.")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update table status: {e}")
            return False

    # --- Data Retrieval Methods ---

    def get_food_names(self):
        food_items = self.db.fetch_food_items()
        self.food_data = {item[1]: item for item in food_items}
        food_names = ["None"] + list(self.food_data.keys())
        return food_names

    def get_drink_names(self):
        drinks = self.db.fetch_drinks()
        self.drink_data = {item[1]: item for item in drinks}
        drink_names = ["None"] + list(self.drink_data.keys())
        return drink_names

    def get_modifier_names(self):
        modifiers = self.db.fetch_modifiers()
        self.modifier_data = {item[1]: item for item in modifiers}
        modifier_names = ["None"] + list(self.modifier_data.keys())
        return modifier_names

    def get_customer_names(self):
        customers = self.db.fetch_customers()
        self.customer_data = {item[1]: item for item in customers}
        return list(self.customer_data.keys())

    def get_waiter_names(self):
        waiters = self.db.fetch_waiters()
        self.waiter_data = {
            f"{item[1]} {item[2]}": item for item in waiters}
        return list(self.waiter_data.keys())

    def get_table_numbers(self):
        tables = self.db.fetch_tables()
        self.table_data = {item[1]: item for item in tables}
        return list(self.table_data.keys())

    # --- Event Handlers for Comboboxes ---

    def food_selected(self, event=None):
        selected_food_name = self.food_combo.get()
        if selected_food_name == "None":
            self.selected_food = None
        else:
            self.selected_food = self.food_data.get(selected_food_name)

    def drink_selected(self, event=None):
        selected_drink_name = self.drink_combo.get()
        if selected_drink_name == "None":
            self.selected_drink = None
        else:
            self.selected_drink = self.drink_data.get(selected_drink_name)

    def modifier_selected(self, event=None):
        selected_modifier_name = self.modifier_combo.get()
        if selected_modifier_name == "None":
            self.selected_modifier = None
        else:
            self.selected_modifier = self.modifier_data.get(selected_modifier_name)

    def customer_selected(self, event=None):
        selected_customer_name = self.customer_combo.get()
        if selected_customer_name:
            self.customer_id = self.customer_data[selected_customer_name][0]
        else:
            self.customer_id = None

    def waiter_selected(self, event=None):
        selected_waiter_name = self.waiter_combo.get()
        if selected_waiter_name:
            self.waiter_id = self.waiter_data[selected_waiter_name][0]
        else:
            self.waiter_id = None

    def table_selected(self, event=None):
        selected_table_number = self.table_combo.get()
        if selected_table_number:
            self.table_id = self.table_data[selected_table_number][0]
        else:
            self.table_id = None

    # --- Order Management ---

    def add_item_to_order(self):
        print("add_item_to_order called")

        if not self.customer_id or not self.table_id or not self.waiter_id:
            print("Customer, table, or waiter missing")
            messagebox.showerror(
                "Error", "Please select a Customer, Table, and Waiter.")
            return

        selected_food_name = self.food_combo.get()
        selected_drink_name = self.drink_combo.get()
        print(f"Food: {selected_food_name}, Drink: {selected_drink_name}")

        if (selected_food_name and selected_food_name != "None") and (selected_drink_name and selected_drink_name != "None"):
            messagebox.showerror(
                "Error", "Choose either a food OR a drink, not both.")
            return

        if not selected_food_name or selected_food_name == "None":
            if not selected_drink_name or selected_drink_name == "None":
                messagebox.showerror(
                    "Error", "Please select a food or drink item.")
                return

        item = None
        item_type = None

        if selected_food_name and selected_food_name != "None":
            item = self.food_data.get(selected_food_name)
            item_type = "Food"
        elif selected_drink_name and selected_drink_name != "None":
            item = self.drink_data.get(selected_drink_name)
            item_type = "Drink"

        try:
            quantity = int(self.quantity_entry.get())
            if quantity <= 0:
                messagebox.showerror("Error", "Quantity must be > zero.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity.")
            return

        notes = self.notes_entry.get()

        base_price = item[3]  # Base price of drink or food.
        modifier_price = 0  # initial state is 0

        # Calculate modifier prices.
        if self.selected_modifier and self.selected_modifier[1] != "None":
            modifier_price = self.selected_modifier[3]

        order_item = {
            "item_type": item_type,
            "item_id": item[0],
            "name": item[1],
            "price": base_price + modifier_price,  # Sum food and modifier
            "quantity": quantity,
            "notes": notes,
            "modifiers": []
        }

        if self.selected_modifier and self.selected_modifier[1] != "None":
            order_item["modifiers"].append(self.selected_modifier)

        print(f"Added item: {item}, Quantity: {quantity}, Notes: {notes}")
        self.order_items.append(order_item)
        self.update_order_display()

    def remove_selected_item(self):
        selected_item = self.order_tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Select an item to remove.")
            return

        item_index = self.order_tree.index(selected_item)
        del self.order_items[item_index]
        self.update_order_display()

    def calculate_subtotal(self):
        subtotal = Decimal("0.0")  # Initialize as Decimal
        for item in self.order_items:
            # ensure item["price"] is string then convert
            subtotal += Decimal(str(item["price"])) * item["quantity"]
        return float(subtotal)  # ensure float for GUI label

    def update_order_display(self):
        print("update_order_display called")
        for item in self.order_tree.get_children():
            self.order_tree.delete(item)

        for item in self.order_items:
            modifier_names = ", ".join(
                [mod[1] for mod in item["modifiers"] if mod[1] != "None"])
            self.order_tree.insert("", tk.END,
                                  values=(item["name"], item["price"], item["quantity"], modifier_names, item["notes"]))

        self.clear_add_item()

        subtotal = self.calculate_subtotal()

        total = subtotal  # max(0, subtotal - discount_amount) #Removed

        self.subtotal_label.config(text=f"{subtotal:.2f}")
        self.total_label.config(text=f"{total:.2f}")
        print(f"Subtotal: {subtotal}, Total: {total}")

    def clear_add_item(self):
        self.notes_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.quantity_entry.insert(0, "1")

        self.food_combo.set("")
        self.drink_combo.set("")
        self.modifier_combo.set("")
        self.selected_food = None
        self.selected_drink = None
        self.selected_modifier = None

    def place_order(self):
        """Places the order after checking and updating the table status."""

        # Step 1: Check the Table Status
        if not self.check_table_status():  # If status is not valid
            # The check_table_status function shows the message box. So, just return.
            return

        # Step 2: Update table status to occupied
        if self.update_table_status("Occupied"):
          pass
        else:
            messagebox.showerror("Error", "There was an error updating the table status.")
            return

        # Step 3: Collect report data (This part remains largely the same)
        table_number = self.table_combo.get()
        customer_name = self.customer_combo.get() or "Guest"  # Handle guest orders
        waiter_name = self.waiter_combo.get()
        # Added guest customer party size
        party_size = self.customer_data[customer_name][4] if customer_name != "Guest" and customer_name else 1
        total_price = self.calculate_subtotal()
        status = "Open"  # Set default status to "Open" here!

        # Build a String (Much easier to read and format and more human readable)
        order_view = ""
        for item in self.order_items:
            # Collect modifier names
            modifier_names = [mod[1] for mod in item["modifiers"]]
            modifier_str = ", ".join(
                modifier_names) if modifier_names else "None"
            order_view += f"{item['quantity']} x {item['name']} (Price: {item['price']:.2f}, Modifiers: {modifier_str}, Notes: {item['notes']})\n"

        # Pass report data to ReportFrame
        report_data = {
            "table_number": table_number,
            "order_view": order_view,
            "customer_name": customer_name,
            "waiter_name": waiter_name,
            "party_size": party_size,
            "total_price": total_price,
            "status": status
        }

        # Step 4: Switch to ReportFrame and populate data
        self.controller.show_management_detail("REPORT")

        # Access the ReportFrame instance and set values
        report_frame = self.controller.active_frame
        if isinstance(report_frame, ReportFrame):
            report_frame.populate_report_data(report_data)

        messagebox.showinfo("Order Placed", "Order placed successfully!")

        # Step 5: Clear order and UI
        self.order_items = []
        self.update_order_display()

    def open_customer_dialog(self):
        self.controller.show_management_detail("USER MANAGEMENT")

    def load_initial_data(self):
        self.get_food_names()
        self.get_drink_names()
        self.get_modifier_names()
        self.get_customer_names()
        self.get_waiter_names()
        self.get_table_numbers()
        self.update_combobox_values()

    def update_combobox_values(self):
        self.food_combo['values'] = self.get_food_names()
        self.drink_combo['values'] = self.get_drink_names()
        self.modifier_combo['values'] = self.get_modifier_names()
        self.customer_combo['values'] = self.get_customer_names()
        self.waiter_combo['values'] = self.get_waiter_names()
        self.table_combo['values'] = self.get_table_numbers()
        self.update_order_display() 










class ManagementFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Set the background color for the frame using ttk.Style
        #style = ttk.Style() # Remove reference to ttk style.
        #style.configure("Custom.TFrame", background="white")  # White background
        #self.configure(style="Custom.TFrame")  # Apply custom style to the frame
        self.configure(fg_color="white") #Instead, set frame color directly.

        # Add the label at the top
        self.label = ctk.CTkLabel(self, text="Management Frame ", font=("Arial", 20, "bold"), text_color="black")
        self.label.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew") 
        

        # Management Frame Buttons
        button_names = {
            "Waiter": "WAITER MANAGMENT",
            "Table": "TABLE MANAGMENT",
            "Discount": "DISCOUNT MANAGMENT",
            "Drinks": "DRINKS MANAGMENT",
            "Main Food": "MAIN FOOD MANAGMENT",
            "Modifiers": "MODIFIERS MANAGMENT",
            "Recipes": "RECEPIES MANAGMENT",
            "Report": "REPORT",
            "Customer": "USER MANAGEMENT"
        }

        # Calculate button layout (Single Column Layout)
        num_buttons = len(button_names)

        # Configure the grid layout to have a single column with adjustable row weights
        self.grid_columnconfigure(0, weight=1)

        # Ensure rows expand evenly and adjust with the frame size
        for row in range(num_buttons):
            self.grid_rowconfigure(row, weight=1)

        # Create buttons and place them in the grid (one column, multiple rows)
        for i, (short_name, full_name) in enumerate(button_names.items()):
            button = ctk.CTkButton(self, text=short_name, command=lambda n=full_name: controller.show_management_detail(n),
                                   fg_color="#333333", text_color="white", hover_color="#555555", width=300, font=("Times New Roman", 18)) #Applied Styling
            button.grid(column=0, padx=10, pady=10) 







#################################
# WAITER
#################################
class WaiterManagementFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.db = Database()  # Initialize database connection

        # Ensure the frame expands to fill available space
        self.pack(fill=tk.BOTH, expand=True)

        # Label
        label = ctk.CTkLabel(self, text="WAITER MANAGEMENT", font=("Arial", 16))
        label.pack(pady=15) 

        # Main container frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  

        # Treeview for Waiters
        tree_frame = ctk.CTkFrame(self.main_frame)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10)) 

        # Customize Treeview style
        style = ttk.Style()

        # Configure header style with background color
        style.configure("Treeview.Heading",
                        font=('Arial', 12, 'bold'),
                        background="red",
                        foreground="#585858",
                        padding=10) 

        style.configure("Treeview", font=('Arial', 11))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 

        self.tree = ttk.Treeview(tree_frame, columns=('WaiterID', 'FirstName', 'LastName', 'IsActive'), show='headings', style="Treeview")
        self.tree.heading('WaiterID', text='Waiter ID')
        self.tree.heading('FirstName', text='First Name')
        self.tree.heading('LastName', text='Last Name')
        self.tree.heading('IsActive', text='Is Active')

        # Adjusted column widths
        self.tree.column('WaiterID', width=70, anchor=tk.CENTER)
        self.tree.column('FirstName', width=180, anchor=tk.CENTER)
        self.tree.column('LastName', width=180, anchor=tk.CENTER)
        self.tree.column('IsActive', width=90, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Form Fields for Waiter details
        form_frame = ctk.CTkFrame(self.main_frame, width=350)  
        form_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        ctk.CTkLabel(form_frame, text="First Name:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=8)  # Added font, padding
        self.first_name_entry = ctk.CTkEntry(form_frame, width=200) 
        self.first_name_entry.grid(row=0, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Last Name:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=8)
        self.last_name_entry = ctk.CTkEntry(form_frame, width=200)  
        self.last_name_entry.grid(row=1, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Is Active:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=8)
        # Set the ComboBox width to be the same as Entry fields
        self.is_active_combobox = ctk.CTkComboBox(form_frame, values=['Yes', 'No'], width=200, state="readonly", font=("Arial", 11))  # Matching width
        self.is_active_combobox.grid(row=2, column=1, pady=8)

        # Buttons for CRUD operations
        btn_frame = ctk.CTkFrame(form_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15) 

        ctk.CTkButton(btn_frame, text="Add", command=self.add_waiter, width=120, corner_radius=8).grid(row=0, column=0, padx=8, pady=8)  # Rounded corners
        ctk.CTkButton(btn_frame, text="Update", command=self.update_waiter, width=120, corner_radius=8).grid(row=0, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Delete", command=self.delete_waiter, width=120, corner_radius=8).grid(row=1, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Clear", command=self.clear_form, width=120, corner_radius=8).grid(row=1, column=1, padx=8, pady=8)

        # Back Button (at bottom, inside the form frame)
        back_button = ctk.CTkButton(form_frame, text="Back to Management", command=lambda: controller.show_management_frame(),
                                      fg_color="#777777", hover_color="#666666", text_color="white", width=150, corner_radius=8)  # Gray button
        back_button.grid(row=4, column=0, columnspan=2, pady=(15, 0), padx=10, sticky="ew")  # Place under the CRUD buttons

        # Load initial data
        self.load_waiters()

        # Bind selection in Treeview
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_waiter)




    def load_waiters(self):
        # Clear existing data in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            waiters = self.db.fetch_waiters()  # Fetch waiters from the database
            for waiter in waiters:
                str_waiter = tuple(str(value) for value in waiter)
                self.tree.insert('', tk.END, values=str_waiter)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading waiters: {e}")

    def load_selected_waiter(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            if values:
                first_name = values[1] if len(values) > 1 else ""
                last_name = values[2] if len(values) > 2 else ""
                is_active = values[3] if len(values) > 3 else ""

                self.first_name_entry.delete(0, tk.END)
                self.first_name_entry.insert(0, first_name)
                self.last_name_entry.delete(0, tk.END)
                self.last_name_entry.insert(0, last_name)
                self.is_active_combobox.set('Yes' if is_active == '1' else 'No')
            else:
                self.clear_form()

    def add_waiter(self):
        try:
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            is_active = 1 if self.is_active_combobox.get() == 'Yes' else 0

            if not all([first_name, last_name]):
                messagebox.showerror("Error", "All fields are required!")
                return

            self.db.execute_query(
                "INSERT INTO Waiters (FirstName, LastName, IsActive) VALUES (?, ?, ?)",
                (first_name, last_name, is_active)
            )
            self.load_waiters()
            self.clear_form()
            messagebox.showinfo("Success", "Waiter added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_waiter(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a waiter to update!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for update.")
                return

            waiter_id = int(values[0])  # Convert Waiter ID to integer

            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            is_active = 1 if self.is_active_combobox.get() == 'Yes' else 0

            if not all([first_name, last_name]):
                messagebox.showerror("Error", "All fields are required!")
                return

            self.db.execute_query(
                "UPDATE Waiters SET FirstName=?, LastName=?, IsActive=? WHERE WaiterID=?",
                (first_name, last_name, is_active, waiter_id)
            )
            self.load_waiters()  # Reload waiters list
            messagebox.showinfo("Success", "Waiter updated successfully!")
            self.clear_form()

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_waiter(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a waiter to delete!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for delete.")
                return

            waiter_id = int(values[0])  # Convert Waiter ID to integer

            if messagebox.askyesno("Confirm", "Are you sure you want to delete this waiter?"):
                self.db.execute_query("DELETE FROM Waiters WHERE WaiterID=?", (waiter_id,))
                self.load_waiters() 
                self.clear_form()
                messagebox.showinfo("Success", "Waiter deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        """Clears the form fields and deselects the treeview selection."""
        # Clear the entry fields
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        
        # Clear the combobox selection
        self.is_active_combobox.set('')
        
        # Deselect the selected row in the Treeview
        self.tree.selection_remove(self.tree.selection())







#################################
# TABLE
#################################

class TableManagementFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.db = Database()  # Initialize database connection

        # Ensure the frame expands to fill available space
        self.pack(fill=tk.BOTH, expand=True)

        # Label
        label = ctk.CTkLabel(self, text="TABLE MANAGEMENT", font=("Arial", 16))  #
        label.pack(pady=15)  

        # Main container frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  

        # Treeview for Tables
        tree_frame = ctk.CTkFrame(self.main_frame)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Customize Treeview style
        style = ttk.Style()

        # Configure header style with background color
        style.configure("Treeview.Heading",
                        font=('Arial', 12, 'bold'),
                        background="red",
                        foreground="#585858",
                        padding=10)  

        style.configure("Treeview", font=('Arial', 11))  # Row font
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 

        # Configure the selected row style
        style.map('Treeview', background=[('selected', '#6d6d6d')])

        self.tree = ttk.Treeview(tree_frame, columns=('TableID', 'TableNumber', 'Capacity', 'Status'), show='headings', style="Treeview")
        self.tree.heading('TableID', text='Table ID')
        self.tree.heading('TableNumber', text='Table Number')
        self.tree.heading('Capacity', text='Capacity')
        self.tree.heading('Status', text='Status')

        # Set column widths
        self.tree.column('TableID', width=80, anchor=tk.CENTER)
        self.tree.column('TableNumber', width=100, anchor=tk.CENTER)
        self.tree.column('Capacity', width=100, anchor=tk.CENTER)
        self.tree.column('Status', width=120, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Form Fields for Table details
        form_frame = ctk.CTkFrame(self.main_frame, width=350) 
        form_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        ctk.CTkLabel(form_frame, text="Table Number:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=8)  # Added font, padding
        self.table_number_entry = ctk.CTkEntry(form_frame, width=200) 
        self.table_number_entry.grid(row=0, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Capacity:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=8)
        self.capacity_entry = ctk.CTkEntry(form_frame, width=200) 
        self.capacity_entry.grid(row=1, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Status:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=8)
        self.status_combobox = ctk.CTkComboBox(form_frame, values=['Available', 'Occupied', 'Reserved'], width=200, state="readonly", font=("Arial", 11))  # Increased width, added font
        self.status_combobox.grid(row=2, column=1, pady=8)

        # Buttons for CRUD operations
        btn_frame = ctk.CTkFrame(form_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)

        # Calculate the width of the entry fields and use that for the buttons
        entry_width = self.table_number_entry.winfo_reqwidth()  # Get the requested width of the entry
        button_width = entry_width / 2 - 8  # Divide by 2 and subtract padding

        # Ensure a minimum width for the buttons
        button_width = max(button_width, 80) 

        ctk.CTkButton(btn_frame, text="Add", command=self.add_table, width=button_width, corner_radius=8).grid(row=0, column=0, padx=8, pady=8)  # Rounded corners
        ctk.CTkButton(btn_frame, text="Update", command=self.update_table, width=button_width, corner_radius=8).grid(row=0, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Delete", command=self.delete_table, width=button_width, corner_radius=8).grid(row=1, column=0, padx=8, pady=8)
        clear_button = ctk.CTkButton(btn_frame, text="Clear", command=self.clear_form, width=button_width, corner_radius=8)
        clear_button.grid(row=1, column=1, padx=8, pady=8)

        # Back Button (at bottom, inside the form frame)
        back_button = ctk.CTkButton(form_frame, text="Back to Management", command=lambda: controller.show_management_frame(),
                                      fg_color="#777777", hover_color="#666666", text_color="white", width=150, corner_radius=8)  # Gray button
        back_button.grid(row=4, column=0, columnspan=2, pady=(15, 0), padx=10, sticky="ew")  # Place under the CRUD buttons

        # Load initial data
        self.load_tables()

        # Bind selection in Treeview
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_table)


    def clear_form(self):
        """Clears the form fields and deselects the treeview selection."""
        self.table_number_entry.delete(0, tk.END)
        self.capacity_entry.delete(0, tk.END)
        self.status_combobox.set('')  # Clear the Combobox

        #Deselect the selected row in the Treeview
        self.tree.selection_remove(self.tree.selection())


    def load_tables(self):
        # Clear existing data in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            tables = self.db.fetch_tables()  # Fetch tables from the database
            for table in tables:
                str_table = tuple(str(value) for value in table)
                self.tree.insert('', tk.END, values=str_table)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading tables: {e}")

    def load_selected_table(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            if values:
                table_number = values[1] if len(values) > 1 else ""
                capacity = values[2] if len(values) > 2 else ""
                status = values[3] if len(values) > 3 else ""

                self.table_number_entry.delete(0, tk.END)
                self.table_number_entry.insert(0, table_number)
                self.capacity_entry.delete(0, tk.END)
                self.capacity_entry.insert(0, capacity)
                self.status_combobox.set(status)
            else:
                self.clear_form()

    def add_table(self):
        try:
            table_number = self.table_number_entry.get()
            capacity = int(self.capacity_entry.get())
            status = self.status_combobox.get()

            if not all([table_number, capacity, status]):
                messagebox.showerror("Error", "All fields are required!")
                return

            self.db.execute_query(
                "INSERT INTO Tables (TableNumber, Capacity, Status) VALUES (?, ?, ?)",
                (table_number, capacity, status)
            )
            self.load_tables()
            self.clear_form()
            messagebox.showinfo("Success", "Table added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Capacity must be a number!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_table(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a table to update!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for update.")
                return

            table_id = int(values[0])  # Convert Table ID to integer

            table_number = self.table_number_entry.get()
            capacity = int(self.capacity_entry.get())
            status = self.status_combobox.get()

            if not all([table_number, capacity, status]):
                messagebox.showerror("Error", "All fields are required!")
                return

            self.db.execute_query(
                "UPDATE Tables SET TableNumber=?, Capacity=?, Status=? WHERE TableID=?",
                (table_number, capacity, status, table_id)
            )
            self.load_tables()  # Reload table list
            messagebox.showinfo("Success", "Table updated successfully!")
            self.clear_form()

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_table(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a table to delete!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for delete.")
                return

            table_id = int(values[0])  # Convert Table ID to integer

            if messagebox.askyesno("Confirm", "Are you sure you want to delete this table?"):
                self.db.execute_query("DELETE FROM Tables WHERE TableID=?", (table_id,))
                self.load_tables()  # Reload table list
                self.clear_form()
                messagebox.showinfo("Success", "Table deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))











#################################
# DISCOUNT
#################################

class DiscountManagementFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.db = Database()  # Initialize database connection

        # Ensure the frame expands to fill available space
        self.pack(fill=tk.BOTH, expand=True)

        # Label
        label = ctk.CTkLabel(self, text="DISCOUNT MANAGEMENT", font=("Arial", 16))  # ctk label and larger font
        label.pack(pady=15)  # Increased padding


        # Main container frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # More padding

        # Treeview for Discounts
        tree_frame = ctk.CTkFrame(self.main_frame)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))  # Added right padx

        # Customize Treeview style
        style = ttk.Style()

        # Configure header style with background color
        style.configure("Treeview.Heading",
                        font=('Arial', 12, 'bold'),
                        background="red",
                        foreground="#585858",
                        padding=10)  # White text

        style.configure("Treeview", font=('Arial', 11))  # Row font
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Make it look nicer

        self.tree = ttk.Treeview(tree_frame, columns=('DiscountID', 'DiscountName', 'DiscountType', 'DiscountValue', 'ApplicableTo'), show='headings', style="Treeview")
        self.tree.heading('DiscountID', text='Discount ID')
        self.tree.heading('DiscountName', text='Discount Name')
        self.tree.heading('DiscountType', text='Discount Type')
        self.tree.heading('DiscountValue', text='Discount Value')
        self.tree.heading('ApplicableTo', text='Applicable To')

        # Set column widths
        self.tree.column('DiscountID', width=80, anchor=tk.CENTER)
        self.tree.column('DiscountName', width=150, anchor=tk.CENTER)
        self.tree.column('DiscountType', width=120, anchor=tk.CENTER)
        self.tree.column('DiscountValue', width=120, anchor=tk.CENTER)
        self.tree.column('ApplicableTo', width=120, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Form Fields for Discount details
        form_frame = ctk.CTkFrame(self.main_frame, width=350)  # Increased width
        form_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        ctk.CTkLabel(form_frame, text="Discount Name:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=8)  # Added font, padding
        self.discount_name_entry = ctk.CTkEntry(form_frame, width=200)  # Increased width
        self.discount_name_entry.grid(row=0, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Discount Type:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=8)
        self.discount_type_combobox = ctk.CTkComboBox(form_frame, values=['Percentage', 'Fixed Amount'], width=200, state="readonly", font=("Arial", 11))  # Matching width
        self.discount_type_combobox.grid(row=1, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Discount Value:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=8)
        self.discount_value_entry = ctk.CTkEntry(form_frame, width=200)  # Increased width
        self.discount_value_entry.grid(row=2, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Applicable To:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W, padx=10, pady=8)
        self.applicable_to_combobox = ctk.CTkComboBox(form_frame, values=['Order', 'Item'], width=200, state="readonly", font=("Arial", 11))  # Matching width
        self.applicable_to_combobox.grid(row=3, column=1, pady=8)

        # Buttons for CRUD operations
        btn_frame = ctk.CTkFrame(form_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=15)  # Increased padding

        ctk.CTkButton(btn_frame, text="Add", command=self.add_discount, width=120, corner_radius=8).grid(row=0, column=0, padx=8, pady=8)  # Rounded corners
        ctk.CTkButton(btn_frame, text="Update", command=self.update_discount, width=120, corner_radius=8).grid(row=0, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Delete", command=self.delete_discount, width=120, corner_radius=8).grid(row=1, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Clear", command=self.clear_form, width=120, corner_radius=8).grid(row=1, column=1, padx=8, pady=8)

        # Back Button (at bottom, inside the form frame)
        back_button = ctk.CTkButton(form_frame, text="Back to Management", command=lambda: controller.show_management_frame(),
                                      fg_color="#777777", hover_color="#666666", text_color="white", width=150, corner_radius=8)  # Gray button
        back_button.grid(row=5, column=0, columnspan=2, pady=(15, 0), padx=10, sticky="ew")  # Place under the CRUD buttons

        # Load initial data
        self.load_discounts()

        # Bind selection in Treeview
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_discount)

    def load_discounts(self):
        # Clear existing data in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            if self.db:
                discounts = self.db.fetch_discounts()  # Fetch discounts from the database
                for discount in discounts:
                    str_discount = tuple(str(value) for value in discount)
                    self.tree.insert('', tk.END, values=str_discount)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading discounts: {e}")

    def load_selected_discount(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            if values:
                # Check if enough columns exist before accessing them
                discount_name = values[1] if len(values) > 1 else ""
                discount_type = values[2] if len(values) > 2 else ""
                discount_value = values[3] if len(values) > 3 else ""
                applicable_to = values[4] if len(values) > 4 else ""

                self.discount_name_entry.delete(0, tk.END)
                self.discount_name_entry.insert(0, discount_name)
                self.discount_type_combobox.set(discount_type)
                self.discount_value_entry.delete(0, tk.END)
                self.discount_value_entry.insert(0, discount_value)
                self.applicable_to_combobox.set(applicable_to)
            else:
                self.clear_form()

    def add_discount(self):
        try:
            discount_name = self.discount_name_entry.get()
            discount_type = self.discount_type_combobox.get()
            discount_value = self.discount_value_entry.get()
            applicable_to = self.applicable_to_combobox.get()

            if not all([discount_name, discount_type, discount_value, applicable_to]):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                discount_value = float(discount_value)  # Try converting to float here
            except ValueError:
                messagebox.showerror("Error", "Discount Value must be a number!")
                return


            if self.db:
                self.db.execute_query(
                    "INSERT INTO Discounts (DiscountName, DiscountType, DiscountValue, ApplicableTo) VALUES (?, ?, ?, ?)",
                    (discount_name, discount_type, discount_value, applicable_to)
                )
                self.load_discounts()
                self.clear_form()
                messagebox.showinfo("Success", "Discount added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_discount(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a discount to update!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for update.")
                return

            discount_id = int(values[0])  # Convert Discount ID to integer

            discount_name = self.discount_name_entry.get()
            discount_type = self.discount_type_combobox.get()
            discount_value = self.discount_value_entry.get() 
            applicable_to = self.applicable_to_combobox.get()

            if not all([discount_name, discount_type, discount_value, applicable_to]):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                discount_value = float(discount_value)  # Try converting to float here
            except ValueError:
                messagebox.showerror("Error", "Discount Value must be a number!")
                return

            if self.db:
                self.db.execute_query(
                    "UPDATE Discounts SET DiscountName=?, DiscountType=?, DiscountValue=?, ApplicableTo=? WHERE DiscountID=?",
                    (discount_name, discount_type, discount_value, applicable_to, discount_id)
                )
                self.load_discounts()  # Reload discount list
                messagebox.showinfo("Success", "Discount updated successfully!")
                self.clear_form()

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_discount(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a discount to delete!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for delete.")
                return

            discount_id = int(values[0])  # Convert Discount ID to integer

            if messagebox.askyesno("Confirm", "Are you sure you want to delete this discount?"):
                if self.db:
                    self.db.execute_query("DELETE FROM Discounts WHERE DiscountID=?", (discount_id,))
                    self.load_discounts()  # Reload discount list
                    self.clear_form()
                    messagebox.showinfo("Success", "Discount deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        self.discount_name_entry.delete(0, tk.END)
        self.discount_type_combobox.set('')
        self.discount_value_entry.delete(0, tk.END)
        self.applicable_to_combobox.set('')
        # Deselect the selected row in the Treeview
        self.tree.selection_remove(self.tree.selection())



















#################################
# DRINKS
#################################

class DrinksManagementFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.db = Database()  # Initialize database connection

        # Ensure the frame expands to fill available space
        self.pack(fill=tk.BOTH, expand=True)

        # Label
        label = ctk.CTkLabel(self, text="DRINKS MANAGEMENT", font=("Arial", 16))
        label.pack(pady=15)

        # Main container frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Treeview for Drinks
        tree_frame = ctk.CTkFrame(self.main_frame)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Customize Treeview style
        style = ttk.Style()

        # Configure header style with background color
        style.configure("Treeview.Heading",
                        font=('Arial', 12, 'bold'),
                        background="red",
                        foreground="#585858",
                        padding=10)

        style.configure("Treeview", font=('Arial', 11))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        self.tree = ttk.Treeview(tree_frame, columns=('DrinkID', 'Name', 'Description', 'Price'), show='headings', style="Treeview")
        self.tree.heading('DrinkID', text='Drink ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Price', text='Price')

        # Set column widths
        self.tree.column('DrinkID', width=80, anchor=tk.CENTER)
        self.tree.column('Name', width=150, anchor=tk.CENTER)
        self.tree.column('Description', width=200, anchor=tk.CENTER)
        self.tree.column('Price', width=100, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Form Fields for Drink details
        form_frame = ctk.CTkFrame(self.main_frame, width=350)
        form_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        ctk.CTkLabel(form_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=8)
        self.name_entry = ctk.CTkEntry(form_frame, width=200)
        self.name_entry.grid(row=0, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Description:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=8)
        self.description_entry = ctk.CTkEntry(form_frame, width=200)
        self.description_entry.grid(row=1, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Price:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=8)
        self.price_entry = ctk.CTkEntry(form_frame, width=200)
        self.price_entry.grid(row=2, column=1, pady=8)

        # Buttons for CRUD operations
        btn_frame = ctk.CTkFrame(form_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)

        ctk.CTkButton(btn_frame, text="Add", command=self.add_drink, width=120, corner_radius=8).grid(row=0, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Update", command=self.update_drink, width=120, corner_radius=8).grid(row=0, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Delete", command=self.delete_drink, width=120, corner_radius=8).grid(row=1, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Clear", command=self.clear_form, width=120, corner_radius=8).grid(row=1, column=1, padx=8, pady=8)

        # Back Button (at bottom, inside the form frame)
        back_button = ctk.CTkButton(form_frame, text="Back to Management", command=lambda: controller.show_management_frame(),
                                      fg_color="#777777", hover_color="#666666", text_color="white", width=150, corner_radius=8)
        back_button.grid(row=4, column=0, columnspan=2, pady=(15, 0), padx=10, sticky="ew")

        # Load initial data
        self.load_drinks()

        # Bind selection in Treeview
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_drink)

    def load_drinks(self):
        # Clear existing data in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            drinks = self.db.fetch_drinks()  # Fetch drinks from the database
            for drink in drinks:
                str_drink = tuple(str(value) for value in drink)
                self.tree.insert('', tk.END, values=str_drink)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading drinks: {e}")

    def load_selected_drink(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            if values:
                name = values[1] if len(values) > 1 else ""
                description = values[2] if len(values) > 2 else ""
                price = values[3] if len(values) > 3 else ""

                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, name)
                self.description_entry.delete(0, tk.END)
                self.description_entry.insert(0, description)
                self.price_entry.delete(0, tk.END)
                self.price_entry.insert(0, price)
            else:
                self.clear_form()

    def add_drink(self):
        try:
            name = self.name_entry.get()
            description = self.description_entry.get()
            price = self.price_entry.get()

            if not all([name, description, price]):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                price = float(price)  # Try converting to float here
            except ValueError:
                messagebox.showerror("Error", "Price must be a valid number!")
                return

            self.db.execute_query(
                "INSERT INTO Drinks (Name, Description, Price) VALUES (?, ?, ?)",
                (name, description, price)
            )
            self.load_drinks()
            self.clear_form()
            messagebox.showinfo("Success", "Drink added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_drink(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a drink to update!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for update.")
                return

            drink_id = int(values[0])  # Convert Drink ID to integer

            name = self.name_entry.get()
            description = self.description_entry.get()
            price = self.price_entry.get()

            if not all([name, description, price]):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                price = float(price)  # Try converting to float here
            except ValueError:
                messagebox.showerror("Error", "Price must be a valid number!")
                return

            self.db.execute_query(
                "UPDATE Drinks SET Name=?, Description=?, Price=? WHERE DrinkID=?",
                (name, description, price, drink_id)
            )
            self.load_drinks()  # Reload drinks list
            messagebox.showinfo("Success", "Drink updated successfully!")
            self.clear_form()

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_drink(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a drink to delete!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for delete.")
                return

            drink_id = int(values[0])  # Convert Drink ID to integer

            if messagebox.askyesno("Confirm", "Are you sure you want to delete this drink?"):
                self.db.execute_query("DELETE FROM Drinks WHERE DrinkID=?", (drink_id,))
                self.load_drinks()  # Reload drinks list
                self.clear_form()
                messagebox.showinfo("Success", "Drink deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())






#################################
# MAIN FOOD
#################################
class MainFoodManagementFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.db = Database()  # Initialize database connection

        # Ensure the frame expands to fill available space
        self.pack(fill=tk.BOTH, expand=True)

        # Label
        label = ctk.CTkLabel(self, text="MAIN FOOD MANAGEMENT", font=("Arial", 16))
        label.pack(pady=15)

        # Main container frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Treeview for Main Food items
        tree_frame = ctk.CTkFrame(self.main_frame)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Customize Treeview style
        style = ttk.Style()

        # Configure header style with background color
        style.configure("Treeview.Heading",
                        font=('Arial', 12, 'bold'),
                        background="red",
                        foreground="#585858",
                        padding=10)

        style.configure("Treeview", font=('Arial', 11))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        self.tree = ttk.Treeview(tree_frame, columns=('FoodID', 'Name', 'Description', 'Price'), show='headings', style="Treeview")
        self.tree.heading('FoodID', text='Food ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Price', text='Price')

        # Set column widths
        self.tree.column('FoodID', width=80, anchor=tk.CENTER)
        self.tree.column('Name', width=150, anchor=tk.CENTER)
        self.tree.column('Description', width=200, anchor=tk.CENTER)
        self.tree.column('Price', width=100, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Form Fields for Main Food details
        form_frame = ctk.CTkFrame(self.main_frame, width=350)
        form_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        ctk.CTkLabel(form_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=8)
        self.name_entry = ctk.CTkEntry(form_frame, width=200)
        self.name_entry.grid(row=0, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Description:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=8)
        self.description_entry = ctk.CTkEntry(form_frame, width=200)
        self.description_entry.grid(row=1, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Price:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=8)
        self.price_entry = ctk.CTkEntry(form_frame, width=200)
        self.price_entry.grid(row=2, column=1, pady=8)

        # Buttons for CRUD operations
        btn_frame = ctk.CTkFrame(form_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)

        ctk.CTkButton(btn_frame, text="Add", command=self.add_food, width=120, corner_radius=8).grid(row=0, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Update", command=self.update_food, width=120, corner_radius=8).grid(row=0, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Delete", command=self.delete_food, width=120, corner_radius=8).grid(row=1, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Clear", command=self.clear_form, width=120, corner_radius=8).grid(row=1, column=1, padx=8, pady=8)

        # Back Button (at bottom, inside the form frame)
        back_button = ctk.CTkButton(form_frame, text="Back to Management", command=lambda: controller.show_management_frame(),
                                      fg_color="#777777", hover_color="#666666", text_color="white", width=150, corner_radius=8)
        back_button.grid(row=4, column=0, columnspan=2, pady=(15, 0), padx=10, sticky="ew")

        # Load initial data
        self.load_food_items()

        # Bind selection in Treeview
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_food)

    def load_food_items(self):
        # Clear existing data in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            food_items = self.db.fetch_food_items()  # Fetch food items from the database
            for food in food_items:
                str_food = tuple(str(value) for value in food)
                self.tree.insert('', tk.END, values=str_food)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading food items: {e}")

    def load_selected_food(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            if values:
                name = values[1] if len(values) > 1 else ""
                description = values[2] if len(values) > 2 else ""
                price = values[3] if len(values) > 3 else ""

                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, name)
                self.description_entry.delete(0, tk.END)
                self.description_entry.insert(0, description)
                self.price_entry.delete(0, tk.END)
                self.price_entry.insert(0, price)
            else:
                self.clear_form()

    def add_food(self):
        try:
            name = self.name_entry.get()
            description = self.description_entry.get()
            price = self.price_entry.get()

            if not all([name, description, price]):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                price = float(price)  # Try converting to float here
            except ValueError:
                messagebox.showerror("Error", "Price must be a valid number!")
                return

            self.db.execute_query(
                "INSERT INTO MainFood (Name, Description, Price) VALUES (?, ?, ?)",
                (name, description, price)
            )
            self.load_food_items()
            self.clear_form()
            messagebox.showinfo("Success", "Main food item added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_food(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a food item to update!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for update.")
                return

            food_id = int(values[0])  # Convert Food ID to integer

            name = self.name_entry.get()
            description = self.description_entry.get()
            price = self.price_entry.get()

            if not all([name, description, price]):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                price = float(price)  # Try converting to float here
            except ValueError:
                messagebox.showerror("Error", "Price must be a valid number!")
                return

            self.db.execute_query(
                "UPDATE MainFood SET Name=?, Description=?, Price=? WHERE FoodID=?",
                (name, description, price, food_id)
            )
            self.load_food_items()  # Reload food items list
            messagebox.showinfo("Success", "Main food item updated successfully!")
            self.clear_form()

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_food(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a food item to delete!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for delete.")
                return

            food_id = int(values[0])  # Convert Food ID to integer

            if messagebox.askyesno("Confirm", "Are you sure you want to delete this food item?"):
                self.db.execute_query("DELETE FROM MainFood WHERE FoodID=?", (food_id,))
                self.load_food_items()  # Reload food items list
                self.clear_form()
                messagebox.showinfo("Success", "Main food item deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        # Deselect the selected row in the Treeview
        self.tree.selection_remove(self.tree.selection())





#################################
# MODIFIRES
#################################

class ModifiersManagementFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.db = Database()  # Initialize database connection

        # Ensure the frame expands to fill available space
        self.pack(fill=tk.BOTH, expand=True)

        # Label
        label = ctk.CTkLabel(self, text="MODIFIERS MANAGEMENT", font=("Arial", 16))
        label.pack(pady=15)

        # Main container frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Treeview for Modifiers
        tree_frame = ctk.CTkFrame(self.main_frame)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Customize Treeview style
        style = ttk.Style()

        # Configure header style with background color
        style.configure("Treeview.Heading",
                        font=('Arial', 12, 'bold'),
                        background="red",
                        foreground="#585858",
                        padding=10)

        style.configure("Treeview", font=('Arial', 11))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        self.tree = ttk.Treeview(tree_frame, columns=('ModifierID', 'Name', 'Description', 'Price'), show='headings', style="Treeview")
        self.tree.heading('ModifierID', text='Modifier ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Price', text='Price')

        # Set column widths
        self.tree.column('ModifierID', width=80, anchor=tk.CENTER)
        self.tree.column('Name', width=150, anchor=tk.CENTER)
        self.tree.column('Description', width=200, anchor=tk.CENTER)
        self.tree.column('Price', width=100, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Form Fields for Modifier details
        form_frame = ctk.CTkFrame(self.main_frame, width=350)
        form_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        ctk.CTkLabel(form_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=8)
        self.name_entry = ctk.CTkEntry(form_frame, width=200)
        self.name_entry.grid(row=0, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Description:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=8)
        self.description_entry = ctk.CTkEntry(form_frame, width=200)
        self.description_entry.grid(row=1, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Price:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=8)
        self.price_entry = ctk.CTkEntry(form_frame, width=200)
        self.price_entry.grid(row=2, column=1, pady=8)

        # Buttons for CRUD operations
        btn_frame = ctk.CTkFrame(form_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)

        ctk.CTkButton(btn_frame, text="Add", command=self.add_modifier, width=120, corner_radius=8).grid(row=0, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Update", command=self.update_modifier, width=120, corner_radius=8).grid(row=0, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Delete", command=self.delete_modifier, width=120, corner_radius=8).grid(row=1, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Clear", command=self.clear_form, width=120, corner_radius=8).grid(row=1, column=1, padx=8, pady=8)

        # Back Button (at bottom, inside the form frame)
        back_button = ctk.CTkButton(form_frame, text="Back to Management", command=lambda: controller.show_management_frame(),
                                      fg_color="#777777", hover_color="#666666", text_color="white", width=150, corner_radius=8)
        back_button.grid(row=4, column=0, columnspan=2, pady=(15, 0), padx=10, sticky="ew")

        # Load initial data
        self.load_modifiers()

        # Bind selection in Treeview
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_modifier)

    def load_modifiers(self):
        # Clear existing data in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            modifiers = self.db.fetch_modifiers()  # Fetch modifiers from the database
            for modifier in modifiers:
                str_modifier = tuple(str(value) for value in modifier)
                self.tree.insert('', tk.END, values=str_modifier)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading modifiers: {e}")

    def load_selected_modifier(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            if values:
                name = values[1] if len(values) > 1 else ""
                description = values[2] if len(values) > 2 else ""
                price = values[3] if len(values) > 3 else ""

                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, name)
                self.description_entry.delete(0, tk.END)
                self.description_entry.insert(0, description)
                self.price_entry.delete(0, tk.END)
                self.price_entry.insert(0, price)
            else:
                self.clear_form()

    def add_modifier(self):
        try:
            name = self.name_entry.get()
            description = self.description_entry.get()
            price = self.price_entry.get()

            if not all([name, description, price]):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                price = float(price)  # Try converting to float here
            except ValueError:
                messagebox.showerror("Error", "Price must be a valid number!")
                return

            self.db.execute_query(
                "INSERT INTO Modifiers (Name, Description, Price) VALUES (?, ?, ?)",
                (name, description, price)
            )
            self.load_modifiers()
            self.clear_form()
            messagebox.showinfo("Success", "Modifier added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_modifier(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a modifier to update!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for update.")
                return

            modifier_id = int(values[0])  # Convert Modifier ID to integer

            name = self.name_entry.get()
            description = self.description_entry.get()
            price = self.price_entry.get()

            if not all([name, description, price]):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                price = float(price)  # Try converting to float here
            except ValueError:
                messagebox.showerror("Error", "Price must be a valid number!")
                return

            self.db.execute_query(
                "UPDATE Modifiers SET Name=?, Description=?, Price=? WHERE ModifierID=?",
                (name, description, price, modifier_id)
            )
            self.load_modifiers()  # Reload modifiers list
            messagebox.showinfo("Success", "Modifier updated successfully!")
            self.clear_form()

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_modifier(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a modifier to delete!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for delete.")
                return

            modifier_id = int(values[0])  # Convert Modifier ID to integer

            if messagebox.askyesno("Confirm", "Are you sure you want to delete this modifier?"):
                self.db.execute_query("DELETE FROM Modifiers WHERE ModifierID=?", (modifier_id,))
                self.load_modifiers()  # Reload modifiers list
                self.clear_form()
                messagebox.showinfo("Success", "Modifier deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        # Deselect the selected row in the Treeview
        self.tree.selection_remove(self.tree.selection())




#################################
# CUSTOMER MANAGEMENT
#################################

class CustomerManagementFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.db = Database()  # Initialize database connection

        # Label
        label = ctk.CTkLabel(self, text="CUSTOMER MANAGEMENT", font=("Arial", 16))
        label.pack(pady=15)

        # Main container frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Treeview for Customers
        tree_frame = ctk.CTkFrame(self.main_frame)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Customize Treeview style
        style = ttk.Style()

        # Configure header style with background color
        style.configure("Treeview.Heading",
                        font=('Arial', 12, 'bold'),
                        background="red",
                        foreground="#585858",
                        padding=10)

        style.configure("Treeview", font=('Arial', 11))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        self.tree = ttk.Treeview(tree_frame,
                                 columns=('CustomerID', 'Name', 'PhoneNumber', 'Email', 'PartySize'),
                                 show='headings', style="Treeview")
        self.tree.heading('CustomerID', text='Customer ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('PhoneNumber', text='Phone Number')
        self.tree.heading('Email', text='Email')
        self.tree.heading('PartySize', text='Party Size')

        # Set column widths
        self.tree.column('CustomerID', width=50, anchor=tk.CENTER)
        self.tree.column('Name', width=150, anchor=tk.CENTER)
        self.tree.column('PhoneNumber', width=100, anchor=tk.CENTER)
        self.tree.column('Email', width=150, anchor=tk.CENTER)
        self.tree.column('PartySize', width=50, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Form Fields for Customer details
        form_frame = ctk.CTkFrame(self.main_frame, width=350)
        form_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        ctk.CTkLabel(form_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=8)
        self.name_entry = ctk.CTkEntry(form_frame, width=200)
        self.name_entry.grid(row=0, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Phone Number:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=8)
        self.phone_number_entry = ctk.CTkEntry(form_frame, width=200)
        self.phone_number_entry.grid(row=1, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Email:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=8)
        self.email_entry = ctk.CTkEntry(form_frame, width=200)
        self.email_entry.grid(row=2, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Party Size:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W, padx=10, pady=8)
        self.party_size_entry = ctk.CTkEntry(form_frame, width=200)
        self.party_size_entry.grid(row=3, column=1, pady=8)

        # Buttons for CRUD operations
        btn_frame = ctk.CTkFrame(form_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=15)

        ctk.CTkButton(btn_frame, text="Add", command=self.add_customer, width=120, corner_radius=8).grid(row=0, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Update", command=self.update_customer, width=120, corner_radius=8).grid(row=0, column=1, padx=8,
                                                                                          pady=8)
        ctk.CTkButton(btn_frame, text="Delete", command=self.delete_customer, width=120, corner_radius=8).grid(row=1, column=0, padx=8,
                                                                                          pady=8)
        ctk.CTkButton(btn_frame, text="Clear", command=self.clear_form, width=120, corner_radius=8).grid(row=1, column=1, padx=8, pady=8)

        # Back Button (at bottom, inside the form frame)
        back_button = ctk.CTkButton(form_frame, text="Back to Management",
                                 command=lambda: controller.show_management_frame(),
                                  fg_color="#777777", hover_color="#666666", text_color="white", width=150, corner_radius=8)
        back_button.grid(row=5, column=0, columnspan=2, pady=(15, 0), padx=10, sticky="ew")

        # Load initial data
        self.load_customers()

        # Bind selection in Treeview
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_customer)

    def load_customers(self):
        # Clear existing data in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            customers = self.db.fetch_customers()  # Fetch customers from the database
            for customer in customers:
                str_customer = tuple(str(value) for value in customer)
                self.tree.insert('', tk.END, values=str_customer)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading customers: {e}")

    def load_selected_customer(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            if values:
                name = values[1] if len(values) > 1 else ""
                phone_number = values[2] if len(values) > 2 else ""
                email = values[3] if len(values) > 3 else ""
                party_size = values[4] if len(values) > 4 else ""

                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, name)
                self.phone_number_entry.delete(0, tk.END)
                self.phone_number_entry.insert(0, phone_number)
                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, email)
                self.party_size_entry.delete(0, tk.END)
                self.party_size_entry.insert(0, party_size)
            else:
                self.clear_form()

    def add_customer(self):
        try:
            name = self.name_entry.get()
            phone_number = self.phone_number_entry.get()
            email = self.email_entry.get()
            party_size = self.party_size_entry.get()

            if not all([name, phone_number, email, party_size]):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                party_size = int(party_size)  # Try converting to int here
            except ValueError:
                messagebox.showerror("Error", "Party Size must be a number!")
                return

            self.db.execute_query(
                "INSERT INTO Customers (Name, PhoneNumber, Email, PartySize) VALUES (?, ?, ?, ?)",
                (name, phone_number, email, party_size)
            )
            self.load_customers()
            self.clear_form()
            messagebox.showinfo("Success", "Customer added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_customer(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a customer to update!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for update.")
                return

            customer_id = int(values[0])  # Convert Customer ID to integer

            name = self.name_entry.get()
            phone_number = self.phone_number_entry.get()
            email = self.email_entry.get()
            party_size = self.party_size_entry.get()

            if not all([name, phone_number, email, party_size]):
                messagebox.showerror("Error", "All fields are required!")
                return
            try:
                party_size = int(party_size)  # Try converting to int here
            except ValueError:
                messagebox.showerror("Error", "Party Size must be a number!")
                return

            self.db.execute_query(
                "UPDATE Customers SET Name=?, PhoneNumber=?, Email=?, PartySize=? WHERE CustomerID=?",
                (name, phone_number, email, party_size, customer_id)
            )
            self.load_customers()  # Reload customer list
            messagebox.showinfo("Success", "Customer updated successfully!")
            self.clear_form()

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_customer(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a customer to delete!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for delete.")
                return

            customer_id = int(values[0])  # Convert Customer ID to integer

            if messagebox.askyesno("Confirm", "Are you sure you want to delete this customer?"):
                self.db.execute_query("DELETE FROM Customers WHERE CustomerID=?", (customer_id,))
                self.load_customers()  # Reload customer list
                self.clear_form()
                messagebox.showinfo("Success", "Customer deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.party_size_entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())





#################################
# RECEPIES MANAGEMENT
#################################


class RecipesManagementFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color=("black", "black")) 

        self.controller = controller
        label = ctk.CTkLabel(self, text="RECEPIES MANAGMENT", font=("Arial", 16))
        label.pack(pady=15)
        back_button = ctk.CTkButton(self, text="Back to Management", command=lambda: controller.show_management_frame(),
                                      fg_color="#777777", hover_color="#666666", text_color="black", width=150, corner_radius=8)
        back_button.pack(pady=10)

        
#################################
# REPORT
#################################

class ReportFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.db = Database() 

        # Label
        label = ctk.CTkLabel(self, text="REPORT", font=("Arial", 16))
        label.pack(pady=15)


        # Style configuration for Treeview
        self.style = ttk.Style()
        self.style.configure("Custom.Treeview",
                             font=('Arial', 8),
                             rowheight=40)  

        self.style.layout("Custom.Treeview",
                          [('Custom.Treeview.treearea', {'sticky': 'nswe'})])

        # Main container frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Treeview for Reports
        tree_frame = ctk.CTkFrame(self.main_frame)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        self.tree = ttk.Treeview(tree_frame,
                                 columns=('ReportID', 'TableNumber', 'OrderView', 'CustomerName',
                                          'WaiterName', 'PartySize', 'TotalPrice', 'Status', 'ReportDate'),
                                 show='headings',
                                 style="Custom.Treeview")

        self.tree.heading('ReportID', text='Report ID')
        self.tree.heading('TableNumber', text='Table Number')
        self.tree.heading('OrderView', text='Order View')
        self.tree.heading('CustomerName', text='Customer Name')
        self.tree.heading('WaiterName', text='Waiter Name')
        self.tree.heading('PartySize', text='Party Size')
        self.tree.heading('TotalPrice', text='Total Price')
        self.tree.heading('Status', text='Status')
        self.tree.heading('ReportDate', text='Report Date')

        # Set column widths
        self.tree.column('ReportID', width=50, anchor=tk.CENTER)
        self.tree.column('TableNumber', width=50, anchor=tk.CENTER)
        self.tree.column('OrderView', width=250, anchor=tk.W)  
        self.tree.column('CustomerName', width=100, anchor=tk.CENTER)
        self.tree.column('WaiterName', width=100, anchor=tk.CENTER)
        self.tree.column('PartySize', width=50, anchor=tk.CENTER)
        self.tree.column('TotalPrice', width=50, anchor=tk.CENTER)
        self.tree.column('Status', width=50, anchor=tk.CENTER)
        self.tree.column('ReportDate', width=90, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Form Fields for Report details
        form_frame = ctk.CTkFrame(self.main_frame, width=350)
        form_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

        ctk.CTkLabel(form_frame, text="Table Number:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=8)
        self.table_number_entry = ctk.CTkEntry(form_frame, width=200)
        self.table_number_entry.grid(row=0, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Order View:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=8)
        self.order_view_entry = ctk.CTkEntry(form_frame, width=200)
        self.order_view_entry.grid(row=1, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Customer Name:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=8)
        self.customer_name_entry = ctk.CTkEntry(form_frame, width=200)
        self.customer_name_entry.grid(row=2, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Waiter Name:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W, padx=10, pady=8)
        self.waiter_name_entry = ctk.CTkEntry(form_frame, width=200)
        self.waiter_name_entry.grid(row=3, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Party Size:", font=("Arial", 12)).grid(row=4, column=0, sticky=tk.W, padx=10, pady=8)
        self.party_size_entry = ctk.CTkEntry(form_frame, width=200)
        self.party_size_entry.grid(row=4, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Total Price:", font=("Arial", 12)).grid(row=5, column=0, sticky=tk.W, padx=10, pady=8)
        self.total_price_entry = ctk.CTkEntry(form_frame, width=200)
        self.total_price_entry.grid(row=5, column=1, pady=8)

        ctk.CTkLabel(form_frame, text="Status:", font=("Arial", 12)).grid(row=6, column=0, sticky=tk.W, padx=10, pady=8)
        self.status_combobox = ctk.CTkComboBox(form_frame, values=["Open", "Closed", "Void"], state="readonly", font=("Arial", 11))
        self.status_combobox.grid(row=6, column=1, pady=8)
        self.status_combobox.set("Open") # SET OPEN AS DEFAULT

        # Buttons for CRUD operations
        btn_frame = ctk.CTkFrame(form_frame)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=15)

        ctk.CTkButton(btn_frame, text="Add", command=self.add_report_db, width=120, corner_radius=8).grid(row=0, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Update", command=self.update_report_db, width=120, corner_radius=8).grid(row=0, column=1, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Delete", command=self.delete_report_db, width=120, corner_radius=8).grid(row=1, column=0, padx=8, pady=8)
        ctk.CTkButton(btn_frame, text="Clear", command=self.clear_form, width=120, corner_radius=8).grid(row=1, column=1, padx=8, pady=8)

        # Load initial data
        self.load_reports()

        # Bind selection in Treeview
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_report)

      
        back_button = ctk.CTkButton(form_frame, text="Back to Management", command=lambda: controller.show_management_frame(),
                                      fg_color="#777777", hover_color="#666666", text_color="white", width=150, corner_radius=8)  # Gray button
        back_button.grid(row=9, column=0, columnspan=2, pady=(15, 0), padx=10, sticky="ew")  # Place under the CRUD buttons

        back_button = ctk.CTkButton(form_frame, text="Back to Ordering", command=lambda: controller.show_ordering_frame(),
                                      fg_color="#777777", hover_color="#666666", text_color="white", width=150, corner_radius=8)  # Gray button
        back_button.grid(row=8, column=0, columnspan=2, pady=(15, 0), padx=10, sticky="ew")  # Place under the CRUD buttons


    def load_reports(self):
        # Clear existing data in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            with self.db.conn:  # Use context manager for connection
                with self.db.conn.cursor() as cursor: # Use context manager for cursor
                    cursor.execute("SELECT ReportID, TableNumber, OrderView, CustomerName, WaiterName, PartySize, TotalPrice, Status, ReportDate FROM Reports ORDER BY ReportID DESC")
                    reports = cursor.fetchall()  # Fetch reports from the database

                    for report in reports:
                        str_report = tuple(str(value) for value in report)
                        self.tree.insert('', tk.END, values=str_report)


        except Exception as e:
            messagebox.showerror("Error", f"Error loading reports: {e}")

    def load_selected_report(self, event):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a report to update!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for update.")
                return

            table_number = values[1] if len(values) > 1 else ""
            order_view = values[2] if len(values) > 2 else ""
            customer_name = values[3] if len(values) > 3 else ""
            waiter_name = values[4] if len(values) > 4 else ""
            party_size = values[5] if len(values) > 5 else ""
            total_price = values[6] if len(values) > 6 else ""
            status = values[7] if len(values) > 7 else ""

            self.table_number_entry.delete(0, tk.END)
            self.table_number_entry.insert(0, table_number)
            self.order_view_entry.delete(0, tk.END)
            self.order_view_entry.insert(0, order_view)
            self.customer_name_entry.delete(0, tk.END)
            self.customer_name_entry.insert(0, customer_name)
            self.waiter_name_entry.delete(0, tk.END)
            self.waiter_name_entry.insert(0, waiter_name)
            self.party_size_entry.delete(0, tk.END)
            self.party_size_entry.insert(0, party_size)
            self.total_price_entry.delete(0, tk.END)
            self.total_price_entry.insert(0, total_price)
            self.status_combobox.set(status)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading report data: {e}")

    def populate_report_data(self, data):
        """Populates the entry fields with the data from the order."""
        print("populate_report_data called")  # print for debug
        print(f"Data received: {data}")
        self.clear_form()  # Clear existing data

        self.table_number_entry.insert(0, data["table_number"])
        self.order_view_entry.insert(0, data["order_view"])
        self.customer_name_entry.insert(0, data["customer_name"])
        self.waiter_name_entry.insert(0, data["waiter_name"])
        self.party_size_entry.insert(0, str(data["party_size"]))
        self.total_price_entry.insert(0, str(data["total_price"]))
        #self.status_combobox.set(data["status"]) #REMOVE THIS TO SET AT THE CLEAR FORM

        # Insert data on DB and refresh.
        self.add_report_db(data)
        self.load_reports()


    def add_report_db(self, data=None):
        try:
            # Determine the source of the data
            if data:
                # Data is coming from OrderingFrame (place_order)
                table_number = data["table_number"]
                order_view = data["order_view"]
                customer_name = data["customer_name"]
                waiter_name = data["waiter_name"]
                party_size = data["party_size"]
                total_price = data["total_price"]
                status = data["status"]

            else:
                # Data is coming from direct user input in the form fields
                table_number = self.table_number_entry.get()
                order_view = self.order_view_entry.get()
                customer_name = self.customer_name_entry.get()
                waiter_name = self.waiter_name_entry.get()
                try:
                    party_size = int(self.party_size_entry.get())
                except ValueError:
                    messagebox.showerror("Error", "Party Size must be a number!")
                    return
                try:
                    total_price = float(self.total_price_entry.get())
                except ValueError:
                    messagebox.showerror("Error", "Total Price must be a number!")
                    return
                status = self.status_combobox.get()

            report_date = datetime.datetime.now() #Get datetime!

            if not all([table_number, order_view, customer_name, waiter_name, party_size, total_price, status]):
                messagebox.showerror("Error", "All fields are required!")
                return

            #Fix the query to support foreign key link
            self.db.execute_query(
                "INSERT INTO Reports (TableNumber, OrderView, CustomerName, WaiterName, PartySize, TotalPrice, Status, ReportDate) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (table_number, order_view, customer_name, waiter_name, party_size, total_price, status, report_date)
            )
            self.load_reports()
            self.clear_form() #THIS WILL SET THE DEFAULT FORM.
            messagebox.showinfo("Success", "Report added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def update_report_db(self):
        """Updates an existing report in the database."""
        self.tree.focus_set()  # Force focus back to the Treeview - IMPORTANT FIX
        selected = self.tree.focus()

        if not selected:
            messagebox.showerror("Error", "Please select a report to update!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for update.")
                return

            report_id = int(values[0])  # Convert Report ID to integer

            table_number = self.table_number_entry.get()
            order_view = self.order_view_entry.get()
            customer_name = self.customer_name_entry.get()
            waiter_name = self.waiter_name_entry.get()
            try:
                party_size = int(self.party_size_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Party Size must be a number!")
                return
            try:
                total_price = float(self.total_price_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Total Price must be a number!")
                return
            status = self.status_combobox.get()

            if not all([table_number, order_view, customer_name, waiter_name, party_size, total_price, status]):
                messagebox.showerror("Error", "All fields are required!")
                return

            # Get the ORIGINAL status before the update
            original_status = values[7]

            #Modify query to support FK

            self.db.execute_query(
                "UPDATE Reports SET TableNumber=?, OrderView=?, CustomerName=?, WaiterName=?, PartySize=?, TotalPrice=?, Status=? "
                "WHERE ReportID=?",
                (table_number, order_view, customer_name, waiter_name, party_size, total_price, status, report_id)
            )
            self.load_reports()  # Reload report list
            messagebox.showinfo("Success", "Report updated successfully!")
            self.clear_form()

            # Check if the status has changed to "Closed" or "Void" and show the message (only once)
            if original_status != status and (status == "Closed" or status == "Void"):
                messagebox.showinfo(
                    "Table Update Reminder",
                    f"Please update Table {table_number} to available!"
                )


        except Exception as e:
            messagebox.showerror("Error", str(e))

    # (Remaining code from the ReportFrame class)


    def delete_report_db(self):
        """Deletes a report from the database."""
        self.tree.focus_set()  # Force focus back to the Treeview - IMPORTANT FIX
        selected = self.tree.focus()

        if not selected:
            messagebox.showerror("Error", "Please select a report to delete!")
            return

        try:
            values = self.tree.item(selected, 'values')
            if not values or len(values) < 1:
                messagebox.showerror("Error", "No valid selection for update.")
                return

            report_id = int(values[0])  # Convert Report ID to integer

            if messagebox.askyesno("Confirm", "Are you sure you want to delete this report?"):
                self.db.execute_query("DELETE FROM Reports WHERE ReportID=?", (report_id,))
                self.load_reports()  # Reload report list
                self.clear_form()
                messagebox.showinfo("Success", "Report deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def clear_form(self):
        self.table_number_entry.delete(0, tk.END)
        self.order_view_entry.delete(0, tk.END)
        self.customer_name_entry.delete(0, tk.END)
        self.waiter_name_entry.delete(0, tk.END)
        self.party_size_entry.delete(0, tk.END)
        self.total_price_entry.delete(0, tk.END)
        self.status_combobox.set("Open") #SET VALUE HERE.
        # Deselect the selected row in the Treeview
        self.tree.selection_remove(self.tree.selection())










if __name__ == "__main__":
    app = RestaurantPOS()
    app.mainloop()
