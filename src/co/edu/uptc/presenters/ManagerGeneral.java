package co.edu.uptc.presenters;

import co.edu.uptc.models.ModelGerman.ManagerModel;
import co.edu.uptc.models.Pedro.ManagerModel202128778;
import co.edu.uptc.views.dashBoard.DashBoard;

public class ManagerGeneral {
    private static ManagerGeneral instance;
    ContratBills.View view;
    ContratBills.Model modelGerman;
    ContratBills.Model modelPedro;
    ContratBills.Presenter presenter;

    private ManagerGeneral() {
    }

    private void createMVP(){
         view = new DashBoard();
         presenter = new Presenter();
         view.setPresenter(presenter);
         presenter.setView(view);
         createModels();
         configModelUserGerman();
         configModelUserPedro();
     }

     public static ManagerGeneral getInstance(){
         return instance==null?instance = new ManagerGeneral():instance;
     }


     private void createModels(){
         // TODO aqui se cream todos los modelos
         modelGerman = new ManagerModel();
         modelPedro = new ManagerModel202128778();
     }

     public void configModelUserGerman(){
         modelGerman.setPresenter(presenter);
         presenter.setModel(modelGerman);
         view.updatedPeople();
     }

    public void configModelUserPedro(){
        modelPedro.setPresenter(presenter);
        presenter.setModel(modelPedro);
        view.updatedPeople();
    }

    public void configModelOtherUser(){
        // TODO  aqui se configura para cado estudiante el modelo y este metodo se llama desde la vista
        //modelGerman.setPresenter(presenter);
        presenter.setModel(null);
        view.updatedPeople();
    }


    public void runProject(){
        createMVP();
        view.start();
    }

}
