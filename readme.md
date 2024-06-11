# Social Networking API

## Installation Steps

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
3. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the migrations:

   ```bash
   python manage.py migrate
   ```
5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:

   ```bash
   python manage.py runserver
   ```
7. Use Docker (optional):

   ```bash
   docker-compose up --build
   ```

## API Endpoints

- `POST /auth/users/` - Sign up
- `POST /auth/jwt/create/` - Login
- `GET /users/search/?q=<keyword>` - Search users by email or name
- `POST /users/friend-request/send/<user_id>/` - Send friend request
- `POST /users/friend-request/accept/<request_id>/` - Accept friend request
- `POST /users/friend-request/reject/<request_id>/` - Reject friend request
- `GET /users/friends/` - List friends
- `GET /users/friend-requests/` - List pending friend requests
