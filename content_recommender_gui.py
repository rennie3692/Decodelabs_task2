import tkinter as tk
from tkinter import ttk
from content_recommender import compute_scores


def parse_preferences(raw_text: str):
    """Normalize the user's comma-separated preferences."""
    return {pref.strip().lower() for pref in raw_text.split(",") if pref.strip()}


MOVIE_CATALOG = [
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


class RecommenderGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Movie Recommendation System")
        self.geometry("560x420")
        self.resizable(False, False)

        header = ttk.Label(self, text="Movie Recommender", font=("Arial", 18, "bold"))
        header.pack(pady=(12, 6))

        instruction = ttk.Label(
            self,
            text="Enter your interests (comma-separated): action, comedy, sci-fi, drama, space",
            wraplength=520,
        )
        instruction.pack(padx=12)

        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(padx=12, pady=(10, 0), fill=tk.X)

        self.preference_entry = ttk.Entry(self.input_frame, font=("Arial", 12))
        self.preference_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.preference_entry.bind("<Return>", self.on_recommend)

        recommend_button = ttk.Button(self.input_frame, text="Recommend", command=self.on_recommend)
        recommend_button.pack(side=tk.LEFT, padx=(8, 0))

        self.output_text = tk.Text(self, wrap=tk.WORD, height=14, width=64, font=("Arial", 11), state=tk.DISABLED)
        self.output_text.pack(padx=12, pady=12)

        self.clear_button = ttk.Button(self, text="Clear", command=self.clear_output)
        self.clear_button.pack(pady=(0, 10))

        self.show_message("Type your interests and click Recommend to see movie suggestions.")

    def show_message(self, message: str) -> None:
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, message)
        self.output_text.configure(state=tk.DISABLED)

    def clear_output(self) -> None:
        self.preference_entry.delete(0, tk.END)
        self.show_message("Type your interests and click Recommend to see movie suggestions.")

    def on_recommend(self, event=None) -> None:
        raw_text = self.preference_entry.get()
        preferences = parse_preferences(raw_text)

        if not preferences:
            self.show_message("Please enter at least one interest before requesting recommendations.")
            return

        results = compute_scores(preferences, MOVIE_CATALOG)
        self.display_results(results)

    def display_results(self, results):
        if not results:
            self.show_message("No matches found. Try different interests!")
            return

        lines = ["Your top recommendations:\n"]
        for index, item in enumerate(results[:5], start=1):
            lines.append(f"{index}. {item['title']} (score: {item['score']}) - {item['description']}")

        self.show_message("\n".join(lines))


if __name__ == "__main__":
    app = RecommenderGUI()
    app.mainloop()
