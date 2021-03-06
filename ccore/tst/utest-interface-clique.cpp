/*!

@authors Andrei Novikov (pyclustering@yandex.ru)
@date 2014-2020
@copyright BSD-3-Clause

*/

#include <gtest/gtest.h>

#include <pyclustering/interface/clique_interface.h>
#include <pyclustering/interface/pyclustering_package.hpp>

#include "utenv_utils.hpp"

#include <memory>


using namespace pyclustering;


TEST(utest_interface_clique, clique_algorithm) {
    std::shared_ptr<pyclustering_package> sample = pack(dataset({ { 1.0, 1.0 }, { 1.1, 1.0 }, { 1.2, 1.4 }, { 10.0, 10.3 }, { 10.1, 10.2 }, { 10.2, 10.4 } }));

    pyclustering_package * result = clique_algorithm(sample.get(), 2, 0);
    ASSERT_EQ((std::size_t) CLIQUE_PACKAGE_SIZE, result->size);

    delete result;
}