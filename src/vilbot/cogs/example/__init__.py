from .cog import ExampleCog

def setup(bot):
    bot.add_cog(ExampleCog(bot))

