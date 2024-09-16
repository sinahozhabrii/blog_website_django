from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your tests here.
class Test_Post(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.post1 = Post.objects.create(
            author= self.user1,
            text = 'this is a test post1',
            title = 'title1',
            status= Post.STATUS_CHOICES[0],
        )
        self.post2 = Post.objects.create(
            author= self.user1,
            text = 'this is a test post2',
            title = 'title2',
            status= Post.STATUS_CHOICES[1],
        )

    def test_post_list_veiw_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_name(self):
        response = self.client.get(reverse('post_deatail', args = [self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_veiw_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_title_text(self):
        response = self.client.get(reverse('post_deatail', args = [self.post1.id]))
        self.assertContains(response,self.post1.title)
        self.assertContains(response,self.post1.text)

    def test_post_list_title_text(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_if_post_id_not_exist_show_404(self):
        response = self.client.get(reverse('post_deatail', args = [999]))
        self.assertEqual(response.status_code, 404)

    def test_if_pub_show_and_drft_dont_show(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response,self.post2.title)
