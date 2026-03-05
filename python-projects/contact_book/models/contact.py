import sqlite3

DB_PATH = "contacts.db"


class Contact:
    """Represents a single contact and handles all database operations."""

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    def save(self) -> None:
        """Insert this contact into the database."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
            (self.name, self.phone, self.email),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_all() -> list:
        """Return all contacts from the database."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts ORDER BY name ASC")
        contacts = cursor.fetchall()
        conn.close()
        return contacts

    @staticmethod
    def delete_contact(id: int) -> None:
        """Delete a contact by ID."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def search(query: str) -> list:
        """Search contacts by name (case-insensitive partial match)."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM contacts WHERE name LIKE ? ORDER BY name ASC",
            (f"%{query}%",),
        )
        contacts = cursor.fetchall()
        conn.close()
        return contacts
