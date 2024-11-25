import psutil # this is module is used to get the memory and CPU of the server 
from flask import Flask, render_template # flask framework to create application
#render_template is used to add style in the flask application
app = Flask(__name__) # app is created and given parameter name 

@app.route("/") # path where the application is going to be run */ = home path
def index():
    cpu_percentage = psutil.cpu_percent()
    mem_percentage = psutil.virtual_memory().percent
# using build-in function of psutil for getting memory and CPU of the server

    Message = None
    if cpu_percentage > 80 or mem_percentage > 80:
        Message = "High CPU or Memory Utilization detected . Please scale up"
    #return f"CPU Utilization: {cpu_percentage} and Memory Utilization: {mem_percentage}"
    return render_template("index.html", cpu_metric=cpu_percentage, mem_metric=mem_percentage, message=Message)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # running the application in debug mode and in local host
