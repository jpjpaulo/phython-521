import boto3

def read_credentials():

    headers, content = None, None
    
    with open('credentials.csv', 'r') as f:
        headers, content = f.readlines()

    dictionary = zip(
        headers.strip().split(','), 
        content.strip().split(',')
    )

    return { 
        k: v for k, v in dictionary
    }

credentials = read_credentials()

opts = {
    'aws_access_key_id': credentials['Access key ID'],
    'aws_secret_access_key': credentials['Secret access key'],
    'region_name': 'us-west-2'
}
ec2 = boto3.Session(**opts).resource('ec2')

ec2.create_instances(
    ImageId='ami-0d8f6eb4f641ef691',
    MinCount=1,
    MaxCount=1,
)