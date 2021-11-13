
<h2>Directory Structure</h2>

```
< root folder>
		├── Gecom
		   ├── components/
		   ├── docs/
		   ├── games/
		   ├── manage.py
		   ├── media/
		   ├── README.md
		   ├── requirements.txt
		   ├── seco/
		   ├── templates/
		   └── users/
```
<hr>
<h3>Directory and files info </h3>

**/seco/**: Main app //settings here, home page content rendered from this app views. 

**/users/**: user  profile and management here, User model from this app is used for signup,registration and login.

**/games/**:  Games  and organisation  create ,update views here.

**/components/**: Component App create update views here.

**/template/**: /registration/, base.html & home.html here.

**/seco/secgen.py**: Generates secret keys

<h3>Keywords </h3>

**components**: here reference to PC parts.

**organisation**: Organisation is created by users , Will act as publisher for games published by user & Vendor in case PC parts allotted by User in store.
 