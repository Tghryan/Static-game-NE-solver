A web-based interactive Game Theory Solver built with Flask and PyGambit. This tool allows users to define custom players, strategies, and payoff matrices to find both Pure Strategy Nash Equilibria (PSNE) and Mixed Strategy Nash Equilibria (MSNE).

这是一个基于 Flask 和 PyGambit 开发的交互式博弈论求解器。用户可以自定义玩家名称、策略选项及收益矩阵，通过程序自动计算并输出 纯策略纳什均衡 (PSNE) 和 混合策略纳什均衡 (MSNE)。

✨ Features | 功能特点
Dynamic Matrix Generation: Automatically generates the input table based on the number of strategies entered.

动态矩阵生成：根据输入的策略数量自动调整收益输入表格。

Pure Strategy NE: Identifies all possible pure strategy stable points.

纯策略纳什均衡：识别所有可能的纯策略稳定点。

Mixed Strategy NE: Computes probabilistic equilibria and expected payoffs using the Gambit library.

混合策略纳什均衡：利用 Gambit 库计算概率分布均衡及预期收益。

User-Friendly UI: Responsive design built with Bootstrap 5.

用户友好界面：基于 Bootstrap 5 的响应式设计，简洁美观。

🛠️ Tech Stack | 技术栈
Backend: Python, Flask

Game Theory Engine: PyGambit

Frontend: HTML5, Bootstrap 5, JavaScript

Template Engine: Jinja2

🚀 Getting Started | 快速开始
Prerequisites | 环境依赖
Python 3.8+

pip (Python package manager)

Installation | 安装步骤
Clone the repository | 克隆仓库

Bash
git clone https://github.com/your-username/game-theory-solver.git
cd game-theory-solver
Install dependencies | 安装依赖

Bash
pip install flask pygambit
Run the application | 运行程序

Bash
python app.py
Access the tool | 访问页面
Open your browser and navigate to http://127.0.0.1:5000.
打开浏览器访问 http://127.0.0.1:5000。

📖 Usage | 使用说明
Enter the names of Player 1 and Player 2.

Input strategies separated by commas (e.g., Concert, Ballgame).

Fill in the payoffs for each scenario in the dynamically generated matrix.

Click "Solve Nash Equilibria" to view the results.

输入 玩家 1 和 玩家 2 的名称。

输入策略名称，用逗号分隔（例如：Concert, Ballgame）。

在动态生成的矩阵中填入每个场景下的收益。

点击 “计算纳什均衡” 查看结果。

📄 Project Structure | 项目结构
Plaintext
.
├── app.py              # Flask backend logic & Gambit integration
├── templates/
│   ├── index.html      # Input form with dynamic JS matrix
│   └── result.html     # Results display page
└── README.md           # Documentation
