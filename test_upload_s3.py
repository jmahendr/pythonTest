import upload_s3

def test_get_s3_client():
    assert upload_s3.get_s3_client() == 1
