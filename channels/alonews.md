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
<img src="https://cdn4.telesco.pe/file/h3kEKV1g-DBCh1LL5Pn8OoBGPJlLpPtovy2nA-0yvA2oDK4dJgJ2t2prDP3TpJFy8S3I2H8ePkxHQr45HAOJnWsfJMMMpWaeFcPsr0JNL4__twBkQnsfoEh02x7o84jGpB4RVuuyNmKUrPkGbJiOdA9gkbs5so5V2EQ5iLvdfkLQ_c48T_WnvyAsEk0_3QDjGIRkU68YjtWDlgn_BXsnfftkHvz7ZvlSDyJ7Xeu-w_FZVuht5CtmAqXAreA_LI4o0_nPCCGFxTT1OTFA7c3bgoDS3n3wTEH-6u12iMc599nHO9xgWlHaZ3ghwY8TiSXyEAYueJP5pCR62YabZg3wDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 956K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 18:30:12</div>
<hr>

<div class="tg-post" id="msg-120218">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhCrp38iLpJc_Wygn1mZSk8q7HilgslpFBAOEzDvsIRtg2pn2_qaxhUxEozBk48F5OBY1kFDRcV2hkNQZY2WPSt1Sq1TifnQHTzOuDAwtaQFLpCAP5tnsiqeq9PvgRPjW-uXTfZ2cz4Bz_QQ0oaNgVYlm8fRVPdKHzd_KP29AUBh8EzrCdHhvxPKaTo5ElYWU-xkm8qG9zwPfonYNv4KVo6RuE9BkjRZ9TRntXx3p5kS-p3_e4FVla3y7vSqzeye0mVa0RC3ZR4wc_UZq3cWv_UWZ2KDFx6o9FbR8t70jocXXknUE32ixintImszN8e6DHDKfZj3jVz45JzY8xkXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
هر صحبت یا مذاکره‌ای باید با اجازه مجلس باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/alonews/120218" target="_blank">📅 18:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120217">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فروش کانفیگ متصل پایدار با ساب و مورد تایید مجموعه الونیوز
⬇️
🔔
@FastProxyMakerBot
🔔
@FastProxyMakerBot
✔️
با خیال راحت و بدون دغدغه خرید کنید</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/alonews/120217" target="_blank">📅 18:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120216">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بلومبرگ: امارات به دنبال پاسخ هماهنگ به ایران بود، اما عربستان و قطر با آن همراهی نکردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/alonews/120216" target="_blank">📅 18:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120215">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: یازده پاکستانی و ۲۰ ایرانی که در کشتی‌های توقیف شده توسط نیروهای آمریکایی بودند، آزاد شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/alonews/120215" target="_blank">📅 18:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120214">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر امور خارجه چین: ما خواستار بازگشایی هرچه سریع‌تر تنگه هرمز هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/alonews/120214" target="_blank">📅 18:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120213">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزیر خارجه چین : شی جین پینگ پاییز آینده به آمریکا سفر میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/alonews/120213" target="_blank">📅 17:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120212">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزارت نیروهای مسلح فرانسه: ناو هواپیمابر شارل دوگل در دریای عرب در ماموریتی احتمالی برای بازگرداندن ناوبری در تنگه هرمز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/alonews/120212" target="_blank">📅 17:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120211">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزیر امور خارجه چین: ما ایالات متحده و ایران را تشویق می‌کنیم که به حل اختلافات و مناقشات خود از طریق گفتگو ادامه دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/alonews/120211" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120210">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شرکت‌های نفت دولتی هند قیمت بنزین و گازوئیل را بیش از ۳ درصد افزایش دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/alonews/120210" target="_blank">📅 17:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120209">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c642ffed33.mp4?token=C3gkCu2vzTs6lW9yaIVOfJiexfxf7_KaQY7RDgdM0gcbakQ1J6f5vYUDhqdUjtIz9j6yM26GD0uOkIMzhlitDX4DmDjRL2omoAAl-Dj8SJAuyto-UFGiMTBdfRkKiOCU1w-HxTz8NJC93Qxs0wwlVzTbGeP9Fo_V01sdTYaJl5lnSyANwFrcM3bNoad0rtPH_Y-rQWmS26w4lbEP9jS85yaRjmlE0rS4PoFqyjGP9DODdn1BfEESlbl8xhp2X86rJrpWE9XIZCoc9cI3PSui2K7swRVnowQjyL3MzEYxGCd1QNCiZkIpMR5X6xHxJ96zNDLj6IOU1GyIaZc6O9wjxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c642ffed33.mp4?token=C3gkCu2vzTs6lW9yaIVOfJiexfxf7_KaQY7RDgdM0gcbakQ1J6f5vYUDhqdUjtIz9j6yM26GD0uOkIMzhlitDX4DmDjRL2omoAAl-Dj8SJAuyto-UFGiMTBdfRkKiOCU1w-HxTz8NJC93Qxs0wwlVzTbGeP9Fo_V01sdTYaJl5lnSyANwFrcM3bNoad0rtPH_Y-rQWmS26w4lbEP9jS85yaRjmlE0rS4PoFqyjGP9DODdn1BfEESlbl8xhp2X86rJrpWE9XIZCoc9cI3PSui2K7swRVnowQjyL3MzEYxGCd1QNCiZkIpMR5X6xHxJ96zNDLj6IOU1GyIaZc6O9wjxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی آمریکا : قبل از اینکه تصمیم بگیریم برنامه هسته‌ای ایران رو خلع سلاح کنیم، قیمت نفت و گازوئیل تو کالیفرنیا رسماً ترکونده بود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/alonews/120209" target="_blank">📅 17:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120208">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bea015880.mp4?token=q3QvSsHkf4am2Al49lThT4vbnX55YjlboknFcZvQNmQ3Hn54rshit2ZohoMw01l46r47y4iAecYswJ_W_7dHV_6_4pi4845mnHVqDrsZ7O_u6KMzqZIyNlvwVYwHeQdfsBNZwozRZ8n2UxvV2HQikfDIT4mpt4Vx5OBTzc3cY169tbACYSZmCBgmo15LRhnpbahyvKND-8XdFlTtQjL9Ti4AqI26ckgX1zcg8PFqVSCbboekBifvFnazcAEAaWp1E591M464Q1h5XsJQDlghn2AYEeKfOgKANJPsVbcAZD7K65ywhbGgpTr9Y4LCUofD43nPbXE7HUO8KJahI0zTeQOXfx2dbR8jnIEb81os_56V1AYlXfzwg-6pCuE4dA2KVu33MIZ8x0lajf_a3ZF-DfI1rjVGDkc1UCBLPlsSXp56hDUnyKZelcK0djgjmbEWL9XqhlHgBP3HXZBOffHZBzSelfsIdrchXlCydIwnADqxODFXVKzl0ShdCv75y0xLA8uDjaR-WYSvOH17086ZETF7oMhKXdeuSsrxae-SbwCV_XAP4mo0grHohCtsFXKn7VhqK6qLJicB_cND-5arx4qzZ08PZ35dL85youPaVzW5AjjZdRzC7Vq24M48zkVBP4W-e-bP_4RLgyvXQx65nlchvyiZq3F-HqF61dpr1w0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bea015880.mp4?token=q3QvSsHkf4am2Al49lThT4vbnX55YjlboknFcZvQNmQ3Hn54rshit2ZohoMw01l46r47y4iAecYswJ_W_7dHV_6_4pi4845mnHVqDrsZ7O_u6KMzqZIyNlvwVYwHeQdfsBNZwozRZ8n2UxvV2HQikfDIT4mpt4Vx5OBTzc3cY169tbACYSZmCBgmo15LRhnpbahyvKND-8XdFlTtQjL9Ti4AqI26ckgX1zcg8PFqVSCbboekBifvFnazcAEAaWp1E591M464Q1h5XsJQDlghn2AYEeKfOgKANJPsVbcAZD7K65ywhbGgpTr9Y4LCUofD43nPbXE7HUO8KJahI0zTeQOXfx2dbR8jnIEb81os_56V1AYlXfzwg-6pCuE4dA2KVu33MIZ8x0lajf_a3ZF-DfI1rjVGDkc1UCBLPlsSXp56hDUnyKZelcK0djgjmbEWL9XqhlHgBP3HXZBOffHZBzSelfsIdrchXlCydIwnADqxODFXVKzl0ShdCv75y0xLA8uDjaR-WYSvOH17086ZETF7oMhKXdeuSsrxae-SbwCV_XAP4mo0grHohCtsFXKn7VhqK6qLJicB_cND-5arx4qzZ08PZ35dL85youPaVzW5AjjZdRzC7Vq24M48zkVBP4W-e-bP_4RLgyvXQx65nlchvyiZq3F-HqF61dpr1w0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه حمله هدفمند با پهپاد FPV به خودروی سازمان ملل تو اوکراین رو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/alonews/120208" target="_blank">📅 17:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120207">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrmeUgwNbhcYZiHCHh5EW2_Mb5yPZFogWq4-p8ZlRRqjbqXjPuVF8B811W-zEJftvctcZC1wZEpVSMQOQ-OatlpbpxATRcL27-7_nI7oWCEJTLKp16Q_S8A_vsfRhQfq0DnL9bncROmqXPJjOGkkV1S17ElHhvoDyejX4Qr3ssAYDSwYKibWYFmzdKkJmg13SQhyGbAXXZ4tQ8QFI24W0KOootNqX-4Dcw4t1PXEbeyiLfaP2zBWiTf9UKbn3lBOofDYErkjMlnDTxWPBu7W2BDkAOluKxg99Z1l7uYmAO6m_BKo6ZHYR7C1sFAmOMgUIrdMRBb_xC3--FGrxt0DXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میدل‌ایست‌ای: ایران دنبال دور زدن مسیر محاصره شده تنگه هرمز با کریدور زمینی پاکستان است
🔴
در پی محاصره دریایی ایران توسط آمریکا که وارد پنجمین هفته خود شده است، ایران و پاکستان اعلام کردند که به دنبال احیای پروژه‌ اتصال چندین کریدور هستند که بنادر کراچی، بندر قاسم و گوادر پاکستان را از طریق بلوچستان به گذرگاه‌های مرزی گبد و تفتان ایران متصل می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/alonews/120207" target="_blank">📅 17:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120206">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40a2b1c26e.mp4?token=B8eWY_gWvOLMLwMZlBoZrAgtYutgI886znlCciNfjUKMjI482tRn9irfuCNLAikuU70xaL6pDLDmtRuuTgQk6WjdY-pyhDT8VM8mVTV4wtMD30jrggHAu7EOwbMwtdBXfVggYJxvUjTD0deaDEgGTXVrTcRMcIsMP0vK0tpuuf_EWFqGCWf6dElkOFbHWmZb1yeo4yiQsKfWe9wHMvB4XCEdOglIyjKUXozZh1TvBAszkxwpWSAlFmoooAr1r8aINBf26M7OFN370aqC27ZJ4LmePbV6i5qdi40VqUmx0lRT5qf-MyzaRCVUNKTg5dEn8Fsce_o9I3Iko2rwEJCg3DquDybdE3F_hYV6EydTCysOs8d-84dQGPtsOicS6001gcqFwW1VAe1ahCVZdZtocTkIJwCRKYSluL1yNUXId4l7X6kUIiJNoms44yfTkSVVZ4FnzUNPgQWAA_Tnp3mqioFb4bfK7uO0cEGEG0PLrKLumSQF6X4vQWgzxpo8DKGMwXDLIqlHCO-2mfwghVRlStVEb_nqzEMg8TkT2LLqLcQSNpJ8XTStYo4Pj_dnr7NMgyMtZeRY98HTwQ0b3SuzI0lR8o3YmAkIy3Hx4SoxkOS6fZvp9dHPKUJvBZGncCEhq7Y7HKEyItw6_gHoY-deB5SJbqIeSDXpSzmoyj46AaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40a2b1c26e.mp4?token=B8eWY_gWvOLMLwMZlBoZrAgtYutgI886znlCciNfjUKMjI482tRn9irfuCNLAikuU70xaL6pDLDmtRuuTgQk6WjdY-pyhDT8VM8mVTV4wtMD30jrggHAu7EOwbMwtdBXfVggYJxvUjTD0deaDEgGTXVrTcRMcIsMP0vK0tpuuf_EWFqGCWf6dElkOFbHWmZb1yeo4yiQsKfWe9wHMvB4XCEdOglIyjKUXozZh1TvBAszkxwpWSAlFmoooAr1r8aINBf26M7OFN370aqC27ZJ4LmePbV6i5qdi40VqUmx0lRT5qf-MyzaRCVUNKTg5dEn8Fsce_o9I3Iko2rwEJCg3DquDybdE3F_hYV6EydTCysOs8d-84dQGPtsOicS6001gcqFwW1VAe1ahCVZdZtocTkIJwCRKYSluL1yNUXId4l7X6kUIiJNoms44yfTkSVVZ4FnzUNPgQWAA_Tnp3mqioFb4bfK7uO0cEGEG0PLrKLumSQF6X4vQWgzxpo8DKGMwXDLIqlHCO-2mfwghVRlStVEb_nqzEMg8TkT2LLqLcQSNpJ8XTStYo4Pj_dnr7NMgyMtZeRY98HTwQ0b3SuzI0lR8o3YmAkIy3Hx4SoxkOS6fZvp9dHPKUJvBZGncCEhq7Y7HKEyItw6_gHoY-deB5SJbqIeSDXpSzmoyj46AaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل یک تمرین نظامی غافلگیرکننده در امتداد مرز اردن انجام دادند که هدف آن آزمایش آمادگی برای تهدیدات ناگهانی امنیتی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/alonews/120206" target="_blank">📅 17:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120205">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyjhJiWR1suPzOM84fi8CYjSIrKtF7SJ_NqIymjep2p0jDyA7dSNJ3XXur4ee6Xk9mCk84Cxt9Zwaa70IP_FDTN0jJbJXU18pXBWHK4Mhk7UZaWTvYja7oIX7cBR8K3x1jIEEACM2Lnj-95QWJHYHk3Hl6jyndSAW98FpQtIQ-1XgHh_IGowE3nLyLYzkJMd4tg243PSBz1DGN7qZ2ngdJoz8KdmV1ViCbdUcnGPGJzF33V4BTN_ZJiYWGtAHVM4AlAVgiCAKb0gVkfIG33Nhtju6UsIndX9A7ouyHmQsJmGfDLgq-gd1NXCuaJ4NSnL8yxCKzMuUS-7YGlEr5XHBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدر اعظم آلمان: تماس خوبی با ترامپ داشتم!
🔴
ایران باید پای میز مذاکره بیاید و تنگه را باز کند، باید از دستیابی ایران به سلاح هسته‌ای جلوگیری شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/120205" target="_blank">📅 17:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120204">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رویترز: امارات هم مانند عربستان به دنبال احداث مسیر دور زدن تنگه هرمز است
🔴
امارات ساخت یک خط لوله نفت جدید را برای دو برابر کردن ظرفیت صادرات خود از طریق فجیره تسریع خواهد کرد تا توانایی‌اش را برای دور زدن تنگه هرمز به طور قابل توجهی گسترش دهد.
🔴
ولیعهد ابوظبی اعلام کرده که این خط لوله در حال ساخت است و انتظار می‌رود در سال ۲۰۲۷ عملیاتی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/120204" target="_blank">📅 17:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120203">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نیویورک تایمز: سفر ترامپ به چین در ظاهر دوستانه بود، اما پشت پرده تنش‌های شدیدی بین واشنگتن و پکن جریان داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/120203" target="_blank">📅 17:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120202">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: تا امروز، ۷۵ کشتی تجاری تغییر مسیر داده‌اند و ۴ کشتی غیرفعال شده‌اند تا اطمینان حاصل شود که قوانین رعایت می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/alonews/120202" target="_blank">📅 17:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd1a2c0e0.mp4?token=KUWORDbwYLIyiBQIlPehOnm7FJ6sRaVPeoc4sLvMpBMKcI8TDoIFhrYpCFmk5lkhxjVzbBELF3Rq7qt21Ob87HH7A6ySZwnhsfAZo7VuMLnU0E5KUI9UWSQJq1U1VDR-YWrKmSPIkTeDsN93TC5OOsUgWcupglHZybZCi14xnvi92fniECkK0gn4SEv86RkmPPo7YDN62eOky_S41WUPlzSNu9n0KtLEam8x4Rt5eamWJPsixiGixQ0t9JGRX4XwYhCWcuP8_hepJ6XlGchkaqrM3ckKscdQZKb_4xeQrtdANvpuaxpCe14u6hNlrcwWjp6SRvauQm5sxIRwGNcerA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd1a2c0e0.mp4?token=KUWORDbwYLIyiBQIlPehOnm7FJ6sRaVPeoc4sLvMpBMKcI8TDoIFhrYpCFmk5lkhxjVzbBELF3Rq7qt21Ob87HH7A6ySZwnhsfAZo7VuMLnU0E5KUI9UWSQJq1U1VDR-YWrKmSPIkTeDsN93TC5OOsUgWcupglHZybZCi14xnvi92fniECkK0gn4SEv86RkmPPo7YDN62eOky_S41WUPlzSNu9n0KtLEam8x4Rt5eamWJPsixiGixQ0t9JGRX4XwYhCWcuP8_hepJ6XlGchkaqrM3ckKscdQZKb_4xeQrtdANvpuaxpCe14u6hNlrcwWjp6SRvauQm5sxIRwGNcerA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل سه پهپاد شاهد-۱۳۶ ایرانی امروز اوایل روز به سایت‌های متعلق به گروه مخالف حزب دموکرات کردستان ایران در شمال اربیل در کردستان عراق حمله کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/120200" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: در صورت حصول توافق با ایران، آزادی دریانوردی می‌تواند با سرعت نسبی به تنگه هرمز بازگردد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/120199" target="_blank">📅 16:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c1130ab0.mp4?token=TWAy6rkGV9_TvpN11P-q_QPe8IPZ1_O9pemTF4ccFm_kpQBgbKXBLoPVyVCUUtj0yxFiQ7bFhN3Gnd4hFx995mmZaxiCoOw9hWyYRUJKngUtU3_bCypE0ZXCBKB5OvVy0ibAANYg3HlW7SMXSgemU29_uaWzbQNFwi5tY2jurGeaB3J_hNcNcennu1UgDRIhIIV0HObYNtDlzAgW9esv13lHj1lq0XCCyvYissZbzbAsuWxw97n5RuWIK0H-_YbH8A7qFI0Jl11YieVSNWusbTYWTH5xK1-L5MTR5mGT_bJQ4cIiN4D0NtoVkyO8rcuWJbf34tn3m67TnrHOQXZ12w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c1130ab0.mp4?token=TWAy6rkGV9_TvpN11P-q_QPe8IPZ1_O9pemTF4ccFm_kpQBgbKXBLoPVyVCUUtj0yxFiQ7bFhN3Gnd4hFx995mmZaxiCoOw9hWyYRUJKngUtU3_bCypE0ZXCBKB5OvVy0ibAANYg3HlW7SMXSgemU29_uaWzbQNFwi5tY2jurGeaB3J_hNcNcennu1UgDRIhIIV0HObYNtDlzAgW9esv13lHj1lq0XCCyvYissZbzbAsuWxw97n5RuWIK0H-_YbH8A7qFI0Jl11YieVSNWusbTYWTH5xK1-L5MTR5mGT_bJQ4cIiN4D0NtoVkyO8rcuWJbf34tn3m67TnrHOQXZ12w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بازید رئیس ستاد کل ارتش اسرائیل ایال‌ ضمیر از مرز "اردن"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/alonews/120198" target="_blank">📅 16:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
العربی الجدید: ایالات متحده شرایط سختی را بر نخست‌وزیر منتخب عراق، علی الزیدی، تحمیل می‌کند و خواستار خلع سلاح گروه‌های مسلح، انحلال شبه‌نظامیان مرتبط با ایران و پیگرد قانونی افراد دخیل در حملات به سفارت آمریکا است.
🔴
واشنگتن تهدید به تحریم کرده است اگر خواسته‌هایش برآورده نشود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/120197" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
الجزیره: هیئت‌های لبنان و اسرائیل به مقر وزارت امور خارجه آمریکا رسیدند
🔴
هیئت‌های لبنان و اسرائیل برای شرکت در دومین روز از مذاکرات بین خود، به مقر وزارت امور خارجه آمریکا رسیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/120196" target="_blank">📅 16:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزیر انرژی آمریکا، کریس رایت : تصمیم درباره تنگه هرمز تو دستِ ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/120195" target="_blank">📅 16:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120194">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
تصمیم ناگهانی وزیر جنگ، پیت هگستث، برای لغو استقرار برنامه‌ریزی‌شده ۴۰۰۰ سرباز آمریکایی در لهستان، مقامات پنتاگون و متحدان ناتو را غافلگیر کرد و باعث سردرگمی و مشورت‌های فوری بین مقامات آمریکایی و اروپایی شد، طبق گزارش POLITICO.
🔴
«ما هیچ اطلاعی از این تصمیم نداشتیم»، یک مقام آمریکایی گفت، در حالی که مقامات در هر دو سوی اقیانوس اطلس تلاش می‌کردند ارزیابی کنند آیا تغییرات نظامی غیرمنتظره دیگری ممکن است دنبال شود یا خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/120194" target="_blank">📅 16:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120193">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رویترز: قیمت نفت روز جمعه با افزایش رو‌به رو شد و شاخص‌های سهام در اروپا و ژاپن کاهش یافت.
🔴
تا ساعت 09:25 به وقت گرینویچ، قیمت نفت خام برنت با 3.47 دلار یا 3.3 درصد افزایش به 109.19 دلار در هر بشکه رسید
🔴
قیمت نفت خام وست تگزاس اینترمدیت آمریکا با 3.72 دلار یا 3.7 درصد افزایش به 104.89 دلار در هر بشکه رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/120193" target="_blank">📅 16:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120192">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیر قطع ارتباطات: بسته حمایتی برای کمک به شرکت‌های آسیب دیده از محدودیت اینترنت طراحی می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/120192" target="_blank">📅 16:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120191">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پیش از سوار شدن به ایرفورس وان که از پکن حرکت می‌کرد، کل هیئت آمریکایی تمام اقلام دریافت شده از میزبانان چینی، از جمله هدایا و اقلام یادبود را دور انداختند و هیچ کالای ساخت چین اجازه ورود به هواپیما را نداشت.
🔴
مقامات از آوردن دستگاه‌های شخصی در سفر خودداری کردند و در عوض در طول بازدید از تلفن‌های پاک استفاده کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/120191" target="_blank">📅 16:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120190">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
امارات و هند یه توافق بستن برای تأمین گاز مایع (LPG)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/120190" target="_blank">📅 16:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120189">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27af438ce.mp4?token=ZArB_ZyH9CYGuqC5a8VG94ecQWo5J_5G5ZA6auv7v9zqfzfiSHTUAXNAsoDectYfZWEwF0VpTxgXK6Idg-NXsAYeFf683LInhZBGWqlb6U6QMPLgTzmpUzdW3YWevkSAhkM5dSfM5nlSxvKqVhvQFjfIEFKImD8bt4dwYy_f1cXEFucaN9o1q5axHRvJdI4jN0Ucobd6vHMR2GJX0dSxoY5I5m7-FnXSBcDgU6FFpRMcCYX7RR_keCctXC-0l435AuGArg27kUMWyj0OEdKiFzuYnDGl2CwMDMSDnRLcLQTQVCaz3w1oT0AaWR5XBR4z-3N_7_EN3IREY9LUXbY5lIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27af438ce.mp4?token=ZArB_ZyH9CYGuqC5a8VG94ecQWo5J_5G5ZA6auv7v9zqfzfiSHTUAXNAsoDectYfZWEwF0VpTxgXK6Idg-NXsAYeFf683LInhZBGWqlb6U6QMPLgTzmpUzdW3YWevkSAhkM5dSfM5nlSxvKqVhvQFjfIEFKImD8bt4dwYy_f1cXEFucaN9o1q5axHRvJdI4jN0Ucobd6vHMR2GJX0dSxoY5I5m7-FnXSBcDgU6FFpRMcCYX7RR_keCctXC-0l435AuGArg27kUMWyj0OEdKiFzuYnDGl2CwMDMSDnRLcLQTQVCaz3w1oT0AaWR5XBR4z-3N_7_EN3IREY9LUXbY5lIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اطمینان‌های سال ۱۹۸۲ که رئیس‌جمهور ریگان داده بود، می‌گفت ایالات متحده در مورد فروش تسلیحات به تایوان با چین مشورت نخواهد کرد.
🔴
ترامپ: فکر می‌کنم سال ۱۹۸۲ خیلی دور است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/120189" target="_blank">📅 16:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120188">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406bb1d113.mp4?token=tKc1QKCwLqe_-_ZY0hfLI6hhkRD0nx4wYr_h6qAyvSU_mZ0MpYFS79vXJp0cjfmgOfXSV6EJ_-1vp0QN3fAGBSE2OjqonG4Jwt6RpoEinOTuOTG3iaUaYA_R-nuywPQ7yXcPR2nvE4Zu_LgV4Paoz3Is5ljIVO59aAdzjZ_x0QtiEBcau9KcfF0hB1y7ENz0m_wCromvUpphRjdyTXlKDeU_nrwWKZRz8zrtWOcLajOK7m0hvFC8-cJerVRheMDphbXxkmlZUyAfvwKPvoKb_wdZXwKRZHUKxSMM1DR_tYE2--NV55pLehcCmO5-T2hlPyeC6hceyEFm_aRWf59Sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406bb1d113.mp4?token=tKc1QKCwLqe_-_ZY0hfLI6hhkRD0nx4wYr_h6qAyvSU_mZ0MpYFS79vXJp0cjfmgOfXSV6EJ_-1vp0QN3fAGBSE2OjqonG4Jwt6RpoEinOTuOTG3iaUaYA_R-nuywPQ7yXcPR2nvE4Zu_LgV4Paoz3Is5ljIVO59aAdzjZ_x0QtiEBcau9KcfF0hB1y7ENz0m_wCromvUpphRjdyTXlKDeU_nrwWKZRz8zrtWOcLajOK7m0hvFC8-cJerVRheMDphbXxkmlZUyAfvwKPvoKb_wdZXwKRZHUKxSMM1DR_tYE2--NV55pLehcCmO5-T2hlPyeC6hceyEFm_aRWf59Sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کوبا: آنها به کمک نیاز دارند. آنها واقعاً یک ملت — یا یک کشور — در حال افول هستند.
🔴
ما چیزهای زیادی برای صحبت درباره کوبا داریم، اما شاید امروز نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120188" target="_blank">📅 15:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120187">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fabdb1f687.mp4?token=XU5KsGeyIvunAE-2ckK4CuXW6CvP7I3yG3v8etwJfAwSsfJdzjD_YKqGOd0I0si4Z3xy5T7wWSXMQgihevRsIiYF2sjrN4F2avJI_APiCDU_RRXtc3bXzNT_5CHFyXsCwPidtlnCeDxIc6crc_lTua28A1D0a8fRGW3fUBRW5zOPU4oYt2V_uEDakPX4mJmnet5WlXihr0zmW8n_LVQf_lQdgcUMr7Ap22hrSVG0VndaeGiv0xROl61PPJRVFFykHM5tpJShHRpmV3MRTMpLF22w7y9A1tFa4bEW2BDwBEBnvGcd4ciaacN7A-G_kwnVKuK2sfGvlAaCFELuj9w-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fabdb1f687.mp4?token=XU5KsGeyIvunAE-2ckK4CuXW6CvP7I3yG3v8etwJfAwSsfJdzjD_YKqGOd0I0si4Z3xy5T7wWSXMQgihevRsIiYF2sjrN4F2avJI_APiCDU_RRXtc3bXzNT_5CHFyXsCwPidtlnCeDxIc6crc_lTua28A1D0a8fRGW3fUBRW5zOPU4oYt2V_uEDakPX4mJmnet5WlXihr0zmW8n_LVQf_lQdgcUMr7Ap22hrSVG0VndaeGiv0xROl61PPJRVFFykHM5tpJShHRpmV3MRTMpLF22w7y9A1tFa4bEW2BDwBEBnvGcd4ciaacN7A-G_kwnVKuK2sfGvlAaCFELuj9w-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا اصلاً درباره اوکراین با شی صحبت کردید؟ و آیا در این زمینه پیشرفتی حاصل شده است؟
🔴
ترامپ: بله، صحبت کردیم — خب، این موضوعی است که دوست داریم حل شود. تا دیشب اوضاع خوب به نظر می‌رسید، اما آنها دیشب ضربه بزرگی خوردند.
🔴
پس این اتفاق خواهد افتاد، اما حیف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120187" target="_blank">📅 15:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120186">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4205c201.mp4?token=qXglAhO6e4RGCsiQ2DUAWIETAO_psBhYQCb8paaO-JF5esYSsxFGTlnTtbGqBTGu7X1HkE0v_qvIZhgaeOVKL4YZvMw2sPMUNiML-HY5B9XvXB-gtgxVpliJQ5Z_NUmDvjRIxt7cES0W5FT8PlN2QzqTnqFEfgqEdl9GbZFN_J97De5Lr48euI-ntvXcrpEWRJ6Nv9XUY5AP4N6iaZTC3pU-XdwvcqGFOwrZ1oksr8MXnQEHFNsqm4K_uzbUeB_CtDZiiF2-XNLOzDepoqyaY65GOahicuI6y4kQyHHdnMIEXiHJZ53ZPntGTs4Tk2OnJzeN-Qg8wYfww8zdN2C2EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4205c201.mp4?token=qXglAhO6e4RGCsiQ2DUAWIETAO_psBhYQCb8paaO-JF5esYSsxFGTlnTtbGqBTGu7X1HkE0v_qvIZhgaeOVKL4YZvMw2sPMUNiML-HY5B9XvXB-gtgxVpliJQ5Z_NUmDvjRIxt7cES0W5FT8PlN2QzqTnqFEfgqEdl9GbZFN_J97De5Lr48euI-ntvXcrpEWRJ6Nv9XUY5AP4N6iaZTC3pU-XdwvcqGFOwrZ1oksr8MXnQEHFNsqm4K_uzbUeB_CtDZiiF2-XNLOzDepoqyaY65GOahicuI6y4kQyHHdnMIEXiHJZ53ZPntGTs4Tk2OnJzeN-Qg8wYfww8zdN2C2EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: دیروز از دریاسالار کوپر درباره حمله به مدرسه دخترانه در اولین روز جنگ سوال شد.
🔴
ترامپ: شما درباره مورد اصلی صحبت می‌کنید — که در حال بررسی است.
🔴
خبرنگار: آیا می‌توانید تایید کنید که این موشک آمریکایی بود؟
🔴
ترامپ: شما با چه کسی هستید؟
🔴
خبرنگار: بی‌بی‌سی.
🔴
ترامپ: بی‌بی‌سی جعلی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/120186" target="_blank">📅 15:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120185">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
عراقچی: اگه به جنگ برگردن این تصمیم خودشونه، ولی نتیجه فرقی نمیکنه و بازم شکست میخورن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/120185" target="_blank">📅 15:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120184">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ رسماً اعلام کرد که یه دور دیگر از عملیات نظامی آمریکا در ایران در راه است:
ما از نظر نظامی در ایران تقریباً کار را تمام کردیم. حدود ۷۵٪ کار را. (البته) ما همه چیز را تمام نکردیم. برمی‌گردیم و آن را تکمیل می‌کنیم. حتی شاید بیشتر!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120184" target="_blank">📅 15:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120183">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
مرتس و ترامپ درباره ایران، هرمز و اوکراین رایزنی کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120183" target="_blank">📅 15:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120182">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ درباره استعفای استارمر: من چنین چیزی نمیگویم
🔴
خبرنگاری از دونالد ترامپ پرسید آیا کی‌یر استارمر، نخست وزیر بریتانیا، باید استعفا دهد؟
🔴
ترامپ پاسخ داد: «من این را نمیگویم. در واقع فکر میکنم او مرد خوبی است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120182" target="_blank">📅 15:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120181">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرنگار : خب آمریکا که شانسی نداشت. این همه بمبارون رو چرا تکرار می‌کنید؟ ۳۸ روز زدید، آخرشم تغییر سیاسی تو ایران اتفاق نیفتاد
🔴
ترامپ : نه، اتفاقاً ما یه پیروزی کامل نظامی داشتیم
🔴
مشکل اینه که سیاسی‌بازایی مثل تو حقیقتو نمی‌نویسن
🔴
ما کل نیروی دریایی‌شونو زدیم، نیروی هواییشونو نابود کردیم، پدافندشونو خوابوندیم، راداراشونو ترکوندیم
🔴
همه فرمانده‌های رده اولشونو زدیم، بعد رده دوم و حتی کلی از رده سومی‌ها رو هم زدیم. الان کاملاً گیج و به‌هم‌ریخته‌ان
🔴
این یه پیروزی کامل بود، جز توی رسانه‌هایی مثل نیویورک تایمز و CNN که حقیقتو نمی‌گن
🔴
حتی به نظرم چیزی که می‌نویسید یه جور خیانته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/120181" target="_blank">📅 15:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120180">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d23a0132.mp4?token=sQ-R5RFck_qiDDlI35awnNpfsZ_9abzEhZNTh3a5UHhO8lQpCICAPHcHrE2G8S9Ko8URqguGXO2Beu943GmB8cgtkZZFimCxfLmFE2cw1MOg56LmXq6YI1ZNyLvWQZmGBWx5wjixZyzanbhDcOZ3dcTw2dutIz7-X5TkR2W2kErUleVkWRdmDsA3Pr3cmCWK40E1Fcpl5Ay4VwJSTEENRbDk8g_-8HBnT4FTlXiOC0yErT7lKfLnXUOYxenRpNNiEJDXkLyeccjdcn4G8tVasqcIQAnBXS-bGkdJ1Iit5olD9j8k4yb6cPI1VcXjuHYl4bIN5dTYabOcoACJ49Y0RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d23a0132.mp4?token=sQ-R5RFck_qiDDlI35awnNpfsZ_9abzEhZNTh3a5UHhO8lQpCICAPHcHrE2G8S9Ko8URqguGXO2Beu943GmB8cgtkZZFimCxfLmFE2cw1MOg56LmXq6YI1ZNyLvWQZmGBWx5wjixZyzanbhDcOZ3dcTw2dutIz7-X5TkR2W2kErUleVkWRdmDsA3Pr3cmCWK40E1Fcpl5Ay4VwJSTEENRbDk8g_-8HBnT4FTlXiOC0yErT7lKfLnXUOYxenRpNNiEJDXkLyeccjdcn4G8tVasqcIQAnBXS-bGkdJ1Iit5olD9j8k4yb6cPI1VcXjuHYl4bIN5dTYabOcoACJ49Y0RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : در مورد ایران، دقیقاً قدم بعدی چیه؟ دوباره می‌خواید با تهدید بمبارون فشار بیارید؟ چقدر واقعیه؟
🔴
ترامپ : نمی‌خوام بگم فلان ساعت و فلان روز بمبارون دوباره شروع میشه
🔴
فقط اینو با اطمینان خیلی زیاد میگم
🔴
ایران هیچ‌وقت به اون چیزی که می‌خواست نمی‌رسه و قرار هم نبود برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120180" target="_blank">📅 15:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120179">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مذاکرات بریکس بدون بیانیه مشترک پایان یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120179" target="_blank">📅 15:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120178">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
آسوشیتدپرس گزارش داد دور سوم مذاکرات لبنان و اسرائیل امروز در واشنگتن آغاز شده تا دو طرف درباره آتش بس تازه، کاهش درگیری‌ها و مسائل امنیتی جنوب لبنان گفت وگو کنند.
🔴
لبنان خواستار عقب نشینی نیروهای اسرائیلی از جنوب این کشور است، اما اسرائیل بحث خلع سلاح حزب الله را جلو کشیده. همین موضوع گره اصلی مذاکرات است، چون حزب الله پشت میز حضور ندارد، اما بخش مهمی از پرونده امنیتی لبنان به آن گره خورده است.
🔴
این مذاکرات برای تهران هم پیام دارد. هر فشار تازه روی حزب الله، یکی از مهم‌ترین بازوهای منطقه‌ای جمهوری اسلامی را محدودتر میکند، آن هم بدون اینکه تهران مستقیما در اتاق مذاکره باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/120178" target="_blank">📅 15:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120177">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6bdaf1c06.mp4?token=ZtISXqzmeIKd7UzB-F8P2_2_wRKPDzSTekfkg-b4U7BsnRWZw1MvRLOewGnOg8gu67GyJ0-EjHt-rorK3HOZztcV9V8sFtodLXgsMnsDZJ8s7zKk78xbUgnokVCz2KdadtwKI4mm8Obh7WZj1PN2WCWZvpn5wSv6HqOeF1gEK3cjwnWi8snuC5fsI1yk4IhcFZC4bk0tQ_b-F3-sMgePo6_X7CTcXk8N-U4tCknW8Rm2OSHFZafV-tn6HIm42cvcKJcYG8nmyiK0FF9qsuTl429NnqoWakgQk9Rbc08MOoUzM1p8V10lINyrcuydxQvZqIS4izcsRwcozS6xto37sFDLpeefxPpwORCLgfsOr_Y-P-vyxrqlO0NNx9IDsuDqDXYyxtWgvAq0JsU_m1WUP983_o4iu6NTrPZaYYztRpG5Bi8Jzd2tMOLUPVB5AjxNF8GH8W2n6ebaVppQl1bg6Eu8IP6HH1U2eFj132Lpm2I8lNF_z-bC8kZ-iF7XP8movcwh7u__AgLsjQZDw0Nlno_r3bz7ie8mFbhb0xTx8MfYcI5e1UMHLnmSChKAG2yYdy7scPM62e3mRzIqu_jITB7j1HLH1V2M1iQO1AFJntbXL5XVXiYdFCcWD6nlh9lD1wqX_brB1axbO4Q9E_ENtmVCbqi5StDlKjCdbEvIqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6bdaf1c06.mp4?token=ZtISXqzmeIKd7UzB-F8P2_2_wRKPDzSTekfkg-b4U7BsnRWZw1MvRLOewGnOg8gu67GyJ0-EjHt-rorK3HOZztcV9V8sFtodLXgsMnsDZJ8s7zKk78xbUgnokVCz2KdadtwKI4mm8Obh7WZj1PN2WCWZvpn5wSv6HqOeF1gEK3cjwnWi8snuC5fsI1yk4IhcFZC4bk0tQ_b-F3-sMgePo6_X7CTcXk8N-U4tCknW8Rm2OSHFZafV-tn6HIm42cvcKJcYG8nmyiK0FF9qsuTl429NnqoWakgQk9Rbc08MOoUzM1p8V10lINyrcuydxQvZqIS4izcsRwcozS6xto37sFDLpeefxPpwORCLgfsOr_Y-P-vyxrqlO0NNx9IDsuDqDXYyxtWgvAq0JsU_m1WUP983_o4iu6NTrPZaYYztRpG5Bi8Jzd2tMOLUPVB5AjxNF8GH8W2n6ebaVppQl1bg6Eu8IP6HH1U2eFj132Lpm2I8lNF_z-bC8kZ-iF7XP8movcwh7u__AgLsjQZDw0Nlno_r3bz7ie8mFbhb0xTx8MfYcI5e1UMHLnmSChKAG2yYdy7scPM62e3mRzIqu_jITB7j1HLH1V2M1iQO1AFJntbXL5XVXiYdFCcWD6nlh9lD1wqX_brB1axbO4Q9E_ENtmVCbqi5StDlKjCdbEvIqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره دیکتاتور بودن شی: این را شما باید تشخیص دهید
🔴
خبرنگاری از دونالد ترامپ پرسید آیا شی جین پینگ را دیکتاتور میداند یا نه.
🔴
ترامپ پاسخ داد: «او حاکم چین است، رئیس جمهور چین است. من به این موضوع فکر نمیکنم. شما با چیزی که وجود دارد طرف میشوید. من به او احترام میگذارم، خیلی باهوش است و کشورش را دوست دارد.»
🔴
ترامپ در ادامه گفت: «اینکه او دیکتاتور هست یا نه، چیزی است که شما باید تشخیص دهید.»
🔴
ترامپ در برابر چین، انتقاد حقوق بشری را عقب میگذارد و بیشتر روی معامله، رابطه شخصی و مدیریت قدرت تمرکز میکند. برای پکن، همین ادبیات یعنی واشنگتن فعلا دنبال درگیری لفظی تازه نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/120177" target="_blank">📅 15:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120176">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
فروش کانفیگ متصل پایدار با ساب و مورد تایید مجموعه الونیوز
⬇️
🔔
@FastProxyMakerBot
🔔
@FastProxyMakerBot
✔️
با خیال راحت و بدون دغدغه خرید کنید</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/120176" target="_blank">📅 15:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120175">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عراقچی: این جنگ، جایگاه و اقتدار ایران رو در دنیا ارتقا داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120175" target="_blank">📅 15:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120174">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxZoSi8OMass7_iPc4w7IJ7555TLyW2WwrdPjMf54I_En2FSc_u367FIPVwQWthXO40_GL3b0TphgZrsw_ytFNPWG51IA8fHCJXkmMmMIFh148v2HLNZZdz64z8uZZWlPPy8DD8xmk0UwoyGHpFpAdsG_Ygdiu8_SvtpnadThzXIAm57siLEj7xZmPJW5_32OdIrFBWW6X6ie7rQ-fKaWuFxFUZqs5_YAlih0PqIEJANOXxwIQuQXlnd72ebRR1TAxJkShKn77RjcPep6YGJSMbUU32XLLK19wezAUtuiftbCskYQN-rSzLum_16e_t5UMJ4nf2kewx0Eb54fpkK8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ: درخواستی برای باز شدن تنگه هرمز از رئیس جمهور چین نداشتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/120174" target="_blank">📅 14:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120173">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
عراقچی: موضوع مواد غنی‌شده ما مسئله‌ای بسیار پیچیده است و اکنون با آمریکایی‌ها به این نتیجه رسیده‌ایم که چون در این مورد خاص تقریباً به بن‌بست رسیده‌ایم، بهتر است بررسی آن را به مراحل بعدی مذاکرات موکول کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/120173" target="_blank">📅 14:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120172">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ به خبرنگار نیویورک تایمز:
پوشش نیویورک تایمز برای جنگ ایران نشان دهنده خیانت بزرگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120172" target="_blank">📅 14:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120171">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👸
سفر رسمی علیاحضرت شهبانو فرح پهلوی، به چین سال ۱۳۵۱ انجام شده است.
🤔
آن زمان، چین فقیر بود و ایران ثروتمند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120171" target="_blank">📅 14:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120170">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om7izPOkHHIZ73MHeqSLt6mKnPiRSzOsjTAlV7thDL1KIlObGJG4tk8oatOpgxWkqoyXNTYFpaVGPfw7ue-eIsgpLfa745Sozlv6zssMrO2R4A_R4UNBxRtEGhBiEw_XjxYAROP5QX44MMetq61ZYbaJlJyVWSo3lWqG35BhUONd-IIqxtNWzCYh-k5rZlDgZzEFCtkK0NLc6y8E6fL8lXbbaMDNKfZaruuYqU761zD3uMHDeWz-24d65WjVCLIwaxfWiDFXS1_KeVglZ1QO0j2BT5PxEWnuIv3oXF5YFA4DZROgDWtd2ezIf2hBNNEAUD7DnGyhfM36piCkFUCo-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل دستور تخلیه به ساکنان: عین بعال، الخریب، الزراریه، عرب سلیم و عرب الجل (صیدا) در جنوب لبنان صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120170" target="_blank">📅 14:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120169">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: اگر 9 ماه پیش از بمب‌ افکن‌های  B-2 استفاده نمی‌کردم، ایران اکنون می‌توانست به سلاح هسته‌ای دست یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/120169" target="_blank">📅 14:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120168">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: به رئیس جمهور چین گفتم در مورد پرونده تایوان صحبت نمی کنم
🔴
چینی ها عملیات جاسوسی انجام می دهند و ما نیز عملیات جاسوسی انجام می دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120168" target="_blank">📅 14:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120167">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: میتوانیم نیروگاه‌های ایران را تنها در دو روز از بین ببریم
🔴
اگر ایران اورانیوم های غنی شده خودش رو تحویل نده وارد ایران میشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120167" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120166">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: ما ارتش ایران را نابود کرده‌ایم و شاید باید یک پاکسازی سبک انجام دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120166" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120165">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: وقتی به پیشنهاد ایران نگاه کردم، جمله اول را دوست نداشتم و قابل قبول نبود، بنابراین پیشنهاد را رد کردم
🔴
تحقیقات درباره هدف قرار دادن مدرسه در ایران در حال انجام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/120165" target="_blank">📅 14:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120164">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: من به جایی رفتم که شی زندگی می کند، چیزی که به ندرت اتفاق می افتد.
🔴
خبرنگار: اونجا بودی؟
🔴
ترامپ: آره قشنگ بود.منظورم این است که مردم هرگز آن را ندیده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/120164" target="_blank">📅 14:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120163">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/701ad40f12.mp4?token=AIiCMkNG3p-NVq721ZXGEnZukLa2P1MfHPGfVXVZYVTHFp_rYtIey-KZoZGh6OKnL99_YyiKdESDLlRSiodpy5iOwjXU4b-lAPuWBmgfqT25qR_xHPRc8O38Pq9jjDvGfAULNJ-B3JBFbKgD4bXpfoGoMtS-OGEottsp9U_4IUkFn9TxK_Dio9BFTzEYw8VcqHmT6-qnPcafCzrALr2Wa14R_u2lNGlyRnR5A7ESrBpXcA3TuClDBgw5zJW_KSIXrnNN53CsuHZpk2B4ithUMjKviV2vLt4kSN-uTaWmOZYEXO1XBOpQ3DLcrwTIgKmhSXg41CH9iswhTPBXmQynTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/701ad40f12.mp4?token=AIiCMkNG3p-NVq721ZXGEnZukLa2P1MfHPGfVXVZYVTHFp_rYtIey-KZoZGh6OKnL99_YyiKdESDLlRSiodpy5iOwjXU4b-lAPuWBmgfqT25qR_xHPRc8O38Pq9jjDvGfAULNJ-B3JBFbKgD4bXpfoGoMtS-OGEottsp9U_4IUkFn9TxK_Dio9BFTzEYw8VcqHmT6-qnPcafCzrALr2Wa14R_u2lNGlyRnR5A7ESrBpXcA3TuClDBgw5zJW_KSIXrnNN53CsuHZpk2B4ithUMjKviV2vLt4kSN-uTaWmOZYEXO1XBOpQ3DLcrwTIgKmhSXg41CH9iswhTPBXmQynTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: رابطه بسیار خوبی با کیم جونگ اون دارم
🔴
دونالد ترامپ گفت با کیم جونگ اون، رهبر کره شمالی، «رابطه بسیار خوبی» دارد و او تا امروز نسبت به آمریکا محترمانه رفتار کرده است.
🔴
ترامپ اضافه کرد که میخواهد این احترام ادامه داشته باشد. این اظهارات در حالی مطرح میشود که پرونده کره شمالی دوباره به یکی از آزمون‌های مهم سیاست خارجی واشنگتن تبدیل شده، جایی که ترامپ مثل همیشه روی رابطه شخصی با رهبران سختگیر حساب باز میکند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120163" target="_blank">📅 14:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120162">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: 80 درصد از توان موشکی ایران نابود شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/120162" target="_blank">📅 14:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120161">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ : «مواد هسته‌ای» ایران، ممکنه به چین یا آمریکا تحویل داده شه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/120161" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120160">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: «من دیگر خیلی بیشتر از این صبر نخواهم کرد. آنها باید توافق را امضا کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/120160" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120159">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عراقچی: پس از اینکه ترامپ آخرین پیشنهاد ما را رد کرد، پیام‌هایی از آمریکا دریافت کردیم که تمایلش به ادامه گفت‌وگو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/120159" target="_blank">📅 14:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120158">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: پل‌ها و سایت‌های برق ایران که می‌توانیم هدف قرار دهیم
🔴
ترامپ می‌گوید ایران آتش‌بس را به عنوان لطفی به دیگر کشورها انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/120158" target="_blank">📅 14:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120157">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: هیچ تعهدی در مورد تایوان ندادم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120157" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120156">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: پل‌ها و سایت‌های برق ایران که می‌توانیم هدف قرار دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120156" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120155">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ درباره ایران: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/120155" target="_blank">📅 14:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120154">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17259012d.mp4?token=BtvIpVphcAO09IFn5hJImpiCEyKTy3zoBlFUIZQtOgsqr5kUFwJPa43JC14dxVO9aI96oH3qRtOBS-RRZNeGVOGzTlyXlgHgiKf3ZPk0vSuQrfE6QDlACjEzS6snixxVOFeSe5w4tIIxdUalANh0TelY66lyqM0yqYqmRRngSatxvoYQdoOR0jLkQeMuqTTuPifEgdnQXYWYzPcTqg0VE8DDyo0E6YF4Qd95Pn5DvPjif7YKHa5plvIjEAoYOZw4IFuRbqPjzAXeS05M2BNHVA7OIm84diQdebjc51fzNgZgsL8jUtx71B_Pi1CUFzs1uQcH2cuQmD3wGtT2vutmMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17259012d.mp4?token=BtvIpVphcAO09IFn5hJImpiCEyKTy3zoBlFUIZQtOgsqr5kUFwJPa43JC14dxVO9aI96oH3qRtOBS-RRZNeGVOGzTlyXlgHgiKf3ZPk0vSuQrfE6QDlACjEzS6snixxVOFeSe5w4tIIxdUalANh0TelY66lyqM0yqYqmRRngSatxvoYQdoOR0jLkQeMuqTTuPifEgdnQXYWYzPcTqg0VE8DDyo0E6YF4Qd95Pn5DvPjif7YKHa5plvIjEAoYOZw4IFuRbqPjzAXeS05M2BNHVA7OIm84diQdebjc51fzNgZgsL8jUtx71B_Pi1CUFzs1uQcH2cuQmD3wGtT2vutmMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
یکی از صدها موشکی که برگشتن رو سر مردم و جمهوری اسلامی طبق روال همیشه با مظلوم نمایی انداختن گردن امریکا و اسرائیل
🤔
مدرسه میناب جای تحقیق و بررسی زیادی داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120154" target="_blank">📅 14:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120153">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ پس از پایان سفر خود به چین، درباره تایوان به فاکس نیوز گفت: ما به دنبال جنگیدن نیستیم
🔴
ترامپ به خبرنگاران گفت: فکر نمی کنم با چین بر سر تایوان اختلاف نظر وجود داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/120153" target="_blank">📅 14:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120152">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ممکن است با تامین سلاح برای تایوان موافقت کنم و ممکن است موافقت نکنم
🔴
هنوز تصمیمی برای تامین سلاح برای تایوان نگرفته‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/120152" target="_blank">📅 14:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120151">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پیام کتبی سید مجتبی خامنه ای ، به مناسبت بزرگداشت فردوسی: فارسی فقط ابزار حرف زدن نیست؛ بخشی از هویت و اقتدار تمدن ایرانیه.
🔴
مردم ایران تو جنگ اخیر مثل قهرمان‌های شاهنامه ایستادن و مقابل متجاوزها مقاومت کردن.
🔴
اهالی هنر و رسانه باید این حماسه و مقاومت مردم رو برای تاریخ ماندگار کنن.
🔴
باید مقابل تهاجم فرهنگی و سبک زندگی آمریکایی ایستاد و روی پدافند زبانی و فرهنگی بیشتر کار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120151" target="_blank">📅 14:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120150">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عراقچی : تنگه خیلی هم گشاده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/120150" target="_blank">📅 14:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120149">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
عراقچی:  امیدوارم کشورهای حاشیه خلیج فارس متوجه شوند که آمریکا و اسرائیل نمی‌توانند برای آنها امنیت بیاورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120149" target="_blank">📅 14:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120148">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e412eeab0.mp4?token=se2OJ6V4uhiOYOA0jM-UEYOF296GDVFo31nKOdlQXwEKfodGX5GhceuK4QMvKS-ik-nUK2qnXQ9tTO_lZEYXdhbPu0jHwbRfU5AlSF-qWLADlOWg8cBvRwSikAYsWo_5lMY5k5jDa1dpcP17N7o2WGl0jhgM1ohz0aUuZyfKC83NjPpPmyAY7Qvp8e6J9i-nEZWOQu1mHCzi_8Xfm3LyOGhOMmb-A2XitDc6UPTBzuYuILQFVmiYWvsxAQdfCgBISMQ70FTcVgqIPJqrf-H7qXUh2fbHFYkQtLmK7Tl9hHD6IeRZTarYIAMK84ANQ6wbNTD44BO5wRUHUawYADodDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e412eeab0.mp4?token=se2OJ6V4uhiOYOA0jM-UEYOF296GDVFo31nKOdlQXwEKfodGX5GhceuK4QMvKS-ik-nUK2qnXQ9tTO_lZEYXdhbPu0jHwbRfU5AlSF-qWLADlOWg8cBvRwSikAYsWo_5lMY5k5jDa1dpcP17N7o2WGl0jhgM1ohz0aUuZyfKC83NjPpPmyAY7Qvp8e6J9i-nEZWOQu1mHCzi_8Xfm3LyOGhOMmb-A2XitDc6UPTBzuYuILQFVmiYWvsxAQdfCgBISMQ70FTcVgqIPJqrf-H7qXUh2fbHFYkQtLmK7Tl9hHD6IeRZTarYIAMK84ANQ6wbNTD44BO5wRUHUawYADodDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نفت به آغوش مناطق ساحلی و جزایر ما رسیده و اینطور در حال نابودکردن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/120148" target="_blank">📅 14:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120147">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oMOOOUnCLj0LfTmoT4M3CIDHaR_IW2Zeqdqszq8Yx0_U-Giov-zUb1LQmWVjm-G3qZJ50UWKs7NvgX1BVLJOvexunUlkQyTJK4Y5UhXuAb02uxcDWWW291ADiaTWwcJqtwWy7Wmu4uQozGydIwFk1RMpw_liuU7YZXT1cIky6y6thcS1uhEXe9w1HzHh0IE9ZcDrgiUjKjIFp82G7yIkCMv2_oSuS5gz2v0slJjzDH1etbmtBTnV-zvCaC1WytVOvuy4xc7hy4_UhiqYwj6-s0bGHxXNbsuTxqmIOlRIAkDCrLbyF_O0LAWU1-4Yncbnn4bkmKgVcwYEFVeH7dVr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی، شهردار تهران: ما قصد داشتیم قبل از جنگ بیت رهبری رو با معماری جدید بازسازی کنیم، اما آمریکا عملیات تخریب رو که بسیار هزینه‌بر هم بود برای ما رایگان انجام داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120147" target="_blank">📅 14:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120146">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XYUixGn2AtJ1qbio33U2_tndXVrwj0r8gDHZwUBDdaVDFdU0rBjVZTSdAyUDwcIA-nyfDHF782Zg5conxEi_c1IJhzPsnlvX9jAlixYyQBaT_TOE0av4yEvisjNivJYatMYNBEHuj52dY1_1vrS8Kyx2s4xEYuGG3ulz1nio2liLJmnSyI7vmw_Ggv-7VlDo7um8YTPDW9nw8XJCXJ-TGtJE9HbmLAhz_Pa010QK3x29bN41U9Sk-7RwwpaGc3cVHVltxEhTL3u6UJ4wGKsMwcjzFoUKOfhBPVMfr30HwVUynZlA5c4SPKC62-uSu3jCZL1n92tJTffvzjnWzl3EwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
اینترنت رایگان و آزاد برای همه مردم
⚡
VPN رایگان
⚡
کانفیگ تست‌شده و پرسرعت
⚡
آپدیت روزانه
⚡
بدون قطعی و دردسر
@NetaazaadVPN
@NetaazaadVPN
اینجا فقط وصل میشی و راحت استفاده میکنی
🫡
👇
@NetaazaadVPN
@NetaazaadVPN
@NetaazaadVPN</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/120146" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120145">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
عراقچی: میانجیگری پاکستان شکست نخورده، اما با مشکلاتی مواجه است
🔴
از هرگونه تلاش چین، هند و روسیه برای حل بحران استقبال می‌کنیم
🔴
عراقچی درباره خروج اورانیوم از ایران به روسیه: مذاکره خوبی با لاوروف داشتم. مشارکت راهبردی با روسیه داریم. با پوتین در روسیه دیدار کردم و در خصوص اورانیوم هم صحبت کردیم، از پیشنهاد طرف روسی متشکریم، این موضوعی بود که باید در حین مذاکرات به نتیجه برسیم.
🔴
موضوع غنی سازی پیچیده است و برای رسیدن به نتیجه با طرف آمریکایی پیشنهاد دادیم این بحث به تعویق بیفتد.
🔴
در حال حاضر این موضوع مورد بحث نیست.
🔴
نسبت به جدیت آمریکایی‌ها شک داریم. آماده توافق منصفانه و عادلانه هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/120145" target="_blank">📅 14:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120144">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر امورخارجه: اگر از سوی آمریکایی‌ها جدیتی احساس کنیم، مذاکرات را از سر خواهیم گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/120144" target="_blank">📅 13:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120143">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
جعفر قادری، نایب رئیس دوم کمیسیون اقتصادی مجلس: اینترنت بین‌الملل مهم است اما از همه چیز مهم‌تر امنیت ملی است
🔴
فعال اقتصادی که برای او منفعت و درآمد دارد قطعا برای ادامه کار خود هزینه اینترنت پرو را پرداخت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/120143" target="_blank">📅 13:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120142">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
عراقچی: ایران هرگز تلاشی برای دستیابی به سلاح هسته‌ای نکرده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120142" target="_blank">📅 13:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120141">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
عراقچی: ایران هرگز تلاشی برای دستیابی به سلاح هسته‌ای نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/120141" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120140">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tzl4d5z2yQg3Q4MS1H1KY3YvaZFv3F54Nyrq-oh1c2QxkeBlICoRzOazv3jeu0wevJ9E1IqYao62Re-K5ZDY31OIHVFZaEi371nHgAOxGKkLR35xjeJPG0Lw9m59nLrSuKrOhGJXyT5xkHMDKsZ94BD86spfR8gl-aQQSIWNxAkU-T-0YR0NVGmjs5HC54seN2k6X9tUecY1CyED5ovTa0zw-q8U2RfQblslvQ8mrMbyPrM0E2T003V-7yuc_yQ1Wn3PqGm--QBXzCRLFbUKP00jWNkOW9c-Rsq2sCLIqeOPzVbu1Azo7l7omrO28ZJdfp51z3JaogFvT2zhy7m98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت برنت به ۱۰۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/120140" target="_blank">📅 13:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120139">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
عراقچی: ما در وضعیت آتش بس هستیم اگرچه متزلزل است، اما
تلاش می‌کنیم به دیپلماسی شانس دیگری دهیم
🔴
در برابر حملات تجاوزکارانه و تحریم مقاومت می‌کنیم
🔴
توافق ۲۰۱۵ یک دستاورد بود، اما ترامپ بدون دلیل از آن خارج شد
🔴
آمریکایی‌ها خیلی زیاد نظرشان را عوض می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120139" target="_blank">📅 13:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120138">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571bfcee62.mp4?token=SMxpUg9uKVslpy7IsKQ_wzamm3U8AfxNbtj2jynd9i0WSNBYr0ASNVd7ywasIwNy6aDLEZDzjMdpar0ZruzRFIbtKXBt2CqIbBHU0_x8FKmh5ndp4kIhr3s2jQNupvqmv7UwzRnSpEJkbubd_mUsGrLuIskEj2_gy0_o7nHyetiLOqnmFDr5Dp6sGfBlYeKhjVruKY1y7hqXfw_9tU4wRvuepOYZbK_s-6jumcErzjIDPXOYddLDh-TWLYWJN0AY621r2NGW3rPjXbdIeNaOuyajYPPPXaztbVQaF3v-ueNtY0gtbcmln_9k-N3nqQ4_b2kHQQNWPF7P6U8GcVUqxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571bfcee62.mp4?token=SMxpUg9uKVslpy7IsKQ_wzamm3U8AfxNbtj2jynd9i0WSNBYr0ASNVd7ywasIwNy6aDLEZDzjMdpar0ZruzRFIbtKXBt2CqIbBHU0_x8FKmh5ndp4kIhr3s2jQNupvqmv7UwzRnSpEJkbubd_mUsGrLuIskEj2_gy0_o7nHyetiLOqnmFDr5Dp6sGfBlYeKhjVruKY1y7hqXfw_9tU4wRvuepOYZbK_s-6jumcErzjIDPXOYddLDh-TWLYWJN0AY621r2NGW3rPjXbdIeNaOuyajYPPPXaztbVQaF3v-ueNtY0gtbcmln_9k-N3nqQ4_b2kHQQNWPF7P6U8GcVUqxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک این ویدئو را از حاشیه‌های خودش و تفاوت با بقیه حاضران در ضیافت شام چین و آمریکا منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/120138" target="_blank">📅 13:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120134">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3IzFZNngCzOEu5iZxeSyZbsHJcZPxkDPpoO31YzL3nbgddJ1fHQk2X44YTd_UZOXLZeutTCCxGRo53kyB5cGmW9uhDX-gRTD1b6kEa_sLNxwIZuGEq8nGALqNBoN6noReL13CIiIeXTc-X-KsBz4z-CmMsmTFjhRTguflImhfyphDVvoHXxC0Ac2tt3W9UjyOXOTAv7VISU937yrtMXQnVjHZ8-r7mvxVuOWSe36KCtURfsSGq8ubt5HYuLw5cWL8SCPouqF4GTbUtf3Ggb9kxjautzuOMDRiPuOuxS1WXG8pybVGXYOFNamA4fcw7M1Qo0gsC_JSoMpQ9_lHuwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXu1HFgjeSUhY7sRb6odnHBuqQ-GHDqraRaYcoU7Dl94fHeuc4LBmADgAeedRSJoBDheOAxGV4GDoD8-A-Fsr8MRgXhFunuOwcaSAtramCoTWo3JLwYyjF9UQR9NMdRGTkaD_skn7nXvYJiu965THXRwmPjIO_Ny1AmJwCrdnBOmw2hPiyqKrj0dRRaYwpqlSx0iQ_-824WlhdhIGEh-NlQf0MH2ouYQjRnKiign1SfOKXGb1nin04kcC6vazpRVRdzL8ZGRF4LBZxxNo2bnk-pVlhfG9jnqcFH2zinKc0EJwIYRkVLi2j3w0VaY3UPzNG0PN63ZAZXHcoU3C8LdXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuGZ7YD5s4KmfN9FTw3NtT6D9kLhrNjQH5X1au7609j6MvGhJVb5eudxtWm57aqEpeMnHPKVTC3uUdtgergxPBxGN2Rqemb__dDgpg0nSsocpmNTZA68EhwVDrtFni8jHxPfoPYty3iIErrv36xTZVUa6sJ_Bx6Viv08nn-3Loi5ZdVu41UsISx96vm6bZ1DF-aTGxAdXx1HO8XATzkVXi49LJ7zYTCeFZah6NPovs2jR1zfMLdRN47kUGFHn4fDg6blfLxUmHTDl57kAApAGQQVRYqn87uY-MJDAAwZGGKYBPC6bZklN6Q66DF6Jp8ZlBPHb6Q_UMgbokIEUBkh1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffd59f94c.mp4?token=RYIgFQzcGMeg8IftMvJneWrTHOYrnsfzL8ZL6FxJ7TLYmEr9vSpvwuy6IauW_XtyBwP2BYHKhQ0ZTGw45aIj106XsbWdad9Uwz5dSdTMHLYQvzWVE5Hhqw_FL8vE-2tJmVKda67fhy4li60-f6px5-MvFUaVmuY3YeT9ZnBkNbQsxvcd9RWnQXDFw6YgbtQ4HvGUoPUcIfjp2Nq8gfThej8L7GjZWp7gdPmFbkMyiYIyAGO2OiHrUe8nrXqTHneKM9S-unLN3ScALiJ-TNHlvHYCTWxgdgI6Gxu424ZNYr9NgOC6MNFTQrU8GtqBOIeABkCsOKWI0_65x9ZqwwxryA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffd59f94c.mp4?token=RYIgFQzcGMeg8IftMvJneWrTHOYrnsfzL8ZL6FxJ7TLYmEr9vSpvwuy6IauW_XtyBwP2BYHKhQ0ZTGw45aIj106XsbWdad9Uwz5dSdTMHLYQvzWVE5Hhqw_FL8vE-2tJmVKda67fhy4li60-f6px5-MvFUaVmuY3YeT9ZnBkNbQsxvcd9RWnQXDFw6YgbtQ4HvGUoPUcIfjp2Nq8gfThej8L7GjZWp7gdPmFbkMyiYIyAGO2OiHrUe8nrXqTHneKM9S-unLN3ScALiJ-TNHlvHYCTWxgdgI6Gxu424ZNYr9NgOC6MNFTQrU8GtqBOIeABkCsOKWI0_65x9ZqwwxryA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات نیروی هوایی اسرائیل به صور "لبنان"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/120134" target="_blank">📅 13:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120133">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
روبیو: اگر ایران فکر می‌کند ما برای رسیدن به توافق امتیازاتی می‌دهیم، سخت در اشتباه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/120133" target="_blank">📅 13:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120132">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaLNxnPYstlR2tGll5oCbybw-DI58oyPpl3_UrMDmkcGYUeKLhW509coL3aMmTIbmCFGY2mOwBIEgYZFnLxI-wSzlSwTjGak4q-bDEbDVh9ocLi9So4Ng87ycRe_Y11Sy5BHaFLM_zJvvPyAmzJy7h_PFZY5r4VbD3f5ulCQF17jCfDVjvRpsjv7aMiZaKp6_nyAqx0dD7c88wjwGna4326UbLGiPIT68-tzJlm-pnekVYCeALMIy1DqnSkf3naqtky5IJddRN13_urJcyrg-rkMUvmagfBh-_gdaxknySKIy23sGzfaFCUTNBr7wkLy-QKUXjbIkfsZwqST2X3yaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت‌بلاکس: قطع اینترنت بین‌الملل در ایران به ۱۸۲۴ ساعت رسید...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/120132" target="_blank">📅 13:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120131">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
شبکه «کان نیوز» امروز مدعی شد که اسرائیل و لبنان در حال نزدیک‌شدن به امضای یک توافق در واشنگتن هستند.
🔴
در این گزارش ادعا شده است: «این توافق شامل عقب‌نشینی مرحله‌ای ارتش اسرائیل از جنوب در ازای اجرا یا پیشرفت چشمگیر در خلع سلاح حزب‌الله خواهد بود».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/120131" target="_blank">📅 13:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120130">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658dded15f.mp4?token=AbRblyaQz_zKliQJ85A3fE3fLEPSL4Q3OjUxhoRTz2ZP8ooKnaxFHt_jSjGdb5hLYA92CqkcSTHZkjJ3ioR8Q34gDiTgX3hl4JVnwpR92h6rnyTj9G2kP0EACSWhZJXhsgOIuPgQA3NoauSgDNnwbz5fK9osuFkJXB7Bh9vZTxknOlXryqTjW51t275C6w9Xi0MuQrWx66FVhmqFPZkPhHySATHYT7ejCf2y54qPMKCWngCtd3Win6WhRC6NzNED1PxWi45CmIjf7sqjr2DV8cRzKr__G8gsvcl6jz0tUzutxfQP3x_2nRo_9zbxV4AJe6NLeeMracfGVY3ISIMgLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658dded15f.mp4?token=AbRblyaQz_zKliQJ85A3fE3fLEPSL4Q3OjUxhoRTz2ZP8ooKnaxFHt_jSjGdb5hLYA92CqkcSTHZkjJ3ioR8Q34gDiTgX3hl4JVnwpR92h6rnyTj9G2kP0EACSWhZJXhsgOIuPgQA3NoauSgDNnwbz5fK9osuFkJXB7Bh9vZTxknOlXryqTjW51t275C6w9Xi0MuQrWx66FVhmqFPZkPhHySATHYT7ejCf2y54qPMKCWngCtd3Win6WhRC6NzNED1PxWi45CmIjf7sqjr2DV8cRzKr__G8gsvcl6jz0tUzutxfQP3x_2nRo_9zbxV4AJe6NLeeMracfGVY3ISIMgLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله فیلم عملیات ۱۲ مه خود را که با استفاده از راکت‌ها و پهپادها، تجمعات ارتش اسرائیل در جنوب لبنان را هدف قرار داده بود، منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120130" target="_blank">📅 13:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120129">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
فرمانده کل ارتش : قدرت ایمان است که می‌تواند یک جنگنده اف-۵ را بر فراز مواضع نیروهای آمریکایی در کویت حمل کند، با وجود اینکه آن‌ها پیشرفته‌ترین سامانه‌های دفاع زمینی و هوایی را در اختیار دارند.
🔴
نیروهای مسلح با تمام توان خود از تمامیت ارضی، استقلال و نظام جمهوری اسلامی ایران محافظت خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120129" target="_blank">📅 13:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120128">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کرملین: روسای جمهور روسیه و چین در یک تماس تلفنی درباره نتایج سفر رئیس جمهور آمریکا به پکن گفتگو خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120128" target="_blank">📅 13:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120127">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuqKev2M4hXb4OCgfpRgGEXQ8-Xln2Rz2mKKiVQCLt8MGa8mvxYGQn2HIDm59mjN_FWvIIjsHqSU-UYAQ3Q9wnhzTDd2gXJKlmwqqKDsXAtF0UnlJ_0AX5TDPrLETFaswNHMvxRv7TRPVlg4I3yePayYaWqeHaLalNm4u-YYkfXlXsQ1j9aIhe1U8ncsKxjeiNQzJMhGPOCUqWpyWDlTD-v6WUSQ9eMEJiQpceHoeKMZ9XEGikPUkgJU6vGIAaPkt3wQncqB_mNggI3dJoiEB-_hVTx42rxxKNyjT-NPzEeAQTgkLSvPIOuCRsViCClgouW00sZg7ysrUWvx9jw3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خنثی‌سازی بمب یک‌تنی در شهرستان دلفان لرستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120127" target="_blank">📅 12:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120126">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بلومبرگ: امارات متحده عربی تلاش کرد عربستان سعودی، قطر و دیگر همسایگان خلیجی را به پیوستن به یک واکنش نظامی هماهنگ علیه ایران ترغیب کند، اما رد شد.
🔴
شیخ محمد بن زاید شخصاً با محمد بن سلمان و دیگر رهبران تماس گرفت.
🔴
هیچ‌کدام موافقت به مشارکت نکردند.
🔴
در نهایت امارات عمدتاً به تنهایی عمل کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120126" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120124">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f297a7c3f.mp4?token=pfnKVy_cVkY38ctyduPaLOfc-jQii3gh45w-EMy5_kXrnH4zI4_p_xMEMrlm7rDbEZ2HV9Oqjd6h1y0tUuGB6m8k8NjgZVqigW4lJsHSZZVWs4sbNmClnoHK9iPrX0MtjcWutREmxfo3nR_aKx1UTPetVIepOedkjuUCMjHaXZgBquAQwQH-7YnPvu1l7KHhCFezrT_0B6mLhemQ4yVy_ct9Mze8qhRdCML9qAtAsvZsCYlwpA0nYs-XLHITV5Kky_9ImT3QGM1q7YvGqNordH1oZWPQkDV6pMkSlBWXsFqjyGmXVCh4ngxiin6DHa-y1ToYseHNPx0nzf_I6zuAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f297a7c3f.mp4?token=pfnKVy_cVkY38ctyduPaLOfc-jQii3gh45w-EMy5_kXrnH4zI4_p_xMEMrlm7rDbEZ2HV9Oqjd6h1y0tUuGB6m8k8NjgZVqigW4lJsHSZZVWs4sbNmClnoHK9iPrX0MtjcWutREmxfo3nR_aKx1UTPetVIepOedkjuUCMjHaXZgBquAQwQH-7YnPvu1l7KHhCFezrT_0B6mLhemQ4yVy_ct9Mze8qhRdCML9qAtAsvZsCYlwpA0nYs-XLHITV5Kky_9ImT3QGM1q7YvGqNordH1oZWPQkDV6pMkSlBWXsFqjyGmXVCh4ngxiin6DHa-y1ToYseHNPx0nzf_I6zuAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات امروز به کرد های عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/120124" target="_blank">📅 12:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120123">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
روزنامه گاردین با اتمام سفر رئیس جمهور آمریکا به چین در گزارشی اعلام کرد: توافق ترامپ-شی درباره ایران دست‌نیافتنی باقی ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120123" target="_blank">📅 12:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کوبا اعلام کرد رئیس سازمان سیا به این کشور سفر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120122" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120121">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120121" target="_blank">📅 12:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120120">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/alonews/120120" target="_blank">📅 12:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120119">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
دستگیری ۲۲۳ نفر از اتباع بیگانه غیرمجاز در زاهدان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/120119" target="_blank">📅 12:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiuZ6P4KlXoYyhx5cv_eJQzMwTAWTFBmbu5TSRAKfGBXhxAiBlmsdwaUn0pXlexs38WfTNtOZN_ccP_XbuRVPJToQo6bpc3FacQ9xHdkgT6F-QSknjyzi6ddae7j1aIzQQ82z0rDJScANrjxycgavGmqfwEbItgHeeIadpZlFEK3ChKB7Cy2kiJNFnL0hxSeI8neQcDQ_0RBUrAg_H5psfBpD6zVzzGdIGuwWVdbSsptBdqhaJd_gzRxKtaqZlpMd_I68RNelgADg63sEd9pTp-14J3vdkcKF28WkjGshKgA4p4YNem6tS3uucIGLD_GgQIC3euJRkt-P4qYe6JqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال‌تایمز: اگر تا ماه آینده تنگهٔ هرمز باز نشود، به‌دلیل تخلیهٔ ذخایر استراتژیک شاهد موج گسترده‌تری از کمبودهای جهانی و افزایش قیمت‌ها در حوزهٔ انرژی خواهیم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/120118" target="_blank">📅 12:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120117">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبرنگار الجزیره: تهران به‌طور رسمی پاسخ واشنگتن به پیشنهاد خود را دریافت کرده است و ایالات متحده تمامی شروط ایران را رد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120117" target="_blank">📅 12:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120116">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
امارات ظرفیت صادرات نفت بدون عبور از تنگه هرمز را دو برابر می‌کند
🔴
امارات متحده عربی اعلام کرد تا سال ۲۰۲۷ ظرفیت صادرات نفت خام خود بدون نیاز به عبور از تنگه هرمز را دو برابر خواهد کرد.
🔴
بر اساس گزارش‌ها: شرکت ملی نفت ابوظبی در حال ساخت خط لوله جدیدی به بندر فجیره در دریای عمان است
🔴
هدف این پروژه کاهش وابستگی به تنگه هرمز عنوان شده است
🔴
بسته‌شدن مسیر هرمز در جریان جنگ اخیر علیه ایران، بازارهای جهانی را دچار بحران کرده است.
🔴
امارات هم‌اکنون نیز یک خط لوله با ظرفیت روزانه ۱.۵ میلیون بشکه از میادین نفتی داخلی به بندر فجیره در اختیار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120116" target="_blank">📅 12:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee518068.mp4?token=rs6rG4K-TB9wVYXWbscUVTr65UTDJrkWnD5xuR_-x7hYBsyn_HkP7nlk4QT-Jg7i_y-GUG6awbGP3sMmkqlSYAatr-iIpZr7uWQTuYhCRGMLN_ZiqPYA3Y3GrGulwPzx7iIMGxV10Lji6fJjZ-6kSWR4S2JK9d4utuBjztV5iPL20YgHabNaJ-MZjY3SXZM4KgyV__hjjeXc-qWe_8Iv9mwQccUlG7Zwrz30RaFBqsbkmBZyTG27MyyJUM41mgYxP5SJYNId4l3wa7ZgkP0ZXnmHL5aTa3oq3W8R0bywYpSY6nA7diUCtOX5877E0WVM1dbO3kZDiI7_kRRwcNes5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee518068.mp4?token=rs6rG4K-TB9wVYXWbscUVTr65UTDJrkWnD5xuR_-x7hYBsyn_HkP7nlk4QT-Jg7i_y-GUG6awbGP3sMmkqlSYAatr-iIpZr7uWQTuYhCRGMLN_ZiqPYA3Y3GrGulwPzx7iIMGxV10Lji6fJjZ-6kSWR4S2JK9d4utuBjztV5iPL20YgHabNaJ-MZjY3SXZM4KgyV__hjjeXc-qWe_8Iv9mwQccUlG7Zwrz30RaFBqsbkmBZyTG27MyyJUM41mgYxP5SJYNId4l3wa7ZgkP0ZXnmHL5aTa3oq3W8R0bywYpSY6nA7diUCtOX5877E0WVM1dbO3kZDiI7_kRRwcNes5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی : مشکل اصلی اینه که آمریکا هر روز یه حرف می‌زنه و پیام‌های ضدونقیض می‌فرسته
🔴
در مورد ایران هیچ راه‌حل نظامی‌ای جواب نمی‌ده
🔴
این همه مدت هی تهدید کردن، ولی نه نتیجه‌ای گرفتن نه از جنگی که راه انداختن چیزی گیرشون اومد
🔴
هرچی بیشتر تهدید کنن، بیشتر شکست می‌خورن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120115" target="_blank">📅 12:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120114">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUy7q4qqD0hQyIRJdgn9M1yob8XXjEjq2taliys__yICEsxJ-fQd3PMN8s-nG0oliPm9g7YOoTAQDaleFywvqAl8NWp3MF71Q6CkN4j0t_rdLF3wWoRSbwgfvCHwYmNT-J00eQsy1OHTp-Sv6CW-LRO2OZnyJHF_PIjFYwA15gYsqQ0coMVE8UwA4eK8JuKGJQv7XT_EGwCFNs--trZVpWC-4u6oztJl_W1K2-tuedmPvYWBeVQC6gywRDolJ0iKynRNLXm05EP9Ca9qR_OwYSo2YiWiLURavAZ0zW-L8ABqa-n7n5aJwR0HohhPvUTeVqSICtUFGJaVE0p1Xf9UIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای باری نظامی آذربایجان از طریق حریم هوایی ترکیه به سمت تل آویو در حرکت هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/120114" target="_blank">📅 12:08 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
