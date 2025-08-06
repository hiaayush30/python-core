from pymongo import MongoClient
from bson import ObjectId

# client = MongoClient("mongodb://localhost:27017/yt-manager")
# or
client = MongoClient("mongodb://localhost:27017/", tlsAllowInvalidCertificates=True) # mot a good way to handle ssl
db = client["yt-manager"]
video_collection = db["videos"]
print(video_collection)


def list_all_videos():
    # cursor.execute("SELECT * FROM Videos")
    videos = video_collection.find()
    # print(videos)
    print("*"*70)
    for vid in videos:
        print(f"id:{vid["_id"]}\t{vid["name"]} ({vid["duration"]} mins)")
    print("*"*70)

def add_video():
    name = input("Enter video name: ")
    duration = input("Enter duration in minutes: ")
    vid = video_collection.insert_one({
        "name":name,
        "duration":duration
    })
    # print(vid)
    print("video added!")

def update_video():
    list_all_videos()
    id = input("Enter video id to update: ")
    updated_name = input("Enter updated name: ")
    updated_time = input("Enter updated duration: ")
    video_collection.update_one({"_id":ObjectId(id)},{
        "$set":{
            "name":updated_name,
            "duration":updated_time
        }
    })
    print("Video details updated!")

def delete_video():
    list_all_videos()
    id = input("Enter video id to delete: ")
    video_collection.delete_one({"_id":ObjectId(id)}) # need to explicitly convert to object id here
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
                exit()
            case _:
                print("Invalid Choice")
                continue
            
          
if __name__ == "__main__":
    main()