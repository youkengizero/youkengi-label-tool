"""
一键部署到 GitHub 脚本
One-click deploy to GitHub

使用方法:
1. 确保已安装 Git: https://git-scm.com/download/win
2. 确保已配置 Git 用户名和邮箱
3. 修改下方配置并运行: python deploy_to_github.py
"""

import subprocess
import sys
import os
from pathlib import Path

# ==================== 配置区域 / Configuration ====================
# GitHub 用户名 / GitHub Username
GITHUB_USERNAME = "youkengizero"

# Git 邮箱 / Git Email
GIT_EMAIL = "646937580@qq.com"

# Git 用户名 / Git Username
GIT_NAME = "youkengizero"

# 仓库名称 / Repository Name
REPO_NAME = "youkengi-label-tool"

# 仓库描述（中文）/ Repository Description (Chinese)
DESCRIPTION_ZH = "优可打标校验工具 - 用于示词的人工检验与调整的 TXT 文件管理工具"

# 仓库描述（英文）/ Repository Description (English)
DESCRIPTION_EN = "Youkengi Label Verification Tool - A TXT file management tool for manual inspection and adjustment of prompts"

# 是否创建私有仓库 / Create private repository
PRIVATE_REPO = False

# GitHub Token (可选，用于自动创建仓库 / Optional, for auto-creating repo)
# 在 https://github.com/settings/tokens 生成 / Generate at: https://github.com/settings/tokens
GITHUB_TOKEN = ""

# ==================== 部署脚本 / Deploy Script ====================

def run_command(cmd, check=True):
    """运行命令并返回结果"""
    print(f"\n>>> {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if check and result.returncode != 0:
        print(f"命令失败: {cmd}")
        return False
    return result.returncode == 0

def check_git_installed():
    """检查 Git 是否已安装"""
    result = subprocess.run("git --version", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ Git 未安装！请访问 https://git-scm.com/download/win 下载安装")
        print("❌ Git not installed! Please visit https://git-scm.com/download/win")
        return False
    print(f"✅ Git 已安装: {result.stdout.strip()}")
    return True

def check_git_config():
    """检查并配置 Git"""
    name_result = subprocess.run("git config user.name", shell=True, capture_output=True, text=True)
    email_result = subprocess.run("git config user.email", shell=True, capture_output=True, text=True)
    
    # 如果未配置，自动配置
    if name_result.returncode != 0 or not name_result.stdout.strip():
        print(f"⚠️ Git 用户名未配置，自动设置为: {GIT_NAME}")
        run_command(f'git config --global user.name "{GIT_NAME}"')
    
    if email_result.returncode != 0 or not email_result.stdout.strip():
        print(f"⚠️ Git 邮箱未配置，自动设置为: {GIT_EMAIL}")
        run_command(f'git config --global user.email "{GIT_EMAIL}"')
    
    # 重新读取配置
    name_result = subprocess.run("git config user.name", shell=True, capture_output=True, text=True)
    email_result = subprocess.run("git config user.email", shell=True, capture_output=True, text=True)
    
    print(f"✅ Git 配置: {name_result.stdout.strip()} <{email_result.stdout.strip()}>")
    return True

def create_github_repo():
    """使用 GitHub API 创建仓库"""
    if not GITHUB_TOKEN:
        print("\n⚠️ 未设置 GITHUB_TOKEN，跳过自动创建仓库")
        print("   请手动在 https://github.com/new 创建仓库")
        print("   或设置 GITHUB_TOKEN 实现自动创建")
        return False
    
    try:
        import urllib.request
        import json
        
        url = "https://api.github.com/user/repos"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {
            "name": REPO_NAME,
            "description": f"{DESCRIPTION_ZH} | {DESCRIPTION_EN}",
            "private": PRIVATE_REPO,
            "auto_init": False
        }
        
        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode(),
            headers=headers,
            method="POST"
        )
        
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                print(f"✅ GitHub 仓库创建成功: {REPO_NAME}")
                return True
            else:
                print(f"⚠️ 创建仓库失败: {response.status}")
                return False
    except Exception as e:
        print(f"⚠️ 创建仓库出错: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("🚀 优可打标校验工具 - GitHub 一键部署")
    print("🚀 Youkengi Label Verification Tool - One-Click Deploy")
    print("=" * 60)
    
    # 检查 Git
    if not check_git_installed():
        return 1
    
    if not check_git_config():
        return 1
    
    # 获取项目目录
    project_dir = Path(__file__).parent.absolute()
    print(f"\n📁 项目目录: {project_dir}")
    
    # 切换到项目目录
    os.chdir(project_dir)
    
    # 尝试自动创建仓库
    repo_created = create_github_repo()
    
    if not repo_created:
        print("\n" + "=" * 60)
        print("📋 请手动创建仓库后按回车继续...")
        print("📋 Please manually create the repository and press Enter to continue...")
        print(f"   URL: https://github.com/new")
        print(f"   Repository name: {REPO_NAME}")
        input("=" * 60)
    
    # 构建远程仓库 URL
    remote_url = f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
    
    print("\n" + "=" * 60)
    print("📦 开始部署 / Starting deployment...")
    print("=" * 60)
    
    # 检查是否已初始化 Git
    git_dir = project_dir / ".git"
    if git_dir.exists():
        print("\n⚠️ 检测到已存在的 Git 仓库")
        response = input("   是否重新初始化? (y/N): ").strip().lower()
        if response == 'y':
            # 备份并重新初始化
            backup_dir = project_dir / ".git_backup"
            if backup_dir.exists():
                import shutil
                shutil.rmtree(backup_dir)
            git_dir.rename(backup_dir)
            print("   已备份原仓库到 .git_backup")
        else:
            print("   使用现有仓库继续...")
    
    # 初始化 Git 仓库
    if not git_dir.exists():
        if not run_command("git init"):
            return 1
    
    # 检查远程仓库配置
    result = subprocess.run("git remote -v", shell=True, capture_output=True, text=True)
    if "origin" in result.stdout:
        print("\n⚠️ 远程仓库已存在")
        run_command("git remote remove origin", check=False)
    
    # 添加远程仓库
    if not run_command(f"git remote add origin {remote_url}"):
        return 1
    
    # 检查文件状态
    print("\n📋 检查文件状态 / Checking file status...")
    run_command("git status", check=False)
    
    # 添加所有文件
    print("\n📥 添加文件到暂存区 / Adding files...")
    if not run_command("git add ."):
        return 1
    
    # 提交
    print("\n💾 提交更改 / Committing changes...")
    commit_msg = f"Initial commit: {DESCRIPTION_EN}"
    if not run_command(f'git commit -m "{commit_msg}"'):
        # 可能没有更改需要提交
        print("⚠️ 提交失败或没有更改需要提交")
    
    # 设置分支名
    print("\n🌿 设置分支 / Setting up branch...")
    run_command("git branch -M main", check=False)
    
    # 推送到 GitHub
    print("\n🚀 推送到 GitHub / Pushing to GitHub...")
    print(f"   远程地址: {remote_url}")
    
    if not run_command("git push -u origin main"):
        print("\n❌ 推送失败，尝试强制推送...")
        print("❌ Push failed, trying force push...")
        response = input("   是否强制推送? (y/N): ").strip().lower()
        if response == 'y':
            run_command("git push -u origin main --force")
    
    # 验证
    print("\n" + "=" * 60)
    print("✅ 部署完成 / Deployment completed!")
    print("=" * 60)
    print(f"\n🌐 仓库地址 / Repository URL:")
    print(f"   https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
    print(f"\n📖 请访问上方链接查看仓库")
    print(f"📖 Please visit the link above to view the repository")
    print("\n💡 后续更新命令 / Future update commands:")
    print("   git add .")
    print('   git commit -m "Your commit message"')
    print("   git push")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
