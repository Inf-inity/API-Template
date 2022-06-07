# API-Template

An API-template for pictures, written in python


## Install the API:


#### HTTPS:

```
$ git clone https://github.com/NekoFanatic/API-Template.git
```


#### SSH:

```
$ git clone git@github.com:NekoFanatic/API-Template.git
```

### Setup:

```
$ virtualenv venv

$ source venv/bin/activate

$ pip install -r requirements.txt 

$ uvicorn main:app --reload --host "0.0.0.0"
```


## Add images:

Add more images by creating `.yml`files in the [endpoints-folder](./endpoints). Every file represents an endpoint in which images can be 
added. The `templates.yml` can't be used!

```yml
1:                                              # a unique placeholder (can be a number)
  artist_name: <name>                           # the name of the artist
  artist_href: <url for the artist profile>     # the url for the artist-profile
  image_url: <url for the picture>              # the url for an image
  tags: ["list", "with", "tags"]                # a list with tags an image can have
```


## Get images from the API:

Note that the host-address "0.0.0.0" is a network-address. Don't use it for testing (use `uvicorn main:app --reload`)
without host-parameter instead.


### Getting a list of all endpoints:

```
https://127.0.0.1:8000
```

### Getting a list of all tags from pictures from an endpoint

```
https://127.0.0.1:8000/{endpoint}/tags
```

### Getting random pictures from an endpoint:

```
# one image
https://127.0.0.1:8000/{endpoint}

# more images (1-20)
https://127.0.0.1:8000/{endpoint}?amount={amount}

# filter by tags (seperated by whitespaces)
https://127.0.0.1:8000/{endpoint}?tags={tag1} {tag2} ...

# more images, filtered by tags
https://127.0.0.1:8000/{endpoint}?amount={amount}&tags={tag1} {tag2}
```
