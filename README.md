
# 📡 ALB to EC2 Metadata Visualizer - Static Web App

Visualizes EC2 metadata & ALB routing with animated connections and real-time AWS details.

## 🔧 Setup Instructions

```bash
unzip alb-ec2-full-deployable.zip
cd alb-demo-full
bash startup.sh
sudo cp -r * /var/www/html/
```

## 🔍 Architecture

```
Client Browser
    |
    v
[Animated WebApp (HTML+JS)]
    |
    v
[ALB: dns-name]
   /  \
EC2-1  EC2-2
(metadata via port 8080)
```

## 🧠 Analogy

Think of ALB as a **receptionist** directing customers (traffic) to available desks (EC2s).

## 📁 Files

- `index.html`, `style.css`, `script.js` – WebApp
- `assets/` – Icons
- `alb-metadata.json` – Generated metadata for ALB (served via Apache)
- `fetch_alb_metadata.py` – Python script to pull ALB info from AWS
- `startup.sh` – One-shot installer for server deployment

---

Ready to deploy in any Apache-hosted EC2 environment with dynamic, animated AWS visualization!
