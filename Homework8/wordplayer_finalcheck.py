""" EC602 Fall 2017

wordplayer checker for python and C++

"""

from subprocess import PIPE,Popen,run
import time
import os
import urllib.request
import random
import sys
from io import StringIO

try:
    import ec602lib
except Exception as e:
	print(e)
	quit()

try:
    assert ec602lib.VERSION >= (2,2)
except:
    print('please download the updated ec602lib.py before continuing')
    quit()


Tests_Short=[
('macabre 6',[]),
('macabre 5',['cream']),
('macabre 4',[]),
('leap 4', ['leap', 'peal']),
('apoplectic 7',[]),
('apoplectic 6',[]),
('apoplectic 5',['apple']),
('apoplectic 4',['leap', 'peal']),
('abcdabcd 4',['aabb', 'abcd', 'adad', 'bbaa', 'daad', 'dada', 'dcab']),
('abcdabcd 3',['aab', 'aac', 'aad']),
('aabcbc 3',['aab', 'aac']),
]

Tests_Big=[
('anechocixq 8',['anechoic']),
('hemangiomatacountermarch 17',[]),
('testthisprogram 11',['prostatites', 'prosthetist', 'seismograph', 'straightest', 'thermistors', 'thermostats']),
]


Tests_Speed = [
({'cpp':0.000208,'py':0.000294},'on 2',['no','on'],),
({'cpp':6.57e-05,'py':0.000123},'act 3',['act', 'cat']),
({'cpp':0.00087,'py':0.01757},'apoplecticmacabre 5',['abaca', 'abaci', 'abamp', 'abate', 'abeam', 'abele', 'abler', 'aboil', 'aboma', 'abort', 'acari', 'acerb', 'aceta', 'acmic', 'actor', 'aecia', 'aerie', 'aimer', 'alamo', 'alarm', 'alate', 'alert', 'altar', 'alter', 'amber', 'ambit', 'amble', 'ameba', 'ameer', 'amice', 'amole', 'amort', 'ample', 'aorta', 'apace', 'apart', 'aport', 'appal', 'appel', 'apple', 'apter', 'areae', 'areal', 'areca', 'areic', 'arete', 'ariel', 'armet', 'aroma', 'artal', 'artel', 'atria', 'atrip', 'bacca', 'baler', 'baric', 'becap', 'belie', 'beret', 'berme', 'betel', 'biome', 'biota', 'birle', 'biter', 'blame', 'blare', 'blate', 'blear', 'bleat', 'bleep', 'blimp', 'blite', 'bloat', 'boart', 'bocce', 'bocci', 'boite', 'bolar', 'boral', 'boric', 'botel', 'brace', 'bract', 'brail', 'bream', 'broil', 'brome', 'cabal', 'caber', 'cable', 'cacao', 'cacti', 'caeca', 'camel', 'cameo', 'campi', 'campo', 'caper', 'carat', 'carbo', 'caret', 'carle', 'carob', 'carol', 'carom', 'carpi', 'carte', 'cater', 'cecal', 'ceiba', 'celeb', 'celom', 'ceorl', 'cerci', 'ceria', 'ceric', 'cibol', 'circa', 'citer', 'claim', 'clamp', 'clapt', 'claro', 'clear', 'cleat', 'clepe', 'clept', 'climb', 'clime', 'clipt', 'clomb', 'clomp', 'coact', 'coala', 'coapt', 'coati', 'cobia', 'coble', 'cobra', 'cocci', 'colic', 'comae', 'comal', 'combe', 'comer', 'comet', 'comic', 'compt', 'comte', 'copal', 'coper', 'copra', 'coral', 'coria', 'craal', 'cramp', 'crape', 'crate', 'cream', 'creel', 'creep', 'creme', 'crepe', 'crept', 'crime', 'crimp', 'cripe', 'croci', 'eater', 'eclat', 'elate', 'elect', 'elemi', 'elite', 'elope', 'embar', 'ember', 'emote', 'epact', 'erect', 'erica', 'etape', 'ileac', 'impel', 'irate', 'laari', 'labia', 'labor', 'labra', 'lacer', 'lamer', 'lamia', 'laree', 'later', 'leapt', 'leper', 'lepta', 'liber', 'libra', 'limba', 'limbo', 'limpa', 'lirot', 'liter', 'litre', 'lobar', 'loper', 'lotic', 'macer', 'macle', 'macro', 'maile', 'malar', 'malic', 'maple', 'maria', 'mater', 'mbira', 'mecca', 'melic', 'merit', 'merle', 'metal', 'meter', 'metre', 'metro', 'micra', 'micro', 'miler', 'milpa', 'miter', 'mitre', 'moira', 'moire', 'molar', 'moper', 'morae', 'moral', 'morel', 'motel', 'oater', 'obeli', 'ocrea', 'octal', 'oiler', 'oleic', 'omber', 'ombre', 'opera', 'optic', 'orate', 'orbit', 'oriel', 'pacer', 'palea', 'paler', 'palet', 'palpi', 'pampa', 'papal', 'paper', 'pareo', 'parle', 'parol', 'pater', 'patio', 'peace', 'pearl', 'peart', 'pepla', 'perea', 'peril', 'petal', 'peter', 'pibal', 'pical', 'picot', 'piece', 'pieta', 'pilar', 'pilea', 'pilot', 'pipal', 'piper', 'pipet', 'place', 'plait', 'plate', 'pleat', 'plebe', 'plica', 'plier', 'polar', 'poler', 'praam', 'prate', 'price', 'prima', 'prime', 'primo', 'primp', 'probe', 'proem', 'prole', 'rabat', 'rabic', 'ramee', 'ramet', 'ramie', 'ratal', 'ratel', 'ratio', 'react', 'realm', 'reata', 'rebec', 'rebel', 'rebop', 'recap', 'recce', 'recta', 'recti', 'recto', 'relet', 'relic', 'relit', 'remap', 'remet', 'remit', 'reoil', 'repel', 'repot', 'retem', 'retia', 'retie', 'riata', 'roble', 'taber', 'tabla', 'table', 'tabor', 'talar', 'taler', 'tamal', 'tamer', 'taper', 'tapir', 'taroc', 'telae', 'telia', 'telic', 'teloi', 'tempi', 'tempo', 'tepal', 'terai', 'terce', 'tiara', 'tical', 'tiler', 'timer', 'toile', 'topee', 'toper', 'topic', 'toric', 'trace', 'trail', 'tramp', 'triac', 'trial', 'tribe', 'trice', 'triol', 'tripe', 'tromp', 'trope']),
({'cpp':0.000325,'py':0.0049},'psychohistoriannoncollector 15',['anthropocentric', 'chancellorships', 'contrapositions', 'controllerships', 'cooperationists', 'corticotrophins', 'ethnohistorians', 'ethnohistorical', 'interscholastic', 'introspectional', 'ionospherically', 'neocolonialists', 'noncooperations', 'noncorrelations', 'nonpsychiatrist', 'prehistorically', 'protohistorians', 'psychohistorian', 'synchronisation', 'thyrocalcitonin']),
({'cpp':0.00118,'py':0.0391},'punishableanglerfishes 10',['airinesses', 'anablepses', 'anageneses', 'anagenesis', 'anglerfish', 'aphaereses', 'aphaeresis', 'aspergilla', 'aspergilli', 'assignable', 'aubergines', 'ballerinas', 'barenesses', 'baseliners', 'beleaguers', 'bengalines', 'bilinguals', 'billfishes', 'bleariness', 'bluefishes', 'bluenesses', 'bluishness', 'braininess', 'burnishing', 'bushelling', 'eelgrasses', 'enfeebling', 'enfleurage', 'engineries', 'enshrinees', 'ensphering', 'enuresises', 'epigenesis', 'euphrasies', 'fairnesses', 'fellnesses', 'fiberglass', 'fibreglass', 'filariases', 'finenesses', 'fingernail', 'flashiness', 'fleshiness', 'frangipane', 'frangipani', 'freebasing', 'freshening', 'fullerenes', 'fullnesses', 'furbishing', 'furnishing', 'galleasses', 'galliasses', 'garishness', 'garnishees', 'generalise', 'glibnesses', 'graininess', 'greaseball', 'greaseless', 'greasiness', 'greenflies', 'grisailles', 'grisliness', 'halenesses', 'halfnesses', 'hanselling', 'harnessing', 'harshening', 'highfliers', 'highnesses', 'hirselling', 'hugenesses', 'hungriness', 'inarguable', 'infeasible', 'inselberge', 'inselbergs', 'insensible', 'insphering', 'langlaufer', 'languisher', 'languishes', 'leannesses', 'liberalise', 'linearises', 'lungfishes', 'nasalising', 'nearnesses', 'nebulising', 'nephelines', 'neuralgias', 'nighnesses', 'nullifiers', 'painfuller', 'palenesses', 'palliasses', 'panellings', 'pangeneses', 'pangenesis', 'parfleshes', 'passengers', 'passerines', 'pearlashes', 'pellagrins', 'penalising', 'peninsular', 'peninsulas', 'perennials', 'perihelial', 'perishable', 'persiflage', 'phalangers', 'pilferable', 'pilferages', 'pingrasses', 'plagiaries', 'plagiarise', 'planishers', 'planishing', 'pleasuring', 'plenishing', 'pleurisies', 'plushiness', 'preassigns', 'prebilling', 'preblesses', 'prehensile', 'presageful', 'preselling', 'publishers', 'publishing', 'puninesses', 'punishable', 'purenesses', 'railbusses', 'realnesses', 'reeligible', 'refinishes', 'refuelling', 'reinfusing', 'relabeling', 'releasable', 'relishable', 'repaneling', 'repassages', 'repealable', 'resealable', 'reshingles', 'respelling', 'rifenesses', 'ringhalses', 'ripenesses', 'safranines', 'sailfishes', 'sailplaner', 'sailplanes', 'salesgirls', 'seafarings', 'serialises', 'serpigines', 'shanghaier', 'sharpening', 'shearlings', 'shellfires', 'shinneries', 'shrillness', 'signalises', 'signallers', 'sinfulness', 'singleness', 'singspiels', 'slanginess', 'sleepiness', 'spinneries', 'spiralling', 'suberising', 'subleasing', 'subpenaing', 'sullenness', 'superbness', 'supergenes', 'supersales', 'supersells', 'supineness', 'surpassing', 'uglinesses', 'uneasiness', 'unfairness', 'unfeasible', 'ungainlier', 'unleashing', 'unpassable', 'unpleasing', 'unreliable', 'unripeness', 'unshelling', 'unsphering', 'urbanising', 'usableness']),
({'cpp':0.00013,'py':0.000152},'anechocixq 8',['anechoic']),
({'cpp':0.00336,'py':0.05306},'psychohistoriannoncollector 8',
['accentor', 'acceptor', 'acentric', 'acetonic', 'acetylic', 'achiness', 'achiotes', 'acolytes', 'aconites', 'aconitic', 'acrolect', 'acrolein', 'acrolith', 'acrostic', 'acrylics', 'actinons', 'actorish', 'actressy', 'acyloins', 'aerolith', 'aerosols', 'ailerons', 'ainsells', 'airholes', 'airiness', 'airliner', 'airlines', 'airports', 'airposts', 'airships', 'airstrip', 'alcohols', 'alencons', 'alienist', 'alienors', 'allicins', 'allotter', 'allotype', 'allspice', 'alnicoes', 'alopecic', 'alphorns', 'alphosis', 'alpinely', 'alpinist', 'althorns', 'altoists', 'ancestor', 'ancestry', 'anchoret', 'ancients', 'anechoic', 'anethols', 'anilines', 'anisoles', 'annoyers', 'anointer', 'anolytes', 'anoretic', 'anorthic', 'anterior', 'anthesis', 'anthills', 'anticity', 'antihero', 'antiphon', 'antipill', 'antipole', 'antiporn', 'antipyic', 'antiriot', 'antiroll', 'antiship', 'antislip', 'antitype', 'antlions', 'antrorse', 'antsiest', 'aoristic', 'aphelion', 'aphonics', 'aphorise', 'aphorist', 'apocrine', 'apostils', 'apostles', 'apricots', 'apyretic', 'archines', 'archness', 'arcsines', 'arnottos', 'arsenics', 'arsonist', 'articles', 'artiness', 'artistes', 'artistic', 'artistry', 'artsiest', 'ascetics', 'asperity', 'aspersor', 'aspheric', 'aspirers', 'aspirins', 'assentor', 'assertor', 'assorter', 'asthenic', 'astonies', 'astonish', 'astricts', 'atechnic', 'atheists', 'athletic', 'atrocity', 'atrophic', 'atropine', 'atropins', 'attorney', 'cachepot', 'calcines', 'calcites', 'calcitic', 'caliches', 'calicles', 'calicoes', 'calipers', 'calliope', 'calliper', 'calloses', 'calorics', 'calories', 'calottes', 'calotype', 'caloyers', 'calthrop', 'caltrops', 'calycine', 'calycles', 'calypsos', 'calypter', 'canephor', 'caninity', 'canister', 'canities', 'cannelon', 'canniest', 'cannonry', 'canoeist', 'canoness', 'canonise', 'canonist', 'canopies', 'canticle', 'cantrips', 'capelins', 'capitols', 'caponier', 'capricci', 'caprices', 'capriole', 'capsicin', 'capstone', 'captions', 'carillon', 'carioles', 'carlines', 'caroches', 'carolers', 'caroller', 'carotins', 'carpools', 'carports', 'carrells', 'carriole', 'carrions', 'carritch', 'carrotin', 'carryons', 'cartoons', 'cartoony', 'caryotin', 'cashiers', 'catchers', 'catchier', 'catechin', 'catechol', 'cathects', 'catholic', 'cationic', 'cellists', 'celosias', 'cenotaph', 'centrals', 'centrist', 'ceorlish', 'cephalic', 'cephalin', 'ceratins', 'cesspool', 'chaconne', 'chalices', 'challies', 'challoth', 'chalones', 'chancels', 'chancery', 'chancier', 'chancily', 'chancres', 'channels', 'chansons', 'chanters', 'chanteys', 'chanties', 'chantors', 'chaperon', 'chapiter', 'chaplets', 'chapters', 'chariest', 'chariots', 'charleys', 'charlies', 'charnels', 'charpoys', 'charters', 'chartist', 'chastely', 'chastens', 'chastest', 'chastise', 'chastity', 'chattels', 'chatters', 'chattery', 'chattier', 'chattily', 'chayotes', 'cheapish', 'chelator', 'cheroots', 'chiastic', 'chicaner', 'chicanes', 'chicanos', 'chiccory', 'chicness', 'chiliast', 'chillers', 'chillest', 'chillier', 'chillies', 'chinches', 'chinless', 'chinones', 'chintses', 'chirpers', 'chirpier', 'chirpily', 'chitchat', 'chitlins', 'chitosan', 'chitters', 'chitties', 'chlorals', 'chlorate', 'chlorine', 'chlorins', 'chlorite', 'choicely', 'choicest', 'cholates', 'cholents', 'choleras', 'choleric', 'cholines', 'choosers', 'choosier', 'chopines', 'chorales', 'chorally', 'chorines', 'chorions', 'chortler', 'chortles', 'christen', 'christie', 'chronics', 'chronons', 'chthonic', 'ciceroni', 'cilantro', 'ciliates', 'cinchona', 'cineasts', 'cinerary', 'cinerins', 'cipolins', 'circlers', 'circlets', 'cisterna', 'cisterns', 'cistrons', 'citation', 'citators', 'citatory', 'citherns', 'cithrens', 'citrates', 'citrines', 'citterns', 'clannish', 'clarinet', 'clarions', 'clashers', 'claspers', 'classico', 'classier', 'classily', 'clastics', 'clatters', 'clattery', 'clayiest', 'clerical', 'cliental', 'clincher', 'clinches', 'clinical', 'clitoral', 'clitoric', 'clitoris', 'cloister', 'clothier', 'clysters', 'coachers', 'coaction', 'coactors', 'coalhole', 'coaliest', 'coalless', 'coalpits', 'coanchor', 'coarsely', 'coarsens', 'coarsest', 'coasters', 'coatless', 'cocaines', 'cochairs', 'cochlear', 'cochleas', 'cocinera', 'cocottes', 'coenacts', 'coercion', 'cohesion', 'cohoshes', 'cointers', 'coistrel', 'coistril', 'coitally', 'coitions', 'colessor', 'colicine', 'colicins', 'colinear', 'colistin', 'collapse', 'collaret', 'collates', 'collator', 'collects', 'colliers', 'colliery', 'collyria', 'colocate', 'colonels', 'colonial', 'colonics', 'colonies', 'colonise', 'colonist', 'colophon', 'colorant', 'colorers', 'colorist', 'colossal', 'colpitis', 'conation', 'conceals', 'conceits', 'concents', 'concepts', 'concerns', 'concerti', 'concerto', 'concerts', 'conchies', 'conciser', 'concocts', 'conepatl', 'conicity', 'coniines', 'conioses', 'coniosis', 'connects', 'connotes', 'consents', 'consoler', 'consoles', 'consorts', 'conspire', 'constant', 'contacts', 'contains', 'contents', 'contests', 'contorts', 'contract', 'contrail', 'contrary', 'contrast', 'contrite', 'controls', 'coolants', 'coolness', 'cooncans', 'coonties', 'cooption', 'coparent', 'copastor', 'copatron', 'copilots', 'coprince', 'copycats', 'copyists', 'coracles', 'corantos', 'cornetcy', 'cornices', 'corniche', 'cornicle', 'corniest', 'cornpone', 'corollas', 'coronach', 'coronals', 'coronary', 'coronate', 'coronels', 'coroners', 'coronets', 'corotate', 'corporal', 'corrects', 'corsairs', 'corsetry', 'corslets', 'cortical', 'cortices', 'cortisol', 'coscript', 'cosecant', 'costlier', 'costrels', 'cotenant', 'cotillon', 'cottiers', 'cranches', 'crannies', 'crashers', 'cratches', 'cratonic', 'creatins', 'creation', 'creators', 'creosols', 'cresylic', 'crinites', 'criollos', 'crispate', 'crispens', 'crispers', 'crispest', 'crispier', 'crispily', 'cristate', 'criteria', 'critical', 'critters', 'croceins', 'crochets', 'crocoite', 'crooners', 'cropless', 'crosiers', 'crosslet', 'crosstie', 'crotches', 'crotchet', 'cryolite', 'cryonics', 'cryostat', 'cryotron', 'crystals', 'cyanines', 'cyanites', 'cyanitic', 'cyanoses', 'cyanosis', 'cyanotic', 'cycasins', 'cyclases', 'cyclecar', 'cyclical', 'cyclists', 'cyclitol', 'cyclonal', 'cyclones', 'cyclonic', 'cycloses', 'cyclosis', 'cyprians', 'cysteins', 'cystines', 'cystitis', 'cytaster', 'cytosine', 'cytosols', 'earlship', 'earshots', 'earthily', 'eclipsis', 'ecliptic', 'eclosion', 'ecotonal', 'ecotypic', 'ecstatic', 'ectopias', 'ectosarc', 'elastics', 'elastins', 'elations', 'elicitor', 'elisions', 'elitists', 'ellipsis', 'elliptic', 'enactors', 'enactory', 'enations', 'enchains', 'enchants', 'enchoric', 'enclasps', 'enclitic', 'encroach', 'encrypts', 'encyclic', 'enscroll', 'ensnarls', 'entastic', 'enthalpy', 'enthrall', 'enthrals', 'entrails', 'entrains', 'entrants', 'entropic', 'eolithic', 'epically', 'epicotyl', 'epinasty', 'episcias', 'epistasy', 'epitasis', 'epsilons', 'erasions', 'eristics', 'erosions', 'erotical', 'errantly', 'erratics', 'erythron', 'escallop', 'escalops', 'escapist', 'eschalot', 'escolars', 'espartos', 'estriols', 'etchants', 'ethanols', 'ethicals', 'ethician', 'ethicist', 'ethinyls', 'ethnarch', 'ethnical', 'hairiest', 'hairless', 'hairline', 'hairnets', 'hairpins', 'halcyons', 'haltless', 'haplites', 'haplonts', 'haploses', 'haplosis', 'haptenic', 'harelips', 'haricots', 'harlotry', 'harpists', 'harpoons', 'harshens', 'harshest', 'harslets', 'hastiest', 'hatchels', 'hatchers', 'hatchery', 'hatchets', 'heartily', 'hectical', 'hecticly', 'heirship', 'heliasts', 'helicity', 'helicons', 'helicopt', 'heliport', 'helistop', 'hellcats', 'hellions', 'hencoops', 'heparins', 'hepatics', 'heptarch', 'heritors', 'heroical', 'herstory', 'hesitant', 'hierarch', 'hieratic', 'hilarity', 'hilliest', 'hilltops', 'hiltless', 'hiplines', 'hipsters', 'histones', 'historic', 'hitchers', 'hitherto', 'hoariest', 'hoarsely', 'hoarsens', 'hoarsest', 'hoisters', 'holiness', 'holistic', 'holotype', 'holstein', 'holsters', 'honestly', 'honorary', 'honorers', 'hoopless', 'hoopster', 'hootches', 'hootiest', 'hoplites', 'hoplitic', 'horniest', 'hornists', 'hornitos', 'hornless', 'horntail', 'horsecar', 'horsiest', 'hospices', 'hospital', 'hospitia', 'hostelry', 'hostiles', 'hostlers', 'hotchpot', 'hotlines', 'hotpress', 'hotshots', 'hyacinth', 'hyalines', 'hyalites', 'hyoscine', 'hyperons', 'hypnoses', 'hypnosis', 'hypnotic', 'hyponeas', 'hyponoia', 'hypothec', 'hysteria', 'hysteric', 'ichnites', 'ichthyic', 'iconical', 'icterics', 'illation', 'inaction', 'inarches', 'inceptor', 'inchoate', 'incisors', 'incisory', 'incitant', 'inciters', 'inclasps', 'incliner', 'inclines', 'incloser', 'incloses', 'incorpse', 'inearths', 'inerrant', 'inertial', 'inertias', 'inhalers', 'inherits', 'inhesion', 'inlayers', 'innately', 'innocent', 'inosites', 'inositol', 'insanely', 'insanest', 'insanity', 'inscapes', 'inscroll', 'insectan', 'insheath', 'inshrine', 'insister', 'insnarer', 'insnares', 'insolate', 'insolent', 'inspects', 'inspirer', 'inspires', 'installs', 'instance', 'instancy', 'instants', 'instates', 'instills', 'instinct', 'intently', 'interact', 'interior', 'interlap', 'interlay', 'internal', 'inthrall', 'inthrals', 'inthrone', 'intitles', 'intonate', 'intoners', 'intrants', 'intreats', 'intrench', 'introits', 'introrse', 'irenical', 'ironical', 'ironists', 'ironness', 'irritant', 'irritate', 'isatines', 'isochore', 'isochors', 'isochron', 'isocline', 'isocracy', 'isohyets', 'isolates', 'isolator', 'isolines', 'isopachs', 'isophote', 'isopleth', 'isospory', 'isotachs', 'isotones', 'isotonic', 'isotopes', 'isotopic', 'isotropy', 'isotypes', 'isotypic', 'itchiest', 'laciness', 'lacrosse', 'lactones', 'lactonic', 'lactoses', 'laicises', 'lanciers', 'lanoline', 'lanolins', 'lanosity', 'lanterns', 'lanthorn', 'latchets', 'latently', 'lathiest', 'latinity', 'latosols', 'latrines', 'latterly', 'lattices', 'lecithin', 'lections', 'lecythis', 'lenition', 'leprotic', 'leptonic', 'liaisons', 'licensor', 'lichenin', 'licorice', 'linchpin', 'linearly', 'lintiest', 'lintless', 'lioniser', 'lionises', 'lipocyte', 'litanies', 'literacy', 'literals', 'literary', 'literati', 'lithosol', 'littlish', 'littoral', 'loathers', 'localise', 'localist', 'localite', 'locality', 'locaters', 'location', 'locators', 'loessial', 'looniest', 'loophole', 'loopiest', 'loricate', 'loriners', 'lornness', 'lothario', 'loyalest', 'loyalist', 'lynchers', 'lynchpin', 'lyophile', 'lyricise', 'lyricist', 'nailsets', 'naphthol', 'naphthyl', 'naphtols', 'napoleon', 'narceins', 'narcissi', 'narcists', 'narcoses', 'narcosis', 'narcotic', 'nascency', 'nastiest', 'nathless', 'necropsy', 'necrosis', 'necrotic', 'neoliths', 'nephrons', 'nepotist', 'nicotine', 'nicotins', 'nictates', 'niellist', 'ninepins', 'ninnyish', 'nitchies', 'nitinols', 'nitrates', 'nitrator', 'nitriles', 'nitrites', 'nitrolic', 'nitrosyl', 'noisiest', 'nonactor', 'nonclass', 'noncolor', 'nonentry', 'nonionic', 'nonlocal', 'nonparty', 'nonpasts', 'nonplays', 'nonpoint', 'nonpolar', 'nonprint', 'nonroyal', 'nonsolar', 'nonstory', 'nonstyle', 'nontitle', 'nontonal', 'northern', 'northers', 'nostrils', 'notaries', 'notation', 'notchers', 'noticers', 'notional', 'notornis', 'nystatin', 'occasion', 'occipita', 'ocotillo', 'octanols', 'octarchy', 'octonary', 'octoroon', 'oestrins', 'oestriol', 'oilcloth', 'oilholes', 'oiliness', 'oilstone', 'olorosos', 'onanists', 'oophytes', 'oophytic', 'oospores', 'oosporic', 'oothecal', 'opalines', 'opencast', 'operants', 'operatic', 'operator', 'opinions', 'opsonins', 'optician', 'opticist', 'optional', 'oralists', 'orations', 'oratorio', 'oratress', 'orchises', 'orchitic', 'orchitis', 'orcinols', 'oriental', 'ornately', 'ornithes', 'ornithic', 'orphical', 'orphreys', 'orthicon', 'orthoepy', 'orthoses', 'orthosis', 'orthotic', 'ortolans', 'oscinine', 'oscitant', 'osteitic', 'osteitis', 'ostinato', 'ostiolar', 'ostioles', 'ostracon', 'otiosely', 'otiosity', 'otocysts', 'otoliths', 'otoscope', 'otoscopy', 'pachisis', 'pactions', 'painches', 'painless', 'painters', 'paintier', 'paisleys', 'paleosol', 'paletots', 'palliest', 'paltrier', 'paltrily', 'panelist', 'panicles', 'panniers', 'panoches', 'pantheon', 'panthers', 'pantiles', 'pantries', 'parchesi', 'parchisi', 'paretics', 'parhelic', 'parishes', 'parities', 'parritch', 'parsleys', 'parsonic', 'particle', 'partiers', 'partlets', 'partners', 'partyers', 'pasterns', 'pasticci', 'pastiche', 'pastiest', 'pastille', 'pastries', 'patchers', 'patchier', 'patchily', 'patently', 'patentor', 'pathetic', 'pathless', 'pathoses', 'patients', 'patriots', 'patronly', 'patroons', 'patterns', 'payrolls', 'peccancy', 'pecorini', 'pecorino', 'pectoral', 'pelicans', 'pelorian', 'pelorias', 'peltasts', 'penality', 'penchant', 'penicils', 'pennants', 'pensions', 'pentanol', 'pentarch', 'pentosan', 'perianth', 'perillas', 'periotic', 'perisarc', 'perlitic', 'persalts', 'personal', 'personas', 'pertains', 'petiolar', 'petition', 'petrolic', 'petrosal', 'peytrals', 'phaetons', 'phallist', 'pharoses', 'phelonia', 'phenolic', 'phenylic', 'philters', 'philtres', 'phonates', 'phonetic', 'phoniest', 'phorates', 'photonic', 'photoset', 'phratric', 'phreatic', 'phthalic', 'phthalin', 'phthises', 'phthisic', 'phthisis', 'phylesis', 'phyletic', 'phyllite', 'physical', 'phytanes', 'phytonic', 'pianists', 'piasters', 'piastres', 'picachos', 'picaroon', 'piccolos', 'picoline', 'picolins', 'picrates', 'picrites', 'pierrots', 'pietists', 'pilaster', 'pillions', 'pilosity', 'pilsners', 'pinaster', 'pinchers', 'pinholes', 'pinitols', 'pinnaces', 'pinnacle', 'pinochle', 'pinocles', 'pinscher', 'pintails', 'pintanos', 'piracies', 'piscator', 'piscinae', 'piscinal', 'piscinas', 'pisolite', 'pistache', 'pistoles', 'pitchers', 'pitchier', 'pitchily', 'pithiest', 'pithless', 'pitiless', 'pittance', 'plainest', 'plaister', 'plaiters', 'planches', 'planchet', 'planless', 'planners', 'planosol', 'planters', 'plantlet', 'plashers', 'plashier', 'plasters', 'plastery', 'plastics', 'plastron', 'platiest', 'platinic', 'platonic', 'platoons', 'platters', 'playless', 'playlets', 'playlist', 'plectron', 'plenists', 'plethora', 'pliantly', 'pliotron', 'plosions', 'plotless', 'plotline', 'plotters', 'plottier', 'plotties', 'poachers', 'poachier', 'pocosins', 'poetical', 'pointers', 'pointier', 'poisoner', 'poitrels', 'polarise', 'polarity', 'polarons', 'polecats', 'polentas', 'polestar', 'policies', 'polisher', 'polishes', 'politely', 'politest', 'politico', 'politics', 'polities', 'pollices', 'pollinia', 'pollinic', 'pollists', 'pollster', 'poloists', 'poltroon', 'polycots', 'polyenic', 'pontoons', 'ponytail', 'poorness', 'poortith', 'porniest', 'porosity', 'portance', 'portents', 'porthole', 'porticos', 'portions', 'portless', 'portlier', 'portrait', 'portrays', 'portress', 'position', 'positron', 'postally', 'posterns', 'postheat', 'posthole', 'postiche', 'postoral', 'postrace', 'postriot', 'postsync', 'potashes', 'potassic', 'potation', 'potatoes', 'potatory', 'potently', 'potholes', 'potiches', 'potlache', 'potlatch', 'potlines', 'potshots', 'potstone', 'practice', 'practise', 'praetors', 'prairies', 'praisers', 'pralines', 'prancers', 'prattler', 'prattles', 'preallot', 'precasts', 'prechill', 'precinct', 'precools', 'precrash', 'prelatic', 'presorts', 'pretrain', 'pretrial', 'prettily', 'priciest', 'priestly', 'princely', 'princess', 'printers', 'printery', 'priorate', 'prioress', 'priories', 'priority', 'prisoner', 'prissier', 'prissily', 'pristane', 'pristine', 'procaine', 'prochain', 'prochein', 'proctors', 'prolines', 'pronates', 'pronator', 'prorates', 'prosaist', 'prosects', 'prosiest', 'prostate', 'prosties', 'prostyle', 'protases', 'protasis', 'protatic', 'proteans', 'protects', 'proteins', 'protests', 'protists', 'protocol', 'protonic', 'protract', 'protyles', 'psalters', 'psaltery', 'pschents', 'psilocin', 'psilotic', 'psoralen', 'psychics', 'ptyalins', 'pycnoses', 'pycnosis', 'pycnotic', 'pyelitic', 'pyelitis', 'pyorrhea', 'pyranose', 'pyronine', 'pyrostat', 'pyrrhics', 'pyrroles', 'pyrrolic', 'pythonic', 'raccoons', 'rachises', 'rachitic', 'rachitis', 'raciness', 'raillery', 'rainiest', 'rainless', 'raisonne', 'ralliers', 'rallyist', 'ranchero', 'ranchers', 'raptness', 'rarities', 'raspiest', 'ratchets', 'ratholes', 'ratlines', 'ratooner', 'rattlers', 'rattoons', 'reaction', 'reactors', 'realists', 'reallots', 'reanoint', 'reassort', 'recharts', 'recision', 'recitals', 'reclasps', 'recolors', 'rectally', 'relation', 'relators', 'repaints', 'replants', 'replicas', 'replicon', 'repolish', 'reposals', 'reposits', 'reprints', 'reprisal', 'reproach', 'reptilia', 'reschool', 'rescript', 'reshoots', 'resistor', 'resonant', 'resorcin', 'resplits', 'responsa', 'resprays', 'restarts', 'restitch', 'restoral', 'restrain', 'restrict', 'retailor', 'retinals', 'retinols', 'retirant', 'retracts', 'retrains', 'retrally', 'retrials', 'retroact', 'retsinas', 'rheophil', 'rheostat', 'rhetoric', 'rhonchal', 'rhyolite', 'richness', 'ricochet', 'ricottas', 'ripienos', 'ripostes', 'risottos', 'roasters', 'rocaille', 'roiliest', 'roisters', 'roosters', 'rootiest', 'rootless', 'rootlets', 'ropiness', 'rosaries', 'roseolar', 'roseolas', 'roseroot', 'rosinols', 'rosolios', 'rostella', 'rostrate', 'rotaries', 'rotation', 'rotators', 'rotatory', 'rototill', 'rottenly', 'royalist', 'roysters', 'sacristy', 'sailorly', 'salicine', 'salicins', 'saliency', 'salients', 'salinity', 'salliers', 'salterns', 'saltiers', 'saltiest', 'saltines', 'saltires', 'sanction', 'sanctity', 'sanicles', 'sanities', 'sanitise', 'santonin', 'sapiency', 'saponine', 'saponins', 'saponite', 'sartorii', 'satchels', 'satinets', 'satirise', 'satirist', 'scaliest', 'scallion', 'scallops', 'scalpels', 'scalpers', 'scanners', 'scansion', 'scantest', 'scantier', 'scanties', 'scantily', 'scarcely', 'scarcest', 'scarcity', 'scariest', 'scariose', 'scarlets', 'scarpers', 'scatters', 'scattier', 'scenario', 'scenical', 'sceptics', 'sceptral', 'schiller', 'scholars', 'schooner', 'sciatics', 'scilicet', 'sciolist', 'scirocco', 'scolices', 'scollops', 'scoopers', 'scooters', 'scorcher', 'scorches', 'scorners', 'scorpion', 'scotches', 'scotopia', 'scotopic', 'scotties', 'scraichs', 'scrannel', 'scrapers', 'scrapies', 'scratchy', 'scripter', 'scrootch', 'scyphate', 'seaports', 'secantly', 'sections', 'sectoral', 'senators', 'senhoras', 'senility', 'senopias', 'senorita', 'sensilla', 'sensoria', 'septical', 'seraphic', 'seraphin', 'serially', 'sericins', 'serosity', 'serranos', 'settlors', 'shaliest', 'shalloon', 'shallops', 'shallots', 'shannies', 'shanteys', 'shanties', 'shantihs', 'sharpens', 'sharpers', 'sharpest', 'sharpies', 'shatters', 'sheitans', 'shellacs', 'sheroots', 'shiniest', 'shinnery', 'shinneys', 'shinnies', 'shirtier', 'shittahs', 'shittier', 'shoalest', 'shoalier', 'shoehorn', 'shoepacs', 'shooters', 'shophars', 'shortens', 'shortest', 'shortias', 'shorties', 'shortish', 'shrapnel', 'shriller', 'silently', 'silicate', 'silicles', 'silicone', 'silicons', 'silliest', 'siltiest', 'sinister', 'sinopias', 'siphonal', 'siphonic', 'sirenian', 'sirloins', 'siroccos', 'sisterly', 'sitarist', 'slatches', 'slathers', 'slatiest', 'slattern', 'slipcase', 'slipsole', 'slithers', 'slithery', 'slitters', 'sloshier', 'snapshot', 'snarlers', 'snarlier', 'snatcher', 'snatches', 'snitcher', 'snitches', 'snoopers', 'snoopier', 'snoopily', 'snootier', 'snootily', 'snorters', 'snottier', 'snottily', 'soapiest', 'socially', 'societal', 'solacers', 'solanine', 'solanins', 'solarise', 'solation', 'solecist', 'solicits', 'solitary', 'solitons', 'solonets', 'solstice', 'sonances', 'sonantic', 'sonatine', 'sonicate', 'sonorant', 'sonority', 'soothers', 'soothest', 'soothsay', 'sootiest', 'sopranos', 'soricine', 'soroches', 'sororate', 'sorority', 'sorption', 'sorriest', 'spaciest', 'spallers', 'spancels', 'spaniels', 'spanners', 'sparsely', 'sparsity', 'spathose', 'spatters', 'specials', 'spectral', 'spherics', 'spiccato', 'spiciest', 'spillers', 'spinachy', 'spinally', 'spiniest', 'spinners', 'spinnery', 'spinneys', 'spinnies', 'spinster', 'spiracle', 'spirally', 'spirants', 'spiriest', 'spirilla', 'spitters', 'spittles', 'spittoon', 'splasher', 'splatter', 'splenial', 'splicers', 'splinter', 'splitter', 'splotchy', 'spoilers', 'spoliate', 'sponsion', 'spontoon', 'spooneys', 'spoonier', 'spoonies', 'spoonily', 'sporrans', 'sporters', 'sportier', 'sportily', 'spotters', 'spottier', 'spottily', 'sprattle', 'sprayers', 'sprinter', 'stainers', 'staithes', 'stallion', 'stancher', 'stanches', 'stanchly', 'stanhope', 'stanines', 'stannite', 'staplers', 'starches', 'starlets', 'starnose', 'starship', 'starters', 'startler', 'startles', 'statices', 'stations', 'stealths', 'stealthy', 'steapsin', 'stearins', 'stencils', 'stenotic', 'stentors', 'sterical', 'sternson', 'stertors', 'sthenias', 'stiction', 'stillest', 'stillier', 'stinters', 'stipites', 'stitcher', 'stitches', 'stithies', 'stollens', 'stolonic', 'stolport', 'stoniest', 'stoolies', 'stoopers', 'strainer', 'straiten', 'straiter', 'straitly', 'strayers', 'stretchy', 'striates', 'stricter', 'strictly', 'stripers', 'stripier', 'stroller', 'strontia', 'strontic', 'strophes', 'strophic', 'stroyers', 'styliser', 'stylites', 'stylitic', 'styptics', 'syenitic', 'sylphish', 'synanons', 'synaptic', 'syncarps', 'synchros', 'syncline', 'syncopal', 'syncopes', 'syncopic', 'synectic', 'synoptic', 'syntonic', 'syphilis', 'syrphian', 'systolic', 'tachiste', 'tachists', 'tachyons', 'taconite', 'tactions', 'tactless', 'tailless', 'tailspin', 'talipots', 'talliers', 'tallness', 'tallyhos', 'tanistry', 'tapestry', 'tapholes', 'taproots', 'tapsters', 'tarriest', 'tarsiers', 'tartness', 'teashops', 'teaspoon', 'technics', 'tectonic', 'telsonic', 'tenacity', 'tenantry', 'teniasis', 'tennists', 'tenorist', 'tensions', 'teocalli', 'ternions', 'terpinol', 'terrains', 'terrapin', 'tertials', 'tertians', 'tertiary', 'testoons', 'tetanics', 'tetchily', 'tetrarch', 'thatcher', 'thatches', 'thearchy', 'theatric', 'theistic', 'thelitis', 'theocrat', 'theorist', 'theriacs', 'thespian', 'thetical', 'thinners', 'thinness', 'thinnest', 'thinnish', 'thionate', 'thionine', 'thionins', 'thionyls', 'thiophen', 'thiotepa', 'thirster', 'thirties', 'thistles', 'tholepin', 'thoraces', 'thoracic', 'thorites', 'thornier', 'thornily', 'thrasher', 'thrashes', 'thriller', 'throstle', 'tieclasp', 'tillites', 'tinhorns', 'tininess', 'tinniest', 'tinplate', 'tinselly', 'tinstone', 'tintless', 'tintypes', 'tipcarts', 'tipsiest', 'tipsters', 'titaness', 'tithonia', 'toasters', 'toastier', 'toenails', 'toiletry', 'tolerant', 'tonality', 'tonetics', 'tonicity', 'tonishly', 'tonsilar', 'tontines', 'toolless', 'toothier', 'toothily', 'tootlers', 'tootsies', 'topcoats', 'topcross', 'toplines', 'topnotch', 'topsails', 'topsoils', 'topstone', 'torchier', 'torchons', 'tornillo', 'torosity', 'torrents', 'torsions', 'tortilla', 'tortoise', 'tortonis', 'totalise', 'toyshops', 'trachles', 'trachyte', 'tractile', 'traction', 'tractors', 'trailers', 'trainers', 'traipses', 'traitors', 'tranches', 'transect', 'transept', 'tranship', 'transits', 'trapline', 'trapnest', 'trashier', 'trashily', 'treasons', 'trenails', 'triarchy', 'trichina', 'trichite', 'tricolor', 'tricorne', 'tricorns', 'trictrac', 'tricycle', 'triennia', 'triethyl', 'trillers', 'trillion', 'triolets', 'triphase', 'triplane', 'triplets', 'triplite', 'tripolis', 'triposes', 'triptane', 'triptyca', 'triptych', 'trisects', 'tristich', 'tritones', 'trochaic', 'trochars', 'trochili', 'trochils', 'trochlea', 'troilite', 'trollers', 'trolleys', 'trollies', 'trollops', 'trollopy', 'troopers', 'troopial', 'trophies', 'tropical', 'tropines', 'troponin', 'trotline', 'trypsins', 'trysails', 'trysters', 'tylosins', 'typecast', 'typhonic', 'typhoons', 'tyrannic', 'tyrosine', 'yachters']),
]




def ask_wordplayer(process,case):
    process.stdin.write(case+'\n')
    process.stdin.flush()
    words = []
    while True:
        res=process.stdout.readline()
        if res=='.\n':
            break
        else:
            words.append(res.strip())
    return words

def wordplayer_tester(program_name,word_list_name,Tests):
        args = ['python'] if program_name.endswith('py') else []
        args += [program_name,word_list_name]
        popen_specs={'stdout':PIPE,'stdin':PIPE,'universal_newlines':True}

        process = Popen(args,**popen_specs)
        time.sleep(0.02)
        return_code = process.poll()
        if return_code:
            return False,'Your program exited with return code {}.'.format(return_code)

        res = ""
        for case,answer in Tests:
                words = ask_wordplayer(process,case)
                if words != answer:
                    res += "Case {}: correct: {}, yours: {}\n".format(case,answer,words)
        if res:
            return False, res

        (stdout, stderr) = process.communicate('stopthisprogramrightnowplease 0\n',timeout=1)
        if stdout != "":
            return False, "Responding to exit signal"
        elif stderr != None:
            return False, "Extra output to stderr."

        return True,"all tests passed"

       
def test_speed(program_name,faster_than_server,fh):
        testtype = 'py' if program_name.endswith('py') else "cpp"
        args = ['python'] if program_name.endswith('py') else []
        args += [program_name,'big_wordlist.txt']
        popen_specs={'stdout':PIPE,'stdin':PIPE,'universal_newlines':True}

        process = Popen(args,**popen_specs)


        time.sleep(0.02)
        if process.poll():
            return {}

        time.sleep(2 / faster_than_server)
        speed_factor=[]
        for target_time, case, answer in Tests_Speed:
                start_time=time.time()
                words = ask_wordplayer(process,case)
                duration = (time.time()-start_time) * faster_than_server
                speed_factor.append((case,duration/target_time[testtype]))
                if words != answer:
                    return {}

        print('Speed test results',file=fh)
        print('==================',file=fh)
        print('Time Ratio    Case',file=fh)
        print('----------    ----',file=fh)
        for test,speed in speed_factor:
            print("{:>10.3f}".format(speed),test,file=fh)

        scores = tuple(x[1] for x in speed_factor)
        try:
                (stdout, stderr) = process.communicate('stopthisprogramrightnowplease 0\n',timeout=1)
        except:
            return {}

        return sorted(scores)





def main_python(program_to_run,original_name,faster_than_server,save=False):

    fh = StringIO() if save else sys.stdout

    print('Checking {} for EC602 submission.\n'.format(original_name),file=fh)

    Grade={'specs':0,'style':0,'elegance':0,'efficiency':0}

    the_program = ec602lib.read_file(program_to_run)
    authors = ec602lib.get_authors(the_program, 'py')
    imported = ec602lib.get_python_imports(the_program)

 
    passed_short, short_report = wordplayer_tester(program_to_run,'short_wordlist.txt',Tests_Short)
    if not passed_short:
        print(short_report,file=fh)
    passed_big, big_report = wordplayer_tester(program_to_run,'big_wordlist.txt',Tests_Big)
    if not passed_big:
        print(big_report,file=fh)
    
    if not passed_big or not passed_short:
        if save:
            return Grade,fh.getvalue()
        return

    pep8_errors,pep8_report = ec602lib.pep8_check(program_to_run)

    pylint_score,pylint_report = ec602lib.pylint_check(program_to_run)
    

    code_metrics = ec602lib.code_analysis_py(the_program)

    complexity = code_metrics['lines']+code_metrics['words'] + 20*code_metrics['words']/code_metrics['lines']
    rel_times = test_speed(program_to_run,faster_than_server,fh)

    eff_grade = 0
    for ratio,scale in zip(rel_times,[0.5,0.2,0.1,0.05,0.05,0.05,0.05]):
        eff_grade += scale / ratio

    Grade['specs']=3
    Grade['style']=max(0,(10-pep8_errors)/20) + pylint_score/20

    Grade['elegance'] = min(1.5,300/complexity) # 0.5 bonus point possible
    Grade['efficiency'] = min(2.0,eff_grade) # 1.0 bonus point possible

    print('---- analysis of your code structure ----\n',file=fh)

    print('authors          : {}'.format(" ".join(authors)
                                               if authors else ec602lib.AUTHWARN),file=fh)


    print('imported modules : {}'.format(" ".join(imported)),file=fh)
    print(ec602lib.code_size_report(code_metrics, {'lines': 49, 'words': 159}),file=fh)


    print('pep8 check       : {} problems.'.format(pep8_errors),file=fh)
    if pep8_errors:
        print('pep8 report',file=fh)
        print(pep8_report,file=fh)

    print('pylint score     : {}/10'.format(pylint_score),file=fh)
    print(file=fh)
    print('---- grading ----\n',file=fh)

    print('grades           :',Grade,file=fh)
    print('grade total      : {:.2f} / 6'.format(sum(Grade[x] for x in Grade)),file=fh)

    if save:
        res = fh.getvalue()
        return Grade, res
  




def main_cpp(source_file,program_to_run,original_name,faster_than_server=1,save=False):
    Grade={'specs':0,'style':0,'elegance':0,'efficiency':0}

    the_program = ec602lib.read_file(source_file)
    authors = ec602lib.get_authors(the_program, 'cpp')
    included = ec602lib.get_includes(the_program)
    

    fh = StringIO() if save else sys.stdout

    #run the specification tests

    passed_short, short_report = wordplayer_tester(program_to_run,'short_wordlist.txt',Tests_Short)
    if not passed_short:
        print(short_report,file=fh)
    passed_big, big_report = wordplayer_tester(program_to_run,'big_wordlist.txt',Tests_Big)
    if not passed_big:
        print(big_report,file=fh)
    
    if not passed_big or not passed_short:
        if save:
            return Grade,fh.getvalue()
        return


    
    code_metrics = ec602lib.code_analysis_cpp(source_file)
    
    if code_metrics['astyle']=="error":
        print('astyle is reporting a problem.',file=fh)
        code_metrics['astyle']=0

    D = code_metrics['errors']
    cpplint_count= sum(len(D[x]) for x in D)
    

    complexity = code_metrics['lines']+code_metrics['words'] + 20*code_metrics['words']/code_metrics['lines']

    rel_times= test_speed(program_to_run,faster_than_server,fh)

    eff_grade = 0
    for ratio,scale in zip(rel_times,[0.5,0.2,0.1,0.05,0.05,0.05,0.05]):
        eff_grade += scale / ratio

    Grade['specs']=3


    Grade['style'] = max(0,(10-cpplint_count)/20) + code_metrics['astyle']/2.0

    Grade['elegance'] = min(1.5,500/complexity) # 0.5 bonus point possible
    Grade['efficiency'] = min(2.0,eff_grade) # 1.0 bonus point possible


    print('Checking {} for EC602 submission.\n'.format(original_name),file=fh)
    print('---- analysis of your code structure ----\n',file=fh)

    print('authors          : {}'.format(" ".join(authors)
                                               if authors else ec602lib.AUTHWARN),file=fh)


    print('included libs    : {}'.format(" ".join(included)),file=fh)
    print(ec602lib.code_size_report(code_metrics, {'lines': 91, 'words': 332}),file=fh)



    print("cpplint          : {}".format("{} problems".format(cpplint_count) if cpplint_count else "ok"),file=fh)
    for e in code_metrics['errors']:
        for x in code_metrics['errors'][e][:3]:
            print('line {} ({}): {}'.format(*x),file=fh)
    print("astyle           : {:.1%} code unchanged.\n".format(code_metrics['astyle']),file=fh)

    print('---- grading ----\n',file=fh)

    print('grades           :',Grade,file=fh)
    print('grade total      : {:.2f} / 6'.format(sum(Grade[x] for x in Grade)),file=fh)

    if save:
        return Grade,fh.getvalue()

 
def pyshell(Parms,q):
      vals = main_python(**Parms)
      q.put(vals)

def cppshell(Parms,q):
      vals = main_cpp(**Parms)
      q.put(vals)


if __name__ == '__main__':
    #PD = {}
    #PD = {'source':"wordplayer.py",'program':'wordplayer.py','original':"wordplayer.py"}
    PD = {'source':"wordplayer.cpp",'program':'wordplayer','original':'wordplayer.cpp'}

    testing = 'py' if PD['source'].endswith('py') else 'cpp'

    DEBUG = True


    if not PD:
        print('please edit this file and set the value of PD to choose py or cpp to check')
        exit()

    # if C++, compile (equalizes for optimization code)
    if testing == 'cpp':
        T = run(['g++', "-std=c++14", "-O3", PD['source'], "-o", PD['program']])

        if T.returncode:
            print(T)
            quit()


    FilesNeeded = ['short_wordlist.txt','big_wordlist.txt']

    Dir=os.listdir('.')
    for fneeded in FilesNeeded:
        if fneeded not in Dir:
            print('getting',fneeded,'from server')
            req = 'http://128.197.128.215:60217/static/content/'+fneeded
            with urllib.request.urlopen(req) as f:
               p = f.read().decode('utf-8')
               g = open(fneeded,'w')
               g.write(p)
               g.close()
    
    st = time.time()
    D = {}
    for k in range(10000):
        D[k] = random.randint(1,100)
    en = time.time()

    # server's measured time on this task is 20 ms.

    faster_than_server = 0.020 / (en -st)
    
    if DEBUG:
        print('your computer is {:.2%} of the speed of the server'.format(faster_than_server))

 

    if testing=='cpp':
        main_cpp(PD['source'],PD['program'],PD['original'],faster_than_server)
    else:
        main_python(PD['source'],PD['original'],faster_than_server)

    




