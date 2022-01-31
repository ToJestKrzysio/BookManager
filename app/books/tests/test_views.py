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
