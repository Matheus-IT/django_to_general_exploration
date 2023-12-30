from django.db import connection, reset_queries
import functools


class HowManyQueries:
    """
    Utility to be used as a context manager to calculate how many queries are
    been made in a code block
    """

    def __enter__(self):
        reset_queries()  # Reset previous queries to measure just the block
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        num_of_queries = len(connection.queries)
        print('-'*50)
        print(f'In this block were made {num_of_queries} queries')
        print('-'*50)


def how_many_queries(func):
    """Utility to calculate number of db queries as a decorator"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        reset_queries()  # Reset previous queries to measure just the block
        value = func(*args, **kwargs)
        num_of_queries = len(connection.queries)

        print('-'*50)
        print(f'In this block were made {num_of_queries} queries')
        print('-'*50)
        return value
    return wrapper