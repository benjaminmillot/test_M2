# Set up a Local Galaxy server instance

## Download the source code
You need to have git installed to proceed (sudo apt-get install git):

```
git clone https://github.com/galaxyproject/galaxy
```

You can also download the 
[zip](https://github.com/galaxyproject/galaxy/archive/master.zip)
or [tar/gz](https://github.com/galaxyproject/galaxy/archive/master.tar.gz)
archives, but it is **not recommended** since there is no way to keep Galaxy
up to date this way.

## Install dependencies and start a local instance
Run the following command in a terminal to check/install the dependencies if
needed and start a local instance of Galaxy

```
sh run.sh
```

## Access Galaxy over the network
From this point can access Galaxy locally at http://localhost:8080/

You can also acces Galaxy over the network.
To do so, edit the `config/galaxy.ini` file and change the host setting to:

```
host = 0.0.0.0
```

It is possible that `config/galaxy.ini` is not present in the folder.
If so, you can either create a new one from scratch and add the previous line
or copy the sample and edit it from there:

```
cp config/galaxy.ini.sample config/galaxy.ini
```

You can also access and parametrize Galaxy by registering and logging in the
[web server](https://usegalaxy.org/)
