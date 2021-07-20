* Step 1: Build the docker image

```bash
docker build -t flask-app -f Dockerfile .
```

* Step 2: Run the docker compose file

```bash
docker compose up -d
```

* Step 3: Create a new user

```bash
http POST http://localhost:5000/users/create first_name=John last_name=Doe email=john@doe.com
```

* Step 4: Query a single user

```bash
http GET http://localhost:5000/users/read/1 
```


* Step 5: Update a single user

```bash
http PUT http://localhost:5000/users/update first_name=Jane last_name=Doe email=jane@doe.com
```

* Step 6: Delete a user

```bash
http DELETE http://localhost:5000/users/read/1 
```
