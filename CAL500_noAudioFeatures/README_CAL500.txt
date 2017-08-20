Computer Audition Lab 500 (CAL500) data set - 500 songs performed by 500 unique 
artists. 
Each song has been annotated by at least 3 people using a standard survey.

PROVIDED: 
Douglas Turnbull, Luke Barrington, David Torres, and Gert Lanckriet
Computer Audition Lab
UC San Diego
May 2007

CONTENTS:
SampleForm.htm 	- example of web-based musical survey
songNames.txt	- list of 502 songs  
vocab.txt  		- list 174 words (unigrams and bi-grams)  
hardAnnotations.txt	- 502 x 174 binary matrix (as a comma-seperated file) 
			- 1 if  80% of the test subject label the song with the word AND 
			  a minimum of 2 test subjects label the song with the word
			- 0, otherwise
softAnnotations.txt 	- 502 x 174 real-valued matrix
- proportion of users who considered a song indicative of a word
annotations/		- directory of 502 raw annotation files
deltas/			- directory of 502 feature files.
			- Each song is represented as a bag-of-feature-vectors
			- each feature-vector

REFERENCE:
If you use the CAL500 data set, please cite the following paper:

@inproceedings{turnbull07, 
	Author = {Douglas Turnbull and Luke Barrington and David Torres and Gert 
Lanckriet},
	Booktitle = {ACM Special Interest Group on Information Retrieval Conference  
(SIGIR '07)},
	Title = {Towards Musical Query-by-Semantic Description using the {CAL500} Data 
Set},
	Year = {2007}}

You can find the original text of the paper at the UCSD Computer Audition Lab home 
page:
http://cosmal.ucsd.edu/cal


COPYRIGHT NOTICE:
Copyright - University of California San Diego, 2007

This work may not be copied or reproduced in whole or in part for any commercial 
purpose. Permission to copy in whole or in part without payment of fee is granted for 
nonprofit educational and research purposes provided that all such whole or partial 
copies include the following: a notice that such copying is by permission of the 
Computer Audition Laboratory of the University of California, San Diego; an 
acknowledgment of the authors and individual contributors to the work; and all 
applicable portions of the copyright notice. Copying, reproducing, or republishing for any 
other purpose shall require a license with payment of fee to the University of California, 
San Diego.
All rights reserved.


DETAILS:

Music Corpus:
The 500 songs were picked from the authors' personal collection of western popular 
music recorded within the last 50 years. We picked one song at random to represent 
each of a diverse set of musicians. A subset set of the songs taken from the 
Magnatunes data set which was used in the 2005 MIREX data mining contest. To our 
knowledge, these songs are copyright-cleared for the purpose of music information 
retrieval research and may be downloaded free of charge from the 2005 MIREX wiki.
http://www.music-ir.org/mirex2005/

Audio Representation:
We represent the audio with a time series of delta cepstrum feature vectors.  We extract 
a time series of the first 13 Mel-frequency cepstral coefficients by sliding a 12 msec half-
overlapping short-time window over the waveform data file for each song.  We compute 
a delta cepstrum vector by appending the instantaneous first and second derivatives of 
each MFCC to the vector of MFCCs. The result is approximately 10,000 39-dimensional 
feature vectors per minute of audio content.  We randomly sub-sample the set of delta 
cepstrum feature vectors to represent each song with exactly 10,000 feature vectors. It 
is not possible to reconstruct the original audio waveform from this audio feature 
representation.
MATLAB-readable ASCII files containing the delta cepstrum features for each song are 
in the "/delta/" directory and are named:
    artist_name-song_name.delta


Semantic Representation:
We consider 135 musically-relevant concepts spanning six semantic categories: 
29 instruments were annotated as present in the song or not; 
22 vocal characteristics were annotated as relevant to the singer or not; 
36 genres, a subset of the Codaich genre list, were annotated as relevant to the song or 
not; 
18 emotions, found by Skowronek et al. (2006) to be both important and easy to identify, 
were rated on a scale from one to three (e.g., ``not happy", ``neutral", ``happy");
15 song concepts describing the acoustic qualities of the song, artist and recording 
(e.g., tempo, energy, sound quality); 
15 usage terms (e.g., "I would listen to this song while driving, sleeping, etc.").
An example of the HTML form presented to annotators is in the file:
    sample_form.html
A list of the semantic concepts used to annotate each song is in the file:
    vocab.txt

We paid 66 undergraduate students to annotate the CAL500 corpus with semantic 
concepts from our vocabulary.  Participants were rewarded $10 for a one hour 
annotation block spent listening to MP3-encoded music through headphones in a 
university computer laboratory.  The annotation interface was an HTML form loaded in a 
web browser requiring participants to simply click on check boxes and radio buttons.  
The form was not presented during the first 30 seconds of playback to encourage 
undistracted listening. Listeners could advance and rewind the music and the song 
would repeat until all semantic categories were annotated.  Each annotation took about
5 minutes and most participants reported that the listening and annotation experience 
was enjoyable.  We collected at least 3 semantic annotations for each of the 500 songs 
in our music corpus and a total of 1708 annotations.  
Text files with the raw annotations are in the "/annotations/" directory and are named: 
    artist_name-song_name-annotation_number.txt

We expand the set of 135 survey concepts to a set of 237 `words' by mapping all bipolar 
concepts to two individual words. For example, the five degrees of the concept `Energy 
Level' were mapped to `Low Energy' and `High Energy'. The resulting collection of 
human annotations uses a vector of numbers to express the response of a human 
listener to a semantic keyword.  For each word, the annotation vector takes the value +1 
or -1 if the human annotator considers the song is or is not indicative of the word, or 0 if 
unsure.  We take all the human annotations for each song and combine them to a single 
annotation vector for that song by observing the level of agreement over all annotators. 
The final semantic weights for a song/word pair are:

	weight(song, word) = max ( 0, #positive votes - #negative votes / #annotations)

For example, for a given song and word, if four listeners labeled the song with +1, +1, 0, 
-1, then the weight is 1/4.
This data is stored as a comma-separated, MATLAB readable (function 'dlmread') ASCII 
file 'softAnnotations.txt'

For evaluation purposes, we also create `ground truth' binary annotation vectors. We 
generate binary vectors by labeling a song with a word if a minimum of two people 
express an opinion and there is at least 80% agreement between all listeners. We prune 
all concepts that are represented by fewer than five songs. This reduces our vocabulary 
from 237 to 174 words.
This data is stored as a comma-separated, MATLAB readable (function 'dlmread') ASCII 
file 'hardAnnotations.txt'

