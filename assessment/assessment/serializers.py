from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "Invalid email or password"})

        if not user.check_password(password):
            raise serializers.ValidationError({"detail": "Invalid email or password"})

        if not user.is_active:
            raise serializers.ValidationError({"detail": "User is inactive"})

        # Generate tokens
        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "email": user.email,
            "user_id": user.id
        }