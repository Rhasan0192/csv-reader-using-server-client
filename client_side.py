rfw_id=input("rfw_id: ")
benchmark_type=input("Enter file to read from DVD-testing, DVD-training, NDBench-training, NDBench-training : ")
workload_metric=input("Enter which metric you want:")
batch_unit=int(input("batch_unit: "))
batch_id=int(input("batch_id: "))
batch_size=int(input("batch_size: "))
print ("use link below") 
#when local server is running use this one
print("http://127.0.0.1:5000/ping?rfw_id={}&benchmark_type={}&workload_metric={}&batch_unit={}&batch_id={}&batch_size={}".format(rfw_id,benchmark_type,workload_metric,batch_unit,batch_id,batch_size))

#uncomment the below line to use it for public IP deployed in AWS
#print("http://52.204.14.58:80/ping?rfw_id={}&benchmark_type={}&workload_metric={}&batch_unit={}&batch_id={}&batch_size={}".format(rfw_id,benchmark_type,workload_metric,batch_unit,batch_id,batch_size))
