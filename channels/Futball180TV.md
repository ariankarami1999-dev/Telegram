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
<img src="https://cdn5.telesco.pe/file/n4rxAIpbi3a270GR_k1zoKXdIz3ujaV0dzUoEYW-anVbR6QjJl65uVGEdk6LbzkoLfEbYRdxKFxHUa_IcuhfNVflWoLbLu2rUNyfabDQMPaPRAOI6ej8tNVELaZe7s24YyMwkzUvFBxooNWFCsFQwI4JjhZHYJWlo9G1VnT1HRVDh-G-nLg7xjsizSY_cu7tMcdOpNCE9TropFn59btkKN69_L7eu0HeeXBQOTx3PDlDru8ke-wlr0QfJQh593kYGt_L0LqStJ_mJulKQipr7zTzpkmgIDRAsZo8h8gQ1cSWS8P5ypM9SkSZhhsDWlE0GCu3dgX4tVj4ACtnIaFALw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 390K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 22:44:37</div>
<hr>

<div class="tg-post" id="msg-107951">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=uu8FTzYe4WAY8zv0tJeXsCnOUCx9E759S4tc30FKh6s7N1OaMU3aoO3WTl6uGJqefKTaJf7nCCou7DRO-AyF6zNAndBsWlXZF3Qvora805Wiyls420YfLu1mXil03cQh1fE4SkYOHb08sj6myiipSnLLHzKxiYiLil9Ki4cjrgqDPFi3EArC-V7KIizOG_UnzUrc4pvWq-AIvvs7OyKSwPfbmZbhpsMBRA0yu3kadHf7OgHLrhiM8kcaZIu8onSWFdv_fYvr8n00loHDNvvp2h-UHCn6ZmQmqW7ahJ2fbICB5iXhVOvrDPmn5KmUTm2yN8cu81dP2aNMCLMJ5iKGQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=uu8FTzYe4WAY8zv0tJeXsCnOUCx9E759S4tc30FKh6s7N1OaMU3aoO3WTl6uGJqefKTaJf7nCCou7DRO-AyF6zNAndBsWlXZF3Qvora805Wiyls420YfLu1mXil03cQh1fE4SkYOHb08sj6myiipSnLLHzKxiYiLil9Ki4cjrgqDPFi3EArC-V7KIizOG_UnzUrc4pvWq-AIvvs7OyKSwPfbmZbhpsMBRA0yu3kadHf7OgHLrhiM8kcaZIu8onSWFdv_fYvr8n00loHDNvvp2h-UHCn6ZmQmqW7ahJ2fbICB5iXhVOvrDPmn5KmUTm2yN8cu81dP2aNMCLMJ5iKGQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
سیل هوادارای مسی برای خداحافظی در آستانه آخرین بازی مسی برای تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/107951" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107950">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d806496fdb.mp4?token=KFwvggMLKxJIR6X1AOKpptiKVrHkmE7OFGgAH3zcDnk90Wp2JnBHalVSQsFRNlNOvZxQXbk4WmvhICrXzDaHBpBEDhij3csJaNgDwD4YSE83m-8T5IkcZISignNQ1Kd2BNoD3K4PXlGn_dWc36O7bB47xxQwpUz6jMUUDcjNw133ys0-lnDzfy0bj8Jn4dk_aNU7YqZXoS61zHB0nCVltc2fmUOtavRyeMbxFUMAsH-FbBLDNaPnqON7-Mcbi-pBxLOpIrAOQP1OqPxxSTmU1A3UxnQXGdO8i5p4cZPXeWcE-4lNzRMVmLfBO5xRGWSSuCoCtx2Q2H6y1G16g8BrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d806496fdb.mp4?token=KFwvggMLKxJIR6X1AOKpptiKVrHkmE7OFGgAH3zcDnk90Wp2JnBHalVSQsFRNlNOvZxQXbk4WmvhICrXzDaHBpBEDhij3csJaNgDwD4YSE83m-8T5IkcZISignNQ1Kd2BNoD3K4PXlGn_dWc36O7bB47xxQwpUz6jMUUDcjNw133ys0-lnDzfy0bj8Jn4dk_aNU7YqZXoS61zHB0nCVltc2fmUOtavRyeMbxFUMAsH-FbBLDNaPnqON7-Mcbi-pBxLOpIrAOQP1OqPxxSTmU1A3UxnQXGdO8i5p4cZPXeWcE-4lNzRMVmLfBO5xRGWSSuCoCtx2Q2H6y1G16g8BrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول کرواسی به اسپانیا توسط ایوان پریشیچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/Futball180TV/107950" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107949">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گگگگل کرواسی یکی به اسپانیا زد</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/Futball180TV/107949" target="_blank">📅 22:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107948">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfAQ39ziWxC5H3R_BRMLwlSLtEPrI4y1OyzbUHUTfISDmVp3Q-H8XkVV_wyv5nSiyfjSgLVlC37Kibi5PcKEsyDDEYyziRV8V-fsY5Z8jbHZyyWs4yMKEEqNtKPny5BOjLS2o1_lbffzx_GAOIsFWp13aIU7x9c2jArI8VUQaOroPg18OAH0RBtxzG0wS4V2SiUwGwSpjQhWxdClviflpdw1gaKdCkrsy509kdcqapIOnglrK6lxFDyLTz2XnTwViQgewzPjjEybuTvGKRlqwcMEzWZo6_xG5IyMdbBZ_Trh8bbkCfhh12X51F1mmucg89n2hLVsl3SKDReO6-u1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
خلاصه‌ای از بیانیه کریس رونالدو:
🔻
رونالدو تأکید کرد که مربی قبلاً با او توافق کرده بود که در یک برنامه مشخصی برای بازی‌ها شرکت کند، و بازی با نروژ در این برنامه نبود. سپس، به طور ناگهانی از او خواسته شد که برای بازی 30 دقیقه آماده شود، و در نهایت، با وجود…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/Futball180TV/107948" target="_blank">📅 22:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107947">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🇵🇹
اسطوره رونالدو:
🔻
بابت ترک‌ناگهانی اردوی تیم‌ملی از تمام بازیکنان و مردم پرتغال عذرخواهی میکنم. من به عنوان کاپیتان تیم مستحق جریمه و مجازات بدون هیچ تخفیفی هستم
🔻
همچنین به مردم می‌گویم که اگر شرایط ادامه حضور داشته باشم قطعا دوست دارم برای کشورم بازی…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/Futball180TV/107947" target="_blank">📅 22:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107946">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxCnr_P2f3BE6dKCbxI9bninHvhRmPNF4pZLFMdkVAVAm2f4gaebv9WqZf0sGHGcACyTaec0iN0sE_SBo3CEG2Gws_LVDpx4hFR8nTKDqNzXZGxS-S2H3RzwxIbxQtdMIOeGNYiTahZQXsXbynZqYod_t4gz1OHbRuLb9lF_fSiAwfW91u9R8lfBgxnrcezB_z9Q_q9xPEqS4QCVJEz0XiQPj8CifjXyM719bfahxlA-H6MKjUAmQ1NCmQiR6_CAPAv793FIQjL1aIfcBZRShVD6O5gH77YPoPROhTuiMJHrAyX6V3H-JiDXhQrcNrv3l23TcAYndyuq8N58Y47CFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره کریستیانو رونالدو:
🔻
جورجی ژسوس برای اولین بار با من تماس گرفت و گفت که مایل است به صورت حضوری با من ملاقات کند. من موافقت کردم و قرار گذاشتیم در پایان تعطیلاتم با هم ملاقات کنیم.
🔻
آن روز، مربی به من گفت که به من اعتماد دارد و حضور من برای…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/Futball180TV/107946" target="_blank">📅 22:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107945">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بیانیه‌ کریستیانو رونالدو:
🔻
بعد از جام جهانی 2026، من پیامی برای مردم پرتغال آماده کرده بودم که آن را تا امروز نگه داشته‌ام و آن را زمانی که به طور نهایی از تیم ملی خداحافظی کنم، برای آن‌ها ارسال خواهم کرد.
🔻
بعد از مسابقات، رئیس فدراسیون فوتبال پرتغال…</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/107945" target="_blank">📅 22:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107944">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
بیانیه‌ کریستیانو رونالدو:
🔻
بعد از جام جهانی 2026، من پیامی برای مردم پرتغال آماده کرده بودم که آن را تا امروز نگه داشته‌ام و آن را زمانی که به طور نهایی از تیم ملی خداحافظی کنم، برای آن‌ها ارسال خواهم کرد.
🔻
بعد از مسابقات، رئیس فدراسیون فوتبال پرتغال از من خواست که با تیم ملی به همکاری خود ادامه دهم، و همچنین از من در مورد انتخاب مربی فعلی نظر خواست. من به او گفتم که این انتخاب، گزینه درستی است. بنابراین، از انتصاب او خوشحال بودم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/107944" target="_blank">📅 21:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107943">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9MBj0Xg8l15bIPDsRj22l1CYySp-RSpjsOMw3y-6gk3GlNe0_36xOvNU117W-TLJ8kz6F0n0kI-5qpxlCUmmaVjgcek-FJ-VWVz_FCpWaEWNwPm-Q6KXrRataR9Rxj96-wju9WtlkdvL9G8bRq_CpkVDzyaYSqP-KRbHesqMS3VtOsFM_okTLDO8lEX-LpO1IehVvIa2aGeZhR1yymbv5E5FM468SQttr1UdlK3mfvBvlEP8dzoHwv1esLUYd20p8dSpXqiZvKNGOs-olgCM5Xp8wcpgs-C5gVicANV4CvZBXnKgBrfrDTymwCNEPJPVFD0d4NRW3PFvPcoI7fZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/107943" target="_blank">📅 21:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107942">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8036043b2b.mp4?token=ZuZLjGA2SphOnmm8srMWzM2vcpZPqT-QCIsHMx_xnCE6sJPxNl-U0z8kz7OWm75N9cuS1QFhwIW4AmbZIghkfe8aQ8Wz7ljFJ3W3L-M5tNWKiLSHs82nDxC4BFRikeq2SnQwhKS8ZAtYyWyu_6T9pqvaXz6LiXUoN0RY3r3nKYQQUGjntUeZHnHFleuJwCxrFFeuyI-iRrIKyh74As3fDBRg6O9mtlyM0XZK-Uv9B-z6o2rHjNmT5UNmbhEissQn-HymnNpQpPWUOXWVkwWlBB0abz7hSjz8oEaHYl30NE2-7NlHoiVBzIe-ZMFvEuE1pnukZx_O8muQgRc4ROHgTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8036043b2b.mp4?token=ZuZLjGA2SphOnmm8srMWzM2vcpZPqT-QCIsHMx_xnCE6sJPxNl-U0z8kz7OWm75N9cuS1QFhwIW4AmbZIghkfe8aQ8Wz7ljFJ3W3L-M5tNWKiLSHs82nDxC4BFRikeq2SnQwhKS8ZAtYyWyu_6T9pqvaXz6LiXUoN0RY3r3nKYQQUGjntUeZHnHFleuJwCxrFFeuyI-iRrIKyh74As3fDBRg6O9mtlyM0XZK-Uv9B-z6o2rHjNmT5UNmbhEissQn-HymnNpQpPWUOXWVkwWlBB0abz7hSjz8oEaHYl30NE2-7NlHoiVBzIe-ZMFvEuE1pnukZx_O8muQgRc4ROHgTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
حمله تند خداداد عزیزی به مدیرعامل تراکتور حجت‌کریمی بابت مصاحبه دیشب در فوتبال برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/Futball180TV/107942" target="_blank">📅 21:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107941">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a98f55b4.mp4?token=SNTpbP1lMwXGLjxhtAO7Nmc3Z8BohGlKw0Z8guwIOD-MIfGV9YHBSdd4SPdzeUDXwuthXQWaO-UChQOrWIfQEvdYmoD_tXstCMe2FtM5TuEsqhPuXtUQxMJSs3H1YUY0jil0TyT1EDI8RtDUPkfGMXrd0kO9bGq3Wbrd1hbd6SfVJrpAFUKEYIgFp5FZWM-GkCo5pQsvPqHyBPI8wUoCIpiGyUdcRpw48RSv_ruYz8u2MefM_WTHHVM2mXCdf5Up6an5xndq5lyZrf3Qw5LoLy62phmqy9UmNItDUHhjQWXavryO7Xp1_AJeElke7B0PTV3t5VstydwsJWmwMDoWnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a98f55b4.mp4?token=SNTpbP1lMwXGLjxhtAO7Nmc3Z8BohGlKw0Z8guwIOD-MIfGV9YHBSdd4SPdzeUDXwuthXQWaO-UChQOrWIfQEvdYmoD_tXstCMe2FtM5TuEsqhPuXtUQxMJSs3H1YUY0jil0TyT1EDI8RtDUPkfGMXrd0kO9bGq3Wbrd1hbd6SfVJrpAFUKEYIgFp5FZWM-GkCo5pQsvPqHyBPI8wUoCIpiGyUdcRpw48RSv_ruYz8u2MefM_WTHHVM2mXCdf5Up6an5xndq5lyZrf3Qw5LoLy62phmqy9UmNItDUHhjQWXavryO7Xp1_AJeElke7B0PTV3t5VstydwsJWmwMDoWnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
افشاگری بهداد سلیمی از ناداوری در المپیک ریو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107941" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107940">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8dd97c34d.mp4?token=JBhacZ9SUJ2a41p6V7nAprn6IpaJY8zd5xZPLQGC153LP_0gHbsSimTyj0CCAHwX2b_2b8bo4eqeuLvqY_ybZewK5Kz4NPNtQmSt8-uSseXuQzSGOix3G61G9hPauqYa2Y52FS6jG6YwHKUd_cnA-DD6VozjQHQ5dXkeOnGXpE2Iu9PJawnGmIKAg5ZExqKUY19x2djmPw1DbgFLIxicgeKaE7FskzZEstspcVPU7G4jiXFljG1FTMyju2IFlteOSpkK7bfUu0RgwG3hmV4bNCaqs4jS-eH9ZVMD3vggL1Q7YhQwnFrUcKXqTc9RuFx_eVg9tcJdOI8DBsj0hTn01Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8dd97c34d.mp4?token=JBhacZ9SUJ2a41p6V7nAprn6IpaJY8zd5xZPLQGC153LP_0gHbsSimTyj0CCAHwX2b_2b8bo4eqeuLvqY_ybZewK5Kz4NPNtQmSt8-uSseXuQzSGOix3G61G9hPauqYa2Y52FS6jG6YwHKUd_cnA-DD6VozjQHQ5dXkeOnGXpE2Iu9PJawnGmIKAg5ZExqKUY19x2djmPw1DbgFLIxicgeKaE7FskzZEstspcVPU7G4jiXFljG1FTMyju2IFlteOSpkK7bfUu0RgwG3hmV4bNCaqs4jS-eH9ZVMD3vggL1Q7YhQwnFrUcKXqTc9RuFx_eVg9tcJdOI8DBsj0hTn01Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
علاقه‌خیابانی به گزارش بازی آخر لیونل‌مسی در تیم‌ملی آرژانتین که بامداد فردا برگزار میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/107940" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e0f6c80a.mp4?token=RSGxZO9f4UhvXq95V8_lGEwMA7x5pvU2hupdpTE4lNbDUC5MO-qR-jJh7lTHPLFvuWJK37YniIVcQrVNqY3i54m--9GN4o0I_hr_aurqqdtS8oXYPOQkETyD37uL28Mx2i9eAgjcsoh3IMlsy89o3D_ylLUF_GqtdljDn51OIDoqG2BfDtYejVpgqKxbg-2-b2K6jG5e2qpfqTRtamXzKP0O7dZjawfgb-rlj0RHYJwRD20EyhkmSQEZ9FdfaaUelmgORJXpDhnJs_yC9Eoy05ujt2Hzsq8olELUSWR0L4AF8JonUciauKkwNOl_dpQSyfeVtGj8OxzFoYYTC_AWNCNn6jZbdXpfgi9YtQYI7voVh3pxZCbev7ijFHCYdjzBY8B_r6zVnc-dHpLu1dkmB6f43UeEk8inPmUa6dU5sl85fRqpTNRQErVJWXkrXF7SM05FcioBBp-7PbCfOg9AzVr74lo-mHDpw4ZG8BXxHI6o7qCJyS19nO06co_7icgai9uz3iZqY2ZMzReZTWzZ9rGN0rbEZr02dVsnWgpr-qF01-SKpYftr1sb1qTK1SWlYCh-IaiqfxlrQDqd6es8VgoZmpamN85pZjgNwR6L4AKRsFFv5SeJZQgtFsHSIcTOBSVPuaeQGVL-N6e69r8nPE8EaUuWd3ZPNqfN0ruQsKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e0f6c80a.mp4?token=RSGxZO9f4UhvXq95V8_lGEwMA7x5pvU2hupdpTE4lNbDUC5MO-qR-jJh7lTHPLFvuWJK37YniIVcQrVNqY3i54m--9GN4o0I_hr_aurqqdtS8oXYPOQkETyD37uL28Mx2i9eAgjcsoh3IMlsy89o3D_ylLUF_GqtdljDn51OIDoqG2BfDtYejVpgqKxbg-2-b2K6jG5e2qpfqTRtamXzKP0O7dZjawfgb-rlj0RHYJwRD20EyhkmSQEZ9FdfaaUelmgORJXpDhnJs_yC9Eoy05ujt2Hzsq8olELUSWR0L4AF8JonUciauKkwNOl_dpQSyfeVtGj8OxzFoYYTC_AWNCNn6jZbdXpfgi9YtQYI7voVh3pxZCbev7ijFHCYdjzBY8B_r6zVnc-dHpLu1dkmB6f43UeEk8inPmUa6dU5sl85fRqpTNRQErVJWXkrXF7SM05FcioBBp-7PbCfOg9AzVr74lo-mHDpw4ZG8BXxHI6o7qCJyS19nO06co_7icgai9uz3iZqY2ZMzReZTWzZ9rGN0rbEZr02dVsnWgpr-qF01-SKpYftr1sb1qTK1SWlYCh-IaiqfxlrQDqd6es8VgoZmpamN85pZjgNwR6L4AKRsFFv5SeJZQgtFsHSIcTOBSVPuaeQGVL-N6e69r8nPE8EaUuWd3ZPNqfN0ruQsKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ترویج دروغگویی به دستور فدراسیون و کادرفنی؛ لو رفتن ماجرای تعویض زودهنگام محبی مقابل روسیه در مصاحبه احسان حاج‌صفی؛ ناراضی بود، گفت بخواب زمین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107939" target="_blank">📅 20:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc57e60057.mp4?token=r8OSTaxAKFNP1iKlz4Dx0A4ozULUZM1rfruvEopc7YO9THreKrQ_gINyrSKu3WEM-GS-_4JfGEJUn82JtHl1Q7Po7N-M0UeshlmdXMH8jok3E8KTdzpx96KMAN3BKeuGnnRIMEPwYvfbocA3oiK3g-oE_tFx9X0xofsj_1DswLEg991jg3YcmT9h1I_xrMwrn3HmQ99EsSj2DWiMzSFZqfHzpZHFxWl2ktmCYeui2MOAyebU4UMYdvyBG8fznHAFtWL37YTudOsp-mMnpEylcJJOOzrMRnfkmSFW_AMeKfOktYSit-o03-TlndPrHIQvwY5ZbR6Y3-8VrxJ63q94jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc57e60057.mp4?token=r8OSTaxAKFNP1iKlz4Dx0A4ozULUZM1rfruvEopc7YO9THreKrQ_gINyrSKu3WEM-GS-_4JfGEJUn82JtHl1Q7Po7N-M0UeshlmdXMH8jok3E8KTdzpx96KMAN3BKeuGnnRIMEPwYvfbocA3oiK3g-oE_tFx9X0xofsj_1DswLEg991jg3YcmT9h1I_xrMwrn3HmQ99EsSj2DWiMzSFZqfHzpZHFxWl2ktmCYeui2MOAyebU4UMYdvyBG8fznHAFtWL37YTudOsp-mMnpEylcJJOOzrMRnfkmSFW_AMeKfOktYSit-o03-TlndPrHIQvwY5ZbR6Y3-8VrxJ63q94jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😱
بدون شک این عجیب‌ترین پرونده فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107938" target="_blank">📅 19:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107937">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
⭕️
طاعون روسی دومین کشته خودشو ثبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107937" target="_blank">📅 19:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZiEIv3R4a1TYeN-RpVLEH629MJ6aHSm--tBlRHaUErvAwgA8hnQE-mH-I_DgCu8vgsgehc31lrJhv8TTu1Tzd__9F2XNLVFY0GiRFPnsA3-dYWyHwG2k0Xx2Uh2inbLY9ZSMGvf3sYyWuzV1-nmbPdRnbtGMPgkjz5XJ5w7iLnEIFOPvzKobQYKyKvnokMI7ZNEPdjWJmoWZiiSAPTKFdl4DfqWatCVIm_yUAmfXHICDGIRj5FbBaUzfIMnjGWKzGlY6xTniVkIe94x1Wbwm5A77YXnwOeN97wPclko6dbvalwc5mK3APTd6mbuGug5KcidqtR2bSbrWIM6AvuOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
طاعون روسی دومین کشته خودشو ثبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107936" target="_blank">📅 19:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5d14acd5.mp4?token=Q7fTXpXBJ8UxMwUYW4DmDlWuSF5c11Xx9soy10-i9qKeUsIr682bt2Uul_L3nasPktt3G8IqJNGw9cBim0QkCZM3P2Y5u6Iu9CXdxxNJ-JFZSxzA9Z3PnASJjvZPM182Ejza21ZCr77dE3ikmIbQK26H1IMRjK3H5nG0KT4yeM20fPDLqyATjEBWYrReMsrwKLCQdRCkVLsro-Uo4m2E9Z69pANOtEQtWCS7aA5HiaY9ymW3_lKVv43ynknp-ES4kJBJKd_M1kWdaDLViLN2fdkOHj31UOF1B4F6fqvVYjJZshNiuc1HqR21IIrfPwxI7bckSOmFtVZsk1RAnxw7Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5d14acd5.mp4?token=Q7fTXpXBJ8UxMwUYW4DmDlWuSF5c11Xx9soy10-i9qKeUsIr682bt2Uul_L3nasPktt3G8IqJNGw9cBim0QkCZM3P2Y5u6Iu9CXdxxNJ-JFZSxzA9Z3PnASJjvZPM182Ejza21ZCr77dE3ikmIbQK26H1IMRjK3H5nG0KT4yeM20fPDLqyATjEBWYrReMsrwKLCQdRCkVLsro-Uo4m2E9Z69pANOtEQtWCS7aA5HiaY9ymW3_lKVv43ynknp-ES4kJBJKd_M1kWdaDLViLN2fdkOHj31UOF1B4F6fqvVYjJZshNiuc1HqR21IIrfPwxI7bckSOmFtVZsk1RAnxw7Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
کنایه‌های ژوله به مصاحبه‌ اخیر قلعه‌نویی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107935" target="_blank">📅 19:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a828a3618.mp4?token=UFnHro4OOn5kKFHdp43sMNc36Acexo3hEXmqaTSY2VyCvN1jf33Fr81DGD44LoD017sCfNycIO5dmOn4VCSAat7YrCTY5V1yVkJpqEvW8H65H2smU37Kpi5H5q8bXBrQagU2OM2SlcFUIiOex7k_7f5FPqkl6TPhXmI0XTsYap_z2zMjkrvwpU3Gg5xr-KjDldyKRmqm-99qRutFqnwkwbrxyC2E7Qm2cWxnRQqK34KtqbQM4G3_eba3zusbfck0-DSXwJVbkhaKkeHGPZY1iUAJk1y9ZGMGgh4jMlP2TAlFQTGQOPewXyTBTWBu8V0ZqN1_F79bdfBzVThjHu3dCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a828a3618.mp4?token=UFnHro4OOn5kKFHdp43sMNc36Acexo3hEXmqaTSY2VyCvN1jf33Fr81DGD44LoD017sCfNycIO5dmOn4VCSAat7YrCTY5V1yVkJpqEvW8H65H2smU37Kpi5H5q8bXBrQagU2OM2SlcFUIiOex7k_7f5FPqkl6TPhXmI0XTsYap_z2zMjkrvwpU3Gg5xr-KjDldyKRmqm-99qRutFqnwkwbrxyC2E7Qm2cWxnRQqK34KtqbQM4G3_eba3zusbfck0-DSXwJVbkhaKkeHGPZY1iUAJk1y9ZGMGgh4jMlP2TAlFQTGQOPewXyTBTWBu8V0ZqN1_F79bdfBzVThjHu3dCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پادشاه مسی:
🔻
لحظه‌ای که منتظرش بودم بالاخره رسید، با خیال راحت میرم چون هر کاری از دستم برمیومد انجام دادم، این پیراهن برای من فقط یه لباس نبود، رویایی بود که بهش افتخار می‌کردم و تمام زندگی من بود. ممنونم که این‌قدر دوستم داشتید، همیشه شما رو با خودم خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107934" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107933">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxBoewIqYkv6nZ5EuWYejEPKYTXuyGPwy0BIFpR1trY1gMaWvIu_WK4kOTO3T52OHZDs7LkG5D-0v9U8PrEE7PuFe8sGs6Pacfqnh15Q40VfEG6EZpfIhjRbBDYqhDYzecLn5bpUrG9aEmAzwZRUOE-1HCpivdmd8iBwGbR8vpF6EwRxEnk0nESY5yky3VV3753cinb8teoZcjmSEZNMQoHUapfm25xwah9pEkojFaTfzF0hGjgtdol3fftRA7JOtIVtatT5B_4tYbzeCb-gSkUqAGjPnkbA3nco_qll9BtIgqysDnpiy6ZLhXC0dsG4xlrCUipPi9tDjh7bMZ-uTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنی‌کارواخال مدافع سابق رئال‌مادرید به ختافه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107933" target="_blank">📅 18:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107932">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341518f56.mp4?token=CqjUFYGHWPINev6mG8-b0YBF_5bwyawhk-QmnmnKcNSkA7oxiq3E68Ft8vd97yAboNOougOv76Vd4g_8dXit13Ha88B-Oe_kLRAK7I3rkKTdP6Um0MWUhy7y1sYimt-o8znhtWXghekG1DOSJ3QV86kdCX6YgGGFGAQvOmJdjpWnf8sBVL2olnZEoFqeDfclzHz6lmQkGnaw0l7XQpP54VTwuHm25byTVNR4zkrI6nA0dXtCCX_ELRCGoXMvHTANDQ2qHqJrpoIfv5h4Q3NKMahB5xr0rucuyO7_cuUA2NfmJs2Q-BF-W0PbN_u85tLmEj9Ri1hj6BJrEQANzhMyTqS3wAUCiZPPDk6CIuVlunlWLVQDyrCSBHhnry7ICngGLF9efVEsSRBQsdd_G4Ya4AOCm7ICWyd35qD4K7bRarr_NXlor5fMmTvOaNsQmLyZ5fREg-0OcWHua8RFYUgKhyExWSGSzs807wXlrV7jpiFbzRLVY2eWXAm8yvHitpCJlqmvcICrYjNvCZspdiXpT1JTlg3Lp0NiG-pQ05ct1pvE9M02t3ZQMg1w1UOyT2IAhjqqWYkVNPohVZvg34flN0HiedtvFj4gxfr28pQQSe1QqmTyDNrjZfQ1bt_JL8f1W1G-BwDpd629ss7mKILqMEVaNCLVCGITujwgiRxTp68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341518f56.mp4?token=CqjUFYGHWPINev6mG8-b0YBF_5bwyawhk-QmnmnKcNSkA7oxiq3E68Ft8vd97yAboNOougOv76Vd4g_8dXit13Ha88B-Oe_kLRAK7I3rkKTdP6Um0MWUhy7y1sYimt-o8znhtWXghekG1DOSJ3QV86kdCX6YgGGFGAQvOmJdjpWnf8sBVL2olnZEoFqeDfclzHz6lmQkGnaw0l7XQpP54VTwuHm25byTVNR4zkrI6nA0dXtCCX_ELRCGoXMvHTANDQ2qHqJrpoIfv5h4Q3NKMahB5xr0rucuyO7_cuUA2NfmJs2Q-BF-W0PbN_u85tLmEj9Ri1hj6BJrEQANzhMyTqS3wAUCiZPPDk6CIuVlunlWLVQDyrCSBHhnry7ICngGLF9efVEsSRBQsdd_G4Ya4AOCm7ICWyd35qD4K7bRarr_NXlor5fMmTvOaNsQmLyZ5fREg-0OcWHua8RFYUgKhyExWSGSzs807wXlrV7jpiFbzRLVY2eWXAm8yvHitpCJlqmvcICrYjNvCZspdiXpT1JTlg3Lp0NiG-pQ05ct1pvE9M02t3ZQMg1w1UOyT2IAhjqqWYkVNPohVZvg34flN0HiedtvFj4gxfr28pQQSe1QqmTyDNrjZfQ1bt_JL8f1W1G-BwDpd629ss7mKILqMEVaNCLVCGITujwgiRxTp68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
شور عقاب‌های سبز؛⁣ هفته دوم لیگ مراکش و تشویق بی‌نظیر هواداران رجا کازابلانکا در اولین میزبانی فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107932" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107931">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7y4peZzrS5rYe2ByRGKaFBp8sj3yDBGZWSwnSTu5adY24n-VvaiIP24I4JWAtrdjWtFeIERMQsqLyrAGn5giyzaYa0fvYybyz2ZhmqUybZOiVv9JuqtoXXdSEm6NNj7Vp8d3rXKuKES2WySxMs4tDP0tG2r9xafFsyuZxA9zp8TGIj87D48Id1ZkvhpW9qGHbvbBdSqdh43JHWlLlZRXBGfqfqYsgURKFvg5xL9YY6JJuHLs1qg0ywaUN5sfsuAdXAp9m_PsAWGb5J4w1NWxxdscujtuQJ-aziP7XMaFo81xFhLeGjD7Un04cuGHJVGt_PNjBa4PP_FkF-ryX_T8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اسطوره لیونل‌مسی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107931" target="_blank">📅 18:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107930">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ad3a54680.mp4?token=KWB2ApkcqH3toUV9QDnlOc7t4YdNG3izk4i7Tya4wvu103pZD6glZ6LMQo-KGuptVDTxB7OMFW2LuAU9ObsCteYXoFRhilM8OMLGHf5gcSzWreN6nV57DZr7FdPaw2NA3YDuWeDDkeWwvaum7nV-uO0YgJ-KR57q6ht547AuGSwtfZfDoQ7NRTLAOww658FjIKVlthq-pEuJlyBONw05JqAWQ8o57U7Zv3aF2tgx_oTotfc3cQk62jomCsvk6vvyVL2nDpKsho_KRl1RtxzK5XIBUBXT3OyBZ6h1acqycFVkbIADj6yh5xu3nfpJPSWgF6VSR3BAI-Pu9ieFea1_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ad3a54680.mp4?token=KWB2ApkcqH3toUV9QDnlOc7t4YdNG3izk4i7Tya4wvu103pZD6glZ6LMQo-KGuptVDTxB7OMFW2LuAU9ObsCteYXoFRhilM8OMLGHf5gcSzWreN6nV57DZr7FdPaw2NA3YDuWeDDkeWwvaum7nV-uO0YgJ-KR57q6ht547AuGSwtfZfDoQ7NRTLAOww658FjIKVlthq-pEuJlyBONw05JqAWQ8o57U7Zv3aF2tgx_oTotfc3cQk62jomCsvk6vvyVL2nDpKsho_KRl1RtxzK5XIBUBXT3OyBZ6h1acqycFVkbIADj6yh5xu3nfpJPSWgF6VSR3BAI-Pu9ieFea1_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
در شهر روساریو، یک پیراهن غول‌پیکر به عنوان ادای احترام به آخرین بازی مسی رونمایی شد.
😲
🇦🇷
این پیراهن در مقابل بنای یادبود پرچم ملی قرار داده شده و روی آن نوشته شده "Gracias" (متشکریم)، که نشان‌دهنده قدردانی از مسی به خاطر تمام تلاش‌هایی است که برای کشورش انجام داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107930" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107929" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107929" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGmh8w9ByuPF7plyIOyppzSjm15meLKk2nP4pZ5Ar9PCCX_cYrLP6sPMlw2o4PQfivGrOhGGJymdWEg65kTADro8z677WkWAlE52kZK8zX7uUSOxC5DBybO4IYehlW8G6iX7NpLHyzbXitu-7Tq1Wl5V_w6sSQyr6B6jXVBsKjIO6qeMRj0VLa9aTRyNintJTq6c-Cl6JaNK332LB5A98H1KxUar7K8dgh9MUkee9i0N3lCeMO5yxBRPuwvD8vhO-TvdU3WfWHRw-jQiu7FX-uypZ65M6fXPTFF2FjPeGq-YxiQefsSJ36f7A1Z-blk5S0rVg9UGO0ACJQfeTuqFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107928" target="_blank">📅 17:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c936aa92.mp4?token=pN0exFE3ePgWM8L_BovSlIu5RE5hBmlWwLq580WPFRNUfxjmNPbFYjO9oDtVUBwa4xTTwMrA3YaGLvmH4QsxlfZTIPSd0IoY4vZ_HRHSr3jGXXpuzym_DwNBuDBav_XWhkzmfrAGQroUGeU1gGnFhaXZRT5dsrxBPnWDPxy5m6adVpuI5Z2LiNNvC4_P_TbNT4cST5a7NxNLP9Oph7PAXDAKaZ8Uliqx0elsXvOTzPyN7IUgUI_Y4RHxUrr55cch3ph1M3LMXzx6Cdcnd0PtZwvqLjkpkKHvnkLdE-IeyyHiAI7s9wHRJNKINdnVH6d_XBozym9RmZ3DPidozjAMJ4kU2EJeC-bHBNxIZXzymtmVDBaaH7l_NQ2nUpwdipRIFfZAy6eqnFJRUzNTM9uPnC3yjfZnagrl3AtnOJjw7B5MaP2KkLr8ZZ0nU0xkhwZu9IGbeQafK3c0O-WL8tJJJ1L8hYBaZieNE0bkzFL77Jly89sIOQVbpa1bSbyniGMae1xpmE5zspw7Bah4STegsHIVdsgckC_JSRSyC5uVZ06G3TNvOTa-AN6qiuAbFEGmSa9q2X1EyBytgx5dBKTG7wlThMjlj6WkpIKzSSiddaZ4BxWCUhGo8XV3zSkO4brHk8alnGIh6Tc4vmN8P6GW6AyJi0v2RmY6UviqVB7xGw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c936aa92.mp4?token=pN0exFE3ePgWM8L_BovSlIu5RE5hBmlWwLq580WPFRNUfxjmNPbFYjO9oDtVUBwa4xTTwMrA3YaGLvmH4QsxlfZTIPSd0IoY4vZ_HRHSr3jGXXpuzym_DwNBuDBav_XWhkzmfrAGQroUGeU1gGnFhaXZRT5dsrxBPnWDPxy5m6adVpuI5Z2LiNNvC4_P_TbNT4cST5a7NxNLP9Oph7PAXDAKaZ8Uliqx0elsXvOTzPyN7IUgUI_Y4RHxUrr55cch3ph1M3LMXzx6Cdcnd0PtZwvqLjkpkKHvnkLdE-IeyyHiAI7s9wHRJNKINdnVH6d_XBozym9RmZ3DPidozjAMJ4kU2EJeC-bHBNxIZXzymtmVDBaaH7l_NQ2nUpwdipRIFfZAy6eqnFJRUzNTM9uPnC3yjfZnagrl3AtnOJjw7B5MaP2KkLr8ZZ0nU0xkhwZu9IGbeQafK3c0O-WL8tJJJ1L8hYBaZieNE0bkzFL77Jly89sIOQVbpa1bSbyniGMae1xpmE5zspw7Bah4STegsHIVdsgckC_JSRSyC5uVZ06G3TNvOTa-AN6qiuAbFEGmSa9q2X1EyBytgx5dBKTG7wlThMjlj6WkpIKzSSiddaZ4BxWCUhGo8XV3zSkO4brHk8alnGIh6Tc4vmN8P6GW6AyJi0v2RmY6UviqVB7xGw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
آنالیز فوق‌العاده سوپر تیم فردوسی‌پور از مصاحبه‌های قلعه‌نویی که واقعا عالیه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107927" target="_blank">📅 17:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=QfKwJXC5DS-msRF97We9-IyBIDtw4pnVW8F3_3tsPjyFB39aHP_XVnMQeJXnjt0gs1CiOVg8eEXxnKYzFjdi_qtwn4ct7WYRTtPzQnVyW-0yqXdKAy-jH_i5ALgegjxxWXoAzfPUB3zxv3gGWw1Kii11P9m1VydLfLuiuGbaQHgPMIJIhEG13AgGIdR4MZbBiHfr5sMBH3U8s_jBhD-x5PHT7KGp0xZ8u847qhWALtj3pOpm_vYvnu0axlRETKfvWrQ_LGn_wq5FjRDSA8iKrk55rk_aIzO0HlymdTsKT48dJLLaQD_e8_no9GG_JrIGL1fM6whEe-X1BKUlwB4L4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=QfKwJXC5DS-msRF97We9-IyBIDtw4pnVW8F3_3tsPjyFB39aHP_XVnMQeJXnjt0gs1CiOVg8eEXxnKYzFjdi_qtwn4ct7WYRTtPzQnVyW-0yqXdKAy-jH_i5ALgegjxxWXoAzfPUB3zxv3gGWw1Kii11P9m1VydLfLuiuGbaQHgPMIJIhEG13AgGIdR4MZbBiHfr5sMBH3U8s_jBhD-x5PHT7KGp0xZ8u847qhWALtj3pOpm_vYvnu0axlRETKfvWrQ_LGn_wq5FjRDSA8iKrk55rk_aIzO0HlymdTsKT48dJLLaQD_e8_no9GG_JrIGL1fM6whEe-X1BKUlwB4L4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👤
👤
حمله عادل فردوسی پور به میثاقی :
تو که‌ حامی قلعه نویی بودی ؛ آفای محترم لطفا رنگ عوض نکن... الان دیگه حق انتقاد ازش رو نداری...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107926" target="_blank">📅 17:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2cHJtsOZeYz1cTsBytC4GTRmC-Z0ioPjWdL9wTvWZOm9bMfsux3JJ4o5NRtEyE_VWLHxSdbuG-YAhcGUvlofRRxOOL9jRVd8vp4gcRQAFoEoYsgbsSnj0b4nSAlXmLSDX1jrjZc_ACF7AorKrRt56Uh3kHWJmy43cHjqtrVopxCWzF0DMDOyImXZJpuda06BwhYE9JKTn4p4MfK3CQzTIR-HastPTibfeSDRk1cdp8PF2I86QgiyjfcA7qt6_OsZMEhHkV0EIV4XHF3_L1hyLE5CHezcFsZNAoqNVXTeBIYyvb3slPRHoZ4dQu_uqsmaMDkL-vzqyEBMVDWd9D9bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
آندره ویلاش-بواش، رئیس پورتو:
🔻
برای مورینیو واقعا حیفه که بارسلونا تا این حد قدرتمند باشه. درست مثل زمانی که اینتر را ترک کرد ، بارسلونا در بهترین دوران خودش به سر میبره.
🔻
اما این دقیقا همان چالش‌هایه که مورینیو بیشتر از هر چیز دیگری از آن‌ها لذت می‌برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107925" target="_blank">📅 16:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مهدوی‌کیا: وقتی شکست می‌خورید باید پاسخگو باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107924" target="_blank">📅 16:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4e21ea3.mp4?token=rUzSTvASbqA5FdiKVYO8frpcDJmSATsCcb36eUtmYVF6LZB85Bdq_Gh3ebeHYShv3sT_augZ0dJL2TzSGUGC7uYKVQItXknsxOHggsvXSLn3cOzWZ7xDXKvTKwLg2T-iOfjvK7t5z7DhoTReh9b4n2aUJOc4k0wAVZJ6IOrBGIilhj6iEhCAmuzP-_d0IafFtDhuhAbZZhG9drt9aDPzajOQxZIhxneUI7GXHLB6MIT-HTRiXsDqmIlDwangnpJxpPjjQE-PzErvsgyAQDSwjZJ2cnSXB8_UIQIMSKvvMdAEBVy6kDk6VLZEMcr1fFF4sDcAVhqcym7QBPWg4s5BlBdJcFaAnz7H5sOQacP4B8HGim3LXqsm6I-I3My2B2O4tF9vWhpVH37-TpMeZS-l8DPkIlGoz1_QENCZGOWnt9Dpy7RSMxvZJoqs0pUUBZMM4eChfn16VCeTbivdP-O9qIXdXjg-VsQwXjgbTIP3n5alKDkR5AGKiOVwKYYQsYkXZWDTdMV4INIYz2B9891CCJe-gnJJejpefWevO__IvC0-EegnPdqQdFZYxWfXxRoUZ3KNLhAR5x3UzYk6tncfDK-sGM8Z29MJMjpAsoGDpQH4ZSZbEb-vRmJwIhSbg9zHgYklUnje08VzFpjuLxUGeXqpfeTrzZhNWJYc-jH50jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4e21ea3.mp4?token=rUzSTvASbqA5FdiKVYO8frpcDJmSATsCcb36eUtmYVF6LZB85Bdq_Gh3ebeHYShv3sT_augZ0dJL2TzSGUGC7uYKVQItXknsxOHggsvXSLn3cOzWZ7xDXKvTKwLg2T-iOfjvK7t5z7DhoTReh9b4n2aUJOc4k0wAVZJ6IOrBGIilhj6iEhCAmuzP-_d0IafFtDhuhAbZZhG9drt9aDPzajOQxZIhxneUI7GXHLB6MIT-HTRiXsDqmIlDwangnpJxpPjjQE-PzErvsgyAQDSwjZJ2cnSXB8_UIQIMSKvvMdAEBVy6kDk6VLZEMcr1fFF4sDcAVhqcym7QBPWg4s5BlBdJcFaAnz7H5sOQacP4B8HGim3LXqsm6I-I3My2B2O4tF9vWhpVH37-TpMeZS-l8DPkIlGoz1_QENCZGOWnt9Dpy7RSMxvZJoqs0pUUBZMM4eChfn16VCeTbivdP-O9qIXdXjg-VsQwXjgbTIP3n5alKDkR5AGKiOVwKYYQsYkXZWDTdMV4INIYz2B9891CCJe-gnJJejpefWevO__IvC0-EegnPdqQdFZYxWfXxRoUZ3KNLhAR5x3UzYk6tncfDK-sGM8Z29MJMjpAsoGDpQH4ZSZbEb-vRmJwIhSbg9zHgYklUnje08VzFpjuLxUGeXqpfeTrzZhNWJYc-jH50jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروژه‌ای که هر روز یک شاهکار تازه رو می‌کند!
قرار بود با عایق‌بندی سکوها مشکل نفوذ رطوبت و آب برطرف شود، اما هنوز هم آب از سقف ورزشگاه آزادی چکه می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107923" target="_blank">📅 16:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4700a47c7a.mp4?token=eFxdkk8H7zmDdzyEwKvuSUXamXG2llG5j67i11GhELcC7EaMqqSSpvXzXJynt-lJx_1VMB_3vupL9GfHhlR5mjxnhuQwoDbBTHPJYm6rFmcJeneB22CFA_pdKE8q77VnK_qxPZNA9I4rxKD6ahHDFSi2JZYp6jWre2HGpRN5o-7EEESEEkYenw_vbnpGRmlP-ROaqx5YfW1i68xjlOgclqoP-uZpSv-wW6urx44Fv7yIpFfpWYBef-kTDWf-GSeS-xo1zPKckv5PS5ziH4iS29HHqkx7abhA4EOiI09Ql6sBXXIPCxJ8SJrhhUnau0yNKuykvkREDa_kqf1_onxEnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4700a47c7a.mp4?token=eFxdkk8H7zmDdzyEwKvuSUXamXG2llG5j67i11GhELcC7EaMqqSSpvXzXJynt-lJx_1VMB_3vupL9GfHhlR5mjxnhuQwoDbBTHPJYm6rFmcJeneB22CFA_pdKE8q77VnK_qxPZNA9I4rxKD6ahHDFSi2JZYp6jWre2HGpRN5o-7EEESEEkYenw_vbnpGRmlP-ROaqx5YfW1i68xjlOgclqoP-uZpSv-wW6urx44Fv7yIpFfpWYBef-kTDWf-GSeS-xo1zPKckv5PS5ziH4iS29HHqkx7abhA4EOiI09Ql6sBXXIPCxJ8SJrhhUnau0yNKuykvkREDa_kqf1_onxEnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🎙
✔️
صحبت‌های جالب یاسر‌آسانی پیرامون فرهاد مجیدی اسطوره باشگاه‌استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107922" target="_blank">📅 15:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27cad11c0b.mp4?token=q1FptjrgZVUsoEcQJdbmLru3qHIAIFHv2-_7gFy_ElrGEP6Bp3eNmYD-iSTEIQ2tx_jxeWbLXc7LsSSxJ5KHfrAS14GglhzxxJq3trc6QP6S7_TSXfgthUmq10CxcVwuwdMOcnrzO_eQlMpTk-t0fiOnfTtrtV14sY0SndJ5P20uoYBt3ICrM2wNAJ_TbVAD5ByjlHuskUk8ycZkhDw97AhtvJmeepPL8PW1PR2DLdeDly9i5IsqRFFEw8oRnnXwDbo549PJUMtd7dBEbn9V8Y8TRaiWicBAjNhuJmYw6CpPwIess8GMgj_jaMwUe6i3I4Vz3oMHIakI1XYsB6ZFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27cad11c0b.mp4?token=q1FptjrgZVUsoEcQJdbmLru3qHIAIFHv2-_7gFy_ElrGEP6Bp3eNmYD-iSTEIQ2tx_jxeWbLXc7LsSSxJ5KHfrAS14GglhzxxJq3trc6QP6S7_TSXfgthUmq10CxcVwuwdMOcnrzO_eQlMpTk-t0fiOnfTtrtV14sY0SndJ5P20uoYBt3ICrM2wNAJ_TbVAD5ByjlHuskUk8ycZkhDw97AhtvJmeepPL8PW1PR2DLdeDly9i5IsqRFFEw8oRnnXwDbo549PJUMtd7dBEbn9V8Y8TRaiWicBAjNhuJmYw6CpPwIess8GMgj_jaMwUe6i3I4Vz3oMHIakI1XYsB6ZFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
پشیمانی بزرگ رجب‌زاده؛ باید به پرسپولیس یا استقلال می‌رفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107921" target="_blank">📅 15:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f6fed1c3.mp4?token=WJ6Fp5yKa9w6MbDrEWOrYEEy3PrQ1zzQO-ndtXt8ATOvK4zm-SfHbSIGG3AGk5tuk42eezl5TI2As4GV0oVCdiURPBh_ws_C-pN2Ksa638y3upBhFMX7p9LQ-i3v3rKTlnJoHZMU198iUXNGqNXJJZA6M04RI_RSEa6tSOMtL326iu33zIh4DR1fICXFfkCiNr1CVkqZE7sm1DPRoZDTXifOMUSq3PwgfwnXIZ45iNgvhdxvHk7RlwWTUnwVGFpu5QVT_AxE4UEuubCBxWu3Nv7E0xaPbpzw4JxStif0jzX5DhKjuMwklSwiBI3YbpHbzMnUKRDhAUTh5GnB36knYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f6fed1c3.mp4?token=WJ6Fp5yKa9w6MbDrEWOrYEEy3PrQ1zzQO-ndtXt8ATOvK4zm-SfHbSIGG3AGk5tuk42eezl5TI2As4GV0oVCdiURPBh_ws_C-pN2Ksa638y3upBhFMX7p9LQ-i3v3rKTlnJoHZMU198iUXNGqNXJJZA6M04RI_RSEa6tSOMtL326iu33zIh4DR1fICXFfkCiNr1CVkqZE7sm1DPRoZDTXifOMUSq3PwgfwnXIZ45iNgvhdxvHk7RlwWTUnwVGFpu5QVT_AxE4UEuubCBxWu3Nv7E0xaPbpzw4JxStif0jzX5DhKjuMwklSwiBI3YbpHbzMnUKRDhAUTh5GnB36knYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی سال ۱۴۰۰ در برابر قلعه‌نویی سال ۱۴۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107920" target="_blank">📅 14:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw_Ng7pqnLLpmQMJIlyqtYlX6L9ujJj26cAVjeEaMkDS7AsUJrS11MAa0JRiz6GY-2AKRykHa_4uBdFmlMazU6aKp14xbRm8n-WYH9UIjQFTG3pbedzhiQo4nRfNuSNSyD5Bdu1ROdw2vdJHx3rB4wvAVGS1wqUheSgokYzdy-lP4ZFN-9sbiKeDrCo8bxuF2yFfJ2oSdLypACCsiLB2LUtPX2xQ9mDrd_VsvmXX4Wswtok-b7PHNo4jck8rrrijs8Rea0A6wq2albp1w2BdjqSNUasSHamTut26RUX31tlheL3UcZ6TF31bZ2HZ1tCHG8OjhtDtwLBFNyzhKlzMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
رسانه‌های برزیلی با انتشار این تصویر معتقدن که وینیسیوس به قتل رسیده و بدلش داره برای رئال‌مادرید و برزیل بازی میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107919" target="_blank">📅 14:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0504ebd98.mp4?token=T1E8yikv0ey1vs-kCdBab5OtltsteXFdwD76mcQci_S7cRqedazIumf0elakMzgaoPmP6usT1Fa4krs5R5-VfSQLGD11lNYPsnbUHbJELnUuGF7r085_mywvCckZztn34f-Tiag9DMt7hM7GgjLFKHsVp25eYStRTspGsjNln0S3VULExQdb0LpYAqPGeTTm8lVVUg9EGj9Sgtq46nd4OiULB7UM09p6-rrjJswss2m8WLXwIO3Px7n72YYyVmB7XEJD8anV0yob9hFD1abHMzNdyLif8n-mLuUfEDsc_9H8NzGZ-8m3bqczcDOq3QnTxLA85Mlby2wOCddVjpvyTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0504ebd98.mp4?token=T1E8yikv0ey1vs-kCdBab5OtltsteXFdwD76mcQci_S7cRqedazIumf0elakMzgaoPmP6usT1Fa4krs5R5-VfSQLGD11lNYPsnbUHbJELnUuGF7r085_mywvCckZztn34f-Tiag9DMt7hM7GgjLFKHsVp25eYStRTspGsjNln0S3VULExQdb0LpYAqPGeTTm8lVVUg9EGj9Sgtq46nd4OiULB7UM09p6-rrjJswss2m8WLXwIO3Px7n72YYyVmB7XEJD8anV0yob9hFD1abHMzNdyLif8n-mLuUfEDsc_9H8NzGZ-8m3bqczcDOq3QnTxLA85Mlby2wOCddVjpvyTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
فتح‌الله‌زاده: از استقلال که بیرون آمدم برای مدیریت پرسپولیس هم پیشنهاد داشتم/ تاجرنیا نه مدیرعامل میشه نه میذاره کس دیگه‌ای بیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107918" target="_blank">📅 14:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8beb00264c.mp4?token=pnwKxvS8WDX17znnM5-YIeSdQaCu_4bs26BTPNz5aPHv2-Yn3BEVdJv_H8qFMfyeG3c8wCI2-jDbCdFCtlqyk63-bRYIGPlMvtcLo7jBHvqtIpZ_DOW3zEPRGzd33NP3ZBH2TQOBOpXJp1FnDjtrkge8qFyqgDRbHirAtUk-3oKDRNrAGMWbO9zHGbdRqHVKdx7QOdw5EdGQ9xgpIQ-Pjcyr5-PDSuefk-8xUj9Fj29s1fYgKVLQfvTCV4YTVcqfyidmrWXoqMxZVwnC59ndOV4WUV8ZXk6ycIAg1BqAuD25_yyMbHhItbqjisbYE9M9nq6bC8Qz3Io_WmTeqLePlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8beb00264c.mp4?token=pnwKxvS8WDX17znnM5-YIeSdQaCu_4bs26BTPNz5aPHv2-Yn3BEVdJv_H8qFMfyeG3c8wCI2-jDbCdFCtlqyk63-bRYIGPlMvtcLo7jBHvqtIpZ_DOW3zEPRGzd33NP3ZBH2TQOBOpXJp1FnDjtrkge8qFyqgDRbHirAtUk-3oKDRNrAGMWbO9zHGbdRqHVKdx7QOdw5EdGQ9xgpIQ-Pjcyr5-PDSuefk-8xUj9Fj29s1fYgKVLQfvTCV4YTVcqfyidmrWXoqMxZVwnC59ndOV4WUV8ZXk6ycIAg1BqAuD25_yyMbHhItbqjisbYE9M9nq6bC8Qz3Io_WmTeqLePlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
▶️
👍
تسسترون خالص!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107917" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اعتراف جدید کلثوم: آمار دقیق افرادی که به قتل رسوندم، ۱۱ نفره. یک نفر هم پیش‌از کشته شدن متوجه میشه و نمیذاره اینکارو انجام بدم
😐
⚽️
Channel: @futball180tv</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107916" target="_blank">📅 13:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8324686f63.mp4?token=f8wtvCuk7qTwkKKacPe0R2leQ1DSxO-VA9y51mtOMs0nsHJSR7LAnVmP7I3fPLIHwNK2LUp-o_r4dFwJYD7vBSVVRcsvDm1etRJH2Tm_9qhf-h9um4SEOab5MIEb4rxZxGNREfyCb_06GVqdo4gCRFCCKo_cpcPRil-KnrI6qpde7DzOzUO3nVjg7GdWsr89Kb1A-wk_ZX_9oJZ-opfhErYuzOv25Z6yE6fbbEhh3foriNWkmy7aTiOlGygsEeZwTzu2EmE6in7oU3EVH5I-alNZEDB67clvJOdYkrO8aCwGo6R5Ucvj9aoF0rFqB_fUIAF1WtmWJk53Qr1-4u-bVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8324686f63.mp4?token=f8wtvCuk7qTwkKKacPe0R2leQ1DSxO-VA9y51mtOMs0nsHJSR7LAnVmP7I3fPLIHwNK2LUp-o_r4dFwJYD7vBSVVRcsvDm1etRJH2Tm_9qhf-h9um4SEOab5MIEb4rxZxGNREfyCb_06GVqdo4gCRFCCKo_cpcPRil-KnrI6qpde7DzOzUO3nVjg7GdWsr89Kb1A-wk_ZX_9oJZ-opfhErYuzOv25Z6yE6fbbEhh3foriNWkmy7aTiOlGygsEeZwTzu2EmE6in7oU3EVH5I-alNZEDB67clvJOdYkrO8aCwGo6R5Ucvj9aoF0rFqB_fUIAF1WtmWJk53Qr1-4u-bVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیس سنگین ابوطالب به هادی چوپان!
هانی رامبد بهت برنامه نمیده؟ خب تو نیازی نداری به برنامه بزرگ‌تر از این نمیشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107915" target="_blank">📅 13:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05980d89a2.mp4?token=n_EZCrFOLaETF6qRgeixXOEnTu5WYyMEoq1i7hZ8r8pbr4PN4X4rF8CWHIMZlnCW0uyRHcyFbQt4d7tcjHtnjqCiuTQj1kQJZaEY3uIyve0CjYvOXXxZv0I3wEf9Z7pW3yFDx4HswQxCq3und72qudmmSdRBtPG1os4Ojbgv8gWabNxyNFzT9PNsUhfC0_RYgohe7lrKqYnJCj2lqxDX9L-jETVjvjPXEI7FaVhL3Zvonk4s0uSKHT3sSqqq7TcY5TIUS1edyDuD-H2z0CDkGYKOnUgTBTZvPUoS_-Er1EVnJ5P3HJD0J3IwqH1kvkMz_m4a_Vzp_KbacOezRyPsjKohLYmwPT3UfvodUwFIutlWf1CVgi1SkqwMDgOUSJ4y2Ar2qgKDPYPkNna2vYAjDH6nNriuj-a6SvjNvqh9dlld2_teuVrpwE3BvY352zbmkjglOLeXvdK1KnVgyl-7niOkejT4-vZjCT2w9OzoXbfMgVZZgHRr5X2ttGSP7qguo-_kc9Cv2NQGeHuS_ABMBWz1T1c6xZi_p44B0qn8Va3tsASzj5iSwZzXIIev_uE8hI8NV7agVOpryd9I2ogQDLmQ4B5s4p3gU6aXpebMk3eqP6mfloVKlgU51oHPn1PbcFrfeg0eqV0vsV3xOaTzdEkqXYy93X527iIlYPvaJ28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05980d89a2.mp4?token=n_EZCrFOLaETF6qRgeixXOEnTu5WYyMEoq1i7hZ8r8pbr4PN4X4rF8CWHIMZlnCW0uyRHcyFbQt4d7tcjHtnjqCiuTQj1kQJZaEY3uIyve0CjYvOXXxZv0I3wEf9Z7pW3yFDx4HswQxCq3und72qudmmSdRBtPG1os4Ojbgv8gWabNxyNFzT9PNsUhfC0_RYgohe7lrKqYnJCj2lqxDX9L-jETVjvjPXEI7FaVhL3Zvonk4s0uSKHT3sSqqq7TcY5TIUS1edyDuD-H2z0CDkGYKOnUgTBTZvPUoS_-Er1EVnJ5P3HJD0J3IwqH1kvkMz_m4a_Vzp_KbacOezRyPsjKohLYmwPT3UfvodUwFIutlWf1CVgi1SkqwMDgOUSJ4y2Ar2qgKDPYPkNna2vYAjDH6nNriuj-a6SvjNvqh9dlld2_teuVrpwE3BvY352zbmkjglOLeXvdK1KnVgyl-7niOkejT4-vZjCT2w9OzoXbfMgVZZgHRr5X2ttGSP7qguo-_kc9Cv2NQGeHuS_ABMBWz1T1c6xZi_p44B0qn8Va3tsASzj5iSwZzXIIev_uE8hI8NV7agVOpryd9I2ogQDLmQ4B5s4p3gU6aXpebMk3eqP6mfloVKlgU51oHPn1PbcFrfeg0eqV0vsV3xOaTzdEkqXYy93X527iIlYPvaJ28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🐐
حالا محکم بشینید؛ این دور آخره …
چهارشنبه؛ ۲:۳۰ صبح - پایان ۲۱ سال سرمستی در لباس آرژانتین؛ رقص آخر، قدم‌های آخر، قرار آخر
🎬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107914" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Tf39QShKdgvZB7QbIEfDJGgvwDk-UwVbQP1RmJWdHhYUqmqOqeC60ekl_XbS-ppJFFNn7QS6513mCh--tVDv_wcnRdG6r7lJxo18ZHxhu6HaLYtTKeXJRY7exoS9dytOFRKaREaH3PJzYzk-wr2Lqu9EXZxmxHprcSUN40-39P9AYHs9J8ltqwKDc4l1eccU01P-9mEWK0Iq58AsZLSI4PcIZYEC2tIufScS8PrPXx2tnpOyY488p5XPEe3ll5sWINXyRbzyI5Cn8C9t4fQSwjzTqiDSZ99Ex8iQY0KfPVykQDoUkxGc8Rifv8MdtdMH1ZYfdRNmXOFFv2DHFVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
۱۰ رکورد اسطوره مسی، با تیم ملی آرژانتین:
1️⃣
بیشترین حضور در فینال‌ها: ۱۱ فینال در رقابت‌های قاره‌ای و جام جهانی.
2️⃣
پرافتخارترین بازیکن آرژانتین: ۴ عنوان قهرمانی با تیم ملی بزرگسالان.
3️⃣
طولانی‌ترین حضور متوالی در تیم ملی: ۲۱ سال.
4️⃣
بیشترین بازی ملی: ۲۰۷ بازی.
5️⃣
بیشترین پیروزی با پیراهن آرژانتین: ۱۳۴ برد.
6️⃣
بیشترین بازی با بازوبند کاپیتانی: ۱۴۷ بازی.
7️⃣
بهترین گلزن تاریخ تیم ملی: ۱۲۵ گل ملی
8️⃣
حضور در ۶ دوره جام جهانی و گلزنی در ۵ دوره از آن‌ها.
9️⃣
حضور در ۶ دوره جام جهانی و ۳ فینال؛ تنها بازیکن تاریخ که به این رکورد رسیده.
🔟
اسطوره جام جهانی: رکورد بیشترین بازی (۳۴) و بیشترین پاس گل (۱۳) و بیشترین تاثیر مستقیم روی گل در تاریخ جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107913" target="_blank">📅 12:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79f527d7d.mp4?token=fo7OGBEhZBJDrCyVAqAVFl7wzsteRkNfqn8ByowohI_G51AI5S0u-Xih2LE_QdlZNqCAmF2rxzqDIOinXFrjmDDbGRtWXND4UqMykjJdmqMUYUs5Dzf7GTrociyQLjn_bEY6fjq3iZtUz7MhOu9S3PfsMyT1p6kYop85GyplGLWOqXG2IaL7LEFmcTVIS5boAeaZQgRPjNQJ8EAAJ1q4NZQg5fertMtlvbeLf4KUwtJKfgQmK4omjIz25AHTtsWMWmpCGNm3iJ3pdSC2mkghcHt_tdgZVKCZLo28CkxT7Er8JcudtNwZ9wrcUhC5SznyFF6rKKaXgAQeAFQgERq3cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79f527d7d.mp4?token=fo7OGBEhZBJDrCyVAqAVFl7wzsteRkNfqn8ByowohI_G51AI5S0u-Xih2LE_QdlZNqCAmF2rxzqDIOinXFrjmDDbGRtWXND4UqMykjJdmqMUYUs5Dzf7GTrociyQLjn_bEY6fjq3iZtUz7MhOu9S3PfsMyT1p6kYop85GyplGLWOqXG2IaL7LEFmcTVIS5boAeaZQgRPjNQJ8EAAJ1q4NZQg5fertMtlvbeLf4KUwtJKfgQmK4omjIz25AHTtsWMWmpCGNm3iJ3pdSC2mkghcHt_tdgZVKCZLo28CkxT7Er8JcudtNwZ9wrcUhC5SznyFF6rKKaXgAQeAFQgERq3cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
ولی این رسمش نبود ...
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107912" target="_blank">📅 12:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83cf644f9.mp4?token=XEMKC03WzXWGe1aPhJEbnasv8tRw2dxSYuYcyng_8uz1lBY3yjuX_nZQgIUBZYG2Zi3f3QurHduDII8JpSQy28aIai0bCFTptTKYlWiikfqGn7i-rVywLw4zpzvF1IE92hzcgV3S-1zm2Msn2pIVH3ZUbVFU_VesRz1WaYsP5rh3E_UMS8hpR41fGuGLv3hVJ4OBq3JvTi6B-MHKuAYAQV7xCdx52RMu8BuD3XYts1yWywems1L3ueWaAiuuwvkHn5qhUzqNE6rvK2NfRec-RCYDIEIJLqQJEPq9zNM30bEeXoOF_RCKPBHYUlYtyu06QIeoisZm_-LuelVK-fFK4Xl-ZFTHSvzUQc_3avIOmbevViZk-oPoLc-H2MwXZtITqg0TbeTVxW88QdOYde9oVGjoem4JNoVioUWYb8xRzDRhG9WDAJKBQYundEaNMK0KnbcbsRI_tFr-uq2u0zG3ROb2vgpdlXGB-aApXLBRa8nFP4BLqkQuB-QsygKyIMwlnj3tVypJesZSZYxLmS2eukULTlLy8bTbDtdt7JtMhv09PFxf_iKqWLomnpxmZLnPM-2cDMBNxXyuc-4fMr1YoiQX5uYnjOqZjNpr_ADrW7o2ZIC2hzod2WxA9jP52AMYyBdWndE5qcikPOISMFfnRj3tNA0_TxB1FxMs_AlUHBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83cf644f9.mp4?token=XEMKC03WzXWGe1aPhJEbnasv8tRw2dxSYuYcyng_8uz1lBY3yjuX_nZQgIUBZYG2Zi3f3QurHduDII8JpSQy28aIai0bCFTptTKYlWiikfqGn7i-rVywLw4zpzvF1IE92hzcgV3S-1zm2Msn2pIVH3ZUbVFU_VesRz1WaYsP5rh3E_UMS8hpR41fGuGLv3hVJ4OBq3JvTi6B-MHKuAYAQV7xCdx52RMu8BuD3XYts1yWywems1L3ueWaAiuuwvkHn5qhUzqNE6rvK2NfRec-RCYDIEIJLqQJEPq9zNM30bEeXoOF_RCKPBHYUlYtyu06QIeoisZm_-LuelVK-fFK4Xl-ZFTHSvzUQc_3avIOmbevViZk-oPoLc-H2MwXZtITqg0TbeTVxW88QdOYde9oVGjoem4JNoVioUWYb8xRzDRhG9WDAJKBQYundEaNMK0KnbcbsRI_tFr-uq2u0zG3ROb2vgpdlXGB-aApXLBRa8nFP4BLqkQuB-QsygKyIMwlnj3tVypJesZSZYxLmS2eukULTlLy8bTbDtdt7JtMhv09PFxf_iKqWLomnpxmZLnPM-2cDMBNxXyuc-4fMr1YoiQX5uYnjOqZjNpr_ADrW7o2ZIC2hzod2WxA9jP52AMYyBdWndE5qcikPOISMFfnRj3tNA0_TxB1FxMs_AlUHBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
آخرین پیش‌بینی خوش‌چشم، کارشناس صداوسیما، از تاریخ وقوع جنگ بعدی ایران و آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107911" target="_blank">📅 11:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM9UVWhD63VyGhP5bi49aiD4MOL7NhgGnI5cpyWz03RjXKH33rk1TUHxkoZOpUiQ3uhdPwTd63PgZ-cBR67NmbsoU7nWEffPbZLIFgDMJfv0bDMq1_FlM_gakcAjddcDxvcpDzefmn_YINQjsyCDWPBwGPbSgWaiWYT0FUxoE-pq5FK7NHWKYk-tbHufUd0xSJwEA8JW6RXL6HRDLAK-2XZRMJDRAH0WqaTa3HN2XK54k1sxibZEaWSbkJoBSi64Q2nEw3_zijT6arrImTUkCpuVu9cQ8XuEWIsb55McPbukWkRkQHRe2IE2Zd5rJLxDsyGFRuveMScLyaPCCP0-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107910" target="_blank">📅 11:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477e1b7cf7.mp4?token=Pzl6l3sYKPq9Qjvz4kRnxkP_mkkaBdIwLx33NsCsTqzrwVEnDmGgkit3r0z_dpr9xm1XGI4hftahIAAMDh5d4frBp_FTIbU50ZLTiZ8jGQlCCLzmhi_noCOywR0EsKr8dZvOY7v67Gu_sNoiD1IhjhGMErjipn5tfEnB-LL4HlryAVxWlz7unnjNZMvMqVJpVDcmDuuEOhFXZXfKo4TugBWNfQhSADm58qfTXCYC0A3etAcJ_g6B8ryaoO3P4McvgW6GqnugRwpdznMkZRy8D9QIJt7xErfdh9tVwoTXHiUcKO7XjQWWepA32dkYcVIUsLrqNdD2o5sRJoDOQVmq1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477e1b7cf7.mp4?token=Pzl6l3sYKPq9Qjvz4kRnxkP_mkkaBdIwLx33NsCsTqzrwVEnDmGgkit3r0z_dpr9xm1XGI4hftahIAAMDh5d4frBp_FTIbU50ZLTiZ8jGQlCCLzmhi_noCOywR0EsKr8dZvOY7v67Gu_sNoiD1IhjhGMErjipn5tfEnB-LL4HlryAVxWlz7unnjNZMvMqVJpVDcmDuuEOhFXZXfKo4TugBWNfQhSADm58qfTXCYC0A3etAcJ_g6B8ryaoO3P4McvgW6GqnugRwpdznMkZRy8D9QIJt7xErfdh9tVwoTXHiUcKO7XjQWWepA32dkYcVIUsLrqNdD2o5sRJoDOQVmq1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
ادامه‌دهنده مطمئن برای راه پدر؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107909" target="_blank">📅 11:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeed962e7.mp4?token=VGS3XCtTIDq4QLKgBF89xjXu7gSH1vWv82_nqs7aF9t8vvdACNR9Npvy_eKMXyezyE3PqhBijqSZRbb-fX9MeoT1NqVGo-6nkM69bYdUyPL1G1e0x5GqaXC_QoZOYvoaU8Tv25SkBRQAOXvMFJTdq2iuMhr1DrHa_nHnsywVdOpzHHUvhakXDygqJfuDB6Oym6KvpMWDgrXSww-Z0HlcKUa3wOUnJ73VCQN87Mx52inU3U_4ixIw7rE4HgMwgPsB4o4wc427sTykGcpkFKhPaZ8ig2fJhFZiWUuUoISgvO63zcrQfH4AWGHfxk9cFRE6s-2ZtHnW3iG8EjUdspn-9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeed962e7.mp4?token=VGS3XCtTIDq4QLKgBF89xjXu7gSH1vWv82_nqs7aF9t8vvdACNR9Npvy_eKMXyezyE3PqhBijqSZRbb-fX9MeoT1NqVGo-6nkM69bYdUyPL1G1e0x5GqaXC_QoZOYvoaU8Tv25SkBRQAOXvMFJTdq2iuMhr1DrHa_nHnsywVdOpzHHUvhakXDygqJfuDB6Oym6KvpMWDgrXSww-Z0HlcKUa3wOUnJ73VCQN87Mx52inU3U_4ixIw7rE4HgMwgPsB4o4wc427sTykGcpkFKhPaZ8ig2fJhFZiWUuUoISgvO63zcrQfH4AWGHfxk9cFRE6s-2ZtHnW3iG8EjUdspn-9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب علی‌ضیا از تغییرات باورنکردنی دختر بهداد سلیمی؛ تو ده سالگی هم قد خودش شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107908" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107907" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YA9_JlpKt6-E7Zj2uHc48DxLiTtQtXVMn4TkgiKSFpccSCeIZ_Jy0RpxLIQNyz0AZDRvcPDKRbThsq_b9z4Q-CxPP59UTiNeqeFgacN6r1wC0pByX7homeAJh-CwXzVMHzsy92M7NYIPpYhQOmoQO3YxFAjYZ0rWatZEcMxAKSMnxdxIMUZtAjYLAis7JGs0NAJTS1kU2bL88CiFkAOMUkJapCSD9PdYHJ-Myc6tPNkmagKTY3c89MbhtE09vtmEs8z76dRD_kB77vs6CEnR1c9iLm8nNPRb98PLxV44ks1Z9d-bxV_tAo3xlPr15QQBfU3MAvxK13wXTJZkRqbx8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیا
🆚
کرواسی
چک
🆚
انگلیس
اسلوونی
🆚
اسکاتلند
مقدونیه شمالی
🆚
سوئیس
ازبکستان
🆚
کره‌ جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107906" target="_blank">📅 11:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107905">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906a8b3b0f.mp4?token=n5wameh9fzDvwm8NkAmHKWWso6pNKRwC18LttVNCi_KyTq37xF1mujAWIcCokCD0MWWAVJCDH39K_oNGBWKev2QTSrGx_h46kpkwORYe0HqoCMrAgnNY_nWtssN-6uH8pFoMofAkQcij6x8hmh5lBkqWo47jzQIlngbtmFe5ShzOib2gChgnh-26Ndr5efCuJm1dfb8ASVcsgqn8_zRmdcWrPS53gOQM4mW6RBoA7zX9XZKndLuJFXTFmXQRfMM5HSCgRQU8HoBIzRSjrhx2l86mL6Z9KqWoEKXIB0-1tez-OPshAkidzJ7KZ-0g3PyuaUr785JVM6UAx4YLmTs4rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906a8b3b0f.mp4?token=n5wameh9fzDvwm8NkAmHKWWso6pNKRwC18LttVNCi_KyTq37xF1mujAWIcCokCD0MWWAVJCDH39K_oNGBWKev2QTSrGx_h46kpkwORYe0HqoCMrAgnNY_nWtssN-6uH8pFoMofAkQcij6x8hmh5lBkqWo47jzQIlngbtmFe5ShzOib2gChgnh-26Ndr5efCuJm1dfb8ASVcsgqn8_zRmdcWrPS53gOQM4mW6RBoA7zX9XZKndLuJFXTFmXQRfMM5HSCgRQU8HoBIzRSjrhx2l86mL6Z9KqWoEKXIB0-1tez-OPshAkidzJ7KZ-0g3PyuaUr785JVM6UAx4YLmTs4rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
محاسبه افت قیمت خودرو :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107905" target="_blank">📅 11:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107904">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT8nldbMS4_vfVVJjII5dcoxEqi2L1QtR_E8-TJ4xy_jxxohbPdgg_Es3KI8V0PZxqJGHMm9oWnDhH6HtsT6JthFTkZ2lJOR_KIkl4HYpvJGbSh19hWiSk4u7KROpQro8tNjmsDQYqh-olbzhDzihuB30X5LM3i461Wnl-UaV319XakC10XmVayx5mBGfneEV29VqLhDRbStNxHTjAUN74lmpXddoMn8ehCZMgCTW7TFSNOGfZiyoSoRyvJjDvPFSo8smtGIa2N_R6K1R0RejUBvO9-DFWkfXGO20E_uMXkWcjVT_nCZl6fLqxvg2-OhJo8U-XhF4O6sRqLKjhHy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
بیشترین تاثیر‌گذاری روی گل‌ها در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107904" target="_blank">📅 10:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1256T7VOS6PelTAdr6-NQFhq9ZgXkmKYZtFeIwzXcdP3l1jgs2PqBhnMUy2G3e1eTdW95fmZCqilb95ywe-o_ld-mjlGhwGaLAsxSeaB2_VduN7SPr6Vo0GRXC7A73cswLsB35TfvltoZXPqmnqDdpRy6UZ3_dh4M6uP3Unz53UmPiCIAZ_ta1kZtMl_T6-Buw9S6t-V1YqTS0JYo2GYOecAi4QUyKFTcAZAD8H1c7GQUzRDdxyo_xVZOMzB-MGgK3XZLVeIQ9y2vwu8jObwwwFI_yjDQ0mF7q0nBf5hXUtLj9rbn_-Am8R5Hg9kqN5qGtNQ6jjJIjTVHGRy5E1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری
؛ رومانو: قرارداد رافینیا با بارسلونا تا ژوئن سال 2030 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107903" target="_blank">📅 10:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBslY8IsouqPubfoZ6GzDA7uQ-U7aEYMtARa-aO5j8NZQEQ8mccmj1BtID012W4-kAATciak1mdZy7KxDmIHkixgll9_AmoImQvO1QnMWLC74NVF4uUW68ODLDhLopr4C2m8U1rrfrLlKWrrXceJljoovuWi0GHp-yar5aW4wckKce6VHzFeFbznv5TqbCjf3loUGeELWwepdk20hhAAoO4IiKAFz5a7-J8_UfK4KUBIWun2AWe5a0_agSG_WCcLBvRhZ_A66STsBFOs1xEX3yawYuuBkGV5v5GcagB4wvEOQnPtVptiu7wby6pAO9e_m_0dhRXwUC38RJ6ms9gmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
معرفی داوران دیدارهای هفته ۸ لیگ برتر
🔸
🔸
تراکتور - استقلال؛ داور وسط: سیدوحید کاظمی، داور VAR: امیر عرب‌براقی
🔸
🔸
پرسپولیس - صنعت‌نفت آبادان؛ داور وسط: احمد محمدی، داور VAR: میثم حیدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107902" target="_blank">📅 10:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff702b8d86.mp4?token=h6IyTZyFCpBtFndmbiH3mOBc4kcVmU_FfDUw7q430DpNkvVh0dITl8LjdTcLdxu9wzHTzhhplfeIPKJLjOquAP80GpkW0l7lJoM1h_1PxqPnOiVS1MgmY4N9_O0nON-3oZ8KAc38rR9Pnkg7Edr_8l_fyXC2SF4I1-FstfkJwEh_UWmvKYvJD8TKWrmbUJUmjeLgJp3xWJzip6YXRlEwvG5XM_QeeHIbnP8F_C8gmofXm8ce7X-D_Tk01wp_Zq7TsnithB_7bTG4Sx7W_BeNobAZEmyoHNEArG0K52Al6VdpTs9QFmIi046QP6bf7SRpcgseXWxoEKasRGwcRrmejX_yfXDdp-TND5JogzibVpEwfhMO9Me4O0X-lqRIbbvCEaZC7xsZIaDHPmQSqMZm5I8uG_BoTPPkI7S2M7OvPb4_vOmNzIO2CqraMd-b1mXbPrZXmncSk9TEXvAuKZ095HAPpAyYWI87cErl_U7SMoENOSt2GRnaMCIAxDteHsAZuNyYZIoP3pvFaSDD0FJgismNwa9WXmLBnSjcWvECG4m-4p0H4apaE9MdgjhHbyW9oDvejENXJOrwFn9ibAluUnd-B-53NyMogmuTR6plVVYMw_787ZVhKHWuuI9OuFe5HCwz4LsHAiQBefHvH8Hkl_tzm-LBKOaaIopIwH6v6pk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff702b8d86.mp4?token=h6IyTZyFCpBtFndmbiH3mOBc4kcVmU_FfDUw7q430DpNkvVh0dITl8LjdTcLdxu9wzHTzhhplfeIPKJLjOquAP80GpkW0l7lJoM1h_1PxqPnOiVS1MgmY4N9_O0nON-3oZ8KAc38rR9Pnkg7Edr_8l_fyXC2SF4I1-FstfkJwEh_UWmvKYvJD8TKWrmbUJUmjeLgJp3xWJzip6YXRlEwvG5XM_QeeHIbnP8F_C8gmofXm8ce7X-D_Tk01wp_Zq7TsnithB_7bTG4Sx7W_BeNobAZEmyoHNEArG0K52Al6VdpTs9QFmIi046QP6bf7SRpcgseXWxoEKasRGwcRrmejX_yfXDdp-TND5JogzibVpEwfhMO9Me4O0X-lqRIbbvCEaZC7xsZIaDHPmQSqMZm5I8uG_BoTPPkI7S2M7OvPb4_vOmNzIO2CqraMd-b1mXbPrZXmncSk9TEXvAuKZ095HAPpAyYWI87cErl_U7SMoENOSt2GRnaMCIAxDteHsAZuNyYZIoP3pvFaSDD0FJgismNwa9WXmLBnSjcWvECG4m-4p0H4apaE9MdgjhHbyW9oDvejENXJOrwFn9ibAluUnd-B-53NyMogmuTR6plVVYMw_787ZVhKHWuuI9OuFe5HCwz4LsHAiQBefHvH8Hkl_tzm-LBKOaaIopIwH6v6pk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇮🇹
آنالیز بسیار جذاب از تقابل تاکتیکی ایتالیا و فرانسه در فیفادی اخیر با هدایت زیدان و مانچینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107901" target="_blank">📅 10:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02c435695d.mp4?token=PMlvyyTPtyHZurgcR8uYC4yeqiudOs91pP0nxZuziqU0Oa7zTz4OFBpbp11ww-cjWW4Q2KgbBCbGVB0kEUXAxyzXIOnCoSbRkAFV4TA-b6y8lbejyoTlIEQYcSgEooTCLUzyyiqCmGSuH53HeIA2miV57lrAXE5qTzCGwpEKy1vjVuDDiKYBVA-qXkMZrlP-Ce6jS0QN5ByiWTaSh25NV68X8zcfskJTMjqTfNSnVP4aErF9oH6JTc2tfCOw-JfYQUgJkPFzPJtiBUvhmf5GqjdZ7_rsl0YME-K9tQSrzuTIcnsC8qiwSqxOLoerlFMPEufwYvR0qKNMDBD6RVK3dLNObOrVlMXYlHz615kquDK0BwCpKYAUEihi4muxevO8HnkGt8tjDdGspPA-hEXc1VoOTPYvHnJb5AKm0z8RkdmsAVDJe-p8CfRnsWFvjBNgoGIrXtIDPwLk3JaclewURtROoJWnWNt-eVygg99a4yIMVjidl9Vy0BCKBN87GdQQxSXKI6unr2Tjc6ET-T4GQPpj_88MykFKe2jCQsyplvAOTdV6JuwW-ZrE0DGw2NZLpPRHjl68hDFMmsJJKRX_14hhPMDTGGFoQVhlPmPM9TzISVd5EEaxTO7WoTrv0NuhRRL0XgtrRaacx7n19IQJVmp0QqnEEVKrLTa09VPBKeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02c435695d.mp4?token=PMlvyyTPtyHZurgcR8uYC4yeqiudOs91pP0nxZuziqU0Oa7zTz4OFBpbp11ww-cjWW4Q2KgbBCbGVB0kEUXAxyzXIOnCoSbRkAFV4TA-b6y8lbejyoTlIEQYcSgEooTCLUzyyiqCmGSuH53HeIA2miV57lrAXE5qTzCGwpEKy1vjVuDDiKYBVA-qXkMZrlP-Ce6jS0QN5ByiWTaSh25NV68X8zcfskJTMjqTfNSnVP4aErF9oH6JTc2tfCOw-JfYQUgJkPFzPJtiBUvhmf5GqjdZ7_rsl0YME-K9tQSrzuTIcnsC8qiwSqxOLoerlFMPEufwYvR0qKNMDBD6RVK3dLNObOrVlMXYlHz615kquDK0BwCpKYAUEihi4muxevO8HnkGt8tjDdGspPA-hEXc1VoOTPYvHnJb5AKm0z8RkdmsAVDJe-p8CfRnsWFvjBNgoGIrXtIDPwLk3JaclewURtROoJWnWNt-eVygg99a4yIMVjidl9Vy0BCKBN87GdQQxSXKI6unr2Tjc6ET-T4GQPpj_88MykFKe2jCQsyplvAOTdV6JuwW-ZrE0DGw2NZLpPRHjl68hDFMmsJJKRX_14hhPMDTGGFoQVhlPmPM9TzISVd5EEaxTO7WoTrv0NuhRRL0XgtrRaacx7n19IQJVmp0QqnEEVKrLTa09VPBKeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تضاد قابل توجه صحبت‌های مورینیو در مصاحبه اخیر خود با رفتار دیروز کیلیان امباپه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107900" target="_blank">📅 09:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107899">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6256aac96.mp4?token=CgEmKc-gt3MGVGe-EmkN9TWYHT1xga1TFfV-Akgv87CQK2y9Zr3abTTD-PkJhkPSJYQe3Ik8gVfmToWNY0-L-1awIFeyO1FwugivfJ5_Ok7IkMsRl_WP88B2cOhk4Sd0kJtEhc9QrSXxwknoUDCEpUuqIvVkrjF1TCdV3spmoYosos3-Y3jmoGHbtYD00PNKq8z6O1OzWfR_brLt176pGJCdhJ8FFPxRFzHBvK1zYW3rk7W4tHPgfMSnUwo6MPVp6EdslfrooiRke-G0Oass6-IpMMmjV9ZwkgmGhqCWjLwDKdS92ZDRZb-Smm-5g2xMMjSd-py9e-bnVb1Qbz0PqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6256aac96.mp4?token=CgEmKc-gt3MGVGe-EmkN9TWYHT1xga1TFfV-Akgv87CQK2y9Zr3abTTD-PkJhkPSJYQe3Ik8gVfmToWNY0-L-1awIFeyO1FwugivfJ5_Ok7IkMsRl_WP88B2cOhk4Sd0kJtEhc9QrSXxwknoUDCEpUuqIvVkrjF1TCdV3spmoYosos3-Y3jmoGHbtYD00PNKq8z6O1OzWfR_brLt176pGJCdhJ8FFPxRFzHBvK1zYW3rk7W4tHPgfMSnUwo6MPVp6EdslfrooiRke-G0Oass6-IpMMmjV9ZwkgmGhqCWjLwDKdS92ZDRZb-Smm-5g2xMMjSd-py9e-bnVb1Qbz0PqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
پرتغال بدون حضور رونالدو همچنان می‌برد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107899" target="_blank">📅 09:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107898">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522303d3e9.mp4?token=ujeTc3m7zZa4wqUGmQEhQrfg5GCSjSRoZ8_r4G_ZAj9AW3sbEN8qzfVxe0iafCxLixiN-6Q1m2sAo4lYs-rh4j_2pLMZ5X07ciygS3nXj0dnPvQ0vCvJ7kblZXWTs8vq_zz_lpSDaDGntVcXyjsu537-FV05yZS6o_oXLiwmctWRdRv5aAzIjjD04ZrGZBLNsA7e1_cvn_HF-m0nHk8MIng2Kb8ESQVwHS__Jmt8YkFXbQ2gIPGPSWDCMF-iZB7Mpft5ANjF5K3vCIU0N6XtEIHGuNciVoCiNdKVQY9cc_mRk_YnRY2yBdKpDZ001PR3uU33Q7_mIN8uN2lMcOHOXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522303d3e9.mp4?token=ujeTc3m7zZa4wqUGmQEhQrfg5GCSjSRoZ8_r4G_ZAj9AW3sbEN8qzfVxe0iafCxLixiN-6Q1m2sAo4lYs-rh4j_2pLMZ5X07ciygS3nXj0dnPvQ0vCvJ7kblZXWTs8vq_zz_lpSDaDGntVcXyjsu537-FV05yZS6o_oXLiwmctWRdRv5aAzIjjD04ZrGZBLNsA7e1_cvn_HF-m0nHk8MIng2Kb8ESQVwHS__Jmt8YkFXbQ2gIPGPSWDCMF-iZB7Mpft5ANjF5K3vCIU0N6XtEIHGuNciVoCiNdKVQY9cc_mRk_YnRY2yBdKpDZ001PR3uU33Q7_mIN8uN2lMcOHOXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تماس‌ژوله با آناهیتا درگاهی عمه مهاجم تیم‌ملی وسط برنامش؛ بهش میگه فوتبال ما عمه‌ای شده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107898" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107897">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25bf4f2e86.mp4?token=fmXsY8YB0eIot5CTrUymtCzJuOhjbC73axEzxa2l4ltzuxDMezgfrxtvudP8bdJjdL0gGVuC3racmcKg8bcneVgXpr8tXoCexpbR70TD5bEZUvf9K5T_tj3PWDjPmBe_sGU1XOgXYDXQ_uBMzk8-Fg_Mg-8BdbWJFVkyEWXefWPaPnGDmMe-2HpMmGSN200W6e46r_nBV8X0TzZamqNpPxuKnc2caZuZP76GAXnK4onyhDawzwi9X_2lzhbCgL84wkBy_qjWA03NKO_-d80MRY7VQ5Nz5gRY_ZDZG4btEwA--CAwQswAH1QsAxWMNhi7DwqRmUO2iIGvREjVeRcRlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25bf4f2e86.mp4?token=fmXsY8YB0eIot5CTrUymtCzJuOhjbC73axEzxa2l4ltzuxDMezgfrxtvudP8bdJjdL0gGVuC3racmcKg8bcneVgXpr8tXoCexpbR70TD5bEZUvf9K5T_tj3PWDjPmBe_sGU1XOgXYDXQ_uBMzk8-Fg_Mg-8BdbWJFVkyEWXefWPaPnGDmMe-2HpMmGSN200W6e46r_nBV8X0TzZamqNpPxuKnc2caZuZP76GAXnK4onyhDawzwi9X_2lzhbCgL84wkBy_qjWA03NKO_-d80MRY7VQ5Nz5gRY_ZDZG4btEwA--CAwQswAH1QsAxWMNhi7DwqRmUO2iIGvREjVeRcRlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
حجت کریمی توهین کرد، علی خطیر تهدید؛ کریمی: تو دلالی، خطیر: دادگاه می بینمت!
❌
درگیری شدید دو عضو هیات رییسه پیش چشم سخنگوی فدراسیون فوتبال در برنامه زنده تلویزیونی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107897" target="_blank">📅 08:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107896">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4798a06f34.mp4?token=A1Hx3WG2gnxah5-v7bc3C_Nv49LP9RGUHxhLusjirehSUxHuoHIZdiejLTN_x9SSidwQpNY_oj8A7uzMPwzFM2iQrQ_0M6mOsIvvFMfUg53lr9bxfI-gdHXWRYUXy5zhdhF5Z1iqSH-K7XWguSI8dNrhZqQjvXp4YvAsjLpMldxHyXIapu-IJQKyIzVkD3szIT2OB7KQUSkD5m4wd1XeR0FowiD0U6Vkq1k0iOf9vbLYCC87XoKnzCGlNnktWdAS4BvUfJy3x256lXOwo1mFm-3-d7ZPCpe-N3zOAg_42lA7x5eg3K0Sjio210CmqZNitpS-NbIp-1GmkOLLBQttSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4798a06f34.mp4?token=A1Hx3WG2gnxah5-v7bc3C_Nv49LP9RGUHxhLusjirehSUxHuoHIZdiejLTN_x9SSidwQpNY_oj8A7uzMPwzFM2iQrQ_0M6mOsIvvFMfUg53lr9bxfI-gdHXWRYUXy5zhdhF5Z1iqSH-K7XWguSI8dNrhZqQjvXp4YvAsjLpMldxHyXIapu-IJQKyIzVkD3szIT2OB7KQUSkD5m4wd1XeR0FowiD0U6Vkq1k0iOf9vbLYCC87XoKnzCGlNnktWdAS4BvUfJy3x256lXOwo1mFm-3-d7ZPCpe-N3zOAg_42lA7x5eg3K0Sjio210CmqZNitpS-NbIp-1GmkOLLBQttSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
خطیر: اگر آقای گل‌محمدی قبول کنند من همین فردا کل هیئت رئیسه را متقاعد خواهم کرد
خطیر: هیچ مربی ایرانی با ماهی 500 میلیون تومان سرمربی تیم ملی امید نمی شود! کمترین دستمزد مربی در ایران 70 میلیار است کدام مربی سرمربیگری تیم امید را قبول می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107896" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107892">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3867ed322d.mp4?token=tDTnou5GVejawHIAR6CYbKGMAdAkEIyBhHPpW-Tvvbiks_uSv7jIOP1NFZJLMhQJEFMMO6sNxbjQ3MfJtU8Pr3gBd-7pK90vU7ea9Cc7JILXRwKtHZiyX8zvQnj6cFM63t4gRn17WkGc6tKvFyYBbKc4Mu0ZNSyTXSWD05dPaKloiZizurEsEZQvgvWu4eMQy4QNreTpQE8zZrOoG1pHw2PeORdKP655_mFcY7uI2ScKGqkSsNxvtAHBVY_SkoYxqcQWey0dSDJx1JWSxrjx9JFlup1PzC8RtAKrwIFxIM3BaFOsA_X7yR_ABjANMrBVlzjfnrvVqX2UmWTWq_Hhag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3867ed322d.mp4?token=tDTnou5GVejawHIAR6CYbKGMAdAkEIyBhHPpW-Tvvbiks_uSv7jIOP1NFZJLMhQJEFMMO6sNxbjQ3MfJtU8Pr3gBd-7pK90vU7ea9Cc7JILXRwKtHZiyX8zvQnj6cFM63t4gRn17WkGc6tKvFyYBbKc4Mu0ZNSyTXSWD05dPaKloiZizurEsEZQvgvWu4eMQy4QNreTpQE8zZrOoG1pHw2PeORdKP655_mFcY7uI2ScKGqkSsNxvtAHBVY_SkoYxqcQWey0dSDJx1JWSxrjx9JFlup1PzC8RtAKrwIFxIM3BaFOsA_X7yR_ABjANMrBVlzjfnrvVqX2UmWTWq_Hhag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
لحظاتی رمانتیک و شبه هندی در شبکه سه
روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده
😂
پی نوشت: گفتنی‌ست در لحظاتی از این برنامه واعظ آشتیانی و علی خطیر با یکدیگر درگیری های لفظی داشتند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107892" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107890">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4ZHWzS-PkmxUT7DKRBlrsLNAea3HNwWgtaGyvbDWR90z8pW1Ps-dw7UNWsOe6B7ooCcV05acghwUdynye6CLQuj70sChRCb-msR3-7j2SWVqMm6eDXAp1NQmgHqmjLDr40TDgyCe18JFePEiA875vMDxlJuQGk1qLV1uMVPEm9SfSkxk9ACeZu_QMsDb6YM6S8exa_qMLivHTGcuTkhqUiVmF2in4_C8l9zUeSN-EDmovqF614Ylsm94p7JP-NxFn1K5EPMLjNvW0IEDKlYz3Z-3ztmZ8k2ysHhsB4SMdCZ9hr8Ey21tA3M6fHvr-YUTx4tbTCuJ73TRiIGSapUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZIQ8QjnbViqqeM4p8-FC1WQ0zCfNFD4gzSei-0JhVL7sxRAWPuS7jMLXsyt-PfTjnizLo66Y3ndDYTwwbC_bz6Q8Oe0srAMbPhKehJ244WcnoVJ_hpqGX9NmWuAFSibwEDwgVr7UpCDvOWYLdzAm1dBsWMoPgFbfeBSsLpeC5rO2RomLTnAONCuF0pwowTSDyjar4yqqZ8bVpx0I1glLet9oVw6n64wn9tw_44_nkkuauZPlT9QB0g1CPzwe3oMAHr7u6zJFG_cF5OuPF1ISwPTtt6SYs8sImUQqfqtyDsJHka0Wwh_Sn3GISo3cQ0eaD-Hj8kvFqZ_FX9oUI-TIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
ترامپ: نمی‌تونیم جلوی شیوع طاعون از روسیه رو بگیریم!  این ویروس بسیار کشنده و خطرناک‌تر از قبل شده و مثل یه ارتش شدن! حتی با پیشرفت چشمگیر پزشکی هم نمیشه جلوشو گرفت، با این حال ما به روسیه کمک میکنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107890" target="_blank">📅 00:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107889">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIriAz9WVQFq-Jt0-tYS0cfl6DwjiegSce8M0ID-sBWbdgW9jm8N-PiqdIDidfXyEPdhbpcVhhcjU2l1RwWb1GTG78PSmuignB454zqK42SzURUlyfMUcn6Aj6wQuQDxEXRwyHRC6zt0O5CvS604QYufeeALutLJABE_iCuZJS3FbpTCuWa-GHpL9hAdbRWYJRKtqKlyxzCczUqjiC5d3eXbbhWMhIekqN7WN1ng4_wWLC938wWhSV_Uo79AC3Kgk2U7r6z9UZI5LkcgTXtJoBt7nEYfbK0O_YC4DzRGdQ9WCXExJG29psWDFCtHn07Vg92rUkeMwJ89H3dID62HcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
✔️
لیگ‌ملت‌های اروپا؛ ایتالیا رفت و برگشت مقابل ترکیه پیروز شد؛ تیم مانچینی سرحال نشان می‌دهد!
🇮🇹
ایتالیا
3️⃣
-
1️⃣
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107889" target="_blank">📅 00:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107888">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3c5cdf08.mp4?token=vFf6UKTXxPlfkdc_so0IROFXLOxxaWeo0QiRwm6aaeaD5lo6bXrKCbSN1W1IFCSjznjB-Y4rvyD4hdSxayL8eIoqYEKeNfvPk0pEL5efs862PYWt1AGSuh2dMrvftygJfkYI_5ABnsQeBiywVqLncKFWc9tdoxZuNrCPAiA-o86n-mZ6O003jk83XefkOU0lOcnVQMRFhfGPRtzxoFDzi1kuA9OYmyb0-0OHsYY-IhJMitcGwE5TwYI7lzrbrb2F8RgqVUS_DX-jinnq0LNgslCRibrVqvl60z9TWrty4hfYl1KZY_Ri07mwSlJ8OJeyqvnYBiFX0UxgeTQig53w7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3c5cdf08.mp4?token=vFf6UKTXxPlfkdc_so0IROFXLOxxaWeo0QiRwm6aaeaD5lo6bXrKCbSN1W1IFCSjznjB-Y4rvyD4hdSxayL8eIoqYEKeNfvPk0pEL5efs862PYWt1AGSuh2dMrvftygJfkYI_5ABnsQeBiywVqLncKFWc9tdoxZuNrCPAiA-o86n-mZ6O003jk83XefkOU0lOcnVQMRFhfGPRtzxoFDzi1kuA9OYmyb0-0OHsYY-IhJMitcGwE5TwYI7lzrbrb2F8RgqVUS_DX-jinnq0LNgslCRibrVqvl60z9TWrty4hfYl1KZY_Ri07mwSlJ8OJeyqvnYBiFX0UxgeTQig53w7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری لفظی واعظ آشتیانی و علی خطیر روی آنتن زنده
🔹
آشتیانی: من فکر می کردم نفرات اول و دوم فدراسیون برای پاسخگویی حضور دارند
🔻
خطیر: من هم انتظار داشتم با نفری صحبت کنم به مسائل روز فوتبال دنیا آگاه باشد
🔹
آشتیانی: همه آقای خطیر را به عنوان ایجنت می شناسند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107888" target="_blank">📅 00:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107887">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff62591c17.mp4?token=cET2CFEXaZ00CynDaAx7MGgWn0rLjaqvqZC24tnpSwBSefDz8F-Z7-_mnLLRLM9QQ9f6xpowN4y-Vr6FME33p73zKYTNlNdE-SgJ7rX_7evo4CXH00Y-G3r6-4Dj5eKHKBu_wsYq07LkuwkkeQMdUZQf843XLQfPpK4X8tpkeYX2DW3lh-37UKJGE9pvN8LXBHsNYb0mWxHmzSqpLdT_LBexxW3Zlk6gg3zf5ojHkEWlagSySzSEmLYopvgAhPP6O1chT-ghWsoetK-dNpVCHGuYc8lr-SmO4Jql8uezuVgleP8u90H9te67cK6LkiPbvMDhdSh88GNpxidKqFGQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff62591c17.mp4?token=cET2CFEXaZ00CynDaAx7MGgWn0rLjaqvqZC24tnpSwBSefDz8F-Z7-_mnLLRLM9QQ9f6xpowN4y-Vr6FME33p73zKYTNlNdE-SgJ7rX_7evo4CXH00Y-G3r6-4Dj5eKHKBu_wsYq07LkuwkkeQMdUZQf843XLQfPpK4X8tpkeYX2DW3lh-37UKJGE9pvN8LXBHsNYb0mWxHmzSqpLdT_LBexxW3Zlk6gg3zf5ojHkEWlagSySzSEmLYopvgAhPP6O1chT-ghWsoetK-dNpVCHGuYc8lr-SmO4Jql8uezuVgleP8u90H9te67cK6LkiPbvMDhdSh88GNpxidKqFGQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚨
‼️
میثاقی
: فیفادی واسه تیم ملی ایران بعد از بازی دوم تموم شد، درحالیکه ژاپن همین امروز بازی داشت و خیلی از تیمای جهان 4 تا بازی انجام دادن. قرار بود تیم ملی با گینه بیسائو بازی کنه، دیدن تیمه 3 تا به نیجریه زده، بازی رو کنسل کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107887" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107886">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/berpiyvf4eDb7wvZwsJdlXuljPkhv3RTfkuZcqLYcYmCrhmTfw_39WHcYm8tu893SZxELCndUyrg3vAw8xhGZhCDC0cYMUt5t4YjdxFZFas8bCt93ajFUWXFy52tuBee7pyaxWXddmsl3JITH2zJAPPjBVxeSKK86TynNpsK_HeeWPGSk_bjJCkUT6kcWDFi_LLX5Emm9FX0iLMy34mmtYX-nAdVRa1aOorck5D4SFXyzy94RX31toN9dkJNf6S3_Z7uGvChZRzDKaEe5x7Y2x-p8SyD3ZMwFH2vahSEh7OAtQORN3Y7LxKMMo1r_XfbgfWI5wfU3vrQn9oBbdWppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇺
لیگ‌ملت‌های اروپا؛ زیدان نیازی به امباپه نداشت؛ اولیسه و چرکی ستاره‌های خروس‌ها شدند
🇫🇷
فرانسه
4️⃣
-
1️⃣
بلژیک
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107886" target="_blank">📅 00:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107885">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh-7wDzern-1jha0KLsX_iHAayZLBznJy_GRXAxPv694A0H1_ws5-DK2OA8HlsNPmoC1JdqxJ2pyUiaxokoqHAh-7RXeU2ztBrO0YO31sxEDST9G3B1PAJ0luN7QqOT3zxj3MOGlhbRoWAVG0d1FcFzEaSRUmrqbAMPC6ZQZMw6VmR6pqpXX04pmmoA1xAawM9EAt78iWPZsYrjqPyKaTifXs7tlCfdj9qHgspLKU6yTKGUlqwVNw19Ox91JO8Ea8Th2LHBcYhrD7Ya5khWuEnYhifXYH98eohFfIgkOzl9wKgJXKOzP7ubkdHd8SU97CZyijKaaF8tW4FmgLL1GTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇺
لیگ‌ملت‌های اروپا؛ زیدان نیازی به امباپه نداشت؛ اولیسه و چرکی ستاره‌های خروس‌ها شدند
🇫🇷
فرانسه
4️⃣
-
1️⃣
بلژیک
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107885" target="_blank">📅 00:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107884">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_AyNaX-vmW9aX2PJwsSvpmBsBme6Wzwtst54BKLn-M6TOyk8wAMNztCGpQdq84o2JZP8pHDUmWyk8vGGynhyZutRww2mfcE1rg-KMs7248mE7A0-4qAi95qL6FO6ESy0WiKAGaKD-lSI4Od_vsLfr0oWwK9RGhc1S0zJg4_YWpfdxi4uARqUcd2mQ6djbWTtVPb7xBZuk5lHl7dcpyLF5AAavMv2Ws1MMoKC9OhLoOk9xiyUEMS013KJJtxao1c1nvc2_1f7E_ctBW52JiuswK9C0LTPPu-cO9vPJe3Yluyd4mlDyvWIcTIJ57_Ke-R2HWVl31c8ytY1k0_XBTTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
✔️
لیگ‌ملت‌های اروپا؛ ایتالیا رفت و برگشت مقابل ترکیه پیروز شد؛ تیم مانچینی سرحال نشان می‌دهد!
🇮🇹
ایتالیا
3️⃣
-
1️⃣
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107884" target="_blank">📅 00:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107883">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f8a10c9e.mp4?token=VUiR0MAunuy1hMtQZsANOILS7PyehVG3Cchca0josGlLbIiar7bCXGn1AntBldLf2S6awFDnGY6v_Lho0bjh99I-jq33bFXssJDWSsvuwX6h6XZa8ddxkrXXQ4rUHAOs8WTqlgOgcgPRZyIfMnl4N0mCh9ZLHV8qhBQMviDnjDXX4rWW8dPT43YVXlxfY4LOI-C3p_pzLJgmTcWy6VAOgJd7BClvcVEzVm23cTuFlLQpPAsbO9ZNlu7lt98zSIyrACE9Ta9lfH4pdyMEI40tLoJGy5zgbdjOQkRUhAsgSxBjhq4WHYYxLgUCp22844EmpNwTHmclvtn6tGszOknyzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f8a10c9e.mp4?token=VUiR0MAunuy1hMtQZsANOILS7PyehVG3Cchca0josGlLbIiar7bCXGn1AntBldLf2S6awFDnGY6v_Lho0bjh99I-jq33bFXssJDWSsvuwX6h6XZa8ddxkrXXQ4rUHAOs8WTqlgOgcgPRZyIfMnl4N0mCh9ZLHV8qhBQMviDnjDXX4rWW8dPT43YVXlxfY4LOI-C3p_pzLJgmTcWy6VAOgJd7BClvcVEzVm23cTuFlLQpPAsbO9ZNlu7lt98zSIyrACE9Ta9lfH4pdyMEI40tLoJGy5zgbdjOQkRUhAsgSxBjhq4WHYYxLgUCp22844EmpNwTHmclvtn6tGszOknyzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ترامپ: نمی‌تونیم جلوی شیوع طاعون از روسیه رو بگیریم!
این ویروس بسیار کشنده و خطرناک‌تر از قبل شده و مثل یه ارتش شدن!
حتی با پیشرفت چشمگیر پزشکی هم نمیشه جلوشو گرفت، با این حال ما به روسیه کمک میکنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107883" target="_blank">📅 00:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107882">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bb309807.mp4?token=dV7Iyap42F3TRGOcrYg_3rcndgvnENVefcpR9UpJycG29TPWzyVwvhFrezsTVzuHC-aytkw4QwB3XrEVXrrF-3ZRXXxeiPNsj0nTqWpTbqIE8NgQdOzkkyI-dT6wy2KrhXKIafQpDaSDZzU8en3pSD680gJDUhvKijR55UjB4BqqD4LR3jO8bsMu6P4vaX_qvf_jSdtV5XHoZXJK8FLtCbTGSHy69TiBlfIPVwKFCw-VKevmrDN2ZR2qL0f5nbSO5_cYKzwZZpWFWvWNVBjoR3T56hFRMmP-8OmV1NWlr5mwM0epIFrEFyHJgAkPn7d3hJCPkZmsseaBycAVwQn1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bb309807.mp4?token=dV7Iyap42F3TRGOcrYg_3rcndgvnENVefcpR9UpJycG29TPWzyVwvhFrezsTVzuHC-aytkw4QwB3XrEVXrrF-3ZRXXxeiPNsj0nTqWpTbqIE8NgQdOzkkyI-dT6wy2KrhXKIafQpDaSDZzU8en3pSD680gJDUhvKijR55UjB4BqqD4LR3jO8bsMu6P4vaX_qvf_jSdtV5XHoZXJK8FLtCbTGSHy69TiBlfIPVwKFCw-VKevmrDN2ZR2qL0f5nbSO5_cYKzwZZpWFWvWNVBjoR3T56hFRMmP-8OmV1NWlr5mwM0epIFrEFyHJgAkPn7d3hJCPkZmsseaBycAVwQn1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
خاطره امیرمحمد رزاقی‌نیا از هم‌اتاقی بودن با رامین رضاییان: سنش را بگویم ناراحت می‌شود ولی مثل یک جوان 24 ساله تمرین می‌کند و در دویدن باهم کل‌کل داشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107882" target="_blank">📅 23:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107881">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d63f949c.mp4?token=mPWCep5PMqgCt0Gj1xmwFgj-xkG5ot2Dz7sLz5q-g_2O_S5zbafYvDLbLfjoHzy9vJvcSFVbGfJpXxWdtUrMG_w3t8Dw48l0ttvm5NYJ_VLW74VwfBlgKMPdnweiln9dqmXrdf86n-a1aCkv8tMBILGnAiLinD_VkHZwRAQPN67201F7Ij5fAMw3Nc3jD0ON8_cUlQhZAPfDicWSPkG2YUcN7nPdGH6YtB1v0JVPPWTorXE8Rr5nyktLEdAmXsQhX6zxgjEL85hqtnT3Jh--RvkmDXpzdirOpFX4zKLN4aw_IruvMzU4KScQC6-SQN00BN2oHAopvtzGHIEomTVw5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d63f949c.mp4?token=mPWCep5PMqgCt0Gj1xmwFgj-xkG5ot2Dz7sLz5q-g_2O_S5zbafYvDLbLfjoHzy9vJvcSFVbGfJpXxWdtUrMG_w3t8Dw48l0ttvm5NYJ_VLW74VwfBlgKMPdnweiln9dqmXrdf86n-a1aCkv8tMBILGnAiLinD_VkHZwRAQPN67201F7Ij5fAMw3Nc3jD0ON8_cUlQhZAPfDicWSPkG2YUcN7nPdGH6YtB1v0JVPPWTorXE8Rr5nyktLEdAmXsQhX6zxgjEL85hqtnT3Jh--RvkmDXpzdirOpFX4zKLN4aw_IruvMzU4KScQC6-SQN00BN2oHAopvtzGHIEomTVw5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سنگین ترین پرونده مهریه ایران اعلام شد:
اقای جراح ۶۳۶۰ سکه مهریه برای خانم با وفاش زده بوده و الانم تو زندانه
+ تا چند نسل قبل و بعدش هم جمع بشن نمیتونن اینو پرداخت کنن
😕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107881" target="_blank">📅 22:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107880">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
‼️
🇮🇷
بعد از پیمان حدادی، موبایل همراه مهدی تارتار سرمربی پرسپولیس پس از تمرین امروز سرخپوشان به سرقت رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107880" target="_blank">📅 22:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107879">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1743ee1f5a.mp4?token=r57FEiIvYMUEE-Q7c5O_m2H05k_CfvlT3PQJjficEtpwMlKuQUtORRaQkvV9ZhPKE_ZbBRmAwZ0u2Xxfv_xoey1Y4VR6ptDoC7m31YZzKQa2sTeMs2GwylouqBuCLoR38pNBZ19bMzEM6yYTmS8C4GIVbdgh65RpO3gE2VDRZOwRWQ987TJu0q8yDxlA3xZ1zX4B4mqBZmKHPysN4fwtX5EbvBX5l15CwNYHtBvRZpwokIhYa4-Ywp-7qZfQLn10nIYNly35lK8MfYMhYy_JK8qCbdPWqXiDVpqESeyktYvg2PdYJl8FLgH2w_ATjtHvoHRRZdULiWYUmSM0Y37cPDnI0NfbrE1ZrTupDKEhzrQTILal0eiRuJp_Nf7NRoykjivQ9ZF1SV7J3FDOSXiesa0MLfLer74IeU0d5n4yEbv3UeVjBCTaSiQTpzTpGrM9dnrIT3JSzOP2vR64c6RQN14aCig5WbVVHU3R1aipJbX4g2JXhM18AJjqZaOTfWva6kCAjQIKXRpR8bUSopdsL2-4nJsRV5F7RmUDrE9If9t3oOZuU_jsjmCRwQ6PZt8bNrzDQhEzZMm9mKD05aPNZH5c_XzZ9e73GgTmURtMiaUV_mpXtGmdVkWI8CLzSIZl2YexUENi4nxbIUvBWtCa8zM6Km9p0dcPYxNEF7I4ofc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1743ee1f5a.mp4?token=r57FEiIvYMUEE-Q7c5O_m2H05k_CfvlT3PQJjficEtpwMlKuQUtORRaQkvV9ZhPKE_ZbBRmAwZ0u2Xxfv_xoey1Y4VR6ptDoC7m31YZzKQa2sTeMs2GwylouqBuCLoR38pNBZ19bMzEM6yYTmS8C4GIVbdgh65RpO3gE2VDRZOwRWQ987TJu0q8yDxlA3xZ1zX4B4mqBZmKHPysN4fwtX5EbvBX5l15CwNYHtBvRZpwokIhYa4-Ywp-7qZfQLn10nIYNly35lK8MfYMhYy_JK8qCbdPWqXiDVpqESeyktYvg2PdYJl8FLgH2w_ATjtHvoHRRZdULiWYUmSM0Y37cPDnI0NfbrE1ZrTupDKEhzrQTILal0eiRuJp_Nf7NRoykjivQ9ZF1SV7J3FDOSXiesa0MLfLer74IeU0d5n4yEbv3UeVjBCTaSiQTpzTpGrM9dnrIT3JSzOP2vR64c6RQN14aCig5WbVVHU3R1aipJbX4g2JXhM18AJjqZaOTfWva6kCAjQIKXRpR8bUSopdsL2-4nJsRV5F7RmUDrE9If9t3oOZuU_jsjmCRwQ6PZt8bNrzDQhEzZMm9mKD05aPNZH5c_XzZ9e73GgTmURtMiaUV_mpXtGmdVkWI8CLzSIZl2YexUENi4nxbIUvBWtCa8zM6Km9p0dcPYxNEF7I4ofc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
کلید واژه‌های تکراری قلعه‌نویی؛
همه مقصرند جز ژنرال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107879" target="_blank">📅 21:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107878">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
‼️
💵
عادل فردوسی‌پور: دیگر حوصله شوخی‌کردن با قیمت دلار را هم نداریم
روزگار سخت و تلخی که سپری می‌کنیم/ شروع فصل لیگ برتر، با دلار ۱۸۷ هزار تومانی، بازگشتش از فیفادی، با دلار ۲۷۰ هزار تومانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107878" target="_blank">📅 21:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107877">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2122fb81.mp4?token=Ja15L9-5P8R8xae6S9mrGL5us28b8tLX2VXIHpWMwu6807si7DN9INbNoZAGnusZFPCeWPmQv8-B6-Trgiy-vcRLtN1jX9ai82e1RdwLgnGCCWETYUvtBnPEI6hPrhmf7PPA_3j_njUpdCVNeBWZiAgxQSHrv_AQhYgKk34W-Ag2NB5i2ADFPfk4VI3psIeNj4pLEo3Bhv412HVvyYQwdNRjy8nID07ZxaxdklD-DpPqpiwj40axJ9YPb9m5JfO-Me93kD6zGiRi680dLPFrLT-ntujkkgWjxd6c7g7pV0O0sEPyhIWoUaqmkBNNnDzdeigDborkFTgXSSGRtZpSMyBxTf6fyiuyHcQ_KyziKuQvF_T_-MOcCgHhbCTru-785lxs6TNpZZGu_-wxqF1prStX3oaIOPVUBcBSDcbwCgoZ8rc6dsSXe_DhuSBGZ8ELJycN39ITLawHlM5cFGgHlPsXtOhBQ_8lzNhNUoTuxHFpEn58lPEAahy6UTeaOeDV_ef-pFYycoQCWWcJCfoGj3JpWipLdi3IcbiVV1o7IcmKrdRby2QKxJIYJjp0wXt8QXPF5sT_M4OdFRzuvamdzZElBu2v6cf8qn7GiHmy4240o1PkEQOGMi_EN5hzeNc7fmWxBMzPbccdmyAYAnxHKdoDDmsGNeQuUaRq9LvHOGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2122fb81.mp4?token=Ja15L9-5P8R8xae6S9mrGL5us28b8tLX2VXIHpWMwu6807si7DN9INbNoZAGnusZFPCeWPmQv8-B6-Trgiy-vcRLtN1jX9ai82e1RdwLgnGCCWETYUvtBnPEI6hPrhmf7PPA_3j_njUpdCVNeBWZiAgxQSHrv_AQhYgKk34W-Ag2NB5i2ADFPfk4VI3psIeNj4pLEo3Bhv412HVvyYQwdNRjy8nID07ZxaxdklD-DpPqpiwj40axJ9YPb9m5JfO-Me93kD6zGiRi680dLPFrLT-ntujkkgWjxd6c7g7pV0O0sEPyhIWoUaqmkBNNnDzdeigDborkFTgXSSGRtZpSMyBxTf6fyiuyHcQ_KyziKuQvF_T_-MOcCgHhbCTru-785lxs6TNpZZGu_-wxqF1prStX3oaIOPVUBcBSDcbwCgoZ8rc6dsSXe_DhuSBGZ8ELJycN39ITLawHlM5cFGgHlPsXtOhBQ_8lzNhNUoTuxHFpEn58lPEAahy6UTeaOeDV_ef-pFYycoQCWWcJCfoGj3JpWipLdi3IcbiVV1o7IcmKrdRby2QKxJIYJjp0wXt8QXPF5sT_M4OdFRzuvamdzZElBu2v6cf8qn7GiHmy4240o1PkEQOGMi_EN5hzeNc7fmWxBMzPbccdmyAYAnxHKdoDDmsGNeQuUaRq9LvHOGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تصویر تکراری تیم ملی
بازنده اما طلبکار و با اعتماد به نفس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107877" target="_blank">📅 21:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107876">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiyREWXaycpn6Sv405mbF08PfaTA60R67Hea3CQSO2OqwHFKvfadlWLLMxSaUZl02Wjz2ZPeKYvq4gg2vODWKCtviGKfqyzIBQQwTdevCJsrx15iGFgtSNLT3YhMsqW5zXkMtrOgIqTcv-aCEPJkale-qME6NXmN2wErJFpNFAv7JQ8KVldNBPXogLXYtd91UHeDj9k1WC2KBvS_LItU8WKkHlUuerJB3M9IKJYHAf7-J5MjtN0Uy2sbAhMadNONcFkC0V187prmYDk4V2dqJk4w6Xkd28bLraVcRPEYz0MjEUMZY9H1nOv37r35ZR8UXgRPAYNOHo6tydRfRJsR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107876" target="_blank">📅 20:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107875">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f2c09e35.mp4?token=bO71ZYKr2yffFH35g94Jj6HMLRvNzXSMSUVr6L-4o-LmQu1rpUV2izQ6v-IoW_tL1Qg_dAywH_MBsbFHxnuhimhS6ZcN7oRpORUqGvM-UEjyUk0LEbUxlh3zDRg5PDnjrc7Ue02yVTHdymVOSv2m2At-VxbtBmT53OOmOUDPrBjNTuhCTkk1hRlAb48KW7QhURI34HyLliiXkSWxCront8Vkm5sHjCjq2dxkx-jrAcmURXbFp5gqPLsipqRrNyZOOcojZ-iVWkap1K60JEwmpYZdjGzLMZOAE8qo8nhLZUq2jyljt6i3HQpNsHGRV3Ikjje0wR9yjhNoDGOy-txfUpzN_Czl9ldIZD8arI8Q1zDXbep9nu0I1IBqlxOrHn9aonlM3j5k6wJELIpzJJ6U7i0HyP6ehUrHRsMOS6ebSoSRfL6bdUNCi76wnZFsKqXtaUedCO6ofYiU5kUjYucRROrPYDSxGNxTeeyg2CWhjgt1UoB36fjZrhNX7BcvPTjDGeR-AHAQS3ipTbYp2nzQWDvfstGClX6IgFUOaEGkXhS8slafcVb9Gab6P4-u9qLffTcvhIll09Uumrpza9260OhlMn2cDGNP5lKspAR3QT2v86rs-I4Rpf2-WM8suoqmT2n4AxZTnE-H-g2x9EGIQYfka0dhyLocKVWtG5iKxPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f2c09e35.mp4?token=bO71ZYKr2yffFH35g94Jj6HMLRvNzXSMSUVr6L-4o-LmQu1rpUV2izQ6v-IoW_tL1Qg_dAywH_MBsbFHxnuhimhS6ZcN7oRpORUqGvM-UEjyUk0LEbUxlh3zDRg5PDnjrc7Ue02yVTHdymVOSv2m2At-VxbtBmT53OOmOUDPrBjNTuhCTkk1hRlAb48KW7QhURI34HyLliiXkSWxCront8Vkm5sHjCjq2dxkx-jrAcmURXbFp5gqPLsipqRrNyZOOcojZ-iVWkap1K60JEwmpYZdjGzLMZOAE8qo8nhLZUq2jyljt6i3HQpNsHGRV3Ikjje0wR9yjhNoDGOy-txfUpzN_Czl9ldIZD8arI8Q1zDXbep9nu0I1IBqlxOrHn9aonlM3j5k6wJELIpzJJ6U7i0HyP6ehUrHRsMOS6ebSoSRfL6bdUNCi76wnZFsKqXtaUedCO6ofYiU5kUjYucRROrPYDSxGNxTeeyg2CWhjgt1UoB36fjZrhNX7BcvPTjDGeR-AHAQS3ipTbYp2nzQWDvfstGClX6IgFUOaEGkXhS8slafcVb9Gab6P4-u9qLffTcvhIll09Uumrpza9260OhlMn2cDGNP5lKspAR3QT2v86rs-I4Rpf2-WM8suoqmT2n4AxZTnE-H-g2x9EGIQYfka0dhyLocKVWtG5iKxPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
بررسی ۵ نکته مهم در جدیدترین نسل‌آیفون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107875" target="_blank">📅 20:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107874">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce1470830.mp4?token=q4eXeJsunBFc4GO1SXabE4mfDY0hUkf7BH5eaCJrFDll0kr8xB_9IYMxgiPTF_9lY9FZr94LZF1Q4iph1V6lXlh2l-c2UmGiWdu5zSGlwDzEkOGFzxfP88cP3z7I27NuD321YTq0pkzu7gJuuF16xDzGpdiZyfDZtIPHG0XU-BDBUBscFaZr2zIol5heB7xTD0hmTcigTbgFPW1GIKjx9IMc9oewFRGpZ3XcI1wg7z46E8g-4KtJTH8ZNMci2ERoh1VY2STLD-y0_EqRe_84nbDC6wC7cPvHkrfQE_Ori2ZxFv4b_COleHzQ94ig00MxaTGD9Be6X4v86EI_PH0bcSx3Fp3zGz9ZN6ruq1oI6yRzscb8-fkf4Y_lVxqqc1sv5fW9dAoaWAlgXphsJoTnpcIkppNYYflTDFyxzJJEzg-a_3hsHRpyEeEHwTYCBpy6Q59Id8NCy-PIm9Bb2jFJYvngGJg6xWeAtFrGGWehx3Dz0BAzF1UaBdJVEGCwdgzdsi3-Eqi1YeuA916UAClhA-clKwzGwLEeY3yByooP2Py9pSGfJovKUF4C1toB9Bjb_NCwdLCArSCBMPGi8Hdk1S_5nSTt7IXxJ2W3fzcTlTtgkdtyUO2bFazeJJURHBFMcdKCpYmgfekcptWxFJCUPfrvOLSyTHn62aT2kh8nXu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce1470830.mp4?token=q4eXeJsunBFc4GO1SXabE4mfDY0hUkf7BH5eaCJrFDll0kr8xB_9IYMxgiPTF_9lY9FZr94LZF1Q4iph1V6lXlh2l-c2UmGiWdu5zSGlwDzEkOGFzxfP88cP3z7I27NuD321YTq0pkzu7gJuuF16xDzGpdiZyfDZtIPHG0XU-BDBUBscFaZr2zIol5heB7xTD0hmTcigTbgFPW1GIKjx9IMc9oewFRGpZ3XcI1wg7z46E8g-4KtJTH8ZNMci2ERoh1VY2STLD-y0_EqRe_84nbDC6wC7cPvHkrfQE_Ori2ZxFv4b_COleHzQ94ig00MxaTGD9Be6X4v86EI_PH0bcSx3Fp3zGz9ZN6ruq1oI6yRzscb8-fkf4Y_lVxqqc1sv5fW9dAoaWAlgXphsJoTnpcIkppNYYflTDFyxzJJEzg-a_3hsHRpyEeEHwTYCBpy6Q59Id8NCy-PIm9Bb2jFJYvngGJg6xWeAtFrGGWehx3Dz0BAzF1UaBdJVEGCwdgzdsi3-Eqi1YeuA916UAClhA-clKwzGwLEeY3yByooP2Py9pSGfJovKUF4C1toB9Bjb_NCwdLCArSCBMPGi8Hdk1S_5nSTt7IXxJ2W3fzcTlTtgkdtyUO2bFazeJJURHBFMcdKCpYmgfekcptWxFJCUPfrvOLSyTHn62aT2kh8nXu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کنایه‌های ژوله به داستان سربازی دکتر بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107874" target="_blank">📅 19:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107873">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2ddbc7f1.mp4?token=XYeLefSp02jVgyaq3_OoUZ-3LFs2Yj-SsgT6fFHCvOcMd8FKoBqJrrjSRWL00SQLbN90R52RFMFdH3wjodxEvnytOemmYCP7he0lkwmE6s3pjp6fo5undAshZrl_vchVdcBYLu9WCMRNeQMSGJMxA8xMoDvtZQgFxqfeZho3iiTewozBzyCzYNjpj18f2Jy9UoQ1H8RagkZUYljZPHHp3aRrkrW2pEasJOzjrw0ZCKPKLwVoKa31arGWf0DhJ4u8XPS0JD_FPHhDqD2EFZDO6_FzgL-N293k3LqkiVLfdM9za1JMP9_V-a_fJZ2R6M0a7tnCx9QA5U0gUTctthXJaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2ddbc7f1.mp4?token=XYeLefSp02jVgyaq3_OoUZ-3LFs2Yj-SsgT6fFHCvOcMd8FKoBqJrrjSRWL00SQLbN90R52RFMFdH3wjodxEvnytOemmYCP7he0lkwmE6s3pjp6fo5undAshZrl_vchVdcBYLu9WCMRNeQMSGJMxA8xMoDvtZQgFxqfeZho3iiTewozBzyCzYNjpj18f2Jy9UoQ1H8RagkZUYljZPHHp3aRrkrW2pEasJOzjrw0ZCKPKLwVoKa31arGWf0DhJ4u8XPS0JD_FPHhDqD2EFZDO6_FzgL-N293k3LqkiVLfdM9za1JMP9_V-a_fJZ2R6M0a7tnCx9QA5U0gUTctthXJaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممکنه دفتر نُت موسیقی دیده باشید ولی ندونید چیه
این ویدیو کمک میکنه تا کشش زمانی نُت‌ها یا مدت زمانی که یک صدا یا نت ادامه می‌ یابد رو راحت متوجه شید
و به هر کدوم از این نت ها چنگ، دولاچنگ، سه‌لاچنگ و ... میگن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107873" target="_blank">📅 19:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107872">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd348ccf0b.mp4?token=kSWg_cxMWhLkd5NRRu7ctdPnMhiR3n1vPZrzPcSaP-TZ5Tbou0iT_iwRF7GFs7trEqVV_CrD_z5jLro7ET3OsFN8s_-q9J9nHW9gpTTvDUXr_6Krf1IMsbdoxUPMAu8GrawJBlW3PD7SqOF0zUJUO4fkqJ7BI1LCB7rIIqw76gWgfOBgOQTY7LuVRu5oUGdLVvMs_N1wlPAmXjhfATeNThUenmra8VK92YAM9C1pB6CiIAh54gSjmKoreGExUumCmqUYhZCRN8T78KvtCsidZ7shERFsi4xvxY0LABsvpbFujnZ7v-gW_JeTEh9a7W-JePY-87Bqca5IiaU1lrujiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd348ccf0b.mp4?token=kSWg_cxMWhLkd5NRRu7ctdPnMhiR3n1vPZrzPcSaP-TZ5Tbou0iT_iwRF7GFs7trEqVV_CrD_z5jLro7ET3OsFN8s_-q9J9nHW9gpTTvDUXr_6Krf1IMsbdoxUPMAu8GrawJBlW3PD7SqOF0zUJUO4fkqJ7BI1LCB7rIIqw76gWgfOBgOQTY7LuVRu5oUGdLVvMs_N1wlPAmXjhfATeNThUenmra8VK92YAM9C1pB6CiIAh54gSjmKoreGExUumCmqUYhZCRN8T78KvtCsidZ7shERFsi4xvxY0LABsvpbFujnZ7v-gW_JeTEh9a7W-JePY-87Bqca5IiaU1lrujiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت پسران و دختران پس از نتایج کنکور:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107872" target="_blank">📅 18:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107871">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyG4K6P0aZbTy-h8FCJNIbLMp-Melz7K43iVvLO4HYOThwXIYtqvyMFxxsq6FVGRsLKJczAMww8fzJgDYNroXcEyqI2ewgbIbChvW03EIKzNQzPBwc0Q5br5J-HpUu-HF_wTYTnwQXlzJJewK1ESHAs5lbJy5X2syZJll1Tqd5nvW7Yr4jNwplMCNu8UYNrHoRa3lTGjy3ZcVaedLdybs3T9SahhpuxCczUorG1Kdy4uJyI4Frd3VHC4kJji76Gh_J9dYV8DiJ7GrHJz0ozqLHoi4aCd_APOUWdpBijJ_J1IJQ0iY0ZmEl1fSJQamOSTr8GQPFCrcF8MEhyzgDLbLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
فهرست نامزدهای جایزه گلدن بوی بعد از کاهش از ۱۰۰ به ۲۵ نامزد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107871" target="_blank">📅 18:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107870">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6601bb6094.mp4?token=CVqyqQse3snUYe9a6Jh2-YvhBxCPV8PVfrGX8HnynX7N4dEeq8PlZlbWQxxNKWmOZ7WXn35yqrdfs1-W3flQf7sXujmMvnciHGylEyGmKH01xH4KYsyNg1eAmTJi4HbcqbqWhAp0Efy_qY9KiBO5kTnfK2FvH34RSA4SfLJQJoATAfeSqF8kbOFC2kXGA6YnxAUfub3RaTcfMJEmm_Pqx5HNnHF_JT9CdZ7VsWKYASrsIUzJGTyPh0-TdHv9E9vRA-2uiqfE3RrzS0w_vNzO_v0S1RxrImtbU4D4t8EHrpgEhOTlEUMZvS58eBTiTgmcFY6IYMlK1tZTyh5MhNYT3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6601bb6094.mp4?token=CVqyqQse3snUYe9a6Jh2-YvhBxCPV8PVfrGX8HnynX7N4dEeq8PlZlbWQxxNKWmOZ7WXn35yqrdfs1-W3flQf7sXujmMvnciHGylEyGmKH01xH4KYsyNg1eAmTJi4HbcqbqWhAp0Efy_qY9KiBO5kTnfK2FvH34RSA4SfLJQJoATAfeSqF8kbOFC2kXGA6YnxAUfub3RaTcfMJEmm_Pqx5HNnHF_JT9CdZ7VsWKYASrsIUzJGTyPh0-TdHv9E9vRA-2uiqfE3RrzS0w_vNzO_v0S1RxrImtbU4D4t8EHrpgEhOTlEUMZvS58eBTiTgmcFY6IYMlK1tZTyh5MhNYT3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
میگل آلبوکرکه، رئیس دولت منطقه‌ای مادیرا، زادگاه کریستیانو رونالدو:⁣ ۳۰ سال دیگه کسی یادش نمیاد کی سرمربی بوده، کی رئیس فدراسیون بوده یا کی کارشناس بازی‌های فوتبال بوده؛ اما همه می‌دونن رونالدو کیه.⁣ این تفاوت بزرگی و معمولی بودنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107870" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107867">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InNM-hEbTCe7RYvck5WjLVB1SxBSzBCQmrWw0R16nIf4xr_SM-Y_nADTxF958swLZVbLinvZFY7IgoBhxj4q3WytpgP10XpHAHJvoeFGvyoX_O1FH5tHDRLRo8zq07etOpzybyKXLBiAyCCB8mUPIRQQXLKJR8qM5Q_gPavsF28z27U7duzNq8t19lEsyphe6u8rolzerHMKp_iBUfyiWTpiCd2yFy1Z53QsZGZ23cKkoynEHcCNJl2MCNS70Vb34J0qR3QgRJs1c93IaeTGEsUxXi_hyZhovVR7KO48MN_WtI0_lsq8XSelWy4JpPJojVwjcJoFnwAEdWbiGOXvGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
گونزالو راموس در هر سه بازی اخیر خود با تیم ملی پرتغال که به عنوان بازیکن اصلی در آن حضور داشته، گلزنی کرده است.
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107867" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107866">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1c39a914.mp4?token=hSa1EYb4dk7C1LBjSqk2QVOBuu9sZ6i027F5iFN5yA85Ed0Joz5Qhgh119qZSMrzUhZqI13lbewnmzCW6MkkgKCHTmYarMyXn50s5D5eLHkJTXiALOPLW8z28OlxpLB-ewRZn84XQSq-Ty6T3gbRCqlVJkSWDhmi-NOtJxa39OGIs8SNch-DqphPrpzgZpftjIjA_O2D5TL7gBqiIpkQEEXOCs-wpYr1R-b_iw59OKpfyeZufWJeFarKd_mkfUqg0e22lYVU7Tc9L1grC2a-VijmFRgkh9Owf7Ah9G03q5hcbG8YsqDjYiJTBb7MLsRbhOY4SXWpgfITqln66VxZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1c39a914.mp4?token=hSa1EYb4dk7C1LBjSqk2QVOBuu9sZ6i027F5iFN5yA85Ed0Joz5Qhgh119qZSMrzUhZqI13lbewnmzCW6MkkgKCHTmYarMyXn50s5D5eLHkJTXiALOPLW8z28OlxpLB-ewRZn84XQSq-Ty6T3gbRCqlVJkSWDhmi-NOtJxa39OGIs8SNch-DqphPrpzgZpftjIjA_O2D5TL7gBqiIpkQEEXOCs-wpYr1R-b_iw59OKpfyeZufWJeFarKd_mkfUqg0e22lYVU7Tc9L1grC2a-VijmFRgkh9Owf7Ah9G03q5hcbG8YsqDjYiJTBb7MLsRbhOY4SXWpgfITqln66VxZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
آخرشم نفهمیدیم بارسا چجوری تونست 8 تا بخوره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107866" target="_blank">📅 17:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107865">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-AXogv6YkD8DJdggkuCKkqRLKaIjX_h74xi0GjyZa4PhmiwOy6zdDEJPoTNBCwPlvS4YbgjxEzcxpcspg03pDG7piWBL82cJhyA3eh8nJFgyrg_oCPVuhGgwMamCDLaGRKw98R0nMBEaa_nGzlM-lDtwOKU-supiF5xvSopOZBpgEfxCdfLDBH80d7Ij0efoJj17l2x06SrZMRd_FP_JOqW55uxhQo_svUjnVHXRY6z8CkCiiK8nELnou4wsqlQV3LQ2cYTSU4IFfKnHaxCusTeRMHS9QPzcP7pFDhZvL7Bp-j0195WaUtEn3k_WRtCfgkhlQhyrQ2nZPiPkzHS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس جدید نیکی کریمی در 54 سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107865" target="_blank">📅 16:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107864">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579a3c3bc.mp4?token=MPwlYp3SSyH16wGr2JT5C5D1igvGSbBCO8aV6hWHUvaLx-9gNja2k-ifQdMA8r3g2jNoi8IGadt5b7mlNc01fjIIVoDM3d56bE6c8HY8BCMFh0Wf57fPSSanU2I3pT5_eL0yTSVSRlGE3AOOTRt6zpExn6FGC5-wEkvyJQbLNiSgybND4f4PRx0LaucyA1WfT60-ktvdzUTeZuSVzmfkKB5WY2G1SzceUgE7orwwJ4xXIvB3hWW-WCfqE47EkYNt-S4SYegQzIgwpcI_U7L98GSs_8mFed1hJ0xRu1ImQPNSQS4i1HLMY0dV0nfb_tbbo5emWk9pwzIDDesda9zp7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579a3c3bc.mp4?token=MPwlYp3SSyH16wGr2JT5C5D1igvGSbBCO8aV6hWHUvaLx-9gNja2k-ifQdMA8r3g2jNoi8IGadt5b7mlNc01fjIIVoDM3d56bE6c8HY8BCMFh0Wf57fPSSanU2I3pT5_eL0yTSVSRlGE3AOOTRt6zpExn6FGC5-wEkvyJQbLNiSgybND4f4PRx0LaucyA1WfT60-ktvdzUTeZuSVzmfkKB5WY2G1SzceUgE7orwwJ4xXIvB3hWW-WCfqE47EkYNt-S4SYegQzIgwpcI_U7L98GSs_8mFed1hJ0xRu1ImQPNSQS4i1HLMY0dV0nfb_tbbo5emWk9pwzIDDesda9zp7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های رسول‌مجیدی درباره سختی مربیان تیم‌های ملی بدلیل زمان کم آماده‌سازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107864" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107863">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ea1e2bc4.mp4?token=NdTGq6nryZCkwJSd3VauFzYfZYim6YO-1mHlg12mkj2mDZXWkbMTx1048BGP7iCXyX-kYSx6DkyBGHYccZech6DpCZ48_4pGJ-cC0KDihtcj39ji4ZCwrvLEPiTzCDGh6B_q00wQ0esm_yszi_pcvLHftySkXNn8P4Y7DRwYPcar9dwx5QYyfHxX-JcQA5CckrlBe6fmzR3ggS6SbbqV81yrFei-OFobxpmMU4BxYlTduyDD2GjmIJZ4Tr_GgCm0rGyL6_QqhJaCJraVkHTswt1oxCue9QQ4MeN2PjTX_1P5nKKM8Mdn6_w852OdFekCW3CtrUTD-obD7u_buo69WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ea1e2bc4.mp4?token=NdTGq6nryZCkwJSd3VauFzYfZYim6YO-1mHlg12mkj2mDZXWkbMTx1048BGP7iCXyX-kYSx6DkyBGHYccZech6DpCZ48_4pGJ-cC0KDihtcj39ji4ZCwrvLEPiTzCDGh6B_q00wQ0esm_yszi_pcvLHftySkXNn8P4Y7DRwYPcar9dwx5QYyfHxX-JcQA5CckrlBe6fmzR3ggS6SbbqV81yrFei-OFobxpmMU4BxYlTduyDD2GjmIJZ4Tr_GgCm0rGyL6_QqhJaCJraVkHTswt1oxCue9QQ4MeN2PjTX_1P5nKKM8Mdn6_w852OdFekCW3CtrUTD-obD7u_buo69WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
بیرانوند تو سربازی اسلحه بازو بست کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107863" target="_blank">📅 16:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107862">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367af750e7.mp4?token=DYjPGo3Wed_P54c9Zf3C3-GnitLhIaCf14NhrXeMHlJCc9H3ts-GKRjPKvagjc7JsBDMSDaGlh7hIuyQFccpYLbjBmh5q0ViCKcSGokRintvHSg5bUtQYLZT45zY5Y-bLEwLgdLkNdQZZMCmz1msRwgh1FyZmOF0s_qNGQi-23BvMMUmZbgIJffFG3Xs2-hkJHITu6BkqvkYjfuPF0R8Ib_056bf820rkiMwX9N-NJsUYGpuBLGfzr5ni4vbHBWdsVpHfZdaSmOPPq35rENJkQlWmdlbSb0sTK8AaOMeQj3H3oIujeg4llE3V77GK3IurW7qiRNXwyltnVb4sS78uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367af750e7.mp4?token=DYjPGo3Wed_P54c9Zf3C3-GnitLhIaCf14NhrXeMHlJCc9H3ts-GKRjPKvagjc7JsBDMSDaGlh7hIuyQFccpYLbjBmh5q0ViCKcSGokRintvHSg5bUtQYLZT45zY5Y-bLEwLgdLkNdQZZMCmz1msRwgh1FyZmOF0s_qNGQi-23BvMMUmZbgIJffFG3Xs2-hkJHITu6BkqvkYjfuPF0R8Ib_056bf820rkiMwX9N-NJsUYGpuBLGfzr5ni4vbHBWdsVpHfZdaSmOPPq35rENJkQlWmdlbSb0sTK8AaOMeQj3H3oIujeg4llE3V77GK3IurW7qiRNXwyltnVb4sS78uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
با توصیه‌های هانی‌رامبد، اینجوری شانه های پهن تری میسازی؛ ذخیره کن و بفرست برای دوستت
❤️
👌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107862" target="_blank">📅 15:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107861">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4AjCplWt6tyW9T9dsiFOPtnY6b0l2f4kVaDUTuMhJ-_gpMfiwlKZYBVRRHjmb7rok44sErdnnZgDTAP_5djEWmT-HOi2mu4M08hHWuTqy12g61hpHDHsVhR58S1jYfuE594WYqouZould7aM9NI3A96HP8N9P1MQQpRCCcSH2JKVLYSxToam8m6N7BYWNrfA6b84Fnl2T_AfIxdPy_KU8HIyMkO9TsrL9yGtXmKVHgoVR7yRU8b8DclxqUbOzl5Nbu5Ni0y-GR0aWues-y9YTLtNby0XJ8Bphj8lp_d1ZFrc44AbEwcwdm-bBsp3Lcg3Pxnt3zJxOsAxMQbLkYU8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
اسپانیا اولین تیم ملی مردان در تاریخ فوتبال است که 41 بازی متوالی را بدون شکست به پایان رسانده است.
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107861" target="_blank">📅 15:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107860">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6f99cc68.mp4?token=nnkTJVtIRPdwPHdwN7sVG227zYeNGJlFbvHBoJb0kNTlVTifvDhozl82q-qKYomgbOAmY46l_nURYwLDByonjySHy1si-YI_pL3XSi4ZkE0d1Qy2m3SfwHKzyErxlcijkMQJXHAKoxrbgF4cby0hmCJySYDCvHb_K57CKDyQMO5A92JWMCG7VGzUuERSma9lu6MHIE0SKADzpY3zEIJPYjG7sryGqudTq0zqguM-bSv7AnQRB697KLPDRkrzt-zVz3pXSSb_O4bH4ZqiNLrx4kyzlj9F-CpxAvfJbrkWfJXuhrFzmeee9MRHJKV_w7WlhrFVXeV8YuVaVyeHGjnulXMqUJwb3LX9u6Od7nJJBFUw-JicNHRQObuDlsP3XKspe4NKF6qUJdtfVYlMQYvuSXxV6Y2CsKTOI3Ku30n-0Pm2UAkLThglPDCTxZH9ppYz-yenDOxvYiCuWhofbLN2-Y2qFum_oy63_RCFL7RkGPy5BA9zdpdGZHZVOHqkPY0YFsrBWw00k2Gisl4ilR27OJlZJtiipLpaLmI2MTXkO6dn2MQHgnww9_vEftxXtM6pWrqwO2RZeQgHL-_HiReAa9UWKxPw2N-ZDYwhsVJ5CGsmdRBBFngzDc-0fZkRLhf293tzFhGRFpAORvPXDV4mFUFhyTrm8xjBV_SADiGwmN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6f99cc68.mp4?token=nnkTJVtIRPdwPHdwN7sVG227zYeNGJlFbvHBoJb0kNTlVTifvDhozl82q-qKYomgbOAmY46l_nURYwLDByonjySHy1si-YI_pL3XSi4ZkE0d1Qy2m3SfwHKzyErxlcijkMQJXHAKoxrbgF4cby0hmCJySYDCvHb_K57CKDyQMO5A92JWMCG7VGzUuERSma9lu6MHIE0SKADzpY3zEIJPYjG7sryGqudTq0zqguM-bSv7AnQRB697KLPDRkrzt-zVz3pXSSb_O4bH4ZqiNLrx4kyzlj9F-CpxAvfJbrkWfJXuhrFzmeee9MRHJKV_w7WlhrFVXeV8YuVaVyeHGjnulXMqUJwb3LX9u6Od7nJJBFUw-JicNHRQObuDlsP3XKspe4NKF6qUJdtfVYlMQYvuSXxV6Y2CsKTOI3Ku30n-0Pm2UAkLThglPDCTxZH9ppYz-yenDOxvYiCuWhofbLN2-Y2qFum_oy63_RCFL7RkGPy5BA9zdpdGZHZVOHqkPY0YFsrBWw00k2Gisl4ilR27OJlZJtiipLpaLmI2MTXkO6dn2MQHgnww9_vEftxXtM6pWrqwO2RZeQgHL-_HiReAa9UWKxPw2N-ZDYwhsVJ5CGsmdRBBFngzDc-0fZkRLhf293tzFhGRFpAORvPXDV4mFUFhyTrm8xjBV_SADiGwmN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
پیت هگست در سالن «کلون آرنا» در آکادمی نیروی هوایی آمریکا، در یک نوبت ۹ شوت از ۱۰ شوت سه‌امتیازی خود را به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107860" target="_blank">📅 14:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969710a175.mp4?token=YNT-CrCpZbb7akcmGF5XA8Afp0ArdVryAoN0gTitd_pD5C9mdHFp-HBB62aarC1nQiWvki25WwYU3qtUvZMAV2BlQGSzVt_qK25N5fhzFFHxSi5IxU_GbN31ajkctzSJgIjerljAhRP1SWNSKtSTUjROAvPWwLN5OPbFguE8jmD55hH8ISyDOo8SSl2vQ3uq6jpd3fv3Lq3zrgC5D_imqt2fseCy60G4kjKhgvL7v-iG2xeCwtrkGPPgti5R2UjnR14ll-UExwDWYm4Xq8Tt3nq8lKojbO-tuk6lfp_ksR4AuSj2e2yVCeIbAWw46wJPC_bnRnAxPCbPvP64zzVIxDQlYDqUUmGoDSTtBNf7pkMBar1_E7XDzIEy1T6baCBTnLX7gmI2afSrrVry1KM9irxzaCcWplWD8PWZx4-D8d8hoMD1vSpQJDT78YDKqEVM16edNU90QyqwkiHvj4jILFFNYd1l9NgWnmqf4k7BhA6VALspAGnzeDAgqL_So26B6n0ZF9QMs5ScffkxLC2ZP2E4MfLcR6rolxbmzErICyVkyAY4PY3Ca-vIWzy42fQlfmUmGg9UxLentQ9474MaBfXROz9K8j-SW4Y2S2yrfl_gW9-76UpMorUU5aYdFr863MHTPvkhH8KaUNpSRmovhxPBSg582ggrl0Lg0CLOBIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969710a175.mp4?token=YNT-CrCpZbb7akcmGF5XA8Afp0ArdVryAoN0gTitd_pD5C9mdHFp-HBB62aarC1nQiWvki25WwYU3qtUvZMAV2BlQGSzVt_qK25N5fhzFFHxSi5IxU_GbN31ajkctzSJgIjerljAhRP1SWNSKtSTUjROAvPWwLN5OPbFguE8jmD55hH8ISyDOo8SSl2vQ3uq6jpd3fv3Lq3zrgC5D_imqt2fseCy60G4kjKhgvL7v-iG2xeCwtrkGPPgti5R2UjnR14ll-UExwDWYm4Xq8Tt3nq8lKojbO-tuk6lfp_ksR4AuSj2e2yVCeIbAWw46wJPC_bnRnAxPCbPvP64zzVIxDQlYDqUUmGoDSTtBNf7pkMBar1_E7XDzIEy1T6baCBTnLX7gmI2afSrrVry1KM9irxzaCcWplWD8PWZx4-D8d8hoMD1vSpQJDT78YDKqEVM16edNU90QyqwkiHvj4jILFFNYd1l9NgWnmqf4k7BhA6VALspAGnzeDAgqL_So26B6n0ZF9QMs5ScffkxLC2ZP2E4MfLcR6rolxbmzErICyVkyAY4PY3Ca-vIWzy42fQlfmUmGg9UxLentQ9474MaBfXROz9K8j-SW4Y2S2yrfl_gW9-76UpMorUU5aYdFr863MHTPvkhH8KaUNpSRmovhxPBSg582ggrl0Lg0CLOBIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فوتبال معلولان عجب صحنه‌های فوق‌العاده‌ای داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107859" target="_blank">📅 14:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e41c5067.mp4?token=LAeZGVp_YlsAvhcYkpFcf1DGAqYyHH_oRvHOqFvsqTE01Bkj_YMALVsSeMsdAfiy1b9ZYdC7K5PGfwMNcKCtOfjIhaHgDYikt4UUbBKgeLK3d1v_DPUKPgqlPHbfE-59F5yuvFQBwPEHepCM46uvS0JrMruF18ugHyhnPixBzuxpLeiZ-9HziNyWJtryBBbuSjvkBniM3L3ZZRm3JUWVxBY37ctePWZB0lIRDKxk-rkM185s7412iJ-JzlSSVEIc5RX6YjoDyfUYSFnnTvTHycAg2Y0ktZqDf-zOprsfXY55IE9zCA4iR1wiJZdmvteLvVYB30zpl6pCDMizREcstg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e41c5067.mp4?token=LAeZGVp_YlsAvhcYkpFcf1DGAqYyHH_oRvHOqFvsqTE01Bkj_YMALVsSeMsdAfiy1b9ZYdC7K5PGfwMNcKCtOfjIhaHgDYikt4UUbBKgeLK3d1v_DPUKPgqlPHbfE-59F5yuvFQBwPEHepCM46uvS0JrMruF18ugHyhnPixBzuxpLeiZ-9HziNyWJtryBBbuSjvkBniM3L3ZZRm3JUWVxBY37ctePWZB0lIRDKxk-rkM185s7412iJ-JzlSSVEIc5RX6YjoDyfUYSFnnTvTHycAg2Y0ktZqDf-zOprsfXY55IE9zCA4iR1wiJZdmvteLvVYB30zpl6pCDMizREcstg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سمفونی خیابانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107858" target="_blank">📅 14:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5554fbfbba.mp4?token=BzgWyHPrgB1fl0fk3pSUp_AIlxmydD0M2cAyHVMyBmUZKFWNNb3UkrzFDhgWkUDpS4u1SJTpgpYOJBjU1X5FXsv5XmKhw-QY20JYRJdi5-3kGLYT0YHdOybk5moQ3ebmUtTMd2amnlrB3AB3O5T8UCjCqHr4IqKgbtzr1CjPFQ1hlDdpMJPxiZip2Fok1BQfSltme_udMDoM-3lU6RKT4qQywMtIL3Sl1BsmGlmmgPyAR6G7ArSceufR7KQ5o-pdXPIPDUDPdUaXikHS7nqkTG_nlrvbC9f0oi1U-IsXxdqztUR6G7EF-BZOrBi1NNZEEaA2gw99dMEs-Da46-g7Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5554fbfbba.mp4?token=BzgWyHPrgB1fl0fk3pSUp_AIlxmydD0M2cAyHVMyBmUZKFWNNb3UkrzFDhgWkUDpS4u1SJTpgpYOJBjU1X5FXsv5XmKhw-QY20JYRJdi5-3kGLYT0YHdOybk5moQ3ebmUtTMd2amnlrB3AB3O5T8UCjCqHr4IqKgbtzr1CjPFQ1hlDdpMJPxiZip2Fok1BQfSltme_udMDoM-3lU6RKT4qQywMtIL3Sl1BsmGlmmgPyAR6G7ArSceufR7KQ5o-pdXPIPDUDPdUaXikHS7nqkTG_nlrvbC9f0oi1U-IsXxdqztUR6G7EF-BZOrBi1NNZEEaA2gw99dMEs-Da46-g7Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
ویدیو جالب دو بانوی کاروان ایران در ناگویا و خوشحالی بابت کسب مدال در آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107857" target="_blank">📅 13:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107856">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedf090cb4.mp4?token=sORuz-tIL6AC5iXAPi_izmh-liTWQCQrXpWfy3mKgE2LdkGM8Qih2497bWeXUlgYsJ-yqy-keqQW8faCpMB7j1qzqbTZbckBWbtBUhECHu-b1Mp8KbBvj0xBhhxyy3bfm7uKVkDzeHqnRxlRdUwIOPITVXoqnraexEApMmx4Q3U8nUytn63LMq2IxOiUAwkesKU9PQLVKU8qGZxxe58gU_P_SgJjpor0UjXNOUMOHjg1aha6yH5ItrZFUHFBgZQIpmXwjliUj8eTpHTIeWG2BRnfRPN2QZPet4VqNBYv7uixkbiEB07c7MAy0xORxwVmBVLKJiVrM2Wu5Hj4S1IQug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedf090cb4.mp4?token=sORuz-tIL6AC5iXAPi_izmh-liTWQCQrXpWfy3mKgE2LdkGM8Qih2497bWeXUlgYsJ-yqy-keqQW8faCpMB7j1qzqbTZbckBWbtBUhECHu-b1Mp8KbBvj0xBhhxyy3bfm7uKVkDzeHqnRxlRdUwIOPITVXoqnraexEApMmx4Q3U8nUytn63LMq2IxOiUAwkesKU9PQLVKU8qGZxxe58gU_P_SgJjpor0UjXNOUMOHjg1aha6yH5ItrZFUHFBgZQIpmXwjliUj8eTpHTIeWG2BRnfRPN2QZPet4VqNBYv7uixkbiEB07c7MAy0xORxwVmBVLKJiVrM2Wu5Hj4S1IQug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های متواضعانه اسطوره مهدی‌ مهدی‌کیا درباره اختلافات بهترین نسل فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107856" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107855">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54734be7bf.mp4?token=qvHalzK7mtKBBzJhN7z9fiqKG4IEOcaHMwPqcTPvsxPrgqvNahZzz-icNMay1luO81gNPe3mOBJXzYcw5K2I0az_1SKgfTsP21zO3gXKN-5jr0Umnd0MJ1EXS_yjgbfsz1RKQ7YIg25ZzFAZp18StfkiPH-aNFsB_QxbiqoIA9MFDuam-MSoO4addGXAjMY6ad_lF4l5LLMQVrA0aseLIuB21vupZQWloiX0MCE4D2OZc_wxVH03xcHhJEmvtEopm_rxyzMpZiN5E5tj5AgxpyKewXab1GSsIyrPBwJYkoLfsil7d6grMtJx94GhtzMpbScEfvKl7SZKjFRRXxJq_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54734be7bf.mp4?token=qvHalzK7mtKBBzJhN7z9fiqKG4IEOcaHMwPqcTPvsxPrgqvNahZzz-icNMay1luO81gNPe3mOBJXzYcw5K2I0az_1SKgfTsP21zO3gXKN-5jr0Umnd0MJ1EXS_yjgbfsz1RKQ7YIg25ZzFAZp18StfkiPH-aNFsB_QxbiqoIA9MFDuam-MSoO4addGXAjMY6ad_lF4l5LLMQVrA0aseLIuB21vupZQWloiX0MCE4D2OZc_wxVH03xcHhJEmvtEopm_rxyzMpZiN5E5tj5AgxpyKewXab1GSsIyrPBwJYkoLfsil7d6grMtJx94GhtzMpbScEfvKl7SZKjFRRXxJq_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطره بامزه علیرضا بیرانوند از شب پیروزی دراماتیک مقابل پرسپولیس در ضربات پنالتی …
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107855" target="_blank">📅 12:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107854">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUNL0vNnnDy1wdSbsTdDiPJP-TtZEHnO_jXP3ej-h2z36t9dGAvCoBYhzmqPio0IE3bJhY0ljbURtHwOkIVSlyswVNyQLTNTBRC4NBDferxVwaN9KHVc-I2EK2_0XyiNI6P5w5GtrbsllE0g2Ele23ok2vuofdOKRgir6fvibmWUpfAmcn5RuVbxMHoZBU40HzgAbV0UkNrqLr45o8RwEMDLhlO2NGmEMdpoldFcFkOlAzsqJ8P6o3G6iGlBLdR59JejbZx1GgAo0KPUB-dQWfI6pSydrLtf9y2qif81k75r-A1FLePj3Ued4etdbCmu4YiucjoLxGIk23v2uRtz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
استوری مدیررسانه‌ای استقلال در واکنش به مصاحبه شب‌گذشته مدیرعامل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107854" target="_blank">📅 12:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107853">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOpqKkIqeFFxhRLJgWIe7aG_3MhSZ2Yp83UMnphE34VJKF7WFzN0JL9YWa8wYpxXTjR2cHNcfQdEK7CXAHnWX0m1cOr25p_vRvX1gKEvBhNFAMvBkYzTwJueFfmvmNPiWKLHfha2W6bsN-t5FzhEQ5SDrXvsVOh2N3lbE1M1eQbvTrwjs-bqA4B7OQubPW-l66Vlj6seqGTIG_3NVfJ4Xc4hgiIfQ_Tmy1S_M34tHrS44hhx1wd8lTRyrkJlJbU5wq9dxFfpy9IOHB3bCbxomm5H6H-7otkSNcWPjzvxOlylqfgqMiu2SXLfXxW6cLvnoeWEWGZDFXDDSUS7vUS1Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
هیئت‌رئیسه فدراسیون فوتبال اعلام کرد که جام‌قهرمانی فصل‌گذشته به استقلال داده نخواهد شد و پرونده این موضوع رسما مختومه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107853" target="_blank">📅 12:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107852">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f754e7f64f.mp4?token=F5V-8pjV95mBZ-h-lpy1S7W8DZ9lb9tNPUlYtD39IXI-zO3kRyKXskzvnSXGGUc9n6RRn6afca5xKtIw7g5GlE-xAPVS8NHhf4Q9VtMkYf2WTw71jk17UJftxNAr_pHTckmlYTh5ljnKMOZYePGrfUqWjU8CsjDRsVmOCLzLi82tNmTmZmRA9RobK4YYWdF8lXPgeqmIGvCrpwCxDFuvED-VsqdWVuwYfNNIbdu4PHt99_uURGAGz0vp_Zb2Alx08NGqpJjz-aC_BReRGnxX0Mjf2BrirJ3PVBDu35xKsUSMEeSyvOX4-3x_7Lgz_ydwNp8cVKe3QJCdFyS40xQHvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f754e7f64f.mp4?token=F5V-8pjV95mBZ-h-lpy1S7W8DZ9lb9tNPUlYtD39IXI-zO3kRyKXskzvnSXGGUc9n6RRn6afca5xKtIw7g5GlE-xAPVS8NHhf4Q9VtMkYf2WTw71jk17UJftxNAr_pHTckmlYTh5ljnKMOZYePGrfUqWjU8CsjDRsVmOCLzLi82tNmTmZmRA9RobK4YYWdF8lXPgeqmIGvCrpwCxDFuvED-VsqdWVuwYfNNIbdu4PHt99_uURGAGz0vp_Zb2Alx08NGqpJjz-aC_BReRGnxX0Mjf2BrirJ3PVBDu35xKsUSMEeSyvOX4-3x_7Lgz_ydwNp8cVKe3QJCdFyS40xQHvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
چالش فوتبالی با چهار اسطوره محبوب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107852" target="_blank">📅 12:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107851">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7BxTl3ARSs4V9-BTeXXnJhCWZcrPbc5TZ8rpdw1en9lh0pBg4sjV_3SBBboG6FVmHAa3LBex5Lz52Cpo6Usq_prJziI4SJPHYpib_FDRKD4J7-cb0GngIFnkZ0SRlbpHIHVcSipsAQ_PgDJpWhnHJ3AbRKnUR2s_zMnZS4P1k5LI6nlpUfTt9ZkzgNh_tMD6QcLHoxdKR1NC9GDG073sq9M3vHEnpanU2qSsUqrF_PmqhDB5amS8VVswB22qzzY2QjePSIpGTCg_tVW62l2FTg71QjBhnbQ5TMABdWnjoPfVur1lbw15TUbQ2D5EVYT5spJvrcOZpW6X-qMhGzs1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد مهاجمان بارسلونا در این‌فصل چه در بازی‌های باشگاهی و چه بازی‌های‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107851" target="_blank">📅 11:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107850">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fd2204c7.mp4?token=nw2g8RrMwan4XITf0LVnBx4_kB98_gWJSGRmhB0_Yor66MhT57xODwMuY3NFh0AJdrnRyAymvEMBpDG93jaLsqZhWX_Z9rOcdLZF_H9L4yvoZIubBGHhshE9dYnJAdkfDSaFNZT2trIvko1PtE7j5QWM_TkHmHjQYdtTpcW9bD7Udio8JMzDrVUO7hOoJZ1XV65Aqgh1I-51WLbvF1J_DIKPmxRuQAy00J2rcAb42oXjr9hW7Ty6YeXUITZvmycs0Ahrk2THjnX2Dc_u_gCMl8PpcOOxRv4vKOQE4UawooaLNhcEHQI1C9cbVwoaFqmxImUn-ood-Apuh2klG1d3HjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fd2204c7.mp4?token=nw2g8RrMwan4XITf0LVnBx4_kB98_gWJSGRmhB0_Yor66MhT57xODwMuY3NFh0AJdrnRyAymvEMBpDG93jaLsqZhWX_Z9rOcdLZF_H9L4yvoZIubBGHhshE9dYnJAdkfDSaFNZT2trIvko1PtE7j5QWM_TkHmHjQYdtTpcW9bD7Udio8JMzDrVUO7hOoJZ1XV65Aqgh1I-51WLbvF1J_DIKPmxRuQAy00J2rcAb42oXjr9hW7Ty6YeXUITZvmycs0Ahrk2THjnX2Dc_u_gCMl8PpcOOxRv4vKOQE4UawooaLNhcEHQI1C9cbVwoaFqmxImUn-ood-Apuh2klG1d3HjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خاطره عجیب حنیف عمران‌زاده از وسواس‌های فتح‌الله‌زاده: حاجی توی عربستان چمدونش رو زیر شیرآب شست می‌گفت با دستمال کاغذی کنترل تلویزیون را بردار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107850" target="_blank">📅 11:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107849">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8daf57827.mp4?token=hsB-OD6pJlFzicjm7mWeKJ8M7uYzZes6WeQT3pbRyf4WUcDJfSijIDBrSeCQS9rQV4-fpBui66L97vfg2hEqJ6BHxnBHrcIYI7OrvJMHTA4RROnMs80DTk8g_-5pqQYdxpj43JYpSwDCdP-Kl5V5vzK3JUwVOlUs0Y3Ze7y4AVFqCExLFobrdpiGR1zPNDeoa0or4n_nR_y7PzkPmedBX787srLQfjKxPQNggokNYfhK0omsbAck7KPJy5u07qVmf2r5t9rs90EHENYAGiFfLlqLNCyhum2w9d7rU7p5eEejVIuqsx4xM9ihHFMFuXbnoSkCig6nuubN4sRD86H86w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8daf57827.mp4?token=hsB-OD6pJlFzicjm7mWeKJ8M7uYzZes6WeQT3pbRyf4WUcDJfSijIDBrSeCQS9rQV4-fpBui66L97vfg2hEqJ6BHxnBHrcIYI7OrvJMHTA4RROnMs80DTk8g_-5pqQYdxpj43JYpSwDCdP-Kl5V5vzK3JUwVOlUs0Y3Ze7y4AVFqCExLFobrdpiGR1zPNDeoa0or4n_nR_y7PzkPmedBX787srLQfjKxPQNggokNYfhK0omsbAck7KPJy5u07qVmf2r5t9rs90EHENYAGiFfLlqLNCyhum2w9d7rU7p5eEejVIuqsx4xM9ihHFMFuXbnoSkCig6nuubN4sRD86H86w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
‼️
سردار آزمون به دو بانوی تکواندوکار ایران یعنی ساغر مرادی و فاطمه احمدی که در مسابقات آسیایی مدال کسب کرده بودند،‌ نفری یک میلیارد تومان پاداش هدیه داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107849" target="_blank">📅 11:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107848">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👀
‼️
🇮🇷
صحبت‌های شروین‌بزرگ درباره پیشنهادی که در فصول اخیر از پرسپولیس دریافت کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107848" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107845">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294e1e1160.mp4?token=RXR7aaQ4byQEqCBfayUOUSCBx4WN1OQ5naXohqIpQR8miHRn1zqbJDAfFGtYqZX_5B5Axxi6s2qqxDPatPRYgAwbdIbj5qWUcDn2I8HBSlvEBjobuV7eVAxIBO85CSNRLD50uxrnJ8uYtrQCHBg6j9hq9fIQi48V1dr6wHLOwmepJ6Ht35hyrDDB_eRhL3R1DIFzYhrkGN8MDk6ScNRInqu3eiehxtOWTqxbswQYO7XuniwSgSlCTS4PsqA6b_hZvOrLPCJec10WlQ8S6ufKnn2j0wO9U6064iHfT5idJPd7lKsFcH_K2rqsr21T_E22oCqu6-skTtvTeJdVyVpc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294e1e1160.mp4?token=RXR7aaQ4byQEqCBfayUOUSCBx4WN1OQ5naXohqIpQR8miHRn1zqbJDAfFGtYqZX_5B5Axxi6s2qqxDPatPRYgAwbdIbj5qWUcDn2I8HBSlvEBjobuV7eVAxIBO85CSNRLD50uxrnJ8uYtrQCHBg6j9hq9fIQi48V1dr6wHLOwmepJ6Ht35hyrDDB_eRhL3R1DIFzYhrkGN8MDk6ScNRInqu3eiehxtOWTqxbswQYO7XuniwSgSlCTS4PsqA6b_hZvOrLPCJec10WlQ8S6ufKnn2j0wO9U6064iHfT5idJPd7lKsFcH_K2rqsr21T_E22oCqu6-skTtvTeJdVyVpc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
حاج‌صفی کاپیتان تیم قلعه‌نویی: امیدوارم در‌ جام ملت‌ها باشم اما قلعه‌نویی‌ دنبال تغییر نسله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107845" target="_blank">📅 11:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107844">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
🎙
🇮🇷
🇮🇷
بی دلیل از استقلال تعریف نکردم؛حمید مطهری سرمربی فولاد خوزستان: کاش سهراب بختیاری‌زاده خارجی بود!
🔺
حمید مطهری می گوید اگر نتایج سهراب بختیاری زاده را یک مربی خارجی می گرفت، همه کار برایش می کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107844" target="_blank">📅 10:40 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
