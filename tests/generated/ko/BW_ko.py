geoid_list = [933000, 933018, 933088, 933099, 933141, 933182, 933271, 933305, 933331, 933340, 933366, 933471, 933521, 933535, 933685, 933719, 933773, 933778]
name_list = ["Tonota", "Thamaga", "세로웨", "셀레비피퀘", "Ramotswa", "Palapye", "Mosopa", "몰레폴롤레", "Mogoditshane", "모추디", "마운", "마할라피에", "로바체", "Letlhakane", "카니에", "Janeng", "가보로네", "프랜시스타운"]
ascii_name_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
alternate_names_list = [["Tonota", "Tonoto"], ["Thamaga"], ["Serooue", "Serova", "Serove", "Serovė", "Serowe", "sai luo wei", "selowe", "seroue", "srwbh", "srwwh  bwtswana", "Σερόουε", "Серова", "Серове", "סרובה", "سرووه، بوتسوانا", "セロウェ", "塞罗韦", "세로웨"], ["PKW", "Phikwe", "Pikwe", "Pikwe-Selibe", "Selebi", "Selebi Pikve", "Selebi Pikvė", "Selebi Pikwe", "Selebi-Phikwe", "Selebi-Pikwe", "Selebi-Pkhikve", "Selempi-Fikoue", "Selibe", "Selibe Phikwe", "Selibe-Phikwe", "Selibe-Pikwe Mine Lease Area", "sai lai bi-pi kui", "sellebipikwe", "slyb fykwh  bwtswana", "Σελέμπι-Φίκουε", "Селеби-Пхикве", "Селебі-Пхікве", "سلیب فیکوه، بوتسوانا", "سیلیبی-فیکوے", "セレビ・ピクウェ", "塞莱比-皮奎", "셀레비피퀘"], ["Ramotswa", "Ramoutsa"], ["Palap'e", "Palapaye Road", "Palape", "Palapie", "Palapye", "Palapye Road", "Palatswe", "QPH", "pa la pei", "palapy  bwtswana", "Παλάπιε", "Палапье", "Палапє", "پالاپی، بوتسوانا", "帕拉佩"], ["Moshupa", "Mosopa"], ["Molepolole", "Molepololė", "mo lai bo luo lai", "mollepollolle", "moreporore", "mwlpwlwlh", "mwlpwlwlh  bwtswana", "Μολεπολόλε", "Молепололе", "מולפולולה", "مولپولوله، بوتسوانا", "モレポロレ", "莫萊波洛萊", "몰레폴롤레"], ["Mogoditsane", "Mogoditshane"], ["Mochudi", "Mochudi Village", "Mocudis", "Motsounti", "Močudis", "mo qiu di", "mochudi", "mwchwdy  bwtswana", "Μοτσούντι", "Мочуди", "Мочуді", "موچودی، بوتسوانا", "モチュディ", "莫丘迪", "모추디"], ["MUB", "Maoun", "Maun", "Maunas", "ma weng", "maun", "mawn  bwtswana", "Μαούν", "Маун", "Маўн", "מאון", "ماون، بوتسوانا", "マウン", "馬翁", "마운"], ["Mahalapje", "Mahalapjė", "Mahalapye", "Mahalatswe", "Makhalap'e", "Makhalape", "ma ha la pei", "mahalapyh  bwtswana", "mahallapie", "maharapie", "Махалапе", "Махалапье", "ماهالاپیه، بوتسوانا", "マハラピエ", "馬哈拉佩", "마할라피에"], ["LOQ", "Lobace", "Lobatse", "Lobatsi", "Lompatse", "lobache", "luo ba ce", "lwbats  bwtswana", "robatsue", "Λομπάτσε", "Лобаце", "لوباتس، بوتسوانا", "لوباٹسے", "ロバツェ", "洛巴策", "로바체"], ["Lethakane", "Letlhakane", "Letlhakawe"], ["Kan'e", "Kane", "Kanie", "Kanje", "Kanjė", "Kanye", "ka nei", "kanie", "kanyh  bwtswana", "qnyh", "Κάνιε", "Кане", "Канье", "Каньє", "Кање", "קניה", "کانیه، بوتسوانا", "カニエ", "卡內", "카니에"], ["Janeng"], ["GBE", "Gabaroneh", "Gaberones", "Gaberones Village", "Gaberono", "Gaboron", "Gaboronas", "Gaborone", "Gaboròn", "Gaboróne", "IGaborone", "Nkamporone", "Qaborone", "gabolone", "gaborone", "gaboroni", "gabwrwn", "gbrwn", "gebaroni", "goborni", "haborone", "jabwrwn", "jia bai long li", "jia bo long li", "ka bo rone", "kaparoni", "Γκαμπορόνε", "Габаронэ", "Габороне", "Գաբորոնե", "גאבאראן", "גאבורון", "جابورون", "گابورون", "گابۆرۆن", "گبرون", "गॅबारोनी", "गोबोर्नी", "ਗਾਬੋਰੋਨੀ", "காபரோனி", "กาโบโรเน", "ག་བོ་རོ་ནི།", "გაბორონე", "ጋበሮኔ", "ጋቦሮን", "ハボローネ", "嘉柏隆里", "嘉波隆里", "가보로네"], ["FRW", "Francistown", "Fransistaoun", "Fransistaun", "Frensistaun", "Frensistaunas", "fransystwwn  bwtswana", "fu lang xi si dui", "furanshisutaun", "peulaensiseutaun", "Φράνσισταουν", "Франсистаун", "Франсістаўн", "פרנסיסטאון", "فرانسس ٹاؤن", "فرانسیستوون، بوتسوانا", "แฟรนซิสทาวน์", "フランシスタウン", "弗朗西斯敦", "프랜시스타운"]]
latitude_list = [-21.44236, -24.67014, -22.38754, -21.97895, -24.87158, -22.54605, -24.7718, -24.40659, -24.62694, -24.41667, -19.98333, -23.10407, -25.22435, -21.41494, -24.96675, -25.41667, -24.65451, -21.17]
longitude_list = [27.46153, 25.53975, 26.71077, 27.84296, 25.86989, 27.12507, 25.42156, 25.49508, 25.86556, 26.15, 23.41667, 26.81421, 25.67728, 25.59263, 25.33273, 25.55, 25.90859, 27.50778]
country_code_list = ["BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW", "BW"]
population_list = [17759, 20756, 47419, 42488, 21450, 30650, 19561, 63248, 43394, 36962, 49945, 41316, 30883, 18136, 44716, 16853, 208411, 89979]
dem_list = [959, 1073, 1147, 870, 1039, 926, 1136, 1146, 1026, 952, 947, 1025, 1191, 984, 1406, 1311, 1011, 989]
timezone_list = [22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22]
altitude_list = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
_feature_class_list = ["P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P"]
_feature_code_list = ["PPL", "PPL", "PPLA", "PPL", "PPLA", "PPL", "PPL", "PPLA", "PPL", "PPLA", "PPLA", "PPL", "PPL", "PPL", "PPLA", "PPL", "PPLC", "PPLA"]
_parent_code_list = ["BW.01", "BW.06", "BW.01", "BW.17", "BW.09", "BW.01", "BW.10", "BW.06", "BW.06", "BW.05", "BW.11", "BW.01", "BW.16", "BW.01", "BW.10", "BW.09", "BW.14", "BW.13"]
_states = {"BW.10": ["Ngwaketsi", "Ngwaketsi", 933043], "BW.09": ["South-East", "South-East", 933044], "BW.08": ["North-East", "North-East", 933210], "BW.11": ["North-West", "North-West", 933230], "BW.06": ["Kweneng", "Kweneng", 933562], "BW.05": ["Kgatleng", "Kgatleng", 933654], "BW.04": ["Kgalagadi", "Kgalagadi", 933657], "BW.03": ["Ghanzi", "Ghanzi", 933758], "BW.12": ["Chobe", "Chobe", 933840], "BW.01": ["Central", "Central", 933851], "BW.13": ["City of Francistown", "City of Francistown", 11778168], "BW.14": ["Gaborone", "Gaborone", 11778169], "BW.15": ["Jwaneng", "Jwaneng", 11778170], "BW.16": ["Lobatse", "Lobatse", 11778171], "BW.17": ["Selibe Phikwe", "Selibe Phikwe", 11778172], "BW.18": ["Sowa Town", "Sowa Town", 11778173]}
_districts = {"BW.09.7670702": ["Gaborone", "Gaborone", 7670702], "BW.05.7670705": ["Kgatleng", "Kgatleng", 7670705], "BW.01.7670706": ["Mahalapye", "Mahalapye", 7670706], "BW.01.7670708": ["Machaneng", "Machaneng", 7670708], "BW.01.7670709": ["Serowe", "Serowe", 7670709], "BW.01.7670710": ["Palapye", "Palapye", 7670710], "BW.01.11819282": ["Tutume", "Tutume", 11819282], "BW.04.11819283": ["Tshabong", "Tshabong", 11819283], "BW.11.11819284": ["Ngamiland East", "Ngamiland East", 11819284], "BW.12.11819285": ["Chobe", "Chobe", 11819285], "BW.04.11819286": ["Gemsbok", "Gemsbok", 11819286], "BW.09.11819287": ["South East", "South East", 11819287], "BW.10.11819288": ["Barolong", "Barolong", 11819288], "BW.10.11819289": ["Ngwaketse Central", "Ngwaketse Central", 11819289], "BW.04.11819290": ["Hukunsti", "Hukunsti", 11819290], "BW.01.11819291": ["Bobonong", "Bobonong", 11819291], "BW.10.11819292": ["Ngwaketse South", "Ngwaketse South", 11819292], "BW.06.11819293": ["Kweneng North", "Kweneng North", 11819293], "BW.01.11819294": ["Tuli", "Tuli", 11819294], "BW.01.11819295": ["Lethlakane", "Lethlakane", 11819295], "BW.11.11819296": ["Ngamiland West", "Ngamiland West", 11819296], "BW.10.11819297": ["Ngwaketse North", "Ngwaketse North", 11819297], "BW.06.11819298": ["Kweneng South", "Kweneng South", 11819298], "BW.08.11819299": ["Masungu", "Masungu", 11819299], "BW.03.11819300": ["Ghanzi", "Ghanzi", 11819300]}