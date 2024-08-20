https://github.com/user-attachments/assets/7820211a-7b9b-4b51-be26-592997f488c4 

### **Documentation for Plant Leaf Disease Classification**

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Directory Structure](#directory-structure)
3. [Setup Instructions](#setup-instructions)
   - [1. Install Prerequisites](#1-install-prerequisites)
   - [2. Setup Virtual Environment](#2-setup-virtual-environment)
4. [How to Run the Project](#how-to-run-the-project)
5. [Deployment](#Deployment)
6. [Contributing](#contributing)
7. [License](#license)

---

## Project Overview

This project involved developing a web application to identify diseases on plant leaves through image classification using Convolutional Neural Networks (CNN). Utilized TensorFlow for model building, incorporating data augmentation and tf.data pipelines to enhance performance. Integrated TensorFlow Serving for efficient model inference with a Flask backend, and deployed the application on Render. The project aims to reduce agricultural losses by providing accurate and timely disease detection.

---

## Directory Structure

The project directory is organized as follows:

```
/project-directory
    ├── models/
    ├── plantVillage/
    ├── static/
    ├── templates/
    ├── app.py
    ├── app.py
    ├── requirements.txt
    └── training.ipynb
```

- **`models/`**: Contains the saved model files.
- **`plantVillage/`**: Contains the Dataset.
- **`static/`**: Stores the static files which is requirement for flask app.
- **`templates/`**: Contains the HTML file templates to render while execution of the flask app.
- **`app.py`**: Flask app.py file.
- **`requirements.txt`**: Lists all the dependencies required for the project.
- **`training.ipynb`**: Jupyter notebook file.

---

## Setup Instructions

### 1. Install Prerequisites
Ensure you have Python 3.7 or later installed on your system. You can check your Python version by running:

```bash
python3 --version
```

### 2. Setup Virtual Environment

1. **Clone the Repository**:
   If you haven't already, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd project-directory
   ```

2. **Run the Setup Script**:
`python3 -m venv venv`
`pip install -r requirements.txt`
   - Install the required Python packages listed in `requirements.txt`.

3. **Activate the Virtual Environment**:
   To start working with the project, activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

   To deactivate the environment, simply run:

   ```bash
   deactivate
   ```

---

## How to Run the Project

Once the setup is complete, you can run the main script to process queries:

```bash
python app.py
```

This will execute the script, which will:
- Loads the model into flask app .
- User will upload the image for Prediction.
- Model Predicts the class which the plant leaves disease belongs to and displays it on the flask app.

---

## Deployment

For deployment instructions, refer to [Render Deployment Guide](https://render.com/docs/deploy-flask).

## Contributing

Feel free to submit issues or pull requests to contribute to the project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This documentation provides an overview of the project structure, setup instructions, and a breakdown of each module. It should help both you and others understand and use the project efficiently.
