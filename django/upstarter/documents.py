from django_elasticsearch_dsl import DocType, Index

from upstarter.models import Project

project_index = Index('projects')

project_index.settings(
    number_of_shards=1,
    number_of_replicas=0,
)


@project_index.doc_type
class ProjectDocument(DocType):
    class Meta:
        model = Project
        fields = ('name', 'description', 'tags')
