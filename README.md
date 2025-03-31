# kafka-data-stream

### Before start the process, ensure that zookeeper and kafka process are up and running.

#### Start zookeeper

`nohup bin/zookeeper-server-start.sh config/zookeeper.properties > zookeeper.log 2>&1 &`

`echo $! > zookeeper.pid`

#### Start kafka server

`nohup bin/kafka-server-start.sh config/server.properties > kafka.log 2>&1 &`

`echo $! > kafka.pid`



#### Create topic

`bin/kafka-topics.sh --create --topic market-data --bootstrap-server localhost:9092 --partitions 3 --replication-factor 2`

