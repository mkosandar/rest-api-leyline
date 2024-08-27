# rest-api-leyline
# check the images folder for output 

#deploy using docker-compose
1. Clone the Repository

```
git clone https://github.com/mkosandar/rest-api-leyline.git
cd rest-api-leyline
```
3. Set Up Environment Variables
Create a .env file in the root directory (if it doesn’t exist) and add your environment variables:

```
DATABASE_URL=postgresql://user:password@db:5432/mydb
```
3. Build and Run the Application with Docker Compose
```
docker-compose up -d --build
```
4. Access the Application
API: Open your browser and go to
```
http://localhost:3000.
```
Prometheus Metrics: Visit
```
http://localhost:3000/metrics.
```
Health Check: Visit
```
 http://localhost:3000/health.
```
6. Stop the Application
To stop and remove the containers, run:
```
docker-compose down
```

#if you want to deploy on k8s check the jenkinsfile by triggering jenkinsfile you can run our application on k8s 
