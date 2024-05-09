import { Test, TestingModule } from '@nestjs/testing';
import { MydbController } from './mydb.controller';

describe('MydbController', () => {
  let controller: MydbController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [MydbController],
    }).compile();

    controller = module.get<MydbController>(MydbController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
