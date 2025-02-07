'use client'
import Link from "next/link";
import "./login.css"
import { usePathname } from "next/navigation";


export default function Layout({ children }) {
    const pathName = usePathname();
    return (
        <div>
            {
                pathName !== "/login/teacherlogin" ?
                    <ul className="login-menu">
                        <li>
                            <h4>Login Navbar</h4>
                        </li>
                        <li>
                            <Link href="/login">Login-Main</Link>
                        </li>
                        <li>
                            <Link href="/login/studentlogin">StudentLogin</Link>
                        </li>
                        <li>
                            <Link href="/login/teacherlogin">TeacherLogin</Link>
                        </li>
                    </ul>
                    :<Link href="/login">Go to Main Login</Link>
                }
            
            {children}
        </div>
    )
}