# User Management System

## Description
This project implements an object-oriented solution for managing user records. It includes three classes:
- **User**: Represents a user with personal details.
- **UserService**: Manages users, allowing adding, updating, and deleting users.
- **UserUtil**: Provides utility functions like generating user IDs, validating emails, and creating secure passwords.

## Features
- Create and manage user profiles
- Generate secure passwords
- Validate email addresses
- Retrieve user details and age
- Maintain a user database using a dictionary

## Classes and Methods

### User Class
| Method | Description |
|--------|-------------|
| `__init__(self, user_id, name, surname, birthday)` | Initializes a user with ID, name, surname, and birthday. Generates email and password automatically. |
| `get_details(self)` | Returns formatted details of the user. |
| `get_age(self)` | Calculates and returns the user's age. |

### UserService Class
| Method | Description |
|--------|-------------|
| `add_user(cls, user)` | Adds a user to the system. |
| `find_user(cls, user_id)` | Finds and returns a user by ID. |
| `delete_user(cls, user_id)` | Deletes a user by ID. |
| `update_user(cls, user_id, user_update)` | Updates user details. |
| `get_number(cls)` | Returns the total number of users. |

### UserUtil Class
| Method | Description |
|--------|-------------|
| `generate_user_id()` | Generates a unique 9-digit user ID. |
| `generate_password()` | Generates a secure password. |
| `is_strong_password(password)` | Checks if a password is strong. |
| `generate_email(name, surname, domain)` | Generates an email address. |
| `validate_email(email)` | Validates an email format. |

## Installation and Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/user-management.git
   cd user-management
   ```
2. Run the script:
   ```bash
   python user_management.py
   ```

## Sample Run
```python
import datetime

birthday = datetime.date(1998, 5, 14)
user = User(UserUtil.generate_user_id(), "John", "Doe", birthday)
UserService.add_user(user)
print(user.get_details())
print("Age:", user.get_age())
print("Valid email:", UserUtil.validate_email(user.email))
```
### Output:
```
User ID: 241234567, Name: John Doe, Email: john.doe@example.com, Birthday: 1998-05-14
Age: 26
Valid email: True
```
