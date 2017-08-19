import glob
from pydub import AudioSegment

for fname in glob.glob("CAL500_32kps/*.mp3"):
    print(fname)
    AudioSegment.from_mp3(fname).export(
        fname.replace('32kps/', 'wav/').replace('.mp3', '.wav'), format="wav")
