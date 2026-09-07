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
<img src="https://cdn4.telesco.pe/file/WhyQmDaD8UBl9Eq-I8gwlRcY7UCaVS_0dLOsIM1pqQG1Nc6Gklab_iG95Y0in9USfSwFFMn7ifOB_11i4U1_HtenDkt4j0fsoH2IQ_bRUjPpqizlqhp8bCEMDghDQy7go0CIc-ojG3C8N9zm7TuuxLUdSh0NS4D_yn92LlCkFDshFpnsANWftkpRPzKVgTANTnvQT0x93Epo8JQAVK3F8cE-q-tOrd08wjpwl5S62Q_XiGrai06kXSFqHhH_Kl8hMJF-m592oyF59biSndldKvWdIUuGxcgi9lDe4CYvIZcJHDHLQIRqmcoJb4TjCfUp5vgWJqhpLs612hdG4hGeaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 02:24:48</div>
<hr>

<div class="tg-post" id="msg-688069">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تولید و پخش پوشاک مردانه یاشین(فقط عمده)
✅
این پست مخصوص بوتیک داران و فروشگاه های پوشاک می‌باشد
✅
✅
پرتنوع ترین دورس و‌ هودی های سه نخ
✅
با رنگ‌بندی های خفن در ایران و بازار
✅
مناسب ترین قیمت و بالاترین کیفیت
✅
محصول مشابه خارجی
✅
لینک کانال تلگرام
✅
👇
https://t.me/Yashinshow
پیج اینستاگرام
✅
👇
http://www.instagram.com/Yashin_men
کانال بله
✅
👇
https://ble.ir/YSHCOLLECTION</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/akhbarefori/688069" target="_blank">📅 01:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688068">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076b9568c9.mp4?token=sBPAs2k_bYnepZyFJvh2VbHiJHV7nxb15pYtin8M8OjIxEwA5NWO0PDQKC2-Gw0eK5S95h4ZfkNw6VjbJ0ZzrQXolLjoUBhG7NENhD6rFCExBXXC8yUul8PoWO19eESRf_zft6Kd2WbWX8dl0_9b7crkkt2eKjiGz0WD8uuEb9sG3qXJY3jsrSLLeAlX1CnYDB6fTlH-nBmahCXz1Fr3WxPPAgc-qlMcWzGT_cU3jBVA0a9iyRgKzMOzhf2wS3mX5v3t6V4fivwaDGjHMYHjr0EuStkb8GrsDHbgIv0JQnoGs9WbjCQmxod_Je2syvMehDRCu53SFqy7hS3BgsiIxX9e-05QZW1e8d0WSPLWjP0SlFAP0K0ftuDEz380eIxYFtF0kvw7CGN8NOs8h269SVkbPdKB6Y-ZPPG1PqREKVMVaBBl7kCd6cgzuQqHc47fdUrCyRiKAGQF5oDD7HKd6yEiJEtQL9dkGZogjtRhzIiq2wi2R_lANQLT6mc4hsOan0JxgVomANNofuG0hnoXsVspMRaxmIqInl5fWEXh4Sz--A9VN2YmiAAxu5UGNNoe0qQYAi0RGR_8KmTDxNZ-NpPQrn8Y1BzlDUUvcnz73Zt9QmxlO2TRZxkGuH9d5oHSFB3ujKUqJsK2ruXpGkhlJh2bLmdAZwDXZdyqaIu1y1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076b9568c9.mp4?token=sBPAs2k_bYnepZyFJvh2VbHiJHV7nxb15pYtin8M8OjIxEwA5NWO0PDQKC2-Gw0eK5S95h4ZfkNw6VjbJ0ZzrQXolLjoUBhG7NENhD6rFCExBXXC8yUul8PoWO19eESRf_zft6Kd2WbWX8dl0_9b7crkkt2eKjiGz0WD8uuEb9sG3qXJY3jsrSLLeAlX1CnYDB6fTlH-nBmahCXz1Fr3WxPPAgc-qlMcWzGT_cU3jBVA0a9iyRgKzMOzhf2wS3mX5v3t6V4fivwaDGjHMYHjr0EuStkb8GrsDHbgIv0JQnoGs9WbjCQmxod_Je2syvMehDRCu53SFqy7hS3BgsiIxX9e-05QZW1e8d0WSPLWjP0SlFAP0K0ftuDEz380eIxYFtF0kvw7CGN8NOs8h269SVkbPdKB6Y-ZPPG1PqREKVMVaBBl7kCd6cgzuQqHc47fdUrCyRiKAGQF5oDD7HKd6yEiJEtQL9dkGZogjtRhzIiq2wi2R_lANQLT6mc4hsOan0JxgVomANNofuG0hnoXsVspMRaxmIqInl5fWEXh4Sz--A9VN2YmiAAxu5UGNNoe0qQYAi0RGR_8KmTDxNZ-NpPQrn8Y1BzlDUUvcnz73Zt9QmxlO2TRZxkGuH9d5oHSFB3ujKUqJsK2ruXpGkhlJh2bLmdAZwDXZdyqaIu1y1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
قبل از سرد شدن هوا، هیترتو بخر!
هنوز هوا سرد نشده و قیمت‌ها بالا نرفته؛ الان بهترین زمان خرید هیتر ریموت‌دار
HANDY HEATER
👌
✅
توان ۸۰۰ وات با گرمایش فوری
✅
ریموت و تنظیم دما ۱۵ تا ۳۲ درجه
✅
تایمر، نمایشگر دیجیتال و خاموشی خودکار
🔴
قیمت 1,798,000 تومان
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/35574/180124/</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/688068" target="_blank">📅 01:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688067">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhwOiGfAYOHMUvHco1tcB_Do7vAwkKhwsJHDi2RDbFuUXjXRs_yAE838JcU0ro2nXXn-kraR5P4Xe7D-KEgx_nw0JUon2HpbyWnwLEGelmjqhRAwfqji2V_ZTvhuEjVw9wlsUxFzX_pEu9qdb8gYR4xp6beIv2KBR8xCIyS5Ez1wLl1R_1l1DWwlcb2QiyVf_C9RWE8AGtWvyTdGRx9uwZp7_MUfK7H5_AGx1LADloXf7xpiDZwMkv0XUqwRRLZSGhbfqlMExGjRddm5-4Nm8RiIHaoRcsaHvcxj6l32oBnfCoqPCpUuJ73g_o27caSjJDlFjQ5zhqrafVQf6KQnJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه می‌تونن با AI محتوای قشنگ بسازن؛
اما چرا بعضی برندها با همین محتوا
می‌فروشن
و بعضی‌ها نه؟
چون امروز مشکل خیلی از برندها «تولید محتوا» نیست؛
ساختن اعتماد و تبدیل محتوا به فروشه.
در
Digital Cast
درباره چیزهایی حرف می‌زنیم که محتوای برندت رو از «فقط دیده‌شدن» به
اعتماد، اعتبار و فروش
می‌رسونه.
اگر می‌خوای بدونی محتوای برندت واقعاً چقدر می‌فروشه،
کانال Digital Cast رو دنبال کن.
👇
🔗
اینجا قراره درباره بازاریابی، محتوا و فروش، متفاوت‌تر فکر کنیم
.</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/688067" target="_blank">📅 01:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688066">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dd2a8dfb9.mp4?token=h6GTlWYdNLT1WIuh_hCOKyG_iJbVZVlupD4jSGf2h_3ymnYDPv1PoxDfrUl55MqO3UU1g-aUfRA1KMj8r4Dj6wV78yLE4a4wM8e9MsIYZ2nIelGCkE3dBgy62fJApYGnP75WHrSPAvtJTHIDcFoLikMOszS21WRfaHwzjpEeawRSL25I-rE65cAtP_f6tXY8a_QOpqb7WTzyeTlvbmz9jO6f1xVipOEjuqiHeTsxu1y_g2Fklcogx6H9a5fmYU_nlwGGQ7qG0wa8mjYw2fkLqVaNIQMDHKiAaYW-uUhhoqRUlhpQEv8unVVNEph3si-Oelpq1eN87FBxheFInNfVDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dd2a8dfb9.mp4?token=h6GTlWYdNLT1WIuh_hCOKyG_iJbVZVlupD4jSGf2h_3ymnYDPv1PoxDfrUl55MqO3UU1g-aUfRA1KMj8r4Dj6wV78yLE4a4wM8e9MsIYZ2nIelGCkE3dBgy62fJApYGnP75WHrSPAvtJTHIDcFoLikMOszS21WRfaHwzjpEeawRSL25I-rE65cAtP_f6tXY8a_QOpqb7WTzyeTlvbmz9jO6f1xVipOEjuqiHeTsxu1y_g2Fklcogx6H9a5fmYU_nlwGGQ7qG0wa8mjYw2fkLqVaNIQMDHKiAaYW-uUhhoqRUlhpQEv8unVVNEph3si-Oelpq1eN87FBxheFInNfVDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آبگرفتگی شدید معابر رشت| هم‌اکنون
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/688066" target="_blank">📅 00:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688065">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
فرماندهی مرکزی ارتش تروریست آمریکا (سنتکام) مدعی شد که نیروهای این فرماندهی همچنان به اجرای محاصره دریایی علیه ایران ادامه می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/688065" target="_blank">📅 00:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688064">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95337866b2.mp4?token=lBs5i1f4-qAi9kVofb6yllCbLJEVxwB2oEoUpyLENQC3GcKHqG4SW1mlTea6dj1YIpxMTQPajCR2saABeGrb2alYKqvmlgWTwvd__1YLeWDhDdDvxQLyoAl5RJz0-QrHlAeTnIuWp0DqhKF0FAj4hZ5RiteRBCFqD0XdMZS1PBxVWCg8Uc-qpIjq_MOaACktmKvDrMzuH4C0LJOtjLAZpfX1rgK5ILwDtWVV4w7iQhiJ7ddpYOQKinZPMz-LgQ5B36V3_ZMPAXZyMUp1sak1FY4umeZ6MR1WPPJAn_vEuH7KbI5Kf8dBLI7nNK9SC5511mnT5xVXQ8IWkCztxgypGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95337866b2.mp4?token=lBs5i1f4-qAi9kVofb6yllCbLJEVxwB2oEoUpyLENQC3GcKHqG4SW1mlTea6dj1YIpxMTQPajCR2saABeGrb2alYKqvmlgWTwvd__1YLeWDhDdDvxQLyoAl5RJz0-QrHlAeTnIuWp0DqhKF0FAj4hZ5RiteRBCFqD0XdMZS1PBxVWCg8Uc-qpIjq_MOaACktmKvDrMzuH4C0LJOtjLAZpfX1rgK5ILwDtWVV4w7iQhiJ7ddpYOQKinZPMz-LgQ5B36V3_ZMPAXZyMUp1sak1FY4umeZ6MR1WPPJAn_vEuH7KbI5Kf8dBLI7nNK9SC5511mnT5xVXQ8IWkCztxgypGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پل سه بلوطک، بلندترین و طولانی‌ترین پل  کابلی ایران
🔹
شاهکار مهندسی بر روی دریاچه سد کارون ۳ و رودخانه کارون؛ در مرز بین استان‌های خوزستان و چهارمحال و بختیاری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/688064" target="_blank">📅 00:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688063">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای سنتکام: از زمان ازسرگیری محاصره دریایی علیه ایران، مسیر ۹۴ کشتی تغییر یافته، ۳ فروند کشتی متوقف شده و ۲ مورد دیگر نیز مورد بازرسی قرار گرفته‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/688063" target="_blank">📅 00:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688062">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/830d0d3599.mp4?token=TTxSK-hOwcMnnZp35L8Y9RR2jfpMS7BmEBbhLO7HLPMZ1pgCtHADCOlxeIa0MbWNm0mY9Tw2FcTqhK7YxHZAjqYTACS7USzYR3yhTSHEK768iNWUP6pe5YYFPghou96CeLd7Zyu3plZ6o5XREid27X76jApMIwVBNK6ebYsP6odRNMGkrqBqn9GufRVq5q64x574wdTCoYXUXyG9tcnaq_3X5aqbYtghZKMNjbp9N6Qy7Q5cbWEKHw-mrRrlln67rWAu8LIbBay0aYARsd7QVn_2BPbCYR4-XZkojUCFgC4xoCkX-QwbAmdgMdyrZNDeNTeudcsSJLfvlEN6EkSJRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/830d0d3599.mp4?token=TTxSK-hOwcMnnZp35L8Y9RR2jfpMS7BmEBbhLO7HLPMZ1pgCtHADCOlxeIa0MbWNm0mY9Tw2FcTqhK7YxHZAjqYTACS7USzYR3yhTSHEK768iNWUP6pe5YYFPghou96CeLd7Zyu3plZ6o5XREid27X76jApMIwVBNK6ebYsP6odRNMGkrqBqn9GufRVq5q64x574wdTCoYXUXyG9tcnaq_3X5aqbYtghZKMNjbp9N6Qy7Q5cbWEKHw-mrRrlln67rWAu8LIbBay0aYARsd7QVn_2BPbCYR4-XZkojUCFgC4xoCkX-QwbAmdgMdyrZNDeNTeudcsSJLfvlEN6EkSJRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه تغییر قیمت بنزین از ۵هزار تومان به ۱۰هزار تومان
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/688062" target="_blank">📅 00:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688061">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzzGi-mW8Nr7Pl_zD0Y7qKZGk_pHaLtCbDEfkgV62f_wQJs61hHl-Cv-3uwyLFXCkj3RC9WK0x9tqhj1fKc2wW0wrynRB9TrajWdcCulpgiBiwArLLWRWBOxaRnYGpJTg223_01La3p-QVCrsCaTb0aZEgZde1Www6nwEa7Uub-JGGKFy4ZTWJ7_8oq0Pm6FKPGF36Tkfo1oBr-ckt9QqRcEZjhPCwJwWwmMGRZ_K8bnOXrZOKFX7M3bObirl_un-grYcYUtZl_JanYvrbmDT4STSMDrQL_MCMknW8m9ZVHmL4bBpL_-DupIDIeDpUFDd8IZdrwdrKxlgyyrpNJHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناتانیا مارشال، فعال مسیحی آمریکایی: چه زمانی رئیس‌جمهورهای ایالات متحده به اسرائیل نه خواهند گفت؟
🔹
پدرو سانتانا، یک فعال دیگر در جواب: آخرین رئیس‌جمهوری که به اسرائیل "نه" گفت، در سال ۱۹۶۳ ترور شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/688061" target="_blank">📅 00:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688060">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
خبرفوری| هم‌اکنون نرخ سوم سوخت از ۵ هزار تومان به ۱۰ هزار تومان تغییر کرد
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688060" target="_blank">📅 00:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688059">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyQNYV4c-GI_I5SbvZbZjJDthW7dB9oUofvqaSLGP65M84_ZdpYJ9BJvoAt_vFXVv45ecknxeaciiuWjBkpyg3Ey8TdHETw2iRTNaMArqiLplXzBd2RanLpVGj6KO9ONxAYfiNDg1qlK_QtHmSgkGlhpId5xuc33EEgVbNj5i_E46Fff35j0BOMxyD83mgJjbgbVICIrLAGa8eoEWaXEJHMSdTN6uMvziHeftX0jWBEKQWLfHogfdPOZAmHD2kTqw3zg3fCGm9RqDjNWAVsSc0SOqxI_C5AImzSGjyBqLlbx9HRBJXzxL-Lb8kGVxzcLyOc83yMfxQbt5gwCE7LDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/688059" target="_blank">📅 00:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688058">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqFEuppuUGaO3W4L3cRcs3tw3HcdDayXrXYdggxdsk_4ESZfFifXvTi8H9XCA1XOL4QoWJHCdrC3gJm3cHtaQKsbOlPWRXGLpkTW6nLzg_vJlg3sDN7_SxUxL8j-obtF_oxro3B5Sn3pJCBxxRUXXA7shRB8_SOhnxgtFvZDz5TmfyO7FP6jyIvJg41T8qeBMOgnNlcAG0nGTnRGoR5t9lsKXH3XMWTKzFV4f_hAcQtK6jDqGv1ajMwzagthw2l_KinQv6muowmasZLNiWcMCQPjYuhSRGagJ0E___NBHTH7p4YihVR4mCtCcOHyP5ySJoYLEenBUVHFAr5xxmuXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای آمریکایی: وقتی کسی می‌گوید خدا به او گفته است که یک نفر را بکشد، ما او را روان‌پریش می‌نامیم
؛
وقتی یک ملت می‌گوید خدا به او گفته است که میلیون‌ها نفر را بکشد، ما آن را اسرائیل می‌نامیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/688058" target="_blank">📅 23:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688057">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6706132e.mp4?token=OlbJBk5KTDKUVMKYdBOaNCAmHKGf6-mmMupH_z-r8BvVslgOwVcB_EtzHWUat3ruq10mQ4lTqoHEpVkQkXmvpYqQYFAeG2EjPiBQcNq4AWVngikvUR4YyRK_4ybiO__hC3NChk4qNBzAGNlwBuDjaIvokeeY1jiezWWgqijudD7S-Kv2FP-bS_06UuQndU-ec5WMenb8hmLqnnJqHZaTlYqAArmXMeuX51YOo-H9ccAQ9JKXXXadCrbQ33Yc-HuNOJLpy5iS4JjJ_PiqadQeX8mq7beBsI4fUDvBjdpzsZuZM_uqxTTyoIyU0kbA5XBdz_YS6Z3Vt3sy5isVsxzEcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6706132e.mp4?token=OlbJBk5KTDKUVMKYdBOaNCAmHKGf6-mmMupH_z-r8BvVslgOwVcB_EtzHWUat3ruq10mQ4lTqoHEpVkQkXmvpYqQYFAeG2EjPiBQcNq4AWVngikvUR4YyRK_4ybiO__hC3NChk4qNBzAGNlwBuDjaIvokeeY1jiezWWgqijudD7S-Kv2FP-bS_06UuQndU-ec5WMenb8hmLqnnJqHZaTlYqAArmXMeuX51YOo-H9ccAQ9JKXXXadCrbQ33Yc-HuNOJLpy5iS4JjJ_PiqadQeX8mq7beBsI4fUDvBjdpzsZuZM_uqxTTyoIyU0kbA5XBdz_YS6Z3Vt3sy5isVsxzEcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار ابن‌الرضا، سرپرست وزارت دفاع: توان زدن ناوهای محاصره‌کننده آمریکایی را داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/688057" target="_blank">📅 23:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688056">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
پزشکیان: از هر چیزی که حق است باید اطاعت کنیم، نه اینکه هر چیزی که منی که رئیس‌جمهور هستم اگر گفتم دیگران اطاعت کنند
🔹
گمراهی از جایی شروع می‌شود که فکر کنم منی که رئیس هستم هر چیزی که می‌گویم دیگران باید اطاعت کنند، انحراف از اینجا شروع می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/688056" target="_blank">📅 23:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwdadbwpKbD_mpOR2hDl5Ibfukl9HZDYDVaFycdTF3WGOmlSMAl50T7v0EYjwbk3xxwXZDclmbnoVoBXq1iF7VjNLZ98zmDRd_r049EINqDG0hnCDFLHfbHqUFjVVOuVT263rGEtKm6nwanMzFNqDpjujZsAW6IIpiDD3-s2uO6d9D2uQkC-THTnD-eFI1dgiMWzYqsYVCCMkXKEmZsFGi-D4_uuD7Q7yEp8R1COouKhgMunwCCW7kfCUaLFcs3bxndwdLJWvrAiGIUoAMkYp0OgaaIeKb__Goz8cHsElCAtJfRxixrDAETDOzahkvTeTQ9r_VOE9_HfLyZC6HbvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4k1PECpJME-thp6PpGWB6LLGCINaHd--gnMQUYNzt40qJs91Wa-oKMpCSr7HsANoIGmUWwZuOvrFPCFWAxwIqLlmOOpffykkQJIZhWodPU6mULNPIXSnmq-3qcC3ZCzG6nbE3PRgyZTt7SMXdMXi_VQ1jBeXRhhBE8XKl_35MO1wtb266RthiUKisXBvNwLDvcTy-QPDdOPWyC2TnAIxrJsalEM2QEy6aaTTbCtRj_u5xvQaMj6us9fJLJGBM4nZ8x4BNvBfM4vOl1GvAZXv8BJ5xwIAaHOJJKm2C0DNnHByr9St29gv9p6EhNPcV2gmBVcA9r5GRO-rv1eUveoMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jC3rlcrketwyZCgOI6GuEpA2WyWuw5R5u8cSwr7Hf-xls78hmOAb2Q5hFBNDHh9ikupYkVdYAWOSyq98isXCmZxcaD4XLXWKB5Ao9edkM_SrNsoytPNRviV-D9RpulOVKhUeSwHwZjzq8rjhhN971sVdmW0fc8hOceL552jk7fAm_1dqNMfBoPg_335tfR5a8FWMXBjC3TusdhPRbUC2MICmq2R8tJxcini07oM-vTAFzkLoOE2Xl3_Z1DNtDyU-vri5UKza-biX-Rh9LggSsdJQFrn-twkX-NgHj56O7WAigldInjLdHNEmZNyKaWZz0_9JUMuAoPnXHApyE2Hbsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منظره غروب ماه از قله دماوند بر فراز تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/688053" target="_blank">📅 23:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiPk3WcKj3P5ZqXKt_9q__5VOLBqj_gQaFKjuFfc2vdEcP7JhFQq77AMsKwZOuonbtChkGIDGCPbx3dCKhSetdAj6iu-hsGQSkVP2sOAL-2gt-HWAyl8J4tekeHq1Ypwo4pX5gBr5RjCQacO9jRTmkvSqfjVIEHVQoWkV4o2eGIGwqbOtxjcUAPer84qJ31qd4qsIDBsSK4aHA9sWwcyVu7MA8U6k7b3ihB4QCwiYdxm-OUzOh9n89igbekc9DAlCkqjhu7aSw-4jEZd7eVPpdA7IVKmndtaKA55j7kLlChQTJ6_jiUHOxv9JJOmGp86qDWi_XvofpAiynBM8LFoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه آنلاین یمن
🔹
مناطق قرمز: نیروهای انصارالله؛ هم پیمان با ایران
🔹
مناطق آبی: دولت فراری یمن؛ مزدور سعودی
🔹
مناطق زرد: شورای انتقالی جنوب؛ هم‌پیمان امارات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/688052" target="_blank">📅 23:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
عادل فردوسی‌پور: خداداد عزیزی احساس می‌کند کسی باهاش کاری ندارد!
ادعای سخنگوی هیئت مدیره تراکتور درباره عزیزی:
🔹
آزاده‌ای که حاضر شده خودش را فدا کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/688051" target="_blank">📅 23:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4bedf3511.mp4?token=RGSoooA_9XP1x9GFAhlf14KWeXgDhYpFKlL5ATV1khVs2LtIRRP2P4AIe9_ktc-H4_YlTO1SE9I_e_ZWhS71dGnSBN7vK6Z1xPnsZdotknUf0wZjXxwbKITmplFrssHe6oc6K3hQZPqOIiAi0cm5_CsoAUDapYFzNTHovUx8ZJeDxrSyehL_l4Q3T3g_TOj19MMIkhiFYBpfPtRvpeoWcfCd27lL5KZEcTKBHs7-hdM3Mz34bYNc1lXO5w_C0Fhxi8BCBrlSg7-xp6ApNhGptLbgzNr0MXR_Sgke-jZ21K1Uw6cZ5WHfJ1CHO_amRiq3JUlB7BnZRBSgGgcq6im-gEHE1yvTXp1ak2NGUE_QSDxnB54p8iZTwikxPdHBa2Pcu8IowC4m2FiFLSnGm_iIh1S8L1rz8B3bNOKm9QnTQfjlQCWrmYehBwfGcweqjoH4JGE2YQH5T7DSC2TXe5boeG4S27SS2fETddyvUR-K3JuTaOSsyGMhkZg0xFsTlLJhrdnyPpTXclGwbQuubjlX3bpZrjfv0j7raPmNAbYoTuxEQf8AySK_gJlnvSVkAlPuZ9nZRwWbFhV0bPPULbNjqHlyuadk5sPB1e058FEa7PGbwY4zxzKlH2NHKEFAU8A-6ctf0pkY-2LZcpLsBM4Vh6334tAkLK9UbrUirz9-6WM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4bedf3511.mp4?token=RGSoooA_9XP1x9GFAhlf14KWeXgDhYpFKlL5ATV1khVs2LtIRRP2P4AIe9_ktc-H4_YlTO1SE9I_e_ZWhS71dGnSBN7vK6Z1xPnsZdotknUf0wZjXxwbKITmplFrssHe6oc6K3hQZPqOIiAi0cm5_CsoAUDapYFzNTHovUx8ZJeDxrSyehL_l4Q3T3g_TOj19MMIkhiFYBpfPtRvpeoWcfCd27lL5KZEcTKBHs7-hdM3Mz34bYNc1lXO5w_C0Fhxi8BCBrlSg7-xp6ApNhGptLbgzNr0MXR_Sgke-jZ21K1Uw6cZ5WHfJ1CHO_amRiq3JUlB7BnZRBSgGgcq6im-gEHE1yvTXp1ak2NGUE_QSDxnB54p8iZTwikxPdHBa2Pcu8IowC4m2FiFLSnGm_iIh1S8L1rz8B3bNOKm9QnTQfjlQCWrmYehBwfGcweqjoH4JGE2YQH5T7DSC2TXe5boeG4S27SS2fETddyvUR-K3JuTaOSsyGMhkZg0xFsTlLJhrdnyPpTXclGwbQuubjlX3bpZrjfv0j7raPmNAbYoTuxEQf8AySK_gJlnvSVkAlPuZ9nZRwWbFhV0bPPULbNjqHlyuadk5sPB1e058FEa7PGbwY4zxzKlH2NHKEFAU8A-6ctf0pkY-2LZcpLsBM4Vh6334tAkLK9UbrUirz9-6WM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای بنزین ۱۰ هزار تومانی به زبان ساده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/688050" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688049">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
انصارالله با پخش این ویدیو اعلام کرد چندین کامیون حامل تسلیحات عربستانی که در راه ائتلاف در یمن یودند را در مرز ودیعه شناسایی و هدف قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/688049" target="_blank">📅 23:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688048">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHUyYquEKGBQb7-ghAqR_01iB2dFnfSnZnrXrhqmjTzE5ZX0iAvL8byQpZGfGDVRaveVk9XxJ85ylwPLWPha86UO4dJlzDg_RBIY5VsXMNCmDuCKNNnoQONbdjxvTqodCbGW_bMesHJhaCQnF8xEcj0b2sEHfFCdv1r2x-4b6eUdavOPJDRTSwV1nEisodwGWtloc-q-ytMx5h1HohjzTfCK4RTdPdFPSpa1p7FRVsSteFMLuUFBn0dqvsYp1wl7Vsl4In4C1QU9LirHFlaEnx9o7DwtXsT3UCX96PJB1ukQPYDp5HdzppWRw2DgekdakoSWj45hEKzBFaW3Z0R45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیر تا پیاز سوخت‌گیری با کارت‌های اضطراری جایگاه/ از محدودیت هر بار استفاده تا اعداد جدید روی نمایشگر پمپ‌های بنزین
در خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3243535</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/688048" target="_blank">📅 23:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688047">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
قبایل جوف وابسته به انصارالله یمن با یک بسیج همگانی به میدان آمده‌اند تا مزدوران تحت حمایت عربستان سعودی را عقب برانند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/688047" target="_blank">📅 23:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688046">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
زلنسکی: آمریکا به‌ دنبال کاهش تنش روسیه و اوکراین در زمستان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/688046" target="_blank">📅 23:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688045">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
اعزام نیروهای باتجربه تروریستی از جنگ سوریه به یمن برای جنگ با انصارالله
🔹
درگیری‌ها در جبهه‌های منتهی به صنعا تشدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688045" target="_blank">📅 23:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR9JvRnO0ThKdgBxOODVCrKiO9Nj87Wvscsfor8lujXLZNDiZCvf6CUzNOKplZy0rPkaVPrvDxr4ZNMJce7N8z8KPd5OhZPpAlQuhhbWmtqES2V2EX4yMbWGsJMfJxh6j9Txa36BnPjpz0f-gvHGSqAIOpfuVCw5g6SMtaT850dGIFaNKkAS6JKZlkLQyiKRkltLIvdcSg5BmvBE1Zqqzv6Io-Gy2b-grheeVpdm3i1q4Sq7WgQQ2VCa-PnyJJosQ3_n28W4-PMisH9sEe2DfxeeOgfPYryhFGxEL4bAfg6MCYXD1GYIFlvJFi6nDsds8px_5aSoEAjENP-A2XKSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر اساس گزارش گلدمن اگر حملات به کشتیرانی در خاورمیانه افزایش یابد، نفت ممکن است تا سقف ۱۲۰ دلار در هر بشکه صعود کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/688044" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
قیمت گاز طبیعی اروپا امروز به ۹۰۰ دلار به ازای هر هزار مترمکعب رسید
🔹
قیمت گاز در این قاره قبل از آغاز جنگ ایران ، ۴۰۰ دلار به ازای هر هزار مترمکعب بوده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/688042" target="_blank">📅 23:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688040">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
نقشه شوم آمریکا برای جنگ با ایران: واشنگتن برای حمله منتظر انتخابات نمی‌ماند
👇
khabarfoori.com/fa/tiny/news-3243473
🔹
در کشوری که با کمبود مرد مواجه است؛ زنان «شوهر ساعتی» اجاره می‌کنند!
👇
khabarfoori.com/fa/tiny/news-3243120
🔹
اگر سهمیه کارت شخصی و کارت جایگاه تمام شود مردم چکار کنند؟
👇
khabarfoori.com/fa/tiny/news-3243324
🔹
هر گرم طلا تا پایان سال چند خواهد شد؟
👇
khabarfoori.com/fa/tiny/news-3243404
🔹
پشت پرده حمله به انبارهای سلاح تروریست ها در عراق | حمله پیشدستانه برای خنثی کردن توطئه نتانیاهو و ترامپ؟
👇
khabarfoori.com/fa/tiny/news-3243484
🔹
صفحه ویژه اخبار پربازدید وبسایت خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688040" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688039">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ایران: آمریکا و رژیم صهیونیستی اساسنامه آژانس اتمی و قواعد ایمنی هسته‌ای را بمباران کردند
🔹
جمهوری اسلامی ایران در نشست شورای حکام آژانس بین‌المللی انرژی اتمی با محکوم کردن تجاوز آمریکا و رژیم صهیونیستی به تأسیسات هسته‌ای صلح‌آمیز و تحت پادمان کشورمان تأکید کرد که متجاوزان با این حملات، منشور ملل متحد، اساسنامه آژانس و قواعد بنیادین ایمنی هسته‌ای را بمباران کردند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/688039" target="_blank">📅 22:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688038">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntl_WrUqIig2B_JtwKPlY-x2W7Xd5jgPQzILGkGNYYMkCqoloF-L-35fjZTm45i82SSo-cQKvTDy8_rwc-as6X9Kgybmu0z0O2YqmCe93Ovyh9006gH0fLPD-Z8xJJo_kBs9-odaxbK6OOwBN77dH3qVh6gGFB_prgkiTwH4cwVtnAc_n_zjKrEudFB9nLUKXL4ADELxQVRD0YOQxkD9BduMHLkhBSmMcpCTXGN8yB77C5a-KfH5s5nSAeuexO_a0f9agFeZKyYD5mAQo5u9xUDPUbLREJmRvqM87qD0femYjtnb1Eku1RlghqdhXX3b0dQxRt4uZVMcuGjevpfoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تولید هر خودرو در ایران‌خودرو حداقل سه‌هزار دلار و در سایپا دست‌کم ۲۵۰۰ دلار ارزبری دارد
🔹
یعنی برای تولید هر خودروی داخلی، به علت وابستگی به واردات قطعات، حداقل ۵۰۰ میلیون تومان منابع ارزی مصرف می‌شود.
🔹
جزئیات آماری نشان می‌دهد تارا اتوماتیک ۴۵۰۰ دلار، شاهین پلاس ۵ هزار دلار و ری‌را ۶ هزار دلار ارز مصرف می کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/688038" target="_blank">📅 22:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688037">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e682bbd6b.mp4?token=nVs8q592KBSAgtOLKcibHUfKqdft4ZGu1kkgUkpc2zrWeutRlJ07EwhUPuoh0DupSteNtYxo4RFbUJnzjctqh2hgzkPHwtQ-IjFhLeB2gehRybn2Snv9QEbCLuv36MPdUd4Fijuv6iwBkxGLuEm6QD9sQdVx4l9oQqt8ZwOjL4GZfQ7I82L5zmwC5Dt8NAUAB03usW12UZ1t8ha7cOwXHyf_C5e_MWfdONHkasQ3s4IbhiFB0kLnrzstcof0KXcaz8OD1QFtmL0Ks3vUxHGV4_Nt-AhS1F-gP0Egu9vRVIAi4M4izd5HhWr2kgtZaeTaxt_byGPm8jmfRd6mPE_HVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e682bbd6b.mp4?token=nVs8q592KBSAgtOLKcibHUfKqdft4ZGu1kkgUkpc2zrWeutRlJ07EwhUPuoh0DupSteNtYxo4RFbUJnzjctqh2hgzkPHwtQ-IjFhLeB2gehRybn2Snv9QEbCLuv36MPdUd4Fijuv6iwBkxGLuEm6QD9sQdVx4l9oQqt8ZwOjL4GZfQ7I82L5zmwC5Dt8NAUAB03usW12UZ1t8ha7cOwXHyf_C5e_MWfdONHkasQ3s4IbhiFB0kLnrzstcof0KXcaz8OD1QFtmL0Ks3vUxHGV4_Nt-AhS1F-gP0Egu9vRVIAi4M4izd5HhWr2kgtZaeTaxt_byGPm8jmfRd6mPE_HVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات معجزه‌آسای کودک در تایلند؛ راننده تحویل در آخرین لحظه او را از زیر کامیون بیرون کشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/688037" target="_blank">📅 22:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688036">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d607a02a97.mp4?token=hYiMuZ_Nft7DN4wid6uVdH2fr_f4lXNR1GY1_qr5tDM_YCSwf2PJFI0qclPYY93a7jJTwn1GfRBKtSRzIAi4y4jDjIlzAetbZLLfYM4tvLvd68EDeNAL80B-O0m2HV65fJoXmNiNoOLYSNm7BtkZZioX512HwQ-Yt2isZq973lILVoIjl9GURFgx697kmusvMTV3D1fs8jyASRU8g0QLBs71_nPQbhZJnkffwnHJ1JbvMj-TQwXK7wVqKgrtdtCHwA6FtjT4WN2MWeSHXH8-Jn4NOzexKXR1clSRP6K-wnN3EaUizeUJPKVsrP1uqiura_7TL5L3jZQzRuvQ1XTQLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d607a02a97.mp4?token=hYiMuZ_Nft7DN4wid6uVdH2fr_f4lXNR1GY1_qr5tDM_YCSwf2PJFI0qclPYY93a7jJTwn1GfRBKtSRzIAi4y4jDjIlzAetbZLLfYM4tvLvd68EDeNAL80B-O0m2HV65fJoXmNiNoOLYSNm7BtkZZioX512HwQ-Yt2isZq973lILVoIjl9GURFgx697kmusvMTV3D1fs8jyASRU8g0QLBs71_nPQbhZJnkffwnHJ1JbvMj-TQwXK7wVqKgrtdtCHwA6FtjT4WN2MWeSHXH8-Jn4NOzexKXR1clSRP6K-wnN3EaUizeUJPKVsrP1uqiura_7TL5L3jZQzRuvQ1XTQLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی پسر‌بچه مهمان برنامه محفل ستاره ها به آرزوش رسید!
🔹
اقدام جالب فرمانده سپاه گلستان بعد از دیدن آرزوی جالب پسربچه گلستانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/688036" target="_blank">📅 22:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688035">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3ca54a33.mp4?token=OAnhspwoGzdG5BI9eNuL-Be7kHr0nbHpS4sjQ39TcJmEC1qtfAQt99I9D6lwlwpSUJfUWnrgOGpKpy6v6cqVrrQvwhQztz8zwnyZcGKx0uzQQGzTUndNgXCG2lhLSi64n6R1iLcCKGsPVzFFEh1-_hv3TkyTjrVPutth-2ezt3D-05Jb-ydYQcLI0BlP3OecWVkwaPr6oLqhwG8YtI2r6QPkocvT8LnxoJHbiKYBX4E0Bi4Z6V6c298FsSWbpCXmftBvwevf3zZw2olDJ7FEJIjtyL_fztcbXZyfhaZyhrezkvX1an4Zk3du3ZJBCkd8zv4Ulqxoc8EaTgS0yZ9uTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3ca54a33.mp4?token=OAnhspwoGzdG5BI9eNuL-Be7kHr0nbHpS4sjQ39TcJmEC1qtfAQt99I9D6lwlwpSUJfUWnrgOGpKpy6v6cqVrrQvwhQztz8zwnyZcGKx0uzQQGzTUndNgXCG2lhLSi64n6R1iLcCKGsPVzFFEh1-_hv3TkyTjrVPutth-2ezt3D-05Jb-ydYQcLI0BlP3OecWVkwaPr6oLqhwG8YtI2r6QPkocvT8LnxoJHbiKYBX4E0Bi4Z6V6c298FsSWbpCXmftBvwevf3zZw2olDJ7FEJIjtyL_fztcbXZyfhaZyhrezkvX1an4Zk3du3ZJBCkd8zv4Ulqxoc8EaTgS0yZ9uTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی زیبا و دیدنی از یزد
😍
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688035" target="_blank">📅 22:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688034">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
عامل ضدانقلاب در ایست و بازرسی هنگ مرزی ارومیه دستگیر شد
فرمانده هنگ مرزی ارومیه:
🔹
در بررسی‌های انجام‌ شده، هویت و سوابق فرد مورد نظر بررسی و مشخص شد وی دارای ارتباط با عناصر ضدانقلاب و سلطنت‌طلب است و تبلیغ جنایات آمریکا را در فضای مجازی انجام می‌دهد که بلافاصله توسط مرزبانان دستگیر شد.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/688034" target="_blank">📅 22:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688033">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8NLu1E_GHglL-8nVS9U8cdsc1xI-fgMi1fwmBtMYuNQFnNSG14oc4ubqBEaWZmGkxjv2W6el8VoK76_JkzDrbMMane44xoFeQtzaGaWYoYNrZBL_H4Hm0cwq-aqajQWZmN6eJ4dfJdWBbciawE2gjbHRPjX9FZNyWxczGfR0EkYfSpW1TEYzgjzJ1Axu28hS9X61slCaeSj7cmFy7-5tv8KPqmxQR-JUz05e7CK_uYLR73f6jiaA-iigWY9XyrAlbnGJXnPIB23GVjS4tAiPImuUYsSnkWLa7O1enrH4kSqqGPR9YaklknTmCxjalWO9xLwmmJsrKZA5A8mfHYNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/688033" target="_blank">📅 22:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688032">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DV1T9G_6S9k1FLU6tKdjsYz5TP2tRYhMs7s2BlXXkDZ3EEnYgHX9-aSwKfmieSq8arXg-fA-_-CV3nzsn7gojteJijiftD-MQufAjqDOnLI083jb-bCfcNJiiTq9gOVXgqrhc_1upePYNPnrMdw6uqtoul3U3D3s1civqFVioptk6jy1mSwU7i59tWWgui6KqI8OA2n9Cr6qqwzJyMZb0nFiMAF6_0zYcmyYIBNOIPijeCjhrGJHJMyFw55SS4FxxlgQh7isHqEGBmD5_dtJLlj6UiChdxs-iCWolt1Txd-IV-XapcrW7TywB36O8PaVv1rJS4xlmKeZkgXrwLdLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا بخریم؟ دلار بخریم؟ یا اصلاً هیچ‌کدوم؟
🤔
🔹
وقتی دلار به ۲۶۰ هزار تومان برسه، از قیمت فعلی فقط حدود ۱۵٪ فاصله داره.
🔹
از طرفی درآمد ثابت تا پایان سال حدود ۱۸٪ سود می‌ده.
پس سؤال اینه:
🔹
فرصت اصلی سرمایه‌گذاری الان کجاست؟
🔹
چهارشنبه ساعت ۲۱، توی یک لایو رایگان جواب این سؤال رو بررسی می‌کنیم؛ با عدد و منطق، نه حدس و هیجان.
👇
برای شرکت رایگان، همین الان ثبت‌نام کن:
[لینک ثبت‌نام]
[لینک ثبت‌نام]
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/688032" target="_blank">📅 22:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688029">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_F6kRVjZUHJIshzz-3X_GNVQ4o3iV4tBlm47no2V_DJQ7hgjde4OEpGeHiGdeGnV-gdWnQPyioJ10QLoxGpsYl2K-iNZPgp0SaBpiQTzlHtL8qa3Ejx_uwhMz_-0B0iQihPJjMEWj81-Tx-QVcBRXpSJaze9QkBc4DTtEwgX3vZocCs-6BlC-jVYEzJeMSv9j17qAVYN5MqWl24uQZJH9tqlPaHMmynkRSdvBeZu-i-hbQztHQV6cCYBV9O7wI2i0YHOCHM7FadkMe12BT21hf_Q8x_uIq1DzYiFcoxrVWCDfRuwe6M71vLmZBl24qUM7OJfROa7K7S_3L9elxE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر پس از پایان هفته ششم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/688029" target="_blank">📅 22:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688028">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
تصمیم جدید دولت برای تأمین سوخت کاربران راننده تاکسی‌های اینترنتی
🔹
در جلسه انرژی که عصر امروز، دوشنبه ۱۶ شهریور، به ریاست دکتر پزشکیان، رئیس‌جمهوری، برگزار شد، با درخواست و پیگیری شرکت‌های تاکسی اینترنتی برای تأمین سوخت مورد نیاز کاربران راننده موافقت شد.
🔹
این جلسه با توجه به ضرورت تأمین سوخت کاربران راننده و در پی درخواست شرکت‌های تاکسی اینترنتی برای رسیدگی فوری به این موضوع برگزار شد. سهمیه مازاد سوخت کاربران راننده تاکسی‌های اینترنتی متناسب با میزان پیمایش آن‌ها، تا سقف ۳۰۰ لیتر در ماه، روی کارت سوخت‌شان منظور خواهد شد تا بتوانند سوخت مورد نیازشان را تأمین کنند. این تصمیم در حالی اتخاذ شده است که از بامداد ۱۷ شهریور، نرخ سوم بنزین در جایگاه‌های سوخت به لیتری ۱۰ هزار تومان رسیده است.
🔹
محمد خلج، مدیرعامل اسنپ، ضمن قدردانی از رسیدگی فوری به این موضوع و تصمیم اتخاذشده در جلسه انرژی گفت: «رسیدگی سریع به موضوع تأمین سوخت کاربران راننده تاکسی‌های اینترنتی و تصمیم اتخاذشده در این زمینه می‌تواند به رفع یکی از دغدغه‌های مهم رانندگان کمک کند.
🔹
دسترسی به سوخت مورد نیاز بخش مهمی از امکان ادامه فعالیت اقتصادی رانندگان است و امیدواریم اجرای این تصمیم نیز با همین سرعت و دقت دنبال شود تا اثر آن در عمل برای کاربران راننده قابل لمس باشد.»
🔹
مصطفی سیدحسینی، مدیرعامل تپسی، نیز ضمن قدردانی از تصمیم دولت و شخص رئیس جمهور برای تأمین سوخت کاربران راننده تاکسی‌های اینترنتی گفت: «هزینه سوخت یکی از مؤلفه‌های مستقیم در هزینه فعالیت کاربران راننده است و هر تغییری در آن می‌تواند بر اقتصاد سفر در تاکسی‌های اینترنتی اثر بگذارد. امیدواریم اجرای دقیق و به‌موقع این تصمیم به حفظ پایداری فعالیت رانندگان و جلوگیری از انتقال بخشی از افزایش هزینه‌ها به سفرهای روزمره مردم کمک کند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/688028" target="_blank">📅 22:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688027">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dffacb8b9.mp4?token=CDiN0_CKoUMFwzW8s1QLY9jpJM1glyrp5zikqRlK8NTOPq38va1Mc6JZ0UBkOUsL9C85a6M82VYBY86DBb85QVjvJVjfHiRCOWUm72wGFLj4vyheb9piIOwTB50WaNu9okW5v8zW5UIrXsuBa1_XVmcmD5eIn2IpTYJry1dH93b1EXLMf1rNeNUjg33oT2kmxKMPezfmU0TrY-LAghiMaxlTWQ4r76Dxuvn0G3bisQaIuZjCovmZI8g0PsWna-R57BObUW1X-X76SwiS3IEu7C1TcyffVD1hUmuRLxxegBfPkLqn0CCt8QpX5b1tTch57nHeTqEZ2CQyAgEFtzo1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dffacb8b9.mp4?token=CDiN0_CKoUMFwzW8s1QLY9jpJM1glyrp5zikqRlK8NTOPq38va1Mc6JZ0UBkOUsL9C85a6M82VYBY86DBb85QVjvJVjfHiRCOWUm72wGFLj4vyheb9piIOwTB50WaNu9okW5v8zW5UIrXsuBa1_XVmcmD5eIn2IpTYJry1dH93b1EXLMf1rNeNUjg33oT2kmxKMPezfmU0TrY-LAghiMaxlTWQ4r76Dxuvn0G3bisQaIuZjCovmZI8g0PsWna-R57BObUW1X-X76SwiS3IEu7C1TcyffVD1hUmuRLxxegBfPkLqn0CCt8QpX5b1tTch57nHeTqEZ2CQyAgEFtzo1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه احیای قلبی ریوی می‌تواند جان کسی را نجات دهد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/688027" target="_blank">📅 22:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688026">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEfisBzA5gQnryg7Ievz-PIrm1iqKGT3sCgYvz-aYrFsfQrBr46wAsNxL6FwWEWOePjMSEQRdOxiYirxr71lrn-Rcvv9-5WkjFL61r6QpqjbwN0NPtAHOiFY1mE5YCIJiIEe4TZ1JaoMkBo38D9UHy5je_9peukIoZxOyx3WFidIXoqgmTCuA-vFLJqhFgzBwTJBD3yYouxuIeuogQ1lvjkSXYZg-Vx73WdcDbKNROEuTewhWy8g18bnwFkrxMxxgVQMnJAqyu5nS7Fg3m6xIAkNKV0z0ptWmVXNpHnrwKLL_nZfNnHcd9D4AEFwWNkYnlHaXi0IpiLXI7GDR7pfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارشی از افتتاح خط تولید جدید کارخانه فعال صنعت باتری کشور در مشهد؛
🔹
نیروگستران؛ در مسیر جهش تولید
🔹
همزمان با هفته دولت،خط تولید جدید شرکت صنایع تولیدی نیروگستران خراسان با حضور معاون امور معادن و صنایع معدنی وزارت صنعت، معدن وتجارت، معاون هماهنگی امور اقتصادی استانداری خراسان رضوی و مدیرکل صنعت، معدن وتجارت استان به بهره‌برداری رسید؛ مجموعه‌ای که طی سال‌های اخیر با توسعه خطوط تولید و سرمایه‌گذاری در فناوری وتجهیزات، به یکی از واحدهای توانمند صنعت باتری کشور تبدیل شده است
ادامه مطلب در :
https://sarasari.khorasanonlin.ir/Newspaper/item/155777
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/688026" target="_blank">📅 22:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688025">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213601a2f2.mp4?token=uqkXlfoR8gTKfYkcYuOZ3da2mMrE9wmIoK47B4Oi20dNDsnpKMSeNC_x0Mw1wxNY8wWoiaH53kadc3kniJDYCBN2LNtyo0VU-14rB7ZQSDKKEcBcAr8IQ-DirdlabMa5_IP8lqR8vKtnI79cCiUQvB0G5Zpfc76ijkjxeGptsA-_o9VoMWrw54TBPJK1EptUHMs7SuasWrSOjlQFQIh0wfmbjemIn1-NqT6fFHIN4W_kc_4d5duGyGkIOtIq7tCcBjajTAdPZ4vtYUriNXr8hTFKDJTyNQeXPrfW08lFn7NVPSgIp4PLfDO64ADeIGV02TI5-Tw5D54cl97QsO-tgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213601a2f2.mp4?token=uqkXlfoR8gTKfYkcYuOZ3da2mMrE9wmIoK47B4Oi20dNDsnpKMSeNC_x0Mw1wxNY8wWoiaH53kadc3kniJDYCBN2LNtyo0VU-14rB7ZQSDKKEcBcAr8IQ-DirdlabMa5_IP8lqR8vKtnI79cCiUQvB0G5Zpfc76ijkjxeGptsA-_o9VoMWrw54TBPJK1EptUHMs7SuasWrSOjlQFQIh0wfmbjemIn1-NqT6fFHIN4W_kc_4d5duGyGkIOtIq7tCcBjajTAdPZ4vtYUriNXr8hTFKDJTyNQeXPrfW08lFn7NVPSgIp4PLfDO64ADeIGV02TI5-Tw5D54cl97QsO-tgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوره سر یعنی چی؟ دلیل شوره کثیفی نیست!
‌
🔹
در این ویدیو دلیل اصلی گفته شده
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/688025" target="_blank">📅 22:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688024">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFt5RNrtAGNbfLByvoDEN2_o5aKl_rc5zXtwiaEiYsikjPoRDIx9FdqTgrhth0tfcaIamPh2nNii6dYALizEASqW_sVF75E1gdt4A0BKoPsGyavuQth5UnHqw_glrER-A5juq94dBfLemER5tghcCvxTFo-p4t_z7mP71YRAF2NcCYR97z9TcWfY5Iw_l4HIf4sqyAiTabZvwXD3geTzWswJZ1S_dRF_S_OZR6ibOhCtZyQOkeGC64Gt_QXZXucCxwJqMavvx4sKmxTYhNIbYVvQHyQqQ3DeZalzBRaUd0FZfp-6JgmUOe3UlUnzkeJk4G8d6RMes87f0HCEoB_ThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده حمله به انبارهای سلاح تروریست‌ها در عراق/ حمله پیش‌دستانه برای خنثی کردن توطئه نتانیاهو و ترامپ؟
🔹
برخی معتقدند حمله دیشب مرتبط با خطراتی است که از غرب، کشور را تهدید می‌کند. این تهدیدات به خصوص از جانب آمریکایی‌ها زیاد شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3243484</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/688024" target="_blank">📅 21:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688023">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5a9e35199.mp4?token=gQ5MJC6bGkc7RCgnfGVPbOrUEX1kch_sLl-3Vod1prfHlruS1u7JPGeQFjONYsGXjh1pwklTy057TwGpsaR6kEPqO6iMGJt9jvLEmYze0hey8e4Mb26aqUnb_Lbl__nqFTS8Kt4A-nTljLXx8ekaUec-vGnOrinxotfLvnrka6VuCYfXTetWNPFbJci7OPLVmIzIFxJxiqEVzDPogRScjdxM-4JmgQJz4rCVjoR34e49kgzj2sdsJ0Z5LDna57MIVZHSbF84iFd-PcTqTrl6pL3pMoPb9l0U1PRRvtymRcu3kyWD2sC6qWd0qafLyAF-0klldXenahl3bCjtVXA9SRq_S8dgjyRQj13-oOOQRPhOJOI8z7C28c_3j6hYGxh5S3FljzD8yaKLxIbhUzzcm1d1_oV7fniBd5XcS-QzG_4mhIiKhCNUDv9A4-LxR-utZ3L7lzfMnp1CsGlKtcyaEge6LBYE57-PTKAyhpGznk8v86vUbxhQSX1lTSl1vV9b1oup4V-7bo3HJ0HcmU-bUvHFDJduuyQYnNmxp0HAVgshl0NSLuEEl9HJ6dYSawZjpf-kFw4JNSHTA-9QyT0xVtv-kBzgTOj8NIW_AUq1FP3Flflva90dIe0HZpCuNpfeW9J5agx8mpoXfxSs0EMqtbr9vxu0JMGKtogre35YvgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5a9e35199.mp4?token=gQ5MJC6bGkc7RCgnfGVPbOrUEX1kch_sLl-3Vod1prfHlruS1u7JPGeQFjONYsGXjh1pwklTy057TwGpsaR6kEPqO6iMGJt9jvLEmYze0hey8e4Mb26aqUnb_Lbl__nqFTS8Kt4A-nTljLXx8ekaUec-vGnOrinxotfLvnrka6VuCYfXTetWNPFbJci7OPLVmIzIFxJxiqEVzDPogRScjdxM-4JmgQJz4rCVjoR34e49kgzj2sdsJ0Z5LDna57MIVZHSbF84iFd-PcTqTrl6pL3pMoPb9l0U1PRRvtymRcu3kyWD2sC6qWd0qafLyAF-0klldXenahl3bCjtVXA9SRq_S8dgjyRQj13-oOOQRPhOJOI8z7C28c_3j6hYGxh5S3FljzD8yaKLxIbhUzzcm1d1_oV7fniBd5XcS-QzG_4mhIiKhCNUDv9A4-LxR-utZ3L7lzfMnp1CsGlKtcyaEge6LBYE57-PTKAyhpGznk8v86vUbxhQSX1lTSl1vV9b1oup4V-7bo3HJ0HcmU-bUvHFDJduuyQYnNmxp0HAVgshl0NSLuEEl9HJ6dYSawZjpf-kFw4JNSHTA-9QyT0xVtv-kBzgTOj8NIW_AUq1FP3Flflva90dIe0HZpCuNpfeW9J5agx8mpoXfxSs0EMqtbr9vxu0JMGKtogre35YvgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا در آستانه پاییز با کمبود بنزین مواجه خواهیم شد؟
/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/688023" target="_blank">📅 21:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688022">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار اصفهان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247a073d5e.mp4?token=FiBejjAGSASJUwbKnSq87jVKniQ-JL--n5-FBh6CjtYbJcCeK1R3fxGxFpgiRBDclcC69x9aa0QlZLqAa6P4aHbx8VZzn36PhvCqeh-eBLMrrhcExkRTvb4Xwo3x1Tb6E1fnawaRlSFsxg0GxZb_6xLu-Yhar7q0qzuhB9zq_Fg_xe5DC3ONWqBG2O_z5u_70EPU8u6BI0KmkdzJ1FfhvTGBcpLHZiOs83z4EgBaMZ5N_qlslh83cf2oBNWKvBNWuuNiTFc_WC1W_55hLHCu608mAPZ9T1Wo3fJEqajuUzraqbjtxk37B1lwAO_40JqImtijqk3UQMkVcREytCH3bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247a073d5e.mp4?token=FiBejjAGSASJUwbKnSq87jVKniQ-JL--n5-FBh6CjtYbJcCeK1R3fxGxFpgiRBDclcC69x9aa0QlZLqAa6P4aHbx8VZzn36PhvCqeh-eBLMrrhcExkRTvb4Xwo3x1Tb6E1fnawaRlSFsxg0GxZb_6xLu-Yhar7q0qzuhB9zq_Fg_xe5DC3ONWqBG2O_z5u_70EPU8u6BI0KmkdzJ1FfhvTGBcpLHZiOs83z4EgBaMZ5N_qlslh83cf2oBNWKvBNWuuNiTFc_WC1W_55hLHCu608mAPZ9T1Wo3fJEqajuUzraqbjtxk37B1lwAO_40JqImtijqk3UQMkVcREytCH3bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چهارمین فرونشست در ده روز گذشته در خیابان رباط اصفهان
#فرونشست_اصفهان
@akhbareisfahan</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/688022" target="_blank">📅 21:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688021">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1a55c75f.mp4?token=QkFPPn2quC22lNEjOREnaNRUHTQe1aczDyEosIVLnGmV6rPVO2EJ1aJGr-u6co9Y89N0DxGz4RjPQiYRG-AHKUh9liUsHnhXiOJxNmFnD5E1dxpsodLewVmKOwcWY3W6mLFUjSs6A_o7yQvY6P_xhIjfq31TtoQVTJjwvVN2ei5KaEQ1cjT1pfYY_hzFrJaUSh-gA8HqrZkRkNQfMoexqXVBUl5-tDU0CeD4fOP555-2xVTfzgi4GORhZno0WlSs27XHyqZBeFOviwqimzu4uUmqW5O4RzQNenxcOAsx0o5xf7H3XbJvU80Anc8VWeWJ3wT5Yvqz7uvvQJd9PW7Rhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1a55c75f.mp4?token=QkFPPn2quC22lNEjOREnaNRUHTQe1aczDyEosIVLnGmV6rPVO2EJ1aJGr-u6co9Y89N0DxGz4RjPQiYRG-AHKUh9liUsHnhXiOJxNmFnD5E1dxpsodLewVmKOwcWY3W6mLFUjSs6A_o7yQvY6P_xhIjfq31TtoQVTJjwvVN2ei5KaEQ1cjT1pfYY_hzFrJaUSh-gA8HqrZkRkNQfMoexqXVBUl5-tDU0CeD4fOP555-2xVTfzgi4GORhZno0WlSs27XHyqZBeFOviwqimzu4uUmqW5O4RzQNenxcOAsx0o5xf7H3XbJvU80Anc8VWeWJ3wT5Yvqz7uvvQJd9PW7Rhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام خلج در برنامۀ سمت خدا: تفکر فرعونی، قدرت و تجهیزات را عامل پیروزی می‌داند
🔹
همان تفکری که امروز در آمریکا و رژیم صهیونیستی دیده می‌شود.
🔹
قرآن پیروزی را از آنِ اهل ایمان و تقوا می‌داند، نه صاحبان قدرت و ثروت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/688021" target="_blank">📅 21:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688020">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وام مسکن تهران یک میلیارد تومان شد
🔹
با اعلام مدیرعامل بانک مسکن، مبلغ وام مسکن به‌ازای هر نفر افزایش پیدا کرد.
🔹
تهران:  یک میلیارد تومان به‌ازای هر نفر
🔹
شهرهای بالای ۲۰۰ هزار نفر: ۸۰۰ میلیون تومان
🔹
سایر شهرها: ۶۰۰ میلیون تومان
🔹
یعنی زوجین در تهران مجموعا ۲ میلیارد تومان برای خرید مسکن دریافت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/688020" target="_blank">📅 21:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688019">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac0ad39474.mp4?token=HN1oZyHfVfVFacZQKIO0YL2q2gNfY2p5HJsGs0TA25JZFQkFmkLPOqrAYtCiM96eMqXC-yyN7HtIBVqTWVj5BzGqsXF8WfxXUAxdIV5Z4bQ62jAjSXBMOI_GMcUD3XxooXrwjluGfBX9TgwMkrtp1qTTwp71szTgv-AIuaZNQ2DEOaDW3NtOQCxCgHwzRKWHfgVzyvTxI-i8Ek7UhsLvUHXiMhvBuiSPEpRpl0xo4fQewzxzXw-yjd6wDttAd9GD9hihgLH5XVwYhQXfNDeynlD9cIC3OAZ81cWPi3a6hl5pkUfU9nvyZBn7Wci-IxzRCW4tSNH2CtYFb49dsvxd8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac0ad39474.mp4?token=HN1oZyHfVfVFacZQKIO0YL2q2gNfY2p5HJsGs0TA25JZFQkFmkLPOqrAYtCiM96eMqXC-yyN7HtIBVqTWVj5BzGqsXF8WfxXUAxdIV5Z4bQ62jAjSXBMOI_GMcUD3XxooXrwjluGfBX9TgwMkrtp1qTTwp71szTgv-AIuaZNQ2DEOaDW3NtOQCxCgHwzRKWHfgVzyvTxI-i8Ek7UhsLvUHXiMhvBuiSPEpRpl0xo4fQewzxzXw-yjd6wDttAd9GD9hihgLH5XVwYhQXfNDeynlD9cIC3OAZ81cWPi3a6hl5pkUfU9nvyZBn7Wci-IxzRCW4tSNH2CtYFb49dsvxd8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتشه با چندتا ترفند، کلی ویدئویی جذاب برای محصولات پیجت بسازی #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/688019" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688018">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65febfc0f0.mp4?token=dGC-pq-_1wkf5UnOcJVjGkHmnaHWUn5_XAf33e72Nya48kjS6EEmwwwkS7tJ3pmYBw2a8ztCcmBAzDDfE7QUM34blnA_TSTDWxyN9DfbT1m0zBMI3EgKD6hEZdp6BymUzywu2AYp6gBdPnJ02VMnecm6IVhq3bG7ppEjH3qDG-FrHlXfBwSZYrfrV7RXuYipkRCGJnlYANhNOCHNfXknRnAFp08wl-P8nev4C3OaSIk5Z41oRcs-lkW_sN_24i60rWU4GwmzMuu3aC_BeQGS8K4v0P6SOPdQ45c5QJknA7rqSVioPNs08b0wbKY9zegnZ2PkSg5tycPUe5AFJXOQMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65febfc0f0.mp4?token=dGC-pq-_1wkf5UnOcJVjGkHmnaHWUn5_XAf33e72Nya48kjS6EEmwwwkS7tJ3pmYBw2a8ztCcmBAzDDfE7QUM34blnA_TSTDWxyN9DfbT1m0zBMI3EgKD6hEZdp6BymUzywu2AYp6gBdPnJ02VMnecm6IVhq3bG7ppEjH3qDG-FrHlXfBwSZYrfrV7RXuYipkRCGJnlYANhNOCHNfXknRnAFp08wl-P8nev4C3OaSIk5Z41oRcs-lkW_sN_24i60rWU4GwmzMuu3aC_BeQGS8K4v0P6SOPdQ45c5QJknA7rqSVioPNs08b0wbKY9zegnZ2PkSg5tycPUe5AFJXOQMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین همسایه ما در دوران جنگ افغانستان بود، حتی اعلام کرد امنیت شما را در پشت مرز حفظ می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/688018" target="_blank">📅 21:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688017">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
آکسیوس: جنگ در ایران باعث افزایش تقریبی ۱٠٠ میلیارد دلار هزینه برای مصرف‌کنندگان آمریکایی از طریق افزایش قیمت سوخت، از تاریخ ۲۸ فوریه تاکنون شده است
🔹
ایالت تگزاس بیشترین میزان خسارت را متحمل شده است پس از آن ایالت‌های کالیفرنیا و فلوریدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/688017" target="_blank">📅 21:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688016">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3Wpv_IZHU_4WXsCj5ze4f9i5XdQMzEjHEPCP6voIJi6PB2qUNLNNBI_Z9h8CluPYcfdiB4O7VBRmdJ6oKJTVD-z1vL2b0GCS5i3VPFeZin9adRQGeQoa2SdM7VEKrXpPf7pX4msk4VqsYvdpDsa8opIkReFtazCPm3q7iqBBNt3rYu9QSDRINslXwrO-C5Jor1bVq74Aj1Bt7z987YVeDTOkcYyPIoLcJ9He2_xuj5nY6Qhx-nnqV8KU-kP4CgJ1ZUtjLmbOOoTzMgO0TT7RuIxExeOWaBUAY8hamr2QfODUSX8JposzXa6GAYc_4UazyHaOjK-kXIKv8x-chkphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرسپولیس ذوب‌آهن را از پیش‌رو برداشت
🔹
پرسپولیس ۲ - صفر ذوب‌آهن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/688016" target="_blank">📅 21:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688015">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4yBSvToZS6esUNHVgmDceFjfxHmQXzdr-lHtxuiEhxXq0QD55Mym2YzanRVVkXWjwTzn-5iZPQifGMV7WwsxeOW_DYqp4HgRjg6ZxehGhfryW8sd7pcH8zVA1wENSd04JPVP7GtXBtobrkN9qQTl7IVE_mfmmevgOeEOrF1wPNkkhOlvzZ4QrpCG7oUeTgog7VDyvL5BRsxUlpUHt9QhHpwidrgYhHrxtEsFvdc-RJxaeOaG31rV-N4C2RNrYKekZlL6Gl-gCRymnqtPZM9Ukcky18JamLV0hdNx7XA4-kKk5suz4NkBycOB7hV7o-NXkrmv4LQpKQb6_M3smimig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط تلفن سازمانی ۴ و ۵ رقمی نکسفون، راهکاری برای حرفه‌ای‌تر شدن ارتباط تلفنی کسب‌وکارها هستند:
🔢
شماره‌ای کوتاه و آسان برای به خاطر سپردن
📞
نمایش شماره ۴ یا ۵ رقمی سازمان در تماس‌های ورودی و خروجی
⭐
امکان انتخاب شماره دلخواه از میان شماره‌های قابل ارائه
🏷️
فرصت ویژه شهریورماه برای خرید خطوط ۴ و ۵ رقمی نکسفون با تخفیف‌های ویژه
🔎
دریافت مشاوره و بررسی شماره‌های قابل ارائه:
https://isp.nexfon.ir/khabarfori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/688015" target="_blank">📅 21:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688014">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ماجرای عدد صفر در جایگاه‌های بنزین چیست؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/688014" target="_blank">📅 20:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688013">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d737af42b.mp4?token=r6XUK0oCT6Af4TFsG01TUI_Qvw8fPP9XxR-dIoNNiwRLCZtO76X8woBO5YW6TEe2wGFtyVRqGfwmq7J-ed70UJtUmFa3So8Kbp2UtAsQPZ15DHrFf9x82EVqyjmplCMnYPet3-6zzYawd33JptBcxC6dp2ifYKvPidVZgVEgX8Z6FxFhQ13sLvgBpIHzjlUKeg34v4r6-ELVO_PXZLS0h47Qg8NpStuoHHnSh6jRvBLJmBylBU3eY8aGkL0SUh5ZlY8xEFEgfDwSETyNlldzLPMKPWWcgACXfPDW8Kd4aLvG5pJ4IWx9dUz01fXxD4_V1SDWCvv1tQ3wyJQvsZ773Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d737af42b.mp4?token=r6XUK0oCT6Af4TFsG01TUI_Qvw8fPP9XxR-dIoNNiwRLCZtO76X8woBO5YW6TEe2wGFtyVRqGfwmq7J-ed70UJtUmFa3So8Kbp2UtAsQPZ15DHrFf9x82EVqyjmplCMnYPet3-6zzYawd33JptBcxC6dp2ifYKvPidVZgVEgX8Z6FxFhQ13sLvgBpIHzjlUKeg34v4r6-ELVO_PXZLS0h47Qg8NpStuoHHnSh6jRvBLJmBylBU3eY8aGkL0SUh5ZlY8xEFEgfDwSETyNlldzLPMKPWWcgACXfPDW8Kd4aLvG5pJ4IWx9dUz01fXxD4_V1SDWCvv1tQ3wyJQvsZ773Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای عدد صفر در جایگاه‌های بنزین چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/688013" target="_blank">📅 20:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688012">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrJqva56T9hH2Z9vLV_rE3mbjkZbHzTrIdPOWL5vgFGoG3KYY4cRbfUkHnYeHur8BZdwUK-EIo2fgdfJTAr7TWChRk8ZdWjMPMLcj0aifmAaF3_VHPSlgvgmQF7c43F9GB-HWTnFB5Ek72k0XcFnV5zWQCu_vKx-yVcFGzwliQA91Maju21DhJSFnggU6tlrUvDquf4ZmP9fLjCh9y5GbJ-FEPlIhLnESzaLE_2gv_S9IhIXngGDIuMZnTAWleLFvGuldmDvT-8-sHV1OvHAdI34-t8qzZSrKPUD3lxblxCX627OJ1__yII2bebLKVMQ5Porl3SwOBvwZHILKHun3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبح سه‌شنبه
🔹
بامداد ۱۷ شهریورماه ۱۴۰۵، طبق اعلام سخنگوی دولت، پس از کش و قوس‌های فراوان برای تصمیم افزایش قیمت بنزین، نرخ سوم به ۱۰ هزار تومان افزایش می‌یابد. با توجه به شرایط موجود کشور، این کم‌درد‌ترین تصمیم برای دولت به نظر می‌رسد و با توجه به رویه مصرف سوخت، گامی در راستای اصلاح قیمت است.
🔹
هشتصدوپنجاه‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/688012" target="_blank">📅 20:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688011">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
عارف: یارانه واردات بنزین به‌تدریج حذف می‌شود
معاون اول رئیس‌جمهور:
🔹
تنها ۱۵ درصد مصرف بنزین، مشمول نرخ جدید است.
🔹
برای وسایل نقلیه عمومی برنامه‌ریزی شده که با نرخ مناسبی بنزین را تهیه کنند.
🔹
همچنین مصوبه‌ای برای اولویت‌بخشی به از رده خارج کردن خودروهای فرسوده و جایگزینی آن‌ها با خودروهای دوگانه‌سوز و برقی اتخاذ شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/688011" target="_blank">📅 20:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688010">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orr2e_dj9macN9yeq37jGdizze2hMkXFl9IZLi7hawesIErJXLZat63rBGB7yVF6nU27biL2mNBiTk7QjbxmGGprmEmLv0qESuNOxMtp2audIaAxLUcod15Ki9S210J0yUUUSnaiAoMCfeQ1tkVsyJgqHfrCgq6iUTDPEoHVOuVjacCgwK0jsbRlwDbmV_dCDhDyJN7aBKxeCL0qaGgIOP5VToDa-r7RHoyap4sHhcZbwo3YWa43liTx7_vrSVSJY8ZbiBDoOYvQYGUORtqOZg5_gD7lN30Bk9REjBEXeMQXopoIuUMmMJL6b-pPDSDKes44txCQzfkJNH7XmtaABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخشش دو اثر سازمان اوج در رسانه ملی «رویای نیمه شب» و «به وقت ایران» پرمخاطب‌ترین‌های تلویزیون شدند
🔹
با اعلام مرکز تحقیقات صدا‌و‌سیما، دو محصول سازمان اوج، سریال «رویای نیمه شب» و برنامه «به وقت ایران» در صدر پربیننده‌ترین آثار تلویزیون قرار گرفتند.
🔹
سریال «رویای نیمه شب» به کارگردانی حسن آخوندپور و تهیه کنندگی سعید سعدی که به تازگی پخش آن از شبکه سه سیما پایان یافته است، در میان سریال‌های رسانه ملی به عنوان پرمخاطب‌ترین سریال مورد استقبال بینندگان صدا‌و‌سیما قرار گرفته است.
🔹
برنامه «به وقت ایران» با اجرای سرباز روح الله رضوی نیز که هر شب از شبکه خبر روی آنتن می‌رود نزدیک به ۶ ماه است که در صدر پربیننده‌ترین برنامه‌های صدا‌و‌سیما، قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/688010" target="_blank">📅 20:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688009">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
عراقچی: بحث مدیریت آینده تنگه هرمز و موضوعات راهبردی مرتبط، یکی از بحث‌های جدی در قوه مقننه است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/688009" target="_blank">📅 20:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688008">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCkAyuGxtDRLtXVb0U2XhAw4fmwcBX4PuI0O3p-kzBIL19CXQHDnCM5cN85MM67izeN7KlP5aTUNvF0_0weYAuQ7MHHXnDpmAWfdHieddVBEJlmrVLD9Z0V8FrDxVjwYlG7zluX_7AeBksrkbBABSLvo6tBsiPLbSA40JFuxqzFcne6BizASMobu3o1O6RnO3u9LV9r97XZ7YSijmEIo40OvH0EaMSd7vzjVZpAC5aEnpV-NeIMd_34T87EOyWsGuK7YweeK-R29S5b_rcK89PEIKlQu3uIoIUy7FuOajrCd0gY9O0US73oPfmrx2uMJN-b_b706hc4D8-esLg3Qeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ بر مالکیت آمریکای شمالی؛ همزمان با سفر رئیس کمیسیون اروپا به گرینلند
🔹
همزمان با سفر اورسولا فون در لاین، رئیس کمیسیون اتحادیه اروپا، به گرینلند و اعلام سرمایه‌گذاری ۲۰۰ میلیون یورویی این اتحادیه در این جزیره، دونالد ترامپ، رئیس‌جمهور آمریکا، در پیامی تمامی کشورها و مناطق آمریکای شمالی را متعلق به ایالات متحده دانست و پرچم آمریکا را بر روی نقشه این مناطق قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/688008" target="_blank">📅 20:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688007">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/027b79e19e.mp4?token=KlrN0IQqsR3ikBjZomxrk3TYHrUBK_K0_cz8fgSaxLGtAgS-zNQ_Sw-MVwMYjKz36Lkqm2FzKFEX-5loNYjpFTZ_Kt-hquaKOyHGzbc_3PC-CiKmK3MyJurPuF5UDFu2_P5wMJ_N5-mfAubyZgXPYS7wCKvVGW4mk4-WaoyhYB10obH1lzlgFTmvR0scJvyi2LxqtBAm6tVWkrflOhqIeh6CjQwUJD4MRnH9Dy77Va7NsSiWS_UnTwSDe9iYWdlLqqwhKVcDcGitola87MN09i8TGHkUxI9WFewLEf-O7HYwnCuZBsyLWD6Le-LM6_o2lWWuQvdLnJJugFDqBK1Cuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/027b79e19e.mp4?token=KlrN0IQqsR3ikBjZomxrk3TYHrUBK_K0_cz8fgSaxLGtAgS-zNQ_Sw-MVwMYjKz36Lkqm2FzKFEX-5loNYjpFTZ_Kt-hquaKOyHGzbc_3PC-CiKmK3MyJurPuF5UDFu2_P5wMJ_N5-mfAubyZgXPYS7wCKvVGW4mk4-WaoyhYB10obH1lzlgFTmvR0scJvyi2LxqtBAm6tVWkrflOhqIeh6CjQwUJD4MRnH9Dy77Va7NsSiWS_UnTwSDe9iYWdlLqqwhKVcDcGitola87MN09i8TGHkUxI9WFewLEf-O7HYwnCuZBsyLWD6Le-LM6_o2lWWuQvdLnJJugFDqBK1Cuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل اول پرسپولیس به ذوب‌آهن توسط علیپور در دقیقۀ ۴۳
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/688007" target="_blank">📅 20:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688004">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1848dbc070.mp4?token=SV18GfAkvZS2Jwvc6rnUrXF-YwhWurH2NRJ2mpuf_wct3NRE8P4m78MGOfI7U_RchS0kXVOc7jHNSHQ7nRs4elVZcNRVLMF6z7WANb8IHCgEeypFwo-XsmEBrEvUlDuF8HKVmxUhQ5JqGslmkW5Kohis_S7aILp69Xlq1hDpCZ4FVkEMHIlwv2v3dKLyXZV59cexBhHW72brP4DWVi_dKU117lXrUJz3-xraEgs7QegK_leK3sxSk7glG0HOrIWiZOowEGvCwjoWnu6-ql2IfginvWfSIyg9Z9uTB4Xa9BK7FwQgyYqI5iDqIkLj5h4a8cygfTSYYrV1szTYeZzXXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1848dbc070.mp4?token=SV18GfAkvZS2Jwvc6rnUrXF-YwhWurH2NRJ2mpuf_wct3NRE8P4m78MGOfI7U_RchS0kXVOc7jHNSHQ7nRs4elVZcNRVLMF6z7WANb8IHCgEeypFwo-XsmEBrEvUlDuF8HKVmxUhQ5JqGslmkW5Kohis_S7aILp69Xlq1hDpCZ4FVkEMHIlwv2v3dKLyXZV59cexBhHW72brP4DWVi_dKU117lXrUJz3-xraEgs7QegK_leK3sxSk7glG0HOrIWiZOowEGvCwjoWnu6-ql2IfginvWfSIyg9Z9uTB4Xa9BK7FwQgyYqI5iDqIkLj5h4a8cygfTSYYrV1szTYeZzXXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برق لباس‌ها رو با یه ترفند ساده شکست بده!
⚡
👕
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/688004" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688003">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c27N_YlUEJo63l1YNuIQQgOA9aW-SXNqDN7tDqwAIVigQbPJV3EqOk9u-GH5CsuXi2EpOciUOHqVWkBzPDWej4qb0ddKjWhx4sWEB1TSzG2fwccyUC9-6WxCqTnG3T8kYpODPxKexRua4n3NOaebcFjAcejqHiZHMRY9EkloJcnbyzrLhYEi95ijQJXXskxqhJAUOsb8cYpJVLaJn85S_R2JSWbi1f8ZUl8lfmnd1LyYUQMPT7JexwbMMo8d7yoP9yXF1mCkwW_MB6pbM_WYLLufWVw4rb08KMgn6hStOzHv2TgU2pcuXfegZ7MgE00-fxVUdk04m2pPqTqrvq9Enw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام رای تراکتور و گل گهر؛
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/688003" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688002">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
اردوغان: همه جهان تاوان جنگ علیه ایران را می‌پردازد
🔹
تا زمانی که بن‌بست در تنگه هرمز برطرف نشود، روند افزایش قیمت‌ها در جهان ادامه خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/688002" target="_blank">📅 20:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688001">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f220f6b1.mp4?token=IniOVrBClvWyBaNOVfxEVAcVTgUKz5-ozoLXCgNbS4VljrNNR_TMhqNicVpcf_dBKMT9ibcnWVT-BR6H9NlAnmSLockO6OVdCoP54AfuPkd2rkDx_xrZ1ovKJsurGwEmBYi27vMJiall85UPT16IQcYLOgur8VfnxcB4Pe-knnmOVNbDJycLdQV7zgJAQgQtt1mG4tMKoJvo93UEZnmwfRv1OrrcxEj2gsNsU4-6edZ8KM1Fn-m9asxxyrPKJ4xzSKrsL88FyC4k4Um65NNBOX4pd9jwH-RmqoeD1sy9Fo2WNIuz9BMNuCcSW6ULH4YPBH3rSjeaaaYVyjPTG1_f64u-6mHm7bezH5-XR1EFg1NoYTznKUUyUSMX8o4HEtKms6i7v1MsKcDDTU4X7bxv_zwQZIXYvFEHxOrqKvEu6NbI3UGci9iydDPUTo3yeB8IYPL9KsHvPFGKASkVTVgoGRBKpAR6-3AWBPEyDzb42xTkEOjf8ThyH8hIRf5alY4wn01txGy51kw8u0AlBNy3X0ed5MxvD37Kuwdd_n-mOqHuq-R9zCs7N6_rnQf1MTfX1HwVx2RI4Qb9R5S0j1Wg6euxiImn68OrBuoo7lfYTKs73Wl8cPWL3g1tAUVFB4gq__YMevNcOE3codt9JpIUXsUl4Lxi_aoKsx68ZUdkIwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f220f6b1.mp4?token=IniOVrBClvWyBaNOVfxEVAcVTgUKz5-ozoLXCgNbS4VljrNNR_TMhqNicVpcf_dBKMT9ibcnWVT-BR6H9NlAnmSLockO6OVdCoP54AfuPkd2rkDx_xrZ1ovKJsurGwEmBYi27vMJiall85UPT16IQcYLOgur8VfnxcB4Pe-knnmOVNbDJycLdQV7zgJAQgQtt1mG4tMKoJvo93UEZnmwfRv1OrrcxEj2gsNsU4-6edZ8KM1Fn-m9asxxyrPKJ4xzSKrsL88FyC4k4Um65NNBOX4pd9jwH-RmqoeD1sy9Fo2WNIuz9BMNuCcSW6ULH4YPBH3rSjeaaaYVyjPTG1_f64u-6mHm7bezH5-XR1EFg1NoYTznKUUyUSMX8o4HEtKms6i7v1MsKcDDTU4X7bxv_zwQZIXYvFEHxOrqKvEu6NbI3UGci9iydDPUTo3yeB8IYPL9KsHvPFGKASkVTVgoGRBKpAR6-3AWBPEyDzb42xTkEOjf8ThyH8hIRf5alY4wn01txGy51kw8u0AlBNy3X0ed5MxvD37Kuwdd_n-mOqHuq-R9zCs7N6_rnQf1MTfX1HwVx2RI4Qb9R5S0j1Wg6euxiImn68OrBuoo7lfYTKs73Wl8cPWL3g1tAUVFB4gq__YMevNcOE3codt9JpIUXsUl4Lxi_aoKsx68ZUdkIwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباراتی وجود دارند که با گذشت زمان، ارزش خود را از دست نمی‌دهند مانند این عبارت از ماچادو که: "همه چیز می‌گذرد و همه چیز باقی می‌ماند."
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/688001" target="_blank">📅 19:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688000">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45c97d9db9.mp4?token=vMMCT-R6k3FEvbFc-BgP1p5SrvpaLOJ_Z1DKbXcF596nwzOamytaHoXD59zeEZjV8n7gnJLvcofAH1PtUGLvUsRqTZ_E2FN3LI0NaOfJhTRT87rdJqNmJloflOu0hJfLIwkb9Cje7UPTd1NGaLpGIMnnFWAdWf0abpe_KXGPF8x9Ot07kaT0w3AlZYjLlFqZVBlUk_cchhrcKLxEkolWe5SzaQX18PgyS-VAoahMqj6TIgQrRN-LqG36TGBdN4XQcUJh0PeQ6e3WZW8Fm16LjfgEzGMALIQBNeUuttCGlB-t1iWoTXaCgk-VcykW4tIMU974EOq9qNUd6Gg14KGLWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45c97d9db9.mp4?token=vMMCT-R6k3FEvbFc-BgP1p5SrvpaLOJ_Z1DKbXcF596nwzOamytaHoXD59zeEZjV8n7gnJLvcofAH1PtUGLvUsRqTZ_E2FN3LI0NaOfJhTRT87rdJqNmJloflOu0hJfLIwkb9Cje7UPTd1NGaLpGIMnnFWAdWf0abpe_KXGPF8x9Ot07kaT0w3AlZYjLlFqZVBlUk_cchhrcKLxEkolWe5SzaQX18PgyS-VAoahMqj6TIgQrRN-LqG36TGBdN4XQcUJh0PeQ6e3WZW8Fm16LjfgEzGMALIQBNeUuttCGlB-t1iWoTXaCgk-VcykW4tIMU974EOq9qNUd6Gg14KGLWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل اول پرسپولیس به ذوب‌آهن توسط علیپور در دقیقۀ ۴۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/688000" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687999">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فیلترشکن‌ها روزانه ۱۸۹ مگاوات برق مصرف می‌کنند/ توسعه هوش مصنوعی بدون زیرساخت برق شوخی است
مهدی مسائلی، دبیرکل سندیکای برق ایران در
#گفتگو
با خبرفوری:
🔹
محدودیت اینترنت و فعال شدن فیلترشکن‌ها روزانه ۱۸۹ مگاوات به مصرف برق ایران اضافه کرد.
🔹
هوش مصنوعی بدون برق و اینترنت امکان‌پذیر نیست و برخی از موبایل‌ها برای استفاده از هوش مصنوعی به فیلترشکن نیز نیاز دارند.
🔹
بدون برق، توسعه فناوری غیرممکن است. اگر مصرف‌کننده‌های جدید مثل هوش مصنوعی را در صنعت برق نبینیم، قطعاً جلوی آن می‌ایستیم.
🔹
در بحران بی‌آبی، پمپ‌ها و تانک‌های آب سر سفره صنعت برق نشستند؛ حالا نوبت فناوری است.
🔹
تا وقتی مشکلات زیرساختی برق حل نشود، صحبت از توسعه هوش مصنوعی و فناوری یک شوخی است. اگر توسعه دانش و فناوری می‌خواهیم، قیمت برق باید واقعی شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/687999" target="_blank">📅 19:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687998">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzGCPLpMyMx-hFhjZNFkMTHmpBPihxiFdEkb1cq5JWPHSomhhP-d2RzWdZhuNFX9M9WZlfvhUOlPpimj9BYU4AqUKIQH3yEJd6kI6rFUjM7wcxojJWqTDi7VP10WbqHXf-6fG8tCx8VUcUCB_dFyOpPXf-Cv4irqwZqCS2fprAXwfc45K-ab1kThSHf7V__8nBOStrlcLjkNOlC5QcJtv7qIZTNyo7OL0RjFp1vM7fHZhbMNrLqX9V7ITFwbTIsEHKxyuWlH-tVglAtlUBwWeaVU_MnUojypWwlhOlil-DDSVXS-XKLBR5onIbnwrBRYPkVCfF8ctEl0dyYWrj1DRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت خانه در شهرک غرب؛ از ۴۷ میلیارد تا ۱۷۶۰ میلیارد تومان!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/687998" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687992">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrPcBPmtWYaCSARWM1GL1KUqSPYks7hgAV8ymkCN38A7CatadlzNulSn0mbfURTqPPWGAKySCKW5ISzii7Ej80WnDPaNBW6iuAQ6ZtQ8N5-sit2uWl9Ygoq-mO4Pr-q8-FvxdoShopqcclMWbD3U6VYk92oYCOGFJdBTCKq6_8D7-BeRqeblkBenVeMJ1mmbb-NwbFriNoyWFXj8JToQg78ZDJu-tIM6j_lJayMDS9hvUYoPPUueznrwZzn2Bi8Js50ygkwEogXsV_q46IanRGoK6NxpHfBu65Doo4d3M6Bn1iUrYkUXY_sxj6uuNlY4a84Ks6te_NOt9oKoNO5gyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_NQ9FunAaxm7fXiFt-Ku1zc2xDjzfkprsq4-bN9ARQBsPIHGfDpZpD5SptXrRQejw77qtMWk7p1_mwe72tYFfQThQRbv6-v412YmZf3DRgvCuWYWZpXdE8o9DrQeLhZPGavPFY_Ymru4xFEeFLbs2tTAU6nxfqkxPLicBC2KwHtubCIWfj702HNUIdokilywTOkS459-DoNhC4fR9W2b9fKSQwcM1aHEgzAmYL4XtPcbmhswaKKGLxV1s9VQhPR7HIcM-DpcOGETJpqzjECnP1ScC2dyeJ7t7bzIiylvn63Vv5dfV7e0E9vHeBQf64NIRiklxhBL3uL_FUzehkX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nj7ggD_qkxCy0vugaJXs2YFqPyZ7p8g9eLRnKi0LbXFzfoVYoxOBA-mAZToxUgyyeSZ0q_X54zibh7wu-9fRaJmjYDKtDQn1IIfv0wKepWaukDH10PQvkERttH1M7DA1m4nq0p6-ywppN7YcXZO_fPenUNo1sgI4fQs2pl0ilE9eIQeCtTLSD1JH0K0zTrIsPChoqWKyp-lzTgeOT0DfQK8d0wxfmE6tRdIxV1mI42hPAaEh8BNg0zkaNkNzr0AmckqqAj1HiZOQ3vxdOUg3DGpwMXpMZlToWDETDXjRfeKBwV-Ex3AdHvWtAuLUs506_KxEpGolYyypn-C2pOWQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZANusXCLqfWGpDHHe5aPIYsq7oYAwJ4CP6r4l42HdrRkcndeFxWeVnXLN3AVDyU6V06RaVCKvwBphveGbZ4CnL7jN8XkSrnu1_u9ITf8NvlQDou6ZzaB4cggQAGAtpdad9Idzz_6g-yyuPEAJ5ap80afvIHJ5B29LaSzcr9DnVV1FzhQZ6mfJFqQ9bFviCo0FqbPTQZFcSOq96bC3sKnB6jSYaSuO2aMQXmdRUXpb8DMY4yuXg6SXl3n5ZqgsRwfJBIKvbHqYg-YmOg59DgI9svOOAA49KIfKtoOD2rQMx8Gc_TxXvKg-PV4EGpz5HxOa8DGCpKsbYbhmStHd7wZpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خیابان‌های توکیو، ژاپن
🇯🇵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/687992" target="_blank">📅 19:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687991">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv3oUWRRWxBZ-grpAQ-UxOJn4myBHdowGckO0IDpmE-XXr6DKm05QMuU72I1hI6wpUUAoBi_IfaZ-SREOAdAVcLufE8CSOxobamhjjK3FflxFAtKEQNneezHwHZy3Pd0Yo70sML2WcuH95doxR0nepSFrGgXhHQRxxiMVOQcp6Z6qWEYm5QsypiUwxAkWJ6TrSAI4x-il4OC_T7DFhVVqeerxduEUrONZ5osXgaaGgfC9ugH6bNji7lT3ev7B-w0j8D5Fy_iMtM9ZQk7P2roARZgSWcyY2hR7lGJKg2HFnp56xGjGULhhjn7wjsg8I1zTbVUaNOP4WKYldgGJuyu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: سوخت کشتی‌ها در حال کمیاب شدن است و سوخت بانکر مورد استفاده کشتی‌ها در حال کاهش است و این مسئله هزینه حمل‌ونقل دریایی را افزایش میدهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/687991" target="_blank">📅 19:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687990">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ترامپ: آمریکا را نجات خواهیم داد
دونالد ترامپ که پیش از این مدعی بود نتیجه انتخابات برای او اهمیتی ندارد، ادعا کرد:
🔹
ما در انتخابات میان‌دوره‌ای به پیروزی قاطع دست خواهیم یافت و آمریکا را نجات خواهیم داد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/687990" target="_blank">📅 19:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687980">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8LHavKjvEj4jcAfO4NW5hirEO3YdV0PrySbJ6dVBa3c-DJjNYmMr2qJnsORCwgIaVY0Us_6yNPRz3Qm8e3LeY4HJLUVgdKQjI8chzUvtnImZ0eoPu7pyauY_mx6lLxu_ok-J2jqmMFToccvhRP_ntEELsE5bB64V_tnX-2ln1uWsYqgnC9o9bTklfS-yGBKRxqPaQbjlbJ6Gtj-X9XBlZHWR2K7c6tjvm05FXkNos8n-B3EnPjH4wGzKaRps8BBUHlfqPV7eaAqmC3xOj3unrN6mmJ1JVbLj6tqY1QtXk0O9lk3PZhm26AfAQofuIrUOPAU5Mjq7e6juwFrJvDwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1ZFQWXBzi9z3LRFeQk4QjGVjn5AGL-m8QqVhJiZx-PkiBrdrMYkad25LssvTcoQ3YWUZ9KdJqlQtIOdtBkqw1XNsrH2npJ6UOtMXKwMiUo-FTEvHVirjtd_TDVINu6fLgHE-9k9XjjztaX1L2QbtxumzA7i8ULPWGVSuSXh1_LA8TN57aRzTHcjvLQ1X4VG4dgN8i3s54lJgXgxZuCFld-kg7iEQTHg-jtxpi1ldjy-ntnEoCD8TPqD8ROJ4HvfydMsfd95ZKf45jhnnsV_e4h4hJYXGvx2PISGlftK32MkkXC0ZCErEQpiOBMI4jGHy1pzPMDNeLpU__Ty6tst7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFIHLVf7InjKR8WCy4fUCY1fuC3nKR3hthceelP_sx7BxsKYcRCYcHg6XaMeZRg7OI_avwgLsw0vXrs35ddRtqIgWGE5SEutECobrHpxImkbsfntqzUUny33YRC2JzGIqlOHSTxCDlrItyFxjYI-NyW-PYH5IhHYoB7mhVGNfJwrAQauXwh0xUuDRrkMLwcM9UxypXlZCUIqTh08qr4T2pMDc2fOZNoPSpNAlixapThEu6wCZVsgS0RGeLscY89n5w_xpfYs9XsH4fBZ0KUflY2wknamfkjt__QKAWCKVQeCBwWSErcHbVClN7RwHnCthPufy3s0jKUIeMUOGCwz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xj4uiDwZuEwqLDgSmseyAB7jce9ohw5NzlCoSbuG3TknHewotsMwnXmI3kmwbMmPD9zYN45Xurcs01dWQ4bgcE7pQ2_BkPpOx8B7vIrWG3LgE2GGchFZa-wmLzsTxmsLkcE7Ke59G9SqVJlsuB2nLDLW68egr7eiVC3BAXWAGE_1dAhys8GO4LVnW7S8Srsx1xS8F4TZbh58SWVGp80Zj55YcUWuVuzX7ekDSwhUcbz2ZCpzZSEFh-_Ccm2FZoFaw2_Wnfv6gXZRWIzdmXTT5xbXihzC9DdaxGCg6VOkjVsleV4YVf9Cgi6RvZlH5QFCUNZKfRq_pyGP6_bci9MuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d45nqJTCEMguHFqWrhoY23sDiGtwcLoNwEZK1mkjXaV7MnCg0pmZphotf6y7w7cswQ3kdy3dQ4YLQBaXv0u39uDP6_q4JtXOkWLWUwXs-Ga4NzCjBBtV7K2EJrVYqB_YGIYTAnhQNILa5ovF-88hGDWL8jPJ2hsPlOlQYI5LTfE5OJO3bVBmUR3vyqZF-v6VLcjXkUn8klgeI0meOHw35Uh6nnWeNym1Cg7UCyieuPYa8HdcXn_U4BPl7KYQiGcyNlooGlVMFBWEX_AkZebAhd7b6AMSMsQjW8xApkxgFBK3JYghLJWa9WWx0dJY49Ix_-GX3JJz8wI4EZBxKYX-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gnmkm8ZnbTS1TmEVfZk3T0_i1EuJd3rgVhiFA28HB8tn5tftb9Mp3ZDs8Ert-SmtqESZmWq5lMY4Vj0XZB6Z66YMScz-8ow9v0flT0jACZwg-KO6p8SOvXXUL2cL3wdrU9nZE-56qLL9inCPZzw7HJqr1MUBNd8T_cPOpznQMcDluLlikifu4IrkY3EObt8Ota_mrIEhnNB5pIlyRNU_ZsOgcWE7qBnb-iDSeUcq_S_qvn9g2ySX4_HfAr8oFyFr8AlHfwDisOqnVoZ1XlKgcOEEYm9CjcNCFZlenlYhoGR93E7ofVoPz0E18wK0WolgTN3DelCnCmZgGEOqIU50Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E58zabdNTbg-ROBE_gn2qnHMsOHrtshuYNPakF7MpgBLCMgZjvFODfDLSZhI-kPONKyXR_3gapQnq9-ZnuiSFDgfWn_C99F3lM-ZQFR1coJBe2z-MdBWyDwnlea1piP01lCe0IOQmVPah4al8Q9Y4ZXJjebqT2R9doiZbcxSEIjlsE-qoUXNiduJtje6O7b75ZjkvhVNpeyxzratl9xrB4oKBOAoaHRKIcLcLiaYS7SkmGnxFA4LEVH02oI_783C0GXWdP1cjG_736kdzjLnmELAts-_6VfjlK6MEG0hY2-nsuJqKGu_qVLGw5sxJHOQhWk1qm4YP_uTrejOOhKQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OyhTORPFOL3m3NbJo2uu8X7uFDwV7kPe06B6-QhLoxOA_5307OHJwkL8cD2eMhZwnsVFxMNuwL6blo7GCz5pAyjyeC1HHsu6uPgSXFnzXKyX-YY7Jq-gtkEZ_MG7Gc370vFej7dUHnCxhldoOqR_5idqc3XEaIhmyTD9xbCH9Pqxk5AgQd7jAB1vkK5udT9CgLNXd1wvWzuXIORRMeA73LHmsLBzjQI_1DRTEi-I34AK0WnI9jGDES6LsSy4Q1WYJ0sTQ0_J1D3EvQqCUj1ha5LDum983c5bbSSddKWyg6dOfgdRcw3jSS_VIq_ULEF00uyvsSj-LtYAH4o-XQqTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8jbhoslNgYr_6ySKCjQFEi8IZfRVr6DA4Vgdult0p6suH2QdUsBDEXi8AnClJDCapqXw50nwPz6kNRbNVSb9UJ3jpd735xKRIEYltjwmGu0MJKdb0iU3gOzLYJjhA3_T8bCHrPBIUcqae-bB0F2yehDi0k7Q6e_52s9WdG9cdnV_75uCPQjTPpD3xF5mhrzzKSqV7z1Ffng7nb5ngzOBCGjyc2V7mRajF2ff2waxncAP3crtttZN2FWWYedamOZdtfhf4Ay-MmVkErGW6VmGhOgvE5G4n34lF2qDYzDaSZKjeY59AIROBq_b0wqoluTkUD8vE3ANzEr3sbB5Ma2Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSyueKMa5BaNdbDLvk7NO4lm79gzUQP5zufvuHM0PcWcijDHVuTL5Z0v44mEvc-oz_NwBoKKREcARntKgiPoaS8a_kCtcL8FeOtwoS2G6W6fhUC0pvlYc4r0YBwPsQZxE4g2i6rJCj4EPrthGr1Iffu2xs__qZ3ntQVuePBkQ2tqUV-z53tn3ja2gAEUKMPAb5NnxwHvC8zy-AYhsnrMKQap3ry3233gzmPAlxsuo8CDjRvez8iXFaW13kn4BCiJqGZw5RQCWnPe_kRWR8-Fm51ws4_d8uOQX9nBtFUHIti6hClU0P_763INX4bnBu7kFLTtx9LmiZO05FKmMDDy2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
موانع و مشکلات  شما مخاطبین گرامی برای  دسترسی پایدار به داروهای ضروری
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/687980" target="_blank">📅 19:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687979">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd9xFD8n3uYI83rZCK5pUwZ8U6zQsPO-m1coXB36p185g7pqN9y43_C2bnlgnrBlyYi_u0-Wj6DnGm7FcYqbCvxf6V8amiJ4WBk3ain_4SgAV2rk4WUiJR79h5QiPXzHgMcfjFPB0n4HeRBTYJsi2MmM9aVR6ydS-nJTjKwfpqpnLXWbiSvuKwdW1uK_njE0S8cYQgabZsYX0QxAqjK9gSGIgItHCbPULn4lf51zB6c06XDXKoeFRGKVZd_TEN9eBZEzQvAskIOdn8LMIynRAQtF9BXtK7XFzqTDY966LDUmx0JtzbBG_hhGXSYrPkNTaN6ECPBt3kj4-yW2oRZ4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت برنت ۹۸ دلاری شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/687979" target="_blank">📅 19:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687978">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsJMj9Vgz03WDlBYfmi2V3k4FTcgJ1L6Mdx5c_8EYGma0uTi6dYkmGDYF8cJi3SO7Y-jxJhPDd0IF4QL7iDiz_02O7d-YwgJEohTGtJZUDwc1X3LJ4K_8g6md3cvOgtayZT_5tUj0ncl2Gv9uVD4XHRriyXipNr7tI02W7gTfEHLGM3C00JLLbAgvRennW_iTk85SAx6TFjE-f2dkoSV4CqicLtiKfEB4r1czvDPypQ26z4DfGSw_yIO5zx3imx_v_-gNDpRDaT-71iKU6F2m68OG34i-YM8sl1HeKZxPaxuRPOCTQez-tuQOL08smFf-zxZWvPyQ2GfUYdCCD97Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ به مقاله وال استریت ژورنال اشاره کرد که در آن ادعا شده: سران ایران خواستار پایان جنگ شدند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/687978" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687977">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سیم ۴۵۰ برابر شد اما برق تنها ۳۸ برابر / صنعت برق با طلب ۳۰۰ همتی چگونه رشد کند؟
مهدی مسائلی، دبیرکل سندیکای برق ایران در
#گفتگو
با خبرفوری:
🔹
مجلس یازدهم قانون مانع‌زدایی از توسعه صنعت برق را کلید زد که جای تشکر دارد، اما این کار خیلی دیر شده و حالا با اعتراض مردم و صنایع مواجهیم.
🔹
۱۱۰ هزار میلیارد تومان پول برق مصرفی صنایع به صنعت برق پرداخت نشده است. نتیجه‌اش هم این است که پول پیمانکاران بخش خصوصی پرداخت نمی‌شود.
🔹
روی کاغذ، وزارت نیرو متولی صنعت برق است، اما تداخل مدیریتی داریم و مشخص نیست واقعاً متولی کیست.
🔹
دولت دو نرخ تکلیفی و بهای تمام شده را برای برق تعیین کرده است و  قرار بود اختلاف آن را دولت بپردازد، اما هنوز پرداخت نکرده است. بیش از ۲۰۰ هزار میلیارد تومان بدهی دولت به صنعت برق است.
🔹
وقتی صنعت ۳۰۰ هزار میلیارد تومان طلبکار است، چطور انتظار داریم رشد کند؟
🔹
از سال ۱۳۸۴ تا ۱۴۰۴، قیمت مس ۴۵۰ برابر، آلومینیوم ۴۸۰ برابر و حقوق و دستمزد ۸۹ برابر شده؛ اما قیمت برق فقط ۳۸ برابر! مگر می‌شود یک صنعت زیربنایی را این‌طور اداره کرد؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/687977" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
کارت امید مادران شارژ شد
معاون وزیر رفاه:
🔹
مرحله پنجم کارت امید مادران شارژ شد و مشمولان می‌توانند اقلام مورد نیاز خود را خریداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/687976" target="_blank">📅 18:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687975">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd014bb00.mp4?token=RLy4g-MWfCUodM8dH9X4lPhtZXOJAI5s90Wb5OJxs90ZJ7RZJ0riUrD92avZn1zYcPNEveVz7neDVkLQslAaBrcX9GILLA8YASlWjb3D_PM4yOnnV_TBTxc8MtZJX38WkeKFtYDm35fuxOCZe3DWELDIYsnODzzj_2S_s_DN4IeZ-2ww87d2Crhzjfz5-rBdyZkoaS1978IowOqaUFt_14bOJSCtjxaXSC2goOdUL3HT3gtQ19N4lGhMgJDk97Dm-5Co-WM7UCpp9OFAVc7s_eVsmClTAdLFTbo_IJqBVkprDGp9wpFwXJHZSsgixuQA2ZK61GXdhKSVBpx6Y88YqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd014bb00.mp4?token=RLy4g-MWfCUodM8dH9X4lPhtZXOJAI5s90Wb5OJxs90ZJ7RZJ0riUrD92avZn1zYcPNEveVz7neDVkLQslAaBrcX9GILLA8YASlWjb3D_PM4yOnnV_TBTxc8MtZJX38WkeKFtYDm35fuxOCZe3DWELDIYsnODzzj_2S_s_DN4IeZ-2ww87d2Crhzjfz5-rBdyZkoaS1978IowOqaUFt_14bOJSCtjxaXSC2goOdUL3HT3gtQ19N4lGhMgJDk97Dm-5Co-WM7UCpp9OFAVc7s_eVsmClTAdLFTbo_IJqBVkprDGp9wpFwXJHZSsgixuQA2ZK61GXdhKSVBpx6Y88YqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور تفاوت انواع باز کردن رو در زبان‌انگلیسی یاد بگیریم؟ #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/687975" target="_blank">📅 18:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687974">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a9998442.mp4?token=r0Pfwbza1J9rKRYS7d5MLzsoMCnGbi5jQU7O8Oum1ffsRn8IuybwVw4zrSWreovqrEqBre1JVJbjHn4MpYfI05b9lTsuQFrMVaEl1duL7N84zxrLnOfKrwMBm4QRHMBBKE9g9wZenuGpJGmQPtWZqqPSHgK6HF6LT6jX8ch3B-fS2gzW-KnxHaqs-sa590Ek9JPPHR8qusctMesylriWX6Vve1--pVx4Rg3x45MJ2cAL5Q7QETMmpA5aFrknxgzBmIiGkCgFmq1-1AkXncxrj-CPScWLjSQf-90gnAi9e9vzfdjJkAr18xeI2ouStx1Xa0Oi6H3MwmmlVUssO0f8Lj6Kmw-t-5MQRFxdq5HKWr-63MhKpLX5Oa09E0pOpZTeI51s_jcTYyqqUS8XDNsrbwcgP88bROcV0IEFGEzYV7TWLPQV2teMPAxSTCm0WHqP6C1oYMs-mUGFAOu2Q26AskZZASo3Q94ib_Ra5JJDlTc2XTdt8QG8RY2KvHTpgDUmu0kUpABF8NcIziTyezuNFOEsrci6llyDEAlwf6Qy6LnKnrvDJs2QLpSMLOFAbXc4mTIbbOfaquTP4jjV7H_8nEeJ20AkhAyo_P63CrrrkcIYunGtnIG5zmBAIlR84_rn6WzR94g4VEJfmUWfrVZVJ9k37IEOJ3XkocubUHAtsEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a9998442.mp4?token=r0Pfwbza1J9rKRYS7d5MLzsoMCnGbi5jQU7O8Oum1ffsRn8IuybwVw4zrSWreovqrEqBre1JVJbjHn4MpYfI05b9lTsuQFrMVaEl1duL7N84zxrLnOfKrwMBm4QRHMBBKE9g9wZenuGpJGmQPtWZqqPSHgK6HF6LT6jX8ch3B-fS2gzW-KnxHaqs-sa590Ek9JPPHR8qusctMesylriWX6Vve1--pVx4Rg3x45MJ2cAL5Q7QETMmpA5aFrknxgzBmIiGkCgFmq1-1AkXncxrj-CPScWLjSQf-90gnAi9e9vzfdjJkAr18xeI2ouStx1Xa0Oi6H3MwmmlVUssO0f8Lj6Kmw-t-5MQRFxdq5HKWr-63MhKpLX5Oa09E0pOpZTeI51s_jcTYyqqUS8XDNsrbwcgP88bROcV0IEFGEzYV7TWLPQV2teMPAxSTCm0WHqP6C1oYMs-mUGFAOu2Q26AskZZASo3Q94ib_Ra5JJDlTc2XTdt8QG8RY2KvHTpgDUmu0kUpABF8NcIziTyezuNFOEsrci6llyDEAlwf6Qy6LnKnrvDJs2QLpSMLOFAbXc4mTIbbOfaquTP4jjV7H_8nEeJ20AkhAyo_P63CrrrkcIYunGtnIG5zmBAIlR84_rn6WzR94g4VEJfmUWfrVZVJ9k37IEOJ3XkocubUHAtsEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپ جدیدی که سایت حسن روحانی منتشر کرد/ روحانی: دوقطبی‌سازی میان موشک و دیپلماسی بی‌اساس است
حسن روحانی:
🔹
حمایت از نیروهای مسلح و دیپلماسی منافاتی ندارد و «موشک، پهپاد و مذاکره همگی از کشور دفاع می‌کنند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/687974" target="_blank">📅 18:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687973">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سخنگوی هیئت‌رئیسه مجلس: خبر مخالفت هیئت‌رئیسه با خرید تجهیزات و تسلیحات نظامی از چین کذب است و مجلس از هر اقدامی برای تقویت بنیه دفاعی کشور حمایت می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/687973" target="_blank">📅 18:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687972">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95959f5d94.mp4?token=paKGKxy9Ndz54AQb-Bm8OUBqMMbW1_cYC2y51seySrH-qn3e-G5C9KYVb7QZxM2EMrMYBP9T14-Bqq-XU5QEmH23pKREX3jtTOLjMaZNnxciVicRCDbOEajFArSRwtZ1ExJCkPRrt5k99wEEDCRB7vNZi7wHy9LsPQ3UeZ7U3E8ZQZWQvH0oLViwwNHfAaCKOKsSGSUqvvYKBzxi-V1M4vW8PJvkYoRC4iau0WDXyCPJeFzQli6X4-4GM_9IUPfusFDaoFxHfAXN0sRagk8d4kyU6PqoPWWLGPEzHuEIEAjRvpdbM4Oqoj7YRqI6u-W4Kp4mjJNCQ7UVaW_2YRPYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95959f5d94.mp4?token=paKGKxy9Ndz54AQb-Bm8OUBqMMbW1_cYC2y51seySrH-qn3e-G5C9KYVb7QZxM2EMrMYBP9T14-Bqq-XU5QEmH23pKREX3jtTOLjMaZNnxciVicRCDbOEajFArSRwtZ1ExJCkPRrt5k99wEEDCRB7vNZi7wHy9LsPQ3UeZ7U3E8ZQZWQvH0oLViwwNHfAaCKOKsSGSUqvvYKBzxi-V1M4vW8PJvkYoRC4iau0WDXyCPJeFzQli6X4-4GM_9IUPfusFDaoFxHfAXN0sRagk8d4kyU6PqoPWWLGPEzHuEIEAjRvpdbM4Oqoj7YRqI6u-W4Kp4mjJNCQ7UVaW_2YRPYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی آقامحمدی، عضو مجمع تشخیص مصلحت نظام: بعد از انتخابات آمریکا، جنگ به حالت قبلی خود بر می‌گردد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/687972" target="_blank">📅 18:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687971">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M6ROlQUO9sFqpCQWA7IvQRht69ZpHKh2jRElvV3MQUxRTTxg7Mo5KBHL41iU0HVro8kp1kD3srRuTGtKW56B83qT49VPEw3J02XHtHWvvmq9o70eoypCmlhriMKvK9UmkmszczghYDaxaCcoTSYoIyjTcKvprz_CTiAKcZRjWYzO9rr4iNmYv75ID4HY1dGwFka1KPa4T7a4FQjmDkicC3GZ26w3nqI6lJq0UK_gE3E_4aIjDogF5EthOlwix36kNlRARhpX5r_Sgi2ZOq8NDXWB4QctKp9BGHUB4CFmfA7JE6vWj3vCsV_9r12HvhI1f_IzAIUXayKF33SwxLmAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درس‌های سیل مرگبار نپال؛ گرمایش زمین چه بلاهای دیگری سرمان می‌آورد؟
🔹
حادثه مرگبار و ویرانگر سیل و رانش زمین که هفته گذشته مناطق مرزی نپال و چین را دچار خسارات فراوان کرد، یک زنگ خطر بسیار جدی است که نشان می دهد بلایای طبیعی ناشی از تغییرات آب و هوایی، چالشی جدی برای تمام جهان ایجاد کرده‌ و آمادگی بیشتر و اقدام جدی تر جامعه جهانی برای مقابله با "گرمایش زمین" را بیش از هر زمان دیگر ضروری ساخته است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3243383</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/687971" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687970">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8spscSmCAZQsQpDPTSylj1yD3CL0UWQT7nvMWtg_9edSaHLbSNt6qbyo8HXv-L1ovSlJjvMXr_03VKc0ZcjFlut2zJym5b-Un1n_0GB6theT27ls9QXQ0BuAuOnVn6KV2TqKIbFgeST3qmwq7ePwSh_ZfHEIZmu4-VlRS6QPmnLvRHxPwVkdGxwocwLF_GdSxd2TpjVn2kNHtAPTG3wAayNhb0-e5H3gV_dvQtohzbHO3dE3oY24f0-zIeiVFg7DGN9q15gVPNIZhGobvVNU_heMpRPOuZVU38PuWR5jJxcvv4TWhI4VJlK181_L60pzrv6Gy7oUTfVb3vVUB1YQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۱
شهریورماه؛ آخرین مهلت شرکت در جشنواره بزرگ قرعه­ کشی حساب‌های قرض‌الحسنه پس‌انداز بانک سپه
🔰
آخرین مهلت شرکت در چهل و ششمین دوره جشنواره بزرگ قرعه کشی حساب‌های قرض‌الحسنه پس‌انداز بانک سپه، تا تاریخ ۳۱ شهریورماه اعلام شد.
🔸
به گزارش پایگاه اطلاع‌رسانی بانک سپه، چهل و ششمین دوره جشنواره حساب‌های قرض‌الحسنه پس‌انداز بانک سپه با استقبال پرشور و اعتماد گسترده هموطنان عزیز، تا پایان شهریورماه ادامه خواهد داشت. هموطنان و سپرده‌گذاران گرامی می‌توانند تا ۳۱ شهریورماه جهت افتتاح، تکمیل و افزایش موجودی حساب‌های قرض‌الحسنه پس‌انداز خود اقدام نمایند.
https://sphbank.ir/news-1301/14050616/5349
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/687970" target="_blank">📅 18:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687969">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a87e72f58.mp4?token=KB60_5DbsEZEZIuHxsTh_Uehy4jpEaiw0-hmp-UQIYoExKZJQpd4nvyoy2FwEnWFOOTJnpJhEJ_1PwW_tzQIV6cVWMuEYFiPt0To7rk-vI8qL55JOtuc1wUsxyaMmvS5IIQ96ZXG_8ERXcEJwmQmPTB4M--NXl5Cwb2JjeChV-tJifYvHtMhq0lqqKac5DyQAZEQedi0sCvgBZW1CwZUohtFU2_CltqWN6gdoQyJ2uF2F-2lEc7RS1uAPhfqaPp0Zw5FfOAlW1PdkGYCHzpbTUByVDwShZm8IzIpxlnH6oliJZ3ypnusw-L3lLyubHlAExzTIIwtbC1xtgNBwbOGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a87e72f58.mp4?token=KB60_5DbsEZEZIuHxsTh_Uehy4jpEaiw0-hmp-UQIYoExKZJQpd4nvyoy2FwEnWFOOTJnpJhEJ_1PwW_tzQIV6cVWMuEYFiPt0To7rk-vI8qL55JOtuc1wUsxyaMmvS5IIQ96ZXG_8ERXcEJwmQmPTB4M--NXl5Cwb2JjeChV-tJifYvHtMhq0lqqKac5DyQAZEQedi0sCvgBZW1CwZUohtFU2_CltqWN6gdoQyJ2uF2F-2lEc7RS1uAPhfqaPp0Zw5FfOAlW1PdkGYCHzpbTUByVDwShZm8IzIpxlnH6oliJZ3ypnusw-L3lLyubHlAExzTIIwtbC1xtgNBwbOGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستی خط زرد‌های پیاده‌رو چطوری اختراع شدند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/687969" target="_blank">📅 17:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687968">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlGrFho9QqH45ooGf_Griby1I7PFnq3c1oDPW0iob-KKbQiY3xY4VIvo7_1MceUj6Ze3hFwdDuyQxGWGIPgeofVMWQPF97b6DSispZHT9IMXKMxR3o7oT_HaklENDHGCS--jczA95TnwRtCKKgNJAnHPlWxF8VdC_QvoX47-nuQzfXjdT1TSAMGtFfyPdC315v6AtX7FrVZrRKpH6KCWgGSSHUkkVZH9W0-mc6undWSx_oIsMGcsSmv4Z3a480_HfxFU77CQeUvryVqqvC9qb68hVGuG91rUM1JS9pxFf64MYs1Iu1CXaWoiOa2U8t9lJ43uCw_g8lKN5YjL4rRChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمید رسایی: این کالابرگ نیست کلاه‌برگ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/687968" target="_blank">📅 17:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687967">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu86QpTdFLUegSMN_npIhIBAe_RMp6B0dehnSpfAvO6NohCwrPYXdP5SHLSi3AyTPM6ufnV83QeP5Upg0rIGaG1pl70tv-JVBSnEVJc6QqnXJ-Ld8SXYACdxa2YaIx7hhnfvFoY5pwFnvTFXGM5ayHLwZkmhvrgXQ77UKvShbqWQyHiEZ_-FBjlcWekIdx4-ufJlXoBpVyYIb0tqdtUHz7xuqLf88t0lzlYs_silQTnPt1u22LYTYPoxYP5LCxw57hMhCupldN5wrS6n_jDV_-EPPiS62VIlfi-lsVzP_LnQQ6bBgur6OLcpfNiQoSSDCEn5QdN1X8X8MRCYEbpoBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمد امید بخوای طهرانی
🔹
کاندیدای مستقل سومین دوره انتخابات هیئت مدیره کانون وکلای دادگستری استان تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/687967" target="_blank">📅 17:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687966">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نهاده‌های دام و طیور تا ۴ ماه آینده تامین است
داوود رنگی، رئیس اتحادیه واردکنندگان نهادهای دامی در
#گفتگو
با خبرفوری:
🔹
در حال حاضر از نظر تأمین نهاده مشکلی نداریم و ذخایر کشور به اندازه مصرف ۳ تا ۴ ماه است.
🔹
در نهاده‌های دام و طیور وفور کالا وجود دارد و رقابت سنگینی میان واردکنندگان برای فروش شکل گرفته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/687966" target="_blank">📅 17:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687965">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
استفاده از مسیر ایرانی در تنگه هرمز همچنان در اولویت است
🔹
طبق داده‌های مارین‌ترافیک، عبور از تنگه هرمز ۲۸٪ کاهش یافته و از ۴۰ عبور ثبت‌شده، ۳۲ مورد از مسیر ایرانی انجام شده است.
🔹
در مقابل، تردد در باب‌المندب ۹.۷٪ افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/687965" target="_blank">📅 17:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687964">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amf-XiCFDPceYDrZwKHH28jq-jkbK0imRKfWh8_birQSLCyVZDrcwcj0LSnpzyUEh57Co09XEiH7kxBJrQfhsnKVgAFrrtJaDClqpOO3JipXDHLvQNN5wi-jCFI8FjTuzzSDNArEEIz-b9rrCbUNiXdXhnttrK6YaWHDnd1ifMNfx8EE_pOOCk-fEmeDst2kpG0XTmsUstPpdXcq90bJL39Y0K8HdZlEyVigkwVHDSCbDvLsV5cxkPJUEgyAt_ud0AyfM1oWh1auIHGJg4K5WX0-WmbMeZsqYnAIr3sPQjK98n2haiFmOeIDH7bdBS_xnK5njdKFxcdYtXeComDImw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهندسان ایرانی خسارت ۲ ساله در ۴۵ روز جبران کردند
🔹
کوره قوس الکتریکی شماره ۸ فولاد مبارکه که پیش‌بینی می‌شد ترمیم خسارت آن ۲ سال زمان ببرد، با ۳۹ هزار ساعت کار مهندسان ایرانی ظرف ۴۵ روز بازسازی شد و به مدار تولید بازگشت.
@amarfact</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/687964" target="_blank">📅 17:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687963">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAdad │ آداد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1LoUol7kHfJvOYBhCi49x0pl6Ipk3gInSef_wDw4AqDnJJaWCUyuz2NsVpGHND3ImAIt_eJ_oSDIx9ZaIkrkzyR24g_XfIlQdc94jsQsOy-8HaUFnNj9xx8yuDtMk82hH6aQm1-V0TyQ8UFP-I-YMnpdagHiu3NRoEAAE2MnmWe8AGCs4bkGsgsxSbVCIEUOOdXvqCeYd2DCqnTZVLm_0ah-9tgIwYEGzdP3eDX9LQyThfTyUMo-HdZwYX7IZ6-8V1dQqTcn4j798uzoW3zDPTHq8xcJLYog7OZfpzPBu2W48Sc126RPCmlSOJO1oiSkBLJ2vGQIgNcTptY7-sY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
قبل از هر اقدام حقوقی، از آداد بپرس
آداد، هوش مصنوعی تخصصی حقوق ایران است؛ برای بررسی مسئله‌های حقوقی، اسناد و قراردادها ، تنظیم اوراق قضایی، انجام محاسبات قضایی و آماده‌شدن برای قدم بعدی.
با آداد می‌تونی:
🔹
سؤال حقوقی بپرسی
🔹
قرارداد و اسناد را بررسی کنی
🔹
مسیر مناسب برای مسئله‌ات را پیدا کنی
🔹
پیش‌نویس لایحه، اظهارنامه، دادخواست یا قرارداد بگیری
👇
رایگان با آداد شروع کن
https://go.adadai.ir/PGOFF4V
@adadai_ir</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/687963" target="_blank">📅 17:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687962">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8r_LejXW-FU-n_0uoqs9eQdIyMNcpTHURm9KPX02qGPY6mXhD7GtjlQlyb1iIgeL9jG4lc8sYgHhm8g615j_yTSyESeMRVCWrfu3VVb3lu-gBlHW1t2yqp6QIhuGuL3u4vRcvi6xmgFqet3wa_nb-GIppARJweBtHiCLgjrCjBIox8vJlkivobi4Fu99vnbnrm0PrLFWxm8Y1UtNHRdihDKqcvi7Bc3dDfUFJdPFhFSddSOF8gG1vOkK2TqCbR3PI9x130dhfOXQNdT_8BCIf4lOfn5_SXxQGXgRfXHJOBlyFrcAOOrzUV5dADRTsTkefkBhEV3hxzncg2qb8_yFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیین‌نامه به‌کارگیری ایده‌های نخبگان بر اساس تأکید رهبر انقلاب تدوین شد.
🔹
حسین افشین، معاون علمی رئیس‌جمهور، در نشست با نخبگان و فعالان علمی و فناور خراسان جنوبی از تدوین پیش‌نویس
آیین‌نامه به‌کارگیری فناوری‌ها و نوآوری‌های پیشنهادی نخبگان جوان
خبر داد.
🔹
به گفته افشین، این پیش‌نویس در
۵ ماده
تدوین شده و اکنون در کمیسیون‌های تخصصی دولت در حال بررسی است.
🔹
بر اساس این آیین‌نامه،
معاونت علمی رئیس‌جمهور حلقه وصل نخبگان و دستگاه‌های اجرایی
خواهد بود؛ دستگاه‌ها مسائل و نیازهای خود را مطرح می‌کنند و نخبگان برای حل آنها راهکارهای فناورانه و نوآورانه ارائه خواهند داد.
🔹
افشین تأکید کرد این طرح با توجه به
تأکید رهبر انقلاب بر به‌کارگیری فناوری‌ها و نوآوری‌های پیشنهادی نخبگان جوان
تدوین شده و هدف آن، استفاده سریع‌تر از ظرفیت نخبگان جوان و فاصله گرفتن از روال‌های معمول برای حل مسائل کشور است.
🔹
پیش‌نویس آیین‌نامه مذکور پیش از تصویب نهایی در دولت،  توسط بنیاد ملی نخبگان منتشر می‌شود تا نخبگان نظرات خود را از طریق بنیادهای استانی درباره آن ارائه کنند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/687962" target="_blank">📅 17:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687961">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سردار آزمون در آستانه بازگشت به تیم ملی
عبدالکریم حسین‌زاده، معاون رئیس‌جمهور:
🔹
پزشکیان شخصاً موضوع بازگشت آزمون را پیگیری کرده و ۹۰ درصد مسائل او حل شده است./ خبرآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/687961" target="_blank">📅 17:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687960">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
بمباران کاروان نظامی مزدواران سعودی در پایگاه «الودیعه» با موشک‌های بالستیک یمنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/687960" target="_blank">📅 17:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687959">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
گروسی، مدیرکل آژانس اتمی: بازگشت به دیپلماسی درباره وضعیت برنامه هسته‌ای ایران ضروری است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/687959" target="_blank">📅 17:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687958">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
سهمیه هر دو کارت تمام شود، مردم چگونه بنزین بزنند؟
معاون وزیر نفت:
🔹
سوخت‌گیری افراد پس از احراز هویت و متناسب با سیاست مصرفی تعیین‌شده، امکان‌پذیر خواهد بود.
🔹
در این طرح اطلاعات کارت بانکی ارسال می‌شود و سامانه مانا کد ملی را به سوئیچ سهمیه ارسال می‌کند.
🔹
در آنجا مشخص است که فردی که به جایگاه مراجعه کرده، تا آن زمان چقدر سوخت‌گیری کرده و چقدر می‌خواهد سوخت‌گیری کند و سپس می‌تواند بدون محدودیت سوخت‌گیری خود را انجام دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/687958" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687957">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تکذیب شد/ تأمین اجتماعی توقف پرداخت معوقات بازنشستگان را تکذیب کرد
🔹
پرداخت معوقات فروردین‌ماه ۱۴۰۵ بازنشستگان از ۹ شهریور آغاز شده و طبق حروف الفبا، به‌صورت تدریجی و مستمر ادامه دارد؛ سازمان تأمین اجتماعی اعلام کرد این روند بدون وقفه تا تکمیل پرداخت‌ها ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/687957" target="_blank">📅 16:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687956">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/687956" target="_blank">📅 16:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687955">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
یکه‌تازی «وتجارت» در بازار کارمزدها ادامه دارد
🔹
بانک تجارت در پنج‌ ماهه نخست سال ۱۴۰۵ با عبور هوشمندانه از الگوی سنتی درآمدزایی و ثبت جهش‌های معنادار آماری نسبت به مدت مشابه سال قبل، فصل نوینی از استقرار بانکداری مدرن را رقم زد:
🔹
رشد ۵۷ درصدی درآمدهای عملیاتی
🔹
افزایش ۷۰ درصدی درآمدهای کارمزدی
🔹
رشد ۶۰ درصدی خالص درآمد عملیاتی
🔹
افزایش ۶۴ درصدی منابع
🔹
رشد ۶۱ درصدی تسهیلات
🔹
جهش ۱۹۸ درصدی سپرده‌های ارزی
🔹
افزایش ۱۴۲ درصدی تسهیلات ارزی
رشد درآمدهای کارمزدی، توسعه فعالیت‌های ارزی، افزایش منابع جاری و تنوع‌بخشی به سبد درآمدی، نشان می‌دهد بانک تجارت در حال حرکت از الگوی سنتی درآمدزایی به سمت بانکداری خدمات‌محور و مدرن است.
📌
بانکداری به نفع همه؛ به سبک تجارت
🌐
مشروح خبر
👉
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/687955" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687954">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12c7771ad5.mp4?token=XWEzghQ7qNMHjWl12eA8Bz2DWQaJxglJAqQHnQHsy6BZfHBYaA5oo4uzW294a-njecdeZxumKZj_cFUFuZUg7b40Xm9vV54rKrYxFVr6fwHt5f_wEmOvlJ4QClPY-AVm8UlnzWKK5yUofmKBgeRNoybeGVlYbJR7SPPJ1cO500yRH7vIogNwkZXmehvslGBmoKcRpVWNg_XWLNJoRLQw0bNEH_Q76QMlrrJtaTASj2XMnG9fdXw81b_UohhPDDpR3AQ_oz5UKm2U1qzWsN0zO1yhPh-V31KSwhQ7QVWIzbFvFQXwbNEDmi7rZSZstFNYfnydC5nKLNbTnON1azLc2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12c7771ad5.mp4?token=XWEzghQ7qNMHjWl12eA8Bz2DWQaJxglJAqQHnQHsy6BZfHBYaA5oo4uzW294a-njecdeZxumKZj_cFUFuZUg7b40Xm9vV54rKrYxFVr6fwHt5f_wEmOvlJ4QClPY-AVm8UlnzWKK5yUofmKBgeRNoybeGVlYbJR7SPPJ1cO500yRH7vIogNwkZXmehvslGBmoKcRpVWNg_XWLNJoRLQw0bNEH_Q76QMlrrJtaTASj2XMnG9fdXw81b_UohhPDDpR3AQ_oz5UKm2U1qzWsN0zO1yhPh-V31KSwhQ7QVWIzbFvFQXwbNEDmi7rZSZstFNYfnydC5nKLNbTnON1azLc2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ مجروح شدن خبرنگار المنار در حملۀ هوایی اسرائیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/687954" target="_blank">📅 16:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687953">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd99461d6.mp4?token=XpeqroL04yfKzglqiLaTOVlprUg4ZrjBVXKCtczNul29cTBUiY-M1scAPE0TRXiYuEtBST1JcMhoGEDdFkiEoGMHMvtqCHKw_WBqAnjbOzM_NrtyjMnBCNANQh5oezrtnMJRCjFH4FSvlNJQ0vK0au_3jwX7HW01mb2Z5XZI3GDvZJM5M6KeGnsdwENtDX8MzaYAnXzUdoHMHS61bHf-gqEVgaPD2bGs_Ly39eEgQQJjg7_DuJ2v3_PVfYKPaQyatCWpiyTqoI1kILBbPdaSGkjKBgZxE3utLb3_IloKhvb-eox5-n05KpsDeMUK4fGZj7orCUgxQ_HU-XCljOWwDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd99461d6.mp4?token=XpeqroL04yfKzglqiLaTOVlprUg4ZrjBVXKCtczNul29cTBUiY-M1scAPE0TRXiYuEtBST1JcMhoGEDdFkiEoGMHMvtqCHKw_WBqAnjbOzM_NrtyjMnBCNANQh5oezrtnMJRCjFH4FSvlNJQ0vK0au_3jwX7HW01mb2Z5XZI3GDvZJM5M6KeGnsdwENtDX8MzaYAnXzUdoHMHS61bHf-gqEVgaPD2bGs_Ly39eEgQQJjg7_DuJ2v3_PVfYKPaQyatCWpiyTqoI1kILBbPdaSGkjKBgZxE3utLb3_IloKhvb-eox5-n05KpsDeMUK4fGZj7orCUgxQ_HU-XCljOWwDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت وجود ماینرها به اقتصاد مریض بازمی‌گردد/ راه بهتر این است که تولیدی ماینر راه بیاندازیم و دولت هم عوارض آن را بگیرد
مهدی مسائلی، دبیرکل سندیکای برق ایران در
#گفتگو
با خبرفوری:
🔹
مردم بخش کوچکی از تقصیر مصرف بالای برق را بر عهده دارند. ما از درآمدهای خود مالیات پرداخت می‌کنیم و در ازای این عوارض، از دولت انتظار داریم یک جاده‌ی سالم برای کسب‌وکارمان فراهم کند.
🔹
درباره ماینرها؛ آن‌ها فقط برق مصرف نمی‌کنند، اینترنت هم مصرف می‌کنند و محال است نشود آن‌ها را از طریق آی‌پی شناسایی کرد.
🔹
علت وجود ماینرها این است که اقتصاد مریض است. تا زمانی که اقتصاد درست نشود، مردم به دنبال راه‌های غیرقانونی می‌روند.
🔹
اصلاً چرا باید جلوی ماینرها را بست؟ هر چیزی را که ببندید، بازار سیاه درست می‌شود. ماینر مگه بیزینس نیست؟ راه بهتر این است که تولیدی ماینر را راه بیندازیم و دولت هم عوارض آن را بگیرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/687953" target="_blank">📅 16:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687951">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561ec2a9de.mp4?token=vFJzZTLozApemwEhIAJfxwSlIs9N_DHBI4qK9phj3I46SqywWE3Youn-tx2uAHDd1Cp7XLwdCgmMfPrh6sjcjealrBAtnawv99KrbFS34-hvzwvjN0nE2QHH77aq5KuYNJ9I5eBt9c2F3-gV9XmPqmRNURNLMiqUO3rw60-uY1pmgVx8dzQNdVoZUKcEctN9QZjUwpXjT-l4x_zVnTWbTS2IsG7eZr3kwJXj8n3Rr5xewzIPxm5LUaXi6YSLuc0A7bkoHL4gXq5KOelLoT8vTyWNbV_tk9sSe9w33zYGo1pCt-N4VsJEiiTB3sLF3H2vjiWtUknYLzaob3g2u2FAyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561ec2a9de.mp4?token=vFJzZTLozApemwEhIAJfxwSlIs9N_DHBI4qK9phj3I46SqywWE3Youn-tx2uAHDd1Cp7XLwdCgmMfPrh6sjcjealrBAtnawv99KrbFS34-hvzwvjN0nE2QHH77aq5KuYNJ9I5eBt9c2F3-gV9XmPqmRNURNLMiqUO3rw60-uY1pmgVx8dzQNdVoZUKcEctN9QZjUwpXjT-l4x_zVnTWbTS2IsG7eZr3kwJXj8n3Rr5xewzIPxm5LUaXi6YSLuc0A7bkoHL4gXq5KOelLoT8vTyWNbV_tk9sSe9w33zYGo1pCt-N4VsJEiiTB3sLF3H2vjiWtUknYLzaob3g2u2FAyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هرپولی که در حساب‌تونه برای ترید کردن مناسب نیست، قبل ترید حتما این نکات رو در نظر بگیرید
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/687951" target="_blank">📅 16:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687950">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه قطر: جنگ با ایران نشان داد اتحاد با آمریکا کافی نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/687950" target="_blank">📅 15:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687949">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5f662aa3.mp4?token=KMQnFqvPwIN85FVe7ZK3yR8-YqYYHQb9zhBvtcmm699nRvYMlAznCuVwnJ00mbZtLFCfENGDQJ1Us4NiHyjKss4084h_qU3NBv7s0YE3lw3SHNXHoyqItqJrWOLrFj3R4nk1CZA2evwID_ZQ-ypiRj8M3-o7ozNki3kr2Ao_zcPOyAPUgsNYNeazDOZVeQaq0kctBPePEVfXRC_4SikBC-y8Q7XTV8TltP52S-f0x5L5Xo0Y8e40ek4cZ8aJeYJKoQIMyeeZxmUWdJYGpEDivsR-WXt5Y9nsDq4W4uIkWlmNPBMoBw8nxnlxkU1I2rEccVTHIkPp4hvP-Ymz43V-sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5f662aa3.mp4?token=KMQnFqvPwIN85FVe7ZK3yR8-YqYYHQb9zhBvtcmm699nRvYMlAznCuVwnJ00mbZtLFCfENGDQJ1Us4NiHyjKss4084h_qU3NBv7s0YE3lw3SHNXHoyqItqJrWOLrFj3R4nk1CZA2evwID_ZQ-ypiRj8M3-o7ozNki3kr2Ao_zcPOyAPUgsNYNeazDOZVeQaq0kctBPePEVfXRC_4SikBC-y8Q7XTV8TltP52S-f0x5L5Xo0Y8e40ek4cZ8aJeYJKoQIMyeeZxmUWdJYGpEDivsR-WXt5Y9nsDq4W4uIkWlmNPBMoBw8nxnlxkU1I2rEccVTHIkPp4hvP-Ymz43V-sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروسی، مدیرکل آژانس اتمی: بازگشت به دیپلماسی درباره وضعیت برنامه هسته‌ای ایران ضروری است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/687949" target="_blank">📅 15:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687945">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqLtq5zN7WYWxm299ti8BbCCpb9kTKbcv3hWsbNz0EI1q0F-yEJEnwTx9RMksGj1Vq05CweS_FGUjNANIArM6_AiKMrIFE0li4XFSW9Yt0GHi1SUpxDi_MIAymOI2gG5o9jaK1CQ0Nm8NmvbWaCb6C3w24UxrSXuZkGtE9SjHcZgFblAmste4goa1R3nrBCres0-IcC3bitZrgKviQF-4gppd-86YU6O63NeCe9ua-x-fK7AJMqA1tgOln2kRbZxAM-rVAkwTbqyBwKBOMygZJtqTPqstlegRECH7hlRqUwE65hJq7QF6MIbYFtDokfnL0UZVgwYVwevzt_74JDd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOkLbmIua-hgywhsqMYkGly6tjibZjZRgZi8mHEXdC2WZHaRkgbFa6cqn_--7kJvR70uWpU_7_AwDzqGLm5tW36Sw0yM-KwW4T_uEyIbxPrCkzuT2WdNx0BOcI17RdBjg2_tLIE4XVpwFtv6NPNxXDdskZtMWNWnH9KJVsKb8bhcN4pSIb5s_0LHE8y3u54-uczCjQHQP46AmszbxzLoMesRaNYXFZ9BfVFo3GB9ea-j0EKLfhZgNaKogaiBZIVGWM7ZvSuAvUqi8jgp8aK-mu4-NstiES11AzhOmP2LCvhrBxzjrswXY6sB3Nig_mSajlQuChLL29xtjhmvFPTqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiMcWNC34FnXDiZylyWJ90jjCD511e0qXH1XekmZOULiT7odTd-skW6u11Hzldq7kQkTXfQ97LajVXd5PSi1zzsnNt_DNmyHBlDFCtJ8VXhuduCM9JO0dhsTIiLNJYqqbcSnUjWqhaRVYlsYs1xUt7VxsErN4EmcMC3SxTQSu75XAHR0M_piIBd9rIBcalc_kwX78bOTypU1wj715FQHl2uj89rxA5Fx4F_Q9CkmWhowWgDjhzEIRFoG1YwHhAcpks-SliJJP0u_yfYDYnuCJpifakOqRr1rnvsUNItlvxERH5zxLClutDX8V4LdETN8AB9oNXMglcSS4AdanZwazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JPXt_7Dt7-2IcjGdbwqUOqJXgAkNDrL041uu3fz8Mm7TB3T7ZdsEEOEAj-Sr2Olf1LPRTGXdfc1MrhMVLOYuaTPT4IJyLkKFyJYVWVbA1MQI33IIFO4LbB7MxSWIcA5WOKtHkOvqzDTWQeVY0B4O817Jntu5_eK0hsG4K3QFoqilBZXkOjawl5YCaypjFPHEpYysDb6NvlG-H-opuN731YeZvbvhxPsPu4cD6GF2jZ6LgKgrQicmbKnv0bQH7QGAturMsZy80fuSJrZYECpPltJJYRZ2pDD5wPNs-hTeda3_AfHpIaiAzHVykISmn6dxfLRFbuWYFcPh2xtcxhk0VA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درخت سیب نیوتن هنوز زنده است!
🔹
درخت معروفی که گفته می‌شود نیوتن با دیدن افتادن سیب از آن به ایده گرانش رسید، در محوطه خانه کودکی او در لینکلن‌شایر انگلستان قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/687945" target="_blank">📅 15:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687943">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8679746b.mp4?token=fwYGp_3so0rvVKuf8EZ6q93_Xu_xNHd5p_2gggxd-BTfsN2-ct6-tIY6W7mnG05Vm7_z1BdMwy_9KXRr8nLEGUxaGBZdoNvJ0FqPEOuLRotU335LG6dCWzW3DPP_v2KYeR48ozfSZ7uPoNQs7IlDQLwSNiuiv7q4iHDJx8FZ3fUjlvHOk6D_loLNcDrhP1NGQjpxJ-Z-0jcMRUU0NDPmmSBYUIlj6W4GuTmSRgOrmYrfeZExxbLygjO18gL-yJkDrr-8CAJ1RlxjtRh8s2PY6PgDscJtSKYyhJ_-JCB5n1k3kGD_hdZR2GJXByCrBQOmRNlw3IsdMLamEXrnGl6CmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8679746b.mp4?token=fwYGp_3so0rvVKuf8EZ6q93_Xu_xNHd5p_2gggxd-BTfsN2-ct6-tIY6W7mnG05Vm7_z1BdMwy_9KXRr8nLEGUxaGBZdoNvJ0FqPEOuLRotU335LG6dCWzW3DPP_v2KYeR48ozfSZ7uPoNQs7IlDQLwSNiuiv7q4iHDJx8FZ3fUjlvHOk6D_loLNcDrhP1NGQjpxJ-Z-0jcMRUU0NDPmmSBYUIlj6W4GuTmSRgOrmYrfeZExxbLygjO18gL-yJkDrr-8CAJ1RlxjtRh8s2PY6PgDscJtSKYyhJ_-JCB5n1k3kGD_hdZR2GJXByCrBQOmRNlw3IsdMLamEXrnGl6CmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعارف؛ پل عجیبی در بوشهر که سوژه کاربران شد!
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/687943" target="_blank">📅 15:25 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
