import sys
import threading
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QObject


# You will need to create the following modules/classes in separate files:
# MonitorWindow
# DetailWindow
# VLBIViewModel
# NetworkModuleBase, FrontEndModule, DownConverterModule, etc.
# SpecManager
# IniConfig
# Logger
# VLBIFrequency, ObservationMode, DeviceStatus, VLBIDevices, NetworkClientErrorCodes, etc.
# FrontEndData, DownConverterData, IFSelectorData, VideoConverterData, VLBIData


class VLBIApp(QApplication):
    """
    Main application class, equivalent to the C# App class.
    """

    def __init__(self, argv):
        super().__init__(argv)
        self.check_single_instance()

        # Mutex to prevent duplicate instances
        self._mutex = None
        self._mutex_name = "VLBIMonitor"

        # Initialize windows and view model
        self.monitor_window = MonitorWindow()
        self.detail_window = DetailWindow()
        self.view_model = VLBIViewModel()

        # Bind view model to windows (PyQt5 uses different data binding)
        self.monitor_window.set_view_model(self.view_model)
        self.detail_window.set_view_model(self.view_model)

        # Initialize network modules
        self.module_list = []
        self.front_end_module = FrontEndModule()
        self.sx_down_converter_module = DownConverterModule("SXDownConverter")
        self.k_down_converter_module = DownConverterModule("KDownConverter")
        self.q_down_converter_module = DownConverterModule("QDownConverter")
        self.if_selector_module = IFSelectorModule()
        self.video_converter_module1 = VideoConverterModule("VideoConverter1")
        self.video_converter_module2 = VideoConverterModule("VideoConverter2")

        # System timer
        self.system_check_timer = QTimer()
        self.system_check_timer.setInterval(1000)  # 1 second
        self.system_check_timer.timeout.connect(self.system_check_timer_elapsed)

        # Spec data dictionaries
        self.spec_hot = {}
        self.spec_cold = {}
        self.spec_sky = {}
        self.down_converter_spec = {}
        self.if_selector_spec = {}
        self.video_converter1_spec = {}
        self.video_converter2_spec = {}

        self.first_timer_countdown = 0
        self.load_spec_data()
        self.init_network_modules()

        self.aboutToQuit.connect(self.application_exit)
        self.start_modules()
        self.system_check_timer.start()

    def check_single_instance(self):
        """
        Prevents multiple instances of the application from running.
        Uses a system-wide mutex, a concept that can be replicated with
        file locking or other OS-specific mechanisms in Python.
        For simplicity, this example uses a basic file lock.
        """
        try:
            import fcntl
            self._lock_file = open("/tmp/vlbimonitor.lock", "w")
            fcntl.lockf(self._lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except (IOError, ImportError):
            QMessageBox.warning(None, "Error", "The program is already running.")
            sys.exit(1)

    def load_spec_data(self):
        # This function would contain logic to load data from external sources
        # (e.g., INI files or databases) and populate the spec dictionaries.
        # This is a placeholder for the actual implementation.
        pass
