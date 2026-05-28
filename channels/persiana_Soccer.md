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
<img src="https://cdn4.telesco.pe/file/Ryqj8MYsapvntTZpREfyy1ymTA70YeBMOZsBIgYH3ffSzlHmY8Ixo-wpTDE8EEmhiEo3kaxJLotocpdUs8o-NTNV05hTehGPSeSxeWMsS0YAocoqd5AHomTXkElPrykZeXi_PBMMBFdgstZQEZGdhBax1E9PeDdgYU4cOe9N894XFI7ZthQGCOG2XrHD-_n8nXHn4p1ahs7mrkn44ef199l9PJ0GSPciKtOuhFy3NyP492J9ZBiNTGYQD5CR0TBd4fdLCEm5HT6Fxw9rePBZnVG7dioBeJGdCfejNYIOId4Vw6RIsogm6KYYum2kxgSrApMBrRbBg7ZaULV2A00UMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 183K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 21:27:45</div>
<hr>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQXZsHiwe9pq_OdrHkmoCTm6KBc61CBqEtV5MB0twlW31XHo115f0QGugNl9I1rhrlBuM34X0HkkqaKhhjsbjFrwzEHTE7cvRXBygzQdKQRZctLv3oW1Bj9k4Y8-F0ri3JmWKkdXq0a4VlB9lfXYDYGCLXbtGjXrQ0l-qB9nqnSIAm2jslH3kO2FyhQDrcAOa0xxkPxpc4Zw5KDiccyL0RSvB1JWlutEdwxDKvLGKcAbjRxb69Q7feXaTQBZE6Hnja0x3Vx7qlVc2C6ssgpSp_puM4NkI_6kLWUHN_FRA54MINj3xP7tPrVZC1ImLE_FK1oPxmcUaTIYwdnFFO1kPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=EOdAg3FlGfUIq_iG299lTb-sg6zJkPyZWdgPDT9MI5cp2Fhdr4lBlt2ZFaVNjnvcnKvQ6QPUJI8I3ZDpaKyVDZBKNKrNrmr3wk-ZlZ7mRsDegaS83jsXgjlYbatmbJ6xP1QcJmt6tjL8I0M5ThxRuUEQ4_wtUnyCElGRRq83SLccOpU6aTOyvRMqeqZDoFoHodRggdsvXnRFcV8E1K5qx7egJ7uKrcY9y-SjZSFXG2SQUtnaj37RGGgeWEZlOlqwPhhTPUu4lXp66kDNXAzW-YaR2N9B1Lx6G6K7r8sGq8tZc7GKXP097C1-IBCmReJ3N2Pxuiz0qLphfAUI8YAu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=EOdAg3FlGfUIq_iG299lTb-sg6zJkPyZWdgPDT9MI5cp2Fhdr4lBlt2ZFaVNjnvcnKvQ6QPUJI8I3ZDpaKyVDZBKNKrNrmr3wk-ZlZ7mRsDegaS83jsXgjlYbatmbJ6xP1QcJmt6tjL8I0M5ThxRuUEQ4_wtUnyCElGRRq83SLccOpU6aTOyvRMqeqZDoFoHodRggdsvXnRFcV8E1K5qx7egJ7uKrcY9y-SjZSFXG2SQUtnaj37RGGgeWEZlOlqwPhhTPUu4lXp66kDNXAzW-YaR2N9B1Lx6G6K7r8sGq8tZc7GKXP097C1-IBCmReJ3N2Pxuiz0qLphfAUI8YAu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEVciEyW1Xo4-E8IWD_s2B9K_Pf8LdnYvbnFq0oKRhXPMgqTFkO8OxLnMnFZoUJMUtIzQwW_WxhcPAsi26uUt4HiNQkcOOr0L1HwXZYy5sNy6o_o5NXkxabFUahVjr4qK2uzwYJIDp7397_foRYOfAPijuSH8FjR80stGSqreM0cflXbXpKLU8MeZEW_LMVSrnJF-sf8qfodcjk87VZW6vo9SxUKGQKUnq4dqRb3Xi1A6AoxjPlicg5IVlCqu9YHh4tkAZEzabpsEnAcAFqcAvrpx5GWfk2Oid5SlWlPS4NSQGy_7gz7rd7AcSTyw1idbXMIlCDFZWJYV4xXAKVEg3RY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEVciEyW1Xo4-E8IWD_s2B9K_Pf8LdnYvbnFq0oKRhXPMgqTFkO8OxLnMnFZoUJMUtIzQwW_WxhcPAsi26uUt4HiNQkcOOr0L1HwXZYy5sNy6o_o5NXkxabFUahVjr4qK2uzwYJIDp7397_foRYOfAPijuSH8FjR80stGSqreM0cflXbXpKLU8MeZEW_LMVSrnJF-sf8qfodcjk87VZW6vo9SxUKGQKUnq4dqRb3Xi1A6AoxjPlicg5IVlCqu9YHh4tkAZEzabpsEnAcAFqcAvrpx5GWfk2Oid5SlWlPS4NSQGy_7gz7rd7AcSTyw1idbXMIlCDFZWJYV4xXAKVEg3RY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd0qm-qZZPV-ETQUO27BTwHj9f5GxM4gGSPk01LnnnzlNZY24eJndCPVCEWFlB0fE5A0aIhQZh82pozomJDaXI1P5EV2AWKVd0sFjjoE76N15Wy9Lufq44fI227V3KvFUG4UhQe55LFrEuCGsHgntI4Q-_q9rdWvfxvD0OHWGbqRL7y-MKsYdpOwLhc01iTUQS9kbzzt3Uu91gBn21Ke7icyQPlHcBX8wkx0zxJDhm2NLYjCZu408NqTFprE5UP_rEVKZWfmvhMTyzDUx8jsofLJSw4_fCeZ1Ken865l9n5Nmq2PwOUipALUikvt0BDza8McdMaAc9qPXl1WWz5zZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22392">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G00dNewW3HJG08WsC2aGYLY1dkvsmjXj_v8AxVKBbQQJihnajnBNmUpFMMy2fDybDwKWwmXupp5I9BAu8GwfZFohfbe-T6Hca7tLny3D76V9bmBkPttq3cUYNU2J4-AHVn7JJyuE61B6Y99X1w-nqtJO3gDAMeJWlOU47sOMOp9jd1O7Pb15ESIxQLApF0Cn56FP9dpi0eqmqwKqAtsAjzoATevmEXC4oRSlAxD2IxJg8Xx4ZQ2SLKRNPJ4vY9x8KZwuMSag5Ci_UkB2ODQ8x1GkHwa6rhbD3lHK7g9j7YBBMcoPdydh3VUfZnnhSfnF-2TZdn7Uigyd1ptVTIWYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط.عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان‌جایزه‌بده نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22392" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_hFD7oZzEj7rpz9wsR-BEvOpvrzShMR3YIG4WPiE23Sw4kx-5StIAm11_bU2nSYhdbuQ8PpP0jDY4CHEFwlDxSB3TXK1qaTo6Y8WhH-7cGNlCREElQCvdC7YpZBjs9p7Q7SZwBdIifOjQgwz9b3P7PiiZh0Ob530-xBdUgD0OtJ6F0WEAotbXI4VPOhQ4KzxYkMNhCjBJHYXY85s6mJjVHCcwgHTzPzGMmNT6tK-_EKILuODbRQklWEDCpAh5llGgqCIxGh3p5vYkh3Q4rWOQRsg6A-Ywtxcb6_dex5JzHm4an-8yt8gCkP9WVfjLNUXiRbzcLkS6oqsqt_B-1sUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YafPWvLQQkHhYyJOnS0N9LkQzkYydtXwjq9T4ZKXJvjoO9KQrmZtRYSiAbuRm8cRzJqB7X0juwNAuXWW5tR68aHcgpwNk_aQUL8mcqJSy2CEFyOtyCfxSZV8u-qNmqhAOT7aEJ4AToWos-p7Q1NYTlG9OWIDOPATqus34VHHhk8Hr85DjimWwRZOJVTDEP4LFjBSVGxglxpJP05FpXVqh-XzRbvwQnefOP-w0-74OlQDLZDzEknrB_nUfmGtVRGY60vxB4eASD764Pgc88bQv4IFP-DlMwrgZU3aE1jF1Z_xYLeUzys3Z2Gd3J590by1BUhiuBHR3tv3ITUgAVcMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skdqExMqG85JDy7UowC9Z7jyEKY0XpfLJBsHSnSXPW4CSKsMauwcDkUQ9u9MvNXeCzwheHnMA-U9Egw6xoqxRYCAIvi2oeXj_RNfcUEnRitsU4B9h6tmocIcbRNpnDLS6QAUZtkqWv7hY4zBC8af71Wph_AW5MMkn00QlDhI8tcluvVojOZ4AubuKf0qrfeVrPuQ6_Q7y5ny10lCFI6-eVYwyL7cp9kPv7IwQmAFsU-HtfdJOvkGjt9qsyjFrRJL9jl3qq2TmWYiUGsHaltYuOZP4pfNEZ2vzuUthNwu94B5u576tL3NO0Mmd6hDbhIwxFP_1TdNewUBJeOMr2yRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyyrXZdDUPTxikXX-bF56HUVjtpTLv_aGuOESmm8NGpDyK1f4xQd1lapEnPQX_9aoKbqqF6ycB6aWgoWZZNC4KtQ7fgvWkDu7gd0QUOn_XEXCafh0dFvTe_tGuxEnd-BIo-SN1HUNrgLvaazHGdJkzBmHisaNumIHpCApG4nk7QzJlQXR62BCNJ00z84fqW1jDQQUr87EOzdvfkakliamHWwIhAozDEGC6-J4WVWkBKBjyX6H9PVIPG-3KK_4CCO4mBnH_3YAVswVx2gjFueyfy2o7BqsCNPAYD90ObD8dSMTRwzxYSFoVdWYGrgz7y25hGPtPMfXljXk4bSJLQ4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRapht_DQXRs1wQ06i065QIltxaSOnFFA0oUjX1rzDTXZ9lzUNciIFzSGGjrqu-wzlVBe6U6p0bPoS9TzU2ZAqo5Zjttqscoksxz6SbtuwC0mTKxa4fg2F0wNJcCSjw9Xk86T-DtmLl_UQHzPa0BkeFWxMJc6qeUBJktMIBrPbgatnuRfnl3ZIolrNrpSCge-FKThvgTFFRVNrpP_ZCfq1fHA1aJR_n98hn5b-j63hYF5hHn7pe7aNhMhewz2IzCnonSDWd3H0aUdApqetBnbkQlFWQe42ShSGOfBDepSkEMP7bxnuvWUUUPKuDrYOCT3vhO_GMfQ-mFQPs4RA8V1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=wBF5tJdVf0cOv9j5lU58fk_57Xp-OUMYeLAVjueyDP8BAlFhHKXTXqqQ9GcVM78AIOGCLzu9-f3Xkho7xHHpCfu89CrohT4PklW5id8sul7wIEwriWSYdIpocsCpkD0UnChF_WxGs8tSvofPGl_ZzQ_I7IS2fXMCyHi-Tj0R--QAc88BNPYcAwca0zR5tX8DN-ZM4evb32fwEYWyFywozsEx6Qm00eLgp2JyWZh3W7rRXpWlJ-As_Ue6ul7rHuGBYIQGtMuJrF0h1tL7TjpP-paVqcV5ZaN4Hs-eO4mAeTXVsv25Q0kiNKeRJtcJ8bOJEvm1MJP_zEQSdr06Zrq0uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=wBF5tJdVf0cOv9j5lU58fk_57Xp-OUMYeLAVjueyDP8BAlFhHKXTXqqQ9GcVM78AIOGCLzu9-f3Xkho7xHHpCfu89CrohT4PklW5id8sul7wIEwriWSYdIpocsCpkD0UnChF_WxGs8tSvofPGl_ZzQ_I7IS2fXMCyHi-Tj0R--QAc88BNPYcAwca0zR5tX8DN-ZM4evb32fwEYWyFywozsEx6Qm00eLgp2JyWZh3W7rRXpWlJ-As_Ue6ul7rHuGBYIQGtMuJrF0h1tL7TjpP-paVqcV5ZaN4Hs-eO4mAeTXVsv25Q0kiNKeRJtcJ8bOJEvm1MJP_zEQSdr06Zrq0uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=CnIqAPJeYjE1jf29xUHlA4bjdMB5d2GNSwU4zpDaqk4qi88OmaWVHi2zEjtyTTeB0zRhEzY9zkQKslUp3WFut9oKMVa2imjzZoSJ3Z0Y5acNI3ZE9LcFpJf83wwm5ROaWjgNjvO2TpF-usvryRwqG_hVqqiAb3V4cJ-aywmOhKJjbDX1YWaK0nIjDocq8Lkyyo3iI5jgHTEaleAHKce2H3-oMob-DmA9XjM1ac6QzzOJ5wpYpsaYduFFpQVxbbVoU_q3PSK6zRk-bv7ZjFdnL0PHPGMdwJyGRzGHevX6i5hVPb0P0mVUfPjwkNHBVbIWrszHuysHckI8-FSaNmLkHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=CnIqAPJeYjE1jf29xUHlA4bjdMB5d2GNSwU4zpDaqk4qi88OmaWVHi2zEjtyTTeB0zRhEzY9zkQKslUp3WFut9oKMVa2imjzZoSJ3Z0Y5acNI3ZE9LcFpJf83wwm5ROaWjgNjvO2TpF-usvryRwqG_hVqqiAb3V4cJ-aywmOhKJjbDX1YWaK0nIjDocq8Lkyyo3iI5jgHTEaleAHKce2H3-oMob-DmA9XjM1ac6QzzOJ5wpYpsaYduFFpQVxbbVoU_q3PSK6zRk-bv7ZjFdnL0PHPGMdwJyGRzGHevX6i5hVPb0P0mVUfPjwkNHBVbIWrszHuysHckI8-FSaNmLkHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qygIZNdq3sYN73f19X5NsftNMfHhYSU3PUYHjYTdRAk6vacMNxzwR4KxPns-6-vRzYlbjptAaze6rr5ZmzymfyV7-Ww2XYTQN2szqFh_IAfABSAaTAGXWoYZax4NUfmJxheE4jZyqptSXcPWbI2LwEABF_boMXk9Ztp0qm39q_2UkzmeGbpb9RI6Ri-Lhyux4SX_RHTyVHA0LMJXv5qTnSfEp3y-JmfwLMEmztiec6gZY7PmwyW7XUQ8ZKFht7T8SDSBx4Ua4NP7CXZQxx90B_YsrUC9j2hGam63yEJFZ0AsmKkAKE5GF--Iw_PsGhFUsFKKLr8x8MR2RvIDb8pWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC3IP1eMveuH-L4FkdaPjI_EO4XV1NpW0RBC-JlvLPukfXccsJSCiMi2lNcC_jrfShNXhqqrJrk6kH1hkXLjWZwy5H02191hABd-8LB6kdW9t9OwugV4IAB64sqVVGaH7eSjiOAfrl6FjMRmu5pTpRl8z2_a6lZusS7VB2BRc42imwQ5-9QBpoLHhH8RzLQY4ZBtnuNNLdMzytTbM98h_0m2cj5PbyQ7-OiLC_f__l1li1tn9Vj8kCEcpI9HEJs-owbIP4jMdxIxIbp5iDr8u8IY8BUhPntcEF2iDHWb24n_7CjcVkASc08odwtEcs1Ccdh4r7Uq2BYT5qtcwRrTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtWnV6AIKzVpJv6n2TDy77jwvB-Qem1rJYFjdGVesKNi42wFuBJJfYdk3r1yTfYdP49IKsarjTpUMjAfXfUqg3gsrnAceQ3zAFVt-hn9chiehzXT6sI-RzuAGDGha5pvMVYrziGsveNGX5mUv7uw96EfCpaW9cWRFwH99WHzcs8lutd5_J9VfQFuU_3brnnNsdw7E6VUedCrNDLjo4S5AOqAY8oj5Tgj4DYaGhYlnvSNJKF6e5BdzIC71GmCkNGEs4oL1uRuT7tTsIWR2fw1R1nuYVUhzxrM-yyelEa2CZOzaTQEfPauxjP-HtGcUnmJUd_5dhz3-QtBOSD3Gn6SCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBTqIzJAcFn76Vq_CabmqpyY81yEOXjJ0bGxdfbgb8ddmm_iZJqDOtQaqpEbPVC-67ukX1ApINcb-iQIVZsyfbnt94iielA3IxZkmgU1PUk38AZuVQAmRUXDKhKgXi-VHmkZqwMjHrbL_PjxcINxwqbmFMF7UyIX0QHiHMbxXdX7uIP7tn7PGOpzrz2XwxV9M3-2Vc3SZ7LFRX0VvMQCsp4sGXqp4NG0sDU2y7qTUOWHOddbEC1V27vYGDZFAsBlOJU9qH3yI3yqOC_RA6tejS6lp6DQohznkWykpYkWGpmTwUUNrKsYVky0RJQTY2mVp_1lRBwDyU6UJyO_PmZ6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Minxp1xQw3nyIxcTXVN2yzO1W36tCm2p4nw4FyYpnQKa7WG7iwboQk550b90URJ9heYNu_YJeQwV1VYRoe7B2IRgYACNG9snJjb5U_NobxCKFCK275LIjIJ_ridsheprd8ndIS80M54zOeGHUBXB8Uju0V-Lga-xnpG2RT06o2wRY3TqL0l9lDCQVlpx5KhMST-CWFopgvjbZIbivx7I6-3QJKIYJaZslNvz1mUiroW8wdS-2SAbs7DwsdKV7ofDrbAPruwlsfNt0vYR29fyyGX8SSma8wD9jT8i9ZexReTsOdBDabE5w8gPIwPABCtqj0oqIx7gtPLVqMhY1LTv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22378">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6q5J1cCWgCyNklCEgwOid28xn9nhiWegCcZkwFvqA2KOAGK3ZNvezWGuqD4l2FDwZzTva0VoRxM4C2IA8VdYhPQ46umBCg3ZsQordyIO0HyMBcyvX1aVQ9uDDaTcKPDPnAInMp67ilcsmQ-8JqP-OP6-JUg5qxlXVksYE61uB2FwvpSyHa6JtFGI1-kXXs_bjdeLnXV7-GcHRyVwVhKKAsi8kWb-DPwf3ZrB1hxiR2T4CIg8lrG3Po_--EZuzDq5iweKDgnsigz6yNDNmDMDgtpvd0jt1B28GSS0e1VRSk7Jh6S3aAeJ-1dMNfwnB5XxD2rijtKVCGaNSMqw7SnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنهاسایتیکه باعضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22378" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=LnTn1RGo-AxOyhUFfgARLefoUJbGzaflxwgRgFkxOgv4jo6RH1B11UOOVLr2odHtvzsvkuIikDH29TncQ_Uxb4OWHebc_6uHXCiAGwhP1wq8lH8GTjQWkT3WqyV6Qa66HxbTEMMgZCj3LXQum_ma4sP3DBbgzJ-Fd0MqxDvyf4hlmn9B9OVTQcxSXlMbwIaO5FRnwYGQkuHz8n07BDz_vHx1ankUDPbuJlNAkLIDJ4OErVkLwFtxg3rPSRSKZNnbYO8YMrwkRduAZGm_NqUJmFM-EnaOyz7okvg7pgwgDf_vuSfteNs6Q4ZPdRhRKI0vWCCtkHWocBhqrWur2OgW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=LnTn1RGo-AxOyhUFfgARLefoUJbGzaflxwgRgFkxOgv4jo6RH1B11UOOVLr2odHtvzsvkuIikDH29TncQ_Uxb4OWHebc_6uHXCiAGwhP1wq8lH8GTjQWkT3WqyV6Qa66HxbTEMMgZCj3LXQum_ma4sP3DBbgzJ-Fd0MqxDvyf4hlmn9B9OVTQcxSXlMbwIaO5FRnwYGQkuHz8n07BDz_vHx1ankUDPbuJlNAkLIDJ4OErVkLwFtxg3rPSRSKZNnbYO8YMrwkRduAZGm_NqUJmFM-EnaOyz7okvg7pgwgDf_vuSfteNs6Q4ZPdRhRKI0vWCCtkHWocBhqrWur2OgW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qujpee2BTT0paG-YbFPH9M7mPpjPLy2ER-bsUn6UWtVglPCa3vMYcgnletWqvhbV9u9MaGsfSG8NOztxR6ukYHdRUOyZ28CnHBIT9Pb8MI4WnAj9YG6NYUXaTY-4smiueZLkx6CUwwds7yR9nCIG_VtbAM6IneCZH1jHe-zredlW0wa95GRSPsHmLZ1_asxKRq3DMXuGlCYPpgiHuj5sFJE0rFqsOCF1-B2K5X2ueQyvd99JxUJYJXnHhtFZUq1_7P7uNWbalncP3W6PxTvPCo3KQHkbzvfduDh8cSQnFXQWG_5yWJ_X2gp4bgyvM5_FnmnCm6exPDKNPydDpj9inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmDCtixmeNghQHUaTk8M9RCJiFdzgQbxJi2k-L02Wlum1L6J7V0f4IayUHlG9luqpxBAv9h1YWCbxhmfonE4V7N7H2gu1aWY18Mi8vYcM_7YwK22qjgIJeZXMrZ_jBCSaTed5zbVD432dFMdrHtPYgWXiLeSWomKX0BBcGMzFpXef4r87ZPf5R8NjsbwM-W0FnbS-pwEPKwfI6Y9-Tp4fy1LoVZrrwkoqDyY0VtAWieOfa14hweRi4CqROlXK8ZD9pq_EQSByJcZnfHUp23Zp9PaI2wXbeiA6mg_f8kbZdccsCTU575rpPbnfyPGKpRWuFgXeJXQD76Jfsy37OlFHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW9rcCUVVtMuLcbxYKWo2W4HCT3XSrQXoP3fg2U9K5xTr0qYUS49xr55BOTlvRoS1s4A2iMt-3Fd2gf1QX8SYT0G38BJaffrDJvIYWcb8TLWH0gkTLF437QX26ziDX3G4q8YcbKzQrNF4UJoGM9FErCfDoW0sm8lTT0GBym6ICtlIZ07Jjr4apwMVFoF3AkfqFPB9X_T6wvDW0V0RxayZKt8K02rKvC-1381fT_xIBf7JKS566OKyr_-FpfNMoWjP1Hn7KumJwyl4v-1LzCab1k6rfvoFRbxk30RyGsLJzGfxVR8NGj8aJYVcZMH7tyhjXlR_Ba3z9dFVFGEorkfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zqh5-9qm1tKsNAAIP0uLySG5w9K-7jHj0T802Ww0ubIhsISteMyDZy65Hm4ncZ6_3Jz7bCRlCbXLOke4u5p8eF5WuMY28ub06-VqX8Qf2k8iew0gIkSUK-b35wQz4aSMHtNonsxHixa54PSkcQq_zbPzD75cklfiYtBqm0u27Y0lu9zJ4n-T7m5OaoLYJM2_PlrsgTPiGiW1jEE0cO8wBKAPNfPF84xjylx-ov38oKClnbEg2-uFTZcqxvYH9pWBUrnClUDJ8pk8-Zw7tnXcaLHqI_foQf_fO_3XNjEJNA8rEjFkjzABXVvfOC9F2pERsEOWJW5PeeN_mehR500coQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=j4Fosvb2eFQ3EKoVN5oGqjfN3nneXNDPM_E3p54xEcNvu0r2TXWPpHz0qYgJYXMfkZ6DkbHg5jebSktfmBAbegKYBlIzZjJKj_TCzoSMVF825_TELQf4EVb9HtUEG_NsUB8h7cpty_CfZBcyWikrkA8py1X2Zq_LvShXAFsQ3vLiP-bXcY2WrcuTPrXSp88PPK04K9uJu_ZkMEYxkdR8RX_SDXjXDCVrA-1eSEDU3h0LmiW-yjE9aBbh03MtKjB1XvrbjBLNbrl5KuDOjz7vJCxTkaUsOcjeG-kNSSNLobq3uu5d2IFCicUpenCpDn5PQgpx5D_zciIaoiYvuN_ZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=j4Fosvb2eFQ3EKoVN5oGqjfN3nneXNDPM_E3p54xEcNvu0r2TXWPpHz0qYgJYXMfkZ6DkbHg5jebSktfmBAbegKYBlIzZjJKj_TCzoSMVF825_TELQf4EVb9HtUEG_NsUB8h7cpty_CfZBcyWikrkA8py1X2Zq_LvShXAFsQ3vLiP-bXcY2WrcuTPrXSp88PPK04K9uJu_ZkMEYxkdR8RX_SDXjXDCVrA-1eSEDU3h0LmiW-yjE9aBbh03MtKjB1XvrbjBLNbrl5KuDOjz7vJCxTkaUsOcjeG-kNSSNLobq3uu5d2IFCicUpenCpDn5PQgpx5D_zciIaoiYvuN_ZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtoilFKyJ_Qjv6tWgO50Wc1a0ZJp_81-gNA2spoxWOKLdstLRuntOlGw1gjinX41SjKgaR7A4uZuEHMCLE6YpJ79Yj_H664KqS2N_izs_5gtANSnYNX_8fInfJwoM5RIpNgsUx5InQMXE3l3pjYxpfP6oJSj-X4-VJD7GP-OtVfCvnS6k91FeGoHzc3hFlrB0UA6LMYR8TBVyhWkTDH1n6aqMC_02LV92QV5wF9vdnhjTzCbIvZ_JRWece_Ea8wlIhoZXYW27-8z7dXpXReP3-YbhVOyqsxSqyzoaxfkAs3LCWbnR0xiQc0RR4kFavGHbtqhwrzKW0cx6nko-rUVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IygrrdbWIaKnnZpU7SmIkfW7ZAfQCis2tvYU-q2jMjW5hy4jsoIhLSWjG2fCHZgV2G-a5fQ0gVrk3XQmLLVZ3K5p0B7IiBnhZz2qZWqwIA6NTNAyOm6ymT1h2-H2qM6AjFE8lZopo3otTqR3UfUKT-qD5DAHzt9DU_-cPu5JZ8GaFB-n5dZFVM0Q1yEIzL9_WoiqRLwXkXWNsG9Gkw1mKuqt9ODgM_3dD9PHur71yBMTV_xlb3i84KkTXqlNuA5FXwrnXmJ9Qhacc69c-1XJ9bMYouqOkffykyk3fs-N9Ghoso5HwSMZqkDMQbFsVwu8JvGECOmgAUBoHvKqL7QWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlANFjxiNY7_N8OSc_pyjn_QF52OZT4D2BtBtvc1BL7NoGJzv1klMMlt8m3I7VNblSmrvgTjTIq2RAlb6_dfBM4OLs5POnuO1JzG6wQBTLUpAASMsM5riH2CS9mFvfBM5fgrWFAKrAl96GBX1bEw5VRd0BQpolrVaJo-9oup4KGFIUtxWhBDlSjrvz1UbUX0DN0nN5ROlrCnsEuZfVc6GIFPf9n4xAa-3gbEBrgkTmR2tlL9sHSURcSqoz0_rwHrQzDZLtmsWFMtaKxtmTDtPBE_ruFH4Ch5ts3MZhgBix7jvzkeKFUX1nCJ0l9H68L-Gp6uysvckDBLH9XaTEmDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=PMRPVqG5hWGBrKOU-VK3GmpjC7sEfDbv6lTNWP9LiOAuAQ4FhoJbtUVU_5eXr045YB1akPUrn-PEZqZLLYV01tMjmjhHbPJiLmtmXWwW3pT9pcbrffPlwILlQUkuAFJhhrnDu_iso1wXGaA0ktwnTmTLhPVHpwtcH2nVwtURn2BDpL8_xdUFEwfcCWh6rFMGA2aUvbu6UjNx3aRgOV32yUvkmPx09twt6HWYNCVMLbB2dcmJWU6hfNAJ9D34EaieWrDoW1nF_u77x_PfHW-Kva03sc0tGs8RZ2xE8Pw-4lTH5PNW4YvGuOo5hYF0BOzMUdRDGIflt9J7NQ4H4-Givw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=PMRPVqG5hWGBrKOU-VK3GmpjC7sEfDbv6lTNWP9LiOAuAQ4FhoJbtUVU_5eXr045YB1akPUrn-PEZqZLLYV01tMjmjhHbPJiLmtmXWwW3pT9pcbrffPlwILlQUkuAFJhhrnDu_iso1wXGaA0ktwnTmTLhPVHpwtcH2nVwtURn2BDpL8_xdUFEwfcCWh6rFMGA2aUvbu6UjNx3aRgOV32yUvkmPx09twt6HWYNCVMLbB2dcmJWU6hfNAJ9D34EaieWrDoW1nF_u77x_PfHW-Kva03sc0tGs8RZ2xE8Pw-4lTH5PNW4YvGuOo5hYF0BOzMUdRDGIflt9J7NQ4H4-Givw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um0o9jzw8eOYO4XtLLb_rK6Gj2Ds2pwrlBWB6TNohaKN0GSj7hmjFI1NNQ7RehTzNn42fn_hrej8s7fl3iSEnUqyCD4JnjKpYBIH8L5fbVeS3yxss1LbXLNgnX65VKtxPjMHcgVJk7ouZB0ZreyVMdI-2ezuKwZHxKifg0Ym-wFMn2mYWgBuP02kHbaqVdhmwHj_nfQx2g8J1fgj_N2YUgy9HUGX5jmj3_frhEQpZxNcnJaRaF2VSbkkn_k0xMerwqJZDieb-DPLedr1yoLkO9rmeObkyvi8QvllvI-pxt5ALkDvt1aoKb1kdxsXCJIWCYQrzSpjTEyz9LQlMEo37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8B3WY6m4zHvEUjDJEcJay_DkmVr6M8kbTCROG1Ys7Sx8I60MX_ut-3S6ZfwJ3NdXiwGFFQyHLEPxtE7ZMEYgL6SwDm2XbC1pHwzCd2q8alB5qHLStl68xMrFLGfxa6EqKMW8fLSCFnYque5VQ47sn0w5yy_yL39IZKnLJnnUOyG6a4DmViMJ9hJUQTKk5tJvwkq5ivTFjIpQNe8bd7d1u2282RHxhdnvjK5dBRT97bHJkQSlrRT4OLCvV2vcc6Kwn9eWtWS5xXhkMrmnhr7ULlX3zRUJUQNqo55OHTUAoq_QigogS32TBsYVxZhK93QSMx9iCePvnOGAJIrCdqRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9NaXbtVqUTOvNQgTUCgQ6Tp0pUSF9GGL_6LVeGPWyA4v5j50Gb7fIqMhzL5h5Mbt4CqEBZhqToohsk0MiHhyZ0WBwVQ1vObxzHW69Ow8oRZsk9zS_4rAR6p_J841UyRQO9BfrW_QoQ_pZtUbGWEkcIGIxqlP7Y9RekmaJR5iJJuzid52eLRcoGil3jbSFoA5KRxONC4GySmQWm2LZtH3dD6nIQ4b3dwIrH4y1Sa3tlv_wM5qmtOyM5OIBA2MQ7D0Ba1LeS8ePNBsAHJyhJ9XerkJjxRsdCYN00nav3l-UB2dKprdXCW7Tzfeg49KesTdZ9Si3cNPtO5cmhoOovzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owB7IhEE_7KlXugIvpl5eDTXy1e8lYLBwxK3OOg7RCyyq-STVTUEvIw8zXrn2Pr16t07I0JhRix_8nrCdg-FJhvvB9X5V-jHkYjQfmxR1YhWYWJqdBlRSV4_ijrI0X_YzgX5gDwioLdM4pftAILIHkaQuMvuNehrOk_ZqivZUGQMuEqW3-lCYLTJLaWfElpKaADOmPS6gztq73g42nLx8i_IPMfpXZ9eQAJ-sqaxtsl1onjjxGrZbJiXv7hZs8NX89c9hHT3uj2NMggJ1bOioGcsuGX4sR2RRvvf574DZZUj4SVS1ujynOHfDNANRarqcupy_jO6joZT0Ip9_qKMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=j49s6UTGfILDSrf1rXQc7TBR_dwO__jpVr_PlFgR7Fj2w-PoAFEwwjhqf_Okhu-Wuth1FuC_Rp4exnpVhm9de21ajalSGbcPV39CsY2YbHFyLKT_P3R_loJlqdtKhVmPM9DufJY9mpSy1P_1_M-lZKxr8VSzdnDe-fIwp0fPOm0gJhpHmclz04STULjt0dhlmbk5Jm0-n_s3dxyxTvICXOOQLXyx7W6foFel0Zx3q_PZpwGLNYzDcVHLo-JQa5HezCKmUrrbTNki7FI9fyjrjN0_6KG-qFmGvMHB3VMWYNO2Umd0GyFx0t5wSVpZkkcS5NSBpD3m3FdDujQRf3Ay1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=j49s6UTGfILDSrf1rXQc7TBR_dwO__jpVr_PlFgR7Fj2w-PoAFEwwjhqf_Okhu-Wuth1FuC_Rp4exnpVhm9de21ajalSGbcPV39CsY2YbHFyLKT_P3R_loJlqdtKhVmPM9DufJY9mpSy1P_1_M-lZKxr8VSzdnDe-fIwp0fPOm0gJhpHmclz04STULjt0dhlmbk5Jm0-n_s3dxyxTvICXOOQLXyx7W6foFel0Zx3q_PZpwGLNYzDcVHLo-JQa5HezCKmUrrbTNki7FI9fyjrjN0_6KG-qFmGvMHB3VMWYNO2Umd0GyFx0t5wSVpZkkcS5NSBpD3m3FdDujQRf3Ay1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVAb5Xq4tKpW8RFgQMIIiepQ6KfYjs1ZAxcAbtkUW1q2k37UeIJelhU-xg1sxYKSlud_SzFadjM6PWEFBDYbjAyovHdtcrOlHNKvnOn28ZyMxDxERzP-tZVs8AmM4KaXf14YQAKO9GoyHKplea9oTE_jvft9a3Lq5aB5qstRcqdKfJYeyJK-NUMbyE5Y0x1RPr-p2mVKJdLrV5pHr8ipQVrxqrD5tgkeDuPA-zgmlarM8L-xPIMOzUeBxmLP-tbl2gSKoPUvMsf1I88GdEFXko8hccoyTjkKh5YrxZqOimdcDLfkOlYwpQqwom6O57DHkXPbyQaLwOQXgLphownilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=l5UVbE1QQZskeuxR5RHeQ4vP3TcCjy9HEv_d78K5omAKEZjb5wjn6PToL3cTo6RKjhxI0PEed-sBT4xp4gcJxJ2wkFNCXXoASKev0U6juKWHtnXeXOgLmzWBOoEvFHudrwGcWVY65nsON4jewX3uB8qKKqaD1nQqeAZ6hefyR1RrR0wAxI9NxCe7rFh3OCh18gvB6FjL96wTskQzyKBcO2_ACbVy22C7jYKNjK3CmfQyPyoru9rmzODSKiv03s3KvSgSIts3afX1BQxIeliA-Ga3Z28vZVCObtx-ZP7_-tw6DkZnGnAFeBm-PawLoCocm2pmnZW70iJTV0-ZrFLtIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=l5UVbE1QQZskeuxR5RHeQ4vP3TcCjy9HEv_d78K5omAKEZjb5wjn6PToL3cTo6RKjhxI0PEed-sBT4xp4gcJxJ2wkFNCXXoASKev0U6juKWHtnXeXOgLmzWBOoEvFHudrwGcWVY65nsON4jewX3uB8qKKqaD1nQqeAZ6hefyR1RrR0wAxI9NxCe7rFh3OCh18gvB6FjL96wTskQzyKBcO2_ACbVy22C7jYKNjK3CmfQyPyoru9rmzODSKiv03s3KvSgSIts3afX1BQxIeliA-Ga3Z28vZVCObtx-ZP7_-tw6DkZnGnAFeBm-PawLoCocm2pmnZW70iJTV0-ZrFLtIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff4pGkKGa2DpWLhTkwj-bG964xGuGXDuBrLsW1hVv8KoQZYowcsUOBiSbqkxttiW2CT-IF6Ivwb4r4C-63PYbubXAjoSKN0uUw2VtRVp2FjywELBV-C4IL3n2LUFONyyM2d6WEx6rdQwP2b2HiZ7Q61cVJPLHvIs9hPU351OUVZyzsAGs72RC_YLXouZg4G_F0IO0UjBQ_UgDuDhOfedkNo1TOD3uk-jkiH4sgTXeHQ9FT095HlNVDNy9stB3mLVau3306D3e-vsLm8B_oejvFkm9I-fk49IhJC82XRHYUaAXYnH05xiNMdENHZn-muUI_0RmbFDj6xqLG_VXGHx4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOlFYBZc5-yCVqZTxN5Gb0cOPKocxJH5-R1mEK-z5pkIWqHQMKSpiRWda0KkCjUDadFzPvjn4neG4YTzhsc8TB3DLrBEvbRnUB5nhQxHqmB95EwdXtEB9JtWloLx31kU5DUvcTJNiPgKWJtALXFowuA-NAgSQRp1HKcBmnfgoAWpQ3PwNB1VBa7-z7KL9MuTuHCho_2GqLqB9WKUUu--MqFyXmqOPAnwMXH0I_s0MLbE17OEaVOwRd_Mw65qNSmbc1NkOKez204y5HZRPVHKOFa7PqkbPVY3Zj944MJNpSuYHHCZtH_ZtNRulRXuEwVwMi7TWtyjqtFjQMymMGRtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H874SWlWETSjU1qwdihfEw76UUJzwE1Mz63FCS-OYMCfgn1DtM6dhTfEBOkVXi8BtRhJ4Ezk10Emkw1_LzJAXw2Ax-_EqcZi0Y2BRGYm1fuk2CWQpt4F4lbgZwS4CA-juGazTBDGgeJaDSGTw0B9rOWyrRep4m8j6MD227v4EpIzcRnHQ0gFCeE68OUCpJauGlB3sLWT9N6U8YyOexlSm2UGOMFA58I7c6I17htrWcSZqQ2wYxLi9ztFJN7bdF5oCoqsxRmWRxCqXSsYuV6TBulzSj3YD1NefMRNv4UBwNRqKJdO0EN2k_PSi3oFfyyTjYflQz90dnv6Ag2gVgAltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2p0kB2yo6MdkAN-SR0IbojxxwUoHLYa91KifQE6ei4eavH6SELxqmU3mjXz9afYSmjzeXYO8HjUsCRJuAStbilv2Q3mPZV9v_2nxekzuEwAriXcsqmsWgdAwGkCyaBc344xHsR1Y80DcNpY1L5pZwhrO4J00mVXJ8bzt1MnYzYnWmWGoSfQWAzAGttZjflBuxk0ji3FSmehlK3iL7ixoMnr4Ao1pjALiWgLvh9RZHa6RsAiNp3qDAjcmIaj0TobD7ga5lB3OTZjeX61vGvBGMXWB-6Iz74V2Y8F6eyDG9CCYG_6-FRea4RYAJJ-JuW2eBy3cbC5nvWKEq_9a5SRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhloFm0jnWnCg1Dm-4uSrliAF4clJIpjTr80DIb3Y-pSZC3esfrX_zCiGg8d237l2puP1sDwMXzGqBlIBKk5n0HvjBMyJkmUDUZcba8nF8II9PxjbB2UfG5SKXW6hBEE2gc0mdNFOsKpf68g2jZjMim1C7lpC7z2mNNObVb3u9J6tflcnCcjnD6z773SQf9XG_DGvsmKiZx7AVcNbULU81e_WARau6SEoRkQZiL0Vvp73l6VLlktd1Vvx8TQQGRB6qIhb19UOcg2biLa60lNE-ARpSln9a5NQMXFqKb1sSuvfDERtF2Xe9w7lDTe62NuB3Algae7pKk_CfRt-OJLhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=UOQDwiCHGnYwVZD69Wyyiz0JEGzdde4VRs97wzok67J-2Brrz1XbB68Hv_5-oG4TXUghnmiQxoycvQjjodiXm8rwOf0zpd9AHngOBXEoQi-Afx4CMMjbwFxwlSkqLmfJDGBfcUeMqmivNkxATVEzhhl2e01aGeS0-EvJkBMco44TW4aVRr9kgaPk6Bs76B5Ior83rgLEMv8vDMSmqsh58Yv2DBfT36xWuDktcn_ZSsv17QMQFS-3sWNyY_QzahXhe3UNflWGNu5rsOI-HVT-3NccnloOZTFnD_IkuW7j3UH15O_dYPPDlQsMGt_b1nVSJ5hgFcBJfNvb7z8eUeuw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=UOQDwiCHGnYwVZD69Wyyiz0JEGzdde4VRs97wzok67J-2Brrz1XbB68Hv_5-oG4TXUghnmiQxoycvQjjodiXm8rwOf0zpd9AHngOBXEoQi-Afx4CMMjbwFxwlSkqLmfJDGBfcUeMqmivNkxATVEzhhl2e01aGeS0-EvJkBMco44TW4aVRr9kgaPk6Bs76B5Ior83rgLEMv8vDMSmqsh58Yv2DBfT36xWuDktcn_ZSsv17QMQFS-3sWNyY_QzahXhe3UNflWGNu5rsOI-HVT-3NccnloOZTFnD_IkuW7j3UH15O_dYPPDlQsMGt_b1nVSJ5hgFcBJfNvb7z8eUeuw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3oNyr7hGb99apL0JEY7zitNAGwV8XnT5hlZZiZ7dIxygPjKFH6Hsrh6F-wDVAGl_1Vc-SPfLFlWP9OKYS-nWPWx8bxq-HYN3zvRIp18P8kBuSPPyZH8lTs21OeVlqQNv_23YAp4ygiDIByE28o5lX8HiCzK2vTxvNjdfnvZ84mmYKxvxgo42mmp29_h-VT8FOjX9idhfWq8bg7kbdouW27nl0qkPRYlNbtjf_28AO-lHIpVCA0To1E3VTgBT-RnMzMtl6nRtxefz1KQiVG023UA0hxmh77wwofY6uFnxK9iOUrUeuzHZx9BQbjITslik21_fzDKudmlPFl12d7GJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6SxrLsPkT0iYSke3PCEgOx2c-gvgxg1-Wl0xdqwJgsLDwoOhQIeoHJYD7S4HqT-8zQRjF3oaxk62qEyLPzF-OxHlQFkQcCZwWzff8MSRrLrsEfD088QcVkiZNQiyQ-UmDNDkt1pp9YpR1rfGXX4mj7zWqnKXP5q7CUb_dcVp9vEPpVrir6AMeus06REaHcE1tTdHzI-6d7jjj8I1qZcY5wsCLhQyKMIMyOq9HXijDIjtWHveElnpqPGj7QR1qaHn8oOq3eN5M8fAViTNmEVeLSZiZIrh4NfIGbGDxQHNgt0Is2JJIrJHIl_VGZ9GZba7e2o1JOnmNVkgucq6NvZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=QUGEopG4OV-LzbXyBnTdJfU2Nvmfq8P8fyvLK8Urxu0Nn6vS2Tg4jttadcShZHezBwbDJoupPtv_LT-CXVBpL7WjAVxvCx4e1Sdx2fAwiMRyB48Hxsx1s_sBaCdI0sVemhIrdHb6Se87xw2PTaDSTP4Ho27C-jouuoX6EfAY2CF0KYy6HYZZZbK3NOPs437pU3juf7CZD__BrWq3JMfmZS4fO7dprKqxr49sUZT4disvP1QKunbIAhQ_99iPYgXEa1uTPZpi0QOloh2Ytrj2kwWbjqHM3qHd51u2ZAR3szIbYkuLLWZ1qp8nAyi7hyRX9zURFRNH4gZWhRodqbMCmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=QUGEopG4OV-LzbXyBnTdJfU2Nvmfq8P8fyvLK8Urxu0Nn6vS2Tg4jttadcShZHezBwbDJoupPtv_LT-CXVBpL7WjAVxvCx4e1Sdx2fAwiMRyB48Hxsx1s_sBaCdI0sVemhIrdHb6Se87xw2PTaDSTP4Ho27C-jouuoX6EfAY2CF0KYy6HYZZZbK3NOPs437pU3juf7CZD__BrWq3JMfmZS4fO7dprKqxr49sUZT4disvP1QKunbIAhQ_99iPYgXEa1uTPZpi0QOloh2Ytrj2kwWbjqHM3qHd51u2ZAR3szIbYkuLLWZ1qp8nAyi7hyRX9zURFRNH4gZWhRodqbMCmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_DEIohaXmrM9Ymbe_6268L4sjEheJ6NFR4Med2ZUand1Quxk4x9OgGIvnmWmWOnCdLPu6OqaF-gMWRNA4X_22FbgOqLIGiiEFFPG7dFn9ujau--szWLvajIhPoYNiuRNw83sTA7z61k1K5AidSdw0jkYJObWUJ2gbCPRxZQi_XUwWWyo12dBvK_CoURKPQ6QeRzMzYlqT1nsweUoLkvBw5KXrZAr6wgs61jyz47XzjqXSUE4znuru0brr3QkDCy0ThuSZDj7rEtJMPusaPZx74PihpXOXMu9Ub3D9g-FuXgZoa1EDM0ckx7h804IMpkHv9VquPqo8PaUB6Gq_v9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm3Qut-Kzsq-u1CviDr-k68b5EAmskVxbdxu0rj9HQZvZoJTStBd_5YBysS-McLMjLsjDrEwBd7V_fB2CQbdvWlP2nG_sXL0Is54HohsZt2uKNBrzjaXPpQxXQdzYoTCJPUxQ03MmKGS2goXtgnDIb2UPwV9zzPOYiA1_Kt9D0XCtcjLScDQWeF8tF10YcEVLQTbnTtgjvuzCfQaGkpSOCeywURpnZk3YD_EkcN2vWH7qfWec7JRkfOldD6A52a9yoA3qr5SAEBGjnz2G3qfKZ3Qvjd0Ie8oSIEBIL0BUOhCFW6s0TLmDACOD9kZHryieuDPby435z66TPD43PbmOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZhH6qxoCd1Wg6UHLdBaRp1XaiMbv-o-MGaYqD9JA0F9935WR4U8o1K8GoGyaBC0uBtVTaeB4JObidY4bPRWC69MY-847PNKBuR-m2UMJ5dvRDHBokz5Khs8zMqVs3pdEmQ_S6wZAl9CfaZYoiuiawOZHS3oEfotewfs0b-nIJyzclqQC3Kfk2WelPyortRefT4EkZ1smRsoJRUXkhHdZBhz43yFqZV5mp-YYKcMEPHXbSD4mUHZoRnQEi2rx7cvw1JhiUzAdOsQLVXOjqvrl7M2tXO9CBg92Do3XqO8u7bNvUejpIQ4GQbpSYSzeNdh5ZEGIb_r4Y9wfztew9HDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpbIrwCZ2dsQgFUIyNHbG8kGrG4WhNreANvY-_5rnp-BfJk1vouh6ff4tOmQJLq1B49CyqotCpKD5KowNN2ZoeZ_gf4-LtpKgBK_BsyciDfyFWlZLLTB4IGigX2ZpOHF8bydKZko-ScljkE5mjNLlH1Cvgdqpoa_haKQChX1x3HGydA6ynJSUQ96DhQjiMoSStEsYyPRtB03NI_k7k8uIRRnuAKU_CTnj78Zr2rcJH6csR5LqVA7XesqD8IZzLbBuxmBLb2L2VJMnFx8t5db_ok1ympVzjm0YwceDiYqJ_MSEPeDXWJ5oTdheGWPlJbCIFttfFlc6aRksLpHlsHTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFaErlbbTITEYP1m9jcHCbWdHX435jdwAGDwh2EHgp0HbAGGDRLvfarAolzCE2skDgdCT9UXziC0sFyKKsXdm66OW2t_pU7Rjvo0DhZq4QK6LN8nRiDhO7JSHcO5SxvjUFj1mlPpyc2u4nhg70E1wlpDQpUdr3XDuD1rL5WHnBPl_PM7OXXIZAvURQDmJJaT3KZbc0Vv2YFLXyA_P5bDlitJqBkdvJfzuUKNAe29rnK8qdBrSrFztdTW7FAH4v7cPJrkIneZ55BN5ZAA4yL4-wVEXCW9OkExfSRY-dzrhF_FV7CaQjVLqQh1T43EUqxVX9Hy9UnfHCvhOwAHAqFBEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLaAEU4iAvq1LfYtU6fFyfnZTpT5loxU8JceLvs8Fe6uLTOXHJ4gK0_Dnj1-pSLfHRGWQsHqq8xVAK12vKGAZ-U8fOpX9l-imqNUoLei7AURUdEJ8zQaQ5uCulJvcuROVdlkU6-VJssnMbB2QrP4wZsSylOn02QFkvgXV0mPCdVAPO9Ja2n7bZ2D3RTms8Sk5Eng9JAXiXvaaLouorDmwhBrdvuT6RSJD18wlTKooGalEXR3wkin85kVCTuQqNhhBxICLVTc9L6YkFO-AfTfbK5SeTNdEjuXICAoBDsAGbm4pFaJEeXlZfGD6SHzst5pEZqWRdjlcEdJj2mU53eQsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsIV6Rrwkf-6i040LXkdpziUF_p0WLpKWvf0nUJrNQvR9pfdw7rSbs2ZvocAWOn8yOxNxhjHrd07MaKq1vTAsxAODjwD_TaWVx2bErShliAL-tXprhvqgbFm3Aw02OZdIZbqJmGu01dqz-FfEC2z8iFWtL_TB9W3SRwlVaieA8v5T8ar0z80M1mRg17CkXFxp_tr2EhsZGhR4fPHgRawwMH0sp_UYo6zcBkZpvsAPEw5E2gj9pjAFULil8mceckwYV2NtDjZ-zOdFEwzsOdugncqM1CiW6yev8R5j7H1gIrIl8hbQAFkcWBsWLL4a4rLlqVcFy7KPe8t4JEr-NGBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSz4ACa1SF9Ffoc_yRBSVi_KDjnShLGPpPhe-AFE3kzCo-ja2bSadn9Bqv1PnxknoZgeyZBc2mbApdS-WK3sy6xsAeoIQrDYmJFBlPRzA71aI24llcOx3s0JdsODLeGH2SqsW6NfRPVujZYza2WFllnNaKCNSzuoiBvw7VhNv60Y9jrrY1zQhoSS7Usm1LgvF8YBL-zGc8wnKTbWMIXuYf0OJjw_aM6GkUmFcO8M1jlKXrscERMG5POIu4ReoD93zvxlAeE-uLRTAem8Kfk2rNlndSLOxXHwEwzGVoRv4wkzPoKDBXxPHPwOa5hwT-7aXCBBbTJLCk97EtoF0lCJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyN3xECcfEUndGNknNB5iQooNDKKc_dyfF0ZgVuJn4G5Z9c2XSsUdHNC_Px0lhyfE0H4YtakPsLPfrtecKD07FNU3KJtwPzdqRf0IZBEflzuokYSCfMlJaeHL9KmnEFjxLP-VInlmUliYos5CsmpdEjn2PUNAxwqSpLUU8KJeTj4NiOW9SPIEV6oTffylgRo-t7b-pZMbgfH5CTZ7MRWatpGUnG-_l0IKU3aZHvSPAp6JCQVEPjArvDuhGh2gAl08Rspz5OWZx2MorsDV1gNO7-66j1bjt6QgMqsZ06-40qXl_uW7H7C8vV5zNtiZJ62FLfkwSukD1vadUo_nannSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIyd9oPcINPpLqf6siGab6VkGDf00jKVZ5SjuxYN7xYh_04vQhx8zTjpX6FxTIytn1wxXrAXp9AiicH8tBQF5jXQpXp493lNjx2ZSxomLsFmZ0xnKqZN9ozLQCp5SipqwRHFPmPborgtyQhXVXQxKWau1xx6xs8fBc6VUnoMArH2BQC_myploXGL4BcHlYOq3BEcEQZF4OBMn3mnqcNudHz5eLiNGOho31sc_vRe0gvya-KXz3b3rXkxjtZdOvgVh2TZreUNnaju-vVi4UgH2MpTzmIRtwhU61NPiawbYo3vzYDg1WtjWERlJ5JhHLSbWPbLzPRoarU5IfHb5jSmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=HXqJ_92bOp9dl2_WwnaCUoyw_DooSy5lUa-q8c7TIjh_fSdLJu_DkIBJyNbgUooa-7tEzL5wGRAjbataTsVfa_gKG2zzPMZiSGSvo-pS_Lk23A5ojWeHZbPDeFkl7WuvzdOKu7K8RMjVDR_GpqXBSCjR7xXHP_4D3XB_PW8aYnwwTv3dkg_GrDewfnhuFDGxlqW4DVnjuw5SgWYZ5QLhKzCyvNYyZo--PLkBiRTsXovYsWQi_HQ58f5T9TVwtyFZnUd5ru1pL2R-VeQfVS030kKWoCLlnuHsZCw53sTbMgiVgqgsEDkzejhfbYX0M7Y393HQhsLplI2hGM6MUPJvZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=HXqJ_92bOp9dl2_WwnaCUoyw_DooSy5lUa-q8c7TIjh_fSdLJu_DkIBJyNbgUooa-7tEzL5wGRAjbataTsVfa_gKG2zzPMZiSGSvo-pS_Lk23A5ojWeHZbPDeFkl7WuvzdOKu7K8RMjVDR_GpqXBSCjR7xXHP_4D3XB_PW8aYnwwTv3dkg_GrDewfnhuFDGxlqW4DVnjuw5SgWYZ5QLhKzCyvNYyZo--PLkBiRTsXovYsWQi_HQ58f5T9TVwtyFZnUd5ru1pL2R-VeQfVS030kKWoCLlnuHsZCw53sTbMgiVgqgsEDkzejhfbYX0M7Y393HQhsLplI2hGM6MUPJvZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Moeeo3EbLzfb0d6PqG1tluiL84-EqEW5l6fOyRhg5lun5_Yt5FZDRlhdFC-weTRhyWEnrTp0j1_cfnvo5zIUMBVfMGX3FToKpS8rhNuUHIA4Ub19hhpLLNoSFby_cnVI4KsrNLf0SnS7IO6DubovwxxTl21baBTL30Jg8ddPeXEDFGWlh29HbTQmKVEyg8CKBnn8UJFbdUEghqJgVzZOdAvJhEOFJiZyuP3iJ2mZPzmbn3LOrvHYMaHqzLGpkfRbnv5dSzqYsJdPOLByHM3Pxxic7mUyjzWGr1D1H0-p2bgkBaEKyB1QYZxA3B9cZsPQ9EGJqes2P1FMS9D_HNBWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8SpoUGBksL7qpGv4NHRhEH_LkXjmQ1QiK_XKiLqs-w_fqaHP6t7b7SLl9kqocxlSemNbGhiwzaGvPDl10TFNqxbUjuFEBwcL5vwHGPmsYTLnbV34oOW9zh6jKcd_Y8811PGHUMV-119fqeUfj-SxB7tqBqWq40uu9SqM1IgRDzKPmdym_6y19UItqlxHtw6KrOZOSQ5CqP9I_-Bmy-yrTTNi-R9s3p7PLH4EMAd0BlFFKMzTLkd8F_DPKfMWOf4nmgoWpSWT12QnSBByF-fhnGj-v0iDKqjJ3SZu_dKG5JGqCJSeMzxBUX4L4rfhHMQc7Hgm09iKPuY5IwOhh-oyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKQzsMrdunHKSQt5QYtwe6sXo38htZYy1IvX4kS-93FnAvJCg8ZuMwrpq84SbiGgr-tPA1uJXzIypvll1iYWTwUWLGUAGoeIsBuxIqMEFrPCtWqJYLXQRou-oJ_HK1wKPAW3CFYrdm8W8nAyviDLtjCV7DvwvOkobbtPv4JH8ohepn4gNTHjZafiie9nQnRaNFA_O-oaioSaPQg6NRn7i7DmLij1mzAs_8bMB9UjWce8eszE8LscSSCUPECa671rFnK_2BZshPHZpL6dwnxoscpRDqWrnV9u-B2acEWUKl09FtjPr0_fYdBtQ2YXvRm-lmjRijIX2Hd_2WKW9w-I8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7LgOZl6LfdV2ESlwdhlBKIZm5SmbNOrmFqq3pX-i7YlUGHkBVXZmvzS6e0lOu0plSjDc5PDlUy5xFNvDMrhD-DccC5qxHgXZGD6iGd02rsR-Ad1yQkroJj5kFl4umd9A2nLYI1QwzJf_x8hKzFTabHkS03a-EOlhoerNFHztHPIp54IonGJ2S3qnAArUbSdEBIy-2PItV_rdS7iGhlLsmpJMZwrlTeGzm6uIeq4bYEXcEyUkoWiq1rc-JBMzdUrKQGGNJlYywmTL9aS3nm-GNYo4JDtUT4smFyuI8VCiREZYF_M0Yp3_NW0pUpZnYbGLJIhHWS6r2z3GDqnfuNf_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBMYj5nYEad5xVk992Yo9zmywr7KaCVlXIn7BNOUSIDDZb0cpuDuYEmzOKNEvm4CmdoRzygCWvD0NbstmGfYCG0OBqINgdxurMvsZvHbfe9VAJdbpKUGW4MCAxudfDRvOwsHzgru-Ccay-zVImbYmqGpil7elCikTkmVFBk2urcg2PZN75IrgXiQnoabEKuEg2noHuBo5tEYrQutNmRZb_Xa9v3_GGrAT5MoHVJQt3qELVHh2E9vWc2I8844Ua-KvyuDA982ApcqF8q9kFTy7uyw7xa3qbqdeZGqMYa49w24Qccwn8_3jtmExdyom1o9bfbF-DAUmSiXOSL5IX7FuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6Fc8L_ud0GvozaHMbd9PFi4pUObjj8JJKoYW_aF0BZo44qn240clJh3uGc5wP4bRdL95IPCUoDgH78s1Ak0bA1Wz7OPRHISFrJm6mMCkwUm7jsfDPoCLCdTIFf9OhHtAqbUo96w6NRmNTwI_OFHOfUjSMFaNmDNjNCIC5mQdrJ9SqQDz0SOPV-kPQaCPCKR-RWxOMxmMqP6e0b-y8-dJrYAENlWWs4paJGIuqsduyHlAkCzWlzyAkJ3teuPCpZb8msXSmUoZL2abaB10tMhyeQAvOwsDJQ_ZW6MKnCNBGjEAcgie-0w4afAg8mbkUx_gftjgsx_cOl5tepkTUZ47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3DJBQ2dlW-RZlsug4sNqBMAou79T2QuUXVq4Q8Ef1whbQZgiMEVRAlr9ycv6ze7Ch5w4fFfcTvYioGeWe49uQoNOdjvQ8JnsSGXhv5lkhhNa-_hbaM2FbKFgfyC6TzIg7Z9RAhMRks2gjVJTbt6uLZgTHXQZhQidqioJhIls1Cn0dq87Zo4gcgwhBemtFne0zxD6B4uOcOTpu2mj3ZdMi3KrmYQ_kvjQ1oosnoOY09v-Pu5CFVlI17a5M2gTrDgi4lbLxJX5_y3Au_eJ4FtaxnNlLJXtJw5TTAh2RKimq87E1jL9lcaXlqZu6TxCb4UEpcYqjEMOAOS4OFaiVFcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=BFui-RK76j4x_odlQg8EiMpRdk3PJHEG3fao7kmH938Zo_Swd0D4-iBekV4rAbhLvKDO3tDB9irZ7ttAw1IfVYHnYJIkNYrBp8Mv1klSyRXUjxsMjpvh08BsgiJVDoOWBCk0R9jsRaatzOZlH0R2-7MRPwUr7XL4YMjSgqR7DvJb2XPOCdPwR460jnbhN9PNV_rmd402g-4tTnle1Rdq7_8Zo4koY2EfKoc1vKSJC1jV_Va68ow2VMe0kuvazX8VMH2E5cOwAv5M0pq0FENZjXRSwIQxYiQ1IaSveeHd9-CQQWMOGFrk0Na-C8OD-ZhReJi6T41jYdUvUEEnqdkmpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=BFui-RK76j4x_odlQg8EiMpRdk3PJHEG3fao7kmH938Zo_Swd0D4-iBekV4rAbhLvKDO3tDB9irZ7ttAw1IfVYHnYJIkNYrBp8Mv1klSyRXUjxsMjpvh08BsgiJVDoOWBCk0R9jsRaatzOZlH0R2-7MRPwUr7XL4YMjSgqR7DvJb2XPOCdPwR460jnbhN9PNV_rmd402g-4tTnle1Rdq7_8Zo4koY2EfKoc1vKSJC1jV_Va68ow2VMe0kuvazX8VMH2E5cOwAv5M0pq0FENZjXRSwIQxYiQ1IaSveeHd9-CQQWMOGFrk0Na-C8OD-ZhReJi6T41jYdUvUEEnqdkmpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvrqgqgRQZL21NB42WV2-T0et0K3zFKsbdfAFnRNCamKy5-GWv-toPf79uCEDbwJbIuykqc9qzQK2DqXzDvZc4hoMJkOfENSentqjJCqdTsq531EvgkzzKyMosqKCxFYrdYGj4bxGlDkccjYbGp4mCiApOukulzneHA2FLBVE_2yp7FAEXIT3YWUsq4rj1hoW52Gi7GGOcND-OPCnfXL3KqZloBcwxPWT-STZYM83JFgUdkttO_XizKK6YhKFUadBxBAIICY7zAeyFgCBt5kJ-RI3kSWI3sWkwG0RC_R5jXxCSJRF_1u90Mu7P-dLBxAG3LJFtMAYSCmEuVUxlWKRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQqjOp9RZ4nhvKO8-F5BsOvd4bx9KZxsr_SD1ewqLHUDa0Ly3KRl7q2DxD7BpuBQaALxxXPRWej-Bn18C4ar0aV4lLnaMjQTDKMLV74_kMH2y5OG61I2Xh0hGt8ljKSFJCEi6fPve0ZhBdjVIjA9aj8Q4mvJOEcylvVVsjiw0ssKrEa0IZgDwXDIlm6ZVKh5HWXHCSvbocbBwkY25LeW--WxbUUCd1W4j_fdC20oXaxUEdHihLfq_U62Go66dFCeF6t_Pfi8uFGbnicWpkHZ_1nDyYWt5NMo7okaBKgRt-PjcClaWslEOueRvvZw7USWfwVAbf4fzLts9QjdbgzyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=iQuuN6_9RQXAUyHe_bIHPq1bdAHEUIB0TtJobULKCy9j9ASjV82M4KtjuownnN7TPM_Dl6PXjv-MXYO6Ri4Mw6PbinpSuJZh0Nv0P20kvoCWryt_tSKPQJB4akb3bmFCxIgTkZj7l3UUUyF63ZNGL7a0Fv0fg7ZV4YeEnKYYEKeXXVc0pyOhjPccoGD3uiHGd4t80b25F_7-Rc-SRCXutZCvjUrInP42X-xNdPO8vx2wDiJLCThELoeBdVacagsA4GivwONDUxsLGIdPJf2oasQsSwoLzb8WCRYkoqkXFNusmaekMzXukYKqdNixRzYcYHSLhSmPFKDApgtgex7d8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=iQuuN6_9RQXAUyHe_bIHPq1bdAHEUIB0TtJobULKCy9j9ASjV82M4KtjuownnN7TPM_Dl6PXjv-MXYO6Ri4Mw6PbinpSuJZh0Nv0P20kvoCWryt_tSKPQJB4akb3bmFCxIgTkZj7l3UUUyF63ZNGL7a0Fv0fg7ZV4YeEnKYYEKeXXVc0pyOhjPccoGD3uiHGd4t80b25F_7-Rc-SRCXutZCvjUrInP42X-xNdPO8vx2wDiJLCThELoeBdVacagsA4GivwONDUxsLGIdPJf2oasQsSwoLzb8WCRYkoqkXFNusmaekMzXukYKqdNixRzYcYHSLhSmPFKDApgtgex7d8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsSDWFeOp6kjaWyNEPF1WPYDvhsUdFdjFEqd55sESHc0n6AyIKMeg9Eed1Rp3ambpOC1FGgjIz-DN5jfPHB_cYcjA6b-FbTSYTJKRI03P5e2YCNEGzxF2kdGG5vsRKR7qDlIPFRmc0rgKTcfzd-rztOaVA5fS1OsVwfrgQVXekTQRxXcUSiF9I5ZPbPVmDLt9JFIi57T-Y3AlGpsZDX59n3l_xuJ_43yRFiRFxdInBsordPy_t6HYaNUOWqRtpavcJI-tpMXJyW7JmKmYiBH2pRmALK5HhDF8sFpugWl0IEIK3zoIzi6B1AvS21f_tDZ1S7ZEnaddn__QCnpGb6LCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5_2-eXy1lIUMWhMNu4CgrvyPvHAfDtvsqKk4qzc2aHK9cAqtqcEU1x1MpIU4t9K29n7Ib2dW2cjhhQGMSE64PbHxlLHI2g3iBtMiXqW5sbnZ8VqhOGeOxjPvxKbGU-AgHmbdo1FxsBHupwfJh86AjbIE2A_KQe1k2Sl1pwv_wMz_6yyOokMeAYO0iUXMkPecSzdp5mk6X2xlN6JYkFqGp5oXNh2_Pago8beDur-eptW_lmRptGeyFCi1WjZSjdIU7PoMyAqX-QFy4zVyhpLpahq2Nia40FEkXV-Xs0cDnZ0l5L1A5y5Qd7DOI2TOGjo5LOjQgdGv4M9iuVF8jsIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMwq_6jYNGQMYMuLGnNACVlNwPA4PtyFeoN50b5IUSC-NK0WnoSZYRiPxqtbt3412k4HHC6PKc2SlB4jy7w_JpWLssKy6FWO9HjC4U6xclP19tI5fyl5WQ7jLqZQdiCIGv7UhaBS75tPBxK65ghktBcG46hlzc0A8rCuKy1QmFz2B5sjXN0viMLS5q_gtw9eE2Y-5vFoT2BR8ELcx2QVSuGec46I9FsJQvwiaMkms3JYYNwyWxBswcLN_88fdSYjq4v9CLQs0qUwJn2HnCyifRBMM0b3dJ8oXyFVPXnD4XBLu8PjwvTX7SpRD4fPzOfjynJg3GVC1p_e22GDtOcCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V83FRve2F9R-Ti4AUDKd28M19QL-pgYsVZC2Arhj5Oqzi3HypyRQzivB8vCNdCMwc5wQsWJJDFtzN7Hz3TlbcDe-z4XkmfXpFVZ4KvAKg3gwz2JJgmr8uszywrX2FF2TweC32XtNeuzNAbfYOsf3fBPZxImwrnlrtfN-tQPq-Vh6daSTdt_-Dd9fRSXW0BsXRPIg6_zHR9lgc0hIG62td6UbgNQ_U_piqZDjEk7BXYTO45j1UIN2l0Zw25g5cb5EWrMQfHSl68Xlvc4zyjW6Fh5kBb96W-Jc-17e7QbduONNOE6UeSMsdgH46Ywe5Wx1-J_pFmRDuwsD3SuuLczVeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=fg7PFvLujr4d6FrXV44CTz_n61ZD6ytfe7ozZ3LlWC0L1zC4kCXx2djIsTAuv7jiSdTqqLksXWhVnUlJhZD5meFTcC_uBF3XVfrD6pEl_XIPR1Al4_kll4GTx0deq8Dr_lZ1KicBBiCEPQkIjRLvPc6C2E_22rgNTcK_vRJ0ou3IC0aaFo-L2wixJ_noXmVTxK22HhJc5Rzv5_gXOhCMbdJ-r1w8u6popXJ9OdsCck_qu5PC__ccbaFcOLB_RZyRL885i062WcJoOBGJzFySfkIxulfBqmFP1acBJabmaTDvCG2osM_bk2mrd_e5y5m6Bke_IXeNRc_Gtztb0Gmaxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=fg7PFvLujr4d6FrXV44CTz_n61ZD6ytfe7ozZ3LlWC0L1zC4kCXx2djIsTAuv7jiSdTqqLksXWhVnUlJhZD5meFTcC_uBF3XVfrD6pEl_XIPR1Al4_kll4GTx0deq8Dr_lZ1KicBBiCEPQkIjRLvPc6C2E_22rgNTcK_vRJ0ou3IC0aaFo-L2wixJ_noXmVTxK22HhJc5Rzv5_gXOhCMbdJ-r1w8u6popXJ9OdsCck_qu5PC__ccbaFcOLB_RZyRL885i062WcJoOBGJzFySfkIxulfBqmFP1acBJabmaTDvCG2osM_bk2mrd_e5y5m6Bke_IXeNRc_Gtztb0Gmaxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc-i5F8JTTUJu7fCFMUaK7qh8r4X1fzynCoExB7TTQzjEWud-5GUKMfmbVEtAEgu2TgG2sN50vWGtkdHDwv8un7ZCUK9uo2n1p90pUC0ajZGDBEQYi95Mrjjrs1mkO7qfOd7uTj0OJbQo4AbZvvDA5i-l8AkkicsgSrg2YXQ9ElgjQUlTsL8zaOAkeg2zfh_htq6JyAVpHuYvRg9ZChZaotnTlOuhQZ1yyt9kLwGPif_oDoihkAHpOgVokl5X9zprwjzxU2RlY6HFSKYwziQ0iV_wF6DIvNRrwL73q37JjDiaraiAW5SBfXyrO5HW1M9QcgSMUomg3ttXfmtsnW9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhf-BmYabGUeCxw_PAzyHhOowQKGdSUTSBqYQx1UTEgv6hjnjQL_flYiAKszIetAF60EZ60qb7eDj6ykcNtvlV5QeykdrWWrtj8RDsmpv4rO5EBlFa_rmsuimmS0_vU3FeBCn_M1cUgXlhXTh14_n2BG8IVUNNAy7-7tk5z9UiEo6out6tQu_VThaOEPZ4XOfpHrNkvVhBOKun6F0cCC_NcoEKiJv03nkkVRq7xy3xVraeMeOKEkjhgNrpVbG_C85SGefPD863iFvqzreEiM04twhJ7gvcLD8E1VGo509s4gUNlSZDA2glM4kF9H_lnF_33onUSNIjP3m_wiuAsYzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btXIl561E6BVBwqN7RbsUqMNMoGiqxJq05v-glS2v50l4HwxZp0USoPicqegYPL0x3uB3DPKVzPZYtLyesOeUtqNxGkyC7yImj1JKE6DMzsH-c2PF4KAW-70jVeR3mQK3B5TpjWNg1d4PJoOviJcW4CTUdCAeJpsxiX_uj0IrUI0cQ4oG9c5agYJ0z5l6KhNIfPiCfm2PGYQeumr6nYNX-sK66s1usNCWW_-WJtuDSpumq4HpRYCh42UkcnTmXsAVqDUFvlsjM9bo_DFxfXw_4QDGBZyjeEOerNyyBHsY8xDogXMQl5v5mbBeLZxyEsqPmUU-XJvttlyUDVF8lS6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViU2hqoKuR-ZIu7nvvl8TE044mwO3XPERgrQcdQwiJnhgYFdvPkQtGJv-dLCvXg5_PC25AYO7P8xGablHdVEKVifTV0Y_jHe5aPP0z1aCvppaFQsRESMP06XcY-uBm76Jt_UbKmv8VcOKmVP1a8Mlt4JGkb0lmKp11aMqt3BSYExiriz2aqKEBKRvBOPEKIREmEd924koIRhze7pek_vKwiyoYLKp66SYDL2RZ6pulmPioleHsKq_SyuNE248ULy-gIldbtRmMw2rqi2esQXtyqMWAMaSPPzOiOaA7-j204g7kxwv-SAWGIxs9VpTyrWLZ4ismG6-31nqwWNHKwF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5piW_GgOT5XCeRiIeLDh8WqfOuUsnlgVKplx7TPF64NApqfmNfPWJoynHMAVa8hXUL8kUR1s_JT84cRwJ3C2GH6vERzR1y22dwXsyaVZYJP7kYmxFYqIL8shryIKOvyNSlGobxqnUWRrZ701DTiZ3ZANilEXNox7XmgoIKW_hjhbeFyXmle-UjrUPT9FIqi-F0O7bKnOTrhEYz0yIgKyVsGq5fBU-GkECwN_vY_DpkbMP5C0E-rP0JvaXhClA_pgsE_VfDZ1HMi_3a9BHxmf1QFEOZmavCCxfIJcVHqFgfp55ni-ZX7S0oyPX1JTfAyvmmFPt0TOZiMv_vYoVsezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEGeAy9EyfS6HJSunMq83KXgC-Zyhlrd20c8XJoinu5u6X1K-TDW9wxWjhZnvg66t4ueeGgME0exIwDGozcrwlIo-1WKdPoG2EQpaPC2HCS7zNObyvbUvsAQwKH5bMra9hnjNNTvyAM67YhsVZ6TG4hyTGB19fwNx0XVfysfO2hfmWogX1IesC3YzepKf7OE5-C6VRN_Ujky8hZe-f-nOcApSY_BA_oY7BXqCRO2fSkF6-j4e6pUYFoHTxie2OTlLeOev7KU3IkTc4UATA71YeIHBxi0rEkamoJk68XcOP3mCtN795jQpcz9lSGzX2LhysqcDkxmzD3GBdi8W-ACcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRlXhIBNRdmZRykM3FDVYJudmZzCndkf9DKOOBPdTo9P3U3plXlM5VdUNh8cp2ZBDRv9K1s7NLX8ays1a9xKIaibTisdBFaFaRM18FWyS-lULiHnCVP-HRoHu8JbTT9zdqEatgZeGVh4b8jrBXkqKCuRxp1pwTpRQzepbRboVhdFmBJqHrEgcoTbBPhg-7JvzBazuyvT4RmNXE-O84WvJKOussKME9kZ9BXTkQXI8gtJtUjxAnYKRdOt0eU1oFQG4hUyNObAOrQxgZW1Nxfz_6lQalw4r6RdFI8RoMTkGqxCU_sBGQXzsSWx3zkZ6BHMd6zq08Gmh6aE0CNR9SXnDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXXNy0jiXkK0cTi7Sx0pxRvqE6BjFrSl16yX-kVGmQb5mpWnzcbd1kuyMG55zSYTn0MCNlpECyNuHL4onbL82LAcvfPoTv4kaeRwdBv5p9XIpwuRuluFYeXvNdPR7k9tXnrg8D6pXh-6Zx36Hsw8nb80cCLblCOehj8thNUAT4kmEvzBcDzdgOGrnX5OAxM3b71-qAGVA1gEqSyMEhJvPRJOSZigbtSCIiJqH8NiuQhvT6Bl5LnUprggYcqERhzFnmPwpMWQRtJ0Iv9ERw3TeuOIScBqnczrnoaomN6Y4k35WI-uIRGS6mzRwlgae6W2HlgvcQtC6CdzRsK42gvNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4yV-etbmRTQ8OokM0-GjfdWN6HEPv628WVjRETv_Lba2sR_BzevRt8iJptYeLsddVX5JXyzZbfXIvAMXx8K7tFAG0IJt10MFtaZWBxOtuZngk1fz-4fSZ6nIMl4R1mbakHzEw8Epr171mXBE5LGnqo4vr7Mjg4ofVtiy5L_nGSFx7pF_rZ73CFz-HdTcbHGhqj4cvd4PyEWT8pZfzpRZhl17gp8MrfSAfGjkyDVX1jU9SmvrHesfoefqQpjYrx6WDpJ3fehkXQJSk67YJLBTARrKo38ORqidJ61wu2k1pb024NwQiYizEyyGb5WuLQiZVRqC6BQk06Vu4W3I3-IaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA1KkpI90x49445haqWtOns7wPtunE3Sm36GzJI8BJLW4Ssjo4X-2xk4zP_aIeb-8UFRsquRfVpUmfYjO3g3j8jc3Ybo_07bpTP4qnrDB6KOflilBbb-aYl2RTUhIy_EblMNGf_-92GkO4qjpp01E519u0u0JeY9TShB3sCpaXGsyOz4yIpvMoU-Zdzpf-oeZC1J3gBc-2sXBIrk7cc0LF9t-Gjip8rrXhgF-ws_IgCtafcUiRwk5BVtrqnciFhBfWBljZEH5HUpANFQ5bM9DNBoFt6dGKHK0h-Np1ToLyjMPNwAyhR2xgO-bWbZWmJf_MfDdm2W35oNIKjFF8dNSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOX2l-Ds-uxzMIh-0Lc80QLiXoVo1DxIv9SYumWTE7PlDQkAMXyRYK_iuPUqLUdZdY61p05dr2RM7NW4o6e6Yiwt9XTiBKf8lwuOccCoXvqtZ1ZtAj2N6yxfj69zUqzyRuXHvy2J7ZY-fZUlfLzZ8vTVsMUyVSDamjvMEW-cddZUIwDEFIvVjTjZLy3VFabFzj9LXd5Dvv-B5myLBOuB1QbBkzNFWxRsC7j4hGj_Ne75MTpY8Af7lL5uubfnI1Bm2Pf0DbO0EJoJGhGgFHfelUeVdsYnsw1XDmfRgVXaxNqsEj2-0FBuNauwKl0-m7J3WeAY7cjuOaIRW6AWTkeQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icgyiyN7d5QJtoM1BjG4-gZmkRVOvYBYrJRFp4PowYi0G_-QKGLH5TonwMxSRMPtQD5a9nviGdg09BI18K5PEJy1dTmLhCTNXGo4IoeB9BerfILCR96Tc4eNFrahm_z8LX0cgJvuDE5oWlMO2tToQwbEUooj9Mt_LygE7XE7sQD5DjsEyFkG-gOfx4XP0Byb4J3iNe1MF_NXF7cQdZTQVR8cYJus-KwJrFwl5e4-ifTd5VUOhsbTevfxaRANjVr1hU1jvALpJd4T4E_1kWL-OkpQsREyjD2V_jGSlOn6bE0_ehhuz9J0GytNZHSfYxKXPD86sQBBwtCSXHxI0LSibQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgvLjfNucydc1Jy0k_krjNY103tUJ1I-BADNdgCc2OTIwyL5yKgqZBNfiqEuXCjEmSG_XxC_KvzFtEGHPqpIkzD9l02de0qfD8zWsdFtQafPNEuzSFeLvrVMM1qPlZLDNZ-z8-K6gfWWOCcOm_kzSw_Z5cAgBN0CZD_YEgNOIOgTsynA4BDyfde4HpcxkutJdMxI8UUPxz5CBqeTU2Gbv7X7diyUJCHVDXUadx6uojC7-qvYx_JCBLEoT9PFH00npsjipSexS9vymfm3FKYGyoRGGHeJ8fPz2Nj9WyJO9MBLlvAJ6hDJVOieV71Z9tIys2P8XpyHCqmxcql55m4xQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hETJaLA1gqm0vLGNlYeE2kJRw70uu6-eQZaYBwzDqbOLwzyaO1TyhUw0XPisRYBzX4Lf17mTkY7YlDz92jzanfGH7XBZpCTmphkWhsEr9oIXwgLmFKZxSSTglhROg3FPVMoqkBnXcS1nPPadvPNAanGfeEwyj4nd-WC_MZBDmfItJYIaKBJUTLxrhFrseuHgYYZbm0X9wdqlXbKwQRv1oqEbThO7bRcgAO-kuFJJhtgTw41IY-V0pIR12D1fBLtsEOBKGvJqGkkHVGB3QVv5ux8X_9VJzWSpVIOvwyyLGiYJvAg3RzfB2J1nEQy29Do8Zq32g7zJo_E0iWVQQEHM6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE3JJ2mw37NGv8rUhdmCjqQ0TICuiBZBOzFqUivr7UP3FONW4hYrd6p_NPPKwtDH0OGwsxZA2ta8atfbQvJFUSHhhW9l10SzN2kVlcwAPrASMApClj5I_U8l5lCLr4SWiGNTYHB9oxvvS6WCCOtBhgv2p0Fz0W48WS-_7-FlOWTkExezYbxqffUErPSG0Nj2w515MQ7qDrDE2pKBM0Szv9-rB2j8ezGoNzktitqIrIXaXZOdRrfG6onZnG3mrOQ4q9CCZUAXbRn0Jqy-rsRbUhdcgMNEb5X3YdBU6PSBA1Te-Pc6U9PDrd8CBLNWqe0CfGwdjDzxThhPWrXFHy0jlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI8eWu13JeIxFADS_BaeSJX4uZlb6tzzkqDHJRvzkwAuz3APo-dXosaxIaAEBaqgWmxKAKOAKZZnYqjU0gN-yP9TNtLTofQH8iC9txl41CIYQDCbXa8wWNMmM0u-shVzqJs4BHFKsHthqjmqvKzz5_mOH0OJCx32SSqz8EELekYuImbWEm0hGM9MfFs0pKSg082uwtLaSOXSanSVcmNia_cFQ3p_ZssB_Vu6IoZ4u8iutDXbRJMHgaYs4asDkLQkzwRjN5FjLw-zqwTHw7K-dL9FMGE7Klpk5JevgSNW-LsXjWnW3waxyJ1k3dtYDUigu1MetIe9aThX3QoE-Wam2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hL-MPNTGKLMofQJQ-gt9AnUCbuc3OFtq77ha7UHkpoH3DAkS-vGB2HxLdUnTWX_-uBaaqV9A5bPmXRzV6bNX28CHJG2MIEq7ClX4b8XqXyQadjihjwokoqmiyUqVLBnsKQ_8-aGSWGhlG7YYJz5Oa-fCstJpR0A_PxWGX6SydUk_PQy0peopmHdJIRIHOT_NZrLEkWC2HszmEZAF0ljIbAqAv15yotow7mK5ZgzV9DrMA6E_ua0jKJ0Q2FGAC7gNtvQqJA1bXKaTLdfEBsb46NH28gBMuMGzHDW2rR-BvwcR9EGvEL_6pmG4G6JH30sJHg_faxznbhPKGdg6MZx_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYOaw-MBp5IGxueGFA8z86ax4O6jCHnqcNkHFXQhDdmNkMkL3IB8J2P1b_LZCxgwaAH87tdJ49-_Ji2IxDhdZPFqPYuAaDDp5uz4DJdx2rtIRO-EosDP74FdZ_SiPVOOdJKlPpWha5jXepelD67BucUP3bkCtquoJUfsi9fycRoY6T1MoPb7YNiTnl-DbmNOn_PPoj73nulQRFKdjKkpoSV9VdmBSajbC1Y0CFiOcWdRyg6BTpmKeA7mOYYUgp5MHUqyz-JHtjKLziBkYIGFEFoN-bfHYwA71YGqc2tRAajovoBxj7vbOSHP9HxblXZnCvPaKvp3aB8Ga0_YzsS-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7eLjn0Pa2rpP33B1pZJbEZvzZ1WrRjrMy27yJ71Vt-2fTeYa84f22opjalzabqalewUNYZWi2S0sH-N4tymsFYLeCvif7IoYqZSKADpDus4ONXZar8ChY0VttPfR-ZhAkgJmHKqK72xuFPPgR7LzX6kBQ7p3F9AS7Iw6F9tg9T3ZNoZlN-tkFp10SB_lNJ94JxCAaTx69E4ofn2srtqnnKwAbqY-7DQjGV4zLhYUeAbbjis9hD7tEknrzvcDmNnJV6EbYW83tGsGVfWs-_AUDx-pMGrYE6mbKaoFTGEo2Kmy-hqCtzxani2HgUkbvdlzedfZ7tv1NbxV-SqKGz8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5oIbw3STQBHw2_VAz1HLuSNxfToqPtVMCgWNcuj0EHCZIZLwNv_JYRuHxZ1SaWGHZK6Ouye0BCxm9XVmi3tRfzF-Flx6-80b9dd3W9ZIlSgVReATPYqet0jGQW3yttbQNlMvs-qtqZXg_VblRNEshod0x5adkPaZ0pDcPOMe4GKkcQkR6RuwMYkrwraEMugtnXgia5yAN5TRihVqh5-zLwISFGWSfR2VGbk1oh_3rVxkm4SpE67iLBb1K-ovxmjeID88dnq4ZTZB6RMfuuVf-skqgN7fYvUZuT7rzhIQFNJ9rYV7TzhRmIm87PTVTe-gtLRD_MQK9gNSa4dIjXtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmflcQEnOEjZUnUuUNn0zkiumlWYafMjl1ea_zRLJD9OKlxrbGG0-k-L5VyhTcs10ZtWeKoK7P97P2redtInQkbEel5CH8TC6kAIv8XvpOocF_qpktUnrMdJJURANnkl-7H2p3qaQEvSHiDvPXdD0b4HiUGVyxymeB3UUOfu6B-bPwXDv1JfGGLuXhHrkNeNr9UAVhCvmuyBN9shTSKcfrSl5HMEgmTrdFJmQ_hWkwlVoyk4xWSHm0-ABFI1zN-EyaJgYbXbpRFeUvcYi7pYONkxsTEtbVK-a41DXAgVNRdKabxQ7gUBzl1QMz7WvJto5PcxT-K0Ie0iTsNH_fHALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2DgHwGzd3dCEA_trcX4cUepfFhgbXd0Dgg-NZc2kSZyo2xRaS0dcnvYJD6dBKxiX-HESerfFq25iq6ogG7gwNvKMbIDan0vSVwGDy1adWbj0kP6d5-KiIVpe69iya32dJTXRfEN9aNPZi51ph8-By8h5qYRJAlUJcxkEggcrpmaH9Ht5iINFgqRs5hDESAczWHALiBSXnOrv4x7SPh9jMq24HWry-f3k16kIC34sQNhBMJl6G2nhQp7_59SEKCsb5e5UCtNKPHTHf6f4_NrvzV6cIp--Ttid8xc7wehgVaDw8mD9Fuo7YwcxrWy8d7Q5upL_4BHgoX_lfyRkJSf2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t99a34sfcLEUBWFKbSYLCp4w-U_x40Jol8dLi_tHTAOVYkVijD9p3DnLDvxNOHTB5WNsymMwe230Z1Q8xcrPfY1MYtTw6Gs3-taG0Q3Jg4jncYSA9lTgVMgkdVIiIxsf5PoEOr4NXCynW8B1ThAszVWe0OxWCCw1uCHwHJcrXEk6Cn5m8IC1F5ObnPpvnc2pWvgNXemK6sZ8FJnHWFcBvYj5iio5F_rakqjIA9vMQNyCUhpFilt-kvB1LYChgjd4mp7qqYg8FpqAZ8kJPnDk2yHcXJMHZMQcGaGdmJjrL_BEh_d6GHy0q-cHdtx6oKFxDTPLxQxyxrSrSbrbh02lrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIX5CKMufwB-xz9Oc5jweImeiR8nF-8Tdfypjy1uU-_6cRuRkt_PtO6WkVDva5jhmEeO0FFb2NnD58RdycBx6B5p9fQG34_vafHnKzlgqGnUjCTFAmeRhQ8I49AX5o0rvZvVtOjAkEgisQ8lElNCMVlN-FUkbod_uD1cCEFwq9yRfrL9wHO3AOVh9UiPV1OL96MT29FwVa2ZdqrhRnGaxWkV2G_qyeix6paSgvp13I09CQkEa2sx4y9Hcx4bD803k838QCbr5_UKDZso3d9qutf2B7-UtzMkgD3uvQg8IL2TA4DevcpaWt1ojwyxn6fTd4bZuYKyakQHmMNOMH6j3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuqDrmSIIcuaIhF-zOWy3wtgvF4u1RZgMN95Xj3R4Iu0EeT2oPQicjzTGzZkHii_C0AaZKsTku-_YSQ8n1HgeATqVCiTVU89BELPRBepknD5W_81_SECYRdrxnzfrM5Ecsk0ta0yeUSjAIHtpYwQdLmG9_-Jx0VpiJxrN8rriJzSDOC2bO1PSLxw_TAqTkbpGEiEv5f42XYabK9iatYHsHHT-TibJfs_ajbEyR2HMZj_rdojd_WWomVW7iRQysAcDHfEOfpSCFD4VoA3VuyRcqxxBCJTaa9DNSIJ79jI8gqtFae_zXzQRCllewVu60illlwtVngT1qTEyB5A1K8NXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqoNCoNixJwyktXt_fhIVLSL3Xw7lxdIW9eWopg4QdiP_c8TUSgMqUT1jfgsBN02PQJEMyI70D3aGlSp8q2CYaX9zAdlOO49cjOZVKY5uhoIccthLmjrprh0M89qJabccXhlGQBTtYAN0ioWksZL0FgVjl6_OD2mDGvN4LHnP6umqf1wAFeI4fnMH062N9Inz-kRL9kU0i4rSKnFUJjfMDwnhw2nghumqRlFcEuBnDd7S73df1bwNff-WT2L1uUA4eMb3EToxEQGX66Ad-UU9gU60W8ivDnfjSWFnbPH-CRDHgXCg38v8HvAd2MEn4aOHREIPzl0e83V-R_pK5cLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4S4YJ28cVg_IuXGYLWfCYNetukY-_3GqDO9n-3QNVvToyH7zKbjCUEbdNdgJf8_xzHV_dN8dmK3BrlH2p-01Pl_t-_t_11lOgTEb1mKzyeD3YoW6w6iUUNRRmz4c7x8MuwfEbIeXCkJQMAmIlLkNtpXNtac9Pp82IrXmhiA6dAgwKuN-Trw5nslUp6gGOaLuz5lvlbThWZCPSvkyJZD8L4FTMLfvSvCsYrgEDZr-sD0mLwIUnE_vdY_ejlLbCmQXgWOei84o5Zr6O6CEMsDtPkpMwWcBsyLo9-Ab4Tv1GjJpMc_zF3_iJMw3ZJJzNBzV7WsACNKQDQ-zBsrsP0w-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avU82AlkmCdSxlxqfZ90fEq-fRRcUjl2JoO1vw6LRIaiQvenAP3VJK3qe_W0DR1FwyMyQEaz_l_V0zXLN7UlQd957ZtubkAvjLILtbdoRRPR9dQ6h60YtUuGQy9X6cttHH1lO1Mhlz0WJNMLaoB7WLqG7qNs1ro4R0VLe_hjLmSa-RWn35jzo83bgZ3eaT2FIdTNYUj7cZFMQza71v5tLxFdBfZamaoV1FNbKRp4BWc8CawTNwZL3dy9kLq5RQdBjTUzogq62FKcNWsUs97e0WC4UzcU_rm1lgL5CNXxUtwVAKGUM29cmmS9iJBjMY8yKPnXqiEJFs3JfiIl8s6w0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI84JT7Z6hliTbG4XI_JiBdV_cqSaFZ9ISXUA91MbH3tJBFANx1M0FmDWyhmkSVM9t5kMKrWWJ3dxCk8tvZaMRReFMCSEadaP-zbbaYCb-WzHbnyKyNAUoe_P0QSWShqoZhVUz7EAupxCWKkGk3Uuhmwh16yffHj285AH5ae_T5wSOc8UWmaaLtxf65VrKxbszwdk2stWH7D1wv68pSAFfJpY_QDtjeeTLMDYdyiTdSyC_vqmAlXXcAcL4-bnApMB5Ri9gY0DEjlBcrmRmY8OOfwAZM5-ebzb_JvX1u4pJfKktTflpZmC5hCfnGFsOQnd7OMwbQUeVpDxUhI7DmCAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbsVieXCypj36Rc3YJuRrNxEQvX3F9G9Zfof903StnrghiC0YNo4RER2UkiE09iMp16jAkXoBhyzqWOIsRx5h1_B5IZ3yXg_qN9B_3jLr7kKS72xixwk_oxan8FthpAUyIoSs2uEz0qBA7gPpyVdhsh6e5azP8TzOjr9x6cl0XU4t3-MZ8HWNdzo7U90Cx3A7YpjET2DAZkKg1SpQnhzK9GHFn_KLm0PQFePNe80xLOv-h35nbpJdhasxPbjIpfLTpiVAeeRZIvXkeL8mcrLfRkxwr-aAtDYwJqNmNZTlTx2OZMeSR3iQEthJVZMCEI9lap-zB7Dlg8wGBBUJZs-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
