#!/bin/sh
# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

set -e
base=$(dirname "$0")

if [ "$PYTHON" ]; then
	if [ ! -f "$PYTHON" ]; then
		PYTHON=""
	fi
fi

if [ ! "$PYTHON" ]; then
	if [ `which python2.7` ]; then
		PYTHON=`which python2.7`
	else
		PYTHON=python
	fi
fi

exec $PYTHON "${base}/gyp_main.py" "$@"
