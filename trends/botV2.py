
from .models import Trend
from .models import TrendNews

class BotV2():
    NAME_OF_BOT = "BotV2"
    def Command(self,command):
        if command == "trend_list":
            trends = Trend.objects.all()
            text = "Trends : "
            for trend in trends:
                text += f" {trend} ;"
            TrendNews.objects.create(text=text,from_user=self.NAME_OF_BOT)
            return f"{self.NAME_OF_BOT} is created news"
        return
    
    def created_trend(self,trend:Trend):
        text = f"Trend {trend.idea} is created"
        from_user = self.NAME_OF_BOT
        TrendNews.objects.create(text=text,from_user=from_user)
        return f"{self.NAME_OF_BOT} is posting news"
        
    def deleted_trend(self,trend:Trend):
        text = f"Trend {trend.idea} is deleted"
        from_user = self.NAME_OF_BOT
        TrendNews.objects.create(text=text,from_user=from_user)
        return f"{self.NAME_OF_BOT} is posting news"