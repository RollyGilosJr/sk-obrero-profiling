from django.db import models

# Create your models here.
class Profile (models.Model):
       
    sex_choices = (
        ("Male","Male"),
        ("Female","Female"),
    )
    civil_status_choices = (
        ("Single","Single"),
        ("Married","Married"),
        ("Widowed","Widowed"),
        ("Divorced","Divorced"),
        ("Separated","Separated"),
        ("Annulled","Annulled"),
        ("Unknown","Unknown"),
        ("Live-in","Live-in"),
    )

    youth_classification_choices = (
        ("In School Youth","In School Youth"),
        ("Out of School youth","Out of School youth"),
        ("Working Youth","Working Youth"),
        ("Person with Disability", "Youth With Special Needs - PWD"),
        ("Children in Conflict with Law", "Youth With Special Needs - CCL"),
        ("Indigenous People", "Youth With Special Needs - IP"),
        
    )

    youth_age_group_choices = (
        ("Child Youth","Child Youth (15-17 yrs. old)"),
        ("Core Youth","Core Youth (18-24 yrs. old)"),
        ("Young Adult","Young Adult (25-30 yrs. old)"),
    )

    work_status_choices = (
        ("Employed","Employed"),
        ("Unemployed","Unemployed"),
        ("Self-Employed","Self-Employed"),
        ("Currently Looking For a Job","Currently Looking For a Job"),
        ("Not interested Looking for a Job","Not interested Looking for a Job"),
    )

    educational_background_choices = (
        ("Elementary Level","Elementary Level"),
        ("Elementary Graduate","Elementary Graduate"),
        ("High School Level","High School Level"),
        ("High School Graduate","High School Graduate"),
        ("Vocational Graduate","Vocational Graduate"),
        ("College Level","College Level"),
        ("College Graduate","College Graduate"),
        ("Masters Level","Masters Level"),
        ("Masters Graduate","Masters Graduate"),
        ("Doctorate Level","Doctorate Level"),
        ("Doctorate Graduate","Doctorate Graduate"),    
    )

    yes_or_no = (
        ("Yes","Yes" ),
        ("No","No")
    )

    

    full_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250)
    suffix = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    region = models.CharField(max_length=250, null=True, blank=True, default="5")
    province = models.CharField(max_length=250, null=True, blank=True, default="Sorsogon")
    municipality = models.CharField(max_length=250, null=True, blank=True, default="Bulan")
    barangay = models.CharField(max_length=250, null=True, blank=True, default="Obrero")
    purok = models.CharField(max_length=250, null=True, blank=True)
    sex = models.CharField(max_length=250, null=True, blank=True, choices=sex_choices)
    age = models.CharField(max_length=250, null=True, blank=True)
    birthday = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    contact_number = models.CharField(max_length=250, null=True, blank=True)
    civil_status = models.CharField(max_length=250, choices=civil_status_choices, null=True, blank=True)
    youth_classification = models.CharField(max_length=250, choices=youth_classification_choices, null=True, blank=True)
    youth_age_group = models.CharField(max_length=250, choices=youth_age_group_choices, null=True, blank=True)
    work_status = models.CharField(max_length=250, choices=work_status_choices, null=True, blank=True)
    educational_background = models.CharField(max_length=250, choices=educational_background_choices, null=True, blank=True)
    sk_voter = models.CharField(max_length=100, choices=yes_or_no, null=True, blank=True)
    national_voter = models.CharField(max_length=100, choices=yes_or_no, null=True, blank=True)
    
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.full_name

