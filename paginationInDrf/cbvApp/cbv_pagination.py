from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 2 #Default page Size
    page_size_query_param = 'page_size' #when you want to change the name of page_size_query_param
    max_page_size = 10
    page_query_param = 'page' #when you want to change the name of page_query_param