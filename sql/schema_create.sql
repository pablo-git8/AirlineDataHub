-- Create Dim_OpCo table
CREATE TABLE IF NOT EXISTS Dim_OpCo (
    OpCo_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    OpCo_Code TEXT UNIQUE,
    OpCo_Name TEXT,
    Subsidiary_Code TEXT,
    Subsidiary_Name TEXT
)

-- Create Dim_Airport table
CREATE TABLE IF NOT EXISTS Dim_Airport (
    Airport_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Airport_Code TEXT UNIQUE,
    Airport_Name TEXT,
    Country_Code TEXT,
    Country_Name TEXT,
    Region TEXT
)

-- Create Dim_Time table
CREATE TABLE IF NOT EXISTS Dim_Time (
    Time_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE UNIQUE,
    Year INTEGER,
    Quarter INTEGER
)

-- Create Fact_Flights table
CREATE TABLE IF NOT EXISTS Fact_Flights (
    Flight_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    OpCo_ID INTEGER,
    Departure_Airport_ID INTEGER,
    Arrival_Airport_ID INTEGER,
    Time_ID INTEGER,
    Aircraft_Type TEXT,
    Cabin TEXT,
    Service TEXT,
    Passengers INTEGER,
    Flights INTEGER,
    FOREIGN KEY (OpCo_ID) REFERENCES Dim_OpCo(OpCo_ID),
    FOREIGN KEY (Departure_Airport_ID) REFERENCES Dim_Airport(Airport_ID),
    FOREIGN KEY (Arrival_Airport_ID) REFERENCES Dim_Airport(Airport_ID),
    FOREIGN KEY (Time_ID) REFERENCES Dim_Time(Time_ID)
)