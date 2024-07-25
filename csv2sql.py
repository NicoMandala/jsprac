import pandas as pd

# Load the CSV file
file_path = 'Synthetic_User_Data.csv'
data = pd.read_csv(file_path)

# Open a file to write the SQL statements
with open('insert_data.sql', 'w') as file:
    for index, row in data.iterrows():
        insert_statement = f"""
        INSERT INTO UserBookReviews (username, book_rating, user_age, book_genre, quote_or_review_text, favorite_authors_or_psychologists)
        VALUES (
            '{row['username']}', 
            {row['book_rating']}, 
            {row['user_age']}, 
            '{row['book_genre']}', 
            "{row['quote_or_review_text'].replace('"', '""')}", 
            '{row['favorite_authors_or_psychologists']}'
        );
        """
        file.write(insert_statement)

print("SQL insert statements have been written to insert_data.sql")
