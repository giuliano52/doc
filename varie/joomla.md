JOOMLA
===
#Installazione
conviene dare i permessi alla cartella all'utente con cui gira il web server 
es supponendo che joomla sia installata in /home/test/public_html/j02 e apache giri con utente: http

    sudo chgrp -R http *
    chmod g+w -R j02/
    
oppure

    setfacl -R -m "u:www-data:rwx" directory_joomla

#Componenti Importanti

##Akeeba Backup
Per il restore:
- copiare il file kickstart.php e il backup nella directory web
- lanciare il kickstart (e scegliere l'opzione direct)
- premere next (o prossimo) e seguire il wizard


#Temi


#Creazioni componenti 

##visualizzazione nel menu
per visualizzare il componente tra i menù disponibili creare il file default.xml all'interno delle view da mostrare es:
site/views/helloworld/tmpl/default.xml  
NB: per  COM_HELLOWORLD_HELLOWORLD_VIEW_DEFAULT_DESC utilizzare il file di language dentro admin
```xml
<?xml version="1.0" encoding="utf-8"?>
<metadata>
        <layout title="COM_HELLOWORLD_HELLOWORLD_VIEW_DEFAULT_TITLE">
                <message>
                        <![CDATA[COM_HELLOWORLD_HELLOWORLD_VIEW_DEFAULT_DESC]]>
                </message>
        </layout>
</metadata>
```


##Variabili utili
```php
JPATH_ADMINISTRATOR     ->  /home/test01/public_html/j01/administrator
JPATH_ROOT              ->  /home/test01/public_html/j01
JPATH_COMPONENT         ->  /home/test01/public_html/j01/components/com_pqz
JPATH_LIBRARIES         ->  /home/test01/public_html/j01/libraries
JURI::root()            ->  http://192.168.1.101/~test01/j01/
Juri::base()            ->  http://192.168.20.27/~test01/j01/ 
```
###Dati Utente
```php
$user = JFactory::getUser();
 
if (!$user->guest) {
  echo 'You are logged in as:<br />';
  echo 'User name: ' . $user->username . '<br />';
  echo 'Real name: ' . $user->name . '<br />';
  echo 'User ID  : ' . $user->id . '<br />';
}
```

### Accesso al db
```php
// Get a db connection.
$db = JFactory::getDbo();
 
// Create a new query object.
$query = $db->getQuery(true);
 
// Select all records from the user profile table where key begins with "custom.".
// Order it by the ordering field.
$query->select($db->quoteName(array('user_id', 'profile_key', 'profile_value', 'ordering')));
$query->from($db->quoteName('#__user_profiles'));
$query->where($db->quoteName('profile_key') . ' LIKE '. $db->quote('\'custom.%\''));
$query->order('ordering ASC');
 
// Reset the query using our newly populated query object.
$db->setQuery($query);
 
// Load the results as a list of stdClass objects (see later for more options on retrieving data).
$results = $db->loadObjectList();
```
comunque guardare: http://docs.joomla.org/Selecting_data_using_JDatabase

##HTML
JHtml::_('grid.checkall') -> mostra il chackbox 'seleziona tutti' (da capire come usarlo in tabella però)

per inserire i css del modulo, metterlo nella view (default.php)
```php
JHtml::stylesheet(Juri::base() . 'components/com_pqz/media/css/com_pqz.css');
```

##Parametri in input
```php
$jinput = JFactory::getApplication()->input;
$foo = $jinput->get('varname', 'default_value', 'filter');
```
per i filtri possibili vedere: http://docs.joomla.org/Retrieving_request_data_using_JInput


##Internazionalizzazione
JText::_('COM_PQZ_TEST') -> mostra il testo nella linga corrispondente relativo a COM_PQZ_TEST (es in language/en-GB/en-GB.com_pqz.ini) 
JText::sprintf('COM_PQZ_TEST',$stringa1,$stringa2) -> sustituisce i %s nella stringa COM_PQZ_TEST con i valori delle stringhe

#MCV
per passare da una view (ad esempio se aggianciata direttamente da un menù con il file default.xml) bisogna creare un modello con il nome: della view ed all'interno la classe nome_compnenteModelNomevista. 
es: 
file: view/edit_csv/view.html.php
```php
class pqzViewedit_csv extends JViewLegacy {
```
file models/edit_csv.php
```php
class pqzModeledit_csv extends JModelList {
```
##JViewLegacy
```php
$this->getNmae(); // print the name of the view
```
##Controller
la funzione di default si chiama 'default'
il model di default ha la lo stesso nome del componente, ma si può richiamare un model diverso (es helloworld_model.php) con 
la funzione:   $model = $this->getModel('helloworld_model');
poi si possono anche lanciare le funzioni direttamente, ma è meglio impostare anche il modello della view es:
```php
$model = $this->getModel('choose_quiz');
$view = $this->getView('choose_quiz', 'html');
$view->setModel( $model , true );
```
##Models
il modello chiamato (es choose_quiz.pgp) ha una funzione 
public function getItems() {

##View
per ottenere i dati dal modello (funzione Get Items). (il modello dovrebbe essere stato settato dal controller
```php
$out = $this->get('Items');
print_pre($out);
```
è possibile avere più template nella stessa view
ad esempio per chiamare tmpl/default_question.php 
si usa 
```php
echo $this->loadTemplate("question");
```

per passare le informazioni si può usare anche (da capire)

```
$this->items     = $this->get('Items')
$this->data     = $this->get('Data'); 
$this->form     = $this->get('Form');
$this->state    = $this->get('State');
$this->params   = $this->state->get('params');
```

