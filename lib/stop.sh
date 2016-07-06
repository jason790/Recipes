ps -e | grep python | awk '{kill $1}'
