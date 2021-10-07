---
title: "Royal African Company Networks"
doi: "https://doi.org/10.31835/crdh.2019.10"
volume-number: 2
year: 2019
date: 2019-08-23
authors:
- last: Ruderman
  first: Anne
  email: A.E.Ruderman@lse.ac.uk
  affiliation: "Department of Economic History, London School of Economics"
  orcid: 0000-0001-5799-3806
  url: "http://www.lse.ac.uk/Economic-History/People/Faculty-and-teachers/Dr-Anne-Ruderman"
- last: Heller
  first: Mark
  email: mark@markheller.org
  affiliation: "Harvard University Graduate School of Design"
  orcid: 0000-0003-2539-0554
- last: Xue
  first: Harry
  email: wenzhexue2014@gmail.com
  affiliation: 2018 Harvard College graduate
  orcid: 0000-0001-8369-8755
  url: "https://www.linkedin.com/in/harry-xue-ab8a84ab/"
abstract: |
  Royal African Company Networks is a pilot project designed to explore the possibilities of using computational text analysis and GIS to investigate the correspondence of the Royal African Company, England’s late seventeenth-century African trade monopoly. Our project maps over 3,000 letters between the company’s main fort, Cape Coast Castle, in modern-day Ghana and the company’s ‘outforts,’ or smaller holdings on the coast. We then combine mapping with computational text analysis to draw out themes in the correspondence. We hope this project demonstrates the potential of bringing an interdisciplinary approach to historical analysis and serves as a stepping-stone for further exploration.
appendix:
- name: Github
  url: "https://github.com/xueharry/RAC"
preview: "/assets/img/v02/ruderman/preview.png"
---

In the final quarter of the seventeenth century, England's
state-sponsored African trade monopoly, the Royal African Company,
conducted trade via a series of forts on the Gold and Slave coasts in
West Africa. The company anchored its trade at Cape Coast Castle, in
modern-day Ghana, which served as a communications hub for the coast,
corresponding with smaller forts, or 'outforts' and relaying news and
requests to London.[^1] Our project combines computational text analysis
with GIS to thematically map the correspondence of the Royal African
Company (RAC) on the African coast between 1681 and 1699, the final two
decades of the company's monopoly. The last two decades of the
seventeenth century are a crucial window for understanding the
development of the transatlantic slave trade on the African coast.
Although the Portuguese engaged in the African slave trade starting in
the sixteenth century, the formation of the Royal African Company gave a
major impetus to the slave trade, laying the English infrastructure for
the transatlantic traffic.[^2] Looking at the last two decades of the
seventeenth century enables us to examine how the African trade operated
before it definitively turned to slaves and before a wide range of
private merchants swarmed the coast in search of captives to take to the
Americas.[^3] This project is currently in a pilot phase, accessible on
the website racnetworks.wordpress.com. We hope that our website, current
findings and ongoing questions will be the basis of a larger research
agenda, culminating in a series of publications and a public exhibition
of cartographic and infographic visualizations.

Our maps and informational graphics are based on a collection of over
3,000 individual letters that the RAC sent from one place to another on
the West African coast. These letters were originally held in the
collection of Richard Rawlinson at the Bodleian Library in Oxford. They
were transcribed and published in a three-volume series, *The English in West Africa: The Local Correspondence of the Royal African Company of England, 1681--1699*, which was edited by Robin Law and published by
Oxford University Press between 1997 and 2006, with an online edition
published in 2015.[^4] The *English in West Africa* collection
complements the more widely known and utilized Royal African Company
(T70) corpus at The National Archives in Kew. Despite the unusual detail
and geographic breadth of these letters, they are often overlooked in
major research projects involving the transatlantic slave trade, as
scholars have consistently favored the company's main archive at
Kew.[^5]

The Rawlinson corpus contains 3095 letters, with approximately 450,000
words, of which 15,625 are unique words.[^6] The letters are incredibly
rich and informative when read up close. They express, at varying
moments, nonchalance, concern, satisfaction and frustration when all
goes wrong. They reveal the mechanisms of Euro-African trade at work and
the texture of life on the African coast in the late seventeenth
century: a world beset by fires, rats, fighting and occasional shortages
of food. They illustrate the tenuous position of the company's forts on the
African coast and the way that the company's fort structure was deeply
embedded in an African geopolitical context. But they are even more
meaningful when read in conjunction with macro-techniques. By using
computational text analysis combined with insights from GIS, we can
challenge some basic assumptions about the way the English monopoly
operated on the African coast. Despite the richness of the corpus, it is
also worth noting what the letters do not reveal: The individual lives
or interior thoughts and feelings of enslaved people, either working at
the company's forts or ensnared in the transatlantic traffic.[^7]

Our research enables us to make two main interventions in the literature
of the transatlantic slave trade. Slave trade scholarship has cast the
Royal African Company as a static and inefficient presence on the coast,
unable to effectively compete with more dynamic private traders, who
operated out of boats.[^8] But the Royal African Company effectively
used coasting and transatlantic vessels as vectors of communication,
ferrying information from one part of the coast to another. We can also
demonstrate that slaves were more prevalent in the company's
discussions on the coast than gold in the late seventeenth century, even
though the trade in non-human commodities was more valuable than the trade in people throughout the seventeenth century.[^9]

{% figure caption: "Figure 1. This map at the scale of the coast of Western Africa illustrates the density of correspondences of the Royal African Company. Line weight corresponds to the volume of correspondences sent to each post." %}
![Map showing the density of correspondences of the Royal African Company.]({{site.url}}/assets/img/v02/ruderman/figure1.jpg)
{% endfigure %}

{% figure caption: "Figure 2. This map illustrates the density of ships “In the Road”---ships stationed one to two miles from shore---for the year 1683. Evident is heavy activity near Sekondi, between Alampo and Amersa, and between Accra and Christiansborg." %}
![Map of ships in the road.]({{site.url}}/assets/img/v02/ruderman/figure2.jpg)
{% endfigure %}

We approached the corpus through three main types of textual analysis:
word-frequency analysis (both globally and by place, type and sender),
word embeddings using word2vec in order to show relational meaning and
co-occurrence to track how pairings of goods that the company traded
varied over individual letters. In order to be able to use computer
software on a seventeenth-century corpus, we had to first eliminate and
consolidate as many of the variations in orthography as possible. Early
modern English writers were very creative spellers, at times writing the
same word---for example, "heareing" and "hearing"---two different ways
in a single letter. The corpus, for example, contains 11 different
spellings of the trade good "perpetuanos," a coarse woolen textile often
exchanged on the African coast.[^10] When confronted with words of
Portuguese descent or words in African languages, the variations in
spelling could be wide-ranging. Ultimately, we were able to trim the
corpus from 17,001 unique words to 15,625 unique words.[^11]

For the mapping portion of the project, we likewise had to derive
coordinates from places on the African coast that were in operation in
the late seventeenth century, but do not necessarily neatly correspond
to modern locations in Africa today. We approached this gap by
triangulating between existing seventeenth-century maps and modern maps
published in secondary literature on the Gold Coast.[^12] The fact that
we could not overlap easily onto the existing geocoded dataset of the
Trans-Atlantic Slave Trade Database shows how much more dense activity
was on the coast than existing online platforms for understanding the
slave trade would lead us to think.[^13]

The variation of textual analysis methods allowed us to investigate how
individual words surfaced in the corpus and how words related to one
another, in other words we could measure importance and relational
meaning. Because we are interested in developing a geospatial
understanding of the RAC's presence on the African coast we looked at
how various words appeared by individual fort. We also tracked how the
appearance of individual words changed over time, and how words appeared
throughout the yearly cycle, contributing to a crucially important yet
often understated aspect of the African trade, seasonality. We then
performed an analysis on the corpus using word embeddings, which
revealed which words appeared in similar linguistic contexts throughout
the letters. This enabled us to visualize which words shared common
contexts, and hence infer the semantic contexts in which key terms were
most commonly used. Lastly, we analyzed co-occurrence of trade goods
mentioned in the letters, tracing how the bundle of goods changed (or
did not) across individual letters in the corpus.

Even straightforward word-frequency analysis on the corpus proved to be
revealing. Communicative words, such as "send," "sent," "received"
are the most important, but the first substantive word that appears is
"canoe." Canoes are vectors of communication on the coast and can
travel against the prevailing eastward current as well as over the surf,
reaching transatlantic ships in the ocean beyond. The word-frequency
analysis also showed a significant gap between "slaves" (1674) and
"gold" (663), suggesting that slaves were very much a part of the
RAC's quotidian existence on the coast.[^14] The salience of the agricultural product,
"corn" (1243), suggests that African agriculture was well-developed in
the early phase of European contact. The RAC discussed the "Dutch"
(904) more than they discussed "gold," "gunpowder" or the term
"trade". "Perpetuanos" (700) emerges as the main trade good mentioned
in the letters and the frustration word, "cannot" (544) ranks fairly
high, suggesting perhaps organizational discord, but also perhaps that
RAC fort factors were pushing up against the limit of what was possible
from their positions on the coast.[^15]

{% figure caption: "Figure 3. A ranked list of the most frequently used words in the corpus. Note the frequency of communicative words, and the presence of the frustration word, “cannot”. The relative high frequency of the word “Dutch” reveals them to be a preoccupation." %}
![A list of the most frequently used words in the Royal African Company corpus.]({{site.url}}/assets/img/v02/ruderman/figure3.jpg)
{% endfigure %}

{% figure caption: "Figure 4. This map illustrates the percentage of correspondences per fort that include the words “Slaves” and “Canoe.” There appears to be greater overlap between correspondences featuring these two words than the singular “Slave” and “Canoe.”" %}
![Map showing correspondence including the words "Slaves" and "Canoe."]({{site.url}}/assets/img/v02/ruderman/keyword-slaves-canoe.jpg)
{% endfigure %}

{% figure caption: "Figure 5. This map illustrates the percentage of correspondences per fort that include the words “Slave” and “Canoe.” There is some, though not considerable, overlap between correspondences featuring these two words." %}
![Map showing correspondence including the words "Slave" and "Canoe."]({{site.url}}/assets/img/v02/ruderman/keyword-slave-canoe.jpg)
{% endfigure %}

{% figure caption: "Figure 6. This map illustrates the percentage of correspondences per fort that include the word “Dutch.” Letters to Butterue and Cape Apollonia heavily feature this term." %}
![Map showing correspondence including the word "Dutch."]({{site.url}}/assets/img/v02/ruderman/keyword-dutch.jpg)
{% endfigure %}

{% figure caption: "Figure 7. This map illustrates the percentage of correspondences per fort that include the word “Gold.” Letters to Butterue, Axim, and Christiansborg heavily feature this term." %}
![Map showing correspondence including the word "Gold."]({{site.url}}/assets/img/v02/ruderman/keyword-gold.jpg)
{% endfigure %}

{% figure caption: "Figure 8. This map illustrates the percentage of correspondences per fort that include the word “Woman” or “Women.” Letters to Kpone and Teshi heavily feature this term." %}
![Map showing correspondence including the word "Woman" or "Women."]({{site.url}}/assets/img/v02/ruderman/keyword-woman.jpg)
{% endfigure %}

Analyzing word frequency by different dimensions---place, sender, year
and month---shows further patterns in the corpus. For example, pirate
and pirates emerge as a major concern to the company, with a
concentration to the west. But "pirate" and "pirates" only surface in
some locations and from some letter-writers, while the term "slaves"
is ubiquitous. Breaking word frequencies down by fort, coasting voyage
and transatlantic voyage, coasting voyages emerge as crucially important
to the way the company conducted business, loaded with key words. The
company had a network in the water that mirrored the information
structure of the forts on land. Seasonal patterns were also significant
and differed for different words: For example, "pirate" and "pirates"
spiked between May and July, "corn" peaked in March, with a big dropoff
in September. "Slaves" likewise peaked in March and then declined
throughout the rest of the year, while "slave" rose between February
and April and then stayed at more or less a continuous level.[^16]

{% figure caption: "Figure 9. A basic count of the words “pirate” and “pirates” by location, reveals pirates to be a concern towards the western edge of the company's fort structure. The prevailing eastward current means that ships approaching the companies string of forts would come from the West." %}
![Bar graph showing a word count of the terms “pirate” and “pirates” by location.]({{site.url}}/assets/img/v02/ruderman/figure9.png)
{% endfigure %}

{% figure caption: "Figure 10. Correspondence from ships, whether coasting or transatlantic vessels discussed pirates more often in relative terms, than did correspondence from forts." %}
![Bar graph showing the percentage of letters mentioning “pirate” and “pirates” by boat or fort.]({{site.url}}/assets/img/v02/ruderman/figure10.png)
{% endfigure %}

{% figure caption: "Figure 11. Different search terms evidenced strikingly different seasonal patterns." %}
![Four line graphs compare the different seasonal patterns between the terms “pirate”/“pirates”; “corn”; “slave”; and “slaves.”]({{site.url}}/assets/img/v02/ruderman/figure11.png)
{% endfigure %}

How words relate to one another is as significant as how they appear in
the corpus by themselves. By obtaining vector representations of terms
in the corpus using the word2vec algorithm, we were able to discern
several distinct clusters of language via visual inspection: There is a
cluster of "company politeness language," words such as: humbly,
honour, worship(s), companys, interest, advise, endeavour.[^17] There is
a second cluster of words around slaves: canoe, old, irons, guns, small,
black, negroes, paid, escaped, left, sent, sloop. A third cluster
encompasses words relating to gold. These are words concerning trade
goods, money and colors: red, pewter, cases, rum, narrow, fine, whole,
sletias. A fourth cluster concerns quantity words. A final cluster
includes nautical, geographic and competitive terms: ashore, windward,
French, Dutch, interloper, aboard, road, ship, coast.

{% figure caption: "Figure 12. Word embeddings done via word2vec show distinct clusters of words around different themes." %}
![Visualization created with Word-2-Vec showing five distinct word clusters.]({{site.url}}/assets/img/v02/ruderman/figure12.jpg)
{% endfigure %}

Our final method of analysis, co-occurrence, traced associations between
goods throughout the corpus. We opted to limit the words under
consideration to trade goods, manufactured items, like guns or
perpetuanos, which the RAC exchanged with its African trading partners.
The co-occurrence analysis showed very little evidence of a single good being predictive of the presence of other goods
except for occasional pairs of textiles, for example, tapseils and
sletias. Here the lack of co-occurrence may be meaningful: The slave
trade pattern of the eighteenth century was characterized above all by
assortment bargaining, the repeated exchange of a small mix of trade
goods for a small number of enslaved people.[^18] In assortment
bargaining, the assortment consisted of a range of trade goods, from
beads to alcohol to textiles to metalworks, as slave-ship captains
combined diverse goods to form the package. It is possible that this
type of assortment bargaining may not yet have fully emerged in the
RAC's trading practices on the coast in the last quarter of the
seventeenth century. While the Royal African Company trafficked in a
wide range of goods during its monopoly era, the company may not have
exchanged these goods at the same time, but rather individually and
sequentially.[^19]

{% figure caption: "Figure 13. A co-occurrence analysis, tracking the appearance of pairs of words on a per-letter basis, reveals a lack of predictability among trade goods. The presence of one trade good in a letter does not predict the presence of other trade goods." %}
![List of co-occurrence analysis]({{site.url}}/assets/img/v02/ruderman/figure13.jpg)
{% endfigure %}

Ultimately we want to ask four different types of questions of the
corpus. First, we want to ask questions about the organization of a
monopoly. We want to be able to use the corpus to better understand how
the RAC defended itself against competitors and how the company
controlled internal problems. We want to use mapping, including
georeferenced fort locations, volume and breadth of letters, and
language of the text indicating directionality and relational values, to
demonstrate the company's "communication zone," (points to which they
had direct communication) and "knowledge zone" (a broader swath of
area for which they had second-hand information).

Second, we want to ask questions about trade goods: How did the company
figure out what its African consumer marketplace wanted? To what extent
was the RAC thinking about trade goods in the context of what they heard
their African trading partners wanted and to what extent was the RAC
thinking about trade goods in the context of what other Europeans (i.e.
the Dutch) were selling?

Third, we want to ask questions about exports: What was the Royal
African Company purchasing in Africa? Did some locations focus more on
slaves and some locations more on gold or ivory? Did the same locations
focus on different exports at different times?

Finally, we want to use computational text analysis to learn more about
the embedded (and precarious) nature of the RAC's operation on the
African coast and the company's relationships with its African trading
partners and surrounding states and societies. The transatlantic slave trade occurred because of the willing participation of African states and societies and we want to tease out individual African actors from the corpus in order to get a better sense
of how European-African relationships worked in the late seventeenth
century.

Beyond the questions we have, we also want to engage in a more
inductive and iterative process with the corpus to elicit questions we
do not yet know to ask.

---

### Bibliography

Charles, Loïc, Guillaume Daudin, and Paul Girard. "The treatment of merchandises in the toflit18 datascape." Conference Presentation, Boston: World Economic History Congress, 2018.

Davies, K.G. *The Royal African Company*. London: Longmans, 1957.

Eltis, David. "The Relative Importance of Slaves and Commodities in the Atlantic Trade of Seventeenth-Century Africa." *Journal of African History* 35, no. 2 (1994): 237--249. <https://doi.org/10.1017/S0021853700026414>.

Fuentes, Marisa J. *Dispossessed Lives: Enslaved Women, Violence and the Archive*. Philadelphia: University of Pennsylvania Press, 2016.

Green, Toby. *The Rise of the Trans-Atlantic Slave Trade in Western Africa, 1300--1589*. New York: Cambridge University Press, 2012.

Heywood, Linda. *Njinga of Angola: Africa\'s Warrior Queen*. Cambridge, MA: Harvard University Press, 2017.

Kea, Ray A. *Settlements, Trade and Polities in the Seventeenth-Century Gold Coast*. Baltimore: Johns Hopkins University Press, 1982.

Law, Robin, ed. *The English in West Africa: The Local Correspondence of the Royal African Company of England, 1681--1699,* 3 Vols. Oxford: Oxford University Press, 1997, 2001, 2006, (Online edition, British Academy) 2015.

Law, Robin. "Provisioning the Slave Trade: The Supply of Corn on the Seventeenth-Century Gold Coast." *African Economic History* 46, no. 1 (2018): 1--35. <https://doi.org/10.1353/aeh.2018.0000>.

Law, Robin. "The Royal African Company of England's West African Correspondence, 1681--1699." *History in Africa* 20 (1993): 173--184. <https://doi.org/10.2307/3171971>.

Lemercier, Claire, and Claire Zalc. *Quantitative Methods in the Humanities*. Translated by Arthur Goldhammer. Charlottesville: University of Virginia Press, 2019.

Mikolov, Tomas, et al. "Distributed Representations of Words and Phrases and their Compositionality." <https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf>.

Ruderman, Anne. "Supplying the Slave Trade: How Europeans Met African Consumer Demand for European Manufactured Products, Commodities and Re-exports, 1670--1790." Ph.D. diss., Yale University, 2016.

Smallwood, Stephanie E. *Saltwater Slavery: A Middle Passage From Africa to American Diaspora*. Cambridge: Harvard University Press, 2007.

Strickrodt, Silke. *Afro-European Trade in the Atlantic World: The Western Slave Coast c.1550--1885*. Suffolk: James Currey, 2015.

Thornton, John K. *Africa and Africans in the Making of the Atlantic World, 1400--1800*. Cambridge: Cambridge University Press, 1992, 1998.

Zook, George Frederick. *The Company of Royal Adventurers Trading Into Africa*. Lancaster, PA: Press of the New Era Printing Co, 1919.

---

### Notes
The authors are grateful to the Centre for History and Economics at Harvard University and the KEI initiative at the London School of Economics for funding. 

[^1]: The company had a second hub at James Fort in Gambia, which oversaw trade in Senegambia. 

[^2]: For the early Portuguese slave trade, see Green, *The Rise of the Trans-Atlantic Slave Trade*, 177--207. The Royal African Company followed a series of failed English African trade monopolies. For its immediate predecessor, see Zook, *The Company of Royal Adventurers*.

[^3]: In 1698 England opened up the African trade to any merchant willing to pay a ten percent fee on the goods he exported to the African coast. The impact of the measure, called the Ten Percent Act, was immediate: In the decade following the Ten Percent Act, English slave ships purchased roughly twice as many enslaved people as in the decade before. Data from the [*Trans-Atlantic Slave Trade Database*](https://www.slavevoyages.org/).

[^4]:  Law, ed., *The English in West Africa*. For an overview of the original transcription and publication effort, see Law, “Correspondence,” 173--184.

[^5]: For publications making extensive use of these letters, see Smallwood, *Saltwater Slavery*; Law, “Supply of Corn," 1--35; and Strickrodt, *Afro-European Trade*.

[^6]: This is our unique word count as of May, 2019. See further discussion of de-aliasing.

[^7]: In the context of enslavement, the Royal African Company archive is a dominant archive, an archive of power and oppression and computational text analysis is a positivistic technique that aggregates data. Is there a way to use computational text analysis not only to mine the archive but to subvert it? For "productively mining archival silences" and discursive methodology that challenges the archive, see Fuentes, *Dispossessed Lives*, 5--6. For a close reading of the Royal African Company Rawlinson corpus to analyze the commodification of African individuals see, Smallwood, *Saltwater Slavery*. For the importance of considering macro techniques in light of methodological advances in microhistory, see Lemercier and Zalc, *Quantitative Methods*, 1--27. For a reflection on the tradeoff between close reading and large-scale analysis and the limits of our methodology, see "An Analog Historian in a Digital World," <racnetworks.wordpress.com>.

[^8]: For the classic view of the Royal African Company, see Davies, *Royal African Company*.

[^9]: Eltis, “Relative Importance," 237--249.

[^10]: Some of the de-aliasing challenges we faced were similar to those faced by the TOFLIT project. Charles, Daudin, and Girard, "The treatment of merchandises in the toflit18 datascape."

[^11]: The de-aliasing process had limits, which in and of itself was revealing. For example we could not collapse the Dutch fort of Elmina, which the English sometimes referred to as "the Mine" with the word "mine" because "mine" also denotes possession. Our analysis thereby privileges certain words. In some cases we could also write a straightforward rule---for example to treat an initial "ff," as in "ffort" as a single "f," but in other cases, we could not---for example to treat a final double "ll," as a single "l," because this would correctly render "fatall" as "fatal," but incorrectly render "well" as "wel."In a future iteration of this project, we will go further with dealiasing. However we feel comfortable to begin to draw some conclusions. Our alias lists are available upon request. 

[^12]: For the secondary literature, we used maps from Kea, *Settlements, Trade and Polities*, and Thornton, *Africa and Africans*. For the historic maps, we used "A new and correct map of the coast of Africa : from Cape Blanco lat. 20°40'. N. to the coast of Angola lat. 11°. S.: with explanatory notes of all the forts and settlements belonging to the several European powers," William Smith, (Undated). "A New Map of the Coast of Guinea from Cape Mount to Iacquin," in Thirty Different Drafts of Guinea, London, and  Luis Teixeira (1602) "Effigies ampli Regni auriferi Guineae in Africa siti." <https://exhibits.stanford.edu/renaissance-exploration/catalog/wd588vc7077>.  Even in instances when we found historic sites documented on rare maps, we faced considerable difficulty in attempting to georeference those sites in latitude and longitude degrees. Each historic map, along with those used the secondary literature, were created in different projection systems, and those coordinate systems were not documented or made public. We therefore performed a series of tests for each scanned map, scaling and stretching each one to best fit the existing shoreline of the African continent.

[^13]: *Trans-Atlantic Slave Trade Database*. We are grateful to David Eltis for sharing his geocodes with us. 

[^14]: Our analysis adds further weight to the idea that transatlantic slavery grew out of African systems of slavery. We deliberately kept slave and slaves apart because the meaning of an individual enslaved person in the corpus may be different than the meaning of multiple enslaved people. It is worth noting that the slaves-gold gap decreases when analyzing words on a per-letter basis, meaning that fort factors mentioned slaves more frequently in a single letter.

[^15]: The frequency of some words in the corpus is misleading, due to double meanings. The word, captain, for example, refers to a ship captain, but captain was also the honorific that the Royal African Company used with its African agents. Says can refer to both the form of speech and a textile trade good. A future iteration of this project might be able to resolve some of these ambiguities. 

[^16]: An exception to several trends is the word, palaver, which according to Robin Law, denotes a discussion or disagreement. Law, *The English*, Vol III: xvi. Palaver shows a higher percentage in forts: About ten percent of all fort letters are mentioning some sort of dispute or discussion in the background. Palaver also appeared consistently throughout the year.

[^17]: A foundational explanation of Word2Vec can be found at, Mikolov, et al., "Distributed Representations." 

[^18]: The trading log of the Suzanne Marguerite out of La Rochelle offers a clear example of assortment bargaining. Journal de traite commencé à la rivière St.-André, Côte d'Afrique le 26 février 1775 à l'usage du navire "La Susanne Marguerite,'" EE 280, Archives Municipales de La Rochelle. For an analysis of assortment bargaining in the transatlantic slave trade, see Ruderman, "Supplying the Slave Trade." 

[^19]: The weak co-occurrence of trade goods merits further investigation. Just because trade goods do no co-occur in letters does not necessarily mean they did not co-occur in transactions between RAC factors and their African trading partners. The company may have also had different trading patterns for gold and for slaves. The mechanism of assortment bargaining was already in use among the Portuguese in West Central Africa by the mid-seventeenth century, where the assortment called a banzo, was, according to Linda Heywood, "the set of trade items equivalent to one slave." Heywood, *Njinga of Angola*, 173. It is worth noting that the words assortment and assorted and their aliases do not appear in the corpus, although the words sort and sorts and their aliases appear over 80 times. 
