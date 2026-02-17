# Create a new build.sh script that builds the site for production:
# The script is simple: python3 src/main.py "/REPO_NAME/" (replace REPO_NAME with your actual GitHub repo name)
# Your main.py is also used for local testing, so it will still need the default / baseurl
# Run the new build script and ensure that the site is built correctly

python3 src/main.py "/static-site-generator/"