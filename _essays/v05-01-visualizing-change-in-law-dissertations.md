---
title: "Visualizing Generational Change in Early Modern Law Dissertations"
subtitle: ""
doi: "https://doi.org/10.31835/crdh.2022.01"
volume-number: 5
year: 2022
date: 2022-04-18
authors:
- last: Scholz
  first: Luca
  email: luca.scholz@manchester.ac.uk
  affiliation: "Department of Art History and Cultural Practices, University of Manchester"
  orcid: 0000-0001-5089-0089
  url: "https://lucascholz.com/"
abstract: |
  In the seventeenth century, German jurisprudence saw important thematic and methodological shifts. This article employs a novel visualization approach to ask whether these changes can be attributed to specific age cohorts or whether they were adopted across generations. Interrogating the metadata of over 20,000 legal dissertations defended at German universities, it visualizes relative frequencies of title keywords and decomposes them by the dissertation supervisors' age at the time of publication. The increasing use of bilingual titles that combined Latin and the German vernacular can be attributed to younger age cohorts who entered the profession after the end of the Thirty Years' War, nuancing explanations of shifts in early modern academic language as primarily driven by the intention and initiative of eminent individuals. In contrast, the sudden drop in mentions of *controversia* in the 1610s was a much broader and swifter cross-generational shift, possibly indicating a shared desire to avoid association with the increasingly established genre of confessional polemics. Finally, the late emergence of dissertation titles mentioning territory suggests that one of the most consequential legal-political concepts of the century faced more academic inertia than assumed and adds to our knowledge of the connection between career motives and subject choice.
appendix:
- name: README
  file: scholz-v05/README.txt
- name: Data archive
  file: scholz-v05/scholz-data.zip
preview: "/assets/img/v05/scholz/preview.png"
---

Scholars and students at early modern European universities wrote
hundreds of thousands of dissertations. These printed, mostly Latin
texts range from a few pages to over a hundred and accompanied oral
disputations, a common teaching format in which a professor or lecturer
(*praeses*) oversaw a student's (*respondens* or *defendens*) public
defense of theses against objections brought forward by an opponent
(*opponens*).[^1] Written in awkward Latin, poorly catalogued, and often
considered of mediocre intellectual quality, the dissertations were
rarely held in high esteem by historians.[^2] Taken as a whole, however,
the dissertations offer insights into the kinds of questions that the
anonymous mass of scholars that populated the faculties of law,
medicine, theology, and philosophy perceived as important. Collectively,
they allow us to retrace long-term shifts in the themes and methods of
entire academic disciplines.

Legal dissertations offer a window into the interests and methods of the
jurists that populated universities, courts, chanceries, and
administrations across the German lands. While those who worked with
these texts long tended to focus on individual scholars or subject
matters, distant reading approaches have allowed historians to reveal
long-term changes that remain hidden because of their sheer scale.[^3]
Recent studies were able to highlight, for example, an increasingly
specialized and topical engagement with imperial law,[^4] declining
interest in civil law in the seventeenth century,[^5], or a turn from
dialogic to more single-voiced, monographic forms of writing and
reasoning. One limitation of these studies, my own included, is that
their graphics often aggregate the data in ways that make it difficult
to identify the role played by different groups of authors. Change
appears as the effect of an abstract, anonymous, and non-aged
*Zeitgeist* rather than as the product of specific groups or
individuals.

This study asks whether and to what extent the jurists' age can help us
understand linguistic, methodological, and thematic shifts observed in
seventeenth-century jurisprudence. The seventeenth century is a
particularly interesting time frame for such an inquiry, because it was
a highly dynamic moment in the history of German jurisprudence, which
saw the creation of new universities across the Holy Roman Empire,
increasing interest in legal studies, and major thematic and
methodological shifts, including a declining interest in civil law and
the rise of monographic, single-voiced dissertations.

This article examines relative word frequencies in the titles of
seventeenth-century law dissertation titles and correlates them with the
age of the *praesides* at the time of publication. Following a breakdown
of the average age and volume of law dissertations supervised by the
*praesides*, the article turns to three conspicuous discontinuities
observed in this corpus, one at the beginning of the century, and two in
the years between the 1660s and 1680s.

To visualize the relationship between age cohorts and word frequencies,
the article combines demographic data and word frequencies in a
technique proposed by Benjamin Schmidt.[^6] The charts in this article
visualize the number of dissertations in black dots, with the years of
publication on the horizontal axis and the *praeses* age cohorts on the
vertical axis. A color palette from a light yellow to a dark green
indicates the proportion of dissertations whose titles contain specific
keywords, as detailed in the image captions. The dots' variable size
helps to gauge whether keyword frequencies are found in many or few
dissertations. Because the raw data is noisy and it would be difficult
to visually discern broader trends, the word frequencies were smoothed
with KDE (kernel density estimation). Schmidt, who applied this approach
to Open Library data, differentiated two ideal types of changing
vocabulary use: words that appear across all age groups simultaneously
and words that are introduced (and maintained) by young generations.
Changes that cut across age cohorts follow a vertical pattern: in figure
5, for example, scholars of all age cohorts published significantly
fewer dissertations framed as *controversia* within the range of a few
years. In contrast, more diagonal patterns, such as the ones in figures
3 and 6, indicate vocabulary use that was specific to particular age
cohorts: at a specific point in time, younger and middle-aged scholars
intensified their use of German vocabulary or introduced new keywords
while their elders did not. The graphics also evince a series of
outliers and more isolated developments that will not be discussed in
this article. While some of these point to interesting phenomena---such
as early mentions of "territory" in the first half of the century---I
limit the discussion to trends which are sustained and stand out either
because they become more widespread or because they appear as distinctly
new.

Schmidt limited his discussion of the age-cohort-language chart to a
blog post, suggesting it as a way of bringing back "people" into the
computational study of frequently anonymized literary corpora. In recent
years, scholars in the digital humanities and cultural analytics have
found productive ways of combining demographic data with text mining
that go well beyond the word frequency analysis employed in this paper.
Examples include Andrew Piper's *Enumerations*[^7] which sheds light on
the relationship between female authorship and gendered characterization
or Richard Jean So's study on cultural redlining which examines the role
of race in American post-war fiction.[^8] Some polemicists have argued
that cultural analytics' preference for "dimorphic traits"[^9] like
male/female or black/white and "time-variance arguments" has more to do
with a technical imperative to reduce complex data to second-order
classifications than with (literary) history. The claim is controversial
and in the case of age cohorts, inconsistent with a long vein of
scholarship.

Indeed, to historians, Schmidt's method should be of particular interest
because it brings a compelling visualisation technique to the study of
age cohorts, a strand of historical scholarship with a much longer
history. A key assumption in historical and sociological studies on
generations and age cohorts has been that shared experiences, parallel
biographies, and similar socialization generate a similar worldview in
members of the same age cohort. The notion of "generation" offers a
means to conceptualize asymmetries between "spaces of experience" and
"horizons of expectation," which Reinhart Koselleck saw as key to
understanding the intellectual and political upheavals of the
*Sattelzeit*.[^10] In a prominent recent example of generational
history, Michael Wildt investigated the leadership of the Reich Security
Main Office (RSHA), the agency responsible for enacting many aspects of
the Holocaust, as a generational cohort.[^11] Born between 1900 and 1910---too young to fight in World War I but old enough to be affected by
the experience of their older siblings and the economic crises and
political violence of the 1920s---Wildt argues that this generation
developed a worldview imbued by ruthless, soldierly, anti-bourgeois, and
antidemocratic values. This is just one of many examples for how
historians engage with the history of generations today.[^12]

Digital historical approaches like the one adopted in this paper can
contribute a new form evidence to this vein of scholarship. The charts
presented in this paper indicate how important developments were
initiated by specific age groups before being adopted by the broader
profession, but they also highlight much swifter changes across all age
groups. Drawing on close reading of metadata, primary sources and
secondary literature, the aim is also to contextualize, explain, and
highlight the historiographical significance of those shifts. Even in
cases where visualization alone is not sufficient to explain a
distinctive pattern (the *explanans*), the approach presented here
nuances assumptions and hypotheses formed through close reading and
evinces latent patterns that traditional research has been unable to
document. The result is a more detailed case of the *explanandum*,
another important way in which computational methods contribute to
argumentation and interpretation in historical research.[^13]

The study of age-cohort specific change also offers a way of making
generational modes of reasoning operable for computational distant
reading while addressing one of the approach's narrative challenges. In
contrast to the "precipitous, dramatic, breathless narrative"[^14] that
characterizes the short-term, micro-historical, agency-oriented
perspectives dear to close reading, *longue durée* perspectives, as
Braudel once put it, unfold in a "slowed time, sometimes almost at the
limits of movement."[^15] Where distant reading requires scholars "to
find meaning in small changes and slow processes,"[^16] the study of age
cohorts offers ways of organizing and interpreting a particularly
abstract kind of digital evidence in new ways.

At the same time, it is worth noting that historical scholarship on
generations has not always been uncontroversial. Historians and social
scientists who used "generation" as an abstract analytical category,
rather than as a self-characterization by historical subjects,
recurrently invested this approach with inflated hopes of re-writing the
laws of history. Critics argue that the results rarely amounted to more
than "banalities, tautologies, and unsubstantial speculation."[^17] More
successful than works characterized by sweeping generalizations and
argumentative overreach were studies of more modest scope which focused
on concrete groups or specific academic disciplines.[^18] Indeed, one of
the pioneers in this field, Karl Mannheim argued that in contrast to the
natural sciences where it was more difficult to observe generational
patterns, literature and the humanities were especially prone "to
promote the emergence of new entelechies,"[^19] i.e. specifically
generational worldviews.

Early modern dissertations are a particularly promising corpus from this
perspective, because they were authored by members of institutionally
stable yet intellectually dynamic academic disciplines. Early modern
contemporaries acknowledged the prevalence of generational conflicts and
geriarchic tendencies in the context of early modern disputations, where
young scholars could be penalized if they did not accept the ideas
professed by their seniors.[^20]

The data under consideration comes from VD17, a catalogue of prints from
German-speaking Europe in the seventeenth century.[^21] The metadata I
obtained includes the dates of birth for most *praesides*, which allowed
me to calculate their age at the time a dissertation was published.[^22]
While many of the roughly 20,000 legal dissertations listed in VD17 have
been digitized, full texts are not yet widely available. Ongoing
digitization efforts are paving the way for computational study of the
full texts;[^23] in the meantime, the hand-keyed metadata makes it
possible to conduct broader analyses of linguistic, methodological, and
thematic trends.[^24]

VD17 is far from complete, but it is the most comprehensive dataset
available, offering a unique window into this corpus.[^25] In the
selection for this study, more than 3700 duplicates and 600 reprints had
to be marked and excluded, as were all *praesides* without birth dates.
Entries in the data that only listed a *praeses* but no respondent were
also excluded from this study, leaving roughly 11,600 dissertations. In
many cases, these authors catalogued as *praesides* would more
appropriately be classified as respondents and their inclusion would
have skewed the observations.

The corpus under consideration has one characteristic that deserves
further discussion. The vast majority of early modern dissertations
features two authors: a presiding professor (*praeses*) and the
responding student (*respondens*).[^26] If both *praesides* and
respondents had contributed to the texts in equal shares, or if the
dissertations had been authored exclusively by the respondents, the
approach adopted in this study would be of limited value. However, in
practice, early modern dissertations were often written by the
*praesides* themselves: for professors and lecturers, dissertations
offered an opportunity to publish their work until that function was
later taken over by over by journals and periodicals.[^27] Even in cases
where a *praeses* did not write a text himself, it can be assumed that
he had a strong influence on and stake in its subject and content.

{% figure caption: "Figure 1. The average age of *praesides* increased from 39 to 44 in the course of the seventeenth century. Average age of *praeses* by publication year (ten-year moving average). Excluded: reprints, duplicates, entries with fewer than two authors, entries without *praeses* birth date. Data source: *Verzeichnis der im deutschen Sprachraum erschienenen Drucke des 17. Jahrhunderts* (2020)." %}
![A line graph entitled "Average Age of praeses" with year on the x-axis and the average age of praeses (moving average) on the y-axis. Blue line on a white background.]({{site.url}}/assets/img/v05/scholz/figure1.png)
{% endfigure %}

{% figure caption: "Figure 2. The majority of dissertations were supervised by *praesides* in their late twenties, thirties, and forties. Number of dissertations published by (*praeses*) age cohort. Excluded: reprints, duplicates, entries with fewer than two authors, entries without *praeses* birth date. Data source: *Verzeichnis der im deutschen Sprachraum erschienenen Drucke des 17. Jahrhunderts* (2020)." %}
![A line graph entitled "Dissertations Published by Age" with the age of praeses on the x-axis and the number of dissertations published on the y-axis. Blue line on a white background.]({{site.url}}/assets/img/v05/scholz/figure2.png)
{% endfigure %}

Age and publication averages for the *praesides* provide important
baselines for understanding the demography of this genre. In the
seventeenth century, the average age of a law dissertation supervisor
(*praeses*) in German universities was 41 years, though it increased
from 39 to 44 in the course of the century, as can be seen in figure 1,
with a surge during the Thirty Years' War, when the average age of a
*praeses* increased sharply and never returned to the pre-war levels.
Figure 2 suggests that the majority of dissertations were supervised by
*praesides* in their late twenties, thirties, and forties. Very young
*praesides* were not usually professors, but scholars who recently
earned their doctorate and were allowed exceptionally to preside over a
disputation to further their careers.[^28] From the age of 45 and
upward, the number of *praesides* decreased steadily, although some
scholars continued to preside over disputations well into old age.
Overall, these patterns are roughly in line with Mannheim's assumption
"that during the first 30 years of life people are still learning, that
individual creativeness on an average begins only at that age, and that
at 60 a man \[or woman\] quits public life."[^29]

### Bilingual Titles

Latin remained the dominant academic language in German universities
well into the nineteenth century. This is particularly true for
dissertations, one of the last "reservations of modern
*latinitas*."[^30] One can, however, observe a gradual increase of
vernacular elements during the seventeenth and eighteenth
centuries.[^31] In titles, a dissertation's subject was sometimes given
both in Latin and German, often specified by words like *germanice* or
*vulgo*, as in this dissertation on signatures with the double title *De Nominis Subscriptione, Vulgo von Nahmens-Unterschreibung*.[^32] Some
early modern observers derided these bilingual titles as a fashion, but
among mid- and late seventeenth-century jurists the increasing use of
the German vernacular was a sustained and widespread trend.[^33] There
has been growing scholarly interest in the use of German language in
universities, but the nature of this process and its causes are not
fully understood.[^34]

{% figure caption: "Figure 3. The gradually increasing use of the German vernacular in the dissertation's titles in the 1660s was driven mostly by scholars in their thirties and forties while older scholars were more reluctant to compromise the linguistic uniformity of this almost entirely Latin genre. Percentage of German keywords (*der, das, germanice, oder, von, vom, vulg*) and number of dissertations by age cohort. Excluded: reprints, duplicates, entries with fewer than two authors, entries without *praeses* birth date. Data source: *Verzeichnis der im deutschen Sprachraum erschienenen Drucke des 17. Jahrhunderts* (2020). " %}
![A dot density graph entitled "Use of German by Age Cohort and Year" with year on the x-axis and the age of praeses on the y-axis. Green, yellow and black dots on a white background.]({{site.url}}/assets/img/v05/scholz/figure3.png)
{% endfigure %}

The data under consideration in this study shows that, while some
bilingual titles had been published throughout the seventeenth century,
the proportion of law dissertations that included German words in their
titles increased from the 1660s onward, but that this new preference was
not shared by all members the profession. Figure 3 indicates that the
initial increase of German vernacular titles in the 1660s was primarily
driven by younger and middle-aged scholars, i.e. *praesides* in their
thirties and forties. Older scholars never took up the new trend to the
same degree as their younger colleagues. In contrast, cohorts of
scholars who entered the profession during or after the 1660s used the
German vernacular in their dissertation titles with more regularity.
While the distribution is not perfectly diagonal, the increase in German
titles is moving more by generation than by year.

This insight adds two important elements to the scholarship on
vernacular language use in early modern dissertations. First, existing
scholarship, centered primarily on discussions around language use in
theological and philosophical dissertations, has suggested two principal
reasons for which scholars preferred German: an enlightened desire to
reach a broader, non-academic public (including women) and discontent
about the disputants' poor Latin, resulting in disputants devoting more
energy to the form of their writing than its content.[^35] This graphic
suggests that, among jurists, the preference for the German vernacular
was also a matter of demographics: the early increase of bilingual
dissertation titles was primarily driven by scholars in their thirties
and forties. These cohorts of scholars were born in the 1620s and 1630s
and experienced the Thirty Years' War as students in schools and
universities, only entering the profession once the war was over.
Linguists will tell us that age cohorts' shared or differential
experiences of war, economic crisis, or social transformation have
regularly been identified as key drivers of linguistic change.[^36] This
finding is thus an invitation to broaden the historiographical
discussion on early modern academic language beyond intrinsic, scholarly
motivations to consider the role of structural factors such as age. The
generation of scholars born in the 1620s and 1630s, who also played a
key role concerning the appearance of "territory" outlined below,
deserves particular attention in this respect.

Secondly, the graphic invites us to reassess the importance of
individual initiative in such shifts. It has been common to credit
individual scholars with advancing the use of the German vernacular and
other important shifts.[^37] Closer inspection of the data shows that
while some members of this cohort---such as Ernst Friedrich Schröter
(born 1621), Heinrich Linck (born 1642) or Johann Volkmar Bechmann (born
1624)---published more bilingual titles than others, this was not a
development driven by individual scholars. The graphic thus cautions
against a top-down reading of this development. Rather than being the
merit of one or a few eminent individuals, the gradual rise of the
German vernacular in late seventeenth-century titles appears to reflect
a shift in preferences that was shared across large numbers of scholars
with a common historical experience.

### The Eclipse of Controversy

The data under consideration also reveals changes that were quickly
adopted by scholars of all ages. The perhaps most distinctive example
for such a pattern is the decline in dissertations that were framed as
*controversiae*. Dissertations entitled as *contoversiae* were often
structured as a series of yes-or-no questions that were to be resolved
with the help of legal sources and established scholarship. While more
than ten per cent of legal dissertations were framed as *controversiae*
at the beginning of the seventeenth century, in the 1610s, the
proportion of dissertations mentioning *controversia* and its adjectival
variations in their titles dropped by more than half, and disappeared
almost entirely in the late 1630s and early 1640s (figure 4).[^38] This
trend is indicative of a broader development in German legal
scholarship: many dissertations lost their oral, dialogic elements and
took on a more single-voiced, monographic form that replaced the motley
collections of theses and *controversiae*. The waning of dialogic,
antagonistic forms of reasoning also resonated with wider shifts in
seventeenth-century academic culture, which saw an increasing
affectation of more courtly, gallant, and conciliatory tones.[^39]

{% figure caption: "Figure 4. In the early decades of the seventeenth century, the proportion of dissertations framed as *controversia* declined significantly, indicating a waning of dialogic and antagonistic forms of reasoning and a desire to avoid association with confessional controversy. Annual percentage of dissertations mentioning *controvers* (ten-year moving average). Excluded: reprints, duplicates, entries with fewer than two authors, entries without *praeses* birth date. Data source: *Verzeichnis der im deutschen Sprachraum erschienenen Drucke des 17. Jahrhunderts* (2020)." %}
![A line graph entitled "Mentions of controversia by Year" with year on the x-axis and the moving average percetage on the y-axis. Blue line on a white background.]({{site.url}}/assets/img/v05/scholz/figure4.png)
{% endfigure %}

{% figure caption: "Figure 5 The early and rapidly declining framing of dissertation titles featuring the scholastic keyword *controversia* indicate a turn away from dialogic and antagonistic forms of argumentation across all age cohorts, pointing to a cultural shift that was more widespread and swifter than others. Percentage of dissertation titles mentioning *controvers* and number of dissertations by age cohort. Excluded: reprints, duplicates, entries with fewer than two authors, entries without praeses birth date. Data source: *Verzeichnis der im deutschen Sprachraum erschienenen Drucke des 17. Jahrhunderts* (2020)." %}
![A dot density graph entitled "Mentions of controversia by Age Cohort and Year" with year on the x-axis and the age of praeses on the y-axis. Green, yellow and black dots on a white background.]({{site.url}}/assets/img/v05/scholz/figure5.png)
{% endfigure %}

Figure 5 breaks this decline down by age, suggesting that the sharp drop
in dissertations framed as *controversia* in the 1610s and their
all-but-disappearance in the late 1630s, albeit slightly uneven, were
not restricted to a particular age cohort, but that they were shared by
jurists of all ages.[^40] Unlike the rise of German language titles
examined above or the mentions of territory discussed below, this was
something all age cohorts changed their minds about within a short time.
The all-but disappearance of *controversia* from legal dissertation
titles acquires particular salience if one considers the context of
confessional controversy and escalating political tensions in the Empire
in the run-up to the Thirty Years' War in 1618.

Indeed, in early modern book titles, *controversia* did not just
designate a rhetorical form. The word had featured prominently in the
publication titles of polemical theologians since the days of Johannes
Cochlaeus and came to connote a particularly polemical and intransigent
form of scholarship.[^41] In the early decades of the seventeenth
century, the same time in which Protestant universities instituted the
first dedicated chairs for controversial theology and incorporated the
subject into academic curricula, the meaning of *controversia* further
narrowed to denote inter- and intra-confessional polemics.[^42]
Theological controversy in the decades leading up to the Thirty Year's
War and its counter-current, irenicism, are longstanding fields of
research, with recent scholarship placing particular emphasis on the
role of conflict in Protestant identity formation.[^43] The work of
irenical theologians who rejected acrimonious confessional polemics in
favour of peaceful dialogue has received considerable scholarly
attention. Similar tensions among jurists (*Kontroversjurisprudenz*)
have been studied less, but the simultaneous all-but-disappearance of
*controversia* from the titles of legal dissertations at the same time
as the word acquired a distinctively confessional connotation may well
indicate a shared desire to avoid association with religious polemics in
a collective move to what one could term "methodological irenicism."
That trend suggests that irenical dispositions may have had a much wider
traction in jurisprudence than previously assumed.[^44]

## Territory

In addition to the linguistic and methodological developments discussed
so far, early modern law dissertations also indicate shifts in jurists'
thematic interests. In the seventeenth century, the number of public law
dissertations published in the German lands increased substantially. As
political conflict and communication in the Holy Roman Empire were
increasingly framed in legal terms, administrations at all levels---imperial, territorial, and others---required legal experts trained in
dealing with highly specific problems and forms of communication.[^45]
The largest cluster of public law dissertations was concerned with
imperial law, around half of which concerned the Imperial Estates, their
prerogatives, and the relationship among themselves as well as with the
Empire. The notion of territorial superiority (*Landeshoheit*) played a
key role in the legal-political conflicts of the seventeenth and
eighteenth centuries. In the seventeenth century, the princes' power was
increasingly understood not as emanating from their jurisdiction or as a
bundle of diverse (regalian) rights and prerogatives---from
safe-conduct to mining---but as the comprehensive dominion over a
territory.[^46] The Peace of Westphalia codified the concept as *ius territorii et superioritatis*.

{% figure caption: "Figure 6. The relatively late appearance of dissertation titles mentioning "territory" among a particularly young cohort of scholars in the aftermath of the Thirty Years' War speaks to the expanding career prospects for young lawyers in the administrations of the Imperial Estates. Percentage of dissertation titles mentioning *territo* and number of dissertations by age cohort. Excluded: reprints, duplicates, entries with fewer than two authors, entries without *praeses* birth date. Data source: *Verzeichnis der im deutschen Sprachraum erschienenen Drucke des 17. Jahrhunderts* (2020). " %}
![A dot density graph entitled "Mentions of territorium by Age Cohort and Year" with year on the x-axis and the age of praeses on the y-axis. Green, yellow and black dots on a white background.]({{site.url}}/assets/img/v05/scholz/figure6.png)
{% endfigure %}

The pattern visible in figure 6 is noteworthy for three reasons.
Firstly, while some dissertations on territorial superiority had been
published in the first half of the century, it shows that territory only
began to appear regularly in dissertation titles from the 1660s onward.
Most of these texts discussed territorial superiority, but they also
include dissertations on transit rights, servitudes, and different
aspects of inter-polity relations.[^47] Questions concerning territorial
rights had also been discussed in dissertations that did not mention the
word in their title. However, territory's late appearance in the
dissertation titles is surprising, given that the concept had already
played a key role in the legal-philosophical literature of the sixteenth
and seventeenth centuries, from Zasius to Reinking, and rose to new
prominence when the stipulations of the Westphalian Peace employed the
language of territory to empower the Imperial Estates in the exclusive
control over their dominions.[^48]

Second, the graphic shows that the late appearance of territory in the
dissertation titles was a distinctly generational phenomenon.
Dissertation titles mentioning territory were published with regularity
from the 1660s onward, but almost exclusively by *praesides* in their
twenties and thirties. It was not until later that *territorium* and
*territorialis* appeared more consistently in the dissertation titles of
other age cohorts. A closer inspection of the data shows that it was
jurists like the twenty-three-year-old Georg Engelbrecht at Greifswald
or the thirty-one-year-old Hulderich von Eyben at Giessen who stood at
the beginning of this trend, respectively with an extensive discussion
of territorial rights[^49] and a lengthy comparison between dominion of
the Imperial Estates over their territories and the prerogatives of the
emperor.[^50] That territory was re-introduced into dissertation titles
mostly by a young cohort of scholars over a decade after the Thirty
Year's War indicates that one of the most consequential legal-political
concepts of the mid-seventeenth century faced more academic inertia than
the historiographical emphasis on territorial superiority and its
cognate concepts would suggest. It is important to note that the
scholars behind this shift---young men who entered the profession at
the end of the Thirty Years War---belonged to the same age cohorts that
furthered the use of German vernacular titles, a circumstance that
warrants further research into the academic preferences and biographies
of this generation.

Third, the prominent placement of territory in the titles of
dissertations by younger scholars adds to a pragmatic theory about why
jurists chose the subjects on which they worked. It has been argued that
jurists preferred topical subjects that appealed to imperial or
territorial authorities to improve their career prospects or transition
into administrative roles.[^51] Figure 6 suggests that age may have
played a key role in a choice that made particular sense early in a
jurist's career. Indeed, most of the young *praesides* who placed the
language of territory so prominently in their dissertations in the 1660s
and 1670s later took on important positions in territorial
administrations.[^52] The wider implication is that younger jurists may
have played a particularly important role as intellectual conduits
between academic jurisprudence and policy and that when studying
processes of reception between territorial administrations and legal
scholarship it may be worth to pay particular attention to the work of
younger scholars.

### Conclusion

The charts presented in this article employed a novel visualization
technique to examine whether linguistic, methodological, and thematic
shifts in the titles of catalogued early modern legal dissertations were
specific to certain age cohorts or whether they were adopted across
generations.

Two distinctive developments in the aftermath of the Thirty Years' War---the increasing use of bilingual titles that combined Latin and the
German vernacular, and the late emergence of dissertations mentioning
*territorium*---can be attributed to the young age cohorts who entered
the profession after the Thirty Years' War had ended, at a time when the
number of catalogued dissertations expanded, and the professoriate
rejuvenated. The cohort-specific increase of German language titles
suggests that conventional explanations for shifts in early modern
academic language as primarily driven by scholarly motives, immanent to
academia, should be complemented by a consideration of structural
factors such as age and the political, social, and economic forces it
mediates. The graphic also cautions against overemphasizing the
initiative of individual scholars, as the use of German in the titles
appears to be shared across large groups of scholars. The late
appearance of *territorium* or *territorialis* in the titles is not just
surprising because of the concept's eminent role in the Westphalian
Peace: that it had to be (re)introduced by a young cohort of scholars
suggests that among established jurists, one of the most consequential
legal-political concepts of the mid-seventeenth century faced more
academic inertia than could be assumed. The pattern also adds to what we
know about career motives and subject choice: in this case, it was
primarily younger scholars who chose to work on a subject that could
improve their academic career prospects or allow them to transition into
the imperial or territorial bureaucracies. In a broader sense, this begs
the question whether younger scholars may have played a particularly
important role as conduits between academic scholarship and policy. In
contrast, the sudden drop in mentions of *controversia* in the 1610s
indicates a cross-generational cultural shift that was remarkably broad
and swift. This happened in the same years as the meaning of
*controversia* narrowed to denote confessional polemics among
theologians and began to be institutionalized in dedicated chairs,
possibly indicating a shared desire among jurists to avoid association
with religious polemics.

As a contribution to digital history, the charts discussed in this paper
illustrate how a visual decomposition of lexical shifts by age can
document patterns imperceptible to traditional research and prompt new
insight into the history of dissertations, legal scholarship, academic
publishing, and universities.

---

### Bibliography

Alvermann, Dirk. "Von steifen Matronen und tanzenden Amazonen. Latein und Deutsch als Gelehrtensprachen in der Greifswalder Universitätsgeschichte (17.--19. Jh.)." In *Vernakuläre Wissenschaftskommunikation: Beiträge zur Entstehung und Frühgeschichte der modernen deutschen Wissenschaftssprachen*, edited by Jürgen Schiewe and Michael Prinz, 15--46. Berlin: De Gruyter, 2018.

Arguing with Digital History working group. "Digital History and Argument." White paper. Roy Rosenzweig Center for History and New Media (November 13, 2017): <https://rrchnm.org/argument-white-paper/>.

Amedick, Sigrid. "Juristische Dissertationen des 16. bis 18. Jahrhunderts: Erschließung und Digitalisierung von Schlüsselseiten." In *Digitale Bausteine für die geisteswissenschaftliche Forschung*, edited by Manfred Thaller, 89--101. Göttingen: Duehrkohp und Radicke, 2003.

Amsel, Johann and Jacob Hoepner. *Dissertatio Iuridica, De Nominis Subscriptione, Vulgo von Nahmens-Unterschreibung*. Königsberg: Reusner, 1697.

Beetz, Manfred. *Rhetorische Logik: Prämissen der deutschen Lyrik im Übergang vom 17. zum 18. Jahrhundert*. Tübingen: Niemeyer, 1980.

Brachvogel, Johann Rudolph and Georg Nikolaus Borne. *Dissertatio logica de usu et abusu disputandi*. Erfurt: Groschius, 1713.

Braudel, Fernand. "Histoire et Sciences Sociales: La Longue Durée." *Annales. Économies, Sociétés, Civilisations* 13, no. 4 (1958): 725--53.

Da, Nan Z. "Critical Response III. On EDA, Complexity, and Redundancy: A Response to Underwood and Weatherby." *Critical Inquiry* 46, no. 4 (2020): 913--24. <https://doi.org/10.1086/709230>.

Eckert, Penelope. "Age as a sociolinguistic variable." In *The Handbook of Sociolinguistics*, edited by Florian Coulmas, 151--167. Oxford: Blackwell, 1997.

Elden, Stuart. *The Birth of Territory*. Chicago: University of Chicago Press, 2013.

Engelbrecht, Georg and Friedrich Gerdes. *De iure territorii*. Greifswald: Doischerus, 1661.

Engl, Elisabeth. "Volltexte für die Frühe Neuzeit. Der Beitrag des OCR-D-Projekts zur Volltexterkennung frühneuzeitlicher Drucke." *Zeitschrift für Historische Forschung* 47, no. 2 (2020): 223--50. <https://doi.org/10.3790/zhf.47.2.223>.

Eyben, Hulderich von and Werner Rudolph von der Schulenburg. *Dissertatio De Origine Illustris Illius Regulae: S. Romano-Germanici Imperii, Electores, Duces, Marchiones, Landgrafios, Burggrafios, Principes, Comites, Barones & Coeteros in His Accensos, Territoriive, Quos Vocant, Dominos, Tantum Posse in Suis Territoriis, Quantum Imperator in Imperio*. Giessen: Vulpius, 1660.

Härter, Karl. "Ius publicum und Reichsrecht in den juristischen Dissertationen mitteleuropäischer Universitäten der Frühen Neuzeit." In *Science politique et droit public dans les facultés de droit*, edited by Jacques Krynen and Michael Stolleis, 485--528. Frankfurt am Main: Klostermann, 2008.

Hessbrüggen-Walter, Stefan. "Interdisciplinarity in the 17th Century? A Co-Occurrence Analysis of Early Modern German Dissertation Titles." (under review for a special issue of *Synthese*).

Horn, Ewald. *Die Disputationen und Promotionen an den deutschen Universitäten vornehmlich seit dem XVI. Jahrhundert*. Leipzig: Harassowitz, 1893.

Jaeger, Hans. "Generations in History: Reflections on a Controversial Concept." *History and Theory* 24, no. 3 (1985): 273--92. <https://doi.org/10.2307/2505170>.

Jureit, Ulrike. *Generationen: zur Relevanz eines wissenschaftlichen Grundbegriffs*. Hamburg: Hamburger Edition, 2005.

Koppitz, Hans-Joachim. "Ungehobene Schätze in unseren Bibliotheken." In *Dissertationen in Wissenschaft und Bibliotheken*, edited by Rudolf Jung, 29--39. Munich: Saur, 1979.

Koselleck, Reinhart. *Vergangene Zukunft: zur Semantik geschichtlicher Zeiten*. Frankfurt am Main: Suhrkamp, 1995.

Mannheim, Karl. "The Problem of Generations." In *Essays on the Sociology of Knowledge by Karl Mannheim*, edited by Paul Kecskemeti, 276--322. London: Routledge, 1952.

Marti, Hanspeter. "Disputation." In *Historisches Wörterbuch der Rhetorik*, edited by Gerd Ueding, vol. 2, Bie-Eul, 866--80. Tübingen: Niemeyer, 1994.

Marti, Hanspeter. "Kommunikationsnormen der Disputation. Die UniversitätHalle und Christian Thomasius als Paradigmen des Wandels." In *Kulturder Kommunikation: Die europäische Gelehrtenrepublik im Zeitalter von Leibniz und Lessing*, edited by Ulrich Johannes Schneider, 317--44. Wiesbaden: Harrassowitz, 2005.

Marti, Hanspeter. "Lateinsprachigkeit---ein Gattungsmerkmal der Dissertationen und seine historische Konsistenz." *Jahrbuch für internationale Germanistik* 30 (1998): 50--63.

Marti, Hanspeter. "Von der Präses- zur Respondentendissertation. Die Autorschaftsfrage am Beispiel einer frühneuzeitlichen Literaturgattung," In *Examen, Titel, Promotionen: akademisches und staatliches Qualifikationswesen vom 13. bis zum 21. Jahrhundert*, edited by Rainer Christoph Schwinges, 251--74. Basel: Schwabe, 2007.

Moretti, Franco. "Style, Inc. Reflections on Seven Thousand Titles (British Novels, 1740--1850)." *Critical Inquiry* 36, no. 1 (2009): 134--58. <https://doi.org/10.1086/606125>.

Pinder, Wilhelm. *Das Problem der Generation in der Kunstgeschichte Europas*. Berlin: Frankfurter Verlags-Anstalt, 1926.

Piper, Andrew. *Enumerations: Data and Literary Study*. Chicago: University of Chicago Press, 2018.

Pörksen, Uwe. "Der Übergang vom Gelehrtenlatein zur deutschen Wissenschaftssprache. Zur frühen deutschen Fachliteratur und Fachsprache in den naturwissenschaftlichen und mathematischen Fächern (ca. 1500--1800)." *Zeitschrift für Literaturwissenschaft und Linguistik* 13, no. 51 (1983): 227--58.

Prinz, Michael and Jürgen Schiewe, eds. *Vernakuläre Wissenschaftskommunikation: Beiträge zur Entstehung und Frühgeschichte der modernen deutschen Wissenschaftssprachen*. Berlin: De Gruyter, 2018.

Ranieri, Filippo. "Juristische Universitätsdisputationen im 17. und 18. Jahrhundert. Zur Analyse des deutschen Autoren-und Händlermarktes." In *Historische Soziologie der Rechtswissenschaft*, edited by Erk Volkmar Heyen, 157--72. Frankfurt am Main: Klostermann, 1986.

Rauschenbach, Sina. "Gemeinsame Gegner: Zur integrativen Wirkung von Polemik in christlichen Kontroversen der Frühen Neuzeit." In *Religion als Prozess: kulturwissenschaftliche Wege der Religionsforschung*, edited by Thomas G. Kirsch, Rudolf Schlögl, and Dorothea Weltecke, 159--71. Paderborn: Ferdinand Schöningh, 2015.

Schmidt, Benjamin. "Age Cohort and Vocabulary Use." *Sapping Attention* (April 11, 2011): <http://sappingattention.blogspot.com/2011/04/age-cohort-and-vocabulary-use.html>.

Schiewe, Jürgen. *Sprachenwechsel---Funktionswandel---Austausch der Denkstile: Die Universität Freiburg zwischen Latein und Deutsch*. Tübingen: Niemeyer, 1996.

Scholz, Luca. "A Distant Reading of Legal Dissertations at Seventeenth-Century German Universities." *Historical Journal* 65, no. 2 (2022): 297--327. <https://doi.org/10.1017/S0018246X2100011X>.

Schubart-Fikentscher, Gertrud. *Untersuchungen zur Autorschaft von Dissertationen im Zeitalter der Aufklärung*. Berlin: Akademie-Verlag, 1970.

So, Richard Jean. *Redlining Culture: A Data History of Racial Inequality and Postwar Fiction*. New York: Columbia University Press, 2020.

Wildt, Michael. *Generation des Unbedingten. Das Führungskorps des Reichssicherheitshauptamtes*. Hamburg: Hamburger Edition, 2015.

Willoweit, Dietmar. *Rechtsgrundlagen der Territorialgewalt. Forschungen zur deutschen Rechtsgeschichte*. Köln/Wien: Böhlau, 1975.

---

### Notes

The author would like to thank Hanspeter Marti, Ryan Heuser, Stefan Hessbrüggen-Walter, Gerardo Serra, the anonymous reviewers, and the editors at *Current Research in Digital History* for their helpful comments in preparing this manuscript.

[^1]: Marti, "Disputation," 866--80.

[^2]: Horn, *Disputationen und Promotionen*; Koppitz, "Ungehobene Schätze," 29--39.

[^3]: The pioneer in this domain was the legal historian Filippo Ranieri. Ranieri, "Juristische Universitätsdisputationen," 162, 164.

[^4]: Härter, "Ius publicum," 485--528.

[^5]: Scholz, "Distant Reading."

[^6]: Schmidt, "Age Cohort and Vocabulary Use." This "cohort semantics" approach combines a more traditional emphasis on demographic data with a more recent emphasis on text mining.

[^7]: Piper, *Enumerations*.

[^8]: So, *Redlining Culture*.

[^9]: Da, "Critical Response III."

[^10]: Koselleck, *Vergangene Zukunft*.

[^11]: Wildt, *Generation des Unbedingten*.

[^12]: For an interdisciplinary sample, see: Jureit, *Generationen*.

[^13]: Arguing with Digital History working group, "Digital History and
    Argument."

[^14]: Braudel, "Longue Durée," 727.

[^15]: Braudel, "Longue Durée," 734.

[^16]: Moretti, "Style, Inc.," 145.

[^17]: Jaeger, "Generations," 273. One of the works criticized by Jaeger is Wilhelm Pinder's generational theory of European art history: Pinder, *Das Problem der Generation*.

[^18]: Jaeger, "Generations," 287--88.

[^19]: Mannheim, "Generations," 319.

[^20]: Brachvogel and Borne, *De usu et abusu disputandi*, ch. 3, § 38.

[^21]: These are the dissertations tagged as 'Dissertation:jur.' as of February 2020. VD17 is an abbreviation for *Verzeichnis der im deutschen Sprachraum erschienenen Drucke des 17. Jahrhunderts*.

[^22]: Unfortunately, the birth dates of respondents are far less densely documented than those of the *praesides*. This makes it difficult to examine whether and how the age gaps between *praesides* and respondents affected methodological and thematic preferences.

[^23]: Engl, "Volltexte für die Frühe Neuzeit."

[^24]: Stefan Hessbrüggen-Walter, for example, has recently conducted a computational study on interdisciplinarity in philosophical dissertations. See: Hessbrüggen-Walter, "Interdisciplinarity in the 17th Century."

[^25]: The Max Planck Institute for Legal History in Frankfurt catalogued a higher number of dissertations (over 35,000 entries for the seventeenth century), but these include a much larger proportion of duplicates and reprints (up to 60 per cent). See Härter, "Ius publicum", 490--2.

[^26]: While the title page, dedications, and other corollaries do occasionally hint to the actual author, determining who wrote a text is difficult and frequently impossible. See: Schubart-Fikentscher *Autorschaft*; Marti, "Autorschaftsfrage," 251--74.

[^27]: Amedick, "Juristische Dissertationen," 90--1.

[^28]: Härter, "Ius publicum," 512.

[^29]: Mannheim, "Generations," 278.

[^30]: Marti, "Lateinsprachigkeit," 62.

[^31]: Marti, "Lateinsprachigkeit," 50.

[^32]: Amsel and Hoepner, *De Nominis Subscriptione, Vulgo von Nahmens-Unterschreibung*.

[^33]: Scholz, "Distant Reading," 23--25.

[^34]: See, for example: Prinz and Schiewe, *Vernakuläre Wissenschaftskommunikation*; Schiewe, *Sprachenwechsel*.

[^35]: See, for example: Marti, "Lateinsprachigkeit"; Alvermann, "Latein und Deutsch."

[^36]: See: Eckert, "Age."

[^37]: Among seventeenth-century jurists, Christian Thomasius is often credited for his embrace of German language teaching. See, for example: Pörksen, "Übergang," Marti, "Kommunikationsnormen," 332.

[^38]: Scholz, "Distant Reading," 18--22.

[^39]: Beetz, *Rhetorische Logik*, 89--108.

[^40]: Not all variation in later decades can be meaningfully interpreted, but the temporary upticks in the 1630s and the 1680s (both visible in figures 4 and 5) reflect two series of dissertations published respectively by Justus Sinold (in his early forties), Johann Christoph Boltz (in his late twenties and early thirties), both framed as *controversiae*.

[^41]: See: Walter, "Kontroversliteratur," 38--42; Köpf, "Kontroverstheologie," 1651--1653.

[^42]: See: Rauschenbach, "Gemeinsame Gegner," 159.

[^43]: One of the most prominent examples is the project "Controversia et Confessio" at the University of Mainz, led by Irene Dingel: <http://www.controversia-et-confessio.de/>.

[^44]: I thank Hanspeter Marti for pointing me to the parallels with irenical and polemic theology. Further studies on neighboring faculties could probe this hypothesis and examine whether a similar development can also be observed in dissertations published in theology, philosophy, or even medicine.

[^45]: Härter, "Ius publicum," 498.

[^46]: Willoweit, *Rechtsgrundlagen*, 124.

[^47]: Even after 1660, the number of dissertations that placed the word *territorium* and its adjectival variations in their title was remarkably low given the territorial language with which jurists commonly framed the Imperial Estates' claims to superiority and non-violability of borders.

[^48]: For an English-language discussion of territory in sixteenth-and-seventeenth-century European thought, see: Elden, *Birth of Territory*, 279--321.

[^49]: Engelbrecht and Gerdes, *De iure territorii*.

[^50]: von Eyben and von der Schulenburg, *De Origine Illustris Illius Regulae*.

[^51]: Härter, "Ius publicum," 486--487.

[^52]: Georg Engelbrecht joined the Swedish Pomeranian courts at Greifswald in 1663 and Wismar in 1664. Hulderich von Eyben was appointed as councilor to the Duchy of Brunswick-Lüneburg in 1669. Other examples include Ernst Friedrich Schröter, Johann Christoph Falckner, and Johann Wolfgang Textor (the Elder).