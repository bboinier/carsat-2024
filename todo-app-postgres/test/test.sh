sleep 5
if curl todoapp:5000 | grep -q 'List'; then
  echo "Tests passed!"
  exit 0
else
  echo "Tests failed!"
  exit 1
fi
