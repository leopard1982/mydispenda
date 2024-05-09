import { Module } from '@nestjs/common';
import { MydbController } from './mydb.controller';
import { MydbService } from './mydb.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Users } from 'src/typeorm/entities/Users';

@Module({
  imports: [TypeOrmModule.forFeature([Users])],
  controllers: [MydbController],
  providers: [MydbService]
})
export class MydbModule {}
