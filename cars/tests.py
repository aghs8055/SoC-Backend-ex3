import uuid

import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from cars.models import Car



@pytest.fixture
def cars():
    cars = [
        Car(id=uuid.UUID('f67f3afd-c50a-43de-9554-a8151399909e'), name="car1", brand="Benz", year_built="2020-01-01", mileage=1000),
        Car(id=uuid.UUID('f67f3afd-c50a-43de-9554-a81513999090'), name="car2", brand="BMW", year_built="2020-01-01", mileage=1000),
        Car(id=uuid.UUID('f67f3afd-c50a-43de-9554-a81513999091'), name="car3", brand="Porche", year_built="2020-01-01", mileage=1000),
        Car(id=uuid.UUID('f67f3afd-c50a-43de-9554-a81513999092'), name="car4", brand="Benz", year_built="2020-01-01", mileage=1000),
        Car(id=uuid.UUID('f67f3afd-c50a-43de-9554-a81513999093'), name="car5", brand="BMW", year_built="2020-01-01", mileage=1000),
        Car(id=uuid.UUID('f67f3afd-c50a-43de-9554-a81513999094'), name="car6", brand="Porche", year_built="2020-01-01", mileage=1000),
        Car(id=uuid.UUID('f67f3afd-c50a-43de-9554-a81513999095'), name="car7", brand="Benz", year_built="2020-01-01", mileage=1000),
        Car(id=uuid.UUID('f67f3afd-c50a-43de-9554-a81513999096'), name="car8", brand="BMW", year_built="2020-01-01", mileage=1000),
        Car(id=uuid.UUID('f67f3afd-c50a-43de-9554-a81513999097'), name="car9", brand="Porche", year_built="2020-01-01", mileage=1000),
        Car(id=uuid.UUID('f67f3afd-c50a-43de-9554-a81513999098'), name="car10", brand="Benz", year_built="2020-01-01", mileage=1000),
    ]
    return Car.objects.bulk_create(cars)


@pytest.fixture
def api_client():
    return APIClient()


class TestCarAPI:
    @pytest.mark.django_db()
    def test_given_no_cars_when_create_car_with_valid_data_then_car_created(self, api_client):
        res = api_client.post(reverse("v1.car:car-list"), data={
            "name": "car1",
            "brand": "Benz",
            "year_built": "2020-01-01",
            "mileage": 1000
        })

        assert Car.objects.count() == 1
        assert res.status_code == 201
        assert res.data["name"] == "car1"
        assert res.data["brand"] == "Benz"
        assert res.data["year_built"] == "2020-01-01"
        assert res.data["mileage"] == 1000


    @pytest.mark.django_db()
    def test_given_no_cars_when_create_car_with_invalid_data_then_no_car_created(self, api_client):
        res = api_client.post(reverse("v1.car:car-list"), data={
            "name": "car1",
            "brand": "Benz",
            "year_built": "2020-01-01",
            "mileage": 5
        })

        assert Car.objects.count() == 0
        assert res.status_code == 400
        assert res.data == {"Error: mileage must be greater than or equal to 10"}

    @pytest.mark.django_db()
    def test_given_ten_cars_when_list_cars_then_ten_cars_returned(self, api_client, cars, snapshot):
        res = api_client.get(reverse("v1.car:car-list"))
        assert res.status_code == 200
        snapshot.assert_match(res.content)

    @pytest.mark.django_db()
    def test_given_ten_cars_when_filter_cars_by_brand_then_cars_filtered_by_brand(self, api_client, cars, snapshot):
        res = api_client.get(reverse("v1.car:car-list") + "?brand=Benz")
        assert res.status_code == 200
        snapshot.assert_match(res.content)


    @pytest.mark.django_db()
    def test_given_ten_cars_when_delete_first_car_then_first_car_is_deleted(self, api_client, cars, snapshot):
        assert Car.objects.count() == 10
        res = api_client.delete(reverse("v1.car:car-detail", kwargs={"uuid": cars[0].id}))
        assert res.status_code == 204
        assert Car.objects.count() == 9
        snapshot.assert_match(api_client.get(reverse("v1.car:car-list")).content)

    @pytest.mark.django_db()
    def test_given_ten_cars_when_update_first_car_with_valid_new_name_then_first_car_updated_with_new_name(self, api_client, cars):
        # Put is used to update the whole entity, while patch update an entity partially.
        res = api_client.patch(reverse("v1.car:car-detail", kwargs={"uuid": cars[0].id}), data={"name": "new name"})
        assert res.status_code == 200
        cars[0].refresh_from_db()
        assert cars[0].name == "new name"






