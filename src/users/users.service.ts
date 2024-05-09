import { Injectable } from '@nestjs/common';
import { CreateUserType } from 'src/app/app.type';

@Injectable()
export class UsersService {
    private fakeUsers =  [
        {
            username:'suryo',
            password: 'chandra',
            email: 'suryo@chandra.com'
        },
        {
            username:'adhy',
            password: 'chandra2',
            email: 'suryo@chandra2.com'
        },
        {
            username:'chandra',
            password: 'chandra3',
            email: 'suryo@chandr3a.com'
        }
    ]

    fetchUser(ascId:boolean) {
        if(ascId) {
            return  this.fakeUsers.sort((a,b)=> {
                if(a.username>b.username) return 1;
                if(a.username<b.username) return -1;
            });
        } else {
            return  this.fakeUsers.sort((a,b)=> {
                if(a.username>b.username) return -1;
                if(a.username<b.username) return 1;
            });
        }
        
    }

    insertUser(mydata : CreateUserType ) : any { 
        this.fakeUsers.push(mydata);
        return this.fakeUsers;
    }

    fetchUserByID(username:string) : any {
        const mydata = this.fakeUsers.filter((data)=>data.username===username.trim()&&true);
        return mydata;
    }
}
