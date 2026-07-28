import React from "react";

class ErrorBoundary extends React.Component{

constructor(props){

super(props);

this.state={

hasError:false

};

}

static getDerivedStateFromError(){

return{

hasError:true

};

}

componentDidCatch(error,errorInfo){

console.error(

"Application Error :",

error,

errorInfo

);

}

render(){

if(this.state.hasError){

return(

<div
style={{
padding:"40px",
textAlign:"center"
}}
>

<h1>

Something Went Wrong

</h1>

<p>

Please Try Again Later

</p>

</div>

);

}

return this.props.children;

}

}

export default ErrorBoundary;
