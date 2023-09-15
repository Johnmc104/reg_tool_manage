rdl_group=usb
rdl_file=usb_otg

mirror=-i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn

init:
	git submodule update --init
	pip install --upgrade pip ${mirror}
	cd ../tool_html; pip install -e . ${mirror}
	cd ../tool_uvm;  pip install -e . ${mirror}
	cd ../tool_ipxact; pip install -e . ${mirror}
	cp ../tool/ipxact/* ../tool_ipxact/examples

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

ipxact:
	cp ../rdl/${rdl_group}/${rdl_file}.rdl ../tool_ipxact/examples
	cd ../tool_ipxact/examples; \
	python generate_ipxact.py ${rdl_file}.rdl
	mv ../tool_ipxact/examples/test.rdl .