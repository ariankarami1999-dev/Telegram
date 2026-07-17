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
<img src="https://cdn4.telesco.pe/file/dL9sMLxqA4yDGGTsZhOrp9saIv2hCznBtK5sqbXZUHHLYRfW7Sa7-BvTY3nQz_tTNWeN52cYqShsiJjEPTlyXiDt0LLAoeItlT021Q9U5CYHb8E58HbvVcKiCD17jy-XDd0UbXrtTd8StZffNfVq2Y5rivJNvEdPPSEfNACBkhDVF10voTlYota7a-qR3UqpIzfHiTFPaXtxGP8xEckVMDXkhW5A98CqV0cj6_QRHIyovEwHA9VkTgGHjUbARCLMq1BHr4pLaHYgBPFMPP24cOeGnMAQsrOov_pbUxQOlstxQufGyoLGpKQTBxKP1Ovd9XFi3dV-FFrr_2CI0GYDAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 403K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 23:29:19</div>
<hr>

<div class="tg-post" id="msg-18603">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سنتکام اعلام کرد
امروز ساعت ۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET) (۲۲:۳۰ به وقت تهران)
،
هفتمین شب متوالی
حملات خود علیه ایران را آغاز کرده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/withyashar/18603" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18602">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سنتکام : شروع کردیم
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/18602" target="_blank">📅 23:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18601">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b7df7221.mp4?token=p9OGaNHGYZc6_R5IIFd5dpRODe1AHz1KtxEmKhTiFqQlbUtkuTWeWhC2-9gQi23yonqY43dVHNesg0qD_TdaSMb0NjYDoedM5kVW_9rXqbFEgMIskTI_TB_6X06EGxrHXbkX2bL7Zl1XXadmt9aSeKem-UZCK8dgpIwxbBefhqqSLV5isG_e2d-kkdyHJjVp7-wbM9F4h9C-dODT1xml3p_6l6T85FoPuikNMVstF-lg7AChbLZbsrPySfFZHR0aNp3NoHd9bPKKVBM63FQH-j8_2MKyUquaHQwOy0DEPokzGbzq3Wzy6wiK0_6tp3yKdV4Y6iF-kM4T6d5oNmEFoaZNsjxz0ZYOmiysYntoFfdczobR8V5Ey-x-Ked4G-Uk4keR4FRxpnnI11mDviQCa2M7DbUCxIfZvCWihxo16n16cZdgyTHD5AlSEG3v4Fzu7CpXn63KOGadL_EGqDa_v3uNQUIpTc5q9O9DRYWdmfw1PAIc4DhytFOEXCVXp8Rg9tz8D5GCwz_rh0TtZHqX_psenMjrtM0-k1ohq8pwIrGIXp1_3jfzb8kqnaLTf43eb6AXh2DSEC0_BecteZObAuVxcG34y_i6hLeWkVsZKdpZOXGkfvNSKBUfbjxcY3fl06skJvapA9LO8wUN3v2Jmg_sSKttoJrhuT9zTarMHwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b7df7221.mp4?token=p9OGaNHGYZc6_R5IIFd5dpRODe1AHz1KtxEmKhTiFqQlbUtkuTWeWhC2-9gQi23yonqY43dVHNesg0qD_TdaSMb0NjYDoedM5kVW_9rXqbFEgMIskTI_TB_6X06EGxrHXbkX2bL7Zl1XXadmt9aSeKem-UZCK8dgpIwxbBefhqqSLV5isG_e2d-kkdyHJjVp7-wbM9F4h9C-dODT1xml3p_6l6T85FoPuikNMVstF-lg7AChbLZbsrPySfFZHR0aNp3NoHd9bPKKVBM63FQH-j8_2MKyUquaHQwOy0DEPokzGbzq3Wzy6wiK0_6tp3yKdV4Y6iF-kM4T6d5oNmEFoaZNsjxz0ZYOmiysYntoFfdczobR8V5Ey-x-Ked4G-Uk4keR4FRxpnnI11mDviQCa2M7DbUCxIfZvCWihxo16n16cZdgyTHD5AlSEG3v4Fzu7CpXn63KOGadL_EGqDa_v3uNQUIpTc5q9O9DRYWdmfw1PAIc4DhytFOEXCVXp8Rg9tz8D5GCwz_rh0TtZHqX_psenMjrtM0-k1ohq8pwIrGIXp1_3jfzb8kqnaLTf43eb6AXh2DSEC0_BecteZObAuVxcG34y_i6hLeWkVsZKdpZOXGkfvNSKBUfbjxcY3fl06skJvapA9LO8wUN3v2Jmg_sSKttoJrhuT9zTarMHwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش گسترده تحرکات ترابری هوایی نیروی هوایی آمریکا به‌ خاورمیانه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/withyashar/18601" target="_blank">📅 23:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18600">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ارتش کویت: حملهٔ رژیم ایران منجر به هدف قرار گرفتن تعدادی از تاسیسات و اردوگاه‌های متعلق به ارتش کویت با استفاده از پهپادها شد. در نتیجه، تعدادی از پرسنل نیروهای زمینی کویت در حین انجام وظایفشان مجروح شدند.
همچنین، تعدادی از تاسیسات حیاتی و مدنی، از جمله یکی از ایستگاه‌های تولید برق و تصفیه آب، مورد هدف قرار گرفتند. این امر منجر به وقوع آتش‌سوزی و آسیب رساندن به تعدادی از تجهیزات ایستگاه و واحدهای تولید برق شد. علاوه بر این، ترکش‌ها در تعدادی از مناطق کشور پراکنده شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/withyashar/18600" target="_blank">📅 23:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18599">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اگه ویس های چنل رو گوش کرده باشی امروز سوألی نمیکنی
😁</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/withyashar/18599" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18598">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دونالد ترامپ، در دفتر بیضی شکل خود با دارلین گراهام، خواهر لیندسی گراهام که موقتاً جایگزین او شده است، دیدار کرد و از او خواسته است تا در انتخاباتی که در ۱۱ آگوست برگزار می‌شود، به طور دائم در سنا نامزد شود و گفت «امیدوارم این کار را بکند، هیچ کس بهتر از او نخواهد توانست میراث برادر عزیزش را گرامی بدارد. دارلین از خانواده‌ای فوق‌العاده می‌آید و در تمام زندگی‌اش برنده بوده است. اگر او موافقت کند، از حمایت کامل من برخوردار است.»
@WarRoom</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/18598" target="_blank">📅 23:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18597">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وای نت عبری : تاکنون بیش از ۶۰ هواپیمای سوخت‌رسان آمریکایی وارد اسرائیل شده‌اند که ۳۳ فروند از آنها در فرودگاه بن گوریون مستقر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/18597" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18596">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da528eaf.mp4?token=dZWSjIoJl4BkIYA2Oa7GdbFiD1uK4jnacwW_CCnsaPCldrxid3TB2No_-94yCymHe9JiTBX4IpG4eCEqzX0tN-BRQ6esUtxCdYM9r9E2lmRJIeGgfKAefHpEQv_Dotn2OoTYhpJ65uQKEvS1sN9DD3Wid3BnPH9MBJcUY3YgXryrbZYxplcv0Bkxb54tDdUIPISzTak24zXvQ8BSOoSWAAJNT8PBTFswISPy0iHS0nU1TJ1Mdyn9HNV18OzVrXlZ5DR-5x5pCHnuCAtJwsBYepIVxpwd8Ns6H-xBNo0xxc6PWYD6og8noomj1OQSxhkr--bcZRaRNbQ1JcYKH7vxTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da528eaf.mp4?token=dZWSjIoJl4BkIYA2Oa7GdbFiD1uK4jnacwW_CCnsaPCldrxid3TB2No_-94yCymHe9JiTBX4IpG4eCEqzX0tN-BRQ6esUtxCdYM9r9E2lmRJIeGgfKAefHpEQv_Dotn2OoTYhpJ65uQKEvS1sN9DD3Wid3BnPH9MBJcUY3YgXryrbZYxplcv0Bkxb54tDdUIPISzTak24zXvQ8BSOoSWAAJNT8PBTFswISPy0iHS0nU1TJ1Mdyn9HNV18OzVrXlZ5DR-5x5pCHnuCAtJwsBYepIVxpwd8Ns6H-xBNo0xxc6PWYD6og8noomj1OQSxhkr--bcZRaRNbQ1JcYKH7vxTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن کج بند : اگر حملات ایالات متحده در دو تا سه روز آینده ادامه یابد، نیروهای مسلح جمهوری اسلامی از مرحله بازدارندگی و پاسخگویی فراتر رفته و وارد فاز «تهاجم و نابودی کامل» خواهند شد، به طوری که پایگاه‌ها و سربازان ایالات متحده فراتر از مرزهای سیاسی تعقیب و مستقیماً هدف قرار خواهند گرفت.
ایالات متحده باید بداند که استراتژی فرسایشی «جنگ و مذاکره» به بن‌بست رسیده است و در روزهای آینده، شدت حملات ایران افزایش خواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/18596" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18595">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فاکس نیوز : یک گزارش محرمانه که برای ریاست‌جمهوری ایران تهیه شده، نشان می‌دهد تنها ۹ درصد ایرانیان از حفظ وضع موجود حمایت می‌کنند؛ در حالی که نزدیک به سه‌چهارم مردم خواهان اصلاحات عمیق ساختاری یا تغییر کامل نظام سیاسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/18595" target="_blank">📅 22:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18593">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e2f05b5ce.mp4?token=SRPNGrvnYJzD96l-l7Rdnk07cg7WEJPk_Yfc93U4AVOYtiFEeFUoPWDbA5QYenB35wJzK6ejnFCesCzXpYo9QmAfje9eWFRZU7kS9iSUKcs5jlbO1h69mHD6UsasNQK0leUZtY_X944WQqmm4Rw-yoWO6b-FSlEUbBaryyxfip4nxoELkvYtxHDRu0xuNKAR98sd3LxbCcfwxZ0t8lbmXhyTpgUeGF6iywB0PH0a-D6sl36e_ggfXcvWZuTCSALeyFlxya1YmW2QeR2Q-8gZsuZiNnzt2L7zT2p3PN9UmwRaKb0bT_4wpeeFRjrFt3F2TAVPH8bG3tnSVQi--Rc7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e2f05b5ce.mp4?token=SRPNGrvnYJzD96l-l7Rdnk07cg7WEJPk_Yfc93U4AVOYtiFEeFUoPWDbA5QYenB35wJzK6ejnFCesCzXpYo9QmAfje9eWFRZU7kS9iSUKcs5jlbO1h69mHD6UsasNQK0leUZtY_X944WQqmm4Rw-yoWO6b-FSlEUbBaryyxfip4nxoELkvYtxHDRu0xuNKAR98sd3LxbCcfwxZ0t8lbmXhyTpgUeGF6iywB0PH0a-D6sl36e_ggfXcvWZuTCSALeyFlxya1YmW2QeR2Q-8gZsuZiNnzt2L7zT2p3PN9UmwRaKb0bT_4wpeeFRjrFt3F2TAVPH8bG3tnSVQi--Rc7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جهنمی سلیمانی عراق انگار که آتش فشان فوران کرده ! بی شک اگه کرد ها تو پلن نبودن اینجوری نمیکوبید پشت دست خیلی خبره !
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/18593" target="_blank">📅 22:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18592">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چهار سوخترسان از اسرائیل بلند شدند @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18592" target="_blank">📅 22:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18591">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbBWPYjLLwmdeFJ1Txn1mq7S0PSzfBpCMFYFBGJ9sSNZIH9AtfTkvgDBs0tM0LcLU3c4yz4Ba7mIDjfsDsB4ihWVYdbbhImwGANGsMqCc9zDucjzTrq8sHGB7gNQCHNnbz-HB-ntGM6G3aViJaDeR45LkDrQV7V27gsL3_O3HcIDu7RuvkhW6JtYXh9tzAfc6j99yMEGhowF_V2IcZm8BV2ejag6hzg9vwMRGtEa7Ys7AdjEeFEDuDvafAJU84oSnBUMIjO18Qeaoe2ap3yW47J9xrrwi-hD41SqYY-GWWCvKoex8D4APiSgOKbVHoVH0a8ugxy8mnF8bNTKJCF5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار سوخترسان از اسرائیل بلند شدند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18591" target="_blank">📅 22:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18590">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3z35BVT_8b1i2q6bwvT_WLB0oTg6FvKi78nQKuJ5fCsMZE6kxTyxc7AlIVqREEZjtEo09a0NGA88UN9RsHplYAz9f01bUqc-4odU0x9vGawY3btAyZr1c5lDS7KK2KWSCCsTovs9KiCTyfr9cNW3F-yFrTlrF05FsBok6826GDzfk4tx2p5posqbkmCg5U-Rgcch6cfesvxwDOVM22B0NjlhyXWFZ3RNu7E_tuCaqRESzHEFP5GidMCuPXvQmXx18HzrfWhHec9AK-ogbrbTyCSZHfHrb6h0QnKPiYt-ejChRx3PvfblINhO4_g26dlyzQyqSinGxKW2AkTmk1uFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود در سنندج
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18590" target="_blank">📅 22:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18589">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SC6aWuQj8uIxCIfBB0StMYfSgQnbhcrbsoADlMD1SKctTS7JI3mbt9OHFG4mhOFZyVWTzl2MJ7cUqQk-NaMEb7OakEP3JZKxZpQvncJo0q-5PhFKRITLR-wp2aa4KW2a_YwVOqKCxpO6Xj9PJpgVZ780Q4gv4IVE-tsGtxl1Y45cmhTlYSNnPrT42soohU2D40L2l7ucb_MY2hcJdclqplFZ7lwPtXsqby47PWtXAfJKVj7PlEeiv_Cq7Z5k_PlNRfH2Y3P4URD1alfGRC4TwGzQ0f477k0v8GmY40xNsZ_yFbbOeXMPOmrfxjMhm9uFKcq7Fy1jTvgG8689V784sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم سنگین آتش در انبارهای مقرهای گروه‌های کرد مخالف جمهوری اسلامی در اربیل و سلیمانیه عراق ، کل کوه در آتش میسوزد این گروه ها از مدتی پیش به کوه ها پناه آورده بودند و پایگاه ساخته بودند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18589" target="_blank">📅 21:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18588">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18588" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18587">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حقیقت یاب اتاق جنگ
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18587" target="_blank">📅 21:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18586">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش انفجار جدید در بندر عباس و یع صدا هایی‌در ‌بوشهر
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18586" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18585">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبرگزاری تسنیم: هم اکنون حمله موشکی سپاه به یک کشتی تجاری در تنگه هرمز.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18585" target="_blank">📅 21:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18584">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">با حملات پهپادی/موشکی آتش‌سوزی‌هایی شدیدی در پایگاه‌های گروه‌های  کرد مخالف جمهوری اسلامی در شهر سلیمانیه رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18584" target="_blank">📅 21:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18583">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت انفجاری ‌منطقه
🚨
🚨
🚨
🚨
🚨
💥
۴۰۰ هزار نفر در اتاق جنگ با یاشار! سپاس از همراهی و اعتماد شما. این تازه آغاز راه است.
🎉
400,000 members in @WarRoom with Yashar! Thank you for your trust and support. This is just the beginning.</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18583" target="_blank">📅 21:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18582">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‎ وال استریت ژورنال:آمریکا جنگنده‌های خود را از اروپا به خاورمیانه بازمی‌گرداند
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18582" target="_blank">📅 20:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18581">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">۲ انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18581" target="_blank">📅 20:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18580">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش انفجار بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18580" target="_blank">📅 20:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18579">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آکسیوس: مقامات دولتی ترامپ به اسرائیل اطلاع داده‌اند که
ده‌ها فروند هواپیمای تانکر سوخت را به این کشور اعزام خواهند کرد،
این اقدام در آستانه یک گسترش احتمالی عملیات نظامی علیه جمهوری اسلامی ایران صورت می‌گیرد. سه مقام آمریکایی و اسرائیلی این موضوع را تایید کردند."
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18579" target="_blank">📅 19:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsKoFAfa67d_K9ykYfbQQrqg-n_KE8i9038JVLaWpkjtCqq6PqS7gfVrissO0u4nUdspdLYMP0mtz7BvDwNfFr2ABU6UWhapaYB1eiyUMbm4-dEqEspq6m-nHaCmltGdVu6gK5Oo2ZQvSmU1O1lyk5FJWeDPKFhDnQjFk5EQHuRTIpLxQfga9hhV6yR1OGs8-yK3Ww7xCzM_dYkz8HedrFfdQStaxy87_5hTCcJgYljTb33v_2xn438UGIpzAKsKxZgtRV4MbuYJUAmA2i2trBQjPvIQDgAJO8zjlQWBkMH9LZzv9mdqXetz-AmOxcotTi7x2zQGAyEXUt5OvaYsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57565771c4.mp4?token=O0UX4C2dUg5Y_WgN6w8yuyzxiYk--3UEjtFBpd24DDEfhgziQ5C2-88GXmPuIvacJlyJ3OvWyYwhYESzqzptMUw2w0oqFsMb3HOtG55beXZQ1DBqk7lECl0fy-czFRDXJfzZy1WwTlFyCdMUdygifsjz0KUS9LGI0t--7bJPfmQhhJBCVExZpC9QN34mV6i1eEG00V6oq8bmwmRy5Aaa4oLG1YRZcL9Wa55Jha36C2sU4jPP-yZ9mdMo7KbejRchVX3lJxg2Ovp8-elJyNpp-yX9FAdibmQx1E9wqpjNYCFG4s0aBc6aLdmC3J_HyQyKj5ZYqRVqhJNYtYSzzzcYhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57565771c4.mp4?token=O0UX4C2dUg5Y_WgN6w8yuyzxiYk--3UEjtFBpd24DDEfhgziQ5C2-88GXmPuIvacJlyJ3OvWyYwhYESzqzptMUw2w0oqFsMb3HOtG55beXZQ1DBqk7lECl0fy-czFRDXJfzZy1WwTlFyCdMUdygifsjz0KUS9LGI0t--7bJPfmQhhJBCVExZpC9QN34mV6i1eEG00V6oq8bmwmRy5Aaa4oLG1YRZcL9Wa55Jha36C2sU4jPP-yZ9mdMo7KbejRchVX3lJxg2Ovp8-elJyNpp-yX9FAdibmQx1E9wqpjNYCFG4s0aBc6aLdmC3J_HyQyKj5ZYqRVqhJNYtYSzzzcYhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری از حملات امریکا به مرکز توزیع خط ریلی بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18577" target="_blank">📅 19:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بیانیه ارتش : نیروهای ویژه تیپ ۶۵ نوهد با انجام ۱۱ عملیات و ورود به خاک کردستان عراق ۸ نفر از فرماندهان ارشد گروهک های تجزیه طلب رو با موفقیت ترور کردن و ۳ مقر مهم نیروهای تجزیه طلب رو بصورت کامل تخریب کردن
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18576" target="_blank">📅 19:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18575">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdac5e1f0.mp4?token=gbpee8JwsBXPBFKifNV2an2tHHeGvQitKZOmMxhL-BYqzwHIXwTsSwLcPDasE25xFNNQeigeunkynVaUROyLMmUuOYDZ2QJqFZ6ZluF2ufLqOB0BJwh2YU9xi-I8HhQ0aFUjCBhu7WY7gfGW-A9H5Xa4OLBpSDB5d-TIHKVMe5r1yYGscUCD9IXZeZwZP2U_CGK4I8sdNQ8Bio_7waYGqutH_Wkt5DYBGc2ocT5OnqmR-jjmty1t5iKouGn1SNFLqCMKnyY9kisa9K87iaObjGBbS4hMVazT3bJeCb0xhghdbGrvI1lxxpief9K6opURWGSLAextnvXgp8mnj4T68Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdac5e1f0.mp4?token=gbpee8JwsBXPBFKifNV2an2tHHeGvQitKZOmMxhL-BYqzwHIXwTsSwLcPDasE25xFNNQeigeunkynVaUROyLMmUuOYDZ2QJqFZ6ZluF2ufLqOB0BJwh2YU9xi-I8HhQ0aFUjCBhu7WY7gfGW-A9H5Xa4OLBpSDB5d-TIHKVMe5r1yYGscUCD9IXZeZwZP2U_CGK4I8sdNQ8Bio_7waYGqutH_Wkt5DYBGc2ocT5OnqmR-jjmty1t5iKouGn1SNFLqCMKnyY9kisa9K87iaObjGBbS4hMVazT3bJeCb0xhghdbGrvI1lxxpief9K6opURWGSLAextnvXgp8mnj4T68Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در
۱۶ ژوئیه (۲۵ تیر)
، نیروهای آمریکایی با موفقیت
برج دیده‌بانی بندر شهید کلانتری چابهار
را منهدم کردند؛ برجی که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در
دریای عمان
بود و به ادعای آمریکا،
سپاه پاسداران
دهه‌ها از آن برای رصد و هدف قرار دادن کشتی‌های تجاری عبوری از
تنگه هرمز
استفاده می‌کرد.انهدام این برج به‌طور مستقیم توانایی سپاه پاسداران برای هماهنگی حملات علیه خدمه غیرنظامی کشتی‌ها را کاهش می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18575" target="_blank">📅 18:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دقایقی پیش فرمانده نیروی دریایی سپاه به آمریکا هشدار داد:آمریکایی‌ها با هر لحظه که می‌گذرد،به لحظه سرنوشت‌ساز برای عملیات علیه یگان‌های دریایی فرماندهی مرکزی ایالات متحده در آب‌های این منطقه نزدیک‌تر می‌شوند،فقط منتظر بمانید،
ساعت صفر نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18574" target="_blank">📅 18:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e9ed530a7.mp4?token=dbOmx9-PbX-sQlO3uP6YUXrp0UwHEe3hVKZInVPX-Ww819KVX5LszijW3EdtqtHUN49h51fzo4TWFFOzbsBp0r7AFWvYgNg2MDMQeh9KOH45E5u0RtiZhny-rMUIqOB-rQtI0lOVlHXX6u2j8LHfAsnhOvjMDHor-LVRA4H4gHCL87Xhx38BZHnEOUaVf4RyLzPjqTMw5IJL4GsWNWrZl2znbbNE2UfiiFmr7q9rw6y5-4lniEiYVlW-BqJs8bZkT-9vmKgTx5NS2jqBH-6pFAxQMU2Fcth89AcX-EkPYtQzalxL5_gnqEq81abWmc6zUt0FwaYki8GwGoTR_-A5Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e9ed530a7.mp4?token=dbOmx9-PbX-sQlO3uP6YUXrp0UwHEe3hVKZInVPX-Ww819KVX5LszijW3EdtqtHUN49h51fzo4TWFFOzbsBp0r7AFWvYgNg2MDMQeh9KOH45E5u0RtiZhny-rMUIqOB-rQtI0lOVlHXX6u2j8LHfAsnhOvjMDHor-LVRA4H4gHCL87Xhx38BZHnEOUaVf4RyLzPjqTMw5IJL4GsWNWrZl2znbbNE2UfiiFmr7q9rw6y5-4lniEiYVlW-BqJs8bZkT-9vmKgTx5NS2jqBH-6pFAxQMU2Fcth89AcX-EkPYtQzalxL5_gnqEq81abWmc6zUt0FwaYki8GwGoTR_-A5Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرارگاه سپاه در راسک که در اثر حملات آمریکا ترکیده و فقط تابلوش باقی مانده.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18573" target="_blank">📅 18:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سیتنا: با پیگیری‌هایی که انجام دادیم، خبرِ "آمادگی دیتاسنترها برای قطعی اینترنت" که از صبح داره وایرال میشه صحت نداره.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18572" target="_blank">📅 18:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAp12P558Wh4gApltgY6aQ9XnCiqWrBVDTm7ndCkguufwjxPDEzmgU9_2pI__MVnHlpsuRvhmy1hwnb-UCl7FbttJo8hPZw3DCKetLAE5KgOOcv4Cckssfh_Avy3nwQnKhoQOOt-3cdGXK036475Dt1ncRnAF9Ha6dfpA6KUAuQ0m4Wg9-1RYtYuODxxAK900CtrFM5W3HNQ0OfEaDZW7kkShNWU9YKoM1B_FmBXj2L-Lr_Z4XTyFzj3N6i-wxLWW7DA3fr4GvSG_7ByabpDNoqCYZuplQDiUqYg7PCOVcVcIQkBtikBjVli6TuMDXDgjMB6CCjmuD7IVliRTcByog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : «عملیات همچنان ادامه دارد»
یک فرمانده گردان حماس که در نگهداری گروگان‌ها نقش داشته و دست راست مقامات ارشد این سازمان بوده، به هلاکت رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18571" target="_blank">📅 18:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18570">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3z2Fqcu-rcN2djclJI6YCosBLXrykGY0pFsg1I3Sv7e2hQHH8J7MQhNPvuevgEXEjKZf8rUkljIK_AfbFTAdNcaAcHkxkvQ_9XreMmO7NmUi_oSqrSC6I8QlxQjt_NrD6STnF8gvnlRxP_i271hoSk9iqsEA8ZJJq2izIXekLogUB44rpUdJ6ayOfBeEN6u2YWT2WrlgZ137FfbAbOzQsRopTezx0BfT49jzxoqRHNeUxbpvVmVZyqZFTo47zhQL2ThxQTh-qa7HoYWdTaGrOiCjtx8kzHq35KplYh9tVH5SYb3PwP2XKA7TQc8oKVDBpyPVxi5Pp95g4-_fjObXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۶ فروند F35 طی ۲۴ ساعت گذشته از پایگاه هوایی اندرسن در گوام به خاورميانه اعزام شده اند.
@WarRoom
پایگاه هوایی اندرسن (Andersen Air Force Base) یکی از مهم‌ترین پایگاه‌های راهبردی نیروی هوایی آمریکا در اقیانوس آرام است و در جزیره گوام قرار دارد.
گوام (Guam) یک جزیره در غرب اقیانوس آرام و یک قلمرو وابسته به آمریکا است</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18570" target="_blank">📅 17:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حقیقت یاب سنتکام: به‌دنبال گزارش‌های رسانه‌های ایرانی مبنی بر اینکه نیروهای ایرانی به پایگاه التنف در سوریه حمله کرده و نیروهای آمریکایی را اسیر یا کشته‌اند، ستاد فرماندهی مرکزی ایالات متحده (سنتکام) می‌گوید هیچ‌یک از نیروهای آمریکایی در منطقه اخیراً کشته یا اسیر نشده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18569" target="_blank">📅 17:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18568">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بر اساس گزارش خبرگزاری رویترز که از منابع مطلع به دست آمده، پاکستان در حال مذاکره برای یک توافق دفاعی گسترده از کویت است، در ازای همکاری در زمینه انرژی.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18568" target="_blank">📅 17:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قدیمی‌ها یادشونه من اینارو هر روز که کم میشدن قبل جنگ اعلام میکرم
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18567" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18566">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">استوری روز قبل حمله !!!
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18566" target="_blank">📅 17:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18564">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a267a27341.mp4?token=Hr-9yNFWeUtsRvjTmRo8ZOlZ0pfO9BsKmfWzIh-K5tvpPTFWPAO9ySNz7bwsAOsfwUaHAiEzOYiR8VkXAOxI2bR65FybgcuBWPYsCEYU2e2-Z1Yqvenc7_dvW2UW1-t1hKMk3wGdicfiJx6OtsX7y0ZYgQcl1ln2fdGFWiA6VkZxi310seH0jtP8CEB-aqBTFXz3cIFNl1cZxKSMvrKU46SQB1YKR4tZWab-tuxdPLJ0seoDRZ_TcrkwpBbVhbSz8ZgOYTHhaRmC2hmaJxmP0jVYNHhcChaArCnKvim-sTC5pGbMSbg9zLqwac3Ejh0Vusgz26HaznE4BQdemQ1aCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a267a27341.mp4?token=Hr-9yNFWeUtsRvjTmRo8ZOlZ0pfO9BsKmfWzIh-K5tvpPTFWPAO9ySNz7bwsAOsfwUaHAiEzOYiR8VkXAOxI2bR65FybgcuBWPYsCEYU2e2-Z1Yqvenc7_dvW2UW1-t1hKMk3wGdicfiJx6OtsX7y0ZYgQcl1ln2fdGFWiA6VkZxi310seH0jtP8CEB-aqBTFXz3cIFNl1cZxKSMvrKU46SQB1YKR4tZWab-tuxdPLJ0seoDRZ_TcrkwpBbVhbSz8ZgOYTHhaRmC2hmaJxmP0jVYNHhcChaArCnKvim-sTC5pGbMSbg9zLqwac3Ejh0Vusgz26HaznE4BQdemQ1aCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق تصاویر ماهواره‌ای بیش از 20 فروند هواپیمای سوخت رسان آمریکایی حاضر در قطر این کشور را ترک کردند.
چنین اقدام مشابهی در روز های پیش از جنگ نیز مشاهده شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18564" target="_blank">📅 17:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18563">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18563" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18562">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هم اکنون جمهوری اسلامی بازهم به اربیل حمله پهپادی/موشکی کرد ، همچنین شنیده شده چندین انفجار در این منطقه گزارش و تایید شده
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18562" target="_blank">📅 16:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18561">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آی 24 نیوز:ایران از حزب‌الله و سایر گروه‌های متحد در منطقه خواسته است تا در حالت آماده‌باش کامل قرار گیرند،زیرا درگیری‌ها ممکن است در هر لحظه‌ای تمام عیار شوند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18561" target="_blank">📅 16:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18560">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38997170e.mp4?token=rINYAtLkbnkDJwv3AieCWmx3D59kcLDXO2oo9ntuDw-wEBhoY2T5UV7nq9QEXbAkNDY3DYaG1fKdYCBegauTE9xziOobaP4rophezv1dW9etPzO_bBuSz3841JlHt5eO_hpDY6GQIXYoiqhYKxAKMf_hGKrU6DJCaQn3ycP7bnIUrHCGylZHdMoQGiLuL7RmofmQzE5hlnl2rA-Oj6rIACOFGSTZjS3ZH6NKm9SeAHa40oAGEGwYLo8Z7fuBbbAUHRuRvMRr3LPCMh1r2JhkYT6imcd5-iPeHGsY-Qi4Ny2tRsmfd0Q_nFM0sgHiibGsZRwI0HiSvDKzmSAIw0ia2pqQCbqIV4iP9u2lLo69Nn8OIA0TOwLmdGMR7DdIh3G2gMxV8LtOwiWaJbUrpzuRoBLI8nMcFYZJBJqXAlvL0onh6_ew2emp4FMy2l9HVVy9OpuCZxmw08ieLD4cAuXmMd398vMI4g7gfac6F28H1-W9g_sbWGCJ0p_ZT9cOGohG4f1ItI5zI3jgRNbW9tQgkUO7seqxUVMUM5GSmaT1mvcx3ZNmhh614oA5N1to82KoWJqX0RN00NcjE_As_SPRhiuoAQgFR3TAhHvJPoPO2hNDAZc6jpu-odrAfnx8kFLXjdNALy2WXEq8oEh1LAt7Mg8f7egJj7rejESVjVZrb7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38997170e.mp4?token=rINYAtLkbnkDJwv3AieCWmx3D59kcLDXO2oo9ntuDw-wEBhoY2T5UV7nq9QEXbAkNDY3DYaG1fKdYCBegauTE9xziOobaP4rophezv1dW9etPzO_bBuSz3841JlHt5eO_hpDY6GQIXYoiqhYKxAKMf_hGKrU6DJCaQn3ycP7bnIUrHCGylZHdMoQGiLuL7RmofmQzE5hlnl2rA-Oj6rIACOFGSTZjS3ZH6NKm9SeAHa40oAGEGwYLo8Z7fuBbbAUHRuRvMRr3LPCMh1r2JhkYT6imcd5-iPeHGsY-Qi4Ny2tRsmfd0Q_nFM0sgHiibGsZRwI0HiSvDKzmSAIw0ia2pqQCbqIV4iP9u2lLo69Nn8OIA0TOwLmdGMR7DdIh3G2gMxV8LtOwiWaJbUrpzuRoBLI8nMcFYZJBJqXAlvL0onh6_ew2emp4FMy2l9HVVy9OpuCZxmw08ieLD4cAuXmMd398vMI4g7gfac6F28H1-W9g_sbWGCJ0p_ZT9cOGohG4f1ItI5zI3jgRNbW9tQgkUO7seqxUVMUM5GSmaT1mvcx3ZNmhh614oA5N1to82KoWJqX0RN00NcjE_As_SPRhiuoAQgFR3TAhHvJPoPO2hNDAZc6jpu-odrAfnx8kFLXjdNALy2WXEq8oEh1LAt7Mg8f7egJj7rejESVjVZrb7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو شبکه خبر مجری زنگ زده به هتل کرون پلازا عمان و داره جاسوسی می‌کنه ببینه  چی شده
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18560" target="_blank">📅 16:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18559">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رحیم پور ازغندی نماینده خامنه ای اول در شورای انقلاب فرهنگی:
اگر جنگ نباشد اغتشاشات شروع خواهد شد!!!
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18559" target="_blank">📅 16:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18558">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سخنگوی سنتکام، به شبکه تلویزیونی الجزیره گفته است که حملات ایران به کشورهای حوزه خلیج فارس «هیچ تأثیر عملیاتی بر نیروهای ما نداشته است»
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18558" target="_blank">📅 16:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18557">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgovY54a4x0TJeC666iRV9qT6wgnTGEBkwelFlCqm1KkKExLNFV_QbQR4NzYxBaL8r-6P35boQxcJtE9_n14ft5CT0DZpW6QEDxsiHia3zYm40xvXSGjM77xUxn7LhaFdhiCuVc54OKdBYjQMob-M23suVbX4tijGenLi-58OS-J4Ku1u9FKl_m231xSpmBVqbFliDt5qPswJrM_fo1UyUWWZLBem2Fm2JStODTozwlfz3TGjjm2PlJZe9st_Mqp0WKPlLHCr33Mvf6HsSvFtRNCpb9RE_SYYFlJHgS0em8bcfTItVT75On4L2F9hkI-_zq24MRvW_EO5FyByYQ1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :سخنرانی دیشب بازخورد خیلی خوبی داشت
لایحه «نجات آمریکا» رو تصویب کنید، ممنون
@WarRoom
لایحه «نجات آمریکا» ترامپ (One Big Beautiful Bill)
است. این لایحه حدود
۳.۴ تریلیون دلار
اثر مالی دارد و شامل این موارد است:
کاهش مالیات‌ها، افزایش بودجه مرزی و امنیتی، تقویت ارتش، هزینه‌های انرژی، تمدید برخی معافیت‌های مالیاتی ترامپ، افزایش بودجه اجرای قوانین مهاجرتی، و تغییرات در برنامه‌های دولتی مثل Medicaid و کمک‌های اجتماعی</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18557" target="_blank">📅 15:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18556">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18556" target="_blank">📅 15:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18555">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚔️
💥
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18555" target="_blank">📅 15:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18554">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آی‌۲۴نیوز: طی حملات دیشب آمریکا، هفت پل و ایستگاه ریلی قطار در ایران موردهدف قرار گرفتن.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18554" target="_blank">📅 15:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPJ8fBmOHva7fZWCNaKAmwU8P8KxSOGNsSIGtISkBaoZejUGiusMffPnXevBD-gKhlKI6nRzrvdYnLS_x_1Aj2Eq47zX3nF28ebPb3G-tqH4CPDmXPELWZ__vyAjHrkw5dJ4PedVTohUM59d2nyPS_oeZNHFv1NdwRcFgE28rrjFGTtOhmYHP-WZBGog1FERjvdvN74Uv5-dFPBdDIrb61s-NjoSsBrLR08-0MEfpsLtWT1G2Bt_2SYSCq5rG6m_G81QbaRluSIVOKzkXVGrcFhmtjCJqqz-IiyFeF8c_Wu12jXg9RuKdpJx-HjNqPOV-m_q-ra6WmwSit1F_q8Law.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بندرعباس مردم قایق‌هایشان را از اسکله بردند و جلوی در خانه پارک کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18553" target="_blank">📅 15:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18552">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Remix Az Asemoon Dare Miad Ye Daste Hoori ~ Otaghe jang</div>
  <div class="tg-doc-extra">Yashar</div>
</div>
<a href="https://t.me/withyashar/18552" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
@withyashar
📱
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18552" target="_blank">📅 15:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دولت انگلیس بعد از اضافه کردن سپاه به لیست گروه های تروریستی:
از این پس هرکس در انگلیس از سپاه پاسداران حمایت یا با آن همکاری کند، ممکن است به ۱۴ سال زندان محکوم شود!
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18551" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">المیادین: بزرگ‌ترین شرکت گازیِ طرف قرارداد با یک شرکت گازی آمریکایی در عراق هدف قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18550" target="_blank">📅 14:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چند گزارش از صدای انفجار ‌در ‌اهواز
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18549" target="_blank">📅 14:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNiJEZKBvR5ffbnpRG2vwl96dQKGXQPX8UrrwX9iGJiSJHMVosuvHpjdOS0s_WGnjbhKmhnjB-_LDr16M5IvI0YOHo_aYH5dyPdH0Ir4BCbsEK4HOZVKcfW-_aLFvW5G1_Jq01L6sNl8eXgrz1cttvJKaG699bonlAEvw4TGMLkLlv2wbGnfiDgA0xy3lZ8huqgNPkZNV-6RUOC8uxkn1G95GlpWpUpioEdTE2uzCGIkwkaekVQ80GwKv3OXC4Gzyq8ow3MW0FD9_o7Iw-1IHcaPJn7Ruh5P_N_TsOygu5A-tkB3zZ4RfU4LNqC7lmkUIsPJyCxR2mrUW_tE5afbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18548" target="_blank">📅 14:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18547">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c5aeeaa6.mp4?token=bvjP9iajQRLabp0VeckbDtAJ6mBDQZ_9vQqGxhxl3KmUTD9AD_vKX0lROPRKAV2LvVhslV4G9dlPL_MiDf3DoiHJlB5OmZpfcno8HIKFx3kCpQvVL7Io9Rp2RuA_zDS5b4TBl8HW_-IyDS-6ZGaEk_lrvhs4oX3RneF27q0znJfF03hOhp2UVNDizytNtOagb1KVGunujRC0u7TI2XgBPpXK2KIcRA0M3kNSDT4x-Z-Q4HgTYkteTSgc4Fqb6ftFrXpD2YpsddyiymgF_cRakroCkiZOSR3xD_wI8jrt-j_BArm0L_ND2_K7Y12lQQsYYJrmMKSnL0eb1CNzYmVeFQdj9IQqoRGfgnGg1vPf736xOOUS6J8JX9tS66hL7Cb2suZdcOoGxGwQpvUL41cYJVho5jPcIoJzgYJB5k2BqwHLDzzTWVYssCiga1awywCDGaY0uPQPQ2SGe5vv7IJ2umvigqfFbJVtKAOy-8DDzNGVGjUt24pWQAxQbeMhX9lk6YZUDY-f64TruBRO_K9qpFnP4OsLbfkKFTd4OUNKeSxXK3QYk-nqELE5JmnHp_gXNIBGi_wHW74TMqvZxAP0uQQ_ZhWzXUvYvuTSW39cmpnWc5T8mwcC3fWC-gShnJ3oFthInQzzUtPgeVIlh3yhLIhL03nTTmNYZuCMiWbszqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c5aeeaa6.mp4?token=bvjP9iajQRLabp0VeckbDtAJ6mBDQZ_9vQqGxhxl3KmUTD9AD_vKX0lROPRKAV2LvVhslV4G9dlPL_MiDf3DoiHJlB5OmZpfcno8HIKFx3kCpQvVL7Io9Rp2RuA_zDS5b4TBl8HW_-IyDS-6ZGaEk_lrvhs4oX3RneF27q0znJfF03hOhp2UVNDizytNtOagb1KVGunujRC0u7TI2XgBPpXK2KIcRA0M3kNSDT4x-Z-Q4HgTYkteTSgc4Fqb6ftFrXpD2YpsddyiymgF_cRakroCkiZOSR3xD_wI8jrt-j_BArm0L_ND2_K7Y12lQQsYYJrmMKSnL0eb1CNzYmVeFQdj9IQqoRGfgnGg1vPf736xOOUS6J8JX9tS66hL7Cb2suZdcOoGxGwQpvUL41cYJVho5jPcIoJzgYJB5k2BqwHLDzzTWVYssCiga1awywCDGaY0uPQPQ2SGe5vv7IJ2umvigqfFbJVtKAOy-8DDzNGVGjUt24pWQAxQbeMhX9lk6YZUDY-f64TruBRO_K9qpFnP4OsLbfkKFTd4OUNKeSxXK3QYk-nqELE5JmnHp_gXNIBGi_wHW74TMqvZxAP0uQQ_ZhWzXUvYvuTSW39cmpnWc5T8mwcC3fWC-gShnJ3oFthInQzzUtPgeVIlh3yhLIhL03nTTmNYZuCMiWbszqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت انفجاری ‌منطقه
🚨
🚨
🚨
🚨
🚨
💥
۴۰۰ هزار نفر در اتاق جنگ با یاشار!
سپاس از همراهی و اعتماد شما. این تازه آغاز راه است.
🎉
400,000 members in
@WarRoom
with Yashar!
Thank you for your trust and support. This is just the beginning.</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18547" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18546">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کپلر (Kepler) که به تحلیل داده‌های دریایی می‌پردازد: کاهش چشمگیر تردد کشتی‌ها در تنگه هرمز. دیروز، تعداد کشتی‌های عبوری به 8 رسید که کمترین میزان تردد در 3 هفته اخیر است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18546" target="_blank">📅 14:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18545">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هم اکنون یک اسکادران بزرگ از جنگنده‌های F-16 آمریکایی با استفاده از چهار هواپیمای تانکر سوخت، در حال حرکت به سمت خاورمیانه می‌باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18545" target="_blank">📅 14:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18544">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8008a8ae42.mp4?token=AwtrzhQPvCSIA3uCm5reSXG9zuHE7IFXYigrP6r3uQXz572rJNxKdBRYlczCETb7Qce8uPxdLTRxF5tU2oUWOm5zDGhZ2mTUNgv5xrWJnxooNpkEXYoVfqNwLXCPCAPICfBPK3YcZrQpQVAkJ2a4GSxa-L_yE2V6vduK5aUS_y1_uwFKbe3e62S3ZCMcZ6gVGs50dnAF9gsGhzjkGFzteDamAXc_NzN172lGL5XM_puax8YHKXXnXvMrokCUpuOOhDO-UR2sBKbe1rqAJISkWHT8Dw1Dfpx96nqGXEmKuC7vHR9tNvohJ8Jz16-B0T2pSRpKd6J_9kjeL6xtfrSimIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8008a8ae42.mp4?token=AwtrzhQPvCSIA3uCm5reSXG9zuHE7IFXYigrP6r3uQXz572rJNxKdBRYlczCETb7Qce8uPxdLTRxF5tU2oUWOm5zDGhZ2mTUNgv5xrWJnxooNpkEXYoVfqNwLXCPCAPICfBPK3YcZrQpQVAkJ2a4GSxa-L_yE2V6vduK5aUS_y1_uwFKbe3e62S3ZCMcZ6gVGs50dnAF9gsGhzjkGFzteDamAXc_NzN172lGL5XM_puax8YHKXXnXvMrokCUpuOOhDO-UR2sBKbe1rqAJISkWHT8Dw1Dfpx96nqGXEmKuC7vHR9tNvohJ8Jz16-B0T2pSRpKd6J_9kjeL6xtfrSimIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف تانکرها در نزدیکی پلی که بمباران شده است
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18544" target="_blank">📅 14:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18543">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C79NYK6W9Natm7F47m9Qk-Xpcek8nqFjI2K5k6NaOejuPXiv97qMW_BXXwv-OwoNqf_LEs2jh3XHV5NkKafQC_HSFSb5O284WeliKf68ygcmNZNm-61eZTyGO_zAJuV4F1Y1W3M51d7q2eLbTeCizn7jAuXD4p9C3pNgAW_MumC6NJEqHlbLTB4nBM0Kh7W2nwHkdRPNSkT6egUtm_rJ4tIjMG1BLE_vt0ccganqzLD1rTAyarkQnbefXICHTYlXEkVLa2VVtD7Wh5p5Q2I-SbP-quABu-XPYeA6qvcj0RDl6aAc1rjfvaiOB8YVczFGT0-vTElOC4PA9lPSNNXS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتر تا ۱۹۵،۰۰۰ تومان پرواز کرد و هم اکنون ۱۹۲،۰۰۰ معامله میشود
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18543" target="_blank">📅 13:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18542">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315ffdb490.mp4?token=WFEYCQ0Y231IzhUkiCKbPzVoI5-w52zt94KCgXguqecQwi3CfXDJmbj6WxFkaa_S8XM9VpDCl1Fzx6tcEtShcwoDxaYGaerPbC4iIXHP_ykqpz43Ktnav6SQ7HYN-uh4Y5fHVGEhQ22POc39M7DCxz8t9nyrxjdMNI0xqte05MwSMapOrgwaLXMG1ITV5Y-GEEkFlwfmEJ22oXjIIifJhdMBkPPNHIgLPbQ-s_hJDHEGM5lnAXAVRpnDJdsWLgN56awAcDh_xtSG9THMdt5eYu0vQXZr67OvpbeHVu47svRxK5KqI0pN1ByEkggrp4aCzcTYeYFGj54z3iLY6aTbhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315ffdb490.mp4?token=WFEYCQ0Y231IzhUkiCKbPzVoI5-w52zt94KCgXguqecQwi3CfXDJmbj6WxFkaa_S8XM9VpDCl1Fzx6tcEtShcwoDxaYGaerPbC4iIXHP_ykqpz43Ktnav6SQ7HYN-uh4Y5fHVGEhQ22POc39M7DCxz8t9nyrxjdMNI0xqte05MwSMapOrgwaLXMG1ITV5Y-GEEkFlwfmEJ22oXjIIifJhdMBkPPNHIgLPbQ-s_hJDHEGM5lnAXAVRpnDJdsWLgN56awAcDh_xtSG9THMdt5eYu0vQXZr67OvpbeHVu47svRxK5KqI0pN1ByEkggrp4aCzcTYeYFGj54z3iLY6aTbhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل مسیر به گچین و بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18542" target="_blank">📅 13:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18541">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرگزاری CNN: ترامپ در حال دریافت گزینه‌هایی برای گسترش عملیات نظامی آمریکا علیه ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18541" target="_blank">📅 13:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18540">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ونس به NBC نیوز : فکر نکنید کنترل امنیت تنگه هرمز کار آسونیه؛ این کار حسابی دردسر داره، چون با پهپادهای ارزون‌ قیمت خیلی راحت میشه کشتی‌ها رو هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18540" target="_blank">📅 13:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سپاه: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن و مواضع آمریکا در کویت را هدف قرار دادیم
سپاه پاسداران اعلام کرد در
موج ۱۴ عملیات نصر ۲
و در واکنش به حملات پنجشنبه شب آمریکا، با موشک‌های بالستیک و پهپادها جنگنده‌ها و سوخت‌رسان‌های آمریکا در
اردن
را در دو مرحله هدف قرار داده که به ادعای این نهاد،
چند فروند سوخت‌رسان و جنگنده منهدم و تعدادی دیگر به‌شدت آسیب دیده‌اند.
سپاه همچنین در
موج ۱۵ عملیات نصر ۲
مدعی شد علاوه بر
انهدام سکو و موشک‌های هایمارس در کویت
، با حمله موشکی و پهپادی
چندین محل استقرار نیروهای آمریکایی و «ضدانقلاب»
را هدف قرار داده است. این نهاد مشخص نکرده منظور از «ضدانقلاب» چه گروه‌هایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18539" target="_blank">📅 13:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31df15619.mp4?token=A5E8S4G2TcRYsYoLQHmYQ0F72HEENbB_1uV6dU4vYtIBy-2owkpMgv4JEe6Ca1us-3-1KkMWLMZ_vibWPND8yFxaIUnGbVjEciiAOv4vLvgrCr9sgR4xxJZj4iTJZeGBCZxTQTp5Lqx0IMDGkWWKQfLSapTvU96QX-50fnn6Ky8Rj03vNiU8uEDZsDKMV7tQ_T2lPMaFFj-HnBd1YwXQaHeL877okZN9qpoMMlMMP-rwQi6yXmwHZcT0aQXbx6kpb8SyHG0Xe7rv7vB-frGvDN70n9DBLb8LKg0_HkjVT4B-54mOUWiFzOuJ4IwhMPazpICyX9OXCu5-zOd4eyIxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31df15619.mp4?token=A5E8S4G2TcRYsYoLQHmYQ0F72HEENbB_1uV6dU4vYtIBy-2owkpMgv4JEe6Ca1us-3-1KkMWLMZ_vibWPND8yFxaIUnGbVjEciiAOv4vLvgrCr9sgR4xxJZj4iTJZeGBCZxTQTp5Lqx0IMDGkWWKQfLSapTvU96QX-50fnn6Ky8Rj03vNiU8uEDZsDKMV7tQ_T2lPMaFFj-HnBd1YwXQaHeL877okZN9qpoMMlMMP-rwQi6yXmwHZcT0aQXbx6kpb8SyHG0Xe7rv7vB-frGvDN70n9DBLb8LKg0_HkjVT4B-54mOUWiFzOuJ4IwhMPazpICyX9OXCu5-zOd4eyIxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کل وزارت صنعت معدن تجارت این روزا:
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18538" target="_blank">📅 13:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca43767734.mp4?token=ViZKKC3vueqCYvLN2dpV8QAOQlj1qYckH5cRXSJdEaWGWB3_Ye8RSI2osfr8zUMyGfuCRCfrYWXGdTSXWuo9973x37Z-9gvqGrYaI7WwJBCFhTXEvKiBAkO5b49Ns88EZYy4Uw5xNKTyBxHNuUpMMbevH2YfxpgjiPm2BnL2v6RCF60Dx08ev72tW4nhHtFtlLMUdFYWiX3oNJXTNAzmKmsznL0USNDSnrOkSXR0JCa60AtAeokXqIY_I2BdIir5IuX_WXd0pA2k40mo_ddCYdXyENyzKwrMiSUvXZHUnA8lyYV6RLfi88kLAHFtvVXR2XnE6N1KFckbNKlmZz4FYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca43767734.mp4?token=ViZKKC3vueqCYvLN2dpV8QAOQlj1qYckH5cRXSJdEaWGWB3_Ye8RSI2osfr8zUMyGfuCRCfrYWXGdTSXWuo9973x37Z-9gvqGrYaI7WwJBCFhTXEvKiBAkO5b49Ns88EZYy4Uw5xNKTyBxHNuUpMMbevH2YfxpgjiPm2BnL2v6RCF60Dx08ev72tW4nhHtFtlLMUdFYWiX3oNJXTNAzmKmsznL0USNDSnrOkSXR0JCa60AtAeokXqIY_I2BdIir5IuX_WXd0pA2k40mo_ddCYdXyENyzKwrMiSUvXZHUnA8lyYV6RLfi88kLAHFtvVXR2XnE6N1KFckbNKlmZz4FYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه هوایی  عقاب  در جنوب که در زیر کوه ساخته شده و قرار بود از جنگنده‌های نیروی هوایی ایران در مقابل حملات هوایی دشمن محافظت کند با حمله مواجه شده و تونل‌های ورودی و خروجی بسته شده
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18537" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0c4907fb.mp4?token=RrHbvdaqvNvwGf13R2p-hfDruXzOywqdJOHbMoyDoUMfIB-doqHbdk-W8jk1z2_zp9IYa69VMzHKOHxEBuOj5RbRO2XDEy7nl6bH4Qum7p8u-DcdYuU5fV9XhIuJejKcCh9tI0E2cGhV9Du1WsvtKjhXZEFMrbhkP8EDqULzhM0W8UGqXXx55PEIWkSzVQhscbprf9sgzZmDomVobiU48SpG8BN4os2eF-SNgXy3SVvamGTtNWMCc1d2JzwtRTNjG4zBibzXvbNy9ZzOTNg6gYmBTbmrI6qyb0ysxydsxFcegdhYPz-eqMBzEkO4gM6Can6uv0tsXr2IsSmftwkVGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0c4907fb.mp4?token=RrHbvdaqvNvwGf13R2p-hfDruXzOywqdJOHbMoyDoUMfIB-doqHbdk-W8jk1z2_zp9IYa69VMzHKOHxEBuOj5RbRO2XDEy7nl6bH4Qum7p8u-DcdYuU5fV9XhIuJejKcCh9tI0E2cGhV9Du1WsvtKjhXZEFMrbhkP8EDqULzhM0W8UGqXXx55PEIWkSzVQhscbprf9sgzZmDomVobiU48SpG8BN4os2eF-SNgXy3SVvamGTtNWMCc1d2JzwtRTNjG4zBibzXvbNy9ZzOTNg6gYmBTbmrI6qyb0ysxydsxFcegdhYPz-eqMBzEkO4gM6Can6uv0tsXr2IsSmftwkVGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت همین الان پل بندر خمیر که کامل از بین نرفته و خودرو سبک عبور میکند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18536" target="_blank">📅 13:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حوثی‌های یمن به یک کشتی در تنگه باب‌المندب حمله کردند @WarRoom
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18535" target="_blank">📅 12:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ادعای اینتل‌واچ: سناتور لیندسی گراهام توسط سم نوویچوک تماسی
(استنشاق، بلع یا تماس پوستی)
کشته شده است
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18534" target="_blank">📅 12:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کانال ۱۲ اسرائیل : موج بعدی حملات آمریکا قراره خیلی شدیدتر باشه و‌ احتمالا تهران و بقیه شهر هارو هم بزنه.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18533" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حوثی‌های یمن به یک کشتی در تنگه باب‌المندب حمله کردند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18532" target="_blank">📅 12:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18531">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کویت اعلام کرد که یکی از ایستگاه‌های تولید برق و تصفیه آب مورد حمله ایران قرار گرفته است، که این حمله خسارات زیادی به واحدهای تولید برق وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18531" target="_blank">📅 12:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18530">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896d0f778e.mp4?token=X1IBpKNtIbAnoLaV0ooZmLTWeFVZKgfZhig7Ll7s0KT68gaQmORqJebgVWXqIcqlxF376I7pPJFL_Nl0W9_TKbOyjuSCMnvIZmYk1BGc0K9qRcyVSNhPZcR9A4vuFeHZCQyoMv87whb6LIXNc8WJjFtwqTBRU1n6nIi29I5ayHS_KpP8h2B7d3nSkAwCWuC5ojjiRbUOIZj3NbpVKm-aOEYbS6gnYGjEePyoMphZKE94OCzC3cqKEY7Rc6aCfezJfoCrDp-eklRtAeKGWuEUj57ZU6oh9dYe2czbizpFfoF8wfpt-cO66UYG_I6nHwXXFTsYh3RsKvi-_sKQp8nkFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896d0f778e.mp4?token=X1IBpKNtIbAnoLaV0ooZmLTWeFVZKgfZhig7Ll7s0KT68gaQmORqJebgVWXqIcqlxF376I7pPJFL_Nl0W9_TKbOyjuSCMnvIZmYk1BGc0K9qRcyVSNhPZcR9A4vuFeHZCQyoMv87whb6LIXNc8WJjFtwqTBRU1n6nIi29I5ayHS_KpP8h2B7d3nSkAwCWuC5ojjiRbUOIZj3NbpVKm-aOEYbS6gnYGjEePyoMphZKE94OCzC3cqKEY7Rc6aCfezJfoCrDp-eklRtAeKGWuEUj57ZU6oh9dYe2czbizpFfoF8wfpt-cO66UYG_I6nHwXXFTsYh3RsKvi-_sKQp8nkFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون با صدا درآمدن آلارم حمله هوایی در دوحه، پایتخت قطر، پدافند مشغول دفع حملات است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18530" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آلارم حمله موشکی در پایتخت قطر دوحه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18529" target="_blank">📅 12:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e27b43e6c.mp4?token=JCNAJ1-Tyt_gefVuNo-FgZhZnUfojwtj4sovZR8fwQttW9clvxYnGSwF6bb-79WQ9dSNOoP2iRdptUksZy3nnZP1qs1kZczMfGMS8Weky9ZlX3YkEXKF2kGAhykfvPy7QmAJ_PED33EepRaFFvZnK9xT_Joln_LeFTC5TjCwHvMVBxT3iiBXuNIXa_bFQeDmA4I78ldt1B9t3Esy4-ql8IfG9WoMbwvc04saVZPPlhg22k8OqxXMwUrEO3rNuEMKy2k7mHwYyB9-iJ6XwgXbgEhTadOjJ1BUrUArhYjVzn3xdVltFaKICix0R8LaJ1c2jI50a1SGZkutgrZJfcdW_2U-Xo5_Awi7PIaSYJoIxBFyzdb4DWzlgm-mvAHZ9fRQQrzFtCrT-R63Z_5Wu1uMBEvwGuIpa55y9scKMpTKqgBh890bjHWAiPIsQXJapSkyPEFIAiuPAVs2osawPJ5TmQxJGehkM_qMs63WFH2-4E5ZeeczV-7vrpvZWOV8ZmsDLJK876Wxc57jmonveuBjbll_sgP8W33aWOShxqq2T2mkjshmCEu_y_fr194z_xddIMdMwntrOvGjjAOCVErPlqoQh4j7IhF5zVU0jGC3G_6yE6WiVkp1qGku0B1TgNLRvGCwnE6Bzegl3tAgu-vRZcJlLa-YZmRWGt9OW3N-Z8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e27b43e6c.mp4?token=JCNAJ1-Tyt_gefVuNo-FgZhZnUfojwtj4sovZR8fwQttW9clvxYnGSwF6bb-79WQ9dSNOoP2iRdptUksZy3nnZP1qs1kZczMfGMS8Weky9ZlX3YkEXKF2kGAhykfvPy7QmAJ_PED33EepRaFFvZnK9xT_Joln_LeFTC5TjCwHvMVBxT3iiBXuNIXa_bFQeDmA4I78ldt1B9t3Esy4-ql8IfG9WoMbwvc04saVZPPlhg22k8OqxXMwUrEO3rNuEMKy2k7mHwYyB9-iJ6XwgXbgEhTadOjJ1BUrUArhYjVzn3xdVltFaKICix0R8LaJ1c2jI50a1SGZkutgrZJfcdW_2U-Xo5_Awi7PIaSYJoIxBFyzdb4DWzlgm-mvAHZ9fRQQrzFtCrT-R63Z_5Wu1uMBEvwGuIpa55y9scKMpTKqgBh890bjHWAiPIsQXJapSkyPEFIAiuPAVs2osawPJ5TmQxJGehkM_qMs63WFH2-4E5ZeeczV-7vrpvZWOV8ZmsDLJK876Wxc57jmonveuBjbll_sgP8W33aWOShxqq2T2mkjshmCEu_y_fr194z_xddIMdMwntrOvGjjAOCVErPlqoQh4j7IhF5zVU0jGC3G_6yE6WiVkp1qGku0B1TgNLRvGCwnE6Bzegl3tAgu-vRZcJlLa-YZmRWGt9OW3N-Z8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خیلی وطنپرستی ‌نبین حالت بد میشه
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18528" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ورود تانک‌های ارتش اسرائیل در مناطق حداتا و حاریص در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18527" target="_blank">📅 12:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18526">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">علیرضا فغانی داور فینال نشد.
فیفا رسماً اعلام کرد اسلاوکو وینچیچ، داور اسلوونیایی، قضاوت فینال جام جهانی 2026 بین آرژانتین و اسپانیا رو برعهده داره.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18526" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک مسئول در حزب کومله کردستان ایران:
شش موشک به مقر ما شلیک شد، از این تعداد، سه موشک به مکانی اصابت کردند که در آن هشت نفر از نیروهای پیشمرگه کشته شدند، و سه موشک دیگر نیز در نزدیکی همان مکان سقوط کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18525" target="_blank">📅 11:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: هفته آینده خاورمیانه تغییر خواهد کرد و همه باید برای آن آماده باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18524" target="_blank">📅 11:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18523">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال ۱۲ عبری: آمریکا در حال تهیه فهرست تازه‌ای از اهداف در ایران است که تاسیسات تولید و انتقال برق را شامل می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18523" target="_blank">📅 11:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18522">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فیلمه لحظه زدن پدافند کنار نیروگاه اتمی بوشهر @withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18522" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18521">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : ویدئوی منتسب به بندرعباس که راننده ای در حال رانندگی شیشه های ماشینش بر اثر موج انفجار خرد میشود، بسیار قدیمی و مربوط به جنگ چهل روزه و در مکان دیگری است من در میان جنگ پست کرده بودم
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18521" target="_blank">📅 11:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18520">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیروی دفاعی بحرین اعلام کرد امروز چندین حمله موشکی و پهپادی ایران را رهگیری و منهدم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18520" target="_blank">📅 11:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18519">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وال استریت ژورنال: اختلاف میان محافل تصمیم‌گیرنده در ایران گسترش یافت
‏ گروهی به دنبال تشدید تقابل با آمریکا و کنترل تنگه هرمز هستند و گروهی با در نظر گرفتن محاصره دریایی و تشدید جنگ نگران وخامت اقتصادی هستند
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18519" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18518">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سپاه پاسداران صبح جمعه در بیانیه‌ای از «حمله غافلگیرانه» به سوریه خبر داد. در این اطلاعیه هدف حمله منطقه تنف و پایگاه نیروهای آمریکایی عنوان شده
@WarRoom
یاشار : خوب سوریه هم اضافه میشه به حمله کنندگان از امشب</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18518" target="_blank">📅 11:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18517">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxgFacyZxmGUO2flE8FB1JmevIXEYxvoA3tIJlDt_8QG1XmcN2Yw_JyRNMFJkDr9qUTpiwjG7n9IibhFtbhoKwm8WxMxcS7S9GtHIT7XD0zFRmOCckwx0JOYLlnDbnUfkMv8O9hGZNugsauxigCQlT84hM3MkxzFxQXjuFIuAC32XQgU21vz3ZpwVAOe6N42SzP77hAKPyb_hqbI1biAqlPMCjUNdy0p81WfseII9XQDPBHJ6Z_95n1cN_Dt4O1Fi-YGEae4yYxAWFxevbuAKvwjz9SXUG_6Uuzr6HeEnGLNYPvjxPkR6FSCite4N5K8s_znd790zoaGCAidhqZB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵ صبح کل چابهار برج ریخت @WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18517" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18516">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjuZCQA_rXSqff6vEcPeVbCDSibTG6WuiH2FC7JwSf44kilVejncemhp82Vn-qUboRJ3JvhRETIHc4RWYSgC0VsOR8-FfrXBqxAu-Er-aboCSFMMz0BhYjvKfRssl4U4zTZN5yahqUJ0jSseBx9iX0iAdms3pErVMLlCEiCfq0_TYE7FTzsE1H9q_JOouJCl1po8suxT6hPIWAbS7Ma2rHsHU_Z8hOKMn3f2yb5xA7HGhBoUfZEe9ksViPlPo-SOyHDtHBo_2dZSFMgaIYY61XvVGrIQMCY1oOU1NVYjH3_1cdgBF0ypC0OtYCmHg-_dPNsBYXbDED4TVcYo-bvHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی اسرائیل با پهپاد،
یک مسجد در لبنان را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18516" target="_blank">📅 10:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18515">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : دیشب عباس چپقچی هیچ جا نرفت و اون یک هواپیمای معراج چارتر ایران ترکیه معمولی بوده ادمین های بیسواد دنده دادن
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18515" target="_blank">📅 10:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18514">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKa27mbgpiVBziYVXDizNd1-1NLUzfad8IlFbYsty708IfQBF5krcvBpic6tmZ5VHebhGMKQ3okOrJuoDCkjMoV4SgwFdTj9PtZ8Hv9Y2_GH6HihYT0hd563CnuiBSYNFrX_M-cFhWCgC3XQRfJErVK9lpuIkeWx8LfuxZVDzNDiDy07K2923K7snWD2NjZDh9zUCFSNrWgDvaD0w62WrAkQSOo-MR9Uz2Q7DSalx2T34oaMUbbFgMbqJJTEjCU4ZLcGvnNMjV82AbUUg_XNnloZ47OOCYUTG8slaw7_vnnhf4W3P-DFdSN3eM55_HmWOSdGywMuhlhrbevJMBGM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی قدیمی از جی‌دی ونس، معاون رئیس‌جمهور آمریکا، با تی‌شرتی دارای نماد اتحاد جماهیر شوروی در شبکه‌های اجتماعی خبرساز شده است.
وب‌سایت راستی‌آزمایی Snopes تأیید کرده که عکس واقعی است، اما توضیح داده این تصویر مربوط به یک مهمانی هالووین است و ونس در آن لباس شخصیت کشتی‌کج نیکلای ولوکوف را پوشیده بود؛ کشتی‌گیری که با نمادهای شوروی شناخته می‌شد
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18514" target="_blank">📅 10:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18513">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حمله به یک نفتکش در نزدیکی سواحل عمان
سازمان عملیات تجاری دریایی بریتانیا اعلام کرد یک فروند نفتکش در شرق خصب در نزدیکی سواحل عمان با پرتابه‌ای ناشناخته مورد حمله قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18513" target="_blank">📅 10:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18512">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رسانه هی رژیم
: پالایشگاه‌های نفت و پایگاه‌های نظامی آمریکا در بحرین مورد حملۀ مستقیم پهپادی قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18512" target="_blank">📅 09:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18511">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fd2e417b.mp4?token=g82K_lhix1lkmqyK-khz2XG2wqoBREIdgXH6NsnziEH-OFR5L2GWWMAIG3oFRxeuateBLocAsOaR9YS0rK5xgqWNifYwd5raaOIPNBBPDN9uOhsldW9xBULf_gEDQRXu4OKyeA1oWGXNSAWYAtugiZmVkHddVK0HmqF31voz-aDDUwBEGvY2tFJ3CtBX4eFmajhyE5IlpA-Z5Twzu0XL6SabbYHSejdNini4RJA5XJGCN-kwgi95uCsbfYfInAgkYa0osJ_ISe0gUeURIOVNtXwskSExxnnlaRMtpmLVhMljN4EneK_f1GZZ7kQ2LysUtdqbw5MH-5XNQP5F5oFlEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fd2e417b.mp4?token=g82K_lhix1lkmqyK-khz2XG2wqoBREIdgXH6NsnziEH-OFR5L2GWWMAIG3oFRxeuateBLocAsOaR9YS0rK5xgqWNifYwd5raaOIPNBBPDN9uOhsldW9xBULf_gEDQRXu4OKyeA1oWGXNSAWYAtugiZmVkHddVK0HmqF31voz-aDDUwBEGvY2tFJ3CtBX4eFmajhyE5IlpA-Z5Twzu0XL6SabbYHSejdNini4RJA5XJGCN-kwgi95uCsbfYfInAgkYa0osJ_ISe0gUeURIOVNtXwskSExxnnlaRMtpmLVhMljN4EneK_f1GZZ7kQ2LysUtdqbw5MH-5XNQP5F5oFlEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد MQ-9 در آسمان چابهار.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18511" target="_blank">📅 07:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18510">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18510" target="_blank">📅 07:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18509">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12de77f1cb.mp4?token=ur01nqo4r2n3MpOSithznwwbH-q3BAFZxzIrsQYgmpJInDf2VCs0Q1XKfhd2zxPpcwxxB0Eynm9k6CuKbBQJBCr8xJ4l_u2C5avXpFY9zWX2bS3W0u8ProdMf8xIMhbfDLRksXfnh0Wq_Ih0mWgmpMUAGft5QA_EaWT9AxfmN6vPCbGtirSPu6YZAdoNtmZaKVmtYrW5AVkj4YhjUASawkT6qqcoK1tIcwuG6Ctpdn0uHz63bZag6vIBoLCf-XuXGsgAisJxePquWUjO5xaLwSi897GwGMJdDccMBoc4syBBn6_MBV4VSQMr3uP7Gzbfkpc1G7ox8Y0230Zu5aF0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12de77f1cb.mp4?token=ur01nqo4r2n3MpOSithznwwbH-q3BAFZxzIrsQYgmpJInDf2VCs0Q1XKfhd2zxPpcwxxB0Eynm9k6CuKbBQJBCr8xJ4l_u2C5avXpFY9zWX2bS3W0u8ProdMf8xIMhbfDLRksXfnh0Wq_Ih0mWgmpMUAGft5QA_EaWT9AxfmN6vPCbGtirSPu6YZAdoNtmZaKVmtYrW5AVkj4YhjUASawkT6qqcoK1tIcwuG6Ctpdn0uHz63bZag6vIBoLCf-XuXGsgAisJxePquWUjO5xaLwSi897GwGMJdDccMBoc4syBBn6_MBV4VSQMr3uP7Gzbfkpc1G7ox8Y0230Zu5aF0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشکاز لار ، جنوب شرقی فارس
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18509" target="_blank">📅 07:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18508">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766440ca91.mp4?token=A3iFmRcHEY_0P5K_C07JTZ3TC58Uxw0spiqCywkvdvLgW-q6BdKBcYvaMLQsV70UemXSis4O_45JM7RR6Lwyp_a4OI1oDC38EDVkmyCTK2l1FhSQ08QW4D_OW0Rjv-jD5cXeGwTzAGQdZv17rzUUNNVIw9xy4QdCXNi549uapsAwuuk7uvvemgTB0Fi1UoUEA-mg6WQEEpMOByCenQDGufqHiBDwaOKUR5ewEXwF5xhPPy2woKcrIj_9eJlbFZpUb98PchVNrJosOkG1-vXawJTiZqruaDC1kAQMKxrLJA_NxOfmnWCCqbLvPDIt0zcv0CxNH4u5_vFS3M8sD4FYdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766440ca91.mp4?token=A3iFmRcHEY_0P5K_C07JTZ3TC58Uxw0spiqCywkvdvLgW-q6BdKBcYvaMLQsV70UemXSis4O_45JM7RR6Lwyp_a4OI1oDC38EDVkmyCTK2l1FhSQ08QW4D_OW0Rjv-jD5cXeGwTzAGQdZv17rzUUNNVIw9xy4QdCXNi549uapsAwuuk7uvvemgTB0Fi1UoUEA-mg6WQEEpMOByCenQDGufqHiBDwaOKUR5ewEXwF5xhPPy2woKcrIj_9eJlbFZpUb98PchVNrJosOkG1-vXawJTiZqruaDC1kAQMKxrLJA_NxOfmnWCCqbLvPDIt0zcv0CxNH4u5_vFS3M8sD4FYdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18508" target="_blank">📅 07:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18507">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزارت کشور قطر اعلام کرد که در پی حمله ایران به این کشور در بامداد جمعه، کودکی بر اثر اصابت ترکش‌های سقوط‌ کرده مجروح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18507" target="_blank">📅 07:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18506">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881e02f1c1.mp4?token=kBZ5ccJjju9Pcw1GEFvySa4XdnDgYXddjg1Cf6aOTWsbRobSs0-P9dSb7d8fMJIeXCSSvjPJOYI7cZ8zTgGnyYNgeIrUQ9FoMPZHyhxa9IYamqXRqIh3rRWlkvi_gZ9UQH0b4AuWSha7A3rY-pNm2b19j80Bz8wotM6jrU5tdIZkFF__b-suMDhYKSYszg8e--Zrj7ALaqzS0A0Hr1csWCcM0JZ7ULmVRwktld10Y9XENs5DRLYIhkKsQLjtiTEP4s7DqjquhbmnBlzComWDs1qaDA6AHAL-Fe46yh_Fihyg0lz4abz2HczvMh0vBV6AkG1B1vtShMPcsEnaXK-m1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881e02f1c1.mp4?token=kBZ5ccJjju9Pcw1GEFvySa4XdnDgYXddjg1Cf6aOTWsbRobSs0-P9dSb7d8fMJIeXCSSvjPJOYI7cZ8zTgGnyYNgeIrUQ9FoMPZHyhxa9IYamqXRqIh3rRWlkvi_gZ9UQH0b4AuWSha7A3rY-pNm2b19j80Bz8wotM6jrU5tdIZkFF__b-suMDhYKSYszg8e--Zrj7ALaqzS0A0Hr1csWCcM0JZ7ULmVRwktld10Y9XENs5DRLYIhkKsQLjtiTEP4s7DqjquhbmnBlzComWDs1qaDA6AHAL-Fe46yh_Fihyg0lz4abz2HczvMh0vBV6AkG1B1vtShMPcsEnaXK-m1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون موج جدید حملات خصمانه سپاه پرتاب موشک از پاوه کرمانشاه
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18506" target="_blank">📅 07:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18505">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxidWFdbfJ1rQZllvyF-KATC12kH-vwuOxpAwtZQQtilTeZIe0KK1vfA3bSFLbRTUJBzMZTPq1Rv51OXe86_uxZpPpSwR2lDROLfyTxXCHLnx1yEtdv6YeqfgF1jH-J1I6aJwuX-Zm6ikJPJaRa3wn_lyYD1kSTakTjyP8zku9XVeVrG1k085Kdu4zOyNrbJpHcg2IbGpbrDW9jAmPkKHI00kGWk8lGyCdIm_yMkuNX8zXPoA-AtmBcwXItjRlisDJhd-q7Hy7ZSTj4_ybGEIzxiJ0Q1CqMU5DyFm19wkwAZNZh_Byau83NiNiOF0LSKfMTPQjDS39NDokGfH62gSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان چیزی از برج چابهار باقی نمونده
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18505" target="_blank">📅 07:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18504">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS1yOfC4QlKGNMyQAuGyUwG9oCVk_l5hJYTBM4DNyapEJiTo5yWipcHxEG8ceS8dcehLXhpVBjpo2_fDdIRhaSgYz-UrWet1dHS_sKUTbzQnnr49gYwlLonWI8qW_fZH50Ei6sT_v9s-fk4B6t16Ebjx8GyZELZIk3RZQOMrSobsoGGdGpzOY5xkgOaUiOK6DNgHTiNBNpW67_j0lqlLP_l6jiMv91tzZpdnV8AWNjRuVUu_xxZHeKqwcpwbgUu_X7tp-nxKrIhBW3M3eKBUOnC7J_6dKbn3IgZsh1xXtjNuq2gJPTij0VJ5rqlMxcQ_6EAvgpq9JWIjezHsZtqhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵ صبح کل چابهار برج ریخت
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18504" target="_blank">📅 07:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18503">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCfLjbp0Tvnq5dE1qhdMoUKL5KjcnT5I_SjyjkNyRlFtXaehNwgW-PZUk2Gg15eHopAY23iefuEmT3efzGMj3djLlFOUG7WBVvMPQEQ8FEe2bhjxabW0E0HFjxpmWavkblR_QU1MLS5y9Ev-HNkOVoF_1m5b-YJhyHOfw3q1kYhOiv5eyJpOfS7_WNFckLNFgxcgiRM9_DFSQR5eYtd-bOmz6g50zlDayPMEdXdUGjyBlMleuYyAyMixKiAB0HJbYWBCOZpJgz6_lqXRkShgumgOSUF6__v3k2_cd83K_JliXlTY-OcJ8xE7QO4jcLv4VStB8Fnxn0lEnDwvMY0x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از استان هرمزگان شهرستان بستک شهر کوهیج همین الان
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18503" target="_blank">📅 06:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18502">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe0dc5a19f.mp4?token=P9WA-iXiVzP6Ho4TAU97Npl4EU7bb9q2FiMzLNDgl-6Nkmv1l0PiJjq3ezOGq5KAoX_o-vmytlDlIU58t2SRgCy2Weki-j-IlHN9hcnGDlgH_mCRCCNFjd7YIeUehZD5sEleIz9av3nrWwRyqAfe2Dqw2rxipQ7tTBrDhglWopaEFhnDtnB4_FwT6X3ZQOZN-A86R_yUf5NwOaCqPASBZO_89HU3L3UXqPT90bKMcaxEqg6rEJ_Gzs0aU1ivondNWRUDu9d7S0D9FRAvzM6fugjjLmWk7B0SQnXU9ZXKxw0P_7a7vygk1eeYev44-ltMiDvSuldiakkGoXa1naXS64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe0dc5a19f.mp4?token=P9WA-iXiVzP6Ho4TAU97Npl4EU7bb9q2FiMzLNDgl-6Nkmv1l0PiJjq3ezOGq5KAoX_o-vmytlDlIU58t2SRgCy2Weki-j-IlHN9hcnGDlgH_mCRCCNFjd7YIeUehZD5sEleIz9av3nrWwRyqAfe2Dqw2rxipQ7tTBrDhglWopaEFhnDtnB4_FwT6X3ZQOZN-A86R_yUf5NwOaCqPASBZO_89HU3L3UXqPT90bKMcaxEqg6rEJ_Gzs0aU1ivondNWRUDu9d7S0D9FRAvzM6fugjjLmWk7B0SQnXU9ZXKxw0P_7a7vygk1eeYev44-ltMiDvSuldiakkGoXa1naXS64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: ششمین شب متوالی حملات گسترده آمریکا علیه ایران به پایان رسید
سنتکام اعلام کرد
امروز ساعت ۹:۴۰ شب به وقت شرق آمریکا (ET) (۰۵:۱۰ بامداد روز بعد به وقت تهران)
، تازه‌ترین موج گسترده حملات آمریکا علیه ایران به پایان رسید.
به گفته سنتکام، نیروهای آمریکایی با استفاده از
جنگنده‌ها، پهپادها و ناوهای جنگی
و با به‌کارگیری
مهمات هدایت‌شونده دقیق
، ده‌ها هدف نظامی ایران از جمله
سامانه‌های دیده‌بانی ساحلی و پدافند هوایی، زیرساخت‌های لجستیکی نظامی و توانمندی‌های دریایی
را هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18502" target="_blank">📅 06:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18501">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نیوز CBS : اگر ایران نتونه پاسخ قاطع به پل‌های تخریب شده بده٫ حملات بعدی امریکا به زیرساخت حیاتی‌تر ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18501" target="_blank">📅 06:39 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
