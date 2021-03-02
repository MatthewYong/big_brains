from django.test import TestCase
from .models import Blog
from django.contrib.auth.models import User


class TestBlogsView(TestCase):

    def test_get_all_blogs(self):
        """
        A test to prove that the view gets all the blogs
        from the model and returns to the template
        """
        response = self.client.get('/blogs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blogs.html')

    def test_get_blog(self):
        """
        A test to prove that the view gets a specific blog
        and returns it to its own template
        """
        create_user = User.objects.create(pk=1)
        user_pk = User.objects.get(pk=1)

        blog = Blog.objects.create(
            author=user_pk,
            title='New Toy',
            author_friendly='12.95',
            description='Funny',
            article='New Toy',
            image_url='New Toy',
        )
        response = self.client.get(f'/blogs/{blog.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blog_detail.html')
