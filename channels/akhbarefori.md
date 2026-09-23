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
<img src="https://cdn4.telesco.pe/file/sUmA3nd-B89jWW6HDwhHZo0ihHyuxftv5_fAebwwIAJvMmSCMjgr3nm42K229HPhRQX9QImlxeBf8fIW3OPmhm9bmcnpuw3sunaf7ewvfBLo19oonOvDpMyHuidhRw0CywTbwZ0xgO-cIjeOjJCfGnRVNev_k1AJWm2GE2teaiAEXDpsf9IKvGIZgNiVrSvFqBgfrn5G1B99mi-u6ZoImfT-vcrof1t-k1yslbapWGHkQA1WR3enu9II8tyP7T4rNL3cBlVDwLu6ytZ_anZmWTjqqM7QFhD5xJ8YF2d689jcaU8P_Uin06lMm-Mt87FzwvyrJYeK5TYY6M9ZoL3R-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.97M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-692249">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez0hkmU8OtKsbVjlAAs7Fwv3SFIIsuxsL783ZshHLtL3K0ad-9Gahe4RB6PCHWEHDL8VlbArXeBYsTnKnlQf0i7LG8T7P_zglW9J7p-dPopiMI_YyHj5gG2z_yDYX1LVKuItfq9Jlr--J19VmxIELoHPlkRjNn0afp4mntvb7oj0nrkXIxqxeetw0CoL_Eb8vXKerEoher7IHiegl_7IKgxGSXwoVEfk3y0DxNyiaRv1HsE4SKplT-zhUaSstYqBaLRJ53oVZoGY4E1roW4iBAJe8x9aR9dV0SBzoitgCCBxSV0eipIqgDADyzIeoeGKmCQtwQsU0Fa0zi1uKwZOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش میلیادری قیمت ۴ محصول ایران‌خودرو
🔹
قیمت ۴ محصول ایران‌خودرو امروز حداقل ۷۸۰ میلیون افزایش یافت؛ میزان افزایش قیمت هایما 7X به بیش‌از یک میلیارد و ۲۰۰ میلیون تومان رسیده است.
🔹
این افزایش قیمت خودرو درحالی اعلام شده که پیش‌از این ایران‌خودرو توقف تولید محصولات خانوادهٔ هایما را اعلام کرده بود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/692249" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692248">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ae946ade.mp4?token=X46S9FruG1ZCUx0e7F-7BVt04Ag3ORQRjKuas_sUQjBbZgTrpakyitGF60G3go5uApBFU4_a8xyVObV7jg3gA5u_ZHjNKsOxZVBATftfB_5jw8OzpisjHN_glJN0XD-es4xMIZSNW6Io1SlDsnsnOqrz0mCTwroz4aWjd9W00WxS60azHQH3QMuK87OYrgC4Y-LZ-3UF4g8PBI-d-o8-lQDYpAn1DVNsdwNB24IIP8-HqnFkYLYarEQriBnBkrnYwjBHco-ttt9X-axBJ1MMMcVHYbPW6npHwFYwsY1z7q9InV7-rBgNb1VlNjfmwwl-q95IHyTCti8DoaLgDYC97w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ae946ade.mp4?token=X46S9FruG1ZCUx0e7F-7BVt04Ag3ORQRjKuas_sUQjBbZgTrpakyitGF60G3go5uApBFU4_a8xyVObV7jg3gA5u_ZHjNKsOxZVBATftfB_5jw8OzpisjHN_glJN0XD-es4xMIZSNW6Io1SlDsnsnOqrz0mCTwroz4aWjd9W00WxS60azHQH3QMuK87OYrgC4Y-LZ-3UF4g8PBI-d-o8-lQDYpAn1DVNsdwNB24IIP8-HqnFkYLYarEQriBnBkrnYwjBHco-ttt9X-axBJ1MMMcVHYbPW6npHwFYwsY1z7q9InV7-rBgNb1VlNjfmwwl-q95IHyTCti8DoaLgDYC97w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک مادران شهدای دانش‌آموز لامرد هنگام به صدا در آمدن زنگ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/692248" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692247">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vys3wZgi3zRyN3uMcpBEvUqMkESvg7xOno9wDB0bVlxd5jDrAaQ8W0W-ZATxm8WRruf7mv18E5djCs3FutWgizYnrM_fwfxTzv5nbHpxuawUCMtTfKtoyGavltYMwbFSi0azfRkcimHJt9XXkyxKJyYHROS48KDP-NQ-7PjEyX7AstqVSs32nMtKLn5ued06Pi2lEOLixJmPQd5O1S-WWo9DAkPnykSLFrO20OsQA38r-93F5ganTq8C1SmYLkgOgiH4FdJ55ceZtAHXUNCaJbgh8NH13jVBlzNBMV9XZoDA_DiftAIaMZFAXZZ5H7QRmaC2oIZJxDj7EuWnx1xxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایدن مصطفی حمید؛ خلبانی که حلبچه را نجات داد
🔹
خلبان عراقی، ایدن مصطفی حمید، دستور بمباران شیمیایی حلبچه را رد کرد و صدام او را اعدام کرد. پیش از اعدام پرسید: «آیا ملت ایران و کردها سال‌های بعد مرا قهرمان می‌دانند؟»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/692247" target="_blank">📅 13:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692246">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224b8e6583.mp4?token=k84cIBSrahp3bUqEQH1IIyRAqot_1AlAT-I896NNEaAdzeZdzcQgNZM2fBof9py1EQlVuigKW0iTU-2xsHTvFZW5W8wZUeYDunxt6y2CTJGeJ7WQY7lMIxlXhEO7KmCGfeutHlW6lfuSo47vt3YE_XM6WUa0w1-4i4wUnFfjqcihlyShnP-ROnuwrewesThlZ7Mi2qcqDAP35jkzXG5PqqcFawTkpNr6CILAYRJ4JnowSyPtkV6IHyg9kgAa3qjzzVwqdWrnT3Ht3pE6YCQI0Pp6hWdqDi5OV5WNQBPBHjKDJsvPVCV4uiA1-jQGFkOF_XuzWatBslkiLdyiqQvrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224b8e6583.mp4?token=k84cIBSrahp3bUqEQH1IIyRAqot_1AlAT-I896NNEaAdzeZdzcQgNZM2fBof9py1EQlVuigKW0iTU-2xsHTvFZW5W8wZUeYDunxt6y2CTJGeJ7WQY7lMIxlXhEO7KmCGfeutHlW6lfuSo47vt3YE_XM6WUa0w1-4i4wUnFfjqcihlyShnP-ROnuwrewesThlZ7Mi2qcqDAP35jkzXG5PqqcFawTkpNr6CILAYRJ4JnowSyPtkV6IHyg9kgAa3qjzzVwqdWrnT3Ht3pE6YCQI0Pp6hWdqDi5OV5WNQBPBHjKDJsvPVCV4uiA1-jQGFkOF_XuzWatBslkiLdyiqQvrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از این معلم که رفته بالاسر دانش آموزش و هرچی آهنگ میخونه بیدار نمیشه
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/akhbarefori/692246" target="_blank">📅 13:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692245">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
وزیر نیرو: آخرین هدف حملات دشمن زدن آب و برق است؛ دشمن وقتی می‌خواهد خیلی ما را بترساند می‌گوید آب و برق‌تان را می‌زنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/692245" target="_blank">📅 13:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692244">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff405a16bc.mp4?token=hSyuNpbTj9Wix_MZrhyv60eUWyA2ftI4d0MlN_ce9yTTBuoxAPc3BJqAXYyzHC4QXUTz8oPWfuXsyNQ9Gu-w9hdjRnuhBMjxpmv7w_mR5MZSmarpVrNiw3-LiHJXf-lUigu6SJhPofbgo-EXij8Vz3hSp-i2uyUfEeSNpcNzf0RoxgvJ6TBon26nFHN_Tg2J5W1tYJHvxMZRYKqdbm8HPs1HXP0nbpJwBMZ6ZG5_8qQj6Ijlh5zbqi-z1pVwsarREMUHB88Eisn3bJ9R5cgRYzL9Xtk7iKcGBBGWooWLqxlDI1cQ1bj_WR6WNdJLyyUWoNxmPQv_8wnRWGkPE-jpVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff405a16bc.mp4?token=hSyuNpbTj9Wix_MZrhyv60eUWyA2ftI4d0MlN_ce9yTTBuoxAPc3BJqAXYyzHC4QXUTz8oPWfuXsyNQ9Gu-w9hdjRnuhBMjxpmv7w_mR5MZSmarpVrNiw3-LiHJXf-lUigu6SJhPofbgo-EXij8Vz3hSp-i2uyUfEeSNpcNzf0RoxgvJ6TBon26nFHN_Tg2J5W1tYJHvxMZRYKqdbm8HPs1HXP0nbpJwBMZ6ZG5_8qQj6Ijlh5zbqi-z1pVwsarREMUHB88Eisn3bJ9R5cgRYzL9Xtk7iKcGBBGWooWLqxlDI1cQ1bj_WR6WNdJLyyUWoNxmPQv_8wnRWGkPE-jpVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرفوری ۱۱ ساله شد/از یک رسانه خبری تا شبکه‌ای با بیش از ۸۰۰ رسانه در شبکه‌های اجتماعی داخلی و خارجی/تلویزیون اینترنتی «مدار»و آکادمی «آوید» دو محصول جدید خبرفوری
🔹
امروز سالروز تولد خبرفوری است، از یک مهر ۱۳۹۴ تا امروز...
🔹
خبرفوری در یازدهمین سال فعالیت خود…</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/akhbarefori/692244" target="_blank">📅 13:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692243">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
فایننشال تایمز: برای نخستین بار، هزینه اجاره یک نفتکش غول‌ پیکر در مسیرهای میان خاورمیانه و آسیا، از روزانه ۱.۲ میلیون دلار فراتر رفته
🔹
حدود ۱۵ درصد از ناوگان جهانی نفتکش‌ها در سواحل عمان منتظر هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/692243" target="_blank">📅 13:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692242">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوهشت - دیده‌بان رشد اقتصادی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nspDSoC-GbUugv4RUJoqnPPNclK6MjyC6LLpka65AJyhG3q7xxOSnf0Uy4PNprPgSy25WC4nsIpejpa3_pn-X0HuHFjgnRbqyyrvoZVUi5v-hs7ySNVg1Z7VozNqiHnZOhDHJaIE-q9LEGyw3ICnAH1L7wTt66CiEC3ahEjJXivoXQy6vPkzLTVf23SC3p0CZAfdRqboMp_OpixVc2c9G-TxtHgUu1HpgiT_xrFJrxqUMlCSoczqn0SU-4rmuFgRxkHtY0OQqDk7Ge_8tVXpfKo4UCAaTuzDz-O0Mx4DVCbXzFaLrUs4_x_rw6nUXZaJ4DJOk5WMrpGckGu2IThIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزپاشی یا ذخیره‌سازی؟ درس گرفتن از تجربه موفق روسیه در مدیریت ارزش پول
واکنش عجیب برخی نمایندگان مجلس به اقدام بانک مرکزی
🏦
الویرا نابیولینا، رئیس بانک مرکزی روسیه، پیش از جنگ اوکراین ذخایر ارزی روسیه را
از ۴۴۸ میلیارد دلار در سال ۲۰۱۸، به ۶۳۱ میلیارد دلار در پایان ۲۰۲۱
رساند.
📉
پس از شروع جنگ نیز
مانع ارزپاشی‌ شد
تا نرخ ارز برمبنای عرضه و تقاضای واقعی تعیین شود. ذخایر پس از یک افت موقت در پاییز ۲۰۲۲، ترمیم شدند و
در آگوست ۲۰۲۶ به حدود ۷۶۹ میلیارد دلار
رسیدند.
🧭
با این وجود اخیرا برخی از نمایندگان مجلس ایران با انتقاد از سیاست بانک مرکزی،
خرید ارز و افزایش ذخایر ۴.۵ میلیارد دلاری توسط بانک مرکزی
را زیر سوال برده‌ و معتقدند اقدامی برای جلوگیری از افزایش نرخ ارز انجام نگرفته است.
🛡
باید توجه نمود که اگر بانک مرکزی در این مدت ذخایر ارزی‌اش رو بیشتر نکرده بود،
امروز در اوج محاصره کشور فلج شده بود.
زیرا
سیاست‌ تثبیت
در دوره پیشین،
ذخایر ارزی بانک مرکزی را به تدریج از بین برده
و کشور را با بحران مواجه ساخته بود.
اکوهشت
- دیده‌بان رشد اقتصادی ایران
@ecohasht</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/692242" target="_blank">📅 13:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692241">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b793d049a0.mp4?token=Fp6WRk--ECB7DFipTurdJVBPgPDHATej6TFD59lAmmAHcPB1LeAEDI1MjKA-2XyTXTxbQ5JnOhUrcN-jzIVcoi0HjqkJXZVIehKzRDD1z5OqvwIOaunSOB3-NvE16CBLDTimTnEID5t8zQnOLBOZPx0hPbVdiBLAJQmKUjh3ZVx8mDW3gPI_agk4aR8Js0C8uEcGEeTVyVsI4cogJF4Rr1_RC6jEEziqhDuKt0YZU8yj9xgeKuP8cfNZWGfpzLz-VQ05quPfsahG5S30zEYUzGtiHbdGVqcEt8T3MGtt6qYl2_Ny8u6NBJ_oblnECs6USFTQvRCjouhek4NBAdhCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b793d049a0.mp4?token=Fp6WRk--ECB7DFipTurdJVBPgPDHATej6TFD59lAmmAHcPB1LeAEDI1MjKA-2XyTXTxbQ5JnOhUrcN-jzIVcoi0HjqkJXZVIehKzRDD1z5OqvwIOaunSOB3-NvE16CBLDTimTnEID5t8zQnOLBOZPx0hPbVdiBLAJQmKUjh3ZVx8mDW3gPI_agk4aR8Js0C8uEcGEeTVyVsI4cogJF4Rr1_RC6jEEziqhDuKt0YZU8yj9xgeKuP8cfNZWGfpzLz-VQ05quPfsahG5S30zEYUzGtiHbdGVqcEt8T3MGtt6qYl2_Ny8u6NBJ_oblnECs6USFTQvRCjouhek4NBAdhCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر کمتر دیده‌شده زایمان اسب‌دریایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/akhbarefori/692241" target="_blank">📅 13:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692238">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKR5Vv7LjB8bS5K3W8zwC56Xyw3w1B8VHuzvrfSd0iK7rfmHDFf9RuHJ8De58pl9rikXKGmwdRet89wyGlbBFhk6gi8lQHsLki0Ig0vS9pLGV1ID0Xe3W55LHBF4pOZtshpP94PyrspjxESKLHZf_R0iEo7RxjnyWJBV3qdAwBW2-Eyj9UdjphgLZudLs30tuxNRsy6HU2u0Bxq6p0TOi-q_JyiTahPeYVQ_8NTuFHw-oCEl8zAOG1RZAPlufgKmd9buZ88Q54ucGpJ1VUm7FgSadn-aipf9p-uOXSz3jEbxmtPygasmUBpApUFxzePnoLbxGPJvwGUdLjdxyNYMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر آخرالزمانی از پالایشگاه مسکو پس از حملات پهپادی اوکراین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/692238" target="_blank">📅 13:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692237">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnTHPMB3YmHahuyafkDBmSgL4q7StkpmdQ70QyWk-UzaZ_kHyCJsMauDkBm2CsigQ0iTAJ3Tw4mV6JMDNv54Oa8gz18yYYoQKjl-KoTq8GRJOjzlsVZKV5tAwEVAmzF5s1XhTob7qg0vtvu3KAaGfEF7XGDlUHmW5P4cii-i8hAN4EJAhyzPf9mtjz2lsNWUsVLJQefTlpdGBWNTaAuSutuAfvZUDzk6Xx7OKoFV4qNEWipyoDJPdliCwpDfYuSeLTH1_W93odJEyp3ixqrQwQh75zMU6_oiU65G6ykupdKpq6VDEdtSvvHRK7_f0VJr9w2Am_atovvziEEUjG_OFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صداوسیما: با اصرار نماینده آمریکا دیدار عراقچی با ویتکاف در حاشیه مجمع عمومی برگزار شد
🔹
ابلاغ شروط ایران برای بازگشایی تنگه هرمز دلیل پذیرش درخواست ویتکاف برای این دیدار بوده است.
🔹
مواضع قاطع ایران در این دیدار به نماینده آمریکا ابلاغ شده است.
🔹
رفع فوری…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/692237" target="_blank">📅 13:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692236">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
کانال۱۴ اسرائیل: تعداد بی‌شماری از شهروندان اسرائیلی حاضرند با دستگاه اطلاعاتی ایران همکاری کنند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/692236" target="_blank">📅 13:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692235">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du1FnXII_pgRhDVW5GBL8gq2dwJRt8ac-N13AmGq1ShR4oO343ublca7nwlK3-3eCWsaNGNIvfxvAWjqHERI1X1j6WVjygY_OAKzp8v6p-mOkjTIveTq-qEP8Q67M5IyoC-QW2fx_X5A4ZB_qzACvDZaGoQzDcFdFL-DJOUfNWPzyq_oc4PXw-7V3oVMhkNAYTtMzWmhhiT4uuUvNJOKHuYdFohugMXWHeKmEIdEAnZSr6CHE88_51mh_KtgIBKCOyBgOD_W70EbF_y4dR7JYx7ATfEmx46SV-6YjAkT4zXPCCOwoNAmKqB53AYOGKSboSeSDNgiGditxLLq0X9aYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضوری که برای فعالان رسانه‌ای و دشمن، نشانه‌هایی معنادار داشت
🔹
حضور معاون علمی رئیس‌جمهور در نخستین روز مهرماه در مدرسه «شجره طیبه» میناب، مورد توجه فعالین رسانه‌ای در شبکه های اجتماعی قرار گرفت.
🔹
حضور نماینده دولت در مدرسه میناب از نگاه فعالین رسانه ای در میانه جنگ معنادار توصیف شده است؛ حضوری که گویا حاوی این پیام است که در برابر حمله به یک نقطه، باید همان نقطه را به عرصه‌ای برای پیشرفت و آینده‌سازی تبدیل کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/692235" target="_blank">📅 13:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692234">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
یک گروه هکری با نفوذ به سامانه‌های اداره تحقیقات فدرال آمریکا (FBI)، اطلاعات شخصی هزاران مأمور این نهاد را به دست آورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/692234" target="_blank">📅 12:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692232">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a72e35c17.mp4?token=Qzpu2fadm6Ic5LbUbH8tEgD5uFbe7YiO0we_0NtxTRavTAJCU73-qvoDJAAlb7uw_Hn-gzuPqTUXqRXFl1qx_pD7w4CUeRuRlieA6gbAizbvk8kL9tdiujxD2GjAAO9q4VYyzLKeM5aR8HV0ybLaxoV6LJREQIZ2hwJS8lq_siVKvcR2QImQmbT3sJ5FdlqynxcuSwRg3OQ80WE9FojZY2fmrBBwJ6G_qNM-47qHyiLmDeqWiPdGREB0rPcVwVQyaRCCyUqOsKd3aF8GKPkpQi-VcZh6gLvbq1Ol-8NyFO7YAgXJ-pX8oSNQRL_ygZKnMtIadRQEtJDQ--3_N2LK1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a72e35c17.mp4?token=Qzpu2fadm6Ic5LbUbH8tEgD5uFbe7YiO0we_0NtxTRavTAJCU73-qvoDJAAlb7uw_Hn-gzuPqTUXqRXFl1qx_pD7w4CUeRuRlieA6gbAizbvk8kL9tdiujxD2GjAAO9q4VYyzLKeM5aR8HV0ybLaxoV6LJREQIZ2hwJS8lq_siVKvcR2QImQmbT3sJ5FdlqynxcuSwRg3OQ80WE9FojZY2fmrBBwJ6G_qNM-47qHyiLmDeqWiPdGREB0rPcVwVQyaRCCyUqOsKd3aF8GKPkpQi-VcZh6gLvbq1Ol-8NyFO7YAgXJ-pX8oSNQRL_ygZKnMtIadRQEtJDQ--3_N2LK1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تصاویر به وضوح چرخش زمین را به شکلی نشان می‌دهند که در واقعیت اتفاق می‌افتد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/692232" target="_blank">📅 12:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692231">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: دیدار پزشکیان و ترامپ در نیویورک انجام نمی‌شود
🔹
شأن مسعود پزشکیان بالاتر از آن است که بخواهد با دونالد ترامپ روبه‌رو شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/692231" target="_blank">📅 12:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692230">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/692230" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692229">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
از ساعت ۲۴ امشب پروازهای تهران به بغداد و مسقط لغو شد  سخنگوی سازمان هواپیمایی کشوری:
🔹
از ساعت ۲۴ امشب به وقت محلی، فرودگاه بغداد پذیرش پروازهای ایرانی را انجام نمی‌دهد و به همین دلیل در حال هماهنگی و رایزنی هستیم تا پروازهایی که مقصد آنها بغداد است، به…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/692229" target="_blank">📅 12:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692228">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سخنگوی شورای نگهبان: زمان جدیدی برای برگزاری انتخابات شوراها اعلام نشده است
🔹
همان مصوبه شورای عالی امنیت ملی مبنی بر اینکه دو ماه پس از اتمام جنگ انتخابات شوراهای اسلامی شهر و روستا برگزار می‌شود، همچنان پابرجاست و هنوز چیز جدیدی از سوی این شورا اعلام نشده…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/692228" target="_blank">📅 12:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692227">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/471fd79e94.mp4?token=ALlqX4xYKDbBo-SrDtDQdvCHMR22NKB2YxJ8_rXVTwpdwPpmfYEEa3HhLjGXIN4CgW3ztY5kOnIPXNq1BKagkvj5KQxFbRgahGCBpL21AWMX6Jnhjr4FT2HGwBk0wam4C_mpvpVQUpEFhgXLdtlaWDtjNx0AbsGkbPGeXWK9iJaHMTnZGafVUF5oEfWg5cHoTxiz7aUZy-NHgO413QKZeUfuLgFB5gtZeGEU-sXWrSJdRy8d60NM-cx_l9gjIZvZRtHcCU4AaMGix_j4AtocxYAEsWZar9Q1v4iE-MA6lVh1p68FRu2Xrv3-i0k1VPNGvIF3JBmKHqieob-rMhzGOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/471fd79e94.mp4?token=ALlqX4xYKDbBo-SrDtDQdvCHMR22NKB2YxJ8_rXVTwpdwPpmfYEEa3HhLjGXIN4CgW3ztY5kOnIPXNq1BKagkvj5KQxFbRgahGCBpL21AWMX6Jnhjr4FT2HGwBk0wam4C_mpvpVQUpEFhgXLdtlaWDtjNx0AbsGkbPGeXWK9iJaHMTnZGafVUF5oEfWg5cHoTxiz7aUZy-NHgO413QKZeUfuLgFB5gtZeGEU-sXWrSJdRy8d60NM-cx_l9gjIZvZRtHcCU4AaMGix_j4AtocxYAEsWZar9Q1v4iE-MA6lVh1p68FRu2Xrv3-i0k1VPNGvIF3JBmKHqieob-rMhzGOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش‌سوزی بزرگی در یک ساختمان چندطبقه در چین
🔹
تاکنون گزارشی از تلفات یا مجروحان منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/692227" target="_blank">📅 12:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692226">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سازمان سنجش: معدل پایهٔ یازدهم در کنکور ۱۴۰۶ تاثیر قطعی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/692226" target="_blank">📅 12:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692225">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: یک هواپیمای مسافربری ایرانی با وجود تهدیدهای واشنگتن به اعمال تحریم، در چین فرود آمد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/692225" target="_blank">📅 12:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692223">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc6376e96.mp4?token=oY7KVypPWo8Y0Khx-kKe69fUw6aInfGzutiQvnNjLOeSQoJ3fAa8ooXcF2BXF5POS4adO5YigDeY8B6fdOa7jIBCzBJAzZ0sxmvkzQnDqG8wn1qa1ZJjVV4mkm4I8ft3pLrEIAMHvESeRzk-MAnBbiZ3WTRlakVtBfZ5NMaV1njwN7IJqFH-ZJMURJw5f7j-3rXKz6rexQmpO_0X7ITPIt6cJuUvxIqdIMbCZLDZEOQQXbYNYEMQRQ-o9uvlQEQLzbA85mgSVdPvbnp_IfsFBF9AhwknKjS9TkL4_40QsQOyoz0n8oAG2_As4uHwJkhbaWKzsYGQXCyF1kMBCApfAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc6376e96.mp4?token=oY7KVypPWo8Y0Khx-kKe69fUw6aInfGzutiQvnNjLOeSQoJ3fAa8ooXcF2BXF5POS4adO5YigDeY8B6fdOa7jIBCzBJAzZ0sxmvkzQnDqG8wn1qa1ZJjVV4mkm4I8ft3pLrEIAMHvESeRzk-MAnBbiZ3WTRlakVtBfZ5NMaV1njwN7IJqFH-ZJMURJw5f7j-3rXKz6rexQmpO_0X7ITPIt6cJuUvxIqdIMbCZLDZEOQQXbYNYEMQRQ-o9uvlQEQLzbA85mgSVdPvbnp_IfsFBF9AhwknKjS9TkL4_40QsQOyoz0n8oAG2_As4uHwJkhbaWKzsYGQXCyF1kMBCApfAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ‌به هر‌ دلیلی دچار استرس و فشار روانی شدید ، با این روش کف دستتون رو ماساژ بدید و از تاثیرش متعجب بشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/692223" target="_blank">📅 12:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692222">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5vzEJy7lfS0JLQEwKQCzUuVddqloab616gBIhAkJgDsG591_nKkKF3wGIOVKGmHRQBtYuOM4jj7Jy21kGnezZwDhRQtQguNFseouLa9fFZFgx2i6i57xH0s9LFiNq8rLZ5r08cQF85bjz83onHoGHPQZPUNRfi--htLiOQWLu5uik2p53iy88mKnykn8BPu6uXlpnU2DgrTsV3KWStJSmy9PZ8O_qBoogMRm-kHxb-BUW4UhlbusZENXQdJH_KrQ_FtE-1j9QPzVkOItWzimZfnei0kzVxMjO-KudhtpZw1pxZMx2r3kreWoUiKy3AWuzrXDV93p8eX61wLTpwI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا بیشترین دارایی سرقت شده از منازل! / چگونه جلوی سرقت طلا را بگیریم؟
🔹
طلا و ارز نخستین هدف سارقان خانگی هستند، اما باورهایی مثل پیچیدن طلا در فویل آلومینیوم یا قرار دادن باتری کنار آن، چیزی جز شایعات بی‌اساس مجازی نیست.
🔹
سارقان امروز روش‌های متفاوتی دارند، در این مطلب، تنها راهکار مطمئن کارشناسان برای جلوگیری از سرقت طلا را بررسی کرده‌ایم.
👇
👇
👇
متن کامل را ینجا بخوانید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/692222" target="_blank">📅 12:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692221">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2NFtNbFrMfHUMve2OVu65S6qhaUDRUMGZXZYa1k8UkqMzhLGfHe1GeUnbLyfyBm0Zd-LqDz69Jit2CfdZ5ucgLYNuYkTqb2z-FP49U_3gy4nBmllcArvlOKK86TTxU3h0MrG7_eLlm5OmmamxjX7gr8k-zxG1LTMo2kR4Lk79rTyYFQJ9EpWX8woqipDwzh_GvZQfmjh76QjNvbJgVNa_bBsi-iRniYG-L0iwvk4L0vU0Fn8SRjHUqbJuOtnQ6xIsWWhp8RUFQX9H9oV5WoCtvEtjQ5NwMtPKc_1bqVIjw5OH97MyUih52KhX5p3hR3HcNAotk3gTWrWRNwTBl7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | جشن فرشتگان
🔹
همراهان گرامی خبرفوری، شما می‌توانید با ضبط یک ویدیوی کوتاه از دانش‌آموزان خود با لباس فرم مدرسه، در این پویش شرکت کنید .
🔸
از کودکان خود بخواهید این جمله را بیان کنند: «کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
🔸
ویدئو های خود را به آیدی زیر ارسال کنید
👇
#جشن_فرشتگان
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/692221" target="_blank">📅 12:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692220">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5ecb9853.mp4?token=v9-cXAYr3qmvCZMhfRIsz3S6zEDWqTwz0Ry9D6bIp04WHgQfVl4VLi73GW4wyD1aeqITLb2js27Gq3sPE-Pr8ZKrSjzeLj8GrgsnmutahE4WuUuIZHBfUqT3iXxMMdgAzvN6VHCL5NMkEJ1RQ9LSQbGUrRTMYSu7w4fM8NiG-E3sS89Y23dL6uAebd_aLXPJQxn2nn8kKDrIrfsec4kNyTSjO6fA46qZdR3L97L4R_2WOrzlHF7u3UTrigHvZbJOArwKBxSZenXUoV7G6lsh5VGuN_tKbvQLNwnT9oEz_AlHSXMmBijPC220T7j1rJ4kHer_zLyAcsNwBxxHrFW6aEfqrM5AU1ysTVZAtAsIQ2_Q5bwABjxiCOwbLMxa9PdD8AfWyR2-SwqXx7F_8hRXPVaHARey94jYJYut6wfqs0ZlhBywaU0zMRIVwR4WepuhiQEcMa8scX35RdlCuzdGnLuhPUTMcApXrBbjySmZWRXOKxAc8Jw0iNB_Xzmz1z02oLL3pQ-3_c-KOsAX79LbKuReDRyb8S2WZFjx0BRUbZ5a42LrL7JwrICisuz4pErqdcRMW4eHCr6jq0SQiPNfGQbDdiSUXgxJ7dC2W8K76LZAj2nRnoCUyLPb8G87E5RbaUPqJgaDAz-Mx0Svt-qP6AFWxBAQUy3NhFfBTmJquas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5ecb9853.mp4?token=v9-cXAYr3qmvCZMhfRIsz3S6zEDWqTwz0Ry9D6bIp04WHgQfVl4VLi73GW4wyD1aeqITLb2js27Gq3sPE-Pr8ZKrSjzeLj8GrgsnmutahE4WuUuIZHBfUqT3iXxMMdgAzvN6VHCL5NMkEJ1RQ9LSQbGUrRTMYSu7w4fM8NiG-E3sS89Y23dL6uAebd_aLXPJQxn2nn8kKDrIrfsec4kNyTSjO6fA46qZdR3L97L4R_2WOrzlHF7u3UTrigHvZbJOArwKBxSZenXUoV7G6lsh5VGuN_tKbvQLNwnT9oEz_AlHSXMmBijPC220T7j1rJ4kHer_zLyAcsNwBxxHrFW6aEfqrM5AU1ysTVZAtAsIQ2_Q5bwABjxiCOwbLMxa9PdD8AfWyR2-SwqXx7F_8hRXPVaHARey94jYJYut6wfqs0ZlhBywaU0zMRIVwR4WepuhiQEcMa8scX35RdlCuzdGnLuhPUTMcApXrBbjySmZWRXOKxAc8Jw0iNB_Xzmz1z02oLL3pQ-3_c-KOsAX79LbKuReDRyb8S2WZFjx0BRUbZ5a42LrL7JwrICisuz4pErqdcRMW4eHCr6jq0SQiPNfGQbDdiSUXgxJ7dC2W8K76LZAj2nRnoCUyLPb8G87E5RbaUPqJgaDAz-Mx0Svt-qP6AFWxBAQUy3NhFfBTmJquas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر نگران آلزایمری، این تمرینات روزانه رو از دست نده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/692220" target="_blank">📅 12:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692219">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
رسانه‌های عبری: شاباک فرود هواپیماهای اسرائیلی در امارات را به دلایل امنیتی ممنوع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/692219" target="_blank">📅 12:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692218">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تصویری از ورود پزشکیان به فرودگاه نیویورک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/692218" target="_blank">📅 11:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692217">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ویدیویی از دورهمی تعدادی از پرسنل هلدینگ تبلیغاتی و رسانه‌ای خبرفوری در مراسم جشن تولد ۱۱ سالگی این شبکه‌ رسانه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/692217" target="_blank">📅 11:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692216">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfxaWnbdJBrPXJy35GWlGD_wPOlp_rK4V_67EDc-xYSxa-AmWabMsdLR9NMaYbtFO7kY2xonlbIWQb1PmpQblvkUJ-a15kOWiCWMZoyGI0TIZLqPq6LpTWEwQtepiygzs_1H54qZhr2-PSg6KbYijBR9IePFc4VZNQzvEV3hl6umb_LPlSvMcjcHGY32aJ_L1BRwEJHAlCfHwMzCj6BY9XfgXUSP-kWrF3WSPmEoS8SsTB0eTco-aLdatmlbtDbrLrpIS-0-6XEbJycDwKsTw1S82NYr5awOQKI8VWdD_LuTrWVygYLtZ_lQPGGBTqXsuoOk_61_hR5S5wMNCCGsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرفوری ۱۱ ساله شد/از یک رسانه خبری تا شبکه‌ای با بیش از ۸۰۰ رسانه در شبکه‌های اجتماعی داخلی و خارجی/تلویزیون اینترنتی «مدار»و آکادمی «آوید» دو محصول جدید خبرفوری
🔹
امروز سالروز تولد خبرفوری است، از یک مهر ۱۳۹۴ تا امروز...
🔹
خبرفوری در یازدهمین سال فعالیت خود مسیر توسعه‌اش را با گسترش شبکه رسانه‌ای، افزایش مخاطبان و ورود جدی‌تر به حوزه‌های نوین رسانه ادامه داد. مسیری که امروز به شبکه‌ای متشکل از بیش از ۸۰۰ رسانه، ۳۲۸ برند، ۶۰۰ نیروی مستقیم و بیش از ۹۵ میلیون مخاطب رسیده است.
🔹
در این سال، توسعه تحریریه‌های تخصصی و خبرنگاران محلی، فعالیت خبری به ۹ زبان دنیا، راه‌اندازی تلویزیون اینترنتی «مدار» با ۱۵ عنوان برنامه اختصاصی و ۱۲ ساعت پخش روزانه، توسعه تولیدات تصویری و مستند و گسترش فعالیت‌های فرهنگی و آموزشی در دستور کار قرار گرفت.
🔹
راه‌اندازی و توسعه آکادمی «آوید»، پیگیری راه‌اندازی دانشگاه خبرفوری، ورود به کسب‌وکارهای جدید و شکل‌گیری «اکوسیستم فرازان» از دیگر گام‌های این مسیر بود.
🔹
همزمان، هوش مصنوعی نیز به بخشی از فرایندهای تولید و انتشار محتوا وارد شد و حدود ۲۰ درصد این فرایندها مکانیزه شدند.
🔹
این گزارش، روایت یک سال از مسیر خبرفوری برای ساختن رسانه‌ای گسترده‌تر، فناورانه‌تر و چندرسانه‌ای است.
گزارش کامل کارنامه ۱۱ سالگی خبرفوری را در سایت بخوانید
👇🏻
khabarfoori.com/fa/tiny/news-3247219</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/692216" target="_blank">📅 11:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692215">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: دیدار پزشکیان و ترامپ در نیویورک انجام نمی‌شود
🔹
شأن مسعود پزشکیان بالاتر از آن است که بخواهد با دونالد ترامپ روبه‌رو شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/692215" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692214">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f1e49d1b.mp4?token=iGZjW0T50HZLvDGhkdqb10W8O4NGNkJgkNJMmq055nkgz9iZ2TjFHPumpBN20x7R_bbsSgBxBt5MC39LH14ZEM9jddBSDH7FeiOM0MxfqQWyXqz8--veUYrTGDBAgZTrFdGrt10-9gAA5bZKq1AF7hRdUwffvmFNsSnoBeuNR0f-06UuUKIjTigdAR6_FHaPeb_d0HuVpK6Yls9VwFi9xGGIgvim_c_ew4sBGX4TTgYs0esHCSzn834DZ41Wcvy-1uEcxCR--xYNBDaa7oidKEicZwBbGMJZbARSLh8IiE0IB2n4vbn8E5ziCoEN9Tw1-9qARtarL-QJYhazIr5FJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f1e49d1b.mp4?token=iGZjW0T50HZLvDGhkdqb10W8O4NGNkJgkNJMmq055nkgz9iZ2TjFHPumpBN20x7R_bbsSgBxBt5MC39LH14ZEM9jddBSDH7FeiOM0MxfqQWyXqz8--veUYrTGDBAgZTrFdGrt10-9gAA5bZKq1AF7hRdUwffvmFNsSnoBeuNR0f-06UuUKIjTigdAR6_FHaPeb_d0HuVpK6Yls9VwFi9xGGIgvim_c_ew4sBGX4TTgYs0esHCSzn834DZ41Wcvy-1uEcxCR--xYNBDaa7oidKEicZwBbGMJZbARSLh8IiE0IB2n4vbn8E5ziCoEN9Tw1-9qARtarL-QJYhazIr5FJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوشیدن مستقیم از پارچ؛ لحظه‌ای متفاوت از سخنرانی رئیس‌جمهور موقت هائیتی در سازمان ملل در سال ۲۰۲۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/692214" target="_blank">📅 11:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692213">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e325bfdf.mp4?token=MteLLXKmCBMW16CM2LrFxOaaRMOiZ7BjUGlYjAVjpu3ApytU3iP1a2cAokjYfhmflJGL2djW5AfV5HuwXX2OMLO2fEUbhFkAOHYrmCOXZqAI0pRbr75SlFWupQSufLEgWjToZLbnwDEaAtq0UPvmfrGuLvxwKswYjUgtR12-ZkxXzpr4d0VdKfJo4yjJG8zoS6BzTA13Y9wUu_9EG7eqDfdyZjvthNUtDT5Jm-wQDbMRX7YEdjLbfjS-qMirrovmT3A-8YOFTWg-933rR1gGFVUf4-M1-WvD_szEGQx6gazhakpwHIClyx0s85toFmNeDXy6gsXy6KFqPzXlpBAR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e325bfdf.mp4?token=MteLLXKmCBMW16CM2LrFxOaaRMOiZ7BjUGlYjAVjpu3ApytU3iP1a2cAokjYfhmflJGL2djW5AfV5HuwXX2OMLO2fEUbhFkAOHYrmCOXZqAI0pRbr75SlFWupQSufLEgWjToZLbnwDEaAtq0UPvmfrGuLvxwKswYjUgtR12-ZkxXzpr4d0VdKfJo4yjJG8zoS6BzTA13Y9wUu_9EG7eqDfdyZjvthNUtDT5Jm-wQDbMRX7YEdjLbfjS-qMirrovmT3A-8YOFTWg-933rR1gGFVUf4-M1-WvD_szEGQx6gazhakpwHIClyx0s85toFmNeDXy6gsXy6KFqPzXlpBAR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری از سود میلیاردی واردات لکسوس برای ایرانیان خارج از کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/692213" target="_blank">📅 11:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692212">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243a70d161.mp4?token=UoKUTlMEmqwj_QI-X1XUZULB2krLGksaAdFFDp3WfyAd90cF8W_0mYiUbwBPDi0CjGWQdGdmxKc60_6EGpGn6TjmJDxdmKO76zJkkqw-JC3U9Z8Cnsbg2TfIWtU1Ym5okfIW2oIhEaqA68gcjA00cWXetPpyJzwTg15dBZM8LHoDWPUQ6cIWXNNVcKFo8j6S4ynYecYXV-SYUZ6GpP9J-BRqaZfUtVAQK_zpK1Kx5mKCS7havhMe9KEWBTH8qT-lZWdjE1D_gZlViOKiowZioLCKap0aXKchBlC5XcTE3Y3P6OferwSfPJsN58RzIpESaW1ACVF23bMfrrVjeg4HQmJjWIMC6Rv4sxIweijcZl9Tea5uzItjJuF8aPwaB30GSO500_GnsNbtIN0v_AlHVRzS0riAhND2fMTCtt6AEaBt4eze1hLjIzTfea3YR4gO7n5M5Q2W2y9OO-37qoKokyYbzSJIwtmfPs-kt8iPVX6ORq4zmqUO9KHmgAJ5UJePl5PtYCjHqPz5x8pwZs0WKL1WGyI9QOceRJ_Ug6QnS-_XnWUXrsCgAQD9T8PxPLFEjNss0ek6UsBf4wkQJ6D4xx5zon39e-kH4owRBjeNHokuARi-o1zn3auAHULW6KxSq4cwq4ex9eQajIQ4K6l5rdiso38WGOvJt4fXEA3Fzew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243a70d161.mp4?token=UoKUTlMEmqwj_QI-X1XUZULB2krLGksaAdFFDp3WfyAd90cF8W_0mYiUbwBPDi0CjGWQdGdmxKc60_6EGpGn6TjmJDxdmKO76zJkkqw-JC3U9Z8Cnsbg2TfIWtU1Ym5okfIW2oIhEaqA68gcjA00cWXetPpyJzwTg15dBZM8LHoDWPUQ6cIWXNNVcKFo8j6S4ynYecYXV-SYUZ6GpP9J-BRqaZfUtVAQK_zpK1Kx5mKCS7havhMe9KEWBTH8qT-lZWdjE1D_gZlViOKiowZioLCKap0aXKchBlC5XcTE3Y3P6OferwSfPJsN58RzIpESaW1ACVF23bMfrrVjeg4HQmJjWIMC6Rv4sxIweijcZl9Tea5uzItjJuF8aPwaB30GSO500_GnsNbtIN0v_AlHVRzS0riAhND2fMTCtt6AEaBt4eze1hLjIzTfea3YR4gO7n5M5Q2W2y9OO-37qoKokyYbzSJIwtmfPs-kt8iPVX6ORq4zmqUO9KHmgAJ5UJePl5PtYCjHqPz5x8pwZs0WKL1WGyI9QOceRJ_Ug6QnS-_XnWUXrsCgAQD9T8PxPLFEjNss0ek6UsBf4wkQJ6D4xx5zon39e-kH4owRBjeNHokuARi-o1zn3auAHULW6KxSq4cwq4ex9eQajIQ4K6l5rdiso38WGOvJt4fXEA3Fzew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تانک آلمانی «پنتر» متعلق به جنگ جهانی دوم
که پس از ۶۰ سال ماندن در زیر خاک، در شهر کازان روسیه از دل زمین بیرون کشیده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/692212" target="_blank">📅 11:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692211">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ba1b5004.mp4?token=twO1At67S-l60YQpnUi9BbK2MUPfFelAjgOW60pikRImIAuYecfGHwBF12pcloJsvH_gP3Ek_ZMi5zCmDFo8Nh2D04EN7Z8824BsavtxZ1nrwq8mML3kw2MEXaDivILYO43kZocrZM5oc0jaU7nIg56aCL2eFUSN-2wcC9nn8D_tRjg5u750NvVuY7WxKLmKyWz6E5y7Fbv4MMXHZgkbbjO0yR-Qw2WmSu9YhNqzwxFyWUvIvbkVKfTTWpqfznIKuD19KtpS58IfOEhas04ggWo0a0nFwTkSEC1u6lRjEIdZt8HKTUSby9kDedwJllXauKNY6H3Nn1qEGsgOdeILhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ba1b5004.mp4?token=twO1At67S-l60YQpnUi9BbK2MUPfFelAjgOW60pikRImIAuYecfGHwBF12pcloJsvH_gP3Ek_ZMi5zCmDFo8Nh2D04EN7Z8824BsavtxZ1nrwq8mML3kw2MEXaDivILYO43kZocrZM5oc0jaU7nIg56aCL2eFUSN-2wcC9nn8D_tRjg5u750NvVuY7WxKLmKyWz6E5y7Fbv4MMXHZgkbbjO0yR-Qw2WmSu9YhNqzwxFyWUvIvbkVKfTTWpqfznIKuD19KtpS58IfOEhas04ggWo0a0nFwTkSEC1u6lRjEIdZt8HKTUSby9kDedwJllXauKNY6H3Nn1qEGsgOdeILhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ عدد دلخواهش علیه ایران را در سازمان ملل تکرار کرد
🔹
ترامپ در سخنرانی خود در سازمان ملل بار دیگر ادعا کرد که ایران ۵۱ سال است که شرارت می‌کند، نه ۴۷ سال.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/692211" target="_blank">📅 11:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692210">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14ab032e8.mp4?token=DeYQHqQWW0l9Eywk4ZLlxGnzpFXcuOTjpKiuF-abG0yuvvSdZqJIThZq4RnwgyH4oEHkf-AjIypO3SDBOMeQg-p_1Nyl_6yPHx3zimhmBhGH_eZvEJW5IeuB5B1ehfRr8RKd6ZVslFwVU_KE8t92hOVr8Q-PqR9YOyauXUapkoDzcRJPrpoAEDM3fxXgeDzjnntpWpKoigR698GDy4j8g0A3XgFUtvdvorZkQpDMaBOMJV1l7Qb99BJCn7KfgIfGtNjErDvtjr6GuaRCdKq5foeUfCJDTBVNX_X3SrQuC03NxFJ5DeRPCAb0Bs7WmEoJlZeJwAwQ2Orqvh84gQDQ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14ab032e8.mp4?token=DeYQHqQWW0l9Eywk4ZLlxGnzpFXcuOTjpKiuF-abG0yuvvSdZqJIThZq4RnwgyH4oEHkf-AjIypO3SDBOMeQg-p_1Nyl_6yPHx3zimhmBhGH_eZvEJW5IeuB5B1ehfRr8RKd6ZVslFwVU_KE8t92hOVr8Q-PqR9YOyauXUapkoDzcRJPrpoAEDM3fxXgeDzjnntpWpKoigR698GDy4j8g0A3XgFUtvdvorZkQpDMaBOMJV1l7Qb99BJCn7KfgIfGtNjErDvtjr6GuaRCdKq5foeUfCJDTBVNX_X3SrQuC03NxFJ5DeRPCAb0Bs7WmEoJlZeJwAwQ2Orqvh84gQDQ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک تمرین ساده که اهمیت کلاه ایمنی در کارگاه را نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/692210" target="_blank">📅 11:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692209">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نجات یک مرغابی گرفتار در خیابان‌های نوشهر
🔹
یک مرغابی که در خیابان همافران نوشهر توان پرواز و راه رفتن نداشت، با کمک یک شهروند به دامپزشکی منتقل شد و سپس برای بازگشت به زیستگاه طبیعی‌اش به ساحل رفت.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/692209" target="_blank">📅 11:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692208">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: رهبری جدید می‌توانند درباره سلاح هسته‌ای فتوای جدید بدهند
/ ایلنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/692208" target="_blank">📅 11:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692207">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2fyakxrgaNrEiHVrwVx946W5_3Zwhe9Iuuc-_YBkj1paTQhoj9rxXNoWp9Qo1PakXb2nh-sclJm8JMzL-0Kz_KF2YI-VVEASDCpDeEA9c7-9yrJzV-edZlAOk1wNlZzC4mnSGenO2rVdY-lgkjIWe35UtpBEuUnsa52FGcys15Mep48GYxP2mae-Bw-AoDAbbpdtawtyWuOcwl-H0_Oxx335o5NQB7uhHR0eO5vrq1vcUJu9IvDUz8-6m9ot4aD9_PQ-m-6vDjW5pUsTwj0c3S_wUgXLW5mRX3EHUYpdHUycy9tIg-L12PTEh3rTg6HkjTIil8M2Rs5FZN4Ws4ToQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ آغاز سال تحصیلی در مدرسه شهدای میناب نواخته شد
🔹
زنگ آغاز سال تحصیلی جدید با حضور معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور و جمعی از مدیران و مسئولان استان هرمزگان، در محل مدرسه شهدای میناب نواخته شد.
🔹
این آیین با گرامیداشت یاد و خاطره شهدای دانش‌آموز و با حضور جمعی از دانش‌آموزان، فرهنگیان و مسئولان استان برگزار شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/692207" target="_blank">📅 11:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692206">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN6K2CVNHAwNetBsb3jRP2CToYb6Ctjumw5SSIw6b2KPPl2MibG2qoZJEZH6xMMu-C2FzbgShvQPkeJhsiTQkC1NJZSCJFmE8yAQnuTNNSXrpgcKhcWMWtt01relNha4_hWTFDQyAoBvhsD-tl3VHnpOsouqJyAzROew5HbLX44S_8gGuHF28egR2hNHZ-dSGODbTy07EQosB4iUmh4DYKFE2Wns4ioeRqYstwFF9PXQyoOkbcQ4nxw9AVhiQEnFznOOdgKTMqPXGG8BFPQkksVnUyhDCVi6G8VemZKCNsbry7mwMVPsyu3AZOeLYcCzyyMjkpNrvtGAkcNrr33h7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییر ساعت کاری ادارات و بانک‌ها از امروز تا آخر سال
🔹
بر اساس ابلاغ رئیس سازمان اداری و استخدامی کشور، از امروز تا پایان سال جاری با هدف بهینه‌سازی مصرف انرژی در دستگاه‌های اجرایی، ساعت کاری ادارات دولتی و بانک‌ها از ۸ تا ۱۳ خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692206" target="_blank">📅 11:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FYUtaolWGqn5zA7rbNLNlf9qQnnVqx_YMaa5DU8WU4whay3Muz2HX3Liw0FmEd5BbR6zOuSYGCksslJw0vY0F1o7JrJuloQNrPGj-CIzk9PtLA0Ugw76SFdRb8Re1hRR42Ne50xa1ELLRDxYwwjdD2njVYygISUoqOyzzgT-foh8gD51VBvQ9rQGulrBbZr84JmD_DzCgIINXAzAvBopIfPbtBP5X8UGdAhdKAuagPePCjc__RdLOxNYVPuPIFFaETkpLiAQKz95eF_uMUBz5eH8TYIaUA_iysSsyLXaQ3dJhec4xVpy3zNdWX9jegxV1ko4G21sEU8ufqfieUfwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCTTEohwu5YUSSQXevo7Kqdh8MLYsOYHpdnbev3V05Qf9BnYIcziHdDI4S4y3Xm7ZUR0VFgDUzIVrWq0f0gS_QsDWOnHtn2cHgQ7o6veeRoewTu7blxniM8pU9GWAXyqNfNqT1A4237gKpwKfs7ThJxOrrJVvmD4WMgOXROjN8srSJ2imv1-jUNxLrMulQnkAc1tUtP35znVzDC4b3zowqyQLHMNK1WawkquCt7KCmzdIQsX29fRx8cIXJaxve4hrNN_dK77Z_nIlGhzitq83n4LK3wmT-KoE_cJL3Hx56KOLKjNGS6ALxVNSseC1urqUFNL4hAwzh3KEovL46jeFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دور ریختن غذا توسط دانشجوهای علوم پزشکی کرمانشاه در واکنش به کیفیت غذاها و پیدا شدن سوسک و کرم داخل غذا
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/692204" target="_blank">📅 11:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owBrxluXYgvIz4DS2XfhiGhor9yOdrAa5TBO70KYkZyhHBQ0c1Ab-1vniU-0LN2VFCbmGN97Tk4qWxuPV2J_l33DBAxl6vQaPcqrjnpW-EvKHz8J1MYGvxtZAVqOu4-q4ZVPdUUiIa99P6jbHKQ5FoiF44QXDvTb_VAtV_s5ardWQwH19lUT4T0zHSxcV_6xlL1GTMHkTyP6-lpnMxz7P0C5xGZL2lmgIUDwZ7Im00A2CaZtePrknOYH2F708uVXDhyxbe1O6KYOh9db8iewYti6iBAcjr4Oko2Loj66adkYKjMjvo6V8HZ1MeZXUZ2c5Tf4RDG19alez4NeEj3JFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از گرمای شدید در هفته اول مهر ماه، اواخر هفته دوم سرمای شدید داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692203" target="_blank">📅 10:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR2BViwYQ3mYeR4Qll7senUTzwCAQ2KbJB1XKt-k-ONDMl491ViEfXeN3755vaZzoJDtH8C6nsv6T2_J7gK2HBWlPOeWoMFDtaKIzYXIzPxju94ZwaBzFvJdOtpULNxlAStBpbwsyurXlyRwIUnUutk-HkdQyWBmZQBCVEVG9gq20U0dGW-ELqbJgTtq1jzAF8g_EIFYG7UXTezo3nBOvRX-48VS-cUElwXfzB-fHzMeVdJskPt4pHFDx-L2JfyT_sgF2PdUvpJLmD58b5g7evX996P5WnbC1CzQgeq9kYeIyE3-Ggk7ow5yKAqQUdjARho-shX7G_L8aEghH8NnIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آثار بمباران آمریکایی بر دست دانش‌آموز میناب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/692202" target="_blank">📅 10:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHwMeZPOjJUKup0LOSDZJDMQKaQMoxCLUOzDXS_yFO0CWknXNFrBe6Ck-sBAEyyapmZ6I6gJgwpzFEDKc7QKUjedvCs7YajRt9NZN7lvlkbxITUo7IRHHrYG-CsemvPE5mpTPmQh9iF245n0PjJUfmZnY5xOcQKeZnOVHwserldDlHxyw_mA6_UoL_Ho5zdl_cbKdZNtd0GCn3sRUisCAdKXiOmUFgRSUstWmPZRZYDKm-Gyl0mZPbYDGqz1J96xcyFyx1GmGPZhmhMYyqHzhqARpPH-rWxfHOFFRVVrUng5bgv6OE5dMWwjLY5WUiHsw6M2jFivZbvEuX7ryRp6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💼
Work Mate | دفتر کار همراه شما
همه‌چیز مرتب، یک‌جا و همیشه آماده.
مناسب کار، جلسه، سفر و استفاده روزمره.
✨
💰
قیمت: ۶,۴۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/692201" target="_blank">📅 10:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d911f81c55.mp4?token=ZsA5RUU3bdp8BE1SaF51STJMJHmEtxMPJ8Y8LmjR_82LBeWz9a8AnQfZ1TNtoEzi-J-Q3VzlbuWspbRoG4qJVI7d_FS_Z1wbrzcrGDzqX26vJ6ZSnqy6F2PXqm_nBsPPhIc6HMdycqyxfK7ILcT3uzbfNJoD5G9gcSwq8WVmfO0OpqkHvZwCM2TgEj1HFBCO23lvhR4DooeF-HsLGhCssyu1ypImmbW9PozeaaQ97Q40i-9E6N-yL0ETQKo0MSYCWgl-FBuqeqntXprGl91FTXR3UHA1ISh9QLCdfBlYwZL41vw9mDPf-lIzaa0DQt2z-T9CP5sTTUJEin2Oo4DNiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d911f81c55.mp4?token=ZsA5RUU3bdp8BE1SaF51STJMJHmEtxMPJ8Y8LmjR_82LBeWz9a8AnQfZ1TNtoEzi-J-Q3VzlbuWspbRoG4qJVI7d_FS_Z1wbrzcrGDzqX26vJ6ZSnqy6F2PXqm_nBsPPhIc6HMdycqyxfK7ILcT3uzbfNJoD5G9gcSwq8WVmfO0OpqkHvZwCM2TgEj1HFBCO23lvhR4DooeF-HsLGhCssyu1ypImmbW9PozeaaQ97Q40i-9E6N-yL0ETQKo0MSYCWgl-FBuqeqntXprGl91FTXR3UHA1ISh9QLCdfBlYwZL41vw9mDPf-lIzaa0DQt2z-T9CP5sTTUJEin2Oo4DNiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پودر گوجه؛ جایگزین متفاوت رب
پودری خوش‌عطر برای طعم‌دار کردن غذاها
🍅
🥫
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/692200" target="_blank">📅 10:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
بهزیستی: واریز تشویقی ماهانه ۲ میلیون تومانی به حساب بازماندگان از تحصیلی که به مدارس بازگردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/692199" target="_blank">📅 10:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ورود هوش مصنوعی به قلب صنعت بانک کشور
اقدامی تازه از تجارت الکترونیک پارسیان
🔹
دومین رویداد بزرگ کاربردهای هوش مصنوعی در صنایع و کسب‌وکارها (IRAN AI 2026) با حضور جمعی از مدیران عامل و ارشد سازمان‌ها، مدیران فناوری اطلاعات و ... برگزار شد.
🔹
شرکت تجارت الکترونیک پارسیان (تاپ) به عنوان یکی از شرکت‌های حاضر در این رویداد از کاربردهای هوش مصنوعی در صنعت پرداخت خبر داد.
🔹
این شرکت با تحلیل رفتار مشتریان، امکان شناسایی مشتریان در معرض ریزش و سنجش پتانسیل تراکنشی آن‌ها از طریق تکنولوژی هوش مصنوعی را فراهم کرده است.
🔹
به گفته مسئولان این شرکت، هوش مصنوعی در تاپ به حوزه کشف تقلب و شناسایی رفتارهای مشکوک هم رسیده است.
🔹
این ویدئو روایتی است از خلق ارزش تاپ در حوزه پرداخت برای مشتریان.
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/692198" target="_blank">📅 10:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3vYFsl7jfikzBxEYCvhzX1i-xNu6Lf8lr_L4CKls1f-s3TFSaXfB-8XDZPUxrBfU188uN3NKPZ4ChoQLPdh79Z-AcUBTs6pkj1JyguPYEjXktCRSvz6CIM80Fz2_mhLOMwVwXSMUhwqxg70CIZP4ITbc8RJ7LcgHghGyI1t-v7tZex9SuvCLc2sCDHQLFpfbLx9N5Bd262uESiuppSHMlEvuJozDlg6GRYbiIYi4fF6QbmROVqJmrfAWM3VTbnoHlP9R58iMk9ejCwiNgPvG4ir-gIeiN_QiPyD9Vbh9RBb5x9moHEBxHnua3FGs5hbS6g5fD3pS60rSJqgAQJi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور از دل بحران تا پایداری؛ به زودی هشت پل آسیب‌دیده هرمزگان زیر بار ترافیک می‌رود
🔹
مدیرکل راهداری و حمل‌ونقل جاده‌ای هرمزگان از اتمام عملیات بازسازی و آماده‌سازی هشت دستگاه از مجموع ۹ پل آسیب‌دیده از حملات دشمن آمریکایی در این استان خبر داد.
🔹
عباس شرفی گفت: عملیات ترمیم و بازسازی این پل‌ها از پنجم مردادماه سال جاری آغاز شد و با تلاش شبانه‌روزی راهداران و عوامل اجرایی، بخش عمده آن‌ها در مدت کمتر از ۵۰ روز آماده بهره‌برداری شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/692197" target="_blank">📅 10:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
هیئت دولت امروز را عزای عمومی اعلام کرد
🔹
در پی رحلت آیت‌الله شبیری زنجانی هیئت دولت امروز را در سراسر کشور عزای عمومی اعلام کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/692196" target="_blank">📅 10:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-ff7c5dKBFXGuKbhQ5oazfCDZZSQUCBdTBAR3he_yEHJmns8m6YnAj1OkC-6SCTiz5WgP7pMF9z3--rO9TdPvwYa-yTrfkWp0pXmcONW3tKJP4xR5aE6BQUcWWOOUQRRzQ-Q1PR_werqfl4umj9n8z1IFispvJ1aw1f4C13zqZFYpzMk7sNW9ktDUsUIp-d0WwlUjlRKROAzaMYYiVyaP3gOOFK5w1yQSUzYO6ZbXVgiV2NCd167lTD7P4n8RRlHNOqRia5UwLy_Pl0NHdlEhAMEMKCTx9SKybzb1v2HQJT4PO9nIeLY6cgzVAnU_ez2VDzxRRJ5BSilIxZgmkIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون، کارشناس آمریکایی حوزه ژئوپلیتیک: ترامپ در این مقطع، واقعا مایه آبروریزی جهانی برای ایالات متحده است
🔹
کسی که در مجمع عمومی سازمان ملل ۳۰ دقیقه وقت گرفت تا نفرت‌پراکنی، حرف‌های بی‌اساس و تبلیغات سیاسی خودش را مطرح کند. این مرد دارد به‌ تنهایی و با سرعتی بی‌سابقه، اعتبار و جایگاه آمریکا در جهان را از بین می‌برد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/692195" target="_blank">📅 10:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692194">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yndv-q3xUHTTW5bznAEj9n3WdNw0G8-OOGbSpfcYaHpzQiKTKn9L4d50gzdtR5S9YJeXUIX9U3WdN2zFKGuS_rtytUFlnEta5Pcm0gRNyTAw7Z668-prE3xTTGL7N3lxLrUSrqygyZeUDwPJ2nohO_y_Sc5RZiSBbASKuX-EeMUpoUmOuxNn6vtqWAZmfgkgq8nZBsshszIKlwrHpFzcVy5YptZuvMH9qC7n47e-rTwR9o3KWx3N5yCfYgLlixSy8twdY6N3RyGNjvMPIfuqWXTwn6PbZYqYQu3phiGG3X21ivHZeUh9YrLQBV-4HGms0TvkB1SRLyXj6yBUQIYAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت نامناسب تالاب چغاخور، بزرگترین پهنه آبی استان چهارمحال‌وبختیاری
#اخبار_چهارمحال_و_بختیاری
در فضای مجازی
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/692194" target="_blank">📅 10:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692193">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7239225b10.mp4?token=MLiMSku96IlY1yrXl4V026NkW_R63LwrRxxXoZJyynGdmS52NDB6QbBb7Hlr6IoRyp1o3KkrAw2EvaiZ9Hyf7arbgfp33vpoZMHHJZuQ0xXUM75Jcxxgf8cOURn1Yv6iHRpu879yDIqdfRj31NL5CL_JfcGhYdUVDlXOgEBJpo-Lv_gpMgcAB13l5tobGzBDIGdWAj786OHq9K8aMxdzUjmTleuRx32edqDtCJ7YQjH8J7euOxeDiTHVvTH2GD1GGTVUV13NSKqq3FuY5xd1wZvdhAFxH8aSNsOSZgwKJKEW_3R5oRgoSeB-ld9WdiqR2W_-YdaXxD42TpEKzxY2UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7239225b10.mp4?token=MLiMSku96IlY1yrXl4V026NkW_R63LwrRxxXoZJyynGdmS52NDB6QbBb7Hlr6IoRyp1o3KkrAw2EvaiZ9Hyf7arbgfp33vpoZMHHJZuQ0xXUM75Jcxxgf8cOURn1Yv6iHRpu879yDIqdfRj31NL5CL_JfcGhYdUVDlXOgEBJpo-Lv_gpMgcAB13l5tobGzBDIGdWAj786OHq9K8aMxdzUjmTleuRx32edqDtCJ7YQjH8J7euOxeDiTHVvTH2GD1GGTVUV13NSKqq3FuY5xd1wZvdhAFxH8aSNsOSZgwKJKEW_3R5oRgoSeB-ld9WdiqR2W_-YdaXxD42TpEKzxY2UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سینه‌مرغ با بافت‌نرم و لذیذ و دیپ‌پنیر همون چیزیه که خیلی سریع باید برای ناهار درستش کنی
😋
موادلازم:
🔹
سینه‌مرغ
🔹
قارچ
🔹
پیاز
🔹
سیر
🔹
گوجه‌فرنگی
🔹
رب گوجه
🔹
پنیر پیتزا
🔹
ادویه به میزان دلخواه #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/692193" target="_blank">📅 10:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692192">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjSilfGd5zlnMY12LNui0C_pS9bM6VJE3mNgX6IPhGfS-VAlogyjvCgqnuoM2qX5pfIzxS9DpOLpxcxXKlCzt-6rWLpNWhMqhsGoxhsyQJpwJBhwnDEs8L2DsbRsV80CxJJshkzFWrsHuCnEfZsttU-wdl3q5cLESTPeqXhHxM_LGLfL7u7B2aUYdUdzqsldQ0tFaAnxfYgvVZwcQBvXUjZZLP3JILvexepqvzwRo2qK9je4HyVKLR1kgkM-RNsHucieBa17dFiPqPzyIzQZ8xB0iZm2KKyGwMiCVtYqwdRaezcxFhHrEn1rsfYayPNRuk0kjhDZjq8OyFHGgkHZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نعمتی طلایی شد
🔹
مرتضی نعمتی در وزن ۷۵- مقابل داود نزمیرادوف از ترکمنستان با نتیجه ۴ بر ۳ پیروز و اولین طلایی بازی‌های آسیایی شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/692192" target="_blank">📅 09:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692191">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
کرباسچی: پزشکیان برای حل مسئله کشور باید با ترامپ دیدار کند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/692191" target="_blank">📅 09:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692190">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری خانه ملت</strong></div>
<div class="tg-text">🎥
شلیک به هواپیمای فوکر اف۲۷
🔹
اول اسفندماه ۱۳۶۴ جمعی از مسئولان برای بازدید از جبهه عازم اهواز بودند که با شلیک دو جنگنده میگ-۲۳ عراقی، هواپیمای فوکر سقوط کرد و تمامی ۵۰ سرنشین آن، از جمله ۸ نماینده مجلس، به شهادت رسیدند.
🔹
از آغاز جنگ تحمیلی، نمایندگان مردم در مجلس شورای اسلامی نیز در این
#دفاع_مقدس
، مانند سایر رخدادهای اجتماعی حاضر بودند؛ گاه با حضور در خط مقدم جبهه و باقی ایام با تلاش برای اداره کشور در شرایط جنگی.
🔹
یاد نمایندگان شهید و شهدای سه جنگ تحمیلی، گرامی و راهشان پررهرو.
🖥
icana.ir
🌐
@icana</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/692190" target="_blank">📅 09:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692189">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGsqudr5ePpspjvFiYIO5spntJJehLp9KXSJaRVvvpVkt3nRQTVlcJdHEie8SHCixw9Dj1vV95x4uXc-DNUq7-MSd_6BlfcS_6TRcpF3_nzfWfiV_1wqX6GtFsNFBc_9n4mHZysztC6tWr5PI5RLAwWfXIqoVEYxQgGC5cbksAqH3p2XxTqdcDJNmSjm3U89fz2i8J269jfE4dFOSd9Ws-A2Us3PrzVmteP0rmKHTmYw4g5aAI103cTFQo60cYXL4QZj3V-atf4WPWojDLy3mk7WonaZ00mkwGVmXa1oM_EacudK9NluqES2kv0mm5_yTHcpEu3VHMltDtBi6ECcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ حسام‌الدین آشنا به شایعه امان‌نامه سرویس امنیتی آمریکا به عراقچی: روال همه سفرهای دیپلماتیک همین است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/692189" target="_blank">📅 09:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_جلسه سوم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/692187" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه سوم؛ مشاهده‌گر هستی
🔹
نیت‌ها و رفتارهای انسان در هر لحظه از زندگی، می‌توانند قالبی از انرژی را در بُعد بالاتر ایجاد کنند.
🔹
توبه، استغفار و انجام کارهای نیک، می‌توانند قالب‌های زشت و معوجی که در گذشته ساخته شده‌اند را اصلاح کنند.
🔹
برای قرار گرفتن در مسیر خیر و نیکی، انسان باید «تسلیم» و «انعطاف‌پذیر» باشد.
🔹
نام
«الشَّهِید»
پروردگار، قالب‌ساز زندگی انسان است و این قالب شامل ظاهر، باطن، نیت‌ها و اندیشه‌های او است.
🔹
انسان با پناه بردن به نام «الشَّهِید» پروردگار، از مشاهده‌گری دیگران خارج شده و تحت تابش انوار الهی قرار می‌گیرد.
🔹
جنگیدن با اتفاقات زندگی و ناسپاسی، مانع از شکل‌گیری صحیح خیر و برکت در قالب زندگی انسان می‌شود.
🔹
شهید کسی است که به تقدیر الهی تن داده و در مسیر رسالت خود، تسلیم محض امر خدا شده است؛ به گونه‌ای که قالب زندگی او دقیقاً با اراده‌ی الهی یکی شده است.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/692187" target="_blank">📅 09:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
آلودگی‌های نفتی در چند نقطه از سواحل هرمزگان مشاهده شده و به دهانه برخی کانال‌های پرورش میگو در سیریک رسیده‌اند
/ ایسنا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/692186" target="_blank">📅 09:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc31f469b8.mp4?token=jwjrXv66wBZWyqk815ViJE4jPmsiKovfK2bRUyq-yl2K9ejmmSRZE65_44QsrseW59utqOpbB2s6dTU5ZlLXY5wPaeGrfplit5Glzo51o5oTcBQ_ipMPm3Rb7JUg-T6SF-DCT94RJab4hs43bF8W3ZOM4dvPqMln-Qm2R2QamsMZHNrmLehWk4O-rTM2XNAL20WMnBl8EgN805qG3YmoPsnDXEvAVsPj9Egppf87QOQLAIeKVtJFNxQTgYySlcpMu0QbYA6DNcLLE359fIlTfb5deArbvU4G8kTZMNp3HPDC4m92jtkctO0xobUiNyIRvPu7g61ztacZeeg5dTDTRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc31f469b8.mp4?token=jwjrXv66wBZWyqk815ViJE4jPmsiKovfK2bRUyq-yl2K9ejmmSRZE65_44QsrseW59utqOpbB2s6dTU5ZlLXY5wPaeGrfplit5Glzo51o5oTcBQ_ipMPm3Rb7JUg-T6SF-DCT94RJab4hs43bF8W3ZOM4dvPqMln-Qm2R2QamsMZHNrmLehWk4O-rTM2XNAL20WMnBl8EgN805qG3YmoPsnDXEvAVsPj9Egppf87QOQLAIeKVtJFNxQTgYySlcpMu0QbYA6DNcLLE359fIlTfb5deArbvU4G8kTZMNp3HPDC4m92jtkctO0xobUiNyIRvPu7g61ztacZeeg5dTDTRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلتنگی مادر محمدطاها دانش‌آموز مینابی، برای روز اول مهر: همیشه بهترین کیف و کفش را برای او می‌خریدم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/692185" target="_blank">📅 09:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1bd0d01ce.mp4?token=Bsx1VT_NZQFTrYQZYFtLvZoZEm5aeFSMU_aj-X9CVj3f-5aZ-db_TG1dH1PdAPX-eKCcGO8o0XbRcZnp7qbggPVfDWpM-S6p9l2ZgN248HLFJWrVPB6LJdPvLDGxByV9ZPtwBw0Ee-5MW5CA6PxNK6BgaJLg_fPnXL6Ee5jx5d5d-A2u-2xeU6qf9uQS8YKZSUizLCkFhe5LcymWRlCbsuaVAM1cBQ6Lavgp8OyRmijxe5bPfoZp_GfeVOyWBgklXNmfIZCpq3gTgeV4ML2u9h5Cv_UepK9s67sz93QIqjrnGoSq6QdjRz5c1qzQrzkzGRwUj8CrjwCtz3FN7VGg3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1bd0d01ce.mp4?token=Bsx1VT_NZQFTrYQZYFtLvZoZEm5aeFSMU_aj-X9CVj3f-5aZ-db_TG1dH1PdAPX-eKCcGO8o0XbRcZnp7qbggPVfDWpM-S6p9l2ZgN248HLFJWrVPB6LJdPvLDGxByV9ZPtwBw0Ee-5MW5CA6PxNK6BgaJLg_fPnXL6Ee5jx5d5d-A2u-2xeU6qf9uQS8YKZSUizLCkFhe5LcymWRlCbsuaVAM1cBQ6Lavgp8OyRmijxe5bPfoZp_GfeVOyWBgklXNmfIZCpq3gTgeV4ML2u9h5Cv_UepK9s67sz93QIqjrnGoSq6QdjRz5c1qzQrzkzGRwUj8CrjwCtz3FN7VGg3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنتی‌بیوتیک‌ها را از زبان خودشان بشناسید؛ هر کدام برای چه عفونتی تجویز می‌شوند؟
🔹
هشدار: قبل از مصرف هر نوع آنتی‌بیوتیک، حتما با پزشک مشورت شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/692184" target="_blank">📅 09:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
مکرون: جلوگیری از دستیابی تهران به سلاح هسته‌ای هدف اصلی است اما تغییر حکومت ایران با بمباران گزینه درستی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/692183" target="_blank">📅 09:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKkFInRYJYbO1EAiYSz808yiajuN96P1ku8esd8-Xo5bpB8OJlZRpGkhXF07Z12czW8poqQwjkoxEA5o31SYIPXX5pr4yNkeg-DqIH65EMQfBQ3EVIOh1jwUTlwYxXqm2SK0hAZy8HDTY84aDBRMTYDUKUtgXMdgNPYZMu6iDAQTw7izKfXFrPnYKfYISKXBZdXIfMCjrwbwxlmWpjob4cZjdqky6BKMVm73-l0BVvsdLFgTkXhNiPoYnUnnYYYHVYhucsd3lKNwG8H0yP1rZ-lNo7VCW0vFEV8n44I379bEuIGriHJLF1rcjdNHZQhmCvaXgS_B78LAVI7ichr5Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ آغاز سال تحصیلی در محل مدرسه شهدای میناب با حضور دکتر زاکانی شهردار تهران، دکتر افشین معاون علمی رییس‌جمهور و جمعی از مدیران استان هرمزگان نواخته شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/692182" target="_blank">📅 09:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692180">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
مکرون: جلوگیری از دستیابی تهران به سلاح هسته‌ای هدف اصلی است اما تغییر حکومت ایران با بمباران گزینه درستی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/692180" target="_blank">📅 09:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
کیهان: برای جبران فشار اقتصادی باید از کشورهای عرب حوزه خلیج‌فارس پول بگیریم؛ اگر ندادند به زیرساخت‌های آنها حمله کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/692179" target="_blank">📅 09:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692178">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c37eaf15be.mp4?token=kDDCQvCvq5IdiomFKEpiH_QWFL2zDziiajf-aKQQEjnSNwQ8Xd7D0S_gJ9DoLt9ySIzqibUyGMCo8hQqqd2IsF-fKXNPXnr50UKudWmsdqceGyMcSmXRdoQVnDiyKSZ6GLjo4inNgo0sew6ctdmravGjHE1Ro2sHSqwnR_nrzPRkdccU0KCVUtKm-lfyxDTQ_0Ai2JQVBvjCfbRGyUFCSMlFVVV12-tYywOCLsZwuPSrs4Ej3JkwHANFD60hS-Arz7JzvqsCXbCs2aFxgD5TU_LxZ0CXNEZloQptzuuTNEnHCFuVydvqHUN9ZubN6C-2uB9oigPWkwyB10niwaZVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c37eaf15be.mp4?token=kDDCQvCvq5IdiomFKEpiH_QWFL2zDziiajf-aKQQEjnSNwQ8Xd7D0S_gJ9DoLt9ySIzqibUyGMCo8hQqqd2IsF-fKXNPXnr50UKudWmsdqceGyMcSmXRdoQVnDiyKSZ6GLjo4inNgo0sew6ctdmravGjHE1Ro2sHSqwnR_nrzPRkdccU0KCVUtKm-lfyxDTQ_0Ai2JQVBvjCfbRGyUFCSMlFVVV12-tYywOCLsZwuPSrs4Ej3JkwHANFD60hS-Arz7JzvqsCXbCs2aFxgD5TU_LxZ0CXNEZloQptzuuTNEnHCFuVydvqHUN9ZubN6C-2uB9oigPWkwyB10niwaZVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی که رئیس‌جمهور ایران، آمریکا را در خاک آمریکا تهدید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/692178" target="_blank">📅 08:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0fbd01bc.mp4?token=sqpP9eOLCvIpVwX3G4DAzaN_EQ0tHX8KhdiyLjnHZ5dI0in1MVmaR5bbVNRIo4zrUF7VUQHcr4i7NliOJ4nfM7_yCElTSvz2gbq_maHt8zdwdfYqR0AMODdoy7Fp6D3Qkzjhxxr2eVR8KGqXM8envf_chwQtw16InRobQ1x-NKygkcr1EzRWJroQh7p5Cq1dTPlRJ-AiDzJrleraR3bewS_AW4CbE9A7V4MsXuZDuh2c9M51wqc2F0W6N8iOxww3aWLOtcR0PEc-DPFJD077WGBIJyNDiGVzIOBMKuJsFFZtjOIyXGJUPLtEZrrSxYF2PDE8ecGrE5IuEp4QNypUXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0fbd01bc.mp4?token=sqpP9eOLCvIpVwX3G4DAzaN_EQ0tHX8KhdiyLjnHZ5dI0in1MVmaR5bbVNRIo4zrUF7VUQHcr4i7NliOJ4nfM7_yCElTSvz2gbq_maHt8zdwdfYqR0AMODdoy7Fp6D3Qkzjhxxr2eVR8KGqXM8envf_chwQtw16InRobQ1x-NKygkcr1EzRWJroQh7p5Cq1dTPlRJ-AiDzJrleraR3bewS_AW4CbE9A7V4MsXuZDuh2c9M51wqc2F0W6N8iOxww3aWLOtcR0PEc-DPFJD077WGBIJyNDiGVzIOBMKuJsFFZtjOIyXGJUPLtEZrrSxYF2PDE8ecGrE5IuEp4QNypUXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد کسی که حتی دیر شدن مدرسه را هم برایمان خاطره کرد
🔹
گوشه‌ای از بازی خاطره‌انگیز مرحوم عبدی در «بازم مدرسه‌ام دیر شد»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/692177" target="_blank">📅 08:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06e72836a6.mp4?token=PjUJQdIidf8Lpd5Ym3ApR1oXds15Gs6WZf2MUVZAMU7qdHYtPDytDfPNmCxAR14xukE_ZBU5xOQI7w3QIyj3GRJUaJPl1I7pgnOuhrPGQ4ASiuET2X8-HwviHhchnbjmleS9Pq5hZA5Qt_a6vB6rOvcKB6MwCtZKBs5XGYeqTOpEEGKtkGIyu8u_rnipJq3l0_tROab8r_-sOp0OfnJpUggvmoAdBC7-dOP24d_4QBlhaLBJdy8Wn2WAYENg2ZzAIpQcGEh2lHQy1jCKnMUlnJsjBOmbM2UxRMDpgtRY_UIhVhrFOJGx5rfXVV__bX0AgPrmFICbF0z8OSR4e370eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06e72836a6.mp4?token=PjUJQdIidf8Lpd5Ym3ApR1oXds15Gs6WZf2MUVZAMU7qdHYtPDytDfPNmCxAR14xukE_ZBU5xOQI7w3QIyj3GRJUaJPl1I7pgnOuhrPGQ4ASiuET2X8-HwviHhchnbjmleS9Pq5hZA5Qt_a6vB6rOvcKB6MwCtZKBs5XGYeqTOpEEGKtkGIyu8u_rnipJq3l0_tROab8r_-sOp0OfnJpUggvmoAdBC7-dOP24d_4QBlhaLBJdy8Wn2WAYENg2ZzAIpQcGEh2lHQy1jCKnMUlnJsjBOmbM2UxRMDpgtRY_UIhVhrFOJGx5rfXVV__bX0AgPrmFICbF0z8OSR4e370eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ تمرین ساده برای سلامت ستون فقرات #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/692176" target="_blank">📅 08:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
مدیر روس اتم: وضعیت در نیروگاه هسته‌ای بوشهر آرام است؛ با این حال تا زمان امضای توافق میان ایران و آمریکا، شمار کارکنان خود در ایران را به طور قابل توجهی افزایش نمی‌دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/692175" target="_blank">📅 08:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692173">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e22c6c392d.mp4?token=WyzFWHdROUPIFwlJvHplHNN-YCTPp9vBE2-CyZQ5A7pA-TJxMRfdmRKRPcKjMobREZYScbDcyQcifB7PBqu3_A3WQEzmNx9WTRm9dbFTsiau2XSjDFfn8uLmbLtqOVUYRj18dPIgoS0rgrIyv7T-V8tn-NPSDQGPO3p6ubjVOu0Q1lLkiDF9SZz0FudVxjnTJYFySH6y4SmTR2yQ-rSK_h8cbqoQchro_BvkBMK_DQlU_JJ3s9U5D_yxapgrR3DBZamBawdsq2_AgxwbS9Oo9vD42PU0GD_Skqdc17Kkr5W0o6rfhrhZoVaHv8VPYV68F6WIFK_s9Rh2-Eo_xWkFRkwadEBfZV2s_ysgXUM2-lht5yEd-hX9Z4jGHnFzAtN4-omXVdty_v8Gb8UfBOrEWCOLX96OInYYLg_qH6-9jbsaxOdhTwJwYxnga4aoV4HFAlx9-phtuT0qUDC2duySO4t1pwZW7aOr0pS-nhnrTJPeNGSQDpaLbJi1lZX7rMPFOXCa67Ik_Aoa5TTXSk4ulf2aHMeDtOy6Fi9Ttddgws02NSA9X_ul3arqaqHqxbJabSJIBJu3j8gNz7YNMKrScFzqp_RgpS4qW5db6o5qmydmn9UgVtIW0YtmdjtzV-h1vEMIm0Qlkv_C9Bbcz8-0CDh3MudbARj9L7Q_1uzGBL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e22c6c392d.mp4?token=WyzFWHdROUPIFwlJvHplHNN-YCTPp9vBE2-CyZQ5A7pA-TJxMRfdmRKRPcKjMobREZYScbDcyQcifB7PBqu3_A3WQEzmNx9WTRm9dbFTsiau2XSjDFfn8uLmbLtqOVUYRj18dPIgoS0rgrIyv7T-V8tn-NPSDQGPO3p6ubjVOu0Q1lLkiDF9SZz0FudVxjnTJYFySH6y4SmTR2yQ-rSK_h8cbqoQchro_BvkBMK_DQlU_JJ3s9U5D_yxapgrR3DBZamBawdsq2_AgxwbS9Oo9vD42PU0GD_Skqdc17Kkr5W0o6rfhrhZoVaHv8VPYV68F6WIFK_s9Rh2-Eo_xWkFRkwadEBfZV2s_ysgXUM2-lht5yEd-hX9Z4jGHnFzAtN4-omXVdty_v8Gb8UfBOrEWCOLX96OInYYLg_qH6-9jbsaxOdhTwJwYxnga4aoV4HFAlx9-phtuT0qUDC2duySO4t1pwZW7aOr0pS-nhnrTJPeNGSQDpaLbJi1lZX7rMPFOXCa67Ik_Aoa5TTXSk4ulf2aHMeDtOy6Fi9Ttddgws02NSA9X_ul3arqaqHqxbJabSJIBJu3j8gNz7YNMKrScFzqp_RgpS4qW5db6o5qmydmn9UgVtIW0YtmdjtzV-h1vEMIm0Qlkv_C9Bbcz8-0CDh3MudbARj9L7Q_1uzGBL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه دانش‌آموزان مدرسه شجره طیبه امروز غایب هستند
🔹
غمگین‌ترین اول مهر مدرسۀ شجرۀ طیبۀ میناب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/692173" target="_blank">📅 08:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692172">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
آژانس بین‌المللی انرژی: اروپا در میان مشکلات تأمین گاز، با زمستانی سخت مواجه است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/692172" target="_blank">📅 08:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692171">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ccdbb707.mp4?token=oD-rywUNNa0Fg27wDnYx6xXf0iSq7FPWliYQS-DkvcuL6JxSSM6_zrmwBZSxlHRrjGQboKrVWAnbJlwTtzTd7R7-C0OPTGMV1vIJs33G3xyvcQ72PsRrTEkh7fYubDN0JJSk93TI3PWZuCBM-rIg4W4-DSVHz37gh4j2MeHlMt4q7PpCnnZJX8h515GAzjekiOZRfZyqZdp_Gy9CgDMKX5nVyVjAXN1gZ4BK6pePqdQvyofy6XPW2w4pZuOkbZsGreDCiR22Vw8pqeYoK02Ck_8S0CBOV4aBCDyJLiTfyfzHv9OnzAjr6r0TYdZcixQCRH_UedfFATzairMxEZjasQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ccdbb707.mp4?token=oD-rywUNNa0Fg27wDnYx6xXf0iSq7FPWliYQS-DkvcuL6JxSSM6_zrmwBZSxlHRrjGQboKrVWAnbJlwTtzTd7R7-C0OPTGMV1vIJs33G3xyvcQ72PsRrTEkh7fYubDN0JJSk93TI3PWZuCBM-rIg4W4-DSVHz37gh4j2MeHlMt4q7PpCnnZJX8h515GAzjekiOZRfZyqZdp_Gy9CgDMKX5nVyVjAXN1gZ4BK6pePqdQvyofy6XPW2w4pZuOkbZsGreDCiR22Vw8pqeYoK02Ck_8S0CBOV4aBCDyJLiTfyfzHv9OnzAjr6r0TYdZcixQCRH_UedfFATzairMxEZjasQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رحیم صفوی، مشاور رهبر انقلاب: الان اگر رهبر انقلاب مصلحت دیدند و دست دولت را در مذاکرات باز گذاشتند، خیلی مصلحت‌اندیشی بزرگی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/692171" target="_blank">📅 08:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692170">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
عراقچی در دیدار با وزیر خارجۀ فرانسه: نمی‌توانید مدعی دلسوزی برای حقوق بشر باشید، اما در برابر جنایت آمریکا و رژیم صهیونیستی سکوت، و همکاری کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/692170" target="_blank">📅 08:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692169">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd08b2201.mp4?token=pc70DU1L9YdDnLDFy8ug8XhIMB3yItRUqlliwbsoMW_I7hEYrcgL_LQ8ErnGekVI5gRmVNyAT0k0sM3km5QHYP5wMU2F7EaCKB6cQayGVyaWNOSfitjz2Ww2hk-HIc0bEPg3T-eSiRCkX0YM0dfZ6rxhGrIdPfExAY_hNBfgf2lRCdPAlpd7c366bjcPPPgHtWIgUsw9yBOZL3h796Pu4I-V-K5UC9Sm0wo3NPgvwRPFUKxFmeDLkUMvtvxWbWG02eePFMEb1_lPIJM5K7yDkxGS4DSc0cpkXfT9NhfAoMdmCo5jkB67fMvvraar6pqKlr1i-5NKeJfp2AQ-svFVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd08b2201.mp4?token=pc70DU1L9YdDnLDFy8ug8XhIMB3yItRUqlliwbsoMW_I7hEYrcgL_LQ8ErnGekVI5gRmVNyAT0k0sM3km5QHYP5wMU2F7EaCKB6cQayGVyaWNOSfitjz2Ww2hk-HIc0bEPg3T-eSiRCkX0YM0dfZ6rxhGrIdPfExAY_hNBfgf2lRCdPAlpd7c366bjcPPPgHtWIgUsw9yBOZL3h796Pu4I-V-K5UC9Sm0wo3NPgvwRPFUKxFmeDLkUMvtvxWbWG02eePFMEb1_lPIJM5K7yDkxGS4DSc0cpkXfT9NhfAoMdmCo5jkB67fMvvraar6pqKlr1i-5NKeJfp2AQ-svFVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت انگلیس از اسرائیل در سازمان ملل
نخست‌وزیر جدید انگلیس در مجمع عمومی سازمان ملل:
🔹
ما در مواجهه با تهدیدات مداوم ایران, در کنار اسرائیل می‌ایستیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/692169" target="_blank">📅 08:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692167">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
جمهوری آذربایجان رسماً پروازها به ایران را تا اطلاع ثانوی متوقف کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/692167" target="_blank">📅 08:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692166">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
عراقچی: بازگشت امنیت دریایی به منطقه مستلزم توقف اقدامات واشنگتن در زمینه ناامن‌سازی و تروریسم اقتصادی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/692166" target="_blank">📅 08:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692165">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بقائی: تعامل با طرف آمریکایی از طریق میانجی قطری بود و شروط ایران ابلاغ شد
سخنگوی وزارت امور خارجه:
🔹
این تعامل با هدف ابلاغ شروط ایران، از جمله خاتمه جنگ در همه حبهه‌ها، توقف اقدامات تجاوزکارانه آمریکا، محاصره دریایی و جنگ اقتصادی، آزادی دارایی‌های ایران، و... صورت گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/692165" target="_blank">📅 08:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692164">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfvsdLZ2DBlYZj3TI9p4wy-DGVPPDKTWybaKLHLYjYSUAbLA4ioJFo6W66-MgjVfzX0csaKAyl_4mDCx42ucXOhdpZWvxivsMXcHCCAEL7P8AbkBj3qcCUK-ZLxXvDD8mvHy2Mz0dPJRwqIJvjhXBba4kklY68MBuTNrc-sVREVtcl5vOuaRbcBmM8hAXePopaex-78ch69qeE28fm5VkplHlBicUeSsSRsxsykZOkoA_siWqGQEPVln5z8r3t7chfAOVlLbROx7TFjtvvYvffWkD9ZY1uvsxul032j6zhs7NkdYsAGo9z_QdzV296J5sTYO4YSs1S5lWBuTEOwDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ویتکاف: مذاکرات غیرمستقیم طولانی با هیأت ایرانی داشتیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/692164" target="_blank">📅 08:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692163">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17cbe4d41.mp4?token=f1AjfI1d-7yiiquwFLRB5KjwJMndt8rP38EBFkjS5XVO6zSUYMdSD8syy8EpTCrH9bRRmbSUkumDEn545vbq1qSK1KgSZLoLGoG8pBgrCiewJLFziAlTFyp0dk7nabVribEPp2onP6FRMk6_i3sjcOVNsHpN2ukzPN3eZpTIb9g3xarZbSTliRTA9eal3yYU1gr287TO4mmUQ-lEfucwnBO5GdGwkWeqthaiKcvIRw3yrJLiAUSppNGnfSQ6t_QBOTDjklICw_HgaLPItTkX9haA1sgUralznEW07aLNqtRzK0CLqy5JbFWgU80JcRKXUeiCtXwDA2tj_6hozWlP5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17cbe4d41.mp4?token=f1AjfI1d-7yiiquwFLRB5KjwJMndt8rP38EBFkjS5XVO6zSUYMdSD8syy8EpTCrH9bRRmbSUkumDEn545vbq1qSK1KgSZLoLGoG8pBgrCiewJLFziAlTFyp0dk7nabVribEPp2onP6FRMk6_i3sjcOVNsHpN2ukzPN3eZpTIb9g3xarZbSTliRTA9eal3yYU1gr287TO4mmUQ-lEfucwnBO5GdGwkWeqthaiKcvIRw3yrJLiAUSppNGnfSQ6t_QBOTDjklICw_HgaLPItTkX9haA1sgUralznEW07aLNqtRzK0CLqy5JbFWgU80JcRKXUeiCtXwDA2tj_6hozWlP5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیمای حامل رئیس‌جمهور و هیأت همراه برای شرکت در مجمع عمومی سازمان ملل وارد خاک آمریکا شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/692163" target="_blank">📅 08:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692162">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1mbySuOURwtt4Dl61RqX1F2jf-Yp7BcIAAhzKHWxsSP_O009-BhUgoe1FVvQCDoXTi1O1UqrO053k8gFTnY4XepStivBoXAzkTkdx2QX78N5wm_t0AYPGFGAiZiuTjXJtMPsNvBuf1kSZdLr5oQPtcd-0ooz-RcUwy3_XvmOfMcaLNBKep1hwdI_lSKtljonrwByl0MwPqZEOLvvCXzVipjJX_pRSHaa1k8tLb8PXtrcSkm3PT0jfGjJAbkXch2qtNYVGXDChNenRUhxsYJYCWdctTDUutAQJbSLSCirR0gqVvxBS87RbMS_aqILNwVf1_zuJr2wwIL2KO4_xH_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱ مهر ماه
۱۱ ربیع‌الثانی ۱۴۴۸
۲۳ سپتامبر ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/692162" target="_blank">📅 08:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692161">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c26154995.mp4?token=sPQC-HrI81t4MyWFjTNiPROoHaIeyx2KaQ49WMwTHaeuAH5HBv8tBevqDn42THyNYwyoZKR2ngItiI5tR-MNGBavoTStiLCjfu6SW4gBGgn1oEAdpajJRJa-122dppP_xZsbe0skBtMvDGBwynir-pcSeLmNu3MbuqD47-N6jnoHpri3gBCMIcCHa4nVU3zX0vDhSWcQZe9Tcd6XnIiiOeOO3SfwjJx-UTk3nvrMjsFXLUG87dGHoXHWm4Rgd35LU7hze-c8zaWLsGhq2Ll6R91eZaORgeQ1TEkL7jVa7cnhj-8bOQBl9hsVx4_HCQ510Dm9vBLRaHxNde2kiXhM9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c26154995.mp4?token=sPQC-HrI81t4MyWFjTNiPROoHaIeyx2KaQ49WMwTHaeuAH5HBv8tBevqDn42THyNYwyoZKR2ngItiI5tR-MNGBavoTStiLCjfu6SW4gBGgn1oEAdpajJRJa-122dppP_xZsbe0skBtMvDGBwynir-pcSeLmNu3MbuqD47-N6jnoHpri3gBCMIcCHa4nVU3zX0vDhSWcQZe9Tcd6XnIiiOeOO3SfwjJx-UTk3nvrMjsFXLUG87dGHoXHWm4Rgd35LU7hze-c8zaWLsGhq2Ll6R91eZaORgeQ1TEkL7jVa7cnhj-8bOQBl9hsVx4_HCQ510Dm9vBLRaHxNde2kiXhM9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔧
هرچی برای تعمیرات لازم داری، یکجا داشته باش!
🛠
آچار بکس
۴۶ عددی مدل Phunda
💪
مجموعه کامل و کاربردی برای تعمیرات و کارهای فنی
🏠
مناسب خانه، خودرو، کارگاه و استفاده روزمره
📦
۴۶ تکه در یک ست جمع‌وجور و کاربردی
🔥
قیمت ویژه: فقط 1,498,000تومان!
📌
دیگه برای هر تعمیر کوچیک دنبال آچار نگرد؛ این ست رو دم دستت داشته باش!
خرید از سایت
👇
https://memarket24.ir/product/fast/27006/180124/</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/692161" target="_blank">📅 02:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692160">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
منبع آمریکایی: آمریکا درخواست رفع محاصره ایران را رد کرد
/
فرصت توافق محدود و اختلافات همچنان پابرجاست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/692160" target="_blank">📅 01:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692158">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTeO6R3vy3D47rC0CAMlNPvB9ntPQJxmwJOly_OAIRdUJAKuv86AinUfa5yAOpzip8xI89xcMrQuDe_HJEDhsHA8vyavuGgDxDfVhf93L02BXhJcP2zx4eh6ZLC3Qg3S78HbzBD80z1hZtzOj2ZdOseMfZT1XsDtuwhQ6FrSzYJ7DxctBiAn_yQLobPQi4tCa16k5WIferlcKTeDtsZg2X7j_VgOO0BTRLz0njLH-_A_NUiv4d_VYV861kuPPG30xrqapjdoL1a-3asnC6If3t1_pv4omTTwFyqOgeS3VePivPf0wpRwqwBDO8Ruq9mLjoq4O-yH4VLHw2fPkgLccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای حامل رئیس‌جمهور و هیأت همراه برای شرکت در مجمع عمومی سازمان ملل وارد خاک آمریکا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/692158" target="_blank">📅 01:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692157">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
دقایقی قبل صدای انفجار در حوالی جزیره قشم به گوش رسید. به نظر می رسد صدا از سمت دریا بوده و اصابتی در داخل خاک جزیره قشم صورت نگرفته/ ایرنا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/692157" target="_blank">📅 01:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
‌هواپیمای حامل رئیس‌جمهور حدود ساعت ۱۷ به وقت نیویورک و ۳۰ دقیقه بامداد چهارشنبه به‌ وقت تهران وارد فرودگاه بین‌المللی جان‌اف‌کندی می‌شود
🔹
این پرواز عصر امروز پس از سوخت‌گیری و توقف کوتاه در الجزایر به‌ سمت شرق آمریکا حرکت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/692155" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: صداوسیما را از یک رسانه معتبر به رسانه‌ای بی‌اعتماد تبدیل کردیم
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
صداوسیما را از محل بزرگی که می‌توانست برای مردم محل اعتبار و اعتماد باشد از دست دادیم.
🔹
ون گشت ارشاد در خیابان نبر که زن و بچه مردم را به زور و با استرس داخل ون کنی؛ اینگونه کسی با حجاب نمی‌شود؛ حرکتی بزنید که مردم امیدوار شوند‌.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/692154" target="_blank">📅 00:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01252d1672.mp4?token=ZJ9zclHJ5lVbv-Ys6rwd243zQadm1DHukq-O4BPTwk9avC-F1A40HyMw3OVWWmHTI_s9-SDRIaf1Kks_Hkv0_NVvE8IA4-i-VJPpC83uEHB__uQIpYfkvcNjRxM4nqXAwPVuQYYbaxb9dwJnhjsmeUxIcHfSpRx1QBjvnOQgPvqvsl4uyWKeCVia9DeAD2iLCuyaKJZAV4A0e9r4_44XHleSxcmJX0Nanv1hgrpA1eYuDG7JZ8WGUbixTJkGh8lcOogvCRUgTsE5xfXccCd2TpWEnlJ3Nr-bp6kbVC2deQu9QRevtQb2dmSn8aUIhVMyWJfC7h5UBD6Qtb03JR-WEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01252d1672.mp4?token=ZJ9zclHJ5lVbv-Ys6rwd243zQadm1DHukq-O4BPTwk9avC-F1A40HyMw3OVWWmHTI_s9-SDRIaf1Kks_Hkv0_NVvE8IA4-i-VJPpC83uEHB__uQIpYfkvcNjRxM4nqXAwPVuQYYbaxb9dwJnhjsmeUxIcHfSpRx1QBjvnOQgPvqvsl4uyWKeCVia9DeAD2iLCuyaKJZAV4A0e9r4_44XHleSxcmJX0Nanv1hgrpA1eYuDG7JZ8WGUbixTJkGh8lcOogvCRUgTsE5xfXccCd2TpWEnlJ3Nr-bp6kbVC2deQu9QRevtQb2dmSn8aUIhVMyWJfC7h5UBD6Qtb03JR-WEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف یک مورد مشکوک
🔹
پس از پیدا شدن یک کیف مشکوک در نزدیکی مقر سازمان، تیم خنثی‌سازی بمب آمریکا اقدام به مسدود کردن خیابان کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/692153" target="_blank">📅 00:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692152">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff7ba5922.mp4?token=lcSH23rHm2evZxcZ-UiBmr1V5ChpYgfr-bZwbWNcMdeoMkDpNKT96SzkBY-9B-3P5X6tVhdJVTV6RPC5JixXOO6_clZd8aC__0hj7FnrarJJgU0UtxuNCdgJarF4c-q8ESDtnYYdoOsHAgej-QRPMNGER71HngXnScYRn8el9pqu7MORZkWRIs5oGiiXV2gfVVxVJ6fL0JKDAOMLssbq_4HQQlzzr16QLWavp2Db8MnRnZb42dL2UWqDhvnOKNE0DYJUGD0-rzff2i0aFdUvk8-xAXe0hg9rPIpvTwEYySWXStz4DCg0BuEjsMbCGdzCccPXy6wQUkhR9MFnGspv_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff7ba5922.mp4?token=lcSH23rHm2evZxcZ-UiBmr1V5ChpYgfr-bZwbWNcMdeoMkDpNKT96SzkBY-9B-3P5X6tVhdJVTV6RPC5JixXOO6_clZd8aC__0hj7FnrarJJgU0UtxuNCdgJarF4c-q8ESDtnYYdoOsHAgej-QRPMNGER71HngXnScYRn8el9pqu7MORZkWRIs5oGiiXV2gfVVxVJ6fL0JKDAOMLssbq_4HQQlzzr16QLWavp2Db8MnRnZb42dL2UWqDhvnOKNE0DYJUGD0-rzff2i0aFdUvk8-xAXe0hg9rPIpvTwEYySWXStz4DCg0BuEjsMbCGdzCccPXy6wQUkhR9MFnGspv_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرایند شگفت‌انگیز سیناپتوژنز؛ اتفافی است که در لحظه یادگیری در مغز رخ می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/692152" target="_blank">📅 00:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سرلشکر صفوی: باز شدن تنگه هرمز در مقابل پذیرش شروط ایران است؛آمریکایی‌ها مانع توافق با عمان در مورد تنگه هرمز هستند
🔹
نه‌تنها تنگه هرمز به حالت قبل برنمی‌گردد بلکه باب‌المندب هم به قبل برنمی‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/692151" target="_blank">📅 00:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ترکیه: پرواز ایرلاین‌های ایرانی به ترکیه همچنان برقرار است؛ محدودیت اعمال‌ شده برای ماهان به سایر شرکت‌های هواپیمایی تعمیم پیدا نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/692150" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkneNiMJ5jM6fQbawYkaHPjMAowmv6ClPD0Bs_gx2gBULODY1anPBZ_aWekJDKNSHTPmpQ_NPhrpBDVabUtHe9PT-oy8yVY8rgQ7VsPtyyci6faflmGOXkPb3yyCTZpDlAFY5YBe3qUM1A3_1cpauHRsvyi5uH7H0SEjTU8Cl_y3o7hjdtStCS1Rcop4NXBhkTW_qo7PhJMdbLPpb-QbkncYCQxyKo_AIFAbtE7FKdtm7uZLQqj9N4ysAP_N4HzxTA88KEgW3Nu30y3itcXrEOxPPqrBYbp_fSgB3fZLvSA0cX3WU3_PwaiBmoT7w1fUJ-zMyvyZzhq2Ok6cx7HkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/692149" target="_blank">📅 00:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb8e6abc3b.mp4?token=G2Mh_Yb9mGz937GjhRNrO1e_8d6gPUCmlrfTt5xsFGMpM22I2ifqSXQIZw_qZXj_8DLjL-1C6AzucYKyvluPGH53Ikrdy261WPuYVWPAWVRAk2GGz6gGhZzEjAToZiIcqydAaRUNNl_sz2VbIk01wDFJEzuiCKWTA85gJj4uf5XrSl3wMcumDKxNyybanFlx-4aUhNVYbemKdYStBzoZqJvEILJpgjiMQrTrjsGy2TsWYLKS7QCIzD65Vz4H_cBXHUEeqQSbKn43tUwiruK8FhH4hlaP0laYQvWEIOukgcaWZxgRhaJ7t1AqUy-cNZbL2-jlq64J-MK5I_XNzRgdTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb8e6abc3b.mp4?token=G2Mh_Yb9mGz937GjhRNrO1e_8d6gPUCmlrfTt5xsFGMpM22I2ifqSXQIZw_qZXj_8DLjL-1C6AzucYKyvluPGH53Ikrdy261WPuYVWPAWVRAk2GGz6gGhZzEjAToZiIcqydAaRUNNl_sz2VbIk01wDFJEzuiCKWTA85gJj4uf5XrSl3wMcumDKxNyybanFlx-4aUhNVYbemKdYStBzoZqJvEILJpgjiMQrTrjsGy2TsWYLKS7QCIzD65Vz4H_cBXHUEeqQSbKn43tUwiruK8FhH4hlaP0laYQvWEIOukgcaWZxgRhaJ7t1AqUy-cNZbL2-jlq64J-MK5I_XNzRgdTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ما به دنبال جایگزین برای حکومت ایران نیستیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/692147" target="_blank">📅 23:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جلال رشیدی کوچی، نماینده سابق مجلس: آقازاده‌ها به شرکت خارجی می‌گویند فاکتور را بالاتر بزن/ هزینه‌اش از جیب ملت پرداخت می‌شود
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
آقازاده‌ها از اسم پدرشان رشد می‌کنند. بیزنس‌های پدر را از طریق آقازاده‌ها پیش می‌برند برای همین از نظر مالی بزرگ می‌شوند.
🔹
آقازاده پول را از سایرین می‌گیرد و در سودش شریک می‌شود و می‌گوید پدرش امضا کند. مگر می‌شود پدرش نداند؟ خودش را به ندانستن می‌زند.
🔹
با بعضی از آقایان صاحب نفوذ برخورد داشتم. شک نکنید پشت پرده یک سری اتفاقات می‌افتد.
🔹
آقازاده از شرکت خارجی کالا را می‌خرند و می‌گویند فاکتور را بیشتر بنویس. در واقع، پای ملت فاکتور کرده است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/692146" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692145">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
حملات موشکی عربستان به شمال یمن
🔹
منابع یمنی گزارش دادند عربستان در این حملات، مناطق «مران وحیدان» و «الظاهر» در غرب استان صعده را هدف قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/692145" target="_blank">📅 23:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692143">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc9f35f8e.mp4?token=BIkDBFCkZjtRqWhL8LZhJd3UIrYRPtsHGWCf_zbQ1qgI1T-2JoGyWyrZodn3rUNU7Yew9Q2-snEfiVdUEALCZs2-QXLKfVCbbphpJzbdpA1x5vyG1dKVFFmH5Bg2eaiRMZxUks67ygT-HSiQ7qOzK3SCEZPxtSiUwIaavVYe_TdmjS4QR5qTDDIavvWqaRF5vhVdvRgGVxaRdTNde0TJGvWw-xyOQzcQM2G-rdwoqTJRI4wapKMGt908EH8VzOnZ6nG_6y0EtioMXV1wV0yoPO92sfyoq9Rwh8L2qBH02IsRvIdKXHdtSdzzya49OiJ6lu5dw9a8-MzIujS56L_WuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc9f35f8e.mp4?token=BIkDBFCkZjtRqWhL8LZhJd3UIrYRPtsHGWCf_zbQ1qgI1T-2JoGyWyrZodn3rUNU7Yew9Q2-snEfiVdUEALCZs2-QXLKfVCbbphpJzbdpA1x5vyG1dKVFFmH5Bg2eaiRMZxUks67ygT-HSiQ7qOzK3SCEZPxtSiUwIaavVYe_TdmjS4QR5qTDDIavvWqaRF5vhVdvRgGVxaRdTNde0TJGvWw-xyOQzcQM2G-rdwoqTJRI4wapKMGt908EH8VzOnZ6nG_6y0EtioMXV1wV0yoPO92sfyoq9Rwh8L2qBH02IsRvIdKXHdtSdzzya49OiJ6lu5dw9a8-MzIujS56L_WuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش اختصاصی شبکه ۳ از وضعیت مردم غزه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/692143" target="_blank">📅 23:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692142">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197e752b37.mp4?token=MG6VKjGRuq_tg41BM0c1c_NoAZYqMUYLa5FDzvDm02yw-22MkuzcTlJEYLUKkWAUtEHkqpZaYlHg0hcpbE_laK1whC1EAy9OOc4e1qMPDc2ANQ2ApMYQvStWAdaUlp-7xrAU46_1VBVXGNGq1FUl0xA66R1El0fn86LbMNRfGPO92BkdBNtfadvzl8GqF2nBzfasYD_yNYyNc7-VtudmDrssU7lPriOgmO99giwIwwrRvlSPK7fqT-eBh-8UQIAw69-gWpf-DVMzhMNtxJmrRt5W5Acx7SIVtJbPEpqZfQ3GOugo5fD1loYDff0549NxYw9JpWQJKxGz0hdXLm06fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197e752b37.mp4?token=MG6VKjGRuq_tg41BM0c1c_NoAZYqMUYLa5FDzvDm02yw-22MkuzcTlJEYLUKkWAUtEHkqpZaYlHg0hcpbE_laK1whC1EAy9OOc4e1qMPDc2ANQ2ApMYQvStWAdaUlp-7xrAU46_1VBVXGNGq1FUl0xA66R1El0fn86LbMNRfGPO92BkdBNtfadvzl8GqF2nBzfasYD_yNYyNc7-VtudmDrssU7lPriOgmO99giwIwwrRvlSPK7fqT-eBh-8UQIAw69-gWpf-DVMzhMNtxJmrRt5W5Acx7SIVtJbPEpqZfQ3GOugo5fD1loYDff0549NxYw9JpWQJKxGz0hdXLm06fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عامل ترور شهید کاک درویشی چگونه عملیات تروریستی را اجرا کرد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/692142" target="_blank">📅 23:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای
لارنس نورمن، خبرنگار مشهور وال استریت ژورنال: امکان بازگشت به تفاهم‌نامه اسلام‌آباد وجود دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/692141" target="_blank">📅 23:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy8wKfNgUsIi_Oka3JeAbl20-qk5d00lEczPlVY9mGLVcS3M3H7iY0DdtZ5-j3gY_TwjAioAInfrVwVaCFEvlhhjL7XbB3VR6BOoqIESF_ebXTHWzZsa0vHGWpcefxsFrFccFzMQLdv-PSU-ooMej31KWMLnyFb6Xvj2mMy-hp5ehgI00qwCeoBPpiOQrKUM0ElGqsfu1x4WeTyCz1C-IEsY21Bhbw0HMo5hMsyJSsUqDoiDZ2na0XeBuUWaYR_lMDsKNV-Si-Af78oVFUwdSxgLBils3lHUye7mvAdSzsTlQlaiGDTe5wyEVHSP0RBD7XYggfjWqkIdT6ltREwpvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسپری کلاژن‌ساز خانگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/692140" target="_blank">📅 23:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692139">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
قیمت گازوییل در بلژیک به بالاترین حد رسید
🔹
با اعلام وزارت اقتصاد بلژیک، قیمت گازوییل در این کشور با افزایش بیش از ۳ سنت، به ۲ یورو و ۵۰ سنت در هر لیتر رسید و رکورد تاریخی جدیدی ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/692139" target="_blank">📅 23:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای واشنگتن پست به نقل از مقامات آمریکایی: پایان جنگ با ايران، اولویت اصلی کاخ سفید است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/692138" target="_blank">📅 23:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-692137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پیشنهاد رشوه ۳۰۰ میلیاردی به رشیدی‌ کوچی؛ مصاحبه کن خودروهایم را بفروشم!
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
بنده خدایی یکبار اصرار کرد و سوار ماشینش شدم. گفت این پول( ۲۰۰ تا ۳۰۰ میلیارد تومان) را از من بگیر و مصاحبه‌ای کن تا بتوانم تعدادی از خودروهایی را که خریده‌ام، بفروشم.
🔹
این فرد حتی کیسه ورزشی حاوی یورو را به من نشان داد، اما قبول نکردم.
🔹
وقتی داشتم پیاده می‌شدم به من گفت که این پول را از من نگرفتی، اما همین را خرج رد صلاحیتت میکنم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/692137" target="_blank">📅 23:41 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
