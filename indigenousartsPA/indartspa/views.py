from django.shortcuts import render
# import the models you created in models.py 
from indartspa.models import Submission
# from indartspa.forms import SubmissionForm 

# Create your methods here: 

# renders your home page 
def home(request):
    return render(request,'home.html')

# renders the gallery page to view all submissions 
def all_submissions(request):
    submission = Submission.objects.all() 
    return render(request, 'submissions.html', {'submission': submission})

# renders a details page to view details on a single submission
def single_submission(request, id):
    submission = Submission.objects.get(pk=id)
    return  render(request, 'artist.html', {
        'submission': submission
    }) 

# create a new submission
def new_submission(request): 
  form = SubmissionForm(request.POST)
  if form.is_valid(): 
    new_submission = form.save (commit=False)
    new_submission.save()
    return redirect('homepage')
  else: 
    return render(request, 'submit.html', {'form': form}) 

# view all artists 

def artists(request): 
    pass


