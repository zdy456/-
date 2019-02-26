from django_redis import get_redis_connection
from redis import StrictRedis
from rest_framework.response import Response
from rest_framework.views import APIView


class CartsCountView(APIView):

    def get(self, request):
        # 是否为登录状态
        if request.user.is_authenticated():  # 登录
            user = request.user
            print(user.id)
            # 从redis中获取值
            strict_redis = get_redis_connection('cart')  # type:StrictRedis
            skus = strict_redis.hgetall('cart_%s' % user.id)
            skus_id = strict_redis.smembers('cart_selected_%s' % user.id)
            # 统计总数量
            count = 0
            if skus_id:
                for sku_id in skus:
                    if sku_id in skus_id:
                        count += int(skus[sku_id])

        else:  # 未登录
            # 获取cookie
            carts = request.COOKIES.get('carts')
            print(carts)
            # 统计总数量
            count = 0
            if carts:
                for sku in carts:
                    if sku['selected']:
                        count += sku['count']
        # 返回总数量
        return Response({'count': count})