"""CLI for tracking movies and series you watch.

Usage examples:
    python tracker.py add "Breaking Bad" series --status watching --season 1 --episode 3
    python tracker.py list --status watching
    python tracker.py update 1 --episode 4 --rating 9
    python tracker.py show 1
    python tracker.py delete 1
    python tracker.py stats
"""

import argparse
import sys

import storage


def cmd_add(args):
    entry_id = storage.add_entry(
        title=args.title,
        type_=args.type,
        status=args.status,
        rating=args.rating,
        current_season=args.season,
        current_episode=args.episode,
        total_episodes=args.total_episodes,
        notes=args.notes,
    )
    print(f"Added '{args.title}' (id={entry_id})")


def cmd_list(args):
    entries = storage.list_entries(type_=args.type, status=args.status, sort_by=args.sort)
    if not entries:
        print("No entries found.")
        return
    for entry in entries:
        print(_format_entry_line(entry))


def cmd_show(args):
    entry = storage.get_entry(args.id)
    if entry is None:
        print(f"No entry with id={args.id}", file=sys.stderr)
        sys.exit(1)
    for key in entry.keys():
        print(f"{key}: {entry[key]}")


def cmd_update(args):
    fields = {}
    if args.status is not None:
        fields["status"] = args.status
    if args.rating is not None:
        fields["rating"] = args.rating
    if args.season is not None:
        fields["current_season"] = args.season
    if args.episode is not None:
        fields["current_episode"] = args.episode
    if args.total_episodes is not None:
        fields["total_episodes"] = args.total_episodes
    if args.notes is not None:
        fields["notes"] = args.notes

    if not fields:
        print("Nothing to update. Provide at least one field.", file=sys.stderr)
        sys.exit(1)

    updated = storage.update_entry(args.id, **fields)
    if not updated:
        print(f"No entry with id={args.id}", file=sys.stderr)
        sys.exit(1)
    print(f"Updated entry id={args.id}")


def cmd_delete(args):
    deleted = storage.delete_entry(args.id)
    if not deleted:
        print(f"No entry with id={args.id}", file=sys.stderr)
        sys.exit(1)
    print(f"Deleted entry id={args.id}")


def cmd_stats(args):
    stats = storage.get_stats()
    print(f"Total entries: {stats['total']}")
    print(f"Average rating: {stats['avg_rating']}")
    print("By status:")
    for status in storage.STATUSES:
        print(f"  {status}: {stats['by_status'].get(status, 0)}")
    print("By type:")
    for type_ in storage.TYPES:
        print(f"  {type_}: {stats['by_type'].get(type_, 0)}")


def _format_entry_line(entry):
    progress = ""
    if entry["type"] == "series" and (entry["current_season"] or entry["current_episode"]):
        season = entry["current_season"] or "?"
        episode = entry["current_episode"] or "?"
        total = f"/{entry['total_episodes']}" if entry["total_episodes"] else ""
        progress = f" [S{season}E{episode}{total}]"
    rating = f" ({entry['rating']}/10)" if entry["rating"] is not None else ""
    return f"#{entry['id']} {entry['title']} - {entry['type']}/{entry['status']}{progress}{rating}"


def build_parser():
    parser = argparse.ArgumentParser(description="Track the movies and series you watch.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new entry")
    add_parser.add_argument("title")
    add_parser.add_argument("type", choices=storage.TYPES)
    add_parser.add_argument("--status", choices=storage.STATUSES, default="plan_to_watch")
    add_parser.add_argument("--rating", type=int)
    add_parser.add_argument("--season", type=int)
    add_parser.add_argument("--episode", type=int)
    add_parser.add_argument("--total-episodes", type=int, dest="total_episodes")
    add_parser.add_argument("--notes")
    add_parser.set_defaults(func=cmd_add)

    list_parser = subparsers.add_parser("list", help="List entries")
    list_parser.add_argument("--type", choices=storage.TYPES)
    list_parser.add_argument("--status", choices=storage.STATUSES)
    list_parser.add_argument(
        "--sort", choices=["title", "rating", "created_at", "updated_at", "status", "type"],
        default="title",
    )
    list_parser.set_defaults(func=cmd_list)

    show_parser = subparsers.add_parser("show", help="Show full details for one entry")
    show_parser.add_argument("id", type=int)
    show_parser.set_defaults(func=cmd_show)

    update_parser = subparsers.add_parser("update", help="Update an entry")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("--status", choices=storage.STATUSES)
    update_parser.add_argument("--rating", type=int)
    update_parser.add_argument("--season", type=int)
    update_parser.add_argument("--episode", type=int)
    update_parser.add_argument("--total-episodes", type=int, dest="total_episodes")
    update_parser.add_argument("--notes")
    update_parser.set_defaults(func=cmd_update)

    delete_parser = subparsers.add_parser("delete", help="Delete an entry")
    delete_parser.add_argument("id", type=int)
    delete_parser.set_defaults(func=cmd_delete)

    stats_parser = subparsers.add_parser("stats", help="Show summary statistics")
    stats_parser.set_defaults(func=cmd_stats)

    return parser


def main():
    storage.init_db()
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
