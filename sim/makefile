rdl_group=usb
rdl_file=usb_otg

mirror=-i https://pypi.tuna.tsinghua.edu.cn/simple

init:
	git submodule update --init
	pip install --upgrade pip ${mirror}
	cd ../tool_html;\
	pip install -e . ${mirror}
	cd ../tool_uvm;\
	pip install -e . ${mirror}

#html
html:
	cp ../rdl/${rdl_group}/${rdl_file}.rdl ../tool_html/example/work.rdl
	cd ../tool_html/example; \
	python generate_docs.py work.rdl

view:
	cd ../tool_html/docs; \
	launcher-windows-edge.bat

uvm:
	cp ../rdl/${rdl_group}/${rdl_file}.rdl ../tool_uvm/test/testcases/work.rdl
	cd ../tool_uvm/test; \
	rm testcases/*.sv; \
	python generate_testcase_data.py gen testcases/work.rdl;
	cp ../tool_uvm/test/testcases/gen_uvm_fac_noreuse.sv .
