from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        print("Starting")
    
    @task
    def index(self):
        reponse = self.client.get("/")
        print(reponse)