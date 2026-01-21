from locust import HttpUser, task, between

class MCPUser(HttpUser):
    wait_time = between(0.1, 0.5)  # Simulate rapid calls

    @task
    def test_mcp_call(self):
        self.client.post("/agent/call")