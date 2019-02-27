from django_redis import get_redis_connection
from redis import StrictRedis
from rest_framework.response import Response
from rest_framework.views import APIView


class CartsCountView(APIView):

    def get(self, request):
        """
        购物车商品数量统计
        """
        count = 0
        # 是否为登录状态
        if request.user.is_authenticated():  # 登录
            user = request.user
            strict_redis = get_redis_connection('cart')  # type:StrictRedis

            values = strict_redis.hvals('cart_%s' % user.id)
            print(values)
            # 统计总数量
            if values:
                for val in values:
                    count += int(val)
        else:  # 未登录
            carts = request.COOKIES.get('carts')
            print(carts)

            # 统计总数量
            if carts:
                for sku in carts:
                    count += sku['count']

        return Response({'count': count})