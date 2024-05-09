import { Module } from '@nestjs/common';
import { UsersModule } from './users/users.module';
import { AppController } from './app/app.controller';
import {TypeOrmModule} from '@nestjs/typeorm';
import { Users } from './typeorm/entities/Users';
import { MydbModule } from './mydb/mydb.module';


@Module({
  imports: [UsersModule, TypeOrmModule.forRoot({
    type:'postgres',
    host: 'localhost',
    port: 5432,
    username: 'admin',
    password: 'chandra1982',
    database: 'mydispenda',
    entities:[Users],
    synchronize:true
  }), MydbModule],
  controllers: [AppController],
  providers: [],
})
export class AppModule {}
