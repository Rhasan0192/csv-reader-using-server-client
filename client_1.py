rfw_id=input("rfw_id: ")
benchmark_type=input("Enter file to read from DVD-testing, DVD-training, NDBench-training, NDBench-training : ")
workload_metric=input("Enter which metric you want:")
batch_unit=int(input("batch_unit: "))
batch_id=int(input("batch_id: "))
batch_size=int(input("batch_size: "))
print ("use link below")
print("http://127.0.0.1:5000/ping?rfw_id={}&benchmark_type={}&workload_metric={}&batch_unit={}&batch_id={}&batch_size={}".format(rfw_id,benchmark_type,workload_metric,batch_unit,batch_id,batch_size))

#uncomment for running on web server
#print("http://3.233.7.227:80/query?rfw_id={}&benchmark_type={}&workload_metric={}&batch_unit={}&batch_id={}&batch_size={}".format(rfw_id,benchmark_type,workload_metric,batch_unit,batch_id,batch_size))
