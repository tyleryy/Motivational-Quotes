import json
import boto3
import requests

url = "https://motivational-quotes1.p.rapidapi.com/motivation"
headers = {
"content-type": "application/json",
"X-RapidAPI-Key": "edad512b76msh7f91d5247a73cf1p1eddeejsnd6c2e1b86fd2",
"X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com"
}

sns = boto3.client("sns")

topic_arn = "arn:aws:sns:us-east-1:530767186927:MotivationalMessage"
my_topic = sns.Topic(topic_arn)

def lambda_handler(event, context):


    response = requests.request("POST", url, headers=headers)
    my_topic.publish(Message = response.text)
    
        
    return {
        'statusCode': 200,
        'body': json.dumps("Success!")
    }
