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
<img src="https://cdn1.telesco.pe/file/jxrGpWZ3gPdfcrwtVBSSoABbRSFB3TABX2sPBbjVPj_nAHo0atS2jslrx0OvGA7n4SlHF7XW5mk4Vmfbkxh8hnWmHFf39p2fIYSMQy76IT3n-IE2ixZDmZozr-xOD532xx_WayAbRwrOw2KluW3iU94QNk_WM44QWukJJqgDx44LFeVr6DvA-Y_WN2PG4Ga1hiNsO_p_CzHaLruH_yTaB6LZuTWnCRyV2spBoFB-3z0muWKz29Cs7e9PPvh1-vHQ2G6oDYaPCMMqdsns-7iDWX7gthr3ERpx63zTOMj57Qj_QvZesEvRrKUCsdm0fvr-STRpxL_mX_PAUgy3paUYyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 161K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-3967">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه سری آموزش راجب ایجنت‌های کدنویسی قرار بود داشته باشیم به زودی، منتها لپ تاپ لولاش شکست و دادم تعمیر کنن
😳
رسید دستم ضبط می‌کنم</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/3967" target="_blank">📅 17:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3966">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from᯽マティ️️ン先輩</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=oIG9KIueQC7WgUOYHOM0DoTslqBce9mtlgJMMl_xpfrCsUnYYQbNHfxXaRA_Cc5oyyTivndASp3qOICio10-69luRHiPEhCQc3QT73Z48glhEBF9nqNogVeS0xy0K2gc3y4c5Dg2jx0DpSOZ5sADCcyErE-Ls8l60IEp2x7YnZM6y5SEI0GKvEzdfqGqpxG9f9WqjYEfC52kqt6OUanr6kDDCu96dF_MJxthoQgmyZ8OvAMGxH68b1sHlzFvDOgnGTw8Z8KBssxbEw-IdBCExxzvJFbuDcyMwrgoeEYahX-RpK9mh-0xvkiMs2ZIexhYUsM9XnXNJo1P9Y58Oiq4Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=oIG9KIueQC7WgUOYHOM0DoTslqBce9mtlgJMMl_xpfrCsUnYYQbNHfxXaRA_Cc5oyyTivndASp3qOICio10-69luRHiPEhCQc3QT73Z48glhEBF9nqNogVeS0xy0K2gc3y4c5Dg2jx0DpSOZ5sADCcyErE-Ls8l60IEp2x7YnZM6y5SEI0GKvEzdfqGqpxG9f9WqjYEfC52kqt6OUanr6kDDCu96dF_MJxthoQgmyZ8OvAMGxH68b1sHlzFvDOgnGTw8Z8KBssxbEw-IdBCExxzvJFbuDcyMwrgoeEYahX-RpK9mh-0xvkiMs2ZIexhYUsM9XnXNJo1P9Y58Oiq4Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر سعی کرد عملکرد و هزینه‌ی GLM 5.2 Vs. Opus 4.8 رو مقایسه کنه. و با هر دوشون با یه پرامپت یکسان، توی یه فایل Html، یه بازی Backrooms بسازه.
نتیجه‌اش جالب بود. این هم پرامپتیه که استفاده کرده:
Act as a senior game developer. Build a technically impressive Backrooms horror game in a single self-contained HTML file. Embed all CSS and JavaScript, no external libraries. Raycaster (DDA) with textured walls plus floor/ceiling casting, 480x270 internal buffer upscaled with image-rendering: pixelated, infinite 16x16 chunks from value-noise/fBm with a guaranteed open street grid, procedural textures. WASD + mouse look, F flashlight, Esc releases pointer lock. Dynamic fluorescent lighting ON by default (never hard to see), warm yellow fog, vignette/grain/subtle VHS, Web Audio hum + fluorescent whine + footsteps. Psychological horror, dread over jumpscares: footsteps behind you that stop when you turn, lights that flicker then settle, a far silhouette that vanishes, rare spatial anomalies, randomized timers with cooldowns, slow escalation. Save position to localStorage. Return only the complete HTML.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/3966" target="_blank">📅 08:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3965">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امیدوارم جای بهتری باشی الان...</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3965" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3964">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/3964" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3963">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:  https://yout…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/3963" target="_blank">📅 20:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3962">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:
https://youtu.be/CPrePbvbbic</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3962" target="_blank">📅 20:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3961">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S6jyJjD4YdFR1CayJwRyeFwi0yBNKY1514xethpayN7xBTsAD4AITeOQLohrIWJQpidIYbjgF9yC-9wroAysDfH2hiViKD97THhHn8sP2WcONnlc24zaknmKl1HCPfoe7eIr54Crw8CU-aJFfsb1rTtO_HglirwOCouJWXfPFC-vcQoyfV0dxldpuaPWLYmxhI_VWEnFde2jPltZRGmTTNwVbTiByYWE9H-_02-XfLcJnigwhG5w8r_Uu0yOT_tHfBo-0a-wX4gm0ivn3bywcjeba18aqa6V-D04UPZ949aFgy_lnXVEsK1AYPsmnBH12BBU1_dEnvSdBdjTx1ZoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
نسخه‌ ۲.۲.۱ BPB Wizard منتشر شد.
۱. قابلیت اضافه کردن چند اکانت کلادفلر به Wizard اضافه شد. این قابلیت برای بچه‌هایی که اهدا میکنن و تعداد زیادی اکانت دارن خیلی کاربردیه.
۲. اسکریپت نصب خودکار برای macOS هم از این به بعد قابل استفاده هست.
✍️
بیا پایین بچه
آموزش استفاده از ویزارد رو قبلا ضبط کردم:
https://youtu.be/uCRKnrQEQYU</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/3961" target="_blank">📅 14:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3960">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا...
پروژه نهان که قبلا متین معرفی کرد رو محصول داداشم دکی واسه دسترسی رایگان به اینترنت آزاد با روش ورکر رو بلدید دیگه؟
حالا میشه آسون تر حتی واسه کسایی که مبتدی و هیچ ایده ای ندارن هم ساخت با کمک ربات:
@itsyebekhebot
شما وارد ربات میشید ساخت پنل نهان رو میزنید وارد سایت کلودفلر میشید و طبق راهنمای کامل پیش میرید و ظرف دودقیقه حتی کمتر با کمترین اطلاع و دانش از ورکر یا هر چیز سخت دیگه ای فیلترشکن رایگان خودتون رو بسازید به صورت رایگان
❗️
نکته:از بات ایمیل فیک هم داخل کلودفلر میتونید استفاده کنید:
@TempMail_org_bot
هر جا هم گیر کردید بهتره که به من پیم بدید
😆
آموزش ساخت پنل نهان
@yebekhe
👑
@xsparvin
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/3960" target="_blank">📅 12:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3959">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">اگه میخواین بدون VPN، به سایت
x.com
(یا توییتر سابق) دسترسی پیدا کنید، کافیه این گام‌ها رو طی کنید:
1️⃣
وارد این مسیر بشید:
C:\\Windows\\System32\\drivers\\etc
2️⃣
فایل
hosts
رو با Notepad باز کنید
3️⃣
انتهای فایل، این خطوط رو اضافه کنید:
104.19.229.21 abs.twimg.com
104.19.229.21 x.com
104.19.229.21 ads-api.x.com
104.19.229.21 pbs.twimg.com
104.19.229.21 api.x.com
میتونید بجای استفاده از 104.19.229.21، هر IP مربوط به cloudflare که تمیز هست، استفاده کنید
4️⃣
فایل رو ذخیره کنید
5️⃣
مرورگرهاتون رو ببندید و دوباره باز کنید و
x.com
رو جستجو کنید (بسته شرایط اینترنت‌تون، ممکنه مجبور بشید که چند بار صفحه رو reload کنید
⚠️
توجه داشته باشید که در این روش، ممکنه
x.com
(یا توییتر سابق)، شما رو با IP خودتون شناسایی کنه، چون که شما بدون سرور واسطه ممکنه متصل بشید (به
این دلیل
از کلمه‌ی "ممکنه" استفاده کردم).</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/3959" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3958">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وقتی اینترنت گوشی رو Share کرده بودم برای لپ تاپ، بدون VPN، بهم آپلود 0.02 مگابیت میداد. اما همین رو وقتی با کابل و PdaNet+ اینترنتش رو share کردم، سرعتش شد 2 مگابیت. یعنی صد برابر
امتحان کنید شما هم، شاید همین اتفاق واستون افتاده باشه</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/3958" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3957">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1ZAV8vmzGDJWc2FuG4uDGIReNv3iCTTmvxOArQsjlmY8eLi35ZXCWjyAEVQcOaqN38L5TbePXuVNYsXxymYrePAr99WSMu7nOWwD068HFNLn541yR1O3uBBgb0b9TNDedRUCiurz4AAdo3JrySOlCN6yQ3-B3gAimFIRmUk6RPZNqGcVAmv90CZENP_7HB3EJhDZAx9Lehb1bD3GFYwiSP61BrzGYCK68BlyVwDnm4W3gyGgBadwALQEvO-uBEPsZdGNH3gnsZvMipkPDluHleeqNu8R_RlcOJhj9GySdGzGnE09Tcry5usnZtPyKNhQFX39JXkEKHgdD4BHVCNZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل در حال آماده‌سازی یک «ارتقای مغزی» بزرگ برای هوش مصنوعی خود است.
تصور کنید یک کارمند بسیار باهوش دارید که گاهی در کارهای طولانی «تنبلی» می‌کند یا برخی جزئیات تصویری را خوب نمی‌بیند؛ حالا نسخه 3.5 قرار است مثل یک متخصص ارشد عمل کند که نه تنها چشمان تیزبینی دارد (درک بصری قوی)، بلکه می‌تواند مستقیماً نقشه‌های مهندسی و کدهای ظاهری وب‌سایت (SVG) را طراحی کند. این ابزار برای کسانی که می‌خواهند از یک ایده خام به یک محصول دیجیتال واقعی برسند، حیاتی است. اهمیت آن در این است که فاصله بین «فکر کردن» و «ساختن» را به حداقل می‌رساند، هرچند که احتمالاً برای این هوشِ برتر، باید هزینه بیشتری بپردازید و با قوانین سخت‌گیرانه‌تری (فیلترهای امنیتی) کنار بیایید.
نشانه‌های فنی در زیرساخت‌های گوگل تایید می‌کند که Gemini 3.5 Pro در یک قدمی عرضه جهانی قرار دارد.
این مدل که به عنوان پاسخی به نیاز بازار برای «هوش عملیاتی» شناخته می‌شود، بر سه محور اصلی متمرکز است:
تقویت بینایی ماشین
استدلال چندوجهی (درک همزمان متن، تصویر و صوت)
جهش در تولید کدهای گرافیکی مانند SVG (فرمت برداری برای طراحی وب)
گوگل در این نسخه، «دقت جراحی» را جایگزین «تنبلی مدل» (تمایل هوش مصنوعی به کوتاه کردن پاسخ‌ها در وظایف طولانی) کرده است.
با این حال، این پیشرفت بدون هزینه نیست؛ گزارش‌ها حاکی از آن است که کاربران با یک «قیمت گزاف» روبرو خواهند شد که این ابزار را از دسترس عموم به سمت بخش‌های تخصصی سوق می‌دهد.
همچنین، اعمال فیلترهای محتوایی شدیدتر، نشان‌دهنده هراس گوگل از سوءاستفاده‌های احتمالی است. در واقع، گوگل در حال بومی‌سازی مفهوم «شاگرد اولِ سخت‌گیر» در دنیای سیلیکون است؛ مدلی که همه چیز را می‌بیند و می‌سازد، اما تنها در چارچوبی که معمارانش تعیین کرده‌اند و با هزینه‌ای که هر کسی توان پرداختش را ندارد.
✍️
Gratomic AI Bot</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3957" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3956">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کافیه یه آیپی تمیز بذارید توی بخش Advanced, ip fronting
زیر ۲ ثانیه کانکت میشه</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/3956" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3955">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/3955" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3950">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/3950" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3949">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frfwpKS1InwjjUeiz92R95b_wnvp4jd7s_Ofpg00vV0qj4rCwPgHSjPLRZA2fXA0BMI_LtEnK4Ro-Ruq9e_7TIOLxMaJQCAQmmF6YXEA_5FEKGWKB8o4QMJ_zxdILdDI6KE22YGel1F7C9_7_B0B0rGEkufiTMOUg2EZ_OZTRe9YpdyZXeFh71ECo3hKayu0jvA12S0CaNt2QZZ4DlvAIAoEUgB1YvS0Ze03e8iB7eBxHSUpjR8BbvVwAr90Ug2EKewRPGM-I_WKm0vGEJjdBxlJwTM-WVaC9udaBWatQBiJokdLJcjkicdaER-O6Twu0luPuK0RQzvTrp8FZSITaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه
• ظاهر اپلیکیشن تغییر کرده
• امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.
• پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.
• با کمک یکی از بچه های گروه، یکسری از مشکلات امنیتی اپلیکین رفع شده.
💬
اگر براتون وصل نمیشه، فقط و فقط مشکل از شبکه شما هستش. آی پی تمیز پیدا کنید و داخل فیلد IP Fronting قرار بدید و براتون کار میوفته.
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/3949" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3948">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3948" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3947">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YLVTcg8RFOu2zN6C7ULB5_0M5EewpXt5c1YgK4IzNXy9HsD8-C0nkWDs-DN7wgcj9iZMB1gvhoW42FZYtHuQt_3h5q4ZTymDotm5sHK6S653AOiMNbZRMr2X9p2eAV4LzxujsBSe-qhoS5Cbz9LIz1PFeWQoNvmvjOvpak5FmM5g2cnCSKn2lA-tklcpalDaSzbm8mTZtYwsBC8RiuTLeQrELT5TByIjGvlrxrMuifjmOUIRB06dZoxeF-GPgMxh9BbnXDcV5zZnw6GN5AVO6w9aRLUf1Usciikf7f2aDZS-Xfl9d3AF-fBjckmnaVBJIP0No6NR4O7MqgMm0W6PHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3947" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3946">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">✍️
دوستان برای جلوگیری از هرگونه سردرگمی، ما در حال حاضر سه اپلیکیشن مختلف داریم:
🛡
۱. WhiteDNS Application
این اپلیکیشن بر پایه‌ی MasterDNS ساخته شده و مخصوص زمان‌هایی است که فیلترینگ و اختلالات اینترنت خیلی شدید می‌شود.
در شرایط عادی فعلاً کاربرد خاصی برای استفاده روزمره ندارد.
🛡
۲. WhiteDNS VPN
این یک اپلیکیشن ساده‌ی VPN برای کاربران اندروید است.
اگر فقط می‌خواهید راحت وصل شوید، این گزینه برای شماست.
🛡
۳. WhiteDNS BPB
این اپلیکیشن برای ساخت و راه‌اندازی BPB روی گوشی اندروید است.
یعنی بیشتر برای کسانی است که می‌خواهند خودشان یک پنل BPB بسازند و مدیریت کنند.
🛡
۴. WhiteDNS Installer Bot
آیدی بات:
@WhiteDNS_installer_bot
در این بات می‌توانید کارهای زیر را انجام دهید:
• نصب MasterDNS Server
• دریافت لیست IPهای سفید Cloudflare
• دریافت کانفیگ رایگان VLESS
• تبدیل کانفیگ‌های خودتان به کانفیگ‌هایی که پشت IPهای سفید Cloudflare قرار می‌گیرند
🛡
۵. WhiteDNS Installer Wizard
لینک گیت‌هاب:
https://github.com/iampedii/WhiteDNS-Wizard
این ابزار برای کانفیگ خودکار سرور شخصی شما استفاده می‌شود.
با استفاده از آن می‌توانید سرور خودتان را همراه با پنل شخصی 3X-UI راه‌اندازی و تنظیم کنید.
❤️
یک نکته مهم:
اینکه اسم برند ما WhiteDNS است، به این معنی نیست که همه‌ی سرویس‌ها و اپلیکیشن‌هایی که می‌سازیم حتماً بر پایه DNS هستند.
ما از اسم WhiteDNS به عنوان نام برند استفاده می‌کنیم، اما راهکارهایی که ارائه می‌دهیم می‌توانند VPN، BPB، MasterDNS یا تکنولوژی‌های دیگر باشند.
@WhiteDNS
🌎</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uJeNQjy8j-3Yl40u9MWxXB8ebDTI-CCB9rkCEW95fzO7LBEfmBr6FWTyhR58tZS9ttpR2afo0KuKpWj4sJAZdz9-aiGZuhJfIyguxzNr-fbShhLHMR0J7E_gEtjYMWm7xtf5_U7EPgs8RsKr53mNVNcuBZPlocwpDy978389h-Ky2P4YMAm3tvy9-Mz56eB431xO2Fy6h3eVn4EaEIc1fJCZ9HHSexpsOmTh7F9w994kT8q7jyC1NNUTW-9be9-Z0QXFHnsHpNQhavn-qdUxyXONgXZOFKWySOkTRDcajISj1r6M_EjHrimvDgU-c6nsMAYZLFOxB-MqxOvt0gstyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K8VsqkCgUiD4wN9gkIOJqSxF3DGo6n_jjDeu-z-2Ze-lzKNDN4RJbixBbA5xCxNl2smP-A03kIoB8t_g9OaYb0CtZS0ZyKgGNKfWGVGuv25OvSZiS28nsAKmA59BvH6qCQLThXbfo3O1qB031KMcOH2f-FkVc-mqLtP3IInfXPff85odHbGP33Af5bg-k2atdzoUOM5CsFo6MtmeC3xUYuB8_ixQoTBtQEHDo3U5bRzkXBGusCGWF28I2MqwNvUhZDVDTZUXVZo_PsfobGcehShKG9bBCUyQ6KLK4oE34CdaR_dLCDzUayEkHBp5Toujb6N-wTOmGYeFOhyPzYtv-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3943">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز
❤️
در چند روز گذشته متوجه شدیم که بعضی افراد و کانال‌ها، به جای همکاری و ساختن، مسیر تخریب و سوءاستفاده را انتخاب کرده‌اند.
این افراد که ظاهراً در فضای اینترنت آزاد و کانال‌های مشابه فعالیت می‌کنند، برای جذب مخاطب بیشتر حاضرند هر کاری انجام دهند؛ حتی اگر نتیجه‌ی کارشان آسیب‌زدن به پروژه‌هایی باشد که با زحمت و هدف کمک به کاربران ساخته شده‌اند.
چند روز پیش اپلیکیشن WhiteDNS VPN را معرفی کردیم؛ اپلیکیشنی که هدفش این است کاربران بدون نیاز به تنظیمات پیچیده، فقط با زدن یک دکمه به بهترین کانفیگ‌های آماده و تست‌شده‌ی ما وصل شوند.
اما متأسفانه برخی کانال‌ها شروع کرده‌اند به استخراج کانفیگ‌های داخل اپلیکیشن و انتشار آن‌ها خارج از برنامه.
دوست عزیز، اگر مسئله فقط بستن مسیر دسترسی شما بود، ما ده‌ها راه برای رمزنگاری، تغییر مدل درخواست‌ها و محدود کردن این رفتارها بلد بودیم. اما شرایط اینترنت آزاد و محدودیت‌هایی که کاربران با آن درگیرند باعث شده ما تا حد ممکن ساده، باز و قابل استفاده طراحی کنیم.
مشکل اینجاست که همین رفتارهای مخرب در گذشته به پروژه‌های خوب و ارزشمندی مثل Slipnet ضربه زد. وقتی هر ابزار مفیدی به جای حمایت، هدف استخراج، کپی و سوءاستفاده قرار بگیرد، در نهایت انگیزه و امکان ادامه دادن از بین می‌رود.
واقعاً هدف چیست؟ آن کانفیگی که با زحمت استخراج می‌کنید، همان چیزی است که بخش زیادی از آن در لینک‌های ساب ما هم وجود دارد. چیزی که روزانه هزاران نفر را متصل نگه می‌دارد فقط یک لیست کانفیگ نیست؛ پشت آن اسکنرها، تست سرعت، بررسی مداوم، فیلتر کردن کانفیگ‌های خراب و یک سیستم کامل قرار دارد.
ما این ابزارها را در مدت کوتاهی، با انرژی و فشار زیاد ساختیم تا به کاربران کمک کنیم. لطفاً به جای تخریب، کپی‌برداری و گرفتن انگیزه‌ی تیم، سازنده باشید.
ما از نقد، همکاری و حتی پیشنهادهای جدی استقبال می‌کنیم؛ اما سوءاستفاده از ابزارهایی که برای کمک عمومی ساخته شده‌اند، نه کمکی به اینترنت آزاد می‌کند و نه به کاربران.
اجازه بدهید این مسیر ادامه پیدا کند.
✍️
@WhiteDNS</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3941">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">تیم داشته باشم، دوست دارم از خودِ شما کمک بگیرم. اگر دانشجو یا دانش‌آموز هستید و مهارت ترجمه دارید، این می‌تواند یک
کار نیمه‌وقت منعطف
برای شما باشد تا در ازای کمک به ترجمه و ادیت، درآمد کسب کنید. آیا این مدل همکاری برایتان جذاب است؟
هدف من این است:
سریع‌تر به محتوای آموزشی مورد نظرتان برسید.
هزینه‌ها برای هر نفر ناچیز باشد (پول یک قهوه!).
بالاترین کیفیتِ ممکن (ترجمه انسانی) را تحویل بگیرید.
یک زنجیره همکاری برای دوستانی که دنبال کار نیمه‌وقت هستند ایجاد کنیم.
هر پیشنهادی در مورد نحوه قیمت‌گذاری، فرمت‌ها و اجرای بهتر دارید، در کامنت‌ها بنویسید.
من تک‌تک نظرات شما را می‌خوانم تا بهترین مدل را برای شروع استارت بزنیم.
این فرصتی است که با هم یک کتابخانه آموزشیِ قدرتمند بسازیم!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7yHqFhRpzH7LLYSEVov8WdFoE9dWU9V5hk62Xq82htmYVKJ6Lh-2HHnkmmkbqkZsrspG4lJ4j_VL8IX0Hso7O37FHnIU_NAb5Gdodr7iXMLmU0Loh7dD8FFiqfA6KL8Y_NX3Qdi5lMCmfwysRYONaTOQvkzRHLzFePEHD6UQj-b8O6M52_h66MC8lH-2dShipt8aJItJa9tL5Gk0Bf9t6IwcC6S4o00MDxUtJWPakmsfUuQA8ECxbmalHBpg-SFJPmkTqypL7vltnALl3IVrvHL9tbFVAc2plIalxXfa1yJO_16jVhvhkw0S1VjYriQASC88Uktqk58lPOCgkP9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی، یک پیشنهاد ویژه برای دسترسی بهتر به محتوای آموزشی!
همان‌طور که می‌دانید، درخواست برای ترجمه و زیرنویس کردن ویدیوهای یوتیوب، یودمی و کورسرا زیاد است. از آنجایی که کیفیت و دقت برای من خط قرمز است، فرآیند آماده‌سازی ویدیوها (ساخت زیرنویس، ترجمه دقیق و ادیت) بسیار زمان‌بر است.
برای حل این چالش، قصد دارم یک
«کانال مستقل»
برای مدیریت درخواست‌های شما راه‌اندازی کنم تا با مدل
«مشارکت جمعی» (Crowdfunding)
، ویدیوها را به صورت عمومی و با کیفیت بالا آماده کنیم. در این مدل، به جای اینکه یک نفر هزینه کامل را بدهد، با مشارکت چند نفر، ویدیو برای همه آزاد می‌شود.
اما قبل از شروع، می‌خواهم «شما» تصمیم‌گیرنده باشید.
برای اینکه این سیستم عادلانه و دقیق باشد، دوست دارم در مورد جزئیات زیر در کامنت‌ها با هم صحبت کنیم:
مدل هزینه‌کرد:
به نظرتان چه مبلغی برای «مشارکت جمعی» منطقی است؟ (پیشنهاد شما برای ویدیوهای زیر یک ساعت و بالای یک ساعت چیست؟)
فرمت خروجی:
ترجیح می‌دهید فایل زیرنویس (SRT) را جداگانه دریافت کنید یا ویدیویِ چسبیده شده (Hardsub) که آماده پخش است؟
یک فرصت برای شما:
اگر تعداد درخواست‌ها زیاد شود و نیاز به</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hbqyXALu-vPYJfHl9yxLyn-Hy3Fw-0DMzrciyfxocgqgai_RLzVsivivcZ-28r0CdReZq8AetySdAchfPDyh0ZeDHTxLAS6ok-1LrQE61Lb-TgfSdxkqnaR71txYtGZSRVfgmWfzgM0KBxgxtTyTbBxGZYylg6Ssgk1i9xfV2YXMPNGSCXqfXR_XRM1eSoAULsAQ9gDIzW-FB26QaIQJ5kKykcFdj3MEDyllgsRQ7X0KXfB_VRK_A9PDhY4mXOZrGX8tqCpqEU3G2hzmQwV48XYQTquBw5IX0m9eMfaSrL3O4TiUnfqX9GL4D2v2ypPdgQgy_KNUyWejUdexPz9DeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P480kVXUconUvMhfXcuMMN2djPu3wjSxeP7gRKK1n_I0Lr6XtrUBOR0wPljNC2p7eFc-6ncYZLuxAyCjUiQoPHXgGDyLrdDSDX25zFOiRq28p8CdaYqifVJ2ut95SjRN5e84ONJUUxPJuO8kPDrKQvPmlzFK3muVpSaysJswAoQ0Ng-TZUauNTabWFDJ08TepJ3myKl86Jz7ROWX7RjLbjOCXli508uB1vVZzf0IPp3vjYjBSOpy9DU0yqy60BPMt1LAVJdG1Kv9fGrD30fUKlqb47nqf5pnI3zticHt7n30ClSOZZJz3DSeABRZCJeucPDTyUmrksyhQZER7zPbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
بدون دانش برنامه‌نویسی و کاملا رایگان، اپلیکیشن اندروید بساز! (فعلا اپلیکیشن ساده
😁
)
⚡️
لینک‌های استفاده شده توی ویدئو:
1- خود AiStudio گوگل:
https://aistudio.google.com
2- پرامپت ساز ریک:
https://chatgpt.com/g/g-6a319e2a22648191836468df375a3763-prmpt-sz-ndrwyd
⭐️
توی این ویدئو:
1- بهتون نشون میدم که چطوری می‌تونید از یه پرامپت ساده، یه اپلیکیشن ساده با تم دلخواه تحویل بگیرید
📲
2- توی مرورگر، Emulator اندروید بالا میاریم و با اپلیکیشنمون کار می‌کنیم
🏆
3- و در نهایت، اپلیکیشن رو مستقیم روی گوشیمون نصب می‌کنیم!
📱
🤎
اسپانسر ویدئو:
خانه EB، خیریه حمایت از کودکان مبتلا به ای‌بی و بیماران پروانه‌ای:
https://ebhome.ngo
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qy9v5Jolnircvq5R-oVlWyCUSkT59HvKdR9VWylYc40DE-p7QV4KVnO6IWJkoZNlYWQSdBtOYnSOU2bTnSGEvt2NGH2HKkHhxnn2LlIT9Mv9Va1oUwgyos6WC6JZe0W02YRlsUrclXHW_pklbs_WhbFsQOfllHVwnAIKYXnuRu-fL7iuAu6aS50_ICPJqazCKxIIlV-WqndCWhE5nSE6j3NJ2PeRrzrRRQtK3nij_J4APOesV4Z6h1vQny4zSnW3X4U3nPQVokdhRuOGDcqke61_Z6Yg92aLLs87t4H_RUUTku6C7J_jW5oZ3H2poUwFxkRk7BmdigHP33ZCEY94nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f4OnUYfyZq-F501g3Tuq_XdKwbScpF8yTTtC_mZnHGpPCmVxOudore9ssKwWeX5k9ibYY6KBeA2bd8WTjNuF61HmT-4WKG-6LhrZZ86uVBalY5pbJ2PoPFNEUCFlbUE4xzAKe_ieYi2IskRJCsXWbJozGfFn-_zzCoa3mbqHVU7tH0HkkbRGlPKUriC0Ji1eDOuQLWtN_n_Y0rLMfW9CX0JzHsyKEgo5Vr-rD2ElPMDIZAUSFwXU0eQetLEENYK0wwPyKM6acjZQIY_QBGXt7ggfEc0vfmPV4P9ADvyNOfyLhCmnF0APBG7B0IAgzRNaZtpkGM2FRDNQR8bMXq5H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tksZQonw24qW-w9KpH-fiVZ6diIenp7lrFwylIl1uKpeYhv2GLJ-RuR6mUP4PRaq9hx2Saw4XtJY1h_Vij4nTduIr304Vmu0BZz2Wvryge7jHvDqPjUlMJfeKnWWcCtssIqlwa03iD5CEakAlaclOXAQwe19Sk5GmuXo_q5fTryPZoz4WysgvjB_3jfZ8JyhrboSSJGiqF4SDpC-aGJcDG6gXmTV4lztB__a5ChBXKga4UZtPMq-apCgnxMTKVbzkjbNTziRs9Fiies7cqRJORKdp4RDAzY8XkRRcWMT7JjvdRjTt0-QAmK5ktvYuFW3Boh8PnRfN-6qK5HxwQ3FSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3926">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s1mHf_bPJlYcQ46cOCvt-z3IZB7QxYRw6rXzP8aoy4KHZ1XMDbSdKKIQGIegZvEQWpJdJJh8C5ke4HbLGELB3Y37lst3ZbKIzNRsEvNIp6JmsmftWDCEwNqCsUOsWYB8O7sMpAngVoCMVIee-usvt0iVPqaI-XXVcP7GS9t45X2K8-gtsnCutY0Au1GQ-x41JyPztLAvk4dPtQvhuipv6fza4wnYZ3eKkPYxxRD1C-2h_skMTj5um-npdwkl1tGiZvWILNrbyYnXopf0uPvcQfkdg0DDisqjkZBSiMjcaA3FgNhgjKOTIcXvaY3uqflhNMhAZHEXUZKh29qHg8Bz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/naSVTt091g6U_CE4s8yEyA7RVIlsApPwwzRGglmtNCOMmnGB3FGpB5TA4dUlswsI1EH9-pSvIQnT7SAd6_AzQPqZFIa-Ar_EfEBJ2nRvNYG71KzfqTR0Uvfg-zjUh8idTXol5cYa_OtXRhoansRuvTUjW7z-1TM1tAe-cGsXndUve0I0wBCRw4wGk5aaor7QcM6povuytWrAPGfX2eaePnwz02lfgYfznYNTATASIk0wSkjEoHNsonXKdtSQ0ZxZLCXM7Xpsq-1Ib4a2Z4qGqB8mVJ4FrKGnF6ditbg_VJ9eiXDxV7Nm69sE5LHyM2JMRD58yUC7s2kLoiAKdYgWxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hmNE-sb-GeFI6B3rKoi0CLLfoBYD3R5XfhuO-FQBKIW-STqH-0uEWDKCswATUOrtQWgSYRGQ4p23a7CTlCgwCZ2JYS_-lGR_iSs7KO_lPawKoVX7zA-32nrWesT39FdtE4QnilcAPTDT55ArfDHIxkZWAsM4vDhd4Emj9_jgVNWtYuPXKRj6uG3WqFX3mF5GFG-zbal2g_QWZkKoZfFJmoVJmP0YKxzA9xAmdMj37cZk8i5NBAR8EP-3I2164ehtX-j72S93XNSCKrwa66KKQu-A0pwqV9gwZZ-j5fTZXR6KfaaioWggMMm5ujc6ggBcKsG5CuD0f0RLP02yvvqCpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MvTmjcpUdcrHDU9IuH-4Mj3ekrj7IIa2SvtcvxbxAuhU7CYykwC-UOfMUXZrOkcnclNAPH5D0dNDJL9YUofHYSvYrr5OsqSwmtwv6qgt8f8yQc-Jyrv5re2LHC5-BKykm6uR4Ge10aAMT9Yl-8AluBphHQyyLGudLWlfOb0LtE72Cl1SWFSucYo05B4CqL4klfQX13mRYSMpDPBGqkUrTJijVpFlgCTYNXQJ7LxuVeGB3P5tETpGkCvHk4p1CouJHSh8XMvozhsXclnSpUUU9ytKinY1OOjgZJ-HvkpiNw3AGWtAHztgYE7Z--SsghRLsc_fos67GhZeFK1NOpqkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u1G2TzcfxLv85Jx27HsQ_4HbmGB2Y4Sn6USZy3u2gkjDv9dwY1MNHdvn_V2s6-PI7BXgRzenUr8PMxmWQoJyL9HDczHEo561Te_0_VLYhaONqC6SNd58l68G2F0fUqkWjr5EmM4PmLdvm_y7pU7OvIWMxwpgZyiuBLbMUZzISRGZ9kJyzOMmfs5ZsZsIUh_bLQOYAcWQN7JXLkYgBEyjJM30CLr5S7pH-CgQh5pS1UT2rTXNmepSfbRzeFotPTnGGQF8jIWcKgqNgkdwhhgDLmG_0ZNQKjqAw3jvlFJTobvequlzZm3LQSvDLpv63TrZYlUnKweKX3mrcK8d0mcSPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jLbWp3zIa_FSOf3Pubz1zUn7sXaw682b6YubemvrOg3HASS8EEo_4EonbJOO5SsdmARDqekq-IKLrpDcmkJdIvmFhB84f4Lj7XjUQHs-oqInh_CuAZkIeH7kF_I40nH3KICtCn5jqEEPlviwjSJEfBQjX98gUwem_HXacj7bHzemzZ3-mrR7mYQKBs2wM61eGp9xtWg4udk4OA4vTpwFjzwUFn-TbmT04wm9445JxexD-uxhky1PalZSagl3VPcPWuHE0nD8wi7zgxeF-SrlwJFpZGYCkIYZLkYqCQZ3unlRdewcSw8pFKv63mzTXcAtz92PgauydFgelQb26DHtOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aI5rCti-NosKHgnXusCpu3NX0pQhVxh2Eit2vDahTq52d7kaPPbWsjAAto9TGonxOVdEEwUlVC1ijR11fPX6W-LAXY9C0SxVbVwYJt3Qyi3cpd9ZGyUl1OSMKrTM0Xq7M5hypvjHK-YM0WQMbdHZAQEQFc4AOmvezdZFCDI5VTBg8GyidXPqrpXIpSDb8hNsVX3cHxON1LLLOmMM0j_lmmpM25KY7fP65WbJPFNiaN0TWl5FuOnIu5bBjIdz6n2iKAQvkEh8GWOvCA0dB1BQnNURcTtPtWKfd4gNo63EikhEQIDXKFXlhEU0OCXHBN27Y89UVwIG2Fws7rE0EDb8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TfpkkEIliRkYAsec-PPT5kmaJmZyDMjEGv86QPwvyJ-2kXshLwZHsGi836HqHHiMcSXXVJOb2TjO-fooS7jrtk0ONw3-_TYRuR9wQrrSZnpUKv7egaU2mLHc11J9baJ9bDwZXKHzaJzIBA5cGsrRwSIyYm1vH5LS86bEjdb1OdlfNA19hWyX7DWwEPVRpDTsSpeS13shV0eZ0llb5UH301N8VaT5AciMx0m2GFB53VsaWIy3hGx4k3a3AxAPCDQxzjPDLi7iqv16iF7IxcYqkHtBGiQzOJkiXhKE1LwzumeKYhXkJDRwYNx4q_MmCgTSOeQWLbxi8ENkvvwxnml-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی نهان:
https://github.com/itsyebekhe/nahan
لینک اسکنر:
https://github.com/MatinSenPai/SenPaiScanner
لینک ربات ProxyIP یـ‌بـ‌خـ:
t.me/nahanproxyipbot
لینک ویدئوی اندروید:
https://youtu.be/2otJfXgNWCM
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل نهان
2- اتصال به ربات تلگرام و api کلودفلر
3- ساخت کاربر و مدیریتشون
4- رفع مشکل وارد نشدن ساب در  V2rayNG و ارور 1031 و 1101
5- اسکن آیپی تمیز با اسکنر SenPaiScanner
6- پیدا کردن و تنظیم ProxyIP بر اساس کشور یا بر اساس سرعت اتصال(توی ویدئو نشون دادم چقدر سرعتم بالا رفت برای دانلود)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از
YeBeKHe
عزیز
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(نسخه باکیفیت‌تر)
💰
دونیت</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی نسخه اولیه WhiteDNS BPB
نسخه اولیه اپلیکیشن WhiteDNS BPB منتشر شد.
این برنامه برای کسانی ساخته شده که می‌خواهند پنل BPB خودشان را راحت‌تر روی Cloudflare راه‌اندازی و مدیریت کنند، بدون اینکه لازم باشد همه مراحل را دستی و پیچیده انجام بدهند.
با این اپ می‌توانید:
✅
به حساب Cloudflare خود وصل شوید
✅
پنل BPB جدید بسازید
✅
پنل‌های ساخته‌شده را داخل خود اپ ببینید و مدیریت کنید
✅
پنل BPB را با مرورگر داخلی اپ باز کنید
✅
لینک‌های سابسکریپشن مختلف پنل را ببینید
✅
سابسکریپشن‌ها را کپی یا مستقیم وارد بخش VPN کنید
✅
کانفیگ‌ها را تست کنید
✅
از داخل اپ به VPN وصل شوید
✅
لاگ‌ها و وضعیت اتصال را بررسی کنید
در این نسخه تلاش شده همه چیز ساده و مرحله‌به‌مرحله باشد؛ از اتصال Cloudflare گرفته تا ساخت پنل، گرفتن سابسکریپشن و اتصال VPN.
اپلیکیشن هنوز در نسخه اولیه است، پس ممکن است در بعضی دستگاه‌ها یا شرایط خاص نیاز به بهبود داشته باشد. اگر مشکلی دیدید یا پیشنهادی داشتید، خوشحال می‌شویم گزارش کنید تا نسخه‌های بعدی بهتر و کامل‌تر شوند.
WhiteDNS BPB v1.0.0
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g5qIfVzTJqaVWShYs6z9enGrd-wQ-OXFvKEsCLu_EfMOfbfUDUyFciTQZiIy-LocvYVZS23q-WYSNCcxNRhyNW0dsArJC9dnzUXrO8NWFnN0jgmD5YaDIMA-0rDfq8Ua2ASjOPpEiXO5QfUF2u3BR6ASb38NF11KKiJmTELCRDfUKT1RHH5t3R86OI8k8LVAvexH0rGcGZuSvW3VZqYXmUwbIaFA_M9NBN2i2vo-xqLgqECnVh7CiMLSYPAMHHim0PPKPr93oZCg2f2-XX_AlsRGpSnwdhaMfMto04KWOtMk8f0VTdoonjhbugIN6uCy_ziW2CG23N3-pryUUFMFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GuwOwwTVo_RqzAzyxp8sAxe0WjdSTdHKrBizqx6p2OnueYJBDJv2eJB--i2XYKzN9AHs5zJUVKN46BBDUGJoDei7OHnJcSaLkE5nQuSMQbyZehjR-yeoygABtvzRoIQDqcw05emggp8tSfbjZ5CjaUsjnjkR7RuObC4fMlDNflykvCZSBa863cu3S8efs2lF4BhRHiiCEHojYajGbwNAK02KPubQt6_q8mGmlaEwkbT6Y-ZezH-hy4XG064pnT2IpOhosAb_hfoyPEL6duoHY0CHaxzxr_D0l4zXaiuXy_PgWd9KNzdutIUhY_9t808DTITdIlXXt62c8tEqNY7X6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DngS6SPe0m_9L2_lvPuZWSoxz4rvAld2boSTus6lHrzHYwgdNZvZBZ81iOehPH0qKHrwXnBP-89WY7fnck8eK8ahtlXtYMh29lEWH92L3TGXlIhAYdxpLwfJTs6jR0Hx-bP8sn7AaGolTt5KFjMJU_mamD4zR3PxkN3IR_exoNWi_YmVk0DhD_FP1pT1-tXymKs0hZ0duWKoLWmvlynCcN0PIc87my9L15QVK059YVk_s_bdYrigGkszc7aVg_z_s_o30HJFkblpZka9e6leGeSGwAfuD3stVs2vNSKMfTO5PaWfblbGu2AC4K8wrnaj2DQP2CdeICznf65BB9QsJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HH2pOgqBMFZ2iGC5yo8HMcnPG7JyaKJUxOwIydRNNCYxMUqSPANeCJb47T_9zyaH8Don0_4XECJ-BaiUD5cZleU57bemmJM4xrd8TSD60fxy3m57BVs6npvBlQny_Rh8g4siScjjv08DWYart4hB8f9arcbuYMbIqxDbAtRPafNUxVc0lk3YB3YwCMTDAfvtjXvL2hv9cy71zXa7xRzs3dvHS1_2oYFYsFpuMNVp5fdoDwKfgWcok4uQTLR47nbvt537GJN78pioFDLi64H4C5A_JkboiFu2JNoYWs6sFnqwjwlbadmjUmZcHbF6cZgJHj-0S3zf_ACAxQwEbq92pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PEvM5fvBqrQMxo08yaN49JHqloW0pW_q8y4Bsw_phs__Ks46YYeZtPof8YC54GJJ-4ocdM0olS4BFuJy_c4tHG6Jy8PBPZuQh1xjT3Y81vMMjHCeKq5_idWzaLI4qGLg3XKzRoYTxHrko0_1pFKEeAvCHBgUAMdQ58MB_zKLyEsPSgDjb5aKPLNE6OzkmPHjoUC-zmVwPY1tCFOR3jBdiCVkk2H7_Eu0Z5tL8_P8xhlVxoRJ3OyKM57TjA--bkuVN4wUoq5a6O2axa1Qi4f7F56LrAsKWm01p-pU3Bn_o3F_VqOvT1D0HsFq70o5r_DuV08604NzdHGY4wkgHaJXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HE6x-FsClzzlK6CLjKyfumsVQZCqVDCIc1vgaOeh-tVVrm-YNr_IkpXIDAeUyjcJhViWAc2qR4xOozPnEwvEJVMi3TqyO4oSVfOUZ3YwNon-Fkv1wpgXgb-EkQgjjB35MK5DMA7_VWfY0z8kVTLJNQ1f-oBuHoG5fJci_jB2iVZ-OsZfBbeddreP02TV-R-mCWV_J4jJ64szoOJLvNIpJIy2jlIV8uzgKnGwz6Nko_5Zof3-tymIZJo5ZuIDfJ5Q6ONcNC2hgYW6O5cSEmcL27dEU_8bOcaJyUauYs3V2mKamQ2a5_dCFzAFKz9hM6sMjbmVXBG8Xyq3JpM_yTGF0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlBCnkUsimz1pCRU1gxmBhiK43009MCYtMJEiIBSxiV9GO_NDb-ytiLUcoZmOj94UHO1YLdhtn3OxiN4T1rxam9HfdnUaTQrppOr0u3IJu6ux8z0xeXhmqh4Q4NYJERmZsNzB63aPfwYEaJs3ZyZMboP73taRIbkhVJfCH_tJMDj-X5UbQygYnkkGtHoIJFM_qcDDcc5KgaXqmyjYlLJ7n6G6aGbJSjj0FtCkf-5FBCeE1eyWbTXinejRdEPf0xb8Ov8JMBaDvQX2BQOvlihEeT-GIY6mvULTbBce4nwBVtc9zw4-AZwjOWT31ICr6lPBYUgQXf58Jr7vGUTCeQC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BFfVmcF1ZeElG1dHmL2YriHOwJGwGq5gWtsILkIrKt8Uu4aSZJgUEC_ZxTc_WBO_UH8Yo5-bqWNW-NtAUUDicWxAZ0IlNtNu9_VNO1Hujo6AsoXHm28DgGxjekhXmn0UrrDvvi-mnRQy6b31H-k3D4tBwGX6eqDBiVDP-R9CJxjiJFcz49Q1QEA1lS2ddVdIMInf1JyVx_OQ9dS_mHzajHwXBltONczvatqm94zlKiAGOQ1VAJdYlNx55KYgZ089APUhDfB21Lpu8t_7LlQSZBDdC9zoK98eUBY9Iaw0k913YIOHHpNjAeFMzn-R7-udeYHd4sTDAJFpQ85ZZVpOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ow7mGVWtza_rPeVx6P1FGRWOto0fDSBVED7Zh3R8vUPCL-3UsIK922MFYA-viaeWu7r78Pqf01lJ3fj1M_ycrlqCbvz2cuITNAn26zNIyraL-iVbbI5XdNXa3jkzmsdEHv1wdnZ5cbZYQrV7wo2vZPwGmFtWGJidJMukFTcpnssb74B7BMVrECysF3h8bsvFv9UJDmFgu9GemPcSiFViXitfQL4PRAosO8KtZsSQjAbPF_DqEFL9HP-cKvsSCKkJTYvMZtYMrZLjRVp_DhsRWs9YGVEEEFO6SVLHEvPa2KBFvKdYQx84tugxe_SvWDiQP951uzKK6DAuJ_63LavtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AVUxKKRbdCsso6Lkxfgirqqq28l-GXIPSgI2AGwJvzB0bO6EbolIKmUGmLGe7zxgPdxtOdOkjSdXuQL4H7X4YpOC19ViueoFFExRK2t6Q8qEBuNF4pytr39akXeobzLNRwq4ppI0lDJA8cUjLesA82koEvoyEd4zB-sI5QQqy8lj_8nntWQKqjxxKAeax7BmoXYXmeKpDDNUPb4WN-BOV6KhTdL2oRBRN1xLCcGOrXZyZ5hZuumqs3qmBGO0lO_EbQhdtUh4243tzeNOIji4nXXd8ARkFiJsnVWtw4_ZYYBg4aQfrdTA6qwbkroDU7uFBGc83zpB_Vzmq9GOxgG0YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m5FKMQW3syp0LaPLKkCKxap6vx4zAk3rLCtY5yNqHFWZ-hD1M4nS5-vc6O9ANaH4VcvNa-s2vL0b2YtFBElj2Sou_8RCsCR5jlJXfP-XkDzgE2w8SlCs0pqTK_HaDX-JtiskwyVLZFSohhzcUzDkkgHtn_4dUgj3KMLA6Fl5mG8ZV3Acvz2k1wHBg-1NxB7UvWXxbKSLvYHMT0POc1wX3fYi9eoRD3o2_SZPz0kM0cpzWAU13l9bd3y0MirbtRFL0oP6SsmkXw_ORh4PvnbD-lsQmCcVAWYS6In6vdvZRrI0XNd50InlV51NUNFPw6NKJNWiqNT3TkttxOsF-zmBzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QNbXFOAd-36E9yUICuMllpvqkn_EA8p9stc_6Q4j4Fo6TfML3fkUm_cnwNytFCotK5hY9u6WYGULNvcJlmfZZb6ndnnXl23nBasMEO-kOsGkKrJFv4e_ZoKAjd1KRMLJ3tL0ba2RX85zmWcSiAoVmcHW3uRlzt6-jcJYGow0rDQml2RaafvdyHwo2Tua1lah0e9jII4ZXiik3bYjvkrSLXAvBdP2arJX3EIGe5tb-ZsJdyd6Ks1jv_hVY4jGRbj0Sf0iReFpecNrjWKBCmsmZY5A00U9YhwqVEtBm6GlZnVhEc6c-Gsnjwm9vXJnzd2unQ_GbGR4IBAks1kfSmbmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پروژه‌ی جالب دیدم به اسم SurfSense، که بهش می‌گن جایگزین اوپن سورس NotebookLM
📞
اگه از NotebookLM میاید، باید بگم که SurfSense همون کارو می‌کنه؛ صرفا با کنترل کامل دست خودتون. خلاصه بخوام بگم، یه agent تحقیقاتی اوپن‌سورس و با تمرکز روی حریم خصوصیه که شبیه به کار NotebookLM رو انجام میده.
👍
مزایا نسبت به NotebookLM:
• اتصال به ۲۵+ منبع: گوگل درایو، Notion، Slack، YouTube، GitHub و افزونه‌ی مرورگر برای ذخیره‌ی هر صفحه‌ای (حتی پشت لاگین)
• آزادی انتخاب مدل: ۱۰۰+ مدل از طریق LiteLLM، یا اجرای کاملاً لوکال با Ollama و vLLM
• بدون محدودیت داده: هیچ سقفی روی تعداد منبع و نوت‌بوک نیست، و دیتا روی سرور(یا سیستم) خودت می‌مونه
• جستجوی بهتر: RAG دومرحله‌ای در برابر سرچ تک‌مرحله‌ای NotebookLM
• قابلیت‌های تیمی جالب: به شما رول‌های Owner/Admin/Editor/Viewer میده + چت و کامنت و...
• تولید پادکستا بدون محدودیته
😭
معایب:
• نصبش هلو برو توی گلو نیست واقعا. رو اعصابه — باید با dependency، API key و فایل‌های Env کلنجار برید
• هنوز کاملاً production-ready نیست و در حال توسعه‌ی فعاله
• باید خودت میزبانی و نگهداری کنی؛ طبیعتا که راحتی NotebookLM رو نداره
#️⃣
جمع‌بندی:
صادقانه بگم، NotebookLM همچنان ساده‌تر و آماده‌تره ولی کاملاً بسته‌ست. SurfSense سخت‌تر راه میفته ولی دیتا و انتخاب مدل کاملاً دست خودته. اگه با self-hosting و سرور هم بخواید پیش برید، به درد بخورترینه.
🔗
ریپوی اصلی:
github.com/MODSetter/SurfSense
آدرس خود وبسایتش برای دانلود مستقیم نرم‌افزار:
https://www.surfsense.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CDtjBrJVT-ibMLC1PQABFcw0Q6FMW5hi-_cBuM7e2LIkSbxfaMwaiLJo4xKraMdpwgIyR_hs4jcYYENb1mnLeeRb3_bARuiy5Tkl3afI8TYYZxiA1NiHnm3xGOzEfYgy4Tb89Tw4euGSkTfQEmtlyZ3Ye7-4qK96As0ZnAAM50poUe9-85GYCez-JbqFHvLDE5uTWTRlDvD9iQvauEKkYWFVNYD81GInqQ6B6DEkiPwTNzLvMXxWCshL9O-D-__zpsjsw_eD2ZBLHXn_lXtezN3jWuB2tso_MoSrzmat1C6zPJeZPlxhFenyFR0jTJTaGg3Tx2LCJ3tAghNpzQw7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wvo23ANIgr5AOiWXNJWKuSGXA0glZPTfmwgl2xL_UkTStaLmfkPi6wsEmKba-ygWmg_daShsyv33k5NcsqFfJ9eqE_Oj00Ra4aQbssueojWX5GBSmBtXZtR9N3ClRvT0gaZwEAoKGMlIBn2Bewr7o-d7JQmOPp82EZFAfoZgEO_OJxs9l1at3Mx8HR1d91FvYtNronV_QydgOOpQiN7y9_xuDR7FyU-Y3oN5I5p4P6Zp5wx3Rd2A7NTSmmIoiA-zukbbrvzP_G_aQtMxeut1VYM5T9ZE9P08gapkQ60KUjw1KewDWj_aCZAzzCZvNjP0Ek1q91pdXsiRuNTLH2epQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FnlohJW_Zv2d2kROvR_ZawxXM9L6Qt2WZ4MTIsdxkRil6LJoVLDTuyacIBqIgMa6PRZIZ08UxaZdWdPZiJyfFLl-uWFekrkjTaHZo1OAktDdrtwBQvg1w2OIS_hTsq6WHbsm_hN7EIbcvKeESy821e9QucO7ZmVZ9et03G7PzpIUHRm5zE7Y0Eq5aL4_o5711v5myNoE54LoRJajzrbqm53eNX-svX2Qr1R24BR9rNgghY9VX-VDdewYIJlQ2SmOOzJd2fhQwz3FPrQaB6UwwZlN3qkTw_nGq1haosGK9cxns7fUsGI0lQaSE3KFcMHrSj4llPRU-OiFWyFlivfbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fpXK7bVUTypWX7CgXKI-_e3vcKhn2uYg4E7nrxaN9RMk3qG6sT4JyzC2h88vU9voaV6TiKhNScq8U4V-R4rgf2j43IBO2qoIh8d5aWXmqJi-FWsLX3qVMPmFKi_jf0NqmTK5b1JHU1ufwCA-TBzxW3Bunb6YLgFuy_3U9Vsbqi7Zm5JTTvQkHvUhEGJ_dpa6JvnySlKoDhPAmWMSMWFVCXCjAS6jHoeo1S2J_slyZtYhsKVz90o7z-ESKnT4ktjGLYWigFFYeh6sDM2vbMdjD_eSbcvj_xhGDNF6wezWEgXfznkDOLo0s-MuVHpucqUnhQzM5qK1e_JTbCmjLz1N8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RDyOog2wJ8CxzbFwKtqBgRhE4qLRk--L4NMDxO5bpHzAXFS1BYXQP7982LinojzQhCCvz4ZdZ73O-_lLN1p0wCfyWRjoGDddwsnavoRc_Gxew7CsQffiyL80KKx2L9oXXnMGAgS9gKecFSPJAmv02vEeNACGSwahR68Npt3VoFZXaOe2Kiz_fvv-4GswAJtVlsTXL0Q_h8pzJQb41lwLCfik4x2vbjSbjrtMA2OnVQyCtfKmhpSDOkczF2EO4FYiPx3ybOPM3ytjT5U883VR4Z1GzOf6wsTJJDVPu7IjUPXz956j-QKvW-pr-wCz_MXT29VhCcxzN7z2Tnow-L1ORQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mW8Rarp5rJhR5W4GsxFUvLy-TPMFpueOdPWq3lIwWT9KLjEsBg_u6Bkh16seL-YXozp6l_5VX0VCMKBzwPBiMnc5TGN37wa-gU5oVQEnTPLKIMVSIkylrLay_cOXcTuWVWD7e_41Of5EA9_mYfv-wp3n0F0LBl1GkQFMX1Qc6Y6qpCzX_8L27lr4-7cUIZXpmIRPCpvf2zJN0fdEMQCDeMx-nHaMqkrukMdr_B-vaOFE9sHxHr7PUc8hqq1aWPr1UGSoDXu8aPQCnuQPR6NBIA-9qmH6kpwks934tC0JFwua2YpKd54LDcIec63uJ1u7sUINN_feY0VYw_YEAc-ktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMy4Hfi4KqwUD3Fgy8sB0yWoz_HPMvpX-EqcqZooLfVynirp7HaakFW7uJNbes_K1uYcPDlS0rH2boIU6AwNHjgdNfV54aKiCNtaidRx1pFbw85D73ynmZO_7FrF-Zo0au-2xUQEmoIDApsvUv0dc-yRLAAe3k_H5pnS3P-lk5GAodrjf3H1qfpC8BRkQlxivfnEBbmGxV7DNp-VfxZBYkk2Kglijv2bWjPx85554uuvr9XF7JFBKfIBZ1fBDApt3SiO8EUGsPH8c7AACH8In1CvhJknmy7aMXt8mT_tw6MtIQ-J6y4XK_lqK_8ye_oovd9lqyFTKP7-iViwTK_kRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hsBfiSpFKLf_ZrX0RGwkmfez0BEFeb3IuwZ0CelZ6JFmpLWBtFlIeQ2vINUIavbwg5kIaxd1-1u7iEmbCaarziJ7QhV_pagEgeqv91gKWHv2iilZQl-V2yZM4VL0TwKaxGXHDNQ0DVvn4E9Q37DMtebhsVQGROq35wbLofhJOX6uBEWaliGmcc1bISOZ5I6toaPQFdXTBE-fZUaqONocdX_xaSwZnboKNR1Vg7WLhbImQ61A_K3lrC2adpA86XOcT5DBVw1bXv7J9R0XfoahUnexebr1pG-1nTcsPIGTR64zet2CbSZj4pgnJLooVOgtiN88Z4vD_mOkMdmrv_Diqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cdCw1URCXNQAz9MrxELR4ecXtUMF9qkUSyvQ-z7M0kelLHGrw2qunRmPyCV9O2tRR-cTB0L-zOUvVQ1kaWNMxXeZ1iVAPMUTThW0UeWCHz2NGQQuFJi2FstUuAyQCYJJ7XIp25P80yI5wL1V5FMxf6WuJWQESJxNardP9YSvP93097LhYGdkDH1wcrxiuteOD3pQvBbrjVja0HepNQuppCoPGEXseGH8uoWoKDN4UkO1rUQc71YxUgpxOs4BkYo-eL1qR3GX1rgSicZ37z-idClIq9P9w-HgO754mSWh9HOGXabwUNjGdUOEzFmMQlxH_1z5umCUiNCe0xPpQ6WdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j2097eAwWgGGUroODBB84vt2Gz39wGvB6zuIBi6vpDjMmXmZU_hsNy2g8mwNJOBEvcZ3OSxgh4ppoBaYh21Kex97EY_AyQM49Bq3v2KyetPDyMLb4_ZUhmgisEFJgLBbqN1O8-pIeSX0cyLiFt1yeY-FItekMbOCjQn6buZ6YNee89SrwBOeFiv0ziUqNRiES7kr394onDui5p1IPFqDwY3ms7nq726AR8wKhQImu3WUsvLM3oZYDjUz8nTb9xZi9-7X_sAsAaWS6RzikvipuWEqgWrQ9eyLxXmzsaYo0858_f8VKhDtJSfpJZr6Uj86ZjeWP7QaKCKdihp6bIUHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kMKdmccy8BGpshx9Wb0-Tp2-UN178S7Udaz5srCWlnhaUkNV7PWW554Hv0QXUXWj7EdxFH0KWPxVimotVCv7z6knY1GCOs6WXIEIk6NSLeY-afjgl7GgOahxrPP_NIq_fFdx7vIxxwPVdLOmDhp5_yB3JqCgzc-HpYrlrnBxHCAt4KftyPnXe8CP2E9j1mt_vxECaENrnqsWYwC-k7KOxg7ldFcoa9WSTwm_oSLuZUy1Q0gclZVMjfUkbfsyg-LxUUFA_dnnVYRueF6M3tem7RVeYwOvPOzWFAuU__9nQIcuzJZlO1TZP3IHsNGSERjppHPmyQDykSVDp88rqN7YtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sd56Fge1cVXe0uuSvb9DaQc62wfnNOJW9nNW5Zg1v-D1u-glIsMo8Up6FBhEfxToLSuR64t8WR_s0cfsbyAupEL-ZfnFCFQyq2twPRvuXrz6_apM0x2pxvZSpH1fzM05YGFEVBo34DHmb0hS_d3QY12Mnz7gBy00xz5qRq2XPGEzQ3D7IhLr-cs3FSpm7u7MTtWNgCS9evOkDk1aHpwLVKC9XFCTJxYET1S8XPSnX2qxzduu_wX_0x93kRhA2S5c_yr-Bo1GUpVyMhcYCrHX8Xk-24qf_Jg355RXHxKBDw0f-E7kZvwB77u8sRNwHEYhKhBZMdfVOnBccX_2MAq8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mZ-Md_CFQXqaPPg6Cka75vNFH_9dd8scUqiB8E9CLJ6xO9_I0FTxiOLjwMMPFWlioTuARNEIEV8DDJh6A5Zo8s4rpa3-AvRiVFphALT6R_zwA7890mhLy3P9Qaqnfg1Dkx5rZ3TSjZQB-a60Yw9EglhN1vxTIkONL4n63iwPBl_jesMamYJUkG-vsotv07ZJlGyZQAWGn3GMtpZYF2ni6PZCWIUdYHEFQa_zyXuPRync3NfkkB_nJYzoHOa2JzYtXSqMVxpm66M4k0RIfEdCPTV2HHMqxPxAVjY2wTVPcmgMyE99-ynpe10G2m_t2ZGWNCfYq5m3pzUJVhY8oWHn2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iIT0ulHFkLpMByW1HknNELOasq_fl2btJy5dSKa7IoHzJakF7pktDED2XSg2tCTup8nAsTNuEorZvyVstZhzbdMiEfd5v9t3mdmBdQZjEA7Z0NfwGWRAro5cVEBMSDRZ7mMbpzBpb_gvayHI-HBEllXsBwUnjLv9R4DIZ3qrulR7Uys5O0XLM5h5zEDajNMeNrNz77oOQnLIisyBrKTA8jzsvfFcUMivmFpn8mySBFFUJ-wdYNUgBQgcZHmuGrXHLwagEC0xWbz73x5q6UcGfBbOPjb8HDc6r_dhoKQAS4EeJHbWa9Jeoj0Zyik-T46ZekrEmZn0g1p46Z0LDkPsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J4ACyOSUcv11u3pNYX2S1dy5LeMKseywh878qKi30eJZVaKsv6uQv_sk-2IfrK-bpxKSnNm105heuqPuAaOLWBEDMYp8FQIsuyd71kmNoqCr3NsYJvMrNnBji1u7PfmHv7Nd72fUu88q4iIhhIgyS3jrZQXv-kjvSXlEvW3h1WSXWXN8CiuroqmakmnUJJDzTwWdI9ooTa3WwK131cj2Da-TP4jdvfSmOPmNXkNVUF4r3gZf7vwH93vAEnRHUMd0CGmhqj92SVHTAF_r9B6gbh_iI6V8X3rtkF2pn2JFweHk4kT2k__IfKFeZ_8-ppu7A7u6mYKu6DHrgHUW-QdXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tE9eqXWkz1t9ayQJMueMzy6kN9G-5MNElgv5AtrENWBMZP_UnBAylKGLIg89FpTM1SVy0Ne37K7_ngHbgpIctFXtvaxywyCzfIUREwLcNv0kEA-srFw5wugfqz1ZktmvcnZYmJLvXOIlPAOhFB9nIwTrNc2wHyvkpVg1Eq-ypNujVt0QvGpkkD5DCMJaUiOeMTUAp1UFeQOAaFbXdvZiV1dhmp25F-ngGJYE250lVf7XgDg86THo8pnOG4Z-eEDXILuWqNPqYjFUO6JwtdrwJPLisRnp49WowMFq2DnH3bksm3F99sMSQDXq4VANNoKBb0TvBFM2aUpeehieWZ9BxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jBvhynSDU2YHGxL5ytjLZ45rjDOPrPr_AJzEQXbyGvoGindoil9yx35Wbb-t_2AeGT12GGSDDA56e6IIprV-Q-075RZP4QIP34nq3gf5a6zcwOoTUugD-YT88ZztYaSx7GnqVG89Lhjsyvy2edC57EJjQX8ryffGgse7mDNNjpOpD6z82QM2cCmiEZ7D6Gd9Gsuim5u3gDwbwSJha6AFXif8zMO9Z2DsjmLyzyIrM9Q-NBSOwiVjtKLIVqv-NG_wNbuURO1xivHrwfqwGfcpn4Rc8APKFwlz8uq2oHagP1wVlel2K9B7ZKN3V_K9ypu2UnSc9rI41dXMwkNKjgFAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
