from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips


def des():

    # 读取视频文件
    video_path = "./ff.mp4"  # 替换为你的视频文件路径
    video = VideoFileClip(video_path)

    # 读取固定图片
    image_path = "./ddd.png"  # 替换为你的图片文件路径
    image = ImageClip(image_path)

    # 创建固定图片的视频片段（15帧）
    image_duration = 0.5  # 固定图片持续时间为0.5秒
    image_clip = ImageClip(image_path).set_duration(image_duration)

    # 将固定图片视频片段与原视频拼接
    final_clip = concatenate_videoclips([image_clip, video.subclip(image_duration)])

    # 保存拼接后的视频
    output_path = "path_to_output_video.mp4"  # 替换为你想要保存的视频文件路径
    final_clip.write_videofile(output_path, codec="libx264", fps=video.fps)


if __name__ == "__main__":
    des()
