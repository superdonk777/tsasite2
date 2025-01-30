import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Drop the old table if it exists
cursor.execute('DROP TABLE IF EXISTS survey_responses')

# Recreate the table with the updated schema
cursor.execute('''
CREATE TABLE survey_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    favorite_cuisine TEXT,
    dietary_restrictions TEXT,
    favorite_food TEXT,
    least_favorite_food TEXT,
    ingredients_on_hand TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()
print("Recreated survey_responses table with updated schema.")
