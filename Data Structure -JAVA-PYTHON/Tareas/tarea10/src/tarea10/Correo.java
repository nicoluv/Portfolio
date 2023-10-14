/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tarea10;

import java.util.Calendar;
import java.util.Date;

/**
 *
 * @author Nicole Urena
 */
public class Correo {
    
    private String remitente;
    private String destinatario;
    private Calendar fechaEnvio;

    public Correo(String remitente, String destinatario,Calendar fechaEnvio) {
        this.remitente = remitente;
        this.destinatario = destinatario;
        this.fechaEnvio = fechaEnvio;
    }

    public String getRemitente() {
        return remitente;
    }

    public void setRemitente(String remitente) {
        this.remitente = remitente;
    }

    public String getDestinatario() {
        return destinatario;
    }

    public void setDestinatario(String destinatario) {
        this.destinatario = destinatario;
    }

    public Calendar getFechaEnvio() {
        return fechaEnvio;
    }

    public void setFechaEnvio(Calendar fechaEnvio) {
        this.fechaEnvio = fechaEnvio;
    }
    
  public int compareTo(Correo o) {
    return getFechaEnvio().compareTo(o.getFechaEnvio());
  }
}