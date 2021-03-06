/*
################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Please refer to the README for information about making permanent changes.  #
################################################################################
*/

#include "QmlZdirPatch.h"


///
//  Create copy of a patch. If the patch is null, or memory was exhausted,
//  returns null.                                                         
zdir_patch_t *QmlZdirPatch::dup () {
    return zdir_patch_dup (self);
};

///
//  Return patch file directory path
const QString QmlZdirPatch::path () {
    return QString (zdir_patch_path (self));
};

///
//  Return patch file item
QmlZfile *QmlZdirPatch::file () {
    QmlZfile *retQ_ = new QmlZfile ();
    retQ_->self = zdir_patch_file (self);
    return retQ_;
};

///
//  Return operation
zdir_patch_op_t QmlZdirPatch::op () {
    return zdir_patch_op (self);
};

///
//  Return patch virtual file path
const QString QmlZdirPatch::vpath () {
    return QString (zdir_patch_vpath (self));
};

///
//  Calculate hash digest for file (create only)
void QmlZdirPatch::digestSet () {
    zdir_patch_digest_set (self);
};

///
//  Return hash digest for patch file
const QString QmlZdirPatch::digest () {
    return QString (zdir_patch_digest (self));
};


QObject* QmlZdirPatch::qmlAttachedProperties(QObject* object) {
    return new QmlZdirPatchAttached(object);
}


///
//  Self test of this class.
void QmlZdirPatchAttached::test (bool verbose) {
    zdir_patch_test (verbose);
};

///
//  Create new patch
QmlZdirPatch *QmlZdirPatchAttached::construct (const QString &path, QmlZfile *file, zdir_patch_op_t op, const QString &alias) {
    QmlZdirPatch *qmlSelf = new QmlZdirPatch ();
    qmlSelf->self = zdir_patch_new (path.toUtf8().data(), file->self, op, alias.toUtf8().data());
    return qmlSelf;
};

///
//  Destroy a patch
void QmlZdirPatchAttached::destruct (QmlZdirPatch *qmlSelf) {
    zdir_patch_destroy (&qmlSelf->self);
};

/*
################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Please refer to the README for information about making permanent changes.  #
################################################################################
*/
