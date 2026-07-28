import { Component,OnInit } from '@angular/core';

import { CourseService }

from '../../services/course.service';

@Component({

selector:'app-course-list',

templateUrl:'./course-list.component.html',

styleUrls:['./course-list.component.css']

})

export class CourseListComponent

implements OnInit{

courses:any[]=[];

searchTerm='';

loading=true;

constructor(

private courseService:CourseService

){}

ngOnInit():void{

this.courseService

.getCourses()

.subscribe(data=>{

this.courses=data;

this.loading=false;

});

}

get filteredCourses(){

return this.courses.filter(course=>

course.title

.toLowerCase()

.includes(

this.searchTerm.toLowerCase()

)

);

}

}
