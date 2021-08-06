from app import app

# This import is necessary to make sure to 
# tell the flask server where to serve the dash app
import dash_interface1
import dash_interface2

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)