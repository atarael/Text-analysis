# Text-analysis
name:Atara elmaliach
id:207233990

The purpose of the exercise:
The program receives a text file as input
And create a statistical report on it.
 
use of library:
from __future__ import with_statement
import string

files:
textAnalysis.py- The main program
dickens.txt-text file for example

input:
The path to the text file

output file:
statisticalData.txt

An example of running the program:
===========================================
Input text file:
===========================================
red.
Mr Lightwood, without explaining that his weariness was chronic,
proceeded with his exposition that, all forms of law having been at
length complied with, will of Harmon deceased having been
proved, death of Harmon next inheriting having been proved, &c.,
and so forth, Court of Chancery having been moved, &c. and so
forth, he, Mr Lightwood, had now the gratification, honour, and
happiness, again &c. and so forth, of congratulating Mr Boffin on
coming into possession as residuary legatee, of upwards of one
hundred thousand pounds, standing in the  red books of the Governor
and Company of the Bank of England, again &c. and so forth.green

'And what is particularly eligible in the property Mr Boffin, is, that
it involves no trouble.  There are no estates to manage, no rents to
return so much per cent upon in bad times (which is an extremely
dear way of getting your name into the newspapers), no voters to
become parboiled in hot water with, no agents to take the cream off
the milk before it comes to table.  You could put the whole in a
cash-box to-morrow morning, and take it with you to--say, to the
Rocky Mountains.  Inasmuch as every man,' concluded Mr
Lightwood, with an indolent smile, 'appears to be under a fatal
spell which obliges him, sooner or later, to mention the Rocky
Mountains in a tone of extreme familiarity to some other man, I
hope you'll excuse my pressing you into the service of that gigantic
range of geographical bores.'
=============================
output file:
=============================
File statistics:
1-The amount of lines:
25
2-The amount of words:
258
3-The amount of unique words:
155
4-Size of longest Sequence by word:
56
4-Size of Average Sequence by word:
25.8
5-The word with highest frequency:
('of', 14)
6-Longest Sequence without k:
red mr lightwood without explaining that his weariness was chronic proceeded with his exposition that all forms of law having been at length complied with will of harmon deceased having been proved death of harmon next inheriting having been proved c and so forth court of chancery having been moved c and so forth he mr lightwood had now the gratification honour and happiness again c and so forth of congratulating mr boffin on coming into possession as residuary legatee of upwards of one hundred thousand pounds standing in the red
8- Freqency of colors:
{'red': 2, 'green':1}
