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
<img src="https://cdn4.telesco.pe/file/BTzqOyjUJdCc5XdnxlQ7zqFf2zaoV5tgStPezha8ou2xCAp3s5f4hss6muFsAW9u5yfdr0mBp-JJQLdFvIOIGviOzHT5W8CvNnM7TpRufMPJxgb8KSLvb13QB9xt8GjNKHc4wj3WVVX8V6OBfA37juzjG9iHyxDfRdGyQT-LU87GrMi1CxR5RIyd9J4Uy1nnUmkxEJ1cE2h7mP_5zzug5hiw67Va5v8mHTv9prEOeOCoQr84_y3Bh382olVZkmacHllkJ4DCDTlnKgqAB2tBLjbjZ5o-rLe7Ajfggbj5OO6N3F6UxyHVRfAVfOTGTgo0yzc9aMIwqpw4kPqahcVKeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 318K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 13:45:33</div>
<hr>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq5Q4hX3wOzjgdOFkEN0uprHZEScEvG_ke-lf51LmMXOkfSqxv1Qa1CVoz89SL4w3KMzSpqDstOqxWhcWh_nYkfVB8aQ0pP4BThcFLr8ecTd6rNXay_QC3sYk5ze4cPqlSf9tkBOvoG6EvYdlemk59F3UW2t14tKVoyPudUqtcUara68n2QFQdpvYnIMReCg9sbfWvNrlOGq0zgmzcj2JBSXCUsxRGMXPMeRL2aCJl1qo1VGBSlckdSVWO5BQJ7xNDrdmNB03dUatwKqIe1q9IaRdGx6XIa_L0RyylGOb9DRZaxjnLfmaTrMQWEcHNYSBFuTLKrXF59EUl9FDI9cLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2dMDdwIu6EgJcVDzLsjWw02fVd7Yk7LVyWA1Abe9Lo_rP35Iy_C5ZbBoIT0zGxiLHHd5FnuXY2qHiBRHXoy3ifvabl091rIqpE2q1UXUb939xijOD8hMHRPYzMD0iGxn9QNaOF0x6jz4UNEg80xjMJhrevhXZhIqAVRGvBcxeBpwAvDVRCqF-GZMDjqILzx0ipP5gDmCyxwGoc6hWzgGjVn4m1nV3NIIyBBHcEK0MsUj7fP0hIsj82jyb-_4aZ_GNxEgXpZdoboOkr9-Y2eKTQlb3gVJbiRse5cUmYm-YZxVBYurEli-hCgWk3A1y6WT9GB-vKzVltw3OPmud5prQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYepwfvNvH43Q3k6SuCmTQHjV_v949qt5njCMaa3bybX3suewhu4AG1IGZQn4mJ-cYo1TskzTx9nQuuNopC4t1WIazOloLWh_S4h1WWVjpj26zh8xmalnZzVdkgoKtqt90Mi7uAicojSicC5xcci3E0Hsy1wVIbRwDINybzzOuZv2JtDNzw56qF-xRUYo7p3Iw69L7u3VuBQaVjeoLEJanh3OFdH3L004Pm45lk4848mF_ZiJfns-RWLyu0brMEMMY-HXBe_H9HGf3gFrB2UTqQWTp00O2DPd7ly0021wTtig-ZjO-Yi_vPJkJVWxzLHmVS8pZSHGgYYdlMCsOVNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upiFSqODacQdRwNUbIJX0WGDqfz8V_tiiQiJ-e_5gIidr7rZeYZNoqKMUwiw3NB2e5xVHiLg3qVX3p0OpPQ6Qd4ZZqMP0LFuw1Bel2QFk1-mPdeauX6RR7AU4svf4lZnr6gb7TETTcbWA11LCwAB3RmKuAfjkT75yhTCuFgsAZ7P_bvxrwJ1BS91ZzReQro0FwpWlfX3iE3TwJasMrelIzszLcIBwQY0hSSyAdhg-uBVLIiPInNlRB-gBPtXbJ_vGqpigyYbAkR4xSg8AexW4JAnZUpOkyTfA7iGDNkY5ZBHwjFlmkGydYLqA6FTf4d8e37BWVblmEwY9lYAgWQYSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=bM4USfpelI7eCm6brTfHxCd9pEry6FNJUBK6K06fXhgYRuBX0YYawH8HJNIvHzsPS17JwMQStl5nIOQ6cATglJYoxHWZnFUZq6CDBYZpkYLP7ciwMQq4vftworsL571JmKIyRtuRYdTPMiiCe-BQH2k4zW_vyC83KVyWgySxHHzCv_g6B3ZYckjUaeVlQ8tezkyfIiYBvXgU4vHY48ghU2cmLWBNKKlIt1tZMX43-h_hRm-XZeu0RZzUBAkkoej2RNprxBFN2dMlI8bvAkUHBPz49mAqC-bw_lpjK_aSyfX_KnDwKmbBlVuoL0YQZGDua-1n2875ZLMHar4HFFu76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=bM4USfpelI7eCm6brTfHxCd9pEry6FNJUBK6K06fXhgYRuBX0YYawH8HJNIvHzsPS17JwMQStl5nIOQ6cATglJYoxHWZnFUZq6CDBYZpkYLP7ciwMQq4vftworsL571JmKIyRtuRYdTPMiiCe-BQH2k4zW_vyC83KVyWgySxHHzCv_g6B3ZYckjUaeVlQ8tezkyfIiYBvXgU4vHY48ghU2cmLWBNKKlIt1tZMX43-h_hRm-XZeu0RZzUBAkkoej2RNprxBFN2dMlI8bvAkUHBPz49mAqC-bw_lpjK_aSyfX_KnDwKmbBlVuoL0YQZGDua-1n2875ZLMHar4HFFu76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBW9jpbEUDjmQl6aS_aWpbBi8dtg2qTWpxoOi-I_yPjn_fgD0gsaeJDa63ixIliM4l6i7AQ3XpbfBG7ppbfPrqSgQPSB1xBAn2jX791ExxoZERFUNYdsyQb_zQMPzxTm1gexNPhKYJHvKW4Pksj3dupWG6u1Gj40kGLiiiQ3JzNavsIL7UQoLw_e7uFG-ZydHpbR8U3dU50zAmobMpEHQllSFxw9MH3df3kYUt16d-MOnCJMv1hK-1npSMwGdGBzTAPJs8aleth0GiwTLRtZD_Y9cKnSixF8vZ9pO3Pf55nri-oHOACYJuLI-IV3DlKE86u3WOznHb_4spIUUA53vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار مثبت 18 و جذاب جام جهانی رو در پرشیانا آنلاین میزاریم. اونایی که جنبش رو دارند اونجا هم جوین‌باشند. ادمیناپست‌های خوبی میزنن.
🫦
🫦
🔘
@Persiana_Pluss
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/24359" target="_blank">📅 12:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBpYhhjeAwADwu28oAyxFGI-7qnFbGHwD1drEeaZVtoL6l-1rfqvBGXLEvxtCjOOyadWm5pnnvjS56tUowBSOgVqudRxLUEoBioQTCfNfPotgE3xq3GSZJq200m5VUM0hcF78MV8RPrn6HLFFhm5CLY7fyPujpeBNxCvFE6y_QWCWzkP9KJV-jZHbdCRo7hBd15SRrQM66MO61WqxhKPd5mPqZ2oMi4oEKXx5zg1m7pG2jtkLeZOKT6j84RO-3thcjH01SOBMlT6WRdeviCG_NkQ0KHdhXvLipbq0wAATdh_M06AoUOs3F-Oc7nR3t3ukBZzlLUWGS_rvq5S2NogWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس: دراوج‌فوتبالم و درسن 34 سالگی خداحافظی کردم تامردم روزهای درخشانم رو از یاد نبرند. موندن نویر درفوتبال درسن40 سالگی نه تنها هیچ کمکی به تیمش نخواهد کرد بلکه باعث خواهد شد که مردم روزهای درخشانش رو از یاد ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/24358" target="_blank">📅 11:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6tJ-Jo_OUNj37B9fvhU5LlKrOO20QJidCSx9kFSfsO4E7EzhI6OARyRMe53KiMiu96xyqqMjJCBNBwqAmb8XOb51MqTzFXOkFWglwrZFV-JjsW8S8g6_nOwPqKNJQYAU0_biJvIfXOGZ2522c3KzmeJ_JFwKXH-92r63RiF6Vm2-1alPV5Ov9fR8HrLdTbPa34YCV3imIxfSbYiws1R7qZh44P-FBqqPrCWaTBfeVspvJ_f46HXySqqCKeppQTuJSNKt5_3dSk43T9ekp-v2l_XWwlaXtkrH6Y_OnT6HA_I9EsHnWYaBcbJPNMqP6cRfYqYRClgUej-SBusxd0FxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الانگا بعدازمساوی‌سوئد باژاپن خیلی‌ناراحت بود و فکر میکرد صعود نمیکنن. بعد از بازی رفتن باهاش صحبت کردن گفتن آروم باش، صعود می‌کنیم. پاترم توکنفرانس گفت بهش گفته بودیم مساوی هم کافیه ولی یادش نبوده. بهرحال‌الان می‌دونه و خوشحاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/24357" target="_blank">📅 11:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFS0Q0-3RmZKMon64cvhrzhQYqfyvRewe9ga770RD9Ry6Ffo3J68go7yQHN1D3v-3l4ynMDvC-VlynsBYMugbcIi8xQF_JpO0coZG--Mx6TuKff0xnq5zmrs81O-k4kG9Tb_146KBA-3mLsjBX2vfcEemlRf8LNRViVArU1yXRY6IpP4R_wWlEmpMT9jlLKln1mJIRx4h328wYGTLcTVWTAK7ACC2ng_veJHdUNn5buv67FLv3FZj1OLowE5xS0RGy9XxYt81RVsyqbyDBB1I3mChRw4qzQXrqV3C02uRi1rw-B7gEKtpt4qW7bNRa9f-0F77sh_riOOo_2GLoTjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
ستارگان رئال مادرید؛ وینیسیوس، امباپه و بلینگهام در این جام‌جهانی در اوج آمادگی بوده اند و ۶ مورد از ۷ جایزه بهترین بازیکن زمین را برده اند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24356" target="_blank">📅 11:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8eiVy6hYsT27ASlDsh7c2GqDd_mKKPJW22DsjlzRN4TzsPGeszrafMIM6jsB2J_wiBe8i1a7sjpvojpvxCUoRjpdWH4ED4McL81QrH6JaJnqV1KkWFIVRoHirAKiuc9Y88qIhnr7i_PZFy9lGFAFPEj8wwj_9_FaqyblLFKi9xM56QuQbC4OVAsJZvJj_W3uhQRg9cPdfElcsTmVD-N8-RfwJvmRCaXQj71tIpMC5kRIF8rZu3axwbrNcizgTu6WgNtVFuzyUn7qB5NPa-pEFFrqsCRKu5xXudGSjQtzWA1IPZn5M9Crx5IIUSsGDz9wyyE1f-TDda_12Guo2ujrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مبین دهقان هافبک میانی الوحده امارات از وضعیتش در این تیم رضایت ندارد و به‌دنبال بازگشت به لیگ برتره. دهقان فصل گذشته قبل از عقد قرارداد با الوحده در آستانه پیوستن‌به تیم پرسپولیس قرار داشت اما عدم توافق مالی دوباشگاه‌مانع…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24355" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=cwxpe74IG7afhelsEtKTAXNqO1UzvtHXtdIri6CeJ4oB-a8iW6-yrYNy0ZCe89U61XoFgNjca2uAKSqsKOub5JfR8A4u2GynDsBAfs9yEq54MwPawueNvTE4Ba_bt8fLYY0pOQmb6UpkE-20G7OAV-x_4VKSclJ4BcZMgAtjXKcOX79tH8dVWggwSCYY6k93hrPSSnkBP7nezJdhf_mB5D5ZH305CrJRPK4FRf7LhAisoTLXYbV0XhLUHa53Pl20KBTSVF5VzAXOfS3wGP9QiX6PqHXmjM6r4yqVQcZKwrpwrhWu2NR6Ngbt5zGLwOHHGE4C72CsfSK6BZ-Iu4zMOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=cwxpe74IG7afhelsEtKTAXNqO1UzvtHXtdIri6CeJ4oB-a8iW6-yrYNy0ZCe89U61XoFgNjca2uAKSqsKOub5JfR8A4u2GynDsBAfs9yEq54MwPawueNvTE4Ba_bt8fLYY0pOQmb6UpkE-20G7OAV-x_4VKSclJ4BcZMgAtjXKcOX79tH8dVWggwSCYY6k93hrPSSnkBP7nezJdhf_mB5D5ZH305CrJRPK4FRf7LhAisoTLXYbV0XhLUHa53Pl20KBTSVF5VzAXOfS3wGP9QiX6PqHXmjM6r4yqVQcZKwrpwrhWu2NR6Ngbt5zGLwOHHGE4C72CsfSK6BZ-Iu4zMOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇸
ژوزه‌مورینیو:
من دوست دارم بازیکنای رئال مادرید درجام‌جهانی ببازن و برگردن به تمرینات تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24354" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇵🇹
🇵🇹
سوپرگل دیدنی نونو مندس ستاره تیم ملی پرتغال دربازی‌مقابل ازبکستان رو از نگاهی متفاوت ببینید؛ همشون فکر کردن که رونالدو میخواد بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24353" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24352">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HFVixNwE-im0mbX3A4fCLwQI8DGUvHK9Y_ZxP_Pn_juShNaMkZQynWgm_5_qlexZKNXSFJfNx1xuvsIur1N9_qlOzDRrPKJMB6y4q72O2lJNt7ln5P0aYFv7KA1SoCnuBz8fIjy2vxiU0b5k4xaSTkPB6Fqq4Om3rEPg4c2QbbE5SLSZa8ifTvKRCZa6s_Zvg8_1DD9i_pMQoGTcCR8gcdzNW49Fht_KPQ3PWm8el1a4XQHf5WXTO8fh-wCqZBY8DYWk2B3xPNLeJFDCUyz4ZxRU-6hz8OHDBYPCUsjyBiYs2yzsX1yltG4sTjZvJjd8ThpC5dhC1e6bGu11481dGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوق حسااااس
فرانسه
و
نروژ
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود به‌سایت‌فیلترشکن‌خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24352" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIuXlL90dLiwLBLKCz4pAMtc6tEX7B6anC0dM0JxSOi9zp5FF0Hk4aFHMRUzNtd7qC5nTgmqgly5W6hiZJHFUi-Kp6B3-9263WRY45AIRfiPjKtYDAbakuyFGaVNiklP-p1DgTwBeN0XHwoSpKMrYFmSoLFajcKwSC44VxBystIvmsdd5FBj2htGO7bJzk2O8T33OqgsRdkK9lWGd6fblVemCDi42d8PW4TPhF6pqDpx6LBm2AhBAxo-vBsZQGUpV3oi0gva_m3WQbESX1e5S-6U-_mv76UY9kDdSSQoOxPu36anIlBjj-EYc-9t6tMTXW_wdIFFN1zlClcg_SlcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24351" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkO27mitCzqnQWUZx3avSOTS41KjPa8vuzJs4n-eK3t2AwJpHQwhGdOyq_ISO6jb0SVJobTNIBFi64M4NKaFXswABLjowlZN_ylQpaaRROWRJ0JYyGdbIJBI8vMJmqDXn6dxdq9vEtSFMiuh_9CfkP7JVwalL-Tei0g4PnfHyQF1S_4hvUIP2svQgTJaCvG2OfNyrFglQITorrad9s7yKYciei3BjCHy9HrOLl-rCAwffbCae1idSzoALihyF0wmgcdoKtige0CGbpbS6euoOL9QWlDJtety6pjodk8KyR7Anr7_1ZULtrumCf4kj_r0Gisb9VKk9fhyhnZfmuZIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ برزیل در مرحله بعدی به ژاپن خورد. هلند به مراکش.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/24350" target="_blank">📅 09:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=XAMFHIYl8YspGSDwQo-nY-35iOH7hN2RlgejsdqWI7CZ7yW4pO7VIVlxAbI7e5GUDlLcmZbr9Fs0UaiI7aTCuPQXgDZb_G2UgreWMi6asX23FkwdncF0sLtCsU7liC9mKqrsIdxFZmZCLaoSDkEngIv6GSoxl1odole-FkHgkutG30LzmxE65m-V1pSEeIeWf_Q7kPHKdZVlwWadTJdWo0FUaDs6J7X68Uzm_JktbpKL_1Y0znH9CZ06eqhOsRg6YPd1m8udEUHGQbjzoq1KBSYFCOLf7LmJ26n8Ia4Cl-Pve_FKbJMvQh2FupkFbppKR2f8hWgOJ95_RogZRCyDvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=XAMFHIYl8YspGSDwQo-nY-35iOH7hN2RlgejsdqWI7CZ7yW4pO7VIVlxAbI7e5GUDlLcmZbr9Fs0UaiI7aTCuPQXgDZb_G2UgreWMi6asX23FkwdncF0sLtCsU7liC9mKqrsIdxFZmZCLaoSDkEngIv6GSoxl1odole-FkHgkutG30LzmxE65m-V1pSEeIeWf_Q7kPHKdZVlwWadTJdWo0FUaDs6J7X68Uzm_JktbpKL_1Y0znH9CZ06eqhOsRg6YPd1m8udEUHGQbjzoq1KBSYFCOLf7LmJ26n8Ia4Cl-Pve_FKbJMvQh2FupkFbppKR2f8hWgOJ95_RogZRCyDvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/24349" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTHPvqqaQEzkpU_5XCTH--6VmCe1G-nYZN-hAqCMarG18lfjK8g7xJWWyc8QMPJ213z8GvADDnxPhh5UBlAeRHBe1DZlmP8oe-COx2Qpo4yhOIFMHabYEXsAaxVthRF4UoHVpFbn3RY-6RzCNAUbF1uBK-_JTSSmvzezk7rTV1td4c9xU0orqcBGHm4QY68qhI7Gs17osavhvFyXYNl034dYTYHBHHJYcK4lMrQw4eX4-8aLXY5EAaDooTUsm2Ht-2sYLhKxIQPUWv5osG1j4Emu0UjnHxH8a7dfyt7MPwqpnygLhz_KV3Wl3LhmTzGchF8KmEaYWuNXeMiQdii9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ ۱۲ سال پیش در چنین روزی؛
آخرین حضور جانلوئیجی بوفون درجام‌جهانی؛ آتزوری فقط یک تساوی میخواست، اما ضربهٔ سر گودین در دقیقهٔ ۸۱ همه چیز را تمام کرد. کسی‌آن لحظه نمیدانست آن اشک‌ها اشک وداع همیشگی‌بابزرگترین‌صحنهٔ فوتباله. پنج جام جهانی، یک قهرمانی، و یک خداحافظی تلخ که هنوز از یاد نرفته. پایان یک اسطوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/24348" target="_blank">📅 08:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbEUg5P7EsUEQAiO7RuFEwc6K6dbF6zacQ__dqkdqaXigBOS_7Xtnvc6f2OoCG_0E_6FRboh0NffMKIMor-GserA441UkkE9JKVi3JHBcCf1WpV5KmDJnJ7mB_381BDn_Xt8qLHn8Xo4B4ybTqn1RwoPxtGRw-HJfwkyp58nrqr28enYX-CJLq7enrNIKE6CTMeOioXaebVxI8RIcffK87ZYztLAPhjAxVJis_AbHjaGX7xWpgy3_v72sazgjZUEx3M_fmLtmK1KpOLjvAOQyIj29GJ56THCu6g-Fv05eHecRNN-89u3rAUX6ppluYXE8W9CEhWnH5_fMkwaEApOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F و D رقابت‌های جام جهانی در پایان مرحله‌گروهی؛ترکیه‌بادرخشش آردا گولر سه بر دو آمریکا روشکست‌داد؛ پاراگوئه با استرالیا بدون گل شد؛ هلند سه بر یک از سد تونس گذشت. ژاپن هم با سوئد مساوی کرد ولی جفتشون رفتن بالا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24345" target="_blank">📅 08:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCOuIosf9jTanOAaDHXR4yq7T0twHMa58BHW5jpg4HAABsN8FCJZA14P0PgME5HSgSjpYiOq0caLLnXmRYKy8eQ9KNj4LYFACyiweB0XaBubw5F4xKNl6TlYYw-YpTGsQJPUuBJqGAoWTnXi5RiCBokvQT_RQCuEToXm8fL5qsoxoKTqYNMoHT15XqKK77fkhW0BDQ6ZB4k_HC8itpVd1-hcwgeo4ep6falLLmGzF6xgNBD9dmpdCVgdNZuM59JG7s_CqpzzqnVLRBV-u-4neBZIaDUoV3pAPQqxn8KTcKG_4MMW5xa7m1W3Z-TI9Kol8X8J1QsunCMDb1kUkkteDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛ از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24344" target="_blank">📅 08:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzqIUyoHgiGrkopBxXYB3SVApdySNzk2cUF9XBNErfFMDwYMaRNs3zb4qlJMcKoQ5UkJO_UeyNppkqOt44F0qRgMNOmLTJ_2NzaNSCLeFhSnOuUxShPJEjZjL7YtlOtWZsGzrIUhh_44HBmeq1judDs1-7Qft_iBmM8CQt8pHh9FuLOvoqOYp5F3sBH-FOOvB8DEZxzoJUCYCe_lEHTokl7aluymQBO_iMiU_7BsxQgvgbVgWWoThsU3qvVb-g8whu4b7KzmEsv6GGGPslSqfRK4eItSOW_wNlcRN05FCU2HBQDrjPP2SpYfTBRxJGQSMW1JoUnHWX7fWWerOpVDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24343" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYzVpFjnivj-kyQN0mGZhaQosk6uYPcB_HB-1c1kRNE4VRpGwZ8yOu1LUeuEXUUHswVoTvOe-IX6vY2Q8BiYvPpLJbPn5R4BGLTyOO2P39YKCJOyGGXdhBJw-i4CfULQJKZLycgC0-qMPMe1rkq3VJphAh0_kzVCcoE5LFCpd0IH3SIESoLyfmzbUT-cWIWIfr7k-koRJayNAfH4jjQOzmljVh6ejHMRtIVRcJZJh40L2yorz0gsc-5AiFizrTtHYO7U6rRbl1fHL6w4ATquOLfjEC7WVO6rboh1AnxB6HqnNRAp98quSUP57mwQSgBvbS_U4W6M30IRkyqvErXM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛
از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24341" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24340">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRgMwEUxYBSFfVY402tvp7tUgdfyMI5qiMP_AzAIG3u8AO0w_YNdUOjgZLGM1q9CK13CUf43B32r_uT-wy3ws1-RgoXNLryuL8G-Iv68teXq_QmrbzIm5p3qvtPHSIWCmhriTOhFjqNANZsILFZMuN6vhsKXa8CNdKtiL-3FohlPXWg66hUpc3RBKpHhZuPWvLSHq-pgwnrE9gbZpmK9NRu6f-ujjuj4e1wW8cV_T660Qc-RO69sU-e21NbsUClQJsGaS1gi7Smn_yWM35BZ5jiMktto-6UfB_U4l2XhaYwt0zx_rXSU5llxEfs_LV1T1KaGArpwujnK3foNszvbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌ دیروز؛
از نمایش خوب شاگردان آنجلوتی بادرخشش‌وینی تا برد دراماتیک اکوادوری‌ها مقابل مانشافت و جواز حضور در مرحله حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24340" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24337">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24337" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edRwBUnrb59i9Et7pXImwkNoY7bM3afO-n8hzWI9Uv5XFbcgrKU-s1NmmsPN0JiVFPDkQcphbP4uSch0XdwucdrsxzCUnjBvxU9YGiZRbQaEgL-gVKvgXej0GLhpB8DaGd-Tjb7wbAjbyBRrvdnGZjPu1O2wxtGvz4FKXoQIRQ3GTHgZyUq_wnY54-4qnciSDvutkPVGVmqDjt5cjGr1lxeVXOhD_55l_AQpsXayQGIRvun-BudGuZQ2NsMOyeyD8hKY7k0-ownrYDs2QGLTxnNq97GeoRJ09rpHnPsYlBPZ-qNsJBLQMRiLQZX5FFfSSD_aB4fXCekn-fpnnECwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24336" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJhsG-QpBXDpj5xPP8uNVn-C1PVNJTVGvPBSUOAz0VIPoI6VbQeB8qbYDS_vnAVzGF4suRQwUFk5R7Qp1qmKfOxG9j9MJc46Vo6_VoRQ0kFBzQIEZrg3j5GFMA28dgK4iCJm2zzowItJLtBaZXfHqcUZqya64YJ-remQqxhn84mnmEYIdhTIwpMPE4aU8uG7dn4XT3YMGSsV8p2PmBhDJAzq53lCTJE6_OpPDS5sAdI4pS4-nxFa7D9gjmTgthXtp1pxpcU1hJyXKZ2kfkRbxnPF2L9dKXpZnAe5pfXDomz9REOCgsDLyPEmfNFnQPQrEKZ8TF7CO0xMOuvxxgjH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24335" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=e07V_Lb70uwZU1ItgT5GUfgpLhW8rJEbVf5KM4UuwvrWjB0TNqVo4G26G_biKvJvFiLQpLJcbZamAE03X2JpS6vnQ5GEW-sicRRYlWNEaOpVSnswLoqyIUbrUqnU-4_CO8wHG3Hx3hdIjri0q_2S969CfL10CiICIBSzCg_11SIdgpbgbyrdNjVpsts0LMufPmHSJs1DUyucJTCmaYLQsqtX04wp8F68PaLUSuozUMAEOm4UlPMO_nT4FJX9ye5XEx20nlDwvG-lR4QKylAJjQ3BqvkjCIxdUaET6Uyu5SPRjijG_hncsl7nDdQJhVEd9Qe4LsAxlpRsJDcfcqhiPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=e07V_Lb70uwZU1ItgT5GUfgpLhW8rJEbVf5KM4UuwvrWjB0TNqVo4G26G_biKvJvFiLQpLJcbZamAE03X2JpS6vnQ5GEW-sicRRYlWNEaOpVSnswLoqyIUbrUqnU-4_CO8wHG3Hx3hdIjri0q_2S969CfL10CiICIBSzCg_11SIdgpbgbyrdNjVpsts0LMufPmHSJs1DUyucJTCmaYLQsqtX04wp8F68PaLUSuozUMAEOm4UlPMO_nT4FJX9ye5XEx20nlDwvG-lR4QKylAJjQ3BqvkjCIxdUaET6Uyu5SPRjijG_hncsl7nDdQJhVEd9Qe4LsAxlpRsJDcfcqhiPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هوادار تیم ملی عراق که تو صفحه‌اش گفته دوتا از بازیکنان جوان اسپانیا بهش‌پیشنهاد رابطه داده‌اند‌. اسمشون رو نگفته ولی گفته جفتشون تو بارساست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24334" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24333">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3KX-c_0WBLbYOIaXQcU-6YtoIP2N-2A_TO-14EUa-y2xk7-G9nMX-g002krofuL0wctCyq8UNB3Ig3U7cu4xkblSmrKrHOzh6Xa20HUMo89le4VzAGOPzOdp4BStyZ4LjzbuzEL7c5yYscZcNPUvud1Xotou-uj9xkxEsTpKfH-7wSAqr9qxIA9wUsSU0DnCpw9Z2CTEuKaTfRVjLnPEZww3fWOleEKwzDFJ_qGwEvkXDKkE4ueZ465cD3eAobgZwCcI5dVQz-hwhKsbdQDS_rwD8iZuOOoP6nzRpyOu_A2S66H2ZJ0pbRlRFtz8dSvLPDmDJhYsWDsk-UzEgz_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
میخوای از مسابقات جام جهانی پول دربیاری
؟
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش‌بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون4:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/24333" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFWG9fqbF9H03lsb-UoCOpW-CfkuBOt_-spxv4kyJYPAVh6U7sunwmWtPkcv_ddeyJudgqlE8qIS5KiHO_ZSUooS4dbzGsOGL9IHW5Lf2QnRcw5U3J7ZsB5gT_CrMraJMklDqesh9DkN9KisZoSjcr8JqA90ZJhl3LG11k2zGUNPhnjGd_X8CGxuduCiyRLbrVEYQ1J4a1Hz3UHyd_S5MRstCtaSr0fA0dkOdrr2gvkBFnz0jNq3UIgF_kl6WnIYP-HrDbwx5AHsd3xhmByv7mOzn-AImhG4-Ity9a184Omqrq3Edv06S0WSXsgGK90qDW71-uG1d_WErnVA3wnXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/24332" target="_blank">📅 00:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6CBuK3cK43lwvm_qbdkxEbF0sbg-GrixjlC1nAGA8zdxEqSh9XRHz1c1CMxacrGyQfEJd9seMMnHUb6A2jaeAH4-WKrGFXSMZOWFJEhwOVOto9-XR1oK9uUCl7TuewAg5cJovZ4lY5XuY7XF8sXLRSJFQlIV8qhealf9gSBy1T8ZaWZMuQpYXuwiY7KCm9nEEb0tiqXrCWdyj2vXPsDEJNJOd-BSiKGVN3cpdCG8VluQsalQApBE0a5syFpC0eMCLBMuXtEiVEJd7T1VvFDj5VGgOj7cAUCw_qQsfVa8t5J136JiKnhVNOusrgVIWrkrS7ClorsxKdfVturmqEJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24331" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU4gfAY_0Iaa5O-jKCQQf07rKXiY0PBtO06p3Y4JOOyWP4AW__I8XG8cWCOK58_O1Rm-Wqm7QmWhc9PerUn-8A2ms4XJgxfIiwnXm_e_MY660Of1psmXmgi9e-H6zpHMpbTzC2uTVupQHPXpsnoz53doQVwqrr3kIsCS5qbpPykcv5PgAx57FfTGXHcY_d75qTYzWLoSFjIUtA_TpeMhFp6T6n5VSt2DvuMa6l_kXKB9GFtncNoKGYAnUO3s8XHnLbYtGluDT7MeDg5VyJa-8FY9HrHIa39SnWSci8M_uREHfLmwUCykRd0Ni3PWj6oHH0bg_seTCXcfZ4a6gvKW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24330" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL2ni4C0e9p-inf_x5YogIlGHgOeLymVQaXCwAGa4bQAUnylhpUcLqSY6h0_Mk5Yv-q_7adJ9tkWMKTjCYUcq1AYUj7-QP5CPDY71uh5bb8f1eiPwQ0PPZtp6MVIRUfU0DnVRBkVtmS4SFV4F75grmcReqzVOIEbF1DMmcp-YKKHVqfPDorlnb_jEj9uTleUFACd_f9tV68H3x7DCyHUDDRI1qe1c3-8XQ03xWL8ndQDvDYP2xfRnIztpc_7Zc4nTxuczTtl6m5TxMwofnyMcbS0IU9EZh_RbC0JmUv70Y48ONtYA4P1HRTi5z83eDzM3Nssl4fTXGyvNVg7V0m2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط ۱۲ تیم‌از ۴۸ تیم‌حاضر درجام جهانی بازیکن سیاهپوست‌توترکیبشون‌ندارند‌.حضور فرانسه بعنوان تیم اروپایی با ۲۰ بازیکن سیاهپوست از نکات جالبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24329" target="_blank">📅 00:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=ZppTNQWpU_rrDNzfDGpEU0w5P41zFx5TljhzWPKLo57vp6LLPWhO7bEreDYzNIWruqFNvwxD6jzYBJjUGPmkMkvXUEY-8VKgEk_37dVlBoihNQDRcQ4Y5t98hvCQ48zgJutpyXlQWgGL7qepgNw0AmrlHVNiJj9d66usy4g90qcN_Y42H74Z6SPZL7x5_Uk9QE5JYYt3pF1Gyhbjqa3iqU_bIvnxOHnUE-3djvNVVgywTR_1XRT7C4TuNECTV9t4HNLWvVUByzbtuTd98Eapla0YL-3m--2IjQL96fk4oldw7M0udXHr5lQzKTOzufz4fUIENQ5Vt4GRIdVeisF0bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=ZppTNQWpU_rrDNzfDGpEU0w5P41zFx5TljhzWPKLo57vp6LLPWhO7bEreDYzNIWruqFNvwxD6jzYBJjUGPmkMkvXUEY-8VKgEk_37dVlBoihNQDRcQ4Y5t98hvCQ48zgJutpyXlQWgGL7qepgNw0AmrlHVNiJj9d66usy4g90qcN_Y42H74Z6SPZL7x5_Uk9QE5JYYt3pF1Gyhbjqa3iqU_bIvnxOHnUE-3djvNVVgywTR_1XRT7C4TuNECTV9t4HNLWvVUByzbtuTd98Eapla0YL-3m--2IjQL96fk4oldw7M0udXHr5lQzKTOzufz4fUIENQ5Vt4GRIdVeisF0bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24327" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nirRB2SucPfoCDALgPW0boyieDvsBTRiCCuu97qsxoc1YOfpWxQ4SdtmHdEIaBKEdTGaXEhOKSBzwRLOt7fFO686hClLAyJ64R1R1Y7_JUMwoj1Sx4vUKOrcPtuIl6hEWwIZKsRsCPYNnyamYzQSBFRMvrpI3BZgjhT6L1lOr0paE-p3d5hGBFF_kQ6mZu2JkBDLWdE_s4VtL-S_N_9Xziq03tZhV70JiJ89W77vbYDnzkv6ihGbeeGETzbheQDSn3u2auMleZ4QulQzfop3mqPm7RIwIqZNpOhg4oLT2hqRbV7PRHoefpxCHzebg1lTFzXTZMNt7Kbst3AwAieTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24326" target="_blank">📅 23:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24325">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR0WiekFz4jdqsXUCt3VDZk3E0FQj5nniBN3fsMqdm1oUiHci3KOw9v7qZrf5cbRzzjAaopvPSQ_vpjuBVjfEl-RzEWYNCfJSoSldtXnRYPY9tta4atlalcRA9kr2JY_UKsNZaaprCUhEtK0t0-ol1F2lsP8SHhV5IUPcNSCVthPQJylEY_WpRRzAVL621TdvK47r6pVGOlITvpn6WlUHdG4wU9uRQ8oW_5Wdf0YrWasbMW45wwX7mPmxCTvkfbeb51c3PVv1-ChicwMHik_CsUmdqD7RWa8C0LNH9mnhODurEk8J0hPcITSndhxe-W-2X7QHpFqiACld0vF8HKfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دوست‌دختر ژائو نوس ستاره تیم ملی پرتغال هم امشب از نزدیکی شاهد درخشش CR7 بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24325" target="_blank">📅 23:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24324">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
🇧🇷
خوشحالی‌منشوری و برگ‌ریزن هواداران تیم ملی برزیل حین گلزنی وینیسیوس در بازی دیشب.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24324" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24323">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8l2ySwHLQk4diIzrQCq_dLoeBnaScaVGbXTWKMLVR_GqXayBmqYYDUfI4Y5YlbVm1soLjqvCU1s53drO7niunwf8-0IDpSHViVPtooISvTOs-Xb6YzVvjfc6t3Itt-sGuS_a7n08uMqNNr54Kxe4ruSNRXXQuutbSXyl5neUMeQDUUE1lePXaRixDZ6BUTRDrD05Fwo4kWILcuH6hm1hrbxmPmPlcrvSAvhxJQG0pujZ-1HosU78bMqR_ZDTdbUBIoULrI0ihDNKo30hhWq_YHYgc60QxmgHwsZWbp4aowQ7TA4inv8Asmbkbwr4ExbIJtUkSnzXf0wMnNOD5bw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24323" target="_blank">📅 23:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24322">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-kuFEOxe7QQl2ZOlm2XnJlGd7jAPiLMP_6EKX6QjBT1sZAgCQoVFk9UyXaprrskVHnd-1GEPNQhWFeFXjLP3iLR519LKGnat5NDdGR7jaMpIsT5UWVh-RLcw52Q0Brp1oCQbU0HAACCW2pmUHl68lDZOWG_94rttqYP9q5tzLvWCPnr-7SDbzShpONFAUVD9y-cFiPLR_Q_dK12fqL_DXqMyzW2cKZwtnH-QWSgsCAfefaAnzToMLSEA7edRyuNGmDsRpGVyFdkU1V996CnIcAdiXj1_vc5L5JBy8zti0clQ4J4J0DifqcqaVsh9Xw4XuZQLCfC8otgjq6MCBkucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو: باشگاه رئال مادرید بند باز خرید یازده میلیون یورویی نیکو پاز رو فعال کرده و این بازیکن رسما به باشگاه رئال مادرید برگشته. حالا فلورنتینو پرز میخواد این بازیکن رو با رقمی بین 60 الی 80 میلیون یورو به تیم‌های انگلیسی بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24322" target="_blank">📅 23:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24321">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=M6C2qDtfM5yXXMApyzR3TPnMV9BcXBLSl7SCedYsecwPRUEDnUrWq_y16RwBusW3JMPyxlNfkDoLEuj6GUVdQjS7TwOzb2WZUup_0VxT8TUthDNAHrCvseLsXLkD-fIVSsNgYRfoScnj6ml8mJqbKOLPgoqP2zuw2k8Bdpzn4pfhJ8jvW_kVB6cOYC94um8l0VRrGO-nvBXMbQ5Pd8yMqkFfsGM2mGnF9Z3C_CeMUnYWx7EzHyHek80lwGswWOx5-omzOF5APkDR3fEgNSs3vKBBCdrJVfuchDa7XWwc4XPypwxoxp7QnuowJO0dpf5gCIWXjZKpleqO267-Zjs9xKgfC4ViHmD4R3CjxtbkSmXjJzoDOvsQvpc0d-eu8GyKQMLGzpodlx_FZ_Y3L0JMAHn3sLrCo2f-r9oRHMyuBsn0sELSyQvHh5-GhznuRNyMFCtL_i8KSA9Nkzc8GqdumibJy0TVB0qQt8T1qOZFG5rgrHPYlNwAQWZd0Df6Wget2gJCz2r5c1ixJXFxLZxwHc4N7fQGFXh6Ohuq9pnFRIBSebwfRposunbE9Iy8UobtGekOmrpvo8wqblupk7t89fBTu4pk_pwmaa1fbMyi5dBzZFP_trX8tBG_OWq0YmCpUTOwSam-xgUJf7AYkQWnjqfNg3WKZDtSew8aGRuAB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=M6C2qDtfM5yXXMApyzR3TPnMV9BcXBLSl7SCedYsecwPRUEDnUrWq_y16RwBusW3JMPyxlNfkDoLEuj6GUVdQjS7TwOzb2WZUup_0VxT8TUthDNAHrCvseLsXLkD-fIVSsNgYRfoScnj6ml8mJqbKOLPgoqP2zuw2k8Bdpzn4pfhJ8jvW_kVB6cOYC94um8l0VRrGO-nvBXMbQ5Pd8yMqkFfsGM2mGnF9Z3C_CeMUnYWx7EzHyHek80lwGswWOx5-omzOF5APkDR3fEgNSs3vKBBCdrJVfuchDa7XWwc4XPypwxoxp7QnuowJO0dpf5gCIWXjZKpleqO267-Zjs9xKgfC4ViHmD4R3CjxtbkSmXjJzoDOvsQvpc0d-eu8GyKQMLGzpodlx_FZ_Y3L0JMAHn3sLrCo2f-r9oRHMyuBsn0sELSyQvHh5-GhznuRNyMFCtL_i8KSA9Nkzc8GqdumibJy0TVB0qQt8T1qOZFG5rgrHPYlNwAQWZd0Df6Wget2gJCz2r5c1ixJXFxLZxwHc4N7fQGFXh6Ohuq9pnFRIBSebwfRposunbE9Iy8UobtGekOmrpvo8wqblupk7t89fBTu4pk_pwmaa1fbMyi5dBzZFP_trX8tBG_OWq0YmCpUTOwSam-xgUJf7AYkQWnjqfNg3WKZDtSew8aGRuAB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مرتضی‌تبریزی‌مهاجم‌سابق‌استقلال
: گُل نمیزدم چون یک‌گلر مشهور برایم طلسم و جادو گرفته بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24321" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24320">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=S8Bgck5tQQ8rN0UyJouQ_stP6H0aUx9bSZ6Rw10xREmuK6ZjZ-mx28U-3OZs8KgTmIPxpPwVwpRE1cyUFeju7vaca6jMezteycl9hovK7oEbFKqFOLgW-V2HlslyKbw8WxPqu-XVhSVSKhHwQ5Go7qAqexacjYLZDsuo1siNGYvAWkDc8NShccbuh_Tf-kQ-KbbW6ecXd572II44hKtyjip8H6e9Vu9W4TAlZ9JrRGWVIBJ5QVtURIt91fxW_wP0mnT9WqXV5EuQULfwkSSfH91ZeryKN86MJeQJEXcqJWMIoXpyvQ8gsw3GoE9aRa9hIPpgKijG_2zLOYCMON0gEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=S8Bgck5tQQ8rN0UyJouQ_stP6H0aUx9bSZ6Rw10xREmuK6ZjZ-mx28U-3OZs8KgTmIPxpPwVwpRE1cyUFeju7vaca6jMezteycl9hovK7oEbFKqFOLgW-V2HlslyKbw8WxPqu-XVhSVSKhHwQ5Go7qAqexacjYLZDsuo1siNGYvAWkDc8NShccbuh_Tf-kQ-KbbW6ecXd572II44hKtyjip8H6e9Vu9W4TAlZ9JrRGWVIBJ5QVtURIt91fxW_wP0mnT9WqXV5EuQULfwkSSfH91ZeryKN86MJeQJEXcqJWMIoXpyvQ8gsw3GoE9aRa9hIPpgKijG_2zLOYCMON0gEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
صحبت‌های‌نیمارجونیور ستاره‌برزیلی‌سابق بارسا درباره لئو مسی فوق ستاره آرژانتین در روز تولدش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24320" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24319">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPXqPtarPI_5FQaXJb_NbNp_ZYDvMzJogUh5GVmCHMhyw9_sZt3qSU0A_Ywity9aOeCPSPhvAfuYNX4ry6mPkPK_x05MsYZ7GVRBCvWV6ZJ65hh5oNl2Xii8Bb6dlWittZMEvSVVhd8pUHs56a_no1gfgDMybz8tZ4umEEdMVdelu9ja9I7OAVYfylWmoi9szqKOehtbUkWwtM-AtIkV6I3DrW_qU06aow18lOnjOn_8BGeMeikkm5s2TQjwJwojNSDR1I2Lbv6X6DBk4ZVo1DTJpi5i8AJHbEeR5jS3m7ulTfSOmnKIYLSjk-tjHAVHXrJQNTUt7eDnZJp6aL4Dew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24319" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24318">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNLaXijyoNSyoEfmSp9XwBjWnkDzRVJVb13BBYX0hg5P8rnAE9tUiuE9ktT39AGBv1GuobbW85UH7gjZXy75nZE9lb7NLKJl61FtKreEtKwy_z6yD-Q4DTZtZ-rnSQXWeq3IAQnxymYgr2jYc2q46uOT9K5MoEIuphqspK28FmEMRfDgFhh0RZPSngN-cQbFd5NlWv6r_g8c966ZjUT3h4wrCXM4CNdQ11mL56lFAcyCe1dUdQghCUSnCVSLvPMaq3bR4P5lZonTRWa0D_Rv2CpMH4FfSckuWB1IMDkuz5YHk7szNSC4DITmcdbjBu7UZHzaHCyYoRtOEOq1Yei3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24318" target="_blank">📅 22:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24317">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETK_WQIaaZmGaC-YHMvsYf7IJuWrMMQ0NONcwynL3Swb-ZMkU6MThYHJcgn6eh-DUx126bw4f95ftsRKFDAFFodAxC_k9MQRyB7oXD2SIz3J9EEvRNtaJVr0EP-S17BhY5QPwXSc2ZJgwBLByoSS7HjIENIpBuPtVtDkLcNSWFeoBLtF8bcmHt0FoJ3A07Phofu0i-NqSwa10eaQb8kmNq-TFtj5otU2EePRVbRArC3xbQllacy-g8e0DrOihptJosVm_Kv3g-bmUYgcvL-s2-u3QoNHLYivr-hr6q27lOqW2so9v5lbLg_yixn7M53BGwZnkcJYryNa87xYF6DYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24317" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24316">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=VhcSIeJO1ubB3Ih5axSRl9725rJ2Nks7kQqQmEi1lYyrAV02AUWgF2eM3bhY5rxmyw1pQaajLxg7bC9TfYcvaoNOO7NESQYBdz9PfgkWhsBtCqbxWd4cBJzadTt3ECI8-wXrqVwDWzZaFSfCBxDOeys1qCUTjvkhb3IDGfDyVCCqsX6Rc70nssoQviqACLazxvwZaWcuAccRiVjOfqDgMyDgiK5I1YoKVg101uVc0RqHyW8-XLieHWl_lfkYNNUaOtbzqyGrbAixMgN1TYptUZt3QcsYzDT2r54SV4egXyQb0DRgMUdOZI--PsVYCvbvWAkoLxJghO-Zb8TZXs-cGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=VhcSIeJO1ubB3Ih5axSRl9725rJ2Nks7kQqQmEi1lYyrAV02AUWgF2eM3bhY5rxmyw1pQaajLxg7bC9TfYcvaoNOO7NESQYBdz9PfgkWhsBtCqbxWd4cBJzadTt3ECI8-wXrqVwDWzZaFSfCBxDOeys1qCUTjvkhb3IDGfDyVCCqsX6Rc70nssoQviqACLazxvwZaWcuAccRiVjOfqDgMyDgiK5I1YoKVg101uVc0RqHyW8-XLieHWl_lfkYNNUaOtbzqyGrbAixMgN1TYptUZt3QcsYzDT2r54SV4egXyQb0DRgMUdOZI--PsVYCvbvWAkoLxJghO-Zb8TZXs-cGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌مرتضی‌تبریزی‌از زمان حضور فیروزکریمی در ذوب آهن: 3 روز مونده‌بود به پایان لیگ گفت تیم از نظرفنی‌اوکیه مارو برد ویلا یکی‌از دوستاش تو کرج باباکرم میذاشت کباب‌بازی‌میکردیم عشق‌وحال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24316" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24315">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eegKCKisPR9cEQ0cqozTV3q0V8P4I0cywt2vcjyi8XURjs_rrUi7VtYwVNDV8IznAkk1A-C5PDExuFoa_pM-4lHLlzoAJ9C_290TVbZtwSl2rrKRdmUtinFM8DJhct97K0iL-CVAkfTYQO-uU6yjInfMJkHToEUfJPXUQat2j2BRQeTIKYsEdclZnNd1gOjyKWvoXrs97XVKIsyMGESvvvcW1YErC_iGgh8WiTc2pfHI548m_38_VIR0YNXYduibm28K3JNDKAPEjFU8jPQVqd-KCgO3BKNW_Jt_ici1BrcLNQpRibzsG5P4WV8zBwI6G8JxUatVxcNedbcT8kdn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24315" target="_blank">📅 22:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24314">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpVWLebVihNR9K77JY_av4-wRuQTTo7KAx91bZIt5lHt8dY5J9z7Sq2l-kcwxvQDb4DeYjyW6GvVtWjuteJHBIOdxBx4HimkNKGmPeCcb-16I-tDfRQQYjOYpWuF_tYzf4_sI8ijxBwlUTEBv-7Xqixpo3kSOhQKZiK2Hmktwx52_CAU5oZG_cmja4aML8aMUSJM7jJhcR1QsFFmBBbGSsQz11RKm3X3MP6K9_a8VcutlZtgJPo9j7PXS1PPcBFaFtMQkkwK1Krfkmi9gnoqsUlFM4HmQANMTwSmof3W6dFN4iXfi75zjf6G9aMXNSxNzqwr5T0CaP3kCQJOdEl8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
عملکرد خیره کننده اشرف حکیمی و وینیسیوس جونیور دو ستاره مراکش و برزیل در تمام دوران حرفه‌ایشون؛ رئال مادرید چقدر مفت حکیمی رو در اوج جوانی از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24314" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24313">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvsnMv3vt4V0sOVR4Nr9raHMAU6qWv34dzBclTt68sX_Jbz70vwnsKJVXY9nDN8NTwuUV0Lu32kHeZaCIplUyC5z0rhnI4bItKEEUgc9r_3mkSFW5SJyp15SNgfn2t1I2UQ_F0BhiB0pvR5tpJn5ezoeyruCJS_FEEh0Dwo9QH-ap7OCttptwtL3416KBse2iKGxN4ia_3nWsQRnq6VxvQfT6h_5ZgFWc4gVK7r06zTyqeaq3UbCtzkGrBOrWmioISdbl3_MVJbik6ZAB0pUPRBRAR-2xsWrX1xzwkzBJCEgIWfjWD_DUdSkIzELeoRTYueP44VPK8jUO05UPCnUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24313" target="_blank">📅 21:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpi2wj3hQy4a1-8bHosTb0WESfuAt7ttdpNTjiSP2hdNxVO1KJrweoZdFESvvjmfIPAuZpHD4CYC6tHd4CusaOZQt2nlxlYAOtLarqF7QVhFfiAX_7jNXGJilHOSmorNNzDxoO_Hi1A7QMxpY7sR7uE1eHG8Irpm8YNlNOMqnCrAX-R_5qqmRr3s6fzELqBhtB33Ee7YD0srkr163igbVobehCqYGauagTdHhKlB8jdeMJlMrieO9bALnKdN0sA6X6-J_ZAzSRhSf3iG7JF44fIwZa2B6NWWYkNTC91GZCJD2sIPsJwL-ZyMlRPu5qVOriBiSLEcJsTC9giWoyh6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24312" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmyOoFANsiTVZjgBInoOoMGwUtF-6lxQW8_HORejoxJ2aoHpIuDKHj9Q_ZZxk3GJSX2c8RladVyvmAjBrcUyiLRTY6x3ZmOc3A7zGpqSh5qYorubvQR1xl2kkMpFXHAzKgqC8_qVc_AB6ccMgtRxVb1Zz43xcPMBpLOW5Nj5Q0N_Er2VVhIuM_LJMx81ojV5RKm0AbM8B71QuKW_a0SY8O3fQYg-Uu_ol7oA2ArKq-LbGwTZjr05GqsMJa26o80QRLr0o3aDwvxv6fCxxLgnDPfrpHNQqVdfUCgVjkyKbrHAwV_dUyVKGppOGidMtlEmNrZ0HI_8dsx8_LbEMHO9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AET_kiXQx0WNOyqJWAd_5GVVWc8R9atSbGwM4slDFG-TVmk9Hz-KhDO4qMdg2neRYGrIYR-YHGFi29sfaVWNdsSyI10zege8hsMaC4UwlGdfi8f5HxUsatKT_iajIT70IgFTPKVQamrHCC6KqiR_5hc0G_dpCEJSWcwNqcPgkZkEjh1K2SjtwxTovEiRXtM0_yTN3TnXRgPAnwAD-s4xs8rXpPBqUq2sqb-29sWd7BTLyZuyKPcY8iu9wJQi7736fa7RTEAmV1ZpH6Ii89WXOB-GQA5G_MnBaNZ55KajBiWus8Pa-BBkNtH1zNH9Nh-olg9yrLPMablQQpVxutHNEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
🇧🇷
#تکمیلی؛ بازیکنیکه‌فقط برای کشورش خوب باشه ولی‌برای‌باشگاهش نه رو دیده بودیم. بازیکنی‌که فقط برای باشگاهش‌خوب باشه ولی برای کشورش نه رو هم‌دیده‌بودیم. ولی بازیکنی که فقط برای یه مربی خوب بوده باشه و زیر دست بقیه زاییده باشه ندیده بودیم که وینیسیوس جونیور…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24310" target="_blank">📅 21:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbsQKJuTLqC8CnnVZw4Be23Hs1iNzLHgDiTQFNR16yEpGgdztixOXJ7B6V9uf7yXCyZsdTZgeL5Frmp2ay8CwpkItWLxqU-6H9cc47Ky-hW3FYi3HMVjw1vKU--DTTkBBjEikZZQITf4kMySbRLQ3RQ0vh6nQbu5G0vQYRfhHEvAtMfIumLiGCrBuEFEdtsiluVwUEEQKa-JKptlXqePOgz7k4GETCscSAEJRUMVMmwveEIvZA_7t7DgmOL6D0JY5jgarOit_Va9KBjM-fwQ-ZRYMZl71BxkqQGasfRBqXHwapb8X2qIQFLBogyr92PI0DqcKJ75tZOQAozhA4zD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کواکو بونسام جادوگرغنایی: حالاهری‌کین کاملا آزاده که گل بزنه، من اصلا دشمن هری کین نیستم، خودم بزودی بچه‌دارمیشم و اسمشو کین میزارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24309" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI8MD9rEnQ_cv6QVTFA38_wfZQ-F8yYQXTa8E_8Ip7PzqT6MEjrfjcNOD7pFE1TU4S6yCAkCpTpZIwqhLu0SmAEAy7iZLS3H_Y-ez4Bfx1kL-4hNmjkaHfOh87n93zcgWw09Ft8dahXTzaTnL5Z6aCYOZ509r_KkEGw2B8KnMow3wQcguvdiijgS956F7DN6QSXvcbDx0NnUudq4vwB1TeuOWy67qsiPiBNIbp8aHOWAUi3dOorj5swnKTUJTsyKY8V0yhrNYnw6fwxbRTzIOSWkewUKDZYj5l8rZKLwaj_XobfuE7emF00cxwcPH2Wv1jkrar6SaQtxKItEJ44ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24308" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24307">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n78irchaIkxL6clWkpPeO76zC2-fAHDlAq8ejpbgHuvBXg0BYPaL69dshjvyEQ8iD7pAPQiy5wKjZEEm7wTo-3QJZOW7xw1R6PYBFJR3DrzQLBfAVZdyCKIU2WLTNsbJlT42ftHAEcB0ScEw6ppe8bkuEOqPl2QYcsF9rdJUfN184hrDB24HBCu3HSm7PtxA-G7hviPGu1b27DiK9kaBhWNG7YiOICrRGMWTs48jhXQeiOCzW4O03jXzaMXR_bp8rYM94J_vK7JdIcckpGPyYaAeM5s5R20FBPcdqM9TtG2vtJiX4Qlg7ldKK82_lz6ZN8rar_hgM-1OxxhzXTJtVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
عملکردخیره‌کننده وینیسیوس‌جونیور در مرحله گروهی‌جام‌جهانی2026: سه بازی سه جایزه بهترین بازیکن‌زمین؛ بازی اول یه گل زد و مانع باخت تیمش شد. بازی دوم یه گل و یه پاس گل داد و سه امتیاز رو برای تیمش گرفت. بازی آخر هم دبل کرد و تیم روصدرنشین گروهش کرد و برد مرحله…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24307" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24306">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=nKAp3VJ4_SQV7YBGFuen6ocw0VUhUQawJsowb0BHgKuGfi71YKG2ugu7k6rrQvTf5kLyEx3y391V9Zt7L5Y3UqVRILvXz_VT4HYRTSDja9xiY-ejz9X7CbpXPNmvBAGqsFrfl-qnn_LOk4n8qz7m5oK8Y9TJ6IJHub2_a4s_oMFtvckW9OA1KRPMnu5y2DOifQ8Br8mhOsidQnYiuI7rFIKTmBs_81sbFaMrHrCtz4LWFI2VHK3nohPydyAiLSFKemRQWhKIm09BM1wFMJJipi3tAmeEF6lrwzAkn_Os42GaWTxxCQKkyLT-GXRGKT14qGFpXb7k-rAJBX8-MBiu9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=nKAp3VJ4_SQV7YBGFuen6ocw0VUhUQawJsowb0BHgKuGfi71YKG2ugu7k6rrQvTf5kLyEx3y391V9Zt7L5Y3UqVRILvXz_VT4HYRTSDja9xiY-ejz9X7CbpXPNmvBAGqsFrfl-qnn_LOk4n8qz7m5oK8Y9TJ6IJHub2_a4s_oMFtvckW9OA1KRPMnu5y2DOifQ8Br8mhOsidQnYiuI7rFIKTmBs_81sbFaMrHrCtz4LWFI2VHK3nohPydyAiLSFKemRQWhKIm09BM1wFMJJipi3tAmeEF6lrwzAkn_Os42GaWTxxCQKkyLT-GXRGKT14qGFpXb7k-rAJBX8-MBiu9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
از زیبایی‌های فوتبال و جام‌جهانی 2026
؛ وقتی میگیم‌فوتبال‌فراتر از یه ورزشه دقیقا منظورمون اینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24306" target="_blank">📅 20:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24305">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTuasafdOnEczu2DDqaenwAwpfNWMcm9khcCn9rVuU6qyclx_-mXGhh4tAfFWqUw99_d2G88U4vroGrzCb3hBABZqIg8d4WLY4EpTapHmc1g8R2Jo-g_5k9kdut-h56_8kGP8nPn1Av3CPjU7Yjj5cx9GrZK1oQNE11lGN5dURUMD3GgZQRhTSyuW1W3iQjY-Xm1en9vwCTixR9oA_XRwsUFnqcRx1rVkC8Og1tFrBUj5M4PvYAzALV1OxJXMpi-699ajyCgN8nhu9eVMPgMMqC9_C-CeJvXKWoX0IFlPaof3WB0l24ddNGDhs76HwDO4iYR4Ym_NxgFCNvuD3DEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کازویوشی میورا 58 ساله میخواد رکوردشکنی خود را تاچهل‌ویکمین‌فصلش با فوکوشیما ادامه بده و بار دیگر بازنشستگی‌اش را به تعویق بیندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24305" target="_blank">📅 19:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24304">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtIONLK4QF_V2mO9ro4gqmsSsajAWt_3-u1Sr7ZhOhbOQHZizcsnIfrJ-jXIEa7--zJm5-fldIlFxfnTqhTbDvAf4oJEUgeewxqCUHULODvnJs2DHg8Y9p1Ipl6Y3D7HL33kyMuoojsyHUeBeLyWp9E_FbTlxP3BSgLaVhvg0n_tj_UYKlfGvnSowf9vxfRJE-qULILjAvSOAWscsRBrDZ9vhlqZ9FS1g3RBrGuJ4RryS1MhDlBC2Xm6c848lJ-zRUb14llE_f29HGXvbuB72VmV74nJG_rKjNc-xqWg71yitUfdMQ7SmmzTko1ase6THq9Rlh2nO-x2paoj0clLGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رونمایی‌دقیق‌از رقم‌قرارداد عجیب محمد دانشگر 33 ساله‌باشگاه‌تراکتور تبریز: فصل اول رقم پایه قرارداد 85 میلیارد تومان توافق شده‌‌. فصل دوم رقم پایه قرارداد 105 میلیارد تومان توافق شده. همین هفته میره دفترمحمدرضازنوزی رسمی میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24304" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBNw2gbBa6C-EPgtWczg6q8iPoRNiUDEBRouFUMkrufCF6TqDVOkFSu6QtqxBSP_M4Omf7wxYYZa-WyU-zqIdVpiH5_6jEFHDnAZ_JrfKXa01AI6a16RpYkfC-bA3p1elQarX4teLL5P9QACZ-9jUVH-iod14gMqVBlnIqSM7MprPlxPcaUChJWaHVRjXr4kf4jAJ3OIrjqcbERQqvZ_gVAnJurD6RMt042SMQf_0bty5bx5ZPXB52jIzTChll_nnSwure7aIKN-P9mEqhqMyeMTRwMGXFnSQdHwN86iFnCm4cydShwY01VzAu-JJyd4uHfo73C49vHarWbITPpXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇹🇷
🇨🇲
#نقل‌انتقالات|بااتمام قرارداد قرضی‌اش با باشگاه ترابزون‌اسپور؛ آندره اونانا گلر کامرونی تیم منچستر یونایتد رسما به جمع شیاطین سرخ برگشت تا مایکل کریک نظر نهایی خود را در این باره بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24303" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Es6vuOfYEmYQ7a1y5nvXaS7uCT4peL4RoITJtRMFgcZPOEMSq31r2T55qh_521ThpXOZ35xKoox67y4wKbuMRiNk-Cv4k0C6iP3A0ZbIoqA_a0t2i_kFvn0byZG_KMlANs9s_65c2VI-4Lc8fHLbItXCCeREySyzsVUUvVpEUlPkYg3RUJCNgMBvxDLgzLKIR1B5bPCvfS7_BFNdE42Bnjj7I6KiPZDUY7pXcYgvSd3TGDFOSUy_D0--YzKqfZ9ppVnOr0iV1gGNdFUIvcPy4vZF5iavgnA-6K6YGpACb1fQzkn9GDKFcw4XmvIQdHoFme-dsaIhA9Lm6IVriTdX2EcyytZJBSxgmqzktcdryIkH86LaOtdFcVno4NdiuQstedCUOnykiyRlkXJbb7nHECK3GaWMg9Gp8ZePyY9UaHbBmhPLtm78IbgiFBpiRJ5lO3Hp7fEpwgTJ0OmmWN8Q11O0quItxXWuJnCRV_NlVRaNz9prJXrdsxMWAMLE5BDwIsMR00_QnulqZwWAK1WKlXoCTWdH2ZWe7bPOeSiHu3jcI2Rs8nsgagupuJg3kjfEd06ytNXeJ1PnuUc49MHeIAPtZ4-CpJFzeNgeUBvUPtcWX7j09olZ8xtJw_C14iteO0lEkzb_cbGbnezeIJAH5np5lBNBr31fa9OeH4CXdo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Es6vuOfYEmYQ7a1y5nvXaS7uCT4peL4RoITJtRMFgcZPOEMSq31r2T55qh_521ThpXOZ35xKoox67y4wKbuMRiNk-Cv4k0C6iP3A0ZbIoqA_a0t2i_kFvn0byZG_KMlANs9s_65c2VI-4Lc8fHLbItXCCeREySyzsVUUvVpEUlPkYg3RUJCNgMBvxDLgzLKIR1B5bPCvfS7_BFNdE42Bnjj7I6KiPZDUY7pXcYgvSd3TGDFOSUy_D0--YzKqfZ9ppVnOr0iV1gGNdFUIvcPy4vZF5iavgnA-6K6YGpACb1fQzkn9GDKFcw4XmvIQdHoFme-dsaIhA9Lm6IVriTdX2EcyytZJBSxgmqzktcdryIkH86LaOtdFcVno4NdiuQstedCUOnykiyRlkXJbb7nHECK3GaWMg9Gp8ZePyY9UaHbBmhPLtm78IbgiFBpiRJ5lO3Hp7fEpwgTJ0OmmWN8Q11O0quItxXWuJnCRV_NlVRaNz9prJXrdsxMWAMLE5BDwIsMR00_QnulqZwWAK1WKlXoCTWdH2ZWe7bPOeSiHu3jcI2Rs8nsgagupuJg3kjfEd06ytNXeJ1PnuUc49MHeIAPtZ4-CpJFzeNgeUBvUPtcWX7j09olZ8xtJw_C14iteO0lEkzb_cbGbnezeIJAH5np5lBNBr31fa9OeH4CXdo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24302" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utLlnLsez9Tae6gouCC6wADZT_ADoq5jdtn2wkIE4TNLkm53qNytDcsYRhL5ay-xAmbOYlX-mYC-HEiLuBQeR2LpeQXJ7rJMbKJGEW7Q99O_dDPjEcW8uSUkFz8ZIQS_h_t7L5F2j24djDYoNW62hJMM9syOOS_qklx3acDKKZbbhuQKU6nemrgthg3v8MAAHKaY3AXeKPKHoB8gmVW0-hQ19uxJhmztmPZPRM8KYQjt_rNqHuI96LEAtyaixih0AQg4DyARF9dcj2VggxrtZqCl6SnoD_sf2WVgn4dz7Q5-SuL90yK5nRdye5gnLP4lzg6xfJ7uIkXLXTBra8LZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
اگه پرتغال درهفته سوم کلمبیا رو ببره در مرحله یک سی‌ودوم بمصاف پاراگوئه میره، بعد بلژیک و اگه ببره دریک‌چهارم‌نهایی با آرژانتین بازی میکنه. اما اگه ببازه یا حتی‌مساوی‌کنه انگلیس، فرانسه و اسپانیا در مرحله حذفی رقابت ها در انتظارش خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24301" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCnRBN80NdKFoeqUElnJWDig1T5MpvDAucp02BrpOyG-uDu-Lvp6_aSHYyPk4TwaETZekJn8W68EHK9xUsXM81B0WXwBw5K3s90CPvtPIP5PI8gyDAIjdFxtQQKhFEDvqMSSp-kXDtaU4d44x6Bj0Rc6hifc_sg9B5wFlM1LfFw3optASqNRU1WK0tPHiA9LPD7QGiePq_W3IPm_B4gpQ8S89vnIFvQmkbqJ6ZTvSjWkERvNHUR9fT_4Ih8Mg78Ium8vhzkxZ-qUcIf9sj_eFhlSBIBLIRE0aa5xCLWbyl4zmBpX-pZ33vxb09c-ebjvB20Dk8vZPcupnaAoCtWLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24299" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5H_siho7x53SUwvS4hfc6TPCdgPSfVk2ugivzIa05_dQWOca_mRuJAAhTjjtz_1vmxikeyqVq6efbTPI5G0v4Np3xvwUCrWYnMHwHU2Ts7BJUkXz4MJj79pT2fFN_Uh2eHAWa517OzOi_P6d3Wg4kFLfhvdM3OyOgVECMuZXC-8a2CjGwU3MHAr5ektYksAGMGRft8BEZ0Q4kmGUtqliPUWtfAgpoCX0rl-eg8vgL8ZHo4HEzrN1qJG4L_nDWvzQFRtydefBu95KweXf376ntRr1o2I5itMfW_4FLYRGjaElQSYvhQziITnfsVXiK4_-f1qrhYxcQmCwt_M-GHt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیماریزیو: رئال‌مادریدمیخواد بند فسخ قرارداد 60میلیون‌یورویی‌ نیکوپاز روبرای پیوستن‌به‌ تیم‌های لیگ‌جزیره صادر کنه. مورینیو گفته مشکلی با جدایی قطعی نیکو پاز نداره!!! دقیقا اتفاقی که برای اودگارد رخ داد و چند سال بعد رئال برای جذبش اقدام کرد و آرسنال گفت…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24298" target="_blank">📅 18:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7nLFhN383sK9EupUMtVqhLxjVE4XyCUtOCqUZ__Xn45-C9eUAkUwa-HFItBEHyO4flM4tvM6OMag61pLNuQaZSXUmRxvivK9p071JpZ8APRLP_l-P9Mif__hHuF42o-sRMzwaTwb0Ju0ni66yZqv2ysJNZ-U2S2VwM0Szf4xUbtqlGcq_voJVT2ixjZJCwy9usY4bp1gPp6hquB9p-RJbPgGmwZFNopnqNlg-dSSE4nKa8sw6J8-ubV3DFSptf6mhiNQNWHpqqxHx31K16h-UVcs6WcyKKRLJDgN7fJ8uX6VL6e-leV36b-vKqjI_Ljw34MN9tA4RGW5X_vHmn7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کول‌پالمر تو یه‌پروژه‌دریایی تو صربستان 10 میلیون یورو سرمایه‌گذاری کرده ولی بعدش فهمیده صربستان دریا نداره و ازش کلاهبرداری شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24297" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFE3-t3jphaL533OwB6I0QpBtpDX-X5LlI14JvAkxCKN7wOBfrDN1x84hAF-RznpXNAMd1o4t8Gx_wL6soeyysQEfBmcn_XAPfmJ9ZIa52_yTR2NigJQK9Lpr9dv4LDQWsk6KPYT-7lLV8jiLcp4Xh7yhXxVnUrSF5nQ9Xj-1z9GXAx2oAyT08FefL5tkPLix4XddqA6YKilpPRYALSMr00_IiP-0OpnQLr_ktFrYXjEibs3pQIoMUzBr_hsfvK6Otki_3zyY5-4kNuAfJgNCBtAj3i0yb8LaRVeWY-iZhTY2etqmwm598-PqayelGnO6sRRfo9qKhHcJxFM5hBVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24296" target="_blank">📅 18:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Omxgx3tPO9jIqDk_rsmb5ZwMVTlCTXtqt243vcISPBKe_LCIVIcc6E9n0RkAecLdl_xRBtyCRgWr0HpPpEW5dBnNa97pNgn7EvIrUex-iWp074r911lUlkwF9w4ckgIuPjkR3QEfVAjFCjJZuUxBigKX_8fQ5Oo5kGB0wpq-qVb0r7a6BJYRiHY6u1078phAnrMXnOJ-MtFNE2mmL2P9e2aB8K2iR26yOzHXuKJh9sm0Y6x5fdhMU5dKdWzhxk6nBsibl-pboSJEfIyhSdEPdFDPSU7DbKxEuo9EmWF7I-1AaWBlB9yKxXGrwbx806nuAUHMj-6CpiGGTso9_rOBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24295" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lR_hHVJobIxxHLxwgl6FQOpVreqE9fEneWxS6GGS45oG_1dDEw0QOTbD-Bj3Gf1viQlLUBVX_A3Sn9UzbEy-UlDZ62emnLyZaijpKSe12M77S4mEV54X8KuD2MeszqtlyAlroWxPSFKKN6BFp3cfgnpORNq_8GX3zAoktWI6-DkEWCXLAUjId1-mm45w7xXIQmNj2M0Av55TyFo3a1x2DsEUa7KtwM-Og17ntx9XhbrDas7UfiEmPbncAGt3kornq_1xZUlnsJtAkHkL9wbHI_N-Xnwo3KNUO0smGzW0XMuZqK96WDK8WhSlp-DTjOzDY1_OyfHLFOyAFKI5CW-0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAitDFITrmZ7pWc3KXasiNYa81Dyqkwhb7pSZerHSUQaA3xGvd0eXDbiwDgSmuiqa2_S-avdn5_QfLfdHb1bq2EWoB0eNKkhKFWZ1huu8qnRHqBqBpfuQhUf2UvhPDskd5Gelq-G8cD88z08KvnBoGVCjNov-J4ObesKTmBdMUlxbdWWYlJqVsvNZGQ6viIEPCshwkg18H6XYOg2mvJoQg2XRtS1oU-SIpjQy_ta26QLuL5q_PrBBIsd-3YpGXE1wQgOH0jRPXTpz0A5soE3UO5ouB0F2ca0Mtrfas5oWrT7l_i9qcR6pFjS-UbifQ7vn2BCoROtVieu8YWOxpZtwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف بود هم بهش خیانت میکرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24293" target="_blank">📅 17:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKM8_ZIHzqsLmBKpDskHkvdCxHishn0JwTi2YaKIOpUHQ9GUj0fvcG71JtmUMikrE6ARacklh3dG6J2DDFdeQq89ytp-aC6QOrPl98fAF7JSI--LmZtaaQW5-oXVFhv0VY84KHmrOlTNL6MWB9PEPDUmddEQkLTmUN9Sb7N8VAGy0jhtxHS_buJZYdUmU92y1aqTmauFwjF0qruC8dJYddxy8CxgTRjLKaxTF7d21fK4Q4NEIc1EsJnal3__pggy3bmGzThhCn5_OzH-nXOp3J1VWdTh2Yp8yulwUTI48rRfpZVwAR0CNl2qEOlnKnna2VvHNR93WmSDjdmCc7asPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24292" target="_blank">📅 17:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8-K6OYZCBULJe-P0HP6aOtbLaHopeH6Ubv16X-0Z7skL4991h3mUoZDhn3YsJLjIYQrUm3mth79_CcXpnFy1vOsA7IDI7j41pzWK0tT92Y0FizIxvcV_pOPsl2vcFMFA5V7L-zoCatowmmf-gwy3t0KFf7COiq8OlKinQlaPPo990luuK3GyTEYa8_vnoAC9u4qn2HFi-16fjntiiJxW23CjHWvhAQTH2z19qfoj4tMAre4oEbnUq4HcnYUCzi6N8vRRccdzaaeTjjkr5axCJvY_2Sxas_CkRzCA1p35jn1_jcJNB9u_2HEDyuzUxK8Ur7uGOIvwmia14vpW4pgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری اوسمار ویرا سرمربی فعلی پرسپولیس درفاصله 24 ساعت تا دیدار مقابل چادرملو اردکان
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24291" target="_blank">📅 17:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=faSN-I7Y8E0l4j3oQEGLZ6TE5-RVi26RRQR0aK2EcR6cldHajWmWu88w0pWeKtdqDdro-6-5fO3DRoKI5PeXAgrxNepeO2wsP970kvZEdchNI3l--AYa42429ePzfdWVmU7bhKg6KNs3C0c_Gp-3GjD16Baf0pKlBgkURfH6F-CDwv8ACjH3kv9o26Rf85av4J-uW-YJN7JpD6FlfMQexL48bFlfxsQZwwcfSBcj0iAbBzDYL3LpYuzAj_D70OYcYhogOnHma3CCdxRSu-NAOpQcLV8IQrzj56C5jUUbhJljpUhoH3zB0j8QajTpanBkssNsvKqXp26pHOreDRCy_KQbbPrS2ePOlbbEeNSMDD670hRRRmL6Un50XpetWkKav0ZXyYUtq1p577d9bk5s1MonN78iZIG0AUP38XF_lkK43ralnTx5dzJkOBlMINXlSObm0YwqkIPUVtFgbsJXKr7WBvdWjwCgqwjHJsTH4AUe35OmDj7-viu8EFKY82yCwo9kyJkYbOpDKKiYjK7xdmmAphnJeDvVvVi1bYmv1X7HG4iK-SU3pWyJCt3tFat-v0iR-6MyCYGTaNQPWe1lF6mlcTnpELY2lU6YBlwaQMmiNCjtj1Y3DJWjA1r_Fqizjds8uLmGQWSangIDB-mAhhTM3EmPBzzeR4U5GipcSUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=faSN-I7Y8E0l4j3oQEGLZ6TE5-RVi26RRQR0aK2EcR6cldHajWmWu88w0pWeKtdqDdro-6-5fO3DRoKI5PeXAgrxNepeO2wsP970kvZEdchNI3l--AYa42429ePzfdWVmU7bhKg6KNs3C0c_Gp-3GjD16Baf0pKlBgkURfH6F-CDwv8ACjH3kv9o26Rf85av4J-uW-YJN7JpD6FlfMQexL48bFlfxsQZwwcfSBcj0iAbBzDYL3LpYuzAj_D70OYcYhogOnHma3CCdxRSu-NAOpQcLV8IQrzj56C5jUUbhJljpUhoH3zB0j8QajTpanBkssNsvKqXp26pHOreDRCy_KQbbPrS2ePOlbbEeNSMDD670hRRRmL6Un50XpetWkKav0ZXyYUtq1p577d9bk5s1MonN78iZIG0AUP38XF_lkK43ralnTx5dzJkOBlMINXlSObm0YwqkIPUVtFgbsJXKr7WBvdWjwCgqwjHJsTH4AUe35OmDj7-viu8EFKY82yCwo9kyJkYbOpDKKiYjK7xdmmAphnJeDvVvVi1bYmv1X7HG4iK-SU3pWyJCt3tFat-v0iR-6MyCYGTaNQPWe1lF6mlcTnpELY2lU6YBlwaQMmiNCjtj1Y3DJWjA1r_Fqizjds8uLmGQWSangIDB-mAhhTM3EmPBzzeR4U5GipcSUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی بال؛
تاکتیک آقای لیونل اسکالونی سرمربی تیم ملی آرژانتین که به شکل فوق‌ العاده‌ ای هم در حمله و هم دفاع بسیار عالی عمل میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24290" target="_blank">📅 16:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOqvRh9k540kzKOL3G4cicVwQI1w5C2gmf6wfc-_nDPMARYTuI4Ag9eMC3oi23wuzUVH_Kj3UoQMpGU--XP2LUWTG-4TLNLFrjgPuGSuJ-PASsV1zw1Hr3_-E8fNugb1EdGO7BqmRLLa1-T2Rkz7lafeNk_ngBHXTljAyC4l9tfcOcnrWzHT9vGEZyuiMUjUVLulDU2zY3wvN_OriyggZOmOnYuftxNTdtkU7GEvxyCbJWL92YqmC-CRMp9ltmiIKDBCDgtQ74_hBe-njTi5Fuvj1QJ4gedAVEnfzJzqViooR-RSRKEK-f5l-2Olm6G36xUlMoZD_D_-jmVNyUwSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24288" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=mlBCOyfVm1_gzy1sbW1LyCocgwgC7VkrE-3DX6Dwo3XYdPguGNXtbto_sQ9lTh23-I66FXjijA29BFPpdwqYYoM0VMh_GH2jcjb-xEUHrE1dp2r-IVEtIlXq-_dT-IXUSwNfdczrVfyszOKYhkduhWjmQXIPRVdglu0UUjnqp2WH0-nqQYTUXB155ym4YcrP-hezq7TNteJyjdmizPDLUzW6Uqe6BWEyPqcvJibyunZwSMSGTHyT8q-8fqTHh7do4WODtqMAFPjQzSIeRieAsgZFbZKu3Nv_RVofxY43hyWRoygcetZi2nUO0PL2NI-c1buYKpKlvbTXkQ-mFlOdQSOCuzDgpqFu2hi9f2tv_94SQ1NsaDt66LbmT6U86A2rN7BdL6gEDk8k2R1poZiAywJZKOZln1Ycu781pPuSRwFHiz9Tn4SmZDQO-cP7FnO4_RM-gfc5PVwM2HK6qfuvA3ZZZcO6BfMOHLwSNe6GZuHUR6r_ff3bNYixDrfk2UE_ETyKcIX7TLOldiZXbM0rozfpiQ9HTwf4d4Ewxf8J6gasLxCNS8rbjvGYTQWhFPZRSlDR-5-6ShQlLO6XtI4_mUX4W5dD8sQ9F6yqt3a2SbMsefOJNF-o5jNo6fRxgRBN7DLn2RpP12V6DyZUsbBbgv-xf9P6P-OhoTy3_D68F2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=mlBCOyfVm1_gzy1sbW1LyCocgwgC7VkrE-3DX6Dwo3XYdPguGNXtbto_sQ9lTh23-I66FXjijA29BFPpdwqYYoM0VMh_GH2jcjb-xEUHrE1dp2r-IVEtIlXq-_dT-IXUSwNfdczrVfyszOKYhkduhWjmQXIPRVdglu0UUjnqp2WH0-nqQYTUXB155ym4YcrP-hezq7TNteJyjdmizPDLUzW6Uqe6BWEyPqcvJibyunZwSMSGTHyT8q-8fqTHh7do4WODtqMAFPjQzSIeRieAsgZFbZKu3Nv_RVofxY43hyWRoygcetZi2nUO0PL2NI-c1buYKpKlvbTXkQ-mFlOdQSOCuzDgpqFu2hi9f2tv_94SQ1NsaDt66LbmT6U86A2rN7BdL6gEDk8k2R1poZiAywJZKOZln1Ycu781pPuSRwFHiz9Tn4SmZDQO-cP7FnO4_RM-gfc5PVwM2HK6qfuvA3ZZZcO6BfMOHLwSNe6GZuHUR6r_ff3bNYixDrfk2UE_ETyKcIX7TLOldiZXbM0rozfpiQ9HTwf4d4Ewxf8J6gasLxCNS8rbjvGYTQWhFPZRSlDR-5-6ShQlLO6XtI4_mUX4W5dD8sQ9F6yqt3a2SbMsefOJNF-o5jNo6fRxgRBN7DLn2RpP12V6DyZUsbBbgv-xf9P6P-OhoTy3_D68F2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
​​
طرفدارکوچولو و بامزه غنایی‌که با جان تری اسطوره چلسی و بلینگهام‌سلفی‌وفیلم‌ میگیره؛ گفته ازکی‌روش میخوام غنا رو قهرمان جام جهانی بکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24287" target="_blank">📅 16:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwX6H7wWyTpzSgUMisq9bhmButP-I-qwm9_2cy2H5LI-VhdYY7vWo61P5-N44IRpcR6_78WtC5jzLxSYVDSrbhW8Zv6vEtyG5WaITouVL8TCRj5CXenpzVgJ2j-KCkyuh1NqGnYlKFzp0aIzaHPJBxxlRgCEBpGN7WOSgDMrU0L9g1yFTmmaWp62eqGKIT6vo2j6HntqDHsu8rnOBtmgdbyEDP1Ci-7s_VYgy7xcy_eK4PO9ZZXa5lKH9az9_ndBfDMAZOfjUcaWCLrV-0wNKmEAw1-ftNbLVLDqBMAIX88sUMwas-q1ri8KZWXMS8UQJx01usUgmuZt5EzXYt6ngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#فوری #اختصاصی_پرشیانا؛جلسه بین مدیران‌پرسپولیس و اوسمارویرا برای‌قطع‌همکاری دو طرفه به‌پایان‌رسید؛ اوسمار ویرا موافقت‌خود را برای جدایی از پرسپولیس با دریافت 900 هزار دلار اعلام کرده‌ قراره بزودی باشگاه‌این‌مبلع رو در دو مرحله به او پرداخت کنه و قراردادش…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24286" target="_blank">📅 15:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEtgP1FuuDaDscO0jl6j9s4DbuiYNxCe2_Y9MqLx1ZtuRRmsMB_g9jDB2iBYG4Rhnm_ISNlBpAUxesXCJfts_IrwufhB2pLfSWm1gzIe8vsX3EwU6O67d1iwaSTlY4WUniyWsA55ucmdh8LGjs7dZNqZNigF4IfgLGMM_hGoD8FxPr7EQFeXRYBCbHEaoCd0ZNS1DblRoh2pvTuRATvfBtfCtjHfoKdkYQ5Yu1xri5fJ_YJsSmw2DoVWXPkyl-gyqYZAaSHmRowEKwjn4_FpBTARoUq3epygdatKXu_bjFxuH3MOMDXQuC8b35Wm86EtPEbh_Y_g_dIa-9rGgToOxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24285" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfsU3wiEQHpUKH1egKoLQtZtce78wGZeaX88ZIvFj2kPIM_sPu0B2blOKt37pyGk4biFrdpS5KTOYYj8WiEKf6OMhEiQVLh6iKi-IAlP9tUbPPop9O6cryTHNXBHnJisLwHNZfQVq3hJmwOYi7CBdIjSbq0dCwOL85gLm-mLq4lN2_y0vYcpPgeC9nqe3S-Hma8mJ6DQa5y5puYtXc9DgagTuy-pn7mmzDz8155YfvisE0TbqJ7mZfQWynp4RYNEsRJ_BSM5UOoX0XzKJLlnBED5xnDxhp4Va2INJa7H1iIqSKtK9unSzOx06YVSorsatK2Hf0Ggj5JnZr2D7P3mZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛
علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24284" target="_blank">📅 15:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKyTbTSTJCV2mpq_h4a0v39963bz4OxtjoaX58S9lks85AijsdISj509Did1Cz9HWlhBSeL5rfr-8MHbKCpMMwnl4KWrecdAb3-GzT5XozDKrK8k-xMTGon6xG9RgJ7DeskjqblYWV8KIh0RHhVjt-fLOeoqwpUy3Lnw2tupA9VqUhR5KrBKCxz9ahZGNEfvOfVPbqa1v3YufcTgBgTiBT5M267V09038Ra67eg3GpJiMAShAi0WPgM6tirlDVp9Lrj-sLBQsmwe46JP1ircZtxs1owvjquLyEZzkCeReYamkf9cLFULCBGl0IUbrx_jKNLRkoC-R52o6aTAjwI85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24283" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXAxp_mMQ_m26qpr6SgdbNWhrArrOcYrv9p7OI73EeKeZYKJNkZy3kobDwB2IyYlfMlG3hwAlib7_OqtTxBwQzkQuDEqE_ijDDwTE3y6pUOaD1wztyoXbow5trtRyQHgKjtkXUm7gor8iww9OBpeD5jK4wnZkVxk1hEGjizn5q0v5PedEahALAIO5-3yoMEA1PjSxFsPK0uB1piHM7Sqil2t0wzW8ZNH2GyQD3mnOQCPsispFxOzLNboj0OUN6cFeP5nTiLY7Y_VP2FSp5_2Nw26hykTR557d7-2J066XKyTMY6sMayJBlnTwzCceu6kAI2WryyHQ7_bmYBZuY9egA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
اگه شاگردان قلعه‌نویی به عنوان تیم سوم صعود کنه در مرحله بعد ممکنه به امباپه و رفقا بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24282" target="_blank">📅 15:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=NQfUIkpTIH8y7SmGeYHr3iZqbh_n2Rg_hz6fMdzzCv_-2259vqrKhzITS3VSn7W5ZluUqhK7uw2XMNQ_hxdVz4KF8uAFYMRXicpAKAa2Hvf1gJdiSBbeRo7RUqlADqUtWEjhr0rajiuwblFli9I-GypIRg0gUrOXiMXXrmS7fmTKwnTzzkUoMCOa-OR1nFzRU3RVnkOkWXTyvuNmDMsDhzIp6akn3BfKcL7sp4xYSJHGxR6TBH5V1YcBvzLiDWpUSsAtbFTaqX1O5bXoEXod1zNjJ4sWpWm-iAtWCX3nyXKZKBMzLjdIs4klTJxiBkTMksS1gmZCtQetPPX5E1X-Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=NQfUIkpTIH8y7SmGeYHr3iZqbh_n2Rg_hz6fMdzzCv_-2259vqrKhzITS3VSn7W5ZluUqhK7uw2XMNQ_hxdVz4KF8uAFYMRXicpAKAa2Hvf1gJdiSBbeRo7RUqlADqUtWEjhr0rajiuwblFli9I-GypIRg0gUrOXiMXXrmS7fmTKwnTzzkUoMCOa-OR1nFzRU3RVnkOkWXTyvuNmDMsDhzIp6akn3BfKcL7sp4xYSJHGxR6TBH5V1YcBvzLiDWpUSsAtbFTaqX1O5bXoEXod1zNjJ4sWpWm-iAtWCX3nyXKZKBMzLjdIs4klTJxiBkTMksS1gmZCtQetPPX5E1X-Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24281" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czHQNM46rXa7REvgZFnjTCQBgoYlNM4ovGU0ybjp0lWAUBaxa7Eq9LHJmWJUdX-0NdE64Tg26Y03P9EWGMpyIgQFf0e8s_PDmWcm-LZ4E0ThQxC_GYa5T79sfIttqzt_TAXt94C0PAPAk12SzsC4tjN5_frmQf-fA3X7yESOBvvK7Ve3U_VAqRMhtAiq2THFRCBuZQeQdbcUTFZ7ecfraci4FKoAUm1fpH2yenFLLkeIfVmTNBD0ZdqUjPKWQ1A_gy-joaMsUFtqv4zZX0lDsalz7H8w4MnNfTznVBHrmcF-yaypZlL-fnpoUuLcPU7JBOHxuCFaPPIYq7s8tldG_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24280" target="_blank">📅 14:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOItqMM3b9_LlnXwhw_EgUpotuxhxHbJs2FZn070XbfZpqK2X6oAMZFFkJcO7GSXJJslX0I39RrSF6jZsoMUlYOh5ldmd0KgrVuQWk0BnhvyIQC800oyeFB_RRBbXH7GM7cxjQHcyKdtrZSYX6eROT_sRPkVbSpJ_HF6atKuXZ9DXkLarhgLHGNtCCXu3FCeZJb8TUW-fh1Q4kbGZVf8eEjta4-4-pdrOlZfMK11-spBGt4CWDzU8UCDsz5ourox5FW61uL-Xfm_rtlZLmGY8GjJGe5czJfktY95UbDxROkF7E_SmSUNdEkeForwJ1WK33cUXGMhUDNZCdtDxUXaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول‌گروهA رقابت‌های جام‌جهانی در پایان مرحله‌گروهی؛مکزیک‌با 9 امتیاز مقتدرانه صعود کرد. آفریقای جنوبی نیز با شکست دادن کره دوم شد و کره نیز احتمالا بعنوان تیم سوم صعود میکنه اما قرعش سخت خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24279" target="_blank">📅 13:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHnBsSsXfEJEtzBGnAud_vAmCzmP6AyBytyI6GVcDzOELvKNkpIYN7H9zpAhF6v1wdHWDIUMI8ypNjDZD0qgUI0U7s_NupvvQ6UOAYpiTYiT3Sel8ccthq0-Z9tBAIxCzyXX6tDLqco_Ilo1QGWxdcm-7o_N5OQfdOoE_K3WFtHI521P2RcXlGiJPctzKPdnjVqWwfVqytGQGF2EwPUzeOOOqqGFDPXcx62RZfIlC8sJD-rye1NBauViQFjs0HRnq0fvojV4fS1Axs_D0DPGRLw1NnZW5lTjGzNCT8SfKa-LprTNX07kEVzCUJNIuJAcS_kav1GeqwD7McoROjQ4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24277" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=NeBhyOL_Lw8byX51xEAc1oIf7j6k5SWDGIAXoQTMpwEohE2aCauMsSdZ-nMSiDHeajJC1FJBzqMaKhfkLRn4Z4wocps7mC67QpXRQnAylI9Dg9mG5rEooqMWBf3W-cSREeMC2uZWphass5GCybcS3vvzX83OYQW_T7V9spQC-_KOzQhlC0rmnWlM3m5pMzfRjxglML9qdd24foiS2pHXpbmn6cklPsl0t9_l58dHJCDFCEDjFvQIQtQeGhSACHqpsTZdlUileKVmHiXQ9fhg9zv_Yg2WHw2LBJO0isUByW8zUj9Q3QZsKCxMjzaNO5OasUqGwoedhaHnQ0dpwCj8AJLvhKBs8d3QvV3Q2-UiunhqcstUZZ858aLsXXtHUY42Q-FW26hRulWSMbjH4AAXlEO6LJseTSWZ_cKGjdNBL-M5mb1DStoH6q2YgPFtwFHqiMaqXg2aBg8otoTTBfGk_jDeQ7FVdUM6iEh0-4XTJXsF7v4RisIJSaj2t8OUSmFy7fOyDx5QDRAboiQtltbLqmepPfhWCKbJYFex3sy9_Xf9REhNzZ0XnsFvYEvsYWw2rUzXo4lnGkyhMGIiNevuJLOUmMYHcyF4DZz-uDw0du5S4iUahkrsAMnYJBXmdm8e6KI-Enj6LVcdPB5UGxL8hPhke2rMGS9xi-UAFYl7vXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=NeBhyOL_Lw8byX51xEAc1oIf7j6k5SWDGIAXoQTMpwEohE2aCauMsSdZ-nMSiDHeajJC1FJBzqMaKhfkLRn4Z4wocps7mC67QpXRQnAylI9Dg9mG5rEooqMWBf3W-cSREeMC2uZWphass5GCybcS3vvzX83OYQW_T7V9spQC-_KOzQhlC0rmnWlM3m5pMzfRjxglML9qdd24foiS2pHXpbmn6cklPsl0t9_l58dHJCDFCEDjFvQIQtQeGhSACHqpsTZdlUileKVmHiXQ9fhg9zv_Yg2WHw2LBJO0isUByW8zUj9Q3QZsKCxMjzaNO5OasUqGwoedhaHnQ0dpwCj8AJLvhKBs8d3QvV3Q2-UiunhqcstUZZ858aLsXXtHUY42Q-FW26hRulWSMbjH4AAXlEO6LJseTSWZ_cKGjdNBL-M5mb1DStoH6q2YgPFtwFHqiMaqXg2aBg8otoTTBfGk_jDeQ7FVdUM6iEh0-4XTJXsF7v4RisIJSaj2t8OUSmFy7fOyDx5QDRAboiQtltbLqmepPfhWCKbJYFex3sy9_Xf9REhNzZ0XnsFvYEvsYWw2rUzXo4lnGkyhMGIiNevuJLOUmMYHcyF4DZz-uDw0du5S4iUahkrsAMnYJBXmdm8e6KI-Enj6LVcdPB5UGxL8hPhke2rMGS9xi-UAFYl7vXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24276" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPpZEs5xJ0LymKu_KzPBvGjmazQTkeM4yYX7mI_-kVnbUGB9R53mhVGaKhw-gkwfJ5vy-SIQPi-dmcukfUCOA6WividMEMDzhyuhnt9JrXLZY5pOX9WThXLfuwHQelJpuadk1mQbQPtKoj32B4dKTLJNxAqX9H2egTg-3XtnV8UiW6VzfRzp4YNYou7N2lPEa9J30tzUoTT6wDHx3bH5-oMUTvo_tHxpCwh1Yq67XZVN3dHI_KHPwG3_fgBGXUVESWhnsOafHKW8sGnCZkP01mtw5-MHyzngESatsPiDSyekkTLis3rVE2LrNSJI7-BTkj2CpG-WPOZVnAW-R9ce8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
باشگاه اتلتیکو مادرید: ما خولیان آلوارز رو زیر500 میلیون یورو به بارسا نمیدیم. آلوارز زجه هم بزنه زیر این‌قیمت‌فروشی‌نیست. رومانو هم گفته مطمئنم 150 میلیون‌یورو بهشون بدن درجا رضایت نامه خولیان الوارز رو برای بارسا صادر میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24275" target="_blank">📅 12:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=Y7zX7rGXoQYrp2J62PwDdDV-z-Su1Cz7m6kfzYd57NOc8TxJrHDTGOdlOfxBpwpnw1skli-BD1MQgal-xLms-l5OkFf38DbLfj96JL5S_Md37EoVr24Q_lEFPebLLTw9H_v6rJNH31bSaDtgponkibV_qm1eN37cI1uUTq9IBh4FLN7kxqA3EuCXBgWOabe3ujb4K06vVgdemjzPUsdUHA-g0VX7UgCN8T7QNJc6V_KzEz-xlgGMc83kwgDHnETAK8PPfbDIu61qF5bRZXAH9KKS86KgxFz3XE5gcPtUnUMwQqBdKks0EtFBB3bOlXQMiUgWFvkG8py-xSoue21E_QMaPIS11HcyWTMJQAvxO6EJu-PaQajDJXcslAalc_cxHTpLow9Y4IeNdrNX4LlN8qdUmIdQVe3XE3A1ztr8Qiza9Aff_TC4LPtLOtb0lbfJmKpROBTNBsrO21Gzf3gJtilr05EPcdzU4vtPwnOSVSXM6hTh-lM1Az6irGJJ7Ipj6_EbwemWbFsSXd7hI77Kx30fpRTSV3WrBNLj5kahqYbmaYfcsturvpSa2wVrSEJ4XYeI_fBoGLJsUw9wQnBGUPkvZwoQddxk8LOitMECkA26J0TbCttv_MOTG9Q87k0KApyDwXLeh9-sq-3d4J_4spShqjMaLttAi7Hh87zQdp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=Y7zX7rGXoQYrp2J62PwDdDV-z-Su1Cz7m6kfzYd57NOc8TxJrHDTGOdlOfxBpwpnw1skli-BD1MQgal-xLms-l5OkFf38DbLfj96JL5S_Md37EoVr24Q_lEFPebLLTw9H_v6rJNH31bSaDtgponkibV_qm1eN37cI1uUTq9IBh4FLN7kxqA3EuCXBgWOabe3ujb4K06vVgdemjzPUsdUHA-g0VX7UgCN8T7QNJc6V_KzEz-xlgGMc83kwgDHnETAK8PPfbDIu61qF5bRZXAH9KKS86KgxFz3XE5gcPtUnUMwQqBdKks0EtFBB3bOlXQMiUgWFvkG8py-xSoue21E_QMaPIS11HcyWTMJQAvxO6EJu-PaQajDJXcslAalc_cxHTpLow9Y4IeNdrNX4LlN8qdUmIdQVe3XE3A1ztr8Qiza9Aff_TC4LPtLOtb0lbfJmKpROBTNBsrO21Gzf3gJtilr05EPcdzU4vtPwnOSVSXM6hTh-lM1Az6irGJJ7Ipj6_EbwemWbFsSXd7hI77Kx30fpRTSV3WrBNLj5kahqYbmaYfcsturvpSa2wVrSEJ4XYeI_fBoGLJsUw9wQnBGUPkvZwoQddxk8LOitMECkA26J0TbCttv_MOTG9Q87k0KApyDwXLeh9-sq-3d4J_4spShqjMaLttAi7Hh87zQdp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24274" target="_blank">📅 12:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=L8w3DGGjFcuqvH8VQexh3ketSnUoC0Wo6GgwYwiRrwdvpK025zg4dySiLVuq6t3zogBfGfMrvkS1mHaqG-HHF8dWsubc3dZaKLlZPbS11sqfmgdXGHm6sUO5o8oEQYPA4sNrzDC05nVZ47zv8d2cXgnulUAGd_yLH3qUTEKu9QSDZRWEJeBAgi6N2bw1ZV9CLPSdH_33D6mTc9-BLbQu7kWyXn-m_BNmWBULaPoN-57s01NETiwSrYqc0kBCpNmn1HDXB_e3NvIn2EEI06fjU3Iy-EaGlXsPfbGJiaaVFkBIDB1TqoE-0gHy_ZL5W4ZpQEDdOmGil9DDv4IFEkl6SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=L8w3DGGjFcuqvH8VQexh3ketSnUoC0Wo6GgwYwiRrwdvpK025zg4dySiLVuq6t3zogBfGfMrvkS1mHaqG-HHF8dWsubc3dZaKLlZPbS11sqfmgdXGHm6sUO5o8oEQYPA4sNrzDC05nVZ47zv8d2cXgnulUAGd_yLH3qUTEKu9QSDZRWEJeBAgi6N2bw1ZV9CLPSdH_33D6mTc9-BLbQu7kWyXn-m_BNmWBULaPoN-57s01NETiwSrYqc0kBCpNmn1HDXB_e3NvIn2EEI06fjU3Iy-EaGlXsPfbGJiaaVFkBIDB1TqoE-0gHy_ZL5W4ZpQEDdOmGil9DDv4IFEkl6SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24273" target="_blank">📅 12:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryIGmP_9_8R2HpAtJIIt6ykJHoGYWBESas6SikTrAqJxmbRbvLgW_zi4Lfhr6MOMXZpmGD-QRFYcXw0AfRkOKoGuRlMv_k20__HMc45LVsc98UOgWSrlfcPEOxYrqwtu9yi_CLWPi1exxPGjJG5bEif-l97X8CKXNJzt5xu4Y8sM0aQ25ihS4DCarKEbG3Q1IN3PqK36s5cR5LhawV8f9YME9vIEcSzViD1TCk2itMImXsDEwsB0oYaoF8TjjuNMzbr_1sAAVKqe917vQudEnq6YIJcY1tLf9s5-1-Cj0IGx0npPTl0-Ad2x4sIl-7HQWvK-RoDliDTBt1jNPRU5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعدادفالورهای وزینیا دروازه‌بان تیم‌کیپ ورد در کمتر از یک هفته از 50 هزار به 15.5 میلیون رسید. تعداد فالورهاش از 8 تاازبهترین بازیکنان حال حاضر فوتبال جهان بیشتر شد. عکس رو باز کنید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24272" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxGbINc6n9kG8noGVRNT4CE0p8HvN_iERP8_ecZP7oATfv-0uIpeIuKHzVfuGEK-_jeXazZ6BoR8iEQwjGQpHe1C4WrpFXoqW2B3VJYpBX4mdLr-LLdZ9N9XqlELWgqUaqDdcAxKaM_8H9mMAcUDllTycRqj-6NupKcah5doi8hk83KAmsE5Qoc3YtAfeFeDQ7JcbxjUrFl0xyXZfLtcXae3oJPQ2LMYaM5kQssDXD9R8pOkFwbcCFIEiOj7G3RSK8CAdStvZuoJd5-CNk48-jfNfGQV7wFQKKKOJGHs_it5xjLwOWhq4C6sRKSJtXfXw8a5eh09TKisv1UT1nVJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌ های دیدار امشب دو تیم برزیل
🆚
مراکش و دیدار دوتیم‌مراکش
🆚
هائیتی در هفته سوم جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24271" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhuQCqzSXWhOjIUXgGmjFRhlmKmQN7mJL3G9wxg9er9qx1WBEjIZaysNeCY1ZDLUoa1jtI8y9wcSpTwNyVYiMrK6JGa0yUW7n82V6-IdpJN0QzTR7GtLTbhbWOBKZz1NY2IL8Ao8PLJVSrF2J4IPxy52DXmRE8Mt1YdgJ-_5n4si3oKM-PK5CLsrMbkAmNLJ58ZMauzYpCDs45vdntxFbBEaGmH9BzbW5zqVR4hAOeCmR_JOJSNv96nV-PEC6FxtfE4YwRy51fMQhTDKFkc1x7CjRy5-ALUW7y599npU6wJVlCpsSVOy1VvvdguPCoGA8FVWhjkjs4Mo_C4k0hPHXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24269" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24267">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYmV8lbM1sQnvsoQcWWZ5UVotIWXLw38UEYVn0PGltS-62Hnsjn2AssfFjpYUSjbx2FzR5L9yKm2wOAezzTAxR5neID8HQsWC-QWLCTtTI8RvZPH6zsaeM6JUwKy6ZfXpr5hRBrYwnrbkOriN-itP7AMQgKtIp6-Rro6IHbm4wXOVnBKE8P9bPSXpftFykfYVLvY7ZUqq2Sb4jFLV7t9tQC_iANoSvYpzTn-L46Em5zcSBV1kXMmmqPgW9gX6LgcI6hK7VMSXJuEsmkFs4cBeI2Jw34kIQ21m0yVMM7Ii7UPuzQtE9NmPTfquAhzagtrxEXfbfVf5rnIgPO4pkq7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hz8TH17QHAjJT4Lves6zzCzrHgk1c5pQ2fysraCKV07qOBqKd1xFIuAMPdouTw2EA1YNkuSRiB25-R3DISbo7k21KuSTMrByZkW7dtHBP4bxW7OaJ0ENniHxOSj9oDFXaFIRhQm237HLifcMp9ySfREgYRxEg14ZNdjfupjrI1tq8bWvR_OOKiiycPfI0YuF_qJVtNwNj5-Rfeehac4YOQk5s-iMvtl3mfsfOeqbzvkpW4b7y-Xw1y_Os4Qa5kjFhB7GDX3rUtbJeCQjnjiqWGj_4iQtxFXtzaVHqJeUBSfkxwotaTRcaK6x4oFB9M_EV1q578S0kvUOMpeXnXomZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24267" target="_blank">📅 11:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24266">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFeU0CTGm5z-xbalKn3gmnlzN8wGEzjTv5ZFl_pQQUh5uVAQdATaTRM5vM4GDIas9ccKAVqbJQiXN7QsPsS66Kn1H11upv_CzQdzfGSJmsoil-cfF8t7k52WL1BufvcjPeCizHvn5PqJeF7zK9__bRklBAcOPAenSITaOsXT-YOm4caOoxfXwe-CWVqwE_rXUW7eUDH8r8X_RLxoRIuw-aF0w4b3CvICV3fgBIIltIIWSY55aaN_l01FtwGG5wETi_H900x3zcEeZND4S-mki7WCdj_8WWi72KxGCKbsHy4gkifNUcvqdDt8lux8njTFbpZy8YgbfAEpMzPPt-IOZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24266" target="_blank">📅 11:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=M_QLl32AfJpXNiOTi9s63NEEOTRQkJLmUHfOheyYS3coc_CmSzjfzLDM57f28yMZ08IqUAzGB-fhq2ys5Ug6m4a-LUHqIaxUg2uoEY6dgUdk_wA---_ixpcl2oESoiIpGHB67Q8qwskTaNjJG9DHyJw9g4BnFAUNZrbDQ9ErBmoO9Mc9RgbzQipttcFK4ThvWsdn5BfAiKbSK3NM3MHmmGndAEURna4j_MqlOVKkDwrfrvis7Tuetw68TYiXC72tnJnPIMdvfo6b31k3JoVFQGzXAcA5gfNHnc79vf2nzzKKQZDLkKntjskyhd3z5329TaOIaw1ffr4g2-sPvzc-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=M_QLl32AfJpXNiOTi9s63NEEOTRQkJLmUHfOheyYS3coc_CmSzjfzLDM57f28yMZ08IqUAzGB-fhq2ys5Ug6m4a-LUHqIaxUg2uoEY6dgUdk_wA---_ixpcl2oESoiIpGHB67Q8qwskTaNjJG9DHyJw9g4BnFAUNZrbDQ9ErBmoO9Mc9RgbzQipttcFK4ThvWsdn5BfAiKbSK3NM3MHmmGndAEURna4j_MqlOVKkDwrfrvis7Tuetw68TYiXC72tnJnPIMdvfo6b31k3JoVFQGzXAcA5gfNHnc79vf2nzzKKQZDLkKntjskyhd3z5329TaOIaw1ffr4g2-sPvzc-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24265" target="_blank">📅 03:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24264" target="_blank">📅 03:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5oJom4_RtUcDJqayQ872oIedTsRCEQ4hYiQn0DqfZsu5bs2E5BkPwEP7CyBenp6Pyt26yTsW97lNKjecvejw4q_FkCepYAxrjhgCwrYjCfJ72S9nfv-h8M6lAg_nyU8FdDjmrobyo6EY-Nl1YAsK344DUvP_zjw8Dv05TQDk4Y-87cDG9oYaevVqHTSelIK8k-JVkZX0g1-D7cZv3sP_O2Ym8VQNBk6rXJrgml_d61B9PFHbC9ZENqRS8pFYBADx6QF-VXBfqQU2SLfxRwoFireh3CaOQYc-dF_E-ga_eLqiDogq57DfyRQCO6vIn1eAFDHqmoQwgizHM8OxByscg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهB درپایان‌مرحله‌گروهی جام جهانی؛ سوئیس، کانادا و بوسنی راهی مرحله بعدی شدند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24263" target="_blank">📅 03:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc0dDiMWNm2YU40fA3T6PiG1JRbsF9-KAXdfdsMUDO_aQDPWVH5rbo5yWJeiCfodAqpqQWMJeqVsltxAbh_V8Xs9iRlMJ1xsQsF-mOe6NfzOCHuNJLHAagVCEJaqa_GAAEo2B7gonfdy0Ns6E74QK1NjDEyppEZoVudpJeO8_-2bFWU7AXmpSwK0LNRuHrqZM-4405D_muijLhqqyVJKJh4Qvr-Zg86JLSGTNRF8XCPRqfbwfXihcVJdcxs5nc1agzJWphZGtqLn5Z9M0hFYDdgET9mPvZqZecZ4XRoKUDqijSabjljAcmTq6uMS1AoiYMrUYU-o9pSvxj6Cqb8f8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=jrDKsRpxVhIlEHA9Z9JD47iQPqk1cjQ6DcPwfE_7rT2Ru8ckGSiYKYqqBfXKPdTMIVpeGzzeNfEH7FKqoGVRcvVdHpYbrccBuEAkkzmXXYgWjFf4h5IvLg9prrWqUWQIINNcfa_r0HN5OSM-UBXgVzLGmQA-J9MIOBu-VAzta9EvsSWGdlUCxGfER2qZnnTbI1bB4FW3tqv8OO8d3s2Ug-vtpLePtbNoenlVadGpZ5JbGQXRmI__B0QjLE2_--HLYOlBF-rxKCK7M8FlR9UC8ob6JbS0B3qxh-HR_R8jz3--E7EgA_NJ74SedcXUVYLtF8XqFwNnJve7MQ3bDiKPXJyxqgitPiVazzY49c1hRb0MsWEATz1y4lj-EP7CDkLcrH5PtSN9oVufESj7Y7vf3M--HU6qCZADS_MAWnT6tKZkVn7QvQjb8DUyxi06YMFkcWhzGqW-bwTq_Al2Y19Ak5vvz0OAfX8jzR3brxwmKiRhnavNeab2UkguBqTj3FD_qvfRIEOdFOavYIC2wqjg4S2e1d7tDCfT50_2LvODmAY9ijqdiEnFfOKviB_JIhR57uA9UnzcQDcDA5o1aHakW02iphKW5vfU6noKfCXQI2O-z9fYU3s8zGGXqg1IWG46q7Fux2MEmuaZrDN8RuzJH7z3Za_wxjbeqWpdg1_kZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=jrDKsRpxVhIlEHA9Z9JD47iQPqk1cjQ6DcPwfE_7rT2Ru8ckGSiYKYqqBfXKPdTMIVpeGzzeNfEH7FKqoGVRcvVdHpYbrccBuEAkkzmXXYgWjFf4h5IvLg9prrWqUWQIINNcfa_r0HN5OSM-UBXgVzLGmQA-J9MIOBu-VAzta9EvsSWGdlUCxGfER2qZnnTbI1bB4FW3tqv8OO8d3s2Ug-vtpLePtbNoenlVadGpZ5JbGQXRmI__B0QjLE2_--HLYOlBF-rxKCK7M8FlR9UC8ob6JbS0B3qxh-HR_R8jz3--E7EgA_NJ74SedcXUVYLtF8XqFwNnJve7MQ3bDiKPXJyxqgitPiVazzY49c1hRb0MsWEATz1y4lj-EP7CDkLcrH5PtSN9oVufESj7Y7vf3M--HU6qCZADS_MAWnT6tKZkVn7QvQjb8DUyxi06YMFkcWhzGqW-bwTq_Al2Y19Ak5vvz0OAfX8jzR3brxwmKiRhnavNeab2UkguBqTj3FD_qvfRIEOdFOavYIC2wqjg4S2e1d7tDCfT50_2LvODmAY9ijqdiEnFfOKviB_JIhR57uA9UnzcQDcDA5o1aHakW02iphKW5vfU6noKfCXQI2O-z9fYU3s8zGGXqg1IWG46q7Fux2MEmuaZrDN8RuzJH7z3Za_wxjbeqWpdg1_kZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
یک پیش‌گویی عجیب و آخرالزمانی از یک پیشگوی برزیلی بنام «وو باهیانا» در فضای مجازی جنجال به پاکرده‌است؛ او با گریه و زاری مدعی شده که در جریان بازی برزیل و اسکاتلند در ورزشگاه هارد راک میامی، دو سفینه فضایی به استادیوم حمله خواهند کرد و در دقیقه ۳۸ نیمه دوم، یکی از این یوفوها اختصاصاً
نیمار
را با خود می‌برد، در حالی که سفینه بزرگ‌تر هزاران نفر از بازیکنان و تماشاگران دیگر را می‌رباید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24261" target="_blank">📅 01:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=RMtls3T-N2xvEb0k0ddmYJVrvPsb1as59iPv13qqMEwfBTLJ0GbkuObTjznO4Vh6EvH_5fBfMVLVgebHXWKwIJFJnUtRZL3eG--20OizwJiwXsZaCmyaD0bXJP8RPKof7Cj0FuoX_BxYraqXJoDYMHJ8wQARYpqGwrok8ofkcUqYhn5upvZKsoBuPGsfkyymekV-wm0C6ansBRP-uftbxOHBDmwm2WouEkUALEBf-m-nMp_W-JPmDGzPXGFh37SJe_la_LeohHYVPQ_MbFTm0eoAhz3l9uIRHKiDt3wtg7igMZthS758_gppxOiFBlT--no7W-o7R_RoQzRwGm7w-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=RMtls3T-N2xvEb0k0ddmYJVrvPsb1as59iPv13qqMEwfBTLJ0GbkuObTjznO4Vh6EvH_5fBfMVLVgebHXWKwIJFJnUtRZL3eG--20OizwJiwXsZaCmyaD0bXJP8RPKof7Cj0FuoX_BxYraqXJoDYMHJ8wQARYpqGwrok8ofkcUqYhn5upvZKsoBuPGsfkyymekV-wm0C6ansBRP-uftbxOHBDmwm2WouEkUALEBf-m-nMp_W-JPmDGzPXGFh37SJe_la_LeohHYVPQ_MbFTm0eoAhz3l9uIRHKiDt3wtg7igMZthS758_gppxOiFBlT--no7W-o7R_RoQzRwGm7w-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسمی فرهنگستان لغت فارسی:
آب درنگ جایگزین فارسی کلمه hydration break شد!
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24260" target="_blank">📅 01:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRC4SOU0PmGy-4BpY8AjmfnbAByGIc3BGdtVrCUBWkxANOZ6lEibJ5NL56eHZV4a3yXwUOtIWug8eip6GmX2ysDlR8TYoPyoXqWzJqGzF-Upv1w1r5HYvM3dp31DfpiG2Zpzs2M6Q2XRvEMg2gBLsH6ai1dV7BYRgRgwWS6xpLsGRGH-qEtStieU9vCWcZ5qFllVdSzsahqBuzWqTC3xnfTGkzb3FkQkp2w8y2ITgmdQEEpGUt5vrYHgxLsZDG_gus1J1dcq1NdY62n5R1nHcxVex_lFminPRmYXqN8M5ImZmeckiu6wxAmGDWOn717CXLEDiWzcRbPdFNFomLIhhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از تقابل حساس سلسائو با یاران اسکات مک‌تامینی تا جدال ژرمن‌ها با اکوادور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24257" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8rd1PYY00AZRnIwoEVgzPdlksyj5yYyTBX-CGytz5rClmkD6pZ3kbVkH8rUscLwz-4zN5m1YvWOkUvF52cN9CftqbzlSV-RVt98wjQG_sJCdbTvkW8wjlWsZQkA4Ug1qa0kshWj91aVQHWP50-xVnZRHG5R36rbTLIopQeN92aM4PkqJntcHb94mwrxLhpgKbiTRgnYgtrmPC5AK1cSfh9SuTICYHvk0hK1FNXP0w3iJ46Ea5XaSioNbIh1q4JlGEdCfKmA6BrkCCrfEC3dtPwdtHkF6OE2TAjiXoXABwy_O_bunb6ix-XW3fC5TLkHzIKLvKydFRpVsCTTtq5eog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌یاران لوکا مودریچ برابر پاناما تا صعودچهار تیم کلمبیا، سوئیس، کانادا و بوسنی به دور حذفی رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24256" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24254">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEhgHcHr-UUv4uKG2L5yZRtbv5yR01KjkBGql4tgWc3YAd19hIh8D03Eu-1owrZ4ES9oY0KWp0Iolb9nBDePlM7mIle_4KwC0rkCY9VS9xlOWTpqLnOsYVM2U1nuLANAPVxm91P4IBWTa2znCgN0sFXAvklfyiNtbj7B_j7zb3GbHvY5_Mh1HJqQJIqEM9pDYB979I1FwcKI35ij5hsMU-g0SzWE-OikgQuRswxELzQqQwkBHyT1OoLGVMeNO5gCOnTQuBM4KbjCgzVCdMUd7QxOjNHI3w55fDIiU3Bc4sQRuHQUqV_iaIWCx2BFgYNryLGEHcSaktOBpGKdp1tbcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZS9TUxCOuYIheuvDtjcURr_Vp-S85IRIbPz5ivXYfrmkmhi4lMXplN5WXne597KXdGEe5mi8QWif94MJwiy3jw_9Jo2vXEB-hAZJOUsmm0UNWIZwrs6RrJGzcAMHfnQeYfK2lJrrF7ky6oLU_9MqIwE6yo_4IQXJzQv5BwUXLY0u8f79PXibzN82tksBWQPQ96Z4e8OU_5QDEJMzapIOO_FV8AoPiKx2od9dRskN-5KyrjA791AmigZtHnXPXqNsOGrls1CFLgQhj41jVGPnR_neDdsQy4BiQBJVaxO6cBl8DKG_qGcqWPwyh__7ZCqvPJcVE4eSjAS5wp_zxcGg9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر گابریل مارتینی ستاره تیم ملی برزیل که آماده دیدار امشب مقابل اسکاتلنده. جالبههه بدونید که همسر مارتینی پزشکان زنان است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24254" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb9UDNfryOxWpE6pj9MAk4cRUNuQuNDEyzcxgDHwAamyXaw0NlblDGxxpxnUUwxoLu8IYzXso1M0WHnB0aAReJA3TbZ1V4but_PlAR-ZolGJBalO9FBEs4ORJI1JGhXfG11QDJDu3IReAW0PqXKLuG8Jeg-8n-msBBH_PTetIFzhSuy7y-wHNpVFU5ggS9I-aVu-KIhV1DJsYiMy8E5QSvh9n5DYB_pSqlw4SVMxJ1CAjKoVtOhK7nbka4TNft4gmgx84Ki26WLC6kvFYmwtZQzYf4Xo9u4PddL6ddl2jBwBzbHzqJvC2V-g2REhITg09W4WDYEHXFcwGTi4PjcnVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24253" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP2bP2XoOEYCR7wun7Pg1G5oxtMjzBVlDgc5veBlegtwIkYfIJmHgVKBQRAGjajn3HiNc6j2oLmvr3mWzlFti3acVCLl-bb-T2AY-_NBPbqx625MPfrZNRKYCz-VTCAGbXLs11LK1y8ZooSIHutW9UtMs8uaQ91YkbOfKcoWkiDtuR9_ztMYTkrdyedvVO7f11BP91QF4wvrL4IbRZNkli5GdfeyddA0fg5nEz-jnKzZYa2IEhiLYT-Oen024d28cJP3nxSSs-Vyn7lLzogd_YaLXq-KKgo4m-YCP7ZytKn1DdemljbF89UlS0Eibsu7m39exnnH0yXuBO6xzLDoYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی برای دیدار با فرانسه؛ ساعت 22:00 از پرشیانا سه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24251" target="_blank">📅 00:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8ZOqjX9g-Xgh2WMJaBdBhfenoZhvo5WgEWctPUj-j7PhnRFN0QLi_1uzt1zdClApE8KV3Kp_gf6055UbzQDbgJMSC8TKQ7eDJPl56MhFO4eYZ0T3y4oC3KYKF6RXwwKmJfVUYhWyUk2rU0jG3_KatKVa2nFj8ugSUy4AsOwJ1MUm3gYY9YA3kZMKX8kz3oRQuM6r_YS904g5NjypIz5eQbXA0Gym-FZ2j8ecLdzDlwITaCP52_hm5UuFosHXW3kZTwWu_TBXLIogltktzPfd7LybvWEvV9FJLEF5dA_IdO6NvbFVbZvb0pZG0epBJ_YdBrupX6ogW4dvsPiQhOyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌جهانی2026؛ شماتیک‌ترکیب تیم ملی برزیل برای‌دیدارمقابل اسکاتلند؛ ساعت 01:30
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24250" target="_blank">📅 00:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOmL3rVs0ldBS4CvXOUDn6o9Lx-KJ44bhnimxI4Iv7zPZyVVJeNbrMPqqEXYZSxqy4Wjj0hgCSFVwCUlDDdwup6g8ePSDtpBiP4KebGml0c6sPR1haZtAXA10RY_OBongfveF0hQzesHNdI_1c0G7-BHgPZMXt_44V5R9ueyV4OR0qQ3c40RldIfn8_B2PVeiuitAJ8BAIWg7AzDr8jb3XPUXPKPh7JmuG-Gzk92E6h778v8idgo9Fa_tSNqkHNmMb-0LEAaS9BwnXE_9a1SdTjA7EbvQuYdGPYLG3olLJL7wgEsAeICsUf8WwxDXyFSkTVZDS_8mCJblJick9rKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24249" target="_blank">📅 00:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=bKbXtwbNBwEYcOiL8Uo7--yi4fwHvYWMb0E5lGKV9l-pRf-dG9x7s58HsFh-YLAhhSiROBjvgQkhFx_9u5910tW88sNIY6dPEkh28P2U6BE1YsN91eFuj9Z-AXZS9jX-ZaBx8T_pvgJ8KR6Q0nym2U_b8aofAHTDpAmJKCN0TIU_cSMl0dc-srh6EcRkTF3XsQifisWRB0xhVFAQs8ILvQx8V--M5CYwRuL2wEc9hjR3RdAbsEW-0Ihz64SuHRD6VdufY_qqBY0weE4WM84Of694Lq7yQV5OTEgIXQshLMTc4xLwLSqHy7kg0CaHGLGdUOLpqIdJvyFaaGqP_9ZQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=bKbXtwbNBwEYcOiL8Uo7--yi4fwHvYWMb0E5lGKV9l-pRf-dG9x7s58HsFh-YLAhhSiROBjvgQkhFx_9u5910tW88sNIY6dPEkh28P2U6BE1YsN91eFuj9Z-AXZS9jX-ZaBx8T_pvgJ8KR6Q0nym2U_b8aofAHTDpAmJKCN0TIU_cSMl0dc-srh6EcRkTF3XsQifisWRB0xhVFAQs8ILvQx8V--M5CYwRuL2wEc9hjR3RdAbsEW-0Ihz64SuHRD6VdufY_qqBY0weE4WM84Of694Lq7yQV5OTEgIXQshLMTc4xLwLSqHy7kg0CaHGLGdUOLpqIdJvyFaaGqP_9ZQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏میگویند کیروش باعث‌شد فوتبال‌ما تدافعی شود. مگر قبل از کیروش فوتبال ایران چه آش دهن‌ سوزی بود که نگران دفاعی‌ شدنش هستید ؟ تیمی که حتی دو دوره متوالی نمی‌توانست به جام جهانی برود و در گروهی مقدماتی‌جام‌جهانی ۲۰۱۰ پایین‌تراز کره شمالی و عربستان قرارداشت…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24248" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO-pbZitB5KfhrEJTv4Lktz9kIZ8Hi2E8JH_RlZ7HHNhRKASTGoZe16HsGnzU8JZxxytKTAMDeaw4ntOg86wk7w7PatGH19r6OSk8vi5gH_f9da8dBcqrVQQf37qGVajsMG_J4QgBzJMTIgt2ab6tuIljPd_7X0CHmMEcPUycKrR0oQP_ITQqekjLZbeReNpOa2x9CRID29a8FCCQlNogsDAuW3iRmI2Rcc5c98M-Q73BYURTpF5l1_Qv4eEcKdvq-gWXXet36DllDOB8yi8GEMesDI0TXuhYtnBRTfppgjK_GNZrSVqN4hgbt-pZxYapPGWATasSwxxeLOEQjVWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با اعلام کادرپزشکی تیم ملی برزیل؛ نیمار جونیور از هفته سوم جام جهانی میتونه برای سلسائو به میدان بره و مقابل اسکاتلند بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24247" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
