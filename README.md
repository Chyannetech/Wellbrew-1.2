## Wellbrew

#### Wellbrew is a full-stack app that uses the Python-based Django Web Framework to track vendors at farmers mmarkets. Users are able to access vendor information which is managed and updated by an admin user account. 

* Visit the deployed app here: [Wellbrew](https://wellbrew.herokuapp.com/)

<img width="500" alt="Home Page" src="https://user-images.githubusercontent.com/103911002/179635950-dc90bdcb-c602-4491-b5a7-28aa652a6570.png">

<img width="500" alt="Sign Up" src="https://user-images.githubusercontent.com/103911002/178975124-683379dd-5dba-46e7-b40b-defa7c82d7d7.png">

## Table of Contents
* [Technologies Used](#technologiesused)
* [MVP](#MVP)
* [Main Django Model](#maindjangomodel)
* [Main Template](#maintemplate)
* [Routes](#routes)
* [Post MVP](#postmvp)
* [Deployed App](#deployment)


## <a name="technologiesused"></a>Technologies Used
* HTML5
* CSS3
* Python
* Django
* Postgresql
* Materialize UI
* Ion-Icon
* Google Fonts

## <a name="MVP"></a>MVP
* Full-stack Django Application
* Persist data in PostgreSQL
* Authenticate users using Django's built in authentication
* Implemement authorization by restricting access to the creation, updating, and deleting of resources.
* Deployed online using Heroku

## <a name="maindjangomodel"></a>Main Django Model 
``` class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    social = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'business_id': self.id})
 ```
## <a name="maintemplate"></a>Main Django Template 
``` 
<h1>Business Details</h1>

<div class="card">
    <div class="card-content">
        <span class="card-title">{{ business.name }}</span>
        <p>Address: {{ business.address }}</p>
        <p>Phone: {{ business.phone }}</p>
        <p>Social: {{ business.social }}</p>
        <p>Website: {{ business.website }}</p>
    </div>
    <div class="card-action">
        <a href="{% url 'businesses_update' business.id %}">Edit</a>
        <a href="{% url 'businesses_delete' business.id %}">Delete</a>
    </div>
</div>
```
## <a name="routes"></a>Routes  
```
urlpatterns = [
    path('', views.home, name='home'),
    path('directory/', views.directory, name='directory'),
    path('businesses/', views.businesses_index, name='index'),
    path('businesses/<int:business_id>/', views.businesses_detail, name='detail'),
    path('businesses/create', views.BusinessCreate.as_view(), name='businesses_create'),
    path('businesses/<int:pk>/update/', views.BusinessUpdate.as_view(), name='businesses_update'),
    path('businesses/<int:pk>/delete/', views.BusinessDelete.as_view(), name='businesses_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
```

## <a name="deployment"></a>Deployed Link
* Visit the deployed app here: [Wellbrew](https://wellbrew.herokuapp.com/)

## Project Schedule
|  Day | Deliverable | Status
|---|---| ---|
|July 9| Wireframes amnd Timeframes | Complete
|July 10| Project Approval | Complete
|July 11| Connect Database and CUD routes| Complete
|July 12| Full CRUD and Create Form | Complete
|July 13| Add User Authorization and Deploy  | Complete
|July 14-15| CSS Styling | Complete
|July 16| MVP | Complete
|July 18| Presentations | Complete

## <a name="postmvp"></a>Post MVP
* Add a catgory model to link vendor information to the homepage and directory.
* Additional CSS to match prototype
![wireflow2](https://user-images.githubusercontent.com/103911002/180382121-6f4770dc-d186-47ba-aa7a-9ae99a23bcde.png)

* View the prototype [here.](https://www.figma.com/proto/KF6Do2q6FTRQAE8PccbngJ/Wellbrew?node-id=20%3A45&scaling=scale-down&page-id=0%3A1&starting-point-node-id=20%3A45)

### Strengths:
I had a clear vision of what I wanted my application to look like and the docuemntation was a great reference for getting things set up quickly. Futhermore, Materilize UI was used for styling which allowed for much more creativity in the design. 
### Weaknesses:
Staying on task with MVP and not letting feature creep take over.  
### Opportunities:
To reinforce all of the concepts learned during this project and get more reps in using PostgreSQL. 


* Background image by one of Disney's amazing artist: [Nicholas Kennedy](https://paintwithnick.artstation.com/projects/W2dDZy)



