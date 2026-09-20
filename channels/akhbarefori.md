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
<img src="https://cdn4.telesco.pe/file/gUkzXDvRQKSYAdTwVyn94PbukzFkyfYOnyG4B3Nms8L9ycX_4L241Igcs7NVU2qYxC0WwVLSLCAEXmupKppzVOVsA_2FUXfuAThYKx8wiEun4rKRRXgUbHgpxBhDPSybJETOzS6gGY3p4KJSyrKNSH0-MEqu4lS1mi_GnbqsXMKL10h5pte2pFj_1gUsSatDK0MtJMbCM5GXKiOxoJ5CHn8_DpAiC8eQ_FOn7Tpak-wW8tx1I_yjhmuCXZCdJ9WRLGGPitz2U_Tsm172xgFB0BJTG8FsQ9lc_3iLN471sWVF7XGNqXJ57wO7KHTU4XKzvd9YT3voqL1IRWuutB0OXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.04M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 13:49:48</div>
<hr>

<div class="tg-post" id="msg-691430">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای شبکه فاکس‌نیوز: در تأسیسات هسته‌ای طالقان فعالیت قابل‌ توجهی دیده می‌شود
🔹
شبکه فاکس‌نیوز با انتشار تصاویر ماهواره‌ای از تأسیسات هسته‌ای طالقان مدعی است فعالیت قابل‌توجهی در این محل دیده شده و یک سازه بتنی روی آن ساخته شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/691430" target="_blank">📅 13:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691429">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
۸
استان دارای بیشترین مدارس آسیب‌دیده در جنگ
رییس سازمان نوسازی مدارس کشور:
🔹
استان‌های هرمزگان، مرکزی و شهر خمین، آذربایجان شرقی، آذربایجان غربی، فارس، اصفهان، کردستان و کرمانشاه از جمله مناطقی بودند که بیشترین آسیب به مدارس در آن‌ها گزارش شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/691429" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691428">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سازمان تأمین اجتماعی: واریز حقوق شهریور ماه بازنشستگان از فردا آغاز می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/691428" target="_blank">📅 13:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691427">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJy_Pm5OTMlLtgeOIfsDHfBkxxlqei_r2_SQR1gNlNIOP2UrvsS4cksFUudTpO5N6zXA3DKlIVWn-NlDKby0gpKIpuW79eM_-o3UVUlUQAWATldscPuTUfq7ZR-ftynWWBYtFAAJObDu7V8OXcMSOdrfRwgU02k3zt2S-AJCOovuLb1q4MGRIMkruAyuEc26WJEmJrB04DZ2in_5nsthbOqnvxppbtrKmo8tOdeLRbEb593jxkr8_aE4YTijeBlpmC_l44yAItwEhAEodvCLeuMxa_55zFAsuiNl9KPv08_GTn4nAu8fInSOFAhzXGh2-bzrjvllngTd6szGtCtvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پک ویژه سوغات رضوی
یک هدیه معنوی و ماندگار از مشهد؛ ترکیبی از عطر، مهر، قاب‌فرش و تسبیح رضوی برای کسی که می‌خواهی یاد حرم را با خودش داشته باشد.
🤍
داخل این پک:
🌸
عطر گوهرشاد — ۸۵۰,۰۰۰ تومان
🕌
مهر تربت مشهد — ۱۸۵,۰۰۰ تومان
🖼
قاب‌فرش ۱۵×۱۵ — ۱۵۵,۰۰۰ تومان
📿
تسبیح رضوی — ۲۰۰,۰۰۰ تومان
جمع قیمت اصلی: ۱,۶۳۲,۰۰۰ تومان
🔥
قیمت ویژه پک: ۱,۳۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
قرار؛ تجلی هنر و ارادت
@ghararshop</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/691427" target="_blank">📅 13:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691426">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUPqGfRP4TzqGSilfr6Ft91mCiRkbNw3bVSuMFDakuJ9h6Bl-cwJjX30N-vTubcBRxl4kCI9Ev8AVDM4ej9zBMig449r6szm_UCFcfkUCcnwpy749kvW4tEbpr053kSv6cOUuRwET64bCfXPcKGG_v_qtIBOtfIYrYBsSQqNhAdpnOHhbw7ynP3KovPuqr8c542z5nFHnAkG67ZAOuMV1LaDWjl8SsZrEnWFYnYsDFPDH2HyJ3syqClkkilKXo63cVktSpChaDtu-InPXMN4YknUSK-44_Wr4d4FMA-AorrjYuAhYnbU2uN3T5CcPzmBh6QS-RWTk1aRAjBSws-ztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت اطلاعات: سه کانون عملیاتی وابسته به گروهک‌های تروریستی که قصد عملیات ترور و تخریب زیرساخت‌های اقتصادی را داشتند در ۳ استان ( کرمان، آذربایجان‌غربی و البرز) به هلاکت رسیده یا بازداشت شدند
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/691426" target="_blank">📅 13:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691425">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
وزارت اطلاعات: سه کانون عملیاتی وابسته به گروهک‌های تروریستی که قصد عملیات ترور و تخریب زیرساخت‌های اقتصادی را داشتند در ۳ استان ( کرمان، آذربایجان‌غربی و البرز) به هلاکت رسیده یا بازداشت شدند
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/691425" target="_blank">📅 13:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691424">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1048d146b.mp4?token=vUIQkYnJtZGzozQ9Fc9hLbOMuhWP-uQW8gRgr_sfwKHCwhdS8BrgfrgXMVKpg1TBXrEwez33J4Mt841Qr63GgQyGmIH0OUMEC73x5kF3I-Se8hYE1HkUOmMfTy02xyip_kS4A5sfgLHPGFlBuxrUPSJWpMTnQqiAgdrIga60bXkPSAuPi90DWcX5I6ZNIHF2UNPuWeeDd_H-kN6v2Vyc2wRS0x2PgAS0UwLWD_Su8tI-fS0snY6Sou0txAB80wsQOijFXdATFX-dXpVMD6s-I1gjRtEgPTl-TtZEXZ31wFMKcOK3BKTa948VtPYRNG1DOhVh2-9v_xoAWf0AhMjRfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1048d146b.mp4?token=vUIQkYnJtZGzozQ9Fc9hLbOMuhWP-uQW8gRgr_sfwKHCwhdS8BrgfrgXMVKpg1TBXrEwez33J4Mt841Qr63GgQyGmIH0OUMEC73x5kF3I-Se8hYE1HkUOmMfTy02xyip_kS4A5sfgLHPGFlBuxrUPSJWpMTnQqiAgdrIga60bXkPSAuPi90DWcX5I6ZNIHF2UNPuWeeDd_H-kN6v2Vyc2wRS0x2PgAS0UwLWD_Su8tI-fS0snY6Sou0txAB80wsQOijFXdATFX-dXpVMD6s-I1gjRtEgPTl-TtZEXZ31wFMKcOK3BKTa948VtPYRNG1DOhVh2-9v_xoAWf0AhMjRfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میکس‌های محبوب قهوه را بشناسید؛ هر
ترکیب، طعمی متفاوت
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/691424" target="_blank">📅 13:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691423">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
حاجی‌دلیگانی: طرح سه فوریتی خروج از NPT تقدیم هیات رئیسه مجلس شد
حاجی دلیگانی، نماینده مجلس:
🔹
با توجه به شرایطی که کشور دارد و تهاجمی که دشمن در ۲ مقطع به ما داشته، ماندن ما در NPT جز ضرر چیزی برای ما ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/691423" target="_blank">📅 13:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691421">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_L-vcuMkXyt2dZT52EuQsBbHxPOjpYBWfaBEKP2P74mirEn33UmMCBhfEtvCTXeOfee7r1rYtrXC6oYuYF2jMqDP_8f7P_knvB8lvsQL31EbGEAKSJnbozoYMZVVfpNIKrrlFjWInCqT8m20S3mXWtjO88z0uqEAkv2jNGVkdzAOqnGI_Zy-vogmq8_kvU-iaWzWFtenozIhIcKPpzIEX9NWgkcvdo-AnOfaK6eEy0Ib4p9ZeIcFfyRpi_s7ZsOXVeXD1GVoBj18kvHrRE7h6eyhi8P4pcUC51fpFyp6Y1NUcjZOQpuUYFfPY8IpPZM0kzZudxHJBJ-fJCT9frMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1F0N76uzgbRgR_cRKdRaIUJmxjnuiKBd7Z-fbWPeemha3B-PxIHZjA_tCJ1yrW8GbbysvrZtSwBONf94Gy6-XfeFNq5vxhNeKlu37A34w3L6cFbu3KIKfy8ICWF1Gi96Y6TQHxjzHkIiKLCZIqgvdin2PNSsGJoTRiHKO5o5F47aw-YZ8Px4GmDgfaJpmw3iGphLqYSiXRwWceev2TFKcRw52Nrm1L0jdfhYhD7zK1WYqOaRbyZEkKN_I2OX7bJYnOlXFLjWS3eJKBaRRvh9rIef0pFqw99YQz7vjseabf3i1RY8HiVMBbugWn1Rjv0PZ-q1tHy3l97-NB6woRcTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دکمه های کهکشانی/ یک ایده خلاقانه برای متفاوت کردن لباس‌ها
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/691421" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAuBC0KROSJz6IkSQx70OVk7gayglUS1SgLCvL0Q-7qCahZDghcPk9pMo3jz20rns4fRB_61ToJhMmPQqc6f2l3PfaWqO8y2XoltMcXjR0iziXjjpPiUt7GsAqSYoUyfV7h2GVsQA6d90HQ5iDjoP2JNo05j9zKJu1C63ltMJUnLoynWKhypQ2G6MC8JHC0_sTc33o0KPyPaq0a88WZgYOwNq-ATxoTg0nAmNDyMwr1pzYLRO9AXH_mQQ5eUfpB011RSSyrCJ1YvXxK3lSn3_UAkYjjtT1FVDfRtgXFHUlN85r9vZydDUfgOx7QWwQEoxgs6pvbe7Gres2ynlB8KoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: تجمع ۳۰۰ هزار نفری در تهران و آغاز جذب نیروهای داوطلب
🔹
به گزارش The Independent، بیش از ۳۰۰ هزار نفر روز جمعه در تجمعی سازمان‌دهی‌ شده در تهران شرکت کردند؛ تجمعی که در آن آمادگی برای دفاع از ایران و آغاز آموزش‌های نظامی اعلام شد.
🔹
به گفته این رسانه، بیش از ۶۰۰ هزار نفر برای طرح «جان‌فدای ایران»  ثبت‌نام کرده‌اند و انتظار می‌رود شمار شرکت‌کنندگان در آموزش‌های نظامی به بیش از یک میلیون نفر برسد.
🔹
تا ماه مه بیش از ۳۰ میلیون نفر از جمعیت حدود ۹۰ میلیونی کشور، به‌صورت آنلاین یا در تجمع‌های عمومی برای فدا کردن جان خود در راه حکومت ثبت‌نام کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/691420" target="_blank">📅 13:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691419">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d3fe8bc3.mp4?token=meEGa3V8ICAHTltQU_oLkOWTf_eBrlDx81SEaCAI090CrOu8yy18kEcY6WQTkOYZZ6PyQKMaO4Fw7MOhYwNouYPy-SjNoZT4TNdXcEvhm-3PvWZ5UpElnqjhxu8yYbfHuIXQbaG73OxQ_-cUg7XuX4bty1_cD_CYbsIR6AmVOimN7Pc4wMwjY9CspILiYd8nMF_7E87dx9Pfx_verURAmifxHGAkv9wcEAJhuyHHTa7YccDZn3eHyonRpEOijEJDDELgjClf5s_6R8EdwFHqOFDz2pjsklRcMPHwbrgLT7BPptuO8SzVaHe_FNJI6vhkGZdKb8mr9XqROkrjBxgitw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d3fe8bc3.mp4?token=meEGa3V8ICAHTltQU_oLkOWTf_eBrlDx81SEaCAI090CrOu8yy18kEcY6WQTkOYZZ6PyQKMaO4Fw7MOhYwNouYPy-SjNoZT4TNdXcEvhm-3PvWZ5UpElnqjhxu8yYbfHuIXQbaG73OxQ_-cUg7XuX4bty1_cD_CYbsIR6AmVOimN7Pc4wMwjY9CspILiYd8nMF_7E87dx9Pfx_verURAmifxHGAkv9wcEAJhuyHHTa7YccDZn3eHyonRpEOijEJDDELgjClf5s_6R8EdwFHqOFDz2pjsklRcMPHwbrgLT7BPptuO8SzVaHe_FNJI6vhkGZdKb8mr9XqROkrjBxgitw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسکتبال ایران با شکست چین، برنزی شد
🔹
تیم ملی بسکتبال ایران در دیدار رده‌بندی بازی‌های آسیایی ناگویا با نتیجه ۷۰ - ۷۹ مقابل چین به پیروزی رسید و به مدال برنز این رقابت‌ها دست یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/691419" target="_blank">📅 12:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691418">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd62af64b8.mp4?token=Pkr-TOdKQtlRzdD3_rnJeQBBsQG0ZZPjePJ9BgUcsy2b8_D8Fdx9lur-mXMM6UyogTy5NjPIGBATw9vNnXXc_VGy7F3HpvVjEImT2o0ljeEK7rZHeXct5em2j4_x-UV0OQ9P2x1_uOMqWKFxWG5p7cLVw0nVzSQ7U10b7SEXhRzEvZXUsAuDH0JA-QZ-JvNmbU4M2MgFAEhOTw7BRTTqMalq3TSQ7ZqSpExG97XHunMOcd-G8cEj82qarQni51RY_3Vk5Ef0Xi0mqOVp4TfLi-LVxgdpSkpl2_sQVyEkZQnrVrVS7SUp7Y3smJBNh0DHq_gQrgdDmpYDHBMXuUbBtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd62af64b8.mp4?token=Pkr-TOdKQtlRzdD3_rnJeQBBsQG0ZZPjePJ9BgUcsy2b8_D8Fdx9lur-mXMM6UyogTy5NjPIGBATw9vNnXXc_VGy7F3HpvVjEImT2o0ljeEK7rZHeXct5em2j4_x-UV0OQ9P2x1_uOMqWKFxWG5p7cLVw0nVzSQ7U10b7SEXhRzEvZXUsAuDH0JA-QZ-JvNmbU4M2MgFAEhOTw7BRTTqMalq3TSQ7ZqSpExG97XHunMOcd-G8cEj82qarQni51RY_3Vk5Ef0Xi0mqOVp4TfLi-LVxgdpSkpl2_sQVyEkZQnrVrVS7SUp7Y3smJBNh0DHq_gQrgdDmpYDHBMXuUbBtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه بیماری‌ها از سرماخوردگی ساده تا سرطان التهاب شروع می‌شوند!  #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/691418" target="_blank">📅 12:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691417">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای ان‌بی‌سی: کوه کلنگ هدف اول آمریکاست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/691417" target="_blank">📅 12:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691416">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: در جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند
هدف قرار می‌دهیم
رضایی در گفتگو با الجزیره:
🔹
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا — مگر اینکه اقیانوس هند را ترک کنند — در هر نقطه‌ای از این اقیانوس که باشند، هدف حمله قرار خواهند گرفت. ما به این توانمندی‌ها دست یافته‌ایم
.
🔹
ما سرعت موشک‌های هایپرسونیک خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم. همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تدابیر دیگری نیز در اختیار داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/691416" target="_blank">📅 12:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691415">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba30f7bb3b.mp4?token=eX4PjRJHOEtg8pEBnVTYaiZUjZaVGQHkSMaRYP2b57mOW2Q1KCEZ-uBSzPxcpjLAy7jS5HyEDmVm-d54eSZmYAmr2qjMj6PlswgAu15KXFBNLtqDrCWn8RZlKl5p1wD6hZQ7kTBwZ5SNL_FsEYkKEbwtzf8iTdlU9CEbDktCNndUfFx3VpMd9fdJ992NbMBDj-F39lRPgooOQt5eeqURVTlZfNCcnegmW5HVgmB7mwDGPgEbYJWXkrig6SZaQb7-s8zyfyRaj7oGM6rA0sOSu1Px6PiGRoEzAWVnya_Ia-eRaCj5q85G4UsMgW39eKN__4-Ii93Z683QxvMmjhHEJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba30f7bb3b.mp4?token=eX4PjRJHOEtg8pEBnVTYaiZUjZaVGQHkSMaRYP2b57mOW2Q1KCEZ-uBSzPxcpjLAy7jS5HyEDmVm-d54eSZmYAmr2qjMj6PlswgAu15KXFBNLtqDrCWn8RZlKl5p1wD6hZQ7kTBwZ5SNL_FsEYkKEbwtzf8iTdlU9CEbDktCNndUfFx3VpMd9fdJ992NbMBDj-F39lRPgooOQt5eeqURVTlZfNCcnegmW5HVgmB7mwDGPgEbYJWXkrig6SZaQb7-s8zyfyRaj7oGM6rA0sOSu1Px6PiGRoEzAWVnya_Ia-eRaCj5q85G4UsMgW39eKN__4-Ii93Z683QxvMmjhHEJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«مرغ شاخدار کرکسی» پرنده‌ای زیبا با پرهای آبی خیره‌کننده و گردنی شبیه کرکس
😍
🔹
گردن طاس کمک می‌کنه در اقلیم‌های گرم و خشک گرمای بدنش رو بهتر تنظیم کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/691415" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691413">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای هگزث، وزیر جنگ آمریکا: گزارش تلفات نیروهای آمریکایی دروغ است چون می‌خواهند ترامپ را خراب کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/691413" target="_blank">📅 12:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691412">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Em0evChjS8lTAFNWhF17CCANvU-7cfs6cMUsttXt6jtx_q9gjWOSvIhjylme8eedUYMJmZ0Ig7arZGIbLl3kpYoetWSmesxNCSAGTNZI0o5oHsyuQkM2IfVrjxaS5w61a4yCV8eb3WJ7lyGSk4D6lN-nvx1ehEX4zQQza-yfCReOKhWSL-ju8cfbMuds0xzoSMMqDLaojcW1nhUmba5opnJQ0hvKj6OqIDLsgUxOCXiO93HaRCFCiPPOIKsAlSIzAovw-lNAho8h_gZrOZjYZd-bhz9fR0mZPX-tFZ_ftRn1zc6GMSzy4bTcjXm4_ykgKoqyzCrTNcrMItaoqHWc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو
قطعات وارداتی شامل:
کیت‌کلاچ، لنت‌ترمز‌،شمع،وایرشمع،تسمه تایم،تسمه دینام و...
مختص خودروهای داخلی
شروع طرح: یکشنبه ۲۹ شهریورماه
ثبت سفارش با محدودیت کد‌ملی
تحویل رایگان از ۱ تا ۳ روز کاری از طریق پست
💳
امکان دریافت نقدی و اقساطی
🌐
متقاضیان گرامی جهت کسب اطلاعات بیشتر و درخواست اقلام می‌توانند به وب‌سایت ایرانکو مراجعه نمایند:
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/691412" target="_blank">📅 12:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691411">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a98dfefe4.mp4?token=lIFIlikopyigcN7ZkLQCFSFejY6M7NWnJ8ytbEsN9mZyVrKlSyhLf3snrbu9D3OwtoT14zf8R-6sQFG82y9NHGb7cR6_qkG9xn7eJv1jdoIlwnaMCsd0RSDSVJkl8lzbHW_G-92AdJjH1yTdu8TY45IpCm4ct1Z4_01-JRn8a-OdSQeu5HQonp5Rl7exkqkwA1OeFoTVBOMmzI44hXptQxLEZCZhefSsKiwU1bhLWj0kPILJAjDXG7qCfeWbSkhQbbUNhJVDBc4iYIDYL2MuSH2VcW6Yzj2Mn1fpXjmGwkefhW1Dn6haLUT98aStQSrtmAFvKes0PB0TeCF9CgncGz8WD0e1gRBCLE5fJJMBhK95CiB02aiLfDseIop0rP7frG3nqxjTvHpPhfwXoo4Ry-e8qZU4lemqINCatSkxCGHRT65OI151VsAtV3yk7jwSE6Kqbn29HIJTaUX7Wunn5qxj6Qk0_T0m2Qq6qIn3J1OWDsAUh3W2PatLfDhd19W8BUFz30vpRZLnsobF2k2rRN3ZP-42uqJQdoqaVi9XGmwl2Wwrd1Rkm75-hd7uObmEs8LFuAisGijvrrGJaDOOGL3EsDx1jV7bMkBK6LxysLn4QyzUdCH9Pw_61nW6k6UoS9xMDurBV9bY-NGYxgIUlWEnL1YSUNkwywoSv5HSj94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a98dfefe4.mp4?token=lIFIlikopyigcN7ZkLQCFSFejY6M7NWnJ8ytbEsN9mZyVrKlSyhLf3snrbu9D3OwtoT14zf8R-6sQFG82y9NHGb7cR6_qkG9xn7eJv1jdoIlwnaMCsd0RSDSVJkl8lzbHW_G-92AdJjH1yTdu8TY45IpCm4ct1Z4_01-JRn8a-OdSQeu5HQonp5Rl7exkqkwA1OeFoTVBOMmzI44hXptQxLEZCZhefSsKiwU1bhLWj0kPILJAjDXG7qCfeWbSkhQbbUNhJVDBc4iYIDYL2MuSH2VcW6Yzj2Mn1fpXjmGwkefhW1Dn6haLUT98aStQSrtmAFvKes0PB0TeCF9CgncGz8WD0e1gRBCLE5fJJMBhK95CiB02aiLfDseIop0rP7frG3nqxjTvHpPhfwXoo4Ry-e8qZU4lemqINCatSkxCGHRT65OI151VsAtV3yk7jwSE6Kqbn29HIJTaUX7Wunn5qxj6Qk0_T0m2Qq6qIn3J1OWDsAUh3W2PatLfDhd19W8BUFz30vpRZLnsobF2k2rRN3ZP-42uqJQdoqaVi9XGmwl2Wwrd1Rkm75-hd7uObmEs8LFuAisGijvrrGJaDOOGL3EsDx1jV7bMkBK6LxysLn4QyzUdCH9Pw_61nW6k6UoS9xMDurBV9bY-NGYxgIUlWEnL1YSUNkwywoSv5HSj94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابستان امسال، همدلی اعجاز کرد
کنار هم ایستادیم، از روزهای سخت عبور کردیم و نشان دادیم وقتی ایران، «قرار» ما باشد، هیچ فصلی نمی‌تواند همدلی‌مان را تغییر دهد.
فصل عوض می‌شود،اما قرار نه
....
قدردان همدلی‌تان هستیم؛ برای تمام همراهی‌ها، تمام «نه» گفتن‌ها به مصرف بی‌رویه و تمام قدم‌هایی که برای ایران برداشتید.
🇮🇷
قرارمان برقرار است؛ برای ایران، کنار هم
🇮🇷
#قرار_همدلی
#همدلی_برای_ایران
#تهران_روشن
‌
💫
با ما همراه بمانید.
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/691411" target="_blank">📅 12:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691410">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
روزنامه کوریره دلا سرا: ایتالیا آماده اعزام ۴ کشتی جنگی به تنگه باب‌المندب است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/691410" target="_blank">📅 12:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691409">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f9ee41a0.mp4?token=s2JkYIZih4aIorW35LB8LzBvS0sbnsCXgfwXc3idW9XOqbLt3keNha-KsXDC0Hz_Iy-xGrOOZb_qchyBHM5EjGU8zYPhbpXOU59tA4ute8R-MfzzQ2wpgk3ShWNgbKHRCBExDaVgb5FHskoAq88S7d9LkNytLfkMlOGLBGzeDTSiinZuqez95j0fuK7QTMov73C14l7d3r9knDaSmSl4wj66f2DGhCsjzsztb-xxteZJU-5phMIwmhy-JgHoV9Wnw253K-EBtIRVI_6ZENj1kNY1RO7Di5jooOshX808BHpRoT42tfopIjkZnpserxYuFBqPO0dpLbStzJqd-7KSHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f9ee41a0.mp4?token=s2JkYIZih4aIorW35LB8LzBvS0sbnsCXgfwXc3idW9XOqbLt3keNha-KsXDC0Hz_Iy-xGrOOZb_qchyBHM5EjGU8zYPhbpXOU59tA4ute8R-MfzzQ2wpgk3ShWNgbKHRCBExDaVgb5FHskoAq88S7d9LkNytLfkMlOGLBGzeDTSiinZuqez95j0fuK7QTMov73C14l7d3r9knDaSmSl4wj66f2DGhCsjzsztb-xxteZJU-5phMIwmhy-JgHoV9Wnw253K-EBtIRVI_6ZENj1kNY1RO7Di5jooOshX808BHpRoT42tfopIjkZnpserxYuFBqPO0dpLbStzJqd-7KSHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازار بورس ریسکی شد!
کارشناس بورس:
🔹
وضعیت قرمز بازار در روز نخست هفته، نشانه‌ای مهم از اتفاقات پیش روی بورس بود. از حالا باید ریسک‌ها را درنظر گرفت و معامله کرد!/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/691409" target="_blank">📅 12:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691408">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f26eb5c361.mp4?token=MQPXdWrQLYDGRmdtvRvmUBP4XIuqS7rNFdJccSXUf_IHXlLpmx3iiuCYVCJeFFVf4vRKFuKxRQ1W4RbjWKeVU4ggaOdwR8BosAXB0Ambr-7HCb2G6tKQ9az6XbpLlc5WlGNssX11qKht-Ptuh7HCCG-vmC7YTMauEfdrkH6Jf7gcLfpajmmY71Bkyx_NCP62xbLaEskmjQjCiIdIeBMwPnLl7RWkoKEvVYD5p1SJpNf56hvb9xKh47pf8Iu165q5RpPKKx92e_ckHNUtt8apmDTzNtPYfiHzPbLAFFSKYwyOPtxhmIrMscP1gdfNmSChZtmlMhf86G0I-ZW6oJ_NHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f26eb5c361.mp4?token=MQPXdWrQLYDGRmdtvRvmUBP4XIuqS7rNFdJccSXUf_IHXlLpmx3iiuCYVCJeFFVf4vRKFuKxRQ1W4RbjWKeVU4ggaOdwR8BosAXB0Ambr-7HCb2G6tKQ9az6XbpLlc5WlGNssX11qKht-Ptuh7HCCG-vmC7YTMauEfdrkH6Jf7gcLfpajmmY71Bkyx_NCP62xbLaEskmjQjCiIdIeBMwPnLl7RWkoKEvVYD5p1SJpNf56hvb9xKh47pf8Iu165q5RpPKKx92e_ckHNUtt8apmDTzNtPYfiHzPbLAFFSKYwyOPtxhmIrMscP1gdfNmSChZtmlMhf86G0I-ZW6oJ_NHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های تلخ محمود بصیری پس از مدت‌ها؛ تلویزیون بیننده ندارد، من برای کی بازی کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/691408" target="_blank">📅 11:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691407">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b684f06d.mp4?token=RGP9JZZfrW9U_FU-qJNQWR9fuD6Ff5qGClwyQddyr3SEn6-HVRn7r8IsWnUp0vpoRdWu5_MYGzGpm6akPkvgIDbkIU3jvVfoHgmxdfS7PhHJf3OOXRd00nWH_r-8TViEmiLEQbmDTc7uSRE0CNRQGbal0Jn-KlNsY2jA890pmqhMywexpP1Gj4c6yIDEBpRvaUuT3RTKIST-383sU9q_fO0qzR02zuYxhCBBN5EuvJNiBhGff-Ds4bZcq7mlcnex6_2DUpq0i_5oyCHBIgdzIrVRCfmjXdfuwKTWavia4MvFNhAegGgbIhn2rIggtde0orjGpwaRfUFzlBfyDkrcnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b684f06d.mp4?token=RGP9JZZfrW9U_FU-qJNQWR9fuD6Ff5qGClwyQddyr3SEn6-HVRn7r8IsWnUp0vpoRdWu5_MYGzGpm6akPkvgIDbkIU3jvVfoHgmxdfS7PhHJf3OOXRd00nWH_r-8TViEmiLEQbmDTc7uSRE0CNRQGbal0Jn-KlNsY2jA890pmqhMywexpP1Gj4c6yIDEBpRvaUuT3RTKIST-383sU9q_fO0qzR02zuYxhCBBN5EuvJNiBhGff-Ds4bZcq7mlcnex6_2DUpq0i_5oyCHBIgdzIrVRCfmjXdfuwKTWavia4MvFNhAegGgbIhn2rIggtde0orjGpwaRfUFzlBfyDkrcnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به دستور تولیت آستان قدس رضوی خوابگاه ۴۲۴ نفری دانشگاه علوم پزشکی مشهد به بهره‌برداری رسید
🔹
خوابگاه خواهران دانشگاه علوم پزشکی مشهد که با حمایت آستان قدس رضوی و اجرای شرکت صنایع معادن و عمران رضوی احداث شده است، با ظرفیت اسکان ۴۲۴ دانشجو و زیربنای ۸ هزار و ۲۶۱ مترمربع، با حضور تولیت آستان قدس رضوی و رئیس دانشگاه علوم پزشکی مشهد به بهره‌برداری رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/691407" target="_blank">📅 11:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691405">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4d41e2f0.mp4?token=EFnsr2QrfPM8OfGp9q9vII_vCDMSuFnJrVNzMIQFnR8icaP64RIyEkEvxjFNuWAu0CP_5CyMAMx16nrSHmjb8Kp-zs2xuA8rdhMlhk4EuQ_VZdduoSEce6LMuyoV1f2buD6MmFc4rBrVY2_LmCyA72g118tC3RdGeOF7XWwJGcW7f9c3Y9jsI17qFeQfLG9wWWfmmX5cohgS5hTTk_O5Id7wbwQig6pvCNoc8NV20T2k0jGrTjRK2YIQCVS5S_LVhB9XebejVdpuEogUF-lmr6bwo4CxPnLGLIF450x0B_od06mn8YCRv6YAcKp3bzaVJ8oaGZTCdZ7xlet8HQeyLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4d41e2f0.mp4?token=EFnsr2QrfPM8OfGp9q9vII_vCDMSuFnJrVNzMIQFnR8icaP64RIyEkEvxjFNuWAu0CP_5CyMAMx16nrSHmjb8Kp-zs2xuA8rdhMlhk4EuQ_VZdduoSEce6LMuyoV1f2buD6MmFc4rBrVY2_LmCyA72g118tC3RdGeOF7XWwJGcW7f9c3Y9jsI17qFeQfLG9wWWfmmX5cohgS5hTTk_O5Id7wbwQig6pvCNoc8NV20T2k0jGrTjRK2YIQCVS5S_LVhB9XebejVdpuEogUF-lmr6bwo4CxPnLGLIF450x0B_od06mn8YCRv6YAcKp3bzaVJ8oaGZTCdZ7xlet8HQeyLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی انتشار تصاویری از برگزاری یک جشن هنجارشکن در یک کلاب ساحلی در نوشهر، دادستانی و سپاه این شهرستان از برخورد با عوامل این مراسم خبر دادند
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/691405" target="_blank">📅 11:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691404">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05cb7ad599.mp4?token=P96C7kq1l2qSRCLxb8C5sotlEh6A2JJHH9bgNxdesJ_42-fNMm796CAFH4wPbPDk1wJi-qwLYtgBQgax2Mq3SvPBCPLjVU0eR12udwZQ54xk6D7Yrckg0kZz8nXvLFtwVoFy6aXb0D3vCHegqHb_8Gyy0r7jAOzSVKCC3sfgNVVER1YzQkInzUEqpVZSzlCqWJB-YjbgFxlgOQmp79d38W4HbbiSJutP4i_3rR8pccDfaElvJRG7MdBQaxifCY32LAp2Sp4zHjwLh8sqDNLEj1CNbVQgS0ziAVA4ixdxJcqdyE9EaOsx-WBlK5cfOUdDOAckIRh-aDwKdH_dmbz3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05cb7ad599.mp4?token=P96C7kq1l2qSRCLxb8C5sotlEh6A2JJHH9bgNxdesJ_42-fNMm796CAFH4wPbPDk1wJi-qwLYtgBQgax2Mq3SvPBCPLjVU0eR12udwZQ54xk6D7Yrckg0kZz8nXvLFtwVoFy6aXb0D3vCHegqHb_8Gyy0r7jAOzSVKCC3sfgNVVER1YzQkInzUEqpVZSzlCqWJB-YjbgFxlgOQmp79d38W4HbbiSJutP4i_3rR8pccDfaElvJRG7MdBQaxifCY32LAp2Sp4zHjwLh8sqDNLEj1CNbVQgS0ziAVA4ixdxJcqdyE9EaOsx-WBlK5cfOUdDOAckIRh-aDwKdH_dmbz3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند ساده، پلاریزه بودن عینک آفتابی‌ را در چند ثانیه تشخیص دهید
😎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/691404" target="_blank">📅 11:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691403">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
شرکت برق البرز: در یک مزرعهٔ استخراج رمزارز که در پوشش صنعت فعالیت می‌کرد، ۳۶۲ ماینر کشف شد
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/691403" target="_blank">📅 11:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691402">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
محسنی اژه‌ای برای پنجمین سال پیاپی به ریاست کمیسیون حقوقی و قضایی مجمع تشخیص، انتخاب شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/691402" target="_blank">📅 11:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691401">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
مقامات مصری در اختیار داشتن حساب کاربری در شبکه‌های اجتماعی برای کودکان کمتر از ۱۳ سال را ممنوع کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691401" target="_blank">📅 11:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691391">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSP29Mq9Qwsh6MJ21O3KxEi5M4OI0M9aCTB_RgM6IC7jn7uojcdVOTAwfChFi2_8L0h42teDhmLNKG6p1NtbA9ZiXb1ltxm8Kbm0j9eySbJMkePW5Ads5emL-kji5CbN0JHUd7dynk8Gt8qDxtTKLNQ7SvC5hYQm9xTxl4cgnPvtFGFDZ1AYwf6cXI3GQf23-K4Q0DOvOgTFvguOqkRUhoB1dFbf4xx0BuXCtfPqf6JyHRtXeqR5Y4zTGkGaclGWcPR0fuRBKGSv2z_PtSttX72UKIz9SnFjLcImUapdn38xwyJr55rOEgj_L4vNe_WKg16jBlvcJHsDtjRbgizFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYctKmYZEpThjrWqccc7-BtQXY-yCBjIONfi8RYEVmMuicHqjYvOQLI0DRGEJC5vmhJXeKGivvmY9o-HdaGWpkWgaVmM_Ws1W8cyLxY6JU9ocNw8znvN9BmTHnIYEZQ5i6gGyHXeItuB-0Tx2tHX-NsLU_s03me2b6WqZJh95E-vFvT9_mrPwN4OtS91YnL2SB090icNDtNxx5ir2gMLaYde6Ja_bGNkFsPOTRzxzVubwQ0FkOiyB7mVT9_NoREMOUwnGM9IKzo-Hy-0H6vtY4wdgNG9mMyIxzgo7KxwyBvw0CxtjTEf2oyTc2YWwIUluumtRy0knkzi8tNEroyRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6y-COc1Cmy6dO2wVBc1tlw79aUNjsrnIWV-uKHLWu3CBlCQR_8swdlB9z_JctVJ0Ws71ZkFztZWM0VZiP-pyt-g50DySFdDThVJD50eTN40kkrmQaW9kgqBYgEDU2Py7ooKBpWg33FvN34C-0E3LL8H7M8EKIzIyzzeMIaBeyHsQRAlC9bITifXMxoC_HJTu_JTq-i_3QSixICvqqGyTdU7P1XpzUrmF67goPB18FSaSS1tzUahk7OE9Y-QEu_LQaewmrz5TbPXtmWkqKSEvwggIvXkgiZcawlIkHVyvHccVfrkxiHkDZFxCBYxpBJS5qF_Fxn5zYJrVpjrRFo49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4qmLmu2q5iSyCE5kNRqdX0wNN5aFf5ac9d9h2PBHEP8aj-_BDiW5G-S2Vi9Q6821zV-dS6uNENEf9c_M6PmORH0r7g-1mMr-Du6Gwx9TOPKL-BUSDlvqbrEkZOg9XvRi94y0xT_nPmLue9sL1q2sd7wkGGNlyT1gVdnmhOkbfnDD05oZBB2Eaw21WFkgq3_DI5BgmGyXIYrWkjfZ27Exp2hf95UazH8bYwYk6GEKkY9H8JxC2QgtSy-N7grzb3zJ4ueE0bR60aG3iVWY_8k2-UJgO6y6r_qllOITEPGIAWzaMtMWvNBuaQN5w7hdEBO-EDsc4FLnKPKiCVl8CcODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxztIspCpBRMQo82FYRabZMhBaNC7VqIHRjcTI3TCMpaopoT00P8xsCBHtEPhctneKDiRb8G9iiIAGcC4aRbf-YZKZASYCHWXU-a6rgoV99wTEbVVl3-75OOJM7Z_yaa4ZqGAd_VlzVD5EG268n2YiBrjVBhy9kf_wp0J8-p4z0bY12MOoNc62LTwp3tsZDZMQcT2J4Aj-TvW3ZN32_5UI4FwqC-VBLVWL2HRf4BY5nubXQ--IsQCh-vXhAAaxhZKoPXvmv82LK6nrN7q1uWgoQ220mmY3d9xUCeO4I33UNo5Sq3I0gxpC8aHkxD5b9gceeAqbgkXlTRisyDClTwrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8q1Y9EdtPJYijFk9d9SKANLOe_873k42nGzpGQYF4J7Pl_28tnDx8WYh3VNG-BlqW3JBpVWerqiYtS3Vb6b_v5eKKMyq-qdyhinqKwflKhTEr4TAQwTTh3Xk99gYUMalIlWDWheYNlI_qheTYQmh7wKPHIX54GJYpw9NiTwJQ70PRRI9hX-jM9zPxu-JJ5w0z0xO6CgsX41_Bzw9couucLOAGYK5yUPhc6cHWB_x2ld0vYX32QgLvFWEuT1utpmRhT6GD3FEZ8qFyJ5w5nBNELb7Uhe5MQKyIU6HtpZG0Ja6a7bcgi56O0rIcopvGI9vOv9Uaqv-rWgxP6gJz-95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pffrADjmJHg6hbM2k_uNsFlgSvKLJ39Isxxq7mt0mTitBSh9gl0LGRF2EiRjbtNdm97VkqzOa7woqNscvhLMTQWekce9CilSkxbUQFUwiaIfobxfBvB9VGUk_gr-oJPRFYGXgxvbB7LUTQHOrYnZeS9rIyY0z3kfj_l_D9ea782gKy8PWQxh1IzYQ7QlofdzQyfToeXglfKGed1-28affHVzD76ghMkqYvvm9Tv_aVZOJnDTodt8nxL_bsYz9TU3cIm9TfiyaSYJfciw0IkW_3TB0j1iydWmgSE7Hu2Vbi4VAnrDQKOVSiqGIOlKqhu1LD6gh80kM0bXHYbSlv0wmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9ppImqCRBBh37acP5Csj_sGzYfBRLyMv7ZK2xeWuabmY0R_KmvQ8MbxCruC_5AGpM0dCwxTVie54B_CU3B7-ZwlIq6u0eeHaTEyWF6NEFct_Q3qJ9gYrfg0zVY92-9OTro2rFgm5xwXJznPiGiLG8JEoIdWwO2uTv0-ErjbsziPjl6pqLYkxvygr2gT5b99z1aN8zlxe9myJLci7mazc_87slFswhpHIWukFpbUSW4lgLlRvYPacfuqla5gPQrrpPaPq_23ubGy_WRYCcQwPwe-Q8m8phGaBVrHZX3S8jqEV7CisXRziMhNi1kguRqmZIcnmBjtJDNFnoHy7cF7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFm-BxUlC6DIlZ0rOEmqAr2JutXTtiEOhiHqbysXD8T56VpC_ODgGb1YQnOfIIM2563SHyrntlfqNDSJ24QrU8RHkLxBoNpFr3ftXJu8sbv0iJHDt7X38I6ldHEUSuIQtmMBNTdyMKksefHB4LZJzUddPT-DsCKNaczINW1GV2lapjStBBwMjj_sTQ-pT4HYqifLWK7_3DBJRY4tEONHNWn1_ZNXGSX_i9H8MQ5mtcDjsFxzt-_vQJMEM5JHdXilFstfqLaDye5RbtOqoF3r337JMI1-7ISgQIcdW549HJgTdxIjxzo2pW5gnGjBZ2mjGlBU5JbspjSk0V3m95FVJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5fSpDa6UvUHVayXK2c3fqIG5EwP9HhlDLOagYpf-D9QruZoJuOhABRSD1sV73xPB2AXmxPIPu48afAh2XRc7aMLFMtoyys-x2SVKx8ZOvcceF5pmlMimoLUc1QG5F3p7y0XkulFNex4Z3VnfwQom2fcoRW4UaE2ohxbZeGu4UNaf0dsUF2gT8WFK5IvCeT08zIwEPO4wzJmLRJOYps_U7-UzDTJ7PFFvmnov0-BpVspRix3bjLhEj3g_XMwZgf730TcqK2x-zrW8_v-Yq5S4r84SdbmcWXIawLh5dMtZMf8TfR1-pvCGX25P9SVjt9A8I9tSywYkT0yS3SzJnHMZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
پیام‌های ارسالی شما درباره چالش‌ها، گرانی‌ها و دغدغه‌های ثبت‌نام مدارس.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/691391" target="_blank">📅 11:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان‌ به نقل از منابع: پیام‌هایی که از سوی ترامپ ارسال می‌شود، این سیگنال را به ایرانی‌ها می‌دهد که او تمایلی به حمایت از متحدان آمریکا در منطقه ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/691390" target="_blank">📅 11:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
مدیرکل دفتر بهبود تغذیه جامعه وزارت بهداشت: در همه مدارس دولتی باید توزیع شیر انجام شود؛ اگر در مدرسه‌ای این اقدام انجام نشده بود، به آموزش‌و‌پرورش و وزارت بهداشت گزارش داده شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/691389" target="_blank">📅 11:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691388">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdNySZrbaeQffcQND-XX_sTExY4p2HrXM_XdXJMZdV6h5KjdJJlVy6yVd6fschleVv2V_7dYrE9IRKu2Ir6Fh0FbSyTC3Ne0D-GSoe2A3uiIgC8NueSnMait3L5SRc5aF7ZvzsSYE6Hy8YnzGCED15e-xSRhqWd_NzVZMIoR6tPP6xLIqf2ZUEO9wB8xQIWvi9KilIGFXH0BbDnPc_zkjvaFWnAbXXDlaAkteNKGqsYld6AVBTb2GuKURLrG6ki4md7LuEJxkEn4mOjNDYt9Tb6D5tkfQuKVheLlQMG3jQwufPM-QppF5x0afhqRKQYnq5dYax6mc2f-a_DGaB0nXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بادگیر چپقی، سیرجان
🔹
یک معمار سیرجانی، ایده‌ای از صنعت کشتیرانی را با معماری سنتی بادگیر ترکیب کرد و سازه‌ای ساخت که هنوز هم یکی از نمادهای معماری سیرجان است.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/691388" target="_blank">📅 11:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691387">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سخنگوی سازمان ثبت اسناد و املاک کشور: مالکان سند سبز و زرد نباید دوباره در سامانه ثبت ادعا، ادعای مالکیت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/691387" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
پزشکیان: با هم‌افزایی و انسجام داخلی بر مشکلات غلبه می‌کنیم/ قابل قبول نیست که ما مسئول باشیم و فردی با مشکل معیشتی مواجه باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/691386" target="_blank">📅 11:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34df6c957.mp4?token=EtL3u4JhGTraxvAZpvPv1iOS2NKO_Gpu89MoHmYz3NeiAIP231yRA6SgbwGBuGDkBlXFCTaLSAxXXQl8OCJ3ieM1zEkLJT2nsSSYpxckE1R59QxBpvYyq59j9AknrSRZVMhvHG9-m9qR9o7Ev-KwzfuK__GYK_o2IixJov-XpS53tY_7THB1R8xJNIatZ0CXKa98JlftDBz1Fv_AR4PjlKiw23jSH3BuDXZeeUglwzA-iOXxd_pc3KQRaKdXRTSFYsY9fraR0luMTs7Q68qpf3uZPoRq0BlL4zIAEvpj-eLxTMP6YeMkQcWtkpW0wQaOPtvI1EszX1-nJ_uyanJ9u0yRsBu6-FTcN-MIjYR6BIAuBlFyc6_FrE71dF4rgfa2EgWSXClkMuHo4X9JAyyjEzVNzdaNlEsyOroN6s2eo_tqwzppOE847mBXYKGFWzvZqCGRGVFKzSrkq00lXt6ndGdTadwEddgvmB0yHXvzs0EnkS_N_U-gbrnkU71O36vwfe4LJxqsCFrA6KrjcyzsgaPWD_VNbCT8UOBR1VuZULIEC1uTPIO4TDJjr3tctwLLE0fGoTX2jINQzkXnNS5lMyNpfHBe5gC3z5QMg441sCKRrxDy_1WBFAt6CSeOtDo-quPNUTB408_NCI1wcIdypTh_YegW8RRrZbaQZwa_9dI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34df6c957.mp4?token=EtL3u4JhGTraxvAZpvPv1iOS2NKO_Gpu89MoHmYz3NeiAIP231yRA6SgbwGBuGDkBlXFCTaLSAxXXQl8OCJ3ieM1zEkLJT2nsSSYpxckE1R59QxBpvYyq59j9AknrSRZVMhvHG9-m9qR9o7Ev-KwzfuK__GYK_o2IixJov-XpS53tY_7THB1R8xJNIatZ0CXKa98JlftDBz1Fv_AR4PjlKiw23jSH3BuDXZeeUglwzA-iOXxd_pc3KQRaKdXRTSFYsY9fraR0luMTs7Q68qpf3uZPoRq0BlL4zIAEvpj-eLxTMP6YeMkQcWtkpW0wQaOPtvI1EszX1-nJ_uyanJ9u0yRsBu6-FTcN-MIjYR6BIAuBlFyc6_FrE71dF4rgfa2EgWSXClkMuHo4X9JAyyjEzVNzdaNlEsyOroN6s2eo_tqwzppOE847mBXYKGFWzvZqCGRGVFKzSrkq00lXt6ndGdTadwEddgvmB0yHXvzs0EnkS_N_U-gbrnkU71O36vwfe4LJxqsCFrA6KrjcyzsgaPWD_VNbCT8UOBR1VuZULIEC1uTPIO4TDJjr3tctwLLE0fGoTX2jINQzkXnNS5lMyNpfHBe5gC3z5QMg441sCKRrxDy_1WBFAt6CSeOtDo-quPNUTB408_NCI1wcIdypTh_YegW8RRrZbaQZwa_9dI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ مردم به چند معمای ساده، به یک نتیجه غیرمنتظره رسید!
@Tv_Fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/691385" target="_blank">📅 11:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691384">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
فراتر از یک میلیون مأموریت در سال؛اورژانس تهران ناوگان خود را دگرگون کرد
🔹
سالانه ۱.۲ میلیون مأموریت امدادی؛ اورژانس استان تهران ضمن پاسخگویی به این حجم عظیم از تماس‌ها و مأموریت‌های روزانه، فاز جدیدی از توسعه زیرساخت‌های عملیاتی را به اجرا درآورده است.
🔹
افزایش چشمگیر ظرفیت پایگاه‌های امدادی در نقاط پرتردد، نوسازی و تزریق آمبولانس‌های جدید و پیشرفته، گسترش خطوط موتورلانس برای کاهش زمان طلایی امدادرسانی و اجرای طرح‌های نوین عملیاتی جهت ارتقای دقت و سرعت پاسخگویی مهم‌ترین اقدامات توسعه‌ای اخیر اورژانس تهران می باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/691384" target="_blank">📅 11:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691383">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
افزایش کرونا و آنفلوآنزا در سه هفته اخیر/ موارد بیشتر خفیف است  رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت:
🔹
بیشتر موارد خفیف است و با استراحت و مراقبت بهبود می‌یابد، مصرف خودسرانه آنتی‌بیوتیک برای بیماری‌های ویروسی توصیه نمی‌شود.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/691383" target="_blank">📅 10:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691382">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سازمان غذا و دارو: مجوز محصول سلامت محور به معنی اجازه برای هرگونه ادعای تبلیغاتی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/691382" target="_blank">📅 10:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691381">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477de95318.mp4?token=fvQEWpDQQMXdehOIy2ylaDq8o9xguljDCuRzRRi-24CB09xKxO8Pi9yDww5ThZS6j5v8Im6_ASfOmnzySzisTEAJjyCxKtrBDQTvL0L1GEZzMgUaKV2d7XS-EnLlWnQxDuR3pD0IIvIdi8cHcHZOOrBIJN-jY0wSRVlwjRZ3Qaxl8qrnTShNagq_PlMXdHBqqRksudXrQ5yF2YzEkCdTJo0_5hlZXrpHYZFf0-F2eCeeswQD8elJxHUk4GoGmw93vWLPGe5MixsYC39tFhqdfHBzF-5fNJMnQ4nP2aJRNepcNpl-GeqZjdw7XmBIh3joGVUbBTgl16AiDZi1kXCGdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477de95318.mp4?token=fvQEWpDQQMXdehOIy2ylaDq8o9xguljDCuRzRRi-24CB09xKxO8Pi9yDww5ThZS6j5v8Im6_ASfOmnzySzisTEAJjyCxKtrBDQTvL0L1GEZzMgUaKV2d7XS-EnLlWnQxDuR3pD0IIvIdi8cHcHZOOrBIJN-jY0wSRVlwjRZ3Qaxl8qrnTShNagq_PlMXdHBqqRksudXrQ5yF2YzEkCdTJo0_5hlZXrpHYZFf0-F2eCeeswQD8elJxHUk4GoGmw93vWLPGe5MixsYC39tFhqdfHBzF-5fNJMnQ4nP2aJRNepcNpl-GeqZjdw7XmBIh3joGVUbBTgl16AiDZi1kXCGdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ سوژه شوخی نخست‌وزیر کانادا شد
🔹
در بحبوحه تنش‌های تجاری آمریکا و کانادا، نخست‌وزیر کانادا با تقلید حرکات دست ترامپ، حضار را به خنده انداخت.
🔹
مارک کارنی، بارها هدف طعنه‌های رئیس‌جمهور آمریکا قرار گرفته و ترامپ از کانادا به‌عنوان «پنجاه‌ویکمین ایالت آمریکا» یاد کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/691381" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691380">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
مکمل آهن و ویتامین D در مدارس توزیع خواهد شد
مدیرکل دفتر بهبود تغذیه وزارت بهداشت:
🔹
در مدارس دخترانه هر هفته مکمل آهن به مدت ۱۶ هفته برای جلوگیری از کم‌خونی توزیع خواهد شد.
🔹
همچنین در مدارس دخترانه و پسرانه به‌ صورت ماهانه مکمل ویتامین D در تمام کشور توزیع خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/691380" target="_blank">📅 10:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691379">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b05cdb98.mp4?token=F8HU-OFsg1UBa1oLRRMUeKIC8cuyVUNdfMsUzaypsfaStG89fvyzkl4U-wX7T7QxKsjJ_1fLct6HuW8mSxfOSUfj_yMhYYto62SgPEd55EVqAmERYR9eRGy42ELdVkIOeX6QeN97vl3OSDSx9GJxt8OMOjBEkxFoH36rFqexCy8LdVBix3F7Npk3_tdz1X2QZRR3QuVptrsFyaRMxTzLc4-kmMDdcsXFU-ba1-Di_w2yXreTbfOKVeWndos49_fNfLkfbCeeSVn1a_rQ-pxL-DL429W0EaUyw1QoAfcQgonbSJhEPDE6fcwGDt57syWRQlTpd_ia4UtTAwGAXWjs4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b05cdb98.mp4?token=F8HU-OFsg1UBa1oLRRMUeKIC8cuyVUNdfMsUzaypsfaStG89fvyzkl4U-wX7T7QxKsjJ_1fLct6HuW8mSxfOSUfj_yMhYYto62SgPEd55EVqAmERYR9eRGy42ELdVkIOeX6QeN97vl3OSDSx9GJxt8OMOjBEkxFoH36rFqexCy8LdVBix3F7Npk3_tdz1X2QZRR3QuVptrsFyaRMxTzLc4-kmMDdcsXFU-ba1-Di_w2yXreTbfOKVeWndos49_fNfLkfbCeeSVn1a_rQ-pxL-DL429W0EaUyw1QoAfcQgonbSJhEPDE6fcwGDt57syWRQlTpd_ia4UtTAwGAXWjs4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گله بزرگ گوزن‌های شمالی در چند قدمی دوربین عکاس حیات‌وحش در ایسلند
🦌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/691379" target="_blank">📅 10:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691378">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/691378" target="_blank">📅 10:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691377">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8b7ba2ca.mp4?token=nSyp_YSVMIPP5w8jqlUiRselw6TwNy3nFGdBzZMrRjUoNds5LxSQqQZdhihX1Oxfji6OUqNFCCkVQ7LZypmy216MTxoHaL7Ihd_PitttuRMmjmsNO9i7qDVBd6JgY4rmlliJdFU79xQznHj8pHFWICHcshM4xiKQYOspqmyPfrnAyfcmHrHwbp50HGcEhD_QaVyetlGgHfBXfvI8uOPdwtUipaADtL-D6K5HjnaBCUCEGKNmlC2OVdj9PHtEkjgobZ7jXehpz9hF49nWKdq2ENrhMP3-NGa79hhkfY-swOtNGu7OImt6YiElvYjVrqUpKld0_CVQXR7d0-2cSVpNWg9ESA-exy4K5QGsVbeO4l5MdBgHn9IfaOHPEYlSbFQyuXuW0XE_JLpNVPE6MKZjJcxYxB5W4gZsB1LVcvq-5NpL9OOT6UlPFshev2rXBIOzJqs03R6Cz02B_iZKEZPrlRFaTlfvJsU77hEHKMuUu5yi2G8eTZYbNXZt4Q11EFv5k3IWKaGbeC6JQHd53-MZ8CTfdVRoh4CPjiHaV1JbQaYlRIIkMEvAh4699S_H1kvij1GI7LuJHauCra8gLqNqKSaeeTBNzKZY_GiazystV2YK6jGnmyI80CUOleK2AHo9SUeaH6wZjSJVofQL8KiYJlxsNrss_B-CIHF406zZMFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8b7ba2ca.mp4?token=nSyp_YSVMIPP5w8jqlUiRselw6TwNy3nFGdBzZMrRjUoNds5LxSQqQZdhihX1Oxfji6OUqNFCCkVQ7LZypmy216MTxoHaL7Ihd_PitttuRMmjmsNO9i7qDVBd6JgY4rmlliJdFU79xQznHj8pHFWICHcshM4xiKQYOspqmyPfrnAyfcmHrHwbp50HGcEhD_QaVyetlGgHfBXfvI8uOPdwtUipaADtL-D6K5HjnaBCUCEGKNmlC2OVdj9PHtEkjgobZ7jXehpz9hF49nWKdq2ENrhMP3-NGa79hhkfY-swOtNGu7OImt6YiElvYjVrqUpKld0_CVQXR7d0-2cSVpNWg9ESA-exy4K5QGsVbeO4l5MdBgHn9IfaOHPEYlSbFQyuXuW0XE_JLpNVPE6MKZjJcxYxB5W4gZsB1LVcvq-5NpL9OOT6UlPFshev2rXBIOzJqs03R6Cz02B_iZKEZPrlRFaTlfvJsU77hEHKMuUu5yi2G8eTZYbNXZt4Q11EFv5k3IWKaGbeC6JQHd53-MZ8CTfdVRoh4CPjiHaV1JbQaYlRIIkMEvAh4699S_H1kvij1GI7LuJHauCra8gLqNqKSaeeTBNzKZY_GiazystV2YK6jGnmyI80CUOleK2AHo9SUeaH6wZjSJVofQL8KiYJlxsNrss_B-CIHF406zZMFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژنرال بازنشسته فرانسوی: مدام به ما می‌گفتند ایران به زانو درآمده و محو شده، نه تنها ایران نابود نشده بلکه امروز می‌بینیم که نرخ سوخت به قیمتی بی‌سابقه رسیده و برخی جایگاه‌های سوخت در فرانسه تعطیل شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/691377" target="_blank">📅 10:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691376">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc38481e6.mp4?token=MeLbQlRCHDpTNAoi_KF8oExk-VkxB_rB4Io9zIPhNTuaHkFBEMwA5qwAZU_-4fxt9eGZj351pT5Si2kEMp4iWH696D4sdp9DnTOKkrWDkfJdyZV6ZLT5NN4FyqzxSjO_l0xO7R-TMqHLVB8ymmATj0UOMLcFD8jZy4jIvMt5x0ohhLhYNhOM3G8wDYhNmCqUuHNPsPaRkV9QPSdLnJhnyT87TlMkIQf6DQb9XOIixTYF8dK08fCC4rAyys2x2QXp0m0qFpuIkS8jNS2Y2GpNp0AYOSDZX0LiUpoMuXniQOIIlrOEjtD6wrHarnw9pHtCkqEnGmH5D1SXit1lbblr6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc38481e6.mp4?token=MeLbQlRCHDpTNAoi_KF8oExk-VkxB_rB4Io9zIPhNTuaHkFBEMwA5qwAZU_-4fxt9eGZj351pT5Si2kEMp4iWH696D4sdp9DnTOKkrWDkfJdyZV6ZLT5NN4FyqzxSjO_l0xO7R-TMqHLVB8ymmATj0UOMLcFD8jZy4jIvMt5x0ohhLhYNhOM3G8wDYhNmCqUuHNPsPaRkV9QPSdLnJhnyT87TlMkIQf6DQb9XOIixTYF8dK08fCC4rAyys2x2QXp0m0qFpuIkS8jNS2Y2GpNp0AYOSDZX0LiUpoMuXniQOIIlrOEjtD6wrHarnw9pHtCkqEnGmH5D1SXit1lbblr6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«بشقاب پرنده» رسماً در چین به فروش رسید
🔹
شرکت چینی «ئی‌وی‌تول»  فروش یک هواگرد برقی دو‌ نفره به شکل بشقاب پرنده را آغاز کرد. این‌ بشقاب پرنده می‌تواند بر آب و خشکی بنشیند، تا فاصله‌ای نزدیک به ۳۰ متر پرواز کند و تا ۱۵ دقیقه در هوا بماند. به خلبان خودکار مجهز است و برای پرواز در باد شدید طراحی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/691376" target="_blank">📅 10:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691375">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12cafc3c9.mp4?token=UeJredKU8-lNnfsd4Yvu_RK9ZBDKPdwjZqzbnqVatvODxRsMVZu-ei6MbCMvDm4qNkE58L4O8W6zrv5bBOeCiEpIMVWMdCxObVz1QUP8Dm7_pQqflI7ShS6U5nFY3To6EGexR-xr57q0P3bnWhiyzFum1QEC4XPlub0b84iqvQPOCSCWbMKtR_HMMWF2jJhyVkh4FaDxHPtPAAmbE1DCZqeku6xNSGCDYXpe1D5TUddfzegbr1XJQaMSa-SygbfxZ-exVlM1izc5XteeH2wJm39QPBrwBeEG3hg1zualumM9VZIneIsNYKNlWQInqgzf4Q5z2bg9IEZb6KNy_F-3yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12cafc3c9.mp4?token=UeJredKU8-lNnfsd4Yvu_RK9ZBDKPdwjZqzbnqVatvODxRsMVZu-ei6MbCMvDm4qNkE58L4O8W6zrv5bBOeCiEpIMVWMdCxObVz1QUP8Dm7_pQqflI7ShS6U5nFY3To6EGexR-xr57q0P3bnWhiyzFum1QEC4XPlub0b84iqvQPOCSCWbMKtR_HMMWF2jJhyVkh4FaDxHPtPAAmbE1DCZqeku6xNSGCDYXpe1D5TUddfzegbr1XJQaMSa-SygbfxZ-exVlM1izc5XteeH2wJm39QPBrwBeEG3hg1zualumM9VZIneIsNYKNlWQInqgzf4Q5z2bg9IEZb6KNy_F-3yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیاین باهم اسنیکرز سالم و خونگی درست کنیم   مواد لازم:
🔹
شکلات تلخ
🔹
خرما
🔹
بادام زمینی
🔹
جو دوسر
🔹
کاکائو
🔹
کره بادام‌زمینی #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/691375" target="_blank">📅 10:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691374">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkxLvWXAU3CrHy3ICRV0H8DzQAdFM9Y2igGGKIY02U4lwDGldUKgvjwoj2eSiQs4YWYv0Mi46MDuvzuusuGARojKN--NEr2WRckiEV_LUFXndHpnXNLHtPvMIVhtepRAo6QX9I4DNoj9K8XzjGcX_YtLFlMLCwnEWRDnNiNhrFr_s5LqnaHfonHpKCJtpvyQDEoRci2sDGiNGDedceT8GylXMt6XSRaSpK3xtdDXnT4fKBwJRaND4DZxHS4AN7Uxy_UKR_SfNxRgFCyqadcRW3gSdS_SrdouRs_BO9ETMzhBMvUU_0CMK2fwYymbyRhFAtYuJ9RhM-MLV6HyrH8Cbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارشی که در جنگ ایران، آمریکا را تا مرز حمله به چین بُرد | گزارش نادرست چه بود؟
🔹
یک خطای تولیدشده توسط هوش مصنوعی در سیستم اطلاعاتی ارتش آمریکا، در جریان جنگ ایران، نزدیک بود واشنگتن را وارد رویارویی مستقیم با چین کند؛ روایتی که بار دیگر نگرانی‌ها درباره استفاده از سامانه‌های هوش مصنوعی در تصمیم‌های حساس نظامی و اطلاعاتی را برجسته کرده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246396</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/691374" target="_blank">📅 10:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691373">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObIEyVtaKWmhCx_WUE1o_NgHvPGuqtR6jNiPhTHkF5-JXoSkJnl36fHsN7hQcfnpf9tQaB5OPSMKmJUZdEzhE_fHX8msJPPDSAtR7HhdIx1Mg9QN4MoC8TfiVSxWxiE5xPnuWFeLFqiLXJyvGKPTmtSto4Sdt0Swa1XQHZxij-SxHavYAT1O838vg53ooa7kR4901M8JZ790oxRbfRCw9k-GsIp0oQk0LgBSdmx-LQd3d8muEI7wASFWmf90ySzXg7FvdbdAyLk3YVGjksgp9onUdSWHEKQthnjcCH7DRuNz_hVAaGHlGmXjSom_aB0-QRMJrBrL_EHGFDDVEWlH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت جالب کاربر یمنی: حتی قدمت لوله‌های فاضلاب یمن هم از قدمت امارات بیشتره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/691373" target="_blank">📅 10:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691372">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4Ymaop3_zHjXeR-OQ601cmhdxjcXr4mDjCIkb1HpWc_JFXsrxiJph9vPzIImqb2RyKjTmClKxPsU13CEtRQHiWORwySmGZjE3jCLheSudDPG_rNFTEoAN6xZeK4OfyC81p3abQvzpQWTXTZSFuL5PxA__G4TGcQU3_yziw4QwRN7XUE_3y6hubhBXVDZkzTAz8JaoX2mRaFMFq1Jvcvqo9tQ1aAiG1tya3-Vl4D8JYy6XfBdlj9BLV4xa5wBchoKOL5dOKJoBL_JFA4EfOG0MElf4UNFx94_duNzgx8mvPUAUMp4Laz0Z8pzovnA-Yeg3wkEY04j2On_9D908KtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوکراین یکی از بزرگ‌ترین موج‌های پهپادی خود را به سمت مسکو پرتاب کرد
🔹
روسیه ادعا می‌کند بیش از ۱۶۰۰ پهپاد سرنگون شده است، از جمله ۴۵۰ فروند که به سمت مسکو هدف‌گیری شده بودند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/691372" target="_blank">📅 10:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691371">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=C9KMsCZTsra1jSHZM5NPrhct5NNJ0HlKDA__AH0BqmTQDShFTcumNuWrnMb31gEln1wpikR40VAeFrKgb5Eyl3qhNAlVyMPEL5W2zCR4sVYE4bNU8nRwrh71Mz8lqcA7XAOtQM80IP101SHr-AlLzwCTrcr7skWIJGDb7C4GZrw8BiM0ylOReegIGyMayrGgBzKvjFp74Y6T-ktmq1n2Gl_OsfkNbcUlrehrwRYTYe59XgkRlHkEFcGLXAY8QZRO-ilwPLO0b42T2k2X1pm_XxVWA7ZmwmFuj0FMSIDTSF2YCeTGysY4u0uuRTcs-vpr7vd7HzNADpK_0qUMP8QU8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=C9KMsCZTsra1jSHZM5NPrhct5NNJ0HlKDA__AH0BqmTQDShFTcumNuWrnMb31gEln1wpikR40VAeFrKgb5Eyl3qhNAlVyMPEL5W2zCR4sVYE4bNU8nRwrh71Mz8lqcA7XAOtQM80IP101SHr-AlLzwCTrcr7skWIJGDb7C4GZrw8BiM0ylOReegIGyMayrGgBzKvjFp74Y6T-ktmq1n2Gl_OsfkNbcUlrehrwRYTYe59XgkRlHkEFcGLXAY8QZRO-ilwPLO0b42T2k2X1pm_XxVWA7ZmwmFuj0FMSIDTSF2YCeTGysY4u0uuRTcs-vpr7vd7HzNADpK_0qUMP8QU8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوکراین یکی از بزرگ‌ترین موج‌های پهپادی خود را به سمت مسکو پرتاب کرد
🔹
روسیه ادعا می‌کند بیش از ۱۶۰۰ پهپاد سرنگون شده است، از جمله ۴۵۰ فروند که به سمت مسکو هدف‌گیری شده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/691371" target="_blank">📅 10:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691370">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQAyTF9uf-CvocjtkuArjflHqRFd0QugpM29lTuhOoPSr6DMwql2hMTswDmVHR8KV93NBfzcapWUTRJbgbptPficup6bmzm9OaS01QaAPuOKm3tGHlQ2TguhgffaNW7WGWTDaz7K9TpxF41IMX_8pf5MwM_AJ8E6SohNKqQR_XEyF_PiHzf5aBzYOdg802zAKrUSRf-BDJmqmmPrGNCoVCScfGE7g33Y7CoD5cOXl173fCFcAx8kPhq07i3v1GWqBBVRDzzIJrB8BcXtz9SIpUiPfLaSIzRPJdAAQt-8g7z3zZjkXJnC75Eq_puw55gI88Lkc5z7K2n_x6B83AKrkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفند درست کردن ماست سفت و خوشمزه خونگی
😋
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/691370" target="_blank">📅 10:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691369">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
فرمانداری دزفول: صدای انفجار شنیده‌ شدهٔ دقایقی قبل در برخی نقاط شهرستان، مربوط به امحای مهمات بود
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/691369" target="_blank">📅 10:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691368">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e8e48689.mp4?token=AEa9n19kF-YXI_iFzSODROZm8tc4-GbAWGSx_WcRL_zlj_vrK5N7TOLq3adScbdpcZjWBtcD5yO5Acjl1MtXgOGDbaKmz0WNtb6IQifZqYLUcj_4IA3uYDkWU5JMgJlmDbgvst5GK-bhweIBGPSuHh2WBAUr4tV0MnXWihoVcB-g5qbRUvEN8AXF_OcViIJFb_UetS2uYC4rVCOmvguXbZOTOC7226aFz4MEAYjdGx7XwOfiv10pDC_B1wKyaGoMXJizTroEgQpO-i4kmeo3E8Wog845jmhhVhne6Q1TGFzJgiOPvVTfuUPr4Pvbm9jDATuhhWBYc81M5F6cEP5nYoHJ1G7sj0_K7lCPDl2Rlot7R6rfTaqHiU30nHJMmexZCrHcL-r9BHHB6UQJ0bA4ZbFvp2ez4e6q8lQ8VLJEKfphqWqmRWBWKikivMUScZyhsJhAoyDhfi0npvC3sKhpYM6a_KID8poVjNZwKAvFsUf9KeYUe4jsrat6PKetfo_ssFiIiWcIOU-w-LWSW60npl1G8dz_8uA2d5_qmAHCcZ9VLX3w0aPHfhN5lNOjipkoZZu91_xwnj1Pvv3JeEp8mflBpGwelXhbkOZdtGD9QP4VgJwxEyLYzAbzQO-tSczA0H891gcyop2wDhqz1ClsM3jN6HV2eHUfhkVwGQ3DaAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e8e48689.mp4?token=AEa9n19kF-YXI_iFzSODROZm8tc4-GbAWGSx_WcRL_zlj_vrK5N7TOLq3adScbdpcZjWBtcD5yO5Acjl1MtXgOGDbaKmz0WNtb6IQifZqYLUcj_4IA3uYDkWU5JMgJlmDbgvst5GK-bhweIBGPSuHh2WBAUr4tV0MnXWihoVcB-g5qbRUvEN8AXF_OcViIJFb_UetS2uYC4rVCOmvguXbZOTOC7226aFz4MEAYjdGx7XwOfiv10pDC_B1wKyaGoMXJizTroEgQpO-i4kmeo3E8Wog845jmhhVhne6Q1TGFzJgiOPvVTfuUPr4Pvbm9jDATuhhWBYc81M5F6cEP5nYoHJ1G7sj0_K7lCPDl2Rlot7R6rfTaqHiU30nHJMmexZCrHcL-r9BHHB6UQJ0bA4ZbFvp2ez4e6q8lQ8VLJEKfphqWqmRWBWKikivMUScZyhsJhAoyDhfi0npvC3sKhpYM6a_KID8poVjNZwKAvFsUf9KeYUe4jsrat6PKetfo_ssFiIiWcIOU-w-LWSW60npl1G8dz_8uA2d5_qmAHCcZ9VLX3w0aPHfhN5lNOjipkoZZu91_xwnj1Pvv3JeEp8mflBpGwelXhbkOZdtGD9QP4VgJwxEyLYzAbzQO-tSczA0H891gcyop2wDhqz1ClsM3jN6HV2eHUfhkVwGQ3DaAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فولاد خراسان در ۲۵ سالگی؛ از رتبه اول بورس کالا تا پروژه‌های توسعه‌ای
محمدرضا سجادیان، مدیرعامل فولاد خراسان در
#گفتگو
با خبرفوری:
🔹
فولاد خراسان در بیست‌وپنجمین سال فعالیت خود در سال ۱۴۰۵ تولید در حد ظرفیت اسمی را دنبال کرده است.
🔹
این مجتمع در سال ۱۴۰۴ رتبه اول عرضه میلگرد در بورس کالا را به خود اختصاص داده و حدود ۳۰۰۰ نفر به‌صورت مستقیم و ۸۰۰۰ نفر به‌صورت غیرمستقیم در آن مشغول به کارند.
🔹
توسعه پروژه فولاد شرق خراسان در سنگان، احداث نیروگاه خورشیدی و پروژه جمع‌آوری، انتقال و تصفیه پساب شهر نیشابور از دیگر برنامه‌های توسعه‌ای فولاد خراسان است.
ادامه مطلب در سایت خبرفوری:
https://www.khabarfoori.com/fa/tiny/news-3246426
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/691368" target="_blank">📅 10:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691367">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdssC_NEZRQm1NPv6fpJCDMlowbhRYCv8Wc-FSVapFXSwDgZX_sNHOiuH4ZoIUTba0l0mYHhcEB-cTGbxm5UhpHV9HlU_RpLM30yiP2PuaYuafUptKpKTjwrKFfDibPb197FAuxwQtevk47m8pmW_TIUkv09vOlQ_WvUWpGZHSzR1iaPC-TCS74YsEMFoDVNVUKsD1yMC6hfjw-F5DSvZ0j7dfWPYO3ArVDePpTv1DrC0h58zyqRHg_zWc-H4loKVooqUeDsnvrP9MxfGnToNqjVoJcp9X6z9RtkpcEmCOmUvbrM34yuuujUF2vOENoBdf8ASYRM_IbF4IwVZnQ91Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف گُل جدید ملقب به گل شیطان
🔹
پژوهشگران در غرب تایلند گونه‌ای تازه از گیاه را کشف کرده‌اند که ظاهری عجیب و تقریباً شیطانی دارد، گلی سیاه با زائده‌هایی شبیه شاخ و لکه‌های نارنجی درخشان. نام علمی این گیاه «تیمیزیا دِمونا» (Thismia daemona) یا «گل شیطان» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/691367" target="_blank">📅 09:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691366">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
قالیباف: نگاهی که از جنگ سخن می‌گوید اما سازوکاری برای پایان مقتدرانه‌ آن ندارد و جریانی که نسخه‌ تسلیم و پذیرش شروط یک‌طرفه‌ دشمن را می‌پیچد، هر دو دچار خطای محاسباتی‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/691366" target="_blank">📅 09:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691364">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
قالیباف: مقاومت مردم با شکل دادن به نظم جدیدی در منطقه و جهان، باعث گشایش‌هایی در حوزه‌های‌ اقتصادی‌ و استراتژیک خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/691364" target="_blank">📅 09:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691363">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
قالیباف: هم باید جنگید و هم مذاکره کرد  رئیس مجلس:
🔹
ما معتقدیم دو گانه جنگ یا مذاکره واقعی نیست بلکه هم باید جنگید و هم مذاکره کرد. باید معقول و مقتدرانه جنگید و در زمان مناسب با اقتدار و عقلانیت مذاکره کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/691363" target="_blank">📅 09:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691362">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5xR-4LnWIm2gnZNU5Sv8Bwx7Q_n0qYH_Zd_BM-N-fnYe_qABf3euWfVwSbODd-COw9Y_bbCHnmA5UehsrkGkpdtY1-cTS1qYNzxdgC1cey9MUGhW4egblSB-f9rASi5g1RmV5Dpsqov97BylfIRx4a6wOUdICdlX9TLBl8W6n13hbkICS1JVyDpCdxjYxp1QyGYJrgjG-Oku57Apgw0uRG1cTOKnbZE0bLPOoVv778aFskCDGIUQ7Tnlzmjb3999RnozBH6XYiqDZZ0UUPBO1Fkhe2UeImDjdUvGWdefCG28yBpUCSWSNE92e6c4FIj635S9EdVbIzj3p6QWRXyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش شدید عبور نفت از تنگه هرمز
🔹
بر اساس داده‌های منتشر شده در شبکه‌های اجتماعی، حجم نفت عبوری از تنگه هرمز در سه‌ ماهه دوم سال ۲۰۲۶ به حدود ۴.۹ میلیون بشکه در روز رسیده است؛ رقمی که در مقایسه با حدود ۲۱.۶ میلیون بشکه در روز شش ماه پیش، کاهش قابل توجهی نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/691362" target="_blank">📅 09:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
قالیباف: هم باید جنگید و هم مذاکره کرد
رئیس مجلس:
🔹
ما معتقدیم دو گانه جنگ یا مذاکره واقعی نیست بلکه هم باید جنگید و هم مذاکره کرد. باید معقول و مقتدرانه جنگید و در زمان مناسب با اقتدار و عقلانیت مذاکره کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/691361" target="_blank">📅 09:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691360">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-text">🔹
روایتی شنیدنی از شجاعت راهدار «جان‌فدا»
‌
🔹
گاهی رسالت یک راهدار، فراتر از آسفالت جاده‌ها و حفاظت از حریم راه‌هاست؛ گاهی این رسالت به وسعت پاس‌داری از جان مردم است
‌
🔹
رئیس اداره راهداری و حمل‌ونقل جاده‌ای شهرستان رزن، داوطلب خنثی‌سازی یک بمب عمل‌نکرده در جریان جنگ شد.
‌
🔹
یمینی در آن لحظاتِ نفس‌گیر، ثابت کرد که «جان‌فدایی» برای ایران، تنها در میدان‌های نبرد نیست و در هر گوشه‌ای از این سرزمین و در راه تأمین امنیت مردمان آن تجلی می‌یابد.
‌
🔹
شما را دعوت می‌کنیم به دیدنِ روایتِ یکی از راهدارانِ جان‌فدایِ ایران..
‌
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/691360" target="_blank">📅 09:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691358">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj87w9gbt4XAh5OfjnYsGwl_KOBNvkv0Vyg8pVaKHYdiPBHQ699i7mSsn2vGwCgDpHQF9ssDCJUUwN5siYEgtnCmapqgH2G8C2EIUCr0HkU-JC-QioN20c5bljHAV5CiOxu9gs6eDGoGR9vqFxSy8CD5lqnyPRCw5WTLQJapAYJtgMIK4BF3F8h9k8W_a_5Eje2zE1Rc-IMlXhkUKuJgSc-vHTOWhJJyelnpv6FkZFTG_ijde6EOjqDD7pRuL9HxO4D2bJfXqv_So2Mae7R1kgAvtLaKXBScy7kYeTD4jXaR6j5mOQipyF1CDOdVkKfWtZvtmA5ZclNPTW_1Tzm89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان درست و مکان درست به روایت تصویر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/691358" target="_blank">📅 09:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691357">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e03868b4.mp4?token=bSMviC4_t1j_yp-_JLeXYGcjA1tTy-Ls4YMiglzG2gW8DU1l31MnNsdZq0Z14neLjj6yi1x-UotRGhAL5jHxfEOmFgUMpd4jg7ShxQ3rSTXv_Y8fqU2BnceQrmCny5AWAsGTEQC6NchjC3jUw0toi4eDqh4HXb5TwvnB05IaJY5Ks5fIq4i0n9qQ3sPNwEQ3Pm4vPW9vGMBxbQFZXKAg-oaPi_o7OfAZn18bf4reedV1dcWWAoOoRoL77IMIszRwxQH2iR1UTqaGBOx7vO6yha5H-JUOuz3O4Naq2uM8Z8S49CnPhQMf4ckyKJDa7z27kv8Jk2k5qDLcUc1pcRktvgKXsBNzw4jXcEVOFEtXn-xjx4MNPi1Aia3NsO4IcSglHbnbbv1AoVF6h2QkwHmtJfxQBmC18JdkAqlGcCku4KgcvAhONysgzy65uoe67C1TZrxwfk7HPIZTYVSHX-cWHziE8cjqa8AKQfGwojU9mnnMcdSFtvDP3uEV7kSTBhGrc-I8mRlgwivCaycK3cCo4eHXaVLAIy4R2Nmn7rJ0XGMmkNO25rvscXazQYmGI004Su_41ot7ZTSKsozj2gIjrVE6xhNWfTiCnLq2V9X6CvKrqvj4iVnDG5SDdCxrB_KMJTUrpUdk7biUPbkUgJm3xr4is6NoJYJN9g_MRgZQHz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e03868b4.mp4?token=bSMviC4_t1j_yp-_JLeXYGcjA1tTy-Ls4YMiglzG2gW8DU1l31MnNsdZq0Z14neLjj6yi1x-UotRGhAL5jHxfEOmFgUMpd4jg7ShxQ3rSTXv_Y8fqU2BnceQrmCny5AWAsGTEQC6NchjC3jUw0toi4eDqh4HXb5TwvnB05IaJY5Ks5fIq4i0n9qQ3sPNwEQ3Pm4vPW9vGMBxbQFZXKAg-oaPi_o7OfAZn18bf4reedV1dcWWAoOoRoL77IMIszRwxQH2iR1UTqaGBOx7vO6yha5H-JUOuz3O4Naq2uM8Z8S49CnPhQMf4ckyKJDa7z27kv8Jk2k5qDLcUc1pcRktvgKXsBNzw4jXcEVOFEtXn-xjx4MNPi1Aia3NsO4IcSglHbnbbv1AoVF6h2QkwHmtJfxQBmC18JdkAqlGcCku4KgcvAhONysgzy65uoe67C1TZrxwfk7HPIZTYVSHX-cWHziE8cjqa8AKQfGwojU9mnnMcdSFtvDP3uEV7kSTBhGrc-I8mRlgwivCaycK3cCo4eHXaVLAIy4R2Nmn7rJ0XGMmkNO25rvscXazQYmGI004Su_41ot7ZTSKsozj2gIjrVE6xhNWfTiCnLq2V9X6CvKrqvj4iVnDG5SDdCxrB_KMJTUrpUdk7biUPbkUgJm3xr4is6NoJYJN9g_MRgZQHz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ جالب کارشناسان صداوسیما به یاشار سلطانی درباره ادعای نقض تفاهم
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/691357" target="_blank">📅 09:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691356">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV-jL94H19SW-8M4HIwR0lRGP-4KB1ZWkso26lb98E7dlunc5YYCvdp3DW9kz_jBNFpljYceUSjcv_atU-4US7OOzc3jS2BxQJ-xAhlgH3I5cVRux4441je_2XmlvaNrLWtJoriRIqbMARFBQ6pGE0KeDLwYaDROlWE2i3l7Rf5opzaDh_doxS5hIbVeDafmN-D7Njqu6J9lI8vqbY211SP4Uc7h0-QL3p7angJiVAJMfdckTW3EukYxWwB9cOw3IduqJ9jLZUYL_ulYEW5TDTfaciIdIFYnkN9IHTNkdo0muksHlq45UNAXtCGAwC6sxh3hfzaTAyaikjlTRvStPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عزیزی رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: بار دیگر مشخص شد همه این "به اصطلاح" اطلاعات‌تان چیزی جز دروغ‌های بی‌اساس نیست
🔹
درس عبرت بگیرید و از خطای محاسباتی مجدد پرهیز کنید وگرنه نیروهای پیروزِ مسلح، درسی فراموش نشدنی به شما خواهند داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/691356" target="_blank">📅 09:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691355">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d7c5fd13a.mp4?token=jviBYJ-af86zSdakEZJLgX_AY_y4j136nzCzRbN7Xazsuaup3BbQD05jcukV5n_hOMyCCx9NW5xBEEbPI-MmpUAQXC3UMR3aFMETsfRrSmL9gsuZUULG1H3bKCiOLxrqP2n73_fpY4v8WOdCx7D0XISKQgaAcqikclCf-VmPSNpry5JrTckoZAKA0HJHTg_hrhOsE_nlWc8hbj6TZS3sPaBQZTErTwv1k9gaEXPxYUp2524g5BEwOr99sYfOY-ndkB2JDrdRVUbBer4A3hiB9pDW5nEhwSPly_mrbQiguymLSDhrCe9ziHrcgFC5xMc81Ag7Z1xu7KYd1X6-O6LLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d7c5fd13a.mp4?token=jviBYJ-af86zSdakEZJLgX_AY_y4j136nzCzRbN7Xazsuaup3BbQD05jcukV5n_hOMyCCx9NW5xBEEbPI-MmpUAQXC3UMR3aFMETsfRrSmL9gsuZUULG1H3bKCiOLxrqP2n73_fpY4v8WOdCx7D0XISKQgaAcqikclCf-VmPSNpry5JrTckoZAKA0HJHTg_hrhOsE_nlWc8hbj6TZS3sPaBQZTErTwv1k9gaEXPxYUp2524g5BEwOr99sYfOY-ndkB2JDrdRVUbBer4A3hiB9pDW5nEhwSPly_mrbQiguymLSDhrCe9ziHrcgFC5xMc81Ag7Z1xu7KYd1X6-O6LLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران شدید گازوییل در آمریکا؛ گازوئیل در چند ایالت نایاب شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/691355" target="_blank">📅 09:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691354">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دیباچه چله علم‌النور4</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/691354" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
اسرار طریق روشنایی؛ فصل چهارم
دیباچه:
🔹
با کسب رخصت از بارگاه الهی، می‌توان چهل بامداد با ذکر اسماء الهی، معرفت‌طلبی و خویشتن‌داری، حکمت را در قلب خویش جاری کرد.
🔹
نام‌های پروردگار برخلاف نام‌های انسانی، حقیقی و راستین هستند، زیرا خداوند در صدق محض قرار دارد و هر یک از نام‌های او به‌طور کامل با ذاتش منطبق هستند.
🔹
انسانی که با باور عظیم و عمیق دعا کند، نتیجه را به حکمت الهی واگذار می‌کند، زیرا نام خداوند
«الْمُبِين»
و آشکار کننده‌ حقایق است.
🔹
شرکت در چله نیازمند شجاعت دل کندن از عادت‌های ناپسند و هجرت از مُلک مجازی شیطان به سوی ملکوت الهی است.
🔹
در دوران آخرالزمان، انسان باید ورودی‌های ذهنی خود را کنترل کند و با سحرخیزی و ذکر، بستر خیال را برای دریافت انوار الهی آماده کند.
🔹
هدف این چله آن است که انسان از مُلک ظلمانی شیطان هجرت کرده و «در نام خدا» و در حریم امن الهی زندگی کند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/691354" target="_blank">📅 09:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691353">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
درمان سرطان از مهرماه رایگان می‌شود   معاون درمان وزارت بهداشت:
🔹
برنامه جامع سرطان کشور از مهرماه آغاز خواهد شد و همه کارهای مربوط به درمان سرطان از جمله بیمه، پزشک، بیمار و خیران در سامانه ثبت می شوند و شناسنامه‌دار خواهند شد. بر اساس این برنامه تمام بیماران…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/691353" target="_blank">📅 08:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691352">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd7489466.mp4?token=NcMDk00x4Sfd6oLGZtFAmlJEuh5BTMKuQ0jhczCArYvMh48MIJGIOAZrIkcA-Ook8R7WqzA6T5UQhSIt1weWpAYs8CmVARCJjkne4zdmuQUDjGE0I0Rdc8IeZEGvBaHmKqCYZp0qwKRq346sFOnJ3v7oMYM1M6RuPVstqoIEHFms0FZKPqYFjNzDqZORkx9jQTyb-JTVaEV8ku-DRYSuChJTFvUcqklZxkcv2fFb1pmC-voJ6olOlqeqYZV8YEp1Aty7NK9gAGUvv7SZb8gkwEJsfkMcrGaQZoJFPRyroVlm2XqlXQA2Va4-TkY_1bXgBhYfBqxDyeTFCXbUKGnKVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd7489466.mp4?token=NcMDk00x4Sfd6oLGZtFAmlJEuh5BTMKuQ0jhczCArYvMh48MIJGIOAZrIkcA-Ook8R7WqzA6T5UQhSIt1weWpAYs8CmVARCJjkne4zdmuQUDjGE0I0Rdc8IeZEGvBaHmKqCYZp0qwKRq346sFOnJ3v7oMYM1M6RuPVstqoIEHFms0FZKPqYFjNzDqZORkx9jQTyb-JTVaEV8ku-DRYSuChJTFvUcqklZxkcv2fFb1pmC-voJ6olOlqeqYZV8YEp1Aty7NK9gAGUvv7SZb8gkwEJsfkMcrGaQZoJFPRyroVlm2XqlXQA2Va4-TkY_1bXgBhYfBqxDyeTFCXbUKGnKVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات پلیس انسان‌نما به خیابان‌های چین آمد؛ گشت‌زنی T800 در کنار افسران مسلح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/691352" target="_blank">📅 08:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691351">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28aca932a.mp4?token=BfSfDISz-pugmwBmBekSYwIY-V2iMdj9yUH780r6I3vqAzEzIQvUbHPX9YGRdx3_F5NdUXetNH6zOA4Hh3A81oiNtgStiPH7MUJvERtJ54nABKDl7wUqubWSdNcvjNCp_cu5Q8c7IG9O-MrEp6In1MnVvpRFfqmnlhzXUkGOloqgMUIhvqGPYqCocDjtO5rwCxwZPI1M1ALOc0K0UxWgwOSXLvycdiJZgIKh5vUu6jxEBDyLzE52CSydwIHnvjPz1wu9Zj-02OsnxqhyumIpPDfKVoex7HD712afNJX7DwQ4oqxf1YzpCeQzf1NsoPu_troDu4jZdqvdCvzngbMdqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28aca932a.mp4?token=BfSfDISz-pugmwBmBekSYwIY-V2iMdj9yUH780r6I3vqAzEzIQvUbHPX9YGRdx3_F5NdUXetNH6zOA4Hh3A81oiNtgStiPH7MUJvERtJ54nABKDl7wUqubWSdNcvjNCp_cu5Q8c7IG9O-MrEp6In1MnVvpRFfqmnlhzXUkGOloqgMUIhvqGPYqCocDjtO5rwCxwZPI1M1ALOc0K0UxWgwOSXLvycdiJZgIKh5vUu6jxEBDyLzE52CSydwIHnvjPz1wu9Zj-02OsnxqhyumIpPDfKVoex7HD712afNJX7DwQ4oqxf1YzpCeQzf1NsoPu_troDu4jZdqvdCvzngbMdqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این حرکت یک‌دقیقه‌ای، سردرد و درد گردن را فراموش کن #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/691351" target="_blank">📅 08:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
کاخ سفید از لغو تمامی برنامه‌های امروز ترامپ خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/691349" target="_blank">📅 08:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845225aa1f.mp4?token=iHjo8SFjlF5SRjqApmOWDfGsbS5ny9MkLsxai0Yj9x131lREPnlq1Xr-wq1cDWs_FFW4eM7cZkJXkXdD7sf-FVshbebCEasVhnKtaHOYnxAkv2St6NnYuqfYGftsZHIvRGfzvSoVzB9JV60fOTeDTXXwS34IDN0DK3Rmv4joJbjME0__LVUgWfUNuaMbMFPkWdILRg1or0ohAl9M9HwP9Wf5J7jgSHu2UXcgLnP6nLqzvFTci4dl6VMyQA-fdg2SDBxm1IJROLq2q0GDuB1B_RErh6mAkK71eqO0zLV6LmQECDH33qCncF94L9Jja0UvjSFUrPnPL4-uJBP1cASitA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845225aa1f.mp4?token=iHjo8SFjlF5SRjqApmOWDfGsbS5ny9MkLsxai0Yj9x131lREPnlq1Xr-wq1cDWs_FFW4eM7cZkJXkXdD7sf-FVshbebCEasVhnKtaHOYnxAkv2St6NnYuqfYGftsZHIvRGfzvSoVzB9JV60fOTeDTXXwS34IDN0DK3Rmv4joJbjME0__LVUgWfUNuaMbMFPkWdILRg1or0ohAl9M9HwP9Wf5J7jgSHu2UXcgLnP6nLqzvFTci4dl6VMyQA-fdg2SDBxm1IJROLq2q0GDuB1B_RErh6mAkK71eqO0zLV6LmQECDH33qCncF94L9Jja0UvjSFUrPnPL4-uJBP1cASitA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبکه العهد عراق با انتشار این ویدیو مدعی شد آمریکا نیروهایش را از عربستان خارج کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/691348" target="_blank">📅 08:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
صدور هشدار امنیتی فوری به شهروندان آمریکایی توسط سفارتخانه‌های منطقه
سخنگوی وزارت امور خارجه آمریکا:
🔹
سفارتخانه‌های ایالات متحده در سراسر خاورمیانه امروز هشدارهای هماهنگ امنیتی صادر کردند.
🔹
شهروندان آمریکایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری بیشتری داشته باشند و از احتمال لغو پروازها، بسته شدن فضای هوایی و اختلالات احتمالی در سفر آگاه باشند.
🇮🇷
ایران – از سفر خودداری کنید؛ در صورت امکان، فوراً منطقه را ترک کنید
🇮🇶
عراق – از سفر خودداری کنید.
🇱🇧
لبنان – از سفر خودداری کنید.
🇸🇾
سوریه – از سفر خودداری کنید.
🇾🇪
یمن – از سفر خودداری کنید.
🇵🇸
غزه – از سفر خودداری کنید.
🇸🇦
عربستان سعودی – سفر خود را مجدداً بررسی کنید.
🇧🇭
بحرین – هشدار صادر شده است.
🇴🇲
عمان – هشدار صادر شده است.
🇶🇦
قطر – هشدار صادر شده است.
🇰🇼
کویت – هشدار صادر شده است.
🇯🇴
اردن – هشدار صادر شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/691347" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
آکسیوس: ترامپ تعطیلات آخر هفته خود را در اقامتگاه کمپ دیوید نیمه‌کاره گذاشته و بدون هیچ توضیحی به کاخ سفید باز خواهد گشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/691346" target="_blank">📅 08:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0bUOUF_MD-tkvNJcQIDU-t8Xz_QRNUIYYKZAYlwb5FpLKv_HAFEakVM2R_bmoQwGu2pLHcr3awvC_aKj9orRjQHvce3AZkQ5kwnJswjsoq7gPvLQgfsUTqVLg_DlSggPZ2T4XCTfYTNi5lbm61-xUVo4ERF_m27l59Xk65ydqHT-PCrqOBUoOAdRZKsV8XdnVqUPVN6i-CNteOcI2dXAgaWEdkcwUJoYHm1MOyVY5QrvjuvUVX2j9RF-KVQ4ueNgsefZMYDVtZUiyrd3UM3hsLj2fJCiIv8PcmRTRKE_7XlRtD00liffR7jxuhh9Gbyt7XmgNceisFx4gEPZxbRSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر اساس گزارش کنگره، از زمان آغاز جنگ آمریکا با ایران، حداقل ۲۴ فروند پهپاد MQ-9 ریپر از دست رفته که نشان‌دهنده خسارتی در حدود ۷۲۰ میلیون دلار است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/691345" target="_blank">📅 08:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ6SiS6-glXTNXFL9jHp5pcKH0Y2f_CTVw2dpVYiN7DSEC43osl1mbo3wVsbw5bltAr8aGl26Z56LPlqhOCH2qUOmkM5WrYsOuR5RdKPFa0rpcRljo-hQPaRBSao6f2ri0RvsfN_kJAm3xc4IeQk0iAwlYQRUZetZKJzoHJWImzmBKl7eO0MmuAZ5Soqqc9wyeHnuUSqSOUhjYPRei50DWlWh7dSd7W-yZ3rl7reX1Ew1D9G8MQFx0UvalsqBQaSMTdOz_PQeAMZHEtQmeV6-rvCbPzUjWADt-rnNJHFAZCmQgpEXEaHnLbNzSE2sAtMmMrMlnJYqeXE1FNm7J4raQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار امنیت ملی سی‌ان‌ان مدعی شده که نشست ترامپ در کمپ دیوید به منظور بررسی و بازبینی گزینه‌های حمله به یمن بوده‌ است
🔹
اکنون، رئیس‌جمهور آمریکا به طور زودهنگام به کاخ سفید بازگشته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/691344" target="_blank">📅 08:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j600Z4xd7pGXMV_SJCfwEe6D4rSJuQahXsplbjm2P1vy6Tkjbjf2uPsL2gacoXF8wJQfKl-LdJSomKllSk3Q6_EPOKI-c5lq5_xjbb79FjVOofzgkRbFUlWyAVuVx6-diNLAVIb_DGndynPkyux0sMh_Qex14OQpBmQ9snK04Y9pjsheBTK88vmvCCBg5y5jrnuz65ZivcEBqd6cP7iZPDCRBkStVM1oFwFQuD7grLb3DEyV6kqpXReWruHuzKVI7Z7nMotGCzSULQiX6O_Rc376lzcQggpDd50Osrq2v2amowONak8isCBE2aI60sAqJR4Jk0UldeIuN-uATBpERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۹ شهریور ماه
۸ ربیع‌الثانی ۱۴۴۸
۲۰ سپتامبر ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/691343" target="_blank">📅 08:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcAQmr6ItzFrxc7qb6T8Lcz1uiwE62dM_ak1jT_pWnJ6KkQaIL1mZfAsaALcc511Cv78kvIK14byhFa5XavmnMWuc-hcatMjZ1F2b4UB1Dz5rEsvA-GGbEnbPNsRpXCFU_MXg47TqujLYiJbQoqMbRPc-Mxp7bnUn4WEGncqtZOGjdd9KqE2iIuBxzBqhrNFG2AXylQvKwYLHeykmAYEXu4uqFDN5WKT7Uik_3ZHzoIye8Lm-X7gIT2jx5egthE_9Q6aFjmhhxfX178rDYrt0LQ3xbsNt-FK0aYS6xmuj6LM9Jw83Mja8MjQ838kZ51zxSfXkVrkWgt2Q8Dtp79yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج دستگاه تست قند خون دیاباتان SMM 1000 +دستگاه فشارسنج بازویی دیجیتال
یک ترکیب کاربردی برای کنترل راحت‌تر قند خون و فشار خون در خانه. مناسب برای استفاده روزمره‌ی سالمندان، افراد دیابتی و همه‌ی کسانی که می‌خوان وضعیت سلامت  رو با خیال راحت‌تر پیگیری کنن
🔴
قیمت: 2580 هزار تومان
پرداخت درب منزل
خرید
👇
https://memarket24.ir/product/brief/63615/180124</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/691342" target="_blank">📅 00:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aafb71c373.mp4?token=dNBJ8UFFbw6zh0ShKf0eMQVC2xia3f9Tt-JQDjmwwzeOakazg3U8lbEQq7c1n6uO0TTMTFYJu3XAtPDRJ0u4-5dezWrHOAHoGfHZ4vyhJ5zONRJbvlLykTW47nCUslkA1DBjgglLnugR_aRwu3ucA_xeohQNo82KyJzjVBHpS8uXQW_utyotaXEffhHe4jbRwYmcYL0nydNq8SkSysNhjP4FrJSPtZaOYLUp9jQyjF2UnphbTc4rRWhPOolLKz3rLvFN0ZuTsfPb-7JDOKEFLEJ7N0IK0peXdomyqL-mDQp9qQkd9fT1kpkAjqMUjFcPE8PWaREESYwl1GLODCsd3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aafb71c373.mp4?token=dNBJ8UFFbw6zh0ShKf0eMQVC2xia3f9Tt-JQDjmwwzeOakazg3U8lbEQq7c1n6uO0TTMTFYJu3XAtPDRJ0u4-5dezWrHOAHoGfHZ4vyhJ5zONRJbvlLykTW47nCUslkA1DBjgglLnugR_aRwu3ucA_xeohQNo82KyJzjVBHpS8uXQW_utyotaXEffhHe4jbRwYmcYL0nydNq8SkSysNhjP4FrJSPtZaOYLUp9jQyjF2UnphbTc4rRWhPOolLKz3rLvFN0ZuTsfPb-7JDOKEFLEJ7N0IK0peXdomyqL-mDQp9qQkd9fT1kpkAjqMUjFcPE8PWaREESYwl1GLODCsd3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت ترامپ از افشاگری رسانه‌های مستقل
🔹
ترامپ جنایتکار، در اقدامی خلاف قوانین بین‌المللی ورود خبرنگاران شبکه‌های خبری سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و وبگاه پولیتیکو به کاخ سفید را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/691341" target="_blank">📅 00:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f7dfdd8c.mp4?token=L3K3BMGlBikatIedVIhhNax7VrT6BTNSM6_3o6-GWDA7R83JsKrhCnyH1wzPFA8ghCiqEy559Ws6tRkjn8eHFs7FqBbKadQTvkmHVZGlxBrjPhJFoXxjBpBNOkg8Wb7E6Q_s5fxKv0VGqO1fHYsM06ZMhbBGnssQ_mTVg_LP2k7NeN1oTm0ZNFhUaK7U347rEyo56Recduc9x83MHfhQQvYdeAOSyISGFPIM-JkHL88149mq91Fso-NuAtcXq8V_n_wd3bQq-kMD-Nx3Rbjow3_qkFkiSlwG28ImKaZ7KwqphZySTB0KRWwMsyDmvhAKoQUziA7HdDJPGj2aMN6U0DzwwZv2vMG1NvTzP7PRxEmuLRxL27VplcvOhT0gpA4rEE1_q4jf_CoGB-JLDvmY6RDeGZDJux0X6He09OsaVF5VBnT60K_Y_xiKKoJiTBMpumdrSKLnEKpMWc3QOIFZNKre9FiwJTZhgDWKr9MunJbo190qBwPV649A6NIGmg2ByOTKFCWlAVOT7T6hb9cHSTBABIgk9oEMi8NX-Mmr0QFA3Qev8yV_zjgm3C7RqQWV-ffVU2qBoy9pLcdxNUJudscEX5yMEFUilji0at5c0_XY4ksZ9Lp3FwkSdGgMAeyQ-PsSXTDE7EHn2_Cz5zpJJWrUPEIeqKYns05WxZKfo4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f7dfdd8c.mp4?token=L3K3BMGlBikatIedVIhhNax7VrT6BTNSM6_3o6-GWDA7R83JsKrhCnyH1wzPFA8ghCiqEy559Ws6tRkjn8eHFs7FqBbKadQTvkmHVZGlxBrjPhJFoXxjBpBNOkg8Wb7E6Q_s5fxKv0VGqO1fHYsM06ZMhbBGnssQ_mTVg_LP2k7NeN1oTm0ZNFhUaK7U347rEyo56Recduc9x83MHfhQQvYdeAOSyISGFPIM-JkHL88149mq91Fso-NuAtcXq8V_n_wd3bQq-kMD-Nx3Rbjow3_qkFkiSlwG28ImKaZ7KwqphZySTB0KRWwMsyDmvhAKoQUziA7HdDJPGj2aMN6U0DzwwZv2vMG1NvTzP7PRxEmuLRxL27VplcvOhT0gpA4rEE1_q4jf_CoGB-JLDvmY6RDeGZDJux0X6He09OsaVF5VBnT60K_Y_xiKKoJiTBMpumdrSKLnEKpMWc3QOIFZNKre9FiwJTZhgDWKr9MunJbo190qBwPV649A6NIGmg2ByOTKFCWlAVOT7T6hb9cHSTBABIgk9oEMi8NX-Mmr0QFA3Qev8yV_zjgm3C7RqQWV-ffVU2qBoy9pLcdxNUJudscEX5yMEFUilji0at5c0_XY4ksZ9Lp3FwkSdGgMAeyQ-PsSXTDE7EHn2_Cz5zpJJWrUPEIeqKYns05WxZKfo4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفت و گاز چگونه به وجود آمدند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/691340" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای وزیر خارجه ترکیه: شرایط جدیدی برای مصالحه بین ایران و آمریکا پیشنهاد شده؛ امیدوارم آن‌ها این شرایط را بپذیرند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/691339" target="_blank">📅 00:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed220764ce.mp4?token=pGblxxoXO0DKKf11IyYFwGthCZVn-P2CUOEW2WOT9hVrV7FUIx4tSfj_U-QugjUXCu861k2NDAl09TvOqCPHQfW_X5UucUfIf5zmwBf1sA6scJLcp0Uj1mLjGPgXFYKYlr0os6PJIEoO_fl3PUenE5QbTtXt3HJZNhdLj_YCxvyTwhVNFa7vRMtt7Tijo2npQDsO_3SOe5Tkz5e2Ki7-dAmS72CTzEK47i5oKXiBIMBihuPCHBx6Ia-o6VgDSfiK5UXb7u3NX4LbfuY3KpQ-GR35RO2aZrGTQT51c4sapSV24l0vuCLRTUzpK0nifEwJ9bm0I2aFG8tz_FR44sUkdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed220764ce.mp4?token=pGblxxoXO0DKKf11IyYFwGthCZVn-P2CUOEW2WOT9hVrV7FUIx4tSfj_U-QugjUXCu861k2NDAl09TvOqCPHQfW_X5UucUfIf5zmwBf1sA6scJLcp0Uj1mLjGPgXFYKYlr0os6PJIEoO_fl3PUenE5QbTtXt3HJZNhdLj_YCxvyTwhVNFa7vRMtt7Tijo2npQDsO_3SOe5Tkz5e2Ki7-dAmS72CTzEK47i5oKXiBIMBihuPCHBx6Ia-o6VgDSfiK5UXb7u3NX4LbfuY3KpQ-GR35RO2aZrGTQT51c4sapSV24l0vuCLRTUzpK0nifEwJ9bm0I2aFG8tz_FR44sUkdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نبستن کمربند ایمنی، کمک‌راننده را به بیرون خودرو پرتاب کرد
🔹
در حادثه‌ای در ویتنام، یک کمک‌راننده که کمربند ایمنی خود را نبسته بود، هنگام تصادف از داخل خودرو به بیرون پرتاب شد و آسیب دید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/691338" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuphLmsCDwopeHcJLSH-UHI3wQaxXaC81CVdmgKMvwTGxzBOV4DwO6a-vRgbFY0SJoqPkAZg-uu2Gp1hvhSuCcQ-CJHoKI3RbJ9skxilz9mOmWxeGbQO1wqoYyRCEm-SsezYLtmNYt8oBG-tGmNSKPejH-XdZL7v1lKPihgOI3JukxWVq-pfGr09RB-gwItFm0DMMiP2SNTd49bLMTKAVQoI1ZmM9kXG8YXf-X5dVx2KOuAX_dvqwQEm9D17mUxjy25HohoJFu9wlk9c_3_N2PLEH8UUUvn4cpOHkh6pHEUnrcebVY2vx5XweCSawBphAK2H1J1J9Jkln40zCAmb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/691337" target="_blank">📅 00:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ائتلاف سعودی: ریاض هدف حمله موشکی نیروهای مسلح یمن قرار گرفته است
🔹
ائتلاف سعودی در ادامه مدعی رهگیری و انهدام این موشک شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/691336" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
امارات میوه و تره‌بار صادراتی ایران را برگشت زد
رئیس اتحادیه ملی محصولات کشاورزی:
🔹
بیش از ۲۰۰ کانتینر یخچالی ۴۰ فوت حامل انواع میوه، تره‌بار و سبزیجات صادراتی ایران، از سوی دولت امارات متحده عربی برگشت داده شده است. هنوز دلیل برگشت این محموله‌ها از سوی دولت امارات اعلام نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/691335" target="_blank">📅 23:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691334">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/691334" target="_blank">📅 23:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691333">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOv81J_dCZbzlgf6Cc2_W04alHSj89lo_RmVNCe7eAq5vqC8e0LchTg70vigN6A6ti8-Xerz63zU-W8DQWK3ph6IMURLw2lGSOiT1OJnI4cadEInO9SqdEa4t8jtcD-nAOJcP5E6gbLSqGlRvkyaHnaB1qSZZfiyV8gBNsvF6soCz354pWd__Nhshqs3MtqIHSDrx_T7-fVFdf9K9xNfa2DCpB0Uo5R29i4c-GlO-bOu9vk-eiAikS7NVh1F0sPhI_Q9Tn9pqGsq24A4RkIrkM7ti6yABsjQsCCk7SxqZNNrHXX1CsYUT7ftzG_iyD3g1IVs4YjAeXNpJcpHvgwPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
جعبه هدیه «ختایی»؛ یادگاری از حریم ملکوت
این جعبه، مجموعه‌ای نفیس از تبرکاتِ آستانِ مقدسه است؛ ترکیبی از سنگ‌های متبرک، تسبیحی با عطرِ مشهد و عطری آرامش‌بخش، تا هر بار که به آن می‌نگرید، قلبتان راهیِ حرم شود. هدیه‌ای فاخر برای آنان که عشقشان، زیارتِ بی‌واسطه است.
✨
مشخصات محصول:
▫️
نگین: قطعه‌ای از سنگ‌های متبرک روضه منوره
▫️
مُهر: قطعه‌ای از سنگ‌فرش صحن‌های مطهر
▫️
تسبیح: سنگ‌های یادگار مشهد (سنگ متبرک)
▫️
عطر: رایحه ملایم با طبع دریایی
💰
قیمت اصلی: ۲,۴۵۰,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۲,۱۰۰,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/691333" target="_blank">📅 23:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691332">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b559054a3e.mp4?token=liNcmKFfDYhdmYwZjN8bip9pe7R59IurfEP4TU5N-Rt9YM1RGsLdRPUlZADCkXtl7lwiMF1JuoksDwoT4zngyjhwKPHmwZqOPANM9QS58DZBJQtvTe98A9C_C3LGXfI6QTORSI6t_V5CAM4s5LD-h7Uy8OptYBboEc-1tWVSFj01zmAs0WUWMmQwJ-Rd6vW2qbg0XHWMvGa9cM-uAH7oSx2ZVMy5pe_pYAn_CxTdyRMNDeAjtBg0Gtf3mziSZo4C39UyaYYF3tjfeUD0eloSDyc-HSGuktAGHjC7r3li0ItVk8-vUE8ZNQ1hM9pfTMgfgTCqha9u97iQYuNWtqgyj5oYGv3zM56aDP9XlCVQiCwIM76-JXOEBigNRAc72IglbEp7PGfHa8M6T6GUQkVF_SZCf6IL27KSzehB8JvrTVQd_HpZEKTp8HuVK-jjcoG9S_R_Q80Cf3iNsCHV_tZPj5Xtpg-lyVfCKMZ2l1Rr2cM_zCHK7n3ThNoFoBqoGVDWt6-nV0HggSaSRJFNREqGmy5OCGAdtyh9MbIq14A133ox64HyHM3qNn-glfAXEaIFdvIHg-5bAZl4cAA9O_T631Bkw6qYiUOJpYuQaAL1sGsTIhFYj3tQm9UEAUPyXut0PmQDVFzxyzfR83MDsX0-7w7gk39Cqn3NSp98-vHw_Mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b559054a3e.mp4?token=liNcmKFfDYhdmYwZjN8bip9pe7R59IurfEP4TU5N-Rt9YM1RGsLdRPUlZADCkXtl7lwiMF1JuoksDwoT4zngyjhwKPHmwZqOPANM9QS58DZBJQtvTe98A9C_C3LGXfI6QTORSI6t_V5CAM4s5LD-h7Uy8OptYBboEc-1tWVSFj01zmAs0WUWMmQwJ-Rd6vW2qbg0XHWMvGa9cM-uAH7oSx2ZVMy5pe_pYAn_CxTdyRMNDeAjtBg0Gtf3mziSZo4C39UyaYYF3tjfeUD0eloSDyc-HSGuktAGHjC7r3li0ItVk8-vUE8ZNQ1hM9pfTMgfgTCqha9u97iQYuNWtqgyj5oYGv3zM56aDP9XlCVQiCwIM76-JXOEBigNRAc72IglbEp7PGfHa8M6T6GUQkVF_SZCf6IL27KSzehB8JvrTVQd_HpZEKTp8HuVK-jjcoG9S_R_Q80Cf3iNsCHV_tZPj5Xtpg-lyVfCKMZ2l1Rr2cM_zCHK7n3ThNoFoBqoGVDWt6-nV0HggSaSRJFNREqGmy5OCGAdtyh9MbIq14A133ox64HyHM3qNn-glfAXEaIFdvIHg-5bAZl4cAA9O_T631Bkw6qYiUOJpYuQaAL1sGsTIhFYj3tQm9UEAUPyXut0PmQDVFzxyzfR83MDsX0-7w7gk39Cqn3NSp98-vHw_Mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکمه‌های لباس چطور ساخته می‌شوند؟ فرآیندی جالب پشت این قطعات کوچک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/691332" target="_blank">📅 23:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691331">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b57bab2cd.mp4?token=uetLUyqcG8fcU7Frc85d3cCLAZnvoOb2i__pKyLI7O6p8U3vB6_6yxSdbMHtDCyG8ezEWjzKabaEbJ-7tSJzxjsXkklZstLrQoE8hjZnf-q0EyNz2bNnANvYKvPIkL1g51jFMHOWCRV2Mz_tPnQT5A0X62tLnLG6BaswvkyHSUGVRy6hOMezTiwntQKzF48_2SUaR8FOFABXqeI0D8-7M3t7Svg_TFLcXsZ3MnYIbCYnfHiE0pXa31qSbpVQuYYwW2F9BX1SNPZOjAMgecmVDlcRbse2yULGxeOWR_HjLbVzPPw8K1hZVPbrAqABJ9Yqxwb8KUc9F-wrVdTY79I6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b57bab2cd.mp4?token=uetLUyqcG8fcU7Frc85d3cCLAZnvoOb2i__pKyLI7O6p8U3vB6_6yxSdbMHtDCyG8ezEWjzKabaEbJ-7tSJzxjsXkklZstLrQoE8hjZnf-q0EyNz2bNnANvYKvPIkL1g51jFMHOWCRV2Mz_tPnQT5A0X62tLnLG6BaswvkyHSUGVRy6hOMezTiwntQKzF48_2SUaR8FOFABXqeI0D8-7M3t7Svg_TFLcXsZ3MnYIbCYnfHiE0pXa31qSbpVQuYYwW2F9BX1SNPZOjAMgecmVDlcRbse2yULGxeOWR_HjLbVzPPw8K1hZVPbrAqABJ9Yqxwb8KUc9F-wrVdTY79I6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات رزمی باورنکردنی استاد ۸۰ ساله در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/691331" target="_blank">📅 23:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691330">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
معاون توسعه مدیریت سمنان: روند تعطیلی پنجشنبه‌ها در استان سمنان تا پایان سال‌ جاری تمدید شد
#اخبار_سمنان
در فضای مجازی
👇
@Akhbar_Semnan</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/691330" target="_blank">📅 23:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691329">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
یک منبع در وزارت حمل و نقل دولت صنعا خبر داد از دهم تا هجدهم سپتامبر، میانگین به صورت روزانه، ۳۵ کشتی از باب‌المندب عبور کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/691329" target="_blank">📅 23:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691328">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ترکیه: آنکارا تحت ائتلاف مکه، نیازهای نظامی عربستان در زمینه فنی را می‌تواند برطرف کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/691328" target="_blank">📅 23:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691327">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840966b12e.mp4?token=k9pqZZKiVSSGJazqGY-lo5WswS5_AtoSZui-ob2eotndBda8JGgG9OVuTvHbnwAq7cAoiSyBjuAxMzhHn0VrF0x_MWe1epq8PhI6MoxQlaSwq8rDLuMvUnKyzWW5CtKz7cv_hSffsnBcjYqTOgsUyU7wSmtjJckXw-3jn-m4WG5vRwoEsrMkhf-t1SmXxC46o3jZODuQfVhG9uDooCOOGH71dxXGpn4s_V0sqTPvYkN6a2TJ8oUce-o11A-afLU6iFwq1fX4SC3HjnTDYpDpsxzKFErASM9OjQEQIxq1NOkrqIa5FnzHBaxnjKVE9tO0RyKaK9GadiVqKRqDIp03OEAOv2ToErn5JXoP57HSr8SLihQyEvbo6aNPS6naa8rAzoFjfy6DfET50GJcav7YWcdx3OvoFmyWVMBCrTPZcd0lLETj7-nUzt8wgyHyfa5GNB42rdo8w1QXDuhx2NT17aghLTtTAGjJQ9N6i0VuBZSuT7PHGZ5PzfyLzKKwTCD8VfMoOsRyEi0vdDz8Gv06dVbrW3rsGBG6s0LHHw-inVep0AWfU5-fSVfd8u-w7a6GuHJFydzhCBBMevCQ-5tD6cHrmAMm7_VaPZ5i5r5-UfdlT9DQlifgR0EXKW-s4uYAzEr3zevH4dQFpkyz3TtWsVjkvDQHVqmeKrxrs_9Yyfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840966b12e.mp4?token=k9pqZZKiVSSGJazqGY-lo5WswS5_AtoSZui-ob2eotndBda8JGgG9OVuTvHbnwAq7cAoiSyBjuAxMzhHn0VrF0x_MWe1epq8PhI6MoxQlaSwq8rDLuMvUnKyzWW5CtKz7cv_hSffsnBcjYqTOgsUyU7wSmtjJckXw-3jn-m4WG5vRwoEsrMkhf-t1SmXxC46o3jZODuQfVhG9uDooCOOGH71dxXGpn4s_V0sqTPvYkN6a2TJ8oUce-o11A-afLU6iFwq1fX4SC3HjnTDYpDpsxzKFErASM9OjQEQIxq1NOkrqIa5FnzHBaxnjKVE9tO0RyKaK9GadiVqKRqDIp03OEAOv2ToErn5JXoP57HSr8SLihQyEvbo6aNPS6naa8rAzoFjfy6DfET50GJcav7YWcdx3OvoFmyWVMBCrTPZcd0lLETj7-nUzt8wgyHyfa5GNB42rdo8w1QXDuhx2NT17aghLTtTAGjJQ9N6i0VuBZSuT7PHGZ5PzfyLzKKwTCD8VfMoOsRyEi0vdDz8Gv06dVbrW3rsGBG6s0LHHw-inVep0AWfU5-fSVfd8u-w7a6GuHJFydzhCBBMevCQ-5tD6cHrmAMm7_VaPZ5i5r5-UfdlT9DQlifgR0EXKW-s4uYAzEr3zevH4dQFpkyz3TtWsVjkvDQHVqmeKrxrs_9Yyfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستین اگر آب هویچ یک روز بیشتر بماند، باعث ایجاد سلول سرطانی می‌شود؟
در این ویدیو ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/691327" target="_blank">📅 23:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691326">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔹
از داغ‌ترین خبرهای امروز و امشب غافل نمانید
🔹
🔹
ترامپ در جلسات خصوصی درباره جنگ ایران چه گفت؟
👇
khabarfoori.com/fa/tiny/news-3246285
🔹
استانداردهای دوگانه غربی درقبال اعتراض؛ از تهران تا لندن
👇
khabarfoori.com/fa/tiny/news-3245872
🔹
ایران برای پایان جنگ ۳ شرط گذاشت
👇
khabarfoori.com/fa/tiny/news-3246417
🔹
افشاگری تکان‌دهنده خانم بازیگر: ازدواجم با این چهره سیاسی دلیل خانه‌نشینی اجباری‌ام بود!
👇
khabarfoori.com/fa/tiny/news-3246265
🔹
دلیل حذف صحنه‌های جنسی در فیلم‌ها چیست؟
👇
khabarfoori.com/fa/tiny/news-3246406
🔹
خبرهای جنجالی هر روز را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/691326" target="_blank">📅 23:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691325">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/691325" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">گزارش بازارها شنبه ۲۸ شهریور ۱۴۰۵
ریزش عجیب بورس
طلا ۲۴ میلیونی
ورود پول به صندوق های نقره
@Titretejarat</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/691325" target="_blank">📅 23:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691324">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b0a0ab95.mp4?token=QnQHi2wDbtUU2tkbXb9Q-Xwxm8llvZECobUuaOZi2fBfWASTGHGdqGhN-pUt0tC3Kif24UZinqaDMhXOxBf8A4SAonOVIgKeJzM40iHaQz14KvvN2YGu7dk6NOyzHZUwqXoqLgi24XQjGfbpcT0MoXMyiZwzfH15OeI7FEDffuWq10oty0A_Gh3uFDc3J35Hg9d_AC8TLm8Wp3GypDWFD9mddn97osnj3uXCdXQU2Bv41rc5ziUM7X1g0R-Y7A6fpTBoDOCW69yj4G484Ic1VkPtsXeteFe6I3X7xTuY6i18Zk_3amS3vV7dokYNdqXR1zRFAVHPzD5ctAH_BNUNWRlAOlnM_JRo6p924ZIEHiWYIwqajrJUWJ4l5H4jTBpraeOMSp34RQ17tIYPzdzpPNKVt8F-jrZEG1Xh39KsvUt6oVp7PT0xT3rbvnDqrX6KVrBH9CutvJpqxjNX9E5Lu2gIQfSqHX_PqOvGngNafQj25A1oCY4pL3eqSwa8lrhUi91nuL-4vzFDdYy7RzNbDjRXa7c7iC4iO3yV-e73eqo2fdgIyWdtpqpPUf1IgY0S_WOXSfsJy2Ut1TMpFJu0LAYJlMsriDRgSfVLwRalV3uNEJqFtXdIyDH8ddmh8O4h0e1ndOaHgnDy80FHNi0tJ63e3MHlemGdt9sCRRvi0VM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b0a0ab95.mp4?token=QnQHi2wDbtUU2tkbXb9Q-Xwxm8llvZECobUuaOZi2fBfWASTGHGdqGhN-pUt0tC3Kif24UZinqaDMhXOxBf8A4SAonOVIgKeJzM40iHaQz14KvvN2YGu7dk6NOyzHZUwqXoqLgi24XQjGfbpcT0MoXMyiZwzfH15OeI7FEDffuWq10oty0A_Gh3uFDc3J35Hg9d_AC8TLm8Wp3GypDWFD9mddn97osnj3uXCdXQU2Bv41rc5ziUM7X1g0R-Y7A6fpTBoDOCW69yj4G484Ic1VkPtsXeteFe6I3X7xTuY6i18Zk_3amS3vV7dokYNdqXR1zRFAVHPzD5ctAH_BNUNWRlAOlnM_JRo6p924ZIEHiWYIwqajrJUWJ4l5H4jTBpraeOMSp34RQ17tIYPzdzpPNKVt8F-jrZEG1Xh39KsvUt6oVp7PT0xT3rbvnDqrX6KVrBH9CutvJpqxjNX9E5Lu2gIQfSqHX_PqOvGngNafQj25A1oCY4pL3eqSwa8lrhUi91nuL-4vzFDdYy7RzNbDjRXa7c7iC4iO3yV-e73eqo2fdgIyWdtpqpPUf1IgY0S_WOXSfsJy2Ut1TMpFJu0LAYJlMsriDRgSfVLwRalV3uNEJqFtXdIyDH8ddmh8O4h0e1ndOaHgnDy80FHNi0tJ63e3MHlemGdt9sCRRvi0VM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیدایش سالپ‌ها در اطراف قشم؛ امیدی برای بهبود آب‌های جزیره پس از لکه‌های نفتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/691324" target="_blank">📅 23:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6nFpgSHi7NEyRjBWUSqjXuBZJVpsCWGxx2ChODVKkEQzcJHAX0Qm7jaW3uhlBurOF-q69HPQPt8iDwu7PPXkrZLGiykuqfsRcQ8fU3wXix6QbyuWqj3t0fF_-bLBSdmMmpZKqhzXNxutHSd0b3PsJ7lFmGAtXxAsj-ogj9LaQVXfSg-IQ2XtPV_COgTqQM1NeYzXp1mGDf9Qq8BgApVVXjh5RsJUdk3Am4VWaPaSPlM4CSIjl8LKyXYB8II32NiSEieB8OO0MfK_3wht13gflpYpfYEgppGsGDt0LS5md4lzrsEBMmr7g1cvt-z7YNEDCc_mS1OmYBVAIrt1wTWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: ما با میانجی قطری که شرایط ما را با هدف توقف جنگ به واشنگتن منتقل کرد، در تماس هستیم و منتظر پاسخ  ترامپ هستیم   رضایی:
🔹
شرایط ما عبارت‌اند از: پایان‌دادن به جنگ در تمام جبهه‌ها، آزادکردن دارایی‌های توقیف‌شدهٔ ما و پایان‌دادن به محاصرهٔ دریایی.…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/691322" target="_blank">📅 23:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691320">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mawovho_-r6o9X5OuQlSjEatqdP4GXqTMA0HiKpwar4xD0_mwp4PM0YNjrNk-3focSIvpGfniQyiqKEbrwknA8LfRh289nj0KjloBTPrZYFrTHuYNMdRPC-RUNX0U9qxPNtpUIGzkAJeIUe7h3SugSkdB9Cz3hZ7_4EEs4lnqFq8B807nG8o2AkraVEVwnL0nGXP2x_w-YL7IQK-La1Npj2_2mizQYqVIaVHHMidb0WL_Q9dKCQt4T971_0F1vsd8ubX1uLq4jZWQVSYCZ0-73k5aBFnMq41IEZ9KUFrXEVH26aFBVeM3h8qwbJkVmTlNB523JiiUs6aBrKwmGPEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقایسه آمار حیوان گزیدگی در سال ۱۴۰۵ و ۱۴۰۴
🔹
میزان حیوان‌گزیدگی در پنج ماه نخست ۱۴۰۵ نسبت به مدت مشابه سال ۱۴۰۴، حدود ۸ درصد کاهش یافته و ۱۵ هزار و ۴۳۷ مورد کمتر شده است.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/691320" target="_blank">📅 22:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691318">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
نقض حریم هوایی محل حضور ترامپ در کمپ دیوید
🔹
هم‌زمان با اقامت ترامپ در نزدیکی کمپ دیوید، یک جنگنده اف-۱۶ امروز شنبه پس از ورود یک هواپیما به محدوده پرواز ممنوع، به این منطقه اعزام شد و این هواپیما را رهگیری کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/691318" target="_blank">📅 22:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691317">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0YuE91Xy-rSO-FaZCk7RFa1HIuk20qOabvQEoDftqEAUfZGKk_3H4kvZzDSSn8die8ZOK3Y25Fjz9QctpyfVhMvYsdAYmX59-JD_63RQ5O3Z-VpaDVJwtM93opUV7kvuAmHR8qgzHvyr3uOxlIRwW1Zr7giBNSTmjien9saI0Xkh8P7ywMY4qQMkCSpJ_u0uLwQ8CmRuqgOlhC75DOHAjOyeh7WiHughyG6G-MdFWuR9hDRH1T9d8l_tOzGUlBQrJiW1p0Qm5eMUPrBOYbrE6TsM4HnLpaBg2giMxTQIk1-6b-PW7Wu4FTYzoPjOz2S7CZYvZRyXO4L5F-D9GAasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثبت تصاویری خیره‌کننده از چشم‌هایی که در قاب عکاس ترک درخشیدند
👁
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/691317" target="_blank">📅 22:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691316">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: مقاومت تنها راه مقابله با صهیونیست‌هاست؛ سایر راه‌ها تلف وقت است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/691316" target="_blank">📅 22:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691315">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
افسر اطلاعاتی سابق آمریکا: روایت واشنگتن از عملیات نجات خلبان آمریکایی از ایران، ساختگی بود
🔹
برنامه‌ای که در این زمینه ساخته شد، یک اقدام تبلیغاتی و سناریوی ساختگی با همکاری وزارت جنگ آمریکا برای قهرمان‌سازی بود.
🔹
آمریکا پس از شکست در جنگ با ایران و عقب‌نشینی از پایگاه‌هایش، به‌شدت نیازمند یک قهرمان برای افکار عمومی خود است‌. این یک شکست واقعی بود که در آن ایرانی‌ها عملکرد بهتری داشتند.‏
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/691315" target="_blank">📅 22:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691314">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4363b66699.mp4?token=bx-jPNUzSvTgepQ9qAytlPOHePxGZSPJtRwnamhb6pPuavqaBQCVg42v5HAWNyhHkv0Fo56DCwDOcIaNvpJl_ho9HFDVLRyKhSdHcskk6maXvTsVgpeDTsRyjs6eIeqJfvG2pvWTHHb-2rAAZ3rVIQE0Sl-UzhE4aIWQ5N7SmzQXuHFOCICTVGlNJA1ycfXrld3ayIVus6fh3l-jIlHbmPGpEKTRo6spR3nnhLdO67pwCywQIgqlmHp_5SEzMqVIUUBoMbOdUyCHMK4ZDdIhUbNz7003b6lrwaVAcEl3nqhd3rPhJY2U_DQR4d0GwoOBuN36CFU7Knonsyx4ueFBrYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4363b66699.mp4?token=bx-jPNUzSvTgepQ9qAytlPOHePxGZSPJtRwnamhb6pPuavqaBQCVg42v5HAWNyhHkv0Fo56DCwDOcIaNvpJl_ho9HFDVLRyKhSdHcskk6maXvTsVgpeDTsRyjs6eIeqJfvG2pvWTHHb-2rAAZ3rVIQE0Sl-UzhE4aIWQ5N7SmzQXuHFOCICTVGlNJA1ycfXrld3ayIVus6fh3l-jIlHbmPGpEKTRo6spR3nnhLdO67pwCywQIgqlmHp_5SEzMqVIUUBoMbOdUyCHMK4ZDdIhUbNz7003b6lrwaVAcEl3nqhd3rPhJY2U_DQR4d0GwoOBuN36CFU7Knonsyx4ueFBrYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری محراب قاسم‌خانی از چگونگی دور زدن ممیزی صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/691314" target="_blank">📅 22:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691307">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2160bb83eb.mp4?token=FbVlObWZELobhJA9V4SIYLwEIYDCqmEgzxWeyU1JujKW_btzewfapce1SlztC_9aIV9ofV4pIR15Uon6BfhznIKHGbv_lBRwRR6TrV1-UwqnA8cHIuE8Ufzs08Hv1DD-HmP2Y5caVY0XjrwbFaCLKhYyB7aovMv6oR-O-rYeeeZ96UZxPD6VLhR3IPv1VeDZ4LKAxvriP_YupNJS-Fy1_QemzurB4otvbD009w1GhKkgfrx9HFd3dmPRL1Rdmbb9xjs3GqPPN14sCKaCrOcV46jFH6m9dEDroEfcQjQElO1IuENokkOHxE8IkpGPp-9kGZ_Nn2JVj3rk_OceDhK5dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2160bb83eb.mp4?token=FbVlObWZELobhJA9V4SIYLwEIYDCqmEgzxWeyU1JujKW_btzewfapce1SlztC_9aIV9ofV4pIR15Uon6BfhznIKHGbv_lBRwRR6TrV1-UwqnA8cHIuE8Ufzs08Hv1DD-HmP2Y5caVY0XjrwbFaCLKhYyB7aovMv6oR-O-rYeeeZ96UZxPD6VLhR3IPv1VeDZ4LKAxvriP_YupNJS-Fy1_QemzurB4otvbD009w1GhKkgfrx9HFd3dmPRL1Rdmbb9xjs3GqPPN14sCKaCrOcV46jFH6m9dEDroEfcQjQElO1IuENokkOHxE8IkpGPp-9kGZ_Nn2JVj3rk_OceDhK5dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ای که تو دنیا وارث حیدری
کی منو باز به سامرا میبری
تولد پدرت مبارک یا حجت بن الحسن العسکری (عج)
🌸
پک استوری کلیپ های ولادت امام حسن عسکری (ع)
میلاد
#امام_حسن_عسکری
(ع) مبارک باد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/691307" target="_blank">📅 22:34 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
