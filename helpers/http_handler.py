import allure
import json
import requests
from allure_commons.types import AttachmentType
from pydantic import ValidationError
from helpers.assertions import Assertions


class HTTPHelper:

    @staticmethod
    def attach_response(response: dict) -> None:
        """Attaches the API response to the allure report.

        Args:
            response (dict): The API response as a dictionary.
        """
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)

    @staticmethod
    def validate_response(response_json: dict, model) -> dict:
        """
        Validates the API response against the provided Pydantic model.

        Args:
            response_json (dict): The API response as a dictionary.
            model (BaseModel): The Pydantic model to validate against.

        Returns:
            dict: The validated response as a dictionary.

        Raises:
            Exception: If the API response is incorrect.
        """
        try:
            validated_data = model.model_validate(response_json)
        except ValidationError as e:
            print(e.json())
            raise Exception("API response is incorrect")

        return validated_data.model_dump()


class HTTPHandler(HTTPHelper):

    @staticmethod
    def get(url: str, model, params: dict = None) -> dict:
        """
        Sends a GET request to the specified URL and validates the response.

        Args:
            url (str): The URL to send the GET request to.
            model (BaseModel): The Pydantic model to validate the response against.
            params (dict, optional): The query parameters for the GET request. Defaults to None.

        Returns:
            dict: The validated response as a dictionary.

        Raises:
            Exception: If the response status code is not 200.
        """
        response = requests.get(url=url, params=params)
        Assertions.check_response_is_200(response)
        HTTPHelper.attach_response(response.json())
        return HTTPHelper.validate_response(response.json(), model)

    @staticmethod
    def post(url: str, model, payload: dict, auth: tuple) -> dict:
        """
        Sends a POST request to the specified URL with the provided payload and validates the response.

        Args:
            url (str): The URL to send the POST request to.
            model (BaseModel): The Pydantic model to validate the response against.
            payload (dict): The payload for the POST request.
            auth (tuple): The authentication credentials for the request.

        Returns:
            dict: The validated response as a dictionary.

        Raises:
            Exception: If the response status code is not 200 or 201.
        """
        response = requests.post(url=url, json=payload, auth=auth, verify=False)
        Assertions.check_response_is_200_or_201(response)
        HTTPHelper.attach_response(response.json())
        return HTTPHelper.validate_response(response.json(), model)

    @staticmethod
    def delete(url: str, model, auth: tuple) -> dict:
        """
        Sends a DELETE request to the specified URL and validates the response.

        Args:
            url (str): The URL to send the DELETE request to.
            model (BaseModel): The Pydantic model to validate the response against.
            auth (tuple): The authentication credentials for the request.

        Returns:
            dict: The validated response as a dictionary.

        Raises:
            Exception: If the response status code is not 200.
        """
        response = requests.delete(url=url, auth=auth, verify=False)
        Assertions.check_response_is_200(response)
        HTTPHelper.attach_response(response.json())
        return HTTPHelper.validate_response(response.json(), model)

    @staticmethod
    def double_delete(url: str, auth: tuple):
        """Sends second DELETE request to the specified URL and validates status code is 404"""
        response = requests.delete(url=url, auth=auth, verify=False)
        Assertions.check_response_is_404(response)
        return response
