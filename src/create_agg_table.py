# Imports
import sqlite3

def create_aggregation_table():
    # SQL query to create an aggregation table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS Aggregated_Passenger_Data (
            Operating_Company TEXT,
            Country TEXT,
            Region TEXT,
            Year INTEGER,
            Quarter TEXT,
            Total_Passengers INTEGER
    );
    """
    
    # SQL query to aggregate data and insert into the new table
    aggregation_query = """
        INSERT INTO Aggregated_Passenger_Data (Operating_Company, Country, Region, Year, Quarter, Total_Passengers)
        SELECT
            o.OpCo_Name AS Operating_Company,
            a.Country_Name AS Country,
            a.Region AS Region,
            t.Year AS Year,
            'Q' || t.Quarter AS Quarter,
            SUM(f.Passengers) AS Total_Passengers
        FROM
            Fact_Flights f
            JOIN Dim_OpCo o ON f.OpCo_ID = o.OpCo_ID
            JOIN Dim_Airport a ON f.Departure_Airport_ID = a.Airport_ID OR f.Arrival_Airport_ID = a.Airport_ID
            JOIN Dim_Time t ON f.Time_ID = t.Time_ID
        GROUP BY
            Operating_Company,
            Country,
            Region,
            Year,
            Quarter
        ORDER BY
            SUM(f.Passengers) DESC;
    """
    try:
        # Connect to the SQLite database
        with sqlite3.connect('../data/processed/aig_data_warehouse.db') as conn:
            cursor = conn.cursor()
            # Create the aggregation table
            cursor.execute(create_table_query)
            # Insert data
            cursor.execute(aggregation_query)
            
            # Commit the changes to the database
            conn.commit()
    except sqlite3.Error as e:
        print(f"A DDBB error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    create_aggregation_table()
