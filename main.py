import sqlite3
with sqlite3.connect('countryinfo.db') as db:
    pass
CREATE TABLE countryInfo(
    CountryName text,
    Vaccine text,
    WaterStatus text,
    Allergies text,
    Weather text,
    LGBTQsafety text,
    WomenSafety text,
    Primary Key(CountryName));



def display_info (place):
  choice = input("What would you like to know? 1) Vaccine+medicine status. 2) Drinking water. 3) Allergies. 4) Weather conditions. 5) LGBTQ+ safety. 6) Women's safety.")
  if choice == 1:
    fetchData = "SELECT Vaccine from countryinfo.db"

print ("Hello user! Welcome to the app!")
place = input("Where are you travelling to?")

