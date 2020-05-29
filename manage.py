from app import app
import sys

def runserver():
    app.run(host="0.0.0.0", port=8080)

actions = {'run': runserver}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: Option is needed")
    else:
        actions[sys.argv[1]]()