WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/bin/sh
echo "var BACKEND_PORT = $1;" > frontend/prebundle/config.js
cd frontend
python3 static.py $2
