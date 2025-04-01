import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import time

class DrinkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Oguru Sushi & Bar - Classic Cocktails")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        
        # Configuração do tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Fontes
        self.title_font = ("Helvetica", 24, "bold")
        self.subtitle_font = ("Helvetica", 16, "bold")
        self.normal_font = ("Helvetica", 12)
        
        # Cores
        self.bg_color = "#121212"
        self.frame_color = "#1E1E1E"
        self.accent_color = "#76FF03"  # Verde claro
        self.text_color = "#FFFFFF"
        self.drink_name_color = "#000000"  # Preto
        
        # Carregar logo
        self.load_logo()
        
        # Tela de abertura
        self.show_splash_screen()
        
        # Após a animação, configurar a interface principal
        self.root.after(2000, self.setup_main_interface)
    
    def load_logo(self):
        try:
            logo_path = "oguru.png"
            if os.path.exists(logo_path):
                self.logo_image = Image.open(logo_path)
                max_width = 200
                width_percent = (max_width / float(self.logo_image.size[0]))
                height_size = int((float(self.logo_image.size[1]) * float(width_percent)))
                self.logo_image = self.logo_image.resize((max_width, height_size), Image.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(self.logo_image)
            else:
                self.logo_photo = None
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")
            self.logo_photo = None
    
    def show_splash_screen(self):
        # Frame de abertura
        self.splash_frame = ctk.CTkFrame(self.root, fg_color=self.bg_color)
        self.splash_frame.pack(fill="both", expand=True)
        
        # Logo com transparência inicial
        if self.logo_photo:
            self.splash_logo = ctk.CTkLabel(self.splash_frame, image=self.logo_photo, text="")
            self.splash_logo.pack(pady=(200, 0))
            self.splash_logo.configure(text_color=self.bg_color)  # Inicia transparente
        else:
            self.splash_logo = ctk.CTkLabel(self.splash_frame, text="OGURU\nSUSHI & BAR", 
                                           font=self.title_font, text_color=self.accent_color)
            self.splash_logo.pack(pady=(200, 0))
        
        # Animação de fade-in
        self.fade_in()
    
    def fade_in(self, alpha=0):
        """Animação de aparecimento gradual do logo"""
        if alpha < 1:
            alpha += 0.05  # Incremento da transparência
            if self.logo_photo:
                # Para imagens, usamos uma abordagem diferente
                self.splash_logo.configure(text_color=self._get_fade_color(alpha))
            else:
                # Para texto, ajustamos a cor diretamente
                r, g, b = self._hex_to_rgb(self.accent_color)
                faded_color = self._rgb_to_hex(
                    int(r * alpha),
                    int(g * alpha),
                    int(b * alpha)
                )
                self.splash_logo.configure(text_color=faded_color)
            
            self.root.after(50, lambda: self.fade_in(alpha))
    
    def _hex_to_rgb(self, hex_color):
        """Converte cor hex para RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _rgb_to_hex(self, r, g, b):
        """Converte RGB para hex"""
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def _get_fade_color(self, alpha):
        """Calcula cor intermediária para fade-in"""
        bg_r, bg_g, bg_b = self._hex_to_rgb(self.bg_color)
        fg_r, fg_g, fg_b = self._hex_to_rgb(self.accent_color)
        
        r = int(bg_r + (fg_r - bg_r) * alpha)
        g = int(bg_g + (fg_g - bg_g) * alpha)
        b = int(bg_b + (fg_b - bg_b) * alpha)
        
        return self._rgb_to_hex(r, g, b)
    
    def setup_main_interface(self):
        # Remover tela de abertura
        self.splash_frame.destroy()
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(self.root, fg_color=self.bg_color)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Barra lateral esquerda
        self.sidebar = ctk.CTkFrame(self.main_frame, width=250, fg_color=self.frame_color, 
                                   corner_radius=20)
        self.sidebar.pack(side="left", fill="y", padx=(0, 10), pady=10)
        
        # Área do logo
        self.logo_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.logo_frame.pack(pady=(20, 30))
        
        if self.logo_photo:
            self.logo_label = ctk.CTkLabel(self.logo_frame, image=self.logo_photo, text="")
            self.logo_label.pack()
        else:
            self.logo_label = ctk.CTkLabel(self.logo_frame, text="OGURU\nSUSHI & BAR", 
                                         font=self.title_font, text_color=self.accent_color)
            self.logo_label.pack()
        
        # Lista de drinks
        self.drink_list_frame = ctk.CTkScrollableFrame(self.sidebar, fg_color=self.frame_color)
        self.drink_list_frame.pack(fill="both", expand=True, padx=10, pady=(0, 20))
        
        # Área de conteúdo principal
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color=self.frame_color, 
                                        corner_radius=20)
        self.content_frame.pack(side="right", fill="both", expand=True, pady=10)
        
        # Título do conteúdo
        self.content_title = ctk.CTkLabel(self.content_frame, text="Selecione um drink", 
                                        font=self.title_font, text_color=self.accent_color)
        self.content_title.pack(pady=20)
        
        # Container para os detalhes do drink
        self.drink_details = ctk.CTkScrollableFrame(self.content_frame, fg_color=self.frame_color)
        self.drink_details.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Rodapé
        self.footer = ctk.CTkLabel(self.content_frame, text="© 2025 Oguru Sushi & Bar - Premium Cocktails", 
                                  font=("Helvetica", 10), text_color="#AAAAAA")
        self.footer.pack(pady=10)
        
        # Carregar dados dos drinks
        self.drinks = self.load_classic_drinks_data()
        self.show_drink_list()
    
    def load_classic_drinks_data(self):
        drinks = [
              {
                "name": "Negroni",
                "ingredients": "30ml de gin\n30ml de Campari\n30ml de vermute doce",
                "instructions": "Misture todos os ingredientes em um copo mixing com gelo.\nMexa bem por 30 segundos.\nCoe em um copo old-fashioned com gelo.\nDecore com casca de laranja.",
                "glass": "Copo old-fashioned",
                "garnish": "Casca de laranja",
                "flavor": "Amargo e herbal",
                "appearance": "Vermelho profundo",
                "ml": 90
            },
            {
                "name": "Old Fashioned",
                "ingredients": "60ml de bourbon\n1 cubo de açúcar\n2 dash de bitters\nÁgua mineral",
                "instructions": "Coloque o cubo de açúcar no copo.\nAdicione os bitters e um pouco de água.\nMacere até dissolver o açúcar.\nAdicione gelo e o bourbon.\nMexa suavemente.\nDecore com casca de laranja e cereja.",
                "glass": "Copo old-fashioned",
                "garnish": "Casca de laranja e cereja",
                "flavor": "Doce e aromático",
                "appearance": "Âmbar",
                "ml": 90
            },
            {
                "name": "Martini",
                "ingredients": "60ml de gin\n10ml de vermute seco",
                "instructions": "Misture os ingredientes em uma coqueteleira com gelo.\nMexa por 30 segundos.\nCoe em uma taça de martini resfriada.\nDecore com azeitonas ou casca de limão.",
                "glass": "Taça de martini",
                "garnish": "Azeitona ou casca de limão",
                "flavor": "Seco e herbal",
                "appearance": "Cristalino",
                "ml": 70
            },
            {
                "name": "Mojito",
                "ingredients": "50ml de rum branco\n6 folhas de hortelã\n25ml de suco de limão\n2 colheres de açúcar\nÁgua com gás",
                "instructions": "Macere as folhas de hortelã com o açúcar e suco de limão.\nAdicione o rum e gelo picado.\nComplete com água com gás.\nMexa suavemente.\nDecore com hortelã e rodela de limão.",
                "glass": "Copo highball",
                "garnish": "Hortelã e limão",
                "flavor": "Refrescante e mentolado",
                "appearance": "Translúcido com folhas",
                "ml": 200
            },
            {
                "name": "Margarita",
                "ingredients": "50ml de tequila\n25ml de Cointreau\n25ml de suco de limão\nSal",
                "instructions": "Umedeça a borda da taça com limão e mergulhe em sal.\nMisture todos os ingredientes na coqueteleira com gelo.\nAgite vigorosamente.\nCoe na taça com ou sem gelo.\nDecore com rodela de limão.",
                "glass": "Taça de margarita",
                "garnish": "Rodela de limão",
                "flavor": "Doce e azedo",
                "appearance": "Amarelo pálido",
                "ml": 100
            },
            {
                "name": "Piña Colada",
                "ingredients": "60ml de rum branco\n90ml de suco de abacaxi\n30ml de leite de coco",
                "instructions": "Bata todos os ingredientes no liquidificador com gelo.\nSirva em um copo hurricane.\nDecore com fatia de abacaxi e cereja.",
                "glass": "Copo hurricane",
                "garnish": "Abacaxi e cereja",
                "flavor": "Tropical e cremoso",
                "appearance": "Branco cremoso",
                "ml": 180
            },
            {
                "name": "Daiquiri",
                "ingredients": "60ml de rum branco\n25ml de suco de limão\n15ml de xarope simples",
                "instructions": "Misture todos os ingredientes na coqueteleira com gelo.\nAgite vigorosamente.\nCoe em uma taça de cocktail.\nDecore com rodela de limão.",
                "glass": "Taça de cocktail",
                "garnish": "Rodela de limão",
                "flavor": "Doce e azedo",
                "appearance": "Cristalino",
                "ml": 100
            },
            {
                "name": "Whiskey Sour",
                "ingredients": "60ml de bourbon\n25ml de suco de limão\n15ml de xarope simples\n1 clara de ovo",
                "instructions": "Agite todos os ingredientes sem gelo para emulsificar.\nAdicione gelo e agite novamente.\nCoe em um copo old-fashioned com gelo.\nDecore com bitters e casca de limão.",
                "glass": "Copo old-fashioned",
                "garnish": "Casca de limão",
                "flavor": "Equilibrado",
                "appearance": "Espumoso",
                "ml": 100
            },
            {
                "name": "Manhattan",
                "ingredients": "60ml de whiskey\n30ml de vermute doce\n2 dash de bitters",
                "instructions": "Misture todos os ingredientes em um copo mixing com gelo.\nMexa por 30 segundos.\nCoe em uma taça de cocktail.\nDecore com cereja.",
                "glass": "Taça de cocktail",
                "garnish": "Cereja",
                "flavor": "Complexo e aromático",
                "appearance": "Âmbar avermelhado",
                "ml": 90
            },
            {
                "name": "Moscow Mule",
                "ingredients": "50ml de vodka\n15ml de suco de limão\n120ml de cerveja de gengibre",
                "instructions": "Adicione vodka e suco de limão em um copo mule com gelo.\nComplete com cerveja de gengibre.\nMexa suavemente.\nDecore com fatia de limão.",
                "glass": "Copo de cobre (mule cup)",
                "garnish": "Fatia de limão",
                "flavor": "Refrescante e picante",
                "appearance": "Translúcido",
                "ml": 185
            },
            {
                "name": "Aperol Spritz",
                "ingredients": "90ml de prosecco\n60ml de Aperol\n30ml de água com gás",
                "instructions": "Encha um copo wine com gelo.\nAdicione o prosecco primeiro.\nAcrescente o Aperol.\nComplete com água com gás.\nDecore com rodela de laranja.",
                "glass": "Copo wine",
                "garnish": "Rodela de laranja",
                "flavor": "Amargo e frutado",
                "appearance": "Laranja vibrante",
                "ml": 180
            },
            {
                "name": "Espresso Martini",
                "ingredients": "50ml de vodka\n30ml de licor de café\n30ml de café espresso\n15ml de xarope simples",
                "instructions": "Agite todos os ingredientes vigorosamente com gelo.\nCoe em uma taça de martini.\nDecore com grãos de café.",
                "glass": "Taça de martini",
                "garnish": "Grãos de café",
                "flavor": "Energético e doce",
                "appearance": "Marrom escuro com espuma",
                "ml": 125
            },
            {
                "name": "Gin Tonic",
                "ingredients": "50ml de gin\n150ml de água tônica",
                "instructions": "Encha um copo balloon com gelo.\nAdicione o gin.\nComplete com água tônica.\nMexa suavemente.\nDecore com fatia de limão ou ervas.",
                "glass": "Copo balloon",
                "garnish": "Limão ou ervas",
                "flavor": "Refrescante e herbal",
                "appearance": "Translúcido",
                "ml": 200
            },
            {
                "name": "Bloody Mary",
                "ingredients": "50ml de vodka\n120ml de suco de tomate\n15ml de suco de limão\n2 dash de molho inglês\n2 dash de tabasco\nSal e pimenta",
                "instructions": "Misture todos os ingredientes na coqueteleira com gelo.\nAgite suavemente.\nSirva em um copo highball com gelo.\nDecore com aipo e limão.",
                "glass": "Copo highball",
                "garnish": "Aipo e limão",
                "flavor": "Picante e salgado",
                "appearance": "Vermelho opaco",
                "ml": 185
            },
            {
                "name": "Caipirinha",
                "ingredients": "60ml de cachaça\n1 limão cortado\n2 colheres de açúcar",
                "instructions": "Macere o limão com o açúcar no copo.\nAdicione gelo picado.\nComplete com cachaça.\nMexa suavemente.",
                "glass": "Copo old-fashioned",
                "garnish": "Fatia de limão",
                "flavor": "Doce e cítrico",
                "appearance": "Translúcido com limão",
                "ml": 120
            },
            {
                "name": "Mai Tai",
                "ingredients": "45ml de rum escuro\n15ml de rum branco\n15ml de Cointreau\n15ml de xarope de orgeat\n25ml de suco de limão",
                "instructions": "Agite todos os ingredientes com gelo.\nSirva em um copo old-fashioned com gelo.\nDecore com folha de hortelã e fatia de abacaxi.",
                "glass": "Copo old-fashioned",
                "garnish": "Hortelã e abacaxi",
                "flavor": "Tropical e complexo",
                "appearance": "Âmbar dourado",
                "ml": 115
            },
            {
                "name": "French 75",
                "ingredients": "30ml de gin\n15ml de suco de limão\n7ml de xarope simples\n60ml de champanhe",
                "instructions": "Agite gin, suco de limão e xarope com gelo.\nCoe em uma taça de champanhe.\nComplete com champanhe.\nDecore com casca de limão.",
                "glass": "Taça de champanhe",
                "garnish": "Casca de limão",
                "flavor": "Efervescente e cítrico",
                "appearance": "Claro com bolhas",
                "ml": 112
            },
            {
                "name": "Paloma",
                "ingredients": "50ml de tequila\n100ml de refrigerante de toranja\n15ml de suco de limão\nSal",
                "instructions": "Umedeça a borda do copo com limão e mergulhe em sal.\nAdicione gelo, tequila e suco de limão.\nComplete com refrigerante de toranja.\nDecore com fatia de toranja.",
                "glass": "Copo highball",
                "garnish": "Fatia de toranja",
                "flavor": "Cítrico e refrescante",
                "appearance": "Rosa pálido",
                "ml": 165
            },
            {
                "name": "Pisco Sour",
                "ingredients": "60ml de pisco\n25ml de suco de limão\n15ml de xarope simples\n1 clara de ovo\n3 dash de bitters",
                "instructions": "Agite todos os ingredientes sem gelo para emulsificar.\nAdicione gelo e agite novamente.\nCoe em uma taça de cocktail.\nDecore com bitters no topo.",
                "glass": "Taça de cocktail",
                "garnish": "Bitters",
                "flavor": "Cremoso e cítrico",
                "appearance": "Espumoso",
                "ml": 100
            },
            {
                "name": "Sidecar",
                "ingredients": "50ml de conhaque\n20ml de Cointreau\n20ml de suco de limão",
                "instructions": "Agite todos os ingredientes com gelo.\nCoe em uma taça de cocktail com açúcar na borda.\nDecore com casca de limão.",
                "glass": "Taça de cocktail",
                "garnish": "Casca de limão",
                "flavor": "Doce e cítrico",
                "appearance": "Amarelo pálido",
                "ml": 90
            }
        ]
        return drinks
    
    def show_drink_list(self):
        # Limpar lista atual
        for widget in self.drink_list_frame.winfo_children():
            widget.destroy()
        
        # Adicionar botões para cada drink
        for drink in self.drinks:
            btn = ctk.CTkButton(
                self.drink_list_frame,
                text=drink["name"],
                command=lambda d=drink: self.show_drink_details(d),
                fg_color=self.accent_color,
                hover_color="#64DD17",
                corner_radius=10,
                font=self.normal_font,
                height=40,
                text_color=self.drink_name_color
            )
            btn.pack(fill="x", pady=5, padx=5)
    
    def show_drink_details(self, drink):
        # Limpar detalhes atuais
        for widget in self.drink_details.winfo_children():
            widget.destroy()
        
        # Atualizar título
        self.content_title.configure(text=drink["name"])
        
        # Criar elementos de detalhes
        details = [
            ("🍹 Copo", drink["glass"]),
            ("🧊 Volume", f"{drink['ml']}ml"),
            ("🌿 Ingredientes", drink["ingredients"]),
            ("👨‍🍳 Modo de Preparo", drink["instructions"]),
            ("🍒 Guarnição", drink["garnish"]),
            ("👅 Sabor", drink["flavor"]),
            ("👀 Aparência", drink["appearance"])
        ]
        
        for icon, text in details:
            frame = ctk.CTkFrame(self.drink_details, fg_color="transparent")
            frame.pack(fill="x", pady=5)
            
            label = ctk.CTkLabel(
                frame, 
                text=icon + " " + text.split("\n")[0],
                font=self.subtitle_font if "\n" not in text else self.normal_font,
                text_color=self.accent_color if "\n" not in text else self.text_color,
                anchor="w"
            )
            label.pack(fill="x")
            
            if "\n" in text:
                for line in text.split("\n")[1:]:
                    line_label = ctk.CTkLabel(
                        frame,
                        text=line,
                        font=self.normal_font,
                        text_color=self.text_color,
                        anchor="w"
                    )
                    line_label.pack(fill="x")

  
        return drinks
    
  

if __name__ == "__main__":
    root = ctk.CTk()
    app = DrinkApp(root)
    root.mainloop()