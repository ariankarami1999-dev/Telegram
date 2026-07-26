<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/OX6DepYrEZtE4USHcYdSCC7rfBhVkMRR_uMs6kDD1_Tqd--MvFG5LGXQCOzLCcNHcnym2iAMSSCixByR2TOA1ocrIPqR0e0w9iMzfzWw4hzFnChi1vP7ZYkmtpF5J3jYkfin_TSBJychEPPEZ4HcfQMxx2l_19Yan4NRlY5MNHoGM5zkyF74X8LPf4I6DNixgsHcUuw7cUdLUicdnxAthAMk2ftJbltCBCoMnhClntKXnGmSgMYFFJBYdBYC6tsOCo3x-O1cBalAUsfDfu7mr_lEgnYa9FPt49Az6uR_JCz2AtJ1V08virF4d8XFxTG42GRur_OUiVvnioPi-yr41A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 14:43:39</div>
<hr>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNiv87_bgx5Ib-4XrZoyPa1gkl--4Co8SXGWhFNdA3adZ4pKAdUmsw0nR4xgsHjZUuX5gsQVPFO5KezOwqWO3L1xbbmdEuQDBWHS8vjNdqL2hlpRK63tguR3E_cSuXXme-5saFXyw7fqXkvbeDe1AxXkD0-ULc-PEqXiVAowBx1jCqpP6dTtSajdGs7XnUUcLv5xPe-BJPkKDQCqbcGk3jEbZbQmffsyFrgzecKtTxHvJq4TnWU7vdfUUk1dtd6Ihua427Zs25w1xlxi0pNEGYQ6z2nKnwV6v8ew46_Oa32ikzchZl3UC-xEMjcfdBaDhab_meJ88qqQcqjjIXuC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkgFVC2gkf8pqf4xXWGIqRs15T_ThzjijgL5KfqRa1nkceAFIjhVbaFg4h0rbMEH2CpLI61Q7pthGfKmKPY_XkgcG8TyInsFRFs9XbuO0DZxkKLuIYEZTUTL2vcMo6mx3UYDHpq2emDvv6D6R11ZH47f8OCx-zShi-e8MNE8Cjw3YEw-W0_UNpSUMyCHSSpeJEWIEyEjcpwnSGaT3LNKrgODkmKAxcYSy-c-lDPivjdjBWT0MzhNiymqbM1vnpRUNZ4aRv0K7SoinrBK3LP0hEBVBSWwqhory546xk5jz9J1vZ1Tz4_jZq_3LpkTvzRMWXbZGDkVrxUPx7-ZbWpfMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/batrqa-JWqraiFwD3KPlrEOHk1skX1abuwhSA-BayhhwthlyUOMWdGEywcfzJenXr43KrHXigS2UUQXHuhiKXKrQ8ezlmG8mRvAS1WOk08tVmBPEoNh9v2Kc8P1thzJPU_vx-IE58voSzUu8QMelQEFHm8S5DCi1MTZ8K5Wfltle-2J4Jfef_WGnkUDtVhYaJwPGsoipjBuRoWtHy4sHsoFFCQOS1BgJZ6PgrXFzHBg6J0s2_A1i9GMKwNVA5x60slsPdbSeSQD86sVdh6aQNftoqL7HQe55igtTBL3kr6iDuBRFAGssuKZvPU_2gC7g9qUOAIG-SqZD-bmt0vyhKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKeDKf_6UkXDzui1SPIv2Yns23AqkFa-q2K00Wrtt5S7GKAjgPuyg5CINOoxCIZYcL-JTbenWHelM_gFjS7U-GoDec1y9kxjRnLBVqt2OXznl-HR635_epM7uDmZ5-vAykOUOucht9pb0ngUYeusO_sz5782HhYNe2NM0EMCFJPMv7edGEks1WOseytAEY98UpyGIqW3zNGiP2IF_2Q-kgiQ9q_2AjLbFTIJAb19_Zv-VJmqw3iRAQ07x37ENQomOgyHa1eBqQyTgmnk_QHHaUs-hTHOjtWEhZVEhwnnhE3wUIyI8RsUSC7ZeI_PUjuzxCDgooZh3Bp1dTJsH3vrTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=iuWPbpNHxteVCOXDv0dz-k8blWi8I1ib-851yw-ShhpLeT3PD3Y4kEguP5A-47eNYNGagLPIsswDM-5QDvDgyKEFdhs-9KVvvELve5pXwbjjid86noLSsE4ab2c4uwvoNnQXbusiIIT6qTmcVmSbQwnQhHQ7-fNgoJJVF51P2vZsVMakF5zsvNr3dFpVGhCQOmEvjKYsfSSw12sjUUOFoCxTR0GNMPm1HztEdVUEU4qmOm7hJnAXWyNuvz5PGq5xN229-MnvtAYUy9Bkq72iBgY4eBlpc5Awh5Ie09iU47XDX6Dy3CxMNMcK9y18s79wxSOznCqhJsOm7xjKQVkc6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=iuWPbpNHxteVCOXDv0dz-k8blWi8I1ib-851yw-ShhpLeT3PD3Y4kEguP5A-47eNYNGagLPIsswDM-5QDvDgyKEFdhs-9KVvvELve5pXwbjjid86noLSsE4ab2c4uwvoNnQXbusiIIT6qTmcVmSbQwnQhHQ7-fNgoJJVF51P2vZsVMakF5zsvNr3dFpVGhCQOmEvjKYsfSSw12sjUUOFoCxTR0GNMPm1HztEdVUEU4qmOm7hJnAXWyNuvz5PGq5xN229-MnvtAYUy9Bkq72iBgY4eBlpc5Awh5Ie09iU47XDX6Dy3CxMNMcK9y18s79wxSOznCqhJsOm7xjKQVkc6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWTwy7qFQ2leTVpbUv0pOGtqMnDhsmyLo4z-o-7nBI2Z9F-kTUxcrkDAT5LqcUt552dWvAEuWPEpjjnmmQXYZbj6mfmjnjmLYNLWSqh7t_nZiOrsD4hbTQOJ3bPFLJOFM4rY3aS03vNsSYxBaPY98YeUarOaw5NYg--fxUelxAu6kTC0VqWTmUs5mx6BMIScMXFqhTYuPA0aZeumcBVXiLhD_TRtTPrn2kv9ji9Id8Zw7LmmRqigFMptRZ1imxhuFRpwcq4cDbVXFeeDgRFabmVzuiMwHPHiKXCXGuf_jr8lhUkRNi-yVFxHjvTrbzGru2gea75qwjg1ZN8aGho74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmoQU1SJHWKFiRuqWWrJ5VflWt5s5N_bn2cxU9wmKke8h4iTyDG66E4n8tQ339OA1-Q3gHeGPf_PoppA9Rq8mX8X11AHr0LNbcGeTPmYZ_hhyAQIv7g1K15wjI1NxhCn2I17giK_4fEQN6QcrHG7MOPp0jO3f1kAgGKdY20bTHhHqwZmww4_QCNN5XyBpFJpexLcj0kQ1wmAwnJCmGd334OVgGNc2P-Sa_pkmC8q_9NqZKkH96WfURaL118iDNOpHlilGiApauT0NDhhVcL9-ZyLwoSMeZZTn9Wtgx1O5wJNgI3RFyHtThajKSpeU1r9EJ1YoMNxFB28_fL1JkHsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMm_ESU-hX2-8muoQSdzXE_BM4NLEtcn5J7l0m8TdQcx2vkrotM2d1UQIKqF4jF0jExUa07Mh7uCHsUifRB_4a-jgzjPkW8lhcjRTf0yW93aZ2CS0u1DWAfniKXkWiNMIcx_wy3qONuzKNkNeDlimLYsq62QWADVyNtcFqwW5C2SRZOt-O5aZ0FsKNcP-n54YlavS9Sm-sH_xh1G8BxWiVWCZYquEPGjIT99eFkH9Hock734ZczLuRLgWBOPtQ6hRnkZtMgY5EuNecQRI0NpBMzBaRIOrljn6VqsaOvdDmQKpF47Zw8nXGllxmdADVzB9WBvfEUGZPxehtHw0yDfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=N4fKBP0-QadePqd60EGUc2_vFWDr9b769rddUcYJJbSOhDfE53t0f0GLGri5n71c59mmrsf73K6Iprcf_3AOKWMDy6p0lhycxu4qpL813N1h8gs03W5vxFmMO-C0eOzOQ8QA837pZpt7FKKLgUfcJBYD9QmVU9pwSuDJ0RlpovsUtx3UWaPktef7HM20PEgMN9ZEiOyxbC9hKT2enCRAWzopxNgj4V3xYQ12wrEd8szBXZ0kmTXLP6AymnO_r3SD9Mvvv98sU1Iegevvx4PdfxRg50BQlQ05E7Fjqa7syndryWxQhbz-oOuryqwHf_BEIgap00EQ72yD_-ZVNL7C1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=N4fKBP0-QadePqd60EGUc2_vFWDr9b769rddUcYJJbSOhDfE53t0f0GLGri5n71c59mmrsf73K6Iprcf_3AOKWMDy6p0lhycxu4qpL813N1h8gs03W5vxFmMO-C0eOzOQ8QA837pZpt7FKKLgUfcJBYD9QmVU9pwSuDJ0RlpovsUtx3UWaPktef7HM20PEgMN9ZEiOyxbC9hKT2enCRAWzopxNgj4V3xYQ12wrEd8szBXZ0kmTXLP6AymnO_r3SD9Mvvv98sU1Iegevvx4PdfxRg50BQlQ05E7Fjqa7syndryWxQhbz-oOuryqwHf_BEIgap00EQ72yD_-ZVNL7C1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiWNIn9AjZs81MmjIvrcD9sGrtXBm50rUG-_C4IfxpIVO1uu23zeWLIfbq2TwWWoxFpD88t-B0iR3xT3bzSwqkzuU39DZiX1FUSgqJf1LiaSmAJs3nWTIwET0HAaKTGwcr5Dhx9BubL3uMBRq3ki6fE0rcRQIv7bS5sGzyrXtaEed-nC_n2unAA5d7ztsxu2MN7hUK98RyJ_uksgWzMcvYdgL2c5NgKWcvcUg4M6YUOHOZxZZl2QikX19JMY0kEJIFV0j9ciP797oFNzjHD84Pf1VrzbPP-tYlbB8aKzieOw-S5PS0dIsUcYgRvUYQUEC23L6qif0vILT-s7yJcDwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=R3yKM9_BDlDY7Zd6JRN4t6zp29o1wTNfoe9NW4rJanPA5ZPSf-ZLwelX6NBW6yB7OniU6mBesHsWi47XnJcMUCz1LEa-jnpiLLYsgG4mr80fm0j4Y52AQroiNrSEcexDY2Y-FW5XpRaUsPX-oRRWavW2vMA4Xw00K_POKFhF44HlwlAxMEAXtioL9PxRqa4qZjnjAK44yBEnkURU2UfHV9yrY12kd8edsQPNkwi4sjuAhnqSLwbm8zbAOpGrbKK8NDazgZaAsfOwnqdzKOzuE85Bgi7be1BJ1f2SeraEi13g2OpWtR_1yvpvq1qWXh36ciJCq0OoS-qB2eyaOEvDNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=R3yKM9_BDlDY7Zd6JRN4t6zp29o1wTNfoe9NW4rJanPA5ZPSf-ZLwelX6NBW6yB7OniU6mBesHsWi47XnJcMUCz1LEa-jnpiLLYsgG4mr80fm0j4Y52AQroiNrSEcexDY2Y-FW5XpRaUsPX-oRRWavW2vMA4Xw00K_POKFhF44HlwlAxMEAXtioL9PxRqa4qZjnjAK44yBEnkURU2UfHV9yrY12kd8edsQPNkwi4sjuAhnqSLwbm8zbAOpGrbKK8NDazgZaAsfOwnqdzKOzuE85Bgi7be1BJ1f2SeraEi13g2OpWtR_1yvpvq1qWXh36ciJCq0OoS-qB2eyaOEvDNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhqLZIw4aPszHN4hhN5JnJGr14vrVfmyBQakgtL-HqBEUUxIxXiIPSQHmCDcnOQdVm5PLK-EMCvtCu2Wye6o4zdO9Dw8do_O6VI7JAP_CUFHXCTyK8haa67rS39TaUGnRTWL9PCdnwjrn7IiQ31u4qJUbbT0PQTFRchyiRl8B3qh8H0yPqjQFpHzXrBg3cDsbLe2e2b7yT-hyg045AuUE2U5f5RkU1yYE-HDXnk-U3u0-hB8tv4cC_ahSfTXCQeuoDYzznQbZ4YPJxHpZyeJl7kaMiAzlRtclSgzBFqQMApvB7N2wbEcvFwxu3Ja0KH2IAi5En_H0x0kQQLPYRo_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdURYNMej5Y4qC0GwopHF67vnAvk49B3szvP3MkIhEWgwSj62VPgTgUqp6SKfhS8ebApH2oc1b0L0oYA3dd3nNvkaxZPiAX6smCOATY1wgVU3AQ67U6hPZL1cOyFmfbqLuHJorV-luuxjfKjiSgpOt2rQZr8LJWpVoAf-r7yQhxvu92WkO8zQfwV3lHCtDBiOyau_bPmGiCVIHak1b9OYCn38bFVu4db8kLdKHm42Q6niModwrcmABJ0g2JCmIZRxA__JPVrnbC2TWxPCp4HYkkdz7mLYu9Lw2STCMTwYbrhZVBhctff4_gNBCKmtdAHLpwKmJa4dXxT5kYM0I3kkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=Xp_mD7LlDws2UcrzIahRl3ub6ns5jxJKJZSA4oXrLH0Lt1bIFoFauc5Lo1YgVnBbS5RPoQ0Rc0hncE1ZAvtOgnLWP8wI5asCLzw7uG1s64-43tHmoetYBAFoR7XfBLXVx4rJA3HeyZd0mFVi_lEuGy8hkH1nLE7LYs932RfMvk0OhYGhC7dQlxr_-MkeXLMuZdIbTMpQu-kbAUSchY2qiLfsxfQb4qeboB_MqLr3SXrgQ0UsNAMu7UvHoTrXXGYvqvbtPlGlllb4vOl9mLGMS0B1jw1PGAIueUT524pMEa6YKv-XXIZrEkzkA0johezCnwl8f7PeWbnyDePJOOobhHWtDtzICge_yI8-o2qZJr9REvYJbPZKnjvoIvG6kmWan-s2eZxk_LvLLrUJ8QcItuz22qvdwOGiLOEeV5SAqDR0HcPmrj1w4YRkwzFM4TFVa0XWXMIFjmUQA7BEXj4gE2r7jXcFE1DXwtiu6Fx4g8UyC-tXEd4GEIAeNRHSHXYBYwK-1etEsC-L7uePEENWVSfHAAis33C45JVjnMBmLnqZeK247a-mg_u7ztE8biVfP20_ctx6mXd2fr3jMGEdM-DvjvurYeuqNsvq2xa3nRDGGK3ScBkyNSE2bJ0P5vJWYV6VIcHyh246RyQiCqkAF-cQynh1u-nax29VPW72x-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=Xp_mD7LlDws2UcrzIahRl3ub6ns5jxJKJZSA4oXrLH0Lt1bIFoFauc5Lo1YgVnBbS5RPoQ0Rc0hncE1ZAvtOgnLWP8wI5asCLzw7uG1s64-43tHmoetYBAFoR7XfBLXVx4rJA3HeyZd0mFVi_lEuGy8hkH1nLE7LYs932RfMvk0OhYGhC7dQlxr_-MkeXLMuZdIbTMpQu-kbAUSchY2qiLfsxfQb4qeboB_MqLr3SXrgQ0UsNAMu7UvHoTrXXGYvqvbtPlGlllb4vOl9mLGMS0B1jw1PGAIueUT524pMEa6YKv-XXIZrEkzkA0johezCnwl8f7PeWbnyDePJOOobhHWtDtzICge_yI8-o2qZJr9REvYJbPZKnjvoIvG6kmWan-s2eZxk_LvLLrUJ8QcItuz22qvdwOGiLOEeV5SAqDR0HcPmrj1w4YRkwzFM4TFVa0XWXMIFjmUQA7BEXj4gE2r7jXcFE1DXwtiu6Fx4g8UyC-tXEd4GEIAeNRHSHXYBYwK-1etEsC-L7uePEENWVSfHAAis33C45JVjnMBmLnqZeK247a-mg_u7ztE8biVfP20_ctx6mXd2fr3jMGEdM-DvjvurYeuqNsvq2xa3nRDGGK3ScBkyNSE2bJ0P5vJWYV6VIcHyh246RyQiCqkAF-cQynh1u-nax29VPW72x-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Fi_wh2e5BrXUiTxpUXyckzuIofgyWSheqLUPfCRJpDozQ1RytJZ2hp7DI6nFXrURRQI0A8tpUTeHg_3RVynQlPpSqgeuGUl0kGQXbtmVYsBDK3wBOnIpIfDDFn5rRM2d-ipjB0PiCIaK1lUjqURmezf4YnMQN7WK2priZaG9mVMHEGpvizsq9_DVCut1PZGaR_BZwcWtuiUB2Wv5rGhmm0zU6tRtqI2HP7eTsHhBJXvb8OQGbbB9R5nbGs514QiXisewkJXaK9Q5VS7bHNtTK6UbIvf0ICy_xpnBNYwf2KmbCKgaCOi6bHWeClkztHBbL4C5liry9b5HKsOVXuUWTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Fi_wh2e5BrXUiTxpUXyckzuIofgyWSheqLUPfCRJpDozQ1RytJZ2hp7DI6nFXrURRQI0A8tpUTeHg_3RVynQlPpSqgeuGUl0kGQXbtmVYsBDK3wBOnIpIfDDFn5rRM2d-ipjB0PiCIaK1lUjqURmezf4YnMQN7WK2priZaG9mVMHEGpvizsq9_DVCut1PZGaR_BZwcWtuiUB2Wv5rGhmm0zU6tRtqI2HP7eTsHhBJXvb8OQGbbB9R5nbGs514QiXisewkJXaK9Q5VS7bHNtTK6UbIvf0ICy_xpnBNYwf2KmbCKgaCOi6bHWeClkztHBbL4C5liry9b5HKsOVXuUWTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz0apyaGlsR1jTcccvP0RFJUdAYuewvXDfx4ZfNdsFiYXCI_FwfGmLL_WaebktkYPSKiEA9zSs2DoeQVH6jn8wujUWm2-1doQB_8MNxz_WR6fTGPA1bXk9NEH61mKWviA4pCmaLLqbhrIk5dofpX_ZbLv08_Ehc5q7aS-26vNUr1xK5xLgdRcOwAZuDyVEog0s7aRoCeaquCijr45Yigow28oMb6VtU5M5Aw5FGKMxcmenzuOtsVKnNzmea6YM_0CfV2oGQdUJ36wN4SJaxXZbrj6kjirR-gEPj5ycVMWw23OH8PisbsZmOjseegDwPEL-id9Q1emiKpGsCoFGT_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=ZtoSeoz_n5HHYp_b60dLI9usT5b6DVzJ4BXJZ2DWtqpIBMHVdEZY-8wJzG7w7TM6z5mRKp8I5F1FkBmZKG0o4mT1xIfWM1eF7FUuFv1J2EAhCdW4HNSwB1RUqt0482h-x4fyTYTGEfVj86-qI0D_s74MOo1Q-6zZdiGYczkuYDYl7JllkcU_9tU6V-F1MP4zmHh4Dj9bBh0zgD5oz9nEb5ahjVo0i6bbvOtHrj7D7sloLHiQPvKN2Jp6U9pQX4BfM0PGW0Zj5_3oy5cZ3JQi-_14-cqEji9sD_YRYTG7gYBHsBAwTJg0k1isKOuje-c2wXO9m2joXKlToYIlAyERUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=ZtoSeoz_n5HHYp_b60dLI9usT5b6DVzJ4BXJZ2DWtqpIBMHVdEZY-8wJzG7w7TM6z5mRKp8I5F1FkBmZKG0o4mT1xIfWM1eF7FUuFv1J2EAhCdW4HNSwB1RUqt0482h-x4fyTYTGEfVj86-qI0D_s74MOo1Q-6zZdiGYczkuYDYl7JllkcU_9tU6V-F1MP4zmHh4Dj9bBh0zgD5oz9nEb5ahjVo0i6bbvOtHrj7D7sloLHiQPvKN2Jp6U9pQX4BfM0PGW0Zj5_3oy5cZ3JQi-_14-cqEji9sD_YRYTG7gYBHsBAwTJg0k1isKOuje-c2wXO9m2joXKlToYIlAyERUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGD1Bi9ODSXHBfVMe5tipnhj0uk52mCZzH1P13mjIb4FlYeWiBrEdoHZvShVlGMzeL_9iGhf09Bb935hFV1f_1QETIWJSsWI9YgGsQc1IbJZllOWsn1M3bBHjVWwHPvtnk09a8uZ6_vRs48RTYd2jx7ty-M6I4srb7rd6FN4hjIIWQBUtog9XjsSl7jpKt_GyMOoW_7LsClw4zYcGvytMPgirY-YTGhVVbi9W7L5wqtS86v_5V2nymH7CzUnQnmJEbuLBph0o9ihpSBhLHAFrtDrQmCHxXpdOW8tj7zb0CB97jSqhunFmQGqu7R8ymi6B986mVwojGXB9Y2BuxmFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOkKYzxRFakx-UppIPZ-lrOVeYgKJl6iLWaPNYCFwXujJYRjYFy4W2QGywtaD_x6sKT8AhUnFiWfnq6amauMiuzbS9jUoFiYwg6SsRSJIXAud--UNGnGGT_r5GK-BC1FFlOhePmbKO2S-aj60oOpUCUNl-FbgAFeZh_L8S9p__t0l1fBzWH2BEOr4plno-KwUQEEDZRgPhEZwsCPbzOPWS2_ovFGJg4OuFx7P8gCDtua7_hK45PpCEFi1ymPAnki9IdzfYRFz9u1wzGfhkefWeMGhnob2Nfr5LvGh2v6gKFeIm5Djds-ew57Jo5y_tmgD8-jO_R9AD1FxArRqgpj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkimbECxwteu1ynJsq5NInT-lPHd40R0SAMzqMssMd941AhYMbCFTqBYWgW83-43IameahaskzJUauhomtLAuqTdRGlcu2At_42vMnt0NEae02s1XvnxTDlnnS-QQRLx3nDExUKINpRkKL4hteJ0NxAYxHzvtZS523m_Q8ksn_0IehU7bOg6vYtl6aNXtyvJpRPjBMoNLrQbzr9ytYsvsuLrXbmvS8JsRwmX3nZ2hLOFA7nBX9r3TAhi_moO4xI_aRpniOVfDC11EPCVSE5ypkNQpRTkztRw9-p1PMqw3Xkry7VuHQNtfcqON2aeLsMqQyg7OU52FTi2pb1pbsJ_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNUGC94BjClytTuSPBulsFOGgk_FOush2JM7HIEOaWesFL7NLNXBdKy-jmmpaN8QmzcA_68wGTysctE56XTiE2C5FleZZFPCfWdR83IITeK-5Wic1o5GPSDa1Bj9UD_r7LM7WV0S7yhWOAC6VAbe41oiAFMhA0JCctrkBCBVF9VlqZg5z_3Q_SXcskVCk2yuxWQVM0xf4WSb3EmMIgfryZVPpVRLsg02pBi8pTKinlOEdMZnhmv3Ief3G-BKW0JJ-pd0n_j5FD19tb7yL4qpmA53sW9CK8jEMAyGyHGk39H2xow-xJUnrr_YJGzsKGKgQr5ybh8mPyaQX90IP-fkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBAydvbzjYQkQgf04uxq8Dhy2o133ET4cNSAd-vOLJPK6W-hwuAAIM3A2zUgRa2HR6gkvxwWyCQaUCXVHSFgx5KtGBcyUbGtOF-veOeJaegixPcqAH658Hpo26iA-QJc-NPiRC5xcH9h_l9Kb3B5Q7VPHMfIt0E1hCMaLaK6df1Jx4BI3wO74kJsZNqHlMFQqw4waZZFXK8ziH_EYTRXDs_q0eSb7qAZl0Qc7iPWP9Ps42umQ0eNPqlVDU0aqpduzULHu27bgGNbD6aCZktKagszXj7wJ0ZoXwcueI0MoUsTW76hgp0PHGxxjjRjLuL7G-Yf1jaY_VfrWYIW403XuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=vyC9Tc3GRv2aTDgLTRlL-_odUIWCojmg1vRCMnFOm475wdJkvigQt461T6DZ9gCZgRMMnHd9l420IH_4E649rQYhnV0nWJlA3TywNz_gL9j9d7lbQz7cyAXlaRtIjhUdVIZxB-BYFXTw4yzFhE3HaB_I23bdfA-H1zNXpaT4FeeHvW_WXJoq29JZM8D6M80LbFHRmVD30t3NxBFyEA7ahPdfpansLl3pW-GA3iCUnKBNfWnr3z-mKCeImxAJCRbe4h_0c_ACdxXkWG1DWmE-QtOxeEDP7MGckjcxhXGBnospmvntYHnUTIgyexTdTfgaVBgGtntHi5HNUrGa2zouig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=vyC9Tc3GRv2aTDgLTRlL-_odUIWCojmg1vRCMnFOm475wdJkvigQt461T6DZ9gCZgRMMnHd9l420IH_4E649rQYhnV0nWJlA3TywNz_gL9j9d7lbQz7cyAXlaRtIjhUdVIZxB-BYFXTw4yzFhE3HaB_I23bdfA-H1zNXpaT4FeeHvW_WXJoq29JZM8D6M80LbFHRmVD30t3NxBFyEA7ahPdfpansLl3pW-GA3iCUnKBNfWnr3z-mKCeImxAJCRbe4h_0c_ACdxXkWG1DWmE-QtOxeEDP7MGckjcxhXGBnospmvntYHnUTIgyexTdTfgaVBgGtntHi5HNUrGa2zouig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-dSvyc1iJ2LzpkL7uJUtBHLX1px9ZC3BNXYmQHzkMRLiEqPkqP8bxLMTHBUuUQ0nxusHb74303mrSr6aX_wV0KZiVJEz2tW45nosTCQHXiVm31isj71R6iUYEPnCHYkyUCG4E1xhp1Hf6gOU3U5ogogibPlgYutWYaGy8Mt61eD8lz4D-aCfsTvSQH6qLi5pEcYSWxjXSQXsqQmWB3db7dDzydLw1iVJkd1f7AeUd5YDkhA9xZ6dAHIUeKJ2EhMHqv2mAfycJO1nA8_MpitoWUxSThq08xoY121WpJReORLzYd3Zsov_iesymBYFq1PgjTelbWPlvuQtjF4lmnihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njmdgTpbPpZadEYDeGKnNYzqwid7dfTWWjawyE3f3WAbZshjX6SZx1n1rhC0qekxVl_9c-Sn_vK53j_nGCDqT6eT7YiYCAua619u5hmhw6XZRKDEAb9OFv1WjIrUHTc-xBzfD4Z_Lg6zp-cdOhEpsRKLa7YN5bfNOSY6Ls7sTZd1RFJ9d18Gpg6gNy0XlizN9SNX12VamrbcPomSzfZeFGgSf-KXeiKx7dxK9Oi9Hr8xh5qVgTGDAYFFDTTGYVZy8THHOTEOo1IpgHPOgU5oRokEsK9S3exps1SCVQ-SRBrxDRZnsesXCt1Ky4LENL89c1NkbkmLKZBfrdQhUWtfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=MoAuetjfRLmj2LHkU1Xjv9FLQdjYQBsSvGBzil9ouSx5PVNFxVJ-5H1zcTVl8TBAOeDMFb2qYZP3j4gsG7gQxjp44dlJv7pfzEo4ssBM001SbnBN92G1CGjCcDtqBOe9H08YKBHwonpcQINvBWHhYGZDPMhpcGNFdjWFliKtkqvqu8bwZHk8hF03us4Nw2FQBeVYg_jv-f1ncfPJUqod6o08a4LuwzgPFylSGseJLSWU6iwCvMm4zvxhY1ffoyRPS3fVi87J6slWpDBxI_tj0Fw7IAFLSKj_xrvDMfUptp2ujHqyEoOpbA24385OROBXUuP_0c6uKL5Xo2z_8tgTk48WBUxTfeKeWBAGMs1wf1AFd6Kk_UMboVKsyNV48NAARBHGmSB-1100jVcHwMUFyozzkj56vw21PhC5DviUnPKOxTI2vU_m3AzVsbJ9-FjL8lBNaTCk312ix6flwuzqgS58bIwVHla8OS4tRVAgj4z3F7210hvnUVEeR6qepvpAW7DSkuB_x_aKZgd2C4FgxXm33pOHlxQwmE7CGyTp3gSAShv-Zs0N8Dw8zlVnZIa5mVkjM6gZAHCAFmFnmrJf58-FF7Xpzd4gXeD2XuKZnxzMKHx9avztJUdDPFDCFpmZ15bIHvjIZeSCx07El2W2phdGigPebS4sjBUxqTZZFtE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=MoAuetjfRLmj2LHkU1Xjv9FLQdjYQBsSvGBzil9ouSx5PVNFxVJ-5H1zcTVl8TBAOeDMFb2qYZP3j4gsG7gQxjp44dlJv7pfzEo4ssBM001SbnBN92G1CGjCcDtqBOe9H08YKBHwonpcQINvBWHhYGZDPMhpcGNFdjWFliKtkqvqu8bwZHk8hF03us4Nw2FQBeVYg_jv-f1ncfPJUqod6o08a4LuwzgPFylSGseJLSWU6iwCvMm4zvxhY1ffoyRPS3fVi87J6slWpDBxI_tj0Fw7IAFLSKj_xrvDMfUptp2ujHqyEoOpbA24385OROBXUuP_0c6uKL5Xo2z_8tgTk48WBUxTfeKeWBAGMs1wf1AFd6Kk_UMboVKsyNV48NAARBHGmSB-1100jVcHwMUFyozzkj56vw21PhC5DviUnPKOxTI2vU_m3AzVsbJ9-FjL8lBNaTCk312ix6flwuzqgS58bIwVHla8OS4tRVAgj4z3F7210hvnUVEeR6qepvpAW7DSkuB_x_aKZgd2C4FgxXm33pOHlxQwmE7CGyTp3gSAShv-Zs0N8Dw8zlVnZIa5mVkjM6gZAHCAFmFnmrJf58-FF7Xpzd4gXeD2XuKZnxzMKHx9avztJUdDPFDCFpmZ15bIHvjIZeSCx07El2W2phdGigPebS4sjBUxqTZZFtE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=jGoQIfwXNS0PTLDRVN2XPv8ALwL855Exa_PTSf389lSM5u2uGnLmXtNER-7XeLu2ZVEXLWAG_T820ir_ckvjwF4KEt1NjdjjDyRr0JIPEov16comH75N2CMsZOuG4noT8hVNSkrVk-YwGr6TT9CaZmDQgU2NoRczJCFtLelAuvvsGCZb5L0RsZcDrvp4cNQ05N8wfX_jdxayHOqMLJUoVCZ8fNpe0akkMxz0ziwOgThQmLqmYgoX7OyHwYB7L7AHL-VyHCEv1ZNsFouzndjJ8LSzs0vYTLaQY3vZTZRSQS_tFIDdBnyRqmEJweFLPvdW7lmzhcBvUAGxSQw3UGKhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=jGoQIfwXNS0PTLDRVN2XPv8ALwL855Exa_PTSf389lSM5u2uGnLmXtNER-7XeLu2ZVEXLWAG_T820ir_ckvjwF4KEt1NjdjjDyRr0JIPEov16comH75N2CMsZOuG4noT8hVNSkrVk-YwGr6TT9CaZmDQgU2NoRczJCFtLelAuvvsGCZb5L0RsZcDrvp4cNQ05N8wfX_jdxayHOqMLJUoVCZ8fNpe0akkMxz0ziwOgThQmLqmYgoX7OyHwYB7L7AHL-VyHCEv1ZNsFouzndjJ8LSzs0vYTLaQY3vZTZRSQS_tFIDdBnyRqmEJweFLPvdW7lmzhcBvUAGxSQw3UGKhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIr6pjyYtBTYFiXRBtcUz-TkpqRBt2-n9f2WoEHqwWtPfsKNGyrZfmcqPvGl4CM_LwzEQeToSB1e1dyG20M17RpBc7qqIWaIMta6QWE3riaDPugxu1Czu0a3Glx2RGkxQrqkFpw5TBm0N9PRU6gbh86-c4dPBT_3zdJKlj4kNZD_rynNRbSL1abIB3b_nULukhLoxMZfIWhBvpB9TJA2avJLxiTlRLt8J8L4t4AcnzYqr1l4oi2a1ifyZYyMXxN0-6Ikb5Sd4x7QA3PbSpCH_yTYJfgFn0f-4DKp1Lfemw5Inq9NAHagi0mX6pHYUjnjVp2cGhjY6_2hoqQ2etW7Rdmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIr6pjyYtBTYFiXRBtcUz-TkpqRBt2-n9f2WoEHqwWtPfsKNGyrZfmcqPvGl4CM_LwzEQeToSB1e1dyG20M17RpBc7qqIWaIMta6QWE3riaDPugxu1Czu0a3Glx2RGkxQrqkFpw5TBm0N9PRU6gbh86-c4dPBT_3zdJKlj4kNZD_rynNRbSL1abIB3b_nULukhLoxMZfIWhBvpB9TJA2avJLxiTlRLt8J8L4t4AcnzYqr1l4oi2a1ifyZYyMXxN0-6Ikb5Sd4x7QA3PbSpCH_yTYJfgFn0f-4DKp1Lfemw5Inq9NAHagi0mX6pHYUjnjVp2cGhjY6_2hoqQ2etW7Rdmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNqIWKaHfDXnJScr7ag-2Qcof6ZzUYi3Be_0iLYH_Cg_3N1nhdGiuS_sA9PKYjIFiO3doqyBqhkejjku86tMGVpsahD9c6x3CL-XF-vPsfTR7d5d4-EOKR9V_zIX3MrdLCEs_tKj2jGPbFW2wIfrvNd0yQGwpOAI0jYK0EmDr-KZmch-ntKsBAOQzIPRYLliFDvLOl6Pay23cGKMr4dRdYtLYoFf86_y1wrku1sgjSMveGlyTfoCswklXJd80oN_c4l5pK4sUHhIalYKZQ6q7w7EGHVMkH_RPvo2l07CyEA95LL9VBzHYpG5Jv158e_HjgJbxHdOHfK43_qfk18pUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beBlRy7ZR3-n4oZL-0s1FKXZTARDybGYXeUvT-SWYYLfgui9DPuZ8SYsbRcHsN_W1moJnJ8TmooZKSwnVAl7ML7DnX9Re1DGVhW1r6eLN5WmdcPIuK1Fk42a_JqqcOUPxDY1vUOvLE12jvHL3W6m4yC2xjh38agkueSLMrpl-NhWue22YI8h1I0Q4UM3XKQRryojFQ01IKfG9hkfxTggAcwILrQLoUUMfaxo2i7JUqRjWPxEqpyWRP2aZf9MpFL3Y2F3rqUJSWO22rt2b2p4kBG2lq3t-knhEllWv2CD1kXZbhHMCcD1hoODPE2ACPkvZ9qDsg-NGkqW8dE0swNYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdfqKmpfYvYe-OrYwkU1MgKCUpFw5mlDyIY0UhkrR5WWqpWNfrfzeYwUKMh7ezMeXxb3k5ZjFPozzAsQQ8SfH4HimC8_XdLov2_92LyUgxUFA7gRIpoIyXWpNB8hgDpD6NJ1waLjTtmtPTVEe4B4mgodazNLJ0b50czKS4bxkTetUaBc8B_Ub0CjdOaSw_VKNn8Z0MTpUVvGJk5P2q7RYpthIvrwlqDEpIxYMpuVtmyfPxuRICFuI4xWdZIsTZrFUhKNFbgm1MCRTdPFV57pebChBuU_xT537eDWzG-wfL2W3cIDAO9vW-so39cMsVJ9eKtw49vtosg0NPqtUgaonQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=MPbS5LapZ8dnXukz8j15EXfVhRNia9cWQvWPvZzJi7LQIfSywAmAaoS9Z4STaHCdCSXlHw8P0Js4chfhZf5cemPOfhX-Naf0cGDPsMljgxsTfz5gHDoNlF7_ZsGxmZpuMY42JngiSDpkGKRRatJDlUH_beNIMelIVDcqEDyaRFgZ62DDV2CTde2gRFrxnROAMa7Jgqa8cfp1_Gd9FxPU2Hhf7Xec0afPUXY7_LoxufE11FQgRD3LgbfGDGZtpTVLHflkjAoYKEFS56mkb32eLf-LOE21OLHo_Gw4yzj-BJvKSGSpjqQApDQ2MTQUzbFyS-GMaDcSfnDSpKR67jskMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=MPbS5LapZ8dnXukz8j15EXfVhRNia9cWQvWPvZzJi7LQIfSywAmAaoS9Z4STaHCdCSXlHw8P0Js4chfhZf5cemPOfhX-Naf0cGDPsMljgxsTfz5gHDoNlF7_ZsGxmZpuMY42JngiSDpkGKRRatJDlUH_beNIMelIVDcqEDyaRFgZ62DDV2CTde2gRFrxnROAMa7Jgqa8cfp1_Gd9FxPU2Hhf7Xec0afPUXY7_LoxufE11FQgRD3LgbfGDGZtpTVLHflkjAoYKEFS56mkb32eLf-LOE21OLHo_Gw4yzj-BJvKSGSpjqQApDQ2MTQUzbFyS-GMaDcSfnDSpKR67jskMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQZJPMvemRvIwDQqr6wTIrw9xXqXYc5gsD4ZNDzFyHGuHE37vcRh3xHOvSBdtblGwNpbDQXBuCSOiFF7NNqyGzgDbKN8GISOGh3XyrNkwbsV3bziEzCzAJxgQiAja3RltsSG_gFrJQWVVMlrmTMnVDVx2trEiidH_jajzAfsiTeBIozxyT9R2q3ivHZQIIBsrZ2LzySI66BUxu71j_LnhQ-zKnmGaZIJn_J9Mv2CcPzI-UzXcxHY0zahL9-_VMcPEPjMTdUEvzIXABRmog5kzkRVTCKkNtuhi0i-LTku_qj5gd8EL_8z3Xjt5YcS2cFc45R7M89U580TfM-rzJi2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hb79qbfZE_wW8bfqiqCZpayFgh8ZRRnPsqP_nv305fiH-j4YxAnsJBA-Y40dYNJj4IiXSRyF71tDyA1RNvXILMIKwXXPFEyaCd8-dgHwG-QkkLCHwMxk7SeZKSj9x1SaDk7u1wz_Xf_HjeuT4-IdvGBDZNEMIsT_i2c8Q9rJPb_hHcVPT3-_YA3GVoAw5l2dGNsuDVDzikIXfyI8qwLXL9ffhecbZ77OgK9sW-s3aSkXiQT0p70suIqcLWTwPP2EkgO9PguZgLQpkf7YzTJqESNwfRCnBhbhEZiVYLh4XbLr8jd_A9VeAbOdEwfj-ndBUYLDL6kYQiJ7g_U_myy_Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BC6JqHcwmbZQXfTjHST1hfduMxvEjnxwJ6K4IQ_N-Pj2faHrAY5WafstmBJGjUIRV_t0eh6rEkN8yxQgBk6LIl8woTdXduwI8QpuNrg_tpeMRkIvmpkyep2IaPbaJxgs4V-lTKw1DktWlneTvXjdAL3Llt6VwjT8t5qZ_-iM2eWIgKIrx9u3yoidsRvRm5T6Obk5YjRXGGnL2kuqGRPnNSL2wR2dN6PqVlwIl3OQUkLC_tmdMFfouImXAOMDjC6kjA5vHW9OffTtVvs-B3fvx1_bZdJq-geFc8CqiJMbcMwL-zKhSej46ZeGiwJ4CXRnB9HaudwLC-mg4zbgMsp9zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHI8CFHL7SFe5StjYNorLe3rzU0FrvRYvJD5qxEavASh6op4edZ2gwZf-8Zg40EMUZCJ6OvIcvYdueg6YdZ9ycrveQU--aLn18Cpft3whoTHqIARAspy3Gae-s-Ge54_EyB9s6yLKWzxASMxUbvRVe1I6StkmftphCYXL4BBMnHLz5N0qRfjk_nuWrWo2xFcd8VFfQrB4YTyuaa4XGTs47ZJcqseXjMMvgXbGmZk9jZmjUoNlGNfUB2Ca6EYlsJJYlTaAgUanFfEibAogjLOwSRa-DkWI3I4-nuXO9xP9Gwv8SqzZTytpwO5JK9TUbSqBQETq7tLugEFl7vAz5WTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=HUZl7zH5BxNEf7NJSs6GIfLqJI4Rlw9PhY32dAkN4OEQNbTNH-fmHOubOh8wNSQVpSQgcoejKBR6gRMgKeA1HyUSCVzgccrNp6p6mnudS7BgkUBvWWa6rJf9k2AmSRvqJl6hg8Q4OGS1TLFlVt9F3cdBOB7y42TxuakUQjRvOjOGdSoCIWY1G8RsS4ci5QkVpX4xmoHKQe6tiASfmwBiPeewA7mnb4HTilJzVAMPCMjKe75cWhJqYJUVmZsNwJe6WLTMO1ZHllC9KgafDXTLJjMKJiy4vn0LCdV4IvV5-46ReMzlVx1Z503nNiq09shtE-UPQol7ZSKd0xezNHfQtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=HUZl7zH5BxNEf7NJSs6GIfLqJI4Rlw9PhY32dAkN4OEQNbTNH-fmHOubOh8wNSQVpSQgcoejKBR6gRMgKeA1HyUSCVzgccrNp6p6mnudS7BgkUBvWWa6rJf9k2AmSRvqJl6hg8Q4OGS1TLFlVt9F3cdBOB7y42TxuakUQjRvOjOGdSoCIWY1G8RsS4ci5QkVpX4xmoHKQe6tiASfmwBiPeewA7mnb4HTilJzVAMPCMjKe75cWhJqYJUVmZsNwJe6WLTMO1ZHllC9KgafDXTLJjMKJiy4vn0LCdV4IvV5-46ReMzlVx1Z503nNiq09shtE-UPQol7ZSKd0xezNHfQtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=OZpkYl1jATaMcOKcXfnp9mUHHOHgC5JXcFGaCJSIlRBDg-MaLEyyoEDHvRGbI9aNyJiO0-Mguxn99sAZqpl2qta71UrvZ9HDa-w0sMq0nra2_bOoj2UK2OQL18umTB0CEJ0i090sohKEgdhQXJ4rRslZijq9AfDWFSoUA6pfIEOQFSDkfR__v5jm9-aRSqJUuFqgwhDdRFiJRA--Kg4JXPm_54Le3HsJ2VAlYZJ8HyxcDDQKVGUJZ5_C3NXiNGnIT1gK9YTzTBNNN_7V47Cndj_mC0Bm--xSOv_4GvCyecWeAxjf0IVPlvh3Kkcm6TEsp9JJGQYfJY4GqA-qLUAZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=OZpkYl1jATaMcOKcXfnp9mUHHOHgC5JXcFGaCJSIlRBDg-MaLEyyoEDHvRGbI9aNyJiO0-Mguxn99sAZqpl2qta71UrvZ9HDa-w0sMq0nra2_bOoj2UK2OQL18umTB0CEJ0i090sohKEgdhQXJ4rRslZijq9AfDWFSoUA6pfIEOQFSDkfR__v5jm9-aRSqJUuFqgwhDdRFiJRA--Kg4JXPm_54Le3HsJ2VAlYZJ8HyxcDDQKVGUJZ5_C3NXiNGnIT1gK9YTzTBNNN_7V47Cndj_mC0Bm--xSOv_4GvCyecWeAxjf0IVPlvh3Kkcm6TEsp9JJGQYfJY4GqA-qLUAZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=WpY3YrKvecZrZKxIMCzNY_Krk7F4zLLYnFaKmO3ZKXKSK2HEUn5KFgcycomGc-qJr3McSEUo_Phd3-_lzrz1RztjCKQXSJ3pFce2NaK6k7s0N3_JfNOZ6_tmBVCUQBwEOHN6AMbMc52gfg7PBxE6c64H3yi73g2jdbtfSZ5wA8vTuvrYK5aTlAwGQthEsj3waqi1kms50I3a2uLlLRi7LS0gu_9SPvcKIJAg2oRnlHhF5ymJEaCuKMMsIGCGlSeeR81TdNSPTKDwPvgzEVAlhMCYffoychARjgqWi2T5oF3u88ni0b_OjjEDewCNg3jHFaz-0gPbMVZGLRYFd1_D9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=WpY3YrKvecZrZKxIMCzNY_Krk7F4zLLYnFaKmO3ZKXKSK2HEUn5KFgcycomGc-qJr3McSEUo_Phd3-_lzrz1RztjCKQXSJ3pFce2NaK6k7s0N3_JfNOZ6_tmBVCUQBwEOHN6AMbMc52gfg7PBxE6c64H3yi73g2jdbtfSZ5wA8vTuvrYK5aTlAwGQthEsj3waqi1kms50I3a2uLlLRi7LS0gu_9SPvcKIJAg2oRnlHhF5ymJEaCuKMMsIGCGlSeeR81TdNSPTKDwPvgzEVAlhMCYffoychARjgqWi2T5oF3u88ni0b_OjjEDewCNg3jHFaz-0gPbMVZGLRYFd1_D9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqfjw3Y-fAtDLMm0vC7UKB4pAM4JquRvUtd5KCk-wk-KrtedP1xttwXMc9agSrD0FtoGH9H487p9X8RzcDeAE8nJ797HXbU0fVjoa5RRObwqNIkkbssKnXRiIHcMt4oZBYXlJQadCHqb53EQKdnGdKz_kDor5LLfzRzIH-vlWKSYKI6gtr6B6nErrTFJbhcLVz2tTwD5o0M7byZIkVwkcbaIkVn5SaxIscXEnUMlvCFKyPmYlIKkACOnJqKX5U2VMIsTi6mkA6b088oJ-3jTi8I6TrJ0qFcpjnd4LPzmzMPvraTWLt2AIWhLfFaErSqZsz-OhMwYF_ApiT1Sefd4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=biuNWWQTszONzIGVRlX53fHODQxZqehXcVxAhiq4cPsSZRlvmqYzohUjIHOzk_JdnRUcwZlBAqcvHfGQV0ziBff0H656Ug4GcbCbl_eTV54CVeJRyEpUHGOBCDXy5Hb6P_rqi_7Cq3uC3tmqc0TQIjiBNeCyawt_92r7w6V4ZdqF-W2pr-5k780b8LOZlYQZYI5o-JGVpYHAiSShSKoLHlZIfcgRTD0elG9gJj0UY_Zh6gpe56OPyangJZYpVpZ_qyjvYjZw51VhFjd-Le0s22qnZwova_iRQMasZIeiK2XpbKd5zyOsfvgC7kIlqh4IQDfPI6Wl_J7kzubmIg_qTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=biuNWWQTszONzIGVRlX53fHODQxZqehXcVxAhiq4cPsSZRlvmqYzohUjIHOzk_JdnRUcwZlBAqcvHfGQV0ziBff0H656Ug4GcbCbl_eTV54CVeJRyEpUHGOBCDXy5Hb6P_rqi_7Cq3uC3tmqc0TQIjiBNeCyawt_92r7w6V4ZdqF-W2pr-5k780b8LOZlYQZYI5o-JGVpYHAiSShSKoLHlZIfcgRTD0elG9gJj0UY_Zh6gpe56OPyangJZYpVpZ_qyjvYjZw51VhFjd-Le0s22qnZwova_iRQMasZIeiK2XpbKd5zyOsfvgC7kIlqh4IQDfPI6Wl_J7kzubmIg_qTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=D6Gak5m0Vw_cDprRmwjXTGfb1OpkY6HyeB3QfOokAVz7Y_EvwC1TgQa3wUoAjh9lVIT0d7WEpRx_CC_3HVp15bK0-kdD6k5rhEixNBX_4tgoWbawZTFRJN07fo51DIGcTN3HoD_A3BSzZ0S5WRbR8NdKnJF4F6izU_CfczNCFHhGef9jRf083R15co-uKMQ4ETdkbB55lFBU2ZvTOV11Az_jRmXP4ScB7CT-r12A6JB184Eulrhdv0i6PYU_ANBYMRSm53gURZAF_K23hRCDQwUbvGityYjGufSy7bDO6zDGvYYBfJ3RA7qqOOnxGMYVVe1ml-MlMqYtOfmt3lNRHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=D6Gak5m0Vw_cDprRmwjXTGfb1OpkY6HyeB3QfOokAVz7Y_EvwC1TgQa3wUoAjh9lVIT0d7WEpRx_CC_3HVp15bK0-kdD6k5rhEixNBX_4tgoWbawZTFRJN07fo51DIGcTN3HoD_A3BSzZ0S5WRbR8NdKnJF4F6izU_CfczNCFHhGef9jRf083R15co-uKMQ4ETdkbB55lFBU2ZvTOV11Az_jRmXP4ScB7CT-r12A6JB184Eulrhdv0i6PYU_ANBYMRSm53gURZAF_K23hRCDQwUbvGityYjGufSy7bDO6zDGvYYBfJ3RA7qqOOnxGMYVVe1ml-MlMqYtOfmt3lNRHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=tvHGogEmTErBT316Tcghk6r2wfB_IMupIrJqIYgi2duij2ZY7HwvvgTOC4HwoUaY3Drx2hLmVzSBS-hcvD267OPmTSA1BEdl-hyXp4IsBh_coAI6Mfs2pRRSz44RMTLlaFnjFhwPlAX962ebUBlGQjizUUGaW2iwo9mV7seaZh9BjmOHDhnHbKdBmV37K9eqUkd3_K6BT0tAP175Mla0eTe41a7d1u0oXVm919LXIKs3WxypXTiN6BqcMP4JBAG042IFc3Wr3jJumh2r0wJw-4BZPomkLFysB-1aOwQYWtN9X-jSR0MNwq0dpPOuXe_MkLvl55U0E4OFaM4yMQPBLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=tvHGogEmTErBT316Tcghk6r2wfB_IMupIrJqIYgi2duij2ZY7HwvvgTOC4HwoUaY3Drx2hLmVzSBS-hcvD267OPmTSA1BEdl-hyXp4IsBh_coAI6Mfs2pRRSz44RMTLlaFnjFhwPlAX962ebUBlGQjizUUGaW2iwo9mV7seaZh9BjmOHDhnHbKdBmV37K9eqUkd3_K6BT0tAP175Mla0eTe41a7d1u0oXVm919LXIKs3WxypXTiN6BqcMP4JBAG042IFc3Wr3jJumh2r0wJw-4BZPomkLFysB-1aOwQYWtN9X-jSR0MNwq0dpPOuXe_MkLvl55U0E4OFaM4yMQPBLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=A-qci7WqBLw09YIw8OelRU1voyuxbiwRbdX2Un_gqepscydv9bBuocvZ_hEEQnIXl5J5BTdsfIWH89Uw-7eoB0baTJpXOR7xuW5xmbECQwcsnoAEe_croRaORvKCDBvVv3CPGMxFYeEYu_PixuUdEKJXr_CnkBLOAphPwdcjheNZmNJd1IAPnohH9DbhFa3LNjYZTUus09vYrzHEvKtAAmAf9pLfINF3rvNlUwydstUmiHIIOQ0LhwGJ-FTz9VMQYwpXmM3qLeOxT9LmnG3HwmkHzMlbtAjoop3u3tL2xEfTDGHeERq5Dl5-RcmOI_7b4_nMEeYbump7L1vwS9gqx0XJdfQdIJNB_zBZLjDpZODz3NGyv6Axc4GG2GzlNxLteiNyrwL_rarfgjUjzIjahMVTH6rxfmCv2lHuhpegsoPkgB3izdK2hZwzmD0y6nsiorgyYIYdbMB25gNG_Ww1xiBYdcJk8eUrWN8nTS0Mtxsk6XCbni-lcme4BwdE9wqCDHznHMKTEByUo3C1Xm-uirZK6LkavQCVWNzU77fYcbYvtrUrm7iKu9-wFBtGHuhe2SWIQOAKA9InbUOSH0PIKeTO-LQCU1lXLUnFZwUGOKSzfwoN51sS3RGHNR4Rt6zxB2adWhQNsmyssDFOorQCrRfuFOdiSmZH0VRjWnDMqO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=A-qci7WqBLw09YIw8OelRU1voyuxbiwRbdX2Un_gqepscydv9bBuocvZ_hEEQnIXl5J5BTdsfIWH89Uw-7eoB0baTJpXOR7xuW5xmbECQwcsnoAEe_croRaORvKCDBvVv3CPGMxFYeEYu_PixuUdEKJXr_CnkBLOAphPwdcjheNZmNJd1IAPnohH9DbhFa3LNjYZTUus09vYrzHEvKtAAmAf9pLfINF3rvNlUwydstUmiHIIOQ0LhwGJ-FTz9VMQYwpXmM3qLeOxT9LmnG3HwmkHzMlbtAjoop3u3tL2xEfTDGHeERq5Dl5-RcmOI_7b4_nMEeYbump7L1vwS9gqx0XJdfQdIJNB_zBZLjDpZODz3NGyv6Axc4GG2GzlNxLteiNyrwL_rarfgjUjzIjahMVTH6rxfmCv2lHuhpegsoPkgB3izdK2hZwzmD0y6nsiorgyYIYdbMB25gNG_Ww1xiBYdcJk8eUrWN8nTS0Mtxsk6XCbni-lcme4BwdE9wqCDHznHMKTEByUo3C1Xm-uirZK6LkavQCVWNzU77fYcbYvtrUrm7iKu9-wFBtGHuhe2SWIQOAKA9InbUOSH0PIKeTO-LQCU1lXLUnFZwUGOKSzfwoN51sS3RGHNR4Rt6zxB2adWhQNsmyssDFOorQCrRfuFOdiSmZH0VRjWnDMqO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=GBx0JVtQr88V9bcwePS50kqPiSVqMB4VjVp2xIr_YbW3HMEoJp3HDKdEfR-Q7wThC7Lh7Zk3IYLIErIJs3oWHdttBRaBBnElW2S-IDQY4PpYegBU_xPOYJqAZiBdKNHAWdC0PYadToa4oWAg2ifi3lv_gsn5MwKniOLnh0d_j-d3HSGj5qyK4iaobMzpLwrvdP-ObkmYS9cMWsxGkz6vX2FR83AIN_dS9NZ2Jph3JUeFDNutmTLfPOejGjrBGXs79f--Cpzg4ycDL-WpJV4lxb736Rx-YolYyGodKksEsILbl8Qy3lMaJPuQ3RuXjC8IPOPYc3GdAeThIgOqSQVSIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=GBx0JVtQr88V9bcwePS50kqPiSVqMB4VjVp2xIr_YbW3HMEoJp3HDKdEfR-Q7wThC7Lh7Zk3IYLIErIJs3oWHdttBRaBBnElW2S-IDQY4PpYegBU_xPOYJqAZiBdKNHAWdC0PYadToa4oWAg2ifi3lv_gsn5MwKniOLnh0d_j-d3HSGj5qyK4iaobMzpLwrvdP-ObkmYS9cMWsxGkz6vX2FR83AIN_dS9NZ2Jph3JUeFDNutmTLfPOejGjrBGXs79f--Cpzg4ycDL-WpJV4lxb736Rx-YolYyGodKksEsILbl8Qy3lMaJPuQ3RuXjC8IPOPYc3GdAeThIgOqSQVSIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=MQc07OLj47xXOh-CdbshmAfZAm1cq7CFKnPm1MuCiwIXNhbs6UHx4OTE-q4r5kzy0iydHNN6lcccYUwpbiZkEut6gzF2M5-7SH0ssda_taqPUJ3Rg0z9P_ccxnW49ZUsgPmny_YYotB0SYHvaGzdxABGxbgGEfbsuJNrNTMsDb3ABwpk7JNmS-VhJjG5DXDzpoJ_CL0ex-_VXnSJLyUuTIXCEr8lvo31I7nRbKUMyKOGlmphb3gvQxKrCKoQcwd6f_YIkxbUMPb_bhhkVxo6oIN6-5DzU-vwooqAcn2UDAEP82Yj1n6Kc0yJh2h3khMjPXnHCR2YXot2ej8bIIAQHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=MQc07OLj47xXOh-CdbshmAfZAm1cq7CFKnPm1MuCiwIXNhbs6UHx4OTE-q4r5kzy0iydHNN6lcccYUwpbiZkEut6gzF2M5-7SH0ssda_taqPUJ3Rg0z9P_ccxnW49ZUsgPmny_YYotB0SYHvaGzdxABGxbgGEfbsuJNrNTMsDb3ABwpk7JNmS-VhJjG5DXDzpoJ_CL0ex-_VXnSJLyUuTIXCEr8lvo31I7nRbKUMyKOGlmphb3gvQxKrCKoQcwd6f_YIkxbUMPb_bhhkVxo6oIN6-5DzU-vwooqAcn2UDAEP82Yj1n6Kc0yJh2h3khMjPXnHCR2YXot2ej8bIIAQHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqKxAgq6i5cQmJm6wCQ_FE2YsYpCZe-H1x1v9adOtalA5vfxkULemAvkAGZaKusFFyHdUBi_ODDL5r3eYgHCtd1WjsA1_isUmOR5ajgDrCWEw3mtJTJPkTVsf_ihY323fpKBW-lCOJaIvESGY8U_l22okgRhNt16lZFg58o_IcJnhhxweBpUbMVMb-M91HHQT2ox2ZWB0ylFBCTWlZj8NP8pKh1U52pjSF9Uj4o23CJvG6VGO_qkJrVoh28y0Eftf3PxhwZdE3NvAyxBT-zBAxwpUscLNBBl8PCpO0mbZAfw7eIxIX2m9ADfRwpYoVIG2T48T8YRqWzI1OKWRK_z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDxg_vqhTj5--IOg6MtFHkpmdIpjfk3nkHIV_EmhBiEkODP_5l_ahXNB0kC_S7tH62KK9aKSFoLf2p09IFHn6kJWoVekkPxigvAjpeXMqFub-P2l_tkOBy1IVDaXn2xs8zQ8koUXg32ErWlE-ql-gtYsTPc8qBzQLOI-RdOJGMJwlr1vrEOFZT-3sbShVtW12u3gBOHVeo0IbYEEdSyGL3zWcIWD8yQZ2ccwB3kD7h-2BCASezLAsDFQ5SOwzzSEzMynyzP9Sejk-lFF2K65V2CAWIpiNlH90TM2E_UciDLNf2CZLzlaYwLEWV1yd2yLr1izdMvjgxJQzwanfgxw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=uC0TbuAdt_SOJikJUlhgJrPPxUqQIggl9CAa3W8k3UhXm3y8lIRd3ms4JJygQZrukRhEAHBUK4jiicVUIkY5CwMUKKi2Yw1N20wegR6om1bcRshZHdBDlvaBezXzUUhz_CRkhbHckN2iUtDDbihfcun0VRUPMDFhTUvm8MoSGsGuG7OEWVtLy4IGELXnwizWq8Jde_3RUZAF43VgBvtzlklNUfhmUctC0n3gPUeGREDl7rEIvZz2DveAPNBUS3VACUrKYOoK8cEWPfPso-e9l1UMl800leDKdX-9SP_3lhIo7PkjIxsCSvv1Kanps9qdDNWXm71BKRz6gJe7pwdAkTZYk7OxpINIfrVhDWLweLdZj8CJyB2JrLZ1yKLTkXCDuwF3ehIK-SwRlwrm9AjHdHTyvJKkuHHy4eDPmieB2ZjeME-YgQcdfwfscZFf0_aMwt5kj8oUk6nmWRH7jesEyRlruPpmzJcJ-9ELWbOvXpt0y_NsYfRW7z0pB7xjimAjNRm0T-pS6sIuLnkpV5burujfjGJ2HN8k5BGbAQfGO78TF6n6vORZdgLG7i9U59dKbPBZcQ9o9B7rlbi4iH7Z2MhwLYpS90FAG79W2wOx4BQ1PmRVE6nkgFCoIzt-nUJ9CKhVd0W4zfjUpLNvethoOIH4opNXAbngBZtcFSMpNM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=uC0TbuAdt_SOJikJUlhgJrPPxUqQIggl9CAa3W8k3UhXm3y8lIRd3ms4JJygQZrukRhEAHBUK4jiicVUIkY5CwMUKKi2Yw1N20wegR6om1bcRshZHdBDlvaBezXzUUhz_CRkhbHckN2iUtDDbihfcun0VRUPMDFhTUvm8MoSGsGuG7OEWVtLy4IGELXnwizWq8Jde_3RUZAF43VgBvtzlklNUfhmUctC0n3gPUeGREDl7rEIvZz2DveAPNBUS3VACUrKYOoK8cEWPfPso-e9l1UMl800leDKdX-9SP_3lhIo7PkjIxsCSvv1Kanps9qdDNWXm71BKRz6gJe7pwdAkTZYk7OxpINIfrVhDWLweLdZj8CJyB2JrLZ1yKLTkXCDuwF3ehIK-SwRlwrm9AjHdHTyvJKkuHHy4eDPmieB2ZjeME-YgQcdfwfscZFf0_aMwt5kj8oUk6nmWRH7jesEyRlruPpmzJcJ-9ELWbOvXpt0y_NsYfRW7z0pB7xjimAjNRm0T-pS6sIuLnkpV5burujfjGJ2HN8k5BGbAQfGO78TF6n6vORZdgLG7i9U59dKbPBZcQ9o9B7rlbi4iH7Z2MhwLYpS90FAG79W2wOx4BQ1PmRVE6nkgFCoIzt-nUJ9CKhVd0W4zfjUpLNvethoOIH4opNXAbngBZtcFSMpNM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi-615VeZeqAD7ibhY_5F75M5-KEQcRzbaoTqxEDeVkUnHm30Xed2mQpJfxG1qciSzrDO8Z5-J_0mvSbzIw9zs6_Lx1eULJceLKfEwxoioh2-iTVmk0y44_VARXfyTUF3lrgl8PcpvSbxdvZajAwooDvl_C6zlOAUCXTidItt9heMeWzkvFq7kTfTA6A_t5adGFSVJyLpU9bFna9dtDFpKL9TYuhoNIx6WEPTS32Tap4ST1XhqkCdFcr6o7wS_zrBEV3B8XPy_vVt_JdfPMdw-Y_YaKvB__fclAdKN9ybdF4FGKEdMzkxS4n68Ss_zkBVafcyqyJq6XiMLoecZFOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpTLfa2O5bN6UYQi7bCFURknfIvrEuU4ilp_tHmmHiikMbUiyuwkojrSQ0soEkkgPgtDBq_mJa27uT-VIlRTR4AszNXZwXbD-JFZpu58tE4TB7tHxGqihql_N6DNsU_9kDaVC2uhRXgG9je82oCXGEs7qQMWjbm6ZoCzG2beE00E0eExtDpiCmiuA3ggcef5P1NdmWgAU_GTw1aIQg7NoLIFxzLUO2Z9yoj3oLGocf20uv8cApRlTsAIJxGI-N0_qr5HA6fbmbwpXtGSUOCFxm2e676zbIOEyORjL3eVSwhUw0x7gcN17NkKYIB2ZnjeMlTzwqArnHI-Om_ESqjr3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWvSDhoDOzTXc7MuO1y_CSI-46ZMsV4i6LONuy7Cr3yFf8VQAmYTn3NkPNp37Bcn1bsT4W3J1OOQpiuLYLcUt3aBwOiduWoVSmyMY-rofq_--Lg1ExmCFnrt20BBrrqZei9ay30uC5TsvxPa7RNKtS2Ly07XUX79Szy-xZhwIy43Q_DqJmF4PvtTjFYaH-rV2oPKmtvoOhmZ9wbr4PKrDf0b1EELja7TCxb1ugmsrPZ7M_r5AklYrOJYGPiTUmKVD8jXpKaLD5nPk6-hy7Y_Wu-UdgHFFmysvofmt3bqZKHfbDdXVJz46Vz7rykkxg1tAXVyl210X4YRD1Jljj5mBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An3adMhAvzpCkEv4y0f5sPD2ql75oRxgCZaGgGfihhz7oF6BHIleCVz4etQTkD5uBWD0lTzz-KCM2RrsI9PaP2zTdt_Olf0vPXgZsF8fHGNIWz9_i0f0iTrpZhpxLM59MA41u9noJRYxcRI1G_wRSJx96hyt53X-M2zVzqL5Hi0S-1DHD6tiw00BvlJ7FDoclYk6Y5WMJ-euYfdcIGCX_y-AxgU-LxeRu1dBAKIVc15iR6cDyyY8yUCu10sQiGnRivs_1_ztM6Fpimp5ZF3MFTIrDQalNqsrOV9TIqa04Su66kePv2-7_GO_TwEc3NIWYiQUJmRwO4Oo1Vk80AA5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=DaktVo05c3R1X2hvY-wZaoEFvjeHoHGCtsPMeRTm4Xxp5lxn-hV3h3kr04Uel35OQxeWXPxe1fDOKDmJ8NcP5Dt-klo4MTSAI9mz8_xGYiMg7mNc65oeUKaTRIKriIezvvaTFHuyoahMn--3jSt0bW0B8m8iDCp1Pa_aavh7D7jKPRKobqSVwXtcn55iYrL8uyha83WBl4uNUqW40qBzUhA3iV8ZtcMNByCWRhmZxkvFljTeXMOpt49noxF96jEsm-nKxK5E_yHVI-BTdBrF_jODMUY0pLHVNeu5jK1lTiGO-YxqwZGkBDAib6bI8dy5P0GW7CEIZz9dAsiuQNwTKFMne6hecdMLOGW6dodIJaNJekBVyDocfI0eSDdTwBcwV_3B_7AAbsqPubQrr9T-_DwUPPI9LSw5f3ThFUV4a2wwwi9Nbe-WG5FiKiaZhwFlcjSeknVD_JbQOOdWb4TArWpMxZwCfj5mcK1p1hn8_fuSuCr04ZxWKM3sLCYm4xNzw6x3mNhkVsevesaexw3z6TD4CkExtmyq9n_yck_h8w4cMKBmz0O_P7Nv1wN2ZUtSQnw_aodwhFPxUxoO01YWZmN-Mmj8znjilRUlrjW4CSY65dUFYeTCoLoijUcXiUMNDfsRo14DOHajB4f-W9hZFVq6XLQ7EEtdj4enmAo1mXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=DaktVo05c3R1X2hvY-wZaoEFvjeHoHGCtsPMeRTm4Xxp5lxn-hV3h3kr04Uel35OQxeWXPxe1fDOKDmJ8NcP5Dt-klo4MTSAI9mz8_xGYiMg7mNc65oeUKaTRIKriIezvvaTFHuyoahMn--3jSt0bW0B8m8iDCp1Pa_aavh7D7jKPRKobqSVwXtcn55iYrL8uyha83WBl4uNUqW40qBzUhA3iV8ZtcMNByCWRhmZxkvFljTeXMOpt49noxF96jEsm-nKxK5E_yHVI-BTdBrF_jODMUY0pLHVNeu5jK1lTiGO-YxqwZGkBDAib6bI8dy5P0GW7CEIZz9dAsiuQNwTKFMne6hecdMLOGW6dodIJaNJekBVyDocfI0eSDdTwBcwV_3B_7AAbsqPubQrr9T-_DwUPPI9LSw5f3ThFUV4a2wwwi9Nbe-WG5FiKiaZhwFlcjSeknVD_JbQOOdWb4TArWpMxZwCfj5mcK1p1hn8_fuSuCr04ZxWKM3sLCYm4xNzw6x3mNhkVsevesaexw3z6TD4CkExtmyq9n_yck_h8w4cMKBmz0O_P7Nv1wN2ZUtSQnw_aodwhFPxUxoO01YWZmN-Mmj8znjilRUlrjW4CSY65dUFYeTCoLoijUcXiUMNDfsRo14DOHajB4f-W9hZFVq6XLQ7EEtdj4enmAo1mXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=TYHOIBdGoyJ2_U69jtHFQ290vYA07kNBMvavXd6z3_v9wI1Ti_n43vGY4hNA73w18AwiDgP97UXfCxXMbLUSzCnLhb1nFVWidyfRXAYJFTunaLdQ-u2vRlhHxQy4GLpZXiuRlKkw1ls_Y7LldwzIzrFGbKeAHSmN4-S6hzq6vgs7UJXfuubVA159HueFjPv2uDXMN-n7BcAlqNNK-jWuFBq6NGw2asDnqPKCH0hn2czwNMKa60E--_rbRM29xmW_bQFGQWOCdNtuasXpFlYtXn9qIUOsHmyB816wbN_9FU6ZUpRMfjfiPPD8uF91tiDFhc4KlFzAQ0ZBvWoFk0SF8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=TYHOIBdGoyJ2_U69jtHFQ290vYA07kNBMvavXd6z3_v9wI1Ti_n43vGY4hNA73w18AwiDgP97UXfCxXMbLUSzCnLhb1nFVWidyfRXAYJFTunaLdQ-u2vRlhHxQy4GLpZXiuRlKkw1ls_Y7LldwzIzrFGbKeAHSmN4-S6hzq6vgs7UJXfuubVA159HueFjPv2uDXMN-n7BcAlqNNK-jWuFBq6NGw2asDnqPKCH0hn2czwNMKa60E--_rbRM29xmW_bQFGQWOCdNtuasXpFlYtXn9qIUOsHmyB816wbN_9FU6ZUpRMfjfiPPD8uF91tiDFhc4KlFzAQ0ZBvWoFk0SF8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHHeDG46jvG1ljsfgaDQm3_ttuh24H1ekKrdSEPH406CwIByPQ3KBgeRqLJLlue6Ja-KUGXak78BzHHCnTbY5rl_krfPCYemE5EpHc7-htoI-b11QDG7Gxz4rz6O78LgNZoUF51Ff03C3CPcpyO51JyEAVRfLIsvLEVEpdLXJR0Dp1xjYmscLEtRo194CIGcrjS2XXDHbCFqWeUz19HPF1VGG229sIE5plKPvdsW2I6YXc11KTOqxaKXwJEGOESXyUbp0RqlKtlW9LcwrvK68V0miFU-2dmXqqoJ0FvipSrzscuq0yXedSzo9UhlHeH80M9wj-Gd2qPyyL5j16go-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5xnPOfWheagLmeIUk9ytIdZ68d8hRoWwWLy1Jt99NZYocLrRbpd2wzEVuVnBzEqVhxYGaBvCZNAZQRShjw5pXPT-jCtHx2MlouA46MJVHV2haGoGcAgFb3ty25MpgwaZ5HKMVf_sn62quyvHuWVuq_16jxtmjo2yc3ZKNilcJM0zq4CFYXEH-oiWImKD2NSUka-3MbTxhBCLmS17ibpPGhocvQN5SALAYsf3-zVWx_j8Cg3HbPKsbUq4WWZkdwvQ7Aa87jPB54bXdLkZsB8pl5JODxAwAzeqb7474AYpy2nr1cRwvwtkUYs3yKVaxSW5z4qCjKrgLGppv8qjgG1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijL5HKJGHeVoiwqyVyYBu5phwYCBfEKK9ZsNYGes0k27qftGiRKrWz7fBrn8dC6MB-sxrs36a35RRzt3JJQvhVpJ91IlMK6tE6qARPSmooezP1upYi0sdLzknhluONV_8SYjs8-jt2EDU_w5r3NO4j5Yw5_k-BojccQqDT7jUqtB4XRYV2GGSwxuAxXIrmot475UVJFri8mY9heDrSMphNnFqPcwJ2SHDc6nxBnYTRl0D8dug1MZzCVGMBXPUHhem0dhrzumoS3nNAvQXNWVlWCZqHeJX5ZKYszQa3Y-keZMWmRuQiFYSrDVSXAF_Ykrbl-PIaJ18A-Lfh_Dji7MWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9lJQs5Zz0J91D7PHXqGQFfM95Lpobv6VW6uNpVXiK9537XlO4QaR8FzpKQ24pFwRhZLX69GDIUjKjgr5qDVDWDLNQ5eD7GS21Kk8EsAmxAv1tLvFPb9bu7A1H5EouGHjgSMm0_eUFQ4v3xi7piBBY_o2rucO8mxL4KxzyAoGRVpT_WvyfVbQ5cnSGerKURGuP6l2N7-IF6Jx0mhM8jJPossBTJckBdfVrnVXCF01lXfigI2kEmAiZKcyxHPcScEnE34bmE0q_4YF1QdbfEP8KlMGjlt6bjrlLmsSBGzSPwIpKo7TKUnYaP9swY9uLJR2Dap2UnNx6-L7plVGcE5Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rpb745una1N9u1yjtjXzQUxSCF0NeewCiUmk0f-bzyL3txZh4u_RR1NJaKUQr7u3_p06_ilhaXeDeEJw6Z6n31wKWT_4T_QSSY290BJADEVo7V9eb79p1zmEojcv2T0I0QcnVWXRjw3kithBHIQvIGvVZTvF_9DGqUv61WDvgHZedB6-U3lvsy9fovBdzykguqyIjRMFvS0eMPo61lpn4OOD2S3jb3f7sLKWp69V6P_b_pAW5KqUgttumDzxbCwYS72gDipu2n4qs_EeJFnGQBHfCkA3YwA60gnUf2Rei-k8h2WBvFUbJXA1dnnfp7IrDs1sNYjKWXNpZU1sRO7zfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFzxneZ-X1Ui8cmphRAvtpE2uEoWdaMn-OnXftUGDqD_Z-BIxOK45PZHn9y2VMPe0qu76EkpG0qKAR9dECpS1JWQ6JGPjcnNepf5nLGgDc8PoH6LYEq1z6-qPjCkwVM2_GETfMryIyf5cm3vhvbLTUgq9sk_4ji-GhY7DPgxBmKaXG47_P_u_9v7aaW2taIG1fV4OVUdl53_YkWxdW_GpMt2Befzm-GmyaItMnlK8guu2DYUCx1TaLNDXksUV8Pa1KAzDR819WdKFLogRAdjqmxkPtZggVqUxAXQ9uxQEKWApz3EKF2FI3M3Frh9S1zvT9b5HHlKIYRdBWDKr4aGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb3qKWETKeqKZdb7USKYH9dJbXCKcMdJ3G5l-VfQgBBmIRB1PM0-UKNEtKMqcLPnClWEVIfA5WXWO2uaNP6gdDzFX-NH9mZxVNP1Z8-2nswwiMd5vTU7fgKwTP0cKi8J6epu6fFK26mjJ9RV3xH01Gm7-p1VB2DFxiCn5yqRQL7JQ5xllGWBrcLwkrsvCnjMJGitsHA8JTCKNieU0Fgr6UkNma31yL57AASE33QAY7RDEY2W4td4DI3CcIKnq_yN7Iona8bqH7-bZ1ZcnxgAQcHoktkRS8CuR6b1R5mK96KOoFx2gxymjvEnbUeJpPHN6cxpISTFieYPB7edIVx_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=fPKYTMf3Ft6C-Bbc4VWYZv8CBChoDqEEmDOBNYldXnuLNfpF0l4NgWPjK7ASoe26M0TtU-0YbNqMmszIaZcMVWmnFd8K1qv3rIxlVcXPftJEUyNj64RLvtrJM8_mwuXn17WZTwEJt_JC1rRUFUMpiK4FEHxuvlrGr99wuZMFP0zCBNt_LZbZcRxsh-e8BBb5kZeCyvGvq9TLiSiaBM2JWiYZzOpCYBf6w8hetsUfYwQ3_rYpnQCF6GNjMplDuJMPF1HC2axSItOsWmyyWqRXCmBX-LNSAm2y0aBWlSbfYsAd0Wa-DyBDFxDPy1CMZMaTO6vD_jO5KKlfDHgV3qJVhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=fPKYTMf3Ft6C-Bbc4VWYZv8CBChoDqEEmDOBNYldXnuLNfpF0l4NgWPjK7ASoe26M0TtU-0YbNqMmszIaZcMVWmnFd8K1qv3rIxlVcXPftJEUyNj64RLvtrJM8_mwuXn17WZTwEJt_JC1rRUFUMpiK4FEHxuvlrGr99wuZMFP0zCBNt_LZbZcRxsh-e8BBb5kZeCyvGvq9TLiSiaBM2JWiYZzOpCYBf6w8hetsUfYwQ3_rYpnQCF6GNjMplDuJMPF1HC2axSItOsWmyyWqRXCmBX-LNSAm2y0aBWlSbfYsAd0Wa-DyBDFxDPy1CMZMaTO6vD_jO5KKlfDHgV3qJVhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw4uVtu5sG6gr5VTdl5CbZKajfLKq2wRQG0HYame3SPbr07MKTXfPLL9J20fq2m6UCmtEA_JFAnGMaJpnjZGactiEjVoHHwJnZ_4Tef4hErAsKrRx1Wmes48syLcEG6-awElgPXpLA6_c-wT_EqdnEP_UaYMHpZ7zRIooj9HONTT9ZBpHl9fR_u-kRuKeURjmtvXq0yy9dTDSFt37X48BDFZ4ndO_ip5ZksNih0GOfq8U-xcAnN2u3ke5_KY7CeSl5vUkkfFwyPs6Vf1C7FalrsZKg-P_5cKuGhWQncolinocCheZhvb8Ku_wqW7ixurasYjzUVxpElJWcU5UyyzCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
