# Contact Book

A web-based contact manager built with Flask and SQLite.

## Features

- View all contacts
- Add new contacts
- Search contacts by name
- Delete contacts by ID

## Tech Stack

- Python 3.11+
- Flask
- SQLite3

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

## Project Structure

```
contact_book/
├── models/
│   └── contact.py      # Contact class + database operations
├── templates/
│   ├── base.html        # Shared layout
│   ├── index.html       # All contacts
│   ├── add.html         # Add contact form
│   ├── search.html      # Search form + results
│   └── delete.html      # Delete by ID
├── app.py               # Flask routes
├── database.py          # DB init
└── requirements.txt
```
