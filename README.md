<a href="https://market.mashape.com/daxeel/abbreviations"><img src="http://i1.wp.com/blog.mashape.com/wp-content/uploads/2013/02/Screen_Shot_2013-02-12_at_6.53.42_PM.png"</a>

## About
Fullforms is a simple API which will give you access to lots of fullforms and meanings of shortforms. Get fullforms programarically via API request in json format

## Documentation
API documentation here is for python language. To use this in python you need to install unirest module.
```sh
sudo pip install unirest
```
### For popular abbreviations
```py
response = unirest.get("https://daxeel-abbreviations-v1.p.mashape.com/popular/{SHORT_FORM}",
  headers={
    "X-Mashape-Key": "V96M0xptiXmsh39L6Mw7CES0c7zgp1C7HOLjsnZGls6d3LiDjm"
  }
)
```
### For all abbreviations
```py
response = unirest.get("https://daxeel-abbreviations-v1.p.mashape.com/all/{SHORT_FORM}",
  headers={
    "X-Mashape-Key": "V96M0xptiXmsh39L6Mw7CES0c7zgp1C7HOLjsnZGls6d3LiDjm"
  }
)
```
<p>For more details : <a href="https://market.mashape.com/daxeel/abbreviations#all-short_form" target"_blank">Visit here</a></p>

## For more information
I have wrote simple blog post on how to use Fullforms API with python programming Language. <br>
You can check it out here : <a href="http://blog.daxeelsoni.in/2015/12/25/working-with-abbreviations-api-in-python/" target="_blank">Click Here</a>
