# chardistance
*Would you rather watch a Catalan movie at *la Cinémathèque française* subtitled in French or a French movie at *la Filmoteca de Catalunya* subtitled in Catalan?*  

# Motivation
As a spanish speaker, being in Barcelona is not an issue... unless you dare to go to La Filmoteca de Catalunya and watch a French movie subtitled in Catalan.  
Given that I don't know any of both languages beyond a small set of words (not even half A1), I wondered how should I watch the movie if I wanted to understand the dialogues.  
Should I focus on the speech sounds or the subtitles? Does it make any difference?  
My intuition says that Catalan should be easier to understand -at least that's what I think when I read it-. However, it resembles French when I hear it.  
In order to find out the difference and measure it somehow, I decided two measure two different but related language aspects using the same metric: Levinshtein Distance on the ortographic transcription of the dialogues (i.e. subtitles) and on the phonemic transcription of the dialogues (i.e. speech sounds).  

# Research Question
What is the Levenshtein Distance betweeen Spanish, French, and Catalan, considering the ortographic and phonemic transcriptions?  

# Data
In order to compare these three languages, a small corpus was created using a fraction of *Harry Potter: The Philosopher's stone*.  

A parallel corpus was manually created considering coincident sentence boundaries when possible. Due to translation, this is not always possible. The main criteria when setting boundaries was to keep sentences short enough to make the comparison reliable, and long enough to convey a full idea.
Examples of the alignment:  
| Spanish | French | Catalan |
| --- | --- | --- |
| El señor Dursley era el director de una empresa llamada Grunnings, que fabricaba taladros. | Mr Dursley dirigeait la Grunnings, une entreprise qui fabriquait des perceuses. | El senyor Dursley era director d’una fàbrica anomenada Grunnings, que feia broques. | 
| Nuestra historia comienza cuando el señor y la señora Dursley se despertaron un martes, con un cielo cubierto de nubes grises que amenazaban tormenta. Pero nada había en aquel nublado cielo que sugiriera los acontecimientos extraños y misteriosos que poco después tendrían lugar en toda la región. | Lorsque Mr et Mrs Dursley s'éveillèrent, au matin du mardi où commence cette histoire, il faisait gris et triste et rien dans le ciel nuageux ne laissait prévoir que des choses étranges et mystérieuses allaient bientôt se produire dans tout le pays. | Quan el senyor i la senyora Dursley es van aixecar el dimarts gris i trist en què comença la nostra història, no hi havia res al cel ennuvolat que pogués fer pensar que molt aviat succeirien coses estranyes i misterioses per tot el país. |

The books used were translated by:
  * Catalan: Laura Escorihuela Martínez - Editorial Empúries (1999)  
  * French: Jean-François Ménard - Gallimard (2007)  
  * Spanish: Alicia Dellepiane - Emecé Editores España, S.A. (1999)  

The corpus comprises 47 sentences, which accounts for ... on average on each language. The shortest sentence is ... and the largest is ... On average each sentence is ...

# Levenshtein Distance
Levenshtein Distance is a number that counts how (dis)similar two strings are. It does so by counting how many times you would need to *insert*, *replace*, or *delete* a character to get a match.  
For example, the distance between `hello` and `yellow` will be of 2:
replace `h`by `y`  
insert `w` or delete `w`
## Character distance

## Phonemic distance

# Preprocessing



# Bibliography
