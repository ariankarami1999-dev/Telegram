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
<img src="https://cdn4.telesco.pe/file/ewP945oEBOYeKUAhNfcsOMd8nYrUfVyNu3u5EhS9kJ636mmYKnbQHLFLz-on_798KPPVTM7V_s-G9zkBbqUP-o4k8GkgsusH4EnVVOow8Vm7dmEUXPJzdL55n9pKVw7GzEwRYeJhg_Dj1tPmKp0Avu9sT5Zwd3VDbPMbw9ky6f3KIu7XvR7BnAcIwRvMP6fi6W-edi8LmwYyj3udBPRBRB3op2YJP5-BJ8K_PIPQA8uxxWuz1kI_PaOdilx7TaM56oT0w9dsblRnjaRispo8zSVULcebacXx5zye5-VpyEaoSierZeNYiM3LTQqasMqAuiSUskzrF0wuiRW0J8e_qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 13:07:41</div>
<hr>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96bba2676.mp4?token=JRWWltp14gjeajGApxnxxkKNO_EmLOQNPmwm3KrAAcKc2hYAbmU_7vUC-Vv_C74ea24fve8bAtwPmSyOGqydAsqyh9sCg1gMLiIIo88MgpSr7AesVkzM2uM7sFc0NZ6spH4g3x-pjQIylnPC7YBBWHTCbC64embHq8hzyLJJyl5KXjd6SpCXxvzC30cLr50n2x5rTGacwtipLQXgRX2zMUWL-IJQ_ai2EcMEV2hDR5d6CIBytFkS2DhTrAt_sY5S41F55Ot37VCs2Q56a8EIJYazXTWrufk5rnPJvteQNWcfFvy7VxclI42lG4uEdbvv8GAjseK2cwEM_8MB1roWCCkG5NsWunIRcFTx8LStwYInAGmu6k4cUo6sv0_ym5Hi9jJ7auVhekkBLBOFCSaQi_7GL9Px1hzee9kkvbG4H-HBQnNqiijgTqqU8nAWzXdzZ_FMRMDF6BCVgjh6AZr2g_OO4fsN_3wCmMPkIVnxuvlHbRgiT64tfhHpUgwprCB3QdCN0eht0v5G9TEfFdRDLyT3YMuJgNmCPHh_M_tl0WMpuW8cBusQ8pbY2HCj_dcWXD91LgDQydYMzueYNKn4HGrJjDe0pb7qHHMEJ0aF3d3aWJGEDd_uZYrc7fiAjl_n1Y4RsF9YCzsomQtLOD8kpofvyYzC4MW4AM9bwjM-rf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96bba2676.mp4?token=JRWWltp14gjeajGApxnxxkKNO_EmLOQNPmwm3KrAAcKc2hYAbmU_7vUC-Vv_C74ea24fve8bAtwPmSyOGqydAsqyh9sCg1gMLiIIo88MgpSr7AesVkzM2uM7sFc0NZ6spH4g3x-pjQIylnPC7YBBWHTCbC64embHq8hzyLJJyl5KXjd6SpCXxvzC30cLr50n2x5rTGacwtipLQXgRX2zMUWL-IJQ_ai2EcMEV2hDR5d6CIBytFkS2DhTrAt_sY5S41F55Ot37VCs2Q56a8EIJYazXTWrufk5rnPJvteQNWcfFvy7VxclI42lG4uEdbvv8GAjseK2cwEM_8MB1roWCCkG5NsWunIRcFTx8LStwYInAGmu6k4cUo6sv0_ym5Hi9jJ7auVhekkBLBOFCSaQi_7GL9Px1hzee9kkvbG4H-HBQnNqiijgTqqU8nAWzXdzZ_FMRMDF6BCVgjh6AZr2g_OO4fsN_3wCmMPkIVnxuvlHbRgiT64tfhHpUgwprCB3QdCN0eht0v5G9TEfFdRDLyT3YMuJgNmCPHh_M_tl0WMpuW8cBusQ8pbY2HCj_dcWXD91LgDQydYMzueYNKn4HGrJjDe0pb7qHHMEJ0aF3d3aWJGEDd_uZYrc7fiAjl_n1Y4RsF9YCzsomQtLOD8kpofvyYzC4MW4AM9bwjM-rf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏اظهارات کم‌سابقه سناتور تام کاتن درباره راز وقایع مرداد ۱۳۳۲ در برنامه هفتگی پربیننده مارک لوین در شبکه فاکس‌نیوز
‏«اوباما ادعا کرد که ما نخست‌وزیر منتخب دموکراتیک ایران را در ۱۳۳۲ سرنگون کردیم. این یک افسانه کامل است. او (مصدق) نخست‌وزیر دموکراتیک نبود. او اساسا سرنگون نشد...
..(برعکس)، مصدق کسی بود که سعی کرد قدرت را تصاحب و به طور غیرقانونی حفظ کند. ولی باراک اوباما با مغز استخوانش باور داشت و بارها درباره آن نوشت و سخنرانی کرد که آمریکا برای دهه‌ها تنش با ایران سزاوار سرزنش است و برای همین هم به دنبال توافق بهتری نبود.»
@WarRoom</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/withyashar/20918" target="_blank">📅 12:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرمانده ستاد کل نیروهای دفاعی اسرائیل، ایل زمیر، به وزرای کابینه در مورد وضعیت اقتصادی ایران گفت: تحریم‌ها علیه ایران بسیار موثر بوده است. بحران اقتصادی در آنجا رو به وخامت است.
@WarRoom</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/withyashar/20917" target="_blank">📅 12:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سناتورهای دموکرات کنگره آمریکا خواستار بررسی شرایط ناو یواس‌اس آبراهام لینکلن شدند؛ این درخواست پس از گزارش‌هایی درباره کمبود غذا، خرابی لوله‌کشی و بحران‌های سلامت روان در طولانی‌ترین مأموریت تاریخ ناو مطرح شد.
سناتور روبن گایگو نیز خواستار بازدید رسمی و نظارتی یک هیئت دوحزبی سنا از ناو برای بررسی شرایط گزارش‌شده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/20916" target="_blank">📅 11:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/20915" target="_blank">📅 11:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvZZCWQgkqaVytujAk2BxfHjVeUTQnaXK1F1lFKULCaMBnT02A9-V4fnponE4XubItGxAEI-cnw-Lf6i3UXb2WEycLE9U6qnfchLHQtD7T-s-0WeIc8JW2880_NTScOXEFpmlogu5d6gVJ_c27DckNQsgRS7fnI1nYRbwPOPgQ33Mw4ZqrO2xf_4RuMHlA4LBQo21bomHXrQkOoSNzX8PD6NwziyfLUkT_9B8AYH1eNu3WzyDIDA2HR7Sng4o1bHN41kAgHSCuryt96rsHFOO2Bev7PPZvVq-_cVyvaiqIzW6xyoHMQN20MQL5jqkNENWk87hx-0rc-k1ESUo0heIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩
https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/20914" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/20913" target="_blank">📅 09:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/20912" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شب گذشته از ترس شروع اعتراضات و انفجار جامعه افزایش قیمت بنزین هشتاد و هفت هزار تومانی در کرمان، کمتر از یک ساعت پس از آغاز اجرا متوقف شد و قیمت بنزین به نرخ قبلی برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/20911" target="_blank">📅 08:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کانال‌های عبری : خبر گران شدن بنزین در ایران باعث شد خبر انتقال پنهانی طلا و دلار به ایران، در حاشیه قرار بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20909" target="_blank">📅 04:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیت هگست، وزیر جنگ : رئیس جمهور ترامپ، سوءاستفاده را برنمی‌تابد. ما اینجا برای بازی کردن نیامده‌ایم.
شهروندان و ملت‌های ما شایسته و منتظر اقدامات واقعی و ملموس هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20908" target="_blank">📅 23:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی امروز کشتی باری «ولا نوا» با پرچم پاناما را هنگام حرکت به سمت یکی از بنادر ایران در خلیج عمان متوقف کردند. پس از بی‌توجهی خدمه به هشدارهای آمریکا، یک بالگرد MH-60 دو موشک هل فایر به اتاق موتور کشتی شلیک کرد و سامانه هدایت…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20907" target="_blank">📅 23:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ در تروث : کارولین لیویت، سخنگوی فوق‌العاده کاخ سفید و یکی از مورداعتمادترین دستیاران من، در پایان این ماه از سمت خود کناره‌گیری خواهد کرد تا بتواند زمان بیشتری را با فرزندان خردسال دوست‌داشتنی و خانواده‌اش بگذراند
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20906" target="_blank">📅 23:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">@WarRoom
ترامپ پوکر باز</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20905" target="_blank">📅 22:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20904" target="_blank">📅 22:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=PIB1B-lxF11sjV3qDIExv4XToXE48yHaUBqbVjGHZvAHmv63cjdzEGDwUn-7RMQ1vn8Gg8faaVAE96nUXgpErGDLdHM0MrfzvX7veoWNYM5WFxpkFfTKOp3PLY0awdXg4x-67nFUJxMW5NnE3RhDFvqmkjGVZX6_yDjzedMPuyXYfEvSS9Hb29Z8jWiceiz8jz4HLUfyo5FkyfhXkGj57pEi2ELXfFaT72kXM4dbARjInJIqye2gAfwhs_kaOoAoYlw6thaLTKW9M_ijCcF_9nkg2m3hK0XnOilwolq_FSEGRnLpXtonOVbwkR5wQDkChW9qfy-5iJmiGq5jKBdhtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=PIB1B-lxF11sjV3qDIExv4XToXE48yHaUBqbVjGHZvAHmv63cjdzEGDwUn-7RMQ1vn8Gg8faaVAE96nUXgpErGDLdHM0MrfzvX7veoWNYM5WFxpkFfTKOp3PLY0awdXg4x-67nFUJxMW5NnE3RhDFvqmkjGVZX6_yDjzedMPuyXYfEvSS9Hb29Z8jWiceiz8jz4HLUfyo5FkyfhXkGj57pEi2ELXfFaT72kXM4dbARjInJIqye2gAfwhs_kaOoAoYlw6thaLTKW9M_ijCcF_9nkg2m3hK0XnOilwolq_FSEGRnLpXtonOVbwkR5wQDkChW9qfy-5iJmiGq5jKBdhtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20903" target="_blank">📅 22:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صدای موشک اقتصادی
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20902" target="_blank">📅 21:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">طرح امتحانی بنزین ۴ نرخی آغاز شد!
نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان
نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان
نرخ سوم: ۴۰ لیتر با نرخ ۵۰۰۰ تومان
نرخ چهارم: ۸۷,۲۰۰ تومان
این طرح هنوز به طور رسمی کامل اجرا نشده و اکنون محدود به ۲۰۴ جایگاه سوخت در استان کرمان میباشد.
﻿
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20901" target="_blank">📅 21:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کانال ۱۱ اسرائیل : با کمک ماهواره‌های روسی ، حملات حوثی‌ها به عربستان سعودی و نیروهای آن در یمن هم افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20900" target="_blank">📅 21:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گاردین به نقل از چند منبع : ناو هواپیمابر «آبراهام لینکلن» پس از حدود ۹ ماه مأموریت مداوم و ۲۵۰ روز حضور پیوسته در دریا، با افت شدید روحیه و فشار روانی خدمه مواجه شده است. خانواده‌ها و برخی ملوانان از مشکلاتی مانند محدودیت غذا و آب، اختلال طولانی در شست‌وشوی لباس‌ها و دست‌کم یک مورد تلاش برای پریدن از کشتی که مهار شده، خبر داده‌اند. نیروی دریایی آمریکا نیز در حال آماده‌سازی ناو «تئودور روزولت» برای جایگزینی لینکلن است، هرچند زمان دقیق این جابه‌جایی به دلایل عملیاتی اعلام نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20899" target="_blank">📅 21:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏وزیر دفاع اسرائیل: من به ارتش اسرائیل دستور داده‌ام که تمام اقدامات لازم را برای حضور طولانی مدت در منطقه امنیتی لبنان، سوریه و غزه انجام دهد. ‏ارتش در منطقه امنیتی لبنان، سوریه و غزه برای دفاع از تمام اسرائیل باقی خواهد ماند. @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20898" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مشاور ارشد قالیباف :آ مریکا و اسرائیل برای یک حمله نظامی پیش از انتخابات سراسری در اسرائیل و انتخابات کنگره آمریکا در آبان ماه،آماده می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20897" target="_blank">📅 19:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر کشور پاکستان در ایران به عراقچی، وزیر امور خارجه، اطمینان داد که "توافق دفاعی مکه" به عنوان یک ائتلاف علیه رژیم ایران طراحی نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20896" target="_blank">📅 19:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42557aaa83.mp4?token=mXaH_SHNDWS6A15pJtrC600xf2lqjDsiUBafHevyDQHGgHVXQRj9CDj_ICY4wRR_oy7V0Belp-p4uGwl1SVp8VdhAeZQ26uK0rn3avZawD2H4ndp-GSNvaDBoJFMXjRDlFsJGordEzrEj7lXygW6jbmZ4zaZA0_cAGf8ruJyjQEAlba-pIOLAeq1brNZSQShOyE2aybevRGfqodLzjLTsyO0fHRI8Jr4_XgPbYYlBoxBNzE5VnyTcdHIBGs4vOebIqrKdl-GDfBCYva8bqzrDmsa7UVSrKhx3J3jq_044pAxAyFDQTJacaUybFhSCQdeG3xf_CxcJ7F_nr1M79Jjui6Q6mHubdZWiHCZCgJyEuhINK6qq3Q_1GHFMG1MMHOn9YArDaNEMA1aBz3SqwJX2jGfzZ3tPkYH_e-pV68-xm2YqqE7StaWYtfenR_0JdJKY4AG8UbK99__nEP4-aRhq6mWqkQtzX521v8FxeTxNN-lY9t4HM4ngdaLLyiJNLOfHlrW8v7vrMQ9Bzh51DCA2rwZgJ8mLG0mdiOk7n2mXIkk4TGlO3XZYT9ms-2qCTLpGQvyyrGhzJrVhcCFYcI4XaEDOZ7sT-XdbHFA4r4lvKpOvXYqg_PtJNZ2kFl7azPGRJ0UcwnW0lp7roQdGEHdjaF9GMBacMqlB78GTUC6dfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42557aaa83.mp4?token=mXaH_SHNDWS6A15pJtrC600xf2lqjDsiUBafHevyDQHGgHVXQRj9CDj_ICY4wRR_oy7V0Belp-p4uGwl1SVp8VdhAeZQ26uK0rn3avZawD2H4ndp-GSNvaDBoJFMXjRDlFsJGordEzrEj7lXygW6jbmZ4zaZA0_cAGf8ruJyjQEAlba-pIOLAeq1brNZSQShOyE2aybevRGfqodLzjLTsyO0fHRI8Jr4_XgPbYYlBoxBNzE5VnyTcdHIBGs4vOebIqrKdl-GDfBCYva8bqzrDmsa7UVSrKhx3J3jq_044pAxAyFDQTJacaUybFhSCQdeG3xf_CxcJ7F_nr1M79Jjui6Q6mHubdZWiHCZCgJyEuhINK6qq3Q_1GHFMG1MMHOn9YArDaNEMA1aBz3SqwJX2jGfzZ3tPkYH_e-pV68-xm2YqqE7StaWYtfenR_0JdJKY4AG8UbK99__nEP4-aRhq6mWqkQtzX521v8FxeTxNN-lY9t4HM4ngdaLLyiJNLOfHlrW8v7vrMQ9Bzh51DCA2rwZgJ8mLG0mdiOk7n2mXIkk4TGlO3XZYT9ms-2qCTLpGQvyyrGhzJrVhcCFYcI4XaEDOZ7sT-XdbHFA4r4lvKpOvXYqg_PtJNZ2kFl7azPGRJ0UcwnW0lp7roQdGEHdjaF9GMBacMqlB78GTUC6dfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏وزیر دفاع اسرائیل: من به ارتش اسرائیل دستور داده‌ام که تمام اقدامات لازم را برای حضور طولانی مدت در منطقه امنیتی لبنان، سوریه و غزه انجام دهد.
‏ارتش در منطقه امنیتی لبنان، سوریه و غزه برای دفاع از تمام اسرائیل باقی خواهد ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20895" target="_blank">📅 18:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">امروز،
۱۲ اوت ۲۰۲۶
، آسمان شاهد هم‌زمانی
چهار پدیده نجومی
است:
صف‌آرایی شش سیاره
شامل مشتری، عطارد، مریخ، زحل، اورانوس و نپتون که پیش از طلوع خورشید در امتداد بخشی از آسمان دیده می‌شوند؛
خورشیدگرفتگی کامل
که اوج آن حدود
۲۱:۱۷ به وقت تهران
خواهد بود و در ایران دیده نمی‌شود؛
اوج بارش شهابی برساوشی
که از امشب تا بامداد ۱۳ اوت ادامه دارد و در شرایط مناسب می‌تواند ده‌ها شهاب در ساعت ایجاد کند؛ و در نهایت
ماه نو
که یعنی ماه تقریباً بین زمین و خورشید قرار می‌گیرد و از زمین دیده نمی‌شود. نبود نور ماه باعث می‌شود آسمان تاریک‌تر شده و شرایط برای تماشای برساوشی‌ها بسیار مناسب باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20894" target="_blank">📅 18:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_N7Kv2T7h9wPEPGRs0eiudqz_VoKJZTzSVGANiZZGHSYskS5NHZOKRV7eZq4kRjm1x28SVg3wbDwzz9NjzBkb5DJc8zdwTmgCYGgUkX9rT-53vq29PUbuTJz53ur6sSwnC5DNq6GGkLpfCUaYeR-Z9VF51QCz1gvJfoLwAXHFqQa7QWk9F3Cg28GN1tkyh1OWIaeoQzDBjX6gHnYRyC0UN7qZnIrhctPwzJ2NItRij8G97EzbzTPsPvhuH-aQKdDdguSbIGWGGU8Y703uSo68ZDlLGV4DyIEV61n-3ZRnjgoyi7P_3G3VG40DhY50iITBA-gccYh-994ec7VeVZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد! محاصره دریایی ما از سوی همه «دیوار فولادی» نامیده می‌شود و ایران هیچ کاری از دستش برای مقابله با آن برنمی‌آید. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق دریافت نمی‌کنند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است و «رهبری» آنها، در بهترین حالت، نامطمئن است! آنها پولی ندارند؛ کشورشان «ویران» شده است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر می‌شود! ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. ستایش از آنِ الله باد!
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20891" target="_blank">📅 18:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7908fd3c.mp4?token=V_Y922Dsr4PJDmmGuej_ujBEnitnbHEGAmE4B-yUomOMPBaPpFmiW3RE1EUZk9nb_luvsqGn__oaHK3ZcnQdiMNJkw3GKeSgmoDi4aUyQwrPGxPfNW1PQFoJPPMNa74vNDi3EL8E_bMX746YneSxWT5GrlH0CIMsa508pEEF-Wun4EaQoEDqd7wfWYTeNQPhVvdsooxlBGTCAkUxWaEXoCJfbTzXVBF1nkU0rE2Pt7PHRlYbSEVK91YP1WZ9_WGnfuW1xK-ENz6-dnu2dPGHLfzRfhxGx0mnYPUf5gnsYtxvmp5Z5BH4eqDq8t-Iv6JzzX-6VX4u-MQihT8MAZb93w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7908fd3c.mp4?token=V_Y922Dsr4PJDmmGuej_ujBEnitnbHEGAmE4B-yUomOMPBaPpFmiW3RE1EUZk9nb_luvsqGn__oaHK3ZcnQdiMNJkw3GKeSgmoDi4aUyQwrPGxPfNW1PQFoJPPMNa74vNDi3EL8E_bMX746YneSxWT5GrlH0CIMsa508pEEF-Wun4EaQoEDqd7wfWYTeNQPhVvdsooxlBGTCAkUxWaEXoCJfbTzXVBF1nkU0rE2Pt7PHRlYbSEVK91YP1WZ9_WGnfuW1xK-ENz6-dnu2dPGHLfzRfhxGx0mnYPUf5gnsYtxvmp5Z5BH4eqDq8t-Iv6JzzX-6VX4u-MQihT8MAZb93w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منم مشکلات زیادی دارم ولی برای شما شاد هستم
😍
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20890" target="_blank">📅 18:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/20889" target="_blank">📅 18:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش CNN: وزارت امور خارجه آمریکا به دلیل تنش های احتمالی به سفارت‌های این کشور در خاورمیانه دستور داده است تا برنامه‌هایی را آماده کنند که به آن‌ها اجازه دهد با تعداد محدودی از کارکنان به فعالیت خود ادامه دهند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20888" target="_blank">📅 17:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6ab93f52.mp4?token=fE6wGH81y2CoFh9AQpMqdKTIMtzqkuzSiIgjEbX8bQc4nNf0SYeMBpBFNVKPbLO1k9_9ETAMm1mizMfcRukbmTjKQoLy_G--tKAMTYonRk5AD9UkYuJixCez4-RW0F_6lSSuSh4TKcXzSclrf-HrXrp2KuJ5X8CaDl8KHofCirWTrP9n-B7INNit3eejTX06gsiCXtSGXN0-B1XgtzlFhworgmdJR2VSNYn3poBj9bAUtXHwgM7mEjhN_9QKguI1JeifLYtZL7tSVMB8iCCHG0lZ_nemhbPYbHl7gdeXBKG41-XFxDcg_n7U5cG14ldsc9rEP5OwQYCeu9yEYus3jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6ab93f52.mp4?token=fE6wGH81y2CoFh9AQpMqdKTIMtzqkuzSiIgjEbX8bQc4nNf0SYeMBpBFNVKPbLO1k9_9ETAMm1mizMfcRukbmTjKQoLy_G--tKAMTYonRk5AD9UkYuJixCez4-RW0F_6lSSuSh4TKcXzSclrf-HrXrp2KuJ5X8CaDl8KHofCirWTrP9n-B7INNit3eejTX06gsiCXtSGXN0-B1XgtzlFhworgmdJR2VSNYn3poBj9bAUtXHwgM7mEjhN_9QKguI1JeifLYtZL7tSVMB8iCCHG0lZ_nemhbPYbHl7gdeXBKG41-XFxDcg_n7U5cG14ldsc9rEP5OwQYCeu9yEYus3jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری پی بی اس: چرا مجتبی خامنه‌ای در طول این جنگ هرگز در ملاء عام دیده نشده است؟
محمدرضا نقدی: استراتژی متعل به اوست. دشمن ما جنایتکار است و به هیچ قانونی پایبند نیست.
مجری: آیا این به دلایل امنیتی است؟
نقدی: طبیعتاً به دلیل امنیت است. مطمئناً دلیل دیگری وجود ندارد.
مجری: آیا او را دیده‌اید؟
مجری: بیایید این موضوع را کنار بگذاریم.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20887" target="_blank">📅 17:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7137b6f963.mp4?token=Aen7UrR1Gtnv_O2v2VDZ3g0VuW3nkMd4oepyJDDgeeh-sMwbN0_xwQlFMnSYcZuyA7wVLG_ovOEL4oLFpnziQkr0f0px7YaSsX3RLsQsqpsB4aQ88SUSGo2Eo3oIK_vVTGOUz9wZvU2ew39x3eo-FT0IerTFlKyW5BMPQ9oVKvkWtymuH-7t58LaiJqlrGPqaYGSAZ1jJFCd6zPkPBidSQOsXzIR3CUYwQFkbtQz39OtAVleWyXBPCbFFlkWxLyNrcpIbkq2S8ZuaYGFaWX7MxsGOwDtQ6YfKQDprECLuu9_IofxwbL0DnGYDjF76O0VKMmVuPrxwNxczhnCYKnM_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7137b6f963.mp4?token=Aen7UrR1Gtnv_O2v2VDZ3g0VuW3nkMd4oepyJDDgeeh-sMwbN0_xwQlFMnSYcZuyA7wVLG_ovOEL4oLFpnziQkr0f0px7YaSsX3RLsQsqpsB4aQ88SUSGo2Eo3oIK_vVTGOUz9wZvU2ew39x3eo-FT0IerTFlKyW5BMPQ9oVKvkWtymuH-7t58LaiJqlrGPqaYGSAZ1jJFCd6zPkPBidSQOsXzIR3CUYwQFkbtQz39OtAVleWyXBPCbFFlkWxLyNrcpIbkq2S8ZuaYGFaWX7MxsGOwDtQ6YfKQDprECLuu9_IofxwbL0DnGYDjF76O0VKMmVuPrxwNxczhnCYKnM_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری آمریکایی پی‌بی‌اس : آیا هدف ایران این است که این جنگ را طولانی‌تر کند، شاید تا زمانی که آقای ترامپ از قدرت کنار برود؟
نقدی، فرمانده سپاه: ببینید، ما باید به بازدارندگی برسیم تا دشمن هرگز جرات حمله به ما را نداشته باشد تا بتوانیم با امنیت زندگی کنیم.
یک راه این است که این جنگ را تا رسیدن به دوره بعدی ریاست جمهوری ادامه دهیم و فرسایش ایجاد کنیم تا اگر کسی بخواهد به ایران حمله کند، بداند که هزینه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20886" target="_blank">📅 16:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKrdbYYeCKkyVKbpeUAv_-0KGLipff9s84bX1w7tA46_bE5Asbldxn3Gp2N8AYNJ825Fo_b7mrag2sXvMNWJGCHVhPUMQCxC_ReANZVzoX597uWu93ndagYKI_NgoDxIfMrGuF4IrC1P8ikyFKvQMS58fnefEhguXOeNcSfBZDynu2jvfkygrre1wjGcRVUzvH43goKFbrv8S-QsicmVivvvKJj27K9KGeESes2Hb0i6oOThS2l4DVivVD8_-5yRULzkg_Bk7U-KRK6AwRkmKx4rWj3IOvsxuSK1N3et0J7sTntX_36dwKSCtUuOs8EPwdIxK7p0Kggx3e7QOchgSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهلوان آواز ، «ایرج» خواجه امیری،  خواننده قدیمی در ۹۴سالگی درگذشت
بخش بزرگی از ماندگاری صدای ایرج در سینمای پیش از انقلاب، به ترانه‌هایی برمی‌گردد که صدای او روی تصویر
محمدعلی فردین
است. ایرج خودش گفته بود در
۲۶ فیلم
به جای فردین آواز خوانده است. در مجموع هم گفته بود برای
۱۳۵ فیلم
خوانندگی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20885" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجار های جاسک رو اعلام کردن کنترل شدست ، هم اکنون باز‌ داره گزارش‌ میشه
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20884" target="_blank">📅 16:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">«الحدث» به نقل از منابع آگاه گزارش داد که اسماعیل قاآنی، فرمانده نیروی قدس سپاه، در سفر غیرعلنی اخیر خود به بغداد با رهبران حشدالشعبی، گروه‌های مسلح و چهره‌هایی از ائتلاف‌های سیاسی عراق دیدار کرده و
پرونده حصر سلاح در دست دولت
را بررسی کرده است. طبق گزارش‌های تکمیلی، قاآنی از گروه‌ها خواسته از هرگونه درگیری با نیروهای دولتی جلوگیری کنند، اما هم‌زمان با
تحویل کامل سلاح به دولت عراق موافقت نکرده
و بر حفظ توان نظامی این گروه‌ها در برابر آنچه «تهدیدهای آمریکا» خوانده شده تأکید کرده است. دولت عراق برای تعیین تکلیف سلاح گروه‌های مسلح خارج از نهادهای دولتی،
۳۰ سپتامبر ۲۰۲۶
را مهلت نهایی تعیین کرده و پس از آن قرار است با فعالیت مسلحانه خارج از چارچوب دولت برخورد شود.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20883" target="_blank">📅 15:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پزشکیان: جنگ کنونی از قبلی بسیار پیچیده تر است و دشمن قصد فروپاشی نظام از داخل کشور را دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20882" target="_blank">📅 15:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرگزاری آناتولی به نقل از منابع دولتی پاکستان گزارش داد تفاهم‌نامه قرار است در ۱۷ اوت منقضی شود. به گفته یک منبع نزدیک به روند میانجیگری، دو طرف موافقت خود را با اصل تمدید مهلت به میانجی‌ها اعلام کرده‌اند، اما هنوز درباره مدت دقیق تمدید تصمیم نهایی گرفته…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20881" target="_blank">📅 15:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرگزاری آناتولی به نقل از منابع دولتی پاکستان گزارش داد تفاهم‌نامه قرار است در
۱۷ اوت
منقضی شود. به گفته یک منبع نزدیک به روند میانجیگری، دو طرف موافقت خود را با اصل تمدید مهلت به میانجی‌ها اعلام کرده‌اند، اما
هنوز درباره مدت دقیق تمدید تصمیم نهایی گرفته نشده و تهران و واشنگتن در حال تبادل پیام برای تعیین بازه تمدید هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20880" target="_blank">📅 15:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک منبع ارشد ایرانی به رویترز گفت:
هیچ بحثی برای تمدید آتش‌بس بین آمریکا و ایران وجود ندارد و در عوض، مذاکرات بر بازگشت احتمالی آمریکا به توافق‌نامه تفاهم (MOU) و یک جدول زمانی برای اجرای تعهدات متمرکز است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20879" target="_blank">📅 14:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش صدای انفجار‌ در‌ جاسک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20878" target="_blank">📅 14:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند. ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20877" target="_blank">📅 13:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بلومبرگ : ایران در دور بعدی جنگ، به سمت یک وضعیت نظامی "تهاجمی" پیش می‌رود. این کشور در حال بازسازی ارتش خود است تا آن را انعطاف‌پذیرتر و تهاجمی‌تر در برابر تهدیدات خارجی کند. این اقدام، در سایه جنگ با ایالات متحده و اسرائیل، نشان‌دهنده آمادگی ایران برای یک رویارویی طولانی‌مدت است، حتی اگر درگیری فعلی به پایان برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20876" target="_blank">📅 13:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نیویورک تایمز: در نزدیکی اجلاس ناتو در ترکیه شخصی با موشک دوش پرتاب شناسایی شد!
نیویورک تایمز گزارش می‌دهد که تهدید ایران که ماه گذشته باعث تبادل مخفیانه هواپیمای رئیس جمهور ترامپ شد، در حالی آشکار شد که او در آخرین روز حضورش در اجلاس ناتو در آنکارا، ترکیه، در 8 ژوئیه حضور داشت.
سازمان اطلاعات ایالات متحده چندی  جریان اطلاعاتی دریافت کرد که نشان دهنده یک تهدید موشکی زمین به هوا علیه هواپیمای رئیس جمهور بود، صرف نظر از اینکه کدام هواپیما حامل رئیس جمهور بود.
همچنین شخصی در نزدیکی اجلاس ناتو با یک موشک دوش پرتاب مشاهده شد، در حالی که عوامل ایرانی دقیقاً می‌دانستند ترامپ در آنکارا کجا اقامت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20875" target="_blank">📅 13:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سازمان بین‌المللی دریانوردی:
نشت نفت از نفتکشی که در شمال شرق جزیره قبلیه عمان به گل نشسته است.
انتظار می‌رود نشت نفت از نفتکش کارولین بیزینجی به عمان برسد.
بادها دسترسی به نفتکش به گل نشسته در نزدیکی عمان را محدود کرده و عملیات نجات را به تأخیر می‌اندازند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20874" target="_blank">📅 12:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بلومبرگ
:
سامانه دفاع موشکی «گنبد طلایی» آمریکا نخستین آزمایش‌های اولیه خود را با موفقیت پشت سر گذاشته است.
به گزارش بلومبرگ به نقل از یک مقام ارشد نظامی آمریکا، این مرحله از آزمایش‌ها شامل انتقال داده از حسگرها به رهگیر و همچنین ارزیابی سامانه پیشران فضاپیمای رهگیر بوده است. به گفته این مقام، آزمایش عملیاتی گسترده این سامانه برای اواخر سال ۲۰۲۸ برنامه‌ریزی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20873" target="_blank">📅 11:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تحریم‌های آمریکا، صادرات نفت ایران را محدود کرده و باعث شده بخشی از
مشتقات نفتی، از جمله قیر،
به‌جای صادرات در پروژه‌های آسفالت‌سازی مصرف شود؛ تا جایی که علاوه بر خیابان‌ها، بسیاری از کوچه‌ها و جاده‌های خاکی نیز آسفالت شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20872" target="_blank">📅 11:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مذاکرات ایران و آمریکا درباره تنگه هرمز به نقطه اول برگشت
خبرنگار الجزیره در تهران:
مذاکرات ظاهراً به نقطه آغاز بازگشته و توپ در زمین واشنگتن است؛ تهران ممکن است به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20871" target="_blank">📅 10:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97fd9de97.mp4?token=X_TG_es7ZepRK_6UYBCeSccfVECqWeQ_fP6qh7ucG287AaMmDSBrNJP0lTSGscS_UhBU13FoeYpJ76Tl66DA07NH0ihWVUocJuDqzLvxu0KyrRTqWOl657GFg4_YP7_LU6EyqcVnD5KnvPtlMWCSVmz5rhJLKZscVbvzd0yGKOIbYeAzfXdw7998O7ZTwTBXK5l_cdcwa4ucmsbIrdzsuiltE40cJLCepj6veuauXO69UBg-ABZA9HZrWfvCW2FVSsfDxsa87qSAHyqS-HIc3LXskNoXg2xYl3SJhnt5-1GkeXj1SmIMA_j8M2aQf8ucOe2gr59k64UYvhTGwKOooQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97fd9de97.mp4?token=X_TG_es7ZepRK_6UYBCeSccfVECqWeQ_fP6qh7ucG287AaMmDSBrNJP0lTSGscS_UhBU13FoeYpJ76Tl66DA07NH0ihWVUocJuDqzLvxu0KyrRTqWOl657GFg4_YP7_LU6EyqcVnD5KnvPtlMWCSVmz5rhJLKZscVbvzd0yGKOIbYeAzfXdw7998O7ZTwTBXK5l_cdcwa4ucmsbIrdzsuiltE40cJLCepj6veuauXO69UBg-ABZA9HZrWfvCW2FVSsfDxsa87qSAHyqS-HIc3LXskNoXg2xYl3SJhnt5-1GkeXj1SmIMA_j8M2aQf8ucOe2gr59k64UYvhTGwKOooQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ : «من از طریق سرویس مخفی و ارتش اقدام می‌کنم. آنها می‌خواستند من با پرواز دیگری، با هواپیمای دیگری بروم... من هر کاری که آنها بگویند انجام می‌دهم... حدس می‌زنم تهدیدی وجود داشته است. من واقعاً زیاد در مورد آن سوال نکردم. تهدیدهای زیادی دریافت می‌کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20870" target="_blank">📅 09:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e3f3981e.mp4?token=s1Ke3El_WjD5PlLYW3S4ppFYDAwaR71Cjh-WbFHg_mZ26F_sqRPv4FV2lrwFb0ycThK3nYGsAfLIU-7zrcLGiwWh-qXUb_uv7BFR9E1kGANcdJ4FTPi6HAZKW-OOsL1T0Ojuez0VO96kSwL1f_UdCzLDnPgh0VbDvBmt81rMGVHE7pudqHNXnfSORHvCo2xH7pTz3XcVLXpd0C7WqpKvn_mrMICtiXvEEnAD9G2ZYTizHhPEpL-YS4JWHK2R5xkWC2WEUkMcV8u_5y9gi4A-mwly_9WIta8pyNdFoB5cO0EqBcAPPWsATXw12KiY-XwfcAtp_ytUNjXGOML1S5OxmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e3f3981e.mp4?token=s1Ke3El_WjD5PlLYW3S4ppFYDAwaR71Cjh-WbFHg_mZ26F_sqRPv4FV2lrwFb0ycThK3nYGsAfLIU-7zrcLGiwWh-qXUb_uv7BFR9E1kGANcdJ4FTPi6HAZKW-OOsL1T0Ojuez0VO96kSwL1f_UdCzLDnPgh0VbDvBmt81rMGVHE7pudqHNXnfSORHvCo2xH7pTz3XcVLXpd0C7WqpKvn_mrMICtiXvEEnAD9G2ZYTizHhPEpL-YS4JWHK2R5xkWC2WEUkMcV8u_5y9gi4A-mwly_9WIta8pyNdFoB5cO0EqBcAPPWsATXw12KiY-XwfcAtp_ytUNjXGOML1S5OxmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
من به ایران اعتماد ندارم، چرا؟ مگه فکر می‌کنید به ایران اعتماد دارم؟
من آخرین کسی‌ام که به ایران اعتماد می‌کنه مدام به من دروغ گفتن، الان ما کاملاً کنترل تنگه رو در دست داریم
اونا کنترلش رو ندارند، ما کامل کنترلش می‌کنیم، مال ماست، شاید یه زمانی کاری بکنن و اون‌وقت کارشون تمومه
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20869" target="_blank">📅 08:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ
:
تهدیدهای زیادی علیه من هست که شما ازشون خبر ندارید
هر رئیس‌جمهور تأثیرگذاری تهدیدهای زیادی دریافت می‌کنه، رئیس‌جمهورهای بی‌اهمیت تهدید نمی‌شند
فکر می‌کنم شاید من تأثیرگذارترین رئیس‌جمهور باشم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20868" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ
،
درباره نامزدیش :  دوست دارم دوباره تو سال ۲۰۲۸ نامزد بشم، ولی قانون اجازه نمی‌ده
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20867" target="_blank">📅 08:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20866">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ درباره اینکه چرا خودش با ایر فورس وان پرواز نکرد ولی خبرنگارا پرواز کردن : نمی‌دونم، اتفاقاً فکر می‌کنم هواپیمایی که من سوار شدم بیشتر در معرض خطر بود
خبرنگار : چرا؟ ترامپ : چون فکر می‌کنم همون هواپیمایی بود که احتمال بیشتری داشت هدف قرار بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20866" target="_blank">📅 08:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edfa0f08c.mp4?token=cn8sVoLgdEAMtdedWFPvgycOKLQ5x3oHou8zp4pzyeWVWxKczuZY_-ic21G7_7-cfKwmx6N4IAyvG6LkJKYdG8vzqzIbdI6RK0euH3P4bKstT5vD7bRY2xaeD4kw4Q8dAXtpritrvqHLb7-dQxJHDV5Lx3KbjsQoXNwdCnerfe_CZwepw6EpU8IPitWSz1ibBKaFWuy0Zo6xfS1Ru8qC_bHWRiprr7B01EIAajmTaFOYbw497WUXTxkQNLeU86L2hGgqH5EIfQw953vvkFEZW6lTk_X_ObioCidvQxYEAl__IOiSgIqhtiKeHfLCXQezyyfQcbH7V-pTLJN4Y5knPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edfa0f08c.mp4?token=cn8sVoLgdEAMtdedWFPvgycOKLQ5x3oHou8zp4pzyeWVWxKczuZY_-ic21G7_7-cfKwmx6N4IAyvG6LkJKYdG8vzqzIbdI6RK0euH3P4bKstT5vD7bRY2xaeD4kw4Q8dAXtpritrvqHLb7-dQxJHDV5Lx3KbjsQoXNwdCnerfe_CZwepw6EpU8IPitWSz1ibBKaFWuy0Zo6xfS1Ru8qC_bHWRiprr7B01EIAajmTaFOYbw497WUXTxkQNLeU86L2hGgqH5EIfQw953vvkFEZW6lTk_X_ObioCidvQxYEAl__IOiSgIqhtiKeHfLCXQezyyfQcbH7V-pTLJN4Y5knPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
اوضاع ایران داره عالی پیش میره ما کاملاً کنترل تنگه هرمز رو در دست داریم و نیروی دریایی‌مون فوق‌العاده‌ست
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20865" target="_blank">📅 08:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">زاکانی : آقا مجتبی داشت تلویزیون میدید یهو تو اخبار شنید رهبر شده
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20864" target="_blank">📅 08:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87bdfe17b.mp4?token=Syl9DoHwuJf2oVzWgDffchlRNkpPNMcSRSWEr3hTxHcf24K6RcBsffnBAlxeKjA_XrS7X7AIy2E0CJEF6yC3Xk9KgohrBwDVXk-aVwnHHv4ZmmL4oVB9Z0FO9pIO2uC4X5FQT3UDuy3U_UrYlRcpMjUlV3VBxhNPXmo9JRH0RlkAM0SWQFXxDEMPB7i_x_WxYrWnqtQH_QkHf54KEIOWhilbmO6CWPvhP6-SAzO1UH8DdLd1fEwp0f-JcfEJ9cKJAbuuqmkW4aGakWwvexjYyXpxtlT73r6GOqoV0wQ5EfSgK6g4MaDQxHFxXtzt24dmnAmkQ-21z4ax-hhK3c1qeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87bdfe17b.mp4?token=Syl9DoHwuJf2oVzWgDffchlRNkpPNMcSRSWEr3hTxHcf24K6RcBsffnBAlxeKjA_XrS7X7AIy2E0CJEF6yC3Xk9KgohrBwDVXk-aVwnHHv4ZmmL4oVB9Z0FO9pIO2uC4X5FQT3UDuy3U_UrYlRcpMjUlV3VBxhNPXmo9JRH0RlkAM0SWQFXxDEMPB7i_x_WxYrWnqtQH_QkHf54KEIOWhilbmO6CWPvhP6-SAzO1UH8DdLd1fEwp0f-JcfEJ9cKJAbuuqmkW4aGakWwvexjYyXpxtlT73r6GOqoV0wQ5EfSgK6g4MaDQxHFxXtzt24dmnAmkQ-21z4ax-hhK3c1qeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در محل بازی‌های میهن‌پرستانه:  به والدین نگاه می‌کنم، آنها به فرزندانشان بسیار افتخار می‌کنند. و من به گروه افراد حاضر در این اتاق بسیار افتخار می‌کنم. عشق به کشورمان را می‌بینید. کشورمان هرگز بهتر از این نبوده است!
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20863" target="_blank">📅 02:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چیزی نیست رعدنیاهو بود غرب تهران
😂</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20862" target="_blank">📅 02:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش صدای رعد و برق شدید</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20861" target="_blank">📅 02:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20859">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بلومبرگ
:
دونالد ترامپ موضع خود را در قبال ایران سخت‌تر کرده است و این امر، امیدها را برای دستیابی به توافقی جهت بازگشایی تنگه هرمز کمرنگ‌تر ساخته است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20859" target="_blank">📅 01:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20858">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش ها از درگیری تمام عیار زمینی میان حوثی های یمن و نیروهای نظامی وابسته به عربستان در شمال یمن.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20858" target="_blank">📅 01:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20857">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آمریکا 2 هزار گیمر رو به‌خاطر تصمیم‌گیری سریع و عملکرد خوب تو شرایط پراسترس ، برای برج مراقبت فرودگاه‌ها استخدام کرده
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20857" target="_blank">📅 01:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20856">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ab5e54bb.mp4?token=f3EeJq8QPIbwjt_VUk-pIL_kz-Sx1HRBGPWmraoNLqjtpHrmQkV65Jv9Ri5GqSDSxubqKIU3OSgVAT6thJp66C8Hppa0jWGjWRe8XoveCvFXTE0_TkffBz4-y-x7iks9aiopGRJn6n0MMP9SaFrZi21xd3bfaH7c-adV4qaNOcJguaE9lWaOgY6eQg36zoppJT6r-3BnKCx9FTlCHENSihQMyb1VdTPm94IRzBy7tqMYRmrjdoDbL89jRQCOZudXEF-VdcJMy4uA8v_BlSoWykiJeqICPpoHLPZxX1IZjLOlP15xPN40brn--h_Tu5j46LYlbYPSbQM3amVSXeKGr4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ab5e54bb.mp4?token=f3EeJq8QPIbwjt_VUk-pIL_kz-Sx1HRBGPWmraoNLqjtpHrmQkV65Jv9Ri5GqSDSxubqKIU3OSgVAT6thJp66C8Hppa0jWGjWRe8XoveCvFXTE0_TkffBz4-y-x7iks9aiopGRJn6n0MMP9SaFrZi21xd3bfaH7c-adV4qaNOcJguaE9lWaOgY6eQg36zoppJT6r-3BnKCx9FTlCHENSihQMyb1VdTPm94IRzBy7tqMYRmrjdoDbL89jRQCOZudXEF-VdcJMy4uA8v_BlSoWykiJeqICPpoHLPZxX1IZjLOlP15xPN40brn--h_Tu5j46LYlbYPSbQM3amVSXeKGr4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ برای شرکت در رویداد
Freedom 250 Patriot Games
(رقابت‌های میهن‌دوستانه ورزشی ویژه جوانان آمریکایی به مناسبت ۲۵۰مین سالگرد استقلال آمریکا) عازم شهر ژنو در ایالت اوهایو شد و سوار هواپیمای ریاست‌جمهوری
ایرفورس وان
جدید شد
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20856" target="_blank">📅 00:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20855">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش ها از هدف قرار گرفتن ایست ‌و بازرسی نیروهای نظامی توسط افراد مسلح ناشناس در شهر مرزی خاش در سیستان و باوچستان ، بر اساس گزارشات داخلی 4 نظامی در این حادثه کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20855" target="_blank">📅 00:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">محمدرضا نقدی، مشاور فرمانده سپاه، گفت که «این سازمان باید برای انجام عملیات هوشمند در خاک دشمن آماده شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20854" target="_blank">📅 00:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم  @WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20853" target="_blank">📅 00:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMdQwTo0Ws5Wm4cYbTWBxMPiCIdyYppXrt2_QSk4fxT-UYSmc20TWN85I92xXQ9mN_mOL-DDWCgSSUCdAA7V_FFdWa5tBweLEZG0UHGGrKYG7Ej3GkbsdNKUG-xdZBl34PtHvru7IMa370Xh0NBb4hegpDMvHH4C7dWY97UwBVIGVtr6qz5ufM2qsh6yQzIr-gQeYm7iRjiDaSvp2fDhgZvu5lsh_eCQtvmsfX311Vjz7frF4allx7tczhspRvs0667q_eObE0c0IxPtmsiZbk9qdEmZQwh-kgu2H_WIe6qSNfaOBWP9Ec2snnHXXpAgXPukEyI9UgfyCXuE_xlNLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل: مجتبی شش تندرو جدید را برای رهبری جنگ بعدی ایران منصوب می‌کند
با وجود شایعات فزاینده درباره سلامت مجتبی خامنه‌ای، تهران ادعا می‌کند که او شش تندرو از رژیم را برای رهبری جنگ بعدی ایران منصوب کرده است؛ پیامی نگران‌کننده برای اسرائیل و ایالات متحده مبنی بر اینکه رژیم در حال تشدید تنش‌هاست، نه عقب‌نشینی
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20852" target="_blank">📅 23:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">باراک راوید , آکسیوس : امید به توافق میان جمهوری اسلامی و آمریکا در حال محو شدن است
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20851" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20850">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6P-myFd8KEeeGuEeL53CsJE7gpHeFJJypK1535wvAQu8ubAu5--B4qZbcLiq5Ympaw8KQP8Tqudnk9kJgVjLJH_Gcv9eVwb8AZ9wk0CelFg860UjCNo5suO0OWcX9lDTqK-rsbKKheM21HGnnaP0D0pWsLvPQkPPHL3asIO2tzfiSbxLYQuWoQGQo9IZP8mD3OtA_10nfTFHSxfUaTexhtnIPU2G1vrfoJh6zf-woQ-1ASkLHCj55kPx52WH8xDCfH6cLQFoGxRpZBZYe9fiXiTvGvzEfXXpbjZ2d7uqToP05rGszmhzTqc-fXOAiDRnMMengvu6cIQPQXY6i6ufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی امروز کشتی باری «ولا نوا» با پرچم پاناما را هنگام حرکت به سمت یکی از بنادر ایران در خلیج عمان متوقف کردند. پس از بی‌توجهی خدمه به هشدارهای آمریکا، یک بالگرد MH-60 دو موشک هل فایر به اتاق موتور کشتی شلیک کرد و سامانه هدایت آن را از کار انداخت. سنتکام گفت تا ۱۱ اوت، ۵۵ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را سوار و بازرسی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20850" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20849">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA B</strong></div>
<div class="tg-text">یاشاار
جون هرکی دوست داری زارتان زورتان و حذف نکن از ادبیاتت
من هم توهمی دهنم سرویس شده
از وقتی نمیگی برکت از جنگ رفت
🤣
خداییش جدی میگم</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20849" target="_blank">📅 22:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20848">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سازمان دریایی بریتانیا: فعالیت‌های سپاه در تنگه هرمز در طول 48 ساعت گذشته ادامه داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20848" target="_blank">📅 22:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20847">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دونالد ترامپ در چارچوب قانون اختیارات جنگ آمریکا (War Powers Resolution)، با ارسال نامه‌ای به کنگره که ۱۹ تیر ۱۴۰۵ امضا و ۲۲ تیر ۱۴۰۵ به‌طور رسمی اعلام شد، از ازسرگیری عملیات نظامی علیه ایران خبر داد. با این اقدام، مهلت قانونی ۶۰ روزه برای ادامه عملیات نظامی بدون مجوز جدید کنگره آغاز شد. این اقدام به معنای صدور مجوز جنگ از سوی کنگره نیست، بلکه صرفاً روند قانونی اطلاع‌رسانی به کنگره و آغاز مهلت ۶۰ روزه را فعال می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20847" target="_blank">📅 21:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20846">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20846" target="_blank">📅 21:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20845">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">من با دیتا های اپن سورس تحلیل میکنم پیشگو که نیستم ! هیچ تاریخی هم نمیدم فقط احتمالاته اگه انقدر حساسی  پس از الان رو نزدن حساب کن  ! اگه حرفه ای هستی پس ویس هارو گوش کردی کامل روحیات منم میدونی و دیگه سوألی هم نداری که هی داریکت بدی</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20845" target="_blank">📅 21:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20844">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به نظرت قطعی شنبه میزنه من میخوام با بچه ها شرط ببندم</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20844" target="_blank">📅 21:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20843">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSajad Mousavi</strong></div>
<div class="tg-text">به نظرت قطعی شنبه میزنه من میخوام با بچه ها شرط ببندم</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20843" target="_blank">📅 21:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20842">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش ۲ ‌انفجار یا پرتاب موشک/پهپاد از سیریک @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20842" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20841">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش ۲ ‌انفجار یا پرتاب موشک/پهپاد از سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20841" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20840">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ اعلام کرد که رابرت گیلمن، سرباز سابق نیروی دریایی ایالات متحده که در سال ۲۰۲۲ در روسیه زندانی شده بود، پس از گفتگوها با ولادیمیر پوتین، آزاد شده و به ایالات متحده بازمی‌گردد.
ترامپ گفت که روسیه موافقت کرده است گیلمن را بر اساس «ملاحظات انسان‌دوستانه» آزاد کند و «هیچ مبادله‌ای انجام نشده است».
ترامپ همچنین گفت که اولین درخواست گیلمن یک «همبرگر عالی» بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20840" target="_blank">📅 20:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20839">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ : ما بر پول ایران کنترل داریم و کنترل کاملی بر آن اعمال می کنیم
ترامپ : سلاح و جنگنده به اروپا می‌فروشیم و آن‌ها در ارسال به اوکراین آزادند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20839" target="_blank">📅 20:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20838">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسرائیل و ونزوئلا پس از ۱۷ سال قطع روابط دیپلماتیک، توافق کردند که روابط کنسولی خود را از سر بگیرند و یک کانال هماهنگی رسمی ایجاد کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20838" target="_blank">📅 20:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20837">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797367122e.mp4?token=t0BwaOwMlYnuVYjLpGoOgNUZNDC-neONSEPIOBpeCcmx3iz0IgADaHw1qm9RJxlWx_eccuQbg0PREJ4WCcAhOEk6qKXp-GI7pbtRJVcXpNLFv0AFMqxBBf0d9Q2x5a2NrObJu94WR3jcSZVmCW0UhynQN_gCnJpEUO-dOCmMYwKga4eQyAhiE8bSZ-oY-lXEa-SsYGBHVU2j4kNWsF3Jy5uyLYDCKNyHr1EmbYJKGFyB_aIUOWXre2zj7a6mgsj89RaMbSgV-lWQaQe08uPWn8bhFCW2xKbtLLPtEx5705bU46Zohh0Zfhc23U13zmwJShOAzs4vAGduUI1_T6ZarQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797367122e.mp4?token=t0BwaOwMlYnuVYjLpGoOgNUZNDC-neONSEPIOBpeCcmx3iz0IgADaHw1qm9RJxlWx_eccuQbg0PREJ4WCcAhOEk6qKXp-GI7pbtRJVcXpNLFv0AFMqxBBf0d9Q2x5a2NrObJu94WR3jcSZVmCW0UhynQN_gCnJpEUO-dOCmMYwKga4eQyAhiE8bSZ-oY-lXEa-SsYGBHVU2j4kNWsF3Jy5uyLYDCKNyHr1EmbYJKGFyB_aIUOWXre2zj7a6mgsj89RaMbSgV-lWQaQe08uPWn8bhFCW2xKbtLLPtEx5705bU46Zohh0Zfhc23U13zmwJShOAzs4vAGduUI1_T6ZarQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20837" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20836">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رسایی : چونکه نمیدانیم اسرائیل کِی حمله میکند مجبوریم جلسات مجلس را مجازی کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20836" target="_blank">📅 20:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20835">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پست قبلی بی بی پاک شد این پست کارای اداری رو انجام بدید
https://www.instagram.com/reel/Db6BHf7MYhi/?comment_id=17896725462373851</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20835" target="_blank">📅 20:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20833">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتانیاهو : جولان سرزمین ماست و برای همیشه متعلق به اسرائیل خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20833" target="_blank">📅 18:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20832">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دونالد ترامپ: ایالات متحده می‌تواند بزودی و با قدرت بسیار زیاد به ایران حمله کند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20832" target="_blank">📅 18:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20831">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یوآو کیش، وزیر آموزش اسرائیل:
صرف نظر از اینکه رئیس جمهور آمریکا چه کسی باشد، حتی پس از ترامپ,  اگر لازم باشد به تنهایی اقدام کنیم، به تنهایی اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20831" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20830">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL7Z6ctKBNWI1lpw6WjlZ5fyLkM22r6wPp-JEqA2CPTFo5yhitJYacKPxVgV0bgtgaEeaBMqS7VvKYl7DIihViD_kFVVPNQTUMBja4yHjixxQ0sQdpEQRTGgpsgLKia3InCntMfzKlniUZ_ba2wLgRbnLcmCG-E-i_Aq3PNs33p60i-SwYrKk-UTExkkfEp-vsSXZFfVO-i8kfVMBmRLgHaRytRMmdVwssS9MXwkchF8DsVZ0StC-JIh3aTPts3KMKG_0P24WU9KI2KuLkc9vFYVZ4CNAM9kh1I3CvzgtydCI3JDTIAAgZmf6fjn0Zsuw4ltwRMi_U2DUrD5Drzbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه اسرائیل : ترکیه این جسارت را دارد که از اسرائیل انتقاد کند؛ اما واقعیت‌های میدانی چیست؟ هزاران سرباز ترکیه و ده‌ها پایگاه و موضع نظامی در سوریه، عراق و قبرس مستقر هستند. در حالی که تجاوز نظامی اردوغان مرزی نمی‌شناسد، ترکیه ۳۶ درصد از خاک قبرس، ۵ درصد از خاک سوریه و ۲ هزار کیلومتر مربع از خاک عراق را در اشغال خود دارد. در مقابل، اسرائیل به‌طور موقت تنها ۰.۱ درصد از خاک سوریه را در اختیار دارد؛ منطقه‌ای حائل که به گفته اسرائیل، برای حفاظت از شهروندانش در برابر تهدیدهای امنیتی اثبات‌شده ایجاد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20830" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20829">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به گزارش رسانه‌های اسرائیلی،
یوسی کوهن، رئیس پیشین موساد در نشست «مجمع جلیل» در شهر صفد گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک و شناسایی کنیم.»
او مشخص نکرد که این بازدیدها چه زمانی انجام شده یا دقیقا چه کسانی از این سایت بازدید کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20829" target="_blank">📅 17:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20823">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">روال هر روز پیج اینستاگرام در ۴ دقیقه ریکاوری شد
😁
عرضشی عر بزن
🤣</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20823" target="_blank">📅 16:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20822">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu3odwoE5v9qDzHfSqt6xSYGo8mgVnhEa-gvLbpNrhIMI25poBopK-CeK6hYmHl8eWkM91tesRHFnC0KfcuHz_U0lFhk_6U-Em9QPA-2eQtsq4IfH_bbG7uTwFEv0wE16-vzQBUzDKIOwt-U493Cw-s8IypPELe0KX9WaauIuTvYQPS3Bu-k1-pf7a4YOKhNCSjvTCc0-JGt76UmFfvhpygw8Z6_0EPr43HCI7jd2KotmL6gCazk-l3t1wuxQaBvsNSoxbb22nhkaw6MNSIiavg_k9S8FBJZ0SCk_YNYcpJJMuqSZNIcThFDKkV6cEc0HwfJcXypyKLSJwupSi3-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی بی دوزندهیاهو : آتش‌سوزی در کارخانه نخ اطراف بیدگنه،  ملارد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20822" target="_blank">📅 16:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20821">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دبیر شورای عالی امنیت ملی ج.ا : ما در یکی از حساس‌ترین و سرنوشت‌سازترین مراحل تاریخ معاصر خود قرار داریم , در برابر تهدیدها، از حقوق خود و منافع ملت‌مان عقب‌نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20821" target="_blank">📅 16:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20820">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وال استریت ژورنال : نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه. @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20820" target="_blank">📅 16:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20819">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وال استریت ژورنال : نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20819" target="_blank">📅 16:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20818">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وزیر دفاع پاکستان به بلومبرگ:
نشانه‌های روزهای گذشته حاکی از آن است که به توافق صلح (یاشار: بمباران) نزدیک می‌شویم
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20818" target="_blank">📅 16:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20817">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">روال هر روز پیج اینستاگرام در ۴ دقیقه ریکاوری شد
😁
عرضشی عر بزن
🤣</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20817" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20816">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آکسیوس
:
به گفته مقام‌های آمریکایی و اسرائیلی، دولت دونالد ترامپ در پشت‌پرده میان سوریه، اسرائیل و آژانس بین‌المللی انرژی اتمی برای خارج کردن مواد هسته‌ای از «سایت ۹۹» سوریه، مرتبط با برنامه هسته‌ای مخفی حکومت بشار اسد، توافق ایجاد کرد. این مواد شامل «کیک زرد» است که برای ساخت سلاح هسته‌ای کافی نیست، اما می‌تواند در بمب‌های رادیولوژیک به کار رود. اسرائیل پس از سقوط اسد با نگرانی از دسترسی به این مواد، ورودی‌های سایت را هدف قرار داده بود. عملیات انتقال هنوز انجام نشده، اما مقام‌های آمریکایی می‌گویند به‌زودی اجرا خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20816" target="_blank">📅 15:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20815">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وال‌استریت ژورنال : خامنه‌ای با تغییر مقام‌های ارشد امنیتی بر ادامه تقابل با آمریکا تاکید دارد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20815" target="_blank">📅 15:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20814">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش حمله موشکی به اردوگاه گروه‌های کورد در شمال شرقی اربیل
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20814" target="_blank">📅 15:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20813">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9-_VkpJzxdbxOZH7moaeMQ1j7uod2afcK57fBLHBIxpMquczozGttkLaAx6lfYp1rsLfVqQNxGVvhwg1NXtokwWCZkz87MWC2vKl4qNMcV2Ew1aAAbryOKPDqBBsrInNKAJBBBzRNcXlN6FgKaEkE_8wl9XsqcNgyu8Hg7DBtENVg5aDUmoT_C_WFcVytv7K883uskFdn-MblxHSFPcKloStKVFAcFMege2IZwJBpGQE8m2wY9-b88MOXtAfKyehuvNG6LhrVPdQjPlRm4OUGCKYvMwFMpG0USM7t4rn0UsEk7NUlX6KPg4OAdYB3f0eOsVYFl2SSyuvploZehy4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری رویترز، سازمان حمل و نقل دریایی بریتانیا (UKMTO) از حادثه‌ای در سواحل المخا، یمن مطلع شده است. گزارش شده است که یک کشتی باری در دریای سرخ جنوبی مورد اصابت یک موشک/پهپاد ناشناخته قرار گرفته و منجر به تلفات جانی شده است ، این در حالی است که یک کشتی سعودی صبح امروز مورد هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20813" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20812">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سید محسن رضا نقوی، وزیر کشور پاکستان برای گفتگو با مقامات ایرانی وارد تهران شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20812" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20811">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رسانه عبری : مجتبی خامنه‌ای، از احمد وحیدی، فرمانده کل سپاه پاسداران، خواست تا برای «عملیات تهاجمی قدرتمند علیه دشمن» آماده شود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20811" target="_blank">📅 13:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20810">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ درباره ایران: ما سه راهبرد داریم , همین کاری را که الان انجام می‌دهیم ادامه دهیم؛ فقط به همین شکل پیش برویم و ببینیم اوضاعشان چقدر بد است، چون تورمشان ۳۰۰ درصد است. پولشان تقریباً هیچ ارزشی ندارد. حقوق سربازانشان را نمی‌دهند. سربازانشان در حال ترک خدمت هستند. بنابراین همین روند را ادامه دهیم، چون این وضعیت پایدار نیست.
خیلی، خیلی سخت به آنها ضربه بزنیم؛ یا در واقع، راه سوم این است که از نظر اقتصادی آنها را شکست دهیم. البته همین کار را همین حالا هم انجام می‌دهیم. این تا حدی بخشی از راهبرد اول است.
بنابراین از نظر اقتصادی، آنها در وضعیت بسیار بدی قرار دارند. نمی‌توانند پول قرض بگیرند. ما کنترل پول آنها، یعنی آنچه در اختیار داشتند، را در دست داریم؛ و مقدار آن هم زیاد است. آنها پول زیادی داشتند و ما کنترل کامل آن را در اختیار داریم.
من بانکدار آنها هستم. من بانکدار آنها هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20810" target="_blank">📅 13:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20809">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ : می‌خواهید یک گورستان پرندگان را ببینید؟ گاهی اوقات به زیر یک آسیاب بادی بروید و هزاران پرنده مرده خواهید دید.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20809" target="_blank">📅 13:50 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
