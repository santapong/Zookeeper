from confluent_kafka.admin import AdminClient, NewTopic

admin_conf = {'bootstrap.servers': 'localhost:9092'}
admin_client = AdminClient(admin_conf)

topic_name = 'test-topicss'
num_partitions = 1
replication_factor = 1

new_topic = NewTopic(topic=topic_name,
                     num_partitions=num_partitions,
                     replication_factor=replication_factor)

# Create topic
fs = admin_client.create_topics([new_topic])

# Wait for operation to finish
for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print(f"Topic '{topic}' created successfully.")
    except Exception as e:
        print(f"Failed to create topic '{topic}': {e}")
