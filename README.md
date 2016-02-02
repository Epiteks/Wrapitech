# Epitech JSON API

**https://epitech-api.herokuapp.com/**  
[The API is available on GitHub](https://github.com/lupin012345/epitech-api-public)  

Every route returns **200** in case of success ,**40X** in case of client error and 5XX in case of server error.  
Every <font color="red">red</font> parameter is mandatory. The parameters mustn't be formated in JSON and must be in the query's body.  
The server always returns JSON responses.  

<font color="red">**Our google.group@epitech.eu mail address is not working anymore since the mail server's migration. Please mail me at api@lp1.eu if you have some questions.**</font>  

* * *

**Connect on the API and get a token**  
**/login POST**  

<pre>Parameters
<font color="red">"login":"amsell_j",
"password":"password42"</font> 
</pre>

<pre>Response
{"token":"42"}
</pre>

* * *

**Get informations displayed on login**

**/infos POST**

<pre>Parameters
 <font color="red">"token":"42"</font> 
</pre>

<pre>Response
{
	"ip":"10.41.X.X",
	"board":
		{
			"projets":{},
			"notes":{},
			"susies":{},
			"activites":{},
			"modules":{},
			"stages":{},
			"tickets":{}
		}
	"history":
		{
			{
				"title":"You have joined the activity Corrections Evaluation - M\u00e9mo professionnel<\/a>"
				"user":
					{ 
						"picture":"https:\/\/cdn.local.epitech.eu\/userprofil\/amsell_j.bmp", 
						"title":"Jeremie Amsellem", 
						"url":"\/user\/amsell_j\/" 
					}, 
				"content":"Remember to validate your presence with your token View other registered people ...<\/a>", "date":"2014-11-23 18:24:42", 
				"id":"6557808", 
				"visible":"1", 
				"id_activite":"173479", 
				"class":"register"
			}
		}
		"infos":
			{ 
				"id":"42891", 
				"login":"amsell_j", 
				"title":"Jeremie Amsellem", 
				"email":null, "internal_email":"amsell_j@epitech.eu", 
				"lastname":"Amsellem", 
				"firstname":"Jeremie", 
				"userinfo":{}
				"referent_used":true, 
				"picture":"amsell_j.bmp", 
				"picture_fun":null, 
				"email_referent":"email@email.com", 
				"pass_referent":"0000", 
				"promo":2017, 
				"semester":5, 
				"uid":110268, 
				"gid":32017, 
				"location":"FR\/PAR", 
				"documents":"vrac\/amsell_j", 
				"userdocs":"\/u\/epitech_2017\/amsell_j\/cu", 
				"shell":"\/usr\/site\/bin\/shell", 
				"netsoul":null, 
				"close":false, 
				"close_reason":null, 
				"ctime":"2013-12-06 04:00:56", 
				"mtime":"2013-11-22 18:00:05", 
				"comment":null, 
				"id_promo":"279", 
				"id_history":"144269", 
				"course_code":"bachelor\/classic", 
				"school_code":"epitech", 
				"school_title":"epitech", 
				"old_id_promo":"244,250,255,254,272", 
				"old_id_location":"4", 
				"rights":{ }, 
				"invited":true, 
				"studentyear":3, 
				"admin":false,
		}
		"current":
		{ 
			"active_log":"0.9069", 
			"credits_min":"120", 
			"credits_norm":"120", 
			"credits_obj":"150", 
			"nslog_min":"15", 
			"nslog_norm":"25", 
			"semester_code":"B5", 
			"semester_num":"5", 
			"achieved":124, 
			"failed":63, 
			"inprogress":39 
		} 
}
</pre>

* * *

**Planning**

**/planning GET**

<pre>Parameters
<font color="red">"token":"42",
"start":"YYYY-MM-DD",
"end":"YYYY-MM-DD"</font> 
</pre>

<pre>Response
{
	"prof_inst":
		[
			{
				"type": "user", 
				"login": "login_x", 
				"title": "FirstName LastName", 
				"picture": "https://cdn.local.epitech.eu/userprofil/login_x.bmp"
			}, 
			{
				"type": "user", 
				"login": "prof_a", 
				"title": "Prof Name"
			}
		], 
	"title": null, 
	"rdv_indiv_registered": null, 
	"allowed_planning_end": "2013-12-15 00:00:00", "
	nb_group": 6, 
	"start": "2013-12-10 14:00:00", 
	"register_month": null, 
	"allowed_planning_start": "2013-12-09 00:00:00", 
	"project": false, 
	"event_registered": null, 
	"total_students_registered": 22, 
	"allow_register": false, 
	"codemodule": "B-PRO-050", 
	"rdv_group_registered": null, 
	"semester": 1, 
	"type_code": "tp", 
	"is_rdv": "0", 
	"allow_token": false, 
	"titlemodule": "B1 - French Writing Skills", 
	"in_more_than_one_month": true, 
	"acti_title": "R\u00e9diger une lettre pro convaincante (Partie 2)", 
	"instance_location": "FR/PAR", 
	"nb_hours": "01:30:00", 
	"register_prof": null, 
	"nb_max_students_projet": null, 
	"room": {"type": "salle_machine", "seats": 50, "code": "FR/PAR/Voltaire/SM-21"}, 
	"codeacti": "acti-133142", 
	"codeevent": "event-140648", 
	"codeinstance": "PAR-1-1", 
	"dates": null, 
	"register_student": true, 
	"type_title": "TD", 
	"num_event": 3, 
	"end": "2013-12-10 15:30:00", 
	"scolaryear": "2013", 
	"module_registered": false, 
	"past": true, 
	"module_available": false
	}, 
}
</pre>

* * *

**Susies**

**/susies GET**

<pre>Parameters
<font color="red">"token":"42",        
"start":"YYYY-MM-DD",
"end":"YYYY-MM-DD"</font> 
"get":"all" or "free" or "registered"
</pre>

<pre>Reponse : see /planning
</pre>

* * *

**Get a susie**

**/susie GET**

<pre>Parameters
<font color="red">"token":"42",
"id":6301,
"calendar_id":42</font> 
</pre>

<pre>Response
{
    "id": 6301,
    "id_calendar": 587,
    "location": null,
    "type_room": null,
    "type": "culture",
    "start": "2013-11-01 14:45:00",
    "end": "2013-11-01 16:45:00",
    "title": "Education Systems",
    "description": "We will discuss public versus private school, the effect education has on future opportunities, as well as our own personal experiences with the education system.",
    "nb_place": 10,
    "color": "#1E7FCB",
    "confirm_owner": true,
    "confirm_maker": true,
    "id_owner": "58054",
    "id_maker": "81459164",
    "rating_event": "3.1429",
    "rating_student": "4.0000",
    "duration": "02:00:00",
    "logins": [
        {
            "login": "amsell_j",
            "picture": "https://cdn.local.epitech.eu/userprofil/amsell_j.bmp",
            "title": "Jérémie Amsellem",
            "promo": "2017",
            "present": "present"
        }
    ],
    "rights": {
        "planning_visible": 1
    },
    "calendar": {
        "id": 587,
        "start": "2013-09-29",
        "end": "2014-08-09",
        "type": "susie",
        "registered": true
    },
    "owner": {
        "login": "prof_x",
        "title": "Prof Name",
        "picture": "https://cdn.local.epitech.eu/userprofil/commentview/prof_x.jpg"
    },
    "maker": {
        "login": "prof_x",
        "title": "Prof Name"
    }
}
</pre>

* * *

**Subscribe to a susie**

**/susie POST**

<pre>Parameters
<font color="red">"token":"42",
"id":6301,
"calendar_id":42</font> 
</pre>

* * *

**Unsuscribe to a susie**

**/susie DELETE**

<pre>Parameters
<font color="red">"token":"42",
"id":6301,
"calendar_id":42</font> 
</pre>

* * *

**Get projects**

**/projects GET**

<pre><font color="red">"token":"42",</font> 
</pre>

<pre>Response
[
    {
        "codemodule": "B-GPR-560",
        "project": "Projet : EIP B5",
        "end_acti": "2015-02-28 00:00:00",
        "acti_title": "EIP - Choix du sujet",
        "num_event": null,
        "seats": null,
        "title_module": "B5 - EIP Validation",
        "begin_event": null,
        "rights": [
            "student"
        ],
        "num": "1",
        "begin_acti": "2014-09-01 00:00:00",
        "scolaryear": "2014",
        "code_location": "FR",
        "end_event": null,
        "type_acti_code": "proj",
        "codeacti": "acti-166505",
        "info_creneau": null,
        "registered": 1,
        "codeinstance": "FR-5-1",
        "type_acti": "Projet"
    },
    {
        "codemodule": "B-GPR-360-0",
        "project": "Projet : projet libre informatique",
        "end_acti": "2015-06-07 23:42:00",
        "acti_title": "Projet Libre Local",
        "num_event": null,
        "seats": null,
        "title_module": "B6 - Student's IT Project",
        "begin_event": null,
        "rights": [
            "student"
        ],
        "num": "0",
        "begin_acti": "2014-09-07 00:00:00",
        "scolaryear": "2014",
        "code_location": "PAR",
        "end_event": null,
        "type_acti_code": "proj",
        "codeacti": "acti-167486",
        "info_creneau": null,
        "registered": 0,
        "codeinstance": "PAR-6-1",
        "type_acti": "Projets"
    },
    {
        "codemodule": "B-GPR-560",
        "project": "Projet : B5 EIP en instance de validation TECH",
        "end_acti": "2014-12-28 00:00:00",
        "acti_title": "Suivi technique sur le sujet proposé",
        "num_event": null,
        "seats": null,
        "title_module": "B5 - EIP Validation",
        "begin_event": null,
        "rights": [
            "student"
        ],
        "num": "1",
        "begin_acti": "2014-10-31 00:00:00",
        "scolaryear": "2014",
        "code_location": "FR",
        "end_event": null,
        "type_acti_code": "rdv",
        "codeacti": "acti-166507",
        "info_creneau": null,
        "registered": 0,
        "codeinstance": "FR-5-1",
        "type_acti": "Suivis"
    }
]
</pre>

* * *

**Get project**

**/project GET**

<pre><font color="red">"token":"42",  
"scolaryear":2014,
"codemodule":"B-GPR-360-0",
"codeinstance":"PAR-6-1",
"codeacti":"acti-167486"</font> 
</pre>

<pre>Response
{
   "scolaryear":"2014",
   "codemodule":"B-GPR-360-0",
   "codeinstance":"PAR-6-1",
   "codeacti":"acti-167486",
   "instance_location":"FR\/PAR",
   "module_title":"B6 - Student's IT Project",
   "id_activite":"167486",
   "project_title":"projet libre informatique",
   "type_title":"Projets",
   "type_code":"proj",
   "register":false,
   "register_by_bloc":"0",
   "register_prof":"0",
   "nb_min":5,
   "nb_max":7,
   "begin":"2014-09-07 00:00:00",
   "end":"2015-06-07 23:42:00",
   "end_register":null,
   "deadline":null,
   "is_rdv":false,
   "instance_allowed":"1",
   "title":"Projet Libre Local",
   "description":"",
   "closed":true,
   "over":189,
   "over_deadline":null,
   "date_access":true,
   "instance_registered":"1",
   "user_project_status":null,
   "note":null,
   "root_slug":"projets\/B-GPR-360-1\/Projet-libre-Informatique",
   "forum_path":"\/Modules-Epitech\/Semestre-5\/B5-Proj-Libre-Informatique-local\/projet-libre-informatique",
   "slug":null,
   "call_ihk":"0",
   "nb_notes":null,
   "user_project_master":null,
   "user_project_code":null,
   "user_project_title":null,
   "registered_instance":230,
   "registered":[

   ],
   "notregistered":[
      {
         "login":"amsell_j",
         "picture":"https:\/\/cdn.local.epitech.eu\/userprofil\/amsell_j.bmp",
         "title":"Amsellem Jérémie",
         "location":"FR\/PAR",
         "promo":2017,
         "course_code":"bachelor\/classic",
         "grade":"-",
         "cycle":"bachelor",
         "date_ins":"2014-09-17 17:22:02",
         "credits":8,
         "flags":[],
         "semester":"B5"
      },
   ],
   "urls":[
   ]
}
</pre>

* * *

**Suscribe to project**

**/project POST**

<pre><font color="red">"token":"42",  
"scolaryear":2014,
"codemodule":"B-GPR-360-0",
"codeinstance":"PAR-6-1",
"codeacti":"acti-167486"</font> 
</pre>

<pre>Response
 {
  "code":"2-Il-etait-une-fois-FR-0-1-amsell_j",
  "title":"2-Il \u00e9tait une fois... amsell_j",
  "url_repository":null,
  "members":[
    {
      "login":"amsell_j",
      "title":"Jeremie Amsellem",
      "picture":"https:\/\/cdn.local.epitech.eu\/userprofil\/amsell_j.bmp",
      "status":"confirmed",
      "master":true
    }
  ]
}
</pre>

* * *

**Unuscribe to project**pre><font

**/project DELETE**

<pre>Parameters
<font color="red">"token":"42",    
"scolaryear":2014,
"codemodule":"B-GPR-360-0",
"codeinstance":"PAR-6-1",
"codeacti":"acti-167486"</font> 
</pre>

<pre>Response
{
}
</pre>

* * *

**Get project files**

**/project/files GET**

<pre><font color="red">"token":"42",      
"scolaryear":2014,
"codemodule":"B-GPR-360-0",
"codeinstance":"PAR-6-1",
"codeacti":"acti-167486"</font> 
</pre>

<pre>Response
{
	[
		{
		"type":"-",
		"slug":"pfa.pdf",
		"title":"pfa.pdf",
		"secure":true,
		"synchro":false,
		"archive":false,
		"language":"FR",
		"size":277067,
		"ctime":"2014-10-08 13:42:56",
		"mtime":"2014-10-08 13:42:56",
		"mime":"application\/pdf",
		"isLeaf":false,
		"noFolder":false,
		"rights":{
		"ged_read":1,
		"ged_write":1
		},
		"fullpath":"\/module\/2014\/B-GPR-360-0\/PAR-6-1\/acti-167486\/project\/file\/pfa.pdf"
		}
	]
}
</pre>

* * *

**Get user's modules**

**/modules GET**

<pre><font color="red">"token":"42",      
"login":"amsell_j" (Optional)</font> 
</pre>

<pre>Response
{
   modules:[
      {
         "scolaryear":2012,
         "id_user_history":null,
         "codemodule":"B-CPE-042-1",
         "codeinstance":"PAR-1-1",
         "title":"B1 - Piscine - Unix & C Lab Seminar",
         "id_instance":"4879",
         "date_ins":"2012-09-29 22:47:11",
         "cycle":"bachelor",
         "grade":"A",
         "credits":8,
         "flags":"0",
         "barrage":0,
         "instance_id":"4879",
         "module_rating":"188711",
         "semester":1
      },
      {
         "scolaryear":2012,
         "id_user_history":null,
         "codemodule":"G-EPI-007",
         "codeinstance":"PAR-0-1",
         "title":"Conferences",
         "id_instance":"5057",
         "date_ins":"2012-09-29 22:48:49",
         "cycle":"bachelor",
         "grade":"A",
         "credits":1,
         "flags":"0",
         "barrage":4,
         "instance_id":"5057",
         "module_rating":"286810",
         "semester":0
      },
      {
         "scolaryear":2012,
         "id_user_history":null,
         "codemodule":"G-EPI-004",
         "codeinstance":"PAR-0-1",
         "title":"Epitech Promotion",
         "id_instance":"5055",
         "date_ins":"2012-10-01 13:10:01",
         "cycle":"bachelor",
         "grade":"Acquis",
         "credits":0,
         "flags":"0",
         "barrage":64,
         "instance_id":"5055",
         "module_rating":"352492",
         "semester":0
      }
   ]
}
</pre>

* * *

**Get all modules**

**/allmodules GET**

<pre><font color="red">"token":"42",      
"scolaryear":2014,
"location":"FR/PAR" or another location in "FR/BDX","FR/LIL","FR/LYN","FR/MAR","FR/MPL","FR/NCY","FR/NAN","FR/NCE","FR/PAR","FR/REN","FR/STG","FR/TLS"
"course":"bachelor/classic" or "bachelor/tek1ed" or "bachelor/tek2ed"</font> 
</pre>

<pre>Response
{
    "preload": [
        [
            101,
            2014,
            "FR/PAR",
            "bachelor/classic",
            "bachelor"
        ],
        [
            9,
            2014,
            "FR",
            "bachelor/classic",
            "bachelor"
        ],
        [
            54,
            2012,
            "FR/PAR",
            "bachelor/classic",
            "bachelor"
        ],
        [
            3,
            2012,
            "FR",
            "bachelor/classic",
            "bachelor"
        ],
        [
            71,
            2013,
            "FR/PAR",
            "bachelor/classic",
            "bachelor"
        ],
        [
            8,
            2013,
            "FR",
            "bachelor/classic",
            "bachelor"
        ]
    ],
    "items": [
        {
            "id": 10863,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-10-05",
            "end": "2015-06-15",
            "end_register": "2015-01-13",
            "scolaryear": 2014,
            "code": "G-JPN-002",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "1",
            "credits": "2",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "0",
            "title": "Advanced Japanese"
        },
        {
            "id": 9053,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2013-10-17",
            "end": "2014-08-31",
            "end_register": "2013-10-22",
            "scolaryear": 2013,
            "code": "G-EPI-005",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "35",
            "credits": "3",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "Communication and School sales training"
        },
        {
            "id": 10135,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-10-16",
            "end": "2015-06-30",
            "end_register": "2015-06-30",
            "scolaryear": 2014,
            "code": "G-EPI-005",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "35",
            "credits": "3",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "1",
            "title": "Communication and School sales training"
        },
        {
            "id": 9065,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2013-09-08",
            "end": "2014-06-23",
            "end_register": "2014-01-30",
            "scolaryear": 2013,
            "code": "G-EPI-007",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "36",
            "credits": "1",
            "rights": [],
            "status": "fail",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "Conferences"
        },
        {
            "id": 10604,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-09-07",
            "end": "2015-06-22",
            "end_register": "2015-01-29",
            "scolaryear": 2014,
            "code": "G-EPI-007",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "36",
            "credits": "1",
            "rights": [],
            "status": "ongoing",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "1",
            "title": "Conferences"
        },
        {
            "id": 9041,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2013-10-17",
            "end": "2014-08-31",
            "end_register": "2014-08-31",
            "scolaryear": 2013,
            "code": "G-EPI-004",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "96",
            "credits": "0",
            "rights": [],
            "status": "ongoing",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "Epitech Promotion"
        },
        {
            "id": 10123,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-09-21",
            "end": "2015-07-31",
            "end_register": "2015-07-31",
            "scolaryear": 2014,
            "code": "G-EPI-004",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "96",
            "credits": "0",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "1",
            "title": "Epitech Promotion"
        },
        {
            "id": 10865,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-09-08",
            "end": "2015-06-29",
            "end_register": "2015-01-13",
            "scolaryear": 2014,
            "code": "G-EPI-022",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "32",
            "credits": "3",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "0",
            "title": "High-School Students Coaching"
        },
        {
            "id": 11276,
            "title_cn": "Hub Events",
            "semester": 0,
            "num": "1",
            "begin": "2014-09-01",
            "end": "2015-08-31",
            "end_register": "2015-08-31",
            "scolaryear": 2014,
            "code": "G-HUB-010",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "1",
            "credits": "0",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "1",
            "title": "Hub Events"
        },
        {
            "id": 10861,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-10-26",
            "end": "2015-06-29",
            "end_register": "2015-01-13",
            "scolaryear": 2014,
            "code": "G-EPI-024",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "3",
            "credits": "2",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "0",
            "title": "Improvisation"
        },
        {
            "id": 10862,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-10-05",
            "end": "2015-06-15",
            "end_register": "2015-01-13",
            "scolaryear": 2014,
            "code": "G-JPN-001",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "1",
            "credits": "2",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "0",
            "title": "Japanese - beginners"
        },
        {
            "id": 9726,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-01-13",
            "end": "2014-02-09",
            "end_register": "2014-01-24",
            "scolaryear": 2013,
            "code": "G-PRO-010",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "3",
            "credits": "4",
            "rights": [],
            "status": "fail",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "Project Week"
        },
        {
            "id": 11148,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-10-27",
            "end": "2014-12-15",
            "end_register": "2014-11-09",
            "scolaryear": 2014,
            "code": "G-CUI-450",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "1",
            "credits": "2",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "0",
            "title": "S0 - Culture Informatique : Lightning talk"
        },
        {
            "id": 11178,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-10-01",
            "end": "2015-07-31",
            "end_register": "2015-07-31",
            "scolaryear": 2014,
            "code": "G-DRT-010",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "0",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "1",
            "title": "S0 - Do the right team"
        },
        {
            "id": 9089,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2013-08-11",
            "end": "2014-06-24",
            "end_register": "2014-02-28",
            "scolaryear": 2013,
            "code": "G-EPI-010",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "34",
            "credits": "2",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "Sport"
        },
        {
            "id": 10159,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-08-10",
            "end": "2015-06-23",
            "end_register": "2015-01-13",
            "scolaryear": 2014,
            "code": "G-EPI-010",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "34",
            "credits": "2",
            "rights": [],
            "status": "ongoing",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "Sport"
        },
        {
            "id": 9719,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2013-12-01",
            "end": "2014-06-30",
            "end_register": "2014-05-01",
            "scolaryear": 2013,
            "code": "G-CAF-001",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "97",
            "credits": "0",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "Un café epi c'est tout"
        },
        {
            "id": 10949,
            "title_cn": null,
            "semester": 0,
            "num": "1",
            "begin": "2014-08-10",
            "end": "2015-07-31",
            "end_register": "2015-07-31",
            "scolaryear": 2014,
            "code": "G-CAF-001",
            "codeinstance": "PAR-0-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "97",
            "credits": "0",
            "rights": [],
            "status": "ongoing",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "1",
            "title": "Un café epi c'est tout"
        },
        {
            "id": 8980,
            "title_cn": null,
            "semester": 3,
            "num": "1",
            "begin": "2013-08-16",
            "end": "2014-03-08",
            "end_register": "2014-01-14",
            "scolaryear": 2013,
            "code": "B-PRO-250",
            "codeinstance": "PAR-3-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "20",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B3 - 1st Internship Evaluation"
        },
        {
            "id": 8944,
            "title_cn": null,
            "semester": 3,
            "num": "1",
            "begin": "2013-09-08",
            "end": "2014-02-21",
            "end_register": "2014-01-14",
            "scolaryear": 2013,
            "code": "B-ADM-250",
            "codeinstance": "PAR-3-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "192",
            "credits": "0",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B3 - Administrative meetings"
        },
        {
            "id": 8932,
            "title_cn": null,
            "semester": 3,
            "num": "1",
            "begin": "2013-12-22",
            "end": "2014-02-10",
            "end_register": "2014-01-08",
            "scolaryear": 2013,
            "code": "B-PAV-442-1",
            "codeinstance": "PAR-3-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "4",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B3 - C++ programming – Pool"
        },
        {
            "id": 8968,
            "title_cn": null,
            "semester": 3,
            "num": "1",
            "begin": "2013-09-29",
            "end": "2014-02-17",
            "end_register": "2014-01-14",
            "scolaryear": 2013,
            "code": "B-ANG-284-1",
            "codeinstance": "PAR-3-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "8",
            "credits": "0",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B3&4 - English - E-Toeic - 650"
        },
        {
            "id": 8832,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-01-19",
            "end": "2014-08-18",
            "end_register": "2014-06-16",
            "scolaryear": 2013,
            "code": "B-ADM-350",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "192",
            "credits": "0",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - Administrative Meetings"
        },
        {
            "id": 8748,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-01-19",
            "end": "2014-06-30",
            "end_register": "2014-02-28",
            "scolaryear": 2013,
            "code": "B-PAV-330",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "7",
            "rights": [],
            "status": "fail",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - C++ Programming"
        },
        {
            "id": 8736,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-02-02",
            "end": "2014-07-21",
            "end_register": "2014-03-23",
            "scolaryear": 2013,
            "code": "B-CPE-330",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "8",
            "credits": "2",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - C- Programming - Individual evaluation tests"
        },
        {
            "id": 8760,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-01-20",
            "end": "2014-07-28",
            "end_register": "2014-02-16",
            "scolaryear": 2013,
            "code": "B-GPR-350",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "0",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - Coaching and Group Managment"
        },
        {
            "id": 8808,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-01-12",
            "end": "2014-07-06",
            "end_register": "2014-03-16",
            "scolaryear": 2013,
            "code": "B-CPE-360",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "1",
            "rights": [],
            "status": "fail",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - Elementary Programming - Special Project"
        },
        {
            "id": 9709,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-01-19",
            "end": "2014-07-14",
            "end_register": "2014-03-23",
            "scolaryear": 2013,
            "code": "B-ANG-350",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "3",
            "rights": [],
            "status": "fail",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - English"
        },
        {
            "id": 9702,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-01-30",
            "end": "2014-03-23",
            "end_register": "2014-03-10",
            "scolaryear": 2013,
            "code": "B-PRO-360",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "4",
            "credits": "2",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - French Writing Skills"
        },
        {
            "id": 9865,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-07-01",
            "end": "2014-08-31",
            "end_register": "2014-07-01",
            "scolaryear": 2013,
            "code": "B-ADM-342",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "2",
            "credits": "0",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - Remedial Session"
        },
        {
            "id": 8904,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-01-26",
            "end": "2014-06-30",
            "end_register": "2014-03-16",
            "scolaryear": 2013,
            "code": "B-BDD-350",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "4",
            "credits": "1",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - SQL Individual tests"
        },
        {
            "id": 8700,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-05-25",
            "end": "2014-07-21",
            "end_register": "2014-06-22",
            "scolaryear": 2013,
            "code": "B-ADS-350",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "2",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - System Administration"
        },
        {
            "id": 8880,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-01-12",
            "end": "2014-08-04",
            "end_register": "2014-02-16",
            "scolaryear": 2013,
            "code": "B-PSU-330",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "12",
            "rights": [],
            "status": "fail",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - Unix System Programming"
        },
        {
            "id": 8856,
            "title_cn": null,
            "semester": 4,
            "num": "1",
            "begin": "2014-01-19",
            "end": "2014-03-10",
            "end_register": "2014-02-02",
            "scolaryear": 2013,
            "code": "B-WEB-275",
            "codeinstance": "PAR-4-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "258",
            "credits": "5",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B4 - Web Security - 1"
        },
        {
            "id": 10111,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2015-04-13",
            "end": "2015-04-18",
            "end_register": "2015-04-13",
            "scolaryear": 2014,
            "code": "B-PRO-599",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "4",
            "credits": "0",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B - French Writing Skills validation"
        },
        {
            "id": 10587,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-09-08",
            "end": "2015-01-18",
            "end_register": "2014-11-09",
            "scolaryear": 2014,
            "code": "B-PAV-590",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "5",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - .Net I"
        },
        {
            "id": 10696,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-08-27",
            "end": "2014-09-15",
            "end_register": "2014-09-02",
            "scolaryear": 2014,
            "code": "B-MOO-430",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "2",
            "credits": "4",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - Adaptation training"
        },
        {
            "id": 10485,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-08-27",
            "end": "2015-02-01",
            "end_register": "2014-09-28",
            "scolaryear": 2014,
            "code": "B-ADM-450",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "192",
            "credits": "0",
            "rights": [],
            "status": "ongoing",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - Administrative Meetings"
        },
        {
            "id": 10425,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-08-24",
            "end": "2014-11-09",
            "end_register": "2014-09-28",
            "scolaryear": 2014,
            "code": "B-PRO-550",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "4",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - Business Management"
        },
        {
            "id": 10076,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-09-08",
            "end": "2015-03-22",
            "end_register": "2014-09-21",
            "scolaryear": 2014,
            "code": "B-ANG-450-1",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "128",
            "credits": "3",
            "rights": [],
            "status": "ongoing",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - English"
        },
        {
            "id": 10708,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-08-19",
            "end": "2015-03-08",
            "end_register": "2014-09-28",
            "scolaryear": 2014,
            "code": "B-ANG-484-1",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "8",
            "credits": "0",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - English - E-Toeic - 750"
        },
        {
            "id": 9979,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-08-31",
            "end": "2015-01-19",
            "end_register": "2014-09-28",
            "scolaryear": 2014,
            "code": "B-PRO-460",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "4",
            "credits": "2",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - French Writing Skills"
        },
        {
            "id": 10557,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-09-01",
            "end": "2014-11-23",
            "end_register": "2014-10-14",
            "scolaryear": 2014,
            "code": "B-CSI-450",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "3",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - Information System Conception - UML"
        },
        {
            "id": 10351,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2015-01-15",
            "end": "2015-03-22",
            "end_register": "2015-01-31",
            "scolaryear": 2014,
            "code": "B-PRO-480",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "1",
            "rights": [],
            "status": "ongoing",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "1",
            "title": "B5 - Law & Privacy on Internet"
        },
        {
            "id": 10929,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-09-07",
            "end": "2015-02-23",
            "end_register": "2014-10-05",
            "scolaryear": 2014,
            "code": "B-NET-460-1",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "8",
            "credits": "1",
            "rights": [],
            "status": "valid",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - Network individual tests"
        },
        {
            "id": 10832,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-09-08",
            "end": "2015-03-30",
            "end_register": "2014-12-21",
            "scolaryear": 2014,
            "code": "B-PRO-525",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "2",
            "credits": "8",
            "rights": [],
            "status": "ongoing",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - Part-Time Job"
        },
        {
            "id": 11172,
            "title_cn": null,
            "semester": 5,
            "num": "1",
            "begin": "2014-09-08",
            "end": "2015-01-25",
            "end_register": "2014-12-28",
            "scolaryear": 2014,
            "code": "B-ADS-450",
            "codeinstance": "PAR-5-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "2",
            "rights": [],
            "status": "ongoing",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B5 - Unix System Administration"
        },
        {
            "id": 11238,
            "title_cn": null,
            "semester": 5,
            "num": "2",
            "begin": "2015-01-13",
            "end": "2015-04-01",
            "end_register": "2015-02-08",
            "scolaryear": 2014,
            "code": "B-PAV-530-2",
            "codeinstance": "PAR-5-2",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "7",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "1",
            "title": "B5 - C++ Programming - Apache Project"
        },
        {
            "id": 10638,
            "title_cn": null,
            "semester": 6,
            "num": "1",
            "begin": "2015-01-31",
            "end": "2015-07-31",
            "end_register": "2015-03-30",
            "scolaryear": 2014,
            "code": "B-PRO-575",
            "codeinstance": "PAR-6-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "4",
            "credits": "20",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "0",
            "title": "B6 - 2nd Internship Evaluation"
        },
        {
            "id": 10497,
            "title_cn": null,
            "semester": 6,
            "num": "1",
            "begin": "2015-02-02",
            "end": "2015-05-17",
            "end_register": "2015-02-15",
            "scolaryear": 2014,
            "code": "B-ADM-550",
            "codeinstance": "PAR-6-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "64",
            "credits": "0",
            "rights": [],
            "status": "notregistered",
            "waiting_grades": null,
            "active_promo": "1",
            "open": "0",
            "title": "B6 - Administrative Meetings"
        },
        {
            "id": 10800,
            "title_cn": null,
            "semester": 6,
            "num": "1",
            "begin": "2014-08-17",
            "end": "2015-03-31",
            "end_register": "2014-10-25",
            "scolaryear": 2014,
            "code": "B-GPR-360-0",
            "codeinstance": "PAR-6-1",
            "location_title": "Paris",
            "instance_location": "FR/PAR",
            "flags": "0",
            "credits": "8",
            "rights": [],
            "status": "ongoing",
            "waiting_grades": null,
            "active_promo": "0",
            "open": "0",
            "title": "B6 - Student's IT Project"
        }
    ]
}
</pre>

* * *

**Get module**

**/module GET**

<pre><font color="red">"token":"42",        
"scolaryear":2014,
"codemodule":"B-GPR-360-0",
"codeinstance":"PAR-6-1"</font> 
</pre>

<pre>Response
{
    "scolaryear": "2014",
    "codemodule": "B-PAV-560",
    "codeinstance": "PAR-5-1",
    "semester": 5,
    "title": "B5 - Java I Programming",
    "begin": "2014-09-01",
    "end_register": "2014-10-19",
    "end": "2015-01-25",
    "past": "0",
    "closed": "1",
    "opened": "1",
    "user_credits": null,
    "credits": 5,
    "description": "This course theme is an introduction the Java world and the different possibilities this language offers.\nThis course provides a basic approach to three major development axes in Java:\n- Java application\n- Web with Java, discovery of JSP, introduction to TomCat\n- Mobile development, introduction to Android\n\nEach project lasts between three and four weeks, and will be introduced by an introduction week, with guests experts in their domain.\n",
    "competence": "+ Technical skills\n- Knowledge and basic understanding of the various environnements Java executes in.\n- Syntax and specificities of the Java language.",
    "flags": "0",
    "instance_flags": "0",
    "max_ins": null,
    "instance_location": "FR/PAR",
    "hidden": "0",
    "old_acl_backup": null,
    "resp": [
        {
            "type": "user",
            "login": "teacher_n",
            "title": "Teacher Name",
            "picture": "https://cdn.local.epitech.eu/userprofil/teacher_n.bmp"
        }
    ],
    "assistant": [
        {
            "type": "group",
            "login": "Koala_Java",
            "title": "Koala Java",
            "picture": null
        }
    ],
    "rights": null,
    "template_resp": [
        {
            "type": "user",
            "login": "teacher_n",
            "title": "Teacher Norm",
            "picture": "https://cdn.local.epitech.eu/userprofil/teacher_n.bmp"
        }
    ],
    "allow_register": "100580",
    "student_registered": 0,
    "student_grade": null,
    "student_credits": 0,
    "color": null,
    "student_flags": null,
    "current_resp": false,
    "activites": 
    [
        {
            "codeacti": "acti-164635",
            "call_ihk": "1",
            "slug": "JAVAweb",
            "instance_location": "FR/PAR",
            "module_title": "B5 - Java I Programming",
            "title": "[PROJET] JWeb",
            "description": "Développement d'un site web en utilisant les technos JSP et Tomcat",
            "type_title": "Mini-Projets",
            "type_code": "proj",
            "begin": "2014-12-01 00:00:00",
            "start": "2014-12-01 00:00:00",
            "end_register": "2014-12-14 00:00:00",
            "deadline": "2014-12-28 23:42:00",
            "end": "2014-12-28 23:42:00",
            "nb_hours": null,
            "nb_group": 1,
            "num": 2,
            "register": "0",
            "register_by_bloc": "0",
            "register_prof": "0",
            "title_location_type": null,
            "is_projet": true,
            "id_projet": "782",
            "project_title": "JWeb",
            "is_note": false,
            "nb_notes": null,
            "is_blocins": false,
            "rdv_status": "close",
            "id_bareme": null,
            "title_bareme": null,
            "archive": "0",
            "hash_elearning": null,
            "ged_node_adm": null,
            "nb_planified": null,
            "note": null,
            "project": null,
            "events": []
          }
        ]
      }

    </pre>

* * *

**Subscribe to module**

**/module POST**

<pre><font color="red">"token":"42",        
"scolaryear":2014,
"codemodule":"B-GPR-360-0",
"codeinstance":"PAR-6-1"</font> 
</pre>

<pre>Response
{
  "login":"amsell_j"
}
</pre>

* * *

**Unsubscribe to module**

**/module DELETE**

<pre><font color="red">"token":"42",        
"scolaryear":2014,
"codemodule":"B-GPR-360-0",
"codeinstance":"PAR-6-1"</font> 
</pre>

<pre>Response
{
  "login":"amsell_j"
}
</pre>

* * *

**Get event**

**/event GET**

<pre>Parameters
<font color="red">"token":"42",
"scolaryear":2014,
"codemodule":"B-PAV-590",
"codeinstance":"NAN-5-1",
"codeacti":"acti-164603"
"codeevent":"event-173408"</font> 
</pre>

<pre>  Response
  {
  "scolaryear":"2014",
  "codemodule":"B-PRO-460",
  "codeinstance":"PAR-5-1",
  "codeacti":"acti-173186",
  "codeevent":"event-174707",
  "semester":5,
  "instance_location":"FR\/PAR",
  "module_title":"B5 - French Writing Skills",
  "acti_title":"(Copie)",
  "acti_description":"",
  "type_title":"Corrections",
  "type_code":"tp",
  "allowed_planning_start":"2015-01-06 13:00:00",
  "allowed_planning_end":"2015-01-11 00:00:00",
  "nb_hours":"01:30:00",
  "nb_group":2,
  "has_exam_subject":false,
  "begin":"2015-01-06 15:30:00",
  "start":"2015-01-06 15:30:00",
  "end":"2015-01-06 17:00:00",
  "num_event":1,
  "title":null,
  "description":null,
  "nb_registered":0,
  "id_dir":null,
  "room":{
    "code":"FR\/PAR\/Voltaire\/SM-24-25",
    "type":"salle_machine",
    "seats":180
  },
  "seats":130,
  "desc_webservice":"The information which you require to create an exam \/ a day of 
  Piscine \/ a rush.",
  "name_bocal":"tp-PRO 2015-01-06 15:30:00-Paris"
}

</pre>

* * *

**Subscribe to event**

**/event POST**

<pre><font color="red">"token":"42",
"scolaryear":2014,
"codemodule":"B-PAV-590",
"codeinstance":"NAN-5-1",
"codeacti":"acti-164603"
"codeevent":"event-173408"</font> 
</pre>

<pre>  Response
  {
  }
</pre>

* * *

**Unsubscribe to event**

**/event DELETE**

<pre><font color="red">"token":"42",
"scolaryear":2014,
"codemodule":"B-PAV-590",
"codeinstance":"NAN-5-1",
"codeacti":"acti-164603"
"codeevent":"event-173408"</font> 
</pre>

<pre>  Response
  {
  }
</pre>

* * *

**Get marks**

**/marks GET**

<pre><font color="red">"token":"42",</font> 
</pre>

<pre>Response
{
   notes:[
      {
         "scolaryear":2014,
         "codemodule":"B-MOO-430",
         "titlemodule":"B5 - Adaptation training",
         "codeinstance":"PAR-5-1",
         "codeacti":"acti-166312",
         "title":"(Copie) (Copie)",
         "date":"2014-09-06 17:19:38",
         "correcteur":"teacher_n",
         "final_note":0,
         "comment":""
      },
      {
         "scolaryear":2014,
         "codemodule":"B-MOO-430",
         "titlemodule":"B5 - Adaptation training",
         "codeinstance":"PAR-5-1",
         "codeacti":"acti-166313",
         "title":"[D06] Projet de fin de piscine",
         "date":"2014-09-29 12:27:16",
         "correcteur":"teacher_n",
         "final_note":15,
         "comment":""
      },
      {
         "scolaryear":2014,
         "codemodule":"B-NET-460-1",
         "titlemodule":"B5 - Network individual tests",
         "codeinstance":"PAR-5-1",
         "codeacti":"acti-169132",
         "title":"Exam r\u00e9seau 1",
         "date":"2014-09-29 16:08:32",
         "correcteur":"teacher_n",
         "final_note":5.75,
         "comment":"voir les traces pour plus de details"
      },
   ]
}
</pre>

* * *

**Get messages**

**/messages GET**

<pre><font color="red">"token":"42",</font> 
</pre>

<pre>Response
[
    {
        "title": "Mark added for activity Soutenance intermediaire du projet UML : diagramme de classes, interfaces et diagrammes de séquence. (Soutenance) by Teacher Name.",
        "user": {
            "picture": null,
            "title": "Teacher Name",
            "url": "/intra/user/teacher_n/"
        },
        "content": "Please verify; contact the person who corrected you if you believe that there is an error",
        "date": "2014-11-29 01:39:35"
    }
]
</pre>

* * *

**Get alerts**

**/alerts GET**

<pre><font color="red">"token":"42",</font> 
</pre>

<pre>Response
[ 
	{ 
		"title":"Your login time is insufficient (3)." 
	} 
]
</pre>

* * *

**Get photo url**

**/photo GET**

<pre><font color="red">"token":"42",
"login":"login_x"</font> 
</pre>

<pre>Response
{
	"url": "https://cdn.local.epitech.eu/userprofil/profilview/amsell_j.jpg"
}
</pre>

* * *

**Validate token**

**/token POST**

<pre> <font color="red">"token":"42",        
"scolaryear":2014,
"codemodule":"B-GPR-360-0",
"codeinstance":"PAR-6-1",
"codeacti":"acti-167486",
"codeevent":"event-177013"
"tokenvalidationcode":"00000000"</font> 
</pre>

* * *

**Get a list of students**

**/trombi GET**

<pre><font color="red">"token":"42",        
"year":2014,
"location":"FR/PAR" or another location in "FR/BDX","FR/LIL","FR/LYN","FR/MAR","FR/MPL","FR/NCY","FR/NAN","FR/NCE","FR/PAR","FR/REN","FR/STG","FR/TLS"</font> 
"course":"bachelor/classic" or "bachelor/tek1ed" or "bachelor/tek2ed"
"promo":"tek3"
"offset":43
</pre>

<pre>Response
{
    "items": [
        {
            "title": "FirstName LastName",
            "login": "firstn_l",
            "nom": "LastName",
            "prenom": "FirstName",
            "picture": "https://cdn.local.epitech.eu/userprofil/trombiview/firstn_l.jpg",
            "location": "FR/PAR"
        },
    }
</pre>

* * *

**Get a student's information**

**/user GET**

<pre><font color="red">"token":"42",
"user":"login_x"</font> 
</pre>

<pre>Response
{
    "login": "amsell_j",
    "title": "Jeremie Amsellem",
    "internal_email": "amsell_j@epitech.eu",
    "lastname": "Amsellem",
    "firstname": "Jeremie",
    "userinfo": {
        "email": {
            "value": "mail@lupin.me",
            "adm": true,
            "public": true
        },
        "job": {
            "value": "Hub - Domaine embarqué",
            "adm": true,
            "public": true
        },
        "website": {
            "value": "lupin.me",
            "public": true
        },
        "poste": {
            "value": "GoogleGroup Epitech",
            "adm": true,
            "public": true
        }
    },
    "referent_used": true,
    "picture": "https://cdn.local.epitech.eu/userprofil/profilview/amsell_j.jpg",
    "picture_fun": null,
    "promo": 2017,
    "semester": 6,
    "uid": 110268,
    "gid": 32017,
    "location": "FR/PAR",
    "documents": "vrac/amsell_j",
    "userdocs": "/u/epitech_2017/amsell_j/cu",
    "shell": "/usr/site/bin/shell",
    "close": false,
    "ctime": "2013-12-06 04:00:56",
    "mtime": "2013-11-22 18:00:05",
    "id_promo": "291",
    "id_history": "152018",
    "course_code": "bachelor/classic",
    "school_code": "epitech",
    "school_title": "epitech",
    "old_id_promo": "244,250,255,254,272,279",
    "old_id_location": "4",
    "rights": {},
    "invited": true,
    "studentyear": 3,
    "admin": false,
    "editable": true,
    "groups": [
        {
            "title": "Paris",
            "name": "Paris",
            "count": 18640
        }
    ],
    "events": [],
    "credits": 139,
    "gpa": [
        {
            "gpa": "4.0",
            "cycle": "bachelor"
        }
    ],
    "averageGPA": [
        {
            "cycle": "bachelor",
            "gpa_average": "1.47"
        }
    ],
    "spice": {
        "available_spice": "30",
        "consumed_spice": 360
    },
    "nsstat": {
        "active": 0.8,
        "idle": 0,
        "out_active": 1.6,
        "out_idle": 0,
        "nslog_norm": 25
    }
</pre>

* * *

**Get a student's documents**

**/user/files GET**

<pre><font color="red">"token":"42",
"user":"login_x"</font> 
</pre>

<pre>Response
[
    {
        "type": "-",
        "slug": "Bulletin_2013_STG-2-junger_m-fr.pdf",
        "title": "Bulletin_2013_STG-2-junger_m-fr.pdf",
        "secure": true,
        "synchro": false,
        "archive": false,
        "language": "FR",
        "size": 23221,
        "ctime": "2014-07-22 11:22:35",
        "mtime": "2014-07-22 11:22:35",
        "mime": "application\/pdf",
        "isLeaf": false,
        "noFolder": false,
        "rights": {
            "ged_read": 1
        },
        "modifier": {
            "login": "brosiu_l",
            "title": "lionel brosius",
            "picture": "https:\/\/cdn.local.epitech.eu\/userprofil\/brosiu_l.bmp"
        },
        "fullpath": "\/user\/junger_m\/document\/Bulletin_2013_STG-2-junger_m-fr.pdf"
    },
    {
        "type": "-",
        "slug": "Bulletin_2013_STG_Bachelor-junger_m-fr.pdf",
        "title": "Bulletin_2013_STG_Bachelor-junger_m-fr.pdf",
        "secure": true,
        "synchro": false,
        "archive": false,
        "language": "FR",
        "size": 21041,
        "ctime": "2014-02-25 09:03:03",
        "mtime": "2014-02-25 09:03:03",
        "mime": "application\/pdf",
        "isLeaf": false,
        "noFolder": false,
        "rights": {
            "ged_read": 1
        },
        "modifier": {
            "login": "brosiu_l",
            "title": "lionel brosius",
            "picture": "https:\/\/cdn.local.epitech.eu\/userprofil\/brosiu_l.bmp"
        },
        "fullpath": "\/user\/junger_m\/document\/Bulletin_2013_STG_Bachelor-junger_m-fr.pdf"
    },
    {
        "type": "-",
        "slug": "Bulletin_2014_STG-3-junger_m-fr.pdf",
        "title": "Bulletin_2014_STG-3-junger_m-fr.pdf",
        "secure": true,
        "synchro": false,
        "archive": false,
        "language": "FR",
        "size": 18846,
        "ctime": "2015-02-26 18:37:48",
        "mtime": "2015-02-26 18:37:48",
        "mime": "application\/pdf",
        "isLeaf": false,
        "noFolder": false,
        "rights": {
            "ged_read": 1
        },
        "modifier": {
            "login": "gailla_b",
            "title": "benjamin gaillard",
            "picture": "https:\/\/cdn.local.epitech.eu\/userprofil\/gailla_b.bmp"
        },
        "fullpath": "\/user\/junger_m\/document\/Bulletin_2014_STG-3-junger_m-fr.pdf"
    },
    {
        "type": "-",
        "slug": "Bulletin_2014_STG-4-junger_m-fr.pdf",
        "title": "Bulletin_2014_STG-4-junger_m-fr.pdf",
        "secure": true,
        "synchro": false,
        "archive": false,
        "language": "FR",
        "size": 21137,
        "ctime": "2015-07-31 19:16:20",
        "mtime": "2015-07-31 19:16:20",
        "mime": "application\/pdf",
        "isLeaf": false,
        "noFolder": false,
        "rights": {
            "ged_read": 1
        },
        "modifier": {
            "login": "gailla_b",
            "title": "benjamin gaillard",
            "picture": "https:\/\/cdn.local.epitech.eu\/userprofil\/gailla_b.bmp"
        },
        "fullpath": "\/user\/junger_m\/document\/Bulletin_2014_STG-4-junger_m-fr.pdf"
    },
    {
        "type": "-",
        "slug": "Convention-Stage-junger_m-FR-tech_1.pdf",
        "title": "Convention Stage junger_m FR-tech_1.pdf",
        "secure": true,
        "synchro": false,
        "archive": false,
        "language": "FR",
        "size": 68846,
        "ctime": "2014-05-15 07:55:20",
        "mtime": "2014-05-15 07:55:20",
        "mime": "application\/pdf",
        "isLeaf": false,
        "noFolder": false,
        "rights": {
            "ged_read": 1
        },
        "modifier": {
            "login": "clauss_m",
            "title": "melanie clauss",
            "picture": "https:\/\/cdn.local.epitech.eu\/userprofil\/clauss_m.bmp"
        },
        "fullpath": "\/user\/junger_m\/document\/Convention-Stage-junger_m-FR-tech_1.pdf"
    }
]
</pre>

</pre>