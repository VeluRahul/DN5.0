import {

createSlice,

createAsyncThunk

}

from "@reduxjs/toolkit";

import {

getAllCourses

}

from "../api/courseApi";

export const fetchAllCourses = createAsyncThunk(

"courses/fetchAll",

async()=>{

return await getAllCourses();

}

);

const courseSlice = createSlice({

name:"courses",

initialState:{

courses:[],

loading:false,

error:null

},

reducers:{},

extraReducers:(builder)=>{

builder

.addCase(

fetchAllCourses.pending,

(state)=>{

state.loading=true;

state.error=null;

}

)

.addCase(

fetchAllCourses.fulfilled,

(state,action)=>{

state.loading=false;

state.courses=action.payload;

}

)

.addCase(

fetchAllCourses.rejected,

(state,action)=>{

state.loading=false;

state.error=

action.error.message;

}

);

}

});

export default courseSlice.reducer;
