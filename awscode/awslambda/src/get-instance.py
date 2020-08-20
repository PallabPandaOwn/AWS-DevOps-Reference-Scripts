def lambda_handler(event, context):
    result= x.describe_instances(Filters=[{'Name':tag:Name,'Values': ['Ambassador_PR']}])
    print(result)