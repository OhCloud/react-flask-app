import React from 'react';
import { Link } from "react-router-dom"
import BootstrapCard from 'react-bootstrap/Card';


const myCards = ['https://images.unsplash.com/photo-1428908728789-d2de25dbd4e2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1050&q=80']

export const Card = ({ listTodos }) => {
    return(
        <>
            {listTodos.map(todo => {
                return(
                    <BootstrapCard>
                        <img src={myCards[0]}></img>
                            <ul key={todo.id}>
                                <li>
                                    <BootstrapCard body><Link to={`${todo.id}`}>{todo.content}</Link></BootstrapCard>
                                </li>
                            </ul>
                    </BootstrapCard>
                )
            })}
        </>
    )
}