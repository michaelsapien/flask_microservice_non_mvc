from app import create_app

app = create_app()
print("click here: http://127.0.0.1:5000/test")
if __name__ == "__main__":
    app.run(port=5000)
