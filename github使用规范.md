### **如何管理和纠正：团队协作的“铁律”**

**在使用git和github前先看一下下面的规定！**

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

#### **规则五：编写清晰、规范的 Commit Message**

*   **目的**：让提交历史成为**任何人都能快速读懂的“项目日志”**。一个好的 `commit`  message 能让人在不看代码的情况下，就明白这次提交的目的。
*   **实施**：
    1.  **采用“Conventional Commits”规范**：这是目前社区最流行的提交信息格式。格式为：
        ```
        <type>(<scope>): <subject>
        ```
    2.  **常用的 `<type>` 类型**：
        *   `feat`: 新功能 (feature)
        *   `fix`: 修复 bug
        *   `docs`: 仅仅修改了文档
        *   `style`: 修改代码格式（不影响代码逻辑，如空格、分号等）
        *   `refactor`: 代码重构（既不是新增功能，也不是修复 bug）
        *   `test`: 增加或修改测试
        *   `chore`: 构建过程或辅助工具的变动（如修改配置文件）
    3.  **`<scope>` (可选)**：指明本次提交影响的范围，比如 `frontend`, `backend`, `auth`, `ui` 等。
    4.  **`<subject>`**：用一句话清晰地描述本次提交的目的。
    5.  **示例**：
        *   `feat(frontend): Add real-time video component`
        *   `fix(backend): Correct emotion analysis API response format`
        *   `docs(readme): Update project setup instructions`

#### **规则六：保持 Pull Request (PR) 的小巧与专注**

*   **目的**：**让代码审查 (Code Review) 变得轻松、快速、有效**。一个包含上千行代码改动的巨大PR，几乎不可能得到高质量的审查。
*   **实施**：
    1.  **一个PR只做一件事**：一个PR应该只专注于一个功能或一个Bug修复。如果你想同时做功能A和功能B，请创建两个独立的分支和两个独立的PR。
    2.  **尽早、频繁地创建PR**：不要等到一个大功能完全开发完才提交PR。你可以先完成一个小部分，就创建一个“**草稿PR (Draft Pull Request)**”。这能让你的队友提前看到你的方向和代码结构，及时给出反馈，避免你“在错误的方向上狂奔”。
    3.  **使用 GitHub 的 "Draft" 功能**：在创建PR时，可以选择 "Create Draft Pull Request"。它不会通知审查者，直到你手动点击 "Ready for review"。

#### **规则七：提供高质量的 Pull Request 描述**

*   **目的**：为审查者提供足够的上下文，让他们明白**你为什么这么改**，以及**如何测试你的改动**。
*   **实施**：
    1.  **遵循PR模板**：在项目中创建一个PR模板文件 (`.github/pull_request_template.md`)，让每次创建PR时自动填充。
    2.  **一个好的PR描述至少应包含**：
        *   **本次PR解决了什么问题？(What?)**: 简要描述功能或修复的Bug。可以关联到对应的 GitHub Issue (例如 `Closes #12`)。
        *   **为什么需要这次变更？(Why?)**: 解释背后的原因。
        *   **我是如何实现的？(How?)**: 简述技术方案。
        *   **如何进行测试？(Testing?)**: 提供清晰的测试步骤，让审查者可以验证你的改动。
        *   **截图/录屏 (如果涉及UI改动)**：一张图胜过千言万语。

#### **规则八：PR 作者的责任与审查礼仪**

*   **目的**：建立互相尊重、积极反馈的团队文化。
*   **实施**：
    1.  **PR作者的责任**：
        *   **自己是第一审查者**：在发起PR前，自己先完整地看一遍代码，确保没有明显的错误或调试代码 (`console.log`)。
        *   **及时回应评论**：积极、友好地回应审查者提出的问题和建议。
        *   **原则上不合并自己的PR**：为了保证审查的客观性，PR应该由审查者在批准后进行合并。
    2.  **审查者的责任**：
        *   **及时审查**：不要让队友的PR等待太久。
        *   **提供建设性意见**：对事不对人，语气友好。多用提问的方式（“这样写会不会更好？”）代替命令（“你应该这样写”）。
        *   **不仅是找错**：看到写得好的地方，也不要吝啬你的赞美！

#### **规则九：合并后清理分支**

*   **目的**：保持仓库的整洁，避免大量已合并的、无用的分支堆积。
*   **实施**：
    1.  在PR被合并后，GitHub通常会提供一个 "Delete branch" 的按钮。**请果断点击它**，删除远程的特性分支。
    2.  同时，也要清理你本地的对应分支：
        ```bash
        git checkout main          # 切换回主分支
        git pull origin main       # 同步最新代码
        git branch -d feature/the-merged-feature  # 删除已合并的本地分支
        ```

