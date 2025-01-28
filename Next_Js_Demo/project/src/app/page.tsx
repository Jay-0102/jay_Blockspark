'use client'
import Link from "next/link";
import {useRouter} from "next/navigation"
export default function Home() {
  const router=useRouter();
  return (
    
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <h1>Home page</h1>
        <User name="jay"/>
        <User name="anjali"/>
        <Link href="/login">Go to Login Page</Link>
        <br/>
        <br/>
        <Link href="/about">Go to About Page</Link>
      
        <button onClick={()=>router.push("/login")}>Login</button>
        <button onClick={()=>router.push("/about")}>About</button>


        </main>
      
    </div>
  );
}

//component
const User=(nm)=>{
  return(
    <div>
      <h2>Welcome {nm.name}</h2>
    </div>
  )
}