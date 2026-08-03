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
<img src="https://cdn4.telesco.pe/file/LHOFFhiazTWK7cVhJgmWtwL7gCMmVeMTDmPvPB-VYMQQ7oprYo_Q2SlDuiiRLKtY_r2jl1H0ylOKDqHnXkk0HyUJGCCZqkosH_Nl4lbMknjVER8kTbcMojyFiecAbosRqZ3lK7H5v18s-tASzdgmoK0vGp8RraI78Qi3nJhOZfPN5tt3VgTuv7Qb_Ce9q5lmObkDnmKNPCvh7rZUFGMIUEm3XxxOqiqL1mVp7Zm7RWRH57TV6iXBrsnsOeiZjgbTkzkgQ4HrEF9EHPzk-F5d31LHjy7lyV-HR61llYsSYbg952r7sK3zv33pG9sALRdUqVqdlqiffxyc94mWCBEYPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 617K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 17:48:11</div>
<hr>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVZ4KXjDj5Ta9lYTFMqxU2Z2i3Zoiehz8UTAU84p7g9MX0V-bfXFo1RC0iXyuVLDhqOUjHjDK8PEt0bzQbvU_Axe4SfLWCWjtu8PiXK25sQ3Bqjg8i8xYLBWR-B5cr2bfFCHlYIrt_p_1AA52thswSUUg9qsvFZp2yaFqsK8743i_iNrkBJOrz1D6d8DfX89ZWwKthoNK2O0E8alvx3_nt5wLoamKbzHVwJ2jTj54HMAQD_OuPDCLnUbTATye9u1R5L4xhtbLZ-3DTziaGBWQntyFQkU1OEPBD4EuccqebyM3b9IktMm3Dn01mjUmuiTPHU5WOpyUENATB3h5Ec2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL-EspvObJ7TgWr_5fZqz_3U30FLFzBSpMvsG1XMl8J8c8ndW5jMYZEUOzYeyastXSi3h8s_P_yKe1z06D539PZ2DspW-ySxP4_ldakLEQTpGkj473J3JRUxxlVujwfe1dto4NdtOkA1wuPTEEpsRM3KmuVgFY2cPBASCHu9wolDLahYRkqIJesP548NUvfxUx8r9tbxV0iS-I4hH3h5YnZ4EZtJ5htUTP41yASUDCaR0sLFFahfS2yOeeOXbV4apSMEgUI3nLw6WTTOmZm6auTK2RsTxx-fOa345WpdTetZZofOFEh5Ej_YhGzFmeYOakg5lEb1hiUx5HQoICXKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHHLNcpJAdnY1HyHidUF19JyoXvNe3Vy2tjxEr52OZfWc2JvCMhDLAIA1c3nyIUk3eudFi5SBsytXpB0I5kLbCuSCYsig6w6l4vuQfMKiVpMLD6iB-tun7vq0nuqk8ScLOT0ZpY7ZLJTw4apRn8-oR4hAGGij5Vmc1frS2gUpcd4hlMFtZktCRHMw3hlu6ga-KdyoTAMMxCJDH_OxVj8sNMk-PN-dafE5i9TZc6vMms6ndxW8zxC4tI9q0RPLb9Qxhf9FQYvQ9FLYZv4X2W3HPips5vZUelJVqZ1RmcjeBRIHFBBBPFHG94nlwSDalOnZK4wpmL-VaDpagR1W82b2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKg2UDVdGVF5vQRMhutRBGCFPdMBK0mhKIY6PXVp9rk-dD0sSQfx_MdUbzX8QYZ2s87omyDIDdkdXlbeQFTc2qMMEXEsdR741jg8YGqZDT2dVyKZJQWepi6fbW3VZLZk0eXsKwM7Ldw5F4bfyZglkqU4-cDQ7gguiN0IAtb7Hd4q3_xz-XtZ69tPvkLNqhjIz38xBGxFSBV7QFSWbasEuruMyrvpGHo1slqjcvSBy2JDoUuzLyJAidLxaNe_mAdqy8AzRMGWPICAXhcDJtXRWtsC4rlQLdngljzF8fIDRiJjChyyvkuGDJcNzhFnBCWjFhagox2CwUfWMN3csMQe5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2279080601.mp4?token=t5PUSeCDmF0iYF9CT760_4YACJp8f6JTMfmdoCBBytOieVYnvpdPJzeBs-9RUPo9Zg2HO96t5jY3kdCTWrR41jDG3jVfAJ7XQ1pAiZ_LXxXVdmXM7DnhcvwysX08qApE0_LjfywSqp2IYnsMiTy4v2CMAcl2PdHoA_hhiD7twNtom4AXZR9x45lNNjmwTjLjHhn6nJiJxgdquAJtaS6g6MUjJH91mhgMvOXuMIYZk0FBjW1Ef2R9WBZSGHdavmMPTEPtVB1sNDXLQjPN-LYbmas1gmaDT94Zs5d989p7mXggQW-rbDMsSJDdYfR1qoQyBpI79JhUSwSEA2dW5oziKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2279080601.mp4?token=t5PUSeCDmF0iYF9CT760_4YACJp8f6JTMfmdoCBBytOieVYnvpdPJzeBs-9RUPo9Zg2HO96t5jY3kdCTWrR41jDG3jVfAJ7XQ1pAiZ_LXxXVdmXM7DnhcvwysX08qApE0_LjfywSqp2IYnsMiTy4v2CMAcl2PdHoA_hhiD7twNtom4AXZR9x45lNNjmwTjLjHhn6nJiJxgdquAJtaS6g6MUjJH91mhgMvOXuMIYZk0FBjW1Ef2R9WBZSGHdavmMPTEPtVB1sNDXLQjPN-LYbmas1gmaDT94Zs5d989p7mXggQW-rbDMsSJDdYfR1qoQyBpI79JhUSwSEA2dW5oziKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقادحديث‌میرامینی‌ازشرایط‌سخت‌اقتصادی:
یه‌جوون‌چقدر باید کار کنه تا بتونه یه ماشین بخره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqjreoQOb16SkBrFmFPGc2SxKtkUVQO_ovP8ahDBgqntui4BiGqL2C3KYWaojls9LJkMRULY8rquNAAfQYkZzKPhzFAXAwXrQ5Mz_d2ngbs0W8JvObZ1Livq8ta4_kw0oq-20YDLqLiDx6BcD2w6qQKspX0Pxx7lc1dDUA1q5wF-npOJYbLgGJs3fx19ZyOPd-xf0hUjatPmsjub__gCcbutnkBT3Y8a9o378-HgD7RIbhwah_W_7pQbXRk0gxQdhOpSPaG4Eo6ysymIDAPumgfKrpwOlTaENRNU8f9vFVE5Mqefh_UQxMq80QTkbPMORZWia827BwyAUnhByDv12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idvg1-Z1zyyTKWOOEtZrU895NWbVAKmjnHsIWGTV3lmTdtM1IqKe9X8IuHDuD1Qw8KgO_TYfQy2eTOFTTgdHrDJvV0EXILzVZzm_8miwe6SDkl_4Vq73SbwKSl2mAdMG7VsDdt2FxuMQ9WaWJj6CK_HG6vK78Mq7GJy2lyboujunDd84DTKnNdyZcgNVzMfSFwMyhucCBmEr6PG076oP2UU9M7HWPlJlvyee-ah0PtN3hRfR0VIX3I4nIid-QzLV0CLc1k0yD2D44HQXqHIgXCcSwdF2vvCbDFlOjsUTEeCf6YtrKmHfYObHauCtzg_k9cRj754a1piBOFoZ0-eTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEfJtMeQ9exu3v3cTZvdplbvxWZg6udvmLsbPp2-Zt8XJIRDd-0hic3M_M_WxrfJE3xUefXvdoFeWVmOUhLzsvbUjykJlcbvFkNUCC4RyECvtvm7mjQYhMho-g6HtuY75KLnzAtccbnYI-5nNWkFbZE-_1nJHQeJxeOqrZ7zop39VWdFt8m1tEjyoprlpUYUd8PJDaLw1b-fUjT_ug0eTEgB3-xUCWyPlURyDSowMAcNOfs35r7U38Ysazrak_gbEYezDUPECdWpQiQ0ffvtlYNOACW-ARv31uvOcDePnvnPZkIhs5bFvZ5M6gGuSlq1cxNJqHQVLjNVm4AvFwbYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQOvin7quw4uH60SkxivND_6RdKd3_gOzhXcHN9aioeBU_jH2qvUyvZRC_SJZefI3ujUrqupiUyorVhGhYsz774NUGi5-EhGWobELC9ihGgtQOrR75ywdv1HhQv67eVAPknw0FkinRRqYebE5-z5VkfH5Y0NbMo4LfO7TE7-lAy7lHS2zSI-hNLa-wuwz6uyZPZb4GCB890SeQmhMttuOopaVMmIOwVAK4FMUt-86lDJFCaSy2w4cUSYBbAxnT4qIqKree5ETSap3t3-syQlWPmpIKcTfcNcn1XvI6j26JrpYsxrhTgVhPUuYpJ_PpvQq_rd5XS6Rkje0n1H-UGpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3LaVLW0UyovC5p4rbhkd6i4IYcYhCYdeJ7TRLBaieMhmCOMKxnwXHyn3gGFok2J_YE_WVRibKZE4Xmx6giHkRrXW4MNceF_-XC3C5Gf141ST3tHy8iP4SwS8wEkUKlRXYa69Jy-3--FyDIFO4nxhxHuddlt0c0M0z-xVay_ireNBs9JlT2-lgU4g33ucH1KQan5jUXSlkPzyTF7ratVhC0b5syorYMVISnBw7p_4CrFdaKZj6bOIj6F4LHXqsd5pL-sBfl7nNNDXgiU9I1KH9XU4GVVdm4Xc9U9pGCKRZ-H9eatkk-a4XNTkZEYsXTcwyQ-mXxz7gfcsUZ3RWx1mglE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3LaVLW0UyovC5p4rbhkd6i4IYcYhCYdeJ7TRLBaieMhmCOMKxnwXHyn3gGFok2J_YE_WVRibKZE4Xmx6giHkRrXW4MNceF_-XC3C5Gf141ST3tHy8iP4SwS8wEkUKlRXYa69Jy-3--FyDIFO4nxhxHuddlt0c0M0z-xVay_ireNBs9JlT2-lgU4g33ucH1KQan5jUXSlkPzyTF7ratVhC0b5syorYMVISnBw7p_4CrFdaKZj6bOIj6F4LHXqsd5pL-sBfl7nNNDXgiU9I1KH9XU4GVVdm4Xc9U9pGCKRZ-H9eatkk-a4XNTkZEYsXTcwyQ-mXxz7gfcsUZ3RWx1mglE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t37qk-tqgP693Q7NV3kUjUoOEyhgbbzJmnqzu24jbixdCWf0WyJqIsHCSItySi2_rg04RBoC5qKFWGrh2yOqri3_PcOuSqBERTyyjnUZ1lu6QWhVO1ATpDdRoXAtT0sGcVsYBcS725v3F-Ngy03mkgCD6WCszqeanNffHlX-gD7r9NFlPQZFSOxOVPn2rI029Z6Yfi0mkT1VSfrmVsii0Ml0tCjOIor_jPCEPZlvxUyMQtz-dHMeWRMmpVaVNwjSaXvHyYFjndz5Oh_B9_npF36xLTyeUezk2JnUUnUsAxOYBLk8L6IlvxE_aX_oWRCPiZ29WmZd30qxs7vOK3Pqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27047">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msPOh1OPKa5UFfsnagmoXwYk2YVxEfSOwMZiChUAH29C8vVMdavSCbsKImF32lzzo7HQxI1dCnrLN2bvtFIJQfyxrcu_EKHJdzETHAzg2p5jL9blOm7Z6apppKrUfUjzKWoWEyYWaRkkIcpKZ2TaZC8FcCRmTR-s77c-IybKEbFpouk4o369MQKtGhL19oHNXs85RBgtGiHZLyq24S3r3uiCEZkIv4mBeq0LZuQx29ULRge_VCyyecyLiEmydoncHZkE5DMIs3s1jhHgg5JaCMvVbY7yIAsDMwS89Yqxe9MW97o2M3IL08YGpj1VM24lfu3UcdNZvIBAgro3cRlCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/27047" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ5s12losXlH-ETyj2GoEj64rTWD0sQ2FtkMu53IVrTNXsKaBPBnBtEbQ6Hev4kIEV5GuTADMcnHU8H2NfMOs_P1DQM0rt9GdKSyLf1EA-5IeOtWjvZ8lIMG2uFr8n2hpGJXNNwTg2gusmJF7pM3EVSyrrGOhpWHwKWMRRmBOsuwjPx0Doj8-lSZ4Fz_R4iRwZk6YSTnYlCEpdImrZ-BWYYPp9UZD8hWmWe0xrUaglBxLIYoJ0sxJW1m3wTcElU9hedplZo3FICBH4_zURxpYdqpsl-M7FQZjUF9oLgQuwOIAA6mye6jHKoFVSj5O3KuzSSJwOO1zmoex5TPVy0WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTi4ky-eEJN-FWprxBMatN7mijtirC4LBjo8mUZbQHnSMyWxFIGAyMjf5RFIojlp-e0mN_Pp2pIdKjTrWZyFXHwxVT9WpYamTXLTRdA8o7g2Y67-dnoBRL_VsFwPBLWbdcpIlNEbX9gcveNATHGndGcg8Mjde02whlMFL2S8CvDVUrKZaCuafWWYaYKvnQaZPPtnp22mrFaMK83iBtc8vIDb42cZX5gndKhWKfGLtHe_-rLkc2OKEm51MAAkUOePhK_QaMW1DvlrATX2CaUV51F4zZ-wzFH2PHjZB2whLXmNZVfzidYXyY5s3hIB0DHDqyQMBMwgiLsU9fY4f8xBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=EmAFyBx_4ElpgfiN8YatkpGYOwgDQC8ScNx5ebr0w47B8u_6NkoH34n33pb4mOxET8fxJIl_p6tG8IMdF45IvMwJd1WvvHCR3lB5x0r0JnqEmUO9uKaeK73DOgqTrCqN231wZfmUbn1OjtXMiQlnz-kFNwELQI9wGJjfb2MyVt50ZcG5y_5gQT0w6ng_FS9lv0qjy1mPnxgZYNZvc7Qs43AQEjnTWarX6IphDA6Qexjuv4NyA5VTXmULvqhVp4bk6DPQwuIH4MVXC9QnhAaE0Y4oJyyznKUAYMbCrQycGvlmyt9cWIqGH3wBidPazLB37PPwCz9J1A3UQbNnbMehaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=EmAFyBx_4ElpgfiN8YatkpGYOwgDQC8ScNx5ebr0w47B8u_6NkoH34n33pb4mOxET8fxJIl_p6tG8IMdF45IvMwJd1WvvHCR3lB5x0r0JnqEmUO9uKaeK73DOgqTrCqN231wZfmUbn1OjtXMiQlnz-kFNwELQI9wGJjfb2MyVt50ZcG5y_5gQT0w6ng_FS9lv0qjy1mPnxgZYNZvc7Qs43AQEjnTWarX6IphDA6Qexjuv4NyA5VTXmULvqhVp4bk6DPQwuIH4MVXC9QnhAaE0Y4oJyyznKUAYMbCrQycGvlmyt9cWIqGH3wBidPazLB37PPwCz9J1A3UQbNnbMehaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-VH2baEseos4w0Q_nyLH33gaRPyocmxol6clW4ALGmnBOBWzlg5cFCVMwfOM7jzi_DSl2zLvG-tJZGx9agroI0im2XHdteYdSS8KAKOq2P98V5D0R_Y29xkTrN5UJFFSLsMRy-adoS5Yf67bpzdeFCCqHwjMjLGbQ9ooaWOKQpFPrF36-AF2AMd3URHTTWo3h2lDO_RsGALeU6Cgr2vdhhLQpqKxErsbeWLEPyb54Slno50jzn9ephB5iJL3gq96bOIiRJ2C3miX1zxSNtEJtnovPP8U7ko9ro4UECywEJQ_9leNCLFpP06ILiSiTyving9zi7hDvGAE4_TaDLU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwQ5OBpHPx7pYSYauVAm7SyyqcrQR12S2FVk5UJdljRJf_FXb1HJ-eWYoFt0WYq8at7aHmbXIfRxEAeVRNnX3ApExP4DPeTME4a1wjTDDLMtX9UMvgUM32h91haDItmwx_TU6vdAaEaM1vdHzehCTQKXdOc8_DlzGpOQdJhi6KpR6NPnv8qqoSqUQ78fL5r3mz0V-sTL7B5KqeZp34q4fCeCeQTfW16zyAnwz6bLetL9lti61WwNmyBKgVJKQlBGLM1WDgC_d3_LrLZKzie4s8Fj5_VOpPJ7cdGatelnJ-VMrf2bMkFbeldbNK18dAs5UPAAymJN-BBGbS_zS4nJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahm5JMMp_dTaKJXmsYQKDa3V1NSPh5fMwRWKM8X0j24b7BITpoXbDwfW9Cjg8klCVv-OrbzZ2QFkRPQL6HY2u-k0AJusCaZcr0LXmkWeJmXRb3UzNyRAvqoxvc-nY0zJDJ4MNJvZ2NeMUrkEUsBmEGfSNXMTsul-XsHuvqvswXHV6vtfkXOjSx6y88s0ojkB_ktzKhI218bVhi6jZ4bFcwK3035afobNggWo-HKIyvamsxr_Mfan0u3rhAhJIp4uJ2ANql1Av7eVlNwYtT4zNRe5mqtj15XRa4gk6F_r17csQCZsJnH_A1u1gV9SOOaksA1Bem9uG4bYm4XYDFiFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWKlj2Q2SNYbehEmjcLUYnrHSgprVuOM1pt2IRf4FXPYFXjZLrIWfJgRAAEVuumICY5DEfo-IPQbsjR_nnj5WME0DR82N-lCdk8i2yjx4LKdzJMcyGFeVJNUP4cH4yyYb5RwLoa3IkqUTbnCtKaEJW3MrS4mshSfN1a-ivd06Un4BSlSTFVkJZHsNFmpc_1dwRB0821ApZCtBi4RBwm92PXyDaI6M9ZEAlLgBF9v0-Quoyk2ePItr5TPYKLysaJ116qPyVGh8qYKsKfx0RVKwZrPWxVpg7kAnDyL-NieIqJjKkjKnoRxeakHKPwVzVy_37XbjSnMR9QNFXCi4w4TLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-rNqPJcouuWsOqSu3e1kTCiWohimJkl7w-0gfnFMujmv76MM0DiSewLNNaGke8riyFSzGbKlotNlkMKZmJAENGvFVQJ1n9u86FNiH8wPrGDDvP-BLcBveNIGRAHoby7zuA6-eyh3PZ5x1-FvoRujEPruipAQXPpC0z71gDJ4MFE-dX7bB9TnR3nVPURkGGOxdPomZh9OhqKSPQTfelD0p_RbXgEatHyQyYpxJL-CW-uucHpzai7DjkAwVFurcUDKljw4tAG0zVOZXvWzj5rdbxEakzCWdYfZL0B51aZ8zHGQAjpEXZLPMb4J47aGnXH5o4tynconpXv9HbydB-lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5EGC-36J6cPMSMH7yz2DedDrR66rKHzDq_NIhRGQl3069m7S5m7N5oe8zhYyYIsh2WeOC6fxr2rTPIgb9eXOCyUz6NK08Ss1JSmJGGqvV2Pa7yJBYEK5SrCu-GgrPerXnCTuHAkahjVKqvTqA6ab4sw6nWeWAAb10GIoqGmeKigVbJVFTuhGWSu36uzQ1qRQT21cB6NcggLe-kr9bUqHzUhcEaJ-amYE4NKKUXhxlkNznNCBg7V4UkZbaN2oeHHfQh-IGR1WuMtPQBfNfQg4qfbhvVIPFRhJsckTTtcf1wxGoapYjCzblpUy4QBSii79PWDY3WtgZy_YU6MJtCTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFA6-I_HHcCFGVn-0kd_wF7_vF2E-YPA_HSp3eLBF1roahFI3Cc_F4oz_6AGf5iuHMRi6hi2073fxYEm04BSBGyp1NrjSbqFA_gVrllktv5VLHUWm20XQEj4HSJsjD8o2xyXKJTVFF464A-BljBBn2zS48VO4KDtQfYax62RFxdZ2HVBbqmGdagzwaN1XeXpfYTljGUKNM1lWtNS5LvB_Is-dq6NjwGXq0BDRVUkoyCJcfyyjgjMG54YRxHq7O32ZmQyQ0SnVHuwizAT-B3o-UwvtZr2NN3E_fOK6BxNCh7I3MmZHVOxIU6Ah0q3ZveJKD6vAuH4y1phExXFZ7g4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvkvtPvLbNxXMvPqOx3nCzzCxgX7xfKnfpdw1sAQGcgX8GNArXh-UU6m-5cfGHL8V5tOzJexwEyqqbUjqFa0F1aTriJ4tINWaa_iXef2LFuU0lxM_R_Uk2VbtMdunPIzNgD_RL2FRrU73vHM0jm1T-dPBiEcs6HGnjjThkwwuvdVFmitSSzqN934nH9gTCihhlAzXVg7SblL-Om3O1P-8m7BwR2vKeBTlsk0aLe3Y4bt2fsVXvf7QcjCcTTd6VghnVFi5nGlVGRrpPE45qPg8iPdIuCccUs5Sm2Sj6BE5nB7O8a3WFeDfLS_yEJVCs8xJi2cQfzRbEUe7h2gmx1JpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=bKWBaWbo3hNW9s6r6bWwgTus5ClTEXv1XaZ5N6i4O01t4zH42SdOKe6IVnBa2rCRw7dsvAy6aDUYdHeOiwBczG_aqWBR9eyTZzcL887YXUro55Ee6Czc3Jb77p8XY9yI60Oj3SRM4QLspbCcqVKNgTEcfdASxiAX7MBNoITtdJTiGUYKFm-A_Uhqtb3owX7faV-7FrSzDD8__2u1zXV8SiD4XoH6CY0xcCJh9KMdte8sNu39vB-thCNZ2lFauEYbEYBYxr0w6q5LE7FldyXezp8JKqwv_Yq6hvvcGwRnVdq4QVMo211IDXhl4F5fN8X1XHt6j0g4xtMNn2BsQ-avZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=bKWBaWbo3hNW9s6r6bWwgTus5ClTEXv1XaZ5N6i4O01t4zH42SdOKe6IVnBa2rCRw7dsvAy6aDUYdHeOiwBczG_aqWBR9eyTZzcL887YXUro55Ee6Czc3Jb77p8XY9yI60Oj3SRM4QLspbCcqVKNgTEcfdASxiAX7MBNoITtdJTiGUYKFm-A_Uhqtb3owX7faV-7FrSzDD8__2u1zXV8SiD4XoH6CY0xcCJh9KMdte8sNu39vB-thCNZ2lFauEYbEYBYxr0w6q5LE7FldyXezp8JKqwv_Yq6hvvcGwRnVdq4QVMo211IDXhl4F5fN8X1XHt6j0g4xtMNn2BsQ-avZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371eeda394.mp4?token=WVWHg8KdGYsPwmfM5yPVEQPpf3CbDam7soEuel5T0WljmVw-nJzb0LmkuJZOD_HAOM8032ebutGXhCOKtKuCjg5IK9t1SO5uwVJuoNQS7s18nwMrfdUYw6q_6b9qYAFZjTzd2wHiBVcTScNpZS77BMZaZ98c3hRvds35xFhA87e4wEfVkmel1-iVJZ8ApAjJI_2a7ym8mvGRVZUGDxZrrWltpHbyhxREGXGwvJ9W_zvOL6v3fh1zXHUsBkS_LpLnZyc9lNgs8b6YjzgXVzm-VlLeci7PJki4GNgYiWr3iUd_Xhre7eFMB3uYZz3zvR6a1hqhxnzZsB7X5D5xd2u7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371eeda394.mp4?token=WVWHg8KdGYsPwmfM5yPVEQPpf3CbDam7soEuel5T0WljmVw-nJzb0LmkuJZOD_HAOM8032ebutGXhCOKtKuCjg5IK9t1SO5uwVJuoNQS7s18nwMrfdUYw6q_6b9qYAFZjTzd2wHiBVcTScNpZS77BMZaZ98c3hRvds35xFhA87e4wEfVkmel1-iVJZ8ApAjJI_2a7ym8mvGRVZUGDxZrrWltpHbyhxREGXGwvJ9W_zvOL6v3fh1zXHUsBkS_LpLnZyc9lNgs8b6YjzgXVzm-VlLeci7PJki4GNgYiWr3iUd_Xhre7eFMB3uYZz3zvR6a1hqhxnzZsB7X5D5xd2u7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
آرتور ویدال ستاره شیلیایی سابق یوونتوس یکی ازبهترین‌ پنالتی‌ زن‌های تاریخ. ببینید چجوری میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huvTI1lTJ5T0fa5iHuckWZP5AJEIR2hSOPVg1RjkgFJbvG5QxYJO-NokWhKRjtrClIG4YYNiINFVlGofcWDyI75_hJvqfjKTG8yFq3SVt6E70U858U0Xk1LA1n2y8UjZwQIW7W5kRxyMW41LHEC2hfIwNHVwAUHQtvxPpO2r0_gapbEu2u-mLqN2ciU0bsxBCHUEx51F0BGxQWwe1fE6k0HU6FbZfMYGX2ieAk69ZOJDaVzKef6ZgBaPOUF5C7_P2bJq-6hZF8zgqBrFExsTPnLRjWewFlgyUm3RXvgcZESjmLdr1110ZEd9Ee-qb8gjHZnnoZaA1oLM5uj04b0Flg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=jHYJZAC_1OxYHmCSWa24VX_2eK1a785YF-_a1bk_HPCPDLCx8QiM8LpII1Y7Lx9NY-1Z6KXvI0h_6geGhbSebHa5bsg867uurO4GwP_omdyrYmmWcAZh1C3VFbYcaJUQcFHR_UxZ9vuvh46g0KKtVQ-WSpKBwDmeZCXot4lUO6AABMaU0XaFZwKbRYZhipFv67qzQnKIJVpMFUOU79QaDMXRu3wHOCk7dTDr3ssz-wI9MulUDJ1i2_2xpLZQwgnF0b9NjIaF7TU0zdMcELOjFUG5W9PjaS1N-U5P5zPrxphCBC9r4c8-PcShUuZl-ts163vEACAL456ABtsNESfOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=jHYJZAC_1OxYHmCSWa24VX_2eK1a785YF-_a1bk_HPCPDLCx8QiM8LpII1Y7Lx9NY-1Z6KXvI0h_6geGhbSebHa5bsg867uurO4GwP_omdyrYmmWcAZh1C3VFbYcaJUQcFHR_UxZ9vuvh46g0KKtVQ-WSpKBwDmeZCXot4lUO6AABMaU0XaFZwKbRYZhipFv67qzQnKIJVpMFUOU79QaDMXRu3wHOCk7dTDr3ssz-wI9MulUDJ1i2_2xpLZQwgnF0b9NjIaF7TU0zdMcELOjFUG5W9PjaS1N-U5P5zPrxphCBC9r4c8-PcShUuZl-ts163vEACAL456ABtsNESfOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODVKBsvp33LVPzlWNvBejbR28J0kJvnIb8nfSCVfLG8t4f3NgIb220AQ2zEE6N3JeUfS9jlv469b-ZUemeHA2-L1aGA78SjxxlAnfJInAoRrwruJkVwLzWMZEhJE796jYjHMWAZJIIeqIVqId47i89N94u9xX0cOVXalckTg2qqiQOSzR9qlOq5bTiq9AeGeOlYTt26aX8rCWcK2hIg7arpCi00L9MspHiOZwnWg1TqwVYXdMukK_CVfRa_RoKF7IsjAohPhzghyY03lAfWq7dwLPpGmL2y7k_iSMbo1pJCxmINRK9zgZam4485xVWmNAUJ5wZ_wXYM_G0-lwEzVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMXV3VYGb73K0vFtmL5Pf57-jq0226FVbi76ZNbTMaWQlcWkIDYzixccL_rdZw6NU350YjmWNUg-xA6Q0Vle2f5X5JTRRYmhKYDsfIgCvVylemSA9OnhYSxHkWLBvqnEGnlanVjkc9HH7k7wCAGG2CzH5i_idOpExpon9Sv5lJ--HzhqMslkkARaIgLqKtOrKbzDizAw6bFNw0tnLLYwp5oQODygrL_sxXmM11tA0eb0aRs6I9wkbbObl52auCWGsJ1m2xQdRA8j9saRNLARdB8UCf6NeaPwUdwlERgtoYuwaR1V3YXWUo7qmUTDdAUTszH9FBAQCXGZIS0nPbqX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJo9enwt4zy58rIfDVqfnXv3kl7voNMgPrEsI2ERojZtXbn3__8m3DSrF4UOpYszAh3yBo1goNI0Uq1xZXD8md_5vwzitfS6b-Mvt2ljkIR7_ecJV0NuWGRHot9DtBTKyzmFI5ADPswA6LaydP-4m1B9QJFQjh4Hw5nJrnpcqHTEfYbXBHudv9jvALFKWMq_IcPXQ3p5oqdgQcHMgkLX3sLs3drSes4dqI8lBG_gNHGOdZC4vMFuL-YrnYZW2Y9iTaVGFJ7Oo-rgl15YqDnDD2Rz8d3tfZ_DHXwLGQYYxVxVelVVaTb2_lJo6R5Gf3noUuD-a76IaK1wHCpLcRYE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0AKEHVxaRhZK1UUZdxNVs9PBb5MRaz-cujCXOlLZ4c_PttON8vJHaZ0nwyaUyan4rAe7eEg7L4nopTAAqrpEnbGzIhtPHgZK2h8bTykdurj6j-Yz0HyGLJHTYfCGQBUR68aESYpYhpQtDFGDVkfOw7aCga-qKRW19QXpv5Ut-DULw2c-Qux6vFcj1zMD9CvFN50DNwj1Id5TAtD8RkMVp2bn_XGaDo3b4lMxbKvixP2v1gfRu-SZQpRALdf7OISaLWEZTPAoBW4S5UxTjHbHyPpMbqPPxSzngnrfG3Kqss7qc1gybwZ2a_6xeku9nsmDpPkYhZ1FsEv2tGGu8mJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mes7OGWkTAMIN169w8KBJG_sh4houu5KyWO7pexV3zsVnD25Dhtm_IotW8iiNWpBT-4ci8TUT0x1g-mrrjC__v9fmFdmesykSow9GL3X3xlXXjZWLmip43UUJBN8MjHplBVJ-TfKTIkUF8QU5GRNWaGLOk6v6X_cGymsngeBkWgeFhtnD-Io7dmWt-QhwYqcEa4B0pERhR6JlT00tu4c5vmDmZ7kRcMJ0lJWEBO3Ow6O3dCxDHkXmk7iOvMunjuQQFFKdpQ34GNsXLL3vtzZaxcNwiezEfcvx4VGIojzfFYcuHRwU8FUalyJuFC1i0y9Mj-G-HSqZfdwjZQTjnYz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrNzNh6bV3tJJcOW60H0j7U9q01LECRyOK85_LUZ1WU8MLoOCotjh1GKdtMu3MQaA2zzWTm9IUkiFHtPblVy-XbdLH6mJTGjSYy_69HDkKVtMSuOdulPw0N_s7v-BMaNeak9AxQ68UB9Lqeh4ZvIgHF0FG3BwzFFHmBZ5JHWOKUNTEuwCl9SBCue9vkw8yLsgEXKTETkuuYSCEIwyEc-i8_t-zt8tlj-phr8wDv0v2nE8ZD7rq5X2uqEt-PP0EBuYncR20XtuF5wvHSmrLIfwWbiSFQ-ng9TfvCbqUQX56QJLkVdgXiV8BDnCStPvn-r98N4Dq81b7_FsS3RQc8jIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27023">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGo9NwkkDziBUxWOOigOqedvpCTetYt1SPhSLAi7Sy1d_OtDEOB-_xLA6OFmq-aufafP6ig8wfIcGzKC5SqKU8M6DH0Xm_yIAdPK2mhIjMuDv_q5e4TeXD5gUXhkQDFrwzosk5tmhxfvBOyjmny0iqMmTpQUi4pybpkWT5LWDnYsxtJHrG5Uy-nQ0NurlY3tnQOlDIG8J5y8QkCLZk3k4mLaBefhw7gKpDBLA97lNABzhcuwYOBe0YYP6xB7lv5ztVdrpsw4Bukc4c_b23BsX3FYmPXqV2VNmcK6gZgdX4gjvbaTGQMFyvHmEQKMYgporijzk6X7xfOSHl32Ni4WPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27023" target="_blank">📅 22:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27022">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMMKvOvdjzx80lvPNdW8CVDcDMz1ELu288W9WSclaAoTxdWoVe6H-sMn_FU77sjpGJVPmjeFffflNY1dno2gWSGYVedX5L-qKke_d7x6_Yii0JbH2sVIplGomTBR2iibL8NCb7oNEzfkMLUmDN6RQEJQl0sz0neWy2utXW_yga5tpR_6zotFanGoKTFBR2F1XSZBCjMFw8rkcF9KW6o-Aqw_yBakY6zBgtxp_eNbv465tkX3T2S9G8Q1LmFaZ2zOErVNSCm6DolBTIy_Y9MnkEKh3f2Oze9cc0SnuIu-sXlQV3EpnN6hvVQxto2labNI7wtNlGBje67Zap1p6TlNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27022" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27021">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeW-Un5NLT8YjVcH6CByz_AaIJmsvaw31-7b8nK2I7L_C4Nlpo7Sx2cg7clkM-o1rqPAn0EzioEQHF0kja-mWmUljuRa2oyE63sGnjtaneqgQo3uGlFFK6BDN9uYeOk4Hv1XHFNoxndTx7YWJzcZhAJHbEJI4vnTjipMIxuS2jdYlTjc7OC9IJnqZ85uBH9fu-21gm5JTiXWycQsW0kY7AxNwV0I51H9AVjrFl_vsn84In79iRjkXxnRtxsk2j08iEeiwhettN1l4XMVqN3QCsY7kciI53RctF9qLSUecxeIPQ0X0eEXu1ZrefBFISJybqFmd9X-Xcs3gbJ-J-Zqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27021" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27020">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjGulgGRZquHXDPRWDXxV-vMy9xOcXzfe4CFT6FgmPY7KXpK1OejKL1DDFowRGjpLXIkplUFMweVQP2_a1D4Gj5qKsyZ4EdDrnwEu5pYIrFTTqgBGp_TxyTBeez-cYIjSd8kutWJRDEqn2kqKF_X1kISWphvWdw3Ki5EzDk2Vjt35cgoakkm8UnVJDT5_sU85F-zER2qm_hHYIjdXuOY39Cb7SYt0lgszXcKWbo_zMez7I6CottSMxaDcGtTdGIpajLUXEKhPamY10WaDBXFT_JkRzgq0M6OzVj2OMK-15B-vUk75C8rlClsUIdFMoLQpEyoZVnb0PjAvmEd-GW6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27020" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27019">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=qP88JUVm2HEFcLuoUx6otWffHwSbFiP5udcLdCjK-5EDWAzWlDo9Qy0Rmftlyr4PIYzBh63MpuWrshZBCTnVigqbHXIQbh03yuxDCrqGt8MdkLi6Ykw66dK716lxkwTXSJdIDqhNnmuHjb2wdOpJqVtG4Ls_wEDaIOAtgxjrq1jmFYFyM40V2vEQ0yufjg0Ztb7_Q_JTBnI1V-No-uUwNUx-TDgOvC73AbN2W_Ab6uP_-Ix5WOqF_ORGaWUrpPgKIdtoB1GQO-ERtz8_-_vaRt3ycCfeQ7a6BTXVlkMtM7qbqaW83ywUQ7bXwRhVyOTuxE5zQ4fcSe-ffHRDwsrpKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=qP88JUVm2HEFcLuoUx6otWffHwSbFiP5udcLdCjK-5EDWAzWlDo9Qy0Rmftlyr4PIYzBh63MpuWrshZBCTnVigqbHXIQbh03yuxDCrqGt8MdkLi6Ykw66dK716lxkwTXSJdIDqhNnmuHjb2wdOpJqVtG4Ls_wEDaIOAtgxjrq1jmFYFyM40V2vEQ0yufjg0Ztb7_Q_JTBnI1V-No-uUwNUx-TDgOvC73AbN2W_Ab6uP_-Ix5WOqF_ORGaWUrpPgKIdtoB1GQO-ERtz8_-_vaRt3ycCfeQ7a6BTXVlkMtM7qbqaW83ywUQ7bXwRhVyOTuxE5zQ4fcSe-ffHRDwsrpKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27019" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27018">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRML64vNqrdwk_xGQgEF6CQhv9oWzTsMjmk9xwYNmti65FtA4wpiK3PQjcnTX-WH3dkizz_ZVZkzXKMRhDBcvv-GVCIPxYKo1_Vq5SLpN9X8T6frO2JFjbjjxfqL96PLVTv6_sEeoBgj09PHL4vF_jDfRp7Z5LHLufYr3yFMNd-pjh5dSqvxHToEPkxlTBAR0svmLX-FPD6LCA97Sq2ydLXGS7lzT_d314wNN9wsUiBG1oNhhPM8uaNhf61APvTgbwkNSAZWph5Ldj4aqITmYwCkvWtp0lBn2IVqpL4GkwdGf7fB6yCzICvqMVtA8t1-NdhVaJjqqJMhbFAlUQT1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه گل گهرسیرجان‌رقم‌رضایت‌نامه امیرجعفری مدافع چپ 24ساله‌این‌باشگاه رو 70 میلیارد تومان اعلام کرده است. مهدی تارتار بشدت دنبال جذب این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27018" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27016">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu2Hw68RqogfcpuztEdpHZ7B6kMoq1Bl8Jz660q_QQNTPbUR-wCcUWDi_BctUH0Um9FtwhjUKoC3mVe5HiVoJfWk27WxhtJWRIUOWVEPfv0K2u2tqik6N8HbrKD8puVUDgjcw-ASwwF5oi1xEZHCQg3M9zePYh_VsDBt9HvXE95kCbldtTjUIS8fpxbqiCHu1QIAtKH1OPyTKO6gR3vaCQ3clKgwWBz3GG-sI1t8GPRbaxadONuEGA90aei2W11VwI-4nXRKqSXde_0WQkVAsDUbSuVVsBM6fQB2eW9BLF3KGt2sC_fxTWpBYq_MTdbIwgrzH2Pmwv5FDblANRQ_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق صحبتی که با یکی از نزدیکان محمد جواد حسین‌نژاد داشتیم این‌بازیکن‌هم‌آمادگی خود را برای بازگشت به لیگ برتر اعلام کرده و به احتمال فراوان راهی یکی از دوتیم پرسپولیس یا استقلال میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27016" target="_blank">📅 20:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27015">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtnqiEvNMF0c5X7eslOduDPgGqj_R_1pX0MaO8qV_elNJ6jV069I5GWHcr2f-z_aQ2CkJXyoqBCK7YNnmEf7WV0QlU3KBUD7D5GjKq8LN7Hub-Q_Q2LfF5eqr7FQOqr6GhnxVpSSPDiD_n8S6-ipRaC41OxEy-FxrhN4iaIj3fXiHeWhVW7mm99G34oXkn0JubKxGakJFwfOrW3mf2Z4pP66fsFXl2S3_FIIzDKmzwRMonA_zaaYnS-ypWnyKG7YPic0VstxGNfuaBAqFBNmtqofOh37Qh5ebAn5Tn41xw20Kdrd1Z4Q7JxeYTK5b1sf6PXDjb0H4ovIcaXewlHi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو درحال‌آماده‌سازی مراسم ازدواج با جورجینا رودریگز برای هفته آینده در مادیرا است. این‌دونفر در کلیسای جامع فونچال رسما ازدواج خواهند کرد و سپس جشن‌ها برای مراسم پذیرایی بسیار خفن به هتل پنج‌ ستاره و لوکس ساوی پالاس منتقل می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27015" target="_blank">📅 20:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27014">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-lrXivIsqZPFGKxIlb6qUQrn5kwcO1cNSfUk1ZkJbom7CuHlnQgHV0NTrQjT7x4aT6T_3liigQRPo0dyQaCt3xYkzItqTMxBhICChGEdR0aF1mGkLzBSQXpNdyIpsXsXREi32wpqjQrdtV9Ed73yOIy3XYIpLLkth7BfDI7S8EpX-CNt384ErxKC8ENOcgT722PuwW24tRUhaffXth8beFD7Sz6dFob1cYyNqgnaUU-iSJ5onNIfLjuS802nX4lOaDly0EyfL5vWalUk2Wat5fWOX1sNb-bau__YgcocPpQ0FNnNWGdKslGTuWMUfoh_2_IxDjyuMZ1pJnOpkiJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27014" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27012">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=K4UMRLRL-C1BR9Y3Umzf7BNyUITxkGzC9fiAV0uS16Dkkk7uMDJjBzu6xKOGfNcWynDfY7oa99RLRt5NPlATPk2v_7d2C4ZX9UlKCiF5a9KloNEd7ybLj_v6uluSbeD0EHeFOJY7BqueqZi0ew6jpRlB2nr8QryBbEugSTNRTVG3nH8QaInn9e8W0Y5AtfHnHoMn22RETrTJj0f7SPUuHrmLN03ZxCw9z3KD5bGjA737fEuUXh1CK0NAejj4nSEIqGefNi6dRkdS27J4-ZjEaCS6MT67V8pH9Xmtk5XNUsIL1yKTdmUzcPyYUJsyacMxJjHxRtCqore__woNX34snQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=K4UMRLRL-C1BR9Y3Umzf7BNyUITxkGzC9fiAV0uS16Dkkk7uMDJjBzu6xKOGfNcWynDfY7oa99RLRt5NPlATPk2v_7d2C4ZX9UlKCiF5a9KloNEd7ybLj_v6uluSbeD0EHeFOJY7BqueqZi0ew6jpRlB2nr8QryBbEugSTNRTVG3nH8QaInn9e8W0Y5AtfHnHoMn22RETrTJj0f7SPUuHrmLN03ZxCw9z3KD5bGjA737fEuUXh1CK0NAejj4nSEIqGefNi6dRkdS27J4-ZjEaCS6MT67V8pH9Xmtk5XNUsIL1yKTdmUzcPyYUJsyacMxJjHxRtCqore__woNX34snQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27012" target="_blank">📅 19:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27011">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJTBDYqYui-oKgoRzv-OUhVRurjbEj9heVyTEYmq8upzEQq4oP5bFURDKVgWVOygxMDtP20_8jJBUt7LW5PHXiTN3WZQtfN87QORtZj9NgSoJvIl4pi7mIGTHaTIROzw-CfVPzE3hAPagOpa_ATYez3jIZqcWr1Ci2TKuIrExmPXWaWGE7Ez-UWebdz8xij1wE9SDi7JbIboNyR2FCm9BST-zXkxBxH-wmjDQwegQXLRlHYaL4FxXzy0Q458aEKxGjYIR4lQAOqXumv5P-t_tcYKXqzP6g0pzd21wQius7Cv9aQMWerRhWrVwHBSLb6x3Dg24kuz99w1h58pn2DlNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27011" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27010">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7FMdYyTL_Pki8dOTGcDAQC3lKdBXWswmuDjA0aVczE3AHjdZLBkyVcZcCIAGEyyYd9yEjeIUPUyOKJ78oNRTIUK5YoHp5KqGR9g_Z_GULQwofNJoRuTV5ho9NhEy9KUrhy87vv8w9W6B-dOxITDgzh-VxEXqu8Te7tFWguy4acA-3VFLNETvO0oGgFU24wCU_ObQkZzEG8FBydPyppqPs-AMoMiCDLwqfiTwYKFrFD22HrG-a4AJbWbGzzCq5u1nhgFVfQ7AcsPGTp7Sfo4okR5TBgiH03HyU6rVFAg17muSBbe5ATqWKgh1_DsoPaevw22SnGaz4OWefyaiMCpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مریم ایراندوست سرمربی‌ سابق‌تیم‌بانوان ملوان عصر امروز با قرار دادی دو ساله سرمربی تیم بانوان استقلال‌شد حالا زهرا قنبری کاپیتان تیم پرسپولیس به مریم ایران دوست بابت سرمربی شدن تیم بانوان استقلال تبریک گفته و گفته خوش برگشتید انشالله فصل خوبی در باشگاه استقلال…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27010" target="_blank">📅 18:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27009">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP1BeqBaOZi4K38FRHenY_tVHHseW6PKJS73Yd4mUB3O_gIBnAH3pCJHG5C6Y6dnuEbfTRuRTZPPmi3D8z5i2lWs2cAhkRh_aSKM-QcmU_2MbYYMFYecErjTrtUbwWWJoypvCz4xPVoVeEySyHRGYbuTYLzjCIj9Fk_Nmg49_Jqu-vd5uImnQi7FogNiI8XovghDmv7DpJahOCm01iCE52bVLgHxkOIRuiEzC7n5ovcnxiYs0J_51JKQuUo2aIFGMkTKiUc8hPGivYAKz-COr4JHHbwm18Y7QWroddg-LXldmLZ2qBvxVZEnpFnsOe7Js97Q2WtRUUETao_NPgMoIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27009" target="_blank">📅 18:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27008">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
در فینال مسابقات لیگ ملت‌های والیبال لهستان تویه‌بازی‌سخت و نفسگیر موفق شد آمریکا رو 3_2 شکست بده و مجددا قهرمان این رقابت‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27008" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27007">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWnKBYc_pSm0pVR8OS5LZeHmO85X7wg0M1E6DiF8Ndljc8Ur6lXPgNnaVUOilb7a3aN-XC-87eAoA3wDzUOVMmyt-J4f-5O3amiqKl_rwYjwR1WqZeVPtbfZOj0_TAb_qYNifgwkB3y0j-78aKCJbj3hMKT4LMLVwHs8mfM_rkYsFDRhOjrtKHygPpIUgngVO9NY6ykToinPRk0bd9e8QeHdMMWAPCR_DvNDUfWWDVTXwHfYmt7QY9I5Y9ffh2EzqLCzvW1-baQWVzUZelXT2XKamS6GW2w2DEHm89PJTq7oMfGEaCp0W90FNcVhxCmOlWgyxAQSPiSolBd3f0OkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رده‌بندی‌لیگ‌ملتهای والیبال؛ اسلوونی با شکست ژاپن به مقام‌سوم رسید. تیم ملی والیبال اسلوونی با پیروزی برابرژاپن دردیدار رده‌بندی‌لیگ ملت‌ها 2026 به مقام‌سومی و مدال برنز این مسابقات دست یافت تابرای نخستین بار روی سکوی این رقابت‌ها برود.
🏐
ژاپن
1️⃣
-
3️⃣
اسلوونی…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27007" target="_blank">📅 17:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27006">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=Cu_Wp_L2Kzhj9PZbez6cAq81m3IqL-82zk-b9c3GOWBeR7wVXDCNedOdaQ__0olroFD2EF4CWVlGFWRs_XMTzsBRUoyxeUc-YMRN_vq8V2aIZ3mu7Ut8u5Gd9EK27pfJxDgQCLMCiHxD6wmGbYDcFl7GlzFpt6aKKDwneBJdRXj31VDp9tS_vuxgnObufX9HP0LEVifQQuV5bT-O3Kepu6etq-5YE093lTrdl2y2odB5IWXkRLUl6EjRm5_xl_1neXs6QBkZUKQOCL0Ya84zi0OYDUR1m-t0KD5xQF7v8VcKdDXiYF3RklNg8e5MNrOfR2Fr9zojSSo1oDp0qB9c_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=Cu_Wp_L2Kzhj9PZbez6cAq81m3IqL-82zk-b9c3GOWBeR7wVXDCNedOdaQ__0olroFD2EF4CWVlGFWRs_XMTzsBRUoyxeUc-YMRN_vq8V2aIZ3mu7Ut8u5Gd9EK27pfJxDgQCLMCiHxD6wmGbYDcFl7GlzFpt6aKKDwneBJdRXj31VDp9tS_vuxgnObufX9HP0LEVifQQuV5bT-O3Kepu6etq-5YE093lTrdl2y2odB5IWXkRLUl6EjRm5_xl_1neXs6QBkZUKQOCL0Ya84zi0OYDUR1m-t0KD5xQF7v8VcKdDXiYF3RklNg8e5MNrOfR2Fr9zojSSo1oDp0qB9c_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27006" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27005">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIQLlZgFOkGJHyjmcthe7YdFJ0lhCgRTx-18YrPiSf_NY1VwHCSEC4Ri1oxWxUnNwOdvtf7aG4-d7-OqIJaXcAb9roZUzzd7AnV1jzr0AbJHq-sSfLv285wN-uY7fDkMiZs2PAoxKJSAGRZ9BTsnHLdUeBqvIUeQkYqT8vJgE85T8mnHDsAZzfzitDOfDzsYPTbk65onvlQ0hkREzrbQxKc_dy8IuFw3Xuho5LdWJK6TeWnDHHPSCMCry5aTX4M5xLz8b7Ztf_-dCA9Ru_4Btv_qh9vSjUhzQiY0ZLfD988eQUknC3OYfsREeur6EYD87SkF_y-mR3vM5CqMRsohSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27005" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27004">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTTAPPjxRbz-O3UlZ_hkAxAhrbwQ0gR0sKI03iqHxHtdyL9DUgv2kIG-_0DGFyDbBAadoo2c8J_hALm3jqyLxtO7cqHWCNRYK49Hle7QSNgbjs-vav69Mz6TCrmyYYLlSCjBp1Gfk6SeagT7VvnP0kvby_leftVEb0EeNODpwDncDfDLAXzv43D9pYMQMo8TxEu41BlKoLe7G_9u7mml0HE2vlW1AKuHEU0zkMOeq6S5L9YUGRjz4IIZTp5m4XSkis2UHt2gZg_1ll5m5MZGDEO3OTgkn6VWzA6Qq2_8XNfSs5M5vQ_hz44BfCIHMd0XkA9cCe-9jQQy--sFgaXJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27004" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27003">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUNB287OlyQj2GOMkFhurgQZCPSVZ2nZYwRywODQwQtchiFqqur4wRM1nSzOotOUUmQS5Kx2cALg8k8z1sHoQS_aJ16X8ZeIPdlPZir0ZEqKOBFHbj4weqEmk8mJI4ZReLFnudOW3GNOP1VCGt9AfUFTadODWuLv7tOWwZDLxYiFjGYZMN5bG9QOx6TkabnEGkoPZxCSaBftFZH9WEsHoEYt5GMFMIZlA1WY-FTuIJCi45MipU2TfLTLyjOSRpNND-GvumSSetgRHqQt-ciqvWaUj0N8-hw_e3_PHTDUhn4OaDnLP88tknkhfHXIQF-u2ViKLObjKUlzNfoAPuLymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27003" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27002">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKBxM2JgWst4Go3yyeo3gJoGv5xWRCUfEQHq--WfFgO4XM6ul7COgHZHN1Jkl0dHWz389SBcs4M55FZqfYbfpzl8EFmcq9ZApaA5p4HDLB3mSZ_802_9g9MEHGdeyocnvreTY9okJfnAoDJ8_vDSNuxoi2JZ7kmUVu6bdKuaNUVygllLwG8hsjjJ3cY4OWAMb7zLXDofnN2Wg4oT-92tI_jnsp-jGdCsd25_bmYmdVewghh7fW4Ms45rLnWtKNNHo4YGFranqL1PqN5i4IUmsthGzU6lj81Fu6XwWVEiDsbqFuMnp-4jj8ikOiikXEiPpLzPBWM-YKJ1th4sAqjL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💰
گران‌قیمت‌ترین بازیکنان در فوتبال زنان
🥇
آلیسیا روسو - آرسنال ۱,۸۰۰,۰۰۰ یورو
🥈
خدیجه شاو - سیتی ۱,۳۰۰,۰۰۰ یورو
🥉
الکسیا پوتیاس - لندن سیتی ۱,۱۵۰,۰۰۰ یورو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27002" target="_blank">📅 15:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27001">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc5Q3-HltpAEQN5pO11H_rx6j9LLrSxOsTHgrKUeZSFl3DQGRpSfpXsOrbjk4G9-hvJf3k7UA5-estiWtqEcsihabDlDsqa9OPbIST8qq6XVySZ3pjXQ6D_nWjCEkSpT1Wt-scfiMPMgIHo79NyLLdTd9SqbuXtXZMM9STLnDEwn_nDkbtqzj4PR-1aCBZuFSqpPhHcc37VZcq70i8E4A9c0OADbS7mEaGkh3DiU9q8OcFmrHM33NNllqC8vtLunAG8UalFIogMcelTjpeXpmUhjTi0meOtC11bM7sShmkrHZn7PXhghOuPRQXmk9td04dfpStuMgdLPZn_gaUKNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27001" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27000">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0oTQZm0Ob_Mp996SKl32PG3vBs5wRj0W_FF2Uun9HXDLQROffBoHzICLgaYuFV9_GgDkSGDuCptrj9-LpxPpBKMK7wRsVZ57x6KS4Pv1AEdDXvjbmZDwSTEX4kjUsdxYSkskYbdHcJUc0ftUiCTySKpiOyTN9CoDerfj38ll6wg6YdLRyMhfWjjtZyLruLZZm_oAsWCXL8RXEMO7QvnjUEdWP2lsGIxuOLMQLBmLb6k40Qr3_3zma_MO_KcLKGGmNwnO_Pc0AVQJkhDz7y8RVPXoIqvbilCbRhO-lK259zPJ_Y5-v4Nk-HgvVnmpd4xI7mU2Bi_5gbBOwhHE03PSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27000" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26998">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGivhny3AVk2mTNotCtvf4TrubEzUxyD5DG_t43muNLMDn-V-vXWcbxJczCtnT89lQMR_bzx2i4PQDuvnIVviT2G0waKzHcM-gorKFWYPD8ZAMcQB-Bpj7GQHE7larSeZHolWaw2ZhW7xvgHL3-ZYB0wphu7sqaz-a8ag4BLCSUPYisZWJa3vH0wZiZSIxrplsKkk23lJ4zdGIaRixpfsl0AHncvYrVRMS6mWW7GOdwQJLY0C7InicMGhBALBmVgJAwsZles1UkKUyNI34MbRTTJLWv3HDgy2UuiDmRYKn3nZ0IxcMnQSBy8f10HXtuJgGW1-W1VUTu4jjKF3QWNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewM-WEhnZETRoyWESM1wQFC_2N43ziLnL5HHUzVoyeuutIYkO2ctZeaIE8kk_CRi1DkbEBM15imCpEkwtVuQHfeMHKEkHwn3xyv-XWEMJYj6b8GjcEvp27XSv0rAb3CUn3jtGQ2qYmxuHRQ-gYFtjKGPMhC72QVFwsWd7kHP_Xx_4HSsnYAA5UFS1LC0NPAa_V9uS2ZwPwCFY_3ScNFe-xITToGF12Kbwyl3pWGH50amt4R3NrEbaQcCNuPduj-woCU89AM7zPb9bFXGnV3vOxwSwjSyc4V9EoxsZqDmKPNRc-0qR-LPTwcuQGDtyHH71DOKCotkNqCuuZx4merOBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
کریس رونالدو و جورجینا میخوان‌؛ مراسم عروسی خود را بعد از مسابقات جام جهانی در جزایر مادیرا در شمال اقیانوس اطلس بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26998" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26997">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5ZFVkVf0Xd_lyxL3mo3a_1MXmlEtpzV_I0efrJn6h-486wuvonYZliGnsWtY5ReVLbHnuintLCVn7ThC6wx7N6KG8Mp4ZG9iEK9EegBrH9dBQBXMStx4PSoH9tuuwkMm_2Mr9BCFRux-cjrZglPO1kLh024wXCM2oNIBlHmAOXBBsUr6foi3fB-f7DrwRJIozGsjm9TXv6mS_o_zsdGE3usEzmoj8RAjaEB_N3pwOIFLwH08ImSwVyJu-baIahdOBQdEAvBE-vdJl5oybblM4aADcTmUzAEBVAF-AcFeK21fW1nF2ZIpTiGEck9h9Xc68LbLMatoVcjBKbteuGD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اینم از توضیحات کوکوریا: خیلیا بخاطر مدل موهام منو مسخره میکنن اما دلیل بلند بودن موهام پسرمه که اوتیسم داره، این تنها راهیه که میتونه باباشو از بین بازیکنای دیگه تشخیص بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26997" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26996">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKXvr0uKtARpGDmsfckjwq3UXlAj0xBL3Vx1NuLOl6p8Ma3hZcZ0DaKKp-jyoqJCUat3iz0P8inm8u-neOJO4iWppWCFG71EBHuVLs0CxqC15aAH3CCt-iAlWsMyo9eJLCobZ1ihQLmKVcBrFZH303pol0er55XoCxFeB_C35LkUl_5iWUiDJDyFEXF_ty8ZRaRLehh5wnhyL-1F6HU61CTw6B59IW7sKNnF0yM1FrOZPGXxFbzAQRuQAc9sS6IBfYTIV0_qwf2QAU5_AWVR3PNrXnK3jqz_x4RZjdyRt8Ha3drmsgDpREYNTvKZPFoo_XxZPHs3Jx4SirTXGjK3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس‌نیشیموتو بازیکن تیم‌ملی‌والیبال ژاپن که باعث خنده خود او شد؛ یه لحظه تعادلش رو از دست داد. بازی فینال هم ساعت 15:00 شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26996" target="_blank">📅 13:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26995">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=BGEpc8-ps7yF70_ADbSe6liJWsU3NFE9Uyhs9joinqNNPEcXOyTS95HL0Qe2NjpBSf8-IB835vg7eX02EnnOE2he6DbFpG8dmCMlsj1EobQVMYtt5rJFIEFa8SxefVmMuvVx35B6sxixjuyE9iX2Bx44Zsk0ED5G-REDXk0__6Fxsk3IIw2CM746Ii44EaLeB0mbj6I_naC8S9UP0f6EneoHj4WpI1P9k7PIRAicpH66sVkCfpUoIKc8rrVX70yaLMqgHEe9SglhvY8RUVI3lFi8rl3ctTJ6CVefkckDy-2H8gFKo6nSzBUlHG_S3ZxUXN4NMRx3LFMpgnVppw804m-nze2kNPrrJW2SBwD_5ov_HhoMX3jTrmSZjz6nQzklm_LvZO60vjBmuN4MPV7rqDTGFpQzM_WSU6PVaajWI_AafsFqK4o7hs0IhkKPAesohIn5-jzYLMedudcuqPabf37YZna9VnBh5J8bbBLK_gOmaG3-K1bfx5dx_6adyXf6L2Q2p2ZNil9KmlQp2JCzTftMuWNezA_BTPSsdoGgAiKJeeCf2CO8-uTekyKMGPqDX1NzEydarq1cNxEDnAdZvnCGLBdDTweVu9Q9w3PqNQMOjj6YOgleClMcxS7ABj-3oc9v49QYqbBb9xm9WXdkFIEYjpvfhTE-87g2xGvE-A0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=BGEpc8-ps7yF70_ADbSe6liJWsU3NFE9Uyhs9joinqNNPEcXOyTS95HL0Qe2NjpBSf8-IB835vg7eX02EnnOE2he6DbFpG8dmCMlsj1EobQVMYtt5rJFIEFa8SxefVmMuvVx35B6sxixjuyE9iX2Bx44Zsk0ED5G-REDXk0__6Fxsk3IIw2CM746Ii44EaLeB0mbj6I_naC8S9UP0f6EneoHj4WpI1P9k7PIRAicpH66sVkCfpUoIKc8rrVX70yaLMqgHEe9SglhvY8RUVI3lFi8rl3ctTJ6CVefkckDy-2H8gFKo6nSzBUlHG_S3ZxUXN4NMRx3LFMpgnVppw804m-nze2kNPrrJW2SBwD_5ov_HhoMX3jTrmSZjz6nQzklm_LvZO60vjBmuN4MPV7rqDTGFpQzM_WSU6PVaajWI_AafsFqK4o7hs0IhkKPAesohIn5-jzYLMedudcuqPabf37YZna9VnBh5J8bbBLK_gOmaG3-K1bfx5dx_6adyXf6L2Q2p2ZNil9KmlQp2JCzTftMuWNezA_BTPSsdoGgAiKJeeCf2CO8-uTekyKMGPqDX1NzEydarq1cNxEDnAdZvnCGLBdDTweVu9Q9w3PqNQMOjj6YOgleClMcxS7ABj-3oc9v49QYqbBb9xm9WXdkFIEYjpvfhTE-87g2xGvE-A0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
۱۲ سال پیش در چنین روزی
؛ منچستر یونایتد و رئال‌مادرید درمیشیگان به مصاف‌هم رفتند که ۱۰۹,۳۱۸ تماشاگرشاهد این بازی بودند. این‌بازی هم چنان رکورددار بیشترین تماشاگر در طول تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26995" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26994">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=pX2QgNFs4_ONKJgIpTAro-GBTa-39mCBtGqOIDAdxaHaoKUNNf-Fa10GK4kpm9QlQayg5ux8ajLr3ew_kSrRZkaQM_xGcMXhgtEJjC0rSzHSly-QOihrG7pvNXCugtQUXIUiTjWgiyKwbKBcMKxGORW4k8pPYNiH-BlVk3PIsHKJbpjMeGqV8AnRkJLI5ZQN00kKeJSeE0AUnWxX-PJwNffy1tz7ZEZXKSo2_LpNj_jwz1ypbZWyvBggfIvJV7jIztyOv9ROCp2AjKFlggHOqOW2nDl8cs6X1xcOofoZX_DJhJnwuDSzVhQxMn8_60dNQXO88uAcbzpTtmrIWleHLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=pX2QgNFs4_ONKJgIpTAro-GBTa-39mCBtGqOIDAdxaHaoKUNNf-Fa10GK4kpm9QlQayg5ux8ajLr3ew_kSrRZkaQM_xGcMXhgtEJjC0rSzHSly-QOihrG7pvNXCugtQUXIUiTjWgiyKwbKBcMKxGORW4k8pPYNiH-BlVk3PIsHKJbpjMeGqV8AnRkJLI5ZQN00kKeJSeE0AUnWxX-PJwNffy1tz7ZEZXKSo2_LpNj_jwz1ypbZWyvBggfIvJV7jIztyOv9ROCp2AjKFlggHOqOW2nDl8cs6X1xcOofoZX_DJhJnwuDSzVhQxMn8_60dNQXO88uAcbzpTtmrIWleHLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
رسانه‌های‌ مراکشی: منیر الحدادی تاکنون دو آفر باشگاه‌های مراکشی، دو آفر باشگاه‌ های برزیلی و یک آفر باشگاه‌ های قطری رو به‌ دلیل پایین بودن رقم قرار دادش رد کرده است. بالاترین دستمزد رو باشگاه استقلال ایران به او میداد که فعلا راضی به بازگشت به ایران به…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26994" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26993">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju7TcOvo_GuAp7QUJx5Y21Fe1gKtFm1vs403feOjPjALLzNRr5iadmvE7JvA4AXn2L7vGSHqbxfvXuk6SBKShhUdXSHl2UCWdskZJia09xFJ77VlA4Q2ofnqNpglxLmcJ2kwi242ZWe3YXFxaLyf5qLr4vnaY9VWzFUcg654fUVaMsf_oWnAiw5z7v41S7HDXX5UNT9X8Vgtf8m7SHtLw45Cof6OeG8pSmkCPZtna-Q0dpQN9etoduq63KYLc0gGUf8HI6HMgL5-1i5FAmuZqn5kNs8QVZHQBmh2LhAHjVVYC00M8JJkR8fLXWUZmiYBgX7oEVewQm2cglXvtMdTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دوران اسپانسرهای شرط‌بندی روی سینه پیراهن‌ های لیگ برتر انگلیس به پایان رسید. از فصل جدید، تیم‌های لیگ‌برتردیگر اجازه ندارند لوگوی شرکت‌های شرط‌ بندی را روی جلوی پیراهن مسابقه درج کنند. این‌قانون‌فقط شامل اسپانسرهای روی سینه است و سایر همکاری‌های تجاری همچنان مجاز خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26993" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26992">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0ByFMgANVsIL4BEayzFMgeRlXYqCcyvFv2xUw67uodnW_d3qbpeR8UZut9lZ5Md-yZOXBURYNKOdfYuKYJ23SooWN4dF_J4PoSmDiiRdcsNGIVhFc-jOGQy2gvNHjR8mkf5G2yFXB7xh_wr4rLRK5dBE4BLNkEgl80y23bC1ITr6UlUROeInHwmtFrm891TMq6YMzKYiQKYzmir1BtkKnjsmH_0oi_qlL9Dr67DLOc3VQUFNze8i_kFlclTeoLaGy3ehr5OpUqluRuzodOVp33Hln4o0J2adbGL0NGvLQ3DZ9jF2U-D9tt0sz0cPt425lSnwnbAYVbFKJX0mJHuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
#تکمیلی؛بااعلام‌رسانه‌های اسپانیایی؛ فران تورس بزودی قراردادش رو با بارسا فسخ خواهد کرد و با عقد قراردادی چهار ساله راهی PSG میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26992" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26991">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfUWLGy_JvEReYzPsyungxBJh-43Rfmx71Qdc5ee0-m10AYQ1TWIQqQQfcoMbxv98cIrdYCTqXgRaMYHV47KXewG8Vh7iuq_ymRcZ-6yIRTt5nH--xe-9W4siPkBrNhk7lVfHj1ZtFax9MfFYpmf8TixEb3QIlEgOyJSzJ6TU5OUNJuaIJnZ-Z924HUjmFC1rASn-21l3jHj1vru9WdV7JJ9kJ6wVC6qGwjyt5LSN2JUUkOzp_UNMmZ1paME6_tF5Cg57r8vOTK2zw3cImOU3lx6igzXLgS1T8cQRO-TCa_NsWgplKD1wR5XhbQCYmNk0NYwPzwzhWKVxfxRwiHNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26991" target="_blank">📅 12:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26990">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcCKdDc9EFGvH_tBb6rqR60mP96roajK8o1kPWoAb3328RfsosJFRPwp2lHcWfVcNLnfOOvvJyWX5uO7rmodfkgEUP6c3IjpmyGkubLCimXN1RRHOcLXIA2hq9rpm15WS1q5n7PFy2DRzIdqCm6Tjq1_kPo6-m5XiOESY3OHK5CsYN8uEUiC_K9DzSp9MMJX0BgWBapiO-JOJ1IdrCB2dn5_hXLhrfdZp59Iedlq4k6czUo2XMxTU6spuQIMi995-FVcPo_brIvQZZf047DRsJ2bQP0eG5favDWmudljm1cjf7NGAyxVYdp4XPhQI28Yd5zQlKHExeCIwD9_UhIAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیج بارسا اومده صحنه سجده حمزه عبدالکریم بعد گلش‌رو استوری کرده و دقیقا تو همون استوری تبلیغات یه‌برند مشروبات الکلی رو هم انجام داده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26990" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26989">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58235729a.mp4?token=unyNzmz6vB8JdN6MjGj5JBUTeOed2elRU9bXZP2zWRByqGs1Wn98GVJDVwVQ8RjJB9gn74yDhF0tOcKTpwgGc63l2xPhHA3-o1cPbRlGvveOkIHBUkeJovHpo1_O1lfraACJNIPeen9PI_Ux-GQR8g1HL8ICh2t0pCb_vKs3WvqbHJFpKqhk6vIZi72qCUGAbyh0ANxDOxthOqEr0MLQf2x7ZjJ8xr86tBHRpQO7dvFY8o-AaI6RDvRr0mMGdSZKMMIceuSLfLQBYw1TBwf4HwjnDVvjaFyKa0I_9CuV1TIsYN2_nr23OYHhXV3lBcpwdDAZNZCIcxnT_PP_z3ulPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58235729a.mp4?token=unyNzmz6vB8JdN6MjGj5JBUTeOed2elRU9bXZP2zWRByqGs1Wn98GVJDVwVQ8RjJB9gn74yDhF0tOcKTpwgGc63l2xPhHA3-o1cPbRlGvveOkIHBUkeJovHpo1_O1lfraACJNIPeen9PI_Ux-GQR8g1HL8ICh2t0pCb_vKs3WvqbHJFpKqhk6vIZi72qCUGAbyh0ANxDOxthOqEr0MLQf2x7ZjJ8xr86tBHRpQO7dvFY8o-AaI6RDvRr0mMGdSZKMMIceuSLfLQBYw1TBwf4HwjnDVvjaFyKa0I_9CuV1TIsYN2_nr23OYHhXV3lBcpwdDAZNZCIcxnT_PP_z3ulPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26989" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26987">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436452afaf.mp4?token=F-X2E5neax7O1hQ9jEfCKNpGxXnmx32tH3UC8MxIWEAEmxz7BRmPdjk2SdXf9lotHFsrlYQPT6oQcajJDZk_ybZC998ugFvJePQLoHCPqzHpibjhXRRNTD5b4DBGaU9AguMm2SZaQlS9AmCmn7GtsXFnleItGhEmEVEcD1Sk4GMyBzeJus25giD-m2MhmnQAxlhunIHDpAv3oLGCWsrMwp9xwtZT6svRSCHoDuXcDij2EHDstg1wYZTVg741IGqA1VGugm2OQe6WXyhB5bSIzEWIEd7VhIctGVGdl06gOwHkvjOtYHU3ekv0s5c5_2MUSEDVXuQWJh4i9G2x7GjGzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436452afaf.mp4?token=F-X2E5neax7O1hQ9jEfCKNpGxXnmx32tH3UC8MxIWEAEmxz7BRmPdjk2SdXf9lotHFsrlYQPT6oQcajJDZk_ybZC998ugFvJePQLoHCPqzHpibjhXRRNTD5b4DBGaU9AguMm2SZaQlS9AmCmn7GtsXFnleItGhEmEVEcD1Sk4GMyBzeJus25giD-m2MhmnQAxlhunIHDpAv3oLGCWsrMwp9xwtZT6svRSCHoDuXcDij2EHDstg1wYZTVg741IGqA1VGugm2OQe6WXyhB5bSIzEWIEd7VhIctGVGdl06gOwHkvjOtYHU3ekv0s5c5_2MUSEDVXuQWJh4i9G2x7GjGzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه بازی فینال و رده بندی لیگ ملتای والیبال؛ فردا ساعت 15:00 مسابقه فینال برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26987" target="_blank">📅 11:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26986">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFwLVG0BYMv9J9XiNxNotwO--Y8dy8AJgthVQTLZaWUfnZSJLSbt930MbcWQbZMrLHmn3CKFOnovqCPWd__0eVRKo7IMJZlAyZXqe4TCBXrr9R7cKFV32RdH84jbrWmz5JSXhU_ED5CGwARiQI8NVOTBT8p2mA-H3TRCphpTLfmMaS1FccxeZcZ8ggR13umH3UA5foOdPqhTFjQu4zLbT7UL5e7XCn7RJTq5FROOodYtsNWdzDds8Ye1WOLg9fjfVYiyceGsnGdyv-FUDvNNLXcDNxBdx6HEmwM-DCrzobSsWjDJivP_hnwpnbXDlO3dlUKhtWfySACgOjt98C_LJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوری از دیوید اورنشتاین: وینیسیوس در حال تصمیم‌گیری برای خروج‌رایگان در ۲۰۲۷ یا پیوستن به آرسنال درهمین‌تابستان است. آرسنال تمام منابع مالی رافراهم کرده و بازیکن به این ایده علاقه نشان داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26986" target="_blank">📅 11:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26985">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV2xWjHMHQkkkTHTXmElFi45E7NbWXu0NyRNw0Sn-ZZZSirge5S3NQnzlh0gYwLJAWD7FcO_6OoH4r3oEutnPC-z-7couMW4JvmoTWi_3eFDRh3B2JOu8ghESl1k6DozHIgjEVvjujOqXGPg_8SoeRtNbwOypDnmKufdBwjRhuK_YFbeXnzpK7xMX4sTgdZeL0eNuFE8WkqOOcF63xZ2QT56j6yY3sKmdpd5tD1EQ_k6oQ1AEt5pZguwdsRupYHK_Ct6l0EhpmmE8l8YRB6c-v7F0THxhEO_7LxMtjZ3JdheLOjGmrn4auBiKsZJHcdiTn7fBINBQ_FlprpW_oxWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26985" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26984">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12920f454e.mp4?token=jfulaJu8KFXOqUJZGex9A2pJ4ILpRQX-Oh_rr-L8f6SOor8QQeEWa2szUQGosksRtPw08yWRpaRbp8uRarfGHBV2w6lfvpOKn_F0DmNyWnwSNCQd9BCEhj5Ij8enxveLMr4P5_tycFyVazg5Hr_6bmIlAzhogtFLtiz_CouLiFjjedMlL9f6N2J7N4UZMgZq5obUlKZFd-akOwM80TGf7JprY_nCkbhFL-dOpBTmki3fmIx3yrX3lVg5hWjBJjMNd2E6mPcHvURaKSTbSheS7suBFtZ5m35WmWjNU18ldGazMQPNsUUsJ4AqCvMD_TtSExURY3HyXPhIp2xYyb4oLKLt8GEXW8WqUmfBU3zS1fgVYWAYzpJZ8jveXsohd2FypBwDZXCBFUut2W6YqatsjzPH0JuLm3JPBmoew_oSuFqTwquVlOqBWsFbLzvPsdpNROviqTb-dXRHJXmS58RB6_zWcLhP0wmL05oVyzMmLkrJg-ziNOJnyj74K2YwPMQX-pUoH7dtVNGLQ0PJBT8Q-4iikMIjhn4npCF4kmBJGNlXk_bDl9tjflJAUIyuhih24Cnj6VLVvv2cRiQaS8MzaBJ_XDNLF71JCD01fPQO8SW-cPY4jdElJHOZA6UowB4zL5Ndfn8Hlc124qbs8hfK-WNYWoCOBGiscMSU2IBhU-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12920f454e.mp4?token=jfulaJu8KFXOqUJZGex9A2pJ4ILpRQX-Oh_rr-L8f6SOor8QQeEWa2szUQGosksRtPw08yWRpaRbp8uRarfGHBV2w6lfvpOKn_F0DmNyWnwSNCQd9BCEhj5Ij8enxveLMr4P5_tycFyVazg5Hr_6bmIlAzhogtFLtiz_CouLiFjjedMlL9f6N2J7N4UZMgZq5obUlKZFd-akOwM80TGf7JprY_nCkbhFL-dOpBTmki3fmIx3yrX3lVg5hWjBJjMNd2E6mPcHvURaKSTbSheS7suBFtZ5m35WmWjNU18ldGazMQPNsUUsJ4AqCvMD_TtSExURY3HyXPhIp2xYyb4oLKLt8GEXW8WqUmfBU3zS1fgVYWAYzpJZ8jveXsohd2FypBwDZXCBFUut2W6YqatsjzPH0JuLm3JPBmoew_oSuFqTwquVlOqBWsFbLzvPsdpNROviqTb-dXRHJXmS58RB6_zWcLhP0wmL05oVyzMmLkrJg-ziNOJnyj74K2YwPMQX-pUoH7dtVNGLQ0PJBT8Q-4iikMIjhn4npCF4kmBJGNlXk_bDl9tjflJAUIyuhih24Cnj6VLVvv2cRiQaS8MzaBJ_XDNLF71JCD01fPQO8SW-cPY4jdElJHOZA6UowB4zL5Ndfn8Hlc124qbs8hfK-WNYWoCOBGiscMSU2IBhU-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26984" target="_blank">📅 11:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26983">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=vJ6n1D-PNA9bascph8Kg2a6ARujPqzM7ZxufrGU4_R5e0UkrCVNffPRMlzC_wmIcuS15-Wr8qf0VFD8MfoqRTa9r1FAkFlfnZJJppK07fp9-bMBzdWN_AvjjOlj25et1eGacrgYy9tk84jEtJ648ZnmODeAI64Wf_CW6wtdbsbpmSxgOAt0Cg0uiw7in0Ju1rHXy8znY8oY41mMfa2dNZ9G_4o0ilGCi72XtmPHdjYiYAnTqQQl_pagHhhGfKlmEgmVusEsgh4dn3DVO7Jt5q8PraPMo1At0TwSa7KavR4m9wWMkthMdMAZjwgYABmTY-mFbEIYCruCiKX7zfcyy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=vJ6n1D-PNA9bascph8Kg2a6ARujPqzM7ZxufrGU4_R5e0UkrCVNffPRMlzC_wmIcuS15-Wr8qf0VFD8MfoqRTa9r1FAkFlfnZJJppK07fp9-bMBzdWN_AvjjOlj25et1eGacrgYy9tk84jEtJ648ZnmODeAI64Wf_CW6wtdbsbpmSxgOAt0Cg0uiw7in0Ju1rHXy8znY8oY41mMfa2dNZ9G_4o0ilGCi72XtmPHdjYiYAnTqQQl_pagHhhGfKlmEgmVusEsgh4dn3DVO7Jt5q8PraPMo1At0TwSa7KavR4m9wWMkthMdMAZjwgYABmTY-mFbEIYCruCiKX7zfcyy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسمیرو بعد از پیوستن به اینترمیامی: اومدم به لیونل مسی کمک کنم که جام‌های بیشتری رو برنده بشه؛ برادر در بازی اولش برای این تیم امریکایی:  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26983" target="_blank">📅 10:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26982">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxJgMMXN6teNfVVQu6qEsDlZ7dikEb1HH16gWfkxQLgAQVvh_AKPwZstAURloRfTsIZdMmk1F7OoSdOwXlaIskd5BIJgeakx-qY80m9dFR5g2SfAmJ6YuWNPM6W_5EeGNrMUWxU9sroyldih-yDLCFyFcTok4VFAxWeo5iZd4WItfAEGO3uV4u99P_UdmHY9FsARyWSyttg8GREo5iKIE-ulBF_mIZ58YvRzB1BepPmsuXOifB7L1QHaoMMSiQiFbL3iVA5KxqsFloYvCVvq01_1LCy7V3gcsJu651wHgPC6CZzlT__RVd7nAqRVNhxraniCOK9cmwjDUobZkAPAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایدباورتون‌نشه ولی‌این‌دراز فقط ۱۸ سالشه!
‼️
«جونگکوچ ماچ» بسکتبالیست اهل استرالیا با ۲۲۹ سانتی‌‌متر قد، درحال حاضر بلند قد ترین جوان دنیاست و عکس‌هاش‌این‌روزها حسابی‌وایرال شده. حالا بخش جالب ماجرا اینجاست که پزشکان گفتن ممکنه از اینی که هست بلندتر هم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26982" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26981">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=uF9w-l0eAFpD8g2ukqlsyOgBaQnvOuT4oL47LXvUO3kOGIowuJeNM47tvPvqDFcS7ugEHT30G94J03NPP86uKxD23lDBVvuO13qVYftrXowTA3-DVUkZzqgcnmpf9It7EHtj6TyreQbgkx42mUS4qtpj3ZthsrAe6uNj6BYg0G0osaM5sgEseDyveilr-nXIYYks4rKedSrgoyRidg8rQgJLYUabiF7A6zUkcEndaRGeF_-uYef5oxGwhzPgF-nHEW-iN6ei-XxtK50MV4YZOWArUjsGjMHSFvZ0QvM-Blk-XpvS438Ki7FZlIPjyaQCIQO-agpO99KKC2865KXmkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=uF9w-l0eAFpD8g2ukqlsyOgBaQnvOuT4oL47LXvUO3kOGIowuJeNM47tvPvqDFcS7ugEHT30G94J03NPP86uKxD23lDBVvuO13qVYftrXowTA3-DVUkZzqgcnmpf9It7EHtj6TyreQbgkx42mUS4qtpj3ZthsrAe6uNj6BYg0G0osaM5sgEseDyveilr-nXIYYks4rKedSrgoyRidg8rQgJLYUabiF7A6zUkcEndaRGeF_-uYef5oxGwhzPgF-nHEW-iN6ei-XxtK50MV4YZOWArUjsGjMHSFvZ0QvM-Blk-XpvS438Ki7FZlIPjyaQCIQO-agpO99KKC2865KXmkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
محمد نوری کاپیتان سابق پرسپولیس ملقب به جمله معروف و تاریخی "هرگز نرسییییدن بهتر از دیر رسیدن است" با عقد قراردادی یک ساله بعنوان سرمربی جدید صنعت نفت آبادان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26981" target="_blank">📅 10:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26980">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_upBowwWbNTRiZCVsialgO8zWO6QDSL0fPvmzbyftN4UsjJ_j-30bAg01FaVXtfh81WMDF9yyNF_ErXtjLEdGQC03ntESCyFvl_7lBAoUWN9Kq4F4zfgyyjxN54TyYio3UajP3JDQ1a1eQta5IDB_NQzCRJfu772qJBFAzJZUcRMXzTNKVhZB88GPAg4zdAFxZf1GlPBIRCLGG5I6wcmWbOmKYwNSnA1B-60fQZEUBfPKQ5h2s4fBTorsLH-3jgJslrWQTzEEkR6YYDKOlxUKKBNZrxt6_PTe8GpN-naW1D3d797dAA2foM6VzQvcY7QNWzaE4_oR8TFmLw3keI6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رکوردداران بیشترین‌تعدادبازی درجام حذفی:
🔴
محمد نوری: ۶ تیم با ۴۷ بازی
🔵
محمود فکری: ۳ تیم با ۴۵ بازی
🔵
مهدی رحمتی:  ۶ تیم با ۴۱ بازی
🔴
مرتضی فنونی‌زاده: ۲ تیم با ۳۹ بازی
⚪️
پژمان نوری: ۵ تیم با ۳۹ بازی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26980" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26979">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiiNxkYcLlM-lHL4d_B6Im-Owt6WDnOexslfY-dxyQKGQ9MuAcWiUop1iWJ55KrubtGn-zIXPxWxVpKJkd5t6Xi7VPBrx5wZ2MoNL-pOz1mLYrh_dkYirhQJe0QOarqQZ85I19BfgPBN_BMgBrrMT0GxF945MccpblJWlao6DPTm_4kHMXvNYp8Vszt9DaWmso720vCcH6fcEWdI_sy6aAEw6_42DIqEq7Hu-wM1i1Gae69Q5sxMUR4RLk6sPcBBH0HHkIBETOZ8BGdKI4Sq8O9_lcJx2CjbiOkh3HKhGAhmOLIDu4Ob9l38OG0aPFwAcWZIIqWGyDcxJ9LVo0LWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تمام‌برنامه‌های‌هوش‌مصنوعی مناسب برای تولید محتوا در اینستاگرام؛ یه جایی ذخیرش کن به کارت میاد. برای دوستانتون هم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26979" target="_blank">📅 02:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26978">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxGOSWgCParUuKRCfafBIpHTplIEqWxUV9a8h9zIHB27TwUU7lw0-N2TN9moapWLUys48Jb8iE4JSK4MPFC_p3ABfCfUKkq_60KZ6cbgFtuJsF919qIHhRnkDq44S3HFZOG3OQsKhPqWdTBZnVQMvJCPGaKVbzP2lZriDA0bVxjpbrzLuC06oDrNi1R4CHpuApQMlZLLE-iHHbS6XgU0yB7g4QVoGW8PpHfzaLEcWjRz5VZ6WzpkdVd7cqyoRkIQcL6aThbKdrLfIdXoCK7FpxdiIz1cBHdyamaHIe-DO6aAhC0qkzl5JHUwy0VQJclRxbXY4YxVhEJ8kM9rxkyiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دپورتیوو مونیسیپال پرو که به خاطر بدهی های سنگین در آستانه ورشکستگی بوده و به لیگ آماتورکشور پرو فرستاده‌شده‌بود در یک حرکت خلاقانه کیت خودش رو به ۱۰۰۰ قسمت تقسیم کرد و هر قطعه بین ۲۵ تا ۱۵۰ دلار برای گرفتن اسپانسرینگ به حراج گذاشت. جالبه بدونید تمام شرکت‌ها محلی و حتی هوادارصاحب‌کسب و کار به طور خودجوش اسپانسرشده و باشگاه‌رو ازورشکستگی نجات دادند وقراره این باشگاه به لیگ برتر پرو برگردانده شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26978" target="_blank">📅 02:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26976">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1wy0DVOS_iD_uU5R7J62mXujhCr8F3R1q8Zrnn2dV7SmT4rp0MHL7P43IHp8_OSxI8Vc_BlrlS9sb8cRyBHQAgUzPLrPas2YfbNSbys-AYdL2BRVqnlwnOrBDXSdDx3FdXoE69mssTn0NfwW7gXMwh4TaHUd7CuD9alM512HnDPswdLjfsyBV3WU6rwxevr5HAhxmpf-VVAmklwUYas3ysdlMXVyHCgknq0wzu7QmJJ8ZUd9VQEr6lmNHI7y_KlCFgU6qoziZ-ZLGsusu7JIS0iUCkzRA5lDJlLHkRuA6WTDyqsS52UINmLOw9hruqNdSHXaI4hs1dGSy7Qzu-AlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
بازی‌ میامی‌ برای بازگشت به صدر و دوئل‌لیورپول‌ولیدز در اردوی پیش‌ فصل!
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26976" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26975">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbtMYsbrqLlAqeGNtowxJSymW1_IZZAm0Skt65aVGFrrhgm1gtB0gUntBz_T44XOGbNKotMfxAMg3ttlGxW-PamVV12WRvzZjfqZ5jHES4Qmad-BHmz0july-AVveYduIECqmVLVX7pm7YTJDLxxRMa9GqiKE3ponaZuNGXdpz1SO8Eb91-2ZYXot52OOPo1tG8smUE4Dofu7VVMk80zxC__4lUfTHD7fiT8STviAALIB3s6J-cvbvzK1-RSjkBKYDCEc9j1wuXq8hrBP83C4quulfAGO5jdcOOkDRk2txYLB5cBgV8ulv_522HUepj9c4BHTjfYsGXYMq82t7qA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برتری لخ‌پوزنان با سوپر گل صیادمنش تا توقف رئالی‌ها برابر یاران دخیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26975" target="_blank">📅 01:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26974">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mal_9FUgGTTon8-yzkskOYZHIKMvMz8tYLVVY8kiM8Kp-agCduoz95b1qUVYVWOCjb0fdAUIvWgKSXbGC5oHklQm1RL7E_G3S_iSUTx-vKobUmX-z4DhDcZG_gS0D6HRu4IXjHuE_QGu6sSAw5MVFYUKWDEW4mNKVRJZTJc4hNXthAeKsKxE0Azzub-MfiReZ_QfFiAKFAgJpq175bHlw4SBoiIyN3JlC33ttqK68M03J68YUmogSDfPupd3HxQZmD70kLJumWbzzlEHQGuauPSS1J1IiVKBvfJs5YsBslfgZLfR73onDrQMMOUBdV-cBbvVT6VQRSJKjACjC3KfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26974" target="_blank">📅 01:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26973">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzWcRRPY-Je0Fty-8SiVrSxIqHm7zRIASMPtAvAlBmgfJffjVgUDuD-LKC-ECT3gctG0r__5qsKxq9GRqf7NOxO0RebZA70-feu3w5c2VveNyXklKEeu7XMTEXSpsJwDmPgmM0MXcpB5fhv-2rbgmcvOexnv4MKjzAttWMu0YZd7AA7iilMFxLkCiaKcG1HfTpgD21hsKZAxtA4IzOQfbr-NXS3RT8l87j6TMKyzPiDNX77MNAlB7GCNPcGDCKajh5gAeAIrkXDqw-i6zlXWceNtSI1cTgtRcjU29rIk9coFegeuOKi5dCH-1ndhgoOeUMNqqAj5PNNq-HQyLGdnNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون مهاجم سابق استقلال: دوست داشتم درتیم‌استقلال بمانم امامدیریت هیچ علاقه‌‌‌ای نشون نداده. بارها گفتم برام بلیط بگیرید تا بیام اما باشگاه هیچ پاسخی به درخواست‌های من نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26973" target="_blank">📅 00:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26972">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UumuifdV4gMMKHStXgf595OiwwwA0Q4VqW2sFMlGjcclV5h8tZVUa79jUZsPkIVUhfpoM9fdZ6amKfH0t6SdE_6Y8Y8e114zWC3HgCX0_iGTKY-ytOOCqYzS7hXfYMj9gQjr2_UXLE27km23zUUixLwXxX21GSZdedwLo7OKk8fs_QzGO68MEfq1U6wp7REcorYkXVrF5degSAvi4rxnIJToAnpBiYlHS4gKAOLKtpnELgalR8ZrQnDwfebPt89YTIZeSpwjVHaNMbhXk_ZHoKdA1vXEx8fMEhutJavpO0nX2o3mKcjB1I-Bq50P0EdDQPs3lW9eyg2KbVrtb4_NxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26972" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26970">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugyN8fX4cVHPASwf7_v9hryPOLepITGldhdSdyKhrkGarzYH_Zeza6kZAtGop_5dlziML2se_VfBlf4cL6TOo9oarvTxT2Wn9X1gHqBXwDubjkrPHJuwuhxYsnLq7klForgWfLT9Sp4RT92Id1WRyE9Qz0E45Q4ScMPiHVw0kkVIxEH80owu3EQSLEGhKtSHVswOSRx0zNWRqWVHpIAC4b-uYaoZAzaQgJUfYjd0JbF-dm0PSJHOCVBcIT9PHoVoCT0sTTcWAnPydrmnQRBunWukoVPrgzZnmy-2xGy7_QwW2gXF3MiqGkzWKxJtGH9bappuXYy1vHVa-5ClNf7aWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQw1Wrt1ZAcfk11Jcteh0c94rX6l39HaOlRWSbrPuRA9ePROZUPRTEVHZBfYcknIpamjUr-VQi4ZD9b8jQtcBWKwm55r8pHMVuVWUE5MBOSxJv5SU8cz7dectCbMXsABUDCJaav4eX7-4wUf-6K3aC5pWRH4wdaqSNWgXxDuipSxoLPNC3RmcNb3aDOOTpnOM30hSWuQuJ6Wn9RzzY9YkI2Icw6XhLXSjaruluDTjcJt7S7-K790CbhmiM8-88xneg4c7izyR66swDzxPSnM6oVQu7VdWUNexaVcnZd0NdOnzGlYqZkUrCCxjkOXKQD2FdxT0i8TzlHu-Ggo_GCQbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دریابنگر دخترخانم 20 ساله محسن بنگر: از بین بازیکنان ایرانی سبک بازی محمد جواد حسین نژاد رو بیشتر از بقیه بازیکنان حال حاضر میپسندم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26970" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26969">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uau_qOEZfKdZ9mmMIrhkW5UOrFr2VE6kw-VHIH5QbiXId7ndv0SzPRL_EXEPaFOs1ZPeqKXQD9qncaSMLm0ekcQRCBnJHTof5EFwjtihssjTqZs0VIWbcFOfM8T-Zs6jm4EEK8FyAxiqf-oTktNFk8bosd5eklFGxu_j2fHhXhKJ33Ng0N0bncO0m4OItyBe8ymKZNIqpPunCT5J8Biiyi9S_s1H_dZC0pSimQFDn9Iv5pXWo88dvnLJ3dTK7Q65Jfgbfa0PNshe087WwfxyFlgRKUilZJTUVOMrhD76WutwV_puzak_EAyYNXTL-XS3LdS6Ch-8CBGLKqmjQmGFgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26969" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26968">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrPZBa6hxprqdUz3K7QXeg7pesikIJY-GfGxXhg8HPSdD52Vjx3HiJkNfMCp43aAsSYIACdy5KNpJ-RLwyq-aXXtaUKIshoKbbFcr2SEyXl6yuHrxeLVASJTzHPLg1nquKIB6AhfKFRqiWj_M1uhGcGf3Ftij3Yj-x7z-bzN_bawgm1GsPuF8Y17_4_Gyi2DP0htaUqQemeLoz_MYNWicaIf51QcYTA-jrqEoAwqTrtTqoSnV6N5VK2CFu0qTmaWBYlzYwoRyUA1EhoLtjWN0675tvxc0CrueWgIine_1_UYNuRh9Pugje05q__6mXsf01o7bs2Is0mlK-s9jFoPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های ما از باشگاه پرسپولیس؛ علیرضا اشرف مدیررسانه‌ای سابق‌پرسپولیس‌بار دیگر به کادرمدیریتی‌سرخپوشان پایتخت بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26968" target="_blank">📅 23:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26967">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChKvcuFQTxsq_N05u_SIzOZ9owsnwtalhc1AMDVMbfmDgWviH81SqZwjeZLtksY-raz1SkuKnetbvpzYuuw0TSSLrC9Cog1uLtJg-Fyb6sq-KSbBQyvV5vEpQhIdI6aWI7eiuwSTos_xBvM2iebw5j1mcOlUEg4oucZb41ETX7UrHfIEqIzsfSsmTDmkW2kCBoSH2gyO-DhiyRaEu2wXozEmo-s1NxVXnsKUo8AjeBB919ykymfKnGxNDCTLtz8oQ7U6BTGtRSNHL6pMC4gVUXQ9y4aTbhZoXdu5FX8XlLWZd7qirbws4o0ruADu6arta-uLWdk503hZWNLmzooubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26967" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26966">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTxzirONpCk_8fuMkxKFONp8XkshRmxOyRbe6aSwsvfrkxyeU86Nhts4NT_iGHatFBB9SMhfbjsg9J6tuPeRdU8KfP6AW_qc_Z4_Jt-lqmtlc70JaPJYtaIBU08flcsuXD2PIxiRke1QQ1DFySIYukiP5nF0DP09Lcv0qoQHb4dVTmhsNcFFL0MA-F5wVrbfqYuVp1rpqrty4D46jmFS3nAXyeXeDJOnoczEtX26JaBlN39gTFuq7sK2HHDIIMS2PvcezwiGpMpLwdnqJ3np_IvPSLuWzOJ0jbrQhYukFgI4zB_RY69ijUuk2VnGJqYvZJek9L-gDQ7dKgSz4WtUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف‌شایعات‌مطرح‌شده؛ باشگاه استقلال تابه امروز هیچ مذاکره‌ ای با آنتونیو آدان دروازه‌ بان سابق خود نداشته و برنامه ای برای جذب او تا نیم فصل در صورت بسته ماندن پنجره آبی‌‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26966" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26965">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4JFpk4aXIS5RPjdnsVRjn4BzwKTcCp913XOjtmjtD_pLLcEWKjri1KoLGHSnK7_tVhO1kb_RwjPWIqnKChkUS3_29tB66mLGv8q8T1D_5B-i7mRUZimbKWVSqBx1F8TcSQm2010TcS7PRfwzDDcB3rMZSf5hK6c-B53UCNkpsrProC5tnav54_aL11j0IaEeac1FqRE_MeaL-agkzm8Qd09F0w-Y9FkX5zIPYFXa25pyHcDJrCXW0nATspw-8zYWyqb1Wf5lqjm_rO0RsmOVN_BB_ir-Z3G_-njWOKTLytu01kApRAPQacXz9ALM4NKpzzEknKc30XREv4pWEoXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید شد...زهرا خواجوی دروازه‌بان تیم ملی بانوان ایران و سابق باشگاه گل گهر با عقد قرارداد تا پایان فصل به‌تیم‌بانوان پرسپولیس پیوست. همچنین زهرا قنبری مهاجم تیم ملی نیز سرخپوش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26965" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26964">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMRExq8uRVHnjiEnLNa3aAswk4ZV492BrnHbwPHC-0bLFGdP465cXotqaQzjsvxSP0RTbgbJ0-93IuS6nYYrFTjyY785LNdAZGmqea673t2JiTxptxZ1o5nj9-UWgWuxiRGOCkadnzecA9tPiNhuqAtGLZgSQvUoiSNtHZxVSF2lPGb_feBVdhIxvuXYBq-1mgqr060DN2x9vTvpsh1wA8zHJRJGY_5a2zrISvws2-qhRnzN_Z3hVpgo7ykGEGh6fKq9UN4Ie10tsaL8EldAcGciFTwqTslESxDvpZcw_3bvu_VDgPD8MfNU_Y8nxOJsC1Ikt7hm4qm_GM1wfUzlAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدید
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26964" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26963">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEb_OqyxWFLA4_PoA_5VsTJ351Vq2tGfDdIivjJSInqD6ZXBWk2uTbMpVsMYYc6PAIYSZUb7WassFiR0B4wF5NPqRIFn2LuL6MlCV5WkEwhc3IZ0cMhTXesgEcWpKoxdzhumxmN8Puo9tHp3ixMgtehxrO5aoZYYZsNSmjitDhR-a-JkwVTS_hVoZaUYDBvtssr_NjOJY9ep5X44r8IIj__aXGCIEwCTsH_Q3uwXpd4JFaLhGCVEijjDL2RBovXLNtI2kxz2P8R9PRfnhGA1Ltr1g0ElxVos4nHaQ4ewXKDPSRT41KCpuzFg2TCQ-Px_XOmn7-GCUMECZDN3CfHldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26963" target="_blank">📅 21:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26962">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq6kclZk-OXSeKUSuo4mHK7jEcZbc30u1809jOIWv7N5c6EWJ_fEWC6UAfkEnVxErMa6gOhuf4J4XwklDk6XmFaP1oLUej8XEtBOZjLH5aiXZlRIt7C0HvwVTVvfvlxJ0mG-_jYDwt4SjtjWm8JzgZWL464fMUaa4DrOFYwEYjZDUTOS2VBGNPY3vQ3KTETx4klwXojzQhuSVA5lpObvxPSj9VM7DxB1_k9J6lyUiEF_ZWWuOITGoETIqFKta5D437Ej56SwTHc7tWHLN8jBtrKXqrcjboNF8aOAbOb4X2uvNrgsoEhmBxlucT7pwfFLRt5YZHMsBr3miKYZMiAQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26962" target="_blank">📅 21:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26961">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJJsyvmOC0JQOp69Ukss_mgjfoXlepZaAIv3qTQZK9t7l3V8WwwlUuB0cyYYrMb-SbgZE_6KYajT1VjEwOqtpDkpt1oBTHl6caHPfZ0jtZkIcqFyGFGHoV_qUqKVn6gXQv-HT22cK3UU32ONQ6cig_aTznaWnq3q3-hBWAY8nJGNX70N8ypzwaMxWsMeGj7tR32g0q6Lu5DKrOX_h1BtChuXU1tWMespgHwiboddmoRXEGlbfDSQB9Y6TIypTsmeltLLof-grpVimwd0sQQuxpru_4eLCdlDDNqTaFOZUUNsyf17LSZdgCtkcGvpdXw8xNDdlgAQOmKIoWBPz-sKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ های رسانه پرشیانا؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ سنگالی علاقمند به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26961" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26960">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkK1KYabpG5Z8NBGHKCifzC112CcvIDohatcGjCLnu-HnPCUNdb7se5apCdc7GsEqlT-gmWqGHQaZjQWCyquEXJEkN-hupHbzsmMb6dkDAdGbrutVowx8bsdTjWPuPwfqSpAylpbu_0KF7ZYolIh6tcsN_7NstP9wSxDQV4NkZQBgW2STaZiWuyxMIzt093bhns9PGNSgaVJbZKPRReTNAOKOE2wlqUAIOtUpx64lXFclN5F4VFoXdZkw1wFGSNyr6a7WaNoQTruwqdpj0zkCyWU9Xb3-c132LzODyS3mbCvE3ZnViJa2YyOXsALTvK3B0LF6W0bal9FwFqfLQhTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26960" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26958">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=IQZIodCf7Fr_Q48s_Zty_MzHYOgoi3dtK7JiRYch58ep5HszIWYHJ0-0jTYak_aN5iABw2R5mDMRmXvm88KaN35yqzn5wOdOUvhtPNfw_8HufjRJuLmFxYXuosSJftQBRF_DCR4CxkzaUhdOtFgmE9io9m7PrFYm8MoYtsbEbgr4CTTquggQO2ztS2cIwp4Okd_c1xqzSHN01LwODPz2i8OLLnqTsfIHgPN6ospzvWkzXEIoA6h2t5dKB-nX9uHSVODC3ttOVYRlSyc6nV8Qw6pGXRhKVf0xxjFZPWKEOaTBc_ptxDXXpXl6GSiHKjdVIkwLc1gaqiLrkMPBOEN8RBdT5IZ0plmSDLVyQvtZ75GjaSZkAjnWGTb-lNniKaFqGSjShHRu4JSYhm75LO-9K5-srX3VCT2ZWQCl817kgbR6442fSbe4yEK7I4e7hqVneS64G2Hs_PfboQM93b7Cs1lYjDCx-zksHIQIiCZ8YLz69fNBDMudfD0cRsH7wrfY7Ppe85vpuBhPJBuJgcUpTj8VwrWplnql_k8IZU8LTDCuP0i9dZe_FZnPqKqNnqFfSyMa_XLvfGTQheZ6VidWWx_Jtpzf7IFH2p9RK6g-uDyJryzURLpnkO-HyAKbYD4rZo1iuANDV4VeJ9YJtsd3QWAuaNDB92ozQcAU2TPtYAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=IQZIodCf7Fr_Q48s_Zty_MzHYOgoi3dtK7JiRYch58ep5HszIWYHJ0-0jTYak_aN5iABw2R5mDMRmXvm88KaN35yqzn5wOdOUvhtPNfw_8HufjRJuLmFxYXuosSJftQBRF_DCR4CxkzaUhdOtFgmE9io9m7PrFYm8MoYtsbEbgr4CTTquggQO2ztS2cIwp4Okd_c1xqzSHN01LwODPz2i8OLLnqTsfIHgPN6ospzvWkzXEIoA6h2t5dKB-nX9uHSVODC3ttOVYRlSyc6nV8Qw6pGXRhKVf0xxjFZPWKEOaTBc_ptxDXXpXl6GSiHKjdVIkwLc1gaqiLrkMPBOEN8RBdT5IZ0plmSDLVyQvtZ75GjaSZkAjnWGTb-lNniKaFqGSjShHRu4JSYhm75LO-9K5-srX3VCT2ZWQCl817kgbR6442fSbe4yEK7I4e7hqVneS64G2Hs_PfboQM93b7Cs1lYjDCx-zksHIQIiCZ8YLz69fNBDMudfD0cRsH7wrfY7Ppe85vpuBhPJBuJgcUpTj8VwrWplnql_k8IZU8LTDCuP0i9dZe_FZnPqKqNnqFfSyMa_XLvfGTQheZ6VidWWx_Jtpzf7IFH2p9RK6g-uDyJryzURLpnkO-HyAKbYD4rZo1iuANDV4VeJ9YJtsd3QWAuaNDB92ozQcAU2TPtYAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
پوستر رسمی باشگاه لخ پوزنان لهستان برای اللهیار صیادمنش مهاجم جدید و 24 ساله این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26958" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26957">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpfUxoU_GJrb7Di2pg-tF_4wiNdqQ_qUg8uvsuP_42L03B4CCc2CqtXIeV_2LjzIq7ZptNhh63pq1pnevLAEkR8rtQ0L0G8Ur90CR5iPSGtIU4a2X1dk09F7b5vHTeuOqdiyKnxgWBtnGNFEYY7UJ6kqGdfiIl_seNuSGmdj9j2AWQ4Ja4NHkCSK6cbTi2iRh9gOc77rCUieGSzQlWbVT-xaNEPHf1RczOsUJJ2M87dqjDfo64a6VIbpCVQnBPhcfRDgorKKzEp6lb7i9AZjDensHkr7ZYfHjJxKiUeKrnPdra6KU0F_o6TtY2QkBHYNxVANym0Sbt-ij6HWpi16ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26957" target="_blank">📅 20:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26955">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJS3vn64JSUlUs9lWLoz1tJkUeq3UTHWW6eiY2QZ8hECi6NdrmfbhFeLO9ow99X5BRWC0VnFeeLpAqd1UBIbifaBrLsrkBOLfzEm4juyvIWqMVyl0WUfZLdAnuNRJySy6rUjQl36bgOFfGx8Vttkxmmv7pjv_rqgTcXd-5YJFaVvOngXlQHDwzcqPEDBJb5QgnLE559H6QA_x-6jo1phL_gCTh7xBHu4KgPA7McYM2-sBXsxPtJdPZy2qFU_kLZ2v1Z7ZZe-STY73xURl9LYuTcIQp985eMdMN0ehta87NZuoRuYWkDQ7jyrvVdQD-SyJh2-R0ctwKYB9zRyGNI7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gK0UAh-vK6ZabZIG7T38LN1FURY9p8KhShTikG62NTZpbgubRQAdGvnlH8RopEPqV9leqEytgOvooib1IwCqsrpMJwMBczzL_UF7PCOTyazQmQkKEujm6VJ2trp0ZQhD1jGPhhcL2oQN1VFMLIEgU-kgXCXKq-ZijvasCpcN-PJQaFg8NCnl5sbhZOvfi-3PMm9Tf0IDqsPCKBdTQJrgLuagtqmAEmII83RRtbC-Xs2EWQCQz01XbksgPMrANnRVH4z1Q7rD1ZIFSQ5LHeKacAxNXuH_bK90vBXPi9GNjNZSjA8a4-tCX1hrCApInf20iivSEShFG_pCJnX-7q2RXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📍
برسی تموم اپراتور های اینترنت در ایران. این‌‌ پست‌رو ذخیره‌کن و برای دوستات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26955" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiZyfzd1aviMkqZFA9PIK3BQrYLDpktXUL5DgW4yuETFJTz4yh6vGd-Komuf3rjkQlmtATCEqiRbbVjGNz-5QrCqAaHAmkb4MNq_cgM-iCfGaJfPMs3hPHZ-WTUGuYDOTjc2Cv0tqM2j9P_zXXjstDwZKoiGcEQ-etEn84-QKyOnPUM0T_9zHMjSDHS7arxRCfQWQtFVa6MLpo3GF6LOUaAIAvrTOdjfyj-eYELPSdGoBo-ywan-QcilEBxCFHLXwObsJkiWHRolMYnKPm0moPT-GynP0Ad0KoD4GDbQv673OXkfTHZULCHe6URd0uEq8BDvc55VoOgrW3-si7LyWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26954" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26953">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSaLYbUQ5_A6-0BnM_j4B2fAMwk5oKiyW7Mev8-8Jjq_IFdKfYfCeVkWuX35NOFuG5jWtDEXvNY1otw0CAwnUMOyUFYuNZAKRSSkj6wgRsEAVU6YX08stYbvOTAyBFqOSGVcFqYxZXYk23lRI_TOqq-y23PUAf6birVZTJqs9c52P19y2KA-bLFjETXmmxef8R-rQ2jAX-cehN1dBzjWiSD62Vh9UDzDBTxI_I2m50LCW_yqn02UjfyouF9lkIeRFqFa83cah4tlt7W-GnDuYyvF3Pw7yPohlPK_tiwQk9uu36fkXV-XUF-PKQN6ygq4PvXMkZF-yUjEmMHvsvDF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/26953" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26952">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=tUdyaBwRb0Ty3f2cIqi6obezeFqVlpM0E5Jv3TEqV-9gmUtkwpAwp_H8FsYMuj5MbO9ZiYphZL8gd0nph1xe2xgQV80aIE0a2B47CAdunzM1PYZ6Rjskbs6lH7URoLCqDWbqneb5gFWTQ9jVVc5spcLymH2h-qIkEsVPESNkvcuzBz6gdvhBTFlnj8EHyeR7gJ1pS2vPfDVj4_98A9st7K8n-VyN9UDEg8fgiRzyH4VAYYeGnujkjry29JWXq28TLKiqT7xDmDx3J6Jw0rPidJCFJRGSWyRClk_5_UodAheNd3JOYfQmDBz7hfPy9nqQKkXqXzIEGbo8W21pWtZr5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=tUdyaBwRb0Ty3f2cIqi6obezeFqVlpM0E5Jv3TEqV-9gmUtkwpAwp_H8FsYMuj5MbO9ZiYphZL8gd0nph1xe2xgQV80aIE0a2B47CAdunzM1PYZ6Rjskbs6lH7URoLCqDWbqneb5gFWTQ9jVVc5spcLymH2h-qIkEsVPESNkvcuzBz6gdvhBTFlnj8EHyeR7gJ1pS2vPfDVj4_98A9st7K8n-VyN9UDEg8fgiRzyH4VAYYeGnujkjry29JWXq28TLKiqT7xDmDx3J6Jw0rPidJCFJRGSWyRClk_5_UodAheNd3JOYfQmDBz7hfPy9nqQKkXqXzIEGbo8W21pWtZr5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26952" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26951">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWZY5fV5a2u2RjOR4ooDbc6Fc1TFMDo0KNrbmWkIA3-KRUt6sq8BcAvu1IbesuhEOnQbfoJpZJwduDYoQmhZ2c3krcQ-aqbXp2lcTyPTZuFLoLm5GS7cQRV7lUViOEqxf3M2527Jg9qppUd-BE6bAxIlY4SlLBpyjgFpQ-dSHnscKeFWZ9I7csfQEjrN_qIOPo8tv566OBZbYh-Id-kvXVA7sZt6ebOiMHmwDImSX9Fg4UiubQ5YWumOM7NqU_ZI_kEUwkrZ1Xt8TumBMX4tMQ-Fj5UjHvJwncem8DoR-i7CCyPKAxiFc4w_sj0638z7U2s6YFzxrZ1Lk5xaCQYKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26951" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=sf5z0ySighbSJ-pWpdK8ZdvRz4QCXr_9fDLmoUCwghNBVrxGp79LwyjLZCDFCC4r39tJ5YOTBkN_yfNYdq1kzyjTIJTxMiCQVti_NqzJfmc6jPpIiSAhByNfQxe04rV8m9HiTSD2KYzH6kvTawnkDEWwxlNlc52mSMHmHfFdFfSYApIE0YkNMrCgQsrLkfbqvFaoEZB27hFgTkyplzF6-wgxitwAXdV0Ax7TO4SLbjJK07kDxusNOe-Xqh95A2b36kWANsGf2yqMls03sO-B6bihgC3o99NQQog9eJs08cZrKDs37wL2xFoLXiUfJx7awyt4v4Qnn4CsJSSOCNEzZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=sf5z0ySighbSJ-pWpdK8ZdvRz4QCXr_9fDLmoUCwghNBVrxGp79LwyjLZCDFCC4r39tJ5YOTBkN_yfNYdq1kzyjTIJTxMiCQVti_NqzJfmc6jPpIiSAhByNfQxe04rV8m9HiTSD2KYzH6kvTawnkDEWwxlNlc52mSMHmHfFdFfSYApIE0YkNMrCgQsrLkfbqvFaoEZB27hFgTkyplzF6-wgxitwAXdV0Ax7TO4SLbjJK07kDxusNOe-Xqh95A2b36kWANsGf2yqMls03sO-B6bihgC3o99NQQog9eJs08cZrKDs37wL2xFoLXiUfJx7awyt4v4Qnn4CsJSSOCNEzZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fO_9cQ9-LP9HihhKrZLXIJkx2HXZQsvfBb7hq_v1bFN6AH-RYFUoA6oJ-goC9xTdMkgVeG5CCh4cfzR67SVerLmkkDqEaSd3r3qgLtxr0_t94IufgiaE66G_chFFUTtfzbyJqEsPAdIj2yPypc2fgT5QjPTDxbFOz5UMynM_3daGdQBeYL4Im9aad_gUD3yebB4-XHNG9a30mxah-mxyc8ncmcGicZSOOBliA7ebjtUoTPZu2nF1Z7-hlaEpYTaMCs9N-OBNZjRabr0GMWoz3YXLQii4MmivsXvGC1o_G8HJTUPpgClKFCoCq60hujkLALxqYBiMvYCcipbv024Ggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
