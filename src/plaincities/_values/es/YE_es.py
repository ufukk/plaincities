geoid_list = [69426, 69500, 69559, 70225, 70979, 71137, 71273, 71334, 72968, 73560, 74477, 75337, 76154, 76184, 76991, 77408, 77726, 78428, 78754, 79415, 79455, 79836, 415189]
name_list = ["Zinjibār", "Zabīd", "Yarīm", "Taiz", "Sayyān", "Sanaá", "Saḩar", "Sa'dah", "Ma'rib", "Laḩij", "Ibb", "Ḩajjah", "Dhī as Sufāl", "Dhamār", "Bayt al Faqīh", "Bājil", "Ataq", "‘Amrān", "Mukalla", "Al Ḩudaydah", "Al Ḩazm", "Al Bayda", "Adén"]
ascii_name_list = ["Zinjibar", "Zabid", "Yarim", 0, "Sayyan", "Sanaa", "Sahar", 0, 0, "Lahij", 0, "Hajjah", "Dhi as Sufal", "Dhamar", "Bayt al Faqih", "Bajil", 0, "'Amran", 0, "Al Hudaydah", "Al Hazm", 0, "Aden"]
alternate_names_list = [["Az Zanjabar", "Az Zanjabār", "Zanjibar", "Zinjibar", "Zinjibār", "Zmjibar", "znjbar", "زنجبار"], ["Zabid", "Zabīd", "Zebid", "zbyd", "Забид", "زبيد"], ["Jarim", "Yarim", "Yarīm", "Yerim", "yrym", "Ярим", "يريم"], ["TAI", "Ta'izz", "Ta`izz", "Taiz", "Taizz", "Ta‘izz", "tʿz", "Таиз", "تعز"], ["Saiyan", "Saiyān", "Sayyan", "Sayyān", "Seijan", "Seijân", "Sian", "Siryan", "Siryān", "syan", "سيان"], ["SAH", "Sano", "San'ah", "San`a'", "Sana", "Sana'a", "Sana'a'", "Sanaa", "Sanao", "Sanaà", "Sanaá", "San’ah", "sa na", "sana", "sanua", "snʿaʾ", "Şana‘ā'", "Şan‘ā’", "Σάνα", "Сана", "Санъо", "צנעא", "صنعاء", "ሳና", "サヌア", "萨那", "사나"], ["Sahar", "Saḩar", "shr", "سحر"], ["SYE", "Sa'dah", "Sa`da", "Sa`dah", "Saada", "Sa‘da", "Sa’dah", "Şa‘dah", "صعده"], ["MYN", "Magreb", "Mar`rib", "Marib", "Мариб"], ["Al Hawtah", "Al Ḩawţah", "Lahaj", "Lahej", "Lahij", "Lahj", "Lakhydzh", "Laḩij", "alhwtt", "lhj", "Лахыдж", "الحوطة", "لحج"], ["Ibas", "Ibb", "ab", "ibbu", "ibeu", "yi bo", "Ібб", "Ибб", "איב", "إب", "اب", "イッブ", "伊卜", "이브"], ["Hage", "Haggah", "Haggiah", "Hajja", "Hajjah", "Hajje", "Khadzh", "hjt", "Хадж", "حجة", "Ḥage", "Ḥaggah", "Ḥaggiah", "Ḩajjah"], ["Dhi Sifal", "Dhi Sufal", "Dhi as Sufal", "Dhi es-Sifal", "Dhī Sifal", "Dhī Sufāl", "Dhī as Sufāl", "Dhī es-Sifāl", "dhy alsfal", "dhy sfal", "ذي السفال", "ذي سفال"], ["DMR", "Damar", "Dhamar", "Dhamār", "dhmar", "ذمار"], ["Bait al Faqih", "Bait al Faqīh", "Bayt al Fakih Ibn `Udjayl", "Bayt al Fakih al-Saghir", "Bayt al Fakīh Ibn ‘Udjayl", "Bayt al Fakīh al-Saghīr", "Bayt al Faqih", "Bayt al Faqīh", "Bayt al-Fakih", "Bayt al-Fakīh", "Beit Faqih", "Beit el-Faqih", "Beit el-Faqīh", "Beit-el-Fakih", "byt alfqyh", "بيت الفقيه"], ["Badjil", "Bagil", "Bajil", "Bâdjil", "Bāgil", "Bājil", "bajl", "باجل"], ["'Ataq", "AXK", "Ataq", "Attak", "Attaq", "`Ataq", "عتق", "‘Ataq", "‘Atāq"], ["`Amran", "`Umran", "عمران", "‘Amrān", "‘Umrān"], ["Al Mukalla", "Al Mukallā", "Al'-Mukalla", "Al-Mukalla", "MKX", "Mukalla", "RIY", "almkla", "Аль-Мукалла", "المكلا"], ["Al Hudaydah", "Al Ḩudaydah", "El-Hodeidah", "El-Ḥodeidah", "HOD", "Hodaidah", "Hodeida", "Hudaida", "Hudaydah", "alhdydt", "hdydh", "الحديدة", "حدیده", "Ḩudaydah"], ["Al Hazm", "Al Ḩazm", "El-Hazm", "El-Ḥazm", "Hazm", "Hazm al Jawf", "alhzm", "الحزم", "Ḩazm al Jawf"], ["Al Bayda", "Al Bayda'", "Al Bayḑā’", "Al Beidha", "Al-Baida", "Al-Baidhah", "Al-Baidā", "BYD", "Beida", "Beidha", "البيضاء"], ["ADE", "Adan", "Adehn", "Adem", "Aden", "Aden khot", "Aden shaary", "Adena", "Adenas", "Adeno", "Adén", "Aidin", "Anten", "Cadan", "`Adan", "adana", "aden", "edana", "xeden", "ya ding", "Áden", "Áidin", "Ədən", "Ɛaden", "Άντεν", "Аден", "Аден хот", "Аден шаары", "Адэн", "Ադեն", "עדן", "عدن", "अदन", "एडन", "เอเดน", "အေဒင်မြို့", "‘Adan", "アデン", "亚丁", "亞丁", "아덴"]]
latitude_list = [13.12871, 14.1951, 14.29804, 13.57952, 15.17177, 15.35472, 15.31637, 16.94021, 15.46253, 13.05667, 13.96667, 15.69425, 13.83446, 14.54274, 14.51635, 15.05898, 14.53767, 15.6594, 14.54248, 14.79781, 16.16406, 13.98523, 12.77944]
longitude_list = [45.38073, 43.31518, 44.37795, 44.02091, 44.32442, 44.20667, 44.3088, 43.76393, 45.32581, 44.88194, 44.18333, 43.60582, 44.11469, 44.40514, 43.32446, 43.28731, 46.83187, 43.94385, 49.12424, 42.95452, 44.77692, 45.57272, 45.03667]
country_code_list = ["YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE", "YE"]
population_list = [19879, 52590, 33050, 615222, 69404, 1937451, 31859, 51870, 16794, 23375, 234837, 43549, 37997, 160114, 34204, 48218, 37315, 90792, 566000, 617871, 18241, 37821, 863000]
dem_list = [20, 114, 2626, 1316, 2482, 2253, 2374, 1876, 1095, 136, 1931, 1795, 1857, 2421, 151, 191, 1148, 2239, 39, 10, 1116, 2005, 16]
timezone_list = [167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167]
altitude_list = [-1, -1, -1, 1400, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
_feature_class_list = ["P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P"]
_feature_code_list = ["PPLA", "PPLA2", "PPLA2", "PPLA", "PPLA2", "PPLC", "PPL", "PPLA", "PPLA", "PPLA", "PPLA", "PPLA", "PPLA2", "PPLA", "PPLA2", "PPLA2", "PPLA", "PPLA", "PPLA", "PPLA", "PPLA", "PPLA", "PPLA"]
_parent_code_list = ["YE.01.1210", "YE.08.1824", "YE.23.1102", "YE.25.1520", "YE.16.2305", "YE.26", "YE.16.2305", "YE.15.2215", "YE.14.2612", "YE.24.2514", "YE.23.1118", "YE.22.1728", "YE.23.1116", "YE.11.2008", "YE.08.1817", "YE.08.1810", "YE.05.2113", "YE.19.2915", "YE.04.1929", "YE.08.1821", "YE.21.1605", "YE.20.1409", "YE.02.2407"]
_states = {"YE.25": ["Ta‘izz", "Ta'izz", 70222], "YE.05": ["Gobernación de Shabwah", "Shabwah", 70935], "YE.16": ["Sanaa Governorate", "Sanaa Governorate", 71132], "YE.15": ["Şa‘dah", "Sa'dah", 71333], "YE.27": ["Raymah", "Raymah", 71532], "YE.14": ["Ma’rib", "Ma'rib", 72966], "YE.10": ["Al Mahwit Governorate", "Al Mahwit Governorate", 73200], "YE.21": ["Al Jawf", "Al Jawf", 74222], "YE.04": ["Muhafazat Hadramaout", "Muhafazat Hadramaout", 75411], "YE.11": ["Dhamār", "Dhamar", 76183], "YE.03": ["Al Mahrah Governorate", "Al Mahrah Governorate", 78985], "YE.08": ["Al Hudaydah", "Al Hudaydah", 79416], "YE.20": ["Al Bayda", "Al Bayda", 79838], "YE.02": ["Aden", "Aden", 80412], "YE.01": ["Abyan Governorate", "Abyan Governorate", 80425], "YE.18": ["Aḑ Ḑāli‘", "Ad Dali'", 6201193], "YE.19": ["Omran", "Omran", 6201194], "YE.22": ["Ḩajjah", "Hajjah", 6201195], "YE.23": ["Ibb Governorate", "Ibb Governorate", 6201196], "YE.24": ["Laḩij", "Lahij", 6201197], "YE.26": ["Amanat Alasimah", "Amanat Alasimah", 6940571], "YE.28": ["Soqatra", "Soqatra", 9645387]}
_districts = {"YE.08.1807": ["Az Zaydīyah", "Az Zaydiyah", 69440], "YE.08.1824": ["Zabīd", "Zabid", 69499], "YE.23.1102": ["Yarīm", "Yarim", 69558], "YE.22.1730": ["Washḩah", "Washhah", 69639], "YE.23.1111": ["Al ‘Udayn", "Al 'Udayn", 69921], "YE.10.2702": ["Aţ Ţawīlah", "At Tawilah", 70135], "YE.25.1502": ["At Ta‘izzīyah", "At Ta'izziyah", 70221], "YE.20.1419": ["Ash Sharafayn", "Ash Sharafayn", 70825], "YE.19.2905": ["Shahārah", "Shaharah", 70908], "YE.16.2305": ["Sanhan", "Sanhan", 71131], "YE.15.2211": ["Saḩār", "Sahar", 71271], "YE.15.2215": ["Şa‘dah", "Sa'dah", 71332], "YE.20.1413": ["Radā‘", "Rada'", 71489], "YE.15.2205": ["Rāziḩ", "Razih", 71519], "YE.23.1104": ["An Nādirah", "An Nadirah", 72370], "YE.25.1506": ["Al Mukhā’", "Al Mukha'", 72514], "YE.25.1501": ["Māwīyah", "Mawiyah", 72780], "YE.14.2612": ["Marib City", "Marib City", 72965], "YE.23.1107": ["Al Makhādir", "Al Makhadir", 73172], "YE.08.1820": ["Khawlān", "Khawlan", 73794], "YE.19.2919": ["Khamir", "Khamir", 73865], "YE.10.2701": ["Shibām Kawkabān", "Shibam Kawkaban", 73956], "YE.23.1120": ["Ibb", "Ibb", 74475], "YE.19.2902": ["Ḩūth", "Huth", 74489], "YE.04.1928": ["Huraidhah", "Huraidhah", 74580], "YE.14.2609": ["Ḩarīb", "Harib", 75132], "YE.22.1702": ["Harad District", "Harad District", 75142], "YE.16.2301": ["Hamdān", "Hamdan", 75257], "YE.22.1728": ["Hajjah City District", "Hajjah City District", 75334], "YE.23.1116": ["Dhī as Sufāl", "Dhi as Sufal", 76153], "YE.11.2008": ["Madīnat Dhamār", "Madinat Dhamar", 76182], "YE.08.1817": ["Bayt al Faqīh", "Bayt al Faqih", 76989], "YE.20.1410": ["Al Bayḑā’", "Al Bayda'", 77026], "YE.21.1610": ["Barţ al ‘Anān", "Bart al `Anan", 77122], "YE.08.1810": ["Bājil", "Bajil", 77407], "YE.11.2010": ["‘Ans", "`Ans", 78321], "YE.19.2915": ["‘Amrān", "`Amran", 78427], "YE.15.2208": ["Haydan", "Haydan", 6940588], "YE.22.1704": ["Abs", "Abs", 6940589], "YE.22.1713": ["Qafl Shamer", "Qafl Shamer", 6940590], "YE.22.1724": ["Bani Qa'is", "Bani Qa'is", 6940591], "YE.23.1109": ["Hazm Al Udayn", "Hazm Al Udayn", 6940592], "YE.23.1101": ["Al Qafr", "Al Qafr", 6940593], "YE.22.1717": ["Al Maghrabah", "Al Maghrabah", 6940594], "YE.26.1310": ["Bani Al Harith", "Bani Al Harith", 6940595], "YE.25.1523": ["Sama", "Sama", 6940596], "YE.25.1512": ["Al Misrakh", "Al Misrakh", 6940597], "YE.25.1511": ["Sabir Al Mawadim", "Sabir Al Mawadim", 6940598], "YE.25.1513": ["Dimnat Khadir", "Dimnat Khadir", 6940599], "YE.25.1515": ["Ash Shamayatayn", "Ash Shamayatayn", 6940600], "YE.25.1509": ["Jabal Habashy", "Jabal Habashy", 6940601], "YE.21.1604": ["Az Zahir", "Az Zahir", 6940602], "YE.21.1612": ["Kharab Al Marashi", "Kharab Al Marashi", 6940603], "YE.22.1715": ["Al Mahabishah", "Al Mahabishah", 6940604], "YE.22.1703": ["Midi", "Midi", 6940605], "YE.22.1705": ["Hayran", "Hayran", 6940606], "YE.22.1727": ["Bani Al Awam", "Bani Al Awam", 6940607], "YE.22.1729": ["Hajjah", "Hajjah", 6940608], "YE.08.1805": ["Al Munirah", "Al Munirah", 6940609], "YE.08.1814": ["Ad Durayhimi", "Ad Durayhimi", 6940610], "YE.08.1813": ["Al Marawi'ah", "Al Marawi'ah", 6940611], "YE.08.1821": ["Al Hawak", "Al Hawak", 6940612], "YE.08.1804": ["As Salif", "As Salif", 6940613], "YE.08.1818": ["Jabal Ra's", "Jabal Ra's", 6940614], "YE.04.1920": ["Rakhyah", "Rakhyah", 6940615], "YE.11.2011": ["Dawran Aness", "Dawran Aness", 6940616], "YE.05.2105": ["Usaylan", "Usaylan", 6940617], "YE.15.2213": ["Al Hashwah", "Al Hashwah", 6940618], "YE.15.2204": ["Ghamr", "Ghamr", 6940619], "YE.15.2202": ["Qatabir", "Qatabir", 6940620], "YE.15.2203": ["Monabbih", "Monabbih", 6940621], "YE.16.2302": ["Arhab", "Arhab", 6940622], "YE.24.2515": ["Tuban", "Tuban", 6940623], "YE.24.2510": ["Al Qabbaytah", "Al Qabbaytah", 6940624], "YE.14.2604": ["Harib Al Qaramish", "Harib Al Qaramish", 6940625], "YE.19.2901": ["Harf Sufyan", "Harf Sufyan", 6940626], "YE.19.2911": ["Raydah", "Raydah", 6940627], "YE.23.1105": ["Ash Sha'ir", "Ash Sha'ir", 6940628], "YE.23.1103": ["Ar Radmah", "Ar Radmah", 6940629], "YE.23.1106": ["As Saddah", "As Saddah", 6940630], "YE.23.1117": ["Mudhaykhirah", "Mudhaykhirah", 6940631], "YE.23.1110": ["Far Al Udayn", "Far Al Udayn", 6940632], "YE.18.3009": ["Al Husha", "Al Husha", 6940633], "YE.18.3003": ["Qa'atabah", "Qa'atabah", 6940634], "YE.27.3102": ["Al Jabin", "Al Jabin", 6940635], "YE.27.3105": ["Al Jafariyah", "Al Jafariyah", 6940636], "YE.27.3104": ["Kusmah", "Kusmah", 6940637], "YE.27.3103": ["As Salafiyah", "As Salafiyah", 6940638], "YE.23.1119": ["Al Dhihar", "Al Dhihar", 6940639], "YE.23.1115": ["As Sayyani", "As Sayyani", 6940640], "YE.23.1118": ["Al Mashannah", "Al Mashannah", 6940641], "YE.23.1114": ["As Sabrah", "As Sabrah", 6940642], "YE.23.1108": ["Hubaysh", "Hubaysh", 6940643], "YE.23.1112": ["Jiblah", "Jiblah", 6940644], "YE.23.1113": ["Ba'dan", "Ba'dan", 6940645], "YE.01.1209": ["Ahwar", "Ahwar", 6940646], "YE.01.1202": ["Mudiyah", "Mudiyah", 6940647], "YE.01.1201": ["Al Mahfad", "Al Mahfad", 6940648], "YE.01.1206": ["Rasad", "Rasad", 6940649], "YE.01.1203": ["Jayshan", "Jayshan", 6940650], "YE.01.1205": ["Sibah", "Sibah", 6940651], "YE.01.1204": ["Lawdar", "Lawdar", 6940652], "YE.01.1208": ["Al Wade'a", "Al Wade'a", 6940653], "YE.01.1211": ["Khanfir", "Khanfir", 6940654], "YE.01.1207": ["Sarar", "Sarar", 6940655], "YE.01.1210": ["Zingibar", "Zingibar", 6940656], "YE.26.1306": ["Al Wahdah", "Al Wahdah", 6940657], "YE.26.1301": ["Old City", "Old City", 6940658], "YE.26.1309": ["Ath'thaorah", "Ath'thaorah", 6940659], "YE.26.1304": ["Assafi'yah", "Assafi'yah", 6940660], "YE.26.1308": ["Ma'ain", "Ma'ain", 6940661], "YE.26.1305": ["As Sabain", "As Sabain", 6940662], "YE.26.1302": ["Shu'aub", "Shu'aub", 6940663], "YE.26.1303": ["Az'zal", "Az'zal", 6940664], "YE.26.1307": ["At Tahrir", "At Tahrir", 6940665], "YE.20.1417": ["Sabah", "Sabah", 6940666], "YE.20.1415": ["Wald Rabi'", "Wald Rabi'", 6940667], "YE.20.1414": ["Al Quraishyah", "Al Quraishyah", 6940668], "YE.20.1418": ["Ar Ryashyyah", "Ar Ryashyyah", 6940669], "YE.20.1401": ["Na'man", "Na'man", 6940670], "YE.20.1408": ["Mukayras", "Mukayras", 6940671], "YE.20.1402": ["Nati'", "Nati'", 6940672], "YE.20.1411": ["As Sawadiyah", "As Sawadiyah", 6940673], "YE.20.1407": ["At Taffah", "At Taffah", 6940674], "YE.20.1412": ["Radman Al Awad", "Radman Al Awad", 6940675], "YE.20.1406": ["Dhi Na'im", "Dhi Na'im", 6940676], "YE.20.1409": ["Al Bayda City", "Al Bayda City", 6940677], "YE.20.1420": ["Al Malagim", "Al Malagim", 6940678], "YE.20.1403": ["Maswarah", "Maswarah", 6940679], "YE.20.1416": ["Al A'rsh", "Al A'rsh", 6940680], "YE.20.1404": ["As Sawma'ah", "As Sawma'ah", 6940681], "YE.20.1405": ["Az Zahir", "Az Zahir", 6940682], "YE.25.1510": ["Mashra'a Wa Hadnan", "Mashra'a Wa Hadnan", 6940683], "YE.25.1516": ["Al Wazi'iyah", "Al Wazi'iyah", 6940684], "YE.25.1514": ["As Silw", "As Silw", 6940685], "YE.25.1517": ["Hayfan", "Hayfan", 6940686], "YE.25.1521": ["Al Ma'afer", "Al Ma'afer", 6940687], "YE.25.1522": ["Al Mawasit", "Al Mawasit", 6940688], "YE.25.1507": ["Dhubab", "Dhubab", 6940689], "YE.25.1519": ["Al Qahirah", "Al Qahirah", 6940690], "YE.25.1520": ["Salh", "Salh", 6940691], "YE.25.1518": ["Al Mudhaffar", "Al Mudhaffar", 6940692], "YE.25.1508": ["Mawza", "Mawza", 6940693], "YE.25.1504": ["Shara'b Ar Rawnah", "Shara'b Ar Rawnah", 6940694], "YE.25.1505": ["Maqbanah", "Maqbanah", 6940695], "YE.25.1503": ["Shara'b As Salam", "Shara'b As Salam", 6940696], "YE.21.1605": ["Al Hazm", "Al Hazm", 6940697], "YE.21.1609": ["Al Khalq", "Al Khalq", 6940698], "YE.21.1606": ["Al Maton", "Al Maton", 6940699], "YE.21.1603": ["Al Matammah", "Al Matammah", 6940700], "YE.21.1607": ["Al Maslub", "Al Maslub", 6940701], "YE.21.1608": ["Al Ghayl", "Al Ghayl", 6940702], "YE.21.1601": ["Khabb wa ash Sha'af", "Khabb wa ash Sha'af", 6940703], "YE.21.1602": ["Al Humaydat", "Al Humaydat", 6940704], "YE.21.1611": ["Rajuzah", "Rajuzah", 6940705], "YE.22.1722": ["Ku'aydinah", "Ku'aydinah", 6940706], "YE.22.1706": ["Mustaba", "Mustaba", 6940707], "YE.22.1731": ["Qarah", "Qarah", 6940708], "YE.22.1723": ["Wadhrah", "Wadhrah", 6940709], "YE.22.1718": ["Kuhlan Affar", "Kuhlan Affar", 6940710], "YE.22.1709": ["Kuhlan Ash Sharaf", "Kuhlan Ash Sharaf", 6940711], "YE.22.1719": ["Sharas", "Sharas", 6940712], "YE.22.1711": ["Khayran Al Muharraq", "Khayran Al Muharraq", 6940713], "YE.22.1721": ["Ash Shahil", "Ash Shahil", 6940714], "YE.22.1726": ["Najrah", "Najrah", 6940715], "YE.22.1725": ["Ash Shaghadirah", "Ash Shaghadirah", 6940716], "YE.22.1710": ["Aflah Ash Shawm", "Aflah Ash Shawm", 6940717], "YE.22.1720": ["Mabyan", "Mabyan", 6940718], "YE.22.1716": ["Al Miftah", "Al Miftah", 6940719], "YE.22.1714": ["Aflah Al Yaman", "Aflah Al Yaman", 6940720], "YE.22.1708": ["Al Jamimah", "Al Jamimah", 6940721], "YE.22.1712": ["Aslem", "Aslem", 6940722], "YE.22.1701": ["Bakil Al Mir", "Bakil Al Mir", 6940723], "YE.22.1707": ["Kushar", "Kushar", 6940724], "YE.08.1822": ["Al Mina", "Al Mina", 6940725], "YE.08.1815": ["As Sukhnah", "As Sukhnah", 6940726], "YE.08.1825": ["Al Garrahi", "Al Garrahi", 6940727], "YE.08.1812": ["Bura", "Bura", 6940728], "YE.08.1803": ["Kamaran", "Kamaran", 6940729], "YE.08.1816": ["Al Mansuriyah", "Al Mansuriyah", 6940730], "YE.08.1801": ["Az Zuhrah", "Az Zuhrah", 6940731], "YE.08.1809": ["Ad Dahi", "Ad Dahi", 6940732], "YE.08.1819": ["Hays", "Hays", 6940733], "YE.08.1826": ["At Tuhayat", "At Tuhayat", 6940734], "YE.08.1823": ["Al Hali", "Al Hali", 6940735], "YE.08.1811": ["Al Hajjaylah", "Al Hajjaylah", 6940736], "YE.08.1808": ["Al Mighlaf", "Al Mighlaf", 6940737], "YE.08.1806": ["Al Qanawis", "Al Qanawis", 6940738], "YE.08.1802": ["Alluheyah", "Alluheyah", 6940739], "YE.04.1922": ["Adh Dhlia'ah", "Adh Dhlia'ah", 6940740], "YE.04.1930": ["Al Mukalla", "Al Mukalla", 6940741], "YE.04.1923": ["Yabuth", "Yabuth", 6940742], "YE.04.1924": ["Hajr", "Hajr", 6940743], "YE.04.1908": ["Shibam", "Shibam", 6940744], "YE.04.1909": ["Sah", "Sah", 6940745], "YE.04.1916": ["Ghayl Bin Yamin", "Ghayl Bin Yamin", 6940746], "YE.04.1919": ["Wadi Al Ayn", "Wadi Al Ayn", 6940747], "YE.04.1921": ["Amd", "Amd", 6940748], "YE.04.1913": ["Ar Raydah Wa Qusayar", "Ar Raydah Wa Qusayar", 6940749], "YE.04.1918": ["Daw'an", "Daw'an", 6940750], "YE.04.1914": ["Ad Dis", "Ad Dis", 6940751], "YE.04.1915": ["Ash Shihr", "Ash Shihr", 6940752], "YE.04.1917": ["Ghayl Ba Wazir", "Ghayl Ba Wazir", 6940753], "YE.28.1927": ["Qulensya Wa Abd Al Kuri", "Qulensya Wa Abd Al Kuri", 6940754], "YE.04.1925": ["Brom Mayfa", "Brom Mayfa", 6940755], "YE.04.1929": ["Al Mukalla City", "Al Mukalla City", 6940756], "YE.04.1910": ["Sayun", "Sayun", 6940757], "YE.28.1926": ["Hidaybu", "Hidaybu", 6940758], "YE.04.1902": ["Thamud", "Thamud", 6940759], "YE.04.1903": ["Al Qaf", "Al Qaf", 6940760], "YE.04.1904": ["Zamakh wa Manwakh", "Zamakh wa Manwakh", 6940761], "YE.04.1912": ["As Sawm", "As Sawm", 6940762], "YE.04.1905": ["Hagr As Sai'ar", "Hagr As Sai'ar", 6940763], "YE.04.1911": ["Tarim", "Tarim", 6940764], "YE.04.1901": ["Rumah", "Rumah", 6940765], "YE.04.1907": ["Al Qatn", "Al Qatn", 6940766], "YE.04.1906": ["Al Abr", "Al Abr", 6940767], "YE.11.2009": ["Mayfa'at Anss", "Mayfa'at Anss", 6940768], "YE.11.2001": ["Al Hada", "Al Hada", 6940769], "YE.11.2006": ["Wusab Al Ali", "Wusab Al Ali", 6940770], "YE.11.2004": ["Maghirib Ans", "Maghirib Ans", 6940771], "YE.11.2002": ["Jahran", "Jahran", 6940772], "YE.11.2012": ["Al Manar", "Al Manar", 6940773], "YE.11.2003": ["Jabal Ash sharq", "Jabal Ash sharq", 6940774], "YE.11.2007": ["Wusab As Safil", "Wusab As Safil", 6940775], "YE.11.2005": ["Utmah", "Utmah", 6940776], "YE.05.2113": ["Ataq", "Ataq", 6940777], "YE.05.2117": ["Rudum", "Rudum", 6940778], "YE.05.2110": ["Nisab", "Nisab", 6940779], "YE.05.2107": ["Bayhan", "Bayhan", 6940780], "YE.05.2114": ["Habban", "Habban", 6940781], "YE.05.2111": ["Hatib", "Hatib", 6940782], "YE.05.2116": ["Mayfa'a", "Mayfa'a", 6940783], "YE.05.2108": ["Merkhah Al Ulya", "Merkhah Al Ulya", 6940784], "YE.05.2109": ["Merkhah As Sufla", "Merkhah As Sufla", 6940785], "YE.05.2112": ["As Said", "As Said", 6940786], "YE.05.2101": ["Dhar", "Dhar", 6940787], "YE.05.2104": ["Arma", "Arma", 6940788], "YE.05.2103": ["Jardan", "Jardan", 6940789], "YE.05.2106": ["Ain", "Ain", 6940790], "YE.05.2102": ["Al Talh", "Al Talh", 6940791], "YE.05.2115": ["Ar Rawdah", "Ar Rawdah", 6940792], "YE.15.2207": ["Al Dhaher", "Al Dhaher", 6940793], "YE.15.2206": ["Shada'a", "Shada'a", 6940794], "YE.15.2209": ["Saqayn", "Saqayn", 6940795], "YE.15.2201": ["Baqim", "Baqim", 6940796], "YE.15.2212": ["As Safra", "As Safra", 6940797], "YE.15.2210": ["Majz", "Majz", 6940798], "YE.15.2214": ["Kitaf wa Al Boqe'e", "Kitaf wa Al Boqe'e", 6940799], "YE.16.2303": ["Nihm", "Nihm", 6940800], "YE.16.2307": ["Bani Matar", "Bani Matar", 6940801], "YE.16.2313": ["Attyal", "Attyal", 6940802], "YE.16.2315": ["Al Husn", "Al Husn", 6940803], "YE.16.2306": ["Bilad Ar Rus", "Bilad Ar Rus", 6940804], "YE.16.2309": ["Al Haymah Al Kharijiyah", "Al Haymah Al Kharijiyah", 6940805], "YE.16.2310": ["Manakhah", "Manakhah", 6940806], "YE.16.2316": ["Jihanah", "Jihanah", 6940807], "YE.16.2314": ["Bani Dhabyan", "Bani Dhabyan", 6940808], "YE.16.2312": ["Khwlan", "Khwlan", 6940809], "YE.16.2304": ["Bani Hushaysh", "Bani Hushaysh", 6940810], "YE.16.2308": ["Al Haymah Ad Dakhiliyah", "Al Haymah Ad Dakhiliyah", 6940811], "YE.16.2311": ["Sa'fan", "Sa'fan", 6940812], "YE.02.2405": ["Attawahi", "Attawahi", 6940813], "YE.02.2407": ["Craiter", "Craiter", 6940814], "YE.02.2404": ["Al Buraiqeh", "Al Buraiqeh", 6940815], "YE.02.2408": ["Khur Maksar", "Khur Maksar", 6940816], "YE.02.2401": ["Dar Sad", "Dar Sad", 6940817], "YE.02.2403": ["Al Mansura", "Al Mansura", 6940818], "YE.02.2402": ["Ash Shaikh Outhman", "Ash Shaikh Outhman", 6940819], "YE.02.2406": ["Al Mualla", "Al Mualla", 6940820], "YE.24.2511": ["Tur Al Bahah", "Tur Al Bahah", 6940821], "YE.24.2514": ["Al  Hawtah", "Al  Hawtah", 6940822], "YE.24.2505": ["Habil Jabr", "Habil Jabr", 6940823], "YE.24.2504": ["Yahr", "Yahr", 6940824], "YE.24.2506": ["Halimayn", "Halimayn", 6940825], "YE.24.2508": ["Al Milah", "Al Milah", 6940826], "YE.24.2507": ["Radfan", "Radfan", 6940827], "YE.24.2503": ["Al Maflahy", "Al Maflahy", 6940828], "YE.24.2502": ["Yafa'a", "Yafa'a", 6940829], "YE.24.2509": ["Al Musaymir", "Al Musaymir", 6940830], "YE.24.2501": ["Al Had", "Al Had", 6940831], "YE.24.2512": ["Al Maqatirah", "Al Maqatirah", 6940832], "YE.24.2513": ["Al Madaribah Wa Al Arah", "Al Madaribah Wa Al Arah", 6940833], "YE.14.2605": ["Bidbadah", "Bidbadah", 6940834], "YE.14.2613": ["Ma'rib", "Marib", 6940835], "YE.14.2601": ["Majzar", "Majzar", 6940836], "YE.14.2603": ["Medghal", "Medghal", 6940837], "YE.14.2602": ["Raghwan", "Raghwan", 6940838], "YE.14.2606": ["Sirwah", "Sirwah", 6940839], "YE.14.2611": ["Al Abdiyah", "Al Abdiyah", 6940840], "YE.14.2610": ["Mahliyah", "Mahliyah", 6940841], "YE.14.2614": ["Jabal Murad", "Jabal Murad", 6940842], "YE.14.2608": ["Rahabah", "Rahabah", 6940843], "YE.14.2607": ["Al Jubah", "Al Jubah", 6940844], "YE.10.2709": ["Al Mahwait", "Al Mahwait", 6940845], "YE.10.2707": ["Bani Sa'd", "Bani Sa'd", 6940846], "YE.10.2704": ["Al Khabt", "Al Khabt", 6940847], "YE.10.2703": ["Ar Rujum", "Ar Rujum", 6940848], "YE.10.2708": ["Al Mahwait City", "Al Mahwait City", 6940849], "YE.10.2706": ["Hufash", "Hufash", 6940850], "YE.10.2705": ["Milhan", "Milhan", 6940851], "YE.03.2801": ["Shahan", "Shahan", 6940852], "YE.03.2807": ["Sayhut", "Sayhut", 6940853], "YE.03.2802": ["Hat", "Hat", 6940854], "YE.03.2804": ["Al Ghaydah", "Al Ghaydah", 6940855], "YE.03.2803": ["Hawf", "Hawf", 6940856], "YE.03.2809": ["Huswain", "Huswain", 6940857], "YE.03.2808": ["Qishn", "Qishn", 6940858], "YE.03.2805": ["Man'ar", "Man'ar", 6940859], "YE.03.2806": ["Al Masilah", "Al Masilah", 6940860], "YE.19.2912": ["Jabal Iyal Yazid", "Jabal Iyal Yazid", 6940861], "YE.19.2903": ["Al Ashah", "Al Ashah", 6940862], "YE.19.2907": ["Suwayr", "Suwayr", 6940863], "YE.19.2920": ["Bani Suraim", "Bani Suraim", 6940864], "YE.19.2906": ["Al Madan", "Al Madan", 6940865], "YE.19.2917": ["Thula", "Thula", 6940866], "YE.19.2913": ["As Sudah", "As Sudah", 6940867], "YE.19.2908": ["Habur Zulaymah", "Habur Zulaymah", 6940868], "YE.19.2904": ["Al Qaflah", "Al Qaflah", 6940869], "YE.19.2916": ["Maswar", "Maswar", 6940870], "YE.19.2914": ["As Sawd", "As Sawd", 6940871], "YE.19.2910": ["Kharif", "Kharif", 6940872], "YE.19.2918": ["Iyal Surayh", "Iyal Surayh", 6940873], "YE.19.2909": ["Dhi Bin", "Dhi Bin", 6940874], "YE.18.3006": ["Ad Dhale'e", "Ad Dhale'e", 6940875], "YE.18.3005": ["Al Hussein", "Al Hussein", 6940876], "YE.18.3007": ["Jahaf", "Jahaf", 6940877], "YE.18.3002": ["Damt", "Damt", 6940878], "YE.18.3008": ["Al Azariq", "Al Azariq", 6940879], "YE.18.3001": ["Juban", "Juban", 6940880], "YE.18.3004": ["Ash Shu'ayb", "Ash Shu'ayb", 6940881], "YE.27.3101": ["Bilad At Ta'am", "Bilad At Ta'am", 6940882], "YE.27.3106": ["Mazhar", "Mazhar", 6940883]}