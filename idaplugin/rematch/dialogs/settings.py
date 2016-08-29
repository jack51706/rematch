try:
  from PyQt5 import QtWidgets
except ImportError:
  from PySide import QtGui
  QtWidgets = QtGui

from . import base
from .. import config


class SettingsDialog(base.BaseDialog):
  def __init__(self, **kwargs):
    super(SettingsDialog, self).__init__(title="Settings", **kwargs)

    autoupdate = config['settings']['update']['autoupdate']
    autocheck = config['settings']['update']['autocheck']
    autologin = config['settings']['login']['autologin']
    autologout = config['settings']['login']['autologout']
    debug = config['debug']

    self.autocheck = QtWidgets.QCheckBox("Automatically check for updates on "
                                         "startup")
    self.autocheck.setChecked(autocheck)
    self.layout.addWidget(self.autocheck)

    self.autoupdate = QtWidgets.QCheckBox("Automatically update to new "
                                          "version on startup")
    self.autocheck.stateChanged.connect(self.autoupdate.setEnabled)
    self.autoupdate.setEnabled(self.autocheck.isChecked())
    self.autoupdate.setChecked(autoupdate)
    self.layout.addWidget(self.autoupdate)

    self.autologin = QtWidgets.QCheckBox("Automatically login using "
                                         "user/password on startup")
    self.autologin.setChecked(autologin)
    self.layout.addWidget(self.autologin)

    self.autologout = QtWidgets.QCheckBox("Automatically forget login "
                                          "token when IDA exits")
    self.autologout.setChecked(autologout)
    self.layout.addWidget(self.autologout)

    self.debug = QtWidgets.QCheckBox("Print debug logs to console output")
    self.debug.setChecked(debug)
    self.layout.addWidget(self.debug)

    self.bottom_layout(self.submit, ok_text="&Save")

  def data(self):
    autocheck = self.autocheck.isChecked()
    autoupdate = self.autoupdate.isChecked()
    autologin = self.autologin.isChecked()
    autologout = self.autologout.isChecked()
    debug = self.debug.isChecked()

    return autocheck, autoupdate, autologin, autologout, debug

  def submit(self):
    config['settings']['update']['autocheck'] = self.autocheck.isChecked()
    config['settings']['update']['autoupdate'] = self.autoupdate.isChecked()
    config['settings']['login']['autologin'] = self.autologin.isChecked()
    config['settings']['login']['autologout'] = self.autologout.isChecked()
    config['debug'] = self.debug.isChecked()
    config.save()
    self.accept()
