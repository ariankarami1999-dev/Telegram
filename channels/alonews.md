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
<img src="https://cdn4.telesco.pe/file/qugs9vHqmldfcp9S95cqbvorrRk4umsmAm_OzXz444eBmQ-LWpEM2J54kyPZnniTfb84CN5mbw1Vd9QuZNcUV-IkwIpvQlatKJXAmrTEL_L6h4tyqRQZvinchGJNk9ZQ0h3AprpyKPACcJeOKdQhC5RDlJPSfggPkAEy4MBSUDMgFheCzAr_z9d6x5L4E91YjRu1D8VqfwmL9pIHGHc2I7QyK4nXCvQEvll8qpGQfmVr_8jHsrEgrLWKkp4UbZFSewyeO-tbVbTdDbc0PmyWBeUf4LIKDOpbSSE-4iXNGsSQTKgoZx1cMfr1S7bSQfeeDiCp2HKe287XC6X_g-TelQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 921K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 14:30:57</div>
<hr>

<div class="tg-post" id="msg-147039">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پزشکیان: برای ارتقای کارآمدی و سرعت بخشیدن به اجرای تصمیمات بریکس، تدابیری همچون مقاومت در برابر تحریم‌های یک‌جانبه، تبدیل رقابت‌ها به همکاری و استقرار دبیرخانه دائمی ضروری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/147039" target="_blank">📅 14:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147038">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB1Y7b4Oc5G9wz9N1kYvlC3EUV-ZFvfGvQ3maww4otTe34V6mh1XI81EaV_99DLicaLOAxsxHhGfB4VY_XnXL4G6zKux3kBvThHSlrae21QJmti3rg60-UAFPFT8snm9XOszzMpw8pi0ZIs2In6Lh3yMVPIYaCUGmMqm3d0JRBSJtbLh7sSvUy1ynhifMsedwptyrh6qHXVrG3mgn6096jRDIOMGdleNy1iPIZsx6Te87ylIsXEM6WzwExmIOaKuGEixo4hpugrSJt-sCKNjomnog-VGf1jHc5X9P9wf2McARaaQ2x8Pe3CKc5uuq0nsPq0QDxUogzz4eJT2tch4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این سوپر النینویی که الان شاهديم و البته هنوز به اوج خود نرسیده تا بحال رخ نداده بود و البته شاید تا صدها سال دیگه هم به این حد نرسه، شاید باورتون نشه تو ۷۵ سال گذشته فقط سه بار سوپر النينو رخ داده که هر سه تاشونم در برابر این سوپر النينو عددی نیستن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/147038" target="_blank">📅 14:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147037">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=dJ9vV9qlhj2Eb1SzEtGzarX1G1ENTgW59H2FXIRpdkwh5htioMigsRLlViKj6UVh-t50erHRJnFyAInvAZIEG6ZYB_h_8oxExA4jmcRm3kUklT_ZMdAC8IQSewa2R4LxQ69BYryIE7pV1ZeKxP3H3nOfiMJJ_41npecHYlbqtK4T2K4-ikuggP5zLzqzH2ptJQ0s830hIRIJ5lvQIqzIWIYNZcFs1qQ6AZeCv1bbyuhmxsMtE6fIL04qQkKwrgBZYi3iiMWjeWsJzIzoSSuj8P8rs6Q8d-3NEcbUASUdHKGFAo6nSecXUcFq5u_A_eC_UmXWszb8iVZwAL4zhYvnYJ3qb0xYepbCVnRp0PF7vd_siVsHLoLpv30xMm0zNYygbbF1erT4SgAUYASRWq0q1a_F7fD5nvCfBR-ZKynjDqRYi7zcVkRtYTrB3m36-waAdIAY2iuagVPHyQy3-yrhwBmo1LZPGpZKugc65vihNB4pQee4PH0gBvE0aUKyFhOhJfYI-gMmCsJiutNOnFLDIrfj8jS-WXlfN03X1EoRrYhuw3RYKExkfUCOPIIzks8-DQnqmsk76QMv3GB9r1mX0rECStba0f8z7w0SXSmfeKaKecsCVFr6i8v9Q3Vnrrdjp2dUB9WpCyTrGBBJm819ZbEpCCbUzGjbH4yGdjHzSAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=dJ9vV9qlhj2Eb1SzEtGzarX1G1ENTgW59H2FXIRpdkwh5htioMigsRLlViKj6UVh-t50erHRJnFyAInvAZIEG6ZYB_h_8oxExA4jmcRm3kUklT_ZMdAC8IQSewa2R4LxQ69BYryIE7pV1ZeKxP3H3nOfiMJJ_41npecHYlbqtK4T2K4-ikuggP5zLzqzH2ptJQ0s830hIRIJ5lvQIqzIWIYNZcFs1qQ6AZeCv1bbyuhmxsMtE6fIL04qQkKwrgBZYi3iiMWjeWsJzIzoSSuj8P8rs6Q8d-3NEcbUASUdHKGFAo6nSecXUcFq5u_A_eC_UmXWszb8iVZwAL4zhYvnYJ3qb0xYepbCVnRp0PF7vd_siVsHLoLpv30xMm0zNYygbbF1erT4SgAUYASRWq0q1a_F7fD5nvCfBR-ZKynjDqRYi7zcVkRtYTrB3m36-waAdIAY2iuagVPHyQy3-yrhwBmo1LZPGpZKugc65vihNB4pQee4PH0gBvE0aUKyFhOhJfYI-gMmCsJiutNOnFLDIrfj8jS-WXlfN03X1EoRrYhuw3RYKExkfUCOPIIzks8-DQnqmsk76QMv3GB9r1mX0rECStba0f8z7w0SXSmfeKaKecsCVFr6i8v9Q3Vnrrdjp2dUB9WpCyTrGBBJm819ZbEpCCbUzGjbH4yGdjHzSAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما کنترل بسیار قوی‌ای بر تنگه هرمز داریم. هیچ‌کس فکر نمی‌کرد که این اتفاق بیفتد.
🔴
به طور متوسط، ما روزانه حدود 25 شناور را توقیف می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/147037" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147036">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
گزارشگر: اگر بخواهید به مردم ایرلند که امروز در حال اعتراض هستند، چه بگویید؟ آن‌ها معترض هستند زیرا نمی‌خواهند شما به ایرلند بیایید.
🔴
ترامپ: من نمی‌دانستم که اعتراضی وجود دارد. من هیچ اعتراضی ندیده‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/147036" target="_blank">📅 14:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147035">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
چین ریاست سال ۲۰۲۷ بریکس را بر عهده می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/147035" target="_blank">📅 14:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147034">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ : حوثی‌ها «نمی‌خواهند با ما بجنگند» و افزود که آنها با آمریکا تماس گرفته و خواستار آن شده‌اند که واشنگتن در این درگیری مداخله نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/147034" target="_blank">📅 14:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147033">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: فکر می‌کنم ایران موشک‌هایی دارد که می‌تواند شهرهای اروپایی را هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/147033" target="_blank">📅 14:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147032">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
رئیس‌جمهور چین: جنگ در خاورمیانه در خدمت منافع مشترک کشورهای عضو بریکس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/147032" target="_blank">📅 13:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147031">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=MrYkCbjMYpREMFWhgGlDo2SaZVmDBRiTDUYOkXUK1qIUS_NTja9Pry0HtJYSNQCj3Z-Ks9ZkYEAKeMnrVkSLkW2m8CObtiMTt8E2eer4uP3zGDFDmbZPLagszi92HS5coX4r9edfs9y4DOHYzxhNrrp8CNWTaRk8-sL7eHL51ZDTbBWy8IMs20NmapydBJ7g9qXl-ChvnHJCM5WJk4jRfBMDXX-IRCyF8xnFzkM0PAPt7LMaytNMz8jOdj_apSrSc_hj9ywOLOwyfZ-bS8I6mtHopE_SgqNT7ufz-lPqGbcvmgPjqyX2y7U6SfB_WEJx8rSX1Qv9ekT3C-uXhApJ8kR1ZHb41mskkpCudpdJptsBZMvF1UqbKr5Zu_ouJv18rsdRe7ri_EPpNJbQZOjfYA8QxSr1QMHD9wuPY7LtKdv-OKkKkT-tZH_4L2M-ZOpiP-jZhkUuZKd1wY1g9dAejCDuULjUv2jjHCmx_xdan3qDSIQg_72I58o48Y249ROpzDeRQvGpnUEUgA234_r9dQ1cD1g-JfVBHM4R3ilkGkILB76O1D1lnNlh2aiyab5TGyilgckHX49Lq1jFAPXgqiPd-9HnAndJUlWlnLPWtIg-G_tlj7oVBDTdV7SOGFCS8fhJ4C34j6SHyFkpJ8MaHOnwMMwuNw7aWHf9bNl2fMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=MrYkCbjMYpREMFWhgGlDo2SaZVmDBRiTDUYOkXUK1qIUS_NTja9Pry0HtJYSNQCj3Z-Ks9ZkYEAKeMnrVkSLkW2m8CObtiMTt8E2eer4uP3zGDFDmbZPLagszi92HS5coX4r9edfs9y4DOHYzxhNrrp8CNWTaRk8-sL7eHL51ZDTbBWy8IMs20NmapydBJ7g9qXl-ChvnHJCM5WJk4jRfBMDXX-IRCyF8xnFzkM0PAPt7LMaytNMz8jOdj_apSrSc_hj9ywOLOwyfZ-bS8I6mtHopE_SgqNT7ufz-lPqGbcvmgPjqyX2y7U6SfB_WEJx8rSX1Qv9ekT3C-uXhApJ8kR1ZHb41mskkpCudpdJptsBZMvF1UqbKr5Zu_ouJv18rsdRe7ri_EPpNJbQZOjfYA8QxSr1QMHD9wuPY7LtKdv-OKkKkT-tZH_4L2M-ZOpiP-jZhkUuZKd1wY1g9dAejCDuULjUv2jjHCmx_xdan3qDSIQg_72I58o48Y249ROpzDeRQvGpnUEUgA234_r9dQ1cD1g-JfVBHM4R3ilkGkILB76O1D1lnNlh2aiyab5TGyilgckHX49Lq1jFAPXgqiPd-9HnAndJUlWlnLPWtIg-G_tlj7oVBDTdV7SOGFCS8fhJ4C34j6SHyFkpJ8MaHOnwMMwuNw7aWHf9bNl2fMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران: ما با قدرت بسیار زیادی تنگه هرمز را کنترل می‌کنیم. هیچ‌کس انتظار نداشت چنین اتفاقی بیفتد.
🔴
ما به‌طور متوسط روزانه ۲۵ قایق را از بین می‌بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/147031" target="_blank">📅 13:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147030">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb11451447.mp4?token=govLm3oZJnSySDvoVSL85I2hesZEPl-3L3rdinHkR1Vs0uRFJaHhbB-RrZIr4dWBJuy8u8998VvCcHEh0pBItP4ZWw659xdnN1ZcVSEaWHGiRcXq59hTBn4t9rEqPRaiNZ54tRSmy3xCTEPMScm4WdJyPjamgN6_Zz7O7QyEhuK-mrEP24K0i5sTBj9zKdejKZ0gMzdxqMZKTT7qmJJiDr2da0Yf_D8Rlbwhjg29Gos9cd4hJbBir6bYhytubchhmSbKSmJOaRM7Z50zugSQI1GxVGZYFY4ebZanrWdCNhhap05tT_p2HtJ364PEQrwS-VG1zvJ6INPVCk9PvZrLkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb11451447.mp4?token=govLm3oZJnSySDvoVSL85I2hesZEPl-3L3rdinHkR1Vs0uRFJaHhbB-RrZIr4dWBJuy8u8998VvCcHEh0pBItP4ZWw659xdnN1ZcVSEaWHGiRcXq59hTBn4t9rEqPRaiNZ54tRSmy3xCTEPMScm4WdJyPjamgN6_Zz7O7QyEhuK-mrEP24K0i5sTBj9zKdejKZ0gMzdxqMZKTT7qmJJiDr2da0Yf_D8Rlbwhjg29Gos9cd4hJbBir6bYhytubchhmSbKSmJOaRM7Z50zugSQI1GxVGZYFY4ebZanrWdCNhhap05tT_p2HtJ364PEQrwS-VG1zvJ6INPVCk9PvZrLkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره غزه: اگر به غزه نگاه کنید، در حال حاضر روابط خوب زیادی در غزه در حال شکل‌گیری است.
🔴
این واقعاً شگفت‌انگیز بوده است. فکر می‌کنم ما کار بسیار خوبی انجام داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/147030" target="_blank">📅 13:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147029">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=J1UoLUxqeQTRTeMRNplhzlIyxCgY7x9ScjpLLVVBXUQn4wG6a9PqFrSH62dAS8r39BUGQ0oVTHwjFOqtpameaehuRbPwcZ_IVJWFBEUgg_O5KXq9vW632XSdJzg8hvgkjdPFP0qdeqZ9cuoYT38bJ5p2qFmC7t7KNHS2RoF0NtQxZkwOtwzhQWt-ctPF19e8dB9Tb5-UmlHg9vTUNNH4rUSTBdw7kGfg0TLIif2jFJQD0AC4gj-34rGcv1bu9KfJaLC0WubTBAw0BcwFngLlDxAFOj8lNlCiFbgXwwg3KKscVnDuC2x44wtqJ_bnOAfMj1IN-BJOMIsqEbYTUFnoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=J1UoLUxqeQTRTeMRNplhzlIyxCgY7x9ScjpLLVVBXUQn4wG6a9PqFrSH62dAS8r39BUGQ0oVTHwjFOqtpameaehuRbPwcZ_IVJWFBEUgg_O5KXq9vW632XSdJzg8hvgkjdPFP0qdeqZ9cuoYT38bJ5p2qFmC7t7KNHS2RoF0NtQxZkwOtwzhQWt-ctPF19e8dB9Tb5-UmlHg9vTUNNH4rUSTBdw7kGfg0TLIif2jFJQD0AC4gj-34rGcv1bu9KfJaLC0WubTBAw0BcwFngLlDxAFOj8lNlCiFbgXwwg3KKscVnDuC2x44wtqJ_bnOAfMj1IN-BJOMIsqEbYTUFnoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی شهردار نیویورک: قربانی اصلی حمله ۱۱ سپتامبر عمه‌ من بود که بعد از اون اتفاق نمی‌تونست با امنیت از مترو استفاده کنه چون حجاب داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/147029" target="_blank">📅 13:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: «کانادا بسیار مشتاق است که به توافق برسد؛ درست مانند ایران که بسیار مشتاق است به توافق برسد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/147028" target="_blank">📅 13:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=NxXSIXK4whiqsXVAO412PkCriS1_P0Felx8ZUcq3_cQK70py7VDgztxMI3zpc94iCczy464dbOseRkUMgjTgOaNUBzGgUgDNOStlwFd27q6_ild-tCM29-DrjIYdBcAXUWarM68JLclz3MeQ3qhVHTEWgUzcRXx33OHmIXBFhQhtXBw8ektMpgEA-Mz35YxNO5QPYr0v_I-WUZb7UqdMw4_vXLN_kZPTArXXyWbWT7MvZYsgXYZ3uGWhka2CNUgrPXRxgImLnUhJBN4MCqpLxNzTfl8d0-cVVF5FoU3_QFEGX62lQPrz5z0QeuGJ2Ocwz3zh_BbX0q07_33k7p6_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=NxXSIXK4whiqsXVAO412PkCriS1_P0Felx8ZUcq3_cQK70py7VDgztxMI3zpc94iCczy464dbOseRkUMgjTgOaNUBzGgUgDNOStlwFd27q6_ild-tCM29-DrjIYdBcAXUWarM68JLclz3MeQ3qhVHTEWgUzcRXx33OHmIXBFhQhtXBw8ektMpgEA-Mz35YxNO5QPYr0v_I-WUZb7UqdMw4_vXLN_kZPTArXXyWbWT7MvZYsgXYZ3uGWhka2CNUgrPXRxgImLnUhJBN4MCqpLxNzTfl8d0-cVVF5FoU3_QFEGX62lQPrz5z0QeuGJ2Ocwz3zh_BbX0q07_33k7p6_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا ایران مسئول حمله به خط لوله نفتی شرق-غرب عربستان است؟
🔴
ترامپ: فکر می‌کنم آنها هستند، احتمالاً آنها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/147027" target="_blank">📅 13:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996f54b8aa.mp4?token=I_jZWxGqmAez-hBVUMz0RkQGzWNFngGzQtN6nUizHs9BXja6ZaydxwAcc8OkAR61MH-Eh04NoRUv0pzNnkZQJCYj_mQIYsmvL01T7XrTCPwuLUgO55IiTd9Vm6AaenWWAgQPqjjGrwjGU1axR1MQD-3CyDKEuowQaGich8ZB1w1PKLKcJWtU_JZ9bH1_Ijw4csMTx2W1AnHxLfE4OLippUwXW6gatvlUQuGfME5BpoOaUQmm5AAu2zbS9j3IFAWWF67qMOfzPJ8BmTExOdnvGK0v-kRhOZGpHYSieTwpR5TNGp69l5oqe7ezTe1lxAHNy98VMchg01OfLJ1lUIw_4mtZ0mCnXupTolhQvkPlW7q_yGLDsmnaipF03vC-TSuS5btyWIwsayq3hilgcrex-GrCOBlG5LVVenK3csMEywmZQqbnT6N-JlxbVJyOqqJ_1Alm1UuOJqPbKGZbv-4khFrLl-1jPxtQo5YgItYhAmpkkh-l-gqztmYVBVidg2Ftl2WQcBP41YVxN-9xhS4c5zbJ7-RRZs-I-wSjAcE1WH096vbqccD7hGFqi16HxpvlmoV-180XVUIFfp4FPb2GsNlLCQMOxU4qjWABoKCYNi03eK4a-w1UBxfrGfkTKvAL8avI29z-dJzpzqqwodeeuIPOvgB_lQHymaS-exkRtz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996f54b8aa.mp4?token=I_jZWxGqmAez-hBVUMz0RkQGzWNFngGzQtN6nUizHs9BXja6ZaydxwAcc8OkAR61MH-Eh04NoRUv0pzNnkZQJCYj_mQIYsmvL01T7XrTCPwuLUgO55IiTd9Vm6AaenWWAgQPqjjGrwjGU1axR1MQD-3CyDKEuowQaGich8ZB1w1PKLKcJWtU_JZ9bH1_Ijw4csMTx2W1AnHxLfE4OLippUwXW6gatvlUQuGfME5BpoOaUQmm5AAu2zbS9j3IFAWWF67qMOfzPJ8BmTExOdnvGK0v-kRhOZGpHYSieTwpR5TNGp69l5oqe7ezTe1lxAHNy98VMchg01OfLJ1lUIw_4mtZ0mCnXupTolhQvkPlW7q_yGLDsmnaipF03vC-TSuS5btyWIwsayq3hilgcrex-GrCOBlG5LVVenK3csMEywmZQqbnT6N-JlxbVJyOqqJ_1Alm1UuOJqPbKGZbv-4khFrLl-1jPxtQo5YgItYhAmpkkh-l-gqztmYVBVidg2Ftl2WQcBP41YVxN-9xhS4c5zbJ7-RRZs-I-wSjAcE1WH096vbqccD7hGFqi16HxpvlmoV-180XVUIFfp4FPb2GsNlLCQMOxU4qjWABoKCYNi03eK4a-w1UBxfrGfkTKvAL8avI29z-dJzpzqqwodeeuIPOvgB_lQHymaS-exkRtz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «ایرلندی‌ها اکنون برای سوخت گرمایشی منازل ۴۰ درصد بیشتر از قبل از جنگ پرداخت می‌کنند. پیام شما چیست؟»
🔴
ترامپ: «وقتی دریای شمال را باز کنند، قیمت‌های شما به‌شدت کاهش خواهد یافت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/147026" target="_blank">📅 13:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
هر یک دلار به 237,500 تومان رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/147025" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147023">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fooHXrLVPWkUoWD-cTkmz-_QO83u7f57rET5YSLbgi3nU3oR733LtXbkNm0MEubIE-Bd-LziOnDCD-hgwrBle8WeYTdNG_DOBu5qqxVXF_Res2ztSzjWNqJ60HLvIuHQEw8fuqa5kPO5Aa7G2C2JuFsjxodmSU76_YwsTg6LCVmy91sLHIPzzHH-xNg04z2J-G3BIWapwuIeTP-40w9_5IQ-YRcCKwqKOZ0J9LSoVQsijmqOw64uBCIfp_W_ka6uUOl0VmTFflz8lUXTqYfzMzkytuxcHOAquDiaN10r0SwdJR3z6Wfv7HNt1dWycf7fLvFq4rGNqZctVLscW86z6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HO2cqhml6YprWFxKTG_cyWC5iNp_10hp6NVwiWeYqCHrv8TchqEIKHArDqVRRe0pS_UBvdBz9PXkRIV2XhyA-4AnpIIU2-2wkqzLAq1d3fQ4FqIDpjl2dCYlRSzKfhU6MDxLChkQpt_fzzd1fe6z8WE7SYzW7tqhHJB55YqinBN6DtBF_VCqu7j2npvARd_umONsBNZs3TfCkCxDAoPeRDuwcM1OfBM99iuGNXi4K1EppoNT2vpoRwpQ80L6fltaNav7XAGzhYTEKdZWsyadOCsQSvpy2c5gq445AvWIqDy77MWtuWfDwZ_ssdY9zmkt_Iivm3HKRmA_Ymy967vwjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک تانکر نفتی متعلق به چین که در تنگه هرمز حضور داشت، تلاش کرد تا از این تنگه از سمت ایران عبور کند، اما سپس مسیر خود را تغییر داد و به عقب بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/147023" target="_blank">📅 13:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147022">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
عراق دومین مرز را هم بست
🔴
مقام‌های عراقی گذرگاه چذابه در استان خوزستان را تا اطلاع ثانوی بستند. پیش از این نیز گذرگاه شلمچه از سوی عراق مسدود شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147022" target="_blank">📅 13:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147021">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزارت امور خارجه کویت حمله پهپادی به خط لوله شرق-غرب عربستان در مناطق ریاض و مدینه را به‌شدت محکوم کرد و گفت پهپادها از خاک عراق به پرواز درآمده‌اند.
🔴
کویت اعلام کرد این حمله موجب تلفات جانی و خسارات مادی شده و آن را نقض جدی حاکمیت عربستان، قوانین بین‌المللی و امنیت تأمین انرژی منطقه دانست.
🔴
این وزارتخانه از عراق خواست مانع استفاده از خاک خود برای انجام حملات بیشتر شود و بر همبستگی کامل کویت با عربستان تأکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147021" target="_blank">📅 13:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147020">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
معاریو: سربازان ذخیره ارتش اسرائیل خواستار گسترش عملیات در داخل سوریه شده‌اند و برخی از آن‌ها ایده اشغال دمشق را مطرح کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/147020" target="_blank">📅 13:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147019">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
خبرنگار: آیا از وضعیت عربستان سعودی و تحولات مربوط به تردد در تنگه نگران هستید؟
🔴
ترامپ: همه‌چیز به‌خوبی پیش خواهد رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147019" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147018">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1D6eNDK0qw4FLVGxYRgIqBuR8uLowfx6_xXaMAUyQvU8yArkP4Afp5oMrWKPvbJ4xwKgLngyvYMGyBideRsjBpvR_TYcg2mXVy-vGPCjpOhPd6ET1ib-HTJ3oa6RZlVoYuC5GXIEzRm8GRAJK1Sx4lfzhDzThBSkkSdM2ob4zBEgiWXZp__DR6nwXz0EppIXBQJCC4ndGQ43jv_5kVQhzkKsz0qacuvH5kQ2K5qW91XXqE8r1D-RoXrbucJo6ymXLkGTntXPxzykgmuplihBAmmWpPoJSx6DQFKvMAsz3z5f3QD1MQeprP65-sAZDkwBbSMStPQV2C0sJ4e1O3tBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکرترکرز: صادرات نفت خام عربستان در چند هفته اخیر روند صعودی داشته و محموله‌های صادراتی از مسیر تنگه هرمز و تحت حفاظت سنتکام ارسال می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147018" target="_blank">📅 12:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147017">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS-helNfaDgDuXeDNgeJq9FVjIUZoujdFem_NUVBnzVJ1DgmJqOeWynFYdMcruEu8jGWSq0Bew4DqMEoiyhjHS2X6fDR3tSpJU4rr2e7oRus8AmqraIoU0KFk3z7fQQ-wEl45XfrSG3IFb8qgwFC5pxB7NIJwvVsOL1435Si_mUTWO35VFsfJiv4ELGV7KkflOYYM3bZedIvhPGPTlkEaMK_0eKYP671ix1d4jlJ2nFDAuD_5KuF3RZGxJW8QH74N1YxJE-zePLvUqb2zOrdcOKXvKDU_3tTtc5UVtjZy_Z5gwSQrmP3lVooY5MOC2RGVZ3kYFTQqMyteAl1bnunqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرود پیاپی هواپیماهای ترابری نظامی آمریکا در استان اربیل در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147017" target="_blank">📅 12:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147016">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6d2568d3.mp4?token=ciy1iioW4NTYtFsdBi3Ip_ihhEsocE6e4UgLyreCvEd6gNnzbSThox_gMVECXR7D1KHEbHzCNs8KHQ5Evt4T-iA_VNk0ge3cfMFbHdyGkyMIYMYrgo_ozCD_Y2OQl3Vm7SCaE2SuzNqMTk6J7Fnm62QqHR3W2y-2XAHMq24Z42VZx9nG_Y1BHnojjtob8FWM0-a5RPiN-rbeMIeYNammRMjGmpc9QH4RFal0SHw86Vs3tBlwYjI_vsKP0oXaxuMXxbd99csyTnTRNC0tE3TR8xJjGVqgDGl_PP6mz3CSB_Bm8L2b6P_Ffw0d9reQLCjEhbtQ79k8sqB1wBd9TKwOa4Zcf755m8FIlUTY2hYFsLDwDBukTeEvjGAS6B5qGad7aQj6tuauWsF33LdZ47rF3mDe0o5-3rTMbv6cH8xDoPkx8VsXc2v7deJE6iaePC6_i5s3yFkacqfvcv9keTmznJm6KZizw91x67MArPoz-UlJjZnZ4oQeXyRyS90LHst9tirjiylUW1GRppaTC4Ty1XkVeUmJB_KTTcF1jds1VJlz2-4v5qMtNHxdHNKe0YXkBUOZFq-Zhl6-kN4RWtMPkoTjfzZS1GpGj7nAiAOIdv8WJSPm6daKh7455QjxtdBe6Ivb2lMA1veowtEvXLZXNpT2BHWgIwsrpyICTeYNk_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6d2568d3.mp4?token=ciy1iioW4NTYtFsdBi3Ip_ihhEsocE6e4UgLyreCvEd6gNnzbSThox_gMVECXR7D1KHEbHzCNs8KHQ5Evt4T-iA_VNk0ge3cfMFbHdyGkyMIYMYrgo_ozCD_Y2OQl3Vm7SCaE2SuzNqMTk6J7Fnm62QqHR3W2y-2XAHMq24Z42VZx9nG_Y1BHnojjtob8FWM0-a5RPiN-rbeMIeYNammRMjGmpc9QH4RFal0SHw86Vs3tBlwYjI_vsKP0oXaxuMXxbd99csyTnTRNC0tE3TR8xJjGVqgDGl_PP6mz3CSB_Bm8L2b6P_Ffw0d9reQLCjEhbtQ79k8sqB1wBd9TKwOa4Zcf755m8FIlUTY2hYFsLDwDBukTeEvjGAS6B5qGad7aQj6tuauWsF33LdZ47rF3mDe0o5-3rTMbv6cH8xDoPkx8VsXc2v7deJE6iaePC6_i5s3yFkacqfvcv9keTmznJm6KZizw91x67MArPoz-UlJjZnZ4oQeXyRyS90LHst9tirjiylUW1GRppaTC4Ty1XkVeUmJB_KTTcF1jds1VJlz2-4v5qMtNHxdHNKe0YXkBUOZFq-Zhl6-kN4RWtMPkoTjfzZS1GpGj7nAiAOIdv8WJSPm6daKh7455QjxtdBe6Ivb2lMA1veowtEvXLZXNpT2BHWgIwsrpyICTeYNk_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کثیف ترین ویدیو وایرال شده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/147016" target="_blank">📅 12:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147014">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b37381aaf.mp4?token=rvrJVftRhCWE91kQS1gU2khN1UDj68-HciDhhp05LMUo5XTAGZMXN17Au0ykZtHSmtb0-BCtjxIOvlU0unSLqctdyADo3Befh3wFUWyuyh0S43lUlfBgAhJtpQnuIlAScsg4whcRX7gjuugBLmIDHsip9p92dtvznFLIu_3ZbXq2MHC_QgPPG14Bu7PwAZT5znCYGiO46LdX1g7qZWZQiaMiCiwjZkhmvvJC9rNH3nG6CQpZwO9lEb6CLdWzYgp-D3fFC1i8TDc1aUWb4xnBBIboPxiXJdXZ_9gpCDsLagA5k8PU_pknZaPQM0tyukeWsA2yf7JUxytV_Z5HmS8vWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b37381aaf.mp4?token=rvrJVftRhCWE91kQS1gU2khN1UDj68-HciDhhp05LMUo5XTAGZMXN17Au0ykZtHSmtb0-BCtjxIOvlU0unSLqctdyADo3Befh3wFUWyuyh0S43lUlfBgAhJtpQnuIlAScsg4whcRX7gjuugBLmIDHsip9p92dtvznFLIu_3ZbXq2MHC_QgPPG14Bu7PwAZT5znCYGiO46LdX1g7qZWZQiaMiCiwjZkhmvvJC9rNH3nG6CQpZwO9lEb6CLdWzYgp-D3fFC1i8TDc1aUWb4xnBBIboPxiXJdXZ_9gpCDsLagA5k8PU_pknZaPQM0tyukeWsA2yf7JUxytV_Z5HmS8vWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی عجیب
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147014" target="_blank">📅 12:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147013">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / سه تن از نیروهای نظامی شورای انتقالی جنوب یمن در شهر الضالع هدف تیراندازی قرار گرفته و کشته شدند.
🔴
گزارش‌ها حاکی است این حمله توسط نیروهایی انجام شده که از المخا در جنوب‌غرب یمن عقب‌نشینی کرده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147013" target="_blank">📅 12:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147012">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXx_lWHVXbXiVaFfP-Xq7G9yazuim2y1xXEdVYmN5yAqLQ6w_BRzLPCMEkpqDC6XvPLSsZNJ9swLdnijwH3f1qX7UhU_VwkqS8INXLXAbw9AeBlGuDwsvIhQHvcITAh0HysHYxmnD9ozLy4JN8Ss6fZGKeFPL3nRuSB-PR27E2Km-lIsXFMAccN7StcunaejlQAQczSZjASWW3fo-flCsDGt0Gymc_PObXCqCMR7Xe0Ux-0g9nipSQrQZ8oydffzqONKiZLXhyV43DV9TXNRuS0gKkn-CFE_IGtewOPTYPg5OkxGHs-M5luoSpQheQISY_SXVXHOQ9WZgp_Jb3e3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
درگیری‌ها میان نیروهای انصارالله و تیپ‌های غول‌پیکر وابسته به شورای رهبری ریاستی (PLC) در منطقه المضاربه در مسیر عدن، در استان لحج در جنوب یمن، همچنان ادامه دارد.
🔴
همچنین درگیری‌ها در هر سه جبهه استان تعز ادامه دارد و هر دو طرف تلاش می‌کنند پیشروی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147012" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147011">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در گفت‌وگوبا المیادین:  نشست برنامه‌ریزی‌شده برای روز دوشنبه در سلطنت عمان، گامی اساسی برای تضمین ثبات و امنیت در منطقه خلیج فارس خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147011" target="_blank">📅 12:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147010">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
اکسیوس: دور بعدی مذاکرات اسرائیل و لبنان که قرار بود هفته جاری برگزار شود، به اکتبر موکول شد
🔴
علت، تدارکات برای مجمع عمومی سازمان ملل عنوان شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147010" target="_blank">📅 11:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147009">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
صداوسیما: لبنان به سازش تن داد و نابود شد؛ حوثی ها مقاومت را انتخاب کردند و درحال پیروزی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147009" target="_blank">📅 11:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147008">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
توضیحات دولت عراق درباره علت بستن برخی از گذرگاه‌های مرزی
🔴
نهاد اطلاع رسانی امنیتی عراق: نهادهای امنیتی ذی‌صلاح تمهیدات اداری و امنیتی را در تعدادی از گذرگاه های آغاز کرده‌اند که این امر مستلزم بسته شدن آن‌هاست.
🔴
بر اساس این گزارش، مجموعه‌ای از اقدامات قانونی لازم انجام شده و کار اطلاعاتی، تحقیقات و بررسی‌ها برای تعیین شرایط نقض‌ها و تخلفات رخ داده در این گذرگاه‌ها و تدوین راه‌حل‌ها و بررسی‌های مناسب، تشدید شده است.
🔴
بر اساس اعلام این نهاد امنیتی عراق، دو گذرگاه مرزی زرباطیه و المنذریه به روی تردد مسافران باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147008" target="_blank">📅 11:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147007">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا از نفتکش‌هایی که از تنگه هرمز عبور می‌کنند خواسته در ساعات مشخصی از روز حرکت کنند تا امکان تأمین حفاظت نظامی از آن‌ها فراهم شود
🔴
این بازه‌های زمانی عبور به دو زمان مشخص در روز کاهش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147007" target="_blank">📅 11:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRHCpE2Pf0MPML6GlELsBX_paxiMzB2kQhpyIFGcfUNb53lbfL1B6g0W16azdItae5hWCJO_HG0o3e5j0ZzOC_gOpDf9beP2E8Lf8ncQvnEPtx0yinh493CeMGNyYJYMG4mhjhbEtWYpoTZyos0fG58liR0TZl342CbWcPx6B5vvVHM55Cf2WqRkVnZdbM609cyz7V0XBMsv7HQ6iwNZu-7U6q_4UFhIjCwjS5Tc0wGLhh6RVjA-Fc2oCLFQr-h5YqOdim7U-5gxyFHze-FOfX08sy75U1f-vWnVNj9pDhvXNVXQqks6qbSLeMZJWj54Sd32hQiG1KJ02_m8hefDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان با رئیس‌جمهور هند دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147006" target="_blank">📅 11:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/547525abfa.mp4?token=BLTSvnAWk8uZ6mlhVUI1ONYj3OW2mJDuUkDpWyhR2kKmtg8er-UZI1Nu3wAvokrbRdDSH2DEZEaWXNsykKcalwYYpFIXIlewxEPZjlBse-8mzZ9YnssGY3h2KsD41KIQTn3q01C07k7cW8-kfRaQjeu3bvusAkkcZ2oBgajYZdq3lxaMUhQL0a4_X7T6FcHatKnxZYfTq6fkA-Pn_Bjh0S8dTGRcA_EIr3vnjuid_pMLbo6c9yZh60f44UfJgoS2qLzqp4_0snC209xA8vOXGzCxK-dU6HJTA6PrQKACDe6A-Y3ogGmy8PrB6FYjch3CcE8G3KLgn71R-OsqE2XQHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/547525abfa.mp4?token=BLTSvnAWk8uZ6mlhVUI1ONYj3OW2mJDuUkDpWyhR2kKmtg8er-UZI1Nu3wAvokrbRdDSH2DEZEaWXNsykKcalwYYpFIXIlewxEPZjlBse-8mzZ9YnssGY3h2KsD41KIQTn3q01C07k7cW8-kfRaQjeu3bvusAkkcZ2oBgajYZdq3lxaMUhQL0a4_X7T6FcHatKnxZYfTq6fkA-Pn_Bjh0S8dTGRcA_EIr3vnjuid_pMLbo6c9yZh60f44UfJgoS2qLzqp4_0snC209xA8vOXGzCxK-dU6HJTA6PrQKACDe6A-Y3ogGmy8PrB6FYjch3CcE8G3KLgn71R-OsqE2XQHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با استقبال مقامات ایرلندی وارد دوبلین شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147005" target="_blank">📅 11:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69323d53ed.mp4?token=XaUNA5oEvw8AKG_NGF1FQ4Q8bslDys_Yifkp9i--hDK7HFaR1IQ8WTgee3SB-PWIh4NCZF4EZP8__mymASn0Irz6V9STbOUl_2YmNoC-xZkmEIfiV7FlApmBLqAblFRFJc3DHuQJeQeZ1VzSnqamXuT80LLrPB8yfmMbjt4oprWvcT3wKTTXKfY1q2GMfgYAdh2z4EBx5xiVf9NATarSfI2BzxE0d186Bh3emfDOwzVXyk3udq2WAVtzYI8uvbK_pNQaXKqCYXfY7pUuAN4jx5aTTct6ji_g6oirDivMKz98tcOmlhWPiZEEWTNVs_Y5mWMSqbpR4NgxOPgQ67d_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69323d53ed.mp4?token=XaUNA5oEvw8AKG_NGF1FQ4Q8bslDys_Yifkp9i--hDK7HFaR1IQ8WTgee3SB-PWIh4NCZF4EZP8__mymASn0Irz6V9STbOUl_2YmNoC-xZkmEIfiV7FlApmBLqAblFRFJc3DHuQJeQeZ1VzSnqamXuT80LLrPB8yfmMbjt4oprWvcT3wKTTXKfY1q2GMfgYAdh2z4EBx5xiVf9NATarSfI2BzxE0d186Bh3emfDOwzVXyk3udq2WAVtzYI8uvbK_pNQaXKqCYXfY7pUuAN4jx5aTTct6ji_g6oirDivMKz98tcOmlhWPiZEEWTNVs_Y5mWMSqbpR4NgxOPgQ67d_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نیرو: ممکن است بارش‌های سهمگین داشته باشیم/ همه آماده باشند؛ نباید غافلگیر شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147004" target="_blank">📅 11:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147003" target="_blank">📅 11:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58db88bf67.mp4?token=TUFDP0q9My_l6gAMwSQDNSo4tmgy3tqm3Kp89C-5uICYJSwPsmFqSnHQvFULYsbc4IOYA2L8c_6MNHTgFnfc_6T3zXi8JLTUNdlJkgkLuVttkRMTO7JaQ8I5ebhSSb8Anc0hT5WHeWiZdjlgjJyp5s6-M3CT5tAnFFbk2vInygUQIUzamapaWI2OChnm-rs3vDPfaZUO1tVpCr0QcDhGKx7aI83f5DLL7_pCpkMPmTLBcDmrxVPC7R5i6DnIIFVObL0SEitbrl5UQFLKBIEYG8_trF_FYycxCoJ1v_pZS269Yjn-IaIpiID9COeDgvn5n1IV-eYM0tNaB6IfeFkHwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58db88bf67.mp4?token=TUFDP0q9My_l6gAMwSQDNSo4tmgy3tqm3Kp89C-5uICYJSwPsmFqSnHQvFULYsbc4IOYA2L8c_6MNHTgFnfc_6T3zXi8JLTUNdlJkgkLuVttkRMTO7JaQ8I5ebhSSb8Anc0hT5WHeWiZdjlgjJyp5s6-M3CT5tAnFFbk2vInygUQIUzamapaWI2OChnm-rs3vDPfaZUO1tVpCr0QcDhGKx7aI83f5DLL7_pCpkMPmTLBcDmrxVPC7R5i6DnIIFVObL0SEitbrl5UQFLKBIEYG8_trF_FYycxCoJ1v_pZS269Yjn-IaIpiID9COeDgvn5n1IV-eYM0tNaB6IfeFkHwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت عجیب مجری؛ قلقلک مهمان روی آنتن زنده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147002" target="_blank">📅 11:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا از نفتکش‌هایی که از تنگه هرمز عبور می‌کنند خواسته در ساعات مشخصی از روز حرکت کنند تا امکان تأمین حفاظت نظامی از آن‌ها فراهم شود
🔴
این بازه‌های زمانی عبور به دو زمان مشخص در روز کاهش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147001" target="_blank">📅 10:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147000">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09617cd40e.mp4?token=Eun-mGhYCfdLqdpd-l6LDLQ-DFXOK3uWPpwYcQrOhClSW8rNEzEsD2AweVefm6xCnfbrbMNsQXg_fGqH0eyrgHNJsHd9_4l8TdJmCoFhAocip5hLfUJmRjHV5ytWQninPIuZi0J0EwAl-2_njbMz92Vh7ksSaGh2ly-GwB3mys1ToKo1n05IQ9kVcPA_4FAXv1hpsJMzC7B-re7L436kAWQJjN6Ic0Qxa8_oc0k09Z1cqZoABYmNPSSxQPxe1_OUbtFlBt1MIj44n2VGlgSgdsZ9SABmmzcaK-Pju4sB6Pp2ws0Km7QIeEiU0lx4E_vH073y9Tm5fAxNy28-3bKirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09617cd40e.mp4?token=Eun-mGhYCfdLqdpd-l6LDLQ-DFXOK3uWPpwYcQrOhClSW8rNEzEsD2AweVefm6xCnfbrbMNsQXg_fGqH0eyrgHNJsHd9_4l8TdJmCoFhAocip5hLfUJmRjHV5ytWQninPIuZi0J0EwAl-2_njbMz92Vh7ksSaGh2ly-GwB3mys1ToKo1n05IQ9kVcPA_4FAXv1hpsJMzC7B-re7L436kAWQJjN6Ic0Qxa8_oc0k09Z1cqZoABYmNPSSxQPxe1_OUbtFlBt1MIj44n2VGlgSgdsZ9SABmmzcaK-Pju4sB6Pp2ws0Km7QIeEiU0lx4E_vH073y9Tm5fAxNy28-3bKirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ در ایکس : با این رئیس جمهور در سر کار بازی نکنید، زیرا نتیجه خوبی نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147000" target="_blank">📅 10:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146999">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3_MYWDGDhhBxsP1DOtO6G3vnVyKfhY_XNzlTOgrNCClUuyURXEe_5kJ-EaY80YoOe5ZTtRgxTreFt2PV38Htn1M_vve-DzRs-bRWuVRKl7OTa9fGJUI9oRtFtgp5QFGufmSJsJKZ_5c3KmSV3hnHZQPLHwUXUfTUHb1IP-9ythpsSLOulXp8NET8BHP245sNxfy-dCN_ec_6yG4OL0TqS1XzQdcvlbRniaNN8FFM6mKZFF27Nw-oAOf1zMwgckXkyqAIzGMtOHZG5l9aY2MrJKQGxAwq_kTH8uE9zybzOx6WQfsphQY76uhv32PhjJdYnn9Xi0c7NF_J86XrMCV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: بدون پذیرش شروط ایران مذاکره‌ای در کار نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146999" target="_blank">📅 10:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146994">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad0ba6154.mp4?token=CNqUBG2dXX3TuE_zOd7NK5ao3OiAnzDiOBJZQeHqKh1PNqzh34CvFwgZtfcteRaAC3A9YvSDccoHkudqiWZQIeXteYzaytYjYCVQhEpv6ckl9CU0hvUR1q-EbpHMd8-Ym5r7v31cUeTvaNwcL-NLmBmi_XmkD83YXh2zQvtl9MUOE27chMjcg-5gg_NLJnIduGi_Y8LJLZKB93Vq0bZH9KjrarK-Sj66IW2BI-ilFqQiI3iAtd7H2wjyGyDKNs1HgWyLEMVxQCEBggp65bZJtZaEX2oz5W0cgX4fZUFMPScPMQvA_Wttxgc8Jhu-bc2xjG7yRF9n3Q50e6zSFWQstA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad0ba6154.mp4?token=CNqUBG2dXX3TuE_zOd7NK5ao3OiAnzDiOBJZQeHqKh1PNqzh34CvFwgZtfcteRaAC3A9YvSDccoHkudqiWZQIeXteYzaytYjYCVQhEpv6ckl9CU0hvUR1q-EbpHMd8-Ym5r7v31cUeTvaNwcL-NLmBmi_XmkD83YXh2zQvtl9MUOE27chMjcg-5gg_NLJnIduGi_Y8LJLZKB93Vq0bZH9KjrarK-Sj66IW2BI-ilFqQiI3iAtd7H2wjyGyDKNs1HgWyLEMVxQCEBggp65bZJtZaEX2oz5W0cgX4fZUFMPScPMQvA_Wttxgc8Jhu-bc2xjG7yRF9n3Q50e6zSFWQstA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌هایی در شهر سراوان در استان
سیستان و بلوچستان ایران
میان نیروهای امنیتی ایران و اعضای جبهه مبارزان خلق (PFF)، که پیش‌تر با نام جیش‌العدل شناخته می‌شد، رخ داد.
🔴
این درگیری‌ها پس از آن آغاز شد که نیروهای ایرانی به یکی از
مخفیگاه‌های این گروه
یورش بردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146994" target="_blank">📅 10:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146993">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان سعودی، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران رو بست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146993" target="_blank">📅 10:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146992">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18db6ddd86.mp4?token=qxcvbDdSjYe5-An02X2d3vA9yCKgWXGhNFWCAWICRJVr6B0RyLy7cz6sGSSUOalbilp_P63uSW2JivkITY1BRyEqOaTkqSrhAV1rR4QnhK6wrIYCDNz80lOQ5KA8vaGMXFf9Wq7C_z1m5cJ411yoFSG-oGwb6z6LMSw__qxh-nzCHo3CS4NNTdRwmM8cP9RyrkkoA9zExHdurAi7wyHsU4SEb7H90XrTY1oyyh6P3OYvpWJU-rgAT8-A-FP1Sjva1uLjPhpdP-ebksO4rrRJljD8lHHUFmTbcvTsmfUfy1BNalBT3qZBZKAlLSa7rspqzADNeUG_FIiVrZSV5cvYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18db6ddd86.mp4?token=qxcvbDdSjYe5-An02X2d3vA9yCKgWXGhNFWCAWICRJVr6B0RyLy7cz6sGSSUOalbilp_P63uSW2JivkITY1BRyEqOaTkqSrhAV1rR4QnhK6wrIYCDNz80lOQ5KA8vaGMXFf9Wq7C_z1m5cJ411yoFSG-oGwb6z6LMSw__qxh-nzCHo3CS4NNTdRwmM8cP9RyrkkoA9zExHdurAi7wyHsU4SEb7H90XrTY1oyyh6P3OYvpWJU-rgAT8-A-FP1Sjva1uLjPhpdP-ebksO4rrRJljD8lHHUFmTbcvTsmfUfy1BNalBT3qZBZKAlLSa7rspqzADNeUG_FIiVrZSV5cvYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، در تیک‌تاک:
«تازه از دالاس برگشتم؛ جایی که یک کنوانسیون فوق‌العاده داشتیم. دو شب بزرگ و دو سخنرانی مهم داشتیم. باورنکردنی بود.
🔴
جمهوری‌خواهان عملکرد بسیار خوبی دارند. اما همه می‌پرسند: «چطور این کار را انجام می‌دهی؟» چون الان هنوز اوایل کار است و من در دفتر بیضی کاخ سفید هستم.
🔴
می‌دانید چطور این کار را انجام می‌دهید؟ باید کاری را که انجام می‌دهید دوست داشته باشید. اگر عاشق کاری باشید که انجام می‌دهید، دیگر شبیه کار کردن نیست.
🔴
و من عاشق دوباره بزرگ کردن آمریکا هستم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146992" target="_blank">📅 10:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146991">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d5dd1149.mp4?token=rjdPwpYp1An91YoWvh-VbsKkM8ExRHiwhUpUh7KTx65fTxQx_y5Pk9qZzM4lx07Qcmw36I0ZQWS9MILkq_ik8RilsFz8HC0CBB12cvbL3xd67_UqM9ymyPfKxov3j3Yme0q5_4rgARx5qY6EtGD_fW79DQCBLbGfThrEEDGa55hyOJtCRvB-zGBum5RXFQjvFQFCTu-lMZtJzOfw65j_M5_7iamIGZteM6cVCe4-GFDIFBAAx70ez_zsbWQcwNiwLFOYp4aS-MDaWHP6jQU8oVBGcqBcQQsgjjOUozhJP6T_r54M5mHLeW7BTLkEanVyM5YIc_jgzjDmgs_ctg632A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d5dd1149.mp4?token=rjdPwpYp1An91YoWvh-VbsKkM8ExRHiwhUpUh7KTx65fTxQx_y5Pk9qZzM4lx07Qcmw36I0ZQWS9MILkq_ik8RilsFz8HC0CBB12cvbL3xd67_UqM9ymyPfKxov3j3Yme0q5_4rgARx5qY6EtGD_fW79DQCBLbGfThrEEDGa55hyOJtCRvB-zGBum5RXFQjvFQFCTu-lMZtJzOfw65j_M5_7iamIGZteM6cVCe4-GFDIFBAAx70ez_zsbWQcwNiwLFOYp4aS-MDaWHP6jQU8oVBGcqBcQQsgjjOUozhJP6T_r54M5mHLeW7BTLkEanVyM5YIc_jgzjDmgs_ctg632A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، واشنگتن دی‌سی را به مقصد ایرلند ترک کرد تا سفری دو روزه به این کشور داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146991" target="_blank">📅 09:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146990">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d237dcf54.mp4?token=GCt6vxfx9zHAg380F4JFYt2NNIRKHuuNeOurbKcm5rjrTDVjQlM8a8FbLRmMaS6h6IGuXlYjXKsupB1kVUiEeLxnxoUX6WbpNM-MAOuqlrqYoNfNh8YXT2cqolryHYnR6gx_n0cyAlZiJnZFveGHJUSv6LjqsgSF8uCzXfU_6myfjysrjJxK12BO1oKUJE4LNKOy8imMSmRDCS62o8XgByg23Kgp_zJ6raw_j0mQa01zHzm7DYzUcg93mmfZ2_wQVL4EqQyawFRRFaj23hoK-rBC3sqTnFrGT7ft2rK6PKfTxGBrhpxOUfrnv1lqFpTYJMeNeaBDsA-PUCWnNC-HVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d237dcf54.mp4?token=GCt6vxfx9zHAg380F4JFYt2NNIRKHuuNeOurbKcm5rjrTDVjQlM8a8FbLRmMaS6h6IGuXlYjXKsupB1kVUiEeLxnxoUX6WbpNM-MAOuqlrqYoNfNh8YXT2cqolryHYnR6gx_n0cyAlZiJnZFveGHJUSv6LjqsgSF8uCzXfU_6myfjysrjJxK12BO1oKUJE4LNKOy8imMSmRDCS62o8XgByg23Kgp_zJ6raw_j0mQa01zHzm7DYzUcg93mmfZ2_wQVL4EqQyawFRRFaj23hoK-rBC3sqTnFrGT7ft2rK6PKfTxGBrhpxOUfrnv1lqFpTYJMeNeaBDsA-PUCWnNC-HVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره انتخابات میان‌دوره‌ای: «اگر از نظر آماری نگاه کنید، وقتی رئیس‌جمهور هستید، چه جمهوری‌خواه باشید و چه دموکرات، به دلایلی اتفاقات عجیبی در انتخابات میان‌دوره‌ای رخ می‌دهد.
🔴
فکر می‌کنم در انتخابات میان‌دوره‌ای پیروزی بزرگی به دست خواهیم آورد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146990" target="_blank">📅 09:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146989">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130d71260b.mp4?token=GG4A2aSTJHfoGGlEtB1It0PRN9pHwmiTorzjEQM6F3_5RWE5tZMWYqe_2JPGz9_2ZUkvaCWmy_l6nnTLYds-KDW8IKrmtzvC4N07hMb8fVohI47NQXVZ7zH9lhhuKzimInWY89te3DLEfUTSUZQ0BtqagHxKTJOgZcCLLrkgS9KTkuqfUzVnFtXYCqVoDMQ5ZguBVlUaaeCm75dYIbNOxBVztATK2uzy40nuuvgiRjhhygo_pG7BZy0tR3-06heGgEvXWBrcDyB-eqK9OS_p_p1e3Dn7o01rKfcjFAZXg7B-uOWrnc40WsLizNgyx7ko8ZESPbbqZU73o61lJTOgnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130d71260b.mp4?token=GG4A2aSTJHfoGGlEtB1It0PRN9pHwmiTorzjEQM6F3_5RWE5tZMWYqe_2JPGz9_2ZUkvaCWmy_l6nnTLYds-KDW8IKrmtzvC4N07hMb8fVohI47NQXVZ7zH9lhhuKzimInWY89te3DLEfUTSUZQ0BtqagHxKTJOgZcCLLrkgS9KTkuqfUzVnFtXYCqVoDMQ5ZguBVlUaaeCm75dYIbNOxBVztATK2uzy40nuuvgiRjhhygo_pG7BZy0tR3-06heGgEvXWBrcDyB-eqK9OS_p_p1e3Dn7o01rKfcjFAZXg7B-uOWrnc40WsLizNgyx7ko8ZESPbbqZU73o61lJTOgnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، درباره سفرش به ایرلند: «ما دیدارهای زیادی با رهبران اروپایی و دیگر مقامات خواهیم داشت، بنابراین زمان بسیار جالبی خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146989" target="_blank">📅 09:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146988">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4e4a261f.mp4?token=HSf5x7KxYhURyWNIYCipzYfPZ90zzYtd-4u0pcPweQGLzdFrj8mOyXMophkmK_qqD0AQWLq0I_lMIVd7d6Uk290Lxs46sjcs78O2KPwbO3XgQ7VKm_9cRprlKDg7FHyL_qOvWVAFCi3UUTv0qzTzp6iuYvfo7BH4p-gNzDyqunUzr-erm1-HoCYz_tCDQeANxHLYnbeCB8b30fIi63_ZkVTyd_FaD7CKhmSzcAceJX_tMcqyFGtsSJ3ir7RFsyJP_TNJ24sE0begoaY2OC0KYhGvEo9xF1cR0sp5DC392K3_arHAgGgJfBVnY2OgnC9s4Qy22tBXoPvksgD9YzJpww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4e4a261f.mp4?token=HSf5x7KxYhURyWNIYCipzYfPZ90zzYtd-4u0pcPweQGLzdFrj8mOyXMophkmK_qqD0AQWLq0I_lMIVd7d6Uk290Lxs46sjcs78O2KPwbO3XgQ7VKm_9cRprlKDg7FHyL_qOvWVAFCi3UUTv0qzTzp6iuYvfo7BH4p-gNzDyqunUzr-erm1-HoCYz_tCDQeANxHLYnbeCB8b30fIi63_ZkVTyd_FaD7CKhmSzcAceJX_tMcqyFGtsSJ3ir7RFsyJP_TNJ24sE0begoaY2OC0KYhGvEo9xF1cR0sp5DC392K3_arHAgGgJfBVnY2OgnC9s4Qy22tBXoPvksgD9YzJpww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من عاشق سیاست هستم.
🔴
به دوستانم که در حوزه املاک یا ساخت‌وساز فعالیت می‌کنند می‌گویم؛ چون واقعاً در ساخت‌وساز و ساختن چیزها خیلی خوب بودم: «آیا در سیاست بهترم یا در ساخت‌وساز؟»»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146988" target="_blank">📅 09:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146987">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2200cb9823.mp4?token=KjtsFlzKfftRqIAzrbktHTOXxPDFNRTTHs6Ip_aL7hjFP6Hk1ZyCdpTZvGJDkH2JYOqOW96a9m0f3qX2Lbtn2bUnvXCsk_zSVdQzaRhEs01W2scXs4b57M94h4vZpvJJwqg_XH1d4DmWuvmcRMJOXTky8HG5nP7WgwSKYsNFbWS3lFNgBx_of4-NwrQ41RBJ1BIDLpmc6ayIvhL0jOHhUpTviOyO3ANd5CWSIPzLnZrGd9rNi8eUXljAToQdVnwAPfzoqFMTNQw8veGVsH_maxVUpmjhdHDWpzQmRm0OndNNlR0WEM9-7strljYpzjqClQRjMCROKnnXjJt2AwvnDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2200cb9823.mp4?token=KjtsFlzKfftRqIAzrbktHTOXxPDFNRTTHs6Ip_aL7hjFP6Hk1ZyCdpTZvGJDkH2JYOqOW96a9m0f3qX2Lbtn2bUnvXCsk_zSVdQzaRhEs01W2scXs4b57M94h4vZpvJJwqg_XH1d4DmWuvmcRMJOXTky8HG5nP7WgwSKYsNFbWS3lFNgBx_of4-NwrQ41RBJ1BIDLpmc6ayIvhL0jOHhUpTviOyO3ANd5CWSIPzLnZrGd9rNi8eUXljAToQdVnwAPfzoqFMTNQw8veGVsH_maxVUpmjhdHDWpzQmRm0OndNNlR0WEM9-7strljYpzjqClQRjMCROKnnXjJt2AwvnDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره هوش مصنوعی: «ما گاردریل‌ها و چارچوب‌های حفاظتی می‌خواهیم؛ می‌دانید، این موضوع خط بسیار باریکی دارد. چین گاردریل ندارد. گاردریل آنها رئیس‌جمهور شی جین‌پینگ است
🔴
آنها تقریباً در هیچ زمینه‌ای هیچ محدودیتی ندارند. در چین می‌توانید هر کاری انجام دهید
🔴
ما در زمینه هوش مصنوعی در حال پیروز شدن مقابل چین هستیم
🔴
و می‌دانید، یک عبارت معروف وجود دارد: هرکس هوش مصنوعی را برنده شود، پیروز است. اهمیت آن در همین حد است. از اینترنت هم بزرگ‌تر است. حتی ممکن است بزرگ‌ترین تحول تاریخ باشد و در بیشتر موارد، برای خیر و منفعت است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/146987" target="_blank">📅 09:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146986">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff392cb863.mp4?token=qyt0hu5AZCibdTEUfZPNOKAdIwU2MC5OWNzyVRiccD9Xg_Nzhy-vaINftHRqR1uOMNKbUYB6Oh9DZKjcjGEp9B2odCh72FFJkymMykWIrqCApMZTLgdps-uR70VdPz9iQBtDq1JZiiCq3TE9B118k7MRf67YdDKqKxBItlwLmjDPEAHnTG07AbPvnfJKXa4ziryIbva6XKUhe69EUC36b66Ru2xA-CDEDpysMuIWY0GppVp8kjn0ZL4zzi-Ko68zjj2cqTcJ7UbKxz6aQFPuYFlFk7-wPaXnAH9TUIz7sgbD7iZC95YDmW5P1B2CzPwQscRWwuln2njMU3fB73QD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff392cb863.mp4?token=qyt0hu5AZCibdTEUfZPNOKAdIwU2MC5OWNzyVRiccD9Xg_Nzhy-vaINftHRqR1uOMNKbUYB6Oh9DZKjcjGEp9B2odCh72FFJkymMykWIrqCApMZTLgdps-uR70VdPz9iQBtDq1JZiiCq3TE9B118k7MRf67YdDKqKxBItlwLmjDPEAHnTG07AbPvnfJKXa4ziryIbva6XKUhe69EUC36b66Ru2xA-CDEDpysMuIWY0GppVp8kjn0ZL4zzi-Ko68zjj2cqTcJ7UbKxz6aQFPuYFlFk7-wPaXnAH9TUIz7sgbD7iZC95YDmW5P1B2CzPwQscRWwuln2njMU3fB73QD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره آنتروپیک: «بیایید درباره آنتروپیک صحبت کنیم.
🔴
آنها کاری انجام دادند که بسیار بد بود و ما آنها را متوقف کردیم. خیلی سریع متوقفشان کردیم.
🔴
ما گاردریل‌هایی داریم. بزرگ‌ترین گاردریل این است که افرادی را داشته باشیم که به همان اندازه باهوش باشند؛ چون هیچ‌کس این موضوع را درک نمی‌کند، مگر اینکه ضریب هوشی بسیار بالایی داشته باشد — نه جو بایدن.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146986" target="_blank">📅 09:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146985">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf0c3dd2b.mp4?token=ET4Y6NJVp2QwbfLiA7M2wyza3idjULI-7pKICay1Lu-oBOBF8F9Nc3woWt9Rh9PNeWbQ4_E7N6eVy0Z1UNzSURdUvfponyjzGRup4BZdJgEuco-KRSZdOD-vmiGJ2mJ36nHzdor971mRuTXMcZmBH3yb7iEMFY-XrCDlWXAKf4-ghVNljt8cxSkvCRWgb4uT5qLkf8XPFVOjmU2r_tRM7QjjEtwVi2dZWM3j1kH8lnWKC-h76ELC0sVSU5NoGNfFEw2FxcyKBEpsw9P0byA5mQqLbla4-VKY32aFdImDfnfANSsQ3uWGzJPHMRVoxS867c6qklmSmc6EjSztbrol1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf0c3dd2b.mp4?token=ET4Y6NJVp2QwbfLiA7M2wyza3idjULI-7pKICay1Lu-oBOBF8F9Nc3woWt9Rh9PNeWbQ4_E7N6eVy0Z1UNzSURdUvfponyjzGRup4BZdJgEuco-KRSZdOD-vmiGJ2mJ36nHzdor971mRuTXMcZmBH3yb7iEMFY-XrCDlWXAKf4-ghVNljt8cxSkvCRWgb4uT5qLkf8XPFVOjmU2r_tRM7QjjEtwVi2dZWM3j1kH8lnWKC-h76ELC0sVSU5NoGNfFEw2FxcyKBEpsw9P0byA5mQqLbla4-VKY32aFdImDfnfANSsQ3uWGzJPHMRVoxS867c6qklmSmc6EjSztbrol1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «راستی،
جنگ ایران پس از انتخابات میان‌دوره‌ای
پایان خواهد یافت.»
🔴
اینگراهام
از
فاکس
:
«اگر جمهوری‌خواهان پیروز شوند. اگر جمهوری‌خواهان شکست بخورند، چرا جنگ ایران باید پایان یابد؟»
🔴
ترامپ
:
«خیلی‌ها فکر می‌کنند اگر شکست بخوریم، من عصبانی‌تر می‌شوم و کار را یکسره می‌کنم؛ می‌دانید؟ می‌دانید، این هم یک راه دیگر برای انجام این کار است. در هر صورت، آنها شکست می‌خورند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146985" target="_blank">📅 09:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146984">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/689440a6bc.mp4?token=lvEdDAbgKJx6-_oixuXNWm2dBiJe8Sw3NSwd56VCF-95ZnFsFevh6u-eCLf5TVBrJNXYHPqf7Uynz42108lLXaW-Ar_Lj3Ok5DlcX82JPaWK0u8Lm9UYLaAcK5d3rxC5UOMZ8_Cg6SW3Ds2OxIq3tmXh8Lz-s0Ee_PgX_3ScjNz2oeVLvnwAhfjoigpvXvwl_170KnCceAirg5X_2ZzxWkh8HKr0nciwFPEeJaDNSGfifk2t2r-ScYe8VG0DQqqx0H5KnChFjhsu9KUX3nkg0OcLMe7HKmUfuVZ6yRVbV2cnnWUHX9omnNrFlGyqGVH7BgZtbDftcJ3oftHbeII0uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/689440a6bc.mp4?token=lvEdDAbgKJx6-_oixuXNWm2dBiJe8Sw3NSwd56VCF-95ZnFsFevh6u-eCLf5TVBrJNXYHPqf7Uynz42108lLXaW-Ar_Lj3Ok5DlcX82JPaWK0u8Lm9UYLaAcK5d3rxC5UOMZ8_Cg6SW3Ds2OxIq3tmXh8Lz-s0Ee_PgX_3ScjNz2oeVLvnwAhfjoigpvXvwl_170KnCceAirg5X_2ZzxWkh8HKr0nciwFPEeJaDNSGfifk2t2r-ScYe8VG0DQqqx0H5KnChFjhsu9KUX3nkg0OcLMe7HKmUfuVZ6yRVbV2cnnWUHX9omnNrFlGyqGVH7BgZtbDftcJ3oftHbeII0uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اینگراهام از شبکه فاکس: «فکر می‌کنید وقتی تاریخ‌نگاران درباره این دوره بنویسند، چه خواهند گفت؟»
🔴
ترامپ
:
«وقتی کتاب‌ها نوشته شوند، فکر می‌کنم خواهند گفت که
من این کشور را نجات دادم.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146984" target="_blank">📅 09:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146983">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1096f3ff.mp4?token=LPo-laDRHg3oOYfJ5mccIgMl2Ho-_xUhtrjvqHO7ShJwFr8I3n7QfTCTNehKQ-2VYrPudCJFniR2XFNb5NVB9hWFKx6deAdbo7zwmc6AICVFqzUMw_WXohgIaPU_Qg-EG5NYbOt7RHQx4MWdml30hsgqI_-q5w_FY23OdG9eUO0eghPPNwUFFjBKfTERv3mxKYFeRC2qk3s6HdpbXrcNc1chwfCBYZ-GXEzw_W0Sl2WWkVEKuqli4AecBSz0qQ9jnqycQ02p_h1sKb7uZvz-gBDGWSgp-j11TNrI04-rIP4g_C8RY2_sB9xx3-4kSVuHE9XQLWHEGuR1VlU_z7p8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1096f3ff.mp4?token=LPo-laDRHg3oOYfJ5mccIgMl2Ho-_xUhtrjvqHO7ShJwFr8I3n7QfTCTNehKQ-2VYrPudCJFniR2XFNb5NVB9hWFKx6deAdbo7zwmc6AICVFqzUMw_WXohgIaPU_Qg-EG5NYbOt7RHQx4MWdml30hsgqI_-q5w_FY23OdG9eUO0eghPPNwUFFjBKfTERv3mxKYFeRC2qk3s6HdpbXrcNc1chwfCBYZ-GXEzw_W0Sl2WWkVEKuqli4AecBSz0qQ9jnqycQ02p_h1sKb7uZvz-gBDGWSgp-j11TNrI04-rIP4g_C8RY2_sB9xx3-4kSVuHE9XQLWHEGuR1VlU_z7p8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره آنتروپیک
:
«آنها مجبور شدند مهار شوند و حالا ناگهان، همان‌طور که می‌گویند، کاسه‌کوزه‌ای از خوبی و درستکاری شده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146983" target="_blank">📅 09:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146982">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f1804432.mp4?token=gaP2Q3IIGq7Xw67QogYgW3TxJJP9HvnFtvkdAiZlzpxEX7-FtSc5Zbi_b8jNnt-sXZ5VTCmcLFDbCI90W_0C1U2XlE_CL7YLJBUOTcgpIkNJOI67iSV_VrmiXn7hW0ODaFHKILRY0It25NrXE7TLq2Nnk9UG2TZxgNlcORe4s1K2Y1hB9G-AvOK48hVWIDDgtjGEXc18EAoxlzToTeduLmfvcKNWjRFzjtc4L6du4DkoK2aHcgVcXLigZyFT1ddUlVhe6YWnExTu6pU93SyZvWkha5PAMO5jvI5mC4BTmFKsTo_kwjG-DOdk4sBvsZb-3ZxGU5WUc6YjXZx-No8wtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f1804432.mp4?token=gaP2Q3IIGq7Xw67QogYgW3TxJJP9HvnFtvkdAiZlzpxEX7-FtSc5Zbi_b8jNnt-sXZ5VTCmcLFDbCI90W_0C1U2XlE_CL7YLJBUOTcgpIkNJOI67iSV_VrmiXn7hW0ODaFHKILRY0It25NrXE7TLq2Nnk9UG2TZxgNlcORe4s1K2Y1hB9G-AvOK48hVWIDDgtjGEXc18EAoxlzToTeduLmfvcKNWjRFzjtc4L6du4DkoK2aHcgVcXLigZyFT1ddUlVhe6YWnExTu6pU93SyZvWkha5PAMO5jvI5mC4BTmFKsTo_kwjG-DOdk4sBvsZb-3ZxGU5WUc6YjXZx-No8wtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره چین: «اگر چین بخواهد اینجا بیاید و کارخانه‌ای برای
تولید خودرو
راه‌اندازی کند، من با آن مشکلی ندارم.
🔴
نکته مهم این است که آنها کارگران آمریکایی را استخدام کنند و از نیروی کار ما استفاده کنند.
🔴
چیزی که نمی‌خواهم این است که آنها در مکزیک خودرو تولید کنند، آن را ارزان بسازند و بعد، می‌دانید، از طریق مرز به آمریکا ارسال کنند.
این دیگر اتفاق نخواهد افتاد.
🔴
درست مثل اینکه خلیج مکزیک دیگر خلیج مکزیک نیست؛ حالا خلیج آمریکا است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146982" target="_blank">📅 09:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146981">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd817edf8.mp4?token=rDSFprryzFmKyR-PZZdF179z64LhZrdXCXzV9GlOMagiNDIknY-gga85pPxZSnw6p8XMTfLn-CEsCliAFvjBxHyezAlP0wXWNopLt1YB5bg_mP0agJNRk5J4leiv6-pqyqHQD11r5fTYh9yw5RPb9fiMXFLGXzfFUhl3z9GJMvwIZk7QwdA4ghR0LG7lnYkPWWiY6_Ulvw9N82TbS7YDfNV8N4ntUZ9iLu8pIxr9O07iDqKlx_hbdydjOpGDFgC61_CZOw524zFfrOsUE-15SXbqM5mujyWDjRem_NXOC_L2jrEuBnm4rnsyuFU8mcbwCApB8WHdx5qr2wZPiLZsUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd817edf8.mp4?token=rDSFprryzFmKyR-PZZdF179z64LhZrdXCXzV9GlOMagiNDIknY-gga85pPxZSnw6p8XMTfLn-CEsCliAFvjBxHyezAlP0wXWNopLt1YB5bg_mP0agJNRk5J4leiv6-pqyqHQD11r5fTYh9yw5RPb9fiMXFLGXzfFUhl3z9GJMvwIZk7QwdA4ghR0LG7lnYkPWWiY6_Ulvw9N82TbS7YDfNV8N4ntUZ9iLu8pIxr9O07iDqKlx_hbdydjOpGDFgC61_CZOw524zFfrOsUE-15SXbqM5mujyWDjRem_NXOC_L2jrEuBnm4rnsyuFU8mcbwCApB8WHdx5qr2wZPiLZsUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«رئیس‌جمهور شی جین‌پینگ قرار است
دو هفته دیگر
برای یک شام رسمی خوب به اینجا بیاید.
🔴
ما با هم کنار می‌آییم. می‌دانید، من و او رابطه بسیار خوبی با هم داریم.
🔴
مردم می‌گویند: «اوه، او از ما جاسوسی می‌کند.» خب،
ما هم از او جاسوسی می‌کنیم.
می‌دانید، ما هم در این کار خیلی خوب هستیم.
🔴
ما اکنون روابط بسیار خوبی با چین
داریم.
قبلاً روابط بسیار بدی با چین داشتیم، اما حالا با چین خوب پیش می‌رویم.»
✅
@AloNewd</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146981" target="_blank">📅 09:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146980">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd52e61643.mp4?token=sxPVAkhXfR9fZ9xu0oHiPI6itPl0zeK41MYIbh5rnlEfuWICpHjmjlJzfjU1ZsFZSuBtEQEfy4NKRcm4_1IIH9vHNlyY66P0jAOP9BNrhlVh4gbU5lXOZzcN2T_hiFsL9VoiJZxM4GwOlu4GnWX4YN6Y6Z1u3pSbt5zL-SI4pp1m5uvh8vWLbwvDah7ztnklBdOaq8tu9rBh_ej_NUACDhAozSUqwSwMFLL3anUt4a05bfDv1XvMp4eii9cCePnYeXaW4Mt1eGn8g973_bMfahaVbMmqIiQFy73qJeAkoKqz9l11zvYLKNEGfXkijCD7U0Dry_d1fTncutO7g8BwIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd52e61643.mp4?token=sxPVAkhXfR9fZ9xu0oHiPI6itPl0zeK41MYIbh5rnlEfuWICpHjmjlJzfjU1ZsFZSuBtEQEfy4NKRcm4_1IIH9vHNlyY66P0jAOP9BNrhlVh4gbU5lXOZzcN2T_hiFsL9VoiJZxM4GwOlu4GnWX4YN6Y6Z1u3pSbt5zL-SI4pp1m5uvh8vWLbwvDah7ztnklBdOaq8tu9rBh_ej_NUACDhAozSUqwSwMFLL3anUt4a05bfDv1XvMp4eii9cCePnYeXaW4Mt1eGn8g973_bMfahaVbMmqIiQFy73qJeAkoKqz9l11zvYLKNEGfXkijCD7U0Dry_d1fTncutO7g8BwIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:به هر حال، جنگ با ایران بعد از انتخابات میان‌دوره‌ای به پایان خواهد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/146980" target="_blank">📅 09:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146979">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
مسعود پزشکیان در گفتگو با یک رسانه هندی خبر داد که روز دوشنبه توافق عمان و ایران درباره مسیر مشترک تنگه هرمز در حضور وزرای کشورهای عربی حاشیه خلیج‌فارس امضا و به سازمان دریانوردی بین‌المللی اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146979" target="_blank">📅 09:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146978">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی: چین پیش از حمله ایران به پایگاه موفق‌السلطی اردن که منجر به کشته شدن ۳ نظامی آمریکایی شد، تصاویر ماهواره‌ای با وضوح بالا را در اختیار تهران قرار داده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146978" target="_blank">📅 09:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146977">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=FqbVHebqbQjzbJx_COGrgCUE1VgHy-lhUGzyVsu6tome8kfd-o-yEdndkF-w3U7ptdh_BFAQbfi9HgSnirdQ1e69VRo7eXFs67A-8TNyp-a4pNehn4MDZS0cAnu8L84ie42uN5bN22YKs62y-fu-AW8djiEmo3ICquVtpuJ-_uPKMELhYM3BzyoRwbyBT1er9CVy2O31FblZWoJtK6VRn_5I0Sq16_Yb-eKKlYd21qMY0rTXIY5LQwX3rdEEInW68i9D8VlzPWQOCYsgfqTGRmhSzY4V3dEE5Y6_XGNYyh9lN3H4V6WOQIk_WC-0i0_DgKJp29xKMqYIebPu-u0N7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=FqbVHebqbQjzbJx_COGrgCUE1VgHy-lhUGzyVsu6tome8kfd-o-yEdndkF-w3U7ptdh_BFAQbfi9HgSnirdQ1e69VRo7eXFs67A-8TNyp-a4pNehn4MDZS0cAnu8L84ie42uN5bN22YKs62y-fu-AW8djiEmo3ICquVtpuJ-_uPKMELhYM3BzyoRwbyBT1er9CVy2O31FblZWoJtK6VRn_5I0Sq16_Yb-eKKlYd21qMY0rTXIY5LQwX3rdEEInW68i9D8VlzPWQOCYsgfqTGRmhSzY4V3dEE5Y6_XGNYyh9lN3H4V6WOQIk_WC-0i0_DgKJp29xKMqYIebPu-u0N7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات پهپادی روسیه به نیروها و تجهیزات اوکراینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/146977" target="_blank">📅 09:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146976">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بدر عبدالعاطی، وزیر خارجه مصر، بر تلاش برای آرام‌سازی اوضاع در باب‌المندب و تضمین آزادی دریانوردی تأکید کرد.
🔴
وی ادامه داد اختلال در ناوبری منطقه باب‌المندب، منجر به خسارت ۱۱ میلیارد دلاری به کانال سوئز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/146976" target="_blank">📅 08:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146975">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پزشکیان: تنگه هرمز به شرط اینکه آمریکا دست از محاصره و حمله بردارد، باز خواهد شد
🔴
روز دوشنبه در مسقط در حضور کشورهایی که از خاک آن‌ها به ما حمله شد، توافق عمان و ایران بر سر «مسیر مشترک در تنگه هرمز»، امضا می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/146975" target="_blank">📅 08:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146974">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac66aef0a.mp4?token=Hj7ABJCtZGdDeZXVCUM8sa6VrRusBEWLpPozz6IEltxcPeRq0gr3z2LtJRu81-0cPnHdSh7rTtkairHimS1hH9d5PEbKPo96UVYpolwr2Cdx8y3PuD5uuMv_IKf07N1ZPVfKS_7FeRIGkHNmflYoQZD0KDkIu28wtHLLv_D3vMlAqs6WrTT2wkxHAy7439tFTNWe24hwcTEf2w8n7bnIBaYs5MaGMcryj2uGtyAFs_3kPq1kPQENFOAo4PT3kWUvJ2QEgUqYjo9eItihyq75sPS77sFjvV9utiUxY06gv7LLxkRlUOxsClA8XsXwTAKNvzyNKkp_jyZrcAkC2lOkKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac66aef0a.mp4?token=Hj7ABJCtZGdDeZXVCUM8sa6VrRusBEWLpPozz6IEltxcPeRq0gr3z2LtJRu81-0cPnHdSh7rTtkairHimS1hH9d5PEbKPo96UVYpolwr2Cdx8y3PuD5uuMv_IKf07N1ZPVfKS_7FeRIGkHNmflYoQZD0KDkIu28wtHLLv_D3vMlAqs6WrTT2wkxHAy7439tFTNWe24hwcTEf2w8n7bnIBaYs5MaGMcryj2uGtyAFs_3kPq1kPQENFOAo4PT3kWUvJ2QEgUqYjo9eItihyq75sPS77sFjvV9utiUxY06gv7LLxkRlUOxsClA8XsXwTAKNvzyNKkp_jyZrcAkC2lOkKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: خیلی‌ها فکر می‌کنند اگر در انتخابات ببازیم من عصبانی‌تر می‌شوم و کار را یکسره می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/146974" target="_blank">📅 08:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146972">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMWuZCPcBBF_pDFQ2Mggpt0rpBtd5xEgdWE4dfk3HeiJEuwTTRJGIhsu03xrRvk5arVSjk1nGohKzuWoh0s43BjFs7Kz5WiCWUfWEsOoNWG_1E1_cMGn-Ya5kN9OLJbqLPAdEnjjq9vizkUxPMHN4BiiGbJ5reH2u6I8-oqsXmYjWDNX-Q5XmlcvsZaKOzWkSsuQYZhmjFZVbZLJ82vjamUTQjWBTsyRtnlWJwJLq0pTVxDXVjIxFqek3fsTpWYkWy5XmSd019jo1E44LODzQ8a-Gn32Zr-bN1sd9QU91lyKyhBtBuRhtBhjNsmloP2F12YEQNEQhJjgZ0FCRMgjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBu743Puko_yEnHqW0iez4cnzwEI40ptr_cWSt3Vk8Mu2ZNZCt_NzmrT0P2s0Qpi3jZ-_Sga0FjaK9R3R6uG5JhSnMlOi4Ye0sTfC6gTV1dQlfzPON5XRMgWcmXpmgLKqni-GNWIiKaa9VJG_BvsMLryQ7MHCors2wnzj6H29cMO3iYqo-qr6ncG2Ptc0D1_3Fd_kPgpYbm8kgbZUMCe7ewVjPMwSrO34glWCfGE9pmMury7wGAreGnIgwKtECCr10c_EurVWFimKhHTAxYFD5XbDXz3xattuW3W_IibgPGdWswSKJCLtADwwUBDpMryuWEexfxA5IG0vceMlaYrbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از یک مقام آمریکایی:
🔴
حمله ایران که در ماه ژوئیه منجر به کشته شدن 3 سرباز آمریکایی شد، ایران از تصاویر ماهواره‌ای چینی با وضوح بالا استفاده کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/146972" target="_blank">📅 05:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146971">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b31d12ff0.mp4?token=ufQL1-DagEcltRNw-97l2-TNE2jenzSsXV0ILlNUnMtK2BS3eQMErnkWJuZy0-liHnc2xYAVjcmzmJExU41D8FCNA9n8BBwsXL2v4EQjR-og8_n6u-3W_4QzR8ZKRvwtdx1XQ7PyFD9R_i_3vwH5gx5b38-uXHdjr4TgYzySb5OsmYcAXyH3ovv_zK-it48h5Jyz5x4aOVKRdIE7D_dVzin0bej2r-Qouo2WVOzmFpFYFxo7yekRnppOCdp5TbxXTdfAhdDmrWTK95XoKSBMEs-kRbpcy-aJfTeYblDVEfHEj6YUavBosAWKnGsLaTvBcmBJRQFbmiU00VNw5pBrWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b31d12ff0.mp4?token=ufQL1-DagEcltRNw-97l2-TNE2jenzSsXV0ILlNUnMtK2BS3eQMErnkWJuZy0-liHnc2xYAVjcmzmJExU41D8FCNA9n8BBwsXL2v4EQjR-og8_n6u-3W_4QzR8ZKRvwtdx1XQ7PyFD9R_i_3vwH5gx5b38-uXHdjr4TgYzySb5OsmYcAXyH3ovv_zK-it48h5Jyz5x4aOVKRdIE7D_dVzin0bej2r-Qouo2WVOzmFpFYFxo7yekRnppOCdp5TbxXTdfAhdDmrWTK95XoKSBMEs-kRbpcy-aJfTeYblDVEfHEj6YUavBosAWKnGsLaTvBcmBJRQFbmiU00VNw5pBrWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراق مرز با ایران رو بسته و هیچ ترددی رو اجازه نمیده انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/146971" target="_blank">📅 03:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146970">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مرز شلمچه به دستور نخست وزیر عراق رسماً به روی ایران بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/146970" target="_blank">📅 03:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146969">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
مرز شلمچه به دستور نخست وزیر عراق رسماً به روی ایران بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/146969" target="_blank">📅 03:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146968">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
برآورد شده در دو دهه برای تاسیسات تپه علی طاهر بالای 2 میلیارد دلار هزینه شده است که خب مشخصه از کجا تامین شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/146968" target="_blank">📅 01:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146967">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f254d9cb95.mp4?token=e6fZ3eE7H_XMtYBgeokkNaR8PsTSo8sUTxZs9LkU3XKo2OT1xHwsqqxNOz_lF8Tm2L7Kn0t4AXsMY7PbwmkU1KnBufmC6ado1d3QmN_7YtIK5BHq7tCsRChMbV-4kjzuF2z-NU7zJl4qbY1ddsLpC1pbdZQInLtWix0gfnnYmGewPrM5IeVCaM4845haFcJ3B5IGjuHtA6X21KZAz9Qd7eT7TgmD2r3W7gvqyBl_iZ1m6F2Z-F91H2b-dEjysqCCR6zF-BLuF_9q90-bVmwgrD1KDOtAYoQWFcvR1aQS0RXwyrNpzzp7pkblXvVawCK1-sBG_GDhcyQmsDgD2-N9OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f254d9cb95.mp4?token=e6fZ3eE7H_XMtYBgeokkNaR8PsTSo8sUTxZs9LkU3XKo2OT1xHwsqqxNOz_lF8Tm2L7Kn0t4AXsMY7PbwmkU1KnBufmC6ado1d3QmN_7YtIK5BHq7tCsRChMbV-4kjzuF2z-NU7zJl4qbY1ddsLpC1pbdZQInLtWix0gfnnYmGewPrM5IeVCaM4845haFcJ3B5IGjuHtA6X21KZAz9Qd7eT7TgmD2r3W7gvqyBl_iZ1m6F2Z-F91H2b-dEjysqCCR6zF-BLuF_9q90-bVmwgrD1KDOtAYoQWFcvR1aQS0RXwyrNpzzp7pkblXvVawCK1-sBG_GDhcyQmsDgD2-N9OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌ها در مأرب، در استان تعز، همچنان ادامه دارد
و گزارش‌ها حاکی از آن است که
نیروهای شورای رهبری ریاستی (PLC) از شهر عقب‌نشینی کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/146967" target="_blank">📅 01:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146965">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqDra4pjTx-IMr7uRVlxVS5mtIKGRiZ-IOY-XI-dUzX3csHFtdoKgqjWIcPNE0DLEuDsmHKU6ZVN4ZQvNfsZFeEEk1W3R5kaj8Gpo1673O7FbQ7IN2CJ9SZLyapvfDArymSVblHSm3cZA-jSpfitBhoU22-dxaphKtsbxJ4w6K89z93mumfsdxmiQ2WpEBDRtS3nnIXzlDvWp1q5TYBAvruyujb-DjGpSF3ZHoPGW6tSqG_GCIZHmdn82LBFhaGLVBT2Fz683k8a935gWPstK4pmbXmFRUKmmUt51ZmPSP00lqDBnlr1Sl-ta9W8ctdyQAARKiNS7OrJ-yx3o4f9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1eGeGWL9qB0_zkXt3EOY7D7rNd8Zkdo-qshaAKMYMjL1kY-4S1GAGZ5JIL9_v4Mo2tRxq2tSrZodONjbiwsyE1hP-cVyeSpepeGSMZieRfihSpKCI8Jbq7n9UtUd-AvWg4IgPTFv3KWcc6UATOSw8mEyI99WEa27GVb3UXH3ctb7lL_e2Kq3earuqkXm7LJT9-dhjTop2HXDaYWVowBSwoy7d0I4RPh1xejwBXFQaT7aUceG3xg_yOBYLUQ1bJEdn7FDBaP2NhIAjuKL51Z75jDFgko8nGbwh5CaXk6c_VbPkTPN6ZlOCJPbs7XSjdGlz5i2PU9aVs0pX2tRRKG_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
برخی منابع ادعا کردن که تابناک گفته بخشی از اموال علی کریمی در ازای تخریب رضا پهلوی آزاد شده ولی سریعا پاک کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/146965" target="_blank">📅 00:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146964">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ec3edad5.mp4?token=bgISn63jlx1rUqfMfFqiLh0tq57cxe6Oqt9AlzrRjksRPD0mvDAIq3l8ptSciDcQAv7gIb_Tfv4TVvohnwUQ5C0gLf_DBsEPVz_s0xX8g2BwxCz7cLnUEyZoVc6pHdHW_1RZiEMJj24ulXANKGEpuWoNmKGz-cLC8E46i9JCyd2sWntyELfYMEctGn_KY-BCK9W3XVrkslTplTlqff5SZ2Dti1g7ch39KcznWnyZbTSpP_DjLGsptRGaI0FbPu3Z1fsjWJY4ZuYxqfmup3AAv-dyaF2o010tggVeFild6AVOQNJUyH7TAXiL3ugOkusoimn_BOaOymtrJieCppiM-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ec3edad5.mp4?token=bgISn63jlx1rUqfMfFqiLh0tq57cxe6Oqt9AlzrRjksRPD0mvDAIq3l8ptSciDcQAv7gIb_Tfv4TVvohnwUQ5C0gLf_DBsEPVz_s0xX8g2BwxCz7cLnUEyZoVc6pHdHW_1RZiEMJj24ulXANKGEpuWoNmKGz-cLC8E46i9JCyd2sWntyELfYMEctGn_KY-BCK9W3XVrkslTplTlqff5SZ2Dti1g7ch39KcznWnyZbTSpP_DjLGsptRGaI0FbPu3Z1fsjWJY4ZuYxqfmup3AAv-dyaF2o010tggVeFild6AVOQNJUyH7TAXiL3ugOkusoimn_BOaOymtrJieCppiM-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمک نشناس مثل چادی هوپان
قبل و بعد قهرمانی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/146964" target="_blank">📅 00:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146963">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
شبکه خبری ABC آمریکا به نقل از مقامات آمریکایی:دولت عربستان سعودی در روزهای اخیر آمادگی خود را برای انجام یک عملیات نظامی گسترده علیه حوثی‌ها اعلام کرده است، حتی اگر لازم باشد به تنهایی وارد عمل شود. با این حال، ریاض هنوز تصمیم نهایی در این زمینه را اتخاذ نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/146963" target="_blank">📅 00:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146962">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c414beafb6.mp4?token=oYsFM024yrzGVRcgU1vTr6qc5y9H74yb_zzXhdzmOZncrkeZbCfeQx1YXr8BUVUYliFWWdw8trvXzD8m-ZT7WQ_V8_bGmX5GAfRU_ei2y_-kw8c2sTmCgsFe7otsLsh5fhHAU4KvnkX7iytuUzGCmGreyG8bVDRvVGy5KQLQOy0x3ROWrQcE8Yg2h86gUFqZxFJYnJd1FxOFlEVMszIJzadz9uZT_vMU9xoHjxfS6BC834nrtqVE6GW6lOJVww1FCitNCbIXs-paxToG7tT_aIBlaPYatOaV8lLybRaj4rMr9c-tLrX9cKrYq1U8pRsIbNZMD3zEHzQYxdIwT0rhBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c414beafb6.mp4?token=oYsFM024yrzGVRcgU1vTr6qc5y9H74yb_zzXhdzmOZncrkeZbCfeQx1YXr8BUVUYliFWWdw8trvXzD8m-ZT7WQ_V8_bGmX5GAfRU_ei2y_-kw8c2sTmCgsFe7otsLsh5fhHAU4KvnkX7iytuUzGCmGreyG8bVDRvVGy5KQLQOy0x3ROWrQcE8Yg2h86gUFqZxFJYnJd1FxOFlEVMszIJzadz9uZT_vMU9xoHjxfS6BC834nrtqVE6GW6lOJVww1FCitNCbIXs-paxToG7tT_aIBlaPYatOaV8lLybRaj4rMr9c-tLrX9cKrYq1U8pRsIbNZMD3zEHzQYxdIwT0rhBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بازسازی مرکز تجارت جهانی:  پیشنهاد من این بود که دو ساختمان یکسان ساخته شوند و ارتفاع آن‌ها ۱۰ طبقه بیشتر باشد.
🔴
به نظر من، این کار می‌توانست یک اقدام بسیار عالی باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/146962" target="_blank">📅 00:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146960">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
برای مردن در ایران حدود 1 میلیارد پول نیاز دارید که خرج کفن و دفن بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/146960" target="_blank">📅 00:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146959">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2693036490.mp4?token=oo2BspfD_lmgi74-c42VdWYL_RD_Sz8jN8dwyTcITByCTwH_VbiRHNtKyC0OYQGd7I86BRwnyuh_voqwfQTGTOwsLAnKtQiDvj00XZNG36HrojXzS-A2opl5L6C4OkoeAUiv1V62rYdlEDFE0lnU86Ab0D_GGagTDe3hjMiGnuVJnbqRcNo0dT8-Aer3jRxDxJO8KX5WDHdt6dv9e19EnuAgCynTrSptdPyV00Mzhw2dBNGiMZLE_LoPbzDhQ4jdAXWo355J3ZJfCpTa3Mm1ykEWptvcdxYLXr8Fyga55L5tw-wT6-ZwZ_-SXLtECC6FAwrPYjJY9lAUCAA8DEdjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2693036490.mp4?token=oo2BspfD_lmgi74-c42VdWYL_RD_Sz8jN8dwyTcITByCTwH_VbiRHNtKyC0OYQGd7I86BRwnyuh_voqwfQTGTOwsLAnKtQiDvj00XZNG36HrojXzS-A2opl5L6C4OkoeAUiv1V62rYdlEDFE0lnU86Ab0D_GGagTDe3hjMiGnuVJnbqRcNo0dT8-Aer3jRxDxJO8KX5WDHdt6dv9e19EnuAgCynTrSptdPyV00Mzhw2dBNGiMZLE_LoPbzDhQ4jdAXWo355J3ZJfCpTa3Mm1ykEWptvcdxYLXr8Fyga55L5tw-wT6-ZwZ_-SXLtECC6FAwrPYjJY9lAUCAA8DEdjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا: یکی از دوستان من نتوانست یک هواپیمای گلف‌استریم را در کانادا بخرد، به دلیل یک قانون خاص که در آنجا وجود داشت.
🔴
من بلافاصله تعرفه‌های سنگینی را بر روی شرکت بمباردیه اعمال کردم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/146959" target="_blank">📅 00:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146958">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
درگیری‌ها بین نیروهای انصارالله و نیروهای همسو با شورای انتقالی جنوب (PLC) در شمال غربی شهر مأرب، منطقه‌ای که تحت کنترل شورای انتقالی جنوب قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/146958" target="_blank">📅 00:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146957">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: من رأی اعراب در میشیگان را به دست آوردم؛ اتفاقی که قبلاً هرگز رخ نداده بود.
🔴
رامنی فقط ۲ درصد رأی آن‌ها را گرفته بود و هنوز هم دنبال این هستند که بفهمند آن ۲ درصد چه کسانی بودند! هیچ‌کس نمی‌تواند پیدایشان کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/146957" target="_blank">📅 23:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146956">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع ارشد ایرانی: مذاکره تا زمان پذیرش شروط ایران امکان‌پذیر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/146956" target="_blank">📅 23:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سنتکام: از آغاز محاصره علیه ایران، مسیر ۹۹ کشتی تجاری را تغییر دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/146955" target="_blank">📅 23:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146954">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfec33d636.mp4?token=Fu1aw62H9igZV6qipBF5hikcQhvl2S3oQSoa1Yc4Zo7Wo2UlN7acEhH4g-1AM9xzx3_77xGf5R2NzCy6PGoOdt_IokqBlRDB_0wZp2fpqOW21vu_RMjRQKTAVLcWU41ckjzYenI-8eNmrBok0sBykfBXx0oGIZrKIlMyOyujZhpfCv_EahGsdtMX1HyqUV-Gwvy5VwDAYEh3_Aw8Jd16HJmhY50UPcJ_N8xWNvdWjuRKnwUaQWvoKJKWl6N9RYUOi71tvgnQ0_ejCIs6wguKcMIJIZCL0TUhIq9mVTkBH2gTjoSIbJTTsCtqQ6V_7612IaiSkKo1V5hciFV6rV65JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfec33d636.mp4?token=Fu1aw62H9igZV6qipBF5hikcQhvl2S3oQSoa1Yc4Zo7Wo2UlN7acEhH4g-1AM9xzx3_77xGf5R2NzCy6PGoOdt_IokqBlRDB_0wZp2fpqOW21vu_RMjRQKTAVLcWU41ckjzYenI-8eNmrBok0sBykfBXx0oGIZrKIlMyOyujZhpfCv_EahGsdtMX1HyqUV-Gwvy5VwDAYEh3_Aw8Jd16HJmhY50UPcJ_N8xWNvdWjuRKnwUaQWvoKJKWl6N9RYUOi71tvgnQ0_ejCIs6wguKcMIJIZCL0TUhIq9mVTkBH2gTjoSIbJTTsCtqQ6V_7612IaiSkKo1V5hciFV6rV65JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور تد کروز درباره اسرائیل: می‌توانید دولت اسرائیل را نقد کنید و ضدیهودی نباشید.
🔴
اما به شما می‌گویم: صددرصد ضدیهودیان، ضداسرائیل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/146954" target="_blank">📅 23:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146953">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d902513f5.mp4?token=cxFdfmEpir5f2nnsLpiyEhsEv9-MRaZ0_6lwr-smZ86NchqJBME2L-X-O-8L96bxh3HGj1ZrUEsMoF1139SMggZptKqjc_A78GwPMna-1J3IsIUgCgVQeFP6n5vIUYtqtl6RLiqAwOP1by9AI2YJKymrQKqdbC97xkuCGcJ6Wc76EFzsrms94K_fJx2uLAk4ejj93wnPzNLSjVqMUwtKWDfOSAeuxBCJmIx-rp0Wk-OpRUHsJ4fJsECbluaL5irCTlOOLbHKiB7iRCaJKvW54OOA_FEkOjlD_aRJQlbYwoJsI-5HSrRsK90jYbsRfmnzT4pdqnoUUMT9KPINoB6PAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d902513f5.mp4?token=cxFdfmEpir5f2nnsLpiyEhsEv9-MRaZ0_6lwr-smZ86NchqJBME2L-X-O-8L96bxh3HGj1ZrUEsMoF1139SMggZptKqjc_A78GwPMna-1J3IsIUgCgVQeFP6n5vIUYtqtl6RLiqAwOP1by9AI2YJKymrQKqdbC97xkuCGcJ6Wc76EFzsrms94K_fJx2uLAk4ejj93wnPzNLSjVqMUwtKWDfOSAeuxBCJmIx-rp0Wk-OpRUHsJ4fJsECbluaL5irCTlOOLbHKiB7iRCaJKvW54OOA_FEkOjlD_aRJQlbYwoJsI-5HSrRsK90jYbsRfmnzT4pdqnoUUMT9KPINoB6PAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هیچ‌کس فکر نمی‌کرد توماس ماسی می‌تواند شکست بخورد.
🔴
او با اختلاف ۱۹ امتیاز شکست خورد و از بین رفت، بنابراین من به این افتخار می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/146953" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146952">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما در وضعیت «نه‌ جنگ، نه‌ صلح» نیستیم؛ ما در وضعیت جنگ هستیم
🔴
تحریم و محاصرهٔ دریایی به منزلهٔ جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/146952" target="_blank">📅 23:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146951">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b7d6fd0c1.mp4?token=q-7uJwLa-932ZurvDEksIInDEcXRBjNypmzhgcNjpO1lieB_cxrF831IMmuroOEOUlbBdRUssnIFwjNfmpdPzAeTvUE7o74dbGk2kOOxNj4CXnRUngKJbHhJGr1Ir86hNuQaQWEVHtTpt5vxYmNLtz509qrcRimOpnErShHJRFIb0h5top8q1fkD2ijhPwKjiFEZyIxWfqLpgNXh_B5yvWd3XR-v__rPwSghhBJzbpc6Lf5F8mZiHLAKkrwcjAIVFnTmlq4zJshFJ6FUydlMZB4Tun7zfF2pv87Njd8xsvNdzROOgDI6nkluTjOF2V_99ysEAVGkopleLGcXbYg_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b7d6fd0c1.mp4?token=q-7uJwLa-932ZurvDEksIInDEcXRBjNypmzhgcNjpO1lieB_cxrF831IMmuroOEOUlbBdRUssnIFwjNfmpdPzAeTvUE7o74dbGk2kOOxNj4CXnRUngKJbHhJGr1Ir86hNuQaQWEVHtTpt5vxYmNLtz509qrcRimOpnErShHJRFIb0h5top8q1fkD2ijhPwKjiFEZyIxWfqLpgNXh_B5yvWd3XR-v__rPwSghhBJzbpc6Lf5F8mZiHLAKkrwcjAIVFnTmlq4zJshFJ6FUydlMZB4Tun7zfF2pv87Njd8xsvNdzROOgDI6nkluTjOF2V_99ysEAVGkopleLGcXbYg_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جمهوری‌خواه تد کروز درباره ایران: هر زمان که یک تعارض نظامی در خاورمیانه رخ دهد، قیمت‌های بنزین بالاتر خواهند رفت.
🔴
و ترامپ تصمیم گرفت که الزامات امنیت ملی برای جلوگیری از دستیابی ایران به سلاح هسته‌ای آن‌قدر مهم هستند که تحمل برخی هزینه‌های اقتصادی کوتاه‌مدت ارزش آن را دارد.
🔴
من فکر می‌کنم که این یک تصمیم مسئولانه بود که ایمنی آمریکا را افزایش داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/146951" target="_blank">📅 23:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146950">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f29b9673.mp4?token=Dm9Asw_R3TzL-4QtxN-1YsfF-L_inhPwnKq1_wJjgNLAADy08x9curTe8-QKwWjkfIeS-bI2nglWfyIKafdxoH5xY38vHEWQ0UOwOhE1aiBbKKekPQ7NVyJA2ia0gxCVt3Ivnr41qEXKIl9GMuyJDG7BDoR66clvgHfhAbJ_F3LpAB0rGXzoooB9h7Zv8Yoi1lOrb56ar7e_HDSKUvJ-8IIn89QUecySU8kapzLjaxezSNZ6CDzO60UVOXPsEQ8meajQaZ6ElhypapnCB7R9X4K04Zh1kbR8dET6vLGGNW7uNF4TolvMqXKqpxQjjGtcvMnhW5OqLgBaWF8fYMVvCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f29b9673.mp4?token=Dm9Asw_R3TzL-4QtxN-1YsfF-L_inhPwnKq1_wJjgNLAADy08x9curTe8-QKwWjkfIeS-bI2nglWfyIKafdxoH5xY38vHEWQ0UOwOhE1aiBbKKekPQ7NVyJA2ia0gxCVt3Ivnr41qEXKIl9GMuyJDG7BDoR66clvgHfhAbJ_F3LpAB0rGXzoooB9h7Zv8Yoi1lOrb56ar7e_HDSKUvJ-8IIn89QUecySU8kapzLjaxezSNZ6CDzO60UVOXPsEQ8meajQaZ6ElhypapnCB7R9X4K04Zh1kbR8dET6vLGGNW7uNF4TolvMqXKqpxQjjGtcvMnhW5OqLgBaWF8fYMVvCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا: کانادا سال‌هاست که از ما کلاهبرداری کرده است.
🔴
آن‌ها سخت‌ترین مردم برای انجام کسب‌وکار هستند. آن‌ها فکر می‌کنند حق دارند.
🔴
آن‌ها باید یک ایالت باشند. می‌دانید، اگر یک ایالت بودند، ما مشکلی نداشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/146950" target="_blank">📅 23:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146949">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
خط فقر برا خانواده های ۴ نفره به ۱۰۰ میلیون تومن رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/146949" target="_blank">📅 23:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146948">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b10559faa.mp4?token=dkFf4-d3wgZWRqB3PODuv8luD8R_HhvYeWwRLHxnrf55Fe6fflj3ea5xnx76QPQ4GMD5F6Ibj6_htGKRxwk-5teivduN-bBWRbRaP-8coROyuUztMLydcw77RQ0zCLeuCtUS4C6OeRgfIjEvqDCzB217QHT1CZq7-xeCi9WgMOUGQqDzHWetyNoHi7pRMrEbdzdvyuahYuxTNYymwIaLsv1gfzBNUZg1_oYbN7t9qHsVBkhYvOUwGOAlBONPO7CvteIMncHzVzPMFNiZYMLAzXuKxXtdsTjjwHAbRe99EgjzZVGsB6RWB6WhFZHmb1iyhFG8ctJqHFJ8MSN7nysXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b10559faa.mp4?token=dkFf4-d3wgZWRqB3PODuv8luD8R_HhvYeWwRLHxnrf55Fe6fflj3ea5xnx76QPQ4GMD5F6Ibj6_htGKRxwk-5teivduN-bBWRbRaP-8coROyuUztMLydcw77RQ0zCLeuCtUS4C6OeRgfIjEvqDCzB217QHT1CZq7-xeCi9WgMOUGQqDzHWetyNoHi7pRMrEbdzdvyuahYuxTNYymwIaLsv1gfzBNUZg1_oYbN7t9qHsVBkhYvOUwGOAlBONPO7CvteIMncHzVzPMFNiZYMLAzXuKxXtdsTjjwHAbRe99EgjzZVGsB6RWB6WhFZHmb1iyhFG8ctJqHFJ8MSN7nysXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جمهوري
ایران: اگر کاری که من انجام می‌دهم را انجام ندهید، آن‌ها یک سلاح هسته‌ای خواهند داشت.
🔴
اگر یک سال و نیم پیش با بمب‌افکن‌های B-2 آن‌ها را به‌شدت بمباران نکرده بودم، الان یک سلاح هسته‌ای داشتند. و از آن استفاده می‌کردند.
🔴
اسرائیل از بین می‌رفت. خاورمیانه از بین می‌رفت.
🔴
شما این را از آن واقعیت می‌بینید که رژیم ایران تمام آن بمب‌ها را رها کرد. من منظورم این است که مردم، مانند عربستان سعودی، متعجب شدند. همه شوکه شدند که به جای آن (موشک‌ها) از یک سلاح هسته‌ای استفاده کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/146948" target="_blank">📅 23:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146947">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d866f8f748.mp4?token=OtnaMGJ5_IFuo5Y5tFwCyBs9-fESobcGmKcAYCuszV9vTsRtr1fapsFgyD7v8ohua2AO3aLpQqX92GAllk7keKVNTGCw6tmkKNc66oDC8dGG0VAbz2Y_VW825Gj1qavS2Fo6hzTZpHdKmuSCqrk5fYq8IWV52yVMQlRh5YPGbpR0Suqm_iqXYQ87k4sMMakqMjhjItqYiqicUI2lN7uN6zPqt2bTTfWrcQRLyoOApnqgi5QAzl4QtQWKwhE-ZcLcW-FbfNpt62RFxq_32TWBovQCd3oyTYX2q046noN8cKIvChwKbzZGjPuZtEssvt2URWcw8OZvAV198P3I2BmO4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d866f8f748.mp4?token=OtnaMGJ5_IFuo5Y5tFwCyBs9-fESobcGmKcAYCuszV9vTsRtr1fapsFgyD7v8ohua2AO3aLpQqX92GAllk7keKVNTGCw6tmkKNc66oDC8dGG0VAbz2Y_VW825Gj1qavS2Fo6hzTZpHdKmuSCqrk5fYq8IWV52yVMQlRh5YPGbpR0Suqm_iqXYQ87k4sMMakqMjhjItqYiqicUI2lN7uN6zPqt2bTTfWrcQRLyoOApnqgi5QAzl4QtQWKwhE-ZcLcW-FbfNpt62RFxq_32TWBovQCd3oyTYX2q046noN8cKIvChwKbzZGjPuZtEssvt2URWcw8OZvAV198P3I2BmO4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تاکر کارلسون: من می‌گویم که تاکر کارلسون هرگز از من خوشش نمی‌آمد. من به نوعی کارهای زیادی برای او انجام دادم.
🔴
من و تاکر رابطه‌ای بسیار نوسانی داشته‌ایم.
🔴
نکته جالب این است که او نسبت به جنگ حساسیت دارد. بیشتر با من و جنگ. اما باید درک کنید که ایران نمی‌تواند سلاح هسته‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/146947" target="_blank">📅 23:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d78dd6d27.mp4?token=ErRVlz-uU9-Y6FJmPcnUdSOQvpIaGzruzyWJH9bErfrQq-B_4epqh_z32dIs_wrqdaRNbucVzCf-8COCQjHNmxm251vqc3sqfmN5FnUPQd8RVRyDdahnPTOzaYstcFFU_y5R06axivhfeGKRNUwQp2maEJlSQ5-LkBvo1giqVMidmad_knMzrWaik3F01mFfNXbpcRg36Zmxs86pNIDE44_2Hzntpj50m7Klr1VqbJR6HPG3o1JEtsIS8kNLyJapGKno1iTWOywAD3f2ixyQPlxqOAUpcvjOH8UROGiAJiVBtp252kgZ0ZLNYZs0h7yWlLzorngr3CinFUb0vlwRPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d78dd6d27.mp4?token=ErRVlz-uU9-Y6FJmPcnUdSOQvpIaGzruzyWJH9bErfrQq-B_4epqh_z32dIs_wrqdaRNbucVzCf-8COCQjHNmxm251vqc3sqfmN5FnUPQd8RVRyDdahnPTOzaYstcFFU_y5R06axivhfeGKRNUwQp2maEJlSQ5-LkBvo1giqVMidmad_knMzrWaik3F01mFfNXbpcRg36Zmxs86pNIDE44_2Hzntpj50m7Klr1VqbJR6HPG3o1JEtsIS8kNLyJapGKno1iTWOywAD3f2ixyQPlxqOAUpcvjOH8UROGiAJiVBtp252kgZ0ZLNYZs0h7yWlLzorngr3CinFUb0vlwRPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ دربارهٍ تاکر کارلسون
:
من تاکر کارلسون را از مدت‌ها پیش می‌شناسم و رابطه‌ام با او بسیار نوسانی بوده است. او بسیار ناسازگار است. و شاید من هم همین‌طور باشم، اما به شما می‌گویم، او بسیار ناسازگار است.
🔴
او بسیار یک فرد فرصت‌طلب است. البته، چند ماه پیش او را رها کردم چون احساس می‌کردم این کار نامناسب است.
🔴
او چیزهای بدی، چیزهای بسیار بدی می‌گفت. نه لزوماً دربارهٍ من، بلکه دربارهٍ بسیاری از چیزهای دیگر که در حال وقوع هستند.
🔴
او به افرادی مانند مارک لویین، که من فکر می‌کنم عالی هستند، و دیگران حمله می‌کرد. شخصاً، من از این موضوع خوشم نمی‌آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/146946" target="_blank">📅 23:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612e19ba40.mp4?token=BxXHHrlqdq3uKrmnbJwX23qY0VWUIedHaJ5q5OdwUjkEcsrQyFHc00moPpER6Hl00psaYEdXjEDqz_8R9y_ZjcvXWC7-OM-1CfqUkYx6tyT6e1xs9ITNumrCdz3J0oTUXPaTMbpeS-PGtbcOmYfj7rlMSG026lPQ1EFoWyc8bqOmpMAViBJU_yqbBa8DB_IQTxcybjuel1dsqGc5riMHYe7o7VvJeZ4aWcllC8ZtTNRpHttJrrAGsQE0U_tYZkX6Jeu5dGv6rTTDrs4CHnxsTjgR2Ymg3H3XgmztlvsPyHOwVHvk8Y56ZwqDyzJ8GPw2L5n0TTiBy9OUHXfIwQciHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612e19ba40.mp4?token=BxXHHrlqdq3uKrmnbJwX23qY0VWUIedHaJ5q5OdwUjkEcsrQyFHc00moPpER6Hl00psaYEdXjEDqz_8R9y_ZjcvXWC7-OM-1CfqUkYx6tyT6e1xs9ITNumrCdz3J0oTUXPaTMbpeS-PGtbcOmYfj7rlMSG026lPQ1EFoWyc8bqOmpMAViBJU_yqbBa8DB_IQTxcybjuel1dsqGc5riMHYe7o7VvJeZ4aWcllC8ZtTNRpHttJrrAGsQE0U_tYZkX6Jeu5dGv6rTTDrs4CHnxsTjgR2Ymg3H3XgmztlvsPyHOwVHvk8Y56ZwqDyzJ8GPw2L5n0TTiBy9OUHXfIwQciHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: امنیت منطقه باید با گفت‌وگو میان کشورهای منطقه و بدون حضور بیگانگان تأمین شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/146945" target="_blank">📅 22:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزارت خارجه: عربستان، ژاپن و اردن تبعات رای مثبت خود به قطعنامهٔ ضدایرانی آژانس را خواهند دید و ما آن‌ها را پاسخگو خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/146944" target="_blank">📅 22:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146943">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be896fba71.mp4?token=ChPOT9VpprC0BXw6ghqsfKEtoGfKkxyvn9PwnBpStt4fQlgSswB7ZBpUVQ6G9vLLdJit8-uhX9DqLn1YflgxS8S47HqTKwBXCXoFtbyUKtW_jyptrWj07qPZ1UKxQ45rwFuFwTcMlBv88gfCuJUiEo3K59w8WPS0UcaltUz1dfLhBFJnlWcSodRBJjNV0kLUmnTjjBop7d214lzDzj4IOKUhWG_h2-eEcTQddg657vRjR4X83SQMX-pumHxx4j-pRDiEUvxwVRhu3LWCPAaUI0HGWd6abl0JnSsTAxGqPSJWOaMqwJbazUowWNl1G6W0qT555aVRFndanvD4b2AZrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be896fba71.mp4?token=ChPOT9VpprC0BXw6ghqsfKEtoGfKkxyvn9PwnBpStt4fQlgSswB7ZBpUVQ6G9vLLdJit8-uhX9DqLn1YflgxS8S47HqTKwBXCXoFtbyUKtW_jyptrWj07qPZ1UKxQ45rwFuFwTcMlBv88gfCuJUiEo3K59w8WPS0UcaltUz1dfLhBFJnlWcSodRBJjNV0kLUmnTjjBop7d214lzDzj4IOKUhWG_h2-eEcTQddg657vRjR4X83SQMX-pumHxx4j-pRDiEUvxwVRhu3LWCPAaUI0HGWd6abl0JnSsTAxGqPSJWOaMqwJbazUowWNl1G6W0qT555aVRFndanvD4b2AZrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: محدودیت دسترسی آژانس نتیجه حمله به تأسیسات هسته‌ای ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/146943" target="_blank">📅 22:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146942">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8466606615.mp4?token=cM9wOKEf4nwVbgdtY4gtGQuR8DV_8Rh602e9O2CiFjiVYJuSCkZ5O_VhqXj0JuyY1u5yW0D0SBJWIPdS_7eFH2yVWA9Gt2EsNuKSnLGtB6rk0g2o6ZLmuuExP4q_fSyOZk7ujcsnWdTO7uft_yvd8-GCCCgAaWovqQU76UhNWLSdgXlGq_XDP-pw65j2FD51sLL0qxK7HzdV8cgyKN5EYVs-NJWRGdNo2VC8jFjC4SrCl7mIIw3r_9DsH3rZKy4QT6Ia0HB5FNORicSr584hoBGUAA1cQgQjGjzeiINhE1gTMqWPY40X9F69V_B4UqUa4NU_JiWpwboq-DL6mzBvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8466606615.mp4?token=cM9wOKEf4nwVbgdtY4gtGQuR8DV_8Rh602e9O2CiFjiVYJuSCkZ5O_VhqXj0JuyY1u5yW0D0SBJWIPdS_7eFH2yVWA9Gt2EsNuKSnLGtB6rk0g2o6ZLmuuExP4q_fSyOZk7ujcsnWdTO7uft_yvd8-GCCCgAaWovqQU76UhNWLSdgXlGq_XDP-pw65j2FD51sLL0qxK7HzdV8cgyKN5EYVs-NJWRGdNo2VC8jFjC4SrCl7mIIw3r_9DsH3rZKy4QT6Ia0HB5FNORicSr584hoBGUAA1cQgQjGjzeiINhE1gTMqWPY40X9F69V_B4UqUa4NU_JiWpwboq-DL6mzBvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بازسازی مرکز تجارت جهانی: پیشنهاد من این بود که دو ساختمان یکسان ساخته شوند، اما ارتفاع آن‌ها را 10 طبقه بیشتر کنند.
🔴
به نظر من این کار، یک اقدام عالی می‌بود.
🔴
آن‌ها این کار را به روش دیگری انجام دادند، و این مسئله قابل قبول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/146942" target="_blank">📅 22:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146941">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb351c81b.mp4?token=uBa93Uxfbf8-NTjEcixxY56RbP6hk1vN-B_o9PTSfkbj0D4KYGzsx-A7iR_BcZHCH4nlM-QFGE__AjgHeImbTz4-VUPPx4dkJB0K5cOkU3HEX1GuItXHnQHnmfIo8zDRRhKyEL-Hm8pePk_-uO_Lc5e98szNIaSbimucA5mnY8dweTrIPQUNbXsbY-FsaQUxW-8CSCV9UcvctTbrNAOZCMlV7rTN8KR2ZdhmIvUynTIAryGBGxzQtx-q7dbtZADw7qMnjkjGLLFgGXX-821eoznkBGmI2sVgDADUn2eGF18S7mNsreNO2Bq6uG5Pb39T5b8kTqroyOwoqPIsyfT67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb351c81b.mp4?token=uBa93Uxfbf8-NTjEcixxY56RbP6hk1vN-B_o9PTSfkbj0D4KYGzsx-A7iR_BcZHCH4nlM-QFGE__AjgHeImbTz4-VUPPx4dkJB0K5cOkU3HEX1GuItXHnQHnmfIo8zDRRhKyEL-Hm8pePk_-uO_Lc5e98szNIaSbimucA5mnY8dweTrIPQUNbXsbY-FsaQUxW-8CSCV9UcvctTbrNAOZCMlV7rTN8KR2ZdhmIvUynTIAryGBGxzQtx-q7dbtZADw7qMnjkjGLLFgGXX-821eoznkBGmI2sVgDADUn2eGF18S7mNsreNO2Bq6uG5Pb39T5b8kTqroyOwoqPIsyfT67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: سیاست، شگفت‌انگیز است. شما با برخی از فاسدترین افراد دنیا ملاقات می‌کنید، و همچنین با افراد فوق‌العاده‌ای نیز آشنا می‌شوید، اما در عین حال، با برخی از فاسدترین افراد جهان روبرو می‌شوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/146941" target="_blank">📅 22:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146940">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/40e05b07a0.mp4?token=n7HIaoijP1LC9Yz5jWWAV2ex4Ddk7JE-T9gPqEwk469wXAx4bmkd0vpV0LyYxzT8E45ugUEjP7Pc9268vWyZ5pHM745wyrbNX9eT4Ar5RP_gyYA-35E4VSgO2xPrI-437YB63ehVmyC9uiwyhSRt850TH2V2Z9eK_y82PhQGZOXe6HseKXkXAN-FPrx1h50DGkcrBS6qfOlEHmkS7HiS2lukBUo6zVxMJKepE06jYsG1aG0SASbLsjjzXSJuyYjcvgVnLrWo8nSURhpZ1EkgSqXlD6gqD0jBKElkJxVwyhfk_-ePHKUQgtztV1tS4DTHzxBouqXj5wxof2jL7fvuiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/40e05b07a0.mp4?token=n7HIaoijP1LC9Yz5jWWAV2ex4Ddk7JE-T9gPqEwk469wXAx4bmkd0vpV0LyYxzT8E45ugUEjP7Pc9268vWyZ5pHM745wyrbNX9eT4Ar5RP_gyYA-35E4VSgO2xPrI-437YB63ehVmyC9uiwyhSRt850TH2V2Z9eK_y82PhQGZOXe6HseKXkXAN-FPrx1h50DGkcrBS6qfOlEHmkS7HiS2lukBUo6zVxMJKepE06jYsG1aG0SASbLsjjzXSJuyYjcvgVnLrWo8nSURhpZ1EkgSqXlD6gqD0jBKElkJxVwyhfk_-ePHKUQgtztV1tS4DTHzxBouqXj5wxof2jL7fvuiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌های نظامی ارتش ملی یمن، تصاویری از حملات هوایی مشترک یمن و عربستان سعودی را منتشر کرده است که اهداف آن، خودروهای وابسته به جنبش انصارالله در منطقه ضباب و مناطق جنوب غربی یمن تحت کنترل این جنبش بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/146940" target="_blank">📅 22:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146939">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LURPw-PysA9nZWqSfbd7njuSsYEI740j-MIkl7-IusMknvThEd0g-0Ceh5klOT3nHvSwuMBpVVCLNu0EIEvsk5Ym4htZf6A6tzJO5Ne7nX_O_OgL2BQZ-m-2M99ZtJD527uI2PeOVvyDGxULx3Ij4uu-Oe0Ec9LMU6w95xcM9dlknEHsOgV2VXAwMT8L17rgfquJcgh7W8H6_C3jCnplAHyHfohbV9XjEflDS08x4tIPawVp4g9BjE3y0UdM-fQlI6X3PC8XylhWRtMJsCiQlWyKwqK5NSIwMn_biEj01qiBKWGs-Pd396u90j9uZVN1Q5uMZbGIcSe1JIVQ1_L6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : بخشش ۵۰۰۰ دلاری ترامپ"، که به همه بزرگسالان در ایالات متحده تعلق می‌گیرد، به این دلیل ارائه می‌شود که کشور ما میلیاردها دلار در زمینه توسعه اقتصادی، سرمایه‌گذاری و موفقیت خالص به دست آورده است. این موضوع از سوی "دموکرات‌ها" مورد انتقاد قرار می‌گیرد، زیرا آن‌ها امیدوارند که این اتفاق هرگز رخ ندهد - اما این اتفاق خواهد افتاد!
🔴
به عنوان مثال، دموکرات‌ها در مورد "قانون بزرگ، زیبا و باشکوه"، یکی از بزرگترین قوانینی که تا به حال توسط کنگره تصویب شده یا توسط یک رئیس جمهور به قانون تبدیل شده است، این ادعا را مطرح کردند که این قانون تصویب شده است، در حالی که دموکرات‌ها می‌گفتند که تصویب آن غیرممکن است. یا "هدیه ۱۷۷۶ دلاری" که سال گذشته به ارتش ما دادم، تقریباً از همان ابتدا با مخالفت روبرو شد. همه می‌گفتند که این کار امکان‌پذیر نیست، اما این کار انجام شد. سربازان وطن‌پرست ما این پول را دریافت کردند و از آن راضی بودند.
🔴
وقتی من چیزی را می‌گویم، منظورم را کاملاً می‌دانم. بخشش ۵۰۰۰ دلاری اتفاق خواهد افتاد، زیرا مردم کشور ما شایسته آن هستند. به حزب جمهوری‌خواه رای دهید - و آمریکا را دوباره شکوه بخشید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/146939" target="_blank">📅 22:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146938">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مدتی پیش، هواپیماهای جنگی اسرائیل حملاتی را به مناطق قانترا، المنصوری، زبکین و نباتیه الفوقا در جنوب لبنان انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/146938" target="_blank">📅 22:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146937">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc6c5ed95a.mp4?token=Ye44oxtYfu9yY8Ibbp-BZGJYybyXY8VOvNgSCI_Su6v3aTmioyJu9qiNs90KNUJzuPEgktX6O1RIyPOL0-Fdr84tmpne8SOwfYFPTxo2FQWK7HzdYvqA_9XHrZt8ARju_McSTEqxefOjg0c8Lsqymr1RpsV2XLsRvJH_dd5yNlpZX9PFRXWsI5Yd4bXHA5EG_irSGDRgtmDM0VVCLV928_ByBVEUk0RvSbC8Cu5xzpyqmff9oYl2RgXMCu7qgqWsI4gMhoBAAscahKwnDFUGrR5G_DwN3dJUGgg5ikV1KJ7GlP3y1EerAuKeIktoTwYzNkCDdX5ZflHykG6SnHBMsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc6c5ed95a.mp4?token=Ye44oxtYfu9yY8Ibbp-BZGJYybyXY8VOvNgSCI_Su6v3aTmioyJu9qiNs90KNUJzuPEgktX6O1RIyPOL0-Fdr84tmpne8SOwfYFPTxo2FQWK7HzdYvqA_9XHrZt8ARju_McSTEqxefOjg0c8Lsqymr1RpsV2XLsRvJH_dd5yNlpZX9PFRXWsI5Yd4bXHA5EG_irSGDRgtmDM0VVCLV928_ByBVEUk0RvSbC8Cu5xzpyqmff9oYl2RgXMCu7qgqWsI4gMhoBAAscahKwnDFUGrR5G_DwN3dJUGgg5ikV1KJ7GlP3y1EerAuKeIktoTwYzNkCDdX5ZflHykG6SnHBMsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: امنیت پایدار خلیج فارس تنها با همکاری کشورهای منطقه ایجاد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/146937" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146936">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WkSH3Unri9jv7I4WxGqqeDOMtcBGg1pz1Ij8ICL1oP_XpTqvWS47-5TrdgbcLAi0LTln2QN7pAnMtXrsI2bYu_-4nrsTfRomGYd-qah2erfYTTgplTcElenTQsMKmXpsEaaU5gzCMz4hHHvh7z_vgo2fdM0rlCXNByohiySH4WOHXyMLlVJuS_QeWTRn0ulSJsTygYiXdcuRcPYmwav-weGn3QaeYsbNdCMBk-HzgWu0uv4arGVt7Tchrs8wAssfK9-bU4KnZX379655FY0oSSngIcLTKF81MQAPcbmwylgDu9Sa_nt3tVpISbYSaGoYqAkMjAtSxGriFwxsRJjzAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاکستان درخواست عربستان سعودی برای حمله به حوثی‌ها را رد کرد
🔴
پاکستان می‌گوید پیمان دفاع متقابل مکه «شرایط از پیش موجود را پوشش نمی‌دهد»، بنابراین فقط جنگ‌هایی را که پس از امضای پیمان آغاز شده‌اند، پوشش می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/146936" target="_blank">📅 22:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146935">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/146935" target="_blank">📅 22:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146934">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما در وضعیت نه‌ جنگ، نه‌ صلح نیستیم؛ ما در وضعیت جنگ هستیم
🔴
تحریم و محاصرهٔ دریایی به منزلهٔ جنگ است و هر آن‌چه که ما در این وضعیت انجام می‌دهیم نامش دفاع است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/146934" target="_blank">📅 22:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146932">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImbOXWU9cuqghMCitOJlrSRE6kmvcMC6vQ21Qa8mexPnNcKkL56Hp-QwauPHWk3OaGjphVdDDkBWsQ9b5VlHN0SqPCI1RNp4tPKTbZud_JqGunZmEL2L7xuTKtwLAaG-QpxgS8hLCVWNiZ6Ak8FyGAataC4Y-Y3qjD5k3UmsoZ1HBlW7NUvKHcbJckFWJzkcgcM2l6OHvRdF06eNhk3uudX280tbZ4hohuZ9-bwzPFYd4M8CzZ8vzDUpTqR9TwdUeLrmsblxqFqOjvq-eSEh8qb-cj7gYrutXJzBmA4NV7K0ubn1Wkc1pBKPi2gRIaNdpeujVK0dUeBG16uW4YzP6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سلیمان العساد، که از اقوام بشار العساد، رئیس‌جمهور سرنگون شده سوریه، است، توسط نیروهای امنیتی لبنان در جریان یک عملیات ضد مواد مخدر در دره بقاع دستگیر شد.
🔴
دولت سوریه از دولت لبنان درخواست کرده است تا اجازه دهد او به سوریه بازگردانده شود، جایی که به ارتکاب جنایات جنگی و قاچاق مواد مخدر متهم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/146932" target="_blank">📅 22:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146931">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
معاریو: نتانیاهو پیشنهاد حمله نظامی مشترک با کشورهای عربی به انصارالله یمن را داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/146931" target="_blank">📅 22:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146930">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvLX7KtOHPzijfTokMVzoElHlJu0mHA7DJ28ZppLYVvXB8htiNIMpR1lPxWWc8mWEkCGfBcAvBQmetOmaE7lGbSNbY9N-0eqlI16ABJ_Khcm0o7guKKrh5zQuT4YtAMWBf3vS5-2DFB5RNpeq2KQGq7zzjmxtbhCAUgTjW76nfnXXjn8cg-QotDHki1u0qJAyfqqqYWn3RcXsWVB9k8yr9cKmX0XE4kC6_tpOeaBMo2tKd7ymvIjzQTbO47AQQD5rUtMssUUOBKPXCpRK4nmYsvefOjnlVF4a3GYJfWpMudW04-juEH-AVrpoDgcQN4tljqBnx-vEvY_Qdb8n1u6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نه نفر از خلبانان سابق نیروی هوایی سوریه، که در دوره حکومت قبلی بشار اسد فعالیت می‌کردند، توسط نیروهای امنیتی سوریه در شهر لاذقیه دستگیر شدند.
🔴
همه آنها به اتهام بمباران بی‌هدف مناطق مسکونی در طول جنگ داخلی متهم هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/146930" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
