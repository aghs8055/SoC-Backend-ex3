import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient



@pytest.fixture
def cars():
    # TODO : Complete here and create 10 cars
    pass


@pytest.fixture
def api_client():
    return APIClient()






class TestCarAPI:
    @pytest.mark.django_db()
    def test_car_create_api(self):
        # TODO : we need to test the create api for cars
        pass


    @pytest.mark.django_db()
    def test_invalid_car_creation_api(self):
        # TODO : we need to be sure that no car created with invalid data
        # FIXME : You have to review the CarCreateMixin in cars/api/v1/mixins
        pass


    @pytest.mark.django_db()
    def test_car_list_api(self):
        # TODO : we neet to test the list api for cars
        # FIXME : You have to use snapshot and fixture in this test !
        pass


    @pytest.mark.django_db()
    def test_our_filterset_on_brand(self):
        # TODO : we want to test our filterset on brand for the list api
        # FIXME : You have to use snapshot and fixture in this test !
        pass


    @pytest.mark.django_db()
    def test_car_delete_api(self):
        # TODO : we want to test our delete api
        pass


    @pytest.mark.django_db()
    def test_car_update_api(self):
        # TODO : we want to test our update api -> test the patch method not the put !
        # TODO : what is the difference between PUT and PATCH in restful apis ? (comment the answer in here)
        pass






