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
    Year,
    Quarter,
    Operating_Company,
    Country,
    Region;
