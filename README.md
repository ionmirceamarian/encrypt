# License Server

License server used to generate and decrypt client licenses

### Prerequisites

We use python 3 in this project.

### Dockerized App

To start both containers run on the encrypt:

`bash run.sh`

### Start on local

Create Virtual environment - Venv:
`python -m venv venv`

Activate Venv:

`source ./venv/bin/activate`

Then install the dependencies with:

`pip install -r requirements.txt`

#### Running tests (must be done with bash):

`bash test.sh`

#### Running curl tests:

`bash run.sh`


1. Register an user

```
curl --request POST \
  --url http://localhost:5000/register \
  --header 'Content-Type: application/json' \
  --data '{
            "email": "test3@test.com", "password": "test3"
        }'
```
expected output:

```
{
	"error": "",
	"status": true
}
```

2. Login to get the auth token

```
curl --request POST \
  --url http://localhost:5000/login \
  --header 'Content-Type: application/json' \
  --data '{
            "email": "test3@test.com", "password": "test3"
        }'
```

expected output:

```
{
	"auth_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTExMTAyNjMsImlhdCI6MTY1MTA2NzA2Mywic3ViIjoidGVzdDNAdGVzdC5jb20ifQ.q5bR2CoQ_RzsEvDCTMxAMmDRMpvLyWcg5XGeLJG1GNo"
}
```

3. Generate a license

```
curl --request POST \
  --url http://localhost:5000/generate_license \
  --header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTA0ODM2NTUsImlhdCI6MTY1MDQ0MDQ1NSwic3ViIjoidGVzdDNAdGVzdC5jb20ifQ.tgFjL3ZS6n4rAB4GXSgXqm75wPGCoXgtE6pAi6r3w5E' \
  --header 'Content-Type: application/json' \
  --data '
	{"sku": "SKU8091",
	 "pods": 102,
	 "tennat" : "ABC",
	 "name_space": "Done",
	 "cluster": "Arc",
	 "client_name": "Merc", 
	 "exp_date": 365,
   "online": false}'
```

expected output:

```
{
	"encrypted": "gAAAAABiX7kzZwN0fwx1S9H9wwTNDH4P-3VnWulTnElK_FvLfp2Ur_tEHBmuvtF-zYkhBKkc07wvkAB2eycRBVR4cwXUcwZDTUR4wcGR8zNPQmWXWPC50oIn8Ak_fEg2uZObkoeq7XluU9BHapVAp-pTJjZS_InU0Jj1uMzYVi1E0384Fvwoxo6nkd19bIfgICCtR_3-8fjXL-OjAI8qfqT5YqKkfXv70i-aXI2n2sGUpNZsEZbXSb1TteG3mS2Oy32dAE_zoH8t0sz2wpSJ5e8oYaMGVUzSzkRkkpdPgzUc_oj0oiXc17TxePfvyJIzEeKglSoUXIKr",
	"exp_date": "2023-04-20 07:41:39",
	"online": false,
	"sku": "SKU8091",
	"status": true
}
```

4.  Decrypt a license

```
curl --request GET \
  --url http://localhost:5000/decrypt_license \
  --header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTA0ODM2NTUsImlhdCI6MTY1MDQ0MDQ1NSwic3ViIjoidGVzdDNAdGVzdC5jb20ifQ.tgFjL3ZS6n4rAB4GXSgXqm75wPGCoXgtE6pAi6r3w5E' \
  --header 'Content-Type: application/json' \
  --data '
	{"encrypted": "gAAAAABiX7kzZwN0fwx1S9H9wwTNDH4P-3VnWulTnElK_FvLfp2Ur_tEHBmuvtF-zYkhBKkc07wvkAB2eycRBVR4cwXUcwZDTUR4wcGR8zNPQmWXWPC50oIn8Ak_fEg2uZObkoeq7XluU9BHapVAp-pTJjZS_InU0Jj1uMzYVi1E0384Fvwoxo6nkd19bIfgICCtR_3-8fjXL-OjAI8qfqT5YqKkfXv70i-aXI2n2sGUpNZsEZbXSb1TteG3mS2Oy32dAE_zoH8t0sz2wpSJ5e8oYaMGVUzSzkRkkpdPgzUc_oj0oiXc17TxePfvyJIzEeKglSoUXIKr"}'
```

expected output:

```
{
	"sku": "SKU8091",
	"cluster_id": "",
	"pod": 102,
	"tennat": "ABC",
	"name_space": "Done",
	"cluster": "Arc",
	"client_name": "Merc",
	"exp_date": "2023-04-20 07:41:39",
	"online": false
}
```