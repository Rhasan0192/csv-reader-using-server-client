from flask import Flask, request #import main Flask class and request object
import pandas as pd
import json

app = Flask(__name__) #create the Flask app

@app.route('/query')
def query():
    rfw_id = request.args.get('rfw_id') #if key doesn't exist, returns None
    benchmark_type = request.args['benchmark_type'] #if key doesn't exist, returns a 400, bad request error
    workload_metric = request.args.get('workload_metric')
    batch_unit = request.args.get('batch_unit') #if key doesn't exist, returns None
    batch_id = request.args['batch_id'] #if key doesn't exist, returns a 400, bad request error
    batch_size = request.args.get('batch_size')
    data=pd.read_csv("Workload_Data/"+benchmark_type+".csv")
    batch_unit=int(batch_unit)
    batch_size=int(batch_size)
    batch_id=int(batch_id)
    c=len(data[workload_metric])
    mul=abs(batch_id-batch_size)
    samples_requested=(mul+1)*batch_unit
    
    dat=[]
    for i in range(0,(mul+1)):
        data1=pd.read_csv("Workload_Data/"+benchmark_type+".csv")
        data2=pd.DataFrame(data1[workload_metric])
        dam=data2.iloc[i*batch_unit:(i+1)*batch_unit]
        dam=dam.to_json()
        dat.append(dam)
        i+=1
        batch_id+=1
        print("batch_id:",batch_id,)
       # print("i:",i)
    #dat=dat.to_json()
    dat_json=json.dumps(dat)
    #batch_id=batch_id-1
    print(dat_json)
    last_batch_id=batch_id-1

    return '''<h1>rfw_id: {}</h1>
              <h1>last_batch_id: {}</h1>
              <h1>samples_requested: {}</h1>
              <table>{}
              '''.format(rfw_id, last_batch_id, samples_requested,dat_json)



if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000