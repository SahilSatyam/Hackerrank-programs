import os
import pytest
import pandas as pd
from unittest.mock import patch, Mock
from flask import Flask
from utils import config

# Create a test Flask app
@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(data_ownr_info_app)
    return app

# Mocking data for fetch_data_ownr_info_data
mock_response = Mock()
mock_response.content = b'APPL_SYS_ID,APPL_SYS_NM,APPL_SYS_STS_NM,CDO_CD,LOB_CD,DATA_OWNR_SID,ENTL_TX,USER_SID,USER_NM,USER_ROLE_TYPE,ASGN_MTHD,ASGN_STS,CREATOR_SID,CREATED_ON,REMOVER,REMOVED_ON\n1,App1,Active,CDO1,LOB1,DO1,Entl1,U1,User1,Owner,Manual,Active,C1,2023-05-01,,,\n2,App2,Inactive,CDO2,LOB2,DO2,Entl2,U2,User2,Delegate,Automated,Inactive,C2,2023-05-02,R1,2023-05-03'

# Mocking drop_file and update_exec_status_to_waiting
@patch('data_ownr_info_app.drop_file')
@patch('data_ownr_info_app.update_exec_status_to_waiting')
def test_drop_csv_file_to_dropbox(mock_update_exec_status, mock_drop_file, app):
    with app.app_context():
        from data_ownr_info_app import drop_csv_file_to_dropbox
        result, status_code = drop_csv_file_to_dropbox(mock_response, 'DATA_OWNR_INFO')
        assert status_code == 200
        assert 'Successfully dropped data file' in result[0]
        mock_drop_file.assert_called_once()
        mock_update_exec_status.assert_called_once()

# Mocking fetch_data_ownr_info_data and drop_csv_file_to_dropbox
@patch('data_ownr_info_app.fetch_data_ownr_info_data')
@patch('data_ownr_info_app.drop_csv_file_to_dropbox')
def test_drop_data_ownr_info_ingestion_file(mock_drop_csv, mock_fetch_data, app):
    with app.app_context():
        from data_ownr_info_app import drop_data_ownr_info_ingestion_file
        mock_fetch_data.return_value = mock_response
        mock_drop_csv.return_value = ('Success', 200)
        response, status_code = drop_data_ownr_info_ingestion_file()
        assert status_code == 200
        assert response == ('Success', 200)
        mock_fetch_data.assert_called_once()
        mock_drop_csv.assert_called_once_with(mock_response, 'DATA_OWNR_INFO')

def test_dataframe_wrapper(app):
    with app.app_context():
        from data_ownr_info_app import dataframe_wrapper
        data = {'Application ID': ['App1', 'App2'], 'Application Name': ['App Name 1', 'App Name 2'], 'Application State': ['Active', 'Inactive']}
        df = pd.DataFrame(data)
        wrapped_df = dataframe_wrapper(df)
        assert 'CRE_TS' in wrapped_df.columns
        assert wrapped_df.columns.tolist() == DATA_OWNR_INFO_COLUMNS

# Mocking ingest_dataframe_to_db
@patch('data_ownr_info_app.ingest_dataframe_to_db')
def test_ingest_data_ownr_info_data(mock_ingest_df, app):
    with app.app_context():
        from data_ownr_info_app import ingest_data_ownr_info_data
        mock_ingest_df.return_value = 'Success'
        response = ingest_data_ownr_info_data()
        assert response == 'Success'
        mock_ingest_df.assert_called_once_with(TABLE_NAME, 'DATA_OWNR_INFO', dataframe_wrapper, HEADER_ROW)







################################################################################################################################


import pytest
import json
import requests
import pandas as pd
from ingestions.bia import product_summary

from unittest.mock import patch, Mock, MagicMock


class MockedData:
    api_result_success = [{}]
    access_token_success_val = 'assgfjhkhkjlkjhkljl'
    waiting_files_result = [('test.csv',)]

    raw_record = {
            "productIdentifier": "2568",
            "lineOfBusinessName": "Asset & Wealth Management",
            "lineOfBusinessCode": "AWM",
            "subLineOfBusinessName": "Asset Management",
            "subLineOfBusinessCode": "AWM - AM",
            "productLineName": "Client",
            "productName": "Reporting and Information Provision",
            "productDescriptionText": "Watershed Implementation",
            "createDate": "2022-11-28",
            "updateDate": "2023-11-06",
            "endDate": "9999-12-31",
            "areaProducts": [
            {
                    "areaProductIdentifier": "152",
                    "areaProductName": "Pricing",
                    "areaProductMembers": [
                        {
                            "workerFullName": "Sean Smith",
                            "standardIdentifier": "U622759",
                            "userRoleName": "Area Product Owner"
                        }
                    ],
                    "jiraDataSource": {
                        "projectInstanceIdentifier": 2,
                        "projectIdentifier": 30801,
                        "projectKeyIdentifier": "SBC",
                        "projectNameIdentifier": "Small Business Card",
                        "projectInstanceNameIdentifier": "CCB - Shared",
                        "activeProjectIndicator": "true"
                    }
                },
                {
                    "areaProductIdentifier": "151",
                    "areaProductName": "Operations and Client Management",
                    "areaProductMembers": [
                        {
                            "workerFullName": "Nadiyah Jones",
                            "standardIdentifier": "N265740",
                            "userRoleName": "Area Product Owner"
                        }
                    ],
                    "jiraDataSource": {
                        "projectInstanceIdentifier": 2,
                        "projectIdentifier": 30801,
                        "projectKeyIdentifier": "SBC",
                        "projectNameIdentifier": "Small Business Card",
                        "projectInstanceNameIdentifier": "CCB - Shared",
                        "activeProjectIndicator": "true"
                    }
                },
            ],
            "productMembers": [
                {
                    "workerFullName": "Diane Plavecski",
                    "standardIdentifier": "O676471",
                    "userRoleName": "Product Owner"
                },
                {
                    "workerFullName": "Mike Janesch",
                    "standardIdentifier": "L003024",
                    "userRoleName": "Tech Partner"
                }
            ],
            "productArchitecture": {}
        }

    bia_success_resp = {
        "productSummary" : [raw_record],
        "page": 
            {
                'currentPaginationNumber': 0, 
                'moreRecordsIndicator': True, 
                'receivedRecordCount': 1000, 
                'requestedRecordCount': 1000, 
                'totalRecordCount': 1056
            }
    } 
    bia_error_resp = None

    response_df = pd.DataFrame({
    "PROD_ID": ["2568","2568"],
    "LOB_CD": ["AWM","AWM"],
    "LOB_NM": ["Asset & Wealth Management","Asset & Wealth Management"],
    "SUB_LOB": ["Asset Management","Asset Management"],
    "PROD_LINE": ["Client","Client"],
    "PROD_NM": ["Reporting and Information Provision","Reporting and Information Provision"],
    "PROD_DESC": ["Watershed Implementation","Watershed Implementation"],
    "PROD_OWNR_NM": ["Diane Plavecski","Diane Plavecski"],
    "PROD_OWNR_SID": ["O676471","O676471"],
    "TECH_PTNR_NM": ["Mike Janesch","Mike Janesch"],
    "TECH_PTNR_SID": ["L003024","L003024"],
    "AREA_PROD_ID": ["152","152"],
    "AREA_PROD_NM": ["Pricing","Pricing"],
    "AREA_PROD_OWNR_SID": ["U622759","U622759"],
    "AREA_PROD_OWNR_NM": ["Sean Smith","Sean Smith"],
    "PRJCT_ID": [30801,30801],
    "PRJCT_NM": ["Small Business Card","Small Business Card"],
    "DATA_SRC_INSTN_ID": [2,2],
    "DATA_SRC_INSTN_NM": ["CCB - Shared","CCB - Shared"],
    "PRJCT_KEY_ID": ["SBC","SBC"],
    "INGS_PROC_EXEC_ID": ["",""],
    "CRE_TS": ["",""]
    })


class MockRequests:

    def __init__(self, data, status_code):
        """
        :param data:
        :param status_code:
        """
        self.json_data = data
        self.status_code = status_code
        self.text = json.dumps(data)

    def json(self):
        """
        :return:
        """
        return self.json_data


def test_drop_prod_sum_ingestion_file_with_success_response(client, mocker) -> None:
    mocker.patch("ingestions.bia.product_summary.fetch_prod_sum_data",
                 return_value=MockedData.api_result_success)
    mocker.patch("ingestions.bia.product_summary.drop_source_file_to_dropbox",
                 return_value=('Success', 200))
    response = client.get("/drop_prod_sum_ingestion_file")
    assert response.status_code == 200


def test_drop_prod_sum_ingestion_file_with_no_access_token(client, mocker) -> None:
    mocker.patch("ingestions.bia.product_summary.get_access_token",
                 side_effect=[requests.exceptions.ConnectTimeout])
    response = client.get("/drop_prod_sum_ingestion_file")
    assert response.data.decode(
        'utf-8') == 'Authorization error while generating token for BIA API'


def test_drop_prod_sum_ingestion_file_with_bad_api_response(client, mocker) -> None:
    mocker.patch("ingestions.bia.product_summary.get_access_token",
                 return_value=MockedData.access_token_success_val)
    mocker.patch("requests.get", side_effect=[
                 requests.exceptions.ConnectTimeout])
    response = client.get("/drop_prod_sum_ingestion_file")
    assert response.data.decode(
        'utf-8') == 'Encountered error while fetching data from product_summary'


def test_drop_prod_sum_ingestion_file_with_success_api_response(client, mocker) -> None:
    mocker.patch("ingestions.bia.product_summary.get_access_token", return_value=MockedData.access_token_success_val)
    mocker.patch("requests.get",return_value=MockRequests(MockedData.bia_success_resp, 200))
    mocker.patch("ingestions.bia.product_summary.drop_source_file_to_dropbox", return_value=('Success',200))
    response = client.get("/drop_prod_sum_ingestion_file")
    assert response.status_code == 200


def test_drop_prod_sum_ingestion_file_with_error_api_response(client, mocker) -> None:
    mocker.patch("ingestions.bia.product_summary.get_access_token",
                 return_value=MockedData.access_token_success_val)
    mocker.patch("requests.get", return_value=MockRequests(
        MockedData.bia_error_resp, 200))
    mocker.patch("ingestions.bia.product_summary.drop_source_file_to_dropbox",
                 return_value=('Success', 200))
    response = client.get("/drop_prod_sum_ingestion_file")
    assert response.status_code == 400


def test_transform_func_success_response(client, mocker) -> None:
    record = MockedData.raw_record
    exec_id = "exec_id"
    transformed_data = product_summary.transform_prod_sum_rec_to_writable_data(
        record, exec_id)[0]
    print(transformed_data)
    assert transformed_data[0] == record['productIdentifier']


def test_transform_func_error_response(client, mocker) -> None:
    record = MockedData.raw_record
    exec_id = "exec_id"
    del record["lineOfBusinessName"]
    with pytest.raises(KeyError) as e_info:
        transformed_data = product_summary.transform_prod_sum_rec_to_writable_data(
            record, exec_id)


def test_ingest_prod_sum_data_with_success_response(client, mocker) -> None:
    mocker.patch(
        "ingestions.bia.product_summary.ingest_dataframe_to_db", return_value='Success')
    response = client.get("/ingest_prod_sum_data")
    assert response.status_code == 200


def test_prod_sum_ingestion_file_with_exception(client, mocker) -> None:
    mocker.patch("ingestions.bia.product_summary.fetch_prod_sum_data",
                 return_value=MockedData.api_result_success)
    mocker.patch(
        "ingestions.bia.product_summary.drop_source_file_to_dropbox", side_effect=KeyError)
    response = client.get("/drop_prod_sum_ingestion_file")
    assert response.status_code == 400

def test_dataframe_wraper_success_response(client, mocker) -> None:
    df = MockedData.response_df 
    transformed_df = product_summary.dataframe_wrapper(df)
    assert transformed_df.empty == False
########################################################################################################

import unittest
from unittest.mock import patch, MagicMock

# Mock some functions for testing
@patch('utils.get_access_token')
@patch('requests.get')
def mock_fetch_data_ownr_info_data(self, mock_get_access_token, mock_requests_get):
    # Simulate successful access token retrieval
    mock_get_access_token.return_value = 'Bearer some_access_token'
    # Simulate successful API response
    mock_requests_get.return_value = MagicMock(status_code=200)
    return fetch_data_ownr_info_data()

# Mock some functions for testing
@patch('os.path.exists')
@patch('os.mkdir')
@patch('open', create=True)
def mock_drop_csv_file_to_dropbox(self, mock_open, mock_mkdir, mock_exists):
    # Simulate successful folder creation
    mock_exists.return_value = False
    mock_mkdir.return_value = None
    # Simulate successful file opening and writing
    mock_file = mock_open.return_value
    mock_file.write.return_value = None
    return drop_csv_file_to_dropbox(MagicMock(content=b"some_csv_data"), 'DATA_OWNR_INFO')

class TestDataOwnerInfo(unittest.TestCase):

    def test_fetch_data_ownr_info_data_success(self):
        # Patch the function and call it
        response = mock_fetch_data_ownr_info_data(self)
        # Assert successful response with status code 200
        self.assertEqual(response.status_code, 200)

    def test_fetch_data_ownr_info_data_error(self):
        # Patch the function to raise exception during token retrieval
        with patch('utils.get_access_token', side_effect=Exception('Error getting token')):
            response = mock_fetch_data_ownr_info_data(self)
        # Assert error message in response
        self.assertIn('Error while getting token for catalog', response)

    def test_drop_csv_file_to_dropbox_success(self):
        # Patch the function and call it
        result, status_code = mock_drop_csv_file_to_dropbox(self)
        # Assert successful result and status code
        self.assertEqual(result[0], "Successfully dropped data file:")
        self.assertEqual(status_code, 200)

    def test_drop_csv_file_to_dropbox_error(self):
        # Patch the function to raise exception during file open
        with patch('open', side_effect=Exception('Error opening file')):
            result, status_code = mock_drop_csv_file_to_dropbox(self)
        # Assert error message in response
        self.assertIn('File Upload Failed', result[0])
        self.assertEqual(status_code, 500)

# Run the tests
if __name__ == '__main__':
    unittest.main()
