# FlexibleFrameworks

Using flexible templates made by the user to store and retreive noSQL data from the cloud (FireStore). This an example is used to demonstrate dynamic UI to define templates for data storage and retreival

---

### Virtual environment

To use the streamlit app, use the virtual environment along with *Python 3.9*. To create the environment, navigate to the folder of the working directory and use the following command in the command prompt

``` python -m venv <Folder name here> ```

And to activate the environment, navigate through the environment using

```<Folder name>/Scripts```

And type `activate` in the terminal to activate the environment. And `deactivate` to deactivate it when required.

---

### Run Streamlit App

To run the streamlit app simply navigate back to the working directory and run the following commands

```
pip install -r requirements.txt
streamit run main.py
```
# 
---

### Directory Structure

Below is the directory structure of the web app

```
main
├── Readme.md
├── main.py
├── T1.py
├── T2.py
├── T3.py
├── AddButton.py
└── Outcome.py
```

> `main.py` is the main file which navigates across the several pages. It is also where the sidebar is initiated and kept constant throughout the app
---

> `T1.py` and `T2.py` are dummy templates used for testing and creating new templates as when required manually. It contains the basic code for sending and retreiving files from the FireStore server (NoSQL database)
---

> `T3.py` is the template with flexible UI which allows the user to add new input fields when necessary. It is made in conjuction with `AddButton.py` and store all input information in a dictionary with the following structure:
 - `{<input field name> : [<function call>, <field value>]}`
---
 
 > `AddButton.py` acts as a plus button to Template 3 which allows the user to add input fields when necessary and modify the template in real time. Current modification allows user to add either text input or number input.


### Constraints

- The NoSQL database relies on the student number being the Unique identifier to each document (as defined by the user) and therefore requires to input a different student number with every form. (Can be changed with design, constraint to only current program)
- The code also relies on sending and retrieval of data via a private key to its corresponding firestore account. To ensure the code works in your system, create a firestore account and add the `private-key.json` file to the parent directory of the working folder. 

