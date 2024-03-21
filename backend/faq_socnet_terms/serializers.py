from rest_framework import serializers
from faq_socnet_terms.models import FAQ, SocialNetworks, Terms


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ('id','question','answer','is_published')



class SocialNetworksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SocialNetworks
        fields = ('title','link','is_published')


class TermsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Terms
        fields = ('title','text','is_published')

