import pyaudio
import wave
def rec():
    filename = "SampleData/recorded.wav"

    chunk = 1024

    FORMAT = pyaudio.paInt16

    channels = 1

    sample_rate = 44100
    record_seconds = 10

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
            channels=channels,
            rate=sample_rate,
            input=True,
            output=True,
            frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)

        frames.append(data)
    print("Finished recording.")

    stream.stop_stream()
    stream.close()

    p.terminate()

    wf = wave.open(filename, "wb")

    wf.setnchannels(channels)

    wf.setsampwidth(p.get_sample_size(FORMAT))

    wf.setframerate(sample_rate)

    wf.writeframes(b"".join(frames))

    wf.close()