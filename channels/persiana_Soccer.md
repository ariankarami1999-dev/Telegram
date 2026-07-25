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
<img src="https://cdn4.telesco.pe/file/OcA9oU9QPTndMhxsxWOTHCWJ3bZrVdUZ5TrO6Hw4XQysfrmOCnhntcXrMhTkC6Fl8wbodEgL7Y3hExvjtJQ7lbIqUG6pFNOmGNHc6XsEIAB4pwJ5O3BCBAt63X5crSFWwIYWVrRFSaqf4PpuTSsRWEoGEx_-a8P2_8Wds8A3i-NK-5PBaDrUfV_KgBRohoSK3jbOnushSuB2yj-7chp7JqIX5m1UtKsS27Xg7igjtHL3GTk3x8NdAkj3N63LukTd0Uiinz3lSpWvSq1BtPe_2RVkXQhkSs9DeIsSIHX_H76QA9UShyZEQgC3qSLJ2c4_TWAVajQQpAnGxH-QRHMDUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 579K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 20:23:49</div>
<hr>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=o-Re4m_9W39m_LncqgU9TdQwVXy5sILYvpYb90dlWZZbsUkgWAxplhb0WD-D0HnRwqUm3EDAt1GSN2A_TNEq5dZkCGRz16HXeOR2rwLlIpYVk_aLUzwUDDbZGcNhj8UhP6G_b4yuK1i-0GYNWA9PjjsZUVb-rd_-fLE0QuNMGrwAug2Lh-5VTbByeKe0WU5y39tcMpE55TYICQUVFCyv6SjxStRSlzzIgM-2HBHFmx8ij5nWrlx0dXMtJmMiERAeSWHGlHSEcRFuOYMD2buoHrTkQrob4_UcSifUYd24ud1lrJ0FxhcEaiNwM_j42oABz_7UVUpu7EKDi_Ugp0qWaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=o-Re4m_9W39m_LncqgU9TdQwVXy5sILYvpYb90dlWZZbsUkgWAxplhb0WD-D0HnRwqUm3EDAt1GSN2A_TNEq5dZkCGRz16HXeOR2rwLlIpYVk_aLUzwUDDbZGcNhj8UhP6G_b4yuK1i-0GYNWA9PjjsZUVb-rd_-fLE0QuNMGrwAug2Lh-5VTbByeKe0WU5y39tcMpE55TYICQUVFCyv6SjxStRSlzzIgM-2HBHFmx8ij5nWrlx0dXMtJmMiERAeSWHGlHSEcRFuOYMD2buoHrTkQrob4_UcSifUYd24ud1lrJ0FxhcEaiNwM_j42oABz_7UVUpu7EKDi_Ugp0qWaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SulGdjBtJZGT-dbk2TpKEfARxiY5n_5edD5baP_0KdXpPpkrPy0C7xTyGlbSCB1OfqUjZbedeNXHS6w1LwZe9kWzzII5skV4q4gYukPGjCn6YjsYMP1qC_-n3Zmo6J2Ow6LEVIbNv2BFi__jANBU2LPzNWBD6_SSl1dkpUOLe2PWueXoRwT33Kv2Asgdf8e80e3dpE29MEZJ5b5WecjXECjLiKj3k7VVpvEKdaXMPhbwdxjoQOkWpzAtzgjUHN3cLzfdr15cOF9cKblysws-KJF_oXHL4P_q0gb3NXukt0_M2isyhROdCoQ8CVTEja_QVAg56ApsTNcBBgOqdwpuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO9Zxj2k3c-u9A3MD5o8CW1a_I89bVFDRe0LO3kmO_T2UHbcYCJ14dculspSOtdEpvZuuyrIaiTKpqzNvF9MF5MpXTWyzw0aPpwcBNRrp49uA3HTUwOwiuRFJLdkeBxSAWNNv92QBLZD15hBQFkFyDg7zfPKhtA2mBuLNcT6N1D8W9VZoRxm1V0G7LcbxMSQXzsP26EqVKbthvKW1c8y8bkUzQJGXmYnyifbEwrJ1vIn5QNv7jbDNUZkB8tLoDsimYMTPcfZ5hgbG0KdPz61zXs50u9MFNlAwhTaa0ivrJKEGNyKOixj6jM2QfBtzBBtN6AAUJ8jwhDBKeGRsIXP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1erqe78W6G_ORauvCB4ZcA05hxQCB-MxGvTlXu7ddHa1FnjdoWHkv6MrI0AZMrYJQPqjxRO7kRbwX_7Zr3g6YivNDyoG1mUnUS_Gj2tBvG2V1p48kJ4IWqqj8NjCZSuIrS-8dfHtIPvGjS4WMVT_MeY0snwlcORTXYYGdzA0bDwWSBSoPH6UBLT68fCjkJc6PxTFCfM5rxQI11mMK9GHgfMbiNQrSSLm3oLKjwPulVNuqVZKjVtTaYqEcUiqYCfL8FivSullOegaQDKzSAvQc0ExvT8IIi21vNllo3UfQ8UD0_SE4EppzCa9hfTg3OKV9nJUjUQKNRWho87m39gIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=GiG1vjp0X-eVttawzZ06LMbhWVcjKc8lUtfGkcPlAx-GC2mxXK0Fk0GNK5x73AWdsxZpQXE3JWCBx3zF87C1Nrqx2AQF0-wvbC_E4Bo0Z7GSumOCcM4LRy1_ga2a2PBoKcFKyyuHvxxx-F9BlMy4vUI0IThg6pfyufs2kooYoFSfD7C4Ynd8iTp1drFTJnGplvpicHWV88LeEmS8blq6qA3PuZk7gHbZ2cay0V_V9IVbbq_g5UbouZRUV8tUF9XW6agmRKPZLg6KUf4ysG8tuQ7uRLb9BtCsXUZxKTj8xoG-j3IbzA0dqRkT1IYD5HoIsBGej6l6J5eCvw4n0pz0XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=GiG1vjp0X-eVttawzZ06LMbhWVcjKc8lUtfGkcPlAx-GC2mxXK0Fk0GNK5x73AWdsxZpQXE3JWCBx3zF87C1Nrqx2AQF0-wvbC_E4Bo0Z7GSumOCcM4LRy1_ga2a2PBoKcFKyyuHvxxx-F9BlMy4vUI0IThg6pfyufs2kooYoFSfD7C4Ynd8iTp1drFTJnGplvpicHWV88LeEmS8blq6qA3PuZk7gHbZ2cay0V_V9IVbbq_g5UbouZRUV8tUF9XW6agmRKPZLg6KUf4ysG8tuQ7uRLb9BtCsXUZxKTj8xoG-j3IbzA0dqRkT1IYD5HoIsBGej6l6J5eCvw4n0pz0XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Od7TfafBQCPLRPITJaJVJ7u9S1iTRXUYJFnVP4FNd7HvCC9bGksI-kXEsEdZpqafwe4hrSt22OTwdvFaPoP46xdIGlqanrGmgIYa9wU1f73G4JtTW3o4VNyTvdWj8YI6g3RjzBKpxT_-DQ0I_dffb21PJf0oD0cTwwMzmrgI4iwgpNJoOnqjbCA5bsYoh77j_vzQdzs8tWq2a-nsFLmJJOZKwe5eGNndrRNzFtEms0MxHonZZ177CvWK_RcBV01Ti11HmaZn3O6-QG8J-qaMh6-bc1TPJBjg56oQqInuk8tPmeeL2oo06GzLkcfHP3DOzTf1whswEYeGuxAIBGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=lvafbe6AtVXiyT44tiQpCo1HnFwfdF1nnTKSEgV3oX-NdcPxmnnaPMCzmKmbvCbmM5aEF9CtpMZU1-PFJNELIdoPD0bEQMJUCvROM8_cJBKvIX6EbTpb2_S1KIKhUkkk5TPeWrEqTGK6cMKaG7jeeF7tXBfUnK3lnM_DlDLSJxLA-AGjvGoij3-fxpFotNkmNPolkTnA_aMBaFrn3hP6s_x56kHacDq2sUdGL6vQTCBiFVq8OLQejhmt7Qjs3EIVxIPRip2yY5qd-mX3nfzHkJYcFN5z1on6vdGQf4fLGT5SRALXNZuw3kSaSOxZdadyfUxiYhAoOEZuKyTrqpmbug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=lvafbe6AtVXiyT44tiQpCo1HnFwfdF1nnTKSEgV3oX-NdcPxmnnaPMCzmKmbvCbmM5aEF9CtpMZU1-PFJNELIdoPD0bEQMJUCvROM8_cJBKvIX6EbTpb2_S1KIKhUkkk5TPeWrEqTGK6cMKaG7jeeF7tXBfUnK3lnM_DlDLSJxLA-AGjvGoij3-fxpFotNkmNPolkTnA_aMBaFrn3hP6s_x56kHacDq2sUdGL6vQTCBiFVq8OLQejhmt7Qjs3EIVxIPRip2yY5qd-mX3nfzHkJYcFN5z1on6vdGQf4fLGT5SRALXNZuw3kSaSOxZdadyfUxiYhAoOEZuKyTrqpmbug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFVeChk_tbt1rW1DMKy8DA8-ROGHsfLvfLd1UoKpEoFIuyo8pCJgT5Alg1TPjmp0x48AYMoiRkoMMuWiQ1AUQKchk9p06P1U-jF56FJn63t5j9xug5733vxEF1aAHHttVWcMMPVfKd3fdBmn4_cJzddKW-muzHooCHAVFh5utHhnZmob5A9vP-iBTJz9TtwzmNjp09OyhzMhglXjvsEoqp14i5YFC-Jq1EsbCQ3yEpXcgKLnzimLm2au-qCQ0Eucy_IEICmlb0_RbzrTEwVB693dpTHRVUYevk6pJ-6XTTpjswtZkIohFATHuS8yVCnET_4pkKSyWLVs6QRutAvjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAfoVNjNxP-MWO95EAXRuA74No1AcdWwLTy1IStmC-lUy4514lpuDEBbu8GzY5vSOvwIY-aAwRB6VQueCTwITqcJWpLxuCKC6WQIVzw5sd7tR3tEi3tposNQXcowkX9ceeSew9TkivSbBpF4kt9L1u8Oa4HJuZEOtcRL16xU4_sYHNtZxipLBg1BdfeAmWOPY7lseohkvYUnMycbsqkrS6PbNi44ivs415bMRVSNKu4JoQIgbKWuz6yNqAK7Rpxd9XIPsPD3yYDnjjymusEjLoPBE2iVvXxFvWXadrJPF8anHA8sHPTMAIRBSvK6nBFoWnFYYaNmq7Wf5wSiphvljw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZ0mAM34qD0JIZjC9tOfeS20LwlV0qCRHiSmFbPNXIAs5AzZdrlNHoJADHEPKBZkeufEM3-bVPNokQLoUPu64R7jUFAdJmkqSd6b-jSKGOxqAQ8yIEQfEGcD6PsRwOsqIZZ2LjfmLmz_gowrx4ZooEl6tftSgQZVd9l2rZQZAiDFCfPtA0Py5yHDqsBcNAmuuXKc5NAyrAuz2hwzyFoHlj2K_3ZBA91mbvmBZVQtIq9pob81DpJPIFx0M2OFFz_TIJIouUkAPnKvaWRf1u9CKKPD35h6marc_Vx50GL8YOmCm1FV2ZliMxmXdt6r7eN0m8RNRypla4akPDStYcBr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtzEJjAiadBkpOk8hRdA6hZGwiwkarDFR8lkr-rD50Yo4rT7ZrJIOUp21mm2EmUGowpIw9-VcDXFHirBnen7-FVsyYsJzJH42qujPr93_TdsTd-XreZPaERKA9zM0SRM08hAtKasTD9SalHKkFoJkbbShs0t-zjopG0WzO9dChEXWVCKHqXopFeuuujPBXUNwPJV5JdwZZ6-5-Thas-5iwFjNmq_n9WsRDKh7jsVLyflNOnYOVTsKjmwpE6kHXQ7IGcSJgnxQxgALMsWAFwPFf6SRaXGAF78wRL0u-1jcV10if-yQTvSWG2T5hETjBfusPymsSpr7Ey4Wh8xU3KqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOXLtSgqp4ybD3AV_clKvbcObNgJav8X9Trof0v7_wDrRIdeBpQntfYHLyLkr6g3F-8OEua39YYtH-Pboa8QaT9RGscMJpcgSVhuz8QLB6qpmf8dOEwuP8RbUjPO-pu6hHSOJ4uUwvoiSrgMtnZOz-ZDhAM4aOJsN_cxw8B-aR9Wy6rVwRSxBVMW0wMSfkVkyz83MVMvds89M-nyTtQnwy9gBTI7WasW9t49YnfnwECNQTBhvfMJAipHi7tQaf8g9ibamqY6HJn-VNm3c1oOx45s-HOc6y6qkWO5krALbs6t6-k7mk5KRned-3UcQ9yN4JAuml0bliLaAZnVMHbR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGwPAMJrT6AIQHZgd_0WC4i435eeJGPLoQzkJfO4Nqh83xoKHAl-BdEaU6CTynd6lKbT6dIZtxCCiEss-NHAImhCmT50zBzNeZCvAQAI8kVnJNtXZQg3pJvaRfeUeGkwz0RnUq1z6Ii5YyP10U2HXcejYREuqur1yn510jQXjNrS7weToDODtabNoSxtXK_bEyyYxL1hlW7pV6xeXsvADWjnSNKCD8sdPlu8Sl9FXMx0yxT-ODL35NA1VB49VnghqH43mjOulBAfPQbago7f88F5L-UrbnuL8Ss60gAHukK0jEV3f-mLO231HAZWeqDfNYpKolyrgaoSqUcs3KzJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O73KE9PPDl3Xx3AKvf1oISzfhWL8H-yVAcM_QdH1UDE1WdZ1mPfWl0OGfs6rtoUpBlkIdKq1CrDFzVMdgzArZJoOnPo1BBOU-BC4E77Wvw6FFy02ur58HrREEMkyT-2oF0iN8yLhM1He51xMO0xhbdcS-QCAY97LF_5FBCHMJDyrtKeSG-HgIvDasfO1XqH_UNy_bVV4Oq-e3d-jyp5t6Js6BD3K6gMvsMgb2Pw7VsNhQvIBxUrgDjK-o0qmT9E3VUb25A4Q9KsSW6fGrsNeBrQmYnyN-YjwF9nHWwJzLuM22m4n-XcTnGAaa6y2X0DN3uYVDjcAltJfVLJtP8vymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDLPVC98ZNwTtNXzH75lgVpMy5yX0TwIOaaci856vj5RxxIDVnYiICmsPW_s_NAKOW79YSVCKMHXywYljyKlrzuQCPtUQ96yzVXymwue6zFAIRRHZ-er7VBZU4u1z3gtCVp4sj6IsdJVFtzFdYwJplmc0dQ2kfPDctPqtcb9I6GdK99FYauJp_tQf9vPQ1Vr_8MmsBBmbsyoJBnDBrSvul2dN7PQQk13OOPECmAk1okhB1emFzIgCBydrn-sWTZswolXXKn9lBSHk2cXxOODsUzCmrRBKmrQb7f83HRpHaWtSI9YiY3TVBto3fSXr5kb2D2LlJ-M0XT4-_5JNVwURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=t5GeoDEKaWEZqC6WApn6FQFvLJQRfp0TnfbiSPqZGHcVKE-m00OOtmLiKZFBV4i6H4AwEqoXV4I6-6QQA6hc6723Zunk-ad6CFvn4R0NZkwzkYBydzFCq78GPkEnMg9ApVkuayyoymPJNuqKwvqLEPJyaqzaa3gPD0ogXnvqt9K06U_cwIR5pj0LWjjqplVUFyb-31AurEVzTn-AXQ3JgML3B1qMu9iURtrzpXRXoWo0_m8jtF5WnBhatU-6qKby__zGwMuWLYKEZSFSd0Z5lM_xeLs_IRFQJpd_sKM2Opg1hStDY8SV1loaKMkkFh7r52Bfaip_pUTD7bd2mmvWbCsQh4JGm4FUICoRznMLdj2HsDAC34Ep-AWeF54geb7XvGcA_PSBvzoeYPLu-b23ahg2ZyNuJr3GYpHL6SFXyzjGIzOXVlSNnIsRqAjJa5dwHhkCIPDrfE7MMi-GXbtJLi_LefoIfVU9UmFkkHlyw9O5IVzO3v6xDZhP6oIpvt3ELrD3LOROugih-Fu8ia0ji8kqJooB1B6VdUkQYJAWz90_6z_PtFddtMf407gsigs9br7uRJIuGFgWwlMOckht1-rfw-htdO-oZJ-7pRFcU9GFDRk1ID-RMvCUAPXC-CLcs4dvXbhtWi0v3td3gGGc27yPABCl-qsUNHclkT0NJ_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=t5GeoDEKaWEZqC6WApn6FQFvLJQRfp0TnfbiSPqZGHcVKE-m00OOtmLiKZFBV4i6H4AwEqoXV4I6-6QQA6hc6723Zunk-ad6CFvn4R0NZkwzkYBydzFCq78GPkEnMg9ApVkuayyoymPJNuqKwvqLEPJyaqzaa3gPD0ogXnvqt9K06U_cwIR5pj0LWjjqplVUFyb-31AurEVzTn-AXQ3JgML3B1qMu9iURtrzpXRXoWo0_m8jtF5WnBhatU-6qKby__zGwMuWLYKEZSFSd0Z5lM_xeLs_IRFQJpd_sKM2Opg1hStDY8SV1loaKMkkFh7r52Bfaip_pUTD7bd2mmvWbCsQh4JGm4FUICoRznMLdj2HsDAC34Ep-AWeF54geb7XvGcA_PSBvzoeYPLu-b23ahg2ZyNuJr3GYpHL6SFXyzjGIzOXVlSNnIsRqAjJa5dwHhkCIPDrfE7MMi-GXbtJLi_LefoIfVU9UmFkkHlyw9O5IVzO3v6xDZhP6oIpvt3ELrD3LOROugih-Fu8ia0ji8kqJooB1B6VdUkQYJAWz90_6z_PtFddtMf407gsigs9br7uRJIuGFgWwlMOckht1-rfw-htdO-oZJ-7pRFcU9GFDRk1ID-RMvCUAPXC-CLcs4dvXbhtWi0v3td3gGGc27yPABCl-qsUNHclkT0NJ_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCaudgXtynWKcDVwQO_cIO5I1hjYsD484YXmKZDRpg4OSOARDa306XLo1eW2DHEtiI6TNGfp7ojUbCRDlp788aFNt0OMK-AkLW4ylAkBNraUmPaAcNiF8zPa5qJd2MRFc5QqZwUi-aK2JjuRZUBNDupPVFeloQWskIq_UZMlnVQm4_5nT2O1-3M0xhqxKwdsMZk_Hom8ddtNewPJknLE1ri9tfpddb3jlDEhGWxZ-aRz_Q18L18nWKRzJhpu9PA3_UfkxCEJhTFD7BzXMJDbJIdxEeUrfKwatvqUr7W56w4RdQP66aHH1EmhVNHSzo18Hnti1T9PEJ5CxZ8v-vYNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngZRunwYAgj53xfMLjTo5zJCfZQHRPW1LTmI4vGqU1diYYx1umkKyFCXGQcqKLFfmFiAwpS7dDrFxuJuEEHIJvIrk7c7LwRZnjSfSuFMbeICo9sMB1DTXsPT3Gu0zb7aizg0YLeCVl1pGK7VHteO58-g0Vfz_VUNdwNoT-ZEff8bUeoha7l9QqOcjITQPNQJGZ0ecE-3H7MruodE1sayjo1LPF1BW-e1grfudt1QnyP6G8uxcyNpVWTFSgR0iUou2G3CoXQt_u7yX0mCHulc2493RdMTDh0_YiAe6eTgiTi7dLv-V6p0xEg3I2pIPlYyrQINbQI7gh39_hW_sV9I-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMR_GBF57Tm2NAL5eIXx-GpiK37_hwI02DPel3SWCi5bigbduPcVFYEpnsPAHf8MY7qxaFpxeYJoFWHze3URBbiOlTqROVvMnqj6gbH22EZIYTzWHuBvDbXws7DTE6Dk7Isr5fUyzlycKIU3nq_9N5U5Wjzbu8GbNcYlKeHiNdec-6NTqTXhMu0_TS7sXP-q7ePQcoeWUVdtdTjjVorXF-IHKntkbd-tsP8x_IB1RZQAwEA16Sb8U0WMVWft3Ara2jhiHIoBN1B8Mo7VHzDRx18CVBRwhzp1Eyn46QgAlqYUArijYFgwVpFXy7ghI9jK0X2YVCyO_AKAYveDdlLTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTgbXyh4McUZxwdUtiV1erqQTVGDgM8BK07xBDhJ_kZWmwKhia5mt3lfMHhItXU7c1jcz-SICBtI3kUHv-FTQ-7t_nA5GmCVi8JaBMF0fuwnk20YlLlUdOnBH85Q-d6g1lR7itftdZX0SNqo3ITj239g3ywca8y5xoZSdcR3qu1YlwyIhvg-mMIMDd-bEFrJADNOBV-oBKLJwTjlbG2VwCLbSKEl-xRCsfNAtUy7x0FXoBvNNu1GMoccP1J0mflt1HjRb9PF-lGhiOjY_2iZjLTaWq_bZB_bj8yAtXf6Cau6DJDG3drY_D5CX3mlxtDMy7sGU0eG1mNZkWo9jG4aiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUYfEkWxnUQHGMD04LFPT8jOyn6n5Hk7solEEoaHOE_4PzpNMOKQ6fakciqHmvNTGSOrgLAgLyi9HFPEnDYMK-3PpgKle4OlvTG30FU0XwTE8TCGHqip4FMI_BYxdj_189rk8TToWskJQAR9QAyWC_F5OHUgDLe4c4hxWxqs88XP2maWjejoebE4xRtwMKXXZJPGS-nB7_G_r3HAgzmRBHO3tt4HdUJQQ59KbUR1BRd34AYz-Nvo04Wr6mz6LmAYfBvzsfXH7Js2JwV8ytJnWPo3cgFfGz1n6C_jBRL3wBtkyqTt5L0X-0YDA9yNobM-1D4m_RO0-JHh4EVd9yB4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrlnVviZUO5-hDgEniXVnLwSoeT2GiL7x9KhN9bnY5SXs1FaXYsk4smpqQmRIE1YfqAsEh5NdGEI_0RIOTytTqBUwdEgbLfRtg2_4U3vyXLVkA3jI8Fe7a0aXNrmOPU0JfAEHiQcFPUgxVlE39rGFL11wGiLyk5Zo45UeedAHfPHRshD3qq-2wLrDAWi-zm-6CHPeci9emvQS0HSF-qqRRfQqooehx88G_OTS3sVUonl2u_XouO4GWHGtVOZkre_lLPfkaLYiXhllR1UqwpHUQfuIaNOiRrLtQyxvJM7OCimLqHHR-M1q8jQWeT5D-V4PCFdSylGIozJYUi1dakERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=ZyT0XyfgY7NwJO3YgRAwnGIFLebDlsm44sxECzz1XQU_Np_yjshifYXOze_Btl-D2jidGIROgg6By-ALP1F5S7yb72w8LynE2L7AJGoKjl_fox7s62WzdEjsMWCSaAWZ8NPd2mZ29-DpYUZ5zmMLh5g8vq2dle1wtoISzAq3XeKqVysoQ4SwtZHwXnQAVg_q88wALXt6i0g3CtLyKYibFbD1If0s2z5CZfzm_yi6wIKRwxWVqO1Ki0CU440x-AlXhZiGsRDGcV8zOnMABy2STMtp5Bw3VhK-C2_nlBD-FyTbIS3EvdMjNbShepcJmyadBuuobOX-pa-cOqfxef7LrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=ZyT0XyfgY7NwJO3YgRAwnGIFLebDlsm44sxECzz1XQU_Np_yjshifYXOze_Btl-D2jidGIROgg6By-ALP1F5S7yb72w8LynE2L7AJGoKjl_fox7s62WzdEjsMWCSaAWZ8NPd2mZ29-DpYUZ5zmMLh5g8vq2dle1wtoISzAq3XeKqVysoQ4SwtZHwXnQAVg_q88wALXt6i0g3CtLyKYibFbD1If0s2z5CZfzm_yi6wIKRwxWVqO1Ki0CU440x-AlXhZiGsRDGcV8zOnMABy2STMtp5Bw3VhK-C2_nlBD-FyTbIS3EvdMjNbShepcJmyadBuuobOX-pa-cOqfxef7LrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpUYEmSfCaVfShvj7MY4lzM3MNMlhNawqrHMYq852nAChqa5_AGT-LTin22OXYCA_lczTaruOcZzWIHnIjZpqSuHeRADS85BJJZJYMgNepBRv37GgmM0Cy_J53BcScznmA1yYyxy4WCDG46fJwIhNFwL190NFeEifLDEYwy6aUMr3Lu4pqJiMUa0dRreOQX4-k5F2TrvjZDRFe2i3mNyv2LJZHZ087_9vHVgjiUJ7r-cYwbJQIJhYIPuE2n77ZPj3lwYOX77Xmu1Jyi5O3-mBlvGWnN8ToLfn-YSqvbKwxU4bQsePlcNecyu4JFEAqW20dkgDTc5gGBWieJLMXLc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzwrVS5N1D0zkmqsFYaCT1kCdo1-yDMPX9PBpYs2YllicPT4otye9aWm8yComBYLpvscvFhm9Ng3pgjfFVPK3CWTVoEPNdaGN9RrVtteWCZC7sRC_H1Zc4sogyiPBVIhMh_2HTdxKT-FUx8kB-TVqCIL9MPHQ7J-LJ2CeKOlJ8VK1bTzrhar1D5DiPOWqgMu0-m0NbhCYXcWYlu5-RP5xZYZRd0JfdSt2j_m1XYZqhJJXZCU7r--zx4IvTYNWN_jy1Oe6ADMtfQwruZy7w47kp7MYF5qezLXPzIM16hZLON69MuIuCkWUuMv6V9Dbb9W0QnWsWstiwKRqDVuwlUQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIudNl8W9BqEaVz9ho9w62MBe4hIDS4umtz3IvOJ7a9Cwe4d6DCCv5ffiiNPYubJm8l5LSib0cWgl8G-ZfVVweKf85IhrnpX1yw4B9OvwLA5JNQqBC5fhCOfdt4s3mu-HoHeRQva5gv2P3hmOmGd9jB21TQ-pmk6GudXA9NcfIbsnIafmHWAtGC3of6QCBVsI6-CxluT9GXQB9Lz7bTWXAR91-YCo2UZFtU8ho744SE1tgkrAg-kxxf7tuXQB2qreX1ErTvUCewqVDGlXOUZfHPsiUFFF6_2uE86DoGy866Kh4chaNOC3w5uquC_Po0qsM3AwEMciR-4D1jUnF74ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXQ-b2P8x_sm_wp-etQcdMJuPH6o49YVvh2wcQpSTtu7PygTBm3YtZ5fGZNyxMXI23o1Z4nKqsZoyg7lPP33XXr6GuXQ3TJ6JgR-5rARrmxXy6J2AlvDy6o4yAGg_p0s_gT3yOTvk166MmfKtz5n2vWs7sVR9y6YPVBU9RAwJI9Nc4z0WXwUP8aVUv5Zwg7V3K_hNe2UxNRg7dyKVzNzAox_RWuYhLkWVKGMrjhzjyDINg5AdR3s5tAw3y_mJACtBB1WQ88FVEM5Ys2s1W3Twe6aLyjiHKuzKP2ILyBz7Ln6FNo-9BOhI1P_e2aJTu9xyoq_aHmnmKYcb3alQtUaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcnPZsOixQe1vgqMH1-dv2moHeQjDB1Sh1yIoKvf9Z05leal180sVW7D5FQWpJUHkcwfzTWBMnW7o7A2jCVIFtbCFI5yQ-DlwIcMl8wqndkMrnNoLytQQA8EKIqJ1w_wxUBvI7pcWXkjNqF8V2f4hicZAgS8ANkDXSP0MZgqYQq6PDdJgYzBvOkqpBBTrOfT7dzViaK78u466uLIxHfKg80HmPqctiM2bUSLnpIlTHnbo4kR2P5fCCYw0f7hQ_Yo_h4GoMzfIHPUiWc2Qhiz5LhcD64CKxb4eWSoAjrAwdbIenjvXS8klWnpXAjBJkDQgm3-gVznssnrv-AfvNV15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on8YNcZOhsfs9aYlvmAzjEvhJX2xLrXmTkfGS35MvJQbetYu9DBFhWBbzVUaMtx6pEJHOoEZ0EHdi5j7ajbe7QTYoC5hhSIyKRv_iY2gUvaPsi_dRemOtPJ4Sg6yVEniMLvVWwcfhDaqNYkHdPon94wLfO-vUnYcvb1_uyJLAPp1JRXujc9duiWao3jVcSIqn9gsfZ3lGwcmVDUqs_kT3STy3hKlie3Fk2CWVlkcaWD5BK5O7_ygaKZCWB93A5quaLUoSBk6CSr6sCuvzsDYCh5q6LdoNhYiNEDv_vs-F2m0WTGHh-wyvn7E1TAy1_Yn-xzOSMcgayQLwywcuGoUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4cWZ3aNvKTovdK5wlJEtcUFMnFti411znMhfubyNZ0rmv5KltvMUj7AZ2Pomn8ziYfO47amy664yeClYtRNZ7jVzEu-vPmZ3bhhsD5PcCS5IOSfkjSgA9N8We6nuJ-IuXg1N61bmEZOtdESyh869RQSdi3EIDc_HdYh0Wc6bB2GoKTjt-hihZZxzbvc-gHj3rcn84Kmr1rzcyrnpEEn-dLYXi1m_8WudHYq1qA0uvN-SOSNsbzYYLIbpMcWxFrOeMulfG6LoBhD46iC2KZgSbiZN24UqYvb323f5CFHR3_7cB346wZoCJEJXKqbbA7ECt4g2WAyJXrGBl1g667Wfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhu32fQUsqr3aaTbqNhoxlZTBfE1NEh4i23a5uec7YFls1k_rpaSGAhrOsDiMzwkOBUcGS9m-gDG34zKBUE9cFXWRGjqjlExwBH0ChnCtHZDrsq2ljbWWTJQ7Gy7FlzHv7wpG52gbBrbPZEX2bl7UQhKPMeEwO-YvTeIXISORO6nyy8gSW2FOwxBm_1yK5XKAWCCm8N6U8m841h1eTVN3VOlqf-Xvk00DAbStpO5iyaBbip6T5CaVg7LJQUWbjFnX2dP97LW5-34gdm_L0cBo_pNdnpewcj0iqa_l0UWAjc5ypu-lcckdDv64I5wFNFv2MlXuQju4euS5QqhUwrQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwn37v3DdiJDyOkrVEzE7DZE9vGhIUi4kHMUgOIHA11nTAf2VpuBzdvo5T0Mu4Wj2JZwUcl0W4UTSYWqGwhvMRmYhOtLOUUMg81NIXAQwh9BwOpJMxmtZRYAqnaz0NMxNw2v0fzCw_YG4Of83-xCPoGmula7_ZKT50YJxP2R2Qv04E_I54yEuY1FmQFaCvJRBuiB_g1m28Aq2KfnsLlYcOECiGC6YjWJwnh3SZy6AHmXP2Dm9qzmU_VJ94ABAnBRJVRaEv8QjVMEznUNokwq8iDdY3Q3zeAYoecKEDbarQi8o8O4WBPreoi5tWpsb5b8fwRfhgV1hjQb3sDw3nFtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe2lWaQ_JE_LuZKxw3SCFSg6-lNNG72W6Lxx7jF8jsGXA-JkxiLC_vegZaEsn0UfTbQ2AqxKO8VKs0tsy4S91lNcLEppagjEdCDx9gE-eOFVooAijNVDgPtG44u_KAI23ATDzLVAVJTBHVpXWr33h_Ezdrhn2PFRMMXt7vN-5p5VorbpTN7t4glVKKIEzXwOBJWRDzJWxxhjDoCev-Z2nr9IcwqouXCvL_NhQ73S0z_E2aLXWy0qKekuIsbuD3BW5Go8Uiisjn2Mc8a6XyIl_9ypJZozPdsiXWgB49qWtys3JenGlrTPrRBnhjYNrvXdL2uQWQMGA1v7vfFDVeHU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=qYVOfYPOs1AJ-41iim8fQq4a1izP09pmvam79tKAGtdBsGqgNlqwjWLb3Yy0hobk3IwUEDxFSROQhmsjzHAPJaJObXJTyxWy3uoJg02_KBtPT6KvrhcepLDCVKsy1d658BYI-vw2rQGtAjcrXDymfdB8rxP9mv0pE92IpRZDVRLxhpNrfkju0o933J3ByYredyQetsD-j27zqAZK3ThxfPm2PjdzKk1oM8wGbtB4UOtx-o4zgqnaw-451pOR8eIDuUX826UaL9gJJ1nTuwrb-MI3zqBg-UkY9oHNULJsfBEi-NXNf1m9qqyZYCMl4ms0UXzGIWwKIMhGoahNRCXhrFp9j9BqeSQDeYomtyz7ERh63j_M_708YINrzMy_uYrONwKK7Fxow_F9IoqFRYCFD5crH2WhnQvbHk9lABu-sOiTwVCGes0LtyHHQfOCJn_aWtfJ5H2WO0Xy8tV_MoGOXI1MINWhVPNRqJQbY9_2V2ggw-Vvryd_C6J81AMAcPpRaE6dLCC1uXIDsRcfwn0WEi_aRVvWVIjK_QC2yqrjCYp98PGEuwE34pEfY1aF4fw1N1W0lA3O7m3oxKQI07kyahV96Cvge2_xdMfBOfUZqiaScUo2gGAODg5WNuSuBb8bFLVm3oLfu9qvjbJvbX1mjOhODdOcvWWmgxB3rMKCQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=qYVOfYPOs1AJ-41iim8fQq4a1izP09pmvam79tKAGtdBsGqgNlqwjWLb3Yy0hobk3IwUEDxFSROQhmsjzHAPJaJObXJTyxWy3uoJg02_KBtPT6KvrhcepLDCVKsy1d658BYI-vw2rQGtAjcrXDymfdB8rxP9mv0pE92IpRZDVRLxhpNrfkju0o933J3ByYredyQetsD-j27zqAZK3ThxfPm2PjdzKk1oM8wGbtB4UOtx-o4zgqnaw-451pOR8eIDuUX826UaL9gJJ1nTuwrb-MI3zqBg-UkY9oHNULJsfBEi-NXNf1m9qqyZYCMl4ms0UXzGIWwKIMhGoahNRCXhrFp9j9BqeSQDeYomtyz7ERh63j_M_708YINrzMy_uYrONwKK7Fxow_F9IoqFRYCFD5crH2WhnQvbHk9lABu-sOiTwVCGes0LtyHHQfOCJn_aWtfJ5H2WO0Xy8tV_MoGOXI1MINWhVPNRqJQbY9_2V2ggw-Vvryd_C6J81AMAcPpRaE6dLCC1uXIDsRcfwn0WEi_aRVvWVIjK_QC2yqrjCYp98PGEuwE34pEfY1aF4fw1N1W0lA3O7m3oxKQI07kyahV96Cvge2_xdMfBOfUZqiaScUo2gGAODg5WNuSuBb8bFLVm3oLfu9qvjbJvbX1mjOhODdOcvWWmgxB3rMKCQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad6BRmJzHYlamC7mTb4Jf2wjhavujf0jc6PXyQMvgH74ne2JqKQHCrH-cAcna8nH16BWdz8jPlsveLEKH69vSc6fdqlGGp_EoZMQtnbTwOOrY3myaetXOP5G8LErQ7PoBDfUIky9nfg1sBHOsDw8A4T9YQm1aYHfgSZYCnhRA3775ShiwEEt5_xB0fHQc3M1orK1mnxVgbEs0mQVgL1-EHw-fTjhm70UZX3YMsRuKL3yKHaCsZDZCfXNDdKnVoXGpSDEeDKse9LEfYvF51Pv1vDmV1pHANjHJUR9HjOpTgBndtVBoNyOlMZotmYZp33AO17Yzst6VxqAREamGInG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls3SXx8BBSPcU7ijYCAWZePjtV6vDbm7XKbCqRTXRwAZhDqhnkTWNqMdfpfSuxc0HcWTvajby__I09g81YghWpZcC2G47684je1Lrwxn2kvA4RDiOcbrXQCKuasqO2wMGUIGqqvt1yNmrXKqNhtYQi8t9p4ar5cEhNCXLOG34sND4YuwtljOspMGtXp5O44QulS47cjYsdHxnTGQBS45NNFjYyuFVbdaLc3MjtKsTfr1AgwRf8LjLwttAr1FP4uKFrJe9f36OVsLoyGLixU4H0_N1EdJj4jvVD9qvjBUUmpiPDbP8dC4HFweIpCj4pwJ-FeS0pAZgWYfEtTDhJXzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPxuzukzgnbhvy85Zi4T1xQyYUj9xfItnNfZfTQ1x_9SDiedRx1_ifysvS5vd6ibgrkNh6Kq5Snnr4FhMw6OWCccLxZerGgsZvAtcs5Q2CKZEJEwbWpgJUK67xAb_wT1p7Hp-HB-TB8OMMBmCyHXMbK_ure6R2ZdDOr6BECDpFqWrZU5hd_ltmba11h5EoaXOxms2F_E7ugT-m3r72yddzrzrvzruJF7nqggTFnfu2a23FEqx8jw7-Wrk_195wO83u8EYuF1k5kwyc0prdyoiPb8t9vPnxi3F9B_ideABLYNKYzc5cqh3AhOr1uSWm99a6o6NY3UiCAlgjoq3eVV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgBRE-0BRoIkjX-llOnkD-WeoHo9lC_nmCHPUi2kM6uSjU9UDkzrgcNR1vKurfokZun9y6wP583WP0qIwEk1UMapusjvn9XixJ8MGHpTQY9MsSa7kiv-ImspkyXvVo_st22-7UUdk53ycFikKV7CQBxCrkaJhRXW9PETvDok3Gb85yKcyP0mvz4LSbpk-is1mV4dItWpQDMUuQFpCD9uMR2T0kym-dTcTNGfh_4wLR8Eb5ViGUwCtIb4B-7ZmeZC9fvrWeQHcmfOSrYFoYGE3aLUL2NJ_sW7xTIE3mNAUI56dPQcTiz7moqgK1TyGlIK5WAXYGitA06sFHhdYRUw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWmCnxFxVeWAmBFeyAp16CmPxt6BWNWISdPBq3lxC2_sd0_L6ZiJqj5OaxpRQmSrUYAq5PxLUvwVw7i3tg6x1-g3vxlqHOMpGLQ9-FFMccYVa_dS9y-of_C0joALwQ8l8JV2fPhEY0hdafIaR280P9bs7ORwXnc7Iv8NJR-jWo0qeBuNmMQgeCNFPyN5wJ3c8sCxiSEXOWOo6ZRRxn9b6VgkeZofScK23zhREMh00f8J-_FXl0shVxJTmqG_L-qsO9v7mREKkG4qS5uR5FG0MFxIhBOY0fowhU9W16M4B_JsbiDYgb6bB2wENkx807gfoM7jyU5UwVr55nhJLmhRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-ULRRlffPzSdu2ecIJEjIBXMWFMo9fMFKIduFdOUSgncZ-Uts3HewWMP_qwK0EDYc41umw5dP0r347jvy6XHSTyMOlh1-gxE90QxGXSrcVruyw0hCCgZWDg0ROkmEa4-nAalcCTfKkmlAIzFBrbs3eOPkoDOih0xud8ppmUO0Zt4_OSQoM7Gxn8JqMgPZcwkwxg--V_XfmsPoxFBMcsS4BN3MI1d34OGLRVH7AigLAmrED5rvMkKjDRTgU-YMcNg-mRankd7908w0ZONj2nuLxe-a8vVkF-LkIKU7J2OAqLjPhjgPpy1qv7lLiS3HsD_zy55pnGAg3gMTSeZNaI1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKJWF_HDlWx-SwpskxQPaK4CihyARFex0xfoypA4LDAN1PqTgN291KbU8-kFC8WPhg64beDiySPSVTRN_A2tCo2w2C7kmwyWYPYkJ7U6VFzUYC7FgliJhdSZm_fqQ_mxCc5lnZrpgVhcwOorH3-MgyvJAc4ziWMCn42beFUxoN0LiJqc3nZeUhPQSINmPYPB9giMmXO3DTg2JS-6fc0FtEsLmp9qvtvqn3FiAOQW9Sf2ZHknDsLG2f3qXUi12ygAZxPUhywlIJJcofqzhcQkXnz0Kn2U4hvzIhnWVHmHP40-PPP737DabBhmeDO9BORsaCVXGh86VhCsctf2G-qLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIfc_th40wuksOPFQ1SyNJ-xVlrreuLg5JNhPN4md57lu35xtCwuO2hJs_6LxRlPWLHTwSd8RlNmMS0IZycN-J1VKsvII6kHxcmuP6IcvOe5dQeq44hVpdI7s5El7vpTkJ1zlEWra2fSVTf49k-vcAlHZ1jQZS64WP99W5Av6LbAdCdKtqjs9okHMgAnnuUwlAUxZox14xGnzsUGGJCV6mcYCjkpVTGvvix415HbrHMtGOSgO5fBTGbXlnZuvkTE3QmNs6dFrrupzKJpVMdT3-OPZ0LpmmVv1tqU4_T7QVGbfjKKMvdlC3EqYUEq79oDLSFiCO7Id5zI9sk5W_NbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLVjKnJxJ8Z9EsZth6Dn6-Gd10e93eoiJM9ppUHDjU4p2qpdxUUYBfS6yxVSZvWBWZBB8BNHKgQCGluE2ovJ5_Tr-OnseDH42dzhh7QK8pEnvYlO5T3ulJZ51qWX6tFHYIXG5_E4wl8lZjGJtT8kLWhSdOevWtA-J2hp7sgRKO-O--zjiIRfO9fPRcpQ3Pr27oKMcM7CcslSm5sbkuLSITXi6SspGdbw35dHODwtX848s0TMKdDuBWDFhUcFYgRioJjgBsstYs5IAw3kFRtbZN9jWCT11c53ctdUTbnj2AHNg_3bN_2E6wz1SThhckTAnA3uKh5hVSRlrB7_CNgqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqK32l4cvE1F_K3n3mR6JVNbrC3ntoOO0Fdbca3kcoXPOyD3Y0g5VOJvAc0pWHkIOCHPYO3p1KeSHxScupSoGMuv88Bv7WY9EzFVuKEryp6tXLJXwCa88iG10Z_h1fX5G7WdgL8ydIP-rxSZYrqaQ8mtX7pg9Tz9rcFOLrMhXMbl81RIzGDsNK9_f7CSfuBzja5o5fRVp1VAl7hmL3dW0rNhtbhhyTRAj_HgUtSQ28ESTkzl2c5nLbVnc_wksVwN17UDnUw3t0eXvAJTPmu1bKo7oMliNNoASHFSmJocJOX3cyCNsg5SPVCFHmoYRSfGhIbxCTdhnSOeRLKna-vhFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzLqZfqkfYk0qlWtgt6vUssIHJQQrPKxDqAfhQCN5yGBTs3Xm_jWg2lkrcOODjrm9SQHxWsKZtmOw6Wy74Qp5tkZ-QNF446TRYdqrSntHW1rRFFyk4oLqaerHKzB9zIwAOXSimpedIdqAW5ijkrsThyVqeOeuqtZOiYQ14ZbBDhwrwYIFQ4qVcbxXAAqRSM4g7eWNwMxXX0KMBoamuUaJQEUgycR-mkfOh7mqdJhScaWsIjyvwmNXRGWeEI5RDw0mvXPNDi5QxMLxLw5I1lX7H1xC82w2_cWfPOxWL7hd-mYhgdLFDAII6_Y0cXhenX_gjNHKb3RJR_PyhWER9HSoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1vLNIaZ4DraD9lNvF2kUL7qUvh08WhrQN_TKEFF1Oqb366Nv3L0EIH3hQysY7dcSQqZO3kjdp6crJMs-9An2hu2uGm7obNKlvQQp75ngbcT-UDo4gsIHAyq9fsswVpwcOdVbBSyxqZbOA32JmNvq2QC-P2xJglfJmQ-qyA0zHFlGnCr7QhpYaCy_5m6KU2K9H_E2kBjP7ekE2kKaB9OgT11GPB8MxDU_vNPYhnb8Ys_UqdTufBQhRqA6uOzGOGZ45S5GbM98FNQb_qzYrDLk0VJV4fN9vfhYrrIJ1SWRH6WCkg12GMFHZjlMj_lxpe501Jo62NQbZ_wjqU9emjSsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKWF6upasO-duIxE7p6JOg4tGso0ocWAt0mZzDIT3HtZ-CG0ujXW2x6wqWOKSKrGRtaYqtqaahXin9LsGFxSQIKy8j8afXzBFDCo7XycMrGHCBJrDACqy2O-3L_ZpQVMAndFp10EiqWzWHkpah4I4-zp5OrwXEQZCO0DA5pww7BHjWAONsFAPvAfzYEVJWmkYtY_T1Y5KPXf8LvCvrHJPhdTSnA3COVCAiFsZcgjQrnLOcKY5dynil4A1xS2DnPzSUgwSUikaFdbpTQezWE6Gapj0SMH-7mhF4wwQJ4KeHeu2OhedLwtSXnex37urNYYt6SglsiaJM7m2ut_DtS1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDFqYSWoXeji160qeHpj2qrVxYUNGbgijuZjtSf18V-ztxdVZrDfTBzlbkDiy2sA6PUj_XzDNdqnzZUIDm5ibgBZxJzTdtvNrcPWtHOLaAwCmrhYsWL_Q46fHog2aTcG45iDfy4g9orpZ7vktUtZF_zNHnvwQQqDrzNMLMBjVRq85bINuVBnNG9mvHlTK8-fpsxtOS753DVxv5U_wMolMQiYE8IRvn5Denw8Mn5BXd4hrerdH0flCoBD2eCNcAFZaiBnqmUibav16HEQdOYOolJDJmguAeF3Yd1fejGg3_vMkI8SAsY9N8paA9-Ei2C7NWaprxHkwKLba5NIXinzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlbuIS1qtyQQo6nJONd8pxLFUvvZk_WoRRX-NgOhcmhTxOD-nd3gqJGytxEAwFSgAx2PmqoMq4SM3c9gmzlzrdxYhuCaXLVdcf2eDfxUeUyHmoz94e3Ni50sgTfGBH1tLca3J93Y3bydAPu8qjpVCs-YedE75aVV_YO01f90-AjzaUH1np5IO_1Xv3JO1ZVRuKh6J3pfaiNppyT625AIpmXVjWD3J8-mIpJgNP3Wv18JgpVThGIKcw9d8rkuMpJjBSDUUUNmOLqf8AfqKENLxPofFOpf1oXoXP_r47iTROYRthln4cHcfjYiJUEL4MgnIscAYv8SW5upNpQ-Tf6DgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZiL7fOUUHgrFCr6U-C4SxljYiJHAKrE-0jRPGLPzDxGUZHC5CePq7O54_bnilOg8FrFYQVx-FMCKaTjLFzC6Tu9m9M8Re_OmOjJKq0WwLUSSrqug524jucpnboLYygdBybiJIvHlVQTRWp2gY-AbM9beBYTQcfjo5qJ5R7XFpuMiHudkGgzV1KEMU8wZJjiOvDxqMVMhEhK3kYyVi2TuY-HpZyUohwMrxXGAARwmDUYMIN3QfgtGbTDu20hiOVOdL-Y_u9XHbAAF4OOvEvPM7PhK8qhD1tAQjem53gooZaOd8th18vl3HWu9QuSn2r-ceZQzpiycNbietj_Rt9gKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_GNgOfQWZgldPemBU_06Brfngim2D0Em8sKvZ5FK6XvHrrvjL9NwG2nDTOqJ4sHV6Z7njWfs-VDuEsxZ1IoI6J3k_Sf1JnfPchTfIJWSKHFdrNQxDige6OEJuOU7C_NbX2BwzNG0T6OFAej_FdKi_8da8fpIBwsIS8euYyf254oYichNh_DazYcCBJcbq3hFUSOcTkn_MvJXrBs-D2y-w0tB25Ddc5VahYVfgYJNAQfRm33EA3PJ29eUv0hMW5_jj-BvMHth-z3sFIyyvPW2Gh7J4WhOzVvVoV_vrW52YCkxzkRE8kVDhVn55PFtXK6oNniHqY4VstpHhf2LTdkJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTUyvcOdQQ59p0ldDkd_GDzUOTomrw3xGIPH4C4kj56D68yOds6CmCTwRgQXSRzOxQNtCFCVZMYMefBVI44F-5CLxtV1QPQKrOG2eGlhVkhgXW70dYXFkjwBzK5Kwg_gNWDBoZoPKBa7HApGPuTDMeWjEaxo2evVJtd_4GcnAeyJHKNExPCJLGnzqqBRAlaAbVtwRCkdIM_C6i4kJFXLeNGI_q1UH5gpeCL3t8Pd8fWHSFiQvJnEcpBSHMhzFO-wR0A_GrKWG608Vwn356spt-1tekBnb7ZVv1aCsw6kQ9hWwp_XTi51vaYtAuFCJ1PdgqigrQF3djLuTr-8dGlEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIGpA7D77wYA0tRo-xMOgSEHr4LCagpQpWWdX4In2hjSqdtDuUu5xUNCNGP2IQn5U-PJOfgRjF8Nw_ZG2bmpYX21e0X1_iqwJH4N3uFjlzStY4eCWXG2JO2BFi4yqCP7ofiQyprGi1qvJAjXYG0OnOqWnRCOjMOmBD9PnXp837OnHiSp980m2Ca0XgAC6WssknCuaEODtwb-ZgDD9GR4HRU2aJFdvCVivYh8G7enGkdPdenLFcMu0NvNudxkVpZh2hweOILTjoSl-wmkZ10x9EivQlU7gcnhvilKp8tamJGQaGlx9yOV5UE_hRIKGMbmwuvYqIz2781WFNYt2uZFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvpgF46VGRJaOOtPAxAyCMTm1eQahiuMzqWYoI9pSmNOhX9DtLooOLS1eOV66lKWV-LfBkFXnEWo63Xq-I-QkwzTqKH5_fX3nYBtngMttVo6ExDR8ToKGwRCEQiKLLLQlcyODFbac0m-ZXz277LTumZqCvsGECfFhItMJ0H9mcU-17DNFBwQl91RC-WnObsreS6nW0LNbKwboLhve5F53PDSaRb3VJU9eSMnHshPskVVte5hGRPeSoHiL3eJtg6oIsFRDLq_tuX5ZwBGcpGpLclDrYBxqBAT06xtHfl8DEGdiaXdOl5LPvZaHa8i_jHqTge9KrkOWNO_BF7LbiReoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=DUccoGLJEi8JOyvRn2VsuJXKYbPtlCoB2RQhOe2LhO9x6tuW1oYQMpFwz3pAhk332JdZpRlGCMHrOpKjcf6O_VfT1I6f0aIFfJxo8CdcoUQDCLvor5iepyyrDdl7JHSXRChRZI-HAE91QMOpZT7Snvp-TIFtONqIchOTASXM9SuZgODyVWu05MGgMzSHLDS8msJySOvtgAPg_gP299n4sDJfrtYeXSBvq4k6KovEgTFWDRKgTnKMnsKMOXkBiitXNB2TnTsOQzaACYKlqozrz0k2FnDZ8o406CG2_ddc86Ridpxq-wr8keiaCNWNGf-T1HOPNJaoiQ4o7XtIzTOO9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=DUccoGLJEi8JOyvRn2VsuJXKYbPtlCoB2RQhOe2LhO9x6tuW1oYQMpFwz3pAhk332JdZpRlGCMHrOpKjcf6O_VfT1I6f0aIFfJxo8CdcoUQDCLvor5iepyyrDdl7JHSXRChRZI-HAE91QMOpZT7Snvp-TIFtONqIchOTASXM9SuZgODyVWu05MGgMzSHLDS8msJySOvtgAPg_gP299n4sDJfrtYeXSBvq4k6KovEgTFWDRKgTnKMnsKMOXkBiitXNB2TnTsOQzaACYKlqozrz0k2FnDZ8o406CG2_ddc86Ridpxq-wr8keiaCNWNGf-T1HOPNJaoiQ4o7XtIzTOO9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ5IHxHWsXJ63GN4Cc5Wchz0kbA3jxQvKRoOluXvdjJDkiljd_l9KpfCe-ZRrBgOP2zjtWS2aALEhDRyu4OA_F3xZs_ICYcfBRo6vk9uRBtiDp5yaYZnQSRvcmnur9_pTyEtOsbzADgKCpLFEOChyIM6EXrAJQdErd3dAzhpdsWkbXFAT7nG3DNLFMoOn04D97yluEUiziQnk9aSF006oCTwkuqGaADykQLGOu9oEUp1GIhqgQ8cILHYDhUBY8Kv3VMMm0wlfh0XSyDR0XvsKySNk4Qc2bN4MinpqjPU2mpLwLOMZQ-GO2K7KyuNsMVVw3imSBUi_qktDFul9ytFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cngTQQMT5djxloTnanLbZlbM2WD0mwNd0GplaThk_gkRY8ydqt0kmW690_QpKyZrfmKXI08-GV5vUbdrjFQPD2FYz8OwxhOex16hFLmT3p_KkPYr_knHnNVTdfe2XIhWcSjTnatOr0oRK0AHZwZmj2SkkgfsUBtdG3Og4rpI5plqlMi3X-B3uzzcnOcsdMUmGJYdP09CQaKnOL-uSNGXvLyiDZPfHu03vLqa1AW8fD-jy7RCh101kejf3rw0HJuCIGIyhDD28q1frJDsz9raHTd5wKdpUb1lWmLoSSgJydXWOnFTQmncdmbu_tNx3WjH46YZY9orleAPNgw_rrjnuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCarzn65oTOmUv0c560HMr88ARBJ43SsMuiXUJrHJjNg-0FyFRmTYzKsQaCEbqAaCxYXtzAST-ZQBOvfnyC08O3qC_oO2qlNwsCri9Z9Lypqe3r9m_uHwCWhneB9O2YituXzVyQzNCyctU4W1qYrvWFN7M_hUzYdcuhdxMEpowybQXLpvBuUKTNk1_6xqt0JWJzSVtchWtFu5Cn10vUFgAApE6gOxgKeJFIuRXR685Is2NjvOg4Wjvnkvb49xJTvWW5C28v-MuRz1541eA0Dzdm7_hQVADjcUOOYDe2NvvcQ5XA-efWbpZeQAH4Vr8l3rdgGIQEWEsd74mIKd5Wp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIgemhKLOxz8EbcY4QDSKnL52_0uvdDsQD24iaSQvM0LUB0DBZnCWWfOJq4CL1ulETPfmMWLeqGvhcknZNCJuJH09w0GEBU4rATPEKhf9XKmWtHFxr3iewjWeGc8I-kQ8OUpKEGlPDExCZHgT-UYH1xAz7J15Es7vBv-xVApHNJnzVxTqsvVDy2prln2PSVr0xopwh2OPbspryzfW4TC2t8B2qXQpPO4dpDfRizVoVxomQ790Ra-JEkq90tPM2pR7YIQcgaAmJybmmXVXEYq8W1VCekNnZHtj_DPTL2GiBNaM4vpBZjDxuaYZJLYmIlX0MboOIgMS2ulneMm6_07-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=cLbcVxlfHjyuCLXxd3kJQbhqBhBNWpg-6qKSxg2oP8hoNAe_WxevPgtQCS_sutT6hRDRTH6vw7id0nxTDM0Vwiic-mEVPPjg3WcTlxz_hZuK3AcYpRr7WN3NI1WusfV4mBlYJwDAMyNVmT-WJ9ySuTrxUJfJKhLV4PsWgsOs0SnAO2dPap_p4MEeT7wPiir0QqmCzBuDDimXoCmb-LGo5WcOBaNfsmG8fwzQsQ4rC_6f-Tw97cq4I3gqXD6y8Rci2aSJPJXX96QLaphvWs5ZmABaS00OnC2_bbrEodQ4wuuuvx9yOedZjzXMP-_2DdsQTC4gN5OqxUTlBTIeNE47jzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=cLbcVxlfHjyuCLXxd3kJQbhqBhBNWpg-6qKSxg2oP8hoNAe_WxevPgtQCS_sutT6hRDRTH6vw7id0nxTDM0Vwiic-mEVPPjg3WcTlxz_hZuK3AcYpRr7WN3NI1WusfV4mBlYJwDAMyNVmT-WJ9ySuTrxUJfJKhLV4PsWgsOs0SnAO2dPap_p4MEeT7wPiir0QqmCzBuDDimXoCmb-LGo5WcOBaNfsmG8fwzQsQ4rC_6f-Tw97cq4I3gqXD6y8Rci2aSJPJXX96QLaphvWs5ZmABaS00OnC2_bbrEodQ4wuuuvx9yOedZjzXMP-_2DdsQTC4gN5OqxUTlBTIeNE47jzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSFOVM8JOIb3_tSCyhnAi7AASs1v-u_AOTwKBn2ixc14-THtT6wHaUV-fkrWeGk3Z9XasGj0BYXhoj0xP7cf2OJUx7w8Uu4CTLrCBRQtbjgF6PTOYyBksdXW5JMWIYVlNIk4MUWdkD8TF00oPUvTUY4AaeZzuRqxIsT9JMcDFSzpO2CnI8pL5uepj-TET8VQO2_hc3FRUEVWFkk1vZET4_SG6MFhcjsEUEpwbe29LDcwNVcogbVgBLoI3tRPGw022lpjIrYJKH0N3JjtHVnAPjpPYnw1T_PPRjrtXTkaLWtt4pZJv2Et578z8L-heIyDy-8f1LjudriU-Xo-hm-r8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okFXOtXROu6llBavClw1ypT12yur06F5OOOx91cmR2G4y04-S-x6Zgn227JN_J1z64Y9L-RnQ-3f5Pb_56gmBtNOSuTsFMC1a-zN_SCIRSd_ckzaDnXudBv-sRkuDxEa-WxQTjzUVUlr1KDVpjc28UGMj6hikiYQgCdKonKvEsY_dDLnQRvf8i_W5SMe1SUnr1ptbPvSPzeg9WN_G3DvoFYGMGQ2t7OzxoueHA0zsCniAAiOUKm9QBuz4vnvzpotSR_nKzFUT7FpbsmAxHuWVZjY-DZ1kZqBqPehCnMZr2apMWJFX_QTfSJEVsHwk3qxBsmRekcCnpbpytC8vy_nMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zpqbkk7wcKmikUSx_xNu844x2W2RkKrqBS4rMa58lASZmSDKAaSKAaMP7NfqxSv65l0I44JZZ9fQFWKGh_XVvCWOTMyV_jNL1mXluR2VwXz-QvNrNeWCk8zVcZNT4NxhCFnQObFtjj-dnsCXUB1b-xCZpT6bXEgn_XVi8ltb-LBSxjtqBoieVD_lV3-ZFB9m9SZwpYXL4zU_P-n_HWupihLQKIm3hUcfEi-5USwck7EfS8aqzGh8Dmvs3xRx7pCVIJ18iXOHgrI2d4yURX2fnDFa9_reccrXKGTH-fGolHtqhHr68zsZSdo9juyPurFuB78RWyaXj8pWPl49Cqz9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiZ7mLsmyk9P5OlrsLUyyzAaKECcOLU2XZbvU_kNDSKKuTZWr_u2RX1ZO_PWMfwS5rf2vJhkoNOuM57SA3TVttwhexCTgQ3-crYHbe5BR8qJ8QpvWHtwVD4Oz0DG5q--XQphTquQnF4nlSwekBEGgfZaYgCUGPZOj1kwm72rqyCIIxi7O3g4vL3ezc1MBgb0RzaPYnN5WcJ6Wq3H7w8FcnUVo-okeSwMiY_TCkPshjHXfoFuxwoQAisHiYX2eyleewweKPwYwkN3Bg7vxVB_Ib2wj_hNBsUj2T-dYmQYSzW2bLRx-OhOvBt65vD6Jyf8oURc3ez9boJvjz5kTszE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tn_vm-MI2K5Yd-oMT1idCpBt_QALVDPogmvlaPsTPpkuAkcMJRBqXZQhSNr42wLVGQ-1rE06EOXy9KVjiSdepK7041BP7PAZAsT5ZS_XxX6OQuUYVjIYkCIhOdW1HvfJqLyJiWnjcsz9KTd3iILTLjQTBjJFTc6vHx9QbhjFKRZu2XMLhLgSIROQhR2AwyHE5tY0HQRAIermIBiXF5tqaN6qKm7fo9xgE0hioHGWFcLy9dsxPRcZ5UFxNlt7x3neQprynz9bbPrVFZz-vmCvp3TbBF5Y7C5qKFkgrM6ZkG2xS_M5bTQIXRdwYhkTCJ1j8mrsOHFohvIOEu0lI--BPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgNtWY_3QnGfqLDprWRGlr40wCKqdBQTZphjgsFaghkLfGla_0H5e4jjLOxFfw-pfXEVXoYA2n3UxBK_H8bBpR_Lacy8zsN1B63N2O4i5uRJAOmbbbTynUAoR_GYWdVG9x0vkXA7gCtLi_bLd12Cga1hPFyNy2rNzR_lUqLR2qgb5Pijotn9bdk52sHkB02931SAPWAKQRXRQh1gV28O_N7pIvJ3M4ql7KVkAWe8pK3h4pYkrB8rbo5dRJxFpI8v8dD_PqRyjFwk9fvYDx7OGdGIZXKE5jCAfsQGzhIEh_mXsbpDAMspiq6WhTRPLAzsDLY49r7uB8QQl3UYEPY6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPfj7qmkPucRFhvO7JEMh1RouoOoXewlgQ8NlNfXRXG25HMyHxY5-1u7rSg4K_WrFExWNohpYp_d941JzeiE6CffF_6rA01NceEvAj52PHt08OwaWejpSj660ALOz_GIsik05ioC5x9XHNclW5yAGqe7OKAJ5JMHoRNnq9rQ7_HPMWc9A-_4PymgNqeUxzA4aTBacd0GLmNYTU4SfKGTtiPactnOON3elDwkpMDPTC2N9TpRK-OnpHtM9kBQLFY_AX8_J1VCw7PS9z9SCSzIx02zxEvuztXsDHNlrBPDyZX7immKvHXPEz69Eqv9auXe1MXu9zh5iavVeFkIC9BzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClyA0LSvJ8BkV7l4hyPK2Jd7Rgvm9uggoC0q2XREEc0JWPQAVczYOrYA34DDe6bHbgMulqxAaRjAAZ-KT4yE1XephqdygmqgrNPVILInLBZNuFL97OVfkCIZKg5sOqdAaInus25seR639mZME6UvXSjJQb35C8aUFyj6CmqF55bwfM1ySzzfEix8j7TCrTZ5dCwAFVVDuopkUEIDEudsjsATagO3aq_7BSLslYdJjZpy7xdZ8TDhK0O2CPPmtnnmjhFefcVpc6xUW0ECgOUEgbZUZCWOPmMXGcjKs-IakwbKoF4KwNJ41Hfb3-W6V-BKXcvBgO5KVNMvt22Yqs49CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kig8I0E3Tf51ClI1kDWYKrKqoSJR6JZyH-Q--i9_HhB_wpTieF8n8I5IA7UH1kpvHpi6j7SEd7m6u28qf218vpjtwFBNEzIYkRF44zixXr7ADUjX3ihuTPIC_gygF8NY__Kq4r4bQ0eejfojS9etxZ3sPFKUyfBYGMZOpss10rflNE36BY1ZVtzIHylD59LrF3T-mI7DgMDVnaN7AJHKO_kV1B4jUl3PqTYQ8f8FoVFYI1CRGEKIug4e3uWS4HGtnLZSKdx476qJRLEF5mMnnRoxWJ7BgbVstfb0dbOrUckrvZKMmx6-n0WlTRzqXoLW6Xr1EEpkRVpGrT6Fk7Mz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8zeebh42nFRHip3Lt3Qj8oC-HkvURNYA8rcukgnHXBfXnBvVZHAbdZhbDO8pjqaHeBdHLYfK-qRTxeaFvSzS-MBHJuX9icwKcxg2hcXUAtAWN-hIYb7_nalUuFOCUsabjWkyLc_b-xq-klaGT_wyFWjISh7ZnpmVw2AIOyR8SbzV4Pj1wGPazHb8wlRQ1_ukqCfSDDeH9HaSKZPDhUuUAOKDnlic9IXTn_FzWdsu7CMctZanS0QiWwVuF5FiD9dbFnEe2iQXA62u6VTaJGwzhuFvjKLj29oxatjy2myp1xQgTCwSsuRAsppym3HHULx2lOZyNRMLUBeSs-gCd2N-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=tHYPMJ_n1u2gwKYBVIJmjBIKcjTlov8pDIXX12-v5bnmb9HRdPZ_J52Xj4z4RjjUq3w33JfCtDoHtJG1Y0OTBm1O-8wR4xqaDQT4YJ77OpDoZCIEJnPdhnZFQYXnP7_jyEddNBTXHa7a8m6_tFPXpiX3TeHp0aTluVnEb8jDFW0nWIjlsnneDuCHSk_fuI56k75zQQsZy01LlNRSYH_y3U5imurePqkjcdNgcjjtCtrn3M7l1dInPhH8XAJpVe-QDy21yi7UZwJIW9pXq0lD14qBlhJ08PKtVBAlq1JBNsIydrvwV03748ursZ3MX6a85oHc3aaIVQGXe1QDOZkokA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=tHYPMJ_n1u2gwKYBVIJmjBIKcjTlov8pDIXX12-v5bnmb9HRdPZ_J52Xj4z4RjjUq3w33JfCtDoHtJG1Y0OTBm1O-8wR4xqaDQT4YJ77OpDoZCIEJnPdhnZFQYXnP7_jyEddNBTXHa7a8m6_tFPXpiX3TeHp0aTluVnEb8jDFW0nWIjlsnneDuCHSk_fuI56k75zQQsZy01LlNRSYH_y3U5imurePqkjcdNgcjjtCtrn3M7l1dInPhH8XAJpVe-QDy21yi7UZwJIW9pXq0lD14qBlhJ08PKtVBAlq1JBNsIydrvwV03748ursZ3MX6a85oHc3aaIVQGXe1QDOZkokA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDhzRQU_cLhPeD-UcQqiAPJP7b9kJyn896oACeMYdoJNo46zguBMIj0T8rloey9IqZ-8yEJve59WrFQwfStkpdr5yKFEAPsefvZs5KdXFm4IBoCPfhdo2lpVmCs-X3K_q03cHodrefdj4PWjk7jcB4Ovu-LP2U8-N9M2SyPOq_Ub-EuNImOyup2laZ-US3JLcVctk9lFrxhSUWfMcmpEmomSR1wWxfuY31tVZEl8qXVCz_p_nFNQ9A6MtfjOHBEhbzBNb_lnxqhNsJ-2gWx9xUmk4vD2q1zjjXJm0rkf5gZoGLuZNpkEANhwv7rPcgOfporsfv521ep0RUuqw73veQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAtotqjQcW34g9qqoxrriCgg8av0lmLZ1elLHRlGMI6rg--GROeJtnWS6lugdOmvoEAB0mCbOB7mI0Jbn4HI49Ir5jE68JbLOtKlOh9qCSA6CEvTiEdSGaloUNK7z9dslhzzokkVpGCGWa74lS3EynDVRVkKEPMzLbfwagK2mIy_eP825BzhfAVB6cpgXItKieXyQGS82pzbMqtEEJA-PSLsuGLBl9opqAyHKdZAF-n6J9NQImHxM_SOsKneN7uAMsOA4Gx1q5jlLYZ4_IYoWMgkm_kukHpfMXZrjaH3uxeiOLnwTMGny26nSeHkRPfaAMClse4cwOBTsz0oFH1QWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n97UJLMYnPyAwPcrwbWoWecPzFFjOXkCmCiG9EaFcpqpstRpkpG3xFFiow_TZmyH0TMU2uNeMPNCdgfCkCHnEjGnWe_J_IK6eyw5byO_KN4hSw6R8dI14vxORChtSNi3g_S0wBsrQK_PYuy-vj_SOGM5Gt45QN4gOjdn8rcSwP0WtEjwB6VrnhsIjr5aVspJQQTIZoVQKIplW_ntjBkw3o2-u-tdUtSAyc-3QEJinA7KzyIzMFJka4-Lvo82A7s6UWmf52tP2BS3-EirOqQcghE3E0ZPM0cSryqZjr4weAUmibxdP58mTmxKNe7XaFRfuUpERdaVoI7875U0Axfn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbhiVm1g_KE6AVU9G8VbOkeqsosZX364wTV51iwB2qyLHeoAp9t_M3QqAnckWIGN4wJT6CidOR_aOY1Q5JRqBnYkW_dPwb36uyNVvDUOWQNporDCdJGggfEHjl_fJoT9rHXTIt533ACShLpcB3Aj7XPsir1KrrAMTtzNSFrEmxk1_JPbYn66dw4gLcb6E_TrU2yx9-CZ2MRnWEur_vNJ1TXNZglkSPx8fn12XSEV4oQzGDK0kUZCHCDCCxBK_ERhk8w8pBHbul2pVRa6SbSXYdrBn14SI--BxlEt1ylcuQY4W571LK5QjgTAcUEeJf9umjEUAHe6LB0-s4Dbx56Jlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFwdLF3Zqki398MIq06WO5ZoIwa0e14VcmpaEII9c9y8F90Tu0ST9EMufOJ7CR7-xTDUC89IijY8X_KBdv4IX-l-eE_WKZEhc853_IItbNcyevITNMO5VO9mnvcFlI11H-k_vBvvTP_VmtFlDN6Jhnr613bYHhMrbhVgumYJo5ph0HwSmkiXsYd9zKxYbbH8wrwe0TiZjH4K-gu4N9tYf9onGivVFbuGV7DUybFTeHBI7Xsx99mxfGEH7KrHwTQh1HREP2njF9WfixZr51YSPjeAdGEH0vt-20QDYrzAKxinaeaqY6WsOxdtwSQx6h1gGcO8H7hJHTO3w9AXgOz5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX64qGRO9iNw09ceNz2qIGCUnHiSJePRWn6jWXjYjhgHmVK3bDBC70KhgZ9EXp6GegI-caUTYiNpNEFJjjLMCMnRX2aSyEuBQNF8Hvz9CMTFOpT_aW15Oml3u_c2cMDVDzEIEjflPKhZFlU0DXlZUBBWUWn4Lv8rvDma4MRL3pxjnczwgF3HI-G0BcAYacBRoENAAg6bkSw56ZcwlxtSU4lAWN0eIwJRJc0spkm2BAokAeI5VsYz7e6qit6aiVHw0CVvXNJAqwKW-xLZbXTBvrPxsD_SaWwZ1F96ROVTY-hHC0O9UQIPmobTeuTQR_C4lqLx8D3AAFq27_IZ-mDZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSw8fWmoWrpxFFFmkIhBzqwXfT_FpddIYeU4d6D1pmdBPSZPcP0X0ujQ56SKTzRtv_LPrhSwe7QZCJ4sJV9jy53Jdu7yfvzPx7wItNOYkPxnhBjcrmS3ImZ43f0TRlgMF37e44TSr0G7paDHEtQnCJ9YaLAkn121K5IHebNF9Apft6sV6FAYXsFcFJBVjFinRXykaz6yEN6vn4mArmZ6M2Ib-_rFuNy5vELDoX0uKf2Ve_5OeGZdvL4lf84pgOJdunWefqZxU0aePA_9c146Kir4UyQBrTJIbN04-D7QtoJoVK0SJBGGgkufY-BXD3PzHUb1Z5kv7tNCx7XbgMQkjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHuUSoh2tMaNQzF6ZpzWwyYA02k8MKrCQy_5KIT81huIgIjEWfeyqwk9lpHxOH5nKkfP5dzGW2G1L1YdDZA8NtCcj8S8oIlmjywXvHPptmFniGV8GRphsDYm3R1sNX-6ek181AQ5k89lQSTT2BivZbbehZrWgU31E2-tBFT6e-rsT-Qe8Xs1r1sfPdIuikfGCNRWYCRvL_p_81_U0mxZLA1G8CXqsYtRxVNKMPajyn4FLMgbIhNZJRES7IYOX2MhNVr1TQAijWZT2ITrqnG3qUGX3j6ow0rtSJzg4HSRmiGWJfs03SYxdw_-pGWUyw1TW8CdKSuC00cKSlenGFbSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDAUHW_pW-zy7XmeCyn2Rb4V8n3xnhHCqlhaqzCWEN5ZG4nj5urHxbsfHwKZyPRNLHmRVufw6CFbF0rF6MJmX-IvLloJVNPQAj-JhapMv__iuu_HwubSu_COESc6AHLpnWIBumzBnBR0aekcWR_ElyNFbSVk7FYnNrCQkW6sc4-voxy6qPphcZlIpWoa9r3baqDdXbyTPGNeNMJhG-zxDABLg6Ng_02R1Pm4M6Z8gwp9rmicpDzys0fwxY7s70vMo4JdJUO-JMsloGBy70dEyz_11niPvYy-9Gyun7Ydf4PUW0wmhGDOkpXjFGH7gRh-HFgwjrje6l0ITsX2OYoL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPhu0FrMlKscA1B-wL8nCY2-vS5HnXSFlULxXobOmONTOMEsqzaDd7NkHaaPys2eCTBNb6jUK_uM2gyM8mQkYPL3gR3LyxmnMMqr_EFEU0eFVAMr1hWS1qQmdRrMWr61JwSIe-2iYDB0b0Otoz_BvVrWDBFO0tKOJkkhsn9U1fu_9iw7g2xYWAMg8nnD80NionaYNbn1sZEzX8H-P6ooDMIDaH7j4oc2_meaf5mjylgzISJoLoOmnS5PUsKRceGGYQp8dKII8fPMaW9WtvWVE8l-isNrbgIlVaR2KIQXXAuZM82dGPuZ8Dkg0VzHM-VyAFv7KfniIc2VjpfzfunScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3hkShXwVy66sZNnWxJmZfgDxNobXpLRWPnQWEZLEW2ZnupbmTW-lvrPD1DQ7CjYj6eTZH5_Uh66LEjT0mQbJzoDnWU7dLo8uIazTmH8v_cqyzIPVxNiCLQ0FGaAkbGFrCQIOypV9qlx1qtvkYMzXelPQCysTX0Yfh9x8n0n-eVQymWSv1jWMLQQgOQxgwM1W99Hrwa9huja9B1TZKwha9C7FR42es44ZD5wevTw8XvqgIZkZejSVxF7lRQZA3YEZLZ9a5wIb0k-qtuMGAnWunp13LO2eYvoGVyETYEW1i3UN6p6O6FmG5bxjxxT0LkM58dMTUdjDE9nZC6ZB5rAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzEZoHuuDrvz2oMVZHcYlizNiOMtcxdYXvxH0Z-kr1oY-jbijrazQGLAt9xvQ6F2Wz8IoigXnE16SgpCeKloc6xs-WoyiqpVwnFrXb9N9po-omU9XKaxQbyWJZYy3lwHHJnov-b7cBMqta_Mn9Zbfn--yuvxWJqjvI8vSX1YCIAiXcPPjl0jf8g_DKZv-TFiP1UX7WBgIsU7cvIVKDGRqUvts-jsIKEQuXDFaeIBO8xie48ZPso9ckwu_iljXK7hS-EZXBmzqoyqpnFnDIS6UiLMxHVaHDquT36YPtSvD-DUEvDy5AM4P8HBMDy0IpHGUrw4hHw9k62F2c8P4NoFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmo6hbTfQTSZWoEXXfO-wkmVUX01uyhPRxZPqdN1oSMNjFFTGbA9haEzHA0T55XTLqS55JoS7nggzHC_axAzXyI091QW6DmoPN2w68CMO6V3kK6gdfGu-hDoWcLmcrE72akamTHQbsSQ-2cQlp-EwA6-poq6iRaIfCVlPweOPtB6JLJVF0T-6zKGd5stH-x7LrjNbaX_p28I5QGRp1qVRCTH0JvD1FFTrEsXdigaUT42S2SxDYlsTbWfrIBJ_WgCY1zy-3NZ3-u0F6h3G0U-HJS_zA-RZuhfi1lWeAPwDK-OWeyHXJSOczSdV15bMA8bqZ80frduAfYElH7koqX4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMwmJCdBjV8jx_X-QLF5frFDc8BYMMtQdEzjMNu4G2hOuUN-6oaX3an-Uvzk7H7ywFnOfMkW2TOgP6djrDH6mAZLghxxDTDrTi98ygQBv35J4gIAJyHMf_LVBxf7kB_rQxfaBDZt91HFVsAKq_O3Z0z-wXHqGK_Lym6-tA1pQicc_7cqUvIVfjxkzYrMbjCjeH6en0jTPAEYy0YgYibCTKK2Jp8NSztph-6cwjGT7AnmzohrUAr6Oxunv7AsXhuZ-ZtvdslMMELBgUROBQdd7jSU9DrMW4DNgBi5B5OTTNjuX8lucxraf3j2QBi8v7gYxRARctcrKC4xgCy-CRtm2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raLi8wnFWEaIMQESdJV12AU3kYWZYqqrOzxzhgkmdMkjk4NJ9xFPOi64j0r481Ho-lh2Qp8Q6hAnBFRkGuM4FIxjwVF9PeRIguRFP9gCCOX6lXzQ2AQbZo27QqQUZmoMiqNO4Ui7YH06FZ18BsxSRehx3V8Ho1hKZlcwRIPaANnEHWAC4_SJSi5b_9dFTuGxZLDv_0C2dPvQbsByvMQ5lfmHBL-w-OPMTghD5p5Rx_LQNafIGUq2I_2qHxH5sBcNfIt8QvuBPsMPVclzC_VTrTwPTQVjmF5m0bsdRBIJ3XOosmXK_r33w-5RgciPr7xqbHcHjML51T7wt-aYiR74KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=fIUpchN_uEsP6vVCZBcTar2P_qmMARExqrifIz83m0ltFmKg_6vyWX11KALSRTctp5U6gLyNAgN8Rggz3aHnbuSi5QT4CaCqHwWJgbjjp8nWE7aYdvKchRtf3HrszFltMMxSMkwJRSLi1dSbD0vMCZ7geKJT0gGP-GG5rY687VT6mIoH1FQTWbopeddqhx0oieTmHLIOBhOH8Q_eZLGgfxxmXOGlMtf4U1QFxcCdfa7XsNHDgcgmCVF0DT_e8_vXEce9OT2FsupGcAP5oWj3J78ygN96e80fjy6_0ZGknm44p9TY4gqvE3MwhO-gTFOWJWXyvcMlXY4CxwlAZC72Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=fIUpchN_uEsP6vVCZBcTar2P_qmMARExqrifIz83m0ltFmKg_6vyWX11KALSRTctp5U6gLyNAgN8Rggz3aHnbuSi5QT4CaCqHwWJgbjjp8nWE7aYdvKchRtf3HrszFltMMxSMkwJRSLi1dSbD0vMCZ7geKJT0gGP-GG5rY687VT6mIoH1FQTWbopeddqhx0oieTmHLIOBhOH8Q_eZLGgfxxmXOGlMtf4U1QFxcCdfa7XsNHDgcgmCVF0DT_e8_vXEce9OT2FsupGcAP5oWj3J78ygN96e80fjy6_0ZGknm44p9TY4gqvE3MwhO-gTFOWJWXyvcMlXY4CxwlAZC72Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vezltNqCxfrIfum9jf94h1Ey6zvKh8MNuqSnOjT-bilSn-OnduGP7P09HDMkNXxJZDVkzFAG4Ck8upQfV4bI7Z60aFixYnhTxovi5-ousexkUrYnGW4y_qz2cjXogyfFptHySQnNBSpb1Z_DKVnv-7UC1vumPHz0rlvR_jTUrVe-BaCxEMJNlXd53nj3umUv1bsPJdO3cNvlXZr7A7fvcpSBoiMQRcdQKCQi_dEVNzkOdsUtSVBL3cqp709_10KmECpwTTnH8SCIW5BU5WI0Op6LMbxP0nPnGwpEY-6L53eEfi7sdwEzY6ONEoE9eU_YrLXHKfnlPA1rGPq-2HIXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOqJtLHtlW5iKUKinJ_HOD1E_wiJ7IjNzLTdlNL_85rViBZQTrkDjNZuheQ2HtboqKtwq80sDI7kZbP8qMWwnqJu-pjSem1e_52BtwV0nD6yeswz-9w3dGWj3FZnhZCmoGM0Dk-xJrZF9T21Wad3WB0x6hXFSeouhzPOTCw3ulyTdzTFZgBcZRg36tyB5eg8zY3Z0dZfvK2ka6EhwR0jOyx_jJ2YMpZFiVZ_UqC0W5aWZpVoGqoFjs52OqF7MEsdSwVuLf8MukSeBqwpbS0mAS-BGRWN0k1VhitzqgK3vq3NthoQ9w1wjsMFxmgiWn-fy9r9QzChKHvgGdeNinwrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAD0Gf934P1VUI8OjdJFognJUlzxcdivESi8buCey027Kx9g2aL0U6DSmh-W5-WmLNHBpyHcTxka4OSeHJco-Lm7A0YJJ9j0k1GV48cMs2gJvZPZIrxygVDNwgh0zs4-_kTTo0x5_tXqzFZKYXeGW9n6n_VJLDEnt_areCFOsg8tS02SzV3OP_nirmZHNORE-3KlGl32vPe5J1TpVhK7fyLLwREfXIOA59XIVjU1jqJHT9psY7PJDdMJ9MSVoYut1EoepPGLZL7-hQwmWi5364lqiPyG7kT-aCxekMpfn4rv-QRTvMv1YunG-yNZxE-r5Ds08bk6LrZ-WNktX3NQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=hUqbntDpD9vZHz32sIDtCQkt4FjtHzv4SSZ6syDm8wILk2IQRGUakawY9ClcLH4YHqkseCJv2g_NN-vIW8VHKagnJi2eNJPdfTFpBzrc07npVZSSsIhzHVqk7yJ4vW6ZDWBUfeKaQHuYPjxPsvDYAJzeKGUQ6VX6yJ0VNEQhYfKnjU71Tq2Euf1WsrFogE3icpYNW1CKw8BqlKm2aIRhZJjKrrRAohv6R872BOCzO2nWpcRmjirXHfKgQtxoth09yYf9UzQ8K1y-jFKOQ5umCXhyCOmoyRR1BsioTN-0WO6cBxImACndHgZ8EnKd6AvFUrDnqLoVX8F5ABWDPoqtzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=hUqbntDpD9vZHz32sIDtCQkt4FjtHzv4SSZ6syDm8wILk2IQRGUakawY9ClcLH4YHqkseCJv2g_NN-vIW8VHKagnJi2eNJPdfTFpBzrc07npVZSSsIhzHVqk7yJ4vW6ZDWBUfeKaQHuYPjxPsvDYAJzeKGUQ6VX6yJ0VNEQhYfKnjU71Tq2Euf1WsrFogE3icpYNW1CKw8BqlKm2aIRhZJjKrrRAohv6R872BOCzO2nWpcRmjirXHfKgQtxoth09yYf9UzQ8K1y-jFKOQ5umCXhyCOmoyRR1BsioTN-0WO6cBxImACndHgZ8EnKd6AvFUrDnqLoVX8F5ABWDPoqtzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOTCkv9FOPPN06f-aF_VEhfWKUhmLFH7e2vaKYrkW7gBhttmRuvrl-UcEMOtFYEygQ3ptky-3NUX2XLT5xejTEnN3eziPRmglQ_-0IeDErn617eZLyN7iT_G9IP8jJcH8Bwx7s8bDVeiNljOSsnDavVjfXoBJ_sOHW4o_ioUzvwExreTjNcPBEZ8A22d2ZjYGvHFNSk8L7os9FvVkxdKis1cdJQHtGhaYfUkbz5bcpQcLohgwx-J47iy_67H5n8ZPGW8WO6Udmeu0GE7uGOe5uI1jon4uaLkLco3NmcxbNCumx-Cgeq2x0EeGEu85za4tUa8fQm6dXQZd40lFNoqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neIU2ZRTtc6PUkaUwibpHUmKfqlv_8_TeBkNjtIc72CgIW6L3l3CAJjmIqFffVuYXsub1fSGeskupp6QPAQvUI5fOWDX8ikkKObD-JP4eXC7V5rGBjOpmNuSMSbtJfhoKLAz37F1_rNaUWIfa5tuIyecH45tLlYjY7cDSOFGzWJNUxKidmTg-rUY4xCL8Qc-_zdVNewwzMqYuk9qrFl_kCJxdSl66IHG5xnb7dRKGzrU_WjC3P1y3IJdDcOLbgby6KmTDcyjaS6EOLwed7zr2rM3M3RjU_MfJMh1_C6uMKrSBOd-QXFrJAg0jm0f-DdU8UmeOYPQ-r9xlHhfq944X-aY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neIU2ZRTtc6PUkaUwibpHUmKfqlv_8_TeBkNjtIc72CgIW6L3l3CAJjmIqFffVuYXsub1fSGeskupp6QPAQvUI5fOWDX8ikkKObD-JP4eXC7V5rGBjOpmNuSMSbtJfhoKLAz37F1_rNaUWIfa5tuIyecH45tLlYjY7cDSOFGzWJNUxKidmTg-rUY4xCL8Qc-_zdVNewwzMqYuk9qrFl_kCJxdSl66IHG5xnb7dRKGzrU_WjC3P1y3IJdDcOLbgby6KmTDcyjaS6EOLwed7zr2rM3M3RjU_MfJMh1_C6uMKrSBOd-QXFrJAg0jm0f-DdU8UmeOYPQ-r9xlHhfq944X-aY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4BO4PZeQWp5_6CTAZ1IfaytVvtZkL3EQSTLsEKJydbpvljv5o6tuh2B6iDXtuNPmBO9Q-9xDhHo8ISUwyi4y0S1pjJ1u8B8Vur-Zj7tuiZDvJVyaSBg5CECROCN_hXGLnFz9M2Z-k9WjJzPcxC8qVberHfRT3WlBrTVw14lZcdqbDFXYlHjtRdRl1REN4fHOBbXuMiNmN8ZUZvWmYZKNA9OMegROs1xxaTOV2dcXeCWVWtuyHyftCORQUuWTz-t1gTWnwaDTNoOxEb4CP7J9tkrkMWgmsc-rEXtFuWCCSKPXkSRBAd5ed1_GsBWsUXVeS-uI7PV7d6IV08VgF-VSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Welw9TQPCb14h5gh7-we3Vnxd8vOxlH5h6dgIwVy6MzCRMXfKXww0hhhzB_Y7FYogf-CgG0cqlZMRcHnOeFvwkTOH1cDsLl906JD1NN6NujX2SjcO6broXStL8vL9wiWr7ryta3Gmqx3mdyRPMJf87cJh3_ogAyirJMiBLisXf7rrGe4zcOXFxKtsjNzaQUpxFozyAq60CEByC4Zihr_Mpe9WO2bQTCUVIwE5P5rl1-q69BX1OCF-4Wf6apQL39wcwRHzj4Uv2RmRO6pkilG09CVUOsk0ttP21gUn7cezUvmupIMQY748tUbiAGZFmGNvJ5LQP89JpwmuyJd74nbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLfqoaWzhFCbgA5PFnjc5fDg0Wvp8lpH8anqT92BlTba0zI4jPw8m2EKXstQmwNKJ45DzC8DDapHB2URPbcFTF3ppYd6R1hfIk3vmuF6tdlZd8cPOWeoN699NDi_HWpbjDp9fW-I9Elebo20aIbU9dBLXg0lmfhL3kS15Ichk5Cb4ivvUQqxJsvp-6sjbnqJiPPnj_5P-bu0ygIc3qNJlA6HBXIA6aN8ZgFWDQ9a9C_QMxpp8atjGh6k0rZYC-ee_uO_WWaAcWD9IGiYVJbafeUDKcP76EnA75LJ54850vTU7YOzjSC2fITKlgz9bOng-FH3ClJYMWheZadKmc0BEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7iXvT69cO5AhnIgJutXwBgRzejbQPOne3SUEMJ1abTEhlxjBJGvRRxlcsZfJi0Q0qEQfCx_ACWEHGgYZf-tP_s74AXU8Cf5SnTbSQE9k-6AleRcbCYxDqT31cQE9xKGaDkvzW7EhjqxPFQY-loV3Fyw9gQvhj8_NcNYhz6bkxM4hDaf3rYYOHZ47YvODSZ2movZiDwKyZ5sKoInI1uDDToWykShSYOXGHRp3z7qn67M4AusinfjZMoF9nP8y14npIX8gIkI635Ukw5qUMocKu3wBkFeWWEM_3Oe-UlIDnQxgTUVQopYEyjmdFrfAYCDu_GoDLNd8Lpfx8W4DND5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
