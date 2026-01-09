from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Team, User, Activity, Leaderboard, Workout

class ApiSmokeTest(APITestCase):
	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_team_crud(self):
		url = reverse('team-list')
		data = {'name': 'Test Team'}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		team_id = response.data['id']
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.get(reverse('team-detail', args=[team_id]))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		response = self.client.delete(reverse('team-detail', args=[team_id]))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
