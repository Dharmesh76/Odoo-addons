/** @odoo-module **/

import { registry } from "@web/core/registry";
const { component, useState } = owl;

export class OwlTodoList extend component{
    setup(){
        this.state = useState({value: 1})
    }
}

OwlTodoList.template = 'owl.Todolist'
registry.category('action').add('owl.action_todo_list_js', OwlTodoList)