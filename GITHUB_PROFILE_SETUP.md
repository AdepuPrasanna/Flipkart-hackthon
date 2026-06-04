# GitHub profile setup (topics, About, pin, social)

Do these once on [github.com/Bannysukumar/Gridlock-Hackathon-2.0](https://github.com/Bannysukumar/Gridlock-Hackathon-2.0).

---

## 1. Topics (copy-paste)

On the repo page → **About** (gear icon on the right) → **Topics** → add each:

```
machine-learning
hackathon
pandas
traffic-prediction
hackerearth
flipkart
```

Or run (after `gh auth login`):

```powershell
gh repo edit Bannysukumar/Gridlock-Hackathon-2.0 `
  --add-topic machine-learning `
  --add-topic hackathon `
  --add-topic pandas `
  --add-topic traffic-prediction `
  --add-topic hackerearth `
  --add-topic flipkart
```

---

## 2. About description + website

**Description** (one line):

```
Perfect-score traffic demand prediction for Flipkart Gridlock Hackathon 2.0 — spatiotemporal lookup (R² = 1.0).
```

**Website:**

```
https://www.hackerearth.com/challenges/competitive/gridlock-hackathon-20/
```

CLI:

```powershell
gh repo edit Bannysukumar/Gridlock-Hackathon-2.0 `
  --description "Perfect-score traffic demand prediction for Flipkart Gridlock Hackathon 2.0 — spatiotemporal lookup (R² = 1.0)." `
  --homepage "https://www.hackerearth.com/challenges/competitive/gridlock-hackathon-20/"
```

---

## 3. Pin on your profile

1. Open [github.com/Bannysukumar](https://github.com/Bannysukumar)
2. **Customize your pins** (or **Edit profile** → pinned repositories)
3. Select **Gridlock-Hackathon-2.0** (up to 6 repos)

---

## 4. LinkedIn post (copy)

```
I open-sourced my Gridlock Hackathon 2.0 solution — 100% leaderboard score using a simple spatiotemporal lookup (geohash + day + timestamp) instead of a heavy ML stack.

Repo: https://github.com/Bannysukumar/Gridlock-Hackathon-2.0
Challenge: https://www.hackerearth.com/challenges/competitive/gridlock-hackathon-20/

Includes reproducible predict.py, approach write-up, and the final submission CSV. Useful if you're prepping for similar demand/forecast competitions on HackerEarth.

#MachineLearning #Hackathon #DataScience #Flipkart #HackerEarth
```

---

## 5. X (Twitter) post (copy)

```
100% R² lookup approach for Flipkart Gridlock Hackathon 2.0 — traffic demand prediction on HackerEarth.

Open source: https://github.com/Bannysukumar/Gridlock-Hackathon-2.0

pandas merge on (geohash, day, timestamp). No heavy model in the final pipeline.

#MachineLearning #hackathon #pandas
```

---

## Optional: script with GitHub token

If you have a [Personal Access Token](https://github.com/settings/tokens) with `repo` scope:

```powershell
$env:GITHUB_TOKEN = "ghp_YOUR_TOKEN"
.\scripts\set_repo_metadata.ps1
```
