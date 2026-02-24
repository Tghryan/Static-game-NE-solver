import pygambit as gbt
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 1. 获取基础设定
        p1_name = request.form.get('p1_name', 'Player 1')
        p2_name = request.form.get('p2_name', 'Player 2')
        p1_strats = [s.strip() for s in request.form.get('p1_strats').split(',') if s.strip()]
        p2_strats = [s.strip() for s in request.form.get('p2_strats').split(',') if s.strip()]

        n, m = len(p1_strats), len(p2_strats)

        # 2. 初始化博弈模型
        g = gbt.Game.new_table([n, m])
        g.title = f"{p1_name} vs {p2_name}"
        g.players[0].label = p1_name
        g.players[1].label = p2_name

        for i, strat in enumerate(p1_strats):
            g.players[0].strategies[i].label = strat
        for j, strat in enumerate(p2_strats):
            g.players[1].strategies[j].label = strat

        # 3. 解析动态生成的收益矩阵并填入模型
        for i in range(n):
            for j in range(m):
                p1_payoff = float(request.form.get(f'payoff_p1_{i}_{j}', 0))
                p2_payoff = float(request.form.get(f'payoff_p2_{i}_{j}', 0))
                
                # 【修复 1】: 使用字符串变量 p1_name 和 p2_name 指定玩家，而不是用 0 和 1
                g[i, j][p1_name] = p1_payoff
                g[i, j][p2_name] = p2_payoff

        # 4. 求解均衡
        psne_raw = gbt.nash.enumpure_solve(g)
        msne_raw = gbt.nash.enummixed_solve(g)

        # 5. 格式化纯策略结果以便前端友好渲染
        psne_results = []
        # 【修复 2】: 使用 .equilibria 属性来遍历 NashComputationResult 对象
        for eq in psne_raw.equilibria:
            p1_choice = [s.label for s in g.players[0].strategies if eq[s] > 0][0]
            p2_choice = [s.label for s in g.players[1].strategies if eq[s] > 0][0]
            psne_results.append({
                'p1_choice': p1_choice,
                'p2_choice': p2_choice,
                'p1_payoff': round(float(eq.payoff(g.players[0])), 2),
                'p2_payoff': round(float(eq.payoff(g.players[1])), 2)
            })

        # 6. 格式化混合策略结果
        msne_results = []
        # 【修复 2】: 同样使用 .equilibria 属性
        for eq in msne_raw.equilibria:
            p1_probs = {s.label: f"{float(eq[s]):.1%}" for s in g.players[0].strategies if float(eq[s]) > 0}
            p2_probs = {s.label: f"{float(eq[s]):.1%}" for s in g.players[1].strategies if float(eq[s]) > 0}
            msne_results.append({
                'p1_probs': p1_probs,
                'p2_probs': p2_probs,
                'p1_payoff': round(float(eq.payoff(g.players[0])), 2),
                'p2_payoff': round(float(eq.payoff(g.players[1])), 2)
            })

        # 渲染结果页面
        return render_template('result.html', 
                               p1_name=p1_name, p2_name=p2_name,
                               psne=psne_results, msne=msne_results)

    # 如果是 GET 请求，渲染输入表单页面
    return render_template('index.html')

if __name__ == '__main__':
    # 启动应用，开启 debug 模式便于开发
    app.run(debug=True)