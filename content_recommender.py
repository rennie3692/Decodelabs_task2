"""Simple movie recommendation system using preference matching."""

from typing import List, Dict, Set


def get_user_preferences() -> Set[str]:
    """Prompt the user for their interests and return normalized tags."""
    raw_input = input("Enter your interests (comma-separated, e.g. action, comedy, sci-fi): ")
    # Split the input on commas, strip whitespace, and convert to lowercase.
    preferences = {pref.strip().lower() for pref in raw_input.split(",") if pref.strip()}
    return preferences


def compute_scores(preferences: Set[str], catalog: List[Dict[str, object]]) -> List[Dict[str, object]]:
    """Compute a score for each catalog item based on overlapping tags."""
    matched_items = []
    for item in catalog:
        item_tags = {tag.lower() for tag in item.get("tags", [])}
        score = len(preferences & item_tags)
        if score > 0:
            matched_items.append({
                "title": item.get("title", "Untitled"),
                "description": item.get("description", "No description available."),
                "score": score,
            })
    # Sort descending by score.
    matched_items.sort(key=lambda x: x["score"], reverse=True)
    return matched_items


def display_recommendations(recommendations: List[Dict[str, object]]) -> None:
    """Display the top 3-5 matched items clearly."""
    if not recommendations:
        print("No matches found. Try different interests!")
        return

    print("\nYour top recommendations:")
    top_recommendations = recommendations[:5]
    for index, item in enumerate(top_recommendations, start=1):
        title = item["title"]
        score = item["score"]
        description = item["description"]
        print(f"{index}. {title} (score: {score}) — {description}")


def main() -> None:
    """Main function to prompt the user once and show recommendations."""
    movie_catalog = [
        {
            "title": "Interstellar",
            "tags": ["sci-fi", "adventure", "drama", "space"],
            "description": "A mind-bending journey through space and time.",
        },
        {
            "title": "The Martian",
            "tags": ["sci-fi", "drama", "survival", "space"],
            "description": "An astronaut stranded on Mars fights to survive.",
        },
        {
            "title": "The Grand Budapest Hotel",
            "tags": ["comedy", "drama", "adventure"],
            "description": "A quirky story of a legendary hotel concierge and his friend.",
        },
        {
            "title": "Mad Max: Fury Road",
            "tags": ["action", "adventure", "thriller", "post-apocalyptic"],
            "description": "A high-octane chase across a desert wasteland.",
        },
        {
            "title": "The Shawshank Redemption",
            "tags": ["drama", "friendship", "prison"],
            "description": "Two imprisoned men bond over years and find hope.",
        },
        {
            "title": "Guardians of the Galaxy",
            "tags": ["action", "comedy", "sci-fi", "space"],
            "description": "A group of unlikely heroes must save the galaxy.",
        },
        {
            "title": "Inception",
            "tags": ["sci-fi", "thriller", "action", "mind-bending"],
            "description": "A team enters dreams to plant an idea.",
        },
        {
            "title": "Pride and Prejudice",
            "tags": ["romance", "drama", "period"],
            "description": "A classic love story in early 19th-century England.",
        },
        {
            "title": "The Dark Knight",
            "tags": ["action", "crime", "thriller", "superhero"],
            "description": "Batman faces a criminal mastermind in Gotham City.",
        },
        {
            "title": "Finding Nemo",
            "tags": ["animation", "family", "adventure", "comedy"],
            "description": "A father fish searches for his lost son in the ocean.",
        },
    ]

    preferences = get_user_preferences()
    if not preferences:
        print("Please enter at least one interest.")
        return

    recommendations = compute_scores(preferences, movie_catalog)
    display_recommendations(recommendations)


if __name__ == "__main__":
    main()
