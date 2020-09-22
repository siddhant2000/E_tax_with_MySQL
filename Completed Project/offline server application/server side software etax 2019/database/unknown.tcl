#############################################################################
# Generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#  Apr 25, 2019 04:05:33 PM +0530  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m43" -background {#ffff24} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1516x821+37+31
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1604 882
    wm minsize $top 124 20
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Britannic Bold} -size 48 -weight bold} \
        -foreground {#ff250d} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text eTAX 
    vTcl:DefineAlias "$top.lab43" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Britannic Bold} -size 48 -weight bold} \
        -foreground {#2212ff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text 2019 
    vTcl:DefineAlias "$top.lab45" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe Script} -size 12 -slant italic} \
        -foreground {#13c12a} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {working for you} 
    vTcl:DefineAlias "$top.lab47" "Label2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but48 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#120bd8} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell Extra Bold} -size 12 -weight bold} \
        -foreground {#fcffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Back 
    vTcl:DefineAlias "$top.but48" "backbutton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but49 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#120bd8} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell Extra Bold} -size 12 -weight bold} \
        -foreground {#fcffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Exit 
    vTcl:DefineAlias "$top.but49" "exit" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text etax-2019 
    vTcl:DefineAlias "$top.lab50" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab51 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text {v 1.0.2} 
    vTcl:DefineAlias "$top.lab51" "Label3_3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Working On Windows} 
    vTcl:DefineAlias "$top.lab52" "Label3_4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab53 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Connected to MySQL server 8.0} 
    vTcl:DefineAlias "$top.lab53" "Label3_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#36911a} \
        -font {-family {Rockwell Extra Bold} -size 40 -weight bold} \
        -foreground {#36911a} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {DATA MODIFICATION REQUEST } 
    vTcl:DefineAlias "$top.lab44" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab56 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Server  Status : Online} 
    vTcl:DefineAlias "$top.lab56" "Label5_3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab57 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Host : localhost} 
    vTcl:DefineAlias "$top.lab57" "Label5_4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 9} -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Port : 3306} 
    vTcl:DefineAlias "$top.lab58" "Label5_5" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr66 \
        -background {#d9d9d9} -height 535 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 1501 
    vTcl:DefineAlias "$top.scr66" "box2o1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr66.01 configure -background white \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    ttk::separator $top.tSe70
    vTcl:DefineAlias "$top.tSe70" "TSeparator2" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $top.tSe71
    vTcl:DefineAlias "$top.tSe71" "TSeparator3" vTcl:WidgetProc "Toplevel1" 1
    button $top.but79 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#2020d8} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 13 -weight bold} \
        -foreground {#ffffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -takefocus 0 -text {Deleted Data} 
    vTcl:DefineAlias "$top.but79" "deleted" vTcl:WidgetProc "Toplevel1" 1
    button $top.but80 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#2020d8} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 13 -weight bold} \
        -foreground {#ffffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -takefocus 0 -text {Clear all} 
    vTcl:DefineAlias "$top.but80" "viewbutton_9" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m43
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    button $top.but44 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#2020d8} -disabledforeground {#a3a3a3} \
        -font {-family {Rockwell} -size 13 -weight bold} \
        -foreground {#ffffff} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -takefocus 0 -text {Updated Data} 
    vTcl:DefineAlias "$top.but44" "viewbutton_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ffff24} -disabledforeground {#a3a3a3} \
        -font {-family {Britannic Bold} -size 48 -weight bold} \
        -foreground {#ff250d} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text ADMINISTRATOR 
    vTcl:DefineAlias "$top.lab46" "Label1_2" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab43 \
        -in $top -x 20 -y 20 -width 156 -relwidth 0 -height 81 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 180 -y 20 -width 156 -relwidth 0 -height 81 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 110 -y 90 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 70 -y 140 -width 97 -relwidth 0 -height 44 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 200 -y 140 -width 97 -height 44 -anchor nw \
        -bordermode ignore 
    place $top.lab50 \
        -in $top -x 20 -y 790 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 20 -y 810 -width 34 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.lab52 \
        -in $top -x 10 -y 850 -width 134 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 20 -y 830 -width 164 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 420 -y 30 -anchor nw -bordermode ignore 
    place $top.lab56 \
        -in $top -x 1380 -y 780 -width 172 -height 28 -anchor nw \
        -bordermode ignore 
    place $top.lab57 \
        -in $top -x 1390 -y 830 -width 172 -height 28 -anchor nw \
        -bordermode ignore 
    place $top.lab58 \
        -in $top -x 1390 -y 850 -width 172 -height 28 -anchor nw \
        -bordermode ignore 
    place $top.scr66 \
        -in $top -x 50 -y 220 -width 1501 -relwidth 0 -height 535 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.tSe70 \
        -in $top -x 20 -y 120 -width 310 -anchor nw -bordermode inside 
    place $top.tSe71 \
        -in $top -x 20 -y 200 -width 1500 -anchor nw -bordermode inside 
    place $top.but79 \
        -in $top -x 520 -y 770 -width 148 -height 33 -anchor nw \
        -bordermode ignore 
    place $top.but80 \
        -in $top -x 900 -y 770 -width 108 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but44 \
        -in $top -x 720 -y 770 -width 148 -height 33 -anchor nw \
        -bordermode ignore 
    place $top.lab46 \
        -in $top -x 650 -y 100 -width 516 -relwidth 0 -height 81 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

