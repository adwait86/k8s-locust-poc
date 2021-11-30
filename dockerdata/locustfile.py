from locust import HttpUser, TaskSet, task, constant
import uuid


class UserBehaviour(TaskSet):
    @task
    def start_load(self):
        for req in self._prepare_data("banner"):
            self.client.post("", data=req, name="skedEventQueue")


    def _prepare_data(self, org_name: str):
        data_template = ""
        with open('load_data.json') as f:
            data_template = f.read()

        data = []
        for i in range(1, 5000):
            new_uuid = str(uuid.uuid4())
            data.append(data_template.replace('REPLACE_ME', new_uuid).replace("ORG", org_name))
        return data


class MyUser(HttpUser):
    wait_time = constant(0.1)
    tasks = [UserBehaviour]


