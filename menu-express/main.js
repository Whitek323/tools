import { Menu } from "./menu.js"
import { Order } from "./order.js"
import { Person } from "./person.js"

let user_data = [
    [1,"Saran C"],
    [2,"Fuangfar Wiwong"]
]

let i=0;
while(i<user_data.length){
    console.log(user_data[i][1]);
    i++
}
let oat = new Person("oat")
let menu1 = new Menu("ผัดกระเพรา",60)
console.log(menu1.name+" "+menu1.price)