---
title: "Synthesis and Large-Scale Textual Corpora"
subtitle: "A Nested Topic Model of Britain’s Debates over Landed Property in the
Nineteenth Century"
doi: "https://doi.org/10.31835/crdh.2018.01"
volume-number: 1
year: 2018
authors:
- last: Guldi
  first: Jo
  email: jguldi@smu.edu
  affiliation: "Department of History, Southern Methodist University"
  orcid: 0000-0002-5085-0738
  url: "https://www.joguldi.com"
- last: Williams
  first: Benjamin
  email: Benjamin@smu.edu
  affiliation: "Department of Statistical Science, Southern Methodist University"
  orcid: 0000-0001-8474-5066
  url: "https://github.com/williamsbenjamin"
abstract: |
  Scholars need tools that will allow them to generalize about the fit of themes, events, and rhetorical styles represented in a body of texts. In this article, we introduce the concept of “nested topics,” an approach to topic modeling large-scale textual corpora that highlights implicit ontologies and relationships <em>within</em> the texts themselves. This tool exploits the fact that topic modeling can be used to generalize about topics on an aggregate level as well as a fine-grained level, an approach that has the consequences of revealing overarching <em>themes</em> that appear across all texts as well as more idosyncratic events and rehtorical styles that adhere to only a few documents. The tool’s effectiveness is tested by modeling discussions of property in British parliamentary debates in the nineteenth century. Nested topics help the authors to locate the rhetorical styles engaged in by Irish parliamentarians as they defended tenant rights in the 1880s.
appendix:
- name: README
  file: guldi-v01/README.txt
- name: Data archive
  file: guldi-v01/guldi-williams-data.zip
- name: Code archive
  file: guldi-v01/guldi-williams-code.zip
preview: "/assets/img/v01/guldi/preview.png"
---

Faced with a previously-undigested body of documents, how can a scholar
generalize about what semantic, ontological, and emotional relationships
organize that corpus? Digital scholars today frequently have recourse to
a wide and growing array of tools for indexing words, subjects, and
change over time. Yet identifying interesting moments of discontinuity
is not the same as understanding what categories were at stake, and
indexing the subjects of document content is not the same as
understanding how they fit together. To use an example from the print
world: scholarly books often have indices that list important names,
places, and ideas discussed therein, and the digital tools today have
allowed us to create indices for collections of document for which no
card catalog exists. But for the purposes of understanding a book's
organization and orientation, reading a book's index is less instructive
than reading a table of contents. Moreover, a table of contents
typically reveals tension as well as organization: different parts of
the book propose ideas, data or methods that contrast with each other,
and ideally the tension is typically resolved through some argument by
the book's end.

This article offers a method for creating an overview through the
"nesting" of topics, a model process for interpreting better how larger
and smaller discourses "fit" together in the historical ontology
represented by an archive. A nesting process offers a way of annotating
a topic model so as to reveal patterns implicit in the topic model. As
this article will show, nesting offers the promise of not merely
indexing, but also generalizing about different major categories that
the body of documents discusses and how they are related to each other.

Topic modeling itself is an unsupervised form of machine learning
invented in the early 2000s to aggregate content from large collections
of documents.[^1] Since its inception, the technique been applied to an
enormous array of text-focused scholarly work, from the sociological
sorting of arrest records in Los Angeles to the indexing of Thomas
Jefferson's letters.[^2] In history, topic modeling has been applied to
studying urban world-views through newspapers and tracking
advertisements for freed slaves, as well as categorizing the censored
articles in the French *Encylopédie*.[^3] Yet the index provided by
topic modeling does not, on its face, provide an aid to *synthesizing*
some historical truth about a large body of documents, and even
topic-distance measurements, while revealing similarities and likenesses
in the topic model, fail to reveal the ontological and epistemological
hierarchies and tensions at stake in a corpus.

In the project described in this article, topic modeling was applied to
the nineteenth-century debates of Great Britain's House of Commons and
House of Lords, colloquially known as Hansard. The accuracy of Hansard's
record of any particular speech is contested (verbatim reporting was not
entirely accurate until the twentieth century).[^4] Nonetheless, Hansard
offers a convenient vehicle for digital study, made freely available for
at least a decade now, and already the subject of several publications
in political science and historical linguistics.[^5] Because of the
wealth of British historical studies of the period, Hansard also offers
a high standard for testing claims about the usefulness of any
particular digital process; the vast literature on nineteenth-century
political, social, and cultural history, which has already revealed so
much about the the implicit debates and identities governing the flow of
events, partially through the success of the "linguistic turn" of
historical scholarship about politics in the 1990s.[^6] Stories found by
digital means are often recognizable by a trained scholar, and new
findings can be easily identified.

The size of the parliamentary archive---a million speeches and a quarter
billion words---makes the parliamentary debates an ideal subject for
digital investigation. It would be nearly impossible for a single
researcher to apply close reading to parliamentary debate to understand
how categories of property and ownership evolved in the course of
debate, a fact that has long made property law the subject of
intellectual biography rather than horizontal reading. With tools that
direct the researcher to both unpacking overarching context and
identifying local events, however, the possibilities for studying
historical dynamics increases immensely.

The specific nesting process described in this article offers an aid to
moving from indexing towards generalization, helping the scholar to
identify a variety of possible categories in the text from the
large-scale to the small-scale, and to make inferences about how those
categories are related to each other. Nesting takes advantage of the
scalar dimension of topic modeling: the fact that a 4-topic model or a
500-topic model may be made of the same discourse, and that these topics
should necessarily have a hierarchical relationship with each other. The
result of this process, ideally, is a more informed interpretation of
the scholarly context offered by the corpus, as well as a keen sense for
particular parts of the archive where abstract categories are in
tension, for instance, particular parts of the corpus where political
categories elide into emotional or rhetorical ones. Theorizing that the
nesting might reveal an implicit structure to parliamentary discourse
and ideas otherwise obscured from the topic model, a topic model was run
on Hansard at four different scales: once asking the computer for four
topics, once with 20, another time with 100, and finally with 500
topics.

To illuminate how the topic overview can demonstrate previously
invisible connections, this article will turn to the example of Charles
Stewart Parnell and Irish tenant radicalism in the 1880s. As the
research presented below will show, radicals insisted on importance of
"fair rent" in the 1880s, lobbying for measures related to rent control
and expropriation of colonizers' property. The very same practices used
to defend these ideals---the tactics of obstruction and the language of
fairness---were later deployed against Irish Home Rule within a few
decades. By the 1900s, Conservatives regularly cut off Irish speakers
with resort to the importance of "fair play" in parliamentary procedure.

The nesting process helps the scholar to distinguish overarching ideas
about property---which remained more or less steady over the entire
period---from temporary fads and events in property law. The grand
overview of context, at the higher levels of abstraction, can be
distinguished and compared to event, agency, and action at the lower
levels of detail. Applied in detail to parliamentary debates, studying
topic structure promises to reveal connections between high ideals and
universal principles, on the higher levels, and rhetoric or tactics
deployed as part of a debate.

### Nesting as a Process for Revealing Features of Discourse Inherent at Different Scales: Ontological, Institutional, and Temporal

Nesting is comparable to other processes for talking about topic
similarity, for example measuring *topic distance*, which are useful for
understanding clusters of discourses that share overlapping language. In
a t-SNE-based measurement of topic distance in Hansard, a cluster
indeed emerges of related debates about fixed rents, crofters, the
compensation of tenants for improvements to their land, the valuation of
taxes, the valuation of fair rents, about eviction, the valuation of
estates, and discussions of eviction, probably because these discourses
share a common lexicon of acreage, rates, improvement, tenancy, and
rent. Its next nearest relationships are to discussions of agrarian
outrages in Ireland, the Metropolitan Board of Works, the Congested
Districts in Ireland, and the regulation of public houses, topics
suggestive of a common language of regulating public and private spaces,
building infrastructure, and cultivating the economic development of the
working classes.

However, the nesting process differs from these measures of topic
similarity by adding information about *hierarchy* as measured by
reading topics from different scalar perspectives. The property of
having multiple scales is natural to any varied body of textual
materials that represents human expression over time. Large-scale
debates, in terms of the topic model of Hansard, are discourses that
were prevalent across 9--35% of Hansard as a whole, either for reasons of
their ideological prominence (in the case of empire), their
institutional coherence (in the case of the House of Commons itself), or
temporal continuity (in the case of Britain's ongoing relationship with
Ireland and India over the nineteenth century). Smaller-scale topics,
ranging from 0.1%--8% of debate, represent issues that were relatively
less prominent in parliamentary debate---and thus only visible at a
smaller scale of modeling. We theorize that a smaller scale in terms of
topic defines issues whose politics only involved a minority of MPs, for
instance, setting freight rates for the railways; which involved minor
branches of British government, for instance the Metropolitan Police, or
that concerned parliamentary attention for a short period of time, for
instance the Queen Caroline Affair. The process of comparing scales
allows a scholar to contemplate the relationship of discourse to
institution, ontology, and periodization.

Scalar hierarchy demonstrates the fact that different discourses bear
different relationships to periodization. The 4-topic model of Hansard,
working at a grand scale, divides Hansard into four major *genres* of
debate, all of which were relatively persistent across the period as a
whole: one about taxation, one about empire and war, one about
extra-parliamentary government, including schools, hospitals, churches,
and towns; and one about the practical matter of presenting bills and
making speeches in parliament. A 500-level topic model, by contrast,
subdivides the genres of parliamentary speech into discourses
recognizable as linked to specific *events* familiar to a historian: the
creation of the Metropolitan Board of Works (1855--1889), the
improvements related to the Metropolitan Commission of Sewers in
185--89, and the building of the Thames Embankment from 1862.

***Table 1. Four-topic Model of Hansard***

| Proportion of Hansard as a whole | Scholar-assigned name | Top 20 Keywords |
|---|---|---|
| 34.85% | Extra-parliamentary Affairs | bill make government member committee house give question gentleman case board matter school clause secretary amendment act year ireland county |
| 11.58% | The Formalities of Presenting in Parliament | house noble bill lord member make great law country give question present measure government state case gentleman opinion time ireland |
| 9.20% | Revenue and expenditure | year country great make land duty house gentleman pay tax tenant amount present ireland give government interest landlord member increase |
| 22.09% | Empire and warfare | government make state country war lord question year great give officer sir house men time india secretary service army noble |

***Table 2. Excerpt from a 500-topic Model of Hansard***

| Proportion of Hansard as a whole | Scholar-assigned name | Top 20 Keywords |
|---|---|---|         
| 0.926% | Sewerage and river pollution | river drainage work sewage board navigation water carry works district drain flood sewer conservancy pollution improvement engineer stream nuisance main |
| 1.07% | The Thames Embankment and other improvements | street bridge public improvement embankment traffic metropolis road side metropolitan propose great foot carry make thoroughfare house plan place parliament |
| 0.904% | The Metropolitan Board of Works | metropolis metropolitan board works district vestry ratepayer local body area central sir power act chairman common question city management inhabitant |

The two scales of topic analysis may also be fitted together, with the
potential of better understanding hierarchical and governing
relationships between large-scale concepts at the macro-level and actual
events at the micro-level. The process of nesting smaller topics within
larger questions raises issues of language and institution that are not
answered by measures of topic proximity, for instance: were the rights
of Irish tenants debated mostly under the heading of taxation, in the
same language as any other debate over property in England? Or did they
occur in the context of other debates about empire and warfare that
stressed the status of Irishmen as colonial subjects?

A scholar-prepared nested topic model was made by modeling the debates
of Hansard, 1800--1910, at 4, 20, 100, and 500 topics, which we have
labeled the "trunk", "bough", and "branch topics." The trunk corresponds
to the most abstract version of topic-modeling, where the computer has
classified debates in only four categories, which loosely correspond to
the rhetoric of parliament, empire, revenue, and expenditure---wide
domains of parliamentary concern at their most generic level. As the
nested topic model branches out from the trunk towards the stem and
leaves, it becomes more detailed, until individual topics refer not to
general processes but rather to particular principles (for instance,
property law), ongoing debates (for instance, fox hunting), or events
(as this paper explains below).

In the first iteration, the hierarchy was created by hand, based on the
repetition of keywords in the top 20 words most relevant to a topic (for
instance, "pay" in the "Revenue and Expenditure" trunk and in the
"Landlords, tenants, and property questions" bough), or because of
seeming overlap of content (for instance, "price" in the "Customs and
Corn Laws" bough). Based on a naive reading of the topic hierarchy,
property appears to be most closely related to taxation rather than to
questions of empire. At the level of trunk and bough topics, land
appears closely related to discussions of taxation, nationhood, and
Ireland, mirroring a familiar imperial discourse where revenue and
political economy predominated. Three property terms ("land," "tenant",
and "landlord") rank within the 20 most significant terms of the tax
revenue topic itself.

The nested topic model allows us to distinguish particular sub-genres of
concern with land that would be less universally relevant to MP's across
the century and more particular to certain time periods, institutions,
and issues. The subcategories of landholding that appear within this
model are three: "taxes paid to the exchequer," "landlords, tenants, and
property questions," and "customs and the corn laws." Indeed,
nineteenth-century historians are familiar with three very different
debates about local taxation, the role of tenants and landlords in
improving the agrarian economy, and free trade and the price of bread,
each of which invoked a similar lexicon ("land", "country", "tax",
"tenant", "landlord") within the context of very different ideas.[^7]

***Table 3. "Revenue and Expenditure" (Trunk Category), with Three Subcategories of Debate***[^8]

<table>
  <thead>
    <tr>
      <th>Prop.</th>
      <th>Scholar-assigned name</th>
      <th>Scholar-nested Bough Topics (20-topic model)</th>
      <th>Scholar-nested Trunk Topic (4-topic model)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>8.31%</td>
      <td>Taxes paid to the Exchequer</td>
      <td>tax year pay exchequer duty amount chancellor make gentleman revenue income taxation increase sum expenditure money fund property present country</td>
      <td rowspan="3" style="vertical-align:top;"><strong><em>“Revenue and Expenditure”:</em></strong> <em>year country great make land duty house gentleman pay tax tenant amount present ireland give government interest landlord member increase</em></td>
    </tr>
    <tr>
      <td>4.14%</td>
      <td>Landlords, tenants, and property questions</td>
      <td>land tenant landlord rent estate farm purchase case act property pay lease holding year commissioners improvement acre farmer sale sell</td>
    </tr>
    <tr>
      <td>4.33%</td>
      <td>Customs and the Corn Laws</td>
      <td>country trade duty great year price present measure state interest increase member house foreign system make law corn produce distress</td>
    </tr>
  </tbody>
</table>

Each of of the "bough" categories of land can also be traced as it
separates into further "branch" subgenres that suggest how particular
debates, for example about taxes, varied with respect to institutions,
time, and ideology. Beneath taxes are two further specifically
quantitative discourses for defining land: "local rates," or the setting
of local taxes as a function of land prices; and "the valuation of the
correct price of land," a controversial surveyor's technique for
determining taxes and/or rent prices as a reflection of geology. Here,
the distinction between different discourses of land is again familiar
to a specialist in the history of taxation and surveying, who can
distinguish in these three subcategories of land three different periods
of debating parliament's role in calculating and improving land value: a
long nineteenth-century debate over local versus national interest in
the sources of taxation, and a new conversation from the 1850s about the
scientific determination of tax rates through the use of valuation,
which fixed rates to geology as determined by a professional
surveyor.[^9]

***Table 4. Taxes Paid to the Exchequer (Bough Category) and Three Sub-Branch Subcategories of Debate***

<table>
  <thead>
    <tr>
      <th>Prop.</th>
      <th>Scholar-assigned name</th>
      <th>Scholar-nested Branch Topics (100-topic model)</th>
      <th>Scholar-nested Bough Topic (20-topic model)</th>
      <th>Scholar-nested Trunk Topic (4-topic model)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.21%</td>
      <td>Valuation of the correct price of rent</td>
      <td>rent tenants years land made rents valuation cases improvements acres man time estate paid good farm pay tenant-right raised don’t</td>
      <td rowspan="2" style="vertical-align:top;"><strong><em>“Taxes Paid to the Exchequer”:</em></strong> <em>tax year pay exchequer duty amount great make land chancellor make gentleman revenue income taxation increase sum expenditure money fund property present country</em></td>
      <td rowspan="2" style="vertical-align:top;"><strong><em>“Revenue and Expenditure”:</em></strong> <em>year country duty house gentleman pay tax tenant amount present ireland give government government member increase</em></td>
    </tr>
    <tr>
      <td>2.11%</td>
      <td>Local rates (i. e., taxes for local government), esp. from land</td>
      <td>rate pay local amount land taxation property charge burden government rating assessment tax poor make valuation relief parish levy ratepayer</td>
    </tr>
  </tbody>
</table>

The bough topic, "landlords, tenants, and property questions," in turn
splits into three branch topics: "improvement and rent as regulated by
parliament," or a discussion about parliament's duty to encourage the
upward or downward tendency of rent; "hunting", a treatment of deer
parks and game laws, and "the tithe," on the payment of land taxes to
the church. Again, the debates are familiar to a historian: a
seventeenth-century conversation about landlord-based improvement and
the scientific economy of the agrarian estate which later became a
debate over tenant-right; an eighteenth-century debate about the rights
of lords and tenants to wild game from the forest, and a specifically
nineteenth-century debate about the the disestablishment of the church
in Ireland, which raised important questions about agricultural taxation
and the ownership of church lands.[^10]

***Table 5. Landlords, Tenants, and Property Questions (Bough Category) and Three Sub-Branch Subcategories of Debate, as Assigned by Scholar***

<table>
  <thead>
    <tr>
      <th>Prop.</th>
      <th>Scholar-assigned name</th>
      <th>Scholar-nested Branch Topics (100-topic model)</th>
      <th>Scholar-nested Bough Topic (20-topic model)</th>
      <th>Scholar-nested Trunk Topic (4-topic model)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.21%</td>
      <td>The Value of Tenant Improvements</td>
      <td>rent tenants land years made rents valuation cases improvements acres man time farm paid estate good tenant-right act pay raised</td>
      <td rowspan="6" style="vertical-align:top;"><strong><em>“Landlords, Tenants, and Property”:</em></strong> <em>land tenant landlord estate farm purchase case act holding year commissioners improvement acre farmer sale sell</em></td>
      <td rowspan="6" style="vertical-align:top;"><strong><em>“Revenue and Expenditure”:</em></strong> <em>year country great make land duty house gentleman pay tax tenant amount present ireland give government interest landload member increase</em></td>
    </tr>
    <tr>
      <td>1.89%</td>
      <td>Landloard Compensation of Tenants for Improvements, the Court as Intermediary</td>
      <td>tenant landlord rent land year case pay act improvement lease make compensation farm give hold fair farmer court government property</td>
    </tr>
    <tr>
      <td>2.139%</td>
      <td>Small Farmers and Tenant Farmers</td>
      <td>land agricultural labourer small acre farmer agriculture farm holding crofter district cottage allotment act purpose highlands owner county condition rent</td>
    </tr>
    <tr>
      <td>1.7%</td>
      <td>The Tithe</td>
      <td>property tithe land estate case pay duty interest make sale year person owner sell real amount law charge title settlement</td>
    </tr>
    <tr>
      <td>2.837%</td>
      <td>Land - Buying, Selling, Evictions</td>
      <td>land purchase estate sale commissioners sell tenant estates act price case buy owner holding farm evicted property chief make purchaser</td>
    </tr>
    <tr>
      <td>3.059%</td>
      <td>Unemployment, Starvation, and Emigration</td>
      <td>people country distress state great population condition measure evil labour district employment part class emigration land money remedy work person</td>
    </tr>
  </tbody>
</table>

The 20-level topic "customs and the corn laws" refers to debates about
the import and export of goods from Britain, as marked by a tension
between land and manufacture that emerged early in the nineteenth
century. Much of the writing of the economist and member of parliament
David Ricardo was attached to understanding the political and economic
rivalry between the landed and manufacturing interests. In an era of
free trade, working-class movements associated with the Manchester
School urged on the removal of the Corn Laws established at the
beginning of the century to protect British farmers from fluctuation in
grain prices. At the same time, Manchester's cotton interest lobbied for
other protective legislation to keep the price of cotton low.[^11] Three
subtopics found by the computer index debates relevant to these
developments: "improvement and rent as debated in parliament," "the
valuation of the correct price of rent," and "local rates." Portions of
this debate gave rise to a conversation about rural riot and the
distress of rural laborers, hence the grouping together of topics about
"the Corn Laws and agricultural prices" with debates over "unemployment
and relief works."

***Table 6. Customs and the Corn Law (Bough Category) and Three Sub-Branch Subcategories of Debate, as Assigned by Scholar***

<table>
  <thead>
    <tr>
      <th>Prop.</th>
      <th>Scholar-assigned name</th>
      <th>Scholar-nested Branch Topics (100-topic model)</th>
      <th>Scholar-nested Bough Topic (20-topic model)</th>
      <th>Scholar-nested Trunk Topic (4-topic model)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.66%</td>
      <td>The Corn Laws and agricultural prices</td>
      <td>price corn country agricultural interest duty year farmer law protection great measure distress produce foreign wheat present state quarter agriculture</td>
      <td rowspan="3" style="vertical-align:top;"><strong><em>“Customs and the Corn Laws":</em></strong> <em>country trade duty great year price present measure state interest increase member house foreign system make law corn produce distress</em></td>
      <td rowspan="3" style="vertical-align:top;"><strong><em>“Revenue and Expenditure”:</em></strong> <em>year country great make land duty house gentleman pay tax tenant amount present ireland give government interest landload member increase</em></td>
    </tr>
    <tr>
      <td>2.013%</td>
      <td>Unemployment and relief works</td>
      <td>distress people relief work government district money emigration employment land condition state country give make population labour poor food relieve</td>
    </tr>
    <tr>
      <td>2.21%</td>
      <td>Customs and taxes on cotton and other imports</td>
      <td>trade country duty foreign commercial manufacture article export import good free british commerce great interest manufacturer united produce cotton increase</td>
    </tr>
  </tbody>
</table>

Finally, "Customs and the Corn Laws" breaks down into three further
subcategories: "The Corn laws and agricultural prices," interfacing with
a conversation about distress and prices; "unemployment and relief
works," a direct encounter with the problem of starvation and
emigration; and "customs and taxes on cotton and other imports," a
discourse explicitly about free trade with respect to a variety of
commodities. These categories as well are familiar to historians of
empire and political economy, who will recognize in them debates about
the repeal of the Corn Laws and the agricultural interest; a discussion
of the role of Corn Laws in driving distress and emigration among the
working classes, especially around Ireland during the Famine; and an
ideology of Britain as the leading nation of Free Trade.

Some preliminary observations about these categories have to do with
linkages between keyword temporality and hierarchy in the nested model.
The higher in topic hierarchy a term, the more pervasive it was. Where a
keyword such as "improvement" appears at multiple levels of a nested
topic model, it shows how a dominant ideology continued to structure new
modes of thought, for instance, early-modern ideas of "improvement" and
Blackstonean "property" being worked out through Mill's concept of the
"magic of property" all the way through the land reforms of the 1880s
and 1890s. Thus a nested topic model can be a tool for discerning
*longue durée* persistence in ideology, contrasted against shorter-term
revisions such as valuation or distress.

Machine-nesting subcategories within a hierarchy potentially provides an
added layer of information. We used JS divergence to automatically
detect hierarchical relationships between topics, with results very
different from those in the hand-nested model. We attribute this
difference to the relative significance to parliamentary *expression* of
less-prevalent terms in the topic model, i.e., terms whose ranking fell
below the 20 top keywords used in the scholarly nesting process.

Reviewing the machine-nested relationships thus has the potential to
reveal hierarchies based less on *ideologically dominant keywords* than
on *rhetorical expression*. Subcategories of "*Landlords, Tenants, and
Property Questions*," according to the computer, included two subtopics
that suggest the kind of formal speech frequently interjected by
objectors about tenant right: "*Objections to a New Bill*," and
"*Eulogizing the Importance of Government Time*" (see figure 7).

***Table 7. Comparing Scholar-Nested and Machine-Nested topics for "Landlords, Tenants, and Property"***

<table>
  <thead>
    <tr>
      <th>Prop.</th>
      <th>Scholar-assigned name</th>
      <th>Scholar-nested Branch Topics (100-topic model)</th>
      <th>Scholar-nested Bough Topic (20-topic model)</th>
      <th>Scholar-nested Trunk Topic (4-topic model)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3.129%</td>
      <td>Improvement and rent as regulated by parliament</td>
      <td>tenant land landlord rent act case farm purchase estate year holding improvement pay make lease hold give farmer fair compensation</td>
      <td rowspan="3" style="vertical-align:top;"><strong><em>“Landlords, Tenants, and Property":</em></strong> <em>land tenant landlord rent estate farm purchase case act property pay lease holding year commissioners improvement acre farmer sale sell</em></td>
      <td rowspan="3" style="vertical-align:top;"><strong><em>“Revenue and Expenditure”:</em></strong> <em>year country great make land duty house gentleman pay tax tenant amount present ireland give government interest landload member increase</em></td>
    </tr>
    <tr>
      <td>1.294%</td>
      <td>Hunting</td>
      <td>game patent forest land dog experiment horse farmer common animal invention sport acre purpose deer woods ground shoot kill damage</td>
    </tr>
    <tr>
      <td>2.061%</td>
      <td>The Tithe</td>
      <td>property tithe land estate case pay duty interest make sale year person owner sell real amount law charge title settlement</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Prop.</th>
      <th>Scholar-assigned name</th>
      <th>Machine-nested Branch Topics (100-topic model)</th>
      <th>Machine-nested Bough Topic (20-topic model)</th>
      <th>Machine-nested Trunk Topic (4-topic model)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>9.51%</td>
      <td>Objections to a New Bill</td>
      <td>bill measure house pass introduce reading present propose principle object provision committee give time session law oppose clause objection move</td>
      <td rowspan="7" style="vertical-align:top;"><strong><em>“Landlords, Tenants, and Property":</em></strong> <em>land tenant landlord rent estate farm purchase case act property pay lease holding year commissioners improvement acre farmer sale sell</em></td>
      <td rowspan="7" style="vertical-align:top;"><strong><em>“The Formalities of Presenting in Parliament”:</em></strong> <em>house noble bill lord member make great law country give question present measure government state case gentleman opinion time ireland</em></td>
    </tr>
    <tr>
      <td>1.56%</td>
      <td>Eulogizing the Importance of Government Time</td>
      <td>house members rule business government time private resolution discussion rules proposal debate bills committees session discuss day speaker supply resolutions</td>
    </tr>
    <tr>
      <td>6.74%</td>
      <td>Reports of Evidence of Persons Interviewed by Committees</td>
      <td>committee report inquiry house select appoint member evidence question refer inquire subject members matter appointment committees propose recommendation opinion move</td>
    </tr>
    <tr>
      <td>5.30%</td>
      <td>Correspondence with Foreign Governments</td>
      <td>government foreign majesty state secretary sir affairs subject powers information receive make convention conference regard territory consul question papers despatch</td>
    </tr>
    <tr>
      <td>8.59%</td>
      <td>Presenting Official Documents to Parliament</td>
      <td>lay return table house information report paper give copy correspondence present papers objection returns document move print receive parliament state</td>
    </tr>
    <tr>
      <td>1.95%</td>
      <td>Coercion Acts to Suppress Dissent in the Colonies</td>
      <td>government law meeting people act crime person league outrage men man coercion country state lord secretary put power case offence</td>
    </tr>
    <tr>
      <td>2.14%</td>
      <td>Small Farmers and Tenant Farmers</td>
      <td>land agricultural labourer small acre farmer agriculture farm holding crofter district cottage allotment act purpose highlands owner county condition rent</td>
    </tr>
  </tbody>
</table>

Indeed, the top debates linked to "Landlords, Tenants, and Property
Question" reveal the coincidence of Irish tenant- and home-rule
agitation with a strategy of parliamentary interruption. Other subtopics
are suggestive of the Irish lobby's strategies. "*Reports of Evidence of
Persons Interviewed by Committees*," "C*orrespondence with Foreign
Governments,*" and "*Presenting Official Documents to Parliament*."
These topics suggest how Irish representatives made use of parliamentary
reports and their interviews with victims of rack-renting or eviction to
command attention in the house. The two remaining subtopics, "*Coercion
Acts to Suppress Dissent in the Colonies*" and "*Small Farmers and
Tenant Farmers*," suggest the commonplace speaking points of the Irish
lobby.

The top debate associated with "Landlords, Tenants, and Property" is
actually a debate about the new procedure rules introduced by Alfred
Balfour as leader of the House of Commons in 1902. Landlords and tenants
are nowhere mentioned in the debate. Balfour had overseen the
battering-ram campaign against rent-striking Irish tenants from 1887,
before executing a plan of railways and government-backed land purchase
to create a peasant proprietary.[^12]

The case of the "Landlords, Tenants, and Property" topic illustrates
both the difficulty of using topics as shorthand for *discourse*: the
"Landlords, Tenants, and Property" topic is clearly more complicated
than simply discussions of land. But the topic is infused with both the
presence of participants in the land struggle: Ireland, the Colonial
Office, and Balfour himself. Present too are issues of Irish
independence and economic wellbeing ("improvement"), and the objections
and diversions of colonial debate that typified the tactics of the Irish
representatives both during the land war of the 1880s and during the
movement for Home Rule thereafter.

Thus there are aspects of debate revealed by the nested topic model that
are otherwise obscured by the topic model. A naive observer might choose
to believe that "Landlords, Tenants" was a dead ringer for property and
be disappointed by top debates, and use the topic as an index for
debates about property. The topic model would fail the scholar,
returning not the most important debates about landlords and tenants,
but rather a subset of debates where Irish issues, including tenancy,
intersected with parliamentary procedure.

However, with the nested topics aided by computerized determination of
topic hierarchy, a careful user will note the coincidence between
debates about smallholders and debates about parliamentary procedure,
and find room for investigation. In the top debates linked to
"Landlords, Tenants" a researcher will then find copious evidence that
debates over the colonies and land rights in the 1880s and 1890s
coincided with a parliamentary tactic of interruption, igniting a battle
for control over parliamentary procedure.

Parliamentary time became scarcer after the Reform Act of 1867, as an
increasing number of MP's depended upon having their speeches profiled
in newspapers to retain the support of their voters. A larger proportion
of members of parliament turned out to vote, and more members spoke than
in previous decades.The Irish lobby specialized in tactics using the
shortness of parliamentary time to their advantage. After the 1850s,
Irish members of parliament developed what Kari Palonen has called
"obstructionist tactics" to insure the hearing of Irish causes, among
them tenant rights to fair rent and freedom from eviction.[^13]

### Conclusion

Machine-calculated nesting of hierarchical topics allows the scholar to
add a layer of critical reflection to the indexing of discourses with
topic models. Nesting topics at different scales opens up general
questions about longue-duree versus event-related periodization of
concepts. Machine-nesting corrects for scholarly bias with the actual
content of speeches, where significant nodes of debate may be less
intuitive than they appear at first.

Hierarchical nesting, both by scholarly assignment and by
machine-calculated nesting, represents one way of trying to capitalize
on the scalar and mathematical properties inherent to topic models on
large-scale data collections where documents are harvested from a wide
variety of speakers working on debates that changed over time. By
extrapolating the mathematical properties of topics at different scales,
our potential appreciation of what any given keyword is doing in a topic
model is enhanced, and with it, our ability to identify and interpret
important changing points in the history of concepts.

Grand comparisons of scale lend themselves to studying the interplay of
context and event: to precise debates located in time that matter for
the study of history. With nested topics, the scholar can track
strategic rhetorical moves and other political events in the corpus,
dynamic features of history that are hard to trace with topic models.
The insight lent by nested topics is their power to reveal the
conjunction between *macrocosmic* categories such as thematic context or
general lexicon and *microcosmic* categories defined by event, agency,
and rhetoric, themes that have frequently been at the heart of
traditional practices of history. In this way, nesting topics allows the
scholar to forge a synthesis that tacks back and forth between evidence
at different scales, encompassing both the macroscopic view of the
*longue durée* and the microscopic material of encounters between
individual lives over the scale of months, years, or a decade.

Nesting topics is but one possible tool to lend precision, insight, and
synthesis to the capabilities of a scholar interested in a particular
theme or event in history. Yet the work of digital tool-building is far
from over. In order to further understand the play between context and
event, future work will be needed to create a tool that dramatizes the
relationship between nested subfields and time. Further steps in the
investigation of nested topics might include separating the substantive
questions of debate from rhetorical figures of speech through
part-of-speech tagging and stop-wording. As digital scholars learn to
make better use of tools such as computer-aided nesting that extrapolate
the properties of historical debates, our ability to identify complex
conjunctions of rhetoric and politics will also grow.

---

### Bibliography

Alexander, Marc. "The metaphorical understanding of *power and authority*." In *Mapping English Metaphor Through Time*, edited by Wendy Anderson, Ellen Bramwell, and Carole Hough, 191--207. Oxford: Oxford University Press, 2016. <https://doi.org/10.1093/acprof:oso/9780198744573.001.0001>.

Alexander, Marc, and Andrew Struan. "Digital Hansard: Politics and the Uncivil." *DH 2017*. <https://dh2017.adho.org/abstracts/007/007.pdf>.

Blaxill, Luke. "Quantifying the Language of British Politics, 1880--1910." *Historical Research* 86, no. 232 (May 1, 2013): 313--41. <https://doi.org/10.1111/1468-2281.12011>.

Blei, David M, and John D Lafferty. "A Correlated Topic Model of
Science." *Ann. Appl. Stat.* 1, no. 1 (2007): 17--35. <https://doi.org/10.1214/07-AOAS114>.

Blei, David M. "Probabilistic Topic Models." *Commun. ACM* 55, no. 4
(April 2012): 77--84. <https://doi.org/10.1145/2133806.2133826>.

Blei, David M., Andrew Y. Ng, and Michael I. Jordan. "Latent Dirichlet
Allocation." *Journal of Machine Learning Research* 3 (January 2003): 993--1022. <http://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf>.

Blevins, Cameron. "Space, Nation, and the Triumph of Region: A View of
the World from Houston." *Journal of American History* 101, no. 1
(June 1, 2014): 122--47. <https://doi.org/10.1093/jahist/jau184>.

Boyd-Graber, Jordan, Yuening Hu, and David Mimno. "Applications of
Topic Models." *Foundations and Trends® in Information Retrieval* 11,
no. 2--3 (July 20, 2017): 143--296. <https://doi.org/10.1561/1500000030>.

Briggs, Asa. *The Age of Improvement, 1783-1867*. New York: D. McKay, 1962.

Burns, Arthur. "English 'Church Reform' Revisited, 1780--1840." In
*Rethinking the Age of Reform*, edited by Joanna Innes and Lyndal
Roper, 136--62. Cambridge: Cambridge University Press, 2011.

Cragoe, Matthew, and Paul Readman, eds. *The Land Question in Britain, 1750--1950*. New York: Palgrave Macmillan, 2010.

Curtis, L. Perry. "The Battering Ram and Irish Evictions, 1887--90."
*Éire-Ireland* 42, no. 3 (December 10, 2007): 207--28. <https://doi.org/10.1353/eir.2007.0039>.

Dalins, Janis, Campbell Wilson, and Mark Carman. "Criminal Motivation
on the Dark Web: A Categorisation Model for Law Enforcement." *Digital
Investigation* 24 (March 1, 2018): 62--71. <https://doi.org/10.1016/j.diin.2017.12.003>.

Eggers, Andrew C., and Arthur Spirling. "The Shadow Cabinet in
Westminster Systems: Modeling Opposition Agenda Setting in the House
of Commons, 1832--1915." *British Journal of Political Science* 48, no. 2 (2018): 343–-67. Published online April 11 2016. <https://doi.org/10.1017/S0007123416000016>.

Griffin, Emma. *Blood Sport: Hunting in Britain Since 1066*. New
Haven; London: Yale University Press, 2008.

Griffiths, Clare V. J. *Labour and the Countryside: The Politics of
Rural Britain 1918-1939*. Oxford Historical Monographs. Oxford: Oxford
University Press, 2007.

Guo, Lei, Chris J. Vargo, Zixuan Pan, Weicong Ding, and Prakash
Ishwar. "Big Social Data Analytics in Journalism and Mass
Communication Comparing Dictionary-Based Text Analysis and
Unsupervised Topic Modeling." *Journalism & Mass Communication
Quarterly* 93, no. 2 (June 1, 2016): 332--59. <https://doi.org/10.1177/1077699016639231>.

Hilton, Boyd. *Corn, Cash, Commerce: The Economic Policies of the Tory
Governments 1815-1830*. London: Oxford University Press, 1977.

Kivell, P.T. and I. McKay. "Public ownership of urban land." *Transactions of the Institute of British Geographers* 13 (1988): 165--78.

Klein, Lauren, and Jacob Eisenstein. "Reading Thomas Jefferson with
TopicViz: Towards a Thematic Method for Exploring Large Cultural
Archives." *Scholarly and Research Communication* 4, no. 3 (2013). <https://doi.org/10.22230/src.2013v4n3a121>.

McKenzie-McHarg, Andrew, and Rolf Fredheim. "Cock-Ups and Slap-Downs:
A Quantitative Analysis of Conspiracy Rhetoric in the British
Parliament 1916--2015." *Historical Methods: A Journal of Quantitative
and Interdisciplinary History* 50, no. 3 (July 3, 2017): 156--69. <https://doi.org/10.1080/01615440.2017.1320616>.

Mitrofanova, Olga, and Anastasiia Sedova. "Topic Modelling in Parallel
and Comparable Fiction Texts (the Case Study of English and Russian
Prose)." *Proceedings of the International Conference IMS-2017*,
175--180. New York, NY, USA: ACM, 2017. <https://doi.org/10.1145/3143699.3143734>.

Mohr, John W., and Petko Bogdanov. "Introduction---Topic Models: What
They Are and Why They Matter." In "Topic Models and the
Cultural Sciences." Special issue, *Poetics* 41, no. 6 (December 1, 2013): 545--69. <https://doi.org/10.1016/j.poetic.2013.10.001>.

Mollin, Sandra. "The Hansard Hazard: Gauging the Accuracy of British
Parliamentary Transcripts." *Corpora* 2, no. 2 (November 1, 2007):
187--210. <https://doi.org/10.3366/cor.2007.2.2.187>.

Newman, David J., and Sharon Block. "Probabilistic Topic Decomposition
of an Eighteenth-Century American Newspaper." *Journal of the American
Society for Information Science and Technology* 57, no. 6 (April 1,
2006): 753--67. <https://doi.org/10.1002/asi.20342>.

Palonen, Kari. *Politics of Parliamentary Procedure: The Formation of
the Westminster Process*. Opladen: Barbara Budrich, 2016.

Readman, Paul. *Land and Nation in England: Patriotism, National
Identity, and the Politics of Land, 1880--1914*. Woodbridge, UK:
Boydell Press, 2008.

Reilly, James R. *Richard Griffith and His Valuations of Ireland: With
an Inventory of the Books of the General Valuation of Rateable
Property in Ireland*. Baltimore, MD: Clearfield, 2000.

Riddell, Allen B. “How to Read 22,198 Journal Articles: Studying the History of German Studies with Topic Models.” In *Distant Readings: Topologies of German Culture in the Long Nineteenth Century*, edited by Matt Erlin and Lynne Tatlock, 91–-114. Rochester, New York: Camden House, 2014.

Ridley, Jane. "Arthur Balfour." In *Modern British Statesmen, 1867-1945*, edited by Richard N. Kelly and John Cantrell, 97--110. Manchester: Manchester University Press, 1997.

Roe, Glenn, Clovis Gladstone, and Robert Morrissey. "Discourses and
Disciplines in the Enlightenment: Topic Modeling the French
*Encyclopédie*." *Frontiers in Digital Humanities* 2 (2016). <https://doi.org/10.3389/fdigh.2015.00008>.

Slack, Paul. *The Invention of Improvement: Information and Material
Progress in Seventeenth-Century England*. Oxford: Oxford University
Press, 2015.

Tangherlini, Timothy R, Vwani Roychowdhury, Beth Glenn, Catherine M
Crespi, Roja Bandari, Akshay Wadia, Misagh Falahi, Ehsan Ebrahimzadeh,
and Roshan Bastani. "'Mommy Blogs' and the Vaccination Exemption Narrative: Results From A Machine-Learning Approach for Story Aggregation on Parenting Social Media Sites." *JMIR Public Health and
Surveillance* 2, no. 2 (November 22, 2016): e166. <https://doi.org/10.2196/publichealth.6586>.

Thompson, James. "After the Fall: Class and Political Language in
Britain, 1780--1900." *The Historical Journal* 39, no. 3 (September 1996): 785--806. <https://doi.org/10.1017/S0018246X00024572>.

Trentmann, Frank. *Free Trade Nation: Commerce, Consumption, and Civil
Society in Modern Britain*. 1st paperback ed. Oxford: Oxford
University Press, 2009.

Vaughan, William. *Landlords and Tenants in Mid-Victorian Ireland*. Oxford: Clarendon Press, 1994.

Wahrman, Dror. "Virtual Representation: Parliamentary Reporting and
Languages of Class in the 1790s." *Past and Present* 136 (1992):
83--113. <https://doi.org/10.1093/past/136.1.83>.

---

### Notes

[^1]: Blei, Ng, and Jordan, "Latent Dirichlet Allocation," 993--1022;
    Blei and Lafferty, "A Correlated Topic Model," 17--35; Blei,
    "Probabilistic Topic Models," 77--84; Mohr and Bogdanov,
    "Introduction---Topic Models," 545--69.

[^2]: A good overview of the literature is Boyd-Graber, Hu, and Mimno,
    "Applications of Topic Models," 143--296. To give merely a sample of
    the voluminous literature applying topic modeling: Dalins, Wilson,
    and Carman, "Criminal Motivation," 62--71; Guo et al., "Big Social
    Data Analytics," 332--59; Mitrofanova and Sedova, "Topic Modelling,"
    175--180; Tangherlini et al., "'Mommy Blogs'", e166; Riddell, "How to
    Read," 91--114; Klein and Eisenstein, "Reading Thomas Jefferson."

[^3]: Roe, Gladstone, and Morrissey, "Discourses and Disciplines";
    Blevins, "Space, Nation, and the Triumph of Region," 122--47; Mohr
    and Bogdanov, "Introduction---Topic Models," 545--69; Newman and
    Block, "Probabilistic Topic Decomposition," 753--67.

[^4]: Mollin, "The Hansard Hazard," 187--210.

[^5]: Eggers and Spirling, "The Shadow Cabinet," 343--67; Alexander, "The
    Metaphorical Understanding," 191--207; Blaxill, "Quantifying the
    Language," 313--41; McKenzie-McHarg and Fredheim, "Cock-Ups and
    Slap-Downs," 156--69.

[^6]: Wahrman, "Virtual Representation," 83--113; Thompson, "After the
    Fall," 785--806.

[^7]: For a sample of the wide literature on these debates, see Hilton,
    *Corn, Cash, Commerce*; Trentmann, *Free Trade Nation*; Vaughan,
    *Landlords and Tenants*; Griffiths, *Labour and the Countryside*;
   Cragoe and  Readman, *The Land Question in Britain*.

[^8]: The authors are grateful to Katherine Harclerode and Christopher
    Stampone of Southern Methodist University for help in labeling the
    500-topic model. We are also grateful to Andras Zsom and Ashley Lee
    of Brown Data Science for helping in cleaning and processing the
    data.

[^9]: For more on the history of these debates, see Reilly, *Richard
    Griffith*; Kivell and McKay, "Public Ownership," 165--78.

[^10]: Griffin, *Blood Sport*; Briggs, *The Age of Improvement*; Slack,
    *The Invention of Improvement*; Burns, "English 'Church Reform',"
    136--62.

[^11]: Hilton, *Corn, Cash, Commerce*; Trentmann, *Free Trade Nation*.

[^12]: Ridley, "Arthur Balfour," 97--110; Curtis, "The Battering Ram," 207--28.

[^13]: Palonen, *Politics of Parliamentary Procedure*, 50.
