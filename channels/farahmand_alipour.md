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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 17:54:16</div>
<hr>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVHNyHPeagSnxkwEfmIrKKeiocZOMLHac-Ampa5iYk4oKWnbnUQ5mmDpj43K9ZZi4ScMe-SFPpbMZp1b374940tv8hyRarAZClhCYlCNkGyTcpRQds0j95atYiMfifXFOZGGgkLPwwPfCRVRR0k1WTNcrkBJMJgZ6qvZk6wpv8qiVbtOlxQqaTASMiclI7q0gZK8jMWIL2hhoGbNqhuD_Jfle6Y9VBm_9GALlygBHfOXYwj9mjO04vM28hgbpjJbAiRy3v1y4AFppInFPv60GbmuRu8QnFNqagehXpjfvLfF9y6oQ41jn-rk4p8tS8jLs4_knXKQ7Fkm41mt_U8Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU03JBBIUrINr83zJT82G-VOKqE8hOi6VDow9Vk_JrqmtdlDqAZ4VWG2z6kPYKYWnTvcu1ghQYhN8YxdE3WNEs-puYUx85kYY4Gj7TJ1HIHBl-Z1qC3StQRjFiHbT7CppiHHAE4v1oZPOpZUMXOfdcUN1h9ilzqqgRBd5aJhbmIOAabbejFL_KnA94YSUmqaZULOPgbThc7gMMVMBuJCRXVs-BoDbGEmpCSNmoXpnK2UBLLuvWLwEo0C_AmejZoVeeOOmnT1FrgCm600e-Zya7Q1SPA1SiH57ooZqksGRi7Mt7Z4_If_Z6p7vDT3ipcJFoN3pXnyeMra1mG0EJK7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6uXN6AIS_5MoIUxC8Y7ktV9p3gNfFu3TR5dpzWtVtsp3ak8GY93NMY5gwTvkLt2EP0AgE26uNAI_5mZ3VS4yzWja7DE6sXcoE56ogTN57GbmcmCRrA99--Vl-uze9Smv4aNX1gBfVF6WnA2ku1E9ydTd69jXDbsfeB_G2edKTeEithmOACjtkYiRBGD__x46cvX0KjphzHYInXTjdn8nNCCb30QIS1IOCAXqrqHtx1rzduST8WOJdn3jn7vio-1fxqGa-uTmg-MMfU57p15zqKAnsO24gUa4ZDerk2oI7emoQCiqoFEElxZX4AGfdV1oK3aX-dd4PJd0FfIrBrWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWTwy7qFQ2leTVpbUv0pOGtqMnDhsmyLo4z-o-7nBI2Z9F-kTUxcrkDAT5LqcUt552dWvAEuWPEpjjnmmQXYZbj6mfmjnjmLYNLWSqh7t_nZiOrsD4hbTQOJ3bPFLJOFM4rY3aS03vNsSYxBaPY98YeUarOaw5NYg--fxUelxAu6kTC0VqWTmUs5mx6BMIScMXFqhTYuPA0aZeumcBVXiLhD_TRtTPrn2kv9ji9Id8Zw7LmmRqigFMptRZ1imxhuFRpwcq4cDbVXFeeDgRFabmVzuiMwHPHiKXCXGuf_jr8lhUkRNi-yVFxHjvTrbzGru2gea75qwjg1ZN8aGho74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmoQU1SJHWKFiRuqWWrJ5VflWt5s5N_bn2cxU9wmKke8h4iTyDG66E4n8tQ339OA1-Q3gHeGPf_PoppA9Rq8mX8X11AHr0LNbcGeTPmYZ_hhyAQIv7g1K15wjI1NxhCn2I17giK_4fEQN6QcrHG7MOPp0jO3f1kAgGKdY20bTHhHqwZmww4_QCNN5XyBpFJpexLcj0kQ1wmAwnJCmGd334OVgGNc2P-Sa_pkmC8q_9NqZKkH96WfURaL118iDNOpHlilGiApauT0NDhhVcL9-ZyLwoSMeZZTn9Wtgx1O5wJNgI3RFyHtThajKSpeU1r9EJ1YoMNxFB28_fL1JkHsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiWNIn9AjZs81MmjIvrcD9sGrtXBm50rUG-_C4IfxpIVO1uu23zeWLIfbq2TwWWoxFpD88t-B0iR3xT3bzSwqkzuU39DZiX1FUSgqJf1LiaSmAJs3nWTIwET0HAaKTGwcr5Dhx9BubL3uMBRq3ki6fE0rcRQIv7bS5sGzyrXtaEed-nC_n2unAA5d7ztsxu2MN7hUK98RyJ_uksgWzMcvYdgL2c5NgKWcvcUg4M6YUOHOZxZZl2QikX19JMY0kEJIFV0j9ciP797oFNzjHD84Pf1VrzbPP-tYlbB8aKzieOw-S5PS0dIsUcYgRvUYQUEC23L6qif0vILT-s7yJcDwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-dSvyc1iJ2LzpkL7uJUtBHLX1px9ZC3BNXYmQHzkMRLiEqPkqP8bxLMTHBUuUQ0nxusHb74303mrSr6aX_wV0KZiVJEz2tW45nosTCQHXiVm31isj71R6iUYEPnCHYkyUCG4E1xhp1Hf6gOU3U5ogogibPlgYutWYaGy8Mt61eD8lz4D-aCfsTvSQH6qLi5pEcYSWxjXSQXsqQmWB3db7dDzydLw1iVJkd1f7AeUd5YDkhA9xZ6dAHIUeKJ2EhMHqv2mAfycJO1nA8_MpitoWUxSThq08xoY121WpJReORLzYd3Zsov_iesymBYFq1PgjTelbWPlvuQtjF4lmnihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=R17oWJrmZwYTW-K3PMMxr9hHD2G2EK-sI_AofvBZiCHDrtUrH7RL0cDYH3XuT4h8zGAwMjRTcu4EbReoEenZoNtan7bnXS4BskLAIq8ts-ZKNkTc7vaMY2-ORs0PlNF96CiKszYi5riWeNeax3zx56-CxRKRFQTioZgvAF0InBwTe_piqjcBPb-XSuMOfybDMA6tJ9_DYlQZ7plUYca_xXWsB385m5Rk4ZJPdIpLnnSpCQSLNkeVotGDZGNytWgRruJntx8_qllM4UZYC_hhUMlB-XJHI5ANYyeLcv-lNrGAUpGO1U01w-RuhrGfET2weKNGCXCRg0aAt1mGQB2suRCYTYSf3pF190Z52Gj4BdaKt69EZRPRomzhwGrqp8mYF1yNfqWDD2lB4R6DqWKLkU9evDNMM8neKckeASbsbaY5HbTYK0ZX3Bspg15TaPkPDNlNfCWloHiRKxr5c0Plg8PiQHpuZ0V_poZHBgsw4Ikt8m2-DvbZNnLwEAcqefU56frXB9rOkLo6o4i5qOjSpmExSEiCu70L5k9vjAS0IWCySbw9bXT3O0rwCBXlgU8ns7j1HPi4s1aYcUMP03dz1Dq5teNVBYiw8tku-cbP1gZBkHoWeuBk5QwWRU-vQMY7KeBTO03_RyUCfnX5wIxn1eKJ8YywS1XilurMu76kX0k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=R17oWJrmZwYTW-K3PMMxr9hHD2G2EK-sI_AofvBZiCHDrtUrH7RL0cDYH3XuT4h8zGAwMjRTcu4EbReoEenZoNtan7bnXS4BskLAIq8ts-ZKNkTc7vaMY2-ORs0PlNF96CiKszYi5riWeNeax3zx56-CxRKRFQTioZgvAF0InBwTe_piqjcBPb-XSuMOfybDMA6tJ9_DYlQZ7plUYca_xXWsB385m5Rk4ZJPdIpLnnSpCQSLNkeVotGDZGNytWgRruJntx8_qllM4UZYC_hhUMlB-XJHI5ANYyeLcv-lNrGAUpGO1U01w-RuhrGfET2weKNGCXCRg0aAt1mGQB2suRCYTYSf3pF190Z52Gj4BdaKt69EZRPRomzhwGrqp8mYF1yNfqWDD2lB4R6DqWKLkU9evDNMM8neKckeASbsbaY5HbTYK0ZX3Bspg15TaPkPDNlNfCWloHiRKxr5c0Plg8PiQHpuZ0V_poZHBgsw4Ikt8m2-DvbZNnLwEAcqefU56frXB9rOkLo6o4i5qOjSpmExSEiCu70L5k9vjAS0IWCySbw9bXT3O0rwCBXlgU8ns7j1HPi4s1aYcUMP03dz1Dq5teNVBYiw8tku-cbP1gZBkHoWeuBk5QwWRU-vQMY7KeBTO03_RyUCfnX5wIxn1eKJ8YywS1XilurMu76kX0k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=rCCe21dPrWwUcq2_LJFYbzy9lU7CdSquWcXirjyZuv-GI0xq3KqoXdtsD0tc7jIgX7ewRInoWxD48Q-nEo4bs9oOj8KMsAF1LvZ6cY2xfVB97Lt-PJkJP_CR9xAf-YoH3EQ7NzYROTxyG0A7-fdsqNAQaxx4nts3FzI7ztW-4a1DFYRnVEEx8VV9OCSB_UE9v0dJvpKRc68EYcaiBay2AxMwL0daMZSjR9y6T4UrfAKuxDvQwDaKuX-umoP2pGLDsSinWS6y24W8OjMXd0td7MnBPj42HzCsbLrTlBakayvhrPYphE3qxDrKkgla40rMfsbTbdFMfoCBTo-Y1Hn0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=rCCe21dPrWwUcq2_LJFYbzy9lU7CdSquWcXirjyZuv-GI0xq3KqoXdtsD0tc7jIgX7ewRInoWxD48Q-nEo4bs9oOj8KMsAF1LvZ6cY2xfVB97Lt-PJkJP_CR9xAf-YoH3EQ7NzYROTxyG0A7-fdsqNAQaxx4nts3FzI7ztW-4a1DFYRnVEEx8VV9OCSB_UE9v0dJvpKRc68EYcaiBay2AxMwL0daMZSjR9y6T4UrfAKuxDvQwDaKuX-umoP2pGLDsSinWS6y24W8OjMXd0td7MnBPj42HzCsbLrTlBakayvhrPYphE3qxDrKkgla40rMfsbTbdFMfoCBTo-Y1Hn0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCqzBTksnx4HNfY8vjdAsnEo8nT9DbzmnTLwZ0XLFiVWT-sQq7pjVkYDpnzBtA2NwdjlsWDocEWXwqmhQIhGPX9z1aidnZZscq3mqJOvqY6-ReimfjST1tPRd5yVejIpPOecYEHfKm363wuQXcOS73CVkW9en_KOM9GfzSs6HUXvVxLcmLwT5DWl_oQF37B3NT_qyGGa0seN97yWwioj773QcEIkfcMmIrDjsbH6X8X9zPh8WSQIIhwsR2fRGX21XWrBwcpSahoqv2h5eN4lHTgYk5aaPNdgvrRMxXyvb1fONxvjbZGw1yz_orum5JCFu7f_g7_XEXf6IS_CC6DXr8C0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCqzBTksnx4HNfY8vjdAsnEo8nT9DbzmnTLwZ0XLFiVWT-sQq7pjVkYDpnzBtA2NwdjlsWDocEWXwqmhQIhGPX9z1aidnZZscq3mqJOvqY6-ReimfjST1tPRd5yVejIpPOecYEHfKm363wuQXcOS73CVkW9en_KOM9GfzSs6HUXvVxLcmLwT5DWl_oQF37B3NT_qyGGa0seN97yWwioj773QcEIkfcMmIrDjsbH6X8X9zPh8WSQIIhwsR2fRGX21XWrBwcpSahoqv2h5eN4lHTgYk5aaPNdgvrRMxXyvb1fONxvjbZGw1yz_orum5JCFu7f_g7_XEXf6IS_CC6DXr8C0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhFYSmDfa9zSrLV42IyVdWMDoGHSjr_QkC-zWK-PIaoqD1PQ8KLa4nRWEg0nRuE9sksg4si9FBVD6CBMICf22pskeA901svZairqqyx2n5unDq3r0z4esy-wT8vQ2f9Vi_AqRHY0AwfUCfozlz7IH1w3lhQ_AWASQKwnNKrIgbOpv-_u1hHhFmagQSgWfyXi-xK-0u-t57Zu0X9X4cYOd-MxzOmXrk1GatEyBzfbN5ULJaorc5zDhZu_pln4Dw1gs5leQ096-lMHpTnmbjOauUYAB2LKnD8GYoLPYQDFWqAm2495vz3Yp742CZbGJ5_T4R59FnsNQqm2WGVc-PV0Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBfZhjftncxRw0H1w0IN0qrYEFqVRkDDAtPL1Z3QwNz33s7tZagInhkUIjCTDAq2lJ9bn2hkIAOzESUYob7CzZfgBJV5FtPlidaBm72Dt1x3yw09bV3YNMDK2JBSgCyptdcqbiKaE7YEvQSVbnlIVtLwJOgNxCAMR4wYfcua4OMbiC18Gpa5pF8GDcHpIeAqwDJZ7KK0Npz5uuUDK4hm7D1CCOk3dF0H2uwoHO8t_JhENtdBK3WAC911Dc0VWsrnWTydlav9tM3XIqzlhweOX0lsSoiX3j11x3jpNc4nyIGQ6EhWE15T_9-kPE7uGe0N_n6eDrOpgKtRaKGl_HQ_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mj2kWVVpJ49ZMT1yg1lmfhRoQXml6IrDvIvdG_FZzsiNgmHW4mlw2ihiPVAGreiM89O0CUm7IpDv074Oxy4frVA-DZlJGbK_aGKU66v96H7K64shvwFus_RBOQJDNFKO2a-f2JKyIyRT0vW0YIQVvg_ea_VFHX0XEynSXaw6O7d7kgEoosehrXzAnRk2JKmQZ2WnVWua4RmrLO_wtFo7wd6r9MAVEqaYfxpl-KKWqebye_4xYHELuUj8kiIzlISdhSdPM1TQbv6QqTPVTCe4S2u05j4jKlk72jvJFTX5RRaOGmVRXxrZ0vsjHuQiUpDdX7nsd1qwzhFgDC8Rl7muDg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=g3EiuhXHO7a2kITaav981EoGFU2cXjhy7TRbnHkL4Pa4fCMiDN8VFeYGrj45nYL7JsI9U5PzdJCF0NsUM4CI2edxuOZ1SZmJh1EuJ-7uN1zm9P9LaRw2HDeNjUiJHK6uwa1c9FKbcd68nUB-R466yKmDMF4Uzwrx9nX-vWM-65Rg24DkSUcy0rE50KMzB7QhaZY4P9J2uzvNn9eSbpNFIHZ18Puf7JaNoc7tYx8KEWZ26XTh20q-5KGbcdF6UGvBs8E9c5FMXXHY_7_FBu7WN3wdEXiWuNhHrgkS6KI481EB_uoRHPh_fRZYmqCxtfGaKjUjO3vlWdOBa8ZN7snRdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=g3EiuhXHO7a2kITaav981EoGFU2cXjhy7TRbnHkL4Pa4fCMiDN8VFeYGrj45nYL7JsI9U5PzdJCF0NsUM4CI2edxuOZ1SZmJh1EuJ-7uN1zm9P9LaRw2HDeNjUiJHK6uwa1c9FKbcd68nUB-R466yKmDMF4Uzwrx9nX-vWM-65Rg24DkSUcy0rE50KMzB7QhaZY4P9J2uzvNn9eSbpNFIHZ18Puf7JaNoc7tYx8KEWZ26XTh20q-5KGbcdF6UGvBs8E9c5FMXXHY_7_FBu7WN3wdEXiWuNhHrgkS6KI481EB_uoRHPh_fRZYmqCxtfGaKjUjO3vlWdOBa8ZN7snRdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtAlBnhs8GhgTUQ0gXLEHe5uNOnwKwXxpoQ6mKVJtRxcqRRap6UhT7jvSNnxxaT2zWvv3ciBmTTIAgPPHK25QjACuvH_SELKqvTHn3DE20aMsVVEpAcD6EGwVFcXOlV309c552vnOMQ8CGA-9_YPqdcaXtPsD7sW4DP9N1ueuGA0zFw5jcKMzw1OdP4ZIpdWAPV2RRWoSdeNQshgzMBo3Dbv5G6FbxRlKljercFQgYW2xLPEbvGDNm9NjYzPB9Z8iBsp1LoRX2WoAXrWPfcXe93ddX351x6Tny-1EyOfww7GHc9SNvrzSVI78vUSNf25xpTbilWKBdRaR7xd2wbskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIbwYiqY6tZK8Pv50ceRBxnOerYPB76iasNx7YXLqJlZGReWQjHC7ZjeLQ5wpq4_1qIaE17tnbXOElQwqF-zQ_Y5eydc_RMFFgVBpUviDN0O_zZ-RrqbgxosvkeTk5SEuHGAi9OfnMPUKhPi-279Thr0gXczySz67EMo7Tw7lzhvukdnOatjwgnmAVpgrB6i4tkEcsEUKwX1H8qVy8bsOKcDKi1nfV0Ss--_Q0RHdIH8K1MWgCzP0uzuxh4yyx_o9dospINaN8h0N5WC-kQnLQ6KGY2i77wCDOGvJmJS3OTc3uJeO6lF8kbmyQMXJucu57UQfOAfn6IvtFhTOZZ1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIyvoypertDo_VkkVmEw1UrheYXYgYK6dhuBmRoL_osqe1ha-hB46yeu5Ki5KAVl1ODt-ogGkdTakc4oXXk4wb603Oa2ZJcvZxYUGIRAFnV5_gIKhhuuApDbfoJmSPa85LculcwMWmd1y87uDfl-9epZfQX8tNp02fJYst5koq0aBz6SSNnDvKlI-PN2v3Yg7Q-6SjGbDKaHwcKZ0Wqbu0SES2j4slI5GabJDQ1PjcurVtSOFCSA4YQAmJDT7aBggmxGJTUc62Zszrt9F9D6aqfJJFvLKh57QMNyQXAByDaD_veDACxkQ29h5be7JLSymzikHUpNdToclsxvUAi48w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqcu67k99fRX4w2B0PqHXih_UcX-ahjqEbAe9noy7-A8KmQg39USKatb93rKDdQFXoJhc_ZmfpFODCtmg_w9SBnj1MCmFX15jnh0mXIEPCt03SkiqnEceR4A2hL9bdRSdUXGiMZRyRBLuuy5_CrNXX1GEh_4ZIlYxCByjGidCLpLGGyVBPS_1Pl5CR37mhY1PhH_tk-KxldWnMjm-vWthlEmE6zNdCtCgZXSik1DfkthtDH-wATTPS6zXupumFrmd_O9Y5n3m92t9BvBnc3U8O9RqlIg1mYgM6dqirm-yNXEpYWRtzatRR9SqP1tDzHsmLp_zETwJeN50hHfBWiw1g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=luhSbo7_aCiHNrOdBw1TXKPGckEvTpRyhhKkCUkA6oSq2x37-uebRhPaxC4y7DHF2h1aZYWJQc2IC9xUxsbyZlen6CvCF8uisD00jeiFj7LOgA2YpK5k4nIxMONadOSE85EhMw9EJY2_S0t91326FMr14Div2yQ21mfOXL573i0DsrF0RyE08iDVXYPpYud-hwsBTca_KYR-VuwgGPQs_QNB4WB2WipXVsnPH608ohYhEVp2acKiFlIyMPGngUlaVZ3puQo7gR6p826koCvl1wIiuBJuXjJ08aHy1_yU6IFQi-aikwcWHFQbKEtnctU2ow9DH7rXt41fuHAEx4TUBoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=luhSbo7_aCiHNrOdBw1TXKPGckEvTpRyhhKkCUkA6oSq2x37-uebRhPaxC4y7DHF2h1aZYWJQc2IC9xUxsbyZlen6CvCF8uisD00jeiFj7LOgA2YpK5k4nIxMONadOSE85EhMw9EJY2_S0t91326FMr14Div2yQ21mfOXL573i0DsrF0RyE08iDVXYPpYud-hwsBTca_KYR-VuwgGPQs_QNB4WB2WipXVsnPH608ohYhEVp2acKiFlIyMPGngUlaVZ3puQo7gR6p826koCvl1wIiuBJuXjJ08aHy1_yU6IFQi-aikwcWHFQbKEtnctU2ow9DH7rXt41fuHAEx4TUBoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=bXOC1AOcl4Kc5yLoVWQfGXUHZPsQKfnjXu5HjakXp-9kxl6aZPDOXE_1uZLvWASyhzyuCvWY9aPtMwN00zHFOtthx2JMC_tH6_WtmD0Ib2fzdRyOxqc1_vKzwusnKVsR70xWtBdE5y9rBa6-r-hk66Sz8-RfM0jVxBz-bFlgv2ooUBfwTj-oRsyK-vG0qzwYB2ue06fuNjoLKqbMSiWfuOaINicLzv63PGBNM8YGK6O80iIFCK-n3b42ItkmfBh0PSVl3YHGDHuNV0cTkDAS1G-uLFn_y3gsD2w8SOmo44uelFhhR3DeVFX5vcaKClUFTi5PshurZdTrEra_GR6Y5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=bXOC1AOcl4Kc5yLoVWQfGXUHZPsQKfnjXu5HjakXp-9kxl6aZPDOXE_1uZLvWASyhzyuCvWY9aPtMwN00zHFOtthx2JMC_tH6_WtmD0Ib2fzdRyOxqc1_vKzwusnKVsR70xWtBdE5y9rBa6-r-hk66Sz8-RfM0jVxBz-bFlgv2ooUBfwTj-oRsyK-vG0qzwYB2ue06fuNjoLKqbMSiWfuOaINicLzv63PGBNM8YGK6O80iIFCK-n3b42ItkmfBh0PSVl3YHGDHuNV0cTkDAS1G-uLFn_y3gsD2w8SOmo44uelFhhR3DeVFX5vcaKClUFTi5PshurZdTrEra_GR6Y5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=rZYB4Vae7_Ro7Ck7OaVUV_gRMmKQ3eVGANltEVcS2dLPHBajYGCehFl176hgo13vH191lWZdOf_tggAQSyUDPsNFuxEEYI1YdK0AeG4imaQbuIKoPflFILoW0zT1hGlqg--9PEZWMRW3DFwS84NRz775vt9b-QHWecsg-UrI4KdqfWnsOXwDZCnSFeQHEuo2R8W4jfdgYI7S6wNU6JKi4hp4XEIvboPJ_pHlZLd8cbE6MqRBP4RDSs32Ci5CXXcUGBzmhx7jcLLR9JPFcm-yx8purrk52XqBtMJFwtx0Q5CnCLWssIACxdq3ygpWiCu6nBzm0SZ_04SmxRFWX9ZA5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=rZYB4Vae7_Ro7Ck7OaVUV_gRMmKQ3eVGANltEVcS2dLPHBajYGCehFl176hgo13vH191lWZdOf_tggAQSyUDPsNFuxEEYI1YdK0AeG4imaQbuIKoPflFILoW0zT1hGlqg--9PEZWMRW3DFwS84NRz775vt9b-QHWecsg-UrI4KdqfWnsOXwDZCnSFeQHEuo2R8W4jfdgYI7S6wNU6JKi4hp4XEIvboPJ_pHlZLd8cbE6MqRBP4RDSs32Ci5CXXcUGBzmhx7jcLLR9JPFcm-yx8purrk52XqBtMJFwtx0Q5CnCLWssIACxdq3ygpWiCu6nBzm0SZ_04SmxRFWX9ZA5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBV82pyIek8Xn2Jd4YW8XUK16WxwwTBZWqWdBe3_ID5q7MLpe8pkj3f3-DIqkppkwpLSOw01QUgoWVj5sE4SpXRcVrevsfBDTzYiGB6U0LP4KvVZool4JA87_2tHfcLZJA9pEF8E0Qssu7BsMC-H-Qnc3xI79-MdSuVvb06JDOXpS06oF3ArPxBvT4_sCWZ94gEHPR2VsVMMzAW79L_j2vBS6ZeZ-LRfRLytAhah5FGcQYh1mnoQb7JQiSKKb7HBWplrSGOrpZ7dHpTO0MybHxkwO_p3Gr0RRTf270NRM1dHAYDOtN4fliiVAIKOs70drJ4E0zESr3tTMuDy9PgTog.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=mskXGm8r2MVzybDkJnUI2Lxlv80HjzcCtG2A_5tLQwZuJsDU6QvLGn5xy2Dghs_i5zGogncxvJZWK3nMFnilrOiaRgOk9_j3L-nsOe1q7w3PjhG2gJToashb9LH2UU6kTmFrAqQKzdZbxuOoTCFJVb0B5EqfmpKO3O9J_8JvwH0OW-PoDR9H4RkADJZqQbaIFUF8VRQpWizILJygX1qCF6s1frK9-ub4sQxv40EX_V_LJLpYUUZY7KVGwrH0jrgZ7f3x86ggW-GCm8js4YANk9JO1byFZao3MiqbcKJQ_pCYiolVSA9vlRMckeC7rajckH6LGBrlNM_LVJCrTtviOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=mskXGm8r2MVzybDkJnUI2Lxlv80HjzcCtG2A_5tLQwZuJsDU6QvLGn5xy2Dghs_i5zGogncxvJZWK3nMFnilrOiaRgOk9_j3L-nsOe1q7w3PjhG2gJToashb9LH2UU6kTmFrAqQKzdZbxuOoTCFJVb0B5EqfmpKO3O9J_8JvwH0OW-PoDR9H4RkADJZqQbaIFUF8VRQpWizILJygX1qCF6s1frK9-ub4sQxv40EX_V_LJLpYUUZY7KVGwrH0jrgZ7f3x86ggW-GCm8js4YANk9JO1byFZao3MiqbcKJQ_pCYiolVSA9vlRMckeC7rajckH6LGBrlNM_LVJCrTtviOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=A9xbLRBZnE3jnnLy3iXPjieZhiXXQaljR0bGN_tf4vayLPphSs-BFIPTUEKuYmsKwMWgoSPoyI0zr1WTOS3RnAakaSbdOC4I5cQlxAc8CSe6X787q-tgl9vFC6WfOlyRAJUZVFNFLfFRxB6nFLbMMaBmjxgKcsyp5veR1YF7YllbM7-3HHMq27vjbIQfbmPVGHqQQ5CaagpThENaL7bUdzJ68SnJKzZVuCbHnXuonJxrMYPKy4NLrSOc0CExl_vZQT8p4TqAfI0uMNLgpOdqVjnLPWHXPYTrZEpGdSCe39zSiC1AEOsecXC5Wrzr5eKL0K8biJIa-ru_ee-fL_8Rmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=A9xbLRBZnE3jnnLy3iXPjieZhiXXQaljR0bGN_tf4vayLPphSs-BFIPTUEKuYmsKwMWgoSPoyI0zr1WTOS3RnAakaSbdOC4I5cQlxAc8CSe6X787q-tgl9vFC6WfOlyRAJUZVFNFLfFRxB6nFLbMMaBmjxgKcsyp5veR1YF7YllbM7-3HHMq27vjbIQfbmPVGHqQQ5CaagpThENaL7bUdzJ68SnJKzZVuCbHnXuonJxrMYPKy4NLrSOc0CExl_vZQT8p4TqAfI0uMNLgpOdqVjnLPWHXPYTrZEpGdSCe39zSiC1AEOsecXC5Wrzr5eKL0K8biJIa-ru_ee-fL_8Rmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=GhyIYp6kpYrOHE3ZE__2rXApTeIKuZikQMdvCCrmKX_950GBO3VdjSWwdAjMsqiw2sWFmWOXue61WWEFsVdNX2IzojxhDk8Z6qRg8a4CNJ_z7hSuBqjAFEp8GZkWWH2Ix2WFQ4ytBr-32NckaKAPst1JAWfIZTxDaO5LRXoCvfgDUfV44EXJr7pL9OdlKLt6QaR-x_Dg5esXfeFma19ulZwnMjxmlg04dlLvNn9UsXLSJ1-zii8NbVooVPU7t0COZAjYJW776sGB3BdPQNCcRxQMrm1kXHBgtUv3-BAgZdnBZqjLN4Cu4ggY5ULHe65O9wsfDH83WhHJEQR43JTJ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=GhyIYp6kpYrOHE3ZE__2rXApTeIKuZikQMdvCCrmKX_950GBO3VdjSWwdAjMsqiw2sWFmWOXue61WWEFsVdNX2IzojxhDk8Z6qRg8a4CNJ_z7hSuBqjAFEp8GZkWWH2Ix2WFQ4ytBr-32NckaKAPst1JAWfIZTxDaO5LRXoCvfgDUfV44EXJr7pL9OdlKLt6QaR-x_Dg5esXfeFma19ulZwnMjxmlg04dlLvNn9UsXLSJ1-zii8NbVooVPU7t0COZAjYJW776sGB3BdPQNCcRxQMrm1kXHBgtUv3-BAgZdnBZqjLN4Cu4ggY5ULHe65O9wsfDH83WhHJEQR43JTJ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=C66MQvGCgX3eW0mEJ33xHD2wtLGX6caih6pQQMULDLYrTBK8VOxscTbx1YpVyvH5oUsLTeWxXbalIofVOGUXGUXvo4RovmT9SocGfsDmRCWH117YW96d2-n2MCnjoAjIDOisrEEF_1Or45G1ye-7DOEjE1_RCivqp_V29-6WC8oux92dF4YqftM0ZNydKC0vpd3K6twNqgpqnrR0kzrPQYFGd27FB05RJCC7PwQGR5EjJaqDI3vN1eDy4vG7oKINu8r_gQ2E-hV7FmqDySQZsMn4mnvgcSqqvinvFjeVOEYMC6OVODDsn1nAFEj9uVNAe78E1elFvh1GSpP_xBseilYxmCbE4Rr4i8S6aOUUm659Ct7dYD4PRBEjYFDCIVemx2BzKPH76bm1eV0JK3c8DmtttWHMfO2WU9rVGn_5Mw8mk7waSDSutvOAkvUpBknUpPnCtpA39c7LZ63OdWWejFY3YEl8C8MMFnoExUwx1e_H5cndGr-6MlkHGmS1472t4mbY84a4lFXoguLIcCWiBLpbTCKqp2ugit5iQG1vBZ2sQVPRhatSJ7Trc7GI089SuAl6f4A5UPvI2xDZ8rjUKK0vTum9bxUB0BG3wgPgks40c9U0kkaJWhAUFvT1MhuSWVtkZn8daALValEzRX-OqQ-3IXSbBSXNK3HtaGjd7ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=C66MQvGCgX3eW0mEJ33xHD2wtLGX6caih6pQQMULDLYrTBK8VOxscTbx1YpVyvH5oUsLTeWxXbalIofVOGUXGUXvo4RovmT9SocGfsDmRCWH117YW96d2-n2MCnjoAjIDOisrEEF_1Or45G1ye-7DOEjE1_RCivqp_V29-6WC8oux92dF4YqftM0ZNydKC0vpd3K6twNqgpqnrR0kzrPQYFGd27FB05RJCC7PwQGR5EjJaqDI3vN1eDy4vG7oKINu8r_gQ2E-hV7FmqDySQZsMn4mnvgcSqqvinvFjeVOEYMC6OVODDsn1nAFEj9uVNAe78E1elFvh1GSpP_xBseilYxmCbE4Rr4i8S6aOUUm659Ct7dYD4PRBEjYFDCIVemx2BzKPH76bm1eV0JK3c8DmtttWHMfO2WU9rVGn_5Mw8mk7waSDSutvOAkvUpBknUpPnCtpA39c7LZ63OdWWejFY3YEl8C8MMFnoExUwx1e_H5cndGr-6MlkHGmS1472t4mbY84a4lFXoguLIcCWiBLpbTCKqp2ugit5iQG1vBZ2sQVPRhatSJ7Trc7GI089SuAl6f4A5UPvI2xDZ8rjUKK0vTum9bxUB0BG3wgPgks40c9U0kkaJWhAUFvT1MhuSWVtkZn8daALValEzRX-OqQ-3IXSbBSXNK3HtaGjd7ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Jf7mZkQQsSKR-wFbu2b0_K79NpsVpqgUovG6DpDfpo28oa2BB4ANN-xKF2Q46iYcRT0G3NxQQvSy9LfhfaJD3OhLG_6xSsESC18bcI98rAEwBb75L24f2aaUg9ubdNWzHKyaf_uCmc4hUMpDEdWiTv78acNEVkwTsLVRTftuBHms6URhaUXdHfk8lp9ND7xUF2cIG6dBM7mXg7pENhQH1OJl9jwwGvjnOe65uVRkqPNjG24k847DZ3SVJr9DWIBFO3nP_kvUJnumVL3ArTtiF5F8UF9jlCfkov8CJ_KI4cDF2kTYJItYIU4Mk3V8Vn9c5QCbQTzz9KI_b2dGsjtR4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Jf7mZkQQsSKR-wFbu2b0_K79NpsVpqgUovG6DpDfpo28oa2BB4ANN-xKF2Q46iYcRT0G3NxQQvSy9LfhfaJD3OhLG_6xSsESC18bcI98rAEwBb75L24f2aaUg9ubdNWzHKyaf_uCmc4hUMpDEdWiTv78acNEVkwTsLVRTftuBHms6URhaUXdHfk8lp9ND7xUF2cIG6dBM7mXg7pENhQH1OJl9jwwGvjnOe65uVRkqPNjG24k847DZ3SVJr9DWIBFO3nP_kvUJnumVL3ArTtiF5F8UF9jlCfkov8CJ_KI4cDF2kTYJItYIU4Mk3V8Vn9c5QCbQTzz9KI_b2dGsjtR4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=CbUTxd0yMYjqvOR319WunoIpojAJRVgc9i_GtTga9qix4fa0Q74utxXJzT41VUvA5fypBDNn1kUtfeoXk56AMZuJnZTnXuiaN0i-6bvhshV453AFyTI-3eO3ITjIw49QLG0a4EphY0OiTi-hG2IzFzw_y_j6TEBwczKVBVPQcWhhkpEfL2aVLLQOuRUs0mBuKFEjs9ZYG3PQgnI_dI6SN36uW1pRy6JaYF-9PaeT75UyN-81Wqs4RDwm3Lme60maTie_AR9KrUhsfemuT5ZsQZIw7xkmlNpkIn84XWoG8UaHN8lJU-MUm-jiTbNKMU_SW_0z-WIUUB5fZ-x647V9fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=CbUTxd0yMYjqvOR319WunoIpojAJRVgc9i_GtTga9qix4fa0Q74utxXJzT41VUvA5fypBDNn1kUtfeoXk56AMZuJnZTnXuiaN0i-6bvhshV453AFyTI-3eO3ITjIw49QLG0a4EphY0OiTi-hG2IzFzw_y_j6TEBwczKVBVPQcWhhkpEfL2aVLLQOuRUs0mBuKFEjs9ZYG3PQgnI_dI6SN36uW1pRy6JaYF-9PaeT75UyN-81Wqs4RDwm3Lme60maTie_AR9KrUhsfemuT5ZsQZIw7xkmlNpkIn84XWoG8UaHN8lJU-MUm-jiTbNKMU_SW_0z-WIUUB5fZ-x647V9fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N81UZmRvCTn47vdCiQ7r56OES1TtB7_K5yBT3dowX60V8Jclk0t1ohlCCfNMPkSRMSsrTfSkCWS--tjPeNCFsejK-XmGAZ8TgUkKL1QkBoImDZ7K0071YT7nkXlTXsSQg6UaMEFWD0_dK0_y_y7TanYSEVDuCAke7GxLwanOix1pWupm1LBhulUWc2JeX8oYoWgFOixPFmYgnOQnrKX_-t7-Gmu0JgHj13ct5DDNzScWiU0bPYMslQxH8cfdtRMdhuEvFGd7YJ2jiO4ZKacROTWy578M-TMOnIIjx5_lP6IoCQeTgWq8MieO89O4Yp0ldS9VAIXGXJwV_eYnP15-Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5NxHpHXFbRv-f6h0ay193WGI1x4gL2qqPDXhbrULu6iYozf6oirYBsuJ8wx52lJXG_MEwsq5ExaP1G9Rb-BbUIPgfPvJ-w2LbGGDlTE_jk-GNmk8u_E4uWgReJeqzkutqk1qgwLLbwJntnklbUjY0Ob8fOL35nV-UZLOtW4YxBb2Ad-7j5S5aagjZzui9rR_oATDXVKbCeWIO1t73AG3Gw_Te1d85P_EHmJT9NS6CnVb0USb-dNKhTNn47auqUBzPdTmd2pPaRbAToxYQkyohtSDlRBVMCMpYxdebzx1bUJZNdZ4Y7TgGMoGJsiaTi3nNumOrXvl-8GFikR96IR6w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=JIjWUo-vYcuvDp536N1itbJ_FZi5ChllpECdFb-A88BkZ9FXcfKFr-xwTY30jxgl5hlcp9imrDbUKGRu7Civzpl3l-_5ArDK4rsFpHAXJb1MoAatmjzvCEqfqfaaIQep-Se5I4QL-4B16Fh7Q2JU3DUT2e72IBkMN6ch6kcjEdqkEFSyMqXDuANpMcqNFmSxuCWReJWa9kNz9ynqrRah0gkR3qDGblsfu2MUMuvzFFO-lzwOSWJcZpf2S9wf2NcvGPgC6p04awhiPOnM0v0xgz423iISpWCz8VQJt8hYLar4TnZQDtCE5RuRkdLFac0m9nYpI3FAdkvgPl2WZGNeIjz8TNS68SKWkOHZty13fmmRJH4f61J2T0RIQw6rhPUdYKWB3qQLNxPKxp6bVqxC-zmFR0qvS8FtM53_ufHAFGIZElNk0hDwvj3gtuAV4JXZ3-rv7xjh58-mIdYyWdBhCqxpVMTBkHoLvr1mbLxcc_18YMEzQ2ofYa_sdtQM_ubdr8XnFDEDaGGL8a0zn8mNaRHPgPrgHV1neyx6G-3AHskZvRb0RQcaP37vQNTQ2KNyfTMQxbP8ppF-WBoHLhf_o3QbFFXEUyhFdv1gFeCfpu-NsdvMhcyMUxa9huN2ospQYQg35vPHS4yPsla6aF-kil3UorVzgxIdW3lksR0N_8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=JIjWUo-vYcuvDp536N1itbJ_FZi5ChllpECdFb-A88BkZ9FXcfKFr-xwTY30jxgl5hlcp9imrDbUKGRu7Civzpl3l-_5ArDK4rsFpHAXJb1MoAatmjzvCEqfqfaaIQep-Se5I4QL-4B16Fh7Q2JU3DUT2e72IBkMN6ch6kcjEdqkEFSyMqXDuANpMcqNFmSxuCWReJWa9kNz9ynqrRah0gkR3qDGblsfu2MUMuvzFFO-lzwOSWJcZpf2S9wf2NcvGPgC6p04awhiPOnM0v0xgz423iISpWCz8VQJt8hYLar4TnZQDtCE5RuRkdLFac0m9nYpI3FAdkvgPl2WZGNeIjz8TNS68SKWkOHZty13fmmRJH4f61J2T0RIQw6rhPUdYKWB3qQLNxPKxp6bVqxC-zmFR0qvS8FtM53_ufHAFGIZElNk0hDwvj3gtuAV4JXZ3-rv7xjh58-mIdYyWdBhCqxpVMTBkHoLvr1mbLxcc_18YMEzQ2ofYa_sdtQM_ubdr8XnFDEDaGGL8a0zn8mNaRHPgPrgHV1neyx6G-3AHskZvRb0RQcaP37vQNTQ2KNyfTMQxbP8ppF-WBoHLhf_o3QbFFXEUyhFdv1gFeCfpu-NsdvMhcyMUxa9huN2ospQYQg35vPHS4yPsla6aF-kil3UorVzgxIdW3lksR0N_8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INP0orNqQrtMhANKe3qrTfmsA_5MayAt2gitubjXpZ3T0d1jS_96RqCOUXzP5rBoFp-gjuWsUkT45FG6jCxF0jY39-gjgAmQxaDSCMohHleBVL4j14U1C7tXM88De6hNdyoieWFUUt_0f9fJL4jmGypshQy8eK_FPuHgU6h407QwJUSiWRVOHMu9NaBG1g6JKydXQT0O6lV5XWf7TnhT92P-QnVJJ8Mle-Oey1oQky_c80JydhTTlfYiyJeVBwSYZAh56s58j12CHILn2hplYSxytbgADF--zsABFHADj_Im9ICVPRCteKvD_3mEm9-OzbcMfbar_VpqM2x368z1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iv3UB_cFLiJC7Q04bfJRaR7_milMRBXnurvxbRBMIGkqoKCX2zwZXUsroUnsI2KD7sx_ptlZTXHyj04E_f_w-SjnHLrvWyxMq-6N5KUuQGhghuS8b2HQWA06BS5og1u4i_gq3RzESTHeAXbFKy9_ilkeOns2Wtu_H6en8pQyQGSbiCzcP3tEnNdme1-DgWj9_MHHy6acl0Y62Iqmx2yLBXv7GKSzxvg9C1KhZ3WB2Y7AjQW1Ef18uhRb6eOjnJ8A3nzqPxvuVfDET4oQtbkCeivi9-lRhjU7G27P0140X-EhBNheCKrF2CgOhkIwsY4e52vyzhfc8QWVSzgbhWIdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raj_HP-eCCyPwCsSGVTgx-UlNeDfrTz5gNoK01XOaOzRNyvpp89Yd2BrTDaW2XWAXJpawox3jOTEMtLXaUzrVqy1BjDSDhxSGvvzCKRdBqIZozotearZsfJElMH68Mqj582KXSjYoXJipiZPdJyd6qYx7Yl9fSEwQsrY5VV4SHHasHx-uYazbmTvJycv6-p0DVyhLFriZfLRkKEZ1_gdK1OV-lBwPXm0MtJuERwVGmsh36uOjMbIobnyLUxNv8jFFFxPIYesMZWxuXU1WdOVOeDwyT-KvleB6RCJiiMORjxNHxC75oduLb9m9kBfICZbr3fsTtI7KjC6JWmrEnw8Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2BEMV4sM2P2dYeu9kZwWWEpf0TpJ2D2i4vGjJMk3Yjwx-T6CqcwNq0VyEOaV98Sq1GNeCOxQXIgUy2AqqjvLouY_RJCpJihrM6rUDukaKWtKyMZp6Svfn3AsiTlYnrkxsGLO8EycXA-E5dNlQJC8iGN4iJ_UYqbkgqXCSveakmjH8KGeo-jNTEJtWAUboBtclyzGCv7hwUWgKYX0Q9H2cklla_iwHeJwGsj2rODtQdp8eyFMBEzyMsyhfX9_M1wjbl2bJBZLVyOqhOjUUs9ecCFf1aqOXgFlcY-ufQbOFLSAc3GGe2y3_nKj_FGOuQHVuXZqzMzZDdaXlfsVZ7VOw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=pTz3n92I-MRXf476hUWjFOZfyjWpwyTAW_iZd5PyC9rhYXDp5lbpM8VGW0D6x1miOe1vY6AhZS0Bw_iB9___8r-g0A_EOsFyU0g81T7qjb6POFJa_cD2AHtTtcpKjMn7uQgFhFvmq4rTsObXxRE5f9U3V-lc1YRrmUnkWqJ_j5k2gRWrjdykmayJBcgeAcO7wQ-UvOe_fVBcESXIUux6f7Jm3ZUKlD6BLQHica2BrT7v3KxkBlQQSPWWLc_CYrcYLv6mCfBlM0OErbEyDJl12vFAAwvFMNBwle-YhYFKKpI5FwD4R16x7y2LsoNO7y-zgBGhXA3uulFHv2h8gMQ61Bkr6CU9trYVkaCR1YuFIOUrir4-YDK_0qijmoJtEKavmkM9vWU199XlMOV21VW5yRFbZGCQQum7WRyTSyl-Yc42DSHs5b1kxiZhvLxnwSYF8ywelHagBI7pQRh62ztfjOt5xmG610LEDDL1iK-EJ9ekkNjHuNu2IAGLFoUfGzeTu3YkYYDgsOWlgeYpSWSGeKMyKn0athALppA5Niu0qHoj9iilIjFiToG8cmbELzLCF0GUCuw9fKFBUzzcI-Gcl3x-Y5VPhijHa370iDo9US5bbxMiAXeQUFq6NAZi4cFg1Qh-F6_pRk1__4d_Ucx9g2RlZZbSH1znZnX5J9BfbXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=pTz3n92I-MRXf476hUWjFOZfyjWpwyTAW_iZd5PyC9rhYXDp5lbpM8VGW0D6x1miOe1vY6AhZS0Bw_iB9___8r-g0A_EOsFyU0g81T7qjb6POFJa_cD2AHtTtcpKjMn7uQgFhFvmq4rTsObXxRE5f9U3V-lc1YRrmUnkWqJ_j5k2gRWrjdykmayJBcgeAcO7wQ-UvOe_fVBcESXIUux6f7Jm3ZUKlD6BLQHica2BrT7v3KxkBlQQSPWWLc_CYrcYLv6mCfBlM0OErbEyDJl12vFAAwvFMNBwle-YhYFKKpI5FwD4R16x7y2LsoNO7y-zgBGhXA3uulFHv2h8gMQ61Bkr6CU9trYVkaCR1YuFIOUrir4-YDK_0qijmoJtEKavmkM9vWU199XlMOV21VW5yRFbZGCQQum7WRyTSyl-Yc42DSHs5b1kxiZhvLxnwSYF8ywelHagBI7pQRh62ztfjOt5xmG610LEDDL1iK-EJ9ekkNjHuNu2IAGLFoUfGzeTu3YkYYDgsOWlgeYpSWSGeKMyKn0athALppA5Niu0qHoj9iilIjFiToG8cmbELzLCF0GUCuw9fKFBUzzcI-Gcl3x-Y5VPhijHa370iDo9US5bbxMiAXeQUFq6NAZi4cFg1Qh-F6_pRk1__4d_Ucx9g2RlZZbSH1znZnX5J9BfbXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Oav3a52oNsgEOOe8dafLkzUWIdXEL37aDLaQ2KHxFQaoL_zhYckgxXBQX-9qya6yxSDUKah-sA6utDnViDHJMJSvYvv8OFc639zdVpoq9j4D7T8Dw_Db7bh67T3lBHMaNbnVtEvU1Z1l-q2P5pm3jnqvdEX7R7irAOt7mnOgqcDoyIpMF3rpb4pRReIQCqYhyXeczOhM4Dwh_oW-Za4nd2Zr1Y7J-moYLXLvQVYlhQlvtyUG-aeJVu7L-A6UAeLpepRg18SqINIkq7zqbrAUI5SJeoRM8USzJ6cpgyGVfkFBoKklLF5RUYD_gAV2xgUPoqRiyOHs0StKc9wrvE_6-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Oav3a52oNsgEOOe8dafLkzUWIdXEL37aDLaQ2KHxFQaoL_zhYckgxXBQX-9qya6yxSDUKah-sA6utDnViDHJMJSvYvv8OFc639zdVpoq9j4D7T8Dw_Db7bh67T3lBHMaNbnVtEvU1Z1l-q2P5pm3jnqvdEX7R7irAOt7mnOgqcDoyIpMF3rpb4pRReIQCqYhyXeczOhM4Dwh_oW-Za4nd2Zr1Y7J-moYLXLvQVYlhQlvtyUG-aeJVu7L-A6UAeLpepRg18SqINIkq7zqbrAUI5SJeoRM8USzJ6cpgyGVfkFBoKklLF5RUYD_gAV2xgUPoqRiyOHs0StKc9wrvE_6-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIGYc9x9j3Ow7fAvYURAZwFupcgjdm_qiQCmIilXxv6PDiKFRT8OpDBDi0LFlM3weDmGLcNEtnVDTe_eeZpwh2JV7iVxw8NUZnYcc6TNnn_FKtp7qsMucepIFSqzRwq65ZDHJyLJhS6_29Q5JzWCsujW3mSQd_Zou0YJ0NfrAVKVwsxnf4TaRTO7jlrHfW7aE81Wf-gc4qZHmgkUzDlSk4danrnBIxEVbdqEMJNjVp6b8qJXNKBu0faW-GAM_QDJMdQo91_6ziG4x1yTA9dZHGsyaNzWRrYSzQ5mzOVaKrNmU7y7CNwrR8eXzgOAtB-fvAr3reyzfOrx5Nion3GGYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntrMIbotkme3MCLO5Lm1tk7GVsWSgcLyXOr3QNFnEWoYdj_V79B4UWkeKXnkL4w7D0nbJfR31terwmNqXywn0cIW2SmP76eNK4490gZM2KA-BLsYIdqzQ5Dy5gGYYqxi86xsE-JYiIyjV3ACVZYwil8gKAbVJEFpjWFOl7gdrwrEuPQseVQur06eULzokA8-SVTwhvfbFkJ0hBH6kYgpNNMjBXGmmTlhV1XrynOqmrZOPskR9uBJT6FDyf0_Whp7vvJkibwHZuE-EcFrOraUceApxCa1z3trZX4kNuSst9jkfTnZg6Snq-4D-MiRde_5V3L_Bp1HkyRuIzUG3mXVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUpYWillKMiBpl5De42yLaiodLHas0skYfjJuJucnVpkaWZQaRG5GOqwSRr66IVQVo9cx3ZR2NnCBfnYJu30QEkXAvkQbiS105K6206KvopkDpg0rl-zeS2mm09S6FIF2-C4RP3LY6EA8DmCFRSR3bsmci_VZFi7n7ThXTcGsuaqor1qtw1M4vnS7-uj5iLjlcgkIPD-P58RC5m28BnYWPdP-4rYlN0jCIvTuIedwj92Ln9viBGnZHPmaJ4jjRHzzbwBceSyCGEBaDIcJXaxYY9XeIprBmPKUIOjRCH02co8Q1ZWBjJwTOxgEr1j-8EZA37J0qxfdWtiiD8BkpaY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvE0NMAH4o6o_8uLMQnHIm9qe5E0vgPPA-GFNX6Wt_88FigIt40RfWRz5D4l_J2e9UDoqoXK2Klb3-_dLe6dG8DlOgVyxeQkf4IFFoEHkSfPP0PNr7TKPBRXe-ziTydGbpVP6v3ZSWfiGBk7KaoLIzKHNyGF4aZM78n9AL73a0JSdAOh1fOWyCLo8J0KHBBUpIOy1lPWbwh3XMMhWvkb6fTumqhOm-E7tVcyStE585npo7V1VL7w1lFNQGWXaYmS_Jh5JGgRdikJaynES5khuUvKZXZV2CeXTmixg6hckWhAlj_wUSRy-2YvMtCgriWZHJK28nlLPAV8EgnvicNSKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd45qUUz4_qHLpp90b3N8wWsz_y-hljVcdtMrAozwOEZ-J5_Dr8vOSAIvo-AKzClRIqzfUPO9SpdByozENa0dZW7dpjhBqUDCp4uZeKkOjp3Ah8ck6YM8M8MlQKkKVIihAPj52QD7I4MNkraIavUFsmajyvDZ0SmT6VFccl_Ttt66qY4u3U181KjG9nCtxy5MtV5n_m8yDbhpzeZy2Ln5hswa5cmdAB74qpLguVXTwQX3DY8Yx_PK5vrNevuXAyU3VIyQ2aPtuOY5FTxO81C-nYfDUf85IjBWPetAV6-u5ybbmaLKdnHJbqSV6_mmy1MYqg2SfmNAuSWwHBgoFtLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_IwfT-wBvQ3kEx8bfxXgtMo36JG9K9l2mb36qLV5ecdtzd57UX7-umEwBxWJxMBGi8hb6PKIGRvWvbBZdGVFEUEilZuFDa1danl17XArH-5nWxT8kf2dYs8CwYVAro12YxbmxU0F-knOEC9gJmBjfwmrALMQJ5LOd604bVcJIRFFuFTiWeZndeQ-JfqvDZEE2SsJypQhU4ZBoND8kY6kC1QKv7QmD1z--3SIRLslImkFRDfGjpoXqHvM3cpayalvDBlm9OZ5lCD7xAWr--OIL1CqvkCeQli0nP4bu7OeLR9GhygKQtM7TQhCt_LJbtcwhI6nHg0xySovCQfQD6Pjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPRk-nK24iiJVbhS--z9gHTXDlQ9wF0QAegg0EFhPS3MlSsY2k9jwDiGyzlEKDAAu6p3Kcj8YQ3LVjM6o1WS4nbZpuL0rSUE3zSsZHa0_6Ro3bXw2t-4A8zvm1X16BMNwl5NBkUUVKTboSHadO9Q_NpFxzGkcdWyhlGjOYWWdYwZI5RITDvw6Q2kmAmd9FcFlIMNuWNGbVYm81yPVnaHDBKSkVTGSoq3EpAOl6YwBaKQcQi_8M-1N-vJn8Kl0O6qUsgA00q94G-UaL5YM0NAm9DPpo_pfofSOr-eDJ3XF-bHtsCvREXMnb7l90FbTNxSaPhCXUjzCN71riBUguHg7Q.jpg" alt="photo" loading="lazy"/></div>
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
