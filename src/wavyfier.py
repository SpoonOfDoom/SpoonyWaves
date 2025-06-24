"""Do the FFmpeg stuff here."""

import ffmpeg


def example_1(input_file: str, output_file: str):
    """
        ❶ Line mode, white color
    → ffmpeg -i input_sample.mp3 -filter_complex "[0:a]showwaves=mode=line:s=1280x720:colors=white[v]" -map "[v]" -map 0:a -pix_fmt yuv420p output01.mp4

    with:

        -i input.mp4 = Reads file «input.mp4» and …
        -filter_complex "[0:a]showwaves = …applies the «showwaves» complex filter to the audio soundtrack «[0:a]»…
        mode=line = … setting the display mode to «line», …
        s=1280x720 = … the output video size to 1280 x 720 and …
        colors=white = … the waveform color to «white», …
        [v] = … calling the resulting video «v» and …
        -map "[v]" -map 0:a = … merges together the generated video «v» and the original audio «0:a» …
        -pix_fmt yuv420p = … sets Pixel format to yuv420p (for compatibility with Windows in my case) and…
        output01.mp4 = … and outputs the result to file «output01.mp4»
        :param input_file:
        :param output_file:
        :return:
    """
    stream = ffmpeg.input(input_file)
    stream = ffmpeg.filter(stream, "showwaves")
    stream = ffmpeg.output(stream, output_file)
    ffmpeg.run(
        stream,
        cmd="ffmpeg",
        overwrite_output=True,
    )


def example_2(input_file: str, output_file: str):
    """
        ❷ Point mode, yellow color, drawing every sample
    → ffmpeg -i input_sample.mp3 -filter_complex "[0:a]showwaves=mode=point:s=hd720:colors=yellow:draw=full:scale=sqrt[v]" -map "[v]" -map 0:a -pix_fmt yuv420p output02.mp4

    with:

        -i input.mp4 = Reads file «input.mp4» and …
        -filter_complex "[0:a]showwaves = …applies the «showwaves» complex filter to the audio soundtrack «[0:a]»…
        mode=point = … setting the display mode to «point», …
        s=hd720 = … the output video size to 1280 x 720 and …
        colors=yellow = … the waveform color to «yellow», …
        draw=full = … setting the draw mode to full (draw every sample),…
        scale=sqrt = … setting the scale to square root (sqrt) and …
        [v] = … calling the resulting video «v» and …
        -map "[v]" -map 0:a = … merges together the generated video «v» and the original audio «0:a» …
        -pix_fmt yuv420p = … sets Pixel format to yuv420p (for compatibility with Windows in my case) and…
        output02.mp4 = … and outputs the result to file «output02.mp4»
        :param input_file:
        :param output_file:
        :return:
    """
    pass


def example_3(input_file: str, output_file: str):
    """
        ❸ Watermark resizing and addition, custom position
    → ffmpeg -i input_sample.mp3 -filter_complex "[0:a]showwaves=mode=p2p:s=hd720:split_channels=1:colors=red|green:draw=full[v]" -map "[v]" -map 0:a -pix_fmt yuv420p output03.mp4
      ffmpeg -i input_sample.mp3 -filter_complex "[0:a]showwaves=mode=p2p:s=hd1080:colors=white:draw=full[v]" -map "[v]" -map 0:a -pix_fmt yuv420p output003.mp4
      ffmpeg -i input_sample.mp3 -filter_complex "[0:a]showwaves=s=1920x1080:mode=cline:n=1024:colors=ffffff:draw=full[v]:rate=25[v]" -map "[v]" -map 0:a -c:v libx264 -r 25 -pix_fmt yuv420p -b:v 1M -c:a aac -shortest waveform.mp4

    with:

        -i input.mp4 = Reads file «input.mp4» and …
        -filter_complex "[0:a]showwaves = …applies the «showwaves» complex filter to the audio soundtrack «[0:a]»…
        mode=p2p = … setting the display mode to «p2p», …
        s=hd720 = … the output video size to 1280 x 720 and …
        split_channels=1 = … splitting the input stereo audio in 2 apart channels, …
        colors=red|green = … setting the colors of the channels to red and green, …
        draw=full = … setting the draw mode to full (draw every sample),…
        [v] = … calling the resulting video «v» and …
        -map "[v]" -map 0:a = … merges together the generated video «v» and the original audio «0:a» …
        -pix_fmt yuv420p = … sets Pixel format to yuv420p (for compatibility with Windows in my case) and…
        output03.mp4 = … and outputs the result to file «output03.mp4»
        :param input_file:
        :param output_file:
        :return:
    """
    pass


def example_4(input_file: str, output_file: str):
    """
        ❹ Cline mode, my favorite
    → ffmpeg -i input_sample.mp3 -filter_complex "[0:a]showwaves=mode=cline:s=hd720:colors=cyan[v]" -map "[v]" -map 0:a -pix_fmt yuv420p output04.mp4

    with:

        -i input.mp4 = Reads file «input.mp4» and …
        -filter_complex "[0:a]showwaves = …applies the «showwaves» complex filter to the audio soundtrack «[0:a]»…
        mode=cline = … setting the display mode to «cline», …
        s=hd720 = … the output video size to 1280 x 720 and …
        colors=cyan = … the waveform color to «cyan», …
        [v] = … calling the resulting video «v» and …
        -map "[v]" -map 0:a = … merges together the generated video «v» and the original audio «0:a» …
        -pix_fmt yuv420p = … sets Pixel format to yuv420p (for compatibility with Windows in my case) and…
        output04.mp4 = … and outputs the result to file «output04.mp4»ꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷ

    → Catch up with the FFMPEG guy Channel
        :param input_file:
        :param output_file:
        :return:
    """
    pass


def simple_waveform(input_file: str, output_file: str):
    """
    Generates a simple waveform visualization.
    :param input_file: Path to the input audio file.
    :param output_file: Path to the output video file.
    :return: None
    """
    stream = ffmpeg.input(input_file)
    stream = ffmpeg.filter(stream, "showwaves", mode="line", s="1280x720", colors="white", draw="line")
    stream = ffmpeg.output(stream, output_file, pix_fmt="yuv420p")
    ffmpeg.run(stream, overwrite_output=True)


def example_5(input_file: str, output_file: str):
    """
    ffmpeg -y -i "input_sample.mp3" -filter_complex "[0:a]showcqt=s=1920x1080:basefreq=30:text=0:axis_h=0:tc=0.7:bar_t=0.2:count=1:gamma2=5:csp=bt709" CLI_output05.mp4
    :param input_file:
    :param output_file:
    :return:
    """
    pass


def my_wave(input_file: str, output_file: str):
    """
    ffmpeg -hwaccel cuda -i input_sample.mp3 -filter_complex "[0:a]showwaves=mode=p2p:s=hd1080:colors=white:draw=full:rate=60[v]" -map "[v]" -map 0:a -pix_fmt yuv420p -r 60 -c:v h264_nvenc output.mp4

    ffmpeg -i input_sample.mp3 -filter_complex "[0:a]showwaves=mode=p2p:s=hd1080:colors=white:draw=full:rate=60[v]" -map "[v]" -map 0:a -pix_fmt yuv420p -r 60 output.mp4
    ffmpeg -i input_sample.mp3 -filter_complex "[0:a]showwaves=mode=p2p:s=hd1080:colors=white:draw=full:rate=60[v]" -map "[v]" -map 0:a -pix_fmt yuv420p -r 60 output.mp4
    :param input_file:
    :param output_file:
    :return:
    """
    stream = ffmpeg.input(input_file, hwaccel="cuda")
    audio = stream.audio
    video = audio.filter("showwaves", mode="p2p", s="hd1080", colors="white", draw="full", rate=60)

    # Combine audio and video streams and set output parameters
    stream = ffmpeg.output(video, audio, output_file, pix_fmt="yuv420p", r=60, vcodec="h264_nvenc")

    # Run the FFmpeg command
    try:
        stream.overwrite_output().run()
        print(f"Successfully created waveform video: {output_file}")
    except ffmpeg.Error as e:
        print("An error occurred:")
        print(e.stderr.decode())


def test(input_file: str, output_file: str):
    my_wave(input_file, "omg.mp4")
    # example_1(input_file, f"{output_file}_1.mp4")
    # example_2(input_file, f"{output_file}_2.mp4")
    # example_3(input_file, f"{output_file}_3.mp4")
    # example_4(input_file, f"{output_file}_4.mp4")
    # simple_waveform(input_file, f"{output_file}_simplewf.mp4")
