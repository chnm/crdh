---
title: "Quantitative and Qualitative Approaches to the Development of Darwin’s Origin of Species"
doi: "https://doi.org/10.31835/crdh.2018.14"
volume-number: 1
year: 2018
date: 2018-08-27
authors:
- last: Murdock
  first: Jaimie
  email: jammurdo@indiana.edu
  affiliation: "School of Informatics, Computing, and Engineering, Indiana University"
  orcid: 0000-0002-1732-5499
  url: "http://www.jamram.net/"
- last: Allen
  first: Colin
  email: colallen@indiana.edu
  affiliation: "Department of History and Philosophy of Science, Indiana University"
  orcid: 0000-0003-4497-1725
  url: "http://colinallen.dnsalias.org/"
- last: DeDeo
  first: Simon
  email: sdedeo@andrew.cmu.edu
  affiliation: "Social and Decision Sciences, Carnegie Mellon University"
  orcid: 0000-0002-5346-9393
  url: "http://tuvalu.santafe.edu/~simon/"
abstract: |
  From 1837, when he returned to England aboard the <em>HMS Beagle</em>, to 1860, just after publication of <em>The Origin of Species</em>, Charles Darwin kept detailed notes of each book he read or wanted to read. His notes and manuscripts provide information about decades of individual scientific practice. Previously, we trained topic models on the full texts of each reading, and applied information-theoretic measures to detect that changes in his reading patterns coincided with the boundaries of his three major intellectual projects in the period 1837–1860. In this new work we apply the reading model to five additional documents, four of them by Darwin: the first edition of <em>The Origin of Species</em>, two private essays stating intermediate forms of his theory in 1842 and 1844, a third essay of disputed dating, and Alfred Russel Wallace’s essay, which Darwin received in 1858. We address three historical inquiries, previously treated qualitatively: (1) the mythology of “Darwin’s Delay,” that despite completing an extensive draft in 1844, Darwin waited until 1859 to publish <em>The Origin of Species</em> due to external pressures; (2) the relationship between Darwin and Wallace’s contemporaneous theories, especially in light of their joint presentation; and (3) dating of the “Outline and Draft” which was rediscovered in 1975 and postulated first as an 1839 draft preceding the Sketch of 1842, then as an interstitial draft between the 1842 and 1844 essays.
preview: "/assets/img/v01/murdock/preview.png"
---

From 1837, when he returned to England aboard the HMS Beagle, to 1860, just after publication of *The Origin of Species, Charles Darwin kept detailed notes of each book he read or wanted to read. His notes and manuscripts provide information about decades of individual scientific practice. The textual nature of these records make them particularly amenable to computational analysis.

Previously,[^1] we located digitized versions of the English-language, non-fiction works listed as read in Darwin’s reading notebooks. We trained topic models on the full texts of each reading, without using any information about his publications or additional historical metadata. We applied information-theoretic measures to the topic models of Darwin’s readings to detect that changes in his reading patterns coincided with the boundaries of his three major intellectual projects in the period 1837--1860: a first shift in 1846 from his Beagle research journals to describing the Cirripedia---his “beloved barnacles”---and a second shift in 1854 from barnacles to the work leading to *The Origin of Species* in 1859. While these intellectual phases are well-known to historians, the model offered a novel contribution by highlighting what changed in Darwin’s reading habits: as he prepared his notes for the “large work on species,” his readings became more exploratory; i.e., as he was organizing his species notes his readings shifted subjects more often than when assembling his Beagle and Cirripedia notes.

In this new work we apply the reading model to five additional documents, four of them by Darwin: the first edition of *The Origin of Species*, two private essays stating intermediate forms of his theory in 1842 and 1844, a third essay of disputed dating, either preceding or succeeding the 1842 essay, and Alfred Russel Wallace’s essay, which Darwin received in 1858. After describing the models and what they can show about the relationship between Darwin’s writings and his readings over the course of his investigations, we address three historical inquiries, previously treated qualitatively:

1. the mythology of “Darwin’s Delay,” that despite completing an extensive draft in 1844, Darwin waited until 1859 to publish *The Origin of Species* due to external pressures;[^2]

2. the relationship between Darwin and Wallace’s contemporaneous theories, especially in light of their joint presentation;[^3] and

3. the dating of the “Outline and Draft” which was rediscovered in 1975 and postulated first as an 1839 draft preceding the Sketch of 1842,[^4] then as an interstitial draft between the 1842 and 1844 essays.[^5]

### 1. Query Sampling the Writings

Our starting point for answering these questions was the previously trained topic model of his readings, as we were interested in how the readings may have influenced the writings. Topic models represent each text as a blend of different topics, with each topic being a probability distribution over the words in the collection. The models are statistically derived from a set of texts through joint inference of their word-topic and topic-document distributions.[^6] Query sampling allows a mixture of topics from a prior model to be assigned to documents not in the original training set. An initially random assignment of the words to the topics is revised iteratively until the assignment stabilizes using the same method used to train the original model. Because random starting points put the algorithm on different paths in the complex terrain, running the query sampling process multiple times leads to different topic distributions for the same text.

This variability in outputs is something to be understood and harnessed, not feared, supporting different perspectives on the text.[^7] For any text, there is not claimed to be a single “correct” interpretation but rather a set of interpretations in dialog with one another. Digital methods can augment existing debates in the humanities by providing different ways of looking at the text.

We approach the diversity of the sampled results by applying a clustering algorithm to the topic distributions, using the silhouette method to choose the number of clusters.[^8] For *The Origin*, this method detects eight clusters, shown in figure 1. Each cluster has a different highest-probability topic. These dominant topics characterize the primary interpretation of the text for each cluster. Inspection of the topics reveals that they are immediately applicable to *The Origin*. For example, pigeons (T49) provide a significant example for Darwin. The dominant topic of the largest cluster (T84) captures some key theoretic concerns with the words ‘’‘development,” “creation,” “geological,” “organic.”

{% figure caption: "Figure 1: Cluster Analysis of *The Origin of Species* — This “violin” plot shows the distribution of perplexity (fit to the document) by topic cluster for *The Origin of Species*. The number below each cluster shows the number of samples classified in that group, and the surface area is proportional to this number. The horizontal line in the center of each violin shows the median perplexity, while the vertical lines span the outliers in each cluster." %}
![alt-text]({{site.url}}/assets/img/v01/murdock/perplexity.png)
{% endfigure %}

Because the topics fit to *The Origin* by query sampling are derived from the model of the readings, some of the words that have a high probability for a topic in the readings are likely not to appear in *The Origin* at all. For example, the second most likely word in T84, “moral” does not appear in the first edition of *The Origin*. Likewise, some of the geographic terms prominent in T177 do not appear in the book. Indeed, T177 (with terms related to forests and South Asian geography and culture) presents an idiosyncratic view of *The Origin*. The information-theoretic “perplexity” of this cluster with respect to the text confirms a relatively poor fit. Nonetheless, the assignment of T177 is grounded both in Darwin’s reading of Falconer’s Report on the teak forests of the Tenasserim provinces in 1853, and in his writing. Falconer is mentioned six times in the first edition of *The Origin*, and related issues are discussed in passages such as this, from chapter 5:

> [W]e have evidence, in the case of some few plants, of their becoming, to a certain extent, naturally habituated to different temperatures, or becoming acclimatised: ...trees growing at different heights on the Himalaya, were found in this country to possess different constitutional powers of resisting cold. Mr. Thwaites informs me that he has observed similar facts in Ceylon.

T177, like other clusters featuring geographical and ethnographic terms (T61, T135, T163), highlights how Darwin’s own travels, correspondence with other travelers, and reading their published accounts expanded the global range of his evidence.

### 2. Measuring Cognitive Surprise

We compared the writings to the readings and each other using an information-theoretic measure of cognitive surprise---Kullback-Leibler (KL) divergence[^9]---used in our previous study and which has proven successful in various cognitive science applications.[^10] Applied to the topic distributions derived by query sampling, KL divergence measures the extent to which the distribution of topics encountered in a new text violate the expectations based on the topic distributions in previously encountered texts.

KL divergence is an asymmetric measure, meaning that encountering B after A may generate a different amount of surprise than encountering A after B. Asymmetric measures are useful in many contexts: for example, travel time may be the more useful measure if it will take longer to climb a mountain than to go down it, even though the distance traveled in kilometers is the same. When a symmetric measure of distance between volumes is more appropriate, we use the symmetrical Jensen-Shannon distance (JSD), which is derived from the KL divergence and satisfies the mathematical properties of a distance metric.[^11]

### 3. Findings

#### 3.1 Explaining Darwin’s Delay
Darwin began drafting his theory long before he started organizing his notes in 1854. With two private essays written in 1842 and 1844, it is a historical curiosity that he would wait until 1859 to publish his work, especially as immediately after finishing the second essay he wrote to his wife, Emma, with an addendum to his will concerning publication instructions should he die before finishing his work.[^12] This period has become known as “Darwin’s Delay.”[^13] Theories about its cause include general fear of persecution,[^14] the anonymous 1844 publication of Vestiges of the Natural History of Creation[^15] highlighting gaps in Darwin’s argument,[^16] and extended illness.[^17] We provide evidence that is relevant to another explanation for the delay that has been proposed by others:[^18] Darwin simply needed more time to gather evidence and develop his argument.

We use KL-divergence to trace the increase in cognitive surprise through Darwin’s written presentations of his theory. Figure 2 shows that with respect to the set of readings at any given time, *The Origin* is significantly more divergent than either of the earlier essays, and that the 1844 essay is slightly more divergent from the readings than the 1842 version. Interestingly, however, the 1842 and 1844 essays are more divergent from Darwin’s readings at their respective times of writing, than *the Origin* is by 1859. This computational evidence, although not directly addressing his motivation, supports the claim that Darwin’s continued reading during the period between 1844 and 1859 was materially relevant to what he eventually wrote.

{% figure caption: "Figure 2: KL divergence between Darwin’s readings and writings — Vertical dashed lines indicate date of publication; horizontal dashed lines indicate divergence at the time of publication. *The Origin* diverges more from the readings-to-date than either of the two previous drafts at all time points. However, each successive draft diverges less from the readings-to-date at the time of writing." %}
![alt-text]({{site.url}}/assets/img/v01/murdock/divergence.png)
{% endfigure %}

#### 3.2 The rush to publish: Wallace’s essay
Irrespective of the reasons for Darwin’s delay, his sudden rush to publication is often attributed to the co-discovery of natural selection by Wallace, whose own essay “On the tendency of varieties to depart infinitely from the original type” was co-published with an excerpt of Darwin’s 1844 essay on 30 June, 1858. When Darwin received Wallace’s manuscript on 18 June, 1858, Darwin had already been organizing his notes for *The Origin* for four years. Writing to Lyell that same day, Darwin remarked on the impressive similarity to his earlier work:

> I never saw a more striking coincidence. If Wallace had my M.S. sketch written out in 1842 he could not have made a better short abstract![^19]

We take Darwin’s remark as both praising Wallace’s work and emphasizing how much further his own ideas had developed by 1858. Darwin’s observation indicated not just similarity between their work, but a specific similarity to his 1842 description of natural selection. The JSD measure[^20] partially captures Darwin’s observation: Wallace’s work is more similar to the 1842 and 1844 essays than to *The Origin*. However, it is marginally—just over 1∕100th of a bit—closer to the 1844 essay than the 1842 essay by this measure (top of figure 3). Darwin’s mention of his 1842 sketch may be interpreted as a generic reference to the earlier period, or it may reflect features of the 1842 sketch not accessible via topic modeling.

#### 3.3 Dating the “Outline and Draft”
Finally, we look at a manuscript originally discovered with the 1842 essay at the Darwin residence in 1896, but which was not included in *The Foundations of the Origin of Species* in 1909.[^21] It had fallen into archival obscurity at the Cambridge University Libraries until rediscovered in 1975 by Peter Vorzimmer, who dated the outline to July 1839.[^22] However, scholarly consensus gravitated to a theory that the paper was an interstitial draft between the 1842 and 1844 essays,[^23] based upon annotations on the manuscript itself and the reuse of headings from the draft in the 1844 essay which were not present in the 1842 sketch. Comparing it using JSD, we find that the draft is further from *The Origin* than either the 1842 sketch or 1844 essay (bottom of figure 3). Moreover, the 1842 essay is further from *The Origin* than the 1844 essay. This finding provides some new evidence supporting Vorzimmer’s 1839 dating, although further investigation is necessary.

{% figure caption: "Figure 3: Similarity between Wallace and Darwin’s writings — These heatmaps show the Jensen-Shannon Distance (JSD) between Darwin’s various writings and Wallace’s manuscript. Top: Wallace’s text is closer to the two earlier writings than to *The Origin*. Bottom: The “Outline and Draft” is closest to the Sketch of 1842 and farthest from *The Origin*, indicating it may have been the earliest writing." %}
![alt-text]({{site.url}}/assets/img/v01/murdock/jsd.png)
{% endfigure %}

### 4. Linking Quantitative and Qualitative Analyses

Measurements and models alone do not yield historical explanations. For historians, they require validation through traditional methods, including close readings of the texts. As described above, our silhouette analysis of different clusters of topics in *The Origin* led us to look at Darwin’s text in ways we might otherwise have ignored. Similarly, our analysis of the changing semantic relations between Darwin’s reading and writing through his “delay” can be used to guide close reading of those portions of his work which are most similar to his post-1844 readings. Finally, our findings about the distances among the undated draft, the two essays, and *The Origin* likewise motivates new close readings of them all, with the goal of understanding why the topic models locate the undated draft as closest to the 1842 essay yet furthest from *The Origin*. By linking quantitative and qualitative analyses, these new methods in digital history have the potential to transform the historiography of intellectual influence.

---

### Bibliography

Allen, Colin, et al. “Topic Modeling the Hàn Diăn Ancient Classics.” *Journal of Cultural Analytics* (12 October 2017). <https://doi.org/10.22148/16.016>. 

Blei, David M. “Probabilistic Topic Models.” *Communications of the ACM* 55, no. 4 (April 2012): 77--84, <https://doi.org/10.1145/2133806.2133826>.

Browne, E. Janet. *Charles Darwin: Voyaging*. New York: Knopf, 1995.

Browne, E. Janet. *Darwin's Origin of Species: A Biography* Books That Changed the World. Starke, FL: Atlantic, 2006.

Chambers, Robert. *Vestiges of the Natural History of Creation*. London: John Churchill, 1844.

Costa, James T. *Wallace, Darwin, and the Origin of Species*. Cambridge, MA: Harvard University Press, 2014.

Darwin, Charles. *The Foundations of the Origin of Species: Two essays written in 1842 and 1844*. Edited by Francis Darwin. Cambridge University Press, 1909.

Fuglede, Bent, and Flemming Topsøe. “Jensen-Shannon Divergence and Hilbert Space Embedding.” *International Symposium on Information Theory Proceedings* (2004): 31. <https://doi.org/10.1109/ISIT.2004.1365067>.

Gruber, Howard E., and Paul H. Barrett. *Darwin on Man: A Psychological Study of Scientific Creativity*. Boston: EP Dutton, 1974.

Kohn, David, Robert C. Stauffer, and Sydney Smith. “New Light on *The Foundations of the Origin of Species*: A Reconstruction of the Archival Record.” *Journal of the History of Biology* 15, no. 3 (September 1982): 419--442, <https://doi.org/10.1007/BF00133145>.

Kullback, Solomon, and Richard Leibler. “On Information and Sufficiency.” *Annals of Mathematical Statistics* 22, no. 1 (March 1951): 79--86. <https://doi.org/10.1214/aoms/1177729694>.

Lin, Jianhua. “Divergence Measures Based on the Shannon Entropy.” *IEEE Transactions on Information Theory* 37, no. 1 (January 1991): 145--151. <https://doi.org/10.1109/18.61115>.

Merton, Robert K. “Priorities in Scientific Discovery: A Chapter in the Sociology of Science.” *American Sociological Review* 22, no. 6 (1957): 635--659. <https://doi.org/10.2307/2089193>.

Murdock, Jaimie, Colin Allen, and Simon DeDeo. “Exploration and Exploitation of Victorian Science in Darwin’s Reading Notebooks.” *Cognition* 159 (2017): 117--126. <https://doi.org/10.1016/j.cognition.2016.11.012>.

Nielsen, Frank. “A Family of Statistical Symmetric Divergences Based on Jensen’s Inequality.” arXiv:1009.4004, 2010.

Richards, Robert J. “Myth: That Darwin Worked on His Theory in Secret for Twenty Years, His Fears Causing Him to Delay Publication.” In *Textbook Myths about Science*, edited by Ronald Numbers, Kostas Kampourakis and Nicolaas Rupke. Harvard University Press, 2015.

Rockwell, Geoffrey, and Stéfan Sinclair. *Hermeneutica* Cambridge, MA: MIT Press, 2016.

Rousseeuw, Peter J. “Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis.” *Journal of Computational and Applied Mathematics* 20 (1987): 53--65, <https://doi.org/10.1016/0377-0427(87)90125-7>.

Schweber, Silvan S. “The Origin of the 'Origin' Revisited.” *Journal of the History of Biology* 10, no. 2 (September 1977): 229--316. <https://doi.org/10.1007/BF00572644>.

University of Cambridge. Darwin Correspondence Project. <https://www.darwinproject.ac.uk/>. 

Van Wyhe, John. *Dispelling the Darkness: Voyage in the Malay Archipelago and the Discovery of Evolution by Wallace and Darwin*. Singapore: World Scientific, 2013.

Van Wyhe, John. “Mind the Gap: Did Darwin Avoid Publishing His Theory for Many Years?.” *Notes and Records of the Royal Society* 61, no. 2 (2007): 177--205. <https://doi.org/10.1098/rsnr.2006.0171>.

Vorzimmer, Peter J. “An Early Darwin Manuscript: The 'Outline and Draft of 1839'.” *Journal of the History of Biology* 8, no. 2 (September 1975): 191--217. <https://doi.org/10.1007/BF00130438>.

---

### Notes

[^1]: Murdock, Allen, and DeDeo, “Exploration and Exploitation of Victorian Science," 117--126.

[^2]: Gruber and Barrett, "Darwin on Man"; Browne, *Darwin’s Origin of Species*; Van Wyhe, “Mind the Gap,” 177--205; Richards, “Myth.”

[^3]: Merton, “Priorities in Scientific Discovery," 635--659; Van Wyhe, *Dispelling the Darkness*; Costa, *Wallace, Darwin, and the Origin of Species*.

[^4]: Vorzimmer, “An Early Darwin Manuscript," 191--217.

[^5]: Schweber, “The Origin of the “Origin” Revisited,” 229--316; Kohn, Stauffer, and Smith, “New Light on the Foundations of the Origin of Species," 419--442.

[^6]: Blei, “Probabilistic Topic Models,” 77--84.

[^7]: Rockwell and Sinclair, *Hermeneutica*; Allen et al., “Topic Modeling the Hàn Diăn Ancient Classics.”

[^8]: Rousseeuw, “Silhouettes," 53--65.

[^9]: Kullback and Leibler, “On Information and Sufficiency,” 79--86.

[^10]: For examples see Murdock, Allen, and DeDeo, “Exploration and Exploitation of Victorian Science.”

[^11]: Lin, “Divergence Measures Based on the Shannon Entropy,” 145--151; Nielsen, “A Family of Statistical Symmetric Divergences”; Fuglede and Topsøe, “Jensen-Shannon Divergence,” 31.

[^12]: Letter to Emma Darwin of 5 July, 1844, Darwin Correspondence Project, University of Cambridge. <https://www.darwinproject.ac.uk/letter/?docId=letters/DCP-LETT-761.xml>.

[^13]: Van Wyhe, “Mind the Gap.”

[^14]: Gruber and Barrett, *Darwin on Man*.

[^15]: Chambers, *Vestiges*.

[^16]: Browne, *Charles Darwin*.

[^17]: Gruber and Barrett, *Darwin on Man*; Wyhe, “Mind the Gap"; Richards, “Myth.”

[^18]: Van Wyhe, “Mind the Gap”; Richards, “Myth.”

[^19]: Letter to Charles Lyell of 18 June, 1858, Darwin Correspondence Project, <https://www.darwinproject.ac.uk/letter/?docId=letters/DCP-LETT-2285.xml>.

[^20]: We use the symmetric JSD rather than KL-divergence, as JSD does not make any assumption about ordering of texts.

[^21]: Darwin, *The Foundations of the Origin of Species*.

[^22]: Vorzimmer, “An Early Darwin Manuscript.”

[^23]: Schweber, “The Origin of the 'Origin' Revisited”; Kohn, Stauffer, and Smith, “New Light on the Foundations of the Origin of Species.”
