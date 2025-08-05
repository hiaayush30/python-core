import sqlite3

conn = sqlite3.connect("yt_videos.db")
cursor = conn.cursor()
cursor.execute('''
      CREATE TABLE IF NOT EXISTS Videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL         
    )
    ''')

def list_all_videos():
    cursor.execute("SELECT * FROM Videos")
    videos = cursor.fetchall()
    print("*"*70)
    if len(videos) == 0:
        print("No videos found!")
    for vid in videos:
        print(vid)
    print("*"*70)

def add_video():
    name = input("Enter video name: ")
    duration = input("Enter duration in minutes: ")
    cursor.execute("INSERT INTO Videos(name,time) VALUES (?,?)",(name,duration))
    conn.commit()
    print("video added!")

def update_video():
    list_all_videos()
    id = int(input("Enter video id to update: "))
    updated_name = input("Enter updated name: ")
    updated_time = input("Enter updated duration: ")
    cursor.execute("UPDATE Videos SET name = ?, time = ? WHERE id = ?",(updated_name,updated_time,id))
    conn.commit()
    print("Video details updated!")

def delete_video():
    list_all_videos()
    id = int(input("Enter video id to delete: "))
    cursor.execute("DELETE FROM Videos WHERE id = ?",(id,))
    conn.commit()
    print("Video deleted!")

def main():
    while True:
        print("\t Youtube Manager")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video's details")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                print("Exiting app")
                conn.close()
                exit()
            case _:
                print("Invalid Choice")
                continue
            
          
if __name__ == "__main__":
    main()