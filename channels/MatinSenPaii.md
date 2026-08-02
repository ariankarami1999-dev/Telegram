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
<img src="https://cdn1.telesco.pe/file/OxDPUcMSmTTLcOt5imCqkFuaGLqSJvTeNceyiMHcB-Akl3d4IVzqDkv8zHGp0EntmTKPdM_Qoabh1ewt1-YyEpicymbWQGkHY3SVgd3bBwvy1568DhegRZha6iMOC7mmM8TNEV_XoMAwWOBHgeTANnxrst9uofOgOlqRwLEbDquMfVuEaNHeHMigHYTEQNYJh_DOZyEjBca1GlpTD_RnArKGUxl1FYoMM3um_a57jc4w4UFh-N3T2QFV1B82LNl6P8U-hqDwEiUwAoQLS5-15n39adL6oR9IYNhpEBWLKWCgpAPujJtAtWbq3fE2jSYCG_2jQZ6V8nWjlH-LjlQZ5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 157K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 17:53:49</div>
<hr>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sotp-WPK5w-f-THlA1_FqBc549mimnm5_S_bGz9thnNPnHU-PjesVIf_WK25_u8IgUAB5jmNP7UpqpgtbQ0ZaqmZlTRl9wCzwV1K2VAB0knULvtuVWPVcRlCjG98FMUTyN6sn0jeGhGkc4r5wMHKCl7H2PxULMNJjc1wlOPoj-ELfxCK7D03whFqTRmapxTbY5MV1djqXAuAWV8KztpmTv9xVFPchAAJR7NCZCw3J5TykbtaShhhUOgUAUOYLpzw76vf5xOtNMrJjOvu3ktnjOIcJC442IJcxa8ANJ6wYtiOR6qs0vNxoDEJvUbzE0PP9cib6etcq6m-Jym3_J_uZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود
مخصوصا راجب این Demo های وان شات
https://www.youtube.com/watch?v=LmXU6SEH3Ks
جمله‌ی کلیدیش این بود:
The Demo is cool, but not actually a game
این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم رو داشته باشید که می‌تونید همین الان(حتی با یه اشتراک 200 دلاری کلاد)، بازی بسازید بدون هیچ دانشی!
طبیعتا کار رو خیلی سریعتر می‌کنه، اما باید مراقب این باشید که ai، لااقل هنوز به این درجه نرسیده(و به نظر من امکانش هست که هیچوقت به این درجه نرسه که دانش پایه حذف بشه از این چرخه) و خلاصه، یادگیری رو متوقف نکنید. حالا توی هر حوزه‌ای که هستید
نه جزو اون دسته‌ای باشید که میگه ai به درد نمی‌خوره و Anti-AI هستن،
نه جزو اون دسته‌ای باشید که ai تبدیل به بُت‌شون شده و می‌پرستنش!</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qcd1u4_Ezr2zQuwzQv6m9tkyOKhCfs_dBeNrNgfLYCZvIalaKSywM8dHFw-NOv6WmR8g4BCbrtTnMXlec6eM6u11ILpM58UKvUEPTvorYmAGgZmWoxU3OsMJkiWY6QoGBTxGpVMenj0rf6b0ah90Py8GJfaiC9H56FVOjsfM_Q2GNGrJbeuqrWS84fDnnwh-oQNc-2PAoPp8JV5-lOH1Ct9AUAvTzsKpTPpR1_Gh7_i8kp_H5U4v5G7Q3jKonc0vH-Q5Tn0tBLY1IcRH-TdVv48oVN7V96DiZOvpKakvmpSSCicIEYFu0Rw8Uhxq4cRaTLKMgEDL5LCoIVxa2gHH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی:
https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو:
1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت زدم رو بهتون نشون میدم
2- کلاد رو نصب میکنیم روی سیستم و به روش استفاده‌ی رایگان ازش رو یاد میگیریم
3- با استفاده از 9Router، بهش Mimo رایگان شیائومی رو وصل میکنیم و استفاده می‌کنیم ازش توی Claude Code
4- با استفاده از API از Kimi3(مدل قدرتمند Moonshot که توی بنچمارک‌های فرانت‌اند در حد Fable5 قدرتمند ظاهر شده بود) هم استفاده می‌کنیم
5- با Hermes+Mimo و با Claude+Mimo و با Claude+Kimi، و با یه پرامپت یکسان، یه بازی سه‌بعدی می‌سازیم و خروجی رو مقایسه می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i-nG6oSbwPny1Bk5N16TO9O4n2krioT476tlLNm1RXXTzEcW1sSv_JJuF-UV-rvrD8gKrgle-MvgGYrohuxCbwZmTirw3QIUdx-L-k-vH06CkOwKJ5UW3apdJyLtJj7g4IiBf9lodnl7_fa3SJd_Lz63IxN0OkQrK9u3EhupOj9zDhQzJWVC4V3YW9jyq2dH1XaGPajVwPfTBfNK9UqhEEccuLjQAC7C-47lalScof3-0M-6eSNIjvWCOys4rBru0sJTCBhRlekadSYRJmLKzZAipKIl4YEA2c70l_8LwvWrTE78KHbRYqCn9FHhSa834ZoKEYkbfAm6HO9xP2TNgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">(با کلاد رایگان زدیمش ولی)</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4764" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BiKAjCZOaf7_Vvyg0-TMUntAB5prBq1B2mARyyqlh6J9plnMrr5gyFTG44nEGDLsCHfoPUDW_Wslr532IYBB_T_AGGAxwgZr7rmrQrdX1HRKqGlD2zcERpYHjYnloqNeLZQO7ixB7MQubsBuAW0f0YJXEU9sLWN51qhYSrO82bWJlAKcPlhSUVS2iAUUL3hAFqDAoBy0rtZE3owLSavrx2iv4bGQRbcc1_5FFpYkT0VpB62GgPRC2HlZp6Of3jiXelS-6L1NBOmGRTvvXZr6V1QH5Z7avuguY89kjHkHha8QEeTBIQiYof4uNLYAudESu7TBWq1qBMyJMHJlrwtj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4763" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4762">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4762" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fhEM80BOXBT9eHCCB8DqVrr81o5EbQJfTkso8f-9zS5C-SOkHZxeL4hGd14KYwpibkc91OC0dmSEL6UQDZcieEFHMOExmTPrQGh83ozHAxspbgGTpoKFz3npisuGFMn69wMoH7ud4Fg7DzjKBeJ8OGbMS38C_5yuoQuo6vsglGWSqzzOXMVMwZ8CvjiSzgJctZzGSmKqFw3nDA6OeI9Tig6sY1CjBUcpbyQiD7ftXCFka9wvF-GSg01yx8LrMgJi9-PrIEFKbd8LF-KJ9eoIEe0C7M6lKrL5XeujeQKwxSZYFzK6ODNdHK_u1xs1dL9LP6y4Se9IX3pRx0d_UKE9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4761" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RWPix8TCNs8-RfDm0GsLCnXF_f5U_mOrr8JwON67cxTIgQ1wfPFh_aOjzFAq9sVnHBDX1TwVxYa6AOpwxFI7vb8RwohBbHon_Dy6E_dVKA5ZJAvBQI0CjhOA_2q5-K5rZQlGh8Tbo8zAE97yJkHMwzTPgphp64AJeQSaFGXAmtpXtJE2mTMp7-0vscYqtEvP4CyGGkcrOqjKZ_NFp5hpr3WDAgyAFuzoHIQaIhVQUmvzKpgPTusPlG6TGYkD3Hu0cZ1P-2TQpGq5vS185me3BzQl4pLDD7-oekuJeHstn3Y_R5S88xgmyjtO2ZwIQWKJwsCsPnNYXnRKvdVXZ3tBRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پرامپت دادم به هرمس که تمام اتصالات سی پی یو لپ تاپم رو داره میسوزونه</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4760" target="_blank">📅 18:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ppCfAcaA35vua9fdnaeE0sCTFFpOGPlmy38ZgzrzNOwYs4l1oTZsQ7ZktHXAPboLaJ4UE10x_n7BtCvUgKXEYEdk65FCiYTA1tiWm0NHI7nKr5ph8JEd5TjSbIT6CPaWftXNLRf7M-dZorU4EvI1LQRCcVxWrkwkDkhajtPMFVuEldo995hOwP_gKZaYRsO3MieQ3GI6HMBAyma6Drodf0eSW8j_4zAKZquDmQDUWZUwAdvMpDhN5Ce4hPBrbGTgiaFbYRxJpH8vT-PmDyZGX53tI8WZMR_l4T8LZozDU1d35C14tl2-ZT8Z--_bdf-VVSaCv8McAlsCVNo6gzu64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!   هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده. منم یه مشارکت کوچولویی روی خود هسته…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4759" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4758">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">و روی یه سری قابلیت خیلی عالی برای SenPai Scanner دارم کار میکنم که به زودی ریلیز میشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4758" target="_blank">📅 17:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4757">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ehMoTvvSSTlUi02F91qpH-2RJzMV4gR9m8OeNL-Ir4InW3rZoXXBLISNk1i4F8nTm3g3ztHD_siN2HanizbR0YKz0eoQgBFvRJQcBJ_92GudP3PwyP0iSTaewQdhBTe_g6uoBrRuSMWwX8aN27ne72ERCI6PkuhPD8ZRtWv8i9IHwg11rLZOo5QXSpMwwltD-Tr6kWHAXTH9mkUrdFSYES-dwZgcAm9GuXheH3pye1Bd0dnltFUZ0tt0vkKbDdUKyHiiqEid_rbAkGW5TjFUHcfjDwPPXD8a9c6pT8w-MDWPp0eeaL0RWiYDROOfVSwjOFTMRPjhQtMmsA6LVEebpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن جدید Aether GUI هم به زودی آپلود میشه روی گیتهاب</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4757" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Aksoy</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=Sp0TEYwSPB5WWDlfha-gSbp-IVbQmALe8yHehldCydLav6w3S9HzvgYlYYJr6wWEPl5sfJ7nJPkvFw5w06ftlz0Zakvz6NDhe7hVghVE6xf3cmPn-nEVzr1ipujzSUnmMwVWgBo2wJAzjuzy_D2NDV_5fhDaf-7qIo25rxpY_lhNCz3ZmPTzr_kuTZva4KIb1sjqnufu6qAsBw1aMrYq1dwANvPdSRP-qfEDq2lfGcVtZHm56lEYmOryagFXgvJP7-Z9ZrMFRyjdJejOnBj90XxW_wsS4F_uRynfTKhfzoGI7Z7C5ICanI4c31vqZyOPamO5bIRNU6L_DPOaQ9rerg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=Sp0TEYwSPB5WWDlfha-gSbp-IVbQmALe8yHehldCydLav6w3S9HzvgYlYYJr6wWEPl5sfJ7nJPkvFw5w06ftlz0Zakvz6NDhe7hVghVE6xf3cmPn-nEVzr1ipujzSUnmMwVWgBo2wJAzjuzy_D2NDV_5fhDaf-7qIo25rxpY_lhNCz3ZmPTzr_kuTZva4KIb1sjqnufu6qAsBw1aMrYq1dwANvPdSRP-qfEDq2lfGcVtZHm56lEYmOryagFXgvJP7-Z9ZrMFRyjdJejOnBj90XxW_wsS4F_uRynfTKhfzoGI7Z7C5ICanI4c31vqZyOPamO5bIRNU6L_DPOaQ9rerg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر با QR Code یه سیستم جالب برای انتقال فایل از یه گوشی به گوشی دیگه ساخته.
فایل رو به تعداد زیادی QR Code تبدیل می‌کنه که با سرعت پشت سر هم نمایش داده می‌شن و گوشی دوم با دوربین اون‌ها رو می‌خونه و دوباره فایل رو می‌سازه.
بدون نیاز به اینکه دو گوشی روی یک شبکه باشن
https://github.com/bashalarmistalt/decimen-optical-transfer/</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4756" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مصرف GPT خیلی خوب شده الان که تست کردم
گویا از خود GPT-5.6-Sol استفاده کردن که مصرف هزینه‌ها رو کاهش بدن
😂
شرکت OpenAI امروز قیمت GPT-5.6 رو به شکل چشمگیری کاهش داد: مدل Luna حدود ۸۰٪ ارزان‌تر شده و Terra هم ۲۰٪ تخفیف خورده. نکته جالب اینه که خود مدل 5.6 Sol (قدرتمندترین نسخه) برای بهینه‌سازی load balancing و حتی بهینه‌سازی forward pass مدل‌های کوچک‌تر استفاده شده — یعنی یک مدل هوش مصنوعی داره مدل‌های دیگه رو بهینه‌تر می‌کنه.
این هم خبرش بود</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4755" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4754" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4753" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetBlocks</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGk12wwVuIwldeYmkU5pBgBS4KVWyWjdBQtNMYmYqm1dYO1a4xVFP48mx6KisyJm05X2-GvPAnEUAkXBzOqFb1eo9_v15NyVPQKkqKbk7QyIBwge324E6cYYBPmRBbRxJkBZWG36RU4aSRYRhdysbpuWZqRWg8NXr4EZUn8DuwwFRIrrlYNhO6Pj83vlU582H3wp0ecjCHhiVy3t7ldkUhbjF75Bkln4PSzt7uPIJN3j8RsnWQmNRRXX9UqqDLGjoFJ2ndVsFcZjQRkM0WYTZLGMWnkwl_n0e_bqxajAwCw1kvDAB8YbbfJZiecKXp-5Zk45djOl_w3-5CwEqK1D1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in
#Turkey
is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4752" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=dBffmIZBLT6mHkO9T51Gx1tTvx0bWbnnhngO3ezwxqBzyBrzhAm0-7dr1BjuQAbmX1Qpki9szEOj2DcdNolM5ESAAcCHUBvqNeklvPHIv3hF7c4b7_o3OenreeADF_xqsHDO5dxUN1S3TH7gPBQux7tOy01ZXQf0iUy0zJO41g9ZZGiHFNzDXUtu3jY6-AmBedPw5HA7vKJRmokQVvN0plxl5O09ndQEm8P7v9N5-DiQ-YotbZ_LiY_rVnBZi8xNDqu7vu_AC9HlJnTbSpjVaKVG7NXPTgJeBNNV50b9LqemU-a5-X7_lNOn4VfrOndieTipHYBppAG88cgybh-vJYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=dBffmIZBLT6mHkO9T51Gx1tTvx0bWbnnhngO3ezwxqBzyBrzhAm0-7dr1BjuQAbmX1Qpki9szEOj2DcdNolM5ESAAcCHUBvqNeklvPHIv3hF7c4b7_o3OenreeADF_xqsHDO5dxUN1S3TH7gPBQux7tOy01ZXQf0iUy0zJO41g9ZZGiHFNzDXUtu3jY6-AmBedPw5HA7vKJRmokQVvN0plxl5O09ndQEm8P7v9N5-DiQ-YotbZ_LiY_rVnBZi8xNDqu7vu_AC9HlJnTbSpjVaKVG7NXPTgJeBNNV50b9LqemU-a5-X7_lNOn4VfrOndieTipHYBppAG88cgybh-vJYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4751" target="_blank">📅 13:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">طبق گزارش Science، استارتاپ‌های لبه‌تکنولوژی مثل OpenAI و Anthropic دیگه مثل گذشته دستاوردهای تحقیقاتی خودشون رو در قالب مقالات علمی منتشر نمی‌کنند. این موضوع که به خاطر رقابت تجاری و نگرانی‌های ایمنی پیش اومده، باعث شده تا روند پیشرفت علم در آکادمی‌ها و به اشتراک‌گذاری دانش توی حوزه AI به شدت کند و محدود بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4750" target="_blank">📅 07:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یادش بخیر، یک زمان اروپایی‌ها فکر می‌کردن مهاجرین غیرقانونی قراره بیان و با گذر زمان در جوامعشون integrate بشن
🥀</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4749" target="_blank">📅 03:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4748">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چیز بامزه‌ای شد Mimo 2.5 free + Claude Code و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4748" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4747">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=kd6A8gRPK42CQ_wK0elR5Xl2JaFumnZ5CYw0jFCq0gjjMI-5wS01J9XXRxncjPLt_V1RITUxJhltj0i320u-wwx1ACcKF3NClPNmHv-oqS17sQOIrDKKNYQTZ3kB3a2RpB5wI3yAUd90WzrapSVoAHsfVI8YsLnWSxhlbd00meBGKgY2rviIS01of7FVvBwbUfg6gKZO_au24sZ44XhD3KTTXhJSaFHwI_MhCAOICy_M8pnn5Q1Pv0Q4sIWLG0ITFqLW4qv3mtD3TvXYYC0s9cmyBTO28R798nr5AsB3c8vtMJhDQ69uSIb2xkJlDLl6k2HjrZmiid8D9yFbSFGsWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=kd6A8gRPK42CQ_wK0elR5Xl2JaFumnZ5CYw0jFCq0gjjMI-5wS01J9XXRxncjPLt_V1RITUxJhltj0i320u-wwx1ACcKF3NClPNmHv-oqS17sQOIrDKKNYQTZ3kB3a2RpB5wI3yAUd90WzrapSVoAHsfVI8YsLnWSxhlbd00meBGKgY2rviIS01of7FVvBwbUfg6gKZO_au24sZ44XhD3KTTXhJSaFHwI_MhCAOICy_M8pnn5Q1Pv0Q4sIWLG0ITFqLW4qv3mtD3TvXYYC0s9cmyBTO28R798nr5AsB3c8vtMJhDQ69uSIb2xkJlDLl6k2HjrZmiid8D9yFbSFGsWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیز بامزه‌ای شد
Mimo 2.5 free + Claude Code
و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4747" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4746">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IWXmphfmDVsTzl-lnRs5tsBKE8-dwm1zC-ISicOji0t-jDGX0jJriF8GQLG-OagvzVyuHAd-kvifs6QTXQ7IMbMpQQs3f0PB1NHjNhwYgfM5QoAuxpCEAc2MYpAZQJKbbXVH6VEZqXIBqjNjio7Jgmy_MSIehYyYZajMfzW5AxIv-eYNvChpdjwk-59EiEgjoiAyOMvU_1GAAVtaJPPrwgTzDSMxYNV4_KqeW3-mVFUtgq_AcbBUVfZB6NCHi27E-LFwE-YlhCAeb3FIk1z0vuQ0hmK7uYIQ2fLL_hLEEp7V9sHy-x0z93WAohEJKmxdTHxCFYjUuqESIQytl2fK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پلنی نوشت برام که اصلا GOD Tier</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4746" target="_blank">📅 00:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4743">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v9ONzHR23uXZYYYJyL9bNSxhat6ly4QIDCu1docabFZsqk0Jg_3SJ8V2EglnvVof9dVoLWf5RzTNujvM08mZ5X3MSCZ0sNHoIjbdfka4Wz-do9bouezGyhp_Jum7yU2D6P-qtGvbDWfak49CAVPU-SPP_0ppulY7zihqZydsNy6bhTlzHuX0dRK4smGuRwucC3RdWI_zF-z-n1GmIAUrAAbRkEEFkKXJVbRGjbPZFB3RSw62fuyvBtatwRCMM_sr-DrEFr8l6ccEz06Dvl31LqSLIQNOEWBdexxk7IDG-vTTkSZWRP0oO8KojsQZgOYjif2tOpozWeW8KxT0V7PidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای گول زدنش به طریق‌های مختلف هم یه کارایی قراره بکنیم</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4743" target="_blank">📅 00:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4742">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به زودی ویدئو داریم ازش
هم اپ دسکتاپ Claude
هم Claude Code
و هم Claude Code CLI</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4742" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4741">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">توی opencode همچنان کار میکنه mimo
با با ratelimit سختگیرانه‌تر</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4741" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4740">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i_vQmafJECfaOupeIEjK2M67sDOhi4mGeFnYrvhhatA0z4g-mFLZZarXSusVwXexgCASZNrbfLKMWGjdLrjFBFMS4Snc8tB7kgCapk6OYQvwK74-wDSBVIyE1WodNcA6uOyedF9gTUBixyHHmwy6GykpfkZaf5euo3XacxzLvsNfr29OZ_YFoL6TrDGUJvb_QANzQ652XM_5R8KdRytun9xwDaWaJyjyg79o86qazaVPbZtWUIDCXfRa9ODUM3uaaCkQVOCjzL5MFaNyWUI6lU-4AZVAGc0Y1j0Os42cNvv07RixeY8sozXM0MyeyRUpQw2yLQqAZhqC2cgORe5aBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون سقوط سهام آنتروپیک
😂
😂
استفاده از mimo چینی در Claude آمریکایی</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4740" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4739">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4739" target="_blank">📅 15:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4738">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4738" target="_blank">📅 09:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4737">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4737" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">روسیه دیگه دید زورش به اوکراین نمیرسه، گیر داد به پاول</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4736" target="_blank">📅 23:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4735">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𝗂𝖼𝖾(𝜶))</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez_zpnD4w5xAaNq1Y6staiK3UztlxSqhFxOlNfsmPLGRjX55LAEjZpL9mOQFdxKj8VWXRz6fmKLy6nLZc1u03mmuyc8kraIfkRAolGke18lok1BAXcdmJN3_gB1-JMYze5-1KyPlnuHqP2X3rEaehGIrwDY-RXsPWHosqobAQr_IgR6C38qqHMxQBYL4exJVGiew1ZeIlax_khd5MV9ex55xxCMXpTXpXlO4evaC7ElwVkGzmzzFP8nWF-FWSvgWT_rGN-5dqVCORs8PQw6XHC27sAouEGE48YucrX8gDwgD9KIrleToGXP5b_IzF8KRXdorEuSE4Ns8DQiXEahyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری | روسیه پاول دوروف را تحت پیگرد قرار داد
💸
بر اساس گزارش رسانه‌های بین‌المللی،
سازمان امنیت فدرال روسیه (FSB)
علیه
پاول دوروف
، بنیان‌گذار و مدیرعامل تلگرام، به اتهام
«تسهیل فعالیت‌های تروریستی»
اعلام جرم کرده و نام او را در
فهرست افراد تحت تعقیب بین‌المللی
قرار داده است.
💸
این اقدام می‌تواند پیامدهای حقوقی و سیاسی قابل‌توجهی برای
تلگرام و فعالیت‌ جهانی این پیام‌رسان
به همراه داشته باشد.
💸
بر اساس ادعای مقام‌های روسی، تلگرام اقدام کافی برای حذف
کانال‌ها، چت‌ها و ربات‌هایی
که به گفته این نهاد توسط
سرویس‌های ویژه اوکراین و گروه‌های تروریستی و افراطی
برای هماهنگی اقدامات خرابکارانه، تروریستی و جرایم سایبری استفاده می‌شدند، انجام نداده است.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4735" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-_Im9Bs-bKNhpHhwxFCCdm8_aJtL4cduVUNBmdKEEYhpzP2seC9oBKqRDZEU4H09JbWtuEQVAJkxslNrQhtpuco200mHg1SInqjkTqt1hlA1eI5SnSS45nFn5aqqVJqNhYcmLXONrnAAcgoY34ykP_aLtucsUtqA7aOQ3KyFaNsFn4NakFoZpTein1Wut7UqDD1zT8y7QTpJmB6lVqpuGaGtaHEc9KlylRL16NmmienZ66g4msgD-VPaouChpHphT3L-KMV8a2CXYCyiqSov0gcJMjaDhLJj3NNgU-JkGiRRNofvCe2b5WEJz1Pgtg8in7TNrL2i80aj4SViJoxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم این کار خیلی قشنگیه که هم برای حمایت از پروژه‌های اوپن سورس و هم برای تبلیغ کسب و کارتون، می‌تونید انجام بدید</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4734" target="_blank">📅 23:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4733">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether:
https://github.com/CluvexStudio/Aether/releases/tag/v1.5.0
\\\\\\
بزرگ‌ترین آپدیت تا الان رو دادم دو تا قابلیت جدید و یه سری فیکس امنیتی. توصیه میکنم حتما آپدیتش کنید مهمه و خیلی بهترش کردم و بشدت بهینه شده و شانس وصل شدنتون هم روی شبکه های پر اختلال هم بیشتر شده:
- پشتیبانی از Zero Trust (وارپ سازمانی) "وارپ پلاس"
قبلا Aether همیشه به عنوان یه دستگاه معمولی وصل میشد. الان اگه اکانت Zero Trust دارید میتونید با همون وصل شید. هم روی مسک هم وایرگارد کار میکنه.
(پلن رایگان داره کلی فیچر اضافه بهتون میده نیازش داشتید میتونید بگیرید و وارپ از حالت معمولیش میشه پلاس ولی بیشتر برای Enterprise ها هست چون Egress Policy داره میشه لوکیشن خروجی تنظیم کرد)
موقع اجرا گزینه ۴ رو میزنید
نام تیمتون و ایمیلتون رو میدید یه کد براتون ایمیل میشه وارد میکنید و لاگین میشید.
توی داشبورد کلودفلر Zero Trust نیازه ستاپ کنید..
\\\\\\
قواعد مسیریابی مثل Xray اضافه کردم:
یکی برای بلاک کردن کامل یکی برای اینکه از اینترنت خودتون بره و تونل رو دور بزنه (مثلا برای اپ بانکی یا سایت‌های داخلی که آی‌پی خارج رو قبول نمیکنن) لیست بلند رو هم میتونید از فایل بدید.
\\\\\\
فیکس باگ گول که بی‌صدا قطع میشد. این رو یکی از دوستان گزارش داد (issue #65)
\\\\\\
قطعی‌ های کوچیک شبکه دیگه کل تونل وایرگارد رو نمیبندن...
مصرف رم روی سشن های طولانی با قطعی زیاد فیکس شد.
-----
ترتیب اسکن رنج آی‌پی‌ هم فیکس شد الان طبق داکیومنت کلودفلر اسکن میکنه...
\\\\\\
روی شبکه‌هایی که سرور ثبت‌نام کلودفلر رو بسته بودن
به دلیل فلگ شدن آی‌پی یا هر دلیلی... کاربر اصلا نمیتونست وصل شه.
الان یه راه جایگزین داره...
کلی فیکس و آسیب پذیری هم رفع شده اینجا جاش نبود بگم...
ممنون از همه کسایی که issue دادن و گزارش کردن :))
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4733" target="_blank">📅 23:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4732">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4732" target="_blank">📅 22:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4731">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tl48d5F5xQlaHusodUklvSsy32xIioAlBoToWrlO4TE2mn_fSzJRej1ykfvEH4D76KzHT-4efXUa5ZYSdYB4UbqeZZV2_A5w7G2b4bZxa3tGDlu8lI8z4Q_CWBNk3_kDU28_1sDfgwHIRiTDjGmyNXzfrXX5F1kAVMFpEVBszZQJbq0IPE887tUxluJ5ixrn3rwDmnLreATbD07s-xGIfkrUrxuyaE0fsulIFBS7eCnQV2AJObRcFRba5bcshXRs2vUWeTwFweGtD55oFAFWaX6QGbz8PV9wDhIpZLeGFch6ObEQzNhV3XckoAVdcPfmCEfNAH5kbb-XCVXroW2erA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین دسکتاپ لینوکسی که کامل توسط AI نوشته شده!
یه پروژه به اسم Starling منتشر شده که ادعا می‌کنه اولین دسکتاپ لینوکسیه که از صفر تا صد توسط هوش مصنوعی نوشته شده. این نشون می‌ده که توانایی AI توی کدنویسی و توسعه نرم‌افزار به سطح کاملاً جدیدی رسیده:
https://starling.build
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4731" target="_blank">📅 19:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4730">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=RF-e6KSstIIs1mS2ljjTDGWL0YwiJTLkSogbPBjMEG72kDfHhhjRdiwN5mc5ownMOA9x4Jv5M-N3Ud57O1Ab3pNsJQv0XHl-pAU6z9McrDpUbI08p-9TpfPQ6ybL9u8v3y6coa9NACoFOWkqYILBSRU8Wld09ObIFenuQZGO1hknP99YJwG_em8IUBLMdvaFW16QluiSFM9jjeTXpsBF88BUVrMmPnDZkhB4NBBCSycZNBzAZgHwKFpb1cNj6QaJMlIgnvp9jkx3FlpvGnvJ3T5_Wavd0hSaDL1nOBjie8wdACWMRlKPPhpxq44obdiNZdpTJx7k8HjSsIoYf4zr7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=RF-e6KSstIIs1mS2ljjTDGWL0YwiJTLkSogbPBjMEG72kDfHhhjRdiwN5mc5ownMOA9x4Jv5M-N3Ud57O1Ab3pNsJQv0XHl-pAU6z9McrDpUbI08p-9TpfPQ6ybL9u8v3y6coa9NACoFOWkqYILBSRU8Wld09ObIFenuQZGO1hknP99YJwG_em8IUBLMdvaFW16QluiSFM9jjeTXpsBF88BUVrMmPnDZkhB4NBBCSycZNBzAZgHwKFpb1cNj6QaJMlIgnvp9jkx3FlpvGnvJ3T5_Wavd0hSaDL1nOBjie8wdACWMRlKPPhpxq44obdiNZdpTJx7k8HjSsIoYf4zr7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4730" target="_blank">📅 06:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4729">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چقد جمعمون همه پولیسیم
خوشم اومد</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4729" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4728">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/giOq6Z9E6qIvopVyq_Xe5FxfzwErEcv5zSl5mbnCVB9TbARK_Wvgwsm-B5F8WoK31ttIUyiPRas22h3PjkILNfm0Yxu0ewvi3DhGTzvgIfkM4NqjCpiP6wsjq_rMc1qChut7oYl6Y2FQoM3HdbuuQZbJVO0QRazuaAQcwtYWnK8Jn9uzivJ7Xkagr5CNB_e3BNgJl74oK3ivk1okGPNOuAlnjoxeVa6NhWBCOAAJUxuc6S5CAIkyyCBup_z5LDynfExzEF32pyXGj7UDPOFCx_Li3q7_DtX7D9C2UnTgu3N5DygRVtgyMbxqg3W1dLzCR5OiTndijf3nYYox4i8tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا بیست روز پیش هم این اتفاق افتاده بود</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4728" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4727">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pljy-BqtqHWwCBPZDCvodRFMcMRKbqNq_dNajOLr4VPi_ChffJBkgOT6RPbUTqwNh49_73FvmWNb-3erZXbAsdi2Ijtd-P7lTeRxU0hEmE9d4Yxs8nmgs_tNgmBVDeBNSL86pNo9dnWbb_hNyZ-7Zq9qFbBZ_fQ5XD9Ux2RsWC7hBayWkavJLabmxsCA2lhwb0A8ptcuojOW4uOlzTgy7eezlpSCqMZWRmg41Xg1YCV3oLop1rF9rI69zgLOzP78TDL-zM-lLEEZVy9GNcC3QyU2L3dKocSqejDnLY-9fr-rospbBNc7mvTJTbbkd1j8ryr9ruudAN6N1RVHANJ-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و... همه یا مال یک نفرن؛ یا از یک زیرساخت استفاده می‌کنن. یکیشون اگه خاموش باشه برای چند دقیقه اگه همزمان به چندتای دیگشون هم پیام بدید…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4727" target="_blank">📅 06:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4726">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دیشب گویا روی نت هم یه گندهایی زدن
زیاد شنیدم از بچه‌ها که ۵-۳۰ دقیقه نت قطع یا به زور وصل بوده روی اپراتورهای مختلف</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4726" target="_blank">📅 06:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4725">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و...
همه یا مال یک نفرن؛
یا از یک زیرساخت استفاده می‌کنن.
یکیشون اگه خاموش باشه برای چند دقیقه
اگه همزمان به چندتای دیگشون هم پیام بدید
می‌بینید خاموشن:)
ماشالا به هوش کسی که پشت ایناست</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4725" target="_blank">📅 06:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4724">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K2TI4OuikwKMi4jWASYX0uvrVRY3DDOb6H9Nfzxsxd6CZABt46sSzSe0IF0ym0dQRTn5FtSq-7TMjIdAxX1XxB0hoov6tNMC8L7HRM-rIgWuBnIAaqFCo8Y7F_C3Z-AfbY8uQhJZq8q3xpuwnHK_Dd62LrfN6flJzqjzacdddaCM4qZmcDpy459ZiXT-eSm95CTgELkjk0RDThQjPbhSBMwU9Q_jeR071CPoV9f7GPoV-sY0WIXovv4vfwuzCy3BhblPXuNYhTTBeiYLop1XSgVhiUt5ju1RKLv6WN8-WoCMctx3-VjGASLvUjMoVSOaGT7ewDlQAaBIJQ17tWHKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیشب به شدت این اپلیکیشن رو توی کانال‌های تلگرامی مختلفی دارم میبینم که گذاشته میشه به عنوان توییتر.
از هر کانالی که داره نشر میده تقاضا می‌کنم که نشر ندید و لینک گوگل پلی بدید.
به خدا گوگل پلی نه فیلتره نه چیزی.
نشر دادن این apk ها توی این شرایط یا از حماقته واقعا، یا از ندونستنِ مردم سؤاستفاده کردن.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4724" target="_blank">📅 23:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4723">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kbpcKGZOtQPaQWbe3HPM1_uiZzGtImzUov-JMicK82ZgScNJxuVNCScWvucD65XXQeOifXGtL_422bll4KyYKPeRWyOg2mTIWFu9R8UZ_29H5A05neDNkGSzTvvsqJBsdQHDegnGUWNgiTXGYaKKH2O7FFiUBQmX5aF1BdrjsBaS0P9Yc58ySPsQDxJwa_xv7rSyUB8AyJV9n6BmXHZNDiy_U_7LIJeWmTeLreO-cam8M5UfBSYk3D01Whl1Wb1TKzZ7yCoI9DOOLxDBtqsrGJ3_9KdlK8uWku5DR5DF7LaDc9l6YbESp0DmG9ZvtS0ICBHtQXONlEiW74OOM8FKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Moonshot AI بالاخره مدل Kimi K3 رو اوپن‌سورس کرد و همون روز اول Telnyx بردش رو Inference API خودش. مدلش خیلی گنده‌ست (2.8T) و برای ران کردنش زیرساخت خفنی می‌خواد، به قول یکی از بچه‌ها در حد نیم میلیون دلار. ولی چون تلنیکس GPUهای خودشو داره ادعا کرده که سرعت و تاخیر رو خیلی خوب کنترل می‌کنه.
قیمتش هم فعلا در حد Sonnet 5 هست تقریبا، با قدرتی که میگن معادل Fable 5 هست که نمیدونم چقدر درسته واقعا
https://telnyx.com/release-notes/kimi-k3-telnyx-inference
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4723" target="_blank">📅 20:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4721">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v857bpJPo3ydciGmzTLrlfvrIW4f02DDvhWsUk3ZkmU8YG59YLQftC0lXM_d97SZb9YegTbGXH2pSQTbMjZZTG-LKEZoSazRJdEKhTuD7YJG9OWXKzKKkYOa8alwiMCWFxZtny3ly0LdU7E_YjnNJgyGOk83B9TJ33KYy364weT2KoJMFHfN1JqCsGIVTN6tcsVa5qk1oJmze9ljF6O2FOxb3jjDi9s-ZJ6lZ3H1f0a-F2BuqtFscuP7Tfmpa0nDAudcljw3I2Shysr1xx6Ik6qegiHubh_Bn2biifXZ1Kvu1x5ZgYmZvE5a_Z441tlZhBAZnvX5Zb3XwVWP3FgpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iBBgF3F9KetHIQU1G7UHeZVAMaoE9vLJocQ78qEbzRw00c0IcohPdy0GUZV-zjbIbdOhmoj6L9j5G1yT9-7BGfTWbYt99tDZBbLQuW5s90PKh6573PFVre43Z9LWzsXA8SknhT-gJJZnRLHXHhVf7a8xL3ka5OcsvAKD-QO4kYRwAThIWMBN3RsdmXCTG2Y00k5lRQOrvz5TIgxUdtK12HgzkhlLFMt5SjcLWEw4DXU0-Q3Fsvu6pKttNOAxd7qLu2KW5zUYmzlB64Gds3Kkd1CmWedfhMLwPIC0jheivbBp04RJAc3vqMva2Nnz8nyE0737SbeBJ_VW1lL3QClzRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور جدید CottonDNS برای تست در نسخه 1.6.0
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید  cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZ2dzIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXNoZW50YWppci5zYnMsIGMuYXNoZW50YWppci5zaX…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4721" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4720">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بچه‌های WhiteDNS انقدر زود به زود آپدیتای خفن میدن من اصلا فرصت نمیکنم بذارم:)</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4720" target="_blank">📅 14:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4719">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به زودی کارهایی برای Aether-GUI انجام میدم
دلیل بررسی نشدن PRها همین بود</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4719" target="_blank">📅 14:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4718">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4718" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4717">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4717" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4712" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4711">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTAaFy_BbXBVotEx6GRZN3Oiqy8T1kH0PQmXSiyh3qlA72L4YYNTR65vFrQTcLAflLOKT21MlyxaTg5NgTXePcI4SSE5BVpstil-jsA_r4VLb0HFqL0_sX_OrviP-5pBVgQ-QYEI3jRMsogRP0B9a1yU1-nIRAWGD7N4subiYuFp2BDU4ffK9r3r5wjM8HAHhqFMKlM6psFvQYuEwSL8Ihi8jyyC1rLFCo-E4xFx8Krei6I8KsU93RIHv3oebtAjuacy8qc8zYNECHUHZJ6Lnq-PGDNn5xvF4DarqOa1hkSghuv_8aEuM5r7yeRerlo5wtvoyL5HBBKxGHW4HLsY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4711" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=DxSSHDYOzdw853sOkV0UaKtuN9UTPAuV9-xJ1l7HnNgRUY78gzeJkojUA6ASb1tgc34sjWUdzzXAOJTjJ3hRnsDIjKI3p0kA8n-OkTF4SfQ4zhcxerKEiJjXT0BjdKzJpQhV575Xrs1JKC0_p6FI-sNbVlgD4qGQUpDmqPHcFD2W5EHD7DHcuX7M0V-vE3rwZXlUf3uEFz8LPq_1rxagSNEmwInu4YonVGheUUawffh9NnDiIq5HxUSSyHjv175xDyAHtYzJxvFt4XpVxO4mY-05d215qaiQ4Wy_IpQQi6kgQEj0RGM596CtaRtJewh44R0lnXUOPgl-qXVjyysaYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=DxSSHDYOzdw853sOkV0UaKtuN9UTPAuV9-xJ1l7HnNgRUY78gzeJkojUA6ASb1tgc34sjWUdzzXAOJTjJ3hRnsDIjKI3p0kA8n-OkTF4SfQ4zhcxerKEiJjXT0BjdKzJpQhV575Xrs1JKC0_p6FI-sNbVlgD4qGQUpDmqPHcFD2W5EHD7DHcuX7M0V-vE3rwZXlUf3uEFz8LPq_1rxagSNEmwInu4YonVGheUUawffh9NnDiIq5HxUSSyHjv175xDyAHtYzJxvFt4XpVxO4mY-05d215qaiQ4Wy_IpQQi6kgQEj0RGM596CtaRtJewh44R0lnXUOPgl-qXVjyysaYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب چرا؟ اندازه پنج جلسه تراپی کمکش کردم.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4709" target="_blank">📅 00:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4708" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4707">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cvpDxU7SbYSoSacPgtD46xqva5GcSqdaDD7u3x4s2jedxEnQDMYM9y06Dfu-e0WZrL3y1aDOnqW1LLgCpxUQUMDk22YNBMgaIKQMowbpbfXf3WKkWj-Vcgyv8TXy1jewohmAaOKe6zG7K75Ozk95DtTmIFJ00FjfOZalfJuZVHh7RbgjHrxAhO_3ku6svIwOehnj3IucQI0o-O37fKUg9vR_pgigON8LaibdWh_FXbeKQTKJywSJgUsOi1Ms9LoxlYWNNU3oMsg7Y3NR6FqJYvav-kV90KcGBKDKaTRZ7jQC7HsbbJMi3uJXovb7IghnYmH3hrJmyqnvxoJVPXTtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4707" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4704">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FOWn5SBdpF6f62I4DyOIvJe1fhtFkOxuPHIufkYsuo_NIhhj0SSz6IPNynJlO_00taaaj8ABM5fUYYn_o1T7tyGkVDIs5zKY9sPOpDiPeHyQdUSv4Y8NhVWBc8dFuJkUezpcq38OgFSshz9kkQXsv_3Fz3OZmfiYH3zR-kjiq0S2m42JsOxT697dUJItt09_zXaYcdflbelYzuu2XgjwVSu_iekxbj1xqy_tPn2VTAxtU0Gi9GvCCKMHeXFlsz2EOVMSrLUxS7VIqvTseyCQP1IZcaHBqt9I4oK8mORHDtFikty_n5ICJCKjtNbDbWv63Dwv02i90iO1plEn004G2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PUuuj_921Pv4AbGagkUsN6_77QPSFm45i7v_TaJQkeO6EgwKGNtV8YacFmNWovwfrHnJymYiClndMdNq-mGglucTEsl36NgTS8KiH3zefmpF4i6uKe5eIg4tksAPL1vpZPJfuk6qqHYOW2JGVKMzM275IKhQ0zsxNDT85rS3s4VSugc9vGuOXqSN9dTJAZm3wMzvQyPyN-RxvEKAVH4zBICnq01SX7sveKizd3oekCPE_UzmDyLKYWAyMRc1ufGs7a_rLA9wC-q2kcL3PBI5Uw7W166VjbCQZhcNLQx6AUBtwBogMPhU7U1j7uPQHbz_D7dyuIAeGVepIysJDgo50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C9MNoEGiBkIFfYOMjbCmwpXaokvfVMgH6LkV2aeIZu8tnM2z3hfgFdAr_Q9JfX75sF1BmMMGNPBqks-saEZ9sbd_95WWn3MoSBTpAdqS6DKJ1lzfEX0E4k6L1U0gemgpBE-aHrJgFaRpu4U5MZg5GR3ajs5g8Na_2QLcFLV11_hgepSea0Lx6mraWw7JWbsUVAvmyLKOeKYxi_oPi0ToamaXYCAnc2KMISWAZeF_rOJZZe8WyEL0H3fTRehUrirtLo14w6panXzQ_3sk9OicXSxpHtDme9haLkXB3oB6rX8ZCPrIDLmxBhj8vcpeBKW9DGd3efwhzpT53S5gvK1azw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماژول رایگان و قدرتمند حذف پس‌زمینه‌‌‌ی FeyNoBg
:
تیم شرکت Feyn از مدل جدیدشون به اسم FeyNoBg رونمایی کردن که برای حذف خودکار و فوق‌العاده دقیق بک‌گراند (حتی برای مواردی مثل تار مو در باد یا ویدیوی ضربات ایستگاهی فوتبال) طراحی شده. در کنار خود مدل، کتابخونه پایتونی که باهاش مدل رو آموزش دادن و اجرا می‌کنن به اسم NoBg رو هم به صورت کاملاً اوپن‌سورس روی گیت‌هاب منتشر کردن که می‌تونید همین الان روی هاگینگ‌فیس تستش کنید و از کدهاش استفاده کنید:
سایت اصلی:
https://usefeyn.com/blog/feynobg
مدل روی Hugging Face برای تست:
https://huggingface.co/feyninc/FeyNobg
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4704" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4703">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rcQFmflpqfgeQ6VsEkBF56SwN2dnAQ1FKEWuhVH-m7O8c6PyGzr7jALUsjepgSkTWHQd8tXtwYaVmXpPB5jgDNEXIs71ruYACt_wMoH2AFTFQmF5fd7_APsb5vfKjrbpd3-gyfHP0ebE8VvEjs4hP2Svqrk2jdESEqZcIblLUuldOqatarpXIQY4rl-x381B60FwZlSD66jBopYE5S6n-D0L7ih9TUm_eZlX7zypbf1QvE6Hg3tJmvGjMivUr5g-AgM3UXEKXcGCtg4PCRR7hYUJdcWfmH27Ias-fXmDQAqovX4P3MvG6NcllEiw5LAlEI8LGrH5h8Cj9qDokLCeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالم که هنوز اشخاصی رو مثل سعید عزیز، در کنارمون داریم...
و ناراحتم از اینهمه آزار جنسی و تجاوز و پدوفیلی که توی دنیای واقعی و فضای مجازی میبینم که خیلی‌هاش هم متأسفانه منجر به خودکشی میشه.
ای کاش لااقل نهادی بود که مثل کاری که سعید سوزن‌گر یه تنه داره انجام میده، کامل و به طور رسمی و جدی پشت این قضایا بود. که این عوضیای بی‌صفت، نتونن انقدر راحت توی اینور و اونور با شماره کارتشون فیلم و عکس‌های این چنینی بفروشن
دردم میگیره اینا رو میبینم.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4703" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4702">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سالواتوره سن‌فیلیپو، هکر ایتالیایی و خالق Redis، توی مقاله‌ی جدیدش توضیح میده که نبوغ واقعی لینوس توروالدز(خالق لینوکس) فقط توی کدنویسی اولیه کرنل لینوکس نبوده، بلکه بزرگ‌ترین تصمیمش این بوده که خیلی زود کد زدن مستقیم رو کنار گذاشت و روی رهبری، هماهنگی و تعیین اهداف پروژه تمرکز کرد. برخلاف خیلی از مینتینرها که خودشون رو درگیر پیاده‌سازی جزئیات می‌کنن، لینوس فهمید برای مدیریت پروژه‌ای به این بزرگی باید زمانش رو صرف رهبری کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4702" target="_blank">📅 16:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4701">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پشت‌پرده بازار فروش غیررسمی توکن و کلیدهای API هوش مصنوعی
تحقیقات جدید نشون میده چطوری یه شبکه‌ی بزرگ (عمدتا توی چین) برای فروش توکن‌های LLM با تخفیف‌های سنگین شکل گرفته؛ این پروکسی‌ها از طریق سوءاستفاده از اکانت‌های Trial رایگان، ربات‌های پشتیبانی ناامن سایت‌ها و ترکیب کلیدهای API مختلف کار می‌کنن.
که برای به سرقت رفتن اطلاعات مهم استفاده میشن یا Train مدلهای AI چینی.
به زودی بیشتر تحقیق می‌کنم و بهتون میگم
https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything
اینم لینک مقاله‌اش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4701" target="_blank">📅 03:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">خدا لعنت کنه این جاوااسکریپتو با این سینتکسش من ده تا زبان بلد بودم اومدم بکنمش یازده تا جاوا اسکریپت رو هم اضافه کنم بهشون، همشون رو یادم رفت الان فقط جاوااسکریپت بلدم
@Linuxor</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4699" target="_blank">📅 20:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">روی اوپن کد هنوز میتونید از nemotron3 انویدیا استفاده کنید</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4698" target="_blank">📅 19:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فعلا میریم nvidia(با اینکه delay زیاد داره) تا ببینم api رایگان امن چی پیدا می‌کنیم باز</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4697" target="_blank">📅 19:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مهم
راجب Mimo
😭</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4696" target="_blank">📅 19:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YhWjPKzLl37tug5TYpXqVuERHtOe0pc9u7NJwDq8dZwE4dup9lhbbIrXR4-Nwz5VBfxkd-DJJm8hbJooNMd05fCDs5RMp0colutCAjBwYpC1ac_SUAfKDWpWWDG4mdTY1yoozRUuSFVcfF9T_hy_MiNw6r08krn5j_2jXd2_L_GBFnAIPoeCBp6Xzi4wh3L-M2SZQKX3VMmBWjI0FbYoHbUR2D6z3aX9uhrG8UqarC757aOY35cWi_7wEjVbnlyRYJp6ufc4dsft6LGAhqKFCEfvzs1RenmfZoSJmO4fwkBWPMzx3JPdmF_NQKNy9_FLHnZpxA-qVIj9uV58hRNAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ovb1E5aIkJzf_MTXhrfBsYZrBdfyt3A4rJB6Z3Xl195HlTo2Kj1O3mSWaXwfqSZh1iz45sgZ7sCcaR90NuS240u_rRvzJ9fEE_FDEa_M2XfNEzFi1hOKlEe-rTXGmiQUeWAsJrOySyRE_3tTXAtjGxTEgWtGPx9VZJLZekX5pROqSsqHS_imUVUmcG-0AjvX-CYd2Ei1cN3WDA7DPOcrLOji6EoZm9117XKYRQR1NTrPaE6YV9MgTJ1TjhSVeId5DLCB8n0sCXjGFB3KecGmRGKdg1_RsdiuttQXYUN5kxMqzh2mNu0pMjuySpu6_U1dDJUUKLWuV0RXnERV1alZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cOrrSlLLBB3QfkSnqLyW2WlHTSvYehEdG-dsINDgpNbFpPOaMiXWBgxum2Z9tHAXAPU9spsJYwiQ3PuBDVLhsz-Y8JP_njPTPv0mcS8xVGFZmKT7F2kadoJZxH0ulPVFoGPYx0IAillVs1Wjl1miKsW1xgYRrAzCIQ3CcH5VQyVgJGeLhq13oaCFFT0-ASBYtOpRBIiqSO38ZgxbDiac-XXWNItvsDXzd9W4A0Qi0Th01cYoh96ZoHxQIXKs7A8oiPleTidqDiFiReBf2dWZKMjrjjbIhYoeH7Q50vksKiclR7F9RruT3AAknz95Sj1IPvbi-eyhkKqERUiGnF5b2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برای این از proxy relay کلودفلر که توی ویدئوهای قبلی یاد داده بودم هم استفاده کنید مشکل برطرف میشه دوستان</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4693" target="_blank">📅 18:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4692">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">همینطور اگر ارور the model provider is ratelimiting میگیرید، به خاطر شلوغ بودن سرورهای Mimo هستش طبیعتا از روش‌های دیگه‌ی api رایگان که توی ویدئوهای قبلی یاد دادم می‌تونید استفاده کنید برای 9router و بندازید پشت همون Combo</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4692" target="_blank">📅 17:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4689">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4689" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Aether 1.2.2</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4689" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4688">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/b4E4bwyTavGqVYAuaoiIEE8UjuCQKUmOc5mA1gQX8oPUz6_z7hLPzoMJarDnv8wR0Eku4-xmSV9J_d9Luq821wlP0I6WHzCCUpN-haFnyBqjbjVUK7A7rtRlF-HrKSfdYcUi-MY_o_DnE95e2iP8T74Otvm768KRZu97AtSIgXK2FsflQNUARN12gliWez5MtOXJTMO7DTj7iYXedTbWQJVgTCknpXPkerY6GBGOa4-r5kxYEocmINPTuoHZ0Rkk9zq2Iad1_lQ0XpRwe2sdxZjZe-mvrnCwBf-q4QzTrqyBdOTD7Y68m0Qe3fwflOOq6OkCpd0G5rSoKzfNPcY_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
تازه‌های نسخهٔ ۱.۲.۲ کلاینت موبایل Aether
🚀
یک به‌روزرسانی بزرگ و بنیادین با تمرکز بر امنیت حداکثری، کاهش شدید مصرف منابع سخت‌افزاری و ثبات اتصال منتشر شد! در ادامه خلاصه تغییرات این نسخه را برای شما آماده کرده‌ایم:
🔄
۱. مدیریت خودکار و ارتقای هسته (Core)
ارتقا به نسخه پایدار ۱.۴: هسته تانل داخلی برنامه به آخرین نسخه پایدار ارتقا یافت.
خودکارسازی در CI/CD: فرآیند همگام‌سازی و اعمال پچ‌های اختصاصی اسکن رنج به صورت کاملاً خودکار و هوشمند در خط‌لوله بیلد گیت‌هاب پیاده‌سازی شد تا از بروز کوچک‌ترین ناسازگاری یا خرابی در فایل‌های نهایی جلوگیری شود.
🗑
۲. حذف کامل سیستم به‌روزرسانی درون‌برنامه‌ای (ارتقای امنیت)
افزایش شفافیت و امنیت: بخش دانلود خودکار درون‌برنامه‌ای به همراه دسترسی‌های پرخطری مانند REQUEST_INSTALL_PACKAGES کاملاً حذف شد.
دلیل فنی: برای اطمینان از اصالت کدها و عدم نصب ناخواسته فایل از منابع ناشناس، از این پس تمامی آپدیت‌ها صرفاً به صورت رسمی و امضاشده فقط از صفحه ریلیس گیت‌هاب پروژه قابل دریافت خواهند بود.
🌐
۳. حذف لوکیشن‌های فیک و واگذاری اتصال به هسته هوشمند
حذف منوی انتخاب کشور: از آنجا که شبکه WARP کلاودفلر از آدرس‌های Anycast استفاده می‌کند، انتخاب لوکیشن در کلاینت عملاً تزئینی بود.
اتصال هوشمند واقعی: در این نسخه منوی لوکیشن حذف شده و وظیفه اسکن رنج‌ها و انتخاب بهترین و نزدیک‌ترین لبه ارتباطی (با کمترین پینگ و پایدارترین حالت) به صورت پویا به خود هسته برنامه واگذار شده است.
⚡️
۴. کاهش مصرف رم، پردازنده و بهینه‌سازی رابط کاربری (UI)
کاهش مصرف CPU در حالت آماده‌باش (Idle): تغییر ساختار مانیتورینگ اتصال از حالت Polling به حالت Blocking روی پروسه هسته که باعث می‌شود پردازنده گوشی در زمان اتصال بدون ترافیک، به خواب عمیق برود.
حل نشت حافظه (Memory Leak): محدود شدن حجم لاگ‌های ارتباطی به یک بافر حلقوی ۸۰۰ خطی (حداکثر ۵۱۲ کیلوبایت) جهت جلوگیری از مصرف بی‌رویه رم در اتصال‌های طولانی.
رابط کاربری روان‌تر و سریع‌تر: حذف انیمیشن سنگین شفق قطبی (Aurora) در پس‌زمینه و جایگزینی با رنگ ساده ساکن که بار پردازش گرافیکی گوشی را به صفر می‌رساند. همچنین منوی تنظیمات پیشرفته اکنون بدون کوچک‌ترین لگی فوراً باز می‌شود.
🔌
۵. رفع تداخل با v2rayNG و حل مشکل نصب (Over-Install)
تغییر پورت‌های پیش‌فرض: پورت‌های اشتراک‌گذاری شبکه محلی Aether به 10810/10811 تغییر یافت تا با پورت‌های پیش‌فرض v2rayNG تداخل نداشته باشند. همچنین سیستم شناسایی هوشمند ابزارهای موازی اضافه شده است.
حل دائمی مشکل امضای دیجیتال: گواهی امضای اندروید در بخش بیلد تثبیت شد؛ کاربران نسخه ۱.۲.۱ می‌توانند بدون نیاز به حذف برنامه قبلی، نسخه جدید ۱.۲.۲ را مستقیماً روی گوشی خود نصب کنند و تمام تنظیماتشان حفظ خواهد شد.
🔒
۶. ممیزی امنیتی ۱۰۰ درصدی خط‌به‌خط
کد منبع برنامه تحت ممیزی سخت‌گیرانه قرار گرفت و از نظر مواردی همچون اطلاعات هاردکدشده، نشت DNS/IPv6، ذخیره‌سازی محلی ناامن و ترافیک رمزنگاری‌نشده کاملاً پاک‌سازی شد.
📥
هم‌اکنون نسخه ۱.۲.۲ را به صورت رسمی و امضاشده دانلود کنید:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4688" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4687">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">همینطور اگر ارور the model provider is ratelimiting میگیرید، به خاطر شلوغ بودن سرورهای Mimo هستش
طبیعتا از روش‌های دیگه‌ی api رایگان که توی ویدئوهای قبلی یاد دادم می‌تونید استفاده کنید برای 9router و بندازید پشت همون Combo</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4687" target="_blank">📅 15:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4686">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خوشحالم که این ویدئو برای خیلیا کاربردی بودش
🔥
روی یه سری آموزش دیگه هم دارم کار میکنم واستون</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4686" target="_blank">📅 15:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4685">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PBkqtjWVceYJ-kooMXGiSQlV5ZhM822-QLxwBvry0fJITUEecVtwOtO5s-Px3e2dJa1HU3WMQJOpiDEoeAjyIhi2eFQnBUdxcSHwL8R0MvHCnYdkUBng4Zqbi3Bd9-sljn8ciTXYPvgEIgsyGhzVDzVZvZdmu8ObT0NfTANqGAQygL06il-_NiGxuQvD7i18ACcQ1Cdfw3qbvzuonsy6BRGF-Kg0_-7fCJHtXz3p7Wvk0FDAoLuPtS59l_MdXwuNZWRoxkY7fFje_FxhmGpwS8dKhtTVwDWI6cpESSm2U2GeuESrLznqZSFIpJvtEAvVeAXk_qWZjR_9MxJwoQPD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان اگر به ارور workspace has been restricted خوردین، باید یه ایمیل جدید بسازین، با ایمیلتون اول اکانت گیتهاب بسازید، و با اون اکانت گیتهاب توی railway ثبت نام کنید تا بهتون گیر نده و فکر نکنه اسپم هستید. خودم الان یه بار با continue with email ساختم دقیقا به همین ارور خوردم بلافاصله بعد از ساخت 9router، ولی درجا یه atomicmail تازه ساختم و باهاش یه اکانت گیتهاب ساختم و باهاش لاگین کردم، سریع ساخت 9router رو و گیر نداد</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4685" target="_blank">📅 05:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4684">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عبارت VPS هم زیاد درست نیست. صرفا جهت شیوا بودن کاری که قراره انجام بدیم بیان شده
👍</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4684" target="_blank">📅 04:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4683">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-railway.txt</div>
  <div class="tg-doc-extra">168 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک‌های استفاده شده در ویدئوی بالا</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4683" target="_blank">📅 04:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4682">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JeS-rKn1B86gdyqjUgjFYdoEr-ZwLFHjV5em1EwpJjg3UWZQ0HCS8ADPjj7eDThyskGnjWQuEWD8l2DA4YZY-CUn7TMUn1n5YqTkUHNJdsR234x1rUkkR6eFPcsUFtySC2o3r9q1GvCkpqFA6-pUvmRp5AADroHt6INB4MhHtQmJJyAGZE1Ibi_juUEZwuUqRlZibhOOrrPHgPI6mR5HV3n2zLvvVndKPhzqYgbbMz6GtwWcfE_jn9ZoTtE4G5K-j_WQoWUJSjN8RBzYvH8SM6wTd2yX9mAxXBY6-Hb8cq9yNLY55n_Jn5CwrtcxmxOjo_mYxEtL4ALF9NYejbwxHw.jpg" alt="photo" loading="lazy"/></div>
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
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/4682" target="_blank">📅 04:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4681">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فکر کنم من تنها کسی باشم که از اینکه مردم از کانالش لفت میدن خوشحال باشه
😂
به خدا حس میکنم هرکسی لفت میده، جمع اینجا خلوص بیشتری پیدا میکنه و اصلا کیف میکنم
شبیه عصاره‌گیریه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4681" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4680">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منم دارم یک چیزی برای بچه‌های کانال آماده میکنم که با گوشیشون هر جا که میرن، رایگان، بدون فشار اومدن به منابع گوشی و روی هر گوشی‌ای(آیفون/اندروید/...) بتونن با بکاپ گیتهاب، هرمسشونو راه بندازن و از تلگرام باهاش چت کنن 24/7 خیلی باحال میشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4680" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4679">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NH-ROCkdeQDRvom5qLl7ea6H-9Ozo-Aq0PbCNjMZXirvMrRp7c0LrHpo4XxRudcLQbAoDOX2CR27QekZa8zj_RMotSjbyVO262o43d1Mu3mRLZRPmRy5mKtdxsmjhUghYiGGp7i5iOuVWfKaK79YnsHljTGP6UlFRtanFwyFtu8XXYzDE5hOWkNyIkk6_J2huUJSZURJerrkkiilzVAZCx9kV0-2MIJGCqFArLd7yjs9IwChDa0yGecwGYbaLJOJgR7tu2uovuzA9WbbHWaQfLYu9ZPU2z-07DixDKfEByh53dzCZmy8cMZ6xApRitasAzfTxfU5XmGDqArMZ4xFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم دارم یک چیزی برای بچه‌های کانال آماده میکنم
که با گوشیشون هر جا که میرن، رایگان، بدون فشار اومدن به منابع گوشی و روی هر گوشی‌ای(آیفون/اندروید/...) بتونن با بکاپ گیتهاب، هرمسشونو راه بندازن
و از تلگرام باهاش چت کنن 24/7
خیلی باحال میشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4679" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4678">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">برو برو
🥰
موفق باشی بعدا میتونی معرفیش کنی خودت و بگی چطوری توی تحقیقاتت کمکت کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4678" target="_blank">📅 01:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4677">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خجالت کشیدم، میرم پروژه رو راه میندازم.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4677" target="_blank">📅 01:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4676">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تینا شاگرد نمونه‌ی منه و به ترسش غلبه کرد و هرمس رو راه انداخت
❤️
پرسید، تلاش کرد، به ارور خورد، و آخر سر تونست با اینکه تجربه‌ی چندانی از کار با کامپیوتر هم نداشت</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4676" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4675">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">باعث خوشحالی منه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4675" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4674">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">من به شما افتخار میکنم.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4674" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4673">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در مورد این، یه وقتایی به نظرم بهتره آدم کمی پروژه‌های پیشرفته‌تر ببینه که هم بدونه دانشش در چه حدیه، هم یه دیوار جلوی خودش ببینه. نه برای اینکه بترسه، بلکه برای اینکه بدونه دیواری هست که میتونه ازش بالا بره! و انگیزه‌اش بشه. من خیلی از مطالبی که میفرستم اینجا…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4673" target="_blank">📅 00:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4672">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4672" target="_blank">📅 00:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4671">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">موافقم و روش تدریست رو خیلی دوست دارم. اما خب، شاید برای کسی مثل من که کلا هیچی از دنیای کدزنی و چیزهایی که آموزش میدی نمیدونم کمی ترسناک باشه این موضوع  این‌ روشی که بهش اشاره کردی رو توی کلاس هم پیش گرفتی و اونجا به من هم حس اینو داد که خب وقتی متین نمیگه…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4671" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4670">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خود هرمس و راه‌اندازیش مثلا شاید یه دیوار بوده برای خیلی‌ها.
من و بقیه‌ی بچه‌ها توی توییتر و تلگرام و اینور اونور، طبیعتا تجربه‌ی کار با کامپیوترمون بیشتر بود، زودتر راه انداختیم.
انقدر نشستیم بالای دیوار و از منظره تعریف کردیم، که چندین نفر دیگه هم ترغیب شدن و تلاش کردن بیان و بهش غلبه کردن.
چون واقعا کامپیوتر، و همچین مفاهیمی که شاید برای یه سری از دوستان ساده به نظر برسه، برای عده‌ی زیادی اولش ترسناکه. و باعث میشه فکر کنن خب، اونا که تونستن از پسش بر بیان باهوشن یا هر چیزی، و من نمیتونم.
که اصلا درست نیست.
کامپیوتر و این مطالبی که اینجا قرار میگیره
همه‌اش مهارته.
و هر کسی با تلاش و پشتکار، بدون استعداد، میتونه یه مهارت رو یاد بگیره.
شاید یکی زودتر یاد بگیره، سریعتر متوجه بشه، ولی در نهایت همه با تلاش می‌تونن بهش برسن</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4670" target="_blank">📅 00:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4669">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اما تفاوتی که هست اینه که تمرین‌هایی که توی کلاس میدی در راستای چیزیه که بهم قدم به قدم یاد دادی اما مثلا اون پستی که برام فرستادی برام آشنا نبود اصلا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4669" target="_blank">📅 00:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4668">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">موافقم و روش تدریست رو خیلی دوست دارم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4668" target="_blank">📅 00:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4667">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به نظرم این شکلی یادگیری خیلی مؤثرتره
😂
موافق نیستی؟ آدم اگه 5 بار هم قدم به قدم جلو بره با ویدئو یا آموزش یه نفر دیگه، خودش اگه یه جا گیر کنه ممکنه نتونه انجام بده ولی اگر خودش درگیر بشه، واقعا تأثیری که داره صدهزار برابره.  بچه‌هایی که تازه اومدن توی کار،…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4667" target="_blank">📅 00:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4666">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">من تاحالا وارد گیتهاب نشدم، پروژه گیتهاب دادی بهم گفتی برو برای خودت درستش کن
😭
😂</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4666" target="_blank">📅 00:39 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
