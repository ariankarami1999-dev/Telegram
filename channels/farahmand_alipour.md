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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 20:19:44</div>
<hr>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVHNyHPeagSnxkwEfmIrKKeiocZOMLHac-Ampa5iYk4oKWnbnUQ5mmDpj43K9ZZi4ScMe-SFPpbMZp1b374940tv8hyRarAZClhCYlCNkGyTcpRQds0j95atYiMfifXFOZGGgkLPwwPfCRVRR0k1WTNcrkBJMJgZ6qvZk6wpv8qiVbtOlxQqaTASMiclI7q0gZK8jMWIL2hhoGbNqhuD_Jfle6Y9VBm_9GALlygBHfOXYwj9mjO04vM28hgbpjJbAiRy3v1y4AFppInFPv60GbmuRu8QnFNqagehXpjfvLfF9y6oQ41jn-rk4p8tS8jLs4_knXKQ7Fkm41mt_U8Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU03JBBIUrINr83zJT82G-VOKqE8hOi6VDow9Vk_JrqmtdlDqAZ4VWG2z6kPYKYWnTvcu1ghQYhN8YxdE3WNEs-puYUx85kYY4Gj7TJ1HIHBl-Z1qC3StQRjFiHbT7CppiHHAE4v1oZPOpZUMXOfdcUN1h9ilzqqgRBd5aJhbmIOAabbejFL_KnA94YSUmqaZULOPgbThc7gMMVMBuJCRXVs-BoDbGEmpCSNmoXpnK2UBLLuvWLwEo0C_AmejZoVeeOOmnT1FrgCm600e-Zya7Q1SPA1SiH57ooZqksGRi7Mt7Z4_If_Z6p7vDT3ipcJFoN3pXnyeMra1mG0EJK7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6uXN6AIS_5MoIUxC8Y7ktV9p3gNfFu3TR5dpzWtVtsp3ak8GY93NMY5gwTvkLt2EP0AgE26uNAI_5mZ3VS4yzWja7DE6sXcoE56ogTN57GbmcmCRrA99--Vl-uze9Smv4aNX1gBfVF6WnA2ku1E9ydTd69jXDbsfeB_G2edKTeEithmOACjtkYiRBGD__x46cvX0KjphzHYInXTjdn8nNCCb30QIS1IOCAXqrqHtx1rzduST8WOJdn3jn7vio-1fxqGa-uTmg-MMfU57p15zqKAnsO24gUa4ZDerk2oI7emoQCiqoFEElxZX4AGfdV1oK3aX-dd4PJd0FfIrBrWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWTwy7qFQ2leTVpbUv0pOGtqMnDhsmyLo4z-o-7nBI2Z9F-kTUxcrkDAT5LqcUt552dWvAEuWPEpjjnmmQXYZbj6mfmjnjmLYNLWSqh7t_nZiOrsD4hbTQOJ3bPFLJOFM4rY3aS03vNsSYxBaPY98YeUarOaw5NYg--fxUelxAu6kTC0VqWTmUs5mx6BMIScMXFqhTYuPA0aZeumcBVXiLhD_TRtTPrn2kv9ji9Id8Zw7LmmRqigFMptRZ1imxhuFRpwcq4cDbVXFeeDgRFabmVzuiMwHPHiKXCXGuf_jr8lhUkRNi-yVFxHjvTrbzGru2gea75qwjg1ZN8aGho74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmoQU1SJHWKFiRuqWWrJ5VflWt5s5N_bn2cxU9wmKke8h4iTyDG66E4n8tQ339OA1-Q3gHeGPf_PoppA9Rq8mX8X11AHr0LNbcGeTPmYZ_hhyAQIv7g1K15wjI1NxhCn2I17giK_4fEQN6QcrHG7MOPp0jO3f1kAgGKdY20bTHhHqwZmww4_QCNN5XyBpFJpexLcj0kQ1wmAwnJCmGd334OVgGNc2P-Sa_pkmC8q_9NqZKkH96WfURaL118iDNOpHlilGiApauT0NDhhVcL9-ZyLwoSMeZZTn9Wtgx1O5wJNgI3RFyHtThajKSpeU1r9EJ1YoMNxFB28_fL1JkHsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMm_ESU-hX2-8muoQSdzXE_BM4NLEtcn5J7l0m8TdQcx2vkrotM2d1UQIKqF4jF0jExUa07Mh7uCHsUifRB_4a-jgzjPkW8lhcjRTf0yW93aZ2CS0u1DWAfniKXkWiNMIcx_wy3qONuzKNkNeDlimLYsq62QWADVyNtcFqwW5C2SRZOt-O5aZ0FsKNcP-n54YlavS9Sm-sH_xh1G8BxWiVWCZYquEPGjIT99eFkH9Hock734ZczLuRLgWBOPtQ6hRnkZtMgY5EuNecQRI0NpBMzBaRIOrljn6VqsaOvdDmQKpF47Zw8nXGllxmdADVzB9WBvfEUGZPxehtHw0yDfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiWNIn9AjZs81MmjIvrcD9sGrtXBm50rUG-_C4IfxpIVO1uu23zeWLIfbq2TwWWoxFpD88t-B0iR3xT3bzSwqkzuU39DZiX1FUSgqJf1LiaSmAJs3nWTIwET0HAaKTGwcr5Dhx9BubL3uMBRq3ki6fE0rcRQIv7bS5sGzyrXtaEed-nC_n2unAA5d7ztsxu2MN7hUK98RyJ_uksgWzMcvYdgL2c5NgKWcvcUg4M6YUOHOZxZZl2QikX19JMY0kEJIFV0j9ciP797oFNzjHD84Pf1VrzbPP-tYlbB8aKzieOw-S5PS0dIsUcYgRvUYQUEC23L6qif0vILT-s7yJcDwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=NPmNFgibiFSa_geOyVg38UQlH9SV_eadZzy_VFltEi9Z4a4-V0dCyM8qYFkuONZL7XLVGVKMkd6B8BHIzoRK5fS-lkvgpMoZ-_BKqF2xm_tP5lody2TPnPE1XJJ3BfoV1PeJ5LQM13ECGUEIjlJ0UFSJYhlfrkZmgq05rKjrCd0t7B0-C-Ao-1rTYqX9Z9S_Zq5FJL1tRWI9VR3PfpwpNXGhJMGKlI7Gv0HGksCT7UAt2PY-RZVWZb48JaYv7aQk-2U_Fh6dlhGbgJX3zsqKKKzK2VJ_7DTl22EV-8v5M7oYflG_RwmpOv4ZuPWWHKuvDz2PXEhtgI7Mu0ZdN9Apsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=NPmNFgibiFSa_geOyVg38UQlH9SV_eadZzy_VFltEi9Z4a4-V0dCyM8qYFkuONZL7XLVGVKMkd6B8BHIzoRK5fS-lkvgpMoZ-_BKqF2xm_tP5lody2TPnPE1XJJ3BfoV1PeJ5LQM13ECGUEIjlJ0UFSJYhlfrkZmgq05rKjrCd0t7B0-C-Ao-1rTYqX9Z9S_Zq5FJL1tRWI9VR3PfpwpNXGhJMGKlI7Gv0HGksCT7UAt2PY-RZVWZb48JaYv7aQk-2U_Fh6dlhGbgJX3zsqKKKzK2VJ_7DTl22EV-8v5M7oYflG_RwmpOv4ZuPWWHKuvDz2PXEhtgI7Mu0ZdN9Apsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH4eleKdFbSgFIZXrxSK9vz6yTm1iZAbPHGLiy-sOaS_YLc923MmdnP0CKa8MiiM9XVXrdqo7BTIO95TYjIBOtujE37QF1S8x_IUuBt6BZMWdjqqCNDVEuBpk6ERngPpv-9nT3vlLHJhGE1kfBo3tH4Yk7eQw6B1aMkZxo9BZW9X6XQe73qiGtEluls4cr4BuODcBPa4qvUUoKOz8GphbbHANcPgzNqOGGZYj4ySj4ClfWP-LQRrUXw8JC8IRSZQLBG77c7r6OWUT3PtOJbUtDa4cLtulM-SnpWp7y3pynRiDQxA0YqmUniImZVpL2aBRBuS63Jo5eQ8Tz2G7OfTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4WHhPI4klZphcAnvfzbFRrs3-gPW_Of8xgJYg9hP6P1fxsVoCQpdFN-aak1IB81wbMgNB5dst07NhM38k8YTCjIJFByp-aNECeOyR-d93Q5Kefgz8oUulnI7v5AkfETmBJ1zu8DnhgB8zk67itxXnncN4rijAbX6txhu3DFUukgRG2VYgG1cp_iHAEZlN-jB_qieZpXWAt_uHHXFZ6Y76IMCU6nAk5zVEHN_AafJ02UmyeUvipHJgltqIvMdDUcpqwobcbY2T3ZtAGjtwbSbfnGL_KuTkHMPWzuOdubADS6r6t2E5ETcaQ2X5qOkgQC_HdPiFHXFvWm2c4zZmVUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=aQCsBRQFwBhkVbrv552lde0Nb_GBh6lgYgbs_irRWZlN6Fih9Gj8QBD9CSCXyTuKnAU-1zSSqRNjjBagUxeGtwKUjkXShDwwKybuCSgo7nOH8GcLR1ZjEcXWHXzN1VHyLpZAGN7wTlh2RAcYUuieAFC7DX77WKRzGq2rNeJNkA08hKd_oYhQHga5Gd6WxWtaFWoDKIXzlUy9iOrRNYeKba_kx0_z-30epOHXdvXTL486ZWEnEScNWuQfinRvw5jcTLaEIdmXPuEXIhKM5YYZYX8vZoHBlvz4Mc68JyQR9P0D1psLpxtMBNLCM_M_CdvG1az1O-fG7Z-JkOpltbBhNFCWmxo3hCp5YU4IR1Eaokm0ug1IXcZljjftuQ2sS1giT7Sz-cQaMzhXBGpWtM4PKjg6wpamX1sqXUT8m8QjnCsTki5wiyCZh3l74ZUcUHqDyhM00uLIXoMx_seMvly-qSbsJkFYgFko_UWpUWzEkzfi9Z-eeVdmtbj3yMqdpgSp0UIAUviorsudie9PDwvdZUOEHockKtsXDYofh4aUm8xG9Oz0FHiXEH-IYkLp3k0iKmm8Bh73kFWoHOGfulBCI0Dc7k3twIFqhkF0x-3pVZYx7t4HA-Pl5-laAk5Fx4gFZiTjZQv8Um2J5qMNcMg_ekpDHNsJ5k56h_3gOn3KPAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=aQCsBRQFwBhkVbrv552lde0Nb_GBh6lgYgbs_irRWZlN6Fih9Gj8QBD9CSCXyTuKnAU-1zSSqRNjjBagUxeGtwKUjkXShDwwKybuCSgo7nOH8GcLR1ZjEcXWHXzN1VHyLpZAGN7wTlh2RAcYUuieAFC7DX77WKRzGq2rNeJNkA08hKd_oYhQHga5Gd6WxWtaFWoDKIXzlUy9iOrRNYeKba_kx0_z-30epOHXdvXTL486ZWEnEScNWuQfinRvw5jcTLaEIdmXPuEXIhKM5YYZYX8vZoHBlvz4Mc68JyQR9P0D1psLpxtMBNLCM_M_CdvG1az1O-fG7Z-JkOpltbBhNFCWmxo3hCp5YU4IR1Eaokm0ug1IXcZljjftuQ2sS1giT7Sz-cQaMzhXBGpWtM4PKjg6wpamX1sqXUT8m8QjnCsTki5wiyCZh3l74ZUcUHqDyhM00uLIXoMx_seMvly-qSbsJkFYgFko_UWpUWzEkzfi9Z-eeVdmtbj3yMqdpgSp0UIAUviorsudie9PDwvdZUOEHockKtsXDYofh4aUm8xG9Oz0FHiXEH-IYkLp3k0iKmm8Bh73kFWoHOGfulBCI0Dc7k3twIFqhkF0x-3pVZYx7t4HA-Pl5-laAk5Fx4gFZiTjZQv8Um2J5qMNcMg_ekpDHNsJ5k56h_3gOn3KPAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=uf5jdjnaE1o0jHtCbPRXMUj6d8_GS3CP4vHcGEDPK0OdzZL9zsTz78-Kz-Td8yAeIA6f0qFQU7FRrozjKLB2DvHXjZ5wtuYQaeK5q8yc_8OWZjnwGmJB2FdzhtmfsU3c4H9108xkM8vqycCUKSntQu5AZvXH_31L6kxKA1XqmPLGzLGqiCqLSU7gcBRH67sjkRUkGeAet_mFP3yDnQDH11nI7dTKlKxOQ-KTnQHKS5-QvQ7is4LJHwUg8tbfemoMQ_I6oliRSAT1LUaZLIW433_oCNPSPGXLsCDKVaNO1gvzMvrkrE0A_TDQl9_CGpI3M6DzQCf2FkmouMLF2yKGdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=uf5jdjnaE1o0jHtCbPRXMUj6d8_GS3CP4vHcGEDPK0OdzZL9zsTz78-Kz-Td8yAeIA6f0qFQU7FRrozjKLB2DvHXjZ5wtuYQaeK5q8yc_8OWZjnwGmJB2FdzhtmfsU3c4H9108xkM8vqycCUKSntQu5AZvXH_31L6kxKA1XqmPLGzLGqiCqLSU7gcBRH67sjkRUkGeAet_mFP3yDnQDH11nI7dTKlKxOQ-KTnQHKS5-QvQ7is4LJHwUg8tbfemoMQ_I6oliRSAT1LUaZLIW433_oCNPSPGXLsCDKVaNO1gvzMvrkrE0A_TDQl9_CGpI3M6DzQCf2FkmouMLF2yKGdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5QkHExe3TCIRwhAoVEy5_07pq5tKoe4tATGsgd7c7y-rAwinelI1uzUUUPSueVkO19yNC4nAofWg69eWRQgnrdxVq1O0G1hIKvTpGbppkV1sXhaYTJ2J1d-DP3rIbazYziF06q1Ji1ja6bRiiUeiqta4QfzLToQ0sR9TcJTLN8-N58rQRHcGTzS_-feXhBPUjJz_PJ8axbjGNI5EPJaJa2GGbetPbWsKwOA5J1ED8I9NDehSwSNhvxUqWH1Gt3ZXJLuRxe8NaDj52uPkwuThUqpIepU33JG5_zviCNPn06f0nzPz4aRnYFBZAcZ8HRYPsckioiOqXmpBhr2StAoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=cIRzQMA8G5OAAYhLzAR2fKjyo_pRlskOhqZBqkMK8sBYkw3Lc-AiUo2MrWnFzAhFLd33uRo7hIaT4lH1ieP_RsVxI6gU1eWoh3ZWL9aIacOcIHPCoP0Lky0Uu2_OOeh4XmoktodNIw1qDazxjQ5CpNvEsCZYv-E-di-1DXZi2X3YAslB3DcCcqClnQxqzQEU8wzd3qfeqpTTYBiNbNJw_X25v6PeoPo-kdzIqMZmWDGJUALsUVdmAg5IL3oDUADpNez0NQK6dT6kwjsU2Qlm9V6uxZIMZf1z9CPbIHEOso8XhQmVT6sh6oEyiObji4VeM-WkCVHHGpukv6QGqyUWEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=cIRzQMA8G5OAAYhLzAR2fKjyo_pRlskOhqZBqkMK8sBYkw3Lc-AiUo2MrWnFzAhFLd33uRo7hIaT4lH1ieP_RsVxI6gU1eWoh3ZWL9aIacOcIHPCoP0Lky0Uu2_OOeh4XmoktodNIw1qDazxjQ5CpNvEsCZYv-E-di-1DXZi2X3YAslB3DcCcqClnQxqzQEU8wzd3qfeqpTTYBiNbNJw_X25v6PeoPo-kdzIqMZmWDGJUALsUVdmAg5IL3oDUADpNez0NQK6dT6kwjsU2Qlm9V6uxZIMZf1z9CPbIHEOso8XhQmVT6sh6oEyiObji4VeM-WkCVHHGpukv6QGqyUWEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFm4MXN2YICCDc4kO4Q1UzuNh1aaWtNOtW31m1NNEtZcokTl3Fb2DpAYzFNGmO_QNGIOzm1xlJEZSX5cyij2GeQpdexxlVZJ0vvpEBqnBsyjg5YlL6gBnYcf8702kTQjANzZpmleimfEIOkjQfT7_YeZg9Y20GQXOFhF9sCEjoRx0HOoEMUHJZGSC_ezqN9DDo6hYm2C0BEoL1iwMF-l9WI0wU-jXpAQuElYNxugo_SB1uOvDrbLAAdxHbXIKPeNZQzG8vn9UE_5DNK1mh2iPBlrxXcsC4N77nVAf4X7dkKaKokg591p0vTtVH-H5yaYzWcKgKYrHsomZSaM3eVziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbXZKf5aalSOwh-7ooaWLS6hlRUCrsBfBIzxAt9UBVZj8kBmR0lbrpPAReLD589uvfm7WgmH71omHgoaKOL8RxZOYK5qXUzMf7Ur6X33QaVNBdUoajcQGdFTP1HmtL2uLcsuJFwc65E-H06uiBYeJqkguk5AQe1NcAj3LXBWq2nBsmWkQ12Rd127MH3MHx0bI4Cn5WCaEbESPTxl9KTw_6WcRXv0l8Pp7ZgNmgOhqKLdLvk_X_g_qrhUsYsZEyTuiWtpA7pvt7vEFmUAKoHAyYHpsm5k_zrAWylw34VfA81RUpJzYT2IuQjQiZhwhvp32f3m8iAcDuEtgVIRRZfnUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlDtNBIpkgGo66sYIyq3lAmezZBuz_EFVa0luAcA_GENsf8Oa7m-e-J-SuzJPT9l9CfyRXnlWTwbZwKnhV1goMhS8jIMAWNOgr89ZY72WETae-26RN_vE-YXDwzeTjiqxAgJCxIRxTcOVn1RJI5odCIzrZ9FvAAY-ambPCvHaWA6mwq1OE8z-HtEYEdOzNt8EuISEPPdnyof3uGopTcMINs00Yuh0fGGQRNd6e-afspti6ljBKdsntcpWqNhPBn7y6YpR4dWubTNGz-cfwR3VB4s1H0Clzd8XRH8thfqrGYrnbyhreiyOFjxpKMRNnWEd7-crRX3YwXQprRShoy8iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojw_aUOccYiFMpz9m-LClIwpYQiUUhXzO4dlOGCSZqFUNz81VRnqAyPaITBBcQlEKhvDkjTZM_AvIQ2eMJpg3v60V8thJ_qjMjhy6UT13d42ogjsavlTdIJFvRQnZB3K7TGxIiXaiXRBxmDKdfKGim9EoOSNwdHOq4Me4Ex9a9w5VTXyyjFS8GNnjrr7r9IuorlFl0CVgp49dHQu2omH_oVgFWKTiDDu8JZWPbaku3v5CrUfqlU_HSa-65KGB6ycN4wKVgQXxxk0oTtJvqlXMCRQbgAMy--Qgv3sryTRm5gKlX18wmW8Cjx90qlFsZfXPejJUAP3dE-fVFNhZqd0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcdvZT5SDZe1jSOUL8plcWwZjUDlr6YNN2VD613IlWE3U4H-XCsJQXLFap_oMUHIE24cgmXqENdR-Kl6lRmPZWhvDYVelb_NGKE1DMvfARcRchO2G0Jcu_hrTAJxWh5CAnXyudqnYNoVFzb5ksXlQ_stiOF93KD4qxjxQeq4-8Q6uOEoGX84l56JiIyO5t08GqUAbvtz46Ev6Ln9CEQcl_b9UKvPcNGc-jN-DYmjlWDo4D6iqgXiB0nLCm3QfIrjoG4OT2tSMrQFfwexV7qtdceQatfmOF5fppYA3X9pvlGifbyraGDJ8lGv_KRU7j52AsKLqtC24BE0s2OQm23W6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=k1UYigTOp6fOE1IkL5R35cfnNAXqkf0keq00dvjOgr-A94aOsK08Gj5imcRTlBYCbU-mM5hzxTF0SXtNlote9A95QN0SJYUhiL3Ig-Sr6KjXkFJtrHFRYUQcy-engag8Yq3-BRek9faavwvZTAsChiZXVt923Rb811ijSvoU8ARMc4aNE1Kr5uo8R0Ab_n_aOWKwf82y4AFgyiV2qVQpS4e2EoVqYVWXF1uH80zmPfd-KopQnxW9naKoWBJhfKJPEMkDLhRrho7vSFCRDAaQNmVtS5jaw2lI4muBt1NJsaUM1O3jxI6TU4ANoeGyes7mbGTxAxa8N-pvNHQUxmdjBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=k1UYigTOp6fOE1IkL5R35cfnNAXqkf0keq00dvjOgr-A94aOsK08Gj5imcRTlBYCbU-mM5hzxTF0SXtNlote9A95QN0SJYUhiL3Ig-Sr6KjXkFJtrHFRYUQcy-engag8Yq3-BRek9faavwvZTAsChiZXVt923Rb811ijSvoU8ARMc4aNE1Kr5uo8R0Ab_n_aOWKwf82y4AFgyiV2qVQpS4e2EoVqYVWXF1uH80zmPfd-KopQnxW9naKoWBJhfKJPEMkDLhRrho7vSFCRDAaQNmVtS5jaw2lI4muBt1NJsaUM1O3jxI6TU4ANoeGyes7mbGTxAxa8N-pvNHQUxmdjBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOoZD7T6L7Jf2wz89cfqagMRNugvU2cOCDfUYJchB6EKfQx1ZqdCHicN6_XpnXbdOOGpPXO4psdvPHqTQOdUTZ89CiHbv2tKW9tdvo8oObIGwFEO8Qe4FxV0qlEVGcFy76-2RZv9wBVQhHkNQ8fdn9Dp2ShiJrO99TxabzwsxqdYBFebBZEdGApqw9X_o2hL_fZnUvvZSaf9q7nk6C9bSn3yOHBFdBhDs9JKOg0i8m89nHsbyA_oSjOH9ecDir9ToxDl1ITicsYClgg34FRKhcaGIkv7Dc6D6teotXRFGusRM9zXGErnfkTAEAo38fZ4uaaj0vmnKY6NXk8It7b6YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDEoIRBvQxs0XNyrVZB_BVbsAx-Hg-blmfTttQ0N2Z7atMw-GFHdUFEtAkULkfBmdOa4xC1QJr8v1tE0BTob_85U4fCjZLs_Z3O6jrSZBKqW3KY84SfedaxpdtLbnd2YOUwFxcRR-Ryzw_jzyhjhkSxSUPV60pUr-mrEQ5HDwP27h93R7G9HeUEKiNZvPvrrGoPPGzatGdWanGlKcL7j8icySK4-nddEISsf-HTNrTB99UmlrD4Pn9oPa-nA5PYaDdWMd0hPXiHHRzSfgjm7gJyKv7kPwhCa9qW06XE8CEsN8q4eBUHQ6us5YQjr7pOzyEfG1OI2YKy7diqtBriDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=OZgEN6OxcJBiHJujmoTG8yWtC-MsJ7z0Ih3jkdUyh5Oz89gWmvcMs84Z0CWWnS2qMXIV2jPj7ylxTGHQ8hkBEfKcwtPU3K_0twPZsRuu342OlxywnWqQxLuB0N1p7hM2pV_G3BuUdV0-tGEe-kFBvJkrsHPhDGk2m8ppwrkWTYNUGeqOppftU3PcGPIoRQrv17IQBROZ3N33jMnMgBQcQfYstpyenTOtJHZRIUf_I0hfbXPPng-r9z32teyJYmieycW6tDf6jo6XDX67wdRYSpZuXh96fZpkKLb47iRYbISatAAJJXurgjARPlNbEk0_4U5t9Em4WnupqpdgsJmOvh4K7CPESsKGRobTllW80f3egucBVOPkYUBM7YGn-zohoBGo2-phnQHpJn14Ge8JbiRsPdC9soULTaDRmZmHCSmIU5OwCMoh4DfBT3YyqszbwJXUiGb3ZuJLYTi0GfyAUxFcBc1xuvLJJ5jDbeHXV4Zu_CWwuN4EEED8fIwlXjMlufKVRVUXTLIQ19LLVPzcu3l4CEmZtzge_fxX6aXp4SAmsxXE3c6RLPKgN6rigALjJwDq4eJTdSCdTcJlpno4c4rWsXX7vcov-oGKByK0c45-NwIbPQs2SdUeze6JKdgeHHwKS8cYw17jc_c6DSyIWk4qWlRKXB7GSVGSyLyK8ak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=OZgEN6OxcJBiHJujmoTG8yWtC-MsJ7z0Ih3jkdUyh5Oz89gWmvcMs84Z0CWWnS2qMXIV2jPj7ylxTGHQ8hkBEfKcwtPU3K_0twPZsRuu342OlxywnWqQxLuB0N1p7hM2pV_G3BuUdV0-tGEe-kFBvJkrsHPhDGk2m8ppwrkWTYNUGeqOppftU3PcGPIoRQrv17IQBROZ3N33jMnMgBQcQfYstpyenTOtJHZRIUf_I0hfbXPPng-r9z32teyJYmieycW6tDf6jo6XDX67wdRYSpZuXh96fZpkKLb47iRYbISatAAJJXurgjARPlNbEk0_4U5t9Em4WnupqpdgsJmOvh4K7CPESsKGRobTllW80f3egucBVOPkYUBM7YGn-zohoBGo2-phnQHpJn14Ge8JbiRsPdC9soULTaDRmZmHCSmIU5OwCMoh4DfBT3YyqszbwJXUiGb3ZuJLYTi0GfyAUxFcBc1xuvLJJ5jDbeHXV4Zu_CWwuN4EEED8fIwlXjMlufKVRVUXTLIQ19LLVPzcu3l4CEmZtzge_fxX6aXp4SAmsxXE3c6RLPKgN6rigALjJwDq4eJTdSCdTcJlpno4c4rWsXX7vcov-oGKByK0c45-NwIbPQs2SdUeze6JKdgeHHwKS8cYw17jc_c6DSyIWk4qWlRKXB7GSVGSyLyK8ak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=e396FfapK5q80Y1ABarGFsmlRpr6pg3C1Z3ubHnXZIz13jixmzwFjKKY0iGfJ0H_nlop8aLclVJpUMuBYg_ntcsH5imxJbVyLgdFgyO1BGlHY7UMNbcG_nAK9Tj5uaFWB2BjqBF_dndJj6VjqvvW-Ez86sV6pXV8TwclFX4Mt3h9Q3oBy2rzeu-F-q8MA6RjOMRssvn8n-6ePCZ6SdPSyNCQPU7zF90lK5YL0oBOa3hzn1jMk-tZ3wB1wJal7Ob-txNWAK-dT_ZyodM6HpUyWq9G56qKfKPwU3xw9NPJ1S7PhXmrUJkPqsH6hYTfhctnDe-DMxyYOv2BZjJxrKI5ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=e396FfapK5q80Y1ABarGFsmlRpr6pg3C1Z3ubHnXZIz13jixmzwFjKKY0iGfJ0H_nlop8aLclVJpUMuBYg_ntcsH5imxJbVyLgdFgyO1BGlHY7UMNbcG_nAK9Tj5uaFWB2BjqBF_dndJj6VjqvvW-Ez86sV6pXV8TwclFX4Mt3h9Q3oBy2rzeu-F-q8MA6RjOMRssvn8n-6ePCZ6SdPSyNCQPU7zF90lK5YL0oBOa3hzn1jMk-tZ3wB1wJal7Ob-txNWAK-dT_ZyodM6HpUyWq9G56qKfKPwU3xw9NPJ1S7PhXmrUJkPqsH6hYTfhctnDe-DMxyYOv2BZjJxrKI5ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCqY-zJovAm9rAJn0fnzL5XieU0RLs9fNAttkqXjQO-J7mHvEL-UCCBaAjN_klKCdFjd2gXb_DxlYb-mECDu1JuaqdNfzX22CKjLI34iJAGtc2dWHfrZ2ukIo9RD8GuCjQ7nEd8X4r6RaL2-dl3Nz67yDQ1t2UQcWf4nITKhXsvKKOA3ji7AJ19fXHdrD7Lz5xScV7vU39W01gIMnT4TWiaHTFmn1K2HfpmVUjbSJmVZomvZlIYYdya3UlUPhgFfABmFyM09BOEkuTWz0eD3eAZNpLcTc7J61WnJE8p5Ej-Cm0LsrlnMLZVncXfgwzyeIxdph_hEPG0eWxSSIeyyQJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCqY-zJovAm9rAJn0fnzL5XieU0RLs9fNAttkqXjQO-J7mHvEL-UCCBaAjN_klKCdFjd2gXb_DxlYb-mECDu1JuaqdNfzX22CKjLI34iJAGtc2dWHfrZ2ukIo9RD8GuCjQ7nEd8X4r6RaL2-dl3Nz67yDQ1t2UQcWf4nITKhXsvKKOA3ji7AJ19fXHdrD7Lz5xScV7vU39W01gIMnT4TWiaHTFmn1K2HfpmVUjbSJmVZomvZlIYYdya3UlUPhgFfABmFyM09BOEkuTWz0eD3eAZNpLcTc7J61WnJE8p5Ej-Cm0LsrlnMLZVncXfgwzyeIxdph_hEPG0eWxSSIeyyQJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCYjecmpmrFCOxdy-hlTkv311eOK2ti14MrEBuVSbfeNUgeIDAyBS6zXQKMoURthY2orI1BlpBwzl8XYCH0_XIVbplg9_urqAsesCVdexFDkEYSWyOPCpTuE0g0KLogOi7HgnT134jyCU--vnXRDee1VpxU0HEVPhovQ0tiVZSNWqIEYRZ8-oq2LZ_hGwePqghliZXY9eWk2auL4g2UIpr1lB6JXTnEtgxQKkTtE_y9UEDb0VaPneg25SdaNRpX6_VWuOBfoIh_VV-R_XypDxnCkEn_sxWpvrSDZhq2hl5LbAQ-LkdQg86nLucdhflfw5rjqw85qxwg8jSUfyprS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cergmAuBH6t7xVWYtgBUeMnh_BkQ0y6HJIGAXsqyUB8P9Kkr50gXCB-dr6tuS2GXL71eeWNv1lC6CE8qL7juC4W94ofGaN13jLM3irxeudyQexxlK07QWd0XbWDI_LkvieBnhdnCPRHZzhICjtus_vfmWFlzoXRYGIoNeFn6_WKK2dbByyRK8hJLgZpFwFeIu28_ujNtN74lIlEQ8LCX_nbbqakauGSrk--eka_X60EVXkG9vzKR4E9oLJph2xAQJdPZ8vD4UOlhSq91iBXBHZvMpqy_9d_27vUptsuhscMNvZVkczwZxxNNIh3hy3EUyMYSZOv3w2w20qZkaG4ldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgGNLtjMcbU6zd6PI7NBgBUTRWV0n_owg3Opb6WQRj5ZcF0zCbG7rQUFFjrNxZD1Cjb01eaZs3tVNjVHW6sRUf0H8DukNcsx7rU7crwuiRwyQsFR06TCrIRAgYaRfOr0bNktA5EXeszBOVL8LX0z8vuxVi181Hjtg_ZSoZGWmhRZ6cnRFIUUfpG4dxKxC7aRIndNdmHmS5zHczx5lXXBtTcrJgIrBT5Yq8Mjmf_uVzxbx8ZWMHQMVpUFD-2lXVpHSe38Y96pWATXQdnnCMoGr5xzCxCG_nToEd6-bJ4HV56EE7X2BqkFUEJocPZSp4DEAN-XuIlD5tzCIfuOhPH8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=vn5r9CXmNEFkJIPLl7Vj2DSoeD8oACkq9lqTb1888Cn2kSY5tWYcFr7zCVCWGm3MMi35M5CW_3vJS9lstiYmZVS9ar5oK_3TKgb7VPgnUkoQSOG-iTu5lNhPyk5O8VpiC8WKkbAFtzdo-tvgq709cN88lkBPpg_CKpx27MlnvbedVnijShiRbBJArOurZfvs0wZ2FtJtnnfC7ScHhMzUaI5bpDAB5JhV1uUIygjrKYH1AeFu_SM79vvZjPpjZga_o53I61PVqUBaboOErzWM927s3c7quUHxuqYAk31c3_X7W8iQWhUidt0FAlBdonp5Slam4U2DGfHROWjzDkSJzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=vn5r9CXmNEFkJIPLl7Vj2DSoeD8oACkq9lqTb1888Cn2kSY5tWYcFr7zCVCWGm3MMi35M5CW_3vJS9lstiYmZVS9ar5oK_3TKgb7VPgnUkoQSOG-iTu5lNhPyk5O8VpiC8WKkbAFtzdo-tvgq709cN88lkBPpg_CKpx27MlnvbedVnijShiRbBJArOurZfvs0wZ2FtJtnnfC7ScHhMzUaI5bpDAB5JhV1uUIygjrKYH1AeFu_SM79vvZjPpjZga_o53I61PVqUBaboOErzWM927s3c7quUHxuqYAk31c3_X7W8iQWhUidt0FAlBdonp5Slam4U2DGfHROWjzDkSJzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZBrH2DiPuNzOq_3sTMkJGhJF5N2-qOu8XC_6GYxKQoFEKKbVLfSgstZopgELB1qwV0WDvO--yendJ8OZ9P6JCdifyCbtGCA-amO6HL_Xpe6Zq9jT8wvzOHa4q_gr0OZD3v2D08F2Pulpj1U3TEXllMTywtBHRj1TYek6JjLhUnNatv5fHyqeKdb3DZvWHlGo9eTwqNkSG6LXPf-cpGUQwpKyO_phO7_IfvbqZ24sJeT-mBpbpCzCs4A71KX3bU1isk30SUrbJsRlWQdKlq9zeQPIZn70UW3cseL1LvYkH1jmsexPvlrGAJUuHD0tB592WDxqRcEANRqCk62E_qYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIF0R-tZgWQ02Tl3RpU_nmKwRHumEoPBxgCp4EBVQr1QXvCEe9WmZ4acWfVKwraMdvLzIPShJthJI2-3fxG1vrDQmrLzs_mqajwGNrqreCWYfDx0NsHBsmTROK5Wr9OpPf_pRwkUu5PWZZ4RSuZvvyFxxctXD07pEEQbl0n6ZE8sOf_DnU08TR5UK4iS7ExhBkK51POoUZpX4cdXf3CnKmFEij2OEJgcHnash_TrFpBCE2EWUp-9dBwI87V9UjqM9kKd-k_h1HhCUuTPhGNZfsJQfcDtUCM9GSeVQsUeIpoRW-5j0kS9fO2zndeOCOhqBktU6K9r9TSdWZcyu3wdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBxEczKO_agB59vxTQPC67d_hGyU_OKhS2n2FFVpGVCqc3fM-D1CHG4GM0CYV0V196-nRZmU6MFUcr9jtsWBu1aLd7y3LgoBWLR0J0-Rj9gRcgXVbkTM3RQCyxJV0Cc_aj_70SxjyikyF2mAmrIWwtHKECNz6dWl8mQZ5-fibOedsmW9QySkT3GjvRpnTxaLnmfL6TjYYUGuX8f2_zJ5lPRUI3w3nk8GG4o4vIXkGYq3G1sIbLeJCrnG_KX89XKuMvLDRQsI4PN7f8jX_cyEppA5mwVQagiuscYphFMUnTTQKah09u54JOn9wneEkJQQzICSJUyNybDUfFs3B0dPPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBqxv3zKtXadXNR4JBSDMUqNAOi5tX_4H9VXmc4MognVaXSmnWkA6T8In-WHVTRk8duAbZ8FqMD_Ru360UY1EEJBFoOgqBkrsSRFh0MkQ103mtPDBr9QDHNPMBRPGAwlCma56TG7hTbpENexZrIvLxl1soLsTdnqO7ykpzDARno4PdpDxId9QZuMtUm3m9okmXGD-ybe445tInowf2K03AeRonmA9kinNTM24tw_mMo1vMioZpHP_zUsZ69zB3StBPLTHbd2L1BC-QPc388_OIou607ytKjfcwmPJ8FqNfUUgEwMxOPSOyoFtHNp2jZuYxKuVz_Nu7MqRVGGEQpl2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=ShchhzIM5fwgMXIB8dZrhy5kFjUkIRlYOfvWQ67y7D8Ea5kCGXoGmMrbeUsei0vspUNbiNiAsTsPYSbu6J8TjDN1OeRaXNwjCKWIy0QzreSp_tTMLs9FsT9_qBfGeMYx3apEDnV48j0h2UYmKujn7f8VhV9-Ue2iIRTCHdd8f8S8uFFDrLp3t7_qs8Fsktydjst83mTPnplwiAIGcOBnAUkvR7851ECi9FJQUSQ5SUMq21AzbGA6vZmxdiBygK7XkAlPVXVIxdrcBIGoYVffjZuIjYRQCkeSFyO7-SgtGPbwo5W3AMGFHSxkbRF3iQzCb1AHJS9yogv2Kh-uTkIMv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=ShchhzIM5fwgMXIB8dZrhy5kFjUkIRlYOfvWQ67y7D8Ea5kCGXoGmMrbeUsei0vspUNbiNiAsTsPYSbu6J8TjDN1OeRaXNwjCKWIy0QzreSp_tTMLs9FsT9_qBfGeMYx3apEDnV48j0h2UYmKujn7f8VhV9-Ue2iIRTCHdd8f8S8uFFDrLp3t7_qs8Fsktydjst83mTPnplwiAIGcOBnAUkvR7851ECi9FJQUSQ5SUMq21AzbGA6vZmxdiBygK7XkAlPVXVIxdrcBIGoYVffjZuIjYRQCkeSFyO7-SgtGPbwo5W3AMGFHSxkbRF3iQzCb1AHJS9yogv2Kh-uTkIMv4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=HEi5AVPMdj4-poB6LQK5jxnAXEExCYG9eZuwSA672gXaCWVumKSEOup-9m8EC3i992n0raLiMgJEzmeOG6Rug9Ud0hb_wWn42DuXCPyYvhbGQqZRB0OlVet6i7MFQrQ16eXqvNxc5pltCT_h-MsB4z6lsNcaqY5VaqCDj5cwtEaigPVvZKTEAix_I-_B2Ai9RJmD-YPsUKhsl_M2MRwIboOMZhkigl1yzUA0g2Xay97xl7zNpnBq6f7Jj00DnhXk1M4Z58Ao-UWvak3mxuKWu3nvTHTkjqHDUnw7ZieCKoTHDolTmv7hUSSn2RNfAlQXzwuoWV_5A5OaGoIzGG2Ilw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=HEi5AVPMdj4-poB6LQK5jxnAXEExCYG9eZuwSA672gXaCWVumKSEOup-9m8EC3i992n0raLiMgJEzmeOG6Rug9Ud0hb_wWn42DuXCPyYvhbGQqZRB0OlVet6i7MFQrQ16eXqvNxc5pltCT_h-MsB4z6lsNcaqY5VaqCDj5cwtEaigPVvZKTEAix_I-_B2Ai9RJmD-YPsUKhsl_M2MRwIboOMZhkigl1yzUA0g2Xay97xl7zNpnBq6f7Jj00DnhXk1M4Z58Ao-UWvak3mxuKWu3nvTHTkjqHDUnw7ZieCKoTHDolTmv7hUSSn2RNfAlQXzwuoWV_5A5OaGoIzGG2Ilw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=i-DSWvK2j9Z46qwfqOsAIYXxRAyuH44EiW923CBYuNPHiivMevhgl7F4WFOTAqqwBE0vx4uIIoz1bQjsFOTiKTI4K5Y1rvgcnoPDmpDl4YczL8qtc0bPOVCyS7ruyIuEezPmzT5S5YAeb9g5ICw2JeJUZiaZxnVixWVUVZT4JjiTXbK9a2AUd9gJJCrtvGXMUpOBGBg5mjt7W492VzYslP-hqP0p933TTWZDd89lExPlKZsuXlCgwOT1pzKUxgdkN9E_EqCgJ8I0aZpKmupFkgwxcgbMYuwsxBRtWXoK_wcNeB6MIxbh5cP0aDtTTjQtx8nNggmgSu5ib-1zjsdMLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=i-DSWvK2j9Z46qwfqOsAIYXxRAyuH44EiW923CBYuNPHiivMevhgl7F4WFOTAqqwBE0vx4uIIoz1bQjsFOTiKTI4K5Y1rvgcnoPDmpDl4YczL8qtc0bPOVCyS7ruyIuEezPmzT5S5YAeb9g5ICw2JeJUZiaZxnVixWVUVZT4JjiTXbK9a2AUd9gJJCrtvGXMUpOBGBg5mjt7W492VzYslP-hqP0p933TTWZDd89lExPlKZsuXlCgwOT1pzKUxgdkN9E_EqCgJ8I0aZpKmupFkgwxcgbMYuwsxBRtWXoK_wcNeB6MIxbh5cP0aDtTTjQtx8nNggmgSu5ib-1zjsdMLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFBSFEYwihq9EjIvxtOZNHhiw2AVzhDouySbYnDLe46KhW7eYRLCiOrWhAOn29QdSgkdVtR4bcs_st9F5HCeDZuRWjIYEoYX-hQ9Jd4MUZ_T-j6SXxThUEhInvj1_qHTCIJCEJ1aBSYeN1zuvP1iPo9cqSJTjqz83Tb2lsFD0Dc-GMFeU4teE8z4D5n0e41EeChf7MfHvroo1b21md8I4tmeOFQsXTAY_wIVkmDXoNKhl6bY6iMfELDkucpPX6_y_r_8gcOcbxbMvNwvPmOIfhO7BzwbkQ_rsz44yBQ8Vos3NAQoVsepY_dNoYsIzjshQ_gYEtm8ErjEgmzRoasj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=V7ceHd2OVz_gh5b0uAA3dBOkUX3e7u6q-o2jIIWYskvvHF9bWmOjaRi7raJLggN2wFhSGfFWt1L1f6_TcL6fycH84LdVxT57LLchRYh41YfNvOsWJqValJD2raF-DuAhcAnX4Ri8Eaq1HrrhC_lJbmKcHWQsfAPtoqkVAnfnPk_lwXSy78aVUbmFpvx1iLNOhG0JC3Jvq9RGSpkJAUO65daLcqmlPBatnu1OHYKQ9ya-WvlDHsilxu0qcY3v9JXpMc2RZeq1YTPDzXWKnLdLaf0qoMJgKUUrFokC-HvOplDbVBc3s8QZ0j5Io-gIuLF-XMY-7f0KGIYf0tR9AEYeLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=V7ceHd2OVz_gh5b0uAA3dBOkUX3e7u6q-o2jIIWYskvvHF9bWmOjaRi7raJLggN2wFhSGfFWt1L1f6_TcL6fycH84LdVxT57LLchRYh41YfNvOsWJqValJD2raF-DuAhcAnX4Ri8Eaq1HrrhC_lJbmKcHWQsfAPtoqkVAnfnPk_lwXSy78aVUbmFpvx1iLNOhG0JC3Jvq9RGSpkJAUO65daLcqmlPBatnu1OHYKQ9ya-WvlDHsilxu0qcY3v9JXpMc2RZeq1YTPDzXWKnLdLaf0qoMJgKUUrFokC-HvOplDbVBc3s8QZ0j5Io-gIuLF-XMY-7f0KGIYf0tR9AEYeLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=cmz-lF9G_5H2MOXFLX0f_vMYdlACIXd2bzfeFGR_x2e3e5q57ieyDsz7GB6dmTy3leSgSIBc779j9AYoueXayUr9MF9mBSQE_tKdJo3qFYbpQoCZNEmVZHo1xyWSPoTOHS62IiVVF_sq187RolfbwEGETpISnPdMIwTSaIhTEC-aVBIrRD9LxvxkPnm6XRlxwJEnMmPZaaUfxWEHUtGvDGVUU__y7YnGFwfDQMf6ev4ZCdEYSuYmWI-mWALA1Gmtr1tUXoJhamOiW2zdLUVEGT8LuuNBMumwZ8e2jNmTjEchqtSA9Ay0ObvHJOCO1PTa6ZHi0KuuryU9i6RERcr5LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=cmz-lF9G_5H2MOXFLX0f_vMYdlACIXd2bzfeFGR_x2e3e5q57ieyDsz7GB6dmTy3leSgSIBc779j9AYoueXayUr9MF9mBSQE_tKdJo3qFYbpQoCZNEmVZHo1xyWSPoTOHS62IiVVF_sq187RolfbwEGETpISnPdMIwTSaIhTEC-aVBIrRD9LxvxkPnm6XRlxwJEnMmPZaaUfxWEHUtGvDGVUU__y7YnGFwfDQMf6ev4ZCdEYSuYmWI-mWALA1Gmtr1tUXoJhamOiW2zdLUVEGT8LuuNBMumwZ8e2jNmTjEchqtSA9Ay0ObvHJOCO1PTa6ZHi0KuuryU9i6RERcr5LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=moFYLSzz43Cm650z1jiRvMiqtfdKfAMIKiZ-dM27qpDkhHy3SnzH5X4A3PvTBThDxFFmTTiszdd-90eSmc77E6dIDE7qOz9ecCADnfhl8xnjgVsvDYmp_U8GTKbOzXeVUzXj8FYeHVOEDb7_ZC1GvnUDWajyJD7Dn8u5MCdKcVHuFc8IcYPh4y9PJjYG0DYd7NPCE6ID-HDUTskYByeMphd4cp9DDu3D47O4-PKUY1uV39EMEEZ-w2i9fCVsHBVh0n9QU74Za0cvDCM2C9JIq32g2j4RGBMjm6L6KIZU_x5RSPTXnRCGiWZvz1_MlOSOSehG0c6cdk9nOI9yCQXtYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=moFYLSzz43Cm650z1jiRvMiqtfdKfAMIKiZ-dM27qpDkhHy3SnzH5X4A3PvTBThDxFFmTTiszdd-90eSmc77E6dIDE7qOz9ecCADnfhl8xnjgVsvDYmp_U8GTKbOzXeVUzXj8FYeHVOEDb7_ZC1GvnUDWajyJD7Dn8u5MCdKcVHuFc8IcYPh4y9PJjYG0DYd7NPCE6ID-HDUTskYByeMphd4cp9DDu3D47O4-PKUY1uV39EMEEZ-w2i9fCVsHBVh0n9QU74Za0cvDCM2C9JIq32g2j4RGBMjm6L6KIZU_x5RSPTXnRCGiWZvz1_MlOSOSehG0c6cdk9nOI9yCQXtYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=ZSuPu1h_sqw1EE6cZHLnWglhXwcUecyfafg7TlegXvDk_bbUicwlrosXFUf_qrp9VJpCaxfcGQWp-oYUaipS4wNsBcZ4jyPE1SVMMusboMyHdxmCj16Ltf1_TZAgv-B0_B-Z-HVTJmeVX9yTa_G2nF30Bu52OFw-ih8J7F5jKlYMRHgwInC4YsAHbCsFP-THkvtYsFTOccF29UjqNlcy3mD02ihyZCotn9AV_keLsoImONh_Mvh2gQ49WZLhtRTiytubOuINQ7i1-IbgjU8tO1W4UyJWJz5pva5B6Jw6_XqJmEQneRLxTgOOWue-Nci3DTYmFyXiiJpGDNvZRMhrhz7EdZnaZas2J2ayYL4j8xhDxD6vlPPV8CmLdBU6cOWZ16AC4cZZmtlPFbU27Z-iuBin_wPyeS6CnfKJmX-NPCKOnOqwcxG41V99H9MC9ONI5ehBaRAODK4VeM61PAqEPm4BVqHABS9OPgPJ-oAYsfC0ntRnrIR7srG-2p-oPy_Gi5UmeyrlsOsCHgpQiIlKLW_XDcAX-2ecIbQuB3eO5MwG-Z3WAtU7phvyqHjhch7Pb0BuMHJiyRxV0QYz3dMKDpJQ-R9tyUWRkVOH9Ul7e9hb-HLbrK0I0eIK2-eM3cG-rMd3ITJftq17jgJojfMIwsGp8iC8cHvxyJnDOjH8pCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=ZSuPu1h_sqw1EE6cZHLnWglhXwcUecyfafg7TlegXvDk_bbUicwlrosXFUf_qrp9VJpCaxfcGQWp-oYUaipS4wNsBcZ4jyPE1SVMMusboMyHdxmCj16Ltf1_TZAgv-B0_B-Z-HVTJmeVX9yTa_G2nF30Bu52OFw-ih8J7F5jKlYMRHgwInC4YsAHbCsFP-THkvtYsFTOccF29UjqNlcy3mD02ihyZCotn9AV_keLsoImONh_Mvh2gQ49WZLhtRTiytubOuINQ7i1-IbgjU8tO1W4UyJWJz5pva5B6Jw6_XqJmEQneRLxTgOOWue-Nci3DTYmFyXiiJpGDNvZRMhrhz7EdZnaZas2J2ayYL4j8xhDxD6vlPPV8CmLdBU6cOWZ16AC4cZZmtlPFbU27Z-iuBin_wPyeS6CnfKJmX-NPCKOnOqwcxG41V99H9MC9ONI5ehBaRAODK4VeM61PAqEPm4BVqHABS9OPgPJ-oAYsfC0ntRnrIR7srG-2p-oPy_Gi5UmeyrlsOsCHgpQiIlKLW_XDcAX-2ecIbQuB3eO5MwG-Z3WAtU7phvyqHjhch7Pb0BuMHJiyRxV0QYz3dMKDpJQ-R9tyUWRkVOH9Ul7e9hb-HLbrK0I0eIK2-eM3cG-rMd3ITJftq17jgJojfMIwsGp8iC8cHvxyJnDOjH8pCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=bdp-Tc_yVFwBwXEI1ofnbgr_0JiyEIVv2UvimCUvi0g60Jzu7lrD4YagEudd7sxrvRIyS2Wynzk035H45WVIHyfD8DByhbuTcnLPwHvtuo24Zk-l5NB_WZdLCM1FTDOHFJbzUBPYswBUjW2WjSQcbGvLxzEa6cWq8eu9TP4gwIQGBlMhZQwB3n0sCrQP0tJjWGYez5x4kQdwgwzYZQEYQWGzfpzLMmlCUxYChP90ON3-9piHWS7qkvw8YheggyZ17mwHqPSs13k7xUDPa4XeyOut0wRCLJ0VmdeFI47Ho83-0AIyt_K-HQHLJXAWJ62ubGGoQlKXK7BNS0OeZogHqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=bdp-Tc_yVFwBwXEI1ofnbgr_0JiyEIVv2UvimCUvi0g60Jzu7lrD4YagEudd7sxrvRIyS2Wynzk035H45WVIHyfD8DByhbuTcnLPwHvtuo24Zk-l5NB_WZdLCM1FTDOHFJbzUBPYswBUjW2WjSQcbGvLxzEa6cWq8eu9TP4gwIQGBlMhZQwB3n0sCrQP0tJjWGYez5x4kQdwgwzYZQEYQWGzfpzLMmlCUxYChP90ON3-9piHWS7qkvw8YheggyZ17mwHqPSs13k7xUDPa4XeyOut0wRCLJ0VmdeFI47Ho83-0AIyt_K-HQHLJXAWJ62ubGGoQlKXK7BNS0OeZogHqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=W7QJb8hDjx7rOB5ENkf6B_4kXQVSM4qJqJL1vVxFMh6zHg4TUcbVPtEEOt-iGod_5rMo5Ot7HvyKXfVPQsdsQVs0CjBGRk2Cb-xzkp6RGzLYvA24eMDW-mnfe1pBnU-h9rNN2NXHzFxBRMhAIGQf84j9Mp2zBDLPXNVm8wFrUCxVcpt4BEy3Wgicdpyylrrg4Ay42376cmvg2vYd1pEFf7zEbJySjs1Kqxyy_h09fFPYz6lwVBxW5wWtlliQAcLQT6ztQ0cqltvNglwaVDZZV0ledTqLaEMFKI9Wx15Bd5dOji0tg3vBtnns_yvQjqKpvUENbIOHYwLM561YrrDVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=W7QJb8hDjx7rOB5ENkf6B_4kXQVSM4qJqJL1vVxFMh6zHg4TUcbVPtEEOt-iGod_5rMo5Ot7HvyKXfVPQsdsQVs0CjBGRk2Cb-xzkp6RGzLYvA24eMDW-mnfe1pBnU-h9rNN2NXHzFxBRMhAIGQf84j9Mp2zBDLPXNVm8wFrUCxVcpt4BEy3Wgicdpyylrrg4Ay42376cmvg2vYd1pEFf7zEbJySjs1Kqxyy_h09fFPYz6lwVBxW5wWtlliQAcLQT6ztQ0cqltvNglwaVDZZV0ledTqLaEMFKI9Wx15Bd5dOji0tg3vBtnns_yvQjqKpvUENbIOHYwLM561YrrDVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy724MYJOm4y12YQ9Z4SJTdDZRujzfLrhAvO1ivL_hgPJHbKKROkNoQPMptUvv9oB32aQfU0esMn8JajGO-GSFJoquRWcyOiMitlygti20HuQbPWInv0ta3v6MzUNVYNE6JwW1oDZtORRIMskdz6hgTZd_IW3z0brcskbdlAskMpRSadGZgWxpl0pGhxWzs_6lLvLn2YmzT1R0zbSorQEn0Rhq8H3gsJkaypoNHiYp-q7AAwnegmf11XV0N9wvzxz1a0biMRNfDHD-2Rc10nnvcjBYFFcS9mxQWDghjgDB6XG4BjTl-GkiNLRU-3YIQrAhvdZ902nbnI5fXT1wyicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4ePSjU0dUsxSRUQcgtKBh0GfsGw3CxO1_RhUFH8QbMSMX2MfSLqGnNdLXN4v808s4sZOK_hnb6HpGqP01FmM5fYHMldRlG9MvOHAwcc4gvJ2CA5aEkSDifpcaZDx1m3pq0x-4faP3nQm-im-a2dDbO2GmIP69EF_jVkn7idz4hkeVNKZxyeUlMW-e0N15Ganuh6IwtHO5F6c-lJbtzoGCKA7RHYPG8ALk79TViphWAzrgvUrkvRgGpmMu0DHckKsuhkGVKUfcbj7YU4j15Y5EAUPXFZuadtgnR8awIuc5PZnsmATFV6t5hIhdG2GGmVpbKY4jV6UK48vAJELwKTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=sx6Wn83GuLU4UMHzEtOpSBphPSHJYdILFogUZYMW2AsZDgXe5vAUhxR0lM5j8fEiw75S-U482Yl83wu7ayyaGcUYYzicTwWvOdzGn_XNosNAtp0LdJgA5dtHJ-vReRop_OFvF2EjOJacyum79SEa8DExZuayetZp_qnykGyHUcMjxVPEOB-OcMMBTTS1UjgpexP4BRqjaeQyC6K4_uCHrKb85ACkzFhi3qBRPVSZlQeq0wG3cqo8tbsnVvwbZ2cv2bHSMJjOLuXoobcmkulTHD5SzaGGI3zrRIRym4ju2ZmCmkBKg1XUbnsO_y8kV2ysEkIF-cvWIUJPoUFnXfiBFFHWh5adBJ6yhKwf8YchFEdrgeWW1EBHRRTpDzEiruKZowpVXs9_1TvZ-WuNd_kIN8Qtei7Pzo1DZjf7hBll47wtXDjPVHNlXzbnD0e1YfmtvK5SJZ-HGkGaxXs7GNaYEbNYGvzV-7v15BnFeP1Hftfeybpyps6a2VuGzg1oTqLDIdSW5Yy_RhrUD98mruUu_dm4-1feit4XlPGoSUFJTSXhV-5bWtMkEF3DFKdlnv1heSzgnLoWGiH28hHXLxKyxTKIb76a5cpmcdSxabHWkqfNPJlMo9V2nUy7pw5XVPR-CmeISxT_6YDyF-NSFrm1DGOEaqdVHGXeElHvEuT1wYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=sx6Wn83GuLU4UMHzEtOpSBphPSHJYdILFogUZYMW2AsZDgXe5vAUhxR0lM5j8fEiw75S-U482Yl83wu7ayyaGcUYYzicTwWvOdzGn_XNosNAtp0LdJgA5dtHJ-vReRop_OFvF2EjOJacyum79SEa8DExZuayetZp_qnykGyHUcMjxVPEOB-OcMMBTTS1UjgpexP4BRqjaeQyC6K4_uCHrKb85ACkzFhi3qBRPVSZlQeq0wG3cqo8tbsnVvwbZ2cv2bHSMJjOLuXoobcmkulTHD5SzaGGI3zrRIRym4ju2ZmCmkBKg1XUbnsO_y8kV2ysEkIF-cvWIUJPoUFnXfiBFFHWh5adBJ6yhKwf8YchFEdrgeWW1EBHRRTpDzEiruKZowpVXs9_1TvZ-WuNd_kIN8Qtei7Pzo1DZjf7hBll47wtXDjPVHNlXzbnD0e1YfmtvK5SJZ-HGkGaxXs7GNaYEbNYGvzV-7v15BnFeP1Hftfeybpyps6a2VuGzg1oTqLDIdSW5Yy_RhrUD98mruUu_dm4-1feit4XlPGoSUFJTSXhV-5bWtMkEF3DFKdlnv1heSzgnLoWGiH28hHXLxKyxTKIb76a5cpmcdSxabHWkqfNPJlMo9V2nUy7pw5XVPR-CmeISxT_6YDyF-NSFrm1DGOEaqdVHGXeElHvEuT1wYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwgxTs7hQW454OR1JTJ21-_QJ_hN3Gtw5Qu9haPkKvnwhDNFo2KnmNUq0NXwhAy5r3le9AkUwmsfEXmbvH2_lZ5E5F32ad4vYH2Y7tzoznyZgfypdQIdazl39VbJ9uwe1uJtFuW8mSvoF0YNF7NnX50t1ZR2AvUT8dTUJfw9tOJGtWZskctLznGckvp0KwP0vBmEnleD99Nix_NuwvRBY0Bov0-wXqHq4IArK1E5cmvNFGV7lKpAWtxBAbFcv6n27zCBJlilxXYA_DYmIWE0tfvzY0XqiEA0jPXfyGGaeIA9-Xkrde2cwxJNwnJw5TL3_AIzZFYBknmDJt8FmZGfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtsjU_xQ-N2sSzuJBJf9brY-LFNUsX9dDdyuNCcDmTrqh93fmnT8YKNjHLxrcqJgJw7pYj1xr6VxQWv82eHGaR6el6MXqAOMP60BWgbzpzehZCgm03su8ITHL76KTLkfWigFVYmTwMdA7r6JetM3cnA-JvMbJcXqinJMPydX425bqNA-jZMDWm1X_GvNuo_fzrx7ZDEE1bvxSPKSxzU6YaVBOf61tj3S8LJhkqD8DCixI3fW48IJL1wZOa_wtLHSPGxD6n3VLPgzc5ZzVnJyqrKusu9Rb1xDIeQAa2qY_JE2o63KeYzIrVMQrkWlPoMYJz35yK4TLlRqy9x9ereMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtemNaDcyWZB5ljGjpfZnYolRy9g4nG2OrfEsL-zqBTUZUl9lMl40mM4StDa5cH6A-uw8eHWwkppv0wKqc6q-CEar-54OW-rxcAYgUTc2NlpHD_gCW2Xc9neb_eMwWxIhOnNjXQ8eNfKJWijFNn1hY89oQOl_71ZZCVSKP8_sTWSCsbodOB0AheHjbk34WlKRCn_IUF1vFmjLJpEZ7ne_RIRhNGsOnsXHBubkX3EIf92M8bCvrVA2FTpNWHqQvBm7Lc0-4IWjfOONBYCwNHQLdbAFCOXTSRBvfO1Vo4CeoYAh2c1BCrVy8KlGwmnVkbLNb-PYKDb-0_BPj3OAyhprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVGpQbWWw4d78aUmyXn48RzBrCrRpgPYWP4JmZJ-UlUlCEH7h1a6janbk0Ghn6DD1V1nzkKj8hXhFOS30KpsKDa3Yk-1DnyNojRvzGLkIoTFq2InAiLUhTiIufaasLh288f8kITG8Z-ppVSfJTHKafCLLPKfD_FCvljwbX1x8yPI8Fh1qfSuSKJqm0jFvs28u01kgHyRmqPmE1maGgMiYYUZYQYS0qE3IpiJ5IFNfqms_LceTnCKFCnhEaerX66_w9zvpqrMnORXmwmXgm23i-V5EqWuqV2dPcKO5BvnkwvhaGaJ1duuIoiB2hrq684y46d7evjvLhDA49U8SVOsKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=E0yUf6GV85M8AgQw8GjamcJMKM_FD7T1L2OGqdsCvAe0hTzJvsOg5igiMspo817w89TwstLlue0wmB-9E09cVF_jXoGzu5u5RvbvrBB3ooAvN2N4BN7TJPCyceManXix2hNMUqwiZyjPx2vfJwUAm_Q3oiixwWPS2_kXXWlNqnEoMJLitqrmjxz9vtKI2ANRbea_u1z21eielh2i9lfnxV_DNf5-cyqGeBHnGBt5uM1lzDWNi880_kvrHYojlK_c4H6TeGfiAM6xvzl5mQoo6G9_j77QWpRKZ8akCS9afACElYi_RznkW4zHfLQg8EvnHN8hJBkmFqU0sZKxWQfinAzeFSS-PHf5oRhabLGVT3sXPDuvpgpPnUMWKuAx44r7741dFnYQ8Ag78CZL1_6R-grGeiIeBdS15zfP2CdByIvTtvRFmV0iSYdieIn_m11Dd2nJ8XWOoRB51SzkGd1gRuz4dZ4eu-oJIPYJRNFmVqa7uQxMHXF3M8brB0Vzgr5fHIMapjzAgKCQ2VOfbvz1g5mUOlFWoduqZFqsgv5yWmnyk4Gq--v2u2DLWGpUf2xvoDJcd-_MMQa4cpRfzwbby4VTzoSy1W5PZvPvGPDW3Dji-ewZeYTt-hMsw_MFAUuQATw9q0-RQ0g0IigumKRyXeeo4x7EeDKgp7xCxYx-CIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=E0yUf6GV85M8AgQw8GjamcJMKM_FD7T1L2OGqdsCvAe0hTzJvsOg5igiMspo817w89TwstLlue0wmB-9E09cVF_jXoGzu5u5RvbvrBB3ooAvN2N4BN7TJPCyceManXix2hNMUqwiZyjPx2vfJwUAm_Q3oiixwWPS2_kXXWlNqnEoMJLitqrmjxz9vtKI2ANRbea_u1z21eielh2i9lfnxV_DNf5-cyqGeBHnGBt5uM1lzDWNi880_kvrHYojlK_c4H6TeGfiAM6xvzl5mQoo6G9_j77QWpRKZ8akCS9afACElYi_RznkW4zHfLQg8EvnHN8hJBkmFqU0sZKxWQfinAzeFSS-PHf5oRhabLGVT3sXPDuvpgpPnUMWKuAx44r7741dFnYQ8Ag78CZL1_6R-grGeiIeBdS15zfP2CdByIvTtvRFmV0iSYdieIn_m11Dd2nJ8XWOoRB51SzkGd1gRuz4dZ4eu-oJIPYJRNFmVqa7uQxMHXF3M8brB0Vzgr5fHIMapjzAgKCQ2VOfbvz1g5mUOlFWoduqZFqsgv5yWmnyk4Gq--v2u2DLWGpUf2xvoDJcd-_MMQa4cpRfzwbby4VTzoSy1W5PZvPvGPDW3Dji-ewZeYTt-hMsw_MFAUuQATw9q0-RQ0g0IigumKRyXeeo4x7EeDKgp7xCxYx-CIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=anSu_ewjFDZJvIh1pZNQ8yVrw-XwsVblLmfQKZSj0F53_InUN50v_O941wOE8I1SWaafMD40_Tmk8yZ1KzefSlfdNWsHfLWRnOjANYCX1ijNmr23j0dWyxyc4t6Sp9YQmgXFPWgUctDMBSgykpbrtqhcrfCiNZEcqPuHhbFLxyLHvO3X7nFT-aOzNsW98CZ_SGFdoxMsgkPkHg1pU8-acWtUkmHj999OZqtAlnxKVRTfzRkKo1ZJzerT4dPcQ07K8drq_EMMGhjzfZri0XSacphoIK1B3_pRZPxk4aBn0NPbtafuDfEza8hEF0iO-ZP5C7xExSJmCq9xTzXAymkNbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=anSu_ewjFDZJvIh1pZNQ8yVrw-XwsVblLmfQKZSj0F53_InUN50v_O941wOE8I1SWaafMD40_Tmk8yZ1KzefSlfdNWsHfLWRnOjANYCX1ijNmr23j0dWyxyc4t6Sp9YQmgXFPWgUctDMBSgykpbrtqhcrfCiNZEcqPuHhbFLxyLHvO3X7nFT-aOzNsW98CZ_SGFdoxMsgkPkHg1pU8-acWtUkmHj999OZqtAlnxKVRTfzRkKo1ZJzerT4dPcQ07K8drq_EMMGhjzfZri0XSacphoIK1B3_pRZPxk4aBn0NPbtafuDfEza8hEF0iO-ZP5C7xExSJmCq9xTzXAymkNbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk5KJaSsb2HEJaT4V0UrIJ_Ud-EBOe4oQUtF4grE5YQeLHzfwp11YehA-S3gEmPlhVMC2kWkJIifZZVvOc0d2W8dPLi54Iz6rKnRN-_lhyyKgIVwGIzewm73TQlNwwUw11DwrJnOmIVHqkE7nRDESmOWmcdiOFlwp1GUpPWSxUhB2pfI9E3_xgJL9u2qN2FsFBECLgf_VTq5DV-vnxdLSxGRg8gkI4UmIicbHvHzsSHkgtwa8YOqhOuf5yLeBLmIAd9eMkwSjaPVSHvUjYwwTLzLZao8dySHPNnwOVcJXwKPwGo1G7omaXaUKOuk_wh6lPdpfdtvZjZzPPR5bvnxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hemxTI605OXeWP-5hm5JWDE08dGSRXgyXWhOHyXNNVg2J-3J7VkNzi1tPWmQUb__nIA-aelSEUwFBiSAX0IJP-YeBY7Rf_cyjYmW9PIlPmNDnwYH3C9TRkv7fnyZdpOhAKSF4roo-Ed_tbCZpYjipDrXLqesGgiGCx1mL3HKyYZNZzLXE62eerOVAGk5izesEq9bKQs8HCcS80-IB2WY2ucJe9gqMEp8LeIfci7nLywInGHMkAn4kun8QzP45SOfrPegn-SUF8WK-HgjtpT3ClCnXG9o2PFfOVEzQdd7TjA9s782kdKQnf-bjXJrtVWneAwrQLxdM0Wv0UB-uJXE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEEVpSWNMUtCgckFYgfjE4b0vw3Y9QJ3K6AWm-9TH1oJ43LXRvklaU0GI8SDTGkN7plqNBFyiwOkmlquIbEIjZUG7vb0trOvMJEyHSfthtXd4FJovMUSIDgVcFby4FRyTfLZwyJc19UejF1SDXmhzF8TWpEDTAgWw-gZu3-pyzG_DSusxFnjJPD8XsyI7tm3s5nRNzwmCwo_3jH7Fiz4TR-YRg1CC8_MYXh5qg-gGFozgqoERC2j_N4TRYnHhQWZLfkg3hjFyWuybxJjuTWxty8V_ZVL2N9yoBK6rXF295kIirfueFPsPTtTsWBwPn0hZzSoms0pwUd7fhkrIe4KLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGU4Oluq9OfAzpeMBHwUsXEPFgLxuMLEeNdHStJUHeFQB0rl3jGQ97t-S1kW-7wakaUZC92AgY-h5gdnVmsd9lhLd-krljUVweE2FNFHOG_dQdOb-0eA6McXr8LZOeljTV8iJ30SKFjakgnr21P83WQ063bzfqrGLxN-SOc8D0xomVv7846q1m1tYqeNSBK-U0sd7STMJGdoavct4nGx_FfUPi9m5FRjWkI36Dt-HoJczFV4naPTAHy-eaZZA0s5VmQEdhN0ITAbTJEt1DCsHSYvHaugjQoxos5HaYrz_Pym2rg707ROfyhTuVJS-WY7-DGQ7OacaVEWPUH9pEw5RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dROwj1ZcNEx8EcMieyB0HNO7KeFPfWuwGN9oUR7BTM-0_EMiC1ND9Ht47986RH5sY8JZMGNFHpIUVC0az9pUwBeD15KS4VPoroiq-tbNTPklBMTF8L2V0fgqTHrWJqK-ODPvcqJBvbWIZyEKEmbL3YL3QLswokNPrk82zo6c3hOThHPCNlXzxhww9sypvc3MIO0zh7peI7VnsHdfGvAVzIhuA-Mn3lZUTFA1FKaQ70naw543ycLrbOUO3vNeKKyE_wLCs4BzNtxryiRaXob5tTaDC-Keb7PGXkYG9YiSDU2pHwY1CwMZIxsFAFRX96IG9ewwkLt_MB2IPAH0J21piQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CghIvN3zRe68s1_YaVZsx-CBFth69LMLFbtV5GO__XsMQg44M-SSKNhta9raT0NfUHa8egmgsurXBbOBtP4j5BV4sj-BPrLuQoe27jK7MvrXd0N6XRqs-Gk2v8YU5ijaoOy4E_v1h5O1bNgTk515UG01LH13Nv8eh2R5-qS6aoAM454d1JEU0pJbeZFGJVRaQxiJH0cg1MP_aphAjfjXgiioBKeH0bQqJa19EE1FqrQt8VbmqWJ4Cj2Tsv3-5tLvNOxrdoV4PArkvHhkeG89Rf2MZsyCCs1Qfo2vI1zCyT2O8sragIB4pTdtiv3QWddWiTVYq8X3aWj9DcutQTsp4w.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
