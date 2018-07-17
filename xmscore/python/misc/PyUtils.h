#pragma once
//------------------------------------------------------------------------------
/// \file PyUtils.h
/// \brief Contains helper functions as well as several utility functions for pybind
/// \copyright (C) Copyright Aquaveo 2018. Distributed under the xmsng
///  Software License, Version 1.0. (See accompanying file
///  LICENSE_1_0.txt or copy at http://www.aquaveo.com/xmsng/LICENSE_1_0.txt)
//------------------------------------------------------------------------------

//----- Included files ---------------------------------------------------------

// 3. Standard library headers

// 4. External library headers
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <boost/shared_ptr.hpp>

// 5. Shared code headers
#include <xmscore/misc/DynBitset.h>
#include <xmscore/points/ptsfwd.h>
#include <xmscore/stl/vector.h>

//----- Forward declarations ---------------------------------------------------

//----- Namespace declaration --------------------------------------------------
namespace py = pybind11;

/// XMS Namespace
namespace xms
{

// Pt3d
Pt3d Pt3dFromPyIter(const py::tuple& pt);
py::tuple PyIterFromPt3d(const Pt3d& pt);

// VecPt3d
boost::shared_ptr<VecPt3d> VecPt3dFromPyIter(const py::iterable& pts);
py::iterable PyIterFromVecPt3d(const VecPt3d& pts);

// VecPt3d2d
boost::shared_ptr<VecPt3d2d> VecPt3d2dFromPyIter(const py::iterable& pts);
py::iterable PyIterFromVecPt3d2d(const VecPt3d2d& pts);

// VecInt2d
boost::shared_ptr<VecInt2d> VecInt2dFromPyIter(const py::iterable& int2d);
py::iterable PyIterFromVecInt2d(const VecInt2d& int2d);

// VecInt
boost::shared_ptr<VecInt> VecIntFromPyIter(const py::iterable& ints);
py::iterable PyIterFromVecInt(const VecInt& ints, bool numpy=false);

// VecDbl
boost::shared_ptr<VecDbl> VecDblFromPyIter(const py::iterable& dbls);
py::iterable PyIterFromVecDbl(const VecDbl& dbls, bool numpy=false);

// VecFlt
boost::shared_ptr<VecFlt> VecFltFromPyIter(const py::iterable& flts);
py::iterable PyIterFromVecFlt(const VecFlt& flts, bool numpy=false);

// DynamicBitset
DynBitset DynamicBitsetFromPyIter(const py::iterable& bitset);
py::iterable PyIterFromDynamicBitset(const DynBitset& bitset);
    
}