from django.http import HttpResponse
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

    def test_home_page_can_save_a_POST_request(self):
        # request = HttpResponse()
        # request.method = 'POST'
        # request.POST['item_text'] = '신규 작업 아이템'
        #
        # response = home_page(request)
        #
        # self.assertIn('신규 작업 아이템', response.content.decode())
        response = self.client.post('/', data={
            'item_text': '신규 작업 아이템',
            })
        self.assertIn('신규 작업 아이템', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')

    # def test_uses_home_template(self):
    #     response = self.client.get('/')
    #     self.assertTemplateNotUsed(response, 'lists/home.html')
    #
    # def test_can_save_a_POST_request(self):
    #     response = self.client.post('/', data={
    #         'item_text': '신규 작업 아이템',
    #         })
    #     self.assertIn('신규 작업 아이템', response.content.decode())

