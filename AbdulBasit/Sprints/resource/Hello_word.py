def lambda_handler(event,context):                                         #we have define the lambda_handler function and pass two parameter
    return 'Hello {} {}!'.format(event['first_name'],event['last_name'])   #this Line will return the first name and last name to the lambda handlwer function