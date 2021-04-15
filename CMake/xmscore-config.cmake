# Import the XMS::Core target
find_package(Boost QUIET REQUIRED log_setup log system filesystem serialization timer)
include(${CMAKE_CURRENT_LIST_DIR}/xmscore-targets.cmake)

# Get the root installation dir
get_filename_component(_IMPORT_PREFIX "${CMAKE_CURRENT_LIST_FILE}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
if(_IMPORT_PREFIX STREQUAL "/")
  set(_IMPORT_PREFIX "")
endif()

include(GNUInstallDirs)

# Set the FindXMSCore variables
set(XMSCore_FOUND TRUE)
set(XMSCore_PREFIX ${CMAKE_CURRENT_LIST_DIR})
set(XMSCore_LIBRARY_DIRS "${_IMPORT_PREFIX}/${CMAKE_INSTALL_LIBDIR}")
set(XMSCore_INCLUDE_DIRS "${_IMPORT_PREFIX}/${CMAKE_INSTALL_INCLUDEDIR}")
set(XMSCore_LIBRARIES XMS::Core)
set(XMSCore_VERSION 5.0.2)
