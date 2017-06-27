check=`yum list installed | grep mysql`
if [$check == ""]
then
    yum install -y mysql-server
    mysqladmin -u root password $1
    echo "mysql installed properly"

