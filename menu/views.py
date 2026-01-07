from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Menu, Booking
from .forms import BookingForm
from .serializers import MenuSerializer, BookingSerializer, RegisterSerializer
from .permissions import IsAdminOrReadOnly


# ---------- PAGES HTML ----------

def home(request):
    menu_data = Menu.objects.all()
    return render(request, 'index.html', {'menu': {'menu': menu_data}})


def about(request):
    return render(request, 'about.html')

from django.http import HttpResponse


def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('book_detail')
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})



def book_detail(request):
    return render(request, 'book_detail.html')


def liste_book(request):
    return render(request, 'liste_book.html')


def display_menu_item(request, pk):
    menu_item = Menu.objects.get(pk=pk)
    return render(request, 'menu_item.html', {'menu_item': menu_item})

def register(request):
    menu_data = Menu.objects.all()
    return render(request, 'register.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            return render(request, 'login.html', {'error': 'Identifiants invalides'})
    return render(request, 'login.html')

# ---------- API ----------

class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrReadOnly]


class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrReadOnly]


class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Booking.objects.filter(user=self.request.user)
        date = self.request.GET.get('date')
        if date:
            queryset = queryset.filter(date=date)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ---------- REGISTER ----------

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
