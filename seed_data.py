# seed_data.py
# Project folder (jahan main.py hai) se chalayein:
#     uv run python seed_data.py
#
# 15 plays ke reviews database mein daalta hai.
# Agar koi play pehle se maujood ho to usay dobara nahi daalta (duplicate nahi banega).

from datetime import datetime, timedelta, timezone

from sqlmodel import Session, select

from src.db.engine import create_tables, engine
from src.models.model import Review

# (play_name, review_name, rating, comment)
SEED_REVIEWS = [
    ("Hamlet", "Ayesha Khan", 5, "Shandar performance, especially the 'To be or not to be' scene."),
    ("Macbeth", "Hamza Ali", 4, "Dark and gripping. The witches' scenes were haunting."),
    ("Othello", "Sara Ahmed", 5, "Iago's manipulation was chilling, and the acting felt very real."),
    ("Romeo and Juliet", "Fatima Noor", 4, "A beautiful love story with a heartbreaking ending."),
    ("A Midsummer Night's Dream", "Bilal Raza", 5, "Funny, colourful and full of energy. The whole family enjoyed it."),
    ("The Tempest", "Zainab Malik", 4, "Magical stage design, and Prospero's final speech was moving."),
    ("Julius Caesar", "Usman Tariq", 3, "Good political drama, but the middle part felt a bit slow."),
    ("Much Ado About Nothing", "Hira Siddiqui", 5, "Beatrice and Benedick's banter was the highlight. Loved it."),
    ("Death of a Salesman", "Kamran Shah", 5, "Emotional and relatable. Willy Loman's story stays with you."),
    ("A Doll's House", "Mariam Qureshi", 4, "Strong message and a powerful ending. Nora's role was excellent."),
    ("Waiting for Godot", "Danish Iqbal", 3, "Very different and thought-provoking, though not for everyone."),
    ("Pygmalion", "Rabia Anwar", 4, "Witty dialogues and great chemistry between the two leads."),
    ("The Importance of Being Earnest", "Faisal Mehmood", 5, "Hilarious from start to end. The audience laughed the whole time."),
    ("Antigone", "Nimra Javed", 4, "Serious and powerful. Antigone's courage really stood out."),
    ("Oedipus Rex", "Saad Hussain", 5, "A masterpiece of tragedy. The final scene gave me goosebumps."),
]


def seed():
    create_tables()
    base_time = datetime.now(timezone.utc)
    added = 0
    skipped = 0

    with Session(engine) as session:
        for i, (play, reviewer, rating, comment) in enumerate(SEED_REVIEWS):
            exists = session.exec(
                select(Review).where(Review.play_name == play)
            ).first()
            if exists:
                skipped += 1
                continue

            session.add(
                Review(
                    play_name=play,
                    review_name=reviewer,
                    rating=rating,
                    comment=comment,
                    created_at=base_time - timedelta(days=len(SEED_REVIEWS) - i),
                )
            )
            added += 1

        session.commit()

    print(f"Done: {added} reviews added, {skipped} skipped (already exist).")


if __name__ == "__main__":
    seed()