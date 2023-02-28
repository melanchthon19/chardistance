# chardistance
*Would you rather watch a Catalan movie at *la Cinémathèque française* subtitled in French or a French movie at *la Filmoteca de Catalunya* subtitled in Catalan?*  

# Motivation
As a spanish speaker, being in Barcelona is not an issue... unless you dare to go to La Filmoteca de Catalunya and watch a French movie subtitled in Catalan.  
Given that I don't know any of both languages beyond a small set of words (not even half A1), I wondered how should I watch the movie if I wanted to understand the dialogues.  
Should I focus on the speech sounds or the subtitles? Does it make any difference?  
My intuition says that Catalan should be easier to understand -at least that's what I think when I read it-. However, it resembles French when I hear it.  
In order to find out the difference, I decided two measure two different but related language aspects using the same metric: Levinshtein Distance on the ortographic transcription of the dialogues (i.e. subtitles) and on the phonemic transcription of the dialogues (i.e. speech sounds).  

# Research Question
What is the Levenshtein Distance betweeen Spanish, French, and Catalan, considering the ortographic and phonemic transcriptions?  

# Data
In order to compare these three languages, a small corpus was created using a fraction of *Harry Potter: The Philosopher's stone*.  

A parallel corpus was manually created considering coincident sentence boundaries. Due to translation, this is not always possible. The main criteria when setting boundaries was to keep sentences short enough to make the comparison reliable, and long enough to convey a full idea.
Examples of the alignment:  
| Spanish | French | Catalan |
| --- | --- | --- |
| El señor Dursley era el director de una empresa llamada Grunnings, que fabricaba taladros. | Mr Dursley dirigeait la Grunnings, une entreprise qui fabriquait des perceuses. | El senyor Dursley era director d’una fàbrica anomenada Grunnings, que feia broques. | 
| Nuestra historia comienza cuando el señor y la señora Dursley se despertaron un martes, con un cielo cubierto de nubes grises que amenazaban tormenta. Pero nada había en aquel nublado cielo que sugiriera los acontecimientos extraños y misteriosos que poco después tendrían lugar en toda la región. | Lorsque Mr et Mrs Dursley s'éveillèrent, au matin du mardi où commence cette histoire, il faisait gris et triste et rien dans le ciel nuageux ne laissait prévoir que des choses étranges et mystérieuses allaient bientôt se produire dans tout le pays. | Quan el senyor i la senyora Dursley es van aixecar el dimarts gris i trist en què comença la nostra història, no hi havia res al cel ennuvolat que pogués fer pensar que molt aviat succeirien coses estranyes i misterioses per tot el país. |

The corpus comprises 45 sentences. Each language has roughly 950 tokens and each sentence is 20 tokens long on average.

# Levenshtein Distance
Levenshtein Distance is a number that counts how (dis)similar two strings are. It does so by counting how many times you would need to *insert*, *replace*, or *delete* a character to get a match.  
For example, the distance between `hello` and `yellow` will be of 2:  
  * replace `h` by `y`  
  * insert `w` or delete `w`

This metric considers the best way of going from one string to the other by doing the least possible changes.  
The following table shows the Levenshtein Distance applied to both ortographic and phonemic transcription of the first example:  
| Language | Sentence |
| --- | --- |
| Spanish | El señor Dursley era el director de una empresa llamada Grunnings, que fabricaba taladros. |
| French | Mr Dursley dirigeait la Grunnings, une entreprise qui fabriquait des perceuses. |
| Catalan | El senyor Dursley era director d’una fàbrica anomenada Grunnings, que feia broques. |

| Comparison | Levenshtein Distance | Score |
| --- | --- | --- |
| Spanish & French | `_r dursley __r__e_it __ ________s_ ___ ___r___is_ qu_ fabri__a__ ___ __r___s__.` | 62 |
| French & Catalan | `__ _____r dursley ___ _i_e_t__ __un_ _______ _n__e____ __u_______ qu_ _e__ _r__ues.` | 60 |
| Catalan & Spanish | `el se__or dursley era director d_una ___r__a ___m__ada grunnings, que f_ia ______s.` | 30 |

## Ortographic transcription
The books used to obtain ortographic transcriptions were translated by:  
  * Catalan: Laura Escorihuela Martínez - Editorial Empúries (1999)  
  * French: Jean-François Ménard - Gallimard (2007)  
  * Spanish: Alicia Dellepiane - Emecé Editores España, S.A. (1999)  

## Phonemic transcription
Two resources were used to obtain standard phonemic transcriptions:  
  * French: [OpenIPA](https://www.openipa.org/)  
  * Spanish and Catalan: [TexAFon](https://tomcat.labfon.uned.es/texafon/)  

Example of the transcription:
| Spanish | French | Catalan |
| --- | --- | --- |
| Era un hombre corpulento y rollizo, casi sin cuello, aunque con un bigote inmenso. | C'était un homme grand et massif, qui n'avait pratiquement pas de cou, mais possédait en revanche une moustache de belle taille.	| Era un home gros i fort que gairebé no tenia coll, però que lluïa un bigoti enorme. |
| eɾa un ombɾe koɾpulento i roʝiθo, kasi sin kweʝo, awnke kon un Biɣote inmenso	| setɛt‿ œ̃ ɔmə gɾɑ̃d‿e masif, ki nave pɾatikəmə pa də ku, me pɔsedɛt‿ɑ̃ ɾəvɑ̃ʃ ynə mustaʃə də bɛlə tajə.	| eɾə un ɔmə gɾɔz i fɔɾt kə kəjɾəβe no təniə kɔʎ, pəɾɔ kə ʎuiə un pigɔti ənoɾmə |

# Preprocessing
Before measuring Levenshtein Distance, preprocessing and formatting was applied. Specifically, before ortographic comparison, all vowel's variations were reduced to one (i.e. â --> a). Before phonemic comparison, `‿` was deleted as it was added by OpenIPA to denote liaison. However, the inserted phoneneme was kept. In both cases, any punctuation was removed.

# Results
The following table depicts the results. Each column represents the Levenshtein Distance between a pair of languages, and each row shows the ortographic and phonemic comparison.

| Comparison | Spanish-French | Spanish-Catalan | French-Catalan |
| --- | --- | --- | --- |
| Ortographic | 95,04 | 68,98 | 92,67 |
| Phonemic | 92,67 | 76,11 | 88,39 |

Considering the ortographic comparison, Spanish and Catalan are closer to each other than they are to French, which is equally away by roughly 25 characters. The difference between Spanish-Catalan and Spanish-French comparison is of 26 changes, and the difference between both distances is of 21.  
According to the phonemic comparison, Spanish is still closer to Catalan than it is to French by 16 changes. However, Spanish and Catalan are not equally away from French as the ortographic comparison showed. The difference between the Spanish-Catalan and Spanish-French comparison is of 15 changes, and the difference between both distances is of 8 characters.  
These results suggests that for a Spanish speaker, Catalan is closer both ortographically as well as phonemically. Nonetheless, given that ortographic and phonemic distances are not of the same scale, the overall reduction of phonemic distances indicates that languages are evenly away from each other with regards to speech: ortographically the distance is of 26, whereas phonemically the distance is of 8, which is closer to 0.

# Conclusions
Reading Catalan for a Spanish speaker will be easier to understand than listening, and understanding Catalan overall will be easier than French.  
With regards to Catalan, even though it is phisically closer to French, their phonemic distance is almost as that of Spanish and French.  
Last, but not least, I would recommend watching a French movie at *la Filmoteca de Catalunya* subtitled in Catalan.

# Future work
  * Use a bigger parallel corpora.  
  * Compare MFCCs on the actual movie (speech, sounds, and music included, as everything affects comprehension).  
  *  Compare ortographic and phonemic overlapping between languages, and their predominance in their lexicon.

# How to use this repository

Clone the repository: `git clone git@github.com:melanchthon19/chardistance.git`  
Change directory: `cd chardistance`  
Install packages: `pip install -r requirements.txt`  
`levenshtein.py`contains the Levenshtein class.  
You can run `levenshtein.py` by itself passing two strings: `./levenshtein.py string1 string2`  
`compare.py` uses Levenshtein class to compare strings from a given file.  
It accepts the following flags:  
`--file: file that stores sentences`  
`--index: analyse sentence at given index only`  
`--preprocess: {ortographic,phonemic}`  
`--verbose: print each minimum edit distance`  
Usage example:  
`./compare.py -f data/hp.csv -p ortographic -v -i 2`  
`./compare.py -f data/hp-phonemic.csv -p phonemic`  

# Bibliography
[OpenIPA: Free, informative IPA transcription for Lyric Diction](https://www.openipa.org/)  
[TexAFon: Herramienta de transcripción fonética](https://tomcat.labfon.uned.es/texafon/)  
[Catalan Phonemic Chart](http://www.ub.edu/sonscatala/en/phonemic-chart-central)  
[Automatic Phonetic Transcription of dialectal variance in Catalan](https://repositori.upf.edu/bitstream/handle/10230/28108/Codina_2016.pdf?sequence=1&isAllowed=y)  
[Phonological Distance Measures](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2856103/)  
[Applying the Levenshtein Distance to Catalan dialects](http://www.let.rug.nl/~wieling/martijnwieling/files/Valls.pdf)  
[Levenshtein Distance](https://people.cs.pitt.edu/~kirk/cs1501/Pruhs/Spring2006/assignments/editdistance/Levenshtein%20Distance.htm#:~:text=What%20is%20Levenshtein%20Distance%3F,to%20transform%20s%20into%20t.)
Harry Potter y la piedra filosofal. Translated by Alicia Dellepiane. Emecé Editores España, S.A. (1999).  
Harry Potter y la pedra filosofal. Translated by Laura Escorihuela Martínez. Editorial Empúries (1999).  
Harry Potter à l'Ecole des Sorciers. Translated by Jean-François Ménard - Gallimard (2007)  