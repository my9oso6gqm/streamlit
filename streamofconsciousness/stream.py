import streamlit as st

st.image('https://my9oso6gqm.github.io/mrz.jpg', width=100)

st.markdown(r'''
Maurizio (mrzgrd557@gmail.com)  
Logica matematica, teoria dei numeri, calcolo mentale, giganti sistemi di equazioni, errori nei libri di matematica, liste.
''')


st.markdown(r'''
# 17:57 10-01-2024
Ascoltando https://youtube.com/watch?v=EaJV2irv7MU

L'Hilpish propone come modo per decidere se aprire una posizione o meno:

```python
data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
```

Che in effetti e' un modo molto elegante al contrario del mio:

```python
doppia_media_mobile_df['segnali'][window_short:] = np.where(doppia_media_mobile_df['media mobile 1'][window_short:] > doppia_media_mobile_df['media mobile 2'][window_short:], 1.0, 0.0)
```

Dove dico di mettere uno zero se l'indicatore non cambia posizione. Ci sara' un motivo se tiene l'inidicatore aperto.

Tutti e due usiamo np.where per comodita' che ci permette di operare scelte sui valori in basi a condizioni arbitrarie, mi ero scritto una roba con dei loop ma se Hilpish usa np.where mi attengo al testo per prevenire batoste (qualcouno ha detto fottuto code refactoring?).

Mi faccio un caffe.

''')


st.markdown(r'''
# 17:23 10-01-2024
https://my9oso6gqm.github.io/doc/171510012024.png
''')


st.markdown(r'''
# 16:58 10-01-2024
Prosegue l'andamento guardingo delle Borse europee, che hanno cambiato più volte direzione, oscillando comunque sempre attorno alla parità, in attesa del dato sull’inflazione americana di dicembre, in calendario l'11 gennaio e cruciale in vista delle prossime decisioni di politica monetaria.  
Oltreoceano, debole anche Wall Street, in una giornata in cui non sono in calendario dati in grado di orientare il mercato. L'attenzione è rivolta ai dati macro di giovedì 11 gennaio (inflazione) e alla stagione delle trimestrali che prenderà il via il giorno successivo.  
ilsole

''')


st.markdown(r'''
# 20:41 09-01-2024
Did you know we contribute to the open source community on GitHub? Take a look at some of the projects that we've made available ➡️ https://github.com/gchq (https://twitter.com/GCHQ/status/1744762491438026899)

''')


st.markdown(r'''
# 20:21 09-01-2024
Sequestro Moro, “ha un nome il presunto uomo del Sismi che aiutò Br in via Fani” https://www.ilfattoquotidiano.it/2014/03/25/sequestro-moro-ha-un-nome-il-motociclista-del-sismi-che-aiuto-i-br-in-via-fani/925401/

''')


st.markdown(r'''
# 18:48 09-01-2024
Slow your roll, Wall Street ⚡ Barclays Head of Research Jeffrey Meli says investors are too optimistic about rate cuts, predicting the Fed will ease policy three times instead of six in 2024. https://twitter.com/moneymoverscnbc/status/1744772643717263751/



''')


st.markdown(r'''
# 17:47 09-01-2024
Prova se ha ripreso a funzionare github actions, e' tutto il giorno che sto scrivendo codice a mano per aggiornare il feed https://twitter.com/githubstatus/status/1744727187620798774
''')
st.image('https://my9oso6gqm.github.io/doc/174909012024.png')


st.markdown(r'''
# 17:19 09-01-2024
Il csirt Italia segnala che per Apple CVE-2023-41990 di Leonid Bezvershenko [https://twitter.com/bzvr_](https://twitter.com/bzvr_) & co e' sfruttata attivamente. Codice arbitrario eseguito giocherellando con i font (cavoli sta roba dei font e' un trend da un botto di anni) Eee no, NON HO LETTO, se CVE-2023-41990 riguarda Operation triangulation, ma non credo.
''')


st.markdown(r'''
# 16:23 09-01-2024
Per scrivere roba dummy uso Gemini di Google DeepMind ma sto passando a llama 2 di Facebook research.

Per il plot di due medie llama mi ha suggerito la best practice:

```python
plt.plot(df['x1'], df['x2'])
```

Ottenendo:
''')
st.image('https://my9oso6gqm.github.io/doc/162109012024.png')
st.markdown(r'''
Ehm, ma che cazz.

Migliorando il prompt (al contrario di Gemini funziona solo in inglese ma a dir la verita usavo anche Gemini cosi')

```python
plt.plot(df[['x1', 'x2']])
```
''')
st.image('https://my9oso6gqm.github.io/doc/162209012024.png')
st.markdown(r'''
Bene 🦙
''')


st.markdown(r'''
# 15:24 09-01-2024
La situazione tecnica di Banca Mediolanum rimane costruttiva. Il titolo, dopo una breve pausa di consolidamento al di sopra del sostegno grafico posto in area 8,48-8,45 euro, ha infatti compiuto un nuovo balzo in avanti ed è salito oltre quota 8,80. La tendenza di breve termine rimane quindi positiva e viene confermata dalla posizione long dei principali indicatori direzionali.  
mf
''')


st.markdown(r'''
# 15:16 09-01-2024
''')
st.image('https://my9oso6gqm.github.io/doc/151309012024.jpg')


st.markdown(r'''
# 15:00 09-01-2024
Nvidia da record: valore in borsa triplicato in un anno. Ecco le previsioni per il 2024 https://video.milanofinanza.it/video/nvidia-da-record-valore-in-borsa-triplicato-in-un-anno-ecco-le-previsioni-per-il-2024-oZf4L21y48dI
''')


st.markdown(r'''
# 14:02 09-01-2024
Banche e tecnologici rallentano il passo delle Borse europee che si muovono in negativo. Gli indici scelgono la cautela dopo i guadagni della vigilia e non seguono i rialzi decisi di Wall Street e Asia, dove Tokyo ha chiuso ai massimi da marzo 1990 trainata dai titoli high-tech. La prudenza arriva con le dichiarazioni di diversi membri delle banche centrali, che proseguono la serie di prese di posizione tendenti a ridimensionare le attese di tagli dei tassi. Questo mentre si aspetta l'inizio della stagione delle trimestrali americane con le grandi banche ai nastri di partenza da venerdì (Citigroup -0,72% , Jp Morgan, Bank Of America +0% e Wells Fargo saranno le prime).  
ilsole
''')


st.markdown(r'''
# 13:08 09-01-2024
https://youtube.com/watch?v=aZxkVTwk3wU
''')


st.markdown(r'''
# 07:17 09-01-2024
Omg un ragazzo della Wolfram research si è assegnato la issue che avevo aperto su github per usare llama di Facebook research. Presto potremmo usare llama 2 con Wolfram Mathematica!... Yeee! https://github.com/WolframResearch/Chatbook/issues/436
''')


st.markdown(r'''
# 17:16 08-01-2024
Le Borse europee, dopo aver concluso un 2023 da incorniciare (+19% la media delle piazze continentali e +28% Milano), recuperano i cali dell'avvio e viaggiano in territorio positivo dopo l'apertura di Wall Street.  

Gli indici di Wall Street sono contrastati, dopo la prima settimana in calo per gli indici delle ultime dieci. L'attenzione è rivolta soprattutto ai dati sull'inflazione, con i prezzi al consumo in programma giovedì 11 gennaio e quelli alla produzione attesi venerdì 12 gennaio, che serviranno alla Federal Reserve per valutare per quanto portare avanti una politica restrittiva, dopo l'ultimo rapporto sull'occupazione migliore delle attese.  
ilsole

''')


st.markdown(r'''
# 16:40 08-01-2024
Grafici aapl enooormiii...! https://www.youtube.com/watch?v=WO9ewCO7TYI
''')
st.image('https://my9oso6gqm.github.io/doc/163808012024.png')


st.markdown(r'''
# 12:57 08-01-2024
La cosa buffa dei luoghi comuni, è che non sono per nulla comuni. Non trovate?

''')


st.markdown(r'''
# 12:43 08-01-2024
https://www.youtube.com/watch?v=QQ_3S-IQm38

''')


st.markdown(r'''
# 12:42 08-01-2024
https://www.facebook.com/photo/?fbid=835049178422322

''')


st.markdown(r'''
# 12:26 08-01-2024
Il machine learning ci sta mettendo sul tavolo quello che conta, le emozioni, il tanto chiaccherato tra gli hr quoziente emotivo, l'abilità cognitiva o meno di provare empatia. Una rete neurale cosciente proverà emozioni? Risolve problemi, li capisce, ma orchestrerà provando gioia? Perchè si o no per una rete di neuroni?

''')


st.markdown(r'''
# 10:58 08-01-2024
Llm in giro https://my9oso6gqm.github.io/doc/105308012024.jpg
''')
st.image('https://my9oso6gqm.github.io/doc/105308012024.jpg')

st.markdown(r'''
# 10:24 08-01-2024
Ascoltando: Rose Villain - Io, me ed altri guai https://youtube.com/watch?v=wia24KWNT9M  
  
La Settimana Cibernetica del 7 gennaio 2024:  
- rilasciati aggiornamenti di sicurezza per prodotti Ivanti e Google,
- rilevato sfruttamento in rete della CVE-2023-7024 in Google (una rima dalla amy https://twitter.com/amyexp/status/1737590346023125348 ndr).

https://www.csirt.gov.it/contenuti/la-settimana-cibernetica-del-7-gennaio-2024

''')


st.markdown(r'''
# 09:55 08-01-2024
***L'ultimo bollettino continua a evidenziare miglioramenti, tranquilli!***

Enpa @ twitter. Orrori di Capodanno. Questo piccolino è stato vittima di delinquenti che gli hanno lanciato un petardo causandogli gravi danni. Scegliamo di dare notizia dei miglioramenti dovuti alle cure affettuose dei bravi veterinari. Vogliamo sperare il meglio per questa creatura innocente (https://twitter.com/enpaonlus/status/1744024915861254559).  

Leone è uscito dalla sala operatoria. Gli è stato inserito un sondino gastrico per poterlo alimentare. Sta bene.

''')


st.markdown(r'''
# 09:42 08-01-2024
Le Borse europee nella prima seduta della settimana, dopo aver concluso un 2023 da incorniciare (+19% la media delle piazze continentali e +28% Milano), si muovono all’insegna della debolezza.  
ilsole

''')


st.markdown(r'''
# 16:37 07-01-2024
Scandalo Telecom-Sismi https://it.wikipedia.org/wiki/Scandalo_Telecom-Sismi

''')


st.markdown(r'''
# 15:31 07-01-2024
GEMITAIZ - Keanu Reeves https://www.youtube.com/watch?v=lXZDLbNNXzE

''')


st.markdown(r'''
# 11:45 07-01-2024
https://my9oso6gqm.github.io/doc/114507012924.jpg

''')
st.image('https://my9oso6gqm.github.io/doc/114507012924.jpg')


st.markdown(r'''
# 09:45 07-01-2024
Evangelion: una Lancia di Longino a grandezza naturale è apparsa in Giappone https://www.justnerd.it/evangelion-una-lancia-di-longino-ad-altezza-naturale-e-apparsa-in-giappone/

''')


st.markdown(r'''
# 08:50 07-01-2024
Nikola Greku - Non hanno una voce per niente soporifera https://www.instagram.com/reel/CzOYXocq2mI/

''')


st.markdown(r'''
# 08:08 07-01-2024
Night Skinny, Ghali, Rkomi e bnkr44 - Diavolo https://youtube.com/watch?v=0VENunWYf60

''')


st.markdown(r'''
# 08:07 07-01-2024
Non hai matrici quadrate e vuoi usare Gauss? Non penso proprioh...!

''')


st.markdown(r'''
# 07:41 07-01-2024
Frankie HI-NRG MC - Quelli che benpensano https://youtube.com/watch?v=kqBR74WqMFU  
Nasi bianchi come Fruit of the Loom - Che diventano più rossi d'un livello di Doom

''')


st.markdown(r'''
# 07:23 07-01-2024
## Guerre Israël-Hamas : ce qu’il faut retenir de la journée du 5 janvier
- Israël dévoile un plan pour Gaza

Près de trois mois après le début du conflit opposant Israël au Hamas palestinien, le ministre de la défense israélien a présenté pour la première fois un plan pour l’après-guerre à Gaza, où Israël a poursuivi ses bombardements et opérations au sol vendredi.

Le plan présenté par Yoav Gallant, qui doit encore recevoir l’aval d’un gouvernement divisé, prévoit la poursuite des opérations à Gaza jusqu’au « retour des otages », au « démantèlement des capacités militaires et de gouvernance du Hamas » et à « l’élimination des menaces militaires ».

Pour l’après-guerre, M. Gallant prône une solution sans le Hamas et sans présence civile israélienne, rejetant de fait les appels de deux ministres d’extrême droite au retour de colons juifs à Gaza et à « l’émigration » des Palestiniens. Ces propos ont suscité un tollé international, dénoncés notamment par l’allié américain et l’Union européenne.

« Il n’y aura pas de présence civile israélienne dans la bande de Gaza après l’atteinte des objectifs de la guerre », a déclaré M. Gallant, précisant toutefois que l’armée garderait « sa liberté d’action » dans ce territoire pour y juguler toute « menace » éventuelle. « Les habitants de Gaza sont palestiniens. Par conséquent, des entités palestiniennes seront chargées [de la gestion] à la condition qu’il n’y ait aucune action hostile ou menace contre l’Etat d’Israël », a-t-il souligné, sans donner plus de précisions.

- La France et la Jordanie larguent sept tonnes d’aide humanitaire sur Gaza

C’est une première depuis le début de la guerre entre Israël et le Hamas, selon l’Elysée : la France et la Jordanie ont largué sept tonnes d’aide humanitaire et sanitaire sur la bande de Gaza, a annoncé vendredi Emmanuel Macron. D’après l’Elysée, l’opération de largage a été conduite dans la nuit de jeudi à vendredi par deux C-130, des avions de transport militaire, l’un français et l’autre jordanien, « avec des équipes mixtes à la fois jordaniennes et françaises dans les deux aéronefs ».

Le « fret humanitaire et sanitaire » était empilé sur des palettes et a été largué avec un système permettant de diriger les colis pour qu’ils se posent sur des zones sécurisées au plus près de la cible, l’hôpital de campagne jordanien présent sur la bande de Gaza, selon la présidence française.

Cette « opération complexe », conduite « en étroite collaboration et coordination avec l’armée de l’air jordanienne (…) a été couronnée de succès », ajoute la même source.

- 500 000 Gazaouis déplacés sans abri à Rafah

L’armée israélienne a annoncé « l’élimination d’une cellule terroriste » à Bureij, dans le centre de la bande de Gaza, et la destruction de sites de lancement de roquettes vers Israël à Khan Younès, la grande ville du Sud, épicentre des combats.

Sur le terrain, le calvaire se poursuit pour les quelque 2,4 millions de Gazaouis, dont environ 1,9 million sont déplacés par le conflit : ils manquent d’eau, de nourriture, de médicaments et de soins, les hôpitaux ne fonctionnant plus ou très difficilement.

A Rafah, la dernière ville dans le sud du petit territoire assiégé, « environ 500 000 personnes déplacées vivent autour des abris, dans les rues ou sur les routes », décrit pour l’AFP Adnan Abu Hasna, un porte-parole à Gaza de l’agence de l’ONU pour les réfugiés palestiniens (UNRWA).

- Début de la tournée au Moyen-Orient d’Antony Blinken

Le chef de la diplomatie américaine, Antony Blinken, est arrivé vendredi en Turquie, première étape de sa quatrième tournée au Moyen-Orient depuis le début du conflit, au cours de laquelle il entend plaider pour une aide accrue pour Gaza.

M. Blinken s’attend à des discussions difficiles lors de cette nouvelle tournée qui l’amènera, outre en Israël en début de semaine prochaine, dans cinq pays arabes − Jordanie, Qatar, Emirats, Arabie saoudite et Egypte − et en Cisjordanie, siège de l’Autorité palestinienne, a annoncé à la presse son porte-parole, Matthew Miller.

Son déplacement vise aussi à conjurer une extension du conflit, après l’élimination − attribuée à Israël − du numéro deux du Hamas, tué mardi dans la banlieue sud de Beyrouth, un fief du Hezbollah, par une frappe de drone. Hassan Nasrallah, le chef de ce mouvement chiite soutenu par l’Iran et allié du Hamas, a assuré vendredi que ses combattants allaient « répondre » sur « le champ de bataille » à cette frappe.

A la frontière avec le Liban, les échanges de tirs entre le Hezbollah et les forces israéliennes sont quasi quotidiens depuis le début du conflit. Vendredi, l’armée israélienne a encore mené des raids aériens visant des sites du Hezbollah. En mer Rouge, les rebelles houthistes du Yémen, soutenus par l’Iran, multiplient pour leur part les attaques de navires de commerce en « soutien » à Gaza.

- Un boom des colonies sauvages en Cisjordanie selon une ONG

Le nombre de colonies sauvages et de nouvelles routes pour les colons a connu une progression « sans précédent » en Cisjordanie depuis le début de la guerre dans la bande de Gaza, a affirmé une étude de l’ONG israélienne La Paix maintenant publiée vendredi. Selon cette organisation anti-colonisation, neuf colonies sauvages, ou « outpost » en anglais, et « dix-huit nouvelles routes pavées ou autorisées par des colons » ont fait leur apparition en Cisjordanie depuis le 7 octobre.

Quelque trois millions de Palestiniens vivent en Cisjordanie, territoire peuplé aussi par 490 000 Israéliens établis dans des colonies jugées illégales au regard du droit international mais reconnues par Israël. Or les colonies sauvages sont des implantations à la fois contraire au droit international et illégales du point de vue de l’Etat israélien.

« Les trois mois de guerre à Gaza sont instrumentalisés par des colons afin de créer un état de fait sur le terrain et ainsi prendre le contrôle de plus larges pans de la zone C », portion de la Cisjordanie sous contrôle civil militaire israélien et où se concentrent les colonies, a souligné l’ONG.

Plusieurs ténors du mouvement pro-colonies sont actuellement ministres, ce qui contribue de surcroît à créer « un environnement politique » favorable à l’essor de projets de certains colons, poursuit le rapport.

Les actes de violences de colons contre des Palestiniens en Cisjordanie ont enregistré un record en 2023, a indiqué cette semaine l’ONG israélienne Yesh Din, l’ONU ayant recensé par ailleurs 1 225 attaques de colons sur des Palestiniens au cours de l’année.

Les Etats-Unis ont imposé début décembre des sanctions à l’encontre de dizaines de colons désormais interdits d’entrée sur le territoire américain. Et la France a « décidé de prendre des mesures » contre certains colons « extrémistes », avait indiqué la cheffe de sa diplomatie Catherine Colonna.

## En direct, guerre en Ukraine : l’offensive russe s’intensifie à Avdiïvka, dans l’est du pays, affirme le chef de l’administration militaire locale

- L’offensive russe s’intensifie à Avdiïvka, dans l’est de l’Ukraine, selon le chef de l’administration militaire locale. L’armée russe mène depuis trois jours de violentes offensives autour de cette ville de l’oblast de Donetsk, « pressant de tous côtés », selon Vitalii Barabash, qui fait état de plusieurs dizaines de raids aériens par jour. Les forces russes cherchent à s’emparer depuis le début de l’automne de cette ville industrielle du Donbass qui comptait 30 000 habitants avant la guerre.

- Au moins onze personnes ont été tuées, dont cinq enfants, samedi lors d’une frappe russe ayant visé la ville de Pokrovsk et ses alentours, là aussi dans l’oblast de Donetsk. Selon les services de secours, six personnes, dont deux enfants, pourraient se trouver sous les décombres de deux bâtiments touchés. Aucune frappe russe ne restera sans conséquences, a promis le président ukrainien, Volodymyr Zelensky.

- Les forces russes ont lancé dans la journée de samedi dix-huit assauts contre la tête de pont de l’armée ukrainienne sur la rive gauche du Dniepr, « mais les soldats ukrainiens continuent à tenir leurs positions et causent des pertes importantes à l’ennemi », a assuré leur état-major, dans son point du soir. La situation reste toutefois « complexe » dans l’Est et le Sud, reconnaît-il.

- Ailleurs en Ukraine, un adulte et deux enfants ont été blessés, samedi, dans des bombardements dans la région de Kherson, dans le Sud ; une personne est morte à Toretsk, près de Bakhmout ; une autre a été tuée et deux blessées à Nikopol, dans l’Est, selon les autorités régionales respectives.

- Dans les territoires occupés par la Russie, deux personnes ont été tuées par des bombardements ukrainiens sur Makiïvka et Gorlivka, dans l’Est, lors d’une attaque qui a aussi fait plusieurs blessés, ont dit les autorités locales installées par Moscou.

- La Russie a affirmé, samedi, avoir abattu quatre missiles ukrainiens visant la Crimée, péninsule annexée en 2014 et régulièrement visée par des frappes des forces de Kiev. Elle a aussi dit avoir détruit six missiles ukrainiens navals Neptune au-dessus de la mer Noire.

- De son côté, l’armée ukrainienne a affirmé avoir frappé la base aérienne de Saky dans l’Ouest de la Crimée, revendiquant la destruction d’un dépôt de munitions russe, la péninsule étant un important nerf pour la logistique des forces russes en Ukraine.

- A Belgorod, en Russie, face au risque de bombardements ukrainiens, les autorités ont annulé la célébration nocturne du Noël orthodoxe, après avoir déjà prolongé les vacances scolaires jusqu’au 19 janvier et proposé aux habitants de cette ville de 300 000 âmes d’évacuer.

- Des femmes de Russes mobilisés pour combattre en Ukraine en septembre 2022 sur ordre de Vladimir Poutine ont mené une action symbolique de protestation, samedi, au pied des murs du Kremlin samedi en déposant des fleurs sur la flamme du soldat inconnu. La police n’est pas intervenue lors de l’action de ces femmes de mobilisés samedi, bien que tout début de contestation soit d’ordinaire sévèrement réprimé en Russie, signe que la question est délicate pour le Kremlin.

lemonde

''')


st.markdown(r'''
# 07:01 07-01-2024
Ritual - Love me back https://youtube.com/watch?v=-rnJXfulbBc

''')


st.markdown(r'''
# 10:43 06-01-2024
La scomoda verità è che non siamo più intelligenti degli altri come pensiamo. Critichiamo le qualità di Stati Uniti e Cina mancando il punto di queste nazioni focalizzato sui volumi. Le occasioni per batterci quantitivamente con questi imperi le lasciamo per strada crogiolandoci in una parossistica qualità che manco il Credit Suisse. Non abbiamo i terreni, quelli che contano nell'economia e ci azzoppiamo con la carne artificiale. Misteri elitari di noi altri.

''')


st.markdown(r'''
# 10:42 01-01-2024
Nella prima seduta del nuovo anno le Borse europee sono in deciso rialzo, riprendendo la corsa del 2023 che ha visto l’indice Stoxx600 salire di quasi il 13% e Piazza Affari guadagnare complessivamente il 28%.  
ilsole
''')


st.markdown(r'''
# 12:03 31-12-2023
Curiosità simpatica. Se da una piattaforma di trading nel mercato valutario, il forex, chessò etoro, ibkr, un conto deposito o Ubs (ha le api dirette, nel senso che a New York ha una piazza di scambio propria un po' come giocare api Euronext), insomma piattaforme tradizionali, comprate 100 dollari in euro ad esempio o, viceversa quei dollari o euro sono presso la Fed o la Banca centrale europea? Sapevetalo.

''')


st.markdown(r'''
# 11:08 31-12-2023
Ascoltando https://youtube.com/watch?v=dh8YwWlSrNY  
  
Clément Nussbaumer @ github (🇨🇭 Software Engineer, h[a,i]cker 👨‍💻 🏔 and musician 🎺 🎹, PostFinance AG, Switzerland. https://github.com/clementnuss). part2 - alternate take :) ♠️♣️♥️♦️ @ advent_of_code (https://github.com/clementnuss/advent_of_code/blob/main/2023/07/solution.py).

''')


st.markdown(r'''
# 11:01 31-12-2023
Ah, ma davvero? Doveva arrivare lui che se la gioca a Luga a dirci che Poste ha un minimo di knowhow in materia finanziaria. Grazie Nevio o come diamine ti chiami... https://www.tiktok.com/@_twitchplay_/video/7304449302523317537

''')


st.markdown(r'''
# 09:53 31-12-2023
Sul SA le ricerche principali del 2023, ne ha scelte 8. E una quale è cari miei, quale è? La prima terapia con Casgevy a modifica del dna umano con crispr approvata cosa? Un mese fa? Yeee! 

''')


st.markdown(r'''
# 08:17 31-12-2023
''')
st.image('https://my9oso6gqm.github.io/doc/081531122023.jpg')


st.markdown(r'''
# 07:41 31-12-2023
Ascoltando(1) https://youtube.com/watch?v=dh8YwWlSrNY  
  
Operation Triangulation: The last (hardware) mystery (il titolo è tutto un programma(1) ndr) https://securelist.com/operation-triangulation-the-last-hardware-mystery/111669/

''')


st.markdown(r'''
# 07:35 31-12-2023
NKVD https://it.wikipedia.org/wiki/Commissariato_del_popolo_per_gli_affari_interni

''')


st.markdown(r'''
# 20:13 29-12-2023
Louis the child - Big love https://youtube.com/watch?v=cEN6sUMuNck

''')


st.markdown(r'''
# 14:23 29-12-2023
![](https://my9oso6gqm.github.io/doc/141729122023.gif)  
Anders De Flon, 3x3, 2005, il font più piccolo.

''')


st.markdown(r'''
# 13:51 29-12-2023
Con i futures di Wall Street in leggero rialzo (+0,09% quello sul Dow Jones e +0,13% quello sull’S&P500), gli indici europei si confermano positivi, anche il Ftse Mib di Piazza Affari, in rialzo dello 0,40% a 30.452 punti grazie alla buona intonazione di Ferrari, Recordati, Erg e Unicredit. Lo spread Btp/Bund risale leggermente a 164,9 punti base. A tenere banco è la notizia che i leader del G7 discuteranno una nuova strategia legale che consentirà il sequestro di 300 miliardi di dollari di asset russi congelati, quando si incontreranno a febbraio, secondo quanto riferito due fonti a conoscenza dei piani e un funzionario britannico a Reuters.  
mf

''')


st.markdown(r'''
# 17:46 28-12-2023
La convinzione che la Federal Reserve potrà iniziare a tagliare i tassi già a marzo non basta a spingere al rialzo i listini azionari europei nelle ultime sedute dell’anno, dato che la debolezza dei titoli bancari e del settore oil compensa i rialzi degli altri comparti. Chiudono dunque piatte le Borse europee, nonostante cresca la probabilità di un allentamento della politica monetaria nel primo trimestre del 2024.  
  
Apertura poco mossa a Wall Street, anche se sta per concludersi un anno molto positivo.  
ilsole

''')


st.markdown(r'''
# 17:42 28-12-2023
Negare a queste creature una vita mentale di questa complessità in favore, ad esempio, di una teoria stimolo-risposta del loro comportamento, mentre affermare una vita mentale complessa per gli esseri umani è, ammettiamolo, una possibilità teorica.  
Tom Regan, The case for animal rights, University of California press, 1983

''')


st.markdown(r'''
# 17:17 28-12-2023
Ascoltando a palla: https://youtube.com/watch?v=ttl1s7IF1wo  
  
I moscerini stanno soddisfacendo tutti i criteri del gioco come lo intendiamo in altri animali. bioRxiv (Seeking voluntary passive movement in flies is play-like behavior) X Sciencemag (https://doi.org/10.1126/science.adk3310).

''')


st.markdown(r'''
# 14:28 28-12-2023
L'ultimo indizio per la soluzione di Kryptos, il codice più segreto del mondo http://www.rainews.it/dl/rainews/media/ultimo-indizio-per-la-soluzione-di-Kryptos-il-codice-piu-segreto-del-mondo-060a81df-2e93-4238-b774-f2fd58e7ae41.html

''')


st.markdown(r'''
# 11:49 28-12-2023
L'Nsa ha un github dove mantiene dei progetti, tra i repository vi è quello di Richard Darling ricercatore per l'Agenzia esperto in teoria della probabilità. Qualche notte scorsa sono andato a rivedere il suo lavoro, FRACTALRABBIT, ed era scritto tutto in java. Omg, sapevo che l'Nsa usa principalmente il java ma io questo lavoro me lo ricodavo in Wolfram language, vado a vedere la storia del repo e in effetti scopro che l'hanno aggiornato ma i vecchi file di Mathematica sono ancora disponibili e... la cosa fighissima è che esiste anche una versione in python nel cui codice sorgente si usa pandas, pure l'Nsa usa pandas per i suoi lavori!

''')


st.markdown(r'''
# 07:01 28-12-2023
L’incredibile statistica di Wall Street: da 95 anni scende il lunedì e guadagna martedì e mercoledì  
Andando a fondo sui dati scopriamo che un giorno non vale l’altro in Borsa. I mercati vivono di emozioni e di stagionalità. Se ad esempio prendiamo le chiusure di Wall Street negli ultimi 95 anni, scopriamo che il lunedì è il giorno più debole dei cinque in cui il listino è aperto.  
ilsole

''')


st.markdown(r'''
# 06:46 28-12-2023
Ascoltando: Sia - 1+1 (Banx & Ranx Remix) https://youtube.com/watch?v=LZ0axeyu1Ag  
  
Vale sempre questa regola?

$$
3^2 + 4^2 = 5^2
$$

Per scoprirlo dal 1985 al 1992 Wiles ha lavorato ininterrottamente solo a questo problema chiuso in soffitta e trovando la risposta; un no che sa di leggenda.  
  
Alcuni problemi sembrano semplici. Non vi è motivo per cui non debbano essere facili, eppure si rivelano estremamente intricati.  
Andrew Wiles

''')


st.markdown(r'''
# 13:49 27-12-2023
Seduta in rialzo per le Borse europee dopo il ponte natalizio e in una settimana con scambi ridotti per soli tre giorni di contrattazione prima della fine dell'anno.  
La Borsa di Tokyo conclude le contrattazioni in sostenuto rialzo, con gli acquisti che si concentrano sulla tecnologia, in scia all’accelerazione degli indici azionari Usa.  
ilsole

''')


st.markdown(r'''
# 20:41 26-12-2023
Rob Joyce @ twitter (Director of Cybersecurity at NSA. Follow NSA cyber for unique, actionable, and timely cybersecurity guidance. https://twitter.com/NSA_CSDirector/status/1738281822088241546).  
Holiday gift for you. Ghidra 11.0 released! New BSim feature can find structurally similar functions in (potentially large) collections of binaries or object files. Initial support for Rust compiled binaries. Golang improved. +more.
''')


st.markdown(r'''
# 19:05 26-12-2023
Nat Rothschild @ twitter (Interested in: public affairs, underdogs, farming, the countryside, and happily married to Loretta. Proud to be Executive Chair of Volex, but all views my own. https://twitter.com/NatRothschild1/status/1732944022174577017).  
Oh to be like Switzerland , a small country with no debt, bucket loads of cash, competent leadership, and self imposed military neutrality baked into its constitution. It has not participated in a foreign war since 1815. #iraq #afghanistan #ukraine #usa #russia.
''')

### 08:30 26-12-2023

st.markdown(r'''
# 08:30 26-12-2023
Ascoltando: Charli XCX - Love gang: https://youtube.com/watch?v=96Bo8n35LYw.  
Carlo Rovelli, How Oriented Causation Is Rooted into Thermodynamics: https://philosophyofphysics.lse.ac.uk/articles/10.31389/pop.46#B31.
''')

### 08:30 26-12-2023


### 22:09 24-12-2023

st.markdown(r'''
# 22:09 24-12-2023
Egli si esprimeva in quel francese ricercato che usavano i nostri uomini non solo per parlare, ma anche per pensare: con quelle intonazioni pacate e come protettrici proprie dell'uomo importante abituato ai modi del gran mondo e della corte.  
Lev Tolstoj, Guerra e pace
''')

### 22:09 24-12-2023


### 21:47 24-12-2023

st.markdown(r'''
# 21:47 24-12-2023
Il ritorno in finanza e' il profitto di un investimento, una formula per calcolare il ritorno logaritmico e':

$$
R_{log} = \ln \frac{V_f}{V_i}
$$

Che puo' essere anche vista come un'equazione:

$$
V_f = V_ie^{r_{\log}t}
$$
''')

### 21:47 24-12-2023


### 09:58 24-12-2023

st.markdown(r'''
# 09:58 24-12-2023

## Guerra Israele - Hamas

- Deux mois et demi après le début de la guerre entre Israël et le Hamas, le 7 octobre, le mouvement islamiste a déclaré que les opérations militaires israéliennes dans l’enclave palestinienne ont fait, selon lui, 20 258 morts et plus de 53 000 blessés. Selon le ministère de la santé de Gaza, contrôlé par le Hamas, ce bilan comprend 201 personnes tuées durant les dernières vingt-quatre heures.

- Le porte-parole du ministère du Hamas, Ashraf Al-Qudra, a accusé l’armée israélienne d’avoir « commis plusieurs massacres atroces entraînant la mort de dizaines de personnes dans le camp et la ville de Jabaliya, et dans la zone de Tal Al-Zaatar », dont certains civils « exécutés » selon lui, lors d’une opération terrestre. Il a également affirmé que l’aviation et l’artillerie israéliennes ont visé plusieurs cibles du nord au sud du territoire, dont le camp de réfugiés de Nousseirat (centre) où une frappe a tué 18 personnes.

- Sollicitée par l’Agence France-Presse (AFP), l’armée d’Israël n’a pas spécifiquement répondu aux accusations d’exécutions, mais a assuré que ses frappes « contre des cibles militaires sont conformes aux dispositions du droit international ». Des images de l’AFPTV montrent un corps sous les décombres dans les rues de Jabaliya ainsi que des destructions massives.

- Le président américain Joe Biden a de nouveau appelé samedi le premier ministre israélien, Benyamin Nétanyahou, à protéger les civils dans la bande de Gaza. « Le président a souligné le besoin crucial de protéger la population civile, dont ceux qui contribuent aux opérations d’aide humanitaire, et l’importance de permettre aux civils de quitter en sécurité les zones où les combats continuent de se dérouler », déclare un communiqué de la Maison Blanche.

- Plus tôt dans la journée, M. Biden avait dit aux journalistes de la Maison Blanche qu’il avait eu une « longue discussion » avec M. Nétanyahou, qu’il avait qualifiée de « conversation privée ». En réponse à une question, M. Biden a déclaré : « Je n’ai pas demandé de cessez-le-feu ». Selon le texte publié par Washington, les deux dirigeants ont discuté des « objectifs et du phasage » de la campagne militaire israélienne ainsi que de questions de sécurité.

## Guerra Russia - Ucraina

- Le ministre de la défense ukrainien, Rustem Umerov, a évoqué à la télévision publique ukrainienne la possibilité d’envoyer des convocations militaires en ligne aux ressortissants de son pays qui vivent à l’étranger. Après des propos similaires tenus jeudi, le ministère de la défense ukrainien avait précisé que le ministre parlait de manière générale de l’importance de rejoindre l’armée pour les Ukrainiens, y compris ceux vivant à l’étranger.

- Selon l’état-major ukrainien, « la situation opérationnelle dans l’est et le sud de l’Ukraine reste difficile ». « Au cours de la journée du 23 décembre, l’ennemi a lancé 11 missiles, 14 frappes aériennes, 21 attaques de MLRS [lance-roquettes multiples] sur les positions des troupes ukrainiennes et sur diverses localités », a-t-il détaillé samedi.

- Une attaque de drone dans l’oblast de Kherson a causé la mort d’une personne, a annoncé, samedi, le gouverneur. « Un habitant de 69 ans a succombé à ses blessures », a écrit sur Telegram Oleksandr Prokudin, précisant que l’attaque avait eu lieu sur la ville de Stanislav.

- Au moins sept personnes ont été blessées à Kherson, après un bombardement russe qui a provoqué un incendie, samedi, a fait savoir le gouverneur. Dans la journée, Olexsandr Prokudin avait déjà dit que l’armée russe avait « frappé une infrastructure critique de Kherson » provoquant « une montée en puissance des réseaux de gaz », qui a ensuite déclenché « un incendie ».  

lemonde
''')

### 09:58 24-12-2023


### 04:01 24-12-2023

st.markdown(r'''
# 04:19 24-12-2023
A Natale 1 milione di italiani ammalati, non vi imbottite di farmaci fino ad azzerare i sintomi è il monito del virologo Fabrizio Pregliasco sul sole24ore. Aggiungendo che grandi sbalzi termici favoriscono alla grande questi virus.

Il classico modello sir dal sito della Maa:
''')

st.latex(r'''
\begin{align*}
& \frac{\textit{d}s}{\textit{dt}} = -b\ s(t)\ i(t)\\

& \frac{\textit{d}i}{\textit{dt}} = b\ s(t)\ i(t) - k\ i(t)\\

& \frac{\textit{d}r}{\textit{dt}} = k\ o(t)
\end{align*}
''')

st.markdown(r'''
Che riesce a catturare anche gli effetti del virus dettati dagli sbalzi termici.
''')

### 04:01 24-12-2023


### 07:34 23-12-2023

st.markdown(r'''
# 07:34 23-12-2023

Ascoltando: Galantis - Bang bang! (My neurodivergent anthem) [https://youtube.com/watch?v=CquFFychvTo](https://youtube.com/watch?v=CquFFychvTo).  
Il task per le 9: https://my9oso6gqm.github.io/pdfjs/web/viewer.html?file=https://my9oso6gqm.github.io/tmp/231220230820.pdf.
''')

### 07:34 23-12-2023


### 22:09 22-12-2023

st.markdown(r'''
# 22:09 22-12-2023
Chiudono deboli le Borse europee nell'ultima seduta prima della pausa natalizia, nonostante il dato sull'inflazione Pce negli Stati Uniti rafforzi l'ottimismo sulle prossime mosse di politica monetaria.  
ilsole''')

### 22:09 22-12-2023


### 10:26 21-12-2023

st.markdown(r'''
# 10:26 21-12-2023
Ascoltando: Achille Lauro - Fragole https://youtube.com/watch?v=fCj2p1Ugwdo.  
Aperta una posizione buy da python su ibkr, non si poteva chiudere quello che ho fatto da app dopo capite il perchè(1): https://my9oso6gqm.github.io/pdfjs/web/viewer.html?file=https://my9oso6gqm.github.io/tmp/211220231026.pdf.
''')

### 10:26 21-12-2023


### 22:46 20-12-2023

st.markdown(r"""
# 22:46 20-12-2023
Piazzare un buy o un sell in ibkr: https://ibkrcampus.com/trading-lessons/python-placing-orders/.
""")

### 22:46 20-12-2023


### 22:17 20-12-2023

st.markdown(r"""
# 22:17 20-12-2023
La conferma che la battaglia contro l’inflazione stia dando i suoi frutti arriva stavolta dal Regno Unito, ma questo non è bastato ad accendere le Borse europee che chiudono fiacche la seduta, con la sola eccezione di Londra, che guadagna oltre l'1%. Wall Street in rialzo dopo la pubblicazione di dati economici positivi.  
ilsole
""")

### 22:17 20-12-2023


### 09:02 20-12-2023

st.markdown(r"""
# 09:02 20-12-2023
Gayle - Ur just horny https://youtube.com/watch?v=DWvuD31VG6Q.
""")
