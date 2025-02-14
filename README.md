# roadmap-github-user-activity
Use GitHub API to fetch user activity and display it in the terminal.

### Requirements
- The application should
  - run from the command line
  - accept the GitHub username as an argument
  - fetch the user’s recent activity using the GitHub API
  - and display it in the terminal.
- Handle errors gracefully, such as invalid usernames or API failures.
- Use a programming language of your choice to build this project.
- Do not use any external libraries or frameworks to fetch the GitHub activity.

### Tech stack
- python
- `requests` for making http requests

### Setup
```sh
# install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage
- Provide the GitHub username as an argument when running the CLI
```sh
python github-activity.py <username>

# take "firebase" for example
# python github-activity.py firebase
```

- Display the fetched activity in the terminal (example output)
```sh
- Pushed 1 commit to firebase/friendlyeats-web
- Starred firebase/flutterfire
- Pushed 1 commit to firebase/firebase-js-sdk
- Pushed 1 commit to firebase/quickstart-js
- Pushed 1 commit to firebase/quickstart-js
- Pushed 1 commit to firebase/quickstart-js
- Pushed 1 commit to firebase/genkit
- Starred firebase/quickstart-android
```

### Acknowledgement
The project idea is taken from [roadmap.sh](https://roadmap.sh). Roadmaps to help you choose your path and grow in your career.
