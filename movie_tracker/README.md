# Movie & Series Tracker

A CLI to keep a personal log of the movies and series you watch, backed
by a local SQLite database (`tracker.db`, created automatically on first
run and ignored by git).

## Usage

```bash
cd movie_tracker

# Add entries
python tracker.py add "Breaking Bad" series --status watching --season 1 --episode 3 --total-episodes 62
python tracker.py add "Inception" movie --status completed --rating 9

# List entries
python tracker.py list
python tracker.py list --status watching
python tracker.py list --type series --sort rating

# Show full details for one entry
python tracker.py show 1

# Update progress, rating, status, or notes
python tracker.py update 1 --episode 4 --rating 8

# Delete an entry
python tracker.py delete 2

# Summary statistics
python tracker.py stats
```

## Fields

- `type`: `movie` or `series`
- `status`: `plan_to_watch`, `watching`, `completed`, `dropped`
- `rating`: 1-10 (optional)
- `current_season` / `current_episode` / `total_episodes`: progress tracking for series
- `notes`: free text (optional)

## Next steps (ideas)

- Web UI (Flask/Streamlit) on top of the same SQLite data
- Auto-fill metadata (poster, genre, episode counts) from a movie API like TMDb
- Recommendations based on genre/rating history
