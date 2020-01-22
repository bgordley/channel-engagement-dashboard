# Channel Engagement Dashboard
The intent of this project is to provide a simple view into the level of community engagement for any streaming channel across any platform.
Currently this is achieved through monitoring chat frequency to determine a chat "mood".

## Current State  
 - Only integrated with <twitch.tv> at the moment
 - Chat monitoring is mocked and will not reflect real chat metrics

## Future Goals
 - Implement a GraphQL interface using [Graphene](https://graphene-python.org/)
 - Implement IRC Twitch chat-bot to collect real chat metrics
 - Create Docker image and deploy to Kubernetes cluster
 - Integrate GitHub pipeline for CI/CD
 
## Testing
Currently testing is limited to a small amount of unit tests. Below is a list of future testing objectives.
 - Implement a suite of integration tests 
 - Implement more robust unit tests
 - Implement code coverage reporting
 
 ### Executing unit tests
Execute the included test script from the root directory.
```shell script
./scripts/test-service.sh
```

Alternatively, execute the following command
```shell script
python -m unittest discover -s ./test
```

## Running
### Prerequisites
The following are required to run this service
 - Python 3.7
 - Pipenv

### Before you start
Take a look at "example_config.json". You will need to create your own "config.json" file in the root directory 
and will need to provide your own Twitch developer client id.

### Executing the service
Execute the included run script from the root directory.
```shell script
./scripts/run-service.sh
```

Alternatively, execute the following command
```shell script
env FLASK_APP=./service/main.py pipenv run flask run
```

## API Documentation
To view additional information about the API endpoints provided by this service simply start the service and navigate 
to <http://localhost:5000/> in your browser. This will take you to the swagger page where you can view and try out the 
endpoints for yourself.
