from user import User
from database import Database

Database.initialise(database="tutorial", user="postgres", password="mJ604998", host="localhost", port=6000)

user = User('mohamad97mj@gmail.com', 'mohamad', 'mojahed')

user.save_to_db()

user_from_db = User.load_from_db_by_email('mohamad97mj@gmail.com')

print(user_from_db)
