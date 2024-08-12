import pywhatkit


# pywhatkit.sendwhatmsg('+923161881076', 'hello this is a python automated message for testing purposes', 23
#  ,49
#  )



pywhatkit.take_screenshot()

# sendwhatmsg('+923161881076', 'hello this is a python automated message for testing purposes', 23
#  ,49
#  )

import pywhatkit as kit

# Example group ID from WhatsApp Web URL
group_id = "123456789@chat.whatsapp.com"
message = "Hello everyone, this is a scheduled message."
hour = 16  # 4 PM
minute = 0  # 00 minutes

kit.sendwhatmsg_to_group(group_id, message, hour, minute)

pywhatkit.sendwhatmsg_to_group('')