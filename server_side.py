import test_pb2
import test
import pandas as pd
import test_pb2
from flask import Flask, request #import main Flask class and request object
import pandas as pd
import json
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
    data=pd.read_csv("Workload_Data/"+query.benchmark_type+".csv")
    #query.batch_unit=int(query.batch_unit)
    #query.batch_size=int(query.batch_size)
    #query.batch_id=int(query.batch_id)
    c=len(data[query.workload_metric])
    out.samples_requested=query.batch_unit*query.batch_size
    
 
    for i in range(0,query.batch_size):
        data1=pd.read_csv("Workload_Data/"+query.benchmark_type+".csv",nrows=query.batch_unit)
        data2=pd.DataFrame(data1[query.workload_metric])
        #data2=data2.to_json()
        #data2=json.dumps(data2)
    
        query.batch_id+=1
    out.last_batch_id=query.batch_id-1

    return '''<h1>rfw_id: {}</h1>
              <h1>last_batch_id: {}</h1>
              <h1>samples_requested: {}
              '''.format(query.rfw_id, out.last_batch_id, out.samples_requested)



if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000



 
#def ping(rfw_id,test_pb2.query.benchmark_type,test_pb2.query.workload_metric,test_pb2.query.batch_unit,test_pb2.query.batch_id,test_pb2.query.batch_size):
'''   data=pd.read_csv("Workload_Data/"+test_pb2.query.benchmark_type+".csv")
 
c=len(data[test_pb2.query.workload_metric])
test_pb2.out.samples_requested=test_pb2.query.batch_unit*test_pb2.query.batch_size
test_pb2.query.rfw_id=test_pb2.out.rfw_id
 
for i in range(0,test_pb2.query.batch_size):
    data1=pd.read_csv("Workload_Data/"+test_pb2.query.benchmark_type+".csv",nrows=test_pb2.query.batch_unit)
    data2=pd.DataFrame(data1[test_pb2.query.workload_metric])
    #print("batch_id:",test_pb2.query.batch_id)
    #print(data2)
    test_pb2.query.batch_id+=1
test_pb2.out.last_batch_id=test_pb2.query.batch_id-1

print("rfw_id:",test_pb2.query.rfw_id)
print("last_batch_id:",test_pb2.out.last_batch_id)
print("samples_requested:",test_pb2.out.samples_requested)
return (rfw_id,)
 
    #return(test_pb.out.rfw_id,test_pb.out.last_batch_id,test_pb.out.samples_requested)
'''
