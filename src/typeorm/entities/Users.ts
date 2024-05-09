import { Column, Entity, PrimaryGeneratedColumn } from "typeorm";

@Entity({name:'myuser'})
export class Users {
    @PrimaryGeneratedColumn({type:'bigint'})
    id: number;

    @Column({nullable:false,unique:true})
    username: string;

    @Column({nullable:false})
    password: string;

    @Column({nullable:false})
    email: string;

    @Column()
    usia: number;

    @Column()
    createdAt: Date;

    @Column()
    updatedAt: Date;

}