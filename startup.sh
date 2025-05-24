
#!/bin/bash
echo "📦 Installing Boto3..."
pip install boto3

echo "🔁 Fetching ALB metadata..."
python3 fetch_alb_metadata.py

echo "✅ Done. 'alb-metadata.json' ready and served from Apache root."
