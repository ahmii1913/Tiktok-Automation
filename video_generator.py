from moviepy.editor import TextClip, CompositeVideoClip, ColorClip

def add_watermark(clip, username):
    watermark = TextClip(f"@{username}", fontsize=40, color='white')
    watermark = watermark.set_duration(clip.duration)
    watermark = watermark.set_position(("left", "bottom")).margin(left=10, bottom=10)
    return watermark

def generate_simple_video(text, output_path="output.mp4", username="yourname"):
    bg = ColorClip(size=(720, 1280), color=(30, 30, 30), duration=10)
    txt = TextClip(text, fontsize=70, color='white', size=(700, None), method='caption')
    txt = txt.set_position('center').set_duration(10)
    watermark = add_watermark(bg, username)
    final = CompositeVideoClip([bg, txt, watermark])
    final.write_videofile(output_path, fps=24)
