---
title: Annotating "Privacy" to Train Semi-Supervised Event Extraction Models for Historical Newspapers
doi: "https://doi.org/10.31835/crdh.2025.TK"
volume-number: 8
year: 2025
date: 2025-08-28
authors:
- last: da Silva Perez
  first: Natália
  email: "dasilvaperez@eshcc.eur.nl"
  affiliation: "Erasmus University Rotterdam; University of Copenhagen"
  orcid: 0000-0003-3723-5682
  url: ""
- last: Borenstein
  first: Nadav
  email: "nb@di.ku.dk"
  affiliation: "CopeNLU at University of Copenhagen"
  url: "https://nadav.dk/"
abstract: |
    This article presents a pilot study at the intersection of history and computer science, focused on annotating “privacy” as a historical concept in runaway slave advertisements from the 18th and 19th centuries. We developed a semi-supervised natural language processing (NLP) framework for event extraction, combining limited expert-annotated data with larger unannotated corpora. Building on existing datasets and producing new multilingual annotations in English, French, Dutch, and Danish, we operationalized a working definition of privacy as the ability to regulate access to oneself or one’s belongings. Through this lens, we explored how enslaved people improvised strategies of privacy during escape, such as using clothing, blankets, or disguises to secure protection and anonymity. Our collaborative approach between historians and computer scientists addressed challenges including dataset scarcity, OCR errors, and the refinement of annotation categories. Preliminary findings suggest that acts of escape not only asserted claims to freedom but also constituted claims to privacy, highlighting the intertwined nature of autonomy, racial discourse, and material strategies across trans-imperial contexts. This work demonstrates both the methodological potential of semi-supervised NLP for historical inquiry and the value of framing privacy as a category of analysis in the study of freedom seekers.

preview: "/assets/img/v08/perez/preview.png"
---
In this article, we discuss our a pilot project where our research team focused attention on texts of newspapers ads from the 18th and 19th centuries, which reported on enslaved people who ran away from their enslavers. In this pilot project, our teammate Nadav Borenstein, a PhD candidate in computer science, trained a semi-supervised natural language processing (NLP) model for event extraction. A semi-supervised approach consists in using a small amount of data annotated by domain experts in combination with non-annotated data, so that the model can be trained to make predictions about the information within the texts by extrapolating from what the domain experts annotated.[^1] Because producing datasets annotated by historians is time consuming and expensive, a semi-supervised approach, when successful, offers a cost-effective and time-saving solution for obtaining training data. In what follows, we will discuss how we repurposed already existing databases and annotations prepared by historians in other projects, how we complemented these data with new material in the languages that were missing, and how we compiled all the data into the multilingual dataset that we employed for training, testing, and evaluating our models. Moreover, we also present some preliminary historical insights that emerged from our pilot study. 

### Privacy for Freedom Seekers: a Pilot Project

To operationalize the annotation process, we started with a working definition of "privacy" that posits it as an ability that a person might have to adjust, control, or regulate access to themselves and their things.[^2] This working definition of privacy is partial, but useful for us because it is versatile: it can summarize privacy in cases when the person in question has access to boundaries or barriers (such as walls and doors that we find in a house), but it can also describe more precarious types of privacy, when the person in question does not have access to walls, doors, locks, and keys, and might try to improvise. Equipped with this working definition, we set out to find historical textual data which dealt with enslaved people and represented ideas of privacy through recognizable linguistic expressions.

In his 2022 book *Freedom Seekers*, Simon P. Newman examined the lives of enslaved people who ran away in eighteenth century London.[^3] Reflected in Newman's work was our team's intuition that there is a strong relationship between freedom, autonomy, and privacy as defined above, so we decided to investigate this intuition further, using the same type of primary sources as Newman, namely, runaway ads published in newspapers. Escaping was an enslaved person's practical claim to autonomy over their own life: it posed a challenge to the claim as private property made by the enslaver over the enslaved person's body. Faced with this challenge and trying to avoid losing property, many enslavers put ads on newspapers reporting on the escapes, offering rewards for the recapture of the enslaved person who ran away. Centuries
later, such ads survive in print as a sort of registry for historians to study these freedom seekers.

As we worked with the newspaper ads reporting on runaways, it became clear that enslaved people who ran away made improvised attempts to obtain a modicum of privacy as defined above. For example, Julia, an enslaved woman who ran away with her eight-year-old daughter Fanny, was reported on *The Louisiana Gazette* of June 6, 1815, as having taken a bundle of blankets and clothes. Another example is that of Jean-Pierre, an enslaved man reported on the Saint Domingue newspaper *Affiches américaines* of February 19, 1777 as having taken his enslaver's "frock coat and hunting knife which he could use and call himself free."[^4] Blankets could provide protection from the weather, and changes of clothes allowed the person running away to disguise their identity, providing a certain anonymity. Protection and anonymity allowed the person running away to regulate access to themselves, serving as building blocks for privacy. Already in the dataset preparation phase, our team noticed that the process of creating the trans-imperial corpus and making annotations of privacy-related expression started to lead to historical insights. Our hope was that, combining these micro level insights with a data driven analysis, we would arrive at a more robust understanding of the strategies of privacy that enslaved people might have taken across colonial and imperial borders.

We formulated our pilot research question thus:

> *In the event of running away, in what ways did the enslaved person
> claim, not only freedom, but also privacy, for themselves?*

The pilot project was framed as an NLP event extraction task, using question answering models as the basis for this experiment.[^5] Such models "can retrieve the answer to a question from a given text, which is useful for searching for an answer in a document."[^6] The goal would be for the model to help us retrieve privacy-related events reported in the runaway ads, such as the ones used by Julia and Jean-Pierre exemplified above.

### Datasets for Training and Testing

Ideally, our team would want to employ a dataset comprised of runaway ads in newspapers published in the Caribbean and American colonies as well as European metropoles, but such a dataset was not readily available, so we combined existing and purpose-built ones to meet our research needs.

The first database, which served as the basis for the dataset for our pilot experiment, was prepared and published within the project *Runaway Slaves in Britain: bondage, freedom and race in the eighteenth century.*[^7] It contained annotated English language runaway ads published between 1700 and 1780 in newspapers from Scotland and England.[^8] All the ads in this database were manually retrieved, manually transcribed, and manually annotated by the *Runaway Slaves in Britain* researchers.

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
> notice.[^9]

In our exploratory analysis of *Runaway Slaves in Britain*, we noticed that among these attribute labels, some of them would often show privacy related events. Of particular interest for us were the following labels: "Accused of Crime" and "Physical Characteristics." In the case of the attribute "Accused of Crime," we found information about mothers running away with their small children, people taking changes of clothes with them when they ran away, and people taking weapons with them, as the reader will recall from the two examples of Julia and Jean Pierre, mentioned above. In the case of the attribute "Physical Characteristics," we found detailed descriptions of the person who ran away, or information about their having changed their clothing or having disguised themselves after escaping. These attributes were the ones that most often contained concepts that became our annotations of privacy, leading us to insights about how enslaved people managed to obtain some privacy for themselves and their loved ones through improvised strategies.

Our team used *Runaway Slaves in Britain* database version 1.4 published on December 12, 2019, which contains 836 individual advertisement texts. To train a multilingual model, Borenstein used machine translations of this dataset, with its annotations, into French, Dutch, and Danish.

Next came a non-annotated dataset provided by the project *Marronage dans le monde atlantique.*[^10] From this dataset, we used 19111 individual advertisements in French and 3027 in English, published between years 1765 and 1833 in newspapers from Lower Canada, South Carolina, Guadalupe, French Guiana, Jamaica, Louisiana, and Saint Domingue (present-day Haiti).[^11] These ads were manually retrieved and transcribed by the researchers of the *Marronage* project, but not annotated.

Borenstein used data from the two datasets described above to train the event extraction models. He also withheld some of the non-annotated data from the *Marronnage* project for the purpose of testing. These two datasets were ideal for training and testing because, having been manually transcribed, the texts did not contain errors from OCR.

### Datasets for Evaluation

For evaluation, historians in our team manually annotated ads that were not used for training or testing, in each of the non-English languages that we are concerned with. For French, Natália da Silva Perez was responsible for annotating fifty ads from the *Marronnage* dataset, which as mentioned above, had been manually transcribed, so free of OCR errors.

For Dutch, Felicia Fricke manually retrieved fifty ads in the newspaper *De Curaçaosche Courant* and annotated them according to the same criteria above. Since the plain text version of these came from Delpher (the National Library of the Netherland's digital repository), where they were produced using OCR, the texts contain errors (see figures 1a and 1b). 

{% figure caption: "Figures 1a and 1b: The first image is a detail of De Couraçaosche Courant from 18 October 1834 showing an ad about an enslaved woman who escaped. The second image shows the transcription provided by Delpher containing OCR errors." %}
![TK]({{site.url}}/assets/img/v08/perez/figure1a.png)
![TK]({{site.url}}/assets/img/v08/perez/figure1b.png)
{% endfigure %}

Fricke purposefully left the OCR errors in the material she annotated for Borenstein so that he could evaluate how the model would perform in real life conditions, where OCR errors are common.

For Danish, we encountered a big challenge. The pool of ads was
significantly smaller, and there are two main reasons for this: we did not have enough time within the pilot project to search all potentially relevant newspapers, and in the Danish colonial newspapers where we did search, the vast majority of the runaway ads appeared in English. Nonetheless, our colleague Rasmus Christensen managed to find eight ads in the Danish language from the newspaper *Sainct Thomæ Tidende*, whose OCR transcription Silva Perez subsequently manually corrected and annotated using the same labels.

### Technical Challenges

There were three pressing challenges that our research team had to face as we advanced our project:

-   Scarcity of collected runaway ads in Danish

-   Refinement of the attributes used for annotation of privacy-related
    events

-   OCR errors in the plain texts provided by libraries and archives

The first challenge, namely, dealing with the scarcity of Danish
language primary source material, seems to be the most difficult problem to tackle since it is a matter of what has survived in the archives. We are working to mitigate this problem by training a different model based on the ColPali vision langauge model to aid in searching and retrieving the ads within the larger context of a full newspaper issue.[^12] This strategy could serve as an alternative to searching for the ads manually, and if successful, could help us save time compiling the datasets.

The second challenge, which is the need to refine the annotation
attributes, seems to us quite straight-forward. With the experience we acquired annotating the pilot project, we learned which strategies work most effectively, and which are least effective. In future experiments, new attribute labels targeted more directly at our research questions can be devised.

Finally, we have the challenge of OCR errors. This is a pervasive
problem that many historians have encountered when trying to do text mining or natural language processing with historical texts.[^13] There seems to be two immediate ways of addressing problems of this kind: one is to try to fix the errors in post-processing (using RegEx, for example), and the second is to do the text recognition anew using more recent technology. For example, using HTR with Transkribus, or purpose-train Tesseract OCR based for our own historical prints. For the moment, our team decided not to try post-processing correction. Instead, we are experimenting with Transkribus and Tesseract OCR to produce our own versions of the corpus in plain text and comparing which of them will deliver the most cost-effective results for the purpose of our project. An alternative solution to the problem of transcription errors resulting from OCR is to bypass the OCR process altogether, by resorting to multimodal models capable of dealing directly with images of texts. As mentioned above, our team is currently working on this strategy using ColPali.

### Preliminary Historical Findings
We worked from the assumption that race and racism emerged, and continue to emerge, as a discursive historical process of social construction.[^14] Thus, in this pilot project, our team examined language used to convey notions of privacy for enslaved people in the colonial period to see what strategies were available for them to obtain privacy. We chose to build a trans-imperial dataset.[^15] By trans-imperial, we mean that discourses about racial perceptions seeped through empires, colonies, languages, and domains of human action, without regard for imposed geopolitical borders. Thus, we worked with historical material from different colonial empires on both sides of the Atlantic. We operationalized our research questions into an NLP task of question-answering using textual data comprised of newspaper ads in French, English, and Dutch about enslaved people who escaped captivity. Though we intended to include Danish in the dataset, it was not possible due to the lack of relevant documents collected in this language. 

We were interested in the way that language used to convey notions of privacy related to language used to convey racial perceptions, and how these linguistic expressions manifested over time and space. These research interest required us to consider a large quantity of written material, therefore, our project was organized as a collaboration between historians of the early modern period and computer scientists who specialize in natural language processing.[^16] By employing a collaborative intelligence approach, we sought to harness the best insights from humans and from machines to achieve a level of analysis that each side alone would not necessarily be able to do.[^17] 

Our process of annotating textual data to evaluate the NLP model led us to some preliminary historical insights about what enslaved people managed to do to obtain privacy. First, the act of running away from the enslaver’s domain is the first step towards privacy. By running away, the enslaved person was putting physical distance between them and their enslaver, which allowed for more control over access to their bodies. Secondly, during the act of escaping, enslaved people had to think about how to guarantee some basic privacy needs, such as warm clothes and blankets for body protection, especially in the case of mothers running away with small children or babies. Thirdly, clothes also provided privacy in the sense of serving as disguise, which enabled to enslaved person running away to remain anonymous or avoid being recognized by their enslavers or those who had been alerted about the escape. These preliminary insights were useful during the annotation phase as we worked to create our model evaluation datasets, but they will also help our team formulate other arguments once our data analysis is completed, allowing us to combine micro and macro analyses in our trans-imperial historical setting. 

### Author's Note
Research for this article received funding from the Sapere Aude grant from the Independent Research Fund Denmark under grant number 2063-00035B, from the University of Copenhagen under a Data Plus 2021 grant for the research project Privacy Black & White, and from the Danish National Research Foundation grant number DNRF138.

### Bibliography

Altman, Irwin. *The Environment and Social Behavior: Privacy, Personal Space, Territory, Crowding.* Brooks/Cole Publishing Company, 1975.

Baker, Paul. *Sociolinguistics and Corpus Linguistics*, Edinburgh Sociolinguistics. Edinburgh University Press, 2010.

Bassi, Ernesto. *An Aqueous Territory: Sailor Geographies and NewvGranada's Transimperial Greater Caribbean World.* Duke University Press, 2017.

Faysse, Manuel, Hugues Sibille, Tony Wu, Bilel Omrani, Gautier Viaud, Céline Hudelot, and Pierre Colombo. "ColPali: Efficient Document Retrieval with Vision Language Models." arXiv, February 28, 2025. <https://doi.org/10.48550/arXiv.2407.01449>.

Jurafsky Daniel and James H. Martin. "Question Answering." In *Speech and Language Processing (Draft): An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition*, 3rd (draft), 2020, 464--91, <https://web.stanford.edu/\~jurafsky/slp3/ed3book.pdf>.

Kaplan, Frederic and Isabella di Lenardo. "Big Data of the Past." *Frontiers in Digital Humanities* 4 (2017): 3--4, <https://www.frontiersin.org/article/10.3389/fdigh.2017.00012>.

Le Glaunec, Jean-Pierre and Léon Robichaud. "Le Marronnage Dans Le Monde Atlantique, 1760-1848." Database, March 9, 2019,
<http://www.marronnage.info/fr/corpus.php>.

Newman, Simon. *Freedom Seekers: Escaping from Slavery in Restoration London.* University of London, 2022,
<https://doi.org/10.14296/202202.9781912702947>.

Newman, Simon P. et al. "Runaway Slaves in Britain: Bondage, Freedom and Race in the Eighteenth Century." Database.
<https://www.runaways.gla.ac.uk>.

Oberbichler, Sarah. et al., "Integrated Interdisciplinary Workflows for Research on Historical Newspapers: Perspectives from Humanities Scholars, Computer Scientists, and Librarians." *Journal of the Association for Information Science and Technology* 73, no. 2 (February 2022): 231--32, <https://doi.org/10.1002/asi.24565>.

Perez, Natália Silva. "Privacy and Social Spaces." *TSEG/ Low Countries Journal of Social and Economic History* 18, no. 3 (December 2021),https://tseg.nl/article/view/11040; Margulis, Stephen T. "Privacy as a Social Issue and Behavioral Concept," *Journal of Social Issues* 59, no. 2 (2003): 243--61, <https://doi.org/10.1111/1540-4560.00063>

"Runaway Slaves in Britain Database Codebook." Database. <https://www.runaways.gla.ac.uk/database/user_guide/Runaway%20Slaves%20in%2018th%20C%20Britain%20-%20Codebook.pdf>.

Wilson, James H. ad Paul R. Daugherty. "Collaborative Intelligence: Humans and AI Are Joining Forces." *Harvard Business Review*, August 2018, <https://hbr.org/2018/07/collaborative-intelligence-humans-and-ai-are-joining-forces>.

Yassine. *Awesome Semi-Supervised Learning*. 2022, <https://github.com/yassouali/awesome-semi-supervised-learning>.

"What Is Question Answering? - Hugging Face," accessed May 20, 2022, <https://huggingface.co/tasks/question-answering>.

### Notes

[^1]: Yassine, Awesome Semi-Supervised Learning, 2022, <https://github.com/yassouali/awesome-semi-supervised-learning>.

[^2]: da Silva Perez, "Privacy and Social Spaces;" Margulis, "Privacy as a Social Issue;" Altman, *The Environment and Social Behavior*.

[^3]: Newman, *Freedom Seekers.*.

[^4]: Le Glaunec and Robichaud. "Le Marronnage Dans Le Monde Atlantique."

[^5]: Jurafsky and Martin, "Question Answering."

[^6]: "What Is Question Answering?", <https://huggingface.co/tasks/question-answering>.

[^7]: Newman et al., "Runaway Slaves in Britain."

[^8]: The newspaper titles are: *Applebee's Original Weekly Journal;Bath Chronicle and Weekly Gazette; Bonner & Middleton's BristolJournal; Bristol Oracle and Country Intelligencer; British Apollo;Caledonian Mercury; Covent Garden Journal; Daily Advertiser; DailyCourant; Daily Journal; Daily Post; Daily Post Boy; EdinburghAdvertiser; Edinburgh Evening Advertiser; Edinburgh Evening Courant;English Post with News Foreign and Domestick; Evening Post; FelixFarley\'s Bristol Journal; Flying Post or The Post Master; FogsWeekly Journal; Gazetteer and Daily Advertiser; Gazetteer and LondonDaily Advertiser; Gazetteer* *and New Daily Advertiser*; *GeneralAdvertiser; General Advertiser (1744); General Advertiser andMorning Intelligencer; General Evening Post; Glasgow Courant;Glasgow Journal; Gloucester Journal; Gore's Liverpool CommercialPamphlet; Liverpool General Advertiser, or the Commercial Register;Lloyd's Evening Post; Lloyd\'s Evening Post and British Chronicle;London Chronicle; London Daily Post and General Advertiser; LondonEvening Post; London Gazette; London Journal; London Post withIntelligence Foreign and Domestick; Manchester Mercury; MorningChronicle and London Advertiser; Northampton Mercury; Observator(1702); Parker's London News or the Impartial Intelligencer; PostBoy (1695); Post Man and the Historical Account; Public Advertiser;Public Ledger; Public Ledger, Or, Daily Register of Commerce andIntelligence; St. James's Evening Post; St. James's Chronicle; St.James\'s Chronicle or the British Evening Post; St. James\'s EveningPost; Weekly Journal or British Gazetteer; Weekly Journal orSaturday's Post; Whitehall Evening Post; Whitehall Evening Post orLondon Intelligencer; Williamson's Liverpool Advertiser;Williamson's Liverpool Advertiser and Mercantile Register*.

[^9]: "Runaway Slaves in Britain Database Codebook", <https://www.runaways.gla.ac.uk/database/user_guide/Runaway%20Slaves%20in%2018th%20C%20Britain%20-%20Codebook.pdf>

[^10]: Le Glaunec and Robichaud, "Le Marronnage Dans Le Monde Atlantique, 1760-1848."

[^11]:The newspaper titles of the ads included in our experiment are: *Affiches américaines; Gazette officielle de la Guadeloupe; Le Moniteur de la Louisiane; Le Télégraphe; The Louisiana Gazette; Le Courrier de la Louisiane; L\'Ami des Lois; Charleston Courier; City Gazette; The Royal Gazette; The Diary and Kingston Daily Advertiser; The Saint Jago Gazette;* and *The Jamaica Courant.*

[^12]: Faysse, Manuel, Hugues Sibille, Tony Wu, Bilel Omrani, Gautier Viaud, Céline Hudelot, and Pierre Colombo. “ColPali: Efficient Document Retrieval with Vision Language Models.” arXiv, February 28, 2025. <doi:10.48550/arXiv.2407.01449>.

[^13]: Oberbichler et al., "Integrated Interdisciplinary Workflows."

[^14]: Baker, *Sociolinguistics and Corpus Linguistics.*

[^15]: Bassi, *An Aqueous Territory.*

[^16]: Kaplan and di Lenardo. "Big Data of the Past," 3--4.

[^17]: Wilson and Daugherty, "Collaborative Intelligence."
