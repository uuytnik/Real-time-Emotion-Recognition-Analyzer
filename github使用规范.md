### **如何管理和纠正：团队协作的“铁律”**

为了解决这个问题并杜绝未来再次发生，你们团队需要建立并严格遵守以下版本管理规范。这正是**专业团队**的做法。

#### **规则一：`main` 分支是神圣的，禁止直接提交！**

*   **目的**：保证 `main` 分支永远是稳定的、可部署的。
*   **实施**：
    1.  **团队约定**：所有人都必须遵守，**任何人都不能直接在 `main` 分支上进行开发和 `push`**。
    2.  **GitHub保护规则 (强烈推荐)**：项目管理员（通常是辅助C或主力A）应该在 GitHub 仓库的 `Settings` -> `Branches` 中，为 `main` 分支添加**分支保护规则 (Branch protection rule)**。
        *   **勾选 "Require a pull request before merging"**: 这会从技术上禁止任何人直接向 `main` 分支 `push` 代码。所有变更**必须**通过 PR。
        *   **勾选 "Require status checks to pass before merging"**: （可选，但推荐）如果你们配置了自动化测试，可以确保只有测试通过的 PR 才能合并。

#### **规则二：所有新工作必须从特性分支开始**

*   **目的**：隔离开发，保持历史清晰。
*   **实施**：
    1.  **开始新任务前**：
        ```bash
        git checkout main          # 切换到 main
        git pull origin main       # 拉取最新代码
        git checkout -b feature/a-descriptive-name  # 创建并切换到新分支
        ```
    2.  **分支命名**：使用有意义的前缀，如 `feature/` (新功能), `fix/` (Bug修复), `docs/` (文档修改)。

#### **规则三：在自己的分支上，用 `rebase` 保持与 `main` 的同步**

*   **目的**：避免不必要的合并提交，保持线性、干净的历史记录。
*   **实施**：
    1.  当 `main` 分支有更新时（比如队友合并了一个PR），你需要同步这些更新到你的特性分支上。
    2.  **不要用 `merge`，用 `rebase`**：
        ```bash
        # 1. 先更新你本地的 main
        git checkout main
        git pull origin main
        
        # 2. 回到你的特性分支
        git checkout feature/a-descriptive-name
        
        # 3. 把你的工作“变基”到最新的 main 之上
        git rebase main
        ```
    3.  这样，你的分支历史就会像是在最新的 `main` 分支之后才开始开发一样，非常整洁。

#### **规则四：通过 Pull Request (PR) 进行合并**

*   **目的**：进行代码审查，确保代码质量，留下合并记录。
*   **实施**：
    1.  在你的特性分支上完成开发后，推送到远程：`git push -u origin feature/a-descriptive-name`。
    2.  去 GitHub 创建一个从你的 `feature/a-descriptive-name` 分支到 `main` 分支的 Pull Request。
    3.  邀请至少一个队友进行**代码审查 (Code Review)**。
    4.  审查通过后，在 GitHub 页面上点击 "Merge pull request"。**推荐使用 "Squash and merge" 或 "Rebase and merge" 选项**，这能让 `main` 分支的历史更加干净。
