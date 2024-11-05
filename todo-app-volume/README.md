## Commandes à tester

- `docker build -t todo_app_image .`
- `docker run -p 5000:5000 -e BACKGROUND_COLOR="#add8e6" todo_app_image`
- --volumes-from
- `docker run -p 5000:5000 -v $(pwd)/data:/app/data -e BACKGROUND_COLOR="#add8e6" todo_app_image`

## Couleurs de fond

- #FF5733 - Un rouge orangé vif
- #33C1FF - Un bleu clair
- #9BFF33 - Un vert lime vibrantS