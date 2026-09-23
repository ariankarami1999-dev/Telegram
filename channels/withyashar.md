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
<img src="https://cdn4.telesco.pe/file/rtbdCo-gNqR4sOL2Pe9UoA8kpMqEMj7061mvch9EhJTsc_MKNd0OjDzYwtQgs9USShPYdq11DYvs09ui_JGUFqPhwnrSSUP1neE6vwmIKbiFyRoZGMmcnnLJuQCFTErEUMuwSSZ_7v6te4ciFbGM9vQtGAfd7XVYOK_TjG-S9_v6ZNqqzV7VvlRLV9o_hvdd3vNSNiC8StPeexkEB5WJHnDjDljRSfQseRfL4o9sgJVsrXxR3cryz65_RGvLNyiVmQ8fIaRR8BOAb6lhU1OpXxEjllyk15am-BQWXwjKdkhWaBbeTYSE5ribcgGJQQEDYEl2BFhhfwOaRnDP-Vtg6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 455K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGqiOOkW2_ci7gPgoavGwGgBFvrm2lcDU68c3QY9GEcByY82iwrt5Sq03zQz-_ZbiTEXRXx13F7AEzuktjFxHjKYvFM00VQM-sB-CK2GXA_okuHWWMLsFMpJv_67beA6u8O0j8tMSDeP7Q9YQR12kAS0jle94RHP4bNXMMdKgN8aKMQeITge7fUK9AqtB05kY7iKaor53fHrKcl3x3EqRCB4-kEsKYScUy7uIJUxGGYGPPNJac3jKBmSZe1cyw1aqLDwoanf1rEnYt_vUCXbREWULRwy2PCyXNyvj98OVLUvmflqE1yjHXI0E_6JXpLmrIdH_3YkUVHHB5lBFiiykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت یه کلاس درس تو سیستان و بلوچستان امروز
@WarRoom</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/withyashar/23888" target="_blank">📅 13:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پزشکیان فرا رسیدن روز ملی عربستان را تبریک گفت
@WarRoom</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/23887" target="_blank">📅 12:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23886">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کرملین:
«
ولادیمیر پوتین
آماده دیدار با
دونالد ترامپ
است، اما برگزاری یک
نشست بدون انجام هماهنگی و آماده‌سازی‌های قبلی
، اتلاف وقت خواهد بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/23886" target="_blank">📅 12:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آکسیوس: کمیته موسوم به «کمیته صلح ترامپ» از طرح بازسازی نوار غزه به ارزش ۲.۴۵ میلیارد دلار پرده برداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/23885" target="_blank">📅 12:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_se-nkbG3MgpzHci2NRe93pbAS2xYiNGGamBXViCNfy22pK77gLuoafBDZfiOdQMNh3zS5aVmDhpZt6waKWO6LYtK075RrlUwp2J-WEkaN3ti3KPmjJkYJyIpI6cUkN5sbCtzVPSURBUuh-Nrz_Rx9h31iFI98QZb7zuZH4y7jb9KBWdJYqrs5LsrOwyjhBjN7vVQaBkrEhi6r1F8AGqlAnbwxM-_NmjgVt9Kvp2SNprb9ONC1ElTnOR7laizuDz3RCxz3DOFGyHW1kS0eH6mPiatE8e9J2bipMRM54yprlY1CzuqtOkJC5Dq2uIXLRCLAUnCkHyGmAfHfQBJmFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : تحرکات زیاد شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/23884" target="_blank">📅 12:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOSs9LEL7dGzL1qxzpBD86kgZRCMvyLDrdtk2XsuDyKd3iCRGvaJVDA4CzqAOVIdD9_bxPU8kSfis5NkrhlNC_P_jQTmwbGPgrCrIyZLTF2Yo39ibi_j_c2jcA8PStJ_4uX5q-WLhL-m2j__mQafBDEvmvePQA-vZbDi0PMg_4fI-tn436Lays9a5OFqMwGxc6xoQ5hKeSY8hke7_nHBi_-KuL9qI8EbK8uy7MM15oi-RV1F8pSV1mTFRxceXkGAhJsnneI-DFuKwEfdol0MiOB7PcTdTTE6-lDACLjGVbjONEMYWPBEBusct6sxFXoVIH2VTn3TH3jDgccAc49YSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث خبر نیوزمکس: ائتلاف نتانیاهو در تازه‌ترین نظرسنجی انتخابات اسرائیل پیشتاز است.
@WarRoom</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/23883" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرگزاری فرانسه: یک هواپیمای مسافربری ایرانی با وجود تهدیدهای واشنگتن به اعمال تحریم، در چین فرود آمد.
@WarRoom
یجور میگه چین فرود اومد انگار شاخ به شاخ زده به ساختمان پنتاگن</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/23882" target="_blank">📅 12:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23881">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آخوند زنجانی ریقش در رفته  و امروز دولت عزای عمومی اعلام کرده
@WarRoom</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/23881" target="_blank">📅 12:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تنگه صدای فرماندهان پیشین قرارگاه خاتم میاد @WarRoom</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/23880" target="_blank">📅 11:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تنگه صدای فرماندهان پیشین قرارگاه خاتم میاد
@WarRoom</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/23879" target="_blank">📅 11:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23877">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نیروهای دولتی یمن: ما به سلاح‌ها و تجهیزات گروه حوثی در جبهه کهبوب حمله کردیم، که این امر منجر به تلفات در صفوف آن‌ها شد.
@WarRoom</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/23877" target="_blank">📅 11:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23876">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نشریه آمریکایی نیویورکر
فاش کرد که طی یک مکالمه محرمانه میان جرد کوشنر داماد ترامپ و محمد بن سلمان ولی‌عهد عربستان نقشه وی برای کنار زدن
محمد بن نایف، پسر عمویش، از ولایت‌عهدی در سال ۲۰۱۷
بررسی شد. در این گزارش به نقل از یک مسئول اطلاعاتی سابق در منطقه آمده است که کوشنر به بن سلمان ابلاغ کرده
همه در دولت آمریکا به جز سرویس‌های اطلاعاتی از وی حمایت می‌کنند.
این پیام به مثابه
چراغ سبز واشنگتن خطاب به بن سلمان برای اقدام علیه محمد بن نایف
تلقی می‌شد
@WarRoom</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/23876" target="_blank">📅 11:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش‌صدای انفجار در قشم @WarRoom</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/23875" target="_blank">📅 10:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دونالد ترامپ پس از پایان سفرش در نیویورک برای شرکت در مجمع عمومی سازمان ملل، بامداد امروز با «مارین وان» به کاخ سفید بازگشت. رویترز زمان فرود او در چمن جنوبی کاخ سفید را
ساعت ۸:۴۱ صبح به وقت تهران
ثبت کرده است.
طبق برنامه عمومی کاخ سفید، ساعت
۱۱:۰۰ صبح به وقت واشنگتن ساعت ۱۸:۳۰ به وقت تهران
یک
جلسه سیاست‌گذاری
در کاخ سفید دارد.
و طبق برنامه رسمی، شی امروز وارد آمریکا می‌شود و ترامپ در
پایگاه هوایی اندروز
از او و همسرش استقبال می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/23874" target="_blank">📅 10:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مستندی برگرفته از اسناد محرمانه ی ایالات متحده درباره ی رخدادهای شب بیست و ششم شهریور سال ۱۳۵۵.  به همراه مکالمات رادیویی واقعی از گفتگوی خلبان های نیروی هوایی ارتش ایران با برج مراقبت و مرکز فرماندهی.ماجرا از این قرار است که شبی آرام در اواخر شهریور ماه حوالی…</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/23873" target="_blank">📅 10:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8175c0276e.mp4?token=K9SDVe-pl5naCY-v2HBhBf7T7IhD6SiP3MquX5f4eZPNSgy7FlMdEQXPuEpu8sf5pdBciJAFBmXj0eri1bFrDOhJjjkJBr0HvYB9f81AAJRTzt_f3KOiZ2tubtqdOQOcRIiki5HUZURuuxLk5WKJP2xRfnDLU0GLEisHhD4fz2LbiRnol5IRFB6M2v4CoEzqx6kjH9QHHYDHrH7L4GzobJ-CEr9kveH0-MjhWDTFBCJ4q6eGITtgmB5JJ10Ze4F9b0_OIiUqyh2sQRbEqur3IdYAXKqrm55uUc8Yxn56qS17vlAxGD5nmI9mV1izYtxwI3IpztGeHtgPb3vIjUqWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8175c0276e.mp4?token=K9SDVe-pl5naCY-v2HBhBf7T7IhD6SiP3MquX5f4eZPNSgy7FlMdEQXPuEpu8sf5pdBciJAFBmXj0eri1bFrDOhJjjkJBr0HvYB9f81AAJRTzt_f3KOiZ2tubtqdOQOcRIiki5HUZURuuxLk5WKJP2xRfnDLU0GLEisHhD4fz2LbiRnol5IRFB6M2v4CoEzqx6kjH9QHHYDHrH7L4GzobJ-CEr9kveH0-MjhWDTFBCJ4q6eGITtgmB5JJ10Ze4F9b0_OIiUqyh2sQRbEqur3IdYAXKqrm55uUc8Yxn56qS17vlAxGD5nmI9mV1izYtxwI3IpztGeHtgPb3vIjUqWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : همین الان (ساعت: ۰۹:۲۷) شیراز، تحرکات سنگین نظامی
یاشار : هواپیمای هرکولس سی ۱۳۰ جمهوری اسلامی که در زمان جنگ در پاکستان مخفی شده بود با چنگال تیز دیدبان اتاق جنگ شکار شد
@WarRoom</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/23872" target="_blank">📅 10:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شاهزاده رضا پهلوی : مردم ⁧ ایران ⁩ را با منابع مالی بلوکه شده مسلح کنید . (ویدیو کامل مصاحبه حدود ۱۱ دقیقه) @WarRoom</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/23871" target="_blank">📅 09:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شاهزاده رضا پهلوی : مردم ⁧ ایران ⁩ را با منابع مالی بلوکه شده مسلح کنید .
(ویدیو کامل مصاحبه حدود ۱۱ دقیقه)
@WarRoom</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/23870" target="_blank">📅 09:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23869">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef7b629ee.mp4?token=NNfQXxWjhrhqXT1u3H7TfuAmeRNERPUUTMKgqL9Y-V4BeLXHvjzK9rGalcyl08S3ZZkVATJr9d8VC23UR0ybDiQzSUfp1Ss3Y4YK9iTxwMXvbWcUg8Ved9E5xOUyIXWuYMFagT7QvjOo8hFtYj8aSLEhcZOhmmvbrk4XmjmhQ130Av-Mv3iK9rdEIG3rJUpSf49UuzztwlxjofnZqkqDsFTyLW01cxguFevk42lt_vI5udUNI2hjuzEffIDRwXvIMPlIvaXzNhT2VkKYIr1zzRJXui1bwFtuY074LtpC37apDTItqD43SCGpz_vw6HwWxy1hivy9d5UhqJ9YcI6cOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef7b629ee.mp4?token=NNfQXxWjhrhqXT1u3H7TfuAmeRNERPUUTMKgqL9Y-V4BeLXHvjzK9rGalcyl08S3ZZkVATJr9d8VC23UR0ybDiQzSUfp1Ss3Y4YK9iTxwMXvbWcUg8Ved9E5xOUyIXWuYMFagT7QvjOo8hFtYj8aSLEhcZOhmmvbrk4XmjmhQ130Av-Mv3iK9rdEIG3rJUpSf49UuzztwlxjofnZqkqDsFTyLW01cxguFevk42lt_vI5udUNI2hjuzEffIDRwXvIMPlIvaXzNhT2VkKYIr1zzRJXui1bwFtuY074LtpC37apDTItqD43SCGpz_vw6HwWxy1hivy9d5UhqJ9YcI6cOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون، رئیس‌جمهور فرانسه، درباره ایران:
«این درست است که ما در این جنگ حضور نداشتیم؛ نه به این دلیل که با آمریکا همراه نیستیم. ما برای آمریکا احترام قائلیم و فکر می‌کنم متحدان خوبی هستیم. اما وقتی می‌خواهید وارد درگیری شوید، باید با متحدان خود درباره راهبرد هماهنگ کنید و پیش از آغاز جنگ از آنها نظر بخواهید. ما تصمیم گرفتیم به این جنگ نپیوندیم، چون معتقد بودیم ــ و من همچنان معتقدم ــ این گزینه درستی نبود.»
«فکر می‌کنم پس از آغاز جنگ در اواخر فوریه، اهمیت تنگه هرمز احتمالاً دست‌کم گرفته شد و امروز باید این مسئله را حل کنیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/23869" target="_blank">📅 09:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de2b4f18b.mp4?token=jZTsvz5oeQLxQBKpTt8L389jlyspvIldxDR_eHe2s7DmiND6DStGNh3xx1IsuDU6XCf7yfpQ2VFOsrOBstNeY6JN_BlIujcyBeC5-UilDriZuDh449jYNJUiEdqLPmePoE3YvW-1mp_webrjtiBW6HYQeOtZxTMOT0V3ugEb68tlDVab7VP_ALGuJ8SyII-Gl1oIm4_rsnbvv48xSFUXxFmL3tyQ58pYVKxwqbbcY5K9TVYEJQDuyqw9p0f8DSFr_OvfvLd_In3jKHfvIGs0ea5nDUGCP1lKvkSomKzSq60dGOkxHzqvYHzO01D5666oZ_Qc3guTgKknwHKRbE7gkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de2b4f18b.mp4?token=jZTsvz5oeQLxQBKpTt8L389jlyspvIldxDR_eHe2s7DmiND6DStGNh3xx1IsuDU6XCf7yfpQ2VFOsrOBstNeY6JN_BlIujcyBeC5-UilDriZuDh449jYNJUiEdqLPmePoE3YvW-1mp_webrjtiBW6HYQeOtZxTMOT0V3ugEb68tlDVab7VP_ALGuJ8SyII-Gl1oIm4_rsnbvv48xSFUXxFmL3tyQ58pYVKxwqbbcY5K9TVYEJQDuyqw9p0f8DSFr_OvfvLd_In3jKHfvIGs0ea5nDUGCP1lKvkSomKzSq60dGOkxHzqvYHzO01D5666oZ_Qc3guTgKknwHKRbE7gkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون، رئیس‌جمهور فرانسه، درباره ایران:
«اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، برای همه ما بسیار مهم است. بنابراین، برای من این هدف اصلی است. تغییر یک حکومت از طریق بمباران یک کشور، چیزی نیست که آن را عملی بدانم و از نظر من گزینه خوبی هم نیست، چون نتیجه نمی‌دهد و ما در دهه‌های گذشته چندین بار این اشتباه را تکرار کرده‌ایم.»
@WarRoom</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/23868" target="_blank">📅 09:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392110b2f5.mp4?token=rFT8x3lhmiME-5vfNYpuEnqyZaWj0qGyuG_gMIGVjeOP0GsIqOVA30OxQ9DsE6_S8vfVG29bw5t9u9Hd2z9vVcehUt9ytD8J5Kw3YN3qvm58ELLVrnpZOhVKwkQWaN8wa9W3r0Uhqvi9sl8QJcc_pX14XAFRnWsq2LqD4E0ukr2YqHsb36qcESeHH-3z9Rzk2MoRh3DIs9c4ZySpcpDhpREpKxD6vPM7MvzfaNpBRJukt7GjMyYPZjXdMhOdZU5RtGbaOH1E0tFfDi2ql96vt4XEwYCwJ2Mi2a2gxOlla5jOTKqAO6w3BENHza0Kwe0MwvZfFK5Tpb3uWbisMcqnDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392110b2f5.mp4?token=rFT8x3lhmiME-5vfNYpuEnqyZaWj0qGyuG_gMIGVjeOP0GsIqOVA30OxQ9DsE6_S8vfVG29bw5t9u9Hd2z9vVcehUt9ytD8J5Kw3YN3qvm58ELLVrnpZOhVKwkQWaN8wa9W3r0Uhqvi9sl8QJcc_pX14XAFRnWsq2LqD4E0ukr2YqHsb36qcESeHH-3z9Rzk2MoRh3DIs9c4ZySpcpDhpREpKxD6vPM7MvzfaNpBRJukt7GjMyYPZjXdMhOdZU5RtGbaOH1E0tFfDi2ql96vt4XEwYCwJ2Mi2a2gxOlla5jOTKqAO6w3BENHza0Kwe0MwvZfFK5Tpb3uWbisMcqnDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران: «اگر آنها حاضر باشند مردم خودشان را قتل‌عام کنند، فکر می‌کنید با ما چه خواهند کرد؟ با اسرائیل چه خواهند کرد؟ یا با همسایگان سنی خود؟»
روبیو افزود: «همه بر این باورند که ایران نباید سلاح هسته‌ای داشته باشد. تنها چیزی که تغییر کرده این است که ما رئیس‌جمهوری داریم که حاضر است در این زمینه اقدام کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/23867" target="_blank">📅 08:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d1e13c3.mp4?token=N8aDHJ-j1xoPPEPSXHkYWPXTHUpgp4mTkBmLDWHt08zYWvyKc0E7i61cASepPA2rvw2rgBuk9Jl1mczYasw9agdjrQCQjDR1bkgtwHwWhAnK-GsHS98p3KZHf2xsjtmQODqZPObD_ub8FFFphwSXIIvMqN4RgRnIQebY9WpSny3y5iYuTrlmrYEgkHg3tzdJ62Wx-3HqcBBEu0Clot7PnPI08VbO69uyuxypEF1dzK9VOsA1krVxQ58GBzPByTbxvYbP7mvomPx1c61q9EZHENhprRpAOqJyueFwIJD7ihgGDWxxEdwkH-jd-V2_AMU2TKEEL1j9MZIWdMJiR5DkGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d1e13c3.mp4?token=N8aDHJ-j1xoPPEPSXHkYWPXTHUpgp4mTkBmLDWHt08zYWvyKc0E7i61cASepPA2rvw2rgBuk9Jl1mczYasw9agdjrQCQjDR1bkgtwHwWhAnK-GsHS98p3KZHf2xsjtmQODqZPObD_ub8FFFphwSXIIvMqN4RgRnIQebY9WpSny3y5iYuTrlmrYEgkHg3tzdJ62Wx-3HqcBBEu0Clot7PnPI08VbO69uyuxypEF1dzK9VOsA1krVxQ58GBzPByTbxvYbP7mvomPx1c61q9EZHENhprRpAOqJyueFwIJD7ihgGDWxxEdwkH-jd-V2_AMU2TKEEL1j9MZIWdMJiR5DkGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: ناگهان مارکسیست‌ها و اسلام‌گراها با یکدیگر متحد و همکاری کردند و دوران افراط‌گرایی و رادیکالیسم اسلامی را به وجود آوردند.
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/23866" target="_blank">📅 08:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dbeff2ed7.mp4?token=G9_6iCNkLTSLOvgJkOQXg_QfZ0-ci63HdGYGMRMIpVH2ONs9hK6hqmS9_0A2m16T97PGR04EG6t3Mr7uQ49S9rn8uYBQWVTCGHmc7emOcQNGs-7NrU3LkxKqNEBCTM2ahF069B-BaqYoRaG2JoAYcvRMYOkP25uAuNEe_uondL_1I5GRCdu46shz55bdlejDE_VpfGYdPeCLnqmZcteCCjCF5sgK27IN5sTR3qvJG3a22lkGiFXG-G9aTmHNho_doLQCU0ZuA2ZrmBqi5LDWAASXIjCO7AGu17pLleN2oXHUJnyLFGhGX8op5PpxIU26QKmHXTXnHr858Ud-0RhHog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dbeff2ed7.mp4?token=G9_6iCNkLTSLOvgJkOQXg_QfZ0-ci63HdGYGMRMIpVH2ONs9hK6hqmS9_0A2m16T97PGR04EG6t3Mr7uQ49S9rn8uYBQWVTCGHmc7emOcQNGs-7NrU3LkxKqNEBCTM2ahF069B-BaqYoRaG2JoAYcvRMYOkP25uAuNEe_uondL_1I5GRCdu46shz55bdlejDE_VpfGYdPeCLnqmZcteCCjCF5sgK27IN5sTR3qvJG3a22lkGiFXG-G9aTmHNho_doLQCU0ZuA2ZrmBqi5LDWAASXIjCO7AGu17pLleN2oXHUJnyLFGhGX8op5PpxIU26QKmHXTXnHr858Ud-0RhHog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: پیش از انقلاب اسلامی، هر روز پروازهایی از تل‌آویو به تهران داشتیم؛ نه اینکه مانند امروز، هر روز موشک‌هایی به سمت تل‌آویو شلیک شود.</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/23865" target="_blank">📅 08:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتاق جنگ با یاشار: اجلاس کنکوردیا یک نشست غیردولتی و غیرحزبی است که هم‌زمان با هفته مجمع عمومی سازمان ملل در نیویورک برگزار می‌شود و محل حضور مقام‌های فعلی و سابق، کارشناسان و چهره‌های سیاسی و اقتصادی است. از چهره‌های مطرح حاضر می‌توان به شاهزاده رضا پهلوی ، ژنرال دیوید پترائوس، فرمانده پیشین سنتکام و رئیس پیشین سیا، نیکول پاشینیان، نخست‌وزیر ارمنستان، لیندا توماس-گرینفیلد، سفیر پیشین آمریکا در سازمان ملل، و ترزا می، نخست‌وزیر پیشین بریتانیا، اشاره کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/23864" target="_blank">📅 08:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c68d554e9.mp4?token=D245kowp9Fr7NLqwknwD71l7rlSsIkYZw6wK66KuKbKuSGMs4OcQg3UUzNuvSyZlnOCmpjGWvim-w5HetVsBnBkgAlMUyEAS-IC0Tn4Bo2vPJ9ziIQLl9K2H6wp3cVni0ql1Lorg8TFEgfUdXmZk2JLfhwsYIjRlGMOrkq47Zr8LvuAyna8He0_mf0pr9c93waAh7M9-VTwuN1-cq8u9hF5fM7MYTgzNQPqiTKsxZrwZKcYhq7JRyOmmY5cBtPQMw5IJ6Etj25Y-HCRjxZwtbQwrfYq1-XWwKwLKVPd27GWO0cEXQSCnoJcSbAwgjjPfvU87jT8o2w9sSmdNCWa5YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c68d554e9.mp4?token=D245kowp9Fr7NLqwknwD71l7rlSsIkYZw6wK66KuKbKuSGMs4OcQg3UUzNuvSyZlnOCmpjGWvim-w5HetVsBnBkgAlMUyEAS-IC0Tn4Bo2vPJ9ziIQLl9K2H6wp3cVni0ql1Lorg8TFEgfUdXmZk2JLfhwsYIjRlGMOrkq47Zr8LvuAyna8He0_mf0pr9c93waAh7M9-VTwuN1-cq8u9hF5fM7MYTgzNQPqiTKsxZrwZKcYhq7JRyOmmY5cBtPQMw5IJ6Etj25Y-HCRjxZwtbQwrfYq1-XWwKwLKVPd27GWO0cEXQSCnoJcSbAwgjjPfvU87jT8o2w9sSmdNCWa5YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: تولید ناخالص داخلی ایران در سال ۱۹۷۸ دو برابر کره جنوبی بود؛ امروز تولید ناخالص داخلی کره جنوبی پنج برابر ایران است. وضعیت اقتصاد ایران قابل دوام نیست؛ پایدار نیست و در نهایت منفجر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/23863" target="_blank">📅 08:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c403db85.mp4?token=ht-B1u3qORy9pquFU_p5qtUvtBhAYgTjOJOvAzDU6ky-v-fWtfmZ_cZZlt7VRCJfIxKzM8WtbbPg2Tuwtrt473GAUyvFSlopBotaQQzZ8RqQ-G_Dc9ufPf57xXi6-qok-5guyUzcFlqYexZ2Mt79JTxtQvQfAsU6BCzPF9h5IXNXolSxtp39JG7mXDm2uMpC2LsgAfcRUsDClCvr3pr-8vUmQa3rUGtPmpaNoWUQwAtOrEtFxhMm4bdRe4SGiygocoF1FC8h3XNVOvobdTThqaV6e9uNVBeMnNLw5XqmlUEyXG_NLPfOyLmVjF2Npk9RtTK3FOwZ5bxMjmYZDeEZig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c403db85.mp4?token=ht-B1u3qORy9pquFU_p5qtUvtBhAYgTjOJOvAzDU6ky-v-fWtfmZ_cZZlt7VRCJfIxKzM8WtbbPg2Tuwtrt473GAUyvFSlopBotaQQzZ8RqQ-G_Dc9ufPf57xXi6-qok-5guyUzcFlqYexZ2Mt79JTxtQvQfAsU6BCzPF9h5IXNXolSxtp39JG7mXDm2uMpC2LsgAfcRUsDClCvr3pr-8vUmQa3rUGtPmpaNoWUQwAtOrEtFxhMm4bdRe4SGiygocoF1FC8h3XNVOvobdTThqaV6e9uNVBeMnNLw5XqmlUEyXG_NLPfOyLmVjF2Npk9RtTK3FOwZ5bxMjmYZDeEZig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که پروازهای شرکت‌های هواپیمایی ایران در پی «عملیات طرد اقتصادی» در چندین کشور لغو شده‌اند، پزشکیان، رئیس‌جمهور رژیم ایران، برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شده و به‌سرعت به حومه شهر منتقل شده است.
سخنرانی او امروز حدود ساعت ۳-۴ به وقت تهران است
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/23862" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش‌ صدای انفجار‌ خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/23861" target="_blank">📅 01:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23860">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش‌صدای انفجار در قشم
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/23860" target="_blank">📅 01:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شاهزاده رضا پهلوی در استودیوی نیویورک فاکس نیوز:
میلیون‌ها ایرانی در ۳۱ استان، در پاسخ به فراخوان من، به خیابان‌ها آمدند و در حمایت از پایان این رژیم شعار دادند.
آنها از اقوام، ادیان و اقشار مختلف جامعه ایران بودند و این نشان‌دهنده وحدت در عین تنوع است. پهلوی گفت
این رژیم عامل ایجاد اختلاف و تفرقه در ایران است
و ایرانیان قرن‌ها فارغ از قومیت و مذهب در کنار یکدیگر در صلح زندگی کرده‌اند و پس از آزادی نیز می‌توانند دوباره متحد شوند. او در پایان گفت:
«انقلاب شیر و خورشید در راه است.»
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/23859" target="_blank">📅 01:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پرتاب موشک از بندر کنگ
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/23858" target="_blank">📅 00:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دفتر نخست‌وزیری اسرائیل در واکنش به اظهارات امانوئل مکرون اعلام کرد: «پوچی و تناقض فاحش اظهارات امانوئل مکرون تکان‌دهنده است. تنها دو روز پیش، در آستانه یوم‌کیپور، نتانل شوکرون،
شهروند فرانسوی و پدر شش فرزند
، در خودروی خود در یهودیه و سامریه توسط یک تروریست حماس کشته شد. او در آخرین لحظات زندگی‌اش به پسرش گفت فرار کند. تروریست‌های حماس تقریباً هر روز علیه یهودیان حمله انجام می‌دهند و شمار زیادی از غیرنظامیان اسرائیلی را در یهودیه و سامریه کشته‌اند. ناآگاهی،
هیچ عذری برای نادیده گرفتن خون قربانیان نیست.
»
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/23857" target="_blank">📅 00:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تتر و دلار دارن میکشن پایین
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/23856" target="_blank">📅 00:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23855">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیویورک‌پست:
جمهوری اسلامی ایران در چارچوب یک طرح وابسته به سپاه،
حداقل سن جذب نیرو را به ۱۲ سال کاهش داده است
. یک مقام سپاه در تهران اعلام کرده بود نوجوانان ۱۲ و ۱۳ ساله می‌توانند برای حضور در گشت‌های اطلاعاتی و عملیاتی ثبت‌نام کنند. گزارش‌های بی‌بی‌سی و عفو بین‌الملل نیز از حضور کودکان در ایست‌های بازرسی و مواردی از حمل سلاح توسط آنها خبر داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/23855" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ:
ما به دنبال تغییر رژیم یا جایگزین کردن حکومت ایران نیستیم؛ هدف آمریکا این است که
ایران به سلاح هسته‌ای دست پیدا نکند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/23854" target="_blank">📅 00:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فاکس‌نیوز:
دونالد ترامپ اخیراً با امضای حکمی،
مارکو روبیو، وزیر خارجه آمریکا، را به‌طور رسمی و دائمی به‌عنوان مشاور امنیت ملی کاخ سفید منصوب کرد.
روبیو از مه ۲۰۲۵ پس از برکناری مایکل والتز، به‌صورت موقت این سمت را بر عهده داشت و اکنون انتصاب او دائمی شده است. روبیو همچنان وزیر خارجه آمریکا نیز خواهد بود و همزمان مدیریت روند شورای امنیت ملی و نقش مشاور مستقیم رئیس‌جمهور در مسائل امنیتی را بر عهده خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/23853" target="_blank">📅 23:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرگزاری i24news : ‏اکسپلور گردی« احمد الشرع » وسط سخنرانی اردوغان در سازمان ملل
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23852" target="_blank">📅 23:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dcb0a852.mp4?token=OpA75CY7fqIeaA-n6fE5IvmRR2PJafKbNc7cw9rblY3ASSPS4XosO8tR53BUU1zFW5O7xlaMq3xGmNcPRbCDP2AWW9W80doF5DG7_U_k3GHLnHt86znii1UTFJLyg1gF11DFHpsHx-ARDc5RSSKzPKsyygus83PIX8XfxCN7iaxz8j0A46F3qrJIvKFE_0LvB2pMq7D1zj_vlgeDhyasroFYIoEHtXQOylUVCM-KCqFbiYeiTMC4MPCJ9pmKPef_Q4L78GSsf6w-d_N870TP6z2X1HWJ7QQj93Pqqy5thb6p7rL_yJhQeblntCNDIaQuEvwgyd3i6k-iM-RPm6ZSsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dcb0a852.mp4?token=OpA75CY7fqIeaA-n6fE5IvmRR2PJafKbNc7cw9rblY3ASSPS4XosO8tR53BUU1zFW5O7xlaMq3xGmNcPRbCDP2AWW9W80doF5DG7_U_k3GHLnHt86znii1UTFJLyg1gF11DFHpsHx-ARDc5RSSKzPKsyygus83PIX8XfxCN7iaxz8j0A46F3qrJIvKFE_0LvB2pMq7D1zj_vlgeDhyasroFYIoEHtXQOylUVCM-KCqFbiYeiTMC4MPCJ9pmKPef_Q4L78GSsf6w-d_N870TP6z2X1HWJ7QQj93Pqqy5thb6p7rL_yJhQeblntCNDIaQuEvwgyd3i6k-iM-RPm6ZSsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره تنگه هرمز: «ما هر شب ۲۵ تا ۳۰ کشتی را از بین می‌بریم؛ گاهی هم در طول روز، اما بخش زیادی از آن در شب انجام می‌شود. این محاصره قوی‌ترین چیزی است که تاکنون دیده شده و ما آن را «دیوار فولادی» می‌نامیم. اکنون نسبت به هر زمان دیگری از آغاز درگیری، نفت بسیار بیشتری از طریق تنگه هرمز عبور می‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23850" target="_blank">📅 23:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb899a45a.mp4?token=WDZext_VAxsGP43ms1YbLYgrk28r6eacA4xt4S3dwurUgn7Jj1POvTZ11GQooE7fYzvHdeXc-Tf6wHFN21j8DGTJDP6QNA3VmrsAPWLKPa6q1Ksjpql5zcIxzbhE9FPMrT8atNPhc3xOCpU-NCOXo4pKZ7PWFcSR8xAGcBaRrbKwarKC9NXjuXBV8IVTEx14-qv1zhlAorqrA6eOdsmqkH54dF_LYDuH7Yhkf6yF_dtx6bl0KFndqVAIYWX0G_GLnnWLGTAqAJYttaQbclymTzO72Z8HMrar34jj8bHlAvhAPXmZ_Bkcol9qD3WdtBhVkaBtiMXLRz6mc39sawv9Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb899a45a.mp4?token=WDZext_VAxsGP43ms1YbLYgrk28r6eacA4xt4S3dwurUgn7Jj1POvTZ11GQooE7fYzvHdeXc-Tf6wHFN21j8DGTJDP6QNA3VmrsAPWLKPa6q1Ksjpql5zcIxzbhE9FPMrT8atNPhc3xOCpU-NCOXo4pKZ7PWFcSR8xAGcBaRrbKwarKC9NXjuXBV8IVTEx14-qv1zhlAorqrA6eOdsmqkH54dF_LYDuH7Yhkf6yF_dtx6bl0KFndqVAIYWX0G_GLnnWLGTAqAJYttaQbclymTzO72Z8HMrar34jj8bHlAvhAPXmZ_Bkcol9qD3WdtBhVkaBtiMXLRz6mc39sawv9Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
بخش بزرگی از اقداماتی که انجام داده‌ایم — شاید ۹۹ درصد آن — برای اطمینان از این بوده است که ایران به سلاح هسته‌ای دست پیدا نکند. آن تأسیسات منهدم شده‌اند. ممکن است مجبور شویم تأسیسات دیگری را هم منهدم کنیم: «کوه کلن گزلا» (Pickaxe Mountain). در حال حاضر فعالیت زیادی در آنجا مشاهده نمی‌کنیم، اما اگر شاهد فعالیتی باشیم، بلافاصله آن را منهدم خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23849" target="_blank">📅 23:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37263286bc.mp4?token=WQW20szFs5nMGu7XYEL23wPevBe8Mzdnt-4ptWPvMhwAjpbCbqIfsFtEkcnJ-m8Td9EempMD-MvdYSsD7k2CcIZLkETF_G81pDUZ4sEIhIad98J4tIjooAE7BlWy8vNNe6tm9KcAKX4X2F6q108fSeCd-wIjLX44dyAXaGNkBjdQeRZR-mzR6uDrHSDhydjVvNybje3RyLMwEBeqG55FGDAXpPk9UNfzzsG9cm_Gnucp3oGuaKPQfzB3E8PiQBJI2ZcsbjYWgNFYVcBQnkOIYV6VX66vOhBI9aMxIULmPEYWtLviJc4X-PbNx6A19aS6EI3NRdlzrh2cvc-cOeDzmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37263286bc.mp4?token=WQW20szFs5nMGu7XYEL23wPevBe8Mzdnt-4ptWPvMhwAjpbCbqIfsFtEkcnJ-m8Td9EempMD-MvdYSsD7k2CcIZLkETF_G81pDUZ4sEIhIad98J4tIjooAE7BlWy8vNNe6tm9KcAKX4X2F6q108fSeCd-wIjLX44dyAXaGNkBjdQeRZR-mzR6uDrHSDhydjVvNybje3RyLMwEBeqG55FGDAXpPk9UNfzzsG9cm_Gnucp3oGuaKPQfzB3E8PiQBJI2ZcsbjYWgNFYVcBQnkOIYV6VX66vOhBI9aMxIULmPEYWtLviJc4X-PbNx6A19aS6EI3NRdlzrh2cvc-cOeDzmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
یا به توافق می‌رسیم، یا کار خیلی خیلی سریع تمام خواهد شد.
آن‌قدر سریع تمام می‌شود که سرتان گیج می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23848" target="_blank">📅 23:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/540fba7a3f.mp4?token=DMHTWZdwNhni0bHuWPPCk8A87YC7EX80UHMSm0ALrKOyfjHJoW9ya18rwGJZhkVP9amVZz9kxC6EfKC_F_IMkOInhw-IxNKQRSY5AZ45IWBZ4Mspl5vC8g5_AQmp6ebGdeC8QUYLd83VkxX6bHO_ANcGgGxCiBSRIX1ClxRqVVfNPpsnc86KxC4e3QYcw6Ta3-0c1G-0tBTab3g_RyNbHqYeW0QweCG858UkISHj5nZ_bJtnExtqpeiHBNdM7yjMSave2eeZSH6droH9Dy4wDbr5jB5EjLNllfcl7s1dLmH1vzjkvEXnkyN6ox2MvdiAkopyEHU8CJZ0A4iR5HJEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/540fba7a3f.mp4?token=DMHTWZdwNhni0bHuWPPCk8A87YC7EX80UHMSm0ALrKOyfjHJoW9ya18rwGJZhkVP9amVZz9kxC6EfKC_F_IMkOInhw-IxNKQRSY5AZ45IWBZ4Mspl5vC8g5_AQmp6ebGdeC8QUYLd83VkxX6bHO_ANcGgGxCiBSRIX1ClxRqVVfNPpsnc86KxC4e3QYcw6Ta3-0c1G-0tBTab3g_RyNbHqYeW0QweCG858UkISHj5nZ_bJtnExtqpeiHBNdM7yjMSave2eeZSH6droH9Dy4wDbr5jB5EjLNllfcl7s1dLmH1vzjkvEXnkyN6ox2MvdiAkopyEHU8CJZ0A4iR5HJEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما فشار ‌زیادی ‌رویشان قرار‌دادیم ،امیدوارم پیش از آنکه خیلی دیر شود، هرچه سریع‌تر کار درست را انجام دهند. می‌دانید، زمانی فرا خواهد رسید که دیگر خیلی دیر شده باشد و ما دیگر فرصتی برای اینکه اجازه دهیم آن‌ها به عنوان یک ملت باقی بمانند، نخواهیم داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23847" target="_blank">📅 23:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23846">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a4e00219.mp4?token=r5Bql0JQEnhjHopWgikRcWxWMNBSxEcV1QFavxawQrUd2JXdHzqZ62NaLiPrICrsfo3O7ZZCidZ9pRS4BcUFdDMGRsG8cpR7qGwCGGzdbD_3KqDRCJ3bKRWiKoXfePEePu6swATDskW_IyfbUKhs98b36R_rhorc_dp3S5oFuHe-9H_2onjaoNzfOJcgyB-A0-hLywjVcK00NPJLBCcJZ7bbyYUpSYxunfftzMsW8zlFzXfKn-R3rqEctjlMP839wdjfgyBbjdxksfZ-_0YH2VUEcMIRRtU-tK3Dx569iBJLY6s9er7yrr-2Kvt-Pch322_Qu9bcCYjsQR92aI6krQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a4e00219.mp4?token=r5Bql0JQEnhjHopWgikRcWxWMNBSxEcV1QFavxawQrUd2JXdHzqZ62NaLiPrICrsfo3O7ZZCidZ9pRS4BcUFdDMGRsG8cpR7qGwCGGzdbD_3KqDRCJ3bKRWiKoXfePEePu6swATDskW_IyfbUKhs98b36R_rhorc_dp3S5oFuHe-9H_2onjaoNzfOJcgyB-A0-hLywjVcK00NPJLBCcJZ7bbyYUpSYxunfftzMsW8zlFzXfKn-R3rqEctjlMP839wdjfgyBbjdxksfZ-_0YH2VUEcMIRRtU-tK3Dx569iBJLY6s9er7yrr-2Kvt-Pch322_Qu9bcCYjsQR92aI6krQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: استیو و جارِد امروز جلسه‌ای بسیار سازنده با دو میانجی از ایران داشتند. خواهیم دید که نتیجه این جلسه چه خواهد بود.
به نظر من، یک حرکت قوی برای رسیدن به توافق وجود دارد. این چیزی است که ما از همه می‌شنویم.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23846" target="_blank">📅 23:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسرائیل هیوم به نقل از منابع آمریکایی:
یک دیدار از پیش برنامه‌ریزی‌شده میان مقام‌های آمریکایی و هیئت ایرانی به ریاست عباس عراقچی، با حضور نخست‌وزیر قطر، برگزار شد و در آن درباره ازسرگیری مذاکرات میان تهران و واشنگتن و همچنین بازگشایی تنگه هرمز گفت‌وگو شد. با این حال، طرفین درباره مسائل مورد اختلاف به توافقی دست پیدا نکردند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23845" target="_blank">📅 22:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بلومبرگ به نقل از مقام‌های آمریکایی و افراد مطلع گزارش داد آمریکا هوش مصنوعی خود را تغییر داد چون حمله مرگبار به مدرسه میناب نتیجه مجموعه‌ای از خطاهای اطلاعاتی و هدف‌گیری بوده است. بر اساس این گزارش، اطلاعات قدیمی ارتش آمریکا همچنان مدرسه را به‌عنوان یک تأسیسات سپاه ثبت کرده بود، در حالی که تصاویر ماهواره‌ای نشان می‌داد این محل سال‌ها قبل به مدرسه تبدیل شده است. همچنین فشار زمانی برای تعیین بیش از هزار هدف و اتکای برخی نیروهای سنتکام به سامانه هوش مصنوعی «Maven» در روند هدف‌گیری نقش داشت. پس از این حمله، قابلیت‌های جدیدی به Maven اضافه شد تا اطلاعات اهداف، تناقض‌ها و عواملی را که می‌توانند باعث خروج یک هدف از فهرست حمله شوند، دوباره بررسی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23844" target="_blank">📅 22:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">توییت جدید
https://x.com/yasharrapfa</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23843" target="_blank">📅 22:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23842">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آکسیوس:
کشورهای عربی در نیویورک تلاش می‌کنند
دیدار مستقیم ترامپ و مسعود پزشکیان
را در حاشیه مجمع عمومی ترتیب دهند
@WarRolm</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23842" target="_blank">📅 22:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سازمان هواپیمایی کشوری ایران: از نیمه شب امشب، فرودگاه‌های بغداد و مسقط، پروازهای هواپیمایی ایران را پذیرش نخواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23841" target="_blank">📅 22:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سخنگوی سپاه:درحال آماده سازی برای سناریوی حمله پیش‌دستانه به پایگاه های آمریکا در منطقه هستیم،در صورتی که حمله ای از سوی آمریکا به ایران محرز شود.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23840" target="_blank">📅 22:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ویتکاف: دیدار با ایرانی‌ها خوب پیش رفت و در حال حاضر احساس بسیار خوبی دارم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23839" target="_blank">📅 22:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرنگار i24: استیو ویتکاف و جرد کوشنر، مقام‌های آمریکایی بودند که امروز با هیئت ایرانی دیدار کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23838" target="_blank">📅 22:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">بازنشری دوباره از صحبت های بسیار مهم از صحبت های مانوک درباره مذاکره و آینده ایران
مجری  :  آیا به توافقی میرسند؟
آیا مذاکره می‌کنند؟ یا ایران رد خواهد کرد؟
مانوک خدابخشیان : ایران رد نخواهد کرد، اگر بپذیرند خلع سلاح کامل می‌شوند، و مجبور به پذیرش بقیه شرط ها حقوق بشر دیگر برگ کوبنده ای نیست زیرا صدها برگ دیگر وجود دارد
مجری: ترامپ میگه پیشرفت زیادی در ارتباط با ایران به دست آمده! از این پیشرفت منظورش چیه؟
مانوک خدابخشیان : دونالد زبل بزرگترین خواسته اش اینه با یکی از این ها سلفی بگیره! ایمان داشته باشید«اینها با یک جماعتی در تهران ساخت و پاخت کردن!»نه این که رژیم بمونه!
یادتون نره!
همه ترسشون اینه امروز آمدن مذاکره کردن کار تموم شد ، استمرار پیدا کرد این رژیم ،نه اینچنین نیست.
«این تحلیل های آبکی رو بعد بذارید و بعد بگید »
آمریکا جایی که رفت مذاکره کنه مذاکره نمیکنه ، باز تکرار میکنم « حکم میکنه »
ببینید آیا رژیم جمهوری اسلامی حاضره مثل صدام حسین تحقیر بشه ؟ اینا به نوکر صدام گفتن برید بهش بگید تمام سلاح های اتمی و شیمیایش بده به ما و بعدش میشینیم مذاکره میکنیم و دیدید صدام حسین تو سری رو خورد چرا ؟ چون «بازی تموم شده رژیم کارش تمومه »
اگر یک آلترناتیو الان بود و اطمینان خاطر داشتن اینها در ایران بحران به وجود نمیاد قطعا عمل میکردن و الانم قول هایی گرفتن!
دلیل خوشحالی ترامپ هم همینه
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23837" target="_blank">📅 22:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">@WarRoom
Selfie</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23836" target="_blank">📅 21:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=DmY4WzA4AWJEKXDzcgamWnqbc4YUs_7r_FOBs8rAhnm_4WP7md0WVaoYkPJ0i96fCY_UBHwIcffDSlbI2QwVXR10-GG-b9t6CQUmcy3AOkaeagh0zJBnWrYJatFBUqUMqOoAui-knfzfo5hKQE3uDR8ybgmsRgrq3PyFUMJ7vcq5kzuMhnxait_Pk3RmrTqwVDG-Qf4YBLQf05NSCg02hfDnio58RoZGE5l7jPkGRcdZYs9PkW0efan62kB7PbLLGpbzUAsk0u5f6mVJrNfxuL-PFIRXO53drr3yc7VaHy-eBFTQGbmevdiJyhPDt4UtGH4PtblfTERDmVHq_40r1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=DmY4WzA4AWJEKXDzcgamWnqbc4YUs_7r_FOBs8rAhnm_4WP7md0WVaoYkPJ0i96fCY_UBHwIcffDSlbI2QwVXR10-GG-b9t6CQUmcy3AOkaeagh0zJBnWrYJatFBUqUMqOoAui-knfzfo5hKQE3uDR8ybgmsRgrq3PyFUMJ7vcq5kzuMhnxait_Pk3RmrTqwVDG-Qf4YBLQf05NSCg02hfDnio58RoZGE5l7jPkGRcdZYs9PkW0efan62kB7PbLLGpbzUAsk0u5f6mVJrNfxuL-PFIRXO53drr3yc7VaHy-eBFTQGbmevdiJyhPDt4UtGH4PtblfTERDmVHq_40r1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23835" target="_blank">📅 21:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23834" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23833" target="_blank">📅 21:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecad76c05b.mp4?token=bP0naKQqF565XzcyImfa9253NZjBZuLrQ26Ujdi2oR0N-XJm55YfkpLXTti0lzlUL9iyPABnEJ-PyUhcbGdCaifxw5K5JbsEKs5mc8oUXdDsyIn4thkb8yaNBX7Qk6boLnWjgOIhPdTxtGSs8j-giHgcx9S8goVH68gKoaoUVx8EvyC7_UzOHhoT2H5Oo9b3rdhzqRFBFw8yDUSEpjJK-_sthxy5rNinfSGeFBARpZiVOJbiLJ5qyRgikOpNoshLWGfTZQwZTU4KQ9h6DDHjVKMSTG-v7JC-_lTM5p6ER__jnJvVMSnAEGejAGLiY4JZ26oUj5TlKP4HStbiuTeeEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecad76c05b.mp4?token=bP0naKQqF565XzcyImfa9253NZjBZuLrQ26Ujdi2oR0N-XJm55YfkpLXTti0lzlUL9iyPABnEJ-PyUhcbGdCaifxw5K5JbsEKs5mc8oUXdDsyIn4thkb8yaNBX7Qk6boLnWjgOIhPdTxtGSs8j-giHgcx9S8goVH68gKoaoUVx8EvyC7_UzOHhoT2H5Oo9b3rdhzqRFBFw8yDUSEpjJK-_sthxy5rNinfSGeFBARpZiVOJbiLJ5qyRgikOpNoshLWGfTZQwZTU4KQ9h6DDHjVKMSTG-v7JC-_lTM5p6ER__jnJvVMSnAEGejAGLiY4JZ26oUj5TlKP4HStbiuTeeEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
امروز، یک ساعت پیش گفتگویی با مقامات ایرانی انجام شد. آن بسیار خوب بود. یک ساعت پیش به پایان رسید.
این یک جلسه‌ای بود که سه ساعت طول کشید.
این یک عظمت، عظمت بالقوه، یا نابودی است.
در یک حالت، نابودی است. و گزینه دیگر، عظمت بالقوه است. می‌تواند کشوری بزرگ باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23832" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خیرگزاری جِی‌فید اسرائیل :
۱۲ فروند جنگنده
F-16C
متعلق به گارد ملی هوایی اوکلاهما از پایگاه اسپانگدالم در آلمان به سمت منطقه عملیاتی
سنتکام در خاورمیانه
حرکت کردند. این جنگنده‌ها که از حدود یک هفته قبل در آلمان مستقر شده بودند، در سه گروه چهار فروندی پرواز کرده و با همراهی
سه فروند سوخت‌رسان KC-135R
به سمت خلیج فارس حرکت کردند. این جابه‌جایی در حالی انجام می‌شود که حضور هوایی آمریکا در منطقه همچنان در حال تقویت است. همزمان، امروز یک فروند
F-16 متعلق به بال ۵۲ جنگنده آمریکا
در نزدیکی پایگاه اسپانگدالم سقوط کرد؛ خلبان با موفقیت ایجکت کرد اما زخمی شد و برای درمان به بیمارستان منتقل شد. علت سقوط در دست بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23830" target="_blank">📅 21:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23829" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23828">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نکات مهم و جدید صحبتهای تکراری ترامپ در مجمع عمومی سازمان ملل  : بخش عمده صحبت‌هایش را به
ایران و جنگ
اختصاص داد و گفت اگر تهران به توافق نرسد، آمریکا می‌تواند جمهوری اسلامی را
«نابود کند»
؛ در عین حال تأکید کرد مسیر مذاکره همچنان باز است و ایران باید تنگه هرمز را بازگشایی کند. او از کشورها خواست به
انزوای اقتصادی ایران
بپیوندند. درباره
کوبا
گفت حکومت کمونیستی این کشور شکست‌خورده است و
«آزادی به کوبا خواهد آمد»
. درباره
غزه
از طرح صلح خود و پایان جنگ گفت و درباره
اوکراین
خواستار پایان جنگ روسیه و اوکراین شد. ترامپ درباره
گرینلند
بر گسترش حضور نظامی آمریکا تأکید کرد، از سیاست آمریکا در
ونزوئلا و مقابله با کارتل‌های مواد مخدر
دفاع کرد و به‌شدت از
سازمان ملل و دادگاه کیفری بین‌المللی
انتقاد کرد. او همچنین درباره
هوش مصنوعی
با محدودیت‌های بین‌المللی مخالفت کرد و گفت آمریکا باید در رقابت برای دستیابی به
ابرهوش
پیشتاز باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23828" target="_blank">📅 21:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امروز ۳۱ آغاز جنگ ایران و عراق و آغاز هفته دفاع مقدس است. ممکن است صداها برای این هم باشد, همچنین گزارشاتی الان به دستم رسیده که در پارک شمیم تبریز رزمایش است
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23827" target="_blank">📅 21:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تبریز صدای انفجار وحشتناکککک @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23826" target="_blank">📅 21:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تبریز صدای انفجار وحشتناکککک
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23825" target="_blank">📅 21:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رویترز:
عربستان عملیات خط لوله شرق-غرب خود را از سر گرفته؛ این تحول نگرانی درباره اختلال در صادرات نفت منطقه را تا حدی کاهش داده است
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23824" target="_blank">📅 21:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رویترز:
ترامپ‌ در ‌سازمان ملل از کشورهای جهان خواست برای اعمال
انزوای اقتصادی کامل ایران
همکاری کنند و گفت تهران باید تنگه هرمز را کاملاً باز کند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23823" target="_blank">📅 21:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mA9YX1UM_Ps6pLc1K8s2xC0W5DCwqLcCQi8PK65BVVp4zLFBlpSndwAQJ5UTC9ej0RGlPDUaICgrDKtJ84DobMo-BKdMBQfhAPCOlkU1jYZVUEVnGi1caov-WKfKNEKHTk_NI8dbO5P1i8mPGaAtj64mZSNEUcKQmpRXcQ_jT3KliP8LjAf2Wxd426mw6kgKTwNjJp66sDJYwups4fD7_YHeUfpSCbCzuF5-Um4CQ_qy4md6As2eRC1kylnkVwdfJ-HnrJoVvQpcTqFGenGhRItCBq-b60aYb9OjHgcewBd9WfkOui0DwVPC-uE3ac9Q8cdk3cFHQYhO4p686pICCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه عالی پودگوریتسا با استرداد امیر براتی، شهروند ایرانی-ترکیه‌ای، به آمریکا موافقت کرد.
مقام‌های مونته‌نگرو او را مرتبط با سپاه پاسداران معرفی کرده‌اند و آمریکا متهمش کرده است که از سال ۲۰۱۳ در حملات سایبری علیه بیش از
۱۵۰ دانشگاه و مؤسسه آمریکایی
مشارکت داشته و این حملات بیش از
۳.۴ میلیارد دلار خسارت
به بار آورده است. براتی در ۲۵ ژوئن در شهر کوتور مونته‌نگرو، به درخواست آمریکا بازداشت شد. او در دنیای هکری با نام
«کینگ‌لِت»
شناخته می‌شد و بعدها با نهادهای اطلاعاتی ایران همکاری داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23822" target="_blank">📅 20:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ درباره ایران: «فکر می‌کنم توافقی حاصل خواهد شد. آن‌ها حتی امروز هم با ما در حال گفت‌وگو بوده‌اند , بگذارید بگوییم که این رابطه در حال شکل‌گیری و پیشرفت است.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23821" target="_blank">📅 20:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315709f99a.mp4?token=c5Jqaj0hib1wWTqUcn5VPIPdCb9Ht7WqNojFNiIyXwZiLyPdW7nyCW5BDuUoXvNiiqXgVKt0omrjgPB-WBwdPBzYe5duYuedAS0aYF85NIxEdQhn6l6EfZKyYxs60OQrWdDUOkhavi34tz44JHJ0h9_F-rghVXRUrNNvIMhrbbNYaFr-tHmmRL9CRtL2qiI43RuRP__cTHtI4PYTwEhyvII-YelnE8putyz88UkzCCqG6eDPhhTRNjYxNZ-5jb3oql0A7YISTUnMvky4xL_F0-W1ndhsQQaejAlr_KnFoq9XPN5hNyeVSjTjmlI6sx_JV9Fl-PMVxsLkikAGf2NgJSjz6TFLHE4x0rOyIh3NgFsTZIMKp-jLCOD10xmTqBOX2T6Tb75q-v59oK5bKEjRAirqKuwA-1mweldy7aD0i8Np6fOG5tWy9SzN0fiXRjAexEv9BdoiCFDvITdQHJRCZyR3z9K9YwOOGz4t3s19hUEYj5GGlmk408lOVHX4KICzg62VQsOzo5msjf9LwC9R62GTdczATMYRbATIw-I5tMx0KeRZf_OPTWlWYxj5nS5lVOC4zghj-2kBTjXXHEn3pYmFnRQXQ-nNv9D6CCHXfmEjRCJKeaN2WwIBs2MQoc-ZeAM2h3GCSf9_d0xxJbY3fSCsKL9HT6gI18awyaa3udg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315709f99a.mp4?token=c5Jqaj0hib1wWTqUcn5VPIPdCb9Ht7WqNojFNiIyXwZiLyPdW7nyCW5BDuUoXvNiiqXgVKt0omrjgPB-WBwdPBzYe5duYuedAS0aYF85NIxEdQhn6l6EfZKyYxs60OQrWdDUOkhavi34tz44JHJ0h9_F-rghVXRUrNNvIMhrbbNYaFr-tHmmRL9CRtL2qiI43RuRP__cTHtI4PYTwEhyvII-YelnE8putyz88UkzCCqG6eDPhhTRNjYxNZ-5jb3oql0A7YISTUnMvky4xL_F0-W1ndhsQQaejAlr_KnFoq9XPN5hNyeVSjTjmlI6sx_JV9Fl-PMVxsLkikAGf2NgJSjz6TFLHE4x0rOyIh3NgFsTZIMKp-jLCOD10xmTqBOX2T6Tb75q-v59oK5bKEjRAirqKuwA-1mweldy7aD0i8Np6fOG5tWy9SzN0fiXRjAexEv9BdoiCFDvITdQHJRCZyR3z9K9YwOOGz4t3s19hUEYj5GGlmk408lOVHX4KICzg62VQsOzo5msjf9LwC9R62GTdczATMYRbATIw-I5tMx0KeRZf_OPTWlWYxj5nS5lVOC4zghj-2kBTjXXHEn3pYmFnRQXQ-nNv9D6CCHXfmEjRCJKeaN2WwIBs2MQoc-ZeAM2h3GCSf9_d0xxJbY3fSCsKL9HT6gI18awyaa3udg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا، جی‌دی ونس:
«رأی‌دهندگان بیشتر روی
مسائل داخلی و محلی که برایشان اهمیت دارد
تمرکز کرده‌اند و نه جنگ با ایران.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23820" target="_blank">📅 19:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815a7ec77d.mp4?token=XMqJMV8YUYVg1KILd2vqjIaKbzozFlZkgo7CPHTFVGiiUgfnNFGopfhXqE_rbkiGRxzPxbokR8VGeDUHZpWFRLYf_oEBaLVW_fOnzIinHcl005WO4p0Oo6zx9LlnEsyZQ5L_-RwpPtLSsxiWZHsqC1F85fyDfAEFsZ25jkaYUVueLweibqSZEhFFGVamMADP67LdeGhZzLcK7cKfkcm0oVLPLAW4zGqZS9qPlOQshbDCx_3KPGdnnNLuGPX7CJ1G7aZpLTwsW79g4B7OrA-yjPhRejBc1ItX0a0KcvsruIy4rnnYzunR3j_yX_Y8CMaRrGdxxx8ZVrd666Ll_aXrKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815a7ec77d.mp4?token=XMqJMV8YUYVg1KILd2vqjIaKbzozFlZkgo7CPHTFVGiiUgfnNFGopfhXqE_rbkiGRxzPxbokR8VGeDUHZpWFRLYf_oEBaLVW_fOnzIinHcl005WO4p0Oo6zx9LlnEsyZQ5L_-RwpPtLSsxiWZHsqC1F85fyDfAEFsZ25jkaYUVueLweibqSZEhFFGVamMADP67LdeGhZzLcK7cKfkcm0oVLPLAW4zGqZS9qPlOQshbDCx_3KPGdnnNLuGPX7CJ1G7aZpLTwsW79g4B7OrA-yjPhRejBc1ItX0a0KcvsruIy4rnnYzunR3j_yX_Y8CMaRrGdxxx8ZVrd666Ll_aXrKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت اسرائیلی هنگام سخنرانی رجب طیب اردوغان، رئیس‌جمهور ترکیه، در مجمع عمومی سازمان ملل، سالن را ترک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23819" target="_blank">📅 19:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23818">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آکسیوس:
قرار است تا ساعاتی دیگر در نیویورک،
دونالد ترامپ با رهبران کشورهای عربی خلیج فارس
دیداری مهم داشته باشد و درباره
ادامه جنگ با ایران
گفت‌وگو کند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23818" target="_blank">📅 19:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فرانس‌پرس:
امانوئل مکرون در دیدار با ترامپ چند طرح برای کاهش بحران انرژی پیشنهاد کرده که یکی از آنها تلاش در سازمان ملل برای
باز کردن تنگه هرمز
است. مکرون همچنین پیشنهاد حفاظت از تأسیسات نفتی عربستان در برابر حملات حوثی‌ها را مطرح کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23817" target="_blank">📅 19:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آسوشیتدپرس:
دونالد ترامپ امروز در سخنرانی خود در مجمع عمومی سازمان ملل از تصمیمش برای آغاز جنگ با ایران دفاع کرد و گفت آمریکا در حال «تسویه حساب با مسائل حل‌نشده» است. ترامپ تأکید کرد ایران نباید به سلاح هسته‌ای دست پیدا کند و گفت آمریکا برای پایان جنگ آماده گفت‌وگو است. هیئت ایرانی در جریان سخنرانی ترامپ از سالن خارج شد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23816" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ:
«کارتل‌ها، داعشِ نیمکره غربی هستند؛ افراد خوبی نیستند. همانند داعش، باید
کشته، تبعید یا به‌عنوان نیروهای دشمن بازداشت شوند، بدون امکان آزادی
؛ و ما همین کار را انجام می‌دهیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23815" target="_blank">📅 18:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce094c02c0.mp4?token=gdYRW40VZAVokPngRbrZmAhir9G6FQwJ1DkTxuuQhwyoKM5Wr1DgBPoXdsv4LqmVlT88nkVLlMS0nAz3TJTRr6OXKIqDGjHR07mZ1j8PJiKvXTmX5tYZWzIknR5K_GakTBnAlra8VVAoLQcgJyLV3-0M8csiGFbHFv0ygTkqGJi6tgRPpjCW81u9JIpFgJGkBo-BsMbQtZREOSMUfIIZWuPy_K-9kRHuR5U5sVI1pH4snoRTk4tw1DANnymJd23RCI990zuvP0f7cposeNkS9QiWuVt6HNFcahZiYBGTuIOwAFKmeR1VxSUlsYN8x29srrF3TvFK4gT9C5m8mm-OUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce094c02c0.mp4?token=gdYRW40VZAVokPngRbrZmAhir9G6FQwJ1DkTxuuQhwyoKM5Wr1DgBPoXdsv4LqmVlT88nkVLlMS0nAz3TJTRr6OXKIqDGjHR07mZ1j8PJiKvXTmX5tYZWzIknR5K_GakTBnAlra8VVAoLQcgJyLV3-0M8csiGFbHFv0ygTkqGJi6tgRPpjCW81u9JIpFgJGkBo-BsMbQtZREOSMUfIIZWuPy_K-9kRHuR5U5sVI1pH4snoRTk4tw1DANnymJd23RCI990zuvP0f7cposeNkS9QiWuVt6HNFcahZiYBGTuIOwAFKmeR1VxSUlsYN8x29srrF3TvFK4gT9C5m8mm-OUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
دونالد ترامپ درباره ایران گفت: «آمریکا و ایران قطعاً این مسئله را حل خواهند کرد؛ به هر طریقی که باشد، این کار انجام خواهد شد.»
او افزود: «این اتفاق سریع رخ خواهد داد.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23814" target="_blank">📅 18:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ: جنگ اوکراین زودتر از آنچه مردم تصور می‌کنند پایان خواهد یافت
دونالد ترامپ درباره جنگ اوکراین گفت: «ما همکاری بسیار نزدیکی با رهبران روسیه و اوکراین داریم و این مسئله را حل خواهیم کرد.»
او افزود: «فکر می‌کنم این اتفاق سریع‌تر از آنچه مردم تصور می‌کنند رخ خواهد داد؛ آن‌ها دیگر از این جنگ خسته شده‌اند.»
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23813" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: بزدلان و خائنان دوست دارند بگویند ایالات متحده با کمبود مهمات مواجه است، اما چنین چیزی درست نیست.
ما بیش از آن مقدار مهماتی داریم که حتی بتوانیم تصور کنیم ممکن است از آن استفاده کنیم و در حال تولید مهمات با سطوحی هستیم که هرگز پیش از این تجربه نکرده‌ایم. ما ذخایر خود را سریع‌تر از هر زمان دیگری افزایش می‌دهیم؛ مهمات و تجهیزات درجه‌یک.
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. در حال حاضر ۱۸ کارخانه توسط بزرگ‌ترین شرکت‌های صنایع دفاعی جهان در حال ساخت است؛ ۱۸ کارخانه در دست احداث است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23812" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: ایران ۷۲هزار شهروند معترض بی گناه خود را به قتل رسانده است @WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/23811" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23810">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc729c6f5e.mp4?token=iHZtwrtMzL-uAh2EdAUuFVnwsdDtlEUWjZLNgaV-lCEL2gP14Kk1k5_Y3u52eo7fjI-gZghi-nmtCIGNPHZydfUfAD4D1B9iAfsf1DOleb-ZgmFvVyjG5w0rZz_xiCthJSRj_hHF4g-Kk7Y2nwEyz-0ImcxN9QuY7-J0BoXjF5Z9rd0vJcNzjVCIGKb2zlOIBKRghn29wq8UioCtapCgvLEXNZGPEUrCcYLZmUua5GSO2PartQ-Kt3I38Emez50diivxhpHEkXr2Ry3yPHSVwyWYxfUm-VOfuYzF6UfwxZkMGJXwNuCQsGIUIFa81oCLruDi0lfe5LIWbUx8kzEwMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc729c6f5e.mp4?token=iHZtwrtMzL-uAh2EdAUuFVnwsdDtlEUWjZLNgaV-lCEL2gP14Kk1k5_Y3u52eo7fjI-gZghi-nmtCIGNPHZydfUfAD4D1B9iAfsf1DOleb-ZgmFvVyjG5w0rZz_xiCthJSRj_hHF4g-Kk7Y2nwEyz-0ImcxN9QuY7-J0BoXjF5Z9rd0vJcNzjVCIGKb2zlOIBKRghn29wq8UioCtapCgvLEXNZGPEUrCcYLZmUua5GSO2PartQ-Kt3I38Emez50diivxhpHEkXr2Ry3yPHSVwyWYxfUm-VOfuYzF6UfwxZkMGJXwNuCQsGIUIFa81oCLruDi0lfe5LIWbUx8kzEwMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران ۷۲هزار شهروند معترض بی گناه خود را به قتل رسانده است
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23810" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
دونالد ترامپ درباره ایران گفت: «پس از آغاز به کارم در سال گذشته، مذاکرات با ایران را آغاز کردم و در ازای پایان دادن به برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی را به آن‌ها پیشنهاد دادم.»
او افزود: «اما آن‌ها این پیشنهاد را رد کردند؛ این یک اشتباه بزرگ بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/23809" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: ایران دیگر قلدر خاورمیانه نیست؛ هرگز اجازه دستیابی به سلاح هسته‌ای را نخواهم داد «آن‌ها قلدر خاورمیانه بودند، اما دیگر قلدر نیستند.» او افزود: «از نخستین روزی که وارد عرصه سیاست شدم، موضع من تغییر نکرده است؛ هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای…</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/23808" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7a774734.mp4?token=IHqF7pWZ7yc5IqNBFekwVwJr8K1w16VQ2w3Cxa7-SdMBIZ88uyofGyBcZC8degfdmmXKv2gmBBpUV8U4lpNZQoFlTo0iFZueRgFFR2-vzq7XHGwUVAvwahlHC3hmTpPkWIGnYmdVUdMNPgym31QuL9g3hM15fLa-AjPcdAJ4H5dz4dcXSd9xyhwhIQVoTrVAWtjo5ZReDiBwYb7wiVCRl8e_loSk7Gx2fecbM7n1zIL50XJW_nBctS4LK4PqzD-18F-AYLPToaYYh_FXQYeCIzqJ702DwuksF7lwfGoRfA6g5gUUdmGFsNzeatTVuIo2Uc2sse0VfhoVK_U_mVeIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7a774734.mp4?token=IHqF7pWZ7yc5IqNBFekwVwJr8K1w16VQ2w3Cxa7-SdMBIZ88uyofGyBcZC8degfdmmXKv2gmBBpUV8U4lpNZQoFlTo0iFZueRgFFR2-vzq7XHGwUVAvwahlHC3hmTpPkWIGnYmdVUdMNPgym31QuL9g3hM15fLa-AjPcdAJ4H5dz4dcXSd9xyhwhIQVoTrVAWtjo5ZReDiBwYb7wiVCRl8e_loSk7Gx2fecbM7n1zIL50XJW_nBctS4LK4PqzD-18F-AYLPToaYYh_FXQYeCIzqJ702DwuksF7lwfGoRfA6g5gUUdmGFsNzeatTVuIo2Uc2sse0VfhoVK_U_mVeIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران دیگر قلدر خاورمیانه نیست؛ هرگز اجازه دستیابی به سلاح هسته‌ای را نخواهم داد
«آن‌ها قلدر خاورمیانه بودند، اما دیگر قلدر نیستند.»
او افزود: «از نخستین روزی که وارد عرصه سیاست شدم، موضع من تغییر نکرده است؛ هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/23807" target="_blank">📅 18:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23806">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac051de59.mp4?token=YxlrliVRU04Qt0XZENfjV54cHzblwiu6TtaTW5ljQW3Jcezgb1fGPl7aly_CNCnZjdCbrG6DLSv6RUnL6C8KVcdLWFTTT3CjUlkGXEqOee6FDgEgsF3Gg7Z4UW_cnNEj2YX_eVz5g-LWsKn8H5u0kmLYrHabGilcfeLAzN6RqcC9AXjlkgI_zZpeBU6sFOfcUQpt2-W0-Rvc6zfTO0vwupoJYnS94x3FbnHFYRhb3P_zp34PfXRYoc24HClJAQefjB_BjlsaSNM_eFcd_eHa_gKgFHS8t5hN3N4zCPC8jnjyjMIIvSHZlz9lGp8wUB_KCvGFM6sSaExUeRepB4145Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac051de59.mp4?token=YxlrliVRU04Qt0XZENfjV54cHzblwiu6TtaTW5ljQW3Jcezgb1fGPl7aly_CNCnZjdCbrG6DLSv6RUnL6C8KVcdLWFTTT3CjUlkGXEqOee6FDgEgsF3Gg7Z4UW_cnNEj2YX_eVz5g-LWsKn8H5u0kmLYrHabGilcfeLAzN6RqcC9AXjlkgI_zZpeBU6sFOfcUQpt2-W0-Rvc6zfTO0vwupoJYnS94x3FbnHFYRhb3P_zp34PfXRYoc24HClJAQefjB_BjlsaSNM_eFcd_eHa_gKgFHS8t5hN3N4zCPC8jnjyjMIIvSHZlz9lGp8wUB_KCvGFM6sSaExUeRepB4145Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«با افتخار می‌توانم به شما بگویم که
آمریکا بازگشته است
و کشور ما امروز از همیشه قدرتمندتر است. اقتصاد ما مورد حسادت جهان است.
ارتش ما قدرتمندترین ارتش روی زمین است.
فناوری ما رقیبی ندارد و ما تقریباً در همه زمینه‌ها
پیشتاز هستیم
.»
@WarRoom</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/23806" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شاهزاده رضا پهلوی برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/23805" target="_blank">📅 17:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تلگراف : ترامپ در حال بررسی گزینه‌های مختلف درباره ایرانه؛ از مذاکره و  تشدید حملات و افزایش فشار اقتصادی گرفته تا حتی «منفجر کردن کل حاکمان ایران»!
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23804" target="_blank">📅 17:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23803">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">با پشتیبانی هواپیماهای سوخت‌رسان BORA74، BORA84 و BORA94، مجموعاً ۱۲ فروند جنگنده F-16C از بال ۱۳۸ جنگنده (138th Fighter Wing) با کد دم «OK»، امروز پایگاه هوایی اشپانگدالم (ETAD) در آلمان را ترک کردند و به سمت خاورمیانه حرکت کردند. @WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/23803" target="_blank">📅 17:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
چند کشور که در تلاش برای میانجی‌گری میان آمریکا و ایران هستند، با هر دو طرف در تماس‌اند تا
یک دیدار در سطح بالا بین آمریکا و ایران
برگزار شود. این کشورها هنوز معرفی نشده‌اند و جزئیات بیشتری درباره این دیدار احتمالی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/23802" target="_blank">📅 17:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال ۱۴ اسرائیل : پیش از سخنرانی رئیس‌جمهور ایران در سازمان ملل، کانال‌های رسانه‌ای سپاه پاسداران ویدئویی مفهومی و ساخته‌شده با هوش مصنوعی منتشر کردند که تصویری از نخستین آزمایش بمب هسته‌ای «واقعیه گرم» ایران را به نمایش می‌گذارد. @WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/23801" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23800">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">هم اکنون پس از شرکتهای ترکیه و عراق، شرکت های هواپیمایی امارات و قطر نیز پرواز های خود به ایران را متوقف کردند. @WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/23800" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رسانه های رژیم : «رئیس‌جمهور پزشکیان دقایقی پیش، پس از توقفی کوتاه خود ، الجزایر را به مقصد نیویورک ترک کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/23799" target="_blank">📅 17:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رئیس‌جمهور ترامپ هنگام ورود به مقر سازمان ملل:تعجب می‌کنم که سی‌ان‌ان اینجا حضور دارد و اخبار مربوط به مرا پوشش می‌دهد. شما نباید اینجا باشید. شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مشغول پوشش دادن اخبار من باشید. @WarRoom</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/23798" target="_blank">📅 17:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هم اکنون پس از شرکتهای ترکیه و عراق، شرکت های هواپیمایی امارات و قطر نیز پرواز های خود به ایران را متوقف کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/23797" target="_blank">📅 17:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/066e31f4eb.mp4?token=qoo-IFt_S4O_5Ezvkcps5Ta2R3cuW82IUwSrw5aX0uFG5_m8CeBoGa5QmQR6iX_MAhvU3ABav4sEDObX_UYG-HyZtOhEhHi-jQJUurzD52gfi0RcXf1rB0jb8qvl9QookCkZRKCoFX8dRNinTJNbmeXHkVsJZ9-PK_d0UCCrQX_sy0jCTEHnZsySqYVPPt-oOl5VXMK3YIkw56bJO_KHo2u7ToGJiXMRRdpnXaOPhH3kiKwaoVikuPS1VD2S2sfgsT2x2qVW_Fy6VVLJx3XpYtdAgvDUCDDd-TrWKxfLcW1Thmhpo1xUnaMtvzpqA-qddFvXHkNXLRQClTCFcwb7Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/066e31f4eb.mp4?token=qoo-IFt_S4O_5Ezvkcps5Ta2R3cuW82IUwSrw5aX0uFG5_m8CeBoGa5QmQR6iX_MAhvU3ABav4sEDObX_UYG-HyZtOhEhHi-jQJUurzD52gfi0RcXf1rB0jb8qvl9QookCkZRKCoFX8dRNinTJNbmeXHkVsJZ9-PK_d0UCCrQX_sy0jCTEHnZsySqYVPPt-oOl5VXMK3YIkw56bJO_KHo2u7ToGJiXMRRdpnXaOPhH3kiKwaoVikuPS1VD2S2sfgsT2x2qVW_Fy6VVLJx3XpYtdAgvDUCDDd-TrWKxfLcW1Thmhpo1xUnaMtvzpqA-qddFvXHkNXLRQClTCFcwb7Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ هنگام ورود به مقر سازمان ملل:تعجب می‌کنم که سی‌ان‌ان اینجا حضور دارد و اخبار مربوط به مرا پوشش می‌دهد. شما نباید اینجا باشید.
شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مشغول پوشش دادن اخبار من باشید.
@WarRoom</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/23796" target="_blank">📅 17:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23795">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تنگه صدای سلامی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/23795" target="_blank">📅 17:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyx9JAcwy85BdGoU8xqOBWqi0ErGW9k8mC2a_c6RyHZFzQCnFApUNbxVwaRjJ3gQ2NHrTaDqjB120QEO94x5fAz-qzmQ2mUMOnyrAdL2D5c8eW8tr-mLiLQkx83ghsu0c4VciblWQXZ92hByO58z1TGC93fG55dytKc3AsQK4JUra0M427h8kb8kRxaEjQ4AprkcWJNzeJPQA6PexYB9ZZvvl9TP8lRtYTLfQqh9IqKgbdlic8n6XDZZS3t2QnuvRY-iR7ch2yuJinyN5J0oYyEsjwgxtHqFcRlJvQYMDljsLsg4ELML4fUVG4FW594d8TrnI981jc2sKpwbUM5faw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">​ جدول سخنرانیهای سازمان ملل مشخص شد
بر اساس جدول رسمی منتشرشده از سوی مجمع عمومی سازمان ملل متحد (نشست هشتاد و یکم)، دونالد ترامپ امروز به عنوان دومین سخنران در صحن مجمع عمومی حاضر خواهد شد.
پس از گزارش دبیرکل و سخنرانی رئیس مجمع و رئیس‌جمهور برزیل، نوبت به رئیس‌جمهور آمریکا می‌رسد.
زمان تقریبی سخنرانی ترامپ:
به وقت تهران: حدود ساعت ۱۷:۱۵ الی ۱۷:۴۵
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23794" target="_blank">📅 17:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عراقچی‌ هم وارد سالن شد تا سخنان ترامپ را بشنود
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/23793" target="_blank">📅 17:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ وارد سازمان ملل شد
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23792" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">با پشتیبانی هواپیماهای سوخت‌رسان BORA74، BORA84 و BORA94، مجموعاً ۱۲ فروند جنگنده F-16C از بال ۱۳۸ جنگنده (138th Fighter Wing) با کد دم «OK»، امروز پایگاه هوایی اشپانگدالم (ETAD) در آلمان را ترک کردند و به سمت خاورمیانه حرکت کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23791" target="_blank">📅 16:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23790">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تنگه دعوا شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23790" target="_blank">📅 16:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران، از وزارت امور خارجه آمریکا درخواست کرد تا در جریان حضورش در نیویورک برای شرکت در مجمع عمومی سازمان ملل، یک تیم حفاظت امنیتی آمریکایی در اختیار او قرار گیرد. بر اساس گزارش‌های رسیده از آمریکا، پس از بررسی تهدیدهای موجود علیه وی، تیمی از «سرویس امنیت دیپلماتیک» مسئولیت حفاظت از او را بر عهده خواهد گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23789" target="_blank">📅 15:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe43fd0fd0.mp4?token=ZmOwLllFHXq_i9AoUy9uzKRb8WywTcBTF3eyUH8fEaKrY-BOi7FmOzrZNap322ZgVTpcVOYmxApI9-htY5Lfwh3W4yfO5XfzAvb0TU9FXiiw9sGXBoBZyPBUAHoAcCM80G5Zk_hldN8dEvB3KEVg2ze6iLyI2sdD_BmPZ5jklhMvG3gOI_Xnx06ynvGIf9lb5XERRwuUtLdiPznq_klp9EzaRV0MzvjDyv4u88NkC4NB7b-2GQMEgbH9aH_3sIJ6wXOl1ZGTehk6-cCr53Nvt-aWNB9JzCUz5F8y-mN8xIN-4rQVgQZAEil6aSXq-nbPuNTQvPwV287t86774y_ZXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe43fd0fd0.mp4?token=ZmOwLllFHXq_i9AoUy9uzKRb8WywTcBTF3eyUH8fEaKrY-BOi7FmOzrZNap322ZgVTpcVOYmxApI9-htY5Lfwh3W4yfO5XfzAvb0TU9FXiiw9sGXBoBZyPBUAHoAcCM80G5Zk_hldN8dEvB3KEVg2ze6iLyI2sdD_BmPZ5jklhMvG3gOI_Xnx06ynvGIf9lb5XERRwuUtLdiPznq_klp9EzaRV0MzvjDyv4u88NkC4NB7b-2GQMEgbH9aH_3sIJ6wXOl1ZGTehk6-cCr53Nvt-aWNB9JzCUz5F8y-mN8xIN-4rQVgQZAEil6aSXq-nbPuNTQvPwV287t86774y_ZXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، درباره ایران:
«رئیس‌جمهور ترامپ آماده دیدار با
مسعود پزشکیان یا هر فرد دیگری
است. اما اینکه چنین دیداری به نتیجه‌ای سازنده منجر شود، مشخص نیست؛ زیرا
تصمیم‌گیرنده نهایی در ایران رهبر جمهوری اسلامی است
و رهبر جمهوری اسلامی یک روحانی شیعه رادیکال است.»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23788" target="_blank">📅 15:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb2d25d09.mp4?token=YIJpkJYkR9bJk9bo_eS7LrdD0kLh5hKz9Yj6udPBkaAeZf8ffptjoOCnGt_zuYDxruhLKenE9aCgD0-TzedT_ytV4fVRLzbC_lIi38agynTumP5LUgA2Y7aiBNOzcjwZxpADPP-k0MzYhYD9i3hkyKxszMHe1r5qWI1sRg8NFzEm_z6SGoIF4jwz4Bj7hp6Rn6eo8p8S2V0fqF41v8D6hvoOlb-_ktY5bZj5rSO4zoTH6UmiN4NQXSSPIQGmxQ3nI4oNZLuMiI_UpNHimfS1thnibxsyjmLcJ22hIjRlzenwTIM2rzPr-SZT5Ke97Pf-MiO3Aiv70Sc5yK6kU3WfBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb2d25d09.mp4?token=YIJpkJYkR9bJk9bo_eS7LrdD0kLh5hKz9Yj6udPBkaAeZf8ffptjoOCnGt_zuYDxruhLKenE9aCgD0-TzedT_ytV4fVRLzbC_lIi38agynTumP5LUgA2Y7aiBNOzcjwZxpADPP-k0MzYhYD9i3hkyKxszMHe1r5qWI1sRg8NFzEm_z6SGoIF4jwz4Bj7hp6Rn6eo8p8S2V0fqF41v8D6hvoOlb-_ktY5bZj5rSO4zoTH6UmiN4NQXSSPIQGmxQ3nI4oNZLuMiI_UpNHimfS1thnibxsyjmLcJ22hIjRlzenwTIM2rzPr-SZT5Ke97Pf-MiO3Aiv70Sc5yK6kU3WfBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، درباره ایران:
«تصور کنید کره شمالی در خاورمیانه شکل بگیرد؛ این برای جهان فاجعه‌بار خواهد بود. در آن صورت، قیمت گازوئیل که امروز مثلاً ۶ دلار است، ممکن بود
سه برابر
شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23787" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2875ab9dd.mp4?token=Myzhe6MaIxockY4XYOIjFuXKQKqsxUsxpfodRSxG3ZRPDO6seDiTKZGA2WFXvPQoITdRDqUnnXt0_DwiD7ZzAg8OxWjmylf4lSJ2KDd0j3FhjDYzvwihzLQyGYbErzWDoCrDilWMtG6v-c4zFMRdHDxCK3no4JyJz_zsijbEOstvICsNrj03ffaf18muOTm_G7NrkbEE4k2icP-s54UsLC_8hBnBAZdv96Ne9ZSaTMtgU8lJn_YEEE1vozj9HBWM3f7uK-uivwPfvdHiVQrQSHxjpUnUqZ4pYjGvtlZuzG1NOJvOojenPPpA39cxYWx40y3RDhkBF5qnaApBT5-BRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2875ab9dd.mp4?token=Myzhe6MaIxockY4XYOIjFuXKQKqsxUsxpfodRSxG3ZRPDO6seDiTKZGA2WFXvPQoITdRDqUnnXt0_DwiD7ZzAg8OxWjmylf4lSJ2KDd0j3FhjDYzvwihzLQyGYbErzWDoCrDilWMtG6v-c4zFMRdHDxCK3no4JyJz_zsijbEOstvICsNrj03ffaf18muOTm_G7NrkbEE4k2icP-s54UsLC_8hBnBAZdv96Ne9ZSaTMtgU8lJn_YEEE1vozj9HBWM3f7uK-uivwPfvdHiVQrQSHxjpUnUqZ4pYjGvtlZuzG1NOJvOojenPPpA39cxYWx40y3RDhkBF5qnaApBT5-BRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو: ما برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم ولی فکر نمی‌کنم هیچ جلسه‌ای بین ترامپ و رئیس‌جمهور ایران برنامه‌ریزی شده باشد @WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/23786" target="_blank">📅 15:18 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
