try:
    file = open("app.py")
    file.close()
except:
    print("File not found")