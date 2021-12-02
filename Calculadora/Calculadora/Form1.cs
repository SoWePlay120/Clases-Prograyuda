using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculadora
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
      
        }

        private void btnresultado_Click(object sender, EventArgs e)
        {
            string num1;
            string num2;
            num2 = numero2.Text; 
            num1 = numero1.Text;
            string rest;
            rest = num1 + num2;
            rest = lbmuestraderesultado.Text;
        }
    }
}
