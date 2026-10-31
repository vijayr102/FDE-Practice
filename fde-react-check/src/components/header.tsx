import { Link } from "react-router-dom";

export function header(){
    return (<header>
        <h1>Diabetic Patient Management System</h1>
        <Link to="/">All Patients</Link>
        <br />
        <Link to="/search">Search</Link>
    </header>);
}