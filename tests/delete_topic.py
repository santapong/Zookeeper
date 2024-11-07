from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import KafkaException
import sys

def delete_kafka_topic(bootstrap_servers, topic_name, timeout=10):
    """
    Deletes a Kafka topic.

    Args:
        bootstrap_servers (str): Kafka broker addresses, e.g., 'localhost:9092'.
        topic_name (str): Name of the topic to delete.
        timeout (int): Timeout in seconds for the delete operation.

    Returns:
        None
    """
    # Configure AdminClient
    admin_conf = {'bootstrap.servers': bootstrap_servers}
    admin_client = AdminClient(admin_conf)

    # Attempt to delete the topic
    try:
        # Initiate topic deletion
        fs = admin_client.delete_topics([topic_name], operation_timeout=timeout)

        # Wait for deletion operation to finish
        for topic, future in fs.items():
            try:
                future.result()  # If successful, no exception is raised
                print(f"Topic '{topic}' deleted successfully.")
            except KafkaException as e:
                print(f"Failed to delete topic '{topic}': {e}")
    except Exception as e:
        print(f"An error occurred while attempting to delete the topic: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Configuration
    bootstrap_servers = 'localhost:9092'  # Replace with your broker(s)
    topic_to_delete = 'test-topicss'        # Replace with the topic you want to delete

    # Delete the topic
    delete_kafka_topic(bootstrap_servers, topic_to_delete)
