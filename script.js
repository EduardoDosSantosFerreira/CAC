// Custom Cursor
const cursor = document.querySelector('.cursor');
const cursorFollower = document.querySelector('.cursor-follower');

document.addEventListener('mousemove', (e) => {
    cursor.style.transform = `translate(${e.clientX - 4}px, ${e.clientY - 4}px)`;
    cursorFollower.style.transform = `translate(${e.clientX - 20}px, ${e.clientY - 20}px)`;
});

document.addEventListener('mousedown', () => {
    cursor.style.transform += ' scale(0.8)';
    cursorFollower.style.transform += ' scale(1.2)';
});

document.addEventListener('mouseup', () => {
    cursor.style.transform = cursor.style.transform.replace(' scale(0.8)', '');
    cursorFollower.style.transform = cursorFollower.style.transform.replace(' scale(1.2)', '');
});

// Hide cursor when leaving window
document.addEventListener('mouseleave', () => {
    cursor.style.opacity = '0';
    cursorFollower.style.opacity = '0';
});

document.addEventListener('mouseenter', () => {
    cursor.style.opacity = '1';
    cursorFollower.style.opacity = '0.5';
});

// Progress Bar
window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    document.querySelector('.progress-bar').style.width = scrolled + '%';
});

// Loading Screen
window.addEventListener('load', () => {
    setTimeout(() => {
        document.querySelector('.loading-screen').classList.add('hidden');
    }, 1000);
});

// Sticky Navigation
window.addEventListener('scroll', () => {
    const nav = document.querySelector('.nav-sticky');
    if (window.scrollY > 100) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// Mobile Menu Toggle
const menuToggle = document.querySelector('.menu-toggle');
const navMenu = document.querySelector('.nav-menu');

menuToggle.addEventListener('click', () => {
    menuToggle.classList.toggle('active');
    navMenu.classList.toggle('active');
    
    const spans = menuToggle.querySelectorAll('span');
    if (menuToggle.classList.contains('active')) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(7px, -7px)';
    } else {
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
    }
});

// Particles.js
particlesJS('particles-js', {
    particles: {
        number: { value: 80, density: { enable: true, value_area: 800 } },
        color: { value: '#6c5ce7' },
        shape: { type: 'circle' },
        opacity: { value: 0.5, random: true },
        size: { value: 3, random: true },
        line_linked: {
            enable: true,
            distance: 150,
            color: '#6c5ce7',
            opacity: 0.2,
            width: 1
        },
        move: {
            enable: true,
            speed: 2,
            direction: 'none',
            random: true,
            straight: false,
            out_mode: 'out',
            bounce: false
        }
    },
    interactivity: {
        detect_on: 'canvas',
        events: {
            onhover: { enable: true, mode: 'repulse' },
            onclick: { enable: true, mode: 'push' },
            resize: true
        }
    },
    retina_detect: true
});

// Typewriter Effect
const typewriterElement = document.querySelector('.typewriter');
const words = ['Auto Clicker', 'Macro Tool', 'Automation'];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;

function typeWriter() {
    const currentWord = words[wordIndex];
    
    if (isDeleting) {
        typewriterElement.textContent = currentWord.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typewriterElement.textContent = currentWord.substring(0, charIndex + 1);
        charIndex++;
    }
    
    if (!isDeleting && charIndex === currentWord.length) {
        isDeleting = true;
        setTimeout(typeWriter, 2000);
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        setTimeout(typeWriter, 500);
    } else {
        setTimeout(typeWriter, isDeleting ? 50 : 100);
    }
}

typeWriter();

// Counter Animation
const counters = document.querySelectorAll('.stat-number');
const speed = 200;

function animateCounters() {
    counters.forEach(counter => {
        const updateCount = () => {
            const target = parseFloat(counter.getAttribute('data-target'));
            const count = parseFloat(counter.innerText);
            
            const increment = target / speed;
            
            if (count < target) {
                counter.innerText = (count + increment).toFixed(1);
                setTimeout(updateCount, 10);
            } else {
                counter.innerText = target;
            }
        };
        
        updateCount();
    });
}

// Start counters when hero section is visible
const heroObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounters();
        }
    });
}, { threshold: 0.5 });

heroObserver.observe(document.querySelector('.hero-section'));

// Tab System
const tabBtns = document.querySelectorAll('.tab-btn');
const tabPanes = document.querySelectorAll('.tab-pane');

tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        const tabId = btn.getAttribute('data-tab');
        
        tabBtns.forEach(b => b.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));
        
        btn.classList.add('active');
        document.getElementById(tabId).classList.add('active');
    });
});

// 3D Tilt Effect
const tiltCards = document.querySelectorAll('.tilt-card');

tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = (y - centerY) / 10;
        const rotateY = (centerX - x) / 10;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
    });
});

// Scroll Reveal
const revealElements = document.querySelectorAll('.reveal');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, { threshold: 0.1 });

revealElements.forEach(el => revealObserver.observe(el));

// Add reveal class to elements
document.querySelectorAll('.feature-card, .about-content, .download-card').forEach(el => {
    el.classList.add('reveal');
});

// Ripple Effect
document.querySelectorAll('.ripple-effect').forEach(btn => {
    btn.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        this.appendChild(ripple);
        
        const x = e.clientX - e.target.offsetLeft;
        const y = e.clientY - e.target.offsetTop;
        
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
});

// Download Button with Animation
const downloadBtn = document.getElementById('downloadBtn');

downloadBtn.addEventListener('click', () => {
    // Simulate download
    downloadBtn.innerHTML = '<span>Downloading...</span><div class="loader-shape"></div>';
    downloadBtn.style.pointerEvents = 'none';
    
    setTimeout(() => {
        downloadBtn.innerHTML = '<span>Download Complete!</span><svg class="btn-icon" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/></svg>';
        
        // Show success message
        const toast = document.createElement('div');
        toast.classList.add('glass-effect');
        toast.style.position = 'fixed';
        toast.style.bottom = '20px';
        toast.style.right = '20px';
        toast.style.padding = '1rem 2rem';
        toast.style.borderRadius = '50px';
        toast.style.zIndex = '9999';
        toast.textContent = 'Download started successfully!';
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.remove();
        }, 3000);
    }, 2000);
});

// Parallax Effect
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.shape, .floating-shape');
    
    parallaxElements.forEach(el => {
        const speed = 0.5;
        el.style.transform = `translateY(${scrolled * speed}px)`;
    });
});

// Smooth Scroll for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Dynamic Blur Effect on Scroll
window.addEventListener('scroll', () => {
    const heroSection = document.querySelector('.hero-section');
    const blurValue = Math.min(window.scrollY / 100, 10);
    heroSection.style.filter = `blur(${blurValue}px)`;
});

// Add hover underline animation to all links
document.querySelectorAll('a').forEach(link => {
    if (!link.classList.contains('nav-link')) {
        link.style.position = 'relative';
        link.style.overflow = 'hidden';
        
        link.addEventListener('mouseenter', () => {
            const underline = document.createElement('span');
            underline.style.position = 'absolute';
            underline.style.bottom = '0';
            underline.style.left = '0';
            underline.style.width = '100%';
            underline.style.height = '2px';
            underline.style.background = 'linear-gradient(90deg, var(--primary), var(--secondary))';
            underline.style.transform = 'translateX(-100%)';
            underline.style.transition = 'transform 0.3s';
            underline.style.zIndex = '-1';
            
            link.appendChild(underline);
            
            setTimeout(() => {
                underline.style.transform = 'translateX(0)';
            }, 10);
            
            link.addEventListener('mouseleave', () => {
                underline.style.transform = 'translateX(100%)';
                setTimeout(() => {
                    underline.remove();
                }, 300);
            }, { once: true });
        });
    }
});

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    console.log('Crow Auto Clicker website initialized');
});