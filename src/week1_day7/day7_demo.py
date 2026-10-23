
from .tools import add, multiply


class CalculatorAgent:

    def __init__(self, name: str) -> None:
        self.name = name
        self.tools = {
            "add": add,
            "multiply": multiply,
        }
        self.history = []

    def execute(self, tool_name: str, a: float, b: float) -> float:

        tool = self.tools.get(tool_name)

        if tool is None:
            raise ValueError(f"工具 {tool_name} 不存在")

        result = tool(a, b)

        self.history.append({
            "tool": tool_name,
            "result": result,
        })

        return result


def main() -> None:

    # 用同一个类创建两个对象
    agent1 = CalculatorAgent("计算助手A")
    agent2 = CalculatorAgent("计算助手B")

    # 第一个对象连续执行两个操作
    result1 = agent1.execute("add", 20, 4)
    result2 = agent1.execute("multiply", result1, 3)

    print("第一个Agent结果：", result2)
    print("第一个Agent历史：", agent1.history)

    # 第二个对象执行自己的任务
    result3 = agent2.execute("multiply", 10, 5)

    print("第二个Agent结果：", result3)
    print("第二个Agent历史：", agent2.history)

    # 查看 Python 类型和模块
    print("agent1 的类型：", type(agent1))
    print("add 来自哪个模块：", add.__module__)


if __name__ == "__main__":
    main()
