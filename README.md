# LightningFlask

Simple project for building a lightning talk on Python Flask

## [1. First Encounter with Flask][step1]

Trivial app that serves a 'Hello, World!' message. 
Covers:
- Python Flask requirements
- 2 ways to run flask
- Having the file named something other than `app.py`
- Changing the host name or port  

## [2. First GET Request Handler][step2]

The most trivial of APIs, able to respond to a GET request.
Covers: 
- Registering a GET handler for a specific route
- Making use of path parameters
- Making use of query parameters
- Responding with an `application/json` response and appropriate status code

## [3. Handling Other Request Types][step3]

Expanding the API to handle receiving data in addition to serving data.
Covers:
- Registering handlers for any request type
- Making use of the request body
- Making use of common request headers such as `Content-Type`

## [4. Getting Fancy][step4]

The title says it all.
Covers:
- Multi method type request handlers
- Exception handling
- Serving static files

[step1]: ./Wiki/step1.md
[step2]: ./Wiki/step2.md
[step3]: ./Wiki/step3.md
[step4]: ./Wiki/step4.md
