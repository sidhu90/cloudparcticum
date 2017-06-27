import boto.ec2
import argparse
from subprocess import call
import paramiko

parser = argparse.ArgumentParser()
parser.add_argument("--image", help="image name")
parser.add_argument("--key_name", help="keyname for the instance")
parser.add_argument("--instance_type", help="instance type for the instance")
parser.add_argument("--security_group", help="security group for the instance")
parser.add_argument("--region", help="region")
parser.add_argument("--password", help="mysql password")
args=parser.parse_args()

try:
    conn = boto.ec2.connect_to_region(args.region)
    createVM=conn.run_instances(
        args.image,
        key_name=args.key_name,
        instance_type=args.instance_type,
        security_groups=[args.security_group]
    )
    instance = reservation.instances[0]
except:
    print("unable to connect to the EC2")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key=paramiko.RSAKey.from_private_key_file("/opt/mykey.pem")
try:
    client.connect(instance.ip_address, username='centos', pkey=key)
    stdin , stdout, stderr = client.exec_command('sh install.sh '+password)
    print stdout.read()
    print( "Errors")
    print stderr.read()
except:
    print("unable to connect to the VM")
