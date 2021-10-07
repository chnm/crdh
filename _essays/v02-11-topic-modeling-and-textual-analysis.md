---
title: "Topic Modeling and Textual Analysis of American Scientific Journals, 1818–1922"
doi: "https://doi.org/10.31835/crdh.2019.11"
volume-number: 2
year: 2019
authors:
- last: Martin
  first: Shawn
  email: Shawn.J.Martin@Dartmouth.edu
  affiliation: "Dartmouth College Library"
  orcid: 0000-0002-9128-5528
  url: "https://shawnmartin.net/"
abstract: |
  When performing a distant reading of some of the most prominent American scientific publications in the nineteenth-century U.S., some very clear patterns emerge. LDA topic modeling and textual analysis methods of over one hundred years of the American Journal of Science (AJS), Proceedings of the American Association for the Advancement of Science (PAAAS), and the Journal of the American Chemical Society (JACS) between 1818 and 1922 helps historians to understand how these journals evolved over the nineteenth-century. Overall, there was an increase in discussion of business and professional issues and a shift in the journals that scientists used to discuss these issues. This shift happened during a very specific period, 1870-1890, the very same time that specialized scientific societies, particularly the American Chemical Society, split from the more generalized American Association for the Advancement of Science. Further analyses of these datasets may help to better understand shifts American science in the nineteenth century, and topic modeling methods allow historians of science to better identify this evolution of American science.
appendix:
- name: README
  file: martin-v02/README.txt
- name: Data archive
  file: martin-v02/martin-data.zip
preview: "/assets/img/v02/martin/preview.png"
---

### Introduction

How did science, as reflected in contemporary journals, change in the
U.S. during the nineteenth century? In 1818 The *American Journal of
Science* (AJS) was first American scientific journal published. The
*Proceedings of the American Association for the Advancement of Science*
(PAAAS) was published between 1848 and 1914 and also served as a news
source, especially for news of the association. The *Journal of the
American Chemical Society* (JACS) was first published in 1879, but it
was not until the 1890s that JACS began to serve as a news source for
the American Chemical Society and a space for discussion of theory and
method in chemistry.

The differences between the content of these three journals can help
both historians of science and academic publishing how American
scientific journals evolved from sources of news to providers of
original research over the course of the nineteenth century. Using
general topic modeling to analyze the content of the major American
scientific journals in the nineteenth century reflect some general
scientific trends. In the mid-1890s, chemistry separated as a discipline
from the more generalized American Association for the Advancement of
Science, and consequently decreased as a topic within the more
generalized scientific journals. In all, this shift in topics over time
serve as evidence about American science in the nineteenth century.

### Historiography

The changes in these journals over the course of the nineteenth century
reflect many of the developments noted by researchers studying journal
publication. Alex Csiszar has focused on scientific publishing in
Britain and France during the nineteenth century, and Melinda Baldwin
has concentrated on a case study of one particular journal, *Nature*,
that started in 1869. According to Csiszar, British scientific journals
attempted to address "the *failure* of the authority of the collectives
that had traditionally adjudicated the boundaries of scientific
authority."[^1] Csiszar also argues that during the nineteenth century,
there was a greater interest among scientists to create a sense of
objectivity in the articles that they were writing.[^2] Furthermore
Csisizar argues that expert communities of authors were becoming
specialized.[^3] Melinda Baldwin's work complements Csiszar's points
about the increasing demand by audiences for scientific content. Over
the course of the century, *Nature* became a specialized scientific
journal similar to what Csiszar generally describes.[^4]

In the United States, the same trends hold, though in different ways.
There was only one major scientific journal published consistently
throughout the nineteenth century in the U.S. According to Simon Baatz,
the *American Journal of Science*, was largely a general science journal
able to bring together divergent metropolitan groups in cities like New
York, Philadelphia, and Boston in ways that more localized journals such
as the *Transactions of the American Philosophical Society* were
not.[^5]

### Methodology for Analyzing Journals

To perform an effective distant reading of these three journals (AJS,
PAAAS, and JACS), I performed several steps. After obtaining electronic
copies of individual years of the journal, I created full text for these
files. These three journals contained 209 text files (one text file for
every year the journal published until 1922) and about seventy-three
million words. These text files contain the entirety of the dataset used
for this paper. I then obtained the OCR of the individual years, and
used Mallet, a topic modeling tool that analyzes words via a Latent
Dirichlet Allocation (LDA) model.

Rather than performing an analysis of an entire year, initially, the
goal was to separate out the articles, and to compare individual
articles. Unfortunately, after repeated experiments, it became clear
that the structure of the journal was too inconsistent to be able to
separate out individual articles using computational methods, much of it
would need to be done manually.

Simon Baatz's article was valuable as a guide for creating categories of
content in our study of AJS and PAAS. Baatz discusses some of the
historical developments with the journal as well as some of the larger
social issues that Benjamin Silliman faced when he was managing the
journal.To obtain the content categories, topic models were created for
every year individually and each topic model created a list of 40 topics
(or lists of related keywords) for each year. These topics were assigned
to 17 categories. These categories included disciplines such as
astronomy or chemistry, genres of articles such as geographical and
coastal surveys, and broader discussions on issues such as publishing,
theory, and news. The "other" category represents either topics that
appear infrequently, for instance there are some music articles that
appear early in the journal's run such as music; additionally "other"
represents topics that could not accurately be identified. After
creating these categories, the number of times each category appeared
during a given year were counted. These categories were then grouped
into spans of 25 years so that some of the math for word counts would
even out and to allow both for more direct comparison and for a smoother
graphical representation of change over time in the visualizations.
These changes allowed for clearer visualizations of the dataset.

After obtaining initial topic models from Mallet, I categorized and
visualized the topics in spreadsheets so that it was possible to create
graphs for each of the three journals and to compare how the three
journals differed and how they changed over time. I performed initial
analysis with yearly topic models rather than with individual articles.
This initial analysis proved useful because the models could test the
general theory of how journals did (or did not become) more specialized
during the nineteenth century.[^6]

***Categories Used for Comparison of Scientific Areas***

| Original Category | New Category |
|---|---|         
| Astronomy | Other Science |
| Botany | Other Science |
| Chemistry | Chemistry |
| Engineering | Other Science |
| Fossils | Geology |
| Geology/Mineralogy | Geology |
| Geography/Survey | Geology |
| Geography/Coastal | Geology |
| Mathematics | Other Science |
| Medicine | Other Science |
| Meteorology | Other Science |
| News | News |
| Other | Other Science |
| Physics | Physics |
| Publishing | News |
| Theory/Method | Theory |
|Zoology/Biology | Other Science |

<figure>
<figcaption>Table 1. This table shows the categories into which I originally placed
topics and the broader categories I created to more easily compare
different areas of science. Topics of Fossils, Geology/Mineralogy,
Geography/Survey, and Geography/Coastal were joined into a single
"Geology" category. I also combined news and publishing into a single
category of "news." Finally, I put together all of the other disciplines
into the "other sciences" category. Chemistry remained as a single
category as well as Theory/Method, and Physics.
</figcaption>
</figure>

AJS and PAAAS were more directly comparable. Both of these publications
produced generalized scholarship and were not specialized. Therefore,
the topic models from Mallet often mapped to disciplines such as geology
or chemistry. It was more difficult to compare JACS directly to AJS or
PAAAS. JACS was a specialized journal for chemistry. However, by
creating a topic list of twenty topics for each year of JACS between
1879 and 1922, a historical analysis using Browne's (1952) history of
the American Chemical Society, was employed to organize the data; this
volume is still the most comprehensive account of the history of the
American Chemical Society for the early period (1879-1922) of the
society. Browne's history also contains a history of JACS and an
analysis of the topics contained within the journal. Topics produced by
Mallet were organized into "chemistry" topics, or topics that were
mentioned in Browne's section on the chemistry topics appearing in the
JACS, and "other" topics, or topics that are largely discussing business
and professional issues that are not discussed in Browne's section
regarding JACS. Chemistry topics are largely related to chemical
experiments. Unexpected topics usually contain words like "president,
election, or committee" and often refer to the business of the society,
methodology of chemistry, or other professional issues.

### Journal Comparisons

The topic models demonstrate some interesting trends that accord with
what we know about these journals through other means. Figure 1 shows
that the journal becomes more specialized in geology and this may be
evidence of scientists of the increasing specialization of AJS and
leaving the more generalized journal for more specialized journals as
they are created in the later nineteenth century. Figure 2 shows similar
trends for the PAAAS. PAAAS and AJS also seem to illustrate Baatz's
argument that American scientific journals in the nineteenth century
were an important news source for scholars scattered throughout
universities in the U.S. In the case of PAAAS, its purpose as a news
source is much more pronounced and business of the society represents a
very large proportion of topics throughout the publication of PAAAS. In
Figure 3, the topics dedicated to professional issues double during the
tenure of one particular editor after 1890, perhaps because there was no
generalized journal (such as AJS or PAAAS) to discuss such issues.

{% figure caption: "Figure 1. This line graph shows the number of topics within categories and that geology topics increase over time, whereas other topics generally decrease. The
graph also shows that until about 1871, “other sciences” were
significantly higher than geology. Also, in 1871 “other sciences”
decline precipitously and geological topics increase and overtake “other
sciences.”" %}
![Line graph charting the change over time in the number of topics in six categories: Geology, Chemistry, Physics, Theory, News, and Other Sciences.]({{site.url}}/assets/img/v02/martin/figure1.jpg)
{% endfigure %}

{% figure caption: "Figure 2. This chart shows the percentage of topics over time in PAAS. This
graph illustrates PAAAS' publication of theory more clearly. Within
PAAAS theory is never less than 10% and often represents more than 20%
of topics within particular years." %}
![Graph showing the percentage of topics in the *Proceedings of the American Association for the Advancement of Science* between eighteen forty-eight and nineteen fourteen. Theory is especially prevalent.]({{site.url}}/assets/img/v02/martin/figure2.jpg)
{% endfigure %}

{% figure caption: "Figure 3. This line graph shows the percentage of topics on business and theory over time in JACS. Such topics were consistently a small number of topics in
any given year (less than 20% of all topics). Nonetheless, the
unexpected topics doubled during the tenure of one particular editor in
the years 1890--1892, from 10% to 20% of topics, and that increase
stayed consistent until the end of the dataset in 1922." %}
![Line graph showing the percentage of topics on business and theory over time in *Journal of the American Chemical Society* between eighteen nineteen and nineteen twenty-two.]({{site.url}}/assets/img/v02/martin/figure3.jpg)
{% endfigure %}

### Conclusion

American journals in the nineteenth century largely reflect professional
trends within the disciplines they served. AJS was one of the most
important means of distributing scientific information during much of
the nineteenth century. AJS was not under the control of any society,
but rather under the control of one of the most prominent scientists at
the time, Benjamin Silliman. Silliman's journal, as AJS was called,
started out as a news source for many scientific practitioners around
the United States; it also specialized in geology, the most popular
scientific discipline at the time. Though Silliman's journal published
articles many disciplines like astronomy and physics, by the twentieth
century it specialized entirely in geology. PAAAS, a journal that
overlapped with AJS in its period of publication (until it ceased
publication in 1914), is quite similar to AJS. PAAAS also published
articles about many different disciplines but served even from its
inception as a news distributor for the society. Unlike AJS, however,
PAAAS became entirely devoted to news (mostly contact information about
members of the society) by the twentieth century, whereas AJS became
more dedicated to articles about geology and less interested in
distribution of news.

JACS combined many of the characteristics of both AJS and PAAAS. JACS
specialized in publishing about chemistry from its inception. News and
professional topics were a rather small, but consistent, part of what
JACS was publishing. Over time, however, it becomes clear that chemistry
as a topic declined in both AJS and PAAAS. More importantly, this
decline happens at exactly the same time ACS forms its own society
separate from AAAS, perhaps suggesting that JACS became a more important
source for discussion of chemistry topics. Additionally, topics covering
professionalization and news increased at the same time. In all, one can
begin to understand the evolution of scientific topics in this
preliminary analysis of some of the United States' most prominent
nineteenth-century scientific journals.

---

### Bibliography

Baatz, Simon. "Squinting at Silliman: Scientific periodicals in the early American republic, 1810-1833." *Isis* 82, no. 2 (1991): 223--244. <https://doi.org/10.1086/355726>.

Baldwin, Melinda. *Making Nature: The History of a Scientific Journal*. Chicago: University of Chicago Press, 2015.

Browne, Charles Albert. *A History of the American Chemical Society: Seventy-five Eventful Years*. Easton, PA: Mack Printing Company, 1952.

Csiszar, Alex. "Objectivities in Print." In *Objectivity in Science: New Perspectives from Science and Technology Studies*, edited by Flavia Padovani, Alan Richardson, and Jonathan Tsou, 145--172. New York, NY: Springer, 2015.

Csiszar, Alex. *The Scientific Journal: Authorship and the Politics of Knowledge in the Nineteenth Century*. Chicago: University of Chicago Press, 2018.

Csiszar, Alex. "Seriality and the search for order: Scientific print and its problems in the nineteenth century." *History of Science* 48, no. 3–-4 (September 2010): 399--434. <https://doi-org/10.1177/007327531004800306>.

Gross, Alan G., Joseph E. Harmon, and Michael Reidy. *Communicating Science: The Scientific Article from the 17th Century to the Present*. Oxford: Oxford University Press, 2002.

---

### Notes

[^1]: Csiszar, “Seriality,” 426.

[^2]: Csiszar, “Objectivities in Print,” 165.

[^3]: Csiszar, *The Scientific*, 8.

[^4]: Baldwin, *Making Nature*, 21.  

[^5]: Baatz, “Squinting at Silliman,” 223.

[^6]: Overall, these three journals combined contain 209 text files (one text file for every year the journal published until 1922) and about seventy-three million words.  These text files contain the entirety of the dataset used for this dissertation. Two topic modeling analyses were run on this dataset. First, an initial topic model of forty topics utilizing Mallet was performed on each of the 209 text files (or years) and compared between the journals, these topic models were then categorized and visualized in spreadsheets so that it was possible to create visualizations for each of the three journals and to compare those visualizations to see how the three journals differed and how they changed over time. After performing this analysis, a second topic model was run on the entire corpus. For this topic model, each of the 209 text files were split into documents of 1,000 words and a 500 topic model was created to investigate the corpus as a whole. See Appendices for topic models.
