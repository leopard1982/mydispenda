import { Controller, Get, Param, ParseIntPipe } from '@nestjs/common';
import { isAlpha, isAlphanumeric, isNumber } from 'class-validator';

@Controller('')
export class AppController {
	@Get()
	getWelcome() {
		return "<h1>Hello World!</h1>";
	}

	
}
