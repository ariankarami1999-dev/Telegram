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
<img src="https://cdn4.telesco.pe/file/rp_LUFX0lCTrkEOG8Waw5f5TrwOGt5TpNW_7HbCpFuwUY-Vfv3yQ6lL1MXcq-xw7il9Ewr5AFGpJ3E-KQOXSB7AskIvh8WJR4MQU9VyvYby7v32mG1M7N5u1LWWRQ0JCOmMAyIzuhm4W9NTMiUMdgaAkM-6xTlX4Ae7raIgkDPwLJzfKej209vuZB1lJZEUKPPVqF-MJ9FZWYVuDURd7qtu-d9jtuFBIqJCbYfx9lbpAQV6vZ_2M0SN-oSwThhh-xir21DnTpG7P6pS8UjPQ9Y48JGfn251H4mrLvm6LJL7ABWqwY2wmiG-i0ExYsqrpAM6eFHli5q_RrEe8a-3kUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 578K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 19:27:26</div>
<hr>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO9Zxj2k3c-u9A3MD5o8CW1a_I89bVFDRe0LO3kmO_T2UHbcYCJ14dculspSOtdEpvZuuyrIaiTKpqzNvF9MF5MpXTWyzw0aPpwcBNRrp49uA3HTUwOwiuRFJLdkeBxSAWNNv92QBLZD15hBQFkFyDg7zfPKhtA2mBuLNcT6N1D8W9VZoRxm1V0G7LcbxMSQXzsP26EqVKbthvKW1c8y8bkUzQJGXmYnyifbEwrJ1vIn5QNv7jbDNUZkB8tLoDsimYMTPcfZ5hgbG0KdPz61zXs50u9MFNlAwhTaa0ivrJKEGNyKOixj6jM2QfBtzBBtN6AAUJ8jwhDBKeGRsIXP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1erqe78W6G_ORauvCB4ZcA05hxQCB-MxGvTlXu7ddHa1FnjdoWHkv6MrI0AZMrYJQPqjxRO7kRbwX_7Zr3g6YivNDyoG1mUnUS_Gj2tBvG2V1p48kJ4IWqqj8NjCZSuIrS-8dfHtIPvGjS4WMVT_MeY0snwlcORTXYYGdzA0bDwWSBSoPH6UBLT68fCjkJc6PxTFCfM5rxQI11mMK9GHgfMbiNQrSSLm3oLKjwPulVNuqVZKjVtTaYqEcUiqYCfL8FivSullOegaQDKzSAvQc0ExvT8IIi21vNllo3UfQ8UD0_SE4EppzCa9hfTg3OKV9nJUjUQKNRWho87m39gIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Od7TfafBQCPLRPITJaJVJ7u9S1iTRXUYJFnVP4FNd7HvCC9bGksI-kXEsEdZpqafwe4hrSt22OTwdvFaPoP46xdIGlqanrGmgIYa9wU1f73G4JtTW3o4VNyTvdWj8YI6g3RjzBKpxT_-DQ0I_dffb21PJf0oD0cTwwMzmrgI4iwgpNJoOnqjbCA5bsYoh77j_vzQdzs8tWq2a-nsFLmJJOZKwe5eGNndrRNzFtEms0MxHonZZ177CvWK_RcBV01Ti11HmaZn3O6-QG8J-qaMh6-bc1TPJBjg56oQqInuk8tPmeeL2oo06GzLkcfHP3DOzTf1whswEYeGuxAIBGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFVeChk_tbt1rW1DMKy8DA8-ROGHsfLvfLd1UoKpEoFIuyo8pCJgT5Alg1TPjmp0x48AYMoiRkoMMuWiQ1AUQKchk9p06P1U-jF56FJn63t5j9xug5733vxEF1aAHHttVWcMMPVfKd3fdBmn4_cJzddKW-muzHooCHAVFh5utHhnZmob5A9vP-iBTJz9TtwzmNjp09OyhzMhglXjvsEoqp14i5YFC-Jq1EsbCQ3yEpXcgKLnzimLm2au-qCQ0Eucy_IEICmlb0_RbzrTEwVB693dpTHRVUYevk6pJ-6XTTpjswtZkIohFATHuS8yVCnET_4pkKSyWLVs6QRutAvjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAfoVNjNxP-MWO95EAXRuA74No1AcdWwLTy1IStmC-lUy4514lpuDEBbu8GzY5vSOvwIY-aAwRB6VQueCTwITqcJWpLxuCKC6WQIVzw5sd7tR3tEi3tposNQXcowkX9ceeSew9TkivSbBpF4kt9L1u8Oa4HJuZEOtcRL16xU4_sYHNtZxipLBg1BdfeAmWOPY7lseohkvYUnMycbsqkrS6PbNi44ivs415bMRVSNKu4JoQIgbKWuz6yNqAK7Rpxd9XIPsPD3yYDnjjymusEjLoPBE2iVvXxFvWXadrJPF8anHA8sHPTMAIRBSvK6nBFoWnFYYaNmq7Wf5wSiphvljw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZ0mAM34qD0JIZjC9tOfeS20LwlV0qCRHiSmFbPNXIAs5AzZdrlNHoJADHEPKBZkeufEM3-bVPNokQLoUPu64R7jUFAdJmkqSd6b-jSKGOxqAQ8yIEQfEGcD6PsRwOsqIZZ2LjfmLmz_gowrx4ZooEl6tftSgQZVd9l2rZQZAiDFCfPtA0Py5yHDqsBcNAmuuXKc5NAyrAuz2hwzyFoHlj2K_3ZBA91mbvmBZVQtIq9pob81DpJPIFx0M2OFFz_TIJIouUkAPnKvaWRf1u9CKKPD35h6marc_Vx50GL8YOmCm1FV2ZliMxmXdt6r7eN0m8RNRypla4akPDStYcBr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOXLtSgqp4ybD3AV_clKvbcObNgJav8X9Trof0v7_wDrRIdeBpQntfYHLyLkr6g3F-8OEua39YYtH-Pboa8QaT9RGscMJpcgSVhuz8QLB6qpmf8dOEwuP8RbUjPO-pu6hHSOJ4uUwvoiSrgMtnZOz-ZDhAM4aOJsN_cxw8B-aR9Wy6rVwRSxBVMW0wMSfkVkyz83MVMvds89M-nyTtQnwy9gBTI7WasW9t49YnfnwECNQTBhvfMJAipHi7tQaf8g9ibamqY6HJn-VNm3c1oOx45s-HOc6y6qkWO5krALbs6t6-k7mk5KRned-3UcQ9yN4JAuml0bliLaAZnVMHbR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGwPAMJrT6AIQHZgd_0WC4i435eeJGPLoQzkJfO4Nqh83xoKHAl-BdEaU6CTynd6lKbT6dIZtxCCiEss-NHAImhCmT50zBzNeZCvAQAI8kVnJNtXZQg3pJvaRfeUeGkwz0RnUq1z6Ii5YyP10U2HXcejYREuqur1yn510jQXjNrS7weToDODtabNoSxtXK_bEyyYxL1hlW7pV6xeXsvADWjnSNKCD8sdPlu8Sl9FXMx0yxT-ODL35NA1VB49VnghqH43mjOulBAfPQbago7f88F5L-UrbnuL8Ss60gAHukK0jEV3f-mLO231HAZWeqDfNYpKolyrgaoSqUcs3KzJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O73KE9PPDl3Xx3AKvf1oISzfhWL8H-yVAcM_QdH1UDE1WdZ1mPfWl0OGfs6rtoUpBlkIdKq1CrDFzVMdgzArZJoOnPo1BBOU-BC4E77Wvw6FFy02ur58HrREEMkyT-2oF0iN8yLhM1He51xMO0xhbdcS-QCAY97LF_5FBCHMJDyrtKeSG-HgIvDasfO1XqH_UNy_bVV4Oq-e3d-jyp5t6Js6BD3K6gMvsMgb2Pw7VsNhQvIBxUrgDjK-o0qmT9E3VUb25A4Q9KsSW6fGrsNeBrQmYnyN-YjwF9nHWwJzLuM22m4n-XcTnGAaa6y2X0DN3uYVDjcAltJfVLJtP8vymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDLPVC98ZNwTtNXzH75lgVpMy5yX0TwIOaaci856vj5RxxIDVnYiICmsPW_s_NAKOW79YSVCKMHXywYljyKlrzuQCPtUQ96yzVXymwue6zFAIRRHZ-er7VBZU4u1z3gtCVp4sj6IsdJVFtzFdYwJplmc0dQ2kfPDctPqtcb9I6GdK99FYauJp_tQf9vPQ1Vr_8MmsBBmbsyoJBnDBrSvul2dN7PQQk13OOPECmAk1okhB1emFzIgCBydrn-sWTZswolXXKn9lBSHk2cXxOODsUzCmrRBKmrQb7f83HRpHaWtSI9YiY3TVBto3fSXr5kb2D2LlJ-M0XT4-_5JNVwURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCaudgXtynWKcDVwQO_cIO5I1hjYsD484YXmKZDRpg4OSOARDa306XLo1eW2DHEtiI6TNGfp7ojUbCRDlp788aFNt0OMK-AkLW4ylAkBNraUmPaAcNiF8zPa5qJd2MRFc5QqZwUi-aK2JjuRZUBNDupPVFeloQWskIq_UZMlnVQm4_5nT2O1-3M0xhqxKwdsMZk_Hom8ddtNewPJknLE1ri9tfpddb3jlDEhGWxZ-aRz_Q18L18nWKRzJhpu9PA3_UfkxCEJhTFD7BzXMJDbJIdxEeUrfKwatvqUr7W56w4RdQP66aHH1EmhVNHSzo18Hnti1T9PEJ5CxZ8v-vYNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngZRunwYAgj53xfMLjTo5zJCfZQHRPW1LTmI4vGqU1diYYx1umkKyFCXGQcqKLFfmFiAwpS7dDrFxuJuEEHIJvIrk7c7LwRZnjSfSuFMbeICo9sMB1DTXsPT3Gu0zb7aizg0YLeCVl1pGK7VHteO58-g0Vfz_VUNdwNoT-ZEff8bUeoha7l9QqOcjITQPNQJGZ0ecE-3H7MruodE1sayjo1LPF1BW-e1grfudt1QnyP6G8uxcyNpVWTFSgR0iUou2G3CoXQt_u7yX0mCHulc2493RdMTDh0_YiAe6eTgiTi7dLv-V6p0xEg3I2pIPlYyrQINbQI7gh39_hW_sV9I-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMR_GBF57Tm2NAL5eIXx-GpiK37_hwI02DPel3SWCi5bigbduPcVFYEpnsPAHf8MY7qxaFpxeYJoFWHze3URBbiOlTqROVvMnqj6gbH22EZIYTzWHuBvDbXws7DTE6Dk7Isr5fUyzlycKIU3nq_9N5U5Wjzbu8GbNcYlKeHiNdec-6NTqTXhMu0_TS7sXP-q7ePQcoeWUVdtdTjjVorXF-IHKntkbd-tsP8x_IB1RZQAwEA16Sb8U0WMVWft3Ara2jhiHIoBN1B8Mo7VHzDRx18CVBRwhzp1Eyn46QgAlqYUArijYFgwVpFXy7ghI9jK0X2YVCyO_AKAYveDdlLTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTgbXyh4McUZxwdUtiV1erqQTVGDgM8BK07xBDhJ_kZWmwKhia5mt3lfMHhItXU7c1jcz-SICBtI3kUHv-FTQ-7t_nA5GmCVi8JaBMF0fuwnk20YlLlUdOnBH85Q-d6g1lR7itftdZX0SNqo3ITj239g3ywca8y5xoZSdcR3qu1YlwyIhvg-mMIMDd-bEFrJADNOBV-oBKLJwTjlbG2VwCLbSKEl-xRCsfNAtUy7x0FXoBvNNu1GMoccP1J0mflt1HjRb9PF-lGhiOjY_2iZjLTaWq_bZB_bj8yAtXf6Cau6DJDG3drY_D5CX3mlxtDMy7sGU0eG1mNZkWo9jG4aiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUYfEkWxnUQHGMD04LFPT8jOyn6n5Hk7solEEoaHOE_4PzpNMOKQ6fakciqHmvNTGSOrgLAgLyi9HFPEnDYMK-3PpgKle4OlvTG30FU0XwTE8TCGHqip4FMI_BYxdj_189rk8TToWskJQAR9QAyWC_F5OHUgDLe4c4hxWxqs88XP2maWjejoebE4xRtwMKXXZJPGS-nB7_G_r3HAgzmRBHO3tt4HdUJQQ59KbUR1BRd34AYz-Nvo04Wr6mz6LmAYfBvzsfXH7Js2JwV8ytJnWPo3cgFfGz1n6C_jBRL3wBtkyqTt5L0X-0YDA9yNobM-1D4m_RO0-JHh4EVd9yB4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrlnVviZUO5-hDgEniXVnLwSoeT2GiL7x9KhN9bnY5SXs1FaXYsk4smpqQmRIE1YfqAsEh5NdGEI_0RIOTytTqBUwdEgbLfRtg2_4U3vyXLVkA3jI8Fe7a0aXNrmOPU0JfAEHiQcFPUgxVlE39rGFL11wGiLyk5Zo45UeedAHfPHRshD3qq-2wLrDAWi-zm-6CHPeci9emvQS0HSF-qqRRfQqooehx88G_OTS3sVUonl2u_XouO4GWHGtVOZkre_lLPfkaLYiXhllR1UqwpHUQfuIaNOiRrLtQyxvJM7OCimLqHHR-M1q8jQWeT5D-V4PCFdSylGIozJYUi1dakERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpUYEmSfCaVfShvj7MY4lzM3MNMlhNawqrHMYq852nAChqa5_AGT-LTin22OXYCA_lczTaruOcZzWIHnIjZpqSuHeRADS85BJJZJYMgNepBRv37GgmM0Cy_J53BcScznmA1yYyxy4WCDG46fJwIhNFwL190NFeEifLDEYwy6aUMr3Lu4pqJiMUa0dRreOQX4-k5F2TrvjZDRFe2i3mNyv2LJZHZ087_9vHVgjiUJ7r-cYwbJQIJhYIPuE2n77ZPj3lwYOX77Xmu1Jyi5O3-mBlvGWnN8ToLfn-YSqvbKwxU4bQsePlcNecyu4JFEAqW20dkgDTc5gGBWieJLMXLc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzwrVS5N1D0zkmqsFYaCT1kCdo1-yDMPX9PBpYs2YllicPT4otye9aWm8yComBYLpvscvFhm9Ng3pgjfFVPK3CWTVoEPNdaGN9RrVtteWCZC7sRC_H1Zc4sogyiPBVIhMh_2HTdxKT-FUx8kB-TVqCIL9MPHQ7J-LJ2CeKOlJ8VK1bTzrhar1D5DiPOWqgMu0-m0NbhCYXcWYlu5-RP5xZYZRd0JfdSt2j_m1XYZqhJJXZCU7r--zx4IvTYNWN_jy1Oe6ADMtfQwruZy7w47kp7MYF5qezLXPzIM16hZLON69MuIuCkWUuMv6V9Dbb9W0QnWsWstiwKRqDVuwlUQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIudNl8W9BqEaVz9ho9w62MBe4hIDS4umtz3IvOJ7a9Cwe4d6DCCv5ffiiNPYubJm8l5LSib0cWgl8G-ZfVVweKf85IhrnpX1yw4B9OvwLA5JNQqBC5fhCOfdt4s3mu-HoHeRQva5gv2P3hmOmGd9jB21TQ-pmk6GudXA9NcfIbsnIafmHWAtGC3of6QCBVsI6-CxluT9GXQB9Lz7bTWXAR91-YCo2UZFtU8ho744SE1tgkrAg-kxxf7tuXQB2qreX1ErTvUCewqVDGlXOUZfHPsiUFFF6_2uE86DoGy866Kh4chaNOC3w5uquC_Po0qsM3AwEMciR-4D1jUnF74ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXQ-b2P8x_sm_wp-etQcdMJuPH6o49YVvh2wcQpSTtu7PygTBm3YtZ5fGZNyxMXI23o1Z4nKqsZoyg7lPP33XXr6GuXQ3TJ6JgR-5rARrmxXy6J2AlvDy6o4yAGg_p0s_gT3yOTvk166MmfKtz5n2vWs7sVR9y6YPVBU9RAwJI9Nc4z0WXwUP8aVUv5Zwg7V3K_hNe2UxNRg7dyKVzNzAox_RWuYhLkWVKGMrjhzjyDINg5AdR3s5tAw3y_mJACtBB1WQ88FVEM5Ys2s1W3Twe6aLyjiHKuzKP2ILyBz7Ln6FNo-9BOhI1P_e2aJTu9xyoq_aHmnmKYcb3alQtUaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcnPZsOixQe1vgqMH1-dv2moHeQjDB1Sh1yIoKvf9Z05leal180sVW7D5FQWpJUHkcwfzTWBMnW7o7A2jCVIFtbCFI5yQ-DlwIcMl8wqndkMrnNoLytQQA8EKIqJ1w_wxUBvI7pcWXkjNqF8V2f4hicZAgS8ANkDXSP0MZgqYQq6PDdJgYzBvOkqpBBTrOfT7dzViaK78u466uLIxHfKg80HmPqctiM2bUSLnpIlTHnbo4kR2P5fCCYw0f7hQ_Yo_h4GoMzfIHPUiWc2Qhiz5LhcD64CKxb4eWSoAjrAwdbIenjvXS8klWnpXAjBJkDQgm3-gVznssnrv-AfvNV15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on8YNcZOhsfs9aYlvmAzjEvhJX2xLrXmTkfGS35MvJQbetYu9DBFhWBbzVUaMtx6pEJHOoEZ0EHdi5j7ajbe7QTYoC5hhSIyKRv_iY2gUvaPsi_dRemOtPJ4Sg6yVEniMLvVWwcfhDaqNYkHdPon94wLfO-vUnYcvb1_uyJLAPp1JRXujc9duiWao3jVcSIqn9gsfZ3lGwcmVDUqs_kT3STy3hKlie3Fk2CWVlkcaWD5BK5O7_ygaKZCWB93A5quaLUoSBk6CSr6sCuvzsDYCh5q6LdoNhYiNEDv_vs-F2m0WTGHh-wyvn7E1TAy1_Yn-xzOSMcgayQLwywcuGoUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4cWZ3aNvKTovdK5wlJEtcUFMnFti411znMhfubyNZ0rmv5KltvMUj7AZ2Pomn8ziYfO47amy664yeClYtRNZ7jVzEu-vPmZ3bhhsD5PcCS5IOSfkjSgA9N8We6nuJ-IuXg1N61bmEZOtdESyh869RQSdi3EIDc_HdYh0Wc6bB2GoKTjt-hihZZxzbvc-gHj3rcn84Kmr1rzcyrnpEEn-dLYXi1m_8WudHYq1qA0uvN-SOSNsbzYYLIbpMcWxFrOeMulfG6LoBhD46iC2KZgSbiZN24UqYvb323f5CFHR3_7cB346wZoCJEJXKqbbA7ECt4g2WAyJXrGBl1g667Wfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhu32fQUsqr3aaTbqNhoxlZTBfE1NEh4i23a5uec7YFls1k_rpaSGAhrOsDiMzwkOBUcGS9m-gDG34zKBUE9cFXWRGjqjlExwBH0ChnCtHZDrsq2ljbWWTJQ7Gy7FlzHv7wpG52gbBrbPZEX2bl7UQhKPMeEwO-YvTeIXISORO6nyy8gSW2FOwxBm_1yK5XKAWCCm8N6U8m841h1eTVN3VOlqf-Xvk00DAbStpO5iyaBbip6T5CaVg7LJQUWbjFnX2dP97LW5-34gdm_L0cBo_pNdnpewcj0iqa_l0UWAjc5ypu-lcckdDv64I5wFNFv2MlXuQju4euS5QqhUwrQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwn37v3DdiJDyOkrVEzE7DZE9vGhIUi4kHMUgOIHA11nTAf2VpuBzdvo5T0Mu4Wj2JZwUcl0W4UTSYWqGwhvMRmYhOtLOUUMg81NIXAQwh9BwOpJMxmtZRYAqnaz0NMxNw2v0fzCw_YG4Of83-xCPoGmula7_ZKT50YJxP2R2Qv04E_I54yEuY1FmQFaCvJRBuiB_g1m28Aq2KfnsLlYcOECiGC6YjWJwnh3SZy6AHmXP2Dm9qzmU_VJ94ABAnBRJVRaEv8QjVMEznUNokwq8iDdY3Q3zeAYoecKEDbarQi8o8O4WBPreoi5tWpsb5b8fwRfhgV1hjQb3sDw3nFtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe2lWaQ_JE_LuZKxw3SCFSg6-lNNG72W6Lxx7jF8jsGXA-JkxiLC_vegZaEsn0UfTbQ2AqxKO8VKs0tsy4S91lNcLEppagjEdCDx9gE-eOFVooAijNVDgPtG44u_KAI23ATDzLVAVJTBHVpXWr33h_Ezdrhn2PFRMMXt7vN-5p5VorbpTN7t4glVKKIEzXwOBJWRDzJWxxhjDoCev-Z2nr9IcwqouXCvL_NhQ73S0z_E2aLXWy0qKekuIsbuD3BW5Go8Uiisjn2Mc8a6XyIl_9ypJZozPdsiXWgB49qWtys3JenGlrTPrRBnhjYNrvXdL2uQWQMGA1v7vfFDVeHU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad6BRmJzHYlamC7mTb4Jf2wjhavujf0jc6PXyQMvgH74ne2JqKQHCrH-cAcna8nH16BWdz8jPlsveLEKH69vSc6fdqlGGp_EoZMQtnbTwOOrY3myaetXOP5G8LErQ7PoBDfUIky9nfg1sBHOsDw8A4T9YQm1aYHfgSZYCnhRA3775ShiwEEt5_xB0fHQc3M1orK1mnxVgbEs0mQVgL1-EHw-fTjhm70UZX3YMsRuKL3yKHaCsZDZCfXNDdKnVoXGpSDEeDKse9LEfYvF51Pv1vDmV1pHANjHJUR9HjOpTgBndtVBoNyOlMZotmYZp33AO17Yzst6VxqAREamGInG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls3SXx8BBSPcU7ijYCAWZePjtV6vDbm7XKbCqRTXRwAZhDqhnkTWNqMdfpfSuxc0HcWTvajby__I09g81YghWpZcC2G47684je1Lrwxn2kvA4RDiOcbrXQCKuasqO2wMGUIGqqvt1yNmrXKqNhtYQi8t9p4ar5cEhNCXLOG34sND4YuwtljOspMGtXp5O44QulS47cjYsdHxnTGQBS45NNFjYyuFVbdaLc3MjtKsTfr1AgwRf8LjLwttAr1FP4uKFrJe9f36OVsLoyGLixU4H0_N1EdJj4jvVD9qvjBUUmpiPDbP8dC4HFweIpCj4pwJ-FeS0pAZgWYfEtTDhJXzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPxuzukzgnbhvy85Zi4T1xQyYUj9xfItnNfZfTQ1x_9SDiedRx1_ifysvS5vd6ibgrkNh6Kq5Snnr4FhMw6OWCccLxZerGgsZvAtcs5Q2CKZEJEwbWpgJUK67xAb_wT1p7Hp-HB-TB8OMMBmCyHXMbK_ure6R2ZdDOr6BECDpFqWrZU5hd_ltmba11h5EoaXOxms2F_E7ugT-m3r72yddzrzrvzruJF7nqggTFnfu2a23FEqx8jw7-Wrk_195wO83u8EYuF1k5kwyc0prdyoiPb8t9vPnxi3F9B_ideABLYNKYzc5cqh3AhOr1uSWm99a6o6NY3UiCAlgjoq3eVV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWmCnxFxVeWAmBFeyAp16CmPxt6BWNWISdPBq3lxC2_sd0_L6ZiJqj5OaxpRQmSrUYAq5PxLUvwVw7i3tg6x1-g3vxlqHOMpGLQ9-FFMccYVa_dS9y-of_C0joALwQ8l8JV2fPhEY0hdafIaR280P9bs7ORwXnc7Iv8NJR-jWo0qeBuNmMQgeCNFPyN5wJ3c8sCxiSEXOWOo6ZRRxn9b6VgkeZofScK23zhREMh00f8J-_FXl0shVxJTmqG_L-qsO9v7mREKkG4qS5uR5FG0MFxIhBOY0fowhU9W16M4B_JsbiDYgb6bB2wENkx807gfoM7jyU5UwVr55nhJLmhRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-ULRRlffPzSdu2ecIJEjIBXMWFMo9fMFKIduFdOUSgncZ-Uts3HewWMP_qwK0EDYc41umw5dP0r347jvy6XHSTyMOlh1-gxE90QxGXSrcVruyw0hCCgZWDg0ROkmEa4-nAalcCTfKkmlAIzFBrbs3eOPkoDOih0xud8ppmUO0Zt4_OSQoM7Gxn8JqMgPZcwkwxg--V_XfmsPoxFBMcsS4BN3MI1d34OGLRVH7AigLAmrED5rvMkKjDRTgU-YMcNg-mRankd7908w0ZONj2nuLxe-a8vVkF-LkIKU7J2OAqLjPhjgPpy1qv7lLiS3HsD_zy55pnGAg3gMTSeZNaI1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKJWF_HDlWx-SwpskxQPaK4CihyARFex0xfoypA4LDAN1PqTgN291KbU8-kFC8WPhg64beDiySPSVTRN_A2tCo2w2C7kmwyWYPYkJ7U6VFzUYC7FgliJhdSZm_fqQ_mxCc5lnZrpgVhcwOorH3-MgyvJAc4ziWMCn42beFUxoN0LiJqc3nZeUhPQSINmPYPB9giMmXO3DTg2JS-6fc0FtEsLmp9qvtvqn3FiAOQW9Sf2ZHknDsLG2f3qXUi12ygAZxPUhywlIJJcofqzhcQkXnz0Kn2U4hvzIhnWVHmHP40-PPP737DabBhmeDO9BORsaCVXGh86VhCsctf2G-qLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUQTs3OCDNVY7JVLiaZixyiwblPBCMmn16RaH9Ru9-yrKcO4QEWjdzanPsKPN7lTQYeU9ddUVCSuKB3tRAe3V4ki6aWnOjPrSPh-ySn3juWTrYG3HEuEA_1VkXKCdLH3i_I3qomiR-cMiwjqF2XRfkGOMoAck5zQW5Zv3kKWyNV3FnHWpignseCI1auYDk6FztfqSfGDVtiFKNA35QVotGpGlAMt1DmRYc0Ka0nzdil1oZWZsBDqqPIq7jv4jV8SEJTK-cNTNHazDI7AdG7ZO1gAtT7nBgkVTtiCD8eNaDw164elmIUvlAa1VKtz2tYiytCLfewSr4zgCyFJBcYZ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L60QCjsoco7Tp5nekDyK_Qq-8UfbUJXKCsOOOARlkNTzS9lV6cC5jl_v51S0K-GuCI7lzGbzUEaiTVDpvMYwaIj0-EjjhZN_Ydq7l984R8UVGtYXlX9xnu0rHTRI2FU3RL19dFbodD8I2ClPi7_F5FNk7-jCoLq44qtZqTcKcdVZ_cYIyXnUBiqHs5yyzazIE3K3aZ99zQhc4Yla4CwJOUdVGTWtlR22R3RlHf0Z3rosVBH5LOOkPnuf9mK9rlLD51oT3_yMw2EZKPEdPCfzZTqfn5rDn1v77-rHa1bTjeJUB9gxyij-1dVhv1iND6mUTMFrKM71xe876t2OeZeEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFm03LkRV7EqzhH2PseiaC0vrDPnelKyGHV6QJ-TKld3QrclgHDAUj6jDrpBQUH10lHf8vP_0N2o_nyHRq7WGedf4ZXA6mzXTO2E91llgp1Lh2Nrr0L1bf6Jg204l0A96s9qRjPCY3WFS8611C4sfOKf5Q_8sqny2-Uz--TgXXMD0jjQBJjiOKebm8eNYLOEdnb6VfeH24nVYyYC9f2d-dxtvbtNGIW-to_0b9-kPX2B8SgwOd2UeIbotiL1fq1-N4a5eVDuuCs_pMMLPgJjcqZxOFjyhEQkki9sraxPCGyZAb20LgceeQ0Gl1Ka0a6wZvdgQwfBLhwB9GZT1BFopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UguR8996BNljfjawu3cCCaBKLRKZjRWalOFoClduF1c3Dxnx6I3nmY7KlRLjNltTlQcKZl33hkasbWi5AddSZh2cw94XfU4nN3afIDTVNtV-0BlQ0I_tSe2l-6afEWU9LAR1CG8rMGg2hS-WJeitIxiNgo9o6nXDGA9y__WZW5VW0fIYprL3y1YSpBnZt-n3mHFqsWr2D-kX2XpiI-CH9fIe2omYwRNZNnNB6R63TiQ2kJgHq7U2BfWtHxslOw_MI6hQcwF0n9dY_Dne0wZyENidPge4CNetJ7p1PvqIZoPf2qu1o9rmRa6emj1UoF6UQD5LiEhSU-hEf2AFZGco6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu7hwE8JVWrDz_qhRl7x7h8_yNiKX9ersxbs3BHzpKXBbWH_2e-MDGZFLz2o7cYkdjMaWyXKAKM6GFORuxu3kReedFpUMXu4IR_147JdPIux_ofI1-43qpguNeLcNvEIJrUQwk7_0fInE1H-JCsGMM88dvTzUfSD6Hb5cyFxEJw_D-jwE9mFwsd59-uJ-Od5kKFkbUnP2161W1KiCmEVchL6OF9ogfy8Cn2Il_5et_vZARXB49S7VpmyGFyvZeiExnO2I29wCJsYHxi46xS_GGgtOpw2F4Y4804YoFyQQ9fRKZMsSGYFvb-7zXG7RCISR-8M1kac5TNaSILRaIMP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbrAnElVO0YaqY2xM7q9LnwGdgXAHzdQLAAQMv-1Bm9HctQg0xgIRHOT9eefgC3VoZSN51r_CdlMsJV_wdTQoc4du3FIkQzyVNkiU60x-87eO6WEBm8XOb3goaIjLqDGqTsIAZWz_l562dz78H6dZhXWtOrAN2oUsnj0e9_8nwlBUrrtjbVxbz48_7BHprRjtG_6J_wF0mZ3OiCPmxqXgsUBxGaNEEQaQa7iNbdx3ZrykvIYWsULKDwribwgisXnyN4tL-7qxn3GysigCDs8LxbYcyPc96YF4xfFSnYAlBm24nnlrZETsT8--5lcUbgH4CPOrAAjHrL3-wbG1a_Z2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDFqYSWoXeji160qeHpj2qrVxYUNGbgijuZjtSf18V-ztxdVZrDfTBzlbkDiy2sA6PUj_XzDNdqnzZUIDm5ibgBZxJzTdtvNrcPWtHOLaAwCmrhYsWL_Q46fHog2aTcG45iDfy4g9orpZ7vktUtZF_zNHnvwQQqDrzNMLMBjVRq85bINuVBnNG9mvHlTK8-fpsxtOS753DVxv5U_wMolMQiYE8IRvn5Denw8Mn5BXd4hrerdH0flCoBD2eCNcAFZaiBnqmUibav16HEQdOYOolJDJmguAeF3Yd1fejGg3_vMkI8SAsY9N8paA9-Ei2C7NWaprxHkwKLba5NIXinzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv367QyH1t3Gu8PLL-4isoLHNhR32dyw9E6oFsWZMdL_6Brp4Nx0jyslanoEihsfwvANYHAT6q5UuJ3k7pLc6OpZ9IZLerpLNEsK-kzjhaalSKzutrenSkyAWPblquQ5KZPw29Oqk7b0BiHeze_R7Vr_AHyfHsiljyYckoZURtCO9wEJ1pYmlh9iG3UN91_ia8uJ2RRR7X0j7KYb2UISFc03LPJ-C2Eyt1wMojSCutoN8H9m604vyEI1Rt4wOa0kuyL24ChNLITNLTsSBdaM42YanahRaGPikvUL3iVBHXf9yBIhzkoMABmR5DtubCJnLpkR3DpsD7FcaIOhQsenBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE5HHCe8Muii97w89rHAOgrm3f9dFmOV_O71YXZKDSom-qH2M_uI5KDAu0is4O1-lpLUsfeRLwG8X0aepkWs4LT9LgofR1JHsVUk_RtZ4IiW0OMMgsWHEH-n9Poxmd2Tsu8J-CY8LrdKHF6Z13-bVWmKRCkC39kx4xUUcOuWa94IcK0Xj-ShR6Yy0BZ-yOaxLf4KiYbCsojDFOprh1nDlv2z5_Yc75oV2sgOQBVBUjVudSfKvG7_N38o07Pnhz7BL_1ZSFUUXhMkO0dHWIECrl6eN9l1oEvC9WHkcdIP1CCJZ9atvQKj00JFK8N8fsm2fptNOcmCCCPktISauNrjdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3dl9FiS4ec6m8tagcc_OKK-WWsNBPqLVLSxovG2vQfERIX4Xy9d2Ax-EKVy_mS7Dxae0ACkYubK2q6iRLoPtn2r8oZLz2updEzx38NW7tbWXP5o6vZVsBji6UhXnBEuJUVHIskhOffyNRsLbeOu6B9UckEcSYQxjfb_G9UTk3jlg0hXYTeawndfHJO6rVjSJUXtTcfOPr2WNeQgdEk7gLSPdUZglEidrcR8t3xFQWdSF5wwVqXWRNCPVeKMch6NJD3vwoQjsj0JgmZzICd00JqKX9TmhJNrX5EYZsBvaQ8CdFXwLovJ_7-sILMlYDk3ZzmnZCQRHdSGuVA8Gwe5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNOgDBz6CM4k0nzdpfComXxqQvQ6jxtiBbGQ1LvzVdQXDEhUU5pHFDE7h7MBdU6shuKBBb7MQDzkFPtxPeYQlwY1SkEpJ8ZVI3EI98PB_TUE6PKywDDZpQCZYSHcciroDYR5tHwEqlolsFe7IpaNL-blVdLUvWuLPp9dcrS46YB18MS341ib-t5B4zOBNn0oWzJnxdQKMAoBAAseruEBQ_sVYWEW27VgMxbO-YF01TTE7tmy6vgOQ4WKDckX7Fnw4KQ0zN5EXik6XiqgCT721RbszW4YkZpvVtBcn5MRkBIkByTSOaGYE2Dnv_ZPafqez8kXTdoqUiPMoqpgVGl1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaQ-wsdtECV87IssjvPSxjjbg7-QB_3VYSykzxZOfRD89jSC1wG9IvALaDY_1sf4Czb62mlwqPhRmGZab6tgS1FvK7GtKB-inkCzOC1ZKTjKpsa1agH15EASA4tiKjx4eqZodB7EYXeOvvybq-KDt6nceCVHOWGDQA7YvrKFG8V5SUi34UhTkIRWyFUurF3mDFKHKRL8N8HR3lCMgA-ptHJ14saYj5WxePJipF9XUDvpr7zNO4ArVbyTGMjv3f52VyMPkrDQyZlF5fQDXIX9jsr4Cd4CJXk2Z0MTx-R7W6IjiPjH_yTqvtmpP7o3-eB3qDLUB6flm2BciYbO6bldSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFxZ9JBdmWh8FMxaXRdIPWRET3ftxx6n5l8yRqgjfEQxNSFLxH3E-Si94pKE5MJBbW-0ad8Z5hjfdrtERAVTmTYStq6gY7ABFxxIa336xC-X2SENEm5MDVCEwAxgwX0bWVezwakuPfpFMasiN2uJ0s2rRNnBfDMYVs9RzoR7mmw27Wx87kgP7OkFovVXDslUfJxGo59henRyEMtJ1-EGxWYKSZdDmaMQh0HfAadH2X6BgdYOjgvETUjXxmCirPtTNJSdh6kgN3IBT-TZ8AKfysrq0k8Igxm4By2j04pYxEmpfVOFxY51vjVgAKue1i4Dv6NSfHlnHGLBagG7t6fBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=DE_PE7dfBc5COP9YlfuDnqHhLB6RSofOcxBGKhuu0jWxCQDniYLsYgSdpP-2EKJdhcFe-fhVauM7g-j4AZ0hOQzunWDIBKT12Of8SS-nyaGrv_QBveImiM-3p2uBnht_h6Po0HUQEcXX-wnmCWauRTNZP1SxVXzcRHUyJtQqBUtKPSiBhcEYP-RomTMqq7V_K0C8RDe9BULEVLU_FYckL971wQo1YQ7sS8bdvxcFE2oqJAh-sk-BJ-sVdABjN8ypXMVwrVR3RgSnVQEYgC5VSZDXCbi35pts7nbuVBg5kJvcH83hXN6i_qpEuFKXFygkM3RqmU2JdkLaO2NrUNTROw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=DE_PE7dfBc5COP9YlfuDnqHhLB6RSofOcxBGKhuu0jWxCQDniYLsYgSdpP-2EKJdhcFe-fhVauM7g-j4AZ0hOQzunWDIBKT12Of8SS-nyaGrv_QBveImiM-3p2uBnht_h6Po0HUQEcXX-wnmCWauRTNZP1SxVXzcRHUyJtQqBUtKPSiBhcEYP-RomTMqq7V_K0C8RDe9BULEVLU_FYckL971wQo1YQ7sS8bdvxcFE2oqJAh-sk-BJ-sVdABjN8ypXMVwrVR3RgSnVQEYgC5VSZDXCbi35pts7nbuVBg5kJvcH83hXN6i_qpEuFKXFygkM3RqmU2JdkLaO2NrUNTROw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGtiBRvskDQU8o8zqeSvm6-ITNwfsB-1h3sGrJUmNXafdyfyqRpNzylr37oAKfSHaEuIEztsLbR4Q7_Ft_9WCRVD1rxZPwHkfunuFPaqLsstTNoqUgee4gv0GyVwaoPZyiLkcDL_GW6yJtKTrV210bPkqz656UpTajipKQYZxYUoW29oR1FzVqlTx4QoIi2mLHXq_LXWjy-y5d_RY6BCcU2caIBp1sN-IxjupekQh_Rfqs033EGcoXw8uWBdEuxS4bOI_2__LgBMiMHX2U7G28nIVrXqt6rFDPsVb-GQfW5lU-uRBWOK2RXU0o6NFeN-5FLWSZuSj6Ir18vow3mEnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DihBoQlEZd4VGuNw9Ys0TwsCPvduXQe6wLOc4I-by1N-LViQ4k5yMW1Ol8HkYF8cd_htiPL0ePO8mfCfvVU13BJ6KQlpbz_7bw-krXvdsWyv0coh3pQc76nX8Rebxx9eQFKBTe0eKjq2BBdmRRLSPHvRTo-WVSY02jNxh6YwHja2EJCSZN8y3tyUj8sgcoy08CPV91E_GU1uJZzgRtRP48wBMWI6HBzglY0jJZUDwOd_Gkij3Z2znvXZhs-W_IvEJFKLUTkbHLqqXRRa3CmHljXwcg86Y9C3-64CcpNtdYfMrmLpQ0esuA3AVVmGbn4AFqqoKTNaWhuXBS-L0sRoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ord21-SsCLCpL40K5lfj6uivaQMIOoEjZHQ2h927dpUK_EcMYe07H372TnDaJYpEEtFd0CNfK92P8NYYcqiXtONCpcSwIihaaCMGtAQopvM7LUjNadWWCotsxEZRJNDIj3Gihk_Xgf8RPmsSQWd-Fa2H1ByPOf_UdMJk_ptBluiPLjkZq5HOCx_UGodE876ycee__yDSrJJ85MV3VLaR-ZO9rJ7RpntPPGhMmre-zfIiZ7mXcNWoL-Y1-_LNGNnxN2gMtOHV657ezgSuFeH7AbpqLqSCd-c5Hb7QZL0mRmny5ErYNOTNLDrdesOvirtGAVcv3gP32gCkAYxEgLh9Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4kx8Qwv8B_nov6ueciUMF-2QfUkVhmFkIVN__mRmp3EROzaY_L5als9WsOfyjXh1MBXdEVjCTSo9gt_323zvaFARp9C7jF7PiQLkHtq5bKb_waCVwsa6KySaA0XdA1WBHS2vv2y8gP154Cp9oJKBiwA_0mY15EBP7zMkms4Gss4NEBUkKAtvr1pFihrcFRhlYRZtJ2NEPl4brigUmNWnVrPh0lbMZnujuIZIreYFMVVpXi_LQGvooqc3QBMPGTzJ4Jhzfc4PA2iNSTQ4IWqeStyExrsFBxP4frn1UAXNVzZ4xQjkLAEQjK0kIT1DIPB_k6Yv9B_LUYaj513g6U2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=D3k8RAj7hVAvZJPA7HzRQv6wBwHOehaf9F1wAWkgHQciQbMiwitlkDYGK2MZYVp9kY9KoazVVAebGeH6bOLRUL3lhCwqUHCwRDN48_kO1dmiA4FiLAl3Cl8_xyi2ru4cSYdRP7mAJr-DnHkpHzxfTtNzAr1gPJ37ERogLQPKJbh3YVOQlu1XMVxsJmGGE_kTtnb0pTqykyJuAuMG_pyFvVV9YT22PB75hf9UIGROBZeBIITxvcknG78nK70xXqC7NH4C0pweqUtCrP0wVJqgJ2veVvnEEj3HDCj0gH0l1N3zmxqTSTLmXneJlUjqH5r2iHey_eLwN8Et3ADE7qrANTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=D3k8RAj7hVAvZJPA7HzRQv6wBwHOehaf9F1wAWkgHQciQbMiwitlkDYGK2MZYVp9kY9KoazVVAebGeH6bOLRUL3lhCwqUHCwRDN48_kO1dmiA4FiLAl3Cl8_xyi2ru4cSYdRP7mAJr-DnHkpHzxfTtNzAr1gPJ37ERogLQPKJbh3YVOQlu1XMVxsJmGGE_kTtnb0pTqykyJuAuMG_pyFvVV9YT22PB75hf9UIGROBZeBIITxvcknG78nK70xXqC7NH4C0pweqUtCrP0wVJqgJ2veVvnEEj3HDCj0gH0l1N3zmxqTSTLmXneJlUjqH5r2iHey_eLwN8Et3ADE7qrANTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgV0uxd7JwQzIqAJNn5PFshFHx-AEZQNow4a-OVjWBHNWBvmpxlXgQFYxLsSTPIo0GiPvUADPD8KC4BM19FwTtgCO4FUjAEua_MxzCTqlX7MD5-hyPZ2VEeT0bfY71mz3nPTj2z_DfxtthrQDem5z3WXIGgu6FcmLAfzDdlWKCBwQHOSTagHtsJdbwvvkENBixaQXnGtrQIzmuBrzQeLosm2LsIg70N-C6rntS8F2o4vzLvYF3LoDmlbp4jEdAbodLVFooJPSXup6AmdP8ndzqZReYJfMZD3eTBJQOOpSIV41kVDeeqzbxZUU8sbTj_8jPD-Qx0n5WzJYr2yyI6jug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR0lSkbh6Qrdk8FJBD7dtKgTys6OlqKYJr6k08vVqkqEUT-o3B8sXMkuY_k7fxxnvGv7WM9GEm4IKte5siwcbkfxNEA-ToqNPFqS_vPsf-gD7-pE0GYVss4i_x6SlTq0LolqU8hA6OLOBZuOq4a5l3FgN_Xnf47nD4nadh9_Thsaraw0662SoEUipyJ1Cl74TgmLuo0EL7TxW7euG1Zsazxbq-CKvki94bppphiPn-1KwjbRvqHi12DcSyBXVyeCdKPUC1UGINjxDBDmNiAe8sGG0DpGUFXoh3SaB8h53mkqBeOPgT15M1yiw0XMFYgbionEdmsAQYj4cQigqtynLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgoZmteifgr2BbqzYioE6bpmVWsmX9-VH9NPGZ0FrNGUl26JdeQVOhGRFv2vO-L1A5PKCL-wkFyHqCF3BNQJ_YH86bQsTIb23QpQZMRW_fRRHpDqkjwCY1-a0up2564oJHXajKgEDHo8dUr6wodqAMkOIToDGNKJnszOVu4sAq3k-D3PFGExBnY7HybP9ptUwJXwt8y_AXGksgbAb6SDtSITTxgRKBLhHxKBH76DMHjhovVbSJM-GG9zlropJBRAZR7SBCVIobmcss9e7kUN1Lbmxat7KjIKH__gB2zyhyPZm82AADWQNvklQQzUPy7aQbH5U6JfJL5gwF8DY8kg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-6VG-lc57m78XI0Ira9XCyASbz2W7qDryrc2nySs4Pa61PK7OS7Adir6EleKug0D7efGpGjG44qlP0pj8KoJsznx5zLw1MeiRG0DdBMvFvHmOLRy52NHvQzrum_zXmORy02yA6HokFYzFI6_7F_FO-_XmiYXu6gxa-qD8_K52oWxFG71pQWeQu1b7_sK1GBd88YtrMU_avdJ62xzpwy1JHJUlvJMgDAA3BWMm_hyTnJNkfQTCVmz467Mped7bJc2y1aMqqdoJOTKOhhWFCviz-X-qdSsFG01Y1N3wYUtT0rvAuPPlmZTMBxSWnpMB3sdSN9q7vEfF7Ho8hBPbe6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tn_vm-MI2K5Yd-oMT1idCpBt_QALVDPogmvlaPsTPpkuAkcMJRBqXZQhSNr42wLVGQ-1rE06EOXy9KVjiSdepK7041BP7PAZAsT5ZS_XxX6OQuUYVjIYkCIhOdW1HvfJqLyJiWnjcsz9KTd3iILTLjQTBjJFTc6vHx9QbhjFKRZu2XMLhLgSIROQhR2AwyHE5tY0HQRAIermIBiXF5tqaN6qKm7fo9xgE0hioHGWFcLy9dsxPRcZ5UFxNlt7x3neQprynz9bbPrVFZz-vmCvp3TbBF5Y7C5qKFkgrM6ZkG2xS_M5bTQIXRdwYhkTCJ1j8mrsOHFohvIOEu0lI--BPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfltxsEf7zzoABFDpJPBuinEGuVFYeHlaqVHXKZfuqxMDFwNk4Q926HL_wUflQdn83G9giv8jwVkHXHGS1TMcjaBdDXBE-DlsVuhcT-wVjOviZYlrdZknOyxRIyz7Hkah5SP2mjSzlbllVJnVGz14GVrUrdPj_sm7-2szhI9327XBzk_QgFUA9lPpaxSR3DJg8FYHGU06OirJGyz5tf_hhMhiV8Is1CJ0r2wy0TOc0OXLgC1wSXeOm6Wbb-c3PnG4OT5lJsCIL7dhvT8ch_I3ZAjMqOV8nEbrPKCJ-FIAPHT76WaJe1iE-wuMz0vkohRUq-9DDFfAe24QyF-5Yo5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCCiBHLRCvO3wy2GnGoryMI5P-3tkRz6AoMcnxbhu7ZWYvaOL62hGGWzUpHUhiZ6QW7Px2Z6pcOlF88qye_wOCz10RRrU_o_Hjd5WKf3tl5J9mXuNYtBOUoq8J_KflBuTsnU1aK_i9VpVfRX6GqhEDtIrr1w4ky7gAHrkCtqP0V9h4l9lCf48sZV0lQ7MzcZNUHRf5rLsvhHCJAXMjKMqIQsTb-hIY8Z58uvSC2PaowDlmlNhbpkTeH9eK9NP1vkeBbnD_2abuyIBwS4_hqZ1WFbgN-QIsXfn2bSp8X1jDOGl_mu0ELNurEfkJ1VWsS2xMZq-FcnuS-4BL_E1CqXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3LxDdxJn1vrMmMMBMLDbJM26cKF6w5Vmra6ZTS89huZgUwdNwng4Xn0jevGsu7ahy1zLW32c5kd2XVXIaxY-UTZmY8URER0N177NHYkopa2gwBiZf6TmE2GToCoyUgrRQee61kIzlQSk-ylX2U4LpJfuAutaXTYaf4yXE970AZdrRPAfp4NvlstUfPZB0vV1cst2ICmDvwx1XPQQCzPccKM-DiUOrCXserPD9U7K0Dug6YN_y8MrX2PRWRHe-SlvMopzPXZcT7_7FEXiJGMFHFOb_Xtc45DQp31aXswXzGUy6enoDafyHLu3C2Rptq8z0YrxVmxGd6RK6nXWIMaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tShlfdcy0PphAE8wYAIMQkmm0-ZOatbDQgMPQd52i2lFUVAxYApdFjgVy5gdjfYbrHceTQNPxYyUVvOF9RAm3T4y5fFyS789M8_s0wWXt-P_yLM3SoDpHKOblUIqqEhtDOWC8cC0WM05XmrDZESo1OgtTwHrqavJZ50chLsohDNuqr51pfGaYtSKC_wpdwKobKPfZ4Fmr8Vx86pSy5aGFbmLYY56F_d9BxKl-Kuw5UbiThBpoZOKhtNuRkxU-8uwvPNLjna8RXJd_JYVgBn6vmryMeJE6wl7yTFgkyGFluqg7CY3MoFVODVQ-039uiuCBEhUYnmejW-6KDL5v4Ivew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8zeebh42nFRHip3Lt3Qj8oC-HkvURNYA8rcukgnHXBfXnBvVZHAbdZhbDO8pjqaHeBdHLYfK-qRTxeaFvSzS-MBHJuX9icwKcxg2hcXUAtAWN-hIYb7_nalUuFOCUsabjWkyLc_b-xq-klaGT_wyFWjISh7ZnpmVw2AIOyR8SbzV4Pj1wGPazHb8wlRQ1_ukqCfSDDeH9HaSKZPDhUuUAOKDnlic9IXTn_FzWdsu7CMctZanS0QiWwVuF5FiD9dbFnEe2iQXA62u6VTaJGwzhuFvjKLj29oxatjy2myp1xQgTCwSsuRAsppym3HHULx2lOZyNRMLUBeSs-gCd2N-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-Go2o5LrFckYZgR5SiMUeXSuYfsfE6qmJRaVUj9SlAinJm8Kbmpckm8BZ-sdoIJ2vBBki-5AsR4Yc5hmDPXLFh_QuTnOkA2FrPremuKN3suHsSeOMv35Qs8mSw3gAPWDmvzE_9UDhjD0UvLNzFvlpqHUPPaJU-QJ6alDd14s1BWoY_jlbqvapwpo6iX2gYAWA0X9-VJe_Q_y5aX3XA018T78MgPxaoFeRQq7GiTMzh_m36h0rGYNVjj51dbreP79OZJB9SRV7R4h-euDAdc5MM37n5PWlkkmIhYANb1_zclqTz9ywbe1LHQrxm0J1wYMlvl3jTW3mxILDg6t5LgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_mi64r47QOhvxVP0d2HyXZFYpPHyp-0XqwBiRHDJY7KHj5X8aIc9liIQrV_O6KqYX2j_yciw-IhmcTpltCIewQVwBYnYG6XvXorOKFJgV31eSCrr7Oa57YohaySXvUsUwbL7RzDB1meVojlafkzamh-ikzC7Zy_jStks8bEIl9e_IT6GpqiC5bMy3rNNLq3xMQYbu2iwWWFx55KWkuXm81Ikhf9UJH4WveGvEpDzv7IjrmZXCrQam-Q3C5Oh2lNLQoADDnN9TxxXfaS59UoBjeldrV0oZCinOpVwBUBG8bMUse3thNYq1MDuEvZzxXmgGmUlNueZ58pb_lUYP6MIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1UKdvBGnDURlLjzSFHRAVmeBtaMQhce_S1O1Cu701h8HkI6qtQhyjDFWiV8hwRAu0EQDIWy05EJul7TYbXUITjkinuyOsHwWCy1uIFsc9pjoucMX4aPK69VpGS2ZT5_5QH_vykPm_SQfq8c8QVgkDjMb0GG1ai2XEDNUVfmbO13qcr-8Lufp1tiC_8BQvmeDD2GQlnQk2MRfF0-09O3saCTtPLCHdSZXZ4weVs4hyT6mMvHYi8Z4Jvpa4wfdSLrXt6Boz99C2ghxFDvzYWq9XQnx5meNTdafI0HPmMARFM0sAhTVNg8ekSvoQ2UgS92Auz3AMaJYP_6NsAooBXVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQdQHobP9fIIr3joPRKNxwyqQ2K7V0ORVd9uXJlXGzUfKPJ1kSc8GPE5c2Hl32GHzm6o6-HI9PvHKcKuIiiWuWugix65DWNRkkW-Wi8ayVzIkZHZKLsUk9gTp1HPJub6Jr4x_0ShhcEd951x8BvHdoVibICUftZbiqiP4ajb_a1VK_e6gD-U_YF9798I92_F1F8ZuxF8LhrG4S4JhLu2NOEz79KOViCGFBYDhvRHFqoJKiUDWkP6EN-wBUW_mdkwroEP01fDYyEWb-xrNNgNQcHRpIwzf2CS4oXNb9wvmrVrd0vBKrmVjSI2e25zIRuyOW0T3KMZCRTWZ9tN9tV5Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYdzz8yu7SRY9EjOQySqUvXZ_z1n4jkUNu1AAGKTEQzhugraxmALCsufbN4_UWSB1vrtvbNT1UhDhXQV1Rd1c0KMH140B2UJi0AdATxBrsH96mB2YLw22NFQ9RY8X1ASLgIndNNNWwht956jsSRzH_-l42xoj0tLdfx4Rcvqj-Il_XqEYu4cVM4nPrTNab4rxM2MY-x53ml3c1-GgV75s186RKCWoFat4Z7rESGXJETRCMV0YwK3h39TiN87un0aQ60dNp8-XDBrpGaeEuKGsQZsGb3uXTBhKQg5jy7ORH7V11q7-r2GphloKBdylEZj5U_2ZWOng3XaPlMIQl-FxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQT5rjWpcNH9gbZ8fdgMuaKfWsJLstFDTDbiGbi4SMxsys5D3HHqdhirXz7SGaZwFqA8jNGkfH3x-dfk_wCxcusUXVxq3MEmEEJiawFXmtrWf71LWWp4LIk2BQvyk5CMymAu7bJ-Lm-hMsX_1tHtrWuA6PvUhE2nYX-f9xfGJZrbcwrc_p18FeYtospuGBJTgqy5Ssak_kQ8kxkOzKseqGQ0Ctv1muUCm9S2tJLLK_T4cAQKir5D_uRDqv4_Oi3pAdInK4IQ5Gvo_cpuovECZyJN0LbtZqgG9UZS0MZat1CnxGCIOqJABLTgfpWTd-0pWq42ij45fG43lV_iwfs-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSw8fWmoWrpxFFFmkIhBzqwXfT_FpddIYeU4d6D1pmdBPSZPcP0X0ujQ56SKTzRtv_LPrhSwe7QZCJ4sJV9jy53Jdu7yfvzPx7wItNOYkPxnhBjcrmS3ImZ43f0TRlgMF37e44TSr0G7paDHEtQnCJ9YaLAkn121K5IHebNF9Apft6sV6FAYXsFcFJBVjFinRXykaz6yEN6vn4mArmZ6M2Ib-_rFuNy5vELDoX0uKf2Ve_5OeGZdvL4lf84pgOJdunWefqZxU0aePA_9c146Kir4UyQBrTJIbN04-D7QtoJoVK0SJBGGgkufY-BXD3PzHUb1Z5kv7tNCx7XbgMQkjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro31sAVs2YnAXUaFK_ewTA0g72l2_f-vJVMUlShDOpRjKycnrAID51yw6CelcJ_Ekkk-tgLVgvY8a1A8TGbZHEjp0fAlSz2mPqy_f5Yht50ro-pyJTWR1NvVHTMUfxJPkzcaI1Zh2lSWSs_KvcAJFbVOfJ1w4qCBAesHYE-pSp0qfeCrDiBIpujpAcQYiFhKCxmBiRYVaokiPjFHLM7EBl_H8THV-xT4UesAaFXqHYt6yMfDi6xUJtpOXmHAeqTroTrxakezxA2HVKGNXx_gRm47PNXJ00z9i3MJd010JArWB6PyfC2SjRoGQgRjDJuRZ64Dytq6IcjwMxv2f3il-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVs5ifazfixfojJdaD2cZ_theiU3XC1V4F7xbNDf38mBJJJCK6okEvh8FmomgoKgyeMrpS6Tb-H63jwJXzKCBVzjTosJIX9Bj0xpxJPQV7ojCKU-SeTBae9wd0uP8BvAnCD8sFmnWWzvNdwV08RkxdJynN242vD2x5irJDc6DA8wsjm5bX_acDAJY77Yx_vOmM6oOEUfghClmwQjxtCexSHcWVG0Pryt2sd9H5SeCwM62Iw8woVZGWixUDtBQUOMUINw9kOMi8RznSyvFhcjrbxPV36sUETJv9FkER5cDFkY5l5QEmzkdX5kVNibqieDW-HzcrXVh6EW6HhDeLfneQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwGwS4dHxZaPFaJnflQ-lTih9dcyJsy-ovJPWh8QVb-gHCgIPKCi_nYkpMkTZHGTCnJRnIelwMZMvcyyE_ZVkIskYQccQZQUecjCt3grOemmjLkTgoHiwsQwR_3i244YaVpLKved9-hj8LJPxZx4a68JtSl5mWJoU5QqhUwAT_3GNxoCGQq3TJV9-xe45bX8N214Iosnwqiel8kZEmrXQFinHihKRNTslUBdvYEKK8J52mTtE-qUk4vWOgD3J3RgsnUfMemDpOgRtKAz87JEbPBmOYsv3hr9aKP1Cxa6ixdDmVCsf6KwzVd7sHFUc2tae3RNbArr8uXWIZGs17duhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szOHrZvsMONk2VFefUkhdbsuKvHUodBikJStVLFEtEQ8-0FtW7ZwYykNPOVNbIol_SnslgKo7AXh_nFDIOACd9KdZeYsAPUGkzW0p1AOS1BhgWek1mUPy8BdaccgCYvzaUsZ3nA9WLWyAYAtb6HcQbFcQ699AGsAQtm8KFKwsNBDJVEcz4zaJ3JzWlEi0kqTzQYwBK9GnmzF6Cl8MgZ5_KYyCzCQ32qwTtDfDnx6mLnwRAiOBK_61Dg_uiYR0Y_RPXIjhw0wDpENU2IoXT8XwFbBVUaBpoQUwnkHcNIJY9eosgHm3tRfupNcR6T3fqSwv9aTL7LPTltPX204ZJYKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNvPmb0HClgvTF4kcdwnOiSCmzFrrJRIkFwzCx-Bu4dkgiW5djU7BxMJ4_ekkGWO_Sy9WK23SgVcaTOMhSjuwC6Fzxyoodk7X2EVFEA_8-8ptF0ZulQ8UYsa4bz7M9-BWVwxDuOvedeBwKGuSc7tHzkdm4S8gUp96IIDBydJXKqxyeuxmHILNWBShsA2ypTzBIfet22FrHMpKtFzqtUTu8IpXChkyzl4Spiv4wOZgmB-KC2UWRkCeF_a8VsPAyccs5QWMhgyHRatSDicMp8NNv6Xf_MXlLMuJb3mwfQRvLF_4icSOi3KvMIDqt-DizSnUbadeZwCeTIj70sPCCkZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKok8RgfoxCKeqJjcd_VqEe2266Iw8I1Nx9ICdG8sxnUCmFS5iVosUIicxLpZo4j-tWHEaj54e5V2zDqF0rzf86aVmDGkW3AQgVMR3Zo1g-GczB3_AxEEdKWNAB52x6DYnxxNQROji1E8TRe_0jFnHC5_b4VIDx8ez98sMWem2TYdlCINyo35EA0GaUawQrMt7iFgqUYd_CLPtjn0BC995Vn_n708ffcBcCEyG4rB0xdnjL_6nVu--QMf8ND6XQ420uzwGXbT404tzeqBS-_SUEmVwnAjqvpArNvCfeDmkOxMm-MA_HUUZst5GX5zA5eFVZ44Hl77Vi_Mz4tojxiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJZlqR5LYCth8k3y4Hym4Zg0ifwsQLOcIpXmc-_LArrTHQUUk23unNbfkV1zCx6cwshwSql3JyJDYden5PdR-g4RhtgYLfN3f_Z-FvcD8bWiBYI50fPQxdgErQLpg1wI1bX5ntBugwILwRou7vh_60JBc5wXWncWW6cI-K8HnNwKtZj7K9CAMaB4-fsA_Ia-vZERoGJft9yrgBAr9dt60dSaJUx1I4YRkpSOq5sAzk7btQJi8vYT61LjaR5UKBT9jAdPriABaCF1Gi2IEvf82NpCPSnsGMRfpWvIv_ygZwkoZzcfKpbHsNVqp1dIMffc3tnCDhPvhuSG5hPrR5cy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNLSsirVOkIQg8LyMR2XWCoNurMBVsTdx8rf-xFzpEeZZGpPKp51pDPIwYvEiuU0tVjH1pCAODGb4ZW5l2vVP_QXtT5Bmniw28xQfsPHdxXlSRTkti4kzYdij80T6KU-DRE-ZQfnjjM5sCQZiXxBKjE6EN_haMKGh0lXVwhOhxMRr0EtwgjuGPXxnZ1e8r0SK27zO5F3G9Rjek5sQBx28oE3VvzPIXR4G41VazziV6hKSI7zzdK-gggnixZFpvbaOv-7wTBX7PNFdXhODGZDovqB3pETBDVZN3bqE_tn6wozZh9WVpDVomX6JD2D-BOcI1l7kmZMkHKtGn5aV5GNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2eK5hSBBxdxMdMZAZC5z-2QltGe2sBwPTK8P2eLTUfWAdLLT_TWpoEvN5afq8-IX6roeZwJeFl1kFG6kCqMorRUfP5uZ1DjVAffXBDaPw-T5SeEU000-745COXMmJdjr4XYL1wH54XNLyFN21FOppFiL7hw2D__0k8vur_gLG_WzL6GvMlh0TSZlGdvTOXhgJQVDIW1pdsBPXxP2xhCKQ-jntMJL0wneQvgR252SIlk2LCg5de8pdYSFZ3e7DRk6EU9j7s2wdTUJzlsRK7uWvSzAxgbuWRQnT_UrIjEAFdfx9ggEaQkOaJ-HbmPVR5YPmjj21fix68EojqFvaRCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3_PH6Yy4f_VnxAVlVQzFMiJk82_vMojEDywkwBntk6SGg5MH6rX4bNgseOYxDNKVPvdAJwxqlRydLmzLDcH7CR9ENd18pNu3KJ2k5yMDx0_iU2gPBDNw6D1btomoc0q-x1KKZszJg6-TztpH3PP7tBoITiXmS23PPEJP-acTpsLlVbLSwAFigGV1uEI_QmC9jnDhIEH_WA62r16qb17unxtSxqrGR9M6rraszmg_udlwjKhIr7rg617GnqgmMs6S8kjKi79Wf_FFNecusu8gAgWkbRHNhFMZvDou64nZ6qjxJZVPaOlNkPatEtCAjkee_IzFORmbZfpyzWGMNntMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJm1F2ue0nsytQpC7uET9PBbRjpTaO6F7QTh_NCV3cWVmD2O5n_Ej_1LOPfuN3H6wKdlPxk1hYsGzIr6UXu3zrJzxXjXhM2Wi_7fl-t9NnznJ2WY5PFQm5igViT66B1E2bsZSHXAX5lNHHmxSpSmVdldOkb8lyLnmkzacfdt8-Tsi2_aD1Ef7VbUzSmub76yKmBh6iN0O-IEyJOYJuhdeeScr8-22YCZVr1TPoitHJPpw1eVjvpLM31ZBYo3mYAJET9ARh05Ua285CDgwt0Pj1oya1lrBHBALFATYXUeBCg-zOMqfM_mFDEjKvyUy-IoB-gOhyz0Wa0O5LhJCt-Hhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=OCJu9B0iAtJJPEjOJqk3ZLJLRxIFwV8n90-ZevHIfZi6CFZcY2hU8FpquuFAKlmNv0WoPptlrlVxkjLulukJ74L73S-21axZjzGrF7wvcBhzzKjnP94d1sloSG1XJUDEuoWnZGyoXGgOdsRgI5dSAUETp6x_Rpd6jrriKz7hwBDjT8exK1fRPGRvr6hctX9pjyLADHzer3iLmVmxs7tBS2WKG9tykdIClfkAZHapUFQvDbfNRUjHyh5qwL-sBJmi_AQGz325dtfve7dbkxK6uB5y7Ej7UEdp3k9tIMFYDGXtEQyOjFjN4tgmWrVLuQFOdwCxCm9nmrxD1edmJOKGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=OCJu9B0iAtJJPEjOJqk3ZLJLRxIFwV8n90-ZevHIfZi6CFZcY2hU8FpquuFAKlmNv0WoPptlrlVxkjLulukJ74L73S-21axZjzGrF7wvcBhzzKjnP94d1sloSG1XJUDEuoWnZGyoXGgOdsRgI5dSAUETp6x_Rpd6jrriKz7hwBDjT8exK1fRPGRvr6hctX9pjyLADHzer3iLmVmxs7tBS2WKG9tykdIClfkAZHapUFQvDbfNRUjHyh5qwL-sBJmi_AQGz325dtfve7dbkxK6uB5y7Ej7UEdp3k9tIMFYDGXtEQyOjFjN4tgmWrVLuQFOdwCxCm9nmrxD1edmJOKGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFvbd9nfQgTLdZa74lJwJ-Qit-aP27AszEEpX6GKT1jv7GPnrcfEpM3cD_OdoddgIlZullr_HiY0DDiuKRgSH-TDcO9h5b1BvqpKnztss-vZWpF89iaiJhKHo53J_xdnwVNHSZ-o1G6nR90XTB_lZsijZTTp6C2ZiI0SyTDiMeHzFAB4T2xg-Ss4mctu8CXGh_J-W__8AH1awDQ3jnVKYWuSx1a0quGMvecFEFHTbc8-yQbZrwVI6TERoOkIP0gTMlQLGfYt2-0fBV9zAFL6_7oqFAAg_dwqYgRgI69JA1eNnHleqmQrscwM1tVy3duAwCUsW7SfI7oENRnUZMqtNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neKSFTYame1eBVd2SCvn-ODM_WPixEik-yRtGdBTZn80nNzTjkk1nFAMW_h1M7U342ZVwCM5MjS0lNBag5_xw9aG30IrZ5x4scP-9OBBCvdSQD9gqoLXyR0peqOBmuIsQ4ZnvqS6EKO6kRJwZOc2TDJB9bOqOtcnLBuOBRkgVAwh625xMAaUUR41fGJFKx5kTtjeAnc3EvlzuHEiOkG0jBgbAIjU2wnEGaRvp2xtKBc1W0zm5prDPaEFWvlMyu0f71CBekiSPZN3GZYPq18LkqKbP7iyv36eN56ta8YjDV0gtSnh9539x4PbBaoF1xl1iqDQRS86FMgjeAUw6dMnZAqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neKSFTYame1eBVd2SCvn-ODM_WPixEik-yRtGdBTZn80nNzTjkk1nFAMW_h1M7U342ZVwCM5MjS0lNBag5_xw9aG30IrZ5x4scP-9OBBCvdSQD9gqoLXyR0peqOBmuIsQ4ZnvqS6EKO6kRJwZOc2TDJB9bOqOtcnLBuOBRkgVAwh625xMAaUUR41fGJFKx5kTtjeAnc3EvlzuHEiOkG0jBgbAIjU2wnEGaRvp2xtKBc1W0zm5prDPaEFWvlMyu0f71CBekiSPZN3GZYPq18LkqKbP7iyv36eN56ta8YjDV0gtSnh9539x4PbBaoF1xl1iqDQRS86FMgjeAUw6dMnZAqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4BO4PZeQWp5_6CTAZ1IfaytVvtZkL3EQSTLsEKJydbpvljv5o6tuh2B6iDXtuNPmBO9Q-9xDhHo8ISUwyi4y0S1pjJ1u8B8Vur-Zj7tuiZDvJVyaSBg5CECROCN_hXGLnFz9M2Z-k9WjJzPcxC8qVberHfRT3WlBrTVw14lZcdqbDFXYlHjtRdRl1REN4fHOBbXuMiNmN8ZUZvWmYZKNA9OMegROs1xxaTOV2dcXeCWVWtuyHyftCORQUuWTz-t1gTWnwaDTNoOxEb4CP7J9tkrkMWgmsc-rEXtFuWCCSKPXkSRBAd5ed1_GsBWsUXVeS-uI7PV7d6IV08VgF-VSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Asom4PXkknbiSCG9JvRttUcjIpNxBMnfOiyQXajXxx51mWPCBcmuDKQmWiLCDhdAa0sGpRQYlmpjbByaATzImnhFG2Ymii4URXMBIm3ON--jmNg1Bn8X6xneQAXlOMB9Ujv5k6995_usnMfNxwAt4enZpHG3ckv7dsfO1lWErLTXDcqNcQwrX6hBxVBkIfpjrcH4lbp8Ravi83eHYd3NYdPSBcyzdmfL2fv0La1s14xLeWV4thOVJeHgWsfGvUuBbOqeBDAcS37V7SAt8ImU_-dPPMeriM_pEB1ga0jlCcZJy3kjHAxOyUdSndUr9eutC3h_Lzjtv7cAJblg4HJAvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLfqoaWzhFCbgA5PFnjc5fDg0Wvp8lpH8anqT92BlTba0zI4jPw8m2EKXstQmwNKJ45DzC8DDapHB2URPbcFTF3ppYd6R1hfIk3vmuF6tdlZd8cPOWeoN699NDi_HWpbjDp9fW-I9Elebo20aIbU9dBLXg0lmfhL3kS15Ichk5Cb4ivvUQqxJsvp-6sjbnqJiPPnj_5P-bu0ygIc3qNJlA6HBXIA6aN8ZgFWDQ9a9C_QMxpp8atjGh6k0rZYC-ee_uO_WWaAcWD9IGiYVJbafeUDKcP76EnA75LJ54850vTU7YOzjSC2fITKlgz9bOng-FH3ClJYMWheZadKmc0BEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhAMiSWfjbtZZkFlomhKYdZzdH0LrWwIXoWNwTl3HKvv7xirh5J8JSoWMR-l_nMi0ak5_YUOPO1DvRd1implg8cUG0HhqtEx5gTd6j51wQujLrgly9S3kUmOYAM2CNxyn0lGZ1Ge6LUX3S4dfH2-pjtUE9_8ikNHnW5-5eI651otFvNrEc9UHltLYMF5MShL02uROz0VjAIxjGydIww0F8EetYQ0VJd1YGkf49rDqFeXPVGobZ9kkFb8m6xrNCWtlW4RKU_Ltyi19Bh2VK1a8y5K4qiGmSS4yZ45tZXXWTbmevgzGXTZpXrHJlu0rWizEzrAPdwD_zWDUUdO_fKuCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdqVZ2K4hMqpuw-z3qPKorFp-W0ImMua81bytGqHk4dEA1yicDORlJrzCCHWsrQ8topuI_71dbQxcEUoEhMYlYrj3b3c6zyp0sCZ7YwUq7uOlc8Z-f1oMlAHmcubRIq8WtXjfgcEflOkmc4sMGgmLe7_sxw0pJtDk8bHl08_D8Wpq00cBsQyW1CwcvO4I6fEOJXko49tCwf0oXiBme7VaxKYPovL6f0KpK6y8CLEQagoiAtKUqrWW2p9OjrNM7hksbanqvD3KRiAs0V2_mwpG2jkUj8pM6uzX6bpQPnidKX6mbHXEDPSH-iXZhiUZc-RyVtIaDjDdUZXYaLIxe0orQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBvoA8pgR8Qm5kHwZUal3svtUzVibCR6P0Npm6NrRj4rlWQSfSbbArpYG26_CsFdGH5L-prAknE5kkSuvb6GjUJNsLG17dRmTcTyuRyU8Z5mSZ0MUyFrmMhJB61_DOzz2FFUrVPRHnTmItlkC-x2kOe7yYeooMNFXsciy6MMh6_JdIZkTxG_u-rdenyD_tPszJv85UpFDc0Ayc0LJX0F27SsGczHCDteitNb2wfbh82_8HxYkLYzCPj91B5CS1J0TUnw2KsR_o38otzlaiSowGzVYrK3hGl-yknpkICYJ0hT41xFf7R89l092KWA0VqP59uf9tZTSvsF9pGbuZPsHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
