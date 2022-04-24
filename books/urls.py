from django.urls import path

from books.views import get_uuids_a, get_uuids_b, get_argument_from_path, get_arguments_from_query, \
    check_http_query_type, get_headers, raise_error_for_fun, AuthorListBaseView, CategoryListTemplateView, BooksListView

urlpatterns = [
    path('uuids-a', get_uuids_a),
    path('uuids-b', get_uuids_b),
    path('path-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    path('query-args', get_arguments_from_query, name="get_from_query"),
    path('query-type', check_http_query_type, name="query_type"),
    path('headers', get_headers, name="get_headers"),
    path('error-raise', raise_error_for_fun, name="get_raise"),
    path('author-list', AuthorListBaseView.as_view(), name="author_list_base_view"),
    path('category-list', CategoryListTemplateView.as_view(), name="category_list"),
    path('books-list', BooksListView.as_view(), name="books-list"),
]
