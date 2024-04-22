from rest_framework import serializers
from dispenda_surat.models import ExtendUser


class serialUser(serializers.ModelSerializer):
	class Meta:
		model = ExtendUser
		fields = [
			"master_view","master_add","master_update","master_delete",
			"approve_view","approve_add","approve_update","approve_delete",
			"surattugas_view","surattugas_add","surattugas_update","surattugas_delete",
			"laporan_view","laporan_add","laporan_update","laporan_delete",
			"is_superuser","username","desc"
		]