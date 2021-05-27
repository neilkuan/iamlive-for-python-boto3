## Demo [iamlive](https://github.com/iann0036/iamlive) for python boto3 sdk


### To Clone
```bash
$ git clone https://github.com/neilkuan/iamlive-for-python-boto3.git
```

### To Install
Go to release page: https://github.com/iann0036/iamlive/releases

### To Use Step 1 : open one terminal.
```bash
$ export AWS_CSM_ENABLED=true
$ export AWS_CSM_PORT=31000
$ export AWS_CSM_HOST=127.0.0.1
$ iamlive --set-ini --profile [replace_your_aws_profile_name]
```

### To Use Step 2 : open another one terminal.
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# modify profile name in `app.py`

$ python app.py
```

https://user-images.githubusercontent.com/46012524/119766220-31f82180-bee7-11eb-8886-9c6ea4bdfa39.mov
