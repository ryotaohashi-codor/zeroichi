from django.test import TestCase, Client

# Create your tests here.

c = Client()
response = c.get('/')
response.status_code
print(response.content)