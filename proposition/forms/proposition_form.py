# pylint: disable=E1101,R0903
"""PropositionForm module.
"""
from django.forms import (
    CharField, DateField, DateInput, IntegerField, ModelChoiceField, ModelForm,
    NumberInput, Select, Textarea, TextInput
)
from proposition.models import (
    Category, CreatorType, Domain, Kind, Proposition
)


class PropositionForm(ModelForm):
    """PropositionForm class. Used for adding proposition.
    """
    name = CharField(
        label='Intitulé',
        max_length=128,
        widget=TextInput(
            attrs={
                'id': 'input_proposition_name',
                'class': 'form-control form-control-sm',
                'autofocus': True,
            }
        )
    )
    description = CharField(
        label='Description',
        max_length=1000,
        widget=Textarea(
            attrs={
                'id': 'input_proposition_description',
                'class': 'form-control form-control-sm',
                'rows': 4
            }
        )
    )
    proposition_kind = ModelChoiceField(
        queryset=Kind.objects.all(),
        label='Type de proposition (demande/offre)',
        empty_label="",
        widget=Select(
            attrs={
                'id': 'input_proposition_proposition_kind',
                'class': 'form-control form-control-sm',
            },
        )
    )
    proposition_category = ModelChoiceField(
        queryset=Category.objects.all(),
        label='Nature (activité/produit)',
        empty_label="",
        widget=Select(
            attrs={
                'id': 'input_proposition_proposition_category',
                'class': 'form-control form-control-sm',
            },
        )
    )
    proposition_domain = ModelChoiceField(
        queryset=Domain.objects.all(),
        label='Domaine',
        empty_label="",
        widget=Select(
            attrs={
                'id': 'input_proposition_proposition_domain',
                'class': 'form-control form-control-sm',
            },
        )
    )
    start_date = DateField(
        label='Date de début de proposition',
        widget=DateInput(
            attrs={
                'id': 'input_proposition_start_date',
                'type': 'date',
                'class': 'input-group date form-control form-control-sm',
                'data-target-input': "nearest",
            }
        )
    )
    end_date = DateField(
        label='Date de fin de proposition',
        widget=DateInput(
            attrs={
                'id': 'input_proposition_end_date',
                'type': 'date',
                'class': 'input-group date form-control form-control-sm',
                'data-target-input': "nearest",
            }
        )
    )
    duration = IntegerField(
        label='Temps de travail (minutes)',
        min_value=1,
        widget=NumberInput(
            attrs={
                'id': 'input_proposition_duration',
                'class': 'form-control form-control-sm',
            }
        )
    )
    proposition_creator_type = ModelChoiceField(
        queryset=CreatorType.objects.all(),
        label='Portée de la proposition',
        empty_label="",
        widget=Select(
            attrs={
                'id': 'input_proposition_proposition_creator_type',
                'class': 'form-control form-control-sm',
            },
        )
    )

    class Meta:
        """ModelForm "inner" metadata class.
        """
        model = Proposition
        fields = (
            'name', 'description', 'proposition_kind', 'proposition_category',
            'proposition_domain', 'start_date', 'end_date', 'duration',
            'proposition_creator_type'
        )

    def clean(self):
        """Method validating Form field on custom criteria.
        """
        cleaned_data = super().clean()
        try:
            kind = Kind.objects.get(name__exact='Offre')
            creator_type = CreatorType.objects.get(name__exact='Collective')
            if cleaned_data['start_date'] > cleaned_data['end_date']:
                self.add_error(None, "Date de fin < Date de début")
            if (
                cleaned_data['proposition_kind'].name == kind.name and
                cleaned_data['proposition_creator_type']
                .name == creator_type.name
            ):
                self.add_error(
                    'proposition_creator_type',
                    "Une offre ne peut pas être collective"
                )
        except KeyError:
            pass
        return cleaned_data
