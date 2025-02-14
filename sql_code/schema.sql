-- Drop the database if it exists
IF EXISTS (SELECT * FROM sys.databases WHERE name = 'RestaurantPOS')
BEGIN
    ALTER DATABASE RestaurantPOS SET SINGLE_USER WITH ROLLBACK IMMEDIATE;  -- Disconnect active sessions
    DROP DATABASE RestaurantPOS;
END
GO

-- Create the database
CREATE DATABASE RestaurantPOS;
GO

-- Use the database
USE RestaurantPOS;
GO

-- Waiters Table
CREATE TABLE Waiters (
    WaiterID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    IsActive BIT NOT NULL DEFAULT 1
);

-- Tables Table
CREATE TABLE Tables (
    TableID INT PRIMARY KEY IDENTITY(1,1),
    TableNumber VARCHAR(10) NOT NULL,
    Capacity INT DEFAULT 2,
    Status VARCHAR(20) CHECK (Status IN ('Available', 'Occupied', 'Reserved')) DEFAULT 'Available'
);

-- Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(50),
    PhoneNumber VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    PartySize INT DEFAULT 1
);

-- Drinks Table
CREATE TABLE Drinks (
    DrinkID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL
);

-- MainFood Table
CREATE TABLE MainFood (
    FoodID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL
);

-- Modifiers Table
CREATE TABLE Modifiers (
    ModifierID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100) NOT NULL,
	Description TEXT,
    Price DECIMAL(10, 2) DEFAULT 0.00
);

-- Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    TableID INT NOT NULL,
    WaiterID INT NOT NULL,
    CustomerID INT,
    OrderDate DATETIME DEFAULT GETDATE(),
    TotalAmount DECIMAL(10, 2) NOT NULL,
    OrderStatus VARCHAR(20) CHECK (OrderStatus IN ('Open', 'Closed', 'Void')) DEFAULT 'Open',
	PaymentMethod VARCHAR(50),
	FOREIGN KEY (TableID) REFERENCES Tables(TableID),
    FOREIGN KEY (WaiterID) REFERENCES Waiters(WaiterID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- OrderItems Table (Links Orders to Menu Items)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY IDENTITY(1,1),
    OrderID INT NOT NULL,
    MenuItemType VARCHAR(10) NOT NULL CHECK (MenuItemType IN ('Drink', 'Food')),
    MenuItemID INT NOT NULL,
    Quantity INT NOT NULL DEFAULT 1,
    ItemPrice DECIMAL(10, 2) NOT NULL,
    Notes TEXT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- OrderItemModifiers Table (Modifiers applied to a specific OrderItem)
CREATE TABLE OrderItemModifiers (
    OrderItemID INT NOT NULL,
    ModifierID INT NOT NULL,
    ModifierPrice DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (OrderItemID, ModifierID),
    FOREIGN KEY (OrderItemID) REFERENCES OrderItems(OrderItemID),
    FOREIGN KEY (ModifierID) REFERENCES Modifiers(ModifierID)
);

-- Discounts Table
CREATE TABLE Discounts (
    DiscountID INT PRIMARY KEY IDENTITY(1,1),
    DiscountName VARCHAR(100) NOT NULL,
    DiscountType VARCHAR(20) NOT NULL CHECK (DiscountType IN ('Percentage', 'Fixed Amount')),
    DiscountValue DECIMAL(10, 2) NOT NULL,
    ApplicableTo VARCHAR(20) NOT NULL CHECK (ApplicableTo IN ('Order', 'Item'))
);


-- Report Table
CREATE TABLE Reports (
    ReportID INT PRIMARY KEY IDENTITY(1,1),
    TableNumber VARCHAR(10) NOT NULL,
    OrderView TEXT,  -- Could be a formatted string or JSON if needed
    CustomerName VARCHAR(50),
    WaiterName VARCHAR(100),
    PartySize INT,
    TotalPrice DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(20) CHECK (Status IN ('Open', 'Closed', 'Void')) NOT NULL,
    ReportDate DATETIME DEFAULT GETDATE()
);

-- Add FK to Table
ALTER TABLE Reports ADD TableID INT NOT NULL DEFAULT 1;
ALTER TABLE Reports ADD CONSTRAINT FK_Reports_Tables FOREIGN KEY (TableID) REFERENCES Tables(TableID);

-- Add FK to Waiter
ALTER TABLE Reports ADD WaiterID INT NOT NULL DEFAULT 1;
ALTER TABLE Reports ADD CONSTRAINT FK_Reports_Waiters FOREIGN KEY (WaiterID) REFERENCES Waiters(WaiterID);

-- Add FK to Customer
ALTER TABLE Reports ADD CustomerID INT DEFAULT NULL;
ALTER TABLE Reports ADD CONSTRAINT FK_Reports_Customers FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID);
GO
