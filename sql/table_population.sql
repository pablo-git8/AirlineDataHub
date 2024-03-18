-- Populate Aircraft dimension table
('''INSERT OR IGNORE INTO Dim_OpCo (OpCo_Code, OpCo_Name, Subsidiary_Code, Subsidiary_Name)
        VALUES (?, ?, ?, ?)''', (row['OpCo_Code'], row['OpCo_Name'], row['Subsidiary_Code'], row['Subsidiary_Name']))

('SELECT OpCo_ID FROM Dim_OpCo WHERE OpCo_Code = ?', (row['OpCo_Code'],))


-- Populate Airport dimension table
('''INSERT OR IGNORE INTO Dim_Airport (Airport_Code, Airport_Name, Country_Code, Country_Name, Region)
        VALUES (?, ?, ?, ?, ?)''', 
        (row[airport_code], row[airport_name], row[country_code], row[country_name], row[region]))

('SELECT Airport_ID FROM Dim_Airport WHERE Airport_Code = ?', (row[airport_code],))


-- Populate Time dimension table
('''INSERT OR IGNORE INTO Dim_Time (Date, Year, Quarter)
        VALUES (?, ?, ?)''', 
        (row['Date'], row['Year'], row['Quarter']))

('SELECT Time_ID FROM Dim_Time WHERE Date = ?', (row['Date'],))


-- Populate Flight fact table
('''INSERT INTO Fact_Flights (OpCo_ID, Departure_Airport_ID, Arrival_Airport_ID, Time_ID, Aircraft_Type, Cabin, Service, Passengers, Flights)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (opco_id, departure_airport_id, arrival_airport_id, time_id, row['Aircraft_Type'], row['Cabin'], row['Service'], row['Passengers'], row['Flights']))
