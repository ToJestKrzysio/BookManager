import pytest
from django.urls import reverse


class TestBookListView:

    @pytest.mark.parametrize("url", ["/books/list/", reverse("books:book_list")])
    def test_response_status_code(self, client, db, url):
        response = client.get(url)
        assert response.status_code == 200

    def test_response_template(self, book_list_response):
        template_names = [template.name for template in book_list_response.templates]
        assert "base.html" in template_names
        assert "books/book_list.html" in template_names


class TestBookCreateView:

    def setup(self):
        self.url = reverse("books:book_create")

    @pytest.mark.parametrize("url", ["/books/create/", reverse("books:book_create")])
    def test_response_status_code(self, client, db, url):
        response = client.get(url)
        assert response.status_code == 200

    def test_response_template(self, client, db):
        response = client.get(self.url)
        template_names = [template.name for template in response.templates]
        assert "base.html" in template_names
        assert "books/book_create.html" in template_names


class TestBookUpdateView:

    def setup(self):
        self.url = reverse("books:book_update", kwargs={"pk": 1})

    @pytest.mark.parametrize("url",
                             ["/books/update/1", reverse("books:book_update", kwargs={"pk": 1})])
    def test_response_status_code(self, client, db_book_1, url):
        response = client.get(url)
        assert response.status_code == 200

    def test_response_template(self, client, db, db_book_1):
        response = client.get(self.url)
        template_names = [template.name for template in response.templates]
        assert "base.html" in template_names
        assert "books/book_update.html" in template_names


class TestAuthorCreateView:

    def setup(self):
        self.url = reverse("books:author_create")

    @pytest.mark.parametrize("url", ["/books/create/author/", reverse("books:author_create")])
    def test_response_status_code(self, client, db, url):
        response = client.get(url)
        assert response.status_code == 200

    def test_response_template(self, client, db):
        response = client.get(self.url)
        template_names = [template.name for template in response.templates]
        assert "base.html" in template_names
        assert "books/book_create.html" in template_names


class TestAuthorUpdateView:

    def setup(self):
        self.url = reverse("books:author_update", kwargs={"pk": 1})

    @pytest.mark.parametrize("url",
                             ["/books/update/author/1", reverse("books:author_update", kwargs={"pk": 1})])
    def test_response_status_code(self, client, db_book_1, url):
        response = client.get(url)
        assert response.status_code == 200

    def test_response_template(self, client, db, db_book_1):
        response = client.get(self.url)
        template_names = [template.name for template in response.templates]
        assert "base.html" in template_names
        assert "books/book_update.html" in template_names
