# GitHub Repository Setup Guide

## Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **+** icon in the top right → **New repository**
3. Fill in the details:
   - **Repository name**: `deepthought-reflection-tree` (or your preferred name)
   - **Description**: "Daily Reflection Tree - DeepThought Fellowship Assignment"
   - **Visibility**: Public (so DeepThought can access it)
   - **Initialize**: Do NOT check "Add a README file" (we already have one)
4. Click **Create repository**

## Step 2: Initialize Git in Your Local Project

Open your terminal in the project directory and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Daily Reflection Tree assignment complete"
```

## Step 3: Connect to GitHub

Copy the commands from GitHub (they'll look like this, but with your username):

```bash
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/deepthought-reflection-tree.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Verify Upload

1. Refresh your GitHub repository page
2. You should see all files uploaded
3. The README.md will display automatically

## Step 5: Get the Repository Link

Your repository URL will be:
```
https://github.com/YOUR_USERNAME/deepthought-reflection-tree
```

Copy this link to submit on Internshala.

## Project Structure on GitHub

Your repository should show:

```
deepthought-reflection-tree/
├── agent/
│   ├── reflection_agent.py
│   └── requirements.txt
├── transcripts/
│   ├── persona-victor-transcript.md
│   └── persona-victim-transcript.md
├── tree/
│   ├── reflection-tree.json
│   └── tree-diagram.md
├── .gitignore
├── GITHUB_SETUP.md
├── PROJECT_SUMMARY.md
├── QUICKSTART.md
├── README.md
├── SUBMISSION.md
└── write-up.md
```

## Tips for a Good Repository

### 1. Add a Good README
✅ Already done! Your README.md is comprehensive.

### 2. Add Topics/Tags
On GitHub, click the ⚙️ icon next to "About" and add topics:
- `python`
- `decision-tree`
- `psychology`
- `reflection-tool`
- `deepthought`
- `internship-assignment`

### 3. Update Repository Description
In the "About" section, add:
> Daily Reflection Tree - A deterministic reflection agent that guides employees through structured end-of-day reflection across three psychological axes. Built for DeepThought Fellowship assignment.

### 4. Pin Important Files
GitHub will automatically show README.md. Make sure these are easy to find:
- `tree/reflection-tree.json` - The main deliverable
- `write-up.md` - Design rationale
- `agent/reflection_agent.py` - Working implementation

## Common Issues

### Issue: "Permission denied (publickey)"
**Solution**: Use HTTPS instead of SSH:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/deepthought-reflection-tree.git
```

### Issue: "Repository not found"
**Solution**: Make sure you created the repository on GitHub first, and the URL is correct.

### Issue: "Failed to push"
**Solution**: Pull first, then push:
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

## Submission Checklist

Before submitting the link:

- [ ] Repository is public (not private)
- [ ] All files are uploaded
- [ ] README.md displays correctly
- [ ] Tree diagram renders in `tree/tree-diagram.md`
- [ ] Repository has a good description
- [ ] Topics/tags are added
- [ ] Repository URL is copied

## Submit to Internshala

1. Go to your Internshala application
2. Find the assignment submission section
3. Paste your GitHub repository URL:
   ```
   https://github.com/YOUR_USERNAME/deepthought-reflection-tree
   ```
4. Add a brief message:
   ```
   Daily Reflection Tree assignment completed.
   
   Part A (Required): Complete decision tree with 41 nodes, visual diagram, 
   and design write-up with psychology sources.
   
   Part B (Optional): Working Python agent with sample transcripts.
   
   All requirements exceeded. Ready for evaluation.
   ```

## Optional: Add a License

If you want to add a license (optional):

1. On GitHub, click **Add file** → **Create new file**
2. Name it `LICENSE`
3. Click **Choose a license template**
4. Select **MIT License** (most permissive)
5. Commit the file

## Final Check

Visit your repository URL in an incognito/private browser window to verify:
- ✅ Repository is accessible without login
- ✅ README displays correctly
- ✅ Files are organized properly
- ✅ Mermaid diagram renders in tree-diagram.md

---

**You're ready to submit!** 🚀

Your repository link:
```
https://github.com/YOUR_USERNAME/deepthought-reflection-tree
```

Good luck with your application! 🎯
