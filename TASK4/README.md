# 🎬 Movie Recommendation System

A simple AI-powered **Movie Recommendation System** developed using **Python** and **Machine Learning**. This project recommends movies to users based on content similarity by analyzing movie genres and calculating similarity scores using Natural Language Processing (NLP) techniques.

This project was completed as **Task 4** of the **CODSOFT AI Internship**.

---

## 📌 Project Overview

Recommendation systems are widely used in platforms like Netflix, Amazon, and Spotify to provide personalized suggestions. This project implements a **Content-Based Filtering** approach that recommends movies similar to the movie selected by the user.

The system converts movie genres into numerical vectors and computes similarity between movies using **Cosine Similarity**.

---

## 🚀 Features

* Recommend movies based on user preferences
* Content-Based Filtering approach
* Genre-based similarity matching
* Fast and lightweight implementation
* Beginner-friendly Machine Learning project
* Command-line interface for easy interaction

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* CountVectorizer
* Cosine Similarity

---

## 📂 Project Structure

```text
TASK4/
│
├── recommendation_system.py
├── movies.csv
└── README.md
```
---

## ▶️ How to Run

Run the following command:

```bash
python recommendation_system.py
```

Enter a movie name when prompted:

```text
Enter Movie Name: Avatar
```

---

## 📊 Sample Output

```text
Enter Movie Name: Avatar

Recommended movies for 'Avatar':

Doctor Strange
Interstellar
The Avengers
Iron Man
Inception
```

---

## 🧠 Working Principle

1. Load the movie dataset.
2. Extract genre information from each movie.
3. Convert text data into numerical vectors using CountVectorizer.
4. Calculate similarity scores using Cosine Similarity.
5. Recommend the most similar movies based on the user's input.

---

## 📈 Future Enhancements

* Add a larger movie dataset
* Build a graphical user interface (GUI)
* Develop a web application using Streamlit
* Include movie ratings and reviews
* Implement Collaborative Filtering
* Add recommendation confidence scores

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Recommendation System Fundamentals
* Content-Based Filtering
* Natural Language Processing Basics
* Feature Extraction Techniques
* Similarity Measurement Methods
* Machine Learning Workflow

---

## 🤝 Acknowledgements

This project was developed as part of the **CODSOFT AI Internship Program**, providing hands-on experience in Artificial Intelligence and Machine Learning concepts.

---

⭐ If you found this project useful, consider giving it a star on GitHub!
