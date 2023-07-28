from django.http import Http404

from .models import Present


class PresentRepository:
    def get_present_by_id(self, pk):
        try:
            return Present.objects.get(id=pk)
        except:
            raise Http404("Объект не найден")

    def create_present(self, **kwargs):
        return Present.objects.create(**kwargs)

    def delete_present(self, pk):
        present = self.get_present_by_id(pk)
        present.delete()

    def update_present(self, pk, name=None, description=None, image=None, url=None):
        present = self.get_present_by_id(pk)

        def update(pr_name=present.name,
                   pr_description=present.description,
                   pr_image=present.image,
                   pr_url=present.url):
            present.name = pr_name
            present.description = pr_description
            present.image = pr_image
            present.url = pr_url
            present.save()
            return present

        return update(name, description, image, url)


class PresentService:
    def __init__(self):
        self.repository = PresentRepository()

    def create_present(self, **kwargs):
        return self.repository.create_present(**kwargs)

    def update_present(self, pk, name=None, description=None, image=None, url=None):
        return self.repository.update_present(pk, name, description, image, url)

    def get_present_by_id(self, pk):
        return self.repository.get_present_by_id(pk)

    def delete_present(self, pk):
        self.repository.delete_present(pk)
