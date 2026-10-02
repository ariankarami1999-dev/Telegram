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
<img src="https://cdn4.telesco.pe/file/LKUcJOMXwon0mKhbhlO5EuKDeiQnQUbLK71hd4w0xXNyZkC42PpXKYogpOmJRmq-Y4oA9SNmbty7xOX4JxsbAoJdaeJQ4tOzj7pMoPl4fKqckU19PYWCPuDgE-PxSNZk-D-FAlyXKhTbyhIoYORKLRPKNq1UxjrkJIEHE6Ym3bYVQgl8OTXcFTBoVw1R5iwV8NhMvuy9xHZavcgdxgmeIa6qjpL5h9F-RCWkdp9pUiRlexj-q9ts2XdcOGAOnhiLkNiiErULk6uhnutyXQVXc6ksF_thUIItdfbnx4AibW7enpBFPZYzf1B4ngbZzijzpxJh54C41bPe-YVhrcz9og.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 05:52:28</div>
<hr>

<div class="tg-post" id="msg-150501">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromver2 vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hqg5sNg3n1zHcBW8-unG4xg8dvUBIIrhUCEjb_rikTq-q7tQXfM1YG4eFHrqtAP747aPQUtFBK1wgwi3zfp6n_-wf9Nl90giLh67P89_zJa1FPs3Up8W_5ldKU2RuKpwSg1UcYYCaNUgFBNzlxiNUBZY3OtIE4ntCdDOxwfc8Z2UPUdnaBOUGyDxMdTME47xWUI8Gdh1YXxXapY9N2tIeT-u0MRRczLBZ4UHDRnIC_1Sv8-dWpbm8OJ6qbh7DgZj-hQO8_NCHXdYXrgRzEh3Ur7ktsgeZlM93ogm-9eYB8Q2t2KHBxxf1-TQ3ZoHViTaSj_GoBOugJktfuJo2ESEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط هزار تومان!!
🚀
--------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
قدرتمند ترین سرور ها در جنگ
💥
سرویس های تانلی بدون قطعی
💥
سرعت بی نظیر و IP ثابت
-------------------
💬
تعرفه ها
🔸
سرویس ver2
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود ver2
▫️
تک کاربر — 200,000 تومان
▫️
دو کاربر — 250,000 تومان
▫️
سه کاربر — 300,000 تومان
🔸
سرویس ver2 ویژه
▫️
10 گیگ — 40,000 تومان
▫️
20 گیگ — 80,000 تومان
▫️
30 گیگ — 120,000 تومان
▫️
50 گیگ — 200,000 تومان
▫️
100 گیگ — 350,000 تومان
🔸
سرویس اختصاصی
▫
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 300,000 تومان
▫
100 گیگ — 600,000 تومان
▫
200 گیگ — 1,000,000 تومان</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/150501" target="_blank">📅 01:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
اسامی ۸ شرکت خودروسازی ایرانی که امشب تحریم شدند
۱- ایران‌خودرو
۲- ایران‌خودرو دیزل
۳- پارس‌ خودرو
۴- سایپا
۵- زامیاد
۶- نیرو موتور دماوند
۷- نیرو موتور شیراز
۸- هپکو
🔴
همچنین راه‌آهن و شرکت قطارهای مسافری رجا به همراه چند شرکت فولادی نیز تحریم شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/150500" target="_blank">📅 01:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ: ایران به‌زودی پایان خواهد یافت؛ به هر حال، یک‌جور یا جور دیگر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/150499" target="_blank">📅 01:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj3_zNAMKIyUNRBDG2wdy2dy5_0LL-Yfu_wkEu_0OLlS4cIyOlK6bwIUMn8OYcDHCLHKz3pbhKwZt-VJPuTuadOI87Mk2xFrw-_8DBA_qb6zVzLMFQBa2StMGvzsFrK1sW8F6YtJv9enNQMul18pJWxfbysLT_sLqZbiv1SPHuAGWkqGDx9D8Q7wrz261_8MkstnHfQfVrzYxI3JIijeyDm5Smm4lbwlQqHyQHMl9TZqkhLd5WMtu9B9l2Fu8t2nFpnzlrmr1SBo7t5cpBvu2aw6D9hjBvxVGyaBgvf9a9I1VFL6xhkUMzBLwpmkBcRl3wgvpJCTJrS14hXukmDqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: ما قدرت اول جهان شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/150498" target="_blank">📅 01:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qp5crZPPYsAMQeFI09_FMkllMAhMoynebt4ZKQIBpX8_pN89VfxAY-otc3UKuby08_Fj-4SaQDegjANnofm02r3pOcw6_kXWxpClpA9rEMlOdsFozoyPLTCpzDAHS-NfCGqqObLtq_8Hqm7wTWPxnVrTM32XiopmpPbcrKSUYySGqsD46-PyccQaPtOsyoPZ3tRk0oYfXlwuyg-cw__OpAxwtDkUxArKNHSefjJjuiP6m1OvxKOO38ENutG5QQPsTFuCWMePa6Qa9YDoyWYt9q3WyqSFi_Yo3H7wCqBV8uOBhUcbnvkdSp8ZHbtNb5puKL7XbORx_KXwwebxgMYlxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
سردار قاآنی:
آمریکا رو ما از عراق بیرون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/150497" target="_blank">📅 01:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150495">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9371c09764.mp4?token=u7iZfE3aelgF7zU6SOYkLiLKdz-7iaGgFcLNZw67okcyhQUD1ggWXx0OU9mzJVQ3HdKqxSp9M5hNfdYVTHWoDIcJ94Qra9kDU_1K6xUuFVP8TF8TsSMO-4papySkoXiaeAolc9R8c9HY2e6HNA1MdDV5qlwYe32_YQyjAG4U7txOzKVDX6WUYLDDBOmM8ScIL8Zyy02j67zML9PHjXFaUqCEXB1ervgLiojrYCopAVhUwfyugvN6BZgWlsMRQu70jqG59yHI41yPssCgxJb_w477W_KTSLv8fo8OmfiRwMgS2D1tT5mKML41f7NRLJAwUKiYkv8mu1ONhwK0qMg2kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9371c09764.mp4?token=u7iZfE3aelgF7zU6SOYkLiLKdz-7iaGgFcLNZw67okcyhQUD1ggWXx0OU9mzJVQ3HdKqxSp9M5hNfdYVTHWoDIcJ94Qra9kDU_1K6xUuFVP8TF8TsSMO-4papySkoXiaeAolc9R8c9HY2e6HNA1MdDV5qlwYe32_YQyjAG4U7txOzKVDX6WUYLDDBOmM8ScIL8Zyy02j67zML9PHjXFaUqCEXB1ervgLiojrYCopAVhUwfyugvN6BZgWlsMRQu70jqG59yHI41yPssCgxJb_w477W_KTSLv8fo8OmfiRwMgS2D1tT5mKML41f7NRLJAwUKiYkv8mu1ONhwK0qMg2kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مامور های عربستان یکیو دستگیر کردن که با خودش انتحاری برده بود سمت خونه خدا که منفجر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/150495" target="_blank">📅 00:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
احتمال مجازی شدن کلاس‌های دانشگاه‌ها افزایش یافت!
🔴
معاون آموزشی وزارت علوم اعلام کرد با توجه به شرایط هر دانشگاه، به‌ویژه در صورت گرما یا سرمای شدید، ممکن است بخشی از کلاس‌ها به‌صورت مجازی برگزار شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/150494" target="_blank">📅 00:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
منتظر افزایش قیمت وحشتناک ماشین های ایرانی باشید.
🔴
ایران خودرو، سایپا و راه آهن ایران تحریم شد
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/150493" target="_blank">📅 00:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
میانگین درامد ماهانه (ناخالص) همسایه های ایران:
ایران 80$
قزاقستان 780$
روسیه: 850$
ارمنستان 750$
آذربایجان 600$
ترکمنستان 300$
تركيه 800$
عراق: 600$
افغانستان 100$
پاکستان 200$
عمان: 2000$ کارگر ساده تا 500$
امارات: 4200$
قطر: 3800$
بحرين 1800$
عربستان 2800$
كويت 3200$
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/150492" target="_blank">📅 00:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ویدیو ‌وایرال شده از تلاش یه موش برای نجات خودش وسط سیل گرگان  [@AloTweet]</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/150491" target="_blank">📅 00:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=qnv7JCv4e0B7t8SruEe_lxbeEq6PfM6gMydz2fzxVPsOLL4rY1jNjHO-S_bEnFzbBDLTLuonLOvFUV_LvIZ4B1mepuPESwAoIrTr6x3hXhTY3PdWMK07dye5F-4zbDuH2PfM-69zn5YZHxjrvai0rkZpk4exKIP1_od7F-thgqEnu0Oz9Y9Pk0sbOuyjHyNgP0dRgtprBpUVeEsz8Ms5cBRA4jgOaLKBLg4iOach69JI9Mrb7zJCT5VChgJ6f6vrV5Jiz9tMmtzm6T8ajyJsSVA67x7-jmGxA1t1bCTwGlejTLhM9WPLilEvXykDcUWGCZ9bVEXQczyRgwB10YJYmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=qnv7JCv4e0B7t8SruEe_lxbeEq6PfM6gMydz2fzxVPsOLL4rY1jNjHO-S_bEnFzbBDLTLuonLOvFUV_LvIZ4B1mepuPESwAoIrTr6x3hXhTY3PdWMK07dye5F-4zbDuH2PfM-69zn5YZHxjrvai0rkZpk4exKIP1_od7F-thgqEnu0Oz9Y9Pk0sbOuyjHyNgP0dRgtprBpUVeEsz8Ms5cBRA4jgOaLKBLg4iOach69JI9Mrb7zJCT5VChgJ6f6vrV5Jiz9tMmtzm6T8ajyJsSVA67x7-jmGxA1t1bCTwGlejTLhM9WPLilEvXykDcUWGCZ9bVEXQczyRgwB10YJYmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سؤال:
«آیا ایران در
حادثه پایگاه RAF فرفورد
نقش داشته است؟»
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا:
«
بله، به نظر می‌رسد همین‌طور باشد.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/150490" target="_blank">📅 00:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
👈
رویترز:
پس از گزارش ها از اعزام سومین ناو هواپیمابر آمریکایی و نیرو های تفنگداران ویژه ارتش آمریکا به سمت خاورمیانه،
قیمت نفت هم اکنون به شدت در حال افزایش می‌باشد و مجدداً از 100 دلار عبور کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/150489" target="_blank">📅 00:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8a55537b.mp4?token=A8YcWKBRU1kKMJ_SqoZ7e1-Bq6-ZDnOFm3vIWPqwoJ3golrnWmQUhYa9IV3CJReWzEXJWBReBOqps84IOZmZ1Sb4-9D1K3CLwC_GUlAZ7x4udC3Lf-IpU2c-yU3-DVMN4hSMrFOPaB1EIn5hSHQEj83V0Rwk5t6MAPD3w0G7E_3YrK-LgU1nEEtQJLRIsCrqObbLxFQVGMEu_gpwwMWtLpOazvDNJ66PSepaOxGXNjl_RQubyKQJcXTEWHEQB8mV5O3US6Z6aOSdV9nhB6bX2e1nCZA_kFHmTuKLxklAGIUho9100rtFEXXGB4vtzOA6T-Lvff4i0tVMBvdQtBHIng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8a55537b.mp4?token=A8YcWKBRU1kKMJ_SqoZ7e1-Bq6-ZDnOFm3vIWPqwoJ3golrnWmQUhYa9IV3CJReWzEXJWBReBOqps84IOZmZ1Sb4-9D1K3CLwC_GUlAZ7x4udC3Lf-IpU2c-yU3-DVMN4hSMrFOPaB1EIn5hSHQEj83V0Rwk5t6MAPD3w0G7E_3YrK-LgU1nEEtQJLRIsCrqObbLxFQVGMEu_gpwwMWtLpOazvDNJ66PSepaOxGXNjl_RQubyKQJcXTEWHEQB8mV5O3US6Z6aOSdV9nhB6bX2e1nCZA_kFHmTuKLxklAGIUho9100rtFEXXGB4vtzOA6T-Lvff4i0tVMBvdQtBHIng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مداح: مجتبی خامنه‌ای ولی خداست
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/150488" target="_blank">📅 23:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ایران اعلام کرد که 3 نفتکش امارات را شب گذشته در تنگه هرمز با موشک هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/150487" target="_blank">📅 23:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نیروی دریایی بریتانیا گزارش داد که یک کشتی در تنگه هرمز مورد هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/150486" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZr4sGp5VELibmunxgZuqn55fUn6ValfJknvz5gWsNUlAn7NFu-0HkbWtA_WuzxY25GqgPNSuhtNh_K4nQc9b6HkOonSHs5S7w6RakdiOJl3R1tCklEU1AkKsb7KsfHSKhk0rvLxFmBkOJB2JZqkqRaHIIGbBJZRwZA54jRENarZKM-z3uYggyLraqi6-rH5I8d5jertSW4K2e1MMfxWOk4ptkmc2pP6aD6KX_-V9Qw_d2-kAS6flc3lQf16paX_m3EoU7somJHccxZT1SgL2Ocvcw9y1fM3TDFprI7pZEx6Cl-sdh6aJ6ch_WhgBTQo_8Vnxyw5aQnvz1HLtCmqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی: یه مشت وطن فروش با تیم‌ملی دشمنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/150485" target="_blank">📅 23:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت خارجه ایران: خواهان بازگشت برقراری پروازها میان ایران و عراق هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/150484" target="_blank">📅 23:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
تحلیلگر فاکس نیوز: نتانیاهو مصمم است تا قبل از ۵ آبان به ایران حمله بزرگ کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/150483" target="_blank">📅 23:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پزشکیان: اگر در مصرف انرژی مدیریت کنیم هرگز کم نخواهیم آورد
🔴
ما سه برابر انگلستان گاز مصرف می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/150482" target="_blank">📅 23:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
یک انفجار گسترده که گفته می‌شود توسط اسرائیل انجام شده، در منطقه المنصوری در جنوب لبنان مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/150481" target="_blank">📅 23:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150480">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8n1OFoueRGL2tE7nxYKb3yKejXEhcC2gi2E-RQCXcBuHeABC3Q4XBiRw0hCB-lG9xvjOmM3cTHDvwFxXVU5MI4lDob28beapZggmoFVlwREs9YH7yFqmK1DVyLKAI7s75bo9Ol0pqBPIa8S0C5CMC2BlxPEEv8kE2p9k8JOFC9tfFG8uaQ4MtoYMNRex5Ff1JYC1TjkBlAqhzL4jWU6lLvG_ijngt5TmaWgLrNh_Ck46o-YedI_EyCnIODiIARBl3t0UEoGwC8k-qPr7Q-gRNrtXugDk2ycrKnBx4Cp3tdUkYqzI4_zZ1Re4F-Bomg478MnqWE5V0UNQoEHgmTdgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری آمریکا، از کشورهای اروپایی خواست ارسال و عرضه محموله‌های انرژی را تسریع کنند تا به ثبات بازار جهانی کمک شود.
🔴
او همچنین گفت نباید بار کمبود گازوئیل بر دوش شرکت‌های آمریکایی گذاشته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150480" target="_blank">📅 23:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150479">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚠️
اگه نمیدونی تو طلا و دلار چطور سرمایه گذاری کنی حتما اینجارو داشته باش
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/150479" target="_blank">📅 23:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فارس: منابع محلی گزارش کردند یک سوپر نفتکش با ظرفیت ۲.۵ میلیون بشکه که در مسیر غیر مجاز تنگه هرمز تردد می‌کرده در ۸ کیلومتری سواحل عمان مورد اصابت قرار گرفته و در حال سوختن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/150478" target="_blank">📅 22:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / وال استریت ژورنال:
10 هزار نیروی نظامی آمریکایی عازم خاورمیانه شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/150477" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
تسنیم: پلیس خشن و نامرد فرانسه امروز به معترضا گاز اشک آور زده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/150476" target="_blank">📅 22:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150475">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b019bf6e.mp4?token=EMiQ3LLWQ08Jp8GWyM1uwE6snWed5rmt1XfcWOzv0Vvn6p9KH-1PK4yQCUMLepc17iCAlSrZOixeYCcekBtqvoE3JGxLVoQWNuOBTg5wXss4JvmYFDZXG3PWT0sCcj3nL_V9CnFcFMwsMQYvmDGbrOzItj9K4BGpKFIbKU3zDaMFp-CEQ33-4xyWPV13hVmVyrJsikCHLTnHf1bFb3tMXK6TcG6Megt_5jI6IHX9sgTQ5JtIsKGDue1EGm05EBN3v3gyBYX0Dgn8Qm9Ns0PhxzwR3uOGy1rZrHeX7jTYOQbKXBgm_44Rue0bRJ-qjDSGlfw_Co7vd4xj51Asjp_cMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b019bf6e.mp4?token=EMiQ3LLWQ08Jp8GWyM1uwE6snWed5rmt1XfcWOzv0Vvn6p9KH-1PK4yQCUMLepc17iCAlSrZOixeYCcekBtqvoE3JGxLVoQWNuOBTg5wXss4JvmYFDZXG3PWT0sCcj3nL_V9CnFcFMwsMQYvmDGbrOzItj9K4BGpKFIbKU3zDaMFp-CEQ33-4xyWPV13hVmVyrJsikCHLTnHf1bFb3tMXK6TcG6Megt_5jI6IHX9sgTQ5JtIsKGDue1EGm05EBN3v3gyBYX0Dgn8Qm9Ns0PhxzwR3uOGy1rZrHeX7jTYOQbKXBgm_44Rue0bRJ-qjDSGlfw_Co7vd4xj51Asjp_cMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین، رئیس‌جمهور روسیه، درباره سوئیس: «ما از بی‌طرفی استقبال می‌کنیم، اما اگر قرار است سوئیس بی‌طرف باشد، باید کاملاً از تمامی تحریم‌ها علیه روسیه کنار بماند.
🔴
بی‌طرفی نباید فقط در حرف باشد. سوئیس چه چیزی به دست آورد؟ هیچ چیز.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/150475" target="_blank">📅 22:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150474">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کارشناس صداوسیما: ژاپن توسعه داره ولی هویت نداره و با کشوری همکاری میکنه که اون فاجعه هسته ای رو براشون رقم زده، مردم ما نمیخوان مثل ژاپن باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150474" target="_blank">📅 22:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150473">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onTVWEw6WDUqyJQuQV1tSj8zKM9LRT5Lyp2Ht6-3FYZsSrydRbF-ti9d24jN-43VyXeOCnqe748ISkPvnG3X_p3xIMTsetZmHCOAkjUtDOMxpiQcC_UjjL7TnpNYVkXYcVSRAKMeeFLi3i2vNlgMlMbHlK_JnsASZJUhgPQ3rF6v1H684SrPlRnq56I26FJaacxg_zfcp_-wfEwaUXulsKe67wWjeFLUsJ8TpUE647KmxeU8gujxp2SHPW-VsHpKS0EuZa6ZZkAWaJTKDAIwW8aKGwecaC3Lf3bKMoq1CsBYnhvhqogtECt6P0o54BaXKSD5ohwXQZNLRsEWWnv_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : قیمت‌ها به طور چشمگیری نسبت به زمانی که بایدن و دموکرات‌ها قدرت را به ما تحویل دادند، کاهش یافته است. به همین دلیل بود که من انتخابات را بردم، و اکنون قیمت‌ها به سرعت در حال کاهش هستند.
🔴
این تقصیر دموکرات‌ها است، نه جمهوری‌خواهان - اما ما در حال رفع این مشکل هستیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150473" target="_blank">📅 22:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150472">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
بلومبرگ: ایران به‌طور غیرعلنی پیشنهاد کرده است که در ازای کاهش تحریم‌ها، دسترسی بازرسان هسته‌ای به تأسیساتی که در جریان جنگ آسیب دیده‌اند را دوباره برقرار کند
🔴
امتیازی احتمالی که هدف آن شکستن بن‌بست موجود در روابط با ایالات متحده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/150472" target="_blank">📅 22:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150471">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
منابع عربی: ایران پیشنهاد داده در صورت کاهش تحریم‌ها، اجازه ورود بازرسان هسته‌ای را صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/150471" target="_blank">📅 22:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150470">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
گزارش‌های اولیه از شلیک‌هایی به سمت تنگه هرمز منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/150470" target="_blank">📅 22:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL1Upf3fsRMoPDfh0jzIfCyN_4tJ7VjqP8CJEQ9p04l_7WKFrLCBSyhO3Jmvbyt3lKcSRQhKXSb-LtAjgXQ1wYY267I2KVgiqzGFsUY81-UhBaFUl9Ish-UzP6-I5BDCC0UnAPi4WWOmJ2Cw6oKIw2omlXKYNzbR1U56Rx2hwHB_9O5EdoRBEQe-_OEX9KLL9eNemVCZMtsjvYD1dp6LQfglO4RuvbeueMCHXhfHQEtx2bf-Twf6s-cLcRfoInbznfBNIde069K2_VoHSvKv1ARrBoqYtVRslr-nRG8kBuNxMakI5TtmjxjCUq0FoGhGQNNIHGkct5A2H4fuDDTxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983fb64c5e.mp4?token=s_n9h0QSNBajuo2aHe1Sj_O4AfIQYDMaApdy_K1BLgW5I7Z-4DxIrbqCyozgnvQfN8_gwIEXMgPNCvMrwsCNdSXDQKafTXscQmvF3xbZAwF0yOFCDOZPhMA2mOXBsaa1vEuzcJVw9SYp6PnGU6tBdo5jBwJ03ZVPPRk8hw-VcSkZwlt5DJDMSxdIs4rs8-YKN8kbCuVB-fVypv1YitBTHWFN-SCXu5uz09pV7As2lkaNMJXKvyEzr43B69_3aByoeJ1FtaEEDffyqZzSdGoT7JyBn7IkYoaOTyUiJrC_eBquCBIdFWxCp7yPGeCAcvkqvsHClzw8nHSYjlWXgcTmUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983fb64c5e.mp4?token=s_n9h0QSNBajuo2aHe1Sj_O4AfIQYDMaApdy_K1BLgW5I7Z-4DxIrbqCyozgnvQfN8_gwIEXMgPNCvMrwsCNdSXDQKafTXscQmvF3xbZAwF0yOFCDOZPhMA2mOXBsaa1vEuzcJVw9SYp6PnGU6tBdo5jBwJ03ZVPPRk8hw-VcSkZwlt5DJDMSxdIs4rs8-YKN8kbCuVB-fVypv1YitBTHWFN-SCXu5uz09pV7As2lkaNMJXKvyEzr43B69_3aByoeJ1FtaEEDffyqZzSdGoT7JyBn7IkYoaOTyUiJrC_eBquCBIdFWxCp7yPGeCAcvkqvsHClzw8nHSYjlWXgcTmUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در‌تروث پستی از اعتراضات ایران منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/150468" target="_blank">📅 21:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزارت کشور عربستان: تحقیقات اولیه درباره حادثه هواپیمای شرکت هواپیمایی دبی نشان می‌دهد که خلبان توسط کمک‌خلبان مورد حمله قرار گرفته است
🔴
خلبان هواپیما و کمک‌خلبان آن، پس از بهبودی کامل، صبح امروز همراه با یک تیم امنیتی اماراتی به ابوظبی عزیمت کردند.
🔴
تحقیقات درباره حادثه پرواز دبی توسط مراجع ذی‌صلاح پادشاهی و با مشارکت یک تیم فنی از کشور امارات انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/150467" target="_blank">📅 21:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن: در ۲۴ ساعت گذشته، جنگنده‌های سعودی ۴۷ بار به یمن حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/150466" target="_blank">📅 21:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بچه هاااا
من هیچ وقت تو زندگیم شانس نداشتم که چیزی و برنده بشم. امروز گردونه صراف و دیدم، چرخوندمش بهم 3 صوت طلا دااااااد
😂
فکر کردم الکیه تا اینکه ثبت نام کردم نشست به کیف پولم
😐
😂
شما بزنید ببینید چی در میاد
👇
https://r.saraf.app/s/agrd346</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150465" target="_blank">📅 21:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
صداوسیما : فرانسه با معترضین دانشجو و دانش آموز به خشونت رفتار کرده و گاز اشک آور به سمت آنها شلیک میکند و حقوق معترضین را نقض میکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/150464" target="_blank">📅 21:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150462">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8620d94f.mp4?token=egsjGnNwsghaocd_iwvBT9_VuC2NRkblJpOdbePmlAjXoIHSAxG3F5lfEDRcKv6-8j2ooklsEW0vIra6ZzwS9yY79CbLMsMVzRejDyztS3wYv71mxFWMilqukixu7bf0Wm7M6S_Gt7IK1D7t8CuDtlITCK_SzZQTfwwbWovQx-tZqWVui_hwLNLMWjP5SPDVGHdn9Uh-KWKRdu-fYqs3Bw6mU69MLAIKA8HWpzAigGxC-hnu6V8QQI-7Of5wYx18ugUmOJ45gRKZ78DkNW_4XVqEPkvNo32745ySXQw1tTZ3QJ9hwlyZ2dmiZErQE6PJnmucqfD5mLxyLZNS7VrkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8620d94f.mp4?token=egsjGnNwsghaocd_iwvBT9_VuC2NRkblJpOdbePmlAjXoIHSAxG3F5lfEDRcKv6-8j2ooklsEW0vIra6ZzwS9yY79CbLMsMVzRejDyztS3wYv71mxFWMilqukixu7bf0Wm7M6S_Gt7IK1D7t8CuDtlITCK_SzZQTfwwbWovQx-tZqWVui_hwLNLMWjP5SPDVGHdn9Uh-KWKRdu-fYqs3Bw6mU69MLAIKA8HWpzAigGxC-hnu6V8QQI-7Of5wYx18ugUmOJ45gRKZ78DkNW_4XVqEPkvNo32745ySXQw1tTZ3QJ9hwlyZ2dmiZErQE6PJnmucqfD5mLxyLZNS7VrkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما خواستار محاکمه محسن نامجو و بیژن مرتضوی شد که به کشور برگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/150462" target="_blank">📅 21:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150461">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کانال ۱۶ اسرائیل: اسرائیل در حال حاضر هیچ نشانه روشنی مبنی بر ارتباط خلبان عمانی با ایران ندارد؛ این در حالی است که رئیس‌جمهور آمریکا، دونالد ترامپ، پیش‌تر چنین اظهاراتی مطرح کرده بود.
🔴
در حال حاضر هیچ اطلاعاتی که دخالت ایران را رد کند وجود ندارد، اما هیچ مدرکی نیز برای تأیید آن در دست نیست
🔴
تحقیقات در عربستان سعودی همچنان ادامه دارد، اما تصویر کامل ماجرا هنوز مشخص نیست؛ بخشی از این ابهام به دلیل آن است که مقام‌های سعودی تنها اطلاعات محدودی از روند تحقیقات منتشر می‌کنند.
🔴
موساد و شاباک نیز از طرف اسرائیل در این تحقیقات مشارکت دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/150461" target="_blank">📅 21:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150460">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/150460" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150459">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/150459" target="_blank">📅 21:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSSW0VWOrjpREbIpJ3axRM7nCO6Age0YYMWoPYjZe5ibq5Dlltep__GWlsHyseHLyhL96KnJkOhc940TDu_geNProS8-4PZev7P0qKKRWy7yMrbTUnekA4WvIf5hofBtrgMIFuq1sHfXoxPY4XAkuTMGprEVaa9z4nCeQ5oWzrmCOe97uiefFUhQWdsyIpu0ijllG9Oiu6kzTwbub4Y80HwbeqBPtFFObeGAIAK0DKqz3ZQpy-dpQlOuaYKMJnnoU_YjBePcKFU3KKzx7WcTYh78EVWdut7WGIOhGdqpW-EYftbrdFxQL0BnsJvWrW90QAOohArvzaArvRG96eVqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
من بارها اعلام کردم که برای از بین بردن تهدید هسته‌ای ایران، به ۴ تا ۶ هفته زمان نیاز است، و من این کار را در یک شب انجام دادم! بقیه زمان صرف این کار می‌شود که مطمئن شویم این وضعیت همچنان ادامه داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/150458" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150457">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
پوتین: جهان از شجاعت و مقاومت ملت ایران شگفت‌زده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/150457" target="_blank">📅 21:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: تحریم های جدید ایران(راه آهن و خودروسازی) حامیان آن را هدف قرار داده و راه را برای خشک شدن منابع مالی این رژیم هموار می کند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/150456" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62a7d15bd.mp4?token=B82S42P1-zwyO5mscLJzZcmZ1e-AqyrSpp5SEv_mufDQWBbaseYvWbjeiIl8WHrCKxx668C84r6KVl0CMkP3nktWnOfSI8z9sZiDuG5o7uzZCp9P4Qk5g-dk6cdCRe-tjB2UxebOaa7XRRH6-fZenu9VICy4C-dZaZsDLBgYt4BWB9OPzPuovSjTZrSkcBOOnPy9qUbtWnJoZif5wYsI4E2TfdoRSh-CW54jXnq144Mnh98JcGjOuKkyNjWahqb3HYi54HA-l-Eee4nGcvDkTdx-u3L6-GBOoIpEZ8ebHN-a6IQur_mt0_1rDXtyKfdYFcdgdxicIww59hfEJa0pTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62a7d15bd.mp4?token=B82S42P1-zwyO5mscLJzZcmZ1e-AqyrSpp5SEv_mufDQWBbaseYvWbjeiIl8WHrCKxx668C84r6KVl0CMkP3nktWnOfSI8z9sZiDuG5o7uzZCp9P4Qk5g-dk6cdCRe-tjB2UxebOaa7XRRH6-fZenu9VICy4C-dZaZsDLBgYt4BWB9OPzPuovSjTZrSkcBOOnPy9qUbtWnJoZif5wYsI4E2TfdoRSh-CW54jXnq144Mnh98JcGjOuKkyNjWahqb3HYi54HA-l-Eee4nGcvDkTdx-u3L6-GBOoIpEZ8ebHN-a6IQur_mt0_1rDXtyKfdYFcdgdxicIww59hfEJa0pTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میلی گلد این فیلمو از طلاهاش منتشر کرد و گفت دزد نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/150455" target="_blank">📅 21:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پوتین: جهان از شجاعت و مقاومت ملت ایران شگفت‌زده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/150454" target="_blank">📅 21:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150453">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ: اگر ایران پشت آن حمله به هواپیما بوده باشد ضربه بسیار محکمی خواهد خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/150453" target="_blank">📅 20:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150452">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=iQ5SluAghWBLz8PLVlYPzh0QP_9YqMXIZhLRgClJ7-d8VBZVQxwr_sq4xEoD3R63L2s8a3Ry3YB1R4thtgQ4HO18Dh1jphIPoOuA3DZxk8Axwueblh2-LCyEE3n3Us_4-fkgD1JUlTb5Tb5zOa0XHMcI-pKK8tL-vxAnGAVl4pbf3YEB6OBhc2qviPzeKbkGJD0GnA1rpV1eMGWf5Ctyn0hH0sYFaNjJ_a1_tPFMLNWlHGG59q_Ec7OWjeAkkWXwBjeWkGzjCZIBYqGQTJwhi3kkWkilY3fS3C8oXorSEU85HUly8nyZVz8DG5jRNW0_Q0xvtjXGVYk-6vUABkXXaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=iQ5SluAghWBLz8PLVlYPzh0QP_9YqMXIZhLRgClJ7-d8VBZVQxwr_sq4xEoD3R63L2s8a3Ry3YB1R4thtgQ4HO18Dh1jphIPoOuA3DZxk8Axwueblh2-LCyEE3n3Us_4-fkgD1JUlTb5Tb5zOa0XHMcI-pKK8tL-vxAnGAVl4pbf3YEB6OBhc2qviPzeKbkGJD0GnA1rpV1eMGWf5Ctyn0hH0sYFaNjJ_a1_tPFMLNWlHGG59q_Ec7OWjeAkkWXwBjeWkGzjCZIBYqGQTJwhi3kkWkilY3fS3C8oXorSEU85HUly8nyZVz8DG5jRNW0_Q0xvtjXGVYk-6vUABkXXaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: وضعیت نیابت‌های ایران، مانند حزب‌الله، چگونه است؟
🔴
ترامپ: آن‌ها با ایران می‌روند، بنابراین نیابت‌ها نیز با آن می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/150452" target="_blank">📅 20:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150451">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ: من به دولت، اقتصاد و همه چیز نمره A+ می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/150451" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150450">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری/ترامپ:  اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/150450" target="_blank">📅 20:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150449">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: ما ذخایر راهبردی ملی خود را با نفت ونزوئلا پر خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/150449" target="_blank">📅 20:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e448c031e.mp4?token=q6QJvnVcepgYEC1KUUtkUorPMDmkZUcE9y3fEqyNbRZryTJ9_pnVJH7redohmopm8M-hzRBkE8DQil3ZFCJwM4D0Kcrr-DeLmpaWF4vD4eIX7HMTLo3x80hb9dumKY6sw235UMxvUqbsShHcNe-nBgFwOPuy198wEV-T0cxuiBcUslMONJ4O399XdjBROcEECEc7__aYQVtAIIfyceM2RDC78TCsNBJwayoFUaIe9zP_qrNQNQ_oWmhCrXLynJ3odpq-F1oqgB0E6APg8HJ86ar-yMNmW_4mYt5Eewt0ZHQkqbd0Pyriu4F10hlWLF58cxlgvAzFG-rK2oL7DKCyYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e448c031e.mp4?token=q6QJvnVcepgYEC1KUUtkUorPMDmkZUcE9y3fEqyNbRZryTJ9_pnVJH7redohmopm8M-hzRBkE8DQil3ZFCJwM4D0Kcrr-DeLmpaWF4vD4eIX7HMTLo3x80hb9dumKY6sw235UMxvUqbsShHcNe-nBgFwOPuy198wEV-T0cxuiBcUslMONJ4O399XdjBROcEECEc7__aYQVtAIIfyceM2RDC78TCsNBJwayoFUaIe9zP_qrNQNQ_oWmhCrXLynJ3odpq-F1oqgB0E6APg8HJ86ar-yMNmW_4mYt5Eewt0ZHQkqbd0Pyriu4F10hlWLF58cxlgvAzFG-rK2oL7DKCyYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/ترامپ:
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/150447" target="_blank">📅 20:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150446">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
ام بی سی: مذاکرات به یک باره مثبت شده است
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150446" target="_blank">📅 20:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150445">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: مقدار نفت عبوری از تنگه هرمز در حال حاضر بیشتر از قبل از جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150445" target="_blank">📅 20:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فووووری/ترامپ: ایران پذیرفته است که سلاح هسته ای نداشته باشد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/150444" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/150443" target="_blank">📅 20:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150442">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/150442" target="_blank">📅 20:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150441">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea51d61a8.mp4?token=EaNvfyO8Y7zC_Hg63YyX3UjWjUbxfearEiOh74GgHCr1zNh39eB88_q1U0wsXKItXioBK96s8IdAzhXiW92UaGx03jeABwF-nXCRddWeycI9GzBa0qCImZWBqs9Qniu29ep_3XlaMHPPP9fM_32onbcYKHNGw2ISw85kytzkPFOi4bltKViF_Y3LOOX5y8aGl3foX7LYbiUSogIlDCjzj5PdnQJGi081WrNOnSdRyFrKYEfvZmCV5oYbkhb_3utsQeflk86xZnS7qxFgSCMG0ocUL7czre5MvewxJPVdQocdALhLxmEvWSbgvEmvbJDPxcI6ewKp1-NWTE6XjYkQsWYSyf0qAMidB9xb8DRWOoTEkg7E0UvRRsIrxc7G-wYPj4GM68BF3XIp-MOek5J_31M8j7Zf_AOG8teLo9KFt1YoloWYL2v8UpettKHbJBmpxMZ0_JSUzGcsz7GATv9TFq1ZmsdGpzM6wOxop2ec7abclT7LUnHxIAjU91tO51fXaXFHy0g39fmvukqMkGpDROzeYUTdWpGU4XGRDq2CaZs6rroz06afyxYuKRY25-AaWrbWBIDbC01qSwRrc-MEGlXHbRFjwyOwmh6dvHSqxN3JxtIvBPkgt5qfB2c4QQOl6v8sFoInlO5k95lE6PO9CiWWTWOzzxeor566rwe9wUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea51d61a8.mp4?token=EaNvfyO8Y7zC_Hg63YyX3UjWjUbxfearEiOh74GgHCr1zNh39eB88_q1U0wsXKItXioBK96s8IdAzhXiW92UaGx03jeABwF-nXCRddWeycI9GzBa0qCImZWBqs9Qniu29ep_3XlaMHPPP9fM_32onbcYKHNGw2ISw85kytzkPFOi4bltKViF_Y3LOOX5y8aGl3foX7LYbiUSogIlDCjzj5PdnQJGi081WrNOnSdRyFrKYEfvZmCV5oYbkhb_3utsQeflk86xZnS7qxFgSCMG0ocUL7czre5MvewxJPVdQocdALhLxmEvWSbgvEmvbJDPxcI6ewKp1-NWTE6XjYkQsWYSyf0qAMidB9xb8DRWOoTEkg7E0UvRRsIrxc7G-wYPj4GM68BF3XIp-MOek5J_31M8j7Zf_AOG8teLo9KFt1YoloWYL2v8UpettKHbJBmpxMZ0_JSUzGcsz7GATv9TFq1ZmsdGpzM6wOxop2ec7abclT7LUnHxIAjU91tO51fXaXFHy0g39fmvukqMkGpDROzeYUTdWpGU4XGRDq2CaZs6rroz06afyxYuKRY25-AaWrbWBIDbC01qSwRrc-MEGlXHbRFjwyOwmh6dvHSqxN3JxtIvBPkgt5qfB2c4QQOl6v8sFoInlO5k95lE6PO9CiWWTWOzzxeor566rwe9wUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین
رهبری شوروی سابق را به ساده‌لوحی، خودرأیی و اعتماد کورکورانه به غرب متهم می‌کند و می‌گوید که این عوامل به فروپاشی اتحاد جماهیر شوروی منجر شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150441" target="_blank">📅 20:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150440">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87899a96b.mp4?token=U99QAs7-hMapaHycWIT5eJnpRCwbX2q2xYN1M-qN0nA4x9h3POhZeNyAml_oiswwRf3IKjDHRw3wOZpWy0M9E_dHBdC3VYBrnQD69ZemMkilQl52dbAGmER1mkIaxH_r2LeNpCYm-kyAr_RvD1OOzIaSiEOw3D_kyXQ5A6JXcX4f6r4ncV8H35QZ0FnVO7yJk_YK5QOrbm9XKoj2tDCh7LHgfFsrkAw3JeXEXfmU5XWxw5tI0bpaILCaC7-6MO0BoAIe6i40PD93ymE9z4NxDaaietjYHpT3nbpK6jcQCIVaW03KjJ-xbcv0F33sqNbNsX5iXptPa_q_fHuD4Fq0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87899a96b.mp4?token=U99QAs7-hMapaHycWIT5eJnpRCwbX2q2xYN1M-qN0nA4x9h3POhZeNyAml_oiswwRf3IKjDHRw3wOZpWy0M9E_dHBdC3VYBrnQD69ZemMkilQl52dbAGmER1mkIaxH_r2LeNpCYm-kyAr_RvD1OOzIaSiEOw3D_kyXQ5A6JXcX4f6r4ncV8H35QZ0FnVO7yJk_YK5QOrbm9XKoj2tDCh7LHgfFsrkAw3JeXEXfmU5XWxw5tI0bpaILCaC7-6MO0BoAIe6i40PD93ymE9z4NxDaaietjYHpT3nbpK6jcQCIVaW03KjJ-xbcv0F33sqNbNsX5iXptPa_q_fHuD4Fq0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بیژن مرتضوی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/150440" target="_blank">📅 20:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150439">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul51jlZwxvpr98lJvRH2j7XriQd2kEct-HCEHubPCBFvxwG9pg69jckz1tMatoTzUGVml8yzpFPp9W17_gYLdyk0mGBGg8ut5wg95elAL6sfsFk_9DiXFGhJvHzGjQ7AJGKvQpfaQWwSIWcsHptdSUyDDt5WyLwRzq1Bmp_hv2Gct_cobnmhTE9hsXXpp8TV_Ev1yXjVE0sB5SEQg4zqnXmKXXJDkTgM-9XSdKAV3CJR0TpyGQfRtQ81a1EniLGUKPWuxXfBlbmke6uEBR98fU9iwvzIAQZ05L5iD0JfCCzFAVqMJDz1al9ipUfy69fY4S9Rprokv5f2zMDFODttPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر اسرائیل بنیامین
نتانیاهو می‌گوید کودکان غزه از شیر مادران خود کینه می‌مکند
نتانیاهو گفت که کینه‌ی یهودیان از دوران نوزادی در غزه درونی می‌شود، در حالی که او اسرائیل را در جنگی علیه گولیات «بنیادگرایی اسلامی جهانی» به عنوان دیوید ترسیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/150439" target="_blank">📅 19:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150438">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
پوتین:
در صورت حمله مستقیم به روسیه یا کالینینگراد، استفاده فوری از تمام سلاح‌ها مطرح می‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/150438" target="_blank">📅 19:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150437">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAnmXKj2i3PIXYQigQaeinOYvEvlWVdGKXJR5aAdYU1RhfSS_QeW8TReUo8bxD1MCI4LDsLD3_535d8fAuTo_C1nUYT9QwiwueujgIPaI2wlmfSEIyt29HBhx_uhKyhuAIiWtfthqh6V02MzAy_w0k8x_wKkdUDN4IQ5el0-wYfL_2ttc7P2Qra3TNjrwohcWszI9H1LpPNpzjAOI8ePX_t3n09fGbTGAgKDz4Uvwwohj1Y9DFaEB_NsaUjaC8XN55FlYbNDn9EibD9URIJQd9CvVy2j_Fr-AqoVmhEUOZacKK1vuMNDgInCZzqpCVQ7aksraLq2DJ3Qz04REt65Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سوخت‌رسان آمریکایی در آسمان امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/150437" target="_blank">📅 19:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150436">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34eeb2e93.mp4?token=Jt8X0VvdYMaAg6Ise_mzwQkBSZoS4aGJLAXOEAWOu9RSAlgC_jWDqCF45xcg2VjOeG60Sf8JRS9Ir1C7wSO8zYGbFzuDumeNF6LlQGlGWCYkluHZIiEB5-jO2N-nuSUFd8GbCqBklzY7e07BqHukkJvqyAU6obdfHMAQ59etLn_X5c3A781OZve2eRm7Uc4p-l7ltHzPMYTHShwB8y1t5SNueVxvU5CgJVNmJK9MExQWRDU-Md1BFliZl7ZiOGFzJQG-AHW1FU6jH1WzTEYjMyBGV3dcGaN-SH9fUwiPO_kfZZa2kGHV_BMxYnkAcQNE55vJhagk-wdrDY4Wi7yscw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34eeb2e93.mp4?token=Jt8X0VvdYMaAg6Ise_mzwQkBSZoS4aGJLAXOEAWOu9RSAlgC_jWDqCF45xcg2VjOeG60Sf8JRS9Ir1C7wSO8zYGbFzuDumeNF6LlQGlGWCYkluHZIiEB5-jO2N-nuSUFd8GbCqBklzY7e07BqHukkJvqyAU6obdfHMAQ59etLn_X5c3A781OZve2eRm7Uc4p-l7ltHzPMYTHShwB8y1t5SNueVxvU5CgJVNmJK9MExQWRDU-Md1BFliZl7ZiOGFzJQG-AHW1FU6jH1WzTEYjMyBGV3dcGaN-SH9fUwiPO_kfZZa2kGHV_BMxYnkAcQNE55vJhagk-wdrDY4Wi7yscw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش یک بلاگر به صحبت سخنگوی دولت درباره کالابرگ و پفک
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150436" target="_blank">📅 19:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150435">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtT5nkTS63WTi0HvbPeVN_puH0WExJjpHiIJsxyPo2VZIU5dXYsQzwvCZlA4BWnTrya9bFH-MUNQ67SRRadBdmOgO_KS6ffy7KzXreMiA8o2tP65RQ0A0ACrH4vqnrCvfZVOaJF3Siz8U7Ja0wdiUPenVqE6qhuz90JfuVeP6AShd_0Q3iGLyi-ZEdC5k9XzK3BoAyfv39VbSEfEWgn9OdEAWxHs27hhBLJJLr0iTDcwY_H1c3YTUZa7h43HLVneGY3yPQZuhky1ldq4aMdIzKIybizDPLnoQrwvJrNVy6GkfPLFJy8mf2LA3wohC4rayD-qIPhFzgOXiG5V6tBEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت با ۳.۷ درصد افزایش از ۱۰۱ دلار عبور کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/150435" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150434">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
۱۲ فروند اف-۳۵ از انگلیس به آمریکا برمی‌گردن
🔴
حداکثر ۱۲ فروند اف-۳۵ از پایگاه لیکین‌هیت انگلیس به آمریکا برمی‌گردن. برای این انتقال چند هواپیمای سوخت‌رسان هم ثبت شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/150434" target="_blank">📅 19:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150432">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
بلومبرگ:
ایران سپتامبر هیچ محموله نفتی بارگیری نکرد
🔴
بلومبرگ نوشته که ایران تو ماه سپتامبر حتی یه محموله نفت خام رو روی نفتکش‌ها بار نکرده. این یعنی محاصره دریایی آمریکا دسترسی ایران به بازارهای انرژی رو خیلی محدود کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150432" target="_blank">📅 19:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150431">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noiOdxsTKzmtTUoBW8U0T1kkNUpzfUco5VbAtr5KFYQQ81uuevcv04_tWyEFkqF4RMmwzeo148KJ0dAkzV_nFYzF07hvr0whsVQ7yiLNqoCuSDQBU45MrtnyHU5TXbULRNm2m0sGizWUh6WDBcl-zsbfTHaiilKyxTIoNW00JXsWB-O5ACoW6OdeD54aLF59SEpB4UZ4IjmCekjrHMvyVlnBIAvQlccmdGzkEcgFMw1FLj2qznl527wgMPaKMCajr7klAepBnEd_W6gOjD9ivBSN4gWHbqS3p-ritWEA8U6BQ8vB4HBcj0ShTXhfyhwB8b3MrE-oppXBWzA3a0e6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طالبان: تحریم هوایی ایران رو قبول نداریم
🔴
طالبان اعلام کرده تحریم هوایی ایران رو قبول نمی‌کنه. این گروه گفته چنین محدودیتی رو به رسمیت نمی‌شناسه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/150431" target="_blank">📅 18:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150430">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c00080542.mp4?token=UnddqB5n6LFNzkuWPVVaHlvNzQ17PjQFl23J6euP21vVfQmSIgAG-JhgW_jfM-cMkgCNBYxRzpH_bduOFQ0TZQI_WnuSZU5SEHYLWcBLSFO59E3UzJscOkTvUKtTuIB8nP5k-rs0ftBHurSlQnjzu6kt_lLKOIbyxASqiVJBgem38NUW0LCsZb2npG7gmJPQK712pKOCDuagY1IJZs0DNthYFQsR79D8xeXLC0x0tGxnDNcOGjV7kM8swiZ7zqgBGzTrVDy6ba1dnCj5_Q7ENK2YAtSvbIytFhg5xt2nzBOJcmf4afy_uAqN6FgflM5DFper1Yby9HiXUFAxExg4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c00080542.mp4?token=UnddqB5n6LFNzkuWPVVaHlvNzQ17PjQFl23J6euP21vVfQmSIgAG-JhgW_jfM-cMkgCNBYxRzpH_bduOFQ0TZQI_WnuSZU5SEHYLWcBLSFO59E3UzJscOkTvUKtTuIB8nP5k-rs0ftBHurSlQnjzu6kt_lLKOIbyxASqiVJBgem38NUW0LCsZb2npG7gmJPQK712pKOCDuagY1IJZs0DNthYFQsR79D8xeXLC0x0tGxnDNcOGjV7kM8swiZ7zqgBGzTrVDy6ba1dnCj5_Q7ENK2YAtSvbIytFhg5xt2nzBOJcmf4afy_uAqN6FgflM5DFper1Yby9HiXUFAxExg4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پور علی: دو شب پیش رهبری نیم ساعت در تجمع شبانه حضور داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/150430" target="_blank">📅 18:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150429">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354527fcb7.mp4?token=JxrxNf-o6_L6YBrjy0Wnf2w4UZH-EO-72FX62NAKPYIjLIJ_EDrlkJV60SnDFSQB5pFg5Hlz1k2B25FEawzoqE9jzGi7IN_p51iTok14LlTlTHOY0cXfHwFHZ7ZcW6FIihpl79ybw7Yt7hQq8d_4YdVJaagtLEkOeK7-5sFEFG_S8a7WFYMi_9ps18SgnYFkrQYMuDUf4ly_xaI7tEUOdeCCeCEkXO312YBM9t7qfrsJevpefWl9S2ZfNR4Q3EUroxmo2f4I19SreYnIgTdv80ncuxqEQm35ZZO_Gvpn3jDtn3PFrpBZIVyDkr7q0Oi9LOLTyTNA7epuG4ubTrpEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354527fcb7.mp4?token=JxrxNf-o6_L6YBrjy0Wnf2w4UZH-EO-72FX62NAKPYIjLIJ_EDrlkJV60SnDFSQB5pFg5Hlz1k2B25FEawzoqE9jzGi7IN_p51iTok14LlTlTHOY0cXfHwFHZ7ZcW6FIihpl79ybw7Yt7hQq8d_4YdVJaagtLEkOeK7-5sFEFG_S8a7WFYMi_9ps18SgnYFkrQYMuDUf4ly_xaI7tEUOdeCCeCEkXO312YBM9t7qfrsJevpefWl9S2ZfNR4Q3EUroxmo2f4I19SreYnIgTdv80ncuxqEQm35ZZO_Gvpn3jDtn3PFrpBZIVyDkr7q0Oi9LOLTyTNA7epuG4ubTrpEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 260 هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/150429" target="_blank">📅 18:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150428">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFofbmr6S3sF4r8fgSsOHFbKfmaNSshQRn56bRV5S1frWsShsMdWctLDmJR3jvP7e2BOKGytXMFiPLI37CWMqX0THHmrnJicmvDPoqHr7gQCKqjPt_FRrUa-z-b2Bo_md_n9Mjq-xDKH6CcmEZv3ezdfm_dclwEh9E4b8cO-SW5N2LxzKeSTaNAC6UUEyGtxplN-RzNwIEORKDqUaJ7E9TpJthnUh6zTKjxicbRbwCQ9mu9VMwlopVCwH5E4WNdVFJ6s3kjinIbP7lywKwqJBgfsG-RTMgs3R_ADYml5xGFznMZVds2t0PjmHqkTplO6CpJe9ylcfdzvTspPHh1g4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):
ارتش اسرائیل دو تروریست را که در جریان کشتار ۷ اکتبر وارد خاک اسرائیل شده بودند، به هلاکت رساند: یکی از این تروریست‌ها در جریان کشتار ۷ اکتبر وارد کیبوتص بئری شد و در ربودن شارون هرتسمن-آویگدوری، نوعام آویگدوری، عدی شوهم، نِوِه شوهم، یَهَل شوهم و شوشان هاران مشارکت داشت
ارتش اسرائیل اوایل این هفته (سه‌شنبه) در منطقه شهر غزه حمله کرد و محمد جمال محمود ابوالشاعر، فرمانده یک تیم در شاخه نظامی سازمان تروریستی حماس، را به هلاکت رساند.
این تروریست در جریان کشتار ۷ اکتبر وارد کیبوتص بئری شد و در ربودن شارون هرتسمن-آویگدوری، نوعام آویگدوری، عدی شوهم، نِوِه شوهم، یَهَل شوهم و شوشان هاران و انتقال آن‌ها به نوار غزه مشارکت داشت.
در حمله‌ای دیگر در این هفته (سه‌شنبه) در منطقه جبالیا، ارتش اسرائیل مصعب عبدالغلیل ثاقب بلابیسی، فرمانده در شاخه نظامی سازمان تروریستی جهاد اسلامی فلسطین، را به هلاکت رساند.
این تروریست در جریان کشتار ۷ اکتبر وارد خاک اسرائیل شد.
اخیرا، این تروریست‌ها در حالی که به‌طور سیستماتیک آتش‌بس را نقض می‌کردند، طرح‌های تروریستی علیه نیروهای ارتش اسرائیل و شهروندان اسرائیل پیش می بردند. این تروریست‌ها از هوا و با هدف رفع تهدیدی که ایجاد می‌کردند، به هلاکت رسیدند.
پیش از انجام حملات، اقداماتی برای کاهش آسیب به غیرنظامیان، از جمله استفاده از مهمات دقیق و رصد هوایی انجام شد.
نیروهای ارتش اسرائیل تحت فرماندهی جنوب، مطابق با توافق در منطقه مستقر هستند و به فعالیت برای رفع هرگونه تهدید فوری ادامه خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/150428" target="_blank">📅 18:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150427">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmASi5t4JyWJKuEUD4dyLIWRWDHhiGwCvdLFosc9AV2-coTHzoftd63U7dUrpPJjYQPZYMtE3AHS4xiORU78bCaH7L5ZS1NcF11aJxirLwtX3YMROcpLDCe-8_dykCp7sjnYcMHh8iNKyYkSVwSMVSQQpZvwVG64RXvacHtYhyT1DMjYj7dUINVykez2G1Wu4DVVTrQeq9unYVtO7Oz4pjtPZhEEFl7uKK7x5AOSq3lLGBM0SQzqVwFYuADegrutOwFZ6Kapv6CV5fQFP3BSyCMrYNKSOpQCh0-JeZXYreunLvHfgzJQ4KlXkLVCrCY-QDIRo9GfPbYHG9mqFoNbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن عبدالکریمی: وضع مردم خوبه و کباب بازی میکنن و هر روز هم کلی خرید میکنن، هرکی میگه اینجور نیست دروغ میگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/150427" target="_blank">📅 18:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150426">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2519fac2.mp4?token=sDYaggRt_8eUiB_AkMn-7KPDymZ-HZxF76z9el45f1p75JzgnNg48OL5C-i6XxJj3RdgPJNFoOCFYX_OiECJgdQ5pY5dh2HZOhL_iNjxYgCEGE8Pc64cxZIM4ifxUGoFWrbQcQaGZfuHN0Dg-sTPVUPWReFWL5KFDxa47qlMblHJc-8Y_8G3o8pmmcociCsxdKkGtiw59N2jklgAIfkCtgh-CU2bpkw7t87yN_GJoTt5JWsIYCO9nKQxJyI-2H3lymwDo7vqqzNjhU29bevCwGL6GJJnbjbpo0BuuZB38EUKCOyAEXTGTOuAA4LNsRxmH0eKv1JbkA7A5goBJFQlDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2519fac2.mp4?token=sDYaggRt_8eUiB_AkMn-7KPDymZ-HZxF76z9el45f1p75JzgnNg48OL5C-i6XxJj3RdgPJNFoOCFYX_OiECJgdQ5pY5dh2HZOhL_iNjxYgCEGE8Pc64cxZIM4ifxUGoFWrbQcQaGZfuHN0Dg-sTPVUPWReFWL5KFDxa47qlMblHJc-8Y_8G3o8pmmcociCsxdKkGtiw59N2jklgAIfkCtgh-CU2bpkw7t87yN_GJoTt5JWsIYCO9nKQxJyI-2H3lymwDo7vqqzNjhU29bevCwGL6GJJnbjbpo0BuuZB38EUKCOyAEXTGTOuAA4LNsRxmH0eKv1JbkA7A5goBJFQlDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیرحسین شریعتمداری، فرزند محمد شریعتمداری، وزیر اسبق بازرگانی و مدیر فعلی ابرهلدینگ خلیج فارس، خواننده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/150426" target="_blank">📅 17:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150425">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پزشکیان :
هیچ‌گاه از گفتگو فرار نکرده‌ایم و نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/150425" target="_blank">📅 17:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150424">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7chVT2AmdEp-dmAPNe1W04eZlpl8o3Oy8VkS2S41UQD2SK-rfRP6TaRRM4kqCdjuV4olxcJrJLP4dsg3OGPAijGbWKXdU31y6ZgYf5QqzjWg-aZl-1u0SvXutvjgz8-zoP7-kxp5J5N75i-C5CHN0hwCs6SaHhjU3lacSpbCqtLB_waoea91qSNk91vP6V6Eza24eIzB3eqtw8d1nA2qT5qVTZzUFBXgiiqWiFpbcDb7H-xoqTjksyffM1WsiL06BsIo_A1dwRoSOh4mRHsgVvFLjUpJk41igFsXr-TilLGPd0qFFPhrDKP1xGtmd2YNETqYu8R5p86pzp4cy9tpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا قراره بیژن مرتضوی تو یکی از تجمعات شبانه ویالون بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150424" target="_blank">📅 17:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150423">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzbFH-fcnOCr_PBgixI-q00q_AKuy1DbCfI13y6wBurhLBecyecfNCBKvzGWXWFZ9kVEW3VNgYwiZE0SU17IGNiZ1xrXMdK2BiWF38EIn-6KHdXVJaeAGkAWIYMTerIdJpMOaEvevOVxYz3PBiQWtb7Z5IYOFBNdBugEPGag-fIHP2AvwRSZL896mEEanEHSPYzvw-SnXCpbOi1JjmYOdI0qTxxXLzqztnucJWSdljd8jWHbxf8WNbHccg98ck8CTthwbPqkGekIdY2ZM4RoeWuOEiP2IyCwPjf7MN-t8fz09OQpAnCBcLdRg9z2txzuJp7T33S5hkt_xEPwvHe07A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر خروج آخرین نظامی و جنگنده ارتش آمریکا از عراق
🔴
شبکه فاکس نیوز همزمان با تکمیل عقب‌نشینی نظامیان و تسلیحات و جنگ افزارهای ارتش آمریکا از عراق و پایان ماموریت موسوم به عزم راسخ، تصویر خروج آخرین نظامی و جنگنده آمریکایی را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/150423" target="_blank">📅 17:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150422">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رسانه های عبری: امارات تحقیقات درباره حادثه پرواز «فلای‌ دبی» را آغاز کرده
🔴
کمک‌ خلبان عمانی که مظنون به تلاش برای سرنگون کردن این هواپیما است، برای بازجویی به امارات منتقل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/150422" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150421">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43b4c69e6e.mp4?token=hh9Q7GSrtIIgg7Ikn5W9PrYek22G4iDCyuCWtz1RtH0G49-m-Dbx72OqjISg5c3DAoukOUExk2Cs16Cfkj7sR5ZKRMK-9QxLxHdUbqbKUrRftu7UASQR_WQcEtAAfW5_gbbc_VpEB-iOsD3aIfEu20k8uDY1Gdda6iVEy08O1EkQ66mcYBmAyZSxrXHDpSqXA2ZvtmQZ-XYfTsLFOEvQQEm71dyOhTmseZisv9mnBmuxerDbLdIcrW8m2p3TCWcffTUrA0gQZJHRdzpIBynKy5S0-1hdcAQipsiJoRkEe2TsMcMfY5zrr1sfs_fpZyim0wRyxFHvGYflHfshsMqyuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43b4c69e6e.mp4?token=hh9Q7GSrtIIgg7Ikn5W9PrYek22G4iDCyuCWtz1RtH0G49-m-Dbx72OqjISg5c3DAoukOUExk2Cs16Cfkj7sR5ZKRMK-9QxLxHdUbqbKUrRftu7UASQR_WQcEtAAfW5_gbbc_VpEB-iOsD3aIfEu20k8uDY1Gdda6iVEy08O1EkQ66mcYBmAyZSxrXHDpSqXA2ZvtmQZ-XYfTsLFOEvQQEm71dyOhTmseZisv9mnBmuxerDbLdIcrW8m2p3TCWcffTUrA0gQZJHRdzpIBynKy5S0-1hdcAQipsiJoRkEe2TsMcMfY5zrr1sfs_fpZyim0wRyxFHvGYflHfshsMqyuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل درباره عمان: سلطان قابوس فقید، رهبر عمان، چند سال پیش از من دعوت کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/150421" target="_blank">📅 16:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150420">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پزشکیان: عده‌ای کنار گود نشسته‌اند و می‌گویند لنگش کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/150420" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150419">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
دونالد ترامپ در مصاحبه‌ای با مجله تایم:
هزینه‌های مربوط به جنگ ایران برای ما کمتر از درآمدی است که از نفت ونزوئلا در یک ماه به دست می‌آوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/150419" target="_blank">📅 16:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150418">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: تحریم‌های اعمال‌شده علیه ایران یکجانبه هستند و از سوی شورای امنیت صادر نشده‌اند؛ بنابراین به تجارت خود با تهران ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/150418" target="_blank">📅 16:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150417">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پرزیدنت ترامپ به مجله تایم: اگر به سوئیس می‌گفتم: «متأسفم، نمی‌خواهم سالانه ۴۰ میلیارد دلار ضرر کنم تا ساعت‌های شما را داشته باشم»، ما همین حالا ۴۰ میلیارد دلار کسب کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/150417" target="_blank">📅 16:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150416">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نتانیاهو: ما می‌دانیم که خلبان مهاجم، تحت "فرآیند آموزش و تلقین افراطی اسلامی" قرار گرفته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/150416" target="_blank">📅 16:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150415">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نتانیاهو: اگر سلطان قابوس زنده بود، عمان به توافق ابراهیم می‌پیوست
🔴
بنیامین نتانیاهو درباره عمان گفت: «سلطان قابوس فقید چند سال پیش من را دعوت کرد.»
🔴
او افزود: «مطمئنم اگر سلطان قابوس زنده بود، یک شریک دیگر در توافق‌های ابراهیم داشتیم.»
🔴
نتانیاهو درباره حکومت کنونی عمان نیز گفت: «حکومت جدید موضعی سرد و فاصله‌دار دارد، بنابراین هنوز نمی‌توانم چیزی درباره آن‌ها بگویم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/150415" target="_blank">📅 16:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150414">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پزشکیان :  هیچ‌گاه از گفتگو فرار نکرده‌ایم و نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/150414" target="_blank">📅 16:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150413">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ به مجله تایم گفت: من آی‌کیو بسیار بالایی دارم. بالاترین هوش را دارم. من خوبم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/150413" target="_blank">📅 16:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150412">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra3KgYsKtY7cM1ALm_BUWMRpmAur9vESY8ocu5BYaUYXwe2Qoqye6lukFLzMt7_va9uC0lKQ8HJOfgUb_bjJVZKTwnaADpugnC1BmRG_Jl_4DPEEA5JmYmdx-lkinYwQHWN-yMqLvzsheSkx_aJV5B9aTYdiQbxnQphknTY7gA0zF0J6gFmAWtaq3SUlL015HJBKgxeMSWsAL-CP5lgebG7ORtICY0lwaHeB4tuGY3QCz9njCIqiVQAElhgKPAfXrwDR5DCTr7GDU-6FxSlrlg40vIa0ZW9klXBmCrlFyTn2Eo8l_Ap3mZXfqiaBYokHqj9oo1ZhU4sdN5BJrfajhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال‌ها بار دیگر به فرودگاه ریاض بازگشته است؛ 10 هواپیما در انتظار مجوز فرود هستند و در نزدیکی فرودگاه به‌صورت دایره‌ای پرواز می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/150412" target="_blank">📅 15:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150411">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دونالد ترامپ با روزنامه تایم: خبرنگار: آیا در نظر دارید که قبل از پایان دوره ریاست‌جمهوری خود، اعضای دولت خود را مورد عفو قرار دهید
🔴
دونالد ترامپ: بله، قطعا این کار را خواهم کرد؛ جو بایدن که به خواب علاقه زیادی دارد، برای همه عفو صادر کرد؛ من بالاترین ضریب هوشی را دارم. من بالاترین را بین همگی دارم و بسیار خوب هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/150411" target="_blank">📅 15:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150410">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ: تهدید بسته شدن هرمز را می‌دانستیم؛ ایران اکنون توان سابق را ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/150410" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150409">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ: پیشنهاد ایران برای باز کردن هرمز «تقریباً کافی» بود، اما نه کاملاً
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/150409" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150408">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: نظرسنجی‌ها جعلی‌اند؛ هر رقیبی را با اختلاف ۲۰ درصد شکست می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/150408" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150407">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: بایدن حجم عظیمی از مهمات آمریکا را در اختیار اوکراین قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/150407" target="_blank">📅 15:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150406">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: فکر نمی‌کنم نتانیاهو پیش از حمله ۷ اکتبر هشدار دریافت کرده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150406" target="_blank">📅 15:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150405">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ درباره زهران ممدانی: او را دوست دارم، اما سیاست‌هایش دیوانه‌وار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/150405" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150404">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ: اگر من رئیس‌جمهور نبودم، امروز عربستان و اسرائیلی وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/150404" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150403">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ درباره طولانی شدن جنگ با ایران: خودم خواستم جنگ را ادامه دهم
🔴
خبرنگار تایم از ترامپ پرسید: «ابتدا گفته بودید جنگ ایران حدود شش تا هشت هفته طول می‌کشد؛ اکنون وارد ماه هفتم شده‌ایم. چرا جنگ این‌قدر طولانی شده است؟»
🔴
ترامپ پاسخ داد: «فقط به این دلیل که می‌خواستم جلوتر بروم. آن‌ها را از میدان خارج کردم و همان زمان می‌توانستم جنگ را متوقف کنم، اما می‌خواستم ادامه دهم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/150403" target="_blank">📅 15:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150402">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ: دیشب بیشترین مقدار نفت را از طریق تنگه هرمز منتقل کردیم، بیش از هر زمان دیگری.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/150402" target="_blank">📅 15:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150401">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: دیشب بیشترین مقدار نفت را از طریق تنگه هرمز منتقل کردیم، بیش از هر زمان دیگری.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150401" target="_blank">📅 15:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150400">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: ما سلاح های زیادی داریم و وضعیت ما عالی است. ما اکنون مقادیر زیادی را ذخیره و نگهداری می کنیم و آنها را بین متحدان خود توزیع خواهیم کرد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/150400" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ عملا گفت که تا انتخابات میان دوره‌ای فرصت توافق هست
🔴
حدود ۳۰روز
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/150399" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150398">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ: با نابودی ایران، صلح را در جهان برقرار می‌کنیم
🔴
خبرنگار تایم از ترامپ پرسید: «هفته گذشته گفتید ممکن است ایران را نابود کنید. آیا همچنان چنین احتمالی وجود دارد؟» ترامپ پاسخ داد: «بله، این کار را می‌کنم؛ ممکن است.»
🔴
خبرنگار پرسید: «چطور رئیس‌جمهوری که خود را رئیس‌جمهور صلح می‌داند، از نابودی یک ملت سخن می‌گوید؟»
🔴
ترامپ پاسخ داد: «چون با نابود کردن ایران، صلح را در جهان ایجاد کرده‌ایم. فکر نمی‌کنم با وجود ایران هرگز بتوان صلح داشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/150398" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها پیشنهادی برای باز کردن تنگه هرمز ارائه کردند. من برخی از جنبه های آن را بررسی کردم، اما نه همه آن، اما به سادگی کافی نیست.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/150396" target="_blank">📅 15:02 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
