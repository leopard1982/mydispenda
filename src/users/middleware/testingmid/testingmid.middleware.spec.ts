import { TestingmidMiddleware } from './testingmid.middleware';

describe('TestingmidMiddleware', () => {
  it('should be defined', () => {
    expect(new TestingmidMiddleware()).toBeDefined();
  });
});
