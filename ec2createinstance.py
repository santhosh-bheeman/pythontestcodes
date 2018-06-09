#!/usr/bin/python
import boto3
ec2 = boto3.resource('ec2')

def create_instance():
        imageid = raw_input("Enter the image id:")
        mincount = int(raw_input("Enter the MIN count:"))
	maxcount = int(raw_input("Enter the MAX count:"))
        instancetype = raw_input("Enter the instancetype:")
	#print type(imageid)
        #ImageId = imageid
        #print ImageId
	#print type(ImageId)
        instance = ec2.create_instances(ImageId=imageid , MinCount=mincount, MaxCount=maxcount, InstanceType=instancetype)
        print("Created Instance:")
	#print instance

#imageid = raw_input("Enter the image id:")

if ___name___ = ___main___:

create_instance()
#list_instance()
#update_instance()
#terminate_instance()
