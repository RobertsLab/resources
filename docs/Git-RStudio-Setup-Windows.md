# Installing Git and Connecting to RStudio on Windows

This guide will walk you through installing Git on a Windows machine and connecting it to RStudio, which is essential for version control and collaboration in the Roberts Lab.

## Prerequisites

- A Windows computer with administrator access
- An internet connection
- A [GitHub account](https://github.com) (see [Computing Hardware](Computing-Hardware.md#accounts) for more info)

---

## Step 1: Install Git for Windows

1. **Download Git for Windows**
   - Visit the official Git website: [https://git-scm.com/download/win](https://git-scm.com/download/win)
   - The download should start automatically. If not, click the appropriate link for your system (typically 64-bit)

2. **Run the Installer**
   - Locate the downloaded file (typically in your Downloads folder) and double-click to run it
   - Click "Yes" if prompted by User Account Control

3. **Installation Options**
   
   During installation, you'll be presented with several configuration screens. Here are the recommended settings:
   
   - **Select Components**: Keep the default selections
     - Windows Explorer integration
     - Git Bash Here
     - Git GUI Here
     - Associate .git* configuration files with the default text editor
     - Associate .sh files to be run with Bash
   
   - **Choosing the default editor**: Select your preferred text editor (Notepad++ or Visual Studio Code are good options if installed, otherwise the default is fine)
   
   - **Adjusting your PATH environment**: Select **"Git from the command line and also from 3rd-party software"** (recommended)
   
   - **Choosing HTTPS transport backend**: Select **"Use the OpenSSL library"** (default)
   
   - **Configuring line ending conversions**: Select **"Checkout Windows-style, commit Unix-style line endings"** (default)
   
   - **Configuring the terminal emulator**: Select **"Use MinTTY"** (default)
   
   - **Choose the default behavior of `git pull`**: Select **"Default (fast-forward or merge)"**
   
   - **Choose a credential helper**: Select **"Git Credential Manager"** (default)
   
   - **Configuring extra options**: Keep the defaults
     - Enable file system caching
     - Enable symbolic links
   
   - Click **"Install"** to complete the installation

4. **Verify Git Installation**
   - Open Command Prompt (press `Windows Key + R`, type `cmd`, press Enter)
   - Type `git --version` and press Enter
   - You should see output like: `git version 2.x.x.windows.x`

---

## Step 2: Configure Git

Before using Git, you need to set up your identity. This information will be attached to your commits.

1. **Open Git Bash**
   - Right-click on your desktop or in any folder
   - Select "Git Bash Here" from the context menu

2. **Set Your Name**
   ```bash
   git config --global user.name "Your Name"
   ```
   Replace "Your Name" with your actual name (use the same name as your GitHub account)

3. **Set Your Email**
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   Replace with the email address associated with your GitHub account

4. **Verify Your Configuration**
   ```bash
   git config --global --list
   ```
   You should see your name and email listed

---

## Step 3: Install RStudio (if not already installed)

1. **Download RStudio Desktop**
   - Visit: [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/)
   - First, ensure R is installed (install from [https://cran.r-project.org/](https://cran.r-project.org/) if needed)
   - Download the RStudio installer for Windows
   - Run the installer and follow the prompts

---

## Step 4: Connect Git to RStudio

1. **Open RStudio**

2. **Configure Git in RStudio**
   - Go to **Tools** → **Global Options**
   - Select **Git/SVN** from the left sidebar
   
3. **Verify Git Path**
   - RStudio should automatically detect Git
   - The "Git executable" field should show the path to git.exe (typically `C:/Program Files/Git/bin/git.exe`)
   - If it's blank or incorrect:
     - Click **Browse**
     - Navigate to `C:\Program Files\Git\bin\`
     - Select `git.exe`
     - Click **Open**

4. **Enable Version Control**
   - Check the box for **"Enable version control interface for RStudio projects"**

5. **Set Up SSH Key (Recommended for GitHub)**
   
   SSH keys allow you to connect to GitHub without entering your password each time.
   
   - In the Git/SVN options window, click **"Create RSA Key..."**
   - Click **"Create"** in the dialog box (you can optionally add a passphrase for extra security)
   - Click **"Close"** when the key generation is complete
   - Click **"View public key"**
   - Copy the entire key (it starts with `ssh-rsa`)
   
6. **Add SSH Key to GitHub**
   - Go to [GitHub.com](https://github.com) and log in
   - Click your profile picture (top right) → **Settings**
   - Click **SSH and GPG keys** in the left sidebar
   - Click **"New SSH key"** or **"Add SSH key"**
   - Give it a title (e.g., "Lab Windows PC")
   - Paste your public key into the "Key" field
   - Click **"Add SSH key"**

7. **Click OK** to close the RStudio options window

---

## Step 5: Test Git Integration in RStudio

### Option A: Clone an Existing Repository

1. In RStudio, go to **File** → **New Project**
2. Select **Version Control**
3. Select **Git**
4. Enter the repository URL (e.g., `https://github.com/RobertsLab/resources.git`)
5. Choose where to save the project on your computer
6. Click **Create Project**

If successful, RStudio will download the repository and you'll see a "Git" tab in the upper-right pane.

### Option B: Create a New Git Repository

1. In RStudio, go to **File** → **New Project**
2. Select **New Directory**
3. Select **New Project**
4. Enter a directory name
5. Check **"Create a git repository"**
6. Click **Create Project**

You should now see a "Git" tab in the upper-right pane.

---

## Step 6: Using Git in RStudio

Once Git is connected to RStudio, you can use version control for your projects:

1. **View Changes**: The Git tab shows all modified files
2. **Stage Files**: Check the boxes next to files you want to commit
3. **Commit**: Click the "Commit" button, write a commit message, and click "Commit"
4. **Push**: Click the green "Push" arrow to send your changes to GitHub
5. **Pull**: Click the blue "Pull" arrow to get updates from GitHub

---

## Troubleshooting

### Git Not Found by RStudio

**Problem**: RStudio can't find Git, or the Git executable field is empty.

**Solution**:
1. Verify Git is installed by opening Command Prompt and typing `git --version`
2. If Git is installed, manually set the path in RStudio:
   - Tools → Global Options → Git/SVN
   - Browse to `C:\Program Files\Git\bin\git.exe`

### Authentication Issues with GitHub

**Problem**: Getting errors when trying to push/pull from GitHub.

**Solution 1 - Use Personal Access Token**:
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name and select scopes (at minimum: `repo`)
4. Click "Generate token" and copy the token
5. When RStudio prompts for a password, paste the token instead

**Solution 2 - Use SSH** (if you completed Step 4.5):
1. When cloning or setting up a repository, use the SSH URL instead of HTTPS
   - SSH URL format: `git@github.com:username/repository.git`
   - HTTPS URL format: `https://github.com/username/repository.git`

### Path Issues

**Problem**: Git works in Git Bash but not in RStudio or Command Prompt.

**Solution**: Git might not be in your system PATH.
1. Right-click "This PC" or "My Computer" → Properties
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "System variables", find and select "Path"
5. Click "Edit"
6. Add `C:\Program Files\Git\bin` if it's not already there
7. Click OK on all windows
8. Restart RStudio

---

## Additional Resources

- **Git Documentation**: [https://git-scm.com/doc](https://git-scm.com/doc)
- **RStudio Git Integration**: [https://support.posit.co/hc/en-us/articles/200532077-Version-Control-with-Git-and-SVN](https://support.posit.co/hc/en-us/articles/200532077-Version-Control-with-Git-and-SVN)
- **Happy Git with R**: [https://happygitwithr.com/](https://happygitwithr.com/) - Comprehensive guide for using Git with R and RStudio
- **Software Carpentry Git Lesson**: [https://swcarpentry.github.io/git-novice/](https://swcarpentry.github.io/git-novice/)
- **Roberts Lab Computing Best Practices**: [Computing-Best-Practices.md](Computing-Best-Practices.md) - includes video tutorial on working with Git and RStudio on Raven

---

## Getting Help

If you encounter issues not covered in this guide:

1. Check the [Troubleshooting](#troubleshooting) section above
2. Search for your error message on [Stack Overflow](https://stackoverflow.com/)
3. Post a question in the [Roberts Lab Slack](https://genefish.slack.com)
4. [Submit a GitHub Issue](https://github.com/RobertsLab/resources/issues) with details about your problem
