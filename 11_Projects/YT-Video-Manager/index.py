import json

def load_data():
   try:
       with open("youtube.txt","r") as file:
           return json.load(file)
   except FileNotFoundError:
       print("file not found")
       return []

def save_data_helper(videos):
       with open("youtube.txt","w") as file: 
           json.dump(videos,file)

def list_all_videos(videos):
    print("\t All Videos")
    if len(videos) == 0:
        return print("No videos found!")
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video["name"]} ({video["duration"]} mins)")
    print("\n \t \t***")

def add_video(videos):
    name = input("Enter video name: ")
    duration = input("Enter duration in minutes: ")
    videos.append({"name":name,"duration":duration})
    save_data_helper(videos)
    print("video added!")

def update_video(videos):
    list_all_videos(videos)
    id = input("Enter video id: ")

def delete_video(videos):
    pass

def main():
    videos = load_data()
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
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting app")
                exit()
            case _:
                print("Invalid Choice")
                continue
            
          
if __name__ == "__main__":
    main()