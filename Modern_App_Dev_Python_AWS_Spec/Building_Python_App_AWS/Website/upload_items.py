import boto3

S3API = boto3.client('s3', region_name="<region>")
bucket_name = "<s3 bucket name>"

filename = "backdrop_camera.jpg"
S3API.upload_file(filename, bucket_name, "backdropcamera.jpg", ExtraArgs={'ContentType': "image/jpg", 'CacheControl':'max-age=0'})

filename= "kiosk.png"
S3API.upload_file(filename, bucket_name, "kiosk.png", ExtraArgs={'ContentType': "image/png", 'CacheControl':'max-age=0'})

filename = "config.js"
S3API.upload_file(filename, bucket_name, "config.js", ExtraArgs={'ContentType': "application/js", "CacheControl": "max-age=0"})

filename = "core.css"
S3API.upload_file(filename, bucket_name, "core.css", ExtraArgs={'ContentType': "text/css", "CacheControl": "max-age=0"})

filename = "flex_search.js"
S3API.upload_file(filename, bucket_name, "flex_search.js", ExtraArgs={'ContentType': "application/js", "CacheControl": "max-age=0"})

filename = "index.html"
S3API.upload_file(filename, bucket_name, "index.html", ExtraArgs={'ContentType': "text/html", "CacheControl": "max-age=0"})

filename = "report.html"
S3API.upload_file(filename, bucket_name, "report.html", ExtraArgs={'ContentType': "text/html", "CacheControl": "max-age=0"})

filename = "jquery.js"
S3API.upload_file(filename, bucket_name, "jquery.js", ExtraArgs={'ContentType': "application/js", "CacheControl": "max-age=0"})

filename = "main.css"
S3API.upload_file(filename, bucket_name, "main.css", ExtraArgs={'ContentType': "text/css", "CacheControl": "max-age=0"})

filename = "main.js"
S3API.upload_file(filename, bucket_name, "main.js", ExtraArgs={'ContentType': "application/js", "CacheControl": "max-age=0"})

filename = "products.js"
S3API.upload_file(filename, bucket_name, "products.js", ExtraArgs={'ContentType': "application/js", "CacheControl": "max-age=0"})

filename = "reset.css"
S3API.upload_file(filename, bucket_name, "reset.css", ExtraArgs={'ContentType': "text/css", "CacheControl": "max-age=0"})

filename = "search.css"
S3API.upload_file(filename, bucket_name, "search.css", ExtraArgs={'ContentType': "text/css", "CacheControl": "max-age=0"})
