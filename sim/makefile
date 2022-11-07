rdl_group=test
rdl_file=basic

mirror=-i https://pypi.tuna.tsinghua.edu.cn/simple

init:
	git submodle update --init
	python3 -m pip install --upgrade pip ${mirror}
	cd ../tool_html;\
	python3 -m pip install -e . ${mirror}
	cd ../tool_uvm;\
	python3 -m pip install -e . ${mirror}

#html
run:
	cp ../rdl/${rdl_group}/${rdl_file}.rdl ../tool_html/example/work.rdl
	cd ../tool_html/example; \
	python3 generate_docs.py work.rdl

view:
	cd ../tool_html/docs; \
	launcher-windows-edge.bat

gen:
	cp ../rdl/${rdl_group}/${rdl_file}.rdl ../tool_uvm/test/testcases/work.rdl
	cd ../tool_uvm/test; \
	rm testcases/*.sv; \
	python3 generate_testcase_data.py gen testcases/work.rdl;
	cp ../tool_uvm/test/testcases/gen_uvm_fac_noreuse.sv .
