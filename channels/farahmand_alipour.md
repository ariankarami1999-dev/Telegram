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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 19:05:58</div>
<hr>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVHNyHPeagSnxkwEfmIrKKeiocZOMLHac-Ampa5iYk4oKWnbnUQ5mmDpj43K9ZZi4ScMe-SFPpbMZp1b374940tv8hyRarAZClhCYlCNkGyTcpRQds0j95atYiMfifXFOZGGgkLPwwPfCRVRR0k1WTNcrkBJMJgZ6qvZk6wpv8qiVbtOlxQqaTASMiclI7q0gZK8jMWIL2hhoGbNqhuD_Jfle6Y9VBm_9GALlygBHfOXYwj9mjO04vM28hgbpjJbAiRy3v1y4AFppInFPv60GbmuRu8QnFNqagehXpjfvLfF9y6oQ41jn-rk4p8tS8jLs4_knXKQ7Fkm41mt_U8Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU03JBBIUrINr83zJT82G-VOKqE8hOi6VDow9Vk_JrqmtdlDqAZ4VWG2z6kPYKYWnTvcu1ghQYhN8YxdE3WNEs-puYUx85kYY4Gj7TJ1HIHBl-Z1qC3StQRjFiHbT7CppiHHAE4v1oZPOpZUMXOfdcUN1h9ilzqqgRBd5aJhbmIOAabbejFL_KnA94YSUmqaZULOPgbThc7gMMVMBuJCRXVs-BoDbGEmpCSNmoXpnK2UBLLuvWLwEo0C_AmejZoVeeOOmnT1FrgCm600e-Zya7Q1SPA1SiH57ooZqksGRi7Mt7Z4_If_Z6p7vDT3ipcJFoN3pXnyeMra1mG0EJK7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6uXN6AIS_5MoIUxC8Y7ktV9p3gNfFu3TR5dpzWtVtsp3ak8GY93NMY5gwTvkLt2EP0AgE26uNAI_5mZ3VS4yzWja7DE6sXcoE56ogTN57GbmcmCRrA99--Vl-uze9Smv4aNX1gBfVF6WnA2ku1E9ydTd69jXDbsfeB_G2edKTeEithmOACjtkYiRBGD__x46cvX0KjphzHYInXTjdn8nNCCb30QIS1IOCAXqrqHtx1rzduST8WOJdn3jn7vio-1fxqGa-uTmg-MMfU57p15zqKAnsO24gUa4ZDerk2oI7emoQCiqoFEElxZX4AGfdV1oK3aX-dd4PJd0FfIrBrWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWTwy7qFQ2leTVpbUv0pOGtqMnDhsmyLo4z-o-7nBI2Z9F-kTUxcrkDAT5LqcUt552dWvAEuWPEpjjnmmQXYZbj6mfmjnjmLYNLWSqh7t_nZiOrsD4hbTQOJ3bPFLJOFM4rY3aS03vNsSYxBaPY98YeUarOaw5NYg--fxUelxAu6kTC0VqWTmUs5mx6BMIScMXFqhTYuPA0aZeumcBVXiLhD_TRtTPrn2kv9ji9Id8Zw7LmmRqigFMptRZ1imxhuFRpwcq4cDbVXFeeDgRFabmVzuiMwHPHiKXCXGuf_jr8lhUkRNi-yVFxHjvTrbzGru2gea75qwjg1ZN8aGho74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmoQU1SJHWKFiRuqWWrJ5VflWt5s5N_bn2cxU9wmKke8h4iTyDG66E4n8tQ339OA1-Q3gHeGPf_PoppA9Rq8mX8X11AHr0LNbcGeTPmYZ_hhyAQIv7g1K15wjI1NxhCn2I17giK_4fEQN6QcrHG7MOPp0jO3f1kAgGKdY20bTHhHqwZmww4_QCNN5XyBpFJpexLcj0kQ1wmAwnJCmGd334OVgGNc2P-Sa_pkmC8q_9NqZKkH96WfURaL118iDNOpHlilGiApauT0NDhhVcL9-ZyLwoSMeZZTn9Wtgx1O5wJNgI3RFyHtThajKSpeU1r9EJ1YoMNxFB28_fL1JkHsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMm_ESU-hX2-8muoQSdzXE_BM4NLEtcn5J7l0m8TdQcx2vkrotM2d1UQIKqF4jF0jExUa07Mh7uCHsUifRB_4a-jgzjPkW8lhcjRTf0yW93aZ2CS0u1DWAfniKXkWiNMIcx_wy3qONuzKNkNeDlimLYsq62QWADVyNtcFqwW5C2SRZOt-O5aZ0FsKNcP-n54YlavS9Sm-sH_xh1G8BxWiVWCZYquEPGjIT99eFkH9Hock734ZczLuRLgWBOPtQ6hRnkZtMgY5EuNecQRI0NpBMzBaRIOrljn6VqsaOvdDmQKpF47Zw8nXGllxmdADVzB9WBvfEUGZPxehtHw0yDfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiWNIn9AjZs81MmjIvrcD9sGrtXBm50rUG-_C4IfxpIVO1uu23zeWLIfbq2TwWWoxFpD88t-B0iR3xT3bzSwqkzuU39DZiX1FUSgqJf1LiaSmAJs3nWTIwET0HAaKTGwcr5Dhx9BubL3uMBRq3ki6fE0rcRQIv7bS5sGzyrXtaEed-nC_n2unAA5d7ztsxu2MN7hUK98RyJ_uksgWzMcvYdgL2c5NgKWcvcUg4M6YUOHOZxZZl2QikX19JMY0kEJIFV0j9ciP797oFNzjHD84Pf1VrzbPP-tYlbB8aKzieOw-S5PS0dIsUcYgRvUYQUEC23L6qif0vILT-s7yJcDwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4PxFPH7vAAHXUyDBl04zZ1dvD5H92_kg7G5JOHOSmdNgKaD84VJPy2RqNLeTUxRvWUDq7Fe1nEOfuKJrjy-XtFvaiqGHc95MOd3hx-WQtj-dTX4znng-t55OehIFRmxKTuCpO13XxtXYDs_x01X44dQCIg55DReHXbdlEAjU0iSaTCsVvWfpSQ_41P8eIzjoMe2VWjd0tcnhEU1npWV7hnJxb28iZybTVft7HHLWiFWrSk67x8io0K-D_s4CygYESPR4afxECxGBpKW9DAXzdvJuMeRiM7-AbK0Noc2YpBSnuA_XoPzY-FSjcryVmjm9aRWAdK6P4TZ5KeO0nEOOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdURYNMej5Y4qC0GwopHF67vnAvk49B3szvP3MkIhEWgwSj62VPgTgUqp6SKfhS8ebApH2oc1b0L0oYA3dd3nNvkaxZPiAX6smCOATY1wgVU3AQ67U6hPZL1cOyFmfbqLuHJorV-luuxjfKjiSgpOt2rQZr8LJWpVoAf-r7yQhxvu92WkO8zQfwV3lHCtDBiOyau_bPmGiCVIHak1b9OYCn38bFVu4db8kLdKHm42Q6niModwrcmABJ0g2JCmIZRxA__JPVrnbC2TWxPCp4HYkkdz7mLYu9Lw2STCMTwYbrhZVBhctff4_gNBCKmtdAHLpwKmJa4dXxT5kYM0I3kkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=AipCGSzs1u5ndlNNSOPJENhmMMiAXdBZ-rjlFkyo5dDNS8_GIT1ZFO0A24-8JNP832tjCEQdYelqQQNpibpLtK8y3qX-o90sfHfmp460JnwZ3DuHaIh11k8gk-t4P1TLNs5fa0emU6PZ-4kMfYKUz5cPtW2jKb6eAUhFWPLbjX9SVBw9GYRIBz0ESnjHYfSp2u1yYpHXDENb5b63OxUlnAna2UTVxtTjYgKp5c7B0t18V0aPEjX0inFCaOZELp_f15YCOQtKBOdWDQ9oWKvBR4jka6c3dWkgq-np1ZqskPkF2rUR99ZOHHLmAxBKLSA92LKxIT2Ua0h6s9UgJTU0CQyP5IuFOqioo1GGcG2yB6b0Ff70sszB01XYX_-lNlLSNgswGTo1r2Jz7loqf6RPlXhdkr9CI3F5WaTd3hS0jf_-7VtzHL74cC2QX0xKdei5LT0r-qxCYrTmXOfvyVAxRFHpIw8sw2Oa40sSADhQVq1EPnPxDVrxX-3eHgrjWD0JWZe8Qc-k3Hddv8ImZ_rl9K8zHBDKFyiFaFg_E4-wDaS6KErGMA6jGd6jmqGG0fSjbK_kCjWaJiXm7ZBFQcePTTzakiOx4Aoh1MoejN_AFAJR4tgNFYpVY_G4SR2DcM4pAPvxYlwevbSNIH8TAmLGvZU1YvzVpH2kbpwTK-8tBlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=AipCGSzs1u5ndlNNSOPJENhmMMiAXdBZ-rjlFkyo5dDNS8_GIT1ZFO0A24-8JNP832tjCEQdYelqQQNpibpLtK8y3qX-o90sfHfmp460JnwZ3DuHaIh11k8gk-t4P1TLNs5fa0emU6PZ-4kMfYKUz5cPtW2jKb6eAUhFWPLbjX9SVBw9GYRIBz0ESnjHYfSp2u1yYpHXDENb5b63OxUlnAna2UTVxtTjYgKp5c7B0t18V0aPEjX0inFCaOZELp_f15YCOQtKBOdWDQ9oWKvBR4jka6c3dWkgq-np1ZqskPkF2rUR99ZOHHLmAxBKLSA92LKxIT2Ua0h6s9UgJTU0CQyP5IuFOqioo1GGcG2yB6b0Ff70sszB01XYX_-lNlLSNgswGTo1r2Jz7loqf6RPlXhdkr9CI3F5WaTd3hS0jf_-7VtzHL74cC2QX0xKdei5LT0r-qxCYrTmXOfvyVAxRFHpIw8sw2Oa40sSADhQVq1EPnPxDVrxX-3eHgrjWD0JWZe8Qc-k3Hddv8ImZ_rl9K8zHBDKFyiFaFg_E4-wDaS6KErGMA6jGd6jmqGG0fSjbK_kCjWaJiXm7ZBFQcePTTzakiOx4Aoh1MoejN_AFAJR4tgNFYpVY_G4SR2DcM4pAPvxYlwevbSNIH8TAmLGvZU1YvzVpH2kbpwTK-8tBlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=No2FNp-8aP_eH5UQinjsOf-0Yv1cvzCaDevGYy3blN0MH13FK7lxFpoJ4uCGU1ozNzqbG4mG6-oWNJ7aIaoLFQdyWubXdMPKfXxyoIV9AIRswRQymsqDgqaH4vK_2e5baDRdbhJmsxYQhzJBzd95jMBtwQjHV8QKFLkkCigUzUdJQOxrrr4jb-NmcrBcEGtnAnDNQg7V6Q_QnrbsL1UzaHUrPzqRCr6W_2tezKS1ASlAsrLaQix3kJPgJLBeVIVXwhWJoJKNw5CRFqzuk4d3hddoU1GyldNeGJVlkUHA6F04MsUnwjIhQrKLJXEUA5yN39Ts5AK1Q6ogA3-MZpUCmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=No2FNp-8aP_eH5UQinjsOf-0Yv1cvzCaDevGYy3blN0MH13FK7lxFpoJ4uCGU1ozNzqbG4mG6-oWNJ7aIaoLFQdyWubXdMPKfXxyoIV9AIRswRQymsqDgqaH4vK_2e5baDRdbhJmsxYQhzJBzd95jMBtwQjHV8QKFLkkCigUzUdJQOxrrr4jb-NmcrBcEGtnAnDNQg7V6Q_QnrbsL1UzaHUrPzqRCr6W_2tezKS1ASlAsrLaQix3kJPgJLBeVIVXwhWJoJKNw5CRFqzuk4d3hddoU1GyldNeGJVlkUHA6F04MsUnwjIhQrKLJXEUA5yN39Ts5AK1Q6ogA3-MZpUCmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz0apyaGlsR1jTcccvP0RFJUdAYuewvXDfx4ZfNdsFiYXCI_FwfGmLL_WaebktkYPSKiEA9zSs2DoeQVH6jn8wujUWm2-1doQB_8MNxz_WR6fTGPA1bXk9NEH61mKWviA4pCmaLLqbhrIk5dofpX_ZbLv08_Ehc5q7aS-26vNUr1xK5xLgdRcOwAZuDyVEog0s7aRoCeaquCijr45Yigow28oMb6VtU5M5Aw5FGKMxcmenzuOtsVKnNzmea6YM_0CfV2oGQdUJ36wN4SJaxXZbrj6kjirR-gEPj5ycVMWw23OH8PisbsZmOjseegDwPEL-id9Q1emiKpGsCoFGT_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGD1Bi9ODSXHBfVMe5tipnhj0uk52mCZzH1P13mjIb4FlYeWiBrEdoHZvShVlGMzeL_9iGhf09Bb935hFV1f_1QETIWJSsWI9YgGsQc1IbJZllOWsn1M3bBHjVWwHPvtnk09a8uZ6_vRs48RTYd2jx7ty-M6I4srb7rd6FN4hjIIWQBUtog9XjsSl7jpKt_GyMOoW_7LsClw4zYcGvytMPgirY-YTGhVVbi9W7L5wqtS86v_5V2nymH7CzUnQnmJEbuLBph0o9ihpSBhLHAFrtDrQmCHxXpdOW8tj7zb0CB97jSqhunFmQGqu7R8ymi6B986mVwojGXB9Y2BuxmFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOkKYzxRFakx-UppIPZ-lrOVeYgKJl6iLWaPNYCFwXujJYRjYFy4W2QGywtaD_x6sKT8AhUnFiWfnq6amauMiuzbS9jUoFiYwg6SsRSJIXAud--UNGnGGT_r5GK-BC1FFlOhePmbKO2S-aj60oOpUCUNl-FbgAFeZh_L8S9p__t0l1fBzWH2BEOr4plno-KwUQEEDZRgPhEZwsCPbzOPWS2_ovFGJg4OuFx7P8gCDtua7_hK45PpCEFi1ymPAnki9IdzfYRFz9u1wzGfhkefWeMGhnob2Nfr5LvGh2v6gKFeIm5Djds-ew57Jo5y_tmgD8-jO_R9AD1FxArRqgpj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvQqKYzwfI56U54RvPpjNQjpLAPdM05iiTgZ6Lo8OXjGJzBVNy_CxcDwmDRxbmALzHbW_s1XclmBsNIGdocoZRvPfNuCFNDvOng9lc2T83MnEES5OQdMq-nNm6hXirSDPqVe2jtyF0jrnFz_yl7UUpk6UBvDhub6HXM0dfahaX6-Gl9MBZJgGVr2JRdj2kYQh8nsSnqEViS5kKoJjw04j2ueXoH_Vsvaaw3_Hkex_QVILspFY9RMgSYkta8x_uVH7-X80nXsIAPdG4CL6kcqAsrjhQMTnN_11CpEb1S69xzh0UHb024sqO6xPo8Y_RsOToepahBmuVCyIJhRUDvfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNUGC94BjClytTuSPBulsFOGgk_FOush2JM7HIEOaWesFL7NLNXBdKy-jmmpaN8QmzcA_68wGTysctE56XTiE2C5FleZZFPCfWdR83IITeK-5Wic1o5GPSDa1Bj9UD_r7LM7WV0S7yhWOAC6VAbe41oiAFMhA0JCctrkBCBVF9VlqZg5z_3Q_SXcskVCk2yuxWQVM0xf4WSb3EmMIgfryZVPpVRLsg02pBi8pTKinlOEdMZnhmv3Ief3G-BKW0JJ-pd0n_j5FD19tb7yL4qpmA53sW9CK8jEMAyGyHGk39H2xow-xJUnrr_YJGzsKGKgQr5ybh8mPyaQX90IP-fkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBAydvbzjYQkQgf04uxq8Dhy2o133ET4cNSAd-vOLJPK6W-hwuAAIM3A2zUgRa2HR6gkvxwWyCQaUCXVHSFgx5KtGBcyUbGtOF-veOeJaegixPcqAH658Hpo26iA-QJc-NPiRC5xcH9h_l9Kb3B5Q7VPHMfIt0E1hCMaLaK6df1Jx4BI3wO74kJsZNqHlMFQqw4waZZFXK8ziH_EYTRXDs_q0eSb7qAZl0Qc7iPWP9Ps42umQ0eNPqlVDU0aqpduzULHu27bgGNbD6aCZktKagszXj7wJ0ZoXwcueI0MoUsTW76hgp0PHGxxjjRjLuL7G-Yf1jaY_VfrWYIW403XuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-dSvyc1iJ2LzpkL7uJUtBHLX1px9ZC3BNXYmQHzkMRLiEqPkqP8bxLMTHBUuUQ0nxusHb74303mrSr6aX_wV0KZiVJEz2tW45nosTCQHXiVm31isj71R6iUYEPnCHYkyUCG4E1xhp1Hf6gOU3U5ogogibPlgYutWYaGy8Mt61eD8lz4D-aCfsTvSQH6qLi5pEcYSWxjXSQXsqQmWB3db7dDzydLw1iVJkd1f7AeUd5YDkhA9xZ6dAHIUeKJ2EhMHqv2mAfycJO1nA8_MpitoWUxSThq08xoY121WpJReORLzYd3Zsov_iesymBYFq1PgjTelbWPlvuQtjF4lmnihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njmdgTpbPpZadEYDeGKnNYzqwid7dfTWWjawyE3f3WAbZshjX6SZx1n1rhC0qekxVl_9c-Sn_vK53j_nGCDqT6eT7YiYCAua619u5hmhw6XZRKDEAb9OFv1WjIrUHTc-xBzfD4Z_Lg6zp-cdOhEpsRKLa7YN5bfNOSY6Ls7sTZd1RFJ9d18Gpg6gNy0XlizN9SNX12VamrbcPomSzfZeFGgSf-KXeiKx7dxK9Oi9Hr8xh5qVgTGDAYFFDTTGYVZy8THHOTEOo1IpgHPOgU5oRokEsK9S3exps1SCVQ-SRBrxDRZnsesXCt1Ky4LENL89c1NkbkmLKZBfrdQhUWtfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=mINVlZMMiap-i3AO7zXTW5U94OZY8uGnNNe6Aed28w10iwqYQIN5dqxlRG4FItY32CQnLxRRtwHmSFVc7QDb0RGktetovLVQvJehDxGjgQZJ26m4n1tQL3CSFZtfSgA5Uu5zZN5CXBcbbqXj8VLskEiW8hQAKjxjQJvRWzwHbgbHg6vHT_mvkH9KnsoWJoL6x2JbAo-rI2BXY3VskdqKmXVDVmvo_c244tmcVGrRDHa-KycP1SMFLyWkfNXCiOwttBnZe20miWd3fdw4RcTzF3N9p3Dsa8MPn-i2OF8YDvKJFXSW1MVfcFypnvp9SHuMzhoNwNySEYHxSMTu-b08ekUBPWAmdy-j_yrleAhY2eXm_mnx7p4Ty55p33u45o52lC2pcofUGYZkfbF_DdM717x5dRkiTBwaanAcF-rBziRwLa8W2xdAqnRcmhYZ9CnrIOSEn0w9-IE_ikXuz0lfhOflglluZ3SHcQeTlzEt4vRUdV5Z2S36jxQxsC78nqdCbH49Vesj_1RM5eQdRMb9c7nuQ0BexSnTg65WzjhbWtknS4rJe9QTZfXlph6HsYp1PQx6k0mJ09cxZWWa3Z0edi3J2ONfLVwva7DsYv6kmQvr9ybSmpnlDMIac5P57FNKPXY5rn3jtkmhgnPVB_PZ6xaOlrTEPG1qtCab7H89hYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=mINVlZMMiap-i3AO7zXTW5U94OZY8uGnNNe6Aed28w10iwqYQIN5dqxlRG4FItY32CQnLxRRtwHmSFVc7QDb0RGktetovLVQvJehDxGjgQZJ26m4n1tQL3CSFZtfSgA5Uu5zZN5CXBcbbqXj8VLskEiW8hQAKjxjQJvRWzwHbgbHg6vHT_mvkH9KnsoWJoL6x2JbAo-rI2BXY3VskdqKmXVDVmvo_c244tmcVGrRDHa-KycP1SMFLyWkfNXCiOwttBnZe20miWd3fdw4RcTzF3N9p3Dsa8MPn-i2OF8YDvKJFXSW1MVfcFypnvp9SHuMzhoNwNySEYHxSMTu-b08ekUBPWAmdy-j_yrleAhY2eXm_mnx7p4Ty55p33u45o52lC2pcofUGYZkfbF_DdM717x5dRkiTBwaanAcF-rBziRwLa8W2xdAqnRcmhYZ9CnrIOSEn0w9-IE_ikXuz0lfhOflglluZ3SHcQeTlzEt4vRUdV5Z2S36jxQxsC78nqdCbH49Vesj_1RM5eQdRMb9c7nuQ0BexSnTg65WzjhbWtknS4rJe9QTZfXlph6HsYp1PQx6k0mJ09cxZWWa3Z0edi3J2ONfLVwva7DsYv6kmQvr9ybSmpnlDMIac5P57FNKPXY5rn3jtkmhgnPVB_PZ6xaOlrTEPG1qtCab7H89hYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=a9HiL7Hy3H7Zeo-tCY85GpuLKK7jKS4X--D9EtLZiVEi4p2IFe3H--5k4g_HrYUu-bT390rGi9-GWnlrF2EUXGwGlUfDhbOc8K1mq6uDWC1Lmm5t--yIxlmpi6Gu1j8dgAmBrJByoBKT9HjM1J4S7vKlvSM3ry_OI_kWodQkEHV7-dGVTM_aIJ-JN6FSKNTYtlYIEVVuXAPkD8UotFhEplbu0TrlkXGsvIZCQjPYy2O7mbxJ496vZn1KsB3ZjIn0USg53cWqjUtI5UcpWv-1_OrTSUR_YQNS2Xe3lELOj166YttTHyoIuxSBN4jCdoBE6_lQtbwpDxApENVYdPyxxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=a9HiL7Hy3H7Zeo-tCY85GpuLKK7jKS4X--D9EtLZiVEi4p2IFe3H--5k4g_HrYUu-bT390rGi9-GWnlrF2EUXGwGlUfDhbOc8K1mq6uDWC1Lmm5t--yIxlmpi6Gu1j8dgAmBrJByoBKT9HjM1J4S7vKlvSM3ry_OI_kWodQkEHV7-dGVTM_aIJ-JN6FSKNTYtlYIEVVuXAPkD8UotFhEplbu0TrlkXGsvIZCQjPYy2O7mbxJ496vZn1KsB3ZjIn0USg53cWqjUtI5UcpWv-1_OrTSUR_YQNS2Xe3lELOj166YttTHyoIuxSBN4jCdoBE6_lQtbwpDxApENVYdPyxxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCroihazUF4cYiTkNPSMLvQb45krhS6F935Be3R_PWgnFxKreLpPBf6q7A0agPhBaKCSijI1LnBib6z0EG0UAf67eUnKGYsLkLmW896v_6wM4wZEOSxRdaTzomVlN6hUfcUcyfGcj8fq6zWg_7_L2QaSsAtuywY35UEf-4JdZrWRTLcpdJsYir9onL6bVtZrBqcm29eCdmZgTCVxfbNBFKdLwlYYotLT0Pe8nQW3MAUaH3g_M4I8UQAkLak6VF-KNPcSOuHV_6v5RemMw-3-I6lLsVCFdvFkeZhd8g9wwnO7az5Lve1-bZRNJG_Zt8_louv3qRUKX6F2gVK4rHDu5PyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCroihazUF4cYiTkNPSMLvQb45krhS6F935Be3R_PWgnFxKreLpPBf6q7A0agPhBaKCSijI1LnBib6z0EG0UAf67eUnKGYsLkLmW896v_6wM4wZEOSxRdaTzomVlN6hUfcUcyfGcj8fq6zWg_7_L2QaSsAtuywY35UEf-4JdZrWRTLcpdJsYir9onL6bVtZrBqcm29eCdmZgTCVxfbNBFKdLwlYYotLT0Pe8nQW3MAUaH3g_M4I8UQAkLak6VF-KNPcSOuHV_6v5RemMw-3-I6lLsVCFdvFkeZhd8g9wwnO7az5Lve1-bZRNJG_Zt8_louv3qRUKX6F2gVK4rHDu5PyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTlQf-kvVTAmzCaglP1BIjYEP3EOuR2I_x6_zVtPCvoL3MRnBUhXTAA8HGWXgcd3EXzTKIyVLQ5rB6uBCt9bo2q9YOGVdtAWPliXgDMhBcuyjWcUoYF1CoPVnZt5QNecncpFtsHLAfQN5zZjOgb9nh7tpGwEaibji6_3FGDhFbpwqmrxAIWD_Jkxd20Pf_cYry7gs-Yh7oY92XHc8dAmehRr24ZtOn-oUlVttxFW9YHcQUD6m_nYJhxVpOKVjsCCSoWYQKpkzoPjuMEX8cdaYzgGi0ivBqrjydLZKSuxP92F2w9k0_R1IA6nJvd9nkh0EoBtgXOap_hISOK_6sX5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGkMczk1321iZRPaw7femqsCyPMHwtS7DBzc42_X5N_0sKqmeznMXMdwsgnEo7JeSXUrcHogQs7hUnKhjCRKlpTon0HoWCrFRm91hcNw6xs5oYo01Lg0mztqxoMwr6sshotHhIxN39qJPEIAofnRuCPVzH2y6F8z12WONWQaubsXf1hkl3H7yqPpwIN5ND0kvuOkgzAcpaPNsK263t7Y20kbToIiF2wOuiIWNqSk8HYQkD4j2cWSY0_EdxRvh4LxrJ9Zb11W0qCLxCmlCJrBoBzLkq8vcYytwuGejCPVwMbt-35dLHXrXoCunu_Qw4hF-sO265yjQHiA5emvyrhW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxZew6lBtyLeKQOipJlIIBuSy3xUWFfuFhWNpTAIJkjtqHkTx61mgW84WzxC_kEFIrI6FjoIl8Ym7_ysDn0pxsa4-SUQVW3_tk93tnYmRiBYyMJ5lC9-nTMXElEuHhfa1Pc_caBsgbI1QRXjBoyH6QejHMsjOWedSV5Q-adxnux8i5pA8c8sTftJ_ciHqitaM2-kqMwAQ-YkdJLpOKrWuKMcXx0EVUudb9YtpfdVXAG2OGf9Q_-SjPYte4x1_wcUNz-QEQxOfdgQeptSUr0uRQXT5s5EZ4bU_J593XW6ttkUDZRLGrf7xrs3Vo1_zLFPFy_LXEjUzM0nfGGDYtwM_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=YgoiyhknMx2J303HNyNyEouo1O9VdmXYhislazdxfH30XhCjfxQbw9Lw_X5-O1FRKexlvnshPuIVYx-v06KjSkdYLXyCIdq8Ja-GJE0SO1JugNXySyQop57_V_UhGCY2LnBcGYnSNxB4digX00RqR6DujcgSoxPd7-IMwaANw85L9vTPXVjIchMzsLbqxylIljyum09OZ5COZSpdB3hi-isS8vvZwlhRvNaDeKHhBFA_ZVNaihtRe2fK0hCPmIufBF07HkSw2GEZaJL6KCElAoiirSCCdyHuvRMoyaRn2bdSOinWpgM2PMX56Pf-vCqwzwhiR39AyN6lpA2pT5OBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=YgoiyhknMx2J303HNyNyEouo1O9VdmXYhislazdxfH30XhCjfxQbw9Lw_X5-O1FRKexlvnshPuIVYx-v06KjSkdYLXyCIdq8Ja-GJE0SO1JugNXySyQop57_V_UhGCY2LnBcGYnSNxB4digX00RqR6DujcgSoxPd7-IMwaANw85L9vTPXVjIchMzsLbqxylIljyum09OZ5COZSpdB3hi-isS8vvZwlhRvNaDeKHhBFA_ZVNaihtRe2fK0hCPmIufBF07HkSw2GEZaJL6KCElAoiirSCCdyHuvRMoyaRn2bdSOinWpgM2PMX56Pf-vCqwzwhiR39AyN6lpA2pT5OBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6cPJ960bxkIGTWay4uHka3MAvkPXoqGMQoTKZNUn5NX0BsGFWGO6HpZDT7qjKO52rI7JUliHUnM3IgFe7ChXx50vWCZ7Q2JNqCiFw80kg-rB8RrvjE7_eckOamZpjxXKRRyr0Qjqe6as0VzrtfY3FQQ9YyPAmKHdIMRRk5VrhttZBizGEpfjwUJvr45d8BqKvv8zTHY_7KQ05OkLKD7TBOKwQYkMvdoz25iSyHlqqR0z1tLwT1Sa9kwo6QBufM0cwIRVzKD60duHPdFsnjLgFd74CL9DG1RafiQO_fu8DoPvbCxE11XsG_-suNIArlMsw22jhVzywWDtxMgI4GI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ll3tPfYx_Cz7VZ9ftUijSRGSJIDmLHZqkngGYGHo45rE7f2d0b5Hr4HKjUOxRJY7m_SaFpYmeoyrcPLpXCH_k8vbvLdZ2MKy223vwao-Wz5IgLaxBnKshySU2fy_SECPslHmPbY2DlhISXlgjbCPkG96EKwMeDuKS60rSXXeKH8-KtaXyCie1WWFV0kzjw6W0lPSxsY8YQgaPf6x20z0Qn1TGkawE2vV0jPmyD2L8ILoH6aw2gaOTrGGi-zDx_kTJsFL4AWdLfAz8frLV84b9NZ_f6d3FlnXBmYkvdzzPxF4ZdnAPgtE_sy_C3m--0F3z8bI2kliDEinm22CnC_IEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-akej99E-EFp_-lFvDhNmiVZkvApRSJ0QM1O4tlFj_vKuWQHa2coEo4FF5NOoqLgR6eG_VZ-j0t00qCywt0T3VE5lI9gHb9rJhHDSGm7xHQvvEnsbFzmTrIuN_VRVHiuIThNBxF5X_KDjCVKdplsCaURiByPfunbxof3NPp3TS8oRmlt4TpZRC7MPwHKomJ7_2pbTobfODh11QwEW0hNLhZ8O35OJhIBbTgZYgww9sJHq1d64thjPNmzNa0HqsfgKvJ72h3VgKpud5r1UZHepkCWGX1ALf0z4LDUloH4RFo9PUylB3yjRR9Mxqn08mTboGBOwf-EDk4l8KDHLWRJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO7naqmik26CLE8muC193RSu_egPNmOYo55hqA2zpiA-BnwsRMLNRn8RFfqaFckmrC8445GkKWk96pYxYFD7tCvIzbsyDOKwKrWot5ISJ8-nXq8_hfFcYdw4hYvGNwlq1KyuBR7vHEifOep-WEJsw2e4YXHSOXcnHcdX4jgYWyTR4s1uiGd5O7LXjjNyRk4FuenmE-PEPRblrdluA4XnLy4Q9B7SIA0lEiy0DBEc6HVRfrS9QFdtekuxwGHkAGLUT0cAtCzDYOIhrjK1z-JU8GMZiOI1WPCRJrBH0fdzOBbegUOqPLUw5VipHEFf1M0LEisVayykTnzQpQXHds6dzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=cqLEaO0XTanqPmW7S_-KZUZpaCybsaj3fg1vD-JT2ZsdmP7IfTxmJ6224UMz2kGAkij02cywP5_0iORssuanCvbOVAelyNs7igyjz6BaW6-9wE1EAA12Kbu6lcSLA20pqxQA8LA5PiFAaDQP77bDV5sn_tagQAlQwqp_cMmFL17MfkR5Q1aw4IACpZ-qGFQ3ifDxiSukkRsQyWjGtulGmGhF8XnSu0twEayIyapw4zk_1j1qqCM-dmTkhjUeLBR6YSI1c1gAnMU-Y_MHq4oKI7EUm5K2dl6Brue_nfgogezavViBodvrem-s2n0KaDk_FgOuymHdnMWCjNv8-ZIO7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=cqLEaO0XTanqPmW7S_-KZUZpaCybsaj3fg1vD-JT2ZsdmP7IfTxmJ6224UMz2kGAkij02cywP5_0iORssuanCvbOVAelyNs7igyjz6BaW6-9wE1EAA12Kbu6lcSLA20pqxQA8LA5PiFAaDQP77bDV5sn_tagQAlQwqp_cMmFL17MfkR5Q1aw4IACpZ-qGFQ3ifDxiSukkRsQyWjGtulGmGhF8XnSu0twEayIyapw4zk_1j1qqCM-dmTkhjUeLBR6YSI1c1gAnMU-Y_MHq4oKI7EUm5K2dl6Brue_nfgogezavViBodvrem-s2n0KaDk_FgOuymHdnMWCjNv8-ZIO7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=nhL0LNw8tSHm0hHfeHWX9NplXd7oJVRUzL8urBwZDGvAMzoaAPC2qD59WA_no6L-6k4-DY-jtDnMP-3KBtznVUHAHn1G5XVb2D7vYqo4AykzX3K3XQ6JlOJYMXYq8Wf0zLp7MfaERobcXulxfkA-UC_KOSPQJUFIEfYQBmIkSIo42nqFVPD_qZqXmZBtlo6cE4L7vYF0B967FsW9uHiQpaalbeaLk3fI2QrtEt3GdT5Z0pHgJep-rpl-scWkF50y0CdcPnbHECL_9Ab3HCuj-Zlh3Sr7DMwtvYHBjGQzGFlWXEQBgseJ2WqFMcOwCSj3qZWKrgKyq481hauELMNmzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=nhL0LNw8tSHm0hHfeHWX9NplXd7oJVRUzL8urBwZDGvAMzoaAPC2qD59WA_no6L-6k4-DY-jtDnMP-3KBtznVUHAHn1G5XVb2D7vYqo4AykzX3K3XQ6JlOJYMXYq8Wf0zLp7MfaERobcXulxfkA-UC_KOSPQJUFIEfYQBmIkSIo42nqFVPD_qZqXmZBtlo6cE4L7vYF0B967FsW9uHiQpaalbeaLk3fI2QrtEt3GdT5Z0pHgJep-rpl-scWkF50y0CdcPnbHECL_9Ab3HCuj-Zlh3Sr7DMwtvYHBjGQzGFlWXEQBgseJ2WqFMcOwCSj3qZWKrgKyq481hauELMNmzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=ck-4h1Dd8XxJcjeIJehRMG0qYzcq8rXsNHP1a3liIdiFJbTsJXJCrDpKb_7dM2jIAsWYfkoHyo0kBtaC1sT8UBcqENncgoB_k-FFd6dmvPk4p3wrMPAgre0OTXRJVDxEBd7WeBMwMnXbdqa1i55jWsag_rG86X2FtyFC4uToxBwDLstzOLSZMGDmjjBpr62_nkd4mXbIaeWNLbGJF_VjDrQLGBzkviXclJ9vMlT3PryuuCj7QjkSSD_LJBZPYGsCYMr6vPrrgPbXLYgxB4G8XAB4GsCHgZFgMg5PLSYIwrw_jLB1gDP1gPMQuu6_IDPMmsXWOXYGcm3rd4CVD3jLWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=ck-4h1Dd8XxJcjeIJehRMG0qYzcq8rXsNHP1a3liIdiFJbTsJXJCrDpKb_7dM2jIAsWYfkoHyo0kBtaC1sT8UBcqENncgoB_k-FFd6dmvPk4p3wrMPAgre0OTXRJVDxEBd7WeBMwMnXbdqa1i55jWsag_rG86X2FtyFC4uToxBwDLstzOLSZMGDmjjBpr62_nkd4mXbIaeWNLbGJF_VjDrQLGBzkviXclJ9vMlT3PryuuCj7QjkSSD_LJBZPYGsCYMr6vPrrgPbXLYgxB4G8XAB4GsCHgZFgMg5PLSYIwrw_jLB1gDP1gPMQuu6_IDPMmsXWOXYGcm3rd4CVD3jLWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mw8JU7l9SEDzXqBfLfQ5CuL8_vkhWfxcOYQ1KYofXV1pZKh1j-SyQDwMmzihrRhjKbrrX3FpnjBrIdcY4M5e-u1JOKWl2_wYdQPH9hpp0cHZo9ctPXnhcPF86XPIlkYfpfzUkAT5IpAuR6f3ZY1_o4UZd-nC8eHQTkdfW-T507UcdAps58d3CRN7dC27vs6OJkdJUjXQNRiOVcyg3nBWbvpYauInsbplNeIgsC4fv8rFhSqjjRyhgHL-sF0puymqSf_MZbirTYan5ETh0L-pnD4mSobGZL1lgXpb4bLv85chI4Byw9-jtXnccwuI_bGr1msc8fhxW43sAxyvWPvn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=C0bZCW1kJI9RUgaUBTKmRIrPSBzPG-CB_WNMj9fDuwNNd_y1mdRqsysJxUU0mC4virO-q9v2AwWs2Zh7xGPsAYE_dXXp6pajo3Pym9f6kY0-bg3HMlxCOP-lKBIBAvWh_e7kA5XA-LjYkF6UiB8JfM8fScAyMjx3wMeanSwiPWKQhjzqyz_e81pw6sJyKBBpYagK9vrtR1S-5FDFeINfkZjirbWeFLL6upjydeH8Mlh18gI0smXKqEp-MwCLBkLYKKlXZlEmt5deIIzNQ4mjC9wOAxMqRyDqKFxdofBpBIj_9oDsHR4o_nssoVC1KYsczNQCPPV5vASqzkGQF7tiOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=C0bZCW1kJI9RUgaUBTKmRIrPSBzPG-CB_WNMj9fDuwNNd_y1mdRqsysJxUU0mC4virO-q9v2AwWs2Zh7xGPsAYE_dXXp6pajo3Pym9f6kY0-bg3HMlxCOP-lKBIBAvWh_e7kA5XA-LjYkF6UiB8JfM8fScAyMjx3wMeanSwiPWKQhjzqyz_e81pw6sJyKBBpYagK9vrtR1S-5FDFeINfkZjirbWeFLL6upjydeH8Mlh18gI0smXKqEp-MwCLBkLYKKlXZlEmt5deIIzNQ4mjC9wOAxMqRyDqKFxdofBpBIj_9oDsHR4o_nssoVC1KYsczNQCPPV5vASqzkGQF7tiOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Fs-eJvQT2f9TxkTklv-M1hSGjLJWjQJYXgV9bnVeZ5xOrc0nXu5rLOOwP2aUnZYxWE-d24O8CFlXhQSXAQgiZrQtECDPjprt1fgqpseft9k-BeyqouwJI7DEaWaIqxsHFWmUFD24KhdIoNu8r0BQomnRcyBwf-BLYR0JkB6NJsRADVh2_8JHS-__8B531Pa1fOsGw2LbcsWLuS3XzbQs2kv8_FZ_ZcDwEssNzjsn0iEmX2XQAqzHoDTCR2VdYWB6q2vZHiYj3xDumDF3dF54dDAyc1NNeZaBmoSpFmouaYwgATFcy6uz847pQ1SS2DziifAOyQAqy46ynL4-u1Hcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Fs-eJvQT2f9TxkTklv-M1hSGjLJWjQJYXgV9bnVeZ5xOrc0nXu5rLOOwP2aUnZYxWE-d24O8CFlXhQSXAQgiZrQtECDPjprt1fgqpseft9k-BeyqouwJI7DEaWaIqxsHFWmUFD24KhdIoNu8r0BQomnRcyBwf-BLYR0JkB6NJsRADVh2_8JHS-__8B531Pa1fOsGw2LbcsWLuS3XzbQs2kv8_FZ_ZcDwEssNzjsn0iEmX2XQAqzHoDTCR2VdYWB6q2vZHiYj3xDumDF3dF54dDAyc1NNeZaBmoSpFmouaYwgATFcy6uz847pQ1SS2DziifAOyQAqy46ynL4-u1Hcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=S8KGElbBSPbQhiiEWNlAc-UGlUy1jT6UQIBQ0hqPBNgMtqKW7LIhdSuy6YE6Hoqsch9xeElgYTWzkBjEyQJUhD3EqXVWV--W25-ipY1DzuHRVIIkjjflN2x6Tpqfu8U0vm94ah0qPQZofSwYTeYiEVuLhyXNRNBHlxZ5HaySHGbkXoineIvZDagPD61-XmJrtEzCcx0yZvAGYxpQbxGNxsVjw-qhsUGQfHGDCmgUJ8AqkL1b5drQBxyx546VWP-TP1-MpHYqysBKxK0aWmQ_F5QFJHJumaPmPsYKoGl_51jbOidaFpBnVixQZq9Sahs8Hjpkc9F1AMvqLFfKJwnkbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=S8KGElbBSPbQhiiEWNlAc-UGlUy1jT6UQIBQ0hqPBNgMtqKW7LIhdSuy6YE6Hoqsch9xeElgYTWzkBjEyQJUhD3EqXVWV--W25-ipY1DzuHRVIIkjjflN2x6Tpqfu8U0vm94ah0qPQZofSwYTeYiEVuLhyXNRNBHlxZ5HaySHGbkXoineIvZDagPD61-XmJrtEzCcx0yZvAGYxpQbxGNxsVjw-qhsUGQfHGDCmgUJ8AqkL1b5drQBxyx546VWP-TP1-MpHYqysBKxK0aWmQ_F5QFJHJumaPmPsYKoGl_51jbOidaFpBnVixQZq9Sahs8Hjpkc9F1AMvqLFfKJwnkbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=C9pPVRKY6SgAysJ-n2ahDKJprBaP_L4z04LKmewcbQD20zxrIvRMPqen7JKZQhERmPGgtEH3xS90DS7N-8F_9zICqFKsZhaZpowQYM-kJ79iZFqb35AhC0Ce_SFMUu7AoOLSmuyZOPFOeiTd0bnvLq1ZbLUqYMpheIyEelmghUPxAbKciuH2z8-N-EuTjdSg73qG3zYwUwceAzA_ApqoADRUhTzxSIFG6EFe78zsiWkaYuqAJ7tDmLH0eslAxKjqL2CAgrAwpa2KnYdU1IEUCenc3tE_AKbWcp0vOr6cG3Gmzb-tQl3PCOz2SqHnmttzAy1FbaSX-GFM2K6WJajnHSnynYVNRzXqp5xMYtCzrW0cYWzxiTgVBJ204bJ_r8yiGhM7XuhoOzBV5gVmVqOxR7bXZgtXC-dN07dm4IhdUe9tx0tBMx9jTiyziqA8SHWPWfrvnh3HN1RTiNH_qHwpna4SwwWH5lSqZxR6HDK6wKEiLgSebmhFZUZqhBPGtUxDTv9D7cBq5b2njWud4-gw_tqN4joWv-7yWqlrKB4eMCcdoqB-eOCnWxswMCClKZ1Ehr0OM-vRHQvtzygBQujnDEJpNMK8sYcnMIX4pfFYbI43amyydgaBpnEwh7nYq5IH9MMc73ejSrsE7oll0-u_BAL72nC9sO_zrMifEMgiKVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=C9pPVRKY6SgAysJ-n2ahDKJprBaP_L4z04LKmewcbQD20zxrIvRMPqen7JKZQhERmPGgtEH3xS90DS7N-8F_9zICqFKsZhaZpowQYM-kJ79iZFqb35AhC0Ce_SFMUu7AoOLSmuyZOPFOeiTd0bnvLq1ZbLUqYMpheIyEelmghUPxAbKciuH2z8-N-EuTjdSg73qG3zYwUwceAzA_ApqoADRUhTzxSIFG6EFe78zsiWkaYuqAJ7tDmLH0eslAxKjqL2CAgrAwpa2KnYdU1IEUCenc3tE_AKbWcp0vOr6cG3Gmzb-tQl3PCOz2SqHnmttzAy1FbaSX-GFM2K6WJajnHSnynYVNRzXqp5xMYtCzrW0cYWzxiTgVBJ204bJ_r8yiGhM7XuhoOzBV5gVmVqOxR7bXZgtXC-dN07dm4IhdUe9tx0tBMx9jTiyziqA8SHWPWfrvnh3HN1RTiNH_qHwpna4SwwWH5lSqZxR6HDK6wKEiLgSebmhFZUZqhBPGtUxDTv9D7cBq5b2njWud4-gw_tqN4joWv-7yWqlrKB4eMCcdoqB-eOCnWxswMCClKZ1Ehr0OM-vRHQvtzygBQujnDEJpNMK8sYcnMIX4pfFYbI43amyydgaBpnEwh7nYq5IH9MMc73ejSrsE7oll0-u_BAL72nC9sO_zrMifEMgiKVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Rm04fXWIyj9thTKIct2LKJrzxZkaNSu7Kcc4GosJ5vSfUw73nAjhWsDCoWQuk8-61pwqdkA347eJrukxA87dicSz7pgAPj1HDdSqaAzN2nvZvfyb8OHvjcVw8iaDwzLYMAtjxyd9ahBlhmpqsfgjj5ZbYyZweuJYOYLdWLsC0uGDhNTF6K098hQWvBZAUmdScO06dRmz-t5FnjT5bsu9ZGRtg6qaPev4ognqFZxa59OjIxgR-kKxgLUJumdoqqhbnfI15G7eiD6nmLqDXCZwWNk6S2E1EvoGsArB-xWz3tqqcrCURARbOTbEVLMzDYDEq6fM5KUOrcbWg0L8NxFWCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Rm04fXWIyj9thTKIct2LKJrzxZkaNSu7Kcc4GosJ5vSfUw73nAjhWsDCoWQuk8-61pwqdkA347eJrukxA87dicSz7pgAPj1HDdSqaAzN2nvZvfyb8OHvjcVw8iaDwzLYMAtjxyd9ahBlhmpqsfgjj5ZbYyZweuJYOYLdWLsC0uGDhNTF6K098hQWvBZAUmdScO06dRmz-t5FnjT5bsu9ZGRtg6qaPev4ognqFZxa59OjIxgR-kKxgLUJumdoqqhbnfI15G7eiD6nmLqDXCZwWNk6S2E1EvoGsArB-xWz3tqqcrCURARbOTbEVLMzDYDEq6fM5KUOrcbWg0L8NxFWCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Lg5tHcYxQAemGDikpqASMDDfubUiHUUko2Szy8Xaekcy67z-sLSK7ngncmHcatwRKa5aNVm956G9H2zXE9UP9c04Oly_in1BnlcSo6LaWCNNg0UzZBpS9ttkQnbL2FMjqBu-L729Z80Ld2r5TgMNY4n3zXmQjETRAF_B1Eu924WWY1w6_1Ap7t3zo7OiD3er2e4ll_bm40FbomPIoXTNIdjr3Wsiw_NIWT3y4tQdJ5gVRyTT7c-yXSsVYm9yYEsYJWnob7ruwWOWBMm4I2VRatgDWAXJ5cG3dLJU6QsFjm3n5BpY544E0aXxvDrBYpumtoYzmwzReTLY5h8qr7xGeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Lg5tHcYxQAemGDikpqASMDDfubUiHUUko2Szy8Xaekcy67z-sLSK7ngncmHcatwRKa5aNVm956G9H2zXE9UP9c04Oly_in1BnlcSo6LaWCNNg0UzZBpS9ttkQnbL2FMjqBu-L729Z80Ld2r5TgMNY4n3zXmQjETRAF_B1Eu924WWY1w6_1Ap7t3zo7OiD3er2e4ll_bm40FbomPIoXTNIdjr3Wsiw_NIWT3y4tQdJ5gVRyTT7c-yXSsVYm9yYEsYJWnob7ruwWOWBMm4I2VRatgDWAXJ5cG3dLJU6QsFjm3n5BpY544E0aXxvDrBYpumtoYzmwzReTLY5h8qr7xGeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGeJkhm2XKfQlFSiKMZG1oxI_YewoQuThMtZ1M_cRd6891unQJisiMgP6ZB-2enzpCEWBgY5sbUUq2bvm8A6n1dd0Bsz2uRb8NJ7vJsQlrWbgQ8OKMhkerSWTW5wiiy8lhh80U9ZqB3ARaF9K-LcyAlrFjFLPPiOgGrxvzahxaHg7RS7tsVUAxOHrBqdptqdVnVjlMaqImFnx4qCRptAqKaJDYUbzrdJOHr5vXgCB3LUPbQ9yy-fQadYY1ga2uHmI9KjgyuC96CqBjdT3cTcUEsxs4pEXBp_dXU539a7Py8d1c9L0Yju031mGv_EhwV7TII1nMLO5-IikjTJKK5ItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmpuQ8nzKDIXYB_M6lNXpRyqArMNK2X9G7abGZzxTKa5O1LViGLRyH80i1drNxmOUv9O7oMZ3hFO9OwhAuj_GG-yjoLXSVkd6nadfiSZyEYoKUBwbpSvgLLxYULy1OoyAF0ju4p_ogJGzqeJGu-iYXVK3gpXS22LCdUFfsuhxFLC1CohJGl10GRZn3Xja8MeeXz9SiTlLcCt18vi4lKB6uy5M58a05C7541x02o_U5wQmegOAU5tKd9gLFsaR394GokQtPNUSXbYDRSXzet098wbqIoOIEj5GUXPtxlMFda0lFrm5ncoffWS2gsQZMNNnaMlpsDE8om7XPDPvAve3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=N1pfzKZuKYyfmFRNEfDYSMctG2dmIPtG7O4KcT-Ly0W_LUnK78dXNZGAbR98yxfmi365IDBN0gxs3TNBePkIgItv1PXWzqgUmedWu80rDPVRwCzrek4YPHYk03A42PhL0ZL_4-Puj5QWxXAYWDV-oZ5D8dl-wXMfbCbfiabfNafxZJjETnC95l2WKoYCC_b7lDbMRngt9VMUIDSFGpM7SznXIoY8U7j692IPCU8zXSszHTIUhYv2InfJ-d2YTcShf3FwsFAb1RPeECrL-aZsiEaZ1c1kqIBFZkClrGbtCsq4I7UmR8QZaS_u-vMW_gBy4OiqRWtah3QshisJET9izjLki_6FeALs12oo8tIoGvPEkFhwodwd_eOmJ18IY3UkWN2L_zbxLWqIg3ciAT5whwKERLoTqgIlTAG3jLd71A467bOAqXXBBbMyCU5fXLhfG3zysHWhs7O8AoszgH5FCIX7cn6nEcSbUZmGXHgAuiHoBoPpeMJXiyYpzfKI9cqDOLdb9T4uNUvgbShpHUnEYjk5gJeIl6unkmqBm3hnc3NFnlaadJMP9oQVP5C2o5lt4bdWddiGYqOUmu0XAfecCuATOJZhGMDXrMsinsSErmQpVg7fVx70lkvYv_rLjECdvBJpJjOQVl-hKhjxs_bfBfj-qHnTSiB0ahxGId9VhJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=N1pfzKZuKYyfmFRNEfDYSMctG2dmIPtG7O4KcT-Ly0W_LUnK78dXNZGAbR98yxfmi365IDBN0gxs3TNBePkIgItv1PXWzqgUmedWu80rDPVRwCzrek4YPHYk03A42PhL0ZL_4-Puj5QWxXAYWDV-oZ5D8dl-wXMfbCbfiabfNafxZJjETnC95l2WKoYCC_b7lDbMRngt9VMUIDSFGpM7SznXIoY8U7j692IPCU8zXSszHTIUhYv2InfJ-d2YTcShf3FwsFAb1RPeECrL-aZsiEaZ1c1kqIBFZkClrGbtCsq4I7UmR8QZaS_u-vMW_gBy4OiqRWtah3QshisJET9izjLki_6FeALs12oo8tIoGvPEkFhwodwd_eOmJ18IY3UkWN2L_zbxLWqIg3ciAT5whwKERLoTqgIlTAG3jLd71A467bOAqXXBBbMyCU5fXLhfG3zysHWhs7O8AoszgH5FCIX7cn6nEcSbUZmGXHgAuiHoBoPpeMJXiyYpzfKI9cqDOLdb9T4uNUvgbShpHUnEYjk5gJeIl6unkmqBm3hnc3NFnlaadJMP9oQVP5C2o5lt4bdWddiGYqOUmu0XAfecCuATOJZhGMDXrMsinsSErmQpVg7fVx70lkvYv_rLjECdvBJpJjOQVl-hKhjxs_bfBfj-qHnTSiB0ahxGId9VhJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr_Fh4X0SiJtX0mr5Sq_PWvBYozRZDL8z9yy8BxuWKHtlxmcikzie_pGIZ_KCMd1NU5gdp5mjfDNlUMORXpWXNvmXrgUfk4rr1v4fJs_7Bg5jhjSBSHNQe1pP4TZbzbuvmKEFsXosZo1Aj7-a8B1Eskz12gqzAHa8qFHDIpHhuIzU8DFUuP1byn_fzwP4GEQUNH8PYNuL-hpIc3Bd4ofitZM8FNNXtV5W0NkZteeGKr_Heh1UEgxKXHZ1iyJjGgM7ofvahZaR4O-7HuoJSW4_-4toDSjH77ztBy3kydW8cuCEICzwIhQk3psjbPgMO3D-rXt37HKsYDFN9ohXLe7CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VneI-ni6FzTIDDaXWCBwNCJG9ri0JyNd3KG36pIpHybyNsLGzc198Zmsc9L6b5T1zUdaIxkJnmi5ZHFufYRcvhcxd5tL7IDl_69wkBEm9ANvhu98LawD-xVsDHPL6-PAbPP3jinfM7Hn6kW_Rh9W81xlsfUis-PjeFPFF4UaB0qp1UYG1RNIgrRQvfg50oDyox-UXq2VNNOMbw8lJ7rFOpaqxeAllF1ibZnc5WSCJDROe5bWpHq_BLZ4wsbnsonilOfm2viWd4WVZwUTx_L6xCY3LaK0SN3D0pmJLB6u8xC9YbjbpORp9L-_ENMSJJ7wQKV7sWCDgrMlDomK7U7NFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwNo5lEuVKCHdahmG0S8VcxTOwUgP1ZZObt5OdLRviy_SZGvfjNbSVnl-PD4e37c5jT7aMmMk3PHcTYlzNCpF2ZQgxxmhbwC-su8tVFsbuUOR2_4T9tQouxy0wGxBheobgdLvHWrwJ9505_-7uIk1c9XZlf6Jt3mjVzLrnMmB-NWgcfyVc2-f-rNEiRiAzKUaERMsUSDZoUeKmFPdgIWgU0Q9t0JlI4DSga7u5HHKDvAY7U-Q0PW_Tkc-0IgL1c2o4PFX9DRcEW40nf_0bg5MzXgOSi-jlKU0TXBroX3a1rSomz76ofA-VLwMY0PCBMAAScJY1sjVfSGyhpITw1yBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdMx6Fsv9gIKUnAuElY7nYas8sFC8tsHpJls3Bc2GAahV4p3znp8FLSbAeq1fl9HZ9qQhaJp46r7BJwiumcy-ioUp7f8Z9jBsU4HuDLCvLTfPhhDiBTceobZMZW0S0Hih0ZX2DGRttkSsL7UNoLJUKk74sQgj3fl4q3JZnu_OIbY_OogGQhHcnb5YDkb3_YdyPfn_YyO3zM-HIvTyvxuF0Biz4R_ktaMFri3V2c_gsnhCfQkq8ijrilR13UElGVmTEf7sp_5ZeFC6UcqmrOgSedabuKdfD79PymN6324hlx808PNjXaYp5jUH0HQPStFjml8O6EK-8cD8TN6L97bMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=jQFA-T2cTuCDiqYFXflw5hfwivtOg95BymXE4YFMx5ziFbZ_uAonR7Dm0dobJf-sCkg8Zq43Qn1XMKKHFLvmAm7br3hCyi51TkaEvjMbfb_eUAhY10D2_Yr_sDdf9VBR0i72uVOl7vcVAdxtNqiH5oBmblYXuCi1HPjJlU64jrgXK3o9tG0DEvL8MJkQ301lkCG-z-5OA2L8hjpFznvirWhcISQmAMWspDfU0I4AhLh8sSJwiXmsFqWf-AxlZ8kdPsTH4x3CqR4i5jzVFDPVL3U6nC898dUJ0_khiNRrFLN20nHnYmurNU-Rg9EkgIqS-tuL0qIj6qnKdAdfn4dwaCMDP_2nqhHTjXl9QNqo2WByBE8Mhf2Kkn_kf1zjlxxh5zPWoIa6FtiXx4f33Xz47QJ60YvNsLWOX6sw6YAcM-WlC78iYRlmAuzIBMg99xlamHzExRkvEM-h8a30SRt33Ri-vpcw2f584DxyxaYIhfo9QSQJN3CbTlWqC8wt0DO3Gh5DnECEIGhj0k5Dh17qXEBMQapfiIMhW7IgkXDiCJbztpAUGkQgov_dfrYIx2CBORpeUilL9JuZ-UD99pAedQBm04oZoficfOlGODtmVeG_gIHT_cgVPiy3repo99CA7H4uRge15hPFFoxyynOedV1c-HjxceGkxErkb5A5QkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=jQFA-T2cTuCDiqYFXflw5hfwivtOg95BymXE4YFMx5ziFbZ_uAonR7Dm0dobJf-sCkg8Zq43Qn1XMKKHFLvmAm7br3hCyi51TkaEvjMbfb_eUAhY10D2_Yr_sDdf9VBR0i72uVOl7vcVAdxtNqiH5oBmblYXuCi1HPjJlU64jrgXK3o9tG0DEvL8MJkQ301lkCG-z-5OA2L8hjpFznvirWhcISQmAMWspDfU0I4AhLh8sSJwiXmsFqWf-AxlZ8kdPsTH4x3CqR4i5jzVFDPVL3U6nC898dUJ0_khiNRrFLN20nHnYmurNU-Rg9EkgIqS-tuL0qIj6qnKdAdfn4dwaCMDP_2nqhHTjXl9QNqo2WByBE8Mhf2Kkn_kf1zjlxxh5zPWoIa6FtiXx4f33Xz47QJ60YvNsLWOX6sw6YAcM-WlC78iYRlmAuzIBMg99xlamHzExRkvEM-h8a30SRt33Ri-vpcw2f584DxyxaYIhfo9QSQJN3CbTlWqC8wt0DO3Gh5DnECEIGhj0k5Dh17qXEBMQapfiIMhW7IgkXDiCJbztpAUGkQgov_dfrYIx2CBORpeUilL9JuZ-UD99pAedQBm04oZoficfOlGODtmVeG_gIHT_cgVPiy3repo99CA7H4uRge15hPFFoxyynOedV1c-HjxceGkxErkb5A5QkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=ItvVDMNfudHqfvpZJVpKn_vE4ARwTbaKCJjuJkB_gN4KQIGbX1TnK3AhXj_SZ0TRMnfA7VVzMzmQ-FnqY2mW3CFdUii7zoU9g-atbl3CUZgLbguMD9lBNtQsKVpNPDrGQrebFBtbJqWMMlRdoS8IwV9XxVdzCrwA6CqWZD_DBPNo0tqKm85QZmPgv2lz2OENcdbhoPy_SIdBqOTxF4PTeQ2jCf5xNaWCX8pWYaQwUNkQ4DocPBjRkQoVLOo3E7iYVXBXSKpMNUcGKXfp7zJY91_9JOvuE9Bf1YjXuQI8KQk4PINurPftNDw_OT7iMTnwkFLDm9_pfvtKHxzxQj7v8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=ItvVDMNfudHqfvpZJVpKn_vE4ARwTbaKCJjuJkB_gN4KQIGbX1TnK3AhXj_SZ0TRMnfA7VVzMzmQ-FnqY2mW3CFdUii7zoU9g-atbl3CUZgLbguMD9lBNtQsKVpNPDrGQrebFBtbJqWMMlRdoS8IwV9XxVdzCrwA6CqWZD_DBPNo0tqKm85QZmPgv2lz2OENcdbhoPy_SIdBqOTxF4PTeQ2jCf5xNaWCX8pWYaQwUNkQ4DocPBjRkQoVLOo3E7iYVXBXSKpMNUcGKXfp7zJY91_9JOvuE9Bf1YjXuQI8KQk4PINurPftNDw_OT7iMTnwkFLDm9_pfvtKHxzxQj7v8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrVe1iR9hCMZv8EgvNVpy02bdDw9UnOCbRaddMOc8eVyc06GpuRqgoJw2Q5n8-b8Pp5AKoEVfV0u3pIWsZfMlUYU3if3OVvapvopKERlP7L-VLKAgHJ_W7wn8HSxyS_AY3x-OMBjUKF5y4ra_aCKJjMrqebrxx0UvyT5erCeA3vSXPZE2lFQqQ7dBEt9vXe4tWItygW4vn2bfMq7TPMgmtLUoGo9W7PpX9F7PQhSMhyOSyGrUz7I3d6buqiYMyFUfN6RwctqlBXr2o-tNWUy-d87Vv_kEShZtmxO41_h1dMRHS2gfrAuRTkRUPe2wzsbexFXDJcVEIzVjwr-MBsURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaZL9aUSafJernvWrCv8_mmi6_I5tNYWZF8k97wkS9NNfR1qHMdLAKy5Yl-e4OoCKrq_Wyzb0hUOSdJWFvTDmD1AzaFjWPiUNaORBVEOc2hXvK9GKdNrhD-GMyVQGcw_rJyZP0Lqg_ri187MAiB4rfwi85cokA-yVeUFu39nA3OXQwqNuyNutOM8KILvhEN1DJ-afi4flS5Iq_pbZoexePgM7_1aCT-fhuqX48EvcNT6twL8a2lz8aEQiMExBiZmK1FSbtsMorI6c3KI2l15ZzFt9YPiLmY-OkOpQRTx0kC9IdEYR9Jh3fK5JsAL35EkgzIeegaXZak0Dhx5tUnFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SP8GYpyGCBh4Q-nDeozVeEW0-X58IChpKPLXBwik3LAPJbtfHYOS6fWJWt3KIIfkOEVHlzE95iG_oySAPIrBwBSmk3luN2dq2aoGkNoOjzAH6TJsRqWXUTPKP9s2uf2NVmzYx8IA3UNQxMefXIi9OJGl_DIGwx_747ywOOhS2HxFv2sIZlMeztcC6QuWVQDgTk4BBDsSTy8uAH7XlFIjeCIqkTDeP_bl8NyffCGqxXsN1Bgn60vHvUUoBBsHYBMUzidR00o8daYjlWsofb3su1c9Jvb8fbm1bkihPJKe27A3fV3H0VFt8JCNtO69uSGd9EHr-Tux7ulb-c3WvegPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VR7wnPkE1chvnSOyqQCZ1PcU3481_dpqalOWli_dFqBCMwFbc4eLCRc8FYBwAxHb7VqxK8r5x7RCFwcZgqagGU6dpKN0v2ZFcDXYKUDLNfZRkMqZ1XW_97HjweVPAsbwGfssdQ1cw8zotWCLaIJ8eJKu38nTEnwC1Mv5AHa4Z5VAvkGhfD3QPopqtJ4SZl2DiwoIjskbvDX7FpsSSCYw78-tS-CUYKCZ8R_UZ_PKVPiT4p6wyXrwGdXiCponkP8NinTgs7TA2AZjJ0a24xlDM8eiPQzYJQPSMkpY-gB-HwvauR3ua0CreouxG6TutUKnGmFkgum7zOM1_3j60cQr3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC74tZEwLGoFDL3ueAWBq5Gt604xxyBZN0a5EtWpVys__hK9YvQ6qnfXO07rlqGh12Un5pJt7t5T6IdO3WVUHn_TMd0wE--LV5Z0-YStv54I2dIt-L0fWxcjGDonx_39BEnCoAFNWSIDRPXZWdeEUXs_Ua2KQcmIt6bF8h_z0pRkR-P6me21AkkK3Uti2QZeeWnVsA0Dk4L76fNA_65i0uhS3k8FvK5Xm1k3P1KI5DG4YMng3DXwR6LCBYtTjF8LoFId_rttB_uiqBIRY_g9ReXWwKTK6hKk7mS7weJYY2rABknLFTevk7Rw7NJy1CawN0owVIqEIpRNfuVbjs-Q6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2le92kf57BOTnO-FMd18TyFerL_-APs4U2t3T0e5NGR-zJS9UGeCAdtX_0u_hPXurv8_8_SDrOMzECTDgrraPqWniENi--IMyg_DYAfpdGCTATAs8U104OpU-nCj2fzfK5gblyu8OXeWxbpF-bvNb-47aylgtACVnpA0-UnLiAO5aHGnSHMBIb6j_IsUlG-PUgQnT02ZCI_yRUtlgdV1-n2GL_PJLE3UnvdablRqUC2zNSbYITjBOGVWrB0bwjiYSt70hE9RddD2Cu2d7LBCexqNapjSL-deJfn4wU73iMDQM8JpEyqr7f4n1xKoU0MkTYsdyRi_puIDxVN1_r-pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7wgAc2oRwqsTdRCC0eKGoPmja0S0mzaaZgg5S_dMeCpFpT9REMmb1FPJRnMFvKSpGfuqurWcgxvrgOIJ2hchhqPHSPvjO71UFTSD6DVKcdoDZBb3PDAcyo6lL1oMup6Khk4AZSKdR1PSDVmiYsVunuLIOG94Juf1AS_-JZ15tJIZ4zMJFeVwfDiz3RgiNQzZH_suXGcTjmFbm5ed9OFG3PwF8CtrtU70gUP7QUEFRxeAiuA1-BLELXqC_EZgr7ekbTHGFiFSXXeElP25uD5rMcCWGIgPigbLpcan0lCB5Tb_w5naOwixVeOF7bpVlHKsFh0huCK5OiS2R-gDsB5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
