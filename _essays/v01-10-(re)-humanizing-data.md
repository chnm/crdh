---
title: "(Re)Humanizing Data"
subtitle: "Digitally Navigating the Bellevue Almshouse"
doi: "https://doi.org/10.31835/crdh.2018.10"
volume-number: 1
year: 2018
authors:
- last: Shrout
  first: Anelise Hanson
  email: ashrout@bates.edu
  affiliation: "Digital and Computational Studies, Bates College"
  orcid: 0000-0001-6277-0607
  url: "http://www.anelisehshrout.com"
abstract: |
  Fleeing poverty, disease and violence at home, thousands immigrated to New York City in the 1840s. In an unknown city, with little support, many became destitute. City officials responded by consigning immigrants to the Bellevue Hospital Almshouse. There they were diagnosed as “vagrant,” “destitute” and “recent emigrant” and incarcerated in New York’s nascent public health system. This paper uses computational methods to reconstruct the experiences of incarcerated immigrants. It demonstrates the (often archivally invisible) forces that structured immigrants’ lives. It also argues that, despite the violence they suffered at the hands of New York City, these men and women used the Almshouse to forge communities, demand medical care, and claim social support.
appendix:
- name: Medical terms
  file: shrout-v01/medical_terms.csv
- name: Data archive
  file: shrout-v01/shrout-data.zip
- name: Code archive
  file: shrout-v01/shrout-code.zip
preview: "/assets/img/v01/shrout/preview.png"
---

On February 23rd, 1847, three adults and one child stepped off the
deck of the ship Fidelia and onto New York City's docks.[^1] James
Burnes was twenty-eight years old, Eliza-Jane Burnes was twenty-two and
Arthur Burnes was twenty. One of the three was likely shepherding Ellen
Burnes, who was just three years old.[^2] All four members of the Burnes
family had been born in Ireland. They came to New York because Irish
potato crops failed consistently between 1845 and 1847. Government
efforts to provide relief proved too little and too late, and the rural
Irish began to starve.[^3] Sickness followed. By 1852 over one million
Irish people had died. Over one million more---those who had the
physical, material and emotional resources to do so---sailed across the
Atlantic. The vast majority of these immigrants, like the Burnes family,
disembarked in New York. Many became sick or otherwise required aid.
When they did, they were sent to the city's public Bellevue Almshouse.
There, they became the subjects of data collection. Many were diagnosed
as "recent emigrants." Bellevue inmates were then assigned to one of
many public health sites across the city, where they remained, often for
months.

There is a vast body of literature exploring Irish immigration patterns
in aggregate.[^4] However, the lives and experiences of individual
immigrants remain difficult to access.[^5] This is both because archival
references to these men and women are sparse, and because the references
that do exist are artifacts of government efforts to control immigrant
bodies. This essay explores Irish immigrants' experience of the
complicated and often hostile nascent public health systems in 1840s New
York. It focuses on the years before consistent immigration policies and
laws clarified the obligations of the city to immigrant newcomers.[^6]
It uses data produced about immigrants by the Bellevue Almshouse to
argue that these spaces could be sites of physical and epistemic
violence and simultaneously be spaces for community and resistance. It
does not merely seek to recapitulate the gaze of the nineteenth-century
state by condensing Bellevue's data into summary statistics. Rather, it
complicates histories of New York public health which have tended to
laud philanthropically-minded doctors and administrators, or emphasize
the institutional logics of Bellevue.[^7] Without discounting these
institutional histories, this essay calls for a greater focus on the
ways in which immigrants experienced historical enactments of power
through data production. It also demonstrates the ways in which that
same data can reveal challenges to that power.[^8]

New York City collected reams of data about immigrants in the nineteenth
century, as part of a broader, trans-Atlantic quantification movement.
Merchants assigned costs to commodities. Census-takers enumerated
families. Slave traders measured and evaluated enslaved people. Federal
and state governments aggregated paupers. Epidemiologists mapped
disease. This enumeration, evaluation, aggregation and mapping
explicitly valued some characteristics and devalued others. It
constituted an intellectual framework that worked to differentiate "the
national 'us' from aliens within and without." In doing so, it helped to
establish the "natural parameters" and features of what Mary Poovey
called "the social body."[^9]

For historians, this glut of information is attractive for its
abundance. It is visualizable, and regressable. It is also fraught with
peril. Nineteenth-century immigration data was produced with the express
purpose of reducing people to bodies; bodies to easily quantifiable
aspects; and assigning value to those aspects which proved that the
marginalized people to who they belonged were worth less than their
elite counterparts. The uses to which this data collection was put meant
that the act of quantification itself had the potential to enact both
epistemic and physical violence on the subjects it nominally preserved.
In reducing people to merely a set of characteristics, immigration
officials rendered them archivally mute. These men and women do not
speak for themselves in immigration records; the city alone speaks for,
and values them.[^10] More specifically, in reducing people to
characteristics associated with immigration status, Bellevue
administrators framed any ailments or difficulties inmates might have
had as a consequence of that status. Additionally, the admission of
these men and women into Bellevue subjected them to the physical
violence that characterized public health institutions.[^11] This
reading of potential violence in quantification is not merely an
artifact of twenty-first century theory. It was also visible to
contemporaries. Friedrich Kapp, one of New York State's first
Commissioners of Emigration, described the zeitgeist of
nineteenth-century New York as one in which "the emigrant is not a
subject, but an object...a numerical quantity; they seem to have no
individual existence, and the student of contemporary history does not
take the trouble to study their individual motives, misfortunes and
aspirations."[^12]

This tension between "individual motives, misfortunes and aspirations"
of immigrants and their quantification was made manifest in the
differences between immigrants' experiences of the Atlantic crossing and
New York city's experience of immigrants. The "Famine ships" that
crossed from Ireland to the United States were rife with typhus,
cholera, sick bodies, effluvia and purification. Those immigrants who
did not personally experience "a reeling to the head, followed by a
swelling pain, as if the head were going to burst" or "excruciating
pains in the bones, and then a swelling of the limbs," would have seen
their friends, family, and strangers with whom they shared close
quarters suffer.[^13] Many died. Many bodies were thrown overboard.[^14]
When those who survived the journey entered New York harbor, many were
weak from hunger and as a consequence of illness. Some were likely still
contagious. Their ordeal was over, but they were in need of support.

New York City officials experienced immigrants as potential liabilities,
and produced data about them accordingly. Ships arriving in New York
stopped at the Marine Hospital on Staten Island, but unless the
passengers were visibly ill, they were allowed to continue on into the
port.[^15] In the early nineteenth century, to mitigate the costs of
supporting sick or indigent immigrants, New York State passed laws
requiring the master or captain of every foreign ship to commit funds or
take out bonds for each passenger. As part of this process, captains had
to collect identifying information about immigrants, so that if they
became ill and turned to public institutions for aid, the city could
charge whoever was financially responsible.[^16] Middlemen got involved.
Brokers, bondsmen and runners scrambled to sell bonds to
vessel-owners.[^17] If the immigrants that they had bonded remained
healthy (or avoided entering public institutions) the bondsmen kept the
full bonding fee---anywhere between ten cents and one dollar per
passenger. If the immigrants became sick and turned to the city,
bondsmen were obligated to cover the cost of their care. These bondsmen
effectively bet that immigrants would not become ill. Immigrants---or
more particularly sick immigrants---became commodities to be wagered
on, bought and sold.

After they spent nearly three weeks in New York City without leaving a
mark on the historical record, the Burnes family surfaced again
archivally on March 12th, when Eliza-Jane and Ellen were "sent" to the
city's public Almshouse at Bellevue.[^18] James and Arthur do not appear
again. It is impossible to know how voluntary Eliza-Jane and Ellen's
incarceration was. The Almshouse admissions ledgers only note "by whom"
they were "sent," two city officials named George W. Anderson and Peter C.
Johnston. However, Eliza-Jane and Ellen would not have entered Bellevue
without work by city officials, who were able to exert considerable
power over newly-arrived immigrants.

George W. Anderson was the Superintendent of Out-Door Poor. He was
tasked with adjudicating the needs of the city's destitute, determining
whether they could receive aid outside of an institution ("Out-Door") or
whether they should be admitted to Bellevue. Impoverished New Yorkers
could approach Anderson, "either personally or through some friend," and
ask "to be committed." They would stay in city institutions "long enough
to recover from their diseases, if sick, and to earn sufficient to pay
all the expenses of their support."[^19] It is possible that in the
weeks between disembarking and entering Bellevue, Eliza-Jane learned of,
and then enthusiastically took advantage of this public health
infrastructure.

However, it is far more likely that she would have been urged or ordered
to enter Bellevue. In the first half of the nineteenth century, city
officials began to encourage incarceration and rehabilitation of the
poor, because institutionalization meant providing relief in exchange
for labor---a far cheaper prospect than providing out-door relief.[^20]
During the week she spent in New York before entering Bellevue,
Eliza-Jane might have encountered an agent of the city or a well-meaning
New Yorker who told her that if she wanted food for herself and Ellen,
she was obligated to enter the Almshouse. She might have connected their
recommendations with Irish workhouses, which required strenuous work as
a condition of entry, and which were notoriously spare in their
accommodations.[^21] This "workhouse test" meant that entering an
institution was a last resort. If she drew connections between Bellevue
and Irish institutions, her decision to enter Bellevue may have been
less a deliberate choice than it was her only remaining option.

It is also possible that Eliza-Jane might also have been explicitly and
forcibly institutionalized. In the 1840s, police officers were tasked
with corralling those "in the street" who seemed "intoxicated [or]
diseased." They were also on the lookout for those who were "houseless."
These "vagrants and criminals"---which included people who did not have
permanent accommodations, and which might have included Eliza-Jane and
Ellen---were committed to the penitentiary, the workhouse, or the
almshouse.[^22] Whether Eliza-Jane petitioned for admission, was
encouraged or coerced by some well-meaning city official, or was
compelled to enter Bellevue, her admittance into the public health
system signaled New York city's growing control over her and her
daughter.

That control was next made manifest in their quantification in Bellevue.
Upon entry, clerks recorded information---name, age, profession,
nationality---but also the names of the people who had referred them to
Bellevue, and, most importantly for New York City, the ship or broker
that was obligated to cover the new inmate's fees. Thereafter, a clerk---possibly Peter C. Johnston---designated the "disease" which had
occasioned their admission to Bellevue. Some were diagnosed with
medically recognizable illnesses, including "fever," "dropsy" and
"neuralgia." Others were diagnosed with "diseases" that made visible the
ways in which immigrants were failing to meet the expectations of urban
citizenship. These included "destitution" and "recent emigrant."[^23]
Neither of these diagnoses reflected an immigrant's health.
Nevertheless, they were treated as pathologies, and those pathologies
governed city officials perceptions of immigrants. Sickness, injuries or
destitution were subsumed under the pathology of "recent emigrant." This
diagnosis also determined immigrants' paths through the New York City
public health system.[^24]

No archival records remain that describe the clerks' logic in diagnosing
some immigrants as "destitute," others as suffering from a generalized
"sickness," and still others as "recent emigrant." No manuals remain
dictating policies that sent some of these men and women to work camps
on the East River islands and others to shantytowns on the hospital
grounds. There are few sources in immigrants' own words that can give a
sense of these men and women's experience navigating these
processes.[^25] Others recapitulate on the reports of Bellevue
administrators or city officials to describe the intervening days or
weeks.[^26] The voices of immigrants are absent.

<script>
    function updateShroutViz(viz) {
      document.getElementById('shroutviz').src = '/assets/iframe/shrout/' + viz  + '.html';
    }
</script>

<figure>
<iframe id="shroutviz" src="/assets/iframe/shrout/disease.html" style="height:725px;"></iframe>
<figcaption>
Figure 1. Pathways through the Bellevue Almshouse. Each line represents an inmate who encountered admittors, was diagnosed, and was sent to one of various sites within New York City’s public health system. Color coding the pathways by <a onclick="updateShroutViz('gender');">gender</a>, <a onclick="updateShroutViz('age');">age</a>, <a onclick="updateShroutViz('admittor_1');">first admittor</a>, <a onclick="updateShroutViz('admittor_2');">second admittor</a>, <a onclick="updateShroutViz('disease');">diagnosis</a>, <a onclick="updateShroutViz('site');">public health site</a> and <a onclick="updateShroutViz('institution');">specific institutions</a> reveals some of the hidden logics of the almshouse.

</figcaption>
</figure>

The Digital Almshouse Project does not give access to immigrant voices,
but it does help to make visible the forces working on immigrants, and
reveals possible sites of resistance to those forces. The Almshouse
dataset includes the information that Bellevue administrators collected
about nine thousand Irish-born inmates.[^27] This dataset is a
transcription of the admissions ledgers for Bellevue, cross-referenced
with ship-logs from the port of New York in the 1840s.[^28] The database
includes information intrinsic to individual inmates (age, name, gender
and profession), information about their arrival in New York (date of
arrival and ship), encounters with city officials (each inmate was
usually "sent by" two people) and processing in Bellevue (disease, and
the public health site that inmates were ultimately sent to). Each set
of variables signified one stage in immigrants' passage through the
public health system.[^29]

Being diagnosed as "recent emigrant," was significantly predicted
by who sent an immigrant to Bellevue.[^30] Two officials in particular,
Moses G. Leonard (the Commissioner of the Almshouse) and George W.
Anderson (the Superintendent of Out Door Poor), were significant in
predicting whether the person they were sending to the hospital would
have been diagnosed as a recent emigrant.[^31] Other diagnoses that
would seem to do similar work of signaling the unsuitability of an
immigrant for public spaces in New York---like destitution---were not
strongly associated with any particular official. An immigrant in New
York City who encountered these men was more likely than others to be
diagnosed as a "recent emigrant," and subsequently sent to the Bellevue
garrets.

The fact that two city officials were more likely than others to send
immigrants to Bellevue who would later be diagnosed as "recent emigrant"
suggests that the personal opinions of these men might have been a
significant factor in how inmates were understood by Bellevue staff. It
is impossible to know if the men and women who encountered George W.
Anderson and M.G. Leonard shared characteristics that are obscured by
the archive. But we do know that the New York official they encountered
seems to have changed their status in the eyes of the institution. We
can imagine that this information might have circulated within the Irish
immigrant community. These correlations do little to access the humanity
of immigrants, or the moments of precarity or contingency that shaped
their lives in the United States. However, they do tell us something
about the archivally invisible forces that acted on Irish immigrants who
were sent to Bellevue in the 1840s.[^32]

After they were diagnosed, these inmates were billeted. Some were sent
to the Almshouse hospital. Others were sent to the workhouse on
Blackwell's Island. Some stayed in Bellevue's Almshouse. Still more
ended up in temporary accommodations in the "garrets and cellars" and in
the newly-built morgue. Moses G. Leonard, the commissioner of the
Almshouse, wrote in 1846 that "the chapel also has been converted into
sleeping apartments and shanties built for their more comfortable
accommodations."[^33] These were marginal spaces intended simply for the
confinement of (mostly immigrant) bodies.

No archives remain to tell us how Eliza-Jane and Ellen, or the thousands
of other Irish immigrants who were incarcerated in New York's public
institutions, felt about their new surroundings.[^34] On the one hand,
their presence in Bellevue was evidence that in the short term at least,
New York officials were able to control their physical circumstances in
exchange for relief. The production of data about them meant that any
ailments that they might experience were filtered through a set of
assumptions about their status as immigrants. Their incarceration also
meant that they were potentially subject to physical violence at the
hands of Bellevue administrators.

On the other hand, despite their classification and incarceration, Ellen
and Eliza-Jane likely would have found a community in Bellevue. In these
shanties with Eliza-Jane and Ellen were other "recent emigrant"
families. They might have met the Crawford family, all of whom arrived
on the ship Glenore from Belfast in early February, and who had also
been sent to Bellevue by Anderson and Johnston. They might also have
encountered Catherine Lynch, a nineteen year old "spinster" who had
arrived alone in early April.

Other potential communities emerge from the Almshouse dataset. Over half
of the inmates diagnosed as "recent emigrant" were sent to the Bellevue
Hospital---likely because, according to one Bellevue official, the
entire Bellevue complex "was constantly filled with paupers," and even
the hospital had to accommodate new inmates.[^35] Over one tenth were
sent to the Bellevue Garret and over one tenth to Blackwell's Island.
Fewer than one percent were sent to the Bellevue Almshouse. However,
when both site of incarceration and the city officials who dispatched
the immigrant were taken into account, being sent to the Bellevue
Garrets was more significantly associated with the pathologization of
immigrant status. This was a space of overflow, which connoted no
particular form of treatment, but merely the holding of people who were
unable---either for reasons of debility or anti-immigrant bias---to
live in New York city.[^36]

Eliza-Jane and Ellen shared with these people a set of paradoxical
conditions: they were not unwell enough to be diagnosed with a medically
specific illness but not well enough to survive New York without aid;
they were in sufficient need to require city assistance, but also at
risk of (in the words of a cautioning commissioner of the Almshouse)
"liv[ing] in idleness, furnishing no return for their support."[^37]
For the city---and possibly for the immigrants themselves---incarceration in Bellevue seemed the only, but a nevertheless imperfect,
solution.

A story of community, of similar experiences at the hands of possibly
hostile city officials is not one that the Almshouse data easily
affords. It is, however, a narrative that is possible to tell by reading
these sources against the grain, uncovering the forces which seemed to
push immigrants through the public health system, and searching for
spaces where resistance to those forces might have been possible. This
kind of work makes it possible to tell the stories of immigrant as they
first arrived in New York, and to begin to fill in the gaps in an
historical narrative which often casts these men and women as
unfortunate subjects of xenophobia, religious intolerance and state
control.

---

### Bibliography

"Admission Records, The Almshouse Department," 1847. Almshouse Ledger
Collection, 1758--1952. Municipal Archives, City of New York.

Anbinder, Tyler. *Five Points: The 19th-Century New York City
Neighborhood That Invented Tap Dance, Stole Elections, and Became the
World's Most Notorious Slum*. New York: Free Press, 2001.

Balch Institute for Ethnic Studies. Center for Immigration Research.
"Records for Passengers Who Arrived at the Port of New York During the
Irish Famine, Created, 1977--1989, Documenting the Period 1/12/1846 -
12/31/1851," 1989 1977. Collection CIR: Records of the Center for
Immigration Research. National Archives at College Park---Electronic
Records, National Archives at College Park.

Binder, Frederick M., and David M. Reimers. *All the Nations Under
Heaven: An Ethnic and Racial History of New York City*. New York: Columbia University Press, 1995.

Bly, Nellie. *Ten Days in a Mad-House*. New York: Ian L. Munro, 1887.

Board of Assistant Aldermen. *Proceedings and Documents of the Board of
Assistant Aldermen, from Dec. 7th 1846 to May 10th, 1847.* Vol. XXIX.
New York, 1847.

Carter, Rodney G. S. "Of Things Said and Unsaid: Power, Archival
Silences, and Power in Silence." *Archivaria* 61 (Spring
2006). <https://archivaria.ca/index.php/archivaria/article/view/12541>.

Chatterjee, Samprit, and Ali S. Hadi. "Logistic Regression." In
*Regression Analysis by Example*. Hoboken, NJ: John Wiley & Sons, 2015.

Derrida, Jaques. *Archive Fever: A Freudian Impression*. Chicago:
University of Chicago Press, 1996.

"Digital Almshouse Project." <http://www.nyuirish.net/almshouse>.

Diner, Hasia R. *Erin's Daughters in America: Irish Immigrant Women in
the Nineteenth Century*. Baltimore: Johns Hopkins University Press,
1983.

Ernst, Robert. *Immigrant Life in New York City, 1825--1863*. Port
Washington, NY: Ira J. Friedman, Inc., 1965.

Foucault, Michel. *Discipline and Punish: The Birth of the Prison*.
New York: Vintage Books, 1977.

Gray, Peter. "Irish Social Thought and the Relief of Poverty,
1847--1880." *Transactions of the Royal Historical Society* 20 (December
2010): 141--56.

Gray, Peter. *The Making of the Irish Poor Law, 1815--43*. Manchester,
U.K.: Manchester University Press, 2010.

Harcourt, Bernard E. "From the Asylum to the Prison: Rethinking the
Incarceration Revolution." *Texas Law Review* 84, (2005--2006): 1751--86.

Hirota, Hidetaka. *Expelling the Poor: Atlantic Seaboard States and the
Nineteenth-Century Origins of American Immigration Policy*. New York: Oxford
University Press, 2016.

Kapp, Friedrich. *Immigration, and the Commissioners of Emigration of
the State of New York*. New York: The Nation Press, 1870. <https://archive.org/details/commemigrant00kapprich>.

Kenny, Kevin. "Race, Violence and Anti-Irish Sentiment in the Nineteenth
Century." In *Making the Irish American: The History And Heritage of the
Irish in the United States*, edited by Joseph J. Lee and Marion R.
Casey. New York: NYU Press, 2006.

Kinealy, Christine. *Charity and the Great Hunger in Ireland: The
Kindness of Strangers*. London: Bloomsbury, 2013.

Kinealy, Christine. *This Great Calamity: The Irish Famine, 1845--52*. Dublin:
Gill & Macmillan, 1994.

Klebaner, Benjamin J. "State and Local Immigration Regulation in the
United States before 1882." *International Review of Social History* 3,
no. 2 (August 1958): 269--95. <https://doi.org/10.1017/S0020859000001127>.

Klips, Stephen Anthony. "Institutionalizing the Poor: The New York City
Almshouse, 1825--1860." Ph.D. diss., City University of New York, 1980.

Miller, Kerby A. *Emigrants and Exiles: Ireland and the Irish Exodus to
North America*. New York: Oxford University Press, 1985.

Mokyr, Joel. *Why Ireland Starved: A Quantitative and Analytical History
of the Irish Economy, 1800--1850*. London, Boston, Sydney: George Allen &
Unwin, 1993.

New York (N.Y.). Commissioners of the Alms-House, Bridewell, and
Penitentiary. *Annual Report of the Governors of the Alms House, New
York*. Board of Alderman Document, no. 44. New York: W.B. Townsend,
1847.

Ó Gráda, Cormac. "A Note on Nineteenth-Century Irish Emigration
Statistics." *Population Studies* 29, no. 1 (March 1975): 143--49.

O'Malley, Brendan P. "Lickspittles and Land Sharks: The Immigrant
Exploitation Business in Antebellum New York." In *Capitalism by
Gaslight: Illuminating the Economy of Nineteenth-Century America*,
edited by Brian P. Luskey and Wendy A. Woloson. Philadelphia: University of
Pennsylvania Press, 2015.

Oshinsky, David. *Bellevue: Three Centuries of Medicine and Mayhem at
America's Most Storied Hospital.* New York: Doubleday, 2016.

Poovey, Mary. "Curing the 'Social Body' in 1832: James Phillips Kay and
the Irish in Manchester." *Gender & History* 5, no. 2 (June 1, 1993):
196--211. <https://doi.org/10.1111/j.1468-0424.1993.tb00172.x>.

Purcell, Richard J. "The New York Commissioners of Emigration and Irish
Immigrants: 1847--1860." *Studies: An Irish Quarterly Review* 37, no. 145
(1948): 29--42.

Rothman, David J. *The Discovery of the Asylum; Social Order and
Disorder in the New Republic*. Boston: Little, Brown and Company, 1971.

SenGupta, Gunja. *From Slavery to Poverty: The Racial Origins of Welfare
in New York, 1840--1918*. New York: New York University
Press, 2009.
<http://ebookcentral.proquest.com/lib/yale-ebooks/detail.action?docID=865347>.

Whyte, Robert. *The Ocean Plague, Or, A Voyage to Quebec in an Irish
Emigrant Vessel*. Boston: Coolidge and Wiley, 1848.

---

### Notes

 The author would like to thank Marion Casey, Kalani Craig,
    Jessica Marie Johnson, Michelle Moravec, Lincoln Mullen, Stephen
    Robertson and Scott Weingart for their support and comments on early
    iterations of this paper, as well as Tyler Anbinder and participants
    in the 2018 Current Research in Digital History for their comments
    and suggestions.

[^1]: Balch Institute for Ethnic Studies. Center for Immigration
    Research. "Records for Passengers Who Arrived at the Port of New
    York During the Irish Famine, Created, 1977 - 1989, Documenting the
    Period 1/12/1846 - 12/31/1851."

[^2]: Kinealy, *This Great Calamity*.

[^3]: Kinealy, *Charity and the Great Hunger in Ireland*.

[^4]: For an overview of the famine, famine immigration, see Miller,
    *Emigrants and Exiles*. For quantitative analyses of Irish migration patterns, see Ó Gráda, "A Note on Nineteenth-Century Irish Emigration Statistics";
    Mokyr, *Why Ireland Starved*; Diner, *Erin's Daughters in
    America*. For a discussion of immigrants' experiences more broadly, see Ernst,
    *Immigrant Life in New York City*; Binder and Reimers,
    *All the Nations Under Heaven*.

[^5]: Some work has recreated immigrants' experiences in New York City.
    Anbinder, *Five Points*.

[^6]: In May of 1847, the Commissioners of Emigration for the State of
    New York were established. This body was tasked with protecting
    incoming immigrants, and was empowered to administer piers were
    incoming immigrants would have to land and be assessed, license
    reputable boarding houses, and supervise ticket agents. The rise of
    the Commissioners of Emigration effectively ended Irish immigrants'
    use of Bellevue as a public health space. However, early famine
    immigrants were not subject to these regulations, and between 1845
    and 1847, the city was not infrastructurally prepared to deal with
    them. For an overview of the development of immigration law, see
    Purcell, "The New York Commissioners of Emigration and Irish
    Immigrants"; Hirota, *Expelling the Poor*, chapter 2.

[^7]: For example, see the recent histories of Bellevue and of the role
    of Almshouses in the development of American immigrant policy.
    Oshinsky, *Bellevue*; Hirota, *Expelling the
    Poor*.

[^8]: Stephen Robertson described this approach as one which makes
    "products" (the Almshouse admissions records) visible as "process."

[^9]: Poovey, "Curing the 'Social Body' in 1832," 196.

[^10]: Derrida, *Archive Fever*; Carter, "Of Things Said and Unsaid."

[^11]: Four decades after the Irish famine, Nellie Bly would famously
    describe "choking and beating" patients in the Blackwell's Island
    insane asylum. Bly, *Ten Days in a Mad-House*.

[^12]: Kapp, *Immigration*, 42.

[^13]: Whyte, *Ocean Plague*, 44.

[^14]: Whyte, 51.

[^15]: Hirota, *Expelling the Poor*, 47.

[^16]: Klebaner, "State and Local Immigration Regulation," 274.

[^17]: O'Malley, "Lickspittles and Land Sharks."

[^18]: The terms in quotation marks reflect the language used in the
    Bellevue Almshouse admission records. The designation "recent
    emigrant" was recorded in a column labeled "disease."

[^19]: New York (N.Y.). Commissioners of the Alms-House, Bridewell, and
    Penitentiary, *Annual Report*, 5--6.

[^20]: Rothman, *The Discovery of the Asylum*, 194.

[^21]: For a review of the competing ideologies of Irish workhouses, see
    Gray, *The Making of the Irish Poor Law*; Gray,
    "Irish Social Thought and the Relief of Poverty."

[^22]: New York (N.Y.). Commissioners of the Alms-House, Bridewell, and
    Penitentiary, *Annual Report*, 4. Officially, those in legitimate need were required to petition for admission while those who were criminals or burdens on
    the city could be forcibly incarcerated. It is unlikely, however,
    that in practice the line between vagrant and deserving poor was
    always clear. For a discussion of the antebellum intersection of
    ideas about race, poverty and crime, see SenGupta, *From
    Slavery to Poverty*.

[^23]:  For a complete list of the possible diagnoses and (when
    possible) their contemporary equivalent, see the medical terms
    appendix.

[^24]: For a discussion of anti-Irish sentiment, see Kenny, "Race,
    Violence and Anti-Irish Sentiment in the Nineteenth Century." For a
    visualization of the different factors that contributed to
    immigrants' paths through this system, see <http://shroutdocs.org/research/bellevue/bellevue_pathways/bellevue_almshouse.html>.

[^25]: Binder and Reimers, *All the Nations under Heaven*, 45.

[^26]: Ernst, *Immigrant Life in New York City*, 37.

[^27]: "Digital Almshouse Project."

[^28]: "Admission Records, The Almshouse Department"; Balch Institute
    for Ethnic Studies. Center for Immigration Research., "Records for
    Passengers Who Arrived at the Port of New York During the Irish
    Famine, Created, 1977 - 1989, Documenting the Period 1/12/1846 -
    12/31/1851."

[^29]: R script repository: <https://github.com/shrouta/bellevue_R_script>

[^30]: This finding, and the ones that follow are based on logistic
    regression, modeled on dummy variables created for disease,
    sent\_to, and by\_whom\_sent. Chatterjee and Hadi, "Logistic
    Regression."

[^31]: The relation was tested with a logistic regression. The coefficient for Moses Leonard was 2.91724, the standard error was .11985, the significance was \< 2e-16. The coefficient for the George W. Anderson was 2.63644, the standard error was .12535, the significance was \< 2e-16. For full details see <https://github.com/shrouta/bellevue_R_script/blob/master/recent_emigrant_logistic_output.txt>.

[^32]: For a visualization of these forces, see <http://www.nyuirish.net/almshouse/data-pathways/>.

[^33]: Board of Assistant Aldermen, *Proceedings and Documents of the
    Board of Assistant Aldermen, from Dec. 7th 1846 to May 10th, 1847.*,
    XXIX:373.

[^34]: For a discussion of the historical relationship between asylums,
    almshouses, institutionalization, incarceration and the long history
    of the carceral state, see Rothman, *The Discovery of the Asylum*; Foucault, *Discipline and Punish*; Harcourt, "From the Asylum to
    the Prison."

[^35]: Klips, "Institutionalizing the Poor," 276.

[^36]: The relation was tested with a logistic regression. The coefficient for garret was 1.34441, the standard error was 0.23120, the significance was 6.16e-09. <https://github.com/shrouta/bellevue_R_script/blob/master/recent_emigrant_logistic_output.txt>.

[^37]: Board of Assistant Aldermen, *Proceedings and Documents of the
    Board of Assistant Aldermen, from Dec. 7th 1846 to May 10th, 1847.*,
    XXIX:373.
