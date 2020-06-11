require 'httpclient'

base_url = 'http://192.168.88.79/hi'

client = HTTPClient.new()
response = client.get(base_url)
puts response.status
puts response.body