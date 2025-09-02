'use strict';

// Данные (команды, сила команд, игроки и рейтинги)
const TEAMS = [
  'Арсенал','Астон Вилла','Блэкборн','Болтон','Челси',
  'Ковентри','Манчестер Юнайтед','Ньюкастл','Эвертон','Лидс',
  'Ливерпуль','Манчестер Сити','Мидлсброу','Ноттингем','Тотенхем',
  'Королевский парк','Шеффилд','Уэстхем','Саутгемптон','Уимблдон'
];

const TEAM_STRENGTH = [
  970,830,910,430,810,385,1100,1180,665,900,
  975,860,890,880,910,840,790,770,550,685
];

// Игроки (16 на команду). Порядок: [вратарь, защитники/полузащита/атака...]
const PLAYERS = [
  ['Симан','Диксон','Кеоун','Винтербурн','Диксон','Адамс','Мерсон','Хелдер','Лужный','Бергкамп','Кивомия','Бертрам','Боулд','Парлоур','Дженсен','Хартсон'],
  ['Соунсенд','Милошевич','Босинч','Спинк','Енюогу','Карр','Саутгейт','Стаунтон','Джонсон','Йорк','Тарелли','Скимека','Чарлз','Макграф','Кинг','Дрейпер'],
  ['Флауэрс','Галашер','Берг','Хендри','Силкокс','Бохинен','Кервуд','Кенна','Рипли','Саттон','Кирар','Мимс','Ле Сокс','Гудмунсон','Маккинли','Невелл'],
  ['Бранаган','Девисон','Бергссон','Колеман','Тейрклоу','Курсик','Селларс','Ли','Макгинли','Блейк','Паателайнен','Грин','Филипс','Стубс','Томпсон','Дефрейтас'],
  ['Харин','Синклер','Спенсер','Джонсен','Кларк','Гуллит','Тайз','Тарлонг','Тьюа','Джола','Петреску','Хичкок','Барли','Ли','Телан','Пикок'],
  ['Борроуз','Огризович','Басст','Ноу','Ричардсон','Джесс','Хелан','Страшан','Ндлову','Дублин','Салако','Морган','Гоулд','Борроуз','Пикеринг','Дерби'],
  ['Шмейхель','Брюс','Невилл','Бекхем','Мэй','Ирвин','Скоулс','Коул','Шерингем','Кин','Палистер','Макклейр','Ван Дер Гоу','Шарп','Батт','Гигс'],
  ['Гислоп','Хоуэй','Бартон','Джинола','Бетти','Китсон','Тердинанда','Асприлья','Пикок','Ли','Гиллеспи','Кларк','Бересфорд','Бердсли','Срникеке','Альберт'],
  ['Саутолл','Эмбрелл','Уотсон','Хоттигер','Канчелскис','Лимпар','Амокачи','Норт','Тергюсон','Райдаут','Хинклиффе','Киртон','Джексон','Ансворт','Паркинсон','Стюарт'],
  ['Лукич','Дориго','Ветеран','Келли','Макалистер','Рейдеби','Палмер','Уайт','Дин','Йебоан','Пролин','Бини','Ремберт','Спид','Толис','Торнингтон'],
  ['Джеймс','Бабб','Руддок','Скейлс','Джонс','Макатир','Барнс','Макманаман','Оуэн','Тауэлер','Колимор','Редкнапп','Стенгард','Бьорнеби','Харкнес','Томас'],
  ['Кинкладзе','Шумерби','Дибл','Керннаган','Курл','Тронтжек','Вонк','Рослер','Куин','Ломас','Симонс','Иммел','Брайтвелл','Бигри','Клоу','Тликрофт'],
  ['Адамс','Эмерсон','Барнби','Флеминг','Морис','Поллок','Бранко','Уайт','Хигнет','Джуниньо','Тьортофт','Толш','Кокс','Пирсон','Мур','Хендри'],
  ['Стоун','Пирс','Хааланд','Кроссли','Тоан','Кемпбел','Ли','Джемил','Рой','Силензи','Барт-Вилья','Купер','Райт','Литл','Филипс','Четтл'],
  ['Токер','Кемпбелл','Токс','Каддервуд','Мабют','Остин','Уилсон','Синтон','Розентал','Армстронг','Раш','Коуэлс','Дозелл','Курслейк','Торсведт','Андертон'],
  ['Соммер','Макдоналд','Бардсли','Синклер','Хателли','Холлоуэй','Бреветт','Дичио','Ятес','Импи','Куаши','Галлен','Робертс','Мелдикс','Паркер','Реди'],
  ['Вудс','Брискоу','Токер','Стефанович','Нолан','Деграйси','Толда','Брайт','Джонс','Херст','Хайд','Витингем','Флинкер','Прессман','Меридан','Ковачевич'],
  ['Коти','Хагс','Билич','Монкур','Брейкер','Микложко','Мартин','Дикс','Димитреску','Бишоп','Слейтер','Доуи','Дани','Сили','Потс','Рипер'],
  ['Луккич','Дориго','Ветеран','Келли','Макалистер','Рейдеби','Палмер','Уайт','Дин','Йебоан','Пролин','Бини','Ремберт','Спид','Толис','Торнингтон'],
  ['Саливан','Фирэ','Джонс','Кимбл','Ардли','Ленардуцци','Гейл','Кларк','Экоку','Госдэн','Харфорд','Каннингэм','Робсон','Блисетт','Барнетт','Рид']
];

// Рейтинги игроков (16 на команду)
const RATINGS = [
  [80,90,60,60,60,80,70,70,70,80,60,30,40,30,50,40],
  [60,50,60,40,70,60,60,70,60,70,70,30,30,40,30,30],
  [70,90,50,50,60,50,60,70,70,70,90,30,40,40,30,40],
  [30,20,30,10,20,70,30,50,50,50,30,5,20,5,5,5],
  [60,60,50,60,80,60,50,40,80,80,40,50,30,10,30,30],
  [20,40,20,20,20,50,30,70,50,10,30,5,5,5,5,5],
  [80,70,60,60,60,80,80,90,90,70,80,60,60,40,60,60],
  [70,90,70,80,70,80,90,90,80,80,70,60,70,70,60,50],
  [50,60,40,30,60,50,70,40,60,60,50,30,40,20,30,20],
  [40,50,30,40,60,70,50,60,70,70,60,40,50,60,40,30],
  [70,80,70,60,70,80,80,90,90,80,70,70,60,60,70,50],
  [50,60,40,50,40,60,60,70,60,60,50,40,50,40,30,30],
  [60,70,60,50,50,60,80,70,80,90,70,50,60,50,40,40],
  [50,60,50,40,40,50,60,60,70,70,60,40,50,40,30,30],
  [60,70,60,50,60,70,70,80,80,70,60,50,60,50,40,40],
  [40,50,40,30,30,40,50,50,60,50,40,30,40,30,20,20],
  [50,60,50,40,40,50,60,60,70,60,50,40,50,40,30,30],
  [50,60,60,50,50,60,70,70,80,70,60,50,60,50,40,40],
  [40,50,30,40,60,70,50,60,70,70,60,40,50,60,40,30],
  [30,40,30,20,30,40,40,50,60,50,40,30,40,30,20,20]
];

// --- Вспомогательные функции UI ---
const $ = (sel) => document.querySelector(sel);
const el = (tag, attrs={}, children=[]) => {
  const n = document.createElement(tag);
  Object.entries(attrs).forEach(([k,v]) => {
    if (k === 'class') n.className = v; else if (k === 'html') n.innerHTML = v; else n.setAttribute(k, v);
  });
  children.forEach(c => n.append(c));
  return n;
};
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

function setStatus(text) { $('#status').textContent = text; }
function logEvent(text, cls='') {
  const line = el('div', { class: `event ${cls}` }, [text]);
  const log = $('#log');
  log.append(line);
  log.scrollTop = log.scrollHeight;
}
function setScoreboard(state) {
  $('#team1Name').textContent = TEAMS[state.team1];
  $('#team2Name').textContent = TEAMS[state.team2];
  $('#score1').textContent = state.score1;
  $('#score2').textContent = state.score2;
  $('#minute').textContent = state.minute;
  $('#tour').textContent = state.tour;
  $('#weather').textContent = weatherName(state.weather);
  $('#place').textContent = state.place === 1 ? 'Дом' : 'Выезд';
}
function moveBall(pos) { // pos 0..1
  const ball = $('#ball');
  const pitch = $('.pitch');
  const pad = 24; // внутренние поля
  const x = pad + (pitch.clientWidth - pad*2) * pos;
  const y = pitch.clientHeight/2 + (Math.random() - 0.5) * pitch.clientHeight * 0.4;
  ball.style.left = `${x}px`;
  ball.style.top = `${y}px`;
}

function weatherName(code){
  return ['Ясно','Пасмурно','Ветрено','Туман'][code-1] || '—';
}
function weatherFactor(code){
  switch(code){
    case 1: return 1; // ясно
    case 2: return 2; // пасмурно (как в оригинале — больше зрителей)
    case 3: return 1; // ветер
    case 4: return 0.5; // туман
    default: return 1;
  }
}

// --- Состояние приложения ---
const state = {
  team1: 0,
  team2: 1,
  score1: 0,
  score2: 0,
  minute: 0,
  tour: 1,
  place: 1, // 1-дом, 2-выезд (как в BASIC: place = INT(RND*2)+1)
  weather: 1,
  lineup1: [], // 11 игроков (индексы из PLAYERS[team])
  lineup2: [],
};

function bestXI(teamIdx){
  const pairs = RATINGS[teamIdx].map((r,i)=>({i,r})).sort((a,b)=>b.r-a.r);
  return pairs.slice(0,11).map(p=>p.i);
}

function buildMenu(){
  const menu = $('#menu');
  menu.innerHTML = '';

  const teamSel1 = el('select');
  const teamSel2 = el('select');
  TEAMS.forEach((t,i)=>{
    teamSel1.append(el('option',{value:i},[t]));
    teamSel2.append(el('option',{value:i},[t]));
  });
  teamSel1.value = state.team1;
  teamSel2.value = state.team2;

  const btnLineup = el('button',{},['Выбрать состав (11)']);
  const btnRosters = el('button',{},['Составы команд']);
  const btnStart = el('button',{},['Начать матч']);
  const btnRandom = el('button',{},['Случайный матч']);

  teamSel1.addEventListener('change', e=>{ state.team1 = +e.target.value; setStatus(`Выбрана команда: ${TEAMS[state.team1]}`); });
  teamSel2.addEventListener('change', e=>{ state.team2 = +e.target.value; });

  btnRosters.addEventListener('click', showRosters);
  btnLineup.addEventListener('click', pickLineup);
  btnStart.addEventListener('click', startMatch);
  btnRandom.addEventListener('click', ()=>{
    let a = Math.floor(Math.random()*TEAMS.length);
    let b = Math.floor(Math.random()*TEAMS.length);
    if (b===a) b = (b+1)%TEAMS.length;
    state.team1=a; state.team2=b; teamSel1.value=a; teamSel2.value=b; startMatch();
  });

  menu.append(el('span',{},['Ваша команда: ']), teamSel1, el('span',{class:'spacer'}), el('span',{},['Соперник: ']), teamSel2, btnRosters, btnLineup, btnStart, btnRandom);
}

function showRosters(){
  const c = $('#content');
  c.innerHTML = '';
  const list = el('div',{class:'list'});
  TEAMS.forEach((team,ti)=>{
    const card = el('div',{class:'card'});
    card.append(el('h3',{},[team]));
    const tbl = el('table',{class:'table'});
    tbl.append(el('thead',{},[el('tr',{},[el('th',{},['#']),el('th',{},['Игрок']),el('th',{},['Рейтинг'])])]))
    const tb = el('tbody');
    PLAYERS[ti].forEach((p,pi)=>{
      const tr = el('tr',{},[el('td',{},[(pi+1).toString()]), el('td',{},[p]), el('td',{},[RATINGS[ti][pi].toString()])]);
      tb.append(tr);
    });
    tbl.append(tb);
    card.append(tbl);
    list.append(card);
  });
  c.append(list);
}

function pickLineup(){
  const teamIdx = state.team1;
  const c = $('#content');
  c.innerHTML = '';
  c.append(el('h3',{},[`Выбор основы — ${TEAMS[teamIdx]}`]));
  const tbl = el('table',{class:'table'});
  const tb = el('tbody');
  const selected = new Set(bestXI(teamIdx));
  PLAYERS[teamIdx].forEach((p,pi)=>{
    const tr = el('tr');
    const cb = el('input',{type:'checkbox'});
    cb.checked = selected.has(pi);
    cb.addEventListener('change',()=>{
      if (cb.checked) selected.add(pi); else selected.delete(pi);
      if (selected.size>11){
        // ограничение 11
        cb.checked = false; selected.delete(pi);
        alert('Можно выбрать ровно 11 игроков.');
      }
    });
    tr.append(el('td',{},[cb]), el('td',{},[(pi+1).toString()]), el('td',{},[p]), el('td',{},[RATINGS[teamIdx][pi].toString()]));
    tb.append(tr);
  });
  tbl.append(el('thead',{},[el('tr',{},[el('th',{},['Осн.']),el('th',{},['#']),el('th',{},['Игрок']),el('th',{},['Рейтинг'])])]), tb);
  const saveBtn = el('button',{},['Сохранить состав']);
  saveBtn.addEventListener('click',()=>{
    if (selected.size!==11){ alert('Выберите ровно 11 игроков.'); return; }
    state.lineup1 = Array.from(selected);
    setStatus('Состав сохранён.');
  });
  c.append(tbl, saveBtn);
}

function ensureLineups(){
  if (state.lineup1.length!==11) state.lineup1 = bestXI(state.team1);
  if (state.lineup2.length!==11) state.lineup2 = bestXI(state.team2);
}

function chooseKicker(teamIdx, lineup){
  // простой выбор — лучший по рейтингу из основы, кроме вратаря
  const list = lineup.filter(i=>i!==0).map(i=>({i, r:RATINGS[teamIdx][i]})).sort((a,b)=>b.r-a.r);
  return list[0]?.i ?? lineup[1];
}

async function startMatch(){
  ensureLineups();
  state.score1 = 0; state.score2 = 0; state.minute = 0; state.tour = Math.max(1, state.tour);
  state.place = Math.floor(Math.random()*2)+1; // 1..2
  state.weather = Math.floor(Math.random()*4)+1; // 1..4
  state.lineup2 = bestXI(state.team2);

  $('#scoreboard').hidden = false;
  $('#field').hidden = false;
  $('#log').innerHTML = '';
  $('#content').innerHTML = '';

  const kwe = weatherFactor(state.weather);
  const spect = Math.round((TEAM_STRENGTH[state.team1] + TEAM_STRENGTH[state.team2]) * kwe * 20);
  setStatus(`Зрителей: ~${spect.toLocaleString('ru-RU')}`);

  setScoreboard(state);
  moveBall(0.5);

  // кто с мячом (1 или 2)
  let withBall = Math.random()<0.5?1:2;
  let holderIndex = Math.floor(Math.random()*11); // индекс игрока в основе (0..10)

  // цикл матча: 90 минут, событие примерно каждые 1-2 секунды
  for (let m=1; m<=90; m++){
    state.minute = m; setScoreboard(state);

    const shap = Math.random()*100 + 1; // как в BASIC
    if (shap <= 75){
      // обычная игра
      holderIndex = Math.floor(Math.random()*11);
      const teamIdx = withBall===1?state.team1:state.team2;
      const lineup = withBall===1?state.lineup1:state.lineup2;
      const playerIdx = lineup[holderIndex];
      const playerName = PLAYERS[teamIdx][playerIdx];
      logEvent(`${playerName} ведёт мяч`);
      // шанс потери
      const lose = Math.random()*100 > RATINGS[teamIdx][playerIdx];
      moveBall(withBall===1? (0.3+Math.random()*0.2) : (0.7-Math.random()*0.2));
      if (lose){
        withBall = withBall===1?2:1;
        logEvent('Потеря мяча');
      }
    } else if (shap < 98){
      // удар по воротам
      const atk = withBall===1? state.team1 : state.team2;
      const def = withBall===1? state.team2 : state.team1;
      const lineupA = withBall===1? state.lineup1 : state.lineup2;
      const lineupD = withBall===1? state.lineup2 : state.lineup1;
      // не вратарь
      holderIndex = Math.max(1, Math.floor(Math.random()*11));
      const shooterIdx = lineupA[holderIndex];
      const gkIdx = lineupD[0];
      const shooterName = PLAYERS[atk][shooterIdx];
      const gkName = PLAYERS[def][gkIdx];
      const shotQ = Math.random()*100 + RATINGS[atk][shooterIdx];
      const saveQ = Math.random()*100 + RATINGS[def][gkIdx];
      moveBall(withBall===1? 0.92 : 0.08);
      await sleep(300);
      if (shotQ > saveQ + 20){
        if (withBall===1) state.score1++; else state.score2++;
        setScoreboard(state);
        logEvent(`ГОЛ! ${shooterName} забивает. Счёт ${state.score1}:${state.score2}`, 'goal');
        moveBall(withBall===1? 0.98 : 0.02);
      } else if (shotQ > saveQ){
        logEvent(`${shooterName} бьёт — ${gkName} отбивает!`, 'save');
        withBall = withBall===1?2:1; // отбитый мяч
        moveBall(withBall===1? 0.35 : 0.65);
      } else {
        logEvent(`${shooterName} бьёт мимо ворот.`);
        withBall = withBall===1?2:1;
        moveBall(withBall===1? 0.4 : 0.6);
      }
    } else { // >=98 — стандарты (штрафной/пенальти)
      const isPenalty = Math.random()<0.4; // часть эпизодов — пенальти
      const atk = withBall===1? state.team1 : state.team2;
      const def = withBall===1? state.team2 : state.team1;
      const lineupA = withBall===1? state.lineup1 : state.lineup2;
      const lineupD = withBall===1? state.lineup2 : state.lineup1;
      const gkIdx = lineupD[0];
      const gkName = PLAYERS[def][gkIdx];

      if (isPenalty){
        const kicker = chooseKicker(atk, lineupA);
        const name = PLAYERS[atk][kicker];
        logEvent(`Пенальти! Бьёт ${name}.`,'foul');
        moveBall(withBall===1? 0.96 : 0.04);
        await sleep(400);
        const shotQ = Math.random()*100 + RATINGS[atk][kicker];
        const saveQ = Math.random()*100 + RATINGS[def][gkIdx];
        if (shotQ > saveQ + 20){
          if (withBall===1) state.score1++; else state.score2++;
          setScoreboard(state);
          logEvent(`ГОЛ с пенальти! ${name}. Счёт ${state.score1}:${state.score2}`,'goal');
        } else {
          logEvent(`Пенальти не забит! ${gkName} спасает.`,'save');
          withBall = withBall===1?2:1;
        }
      } else {
        const kicker = chooseKicker(atk, lineupA);
        const name = PLAYERS[atk][kicker];
        logEvent(`Штрафной удар. Исполняет ${name}.`,'foul');
        moveBall(withBall===1? 0.9 : 0.1);
        await sleep(400);
        const shotQ = Math.random()*100 + RATINGS[atk][kicker];
        const saveQ = Math.random()*100 + RATINGS[def][gkIdx];
        if (shotQ > saveQ + 30){
          if (withBall===1) state.score1++; else state.score2++;
          setScoreboard(state);
          logEvent(`ГОЛ со штрафного! ${name}. Счёт ${state.score1}:${state.score2}`,'goal');
        } else if (shotQ > saveQ){
          logEvent(`${name} пробил — ${gkName} отбил.`,'save');
          withBall = withBall===1?2:1;
        } else {
          logEvent(`${name} пробил мимо.`);
          withBall = withBall===1?2:1;
        }
      }
    }

    await sleep(700);
  }

  // Итоги
  logEvent(`Матч окончен. Итог: ${TEAMS[state.team1]} ${state.score1}:${state.score2} ${TEAMS[state.team2]}`,'goal');
}

function init(){
  buildMenu();
  showRosters();
}

document.addEventListener('DOMContentLoaded', init);

