import boto3
import boto3.session

# Create your own session
my_s3_session = boto3.session.Session(region_name='ap-northeast-1', profile_name='[replace_your_aws_profile_name]' )
# Now we can create low-level clients or resource clients from our custom session

s3 = my_s3_session.client('s3')
responses3 = s3.list_buckets()
print(responses3)