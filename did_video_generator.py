import requests
import time

DID_API_KEY = "YOUR_DID_API_KEY"  # Replace with your actual D-ID API key
DID_API_URL = "https://api.d-id.com/talks"

def create_did_video(text, output_filename="did_video.mp4"):
    headers = {
        "Authorization": f"Bearer {DID_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "script": {"type": "text", "input": text},
        "driver_url": "https://media.did.com/avatars/demo_driver.mp4",
        "output_format": "mp4"
    }

    response = requests.post(DID_API_URL, json=payload, headers=headers)
    if response.status_code != 200:
        print("Failed to create D-ID video:", response.text)
        return None

    video_id = response.json()["id"]

    status_url = f"{DID_API_URL}/{video_id}/status"
    while True:
        status_resp = requests.get(status_url, headers=headers)
        status = status_resp.json()["status"]
        if status == "done":
            video_url = status_resp.json()["result_url"]
            break
        elif status == "failed":
            print("D-ID video generation failed")
            return None
        time.sleep(5)

    video_data = requests.get(video_url)
    with open(output_filename, "wb") as f:
        f.write(video_data.content)

    print(f"Video saved as {output_filename}")
    return output_filename
