import { CanActivate, ExecutionContext, Injectable } from '@nestjs/common';
import { Observable } from 'rxjs';

@Injectable()
export class MyguardGuard implements CanActivate {
  canActivate(
    context: ExecutionContext,
  ): boolean | Promise<boolean> | Observable<boolean> {
    const myreq = context.switchToHttp().getRequest();

    if(!myreq.headers.authorization) {
      return false;
    } else {
      return true;
    }

  }
}
