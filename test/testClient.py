from django.test import Client

c = Client()
response = c.post('/weixin/', {'username': 'john', 'password': 'smith'})
print(response.status_code)
print(response.content)

