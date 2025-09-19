# 🪨📄✂️ Rock-Paper-Scissors Image Recognition Model

This project is a **real-time image classification model** that predicts whether an image shows **Rock, Paper, or Scissors**. Users can upload their own images, and the model displays the **predicted class** along with a **confidence score**.

---

## 🛠️ Tech Stack

- **Backend:** Python
- **Machine Learning:** TensorFlow, Keras, NumPy, Pillow (PIL)
- **Web Framework:** Streamlit
- **Version Control:** Git & GitHub

---

## 💿 Dataset

This project uses the **Rock, Paper, Scissors Dataset** provided by TensorFlow Datasets. It contains 2,892 diverse images of hand gestures.

---

## ⚙️ Local Setup & Installation

Follow these steps to run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Ashik-Pareeth/rock-paper-scissors-image-classifier.git](https://github.com/Ashik-Pareeth/rock-paper-image-classifier.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows
    venv\Scripts\activate

    # Activate on Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

---

## 🚀 Usage

1.  Once the application launches in your browser, click on the "**Browse files**" button.
2.  Upload a **JPG, JPEG, or PNG** image of a hand gesture.
3.  The model will immediately display the prediction (**Rock, Paper, or Scissors**) and its confidence score.
