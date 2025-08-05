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
    print("*"*70)
    if len(videos) == 0:
        return print("No videos found!")
    for index,video in enumerate(videos,start=1):
        # takes a list returns  (enumerate object) indexing along with each object ex (1, {'name': 'Lagaan', 'duration': '300'})
        print(f"{index}. {video["name"]} ({video["duration"]} mins)")  
    print("*"*70)

def add_video(videos):
    name = input("Enter video name: ")
    duration = input("Enter duration in minutes: ")
    videos.append({"name":name,"duration":duration})
    save_data_helper(videos)
    print("video added!")

def update_video(videos):
    list_all_videos(videos)
    id = int(input("Enter video no. to update: "))
    if id > len(videos) or id < 1:
        print("Invalid id")
    else:
       updated_name = input("Enter updated name: ")
       updated_duration = input("Enter updated duration: ")
    videos[id-1] = {
        "name":updated_name,
        "duration":updated_duration
    }
    save_data_helper(videos)
    print("Video details updated!")

def delete_video(videos):
    list_all_videos(videos)
    id = int(input("Enter video no. to delete: "))
    if id > len(videos) or id < 1:
        print("Invalid id")
    else:
      del videos[id-1]
    save_data_helper(videos)
    print("Video deleted!")

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