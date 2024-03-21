#--------------------------------------------------------------------------
# Software:     InVesalius - Software de Reconstrucao 3D de Imagens Medicas
# Copyright:    (C) 2001  Centro de Pesquisas Renato Archer
# Homepage:     http://www.softwarepublico.gov.br
# Contact:      invesalius@cti.gov.br
# License:      GNU - GPL 2 (LICENSE.txt/LICENCA.txt)
#--------------------------------------------------------------------------
#    Este programa e software livre; voce pode redistribui-lo e/ou
#    modifica-lo sob os termos da Licenca Publica Geral GNU, conforme
#    publicada pela Free Software Foundation; de acordo com a versao 2
#    da Licenca.
#
#    Este programa eh distribuido na expectativa de ser util, mas SEM
#    QUALQUER GARANTIA; sem mesmo a garantia implicita de
#    COMERCIALIZACAO ou de ADEQUACAO A QUALQUER PROPOSITO EM
#    PARTICULAR. Consulte a Licenca Publica Geral GNU para obter mais
#    detalhes.
#--------------------------------------------------------------------------

from invesalius.navigation.image import Image
from invesalius.navigation.tracker import Tracker
from invesalius.navigation.iterativeclosestpoint import IterativeClosestPoint
from invesalius.net.neuronavigation_api import NeuronavigationApi
from invesalius.navigation.navigation import Navigation
from invesalius.net.pedal_connection import PedalConnector
from invesalius.navigation.robot import Robot


class NavigationControl:
    def __init__(self):
        self.tracker = Tracker()
        self.image = Image()
        self.icp = IterativeClosestPoint()
        self.neuronavigation_api = NeuronavigationApi()
        self.pedal_connector = PedalConnector(self.neuronavigation_api, self)
        self.navigation = Navigation(
            pedal_connector=self.pedal_connector,
            neuronavigation_api=self.neuronavigation_api,
        )
        self.robot = Robot(
            tracker=self.tracker,
            navigation=self.navigation,
            icp=self.icp,
        )
