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
<img src="https://cdn4.telesco.pe/file/OIkWjs16JwkqQ-kimOUR-LB12u6ddOU17IjuNvqhdZqjrscW27ey3w9c7ra2bU5pHiTair2dXFx-kkTFuBDRwNMZN8U3Fjcpp1tCnkN_TdOFY-nYXEyBnyJ9xYQWGW7VbMMARVuBHofBc7FaKel0PWPj65JwZvzzq89DkAyep9zu7Jdy2l-jbdWwoJIOD83Q77FdPRccBdDO0UKf9hcgvaHEA8oWXt3xJIWxc6YqhPReNgG9Strj_CggawWFdpJ4dgfhwOvTtCxUvV8YZj5LOr7XRzzJhaTl6yXH3ZCEnzf8MzaiJiXNMphDhUn3Z9TPRQhiwJKKGVQ-8sK3nNJIVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 442K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 02:44:50</div>
<hr>

<div class="tg-post" id="msg-21469">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کوینتلگراف : گانون کن ون دایک، سرباز آمریکایی، متهم است با استفاده از اطلاعات سری درباره عملیات برکناری نیکلاس مادورو، بیش از
۴۰۰ هزار دلار
از معاملات پولیمارکت سود کرده است. او اتهامات را رد کرده است.
کمیسیون معاملات آتی کالاهای آمریکا
تلاش دارد در پرونده کیفری او دخالت کند و درباره قانونی بودن قراردادهای پولیمارکت نظر بدهد، اما وکلای ون دایک با این اقدام مخالفت کرده‌اند. رسیدگی به پرونده مدنی CFTC نیز تا پایان پرونده کیفری متوقف شده و دادگاه احتمالا اواخر ۲۰۲۶ یا اوایل ۲۰۲۷ برگزار می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/withyashar/21469" target="_blank">📅 02:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21468">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQo3dAagAUSb6NDgQtEwT0DHCGPNj6GxbZGLBHxqCIuMaNFNANZkJUv5oqSCLjHI9nCnVhRoj4E2IyrFRGQm8HkX8QpY5Emq4qtTTmH5FRrm4QiF3-9mBU0UjOMPGCW17Zmix38dW3EpUO8Cxv2HdNIbPEeNYMFzNErARxXwaDrn8vpDsQlzIQmKk2RzyZKEemcTpA86zfizePUcAlSjqk09_bo546BJ-KrueC0kAH-ZGLOrp6ECQIqVgeWCEse1_-6D92dGJIHlSGLua-Qvt_bVrGgdYnMMWUo4VJ79OzqSrFy3grvOzz7ml8OPsyftwbbxtw_woJmXGcCf5ClNHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست : ایوانکا ترامپ در سفر خانوادگی به کاستاریکا، مهارت‌های موج‌سواری خود را به نمایش گذاشت.
ایوانکا ترامپ و جرد کوشنر در سال
۲۰۰۹
ازدواج کردند و سه فرزند دارند
@WarRoom</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/withyashar/21468" target="_blank">📅 02:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21467">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncKVPwPDHEVIYc0jU1oMMRDRACRveA2QZCsUTX-TcB5fPgeEyiGo2dKH9B-FRU1GVmnmo4PnCnAw-6d6bijT0wenPGrI1rJST7QPdeCc7lTNbiE-Jb06JyWmlm_ErSL291E7PPDpX-Kl2RlKMf2NSduwDo_Xqnk8V60aPS_FxN6AlIk-wJZV_Wrk-MGNcTSLMpgOC9-iS-qKJMyVbbsfBuutkjtVxqSd6RHslX1Bvb5NRVJcZFX9pdVLtnNcOvSlmjSTk4JH5wjMW8KSQMka-iEKKMPFeghKIBkh3ISt0unt7PKiFgxR18l5XADf7_qQuDRx0onn1K0Eq6gy0EC2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : تفنگداران دریایی ایالات متحده در حال انجام تمرینات سنگین آمادگی بر روی ناو جنگی یواس‌اس باکسر (LHD 4) در حین دریانوردی در دریای مکران هستند
@WarRoom</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/withyashar/21467" target="_blank">📅 02:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21466">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرقی منطقه «الشیشاه» در عمان دریافت کرده است. ناخدای یک نفتکش گزارش داده که کشتی با یک پرتابه ناشناس هدف قرار گرفته و در اثر آن، موتورخانه آسیب دیده و کشتی از حرکت…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/withyashar/21466" target="_blank">📅 01:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21465">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVhcM4u57HlgkbZl3d05l4xqufIZ4yMQ7OAAPWeK8BS7uIkSFnubqvuow3OCqTVrP8FCbYLsebep4vuMhyv-yXDlWfbukYoImCDMAD_2w_WfjevZroAImhJjxty-IEhp0kU5pLWesXGTWIjdKQCybP5BDxwQNlGlfwtI2nbL4bhOM9XWYHr9bv40NCGzvKMkLdMLcm1Jv-usW3BKuNhNCjFWrqp4YVswXOdkDQGoxSE469giX_GXARbX-byUDqm1ozj5DW33NQZ1VVSu70sbgEmtMlkhutJWTG8fIVytWwfOjWVdL95A9UTRWsCGnh4AGGOtpFAgsSwZ-0sIEvdgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرقی منطقه «الشیشاه» در عمان دریافت کرده است. ناخدای یک نفتکش گزارش داده که کشتی با یک پرتابه ناشناس هدف قرار گرفته و در اثر آن، موتورخانه آسیب دیده و کشتی از حرکت بازمانده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/withyashar/21465" target="_blank">📅 01:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مارک لوین : ایران سعی کرد یکی از پسران نخست وزیر نتانیاهو را ترور کند. آنها همچنین برای سر بارون جایزه تعیین کرده‌اند…
@WarRoom</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/withyashar/21464" target="_blank">📅 01:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21463">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cde83dba14.mp4?token=cafA8bF_5qe2RcUmXU8UeFJ4rDpmjsDrS6L7UahkLt6q6HpV2wBwnZ6mdDFQOrXvT2GNlXhMZiVB7h7S2m3Unrue3w58TmOX-7V68zHX5uHYy9362t1_IG9xzZj-kRnaaM-kPwRIZWnZj0Cwyp44wdZNHYIuJ11ifL85ToSw0N_n2X7Xa5c5ie4SacnBVN0hF0D5HX5HvbxsHj485NOE6_AM1b9bGjyT0bstE8N5iF_2c0QR5n_Zaf2u41XaiRIgdaHog9pKvKgcTFC-IiU_VILJS7pmhSTee1sjvb3HvFgk2VrfCGPRT6v2aZx3-bHwBZEliwz8g-Ft_FhLO8OHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cde83dba14.mp4?token=cafA8bF_5qe2RcUmXU8UeFJ4rDpmjsDrS6L7UahkLt6q6HpV2wBwnZ6mdDFQOrXvT2GNlXhMZiVB7h7S2m3Unrue3w58TmOX-7V68zHX5uHYy9362t1_IG9xzZj-kRnaaM-kPwRIZWnZj0Cwyp44wdZNHYIuJ11ifL85ToSw0N_n2X7Xa5c5ie4SacnBVN0hF0D5HX5HvbxsHj485NOE6_AM1b9bGjyT0bstE8N5iF_2c0QR5n_Zaf2u41XaiRIgdaHog9pKvKgcTFC-IiU_VILJS7pmhSTee1sjvb3HvFgk2VrfCGPRT6v2aZx3-bHwBZEliwz8g-Ft_FhLO8OHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا می‌توان گفت که در حال حاضر حملات نظامی علیه ایران متوقف شده‌اند؟
پیت هگست: نه. اگر لازم باشد از حملات نظامی استفاده کنیم، این کار را انجام خواهیم داد. اگر ایران آن‌قدر احمق باشد که زیاده‌روی کند یا با ارتش آمریکا درگیر شود، ما هر کاری را که لازم باشد انجام خواهیم داد. فشار اقتصادی در حال حاضر بیشترین آسیب را به آنها می‌زند، اما به هیچ‌وجه استفاده از حملات نظامی را، چه در تنگه هرمز و چه در اطراف ایران، منتفی نکرده‌ایم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/withyashar/21463" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21462">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa3f78fcb.mp4?token=STeIOqk79eqHN5YRj7Csr5BV6iQTXRchRbJ9so1xIl6uJDHfcVFSoU__UGmIHAhH96buM66MJBoZ4Uo1SrDws6gvWLskspIdqpZZC7izqWj7fA-yy8TDtZLLsEV8cxczdHZsOBaebArxUuzS4Za9BXQ-q5Wq-oY3wl7AEXQv68ZwAFfQ6oTg4P4WAfB2NuEgwLah6lePuMNrr3XR5fDZaglHfhweXQh_gjZjm-NJbDZvrYTB-zJOshXlhPP_CgpzKv3YXG_FVZMiPQUPBljDO4sxSE6A186XEZjuYTwyfuUvT7memsoUPrBBfAwVjez7Otv2LHkdS5n56lWjL02KQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa3f78fcb.mp4?token=STeIOqk79eqHN5YRj7Csr5BV6iQTXRchRbJ9so1xIl6uJDHfcVFSoU__UGmIHAhH96buM66MJBoZ4Uo1SrDws6gvWLskspIdqpZZC7izqWj7fA-yy8TDtZLLsEV8cxczdHZsOBaebArxUuzS4Za9BXQ-q5Wq-oY3wl7AEXQv68ZwAFfQ6oTg4P4WAfB2NuEgwLah6lePuMNrr3XR5fDZaglHfhweXQh_gjZjm-NJbDZvrYTB-zJOshXlhPP_CgpzKv3YXG_FVZMiPQUPBljDO4sxSE6A186XEZjuYTwyfuUvT7memsoUPrBBfAwVjez7Otv2LHkdS5n56lWjL02KQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: فرماندهی مرکزی ایالات متحده اعلام کرد تا امروز (۲۴ آگوست)، نیروهای آمریکایی ۷۱ فروند را تغییر مسیر داده، ۳ فروند کشتی را از کار انداخته و ۲ فروند شناور را به عنوان بخشی از محاصره جاری بنادر ایران، توقیف کرده‌اند
ویدئویی از ناو هواپیمابر جورج بوش، مستقر در دریای عرب و پرواز جت‌های جنگنده F/A-۱۸ نیروی دریایی آمریکا.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/withyashar/21462" target="_blank">📅 00:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21461">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZkLhGbzFJm8WLx_eSEJQBaHabSyiJLi6k7aJBMUWXp59eeZDZnd-cf9SY465HvMZJwYSXhu1oJlYxn4osvYFvo2AdIJct6v5SuMrw0XL4ZIZpWHQM9lVfzmILsfxLlzw5jG9AKkK1rnCt0W6ttTyjnGjFjuOXTYBGcovlMruG-0MPkxqmJE1NEBVXphoohD0-XY8ypCtL6BB9HoM9t8pNhKbkGvXM9wHAbldoLwpd10OaHx1gonjQvhxPy9o1xdyGanOFjwS1oU8AVc2F8sPmiFiftWaYWYNxONMJCq3bA6KhNvlgiukRrvFqa4UAqgMq8NC-6rFjV7w6tAFBJdCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم پاکستانی سیک و زد برگشت… همکنون نزدیک اسلام آباده ، همچنین ۵ سوخترسان آمریکایی همکنون با سیگنال روشن در حال انجام مأموریت در تنگه هرمز  هستند
@WarRoom</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/21461" target="_blank">📅 23:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21460">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiSb-dlf-JRPyLJDqGdPvg3VbK7JVfT0kpg1pIsVmBOpTBn87fqM3VwjHjJPdBZpTxmvXVPgcrCamC3UUsahNhPSI7r4eMXwhY_kQO36ZxfMs8YhsHVxlaqZiC-Ksi3ARGcbhrn71EFAaRTPPpjjsKg4yy-Mtn4e8v-76YPT6CYo38NpwPCE5E5u8ZBIYNddt9SWjS8PBgg4VVjN1vNUdxo0P4kh5yw0ItVSQY-mV6Gre0K1lrBvAxoxtm_R82E1Sdd6GAVZ-qj3zbSOLeE4iKryxzQ-x5Fjxn5eSjxLM7Ee4CoRCj6oG3rKfyS9dMMIXTh8FtzK_cW4X9FIRddebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه ایالات متحده آمریکا، اداره امنیت دیپلماتیک، برنامه «پاداش برای عدالت»:
تا ۱۰ میلیون دلار پاداش برای اطلاعات درباره رهبران کلیدی سپاه پاسداران انقلاب اسلامی ایران.
این افراد فرماندهی و هدایت بخش‌های مختلف سپاه پاسداران را بر عهده دارند؛ نهادی که از دیدگاه دولت آمریکا، برنامه‌ریزی، سازمان‌دهی و اجرای اقدامات تروریستی در سراسر جهان را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/21460" target="_blank">📅 23:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21459">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4O8EX2NsGEYDA0yvO6oDHZO48ax1SZ-cRsRjTvjQlB9mSxsZ_3_1ALwPP-W0PNSbReXnR2yKX5lLbO0ORwz9c76fB0QuI1dBURTJBUOhsxYZOx1WvxPSt6VEGZzRRcKQ8XRP4Is8ytMHDSBBYxJ61Xl4X_TedsDeFR7HsNpLoLIueth9Mh_aOpo5zEer_YEVvnSBUIFd4dgleTYw87FfRszt9h6_hMrccL4gl9bEEV456TV1-gX-SfINlWcEEwZGDUwdlImhTPln9_KY5c7KQj0X25RtKGXmMrtRSUZ2Xd9GDAQQNQYWhR8C5K1g4rBiIC5zm-O42dXwJ3BlkXE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن کج بند رضایی : نتانیاهو و ترامپ یک برنامه برای 6 ماه محاصره دریایی و اقتصادی علیه ایران را دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/21459" target="_blank">📅 23:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21458">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو : تبریک به ترامپ و بِسِن بابت آخرین تحریم‌ها علیه رژیم ایران.
شما به حق هزینه گزافی را از آن دیکتاتوری ظالم و از کسانی که به تجاوز مداوم آن کمک می‌کنند، دریافت می‌کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/21458" target="_blank">📅 22:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21457">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">@WarRoom
Economic Covid</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/21457" target="_blank">📅 22:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21456">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پرس تی وی : ایران مستقیماً پیشنهاد مورد حمایت ترامپ که چند ساعت پیش از طریق پاکستان به ایران ارائه شد را رد کرد  ایران از سرگیری مذاکرات با ایالات متحده را نیز نپذیرفت @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/21456" target="_blank">📅 22:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21455">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=fHFyPWwaboEi1lXvheOBIxWDorBA61cajRkIMnC_4dxnlLyR2vpyM4J-nZQP2-cLSdvfnGjbs_vJQq9cCwXzgrEvrTtMIRB6D0B5r4-Zsmw1NcBh0RkMrWrSfZL8USndtUGUmQHmqaw0NLH0Cu6hcWF78SK82T0GtbOVMZuQgvhbjH5WGnTqEC_o2y1R9RMXsO2rb1EU6938v_OZtpwzThkShZj9CJ0BxTvakfW00s13PfCeSpM-giGA6QEKFhwPEltgZLiCF3Jjc6tmkfyGQK5SPay0eveK3hUGVcgPaLKmv7O5ltpGqFskc6udw21Y-XRYe9VQWcCkQ2OB8Mrb1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=fHFyPWwaboEi1lXvheOBIxWDorBA61cajRkIMnC_4dxnlLyR2vpyM4J-nZQP2-cLSdvfnGjbs_vJQq9cCwXzgrEvrTtMIRB6D0B5r4-Zsmw1NcBh0RkMrWrSfZL8USndtUGUmQHmqaw0NLH0Cu6hcWF78SK82T0GtbOVMZuQgvhbjH5WGnTqEC_o2y1R9RMXsO2rb1EU6938v_OZtpwzThkShZj9CJ0BxTvakfW00s13PfCeSpM-giGA6QEKFhwPEltgZLiCF3Jjc6tmkfyGQK5SPay0eveK3hUGVcgPaLKmv7O5ltpGqFskc6udw21Y-XRYe9VQWcCkQ2OB8Mrb1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/21455" target="_blank">📅 22:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21454">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایالات متحده، سوریه را بعد از ۴۷ سال از اوایل انقلاب اسلامی از فهرست حامیان تروریسم حذف کرد
‏سوریه از سال 1979 تحت تحریم‌های کشورهای حامی تروریسم آمریکا قرار داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21454" target="_blank">📅 21:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21453">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c663b3442.mp4?token=RfPQ36pLNdo1pKsXIaY99K_IDOC0pwaF6M9PSOr_pl3CbwcsQgvB-J_lS7UziBzcX4W8WqyVqfRpfLj4Chl6qmmqWHgMRZeqihS7zcwAt2o5M3vhQqqE_yex-e-skshIhL-pBj46jerxNl8IiwU8gY-GuzMaaHEPFcxQLdA1BGQ5kPCc_EEXkVjK2dPr4o9gK8maDMv6DEHkyf3uYDSewcRmUIUfbc0QvgZHXQZ2O5QHJGeJmG6yGq8VQuR-eab0Lu38JJC0IS9silyN-TK96HehkKXfLBWGkE5k1Sc6utN4q4WS68Lq2o_lyqC9mEqgAtbDyw2FZPlgg7D6U9hezQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c663b3442.mp4?token=RfPQ36pLNdo1pKsXIaY99K_IDOC0pwaF6M9PSOr_pl3CbwcsQgvB-J_lS7UziBzcX4W8WqyVqfRpfLj4Chl6qmmqWHgMRZeqihS7zcwAt2o5M3vhQqqE_yex-e-skshIhL-pBj46jerxNl8IiwU8gY-GuzMaaHEPFcxQLdA1BGQ5kPCc_EEXkVjK2dPr4o9gK8maDMv6DEHkyf3uYDSewcRmUIUfbc0QvgZHXQZ2O5QHJGeJmG6yGq8VQuR-eab0Lu38JJC0IS9silyN-TK96HehkKXfLBWGkE5k1Sc6utN4q4WS68Lq2o_lyqC9mEqgAtbDyw2FZPlgg7D6U9hezQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: کشورهای خلیج فارس باید از خود بپرسند مدارا با رژیم ایران در سال‌های گذشته چه دستاوردی داشته است؛ در حالی که آمریکا ایران را هدف قرار می‌داد، ایران نیز کشورهای خلیج فارس را بمباران می‌کرد و
مدارا با این رژیم کارساز نیست.
او خطاب به نیروهای عادی حامی حکومت گفت اگر حقوقشان قطع یا عقب افتاد، از خود بپرسند فرماندهانشان کشور را به سمت پیروزی می‌برند یا نابودی؛ همان‌طور که
دیوار برلین زمانی فرو ریخت که سربازان تصمیم گرفتند به مردم خود شلیک نکنند.
بسنت گفت تا پایان همین هفته یک مؤسسه مالی بزرگ دیگر به‌دلیل ارتباط با ایران تحریم می‌شود و
هیچ‌کس از تحریم‌های آمریکا در امان نیست
؛ هرکس در انتقال پول نفت ایران و تبدیل آن به منابع مالی برای سرکوب نقش داشته باشد، هدف قرار خواهد گرفت.
در پاسخ به خبرنگاری که پرسید چرا با وجود توصیف این اقدام به‌عنوان «روز دی» اقتصادی، تحریم‌ها فوراً اعمال نمی‌شوند و یادآور شد که روز دی تهدید به تهاجم نبود و آمریکا نیز جدول زمانی مشخصی به آلمان نداده بود،
بسنت گفت آمریکا به کشورها فرصت می‌دهد رفتار خود را اصلاح کنند و نمی‌خواهد با اقدامات ناگهانی سیستم مالی جهانی را مختل کند؛ اما این مهلت کوتاه است و روند اقدامات بسیار سریع خواهد بود. او تأکید کرد تحریم‌های ثانویه ابزار قدرتمندی هستند و اگر طرف‌ها انتظارات آمریکا را برآورده نکنند، باید انتظار داشته باشند از
سیستم دلار آمریکا
کنار گذاشته شوند. بسنت در پایان گفت:
«ما این را یک شلیک هشدار و شفاف‌سازی انتظارات می‌دانیم؛ اگر افراد نخواهند انتظارات ما را برآورده کنند، باید انتظار داشته باشند که مجبور شوند سیستم دلار را ترک کنند.»
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21453" target="_blank">📅 21:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21452">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پرس تی وی : ایران مستقیماً پیشنهاد مورد حمایت ترامپ که چند ساعت پیش از طریق پاکستان به ایران ارائه شد را رد کرد
ایران از سرگیری مذاکرات با ایالات متحده را نیز نپذیرفت
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21452" target="_blank">📅 21:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21451">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‎ وزارت امور خارجه اسرائیل: حتی دایناسور هم جلوی دوربین ظاهر شد ولی مشتبا نه
@WarRoom
🦖
🦕</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21451" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21450">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9176177aa.mp4?token=rkNdcwG1GFdTrZVD1k53rjxv9y7IGyvUvGWaVTZL2v2qiqrlo3eQk4-YTgeszCLN_F288hIWWFCMs1RR2fzLXjHBeU1NTtB6XOsuFVHdQl1gjG-yr3LVWSet_Ae4gZOTMKo4FHuPSr5X61tYn64W3zn0ZBIqoOIFILZhPiB4UEjtm1jjHOkV_Sxo1iYhux4jqpBBkpv6oOopPXOyuqOT-bvmE2ZBnWsWG7KfGflK9gY4Xcz2qdVCQU1w7yomDO_Z4GesC2D0zryLoIi2eRrRdm1fUUMN_KL2D2ewjcqEaPZjnqg_TF-i5bqPmxDORuC0Z_S8idjlhK5z_qe6A5KXq6iNcl99bqBzi-jM4Iqtl5kwn_TYLEi7DbqRl4vyZCc63DMEHmK5UmlCVDjpqX3cDAWUVp4chVdIqfqvSAK-gyFYmganICkraeLyjA4DtU6fhTuF3KTWHRhMN06rdUobnmmqvCNDAmDXmLrj4vchWUbTevSYGlxzeviUXsFs5jkq2M5rTJU6uz0u2xZOzu-BSNUN0D3HGpvw2DDg0D0tuSzSH6ldYj7GcxAImojSdFeBMKcwhE6dJpuVqBua6uzCfEUVqydU0wVYbn5EBtRaJPd-eqNMrt983ZeRU-IntF29LCKFMAlZkVNWFOk5PHhNfRB98vPwMIwSFNfNe6aANcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9176177aa.mp4?token=rkNdcwG1GFdTrZVD1k53rjxv9y7IGyvUvGWaVTZL2v2qiqrlo3eQk4-YTgeszCLN_F288hIWWFCMs1RR2fzLXjHBeU1NTtB6XOsuFVHdQl1gjG-yr3LVWSet_Ae4gZOTMKo4FHuPSr5X61tYn64W3zn0ZBIqoOIFILZhPiB4UEjtm1jjHOkV_Sxo1iYhux4jqpBBkpv6oOopPXOyuqOT-bvmE2ZBnWsWG7KfGflK9gY4Xcz2qdVCQU1w7yomDO_Z4GesC2D0zryLoIi2eRrRdm1fUUMN_KL2D2ewjcqEaPZjnqg_TF-i5bqPmxDORuC0Z_S8idjlhK5z_qe6A5KXq6iNcl99bqBzi-jM4Iqtl5kwn_TYLEi7DbqRl4vyZCc63DMEHmK5UmlCVDjpqX3cDAWUVp4chVdIqfqvSAK-gyFYmganICkraeLyjA4DtU6fhTuF3KTWHRhMN06rdUobnmmqvCNDAmDXmLrj4vchWUbTevSYGlxzeviUXsFs5jkq2M5rTJU6uz0u2xZOzu-BSNUN0D3HGpvw2DDg0D0tuSzSH6ldYj7GcxAImojSdFeBMKcwhE6dJpuVqBua6uzCfEUVqydU0wVYbn5EBtRaJPd-eqNMrt983ZeRU-IntF29LCKFMAlZkVNWFOk5PHhNfRB98vPwMIwSFNfNe6aANcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : مؤسساتی که انجام معاملات برای ایران را تسهیل می‌کنند. صحبت‌های زیادی درباره هدف قرار گرفتن بانک‌های چینی مطرح شده، اما ما در اینجا هیچ‌کدام از این مؤسسات را هدف قرارگرفته نمی‌بینیم. آیا قرار است چنین اقدامی در ادامه این کارزار انجام شود، یا آتش‌بس تجاری بسیار حساس با چین ممکن است مانع از این شود که تا این حد پیش بروید و چنین گام بسیار بزرگی بردارید؟
بسنت :
ما می‌خواهیم امروز در اینجا کاملاً روشن کنیم که هیچ‌کس از دسترس تحریم‌های آمریکا خارج نیست. اگر مؤسسه‌ای انجام معاملات را تسهیل کند و بخشی از آن اکوسیستمی باشد که نفت ایران را به پول و در نهایت به سرکوب تبدیل می‌کند، آن مؤسسه نیز هدف تحریم قرار خواهد گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21450" target="_blank">📅 21:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21449">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال 13 عبری: ایران به کشور های خلیج فارس هشدار داد که پایگاه‌ها و تجهیزات آمریکایی را تخلیه کنید، در غیر این صورت ما به خاک شما حمله خواهیم کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/21449" target="_blank">📅 20:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21448">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529f1c3c67.mp4?token=U9SQwcbYHAdyygpDYSNglhSmclMFgtGfqdV4JkvBKcD6-lmiSk2oZpxp83ByTo9LpF7bo44vv0flB8AQ5Lp2qg1QLW-ebkg7oxumfL_w1K8hdJ9d_pyry6VEuWoHi-djXqtniGZA8B_DCJqnVg754nFhqdXN4Pea3CCz0TJDToHlAA5h7MldMXlAsKzz_eK5tUhNjSVegZ5GrfqWAeYXB_AM0QqA-WYRDDr8iZijwjprK18Bg4thBry6uMtOejZieNUqIG862aZXxLyYpCHLG9ghecuZU24iKkk43cGgQBtPNCBHenckXdcZ3BuaiwMCpOpCc_sRwx4ES5W015qOYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529f1c3c67.mp4?token=U9SQwcbYHAdyygpDYSNglhSmclMFgtGfqdV4JkvBKcD6-lmiSk2oZpxp83ByTo9LpF7bo44vv0flB8AQ5Lp2qg1QLW-ebkg7oxumfL_w1K8hdJ9d_pyry6VEuWoHi-djXqtniGZA8B_DCJqnVg754nFhqdXN4Pea3CCz0TJDToHlAA5h7MldMXlAsKzz_eK5tUhNjSVegZ5GrfqWAeYXB_AM0QqA-WYRDDr8iZijwjprK18Bg4thBry6uMtOejZieNUqIG862aZXxLyYpCHLG9ghecuZU24iKkk43cGgQBtPNCBHenckXdcZ3BuaiwMCpOpCc_sRwx4ES5W015qOYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است. ایران اکنون دو راه دارد:
انزوای کامل جهانی و اقتصادی در حد تأمین نیازهای اولیه، یا بازگشت به مسیر عادی و پیوستن دوباره به اقتصاد جهانی.
وزارت خزانه‌داری تمام شبکه‌ها و واسطه‌هایی را که ایران برای قاچاق نفت و دور زدن تحریم‌ها استفاده می‌کند شناسایی کرده و برای قطع منابع درآمدی حکومت و سپاه وارد عمل می‌شود.
رئیس‌جمهور ترامپ با رهبران کشورهای جهان تماس می‌گیرد و از آنها می‌خواهد تعامل خود با حکومت ایران را متوقف کنند؛ کشورهایی که همکاری کنند از شراکت با آمریکا بهره‌مند می‌شوند و کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
کشورها مهلت مشخصی برای توقف فعالیت‌های موردنظر آمریکا دارند و در صورت عدم اقدام، واشنگتن به‌صورت یک‌جانبه وارد عمل خواهد شد؛
تمام شعب بانک ملت باید تعطیل شوند
و هر نهادی که به پول‌شویی برای ایران کمک کند، از نظام دلار آمریکا حذف خواهد شد. تحریم‌های جدید
دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی
را هدف قرار می‌دهد و بیش از
۶۰ فرد، نهاد و شناور
مرتبط با تأمین فناوری هسته‌ای و موشکی، عملیات سایبری و درآمدهای نفتی ایران نیز تحریم می‌شوند.
هیچ ابهامی در موضع آمریکا وجود ندارد؛ هرگونه تعامل اقتصادی با این حکومت، طرف‌های دخیل را در معرض تمام قدرت آمریکا قرار خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21448" target="_blank">📅 20:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21447">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اتاق جنگ با یاشار
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/21447" target="_blank">📅 20:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21446">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتنياهو
:
ایران تلاش کرده است تا یکی از اعضای خانواده من را ترور کند.
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/21446" target="_blank">📅 20:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21445">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یاشار تروخدا یه گروه بزن چت کنیم خیلی دلمون گرفته یکم دوست پیدا کنیم</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/21445" target="_blank">📅 19:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21444">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐁𝐫𝐨𝐧𝐢𝐥</strong></div>
<div class="tg-text">یاشار تروخدا یه گروه بزن چت کنیم خیلی دلمون گرفته یکم دوست پیدا کنیم</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/21444" target="_blank">📅 19:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21443">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoep67DFwCc_6hQrCljIO4RNP3U66HJR3hfsBA8BNCWABhlqY2YUBZNJfktyRZT4a37ar1lH7mkGR3VW_ugFMMKokUPya18QxXem7Yo-bD9GWAIcxV3nKIcUO-RmvNdsVEV2KE08e1aXthgzbxpWvHRXzZ231L4CDKu1tugJWNaKK-oJtqDwto5H6lkShga8j-NRRQRoD-g8_CLYkzcP6eI1BzO_YLlyGAlvOVlgjAycU9I4clQqC2R3PaRDrHA79b9zRCk-sgyYI5USeHwVwtGL3vAerHIken3obpm4YF_pEZ9mMLLXZCOjsYBxn411f8sqarhKgBhLGuM7nSfT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دموکرات‌های چپ افراطی با نظرسنجی‌های جعلی دیوانه‌وار عمل می‌کنند و آنها را با حجمی بی‌سابقه منتشر می‌کنند. به این اقدامات «عملیات تضعیف روحیه» می‌گویند؛ یعنی تلاش می‌کنند روحیه جمهوری‌خواهان را تضعیف کنند تا آنها پای صندوق‌های رأی نروند. اما نظرسنجی‌های واقعی فوق‌العاده هستند و روحیه در کشور ما هیچ‌گاه به این اندازه بالا نبوده است.
ما در برابر همه پیروز هستیم، از جمله ایران؛ کشوری که در یک مارپیچ مرگ اقتصادی و نظامی قرار گرفته است
. از توجه شما به این موضوع سپاسگزارم!
@WarRoom</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/21443" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21442">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ممباقر : با عاصم پاکستانی درباره مواردی که آمریکا به تعهدات خود، طبق یادداشت تفاهم، عمل نکرده است، گفتگو کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/21442" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21441">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش فاکس نیوز : کاخ سفید تا ساعاتی دیگر در آستانه اعلام سخت‌ترین تحریم‌های تاریخی آمریکا علیه ایران قرار دارد؛ اسکات بسنت این اقدام را یک «حمله اقتصادی» گسترده برای قطع ارتباطات مالی و تجاری ایران توصیف کرده است. هم‌زمان، ریال ایران به پایین‌ترین سطح تاریخی…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21441" target="_blank">📅 19:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21440">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ: کانادا سال‌هاست از آمریکا سوءاستفاده کرده است؛ آنها خود را مستحق امتیازات ویژه می‌دانند، در حالی که ما به کانادا نیازی نداریم و این کاناداست که به آمریکا نیاز دارد. دیگر با کانادا در تجارت مانند یک ایالت رفتار نخواهد شد و آنها از جمله بدترین کشورها در جهان برای تعامل و تجارت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21440" target="_blank">📅 18:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21439">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش فاکس نیوز : کاخ سفید تا ساعاتی دیگر در آستانه اعلام
سخت‌ترین تحریم‌های تاریخی
آمریکا علیه ایران
قرار دارد؛ اسکات بسنت این اقدام را یک «حمله اقتصادی» گسترده برای قطع ارتباطات مالی و تجاری ایران توصیف کرده است.
هم‌زمان، ریال ایران به پایین‌ترین سطح تاریخی خود سقوط کرده
و فشار تورمی افزایش یافته است.  ایران نیز تهدید کرده کشورهایی را که در اجرای تحریم‌های آمریکا همکاری کنند، تلافی خواهد کرد. در همین شرایط،
عاصم منیر، فرمانده ارتش پاکستان، برای میانجیگری و احیای مذاکرات میان تهران و واشنگتن به ایران رفته
و
وزیر خارجه عمان نیز قرار است برای گفت‌وگو درباره تنش‌ها و وضعیت تنگه هرمز به تهران سفر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21439" target="_blank">📅 17:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21438">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رویترز: پیش‌بینی می‌شود صادرات هند به ایران، شامل چای، برنج و برخی داروها، به دلیل تحریم‌های ایالات متحده کاهش یابد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21438" target="_blank">📅 16:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21437">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بیتکوین برای عبور از مقاومت ۸۰،۰۰۰$ خیز برداشت
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21437" target="_blank">📅 16:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21436">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuaEA5rvLnf8d269-YsSPjbGkGCnjTy3BCh1OQt2H3y-RjkcEVrInqwGmAj4nGvjU2hbDNJhJRszyuJ0sVSpkEkXnlsQBjzyfykGXTdoLhtyvnbvPQU8Cpf08_cK36vDCkSYO8ARoyZvy4qo7E1bj1EqtdxSjpH2GSC7B3VpmI8R4ZnQ8RKdazV15QVrSO6YGMXOPEKf36_ginuJT5QiHcWkPK2t2agbjwm2ogJgCrUD6_u0qbFKq3UqhROhmXlQseB1_Bi1yE5kfyTLKxkwuaZ5OhJTOYw0Ng1bO8x48l5-JS1xSSETKeFag5w6VjYLF5CL8JisF3M3ycHcce0c-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایران کاملاً فروپاشیده !!!
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21436" target="_blank">📅 16:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21435">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBn-PIWbkM0WmdJjj0nQHdHJ3_HNb0prDauwnPh30BtayYuoFEcjtBdBC-nldQCYqxSTEUNXSD2iTiLO4nJNbz-uESjkehoePj0Oi5XbXyxNPZkhROYbVj1TdY3v6v4fcxxaua1-_0XXuJkm5fdmviRTZjA5fGP5ChLZW7_8PXl__hcu_vJUUGR4o1kIWkVxs0mQEc8HJ2Vbgc4HdtiPQgZHNV4VIOQ9_sF0AHBcDaWAlIq4vWP8LQDzanv-8kjhzCjbKHldCtu_QS3WqBstFnvt8TMtvITxZG5opzTZ-reHXvj_Vy6GW-hzRDnUxm-WEnM-AtrK8XoR4K8MIyaQxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتی ایران بالاترین رشد اقتصادی جهان رو داشت روزنامه‌ها با دشمنی و حسودی مدام از «ثروتمندترین کودک دنیا که هیچ دوستی هم نداره ، جز سکش » مینوشتند٬ هزار بار با شاه مصاحبه میکردند که توضیح بده چرا و چطور انقدر رشد کرده مملکت...
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21435" target="_blank">📅 15:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21434">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ در تروث :از قول ممباقر ،رئیس مجلس ایران: «ما گرسنه‌ایم، نمی‌توانیم زنده بمانیم»نیوزمکس @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21434" target="_blank">📅 15:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21433">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اورشلیم پست : همه نشانه‌ها به پایان رژیم در تهران اشاره دارند و شاهزاده رضا پهلوی فرد مناسبی برای به دست گرفتن مسئولیت آینده ایران است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21433" target="_blank">📅 15:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21432">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yj97ymMRjon0aD6UwIsWN-uWngOVkNjwNXrkNJTkX98gjwU3-3hzG1LzpajndeakNzRJdS4UUo8dNLtGZ1aZDcmcFMmHatYZrPkKCx6KsbZCSL_XOZuEzm2M5k4buAaIY-wGyuGbfIQiP7zQ2_1W1UhI7fKOe9FCwccNQZYH4XUX3lITxtV4GIsmjrQpLYRJgaWYqx_FKDO9j8_etPgQLD0aqKh17DL3rcOANWCPXTrO_B6YLtBNplm_kc64UeCQF8wA2j4pEEevD7hvYskmPmM9-X8ikkwj7wD9t3LTtdkSQ92ljHQXLJ4yRTVJ_6W39mkiJxnGcUrLhbGkuVgBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه اول روزنامه نیویورک پست امروز:
تنگه ترسیده ، رژیم ایران زیر فشار در حال فروپاشی است، زیرا ایالات متحده حلقه محاصره را تنگ‌تر می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21432" target="_blank">📅 14:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21431">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ارتش اسرائیل، دو تروریست از سازمان تروریستی حماس را که در حمله 7 اکتبر وارد خاک اسرائیل شده بودند، به هلاکت رساند
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21431" target="_blank">📅 14:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21430">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۸ کیلومتری زمین، پل‌ سفید مازندران را لرزاند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21430" target="_blank">📅 14:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21429">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUo6GJK6bDi8MyXmESylIXLZ3bkkXqeg7w0WBPjLWe5QPLEAv9GPJ4zsuspm9DHmtCyuY8JsgBhtgR-LIJ1tk1GsD3_UVv1NJWYulyU5km_7PhOVEjDkTYooiW0MRoOPGx4rHbd84WMN5odHuRdbsXbY4pw-8Y28V8Px56hbWbAXiuOqswfgqNvSTxEOBfjE7p9MJ5w1HF32lcV8yy5A_c8uiwiu-m9nHNsaqd04fpDqMfyDPYdL2_AuwNQvw42l5QbAN7gzxDIi5U2uS7SY5L-ddi3pIPNi5CtLLKyEl1Afkk0wnHUSI6jTR0LwGTPpu7203uye3e0Z40oU1ck_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب افکن مخوف B1-B از پایگاه فیرفورد انگلستان بلند شده و در حال تمرین است
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21429" target="_blank">📅 13:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21428">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g14Bq21TKj7nBnIKbcEgzoryhUm9m6MZUpTCHDUEpGLWt_86l_0hzuWSxSwPJG1AE8du46RGBYyLv57io1V_G8NXSeqprZsZBdq4_XbAlxVOmYuv9VM3KHUE_lUf4vJ0EF9kWetuZPJyU83bDgeUvWD5n34d5ZLSDCKtiKLsHSAk33BEu6t4YlV4vU88oq2L03MEXkirHYExLYxk94c0erAVHjdZdqfNFGp2IibClqQA99wu3WvQ_xspO3BJDqE1TpdPZQ_fnR6LKBnrnRf2ZsVpwHSs4aqkfnkCpTHkc-EhRFdaSaB_Vi1fSXgvOxR7bl1iPuYBfiRivg_SNC634A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند
E-11A BACN
نیروی هوایی آمریکا پس از چند هفته غیبت دوباره بر فراز عراق مشاهده شده است. این هواپیما یک
گره ارتباطی پرنده
است که شبکه‌ها و سامانه‌های ارتباطی مختلف نیروهای هوایی و زمینی را به هم متصل کرده و امکان تبادل صوت، تصویر و داده را حتی فراتر از خط دید فراهم می‌کند؛ در نتیجه جنگنده‌ها، پهپادها، نیروهای زمینی و مراکز فرماندهی می‌توانند اطلاعات میدان نبرد را سریع‌تر و هماهنگ‌تر به اشتراک بگذارند. بازگشت E-11A به آسمان عراق از نظر نظامی قابل توجه است، زیرا حضور آن می‌تواند به حفظ ارتباطات و شبکه فرماندهی در عملیات‌های گسترده کمک کند
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21428" target="_blank">📅 12:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21427">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک حمله مسلحانه توسط عناصر در شهر زاهدان، واقع در جنوب شرقی ایران؛ بر اساس گزارش‌های اولیه، یک مأمور کشته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21427" target="_blank">📅 12:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21426">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نرخ دلار ۲۰۱،۶۰۰ تومان (رکورد تاریخی)  دلار کف بازار  ۲۰۵-۲۱۰ هزار تومان تتر  ۱۹۹،۹۹۰ تومان(رکورد تاریخی)  بیتکوین ۷۷،۳۷۹ $ انس جهانی طلا ۴.۶۳۶ $ نفت برنت ۹۱.۰۲$ @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21426" target="_blank">📅 12:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21424">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3_GrieD-AgP8ir0-sTq_XDxZx95ruNq53VxKM2-hrqxOOFXKBy4tA0-L9N1I_yX71SNxdoB_Y3tRTO6hVElYayz31NyTIuEQjrVRm59hauN6y37An4mWER8kFiKBrvG5TQFizOFNo6KsIQ-NRyY5KaoRsTuFvWnkoL7y2F4mkXfQkitGRpKbnO1v1nv-6aTH2mev7hpkBKqB1xB1POH8uQIYV5qkU0ZJCaUxWpUynLFMeRW4vexP1bWVnPyQUs07rG3vjbSng6yyLfL7NOK09PtrmePHNYH08Uzck-afuxGETqtutdtHrwd-gT01BpBKBO7o22gpn_Xf5npRugaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcMaVJsogQyRIy2Jgfy-ZVm6thbx_G0L1Vw4VUj9EmF5RaUOuonptIPQcrjEH3Imr4TbQAIVpnG5NjS2g9TjuG0Lw_yNgJlZqLBRKYDrNAe-BKjsGo-EyTcaL1qb5ynK34ti5gMaLilwz7xciXwIXoYrOsEwtIoCZctkF-UCTnz4gDaj6Mk9xjond6EtTq0iZnzxiY32zDI9PX3xwq1-whunCUcBoFWrZh3WpNIYYcvqTFKnRXs0Dfik6Wa_asgEngqZBeFFEV-YHcTj_H5OW8pssVMw25jJK5bG7vOnA7xXQGfBj7K0qN7LPpF68yd-C1fHu2-5X0aw8vozjHC0Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش انفجار شدید در ارومیه ، شدت انفجار در خانه را پرتاب کرده
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21424" target="_blank">📅 12:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21423">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الجزیره به نقل از رویترز: فرمانده ارتش پاکستان پیش از سفرش به تهران، با ترامپ تماس تلفنی برقرار کرده بود
@WarRoom
خبر رویترز که سفر کنسل
شده
فیک نیوزه ، خودتون اینترنت دارین چک کنید قبلش نفرستید برام</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21423" target="_blank">📅 12:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21421">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نرخ دلار ۲۰۲،۶۰۰ تومان (رکورد تاریخی)
دلار کف بازار  ۲۰۵-۲۱۰ هزار تومان
تتر ۲۰۱،۵۰۰ تومان(رکورد تاریخی)
بیتکوین ۷۷،۱۲۴ $
انس جهانی طلا ۴،۶۳۰ $
نفت برنت ۹۱.۴۲$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21421" target="_blank">📅 12:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21420">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC0S-HnVL-EpkK7WFZcMZxtC1jSY7YfspQmlx4e3zADFFLGtLy95XA1UD5kM9vDf_AvFCdIgKFaKQQF32QJ-95YAzwpYFkda351_zDp1bCCvrN4OPv8KOeDLoAi0w--7UErf0Es5z3QCS7Qf2rwibMa-fqnhphLU3kTneSefW4cCcBZD2S767Mnb_JzytFt9JOeK7pC8UjGUirlBuNot8c65l_OWWEA55G_2GJ7dyCllCXBY7fcQ6kRC1ZZyLxzwQXdgls-nbtIu0XDgRzns_lcuW1L1Dp9F_Ioxh32lcgd9AM-gN4VWhVO73bDzneHm6d5aL4wfNj5Wq1h_vdETcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم منیر به تهران رسید
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21420" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21419">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bExDlV4E9Hpihg57udsjYBmd7RVQr3xJvk6GPXbiS98XiLVewOqrZBHdi8_VlO2M5QtvdcxL0B2NradYwMRsdq1VEpMu0_iyaNWzkwkFpUWsArLk9oRzJUIzisbTz0SYi3pqnAVZDNTQIZUsyJNUpsOoaKNCaVEncDtnJXStfsVv8WXzgMsVkbnufnpAvtwtrpOcxPmMikhDX9ZL0kZsnMudVus1qMnGmguOY7IoKz3_8NwLrx4zaSLYuS17JmLQCn5ez0zi3jZ8zxYJuAA3Qp3TW68s17kgH0R36OHla25_eDk-8Ea90eH4C_b_lVBH6a8wTOhvOhJlb6dMLnxfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی : ما از قدیم شطرنج باز بودیم، در سالای اخیر پوکر باز هم شدیم، الان هم مدتیه که ترکیبی بازی می‌ کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21419" target="_blank">📅 11:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21418">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqg0mzKGWqKoEc7yLe0ynFPaaa7to1AxW69sVgiyXHCOASmX0dKAwFqEX4GRk7qKGthPXRnLmwQIgMBCu6CCPm-ZlrqkxpzZO9QU7rIsYezxM2J-aUesNV7ZanvmdHbrY0fXraKk_-S9b4oZ0dmqMN8ACIYwXpt_LwFLVd9hbPPDRzBKx8r7tWpflGeUC7g8Q5lVyRqpkj-QpQdluzOqJjLjiw5LlwczrComq7PaqLB8skd-50LMkoTA4Gf_b1yaOURBzsAy0wVq3dcUANKyy4bx5byASw-mefATQbvJ2vs9ltwaV6ELacNLjKjXg-C-BYcJYIPnwC-dQdYHVfWu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریای بریتانیا: گزارشی از حادثه‌ای در ۶۳ مایل دریایی غرب ینبع، عربستان سعودی دریافت کرده است.
مسئول امنیتی شرکت گزارش داد که یک تانکر توسط یک پرتابه ناشناخته مورد اصابت قرار گرفته و باعث آتش‌سوزی در عرشه اصلی کشتی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21418" target="_blank">📅 11:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21417">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نرخ دلار ۲۰۱،۶۰۰ تومان (رکورد تاریخی)
دلار کف بازار  ۲۰۵-۲۱۰ هزار تومان
تتر  ۱۹۹،۹۹۰ تومان(رکورد تاریخی)
بیتکوین ۷۷،۳۷۹ $
انس جهانی طلا ۴.۶۳۶ $
نفت برنت ۹۱.۰۲$
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21417" target="_blank">📅 11:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21416">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9bbfIz319v4uAGUvAF6hH3bB6-GWHofQtTp1SrqElyr4b7XKbcGYopAPPHOKo3JySFrklEh94Heg-2F68NaSdFMmSI8yU9W3Eaz9XvS8wzsfm4WwOy1qnAWH2V81d6lefv-CZbkWLGfa3prjWbfqdssAXLVbqlphtHv87wuTt73Icjilje83m5tK90_336mshuMTrctvUwwpsx7c0d0a4PgNongaHCWV4C0F9E3Qk_ISPsdTPuHIebzKkkjOMchDTj8DjqtNpjppmuvT_C1cRPeyD-xGvLe9twULFHiCsWpKRdkK4a12Yi4vq4yIjR68dm0wtuIl7wuOrrMcFI_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21416" target="_blank">📅 09:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21415">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فایننشال تایمز: اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد واشنگتن وارد «مرحله پایانی» علیه ایران شده
و در حال آماده‌سازی گسترده‌ترین تحریم‌ها برای قطع باقی‌مانده ارتباطات مالی و تجاری تهران است. او هشدار داد کشورها و شرکت‌هایی که به حمایت اقتصادی از ایران ادامه دهند نیز ممکن است هدف تحریم‌های آمریکا قرار گیرند؛ اقدامی که هدف آن انزوای کامل اقتصادی و تشدید فشار بر جمهوری اسلامی است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21415" target="_blank">📅 09:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21414">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82cd04aaff.mp4?token=h9CfUvfztZMKJBJMQ4w3A0QYT38mpbduB0uqmDy_DHWAJPUvMofqRfTMz9maC9J9A7CZsyQCPiSCqoNNd_7crxGrMLjY0wBPcviNWEOu7D65RuXf-4ET-yCUpJXpRn6ghybAU38P3aqEkDesPS0juVqtPzmY73-d8s-sXOO5h07CjozGIBY9SyP1D1RZoro1HWva8XI1J0YKpCrKNhwVlvYWrPHVmym98s7FoT9edAcFVRkxNIgDAVUePiHggIJ8afbXm0vUr593pFezucWyvII_BqbMS-ITg0lO7GKThRPJKX_Q1OwVyzuJcyBI1ogKLSEEgKFPRAoZSx0F-t9SMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82cd04aaff.mp4?token=h9CfUvfztZMKJBJMQ4w3A0QYT38mpbduB0uqmDy_DHWAJPUvMofqRfTMz9maC9J9A7CZsyQCPiSCqoNNd_7crxGrMLjY0wBPcviNWEOu7D65RuXf-4ET-yCUpJXpRn6ghybAU38P3aqEkDesPS0juVqtPzmY73-d8s-sXOO5h07CjozGIBY9SyP1D1RZoro1HWva8XI1J0YKpCrKNhwVlvYWrPHVmym98s7FoT9edAcFVRkxNIgDAVUePiHggIJ8afbXm0vUr593pFezucWyvII_BqbMS-ITg0lO7GKThRPJKX_Q1OwVyzuJcyBI1ogKLSEEgKFPRAoZSx0F-t9SMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن کج بند رضایی : مردم خودشون در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه باید بکنند. @WarRoom یاشار : یعنی‌کوکتل مولوتوف درست کنند ؟
😂
😂</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21414" target="_blank">📅 09:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21413">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNskO09tF02Gx-6sHW_0kQfU6TiKlqTM37yGEgiTiEG-IqYem2v2b_HKqfGLXa7I1wr-SvrSvAmTaoODuYBvggpclh1eGv6NQf747uyDpS5P3fTqFJzdJas2IA9D9mlt5SEpHBGrvQJDZG6HZBzwLmbH2quGz01GOxX5t-kFbrLqSgKr1AYGeRD9VftcRAFQqPjzKPL6iGbPw3GOnPeVqnVMQxqR4RTcnQAd8TJ42femRX9bsts9MKm-zLiXBYORZ76y5tL_LC28FqyRdFeqZ7tb0BaToWDlcEhzS7eTwzRAYsIaDRGDQRTW337b3gmUO7OX6ZGnk9KQ8HgA04bZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :از قول ممباقر ،رئیس مجلس ایران: «ما گرسنه‌ایم، نمی‌توانیم زنده بمانیم»نیوزمکس
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21413" target="_blank">📅 09:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21412">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281df71e3f.mp4?token=ed6ZaATMekwMgoFj-VnjUMdnuTl1zadjtswExOg_v1QAmHuc7y2Y_F80FAMNYDTkyCAZ24kGN--gSPF2LafsQKO6emC14shnTCvYT8IQGL1_AYgd_7SatNOLl352l6KIroucRHrujaxEI1v5b9VoWKojU5zE8htQRMRpF36jv_VwIYd1cxFPyL7MWcLaSC8lPQz4M98kszazdxdjo1GecbDLYBGvrV3WNgBeQage09v9zp_6rx6Ov7VEnvT813A4pdjbOQW0zkiJIKfDGC_SHveEE6XiGxP2Ktbaz8aqeZGGVIhs3sGUWCt4dQOnkdA8AUUBC7XUArHssvdW4ZrRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281df71e3f.mp4?token=ed6ZaATMekwMgoFj-VnjUMdnuTl1zadjtswExOg_v1QAmHuc7y2Y_F80FAMNYDTkyCAZ24kGN--gSPF2LafsQKO6emC14shnTCvYT8IQGL1_AYgd_7SatNOLl352l6KIroucRHrujaxEI1v5b9VoWKojU5zE8htQRMRpF36jv_VwIYd1cxFPyL7MWcLaSC8lPQz4M98kszazdxdjo1GecbDLYBGvrV3WNgBeQage09v9zp_6rx6Ov7VEnvT813A4pdjbOQW0zkiJIKfDGC_SHveEE6XiGxP2Ktbaz8aqeZGGVIhs3sGUWCt4dQOnkdA8AUUBC7XUArHssvdW4ZrRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر ایران به سلاح هسته‌ای دست پیدا می‌کرد، فکر می‌کنم تمام خاورمیانه از بین می‌رفت و قطعاً اسرائیل نابود می‌شد. آنها به من می‌گویند اگر دونالد ترامپ رئیس‌جمهور نبود، دیگر اسرائیلی وجود نداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21412" target="_blank">📅 08:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21411">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">روزنامه یونانی کاتیمرینی گزارش داده که آتن پس از تهدیدهای تهران علیه پایگاه‌های آمریکا در اروپا یک سامانه پدافند هوایی Patriot را از کارپاتوس به جزیره کرت منتقل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21411" target="_blank">📅 08:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21410">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏نیویورک پست با استناد به تصاویر ماهواره‌ای نوشت: فعالیت در قطب صادرات نفت ایران در جزیره خارک تقریبا صفر است.
‏داده‌های کشتیرانی نشان داد که روزهای شنبه و یکشنبه ۱۷ کشتی از تنگه هرمز عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21410" target="_blank">📅 08:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21409">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏خبرگزاری مهر: آتش‌سوزی گسترده در چندین سوله یک کارخانه تولید چسب و عایق در فرون‌آباد پاکدشت، بامداد دوشنبه به وقوع پیوست و به‌دلیل وجود مواد قابل اشتعال، عملیات مهار حریق با دشواری همراه شد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21409" target="_blank">📅 08:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21408">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش های‌ زیاد از صدای انفجار بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21408" target="_blank">📅 23:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21407">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مایک پنس: ترامپ و اسرائیل دوباره برای «تمام کردن کار» وارد عمل می‌شوند
به گزارش سی‌ان‌ان : مایک پنس، معاون سابق رئیس‌جمهور آمریکا مدعی است:
«بسیار زود و پیش از آنکه دیر شود زمانش فرا می‌رسد که رئیس‌جمهور و متحد ما اسرائیل مجبور شوند وارد شوند و کار را تمام کنند.»
آمریکا باید نیروها و تجهیزات نظامی خود را در منطقه حفظ کند تا برای اقدام احتمالی آینده آماده باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/21407" target="_blank">📅 23:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21406">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اناق جنگ با یاشار : این خلاصه از بهترین ویدیوها از ساعتی پیش که مسابقه شروع شد تا همین دقایقی پیش درست کردم که هیچ جا پیدا نمیکنید.
گرندپری «Freedom 250» در قلب واشنگتن و در مسیر اطراف نشنال مال برگزار می‌شود؛ مسابقه‌ای ۲۵۰ مایلی که نماد ۲۵۰ سالگی استقلال آمریکاست. ترامپ که با فرمان اجرایی زمینه برگزاری آن را فراهم کرد، پیش از آغاز مسابقه با خودرو ریاست‌جمهوری یک دور نمادین زد و پرچم سبز شروع را به اهتزاز درآورد. هم‌زمان، نمایش هوایی گسترده‌ای با حضور بمب‌افکن‌های راهبردی B-2، B-1B و B-52 برگزار شد تا قدرت نظامی آمریکا نیز بخشی از این نمایش ملی و میهن‌پرستانه باشد. هم اکنون ترامپ از جایگاه ویژه در حال مشاهده مسابقه می باشد. البته بیشتر در حال صحبت کردن با اطرافیان است تا این لحظه…
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/21406" target="_blank">📅 22:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21405">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جمهوری اسلامی اعلام کرد از امشب هر نفتکشی از مسیر جنوبی تنگه ی هرمز(متعلق به عمان و آمریکا) عبور کنه جریمه میشه و یا خود کشتی توقیف میشه و یا اموال کشتی مصادره میشه.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21405" target="_blank">📅 22:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21404">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شاهزاده رضا پهلوی: قیمت دلار امروز از مرز ۲۰۰ هزار تومان گذشت. امروز قیمت دلار ۲۸٬۵۷۱ برابر زمانی است که جمهوری اسلامی به قدرت رسید. حاصل نزدیک به پنج دهه حاکمیت فساد و ناکارآمدی در جمهوری اسلامی، فقر، فساد و انزوا برای ملت ایران بوده است. تجربه این پنج دهه یک مسئله را برای همه روشن کرده است: در جمهوری اسلامی اصلاح ممکن نیست. قطار ایران در بهمن ۵۷ از ریل تمدن و پیشرفت خارج شد و امروز جمهوری اسلامی آن را با سرعت هرچه بیشتر به ته دره هدایت می‌کند. امروز وظیفه تک‌تک ایرانیان، از جمله کارمندان دولت و بدنه اداری کشور، این است که به هر شکل ممکن با اخلال در فعالیت‌های مخرب جمهوری اسلامی و تضعیف آن، زمینه برکنار کردن رژیم و نجات ایران را فراهم کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21404" target="_blank">📅 22:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21403">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مایک جانسون، رئیس مجلس نمایندگان آمریکا، به فاکس‌نیوز گفت آمریکا در حال ورود به مرحله جدیدی از جنگ علیه ایران است و دولت ترامپ همچنان به‌دنبال پایان دادن به جنگ است.
او گفت تمرکز مرحله بعدی بر
فشار اقتصادی و تحریم‌های شدیدتر
خواهد بود و دولت آمریکا می‌خواهد با افزایش فشار، تهران را به پذیرش یک تسلیم وادار کند. جانسون همچنین گفت ترامپ «شبانه‌روز» برای حل‌وفصل جنگ تلاش می‌کند. این اظهارات هم‌زمان با اعلام اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره اعمال
«سخت‌ترین تحریم‌های تاریخ» علیه ایران
مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21403" target="_blank">📅 21:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21402">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d23c54da.mp4?token=pbL0fgKM4A39lsLhAGicGI1IDEcNI4vBqSBLTo3IdaXHIShRsgRFamBm3ivzvRV-CkN8UGVxXzJUhNtdvJpBQfOW3nYWC-NWsNyx7QT3RbeIXjdHSgpn9uV_b2qEhjokVEi87hYVP593RSiZUgMCcrFFPY9cIcOJEHk0syZY_7-YSYSPDWM7mjAczggGlDZenZCHvJZ3Z3g-pKG9opNML0ii36IfrCxw_VIcmhMvRaOAJpOHPpezVBuFSCOKxyGCUEGSTtgwRJ-GaBaQXrA8HTgDT4Uv7TLfBieBieFFc-_GMnbXb65cOJU8M3pWpXMkho1-wykPlJOjQWBRVU0lIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d23c54da.mp4?token=pbL0fgKM4A39lsLhAGicGI1IDEcNI4vBqSBLTo3IdaXHIShRsgRFamBm3ivzvRV-CkN8UGVxXzJUhNtdvJpBQfOW3nYWC-NWsNyx7QT3RbeIXjdHSgpn9uV_b2qEhjokVEi87hYVP593RSiZUgMCcrFFPY9cIcOJEHk0syZY_7-YSYSPDWM7mjAczggGlDZenZCHvJZ3Z3g-pKG9opNML0ii36IfrCxw_VIcmhMvRaOAJpOHPpezVBuFSCOKxyGCUEGSTtgwRJ-GaBaQXrA8HTgDT4Uv7TLfBieBieFFc-_GMnbXb65cOJU8M3pWpXMkho1-wykPlJOjQWBRVU0lIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : از زمان ازسرگیری محاصره دریایی علیه ایران، مسیر ۷۰ کشتی تغییر داده شده و فعالیت ۳ کشتی دیگر نیز متوقف شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21402" target="_blank">📅 21:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21401">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">واشنگتن پست : تعداد مجروحان آمریکایی در جنگ با ایران به 774 نفر افزایش یافته است. این آمار شامل 18 کشته و 756 مجروح است. طبق داده‌های وزارت دفاع آمریکا، حدود 60 مورد جدید از جراحات در روزهای اخیر ثبت شده است، که شامل آسیب‌های جدی مغزی ناشی از انفجارها در حملاتی است که پایگاه‌های آمریکایی در منطقه را هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21401" target="_blank">📅 20:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21400">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو: ما به شرایط قبل از ۷ اکتبر باز نخواهیم گشت و اجازه نخواهیم داد هیچ گروهی در غزه به شهرها و مناطق اسرائیلی تهدید کند یا امنیت را تضعیف نماید.اگر حماس فوراً از پرتاب بالن‌ها و برگزاری تظاهرات‌ها خودداری نکند، هدف قرار دادن مسئولان این اقدامات را تشدید خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21400" target="_blank">📅 20:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21399">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سخنگوی دولت : خبر خوش برای مردم، سود سهام عدالت (۲-۳ دلار) از 2 تا 8 شهریور واریز میشه
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21399" target="_blank">📅 20:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21398">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اورشلیم پست گزارش داده است که اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه ۲۴ اوت در یک نشست خبری جزئیات برنامه جدید دولت ترامپ برای تشدید فشار اقتصادی بر ایران را اعلام کند. این نشست ساعت ۲ بعدازظهر به وقت شرق آمریکا برگزار می‌شود که با توجه به…</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21398" target="_blank">📅 19:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اکسیوس: وزیر خارجه سوریه، اسعد شیبانی، امروز یکشنبه با رئیس سازمان اطلاعاتی اسرائیل (موساد)، یوآو گالفمن، دیدار کرد تا تلاش‌هایی برای کاهش تنش بین دو کشور صورت گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21395" target="_blank">📅 19:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21394" target="_blank">📅 19:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21393">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21393" target="_blank">📅 19:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بی بی نتانیاهو الان این شماره رو گذاشته  مردم زنگ بزنند اگه عبری بلدید صدای مردم ایران باشید
+972544700047
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21392" target="_blank">📅 18:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60dddfa42.mp4?token=aTQmZN2eec2GlWl4L9slFBqAzA8AQFaJBSG3JKn49-vZxld00XQFwPno8AH0MjpLD-Iuu6a2DLZwAlystWVe6fg1wNeXLkcpLJJh4MCeSlQpTZouKx6zvd5KQkMXGHJhtnB1cAsvxeJCDeDAZjrCUL1MCmMIeJNoGwiUbKS4OxZgU3KwpLoKlcPXVpPfDqyhxZ6vUV9u58esh8VdGwMQr9wXSWuQovQMV8eugnDLf7mOk0x1yLkSsyMaE6NsY3Mh_-4lbgF0rAsvxTuHb1Bxehl73XE82pyaufkFqpJx7I3cRnM9IUBYZ3nCMkVv8gHNsDW9jT4pGWlQFOwebri355AjBfFZlqvTD5spfDQcT2BfntUemvRFVqEcqm8E5esSFv3heA1e6ZjqcdNwM-NrhUurX6OInW1qGXBE28MSOuMmDbLtoEG-g5i8JH9G8DGo4Rw905oXWcmDtyA8oj50q7Be11YtHSy08V7aen6v4pb2wCwljK1-upXw4tyyXvEdf25mCUs6duXep-vJF1nTn-Or273Rj0ozfa2YPgQHtJ73_0OrF2aVLwkTGmxRQVJ2uE3rnXBPCHOdBs4V_U6eDSkBjfvnvcP_GvDs6rduFzidGo0z3bvHh3gNofdrcOvPF3FqniOgiFD1tX9716561b1C98PXbH0B77WX0Hw4TZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60dddfa42.mp4?token=aTQmZN2eec2GlWl4L9slFBqAzA8AQFaJBSG3JKn49-vZxld00XQFwPno8AH0MjpLD-Iuu6a2DLZwAlystWVe6fg1wNeXLkcpLJJh4MCeSlQpTZouKx6zvd5KQkMXGHJhtnB1cAsvxeJCDeDAZjrCUL1MCmMIeJNoGwiUbKS4OxZgU3KwpLoKlcPXVpPfDqyhxZ6vUV9u58esh8VdGwMQr9wXSWuQovQMV8eugnDLf7mOk0x1yLkSsyMaE6NsY3Mh_-4lbgF0rAsvxTuHb1Bxehl73XE82pyaufkFqpJx7I3cRnM9IUBYZ3nCMkVv8gHNsDW9jT4pGWlQFOwebri355AjBfFZlqvTD5spfDQcT2BfntUemvRFVqEcqm8E5esSFv3heA1e6ZjqcdNwM-NrhUurX6OInW1qGXBE28MSOuMmDbLtoEG-g5i8JH9G8DGo4Rw905oXWcmDtyA8oj50q7Be11YtHSy08V7aen6v4pb2wCwljK1-upXw4tyyXvEdf25mCUs6duXep-vJF1nTn-Or273Rj0ozfa2YPgQHtJ73_0OrF2aVLwkTGmxRQVJ2uE3rnXBPCHOdBs4V_U6eDSkBjfvnvcP_GvDs6rduFzidGo0z3bvHh3gNofdrcOvPF3FqniOgiFD1tX9716561b1C98PXbH0B77WX0Hw4TZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جنگ اخیر کی بیشترین پول رو در آورد ؟!
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21390" target="_blank">📅 18:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کمیسیون امنیت ملی جمهوری اسلامی:
دریافت هزینه خدمات از کشتی‌های عبوری از تنگه هرمز تصویب شد‌.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21389" target="_blank">📅 18:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a2f95843.mp4?token=EIFnHOEX4_s58c5uVtkSKrB6IbN-qaavPXjaWGA1ndCeo0w-f4YV978LFLFvx_SeK6IVIpfQ1opFZQzAWO3Gq8qtoOAD73vjb_zx1q1vyqIi8q9dkVbX1w5r47HsCDvRe3IdgeFRum7S-NHC3JUIKWO4e6Es6teQmMJ7EtWj3bZBv5Mf8hosEzpepp1lOtG6cGDIRTizEHDJv2g0zq1-QKtTHEPLuUQnQoB63f8fqcXGahWs9awpZMsXKPFJN9-_PmI59ElAJjymCJdr0wOw2yqFkLdmfL3ibAxTy08Y2Ie4MS6YYCy96MCuWydFud7RTn2I1fWwiNeXFF5iQaAkOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a2f95843.mp4?token=EIFnHOEX4_s58c5uVtkSKrB6IbN-qaavPXjaWGA1ndCeo0w-f4YV978LFLFvx_SeK6IVIpfQ1opFZQzAWO3Gq8qtoOAD73vjb_zx1q1vyqIi8q9dkVbX1w5r47HsCDvRe3IdgeFRum7S-NHC3JUIKWO4e6Es6teQmMJ7EtWj3bZBv5Mf8hosEzpepp1lOtG6cGDIRTizEHDJv2g0zq1-QKtTHEPLuUQnQoB63f8fqcXGahWs9awpZMsXKPFJN9-_PmI59ElAJjymCJdr0wOw2yqFkLdmfL3ibAxTy08Y2Ie4MS6YYCy96MCuWydFud7RTn2I1fWwiNeXFF5iQaAkOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زامبی ؟ بدترشه ، نسل ۵۷
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21388" target="_blank">📅 17:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21387">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بنیامین نتانیاهو:
«پهپادهای کوچک می‌توانند بسیار مرگبار و دقیق باشند و به‌سختی دیده شوند. ما سال‌هاست روی مقابله با این تهدید کار می‌کنیم و آن را در اوکراین، لبنان و ایران دیده‌ایم. حالا تلاش می‌کنند این تهدید را دوباره احیا کرده و وارد غزه کنند. دستور من به دستگاه امنیتی و ارتش اسرائیل این است که
خود پهپاد، اپراتور آن و محل شلیک یا پرتابش را هدف قرار دهند و هر کاری لازم است برای محافظت از شهروندان اسرائیلی انجام دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21387" target="_blank">📅 17:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21386">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">میدل ایست آی: ده‌ها پایگاه اروپایی در جریان جنگ ۴۰روزه از عملیات آمریکا علیه ایران پشتیبانی کردند؛ بریتانیا احتمالاً مهم‌ترین حمایت را ارائه داد و پایگاه‌ها و زیرساخت‌های نظامی آن، از جمله دیه‌گو گارسیا، در پشتیبانی از عملیات آمریکا مورد استفاده قرار گرفتند. فرانسه نیز به هواپیماهای نظامی پشتیبانی آمریکا اجازه فرود و استفاده از پایگاه‌های خود را داد. بلغارستان هم اجازه استفاده آمریکا از فرودگاه‌ها و خاک خود را صادر کرد و به این ترتیب، با وجود مواضع متفاوت برخی دولت‌های اروپایی در قبال جنگ، زیرساخت‌های نظامی کشورهای مختلف اروپا در پشتیبانی از عملیات آمریکا علیه ایران نقش داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21386" target="_blank">📅 16:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21385">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیویورک پست
: در هفته گذشته حدود 200 کشتی چراغ خاموش از تنگه هرمز عبور کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21385" target="_blank">📅 15:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21384">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دیجیکالا از دسترس خارج شد تا بعدن بتونه گرونتر بفروشه
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21384" target="_blank">📅 15:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21383">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">یاشار داش دلار تو بازار من الان 210 چنج کردم</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21383" target="_blank">📅 15:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21382">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏دونالد ترامپ در‌تروث با انتشار ویدیویی جنجالی از سخنرانی خود، به انتقاد شدید از تلاش‌های حزب دمکرات برای محدود کردن اختیارات نظامی رئیس‌جمهور آمریکا پرداخت.
‏او در این اظهارات طعنه‌آمیز گفت : اگر علی خامنه‌ای در حملات کشته نمی‌شد، دمکرات‌ها احتمالاً او را برای ریاست‌جمهوری سال ۲۰۲۸، سنای میشیگان یا حتی مدیریت کمیته ملی دمکرات‌ها (DNC) نامزد می‌کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21382" target="_blank">📅 14:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21381">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حمله هوایی اسرائیل به غزه
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21381" target="_blank">📅 14:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21380">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دلار کف فردوسی ۲۰۱،۰۰۰ تومان
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21380" target="_blank">📅 14:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21379">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دلار ۱۹۹.۰۰۰ تومان (رکورد تاریخی)  تتر  ۱۹۷.۰۰۰ تومان (رکورد تاریخی)  بیتکوین ۷۶.۶۱۶ $ انس جهانی طلا ۴.۶۰۲ $ (آخرین قیمت) نفت برنت ۹۳.۹۹$ (آخرین قیمت) @WarRoom ساعت ۱:۳۰ دقیقه تهران</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21379" target="_blank">📅 14:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21378">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دلار ۱۹۹.۰۰۰ تومان (رکورد تاریخی)
تتر  ۱۹۷.۰۰۰ تومان (رکورد تاریخی)
بیتکوین ۷۶.۶۱۶ $
انس جهانی طلا ۴.۶۰۲ $ (آخرین قیمت)
نفت برنت ۹۳.۹۹$ (آخرین قیمت)
@WarRoom
ساعت ۱:۳۰ دقیقه تهران</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21378" target="_blank">📅 13:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21377">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حبس مهریه بالای ۱۴ سکه حذف می شود
نماینده نجف‌آباد در مجلس اعلام کرده طرح اصلاح نحوه اجرای محکومیت‌های مالی در صحن علنی تصویب شده و بر اساس آن، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف می‌شود.
برای مهریه‌های زیر ۱۴ سکه نیز امکان اجرای حکم با استفاده از پابند الکترونیک پیش‌بینی شده است.
این مصوبه برای بررسی و تأیید نهایی به شورای نگهبان ارسال شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21377" target="_blank">📅 13:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21376">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رسانه های کره شمالی : دولت کره شمالی اعلام کرده است که قصد دارد توافق دفاعی با ایران امضا کند. در صورت نهایی شدن، این اقدام می‌تواند منجر به تعمیق همکاری‌های نظامی بین پیونگ‌یانگ و تهران شود. این توافق بالقوه در بحبوحه تنش‌های جاری بین ایران، ایالات متحده و اسرائیل مطرح شده
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21376" target="_blank">📅 13:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21375">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">صداوسیما در اقدامی ، اطلاعات به ادعای آنها محرمانه و مکان‌های دقیق تردد پسر ترامپ و نقاطی که در تیررس است را منتشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21375" target="_blank">📅 12:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21374">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بامداد امروز یک شهریور، کارخانه‌ نوشابه‌سازی ایرانشهر طی حادثه‌ای در آتش سوخت. هنوز از میزان خسارت‌های مالی اطلاعات دقیقی منتشر نشده است. مسئولین این واحد تولیدی در حال پیگیری این ماجرا هستند. @WarRoom عمو نوشینیاهو ، بی بی کولا</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21374" target="_blank">📅 12:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21373">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رسانه های عربی : ارتش اسرائیل (IDF) مدتی پیش به ساختمان‌های متعلق به گروه‌های تروریستی در روستای زوتر الشرقیه و حداتا در جنوب لبنان حمله کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21373" target="_blank">📅 12:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21372">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دلار ۱۹۶،۴۰۰ تومان (رکورد تاریخی)
دلار بازار آزاد ۲۰۰،۰۰۰ تومان
تتر  ۱۹۵.۳۶۰ تومان
بیتکوین ۷۶،۲۳۷ $
انس جهانی طلا ۴.۶۰۲ $ (آخرین قیمت)
نفت برنت ۹۳.۹۹$ (آخرین قیمت)
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21372" target="_blank">📅 11:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21370">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOo_gXBW-ba0pIR7F9ljWtaSm3NPQ1OUDq3eaP0iqIgbbumd2VrpbSNMb6pRIXehd5Y7NNIpI0rrl_u1OI8dy5Y5XalewJyrisYzcjMpZQyVsAgrHpjnCRVxsq6fTBreCoL4vfdRstu9RU-R3Jdv-CsvNg1ddzDhZc2uJInRtprXnIfZEwHnI9KWKXMiWlcwm8CVZIXrNNIjTZdeLshi_XhXplW5BUb-t1awJ1QeQYBuDNgDjMmxhCvKZe0oMLinWL-5opk_FiPBb3mv_Od6FlzOljCO6zEV253qyJEs-bWTD2u79fQDAa2Wl6z-UcNWnDuKKyChzebK3gT8-KrMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بامداد امروز یک شهریور، کارخانه‌ نوشابه‌سازی ایرانشهر طی حادثه‌ای در آتش سوخت.
هنوز از میزان خسارت‌های مالی اطلاعات دقیقی منتشر نشده است.
مسئولین این واحد تولیدی در حال پیگیری این ماجرا هستند.
@WarRoom
عمو نوشینیاهو ، بی بی کولا</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21370" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21369">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر امور خارجه سوریه:پیش‌بینی می‌کنم که به زودی مذاکرات با اسرائیل در مورد یک توافق امنیتی از سر گرفته شود. ما دست دوستی دراز می‌کنیم و از اسرائیل می‌خواهیم که از این فرصت تاریخی استفاده کند
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21369" target="_blank">📅 11:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21368">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">العربیه: فرمانده ارتش پاکستان، عاصم منیر، روز دوشنبه با پیام‌هایی از آمریکا به تهران سفر می‌کند.
این سفر در چارچوب تلاش‌های پاکستان برای شکستن بن‌بست دیپلماتیک ایران و آمریکا و از سرگیری مذاکرات پس از ناکامی دو طرف در دستیابی به توافق نهایی درباره پرونده هسته‌ای و تنگه هرمز انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21368" target="_blank">📅 11:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21367">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ4Y0mnqtr5W8Wlobn1m5dXl4QxrGg8hWiRCygl-uJTWQBAsSrWVrr_bAZn1O5EbVvt8BT9rvqnPjq0sWAyHnCyWUJRa_dUKaRRoCEqU0JnyGzP7AxCoAI6bDYyNsfbo2D_aLEU4EX4DUaLWuYdgkVLTo5MjQBxbXr1Ez-fTqvEQajmIduJ_rY6pjxNlCVdQ_0wvco4AvSgz9KXEbQwqNjEtL3d-SrObwj_Bh8ASv6vYqn57LweunaHaLD6BlGqH1VcgXXEWdRznUiqzx7fd2a1tppISKxLj0ezYz8-dlHfCTFM5fToM6yHnCXfWCm_dMd95xrcOW7D3cYdFg50wIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهده دایناسور در مناطق بیابانی خراسان رضوی تکذیب شد
دبیر شورای اطلاع رسانی اداره کل حفاظت محیط زیست خراسان رضوی
:
طی روزهای اخیر تصویری در شبکه‌های اجتماعی دست ‌به‌ دست می‌شود که موجودی شبیه دایناسور را در محیطی بیابانی در شهرستان بینالود نشان می‌دهد.
تصویر مذکور کاملاً مصنوعی، تولید شده توسط هوش مصنوعی و فاقد هرگونه واقعیت میدانی است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21367" target="_blank">📅 11:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21366">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">روزنامه تلگراف بریتانیا : هکرهای ایرانی یک حمله سایبری بی‌سابقه به یک نیروگاه در بریتانیا انجام دادند که منجر به از کار افتادن آن به مدت ۴ روز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21366" target="_blank">📅 11:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21365">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96ca1be3f.mp4?token=CD4jPW2uYUKH7VMdZlM2wB9RAZ3H6FYrXmWhA9stiUimzmuDi4ELtXAjDzPHZCH-hKFvK3IH1GPFEDlw4hzteA6ay4DXsuDH8Ul23283_IxAR1616hPs1IWnIm2c9IpwxEIzuf8hnNA6PiHVBRFQliuJl-15zNw6jxBtq5Sn633CslSgnf2Ak0gKssAPxQwInE1oHYIASZ3Qo1uUfHshNUdz70zGIwoaQSDhvUyZ62cKSoP3aYi6ufYcgAD3sP4_0vbwiEYoLtvLwP1Xy25dI4-JeBBYv87J6pwODKf8Myc54X6SPMsGj6IUNyiNp3mukDYge24YCnSSRZwKBTR7FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96ca1be3f.mp4?token=CD4jPW2uYUKH7VMdZlM2wB9RAZ3H6FYrXmWhA9stiUimzmuDi4ELtXAjDzPHZCH-hKFvK3IH1GPFEDlw4hzteA6ay4DXsuDH8Ul23283_IxAR1616hPs1IWnIm2c9IpwxEIzuf8hnNA6PiHVBRFQliuJl-15zNw6jxBtq5Sn633CslSgnf2Ak0gKssAPxQwInE1oHYIASZ3Qo1uUfHshNUdz70zGIwoaQSDhvUyZ62cKSoP3aYi6ufYcgAD3sP4_0vbwiEYoLtvLwP1Xy25dI4-JeBBYv87J6pwODKf8Myc54X6SPMsGj6IUNyiNp3mukDYge24YCnSSRZwKBTR7FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت من وقتی یه شب دیگه هم باز نزد !
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21365" target="_blank">📅 03:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21364">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLadan</strong></div>
<div class="tg-text">ترامپ فعلا داره با کانادا کل کل میکنه. توی کانادا همه از دستش کلافه شدن، دیوانه باعث شده وضع خراب بشه و همه چی گرون شده بیش از حد</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21364" target="_blank">📅 02:21 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
