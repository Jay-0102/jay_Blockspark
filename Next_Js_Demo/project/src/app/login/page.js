'use client'
import Link from "next/link";
import { useRouter } from "next/navigation";
const Login =()=>{
    const router=useRouter();
    return(
        <div>
            <h1>Login Page</h1>
            <br/>
            <br/>
            <Link href="/">Go to Home Page</Link>
            <br/><br/>
            <button onClick={()=>router.push("login/studentlogin")}>Go to Student Login Page</button>
            <br/>
            <button onClick={()=>router.push("login/teacherlogin")}>Go to Teacher Login page</button>
        </div>
    )
}

export default Login;