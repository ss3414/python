# ****************************************************************分割线****************************************************************
# todo mido

from mido import Message, MidiFile, MidiTrack

input_file = MidiFile("../untitled/test.mid")
tracks = input_file.tracks  # 音轨

new_tracks = []
for track in tracks:
    new_track = MidiTrack()
    new_tracks.append(new_track)

    # 遍历音轨中的消息
    for msg in track:
        # 如果消息是音符on
        if msg.type == "note_on" and msg.velocity > 0:
            # 调整音强值
            new_velocity = msg.velocity // 2
            new_msg = Message("note_on", note=msg.note, velocity=new_velocity, time=msg.time)
            new_track.append(new_msg)
        else:
            new_track.append(msg)

output_file = MidiFile()
output_file.tracks = new_tracks
output_file.save("C:/Users/Administrator/Desktop/test_1.mid")
