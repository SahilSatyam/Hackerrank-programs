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
