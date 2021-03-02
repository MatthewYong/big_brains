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
        create_user = User.objects.create_user(
            username='test_name',
            email='test_email@email.com',
            password=None)

        blog = Blog.objects.create(
            author=create_user,
            title='New Toy',
            author_friendly='12.95',
            description='Funny',
            article='New Toy',
            image_url='New Toy',
        )
        print(blog.id)
        response = self.client.get(f'/blogs/{blog.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blog_detail.html')
