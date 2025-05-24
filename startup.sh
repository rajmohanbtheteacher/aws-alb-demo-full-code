
#!/bin/bash
echo "📦 Installing Boto3..."
pip install boto3
export AWS_DEFAULT_REGION=us-east-1
echo "🔁 Fetching ALB metadata..."
python3 fetch_alb_metadata.py

echo "✅ Done. 'alb-metadata.json' ready and served from Apache root."
cp alb-metadata.json /var/www/html/
echo "Copied alb-metadata.json to apache web folder ✅ Done."
