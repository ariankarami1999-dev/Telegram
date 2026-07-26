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
<img src="https://cdn1.telesco.pe/file/oADwrzzJIygYZdVaeAQqtqBvBxzXMgkSd8mOCtRnOpStjDCDH6ukLfvdZ-YShHHLmz8-6y4FrwG1ZEMEeus3jQp1GP1FKgiC1QwoZIJSouZILlv3xLaONV7GFZLQBHb3Wn-ynClsbGgVr-4Phyn73XRlIXDYCQDwmUtCmPnGKTrZbxtUahIbDEE2PrWq6yxDVuKoT3isB8h1wy-BfQ2bE6hdqkzOXrv9BUW6JPwNT2EH-zG7B30BhFamTu8NDP4NuAjofSlVUQCj1zxtGFxQXAW1n670K__wpt2--0gHLrhIGXkMh4Ss5AeEGk7o3x0-oTM9FoHQI0c4KBsTGLnOMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 157K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 08:22:00</div>
<hr>

<div class="tg-post" id="msg-4685">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rpIODUO9TU5yB9FbBD2DnMfff0IJHCW1pOr8Qtg8g13BdueNF1M2IdS00yQ_pefRZ8I1jTbr0MQNSf6_lKd6xiiC94vQUphyzMxYTX7ieRAVe8lc699Tr2jkZYJweWZ_vLpwPBrJF9dl_gZSt_yoj-vW6KsHcdNX2FRhw78Qav2bSd669g1tqbKiD0aX9tgIEPLfZKhvOTM4MrzZLlKvgE0ldY_hln-slgPsJYGoCM5LEVyiXQRBboRxEoe2ccCFErI9Gnep7SE-ukx-V7phWAFm5f5tIiZmWKgGEUGKPb5mzXFZcQ9Mmxk2GxjSDiduYrVr439NeOD2u-BjtBvwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان اگر به ارور workspace has been restricted خوردین، باید یه ایمیل جدید بسازین، با ایمیلتون اول اکانت گیتهاب بسازید، و با اون اکانت گیتهاب توی railway ثبت نام کنید تا بهتون گیر نده و فکر نکنه اسپم هستید. خودم الان یه بار با continue with email ساختم دقیقا به همین ارور خوردم بلافاصله بعد از ساخت 9router، ولی درجا یه atomicmail تازه ساختم و باهاش یه اکانت گیتهاب ساختم و باهاش لاگین کردم، سریع ساخت 9router رو و گیر نداد</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/MatinSenPaii/4685" target="_blank">📅 05:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4684">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عبارت VPS هم زیاد درست نیست. صرفا جهت شیوا بودن کاری که قراره انجام بدیم بیان شده
👍</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/MatinSenPaii/4684" target="_blank">📅 04:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4683">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-railway.txt</div>
  <div class="tg-doc-extra">168 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک‌های استفاده شده در ویدئوی بالا</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/MatinSenPaii/4683" target="_blank">📅 04:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4682">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bc8cONdBafWhT6syg6iMkZNuKsx5dEFFqjTORoYt1vj075fAUolzCk8DLuXLUgpR-Nz56Rzzs1Dxa_7qhi2zaZlLMok5kHEQohebjplubTxeQA2uGFtLgWZ8caj8mCez_XYsSb1edqA60oShI13t3-Gr7FEQvdQMGVo2bcOSv1cgOlnbipdoDFdfoZo5_e_SMdcH8xCXqdfMSns_-VrT1jn-kvfS9KeoKxYkRT06w72YPH4UKjO20GryK09ZNEgia9UqrtuJ2k0Q6EjYUmGxtF-pPhQfaJsAI5xBygee3_zHkNLmHk9t8waw2_bs1_-DuCT2sNid4wgybBcH8nTSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
هرمس رو با گوشی موبایل روی VPS رایگان و تلگرام اجرا کن! + آموزش بکاپ کامل از Hermes
⚡️
دستورات نصب استفاده شده در این ویدئو:
https://t.me/MatinSenPaii/4683
⭐️
توی این ویدئو:
1- بهتون یاد میدم چه شکلی با گوشی آیفون/اندروید/لپ‌تاپ، هم Hermes و هم 9Router رو به رایگان روی سرورهای Railway بالا بیارید.
2- وصلش می‌کنیم به تلگرام و از مدل Mimo رایگان روی OpenCode استفاده می‌کنیم و API 9Router رو ست می‌کنیم.
3- به طور کامل بهتون یاد میدم که چه شکلی می‌تونید از اکانت گیتهابتون استفاده کنید تا Hermes رو بهش وصل کنید و به راحتی، هر چند ساعت یک بار از تمام داده‌هاش برای شما بکاپ بگیره.
4- به علاوه روش ایرانیزه شده‌ی استفاده نامحدود از کردیت رایگان 5 دلاری Railway
😂
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api و سرور رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/MatinSenPaii/4682" target="_blank">📅 04:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4681">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فکر کنم من تنها کسی باشم که از اینکه مردم از کانالش لفت میدن خوشحال باشه
😂
به خدا حس میکنم هرکسی لفت میده، جمع اینجا خلوص بیشتری پیدا میکنه و اصلا کیف میکنم
شبیه عصاره‌گیریه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/MatinSenPaii/4681" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4680">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">منم دارم یک چیزی برای بچه‌های کانال آماده میکنم که با گوشیشون هر جا که میرن، رایگان، بدون فشار اومدن به منابع گوشی و روی هر گوشی‌ای(آیفون/اندروید/...) بتونن با بکاپ گیتهاب، هرمسشونو راه بندازن و از تلگرام باهاش چت کنن 24/7 خیلی باحال میشه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/MatinSenPaii/4680" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4679">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hOIk8i-EIVWVvsDBF_BTdWjGbVArL-UVSXa8_RXJpCHmOpklMaargImIU7tvTCMxdM5UDZBGdBDp_mdt9nBKW-HneFFsa14ZTdcuGMEYLgLxJpbKEucFK9wNxYzfXcoFfAq0epiCQRHrzznYpftwExkxX-Omj72JPSyG3kcGAXGFKZfI8scS7Ln9rX_LcuBrTxTLdZdWOvpKqS2FXBFV9X-SYr1SQFzqObbExvKqdmLiSQz3kNGtuor4c72BCiYTsA6Y48L0lkvlo279bip5nMgEjeK_S1ARKKGwphYX1oZeZrs7d41xyxV7HIfw-eziYWXhLXJOxgM6bg6PxB0Zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم دارم یک چیزی برای بچه‌های کانال آماده میکنم
که با گوشیشون هر جا که میرن، رایگان، بدون فشار اومدن به منابع گوشی و روی هر گوشی‌ای(آیفون/اندروید/...) بتونن با بکاپ گیتهاب، هرمسشونو راه بندازن
و از تلگرام باهاش چت کنن 24/7
خیلی باحال میشه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/MatinSenPaii/4679" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4678">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برو برو
🥰
موفق باشی بعدا میتونی معرفیش کنی خودت و بگی چطوری توی تحقیقاتت کمکت کرد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/MatinSenPaii/4678" target="_blank">📅 01:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4677">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خجالت کشیدم، میرم پروژه رو راه میندازم.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/MatinSenPaii/4677" target="_blank">📅 01:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4676">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تینا شاگرد نمونه‌ی منه و به ترسش غلبه کرد و هرمس رو راه انداخت
❤️
پرسید، تلاش کرد، به ارور خورد، و آخر سر تونست با اینکه تجربه‌ی چندانی از کار با کامپیوتر هم نداشت</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/MatinSenPaii/4676" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4675">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">باعث خوشحالی منه</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/MatinSenPaii/4675" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4674">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">من به شما افتخار میکنم.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/MatinSenPaii/4674" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4673">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در مورد این، یه وقتایی به نظرم بهتره آدم کمی پروژه‌های پیشرفته‌تر ببینه که هم بدونه دانشش در چه حدیه، هم یه دیوار جلوی خودش ببینه. نه برای اینکه بترسه، بلکه برای اینکه بدونه دیواری هست که میتونه ازش بالا بره! و انگیزه‌اش بشه. من خیلی از مطالبی که میفرستم اینجا…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/MatinSenPaii/4673" target="_blank">📅 00:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4672">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/MatinSenPaii/4672" target="_blank">📅 00:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4671">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">موافقم و روش تدریست رو خیلی دوست دارم. اما خب، شاید برای کسی مثل من که کلا هیچی از دنیای کدزنی و چیزهایی که آموزش میدی نمیدونم کمی ترسناک باشه این موضوع  این‌ روشی که بهش اشاره کردی رو توی کلاس هم پیش گرفتی و اونجا به من هم حس اینو داد که خب وقتی متین نمیگه…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/MatinSenPaii/4671" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4670">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خود هرمس و راه‌اندازیش مثلا شاید یه دیوار بوده برای خیلی‌ها.
من و بقیه‌ی بچه‌ها توی توییتر و تلگرام و اینور اونور، طبیعتا تجربه‌ی کار با کامپیوترمون بیشتر بود، زودتر راه انداختیم.
انقدر نشستیم بالای دیوار و از منظره تعریف کردیم، که چندین نفر دیگه هم ترغیب شدن و تلاش کردن بیان و بهش غلبه کردن.
چون واقعا کامپیوتر، و همچین مفاهیمی که شاید برای یه سری از دوستان ساده به نظر برسه، برای عده‌ی زیادی اولش ترسناکه. و باعث میشه فکر کنن خب، اونا که تونستن از پسش بر بیان باهوشن یا هر چیزی، و من نمیتونم.
که اصلا درست نیست.
کامپیوتر و این مطالبی که اینجا قرار میگیره
همه‌اش مهارته.
و هر کسی با تلاش و پشتکار، بدون استعداد، میتونه یه مهارت رو یاد بگیره.
شاید یکی زودتر یاد بگیره، سریعتر متوجه بشه، ولی در نهایت همه با تلاش می‌تونن بهش برسن</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/MatinSenPaii/4670" target="_blank">📅 00:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4669">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اما تفاوتی که هست اینه که تمرین‌هایی که توی کلاس میدی در راستای چیزیه که بهم قدم به قدم یاد دادی اما مثلا اون پستی که برام فرستادی برام آشنا نبود اصلا</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/MatinSenPaii/4669" target="_blank">📅 00:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4668">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">موافقم و روش تدریست رو خیلی دوست دارم.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/MatinSenPaii/4668" target="_blank">📅 00:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4667">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">به نظرم این شکلی یادگیری خیلی مؤثرتره
😂
موافق نیستی؟ آدم اگه 5 بار هم قدم به قدم جلو بره با ویدئو یا آموزش یه نفر دیگه، خودش اگه یه جا گیر کنه ممکنه نتونه انجام بده ولی اگر خودش درگیر بشه، واقعا تأثیری که داره صدهزار برابره.  بچه‌هایی که تازه اومدن توی کار،…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/MatinSenPaii/4667" target="_blank">📅 00:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4666">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">من تاحالا وارد گیتهاب نشدم، پروژه گیتهاب دادی بهم گفتی برو برای خودت درستش کن
😭
😂</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/MatinSenPaii/4666" target="_blank">📅 00:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4665">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">:)) کاملا درسته بانو
❤️</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/MatinSenPaii/4665" target="_blank">📅 00:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4664">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شما فکر میکنید متین به سوالاتتون توجه نمیکنه و برای همین جواب نمیده اما روش تدریس متین اینطوریه که تمام چیزی که نیازه بلد باشی برای اینکه خودت بری دنبال یک چیز رو یاد میده و بعدش خودت باید تلاش کنی تا ازشون درست استفاده کنی.  دیروز یه پست برام فرستاد از هرمس،…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/MatinSenPaii/4664" target="_blank">📅 00:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4663">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شما فکر میکنید متین به سوالاتتون توجه نمیکنه و برای همین جواب نمیده
اما روش تدریس متین اینطوریه که تمام چیزی که نیازه بلد باشی برای اینکه خودت بری دنبال یک چیز رو یاد میده و بعدش خودت باید تلاش کنی تا ازشون درست استفاده کنی.
دیروز یه پست برام فرستاد از هرمس، بهش گفتم من هیچی نمیفهمم:>>
گفت جلسه قبل بهت یاد دادم چطور چیزی که بلد نیستی رو با استفاده از AI ساده‌سازی کنی برای خودت..</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/MatinSenPaii/4663" target="_blank">📅 00:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4662">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک کاری دارم میکنم مربوط به هرمس و مدل رایگان و ران کردن هرمس روی گوشی بدون هزینه و 24/7
نتیجه خوب بود بهتون میگم
😁</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/MatinSenPaii/4662" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4661">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بیش از ۹۰ هواپیمای سوخت رسان آمریکایی در اسرائیل حضور دارند و هواپیماهای ترابری به صورت گسترده و بی‌وقفه درحال پرواز به سوی اسرائیل هستند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/4661" target="_blank">📅 22:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4660">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">یکی از دوستان برای OpenWrt یک پنل مدیریت نوشته.
این پروژه یک اسکریپت نصب برای Aether روی روترهای OpenWrt است که امکان مدیریت از طریق LuCI و CLI را فراهم میکنه
https://github.com/moein8668-git/aether-openwrt-client
خودم تستش نکردم
اگر مشکلی یا باگی مشاهده کردید لطفا به توسعه‌دهنده اصلی گزارش بدید. (Issue)
توجه: این پروژه فقط برای روترهای OpenWrt طراحی شده.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4660" target="_blank">📅 22:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4659">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اگه بک‌اند کار می‌کنید و Go می‌زنید، پروژه‌ی Gsxui احتمالا براتون جذاب باشه. این پروژه کامپوننت‌های فرانت‌اند استایل Shadcn رو مخصوص اکوسیستم Go زده که اگه با ابزارهایی مثل HTMX ترکیبش کنید، می‌تونید خیلی سریع وب‌اپلیکیشن‌های تمیز و مدرن بسازید بدون اینکه درگیر فریم‌ورک‌های سنگین جاوااسکریپتی بشید:
https://ui.gsxhq.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4659" target="_blank">📅 19:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4658">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⏺
عراقچی: کتاب نوشتم، «قدرت مذاکره» نتیجه‌اش هم داریم می‌بینیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4658" target="_blank">📅 16:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4657">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
برای اینکه مطمئن بشی VPN درست کار(نشتی ip نداره) می‌کنه، می‌تونی از سایت BrowserLeaks استفاده کنید. این سایت IP فعلی، موقعیت تقریبی، اطلاعات شبکه و همچنین تست DNS Leak و WebRTC Leak رو نشون میده تا مطمئن بشی
#اطلاعات
واقعی اینترنتت لو نمیره. اگر بعد از اتصال به VPN، آی‌پی و DNS نمایش‌داده‌شده مربوط به سرور VPN باشه و نه اینترنت خودت، یعنی اتصال به‌درستی برقرار شده و نشتی وجود نداره.
این سایت ها
#امنیت
سرور و نشت در اپ ها رو نشون میده:
https://browserleaks.com/ip
https://myip.theazizi.ir/
@xsfilterrnet
👑
@xszapass
🤩</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4657" target="_blank">📅 15:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4656">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تا اکانت گیتهاب سازنده‌ی Aethery اندروید درست میشه، به هیچ وجه از پروتکل MASQUE روی اپ اندروید استفاده نکنید.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4656" target="_blank">📅 05:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4655">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iD8gaalBWJZi-D5Hs-vJ3y_qS0YIGtd3YhLOQYF4AE-GyZK4qwCAwBJw9S9mlv9vqrVT1dmCo7A8fDo8YhfcgfvCJ4v1DVvNZbre8-R8M9aredz0ZW_BBSQwyeZlrd6d0j216BjPvZc0PlxmvJ9VClIabQ_ND-53EKj2kyEz7ZqN1Km6L9IquJSGWHJuRYhUiB5AtRWdLgrkofHoDrPR6DH84eSN-_ybdEVBG_qD1Ht_UNDBucWpSufIsKMkggTMJArFsvGfPIiCW7aoOOffg4GSo9aU4rvS8Ic1uFCsB-urBxS96oh00GNvS3CMt1qhlW6Qr2Lf6OQf7dLDeahyZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4655" target="_blank">📅 05:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4654">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JreDwipb0lJtrKT6SPDMiPEVMweE_1BkkNROfMAPuTotGf23WFO2i5RR2ghmkMGA2s6g3sFcGAOEzRkCzevrEYKLgT_cXW2lAEVfB9FB4dltx0OJ40HF7YrwQ1rBnPT2_qGWF4fPedbdqBZ8hqZipM4w4WRl_84w76Yv0zWBAFS59ZO0JiriqEDCzocHbi4_g4p-pIrGiBnfVhlpeuzTSDQw38Un1LXCd5mg36IInNwTVu3E5dwoek2qYywcsO0P0KdKJM_tw32hKEeGGVGpnxaAaNBtZhcybdOKuSzYiIy74Iuqil8CO_wvKOnm-CNOL5a0KskvDxyE1kV5kgz23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با تشکر از علیرضای عزیز بابت تیزبینیش و زحمتای @CluvexStudio  این مشکل خطرناک که شانس MITM داشت حل شدش. حتما aether رو به نسخه‌ی 1.4.0 به روزرسانی کنید. آپدیت GUI هم به زودی منتشر میشه https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4654" target="_blank">📅 05:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4653">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آپدیت جدید Aether v1.4.0  https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0  توی این ورژن بیشتر رو امنیت و پایداری واقعی اتصال کار کردم (توصیه میشه حتما آپدیت کنید) :  فیکس امنیتی مهم: توی ورژن های قبلی اتصال MASQUE اصلا سرتیفیکیت سرور رو چک نمی‌کرد…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4653" target="_blank">📅 05:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4652">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether v1.4.0
https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0
توی این ورژن بیشتر رو امنیت و پایداری واقعی اتصال کار کردم (توصیه میشه حتما آپدیت کنید) :
فیکس امنیتی مهم: توی ورژن های قبلی اتصال MASQUE اصلا سرتیفیکیت سرور رو چک نمی‌کرد (verify کاملا خاموش بود)
یعنی از نظر تئوری یه نفر که بین شما و کلودفلر قرار بگیره میتونست یه سرتیفیکیت جعلی بده و ترافیک رو ببینه الان اضافه کردم که سرتیفیکیت edge کلودفلر با هش‌ های واقعی که pin شدن چک بشه هم روی HTTP/3 هم HTTP/2 این رو یکی از کاربرا (Matin Senpai) گزارش داد و خودش هم pull request فیکسش رو فرستاد بررسیش کردم درست بود، مرج کردم :))
فیکس مهم دیگه روی WireGuard و گول (WARP-in-WARP): گاهی اوقات "Connected" میزد ولی داده رد نمیشد. الان هر دو مدام چک میکنن که واقعا داده از طرف مقابل میاد یا نه.
اگه یه مدت هیچی نیومد خودش میفهمه تونل مرده و خودش دوباره وصل میشه. گول هم قبلا اگه تونل بیرونی قطع میشد کل برنامه میبست. الان اونم دیگه ریکانکت میزنه.
یه لیک هم فیکس شد: هر بار reconnect میشد (روی مسک یا وارپ) تسک‌ های پس‌زمینه‌ قبلی درست بسته نمیشدن. که روی نشست‌ های طولانی با قطعی زیاد رم رو الکی بالا میبرد. الان هر reconnect درست پاکسازی میشه. :))
--verbose
قبلا همه‌چی رو یهو میریخت بیرون که خوندنش سخت بود برای بعضیا که الان
--log-level
اضافه شده با ۵ سطح:
error warn info debug trace
دیگه راحتین :))
حالتِ info آرومه و عادیه
debug
جزئیات تونل رو نشون میده
trace
همه چی رو حتی تک‌تک پکت‌‌هارو
و...
Aether
الان موقع اجرا رم و تعداد هسته سیستم رو خودش میسنجه و اسکن و بافر ها رو خودش تنظیم میکنه که روی روتر یا برد ضعیف زیاد مصرف نکنه. با
--perf low/medium/high
هم میشه دستی مشخص کرد.
پشتیبانی از OpenWrt کامل‌ تر شد: علاوه بر armv7
الان بیلد استاتیک برای x86_64 و aarch64 هم هست
aether-linux-x86_64-musl.tar.gz
aether-linux-aarch64-musl.tar.gz
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4652" target="_blank">📅 04:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4651">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مدل Opus 5 توی یه سری بنچمارک‌ها از Fable 5 هم قدرتمندتر بوده توی کدنویسی
با نصف هزینه
ای کاش زودتر بیاد توی کلاد کد تست کنیم. فعلا توی اپ اومده</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4651" target="_blank">📅 00:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4650">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26436ea3fa.mp4?token=gyj1ho6L9VnRUX6JI3bDTvB5NR8TmVHmA8RHHnEB2xYuDvwFh4k70uUWIwalIV9Tn07OKsvmIkhBQ1o1Vfy3BiXWWvUVHELMWVJBd4aZeXfAPmiXFugXxjDHqnOUk7CXeUANvzpwfR0AJ5xabmUwY_Rs5gZ28Lu4cIysZwgceqUu9CV6vqB2L4FzIbB-j4z5tWomPqjNw8AWelElYWGFVFRkpoUeVcXqtZ56GMR8BY4vho2NcUrniTUMl9XAGaspXoU66zw_IHiZb2UwZ8mgnxgjKz1bi6Xp-mIe0CEADpWT0SNqOZVdnf0HE9j9oteEPeJTJYn6yZY2KuLT_UIGqjh1Szkp2C6fV4MWiVw1UCoJy2oNe2iNYch4sw5ALZuJuRE89GNVes7IJfN9C5J-fnQ38shiqNDdhtmegzKqNIojIwkOawdnyjxDPE-St_5yK65oB3vlszY_viWE3qDdQd9INJRgz-aaVoetWl8E0606qTNPDhsXx47yGUYgSjO60QDMYxrefP0Z4y5CFHHKmgNQBylwKzAD9JjAzf0wpxg42Al-7SOstYeeFxR5AKxTPfsRqVdWDHIV8ccxnFOzw1XZS22ILn9z4tFfifOhG_bE3wihAHyqwQyrZOgBx6rtSb1DpWET3_CV-cCHz_KK2Ricyw7nmZiz5AWuTYPfxQs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26436ea3fa.mp4?token=gyj1ho6L9VnRUX6JI3bDTvB5NR8TmVHmA8RHHnEB2xYuDvwFh4k70uUWIwalIV9Tn07OKsvmIkhBQ1o1Vfy3BiXWWvUVHELMWVJBd4aZeXfAPmiXFugXxjDHqnOUk7CXeUANvzpwfR0AJ5xabmUwY_Rs5gZ28Lu4cIysZwgceqUu9CV6vqB2L4FzIbB-j4z5tWomPqjNw8AWelElYWGFVFRkpoUeVcXqtZ56GMR8BY4vho2NcUrniTUMl9XAGaspXoU66zw_IHiZb2UwZ8mgnxgjKz1bi6Xp-mIe0CEADpWT0SNqOZVdnf0HE9j9oteEPeJTJYn6yZY2KuLT_UIGqjh1Szkp2C6fV4MWiVw1UCoJy2oNe2iNYch4sw5ALZuJuRE89GNVes7IJfN9C5J-fnQ38shiqNDdhtmegzKqNIojIwkOawdnyjxDPE-St_5yK65oB3vlszY_viWE3qDdQd9INJRgz-aaVoetWl8E0606qTNPDhsXx47yGUYgSjO60QDMYxrefP0Z4y5CFHHKmgNQBylwKzAD9JjAzf0wpxg42Al-7SOstYeeFxR5AKxTPfsRqVdWDHIV8ccxnFOzw1XZS22ILn9z4tFfifOhG_bE3wihAHyqwQyrZOgBx6rtSb1DpWET3_CV-cCHz_KK2Ricyw7nmZiz5AWuTYPfxQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از کاربرا اومده توی توییتر یه مقایسه‌ی خفن بین مدل‌های Claude Opus 5.0 و Fable 5 Max برای ساخت کدهای فضای 3D (توی وب) انجام داده.
نتیجه این شده که تکسچرها، نورپردازی‌ها و جزئیاتی که Opus 5.0 تونسته خلق کنه، اونقدر باحاله که هیچکس باورش نمی‌شه همه‌ش فقط با کد زدن ( و بدون نرم‌افزار گرافیکی) درست شده باشه.
البته مدل Fable 5 هم این فضا رو با یه بار تلاش (One-shotted) در آورد، ولی خروجیش جای کار و بهبودی داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4650" target="_blank">📅 20:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4647">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگر نمیدونید معماری پردازنده‌تون چیه، این نسخه رو نصب کنید
Universal</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4647" target="_blank">📅 14:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4642">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4642" target="_blank">📅 14:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4641">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saXCsiPoQKqVJClvV5XjBygED-H_Bm4_40ezQR_W4201NxvJqx9kWev2oPN3gwa5eGS1fMs1zsdkPm45PwGzlsutMDeAIOGNDuKb3_hFEm1TgYaVPVVv5AiufVZg-lvg871_LwMGjqXJzXxesUx0NR6_3OJ9wxYAmZW4g_O4h1G8Sq8gAC0SVc4IvL26lG9JD4rwRJMO-gq2iSMIvwC0nFehDWkUFXNRqsjXa1V_zSUXYSUbcsTUVUAdD7Vpubfwgu4PsXRRBjuY-2BOv3rbs16tZABGi4b8ICGx_LEtmsmcxSFOc37Gh7ZKsOdJC5AxUq55wVzng1TlRJR4rBg3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4641" target="_blank">📅 14:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4640">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4640" target="_blank">📅 02:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4639">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f8WuISoyPMq5VXYTy4YDBewoiqoOcZ8n2xqQFpmiuFhfgGcWOgqTdYIX5u0LLRgCRPGDfsUwjmUvwoDbaIkOlA7IXNFxXQKp1nArOWbxSwHcWoqEnn-O9UKwgzIyeNm1CfhiwZv8PMWVzOWnImVZmuAs_MQEvdYITUdTPPeJMx_CHmIYWzfgxUS-hEZEgyfvjhCWaY_mwT6sImytrCJsUpF-f-bxSN7MIakJW1VCx3WvmtB0Kl8huUTcfNSvFnoB-29_XgJkyrO_1cVJkK12k6qX2K1VKF5miSxguT0cMVM9TYPoti85FLlpvsWo3dcp_chBw3jIrmggpEQ88qLtMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استارتاپ Screenpipe ابزاری ساخته که تمام تصویر و صدای سیستم رو به صورت لوکال ضبط می‌کنه. این ابزار به Agentهای هوش مصنوعی یه «حافظه قابل جستجو» میده تا بدونن چی دیدین و چی شنیدین، که برای اتوماتیک کردن کارای تکراری و ساخت SOP خیلی کاربردیه.
میشه گفت رقیب اوپن سورس کلاد توی این مورد
https://github.com/screenpipe/screenpipe
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4639" target="_blank">📅 01:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4638">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انگار دارن یه چیزی رو روی فایروال تست میکنن</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4638" target="_blank">📅 17:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4637">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یهو خیل عظیمی از آیپی تمیزهای range 104 کلودفلر واسم از کار افتاد
ایشالا که خیره</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4637" target="_blank">📅 17:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4636">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehFzzT_RISTKvFQlyCf093xLLUpX1DW7dW8IgO1SXnTipPWu6FH5720qvDc9YsyJtaEm6mHSpW_C4QZZrSJcjNmWqryTl_cFh5VZWsW3jwkcgEo1gcchfEWXWqMNvLDo98Y2xfcelPHfS8Rs0nUrAmRm2Uyazp1TYpWBIm4cEtNWA99sIThvqnsV9QpPC4MwYQf5dg1LiPtpdqzslV9YacCs4zAlUuhWNAIEeENu1RXKLIDh4KIB_rhYzHG5pvx7CTtBg7mg5fp9UcnIHyAAS8HOdAPs-zWWALkbfEqiw1nBKmgXr5JDCP_W1dBqnNRnrfb4beurewppxMgp5vJEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4636" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4635">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aafx8D49snlTEPCeii3XDH4bHMkwmi9hknTWzoXms4oGQb9r26EaJqbabTPH5bmuZ7O248QZ4yChoYiJVP9m9CA50XrL9tVuNTKsPBKzJVJT4_0vLum94SEk_ztB0DUziDWwA0dPF-7IdcKg4b-2fhcPMhU3CZGd443AbAIBaTcKGMGNOlzZG3ueHoXl0mTMxfYcVtbg3CaKF5X_op4Nc2tsSt_XUmQ2BxNJ5QG9O2tSeGiN3ARhCYzNVEqvt1qMfyF33c3snBXlaG8FWGDwgAg1qpejQATVAVtMuKXmcCf-behmYJAAPxqemmoTm2KWvf9Mhh7jBaYcwNERnziFJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام
😭
اکانت Nous Research سازنده‌ی هرمس ریپلای زد روی توییتم
ولی واقعا قدرت این ترکیب hermes+9router+opencode+mimo هنوز باورم نمیشه که از پس این تسک پیچیده بر اومد</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4635" target="_blank">📅 04:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4634">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بچه‌ها من اگه کمتر هستم این روزا، چون دارم روی یه سری ویدئوی کاربردی کار میکنم که اگر اینترنت قطع شد به دردتون بخوره. و یه سری مهارت که تا اینترنت قطع نشده بهتره یاد بگیرید که بعدا اگر لازم شد آموزشی بدیم، بتونید سر راست برید سراغش</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4634" target="_blank">📅 02:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4633">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard  https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4633" target="_blank">📅 21:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4632">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4632" target="_blank">📅 19:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4631">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دقیقا. درخواست نوشتن راجب ریتالین هم داریم چون متاسفانه خیلیا به خطراتش آگاه نیستن</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4631" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4630">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">متاسفانه من مثال‌های واقعی زیادی از مصرف خودسرانه خیلی از دارو ها دارم میبینم و متوجهم که ما همیشه دنبال یه راهی هستیم که زودتر جواب بده، اما همین راه‌ها هم بدون آگاهی ممکنه شرایط رو بدتر کنه
❤️</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4630" target="_blank">📅 18:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4629">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.  ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4629" target="_blank">📅 18:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4628">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.  ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4628" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4627">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngvd2b927kt5RH5QKeQjxzsN4BZRKNv15f3Ct2zSH6GsgKjN-uLt0QLuzOu0QOWnWWpgFTiFp_TC6zMkvCt7e8FGwJ7apxUjtXjMMsswiXADi0p_V03llnRF4sp7NUb1uKAWnB8fd115_R7fOY4GBcm13pWpeB2L4kHGO7eZXkfQfAWJoPZxfL3JqpOxrOAFWRrCj8jCT-pOu-Or9maYNB4-NEI0iXcf48qJFdnh0WABCYF1ljsRwqlXPLt5uYy3e-CuRwL5XiglBsP3_7oounqnYFRyFVxRPujTmYP9lq13JyJ7PdGsfzUt7GLd1653h-l4jeH2nexCmadQvD9OLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.
ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد ایمن محسوب می‌شه، اما درباره استفاده طولانی‌مدت هنوز اطلاعات کافی نداریم. بعضی مطالعات، مصرف طولانی‌مدت اون رو با افزایش برخی مشکلات سلامتی مرتبط دونستن، هرچند هنوز رابطه علت و معلولی ثابت نشده.
از طرفی، عوارضی مثل خواب‌آلودگی روزانه، سردرد و سرگیجه هم ممکنه در بعضی افراد دیده بشه.
ملاتونین
دارویی هست که به‌صورت آزاد می‌تونید از داروخانه‌ها تهیه کنید؛ پس تحقیق درباره نحوه مصرف و حتی مشورت با یک متخصص قبل از استفاده از اون، اهمیت زیادی داره. معمولاً پزشک با توجه به شرایط فرد، پاسخ بدن به درمان و علت بی‌خوابی، دوز و مدت مصرف رو تعیین می‌کنه. اما اگر قصد مشورت با پزشک رو ندارید، بهتره از مصرف خودسرانه و طولانی‌مدت، به‌خصوص بیشتر از یک ماه، خودداری کنید.
جدای از همه این‌ها، بسیاری از متخصصان خواب معتقدند ملاتونین نباید اولین راه مقابله با بی‌خوابی باشه. تا زمانی که سبک زندگی، بهداشت خواب و عادت‌های روزمره اصلاح نشن، نباید انتظار داشت هیچ دارویی به‌تنهایی مشکل بی‌خوابی رو برطرف کنه.</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4627" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4626">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHQWIDaubWxwmBSTJ-4LSIjMbVLphq57GKbA2f4tD0D939unLrJ1b2fftO90J01303Z-5PSWfnPedMvZCKiZ5SqAozGbAwKlKR38VSDQPng-IfL9EhZlUP4bNbBqZeG48Yl3jB2ExlkmbUD4Cd8Xq8ogmhCxdte1gZH3lN-RhmRbPtedPb9DBy-3Fc-tVILPxkOTbOPGxIzy7WMpPfiwtF6t-xe9QAHQTfQrqelM816qXZFZevFxp9QU3fcvW1XfLKT2wOlYSjVWP7hDGiqbDUqFhj3olqX2KHR_2LvReJZ6ZnjzQSOnHKi4X8sVqN0oxzAv2WHQT7bLWuuYKzD77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای فقط داره گند میزنه
الان نفهمیدم واقعا چرا نیازی به 3.6 flash بود
😑</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4626" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4625">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بچه‌های Fireworks AI یه بررسی تخصصی منتشر کردن که نشون می‌ده مدل Kimi K3 نه تنها با Fable در حال رقابته، بلکه ترکیبشون به سطح SoTA (بهترین عملکرد فعلی) تو خیلی از بنچمارک‌ها رسیده و می‌تونه انتخاب خیلی جذابی برای برنامه‌نویس ها باشه.
البته برنامه‌نویس‌های پولدار متاسفانه
😞
https://fireworks.ai/blog/kimik3-fable</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4625" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4624">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4624" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4623">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4623" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4622">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4622" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4621">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4621" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4616">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4616" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4616" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4615">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4615" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4607">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4607" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JmTFye_mR0CcvvpttLha7vmJeOh7NAr3WfFAbSE8y81pdBTLLAhmBHXb77F1zJo8R4kiOCfFgKTrNIAeu61ZuuIbQXVRy8-6-CdcXB4T9rtwnOJcGwa9Q7eLxZer3Gw5cvpAPsLo61UD3j8n3n27PgUKaKmFRR_Dz7lQJ8gIOPGawAhWjfp-Z5q2ExSmYSGala6nxrQtQf1neVq7H3ty_VuvB1ecHxR2RslQiHSiDvO-kULZ7Y6BAfKkSCU59DnRrwE0E-aAsqCGHRPZe4E-lJwabWz65B1o9brJ67G_RFgbU3BBUBt0D8iVg0rNqh1FyRB0Wo35aJcwaxkq7mQmGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4606" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4605">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یه مقاله توی
exe.dev
خوندم، راجب این بود که اوایل سال ۲۰۲۵ خیلی‌ها می‌گفتن هوش مصنوعی مثل یه «کامپایلر» جدید عمل می‌کنه؛ یعنی همون‌طور که کامپایلر زبان سطح پایین (مثل C++) رو به زبان ماشین تبدیل می‌کنه، هوش مصنوعی هم «زبان طبیعی» (مثلا فارسی) رو به «کد» تبدیل می‌کنه.
اما الان جواب فرق کرده:
نه، کلاد کامپایلر نیست؛ خیلی از اون بهتره!
چرا؟ فرقش چیه؟
توی دنیای واقعی، نرم‌افزار لایه‌لایه ساخته می‌شه.
مدیرعامل استراتژی می‌ده
👈
مدیر محصول فیچر تعریف می‌کنه
👈
آرشیتکت معماری می‌چینه
👈
برنامه‌نویس کد می‌زنه
👈
و در نهایت کامپایلر کد رو باینری می‌کنه.
هرکدوم از این لایه‌ها دارن جزئیات رو مشخص‌تر می‌کنن و کلی
تصمیم‌گیری ا
نجام می‌دن. مشکل اینجاست که ارتباط بین این لایه‌ها پر از اصطکاک، و جلسات خسته‌کننده‌ست.
کار اصلی کلاد اینجاست: هوش مصنوعی می‌تونه
به‌صورت عمودی توی تمام این لایه‌ها حرکت کنه
. کلاد می‌تونه همزمان باهاتون درباره استراتژی محصول بحث کنه، معماری بچینه، کد بنویسه و بهینه‌سازی ماشین رو انجام بده؛ بدون اینکه نیاز باشه واسه هماهنگی اینا جلسه بذارید یا از کسی اجازه بگیرید.
یه مثال واقعی
:
نویسنده‌ی مقاله می‌گه برای سیستمشون نیاز به یه سرور DNS توزیع‌شده و سریع داشتن. به جای اینکه خودشون بشینن کد بزنن، اومدن چند تا ایجنت هوش مصنوعیِ موازی (کلاد و کدکس) بالا آوردن تا کل سیستم رو براشون بسازن.
نکته‌ی جالب ماجرا اینجا بود:
وقتی خروجیِ ایجنت‌های مختلف رو با هم مقایسه کردن، دیدن ایجنت‌ها کلی از مشکلات لبه (Edge cases - مثل وقتی که دیتابیس Rollback می‌شه) رو
خودشون متوجه شدن و بدون اینکه از برنامه‌نویس بپرسن، براش راه‌حل و منطقِ کدنویسی طراحی کردن
.
هرچند اگر نظر منِ متین رو بخواید، ai همچنان نیاز به یک متخصص خوب داره که بتونه دیتاش رو Validate کنه، پس به یادگیری ادامه بدید دوستان خوب من
🔥
🔗
منبع:
https://blog.exe.dev/claude-is-not-a-compiler
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4605" target="_blank">📅 00:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4600">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4600" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4600" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4599">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev7gtkU98G9fxjuUvBb8DJ4B4Em4DFUWt8Y1l5baIV0sGfoDXr3FAT7Jb5Do_Bs4e7aaKxdu-sA8aIf9l1mrjEczJUvJ9MFP8yoV9hxGdmMfyv2b9Qky-7D3n0F9YZdLuIrJcW7tVVfdORjfCcPO0fR8RLR9ZNyiHYom5o9EzcWDvHNZsB3tk412Q0Sg0iE7h3TgWPVJIPTQPmA6Ukl7uOnEWGkgsY3dCQE-LChUmkryMkJ8e-1pReoRgXY0OtC7ZqaeqKDQ6ikqq8ljV_DJT8KGXWFr-IqJs30jPWAuqytC1wdhw4WmqHuBq0aFP9-FGD1gzHkVQmdZ-NNOr5YEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4599" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4598">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگه شما هم با نمایش متن‌های فارسی در Claude مشکل دارید، ریک سانچز راه‌حلش رو براتون آماده کرده! فعلاً این ابزار برای macOS منتشر شده و کاربران ویندوز باید کمی منتظر نسخه‌ی مخصوص ویندوز بمونن. در طراحی این پروژه، به یاد زنده‌یاد صابر راستی‌کردار، خالق فونت…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4598" target="_blank">📅 16:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4597">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/crssc6kJA_aDsFBGcq1GO2kW8V4YzVQamYwJzwFThm6u76YvkMtMOrea7B81hs2T1gtmwQbG0Wo2ok0niQwOyJ3bgFDIsHjtL1ztFUNmJQGPRo64l_LdHX-J_7vaCWISpqKKoMa89vI35qC0d1qoq-ZRHgB1SYfx1k1hfBTAfRjqRfwUewCcqdLLz02Q1DV0jl4MBcbpaGyet2HRxQzZPaktcfPmmTMhGCBWgf_2SsjsszzE_s7XUDUsr2_KXnS-hGCJRSYZeL-Xyp7rzdvbL-WfJqHIvTFoIjd4qcvv3rFpL0pWDOIMmD0FIQH0nndhBTjx71CRlh8oS8KbRE6IFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4597" target="_blank">📅 15:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4596">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUWZjd2xEFVXs9fCgi7-e3DTC0WtPTcEJ3o8n73TyaKB5NRJ5KTTHDn9cqM4k_S1zw3FH7Me_ZmfrBjTWCTKWnaEElINXCj9iEi5Cz-fPlDsY_DFvEcXhajr-r0IKEAHV3cTNAEIpqTuT0sbJ0K6IiR5xkEzbG2LTUHlVH_oVul7l35fy-HzmAgkC-D_wM9hDyqcuyQK63iCZ8F6SYlInHGefKTfzUXS6JgQBqIm2qU5_0nrkExD8FXi9aivgqVFQbtMD3HevD1w4MVUSuiwDZPcGbix1UDLgcaNMKgZE1riY9uiTIumoSd1szoWbCOMKczSYuudMAGXhDO6EE05ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه شما هم با نمایش متن‌های فارسی در Claude مشکل دارید، ریک سانچز راه‌حلش رو براتون آماده کرده!
فعلاً این ابزار برای macOS منتشر شده و کاربران ویندوز باید کمی منتظر نسخه‌ی مخصوص ویندوز بمونن.
در طراحی این پروژه، به یاد زنده‌یاد صابر راستی‌کردار، خالق فونت وزیرمتن، از همین فونت استفاده شده است.
کافیه لینک زیر رو به Claude بدید و ازش بخواید نصبش کنه؛ بقیه‌ی کارها رو خودش انجام می‌ده:
https://github.com/m4tinbeigi-official/claude-rtl-patcher
به همین سادگی و خوشمزگی!
😄</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4596" target="_blank">📅 14:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4595">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ot-gHWVdNpkBKU2CLhov8qhvk2X8SMSMFGQR5fFZ601UCih2_Y52Mf1doFh5z9M6cQymAY5iHpUuIHKjS1SWxYlHqGVSTL3KSZ_zsW60UuB9YJ7PlfglA2Y1jrA5ZCP0pqkpooosQBSJGy-JqV0XGjv8Sx4q9IjA_IHg6S87IoIHYMJmUR9RtVwTbOxcfyKrNtT6KBsPsnxKz6hXicxamawbJzfAYINTl6xDXEvbLTRvOfUA5cdkcvPYXYRO3Kd9cVRflGXy9dsAsdj3BSJYc3xKjgeojwnuoTTgoMZ6DMdYydaBEfYiRIEUvxjZ7e_CfNt6cHAVX6Aa1ARC9htNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده است.
✨
مهم‌ترین ویژگی‌ها و تغییرات این نسخه:
🔹
نصب سریع با One-Click Wizard:
دیپلوی پنل حالا فقط از طریق ویزارد آنلاین و اختصاصی انجام می‌شود و پس از نصب، یک لینک کاملاً پرایوت به شما می‌دهد (روش‌های نصب دستی روی این نسخه کار نمی‌کنند).
🔹
داشبورد مدیریت داخلی (Admin Dashboard):
امکان آپدیت پنل به نسخه‌های جدید، حذف کامل پنل، و ریست پسورد مستقیماً از داخل خود پنل اضافه شده است.
🔹
راه‌اندازی ربات تلگرام:
مدیریت کانفیگ‌های تکی، دریافت لینک‌های سابسکریپشن و مانیتورینگ مصرف (همراه با هشدار مصرف بالای ۸۰٪) از طریق ربات تلگرام.
🔹
حذف کامل Environment Variableها:
تمام متغیرهای ثابت (مثل VLESS UUID، Trojan Pass، Proxy IPs و...) از داشبورد کلودفلر حذف شده و مستقیماً داخل پنل قابل آپدیت و مدیریت هستند.
🔹
ارتقای چشمگیر امنیت:
لاگین به پنل حالا نیازمند ایمیل کلودفلر شماست.
مسیر ورود به پنل به یک آدرس تصادفی و امن (Secure Path) تغییر یافته (دیگر با زدن
/panel
وارد نخواهید شد).
🔹
تنظیم سریع Custom Domain:
دامنه‌های سفارشی خود را می‌توانید مستقیماً از بخش Common settings وارد کنید تا کانفیگ‌های مربوطه با تگ
D
به سابسکریپشن شما اضافه شوند.
🔹
قابلیت‌های جدید شبکه و پروکسی:
پشتیبانی از Xhttp و VLESS Encryption برای Chain Proxy در هسته‌های Xray و Clash.
🔹
انتقال آسان تنظیمات:
اضافه شدن قابلیت جذاب به‌روزرسانی و همگام‌سازی تنظیمات از یک پنل ریموت BPB دیگر.
⚠️
نکات بسیار مهم برای اتصال کلاینت‌ها:
حتماً کلاینت‌های خود را به آخرین نسخه آپدیت کنید (حداقل Sing-box نسخه 1.12.0 و v2rayNG نسخه 2.2.3 به بالا).
برای اتصال پایدار در v2rayNG، حتماً گزینه
Hev TUN
را فعال کنید.
در صورت مشکل با فرگمنت در برخی ISPها، حالت
Packet
را روی
1-1
تنظیم کنید.
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
@whitedns</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4595" target="_blank">📅 13:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4591">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-poll">
<h4>📊 دوستان پروتکل WireGuard واستون وصل میشه؟</h4>
<ul>
<li>✓ 1- وصل میشه توی Aether، اما پینگ نمیده توی V2ray یا تلگرام🚫</li>
<li>✓ 2- کلا توی Aether هم وصل نمیشه🚫</li>
<li>✓ 3- وصل میشه، اوکی هم کار میکنه✅</li>
<li>✓ 4- دیدن نتایج(حال نداشتم تا الان aether رو ران کنم)🤡</li>
</ul>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.5.0 منتشر شد(با پشتیبانی از MacOS و Linux)  توی این ورژن، هسته (Core) برنامه رو به آخرین نسخه یعنی v1.3.0 ارتقا دادم. که توی این نسخه تمرکز روی پایدار کردن اتصال و اسکنر بوده. یه سری ویژگی کاربردی هم به رابط کاربری اضافه شده.  تغییرات…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4591" target="_blank">📅 01:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4590">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ee4r7PJD3zhILmmWVLRf0PUP96j6zMSMX8Rwk7D5kfQikdKAzvgFqIpYfEUUmuNZGZD-8Ic3Zmq3d-bxcm_oB2DWcKBQDzSQkn7uSHrWa8WsnhkjvsRsllxaXMLe-Evqbl-F53sAqcnAFLRng-C3EGMVilr7yzN-E6qy8hKmz_PxMNrzJ8strBsjRzxTVAjExmMdDpyBuF0IHe94M_MfadGDTklp66Kc0FpkIL-yFutKM52qjDmpVY01m7yIXkH7pNTkfvXPTjhJCb0Mi66WI4FBtQcxHP1-ERnrrfGV-I4ddo3Q2Mv_7wcoQkxAf3oVySTI6_NIcQa4W3asA0JZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.5.0 منتشر شد
(با پشتیبانی از MacOS و Linux)
توی این ورژن، هسته (Core) برنامه رو به آخرین نسخه یعنی v1.3.0 ارتقا دادم. که توی این نسخه تمرکز روی پایدار کردن اتصال و اسکنر بوده. یه سری ویژگی کاربردی هم به رابط کاربری اضافه شده.
تغییرات اصلی این نسخه:
1-
اسکنر قدرتمند Ironclad:
بقیه حالت‌های اسکن فقط چک می‌کردن که آیا Gateway پینگ می‌ده یا نه. اما Ironclad یه تونل کامل و واقعی می‌سازه و یه درخواست HTTP ازش رد می‌کنه تا صددرصد مطمئن بشه که کار می‌کنه. یکم کندتره، اما قطعی‌ترین حالت ممکنه
2-
اتصال مجدد (Reconnect) هوشمندتر:
قبلاً اگه اتصالتون قطع می‌شد، Aether می‌رفت از صفر کل آی‌پی‌ها رو اسکن می‌کرد (که تو حالت‌های سنگین ممکنه چند دقیقه طول بکشه). الان اول همون آی‌پی‌ای که تا دو ثانیه پیش کار می‌کرد رو دوباره چک می‌کنه؛ اگه واقعاً مرده بود تازه می‌ره سراغ اسکن کامل
3-
اضافه شدن بخش Obfuscation:
این قابلیت دستتون رو باز می‌ذاره تا شدت مخفی کردنِ هندشیک از سیستم‌های فیلترینگ (DPI) رو تنظیم کنید. پروفایل‌هاش با توجه به پروتکلی که انتخاب می‌کنید (MASQUE یا Wireguard) متفاوته. اگه دیدید رو حالت دیفالت وصل نمی‌شه، درجه‌ش رو ببرید بالا
4-
تغییر پورت و Bind Address:
الان می‌تونید پورت SOCKS5 رو به دلخواه تغییر بدید یا اینکه روی آی‌پی
0.0.0.0
ست کنید تا پروکسی رو به کل شبکه‌ی لوکال (مثلاً موبایل‌ها یا تلویزیون تو خونه) Share کنید. اون باگ کلافه‌کننده‌ی پروتکل UDP هم بالاخره تو هسته فیکس شده و الان بدون مشکل توی شبکه‌ی لوکال کار می‌کنه.
5-
پشتیبانی کامل از مک و لینوکس:
این اولین نسخه‌ایه که کاملاً مولتی‌پلتفرمه! فایل‌های نصب ویندوز (exe و msi)، فایل‌های مخصوص مک (برای چیپ‌های اینتل و اپل سیلیکون به صورت جداگانه)، و انواع پکیج‌های لینوکس (deb، rpm و AppImage) رو براتون گذاشتم
6-
رفتن به System Tray:
گزینه‌ای اضافه شده که وقتی برنامه رو می‌بندید، به جای خروج کامل، بره تو تسک‌بار پایین ویندوز و همونجا تو پس‌زمینه کارشو بکنه
ممنون از
@rqzbeh
عزیز بابت مشارکت‌هاش تو این آپدیت؛ و ممنون از
@CluvexStudio
عزیز بابت زحماتش روی هسته‌ی برنامه
لینک گیت‌هاب برای دانلود نسخه‌های مختلف:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.5.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4590" target="_blank">📅 00:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4589">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بعد میگن شبکه‌های اجتماعی چطوری پول در میارن
"Data"</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4589" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4588">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اون روز داشتم از claude راجب s3 storage سؤال می‌کردم و کمی داشتم دانشم رو بالاتر میبردم، صرفا سوال جواب بود فرداش فید گوگلم پر شده بود از خرید فضای ذخیره سازی s3 و کمترین قیمت s3 و...</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4588" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4587">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اون روز داشتم از claude راجب s3 storage سؤال می‌کردم و کمی داشتم دانشم رو بالاتر میبردم، صرفا سوال جواب بود
فرداش فید گوگلم پر شده بود از خرید فضای ذخیره سازی s3 و کمترین قیمت s3 و...</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4587" target="_blank">📅 00:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4586">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه مقدار برای همین طول کشید. اما خودم هم بیلد رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4586" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4585">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در حال آپلود</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4585" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4584">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SD94ClDl5QuUeat5w5DOJfg5z1EHfEY_0TlnIktmHVqaOroerR5oHIjuOK4pLNQFVoCSjA9v0dBhGvbEmbTLYET-4PpOnX-Ldb3uVpntp6r8X_KKM7WDslHev80Awgje3GId_CSGRsheryAzwLWlBDMhx30vUljeWmiRBAj5IjDILRU6fdCknuuB3uTGx_a1ZaeIyIOJqNF2gXl3pRkzd3YXce1uGb8UuvsLViB9NOD4wiVdysbddtF78bNGjfy1nZt8e10RiU7bUGPSLumvecuH1lR6OJ_8TwtoG6dO4DYw4UfLHxGAYHQDS-6HvWutMvItuJypTLCh9HDiqnD5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی تغییرات جدید به GUI اضافه میشه
🙏</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4584" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4583">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4583" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4582">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هکرها زدن کل دیتابیس ثبت اسناد و املاک رومانی رو پاک کردن:)))
یه هکر الجزایری به اسم ByteToBreach (که اسم واقعیش زکریا محجوب از شهر وهران الجزایره و قبلاً هم پورتال دولت سوئد رو هک کرده بود) با استفاده از اطلاعات ورودِ یه کارمند، وارد شبکه‌ی سازمان کاداستر (ثبت اسناد و املاک) کشور رومانی می‌شه.
هکر اول کل سیستم‌ها رو مپ می‌کنه و اسناد و اطلاعات کارمندا رو می‌دزده، بعد سعی می‌کنه ازشون باج بگیره. وقتی دولت رومانی باج رو نمی‌ده، هکر کل دیتابیس ثبت اسناد کشور رومانی به اضافه‌ی بکاپ‌های آنلاینشون رو پاک می‌کنه
😂
(یعنی عملاً کلاً نابودشون کرده).
این کار باعث شد کل بازار املاک و مستغلات رومانی فلج بشه و دفاتر اسناد رسمی نتونن هیچ سندی رو ثبت کنن. هکر هم دیتای دزدیده شده رو تو یه فروم دارک‌وب گذاشته برای فروش
👌
خب باج رو بهش میدادین دیگه ای بابا
مقامات رومانی گفتن که دارن کل شبکه رو از صفر می‌سازن. با اینکه هکر ادعا کرده تمام بکاپ‌ها رو پاک کرده، اما خبرنگار ریسکی‌بیزنس (Risky Biz) می‌گه به احتمال زیاد اونا یه نسخه‌ی بکاپ آفلاین (Cold Backup) داشتن، چون اگر اصلاً هیچ بکاپ آفلاینی نداشتن، فاجعه‌ای تو رومانی رخ خواهد داد که تا ماه‌ها نمی‌تونن ثابت کنن کی صاحب کدوم زمین و خونه‌ست! یا اینکه باید برن از دارک وب، اطلاعات خودشونو بخرن
😂
😂
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4582" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4581">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/I92YrScioYdN0EOXWPDgS6NiD7ezMko9YG3hCoPgFjpf28-vRCKuv5ulM86DTKIQ397-aA-XoVJycFd94Wgu29Mg-b2UVhcxohtfg_dR15sdYJrR2ufIDhxTbRQxQLg1P0SdBuzGOgI-whdhYQZXFBTbYF0TRaZgr20vrqFkff_Lz3ZcCqn9Ga4BA_nmUOTjjDj6XqqRhecD0vwwVEBKvufFBKW7DNSjjtjtNDG0lHCsLD_ac40EMj0XtF8-eYvXEYjHl05LhKTE876tSSl_iqO3tyX_x9QbSWv1L6oPCZoTLEQYjH-lMPYsYHWhruwDRU5b7hjCfaFc-EHhGbvVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4581" target="_blank">📅 14:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4580">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آپدیت جدید Aether v1.3.0:  https://github.com/CluvexStudio/Aether/releases/tag/v1.3.0  توی این ورژن بیشتر روی اسکنر و پایداری اتصال کار کردم:  یه حالت اسکن جدید اضافه کردم به اسم Ironclad توی این حالت برای هر IP کاندید Aether یه تونل واقعی و کامل میسازه و…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4580" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4579">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether v1.3.0:
https://github.com/CluvexStudio/Aether/releases/tag/v1.3.0
توی این ورژن بیشتر روی اسکنر و پایداری اتصال کار کردم:
یه حالت اسکن جدید اضافه کردم به اسم Ironclad توی این حالت برای هر IP کاندید Aether یه تونل واقعی و کامل میسازه و یه درخواست HTTP واقعی از توش رد میکنه نه فقط یه پینگ ساده. :))
یعنی اگه یه Gateway رو با این حالت انتخاب کنه مطمئنید که واقعا کار میکنه نه فقط جواب پینگ داده. کندتر از بقیه حالت‌هاست چون کار بیشتری میکنه... ولی از نظر قطعیت بهترین گزینه‌ست و همینو پیشنهاد میکنم.
- ریکانکت سریع‌ تر بعد قطعی قبلا اگه تونل قطع میشد (چه MASQUE چه WireGuard) Aether مستقیم میرفت سراغ یه اسکن کامل از صفر که توی حالت‌های سنگین‌ تر مثل Ironclad میتونست چند دقیقه طول بکشه. الان اول همون Gateway قبلی که کار میکرد رو یه تست سریع میگیره
و فقط اگه اون دیگه جواب نداد میره سراغ اسکن کامل.
فیکس UDP روی SOCKS5 وقتی پروکسی رو روی شبکه لوکال باز میکردید اگه AETHER_SOCKS رو روی یه آی‌پی غیر از
127.0.0.1
ست میکردید تا از دستگاه‌های دیگه توی شبکه هم بشه وصل شد
بخش TCP درست کار میکرد ولی UDP هیچ‌ وقت رد نمیشد
فیکس کردم. (گزارش یکی بود issue )
پشتیبانی از OpenWrt یه بیلد استاتیک جدید اضافه شد (aether-linux-armv7-musl.tar.gz) که مخصوص روتر های OpenWrt و سیستم‌های مبتنی بر musl هست.
(یکم مشکل بود این قسمت، کلی وقت گرفت، یکم دیر شد سر این بود)
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4579" target="_blank">📅 09:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4578">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گویا شرکت Moonshot ، توسعه‌دهنده‌ی مدل چینی Kimi 3 انقدر به خاطر تهاجم مردم فشار اومده به سرورهاش که کلا فروش اشتراک‌های جدید رو متوقف کرده:))
همینطور اونایی که قبلاً اشتراک ۲۰ دلاری رو خریدن هم شاکین. چون مدل سنگینه، توکن‌ها خیلی سریع‌تر از مدل‌های قبلی مصرف می‌شه و کاربرها می‌گن بودجه‌ی هفتگیشون تو دو روز اول تموم می‌شه. (این رو با مدل قبلی یعنی K2.5 که خیلی به‌صرفه‌تر بود مقایسه می‌کنن).
توی فروم‌های تخصصی (مثل Hacker News) بحثِ جالبی راه افتاده؛ خیلیا می‌گن دقیقاً به خاطر همین مشکلاته که ما باید به سمت مدل‌های اوپن‌سورس و اجرا روی سخت‌افزارهای خودمون بریم، وگرنه حتی بزرگ‌ترین استارتاپ‌ها هم یه جایی زیر بارِ ترافیکِ مدل‌های هوش مصنوعی زانو می‌زنن.
هرچند توی ایران متاسفانه نمیتونیم زیاد به همچین چیزای گل و بلبلی که خارجیا میگن واقع‌بینانه نگاه کنیم</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4578" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4577">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هرچقدر بگم هرمس برای تحقیق و پیدا کردن گسترده‌ی یه چیزی عالیه کم گفتم</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4577" target="_blank">📅 23:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4576">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبر فوری :  ‏اگر سایت وردپرسی دارید حتما هسته وردپرس رو آپدیت کنید دو تا باگ SQL Injection و RCE داره  نسخه های اصلاح شده: WordPress 6.8 → 6.8.6 یا جدیدتر WordPress 6.9 → 6.9.5 یا جدیدتر WordPress 7.0 → 7.0.2 یا جدیدتر    @Linuxor ~ seramo_ir</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/4576" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4575">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">خبر فوری :
‏اگر سایت وردپرسی دارید حتما هسته وردپرس رو آپدیت کنید
دو تا باگ SQL Injection و RCE داره
نسخه های اصلاح شده:
WordPress 6.8 → 6.8.6 یا جدیدتر
WordPress 6.9 → 6.9.5 یا جدیدتر
WordPress 7.0 → 7.0.2 یا جدیدتر
@Linuxor
~ seramo_ir</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/4575" target="_blank">📅 20:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4574">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNuA8YJCCwcC-yQTvDyQtudWPAfFzbjiP8cBmc16mhvVWoAg2ki88xhR9C5F2IgTCcYX3gEfGGlha001WbJ5VbvbpQXKpVcT8prO0YfBIL4QTGCRHdQf-K1MKceEoWFFfY9IK3ixrNVUS_acIJYnmbEx17aDVyfim9pHfjoAcUrHppbo7BWh8EfdswUNrscA6viHyyCbesmc_kQpa4oG9LewSsJJCEUjFV5L7tHOBFMRIe7JGZ1XUq771Zkm3NOIjGxxT_A4rXz5OZY2zjmkkWxKGiqn_c6MQqPBoYZxtj7Zy00nfpWaMQ14pCfqHjYTWY67HQUMg2-p_JYufNXJUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌های متخصص امنیت (که توی حوزه SOC و Red Team فعاله) یه سایت و کامیونیتی زده به اسم VulnCity (شهر آسیب‌پذیری‌ها). که یه مرجع جامع و دورهمی برای بچه‌های امنیته.
1- مقالات و آموزش‌های دست‌اول: مؤسس سایت هر چیزی که توی پروژه‌های واقعی (مثل Red Teaming) یاد می‌گیره رو به‌صورت مقاله می‌ذاره اونجا.
2- شبکه‌سازی: بچه‌های امنیت می‌تونن با هم چت کنن، پروفایل همدیگه رو ببینن و یه تیم بسازن.
3- بخش Vulndark: یه قسمت باحال داره که اخبار مارکت‌های فعال دارک‌وب، فعالیت گروه‌های هکری و خبر لو رفتن دیتابیس‌ها رو پوشش می‌ده.
آدرس سایت:
🔗
https://vulncity.com
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/4574" target="_blank">📅 20:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4573">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فرق H3 و H2 برای من روی یه اینترنت، 18 و 2 مگابیته
یعنی H2 سرعتش پایینتره
همینطور وایرگارد و gool هم برای من همون سرعت H3 رو دارن</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4573" target="_blank">📅 20:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4572">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">من حس میکنم به قدرت gool پی نبردید
یه تست بکنید جداً</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4572" target="_blank">📅 14:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4571">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-poll">
<h4>📊 حالا دوستان MASQUEـی، بهم بگید کدومش بهتره توی آپلود/دانلود؟</h4>
<ul>
<li>✓ http/3</li>
<li>✓ http/2</li>
<li>✓ مسکی نیستم دیدن نتایج👺</li>
</ul>
</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/4571" target="_blank">📅 14:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4569">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-poll">
<h4>📊 توی Aether بیشتر روی کدوم پروتکل بودید و براتون بهتر بوده تا الان؟</h4>
<ul>
<li>✓ 1- MASQUE</li>
<li>✓ 2- Wireguard</li>
<li>✓ 3- Gool(warp-in-warp)</li>
<li>✓ استفاده نکردم</li>
</ul>
</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/4569" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4568">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
اگر دنبال یه آرشیو کامل از یاد گرفتن ساخت کانفیگ با سرور شخصی و تمام روش های
#اینترنت
آزاد هستید از مبتدی تا حرفه ای میتونید از این آرشیو کامل که یکی از بچها زحمت کشیده و آرشیو بسیار کاملیه استفاده کنید.
لینک سایت:
👇
(باز نشد با فیلتر برید)
filtershekan.sbs
خلاصه:این سایت برای تمام آموزش
#امنیت
ساخت
#کانفیگ
و تمام روش هایی که شما رو میتونه با کمترین هزینه و رایگان وصل کنه رو گذاشته.
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4568" target="_blank">📅 13:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4567">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">اطلاعیه:
سطح پهنای باند و کیفیت اتصال اینترنت در تمامی اپراتورها و دیتاسنترها به‌طور قابل‌توجهی کاهش یافته است. بررسی‌ها نشان می‌دهد ظرفیت پهنای باند نسبت به روز گذشته کاهش محسوسی داشته است.
همچنین برخی رسانه‌ها از اختلال یا قطعی در خطوط انتقال پهنای باند و زیرساخت شبکه در برخی مناطق کشور، به دلیل حملات منتسب به آمریکا، خبر داده‌اند. :))</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/4567" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4566">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آپلود عملا مرده</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/4566" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4565">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oNAqlW2FMnC9tjQIVFN6PutXohC6tHttWCiDUBBKrKywg_oX5GpQn1R4EPwS0k7yggcP5oLjjCRUI0J3RRZl6spaAngbDHh58Couj1GZwWdxrg-yEk1gPY2OAJQ7hL1ZgGMwQWhA5alb4MNreKbR6pZ7xLXaIxX96VOUNT4QAfA9njVWZXuo8pHQR1roj01qPgNBquLhTY3TdZcp2eqRQkmzMCBt3AidcSh5DpvBcA4Ezz9BQwDG88Q3RsLDfjBWuGO6SkRoj3IYujPip3qcgUTw2HG-IJMZOSqazl5PFCfuUP1yrh-eLpPVurZr4Ry9oZwjMLgQQQ3h9g2og9M2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کپچایی بود خدایی حالم بد شد
کم کم ما ربات تشخیص داده میشیم،‌هوش مصنوعی انسان</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/4565" target="_blank">📅 22:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4564">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d80c0238b.webm?token=JBcRBurIBimPfQHPKeJETSBFiEIIJzIRop1eNRRywRXhmMBm4rKh1vJaz0d0yrEJlz2BGQzJ8irJS2s40muwQ16D9KaQaNN8fR2gAAOt4-I7XTh0sFS39vup724QRbHS6907fx-E4APulHMxRpfCqzIjXWQNJdeKfGvlaNxSP8RsyUNf9VsN5c-aGiX3PXT8tjdTJ1X0hXRlXCTuSdKfM71VeblGlc-ItyQAweWxxrgcrRVIMKQ8cO1GnnpQ81QHwZZ9IjBPR5cNRKyoRg97-iANq3MWWBHGConCm98YkIiyGpAH4OtlcjyGASwLmfbIg591f9fwi6EyTnjj60XXOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d80c0238b.webm?token=JBcRBurIBimPfQHPKeJETSBFiEIIJzIRop1eNRRywRXhmMBm4rKh1vJaz0d0yrEJlz2BGQzJ8irJS2s40muwQ16D9KaQaNN8fR2gAAOt4-I7XTh0sFS39vup724QRbHS6907fx-E4APulHMxRpfCqzIjXWQNJdeKfGvlaNxSP8RsyUNf9VsN5c-aGiX3PXT8tjdTJ1X0hXRlXCTuSdKfM71VeblGlc-ItyQAweWxxrgcrRVIMKQ8cO1GnnpQ81QHwZZ9IjBPR5cNRKyoRg97-iANq3MWWBHGConCm98YkIiyGpAH4OtlcjyGASwLmfbIg591f9fwi6EyTnjj60XXOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز : ترامپ از کشته شدن سربازانش بسیار عصبانی و خمشگین شده است.</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/4564" target="_blank">📅 22:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4563">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سرعت نت من به شدت پایین اومده. از 30 مگابیت به 2 مگابیت عملا. با و بدون وی پی ان هم فرقی نمیکنه
نمیدونم چه گندی دارن می‌زنن باز</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/4563" target="_blank">📅 21:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4562">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رفقا یکی از دوستان من به اسم محمد، خارج از کشور هستش و برنامه‌نویس Back-end با بیش از ۵ سال سابقه کار هستش و روی پروژه‌های مختلفی از جمله سیستم‌های رزرو پرواز، پلتفرم VOD، مارکت‌پلیس، سیستم‌های پرداخت، احراز هویت، پنل‌های مدیریتی و معماری میکروسرویس کار کرده.
تکنولوژی‌هایی که بهشون مسلط هست:
Node.js • TypeScript • PostgreSQL • Redis • Docker • RabbitMQ • Microservices • Prisma • REST API
هم برای همکاری Remote میتونه اقدام کنه، و هم اگر فرصت مناسبی باشه، برای Relocation مشکلی نداره
حیفه که از چنین استعدادی استفاده نشه
😁
لینکدینش:
https://www.linkedin.com/in/mr-ln
آیدی تلگرامش:
@MRLN2001</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/4562" target="_blank">📅 20:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4561">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این وسط مدل Claude Fable 5 موندگار شد.
آنتروپیک اعلام کرده که از ۲۰ جولای، مدل Claude Fable 5 رو توی همه‌ی پلن‌های Max و Team Premium (با ۵۰ درصد محدودیت‌ها) نگه می‌داره. کاربرای Pro و Team Standard هم می‌تونن با استفاده از Credit بهش دسترسی داشته باشن و یک اعتبار ۱۰۰ دلاری هم دریافت می‌کنن. به نظر میاد فشار رقابت سنگین با GPT-5.6 Sol و Kimi 3 باعث شده آنتروپیک از برنامه‌ی قبلیش برای حذف کردن Fable 5 از پلن‌های اشتراکی عقب‌نشینی کنه که خب قابل پیش‌بینی بود
🤤</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/4561" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
