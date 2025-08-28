---
title: "Annotating "Privacy" for Semi-Supervised Event Extraction in Historical Newspapers"
doi: "https://doi.org/10.31835/crdh.2025.TK"
volume-number: 7
year: 2025
date: 2025-08-28
authors:
- last: da Silva Perez
  first: Natália
  email: "dasilvaperez@eshcc.eur.nl"
  affiliation: "Erasmus University Rotterdam"
  orcid: https://orcid.org/0000-0003-3723-5682
  url: "https://silvaperez.github.io/"
abstract: |
    TK
preview: "/assets/img/v07/dasilvaperez/preview.png"
---

In the project *Privacy Black and White,* our interdisciplinary team of historians and computer scientists examines how language used to convey notions of privacy influenced discursive processes that helped differentiate between Africans and Europeans during the colonial period (c. 1500--1850). Our team works from the assumption that race and racism emerged, and continue to emerge, as processes of social construction that took, and still take, place through the way humans use language.[^1] From this perspective, we ask: how did language used to express notions of privacy in the colonial period contribute to shaping race and racism as we came to experience them in the present? To investigate this question, we combine methods from historiography and from natural language processing.

Our team also works from the assumption that this process of social
construction has, from the onset, always crossed borders. If today we might refer to it as a globalized process, for the period of our study (1500 to 1850), we frame it as a trans-imperial discursive process.[^2] By framing this discursive process as trans-imperial, we mean that discourses about racial perceptions seeped through empires, colonies, languages, and domains of human action, without regard for imposed geopolitical borders.

With all of this in mind, our team's goal is to advance our
understanding of the racist legacies of colonialism as a shared European concern. For that, we work with historical material from both sides of the Atlantic, for example, from the Caribbean islands of Guadalupe, Saint Croix, Saint John, Saint Thomas, as well as other locations in the South, Center, and North regions of the American continent, which were sugar producing colonies controlled by the French, British, Danish, and Dutch colonial empires.

We are interested in quantifying and analysing diachronic and
geographical change in language. More specifically, we are interested in the way that language used to convey notions of privacy related to language used to convey racial perceptions, and how these linguistic expressions manifested over time and space. These research interests require us to consider a very large quantity of written material; therefore, our project is organized as a collaboration between historians of the early modern period and computer scientists who specialize in natural language processing.[^3] Our team employs a collaborative intelligence approach, which means that we seek to harness the best insights from humans and from machines to achieve a level of analysis that each side alone would not necessarily be able to do.[^4] That is needed because, as might be inferred from the geographical scope
covered in our project, the historical documents that we examine are in several languages. We have texts in English, French, Danish, Dutch, Portuguese, Spanish, and other languages. Moreover, these texts are in non-standardized, early modern varieties. The genres of texts in our historical sources also vary. We must cover newspapers, treatises about law, religious manuals, printed sermons, literature, not to mention handwritten documents, such as court records and correspondence, for example.

In this article, I will discuss our pilot project, where our research team focused attention on texts of newspapers ads from the eighteenth and nineteenth centuries, which reported on enslaved people who ran away from their enslavers. In this pilot project, our teammate Nadav Borenstein, a computer scientist, trained semi-supervised NLP models for event extraction. A semi-supervised approach consists of using a small amount of data annotated by domain experts in combination with non-annotated data, so that the model can be trained to make predictions about the information within the texts by extrapolating from what the
domain experts annotated.[^5] Because producing datasets annotated by historians is time consuming and expensive, a semi-supervised approach, when successful, offers a cost-effective and time-saving solution for obtaining training data. In what follows, I will discuss how we repurposed already existing databases and annotations prepared by historians in other projects, how we complemented these data with new material in the languages that were missing, and how we compiled all the data into the multilingual dataset that we employed for training, testing, and evaluating our models.

### Privacy for Freedom Seekers: a Pilot Project

Our team started with a working definition of "privacy" that posits it as an ability that a person might have to adjust, control, or regulate access to themselves and their things.[^6] This working definition of privacy is partial, but useful for us because it is versatile: it can summarize privacy in cases when the person in question has access to boundaries or barriers (such as walls and doors that we find in a house), but it can also describe more precarious types of privacy, when the person in question does not have access to walls, doors, locks, and keys, and might try to improvise.

In his 2022 book *Freedom Seekers*, Simon P. Newman examined the lives of enslaved people who ran away in eighteenth century London.[^7] Reflected in Newman's work was our team's intuition that there is a strong relationship between freedom, autonomy, and privacy as defined above, so we decided to investigate this intuition further, using the same type of primary sources as Newman, namely, runaway ads published in newspapers. Escaping was an enslaved person's practical claim to autonomy over their own life: it posed a challenge to the claim as private property made by the enslaver over the enslaved person's body. Faced with this challenge and trying to avoid losing property, many enslavers put ads on newspapers reporting on the escapes, offering rewards for the recapture of the enslaved person who ran away. Centuries
later, such ads survive in print as a sort of registry for historians to study these freedom seekers.

In our team discussions, it became clear that enslaved people who ran away made improvised attempts to obtain a modicum of privacy as defined above. For example, Julia, an enslaved woman who ran away with her eight-year-old daughter Fanny, was reported on *The Louisiana Gazette* of June 6, 1815, as having taken a bundle of blankets and clothes. Another example is that of Jean-Pierre, an enslaved man reported on the Saint Domingue newspaper *Affiches américaines* of February 19, 1777 as having taken his enslaver's "frock coat and hunting knife which he could use and call himself free."[^8] Blankets could provide protection from the weather, and changes of clothes allowed the person running away to disguise their identity, providing a certain anonymity. Protection and
anonymity allowed the person running away to regulate access to
themselves, serving as building blocks for privacy.

We formulated our pilot research question thus:

> *In the event of running away, in what ways did the enslaved person
> claim, not only freedom, but also privacy, for themselves?*

Nadav Borenstein framed our pilot research as an NLP event extraction task and used question answering models as the basis for this experiment.[^9] Such models "can retrieve the answer to a question from a given text, which is useful for searching for an answer in a document."[^10] The goal would be for the model to help us retrieve privacy-related events reported in the runaway ads, such as the ones used by Julia and Jean-Pierre exemplified above.

### Datasets for Training and Testing

Ideally, our team would want to employ a dataset comprised of runaway ads in newspapers published in the Caribbean and American colonies as well as European metropoles, but such a dataset was not readily available, so we combined existing and purpose-built ones to meet our research needs.

The first database, which served as the basis for the dataset for our pilot experiment, was prepared and published within the project *Runaway Slaves in Britain: bondage, freedom and race in the eighteenth century.*[^11] It contained annotated English language runaway ads published between 1700 and 1780 in newspapers from Scotland and England.[^12] All the ads in this database were manually retrieved, manually transcribed, and manually annotated by the *Runaway Slaves in Britain* researchers.

The annotation done by the *Runaway Slaves in Britain* researchers to annotate their corpus included of the following labels for the
attributes:

> Accused of crime; Age; Also known as; Clothing; Companions; Contact
> address; Contact name; Contact occupation; Country marks; Destination
> (region); Destination (specified); Disease; Gender; Given name; Given
> surname; Height; Injuries; Language; Literacy; Motivation; Notes;
> Origin; Other reward; Owner; Owner address; Owner occupation;
> Personality; Physical characteristics; Physical scars; Plantation
> marks; Racial descriptor; Ran from region; Ran from ship; Ran from
> specified; Religion; Reward pence; Reward pounds; Reward shillings;
> Runaway date; Skills; Specified occupation; Stutters; Total reward;
> Total value; Value pence; Value pounds; Value shillings; Warning
> notice.[^13]

In our exploratory analysis of *Runaway Slaves in Britain*, we noticed that among these attribute labels, some of would often show privacy related events. Of particular interest for us were the following labels: "Accused of Crime" and "Physical Characteristics." In the case of the attribute "Accused of Crime," we found information about mothers running away with their small children, people taking changes of clothes with them when they ran away, and people taking weapons with them, as the reader will recall from the two examples of Julia and Jean Pierre, mentioned above. In the case of the attribute "Physical Characteristics," we found detailed descriptions of the person who ran away, or information about their having changed their clothing or having disguised themselves after escaping.

Our team used *Runaway Slaves in Britain* database version 1.4 published on December 12, 2019, which contains 836 individual advertisement texts. To train a multilingual model, Borenstein used automatically translations of this dataset, with its annotations, into French, Dutch, and Danish.

Next came a non-annotated dataset provided by the project *Marronage dans le monde atlantique.*[^14] From this dataset, we used 19111 individual advertisements in French and 3027 in English, published between years 1765 and 1833 in newspapers from Lower Canada, South Carolina, Guadalupe, French Guiana, Jamaica, Louisiana, and Saint Domingue (present-day Haiti).[^15] These ads were manually retrieved and transcribed by the researchers of the *Marronage* project, but not annotated.

Borenstein used data from the two datasets described above to train the event extraction models. He also withheld some of the non-annotated data from the *Marronnage* project for the purpose of testing. These two datasets were ideal for training and testing because, having been manually transcribed, the texts did not contain errors from OCR.

### Datasets for Evaluation

For evaluation, historians in our team manually annotated ads that were not used for training or testing, in each of the non-English languages that we are concerned with. For French, I was responsible for annotating fifty ads from the *Marronnage* dataset, which as mentioned above, had been manually transcribed, so free of OCR errors.

For Dutch, our teammate Felicia Fricke manually retrieved fifty ads in the newspaper *De Curaçaosche Courant* and annotated them according to the same criteria above. Since the plain text version of these came from Delpher (the National Library of the Netherland's digital repository), where they were produced using OCR, the texts contain errors (see figure1). 

{% figure caption: "Figure 1. TK" %}
![TK]({{site.url}}/assets/img/v07/dasilvaperez/figure1.png)
{% endfigure %}


Fricke purposefully left the OCR errors in the material she
annotated in order for Borenstein to evaluate how the model would
perform in real life conditions, where OCR errors are common.

For Danish, we encountered a big challenge. The pool of ads was
significantly smaller, and there are two main reasons for this: we did not have enough time within the pilot project to search all potentially relevant newspapers, and in the Danish colonial newspapers where we did search, the vast majority of the runaway ads appeared in English. Nonetheless, our colleague Rasmus Christensen managed to find eight ads in the Danish language from the newspaper *Sainct Thomæ Tidende*, whose OCR transcription I subsequently manually corrected and annotated using the same labels.

### In Conclusion: Future Research Challenges

There are three pressing challenges that our research team must face as we advance our project:

-   Scarcity of relevant runaway ads in Danish

-   Refinement of the attributes used for annotation of privacy-related
    events

-   OCR errors in the plain texts provided by libraries and archives

The first challenge, namely, dealing with the scarcity of Danish
language primary source material, seems to be the most difficult problem to tackle since it is a matter of what has survived in the archives. We might be able to mitigate this problem: I have been in conversation with my colleague Nadav Borenstein about the possibility of training a different model to aid in searching and retrieving the ads within the larger textual context of a full newspaper issue. This strategy could serve as an alternative to searching for the ads manually, and if successful, could help us save time compiling the datasets.

The second challenge, which is the need to refine the annotation
attributes, seems to us quite straight-forward. With the experience we acquired with the pilot project, we learned which strategies work most effectively, and which are least effective. In our next experiments, we plan to devise our own attribute labels targeted more directly at our research questions.

Finally, we have the challenge of OCR errors. This is a pervasive
problem that many historians have encountered when trying to do text mining or natural language processing with historical texts.[^16] There seems to be two immediate ways of addressing problems of this king: one is to try to fix the errors in post-processing (using RegEx, for example), and the second is to do the text recognition anew using more recent technology. For example, using HTR with Transkribus, or purpose-train Tesseract OCR based for our own historical prints. For the moment, our team decided not to try post-processing correction. Instead, we are experimenting with Transkribus and Tesseract OCR to produce our own versions of the corpus in plain text and comparing which of them will deliver the most cost-effective results for the purpose of our project.

### Bibliography

Baker, Paul. *Sociolinguistics and Corpus Linguistics*, Edinburgh
Sociolinguistics. Edinburgh University Press, 2010.

Bassi, Ernesto. *An Aqueous Territory: Sailor Geographies and New
Granada's Transimperial Greater Caribbean World.* Duke University Press,
2017.

Jurafsky Daniel and James H. Martin. "Question Answering." In *Speech and Language Processing (Draft): An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition*, 3rd (draft), 2020, 464--91,
https://web.stanford.edu/\~jurafsky/slp3/ed3book.pdf.

Kaplan, Frederic and Isabella di Lenardo. "Big Data of the Past."
*Frontiers in Digital Humanities* 4 (2017): 3--4,
https://www.frontiersin.org/article/10.3389/fdigh.2017.00012.

Le Glaunec, Jean-Pierre and Léon Robichaud. "Le Marronnage Dans Le Monde Atlantique, 1760-1848." Database, March 9, 2019,
http://www.marronnage.info/fr/corpus.php.

Newman, Simon. *Freedom Seekers: Escaping from Slavery in Restoration London.* University of London, 2022,
https://doi.org/10.14296/202202.9781912702947.

Newman, Simon P. et al. "Runaway Slaves in Britain: Bondage, Freedom and Race in the Eighteenth Century." Database.
https://www.runaways.gla.ac.uk.

Oberbichler, Sarah. et al., "Integrated Interdisciplinary Workflows for Research on Historical Newspapers: Perspectives from Humanities Scholars, Computer Scientists, and Librarians." *Journal of the Association for Information Science and Technology* 73, no. 2 (February 2022): 231--32, https://doi.org/10.1002/asi.24565.

Perez, Natália Silva. "Privacy and Social Spaces." *TSEG/ Low Countries Journal of Social and Economic History* 18, no. 3 (December 2021),https://tseg.nl/article/view/11040; Margulis, Stephen T. "Privacy as a Social Issue and Behavioral Concept," *Journal of Social Issues* 59, no. 2 (2003): 243--61, https://doi.org/10.1111/1540-4560.00063; Altman,Irwin. *The Environment and Social Behavior: Privacy, Personal Space, Territory, Crowding.* Brooks/Cole Publishing Company, 1975.

"Runaway Slaves in Britain Database Codebook." Database.
https://www.runaways.gla.ac.uk/database/user_guide/Runaway%20Slaves%20in%2018th%20C%20Britain%20-%20Codebook.pdf.

Wilson, James H. ad Paul R. Daugherty. "Collaborative Intelligence:
Humans and AI Are Joining Forces." *Harvard Business Review*, August 2018, https://hbr.org/2018/07/collaborative-intelligence-humans-and-ai-are-joining-forces.

Yassine. *Awesome Semi-Supervised Learning*. 2022,
https://github.com/yassouali/awesome-semi-supervised-learning.

"What Is Question Answering? - Hugging Face," accessed May 20, 2022, https://huggingface.co/tasks/question-answering.

### Notes

[^1]: Baker, *Sociolinguistics and Corpus Linguistics.*

[^2]: Bassi, *An Aqueous Territory.*

[^3]: Kaplan and di Lenardo. "Big Data of the Past," 3--4.

[^4]: Wilson and Daugherty, "Collaborative Intelligence."

[^5]: Yassine, *Awesome Semi-Supervised Learning*.

[^6]: Perez, "Privacy and Social Spaces;" Margulis, "Privacy as a Social
    Issue;" Altman, *The Environment and Social Behavior*.

[^7]: Newman, *Freedom Seekers.*.

[^8]: Le Glaunec and Robichaud. "Le Marronnage Dans Le Monde
    Atlantique.\"

[^9]: Jurafsky and Martin, "Question Answering."

[^10]: "What Is Question Answering?\"

[^11]: Newman et al., "Runaway Slaves in Britain.\"

[^12]: The newspaper titles are: *Applebee's Original Weekly Journal;
    Bath Chronicle and Weekly Gazette; Bonner & Middleton's Bristol
    Journal; Bristol Oracle and Country Intelligencer; British Apollo;
    Caledonian Mercury; Covent Garden Journal; Daily Advertiser; Daily
    Courant; Daily Journal; Daily Post; Daily Post Boy; Edinburgh
    Advertiser; Edinburgh Evening Advertiser; Edinburgh Evening Courant;
    English Post with News Foreign and Domestick; Evening Post; Felix
    Farley\'s Bristol Journal; Flying Post or The Post Master; Fogs
    Weekly Journal; Gazetteer and Daily Advertiser; Gazetteer and London
    Daily Advertiser; Gazetteer* *and New Daily Advertiser*; *General
    Advertiser; General Advertiser (1744); General Advertiser and
    Morning Intelligencer; General Evening Post; Glasgow Courant;
    Glasgow Journal; Gloucester Journal; Gore's Liverpool Commercial
    Pamphlet; Liverpool General Advertiser, or the Commercial Register;
    Lloyd's Evening Post; Lloyd\'s Evening Post and British Chronicle;
    London Chronicle; London Daily Post and General Advertiser; London
    Evening Post; London Gazette; London Journal; London Post with
    Intelligence Foreign and Domestick; Manchester Mercury; Morning
    Chronicle and London Advertiser; Northampton Mercury; Observator
    (1702); Parker's London News or the Impartial Intelligencer; Post
    Boy (1695); Post Man and the Historical Account; Public Advertiser;
    Public Ledger; Public Ledger, Or, Daily Register of Commerce and
    Intelligence; St. James's Evening Post; St. James's Chronicle; St.
    James\'s Chronicle or the British Evening Post; St. James\'s Evening
    Post; Weekly Journal or British Gazetteer; Weekly Journal or
    Saturday's Post; Whitehall Evening Post; Whitehall Evening Post or
    London Intelligencer; Williamson's Liverpool Advertiser;
    Williamson's Liverpool Advertiser and Mercantile Register*.

[^13]: "Runaway Slaves in Britain Database Codebook."

[^14]: Le Glaunec and Robichaud, "Le Marronnage Dans Le Monde
    Atlantique, 1760-1848."

[^15]: The newspaper titles of the ads included in our experiment are:
    *Affiches américaines; Gazette officielle de la Guadeloupe; Le
    Moniteur de la Louisiane; Le Télégraphe; The Louisiana Gazette; Le
    Courrier de la Louisiane; L\'Ami des Lois; Charleston Courier; City
    Gazette; The Royal Gazette; The Diary and Kingston Daily Advertiser;
    The Saint Jago Gazette;* and *The Jamaica Courant.*

[^16]: Oberbichler et al., "Integrated Interdisciplinary Workflows.\"
