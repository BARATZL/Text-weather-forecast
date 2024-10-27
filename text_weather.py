import requests
import os
from twilio.rest import Client

def space_string(text):
  result = [text[0]]
  for x in text[1:]:
    if x.isupper():
      result.append(' ')
    result.append(x)
  return ''.join(result)

api_key = 'api key goes here'
  url = f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}?apikey={api_key}&details=true' #when doing multiple query params, use the & symbol!
  r = requests.get(url)
  fcast_dict = r.json()
  weather_condition = str(fcast_dict["DailyForecasts"][0]["Day"]["IconPhrase"]).lower() #partly cloudy, sunny, etc.
  precipitation_chance = str(fcast_dict["DailyForecasts"][0]["Day"]["PrecipitationProbability"])
  high_temp = str(fcast_dict["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"])
  low_temp = str(fcast_dict["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"])
  moon_phase_raw = str(fcast_dict["DailyForecasts"][0]["Moon"]["Phase"]) #gives me an unpretty string with combined words
  moon_phase_adjusted = space_string(moon_phase_raw).lower() #Prettier!
  weather_summary = f'Hi there! Today the weather is expected to be {weather_condition}. There is a {precipitation_chance}% chance of rain. \nThe high is expected to be {high_temp} degrees Fahrenheit. The low is expected to be {low_temp} degrees Fahrenheit.\nThe moon is in the {moon_phase_adjusted} phase today. Have a great day!')

account_sid = "account sid goes here"
auth_token = "auth token goes here"
client = Client(account_sid,auth_token)

message = client.messages.create(
    body=weather_summary
    from_="toll free number established with Twilio"
    to="number of interest"
)
