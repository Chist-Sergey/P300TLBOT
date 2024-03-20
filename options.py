# and set a time
from datetime import (
    time as dt_time,
)

# set a time zone
from zoneinfo import ZoneInfo


def job_time_first():
    time = dt_time(

        hour=8,                 # your value here
        minute=0,

        tzinfo=job_time_zone(),
    )
    return time


def job_time_second():
    time = dt_time(

        hour=20,                # your value here
        minute=0,

        tzinfo=job_time_zone(),
    )
    return time


def job_time_zone():
    timezone = ZoneInfo(
        'Etc/GMT+7'             # your offset here
    )

    return timezone

"""
In case you are curious...
There's a list of all available time zones (very long!)

'America/Cordoba',
'America/Grand_Turk',
'Pacific/Yap',
'Asia/Harbin',
'Pacific/Saipan',
'Hongkong',
'Pacific/Efate',
'Africa/Tunis',
'Antarctica/Macquarie',
'Canada/Saskatchewan',
'Asia/Krasnoyarsk',
'Canada/Central',
'Pacific/Tongatapu',
'America/Santarem',
'US/Alaska',
'America/Iqaluit',
'Asia/Atyrau',
'Asia/Calcutta',
'Asia/Yangon',
'Europe/Lisbon',
'Africa/Juba',
'Pacific/Noumea',
'Asia/Dacca',
'America/Argentina/San_Luis',
'Asia/Amman',
'US/East-Indiana',
'Indian/Chagos',
'Etc/GMT',
'America/Catamarca',
'America/Nome',
'America/Indiana/Petersburg',
'America/Ciudad_Juarez',
'Atlantic/Cape_Verde',
'Etc/GMT+11',
'Asia/Singapore',
'PRC',
'Asia/Yerevan',
'Asia/Pontianak',
'Canada/Atlantic',
'Indian/Reunion',
'America/Porto_Velho',
'America/Indiana/Tell_City',
'Australia/Darwin',
'America/Tortola',
'America/Panama',
'America/Winnipeg',
'Etc/GMT-13',
'Europe/Paris',
'Etc/GMT-14',
'Africa/Addis_Ababa',
'Indian/Cocos',
'America/La_Paz',
'Pacific/Galapagos',
'Pacific/Tarawa',
'WET',
'Asia/Tel_Aviv',
'UTC',
'America/Tegucigalpa',
'Africa/Casablanca',
'Asia/Kabul',
'America/Paramaribo',
'Asia/Aqtobe',
'Europe/Busingen',
'Europe/Kaliningrad',
'Asia/Qyzylorda',
'Chile/EasterIsland',
'Asia/Nicosia',
'US/Mountain',
'Asia/Tokyo',
'Europe/Jersey',
'Africa/Asmara',
'America/Goose_Bay',
'MET',
'Europe/Guernsey',
'Africa/Monrovia',
'GMT-0',
'Turkey',
'GMT0',
'Asia/Makassar',
'Asia/Thimphu',
'Asia/Baku',
'Europe/Brussels',
'Asia/Dhaka',
'Atlantic/Reykjavik',
'America/Swift_Current',
'America/Argentina/Ushuaia',
'Australia/ACT',
'Australia/Broken_Hill',
'America/Cayenne',
'America/Cancun',
'Chile/Continental',
'America/Argentina/Rio_Gallegos',
'America/Caracas',
'America/Menominee',
'Asia/Tbilisi',
'Iceland',
'America/Manaus',
'Antarctica/Casey',
'Etc/GMT-0',
'Asia/Phnom_Penh',
'Antarctica/Syowa',
'Asia/Brunei',
'Asia/Magadan',
'Asia/Ulan_Bator',
'Indian/Comoro',
'America/Denver',
'Europe/Luxembourg',
'America/Bahia',
'Etc/GMT+9',
'America/Argentina/San_Juan',
'Africa/Ndjamena',
'America/Indiana/Knox',
'Asia/Taipei',
'America/Scoresbysund',
'Africa/Lubumbashi',
'Africa/Kinshasa',
'America/Anguilla',
'Europe/Vaduz',
'Brazil/Acre',
'America/Indiana/Vevay',
'Asia/Macau',
'Brazil/DeNoronha',
'America/Chicago',
'Israel',
'Zulu',
'Asia/Almaty',
'Europe/Rome',
'Australia/Lindeman',
'Asia/Yakutsk',
'America/Boa_Vista',
'America/Montevideo',
'Europe/Zaporozhye',
'Europe/Istanbul',
'Singapore',
'America/Detroit',
'America/Argentina/Salta',
'Antarctica/Vostok',
'Atlantic/Azores',
'America/Belem',
'NZ-CHAT',
'America/Cayman',
'Asia/Ust-Nera',
'America/Boise',
'Asia/Kolkata',
'Indian/Christmas',
'America/Monterrey',
'America/Belize',
'Asia/Hovd',
'Asia/Jakarta',
'Antarctica/Davis',
'Australia/Adelaide',
'Pacific/Guadalcanal',
'America/Moncton',
'America/Argentina/Cordoba',
'Africa/Windhoek',
'America/Knox_IN',
'America/Cuiaba',
'HST',
'Asia/Shanghai',
'America/Asuncion',
'America/North_Dakota/Beulah',
'Africa/Lagos',
'Europe/Ulyanovsk',
'America/Sitka',
'Europe/Samara',
'Etc/GMT0',
'Asia/Kuwait',
'Antarctica/McMurdo',
'America/Santa_Isabel',
'America/Antigua',
'Pacific/Guam',
'America/Punta_Arenas',
'America/Grenada',
'Europe/Berlin',
'America/Indiana/Winamac',
'Australia/Canberra',
'Europe/Chisinau',
'Asia/Istanbul',
'Atlantic/Faroe',
'Asia/Muscat',
'Asia/Hebron',
'Europe/Vatican',
'America/Mexico_City',
'Etc/GMT-4',
'Asia/Rangoon',
'Pacific/Chuuk',
'America/Argentina/Mendoza',
'Africa/Blantyre',
'Etc/GMT+8',
'Asia/Kashgar',
'Pacific/Pago_Pago',
'Pacific/Wake',
'Asia/Beirut',
'Pacific/Marquesas',
'America/Rio_Branco',
'Asia/Yekaterinburg',
'Atlantic/Canary',
'Asia/Jayapura',
'Africa/Nairobi',
'Pacific/Midway',
'Etc/GMT+3',
'US/Samoa',
'Canada/Mountain',
'Pacific/Ponape',
'Asia/Bishkek',
'Europe/Ljubljana',
'Etc/GMT+6',
'Africa/Conakry',
'America/Yellowknife',
'America/Ojinaga',
'America/Martinique',
'Europe/Copenhagen',
'Europe/Astrakhan',
'Asia/Barnaul',
'Asia/Kuching',
'Australia/NSW',
'America/Campo_Grande',
'Atlantic/St_Helena',
'America/St_Thomas',
'Europe/Uzhgorod',
'Australia/North',
'Australia/Lord_Howe',
'Europe/Podgorica',
'Eire',
'Atlantic/Jan_Mayen',
'America/Thule',
'America/Barbados',
'Europe/Bratislava',
'Asia/Kuala_Lumpur',
'MST',
'America/Puerto_Rico',
'America/Matamoros',
'Asia/Tomsk',
'Etc/GMT+0',
'Etc/GMT+10',
'Asia/Hong_Kong',
'America/Atka',
'America/Indiana/Indianapolis',
'America/Mazatlan',
'Pacific/Enderbury',
'America/Bogota',
'Australia/South',
'Etc/GMT-5',
'CET',
'Brazil/East',
'America/St_Johns',
'Asia/Bangkok',
'Etc/Universal',
'EET',
'Canada/Pacific',
'Factory',
'Africa/Bamako',
'America/Pangnirtung',
'Pacific/Kanton',
'US/Pacific',
'America/Marigot',
'America/North_Dakota/New_Salem',
'Europe/Skopje',
'America/Guatemala',
'Africa/Ceuta',
'Greenwich',
'ROK',
'Indian/Mayotte',
'America/Inuvik',
'Asia/Samarkand',
'PST8PDT',
'America/Rankin_Inlet',
'America/Mendoza',
'Europe/Belfast',
'America/Cambridge_Bay',
'America/Fortaleza',
'America/Toronto',
'America/Eirunepe',
'Australia/Eucla',
'America/Adak',
'Europe/San_Marino',
'Africa/Kigali',
'Etc/UTC',
'America/Havana',
'GB',
'Europe/Tiraspol',
'Europe/Warsaw',
'America/Nuuk',
'Asia/Chungking',
'Canada/Newfoundland',
'Europe/Kiev',
'Africa/Asmera',
'America/Guayaquil',
'America/Creston',
'America/Aruba',
'Europe/Andorra',
'America/Ensenada',
'Cuba',
'Atlantic/Faeroe',
'Etc/GMT-3',
'Pacific/Majuro',
'Australia/Yancowinna',
'Pacific/Bougainville',
'ROC',
'America/Araguaina',
'Asia/Ujung_Pandang',
'Africa/Douala',
'America/Los_Angeles',
'America/St_Lucia',
'Australia/Tasmania',
'Asia/Chongqing',
'Jamaica',
'Etc/GMT-12',
'Indian/Kerguelen',
'Europe/Isle_of_Man',
'America/Hermosillo',
'Europe/Tirane',
'America/Coral_Harbour',
'Africa/Djibouti',
'Europe/Gibraltar',
'Europe/London',
'America/Vancouver',
'Asia/Bahrain',
'America/Guadeloupe',
'America/Halifax',
'Etc/Zulu',
'America/Regina',
'Pacific/Samoa',
'Europe/Zagreb',
'Asia/Ashgabat',
'America/Lower_Princes',
'Africa/Algiers',
'Asia/Gaza',
'America/Danmarkshavn',
'Australia/LHI',
'Australia/Currie',
'Pacific/Chatham',
'Africa/Maputo',
'America/Argentina/La_Rioja',
'Africa/Mbabane',
'Europe/Malta',
'Australia/Queensland',
'America/Santo_Domingo',
'Mexico/BajaSur',
'America/Noronha',
'America/Dawson_Creek',
'Canada/Yukon',
'Pacific/Auckland',
'Pacific/Apia',
'Pacific/Fiji',
'America/St_Vincent',
'America/Santiago',
'Europe/Vilnius',
'US/Aleutian',
'Asia/Omsk',
'GMT',
'Africa/Timbuktu',
'Asia/Famagusta',
'America/Chihuahua',
'Asia/Tashkent',
'Asia/Qostanay',
'America/Kentucky/Monticello',
'America/Blanc-Sablon',
'America/Rainy_River',
'Indian/Antananarivo',
'America/Louisville',
'Pacific/Pohnpei',
'Asia/Pyongyang',
'America/Buenos_Aires',
'Asia/Sakhalin',
'Asia/Jerusalem',
'Africa/Lusaka',
'America/Port_of_Spain',
'America/Phoenix',
'America/Porto_Acre',
'America/Nassau',
'Australia/West',
'Brazil/West',
'Japan',
'Europe/Prague',
'Europe/Minsk',
'Africa/Dar_es_Salaam',
'America/Kralendijk',
'Australia/Perth',
'Europe/Kirov',
'Europe/Oslo',
'Poland',
'Libya',
'Etc/GMT+5',
'America/Lima',
'Europe/Saratov',
'America/Maceio',
'Asia/Riyadh',
'Asia/Manila',
'Atlantic/Bermuda',
'America/Indianapolis',
'Africa/Banjul',
'Africa/Gaborone',
'America/Virgin',
'Pacific/Palau',
'Europe/Bucharest',
'Indian/Mahe',
'Etc/GMT-1',
'America/Managua',
'UCT',
'America/Fort_Nelson',
'Africa/Maseru',
'Antarctica/DumontDUrville',
'America/Godthab',
'Africa/Malabo',
'Egypt',
'Africa/Accra',
'Asia/Kathmandu',
'EST',
'Antarctica/South_Pole',
'Pacific/Kwajalein',
'Arctic/Longyearbyen',
'Africa/Johannesburg',
'America/Bahia_Banderas',
'America/Tijuana',
'Europe/Kyiv',
'Asia/Dubai',
'US/Arizona',
'America/Argentina/Catamarca',
'Europe/Budapest',
'US/Indiana-Starke',
'US/Eastern',
'America/Guyana',
'Europe/Dublin',
'Europe/Nicosia',
'Pacific/Easter',
'Europe/Stockholm',
'Asia/Chita',
'Africa/Porto-Novo',
'America/Argentina/Jujuy',
'Africa/Bujumbura',
'America/St_Kitts',
'America/St_Barthelemy',
'Asia/Vientiane',
'Asia/Macao',
'Asia/Novokuznetsk',
'Europe/Zurich',
'Asia/Vladivostok',
'Africa/Freetown',
'Pacific/Johnston',
'Kwajalein',
'Africa/Mogadishu',
'America/Juneau',
'America/Sao_Paulo',
'America/Indiana/Marengo',
'Africa/El_Aaiun',
'America/Dawson',
'America/Metlakatla',
'GMT+0',
'America/Port-au-Prince',
'Europe/Amsterdam',
'America/Fort_Wayne',
'MST7MDT',
'Antarctica/Troll',
'Etc/GMT+12',
'GB-Eire',
'Mexico/BajaNorte',
'US/Hawaii',
'Europe/Mariehamn',
'Etc/GMT-10',
'Africa/Lome',
'America/El_Salvador',
'Pacific/Honolulu',
'Asia/Dili',
'EST5EDT',
'Europe/Sarajevo',
'America/Dominica',
'America/Thunder_Bay',
'America/Argentina/ComodRivadavia',
'Etc/GMT+1',
'Africa/Bissau',
'Atlantic/South_Georgia',
'America/Shiprock',
'Africa/Niamey',
'Asia/Novosibirsk',
'Asia/Tehran',
'America/Whitehorse',
'Asia/Colombo',
'Australia/Hobart',
'Europe/Riga',
'Etc/GMT+4',
'Africa/Dakar',
'Pacific/Rarotonga',
'Africa/Khartoum',
'America/Curacao',
'Africa/Ouagadougou',
'Africa/Bangui',
'Pacific/Kiritimati',
'Antarctica/Palmer',
'America/Jamaica',
'NZ',
'Etc/GMT-2',
'US/Central',
'CST6CDT',
'Etc/UCT',
'Asia/Urumqi',
'America/Edmonton',
'America/Montreal',
'Pacific/Pitcairn',
'Iran',
'Asia/Khandyga',
'Asia/Ashkhabad',
'Asia/Ho_Chi_Minh',
'America/North_Dakota/Center',
'Africa/Harare',
'Europe/Athens',
'Australia/Victoria',
'America/Jujuy',
'America/Atikokan',
'Africa/Kampala',
'America/Yakutat',
'Mexico/General',
'Atlantic/Stanley',
'Europe/Vienna',
'Africa/Sao_Tome',
'America/Anchorage',
'Europe/Moscow',
'Asia/Damascus',
'Asia/Irkutsk',
'Etc/GMT-7',
'Etc/GMT-9',
'Africa/Libreville',
'Asia/Karachi',
'America/Costa_Rica',
'Africa/Brazzaville',
'Asia/Aqtau',
'Asia/Seoul',
'America/Argentina/Tucuman',
'Asia/Ulaanbaatar',
'Pacific/Funafuti',
'Asia/Srednekolymsk',
'Europe/Madrid',
'Africa/Tripoli',
'Pacific/Norfolk',
'Etc/GMT+2',
'Asia/Qatar',
'W-SU',
'Pacific/Niue',
'Antarctica/Rothera',
'Asia/Katmandu',
'Europe/Volgograd',
'Asia/Anadyr',
'Australia/Melbourne',
'Asia/Baghdad',
'Asia/Oral',
'Etc/GMT-11',
'Pacific/Kosrae',
'Atlantic/Madeira',
'America/New_York',
'Pacific/Gambier',
'Australia/Sydney',
'America/Glace_Bay',
'Etc/GMT-8',
'Africa/Abidjan',
'Europe/Monaco',
'America/Rosario',
'Etc/Greenwich',
'Europe/Sofia',
'Portugal',
'Africa/Cairo',
'Asia/Dushanbe',
'Navajo',
'America/Resolute',
'Europe/Tallinn',
'Africa/Nouakchott',
'US/Michigan',
'Pacific/Port_Moresby',
'America/Merida',
'America/Nipigon',
'Pacific/Nauru',
'America/Argentina/Buenos_Aires',
'Asia/Thimbu',
'Indian/Mauritius',
'Europe/Helsinki',
'Pacific/Truk',
'Asia/Saigon',
'Antarctica/Mawson',
'Asia/Kamchatka',
'Europe/Belgrade',
'Pacific/Wallis',
'Pacific/Fakaofo',
'Africa/Luanda',
'Universal',
'Pacific/Tahiti',
'Asia/Choibalsan',
'Indian/Maldives',
'Australia/Brisbane',
'Asia/Aden',
'America/Indiana/Vincennes',
'Etc/GMT-6',
'Europe/Simferopol',
'Etc/GMT+7',
'America/Recife',
'America/Kentucky/Louisville',
'Canada/Eastern',
'America/Miquelon',
'America/Montserrat'
"""
