import test_pb2
import test
import pandas as pd
import test_pb2
from flask import Flask, request #import main Flask class and request object
import pandas as pd
import json
import sys
query=test_pb2.query()
out=test_pb2.out()


app = Flask(__name__) #create the Flask app

@app.route('/ping')
def ping():
    query.rfw_id = int(request.args.get('rfw_id')) #if key doesn't exist, returns None
    query.benchmark_type = request.args['benchmark_type'] #if key doesn't exist, returns a 400, bad request error
    query.workload_metric = request.args.get('workload_metric')
    query.batch_unit = int(request.args.get('batch_unit')) #if key doesn't exist, returns None
    query.batch_id = int(request.args['batch_id']) #if key doesn't exist, returns a 400, bad request error
    query.batch_size = int(request.args.get('batch_size'))

    #for serialization
    quotesFile = open("quotes.txt", "wb")
    quotesFile.write(query.SerializeToString())

    #for de-serialization
    with open('quotes.txt', 'r') as infile:
        for line in infile:
            query.ParseFromString(line)
    
   
    data=pd.read_csv("Workload_Data/"+query.benchmark_type+".csv")
   
    mul=abs(query.batch_id-query.batch_size)
    out.samples_requested=(mul+1)*query.batch_unit    
    dat=[]
    for i in range(0,(mul+1)):
        data1=pd.read_csv("Workload_Data/"+query.benchmark_type+".csv")
        data2=pd.DataFrame(data1[query.workload_metric])
        dam=data2.iloc[i*query.batch_unit:(i+1)*query.batch_unit]
        #dam=dam.to_json()
        dat.append(dam)
        i+=1
        query.batch_id+=1
        #print("batch_id:",query.batch_id,)

    #print(dat)
    out.last_batch_id=query.batch_id-1
    print(dat)
    

    return '''<h1>rfw_id: {}</h1>
              <h1>last_batch_id: {}</h1>
              <h1>samples_requested: {}</h1>
              <table>{}
              '''.format(query.rfw_id, out.last_batch_id, out.samples_requested,dat)



if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
