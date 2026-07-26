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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 13:21:19</div>
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
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=kH5vKw1OCBuOkkyBl4XvvI_S_xTMHcZC-CGCsGOyi6MjbD-_FIAu-vrH5Wc74c7YYU8dZQMWpUs5dM9A-licfrgNm_A3SiLyf0K-rnjY0VtykVW8ZxIMF2BS-03xtsO4ObhxWA2G_RsbfMDazdRI5LLXT-s6f0vMBeo_qYtjPhORkFqnKqBSb50xc4knpfj2UTsYDhJWVEQxPa5sGsPZy1a4qBLZrer5Om6buA-p3Ovdh2U_g06NxEC4x3CBIXvdJe1621xVlBWqIKD8WCtdRle2iIRslPEzd_MlND6Yk95gcPMXIVBz2uVNX7upXf1m5VaMIVGWnDakbl1sHjUYTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=kH5vKw1OCBuOkkyBl4XvvI_S_xTMHcZC-CGCsGOyi6MjbD-_FIAu-vrH5Wc74c7YYU8dZQMWpUs5dM9A-licfrgNm_A3SiLyf0K-rnjY0VtykVW8ZxIMF2BS-03xtsO4ObhxWA2G_RsbfMDazdRI5LLXT-s6f0vMBeo_qYtjPhORkFqnKqBSb50xc4knpfj2UTsYDhJWVEQxPa5sGsPZy1a4qBLZrer5Om6buA-p3Ovdh2U_g06NxEC4x3CBIXvdJe1621xVlBWqIKD8WCtdRle2iIRslPEzd_MlND6Yk95gcPMXIVBz2uVNX7upXf1m5VaMIVGWnDakbl1sHjUYTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWTwy7qFQ2leTVpbUv0pOGtqMnDhsmyLo4z-o-7nBI2Z9F-kTUxcrkDAT5LqcUt552dWvAEuWPEpjjnmmQXYZbj6mfmjnjmLYNLWSqh7t_nZiOrsD4hbTQOJ3bPFLJOFM4rY3aS03vNsSYxBaPY98YeUarOaw5NYg--fxUelxAu6kTC0VqWTmUs5mx6BMIScMXFqhTYuPA0aZeumcBVXiLhD_TRtTPrn2kv9ji9Id8Zw7LmmRqigFMptRZ1imxhuFRpwcq4cDbVXFeeDgRFabmVzuiMwHPHiKXCXGuf_jr8lhUkRNi-yVFxHjvTrbzGru2gea75qwjg1ZN8aGho74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmoQU1SJHWKFiRuqWWrJ5VflWt5s5N_bn2cxU9wmKke8h4iTyDG66E4n8tQ339OA1-Q3gHeGPf_PoppA9Rq8mX8X11AHr0LNbcGeTPmYZ_hhyAQIv7g1K15wjI1NxhCn2I17giK_4fEQN6QcrHG7MOPp0jO3f1kAgGKdY20bTHhHqwZmww4_QCNN5XyBpFJpexLcj0kQ1wmAwnJCmGd334OVgGNc2P-Sa_pkmC8q_9NqZKkH96WfURaL118iDNOpHlilGiApauT0NDhhVcL9-ZyLwoSMeZZTn9Wtgx1O5wJNgI3RFyHtThajKSpeU1r9EJ1YoMNxFB28_fL1JkHsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMm_ESU-hX2-8muoQSdzXE_BM4NLEtcn5J7l0m8TdQcx2vkrotM2d1UQIKqF4jF0jExUa07Mh7uCHsUifRB_4a-jgzjPkW8lhcjRTf0yW93aZ2CS0u1DWAfniKXkWiNMIcx_wy3qONuzKNkNeDlimLYsq62QWADVyNtcFqwW5C2SRZOt-O5aZ0FsKNcP-n54YlavS9Sm-sH_xh1G8BxWiVWCZYquEPGjIT99eFkH9Hock734ZczLuRLgWBOPtQ6hRnkZtMgY5EuNecQRI0NpBMzBaRIOrljn6VqsaOvdDmQKpF47Zw8nXGllxmdADVzB9WBvfEUGZPxehtHw0yDfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiWNIn9AjZs81MmjIvrcD9sGrtXBm50rUG-_C4IfxpIVO1uu23zeWLIfbq2TwWWoxFpD88t-B0iR3xT3bzSwqkzuU39DZiX1FUSgqJf1LiaSmAJs3nWTIwET0HAaKTGwcr5Dhx9BubL3uMBRq3ki6fE0rcRQIv7bS5sGzyrXtaEed-nC_n2unAA5d7ztsxu2MN7hUK98RyJ_uksgWzMcvYdgL2c5NgKWcvcUg4M6YUOHOZxZZl2QikX19JMY0kEJIFV0j9ciP797oFNzjHD84Pf1VrzbPP-tYlbB8aKzieOw-S5PS0dIsUcYgRvUYQUEC23L6qif0vILT-s7yJcDwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P75mYis3bDtCCT2Wdg_Yp9kbFsD5tZqizbcAp6X51GUz8CH9iD2vgU8jjuSNId6ftTzDJFdu0grH7ZsQsTudx1C7cH8C9VQCo-d1Np7Rdf5_Ds1b9m-e3kSLG6_2ssS8UxKv26xR9GxqZKAm61Eia40IVPjONPjjIZR0CQ9N7jG5TmiIQZq6VEquW1-sq5iTI4gv9MnedrCUDxyW4eK8_mZFKzjiNQoTSfnZ4Wm6ydpnFzib2VZXmX69ZRxCkD0N0oOBAAjtC4KR_94p4N6jAN1gHXNg-P8-fVs8DTGpW5XCvYOOcF-FcJtJoQnlM6Dcj-CVLUxGkN-C5yKIbVHh4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=S07THBB9ArIHkAlH5Hqz6mLn0G8cIUjUsnOSWK9cenKEj--E59Qc71T2Iv-Do_3zPIOXnSigFPsIFATVtGi82WjFYT2vwMUKRgBc4-0Pk8dYaAJiMRmqkarI8-rels2hJOkT4DUzMs-LVBUoooBxBUCqcUiNWCqLMKzaHNBMFtBhgX1wO2CSdUwgk6BNeNFE7ajOXAlaKo2F7ycdMC1uTxKRssO2Dx7DP_vBOCiIMBj35_bKBPN123uA917TScOJy8RLY9hnZ0rfYInGFjVbNsJAIssnwBkJuD3QIfQv1StRMRS-nkI_jTT1zRA5eyOIhUURn085-xo2SWI0sa4leahiPkyN3abUhXDfDmv8kxSJjQeFL-apIgnY3XGbNHaTPAl-GjgP8upB65cZ6mRo_1fAbaydm7_VL0E0N-q2wG9DPKJcvYDzHjzLrQeAvOwsqKawYkwR_TKwhx1Aekyvm0DFR8TClN5H78mNNxWc6xEGRO1ozFsYeTgB2poBJ9k3HoHTFHnvCX0beyuhCvIrn44L_hoY1JcLAQLMFOOkyz4QKn-sZ1YMUSmPUT52d5nnXKBdMKNOiypC8dxR_-lIRcCmtDHo_idhfqPpXpN2RUONdLOPspIYbHzP5Oa6GUfCrIdoFQtiMKomNocAGi9vd9iyKdvBoHL-6NxQ2TheP5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=S07THBB9ArIHkAlH5Hqz6mLn0G8cIUjUsnOSWK9cenKEj--E59Qc71T2Iv-Do_3zPIOXnSigFPsIFATVtGi82WjFYT2vwMUKRgBc4-0Pk8dYaAJiMRmqkarI8-rels2hJOkT4DUzMs-LVBUoooBxBUCqcUiNWCqLMKzaHNBMFtBhgX1wO2CSdUwgk6BNeNFE7ajOXAlaKo2F7ycdMC1uTxKRssO2Dx7DP_vBOCiIMBj35_bKBPN123uA917TScOJy8RLY9hnZ0rfYInGFjVbNsJAIssnwBkJuD3QIfQv1StRMRS-nkI_jTT1zRA5eyOIhUURn085-xo2SWI0sa4leahiPkyN3abUhXDfDmv8kxSJjQeFL-apIgnY3XGbNHaTPAl-GjgP8upB65cZ6mRo_1fAbaydm7_VL0E0N-q2wG9DPKJcvYDzHjzLrQeAvOwsqKawYkwR_TKwhx1Aekyvm0DFR8TClN5H78mNNxWc6xEGRO1ozFsYeTgB2poBJ9k3HoHTFHnvCX0beyuhCvIrn44L_hoY1JcLAQLMFOOkyz4QKn-sZ1YMUSmPUT52d5nnXKBdMKNOiypC8dxR_-lIRcCmtDHo_idhfqPpXpN2RUONdLOPspIYbHzP5Oa6GUfCrIdoFQtiMKomNocAGi9vd9iyKdvBoHL-6NxQ2TheP5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=LfMOlWokXqnVjfmrJzVwSabp5bqo6PhYnznPLWut7bbxj5ej1Jtmtxwl5icK0aZHy9FsVYc0SjFdoa7NAvRFzXDUwh4T-0B3ioLXwH6JZqYH7uAznjCwZVK00A-BdapChINbN03fn3fxcIx9SEDGQAWPMgoO_dSFLSOu_iMNlYIo5YakNLKNXOGn8Fm60u_dLA-_Zrnl99WRGLiZkBZ6zKtwHN9VnEY71-RNsrAQSw37vU81kNfnnrSO-CKHGr9DA6IjUQtq2CbWYH7V2pCOhq1x7AiGmUtABC9HXFhmlTpSD6hnZZBiryN9Sz8NAjQVlvn3zwLoVHqBttAqSDJzow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=LfMOlWokXqnVjfmrJzVwSabp5bqo6PhYnznPLWut7bbxj5ej1Jtmtxwl5icK0aZHy9FsVYc0SjFdoa7NAvRFzXDUwh4T-0B3ioLXwH6JZqYH7uAznjCwZVK00A-BdapChINbN03fn3fxcIx9SEDGQAWPMgoO_dSFLSOu_iMNlYIo5YakNLKNXOGn8Fm60u_dLA-_Zrnl99WRGLiZkBZ6zKtwHN9VnEY71-RNsrAQSw37vU81kNfnnrSO-CKHGr9DA6IjUQtq2CbWYH7V2pCOhq1x7AiGmUtABC9HXFhmlTpSD6hnZZBiryN9Sz8NAjQVlvn3zwLoVHqBttAqSDJzow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4qlhYfLPQpf045cfddYYHB8VpBc3f3dFFWkeyQjnFKNSJOmJvgrw7n_bHDNu7DzyEA5pJmSvyXkABUMd6F2aEwVvfo_S2RAjsYR8VXVe_qhi9ouUxcKAl9Ok4g9WGmlhPhunFYPkdMDkJQe3B47qejpkytRLsOoz3b3e8kpkf9BvwKIsdXRg3Y2XFm56B4dDXGFCkkBaHfilk_irgNmfpnhSYuY2rNbe0V_ps6fom3xFfNrQVQrHHdy1LwEaZKOqlAQn5alQOtv3thZjOzQjq0cMpoK2WbedXz3W6TFZ1_JjV8lNEfbOELJ-7PbXKrg6y6Gg-9F-SaBZ_pGbJzZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tgkWOCugrXW7cSu-pYDyWc-GGbr_0ChTokRttTWkALmAV2FquXgVE2SjJJeUYIFFOkFN3RqWphQbV7Vx1imgfO4R2Usn8KRdyJg6LTyKE6qrZuUnLNc7vlLH7hEO-cNcR6rS-ua0I4R0vMD3pb-zV7JqJ8tlTirgDn-LlgvmOkYy9R3EcVN5RKiDTKBTe_rvh_eHM_lQsFucaIV4GZwvfbiyLU9NjKAjHxdoHa-LH-wtpYM7i0nv5NWkc5mpp0D_bnqPjHRtaAG_uO31U9RZijz0wIY8CQQUNMz3Kr39exnIJSXPUjOQdr9l_eBUVAWhXiC4RlASIgiROtvjkLfXJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tgkWOCugrXW7cSu-pYDyWc-GGbr_0ChTokRttTWkALmAV2FquXgVE2SjJJeUYIFFOkFN3RqWphQbV7Vx1imgfO4R2Usn8KRdyJg6LTyKE6qrZuUnLNc7vlLH7hEO-cNcR6rS-ua0I4R0vMD3pb-zV7JqJ8tlTirgDn-LlgvmOkYy9R3EcVN5RKiDTKBTe_rvh_eHM_lQsFucaIV4GZwvfbiyLU9NjKAjHxdoHa-LH-wtpYM7i0nv5NWkc5mpp0D_bnqPjHRtaAG_uO31U9RZijz0wIY8CQQUNMz3Kr39exnIJSXPUjOQdr9l_eBUVAWhXiC4RlASIgiROtvjkLfXJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvFAJ4eJXZ40DfNUzjFlwfdnRLnf0onSNdvmJIGf5Y4QFjmDPwTHg68Qc1LeLkXH5xsyoWvN0isYqmOt3iLrIqDxT2ZQhUyzCJhJwenQBCLWVbH97gaxTYqX4UzbGI9ALYSLnCGPJeUpFhRZEjMKqnayUTB2k1ndX6NNvhgFK3gE1674EMBgWb54iz9GI3Lp9jQ1Vzob8fzMKnarT3MaDa4LUrV97l6PTxD_LnazexjZ0_Rpg9VTidbYvG2ElSX5DRgvA127qB4XQbwJtLTsWfufLldZUHyCT1UdXSbJbb4HpIR_XHFmBLinrLVEfCnnPw6caxHZw4DoXtL6SW0VPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0sE-t8sTIFGp6lkf0AYABE8nfsE7F8MnxOb6sgeS7r9qEb716k2vw7Q9X4nd1UDnhSqBjILJaILlWTYbid9-XYK6XQQSVijoDWxNx42_3yGN5dOeO_kdD9-uJnOD4MGHcRBBzAOPu6U3wGfI_uVLAC3hqUsKWmIcveaT9iP_Yz-PBGRbm9rCwDr11W-Fo-FSjZ65Oc4OvBoFTN3kdOfXIK7M-s21mqYfFhGlyNK4Ykol97AgY54wqnRpjuNEDIMgfZatszarxPi6gEIgCu4wpub7IfYRi-qG70R1RA2Ynz2f_SuswydxxiyKyOxb15GE8aJrNOQT3Em9IbTuRwPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8bR_xk3vgaDwcQFYYuhgMm41im-QKnDMuXCl2v8p8S86DEpYAVHpVQt0dW7MwXjDcOEdydcW39BYgNXr6_NaUynttyNZ3_GFZ1aKk-qBPpZR33C1F64QXxvYCeFI3xxltsSuOjcrsnZSmq3AoGWliGBoIxIeBiWL7zeNXFWFPikLsCS7dEE6ZSI6ww6cQ1ygtf4nEbe-gb6pwp29MJ70XRhNp-LPx-ufTmCJSBoF8KjrOz9M-tpCwhGg8olkpGCZ7C3KZAt3-FRRJY1j6bNYBXHStlW-CLmnTe5TJF5Qj8T0a8PGdZgkE6wtZ1wsAvECcrU4Xbiq46EhItCuth_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8aAGfLgK1kg9G52xcEHDFVmdqAW6IoarRlL0_QMm-56yLMX55OEBgVL1U9R2CyP3jHBOrUixyWzDo8IWSUHNEKCic14II68AY_x62H9sfxFLVj2DYnoUmPR6-eOUyFFI43HsaYn4t0eWzGTtXUWzZmC8lXrJr2Ll887To7IDZiRf-ak9Xj0DonS5heiv-z6CEfpbpUFdGNIugrdut-25P3Nkiad6vCwHQgr9JrOTo0fkwkdaUZ47sNnd1Z3wYlqmK0-oUQh7LRmLsyBbKBcGaSmNtLGdKcGe3zUENBP67FcdLfRMQng1DBiCcaSrvxtOs-jPRAgYoWWt-k4Y4oL7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwtpq4pWzrs24Aoj0E6cQoaXvFQpA0Qc38zbOpEftUiw6JKVj04k1sYSjBdnIaV4N5CGxiMZ9j6sl3ZESBAzoA9d6MYTgCY4coKPoJ85RAHQC1JzyKcP1cuPdKA1XuoT0HTfciZzJ7wlx_-V_6XBmaQeMv09oUZi9b9T5-caszImSWJu8c4948IpWkbESb-zLm2yD_XBKT998v1dEHmnwc-Ty7m7gpoWgBlxPMGxSXtXwGbxCl8XAr_-YuJwISWCGkBUS1tWsnopeI1CNc_yfTlenMNFZT34FlXMUJJ7habz8H94Ln5ZOM3t_J-Nlyoxyr5gJW5pwwke6XtGwIB6fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Ftt8S3L89k7ib28g40AX_KibNEVR0FsuKC3hRIWC1oJ1y87Kidiadb9jURAnPfRfdLj08_uNHSmMEFDxkGxC3KQuqtnHdDRLUe_OdNAhQFFwAx3GOx15Fu7CPiDoj3d9esQ17_esrqzs0Q5HpKMF3nBKoCr3XMt6zoq2IDKaHN5xGiHSzPZT-VaoB8AvXF2OaIvbGla5w5up_w9H-kkMQT6k5fUFQU8ZUC6Q1DiAuxMngAs-UZJFSA3LPwFM-vdsFijH0fc8-LAvCD-IjAihyuEWVCn60O61fE8M8iyIs2hoRnfOAGx8TuOSOiH-60FZnBFiWTk4YFF02oEu3NHdtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Ftt8S3L89k7ib28g40AX_KibNEVR0FsuKC3hRIWC1oJ1y87Kidiadb9jURAnPfRfdLj08_uNHSmMEFDxkGxC3KQuqtnHdDRLUe_OdNAhQFFwAx3GOx15Fu7CPiDoj3d9esQ17_esrqzs0Q5HpKMF3nBKoCr3XMt6zoq2IDKaHN5xGiHSzPZT-VaoB8AvXF2OaIvbGla5w5up_w9H-kkMQT6k5fUFQU8ZUC6Q1DiAuxMngAs-UZJFSA3LPwFM-vdsFijH0fc8-LAvCD-IjAihyuEWVCn60O61fE8M8iyIs2hoRnfOAGx8TuOSOiH-60FZnBFiWTk4YFF02oEu3NHdtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Syjojn1jmiNtDhuRPCwKD0g4lVBx0_UHAX5NExVHv2TznS1wrrHylUMLSBRI8WEFd4_dkRKL1K2Jivz9W_-9HVRPgf80yvoLj2joKQHlFvsTjs108LgpVmd42ZOA9HFZQ6eHev04m-9elZYSXGszQxm1yv9d4Scia9mJHHN4A9PC53Kqq7O_xIyfbWiUvjA_4Dq4cjgwFrldJe9SmO7Mc6AlfQe5ep9e08OAEI8kn2MxO71Uxcl-8Tmh3Esc8cNIXl_HPmhGBluPH9F_n4H8s3viYklVqpodzd-GOY9CGX_HzMgpiNt7w8peAVKJTYQ-5wPxOAVJ5C4NyMtcSZ4T_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgXa5i9vvNWH3LY_ssyz9Fv4gHnCVGXxmJWsCgvwapdEJSvjH4Z0CGxBLkPY-pRuag9p8i_b2WgvicFkMrxoV-n420D049SZ7lfExS2-YHKUrEU9w_zn1TwYwLnlG2GWPb8BV3uaGpM7EDwrubd2sEwMAhFX1gODsWyWObCKSSSP8yPqUj2GnJIGk7MNu1KCYlsxySkzWsZl5JF4-cKrK-9jiTWo3QAsl1DynGVS_LqIdMM66LJoS-lmebEEqBUAyM6c7c6jHA1vFO-jEZUoRhTtjH1av8HwV3trodBG09OhiaUaEef__1r57u8TSBpbbxQZPhbXhbZSsFd7Ula0sA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=EAilPCztZEjnGumLA5r5-56tAWTkc87GhIUxL_PSfkIUh3hpVzkh-Rrc6SQE2wu9s1gHWb-AkjKv-ONsbJ2THdYhswAC626UC5Tsywnn7VEjvMEAhOEmD-cfCKdkq9HJEU5DEwu_GTjgEZBSy0_h58ShxK_Tm93nLYG8yKx72s5N2oOCxssQm_1J_smpp7x76dl_6dxH38oBVeRv4RNfupDLxsHTdgjwnDzOWKBhzDhLbCfpvUpHzOG2wd9JmjgK0t6agtDLX0XqUYHcNwbhJNyMDH71eQ9qEE6P-P_AWCrmCNAqs08q76VMFryyOp0lc0xlueK0zQWqWyUTU9dZyw7LKC2OlUFrBVpC729GxWLNZ4-j7KWsLOU7s2BQtWShPvw93LG4F5pER3mptJxS_6vD9v3FH99xmuG09JCgIQDDcqBEZigHS_MUe6WwPH3L6C__XRELOtUFX_zwc9H2b9Ra87MKManOsQtW-zremXdKaiHF-ENSlRkhw3QobalHl8hM_uly7M5Ga0HvbTKJra3jc79VgWIxakrkelZon5tKqsBcynfh8-HV0bCPBOkNk6smCYdfmcRyk7P7AcCF25hb48TJ3ykdid30_K96Q1hJkWfuaSGWMeIOllFMueYpuSvkJFjeWLEHlOZyNao3-Zm7qTo5txiKl0MKPE4Obcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=EAilPCztZEjnGumLA5r5-56tAWTkc87GhIUxL_PSfkIUh3hpVzkh-Rrc6SQE2wu9s1gHWb-AkjKv-ONsbJ2THdYhswAC626UC5Tsywnn7VEjvMEAhOEmD-cfCKdkq9HJEU5DEwu_GTjgEZBSy0_h58ShxK_Tm93nLYG8yKx72s5N2oOCxssQm_1J_smpp7x76dl_6dxH38oBVeRv4RNfupDLxsHTdgjwnDzOWKBhzDhLbCfpvUpHzOG2wd9JmjgK0t6agtDLX0XqUYHcNwbhJNyMDH71eQ9qEE6P-P_AWCrmCNAqs08q76VMFryyOp0lc0xlueK0zQWqWyUTU9dZyw7LKC2OlUFrBVpC729GxWLNZ4-j7KWsLOU7s2BQtWShPvw93LG4F5pER3mptJxS_6vD9v3FH99xmuG09JCgIQDDcqBEZigHS_MUe6WwPH3L6C__XRELOtUFX_zwc9H2b9Ra87MKManOsQtW-zremXdKaiHF-ENSlRkhw3QobalHl8hM_uly7M5Ga0HvbTKJra3jc79VgWIxakrkelZon5tKqsBcynfh8-HV0bCPBOkNk6smCYdfmcRyk7P7AcCF25hb48TJ3ykdid30_K96Q1hJkWfuaSGWMeIOllFMueYpuSvkJFjeWLEHlOZyNao3-Zm7qTo5txiKl0MKPE4Obcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=f3JjIfdoGahIJDG_5Oihl6tOX9-yf9-ISDbxQKnZ5ZUuvefxD-WsNJA_XjxrUYroqG3wgf_g3n8gCNSaSsodchu6C-0zoqz0eBJqy9U9R0Iw-avl1astGSkS3MKxtCDgNSquCEtCE0jZhSq3pYU5n7XrtQuj6KQPC3SpGf_MMekfpEGFUWjZ30WUhBTYE81Su96t2LirZ5rPFQ4P8BKrNinW11TI_fEm5l61R97YKg47U8cpzCUclyoHAEdi7jxw39U6LdtbncsdUdS07_I_9ku3sHuok_YigsE2HJ_NlI_Y_v_j2znY3TfhSnEt030iJwZOv10578BXB_LTwkxluw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=f3JjIfdoGahIJDG_5Oihl6tOX9-yf9-ISDbxQKnZ5ZUuvefxD-WsNJA_XjxrUYroqG3wgf_g3n8gCNSaSsodchu6C-0zoqz0eBJqy9U9R0Iw-avl1astGSkS3MKxtCDgNSquCEtCE0jZhSq3pYU5n7XrtQuj6KQPC3SpGf_MMekfpEGFUWjZ30WUhBTYE81Su96t2LirZ5rPFQ4P8BKrNinW11TI_fEm5l61R97YKg47U8cpzCUclyoHAEdi7jxw39U6LdtbncsdUdS07_I_9ku3sHuok_YigsE2HJ_NlI_Y_v_j2znY3TfhSnEt030iJwZOv10578BXB_LTwkxluw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCnU0euYXdphRibsg9531aLADRiNFoZc0njxcSloiDLOn-Hc8oShZ24c8Xe1OStUB2znk-jrUouVfIlaNVEYHSYowbKDuYy7nhVN3nY-gaSxJmUXCMPebKOcBmy6xbzTXxi3OYWsazMW6ub1q3WorFFCSwT_NCERztaI59d9baJ_PR7hNRFQHmZwiom3rOMwGCNGvqxnKd6ARtBZdEwdGekHc9wcDe4sN4VJYe0KHXbqhGg82wsSUiihFq6k2QJQCP-qdGXmvR4pi8lCVME9udSGU_rT5DObRI8APG-OOXMfT9bP8cOmurAXxMrMfVscF_UFOPdMbYc1Xfqwd8k_AYu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCnU0euYXdphRibsg9531aLADRiNFoZc0njxcSloiDLOn-Hc8oShZ24c8Xe1OStUB2znk-jrUouVfIlaNVEYHSYowbKDuYy7nhVN3nY-gaSxJmUXCMPebKOcBmy6xbzTXxi3OYWsazMW6ub1q3WorFFCSwT_NCERztaI59d9baJ_PR7hNRFQHmZwiom3rOMwGCNGvqxnKd6ARtBZdEwdGekHc9wcDe4sN4VJYe0KHXbqhGg82wsSUiihFq6k2QJQCP-qdGXmvR4pi8lCVME9udSGU_rT5DObRI8APG-OOXMfT9bP8cOmurAXxMrMfVscF_UFOPdMbYc1Xfqwd8k_AYu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyg0qtcdlZl1RmsPN5p_2PNid0omFdsXCPkUriP6PgUEK9XOJNp-5ko3aWaWku2guqMTcCktlDm0RPU4Aj8xEwxb2YNyq_MVbhbL3c8l70tt61jGjCBzBZ9VsIgeruyZTc_SfOi6XSHgTHHWI2NgAp2-zGXG81Hg12b_YBwGhJR3wMBc2eWq0dLPPyyGdeSawyt8Dci8VVUoxgRNvLFlZaVReCwUCA6pesbCtwpx3fXqEcdxZLAeESbkqS7_WEqOB7VnS84BMPi5AEWN0yue5BCfuLVqHPGDKxohsVW-9HXM5h6W-iynx3wT69P7JFS6diJ_C_V4j0nlZXMjRVMTQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpolbepm7Eo72R_DqTxM9MD_1cfvM2bHJYBbQ-NsRg0yrciQUGEGGWu-jdDaZroKGoL2SiwfMbD2h9qIYH0KOU0d2R0Y_Jltp0Hvc7lC-0SCQtgI4zFb2MU5_e7F2cLDgD8ZossJfj8v-2yRAUo6aPLXBpUdQpD_3P18gADxuTG_9jvCeXw9_b0Y_4N7Kr3_TdR6P00JljGhron0-iEyuJ97Ywlt3Mpk9RTQfrM4X1lkb7ENfNcJ8TW2QYNRshp9czvSvyp5RmOaaO9pAozd3mz4Ruon1Hk7OexDrQjJuvs1qzLrg_fNpAEpJvIUGPuGyifh28faDfTUFj5o43R13A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlsM0JalcZRrIPGvATT08LBnYaCEVuNviwSKVL2-W1i7QXhnxnE3am4qUd6Z7ne9P6VQh9Ei-ID0KYsAMtox-YAR0gT6YBO_u3tqHDmtTXaerLG1uLhOuE9y0ioJ_UrG_E3xX108sXtOXnPOTjAlrVtb3k8a_t26xcEKte6AP3oi8kziIhPCaX2x1H5w_7SPasI7zlb13-ab42RrlXpHMww_bAugAaFflpUsbRvhbw7RsFiIKA8lHqyxAPfEgZM3hQoeJ6w33mDP72P3WY8lQf4HITWi7bWfXWkQSsJ-T_pRCa-02vShEHFzNVMEg0KHUK5tGvdqe2U17v_a5YBoUw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=ktmkd4U8wN92vtPlwt90FM3gYc-1ZOCRIk94l0cV9Wj1m1AUqs8qJtrOCzd752Ut_r8NDiwwEGiy4e0OAykBY3ECYddsiiIMlJwwWO4MNPzsmYxwLkY_N5z9lwZ7qJpOdHpVlTqY3bShbfOztK-IzSgyHSazFNc0QfiY9sFD39csbJRzeIBri_AcEwhY1uDgOsGHqnS0TyTXkGwqZfin-yoAaE2FCHkOYdnIif7Vdqt__WtNi_oT7_tHWHBfBaW1HD8zF44NnsQj6YckCcjh6SUtaNVNAbwlNZRTgvc_6J29BeB1scWIdPVR3V0fWs0aASe7T98EiC45SnaPOnwazg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=ktmkd4U8wN92vtPlwt90FM3gYc-1ZOCRIk94l0cV9Wj1m1AUqs8qJtrOCzd752Ut_r8NDiwwEGiy4e0OAykBY3ECYddsiiIMlJwwWO4MNPzsmYxwLkY_N5z9lwZ7qJpOdHpVlTqY3bShbfOztK-IzSgyHSazFNc0QfiY9sFD39csbJRzeIBri_AcEwhY1uDgOsGHqnS0TyTXkGwqZfin-yoAaE2FCHkOYdnIif7Vdqt__WtNi_oT7_tHWHBfBaW1HD8zF44NnsQj6YckCcjh6SUtaNVNAbwlNZRTgvc_6J29BeB1scWIdPVR3V0fWs0aASe7T98EiC45SnaPOnwazg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN2T_urlaR4I05F6Nis8YbN0wMcnVGvU-9I01_tffaqqoMDqxRH5r5qkV7mzkCQay_LzjQNK3miMQ5A8hTIZOBeF9_rpIda61bye2LTNR-NDI2cnmeAwfXRAcxdKSjPSVhJ9_6jp1STQs6cPdL8bLmTTA0F96MZBHGIep1Kfm5L7UDDWz06bl7l0q8VZt8ugq4f3mB8asl0WuHFvB4sxr-nUIy5mPx0oO6dey5xS7eLBrmFULra_uItSjthfWP_IcciANPj7Krgbp6M2vE9vq8Wval9EORDQM2kwHIFZDfnwVYBcEtphNC8y1d6fxecf_111JApNcVy-Q53q-1DLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qj23rsIg84z_I1ddaa7X2tDqoh78oVsjvW70GBaNgDPU1BXSvuEGAo6zqcdRMhI1T_kzMrTd1Qu5Ua7gdoN3TQTl1jCJgT7PjliWqx4mbUWO7gejfEXiCtC3K-MLTM-q4B8vTZDSJIRF7j9XW-7qPSsSbqe5duYaTjhnPMgD6G3dnDeIiXyG7H4AesMQO9X1k4A3QH_dPC0BV0T_ic4BU2XP4HmsxaABDlyoZRGBBPUSICN17ladg9fTPcL48BVyc6uJTBufrc_6q0ck30pmw6al5bkuvo9PGow8esfEaYlflujTSD1gnIZup7kivtrss4JTwK1ewx1a395y7ipvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaoZTmE9EowveSgqPfq37xSSgiZzhEsJi0umMw0VAcJeRAzzcxiclFsvnowT8Ytat36B1_fB8y39aMlTKBkz7i8hLsWktv8TU0t5VEuBjndEljaOZ9GfSZuwui92siC3rFGHK8BMVjU2CtETIujUZGdZMOgENCcEwFqb-4ZcUOAYQZ86MKAmZwmW8INSJlv5Y9E3BCKDPWTqqz9MkZ6JmianrA5bdHMURLBKHuNXNrlSdGHhFAMQT0IVGbZhvj48YX0buRIrV2xLqYemjrVmFjN59yF81qU7368YVxTZHDuo3DrYhY6KG8btuicLDz4WsOWG4qSUikmh4T_AyM0fjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck0J2CXvWDED6kRzbnVR-BXLRWdOkS5PizLNeB7_wnibMHD93gkmPEHoGQ-RvD76N68E26YTIEzMH_Olk9uEdFHzWONSziwdLEzaCLOvyao5cpqVLhrCtt5vFaLLd6bpf2f5wlpkGMi-epTr4ZO2-VmuSARXJb1-HOadSJDZVdCl6WpBlv5IaiQMwdLA7rstZ4_vQUzl24FMmPpvy6lP2dZ7clmC2hhVZylFSz9_1zM5vtWrHoasuMy_15uuhTqh8dgWuI-mqsAKlj6hSAGz-7MT6Pa5qiKTDh9H-fTZ3XT6xUtagp1l1ZcWNubGfOudexSpx5bm6x41c_s-Sj_6JA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=NAf03IUc-6xXQpJcQ6ksu5z2LfybV5Obdss4TgVkIdKZNc-kMhwNsUxU_71LtNuzqOGoaIr53qawvWv_O0P4-d88qxhZyQEvdZ6HBRcflzuDh70KmEEZzuVT7e3bVxEUJlNeeSKd97F19ilasNBUlmwb2O-SRUhc4YDCcdb0OXa-5yFruqe6syh-_9Q6kXEdCWzEwanQT1mBYnH7AoI_QGXCYamybk5TsfO_MUihQjyO8DiDLFLYWWS6dnVUh5Mdt_-G4hU5jkV18xIMkYZcCYqEAfhZdYz6_UpDfg-oX6l_vv1ddPZ2H8zeGJnG7y7Dfgvijdr2qSzJ-ypTZgBmzIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=NAf03IUc-6xXQpJcQ6ksu5z2LfybV5Obdss4TgVkIdKZNc-kMhwNsUxU_71LtNuzqOGoaIr53qawvWv_O0P4-d88qxhZyQEvdZ6HBRcflzuDh70KmEEZzuVT7e3bVxEUJlNeeSKd97F19ilasNBUlmwb2O-SRUhc4YDCcdb0OXa-5yFruqe6syh-_9Q6kXEdCWzEwanQT1mBYnH7AoI_QGXCYamybk5TsfO_MUihQjyO8DiDLFLYWWS6dnVUh5Mdt_-G4hU5jkV18xIMkYZcCYqEAfhZdYz6_UpDfg-oX6l_vv1ddPZ2H8zeGJnG7y7Dfgvijdr2qSzJ-ypTZgBmzIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=G3k63QeZ8xkHRFe3vxlLeFnSateXOWr-UPN0h3u76VCQEbY3QpOh06O0sNmyX7J8owWGWL_615_J0GAyZ8D4PVql-4pdgUy3XN8UlxeHp-JThUtGMdmIUWXd1N_4fpsBZI8sGepZhFVWGTk3o2n49LWeIgCDfKFzIveCv3o-aiiRUo3rwz2vuNHJjl6q2o7R6pxKQz12KTRJth4Te96ri3pAoHB8oIorhX3wQuCcZ3SY-6p1KiZ8cNoWfcwB9FOZ-F-6ex9eJXGlewv66bNZF2sJqYpBU8DQkZ5rCmMiLZoLM_YJ6jsvczOFuYFuKJrznhOQwza549dS8oPGgT2hxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=G3k63QeZ8xkHRFe3vxlLeFnSateXOWr-UPN0h3u76VCQEbY3QpOh06O0sNmyX7J8owWGWL_615_J0GAyZ8D4PVql-4pdgUy3XN8UlxeHp-JThUtGMdmIUWXd1N_4fpsBZI8sGepZhFVWGTk3o2n49LWeIgCDfKFzIveCv3o-aiiRUo3rwz2vuNHJjl6q2o7R6pxKQz12KTRJth4Te96ri3pAoHB8oIorhX3wQuCcZ3SY-6p1KiZ8cNoWfcwB9FOZ-F-6ex9eJXGlewv66bNZF2sJqYpBU8DQkZ5rCmMiLZoLM_YJ6jsvczOFuYFuKJrznhOQwza549dS8oPGgT2hxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=NmXHWnOfdLQqDh2YtphwtbeqnylQjoJ3GVLtyByOmcUVKYyz9NEHyns2PFBqX93li9nfOg9G8JUeaI13hL-zcggml9GLWQyB6HwlnkZG7l_Y-0k7x0voMdplnIWUoxbcyjnGX4YDjKiB2jeWB8BoKzItqMdKjcX6GA5mGSunR9R9b81ju2FO2arY6utlM9ns71dhyi3dtcnIBySJ7mFqqkDDiPDzL2in_KwZVblVNcULrMBAkd7y8xqcTL5SIAwPKtC_K1is7kHnLPZEh0DiM5T4U8SJp890g3N6BGO8Gu8lRwFi_hxwoIyVJQ22yiGDN8q51abgtqI7or7dxvyN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=NmXHWnOfdLQqDh2YtphwtbeqnylQjoJ3GVLtyByOmcUVKYyz9NEHyns2PFBqX93li9nfOg9G8JUeaI13hL-zcggml9GLWQyB6HwlnkZG7l_Y-0k7x0voMdplnIWUoxbcyjnGX4YDjKiB2jeWB8BoKzItqMdKjcX6GA5mGSunR9R9b81ju2FO2arY6utlM9ns71dhyi3dtcnIBySJ7mFqqkDDiPDzL2in_KwZVblVNcULrMBAkd7y8xqcTL5SIAwPKtC_K1is7kHnLPZEh0DiM5T4U8SJp890g3N6BGO8Gu8lRwFi_hxwoIyVJQ22yiGDN8q51abgtqI7or7dxvyN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVLJugCkq32hbVvBwnsYjgcxK2DG-eiNzMCzl9rKQJCgOKHyKR9uszpOA60kfz3449xUjBVLCAxoMaymrk_oTVU_3ISF6vxz2E62I8RBvt_t5XY8F3OxJqRzv3DkvQZZE0jGnFeD4JIH2SP0Zzal2s7XaQSQxHGkQoGoJlEZ8lYpH9RzzDtAqxfzBAYBPU9J2arBKfRRJVmF-4q1MihibnJGUtWCz_iRp0d9OWcu1mSwLkmCihdfkYBF1CxF_34znCrIaLkSbqNthURZ0sdRlb3TGF9f4kuE_tC54hB2oSKzTPa67GGvNvem9PSBNHWBGEW4WCiyiNmW57-YZ8SyKw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=pF4LFaQI76CwSXYwJQOtQfX-EnoIX2rs_j3TCQZ4Z_AO4mTBdZL3eLpotom9UenG7IChxhPAL7vVAc2d1ZRIJH-GCZaGYMGY80ZxD1vUmY-fPif4YcLWz0VVZoieaatJqSHUfRweMp40JN-wjncOfyjnjf36I7F9yaZxmmgO7Axj-nZNMfeWfC3iQSevwnb3vNwAJUdsbRQs7x8QFi8MnvG3kGTZism2pdhUdWwOsmM4QDKtDSOlBH4jFqkr7JgaQUGxlhkPKxc6wtCvV_NF_5Bk9bkWz1iW4HAWWCWeYkEYuuvJa-gAtkSUEuL2Avkw3hC7O4-ej3V1vxkAJyJvWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=pF4LFaQI76CwSXYwJQOtQfX-EnoIX2rs_j3TCQZ4Z_AO4mTBdZL3eLpotom9UenG7IChxhPAL7vVAc2d1ZRIJH-GCZaGYMGY80ZxD1vUmY-fPif4YcLWz0VVZoieaatJqSHUfRweMp40JN-wjncOfyjnjf36I7F9yaZxmmgO7Axj-nZNMfeWfC3iQSevwnb3vNwAJUdsbRQs7x8QFi8MnvG3kGTZism2pdhUdWwOsmM4QDKtDSOlBH4jFqkr7JgaQUGxlhkPKxc6wtCvV_NF_5Bk9bkWz1iW4HAWWCWeYkEYuuvJa-gAtkSUEuL2Avkw3hC7O4-ej3V1vxkAJyJvWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=W2zkz9kAF3gYlOgMGhVPXR46U3g3hhWNZeVAFPIkvQWRJSOalnQAc3VNr9JohCYy0tRhF06jb4hficnH4iJOdeXURbbd9nR0imGXyGETcX8WGZRWLbDbO5lFaBby4_QkkWegNt7UNxjOHCFNI9DXLNfmt4L3YfcIGBi0sc1yuPsKTSriGgUxX8iANIuW9wsq90Smgy6AYfYc6Z1t9_h-vlHJsMkDZJGwmCpic29IGt4zSaK7lz93WOVS0hpUMRZpnzc-GN2HKr0s50ZtwnVRb_NHuXp6CXCC8OoGlkgBOOOwpW4sGldLhaRwHaQgaNmzkaqTy8nRg57E8gsuKjZwfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=W2zkz9kAF3gYlOgMGhVPXR46U3g3hhWNZeVAFPIkvQWRJSOalnQAc3VNr9JohCYy0tRhF06jb4hficnH4iJOdeXURbbd9nR0imGXyGETcX8WGZRWLbDbO5lFaBby4_QkkWegNt7UNxjOHCFNI9DXLNfmt4L3YfcIGBi0sc1yuPsKTSriGgUxX8iANIuW9wsq90Smgy6AYfYc6Z1t9_h-vlHJsMkDZJGwmCpic29IGt4zSaK7lz93WOVS0hpUMRZpnzc-GN2HKr0s50ZtwnVRb_NHuXp6CXCC8OoGlkgBOOOwpW4sGldLhaRwHaQgaNmzkaqTy8nRg57E8gsuKjZwfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=ULLhMGQyh4bWMQKrgzno1HaII2VvN1KFtzY1DctfDu_6aN2nxm6x8cS1GWiYvLlaXVwPeUrnAvBRhx1cSzJxeIa5F0MDLwhL8i9usum4Qn4ooKGlcqWU7rWbbPLnsYAhogY_C2gChJXwugtquQGPzxjejJGAn6J2lw04ZDzUucaGXVgHqB-OucsZ80C1gE8Avm0r-4p1Cl-2aiQhU7ll8XAFh_8qgckTNRD-NMpwA0ii5sUPFH-C_xuDJJuT5cU5rUQxy1GIUQ7Kv7N1mj3W9tgU2UZ89g1PKwy9iAZk4Cgsb_dmkgmqKKp-uAsQaj2GAuf9gIZt2RpPpHuekyaEGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=ULLhMGQyh4bWMQKrgzno1HaII2VvN1KFtzY1DctfDu_6aN2nxm6x8cS1GWiYvLlaXVwPeUrnAvBRhx1cSzJxeIa5F0MDLwhL8i9usum4Qn4ooKGlcqWU7rWbbPLnsYAhogY_C2gChJXwugtquQGPzxjejJGAn6J2lw04ZDzUucaGXVgHqB-OucsZ80C1gE8Avm0r-4p1Cl-2aiQhU7ll8XAFh_8qgckTNRD-NMpwA0ii5sUPFH-C_xuDJJuT5cU5rUQxy1GIUQ7Kv7N1mj3W9tgU2UZ89g1PKwy9iAZk4Cgsb_dmkgmqKKp-uAsQaj2GAuf9gIZt2RpPpHuekyaEGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=PKVZi5BjgDW5dxqaUKOFJkFcHzZLKkPU2pfWeiCkt7U8EGZ6VZXDv7X4va9j4iit30bZm_jjkmXJZzyJCqXpVN_EY5JbNjpiXUloXxvA8ynRIhQVYk069sMJYmdcNT0jLvTAsAaPgM15NjvVquM83dyOAFGhjG-BPIY1lVg-yqvlWIdC0wyeULSzUsp16l6qmqVom-ucPh_cQzlHnCAYzMqWrPPn9cuK3dXEtABdQ6fw6ljlew1h1ripMf7K80M5rAZ8Ms22zj5UqGmb63kwuloIeqQw__EZhm83ERq7tuVSJqyfqnn6Pvd0LQc1wDRVjQvIWSStyBwlxQJwRQdIlCg2V1i2ZNl7XWLpNeZ5PPy3vena1I4e5k0UpGHpiVr4RfoStyEF15KNIpppVUc4OulmgAo-4W5nvuNm04ZwR5x8wb0INT9pGdcMqFSH83NEkFKKoOMoIw7_YCBw173VWls3zsj9bnFZi505dv2zOFnWHUgPMnLIFiMuopwqLFONynjEOTNKw2ZAYb00Nve1V3N0x95Hn8h_vr29FSIRJfuo1rOls3GC5Jb68nGu4p2FiTYPeNWMkPWQzPOLX9IwcJAHQXGjXpqiOBXsubCpQR2x_HKbahO5QQLW-03AZTM0Hb0FRIMOLCG9Qd7lOaHeAot8KN42hsL34rCWcFDKk9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=PKVZi5BjgDW5dxqaUKOFJkFcHzZLKkPU2pfWeiCkt7U8EGZ6VZXDv7X4va9j4iit30bZm_jjkmXJZzyJCqXpVN_EY5JbNjpiXUloXxvA8ynRIhQVYk069sMJYmdcNT0jLvTAsAaPgM15NjvVquM83dyOAFGhjG-BPIY1lVg-yqvlWIdC0wyeULSzUsp16l6qmqVom-ucPh_cQzlHnCAYzMqWrPPn9cuK3dXEtABdQ6fw6ljlew1h1ripMf7K80M5rAZ8Ms22zj5UqGmb63kwuloIeqQw__EZhm83ERq7tuVSJqyfqnn6Pvd0LQc1wDRVjQvIWSStyBwlxQJwRQdIlCg2V1i2ZNl7XWLpNeZ5PPy3vena1I4e5k0UpGHpiVr4RfoStyEF15KNIpppVUc4OulmgAo-4W5nvuNm04ZwR5x8wb0INT9pGdcMqFSH83NEkFKKoOMoIw7_YCBw173VWls3zsj9bnFZi505dv2zOFnWHUgPMnLIFiMuopwqLFONynjEOTNKw2ZAYb00Nve1V3N0x95Hn8h_vr29FSIRJfuo1rOls3GC5Jb68nGu4p2FiTYPeNWMkPWQzPOLX9IwcJAHQXGjXpqiOBXsubCpQR2x_HKbahO5QQLW-03AZTM0Hb0FRIMOLCG9Qd7lOaHeAot8KN42hsL34rCWcFDKk9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=WoEz199Ki9h4meGR2pVbQrCAp5E6W4WDNIAU8EnO-DUHz4z5-2KLMRkgxJSBU66lE1m3BqnLiGAJ2t11D_1uKi6rEN3VjQmw7VWYWzeVJ94c_ErM3kWP13M3UdW-7rWn1VgTC5CIdrOa8epznz1x9EETCqQLy4Za-ko_s8eTnqMgZTtCIg8yE6a454gdglpJ0PEn9ayEXGwZJrBkoZ48rPzX3R9UCiEn0GMsiWh6Ik7jbeOIReFCU3ZjdG-vd2hAwwER2CLtxnv2EZARcgiNSD13r9PAb3-Yvy0AalvPBVX2syYt4pMBvxujx12bKSodWp3AVo9dtdO8ReCosjxC5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=WoEz199Ki9h4meGR2pVbQrCAp5E6W4WDNIAU8EnO-DUHz4z5-2KLMRkgxJSBU66lE1m3BqnLiGAJ2t11D_1uKi6rEN3VjQmw7VWYWzeVJ94c_ErM3kWP13M3UdW-7rWn1VgTC5CIdrOa8epznz1x9EETCqQLy4Za-ko_s8eTnqMgZTtCIg8yE6a454gdglpJ0PEn9ayEXGwZJrBkoZ48rPzX3R9UCiEn0GMsiWh6Ik7jbeOIReFCU3ZjdG-vd2hAwwER2CLtxnv2EZARcgiNSD13r9PAb3-Yvy0AalvPBVX2syYt4pMBvxujx12bKSodWp3AVo9dtdO8ReCosjxC5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=NWoIPV80LsZaRQews_e4JwqxRXgWxG751tNQrviUkLURVnHDX9m-7KfKzrlIkpXu8JMm9D8yUviyMiOOBI8ihu3H7gZNDAZoeRgubjH1HR3CF5Aw3MAnrnEJSlUwVMYRG4bu0gXT2rPg_pkHhAh7EZfLFqlmxghTAciRjwNJggGDpQ8sVqk9NBZOf01yQZDaMrFvLkBEcMqGIYeJ7plgALwp6lhUpylsx-IWeu9ER_DYKITcaRvwwudS4t-8NblZyJrLwupDDN_4x13SiJSg48j_R4ePisCzYXjpjQn_fExDayRRahsB4Jqa7OtK6Z-LKR9Y_ZMFF8hc22oLvCtXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=NWoIPV80LsZaRQews_e4JwqxRXgWxG751tNQrviUkLURVnHDX9m-7KfKzrlIkpXu8JMm9D8yUviyMiOOBI8ihu3H7gZNDAZoeRgubjH1HR3CF5Aw3MAnrnEJSlUwVMYRG4bu0gXT2rPg_pkHhAh7EZfLFqlmxghTAciRjwNJggGDpQ8sVqk9NBZOf01yQZDaMrFvLkBEcMqGIYeJ7plgALwp6lhUpylsx-IWeu9ER_DYKITcaRvwwudS4t-8NblZyJrLwupDDN_4x13SiJSg48j_R4ePisCzYXjpjQn_fExDayRRahsB4Jqa7OtK6Z-LKR9Y_ZMFF8hc22oLvCtXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYDQU2Z9zGS_oaT_lDMCkcqFPdQRBqMQ3I26gE2QplQDlvMxI8wVSgIBbFQkyAKrSV0igFJhc2DOQTH02GCys3Ia5jSYhtTXd8lKfx1WVo0XXduoHlnc5LWVoAAfbtI-uptzsdwNgXMwrLkUYwxF3RoABxZlSAvVMaUWuYglh8aII59gmRISZCWBQyVoDZmln2H6ss5zrRbUD9b_taLhJZPp6iRljtNORMhCXKTeKs_EVPOnfYhYktkBUawJNh-LM6dVxhh-NFgCHF7SGZVms6kQRbFX1kqaIt5GZuIkTj63JjNEy07WzWypbgs0C4GhxZnaxjt7u7NfZ-z8sbScRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8YJOvpUx7_3QLVPiAIZhLoxdOjSAax7iAF93d0uRDmmt0aqJ_mz-AgEAX1CAJ9PaSjwSaiX1nXhm-1dTvK6rbjNa7T9OsQ-3ekRc4ok2pNN5uuDNKTH9E-e-GkDKkyFfkpi23xPj4ylm5ZkOe0ATiYLDq6faPEsdAwRfLCf_liEQVSphZTufiGOZfe7rDCSeJ083JusM-YHH4kuHaYGLGQWjNhPjZy4IibxWI_U2DSOuyTkRAvwC4q3Zze5bSb8Ff51x1eIPTQZy0pj5w4Rpu-yzgr0VrCE6hNcCsTrXBwhJHUI7krWEEec5o1eFN7KmICDqIqTPVH8ulkZLn0lnw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=rVb4ASVIAvylJ7nwKn_Nv4QvbwsNKarKx3WCKMGkfWsu_KJBBgCKkYpacBnDCgYgmLGxBcJ238asx2z_0GyRFqJL-o87gtdFbK9pTRRdo-sFMDnP73fYCxeU02WgZH3eDhcKokcUskCOw0Vj7HMBoeX-u8tV9rLNI_YnnbE49YkFndcleH1J4cX4R6y6okuOIGyDXtSa1bkfYSuTq9v6TUuWtj1SdLP40mYY0_DGbfzDLgOGfBvNHEfWZpLTV5mIKrAIkrN1Er3HmvhPFaMHO450QowX-CkfsWJt2Yott8iwyDDbwR1MYYmWex9BtTHrvdyFk2keVa7_2j3V8w-4yyx84ojWBgYwL57MM9yVZg_WoD95x3-DdQyQyH2aGlfUMg-jfnkypacxdLLC2eP42X_MM_FVdqKIbydaQiCIxBnDWroxTsRqVEAT62YM3ZP2Nj_k79lxPPCYnB1-5pWt1-hnrv5bG3DYuhFCyndQbcj80Tmyb4pJCIIQPg9OUWTXOJS9gnwxbFyODnEZS1D9t8T3-GrVX_iu5ronkfVXpr7s6V533q1ap3_TmwEplbHqO3eafk0JU3HlZPbzFL09YCsmYhy3bis5272c-LdA9RwpOjlmH3O4AM7P8xU_jt-PiTCBxR7v0REiXm_tbzDHOFBdQK_D52LEZ9qHLCiMRwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=rVb4ASVIAvylJ7nwKn_Nv4QvbwsNKarKx3WCKMGkfWsu_KJBBgCKkYpacBnDCgYgmLGxBcJ238asx2z_0GyRFqJL-o87gtdFbK9pTRRdo-sFMDnP73fYCxeU02WgZH3eDhcKokcUskCOw0Vj7HMBoeX-u8tV9rLNI_YnnbE49YkFndcleH1J4cX4R6y6okuOIGyDXtSa1bkfYSuTq9v6TUuWtj1SdLP40mYY0_DGbfzDLgOGfBvNHEfWZpLTV5mIKrAIkrN1Er3HmvhPFaMHO450QowX-CkfsWJt2Yott8iwyDDbwR1MYYmWex9BtTHrvdyFk2keVa7_2j3V8w-4yyx84ojWBgYwL57MM9yVZg_WoD95x3-DdQyQyH2aGlfUMg-jfnkypacxdLLC2eP42X_MM_FVdqKIbydaQiCIxBnDWroxTsRqVEAT62YM3ZP2Nj_k79lxPPCYnB1-5pWt1-hnrv5bG3DYuhFCyndQbcj80Tmyb4pJCIIQPg9OUWTXOJS9gnwxbFyODnEZS1D9t8T3-GrVX_iu5ronkfVXpr7s6V533q1ap3_TmwEplbHqO3eafk0JU3HlZPbzFL09YCsmYhy3bis5272c-LdA9RwpOjlmH3O4AM7P8xU_jt-PiTCBxR7v0REiXm_tbzDHOFBdQK_D52LEZ9qHLCiMRwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_ibmjqTElDBrvXxfk99D8qEw9z2aA9oYEEVOmU3hFTKFcK4jSate6W_49rUCjcmR1w2M8sDM92OXuNVqNJESqZPV0CEF-oye8vCe_0sK_Q7FfDMX3pyL1rt8wlBu3XZIhsyRXO9IjzXblFZPDxNeuBlbWck6YHHz_L7hHPH6sBfN5kCrX8JrD6bpBTGJG9_BhfEU8QTZWkkvfk8xj9UN_hMcZ90XLyutCeMP8ZNk5QQ8EEXo2SvS_ee-6ao4RORzcAHVEOdi7BKfLRvWrFEX4A2_ABcHBH_XsPOBpHlWo6xX76QJvO4rWKFBN8NAKF6VsLYryVIA8bQuUCHbheEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us7_JP3CQtt85tfCjniNUs_9TEUPoWux_fCpBP4-slHYPZ8T0h_pb15dboVq2c5er0_FqODPvLklmVM0c3yiNRRrtrieTY3a5XWVzSzGgrzBlUHbX4kXghdiB1Hx3bXo4V19eur6ISKNE6S8FUTlqqIHzXC_6v6m4Uv7dTBS3SE6jPS4RBjIIWD9CzabeK-D1jNfV72QMA_nXXr7nIA_Yzk3YfiLZ8bjit0IjqP9WJrIdZ1j8_GX2Hi_1D8Sgpj0brObuXnOi56EH5cNq186l4Oj4D_naWDLJZBcxo77rrEF80DjbWbcJE_QmwMLXYtq73psuqM7kBANBnAux4psQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyb50PreZ0agQSGfdmL7fCZI9bk7eyrwREMs0iNnUqlYJEc7SSp0cIARlE3dl-6QD0t9sfHKwc4xE2qEjPG30i82KiHO2Jh5ShJokHeByPfZ5CwmpE8QZZwLJPoZaqOm8JcAippb_SzKzl9ckAuLoAD8H5Zcj5Jd1QnSHnGf2dYflJlEme3WR-bFVeNW64ig8n_kKhEY1qdRJrLNOHe0oU8UCvokKI4YM8mJkutg7M4OV4yMQS0Fxz8CIg5FMZB44dekLhBOXI_-H5X7bJ9aeka-mBy_kTetgM7tHvNOp69FVQ00yauiaqPWEoWC2pbAQCtmKLI5Kn19cmLNRQnHdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHcmYElixoCjoY-39DR9OG3dnxjlkh8UVEond-LVINuoUIgvobMjRo_7GjF4hccEjoHnZ2jed-Li6-wfaHNryIoIMLuVMbum91wdMU9kSvCOaJG4f7WrYBBxixH-JG6zjUY3Mwr4df8Yfk3Fc-_aSsXd9WrMZfmmAvdfVkmx2H3CfUkWzDN7w0iNXvrDwRJigALfqb-BPZuH5XFfRCRDH20ZTj76jnT5Xu2kzv3pOiV-_seTNm8MydojjMiTqozdQ0r1uQWXo5Zo2pEP_Ats4oYLZquC8KFM4SK2sadrmhoPiKL4vvaHTPhsL64boTmxezD6CHF58FsvuGf1gVvOyQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=kfesHpPM-NdrOskbefgZ9t91vQYgIIGelp_EdXWzbhTbA88mG_ZdJeGmg7Bz5DzOwCX2A8zeFIe7-sGAUIB9FWWVBLuHs5DGespgFvs6LP7arwwSLsDL2G63HrJEKtqW0V-ptOSqFtRwBK47D15W7tGN101rZ95FTd-KkDbr4u94BGP2zrJxYfHUDXKESDAcbFXo2NSLOH_LCXrrTBKptxJzajlQCtA1PvNXnK8TGpdqyjDfPVyPu5s1_NKaiXdy1vX06zrZJmlhEfRwm79H7QGITTBnn0eCT0dppy4r-I7apEgmDMSAiXBWveSPfX2d15PwB1jMNpEAYldnTgAL2p31rUr0Dxq-osRYbidzxRrmfjPF0W2l4orFLwazYOvARNa64GmpZbjp_2H-U9q7OdA1O72_zavNKMbrtVH69SQjTHWItw51-vrga-FiMG8ImmF58PVENZ85Tnm1YkV38G6Ns6fMuSgR-p0LJzs9NxyDLttHBC0VUYkru2-6B5kpAH_77fI7_kr7sQVVhsPxkSpPnh4u4FTG0vJK2W0-nMjIr2A8AUB3AuTqHiuyYNzM1coUs03GBQuBHskKE6anFlxfm9rPJimvSRYUcf9BYoNnzCvD5TnHWFi8SZy5k4uHDYUALypb6aYxHE_9zq86Sp7RWOEJXGzjS5Z2ZCoDhnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=kfesHpPM-NdrOskbefgZ9t91vQYgIIGelp_EdXWzbhTbA88mG_ZdJeGmg7Bz5DzOwCX2A8zeFIe7-sGAUIB9FWWVBLuHs5DGespgFvs6LP7arwwSLsDL2G63HrJEKtqW0V-ptOSqFtRwBK47D15W7tGN101rZ95FTd-KkDbr4u94BGP2zrJxYfHUDXKESDAcbFXo2NSLOH_LCXrrTBKptxJzajlQCtA1PvNXnK8TGpdqyjDfPVyPu5s1_NKaiXdy1vX06zrZJmlhEfRwm79H7QGITTBnn0eCT0dppy4r-I7apEgmDMSAiXBWveSPfX2d15PwB1jMNpEAYldnTgAL2p31rUr0Dxq-osRYbidzxRrmfjPF0W2l4orFLwazYOvARNa64GmpZbjp_2H-U9q7OdA1O72_zavNKMbrtVH69SQjTHWItw51-vrga-FiMG8ImmF58PVENZ85Tnm1YkV38G6Ns6fMuSgR-p0LJzs9NxyDLttHBC0VUYkru2-6B5kpAH_77fI7_kr7sQVVhsPxkSpPnh4u4FTG0vJK2W0-nMjIr2A8AUB3AuTqHiuyYNzM1coUs03GBQuBHskKE6anFlxfm9rPJimvSRYUcf9BYoNnzCvD5TnHWFi8SZy5k4uHDYUALypb6aYxHE_9zq86Sp7RWOEJXGzjS5Z2ZCoDhnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=P80i7OuSR8jTVBFqSifIYkLSNuu7pRSReNkOtrJrrzxVgmbNmEjuEuPlbfa2u4rmxZCBYfTjGbapTGlJzCjBV9ds2qPN448qUm-bxDrk_dttj8ICCxd8ZaHRpd2Skgr9HGELYgfzIZQelpfgkWqydgOuR4NTgr3V-m2HYOrOMgK96fi-JzghLNpwYX-bzhFCl9tnO7V7gDx0xCdmj_rovGUOyG9bYYFyGbbxyN2jAP4VKpBe9UGwjZVoCIKub6IpbbmcXDUtxw9QtgI97U92-PkBY0F2fVsU-ubNqDY2Yq4jIqtlKBFWL7F3xGxx2R2BCsmljn0vyF1nEOYXOAxrQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=P80i7OuSR8jTVBFqSifIYkLSNuu7pRSReNkOtrJrrzxVgmbNmEjuEuPlbfa2u4rmxZCBYfTjGbapTGlJzCjBV9ds2qPN448qUm-bxDrk_dttj8ICCxd8ZaHRpd2Skgr9HGELYgfzIZQelpfgkWqydgOuR4NTgr3V-m2HYOrOMgK96fi-JzghLNpwYX-bzhFCl9tnO7V7gDx0xCdmj_rovGUOyG9bYYFyGbbxyN2jAP4VKpBe9UGwjZVoCIKub6IpbbmcXDUtxw9QtgI97U92-PkBY0F2fVsU-ubNqDY2Yq4jIqtlKBFWL7F3xGxx2R2BCsmljn0vyF1nEOYXOAxrQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1CnZMGnogGWVPMEfEpXSktLKADByz4nM_RkVJlZezJ1rrDpjnoq3bCp1QqS8aTDmOS0qMWtPYiQwkd7TYUDFwGwN299si3gfw_lxU8_Tw3Z93QMDjcX7cc-UUpMVsIIG_YevJ7fAZpI5d4KuM7j8hCcLZuHV0PMw0r4kVV61fdOFoNbAM9HyWzHo70kFDHWZ2qAY-TPOHCLVdWc9shwhQrwzjGdMCDH262qDkKPrr_EHSFpLjKKDw22H-dOlcjwweX0Y3F5qUu_yqgCqgeKJeZJT17jPMdXgXkgyAkNmgAOybUnGDVPVnxQIbh-4onsNWed6gvXAq6cEGP38vWdsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9xeECR8Uye-KogF6zUcxjaLLTbjVG4XcCcvWBoCg0Ie3FPRXxVv3-ELK8jDs_0_Ia2wIpTSZnlGBVSbB3NyyeRHvOlMW2Lwj3_GUiweTTzIN9Hqp0H5_HicqXmIqEV8Us1_iyXmoYO4Avyt7jZXqNahzK1unzpLDKeX5MBSfN5tfwFdq7uLtjYZcFgt6TPKEPXSGvJ9CuAclH4ItBHAJjOAZmMhBUAuO1K1LyJEFPpime1Cgt8Lw7f22qrxN3j-hz3m5uVKH3HyICQcB6zh_BPbHOSCf7AYwXEwCzejrvwoE3H3Jz3eom94p8lG3TO4yClYTa4RV0ZWCJ21fw9YQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4wvXWbvPvXUWNIwas2p-KcSKGleRR6OG2Qir3mMhkoKMu2QV3d695wXqTQTWY-4XfWZPN41P5N3qd8N9boc9L9jyIkYrJ0yBHPlgBYNrpSselQXWa9Q15bmbJcaYWTzKP3luvsQc_5i5Txs8FqozduC_UC56U2CvLPk0vUJ66jY10GYm6AcfzXfQ-ivYWhj_w1W9ltgiJwrV4-I1JtABjUvLpyD_e4yC94GvbIY-C07LA3I1z80WcENPpvSLjSZXspf-CiBjdVwk81nPLwkFQGud4qQKq9YoY6TuWSaVCwsqiW0l0RMr6OYr6ChhzM9BboyfJaNoYzs4oBxEz54iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUR5XY_rEKLjlQlI5SiMmaZs92nlGcJPWLd62OlHlziwYzfQ4I5iUyn2z9ROY7_A_wtk_W2lVD3ddhxRdLw4EBNeLuzFJhrkw4RtyUpkLDiuzt2ItE4zpz552HyZXvl9VHGZO9f4IO6ijGCEY9H-T1Sleea4m97a4u7K857h2T9e4PTd6QiVWeIbKKoaUJtEQAMbs4l9x79ZNZVX0HKzzN5805fd0Ps2TrlMat_IFoVzRqBU8SXBqHGZA3MftapBlyyj0O8Gh1mvOM3PYIyHzBBshd9ZSuIosWvVI_9S0W-uJIUeTs1dMuHJdYN7Cprr_GdmbHhSVtxxbZu-P_TSkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faH47GFu7SDWah4Sq0U9wKfgsRSS8yJhYSfY-Bn7PAS0njF876KmlVBrlZbTmJjPXKrvP-eV5AZetl-YEc6JUr6VLju9fV0GUwu4Uee2rYn1HmTDiu01gsNSGC9uqKTbxR0KSLluJA4AUDjUg2fJNQIIwMXQ2aTGJUcEOffn3LzrckPZgcu42012c9osukNY1N0TTBpuNQyMMoc1LOfoVbj4xYzVT4zsRtvgneiMGGZiaaxqAeyr-cNCzrCcIPTjoXgvnUj-JHuhgrsA-HZ-r20hQ49JbwyxfmeHxqswy7cDAH4v3pyLtw9O7MEvZ11hr4IEV-tWcqoWEf7j5QNMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lygEIr6JPWdbHcKVeV8GfUCkIFER66xjzktzOLtH9wvB-ZiHXqKe-dPYK3fQ-prEYsq4UCAiNFjGgTiPEgknyf8qmzJ19FjBD2u_5U6-hPvJBcntie_i6kxySYeQkRKO1GYC6XUB0--fp_McWsLoBlO5iBObL48BAB4m7R40AbyPWNrKDNzUAAWATDQ7Bjf91_hA7QYiyFUNQZ9Pwd4lmNwOXwev_2MzKSGMluihgWFJC07sIfXfO2wgvwbqoXka1on5NYtwOYDfUtsRmlYocVr1Pt7llrnA61UVCcOBJg3jmdLbunRHi3wcos9LiPp2h4zKZhTsh4qMG5hyyR1k7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw7Ohz1ODueAyhaT2jwgtjUAIyqFmSshrwANtKYKVlgRmOjVmukR53j1NzrpHsSd6pBjwgMK4ZkMg_50U8l6zBm1u__1_25mzlzdXADQ2J_8WJkVzkgkQTfiP-yN9WN7GniWSpSdZXx9YzqCZWNpguWlCiXjFBh5hMVv9ZgVjhJ9p5guWHSjFKJjipOlClGgvbGiYfhsJzqtgghtiNX9xLHDRMW7LtaRpiOgI0BFs6ht6aIiUOQrmNqnI5Z6C_UnuEGVv7cpoy5gGrC3a94uMDrBG_Ig-8ibDXEXvAhdYb4uSIU7LiDRqBd8uY3QJ02ekEvmsYHzwd8pxyeGuhL7Qw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=LOdpWjV_rKeFwjYPE_MtL7W3HvBI7R5yPDlFwuxgWa1C-WkQJ7dfGdw_LcT7zJ51JobBQQTddzphpGm9WSvSUrpDdICxDcTgs_f0DHhbAHvL15PpTIomflMmy5W4Wvrs5PlM_5PTmudwcY1MFj9LjQ7IEnOeMJAHyFuUNn0Zpi1Vb-mdpAJsHFUOIy778QpPulAEWH1JoQ3gM0WowdGfQQSFjLEOWxXFGMdOLDZ1iOFsPLzj8XNAea3YyQIlunfZMnYp31_vleGm3oepT5WwiKInmTfPi0diJ5BJdH7EYT9HMauLenLxNHyDzlOludNzWVIfaNHW1zGwPfYGL4oWeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=LOdpWjV_rKeFwjYPE_MtL7W3HvBI7R5yPDlFwuxgWa1C-WkQJ7dfGdw_LcT7zJ51JobBQQTddzphpGm9WSvSUrpDdICxDcTgs_f0DHhbAHvL15PpTIomflMmy5W4Wvrs5PlM_5PTmudwcY1MFj9LjQ7IEnOeMJAHyFuUNn0Zpi1Vb-mdpAJsHFUOIy778QpPulAEWH1JoQ3gM0WowdGfQQSFjLEOWxXFGMdOLDZ1iOFsPLzj8XNAea3YyQIlunfZMnYp31_vleGm3oepT5WwiKInmTfPi0diJ5BJdH7EYT9HMauLenLxNHyDzlOludNzWVIfaNHW1zGwPfYGL4oWeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z72BkTyK3Te25KkGKvBzmLEbUwmR4OoVF2iM2ekWMXscfFmPU5eAIAG1miNgar-jqgNACas75_QGGMfcU4tnDX_iwR2-6OM_UcdIWsHl8rMQxW1q8XJdBLGDiyO1uaOwRRJYVwjZ6MtS4VDf1zdTERrIK6Cq-Sau9zJLuvYgD-lndGmQRgWyIZDWFb-x4vL_9EwtUWuK7TMMvs3bHf3P_s8BJzxAR4shv9EPR__s5--zSF_NUpKWNJJ6mCNmPFfcgEJPUgJkoBfvWf0kcGEwjvtdha0lSsB1TOd8Xyn5NqkOccxEq3SRiFx4U0A8MWn4vvNVV36OcJczZCybmQN1Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
