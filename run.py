from flaskblog import create_App
app=create_App()     #no parameter will be passed into this function
if __name__=='__main__':
    app.run(debug=True)
    