# import pytest,Book
# from library import reader

# @pytest.fixture
# def new_entity_factory():
#     def new_reader(name,contact="1230",address="1234",password="1234"):
#         reader1=reader(name,contact,address,password)
#         return reader1
#     return new_reader

# @pytest.fixture
# def create_reader(new_entity_factory):
#     return new_entity_factory("rohit")