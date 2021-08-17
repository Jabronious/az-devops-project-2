from app import app

def test_predict():
    response = app.test_client().post('predict', json={
            "CHAS":{
                "0":0
            },
            "RM":{
                "0":6.575
            },
            "TAX":{
                "0":296.0
            },
            "PTRATIO":{
                "0":15.3
            },
            "B":{
                "0":396.9
            },
            "LSTAT":{
                "0":4.98
            }
        })
    assert response.status_code == 200
    assert response.data == b'{"prediction":[20.35373177134412]}\n'
