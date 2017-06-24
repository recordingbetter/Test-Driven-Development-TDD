from django.http import HttpRequest
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # request = HttpRequest()
        # response = home_page(request)
        # html = response.content.decode('utf8')
        # expected_html = render_to_string('lists/home.html')
        # self.assertEqual(html, expected_html)
        # print(repr(html))

        # django test client 사용
        response = self.client.get('/')
        # django TestCase 클래스가 제공하는 테스트 메소드. 응답을 렌더링하는 데 사용 된 템플릿을 확인
        self.assertTemplateUsed(response, 'lists/home.html')




# class SmokeTest(TestCase):
#
#     def test_bad_math(self):
#         self.assertEqual(1 + 1, 3)
