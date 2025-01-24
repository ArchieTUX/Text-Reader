# Text Reader App

**Text Reader** is a simple and user-friendly web app that converts text into speech. It allows users to enter any text and have it read aloud with adjustable reading speeds. Built using **Streamlit** and **gTTS (Google Text-to-Speech)**, this app offers an interactive experience suitable for various use cases like language learning, accessibility, and productivity.

### Features:
- **Text-to-Speech**: Convert any text into speech.
- **Adjustable Reading Speed**: Control how fast or slow the text is read aloud.
- **Clean and Simple UI**: Focuses on ease of use with a sleek design.
- **Web Compatible**: Built with **Streamlit**, making it easy to run locally or deploy online.

---

## Requirements:
Before you can run this app locally, make sure you have Python installed on your machine. You’ll also need to install the required Python libraries.

### Steps to Run Locally:

1. **Clone the Repository**:
   Open your terminal and run the following command to clone the repository:

   ```bash
   
   
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:
   Create a virtual environment to keep your dependencies isolated:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install the Dependencies**:
   Use the following command to install the necessary libraries from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the App**:
   Now, you’re ready to launch the app! Run the following command to start the Streamlit server:

   ```bash
   streamlit run TextReader.py
   ```

   This will open a new tab in your browser with the Text Reader app running locally.

---

## How It Works:
1. **Input Text**: Type or paste the text you want to be read aloud into the provided text box.
2. **Adjust Reading Speed**: Use the slider to set the desired reading speed.
3. **Click "Read Aloud"**: Press the "Read Aloud" button to hear the text spoken out loud with the chosen settings.
4. **Enjoy**: Listen to your text being read aloud! You can adjust the speed and re-trigger the speech as needed.

---

## Technologies Used:
- **Streamlit**: Framework for building the app's frontend interface.
- **gTTS (Google Text-to-Speech)**: A library to convert text to speech.
  
---

## Contributions:
Feel free to open issues or submit pull requests if you'd like to contribute to the project. You can also suggest improvements, bug fixes, or new features.

---

## License:
This project is open-source and available under the [MIT License](LICENSE).

---

**Happy Listening!** 🎧

---

