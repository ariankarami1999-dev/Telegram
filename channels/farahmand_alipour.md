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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 11:00:43</div>
<hr>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیار دلاری بر ایران وارد کرد و حاصل فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران متحمل کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiWNIn9AjZs81MmjIvrcD9sGrtXBm50rUG-_C4IfxpIVO1uu23zeWLIfbq2TwWWoxFpD88t-B0iR3xT3bzSwqkzuU39DZiX1FUSgqJf1LiaSmAJs3nWTIwET0HAaKTGwcr5Dhx9BubL3uMBRq3ki6fE0rcRQIv7bS5sGzyrXtaEed-nC_n2unAA5d7ztsxu2MN7hUK98RyJ_uksgWzMcvYdgL2c5NgKWcvcUg4M6YUOHOZxZZl2QikX19JMY0kEJIFV0j9ciP797oFNzjHD84Pf1VrzbPP-tYlbB8aKzieOw-S5PS0dIsUcYgRvUYQUEC23L6qif0vILT-s7yJcDwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhqLZIw4aPszHN4hhN5JnJGr14vrVfmyBQakgtL-HqBEUUxIxXiIPSQHmCDcnOQdVm5PLK-EMCvtCu2Wye6o4zdO9Dw8do_O6VI7JAP_CUFHXCTyK8haa67rS39TaUGnRTWL9PCdnwjrn7IiQ31u4qJUbbT0PQTFRchyiRl8B3qh8H0yPqjQFpHzXrBg3cDsbLe2e2b7yT-hyg045AuUE2U5f5RkU1yYE-HDXnk-U3u0-hB8tv4cC_ahSfTXCQeuoDYzznQbZ4YPJxHpZyeJl7kaMiAzlRtclSgzBFqQMApvB7N2wbEcvFwxu3Ja0KH2IAi5En_H0x0kQQLPYRo_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAKbopNILFRsrrsik5imWYIQndMP1PV3KFoUcaWa4VQGEv-zySMG3jlfh79ZXyT9BR7mnG-Jc7A1Th3DzfKcDA1PNU1G21uEKIDDimieO1zF9BJ2ue5RdoI4dtz58sTuSpqhlATFm5vKIvAxk7vFb22iYg9nsI-IRUetW6zFdkoPVWB0mgzGI5zrtXH4iKTb0C8bLeoFo4qLl-mN55sxGtxsSJ6E2p9da8SufyQJXr6vzlobkuMTRUwIPmGLk3B30PZcL86zcnc0cmzhRgiDmCkrpPYOglSxeTM5cxpNw6995yVXm9T3TIGVm1fJee6F42_LVqm_cpFQIzE13gDWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=spJIda_Vp38ADUMBdksliQqpfEEiN0ATNkEJZqn5KFeOPVmVFKKz_H64dMALhFjkyyNejlpllxfcukmyRpxlVLBWH3PWZv7FJ1pZB0a9QQuSOxe--zJi_sko5UD7Lnt53lD0wB5jyAg7mjA8ApeCN-CtKTBmgN4U6kKoQZoF5x1wlCJXIVXzQRJEa9bgYaGmcnVxclHkNhMwPRKnmxbLTD5RCOkDaTSwOZ9ww727YXBKgAKjPP6l6xhD1qo4CTXbPz3qNcaBatyr5d2Qos1bqc-pVMLEkvBkzjzXiLDk06varrX56bBQIbep38htWrCxZ8sqvG_imb0yh9DqQRIlfWpylCEeQVy-X-Ex221VXNUUCsqWoVtTpJ1XL6ScaKfYKByHOqATC81agkN5gHSSeJZkcDyJhrI-IfAp8naDhQFms9iOopQn2WsWb_RNpMh-m_oUSQzSlggbo4YIfRzT7LEq1wDVDavxh2b9e6s9t5LJ-BCCI2ajJh4yG90sKYoT1n2LicRsRWHdp3Lv4Ey2tYdlnwzMu8bQswAgcwZleEltDKaHxzz3onfGFvIk7hRAdZvCxcYpC30D15S7Fv0gMfWTBYv_FwLnXziDL_-tgQ-MZSs3m20vz0sK7g-CbDg9vfCOY8NTIxvaZSr4TCkCvg51XqMMt-USdVvfK8uY5do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=spJIda_Vp38ADUMBdksliQqpfEEiN0ATNkEJZqn5KFeOPVmVFKKz_H64dMALhFjkyyNejlpllxfcukmyRpxlVLBWH3PWZv7FJ1pZB0a9QQuSOxe--zJi_sko5UD7Lnt53lD0wB5jyAg7mjA8ApeCN-CtKTBmgN4U6kKoQZoF5x1wlCJXIVXzQRJEa9bgYaGmcnVxclHkNhMwPRKnmxbLTD5RCOkDaTSwOZ9ww727YXBKgAKjPP6l6xhD1qo4CTXbPz3qNcaBatyr5d2Qos1bqc-pVMLEkvBkzjzXiLDk06varrX56bBQIbep38htWrCxZ8sqvG_imb0yh9DqQRIlfWpylCEeQVy-X-Ex221VXNUUCsqWoVtTpJ1XL6ScaKfYKByHOqATC81agkN5gHSSeJZkcDyJhrI-IfAp8naDhQFms9iOopQn2WsWb_RNpMh-m_oUSQzSlggbo4YIfRzT7LEq1wDVDavxh2b9e6s9t5LJ-BCCI2ajJh4yG90sKYoT1n2LicRsRWHdp3Lv4Ey2tYdlnwzMu8bQswAgcwZleEltDKaHxzz3onfGFvIk7hRAdZvCxcYpC30D15S7Fv0gMfWTBYv_FwLnXziDL_-tgQ-MZSs3m20vz0sK7g-CbDg9vfCOY8NTIxvaZSr4TCkCvg51XqMMt-USdVvfK8uY5do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=aD1P5GTQElZgHtmA4fqSAW1aSSPCCAlvKvCSPd0ykOK75xqY7x_BFHSjV2uBd3XQOMIdpo-7r32pWAIT5GmLF_9Ae-SlCyiBqCIKd6ZKxpp-W-xfVzp2I1yPAebGLE-6ybOuYIQiQaDmylry7WOYkSiPIW4xXqXB5Tqv_45e2yY3AaKprCRty6h8JL9Bl543M582ReeP_YmG_wxamOWapZy7fTyZid5SPhnCIzBbEo1LZY2PFdeJDx5y0C_aK3qCspoVM9KyiohX-724_tlDBaU_WJ8JFdiOTUB-Rhs2JbRF7vy8zTE98gvGuagw_ZND1TcLf8jrhhn5RXOYcceWhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=aD1P5GTQElZgHtmA4fqSAW1aSSPCCAlvKvCSPd0ykOK75xqY7x_BFHSjV2uBd3XQOMIdpo-7r32pWAIT5GmLF_9Ae-SlCyiBqCIKd6ZKxpp-W-xfVzp2I1yPAebGLE-6ybOuYIQiQaDmylry7WOYkSiPIW4xXqXB5Tqv_45e2yY3AaKprCRty6h8JL9Bl543M582ReeP_YmG_wxamOWapZy7fTyZid5SPhnCIzBbEo1LZY2PFdeJDx5y0C_aK3qCspoVM9KyiohX-724_tlDBaU_WJ8JFdiOTUB-Rhs2JbRF7vy8zTE98gvGuagw_ZND1TcLf8jrhhn5RXOYcceWhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhUkePIIQi3ZP3LHcl4hVXd8WR2hXcZwEpquIINSvMW6KskkOTo9qgnt_krl3iwQwp21qRY0R6o-gZC92xdx5gel3LWYfCU8UrEQVlrEqHoSkfvI0nxqXAtgXejGfUA8JXReIX_B8k0h-OHuXbVF1t5sT1aNPlWQF3KdcXz0qDOijXIsummurvD_6QkpTL-kgTU0ID1WZj9D-KBZq9OIMVfkFS3UtIdYIFTcpONunxRdmIqwzSpXD0ektJ1a1UACN6MmHMLA5sqO-21UmXOf-zWKPw8miWf_uY6oUt9EEr5X6Udcuuekw2XiF9teqofjofc4DEts_NYLjGUeSD0TFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=PEyb2qUcqkC8NICSIvLDyeKspTKVxyYj-UVQ5-4KZh08Y9aj3_YqJijZy9RJPD-OKMv_i85VVr6X5dhh7eLf8iNTtFeAMSFNXFwtTnqyGPF0wtEkeUHr1zGwSmk1q6IzoTdiyVWd-3wIIueaU2zYfX68fBDunGFMm0A9w6ywqB3s-uDWgchCA5vr94Mp95NbI-kHqCPnff3mMsue8xGAojB6XWhlZ5JstfZyRWvTQbt0LHWW-dzescQbd75X_7GMYxknZFJ03VzTRRhyE_biZgYfBk5V8XWU7ntQ3Xe24SIBiWgLeDC8e294UltYSPji9j8uZR1xkmEofMBhsdCfUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=PEyb2qUcqkC8NICSIvLDyeKspTKVxyYj-UVQ5-4KZh08Y9aj3_YqJijZy9RJPD-OKMv_i85VVr6X5dhh7eLf8iNTtFeAMSFNXFwtTnqyGPF0wtEkeUHr1zGwSmk1q6IzoTdiyVWd-3wIIueaU2zYfX68fBDunGFMm0A9w6ywqB3s-uDWgchCA5vr94Mp95NbI-kHqCPnff3mMsue8xGAojB6XWhlZ5JstfZyRWvTQbt0LHWW-dzescQbd75X_7GMYxknZFJ03VzTRRhyE_biZgYfBk5V8XWU7ntQ3Xe24SIBiWgLeDC8e294UltYSPji9j8uZR1xkmEofMBhsdCfUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvFAJ4eJXZ40DfNUzjFlwfdnRLnf0onSNdvmJIGf5Y4QFjmDPwTHg68Qc1LeLkXH5xsyoWvN0isYqmOt3iLrIqDxT2ZQhUyzCJhJwenQBCLWVbH97gaxTYqX4UzbGI9ALYSLnCGPJeUpFhRZEjMKqnayUTB2k1ndX6NNvhgFK3gE1674EMBgWb54iz9GI3Lp9jQ1Vzob8fzMKnarT3MaDa4LUrV97l6PTxD_LnazexjZ0_Rpg9VTidbYvG2ElSX5DRgvA127qB4XQbwJtLTsWfufLldZUHyCT1UdXSbJbb4HpIR_XHFmBLinrLVEfCnnPw6caxHZw4DoXtL6SW0VPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekXpSq5A7l_hki0SdqOI2jWAX6Zj46dhN5bOB7-kr614-lpFUW9yJS8fPx43QOayDC8OJG1Ve2yXP10FsOtNMo4GqNI5KEVO9KovVx6CpuAv1zNe0FFa2FHzC34X5MRt-eBnkceX8ZoZD6HxSrB163-h8tPNI5umgJERvQPdf9StZAmyxnIurhUKxDwZiGJ9swaD0vwiY_8Iv6prI9ws5IabCz71f_zPyPKbPA6KU9xEkrHSKJ5g0tc7LWUwFcvGsEmZ8473wp9x8THylEbGOGi9vqlUQtzd_-Bs6mxjkznsDVMuPzzJaf3V2ZnQyEHk1WTE_FyVh95R_KyQ4CkUZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpPnB4O5SovOKfHs0NGpVEdjMUY6OjCculpLwQPlFty6JlE4s1SGFjkMKb7R2xdrhA6lU256InscGauuxkGbVDif8d-trA2Pn7hZ5Ez9zeNH_-MY2Y76jSCaiBRIuPCYFZ7ehgHtCfsScp5HbsueGS3klRRLdD23C4fh0euE2gGfEhxuZ2KHaPxsgM6eVskY2LDAC55VCDR6uW524Hve_JSX2pW355-x6aSjzPwzAIZ93VIS0Y3W6aQ0HUsKnzwUoLMqHvRFZv39-aC1wRwDSpoDnnjgp9ukOSzAV3vNha3dlYFv1N29Px7UXkMMp5qtmTp9xzTocCttSsTs3DXf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0XMK4kg5zAKCZ0VnJDQPUEceumEX6CMKUnNgnHUlmnDNE9VWdfyX5vCw0kjiMVwfbvaH1X5PLfqRvZgv3ktdg-F41CSWNelHaGd78kouBcO45pD1DfIRODrQdZC50PMm-ReWRwKIACuYY1vBtgIthQSDOvuZOWjatTlR5Tu97qqs-FGBdeG-gLozeZoeCptF6rLxTWDn3bdImLrOIdoh2cT-b9sjkMES_O9iqTMsAeb_hYvoBGEBxU-e9Qrf5nnbnDhI28WW5O0Xiklfe1EjZG3gt9ZgLghJIJwSDPc-ucAp_zruepI_XpICcztHk-gbJTGkfPId9jGZgxwfEL2Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmFjvLPi3UL-W6Eg_2UDGbvtAWtFESwQcc61V6SFPivXBE00vk5HA-j1op8Gl2_8Cgk6sN7ic6-03V31fzelb9aYf1rjfj8yDPhdEVtNU_uZswxxz3KnDbZisCs-d4tH1vZUIe4OQHnT1vctRklQvU3zBZbSqMgwrOJyUMNmPP1XE0yEir7NfNMhR2e1Lclz65ANpTVOjyvyY1u5ughrHJAWFZpa0XoVxDUiiao5JubJ_485d7CxSd7JqIt9_TurmOjgae2ioJK3hMk2GNyN29445pBQiMq28YMpID44hkf2pCctz2JPu1F_Nhta_ogonOmTyJKbcIi3IN3a5Xc1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3BQWAQxMG721Qr0epNBRmh1KxRFYd2NWb6fNiW-izW1EkYIKZlvxcwRQ3CQbxxtwk8ldBgB_msEInmCbqRfw1AMGq4nuinR-j94bWjmnBudcOJlZaehv47Hq0R5RSL_g4A_xOeVVvXBZKzrEC3GYLGkazWnvXIuV4D4rTGiadT932xAKBRcgZowAIl3T2tepLNT2k_ANPrpG51wIFKFX7Qi1m5Nfk_9Om7NteJLAZUM5Qw7ln_7D9wiZw6E_Kdy581EPs3wS8tT_sGZ3ZbCW95LIG6zFeD0Cl5R-aKdTMSR6E_Ihz7fX8TsAm4nab5NtBprZfU4H-dGqE_Q0mapZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDhDHIH6WRSl6QvcEqSLy-hiIMBJRSyEARCqDcB261UJkr9X-154B4-WNKbAgqPI53sD7Ny0jZfF6hdQbP4Jx389_Ff9OMXygT1jWS5bbscjjEXowkxoKjGfsN8dTO4Wp0OKPbiwpuiQKOIDtAC_3h2_bNVzBRSa3aSuX4APksw9H5aW7leaa3nUwoPsPMV0TXLCPeIOTcTK42xZhfxChptwbrWCGb7HnuN4xK7HTo4sL28OsPmIHrvwpTMwaHm49IrHMebpp14ZrcXOj3Cy1BQNkdFDVvF43Byl5JkNVlsP3Q963Pvy4Bi9r6EyF_8bokY2wu9vH18h2apBfSwqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=RkiGvILy2pQ4eKXEJNfsGCh4b4B22wxYP24iqacv74t1xLcjiA4nyU3Jf20nD1WYDhwrn6PzO70zwuJw9tBsoK4LrT8w5cIGWYULWsK2jbJdvrSQNFBG3slEa2Bt8ncWwCmmYFrHenzncMY6AlPr3F7CtTQrUjYid2A5EhFWJtr5jDW4QN-eaDL7TGk4TnaT60d1-wnWWi78cCqWHnpWsBevDjVThmo7MxtqCvqqCCNt0nmCnyRRzyDfMxOfTawHzz9sx-zL3W7Daj1MW07Oz-FMN4AZUmGdfDJlsz8wHNMiwaLToEg1MXYwm-ycwSl8RtfO7J9B-tTamEvFsTjp6p_pTad-Hkx3xLT5gHGFJ-lOUp6inNFcKCmUjH4_5EPVqGwvJHKl-4PgYFoqJ0NHFzhGTsuMeRBLEAs7JETAngmMrfAgF6Aa-pZICbS_hv4T1mf2qqO1Z5nw0nn_F7Q9QOVycvFx9gGiYHwOpqgvWd7NZFz14hmCaRiCuyTMjP-np_gOi0h7ftYrJrjo8QhNjDAgzNuZG6hFuZzdbb1J4Kx7WpnZSoJ4ODk6IdEgUcGfoYKrrSRBQuoAAcOTyOMmNaBssv4PtEqfACawJEC1Cxsd-fUaQrB8JsxUahbeoNwBRoVNK9NnwXTUWBs7fk3vPa0iHZjNpFiJ93rYFqYptR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=RkiGvILy2pQ4eKXEJNfsGCh4b4B22wxYP24iqacv74t1xLcjiA4nyU3Jf20nD1WYDhwrn6PzO70zwuJw9tBsoK4LrT8w5cIGWYULWsK2jbJdvrSQNFBG3slEa2Bt8ncWwCmmYFrHenzncMY6AlPr3F7CtTQrUjYid2A5EhFWJtr5jDW4QN-eaDL7TGk4TnaT60d1-wnWWi78cCqWHnpWsBevDjVThmo7MxtqCvqqCCNt0nmCnyRRzyDfMxOfTawHzz9sx-zL3W7Daj1MW07Oz-FMN4AZUmGdfDJlsz8wHNMiwaLToEg1MXYwm-ycwSl8RtfO7J9B-tTamEvFsTjp6p_pTad-Hkx3xLT5gHGFJ-lOUp6inNFcKCmUjH4_5EPVqGwvJHKl-4PgYFoqJ0NHFzhGTsuMeRBLEAs7JETAngmMrfAgF6Aa-pZICbS_hv4T1mf2qqO1Z5nw0nn_F7Q9QOVycvFx9gGiYHwOpqgvWd7NZFz14hmCaRiCuyTMjP-np_gOi0h7ftYrJrjo8QhNjDAgzNuZG6hFuZzdbb1J4Kx7WpnZSoJ4ODk6IdEgUcGfoYKrrSRBQuoAAcOTyOMmNaBssv4PtEqfACawJEC1Cxsd-fUaQrB8JsxUahbeoNwBRoVNK9NnwXTUWBs7fk3vPa0iHZjNpFiJ93rYFqYptR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=FW6JsQIzLNqAi3MzP-79cDQX1aAJn213qdGiqdfOdg5aPAYIuSmpCHrVL4Y3hU_oeMLCvhoiHFQXHY3AIi310RH_q4uvXBq6TeYhZ68xs2Q8rHV-kfIT5Ds5WA-AFyygEjkXaPxGmvOEsrOhC06oDrz2FqfjjMs23UZJnlV3-ORyWNGpIezRgaFPI_FxPWcD5xooKcAmWS1NOOMyxQLAFtGcY1oi3OjuYbtWplXAHX1VKL4V3eYw__G62dCvMf-4-2t18_yNvv0cYnApeHrqLkMNT0xTu64BLXCNndQ4SRwXtMoCbaJGpe-iLVpVIlwaxJ1iX1nHj0pawUHhosE9LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=FW6JsQIzLNqAi3MzP-79cDQX1aAJn213qdGiqdfOdg5aPAYIuSmpCHrVL4Y3hU_oeMLCvhoiHFQXHY3AIi310RH_q4uvXBq6TeYhZ68xs2Q8rHV-kfIT5Ds5WA-AFyygEjkXaPxGmvOEsrOhC06oDrz2FqfjjMs23UZJnlV3-ORyWNGpIezRgaFPI_FxPWcD5xooKcAmWS1NOOMyxQLAFtGcY1oi3OjuYbtWplXAHX1VKL4V3eYw__G62dCvMf-4-2t18_yNvv0cYnApeHrqLkMNT0xTu64BLXCNndQ4SRwXtMoCbaJGpe-iLVpVIlwaxJ1iX1nHj0pawUHhosE9LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIriiyeVRiEcpfuTGharM0MS-6ZiMTHJQAsDXAgH2A_qXakr-tTltvGJXQu0rUb5-oR0cBcJq1mEBD9bG1Tv511dND4F8-dtGu3eVN4zot6TjboL9xuiV_lVBVHzGscP-f0C1pG22XzkhiOD8bKlRmM1SQyXIrAZEXQwl2FOwAapi36rzESgJOEz_lfymU8zHA8UGeDzwDRe5PGUx9B8e5cvScNd0-5gjZynqyem4iCAGfGOaBlrHOhWN_6kKQXU_mEumZ8qNX-adFJeEx4VjGZPOOBYH-Hc9jBeK5V5VjMLOc-L1NVjTW0OJHCab03p86jFLpcm8apngUV1feWHQJ-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIriiyeVRiEcpfuTGharM0MS-6ZiMTHJQAsDXAgH2A_qXakr-tTltvGJXQu0rUb5-oR0cBcJq1mEBD9bG1Tv511dND4F8-dtGu3eVN4zot6TjboL9xuiV_lVBVHzGscP-f0C1pG22XzkhiOD8bKlRmM1SQyXIrAZEXQwl2FOwAapi36rzESgJOEz_lfymU8zHA8UGeDzwDRe5PGUx9B8e5cvScNd0-5gjZynqyem4iCAGfGOaBlrHOhWN_6kKQXU_mEumZ8qNX-adFJeEx4VjGZPOOBYH-Hc9jBeK5V5VjMLOc-L1NVjTW0OJHCab03p86jFLpcm8apngUV1feWHQJ-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAmrXwfDWA_Q1vUqYGMiC7eJdqGtLSKzYibHeKkYcV5h80s566Qp37ROpwtjwm9RAGa2_n-y8wPKooOxluUOlZaIzLyyxwGfbYaHQeWOzxDRSPSLzl-Ks93WNHATFSHfypTmhMlDG9x6DWaZIGQ6GkKU6buBWJKlqlalhvil6lYlFQVfDWJshbmBs1jCKaI8BPew0-DPeS_nxZMW2m9L6kgOL8wFYmptV1HHn4nUOdO25GesWdzI1meKnd-wW1-lMp_j3XXkdaBnKkDBQ0Wa9MzUambwEPsjuJt1fXpedK372U3gXu43seJSZLXOlas4uXWkoOsmcZwE-Q4P8sCmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbIsFfvMe5rrqaqRSpEiEzL1qnREt_HWS_FyCAxI9CjLivpdFjcmk9kp2uJTWZJf1jTTEAH1AgXDfWyyLgP2ptuTQL9-9g4QpuslpTNhds73K_eoaiLfrS8YU_tKBvfQATfQOE8IUayl9jR9p6LcRudv5RVnvbruoaj_HwPQf5LaikM2BZ3gTY3eCTa6_h6wEGztd7OZisJQBO2GdOYqo_BqWbcCQUhWNDULGSTxvWzP9-ZVfexBMkIum50GcY_qcmJyZAlxfeoE-_k4dVSqo9GnNgsRM5PHHA9PzzF3vZJRLSsvXGCUtv75tSgznWolR3zVdEp4YHysdaAyFyRonQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRtaUSbYWLzD-50Xq06NnXOBnF3O2TMs7jZOXLEPPt_kbG4Cqfx55FTdqkhLg1ePnsBPDKxdQN6CAsXG9h8qOURsvsK-zMUkSSTeifLZ0dy702804CwGD-aU3ckxCTCFYQud2QCqS9OInOqM2aN5iPmpNKBTr4h_4KNjK7PtIPcRxuZH9neNcxnCQh3a9K0bCKm2zg_Q0-B6O8Bcy5TJ0g6Agu3DkBJdUS3ccFU41CebKHCMdDky9eDbj-_7L18QegButwTrXgp3xo2AMp1mDYOfRFOq1AaXpR8lnVVr4VwsHk27g5FHdLpFjSdRCLmdXP6hASYa5mkQgXafIJqVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=p5Dj7syUnIjnbHq3aTCANlnYC1qJO8WvTLjsqDUuTuS3GKdVwWXePXXyNxhChKtQI4krD-PNURlDxRusE9Tyxc0lK0_d0d93fsYP-sD9O11JLpmQtfdCZOURPyQry8DWjG4mCA8HX7EdlGfi7wbW2jzSmrUDDrMnQ5OKKDFnLQkRitiAzJJStRunYMPP6mrInUo-nmMqtUUrK4vfCTO9UP0kJ_4zVNW1V8I695mf2ITW0cX5E_mwXrUSWGRV-buAcEesSfYrlYkKgTDmrT-8u8SIkJzAyvOGxRSCs-YprCTOsCmzkegGDmKTUSdzSutPK9rhS7iXP9uwlcbBxixjdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=p5Dj7syUnIjnbHq3aTCANlnYC1qJO8WvTLjsqDUuTuS3GKdVwWXePXXyNxhChKtQI4krD-PNURlDxRusE9Tyxc0lK0_d0d93fsYP-sD9O11JLpmQtfdCZOURPyQry8DWjG4mCA8HX7EdlGfi7wbW2jzSmrUDDrMnQ5OKKDFnLQkRitiAzJJStRunYMPP6mrInUo-nmMqtUUrK4vfCTO9UP0kJ_4zVNW1V8I695mf2ITW0cX5E_mwXrUSWGRV-buAcEesSfYrlYkKgTDmrT-8u8SIkJzAyvOGxRSCs-YprCTOsCmzkegGDmKTUSdzSutPK9rhS7iXP9uwlcbBxixjdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWhfE8mAj_LuCK1-mDsHc6OxDjK2oHObnntlS-bNDhxpx-tzPjlUnlb5kWzAOIhWMpAfo83zD2hr-QHTWpI2ExYIptQgEcWs3YDwGKt0XCYP4QPynqq-RD0j9Y8q5IwOqwcoFZB34FW4K31u-29nOIEBMNJUOXqmnpMQ6th3ZvWEmBEksXgeHDhXneDiWKpR-VpF_-WLAj80u05aUEay2YHPVjKPjIO-RcdGFNwBqYBGhr0VpIApjXXbP-6uGPuH1jn9a8TNYJeAtgyYZ_aTCrcwfm6a-Smei-ZXAmZ6zNmLVS0RrhzEiCXhJ6-isvQMHz_H6jrV6p5RBII4IZrmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQaReb2G2gRfBgjUk1A8cMcojvF8pBzwnkLePMxMIfsKRz9N7l__Ogj1DRDeRxnZ047nD3x91BiKiQRgmrKMwkQ6Bb-wgcnoa_QosbCc8sIWek3pVY-vh_FTOYuVIKXb8WbWuBjZW7QMuWsoIhhrdJA3KoKpoi9aMkqdpXr4-b0zKuKp2JDPqkQlnYYLK_yFXc3a88g-g9fdplTLxRV_42d51ecRJ1KBiqYrPLC1SZCowXSd_Nt_RphlQnLI6oWot9CTb2JczlPDb7Y9r5QaNYoozAA7b_W_9yfLOF4HEA__gB2nLLdp2IrgaIv0uyZb8VocxEpNje650qa3HrCftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bo2Wo0gBy3DD6sR20FssHuVErfgLvVT9e6lQZf-tJf12mW_ssbZAkaoGclsfZ37QtoF83YormONbspzeQPJDg2auCchHDslSRcfyrp4VvC3rHu8CEW9TyC5iZtntL48PRQN0GrDiKnQzfxWkA30QYBM7Phc-WEw8iFkKfUGEltzX8qCMsWR6zk7alDzVhlt_YPppy9GJo81EU__XXFHIfR1Fk_H3ocd2kxEY7kn3JPRisF13iY0SN_Y6WtmkTOM-xfcNN8DucWIoApfA6ASKo9jWmbmQOfzUlG2MYDbvglLWYh8hb_WDkdSnePiecaJFMKD_UDrwUbPnfRwomhLATg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOqRctx1pt8Xzm21jwfkXseOM2exX4rJS-Dk63h5a3coW7-sbEdH7zuqYCMD5ED2H_ocXtKwCwJFSqT1w9WgZ5btquLmIs3zH8YgweYMJgxf2YCzxoSpbiyPZ8SMSv5DRNbuXZlOcISyoW-jerzAE8Cky8p-XB-NiOtXC2QMb33YKP2GHBTVgDIokQdL520fbUbwIVnlBv17HoA7HgpydM9L8uZa7Nh2KW2hglVltlIQH_-k3RZ42683-QgXdlvRmnUHUY-zUqvozT2WPxSSK6ycBwNNnBp3IbKvLJVIpU0BSyBAxk1--UXTPEv1MyHLPR4i-YIzWVj6IzWGyEgTbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=vGZ1d9ZNN5NfgGjffeml1-zKg7FFThGIC5bqdlJKzDZb2a99ZkdX8caT0_y7a0pdNUg0pCzNMY-WEsgGHX8AL9yDIPmKgQIEKtQPO43DlKboyNflwd9XQNbGFxCSRrRPDkF2lrYUlIeMhihuh0JnAmSnpU3xV2MwxKlPmIVnSIXlOtDYCThRpg-mAhQkK6qkFUc1Hz5NTRf_Lig1VQj3YFKMR_DZ8kq4uanRRNO3cMp3QGrjzI0d5EnU_9_5FOfceQSST4pZdsq6-gHXSWL9Ra9Ek9PjgV-h8_eQPAU9ZUOTbtTw69GehOJhVnRJYBS5jiPwlRzda5FeyQo9YX1WrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=vGZ1d9ZNN5NfgGjffeml1-zKg7FFThGIC5bqdlJKzDZb2a99ZkdX8caT0_y7a0pdNUg0pCzNMY-WEsgGHX8AL9yDIPmKgQIEKtQPO43DlKboyNflwd9XQNbGFxCSRrRPDkF2lrYUlIeMhihuh0JnAmSnpU3xV2MwxKlPmIVnSIXlOtDYCThRpg-mAhQkK6qkFUc1Hz5NTRf_Lig1VQj3YFKMR_DZ8kq4uanRRNO3cMp3QGrjzI0d5EnU_9_5FOfceQSST4pZdsq6-gHXSWL9Ra9Ek9PjgV-h8_eQPAU9ZUOTbtTw69GehOJhVnRJYBS5jiPwlRzda5FeyQo9YX1WrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=fkq32sBvAHB54yo8dUPGRPoDXtJ09K11GzcBsCn_cISSt0SN9v6p4t0n-BYQfQMHV6cclXYZnqwpequ7w1Q2TbQmcMh6MClmb7T6APAaSYs-hSxNRYD3sKBBxuXqTgpWBsC3xEn4qGumN0qvdFJbb6Wpvro5I0PEMrrvLONEO8zWZow0-DbcXRIYmw1wtOOl0vqGDfLdOUwX0URIhh2UjjxQ6F4An9k6FtbFGKqCfjoiS-YcfA321rsKejuz266_4lblM2BfHw07J3NexD61-yXgMRXuO6H03C6fjs3kJ_RJIwJ4o5pQl9lw7wRc_kJKeORsfWillmpwDbIuo6NlgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=fkq32sBvAHB54yo8dUPGRPoDXtJ09K11GzcBsCn_cISSt0SN9v6p4t0n-BYQfQMHV6cclXYZnqwpequ7w1Q2TbQmcMh6MClmb7T6APAaSYs-hSxNRYD3sKBBxuXqTgpWBsC3xEn4qGumN0qvdFJbb6Wpvro5I0PEMrrvLONEO8zWZow0-DbcXRIYmw1wtOOl0vqGDfLdOUwX0URIhh2UjjxQ6F4An9k6FtbFGKqCfjoiS-YcfA321rsKejuz266_4lblM2BfHw07J3NexD61-yXgMRXuO6H03C6fjs3kJ_RJIwJ4o5pQl9lw7wRc_kJKeORsfWillmpwDbIuo6NlgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=FjAZ-MrGQRsa4E0pcTO7IvAvpG3E6uF_g72KesY2P9TtesAgv6pT5kn1l5nRrJ5P6FpVz6DA8c6YuKAGC6j3hhHYta7LWCNq-J985W3_sh6f5pzBZC5dS_NUYr1UaVQOujYnAEi-Ka3j78vGb_b-llrJfD7j2XVcS30VIzph73jteW7Zbs6RCrZMLu243CIk5TqjhbqfhdrySMEufxYgfO-29GXj45lXscmPWytG4buwnlp-iCearmzBT9llwgKTdSMqKgZuZmEX9JgLNv9J4AmiKdSnXL98jSshUStAqFbOh9_cu-1m-fbyA0_woq_MUdHwbobTBOQiFEmfbdkULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=FjAZ-MrGQRsa4E0pcTO7IvAvpG3E6uF_g72KesY2P9TtesAgv6pT5kn1l5nRrJ5P6FpVz6DA8c6YuKAGC6j3hhHYta7LWCNq-J985W3_sh6f5pzBZC5dS_NUYr1UaVQOujYnAEi-Ka3j78vGb_b-llrJfD7j2XVcS30VIzph73jteW7Zbs6RCrZMLu243CIk5TqjhbqfhdrySMEufxYgfO-29GXj45lXscmPWytG4buwnlp-iCearmzBT9llwgKTdSMqKgZuZmEX9JgLNv9J4AmiKdSnXL98jSshUStAqFbOh9_cu-1m-fbyA0_woq_MUdHwbobTBOQiFEmfbdkULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFcZhEPz1nyoGY4TUj5enHTO0Rpz5EmtsPhuOKZMgA3TMac1XxtL3eK6L7yEiwf7VICNzF6q2Th6mJ68aC0RW9SKVGHTCWxwXFXd6z_Mb7FhooGtAMczQObUYFbQDiGUkdZBzBZCRX9V3P07LTc2nXfpRpufXseNUvOb2djwG_mPbYMMwCY42gx6ndehS46Sswn6FTuBZPv3g8KCRcsFIWnp2Iv2wKYbpserLNj0DAJ_34ASAeZmTcxWWmgBTHzGh3Bi2LHwLN6wRvQVdS5_QAfjRdUmkqUJXGCxOKi9VLEXDyrFkJquDlhSxyAFmW9dj1xRsUyNU31cx8cdq57JaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=MP9JVmdkXtfgEiZyXiCotuaWvlXeilOkQ0YVgEPLFMxblFd1Z2UKjrGphLyR4wKxI8_Mqwgcxx_uxCP4U_UnPEo8Zky_73RIBbmc5OrYemCROKkCnKhNUW5x6MdNcLnTWxwUa50KVNTzuZhmD2Dxm6WDG_f7HECkGuqVgKfgXrwoQcaM3S1SoF9I87OhY36AH0LcdPDjft2u9dZS1s_UJhU6RZFP85EfrdWGyFg_DtVMUnQRnGWYvErPS6ASXS895bCd4T83F7rkFpZnCvrHsLdMZfoLghjuspbKPGm698galezOnzMln7gY3wMB8kb-ImoxIVtj9oiXgO-6rrX7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=MP9JVmdkXtfgEiZyXiCotuaWvlXeilOkQ0YVgEPLFMxblFd1Z2UKjrGphLyR4wKxI8_Mqwgcxx_uxCP4U_UnPEo8Zky_73RIBbmc5OrYemCROKkCnKhNUW5x6MdNcLnTWxwUa50KVNTzuZhmD2Dxm6WDG_f7HECkGuqVgKfgXrwoQcaM3S1SoF9I87OhY36AH0LcdPDjft2u9dZS1s_UJhU6RZFP85EfrdWGyFg_DtVMUnQRnGWYvErPS6ASXS895bCd4T83F7rkFpZnCvrHsLdMZfoLghjuspbKPGm698galezOnzMln7gY3wMB8kb-ImoxIVtj9oiXgO-6rrX7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=dqI4_4Cm8HXt0tYF8hDZjDLckWY6KbQfJdLMUTB5MCXmeBZoPMYJ2aWJl7TG9bZSjXRV6Jt-dw_iO84M5-KcneHpOsBh3RupyrBAz142mT2twNufGEdEPxnLGq2JSsv5pLmXQL4IKD8ADRMzxINm-FFckj4oYi0E3NW68eIjBGkDXng5-bvv1fdJvAvHq-_mBXijlpahYB0nifsPQlYwn8CoxoiH0iOssE_DhbnWp7Xe1nsA0vxqX7vzEINUwmERRGR3tmDafU8U1lbIyk2hFhnNUMvzNfMVyq9xH0EhJSgPJH0snArSDcpn0T9X2YCWi8MmHHr2_2W6FfCVneknIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=dqI4_4Cm8HXt0tYF8hDZjDLckWY6KbQfJdLMUTB5MCXmeBZoPMYJ2aWJl7TG9bZSjXRV6Jt-dw_iO84M5-KcneHpOsBh3RupyrBAz142mT2twNufGEdEPxnLGq2JSsv5pLmXQL4IKD8ADRMzxINm-FFckj4oYi0E3NW68eIjBGkDXng5-bvv1fdJvAvHq-_mBXijlpahYB0nifsPQlYwn8CoxoiH0iOssE_DhbnWp7Xe1nsA0vxqX7vzEINUwmERRGR3tmDafU8U1lbIyk2hFhnNUMvzNfMVyq9xH0EhJSgPJH0snArSDcpn0T9X2YCWi8MmHHr2_2W6FfCVneknIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=dNOIMCQUMCxjv0XKjaS75et5xJsHxc65sQoUMO5pNpt0o7pu2wnZJscpFVH6ju-ZlN1Qhgj55Qq969n_s2oECB61fFTcR7lJ62wUMJFgDMioBSMXqxQaLfwT5easY9OPjepuAZIFTFS38VGE_HWaJIku2WjQAIymPxoMQp50-KQIstWMESpEUd-1gq-wocGtlEbkA_srZ4ycIYkkfYt5Yi5mBPRuN0GIcqv-7SWDP4cjGOK-yRk164unt6wIKbhiQKrauG36oyS7EdBEnRF4H9qFyhmjPQ3lIPCvR8atxExt5EPYWWHRg9FOw9BsntNVmore1kjPd7bTOPWUCpFjrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=dNOIMCQUMCxjv0XKjaS75et5xJsHxc65sQoUMO5pNpt0o7pu2wnZJscpFVH6ju-ZlN1Qhgj55Qq969n_s2oECB61fFTcR7lJ62wUMJFgDMioBSMXqxQaLfwT5easY9OPjepuAZIFTFS38VGE_HWaJIku2WjQAIymPxoMQp50-KQIstWMESpEUd-1gq-wocGtlEbkA_srZ4ycIYkkfYt5Yi5mBPRuN0GIcqv-7SWDP4cjGOK-yRk164unt6wIKbhiQKrauG36oyS7EdBEnRF4H9qFyhmjPQ3lIPCvR8atxExt5EPYWWHRg9FOw9BsntNVmore1kjPd7bTOPWUCpFjrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=gxBF5g2W7YKbA_r-AfxPm-gsoLnLiF_jMyrK3bXVsrgUZouga46SdUTvDGs1nGEI1JMqoiSEOAlqjZitNK6_BF60YqU7_FAKUuJjNNc1vPa_Zz7dAdWMTmQnSiRXBpgckFyQNEpSJmWzZcyuVhZzHrevgU3CX5G3bk6bXm2qirInwBS0vBbb89kbraw2iR6u6Qf7pPGm0CJ_3vwt1OTNZBHgx70qGTacyhwHzDIhqnpXeiwQYNAh4JAVWlsWXbfca6FY7rFVNvRleegVpLiPaP6-KzfH4S0En_dlVADz1dvm-BcGf1z9kjRmmCfFBXz-SyLWBb2S-qPewjavJ6JnUTAoboyvInannlEm9ATXNxEVwlIMU0GOS8PT8ZHdV5jJACIcwiQkZHiM3NPyWkFP4zfTgnRbklVDgw-AuilEszSDVAPKHBeS2peBU3qTQiWcCKOUn2Hia5Bx4MkZVv3Eh3pT5XlkjBm-q5lVLWS8jiOA3NXAoF6KEWFIYb6fBQnlKM7qdMxjDL4oTWXslseyCJeYwO-YsSs8kqoEVN5x_z_69v8uP_xhCZpeDWeHzWdRcnkFj5Tm-m-tgRJr7zr7QB5DrdK74ED5OHylJm0ttlp1pd-XHib5gll4fHVqOt4NbeI1KFUu5RK-78AgjbUi8oCBn5AWnAkPjsrAiD2H8aU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=gxBF5g2W7YKbA_r-AfxPm-gsoLnLiF_jMyrK3bXVsrgUZouga46SdUTvDGs1nGEI1JMqoiSEOAlqjZitNK6_BF60YqU7_FAKUuJjNNc1vPa_Zz7dAdWMTmQnSiRXBpgckFyQNEpSJmWzZcyuVhZzHrevgU3CX5G3bk6bXm2qirInwBS0vBbb89kbraw2iR6u6Qf7pPGm0CJ_3vwt1OTNZBHgx70qGTacyhwHzDIhqnpXeiwQYNAh4JAVWlsWXbfca6FY7rFVNvRleegVpLiPaP6-KzfH4S0En_dlVADz1dvm-BcGf1z9kjRmmCfFBXz-SyLWBb2S-qPewjavJ6JnUTAoboyvInannlEm9ATXNxEVwlIMU0GOS8PT8ZHdV5jJACIcwiQkZHiM3NPyWkFP4zfTgnRbklVDgw-AuilEszSDVAPKHBeS2peBU3qTQiWcCKOUn2Hia5Bx4MkZVv3Eh3pT5XlkjBm-q5lVLWS8jiOA3NXAoF6KEWFIYb6fBQnlKM7qdMxjDL4oTWXslseyCJeYwO-YsSs8kqoEVN5x_z_69v8uP_xhCZpeDWeHzWdRcnkFj5Tm-m-tgRJr7zr7QB5DrdK74ED5OHylJm0ttlp1pd-XHib5gll4fHVqOt4NbeI1KFUu5RK-78AgjbUi8oCBn5AWnAkPjsrAiD2H8aU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=CEEULTSW-qNKy0tcs9S_0iboVhh8hElkdPamTXQkcPHSf4hntkMqJa_FB5FwjmuMkkVckwuilUIm6b3anJkaySbNUYfhK1QbA-ot62iWmziP6c57rq7N4A6aJvMvEGwHeicPUJHJDg7_UzKe7uaqi7c0ysZwx0HiUI07CFsuNP50Q4SXK288qp16I9Ao-gP21gZ8EBHPWMsgKw3qVu6hxLNaIptUMiF4a1cTx6fQCjlVQRpB1ATBn38Llm0JCtgGE0tZ20oaqQIzsnO8h8N0mC1J-fYSzWm5w0hVflUkp6Pny0IVc_zsDnSvPZu4pJRx7pzvlgi7GzBVkWgRGMHU6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=CEEULTSW-qNKy0tcs9S_0iboVhh8hElkdPamTXQkcPHSf4hntkMqJa_FB5FwjmuMkkVckwuilUIm6b3anJkaySbNUYfhK1QbA-ot62iWmziP6c57rq7N4A6aJvMvEGwHeicPUJHJDg7_UzKe7uaqi7c0ysZwx0HiUI07CFsuNP50Q4SXK288qp16I9Ao-gP21gZ8EBHPWMsgKw3qVu6hxLNaIptUMiF4a1cTx6fQCjlVQRpB1ATBn38Llm0JCtgGE0tZ20oaqQIzsnO8h8N0mC1J-fYSzWm5w0hVflUkp6Pny0IVc_zsDnSvPZu4pJRx7pzvlgi7GzBVkWgRGMHU6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=iatqJEbq5DHXqwEycWgg2aElIZkD4R8sb6-yBZhccK0sjX1WB9hDN7tT1PWZD9h2v1oBu62T3Y1WhntnoADWig1VgE6tM5Il2MiYTCGeLI9xla2j6PrfWbNEJ-kt8djiKFTwmfTiPMtnSlestRy5BiK0tAAew3vUocVkstGApbJHHwV4V15H7OD4x35EjhwhSEfx-Ik6xqwzerewnj0OJMd2oXtFOlJPS7wa70H4uMAfgO4xsGXNCQhchBAkwCSoeTpPvAKmzhIwhnPaPmYIpXX-Jj_kvXkLjQ3Y2Mm4PLbdV9C9EuCBaJ81ysJDpKMTiKy_h63eAI_pYAb_DFS3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=iatqJEbq5DHXqwEycWgg2aElIZkD4R8sb6-yBZhccK0sjX1WB9hDN7tT1PWZD9h2v1oBu62T3Y1WhntnoADWig1VgE6tM5Il2MiYTCGeLI9xla2j6PrfWbNEJ-kt8djiKFTwmfTiPMtnSlestRy5BiK0tAAew3vUocVkstGApbJHHwV4V15H7OD4x35EjhwhSEfx-Ik6xqwzerewnj0OJMd2oXtFOlJPS7wa70H4uMAfgO4xsGXNCQhchBAkwCSoeTpPvAKmzhIwhnPaPmYIpXX-Jj_kvXkLjQ3Y2Mm4PLbdV9C9EuCBaJ81ysJDpKMTiKy_h63eAI_pYAb_DFS3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvTELUAuCGbhOoc_HFX9d6iYDhSuGa2SMFBUBKOJOI0CXRktp0IDnQRQnWd1OtOsJostFfjhgyn2PHdSvYCbNurKfoFQ_b1Dm9wWNx0q5MTJqAIWkRDYfNoDyc3O9OXfRj6YcGdNy2AcBvst9GgfUATHRmuJRMAnbSqjrbxBXCNzRYRA_-qvh7zdadH6pT0B4_d6_L_9mtkgohaHNLYtpeASLlDewWJb2BYltvhFtY49Ev-g8ZscUhz4yK209U2hzd8H6RUqdwhQENTqQp3kxokSgfgUpHnjGHBG-GTYAjBun8ELeKgkLBi3vvj2d5XRbt5IWupawTKEzED1kyBKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-ZLHFmTAxNKj7683bhMDnFNYBFPNybW-nTEBv9GIXBLOXUkLfehkxCU9GOdkYCOZznawJNvtwgk1lRq-kdrvzLYyCqBSLrQYqEpfgwsE76GkCxiK3RAxGd-RaIaC9bXe8qtWdt2GHEuoy1ygF5zP6skobPrqtiu-rn5t0aBLBXepaF3DoDqc-JgShCxtgvYaHDfpWUUx_f8ONSGaDWptkKtDsw2MAx_OalZBN5BMqlHep4b4LQ03toVNLnoFW66Zv_sPRScjPlmnium6V8dIhCC6c4mA0q3qrj1MoJxM4FJhglBSu96abAvvnzSpep_NidJ5DA25Pw4jaelubIkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=qWXQBBD5OyhgzhvJjXZbZEuRm4feP95FEIqLAWP3aiwGoj8k371eVyIOoeRVKdL5fOIepgPj87omDdJSL1qF5NpyJVMBZWH8s5KHZa4Cfvm6ohs1LugKmJWC4euNJxL9NJSlDheszFMfTRU81G41OBB_IO9xoffiH-dcD6R_UxnCrbulPgllgEc0zPR62ii_fA2RznCK-2ZmZq7s28qDUVN7iiF7FCgTVlq6cq3Ianrtb272-hkxNzjXJIVYEpKqbsMkSSZhuVmhsTNXy60yS7Y1rsgUFTvPL998Faa1mLKEYOck0gQJm0DQe6NpPBsZafIEC-exnDTAb7WZtyqsphEz6yqiBdtNakVtPIDaoOfjeTEqMB1uML_NUhGHIqp0360e9NUfihk_f1mxvV11eqbktSc7i03qxNHWI3RaJVBqDwYjAaTFc7VJP-CxlK0YjY-xjYU6OZv4__lSGzM40gYiTvek_3d1p31-S_Jn_8KYTWUHLVawliRGatN0EosNaA2PkXlEKGGNZ4x7_Xk0w1VJYb-MeKt-e5j6CdoxpczASiARfof0Lu8zRYhlOi6XIJgcyleyCE_2xGwDSoAFgYiOdzgV7M3sq1ak90w6XdCRHqaSME6ReNA6_6gCfdBg51JCh7k5MnBrXhdTWaBIxrTyVpSOHeCnVMZAMoGcrBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=qWXQBBD5OyhgzhvJjXZbZEuRm4feP95FEIqLAWP3aiwGoj8k371eVyIOoeRVKdL5fOIepgPj87omDdJSL1qF5NpyJVMBZWH8s5KHZa4Cfvm6ohs1LugKmJWC4euNJxL9NJSlDheszFMfTRU81G41OBB_IO9xoffiH-dcD6R_UxnCrbulPgllgEc0zPR62ii_fA2RznCK-2ZmZq7s28qDUVN7iiF7FCgTVlq6cq3Ianrtb272-hkxNzjXJIVYEpKqbsMkSSZhuVmhsTNXy60yS7Y1rsgUFTvPL998Faa1mLKEYOck0gQJm0DQe6NpPBsZafIEC-exnDTAb7WZtyqsphEz6yqiBdtNakVtPIDaoOfjeTEqMB1uML_NUhGHIqp0360e9NUfihk_f1mxvV11eqbktSc7i03qxNHWI3RaJVBqDwYjAaTFc7VJP-CxlK0YjY-xjYU6OZv4__lSGzM40gYiTvek_3d1p31-S_Jn_8KYTWUHLVawliRGatN0EosNaA2PkXlEKGGNZ4x7_Xk0w1VJYb-MeKt-e5j6CdoxpczASiARfof0Lu8zRYhlOi6XIJgcyleyCE_2xGwDSoAFgYiOdzgV7M3sq1ak90w6XdCRHqaSME6ReNA6_6gCfdBg51JCh7k5MnBrXhdTWaBIxrTyVpSOHeCnVMZAMoGcrBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGeL_fMNoIIIcMDg1aJRBudL8fHfKYFQCAyx728h3xE4thOKx2uZaDfG6TxbzIqy_OkiE1B6jC2j7WwH4ZdZrMmLFtQIZTD551RYBNFEp308MfMM2Pqday9gV11tq1HrQnuf1g-NzvS3zC-lhOjAYqpK9LDA53-xxFpyeneXE1rccSa0tPNt2zQ83C2JVgmNXYSiOc9bj4qygebkRF_mZS_KLZT1WQHrDlmpXsFy6cjGDhZxb6E8wXbQtaXlx_3VW-mirvZ-XjMEEx9noMa_b7NEc1fVbV4F6KLwRlF3Vremsc9mbKGTfZCHE1B3bsmzoTnHC-50AsV6VKUjSrUecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moDqi0d1_GTy996ebEQT8DKnz0Fs8LLoBm10bBMY8v4ioEgWQ5n5hG_t4zYBLrBcQwQfeVkPf7_A8EcfyeOO_VuV3gsOaoY5Nd_ZYUIKWdB4YOYN2ErIfktzaXXtk_agRfToPkLt8eyyJZSii02yl26fvtLQ9CD_d_6kVo67C1TUf63Co85QmB-bbdSZvGw2eN76vQTzzV9KN_w2cpxgjOTxV28szNPxU2_o4CPA8vPxrXbLkenguhyLatZZH0WCabjABIdpdRN6iPE2GzB5x1wmy5HTsEWxXvk7p_TwCPRzcVLBKxvFeBAtOf1NfPC7yWbvbc5L4ribgPGWY7EcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJCJfRmsLncyz_ohhhY2myFi-aK040wvPo3NQtr3ixzizhhJT3PTsaI6Hwe0rUmK1B8DvaAHea0RKruI7hvteqoKNGMxVnPLZGvn5PMlZrWx8zbRW_Z1oMGgAK4kRQHfUN7itsJlzMoHAIIU5ouN1549sw2ioAPjQOyE_cDn1sqJsyvk8IRx03_OoRefXyfbFgy5MsfwFNBEcHs9kGY1-YsuSfrR1N6WYjZpNal_ZRsy2Irjv_4PEzlzc9Y8-TN5hmhUrcFgYS3kigc6xXH3YFfbbuZpbu58MhkjlH77XqQXwrrPeSuMTbR1do7re7UO9g3rRV--j223sjEVy--iZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns6xU14GRtW4Lp0mnuMXPEZRnMPBiHPLQ0aaUP7svmZF42IyxBrk2h7Isgsn0DzlGlDIyPqfIXMy90HjEw4V3spRic18KgugmAlbI9LOPu__XkePUa-3cHND0jUawNzx4nt79FPYbaLu26rphcezrzcTEwpnWYOFLB7I8oIzzp-1XuyCLOqIA0IBl1tR3LvwRkhtVAXgkU8va53Od9FXFHPAP6oFdq7HA6y_qkiJIkCsZvzhUXuIzOLnUMD5HGMto46p65j63MPohfkUkamADRScO3UEXLJimbd8ZLmH5AJtC2WQYgOQCtPu9Ydn2Zn__WYQw-2TSANcyoD05fGGjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=IL8JPL-CCwCOYmDaXiy1hSgFLsB2DW8ufQZLb4p5XFaV-9aqMGjtk9YmxduIguCj9kbiEY22zf8PfZHwekmi2Gqy6zfPRE58hFPF6hbB24deOZ84MuRDEGh0kMTk7Rg8ziR-age5QFmOqwpEZlSboERmfjD0aHTbog_9AGXkTqblOenBBpPz0dVzSfe525_UtFLX4cSMgdb5SkRicfw4FZoAO2Ap41y8FoYhcZy89c7vU1Ib6JlCu89Gg_4VUvK8JzhOB5MNrFuTMB0qFI_oVklAQ6j359cyisXs0JYXDoMtmDvnZUCj3099GQXyWw5G8xEDa-AjE1qROTEy7DwajyXeCOAFksNypu_eoDQk0VJOCRl8uPq_Cgk8reD1mL0Dboen_qYGt4CyBpouVFuvprqkvwFRVYSjF_sE4hI69wz09fzejd0GxqBAr6PFaYi9KLg-2JcqFgY2W34_MTe7v2cptY4JcYrLKWXGn3Rif13Zh7VN_r9J0kLI55LVgJ04K4D-Khdd9D68KFaMgXupGl9x0DgWVCphD3mhlbOqsTymDO9JwkXMJeCiGeyk8is3Rw1h387cAh1cJqaGF1j8xLNlAHCCi5fYA0GYLS0qm57P_gzmeV97owFLPTJXWPtwHQ1vIFKrBum_s2vgz_5KWjY17Dogo-wdGlOjptykaiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=IL8JPL-CCwCOYmDaXiy1hSgFLsB2DW8ufQZLb4p5XFaV-9aqMGjtk9YmxduIguCj9kbiEY22zf8PfZHwekmi2Gqy6zfPRE58hFPF6hbB24deOZ84MuRDEGh0kMTk7Rg8ziR-age5QFmOqwpEZlSboERmfjD0aHTbog_9AGXkTqblOenBBpPz0dVzSfe525_UtFLX4cSMgdb5SkRicfw4FZoAO2Ap41y8FoYhcZy89c7vU1Ib6JlCu89Gg_4VUvK8JzhOB5MNrFuTMB0qFI_oVklAQ6j359cyisXs0JYXDoMtmDvnZUCj3099GQXyWw5G8xEDa-AjE1qROTEy7DwajyXeCOAFksNypu_eoDQk0VJOCRl8uPq_Cgk8reD1mL0Dboen_qYGt4CyBpouVFuvprqkvwFRVYSjF_sE4hI69wz09fzejd0GxqBAr6PFaYi9KLg-2JcqFgY2W34_MTe7v2cptY4JcYrLKWXGn3Rif13Zh7VN_r9J0kLI55LVgJ04K4D-Khdd9D68KFaMgXupGl9x0DgWVCphD3mhlbOqsTymDO9JwkXMJeCiGeyk8is3Rw1h387cAh1cJqaGF1j8xLNlAHCCi5fYA0GYLS0qm57P_gzmeV97owFLPTJXWPtwHQ1vIFKrBum_s2vgz_5KWjY17Dogo-wdGlOjptykaiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=OvjV6pBvGj14LR58bucc3BfDyQDIIQ5dGYg-styVYqnJALy9rCjTBvrcZ9S8IomyHuBSbBu2R4XPgIecWQjXmfU13FI608Wf7gCtFL-eEc6PsnnDrU7pQmlgwVekO0JqORSd3OXhtO5DhEYlqUqsVd6nUPCH_FD37n_s65riAb-XB9AvceS9dzATAWYzmCsKadHDY5yD82F1L9s8_E7HBDpah4MXUn02bxQwfZe0JCIbH13pohrw2u_FGEOzOosGH4OmMSL4aXce0ZcONrOoSZ0C1Ypu3rCM1HtOPEgN4svLv7foCLUVUX8SnIWlws-eJbAbOic41CPHFUSBSMQlgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=OvjV6pBvGj14LR58bucc3BfDyQDIIQ5dGYg-styVYqnJALy9rCjTBvrcZ9S8IomyHuBSbBu2R4XPgIecWQjXmfU13FI608Wf7gCtFL-eEc6PsnnDrU7pQmlgwVekO0JqORSd3OXhtO5DhEYlqUqsVd6nUPCH_FD37n_s65riAb-XB9AvceS9dzATAWYzmCsKadHDY5yD82F1L9s8_E7HBDpah4MXUn02bxQwfZe0JCIbH13pohrw2u_FGEOzOosGH4OmMSL4aXce0ZcONrOoSZ0C1Ypu3rCM1HtOPEgN4svLv7foCLUVUX8SnIWlws-eJbAbOic41CPHFUSBSMQlgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0uMsZgkDXeu5ytxhVkERz92_XaeENf4gkr33hCorc9d3xxthDiMWDptYAY6vhZBpKmCUC7yPtR5j6jplnOZxrNSiVD2mEiREIda6SUggzkPgjBdTv7OQ-iWjtbdxS-P9qMVNGeHOQLRmJWPbgi289MM9u3Q_HzVKXCd40vm8QIXaIVOvQgiPTik7skwBPMNK-B_LfcKNns1BWrQMl7jr9XBgKq07x_ctlbVJjH0ahgLwu8Oo9huewesLJX7PMLUKWqys7jycd8wa3S3TOTvkwZ_6SndDkMNMmQohlH8opCJtdIxzJK-AjJ_EWMbgeajPvJJL6O7AI3OmbXBMERqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzNOKZS4-xP9gYjC1Ngbd_jfTPukxYxSbPB4OHGqVAyAaGra4DOXMI0ar--9YfSqvNPgmKi3m5bLCNkjkTqh9H6UN7ExNrV55OXqVS4qbUlBx3piES1iZ-KsknloMUqeavG_4xJb2WoYvfNAh6i3XvhCfLV0Yo3ijs_0jYnOAEmt2nCxIPt4UIrNmi8igdQpoURq0hcicv9iidzCQNccwd9p7cSxAWtjKFl6_2YV9rp8p-y6fhZ6LN97SFoWY_XsqzEoXNySHrKqYRtxI67EkVoZVLSLJkVw6r_MIkXzIAB3Uk_DqHjHELX98BRg1CDfVFCfxt9k4F9IwGhvO0mzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mr-hE4wtdqsfLea1Tz3n3Y_temFDgRisyfCAKV2xfVPp1FqX5vCX6YBprGtqT0Mih0uAn6BgQ3vSRd5zEAUKrc69y6w3OumW30iu5XcQtw37mCaab9doWuMdBjzakELp2ZzzrchJ0rRQZO9d2SfzALpMMAcXsCIVyPbH7T9g5hdvertX-x8iU6Pg-aUpGggkBl33wdWfgI7J-p2-bBW02yKE-swiXP8552973whevBC2WTmEgGJqt3ku3rOxHT7Z8DYJZBWPeZLKIKO7uEwBG3r93vYi8mwbb3Fp0pbhfMPz3dbhHqDNTxsWKvY3wuu9WoJV7ysfIvEd_y6O9nY2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sa2Y1DVboHN9otQ-GBdeRiBX7aUEr2yctq0-P5E0bf-l8swWCrIkkQE_x5WUTj0FPKzR8L_Apfr69_qyQQQcrxX9zlV17A52AYjT7QKIYNZjtrkbLqQ-houOkElnlKdG5Fyc9lmxCpwhgQkNUCJ1-PiFUVvZN7CLG7FpcojaC37hZVc3kkcRjFjpUHqpbe-1fJaCIgRC5xbneZQFbXt1BJ3hbT15OAsyLFJDqVw9AT9XpbHkIukLXNfUO2HEg98TYS83Q9GnqZ12lLRZavckv-lijD76vwiB_jvxdbOXgrrw0jcTbqstg1m_bmuzqWRzfMCUOwqqYFrANFVJ1-u73A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCu8RJBZ2yFAMEJn1H6A9as3iMJUP27fnL8AHpg05ihX2vG1Hn4yrdHpVFwD9y2DqEQxWBQHjYxIPZmW4XxFn4VgDNlS1sfUSB9gVLXGVmLqgXbOmf9S62Ld7ZRL3_Ujd0KIBeG8fzbwLDB07u62KZqOYlSw7k-hTyZeH6k-_BloPzhEOEJfTRMg6J7_SunRYVTy_FMxkatcR64JvRezQQNfTUBqL3U03klzt_rP7pSeTSNZU3TdOsgKL2ptFszMtuLBmu8RjZi4iClxZdgiXfpjB7P3j2SzOvuwiG1nam9c3plh01OgZmW8FsD1TrV7R0YiNQX-Qx_50klysLc_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZtLNRvHXk3cID8Z7wgVkDFuNC9WqGkilGc1e5P3WEv3hoyCxl-ZM1RfBvcbJQhWLW1roRS32DWneqo_UMpp6MBqCWlSxdgYLKx9nJziy1erLwP_3bE6Oxz04rDnnjQk086_mKQyLdmvnoa9oPc5iP0V4oLmdaFbyhvAiyABQNrPZ8DP11AmxKOXmZE-Y6c_-theKO7bAsC6d71umdSJm6uAuWhFPKBmCvapwmklxqYsih9dEcsltunNVY_DCCFABz3va5GomMEcEu312bzVlV9KjIrL8txGo2y6USRvW4f6Me_QMaoJX5njRohaHCpnzo8foyzhHqKYCClYI0KwuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOJ2YoQ_IZTyC7Q-FWmtpSn8dZ4TPqJ45vlFiQ4vQd5Gb2_cM3c9fyf-4VT-euWUXu7wrQjn8RjUXSeFEqAlCBhpPlCnXAbVtilEqS0yyw0W_m0AQh03lK73pAxzilVZh00dYdJakt6KvA4YsG-PEH16RLmAxCduQAS5mR1bgGgZjAv6Hx0qI_g5rltQL_PCm9Wcr-2w7vyS_TFMZJpwa9v4jw9BvS5P_EoUiURXAnLD8MdWU9su4MurfENDmmhSe_cGE2DODt_eXKyH-If7iEt29MULPnzQfMwg1VifpJkaBe8yRBLXyCexga_GBegOGVgCVVZWnPI9IX7uS6NM0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=mog8JUUZZOcOZjf1MV15L417kczenrOcl1_CUutJ9MhArxOEqyfY8eaB4oC2JWjjyXf_7bmJ7CEQ3PqgP8QiKwqKOakm8Sd4DiccfMi2Wzgg69XLzt2qtEII5EK-WoDZPBYb6tirXf1q5UpNJU40v1NM1QFIb7GMzLaVx4WdWA6lgZ_J_P9swn_ilY1yhvjSjWZPhCvxg73fFDIw05Qs7XkIshsORkKHCE0Ed4EQ0uBciP1bj6GbQpj0fnvpgUQ8PhDgLI4qkLdSWLnZqisMf-YxnNAU44aZ5UbSsDROAZ-iZ8DrGg8Phx4DNDQ9aE8FkZ7LjZ60_wpexiWr-SAYLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=mog8JUUZZOcOZjf1MV15L417kczenrOcl1_CUutJ9MhArxOEqyfY8eaB4oC2JWjjyXf_7bmJ7CEQ3PqgP8QiKwqKOakm8Sd4DiccfMi2Wzgg69XLzt2qtEII5EK-WoDZPBYb6tirXf1q5UpNJU40v1NM1QFIb7GMzLaVx4WdWA6lgZ_J_P9swn_ilY1yhvjSjWZPhCvxg73fFDIw05Qs7XkIshsORkKHCE0Ed4EQ0uBciP1bj6GbQpj0fnvpgUQ8PhDgLI4qkLdSWLnZqisMf-YxnNAU44aZ5UbSsDROAZ-iZ8DrGg8Phx4DNDQ9aE8FkZ7LjZ60_wpexiWr-SAYLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkxCiW7fut4K2uUzoxkMBrXG5DxdB4dGhEQ4ZTmTPkICv66Q5GXtppiC3pg0tpce4qX-_ZBX7zummaG1vReA78cgieiRjxGyvCJ5gLdhus4ztBZqYjPYo9zsLQdvrTaLiVamy6s_PA0U4QVUpSzKDIYLc99E1RAcys1q1FHgF2CnDAomBX-itMEusGi3kHSCvXOlNVLdth8HU2ZuJijZ_0ilmxXs_c2rn6yU-OI1yjP5TI3kDsSjIW3yyrNdIomnJlWYXVNISelmL707CLdXz0FGUD3XTTIoAFQHlhcIPY64MFhoD7Qj_8-8btuS76PM4yZkinaNxyRJ_f2Oz7VMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=lqFwHtYFkARzjzf79Gmze3KXSo1IVezVqeLpMqnccCKt9jQ57Ua6AZzzSwgpQtSXzj7tYfrAEm9wnUD0HRo_bMblQVR1R_Ae_8Ksg905oSRfr0u2FP4aqhtbSLaNO7uXmtFbEeqabbCqAke3SZhBVPVHqoI46cmUPSAgsOgbro2dDq0RDQF3w80lzGXi-52X3VULNcbs0y8y5neDNe3TunR2N7ZpH2stwbVnXPGYqb4d8h6X-j0fHIUg9MjJ1ggHCjaWnUto25Oi7Ue2Jo5f6pRTeqA17mzO5ltsK8sGXTkWzbclPLIEgCP-Wxj5Lxm4Qt7hfaA65vShpiSonjwkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=lqFwHtYFkARzjzf79Gmze3KXSo1IVezVqeLpMqnccCKt9jQ57Ua6AZzzSwgpQtSXzj7tYfrAEm9wnUD0HRo_bMblQVR1R_Ae_8Ksg905oSRfr0u2FP4aqhtbSLaNO7uXmtFbEeqabbCqAke3SZhBVPVHqoI46cmUPSAgsOgbro2dDq0RDQF3w80lzGXi-52X3VULNcbs0y8y5neDNe3TunR2N7ZpH2stwbVnXPGYqb4d8h6X-j0fHIUg9MjJ1ggHCjaWnUto25Oi7Ue2Jo5f6pRTeqA17mzO5ltsK8sGXTkWzbclPLIEgCP-Wxj5Lxm4Qt7hfaA65vShpiSonjwkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
