import unittest
import homework40
import homework41

tournamentST = unittest.TestSuite()
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(homework40.RunnerTest))
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(homework41.TournamentTest))

tournamentST_runner = unittest.TextTestRunner(verbosity=2)
tournamentST_runner.run(tournamentST)

