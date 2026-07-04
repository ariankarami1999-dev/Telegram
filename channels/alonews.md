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
<img src="https://cdn4.telesco.pe/file/S3IdUroGKnTseHkP9ZLAZKAWQvGTbB9RI1irxMNz9_cnkg9iA97KLB-GBZGZwSj2vT6SUuQQV8T-tybNH2Cytf_LxZ0l8jqoJfJInd_Bf_ZWENIiYgntSi0jZEJBC9LPG-9hMIbpgMWnSzaRiUY5tZY0XuBH728vLdx4mvecXYNqgajYbt6YpXz08nW0y4IC071Hx1fXnMCwHOOD2O9peum64VA8s6UpMlNUlS8sFFouElzgLba0kpH7KnRFcAW25sPbGkMKS90dHZNDUtzb6h76FrwGAd8hjZ1EmSt_PsZNRtP7RaL2WC247Udx97RDiw_Bc7fYQpDfSw1999iRiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 21:27:15</div>
<hr>

<div class="tg-post" id="msg-131793">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ادعای کانال ۱۵ اسرائیل: منابع مطلع فاش کردند که ارتش اسرائیل آماده است تا یک مقر و سنگر مستحکم حزب‌الله در منطقه «علی طاهر» را مورد تهاجم قرار دهد، اما این عملیات با دستور مستقیم نتانیاهو متوقف شده است.
🔴
این تصمیم در پاسخ به درخواست رئیس‌جمهور آمریکا، دونالد ترامپ، گرفته شده است؛ کسی که «در حال حاضر نمی‌خواهد در لبنان انفجارهایی رخ دهد»، تا مذاکرات حساسی که او با ایران در جریان دارد دچار اختلال نشود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/131793" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131792">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfVZG0DyavFRgltXoikjQQeIDEBifsothvsV-1-zcDdqsvKLElbWlaJQzmMt5aA4ESb_1pQ6wdwZH9krcaCZt2wuLBnd_g0WjtAYbI0fwtP5ersW8OyWQdarWjC2ZEKvingzcWJYSxFML5smKcNxo-8KIJVsnxMl5ZAY_wXH142FTxsbtlN5Qu5ubWTujKpSYnx9Lrc4H_ittoDojSvOaH7sHSdQCcGeZBccLHMQ2Y7C_-GSA77nJOjwfGmUowtOO-nLjGj_TWqV-LXySvd1cWZvvwdxXOzftFGYVQzewH_pgB5lZaFmBlB4OoeJ1I1i771Z-3f8zaMZ73apCcWDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/131792" target="_blank">📅 21:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131791">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
آکسیوس: بسیاری از نزدیک‌ترین مشاوران ترامپ معتقدند که «بنیامین نتانیاهو» در همه چیز اشتباه می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/131791" target="_blank">📅 21:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131790">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نتانیاهو : ۲۵۰ سالگی آمریکا رو به ترامپ تبریک میگم
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/131790" target="_blank">📅 21:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131789">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
انصارالله یمن : با حضور تو تهران، محاصره دشمن رو شکست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/131789" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131788">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: بنیامین نتانیاهو درخواست ملاقات در کاخ سفید را داده است که می‌تواند اوایل هفته آینده انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/131788" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131787">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
العربیه: هیئت ایرانی شامل قالیباف و عراقچی بعد از مراسم برای ادامع مذاکرات به پاکستان خواهند رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/131787" target="_blank">📅 20:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131786">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
اکسیوس : ترامپ می‌گوید که ایران «می‌خواهد به توافق برسد» اما گفت که هر دو طرف توافق کرده‌اند که مذاکرات هسته‌ای را به مدت یک هفته متوقف کنند تا وقایع مربوط به تشییع پیکر  رهبرشان به پایان برسد.
🔴
او افزود که هیچ یک از طرفین در طول این توقف به دیگری حمله نخواهد کرد.
🔴
ترامپ :  از دیدن گریه مردم ایران در تشییع آیت‌الله خامنه‌ای غافلگیر شدم؛ چراکه فکر می‌کردم مردم از او متنفر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131786" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131785">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY7lh2KSVcD2YAaTaIsXejiY15l1V-a80WSJdTgLr2_IBeOHMsKpuQ__lkpuEFWPLCP_rTZxZRz5XN3P0oTG-TUzuEbnaKSk1bYKJwAhC-i__8CtNqNg1Kp9KC2JgCYHJ3P4VZ_5lUKlI-loCnkHD8by5dZIMHuj4rpRwECUzG6xfWuS0EM1Lk_bxl979e0xVYoV3vxu9whJINixFzroK-5nOPBzeYTWcULrl6LhXvMwv9-lXriErQQbW2LE457745AA0x1rsbYTWscgsexyeTDakkcvdWniiKLeiyaW55O3VDZU2LfTfmFrcYfL3xeNnw7xmiDMCtnfijzPqXsMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قبلیه بنی مطر یمن علیه آمریکا و اسرائیل اعلان جنگ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/131785" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131784">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HzhGzfoL_9Wtu1H89HJX2pUbSw7WqPLLAOHA-nzde6LqKMU6F8KP6Kl9fYbTBeJcSdRl1was-27akAN5EwAf2ZYS3hMkLbu9DmhxRzNyo8PI7mzo1RIA1-E6zZx_VijPWa8vlwmcpCs7tT_fiqWQaY78MMrO4JAhawm4C0xlBeI05kDjQrljj_IsP2fkYqouuZvEBTSAFvupykzUDyRoUaVAZ9ZZGdjYKu2b3QK9K4ml6eJvA_-hfyXK5_WNOy0WyZDJ9DUGk2fH2i_0NIRKpzMoxM0T9RvyD_l3kO0iaXA78_xxHCrgLubuKLnMHpnK9I6pimMULhhtHu2brgJ-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ُ
👈
ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/131784" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131783">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رئیس‌جمهور عراق:عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/131783" target="_blank">📅 20:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131782">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c668b6cf80.mp4?token=lZ-YbrEUE_vD-zreCp5OLB6aiyyibcs0LVgZjhoLBHljeEkcGue7A9fA7fQPZQMxtmVl7Uk2qU9ygdYxapKh9ZoTUyyp4W1V6J2ATXDDhhVrFhAgCCd59unT3cp34vHIhSfxXPCNtOibIDHNfPdWmzrxuurSIGlDyMiLLOjXB6EeaSPaDHf8qcE-3EcLEgL74sgB-xtN4zagwm3IrZQHJhoQmV2bU5FNh1W8kMGJdjCgOzG2PN4i5JOoltZPQNsXfXWsNCv_RzLphQcoDz9d0SP4ZUts4L1CFWmDA5w0qOLvCRcn6EEPH2ajiMPCvaa_-rJEOAbCizEv7ZLkgUIzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c668b6cf80.mp4?token=lZ-YbrEUE_vD-zreCp5OLB6aiyyibcs0LVgZjhoLBHljeEkcGue7A9fA7fQPZQMxtmVl7Uk2qU9ygdYxapKh9ZoTUyyp4W1V6J2ATXDDhhVrFhAgCCd59unT3cp34vHIhSfxXPCNtOibIDHNfPdWmzrxuurSIGlDyMiLLOjXB6EeaSPaDHf8qcE-3EcLEgL74sgB-xtN4zagwm3IrZQHJhoQmV2bU5FNh1W8kMGJdjCgOzG2PN4i5JOoltZPQNsXfXWsNCv_RzLphQcoDz9d0SP4ZUts4L1CFWmDA5w0qOLvCRcn6EEPH2ajiMPCvaa_-rJEOAbCizEv7ZLkgUIzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت مترو بهشتی تهران: شعار مرگ بر اسراییل
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131782" target="_blank">📅 20:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131781">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
به‌دلیل افزایش ازدحام جمعیت، از ساعاتی پیش قطارهای مترو در ایستگاه مصلی توقف نمی‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131781" target="_blank">📅 20:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131780">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
پزشکیان:
اسرائیل به همه کشورهای منطقه حمله کرد و عامل بی‌ثباتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131780" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131779">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سفیر جمهوری اسلامی در چین:  پکن از تسهیلات ویژه‌ ای در تنگه هرمز برخوردار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131779" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131778">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcLdwhd1ZO2c0NO0q7QD7faXyaXwNZ1BLMyb75bCbiLSpib0KSI4GcimuVTYB5ZYU-EBZQoXuM_PguQ3ukbjB2iX2UDLSTUaZEMBkOjvz1WEvhHfzKw8Ex459KXUXXQtqt-QF4-s7ydBwRLAY169osFzLCl3M9obHtvSjqvW10Zk-3WVBqVkYOaMxrIeU5cWi7MafW6InMK0jz-ynw-b1UsaH-pZFWoU7Anx1Ju5hX3qa-NgD-0z0G2Uc8k_N6p4HbBmUuGx7fSFM0eR5IkKDOJrf4-LqAqP21XYO8Tnd83v8y-l4QKAUwZePdd1d4C-VfcBkye7-n1XLijiZjOIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا گوشی آیفون علی نعمتی در مراسم استقبال در فرودگاه توسط حامیان حکومت  دزدیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131778" target="_blank">📅 19:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131777">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNDZECTpRZWan7hPuzEM8ZiZJ-PAnI7bPgHq-2Jxh4OUDGBNH01CxdO9QC7pPGMDAEjiLutzm8vZSnJE5c648ML_HN6g4s_7uDgtTe-CfIZWTAH3RfsO93FaK7wxozkjQKOMJt_DcGQFvaDcDYPQw8t1rlWFh1iXEnDd9URVJVyf-qKgm2zyV1if3RtfEXo7Z3kBzvF22oHUGG8NZyUxs9moTssvSnRGl82c66ry-iu9N5j_yj7dorQHIEp7H4Nk5INUN-P-NXLzLLUWWXDmAMBfPVZP8vZNvy5Y9ubFw-sA7ldZmV7QELYOhiW-YTnoCE8ntxBVA4asmJ3tHeBeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
مردم برای یه لحظه هم موضوع انتقام خون رهبر شهید انقلاب رو رها نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131777" target="_blank">📅 18:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131776">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfMcuHkCA0LsvgURfrpZiIUveH34TzUZik0TQf9PTfle0z659kns7NSqOCT6PziNDr8FnFw5FQZoBzEASyjvhn9RzllW01RoydaGpavRyHsrPoQmXSFbVSkRTvmGzjfvHXSapJ25nxNvm8oErCcufR9Ccra02nenPprqB1laPPzCiSTlM541_K1OQgiDPfNYXgN-4JoqzOm9ndfbXDeQUZi8ji43qp4IwNzHshj5qZS0iZO2EbyB3j0Juql0kxY1M15vyyk9sSqZ_V6rOfid4TOTsHsWJ7B9_XiVvIKIjEe0E8uGKorHxIN_R9ZjzQLtiyruTE4Rr4w-Z4jkrNEGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌ها اعلام کردند که یک فروند بالگرد MH-60S Seahawk نیروی دریایی آمریکا که از ناو هواپیمابر USS George H.W. Bush به پرواز درآمده بود، در روز چهارشنبه در شمال اقیانوس هند سقوط کرده و یک خدمه از چهار خدمه‌ی آن مفقود شده و تا به امروز پیدا نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131776" target="_blank">📅 18:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131775">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb289f43ad.mp4?token=er2TBsep6_AsI1tZhcJNPEX5uNzRFy1Zwf2CA0I_wgIk0eviskjpYiItroZ9EcIVP69KLxrFKTzq1gqPlMGpvVQShAh1dhJ-SJezdxl5Qr-D6MXjvThm-rmcXji27xxjaQDaTQYe3yRjh6xJsord0jfBVeAqMK_kjbuVT6mkixf3obcwewH3EfayhXGKzYnjufUsuZqB8wc0URRAoG5wdX3FPcKj7GUkWFwR7rBPW4TwWal14ZXlEb9weY5T6JOEr13AANlnlwl0hvQ0igGkLsCEDAccFfpd6bQeyKNFJ8o8BsQsEwP0ojwXbdidq8BBTws70Nbo6xCEOkxcVPJVMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb289f43ad.mp4?token=er2TBsep6_AsI1tZhcJNPEX5uNzRFy1Zwf2CA0I_wgIk0eviskjpYiItroZ9EcIVP69KLxrFKTzq1gqPlMGpvVQShAh1dhJ-SJezdxl5Qr-D6MXjvThm-rmcXji27xxjaQDaTQYe3yRjh6xJsord0jfBVeAqMK_kjbuVT6mkixf3obcwewH3EfayhXGKzYnjufUsuZqB8wc0URRAoG5wdX3FPcKj7GUkWFwR7rBPW4TwWal14ZXlEb9weY5T6JOEr13AANlnlwl0hvQ0igGkLsCEDAccFfpd6bQeyKNFJ8o8BsQsEwP0ojwXbdidq8BBTws70Nbo6xCEOkxcVPJVMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهباز شریف: موفقیت ترکیه موفقیت پاکستان است.
🔴
پیشرفت پاکستان پیشرفت ترکیه است.
🔴
ما زبان‌های متفاوتی صحبت می‌کنیم و در سرزمین‌های متفاوتی زندگی می‌کنیم، اما نوری که مردم پاکستان و ترکیه را راهنمایی می‌کند، یکی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131775" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
هشت جت تهاجمی A-10C Thunderbolt II که در خدمت وینگ بیست و سوم ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131774" target="_blank">📅 18:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131773">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ارتش روسیه : ما 5 روستا رو تو شرق اوکراین تصرف کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131773" target="_blank">📅 18:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131772">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شریف :  با افتخار می‌گوییم پاکستان و ترکیه، دو قلب در یک روح هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131772" target="_blank">📅 18:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131771">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شریف :  با افتخار می‌گوییم پاکستان و ترکیه، دو قلب در یک روح هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131771" target="_blank">📅 18:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131770">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سردار رحیم صفوی:  بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131770" target="_blank">📅 18:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131769">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
اردوغان: ما از نزدیک تلاش‌ها برای برهم زدن توافق ایران و آمریکا را زیر نظر داریم/ نباید به اسرائیل اجازه داد دوباره بوی باروت و خون را در منطقه ما بپراکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131769" target="_blank">📅 17:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131768">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
اردوغان : وقتی آمریکا و ایران توی اسلام‌آباد به توافق رسیدن
🔴
دنیا نفس راحتی کشید و نگرانی‌ها کمتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131768" target="_blank">📅 17:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131767">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66ce12768.mp4?token=u1rGH4et9PkRumyEzVuKh4AHCboAZbiLqDo6K6u9BbaM2OvJqVGTh7iKjO8f8I_CjMsgsKXV5dHfAPlJ6szwHZxtN5c1gEFDGOoAko4d7aikehzIMa8o9AnOtQs8tSB9R7BUH3chooLipCGepmuLo-ZwFfhrrQzWSw1tnYfvX3Vibyl32mqsp05QuHVf5NC2Rv5bpkSYmJAO9b8lVXc3PVapZXeENseQSzkIL_GMa8vkVA02cTe-KwSEUds5qmSIECUADrbKbemMdCASA3hgvPS8J9RSxYrrS4M4RJQ2vUF2_UYP0_l-3damoAY9UrAY0OlgEpBhxAIyevtR-AwyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66ce12768.mp4?token=u1rGH4et9PkRumyEzVuKh4AHCboAZbiLqDo6K6u9BbaM2OvJqVGTh7iKjO8f8I_CjMsgsKXV5dHfAPlJ6szwHZxtN5c1gEFDGOoAko4d7aikehzIMa8o9AnOtQs8tSB9R7BUH3chooLipCGepmuLo-ZwFfhrrQzWSw1tnYfvX3Vibyl32mqsp05QuHVf5NC2Rv5bpkSYmJAO9b8lVXc3PVapZXeENseQSzkIL_GMa8vkVA02cTe-KwSEUds5qmSIECUADrbKbemMdCASA3hgvPS8J9RSxYrrS4M4RJQ2vUF2_UYP0_l-3damoAY9UrAY0OlgEpBhxAIyevtR-AwyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا کِیر استارمر می‌گوید که نمی‌تواند فاش کند از چه ژل موئی استفاده می‌کند زیرا این یک «راز دولتی بسیار سطح بالا» است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131767" target="_blank">📅 17:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131766">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123544aa58.mp4?token=mh1wdv6TbtzMBnc9IbSwDCpynSiYIZxYEes6-YbYhIXcs87EBADcCGChPxX-wYcmmk5Hh87ohVctvXsL13OO2tyf4eeuXisN6Sud4r9VZpiuWg6tQV2SAlYTLkH3NI7bia9pRHJ-MwOrjEke9_9eOncZQPWd6ZBEYuCV4A428NVCYjj13Vq6LdhRYr_XRgFv2pF1Il0gW0VrmEky8RVxTh6spEx8i1GYviGMBi-6Bks770lvqwE935J6X1adkuDxUB_bRBP7L4LeJXWXdByStvrDZSgeJwv1V7B6XnhBEzE7nC0JSMPJ5tvJLVUW89nFdK_np_3gw09-BoQ7hbMTyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123544aa58.mp4?token=mh1wdv6TbtzMBnc9IbSwDCpynSiYIZxYEes6-YbYhIXcs87EBADcCGChPxX-wYcmmk5Hh87ohVctvXsL13OO2tyf4eeuXisN6Sud4r9VZpiuWg6tQV2SAlYTLkH3NI7bia9pRHJ-MwOrjEke9_9eOncZQPWd6ZBEYuCV4A428NVCYjj13Vq6LdhRYr_XRgFv2pF1Il0gW0VrmEky8RVxTh6spEx8i1GYviGMBi-6Bks770lvqwE935J6X1adkuDxUB_bRBP7L4LeJXWXdByStvrDZSgeJwv1V7B6XnhBEzE7nC0JSMPJ5tvJLVUW89nFdK_np_3gw09-BoQ7hbMTyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جکسون هینکل فعال رسانه‌ای امریکایی در حال توزیع شربت نذری در مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131766" target="_blank">📅 17:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
به گزارش بلومبرگ، سفیر ایران در پکن اعلام کرد چین و دیگر کشورهای دوست هنگام تعیین سطح و نوع هزینه‌های خدمات دریافتی از کشتی‌های عبوری از تنگه هرمز، از «ملاحظات ویژه» برخوردار خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131765" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131764">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ادعای الحدث به نقل از منابع آگاه:
دور جدید مذاکرات آمریکا و ایران در تاریخ ۱۱ ژوئیه [۲۰ تیر] در پاکستان برگزار خواهد شد.
🔴
دور بعدی مذاکرات بر موضوع تحریم‌ها، دارایی‌های مسدودشده ایران و پرونده هسته‌ای متمرکز خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131764" target="_blank">📅 17:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131763">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAMxTg3ljJiV4Pimu9fNAovRlAzYeUV7dHS57gyZC27kHmIwQKV1AaAmB0Dp_buU6lnQX6hSdbPtnBqQnnF2RjSf_PQwjXdgrpbhXdHKdgeMUDIR79ycA9SNsIPDM4SfJkgOuCJPuKgMZitFIc8VaipX53tfC5qRhv1zQBoDVUkpVe3HLze6htUrwcnRr8IZJ2XkHbSRbteBtzdhKE6GihcS_LTaRVtwbAs5qBCEj9aGLXef3HmVVmUIWiqbPfYwXtX-4sZ4g6wocJw59AHmF0JxVbAHqUDrghXPkdPtRrBxZ8TEN0m3lvko73x8nRmBaNALmCYpnRxQS703T26IJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز مستقیم هواپیمای باری 17-C نیروی هوایی ایالات متحده از پایگاه هوایی نواتیم به پایگاه هوایی الظفره امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131763" target="_blank">📅 17:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131762">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ec205bc1.mp4?token=t7i-gIjMtw14b0qCUWMqQkXg__dgyNj3q09cR2HC6idbMmk96kmT0PoLxQ0ZZkuZMDDkMT4cZHslz1cfl72csxVoL3ceCPuRThHkrfY9Ma3hAwpOzP60Eor8Gyzt4cS2wCIeB6aMMTWB1gA1mC-VxY-xVMGrX35LMJx8IjJzIv4W-O_vVs3vCK4WIHaRadth8x8GPfE4OXiyT4XFEVMgrN2q9rOKYDnR8sK_dwzX9E8-IuQMic9iGd0OcLEqGy5eBIKufeKS2K6sAhHwmfxB-QWR2f0ZilM51OXvzhL8HbMPY4Yc5COvdEY-SNV2xDfkuNOkZLB3aKjv-ym_2cmNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ec205bc1.mp4?token=t7i-gIjMtw14b0qCUWMqQkXg__dgyNj3q09cR2HC6idbMmk96kmT0PoLxQ0ZZkuZMDDkMT4cZHslz1cfl72csxVoL3ceCPuRThHkrfY9Ma3hAwpOzP60Eor8Gyzt4cS2wCIeB6aMMTWB1gA1mC-VxY-xVMGrX35LMJx8IjJzIv4W-O_vVs3vCK4WIHaRadth8x8GPfE4OXiyT4XFEVMgrN2q9rOKYDnR8sK_dwzX9E8-IuQMic9iGd0OcLEqGy5eBIKufeKS2K6sAhHwmfxB-QWR2f0ZilM51OXvzhL8HbMPY4Yc5COvdEY-SNV2xDfkuNOkZLB3aKjv-ym_2cmNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز : هم‌زمان با مراسم تشییع رهبر جمهوری اسلامی در ایران ، آمریکا جشن دویست‌وپنجاهمین سالگرد استقلالش را برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131762" target="_blank">📅 17:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131761">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
به گزارش فارن‌پالیسی، هند و ایالات متحده ممکن است در برخی اولویت‌ها اختلاف‌نظر داشته باشند، اما رقابت جداگانه هر دو کشور با چین همچنان به اندازه‌ای جدی است که همکاری راهبردی بلندمدت میان دهلی‌نو و واشنگتن را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131761" target="_blank">📅 16:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131760">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کامران غضنفری نماینده مجلس: پول دادن به مداحان که دیگر در تجمعات شبانه حاضر نشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131760" target="_blank">📅 16:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131759">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
روزنامه تلگراف گزارش می‌دهد که یک ابرقایق ۱۳۳ میلیون دلاری که گمان می‌رود به ولادیمیر پوتین، رئیس جمهور روسیه، مرتبط باشد، به سمت بندر مورمانسک در قطب شمال در حرکت است تا خطر حملات پهپادی اوکراین را کاهش دهد.
🔴
این کشتی ۸۲ متری گریسفول توسط ناوشکن روسی سورومورسک و کشتی گشتی وووودا اسکورت می‌شود، در حالی که ناتو کاروان را زیر نظر دارد.
🔴
از این قایق تفریحی در حالی که تورهای ضد پهپاد عرشه آن را پوشانده‌اند، عکس گرفته شده و پس از ورود به دریای شمال، سیستم شناسایی خودکار آن خاموش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131759" target="_blank">📅 16:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131758">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نخست‌وزیر و وزیر امور خارجه قطر، محمد بن عبدالرحمن آل ثانی، با وزیر امور خارجه سوریه، اسعد الشیبانی، در دوحه دیدار کرد تا درباره همکاری‌های دوجانبه و آخرین تحولات در سوریه گفتگو کنند.
🔴
در این دیدار، آل ثانی مجدداً بر حمایت قطر از وحدت، حاکمیت و تلاش‌های بازسازی سوریه تأکید کرد و بر حمایت دوحه از آرمان‌های مردم سوریه برای ثبات، ایجاد دولت و بهبودی بلندمدت تاکید نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131758" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131757">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نشریه نظامی «میلیتاری واچ»: کارخانه هواپیماسازی روسیه تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط ایران را به پایان رسانده
🔴
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
🔴
احتمال دارد نخستین سوخو-۳۵ها از سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131757" target="_blank">📅 16:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131756">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01db34aaaf.mp4?token=X5o1RSSvnu80uYhliJ-0qt7qg6Ib1I399K2o2bNzdF8AXlH5-Z9HEjyNibk1-vl8weIUmDibfYfo90Mt79nAnEgXlGLWeuDGRnuP49FVu_oFJwhKswV4fBMrCEF43ZWR6H78ElxsAm_rH0b7x3LhEM1hdvtAFNlCLaYYGZihJ_absL4OehGHJl23YBHphMTTV2jwP83NdXSsyvhBD8ztPdlQjkjPQv6sqadH22RrKvjyb7AgmGj1_sRTKTkupfZiKj8ibanrQC8P0fVfuLiO2fmqWyXWo6aQAIZpS8NI-KfLa_78-S3CfNnnHGTz1cwlG9KLu24XBigIMBAQoWS7GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01db34aaaf.mp4?token=X5o1RSSvnu80uYhliJ-0qt7qg6Ib1I399K2o2bNzdF8AXlH5-Z9HEjyNibk1-vl8weIUmDibfYfo90Mt79nAnEgXlGLWeuDGRnuP49FVu_oFJwhKswV4fBMrCEF43ZWR6H78ElxsAm_rH0b7x3LhEM1hdvtAFNlCLaYYGZihJ_absL4OehGHJl23YBHphMTTV2jwP83NdXSsyvhBD8ztPdlQjkjPQv6sqadH22RrKvjyb7AgmGj1_sRTKTkupfZiKj8ibanrQC8P0fVfuLiO2fmqWyXWo6aQAIZpS8NI-KfLa_78-S3CfNnnHGTz1cwlG9KLu24XBigIMBAQoWS7GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای روسی مستقر در آفریقا، امروز صبح حملات هوایی را بر علیه مواضع گروه‌های FLA-JNIM در شهرهای آنفیس، گائو و سِوارِه انجام دادند.
🔴
همچنین، یک اردوگاه کوچ‌نشینان توارگ در منطقه زارحو، واقع در استان تیمبوکتو، مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131756" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131755">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpbd45n83Y6xXY5I9USlo6jqXfr5xNEp0HAPuoxk1HtIXfVy-pc3BiGTt4xL3W5icuw3bI-I9mi_MkbgiPZ2h-WcCGjiTjJfiWEGzq198oq_wHwb8Ti-ePdZDQNuPifxjBIVlkXPHXIsDy0AIMWw0-CPVUJUoSEWjH318WwS6OOUadBSFLlNkSCQ_pax28k-Jt5bggP8lDgYMN__bZQz88TeTNKFJmIXvqZ9eZ9w27EZ3hztS-PSMIkUwYBWlLnVajYZ1ew1WVlPKbZBA4X42uOpRASG9QVYrf87UpMKZRDHzA2Rx8MQnniLsouwHnDj26oyP6PqDeF3piw4yiOZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی در ایران به اعدام محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/131755" target="_blank">📅 16:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131754">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/فردا یکشنبه سراسر کشور تعطیل رسمی اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131754" target="_blank">📅 16:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131753">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdhyqBS7kkszvCITqSlegFY0DYlLMvONru0rvoKR79luviWeNibhGQID6dJA8uW5AIbaXxae6ENtv0Xj7WLazsmyroiO_Y6vlI8_qe2RnRQlppMN4L-AEvxfYSqkyrpAbVZPlIlp3Sli69rmcV3_XcIzZaVi68Zu3n1yt2ulEkS9lLVWuxJEa5zeCgDUB6aHqHcDm7lbC8tdgLejyquQ_NIi-ITpo6Se3Psci2-dm7WQbX1KuZRcEyhLfKhVjAev2uQvNOgtgS3UCK1y6glyi413d1Yf9Cuw9B3fvaSsQCqMbs6Kf1Wjes6OoRxV8JGexe2AFOUDRmsODpcPt8slHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار عظمایی به عنوان فرمانده نیروی دریایی سپاه معرفی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/131753" target="_blank">📅 16:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131752">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9286675b.mp4?token=gLDzVHhmCPZoQ2XfvVuwCyHbFqMG57SYD20juAOalZBT1okgMoSNiScUs97OO8orFTnp4UO1De3l-tdUBth8WSEyQY72x48kF0lL3eOUXEv_x26ZIJmskK6ucBpYbGanTIcYk_dpT4ynYLfsGYnyks0KLMxEyU_E5KeC5KuX2NxE5KaaPi_aYMvg6ypERLVVWZ9SdA5XQVSRZZB06oMThP2XhwnZGou_Zm2rlFYi5s6spAW8qu8bS4Q9U5eK7f8cFgF9FwfBwMyzlVlUzR43UkpaNCRtyXisg-5tSkrg0iz_9G_xzqcXSLWP5qr8Dt5iCkx-7Br3ge3xVI9HfEpbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9286675b.mp4?token=gLDzVHhmCPZoQ2XfvVuwCyHbFqMG57SYD20juAOalZBT1okgMoSNiScUs97OO8orFTnp4UO1De3l-tdUBth8WSEyQY72x48kF0lL3eOUXEv_x26ZIJmskK6ucBpYbGanTIcYk_dpT4ynYLfsGYnyks0KLMxEyU_E5KeC5KuX2NxE5KaaPi_aYMvg6ypERLVVWZ9SdA5XQVSRZZB06oMThP2XhwnZGou_Zm2rlFYi5s6spAW8qu8bS4Q9U5eK7f8cFgF9FwfBwMyzlVlUzR43UkpaNCRtyXisg-5tSkrg0iz_9G_xzqcXSLWP5qr8Dt5iCkx-7Br3ge3xVI9HfEpbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهرک‌نشینان اسرائیلی، دسترسی فلسطینی‌های محلی به زمین‌هایشان را در نزدیکی شهر سنجیل، در مرکز کرانه باختری اشغالی، با مسدود کردن یک جاده، مختل می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131752" target="_blank">📅 15:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131751">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
آگهی دبیرخانه شورای عالی مناطق آزاد تجاری: انجام هرگونه پیش‌فروش خودروهای وارداتی در مناطق آزاد ممنوع گردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131751" target="_blank">📅 15:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131750">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر خارجه مصر: از تسهیل مذاکرات ایران و آمریکا حمایت می‌کنیم
🔴
باید آتش‌بس در لبنان اجرا شود و اسرائیل به طور کامل عقب‌نشینی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131750" target="_blank">📅 15:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003c393383.mp4?token=vtPF5DwOuofdAtRxPZ6GmcuRF0MS60W6dFphdbReG6-uY-VNnHhm8Qx17aNj-PBC0pLpXYf3F1Wd3aDBRBGdxyzbr_Ll67q6MvYcq0WXlWCTloEIW2fFk3H4NboH7kdlObzYL7xZuQvu4kdUH10AeCyfl_0Fzbnd-h-rVYBJAZ1s3tnZxuNqAQI-fQxibDlZFOuDUD8SPGyx9jTV6MEwsPUtot2D8bWjaf1TPqozrQ5qo-MGAPWulzZZ6u8Nb58q8nE-Fhd_XknRchEYME3WOUD_t9s4WwIMwj8nPZ7Iy8RIj6n5CvovNBzTiNOZ5JoPRqmm2JJ0QjrUnvJy4oA2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003c393383.mp4?token=vtPF5DwOuofdAtRxPZ6GmcuRF0MS60W6dFphdbReG6-uY-VNnHhm8Qx17aNj-PBC0pLpXYf3F1Wd3aDBRBGdxyzbr_Ll67q6MvYcq0WXlWCTloEIW2fFk3H4NboH7kdlObzYL7xZuQvu4kdUH10AeCyfl_0Fzbnd-h-rVYBJAZ1s3tnZxuNqAQI-fQxibDlZFOuDUD8SPGyx9jTV6MEwsPUtot2D8bWjaf1TPqozrQ5qo-MGAPWulzZZ6u8Nb58q8nE-Fhd_XknRchEYME3WOUD_t9s4WwIMwj8nPZ7Iy8RIj6n5CvovNBzTiNOZ5JoPRqmm2JJ0QjrUnvJy4oA2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروه‌های بزرگ وابسته به سازمان FLA-JNIM وارد شهر آنفیس در شمال مالی شده‌اند.
🔴
تعداد زیادی از نیروهای ارتش مالی (FAMa) کشته یا اسیر شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131747" target="_blank">📅 15:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b402cee7.mp4?token=DVjPkj0_YBROg-1FiEEHAKmwL_GonsG9_h1TTffn3nhlCJrV0B8Jyrmrqbjl5yEoIuSXqL1qN3N3TYSudSmXerA0rlTG8JD8olAnantvyDSDZlntIG7mi6CkOCLcV7N8rA6NoABodyMN55iX_lYluVcDmwDCaX-XWyKeE4druwKZLQAVflMtkM_YPDAyJLwe0ea1SCl5MWwLD9eBMZJhqcgoysm2H7FPeZeix1jRUg_Bs8bMMFpA2SLTZqAgeTOEksKS3l3hiTTPLioR-S8QQFM1V_KagzaP76-MqK1xYXb4bbPYjA-rj_8x3YpSaGdqWydi8C1Rb6yJvCt9RxJJKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b402cee7.mp4?token=DVjPkj0_YBROg-1FiEEHAKmwL_GonsG9_h1TTffn3nhlCJrV0B8Jyrmrqbjl5yEoIuSXqL1qN3N3TYSudSmXerA0rlTG8JD8olAnantvyDSDZlntIG7mi6CkOCLcV7N8rA6NoABodyMN55iX_lYluVcDmwDCaX-XWyKeE4druwKZLQAVflMtkM_YPDAyJLwe0ea1SCl5MWwLD9eBMZJhqcgoysm2H7FPeZeix1jRUg_Bs8bMMFpA2SLTZqAgeTOEksKS3l3hiTTPLioR-S8QQFM1V_KagzaP76-MqK1xYXb4bbPYjA-rj_8x3YpSaGdqWydi8C1Rb6yJvCt9RxJJKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار نمایندگان جنبش امل لبنان  با سید عباس عراقچی وزیر امور خارجه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131746" target="_blank">📅 15:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی: پزشکیان به مجتبی خامنه‌ای اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
🔴
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی خامنه‌ای با یادداشت تفاهم موافقت کند.
🔴
دکتر پزشکیان، قبل از امضای توافق، به آیت‌الله سید مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/131745" target="_blank">📅 15:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131744">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
گزارش ها از پرواز گسترده و غیر عادی پهپاد های اسرائیلی بر فراز بیروت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131744" target="_blank">📅 15:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
تصویر بسیار منشوری و زننده دیگری را همسر سپهر حیدری در اونلی فنز منتشر کرده!!! که به شدت وایرال شده
◀️
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131743" target="_blank">📅 15:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSyowGP0DaIrGYxLi6IS4ZAIWI6r7Rrae-WV_T5u7rEyAY_LiwFddqqLiB46TIBdaXZApvUhbrHlOOttzEO83GpfLVo69TQzh55uQquY5O-HObLPRn5Ds7s_7Xb0TyKVKOTv8-0Jc5Hv-W0rZQjnOa5XxQ166J6YgtXJCIMaR2OG8uB4_JmSjVysQMOSUSP7FfNUFh8IpNc_aZ8Pc-2w8rO8jdA-APe6jG8id9LBx5lFaOgrkIx2zN5ptz_w4n5_7izd-VxAw6hruD08XyRzyN_Zq4i8smCS-0mvYlJnScrPHUIfrL3-MsSa0v9abZhq9Zm6NzwW3otwVLczkak8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خلاصه‌ای از کیفرخواست رضا پهلوی که توسط خبرگزاری تسنیم منتشر شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131742" target="_blank">📅 14:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس‌جمهور عراق: عراق نه با ایران در برابر آمریکا متحد است، نه با آمریکا در برابر ایران
🔴
روابط خود را صرفاً بر اساس منافع ملی تعیین می‌کنیم
🔴
پرونده گروه‌های ضد انقلاب بر اساس توافق با تهران، حل‌ می‌شود
🔴
امنیت خلیج فارس، ما و منطقه به هم گره خورده
🔴
تلاش داریم تا بهترین روابط استراتژیک با عربستان برقرار شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131740" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d_Ct0ynsRcnZDeNPoz59KPFKOZLs_i-x786K7s1KCxXb-TufKScnnZRFog-oRjACgDCb8AEGvTZO1-HVTFd6JZiOQ5iic7n__uD8nWaFfPQaYbh-OvlYxDtKDXlNR3Y-jS9Sr00W2p6GvdZ_agzoibUI6g_glZj16Gzh6G-SoOjmN2dc5tzyq9StE8RKdSluAlkNkY9MV7M_vQuV_Wv0KqtRkt4Zm9lt2QiDLRd2YdhLR9GnKAldJmXqCzHMsZcPmNXC2qoCRbPOHsf9vP4B8aqDhSFXmqUoZrfPkQ3Ex0qCwcRIZfXeV0lw6qIrpnp-OiuXgPDEXX1O7o4gIFhc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UXbEXLCv2dxPusgLLL5up8sVmzB6yMoVIciakL8jIp_lJaFUqTtfwp8F3ZVYIm9Y96gTAk_8bSoqHVK7zJ61lzty6vakOVUc2jSv4Tz0zVz-g_7WUgpJk-53kJfqATxo9dSEU1PPFQqUeX7SRQsmiaCQHBeY1-MX5ARDGfcYAT6OzbC-UsVUJe2pEsLLdvIS0GyyHU8iKk8LxzCYXnYu_1I5ISG_vdaAaFzFzvRgAiAVkJ55nabWAZZU4OAPsi0DLz5FtVf8H08FVN7zNfqchfywLjQ26l4_nwD74mFHOnXCsAfve3KMQLWjIwu_CQ6A_bh76HfrU7wCaz5sYMCLuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا یک بالن نظارتی (الکترواپتیکی) یا مخابراتی در آسمان تهران مستقر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131738" target="_blank">📅 14:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131737">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
به گزارش اسکای‌نیوز، گروهی فراحزبی متشکل از ۷۱ نماینده و عضو مجلس اعیان بریتانیا از دولت این کشور خواسته‌اند بنیامین نتانیاهو و یاریو لوین را به اتهام نظارت بر سوءاستفاده و شکنجه سیستماتیک بازداشت‌شدگان فلسطینی تحریم کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131737" target="_blank">📅 14:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131736">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ : کمونیسم یعنی مرگ، استبداد و دنبال کردن شرارت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131736" target="_blank">📅 14:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131735">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پیام پوتین به ترامپ: مطمئن هستم که روابط برابر بین مسکو و واشنگتن، به نفع کل جامعه جهانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131735" target="_blank">📅 14:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131734">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
به گزارش بلومبرگ، امانوئل مولین، عضو شورای حکام بانک مرکزی اروپا، اعلام کرد این بانک پس از افزایش نرخ بهره در ماه گذشته و انتشار داده‌هایی که از کاهش تورم همزمان با افت قیمت نفت حکایت دارد، در «وضعیت خوبی» قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131734" target="_blank">📅 14:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است؟
🔴
مقام‌های ترک و اسرائیلی سال‌هاست که علیه یکدیگر تهدید و توهین نثار می‌کنند. از زمان آغاز جنگ اسرائیل در غزه در سال ۲۰۲۳، این جنگ لفظی تلخ‌تر هم شده است. اما حالا به نظر می‌رسد اوضاع دارد از کنترل خارج می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131733" target="_blank">📅 14:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5_DeWNi1nYik9V297R8wJ9zWFyw85Km9gJyV276YpRk5IrWWFHy5rcQYTPPwAjgslgS_Ouxx-kf7Ct5_3hfoCgtM9umunnSZKtNo9NKs198MIq-AnTeIOxY1LebAXH5PrixSwEhGJyGBZZfEMLU-5MOFu6TBbtGGmaYuQSwkhUGOAdo7MqVFn-KxAkVuOcrJBMRNEf-q9U4ExR_5Ye9wNlqjZzmnOuneBukDz16gVf_PiOvLCFj-jHonpPis7as4s8ZA6ETgcNTKuEDEEYv19F1Qf8S-sJhUXZToix8186fptUKHBPpVNS0fHDfc1CzuZ5i4fDCfXEtA2-OxnhLkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار سی ان ان در مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/131732" target="_blank">📅 14:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m89zcPHBiw-UEmi0q3y5X3bZ4pZe06jTeOKnv_fJVTndwpQ0auRZlbaZg4E-ovgEVhyfMSZaF8EhyElsJVOn4hrUHExXqY6s6wUCl46aKX5Z_TjEJs5ue6fHdBaCd6gmF_k_AUyxnI4xWeZgrZrq_l2WIv70wPo7rxQTBJ1IABwKxEKCTXl3KfbAFc_e0ZQl8I98G8N_eocmUJsZcksVooExwEwOW-5-uZXZZVssJFJplgk7oNZIr_3wJ0KTkR2zAzYT62LI_GB0c1uK9jZS3Ah_IxBb7dqaCkNEZLqIyj4o5rLmmvhQPg3q4f2DNtW4azMCLgtd6my1gLK-AQthEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131731" target="_blank">📅 14:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر سقوط یک هواپیمای جنگی متعلق به ارتش روسیه به دلیل آتش زمین در شهر گائو در مالی منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131730" target="_blank">📅 14:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
به گزارش بلومبرگ، پاتریک پویان، مدیرعامل توتال‌انرژیز، اعلام کرد تولیدکنندگان نفت خاورمیانه به‌دنبال فروش نفت خام ذخیره‌شده در جریان درگیری‌های خلیج فارس هستند؛ با این حال نگرانی‌های حمل‌ونقل همچنان بر موجودی بنزین و گازوئیل فشار وارد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131729" target="_blank">📅 13:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مهران رجبی : حسرتی که پس از دیدار با رهبر به دلم ماند این بود که نتوانستم پایش را ببوسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/131728" target="_blank">📅 13:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی : تاکنون هیچ حادثه‌ای در مراسم وداع گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131727" target="_blank">📅 13:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKxfyIFFweOqd4_2kOR4iB-DiRacTStObbx6_RJlJPkmeluyLOfo3D4wPVd2LyKDIVCvo1YVcSksQp1e28YYGGpI5F_K42DW9OogpmrLx3VbCsegTQejuBtDxN5mc1Eu6pKIt2WDEwqWjP0Xs7a-CFRWr8Nc5XMmbHaMeCWHCy-9Q4cElFhv_tuD9FFS79h1KN0HLA73Cx3_fNDrcQGe3OkHdydY_5NlMqEqlvLI4GCNTn9zXlTU9Yb4MhelFSQ533Wl8kl_08aUZDfKdQt-W3H-iq2pbYdHay2Oj7rVu_b0fHwT9Q4Lr18RMlihUlgLxLUXTzI55OZqTw8ELadJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز روز استقلال کشور ایالات متحده آمریکا هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/131726" target="_blank">📅 13:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X53spOYrWcvT-hXyOHbqrrj0hYCg46jWg4kzSisaCwb9XSRITItUYISiuDRgnvmO5EVa91qhpvnixGQ45wLAP1HRevPPgWXuYect7vcgaIsp-B_gkNp2STUczZoQOZx9igGHUUEt3IPfBfyRicpI-GqXSiINIEkKW8EVv8btBRSBrXjXjEzU0nzLY4Rm9OeCnGqHMM9zl6QMWSGPJk4xa8JFqBSw0bwGFH9aMIzHeDbd3Pyob80ZEC6JByDEm2SpvAzSvLQlbFa2o8CfJDcg9QAtcQU4n2GUDw9aTJ_IYpmRgxwJPFpq3mnNGDU0AUcRf7I0VKWaY60YUxYb-D09LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب/برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131725" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
میشل عون در پیامی به ترامپ : از شما می‌خواهیم که همچنان در کنار آرمان‌های عادلانه لبنان و نهادهای آن بایستید تا بتوانیم فصل جدیدی از امید و صلح را آغاز کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131724" target="_blank">📅 13:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ:هیچ کشوری به اندازه ایالات متحده آمریکا، خیر بیشتری برای این دنیا انجام نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131723" target="_blank">📅 12:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131722">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
آلمان انتقاد ترامپ درباره صرف هزینه‌های نظامی کم در ناتو را رد کرد
🔴
فریدریش مرتس صدراعظم آلمان، انتقادات تند دونالد ترامپ رئیس‌جمهور آمریکا، در مورد کمک‌های ناچیز آلمان به ناتو را رد کرد.
🔴
وی پس از دیدار با سران کشورهای حوزه بالتیک در برلین گفت: آلمان در حال حاضر بودجه دفاعی خود را ظرف چهار سال دو برابر می‌کند. این بزرگترین تلاشی است که ما تاکنون برای تقویت قابلیت‌های دفاعی خود انجام داده‌ایم. بنابراین، چیزی برای پنهان کردن از کسی نداریم.
🔴
وی افزود که این موضوع را با کمال فروتنی در اجلاس آنکارا در روزهای ۷ و ۸ ژوئیه ابراز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131722" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131718">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujUrL0MBlv1gZpRRQE9i8BS8Vg0HtPQSrjLTFT5_n5ObHhG-mTy8rBbM8bn7AfIRrMFEK38TV0DHpbqgfUkkmqY7nsGettXClYVclcSQvbPNzRdgZ4OBja8mWfa-IrNRsu1irnGkn5uRAXL0B5UgvV_NfZ9v95XHNDU8S-KSHkDn7iyYBApW6pJpA32R-Jlf-zEnoCztesTJqJsvA-lXmyJZr2xBh1jvKswhtVflJtO3UsVWllDqdo01jOx5WciUx-5g3Q_OL-MGZl482qWmmLooCWUXqnztzvf5ZAqzSd6nH1LDJRH7pNLcA2rp7O-QcP-XJytRUEku1VhnuJtQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atoXGr6uLVOpZhb8laFE-2q8HVdVhYlpduKNsUuFbBBTaouNHx_t-MUK8CUl9KR7MbJ80spXKhx6SN62HLUYt15Fp9EIKWIsv0M8W5qNo9DOYpqxRYz-faLjofysBm4nGk-VRFDsveEcZz1992-FC5y0cQqr_gT-M9tw0c49JLhb50Xiz8VH1V38EWLrmz3CB68UXcF23vKfpG-WwKn-zNR8G3CsDFZ5PfkbbhUOykFvdgbw2Rftwz1m9MEsZG-XMS5iOcf6UGloZ7estZHUW4jLg3DDom8DylGIVdnZYEMSleaxMsiFOwtc4Y5eOHHl0KNF472qSOYCHdAirEEkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rc-fWI3UpTWmxnEgsoql37ri1zBeGtBGXSZ8f7aGcV1uTgyxh2t23RqAdky5LZ5EjbHn1IaZqlCemSM4j3Vc3XVvDcFn5n26-1o53Ye5nKmq28xx5wNtuY3LOn50w8k0b2Bjig5dvEnNEdkE4ZNxh7q-oVQuHPB00HT0jyW9eE0OTbqyiB-Q7jk075YGSD5Hw8C7ZrcLHhBileBULBJkVNCQWduOL_cLn20i4_Id6BGgVWcWONOM-0O-l19Uk22C_Nd3wfgYfGFk3M59rYRZatEaFvZ8vNdYSqSGjJu2BFm9ZRBNJgBQna6O6A78lY9mdwjxDmkrKcg_vRqHsbLTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgO8ZcWWUCPAK--TZCozsA343629ShNEOfd1-EmrZC8HtN6ZDUm2xNfphunlylgBAkenSYVCRv-KtvLlWduRNfqg3olAeD3GZXzEfPcO1aR6yN8wNmVpzypygLu38ilvTESyE2bfj6LxM-2yosZKbl5zNMsOlUPgVTcTnEFYSvXvH2jSldXnG_ZvW-62lswDQ9Uq8-Mozjt8-eSUbEDBKGkUf7g1nq-l8eb0PcMIG2Ql_tE5TzjgMzPRfF8Q2j3Foe40qQsVY1vAB3loFSXwL0pl697DlbGfoB1evwH8sVEfgFsbUsuyYx6Y-5pbBzkiy24C84kSp8sYYJGmEAp6Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
به‌روزرسانی (تنگه هرمز): چندین کشتی به‌طور ناگهانی در حال تغییر مسیر از کریدور عمانیِ تحت کنترل آمریکا به کریدور تعیین‌شده از سوی ایران هستند، یا حتی دور زده و بازمی‌گردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131718" target="_blank">📅 12:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131717">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
منابع لبنانی از حملهٔ پهپادی اسرائیل به اطراف شهرک «صدیقین» در جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131717" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131716">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی: به سایت‌های هسته‌ای ایران باید دسترسی داشته باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131716" target="_blank">📅 12:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
زلنسکی: زیرساخت‌های نفتی روسیه در نزدیکی سن‌پترزبورگ را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131715" target="_blank">📅 12:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOuj9wdNPOvzyeQ2oc54IAD_cTczmlb2pfj4ixHxGtwiV2F6ryumSm7LLkVTN7kiQh7ECFgTTUb6DPk2D9DaArQv9ZHmOVOzY6UIqVF0fW5zkHgHdT8PH985ncKOxFt0j3qYv8KjISW3JNQch9zufX5VU3lxXPt__1skO9WSTHdBpEr6aKxQ_2lNAcA3HZBjDCVdo1ueUGUbblRNHxstboDZXoAyQL49m6S6SfC7Df4BeaL3ej5mjFTWGMBUU8L1CZIZ2f5toWtCm_tYksPw9PxAVXlS7Fyl79SFSj_bbfFYEh4n4wk5Q76lWn7C6wJi9cxfXG83DPF_K3Fh0H36Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌ پهپادی گسترده اوکراینی ها به یک پایانه نفتی در سن پترزبورگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131714" target="_blank">📅 12:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
تولید نفت اوپک با بازگشایی تنگه هرمز و ازسرگیری صادرات تولیدکنندگان خلیج فارس افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131713" target="_blank">📅 12:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEZvWjACQc6uLbEfuoCSwn5pgABQl_UivWOwolioYp1ZWR4ExGlSariehMV3hOO5kIDo3dUvxD0PJGGB5Ih-UQYZdllUnDs_A5QIqR38mH577lM9WCnxxc0LHr5njkHiMgl9emjQ0OTy2vY-ReP0lBbEFJgQTDwPP_Fb0I0X_2Fc_2ZtA083Xe-jvD6PYtlUO2RrJuht2R4glT973FdV2J8KkoDYie3DZDe1a9ZHCR46cmHMTvk8srrKT3toEUI9XzI9sUJyPY8Y_QyvfIiA6Vww9m5obpcOPnJ7eMadGHCdLhscXNJm6B4jvo5cdRokBNr6kD2EJLTOBJjO9qF3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: به گفته سه نفر که از موضوع مطلع هستند، مجتبی خامنه‌ای در حمله‌ای که منجر به کشته شدن پدرش در آغاز جنگ شد، جراحات شدیدی متحمل شد، از جمله سوختگی در صورت و بدن و زخم‌هایی که نیاز به چندین عمل جراحی روی یکی از پاهایش داشته است.
🔴
انتظار نمی‌رود که او در مراسم تشییع جنازه پدرش شرکت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/131712" target="_blank">📅 11:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131711">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeESAD6Ta6dcDofsV6lpg8jZx4A8sWzZpnaAh-5or9eMnknf_fZz8DnMLKm5O_4ZW7DbLsvVnOvltE47jwmfcOlWk76AXvzijXLDwgbjX3u1JxjoUPbeBIWUkzN4MyMLQBrFD4jjfuhAdIOF6fYuUYvGqEObONMYywrpZs18XX8XhvJH5abuYXUS5E5x0X56wcrWW2yfXDA8abAAsG1sTLxb31szO5R-Rv16xYmWwqr6X5AEwyF5VwCd4821FFTHSp8yqk76J9uYvLrfAzyeMjO6eMLcwIzIB9XbBga8iVSQpfHzj_MdzOgsS94uZq4Z0oeeWKjBuq9pOFDR4mugRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک
کاربر اسراییلی:همه کشورهایی که در طول جنگ توسط ایران مورد حمله قرار گرفتند، در مراسم شرکت کردند؟
🔴
چه آدم‌های بی‌اراده و بی عرضه ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131711" target="_blank">📅 11:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131710">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
محمدباقر قالیباف در دیدار با رئیس پارلمان عراق: درباره مدیریت تنگه هرمز موضوعات مهمی در تفاهم اخیر با آمریکا به امضا رسیده است و بر اساس قوانین بین‌المللی، اداره تنگه هرمز باید میان دو کشور ساحلی ایران و عمان انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131710" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131709">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
انفجارهای کنترل شده برای امحای مهمات عمل نکرده، امروز در جنوب اصفهان (ارتفاعات صفه و بهارستان) انجام میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131709" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131708">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5fF8YaZWO9UYlIbSEJbCxaRjs5LhS5h0-HyBPtKzNDuC3u4VlbbM9Ee_HJ3ZyPYkHnQmqzmt1gMpi6PG15-NLHk3Ep0TFgI-g2GUQwdnRXBhtFDamkgJAiycGJp7iBJ08ix2Y6aV5Z-2mMC8RbxcuATlf5UDJWOkwgLr4xs5QOVCoZxa53-drP6EIO2KU6GUDNA5Lo4qWIUAukKU5yBHtvXdFuinrXRQs-ZHOcCBmYr3FtBuQ-nDNARa9SgobB5tVkZklsn51hoKTxFr3QClelhRZBg8eAmZcBdVTmpNs01w1LgNuyQCyBsfWVuDwa9RjC7VsxurhtO7AQatcqXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده در رویترز از مراسم امروز در مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/131708" target="_blank">📅 11:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131707">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مدودف: تنگه هرمز اکنون برای ایران به سلاحی تبدیل شده است که از نظر اهمیت دست‌کمی از سلاح‌های هسته‌ای ندارد؛ اما یک «سلاح هسته‌ایِ» دیگر نیز وجود دارد و آن تنگه باب‌المندب است.
🔴
روسیه، ایران، چین و دیگر کشورها می‌توانند درباره ایجاد یک پلتفرم مشترک برای کشورهای تحت تحریم به‌منظور مقابله با محدودیت‌ها و تحریم‌ها گفت‌وگو و رایزنی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131707" target="_blank">📅 11:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131706">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ارتش اوکراین کنترل شهر کوستیانتینیفکا در شرق این کشور توسط روسیه را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/131706" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131705">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
تعطیلی سراسر استان تهران در روز سه‌شنبه اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131705" target="_blank">📅 10:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131704">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فرانس۲۴: عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند
🔴
از آنجا که‌ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد
🔴
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود
﻿﻿﻿﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/131704" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131703">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW-n-_ryg3wu9UJpO6-MQqcktmk_KcA6P7SpC1-4a_GntezzCMT46OcKYdacUNT_Wew2PZqLUrB32F0S2G_5GoXk4_mmyhgmMwc_fLouLYE-q0GSiElP-KmTFdAXqoDhjktMYTt2ZpGnoHYolRlFPd4CQ5AvyYmrI6UydNssHOH6TTmR8nMG0n-D9KVBJXU2vskEj04UOaAF7sRhr929a80MHLxX0kXj22ZbCtcCBg08XzFNWGBmkWOH8hf_UXdbIGfCnXtzM6TKpdGq0s_H51guPKyo06StQ4QzWs0qxk7YG902QF1sowVaM-fQHjgYZHiQkKLGDY0Mo8MNxC_p2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت سنگین نیروی هوایی آمریکا در خلیج فارس
🔴
نیروی هوایی آمریکا در حال اسکورت کشتی‌ها در آب‌های عمان و جمع‌آوری اطلاعات درباره جنوب ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/131703" target="_blank">📅 10:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131702">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
🔴
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/131702" target="_blank">📅 10:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131701">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4JLrG1B0Uv99pGiiWDQnvGjg_Zw0lp1SlXk6OlqCSNrjR6nJOB1YiYVGmx3KZX60-VJfy_-BfzftV67LwOynt-5PjSy411zze4_j8CskQkGbZqgS5PQbBq_mh7EcR9mS-T-DbOp8p7JuO-_P2PDNGfmhoCyHilsGHSYE5HMabUiY3EaQzLWWktWFO4ZWJikrx9hJs1XiEI6JWrjOuGtBJ1-6paOGhWDwshXv01dmmADSM4dMjPOUHfz--BveO-SwsrdsST_8z6yS3x0Ircyk6ooH3oHsC_g1r36r0Xhsl0q23kFkDlbOrTwync3RjUs8GTls8fbnbQQ50-XjOA1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار غریب آبادی نسبت به هر حرکت نظامی در تنگه هرمز
🔴
معاون وزیر امور خارجه در واکنش به بیانیه مشترک فرانسه و انگلیس: تنگه هرمز میدان نمایش نظامی قدرت‌های فرامنطقه‌ای نیست. ایران به‌عنوان قدرت مسئول و ضامن امنیت تنگه، نسبت به هر حرکت نظامی در این آبراه حساس هشدار می‌دهد.
🔴
امنیت هرمز با دولت‌های ساحلی است؛ بحران‌سازان مسئول پیامدهای ماجراجویی خود خواهند بود؛ این هشدار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/131701" target="_blank">📅 09:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131700">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
گروسی: تاکنون نتوانسته‌ایم به تأسیسات هسته‌ای ایران دسترسی پیدا کنیم؛ این موضوع به مذاکرات جاری میان ایالات متحده و ایران بر سر تفاهم‌نامه گره خورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/131700" target="_blank">📅 09:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131699">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
خبرنگار الجزیره تأکید کرد که تاکنون هیچ اظهارنظر رسمی از سوی واشنگتن منتشر نشده است، اما رسانه‌های آمریکایی به نقل از منابع آگاه از وجود «تفاهمی موقت» میان ایالات متحده و ایران برای کاهش تنش خبر می‌دهند؛ تفاهمی که امکان ازسرگیری روند مذاکرات را پس از پایان مراسم تشییع رهبر فقید ایران، فراهم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131699" target="_blank">📅 09:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131698">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مکرون، رئیس‌جمهور فرانسه: دو شناور مین‌روب را به خاورمیانه اعزام کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131698" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131697">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUg8xBEcLiWGrFjTW8ItRTNYuSjNTrbeR2REBgSrA-bnPbopT79mdz016ftx0_Yjn_NE05KCz6UkMW52roqouE6_pNYWJ-Ks2NYK0VmaUDE2IZUe0LQeiP-ToqiG1Z9PR2mavR437L44noo2kQANPd8I-69_n8iFRgGHk_hBlnCJp2qu1QmsH7iVxMePhsXo7v1LlqB3_flYQ0pvxyzj3-LwUJFZNaz-Sm-wRGO3pufk8JIOdxV75xi8gJAD3q83QRVx3GpLp6qc-ADOcZho4qXkNXfAy0vPorwxvsYYKH-Gh2tqF-71g-dKc6TEv9KmEKN7h2zBrVIWwXJaRxSZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی از پهپاد انتحاری دوربرد «SKYWASP» رونمایی کرد
🔴
این پهپاد توسط شرکت SR2Vector توسعه یافته و برد عملیاتی آن حدود ۱,۵۰۰ کیلومتر (۹۳۲ مایل) اعلام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131697" target="_blank">📅 09:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131696">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فرانسه و بریتانیا آمادگی خود را برای استقرار یک نیروی چندملیتی به بهانه حمایت از آزادی دریانوردی در تنگه هرمز و تضمین عبور ایمن از تنگه هرمز که یک موضوع با اهمیت جهانی است، اعلام کردند.
🔴
فرانسه و بریتانیا هر دو همچنین بر تعهد خود به ثبات منطقه‌ای و احترام به حاکمیت همه ملت‌ها تأکید کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131696" target="_blank">📅 09:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131695">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oIGWYLMFYyfLkjA9jTh-p9_9C161paLOQqbgfakVwxo8hbqFcNUWigZJ6ZoE2f0lRJFeou0Y9tcI5IVMSne-S2nGx1wmOzoC0xeS7n2bJ0Dty8ILTviD9on78HTLJ0jJITfNORY5SkCOPgDLCojxghKqDXoHhbTQ0EIomHdtsTIavd3OX8xCVFqoKgnjX0VpPBj9tN8hwOzZF0i9quDvXvvrFrkYaGfaUVZJtzEy7Zv5Wv9y-FSii67jx22vtR558CtPTxNBBsW5odYkYvYlFRVB88GBg231uLteD2CEG7jdKtBN7hUYQAYv9LsgX1AMWWP7qBp6kl2KnvVl84QlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی اسرائیل در نزدیکی تپه استراتژیک علی‌الطاهر، در جنوب شهر نابتيه، لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/131695" target="_blank">📅 08:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131694">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
متروی تهران از امروز ۲۴ ساعته شد
🔴
مدیرعامل متروی تهران: تا ساعت یک بامداد روز سه‌شنبه، ۱۶ تیر، خدمات مترو به‌صورت ۲۴ ساعته و رایگان ارائه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/131694" target="_blank">📅 08:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131693">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
منابع محلی از حملات توپخانه‌ای اسرائیل به منطقه «ارنون» در جنوب لبنان خبر دادند. گزارش‌ها حاکی است اسرائیل این منطقه را هدف حملات سنگین قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131693" target="_blank">📅 08:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131692">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeebf5f487.mp4?token=IHLeXRxRoKYbVuiibgyEJ9QLZ66luOL7Xrm5IpvZJvJnqHOcxY5bcvvKlUKc3SUE5UC_J4x5PZkk0OddD_BWMeQL3HIDpkK3hUaivGHtlyi7RHyNp0aPdcar-Pk8NRRf6oyF9Ap2lv02ff7IB66daimorKvZzwejHft5MoxgoJBpashRGMeMvqPdaxWc9bBrqe1zXpa0fbqnkGa72eBDtl6gbG6kapfNTFyRIcjvabwxDnlv4tSA88fPxXs-V4lrc5M3iE8NEz7WBO8qyY6Fba-S6ZQ5jGSobjWEYQ5vG9sH7Lchiv9QN-SvcBfJvPYKiuWjR3hsTzW5yLonkW0h5miIXKy5v89aSsCxDOULlnDyF0vjyHmySX94D31fsIdII36nPnIVXye5h_PUs1t4bIwdJHYJOxy6sazC_OF35J2K6aXLqo9HL-gY-1VUb8TivpBL_8sIF_iSZoJWIIseut4CuIMaDqIBjnt42A7PruqT__GXEnjY2augZ2CYytVrGXnHO_2yVGLyoxe10hR5Bhul3jnVmuqtjgzOkjicTqRmUJSY2aMAuAjeaPxtSepRcMi_YPfMj0Ixw5r4493Db1p2jM0P2u2KA8CSUKDTtSEBEO2Q7mOqfBg5aC4KMabl2Zmi-cVixNaxTcGMPZdBEadZ3JTxECY3A6S_3E8XJ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeebf5f487.mp4?token=IHLeXRxRoKYbVuiibgyEJ9QLZ66luOL7Xrm5IpvZJvJnqHOcxY5bcvvKlUKc3SUE5UC_J4x5PZkk0OddD_BWMeQL3HIDpkK3hUaivGHtlyi7RHyNp0aPdcar-Pk8NRRf6oyF9Ap2lv02ff7IB66daimorKvZzwejHft5MoxgoJBpashRGMeMvqPdaxWc9bBrqe1zXpa0fbqnkGa72eBDtl6gbG6kapfNTFyRIcjvabwxDnlv4tSA88fPxXs-V4lrc5M3iE8NEz7WBO8qyY6Fba-S6ZQ5jGSobjWEYQ5vG9sH7Lchiv9QN-SvcBfJvPYKiuWjR3hsTzW5yLonkW0h5miIXKy5v89aSsCxDOULlnDyF0vjyHmySX94D31fsIdII36nPnIVXye5h_PUs1t4bIwdJHYJOxy6sazC_OF35J2K6aXLqo9HL-gY-1VUb8TivpBL_8sIF_iSZoJWIIseut4CuIMaDqIBjnt42A7PruqT__GXEnjY2augZ2CYytVrGXnHO_2yVGLyoxe10hR5Bhul3jnVmuqtjgzOkjicTqRmUJSY2aMAuAjeaPxtSepRcMi_YPfMj0Ixw5r4493Db1p2jM0P2u2KA8CSUKDTtSEBEO2Q7mOqfBg5aC4KMabl2Zmi-cVixNaxTcGMPZdBEadZ3JTxECY3A6S_3E8XJ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: در آمریکا، ما به زبان انگلیسی صحبت می‌کنیم، زیرا این زبان، زبان بنیان‌گذاران ماست. و برای هزاران سال، این زبان، زبان آزادی بوده است
🔴
یک آمریکایی همیشه خواهان صلح و آرامش است، اما ما هرگز از خطر یا تهدید فرار نخواهیم کرد. ما همیشه خواهیم جنگید، جنگیدیم و خواهیم جنگید، و همیشه پیروز خواهیم شد، پیروز شدیم و خواهیم شد. ما باید این کار را انجام دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131692" target="_blank">📅 08:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131691">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: شما می‌توانید به کارل مارکس وفادار باشید، یا به آمریکا.
🔴
شما می‌توانید یک کمونیست باشید، یا یک وطن‌پرست. اما نمی‌توانید هر دو باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131691" target="_blank">📅 08:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131690">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd5cf7670.mp4?token=XTuZ4NM10WK9UnSmeiEmV8uEi-ip43mtae5io_KqUFRkwRWQlU3NOk5RZZF9083miTz8KFobtmtt2aKfCItZDY1Vfi0ektC9YEV2mS6EF0zCC_rSOtJLL_tQiHl1gKz0DQTX1otyNCjMYISs1pEnoVMmVqAGRg6YTdWLl0DVa6__EI2xrtToarbwlNtGhVYSWxL0T_O3s1gZ_UvMcvooOTkp6W7OMYFUnRuuPJlpIib2FUDjuLSreYLsPEt6sXc1P4mIRhm9b8iQ4H-WE3IsoyNzVxHWkknwCfDHRsvhDpa_v6mbLrOVcWnMf6YKPPR0nI6VKJmnMYAwC-HhZ2C-0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd5cf7670.mp4?token=XTuZ4NM10WK9UnSmeiEmV8uEi-ip43mtae5io_KqUFRkwRWQlU3NOk5RZZF9083miTz8KFobtmtt2aKfCItZDY1Vfi0ektC9YEV2mS6EF0zCC_rSOtJLL_tQiHl1gKz0DQTX1otyNCjMYISs1pEnoVMmVqAGRg6YTdWLl0DVa6__EI2xrtToarbwlNtGhVYSWxL0T_O3s1gZ_UvMcvooOTkp6W7OMYFUnRuuPJlpIib2FUDjuLSreYLsPEt6sXc1P4mIRhm9b8iQ4H-WE3IsoyNzVxHWkknwCfDHRsvhDpa_v6mbLrOVcWnMf6YKPPR0nI6VKJmnMYAwC-HhZ2C-0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
🔴
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/131690" target="_blank">📅 08:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131689">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx23J6HuP8jJilSuAHxjqqjtp49JKloNQRIfJfao9dRItqEqBxITGZiaNC1mcELhNBsT8fn4UUT7bvYLdwJEJd6_FH1dESIxM2KQ_27Z-wu1P43j3vW0DA6P3AJLb_VyQrYefER7Cxhk6xvGsVL5mdeKVccG-DcFQXdcE2tupMsMKnQCCSOrKh57_5sZM6x9_jo2iCuwX2ETn6LXGLCMBf4rz7qoml7fcgjZ7v26Bu4DWAZ-QeJJqj9n7n-FHw8xu1geYTml2RW-scpOQqko-HDhjY6NQtEatzNC_9Z9EOOadYQYiQixv40VyOKfjIzLi2YT0DDs554RrZGmx4hnjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بزرگترین سایت کاریابی روسیه، برای دفاع از آسمان مسکو از دست پهپادای اوکراینی به دنبال استخدام داوطلبان اپراتور پهپاده!
🔴
وظایف این شغل شامل آماده‌سازی قبل از پرواز، شناسایی و جمع‌آوری داده‌ها در روز و شب است؛ تنها مهارت‌های فنی اولیه رو هم داشته باشید کافیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/131689" target="_blank">📅 08:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131686">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_B8G8qUSTMWSV8G_9OMmZuxg2ZlHtQ6mi8Uh-qvHlx6mpqyz0ykbQ8pdHXJ9Z5GC9NjnDNpDkAcshd4Cyh6_A1V_gyHhsxYldOWBGdIuLFVCPVMVIlBSZ_ZSS6T_z9N_fh9KihHFiS78Uz3-FcBsUIMtfARy-NgZJ8tN18EMGYKXOHYV5q7JHnKc0FJdkyQek7crX7u-b6owSrDFzu5s2c2XcilsSp4WpWraHPX6Wdtj9-aXLL3hUKXPlJOwBmn_oSs-vkl2hpwLkAIcU84vP4MlF4bYyh1yrvMP7ZuLv3C1VYS0a0IMu9Q76KM_3Q-i92agd0CF7ldKZWQ8WAk_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0E34bijyjBTEDjdbX7eJhI_bEiEcjy0AacbLD8z28LyGZpNVPeX1nMHlQ49daGKyDD8HL_o5t257CdIsJCouuHuv2zvdxDwUfVEt1gD5y-HcW1Vz5weRYKF_YPCTelbas1ZrYGkQjf3XHV79zsslZbRsubWAoj6M2HWo8_8Umkq8ZGgmok2-dprKHMoqpomelWrWMIHFUdmkln6nX8oNtit2ZpJsADIAuCUdFfeIeDWsSqqkWaNBU6yHkoruYgmUz6DG6OES-9mXF1wnl_x-y586KEwKtKyTa-1fXjRltZHmp9-i8OUpdzGuBfkCQD23dtwUSs8c5QQlcgjVUVTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPaxm8YVf75o9Drk7L_dwdAeLpPzR9pZD6GDOimfgHez_bftpE31702-zpoV1fXYI_vDbY5pf0j3XrllrYU-fggTujWJEsRyeZyQRiqlUjAHdpPXvJPWHaD8wcTwgZg_H4Chpb87sGylf-e3Fh0nkn71IyI9mXo5MJFRO4LEHR4rEs598iaBPHBMKQgBsdruqsFYfS8eX57QNqjYwv7RIlgWIW94k768WNjVnqRh9TLXG4MnNSvBHbZXndoV25FOItPfTNBp_gyyQhT_EMvshUy1ML6mPBwYJAD7VfTLJou1h5CV0Vl9z8rXadh2wSXypWb27nX_9fUp4tpukueszg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/131686" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131685">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=C4U76qUDUCSZueNoynzlhtO7u8Iu7RZRoVjf6Tbk04PPhz4cr6fAaKMfxZPrD4sXGeIq9yx0kb92AuWJl8jVBWT0_7b86hx4j-wl4NO_7JQu4zw_0CAudQCYffyJMXEfhGQMrWbXlcH5nOI5n_Hh17hxM77b9-s_mt_zSbvqi9FwlTl4Vg8B7Xw3JZf27K5YSnWws3XlHX7Rugmm07kWyYiO3Ng2vuAdoBHdhEOB_K-OAlxvZI_YTkq5K_ufPYY_HtRFuPdC4rqEsOM6i7uVYxUR4yMpnJYYEmDtHAx4kofdudFW-fOoW-H7-VsDOSsUnBHhlD9EVFteDrlIGELXVgAmRSboSa9Ra8bQFeUyePh6f4Y2mujIWX4UOjnvbrDZAqR_GpggnKCEKCbhOn1LGTBOcP_Dbc6lOt-IZhJViUt3emIOUwfYz_jO1lEfEWkmL3DotxVcaROzVCRkWFoXVjOqQ5r6qKYVU8C7c_LjVMraKKtG8ZSYSdvKZ_2clDdr5NJuyNIvSpyMU8PH2WDNJ69oyE8Ptx-QWmLI8UYUjlNF8nzEfpw260rRxiTzbttQxLgsM2HPcmMH9z4VK2IQIoQ_mi4th9Yhaq6CVBtdvJ1U_MF3Y3kAkg4DhfS-ojif-mEBK53HobAHZtwl0tNXWKDB5bNhijxjurvy8hYNAbM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=C4U76qUDUCSZueNoynzlhtO7u8Iu7RZRoVjf6Tbk04PPhz4cr6fAaKMfxZPrD4sXGeIq9yx0kb92AuWJl8jVBWT0_7b86hx4j-wl4NO_7JQu4zw_0CAudQCYffyJMXEfhGQMrWbXlcH5nOI5n_Hh17hxM77b9-s_mt_zSbvqi9FwlTl4Vg8B7Xw3JZf27K5YSnWws3XlHX7Rugmm07kWyYiO3Ng2vuAdoBHdhEOB_K-OAlxvZI_YTkq5K_ufPYY_HtRFuPdC4rqEsOM6i7uVYxUR4yMpnJYYEmDtHAx4kofdudFW-fOoW-H7-VsDOSsUnBHhlD9EVFteDrlIGELXVgAmRSboSa9Ra8bQFeUyePh6f4Y2mujIWX4UOjnvbrDZAqR_GpggnKCEKCbhOn1LGTBOcP_Dbc6lOt-IZhJViUt3emIOUwfYz_jO1lEfEWkmL3DotxVcaROzVCRkWFoXVjOqQ5r6qKYVU8C7c_LjVMraKKtG8ZSYSdvKZ_2clDdr5NJuyNIvSpyMU8PH2WDNJ69oyE8Ptx-QWmLI8UYUjlNF8nzEfpw260rRxiTzbttQxLgsM2HPcmMH9z4VK2IQIoQ_mi4th9Yhaq6CVBtdvJ1U_MF3Y3kAkg4DhfS-ojif-mEBK53HobAHZtwl0tNXWKDB5bNhijxjurvy8hYNAbM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس :ساعت ۶ صبح بیاید مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/alonews/131685" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
