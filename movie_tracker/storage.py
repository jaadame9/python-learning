"""SQLite storage layer for the movie/series tracker."""

import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "tracker.db"

STATUSES = ("plan_to_watch", "watching", "completed", "dropped")
TYPES = ("movie", "series")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            type TEXT NOT NULL CHECK(type IN ('movie', 'series')),
            status TEXT NOT NULL CHECK(status IN ('plan_to_watch', 'watching', 'completed', 'dropped')),
            rating INTEGER CHECK(rating BETWEEN 1 AND 10),
            current_season INTEGER,
            current_episode INTEGER,
            total_episodes INTEGER,
            notes TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def add_entry(title, type_, status, rating=None, current_season=None,
              current_episode=None, total_episodes=None, notes=None):
    now = datetime.now().isoformat(timespec="seconds")
    conn = get_connection()
    cursor = conn.execute(
        """
        INSERT INTO entries (
            title, type, status, rating, current_season,
            current_episode, total_episodes, notes, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (title, type_, status, rating, current_season,
         current_episode, total_episodes, notes, now, now),
    )
    conn.commit()
    entry_id = cursor.lastrowid
    conn.close()
    return entry_id


def list_entries(type_=None, status=None, sort_by="title"):
    conn = get_connection()
    query = "SELECT * FROM entries"
    conditions = []
    params = []
    if type_:
        conditions.append("type = ?")
        params.append(type_)
    if status:
        conditions.append("status = ?")
        params.append(status)
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    if sort_by in ("title", "rating", "created_at", "updated_at", "status", "type"):
        query += f" ORDER BY {sort_by}"
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return rows


def get_entry(entry_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM entries WHERE id = ?", (entry_id,)).fetchone()
    conn.close()
    return row


def update_entry(entry_id, **fields):
    if not fields:
        return False
    fields["updated_at"] = datetime.now().isoformat(timespec="seconds")
    columns = ", ".join(f"{key} = ?" for key in fields)
    values = list(fields.values()) + [entry_id]
    conn = get_connection()
    cursor = conn.execute(f"UPDATE entries SET {columns} WHERE id = ?", values)
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated


def delete_entry(entry_id):
    conn = get_connection()
    cursor = conn.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted


def get_stats():
    conn = get_connection()
    total = conn.execute("SELECT COUNT(*) FROM entries").fetchone()[0]
    by_status = conn.execute(
        "SELECT status, COUNT(*) as count FROM entries GROUP BY status"
    ).fetchall()
    by_type = conn.execute(
        "SELECT type, COUNT(*) as count FROM entries GROUP BY type"
    ).fetchall()
    avg_rating = conn.execute(
        "SELECT AVG(rating) FROM entries WHERE rating IS NOT NULL"
    ).fetchone()[0]
    conn.close()
    return {
        "total": total,
        "by_status": {row["status"]: row["count"] for row in by_status},
        "by_type": {row["type"]: row["count"] for row in by_type},
        "avg_rating": round(avg_rating, 2) if avg_rating is not None else None,
    }
