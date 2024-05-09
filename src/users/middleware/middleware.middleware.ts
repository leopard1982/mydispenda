import { HttpException, HttpStatus, Injectable, NestMiddleware } from '@nestjs/common';
import { NextFunction, Request, Response } from 'express';

@Injectable()
export class MiddlewareMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    const {authorization,tokennya} = req.headers;
    if(!authorization) {
      res.json({
        'statusCode':HttpStatus.FORBIDDEN,
        "msg": {
          "pesan":"Tanpa Otorisasi, ga boleh lanjot!"
        }
      });
    }
    else 
      return next();
  }
}
