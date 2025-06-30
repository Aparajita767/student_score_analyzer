from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_valid_csv():
    '''
    test valid csv uploads

    returns : status code
              json message
              filename
    '''
    test_file_content = b'Date,Amount\n2023-01-01,100\n2023-01-02,150'

    response = client.post(
        '/upload',
        files={'file':('scores.csv',test_file_content)}
    )
    assert response.status_code == 200
    assert response.json()['message'] == 'File has been successfully uploaded'
    assert response.json()['filename'] == 'scores.csv'

def test_upload_invalid_extension():
    '''
    tests invalid extension
    returns : status_code == 400
    '''
    test_file_content = b'This should fail'

    response = client.post(
        '/upload',
        files={'file': ('badfile.txt', test_file_content)}
    )
    assert response.status_code == 400