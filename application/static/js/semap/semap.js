import { setores } from "./modules/setores.js";
import initWarning from "./modules/appWarning.js";
import initSearch from "./modules/formSearch.js";
import initIdSector from "./modules/idSector.js";
import initMapPoligonos from "./modules/mapPoligonos.js";

initSearch(setores);
initIdSector(2);
initWarning();
initMapPoligonos();
