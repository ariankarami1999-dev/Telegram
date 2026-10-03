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
<img src="https://cdn4.telesco.pe/file/P1B9SJAAZxVwbOAq3Hb5KNL-aJBwx1esg_xSw8cjnLOCJcjtAo76HMA6oiEh5aX6wVNHMHf7K57fXaZI6MBDOe-4bQHo2p7V-3zBBtbUtoZm67NoJjetmb9iNGW6ZlLsK2o2EQCgjZNxcQzkHl1jkGGtmGW3g2jMbiiNzUKFaeX-rdtUui6fA0TH8RVKXMq3_-a7O0xa6eBmJQGagIcoxj1997Uny7saeneMya3-3H9CMe7pfZkpaYXqboJMDRAjBKPa2cFJOvJKz_3VQ2yWr9icVBWKdjs3YrEXgxSJdGwuM4D1UoslxmqEVRY8dOAKZhs42rmFCmbas3F-Us6reA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-466016">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhZwfkeH4kRG2BBsfmLQCr07yLLH3fYJu3j88KPZ5DRgCksBh4hCbrdPR8OXkfgSR74yCjHRYGzKWsOHOLYeNfk36BV3rf70syqm4z0mZsFoogu-U6qdndAgz3WIDmpHCgO9re1OK3Aw8qlwGaJLzjTyjkviVxHgMNpOyWvLjJjWdjLAN-w8J2lI_Rmv1nRXRMEN18xqMmXFIwHJhcNHJn52baygzbms0DM2EEt0qZCEHOEy_jY5RU-FzeykLq8UB572aA2Xm_WJRuhuy_gPScSctc1zaCzWoglHU1cdkfZ_s_DRkZHpOmTd0ZvWkf4ghF_BspzOSTHLvO_V4pjBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز هفتهٔ بورس با عبور از رکورد ۷.۹ میلیون
🔹
شاخص کل بورس که امروز رکورد تاریخی ۷ میلیون و ۹۰۸ هزار واحد را ثبت کرد، در پایان معاملات به ۷ میلیون و ۷۸۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/farsna/466016" target="_blank">📅 12:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466015">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تیراندازی در مقابل دادگستری مهاباد
🔹
دقایقی پیش در مقابل ساختمان دادگستری شهرستان مهاباد در آذربایجان‌غربی تیراندازی توسط فردی مسلح انجام شد.
🔹
پیگیری‌های اولیه خبرنگار فارس از وقوع تیراندازی در جریان یک درگیری خانوادگی حکایت دارد.
📝
هنوز اطلاعاتی درباره شمار…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/farsna/466015" target="_blank">📅 12:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466014">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f96ccd1a9.mp4?token=lHbYSOCvxfP2SgfSs5nTUkOHyphNZYvtj1lWw5RJvqtJ0_rEX-yjUDuuXQweyjt4cqsvapB_2TitiKrWHcLuSCF7Mfab0_TzoxY5Is7-NqNX8I3dt_WURgHa-l3hHQpzXecXu9LXZg1AFoLQ9nJgdo7_kwkUS8cRG5AJ38dN-tOAwGnrjqxEIe2e5ot1NIzI-lP19UBdOPS16j19tye2aEp8TWe9ltG5QmS8i6pfDv5l6M7uA-gD-FEBoWq0dfQ2NPtrbSoGr2VwL0l-WhSNK6exBhiITnlew4bF7gQyWIJIZ4zA9d9aCRtStZSS0up1NFCib73HoQN4Tm4KJuGIWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f96ccd1a9.mp4?token=lHbYSOCvxfP2SgfSs5nTUkOHyphNZYvtj1lWw5RJvqtJ0_rEX-yjUDuuXQweyjt4cqsvapB_2TitiKrWHcLuSCF7Mfab0_TzoxY5Is7-NqNX8I3dt_WURgHa-l3hHQpzXecXu9LXZg1AFoLQ9nJgdo7_kwkUS8cRG5AJ38dN-tOAwGnrjqxEIe2e5ot1NIzI-lP19UBdOPS16j19tye2aEp8TWe9ltG5QmS8i6pfDv5l6M7uA-gD-FEBoWq0dfQ2NPtrbSoGr2VwL0l-WhSNK6exBhiITnlew4bF7gQyWIJIZ4zA9d9aCRtStZSS0up1NFCib73HoQN4Tm4KJuGIWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدال برنز آرین سلیمی قطعی شد
🔹
آرین سلیمی در مرحلهٔ یک‌چهارم نهایی وزن ۸۰+ کیلوگرم تکواندو بازی‌ای آسیایی ناگویا، با «هائو تانگ» از چین مبارزه کرد و دو راند پیاپی به برتری دست یافت تا ضمن صعود به نیمه نهایی، مدال برنز خود را قطعی کند.  @Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/466014" target="_blank">📅 12:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466013">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izi3Poz--GNGTxJhC0mDe7uEc45b2YWJdbHBQ0WtjqvW5-nxjWSnvINujIeyyWzKoNChLuYKr5KLa-uv-Y_y64QbB_iGQZJYErY1dj0cgQKoZs13VUTGKHKk_t200WCGqEOKgezKJSDu1z4ZnKmS_Zc6inc0LrDAJdFtZB8Rv2s36aWccOqzphqdMwRqJ24JjXzGKS0q4fieYDA87tWske3Kc-_bs0oYZYjlEo7qvTEwbU7R7OZ3zXHO-GvrgO9-TBbXs-z5EARJ0v0z24hgZUvHWqMBPaoaJDJOkwc4jVMTyfLdJTjowlsgGpIFeO5mo__jur-2LcEnH_jJPU-thg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر وحیدی: فراجا نماد پلیس مقتدر، هوشمند و حرفه‌ای است
🔹
فرمانده کل سپاه در پیامی به سردار رادان نوشت: «فراجا امروز نماد پلیس مقتدر، هوشمند، حرفه‌ای و متکی به پشتوانه مردمی است.
🔹
فراجا با تکیه بر نیروی انسانی مؤمن و انقلابی، توانسته است پایدارسازی امنیت و آرامش اجتماعی را در هم‌افزایی با سایر نیروهای مسلح و نهادهای امنیتی در سراسر کشور تحکیم بخشد.»
🔹
سرلشکر وحیدی همچنین با گرامیداشت یاد شهدای فراجا، از نقش آنان در دفاع از امنیت و مقابله با اشرار، قاچاقچیان، مفسدان اقتصادی و مخلان نظم و امنیت تجلیل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/466013" target="_blank">📅 12:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466012">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تیراندازی در مقابل دادگستری مهاباد
🔹
دقایقی پیش در مقابل ساختمان دادگستری شهرستان مهاباد در آذربایجان‌غربی تیراندازی توسط فردی مسلح انجام شد.
🔹
پیگیری‌های اولیه خبرنگار فارس از وقوع تیراندازی در جریان یک درگیری خانوادگی حکایت دارد.
📝
هنوز اطلاعاتی درباره شمار مصدومان احتمالی این تیراندازی در دست نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/466012" target="_blank">📅 12:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466011">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تشکیل پروندهٔ قضایی برای فوت ۴ نوزاد در بیمارستان میبد یزد
🔹
دادستان میبد: برای فوت ۴ نوزاد در بیمارستان میبد پرونده تشکیل شد. احتمالاتی چون قصور پزشکی، قطعی برق و مشکلات زیرساختی درحال بررسی است و نوزادان برای تشخیص علت فوت به پزشکی قانونی ارجاع شده‌اند.
🔹
تاکنون علت قطعی فوت مشخص نشده و در صورت احراز قصور یا تخلف، با عوامل متخلف طبق قانون برخورد خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/466011" target="_blank">📅 12:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ki6b4EmtwBacD1sdzIz5vIggtyVcFNsfkBBdBn_vVoEQlVtrm4dnfatEo28CH1R37aRI85WcOPi2WTBF5MA4lvwxtE9Tx3uUGDsZPcpw0K2aeMEic6KHF16tv_0Abl8_H_NcWeYEG8nHtnFZWY0n4ifg2vXiPHowI2jq4dKL8RcNEy2gaJ4IRnUHhjpDAQ6C_4XTOQLxU68VAgqt3qqFwgUx4tojjefGfNTG7DAvWuChlddbakpkup9UChiOIJn_Du_130xoFiA0xqDyHLHlFIGvQPYozXvhuPTkU4Q3Pm7i4FFZqNMxLVTL8u76x9ZRQPh5YmoyHIeUjlZAV8CaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZu_MPjmaj-mh0r5txVaDOSCOT5YFI7rgWgiLhwra4awJHCG8rgOfyRtpml5yO62LNU2hkBGvht7kGRDrLWszsatHkUGFpjjyIULsKHsAnWHknkf2YHwnaUqUGY_rOdjeS3cR-TnonyhOLoKWOUYMs-3JAfZYjeEjDTXL7pRSTHzJ4n9BDAUkoaBvPnxdbnLlDwiY0uZJi3Kl23wqCPITitkTliyxpUYDBh4aEAPBNiWAnQa0pEz-UysH_cLnjJxuRH2OAnNs33vrH9WK9OEb1WZX_oWnJzkg3BOFM67QHKkRDnsnRqG_mA-GFCU-SUmJgdWagvXr-VKkR6cwL7vKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اختلال در فرود پهپاد جاسوسی آمریکا
🔹
یک فروند پهپاد شناسایی MQ-4C Triton نیروی دریایی آمریکا پس‌از آنچه به‌نظر می‌رسد «فرود ناموفق» و عبور از انتهای باند بوده، در حاشیهٔ رودخانه در نزدیکی ایستگاه دریایی «می‌پورت» در ایالت فلوریدا متوقف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/466009" target="_blank">📅 11:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJQ4cF7P6jC-QyUSgpgs_qt1WaiBG41L0LaSFPbVGzTYX6uBL-C4nb_zfHWCMxRkfaOsFxnZP6HcRWJJAPAL3T4J8o2wXjVOSE3KdmBisFzZyGTBn-sULGdsY6Iz_4OdFTpCD2PJWFoGaBEvrB5XdX8z-Vp-KoNPTTSJIPJq_QRFDT6Vfb9mjGQCCAbkRi3S48MjyKd8OYN_XTx0B0fwn8tpsoqnIrcEKy_2YnXNPojgvh7-s5hR5wSOyET5EPde02odP2dcRTAfA5ryNtC-SwOT0V5c0uGeyXEI5lgf4P0-nqHdigKgDCXehS-UT-m8I63hvfD9j17uFVooJMU5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس مهرماه سال ۱۴۰۵ تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا ۱۳ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/466008" target="_blank">📅 11:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d0da5230.mp4?token=gKpzMBoToGQcngRUkJX5-WruPiINGfIlOSW1umTR3gOzCpFxE2Eqy2SkAV9YevLI0BdYIgiAQ4ejEj2uL2aV7GLMhMg7ImBc8ciWIyj8uwxJpsbbpzYLsFGCxL-6UJXJz_MCoyw_CJW_R9A73sawfC0hLD1XCR41MvanwfqOVud8XKFZjq2Nsvr2f0cmCzUleQC3zIZRL1XZurRu5Q-F_h3TEhHHo8jaj34VY5f6zpINdh_KFtZzcGhc9uZBVr3-cnJ3gthb8URGo1n_D6v7a9bNE8Au2Noiaw5QQL0MBieiAAjR8YQOml2cwMVS6KTFPdoNGf-efShs77GNN6_C-Z8qZV8tKvEwC8EO8iO5hCfNMiMc0eQDo3iqm6Xk0XUgCP3yV1JHxLi1eKZVFEKdTljPq2h_65zgcHRKKXNjWCbCIYL_wz8jmouqhHS3WYAepg5o7G4HtCDqEv_lTTdXtIAmD2sssvOqmjN1LKu5cPDkiJbkkeFMBb8yOHk-hKOMf-3j6hFkOiXFLWugA8mJvZnvNIIfiV0rFPhWaik-1AkweHpMiNrSjKIU-qzuEzanHDXVJdkDKEOnBlDozCJjqgrXCgqQ_Nx1jlj8XPRNEVibUmT4NiUPd8JLuUpcHBNwW6ruuQX4tJauF4pE51OvrJi3mWVgC3VjVEgKCrVb5MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d0da5230.mp4?token=gKpzMBoToGQcngRUkJX5-WruPiINGfIlOSW1umTR3gOzCpFxE2Eqy2SkAV9YevLI0BdYIgiAQ4ejEj2uL2aV7GLMhMg7ImBc8ciWIyj8uwxJpsbbpzYLsFGCxL-6UJXJz_MCoyw_CJW_R9A73sawfC0hLD1XCR41MvanwfqOVud8XKFZjq2Nsvr2f0cmCzUleQC3zIZRL1XZurRu5Q-F_h3TEhHHo8jaj34VY5f6zpINdh_KFtZzcGhc9uZBVr3-cnJ3gthb8URGo1n_D6v7a9bNE8Au2Noiaw5QQL0MBieiAAjR8YQOml2cwMVS6KTFPdoNGf-efShs77GNN6_C-Z8qZV8tKvEwC8EO8iO5hCfNMiMc0eQDo3iqm6Xk0XUgCP3yV1JHxLi1eKZVFEKdTljPq2h_65zgcHRKKXNjWCbCIYL_wz8jmouqhHS3WYAepg5o7G4HtCDqEv_lTTdXtIAmD2sssvOqmjN1LKu5cPDkiJbkkeFMBb8yOHk-hKOMf-3j6hFkOiXFLWugA8mJvZnvNIIfiV0rFPhWaik-1AkweHpMiNrSjKIU-qzuEzanHDXVJdkDKEOnBlDozCJjqgrXCgqQ_Nx1jlj8XPRNEVibUmT4NiUPd8JLuUpcHBNwW6ruuQX4tJauF4pE51OvrJi3mWVgC3VjVEgKCrVb5MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌موسایی نقره‌ گرفت
🔹
مهدی حاجی‌موسایی در دیدار نهایی تکواندوی بازی‌های آسیایی مقابل حریف تایلندی شکست خورد و به مدال نقره دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/466007" target="_blank">📅 11:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTaOcPF6-D81vvL3pRYbmE9IK-elrhFKmcBnxwcfgKL8UR4txWSwLvbvBVyqLD9lrX8k9CF-9JfpeYKUzp44zgktb22RGMg6sMQqJiFYFH_dGevrF6c3alvRc8R2bUDvbcfwK7eUBPVfrSsdWIL8JglGFZCZMtSN3hSzr3RsRZCSwU3TjnGU1N7fFjUQ3VN0wRQ8Od1MUS93TZh5sc_RPsp8bnH-t7ByrZOvDGNdXEe4O1MJacqIXmwa0waHaeLfxrY5x0VaRTF1FGQzGVjUQL2hl9an7SzL8uC_4Cb88SEIWtSYIqiLgU8k1uR9prMYs9b-PIPUmc_yTItD0vJi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی‌ وزارت کشور برای برگزاری انتخابات تمام‌الکترونیک شوراها
🔹
وزیر کشور: با وجود شرایط جنگی و فشارهای اقتصادی، تجهیزات کامل و کافی برای برگزاری انتخابات تمام‌الکترونیک آماده شده است.
🔹
تمام تجهیزات، دستگاه‌ها و تعرفه‌ها در سراسر کشور توزیع شده و آمادۀ…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/466006" target="_blank">📅 11:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466001">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBCp0YtFz4dhm0gwDwOkiWPHEOU1DGuDQRIb_EdHMi7J6OJp1sNLEwyn5CXjcj797UGVQ38_8FCTnLRTRYL7zLO5O0Zazv-FtNgyxNEb4twB0-mOfPxwNn7NLtZdlFtWMrlKrVV585q8_7LZ8DH0D1rJdC4qPLL1o55htNbaG5M6XMzkWMhX9Xt_Zr6-laXJa3QF-FvGLKyD8SZErRC5TiuQ8Q8AMltYTZBVBRi5ZbJOmemQtF4tODutAG-R-5tE3PZmtPCIx44Q-DM13k1BlDC2cTEaL4Oy6cg8y0fZ_-UIVeIgzMWMVDc_hcBAM6uZgjJQiuKVHLhuFtx0vi5Zsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puirWOTuT7rTFglLJqmIJoUVKZ-yB-jTsHtkCwyytCwhftFf9iz2h7r5Pv4dhgan4ak1V7shLcZlztPkj-DAXTuZh7u-Mo4zu80uu0yS-hxe1YBHY7vdCrKn98GHU7BVfEmSGiR6c5IHKs6FZbEfmNwUM4CY325gcW6J4MIG3_aabZkbuf32F02ArLOOdtvD8bf__AjKzsckOab1VFhQ52RssROIR_4U-i8wxTWnNmrK9KNtlH1WcF65GydH1TBmdJaVmhzRj0m1wbXeDnxNeH-r0uf7RbkGa5_MM9glowM5mTSiD40s5qzVgYZEcqVSa4MVfYwAQzaRTiVZ5aiQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHfYbctcbi_UyiDSLfb42PKy4muwNzsBvqtrws2IpThL7E7rJlwuR_7Zum93kMEN51gbcnfDrYCsnB-YCKAbDiy092y3gZRNJZU7m_EOtqg2ZsCR7v6oXxdxCjLkPcBBGC87-NrGjX0Dl_yd96S6IGGE73PJwt4ulYyaGnCWasgp4cSSs4d-lDSC5p6Y7HTSbrA51zkNQwXrLrKOQrEivXMZiLVbpJ3F7NEQiVTOhkZVTpe5t4pvL-OiYtxzp2lZoavVwYFgoS75EYowxmzSEl4uWD5dINGBTxa85YyNzV5PCTJJqoSUlqwCOiNGNeLaDtxixfXuTlpk99mM4-0z2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGuIKFHp7_4wRuF-uscxwIyC0h-rhhOFcd-oge9rrv8kbA2XMyiahNR_h2ehzI2if6_YxVisSGmdBIhuwgpFZpavgRCxY0kad7b5Cr5E-81ixOkO7Za8Ia7LyrfwqteK9mmE1cRBrBAuRqyQNe8EUFaH0gYCc6QSqeP_t8UgkqdSEePkhMdpwfZrQlzIRq_Lwd408SnaGnmygIXMmm9Pn9YsXBN7vAt3kpITuPBbbwVdUNLk-XGDTtaOxZ2u7kFoo66B5AWMK20YzrjUjpJW-TAtRtNBT7KXQnOQPdiD7kdxIU5eKQ9jg_aYJhiICKgH9t2QdJeAZuZsnIx747KReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuolJ9OMhW8O0HYaq1X_CEAubA2iqXYP6cdLogMB4lm6EzkOb00JOYbWs43fKKm1Aw74p6pGrL25KVesrLimgSXn0a1XcjW5BN-DuadQozdUIJMdde56dxjG2Z6s698trfRvJ1jQh-G30tl7zPG-7e-E1EckBM4RLRSFDtPwWJfkaCjmUXe9-CnMoPDCVqjYK7MIBGBy4p6UaS-W_gtSs3GLchmVZBJibleOad08OniYtuXGjqJyNwma62-TNa1f5nJn1vDr_U76dvHlu0FLA6_GxSh49wQ2qcvS2z2P_zx3LzXjHBsQpEucTFTjtSOfTbkJpgBv4HSK-68Z2-yevQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روزهای برداشت پسته در پروین‌آباد مرکزی
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/466001" target="_blank">📅 11:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466000">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2BOf3J_z5PozYWkrHKwUBmPaytcpRxvLKCqa5RssrhOYRz7wWUfW2EvtjCWI3G2-WO3yfr0yZ_4Q9bUZxuW9RQmRpOFzrLa_CQDYAAWn3b9k9-CzAsNGB4XLAWm3UVSfuauCPTf5N_VYNYB2mUuB5LJ7XKHeq5Mfiao55CvVg_QaDlFEn8NskPqWIVG95GG_sSSLawCooRZMuAjFEh7KDjODeCW4cDYT_ORlkWabXUTYrJiCo5YAVACapSFhKHmVAPuiXUKXpRo3-wJ9ND4Mg1dmWUstJe_DQ53vAS5yIWvClrgq_6xLjSiYP9dOMHGNty9kfYZc7Y11x30i2aK0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه پاکستان، میانجی بی‌طرف یا طرف منافع آمریکا؟
🔹
در حالی که پاکستان نقش میانجی را بین ایران و آمریکا برعهده گرفته است، وزیر خارجه این کشور خلاف تفاهم‌نام اسلام آباد، خلاف خط قرمز ایران و هم‌راستا با منافع آمریکا، خواهان عبور نامحدود کشتی‌ها شده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/466000" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465999">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84cfdb285d.mp4?token=Tg6vwd9IJTmvCa5lq7hicddPKv7N0ZJHl8oZC6tr4R99MR7qR1ALnjjA2HYb3tCEtw2VIRh5Nygb9maR90-DSu3xS15YsPTvuY8QMDbQVRr301wT69LBwmAzzaQFaqHyAfjVqagm8GPPFVgRf7fiRhJxRykZPqhNeCBN6SdhuhwJq8HMrziGlkoa7dPiWtHpyoQesmbwRzRJ6ItxzIQbTyHGryhPPzgxfO8My_GuzQaBhsUflm9P88PEvHbwatC5sG69sV1bNFXLOE5ZazJThKhI9IVfBx6e6Ny4tgARK3oE8ktGpWbNsN9wiJo43YmwNuXReqOtdGNuJ_R9ZJfc5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84cfdb285d.mp4?token=Tg6vwd9IJTmvCa5lq7hicddPKv7N0ZJHl8oZC6tr4R99MR7qR1ALnjjA2HYb3tCEtw2VIRh5Nygb9maR90-DSu3xS15YsPTvuY8QMDbQVRr301wT69LBwmAzzaQFaqHyAfjVqagm8GPPFVgRf7fiRhJxRykZPqhNeCBN6SdhuhwJq8HMrziGlkoa7dPiWtHpyoQesmbwRzRJ6ItxzIQbTyHGryhPPzgxfO8My_GuzQaBhsUflm9P88PEvHbwatC5sG69sV1bNFXLOE5ZazJThKhI9IVfBx6e6Ny4tgARK3oE8ktGpWbNsN9wiJo43YmwNuXReqOtdGNuJ_R9ZJfc5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بوسه حسین یکتا بر تصویر شهید لبنانی در منطقه نبطیه در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/465999" target="_blank">📅 11:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465998">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e49ed69e1.mp4?token=orEZdIT0RWFeeELP_5OreYG_2TRmmWp_p-zYitTZQVcAzzvee0qNBqlSM5SLOZemD_GVzcAn2u-jhcP-Eng8V5Ux3kV7S2y11C7IaBnr4cPYDLGkPBUDdpy7Woz8lrfcC03D9HrYttZkhwvlLkV_f6Bvp4UkBWx3StwH0n0uaCH-Ism1wxc-91PeuHBZj1lhD5c10KHf46ix0CWFI01vpVUuy__kfSGLnmUOCk65Mk1R8EaQjz7fzMj4AlwOJ4551_l2kZUDuFsat-H94UjPPhnx-gNNA-lo4qT50Mh33EcmJvac_kuKKCqL5oWRiec8cjbCMJq7RUYz8YNRchJt8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e49ed69e1.mp4?token=orEZdIT0RWFeeELP_5OreYG_2TRmmWp_p-zYitTZQVcAzzvee0qNBqlSM5SLOZemD_GVzcAn2u-jhcP-Eng8V5Ux3kV7S2y11C7IaBnr4cPYDLGkPBUDdpy7Woz8lrfcC03D9HrYttZkhwvlLkV_f6Bvp4UkBWx3StwH0n0uaCH-Ism1wxc-91PeuHBZj1lhD5c10KHf46ix0CWFI01vpVUuy__kfSGLnmUOCk65Mk1R8EaQjz7fzMj4AlwOJ4551_l2kZUDuFsat-H94UjPPhnx-gNNA-lo4qT50Mh33EcmJvac_kuKKCqL5oWRiec8cjbCMJq7RUYz8YNRchJt8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رتبه‌های برتر کنکور امسال از کدام شهرها بودند  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/465998" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465997">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dc49736a.mp4?token=cxyh5zmHk6BB1mzm_NsRmTDmtb8oGH2cDWShykuqbx-qWbISupzDzHK84cA_THFeUqAIh5Kx9zmqwMuzf10RLPxge_NVmPHeU0LpE48hG-gd7f6pg31AblvGlvLOzBFGEQC5NcBHbMqmpK1at7kj7O1Th_vmOMrpnW3gQt9OiS31eGFlYOh-iMxyQXOu-yb2X5KsM_KUwgqrUmqE4SJb6NbNx5NkyoQhVBSeA5phaJyp-YkP2l0qS_-f9PUNISY7fT_izAooPX5_J_4p2rMzUvWa0eZu8twQ1FD2TJibQr0L69DZysCM2k7GXF4VEy9l4yijZoH3tHJOB8Hyi4n6YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dc49736a.mp4?token=cxyh5zmHk6BB1mzm_NsRmTDmtb8oGH2cDWShykuqbx-qWbISupzDzHK84cA_THFeUqAIh5Kx9zmqwMuzf10RLPxge_NVmPHeU0LpE48hG-gd7f6pg31AblvGlvLOzBFGEQC5NcBHbMqmpK1at7kj7O1Th_vmOMrpnW3gQt9OiS31eGFlYOh-iMxyQXOu-yb2X5KsM_KUwgqrUmqE4SJb6NbNx5NkyoQhVBSeA5phaJyp-YkP2l0qS_-f9PUNISY7fT_izAooPX5_J_4p2rMzUvWa0eZu8twQ1FD2TJibQr0L69DZysCM2k7GXF4VEy9l4yijZoH3tHJOB8Hyi4n6YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف‌های طولانی بنزین در امارات
🔹
درپی افزایش ۱۶ درصدی قیمت بنزین در امارات، خودروها پیش از اعمال گرانی برای سوخت‌گیری در جایگاه‌ها صف کشیدند.
🔹
افزایش قیمت سوخت درپی بسته‌بودن تنگهٔ هرمز، گرانی نفت جهانی و اختلال در عرضه و انتقال انرژی رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/465997" target="_blank">📅 11:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465992">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwG_g_j2bfWuG_CrLYhMp4o0d9XQfFvq5w7hdbiQpg1QbHR4Zt9TfCh_he9qRYddVMWBh2q8TwMcOxoFxlCEBiKs1MVOww1w370auNLC7HzLynkxuBbyMaOycW3BCTZSVK1ph4xQul-Mn4ZXTHBsnj3Byrw7155KDDptV2hLU9e2V1Y277GapMHjarFgGpaFfOXLtBeKgnO0S_GYiRi6Fvrc6GrQFFuVcG9Cdbe-Qh8mc4Zx6uyzNp0TXY5q4PFg12_yhuXOMrKNsuqT7xmxwJL73nw0KAmr_Qi-WwkDqtcoxfu0WhsiEvcZvAxBlvJOL2i5Vljz7dkAaN9yrdsUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKK1Ijomhw3VAzOwqaXoymAV-mKz6cL3IqXgi2Js-2BW3Vg_Ppj6CTySkUFR5y8ygUSjCjY6P8sxl4qcSTRMxmGqM6jFH5gLxAm9eNvPioFyN-NE-YU5_guDwabEgpHJzfijl66ktfaWB2K-XuFGnILTszqmuDGxAs7ggpmyb1yaxrc2VTKm_NdcU9KeamK1rAVM9Ybmz9WynANGmG20jjIORjuFtzVJtzISMxuLJnhR0zvhx6lGhjOcotRi_PP0Bo4Qk_qBQabD0DiaChILLeKVgwHRDT0GEMSmqDoBCy2urHyh8GDOVz71-EWt-ELGNMBtaRPAFdgg0H3pcQ-UcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2Ru5-Tlcw97SaElF6KC94NeS3taJFDVHvYReKHXfBIhG6xEg8ij5b8BJXtojqLtJVl9yO7utCwwju30yBXZfzQNrfcmztx0cT1G5CrFTnU4Z50KukSZYxfY2bEgNDL4MvdRVj7SBYPe4whVevJeMRbMyztW8LmE1X7pQqrmzLkecTTJXmIMy7F54Pam9UkY0noRs-JA-DU_7y22Sr6yecUoQhfl0U09acCZ392jQrHSC7c-MEYx5ebMGGiHMzViCk1CInT_7XyHMARvQhjsgxKvlUMuxsCqycXRhwWKtCxgV0j7-m0EpCdfcstd_ANBi9n3dHush4QEvrtdNdCSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTHRtR4xz6nOwdKLMmAS_JqW05IV_HAbZfUgeJM1BhU0hObHYIDTwAkiwfWyC4W2US6GwjCRDXP1Fvbgv0wkRweLgglbxPScGf27vb1Q-5kMeZwNXzAAjFLJMowISOlVcwJUD2Kkx00P4WEqKAAgFIwKKWI0LO2gVrQJ9XR9YrsiTWIGX29F41uV2ygSR_tIwLtoPwVNd8sfaApKqXTsjWs6mS_ENykHRMYNR_cZtTfX58JZjIB6t5MY56JJ9GQ06E9H4YOsMc-yOhrKwWo5tX44v3jRxedN7x-dyj4Jv5abjEOWnrw0T5Js76Uwy96JLieQmVzjETp39yltP4t2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SF0KngjQ8IJSaVw5ynkNHBRhN4MWDfNW6XKrAhxIWHBscAaSdgyucd8AT4CcO8dVwD-LseAk9teEcn41KOrieEMMGGjZhAYbTF5EY8UBJu2GGq8_SE2VBzO58ZcBiLPCqY1jqnU0BUTG2eebtDBLWdTows9IIbWgpfzaNCwnaHQ-zmpVuwkfmdMyj2NvUxB3X0cBsCjcJZgN3QFVMEEbqTgut88crAC3zYxUlvcMGxVXZmaafV9yeR7s37Ygwja8Y_umWerswCuCkwKOzOj8F-wnJLeHWLUnueoOV4olmp3kOeVzx-gBZXfchFECT4PdxPMNkcg1KuVQAt3xTRZYzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور هنر
🔹
۱‌. غزل کرمی
🔹
۲. هدی ناصری طاهری
🔹
۳. ملیکا شجاعی @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/465992" target="_blank">📅 10:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465991">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d8a9de0f.mp4?token=MAgadmMe1iTsfdNs6D9lg-4FGzldAL3S_WEQeaMau_lMHxU__pgMednj6pYNTxDbo6DCxR2VfkOPUE0j3gosLC84DCqQcgHa-T0dyzv83TjDsBjFDffOLMHLbMpgT_1KlCZc_o1BvlqblUhODOCQpYYL07woyTmwaS4JKlB9cU-TKM7z5kdYLj_K3DU210aWVle4OqtjKJxTaP_eVuhoj3y1e-4GA3a7pf8rpGX1AkKPx7jnbN3Rp5KSS7Sxupfw2Cy2RZIarKPxCMTHW5jhp8xyDcupR32hf3g0yxZIuLLH4O2KRo-HyZ3jav7M51Uvv5R_Zx6TE_njsxpxqXW0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d8a9de0f.mp4?token=MAgadmMe1iTsfdNs6D9lg-4FGzldAL3S_WEQeaMau_lMHxU__pgMednj6pYNTxDbo6DCxR2VfkOPUE0j3gosLC84DCqQcgHa-T0dyzv83TjDsBjFDffOLMHLbMpgT_1KlCZc_o1BvlqblUhODOCQpYYL07woyTmwaS4JKlB9cU-TKM7z5kdYLj_K3DU210aWVle4OqtjKJxTaP_eVuhoj3y1e-4GA3a7pf8rpGX1AkKPx7jnbN3Rp5KSS7Sxupfw2Cy2RZIarKPxCMTHW5jhp8xyDcupR32hf3g0yxZIuLLH4O2KRo-HyZ3jav7M51Uvv5R_Zx6TE_njsxpxqXW0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور زبان‌های خارجی
🔹
۱. ثنا اکرمی
🔹
۲. سارا اعلایی
🔹
۳. ساینا دهاقان دهنوی @Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/465991" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465990">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698d1a0e28.mp4?token=GpG1W0M5nJ4nUM15WXh4o9GLfODhkUE28y1PQuP7xjjowj5cM0VWDJVyDpw7icRhqwK_E6fuBB0mKq7C3FlEmqGAoz4c5F5E52ZCQCSMAtFpHnEJDjya_XlUyNxEuy0TABWLJLvdSzPTlIWDfKkXrkUX837T9uvSvK2BlsEJlDMKP9vA8HSSYOnRZFqdD5AwF6kNfcLu3bqyyTid2hobUZ2zBQDAoWeC7bHgYcpwLm5jZWp1t5i8S6xRQuPKz8cHb4VVzQ6_c0XS7UPGX9vW0MWa7CxOQnM4c4ARfqpA1UpaZ7uOGY-Ec4LhozI7po1l-TeymcVavmBQFTuHysjjiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698d1a0e28.mp4?token=GpG1W0M5nJ4nUM15WXh4o9GLfODhkUE28y1PQuP7xjjowj5cM0VWDJVyDpw7icRhqwK_E6fuBB0mKq7C3FlEmqGAoz4c5F5E52ZCQCSMAtFpHnEJDjya_XlUyNxEuy0TABWLJLvdSzPTlIWDfKkXrkUX837T9uvSvK2BlsEJlDMKP9vA8HSSYOnRZFqdD5AwF6kNfcLu3bqyyTid2hobUZ2zBQDAoWeC7bHgYcpwLm5jZWp1t5i8S6xRQuPKz8cHb4VVzQ6_c0XS7UPGX9vW0MWa7CxOQnM4c4ARfqpA1UpaZ7uOGY-Ec4LhozI7po1l-TeymcVavmBQFTuHysjjiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور علوم ریاضی
🔹
۱. اشکان کریمی
🔹
۲. امیرکیان رئیسی بهان
🔹
۳. امیرحسین جعفری @Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/465990" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465989">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89758407b.mp4?token=Jsm6iIwIIhtaI0nz-lK5Y8b5a0twzQnvtGczGjmp5znq6JT3H6ShTROKkqLD4Hm3bMoQ_Taz9SxVku22oTSVvPMgrNcjlutwm8IsxQvhDFqybLI1tqVwqOpvPSZt7vpIo7mW5iK8lAuoZK2mwPMUAiRaJkktjhEjBklZSbnS9irvw9x0UXnZiTP0JPmv3QAn625WghMm1UA6UuH3VuZFZhOZKcD_CwmluZ4y-zAoPA9W9d76x1_IQ2-dhitIQ6rv0cBFm2_EzlSzYBfSh95HND7_nIdwA-cOX5W12q7KX4V8oR2MBpGYVKkOs-6QhljaK2_E6eMpCHVmr605YvL4Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89758407b.mp4?token=Jsm6iIwIIhtaI0nz-lK5Y8b5a0twzQnvtGczGjmp5znq6JT3H6ShTROKkqLD4Hm3bMoQ_Taz9SxVku22oTSVvPMgrNcjlutwm8IsxQvhDFqybLI1tqVwqOpvPSZt7vpIo7mW5iK8lAuoZK2mwPMUAiRaJkktjhEjBklZSbnS9irvw9x0UXnZiTP0JPmv3QAn625WghMm1UA6UuH3VuZFZhOZKcD_CwmluZ4y-zAoPA9W9d76x1_IQ2-dhitIQ6rv0cBFm2_EzlSzYBfSh95HND7_nIdwA-cOX5W12q7KX4V8oR2MBpGYVKkOs-6QhljaK2_E6eMpCHVmr605YvL4Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور علوم تجربی
🔹
۱. آرش محمدی
🔹
۲. سیدآرمین حسینی
🔹
۳. علی جعفری @Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/465989" target="_blank">📅 10:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465988">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42af7f2d26.mp4?token=f60P6rF9NroSlgbdtV7vdPYjfLMqCwi0dcOLWXlEJZC3DJl5j4gtFfyrV41xvdUAj3wdotJwI_02KCCv47MjtohodSP86OllM68Udo9gca6eMD2brLc-La9rK04m-_-u2dHKFVsJSfUxrLDZAbSdSM14j8hrFGDxKdQg3BYUer6ZEHzapZKpD8eQFQOf4R8nRF86LRII-pk8VoYQK08hh2ZRDpFzGOIx046mYvxSMFnkrYPlLQgv5K3KbBJ5Yay-UCGRWUNKoFcnYYckRvCdRMHv7ZPEnU80cJLlw1MRzz177OPxC7qKoFpO7ef6I0AgEuiXNFLBbDZSleXN8nWxMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42af7f2d26.mp4?token=f60P6rF9NroSlgbdtV7vdPYjfLMqCwi0dcOLWXlEJZC3DJl5j4gtFfyrV41xvdUAj3wdotJwI_02KCCv47MjtohodSP86OllM68Udo9gca6eMD2brLc-La9rK04m-_-u2dHKFVsJSfUxrLDZAbSdSM14j8hrFGDxKdQg3BYUer6ZEHzapZKpD8eQFQOf4R8nRF86LRII-pk8VoYQK08hh2ZRDpFzGOIx046mYvxSMFnkrYPlLQgv5K3KbBJ5Yay-UCGRWUNKoFcnYYckRvCdRMHv7ZPEnU80cJLlw1MRzz177OPxC7qKoFpO7ef6I0AgEuiXNFLBbDZSleXN8nWxMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور علوم انسانی
🔹
۱. پریزاد نیرومند
🔹
۲. یاس هاشمی
🔹
۳. پوریا زارعی محمودآبادی @Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/465988" target="_blank">📅 10:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465987">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d38177d2c.mp4?token=ZDlaKKVwUVe4CNaaAKvc-T7w2WhyaaWGRpncV7LPyZK3iiWUSjf9xOem3hLDmDwaNyLT2Lnl_Al7DuGjxI0c2sbztquokR4bGEzHaRn22ALo9J9gaUQLAYn2_LTfq0-Os6qFVfS_dr5jpX8r-YMHuksYR0AZDL_Jg-hSIrWxUwthCcBAbHhyJo4cwW8xYQkOrSFMEEHuyferM7JZy3Ud88ggOBqWA57l77g7Uce4qOkN05OPnqj9Ytqns1V6-FfjEupCwOuHAKre_BgtrUdf6stMkEKIe2QIMMORp93vKmajg9H-TzXKDy_ZnO22buXjXr7JSGGXagFsi4oJcEZArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d38177d2c.mp4?token=ZDlaKKVwUVe4CNaaAKvc-T7w2WhyaaWGRpncV7LPyZK3iiWUSjf9xOem3hLDmDwaNyLT2Lnl_Al7DuGjxI0c2sbztquokR4bGEzHaRn22ALo9J9gaUQLAYn2_LTfq0-Os6qFVfS_dr5jpX8r-YMHuksYR0AZDL_Jg-hSIrWxUwthCcBAbHhyJo4cwW8xYQkOrSFMEEHuyferM7JZy3Ud88ggOBqWA57l77g7Uce4qOkN05OPnqj9Ytqns1V6-FfjEupCwOuHAKre_BgtrUdf6stMkEKIe2QIMMORp93vKmajg9H-TzXKDy_ZnO22buXjXr7JSGGXagFsi4oJcEZArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان سنجش:  فردا نتایج اولیهٔ کنکور در تارنمای سازمان سنجش قرار می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/465987" target="_blank">📅 10:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465986">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e635afaa1d.mp4?token=Ck1dXX4uR8O20neIE1CV18209g-8dp39wSJO3DQAJXe7YjLoGkA9UC6CvQxCUYFxfVb3bUVfbEsHjrDh4p8I1zjXFFLpFA0cpLtpS2J1Eb0LYl9P2xLKarfzf9MWlP09JNlzltlJwUnx9AMkqlHY-IpjD4MA1oQ4IcAy9bWREym12DfDuwH_dsvqchtarWixAVYm5vElF2fMem0gq-1mM_fIwq6wE-RdJ0zNEWyhA3iDnNa4vy75FRp-cV58X8AtQRdfzff0_JEMLmlFLDKjrkGnpGYbTqvNiRHODzdI59wMFFcVSodmsn0yq48NkPawzYKj2iIj__qrZwvblOfwtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e635afaa1d.mp4?token=Ck1dXX4uR8O20neIE1CV18209g-8dp39wSJO3DQAJXe7YjLoGkA9UC6CvQxCUYFxfVb3bUVfbEsHjrDh4p8I1zjXFFLpFA0cpLtpS2J1Eb0LYl9P2xLKarfzf9MWlP09JNlzltlJwUnx9AMkqlHY-IpjD4MA1oQ4IcAy9bWREym12DfDuwH_dsvqchtarWixAVYm5vElF2fMem0gq-1mM_fIwq6wE-RdJ0zNEWyhA3iDnNa4vy75FRp-cV58X8AtQRdfzff0_JEMLmlFLDKjrkGnpGYbTqvNiRHODzdI59wMFFcVSodmsn0yq48NkPawzYKj2iIj__qrZwvblOfwtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیاره، معاون سازمان سنجش آموزش: تا ۱۰ روز آینده نتایج کنکور سراسری ۱۴۰۵ اعلام می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/465986" target="_blank">📅 10:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465985">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2e23b992.mp4?token=rooyDoG-D_KnWGFMKiB7Ak-9oS54eIhNKMX70VJfOzmg7HaU0fBGEwsU6nrVYjaTPSZX7fgnX21inX8pmRFcEYSZ4i1Y71stvEYx0Eev1R23UehMQM3WvlgBoOmw1MvDfzs6H1MhVGtjfyQbBF_gvFLZA-0vllVZrqGhPVZaUdI89lRjK-C9VMm3yC0N4Ru58YrJXDsqKeI9rNr_SyH5jqt-bSqwcc2B9ynU6LVEv4ftH259Q81CWStvLDxJ9KfM6MnASBtnFttRdvRsAHtXb0E1hdnwMtagzQw02YBz_U_qN6pJEmqIMFzPyE-S7ttMO9DFupXdt-c-tNQQtr5maA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2e23b992.mp4?token=rooyDoG-D_KnWGFMKiB7Ak-9oS54eIhNKMX70VJfOzmg7HaU0fBGEwsU6nrVYjaTPSZX7fgnX21inX8pmRFcEYSZ4i1Y71stvEYx0Eev1R23UehMQM3WvlgBoOmw1MvDfzs6H1MhVGtjfyQbBF_gvFLZA-0vllVZrqGhPVZaUdI89lRjK-C9VMm3yC0N4Ru58YrJXDsqKeI9rNr_SyH5jqt-bSqwcc2B9ynU6LVEv4ftH259Q81CWStvLDxJ9KfM6MnASBtnFttRdvRsAHtXb0E1hdnwMtagzQw02YBz_U_qN6pJEmqIMFzPyE-S7ttMO9DFupXdt-c-tNQQtr5maA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا  یک برد دیگر در تکواندو بانوان
✅
فاطمه احمدی در نخستین مبارزه خود در وزن ۶۷+ کیلوگرم مسابقات تکواندو با نتیجه ۲ بر صفر مقابل لین یی‌چن از چین‌تایپه به پیروزی رسید و راهی مرحله بعد شد.  @Sportfars</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/465985" target="_blank">📅 10:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465982">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHr-Fg74HC_o2nxTu5V4ONz6q1LUk_wo8pImwGffsSQGPNwydtZnZePXhYIYb4_OYLukteF7iiQ4LbFq6okbt8RD_rVYXjyCYSjr6hCgPKYlaiJD7r23g1usYqYkL7-CQtATjtV2KIEnXB8Iz_Pndxp63EyiEgHwcguJ0MtaBlrv6EvBITuKqyHQNIOZzwK7NVdJ8tHCxnjM1_d9jcxTj8yEA-wTMkIJm4iSU8bqBn41l_M7g_xBvGu3g0-CQz21RaQRVEAU-fR5zTF028yg0RsDqAuzM7JfbHI1PPNMd_VXxGbrLCpPt4jVd5JgdyttD02EgVpRLE3WMztTtjIzbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVb_THql9qPsqwMLewur04y5CScgKxGFJLCw6he6kHp7ox1fNhtWfwjYsePH_JWSljVZccNaN9jHZK1gx4QcjMh8H6qzbRYO-MCwMn_dPNDeInCGZfgr5DIuMw-QkdZGhgUZ2zbePCmI2TWX28ELKyistKGXe51EEKb7JIqQ1i2cOj1mhOg1mZ5rx7lOttW08Hs-Wv5cUnVGfd_1mQtXQdq2CkyCJZTx4WHz92OydhDSOcUQKKwXnvmGr_n7c4Ou6BC0ePmDWy1Psn3R1pha01sLUR7HiA03BiZCLNrvpSnqaegL0BKj4s7k-DXa4OF1Nfq_WJfRsQQyDvT567zMNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86287d76d.mp4?token=tOKg63leROKb317dVyRmQJGZpBKc8XOlKbbqEyg6wGlSv6phM8YtfGOIrnpHIm8bplEQNG_ilW25lOS7c6epE1WhxRqrBGKq1r3zaAJSSg9lHvPPXUUkBjxEm-pxc8uVok0o-L5gXKPSdgkkOIWNEpR8e2yYxtkVbVk32Qb01LHh9cF6qzPbKdKTdw0QMjSXU2mciXGTzgYDiCBqjoTb7O3mAHP-zOOmcx0KrBCJEVglqhlgraZS-WsxL-fPKaN7cyuP97v9BZt0olor6VGo3YTbOJK-IDgVUv3Ot5paeULVK23V_9A3Dfufa6Wjfode9AOAc41nBjSSrgNow-aC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86287d76d.mp4?token=tOKg63leROKb317dVyRmQJGZpBKc8XOlKbbqEyg6wGlSv6phM8YtfGOIrnpHIm8bplEQNG_ilW25lOS7c6epE1WhxRqrBGKq1r3zaAJSSg9lHvPPXUUkBjxEm-pxc8uVok0o-L5gXKPSdgkkOIWNEpR8e2yYxtkVbVk32Qb01LHh9cF6qzPbKdKTdw0QMjSXU2mciXGTzgYDiCBqjoTb7O3mAHP-zOOmcx0KrBCJEVglqhlgraZS-WsxL-fPKaN7cyuP97v9BZt0olor6VGo3YTbOJK-IDgVUv3Ot5paeULVK23V_9A3Dfufa6Wjfode9AOAc41nBjSSrgNow-aC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استوری‌های راحله امینیان از وضعیت مدارس لبنان و تنها خواسته مردم لبنان؛ «فقط سلام ما را به مردم ایران برسانید»
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/465982" target="_blank">📅 10:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465981">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViQcU6vgDjrVi0-9HKx9AAAsFdXpUgyiUdTu0-OpkrBChGtBFQuprl3_25lhNL7_FPUnvgb2NipSMZi34YzIfiBtkahAg_Y4Cv_DxQzUIcyKY57MGTUQLPa4Rru3L64nxKNoBy0Ct35YtjZfgKmpMnJmm5VLKQ0rU3MQVqbcLFdWoMiiqahVGGYJ8-2blZGKko3-kLwA2JoX9NRlOjpptc6srPTA8Hw_PZ0ZDxE9TTz9Rr7TStvb2X21XHgNz_R6lfNPy_ONpY_E3p0WVWp0vJla5SVa7Xkz5_a_H9on3NrSM7hBjQ7M6w-a8D0oNEvkH8tZ9nAnOJuIGjsTAq-_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک نفتکش در مسیر غیرقانونی تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد که بامداد امروز سمت چپ یک نفتکش در فاصلهٔ ۴ مایلی شرق عمان هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/465981" target="_blank">📅 10:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465980">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf8d6aa62.mov?token=O3qLhSzuxscTldFPD32g1v1qdU5x_oq1MyX5Y6bFZUFAuHF_XMerjpThkRSkSLp_E_trh9XkbEHPe-RObD-0WVOv4NuLaZZNZPkrRm200qB4RUAl5OGlhTJxjDmMUelj77v2_FnRAx8mm7ayvJnNpyyZ2Uua5qk4uAyAHehYp6hsW-MNZTU3ULmONAKvcqF-txXmHmBNc4vXG1vQeKBbmWCTOB7ToBactT1z1D-rdBq4TgCjQ3V9Yh2KdFVbWRPBy-J1dK-AtPo9oOJKy2PYs7oCuVmeAbGoNi_If9yzO-o8Temi_u4fwddd9i5p55g-rDVQt209yj8slF-kFD9hYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf8d6aa62.mov?token=O3qLhSzuxscTldFPD32g1v1qdU5x_oq1MyX5Y6bFZUFAuHF_XMerjpThkRSkSLp_E_trh9XkbEHPe-RObD-0WVOv4NuLaZZNZPkrRm200qB4RUAl5OGlhTJxjDmMUelj77v2_FnRAx8mm7ayvJnNpyyZ2Uua5qk4uAyAHehYp6hsW-MNZTU3ULmONAKvcqF-txXmHmBNc4vXG1vQeKBbmWCTOB7ToBactT1z1D-rdBq4TgCjQ3V9Yh2KdFVbWRPBy-J1dK-AtPo9oOJKy2PYs7oCuVmeAbGoNi_If9yzO-o8Temi_u4fwddd9i5p55g-rDVQt209yj8slF-kFD9hYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رده‌بندی تمام ایرانی بدون سرمربی!
🔹
با توجه به اینکه دیدار رده‌بندی پدل بازی‌های آسیایی بین دو تیم ایران در حال برگزاری است، سرمربی تیم ملی در جایگاه ویژه، تماشاگر این مسابقه شد و هدایت هیچ‌کدام از تیم‌ها را بر عهده نگرفت. @Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/465980" target="_blank">📅 10:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465979">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b3fc0d84.mp4?token=G7Z_li4iVIMQoRnlqKpQyj6AgA5idh50fAY5kGGRN6yLyQE0qdKrZ9f6bgR25Yb6nl5fRnVGByYi9cKzsyCrIXQN56iX75-ZCidq5qxyocbQJtD0On0IfJeMkrt7v30rlssLm0BeWLomF_B9aAAkAjV15JGWGSE92ftlGCuGtca3nTiXUg9kBbCzbolya0YBHMVTq-sG0aFYbk3bahG5LAjZaizck34pt6Dquvf677kBu3q79C5NaXBg74B36834CN_S2gMAmYIta0Ip070405uc-oQa3w-xyseeZ7EQqDjkrPGx0Zp2L5pu6eyDkAP0sqKM3i-0NxedgV7Zsnx_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b3fc0d84.mp4?token=G7Z_li4iVIMQoRnlqKpQyj6AgA5idh50fAY5kGGRN6yLyQE0qdKrZ9f6bgR25Yb6nl5fRnVGByYi9cKzsyCrIXQN56iX75-ZCidq5qxyocbQJtD0On0IfJeMkrt7v30rlssLm0BeWLomF_B9aAAkAjV15JGWGSE92ftlGCuGtca3nTiXUg9kBbCzbolya0YBHMVTq-sG0aFYbk3bahG5LAjZaizck34pt6Dquvf677kBu3q79C5NaXBg74B36834CN_S2gMAmYIta0Ip070405uc-oQa3w-xyseeZ7EQqDjkrPGx0Zp2L5pu6eyDkAP0sqKM3i-0NxedgV7Zsnx_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در لبنان: مجاهدان لبنانی پس از حمله اسرائیل به ایران و شهادت رهبر ما وارد جنگ شدند و با چند هزار شهید، نقش بازدارنده‌ای در برابر دشمن ایفا کردند
🔸
برای احترام به این فداکاری‌ها کافی است فقط ایرانی باشید.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/465979" target="_blank">📅 10:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465978">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b040582fd6.mp4?token=dihD_ngtigztTPcM86-7Lwz3L6aVxiTsfDXbaZkJezGUOlMhsncjPmAPj3gQ0utNUtDPwy5V7YFQy9sYIKi5OcFRfzB-H9S6XzRjjAb6S6uKdbtw-Fmw2hFwjkXsh9AMg5zTb2FpMBMJuwA2xtMJeDkSPid4TpB8EHGYQDYuxpV2ijc1YroZHrvehaTBbcAs4IE7wZnPOtddc5kA_JqcAyVB-10a5MkRfq2FL8fPyM4XBVmdB7CgfZ2pUSD5nAfxXuOd0DoDvaQM5wGmEP3JG1d5THMDRk-Jydi1fSn-eBWP2LAl9qfz9LA48ztA-AtglOfRKp6BL2jyOcs4AlHULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b040582fd6.mp4?token=dihD_ngtigztTPcM86-7Lwz3L6aVxiTsfDXbaZkJezGUOlMhsncjPmAPj3gQ0utNUtDPwy5V7YFQy9sYIKi5OcFRfzB-H9S6XzRjjAb6S6uKdbtw-Fmw2hFwjkXsh9AMg5zTb2FpMBMJuwA2xtMJeDkSPid4TpB8EHGYQDYuxpV2ijc1YroZHrvehaTBbcAs4IE7wZnPOtddc5kA_JqcAyVB-10a5MkRfq2FL8fPyM4XBVmdB7CgfZ2pUSD5nAfxXuOd0DoDvaQM5wGmEP3JG1d5THMDRk-Jydi1fSn-eBWP2LAl9qfz9LA48ztA-AtglOfRKp6BL2jyOcs4AlHULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منظور، رئیس سابق سازمان برنامه‌وبودجه: ۱۰ میلیون خودروی فرسوده، بنزین را می‌بلعند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/465978" target="_blank">📅 09:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465977">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769e47fdeb.mp4?token=SLlyMFk7FDOdScZvYNIzmd6jTsXbAof-vuOZTpuGuVxYFFwNTzdjFXh3aY2i6nHkEu1MGhJQWzOmGHrSZAwyQ_Tu4-xQqiB_1-e5z6PwspTkath8QN2PGNbC1vrNVxYCvYJkKUWqjbz7e1XfEC0zQuAloW3dwS_jYOHcFj0HhVtt9KSqOpLJf0tnriOQZisyqWiTEhLCq5NlafCwjTsiLLzLFZg--0RZDPll21bKIac751PnNcOmyvCSu8efZo8ThR0JJOm4s-P9pWcIF9BCi8o8w4CmGEYqzOc3PIN3XrvtLuAU27iafb77TD4Y37FrAqU2iaRgwhUIhuogXAinJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769e47fdeb.mp4?token=SLlyMFk7FDOdScZvYNIzmd6jTsXbAof-vuOZTpuGuVxYFFwNTzdjFXh3aY2i6nHkEu1MGhJQWzOmGHrSZAwyQ_Tu4-xQqiB_1-e5z6PwspTkath8QN2PGNbC1vrNVxYCvYJkKUWqjbz7e1XfEC0zQuAloW3dwS_jYOHcFj0HhVtt9KSqOpLJf0tnriOQZisyqWiTEhLCq5NlafCwjTsiLLzLFZg--0RZDPll21bKIac751PnNcOmyvCSu8efZo8ThR0JJOm4s-P9pWcIF9BCi8o8w4CmGEYqzOc3PIN3XrvtLuAU27iafb77TD4Y37FrAqU2iaRgwhUIhuogXAinJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در لبنان: مقابل رزمندگان، مجروحان و خانواده‌های شهدای لبنان جز شرمندگی احساس دیگری نداشتم؛ این مجاهدان دارند جهاد می‌کنند
🔹
خانواده‌هایی را دیدیم که چند شهید داده‌اند، خانه‌شان را از دست داده‌اند و در اتاق‌های کوچک زندگی می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/465977" target="_blank">📅 09:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465976">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یکی از متهمان پروندۀ دوومیدانی در کره‌جنوبی به ایران برمی‌گردد
🔹
یکی از اعضای تیم ملی دوومیدانی ایران که در جریان رقابت‌های قهرمانی آسیا در کره جنوبی با اتهام آزار جنسی مواجه شده بود، پس از پایان مراحل اولیه تحقیقاتی و رفع ممنوع‌الخروجی، به‌زودی به ایران بازمی‌گردد.…</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/465976" target="_blank">📅 09:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465973">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a14e06e9c.mp4?token=RnCZIGiYyOkKviBuVN1j7ttqVIoxuaYbb6hzphjPEefi3VOJ9Bc6IgnVgL5Jd6sNOB1sX0tHypq1gcl7bdIgBCoGO19ZyIayAP7b9HVh_OdgcIAQWNbcLEhFFEJRhHmA5iQ-hjCMQn_oQSF7FMN6TYr5KE4ayQWLdREUBzuF2qzSon81MNQQg2yN0dfDQzK0aQ2qimzv8gCUDNks5-TfMfPfWB689XAxx1Pxu-DyViFItRoMcNdJq7y8FcGWA5zup5iiER1lW0uuF6ZyM110plmb__BJRCDZuJV6jNE8Frx8cGZ8S0dh6L01BZAaHL7YaSTG-VVzEdPL3Mun0XGs9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a14e06e9c.mp4?token=RnCZIGiYyOkKviBuVN1j7ttqVIoxuaYbb6hzphjPEefi3VOJ9Bc6IgnVgL5Jd6sNOB1sX0tHypq1gcl7bdIgBCoGO19ZyIayAP7b9HVh_OdgcIAQWNbcLEhFFEJRhHmA5iQ-hjCMQn_oQSF7FMN6TYr5KE4ayQWLdREUBzuF2qzSon81MNQQg2yN0dfDQzK0aQ2qimzv8gCUDNks5-TfMfPfWB689XAxx1Pxu-DyViFItRoMcNdJq7y8FcGWA5zup5iiER1lW0uuF6ZyM110plmb__BJRCDZuJV6jNE8Frx8cGZ8S0dh6L01BZAaHL7YaSTG-VVzEdPL3Mun0XGs9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقف پروازها در فرودگاه ریاض به‌دلیل انفجار
🔹
همزمان با گزارش‌ها از حملات موشکی و انفجار در عربستان، فعالیت پروازی فرودگاه بین‌المللی ملک خالد ریاض با اختلال مواجه شده و پروازها با تأخیر یا لغو مواجه شده‌اند.
🔹
برخی منابع عربی هم از حملات موشکی یمن به مخازن آرامکو در ریاض خبر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/465973" target="_blank">📅 09:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/simzBoesBqiMimDGGA0PWPCf8HEEcqrYpysoJJPttkSkYKIPa4f_8Ufajfi7taLUHug5baqe_f4KmpeGsCf4eKT3_7cuiKniy4KOYz-A8i8RpEGMN0jQik-Y2hKGXoO9Sbo4a6w0gG96HMYaMcCcjsyCWi7JXbu-As3WcjGwhHTKKuX4Vy8yxUgxSfvOjAnd8xvpOjv1Rl-riBVbvf6Lx51Oo4qXh6VZBuv6mlwSTKA1d4rI5u-aLAohmTlvgpb-Zvcb5soJs-oA-NTpWiT-9Ypgp3F5owHnITO9wmTFEvKDpJHeCMw4Y0BkdmwOn58AFNvwKc3zWt2oGgHmgu7_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین نقشهٔ نفتکش‌های تنبیه‌شده توسط ایران در تنگهٔ هرمز
🔹
جدیدترین نقشهٔ مؤسسهٔ واشنگتن که نفتکش‌های هدف‌قرارگرفته توسط ایران در یک‌ماه گذشته را نشان می‌دهد، حداقل اصابت به ۲۰ نفتکش در مسیر غیرقانونی تنگهٔ هرمز را ثبت کرده است.
🔸
این در حالی است که ترامپ همچنان مدام مدعی «نابودکردن نیروی دریایی ایران» می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/465972" target="_blank">📅 09:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465971">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کشف سلاح کمری و فشنگ از دکهٔ فروش روزنامه در تهران
🔹
پلیس تهران از کشف یک سلاح کمری، ۲ خشاب و ۱۶ تیر جنگی در بازرسی از یک دکهٔ روزنامه‌فروشی در خیابان مولوی خبر داد و اعلام کرد که «متصدی این واحد صنفی به دلیل نگهداری غیرمجاز سلاح تحت پیگرد قضایی قرار گرفته است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/465971" target="_blank">📅 09:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465970">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d58c47b27.mp4?token=bbmei9iqL357tpC_DNKUPljzIb4udfU7MIuY_6PLCsWTpzxqAQn1j6S15CLryS8oHSgmUB_7M5pgWpw2C57onFk1IeqlHRcTvyRF_7eckXouj1x_yUK3xknUMUkQSdlZAOqEN1KJSN0mVaCXbIMadAakEcdHe1ktSxgxG3RjxNa7QXoTrV4ZMNcmHhq2U2fZd1eANHWKl22JNJ2TmyMWa1_IUt3oqsyCdi77Nw5qoJzMnC_Gk2zcGIkUxr1v8FTsT8vMA4ki7NtshG-YR6dsPQQJLzaVTuIBiPzLXbOOnpxP374EgFNd8RsPXXp209YlL4OYE6wPb3941_dQEpWsbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d58c47b27.mp4?token=bbmei9iqL357tpC_DNKUPljzIb4udfU7MIuY_6PLCsWTpzxqAQn1j6S15CLryS8oHSgmUB_7M5pgWpw2C57onFk1IeqlHRcTvyRF_7eckXouj1x_yUK3xknUMUkQSdlZAOqEN1KJSN0mVaCXbIMadAakEcdHe1ktSxgxG3RjxNa7QXoTrV4ZMNcmHhq2U2fZd1eANHWKl22JNJ2TmyMWa1_IUt3oqsyCdi77Nw5qoJzMnC_Gk2zcGIkUxr1v8FTsT8vMA4ki7NtshG-YR6dsPQQJLzaVTuIBiPzLXbOOnpxP374EgFNd8RsPXXp209YlL4OYE6wPb3941_dQEpWsbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید حدادیان: بیش از ۷ ماه است که برخی مردم در جنوب لبنان آواره‌اند و تقریباً بدون امکانات در یک مدرسه زندگی می‌کنند، اما با صلابت ایستاده‌اند
🔹
با همه این سختی‌ها، آن‌ها حال رهبر معظم انقلاب و مردم ایران را از ما می‌پرسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/465970" target="_blank">📅 09:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465969">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0b96e3f8.mp4?token=aaepDG087H6BsnY79X-APl4sKLaBZma03arPRQeIunuXcqrL6KpptoTuTe2iroosyC7_5MegCJmbLv5rEbYsfRyE1Xd85IFIWDGyT5I0uoczzEapiwCTAp1APamjj6zIh6ofSj1WVoU5VS0dJ4BhkMKOtGFAOoaydTl__xzTNNX3TQELkEmbokB1oXTCxw2POn0XmN53dozzCVTzI7mEVHKajOhmKYQ6aLwD8k1tk8OINv5sFRHHSf8JrH5FGp0U-iTjqY-f2p6_N7hS4IB67bKGWav8Cs1FqyLM3uhznB1GaObA2K0cLP4SHp6LyvOwyye2v5H1BOxCSYHq75B8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0b96e3f8.mp4?token=aaepDG087H6BsnY79X-APl4sKLaBZma03arPRQeIunuXcqrL6KpptoTuTe2iroosyC7_5MegCJmbLv5rEbYsfRyE1Xd85IFIWDGyT5I0uoczzEapiwCTAp1APamjj6zIh6ofSj1WVoU5VS0dJ4BhkMKOtGFAOoaydTl__xzTNNX3TQELkEmbokB1oXTCxw2POn0XmN53dozzCVTzI7mEVHKajOhmKYQ6aLwD8k1tk8OINv5sFRHHSf8JrH5FGp0U-iTjqY-f2p6_N7hS4IB67bKGWav8Cs1FqyLM3uhznB1GaObA2K0cLP4SHp6LyvOwyye2v5H1BOxCSYHq75B8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رده‌بندی تمام ایرانی بدون سرمربی!
🔹
با توجه به اینکه دیدار رده‌بندی پدل بازی‌های آسیایی بین دو تیم ایران در حال برگزاری است، سرمربی تیم ملی در جایگاه ویژه، تماشاگر این مسابقه شد و هدایت هیچ‌کدام از تیم‌ها را بر عهده نگرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/465969" target="_blank">📅 08:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465968">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سیاوش جمشیدی، از اوباش مسلح شهرکرد اعدام شد
🔹
کلاهبرداری، تهدید، سرقت، حمل و نگهداری سلاح جنگی، مشارکت در آدم‌ربایی، قدرت‌نمایی، واردکردن صدمة بدنی عمدی، تهدید با سلاح گرم و شلیک با سلاح کمری مقابل حوزة علمیه شهرکرد، از جمله سوابق متعدد سیاوش جمشیدی بود.
🔹
جمشیدی همچنین در جریان کودتای دی پارسال فعال بود و با سلاح جنگی به‌سمت مأموران پلیس شلیک کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465968" target="_blank">📅 08:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465967">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af39fa7c6.mp4?token=BLWAuT-D9dGDwlc_vIePKpcx3Zd9uq0F45XZVVaVpJG2qH-1jtSpLDm4OzbkXFR_MFrWBYti_SuEIyDKQIus8q6ECKLtK_PFmfJM_Ao__f_m8oOzBkQcpUyHIQALMdLxbTArOnNzMDdLlZwsqbkT0brjrNloFyqgsYgQtGDkjxudassPK2zZ_rI20cnOTi0Vyi-51p06Jf-7uqNPfKKpqF3PVucHY6OxqqP_LlMZvIwIkUpPIPpaq1AQKjDMU2FkLJFHd1olsr0EOfqZCDOPohnVsPGdVDDd31UmrGsPR6ZKegSwsbHpjRB5sxI-8MGwl8wRdz1yuiyMihdsctax10bwlym6bSQn3p1g7VEtd2evahx6CVnKL-zlMPJWJ7J9-btVDLcEMt5rHj-pLp5qC9xHAqWv-3yBTH_yxYi7MApqRhBs3hAgKNLs5zs3s23SbsB7zun2N_iJp43FuaM8zO6Jg2xqDCk1Xs0lPy_443w1yaFAIQt00JetIdk7PJpqtpy0_QaPCxmCk6VUqTr4XcSKOmP7AiCYpv8_b-VdfAh0HGtPp5rNfzjBbZi2JQFhlHOnjGLQkADFScaOXPwe7DgQrgcwtTEUHEi5TNfqhfOgMKAgBQzvVYmqknJaz8S-cFm_uoj9Isao0Jphi7m-lZOvGo17k6LokGRc2ksewPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af39fa7c6.mp4?token=BLWAuT-D9dGDwlc_vIePKpcx3Zd9uq0F45XZVVaVpJG2qH-1jtSpLDm4OzbkXFR_MFrWBYti_SuEIyDKQIus8q6ECKLtK_PFmfJM_Ao__f_m8oOzBkQcpUyHIQALMdLxbTArOnNzMDdLlZwsqbkT0brjrNloFyqgsYgQtGDkjxudassPK2zZ_rI20cnOTi0Vyi-51p06Jf-7uqNPfKKpqF3PVucHY6OxqqP_LlMZvIwIkUpPIPpaq1AQKjDMU2FkLJFHd1olsr0EOfqZCDOPohnVsPGdVDDd31UmrGsPR6ZKegSwsbHpjRB5sxI-8MGwl8wRdz1yuiyMihdsctax10bwlym6bSQn3p1g7VEtd2evahx6CVnKL-zlMPJWJ7J9-btVDLcEMt5rHj-pLp5qC9xHAqWv-3yBTH_yxYi7MApqRhBs3hAgKNLs5zs3s23SbsB7zun2N_iJp43FuaM8zO6Jg2xqDCk1Xs0lPy_443w1yaFAIQt00JetIdk7PJpqtpy0_QaPCxmCk6VUqTr4XcSKOmP7AiCYpv8_b-VdfAh0HGtPp5rNfzjBbZi2JQFhlHOnjGLQkADFScaOXPwe7DgQrgcwtTEUHEi5TNfqhfOgMKAgBQzvVYmqknJaz8S-cFm_uoj9Isao0Jphi7m-lZOvGo17k6LokGRc2ksewPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار بلالی: می‌توانیم اهداف متحرک را با موشک بالستیک دوربرد بزنیم
🔹
مشاور فرمانده نیروی هوافضای سپاه: یکی از چالش‌های ما، اصابت موشک بالستیک دوربرد به هدف متحرک بود که در چند روز گذشته محقق شد؛ موفقیت‌های بیشتری نیز در راه است.
🔹
در هر عملیات، با استفاده…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465967" target="_blank">📅 08:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465966">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7fdb6739.mp4?token=mxz6rWvxPD-yvPacUMJL6IuH72e8AJirX09yg6ARjbHweFkj_zzbc1ZcbLLw2vZb8VGjkBuyV9QYHj_EsUXVFoHTBf9C3w9mzMhbGFWKbV8bzHuVZTpCNUHQDRjZS1KMxA0zqbZyuxlarRQa88zTrlJuyKZCd-OeKZdktE_wniSKvsqbiIBlkRHWdRYAK6w4E_fGEYrmyOjPTIyxJHHuaI0MVHVCI6bOAkOfijIEp0b9BHo-0kI9Z87jJGAAxrDYZEOgntGCmdmmirOfPh0lsTJ2n8ac21cYJP-VPIl5lgLzbHGe1rYL7PZgD-rfq6s3oaGu3TMa_68stAG9KFvbPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7fdb6739.mp4?token=mxz6rWvxPD-yvPacUMJL6IuH72e8AJirX09yg6ARjbHweFkj_zzbc1ZcbLLw2vZb8VGjkBuyV9QYHj_EsUXVFoHTBf9C3w9mzMhbGFWKbV8bzHuVZTpCNUHQDRjZS1KMxA0zqbZyuxlarRQa88zTrlJuyKZCd-OeKZdktE_wniSKvsqbiIBlkRHWdRYAK6w4E_fGEYrmyOjPTIyxJHHuaI0MVHVCI6bOAkOfijIEp0b9BHo-0kI9Z87jJGAAxrDYZEOgntGCmdmmirOfPh0lsTJ2n8ac21cYJP-VPIl5lgLzbHGe1rYL7PZgD-rfq6s3oaGu3TMa_68stAG9KFvbPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید حدادیان: انگشترهای اهدایی رهبر معظم انقلاب برای خانواده‌های شهدای لبنان مثل «خاتم سلیمان» ارزشمند بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/465966" target="_blank">📅 08:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106db1b8b3.mp4?token=JdHUib_hciwop9bVgDLLGQYDsHxQDPNB49QkEupXOCJh7Lbm7eQk-pdo5_c3_cIS-AKTPl5GeILyXETJJ0MT-3AsXJbqmxHbU4i18sjAelzPyDzX63q4afCcqTuczqKoCYPwx5N-Uipmkfeu0LG6zoN7aH1kY0Fh-xZts5opDtur201cX2qNpJNayItVtsRG0aXsE-JJCkuP7QlBqcPHL2Wh9ATORlo023kY79ZpRdWDkYhlLho7qHKem6WRWfK0V7yOuBlBha7zfDIYOPRQxVTM3MdjaaykSbULPpA-Seu7fft8ngCF3p9XpRY87uz5TDzSCziZCG8XmM_G00tNjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106db1b8b3.mp4?token=JdHUib_hciwop9bVgDLLGQYDsHxQDPNB49QkEupXOCJh7Lbm7eQk-pdo5_c3_cIS-AKTPl5GeILyXETJJ0MT-3AsXJbqmxHbU4i18sjAelzPyDzX63q4afCcqTuczqKoCYPwx5N-Uipmkfeu0LG6zoN7aH1kY0Fh-xZts5opDtur201cX2qNpJNayItVtsRG0aXsE-JJCkuP7QlBqcPHL2Wh9ATORlo023kY79ZpRdWDkYhlLho7qHKem6WRWfK0V7yOuBlBha7zfDIYOPRQxVTM3MdjaaykSbULPpA-Seu7fft8ngCF3p9XpRY87uz5TDzSCziZCG8XmM_G00tNjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مالیدن چشم‌ها می‌تواند منجر به پیوند قرنیه شود!
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465958" target="_blank">📅 08:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نامهٔ ۶۵۳ استاد بانو به وزیر علوم: چارچوب‌های روشن پوشش در محیط‌های علمی را تدوین و ابلاغ کنید
🔹
زیست عفیفانه در دانشگاه، نه یک انتخاب، که یک ضرورت است. ‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌
🔹
هر آنچه به ارتقای تمرکز علمی، حفظ وقار محیط آموزشی و تقویت امنیت روانی یاری رساند، از لوازم بنیادین حکمرانی علمی و فرهنگی است
🔹
غلبه ظواهر و حواشی بر فعالیت‌های علمی و پژوهشی باید متوقف شود.
🔹
حمایت از مدیران دانشگاهی در صیانت از حرمت محیط‌های آموزشی و پژوهشی باید مورد توجه قرار گیرد.
🔹
تدوین و ابلاغ چارچوب‌های روشن، متناسب و متین درباره الزامات پوشش و رفتار در محیط‌های علمی ضروری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/465957" target="_blank">📅 07:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌ آذرپیرا به هم به نیمه‌نهایی رسید
🔹
در وزن ۹۷ کیلوگرم کشتی آزاد، امیرعلی آذرپیرا در دور دوم با نتیجهٔ ۱۰ بر صفر هملیف از ترکمنستان را شکست داد و به نیمه نهایی رسید.
🔹
آذرپیرا در این مرحله با آرش یوشیدا دارندهٔ مدال برنز جهان مبارزه خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/465956" target="_blank">📅 07:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امامی به فینال رسید
🔹
یونس امامی در مرحلهٔ نیمه‌نهایی وزن ۷۴ کیلوگرم کشتی آزاد، ۳ بر ۲ حریف قزاقستانی را برد و به فینال رسید
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/465955" target="_blank">📅 07:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شنا و صیادی در دریای مازندران ممنوع شد
🔹
هواشناسی مازندران: به‌دلیل تغییرات جوی شدید، فعالیت‌های دریایی از اوایل وقت شنبه ۱۱ مهرماه تا عصر دوشنبه ۱۳ مهر ممنوع است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/465954" target="_blank">📅 07:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2538348579.mp4?token=GUHNStEck_hfEaNLCWPkEkOOOjeitRlIgyqbPMKWLEgwkvd4rTAlZMwKSuusFSKKasAvKFyiNPcuP1hcdbMBfEpmBNExy4lJQUb3rBEVQPoarw__SqvKabogWyx_Uf8xFLQojJsYRnyD6FVAsurL8G7luIEkvIn-L9Yw4z8ZW02A_se2jtzeDmfNbf24FtXg-nI2Isa47ahYIyaS6wVLnUQQgKmSUCjA3J5AZpaRtiliYYKVVgJfOYuG3Wrs8kO8XcGYMDfxCDx0wbw-wBQleoQTvaZ2hbO2D7Jfni2o8Wy501p9W_kqP3eR1Tt0EYONRnz8jtuJQvbplzF64IdvaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2538348579.mp4?token=GUHNStEck_hfEaNLCWPkEkOOOjeitRlIgyqbPMKWLEgwkvd4rTAlZMwKSuusFSKKasAvKFyiNPcuP1hcdbMBfEpmBNExy4lJQUb3rBEVQPoarw__SqvKabogWyx_Uf8xFLQojJsYRnyD6FVAsurL8G7luIEkvIn-L9Yw4z8ZW02A_se2jtzeDmfNbf24FtXg-nI2Isa47ahYIyaS6wVLnUQQgKmSUCjA3J5AZpaRtiliYYKVVgJfOYuG3Wrs8kO8XcGYMDfxCDx0wbw-wBQleoQTvaZ2hbO2D7Jfni2o8Wy501p9W_kqP3eR1Tt0EYONRnz8jtuJQvbplzF64IdvaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید حدادیان: در ۲ جنگ اخیر تعداد شهدای حزب‌الله لبنان ۲ برابر شهدای ایران بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/465953" target="_blank">📅 07:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRTpSd4177KZuQntE-nYv1v3Kh3Q4lt7XQ1b89gW8rHakn4nwJwnXNUGOZe-93ZKyAKvu49dAGD8l27WCdzeYXyShs3hl8s8_HLUP3i3lDTMlqRqzs0juap4H5DJCLyXUgT6aCwLOKTpk0b3Em2CFfsF2KOTx6zfMI8BGuixuF01d-9deDpHf6XdtecmB8r7SMO7ViKk9ip04cH00Le3-ScTzOJcy36YUwjoqTQoxPQ564RR_nOaK9TTaQqh1zWBJRhHR9bZFfekd_IeHey-ThYemw-5ErSi2YrDjykZKBcxqTr9qM7IzokfdbwikOYjwfQk23fMmgaPN4D0g8ohCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ نفتکش در ۵ روز در هرمز به آتش کشیده شدند
🔸
درحالی‌که تقریبا هر روز ترامپ می‌گوید که تنگه هرمز باز است و آن را کنترل می‌کنیم، گزارش‌ها نشان می‌دهد که نیروی دریایی سپاه هر روز تقریبا بیش از یک نفتکش را هدف گرفته است.
🔹
اکانت رهیابی‌های دریایی منچ‌اوسینت بر اساس آمار نیروی دریایی انگلیس می‌گوید ۲ نفتکش کویتی و ۳ نفتکش اماراتی در ۴ روز مورد هدف واقع شده‌اند. حالا با دو نفتکش هدف گرفته شده در روز جمعه، ایران ۷ نفتکش را در ۵ روز هدف قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465952" target="_blank">📅 07:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آذرپیرا به حریفش رحم نکرد
🔹
امیرعلی آذرپیرا در وزن ۹۷ کیلوگرم کشتی آزاد با نتیجهٔ ۱۰ بر صفر مقابل محمد گلزار از پاکستان به پیروزی رسید. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465951" target="_blank">📅 07:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465950">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مدال برنز آرین سلیمی قطعی شد
🔹
آرین سلیمی در مرحلهٔ یک‌چهارم نهایی وزن ۸۰+ کیلوگرم تکواندو بازی‌ای آسیایی ناگویا، با «هائو تانگ» از چین مبارزه کرد و دو راند پیاپی به برتری دست یافت تا ضمن صعود به نیمه نهایی، مدال برنز خود را قطعی کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/465950" target="_blank">📅 07:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465949">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حذف کشتی‌گیر آزاد با شکست مقابل تاجیکستان
🔹
علی مومنی در وزن ۵۷ کیلوگرم کشتی آزاد بازی‌های آسیایی ناگویا با نتیجهٔ ۴ بر ۱ مقابل آیال بلولیوبسکی از تاجیکستان شکست خورد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/465949" target="_blank">📅 06:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465948">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ناهید کیانی از دور رقابت‌ها کنار رفت
🔹
ناهید کیانی، در وزن ۵۷- کیلوگرم تکواندوی بازی های آسیایی ناگویا در مرحلهٔ یک‌چهارم نهایی مقابل حریفش از چین‌تایپه با نتیجهٔ ۲ بر یک شکست خورد و از راهیابی به مرحلهٔ نیمه‌نهایی بازماند ، و از دور رقابت‌ها کنار رفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465948" target="_blank">📅 06:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465947">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شنا و صیادی در دریای مازندران ممنوع شد
🔹
هواشناسی مازندران: به‌دلیل تغییرات جوی شدید، فعالیت‌های دریایی از اوایل وقت شنبه ۱۱ مهرماه تا عصر دوشنبه ۱۳ مهر ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465947" target="_blank">📅 06:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465946">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آذرپیرا به حریفش رحم نکرد
🔹
امیرعلی آذرپیرا در وزن ۹۷ کیلوگرم کشتی آزاد با نتیجهٔ ۱۰ بر صفر مقابل محمد گلزار از پاکستان به پیروزی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465946" target="_blank">📅 06:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465945">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امامی قهرمان المپیک را برد و صعود کرد
🔹
یونس امامی در وزن ۷۴ کیلوگرم کشتی آزاد با نتیجهٔ ۷ بر ۶ مقابل رازامبک جمالوف قهرمان المپیک پاریس به پیروزی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465945" target="_blank">📅 05:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465944">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b494059ca.mp4?token=Mi7Y00Xtr2t-sJLChiFgLR0LP2XaTuEeUv_bgGL7qACGRYKjydNR7hQuKDYrXbSJZUtyFp_Y4-sTFMXuPzoe9eFaAzHHrQ3Z5Lcluyz2rTXpB1DYtjf8jAgxJts91sj8_OenxTnP2Bg-ivKtfse2GpjVMvHS17oLd-F9P3ysXHZZ3YtRJLAVlpYwsH4C793YiJToI6W3DLHyUXBTK-RAAmfthBEMHjhjANwFDLszHo_36LlyeoOTGFC8VwCx4y7JkXnVEcCfFWbx1XQua7OJJWIvXXUxv48VnRvaUpWb4Kw4w4fS1bFpM2If2RT9mIXUBfHvzuqEvCNaZIJAiPOrpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b494059ca.mp4?token=Mi7Y00Xtr2t-sJLChiFgLR0LP2XaTuEeUv_bgGL7qACGRYKjydNR7hQuKDYrXbSJZUtyFp_Y4-sTFMXuPzoe9eFaAzHHrQ3Z5Lcluyz2rTXpB1DYtjf8jAgxJts91sj8_OenxTnP2Bg-ivKtfse2GpjVMvHS17oLd-F9P3ysXHZZ3YtRJLAVlpYwsH4C793YiJToI6W3DLHyUXBTK-RAAmfthBEMHjhjANwFDLszHo_36LlyeoOTGFC8VwCx4y7JkXnVEcCfFWbx1XQua7OJJWIvXXUxv48VnRvaUpWb4Kw4w4fS1bFpM2If2RT9mIXUBfHvzuqEvCNaZIJAiPOrpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا
یک برد دیگر در تکواندو بانوان
✅
فاطمه احمدی در نخستین مبارزه خود در وزن ۶۷+ کیلوگرم مسابقات تکواندو با نتیجه ۲ بر صفر مقابل لین یی‌چن از چین‌تایپه به پیروزی رسید و راهی مرحله بعد شد.
@Sportfars</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465944" target="_blank">📅 05:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465943">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ: شاید درست بعد از انتخابات جنگ با ایران تمام شود
🔹
رئیس‌جمهور آمریکا که به بیان اظهارات تکراری شهرت دارد، باز هم گفت که جنگ با ایران به‌زودی پایان خواهد یافت.
🔹
او گفت جنگ با ایران به هر نحوی به زودی پایان خواهد یافت شاید درست پس از انتخابات میان‌دوره‌ای.
🔹
ترامپ همچنین یک بار دیگر وعده داد که بعد از اتمام جنگ، قیمت نفت پایین خواهد آمد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465943" target="_blank">📅 03:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMSiKpJBiVxR2aEf4xHq8CUh_BBK3u609rJe8AR3zb84XRVRdpQivKi4vFQZDkUAH-7Nl-V3g_osgiSAFutj0WTYI_3zkHRgloAYXNpmuIBpmeV_yMpPBRRhYQYbOiVCT3RYwwtaLVT3sr6jYLCQrTkb8MJ06rWR4Gd4fk3V-e5XP7Qd-HSomB6r6j_LHPlO96Qf70kXZS7q-U3G0_mFKbZ4jFhGBL-nXdbUo3I49KaDv6Ct8Dufb-SWQ9NA5YndZ923PMnZoZNF_rOR_Y5t1c_Ql4qourALK5CtTe6SDramDuFolhCzbZ-JnlncO3x5pcxt66cYBw6RC5a-numCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNLJQhsanXWvFVrMv3AWWRbOpkLHyooEUyIWBSA-N9fEvtOkRPIi_anGniDK6bWr64EZYqKN-lHUjQps-0l9x6Whz8kZPg5308BLXtGRi5AIwo3zriOdBN9kvkfYd1OvMg_I16BXqn7vYl4dqU73UI3c08-Wm6fOiKU1gMUNYue3LYZ8oNzjrClBnuwGfuGn7DPoku2ckMrk0FWQPDg4l38nWacAwSc4mkv6axExFmhHVgurqwuYAKy4cssYYHdtlC03vSDX4BsBdHC9mLjV4iuWUN6NQOxlbZ_8VDRu4z32Z7gOEo3mdNE1xqxf_5Dbs4Lm3FYii4KQR-rkJOuuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLG3WC75OcuQ-Z4xt4TfGy3Z2sFDRXLNeMmGpdhTrDxp87RB2BwfcCjfTQ1BFEsuHEIbZN4B0DVq2fobnXLJ5PSZYSPikhdkTGrvr4gKaXUUij6kmM5cXiHhbbOuf-6ZKAOJgK-rs8D_SQLuU81-QREStu9Cx0OeCwMwWtUqmigXk6MrI-_FSn2rcp1gqHzpFAXjnRxjesIVVJq66tpqkPf_m8-Nxx_iEKVJxPfqsSnZjKxxoBTjrs8jeNIn9hmmgCbDRdys7C3p35p0IGmgJJJo7DfFVYfaA49djyZJ52LHwnxpXGNnesknfcz5SuHhxgMEysa6tKV3j6KH5kZXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mP1_3I3M8I66p71GfO3mJuATlsq9-ZMPXfniMh3n2ftFS3kGATHqhUBCmIpT5HJYjqyEi6eCbkW_h05VNMlW_C0ald0B6aLnT12fWHnaFphaxPJYfWvB_hf6dM4WUuGkcc020nYEHqhCKbOq4YVknICjrLzQxBr4NQZdt455MqQu14rqzXRrcr2OHT937bHU3A_TASnuZ7filmv_B_sva8DaiAJNT7pZnlVejm0eaVY5_Oe4Ivo-_EvjkB4AxyUgtqrukpyaGwhOHvyz7dSp1w1aahObc8zEQgb0pIx2nIQofIAHjk-8rVsrvuEL6KZnHJXVneNISg__DkfIUlEkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPwzSucqmSgKdJZz4Ut7nS10GpPlQm8TFfAY7PGjP-AXu1hudPYtq0cpZ5jhnlM1kg_6ffAsxgZEfwC75hjZC8Qg5jUTmFZZpPtd0dRgK93qBTlNlHyx2Am7D11cd1QU0xNgQddTCBOL1MdMRylFKKqT2rjIMLlfEQ0HmjekAy-VAyMj_Gg8FppW4BSHCLI8nZOBHBDd8R6v2fMLT-pJNp-iWCQxkRNShv4pSRdkgD1hGKrpnqhiVYC0AoqYF23DkvLNGG7WmLC-Gnrpi2ZXp1YCgrnL0Vjd06aFvF1jbqjeGVLN94-tM3gqOnX1mITUB00PaDN3pB8y4NEjp166NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qg9t2cuqi-D0HImjTD0OrzGTJZbOdfzyzJSg3flm8Q6x6GyCW8hjZINr0Xrd5copuSr_Mmz6hpg1Ruwrtx_Wpe1PQPuFOufpg-P7xoufIaDtCMQmJ8UM5MY-P7_HblivitVlxL3VC7QF4hVr9N7mWIeb-ZVmCM4JFPOEWybuxr1meswRufkZ1ZN0OJc4PyYveCvdA8YOJ8wuIa8c0ZQAYRkfeu0oTDxGNMrJ1thAXHPsTlfaboAxvupCckctxgHY3qL7l6O9aEOjvC1vL8eXZ6dI6d66-0ShMlfALfwmw5yFwNzUhuxdteLOUQ112NkcfZABNNxLHYMYIgBaY0vtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJT5oSGD0Y1hGOtZtmJTUEEFFqEpImaC4jAIa_Uj1XrWc6Ko7h3gArG9zfIAkA_lqD9P94-X-wrNarg-MwunrbUkSt_yizprug0xxl3SVu3R9eMZcoJVIWVoP6OU5kU4IXlpFWNAzO2cYvUedBsukYzIW8l3uQCyoRABeQfL4H8slqo4mVuDQT53kD56rg_f8I4dGS47tE99dD8-Sidl_pDW0FsLsYq-ANLJNUM0p8y6pdllDYg_xbh4_xuGZBDNNNQZYk5Niq49y88s6dZU-CRQDwK1fkMqWd_F06ZS-Upw8yWNuc8KU82Hfv7VwlZ1Gtmia5BxBQpcyQZ1tP0dHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یادوارهٔ شهدای غریب در اسارت خراسان شمالی، در بجنورد برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465936" target="_blank">📅 03:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465935">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">منابع بیمارستانی در غزه:
بر اثر بمباران یک منزل مسکونی در غرب شهر غزه، ۵ تن از جمله یک دختربچه به شهادت رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465935" target="_blank">📅 03:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465934">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3348161d28.mp4?token=rq8K4J7-m1BEJthXjzxloZ8E-7JvRmARkI4sLYmMJFscBL48b3aIyFK3tl3FEyPtvFe6rDCjLNWvRBXSUPeZywDHQS2QGAqchwTM-jfIMEaVEbw0Q9PqaLuEVorHYYN2mcTUkGgY6qFP_HZP5DDK85JWq884cThgptUZc8fiXLXpOvdO5Bf7Jse8Wi9VYFhfjeAh_qrkeAJFAoKhIw_WaBR50cbCwNeCRkbC8sVzgSNpVFh-oBJ_Gqry3r4eAp8KYGt0pejb6ZsAl9x9OtDwIeR03Dy_gOwlyptl39fMameYaY_XgwJt-HqLM8ReTOW1mmgoD_pFDbQZ7Iao3X3uHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3348161d28.mp4?token=rq8K4J7-m1BEJthXjzxloZ8E-7JvRmARkI4sLYmMJFscBL48b3aIyFK3tl3FEyPtvFe6rDCjLNWvRBXSUPeZywDHQS2QGAqchwTM-jfIMEaVEbw0Q9PqaLuEVorHYYN2mcTUkGgY6qFP_HZP5DDK85JWq884cThgptUZc8fiXLXpOvdO5Bf7Jse8Wi9VYFhfjeAh_qrkeAJFAoKhIw_WaBR50cbCwNeCRkbC8sVzgSNpVFh-oBJ_Gqry3r4eAp8KYGt0pejb6ZsAl9x9OtDwIeR03Dy_gOwlyptl39fMameYaY_XgwJt-HqLM8ReTOW1mmgoD_pFDbQZ7Iao3X3uHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه را از خودت بهتر بدان
🎙
استاد کافی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465934" target="_blank">📅 03:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465933">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8KILq1pXdVwgLK5XHcGswZmQvm9Uvbbdo6hQsIaLEoBLcOIhGqOnAfrwyneDKdUI3O4T1IdFylYZWDEdGprUFgW7hmzIdlc7Ml07dIyefsYN5SL-tmYDJaJrXAQzr0pEo8jNhZhdwXvBxbLll_5s-K29_NW-rJks94xqJNEL1RPEsxL_l9hnf7MrAez4KEpu2ifrVYkfW9zchR7IuqBYR9LYgw7EM7dASSUsjlLwPmjYC5W_Cn_Uuoo4WCyD4QWLT4V2bIoYrT2CDGq7jPD7FV6HC-t6mA2s03XxNKUIyNsrhXfD2jSnLF3j0pyN9oaUhw8_DJXN_idz5ifvzFxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک نفتکش در نزدیکی سواحل عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع یک حادثهٔ امنیتی برای یک نفت‌کش در ۴ مایلی شرق سواحل عمان خبر داد.
🔹
گفته می‌شود این نفتکش از سمت چپ بدنه مورد اصابت پرتابهٔ ناشناس قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465933" target="_blank">📅 02:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465932">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIxEo_7e1AoQfDcmhT0LTj-JLM621wpiz2TwC6O5DAc0ruOf77362wzN7hkgZTtSOuHaWqlau6ULxOGlNkZLh3Gnl4J_Xp1skdHbxZSemcG-TAj0kIThdctDd0VYBDvw9wkS9hF-7hGl6rocXongD_dMzyBrvxNxtVFztwVvvu9D1-W9u1N1v4SwVJqgUyV9_SwIYSusTpArNRKprDuYGFKBBA-th_9jr7fDXLnui7xT62M-Yr7bbP7CdYqX5juDj-ihsbNUQmG3JFWbqXy32P8dQ8AFZd20hOdwsc70QylCA4pad_qaTgdKuRoX66eOVTFbbO5jQIi3oR7_RJIYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به خلبان‌های متجاوز به خاک ایران مدال داد
🔹
آمریکا بار دیگر از نظامیانی که در عملیات علیه ایران مشارکت داشته‌اند تقدیر کرد.
🔹
این بار هفت خلبان جنگندهٔ اف-۲۲ رپتور به دلیل نقشی که در عملیات موسوم به «چکش نیمه‌شب» و حمله به تأسیسات هسته‌ای ایران در ژوئن ۲۰۲۵ داشتند، یکی از بالاترین نشان‌های نظامی این کشور را دریافت کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/465932" target="_blank">📅 02:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465931">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کرهٔ‌شمالی پرتابه‌ای به سوی دریا شلیک کرد
🔹
کرهٔ‌شمالی بامداد شنبه در بحبوحهٔ افزایش تنش‌ها میان پیونگ‌یانگ و سئول یک پرتابهٔ نامشخص را به سمت آب‌های سواحل شرقی خود شلیک کرد.
🔹
ستاد مشترک نیروهای مسلح کرهٔ‌جنوبی اعلام کرد این پرتابه از خاک کره شمالی به سمت دریای شرقی شلیک شده است.
🔹
ارتش کرهٔ‌جنوبی هنوز اعلام نکرده است که پرتابهٔ شلیک‌شده یک موشک بالستیک بوده یا نوع دیگری از سلاح. مقام‌های نظامی این کشور هم جزئیات بیشتری دربارهٔ برد، مسیر پرواز و محل فرود احتمالی آن ارائه نکرده‌اند.
🔹
این شلیک در حالی انجام شده است که تنش‌ها میان دو کره افزایش یافته است. ماه گذشته، انفجار مین‌های زمینی در مرز دو کشور به زخمی شدن سه سرباز کرهٔ‌جنوبی منجر شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465931" target="_blank">📅 01:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465930">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کمک‌هزینهٔ ۴ میلیون تومانی برای متولدین ۱۴۰۵ و به‌بعد تهرانی
🔹
زاکانی، شهردار تهران: در راستای طرح حمایت مدیریت شهری از فرزندآوری، برای متولدین ۱۴۰۵ و بعد، کمک هزینهٔ ماهانه حدود ۳.۵ تا چهار میلیون تومانی در نظر گرفته شده است.
🔹
جزئیات این طرح و همچنین آمار دقیق مشمولان، به‌زودی اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465930" target="_blank">📅 01:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465929">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6ce17d3f.mp4?token=ItXsXpkMzjw8obPNfhb3_xlZaYzIRq9xTUUXiUvMlnWOW5bNN1DFE3X0XSiH5Jm286BZ_fdF2ZV3tghJ8swQL6D-4-AhfAAEBGz5MVysK_qwHXCCC_83wIIWUolxGNrKVmdcpC140lCrGeIPTkWZWAy9h1a6Xlk3YAhtl7KB4GhGZrCJx0o-P4O1eJsf5ZXPrUx1M190bbUy6KMelTAT2S5s7yhd8CsBj6q4SCjEte8zwx61d6aUwrMuHOJL4Ec4c2pU7pO2MO2SmPGee1GA6jE3Fw0n78z8HPxb6Nb7CDFbaST7utKETU-0cdfV2NKh26uf2A20Q_QOZTf-82iU5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6ce17d3f.mp4?token=ItXsXpkMzjw8obPNfhb3_xlZaYzIRq9xTUUXiUvMlnWOW5bNN1DFE3X0XSiH5Jm286BZ_fdF2ZV3tghJ8swQL6D-4-AhfAAEBGz5MVysK_qwHXCCC_83wIIWUolxGNrKVmdcpC140lCrGeIPTkWZWAy9h1a6Xlk3YAhtl7KB4GhGZrCJx0o-P4O1eJsf5ZXPrUx1M190bbUy6KMelTAT2S5s7yhd8CsBj6q4SCjEte8zwx61d6aUwrMuHOJL4Ec4c2pU7pO2MO2SmPGee1GA6jE3Fw0n78z8HPxb6Nb7CDFbaST7utKETU-0cdfV2NKh26uf2A20Q_QOZTf-82iU5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در محضر خانواده‌ کم‌سن‌ترین شهید سال‌های اخیر لبنان: پدر شهید نقل می‌کند که بعد از حادثه پیجرها، شهید اصرار داشته یک چشم و کلیه خودش را به رزمندگان مجروح اهدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/465929" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465928">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یمن، اخراج نظامیان آمریکا را به ملت عراق تبریک گفت
🔹
مهدی المشاط، رئیس شورای عالی سیاسی یمن از اخراج نظامیان آمریکایی از عراق تحت عنوان
«دستاورد تاریخی بزرگ و پیروزی ملی»
یاد کرد.
🔹
او این مسئله را به ملت عراق تبریک گفت و تأکید کرد این دستاورد پس از بیش از دو دهه حمله، اشغالگری و سلطه‌طلبی، سرکوب ملت عراق، ایجاد تفرقه اتفاق افتاد.
‌
🔹
وی اخراج نظامیان آمریکایی را حاصل پایداری، مقاومت و فداکاری‌ ملت عراق دانست و گفت این مسئله، تاییدی بر حق این کشور در برخورداری از حاکمیت و استقلال است.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/465928" target="_blank">📅 00:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465927">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465927" target="_blank">📅 00:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465926">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت ۵</div>
</div>
<a href="https://t.me/farsna/465926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۴ – سفرهای گالیور</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465926" target="_blank">📅 00:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465925">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7057a07fa.mp4?token=jb5CEyakwmo95ODW-EE931Lx_tXy-E607B34m2xsKT6dANRgdOzaH6ouMm2kIrEcjLkAC83n-FLK1JsvkhXkUwsG3oFPy99bDbcjbjisjb7kWmsVRkaO8jrk7ee8ql8-maRNH9_s_6Y_t84oyhZRIapD1I19xuCzyQQV6STlSTbt7myWHAUnw6aK4l1B5h4D--NJ1eywolivt8P4Ut8wqcj8xex1lsfKh1hGi32aLcXXR3GhMA96GZDTVH4fxpirFjdSc2RbCsy4h3uznPbQlzR4EsCWaPCTUD9tcOKw-lkELxn3BhSHJNrXeqUBJUZnypJGwCua3AD-TC9opuflUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7057a07fa.mp4?token=jb5CEyakwmo95ODW-EE931Lx_tXy-E607B34m2xsKT6dANRgdOzaH6ouMm2kIrEcjLkAC83n-FLK1JsvkhXkUwsG3oFPy99bDbcjbjisjb7kWmsVRkaO8jrk7ee8ql8-maRNH9_s_6Y_t84oyhZRIapD1I19xuCzyQQV6STlSTbt7myWHAUnw6aK4l1B5h4D--NJ1eywolivt8P4Ut8wqcj8xex1lsfKh1hGi32aLcXXR3GhMA96GZDTVH4fxpirFjdSc2RbCsy4h3uznPbQlzR4EsCWaPCTUD9tcOKw-lkELxn3BhSHJNrXeqUBJUZnypJGwCua3AD-TC9opuflUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژیلا صادقی در لبنان: زنان لبنانی به ما می‌گفتند «دل‌مان به قدرت شما ایرانی‌ها و ایران قرص است»
🔹
این حرف را از خانواده‌ای شنیدم که ۸ شهید داده بود، اما از اقتدار و آرامش مردم ایران می‌گفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465925" target="_blank">📅 00:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465924">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">بیانیهٔ مشترک آمریکا و متحدانش علیه ایران در سالگرد مکانیسم ماشه
🔸
آمریکا به‌همراه ۵۰ کشور متحدش به مناسبت سالگرد اجرایی‌شدن سازوکار موسوم به مکانیسم ماشه بیانیه‌ای مشترک صادر کردند.
🔹
در این بیانیه بدون اشاره به نقض عهد کشورهای غربی در برجام، مسئولیت بازگشت تحریم‌ها عمدتاً متوجه ایران دانسته شده و از کشورهای جهان خواسته شده است محدودیت‌های اعمال‌شده علیه تهران را اجرا کنند.
🔹
این بیانیه روز پنجشنبه، دوم اکتبر، از سوی مجموعه‌ای از کشورهای عضو «ابتکار امنیت مقابله با اشاعه» منتشر شد و آمریکا، انگلیس، فرانسه و آلمان از جمله امضاکنندگان آن بوده‌اند.
🔹
آمریکا و کشورهای همراه آن در بیانیهٔ جدید اعلام کرده‌اند که به اجرای محدودیت‌های بازگشته ادامه خواهند داد.
🔹
آن‌ها مشخصاً بر جلوگیری از انتقال تجهیزات، فناوری و موادی تأکید کرده‌اند که به گفتهٔ آن‌ها می‌تواند در فعالیت‌های هسته‌ای حساس، توسعهٔ سلاح‌های کشتار جمعی یا سامانه‌های حمل آن‌ها مورد استفاده قرار گیرد.
🔹
بیانیه همچنین از تحریم‌های آمریکا علیه ایران با عنوان
«عملیات طرد اقتصادی»
حمایت کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465924" target="_blank">📅 00:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465923">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حمله به یک ابرنفتکش در ساحل آمریکا
🔸
اف‌بی‌آی و گارد ساحلی آمریکا در حال بررسی حملهٔ سایبری به یک ابرنفتکش در نزدیکی سواحل تگزاس هستند.
🔹
بر اساس این گزارش، نفوذ به سامانهٔ پیشرانهٔ این کشتی انجام شده است. هنوز مشخص نیست هکرها چه مدت به این سیستم دسترسی داشته‌اند و با استفاده از آن قادر به کنترل چه بخش‌هایی از کشتی بوده‌اند.
🔹
در گزارش‌های تکمیلی، نام این نفتکش VL Prosperity و زمان حمله ۷ اوت ۲۰۲۶ هنگام عبور از تنگهٔ جبل‌الطارق ذکر شده است.
🔹
برخی رسانه‌ها نیز مدعی شده‌اند هکرها در عملکرد موتور، سیستم خنک‌کننده و ناوبری کشتی اختلال ایجاد کرده‌اند؛ اما مقامات آمریکایی این جزئیات را رسماً تأیید نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465923" target="_blank">📅 00:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465922">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsmALGcMnE54Z0lfSipfWNx6ql9l7G3vPqXEaU-27ZZfB8OXuJgR2ppXMTj0HXh56DvU4_owFkPIEXz5zyt_5YAgGNmCdmi6gGNp4merxtzVy04aKDd1L-NsLLUKjFeYqQcsYJ-I-Z0JezAkFVbi46PveX2ax3Ur_nSI7v2Q4szhmav2J2deT0kLYTZjdSQBqllfSpL2eBOyaCXz_xS9WEpE015oZ5aXevL2lDEfg4MO0mmL8A2T7xeas3rs-i2mwTci24nc1SMm1X1xi5JtMLHXAewACEbvONZUIzkw1tgAPmStQN4-RnXmv38uM7OfOd0NDuLfZlYUrGNhWSdMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطق کج‌اندیشان
🔹
الاغ طلخک را دزد برد. هرکس از راه می‌رسید، نظری می‌داد و سرزنشش می‌کرد؛ یکی می‌گفت: «همه‌اش تقصیر خودت است که حواست به مالت نبوده و خوب مواظبت نکردی!»
🔹
دیگری می‌گفت: «تقصیرِ نوکر و خدمتکار است که درِ طویله را باز گذاشته!»
🔹
طلخک که دید همه فقط مال‌باخته را متهم می‌کنند، با کنایه گفت: «با این حساب، فقط آن دزدِ فلک‌زده و مظلوم هیچ تقصیری در این ماجرا ندارد!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/465922" target="_blank">📅 00:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465921">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW9klKYn6xdE4_chAee1cv9WN6drdQ5H-V35vrtnKGDZMts2LwvsOaodSLlaC5TfL8F2Jmthj9rNamor7lWialWOZLM_G76AvljJKXBhYdcxRPX39Akz83XjS2GecYqdN_cj8W8wZxs_AULpk_VBofpqiTP7vpDuXF0J6Hkbjx-kGil5C0wzYL8Vx6zleBV7eX54rWonpldy5LdqkLnuvcCn9NbgOFLTPHJEhPjfNdK81d1ODyYgBtUIiTaYboqclp2uJCDVFW9E44sO6flxW-SpXTvEWKCI4iZ-8whZuTIYvejnayDVETAmEREjjwpJZRxqYnqJzea7wcYR9-qJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465921" target="_blank">📅 00:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465920">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aadee68a7.mp4?token=vVtIzfzb4WtbW568-tSxK7GNYfFwticexRumeU_ZWeIVfEXoJEzQLAHhnmnT3WqE5vKHAFa3XjV92Z6QCE6ubIfczetwyiwgQ0YQgHSkOBZL5TdOqIYZ2KpAGNLu5KqM-qctw-IpUUp5rJF1jiL2zemvXnxZ8UZuJFJlzNOE7t-JPBmJxeA7R4Gk0TAGopvHazpUGpCGQ8Uw19RvJnEHRbPdUn6uzerEcIUnjOS4R-pLKylUYcgq0c4C148UabmV1zVTheYCYG6LFGa0lkRkx5s7sibzvHLzYL_n64Fs7Fbl4cFf0jp60JNcKOxFK5Swz9vN1QWDUzSsbF1wpTLABw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aadee68a7.mp4?token=vVtIzfzb4WtbW568-tSxK7GNYfFwticexRumeU_ZWeIVfEXoJEzQLAHhnmnT3WqE5vKHAFa3XjV92Z6QCE6ubIfczetwyiwgQ0YQgHSkOBZL5TdOqIYZ2KpAGNLu5KqM-qctw-IpUUp5rJF1jiL2zemvXnxZ8UZuJFJlzNOE7t-JPBmJxeA7R4Gk0TAGopvHazpUGpCGQ8Uw19RvJnEHRbPdUn6uzerEcIUnjOS4R-pLKylUYcgq0c4C148UabmV1zVTheYCYG6LFGa0lkRkx5s7sibzvHLzYL_n64Fs7Fbl4cFf0jp60JNcKOxFK5Swz9vN1QWDUzSsbF1wpTLABw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیشابوری‌ها در شب ۲۱۶، چراغ خیابان‌ها را روشن نگه داشتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465920" target="_blank">📅 23:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465919">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d70034ddec.mp4?token=uEVNbv18OLKRJDKx4NqcGpyH4Fw9PB12AMofnYLw3SkZdNDUxpKCkP9DuW0lMp6ubO8N46hJzVMgeJs6YaHh9WFZBPQmMxzDnopekJ99gKJA9y_uEaaafVxROGI1sHdOLjIOSIbWVidpw6fyB9k4o70akNVKTnCkRFcQITDkF_1P1kPz9gKi60J61LhEvcFjTpUHKkljyibC8uzMJCG8owTwWk_cMEHmahJf9Awnq4k_04ZNIrnP4t4HIXu8PoSmRUZ7Bs87DWHCVbqxKW9rjgK-Tp3OCvDWG9lIqVASgRd_MmmakhMn_3q6w7FHi5AOT-wM7bOiOkayIs_4QyzDHYrU_DZlQYMhQr8_etOEs1fK3NzysmcLWI9gz33rcEmHsXzXrojRL8XYJGd2B6Ncv5fD_Umcz7qJWQfHjXJvIUwcdl3QDLRMKCr0prDwX_GuJLc-MjLpW9jJB31jcmRLE_YTKjNi5bwzEyTMFy7iPGGUJKdn20y0kG07P0IE8n-1FNnGhGm7BUDmhEtgypN_MQn7XLFb4DuaKO1V-tQFQdTvt2i-jEwiX0aSECWr6OYSX0lXk6Gf47G9msRevkLWcnXIpueHLglPmlWo1vn2wJDa68bma2YcV1tHOrcENV5Z5p-3BzjW5MEhspDyTpzJ-xGpdMImqCVVqQ5v7o1_Idc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d70034ddec.mp4?token=uEVNbv18OLKRJDKx4NqcGpyH4Fw9PB12AMofnYLw3SkZdNDUxpKCkP9DuW0lMp6ubO8N46hJzVMgeJs6YaHh9WFZBPQmMxzDnopekJ99gKJA9y_uEaaafVxROGI1sHdOLjIOSIbWVidpw6fyB9k4o70akNVKTnCkRFcQITDkF_1P1kPz9gKi60J61LhEvcFjTpUHKkljyibC8uzMJCG8owTwWk_cMEHmahJf9Awnq4k_04ZNIrnP4t4HIXu8PoSmRUZ7Bs87DWHCVbqxKW9rjgK-Tp3OCvDWG9lIqVASgRd_MmmakhMn_3q6w7FHi5AOT-wM7bOiOkayIs_4QyzDHYrU_DZlQYMhQr8_etOEs1fK3NzysmcLWI9gz33rcEmHsXzXrojRL8XYJGd2B6Ncv5fD_Umcz7qJWQfHjXJvIUwcdl3QDLRMKCr0prDwX_GuJLc-MjLpW9jJB31jcmRLE_YTKjNi5bwzEyTMFy7iPGGUJKdn20y0kG07P0IE8n-1FNnGhGm7BUDmhEtgypN_MQn7XLFb4DuaKO1V-tQFQdTvt2i-jEwiX0aSECWr6OYSX0lXk6Gf47G9msRevkLWcnXIpueHLglPmlWo1vn2wJDa68bma2YcV1tHOrcENV5Z5p-3BzjW5MEhspDyTpzJ-xGpdMImqCVVqQ5v7o1_Idc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور متفاوت دانشجویان کرجی در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/465919" target="_blank">📅 23:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465918">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F30FWR7hNVeIMvOZ4kX0K16YMVUOlHAuViCXAQ2Y0_TE9ik6Wuw-8Ons0e6wYZytLUiW0jr1Va59fe9flQgjEIzLmDhBwEFsSZ60UHyF7YZv7zQdJRLxLhGUXTy3XaX7LV3lCbG6DaRQ9o-zlXgFPDbBPbQiJ-f1mTExnDE5zbkIEkRM1nEmsAOPMrvJWUCKqYJR23syjfvsfKk6tOJ6Vspb1whAvgmCZAymoPe-7Sxy2sWpYXB0QiKnyr0snBUPdaIes_02Bge5-R3k11KMWMBEmydoH1E7gGgWeHAmQobFH9GfFriGYDLUy9SC_RpkFDARlku1dMFMqDpsSR67Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای رویترز دربارهٔ تدارک عربستان برای حمله به انصارالله
🔹
رویترز: عربستان سعودی در حال بررسی طرحی برای آغاز عملیات نظامی علیه انصارالله یمن با هدف بازپس‌گیری مناطق ساحلی و خارج کردن تنگه باب‌المندب از کنترل این گروه است.
🔹
منابع منطقه‌ای و غربی گفته‌اند این عملیات ممکن است طی هفته‌های آینده آغاز شود و نیروهای یمنی تحت حمایت ریاض در خط مقدم آن قرار خواهند داشت.
🔹
عربستان ۲ گزینه را برای این عملیات بررسی می‌کند: حمله‌ای محدود به مناطق اطراف باب‌المندب یا عملیاتی گسترده‌تر در چند جبهه همزمان در استان‌های البیضاء، مأرب، تعز و الجوف.
🔹
در صورت اجرای طرح گسترده، ممکن است بیش از ۱۰۰ هزار نیروی یمنی برای عملیات بسیج شوند.
🔹
یکی از اهداف اصلی این عملیات، عقب راندن انصارالله از مناطقی است که این گروه در ماه گذشته در امتداد ساحل دریای سرخ به سرعت تصرف کرده و در نهایت کنترل تنگه باب‌المندب را به دست گرفته است.
🔹
همچنین یکی از نگرانی‌های اصلی عربستان در صورت آغاز عملیات جدید، حفاظت از تأسیسات نفتی و زیرساخت‌های این کشور در برابر حملات پهپادی و موشکی انصارالله است.
🔹
منابع منطقه‌ای گفته‌اند ریاض از چند متحد خود درخواست کمک برای تقویت سامانه‌های دفاعی کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/465918" target="_blank">📅 22:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465917">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_HrdVhJrrSJpvutSibvxAjbBazguj15SjIZ2pVWKk6XQsngcIAmZJjYg16xgLHVhjXg21OieO0_77gmAPnz06d_xSjpzt_LOVIQydZoGjZrZq1GVc2he_-jS07MrT71UXv5WcSEjnVM8bsWxpO1pmB8gynn1DCyIQYCh2-D4ru4u_FTf1ttj1QW3SfFOM94bh1-TFEm1spQoRdMFW0SpdzioyU6GsGV7Jm30HTwWAXc4RQ543j2BSK53PYjNnikcwg-nmZ6kJtCg-oKxyWEazANeauEeAgIqTlXnRBkmZS8V_RmJigHdyVTMqJ1bxFeVu5bD45OOebK9W57TPfFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر رفاه: دهک‌بندی خانوارها به شیوهٔ قبلی نیست و براساس سطح درآمد به ۳ گروه تقسیم‌بندی می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465917" target="_blank">📅 22:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465907">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/euFbZj2BDbgOTrxotW2qO698VrPhMiieLwjdNp_Al09ZP7IQuz1GAQNUW4BQPG7JkHp-f39UFcQdclm0-FoICblR4Ar2DtJvW2OJn-55tRo3IFivAiy7fpP7p3-_MLEgcM3hpXeLncz6a09orIzBPzN4YIIkgTB1i1cwl70D9V6SGrpq0Fiyt9wKotIs4Yq8ftGvTHgaG84Uz2-yW1qwDTM4jKtsd3TZDuPFwy0fC8jUCTt_Nq2SZfwpI66_eNJQO7Npf-QoTVHws4dBwhrU7RhKiN7UFDIqYcAjm1X1tOMcLIyWJ9eYjQpJXVHGCYKTv3GyuIvDjsaHH82H86t1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sy9MBCz7rIgTN-h9jI2YKgzI-I1RdFbR5kDMD60W5cNgw9iTbZ6CaxhXWYpbZHoAtPOl6q3Dl9saoiA9RTkHN8B1d3yl4p3VZdTQ-FB_PZUJs81-QWROWyzOeK4WNF_v0fvCmgFHG7XEP5FcvP_YSWMN8RNm-xEI3oVyPbY-dh68Ukv44h7lu-NNHvi5EwO-YpaU6EgoRUx9pxqcGwoAzrQ2JdddqK6u-kU4KBjkGdL6glGZcxqA0R6sLKklJfKDRJa71qxF-Png54-ATKVii9CWJ5DnVuIYasbpazVspttcRhBiUNhLCT1ZBQBS3qNZRrN4uPUA3Jms68TTpbSWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTrfiACYMJxi1NQlXeTiQyhuHFvJsb-zyLFDNE4GuT8s6W7IRey5bBiztjnOiR9wnvgPr1eSjepZdBBcsqVHZSGkiWnwtCY8Rd-rf-icOW3jlaESL6B5rlZ2ILu2QYEkcQK-zDhKovKeJnIcZgX4IFfaC9b2pUSkEgx21KNWomsPIQiMd4JHdqdE9_zHZqwA4ObVE5MJylveHWlXl-EjU4P28dDbPfcHKpfNjxNd_Q5Q7_zfmOK0ugK6W911I_EKKSanix3rqeYQNnU8duOLDhU_FYCBPuvwvI70BlZoqu0md2MZeTGA-bnxyZb_Ow3fvOM2UcUigAriGlSUIu0J3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdeCDPsHWV55lQyXXl-pUvtk9ctdNxp1LSOvFODldknhQpB9g3vEzV8oN8WV7Pl_Iuid8E04BolHmzWqgp52oeKeekgdiOG9c_lLiI6bWKJoLeKfzw_Ysjwoeq2V_zPGhIXbwmuXGxKjd02NEpqZohLogulMCeMAf5WlMXcaQOeW-2J0lx-Txxy_ljyTkoh45RpleFC1yumiFcqvcRwgEGCKi1hQlZDUaAmmFrAu--jx8c03XhsGVDI8vQqHqvcCHQLOFOYm3HtiSnQiGJT74YC7Yij7CgJc5bubb8Wrv58GfV0gUTQLoTkekGSA76NkeIU2rxsYoTMCB_OpOxNQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUisVw95ZWb4pDoHTMJCCDWu4V9keTrp_ov2xVrkEcG0FrFbK8G1NBKXt8yzrUg5hDXHrMLXMUZCQnz0ebyJCsrW72QuoS9fztkLsxl6S0kjqHzkR3vGpjPjw6qGBjKsjvSV5Iit-rkbAm67L7wtrUl2eqpyHP8GiYaf-P-kPrmmoFmhuveyoQFCIthfgQ355EGJK-3uqmBppSDwhf3Ji4Nkx9eQSnjR0Q2iFDZ940m01qjJ-qzIUN5dp2erxUID9XI3nxItVTvpLR4BMlQTprppPTR2sDiKXUk3hlWpztfuFPApx3OEKoDOTzZLUbaEdrkdACsMN6Wm_7tz-khpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6GQ0mPvoOnBiT2l7epW-I_G49PLODCBTueacFF1dueCQfow1b8hCwiSIqyi5M48Qss0C9ywPtYt9QXLjQiqRHCDegex-oYOOdVrCRhwA6U0eRmXuIGF3Y-K9InGeohw1ZA8rNcF8L-nx8DQpnXJXCwsdaRXGgXv29cTnO2Ifr7IbvfekHU2ULG656DRAD-lHor2srZqbjWjvj7Azq3XCVIfKH9dgmyIoHKOLagbeNdezLXNcRjYu_7rt2JX4BJm50ENkvCyhtJQqBz-ibLrVTXidaB70_ZVjUrlOZPzfTRgx7usXe_EJcstHnGqX9G1noDdI0t-mUF-rfPPLyCu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuJuRlEU-gDrwJkhAlgAtK7vQeKrZMljQsgxNQ6Rg9x8eWUnQ83883ym39UFNh8s7CsT7iR6AJE0oasB6UU42m9f9ALN29z8O7RiZ13tm5MEeP-VZ5r7WRE6q_mitaqRZM2M0p8MY7xuKeoPHi2jmdfuAL2xCP7C_MtfqUc5pa2LzUas_YVl7hn0p7In0ckLPmR9cmAROtC11gKC74SPaF2BNbRU9GvBbHJY05Nx4XOqjiFF-TLPNFNXQEQ-6UZPFv6e-175UN4uyJfWPjqnU1LoOxHud3e6qzRX_FJAP47ziqau1xh1AeGCsZHiH26CIb1yGIreNy9oqn1y61ES6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/od8dWnyrwUWXTDaBNHDwwu-ASbn6cXavgr-xLK1_fk9WJaQS8e3kemFZYmDA4LUsyR90hP_FGhZ-r72h4FqtStvSXDVvwWKM0E8gNcEOTXG3lsg3XhtkRNPz4EWLYj_iXhCpPd1upW8k2J0qucLmheu19INlz9sV-TmT0VkPxGHTRAEEk41VBeu5Haxux5bcSj1NPuz5n24Dz3yYmFTKjbbAPQsNExHBgxQciXtih_chBt0XR_c6_fIvgiZD2NPk7z-zBrBaDBRfUUK-dqNE93aOXClom5Jn-hCpzRnJi9K_UVoSRWBd4w7qXCQZ4Xhn3rN1bGR6WWYImZRy-3On3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1RHsG29yZGw3AyKsYQB8npHnY9hN9V1jhJmtUenuyQ1u6qN0G7sLj6_M1DbqkrNRwzRWCihie4ahQu306Ot67B2jddrhyCiVW9a9Pi5esrQ_R5lAgnGTSEky6babgwlJzPO31-VdluUWPr988NL8YCMmOwHzF9ayG-7RVMKhHUe5UnaQGNmbvrSEqvssFGahejrM5N5_VSb1g18zPkP1dEW_rST3e2wj42m45Wi6c1UZBs47uRhj0ifBJzGWSbbvmJx2vqTKs2VjuC70aW7LpC5muCaZsXEB8PbZsIJ1LHa7kXsW03xzMlls9rWQktfIQyWfuqYpoGwbBUIm_7_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQOUxF-ygnQxwtW98cj3i7ea1Jox93P5egMZGxovVsZY8PB7OTMFubUtlF6zvR-xe4XqXad_ByV9OxBZfeEnac2HJenb0-_KbqfycclqWU4T1iWzRnj_BCBC_bZrVGlOEvaYkdsxR6DKnC3BsLKX1YcNY7oTKIc41ng564LEnTKQZjaRcWTjt8tF9boSTMMeBexvEQzApji32e2ULVStCvlSzt9VlsO6wRKkLCSsyrIlUdUYGpjWiqxOEjtTsj3cfyM4YYrcbT9V46fyhnDXpxLIcR3sAEIWmfCK5DIAdlsEK0kUx5hJ3Tj08-BCm5mPdokY-ThhSl5XZdqscsk-gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع باشکوه جان‌فدایان البرزی
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465907" target="_blank">📅 22:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465900">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgAbneBs-EF12pnHaGbBTmB5YItRkI2l5vMVy5GKj1nysYajeiuXCt44xzoaEv5qZhNgNPU6tPrAcIjly4CbMStMFTT4KGVr1UwWwZRnNSbOpwLv-ik1KCid8LvJTbRicX3diXnZqjNYLyVOVFLg7J1Qc_9HN602VeMtRe63trwU_W34ro2RmUM0PY8nsUSS7I_qOjeJTT8pWD9stmeyyIb59UeGRMLfI2sDjcPyqeyT1wFa2ZPKtT9t4dRlosnL53ENf3glHZSpn385YDIsh38f1dpAdY9ugwkKNnPEvqOIQLOTD_7XRrPZlgBq4wqEIkGF5I1vhNqhU2NqhtGaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohcTHynNDFHlv3qKiZ3nIOq-Uqw8RfH1FKiawKyLO479v77uGQBQKdmzUtm45PI_pVpPjJ8NzYquSu_GP0q6khjgTiwuEPeeVj-YKtvbp6fbq-qUoMdCKe4-2OXMzpKCMyNDNNT7vFGYviVkhkJW3m8Gg-fk-9l9h_7CCR82PJ1d2TKXUwHjsO9Qyzkl6DXUIIK8gI81woInJ1sgmrIQRJC4LZdRlqPj8kFvWHAWkJb29z47uHr0eWdZxB6lUODVmJ5NeR_r9LL3dS31odb8eJWp_DEyQuJHfm6sf2XdHBYsoNkvyVhGyCj1kcqSZt08ckhWab8DBnLb4r_4Ts9_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UftyUsmD8rwYu3HnpxJJoBlfiJl5SbTu6YljEUTOABFkUZ1FmBG_K5la22IJ476wK0Uq5MsbJpar6W-070UpLBh3ef5suxDi81n1kXRRmx9PZ9blZXIW0Q3JBvj5I-6j_Mx1Vu1IxzxnL42HBSFSDUBESJl4aMVYNGm0kInGKi3KdBpvxdKveOoapvU8Ax2hOFcg7kwit1GmnytVvUxRHs3c0P8Mb_dvhVKBfDZr7z2oqZ-MnFOYC0J5A6fy1vS427bxTfasF4h5O8fwj4RjGH12U4GFmdj9ocTKTTG1tW0PdUVdUy2aYpj-Ef5yNhxpp1chLZTpPI-ZbLyqpTzQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOPQc6e-IevozTGbLWekjapkd8KhhovNVxFV2TwvNUEMGMlvjUBekM9dT8GgWGTmRywTGQ2IZc77o5jswYV2mp4_bbWS_nPYK-X2jIYIoA7NWdUth-dLT97Z02UC2JAv0l2_kPb12xp7QobOs6rBcfl9vVg_dh9OxkQSdQ2nSZIp79IYSmTTcFdks9wJezED3QoTJDH48368Xi6LivMSCEMJ4AEg1Wv7jllkd2nGemAGhrGGX2Eb8qB5TOUs1R9GeBlI3A82gV8Q2gHkfHVn062pvHwowAR--q8DjsFl5M2ikF_wNS1UAAtFz2zIoZlGOPkd9e2OJH6n4k91f1Mm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7BcFJSOzN5Y0-4496sJI5hIrx7otxpOoUmgwZE8YBVds4f4Q_Xd8VcIC_Qbxyj3Fetc4jG7cb7laE4i0HfQRxt3S-AaPxb1JifEskaaZ1gA08QRoL8c-WGZVO_HhrOwQqAbJMAuOgZnTVt5IVizDl9nOiaaxgSrszBcBPr5Rq749EDo5W5hms7TcU8Gzx3EeKtStcYkx49cdDp0ubUIQdN3KQOWDehf3yaoVr438Ek92QSPlEZjZCiBehKSDQFbMvkylHEhT5bLQs0Xra5xJs4DJ6a0KHXj409teMZIAP6LjyjjdlGPImDmPc_U_ARnWPo7VuQan0AxoCpqzRR6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3kAyhCV0e2nR1gBq7WS81UOsnLMYOAuQTbIT2MBpJ8Q-u26TAP1cfzxTH_BzONOtIit8goC5hANd0CEZqXob9louCDRVh1Ha0noW-TtEZiYMKDNwwavLsdKE24Z6TLDzcNfzQdUL3JRpy-Zg_YsuD2e0nbPvkofhxgvLFnktUJZfbn6aOAAXIj_MimPS180Mmo0TVqKgNFVrnZk1mn4Ihsq6JHMjV_4sbsbJtiyaYWHXxAWzLdpiLxABXnsU6IY8NuikYcgFM7Z_aSKXm4xRJy6A54-fKS45F9Mf0jQFvAI3vXHmYddaRGl-Fq2FK-sNwCktVmfI-TLMp3mHykwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUBWcfdcSMnpcy5Hp8mxzNWRBX8gv-OfPXVf69qsR8VvJihUjbJShUyCfKkWxGt9RY6E2q0nB5a5a6Y1x-nii8W2eDo7hcoXo1rzCoq6fTQjan9x94ysMDMyGzTaXEqRK6VwXXNkkxqLCj_PTNw0huiChmrpwwD_Ka1g-drmWtwk9ogn_lW_NVqJZEatncdhZze_Aq0oFdh2Uwgn8ql3OLJXRJTkFhPt6GyF1gcrvKpAqHOBELjVuIeuOGuQxdH6ItrofMrhH5FAXN3gy2jKv5LcOpizLrT1zWlFqjXw9JZCmiWXDh6NvNbUW0R8CObGfEDdqaegVto_y1XPa_JhUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت دومین سالگرد شهادت سیدحسن نصرالله در حرم حضرت معصومه(س)
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465900" target="_blank">📅 22:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465899">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
۲۱۶ شب گذشت؛ خیابان هنوز در اختیار مردم است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465899" target="_blank">📅 22:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465898">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">جام حذفی حذف شد
🔹
جمعه‌شب، سخنگوی فدراسیون فوتبال گفت: «تا این لحظه باتوجه‌به فشردگی که وجود دارد، امکان برگزاری جام حذفی وجود ندارد».
🔹
سال گذشته جام حذفی و لیگ برتر در ایران به دلیل جنگ ناتمام ماند. بدین ترتیب لیگ برتر امسال تنها جامی خواهد بود که به یک تیم اهدا خواهد شد. این یعنی از آخرین کاپ باشگاهی داخلی که به تیمی اهدا می‌شود لااقل دو سال می‌گذرد. آخرین جام حذفی در فصل ۱۴۰۳-۱۴۰۴ به استقلال رسیده بود.
🔹
باشگاه پرسپولیس با توجه به عدم حضور در رقابت‌های آسیایی و ترکیب پربازیکنش در نامه‌ای به سازمان لیگ اعلام کرده بود که باید جام حذفی برگزار شود. همزمان پیشنهاد شده که جام حذفی بدون حضور بازیکنان ملی‌پوش انجام شود که هنوز نتیجه آن هم اعلام شده.
🔹
حالا علوی، سخنگوی فدراسیون گفته که امکان برگزاری جام وجود ندارد. او درعین‌حال گفته رئیس سازمان لیگ در حال تلاش است تا در این مورد تصمیم گرفته شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465898" target="_blank">📅 22:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465897">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO6JEaXpe74dXCw6EbwcdfbvELHkqjgDtqNL2QN2uegfzRYzpQsTP1q519QtcEUiJbf0qp_28qni6ePX9UOfIqhvHFmcVUJWx8RzyLWcodthd8lypZndNTQgqq79OQc_6HmZNfweDmFUAVKJIqDWoGvfb0fDFNvr_Q7Ds-YpCy1uZvsdg_XPhgK7YxMq9waYFnfnCA6XHWmWNzFIo7vtq_eq3Duf_LpL4dJCmNEfa2e56y4r1S_du8YhahTEk8pHpNZr0cCYc5Fo3HPIwAU0XZdpsPTqM2aw8DgHTB4yH9x2RlTcPSmx0kDMGl0D8bDlmSyb-eXo6jn0l1JcMevxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر متفاوتی از سردار قاآنی در مراسم «نصر قریب»
🔹
مراسم «نصر قریب»، بزرگداشت دومین سالگرد شهادت رهبران شهید جبهه مقاومت، شب گذشته با حضور فرمانده نیروی قدس سپاه پاسداران، خانواده شهید حاج قاسم سلیمانی، خانواده شهید صفی‌الدین، خانواده شهید نیلفروشان و خانواده‌های محترم شهدای لبنان و ایران در برج میلاد تهران برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465897" target="_blank">📅 22:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465896">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
ماجرای هالیوودی پرواز فلای‌دبی زیر ذره‌بینِ کاربران فضای مجازی  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465896" target="_blank">📅 22:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465895">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa1a7af43.mp4?token=EM21qzW8P2wI2kRgQTEDLk3g0pT9gB-rXouIjYDjhIFMaMOTElXWYTbSpFUfTng4zyxDznP6qC9XMYHx1epJQJxn-ry1H7u3QUDNHFZNXp0LD0TkITm0PM-uUU2ewGdbVVTTCYEJ1FuZE1qz0AAkSsPbY1NHTBGvNknI4gO3NbmJXkmfOpvfynXUF3A58l5SyEEibz51xRQn6SXKdcllzhr4EyqyZUCfWm3mrBBDO5NEUkz-dyDCmQwq8Usmd_mGUwX5G_8s33KDHzAoWDW1IR4NhOjsZyjvMFQnZOE32TwFTKc0B3bIMNITbCGjHZwn6HIT89rmt4QGf9z4_7Q9Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa1a7af43.mp4?token=EM21qzW8P2wI2kRgQTEDLk3g0pT9gB-rXouIjYDjhIFMaMOTElXWYTbSpFUfTng4zyxDznP6qC9XMYHx1epJQJxn-ry1H7u3QUDNHFZNXp0LD0TkITm0PM-uUU2ewGdbVVTTCYEJ1FuZE1qz0AAkSsPbY1NHTBGvNknI4gO3NbmJXkmfOpvfynXUF3A58l5SyEEibz51xRQn6SXKdcllzhr4EyqyZUCfWm3mrBBDO5NEUkz-dyDCmQwq8Usmd_mGUwX5G_8s33KDHzAoWDW1IR4NhOjsZyjvMFQnZOE32TwFTKc0B3bIMNITbCGjHZwn6HIT89rmt4QGf9z4_7Q9Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کار: بدون نظارت و حمایت هم‌زمان، حاجی‌زاده‌های اقتصادی تربیت نمی‌شوند
🔹
در حوزهٔ اقتصاد نیز تا زمانی که نیروهای صدای جامعه نتوانند دو نقش نظارتی و حمایتی را هم‌زمان ایفا کنند، نمی‌توانیم افرادی همچون حاجی‌زاده را در عرصهٔ اقتصاد پرورش دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465895" target="_blank">📅 22:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465894">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77717107eb.mp4?token=eSIQWuEijWXru9jhc6EIsIfmD5mF6jsLhpdXnKw76P7SamweLJiVWGSCMO09-kFkOj1qMVlUyYJK-T92fr72o0NcFb2Wq98lAJJ69u8jefO7GZVlSgiHNkHCj00bYnypcnhLTZNWuHKrs_J67FxzJh9ATRp8VzCrb2sJSWxTlaDjDoxtZFHJ-l6LIaoF1FaMDaYKuOZI0xJRJetjGg_4X5cQibunlUjWmhDgFjz8e2MWc51BgOQw80al-TouP6nBubP8_rH8z2zPt55D-g7gPUqksLrxk49kQXzrxJ1M50zwmk6QXGFoye64LyUzHpvUeB0nlojfydxL6jDxa84fpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77717107eb.mp4?token=eSIQWuEijWXru9jhc6EIsIfmD5mF6jsLhpdXnKw76P7SamweLJiVWGSCMO09-kFkOj1qMVlUyYJK-T92fr72o0NcFb2Wq98lAJJ69u8jefO7GZVlSgiHNkHCj00bYnypcnhLTZNWuHKrs_J67FxzJh9ATRp8VzCrb2sJSWxTlaDjDoxtZFHJ-l6LIaoF1FaMDaYKuOZI0xJRJetjGg_4X5cQibunlUjWmhDgFjz8e2MWc51BgOQw80al-TouP6nBubP8_rH8z2zPt55D-g7gPUqksLrxk49kQXzrxJ1M50zwmk6QXGFoye64LyUzHpvUeB0nlojfydxL6jDxa84fpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای لو رفتن عملیات وعدهٔ صادق ۲ و دستور شهید سلامی برای ادامهٔ عملیات
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/465894" target="_blank">📅 22:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465893">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14248f3224.mp4?token=eGknVcW5wITxZFXr474fqWtmKKwZAi8fDSSUWAqhdg6yZY9iuD7rx3fa8IzganfvnyNYywetHONJRplVJEiGMNe8WmENCh4DzKYPc_kO8ulD3176R61f2zy49hzTvyxjh7xtcRx0te0Nz2945afmXajPYf6_ZIkmal7949T1ligOtEo67vLIDJ5MOREL5KxxtGxbxGaA0gsElrwqAKN_vHAzyEAwpWeR0iiYmVK4AvH8kOikL-UG0IE7NAkZqaLRXJN_1qh3OfLZQVYlItf9xnBqaEM26QFDWMQyRBBNFhH87SkQpWW3SJbFNikNSvLkbyfAV8wVTreUnjgLWm4DnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14248f3224.mp4?token=eGknVcW5wITxZFXr474fqWtmKKwZAi8fDSSUWAqhdg6yZY9iuD7rx3fa8IzganfvnyNYywetHONJRplVJEiGMNe8WmENCh4DzKYPc_kO8ulD3176R61f2zy49hzTvyxjh7xtcRx0te0Nz2945afmXajPYf6_ZIkmal7949T1ligOtEo67vLIDJ5MOREL5KxxtGxbxGaA0gsElrwqAKN_vHAzyEAwpWeR0iiYmVK4AvH8kOikL-UG0IE7NAkZqaLRXJN_1qh3OfLZQVYlItf9xnBqaEM26QFDWMQyRBBNFhH87SkQpWW3SJbFNikNSvLkbyfAV8wVTreUnjgLWm4DnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ملتی که ۲۱۶ شب، خیابان را به میدان حضور خود تبدیل کرد
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/465893" target="_blank">📅 21:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465892">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ed80517.mp4?token=eNCvikBG2IAUmj0t7VOJ2nO67UlKEkICG4xUF5-jiy_oljHx-8meZzLxUydhz6LQBJCFQz4ApvDI0SgFFFppJocFESrcaWG83jkYqhePtdLlJ2dn8cs5CxrsfP2FIJobBwxrTqmjwiqOqa4HIYAJyaKi6tYhbGOU_mIJ8EhnjkTGqzKZ1N00XAL8jqLeGPMI2Hyti9PvEsqzOtZTlhrRTh9bffO4vxC8MQZHLzf2SMyPDgAdil9w5BNWpf7q1b4NcD-X8SaplShW648o_oUfBmMCMGhPfZYFY8u6wSfbGps7z1-Xw2GcXv1CvDrt9yEuFLc3zciZaRhWJnIt-_W6Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ed80517.mp4?token=eNCvikBG2IAUmj0t7VOJ2nO67UlKEkICG4xUF5-jiy_oljHx-8meZzLxUydhz6LQBJCFQz4ApvDI0SgFFFppJocFESrcaWG83jkYqhePtdLlJ2dn8cs5CxrsfP2FIJobBwxrTqmjwiqOqa4HIYAJyaKi6tYhbGOU_mIJ8EhnjkTGqzKZ1N00XAL8jqLeGPMI2Hyti9PvEsqzOtZTlhrRTh9bffO4vxC8MQZHLzf2SMyPDgAdil9w5BNWpf7q1b4NcD-X8SaplShW648o_oUfBmMCMGhPfZYFY8u6wSfbGps7z1-Xw2GcXv1CvDrt9yEuFLc3zciZaRhWJnIt-_W6Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نتانیاهو به‌دنبال بهانه‌ای برای ربط‌دادن حادثهٔ هواپیما به ایران
🔹
نخست‌وزیر رژیم صهیونیستی در واکنش به حادثهٔ اخیر هواپیمای مسافربری «فلای‌دبی» به‌دنبال ربط‌دادن این رویداد به ایران گفت: «مشخص نیست این حادثه به ایران ربط داشته باشد یا خیر؛ ما نشانه‌هایی…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/465892" target="_blank">📅 21:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/490dab02ba.mp4?token=H92wkh4gGj6rvGUFVtA1HbfrxxmtmL341XTFWJbAbHn-wOnUC2cz5JvtIofq0zAUvjJiZnH8Vc_Qyusxu70fGEy7SbIAl71giCPVoQG91frJi2OHiYbaJSi8ETO4sUoSDfUpZ7qpxkMplztw15bW77duvAs1YSrv1UskWtlyqi1-IHGOZPJyMriJt79LII1EMeVTSczQYhjocADBvwYklSo08ZRxRk2QHd1RV6NO_dfdGQ5nXHpaPgA2J8VXOCyiNBQhofiqb_irtHi9PeoczcksVIopbd4cbRuBWWDDvKkCgOMDqLQZzGdqwGWHnLJ4y5wJq_ZWnTRO1nVfqxWC6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/490dab02ba.mp4?token=H92wkh4gGj6rvGUFVtA1HbfrxxmtmL341XTFWJbAbHn-wOnUC2cz5JvtIofq0zAUvjJiZnH8Vc_Qyusxu70fGEy7SbIAl71giCPVoQG91frJi2OHiYbaJSi8ETO4sUoSDfUpZ7qpxkMplztw15bW77duvAs1YSrv1UskWtlyqi1-IHGOZPJyMriJt79LII1EMeVTSczQYhjocADBvwYklSo08ZRxRk2QHd1RV6NO_dfdGQ5nXHpaPgA2J8VXOCyiNBQhofiqb_irtHi9PeoczcksVIopbd4cbRuBWWDDvKkCgOMDqLQZzGdqwGWHnLJ4y5wJq_ZWnTRO1nVfqxWC6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واگذاری سهام سایپا به کجا رسید؟
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/465891" target="_blank">📅 21:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حکم حبس الناز شاکردوست در دادگاه تجدیدنظر تأیید شد
🔹
شعبهٔ ۲۳ دادگاه انقلاب تهران، الناز شاکردوست را به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیری محکوم کرده و به‌عنوان مجازات تکمیلی نیز ۲ سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری برای او مقرر کرده است.
وکیل شاکردوست گفت که موکلش به‌واسطهٔ انتشار یک استوری در صفحهٔ شخصی خود در فضای مجازی پس از حوادث دی‌ماه سال گذشته، به این مجازات محکوم شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/465890" target="_blank">📅 21:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بازداشت مهندس وزارت انرژی آمریکا به اتهام حمایت از انصارالله
🔹
اف‌بی‌آی یک مهندس برق شاغل در وزارت انرژی آمریکا را به اتهام تلاش برای حمایت از انصارالله یمن بازداشت کرده است.
🔹
مقام‌های آمریکایی می‌گویند این فرد در سفر به یمن، اقدام به خرید موادی برای ساخت مواد منفجره دست‌ساز و قطعات مورد استفاده در پهپادها کرده و تلاش داشته توان ارتباطی انصارالله را ارتقا دهد.
🔹
شتون حامد اللبودی، ۵۱ ساله و ساکن ریچلند در ایالت واشنگتن قرار است روز جمعه برای نخستین بار در دادگاه حاضر شود.
🔹
براساس اسناد ارائه‌شده از سوی اف‌بی‌آی، اللبودی با هدف کمک به بهبود قابلیت‌های ارتباطی انصارالله به یمن سفر کرده است. مقام‌های آمریکایی می‌گویند او در سپتامبر سال گذشته به یمن رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/465889" target="_blank">📅 21:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b75d5430.mp4?token=D0RDBjh9mrwKMwdO0n8TsKAaLZPjygoL6J-0HGH_RqbCWoa3NsLVuEEpufhOfDpxyUznXDhTPR5nlkfJn2xGVwMJfLtWAaRbwbrNpzFKyLtE77bxDylKoJOf2BadDEOyQSom_A_z7DmRRzf-aRw-qrYMuZOfcgQyU4DI-xvGB5eqCSdfWFcZT0KumDZ2EADUyTG7N3PnWnYRPpgCgZNZKUwFPDh9aFl3Yzp3pP2ytEjfqnt1_XkFWMrml4TBXfwimCFvC0AJm8_RiTuKxWf6uWkxQEyJQ_btTIm130cBTb6EdnvgYQT7yhVdcolXZcRp1-wbawzUBvEIuEQpWIm5Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b75d5430.mp4?token=D0RDBjh9mrwKMwdO0n8TsKAaLZPjygoL6J-0HGH_RqbCWoa3NsLVuEEpufhOfDpxyUznXDhTPR5nlkfJn2xGVwMJfLtWAaRbwbrNpzFKyLtE77bxDylKoJOf2BadDEOyQSom_A_z7DmRRzf-aRw-qrYMuZOfcgQyU4DI-xvGB5eqCSdfWFcZT0KumDZ2EADUyTG7N3PnWnYRPpgCgZNZKUwFPDh9aFl3Yzp3pP2ytEjfqnt1_XkFWMrml4TBXfwimCFvC0AJm8_RiTuKxWf6uWkxQEyJQ_btTIm130cBTb6EdnvgYQT7yhVdcolXZcRp1-wbawzUBvEIuEQpWIm5Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در شب ۲۱۶ صدای تکبیر از شهرکرد به گوش جهان رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/465888" target="_blank">📅 21:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5177fc9a.mp4?token=g-lGImIvwK0e1-2Ns3Y4Fmtf_VasmU96AlEjgXOYABVY6CtDx8GseyjDzeJSz9CXQnQ03lWqOIsPLazGypN9c30l11R-iq21z0H-B66mC6YlVEpEZs0SmtAt7r_ab78w5Zy6X6kju-wiC8-6gqKA0s5xeydqujBMRIhxAgocd_fpTEcXTfPSRQ8tKLjwWnkPiOwgGtyK1AIOkcb3VskNooT6zheEkbhFXsz-UkD4sUdPmAKLuERsKyItd5ctMp4UWhcpvkpjHJ7qMESjmxZPSDnIlTQtGWmJIJbc750rhvdyvqPjQ80nP0C2ZH0BtSdEgqnGIbD7wJ68SfHYzTgySqghMCwLPI9Mj7Pdr3poIEXixMRgVJxCi5nYkwpV4J7Mb-VEswcGWAOu7qi2Z1IeERKcZvdTcquUfUN6-9SUe_yGFmTI3qW28zLq5eeWEEHnXO1WAy33DMBKfZc-HHMAR-XwICcuxCFLQBy3kXvp5EKYYfrSHHoBUkAqSgF5KIAFtr7dYASmKzUcX6H73SaiQ6abKVIKhQT1ePViKII3y4jiZ9DyasscJPb6Du1mvqTzm8EdvM4vzSWFuP5aaMH_2136kRM8_GkB737axW4PUvr2L7tkhlEdyJPWtliNBOv0riWUO9Oe0LnQz6IraSXMUHKBlK85saVfukmfQ1z6ERQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5177fc9a.mp4?token=g-lGImIvwK0e1-2Ns3Y4Fmtf_VasmU96AlEjgXOYABVY6CtDx8GseyjDzeJSz9CXQnQ03lWqOIsPLazGypN9c30l11R-iq21z0H-B66mC6YlVEpEZs0SmtAt7r_ab78w5Zy6X6kju-wiC8-6gqKA0s5xeydqujBMRIhxAgocd_fpTEcXTfPSRQ8tKLjwWnkPiOwgGtyK1AIOkcb3VskNooT6zheEkbhFXsz-UkD4sUdPmAKLuERsKyItd5ctMp4UWhcpvkpjHJ7qMESjmxZPSDnIlTQtGWmJIJbc750rhvdyvqPjQ80nP0C2ZH0BtSdEgqnGIbD7wJ68SfHYzTgySqghMCwLPI9Mj7Pdr3poIEXixMRgVJxCi5nYkwpV4J7Mb-VEswcGWAOu7qi2Z1IeERKcZvdTcquUfUN6-9SUe_yGFmTI3qW28zLq5eeWEEHnXO1WAy33DMBKfZc-HHMAR-XwICcuxCFLQBy3kXvp5EKYYfrSHHoBUkAqSgF5KIAFtr7dYASmKzUcX6H73SaiQ6abKVIKhQT1ePViKII3y4jiZ9DyasscJPb6Du1mvqTzm8EdvM4vzSWFuP5aaMH_2136kRM8_GkB737axW4PUvr2L7tkhlEdyJPWtliNBOv0riWUO9Oe0LnQz6IraSXMUHKBlK85saVfukmfQ1z6ERQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رزمنده‌ای که داغ دید، اما برای دفاع از میهن ایستاد
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/465887" target="_blank">📅 21:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465886">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f7f2b5305.mp4?token=WtM1iePkPh_4ps-_FUhnv5r_jfil4wY67PcYjQT0phbJAuVyjLbddR6NM-gdP2-O6SrTsnti8ySmdUjMhK6PPzREJ830uBGto7yPOuOtdg0SgYx5ezXqSVVOKlB0-Onv2B2VrRIU8er0bs-pWmAp9OPxXXv-eFj082mpOlaVjPTaz906sBP5P-ybjJECZKupy0H0tEiGTDyMXAJ2JvtR_kNxpi7PbxhEoZXkwb1m59lGYpJ_a3ReHDQvC3qPbkQl1l5ztEfAhwXA4f8NgQmgjt33UqlN_Agfpi71i1qrGp72e8YXzOD14MqyZn3UhoXaf9s_OJ0ErEXnR-NUevCYQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f7f2b5305.mp4?token=WtM1iePkPh_4ps-_FUhnv5r_jfil4wY67PcYjQT0phbJAuVyjLbddR6NM-gdP2-O6SrTsnti8ySmdUjMhK6PPzREJ830uBGto7yPOuOtdg0SgYx5ezXqSVVOKlB0-Onv2B2VrRIU8er0bs-pWmAp9OPxXXv-eFj082mpOlaVjPTaz906sBP5P-ybjJECZKupy0H0tEiGTDyMXAJ2JvtR_kNxpi7PbxhEoZXkwb1m59lGYpJ_a3ReHDQvC3qPbkQl1l5ztEfAhwXA4f8NgQmgjt33UqlN_Agfpi71i1qrGp72e8YXzOD14MqyZn3UhoXaf9s_OJ0ErEXnR-NUevCYQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ برای کودتا در ایران دست به کار شد
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/465886" target="_blank">📅 20:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465885">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
اولین واکنش رئیس پدافند غیرعامل به حواشی استفاده از ساعت هوشمند
@TehranFarsnews
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/465885" target="_blank">📅 20:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465883">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
تصویری از جنس ایران؛ کرجی‌ها قاب ماندگار ساختند
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/465883" target="_blank">📅 20:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465882">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0977608af.mp4?token=M3Mfr1YOblleYGMkPiuUUC2Ynf216kNnfRHxv23KKTbr-rXdZA4sBrw7WdDCk14Zin6_54GJXGohBsX1u_ts6SQaa7ScuacML8woKmxpXvKjSe4T_UCWOwaRy11mAlL1EFyQmHRv4GhJoLx_GCUmbkn0oYosq3xVsX5rrkBqaF3QNQpTSq_-j61vlpme_o3wYTsoDmGY-u2bvA3nZm9YzZj-PCo1w029QLsSALTdobVSXsa1iRe64GdRNMBTu89TfNc03azZMpxXs958O7Ntp7na_CxOoHTKDYDTVPnpeh5-OJBcEh3wimo7FwWEYnLj7ZjivLVObghHd7FVCquFJjn1u_tGoWELrm7DqChoyxVnUqShI-A5NZ3lUQ4kWBRLkmE29uPyhWJR69XFqqyClTvR4FqWXY2pMWI5sHujYKtM9pHOPtE72MRRSoEs2u29o82ynfdQVExuatoXYmGj9LApVNS4nl9d-VuOuIX1GkL3f2aXJD39ynHMynz4DHYGXV97vq1W1QwZxiK8PDPLWktO_zxqcT_GG1GoRIH1WQXwivbFWmKhvqaOu3XTWaWwakPZbz1FpyfhXptW5vQeyTw-ZPYYzRpZ4JCj42PF5ubOkEGYKSptWGhtW4sggHCxkrzjCNOQmvfamkgBoIHpps9-f3W8zdJyplOd2RB6Id8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0977608af.mp4?token=M3Mfr1YOblleYGMkPiuUUC2Ynf216kNnfRHxv23KKTbr-rXdZA4sBrw7WdDCk14Zin6_54GJXGohBsX1u_ts6SQaa7ScuacML8woKmxpXvKjSe4T_UCWOwaRy11mAlL1EFyQmHRv4GhJoLx_GCUmbkn0oYosq3xVsX5rrkBqaF3QNQpTSq_-j61vlpme_o3wYTsoDmGY-u2bvA3nZm9YzZj-PCo1w029QLsSALTdobVSXsa1iRe64GdRNMBTu89TfNc03azZMpxXs958O7Ntp7na_CxOoHTKDYDTVPnpeh5-OJBcEh3wimo7FwWEYnLj7ZjivLVObghHd7FVCquFJjn1u_tGoWELrm7DqChoyxVnUqShI-A5NZ3lUQ4kWBRLkmE29uPyhWJR69XFqqyClTvR4FqWXY2pMWI5sHujYKtM9pHOPtE72MRRSoEs2u29o82ynfdQVExuatoXYmGj9LApVNS4nl9d-VuOuIX1GkL3f2aXJD39ynHMynz4DHYGXV97vq1W1QwZxiK8PDPLWktO_zxqcT_GG1GoRIH1WQXwivbFWmKhvqaOu3XTWaWwakPZbz1FpyfhXptW5vQeyTw-ZPYYzRpZ4JCj42PF5ubOkEGYKSptWGhtW4sggHCxkrzjCNOQmvfamkgBoIHpps9-f3W8zdJyplOd2RB6Id8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بردسکنِ خراسان‌رضوی درقاب ۲۱۶ شب همراهی مردم
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/465882" target="_blank">📅 20:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465881">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fd25655c.mp4?token=BrBWhRqpeZTLnexygM2LdX0LfNrE9xI0YbUAsQ7D9PpZlj66m6rlPpPVmVtUH2RiFKxvAP9M4E1ksNZVdnnPPElT3-HH_sY9im7-XeHQvIR36PUzYbsD40WryjARL1CycGFUfNqB2nERdINE40c4ssoegSnkWgz-CnJz-53Cd6H2I4Xdze-z1y_PY6QYQdUuTqtSXNqO8W_I9xf7n_U0pCbCHukBB-Z_OO1Oh8YIY1WDqQFIfa1-qPn0ySLQYKmNFjx_7HnNu22PM0Hj0ROO4EKPYlRanXxB7FMyXtZ5rIQAMAFcnbHf65mGTse-kmWQLXexrNn8xy3xck3aHdaeaRQqBnrcuxs-vmHInJ8MU4MEbEgyLAgK4BMSfoHzkv0DWpYqMH1YJRJtXEvCNbyci22b8X24CLmskq0OM1rUFoFiMtKJdOG4JHxpBnCJ38dW9ZNpHmec0lq6aPjHiGVOD5_BdnX1iPVPxAk8i5D6w8BArbZJxQXM3mCEIQU8v0_en8-5QCSOxHqjipoG3ZUHA-skq9Ipr3EXdklq0qELB4zOV3CgInvPp97VKPZea2Oo-fIIUFTjK36iR-7BmXW47j-J0ujdpbUxjUBHTCfIfoIDUPlftzjpDnxlTMd-rqplUvgPf6x9prI0VPxXjdPXBbxwjkHGjdjpG6qVr64wr4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fd25655c.mp4?token=BrBWhRqpeZTLnexygM2LdX0LfNrE9xI0YbUAsQ7D9PpZlj66m6rlPpPVmVtUH2RiFKxvAP9M4E1ksNZVdnnPPElT3-HH_sY9im7-XeHQvIR36PUzYbsD40WryjARL1CycGFUfNqB2nERdINE40c4ssoegSnkWgz-CnJz-53Cd6H2I4Xdze-z1y_PY6QYQdUuTqtSXNqO8W_I9xf7n_U0pCbCHukBB-Z_OO1Oh8YIY1WDqQFIfa1-qPn0ySLQYKmNFjx_7HnNu22PM0Hj0ROO4EKPYlRanXxB7FMyXtZ5rIQAMAFcnbHf65mGTse-kmWQLXexrNn8xy3xck3aHdaeaRQqBnrcuxs-vmHInJ8MU4MEbEgyLAgK4BMSfoHzkv0DWpYqMH1YJRJtXEvCNbyci22b8X24CLmskq0OM1rUFoFiMtKJdOG4JHxpBnCJ38dW9ZNpHmec0lq6aPjHiGVOD5_BdnX1iPVPxAk8i5D6w8BArbZJxQXM3mCEIQU8v0_en8-5QCSOxHqjipoG3ZUHA-skq9Ipr3EXdklq0qELB4zOV3CgInvPp97VKPZea2Oo-fIIUFTjK36iR-7BmXW47j-J0ujdpbUxjUBHTCfIfoIDUPlftzjpDnxlTMd-rqplUvgPf6x9prI0VPxXjdPXBbxwjkHGjdjpG6qVr64wr4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله سیدمجتبی خامنه‌ای از نگاه مادر همسر شهید رهبر انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/465881" target="_blank">📅 20:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465880">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8jNij69LmafIjDa4rlVcUSpGQsaRevYv2Lqf5BmUtSpTSs4nYuIY65VWWrHysvV5sChKDc-ZmpFaM591GRJRJlDidQWaR-iuiEIlWaZ_6f0a-SGD_Z4DkCaOLo_0ndjYdSXE5pygeho9JEXYoT8VJh_Io9LviF01deTmSzkk_ucbzFjOsc1Pr4ePsmrqUbH45vT3kMDkIQfk46PBMwmA2b2C3wlpyhEzdZJq4XiHhqBHBD2dUJzXHhsxrl9TAWeZ753kNu2pPy8qg25fe26aFqw0DCk1pwKFJofXyJxIFqoitIt0yMOlRKxCUVCvjsN9oAilNloe7DxW6qFyA9gAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی انگلیس: یک نفتکش هنگام خروج از تنگهٔ هرمز بر اثر اصابت یک پرتابه ناشناس آسیب دید و دچار آتش‌سوزی شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/465880" target="_blank">📅 20:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465879">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec41398a0.mp4?token=f3cj0h-uANj7FcMy0Eh5VYScfnq15Yn_HyP6m4W8DZwwFrPX-tQn6n-MrGv1LLRmS5Mybx-hQMV6W16p6D_SGM2AOtcP61T1Fu8G-tVCOev7OrEdHhYjVaJNwNYAdfK9T_2n0R66laaDaQ1K_c_SlN5k2YTKOVxw9VupkyhgMzLrzVpjloiXkB5laq4Zl_Kf1wHgYZU0_d5EMciThHnYbzN_lZN9r-PqJZeDaJPip6boNYOOtI-CMfdCcF-cwHYXtGKArCfmWSyT1ihdXXcB_on-sUfLEcHgpQcpvwJ_oioYH3llQvTl109Rb4umJY11dGbxnKP72A7LWBMy_51QPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec41398a0.mp4?token=f3cj0h-uANj7FcMy0Eh5VYScfnq15Yn_HyP6m4W8DZwwFrPX-tQn6n-MrGv1LLRmS5Mybx-hQMV6W16p6D_SGM2AOtcP61T1Fu8G-tVCOev7OrEdHhYjVaJNwNYAdfK9T_2n0R66laaDaQ1K_c_SlN5k2YTKOVxw9VupkyhgMzLrzVpjloiXkB5laq4Zl_Kf1wHgYZU0_d5EMciThHnYbzN_lZN9r-PqJZeDaJPip6boNYOOtI-CMfdCcF-cwHYXtGKArCfmWSyT1ihdXXcB_on-sUfLEcHgpQcpvwJ_oioYH3llQvTl109Rb4umJY11dGbxnKP72A7LWBMy_51QPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله سیدمجتبی خامنه‌ای از نگاه مادر همسر شهید رهبر انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/465879" target="_blank">📅 20:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465876">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فلای دبی پروازها به تل‌آویو را تا اطلاع ثانوی متوقف کرد
🔹
فلای‌دبی که روزانه ۱۰ پرواز رفت‌وبرگشت بین دبی و تل‌آویو داشت، به‌دنبال حادثه پرواز جنجالی چهارشنبه گذشته پروازهایش را تا اطلاع ثانوی تعلیق کرد.
🔸
روز چهارشنبه ۳۰ سپتامبر، هواپیمای فلای‌دبی از دبی به مقصد تل‌آویو با ۱۷۴ سرنشین درحال پرواز بود که درپی درگیری میان خلبانان در کابین، مجبور به فرود اضطراری در فرودگاه تبوک عربستان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/465876" target="_blank">📅 19:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465875">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac579fbaa9.mp4?token=MukpIkbGvB_fdBa6o-vZlxHM18JkZtiVHgieQZ79c5rzkgbOK0HR6_VIzN2a2vbvvRCgXdLdF5FYx7tRC9A8PVTNeJujcHUmcBAUleWr2b3GtJoFvxSZ1XcMJyugLLqmNcKBJdieK3sM_j3XNQoYJc4MFPL5Qz2Y8TpcPpMfFIU_4pEKzgp6OZMe-KMjyh_5GicoxfkyfbQU5DtkWpDzgm33StZgzbCRKptES2DiEVw_7LRK0q22NL5d_-Dxc72Knwczbmwm-q8545a3-P0wA1L3WFKyQglCXdUtesWBJreK8fmJ3GMT8SF5Lg8QbY2hTmkuQy2KHHfnNJacxzfL6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac579fbaa9.mp4?token=MukpIkbGvB_fdBa6o-vZlxHM18JkZtiVHgieQZ79c5rzkgbOK0HR6_VIzN2a2vbvvRCgXdLdF5FYx7tRC9A8PVTNeJujcHUmcBAUleWr2b3GtJoFvxSZ1XcMJyugLLqmNcKBJdieK3sM_j3XNQoYJc4MFPL5Qz2Y8TpcPpMfFIU_4pEKzgp6OZMe-KMjyh_5GicoxfkyfbQU5DtkWpDzgm33StZgzbCRKptES2DiEVw_7LRK0q22NL5d_-Dxc72Knwczbmwm-q8545a3-P0wA1L3WFKyQglCXdUtesWBJreK8fmJ3GMT8SF5Lg8QbY2hTmkuQy2KHHfnNJacxzfL6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یامین‌پور از سفر به لبنان و نقطه صفر مرزی در سالگرد شهادت سید
حسن نصرالله
🔹
مردم مقاوم لبنان، مشتاقانه درباره حضور مردم مبعوث ایران در خیابان ها سوال می‌کنند.
🔹
ما حامل هدایای چفیه و انگشتر متبرک به دست و دعای امام سید مجتبی خامنه‌ای برای مردم لبنان بودیم.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/465875" target="_blank">📅 19:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465874">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">برقراری ۴۰ پرواز به صورت روزانه از ایران به نجف اشرف
🔹
خبرگزاری رسمی عراق به‌نقل از دفتر نخست‌وزیر این کشور گزارش داد که به شرکت‌های هواپیمایی ایرانی به‌جز شرکت ماهان اجازه‌داده‌شده روزانه ۴۰ پرواز رفت‌وبرگشت از ایران به نجف و بالعکس انجام دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/465874" target="_blank">📅 19:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465873">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26710743e8.mp4?token=ZnSRmaR_ZyU0guDMc_a01iyNBJx9i0WeaLay8z8ax_YHiQsXWDs6JtmK92FBStN-GeABsBHrcFujxFByJLX_HwSlPQqs7YWkgw50AurK5qC9iEX3vevpTZIsLdsanU47TWgKE_EWfoZv9KiRZe2I5uf5KaemBqNtP_2gWi1cyG21jeeVMxGtJlVieh1Ow4x6fzygceDVRQJ1sqppGCYCkCd8nn5OzwHzxAgBRMtPwoCgQcY-2z_ruNwket_PZF0wJtPAkTxpgEoj1vh2xZOgzoqGPJ-DbNbYFYF0SKO7JJ5xDy6D_k18b4DverYRbaRfNOzPKc42TXiRAwOKTb5jtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26710743e8.mp4?token=ZnSRmaR_ZyU0guDMc_a01iyNBJx9i0WeaLay8z8ax_YHiQsXWDs6JtmK92FBStN-GeABsBHrcFujxFByJLX_HwSlPQqs7YWkgw50AurK5qC9iEX3vevpTZIsLdsanU47TWgKE_EWfoZv9KiRZe2I5uf5KaemBqNtP_2gWi1cyG21jeeVMxGtJlVieh1Ow4x6fzygceDVRQJ1sqppGCYCkCd8nn5OzwHzxAgBRMtPwoCgQcY-2z_ruNwket_PZF0wJtPAkTxpgEoj1vh2xZOgzoqGPJ-DbNbYFYF0SKO7JJ5xDy6D_k18b4DverYRbaRfNOzPKc42TXiRAwOKTb5jtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پدر شهید زهرا محمدی گلپایگانی در رواق دارالذکر و اقامهٔ اذان برای نوزاد یکی از زائران
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/465873" target="_blank">📅 19:20 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
