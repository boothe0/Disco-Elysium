# Disco Elysium Interactable Page

### Features implemented
- Make account
- Login Authentication
- Rotating images with credits
- Routing to Blog, About and Home
- Various animations
- SQLite3 connected via SQLAlchemy for user information
- Selenium testing updated regularly with modular functions for repeated use cases
- Local debug server for Flask-email



### Features (planned)
- Email newsletter via Flask-email
- Blog post feature that gets updated
- Host on githubpages


### Tech Stack
- Flask
- SQLite3
- SQLAlchemy
- Jinja Templates
- Selenium
- HTML
- Bootstrap CSS
- JS

### Running local flask debug server for flask-email
`pip install aiosmtpd`

`python -m aiosmtpd -n -l localhost:1025` (make sure it is 1025 as that is what is set in main.py as the server to listen on)


![disco_elysium_progress02](https://github.com/user-attachments/assets/23662029-6cc0-4e36-bec5-c3e9124c0758)
