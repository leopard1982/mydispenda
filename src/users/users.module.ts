import { MiddlewareConsumer, Module, NestModule, RequestMethod } from '@nestjs/common';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';
import { MiddlewareMiddleware } from './middleware/middleware.middleware';
import { TestingmidMiddleware } from './middleware/testingmid/testingmid.middleware';

@Module({
  controllers: [UsersController],
  providers: [UsersService]
})
export class UsersModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
      consumer.apply(MiddlewareMiddleware).forRoutes(
        {
          path: 'users',
          method: RequestMethod.GET
        },
        {
          path: 'users/:username',
          method: RequestMethod.GET
        }
    ).apply(TestingmidMiddleware).forRoutes(
      {
          path: 'users',
          method: RequestMethod.GET
      },
      {
          path: 'users/:username',
          method: RequestMethod.GET
      }
    );
  }
}
