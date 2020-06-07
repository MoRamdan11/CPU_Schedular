elif self.comboBox.currentText() == self.comboBox.itemText(4):  # Priority Non_preemptive
            try:
                for i in range(n):
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:  # FCFS
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                            temp_priority = p_priority[i]
                            p_priority[i] = p_priority[j]
                            p_priority[j] = temp_priority
                        if (p_arrival[i] == p_arrival[j]):
                            if (p_priority[j] < p_priority[i]):
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                        if p_arrival[j] < text:
                            if p_priority[j] < p_priority[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 15)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 15)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                    text = 0
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    while index >= 0:
                        text = text + p_burst[index]
                        index = index - 1
                    text = text + idle_total
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(15)
                    t.color("Black")
                    style = ('Courier', 12)
                    text = round(text, 2)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(0)
                    t.forward(15)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                    t.color("Black")
                avg = w_time / n
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
