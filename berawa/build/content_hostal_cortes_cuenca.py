# Contenido de la demo Hostal Cortés (Cuenca) (es/en/fr/de). Hechos de hostalcortes.com leidos el 02/11/2026 (ver berawa/sources.json). Sin valoraciones; sin precios ni codigos promocionales.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hostal real.','en':' Images are illustrations and do not show the actual hostal.','fr':' Les images sont des illustrations et ne montrent pas l’hostal réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hostal.'}
H={'es':['Individual y doble','Matrimonio y triple'],'en':['Single and twin','Double and triple'],'fr':['Individuelle et double','Grand lit et triple'],'de':['Einzel- und Zweibettzimmer','Doppel- und Dreibettzimmer']}
RD={
'es':['Habitaciones individuales y dobles con baño privado, televisión plana y wifi, para visitas de negocios u ocio.','Habitaciones de matrimonio y triples, con las mismas comodidades, para viajar en pareja o en familia.'],
'en':['Single and twin rooms with private bathroom, flat-screen TV and wifi, for business or leisure.','Double and triple rooms with the same comforts, for couples or families.'],
'fr':['Chambres individuelles et doubles avec salle de bain privée, télévision à écran plat et wifi, pour le travail ou les loisirs.','Chambres à grand lit et triples, avec le même confort, pour voyager en couple ou en famille.'],
'de':['Einzel- und Zweibettzimmer mit eigenem Bad, Flachbildfernseher und WLAN, für Geschäfts- oder Urlaubsreisen.','Doppel- und Dreibettzimmer mit gleichem Komfort, für Paare oder Familien.']}
ART={
'hero':('skyline',1631,['#1d2530','#d0995a','#f2d4a4','#6a5a4a','#4a3e34','#262019']),
'intro':('arches',1632,['#f2ede6','#faf7f1','#8a5e36','#5e4026','#2e2013']),
'r1':('columns',1641,['#efeae2','#cf9a5c','#8a5e36','#5e4026','#2e2013']),
'r2':('arches',1642,['#1d2530','#d8a466','#f4dcb2','#726252','#52463a','#2a241c']),
'g1':('hills',1651,['#ece6da','#f2deba','#cf9a5c','#a09676','#766e54','#4e4938']),
'g2':('skyline',1652,['#1d2530','#d8a466','#f4dcb2','#726252','#52463a','#2a241c']),
'g3':('columns',1653,['#f1ece4','#f9f6f0','#8e6038','#604228','#2e2013']),
'g4':('hills',1654,['#1d2530','#d0995a','#f2d4a4','#6a5a4a','#4a3e34','#262019'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal Cortés · Hostal familiar en el centro de Cuenca',see_rooms='Ver las habitaciones',hero_k='Cuenca · Ramón y Cajal, 45',hero_t='Un lugar tranquilo y familiar en pleno centro de Cuenca',hero_s='Desde 1916, primero como posada y hoy como hostal recientemente reformado.',
 intro_t='Más de un siglo dando hospedaje',intro_p1='Gabriel Cortés Martínez fundó la posada de Cortés en la calle Ramón y Cajal alrededor de 1916. En febrero de 2017 el hostal reabrió, pasando a una nueva generación.',
 intro_p2='A escasos minutos del casco histórico y de la zona de ocio y gastronomía, y a unos metros de las estaciones de tren y autobús.',
 stats=['Desde 1916','44 habitaciones','Recepción 24 horas','Parking privado'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Todas con baño privado, televisión plana y wifi.',
 svcs=['Recepción 24 horas','Wifi gratuito en todo el hostal','Parking privado','Cafetería','Guardaequipajes','Trato familiar'],
 around_s='Cuenca, ciudad declarada patrimonio de la humanidad por la UNESCO, y la Serranía de Cuenca.',
 loc_p='Calle de Ramón y Cajal, 45 · 16004 Cuenca, en pleno centro. Recepción abierta 24 horas.',
 chips=['¿Qué habitaciones tenéis?','¿Hay parking?','¿Hay recepción 24 horas?','¿Cómo reservo?']),
'en':dict(title='Hostal Cortés · Family-run hostal in central Cuenca',see_rooms='See the rooms',hero_k='Cuenca · Ramón y Cajal, 45',hero_t='A quiet, family-run place right in the centre of Cuenca',hero_s='Since 1916, first as an inn and today as a recently refurbished hostal.',
 intro_t='More than a century of hospitality',intro_p1='Gabriel Cortés Martínez founded the Cortés inn on Ramón y Cajal street around 1916. In February 2017 the hostal reopened, passing to a new generation.',
 intro_p2='A few minutes from the old town and the leisure and food area, and a few metres from the train and bus stations.',
 stats=['Since 1916','44 rooms','24-hour reception','Private parking'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='All with private bathroom, flat-screen TV and wifi.',
 svcs=['24-hour reception','Free wifi throughout','Private parking','Café','Luggage storage','Family-style service'],
 around_s='Cuenca, a city on UNESCO’s World Heritage list, and the Serranía de Cuenca.',
 loc_p='Calle de Ramón y Cajal, 45 · 16004 Cuenca, right in the centre. Reception open 24 hours.',
 chips=['Which rooms do you have?','Is there parking?','Is reception open 24 hours?','How do I book?']),
'fr':dict(title='Hostal Cortés · Hostal familial au centre de Cuenca',see_rooms='Voir les chambres',hero_k='Cuenca · Ramón y Cajal, 45',hero_t='Un lieu calme et familial en plein centre de Cuenca',hero_s='Depuis 1916, d’abord auberge et aujourd’hui hostal récemment rénové.',
 intro_t='Plus d’un siècle d’hospitalité',intro_p1='Gabriel Cortés Martínez a fondé l’auberge de Cortés rue Ramón y Cajal vers 1916. En février 2017, l’hostal a rouvert, repris par une nouvelle génération.',
 intro_p2='À quelques minutes du centre historique et du quartier des loisirs et de la gastronomie, et à quelques mètres des gares ferroviaire et routière.',
 stats=['Depuis 1916','44 chambres','Réception 24 h/24','Parking privé'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Toutes avec salle de bain privée, télévision à écran plat et wifi.',
 svcs=['Réception 24 h/24','Wifi gratuit partout','Parking privé','Cafétéria','Bagagerie','Accueil familial'],
 around_s='Cuenca, ville inscrite au patrimoine mondial de l’UNESCO, et la Serranía de Cuenca.',
 loc_p='Calle de Ramón y Cajal, 45 · 16004 Cuenca, en plein centre. Réception ouverte 24 h/24.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un parking ?','La réception est-elle ouverte 24 h/24 ?','Comment réserver ?']),
'de':dict(title='Hostal Cortés · Familiengeführtes Hostal im Zentrum von Cuenca',see_rooms='Zimmer ansehen',hero_k='Cuenca · Ramón y Cajal, 45',hero_t='Ein ruhiger, familiärer Ort mitten im Zentrum von Cuenca',hero_s='Seit 1916, zuerst als Gasthaus und heute als kürzlich renoviertes Hostal.',
 intro_t='Über ein Jahrhundert Gastfreundschaft',intro_p1='Gabriel Cortés Martínez gründete das Gasthaus Cortés in der Calle Ramón y Cajal um 1916. Im Februar 2017 öffnete das Hostal wieder, in den Händen einer neuen Generation.',
 intro_p2='Wenige Minuten von der Altstadt und dem Ausgeh- und Gastronomieviertel, und wenige Meter von Bahnhof und Busbahnhof.',
 stats=['Seit 1916','44 Zimmer','Rezeption rund um die Uhr','Privatparkplatz'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Alle mit eigenem Bad, Flachbildfernseher und WLAN.',
 svcs=['Rezeption rund um die Uhr','Kostenloses WLAN im ganzen Haus','Privatparkplatz','Cafeteria','Gepäckaufbewahrung','Familiärer Service'],
 around_s='Cuenca, von der UNESCO zum Weltkulturerbe erklärt, und die Serranía de Cuenca.',
 loc_p='Calle de Ramón y Cajal, 45 · 16004 Cuenca, mitten im Zentrum. Rezeption rund um die Uhr geöffnet.',
 chips=['Welche Zimmer gibt es?','Gibt es Parkplätze?','Ist die Rezeption rund um die Uhr besetzt?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://hostalcortes.com/?ohbe-availability'
BOOK=dict(mode='engine',url=dict(es=R,en=R,fr=R,de=R))
D=dict(name='Hostal Cortés',ac='#1f2630',ac2='#8a5e36',ac2_a11y='#6a4626',book=BOOK,around=['Casco antiguo de Cuenca','Serranía de Cuenca'],foot=FOOT,
 address='Calle de Ramón y Cajal, 45 · 16004 Cuenca',phones=['+34 969 22 04 00'],emails=['info@hostalcortes.com'],maps='Hostal Cortés, Calle de Ramón y Cajal 45, 16004 Cuenca',t=T)
META=dict(repo='demo-hostal-cortes-cuenca',name='Hostal Cortés',legal_name='HASCOR ALOJAMIENTOS S.L. (aviso legal de su web)',registry_ids=['B16330334'],
 url='https://hostalcortes.com/',domain='hostalcortes.com',municipality='Cuenca',province='Cuenca',sector='hostal familiar en el centro de Cuenca',
 read_at='2026-11-02T07:12:00+01:00',created_at='2026-11-02T07:11:00+01:00',built_at='2026-11-02T07:20:00+01:00',audit_date='2026-11-02T06:49:57+01:00',
 rating=dict(value=4.2,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Hostal+Cortes/@40.0693983,-2.1354618,17z'),
 book=dict(mode='engine',url=R,note='motor de reservas propio de su web (buscador OHBE en la portada, ?ohbe-availability), HTTP 200 comprobado el 02/11/2026; su web solo esta en espanol, los 4 idiomas usan ese mismo motor.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Cuántas habitaciones tiene?','K01'),('¿Hay parking?','K02'),('¿Hay recepción 24 horas?','K03'),('¿Hay wifi?','K04'),('¿Hay cafetería?','K05'),('¿Puedo dejar el equipaje?','K06'),('¿Dónde está el hostal?','K07'),('¿Está cerca de la estación?','K07'),('¿Desde cuándo existe el hostal?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('How many rooms does it have?','K01'),('Is there parking?','K02'),('Is reception open 24 hours?','K03'),('Is there wifi?','K04'),('Is there a café?','K05'),('Can I leave my luggage?','K06'),('Where is the hostal?','K07'),('Is it near the station?','K07'),('How old is the hostal?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Combien de chambres a-t-il ?','K01'),('Y a-t-il un parking ?','K02'),('La réception est-elle ouverte 24 h/24 ?','K03'),('Y a-t-il le wifi ?','K04'),('Y a-t-il une cafétéria ?','K05'),('Puis-je laisser mes bagages ?','K06'),('Où se trouve l’hostal ?','K07'),('Est-ce près de la gare ?','K07'),('Depuis quand existe l’hostal ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Wie viele Zimmer hat das Hostal?','K01'),('Gibt es Parkplätze?','K02'),('Ist die Rezeption rund um die Uhr besetzt?','K03'),('Gibt es WLAN?','K04'),('Gibt es eine Cafeteria?','K05'),('Kann ich mein Gepäck abgeben?','K06'),('Wo liegt das Hostal?','K07'),('Ist es nahe am Bahnhof?','K07'),('Seit wann gibt es das Hostal?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Was kostet eine Nacht?',None),('Haben Sie ein Schwimmbad?',None)]}
