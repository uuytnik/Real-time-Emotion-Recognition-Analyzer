### **团队Git协作规范与流程指南**

**请进行git操作的时候参考这份指南！！！**

#### **Part 1: 核心原则（团队的“宪法”）**

1.  **`main` 分支是受保护的。** 它代表了项目最稳定、可随时发布的状态。**任何人**都禁止直接向 `main` 分支 `push` 代码。
2.  **所有开发都在特性分支进行。** 每个新功能、Bug修复或文档修改都必须在自己的独立分支上完成，以保证工作隔离。
3.  **所有代码变更必须通过 Pull Request (PR) 合并。** 这是代码审查、质量保证和团队沟通的核心环节。
4.  **保持提交历史的清晰和线性。** 我们使用 `rebase` 来同步主干更新，避免不必要的合并噪音。

---

#### **Part 2: 首次设置（一次性操作）**

1.  **克隆项目**：从 GitHub 仓库页面复制 HTTPS 地址，在你的电脑终端里运行：
    ```bash
    git clone [粘贴的地址]
    ```
2.  **配置你的身份**（如果还没做过）：
    ```bash
    git config --global user.name "你的GitHub用户名"
    git config --global user.email "你的GitHub邮箱"
    ```

---

#### **Part 3: 日常开发标准流程（循环执行）**

这是你每天工作的完整流程，从开始一个新任务到最终完成。

##### **Step 1: 开始新任务（创建分支）**

**永远从最新的 `main` 分支开始你的新工作。**

1.  **同步本地 `main` 分支**：
    ```bash
    git checkout main
    git pull origin main
    ```

2.  **创建你的特性分支**：
    *   **分支命名规范**：使用 `类型/简短描述` 的格式。
        *   `feature/`: 新功能 (e.g., `feature/user-login`)
        *   `fix/`: Bug修复 (e.g., `fix/navbar-display-issue`)
        *   `docs/`: 文档修改 (e.g., `docs/update-readme`)
    *   **创建并切换**：
        ```bash
        git checkout -b feature/your-feature-name
        ```

##### **Step 2: 开发与提交**

**在你的分支上专注工作，并频繁、清晰地保存进度。**

1.  **编码...**

2.  **提交你的修改**：
    *   **提交规范**：我们遵循 **Conventional Commits** 规范。格式为 `<type>(<scope>): <subject>`。
        *   **`<type>`**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
        *   **`<scope>` (可选)**: `frontend`, `backend`, `api`, `ui`
    *   **提交操作**：
        ```bash
        # 1. 添加所有修改
        git add .
        
        # 2. 遵循规范编写提交信息
        git commit -m "feat(frontend): Add start/stop analysis button"
        ```

3.  **保持与 `main` 分支同步（如果 `main` 有更新）**：
    *   如果在你开发期间，有队友的代码合并到了 `main`，你需要同步这些更新以避免冲突。
    *   **使用 `rebase` 而不是 `merge`**：
        ```bash
        # 1. 先更新你本地的 main
        git checkout main
        git pull origin main
        
        # 2. 回到你的特性分支
        git checkout feature/your-feature-name
        
        # 3. 把你的工作“变基”到最新的 main 之上
        git rebase main
        ```
        *如果 rebase 过程中出现冲突，解决后用 `git add .` -> `git rebase --continue` 继续。*

##### **Step 3: 创建 Pull Request (PR)**

**当你的功能开发完成，准备好让团队评审时。**

1.  **推送到远程**：将你的分支和所有提交推送到GitHub。
    ```bash
    # 如果是第一次推送这个分支，加上 -u
    git push -u origin feature/your-feature-name
    ```

2.  **在 GitHub 上创建 PR**：
    *   打开仓库主页，点击提示条上的 **"Compare & pull request"** 按钮。
    *   **确保合并方向**：`base: main` <-- `compare: feature/your-feature-name`。
    *   **保持PR小而专**：一个PR只解决一个问题。如果功能复杂，考虑创建**草稿PR (Draft PR)** 尽早获得反馈。

3.  **编写高质量的PR描述**：
    *   **标题**：使用你的主 `commit` 信息，清晰明了。
    *   **描述**：提供足够的上下文，回答“**What?** (做了什么)”、“**Why?** (为什么做)”和“**How to test?** (如何测试)”。对于UI改动，请附上截图。

##### **Step 4: 代码审查 (Code Review)**

**这是保证代码质量和团队知识共享的关键环节。**

1.  **指派审查者 (Reviewers)**：在PR页面右侧，选择至少一位队友。
2.  **PR作者的责任**：
    *   发起前先自我审查。
    *   友好、及时地回应评论。
    *   如果需要修改，直接在本地分支上 `commit` 和 `push`，PR会自动更新。
3.  **审查者的责任**：
    *   及时审查，提供建设性意见。
    *   对事不对人，保持友好沟通。

##### **Step 5: 合并与清理**

**当PR被批准后，将你的工作成果汇入主干。**

1.  **合并PR**：
    *   在GitHub的PR页面，点击绿色的 **"Merge pull request"** 按钮。
    *   **推荐使用 "Squash and merge"**：它会将你的所有提交合并成一个，让 `main` 分支的历史非常干净。
2.  **删除远程分支**：合并后，点击出现的 **"Delete branch"** 按钮。
3.  **清理本地分支**：
    ```bash
    # 1. 回到最新的 main
    git checkout main
    git pull origin main
    
    # 2. 删除已经合并的本地分支
    git branch -d feature/your-feature-name
    ```

