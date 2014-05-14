import unittest;

from cure               import tests as cure_unit_tests;
from dbscan             import tests as dbscan_unit_tests;
from gcolor.dsatur      import tests as gcolor_dsatur_unit_tests;
from gcolor.sync        import tests as gcolor_sync_unit_tests;
from hierarchical       import tests as hierarchical_unit_tests;
from hsyncnet           import tests as hsyncnet_unit_tests;
from kmeans             import tests as kmeans_unit_tests;
from nnet.legion        import tests as nnet_legion_unit_tests;
from nnet.som           import tests as nnet_som_unit_tests;
from nnet.sync          import tests as nnet_sync_unit_tests;
from rock               import tests as rock_unit_tests;
from support            import tests as support_unit_tests;
from syncnet            import tests as syncnet_unit_tests;
from syncsom            import tests as syncsom_unit_tests;


if __name__ == "__main__":
    suite = unittest.TestSuite();
    
    suite.addTests(unittest.TestLoader().loadTestsFromModule(cure_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(dbscan_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(gcolor_dsatur_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(gcolor_sync_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(hierarchical_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(hsyncnet_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(nnet_legion_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(nnet_som_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(nnet_sync_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(support_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(syncnet_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(kmeans_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(rock_unit_tests));
    suite.addTests(unittest.TestLoader().loadTestsFromModule(syncsom_unit_tests));
    
    unittest.TextTestRunner(verbosity = 2).run(suite);
    