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
<img src="https://cdn4.telesco.pe/file/hPcx50AwDt5oNyv-C_yvlUfVjEgdqDRbv_QrwAAkl-mneZLe9IP0LG2O38v7EDn1w7TLvERJcewgzIAztRBXGIUEw0SkNN_zKHE9T6nLSD4UYEXRNJvk22yBrEIqzTdxaYKVt8GVghqnph7Na9fAyZ40luWZdggqdHtNXblQExWQdEe7k8zQlJQ-JCHCtByiDxwxcqOe65wWCMzs2-7rM5ce9AEtrkadXi7On-XvPzanoaoWX3mAZWZTxvY_FnWbSTTFtgOcoyzhuJhQ9XGWdiryG4HGnGPYX7MEqE_tcz1bFGwlag5Le3L01kxZ5urtmEnRTfg7NmTSdvQiF_EV0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 190K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 00:30:37</div>
<hr>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=qg3NzoZhJdF6arKEgIEIaC5RMkDQqq5q3i_ezhMWk6qWudeMUburY3ngPOyzNwPW3bXujWQ7PtlY7Ze-TYgpRhgH4XkPb8yJXgoPDZlJjlKFr9UlyQYGosGiZQ6jduSDoL8yHJ7tPA9fK1jEybakeK7dJ7nkrd5AGS18ShmiaTGcBde3s-E9P-o1w5SoctJxkMbp5YXazXg6MdCJNs0bgLwf9pxaSriyOTQnFMVIGrmMP1PgT2joAVx1lSHSKzVaXO6ej2tVNH6LpDFsHw3VnkT5JjUbPVg4zclpqDG0PPOPBJe5ll_uNiJAfkaWms7R7ryuNb0tZPKCtkv8ihhMYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=qg3NzoZhJdF6arKEgIEIaC5RMkDQqq5q3i_ezhMWk6qWudeMUburY3ngPOyzNwPW3bXujWQ7PtlY7Ze-TYgpRhgH4XkPb8yJXgoPDZlJjlKFr9UlyQYGosGiZQ6jduSDoL8yHJ7tPA9fK1jEybakeK7dJ7nkrd5AGS18ShmiaTGcBde3s-E9P-o1w5SoctJxkMbp5YXazXg6MdCJNs0bgLwf9pxaSriyOTQnFMVIGrmMP1PgT2joAVx1lSHSKzVaXO6ej2tVNH6LpDFsHw3VnkT5JjUbPVg4zclpqDG0PPOPBJe5ll_uNiJAfkaWms7R7ryuNb0tZPKCtkv8ihhMYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1yZxVZAVjFUCJzLHkGpUOPYrOUgi0v1GF5HL4d3EgAMglV4yLhTZGMG1Z4bFSje8Nt0gmjvzgK4G1HBnSkBhBjYefodJjJxSuIAlNcJ7sLtYGrbXGLWIlEh2N3IbUSGJRJMY_ABqszaTtyJK_K9rzhbVYfh6ws3KYb6l3a60U8-AebvXWxCVGoxGBmXcCwx65QQY99a6GCMjNFPjBTCLY74_dwiA3-E6U93uQF7AgY1taeqfrWUTW0xBg8Gx_-ohouDLC2mF4mBzpFq4_-NtjK2XD2hbgSEr0Q3--2dmrwOoABWU05RDWhBy-2DFuSUmXBnz7dttq9aTg1M4RfO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ63as7Tp4L4Kyiy5_A4wbvqQhlHHia2GdLokuamDQCiV8uyoUTTf92zJXIiuPK4kVEkl3E55dzln8A4iWTio3eZW5jFQnUj6cdfHELhknehROcBuuFW0rQP9d_MQFRfWwvcuH-6ZU57T0RpReMg7vA0VsUmoMt71vb14yLWoKbvS9Ds3M700Pze0Vk8E670fdB6oLdkTtwiEy-qdxTGxOP9JFcueDautwuaJeZ7DRBEPjMEDGZguaRDOTYeY17UE8pZoO5mCNRBF0JE3YJPjm7vpoeEstvvwrawYwZ6u75E8ho6YfAPpA2A7fH-Pe5K24PAsv_Upsu7VVYHDzslww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCILebHerj1h59p4R76BI7xSKvhl1nhH8UIK5tOeC0LuTED18SQj7xiRNFO2__7YUO3PpEZW7x8_uiiwCJ-NYVYsjOPrXEY0rpBbNpwbT0nfMfRnlPEYPzuAUscASwUv0e8RjqQh3OkASF0NG02VWqVAtl1_SXgFTHbeCo26NI9svf7-db927vLk4bDYdaXQexz_V5QwCb8DHg5HWHbHFoarvIJOKvxOkMOzTUk3hCxLsFnGNxAUv8vD2pwjgSnmQVQFg54EZrt46_ZLKMKCnGkU680oZBetWbWUQYAc3SgyGEnzve4S3oMXpSL1R9MPCVDof2PRrGGfbwu_wVy5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWxWawQ0Ovw-PxGSuTXEwf_9VMSjV9VgNi-rTZlayTGr_IbY0zedIMUGvW3rOHxPqCqC4Jsp62JH7D4MgMYl4WsAwagpydzUDNX-RsajCfecl1PZ272p1EqiYRIRfRijSL-xk_FCd2vfl6fY0lPWe98OHMUs3bYDEMq3L9PYzjNFGpfgSQm9dJFmJ0QMfrYRJ8tPDfeCCen-lbne90ekXlRH05IQo2u4plZj6edwbrk3mXx_Qqb_VVXi_gKVi6Cpgf6JHKfwez4eUYbpvn-4r7zIVyR11JtMqeqYLVaz1Up7bjmhUaIrvQPYVzOBAvwiff3EayZyU6Kw4UjlGJ6Beg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=QaW-g3NV4rfxIHm1Z53lTy6Bjaa20cz2Jo4688_pQaWKagGvxtUF-E40iHQjDVz8-sxOUMht7V4yKlXpK2couGWut1ARxBFBO05fNGOupcLHK4zak1X6MKl4OLQEF9Ji7lC2bOmSCaGMyfcSYAP1qplVLychcQrRK_beiFIngX_rI0CUV8Wdp-CnWhVRISKlYzfigB8soNIcbafcewZd9M3ue4rgINLI-qyZOW7f8jmBUuc8ag0RjQiwCNHJkORQtxFD4vhjjjtJov50eInw5dWfxsJf9b9vGRxHmB4X9T-upmmA06yyBm7kZuopUPXE1xWP0GeESt6hxctCK4cfqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=QaW-g3NV4rfxIHm1Z53lTy6Bjaa20cz2Jo4688_pQaWKagGvxtUF-E40iHQjDVz8-sxOUMht7V4yKlXpK2couGWut1ARxBFBO05fNGOupcLHK4zak1X6MKl4OLQEF9Ji7lC2bOmSCaGMyfcSYAP1qplVLychcQrRK_beiFIngX_rI0CUV8Wdp-CnWhVRISKlYzfigB8soNIcbafcewZd9M3ue4rgINLI-qyZOW7f8jmBUuc8ag0RjQiwCNHJkORQtxFD4vhjjjtJov50eInw5dWfxsJf9b9vGRxHmB4X9T-upmmA06yyBm7kZuopUPXE1xWP0GeESt6hxctCK4cfqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=WMLwk3xuAiKftyyox8gQELvCoIxdxd9bBQU_GZa4LP8ACcwi24waUoGiwQsg6pfyE9jMMRNlneFy26sO0Pem8iIMhgDoCKpByUf17bZgLHrO1g1YZZ1a1z59fSEZ1g9g9nT5LpkZmjrhntU-arebO5G0nSfHGo7YgbPQliO78Cmsn6Y-NbBCsXaFubs2fcpPqSFf2s1RNjH_TtngCmHGADOxsU-EyO9i1dSqSo9Cr62b6vwmbZnkY_xoIyO3DXivvuNCVJYyipytbaLA-7toLy0sSBJvR6EfzxbarnOIImtyxVwkCC4o1DCMCuRQMwukkk8bO_VPuG-CZ4uOzkjx5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=WMLwk3xuAiKftyyox8gQELvCoIxdxd9bBQU_GZa4LP8ACcwi24waUoGiwQsg6pfyE9jMMRNlneFy26sO0Pem8iIMhgDoCKpByUf17bZgLHrO1g1YZZ1a1z59fSEZ1g9g9nT5LpkZmjrhntU-arebO5G0nSfHGo7YgbPQliO78Cmsn6Y-NbBCsXaFubs2fcpPqSFf2s1RNjH_TtngCmHGADOxsU-EyO9i1dSqSo9Cr62b6vwmbZnkY_xoIyO3DXivvuNCVJYyipytbaLA-7toLy0sSBJvR6EfzxbarnOIImtyxVwkCC4o1DCMCuRQMwukkk8bO_VPuG-CZ4uOzkjx5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=elWau506QFEJAiT0SPJbEXFGNZsywnVeJAnptdFuUBPEW216XY4fHXAq6insvDwdlGhjs2breFjmhyNYqLEE9uvvWP12d63WLezsNgwfMjPvTltZ1pEDX-qnCvL2wJJ9iQrwrefaqagXxuxtZ-enAS2ixXH505F3ZMsxJMd2dfIt5KFs0QL32jM3mdVHSgD9yYnZ0ku8phFQfzZEgEt6wrenecKLR1QJmnK6elVCaIZvFraq9YS_Sm5lLJLr92ZLvcuZabKptyZBzbFQBbRW-yZXCbH8lj3IecCL-hbybw_6KweGwvT8_8XZzjcOFHwTdE8K2DCHqIvj5TdpOeHINg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=elWau506QFEJAiT0SPJbEXFGNZsywnVeJAnptdFuUBPEW216XY4fHXAq6insvDwdlGhjs2breFjmhyNYqLEE9uvvWP12d63WLezsNgwfMjPvTltZ1pEDX-qnCvL2wJJ9iQrwrefaqagXxuxtZ-enAS2ixXH505F3ZMsxJMd2dfIt5KFs0QL32jM3mdVHSgD9yYnZ0ku8phFQfzZEgEt6wrenecKLR1QJmnK6elVCaIZvFraq9YS_Sm5lLJLr92ZLvcuZabKptyZBzbFQBbRW-yZXCbH8lj3IecCL-hbybw_6KweGwvT8_8XZzjcOFHwTdE8K2DCHqIvj5TdpOeHINg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6wBP70QzIv4-hqBWP2UihMLtHDHPTa6s2n8xelomfrKH89OIFfP2YEpQ0dEBGw4eBdA4yoyevz8FZjzhrc5gmY997qQYmKobRqM99mm5dNY0OuC6UIZHgHgsI5-amg5Np-a0QsvCg_uAqDpH4JzUYi1WRFhVBDs47CD8qS_q3WL7cJAIr3ngO_spgtLF00C0R5Mjvf0NNNhGnPS6zuJ8tGmUlrVinbFso4XNmFwev_353bcpKOk8HXk0-ZYRBZgFIesVM77gkwbRDo-TIcv-LHMZPLuJxw0N9NyZKjMubSZfGkty8T24DG22boi9Mi3R6RQftxSFwGwfjIq2i6BWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnRlNF7r0qmvGefJ0jcj1MBTUoGeWIOst4p45g017v5dvorNe5ylcsJqJycJMxJp_Mu33f_3XPMNE5x4C7lr1Ug_6awXsg_CXcheYw3zd6BjlyOrtwjzyqmkKPwOMdxeNcUX68YTu1LDnW14iwi103rB-aB1FAO5GO451V7T7VoNbrKqVsC6iLN7ucdJtp9LDzLUVp0zN3Hfeugl9TomTBNOJ5kGZWkmkSxvivIR5-OUJdzGpl57TaDDM7B7gTjqlKn5Bk_PC1XbBbHAa3oW0fmqwopl8oCrWEp03zC5a98XksMi2wb2vIVBV3jgN2Iv8161i0jbX4879hov9YB0ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=uMRjdrB8tWYqCumsoWpo2UOk6LRWjKIK3agtU62AzI-5XFtOjgA-rig0SEF7BYJQlAutItrg1EZ68MyFOy64fE798Yh7NKaW4okKXEIzMGQkrqqJjHRhtC7G3Cnhi7irdRu17xk_4CHSL8MDpgn2fUDRDYUOHAsvRRr4XuDvbldr81dv8icUQtx0yzDMoyORWr5w3uWZ1r1FXMx0eL4Ud4OBfssyyrUcKvdnmYlMeLy8_ARDwcq_SF0l2gUFRY0gv3sMKZ7fPPg1ARCsNTt3h6kzQYCI19kp-FcfC7CLhh-JSY1isWVmZCMuugO-FSvcr7a2l0y0xbQS2BfKta1zLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=uMRjdrB8tWYqCumsoWpo2UOk6LRWjKIK3agtU62AzI-5XFtOjgA-rig0SEF7BYJQlAutItrg1EZ68MyFOy64fE798Yh7NKaW4okKXEIzMGQkrqqJjHRhtC7G3Cnhi7irdRu17xk_4CHSL8MDpgn2fUDRDYUOHAsvRRr4XuDvbldr81dv8icUQtx0yzDMoyORWr5w3uWZ1r1FXMx0eL4Ud4OBfssyyrUcKvdnmYlMeLy8_ARDwcq_SF0l2gUFRY0gv3sMKZ7fPPg1ARCsNTt3h6kzQYCI19kp-FcfC7CLhh-JSY1isWVmZCMuugO-FSvcr7a2l0y0xbQS2BfKta1zLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=S6t6xI7g7cI1-AjYfsUypYZ2ws2vc9YLZGLt7m23LhT3zWK7zxmpi4a5jLCoPuyrvU_Nb3ukFOidUDwrrmvN4f6jou2NJqyx8zJoxjTwy6LDESNa9JGf6A9phrrv-Q0EPASJ2R0_qWuM4_Ah3-0BMnI20gO0o4Dw6tkEtOrpPB162oOX_ihEFAu7PCwz35buE3HbXLwyBPmgLQScI18t5K0TzoAX_LDDdEqYO3l-YtYUylCr8bAeeOgzesQT9H0c6tmtf4HUAooR5tzVDnbw9dLGvsNzOhc1Re_5mpgIU204aWv52Lsqma0RZ9pNHzgfibl3jMoPaMUESxeQVNofrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=S6t6xI7g7cI1-AjYfsUypYZ2ws2vc9YLZGLt7m23LhT3zWK7zxmpi4a5jLCoPuyrvU_Nb3ukFOidUDwrrmvN4f6jou2NJqyx8zJoxjTwy6LDESNa9JGf6A9phrrv-Q0EPASJ2R0_qWuM4_Ah3-0BMnI20gO0o4Dw6tkEtOrpPB162oOX_ihEFAu7PCwz35buE3HbXLwyBPmgLQScI18t5K0TzoAX_LDDdEqYO3l-YtYUylCr8bAeeOgzesQT9H0c6tmtf4HUAooR5tzVDnbw9dLGvsNzOhc1Re_5mpgIU204aWv52Lsqma0RZ9pNHzgfibl3jMoPaMUESxeQVNofrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0FvGELUSCcSJpteQp36i9AOuDjVNmRyCsk-h5t1bGAJdqjsZH2uct_oWr5QuSPvwG8VUWXMloMpAbaGUChzW7ujZauxRDVJObKOqhF2fzd1gbsyYzhQuGw4Etu7zqP6p0XL8ZJKgNZv61fKsdZsdp9_3xvnkrNdBYafAFLbC05znSuPgK8sanJlvhuhC8lIdlfYV_ehssjG_VrCuc1f_OqkwhTkowW7KunxdbJFNzqW0LtosYVc_TN64l1Pm6m0EO8lgVrcxAn5BUlgE6D73UQd9AgUBeQHwmH-BeuHsuG7phG8AK7p5E9G0eIxq6K2tArKz59abPXUze0-oZ9NoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6MaP9C3EbDBi-Kz7LQD-Qh3JWuf6aT1qhnubtJ4fuY7FX7vhl8REdU6xLs4Zm1T6-tkIeuGraq7TjIJrDVJ6jpvJAhInS2wxMYG_qdUmOgM3AQ3lKQMcIZ4c0rHT-SUHAhmwl5yVQDyZOdXsiTKrnEeJEAfJkyCMCPPsiJ7SKc9v6mmXtxegVN_YR7iJ49XpAVjlhe8xhVPxAjah1eQIH1E62R0upm75OG2uNsriaPgTcmhE0BtSuUC-wNFzVsffZV7Zu6PMp6HNw0_eGDbxyJYvioO62nWPXUSKfBdKNiK8xdI1az6iRATgdEFN3LbFExNx0-e7bHzIkTX2hwMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfwlwwGnjTkXWKGeIteqBJUS7dhUG3PwEFFR5NJSrE16Gz_jyiZRwCamHdIpQ1S5YZmiCnlY7NCE-bIxEi_Ex2FacGP1zbL-HEdXLxpgjJFX5OjJPwhEvPph-Drijfc3fOwglcybeVnmpSm787Y_7HLXRziA5EuPeUzO-0iAvfkZindE5_dQ9GpwOHAElws9f_xiSme387_mQFZprsJNcblG4cGnLC0TnKmfzRe2jnzYiZuwFRoqGl72eu0F4GK2xAYu3wBArKU_1ksbYk1YQuv5K5HuaxwoLUDpmBt0UhKN7sap552bMJ0Jotk_vd4gr5vrnP6PRqMQ3WSmFqldgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=hruGgHfNi21826GJqG_7lfAQX2bDWjjg3mijMbo_6M9Qtaph7Mo5iN1EzaPzFUgI6oLkJbXhogqhsRBMI_UI-thswvzUx14v6BQQ92pC65zs0z3Xpj-xtwu12tDdpCGgbW3lITMY2HrhvOY33GPoxwRMEKvnCYQDSOT6pJrLmmNk1qo_dc8md3d9u2VM6n8pV5h0NA5x3wPcJ4z9oj6LOz_QuengRfcyYKqQHv8AbBhvOSUc7bFbBXcOEtHLhSTVPuNj6mnpsAXrVHWKzeRzamRT2GN7dZ1h6kkMjBX7ZtM-JRrxtJV3STKyUGA8lHmxVm-wqn4kEdUAokf19rUXnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=hruGgHfNi21826GJqG_7lfAQX2bDWjjg3mijMbo_6M9Qtaph7Mo5iN1EzaPzFUgI6oLkJbXhogqhsRBMI_UI-thswvzUx14v6BQQ92pC65zs0z3Xpj-xtwu12tDdpCGgbW3lITMY2HrhvOY33GPoxwRMEKvnCYQDSOT6pJrLmmNk1qo_dc8md3d9u2VM6n8pV5h0NA5x3wPcJ4z9oj6LOz_QuengRfcyYKqQHv8AbBhvOSUc7bFbBXcOEtHLhSTVPuNj6mnpsAXrVHWKzeRzamRT2GN7dZ1h6kkMjBX7ZtM-JRrxtJV3STKyUGA8lHmxVm-wqn4kEdUAokf19rUXnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=ebfY1-fVlvBUJ-UdG7uHN4836BQ9fnYX3H1JVhoJ7LO0MApO9yH5SNlRpsxqxY5WczLsTxx8FonPr5_Sb_fo7A3SsTDJJCfge5sIKqSNlizT-d9ySSpuKmpZWdJ3W5qClXxcqQi3si6jNtoRWCFRY7_P23Ee_hrPA0yNVG_dt23iEgnpGJKYKhMgPU2js6JW_dpMdpTmVwjCKyo-ZEw2FIEhtqtNMrtDWwd99MuoeadvtpwGq3i9Wd0VJ0uCE7eds-6j3BipvJF_RL64_VMHvpkFd9hYhJyhK4FOCs7mxYDni06bUfEHbC06Aiqt9SOSJ3rIgEjrQ-p5FHC65O2z0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=ebfY1-fVlvBUJ-UdG7uHN4836BQ9fnYX3H1JVhoJ7LO0MApO9yH5SNlRpsxqxY5WczLsTxx8FonPr5_Sb_fo7A3SsTDJJCfge5sIKqSNlizT-d9ySSpuKmpZWdJ3W5qClXxcqQi3si6jNtoRWCFRY7_P23Ee_hrPA0yNVG_dt23iEgnpGJKYKhMgPU2js6JW_dpMdpTmVwjCKyo-ZEw2FIEhtqtNMrtDWwd99MuoeadvtpwGq3i9Wd0VJ0uCE7eds-6j3BipvJF_RL64_VMHvpkFd9hYhJyhK4FOCs7mxYDni06bUfEHbC06Aiqt9SOSJ3rIgEjrQ-p5FHC65O2z0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=pm5OdhEPXlLAJIP_SROsOUExmhTyGbVM43hX0s-pC9UkO3RkmukgxvuETvJQOadouNel-ZmCtMOxaPpd7NF7s3ZT2m-N5nQ8qkHgLyZ1bMTQw70j_BImBL-gq1GaJM4Qu_TLnvKlDvkoK-thVfdxAHz9y7y_qsBM_fkUCqS4fiXg7IAAllfY2XveTZv4Vekle2VPIiVbx1sezouvw4d46aQXEE9IYkeDNman0rE4UdOAVWefa0hxZzWwTlhHV90FfLndL8fNHzWaIeFKFT-yVHDvdPCr3LnXVlKDfKhOTXQp2lWFPBK-dJ03YJvvM0-R9yl3FA3pKAbad3k76-vi2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=pm5OdhEPXlLAJIP_SROsOUExmhTyGbVM43hX0s-pC9UkO3RkmukgxvuETvJQOadouNel-ZmCtMOxaPpd7NF7s3ZT2m-N5nQ8qkHgLyZ1bMTQw70j_BImBL-gq1GaJM4Qu_TLnvKlDvkoK-thVfdxAHz9y7y_qsBM_fkUCqS4fiXg7IAAllfY2XveTZv4Vekle2VPIiVbx1sezouvw4d46aQXEE9IYkeDNman0rE4UdOAVWefa0hxZzWwTlhHV90FfLndL8fNHzWaIeFKFT-yVHDvdPCr3LnXVlKDfKhOTXQp2lWFPBK-dJ03YJvvM0-R9yl3FA3pKAbad3k76-vi2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=VVRsWDSlynjkgqZunBUASryPuAXGk769j76e2xeyJ57oJY9pW4PuG2U8zZkK9-eD1OAu4iTPcAtXGWpXI_cOeeXgdEQFkqqL8B_5FfcRplY82r2ewSJwMGVz_2GZtKjHLAStEc_mOaqd1ln80_jaqdqg7lDMK8Q0L_8EgIeERL0DswOko95xMtpWPxZYuk3mAMGFZmdpcYWa-qAOWmSGK1i9c6SPzKlqcTPl4skexxU4yuwccSFHmo8BjQNzHmw09toUCm5u4fyZKaCHTQCLHhfWya1hr8fFTZy3CZpT9fyWR9R9pJnyAq-uSOyKpdROalqEj7NYoiHbSuAEe6kBZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=VVRsWDSlynjkgqZunBUASryPuAXGk769j76e2xeyJ57oJY9pW4PuG2U8zZkK9-eD1OAu4iTPcAtXGWpXI_cOeeXgdEQFkqqL8B_5FfcRplY82r2ewSJwMGVz_2GZtKjHLAStEc_mOaqd1ln80_jaqdqg7lDMK8Q0L_8EgIeERL0DswOko95xMtpWPxZYuk3mAMGFZmdpcYWa-qAOWmSGK1i9c6SPzKlqcTPl4skexxU4yuwccSFHmo8BjQNzHmw09toUCm5u4fyZKaCHTQCLHhfWya1hr8fFTZy3CZpT9fyWR9R9pJnyAq-uSOyKpdROalqEj7NYoiHbSuAEe6kBZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoqrDylknoqgwuXng53uqVywTupVrkX4rezIsgEv6GCfkTdf4lQ0tCTqgSjW7Bh3OQRi7CKUg-JDJqCf0v_cl0sArwFU_N3fyqPmja-jHJ9PPXNyy0defPcfv0L_TQ2oglpS5XVfasSLipf4Rs2JgSYeO63rhEN7hub7UjMQo3nTJZstGFiwPWvEVTuiSugQm7r7O1wa9m-Je_p4S9fxuREfA0qkojaJjaPyzK2df9yl0RfiZ1NnkVtuQUfbT1RCwR1EDcfnR-xKI8xnUSHjsgCD6V13gH1vwMujjCHhNegPDd8rX0OP95kLgLtql4UT8ZffV78234PdUhYONuoaEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=SyEWDvdmilCoaPinHAJm1EbWvfU8_MQPtGM8Nkm2ZWujg4mGIyCJA9h2e2192k4b7RfG8kTU40YVhyO8cFZWN-STxVAGDZcinNfN1fsDW22PaSTQFUfbeCBhvxIQG2Nw9CG5bZyzpRnoZ06FWxeLFa8NlHqfbCzXYqUtJLfR0GA0yZtzcmTVyQOr65d-gOXOEgRyOtWv4bcl4iSaXpWfpefs9zlCkUjlICyRcI84eRPzXSwdSm885ljT0XYBvJFNQDzQpD0wXYx9ZmnvBQGqQHeY4vMNIr_GpioN7zh9RY9bAVU77DqpGaCALBdQ63BsqdUm8sMRpjMkpedGGgEo5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=SyEWDvdmilCoaPinHAJm1EbWvfU8_MQPtGM8Nkm2ZWujg4mGIyCJA9h2e2192k4b7RfG8kTU40YVhyO8cFZWN-STxVAGDZcinNfN1fsDW22PaSTQFUfbeCBhvxIQG2Nw9CG5bZyzpRnoZ06FWxeLFa8NlHqfbCzXYqUtJLfR0GA0yZtzcmTVyQOr65d-gOXOEgRyOtWv4bcl4iSaXpWfpefs9zlCkUjlICyRcI84eRPzXSwdSm885ljT0XYBvJFNQDzQpD0wXYx9ZmnvBQGqQHeY4vMNIr_GpioN7zh9RY9bAVU77DqpGaCALBdQ63BsqdUm8sMRpjMkpedGGgEo5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uciI9tsZBanF9Po7VOEhKamA9jzLg37DIO7c1tU4_yX2u9fdqTawCCfR8qfxbjJ2227Y3OhpQr6dWygxbQASERfb254HEIylgL7edCjd-CuC58gpDczMje8cdE5KvtnrIOt5nQj5UjgKmLTTxwntmWwcGtpVyCeVQBRJMy0W6SizIY4ieIV0_ukvrcRj-UY7kz1Vs-hrItH0DL3Gn4o-_Pjx21WQLQ5Mi9FfEO223CDIC5GusXKpq1fAs1pf9GOQrL3qFyiSgLtlDloPTDAH0NVd2FLDsxPbv5hVtvdrr7QEVgQKVPjVbgN-ftCrgy8cxwCU10TSImZG5YxWpwMvew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ho330k5G5HSuH01NScybqB8By2iNy4LM60FRYCsqdq_jtVNGcjCsglDLxrzsH8o26GWzqj6WPbhZeHNWKr6dG8_CZUxl0wssrbrUp7oSOXRvO3HkOleA25YR5Usyt9YfZWZJQfDK-w5ECWo-Uaaps64yMASUGrlicdMg5TAM-BuBNsMFdXoW9XxP6gXWWErJhscsTMzpvKG2EUOnXLTBDThX8N7RcSae0n6u1xFZTbdPG_P9lioL3vy1y1SS3blUR35FIHs3l23DDM8M9HAskawgIjywDF6COQD_e4695cdrDGcbZ8h9hY_uLGRifiZYwllF4ZTugfoSYPGWDmaLhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGaRL_adVe-1QXj5eVCVLr9_l61TdrqnButor7sXty32NIah8Zg_Aj24G6dp832OyJV-Z0B7crgRRxWQQflf6OJKij-2HR7TlKQavVZz4J7x5JGQ1UDJkR9BueVlBcbYxXrGBJTfM-PnM5VqD4358-MCH7u8fjNM0LQ9lXJdfPAL4oEFB5yirB7ededo79HUS6RyTg-qRjhPip5po4nEICOat1ssc1bp5u-eEbgCca7rfrzjNVGH34W5-kSplNFXzcu57zO5HpFcCdFFlqjv0hJogPBqWiGaBCloBjXeic_T3nrBSciPXSPtBdw9VNf3q_zUjGbYKX_Kz-ISp7wE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G32uu39DLnRtve8hpYVNZfxuK1aIQg2U8SluHSArBGJhJd52p4KYYK6s-UdhW_67H8R1uX09HnQXPefuoxfLQn62GownwWWhXYxhOXnarsLrBNUhQtznZ8lESjhcEKFcwhBZl7xe6ruErMxYKhFUuOuQs1KmuTd9_QB4d721hq6smghUjzfH991ZXDm9Y4WJQLUzJbQDerJ4-vDYXiT7natEWOhfNN8ukSmARhekLLvxB0yutwbqF49QVGdIgqg9mptj7n1oea2lVZHJyikZ9eY66iaocHsOs8NPEDbpCME6c3qsme3E0Q14bUADLhV158UGcDevKThjOdnjB-XfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=jSDmIzHWZM_wKS0SMEWfg3todHNN8JWZSvcVQ8wlLuYDqnVntKWFDGcaSUwXWFunzZZjmWESOOudZVwGeFSXQA6PKWVOZBsGSU3zVfSHvE34vYmLPMds3i5bPojY56qcbogD2pyOFFVpQgV6ZfSIG1CcsHH_ec4yKZrgqWw9xWn0rvKV6wds2xSU4WjVIyNd1Qda2NOE2vuNDqy5flTlGvi6CoRUrCi0yYVLCDU9miDfAXcQ8GukKXKKZ8tEimmjwmYu-C3jG4H6ufB1RmPg9_Wz1E7GZVh8WiXhNra6U1Rv8YFqwhH7c4vCg5-4aH9MjV06e2ZhtlSv8-rJCODHeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=jSDmIzHWZM_wKS0SMEWfg3todHNN8JWZSvcVQ8wlLuYDqnVntKWFDGcaSUwXWFunzZZjmWESOOudZVwGeFSXQA6PKWVOZBsGSU3zVfSHvE34vYmLPMds3i5bPojY56qcbogD2pyOFFVpQgV6ZfSIG1CcsHH_ec4yKZrgqWw9xWn0rvKV6wds2xSU4WjVIyNd1Qda2NOE2vuNDqy5flTlGvi6CoRUrCi0yYVLCDU9miDfAXcQ8GukKXKKZ8tEimmjwmYu-C3jG4H6ufB1RmPg9_Wz1E7GZVh8WiXhNra6U1Rv8YFqwhH7c4vCg5-4aH9MjV06e2ZhtlSv8-rJCODHeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=evih5HOLJU7VWW7sQ_-7cUzcjiDsPu50pxybei5rnBfpqLvz2PsJumwWWwzRjkCD72nXFRT5JqSYtsGp_Jsq6kJb6_MFd-qeA7PzYOmILH49PLQaD4il0te67LGINc5cdHB_6I5ESxcTD3lWQFMfmYi1ivayuVxwGGDbmbhQDqRTTQJVLkH29KhYzS5UwWpks8zLmA1Oy6JzkWZ-59h2XtVTwbpsWyhNQCBZsPzt9fYM6KYPDvygSbXzrhcSAOUbPXU1kyIbBgtnUk8uM7IUX1U8kgfKYfXgUUcVUBbJoCg6pFPYLZkavTfNnh234fUVSWdTPnaaP9v7tR32PZnAHoiOuJy5mXPw5EWmIjW9kon2WGu2vz5Dc0ASWmuarOdzwrVAQAwio5lpXNKALuuh30GSPsv1NUKvb-RI62BnrTCKxblroKddxahz3n05r5v8tzeWrCMVmUMol2fO7IoSxL1ZNepp1uPQKtXy-uSYDxom87Tp02UfFZgowwCfaCyVttslmLRItrodxIwPXorvlB_Sv3gPl6H2nyvind4SWntyJGUOJta9NOttV9U9vZQS8OWbK-ji4nRv69XU6gFwqBTAvKhXijjfhn-Q2aezjHmPOe7-AErdBv3nAv3FS4l2m4kCD9865I0aK9AEaQc8kYwrPnknY3u4Gp5nWL4f5PU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=evih5HOLJU7VWW7sQ_-7cUzcjiDsPu50pxybei5rnBfpqLvz2PsJumwWWwzRjkCD72nXFRT5JqSYtsGp_Jsq6kJb6_MFd-qeA7PzYOmILH49PLQaD4il0te67LGINc5cdHB_6I5ESxcTD3lWQFMfmYi1ivayuVxwGGDbmbhQDqRTTQJVLkH29KhYzS5UwWpks8zLmA1Oy6JzkWZ-59h2XtVTwbpsWyhNQCBZsPzt9fYM6KYPDvygSbXzrhcSAOUbPXU1kyIbBgtnUk8uM7IUX1U8kgfKYfXgUUcVUBbJoCg6pFPYLZkavTfNnh234fUVSWdTPnaaP9v7tR32PZnAHoiOuJy5mXPw5EWmIjW9kon2WGu2vz5Dc0ASWmuarOdzwrVAQAwio5lpXNKALuuh30GSPsv1NUKvb-RI62BnrTCKxblroKddxahz3n05r5v8tzeWrCMVmUMol2fO7IoSxL1ZNepp1uPQKtXy-uSYDxom87Tp02UfFZgowwCfaCyVttslmLRItrodxIwPXorvlB_Sv3gPl6H2nyvind4SWntyJGUOJta9NOttV9U9vZQS8OWbK-ji4nRv69XU6gFwqBTAvKhXijjfhn-Q2aezjHmPOe7-AErdBv3nAv3FS4l2m4kCD9865I0aK9AEaQc8kYwrPnknY3u4Gp5nWL4f5PU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=q7MC6o9f5U8R9you848v_V49OrVvQEhsORVrvK3fFhdP-ikngG3zS6OgagBP12ZOKel3-8JPPuGSSB9iYZcPKJENGKjQDmer5n_LAAa1G7etB4jhlsdpQAloB0QLTEPS0JPu115O9bQYgEoiCc_9jhPRAWxYQwyFXG8liv-yvhXolUpPKjy-yzFplQAbRqrcRuWWDnK8JD9I4WMyQViWN_aATxVys99b2a31eokO5zZrhGxhHZu4shJX_z7x07F1ZTMMHmzUeoIPlOj5ZYYcEzMkmg7J4GyPSLyzUJLo0KkTPBrE_Z3axT203ChPorzOSb3twcVwyt1gxPzgWYAMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=q7MC6o9f5U8R9you848v_V49OrVvQEhsORVrvK3fFhdP-ikngG3zS6OgagBP12ZOKel3-8JPPuGSSB9iYZcPKJENGKjQDmer5n_LAAa1G7etB4jhlsdpQAloB0QLTEPS0JPu115O9bQYgEoiCc_9jhPRAWxYQwyFXG8liv-yvhXolUpPKjy-yzFplQAbRqrcRuWWDnK8JD9I4WMyQViWN_aATxVys99b2a31eokO5zZrhGxhHZu4shJX_z7x07F1ZTMMHmzUeoIPlOj5ZYYcEzMkmg7J4GyPSLyzUJLo0KkTPBrE_Z3axT203ChPorzOSb3twcVwyt1gxPzgWYAMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=dtOiMxQXVGhDPEbLah0PasxUeFdGfBwDE9idJwQCpoMIGE8FDK447rvUwYlW-pshvrp_Ak6eb4eX3nDFeHfNNwe09yFeL6u3O5TcW_hM6u7hnPrEwpRVhBDZN5c_yyhX5jZTUH8s3ZykZY_OlDu4kC7e6g4kWwVChzwnTdhKw9HD9yCvdiwa3zJR-HSrn3f4b2p84G1oKoToiQtVOGYBP1xW0H0k1jPwR26WTGDPxulCWoYbK88iUi2LN-Xf6fI2R37Vw5QGsY1ZjC9ns2wgggC6puIsZiRefMqRVfzHdYpXgdaCbZK4rReHyN1naqpGG7m6J0aEuIMhqLt4MAzN1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=dtOiMxQXVGhDPEbLah0PasxUeFdGfBwDE9idJwQCpoMIGE8FDK447rvUwYlW-pshvrp_Ak6eb4eX3nDFeHfNNwe09yFeL6u3O5TcW_hM6u7hnPrEwpRVhBDZN5c_yyhX5jZTUH8s3ZykZY_OlDu4kC7e6g4kWwVChzwnTdhKw9HD9yCvdiwa3zJR-HSrn3f4b2p84G1oKoToiQtVOGYBP1xW0H0k1jPwR26WTGDPxulCWoYbK88iUi2LN-Xf6fI2R37Vw5QGsY1ZjC9ns2wgggC6puIsZiRefMqRVfzHdYpXgdaCbZK4rReHyN1naqpGG7m6J0aEuIMhqLt4MAzN1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sehEX10w0si28aH1IWOMdzk-pa8AD73Pt8VHLG7EIggrg2yxst7bdZixYd2IS4u-5AsK1BMG-MdJ4yA7gor_Nq05K9QNNBvERkx_zGFSNJQllX9yU6LnM788ubCuAF5-I1q7hAZSXyOuE-txZUyZ_BnZPA_I7oCs0e-9dbPCouI8BDUlAwbdEZypTAxtmkj1TR59eg6RW2GMeOl8dfjGO5L2X0T5l6YdPE4_aDiVMpH8_gdIrsBKby1pzfOKW-nYRc1a6vZecQfnCw13sCmM16Zg_iMKD5anakUaBiBqNPKKtbzg78XNxZM0AS44-Ew-_-Pmy2sIai6kpypKFb4emQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NKwQRf0_u9oU3NtO_afcupsRmH7bpX3Rqq-So3fBjBPlNo6HDuYNwFCAFiDg8rShHRP0gxx6gmHjvBwL2uvp1K-ls0G_cHF35Fd7CQZC0Q203jme9G2Z-cZQ6bgoAIGc7SgGxihuI1JXtx5j9sykyWN1d1VMtl9HTajuBmTdtq29sjUvV_qHVaDoTZDFqwN815JceeXEzixTJTG-xV-JIB41H80vEJAdTlSty-dHcSYumxFGGTjrUFYt_FPXFBHqB-CCPP2QoGDLY2YkpwBdtjd1PP4v8-TJK8DpjzJB_slizUcnR8wMKQLcKIHCxu8ca8PVxdpKux069_EwoGxOSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbAhqnbE1pZCDZR6_cSGWnaAQw_61VtrjKYQEFBXCoA2S8vDMaIEv4jM3dIcPPm301UAzS62sP7e9L5xQLeAPWmCWwwJyKuFLqntMz8qO1gqO0lgS5A-_kQMP-JPc26FPK-DiiZO92xfvFUx6Guzogo2n1CYqBxoTNcalwTpXbmTi0-JLUHmu0RzM_t9hKJ8y--2rJANZNJlgdPYEGH4zZnTt5eJD3LMzLanA1IEQ3DYLjofoXpY6x17Z0tlIjEuy4nEhpNycAYjwLqbrbSlgkCci_nN4Unnrag--0B6xYtBM-Lzt_3h2a5GCVza05jz45AjNF5kjeb1z4DKTkoR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofwVRl0W85iF_MQ9O__qSQ7UlAznAlyUXSzG4AT3DF3JfqF1tsJu1Su2v2X0nKyd7Yxh59VPatpvgaz0JfBmjsa8hc-oDdVkpFUuCI0ROKx3csvBN-e8gs7WDCTr4PrCZC-zvsi-zxb6mrCaHfVB1in4gZU3fLbKhMy3rfdGUMCgNZwpApYelZl_IgH7HHelNhBsGTmqHPrxHm9aH6CcB2xEN9_fsRDaCTUdwFGDkrummpzSrRdgnCoMq17DgFQ1pjW0JELWapMDJE5SOUSkPldgxhpIaAiLMcD0mXhPtO7svR5ItspJLZRRyHHPBatmzkRkiFJg7h3KKtxsc1mEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUJSK42KT7VqS9mBjTq5ga843zSZP9PjDJqw5XkPKDoZVjmTH-MpewNtLDFEOIlYGr3hMBS870KWjAx6_7-0CFKI2aZ5Lv8X_p0gPciPK6mlc32brbI1HkGp_opyUcit4eEyj-qhmXrUQ5ZBetNPHZfFWpIamCmN2_hdSVlB7OIb8NmzZwFDRbAZd4ZFCNColTA0HYYSj_pA9vwfosqdEdfDSMhAGOzBVNWapJzKSpHUkgg1FOs19wQsU8jWcFCOICywVi3gDzEElZPCqGaMAJHbWnAUwRDjZJ8cPVYwPihtDMlQgOxe1nbGAe0-NffyaadBRgEwDYXpdL0ANm4_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpNLhfaTr1y3HGlaJgA7v_P0SomzPKJ5o3PKIVrCl6F156vunlQf6QN_WnO7sivoKEEMnDg3BbwHbvB4dIjNAQMUAPkD66BErjMHbbkFRVjNFqLdDu6bHKA8xFYvCop6Zn51EDPBIsM43uiWDtHhqyGBHgBSIRG2FtgS5VEVZXk5rWarQlZRPiSV_WK2IgKziu_23QNoEtp6zjE_bGR3v7m7wGaz_SQE1P6cVVN_g8KDdBmFY0rlNZpZthWccSCe0RkZSfQIqyi_9KzLB_06u1Td5OUtqSs0LkjHVBKObNDt7CjyNXRgE-ZqCz9MtUL7yVOS2vnZxadZ7wfCBvxhtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tucab1LdHLa_dtkx6ISA8Rs0pgynoCAuBhMUlJtCj7a3vHx4YxUbtEMVRCP0XTYouMkYdenK49xRbqM5z32UNdtTwjYsqtqh15I9nghn8xM1EUYNa7g31kpJ4pLRdFClSfB9sLuAa2mkel-l-rk_xv89vvvSUPJ74vGuIjdwaprncj7ryKlx3LDIKgCrsS7E6AJImtWFy5BuzilRUMeEs-ZlGFrI7gBkw7sOB4g7ih8TsQbDopn-9HHuwmEiu1KjARkvF8V-a7JgBkz4Ph6Q0x7XCblE3GxLUWvNX0h4CRiu-g3teZf82x38N1rPInFdibDn85RNEshvk33LdU4jnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhkOIBvt8Ix2pAYokZYxy1WIzsVOC7ACV87TvkaG6bAyZpJfN6zHoqpN3OS5bQd4UExyo2lUF1rFObPgPjgVpj1ulT5xRpec7BYwNcwEYMawpeYZRxpqsp_5zaeKtW3-XDMLiEKjZtR0-D483htuZX5hRCDrshFz2ViivAk8I2kl8dMXG59U9AvPyhaxJ3hOYW6vFEIA6ojB_i5ohNV4Usz_ZRmpKQ_JU9vraqOdv-RZdHot_el5crMtJYF3FezBgFj1cS1E2tQthpMW1k7Z17yCs0hx8-LuQpUddcqtrNBEIRFd48FRUTflPGVTW9Rr-13wUp1PTGKnngSm04OPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=JnF7DOYEdVEhT-wMtuXd0Otc1khh3TA73x6lgxy822yX_qiYfwuI2S_DyRDbYnqhjD6ucoeeITMGpByDxU6UV8xv1gfnSkDPgygeHnYfDkA8ji34zW7zi7PcfsSAHa_e8A16LM6fc-Wv0QUMwU7gWMfdSY9e2k4TVfvn0kZRwwtw4KT6N7D1hzrha3b2k48YVowKEncT-t87TN4s2NMxbBX3d-8i1HOHJCMCjyOA-J0YHtAmzVw3q1rURbbx2KPODU3reVhD4uTfW0MXvuV1Z0P5JXBwYJER8d7qhw2MnZBghuldOWd1uVJ8YYffny6mqMGkn5E0isz7PBltfNCnqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=JnF7DOYEdVEhT-wMtuXd0Otc1khh3TA73x6lgxy822yX_qiYfwuI2S_DyRDbYnqhjD6ucoeeITMGpByDxU6UV8xv1gfnSkDPgygeHnYfDkA8ji34zW7zi7PcfsSAHa_e8A16LM6fc-Wv0QUMwU7gWMfdSY9e2k4TVfvn0kZRwwtw4KT6N7D1hzrha3b2k48YVowKEncT-t87TN4s2NMxbBX3d-8i1HOHJCMCjyOA-J0YHtAmzVw3q1rURbbx2KPODU3reVhD4uTfW0MXvuV1Z0P5JXBwYJER8d7qhw2MnZBghuldOWd1uVJ8YYffny6mqMGkn5E0isz7PBltfNCnqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=ngwgtfUwqJ6gHfWTkacHWW4g4KxtceNkKe2fJdNwTkIIDfdJOKLbv80gMC_bjKxVyslysemfTT8khat2fT2kd04_S-dPDKNUg_iq2am92gUiqRzGNEzKcSmugRT0a50lSgmRHh3sHvtPaZYn2t-GFM5IrKDub3ZwJ-H-4QIf1G2SUsTXG1fQxux6BRqUwpptEcL0_VVy2JfKQc2WaT2sGSzaHbxCK2oGiFbxIag8u2wgMRLrCqJwiUNpRoe0yD1YUFP2EE6HiYnypJZ_ab0EljElzYIB_bnH4c2nTtrM64iBJIqnw1t93Iay5jCrWGDqWm7FjDbwRq3z3I9HXYqVag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=ngwgtfUwqJ6gHfWTkacHWW4g4KxtceNkKe2fJdNwTkIIDfdJOKLbv80gMC_bjKxVyslysemfTT8khat2fT2kd04_S-dPDKNUg_iq2am92gUiqRzGNEzKcSmugRT0a50lSgmRHh3sHvtPaZYn2t-GFM5IrKDub3ZwJ-H-4QIf1G2SUsTXG1fQxux6BRqUwpptEcL0_VVy2JfKQc2WaT2sGSzaHbxCK2oGiFbxIag8u2wgMRLrCqJwiUNpRoe0yD1YUFP2EE6HiYnypJZ_ab0EljElzYIB_bnH4c2nTtrM64iBJIqnw1t93Iay5jCrWGDqWm7FjDbwRq3z3I9HXYqVag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCH4XnC9yJIaR4ovd1R8lNbKyCFAH9Jx2sGbTudcmvqsd5XoyjhHUMoCbcWVpsvEpub1D_nNTOVa_rlQgSZyfOSM4wrwh3h_XeE8I-KtDtZUTi38K-LTf89nGRP2ZTkQD_A8dVm55hzH8jZEn8qRPZ1g_Zq0Us6Ykdv0folZ6HCKzjkXueD2bo0RvP9a8EBi4eQ9Pc3vMol98q7nf-fOdwel1YF4iQMdfEoiR-bFrkIQOnfi1Sv_5ADm1BL-zGPMQ3ZIfSlJO_uQvvp1PBYhP6MKBnd7El7zYzq1FL508MKfA88yHG39Wpy0aOnN7hkXjt11uAUVrps-HFLhwenp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=Iz-3qXRT4QJi7_tlLsQJ3xZNWOvzSSqCZmexhC5Ka3Y3Q2UmpcHi2G6pAT_lcNbxcA0rRsKQWG2ec5oPDNe3wGk_iDysHDW0POV0c9Ntx5STqQMcr6srlZ_sxGPa_Ln3WqOz2YiKbyg0Ln9HyLj0jIQCm9U6gPolpjvWLC1SyGaeHQxG-V73x7_Ua2AzrVmkd7FtDXmFsiM0EMtcT6YyqggPlZM9moNKXY19LbRWbjh4mto8NQOS1U1c7-YaRu8B0BTcnavdUJ_JHePzLWbs6wxVVy2x2f7ENHVVp5OLEwW7gQHXLAjESIRzQzXYLVn-lX6jVJG3trFNue73OouZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=Iz-3qXRT4QJi7_tlLsQJ3xZNWOvzSSqCZmexhC5Ka3Y3Q2UmpcHi2G6pAT_lcNbxcA0rRsKQWG2ec5oPDNe3wGk_iDysHDW0POV0c9Ntx5STqQMcr6srlZ_sxGPa_Ln3WqOz2YiKbyg0Ln9HyLj0jIQCm9U6gPolpjvWLC1SyGaeHQxG-V73x7_Ua2AzrVmkd7FtDXmFsiM0EMtcT6YyqggPlZM9moNKXY19LbRWbjh4mto8NQOS1U1c7-YaRu8B0BTcnavdUJ_JHePzLWbs6wxVVy2x2f7ENHVVp5OLEwW7gQHXLAjESIRzQzXYLVn-lX6jVJG3trFNue73OouZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=t699eHFtPruAEh343f3bQ5WjOXX6I4H-AqmUjbiCaB6rwe9hLRvUkJ777q6yoPG3Fr5uaTDfozm4D6WaIZVBZnxZJJsI0f9JvHbw2g_Dj2R7dZtVYfByIXj9ss-CRJTAPKJallzpGyh5VisQUYK7_fBTBia8fKIYygCB1Io9DgREra1awtmCVMOWIze8c7k7Pwg9Dwb4Yv7hP19sAddzN_i0edOITM6lVSYjqW1j_QRg-VBCmIoD-Tr-0xvSQv6JsFvQcm312aHTWDyzzTl5C64YUSczV2q_Tl8yi4si-sslitSGlFO-H1xHeBYz3QKXWNgTakI6jRQ6YKqXDifCDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=t699eHFtPruAEh343f3bQ5WjOXX6I4H-AqmUjbiCaB6rwe9hLRvUkJ777q6yoPG3Fr5uaTDfozm4D6WaIZVBZnxZJJsI0f9JvHbw2g_Dj2R7dZtVYfByIXj9ss-CRJTAPKJallzpGyh5VisQUYK7_fBTBia8fKIYygCB1Io9DgREra1awtmCVMOWIze8c7k7Pwg9Dwb4Yv7hP19sAddzN_i0edOITM6lVSYjqW1j_QRg-VBCmIoD-Tr-0xvSQv6JsFvQcm312aHTWDyzzTl5C64YUSczV2q_Tl8yi4si-sslitSGlFO-H1xHeBYz3QKXWNgTakI6jRQ6YKqXDifCDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
🔴
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور دیگری از حملات را علیه ایران به انجام رساندند تا توانایی این کشور برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
🔴
نیروهای آمریکایی حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، انبارهای موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
🔴
این حملات جدید در پی اجرای موفقیت‌آمیز حملات تهاجمی در شب پیش از آن صورت گرفت.
🔴
نیروهای سنتکام در تاریخ ۷ ژوئیه حدود ۸۰ هدف نظامی ایران — از جمله بیش از ۶۰ فروند قایق تندرو متعلق به سپاه پاسداران انقلاب اسلامی — را هدف قرار دادند تا در واکنش به نقض آتش‌بس توسط ایران (از طریق حمله به سه کشتی تجاری در حال عبور از تنگه هرمز)، هزینه‌های سنگینی را بر این کشور تحمیل کنند.
🔴
نیروهای ایالات متحده همچنان هوشیار و آماده عملیات بوده و برای اجرای دستورات فرمانده کل قوا آمادگی کامل دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lCvuSSY2XV4Gxn0WO1xsGNPVl3ELTYNMlSdF8b-veP50vb7GyWWgZJUnSrcwlorrPTw8nPKUza3VxRApMZcESXWT7auF2YWCfFTDJR4p1nBjR4Gcxkfn_LK2YXCXFwc6cvblVRCQ1rXHOEjAOSyXrpsbHam6HHaApED4e6pq8HlKxmnfrWXCRdE_BKb3y2uGe2PXsSgcFiVlyUuT78mAwJvY3KHRRc4_1hahquu1xRbE7L0Y50GjSPxXty7GnrRUgxXY8FarCa_fWWpAn31ToOxeF1kZWSfKFcwUTOI-wAseIB9XWcakdGMc_YFOpB5ZqIOxYtuGlZuvHzGQO0OuAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJsr9Mi2J3jLJWnyofsL8F2ISF8JGK2WV3YgQT4gQcvhcGQR2Ch8Z-G7R2xBVhq1cMMYTDNq6laWuqa_Fo2NfPFJdOEDtgBs8ooo1O2RW9iABGE9LLrOqhKT1g0DjKgzUXH5bCI9ohd2JQYY0gRMh50tQDx5zaVomYdVneiaaiKo-_I0wbS4opGlBULr03ANQ9X2xtttZdHs70Bpjp-Hd7J3kA7Fvt5hTj5ZpmaQ1LVjRcq2N2hJyMowImE0r3g2F9Nk-hidzJrCKfZQRahSmONtYE6UtBU6dv9PDWzHzMy7WjCFi3hoP9_3xbcbNLVbNdrGvEhS7UbN4v6yZPNi8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FvJ_yuwTjFUm4h6vjQjZZJlUsFYJqqFvSdCQWw9NwKKW5tnYmna5LJIr-a2Qm-v0CgCQ7IqkUpzei58KJlR5a7f19GRBaZMa9pT9B5rsuZsAeKCV9uX0glgI_q7s-ZKu3HC8E0pMbvp_GRRO056TFe5bqAgr2Hn3EXLRLjMqjr8hvZbSXItI69HjxOxSReQRAYtfIMbs9ON9uJVuoBE8wSdwmICkHMLYan_jEy8fO8iJUVvSn4XyhBL-bYkmdBEbCRnsHGjjLOHwhiF2ZVpi-XyKp5FY9RxEXV3zYH4QVJqdQrN8gdcqI7FKOiYNnsYr2JPiQEhvHC5K05xgy_PiyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=ezMMQZ7X8FuFHMeiBvmDJUCnj0hdkKqEcxAvg4TUFz1-9fUKsufLWkMrCsPwTohGm_ursKO2-QeT4qx3RWJ8Lfeb-Vl-zu0ZgJj_4UHbiuAC__Svbq1c3aoBSMfPUVmS_37En6ASDa4x2nrC1mPUMX-WMRM9zmP50oj-AAzqbQFH0ROjFyYGpD8YKJ0QE32RlEz8hAL8MsSn3FV2jDsX6zI-vbkDJdv6LG3wgxmDP4onyMI6UAPqKyopccuzVmgwFEWfgyJXhN-Wv4IDCyzVqsg1MpGba2TL34I03bWz9dKuUk96vO_AgasGZzwvX8kbZim-liPbbP2nqQ9NGNuI8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=ezMMQZ7X8FuFHMeiBvmDJUCnj0hdkKqEcxAvg4TUFz1-9fUKsufLWkMrCsPwTohGm_ursKO2-QeT4qx3RWJ8Lfeb-Vl-zu0ZgJj_4UHbiuAC__Svbq1c3aoBSMfPUVmS_37En6ASDa4x2nrC1mPUMX-WMRM9zmP50oj-AAzqbQFH0ROjFyYGpD8YKJ0QE32RlEz8hAL8MsSn3FV2jDsX6zI-vbkDJdv6LG3wgxmDP4onyMI6UAPqKyopccuzVmgwFEWfgyJXhN-Wv4IDCyzVqsg1MpGba2TL34I03bWz9dKuUk96vO_AgasGZzwvX8kbZim-liPbbP2nqQ9NGNuI8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67628">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67628" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67627">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vyCIvVaB-3jEQ4IvyFdIaUd5o6g9X8V4WOxpAFAAyidVLY-P_871_1Pk-qNns8o_T-5LRtuHAIsHDABZj8mk2F__zppU7f6SH6NiYNnsviXH2G8CC8TijDB7L8nEzoKKoNUAKky_wGh29TqMWh-M0FNBUPJU48oxS_mh8lgcDNOWNiI22ng9paovMHrgXd4wiDV4oXESBL3aXcJjS4XPhoK2EtK4wdYqFt0CyNIVUjtag_NSDNcrLPqSdMv6sUqrvI2wIhGdPiB6UCULYi-rf7m8xcW7w6NgUYm9mazyfUM9bFtByJ2i2d0y7IxTBi748zUp0fcNiqIZjw0WfyfRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67627" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRsuYi4GrXDvPXRc5xr6K6THNRXV44G-Q_mPTgGxK9Z5Gy-LTDTaAeUyfgW_8ZfJuT-xxAu7a3oj1yDFv8aYEbUQzYY5SoIi1wLmpLPkcCSlPwqLNXVpMUXguM21bkg5UEu4qU0aKrEvlwzotw_SwubBwH8-80JloxWXpbB467LAqz3L5IUH3bJgsJUavZZtK5mowgZdYTHp7dVobftDn74WQMNqTNGIyjQwAue2UxtKAF5b9GhiM94N2ltwWLCqijhRfygB--Qs0ObxyWhKX-HoP5GET__H7C4de1PsaEVGSZUycwzw0f3wA6DCh5zeY7l8ABHKEFqk2i-_IdjTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJozlr0Qrvzv6gvrLMg0_vnDI1AqTM-v784tKnMKBWfP2_x0g86UZmh3ujf_zZ4zN6rFBCUmNjsEvkYClwkivJz4Um6BmSA_hAO1hOlo26SkF-YAQz3oaf_fyirnkKZcp5Pef8sqB2gDULYRbTuqR1LBneyzS5D77OP7BbfoXx-KdDxTjxWzRPvVlzEGNLtbPqpni7nVG5ZWjDdD7p5z2rOlhVcXxvIUrDZMpeYeyAOA3Cu6yMzpsVKsAPcnhBtHZ-XyoEqAk2oFoCsnLGzMXUYYXgyGUzmL-N2UtZgb7qPx9yWnyn0GPJqShEenW8HWS96hxEmoxVu3xlYxukGr0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pA_GMqr8AwX72RVMVb037CtGQYX41RAqDJojUhsnh2kNbAQBOFgxMGgn1WW_HhWkWycsoeL1IbVS1BOjWAzVuVCxIclL3j1z136Gk-WYTacy3ijcrIV8FOe2bbilYMCLUQuEoDz-7brV6xJKR86b5QKQ-H4KV_s4ZlCzsdvI_cwzBQEMtxfhTy2Sv7OBdpoe7CSAHtz7NBrak9XwAWnylNBF8lyijaTv8DkPBur7r9rkQlGgDlR2gEdhmBKzJ66LYTSlw_AZ1i26YgpYra19KzWUkXWZDUhUFzL9yfKmOJUZLlaJaOuOTUG1vpTEmdWSsjZWI5nSOSIs1U8Dp4jYzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=UTDaA1b7q-y3FT4Ski62NkXmdbmJFK7row3csEaIs1nUVGqeID8vVIHAM73dUo4OLlk1WrAMfsAUiEt1VCWb4sZp-TJmTCbU18O2KRd_kjLOK_5uMglAbwzntttXcBrgNGHDD86FcKoS6nIJHlDjJ-aR2LD5CmsQFcmodGLJU00GwIwkFNwaB7GRqhiGIUaMjh3Z_QLljTRGYjhQwLR16e76M9yTBHzqbTul4Ok8IxJO8SznO8aBr8bqmfUoYj7BRrbCT23DaR7Zd9HMezwvE2IoS1nztMKfAAjb8DQkcXxlt90Bq9-ZruqWnFivXbZK3WdKOvgUyPs5nz2brEVjGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=UTDaA1b7q-y3FT4Ski62NkXmdbmJFK7row3csEaIs1nUVGqeID8vVIHAM73dUo4OLlk1WrAMfsAUiEt1VCWb4sZp-TJmTCbU18O2KRd_kjLOK_5uMglAbwzntttXcBrgNGHDD86FcKoS6nIJHlDjJ-aR2LD5CmsQFcmodGLJU00GwIwkFNwaB7GRqhiGIUaMjh3Z_QLljTRGYjhQwLR16e76M9yTBHzqbTul4Ok8IxJO8SznO8aBr8bqmfUoYj7BRrbCT23DaR7Zd9HMezwvE2IoS1nztMKfAAjb8DQkcXxlt90Bq9-ZruqWnFivXbZK3WdKOvgUyPs5nz2brEVjGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=NWi-AwzftW-JFt2mAbv7s3k7Vg7nII9ULkFDy-2nRPeagF5pJGKIdm1zTxqW9WelX-8qpasc9rSsxkI11pXNHUIlH9kMXSaOqCwcIN6aU5PUpDIS2gB1kMjcoe2Wz4pDl8DO41T3rV4hx0RKvRrZYXNdghPsbzMgWOg4Jes8YEXblHQ38zmlQL0w2xn4tbW8cd0vnrVfzLwm3s4qfdh_p-0zAx2G9gliNSPmDG93YqMSP67-7RkAAedlUlpe1cZe0LcNLaRXVSi53YwAR_6RzkYFnLfuKYHaIcUbIZTfZWZt0Z2BcQjzQxpVlut195tpOUaudcV3FaQ_zr6N9RQAvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=NWi-AwzftW-JFt2mAbv7s3k7Vg7nII9ULkFDy-2nRPeagF5pJGKIdm1zTxqW9WelX-8qpasc9rSsxkI11pXNHUIlH9kMXSaOqCwcIN6aU5PUpDIS2gB1kMjcoe2Wz4pDl8DO41T3rV4hx0RKvRrZYXNdghPsbzMgWOg4Jes8YEXblHQ38zmlQL0w2xn4tbW8cd0vnrVfzLwm3s4qfdh_p-0zAx2G9gliNSPmDG93YqMSP67-7RkAAedlUlpe1cZe0LcNLaRXVSi53YwAR_6RzkYFnLfuKYHaIcUbIZTfZWZt0Z2BcQjzQxpVlut195tpOUaudcV3FaQ_zr6N9RQAvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67621">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=R20d1IPVp0wF67Vyq2iyOTuGpxWL-uNqawL8OeYERXR7R472fbfuuHIxRgkLP7WLidAukQbCAUE-WPYuMQV5WSUI2mJsD52p2BO3I4kxIXuKMCu4JTLbNmEhditSdLm7G5U6RA05wj5Wj7yP1bAkKEYo_bg_-xjmVPdz10eVQRA8ZMsycOJkGNXX_ks9_UBoe_atQawgokZGOh4r0kUAJmqmaeiHcdkwOokjAsmhZMj2WEo2lvwt0iOk0H1_2ERJ9t67WzkXfxVTde0wW-7q34ofc4_81oOzWEKsIMB5FK7H-eS94L5m2EB5uXnVUethg92DV9MNe-c99D9j4zkxag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=R20d1IPVp0wF67Vyq2iyOTuGpxWL-uNqawL8OeYERXR7R472fbfuuHIxRgkLP7WLidAukQbCAUE-WPYuMQV5WSUI2mJsD52p2BO3I4kxIXuKMCu4JTLbNmEhditSdLm7G5U6RA05wj5Wj7yP1bAkKEYo_bg_-xjmVPdz10eVQRA8ZMsycOJkGNXX_ks9_UBoe_atQawgokZGOh4r0kUAJmqmaeiHcdkwOokjAsmhZMj2WEo2lvwt0iOk0H1_2ERJ9t67WzkXfxVTde0wW-7q34ofc4_81oOzWEKsIMB5FK7H-eS94L5m2EB5uXnVUethg92DV9MNe-c99D9j4zkxag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما به آنها ضربه بسیار سنگینی وارد کردیم، و من می‌گویم که ما به آنها 20 برابر ضربه وارد کردیم.
هر بار که آنها به ما ضربه می‌زنند، ما 20 برابر به آنها پاسخ خواهیم داد.
وقتی آنها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67620">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=J9BuvC3TkJyvYQ0lO1lwS7341ImfEN1cUovY89IJu0k9mifFoeTmifOoC_-lYSb5r_SfrSsz97rza4xzvectAuJzYJRblqIqGlp8zpCH0A1DtcKzMzTlREtLf03E89vOHGdad7FReD3So_KQ5XoFOMgEFe9uG2cHpT4MNc2tKvByYdS4GIBVd2Hwxw_fvr9Ao2aRy9fcJqEEpXZ0o86GyqnaHKUnr_6CnVkgaR0pEpas_EPfN_Za6oD5K_ZXWAtZwnthCj8CZFS2OuN0CSdN3_K0n5EDKZIkparRum8bLwWvuuL4FkVb1f4fj-2qs83mSa0vL-DPUr5gOQHoSXFPzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=J9BuvC3TkJyvYQ0lO1lwS7341ImfEN1cUovY89IJu0k9mifFoeTmifOoC_-lYSb5r_SfrSsz97rza4xzvectAuJzYJRblqIqGlp8zpCH0A1DtcKzMzTlREtLf03E89vOHGdad7FReD3So_KQ5XoFOMgEFe9uG2cHpT4MNc2tKvByYdS4GIBVd2Hwxw_fvr9Ao2aRy9fcJqEEpXZ0o86GyqnaHKUnr_6CnVkgaR0pEpas_EPfN_Za6oD5K_ZXWAtZwnthCj8CZFS2OuN0CSdN3_K0n5EDKZIkparRum8bLwWvuuL4FkVb1f4fj-2qs83mSa0vL-DPUr5gOQHoSXFPzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
من در صدر فهرست(ترور) اولویت‌های آن‌ها قرار دارم، قبل از شما.
اما اگر من [مشکلی] پیدا کنم، شما هم [مشکلی] پیدا خواهید کرد. بنابراین، شاید روزی بخواهید شغل خود را تغییر دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=FXWetJgcxd1MXZYRImVCldTmGBvK8nSlk853Tmn83kW5-iL6Ji52OjmDc0v8WrPz1sR9Mpv9iufw1lk44GiEXFMAR6_0R2ouCGPIS5GdD0xIWUDkWS4S3xPxtiPTTqT7pL3FvM1C7tSQq13tuzkNXk9gR3eypWPeFZOR725FxWKaxk09VSeqAAc4YdPseMl_nLp_KWhesdd9djf-JnjEJyToyP961gFiIhCfo3QYe9fDCa4YFoDWv9bSATmN6KMEnDw3dneK9aRgMMTVG09wGLKp31SBO4p748ikKWbUOIkan4eat_kK7faXxnxtD6GwpbF2aFrWGzOnfbl6-jDyGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=FXWetJgcxd1MXZYRImVCldTmGBvK8nSlk853Tmn83kW5-iL6Ji52OjmDc0v8WrPz1sR9Mpv9iufw1lk44GiEXFMAR6_0R2ouCGPIS5GdD0xIWUDkWS4S3xPxtiPTTqT7pL3FvM1C7tSQq13tuzkNXk9gR3eypWPeFZOR725FxWKaxk09VSeqAAc4YdPseMl_nLp_KWhesdd9djf-JnjEJyToyP961gFiIhCfo3QYe9fDCa4YFoDWv9bSATmN6KMEnDw3dneK9aRgMMTVG09wGLKp31SBO4p748ikKWbUOIkan4eat_kK7faXxnxtD6GwpbF2aFrWGzOnfbl6-jDyGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbUs2BoE_aXhfuMBTjp73VId0sGhUzlhdY3p0ENaH6DyciOwTHEEP0gUe1YJgciYOWy_oZ-5h7ANdnHaInm5XZtDKfJLKo_EF16FmTeRfGGfsaWCxCVx2pCKtNZFwZzBPw-L-F86M-vljsMQmFdqxiK0z1kFvCA86qf2_VYT_wI2llEbJ0rWyNlziEnirhpQdhFaRYl_QB3BRdDTV6IVfiOmbjtj9qSUUXyltJ5Sm1DPLFDj_h8J7X5AWjzxunYqjVglj2Hdh7Ia_DM_9rNjkRVCfiqW5Yl_-ZCM-f-bgEZjXcMameua914TZ9tAWnQJmCkQF294HfzN9CHggUoQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyCMF1i3dUzKGDJon9ERc5wH1IoRJZJhNQv-prKZvaLmr43MaKzzwdfH_nN3tZayIaMcKOTF1jgBdb_-mtQ5Z8iBUTgyEszXvWVlAx4pGVQubxGl2TRvBuK-M3bonG8dlx1jVTmx0vvR-5RTH7-0WNFJJJ1siOHLuYLKIFAhDb_Ku0HJ7eEfnWqdOs1wojoRM4zJC7h8Xkk51iheoYxDP0DFhuIxP0-nwHXBKtemD517EWGca8zyYq7GuzZf5Qahz4mca3w7bEzxVSf0akFcr8iXBQ-Etvo6zI7qT_CkZfxqeEOaZGhIUobc_CDM4FqrxeSw1Rx7nKoAaGdbBFsn7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=UnxuIUrUttpUiPBq5v_drGEwdA959cuK2tmcjSr4jctnENnKY9yLovRNLU9SZWoienKReqnCJ_-porUyJH9OF6YXJ1jfn5akc4imRsLvzC06tmONle7M2bO7_YRzs4Lcn6JZVduBjwD-zjK3-7DDKu6_QnJBpr0XPctAhtKhdHtReKSQZV7XrcluyjdtLD3HLrx0L0U-o8Dn6ZUh6S21nFonsYpWDJiiVvBWoqRsgimDZXb9xGGCsc7E7EzFhb7Oj5ukReIHb8B3SKMhMGLV6-iJ0fMrwthlTj9R67gm1sNjT0iPnKjRbJx4O4yGedJGhkcjcuGeB4D_Xw5e7QcJLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=UnxuIUrUttpUiPBq5v_drGEwdA959cuK2tmcjSr4jctnENnKY9yLovRNLU9SZWoienKReqnCJ_-porUyJH9OF6YXJ1jfn5akc4imRsLvzC06tmONle7M2bO7_YRzs4Lcn6JZVduBjwD-zjK3-7DDKu6_QnJBpr0XPctAhtKhdHtReKSQZV7XrcluyjdtLD3HLrx0L0U-o8Dn6ZUh6S21nFonsYpWDJiiVvBWoqRsgimDZXb9xGGCsc7E7EzFhb7Oj5ukReIHb8B3SKMhMGLV6-iJ0fMrwthlTj9R67gm1sNjT0iPnKjRbJx4O4yGedJGhkcjcuGeB4D_Xw5e7QcJLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای منتسب
به
حملات آمریکا به ایرانشهر( سیستان بلوچستان)
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFtVJ_M-WjKuWgiJqjI9NfusTtc9AeJ8NnAWuO9DUL2134IvVGkK98V1IRU2HSsW_mcc-wGQAPosGpf8nMo1uzzdPGaKjDY_-ukeazufQJC5Pe7EwVvLRVL7tK7zdBEw-MjZ6ob9nYJVkbKimYMhhLQ_A6qYjn6vkmQlwJH_hNdWdzh7a5ZNce6WRohsfDSDhy5IWKE7twbSrIQSTJpX6ySTK4fVWJntLAqn9h8c_FOxEv0N6C8B0mDrn8YAgD24Bio2IRgZPPJCL7d63P7U6KzDxHNgcKrDpm7RShTU24mWYhtV_wFhD5Ksuv3oW5stS9TRgoxDhPDRY3GtoVvGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiZwMVny0J_LH2qeuFt3pojXKdME4tIR0NYGyj1aHR6QHg3HTsOGkHunM4VZZND5tlo8Kuwp3YPNjflfJW8VL7qXLdJjJqw-SC3kTiM6IiChW-USstLayq0GeiVXrSOl07v_BcOpf6AQOkJVUKTM7NTAiqmoIpmzcs5jI1ywOAiqGfkWefZY7io4iwbdINenOzupW_qCoHoG4Kmz7aFbndbDsLsWXtzn9wq6845lqgVur6WaPE3dvcxVtuPO7dsVoVxwuhk-wQ_p0FP0kkjq_wG-_z2TGMFjOije8c9XwyjPU0bFkkvJmOAnZwoZuWsj3hBH_TwQWvaMOqnTD3u1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4-FxA5LPbjqhiYGPrO6TFWQ9_-Srn-x4aYkPDADMz1a3c25vB3buWe7VgHSmK8-9PYnu7BGGXY9ZvQb1wXI20EpY-qN80ZkeYKosuxU8NMFBHGPhpWvKBP6JyKEW9g5J6Mr_Q37DQeAIcbluCXT-yHhs6cF6XV818tKVNTUbUurvhUuhKzPPDlPQEuHWAZvEs1p2dlcimCLKunOEOmw-tjykVIULxHcpi4sAvcEY62okuICsNuGBtlQgQa53REn8aaXcyi-AHFNwCLstsSYmP4a-Kvad30F93VlSnVsQubOqWQdk_U9dPZtuBBjJUnrGmhRn9UIj6iAwnjVONbaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Led9NuH5gFAUYWw1YU36gH_0ThCRuAKyF2X-6smplY6siektsg16lPALKvn6DpEKTyWfYn6mPxXRVb-VETV4i02eVHtRnqh8YTLsPc27zBrjtU1dTDGTU7CpMxtuSaUnHyYYf0YcWUbzsOJBaT7u5KpA5mgaLbby2VCvjLJB1FNULyfrEPcLQKeYCei-OlNgYp6iE8jtppJgvvCeEHLJawvLp1ZGN9n39d8QC8AScXHId8HH0mv1d93u5d8D_RiA9yCWVnSFIhrOJa9jNehzdRu-P3xJWKOJu8vhwOuR0qFZkW8hZ3nunCSPmd-hzPOWoFUctiRlFdrsdQLvG8Uymw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67605">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=sUdmtDDKLyG05oKoftylZJOUFpqmJd-mQD_n8cptdsDBBT4Nd7HuelpE-DCAy3QuM9x0bW1gPLw8pyjeBfd1chXL_ypPLV_ipfk04FCSd1-uBA5UgIcJm1_9tuCJGVWjbuihQ3mQMydSdgsHTKS_Y9QQUangFqhR4KP6mUo4Mr_vsH2yT-eWATipWq3lW-XCU5ifCUjM58f8MBOOz6hZTucyFFh4cNbektjfMzuL180g9oOq3Hu2djLWhZGI_BqmCt8twSOeTKcXHj9KvtegoXynofwJQ9CuL1HzN_UNS28PEZghx4kE2btHZ9vuCw_Amse4AZ1l_nmin8_3d-m_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=sUdmtDDKLyG05oKoftylZJOUFpqmJd-mQD_n8cptdsDBBT4Nd7HuelpE-DCAy3QuM9x0bW1gPLw8pyjeBfd1chXL_ypPLV_ipfk04FCSd1-uBA5UgIcJm1_9tuCJGVWjbuihQ3mQMydSdgsHTKS_Y9QQUangFqhR4KP6mUo4Mr_vsH2yT-eWATipWq3lW-XCU5ifCUjM58f8MBOOz6hZTucyFFh4cNbektjfMzuL180g9oOq3Hu2djLWhZGI_BqmCt8twSOeTKcXHj9KvtegoXynofwJQ9CuL1HzN_UNS28PEZghx4kE2btHZ9vuCw_Amse4AZ1l_nmin8_3d-m_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدئوهایی از لحظه حمله آمریکا به برج کنترل دریایی اسکله شهید کلانتری چابهار :
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67601">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V430O16rpdgxbYtjZq1dHBfCG5oXKTgteu3Aqdfnl9Nyiol1kCzGVtJQKZYjzjLo6rL3eK4N0pC9pt5nOLExAJC9ND6APEQSbiYkxw_l1xkUuLzER3moRr2VWIcLebd5FwQ2DSWbBQW8zTBEhKwCAe-MFK-8AC6CBw-QANSN9vGto30lEVuO6HHN_oIzIIP5UNnfKCiituI_RO8xG9r4PDjGxVZiUnBMwyO5fWW0xMH6LWB7rJLdw8pXdiJssgf2-l6H4MKdyIzPppJKUOu0AuP2QpLN__2_weQwilMwB9M0MQ_iVrPt9ZuQ5-nbqpwzakCZCQjBT1MVXbLhyW92mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFtpp7lnDoZ9wiMwHZHXVE4orpP7ME28eBeOn92XTCluWVmD8mNDaVBOoL68gvEkTxwKwcf2K2U7EVTmEybPGnOtmKDPJhpKZSKdS3V8uigpqzCwSklOJnXmq3xMpQCphE7gUVfTqkbu8K1Uh2M0DHhmCyZpWeUzPRVsLYHqP2fnjvjDUicpoQqNdWoo3Wr5sr8PCvWSYiA6Z_u9C23BwqRkjougWtAfxrUPb1DuyScOJwE592sEcfMwDf_nUPf8AfiKVZM19PCcnLGbJIJhoQoWc5kDK9-tpdn18HiD16qgSwKH3cGcE3ld6qxOAb6NBTDfdVtMX3UGlLivOyJoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67599">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
صداوسیما :
نیروی هوایی آمریکا در حملات به چابهار، اسکله‌های «شهید بهشتی» و «کلانتری» رو به همراه برج کنترل ترافیک دریایی این بندر هدف قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67599" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67597">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBNmwWDr2ETW9f9IN75-gAPLFVeKTauiXF_dtpjqrmiGdIKGwu6sEFGA1enXXxnbrg9FWl82qQX3oCFLeFsYY_dbmIazKyDcQ1vtk8hT_p3BFTv-usY0ufIA72cyvp7cRxeLYLgVTTp2Bwz9u9cDPCTVZstQZConZRA-wHIGd6llbDxca6EhKgBkswHd6Ay3aDpNmvUBd8x68Y5_0ScsfJeuPo75KDj-2KPiNlkMtrZIJvckGLvOcVFYdQdb8GBdPhK2Q7hLhXX14gQymej72D8sGN93CcM59pixlehSscSmvJJ9Nd5UykGEn5J4sW1YQKwvxXfqcoOV5HO0nJH9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2TOVIkOaTtQx4nqxUZt2Q47-ie254FDvecY6X1H2xFmrWOCSWa0DXlgomD1Avce0bnE5UcNnIgry8VbupakMzptymv-oiD0kt9zppfz7x0jg2Pcpq7YLoqVhxsQtdxBNfVNSDms3I8ptjlXGiMrMuHVxjmobiot8ryUbnhq3cD_Nlt6RqkHMEn7_6avI57V9nMKZH-FsP51XlTlUPLsx2oW-GqhS2yhH9Fc948-SGM6MMNA0Mi6O9g9gbK0yiG83vehq6PNuPkeKUfHbF-lsgPC_abr0awZ7_2MYcufB1QFqEKIXZKYYWG-TqBpqlUVkeBwle1VoBNr9ufL0RpPBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
برج دریایی اسکله شهید بهشتی چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67597" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67596">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی مشاور رهبر:
دشمن متجاوز و همدستانش به شدت تنبیه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67596" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67595">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67595" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67594">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
چندین انفجاردر بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67594" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67593">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
فعلا تمرکز حملات مربوط به خط ساحلی جنوب کشور بوده
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67593" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67592">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60497304.mp4?token=TtZExwzH4up8a_cB_BZnEjqmFuphAwXRvLQf0HVstb794KbnbesEidmXfkdMOfVHPhUPPgLRJMKUhnFOmOsEga_nepcjlYMxlEN0LY5g9l73-IBPdpAQ3ciD5yrF9ov_iPTNGt1BwLNjcjkGwz0oLhYpEFM2EDD3LxtI9ByFYGVBr1uYtPfMSAxiPLr5uxTcfLeJYjkTt5BmWuyacYq6QAKiQ_6upGrHdzuUn11RzCv1RbRsZgU3pkZDg4UkB3IP2CNEXj56ISW5sFHga_4Y8p_NarU17FSBqTK6YS_cMqqmLNgJY1zBl7YeiE4UYJmOy-E5AOfOMD9w7bOxMnib5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60497304.mp4?token=TtZExwzH4up8a_cB_BZnEjqmFuphAwXRvLQf0HVstb794KbnbesEidmXfkdMOfVHPhUPPgLRJMKUhnFOmOsEga_nepcjlYMxlEN0LY5g9l73-IBPdpAQ3ciD5yrF9ov_iPTNGt1BwLNjcjkGwz0oLhYpEFM2EDD3LxtI9ByFYGVBr1uYtPfMSAxiPLr5uxTcfLeJYjkTt5BmWuyacYq6QAKiQ_6upGrHdzuUn11RzCv1RbRsZgU3pkZDg4UkB3IP2CNEXj56ISW5sFHga_4Y8p_NarU17FSBqTK6YS_cMqqmLNgJY1zBl7YeiE4UYJmOy-E5AOfOMD9w7bOxMnib5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67592" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
