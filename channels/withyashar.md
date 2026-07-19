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
<img src="https://cdn4.telesco.pe/file/RcNWJov13IRwYWKvNLtkRKXmHoK2PuJsOyDHUXwV5gJejWWv8cEh3hw-UE5p36v6HCnSH7Ozv7imNkbGJWIfvnMa-3Q2gmZI4eKURg42ZCzKTTKBaYa67edaOxHbZpI9IrrIYLDEsvd-kQ9Fa-f0CrpVtC-X2kxBYR10anlhBftsW3H1UweAdv8XumWhg3-1KaytA4llOoz2L3P_MG4bPMBR0g0fn_un0hoAjRa14T_xIziJ0EDvFzOLgdoifsGvRhG-4JyN88-YlFYXslv20CI5mcB2cHSxHqFUIEJpra9977P7wvazA0n82IKR0ePuLlNByLFR_nNsIrGSyNH4aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 411K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 11:07:53</div>
<hr>

<div class="tg-post" id="msg-18838">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e681b632df.mp4?token=f3ylE0cqo6MgyV9UkXFb65eqGP4a-72SCjdtCcyQpm9p-d7BYbTl9naiDfGbVn9flLAfC7NIwSFhw-tiE5g3YXNHUZ64dnlVvqNot7XaQEUwqye6yCN4DyF6MjAc6rZVeGSWALJ9xdNoTYqLTE49DasKiDYB61TjNMAgAeLmk2q1BjkI88BOzuYLrdjsBbpkMVvjNHCQQPUfDV1y04_CZwsW80DS1-Kc29RQCEbLXf3Qe78y5KxJcFT6_1qRHd_AGSHAXXKIw6WkAjX3zLgx3j8c8bkpbO6DoKlQI93pl-oMD-wp6IcGjoptsePIdM-9elLCbLJS6KVPvLj3BO903RmSujjOWV4t-FwWamP1iok8HIgSYmdISkcodYgRw5xodGGczQZK36rycCjLAVbYALvmjOrfqMa2KZf-ewWf8oSHewBaP-aFnYJrsSUBmw0176bwlrXk94Tb0CbEx2LViPDpMcRr4Q_OtvZYD6O8Vw6_r4n6Csx8XGZDqf80lI6GH8hpyyXPWQEmxextbC0LXLjd3R6HB5A-OZ7-p97M-nW7c8ySgl85GZkJGWnLLQcu7sxFJUCVzr0R74F-5JNqcugzSa7t20oiPrxa39n58kLtJHziasAwCYS86leu03Nur5wh2OUqgAQOl62w9pYhatGngt4IbvuIGpEd2EJ2CpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e681b632df.mp4?token=f3ylE0cqo6MgyV9UkXFb65eqGP4a-72SCjdtCcyQpm9p-d7BYbTl9naiDfGbVn9flLAfC7NIwSFhw-tiE5g3YXNHUZ64dnlVvqNot7XaQEUwqye6yCN4DyF6MjAc6rZVeGSWALJ9xdNoTYqLTE49DasKiDYB61TjNMAgAeLmk2q1BjkI88BOzuYLrdjsBbpkMVvjNHCQQPUfDV1y04_CZwsW80DS1-Kc29RQCEbLXf3Qe78y5KxJcFT6_1qRHd_AGSHAXXKIw6WkAjX3zLgx3j8c8bkpbO6DoKlQI93pl-oMD-wp6IcGjoptsePIdM-9elLCbLJS6KVPvLj3BO903RmSujjOWV4t-FwWamP1iok8HIgSYmdISkcodYgRw5xodGGczQZK36rycCjLAVbYALvmjOrfqMa2KZf-ewWf8oSHewBaP-aFnYJrsSUBmw0176bwlrXk94Tb0CbEx2LViPDpMcRr4Q_OtvZYD6O8Vw6_r4n6Csx8XGZDqf80lI6GH8hpyyXPWQEmxextbC0LXLjd3R6HB5A-OZ7-p97M-nW7c8ySgl85GZkJGWnLLQcu7sxFJUCVzr0R74F-5JNqcugzSa7t20oiPrxa39n58kLtJHziasAwCYS86leu03Nur5wh2OUqgAQOl62w9pYhatGngt4IbvuIGpEd2EJ2CpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : دست فرمون شما ما رو رسوند به جنگ
خلاصه گفتگو با سید عباس عراقچی
@WarRoom</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/withyashar/18838" target="_blank">📅 11:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18837">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرماندار چابهار گفت: صدای انفجار شنیده‌شده امروز، ۲۸ تیرماه، در حوالی این شهر مربوط به عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده و هیچ خطری شهروندان را تهدید نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/withyashar/18837" target="_blank">📅 10:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏ارتش جمهوری اسلامی با صدور بیانیه‌ای، مدعی حملات تازه به دو پایگاه نیروهای آمریکایی در کویت شد.
‏در این بیانیه آمده که ارتش جمهوری اسلامی در پی «حمله به پل‌ها، زیرساخت‌ها و مناطق غیر نظامی»، انبار مهمات ارتش آمریکا در اردوگاه العدیری و رادار پاتریوت و رادار هوایی این ارتش در پایگاه علی‌السالم کویت را، آماج حملات پهپاد‌های خود قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/withyashar/18836" target="_blank">📅 10:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیویورک پست از قول دونالد ترامپ: کشته شدن دو سرباز آمریکایی مایه تاسف است، اما ماموریت نظامی همچنان ضروری است
@WarRoom</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/withyashar/18835" target="_blank">📅 10:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اگر تهران متوقف نشود، منطقه ممکن است وارد یک درگیری گسترده‌تر شود
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/18834" target="_blank">📅 09:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وال استریت ژورنال: بر اساس اظهارات افراد مطلع، در حمله ۱۷ ژوئیه ایران به پایگاه هوایی موفق السلطی، علاوه بر موارد دیگر، هواپیماها و پهپادها نیز آسیب دیدند
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/18833" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18832">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Iz1-x8dAYFGCCDlBWYnpTWx2LZjRdev5uYXLB7cL5BfRq16gB613FOwkuI9cXHhAygWCx0NMApt6Hx4cJO9RguN71gyFkjFjBY8hDmNSzpgN-6ocvmrqb1ZfHtqayUV7vVAWEluR4xbY_pt3-BDrv3BEfMWHo3prMGDE_3OyALwLouQdJ2jDtVPLcXfcOyF44A2JHWmwr50CMAPlEhmC1Yzz-KsMsQg-RtJtIfQmm_ROEtkhgb5zPOpHJQNJoUiDrLMAlECwOPr4dm2UWgfsLsjpn0XqOtX8IJ-OqlsNwwBWPJn-qVtoyHujJIfpIjuHDUdBYBNDCabMCpxBvCHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله در دزفول و اهواز @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18832" target="_blank">📅 08:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18831">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">معاون امنیتی ‌استانداری خوزستان:
جنگنده‌های‌ آمریکا ساعت ۰۵:۵۵ دقیقه نقاطی در اطراف شادگان را مورد اصابت موشک قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18831" target="_blank">📅 08:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18830">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سایت موشکی خمین ,کوه انگشت لیس , بین خمین و گلپایگان @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18830" target="_blank">📅 08:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18829">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">زلزله در دزفول و اهواز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18829" target="_blank">📅 08:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18828">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95514648b.mp4?token=NC-z4i61X0GebNF9dogSrqobPAgtcaKE_i1-ZJL0hCGCBz_lVnpuG1YGauFzX3cfHYp4wlCAFRa-gVJ_M_yzs-AWySkdVhaMhOzPWKPHRGgGgTOi6xP278r6g0tP1hBZSg3Q2cfx4_5M_ZchYf5AsqUBHdgxeNPn27NP4-wzMBEg517gLE4RMerXZIa_IT0JaNDrBvGPZ2FTzmNNW5zdfLV8tiM1W9_1kwJrLK2KCP2Gj6RqBQoFonDWEkKgwJ0IbCkujre3L06kym82lfaFRwKV_KFAdXESKkY16zAPI1jyL9zFWGCx6_Yh3s_RzoN5DXfW1bupE5J92Epke5HcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95514648b.mp4?token=NC-z4i61X0GebNF9dogSrqobPAgtcaKE_i1-ZJL0hCGCBz_lVnpuG1YGauFzX3cfHYp4wlCAFRa-gVJ_M_yzs-AWySkdVhaMhOzPWKPHRGgGgTOi6xP278r6g0tP1hBZSg3Q2cfx4_5M_ZchYf5AsqUBHdgxeNPn27NP4-wzMBEg517gLE4RMerXZIa_IT0JaNDrBvGPZ2FTzmNNW5zdfLV8tiM1W9_1kwJrLK2KCP2Gj6RqBQoFonDWEkKgwJ0IbCkujre3L06kym82lfaFRwKV_KFAdXESKkY16zAPI1jyL9zFWGCx6_Yh3s_RzoN5DXfW1bupE5J92Epke5HcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام :شب هشتم تمام شد
ما
دور تازه حملات علیه ایران
در
۱۸ ژوئیه، ساعت ۱۱:۳۰ شب به وقت شرق آمریکا (ET) (۰۷:۰۰ صبح ۱۹ ژوئیه به وقت تهران)
و
به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)
به پایان رساندیم.
به گفته سنتکام، در
هشتمین شب متوالی
حملات آمریکا، نیروهای این فرماندهی
تأسیسات دیده‌بانی ساحلی و پدافند هوایی، توانمندی‌های دریایی، و انبارهای موشک و پهپاد ایران
را با موفقیت هدف قرار دادند تا توانمندی‌های نظامی ایران بیش از پیش تضعیف شود. همچنین نیروهای آمریکایی،
عناصر سپاه پاسداران
را که به گفته آمریکا در
۱۷ ژوئیه (۲۶ تیر)
در حملات علیه نیروهای آمریکایی در اردن مشارکت داشتند، هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18828" target="_blank">📅 08:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18827">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09cf3dc329.mp4?token=vtZT_MwuvFHUYoPuCpJ-tEXR532Dhizl4Sv_A3-lnoVqdniRJPKyge-RWTTyfTj1kV_u1VlkGb-WrKMG6gRQpf4L-GoBiNHE3VDPD3tZQ-zzr4aNTcm17TdWIYA7USJLj5IZ1gPROogdcIgf-EeEOlG4Y_f4hMgvBk04PUJ_OER3Yd38UMwrk4Hq2U6tNIrqYVUrBq4bxrx_pJLyfu6ad4JjKBumVZ2DU61THsGlWdt4c9rd4abyOLXPTLdwX4cF_6HxCeGfzaLWfjz1pl5dY_iaYqs6txNkbgLm9w3zVjw11AQsRr1BNZSOEE7sB-vTuEX3wqwnbF8d8tBRamgoYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09cf3dc329.mp4?token=vtZT_MwuvFHUYoPuCpJ-tEXR532Dhizl4Sv_A3-lnoVqdniRJPKyge-RWTTyfTj1kV_u1VlkGb-WrKMG6gRQpf4L-GoBiNHE3VDPD3tZQ-zzr4aNTcm17TdWIYA7USJLj5IZ1gPROogdcIgf-EeEOlG4Y_f4hMgvBk04PUJ_OER3Yd38UMwrk4Hq2U6tNIrqYVUrBq4bxrx_pJLyfu6ad4JjKBumVZ2DU61THsGlWdt4c9rd4abyOLXPTLdwX4cF_6HxCeGfzaLWfjz1pl5dY_iaYqs6txNkbgLm9w3zVjw11AQsRr1BNZSOEE7sB-vTuEX3wqwnbF8d8tBRamgoYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش انفجار  در قشم
@WarRoo
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18827" target="_blank">📅 05:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18826">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سکوت عجیبیه</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18826" target="_blank">📅 03:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18825">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سنتکام: امروز ساعت 6 عصر به وقت شرق آمریکا، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی رو علیه ایران آغاز کردن. هدف این حملات، تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب…</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18825" target="_blank">📅 03:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18824">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جزیره لارک سایت سپاه رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18824" target="_blank">📅 03:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18823">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجار‌سایت موشکی حاجی اباد، هرمزگان  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18823" target="_blank">📅 02:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18822">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDwNeSXT5yTnPgMzjk8RcLbUWCa5hYl_7lcmQsiEMurPNJwCQUYYbCYc2I4Y6hiV04f0Fs8EwG_jCPhTdGoNI3ztYpl2DUaS6glQ8e-4bmR4ho6X7j5SHXw_MFNbalUN4okx23FOgICY22GENTa8sLq8xk8FovVVBGuNizNNx6lCJ74mxwulKmOkXHmHgGOmkHV1ENQh1CE5AEEXyHihmzxnlnf2W8zzRiTNFgyj1GToJJWe9zzrwkcoCE19_s04OAB_fhcV_w7qzhEwlCbNtQGVkFgTtgrg5JvacHvBJZWucWKqE1JIYtGxKsmxt81iKPxxZUYY6KocVz8zW5z4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار جان الان امدم بالا پشت بوم جنوب تهران ستون دود بلند شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/18822" target="_blank">📅 02:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18821">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از مدتها نمیتونم ببینیم چیزی
🤒
همه رفتن زیر پتو رررپتپتوووو  @WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18821" target="_blank">📅 02:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18820">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک صدایی شبیه به انفجار در کوه دراک شیراز که شهر موشکی هست شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18820" target="_blank">📅 02:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18819">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار‌سایت موشکی حاجی اباد، هرمزگان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18819" target="_blank">📅 02:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18818">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش انفجار خرم آباد لرستان
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18818" target="_blank">📅 02:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18817">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18817" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18816">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هیچ گزارشی از‌ بندر عباس نیست !
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18816" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18815">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش انفجار در بوشهر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18815" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18814">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش‌ انفجار در اراک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18814" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18812">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18812" target="_blank">📅 02:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18811">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18811" target="_blank">📅 02:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18810">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18810" target="_blank">📅 02:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18809">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18809" target="_blank">📅 02:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18808">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش حمله با موشک های کروز تاماهاک (که خامنه ای‌رو کشت ) توسط ناو های آمریکایی‌به ایران
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18808" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18806">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مسیر جاسک (بیاهی) از طرف دریا  ۳۰ جنگنده اومد
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18806" target="_blank">📅 02:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18805">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حقیقت یاب اناق جنگ : همانجور که اعلام نکردم سیریک خبری نیست فقط نیم ساعت پیش صدا جنگنده اومد اما انفجاری چیزی رخ نداد فیک نیوزه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18805" target="_blank">📅 02:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18804">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">۲ انفجار بندر لنگه
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18804" target="_blank">📅 02:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18803">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جنگنده های آمریکایی بر‌فراز ‌کیش
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18803" target="_blank">📅 02:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18802">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش انفجار‌اهواز
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18802" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18801">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18801" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کانال ۱۴ : کنسولگری آمریکا در اربیل کردستان عراق در حال حاضر مورد حمله شبه‌نظامیان تحت حمایت ایران قرار گرفته است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18799" target="_blank">📅 02:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcMXFXtMNeaOtfJ4P8f6m5UqwSD9icbcJdNkpQN3UuIkxkycThUtSKNwZiDp_0zVby-cB1nruVZkt3gsAN7CdqJLu_3A6owUvJrUXBstCJuRFi10dusJyhh2a9aiCCP0k2SSLPyIfe-wWWGZz-qXVLt1Dd4cDtTfpdBgo3usVf669yjX9tL7iTlXUey0mNEhWusm-d-CMgu2GvuVMIg63idGN17k36Ios9wi4MIEjqu8B0QF41_TPkq4yjYiniUM79emEs5eQhHVRJUAdvae0_qQi3_7gnGid6FHuBrd1v8D1NKZNN6AVFMr-TQ0uYSOV1wnbVwhH3kuEpilUDBo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اربیل عراق کنسولگری‌ آمریکا رو زدن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18798" target="_blank">📅 02:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18797">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18797" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18796">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18796" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18795">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سنتکام: امروز ساعت 6 عصر به وقت شرق آمریکا، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی رو علیه ایران آغاز کردن.
هدف این حملات، تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی است که شب گذشته حملاتی رو علیه نیروهای نظامی آمریکایی در اردن انجام دادن.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18795" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18794">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سنتکام آغاز حملات را اعلام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18794" target="_blank">📅 01:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18793">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سنتکام آغاز حملات را اعلام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18793" target="_blank">📅 01:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18792">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وال استریت ژورنال: جنگنده های F35 ارتش آمریکا از بریتانیا به سمت خاورمیانه اعزام شدند
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18792" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18791">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/18791" target="_blank">📅 00:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18790">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزارت امور خارجه ایالات متحده آمریکا یک "هشدار جهانی" صادر کرد و هشدار داد که گروه‌هایی که از ایران حمایت می‌کنند، ممکن است به سایر منافع آمریکا در خارج از کشور یا مکان‌هایی که با ایالات متحده و/یا آمریکایی‌ها در سراسر جهان مرتبط هستند، حمله کنند
@WarRoom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/18790" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18789">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وال‌استریت ژورنال: آمریکا به نقش احتمالی چین یا روسیه در هدف‌گیری‌های ایران مشکوک است
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد که پس از اصابت حملات ایران به چند هدف حساس با دقتی غیرمعمول، احتمال ارائه اطلاعات هدف‌گیری از سوی چین یا روسیه به تهران در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/18789" target="_blank">📅 23:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18788">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک حادثه دریایی دیگر، سومین مورد در امروز، دقایقی پیش در نزدیکی سواحل عمان رخ داد.
@warroom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/18788" target="_blank">📅 23:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18787">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">طبق گزارشات غیر رسمی دقایقی پیش آمریکا پل سورمیچو که ایرانشهر رو به چابهار متصل میکنه هدف قرار داد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/withyashar/18787" target="_blank">📅 23:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18786">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">میگم تا حمله شروع نشده، یه لطفی کنین خستگی منم در بره. چیزی نمونده بشم 1.7M یه هول بدین تو گروه چتا بذارین، به دوستاتونم که ندارن بگین اینستاگراممو فالو کنن. نوتیفیکیشنهای پیجم روشن کنین، استوریا رو هم حتما ببینین.
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/18786" target="_blank">📅 23:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18785">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مقام آمریکایی به NPR : ترامپ دستور داده تا طی ساعات آینده ارتش آمریکا درهای جهنم رو به روی ایران باز کنن.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/withyashar/18785" target="_blank">📅 23:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18784">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وال استریت ژورنال : مقامات آمریکایی می‌گویند ایران در حال شلیک موشک‌هایی است که با سرعت بسیار بالایی حرکت می‌کنند و می‌توانند هنگام نزدیک شدن به زمین مانور دهند
@WarRoom</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/18784" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18783">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : ویدئوی منتسب به پست دونالد ترامپ در اینستاگرام مبنی بر حمله زمینی فیک است و ترامپ از دیروز در اینستاگرام هیچ پست جدیدی قرار نداده.
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/18783" target="_blank">📅 23:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18782">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxiqv6BV2b-VI7F9d-IPsNLq7YIHYHNDyaOpEyD-rocHtjkW1WbP-o_-APy3hPMQKvQxu6jTKS1uVuC9P6hSzjlLUgaZOHorVZXDuXY380jyGmHflZ4KFdv-_qHKsvb8qzn7lmUvVk-o5XxQClZInQSjohyOSk8IC6hoyqg6pCc9MG5wdQWA4-2CeRiHJa_kGuHeKMOEVIr_D3ZT3I4KsCQwhOpToYwveenpEn1cYOt7qVxtgR7RLdgLP2_lsQuEcsrQfcZSUNnGMsyWN3U5KM2NSPjwe34GT6ORaEZRhf0e8JoP6ED8KYlI7-hFKxb__zeH4EkKECnevJUPESsGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از مدتها نمیتونم ببینیم چیزی
🤒
همه رفتن زیر پتو رررپتپتوووو
@WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/18782" target="_blank">📅 22:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18781">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هواپیمای های آمریکایی در منطقه فرستنده های خودشونو خاموش کردن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18781" target="_blank">📅 22:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18780">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شبکه CBC: امشب احتمالاً شاهد فعالیت‌های بیشتر در ایران خواهیم بود، و کشته شدن سربازان در اردن ممکن است چهره اوضاع را تغییر دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/18780" target="_blank">📅 22:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18779">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/18779" target="_blank">📅 22:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18778">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کانال 14 عبری: نشانه‌هایی حاکی از احتمال قریب‌الوقوع از سرگیری جنگ با ایران، از جمله در خاک اسرائیل، وجود دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/18778" target="_blank">📅 22:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18777">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آکسیوس:ایران از خط قرمز ایالات متحده عبور کرده است. این احتمالاً باعث می‌شود رئیس جمهور ترامپ علیه رژیم ایران تشدید شود. کمربندهایتان را ببندید.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/18777" target="_blank">📅 22:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18776">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18776" target="_blank">📅 22:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18775">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبرگزرای CBS به نقل از مقام نظامی: حملات امشب دقایقی دیگر آغاز میشود و گستردگی بیشتری دارد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/18775" target="_blank">📅 22:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18774">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کارشناس صداوسیما: اگر آمریکا اومد جزایر ما رو گرفت، اینم جزو سیاست‌های جنگه، نباید بشینیم گریه کنیم چون دنیا به آخر نرسیده. باید بریم تلاش کنیم تا آزادش کنیم. زمان جنگ با عراق تمام سران کشور زنده بودن ولی خرمشهر سقوط کرد و ۱۸ ماه طول کشید تا آزاد بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/18774" target="_blank">📅 22:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18773">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیت هکست وزیر جنگ ایالات متحده
خداوند به قهرمانان سرعت و توان دهد.
فداکاری آنان تنها عزم و اراده ما را راسخ‌تر می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18773" target="_blank">📅 22:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18772">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بندر عباس ( حکم به نام خدا داره) صدا انفجار گزارش شده
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18772" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18771">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فککک کنممم شروع شد
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18771" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18770">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18770" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجار در سیریک و جاسک تکذیب شد
استانداری هرمزگان:
دقایقی پیش خبری مبنی بر حمله جنگنده‌های آمریکایی به مناطقی در حاشیه شهر سیریک و جاسک منتشر شد که این خبر صحت ندارد و تا این لحظه هیچ گونه انفجار و حمله جنگنده های آمریکایی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18769" target="_blank">📅 22:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18768">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5c312e2f.mp4?token=kSruf4iW8Ewn78FibcQwya-Puc91jGm2iHVxZMFgNDMv5UhuMu6aIwdPOoo2TTQ7yoNabH-VJVc1A9mEA0hDGvl-oGZOfQWceNTFagZC0cJXq8y5AeTfdrYVZ35OjjHjqi2Xo4FB0O3tFcuk5FpjEjF0pbYXh_ol0ySvQrZTN_bbnzcTgw1V0MaWvHBGa86ka9gPl--xdGvs41M2fa2AYzpCC8lfa4bdZQusb8OQjsbI3l0jRSwe2JLJ-RBel22I7bZuBw8yk5wbxK8E_2pLM0rY9-e7mtr9DT72ui5OlNanqtjJF7IfjK-2RfXa1Cvr6YmgTNGZ8pClFgSZBqT5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5c312e2f.mp4?token=kSruf4iW8Ewn78FibcQwya-Puc91jGm2iHVxZMFgNDMv5UhuMu6aIwdPOoo2TTQ7yoNabH-VJVc1A9mEA0hDGvl-oGZOfQWceNTFagZC0cJXq8y5AeTfdrYVZ35OjjHjqi2Xo4FB0O3tFcuk5FpjEjF0pbYXh_ol0ySvQrZTN_bbnzcTgw1V0MaWvHBGa86ka9gPl--xdGvs41M2fa2AYzpCC8lfa4bdZQusb8OQjsbI3l0jRSwe2JLJ-RBel22I7bZuBw8yk5wbxK8E_2pLM0rY9-e7mtr9DT72ui5OlNanqtjJF7IfjK-2RfXa1Cvr6YmgTNGZ8pClFgSZBqT5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
ما از آرژانتین به طرق مختلف حمایت می کنیم، از جمله فردا.
کتمان نمی کنم که به آرژانتین علاقه دارم. من فکر می کنم بیشتر شهروندان اسرائیلی به آرژانتین علاقه دارند.
موفق باشید! واموس آرژانتین!
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18768" target="_blank">📅 21:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18767">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ادعای i24news فرانسه: نهادهای دفاعی اسرائیل در حال آماده‌سازی برای وقوع یک جنگ بسیار جدی در کل منطقه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18767" target="_blank">📅 21:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18766">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هم اکنون ۳ سوخت رسان از اسرائیل بلند شد، احتمال میرود دو تا سه عدد دیگر نیز  بلند شوند. اون یدونه که سلکت کردم داره برمیگرده حساب نکرم @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18766" target="_blank">📅 21:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18765">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvREtKrnagr4VlNmTKOT19mCHd9dT2R3_uyb51RnyVO8lkW00aV96oaEKUSS-bbVUBZr9shsRrO0RMiffRZ7hSY0qXS5f70i5bLO9mC1RHdbITXgOAfCyZ1LhZqtY26AVF0oHKRHPHsYtLH-ihAl_uM16ECmItSE0B4Qm6Q6_Acatq8SgFeTgrNuVgSWEbdAwLp5YYOnbqhhIun8Q-8u97R4dgRQFxMQQ9qtWk8HJqJCOE1MXIOxntYB8cWt2DzgjRiZ5o4x2ZlIk5Fy2RMPy3pX6_FXdw8jc0BKQmswEfF1h6qwy8l7Csn9HBPqliOniSOYI-3z2M19JBRwsP_qcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۳ سوخت رسان از اسرائیل بلند شد، احتمال میرود دو تا سه عدد دیگر نیز  بلند شوند. اون یدونه که سلکت کردم داره برمیگرده حساب نکرم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18765" target="_blank">📅 21:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18764">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">درود بر خانواده تلگرام ما
😍
🙌🏾</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18764" target="_blank">📅 21:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18763">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18763" target="_blank">📅 21:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18762">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صدای انفجار سیریک سمت اسکله که دکل معروف هم آنجاست
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18762" target="_blank">📅 21:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18761">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">صدای انفجار سیریک سمت اسکله که دکل معروف هم آنجاست
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18761" target="_blank">📅 21:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18760">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فاکس نیوز:موشک های ایران مستقیم به نیروهای امریکا در کویت برخورد کرده و حتی جسد پیدا نشده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18760" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18759">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادعای رویترز‌ : خبر کشته های امریکا به کاخ سفید رسیده است و ترامپ بسیار عصبانی است
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18759" target="_blank">📅 21:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18758">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سنتکام : در
۱۷ ژوئیه (۲۶ تیر)
،
دو نیروی نظامی آمریکا
در اردن، در جریان دفاع نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان در برابر
حملات موشک‌های بالستیک و پهپادهای ایران کشته
شدند
. همچنین
یک نیروی نظامی آمریکایی
همچنان
مفقودالاثر
است.
سنتکام اعلام کرد
چهار نظامی آمریکایی
برای دریافت خدمات درمانی به بیمارستان‌هایی در اردن منتقل شدند، اما پس از درمان مرخص شده‌اند. همچنین سایر نیروهایی که دچار جراحات جزئی شده بودند، به مأموریت خود بازگشته‌اند.
سنتکام افزود که
به احترام خانواده‌های جان‌باختگان
، تا
۲۴ ساعت پس از اطلاع‌رسانی رسمی به نزدیکان آن‌ها
، اطلاعات بیشتری از جمله هویت نیروهای کشته‌شده منتشر نخواهد شد.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18758" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18757">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ادعای کانال ۱۳ اسرائیل:
در اسرائیل می‌گویند آمریکا برای گسترش عملیات نظامی در ایران آماده می‌شود: هفته‌ای سرنوشت‌ساز در پیش است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18757" target="_blank">📅 20:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18756">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شبکه i24 گزارش می‌دهد که شبکه‌های تلویزیونی اسرائیل از سوی دفتر نخست‌وزیری مطلع شده‌اند که ممکن است پخش برنامه‌های اضطراری به‌زودی و در هر لحظه آغاز شود.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18756" target="_blank">📅 20:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18755">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18755" target="_blank">📅 20:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18754">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9571048b32.mp4?token=d0B45aHem5JZfuEGRkC9uaq7uvEbexcuq6vWzhymzWaPZzXQFnAiJyXVtadp6qpEQCBp3GdK1R3TLM22Tryue4hufjmRt23DbQL9hPUABN_o-o7AX2ja-SF_uHtBc6E9Q4Z13jImneMW6R3D9LM0pTrk1CrJUJvqJGwVUALOA0478K6ogrbj1HN0HfUu7BxWSXLOWtaeKhErVOipmRRkW-sm-HPphrbQaMKXVhTT4kgGzgsWG1OkOIg49L6MBsl-oNr-2CSUJgFsdRpBvy1AkcfIkB2YUdkk15CWDzFcARH0WQoGnocjl6S2c3mceiwjNb72x7C41WuR6b_s4dF7iUkpbmRuNOplNRYzIPtvVt54a2uDMAj_EBk7yaNQG6KGPOWRA05hANmjigO8PYjPHHS8Alh-znjvDxmwlhV-eFR6biy0v-Yxfv56wZAWF5bKk_tWHs5-K9nOscqM7WKijuEWd7V8PqFj6u1TiPubiJeNbYfd7TkKXUG3P_ePnza5rsiby40sc3RmYcvbf8CI1h3QiuO1v9FxL_bM1bJzMldYM02GJqOV0vbbmNmKna3AJ0A8PxLqhOY_KX5mgyjqd9wXfdL6THvGKexEkonbFDbmPJZ9aBilaVtdfDgkD0Ut49V8449cgQBbt3qg30yCuzEIxvruJb3xlGFduE1KIDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9571048b32.mp4?token=d0B45aHem5JZfuEGRkC9uaq7uvEbexcuq6vWzhymzWaPZzXQFnAiJyXVtadp6qpEQCBp3GdK1R3TLM22Tryue4hufjmRt23DbQL9hPUABN_o-o7AX2ja-SF_uHtBc6E9Q4Z13jImneMW6R3D9LM0pTrk1CrJUJvqJGwVUALOA0478K6ogrbj1HN0HfUu7BxWSXLOWtaeKhErVOipmRRkW-sm-HPphrbQaMKXVhTT4kgGzgsWG1OkOIg49L6MBsl-oNr-2CSUJgFsdRpBvy1AkcfIkB2YUdkk15CWDzFcARH0WQoGnocjl6S2c3mceiwjNb72x7C41WuR6b_s4dF7iUkpbmRuNOplNRYzIPtvVt54a2uDMAj_EBk7yaNQG6KGPOWRA05hANmjigO8PYjPHHS8Alh-znjvDxmwlhV-eFR6biy0v-Yxfv56wZAWF5bKk_tWHs5-K9nOscqM7WKijuEWd7V8PqFj6u1TiPubiJeNbYfd7TkKXUG3P_ePnza5rsiby40sc3RmYcvbf8CI1h3QiuO1v9FxL_bM1bJzMldYM02GJqOV0vbbmNmKna3AJ0A8PxLqhOY_KX5mgyjqd9wXfdL6THvGKexEkonbFDbmPJZ9aBilaVtdfDgkD0Ut49V8449cgQBbt3qg30yCuzEIxvruJb3xlGFduE1KIDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون تأیید کرد که در درگیری‌های هفته جاری، سیزده پرسنل نظامی آمریکایی مجروح شده‌اند؛ این شامل ده سرباز و سه ملوان است که با سه پرواز تخلیه پزشکی از منطقه خارج شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18754" target="_blank">📅 20:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18753">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش پرتاب موشک سیریک و صدای انفجار از تنگه @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18753" target="_blank">📅 20:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18752">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بیانیه جدید ای‌آی : مجتبی خامنه‌ای با اشاره به نقض تفاهم‌نامه از سوی آمریکا، این اقدام را نشانه بی‌اعتباری و بی‌ارزش بودن امضای رئیس‌جمهور آمریکا دانست و تأکید کرد که زورگویی، تمامیت‌خواهی و وحشی‌گری جزء جدایی‌ناپذیر سیاست‌های آمریکاست. وی افزود آمریکا بار دیگر چهره واقعی خود را آشکار کرده و این بدعهدی، سندی دیگر بر غیرقابل اعتماد، دروغگو و پلید بودن این کشور است. او همچنین هشدار داد اگر آمریکا به دنبال جنگ‌افروزی و تحمیل هزینه‌های بیشتر باشد، ملت ایران و جبهه مقاومت درس‌های فراموش‌نشدنی به آن خواهند داد و رشادت رزمندگان و مردم جنوب نمونه‌ای از این توانایی است
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18752" target="_blank">📅 20:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18751">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آخرین آپدیت نقشه جاده‌های مسدود شده‌ در نزدیکی تنگه هرمز @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18751" target="_blank">📅 20:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18750">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرگزاری رژیم: حمله موشکی نشده
آتش‌سوزی در مخزن سوخت است.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18750" target="_blank">📅 19:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18749">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دلار ۱۹۵،۵۰۰
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18749" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18748">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">تو تنگه درگیری ناموسیه لب دریا بودم صدا موشک میومد</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18748" target="_blank">📅 19:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18747">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd827c3ab1.mp4?token=INL5fGNlTfM1pG8HvUHsUm1WUYA4XxwHvx4Okl8CEW0sch_6V_SRdVb7XfxvwpB-NqBqydl1vB0dl0v9miQtCOrPwaIBB83v0o-xTYn3ITa78WGFr_qG4nu1_f5_Zw_ESCbigEahQW1Z8dalK451m6IqHyeCA6ogJOYztA0Q_1_JkBbk3K0TsAoLJSHD0HOM2Md3bMiri8z4lbbQw82l6AezfcdplNd3dRIl3P2yUFgkGz91W_gxTYdysHSkiqead25trfQO5L8h6L3pNl7pQcnUn_trSz9OS602GlJbvSrVPJlwVaOV5NKY6YGVDvjX6YzzljNkKGrXQAodPAVuXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd827c3ab1.mp4?token=INL5fGNlTfM1pG8HvUHsUm1WUYA4XxwHvx4Okl8CEW0sch_6V_SRdVb7XfxvwpB-NqBqydl1vB0dl0v9miQtCOrPwaIBB83v0o-xTYn3ITa78WGFr_qG4nu1_f5_Zw_ESCbigEahQW1Z8dalK451m6IqHyeCA6ogJOYztA0Q_1_JkBbk3K0TsAoLJSHD0HOM2Md3bMiri8z4lbbQw82l6AezfcdplNd3dRIl3P2yUFgkGz91W_gxTYdysHSkiqead25trfQO5L8h6L3pNl7pQcnUn_trSz9OS602GlJbvSrVPJlwVaOV5NKY6YGVDvjX6YzzljNkKGrXQAodPAVuXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه زاهدان هم اکنون
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18747" target="_blank">📅 19:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18746">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2676d61e10.mp4?token=Zt0vS4tp8hW0epbGBiUuAZiXWBEnOcdlsW99UGMkEMe86meSmP09JKLW2Z_VbDJ4jwBrNl4c2wzjxqmjOeJkmaV7rp7pdj-FozaySkiLbbxidve-yyIXOvCMrxSyGu0LmQbkkZC2b-Kj_rokC8ZgTsA6M6vUiy0rhirqVF7rT7owYhB4Umle8TXun4V2Y_-0O313LPgqJTe0l0DVaOZfNr3L5MsWwkNzAWYqmja0kv2eFobnbaLinC5TG7T4lx0rSEqfB14ZYi3EGq0KSgS75euu6KylnvkOSJNpyi7MUrBy-hE6n327vRestbuHVw8j9zlcIOC3SpNsNp8lnoVa1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2676d61e10.mp4?token=Zt0vS4tp8hW0epbGBiUuAZiXWBEnOcdlsW99UGMkEMe86meSmP09JKLW2Z_VbDJ4jwBrNl4c2wzjxqmjOeJkmaV7rp7pdj-FozaySkiLbbxidve-yyIXOvCMrxSyGu0LmQbkkZC2b-Kj_rokC8ZgTsA6M6vUiy0rhirqVF7rT7owYhB4Umle8TXun4V2Y_-0O313LPgqJTe0l0DVaOZfNr3L5MsWwkNzAWYqmja0kv2eFobnbaLinC5TG7T4lx0rSEqfB14ZYi3EGq0KSgS75euu6KylnvkOSJNpyi7MUrBy-hE6n327vRestbuHVw8j9zlcIOC3SpNsNp8lnoVa1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون سپاه زاهدان پودر شد ، حالا یا آمریکا زده یا بی بی آتیش زده
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18746" target="_blank">📅 19:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18745">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش پرتاب موشک سیریک و صدای انفجار از تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18745" target="_blank">📅 19:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18744">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18744" target="_blank">📅 19:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18743">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e92f5909.mp4?token=VB1thFvh3SMP5l5OVADEb-_PHe4iYSbhhurQ7kMRkfJOQb_E2G1nHlUINNleGKe7EdYNxLTXcKFWGWkfQdUjRlR74Vemiq-KPyVuK9q1hU2BQiOPUv7MgOX66HdxnmoJfQiwywGwdE7AD1YPxe_l12pRqwEgQtIdnFOWOqcLfhih7eIGZrh8AMMPqTh-_bjjaRXI5_cRwMfV3XzwPNOSkxI7OmFYAiczWSXisDdQPwgjuM8jPYjs0PSrF73A9iU_4bWTuRDnhe0KF0b8gM5xvNEjL0oM546AyYEheBgRvzInkjjurcbVTcXVjolGPIWAWDJKMHAjUKa9AuS9AuQcGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e92f5909.mp4?token=VB1thFvh3SMP5l5OVADEb-_PHe4iYSbhhurQ7kMRkfJOQb_E2G1nHlUINNleGKe7EdYNxLTXcKFWGWkfQdUjRlR74Vemiq-KPyVuK9q1hU2BQiOPUv7MgOX66HdxnmoJfQiwywGwdE7AD1YPxe_l12pRqwEgQtIdnFOWOqcLfhih7eIGZrh8AMMPqTh-_bjjaRXI5_cRwMfV3XzwPNOSkxI7OmFYAiczWSXisDdQPwgjuM8jPYjs0PSrF73A9iU_4bWTuRDnhe0KF0b8gM5xvNEjL0oM546AyYEheBgRvzInkjjurcbVTcXVjolGPIWAWDJKMHAjUKa9AuS9AuQcGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار ویدئوی بمب‌افکن B-2 در حساب ایکس دن اسکاوینو، گمانه‌زنی‌ها درباره ایران را افزایش داد
دن اسکاوینو، معاون رئیس دفتر کاخ سفید، در حساب کاربری خود در شبکه اجتماعی ایکس ویدئویی از پرواز یک بمب‌افکن رادارگریز B-2 نیروی هوایی آمریکا منتشر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18743" target="_blank">📅 18:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18742">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704c0a3914.mp4?token=uGsIB5_Rk_X2rucdMXPryJ8f3w3KKzdsW5uaj5ZeK-KJyd-TSC7pj0DORnD5rU8YcYv6AKxh48bzitdiuWaHjxiO38mpnE3HgoMMEdMBinrRUQrIm4_HGyYmBMWBlmgRSFpt0igy03Krtyz12Yfv4dbUIXunQruG4Zm4wv48jC83JTaBeogUCPYqPZ24jqB3Fcn2J3AH3fMlBkeL8yUNAbbVG6Z2V9UE1hx6RL7PfMzeO_2FsMtTKn1HVxGW-AlcP7JfmrVZirWo0mk_EQBLsu8op4R4I_SWrDllKqa0qHqZaivyAmWEMs6wg5L8YKOzBdnzJwQaVl3mr_Avkj2t4AY4uV3AjaHmL9sWXEcgltbUY6-aBfRXpZdFgcFX8b8GX-7qNPI9Mk5EofAUjFvS6GEl3B-ULPvB2VzCqn3Ss4kIE_IkVuMIT3MkFGtjz4xi9HdAe8ptNrZFfLouw63n7Lw5H2LXQ-lFJ-B7u1sBIczprheUz7G2LpV-PVNgrae6Sho9mC7JUHVTIB5h59reUr2V4F07Dpjtojaw3p3NBD6EGOj1XHG2UQcV-sKKgYPUrd-5DVpkxtd2_wxh_7k6KgKLq1Obr5fqSnm8A797BqHoHErmEP2ds7yVSrpVXNZcxpGTJnB7fNQb9Q1DVt8SSVnpcfrPg3D-xEwaM08IbjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704c0a3914.mp4?token=uGsIB5_Rk_X2rucdMXPryJ8f3w3KKzdsW5uaj5ZeK-KJyd-TSC7pj0DORnD5rU8YcYv6AKxh48bzitdiuWaHjxiO38mpnE3HgoMMEdMBinrRUQrIm4_HGyYmBMWBlmgRSFpt0igy03Krtyz12Yfv4dbUIXunQruG4Zm4wv48jC83JTaBeogUCPYqPZ24jqB3Fcn2J3AH3fMlBkeL8yUNAbbVG6Z2V9UE1hx6RL7PfMzeO_2FsMtTKn1HVxGW-AlcP7JfmrVZirWo0mk_EQBLsu8op4R4I_SWrDllKqa0qHqZaivyAmWEMs6wg5L8YKOzBdnzJwQaVl3mr_Avkj2t4AY4uV3AjaHmL9sWXEcgltbUY6-aBfRXpZdFgcFX8b8GX-7qNPI9Mk5EofAUjFvS6GEl3B-ULPvB2VzCqn3Ss4kIE_IkVuMIT3MkFGtjz4xi9HdAe8ptNrZFfLouw63n7Lw5H2LXQ-lFJ-B7u1sBIczprheUz7G2LpV-PVNgrae6Sho9mC7JUHVTIB5h59reUr2V4F07Dpjtojaw3p3NBD6EGOj1XHG2UQcV-sKKgYPUrd-5DVpkxtd2_wxh_7k6KgKLq1Obr5fqSnm8A797BqHoHErmEP2ds7yVSrpVXNZcxpGTJnB7fNQb9Q1DVt8SSVnpcfrPg3D-xEwaM08IbjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور یک هواپیمای مسافربری بر فراز انبار در حال سوختن «وایلدبریز» در حومه مسکو
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18742" target="_blank">📅 18:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18741">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تداوم حملات اسراییل به جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18741" target="_blank">📅 17:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18740">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqRPlm4tBkL_zOdUlcBBb5pGRY_mUuKvMsHDpdYXuiWFRM52VRAT_m0bem2-bNdWzAi9MXozrHC-K6_lGEmy3L-xJW-kH4b1rIvNuwlF2d2dWrNVtPsGR5S9AgRU_kOS3-Zg0KYzHb09r0rJctMREhSzRKIUcyeXfC-jKZQjWSGH-Wofu4DK7zsHPkM_uToWA5B7eAnzptT7y3uSN91uOCAFbc6o7ilhaJxM6qw4pb5XtrbGwAzvHaFDufiP5WxcjWbFYebOYJAhuLRlHXrVbH7MdSwTpimT0Fe99zNOuNZTlZCQfeHY_ZaNBrTy18uaM3MSdDvZ4QKSjuXFsLTeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18740" target="_blank">📅 17:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18739">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad58b44d3.mp4?token=kttFLHIB9QhpPiSyDnSiGWQfFVjyo51mTDN7o6ieo9Xof5XOQrrXL5KnwsZW95WHTTw9vZW5dFY2TGf62MPyVDnxTpGd7AJiMjSeuOMSAR_X7oFMGLprMS_UxjVbbMrU-KQcvWMS_ljKi3BeeI4FJrzOOFDmaC7REYBKcSW4-dpHGLZzbSX8FnmsQMgnDEog2w5JsDMsDoG7pvIIx7wZo5vNElRVKeBxaSeslNHS-3EVsNAp7_6pBoPmRHIiIH553lqIb_e5ILEb3vM7RRQ2DHTGXu5YJSLzJKofcDyeiy00NLKb50ip_-dREAEFhLoBUWxuu2ZuWbBpAvZejLJeww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad58b44d3.mp4?token=kttFLHIB9QhpPiSyDnSiGWQfFVjyo51mTDN7o6ieo9Xof5XOQrrXL5KnwsZW95WHTTw9vZW5dFY2TGf62MPyVDnxTpGd7AJiMjSeuOMSAR_X7oFMGLprMS_UxjVbbMrU-KQcvWMS_ljKi3BeeI4FJrzOOFDmaC7REYBKcSW4-dpHGLZzbSX8FnmsQMgnDEog2w5JsDMsDoG7pvIIx7wZo5vNElRVKeBxaSeslNHS-3EVsNAp7_6pBoPmRHIiIH553lqIb_e5ILEb3vM7RRQ2DHTGXu5YJSLzJKofcDyeiy00NLKb50ip_-dREAEFhLoBUWxuu2ZuWbBpAvZejLJeww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سوریه یک کامیون حامل خیار که به سمت مرز لبنان در حال حرکت بود را توقیف کرده است و درون آن چندین قبضه گلوله و موشک ضد زره کورنت پیدا کردن
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/18739" target="_blank">📅 16:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18738">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">در منطقه بندر کویت، صدای چندین انفجار شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18738" target="_blank">📅 15:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18737">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b511507b37.mp4?token=Ag7zz8sbzuz6AX2lWx1NGi8i2lJITPxlcd1XgjawaV1gB_QVjckf2rrHhhtITTyKh2qkTPeQdqtRj_gpqmM0_h9yEcYfA2cOsR23AS1CZHaGCOdjFPObwvqbmn9CQTPL5ObqhkkF-RocbDWUDAmFaxR-9fJW3yvmrluPZ0cwM_KIocPazfc05cdZU0gjqk234l3rkYBIDELFY89I-e-9sZ-cj_ImvGu3kCShPPDS3LlpHubldA669_JMHYRlc_JLSw33qRLuLFIIiPhlivHDpsV5GZDRGZclICPvBpmOCWPCWN2aMs_bm_aT96zjKAT1qNFuVxADhk7Bnf3ZABdA9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b511507b37.mp4?token=Ag7zz8sbzuz6AX2lWx1NGi8i2lJITPxlcd1XgjawaV1gB_QVjckf2rrHhhtITTyKh2qkTPeQdqtRj_gpqmM0_h9yEcYfA2cOsR23AS1CZHaGCOdjFPObwvqbmn9CQTPL5ObqhkkF-RocbDWUDAmFaxR-9fJW3yvmrluPZ0cwM_KIocPazfc05cdZU0gjqk234l3rkYBIDELFY89I-e-9sZ-cj_ImvGu3kCShPPDS3LlpHubldA669_JMHYRlc_JLSw33qRLuLFIIiPhlivHDpsV5GZDRGZclICPvBpmOCWPCWN2aMs_bm_aT96zjKAT1qNFuVxADhk7Bnf3ZABdA9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
🤣</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/18737" target="_blank">📅 15:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18735">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بحرین رو دارن میزنند
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18735" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
