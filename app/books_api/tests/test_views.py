from rest_framework.test import APIRequestFactory
from books_api import views


class TestBookListAPIView:

    def setup(self):
        self.factory = APIRequestFactory()
        self.view = views.BookListAPIView.as_view()

    def test_response_code(self, book_list_api_url, book_db):
        request = self.factory.get(book_list_api_url)
        response = self.view(request)

        assert response.status_code == 200

    def test_response_data(self, book_list_api_url, book_db, book_serializer_return):
        request = self.factory.get(book_list_api_url)
        response = self.view(request)

        assert response.data == [book_serializer_return]
