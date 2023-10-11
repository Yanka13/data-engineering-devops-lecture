from dice_roller.wsgi import app 

def test_flask_home():
    
    app.config["TESTING"] = True 
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200 