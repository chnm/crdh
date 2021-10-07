---
title: "A Tale of Three Valleys"
subtitle: "Text Mining, Spatial Analysis, and the Contested Geographies of Colorado and New Mexico’s San Luis Valley"
doi: "https://doi.org/10.31835/crdh.2020.06"
volume-number: 3
year: 2020
date: 2020-10-28
authors:
- last: Swisher
  first: Jacob
  email: jswisher@nd.edu
  affiliation: "Department of History, University of Notre Dame"
  orcid: 0000-0003-2270-4933
  url: "https://history.nd.edu/graduate-program/graduate-student-directory/jacob-swisher/"
abstract: |
  During the mid-nineteenth century, Colorado and New Mexico's San Luis Valley experienced an influx of migrants, land speculators, American soldiers, and capital. Much like in other borderland regions throughout the American West, their arrival was anything but smooth. As these new arrivals settled alongside an existing population of Utes, many attempted to reimagine the region in ways that supported their own economic ambitions. This article traces two regional identities that white Americans created for the San Luis Valley as they migrated to the region in the 1860s and 1870s, both of which ignored claims laid to the region by existing Indigenous and Nuevomexicano populations. The first imagined the valley as an agrarian paradise that land speculator William Gilpin and his partners created to appeal to white settlers. This article employs text mining and spatial analysis to reconstruct the second, an identity that emerged in Colorado newspapers and defined the region as a thoroughfare to mines farther west. Through digital methods, this article links localized attempts to define the San Luis Valley as a region and to lay claim to its resources to those that occurred in the press from afar. In doing so, it demonstrates the efficacy of digital methods for connecting local borderlands histories to broader regional and national narratives.
appendix:
- name: README
  file: swisher-v03/README.txt
- name: Data archive
  file: swisher-v03/swisher-data.zip
preview: "/assets/img/v03/swisher/preview.png"
---

On a brisk October morning in 1868, William Gilpin and Ferdinand Hayden
emerged from the mountain pass and gazed along the broad grassy valley
toward the headwall of the Sierra Blanca Massif (see figure 1). Their
arrival likely caused little commotion in Colorado and New Mexico's San
Luis Valley. The valley, like much of the Colorado and New Mexico
territories, buzzed with excitement over rumors of a recently renewed
Ute-American conflict and the final reports of a federal boundary survey
at the Colorado-New Mexico border.[^1] Gilpin and Hayden, however, were
in the region for different purposes. In just a few short weeks, Gilpin,
a former Colorado Governor turned land speculator, and Hayden, a
renowned federal geologist, intended to survey the Sangre de Cristo Land
Grant, a one-million-acre parcel in the valley's southeastern corner.
Gilpin, who had recently acquired large swaths of the parcel, aimed to
appraise, develop, and sell the grant with the help of English and
American financiers.[^2] Upon their return from the surveying project,
Hayden wrote to William Blackmore, Gilpin's business partner and fellow
stakeholder in the grant, to report that the San Luis Valley "could not
have been more perfectly adapted to the wants of an agricultural region
if it had been arranged by the hand of art."[^3]

{% figure caption: "Figure 1. “The Sierra Blanca, Ft. Garland Colorado,” Henry W. Elliot, 1869. United States Geological Survey, Washington, D.C. As Gilpin and Hayden reached the valley floor in October of 1868, they encountered a view much like the one Henry Elliot sketched of the Sierra Blanca Massif and the U.S. Army post at Fort Garland in 1869. Like Hayden's report to Blackmore and Gilpin, Elliot's sketch similarly portrayed the landscape as open and hospitable to westward-bound Americans." %}
![Sketch, with Sierra Blanca Massif in the background, and Fort Garland, an American flag on a flag pole, and a person on a horse in the foreground.]({{site.url}}/assets/img/v03/swisher/figure1.png)
{% endfigure %}

But was the San Luis Valley such a paradise? Or was Gilpin and Hayden's
portrayal of the region more promotional act than truthful
testimony?[^4] Gilpin and Hayden's vision of the San Luis Valley was but
the latest in a series of attempts to define, control, and profit from
the valley's material environment---a repetitive pattern that, as
historian Patricia Nelson Limerick argues, is ubiquitous in American
Western history.[^5] During the mid-nineteenth century, the San Luis
Valley existed as a borderland region, a contested meeting ground
between unique cultures and peoples who sought to harness the valley's
resources to their own ends and among whom Gilpin and Hayden were the
newest arrivals.[^6] Throughout the 1850s, Capote and Muache Utes,
Nuevomexicano farmers and sheepherders, and U.S. Army regulars all laid
competing claims to the region's future.[^7] Alongside Gilpin and
Hayden, during the 1860s and 1870s, a growing tide of American and
European migrants joined the existing population of Utes,
Nuevomexicanos, and American soldiers in this contested borderland.[^8]
When Americans flocked to the San Luis Valley in growing numbers, an
alternative portrait of the region emerged alongside Gilpin,
Hayden, and Blackmore's promotions; an "imagined geography" largely
produced in Colorado newspapers that represented the San Luis Valley as
an obstacle to be overcome en route to the mines of the San Juan Country
rather than as an agrarian paradise rife with potential.[^9]

{% figure caption: "Figure 2. “Map of Colorado Embracing the Central Gold Region,” Frederick J. Ebert, 1869. Colorado State University Water Resources Archive. The Sangre de Cristo Grant (colored in dark green and pink) is located in the southeast corner of the San Luis Valley (light green). Ebert produced the map “under the direction of” William Gilpin. Notably, the shading employed by Ebert focuses the viewer's attention on the San Luis Valley as both a confluence point of railroad tracks and, to the uninformed reader, as a significant area in the “Colorado Gold Region.” Many viewers, however, were likely interested in learning more about the mines of the San Juan Country, which lay northwest of the San Luis Valley and unshaded in Ebert's depiction of the Colorado Territory." %}
![Map of Colorado, with the Sangre de Cristo Grant in the bottom-middle of the map.]({{site.url}}/assets/img/v03/swisher/figure2.png)
{% endfigure %}

This essay leverages digital tools to place Gilpin and Hayden's
portrayal of the Sangre de Cristo Land Grant and the San Luis Valley
alongside an alternative portrait of the region that developed in
contemporary Colorado newspapers as Americans moved west into the
basin. In doing so, it adds to the local body of scholarship on the San
Luis Valley by revealing how distanced historical actors also laid
claims to the region as they sought to promote the valley as an ideal
and profitable route between the Colorado plains and the San Juan
Country. I use Voyant Tools and Palladio to analyze a corpus of 256
Colorado newspaper articles published between 1862 and 1878, largely by
newspapers located outside of the San Luis Valley whose reporters and
contributors wrote to inform migrants and distant readers about the
region.[^10] While a selection of 256 articles is a small corpus for
digital analysis, it constitutes a surprisingly large source base for a
historically remote location like the San Luis Valley. Applying digital
methods to projects with small data offers a new avenue for regional
approaches to borderlands history and the history of the American West.
As a digital study in the contested nature of the San Luis Valley's
regional identity, this essay demonstrates that digital methods are
well-suited to broaden the geographic scale of the stories we tell about
borderland regions like the San Luis Valley---an approach that allows us
to more fully consider the wide range of peoples who have laid claim to
the borderlands of American Western history.

Though many aspects of Hayden and Gilpin's promotional efforts failed to
materialize in the Colorado press, the findings in Hayden's published
report were not entirely divorced from distanced perceptions of the San
Luis Valley. Like the regional press, Hayden devoted parts of his report
to the San Luis Valley's road system, noting that "the roads travelled
were firm and smooth."[^11] According to Hayden, "the natural roads in
this district \[were\] not surpassed for their excellence in any part of
the world."[^12] Americans outside the San Luis Valley shared Hayden's
preoccupation with road conditions in the Intermountain West and,
between 1862 and 1878, the Colorado press discussed roads, distance, and
mountain passes most frequently relative to other topics in articles
associated with the San Luis Valley (Figure 3). Unfortunately for
Hayden, Gilpin, and Blackmore, newspaper accounts of routes into the San
Luis Valley rarely championed the valley's potential for cultivation.
Although references to stock-raising appear with some frequency (Hayden
purported that the valley contained "excellent pasture"), outside
observers were more likely to encounter newspaper accounts that
discussed how they might reach the San Luis Valley but said little about
what they might do once they arrived. Unlike Hayden, the
regional news media did little to portray the San Luis Valley as "the
most inviting and most promising district west of the Missouri
River."[^13]

***High-Frequency Topics Discussed in Coverage of the San Luis Valley (Excludes Place Names)***

| Term | Frequency |
|:---:|:---:|
| Mile(s) | 194 |
| Road(s)  | 163 |
| Pass(es) | 114 |
| Good | 86 |
| Stock | 86 |
| New | 84 |
| Mine(s) | 79 |

<figure>
<figcaption>Figure 3. High-frequency topics associated with the San Luis Valley in Colorado newspapers, 1862-1878. Excluding place name references, such as "San Luis Valley" or "San Juan Country," Colorado newspapers most frequently paid attention to distance and movement both into and through the San Luis Valley, with mile(s), road(s), and pass(es) appearing most frequently in the corpus. Stock and mine(s) also appear with high frequency, ranking fourth and seventh respective to the adjectives good (tied with stock for fourth at 86 mentions) and new (sixth with 84 mentions). Topics selected based on frequency of appearance as ranked by Voyant Tools. Stemming of terms like mile(s) and road(s) occurred after examining initial list of high-frequency terms.</figcaption>
</figure>

Colorado newspapers differed from Hayden and Gilpin in their
interpretation of *why* Americans should travel over the region's
apparently impeccable thoroughfares. Whereas Hayden and Gilpin
positioned the valley floor as a destination for eager settlers,
newspapers were far more likely to identify the region as an obstacle
that stood between American migrants and southwestern Colorado's crown
jewel: the San Juan Country. Following an initial gold rush in 1858, the
San Juan Country garnered prospectors' attention in the early 1860s and
loomed large in public perceptions of the Colorado Territory. The San Juan
mines, however, remained physically remote throughout the 1870s and most
overland traffic to the region flowed through passes along the western
edge of the San Luis Valley.[^14]

For the unfamiliar migrant, knowledge of road and pass conditions was
crucial to any attempt to tap the San Juan Country's mineral wealth. By
publishing details on routes to the San Juan Country, Colorado
newspapers provided travelers with valuable geographic knowledge. Often,
newspaper articles linked a road or pass into the eastern edge of San
Luis Valley with a complimentary route leading out of the valley's
western side. For example, in an 1872 article appearing in Pueblo
Colorado's *Colorado Daily Chieftain*, a G.W.J. claimed to offer the
"sound advice" that future travelers should restock their supplies in
Pueblo before heading over the Sangre de Cristo Pass and across the
valley. If they were lucky, G.W.J. noted, they "may possibly outfit in
part" at Saguache or Conejos, two towns along the valley's western edge
frequented by travelers en route to the San Juan Mountains.[^15] Though
brief, G.W.J.'s description of the valley suggested to travelers that
Pueblo, Saguache, and Conejos were of some utility during the journey to
the true objective of readers moving towards the San Luis Valley: the San
Juan Country. In G.W.J.'s report, communities that lay in between Pueblo
and the valley's western markets, like Fort Garland, simply faded into
the blank space of the press's "imagined geography" of the San Luis
Valley.[^16] When geographic knowledge like that offered by G.W.J. is
visualized as a bubble map in Palladio, it becomes clear that aspiring
prospectors and migrants who read Colorado newspapers received
information that granted the mountain passes and supply points along the
valley's perimeter more geographic significance than the small
communities spread across the valley's interior, including those on the
Sangre de Cristo Land Grant (see figure 4).

{% figure caption: "Figure 4. Bubble map of place-name references in Colorado newspaper articles discussing the San Luis Valley, 1862--1878. Nodes sized according to aggregate number of references to a given place in the corpus. In addition to primarily referencing places around the San Luis Valley's edge, such as mountain passes, Colorado newspapers also privileged the northern half of the San Luis Valley in their discussions of the region. Yet, in doing so, newspaper coverage of the San Luis Valley obscured the region's sizable Nuevomexicano population, many of whom migrated to the region in the 1850s and primarily settled in the valley's southern half." %}
![Map of Colorado and northern New Mexico, with blue circles to indicate the locations of places referenced in Colorado newspapers. The circles increase in size to indicate a greater number of references.]({{site.url}}/assets/img/v03/swisher/figure4.png)
{% endfigure %}

As newspapers directed new arrivals through the San Luis Valley and
onwards to the San Juan Mountains, they provided readers with a
geography of the San Luis Valley that privileged routes to the San Juan
Country. In the text of Colorado newspaper articles, places along the
valley's edge appeared more frequently in association with the San Luis
Valley than did settlements on the valley floor. Often, these locations
were passes high in the Sangre de Cristo or Sierra Madre Mountains or
westward towns like Del Norte and Saguache that offered trade goods and
supplies for prospectors headed to the San Juan Country. By emphasizing
mountain passes and markets along the route to the San Juan Country, the
Colorado press attempted to reimagine the San Luis Valley as part of a
new Western region---one with a geography defined by the movement of
prospectors and minerals over the Rocky Mountains rather than by the
priorities of land speculators or the valley's Nuevomexicano and
Indigenous residents.

By the late 1870s, the physical route across the San Luis Valley became
more linear as the Denver and Rio Grande (D&RG) railroad transformed
roads into narrow gauge track when they constructed new lines to the San
Juan Country. So too did the "imagined geography" of the region produced
in Colorado newspapers.[^17] The D&RG, which eventually crossed the
Sangre de Cristo Mountains and arrived in Alamosa, Colorado in 1878, was
regularly covered by the regional press. With plans to push on towards
Del Norte and the San Juan Country, the D&RG, as the *Colorado Chieftain* put it, had "come near to annihilating time and space" in the San Luis Valley.[^18] Unlike the Ebert's "Map of Colorado Embracing the Central Gold Region" (seen in figure 2), which positioned the Sangre de
Cristo Land Grant as the eventual destination of the D&RG (likely at the
behest of Gilpin), press coverage of the D&RG instead portrayed timely
access to the San Juan Country as the railroad's primary objective. In
covering the D&RG's activity in the San Luis Valley, the regional press
began associating the route through the San Luis Valley with existing
and planned stops along the D&RG tracks. No longer would migrants need
geographic knowledge of multiple routes into the valley. Instead, the
public only required knowledge of places touched by D&RG locomotives
(see figure 5).

{% figure caption: "Figure 5. Mapped network of geographic associations between the San Luis Valley and the D&RG. In contrast to the bubble map above (figure 4), newspaper references associated with the D&RG produce a strikingly linear visualization---a pattern that makes visible the compatibility of railroad construction with ongoing attempts by town boosters, merchants, and newspapers to define the San Luis Valley as a direct route to the San Juan Country. Node size based on aggregate number of references to a given place in the newspaper corpus. Edges signify sequencing of place names in newspaper articles discussing the D&RG and represent how authors described multiple place names as stops or waypoints along a westward or southward moving route that the D&RG might take on its way to the San Juan Country or to markets in New Mexico. Edge weight not significant." %} ![Map of southern Colorado and northern New Mexico, showing Denver and Rio Grande spur line references. A orange circle indcates the location where the spur line began. Blue circles indicate locations of waypoints. The circles increase in size to indicate a greater number of references.]({{site.url}}/assets/img/v03/swisher/figure5.png)
{% endfigure %}

Although mapping the place names that Colorado newspapers associated
with the San Luis Valley populates the region's northern half with
place-based nodes, the San Luis Valley's southern half was hardly devoid
of human activity. Since the 1840s, Nuevomexicanos had occupied
settlements in the valley's southern end where they primarily herded
sheep.[^19] Ute bands had also resided in the San Luis Valley for
centuries and, in the 1850s and 1860s, the southern San Luis Valley
operated as a focal point of Ute-American military conflicts and
diplomatic relations.[^20] Within the selected corpus of newspapers, Ute
bands and Nuevomexicanos appear occasionally, receiving forty-three and
thirty-four respective mentions. In contrast to more frequent references
to the San Luis Valley's physical landscape, including to distance,
movement, and land-use practices (see figure 3), Utes and Nuevomexicanos
hardly received attribution equal to their population size or history of
land tenure in the region. Newspaper articles discussing Ute bands are
also skewed towards the earlier temporal bounds of the corpus, a pattern
that likely reflected a regional preoccupation with the treaty-making
process in the 1860s.[^21] The relative absence of Nuevomexicanos in
textual descriptions of the San Luis Valley, however, is far more
surprising given that Nuevomexicano colonists had moved into the
valley's southern end in the 1840s and, by the 1880s, comprised a
sizeable majority of the region's population as well as an important
voting bloc in territorial elections.[^22] In Colorado, where most of
the San Luis Valley lies, 8,484 of the valley's 10,457 Coloradans lived
in the overwhelmingly Nuevomexicano counties of Conejos and Costilla
along the Colorado-New Mexico border in 1880.[^23] Even Hayden, in his
1868 report on the San Luis Valley and the Sangre de Cristo Land Grant,
noted the presence of Nuevomexicano farmers and shepherds in the
valley's southern half.[^24] Though Nuevomexicanos played a significant
role in the region's mid-nineteenth-century history, the "imagined
geography" forwarded by the Colorado press reveals how distanced
observers readily erased the existence of communities who presence was
either insignificant to or, in the case of Ute bands, incompatible with
many Americans' vision for the San Luis Valley's future.[^25]

This spatial disparity, between the northward geography forwarded by the
Colorado press and the southerly distribution of valley populations,
suggests that multiple, distinct San Luis Valleys existed in the
late-nineteenth century. The first was the valley toured by Hayden and
Gilpin and populated by Nuevomexicano settlers and Ute bands. The second
emerged in the public consciousness and characterized the San Luis
Valley by the quickest route across the basin and into the San Juan
Country. The third, an agrarian "promised land," existed only in the
minds of a select few among the area's travelers and residents---a group
interested in portraying the region as ripe not only for settlement, but
for a white settler utopia.[^26] Together, these divergent geographic
identities reveal that the San Luis Valley was hardly remote and unknown
to migrants and distanced observers. Rather, the valley remained a
contested space throughout the mid-nineteenth century; one whose
identity shaped how people moved through, experienced, and understood
the southern Colorado landscape.

Throughout the 1860s and 1870s, differing individuals, communities, and
corporate interests attached distinct identities to the San Luis
Valley.[^27] Yet existing studies of the region thus far have not
attempted to overlay these contested geographies with one another for
two primary reasons: (1) historians of the San Luis Valley have
generally privileged local narratives over regional or national ones and
(2) until recently, the region's late-nineteenth century history has
often remained distant from historical evidence that originated and
resided outside the valley.[^28] By using Palladio to visualize how the
San Luis Valley emerged in newspaper accounts primarily from outside the
region and considering those accounts and their associated geography as
representative of how distanced readers understood the San Luis Valley's
cultural and physical geography in the 1860s and 1870s, this article
demonstrates that digital methods are well-positioned to begin
addressing these gaps in the region's historiography.

This paper also holds implications for the use of digital tools in
studies of other remote borderland regions. Although Daniel Cohen has
argued that "it is now quite clear that historians will have to grapple
with abundance, not scarcity" when working with a constantly expanding
base of digitized sources, borderlands historians often confront the
opposite: we regularly deal with scarcity in the places we explore
through historical inquiry.[^29] This paper, however, suggests that the
common paucity of digitized materials from historically remote places
should not keep digital tools at bay in borderlands studies. Instead,
borderlands scholars should leverage existing tools to redirect
distanced sources *towards* remote places, as this paper attempts to do
with Voyant Tools and Palladio. In doing so, we may find that digital
tools can add depth to local stories while placing borderlands into
narrative association with regional, national, and even continental
histories.[^30] Moreover, by applying digital tools to places without
readily available, massive datasets, we may also further the central
goal of borderlands scholarship: leveraging stories from exciting,
unique, and often unpredictable places to valuably complicate our
understanding of regional, national, and global histories.

---

### Newspaper Corpus

*Boulder County News*, (Boulder, Colorado)

*Colorado Chieftain* (Pueblo, Colorado)

*Colorado Miner* (Georgetown, Colorado)

*Colorado Springs Gazette* (Colorado Springs, Colorado)

*Colorado Transcript* (Golden City, Colorado)

*Daily Commonwealth* (Denver, Colorado)

*Denver Daily Times* (Denver, Colorado)

*Daily Miners' Register* (Central City, Colorado)

*Denver Tribune* (Denver, Colorado)

*Las Animas Leader* (Las Animas, Colorado)

*Ouray Times* (Ouray, Colorado)

*Daily Rocky Mountain News* (Denver, Colorado)

*Saguache Chronicle* (Saguache, Colorado)

*Silver World* (Lake City, Colorado)

---

### Bibliography

Andrews, Thomas. "Tata Atanasio Trujillo's Unlikely Tale of Utes, Nuevomexicanos, and the Settling of Colorado's San Luis Valley." *New Mexico Historical Review* 75, no. 1 (2000): 4--41.

Aron, Stephen. *American Confluence: The Missouri Frontier From Borderland to Border State*. Bloomington: Indiana University Press, 2006.

Bartlett, Richard. *Great Surveys of the American West*. Norman: University of Oklahoma Press, 1962.

Blackhawk, Ned. *Violence Over the Land: Indians and Empires in the Early American West*. Cambridge: Harvard University Press, 2006.

Blackmore, William. *Colorado: Its Resources, Parks, and Prospects as a New Field for Emigration; With an Account of the Trenchara and Costilla Estates, in the San Luis Park*. London: Sampson Low, Son, and Marston, 1869. <https://mountainscholar.org/handle/10217/35691>.

Blevins, Cameron. "Space, Nation, and the Triumph of Region: A View from the World of Houston." *Journal of American History* 101, no. 1 (June 2014): 122--47. <https://doi.org/10.1093%2Fjahist%2Fjau184>.

Brayer, Herbert O. *William Blackmore: The Spanish-Mexican Land Grants of New Mexico and Colorado: 1863--1878*. Denver: Bradford-Robinson, 1949.

Cassidy, James. *Ferdinand V. Hayden: Entrepreneur of Science*. Lincoln: University of Nebraska Press, 2000.

Cohen, Daniel J., Michael Frisch, Patrick Gallagher, Steven Mintz, Kirsten Sword, Amy Murrell Taylor, William G. Thomas, III, and William J. Turkel. "Interchange: The Promise of Digital History." *Journal of American History* 95, no. 2 (September 2008): 452--91. <https://doi.org/10.2307/25095630>.

Deibert, Jack E. and Brent H. Breithaupt. *Tracks, Trails & Thieves: The Adventures, Discoveries, and Historical Significance of Ferdinand V. Hayden's 1868 Geological Survey of Wyoming and Adjacent Territories*. Boulder: Geological Society of America, 2016.

Department of the Interior, Bureau of the Census. Cartographic Boundary Files. 2017.
<https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.2017.html>.

Department of the Interior, Bureau of the Census. *Tenth Census of the United States, Volume I, Statistics of the Population of the United States*. Washington, D.C.: Government Printing Office, 1883.

Department of the Interior, Geological Survey. "Digital Archive: Previously Unpublished Sketches by Henry W. Elliot united with the *Preliminary Field Report of the United States Geological Survey of Colorado and New Mexico*, 1869, by. F. V. Hayden." Edited by Kevin C. McKinney. <https://pubs.usgs.gov/of/2003/0384/report.pdf>.

Ebert, Frederick J. "Map of Colorado Embracing the Central Gold Region." 1869. Colorado Agriculture Bibliography, Water Resources Archive, Colorado State University, Fort Collins, Colorado. <https://mountainscholar.org/handle/10217/35691>.

Edelstein, Dan, Nicole Coleman, Ethan Jewett, Eliza Wells, Giorgio Caviglia, and Mark Braude. *Palladio*. Release 1.1. Stanford Humanities and Design Lab, 2015. <http://hdlab.stanford.edu/palladio/>.

Foster, Mike. *Strange Genius: The Life of Ferdinand Hayden*. Niwot, CO: Roberts Rinehart Publishers, 1995.

Geary, Michael. *Sea of Sand: A History of Great Sand Dunes National Park and Preserve*. Norman: University of Oklahoma Press, 2016.

Goetzmann, William. *Exploration and Empire: The Explorer and the Scientist in the Winning of the West*. Austin: Texas Historical Association, 1966.

Gonzales, Nicki. "'Yo Soy Loco Por Esa Sierra': The History of Land Rights Activism in San Luis Colorado, 1863--2002." PhD diss., University of Colorado at Boulder, 2007.

Hämäläinen, Pekka and Samuel Truett. "On Borderlands." *Journal of American History* 98, no. 2 (September 2011): 338--61. <https://doi.org/10.1093%2Fjahist%2Fjar259>.

Hamber, Anthony. *Collecting the American West: The Rise and Fall of William Blackmore*. Salisbury, UK: Hobnob Press, 2010.

Kindquist, Cathy. "Communication in the Colorado High Country." In *The Mountainous West: Explorations in Historical Geography*, edited by William Wyckoff and Lary M. Dilsaver, 114--37. Lincoln: University of Nebraska Press, 1995.

Limerick, Patricia Nelson. *The Legacy of Conquest: The Unbroken Past of the American West*. New York: W. W. Norton & Company, 1987.

Mondragon-Valdez, Maria. "Challenging Domination: Local Resistance on the Sangre de Cristo Land Grant." PhD diss., University of New Mexico,
2006.

Sánchez, Virginia. *Pleas and Petitions: Hispanic Culture and Legislative Conflict in Territorial Colorado*. Boulder: University Press of Colorado, 2020.

Schulten, Susan. *Mapping the Nation: History and Cartography in Nineteenth-Century America*. Chicago: University of Chicago Press, 2012.

Simmons, Virginia McConnell. *The San Luis Valley: Land of the Six-Armed Cross*. 2nd ed. Niwot, CO: University Press of Colorado, 1999.

Simmons, Virginia McConnell. *The Ute Indians of Utah, Colorado, and New Mexico*. Boulder: University of Colorado Press, 2001.

Sinclair, Stéfan and Geoffrey Rockwell. *Voyant Tools*. 2016. <http://voyant-tools.org/>.

Steiner, Michael and David Wrobel. "Many Wests: Discovering a Dynamic Western Regionalism." In *Many Wests: Place, Culture, and Regional Identity*, edited by David Wrobel and Michael Steiner, 1--30. Lawrence: University Press of Kansas, 1997.

White, Richard. "What is Spatial History?" Stanford Spatial History Lab, Working Paper. February 1, 2010. <https://web.stanford.edu/group/spatialhistory/cgi-bin/site/pub.php?id=29>.

William Blackmore Land Records, 1856--1870. New Mexico State Records Center and Archives, Santa Fe, New Mexico.

Wrobel, David. *Promised Lands: Promotion, Memory, and the Creation of the American West*. Lawrence: University of Kansas Press, 2002.

---

### Notes

The author would like to thank Dr. Leisl Carr Childers, the anonymous peer reviewers, and the editorial staff at *Current Research in Digital History* for their helpful comments and feedback in preparing this manuscript.

[^1]: "The Utes," *Daily Rocky Mountain News* (Denver, Colorado), October 10, 1868; "The Southern Boundary," *Daily Rocky Mountain News*, October 24, 1868.

[^2]: On Gilpin, Blackmore, and Hayden's efforts on the Sangre de Cristo
    Land Grant, see Brayer, *William Blackmore*. On Blackmore, see also,
    Hamber, *Collecting the American West*. On Hayden, see Foster,
    *Strange Genius*; Cassidy, *Ferdinand V. Hayden*. On the Hayden
    Survey, see Bartlett, *Great Surveys of the American West*;
    Goetzmann, *Exploration and Empire*, 489--529. On the circumstances
    leading to Hayden's hiring by Blackmore, see Deibert and Breithaupt,
    *Tracks, Trails & Thieves*, 58--68.

[^3]: Ferdinand V. Hayden, "Report of Professor F. V. Hayden" in *Colorado*, William Blackmore, 197. Blackmore also advertised the grant's material environment in "Southern Colorado and Its Resources: A New Field for English Emigrants," William Blackmore Land Records.

[^4]: David Wrobel has referred these promotional landscapes as the
    "promised lands" of the American West. See Wrobel, *Promised Lands*.

[^5]: Gilpin's attempt to portray the Sangre de Cristo Land Grant as
    ripe for white settlement despite the presence of Nuevomexicanos and
    Utes in the region reflects Limerick's insight that "Western history
    has been an ongoing competition for legitimacy---for the right to
    claim for oneself and sometimes for one group the status of
    legitimate beneficiary of Western resources." See Limerick, *The Legacy of Conquest*, 27.

[^6]: In positioning the San Luis Valley as a borderland, I draw here on
    Stephen Aron's concept of a "confluence region," a framework that
    positions places like the Missouri Valley borderland, which Aron
    studied, and the San Luis Valley as contested spaces of interaction
    and transformation between diverse groups of people. See Aron,
    *American Confluence*, xiii-xxi.

[^7]: The San Luis Valley's rich nineteenth century history has been
    explored in Brayer, *William Blackmore*; Simmons, *The San Luis Valley*; Mondragon Valdez, "Challenging Domination"; Gonzales, "'Yo
    Soy Loco Por Esa Sierra.'" On Utes in the San Luis Valley, see
    Simmons, *The Ute Indians of Utah, Colorado, and New Mexico*;
    Andrews, "Tata Atanasio Trujillo's Unlikely Tale,"
    4--41; see also Blackhawk, *Violence Over the Land*.

[^8]: American and European migrations to the valley, especially its
    northern portion, receive greater treatment in Geary, *Sea of Sand*.

[^9]: Cameron Blevins employs the term "imagined geography" in his
    study of the *Houston Daily Post* between 1894 and 1901. Like
    Blevins, this study treats the Colorado newspapers' "imagined
    geography" of the San Luis Valley as "an active process of social
    construction rather than a passive reflection of the world." As
    Blevins aptly puts it, "newspapers print, and thereby privilege,
    certain places over others," an argument that holds true both in
    turn-of-the-century Houston, as Blevins shows, and in the
    mid-nineteenth-century San Luis Valley. See Blevins, "Space, Nation,
    and the Triumph of Region," 124. As Susan Schulten has shown, Gilpin was well-versed in using maps like the one produced by Ebert as well as other reports to promote
    settlement of the American Western interior by the time he and
    Hayden travelled across the Sangre de Cristo Land Grant. See
    Schulten, *Mapping the Nation*, 112--5; Ebert, "Map of Colorado
    Embracing the Central Gold Region." 

[^10]: The act of reporting on the San Luis Valley was an exercise in
    what Richard White describes as "spatial representation," which
    White defines as "an attempt to conceive in order to shape what is
    lived and perceived." Through digital methods, this essay captures
    both the characteristics and geographic extent of this act of
    spatial representation. See White, "What is Spatial History?"
    Selected articles contain at least one use of "San Luis Valley,"
    were published by outlets located in the Colorado Territory, and
    were retrieved through the [Colorado Historic Newspapers Collection](https://www.coloradohistoricnewspapers.org/). Other than the 14
    articles in the corpus published by the *Saguache Chronicle*, all
    newspaper articles originated outside the San Luis Valley. Consult
    bibliography for full list of newspapers used in the corpus.

[^11]: Hayden, "Report of Professor F. V. Hayden," 196.

[^12]: Hayden, "Report of Professor F. V. Hayden," 197.

[^13]: Hayden, "Report of Professor F. V. Hayden," 200.

[^14]: Kindquist, "Communication in the Colorado High Country," 114--37.

[^15]: G.W.J., "Interesting Sketch of the San Juan Mines---Sound Advice
    to Par es \[sic\] Who Propose to Visit that Region," *Colorado Daily Chieftain*, May 9, 1872.

[^16]: Blevins, "Space, Nation, and the Triumph of Region," 124.

[^17]: Blevins, "Space, Nation, and the Triumph of Region," 124.

[^18]: Manifold, "From Del Norte," *Colorado Daily Chieftain* (Pueblo,
    Colorado), July 8, 1877.

[^19]: On early Nuevomexicano history in the San Luis Valley, readers
    should consult Simmons, *The San Luis Valley*; Mondragon-Valdez,
    "Challenging Domination"; and Gonzalez, "Yo Soy Loco Por Esa
    Sierra."

[^20]: On Ute-Nuevomexicano relations in the San Luis Valley, see
    Andrews, "Tata Atanasio Trujillo's Unlikely Tale,"
    4--41. On treaties see, for example, "Indian Treaties," *Daily Rocky Mountain News*, September 11, 1863; and "Indian Affairs," *Daily Rocky Mountain News*, February 20, 1864.

[^21]: Blackhawk, *Violence Over the Land*, 200--25.

[^22]: On Nuevomexicano activity in elections, see, for example,
    Lafayette Head, "Important from Conejos," *Daily Rocky Mountain News*, November 14, 1865; and Chaffee, "Election Returns," *Daily Rocky Mountain News*, September 17, 1870.

[^23]: A small portion of Taos County, New Mexico also lies in the San
    Luis Valley and the small, San Luis Valley communities that added to
    the county's 11,029 residents were similarly Nuevomexicano in
    demographic character. See Department of the Interior, Bureau of the
    Census, *Tenth Census of the United States*, 52--53, 72.

[^24]: Hayden, "Report of Professor F. V. Hayden," 198.

[^25]: Blevins, "Space, Nation, and the Triumph of Region," 124.

[^26]: Wrobel, *Promised Lands*; for an example of promoting white
    settlement in the San Luis Valley, see Blackmore, "Southern Colorado
    and Its Resources: A New Field for English Emigrants."

[^27]: Wrobel and Michael Steiner have argued that "at certain points in
    their personal and collective histories, Americans have been roused
    to a more vivid appreciation of place, creating historical rhythms
    in regional consciousness." Their point is appreciably visible in
    the mid-nineteenth-century San Luis Valley, where white Americans,
    Nuevomexicanos (many of whom were American citizens), and Utes all
    attempted to shape a regional consciousness. In effect, the San Luis
    Valley's history confirms not only that, as Wrobel and Steiner note,
    the American West was "really many Wests," but, in the San Luis
    Valley at least, the American West names a space where multiple
    regional identities could exist simultaneously, even in opposition
    to one another. See Steiner and Wrobel, "Many Wests," 7--9.

[^28]: Recent works by Michael Geary (2016) and Virginia Sánchez (2020)
    suggest a growing interest in linking the San Luis Valley to a
    broader regional and national context. See Geary, *Sea of Sand*; 
    Sánchez, *Pleas and Petitions*.

[^29]: Cohen et al., "Interchange," 455.

[^30]: Historians Pekka Hämäläinen and Samuel Truett argue that the
    difficulty scholars currently have with pushing borderland histories
    beyond local context and significance is the core problem facing
    borderlands history. See Hämäläinen and Truett, "On Borderlands,"
    338--61.
