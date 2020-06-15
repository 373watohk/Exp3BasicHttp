require 'socket'

server = TCPServer.new 2000
loop do
  client = server.accept
  headers = []
  while header = client.gets
    break if header.chomp.empty?
    headers << header.chomp
  end
  p headers
  
  client.puts "HTTP/1.1 200 OK"
  client.puts "Hello: BasicHTTP!"
  client.puts "Date: Tue, 26 May 2020 06:53:14 GMT"
  client.puts "Content-Length: 13"
  client.puts "Content-Type: text/plain; charset=utf-8"
  client.puts
  client.puts "#{ip_address}"
  client.close
end