from rest_framework.test import APIRequestFactory, force_authenticate
from books_api import views
from books import models


class TestBookListAPIView:

    def setup(self):
        self.factory = APIRequestFactory()
        self.view = views.BookListAPIView.as_view()

    def test_response_code(self, book_db):
        request = self.factory.get("")
        response = self.view(request)

        assert response.status_code == 200

    def test_response_data(self, book_db, book_serializer_return):
        request = self.factory.get("")
        response = self.view(request)

        assert response.data == [book_serializer_return]


class TestBookRetrieveUpdateDestroyAPIView:

    def setup(self):
        self.factory = APIRequestFactory()
        self.view = views.BookRetrieveUpdateDestroyAPIView.as_view()

    def test_get_response_code(self, book_db):
        request = self.factory.get("")
        response = self.view(request, pk=book_db.pk)

        assert response.status_code == 200

    def test_get_response_data(self, book_db, book_serializer_return):
        request = self.factory.get("")
        response = self.view(request, pk=book_db.pk)

        assert response.data == book_serializer_return

    def test_put_response_code_unauthenticated(self, book_db, book_serializer_return):
        data = {**book_serializer_return, "title": "42"}
        request = self.factory.put("", data=data)
        response = self.view(request, pk=book_db.pk)

        assert response.status_code == 403

    def test_put_response_code_non_admin(self, book_db, book_serializer_return, user_1):
        data = {**book_serializer_return, "title": "42"}
        request = self.factory.put("", data=data)
        force_authenticate(request, user=user_1)

        response = self.view(request, pk=book_db.pk)
        assert response.status_code == 403

    def test_put_response_code_admin(self, book_db, admin_1, book_serializer_return, author_db):
        data = {**book_serializer_return, "title": "42"}
        request = self.factory.put("", data=data)
        force_authenticate(request, user=admin_1)

        response = self.view(request, pk=book_db.pk)

        assert response.status_code == 200

    def test_put_response_data(self, book_db, admin_1, book_serializer_return, author_db):
        data = {**book_serializer_return, "title": "42"}
        request = self.factory.put("", data=data)
        force_authenticate(request, user=admin_1)

        response = self.view(request, pk=book_db.pk)

        assert response.data["title"] == "42"
        assert models.Book.objects.get(id=1).title == "42"

    def test_patch_response_code_unauthenticated(self, book_db, book_serializer_return):
        request = self.factory.patch("", data={"title": "42"})
        response = self.view(request, pk=book_db.pk)

        assert response.status_code == 403

    def test_patch_response_code_non_admin(self, book_db, book_serializer_return, user_1):
        request = self.factory.patch("", data={"title": "42"})
        force_authenticate(request, user=user_1)

        response = self.view(request, pk=book_db.pk)
        assert response.status_code == 403

    def test_patch_response_code_admin(self, book_db, admin_1, book_serializer_return,
                                       author_db):
        request = self.factory.patch("", data={"title": "42"})
        force_authenticate(request, user=admin_1)

        response = self.view(request, pk=book_db.pk)

        assert response.status_code == 200

    def test_patch_response_data(self, book_db, admin_1, book_serializer_return, author_db):
        request = self.factory.patch("", data={"title": "42"})
        force_authenticate(request, user=admin_1)

        response = self.view(request, pk=book_db.pk)

        assert response.data["title"] == "42"
        assert models.Book.objects.get(id=1).title == "42"
