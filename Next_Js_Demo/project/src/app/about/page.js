'use client'
import {useRouter} from "next/navigation"
import Link from "next/link"
const About=()=>{
    const router=useRouter();
    return(
        <div>
            <h1>About Page</h1>
            <button onClick={()=>router.push("/")}>Go to Home Page</button>
            <br/> <br/>
            <Link href="about/aboutstudent">Go to About student page</Link>
            <br/><br/>
            <Link href="about/aboutcollege">Go to About Collage Page</Link>
        </div>
    )
}

export default About;