
import hmac
password = "4416f63125284a43de6r113a7e39bd35"
while True:
    user_input = raw_input("Insert password: ")
    my_hash = hmac.new(user_input).hexdigest()
    if my_hash == password:
        print "Tocno"
        break
