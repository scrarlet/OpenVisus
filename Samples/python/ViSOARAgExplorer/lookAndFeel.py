import sys, os

#Color Scheme:  https://www.colorhexa.com/045951
visoarGreen = '#045951'
visoarRed = '#59040c'
visoarBlue = '#043759'
visoarLightGreen = '#067f73'
visoarDarkGreen = '#02332f'
visoarGreenWebSafe = '#006666'

LOOK_AND_FEEL = """
		font-family: Roboto;font-style: normal;font-size: 20pt; 
		background-color: #ffffff;
		color: #7A7A7A;
		QTabBar::tab:selected {
		background: #045951;
		}
		QMainWindow {
			#background-color: #7A7A7A;
			#color: #ffffff;
			background-color: #ffffff;
			color: #7A7A7A;
			
			}
			QLabel {
			background-color: #7A7A7A;
			color: #ffffff;
			}
		QToolTip {
			border: 1px solid #76797C;
			background-color: rgb(90, 102, 117);
			color: white;
			padding: 5px;
			opacity: 200;
		}
		QLabel {
			font: 20pt Roboto
		}
		QPushButton {
			border-radius: 7;
			border-style: outset; 
			border-width: 0px;
			color: #ffffff;
			background-color: #045951;
			padding: 10px;
		}
		QPushButton:pressed { 
			background-color:  #e6e6e6;

		}
		QLineEdit { background-color: #e6e6e6; border-color: #045951 }

		"""

TAB_LOOK = """
			/* Style the tab using the tab sub-control. Note that
		it reads QTabBar _not_ QTabWidget */
		QTabBar::tab {
			background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
			stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
			stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
			border: 2px solid #C4C4C3;
			border-bottom-color: #C2C7CB; /* same as the pane color */
			border-top-left-radius: 4px;
			border-top-right-radius: 4px;
			min-width: 200px;
			padding: 2px;
		}

		QTabBar::tab:selected {
			background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
			stop: 0 #045951, stop: 0.4 #045951,
			stop: 0.5 #034640, stop: 1.0 #045951);
			color: #ffffff;
		}
		QTabBar::tab:hover  {
			background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
			stop: 0 #07a294, stop: 0.4 #07a294,
			stop: 0.5 #045951, stop: 1.0 #07a294);
			color: #ffffff;
		}

		QTabBar::tab:selected {
			border-color: #9B9B9B;
			border-bottom-color: #C2C7CB; /* same as pane color */
		}

		QTabBar::tab:!selected {
			margin-top: 2px; /* make non-selected tabs look smaller */
		}"""


GREEN_PUSH_BUTTON = """QPushButton {
			max-width:300px;
			border-radius: 7;
			border-style: outset; 
			border-width: 0px;
			color: #ffffff;
			background-color: #045951;
			padding-left: 40px;
			padding-right: 40px;
			padding-top: 10px;
			padding-bottom: 10px;
		}
		QPushButton:pressed { 
			background-color:  #e6e6e6;

		}"""