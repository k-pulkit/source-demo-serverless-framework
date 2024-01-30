import faker
import uuid
import boto3
import dotenv, os, json, time, sys

basepath = os.path.dirname(os.path.abspath(__file__))
print(dotenv.load_dotenv(os.path.join(basepath, ".env")))

fake = faker.Faker()
stream_name = os.getenv("STREAM_NAME")
assert stream_name is not None
k_client = boto3.client("kinesis",
                        region_name="us-east-1")

print(f"Stream name - {stream_name}")

def gen_row():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "id": str(uuid.uuid4()),
        "phone": fake.phone_number()
    }

if __name__ == '__main__':
    for i in range(20):
        data = gen_row()
        print(data)
        resp = k_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="name"
        )
        print(resp)
        time.sleep(0.5)
        