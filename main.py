import spade


class DummyAgent(spade.agent.Agent):
    async def setup(self):
        print("Hello, I'm agent {}".format(str(self.jid)))


async def main():
    dummy = DummyAgent("dummy@localhost", "passw")
    await dummy.start()


if __name__ == "__main__":
    spade.run(main())
