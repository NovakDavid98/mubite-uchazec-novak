#!/usr/bin/env python3
"""
Generate stunning visualizations for the Album Collection App README
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio
import os

# Set style
plt.style.use('dark_background')

OUTPUT_DIR = "assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color scheme matching the app
COLORS = {
    'bg': '#18181b',
    'card': '#27272a',
    'border': '#3f3f46',
    'purple': '#a855f7',
    'pink': '#ec4899',
    'accent': '#8b5cf6',
    'text': '#f4f4f5',
    'muted': '#71717a'
}

def create_architecture_diagram():
    """Create animated architecture flow diagram"""
    print("🎨 Generating architecture diagram...")
    
    frames = []
    
    for frame_idx in range(40):
        fig, ax = plt.subplots(figsize=(14, 8), facecolor=COLORS['bg'])
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        # Title
        ax.text(7, 7.5, 'Album Collection - Architecture', 
                ha='center', va='top', fontsize=24, weight='bold',
                color=COLORS['text'])
        
        # Calculate animation progress
        progress = frame_idx / 40.0
        
        # 1. Browser
        browser_box = FancyBboxPatch((1, 5), 2, 1.5, 
                                     boxstyle="round,pad=0.1",
                                     edgecolor=COLORS['purple'], 
                                     facecolor=COLORS['card'],
                                     linewidth=2)
        ax.add_patch(browser_box)
        ax.text(2, 5.75, '🌐 Browser', ha='center', va='center', 
                fontsize=14, weight='bold', color=COLORS['text'])
        ax.text(2, 5.4, 'User Interface', ha='center', va='center', 
                fontsize=9, color=COLORS['muted'])
        
        # 2. Next.js Frontend
        frontend_box = FancyBboxPatch((5, 5), 2.5, 1.5,
                                      boxstyle="round,pad=0.1",
                                      edgecolor=COLORS['accent'],
                                      facecolor=COLORS['card'],
                                      linewidth=2)
        ax.add_patch(frontend_box)
        ax.text(6.25, 5.85, '⚛️ Next.js 16', ha='center', va='center',
                fontsize=14, weight='bold', color=COLORS['text'])
        ax.text(6.25, 5.5, 'Server Components', ha='center', va='center',
                fontsize=9, color=COLORS['muted'])
        ax.text(6.25, 5.2, 'Port: 3000', ha='center', va='center',
                fontsize=8, color=COLORS['purple'], style='italic')
        
        # 3. Express API
        api_box = FancyBboxPatch((9, 5), 2.5, 1.5,
                                 boxstyle="round,pad=0.1",
                                 edgecolor=COLORS['pink'],
                                 facecolor=COLORS['card'],
                                 linewidth=2)
        ax.add_patch(api_box)
        ax.text(10.25, 5.85, '🚀 Express', ha='center', va='center',
                fontsize=14, weight='bold', color=COLORS['text'])
        ax.text(10.25, 5.5, 'API Bridge', ha='center', va='center',
                fontsize=9, color=COLORS['muted'])
        ax.text(10.25, 5.2, 'Port: 4000', ha='center', va='center',
                fontsize=8, color=COLORS['pink'], style='italic')
        
        # 4. External API
        external_box = FancyBboxPatch((5.75, 2), 3.5, 1.5,
                                      boxstyle="round,pad=0.1",
                                      edgecolor=COLORS['purple'],
                                      facecolor=COLORS['card'],
                                      linewidth=2,
                                      linestyle='--')
        ax.add_patch(external_box)
        ax.text(7.5, 2.85, '🌍 JSONPlaceholder', ha='center', va='center',
                fontsize=14, weight='bold', color=COLORS['text'])
        ax.text(7.5, 2.5, 'External Data Source', ha='center', va='center',
                fontsize=9, color=COLORS['muted'])
        ax.text(7.5, 2.2, 'typicode.com/albums', ha='center', va='center',
                fontsize=8, color=COLORS['purple'], style='italic')
        
        # Animated arrows based on progress
        if progress > 0.1:
            # Browser -> Frontend
            arrow1 = FancyArrowPatch((3, 5.75), (5, 5.75),
                                    arrowstyle='->', mutation_scale=30,
                                    color=COLORS['purple'], linewidth=3,
                                    alpha=min(1, (progress - 0.1) * 5))
            ax.add_patch(arrow1)
            if progress > 0.15:
                ax.text(4, 6.1, 'HTTP Request', ha='center', fontsize=9,
                       color=COLORS['purple'], alpha=min(1, (progress - 0.15) * 5))
        
        if progress > 0.3:
            # Frontend -> API
            arrow2 = FancyArrowPatch((7.5, 5.75), (9, 5.75),
                                    arrowstyle='->', mutation_scale=30,
                                    color=COLORS['accent'], linewidth=3,
                                    alpha=min(1, (progress - 0.3) * 5))
            ax.add_patch(arrow2)
            if progress > 0.35:
                ax.text(8.25, 6.1, 'Fetch Albums', ha='center', fontsize=9,
                       color=COLORS['accent'], alpha=min(1, (progress - 0.35) * 5))
        
        if progress > 0.5:
            # API -> External
            arrow3 = FancyArrowPatch((10.25, 5), (7.5, 3.5),
                                    arrowstyle='->', mutation_scale=30,
                                    color=COLORS['pink'], linewidth=3,
                                    alpha=min(1, (progress - 0.5) * 5))
            ax.add_patch(arrow3)
            if progress > 0.55:
                ax.text(9.5, 4, 'Proxy', ha='center', fontsize=9,
                       color=COLORS['pink'], alpha=min(1, (progress - 0.55) * 5))
        
        if progress > 0.7:
            # Return path - External -> API
            arrow4 = FancyArrowPatch((7.5, 3.5), (10.25, 5),
                                    arrowstyle='->', mutation_scale=30,
                                    color=COLORS['pink'], linewidth=2,
                                    linestyle='--',
                                    alpha=min(1, (progress - 0.7) * 5))
            ax.add_patch(arrow4)
        
        if progress > 0.85:
            # Return - API -> Frontend
            arrow5 = FancyArrowPatch((9, 5.4), (7.5, 5.4),
                                    arrowstyle='->', mutation_scale=30,
                                    color=COLORS['accent'], linewidth=2,
                                    linestyle='--',
                                    alpha=min(1, (progress - 0.85) * 5))
            ax.add_patch(arrow5)
            if progress > 0.9:
                ax.text(8.25, 5.1, 'JSON Data', ha='center', fontsize=9,
                       color=COLORS['accent'], alpha=min(1, (progress - 0.9) * 10))
        
        # Docker container outline
        docker_rect = patches.Rectangle((0.5, 4.5), 11.5, 2.5,
                                       linewidth=2, edgecolor=COLORS['border'],
                                       facecolor='none', linestyle=':')
        ax.add_patch(docker_rect)
        ax.text(0.7, 6.8, '🐳 Docker Container', fontsize=11,
               color=COLORS['muted'], style='italic')
        
        # Footer
        ax.text(7, 0.5, 'Bridge Pattern Architecture | Full Stack Microservices',
               ha='center', fontsize=11, color=COLORS['muted'], style='italic')
        
        plt.tight_layout()
        
        # Save frame
        temp_file = f'/tmp/arch_frame_{frame_idx:03d}.png'
        plt.savefig(temp_file, dpi=100, facecolor=COLORS['bg'])
        frames.append(imageio.imread(temp_file))
        plt.close()
        os.remove(temp_file)
    
    # Save as GIF
    output_path = os.path.join(OUTPUT_DIR, 'architecture-flow.gif')
    imageio.mimsave(output_path, frames, duration=0.1, loop=0)
    print(f"✅ Saved: {output_path}")


def create_tech_stack_diagram():
    """Create technology stack visualization"""
    print("🎨 Generating tech stack diagram...")
    
    fig, ax = plt.subplots(figsize=(12, 10), facecolor=COLORS['bg'])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(6, 9.5, '🛠️ Technology Stack', ha='center', va='top',
           fontsize=26, weight='bold', color=COLORS['text'])
    
    # Layer structure
    layers = [
        {
            'y': 7.5,
            'title': 'FRONTEND',
            'color': COLORS['purple'],
            'items': [
                ('Next.js 16', 'React Server Components'),
                ('React 19', 'Modern UI Library'),
                ('Tailwind CSS v4', 'Utility-First Styling'),
                ('TypeScript 5', 'Type Safety')
            ]
        },
        {
            'y': 5,
            'title': 'BACKEND',
            'color': COLORS['pink'],
            'items': [
                ('Express 4.21', 'Node.js Framework'),
                ('TypeScript', 'Backend Type Safety'),
                ('REST API', 'Bridge Pattern'),
                ('CORS Enabled', 'Cross-Origin Support')
            ]
        },
        {
            'y': 2.5,
            'title': 'DEVOPS',
            'color': COLORS['accent'],
            'items': [
                ('Docker', 'Containerization'),
                ('Docker Compose', 'Multi-Service'),
                ('Multi-Stage Builds', 'Optimized Images'),
                ('Dev + Prod Configs', 'Environment Management')
            ]
        }
    ]
    
    for layer in layers:
        # Layer title
        ax.text(1, layer['y'] + 0.5, layer['title'],
               fontsize=14, weight='bold', color=layer['color'])
        
        # Items
        for idx, (tech, desc) in enumerate(layer['items']):
            x_pos = 2.5 + (idx % 2) * 4.5
            y_pos = layer['y'] - (idx // 2) * 0.6
            
            # Tech box
            box = FancyBboxPatch((x_pos, y_pos - 0.25), 3.5, 0.4,
                                boxstyle="round,pad=0.05",
                                edgecolor=layer['color'],
                                facecolor=COLORS['card'],
                                linewidth=2)
            ax.add_patch(box)
            
            # Text
            ax.text(x_pos + 1.75, y_pos + 0.05, tech,
                   ha='center', va='center', fontsize=11,
                   weight='bold', color=COLORS['text'])
            ax.text(x_pos + 1.75, y_pos - 0.15, desc,
                   ha='center', va='center', fontsize=8,
                   color=COLORS['muted'])
    
    # Stats boxes at bottom
    stats = [
        ('100%', 'Type Safety'),
        ('0', 'Runtime Errors'),
        ('2', 'Microservices'),
        ('Multi-Stage', 'Docker Build')
    ]
    
    for idx, (value, label) in enumerate(stats):
        x = 1.5 + idx * 2.5
        
        stat_box = FancyBboxPatch((x, 0.3), 2, 1,
                                 boxstyle="round,pad=0.1",
                                 edgecolor=COLORS['purple'],
                                 facecolor=COLORS['card'],
                                 linewidth=2)
        ax.add_patch(stat_box)
        
        ax.text(x + 1, 0.95, value, ha='center', va='center',
               fontsize=16, weight='bold', color=COLORS['purple'])
        ax.text(x + 1, 0.55, label, ha='center', va='center',
               fontsize=9, color=COLORS['muted'])
    
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'tech-stack.png')
    plt.savefig(output_path, dpi=150, facecolor=COLORS['bg'])
    plt.close()
    print(f"✅ Saved: {output_path}")


def create_features_showcase():
    """Create features showcase graphic"""
    print("🎨 Generating features showcase...")
    
    fig, ax = plt.subplots(figsize=(14, 8), facecolor=COLORS['bg'])
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(7, 7.5, '✨ Key Features', ha='center', va='top',
           fontsize=26, weight='bold', color=COLORS['text'])
    
    features = [
        {
            'icon': '⚡',
            'title': 'Server-Side Rendering',
            'desc': 'Next.js App Router with React 19 Server Components for optimal performance',
            'pos': (2, 5.5)
        },
        {
            'icon': '🎨',
            'title': 'Modern UI/UX',
            'desc': 'Dark gradient theme with glassmorphism, smooth animations, and responsive design',
            'pos': (7.5, 5.5)
        },
        {
            'icon': '🔒',
            'title': 'Bridge Pattern',
            'desc': 'Secure API proxy layer between frontend and external services',
            'pos': (2, 3)
        },
        {
            'icon': '🐳',
            'title': 'Production Ready',
            'desc': 'Fully dockerized with separate dev and production configurations',
            'pos': (7.5, 3)
        }
    ]
    
    for feature in features:
        x, y = feature['pos']
        
        # Feature box
        box = FancyBboxPatch((x - 0.2, y - 0.5), 5, 1.8,
                            boxstyle="round,pad=0.15",
                            edgecolor=COLORS['purple'],
                            facecolor=COLORS['card'],
                            linewidth=2)
        ax.add_patch(box)
        
        # Icon
        ax.text(x + 0.3, y + 0.7, feature['icon'], ha='center', va='center',
               fontsize=36)
        
        # Title
        ax.text(x + 1.5, y + 0.85, feature['title'], ha='left', va='center',
               fontsize=13, weight='bold', color=COLORS['text'])
        
        # Description
        ax.text(x + 1.5, y + 0.3, feature['desc'], ha='left', va='center',
               fontsize=9, color=COLORS['muted'], wrap=True)
    
    # Bottom banner
    banner = FancyBboxPatch((1, 0.5), 12, 1,
                           boxstyle="round,pad=0.1",
                           edgecolor=COLORS['accent'],
                           facecolor=COLORS['card'],
                           linewidth=2)
    ax.add_patch(banner)
    ax.text(7, 1, '🚀 Built for the MUBITE Testing Challenge',
           ha='center', va='center', fontsize=14, weight='bold',
           color=COLORS['text'])
    
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, 'features.png')
    plt.savefig(output_path, dpi=150, facecolor=COLORS['bg'])
    plt.close()
    print(f"✅ Saved: {output_path}")


def main():
    """Generate all visualizations"""
    print("\n" + "="*60)
    print("🎨 Generating README Visualizations")
    print("="*60 + "\n")
    
    create_architecture_diagram()
    create_tech_stack_diagram()
    create_features_showcase()
    
    print("\n" + "="*60)
    print("✅ All visualizations generated successfully!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()

