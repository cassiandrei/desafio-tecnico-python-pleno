sudo cp -r api/* /var/lib/docker/volumes/delivery_api_data/_data
docker exec -i -t api-delivery pip install -r requirements.txt
docker exec -i -t api-delivery python manage.py makemigrations
docker exec -i -t api-delivery python manage.py migrate