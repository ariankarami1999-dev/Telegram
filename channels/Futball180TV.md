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
<img src="https://cdn5.telesco.pe/file/XlSyKenPPXmNxR2dMCPJzt-Efpbs88W-pHjrRzoHx7BHOklkPwBAwUzYcfW5OiUHuOa_ELyxHzadS94V3TbB9VQZV761JlUaXZqUSWXqtAR72rCIpBkfLQoFVTr_a_uB3d9wrZYz-VpT2OMrtsvLYnTphAAj0-fPHKJ_QOublKqsL3vvhjKnTp9K08u0ACbPhXVS5CLNkxlh8FT2wenB1JV3cr2K3uV0uqv5SFsaCEchBVMnV2HoB5MDFTOu1B7_XeXWlFAUCFinVwQrSVgM6UJpbq9dslaZPaDCrajWIzNyUejQmg_gyeI9yKroKSEp9lA4CdewoP7iYo0GPCXKXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 671K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 01:58:36</div>
<hr>

<div class="tg-post" id="msg-94306">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a94bfbfc0f.mp4?token=L0jtL0tXazvoCxKeXzYosfc6_kYOUm7D4q2AaWXrc4BMzXXj3I37-whr80w5sEAqJ0wJiBUJBpoxXpR3W5ENXe1Tahhz8cwmHlxZlXc7wVZ6-0bHvN1IuHpSwOqxPCBJvbVoG651ilQUUgKprm7PuPcoiiJWRG0aJxilZePRi6VfBs8ATaLfhmjUJoeakMEtlYqPw51eVZVgHHpwUmoOwY230P1253Ghhj0L1YigLsNVMNYogEGeb4m-_7Z_9oVrlLWmUHq64MO4u5y2G0f_uzLE3_rRq32H70BF_bjviDgJ4O3dFHku_m6rviubLqFyx3caxL9ic3I82R5taPPFqwtTU77Oq3K99trZMpEAboTYuEGItdKko6w4ODDFeMYB8ljLTJadbmR8i5T06rgTT8GCjtqOveVrHRFjTLNdFQTsCLFbI2WUTapvcQnHZtLQ7n4iL6KDB5SgoSkIi63s_BvH78k_e1V8qtRgTnkko6jqm4A1K5iDg6k4M_CsT3bYfylQpBkXobh1xOEztASb3j6-MHINHDhjFnclTGV7IhiSdXQoN5T3bS3mtXiROtimewsa9Rv0PcysVhcRk7a013oq3TEz_U89VzBY6d0HztLzZAGD4a1sIoe-jjG-0hgPNSwOmM6eaS6WsUr7q-qKWYq7q9aejiZUASSPe0sPuzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a94bfbfc0f.mp4?token=L0jtL0tXazvoCxKeXzYosfc6_kYOUm7D4q2AaWXrc4BMzXXj3I37-whr80w5sEAqJ0wJiBUJBpoxXpR3W5ENXe1Tahhz8cwmHlxZlXc7wVZ6-0bHvN1IuHpSwOqxPCBJvbVoG651ilQUUgKprm7PuPcoiiJWRG0aJxilZePRi6VfBs8ATaLfhmjUJoeakMEtlYqPw51eVZVgHHpwUmoOwY230P1253Ghhj0L1YigLsNVMNYogEGeb4m-_7Z_9oVrlLWmUHq64MO4u5y2G0f_uzLE3_rRq32H70BF_bjviDgJ4O3dFHku_m6rviubLqFyx3caxL9ic3I82R5taPPFqwtTU77Oq3K99trZMpEAboTYuEGItdKko6w4ODDFeMYB8ljLTJadbmR8i5T06rgTT8GCjtqOveVrHRFjTLNdFQTsCLFbI2WUTapvcQnHZtLQ7n4iL6KDB5SgoSkIi63s_BvH78k_e1V8qtRgTnkko6jqm4A1K5iDg6k4M_CsT3bYfylQpBkXobh1xOEztASb3j6-MHINHDhjFnclTGV7IhiSdXQoN5T3bS3mtXiROtimewsa9Rv0PcysVhcRk7a013oq3TEz_U89VzBY6d0HztLzZAGD4a1sIoe-jjG-0hgPNSwOmM6eaS6WsUr7q-qKWYq7q9aejiZUASSPe0sPuzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌اول کانادا به قطر توسط لارین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/94306" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94305">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاناداااااا</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/94305" target="_blank">📅 01:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94304">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گگگگلگگلگلگل</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/94304" target="_blank">📅 01:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94303">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کم کم بریم سراغ بازییییی</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/94303" target="_blank">📅 01:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94302">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prq3VHHwgiSb4wdDECryJyNcUwIFw5zGSQXX1sGrSGHfEA5aAkQ-j8z47PTS71Vutj97Vcx_som90S_g475vWD8G1YOHjn6eci49pkJm7ecFVR85Y5x5u8gd1BkPQJ-SeYXMjcpXucf6cRZcMxwn9RkO-9S5uVTRZesf7QFj570-nqt1XVIKK7ohANE7wFrTI8SM8Ycs0XdtNXWZz_TgRkKYQXY0mFjpyN_4j8bqzEUfufcVUh5Eo_Iqjz8iYUVukisGmyMOauIXfB6ItQLxOoofRl1mDFsR5BWDcJPoyw-SkVyJnRLGk3_DqbDZj7UVHnzXL8weaYiUCVYvVuIArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
🇪🇸
گاوی: انتقادات نسبت به من همیشه هست اما بهشون توجهی ندارم. اسپانیا واقعی رو از بازی بعدی خواهید دید. هدف ما فقط قهرمانیه و برای رسیدن بهش حاضرم جانفدا بشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/94302" target="_blank">📅 01:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCUi2BIT8KaOWH7XECOd79c7An22B1aXvKfabS7zzU0FFyVqsthqxmq4lFpt1JVvO17JUrbo814JyMXMnRupE3SEoFjgB5eaVgafuGCpJyXNgugdwGgqsMLIr03UXGB-5rZf-4ypKOi1gXYu2MWHM9u7swkkA8HsFL_S3gjnORyUiebPL-6j5FuEi8xwXqKRDXZ8Hw91y6TwNyNqygB4-X9VyMNJ3E1Ti_muJwvJrC0mswnNGd6f6fGS4RuNlTuP8pbtj2GSzfqA6mSfIUiARCdIVzwoi2L_zeE1dUoFWn0ROPq-QAQNF7CmNS9PRV40j_50HF_gZNgzC28uIDaPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🎙
دنی‌اولمو درباره انتقال کوکوریا به رئال: فکر میکردم به بارسلونا بیاد چون قلبا طرفدار تیم بود اما حالا که خیانت کرده باید کونشو سفت بچسپه چون فکر میکنم لامین یامال راحتش نمیذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/94299" target="_blank">📅 00:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq290afVd9cVgr34Z56kOUR9ujS9QpORZDJNb1ZUgcmOmMN1oRgwjRBDawgvkwlGmxCSx7Ju64p8cjvOObEftdDSUN_3LTvXyEdYfn4DE026MgeDcdTFST3u9svo7jQRzdjhXn3VZv4PPvNF-0_BLwb95WXR8e8cZuYVNFQGe5VE9ldZNqTH-VBGURgDUdaYlMNUcZhjYa1Vx-Yjl2PQeq-x3KYdCugLUVGkgRbXwnfyge-1bs8prI2sayZLvg21pVSKNP7SWjNVnNNA2BEI9iJqUdZnA9tW2ZAvPnkNel3UPgCXMAmX_cVrHemirXTdzhLA1cq73dL0FPfhXLtyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آرشیو VAR:
پنالتی سوئیس به اشتباه اعلام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/94298" target="_blank">📅 00:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O41IpBm3bD7gsLjuEkwhzR6qLsY-YBTEQA4dX_y7jhmLWV-GdRR4C66dlua4eZyr3kixLzyQafDgeRB_OaKvSGffZVOs92Q78SXs114_qXPtsxikoeIhQGhTR76rMqAHk4bo17aNYRtCFe56eVaDOn8jf_PubLrcYgYWXRkaAATltJRSFg7gPsEGHPe49ObEwDEgIgWXoaSooqWhTzVYvjQEl3lNIP73jTOCMbrUv-KJLJ7Q8wfw5-ETV6L6A01AqfOFBPX7lq4QgrJq20q0FyJlEu5vGT6M2mapT7KE20lLT1MQu9dZ4S_FyNZaWy2_haSHXwR9TY3WRnhGKpo1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
#فکت
؛ یوهان مانزامبی (۲۰ سال و ۲۴۷ روز) جوان‌ترین بازیکن تاریخ جام جهانی است که به عنوان بازیکن تعویضی وارد زمین شده و در یک بازی دو گل زده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/94297" target="_blank">📅 00:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/94296" target="_blank">📅 00:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BlFoWqAdseE4yHapPRADZ1Uf_OTCoX_1UDLAGe0o4QiT8vehnevOt-_8Um5JG65VRtKLV6B2c_048eGhIIk0bFfmsI2AjRKYkElIU6-J8QCv3dNTE58y09zmkyP9Qc016YoydoqbFfBXHbq0Sn-YzCMloLkGxSXU4xmNsb_FsY52jK5hPODy9FYxgBmU2PtxsVBpQp7-oGarGJ8hgCnwAzskRmNX5DHbTUDhUunomkD6hmRLQLMJgdnBMrdzbf-l83yb_W_dKSqQQ-q8VoyNFj0QHAufTifFik9QbkFRbEqXyq4M-kWLQkcYEvnIybIOm_OPMBc7hZMvPpm_FN2q-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/94295" target="_blank">📅 00:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJ4FvjB7lusabPzCk24bOGEaWB8dIKBJKntj6PXEUztdgoByv3kn8DTnv_-bS1fIKXDg6evMUS5r_4Ze53YyLCCtSj5DSkN67BuoojZ4H7BVdjP-fModHZHxwpHvc6S2ORuWm_eccbm2wNKNwIA1BRWwTLY9iFz7IFtC7I63GtJqxSMLQvTdepRHw3OzbK5Iyh0dpByfs-NGKQZezSlxR7xSNGmpzydYHzM5gSOSMrxeqRoGvm_ZdRAOyjO0lccEdfWxL6S5kYEVkvMQ6OaweaFFH6U1IyIut7AOg67G0YxYYAQNZO-h2kMPDo-W7R-c54pi2hnCMuTO3dzFLTD5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تا اینجا جام جهانی 4 کارت قرمز داشتیم، به اندازه کل جام جهانی قبلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/94294" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyl5ihN0EAhXsPyIjyoHFLAlFHvnK9MoUBU_2Uw05xkSHZfb2mCuJ4LSOEycepoub46JMFA32SdOpsYUw2DIeKVI9UmS8kBm_Ae4aaLBBoI5DiUFE_GfO5ubmm_QxU309R0N64q6JrlL7yi5rDiF6EiyXo8J9fZ1AAO4sibRxhqf6AE5McZoifDdgs8HYeMsxp2E_7DP-q8jhZyijvIG3Dv9LR9hRBaLhqGyI50TTdHgdsjpf8fvDIqlEbTSz6X_rABIj4f9N-l5ADdJluPkobuj2GVAsexVB9mOTubc8x7UDZYRVajmNvNMDO0JMtaSOTNMugB2aqZtxgHwZgtYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگه تا دقیقه 74 بازیو نمیدیدین چیزیو از دست نمیدادین ولی از 74 به بعد:
◀️
دقیقه 74 |
🇨🇭
گل اول سوئیس
◀️
دقیقه 80 |
🇧🇦
کارت قرمز برای بوسنی
◀️
دقیقه 84 |
🇨🇭
گل دوم سوئیس
◀️
دقیقه 90 |
🇨🇭
گل سوم سوئیس
◀️
دقیقه 93 |
🇧🇦
گل اول بوسنی
◀️
دقیقه 97 |
🇨🇭
گل چهارم سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94293" target="_blank">📅 00:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8sGGO7xq207MQoim977vkrtkkIelnLWBLC61StsKy6E1q6ubk4nwrgEEGIjDDfsytlFegva5GcdcjtZsNrY-JX6Ms3Em0uzIimFutR6-N7iKyB0KBc3mFhdTcWtfwdfNvIHWCBYuOm3IFC4zt5b5NbnViw3siDsYGZooCNij09Mb045ozRwk3MwHgbjW-tjYv1N5q9G9Bin6OcD2LqeXLMRNOgCq2fyLN8sG3ttMODYMGTL7z6_RfNUXb3veNnpg4gQ8toM00b0kmvarap0CwprdKJx7Sddj4HrxmoZrcg7vwOMimigyT4G5kIn24EGgMT_dR-AOB4liJ-WaJgnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یوهان مانزامبی به عنوان بهترین بازیکن دیدار سوئیس و بوسنی انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/94292" target="_blank">📅 00:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlSfONj_LBsmYn6DPWEV6bLH_7LjeeMUqgcp5zdqZOQo1TFcmOAiCvqCZDLTA8OtED7ZLg-ZviV0WsZZvKGoFYGY-V5CxAOGbIvbH3FPYOcPwzC29YHh_oOUAMEENRTvaJSJJslyXxadHrrlNPBXjCiPBXUcGAex1v7pcEsIUh46KxgV4nnNGBBC-pSLBfIH_WgB4hLGe-sbk4-sWMmdPPT122l-iz66mn_8spJLDobknHWz8TvDjqoDiQKZP0m2KQ-9ZiX95b616fhiTd2J7GdsBkUehWLLLPTnB46fP_vlQa0QnVNThseR8nmyNbALfF9rYF6cB6LK43JXJloTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇭
📊
سوئیس با کسب ۴ امتیاز، طبق آمار شانس ۹۹.۸۱ درصدی برای صعود به مرحله بعد داره و عملاً اولین تیمی محسوب میشه که یک قدم تا صعود فاصله داره. جالبه بدونید در این دوره از جام جهانی، ۳ امتیاز حدود ۶۶.۷٪ شانس صعود به تیم‌ها میده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/94291" target="_blank">📅 00:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E64l8I7htdMJ1oA27hbIe9wN4XegMxRD6FkCorRqddYUtQMReSaun8Mp4OYZDcA2M2Fr3PF_1J833TMx7JqDHVXDNUJGChV6ZvTD5u0CUKZB00wwyztwYsjtE01IXx3Iw0MRPSuOpDgkMhVRP1UGMK5I6XTt1eYABEX3Qn_OYtLfY0Io2alZMrSEY5o-8zYC4QYi0PWvyAhHDAZoWkHAbFYhUUjJ1HxB4Ls4ZP8iq764ZproJN6wGtmysdO7Q6Ut2_w_jIx6Hxm5pjtMlMuvAU_av7cNTpmDqYsjwnwN1ALQ2h62-S9qwhHpdEh0_coAOaMQbiDh_FMVSeDQ8t8Now.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آمار نهایی بازی سوئیس و بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/94290" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY4QP3uA_4_GSbE5HAbaXxoCxjgkOsuVogRKKGaR3giH32DVg3lgQfM6M6mkRiD2e9xeg18ksq5OqpjryCvX0Lf8kzHipg7Ll6CfuqxNdzFTI2O5WczpONuDl0YHW03o1MVmUGwTaQA7qwbzvaTNFJ-FD03XipTcZ0phb3RpEwBOCt4Jd-vpX8ghixh4wTSWHyC7mq2SKxFaNh65aDPvrP4FZzCWZ58dzUmh5SRhwVYjktVGgYS_s_qO9IjJPFroJs5evi8xy9jsAYmcY11S8tvTHjU4FciSJ6HC9csBn-fPoSKUfAgzdvf8zyaa6URyhDIH6BnWAG7hsJp46A7wIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|سه امتیاز ارزشمند در جیب سوئیسی ها در شب گلباران بوسنی.
🇨🇭
سوئیس
😀
-
😃
بوسنی
🇧🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94289" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eca495a4d2.mp4?token=jdkdGLpQWnJK3IHJpPWLzgm5-mTdHpwEBY5ASRcdP12iwFDRhYaL75UOh5sZvmmRLNgA0thd9jfGR3PDcjNR9ksASHc_LMwxk-4_9OrKW7z-mxj99VK9nn7Bfdb9BO3n4hN-HHa77gytNXFJDuzvu9ot2Pix9J3DUNWIJ-JVyquwNtIzSGGOhyhMKdp0nA3GNNRZu313rud40yaizGPmSaOMj9-y2xPqND4pCG8I_HbaF7anUxkS5FwgjhiKGbHZ7KUJhIBEfCVLmoK8HfSW5-EpsMW5HYMDhZWpSO2WigZiKIYKksTRFTQGBd3Kpj0F8DR8whGP6MnemoDt6XrWkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eca495a4d2.mp4?token=jdkdGLpQWnJK3IHJpPWLzgm5-mTdHpwEBY5ASRcdP12iwFDRhYaL75UOh5sZvmmRLNgA0thd9jfGR3PDcjNR9ksASHc_LMwxk-4_9OrKW7z-mxj99VK9nn7Bfdb9BO3n4hN-HHa77gytNXFJDuzvu9ot2Pix9J3DUNWIJ-JVyquwNtIzSGGOhyhMKdp0nA3GNNRZu313rud40yaizGPmSaOMj9-y2xPqND4pCG8I_HbaF7anUxkS5FwgjhiKGbHZ7KUJhIBEfCVLmoK8HfSW5-EpsMW5HYMDhZWpSO2WigZiKIYKksTRFTQGBd3Kpj0F8DR8whGP6MnemoDt6XrWkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم سوئیس توسط ژاکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/94288" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94286">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سوئیس گل چهارم رو زد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/94286" target="_blank">📅 00:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94285">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پنالتی برای سوئیس</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94285" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94284">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01debfe500.mp4?token=SuPpQDrGTp2vIOwSRGKXlcEhB9oYfaSgKvKmefc994pbZDfyWDX2hBdG51ff1dl6HnLT6dQSFSpg-2mXVLSJpABGb6lSoRJnSlSA6S0p5-uA-y3GDYgsrrQwXq1ZKDwkEIQ2URN9Ba5WGl-slr_OIf2JYNIX9e72XkVN7yrOF7OywTbDZLSvn4IrIef7X3gJIwfZXfIR9r0ggj5HFJwwUP5dhENixmgKwPM34Im86LCykiEZeUJEOisYTetn6LCQLoHZ6pViNigBLHg0HCZ3L463QZAacQOLcpyIj4WvPsu054REAKuetHC4h9o83qOEg5OAdSuAEqT9o2Wcd6jrZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01debfe500.mp4?token=SuPpQDrGTp2vIOwSRGKXlcEhB9oYfaSgKvKmefc994pbZDfyWDX2hBdG51ff1dl6HnLT6dQSFSpg-2mXVLSJpABGb6lSoRJnSlSA6S0p5-uA-y3GDYgsrrQwXq1ZKDwkEIQ2URN9Ba5WGl-slr_OIf2JYNIX9e72XkVN7yrOF7OywTbDZLSvn4IrIef7X3gJIwfZXfIR9r0ggj5HFJwwUP5dhENixmgKwPM34Im86LCykiEZeUJEOisYTetn6LCQLoHZ6pViNigBLHg0HCZ3L463QZAacQOLcpyIj4WvPsu054REAKuetHC4h9o83qOEg5OAdSuAEqT9o2Wcd6jrZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇦
سوپرگل یار تعویضی بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94284" target="_blank">📅 00:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94283">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلللللللللللل اول بوسنی</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94283" target="_blank">📅 00:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94282">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcd1a5f6db.mp4?token=nL_ARD_MB34Uj6Yg98BNWJhE5mURkCLq5LRb2A2lp4CO6YFC6s_RB0jQ7OsBSHT7Ocu7MmNnsYP3fuOd77MXEjygSCMPQXY1nkoYY-7xeqrUYpkfNjCK27DK1ZuxwvtWICjHB2mTQjIn_keKm3B9sH7v63xoM4SJNNPMUTY5ImVkTngwiWzoJ2AItpIsrxf4gvmrRp-kOceKwg4KTzRYrJu0FkYxTbxPGSzIDA6WmKpLQTONWlzDy8-xyYzOYiA96vcJFzYm8jppWgBsEctvKXTM4JPCdKlvXtwZJxIr_qz7f2BT-nTcvYZ4joCBsDzz41bENOn0e9L37kfDq31yew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcd1a5f6db.mp4?token=nL_ARD_MB34Uj6Yg98BNWJhE5mURkCLq5LRb2A2lp4CO6YFC6s_RB0jQ7OsBSHT7Ocu7MmNnsYP3fuOd77MXEjygSCMPQXY1nkoYY-7xeqrUYpkfNjCK27DK1ZuxwvtWICjHB2mTQjIn_keKm3B9sH7v63xoM4SJNNPMUTY5ImVkTngwiWzoJ2AItpIsrxf4gvmrRp-kOceKwg4KTzRYrJu0FkYxTbxPGSzIDA6WmKpLQTONWlzDy8-xyYzOYiA96vcJFzYm8jppWgBsEctvKXTM4JPCdKlvXtwZJxIr_qz7f2BT-nTcvYZ4joCBsDzz41bENOn0e9L37kfDq31yew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل سوم سوئیس به بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94282" target="_blank">📅 00:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مانزامبی دبل کرد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94281" target="_blank">📅 00:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سوئیس گل سوم هم زددد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94280" target="_blank">📅 00:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2dc23848e2.mp4?token=OOB8hg_3mcn7E1PKL11QU_s-O9SR41bdevbHVStJ5ae2DUhOwyaCLzz19UP6u9n7ENtabv9OSIeTfjMcmTv0gZ5CkKhypF1YkwQA-b8yW3EIKXZmZwlDxKEBzuu-uY06bUw_nxg7Z-jZPyu-xz4PqRh8nxb_8jYceBxJTTj7g4CsMaoXaSy41jlIjb73gB4sAawqDm1TZse8aVySN-b--L33ak1_6bEOu0OF81L-jsKK4VzUlRfaAh7bdEJvDro0q-kG5icbaI-yqCUjCFxB28xmHPDwEK0yJxkRa-brYSdZmQ4pzALR5Nx2u1a6g5cmfU0NAYksShVLTAe34PaTTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2dc23848e2.mp4?token=OOB8hg_3mcn7E1PKL11QU_s-O9SR41bdevbHVStJ5ae2DUhOwyaCLzz19UP6u9n7ENtabv9OSIeTfjMcmTv0gZ5CkKhypF1YkwQA-b8yW3EIKXZmZwlDxKEBzuu-uY06bUw_nxg7Z-jZPyu-xz4PqRh8nxb_8jYceBxJTTj7g4CsMaoXaSy41jlIjb73gB4sAawqDm1TZse8aVySN-b--L33ak1_6bEOu0OF81L-jsKK4VzUlRfaAh7bdEJvDro0q-kG5icbaI-yqCUjCFxB28xmHPDwEK0yJxkRa-brYSdZmQ4pzALR5Nx2u1a6g5cmfU0NAYksShVLTAe34PaTTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل دوم سوئیس به بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/94279" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سوئیس دومی رو زددد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/94278" target="_blank">📅 00:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/94277" target="_blank">📅 00:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بوسنی ده نفره شد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/94276" target="_blank">📅 00:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94274">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qN04hlktaHr2PE_dHSZVVK-D_wG49bRa3sc-lMwwOEH502gbn4tHgv6IzdK92AQikOx8CUiSmhqJfdxSiPhvWl0f6FsMPLktNPJ4S6fJ3tVtbgsjXPuhC-BDsrFrBGClsNJEbjr2rgmrCkBJ8RFvazevf_fRe--hsK1T_7kDPNpd0eaE1P7DEt9hDi3ivw5VlyhbTxcPO_9xK4lnw3x3qrB5NNA7RPB_hYm4iSY4d-ui0V2Ix5Gihpfn5YE6KbTQJBXU7wira2S2lnBEil9ziH1AvTeJcVwX6gk9zZR-IRXwYZPgTk35y3jGUiJvknBC-BHcEhtPQEwdOFqSN6B-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmWPhbee10rfD_azgmkLTWsFueaWaA5_NkNC1Q3yfDj7uV98JJlQIKlsnq-vxOd_4SSoQcpVvr9ml1GX4ii7IHWm4PUKAffh04K5mghKSc9_EX0qoXWOg8qZSjik34XFjIqW5qCWZE_vJyO_A6eMom_k4HITPpuPew2RtQMjKtp_Ya4_ApEw0d52ECX-BMWR1uk8VPteL9JagXRU8rTCJcj8AvL4tUdEwAb7UIwfTLdeQz7zvAILBg6pxo6cygBMLzm_xf2YQ_5pqTUax5w-j9iB0ov5-OVC0QkY9BSKsZw5n0lWq1UQ2zk3cW9c4l-rBd7DyFDYfvB1JP-01VGWdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇶🇦
🇨🇦
ترکیب رسمی قطر و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/94274" target="_blank">📅 00:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04d0160117.mp4?token=Xtqx483wg4SyW48Y7tzoQRz0KiD4Spd8NrrFDrMI0yK1L93AIaLMq6eZtgM-zBhUHYOE7BmyYR9cX_F4JnxzR_MOnSPC7k2Y67XXOBIiQT3HFgaSIxkMfB6AVfY5SWfAzWPnFe1jkG6uVE2sPwuS4RLBJ4mxUUL2EoU5CtnglsBN87pvbH926JBfNRQepFSoDb6fNKh9VFqny3mww-8AeZDYZBddeSLpPj1-CzWzipQW6FXI_hQx0vgOksnKbpfdELNf2qQb7pJH3ngX-SwfQ23rT36L6DXv8dUN5EXSErU2lPcu2TXwOSNpCoLGmq4sxiAjFOjkXBaHxJYSq28aIbybFS83GCT7PJFR1zax8B-WqoK1tLTqnKs2DGqC5qw_vn14DL_rqx3NbtdZVnNNT3nRIUkJ6D0RpLj1HmOvhKFXoyK2tmT9oAWIjlM8yij4Tu05nmnBCVA2zEcax0XXCGdYLVkWJ3Zeh7hHLEHXuZdS5a65bwpyxGUK-sCBHW7sYsqlZYMv4suaAORQNUSO-Q5yA4NHZ7cTLvXrtL9vO3ktJFyxuDArA5janprMWExA7ZW1HsEPME7AQyQL9v2WQPTMrgrV5YYraTYTglKKWNdqfZ7I2uPElZ7qdYNn9LBpTb5SuEYoNJ01ttk2op_W94Bqo0xFgScWoNyVg07ORU4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04d0160117.mp4?token=Xtqx483wg4SyW48Y7tzoQRz0KiD4Spd8NrrFDrMI0yK1L93AIaLMq6eZtgM-zBhUHYOE7BmyYR9cX_F4JnxzR_MOnSPC7k2Y67XXOBIiQT3HFgaSIxkMfB6AVfY5SWfAzWPnFe1jkG6uVE2sPwuS4RLBJ4mxUUL2EoU5CtnglsBN87pvbH926JBfNRQepFSoDb6fNKh9VFqny3mww-8AeZDYZBddeSLpPj1-CzWzipQW6FXI_hQx0vgOksnKbpfdELNf2qQb7pJH3ngX-SwfQ23rT36L6DXv8dUN5EXSErU2lPcu2TXwOSNpCoLGmq4sxiAjFOjkXBaHxJYSq28aIbybFS83GCT7PJFR1zax8B-WqoK1tLTqnKs2DGqC5qw_vn14DL_rqx3NbtdZVnNNT3nRIUkJ6D0RpLj1HmOvhKFXoyK2tmT9oAWIjlM8yij4Tu05nmnBCVA2zEcax0XXCGdYLVkWJ3Zeh7hHLEHXuZdS5a65bwpyxGUK-sCBHW7sYsqlZYMv4suaAORQNUSO-Q5yA4NHZ7cTLvXrtL9vO3ktJFyxuDArA5janprMWExA7ZW1HsEPME7AQyQL9v2WQPTMrgrV5YYraTYTglKKWNdqfZ7I2uPElZ7qdYNn9LBpTb5SuEYoNJ01ttk2op_W94Bqo0xFgScWoNyVg07ORU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل اول سوئیس به بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/94273" target="_blank">📅 00:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سوئیس گل اول رو زد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94272" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94271" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtNPydC9ktX_UbGw9GNdD58jVNael1kczjTRY1szXv2QLUZGpcwWhaf8EHvE8Mmo0hqLROqe_zZ8gAZ5XYvcSoyI57ILhoXemFuH2zxkwkLpZKsRKOOnZ_H99m9F_njoFsK0fYOfGSpPEG0GFe615xOEdDNQMo_qbZnyalPKFa0P-8D-at_mYelYv1lmgtC2xFymPXAczvWR_CPIggA9Km99HXqewfgm3Q5oF6JH6hZqR5lbMyuuzYTfqJX-F6GaeUN7w6EVbj-qDVsVYyPbxr7hBmSVhwjqB7JDXQ0iKkxnTwRNfd0O-ozNZqk2xf7ClDb03VfO9BGGc0cQOdgUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این گلر کصخل کیپ‌ورد 1.3 میلیون فالوور میخواد تا به تعداد فالوورای نویر که 20 ساله داره کون خودشو تو فوتبال پاره میکنه برسه
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/94270" target="_blank">📅 00:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkI9r8UQlWPSp5lRDSo343iffYCI7Fw1zKdsOrjMDy4kEtqBqMJ4x_A6TU6OLXNy5UHzW8YDdyC7cFRuBzUx7kTfgTQ7Uxev0xh9rZA8gsC41Mv_QENpRZaKDWNSDeZRU0nZXMS8KoycoMTez2EFn-juJAStXMAocLb6q3tKJXXNivuxzo8T6N_ZLe8b-q2XHq-FO1XiaLqBWkAbOxLVCx7m77K6rclfxaDkitVTUvTY7DAdlaTFxuOJfh_QCVU0m-qMMg32LmaXf8wereSh2E75qNLgS0qRSnotEibIGoFx9QSjiBD-ucl2hwCLcPZBs1UAAggT1u5Ha3_VpLzfTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇿🇦
خوشحالی بعد گل بازیکنای آفریقا به سبک رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/94269" target="_blank">📅 00:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94268">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqYyJRSMnIcK5AUluAGN3-y_mMuzrxOONn_2owy7QuhmDJ0NIpbJyfTc3jc_ZuekBx10bJtQiOPDGvoi_-pBe-tQ3gheCObII59cs8JKXAFvkXyi7eC-WQ-g4N7oOeWOZFhpcoYzBbAVyU0SEACFPc2ic-Mxgiswb4hqV_jWZXn4obcUimOzHw_RSb708QNGdIzsdPy6PP3BHH2UBjicXRqRlkPYt3GygWTY_WJCQ-NV-tVVz3BBdSnHCGXOI3m8ZOi6YYt3uK5ebT6U1iJhmJFk6PJwCRW2C4yhQKmeBq_xwyaVGuK_VmO0sMjkXV6UFBEEoeiY6SXZxBj09EsaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جیکوبز:
انزو فرناندز فقط به یک باشگاه فکر می‌کنه و اونم رئال مادریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94268" target="_blank">📅 23:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بازی سوئیس و بوسنی چنگی به دل نمیزنه</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/94267" target="_blank">📅 23:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94266">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a9674b76.mp4?token=dteM39J1eSA_zUGR-x1UiZOL0iCIwsb4vqpmIDlAqB8veL2Do3hri_yqx7FqTsI06wbu_7wwbRpFkOZ2En9qHoWDc1zmPffyKY6vX7qC_-ypn4orkO-LrO9lxGDAUp2uQl6b9U9fYotBLwX_6Xo5YBR3xfLk31sVTWESleK7UKP_Nf0efowgKVSNQLPb1--dtaAPXk1HcYwgPjouz1-PJzAaxLPbk7mlDmG9pUWk-1ISTu9OKWiu3HYDb0245Qo__H7y3PeS3t0Gp2TR9Ck2F-SdHDOwOL1vJ-wT7ku46cO6CiIJ907NDILBwXNMPSRCWqQ_0228FIl1RtmdrWAYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a9674b76.mp4?token=dteM39J1eSA_zUGR-x1UiZOL0iCIwsb4vqpmIDlAqB8veL2Do3hri_yqx7FqTsI06wbu_7wwbRpFkOZ2En9qHoWDc1zmPffyKY6vX7qC_-ypn4orkO-LrO9lxGDAUp2uQl6b9U9fYotBLwX_6Xo5YBR3xfLk31sVTWESleK7UKP_Nf0efowgKVSNQLPb1--dtaAPXk1HcYwgPjouz1-PJzAaxLPbk7mlDmG9pUWk-1ISTu9OKWiu3HYDb0245Qo__H7y3PeS3t0Gp2TR9Ck2F-SdHDOwOL1vJ-wT7ku46cO6CiIJ907NDILBwXNMPSRCWqQ_0228FIl1RtmdrWAYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیمار وقتی آنجلوتی‌ گفت بره انفرادی تمرین کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94266" target="_blank">📅 23:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWRxWgj2pfrDkT5mPtSp224gPZWGMBeKTE-exKaQ9CpfFJD6cP5jMkMfTGDp7Ysg4-OgNL-Fbeay_5xIMFcRqN8wDkkAo56-xb_M0lZaZ4PE99gvcfbUc7Umfb2ywhkJCnXrkzVCNNLhhAj0CTeir_Tb9NznKlu5q8vXXcJdsrX73mP_XmiT4GtMIRbjWnipn3EsyaiM9yJjJ-yajSlswvQlaLAE1gt19a30gP_JfkQckZhqu3Zlt_nuIrAGDh9iq2YkFhwc7xcyTfsVB9akRHk4eoMAmUDlPTGF8XVrfPSrwfcMdqgGuRpJz6RPSJ0qd7oFyahJFt_Vgslir662bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
فعلا خبر پیوستن انزو فرناندز به رئال فیکه و باور نکنید، خودم روزهای آینده دربارش صحبت میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/94265" target="_blank">📅 23:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94264">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdOj6fA38SeMHnVPp9b8lncrdWn7ioUjprbvt1ZwDptzVHGyIavWlk7lMqNm8zB3_XMCPrDCuxOzgVtraCyTsUUtFdAErZDJalFHRtYFZbc-KTqYcu6EmYFfIkQRY1zVb2bzKwaNnYMv1rJPuGv_WbG17gAagDqq2yWkCbleSCgEnK529ynNwzNFYld9S6kOuBOXThvszl9pS7SCL-NZICvrgriYLJ7V0kQtlZURs64DoCwlbh_eTWu3kroWweL13R4c_JyKIQ4p-IKIXUcbtxljrQnfKjmuDqr19X8HOhsWfRn7haz1z8psnnByeDgNKHjzZa6mjHp1elfwTTd1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا پروتکل جام جهانی را تغییر داد و به درخواست توماس توخل، به عکاسان اجازه داده نمی‌شود که هنگام سرود ملی جلوی مربیان و کادر فنی آن‌ها بایستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94264" target="_blank">📅 23:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwPUzL52tjADM7nm2FpEXBJbSaT2fD5E4ntt-Y6Btmq7vYrgJlMCKtf3-4BKDTSzSBNMj2fQ9dnnhv9bWARNCnDhtGLhNn01qzgaFdOA2XCiBElUZR_fsK7H5ljC7K8kHd7F2nuVVFbXl-6TmqBfW2M_d8LWOaoxYkqFPUWejuNQ-J9FT-j0o0ochaNIA6i3WzFe9EGGxFFP4R1g8hFLolvtu0SbBcebMBzhNbnMQpIAfRHOeB8QN25IbekN0EA8Dh4ljckFrBKhCGRaRZnVn4jMYlGQ-37tV7EQ9RnQpe5K08E9bCw-71s3HcruyWjVfjM57GudhNuKHNARwOTg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
از تلگراف: بارسلونا و لیورپول به میکی فن د فن ستاره تیم‌ملی هلند علاقه‌مند هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94263" target="_blank">📅 22:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94262">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss3pZurxBrl2zCLXec2IkbLO1UOEe5WKwGMkh3xgYV-QlqTke9tyPuheAmjKMKhGW1-16Smp6PyFObU40PC7z7C8PoHtoEGUtKvrwDrlwF4itKGRFFQDP4ASIC1dfG_0LhpciIx-LO11HrP2K7kj0Pupsqi0Bh-Lf9JMguCG-4HEooknwHTe6oRr4NiOeC94GYoZspyIFh6N0mhY-GXZ34ctrUsWIaVYqBrKUDWRKvODayDmYuqV1N_92px2CLJGYvA9jbQcpdhmR9K90987hPpOFlduREHIE4JGfhrrirBJJiu1iaY0j0sv9MHhRzxb9M-adj6z2UdjJo4Ip7vYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بهترین بازیکنان ۲۴ بازی اول جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94262" target="_blank">📅 22:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94261">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29742102b.mp4?token=BChAHa96AAFxT8pbk_3pCBbwpFKASbBEIr2dAr5nZTjsJNW_laCMkpMYSsI_P94DFPtyKjsd-X3rcT_57WWiBJ58APZsLzZAfyJq2p5RHg-pUH_nAP_2Q3qoudJjKG2-3iuKlobR0HCvY8vpzip7EtmSe83jKUZidZpDYhuiqeYooiiJNQ1IT_M01wGeywRPA4VXKhYgMNOCLdgwI-S60cXE_iE2SSiFKw9XXRDAioj1DSxczYCJFts4GwCzqR82Iy0MFKeG21G3H3Q8eQyR5VwEXoNRwfbvTFhRJw3Xu9qwQ0jdcsVSBxAkV7hWAEV-7PngL_NEdh2BytC2LHlh_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29742102b.mp4?token=BChAHa96AAFxT8pbk_3pCBbwpFKASbBEIr2dAr5nZTjsJNW_laCMkpMYSsI_P94DFPtyKjsd-X3rcT_57WWiBJ58APZsLzZAfyJq2p5RHg-pUH_nAP_2Q3qoudJjKG2-3iuKlobR0HCvY8vpzip7EtmSe83jKUZidZpDYhuiqeYooiiJNQ1IT_M01wGeywRPA4VXKhYgMNOCLdgwI-S60cXE_iE2SSiFKw9XXRDAioj1DSxczYCJFts4GwCzqR82Iy0MFKeG21G3H3Q8eQyR5VwEXoNRwfbvTFhRJw3Xu9qwQ0jdcsVSBxAkV7hWAEV-7PngL_NEdh2BytC2LHlh_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
انگری‌بردز ۲۰۲۶
🏆
بازی کن درجا و بدون قرعه‌کشی تا ۱ گرم طلا ببر!
💰
اگه تو هم طرفدار سرسخت بازی انگری‌بردز بودی، اصلا نباید
انگری‌گلد میلی
رو از دست بدی!
👇
کافیه وارد بازی بشی و
تا ۱ گرم طلا ببری!
📎
انگری‌گلد با جایزه طلایی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94261" target="_blank">📅 22:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94260">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-Fy2Teo_Fo7MrL0jSW13OTm8zRB5M-0ukNKcTI9ZfICttneu18n1fRscyk0kwFCw5NkNLrQmoI-Xwj2nIgMXt0coU1BXpck7loXfkPizmrxtNEwUmrddf7mQq-vLSG_eZT2E_ULUXqeRwYU0Inb4BJolW2M19ViFZfIstIsCYCHV2wnO4fYXCOBhmZKDAPpqa1_reetNeqndG7xCSWxeGwFRz6u8fvN6hvdqSmAfS9u3stIKYVCert42PXvAnas8L_-X6pU2bWstEtBZTmZfoSqMg0ElzYbzmazN8-vQIGscT6gu7z1vkU2C3ViFt3_py91ceCfTVR3Czvm5CIoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ژوائو نوس:
همه می‌دونیم کریستیانو رونالدو چه کارهای بزرگی برای پرتغال و دنیای فوتبال انجام داده، اما اینجا همه برابرن؛ کریستیانو هم مثل بقیه فقط یه بازیکنه که اومده به تیم کمک کنه و کنار ما برای موفقیت بجنگه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94260" target="_blank">📅 22:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94259">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8RdT6peF7tGLd7ktAHXdhSpmgcxCUwrT2kQellEvf_NwM6tsxbx5lxq4sUbz8Qzy5LWMqB9UkX75hkbv1-LrN2CzCL3AGP8k4BfhP1cemVWiaRkJJemRmnLD7iNx11xXTHpy7AmUWDAgwCsIeW7tS7DSV0-bQzzmw_UiuoAiLROIskJlx5ecJVUDuE7s3c2kRXjQpl9m_zLdagIs1oNHzWhu4xCU28Fn_gETjFzxGwNyGnQwHXi38ljqUQALb4lzpE3kyBD1KP0dA-GAKfXtlcnLOjP913HXI0gDQe4FRJeZEHpx8OH1Q3v2Rrajj9-sFdG-3cyjC3Vn33D-TxbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
رسمی فیفا ؛ رامین رضاییان به‌عنوان خلاق ترین بازیکن دور اول گروهی جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94259" target="_blank">📅 22:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6kgHgSANpfof8E5VrSCptpfYcwfqH-znMokmmw_ksVUBxTeER0sqIbhzm2gn_nNXae-FfJZf1BEPG9UUysjqhSZCYsATDiCCMoYNLcKJqlLRf3XF4u-wBXNU8_AUzryhLm6fO_DMpTLo2U3_GD_D_EMcuNtQGZzQCFAbnMrR6lnFybLSLfkwXCm5KKyOB9rlevahTx-xEdsr2pkGeXr5m4X5UjETtMypz8c00CVjO87MdaoBrwzZaU8BN5c1CzejL1F99w0prz8-xRBt9NTmiVg6W5z3OwIhtt4nGlPzW2jXZkmOIXd8d4K1ln-qGME294IkMdZA1nvverXZFf7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
رسمی فیفا ؛ رامین رضاییان به‌عنوان خلاق ترین بازیکن دور اول گروهی جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94258" target="_blank">📅 22:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94257">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjQNzvEV-RcUMsLCS9laJEwy4kdxsqAQHNn4ZIJxtPEo5F31bYQUZGTrTZGuP1cvtlvJ7pzoPfJI3pMVwdOHGVfFCLhihs_n3QGsn1eYDsnWjQOMQk8lN1OupZtNHqd-7lFyXYgl0gbsLW8ATJGnCiMUop0EzKQCQ715mDngQpUCJN5v-HL5Uy6nQbr9JCM1tIVX9ydvUujPvBiyh6MRKcr8MQ1mH-ImR2emMQR6MjQif3ySGTfXqzvf9K2mzHTp1K_JyKswVGHe4SMkiDIxtP3UIirjbs9AEgDeCrUJqS46oCC6Tj_2VxfofuGgu2M2_B2nlgSQ9OsnTJ6sieFfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری و رسمی |
جان پائول فن هکه، مدافع هلندی برایتون به تاتنهام پیوست.
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94257" target="_blank">📅 22:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94256">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxeIF6ovyHWoiSDBPR911Ruyo1oMG2I1fxHpm6mYQchg3EcwfdiTSY7J8shfrJxflLZlcUhPnWs0cOwax5QYPXNZef4zT2_iQLwJwpbF2BEn6Vltxk64LE-d9ivloeQfm7WcK8cWXrv_hO2RFHwq8J5L8unvUUKXUXpu6dGLUSxyPFej5y2ujmXUMKHJubPIPjytm-Pa8G97QEPaUC_mAJvD35AGUDe5hhgdIfRgjyg_4MkofH0MyHpOPhxPjmynpBClbcMS0-xDFBsMKQ72Mwf7qVrcYdJt2gdSYCJRYd8jQsNP8TWYeQBQDa24GIp-qOQg-Urvq_cGXYpAAJU2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
#فووووووری
؛ کوبو ستاره تیم‌ملی ژاپن بدلیل مصدومیت دیدار با تونس را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94256" target="_blank">📅 21:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94255">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFlE6iqo8rYkDgc4FhfsIR8w4CsiqIkmT_yQyCkwI44P-BiA8GgW-2OuliqzpSmvhAT21NOJqUX8y00i8UyliUluz8NGuePgtriwvxpzMqVdIrKYf5z3n_5EH8udt7Y_VuV9nbxgM7Hy5DpiovpmbDHNqfV029S0FPhQGRGueHhvdeXCuhh39tsnLafGHZNkCvm6d5VbxolSFI0HE1qt2RtUbjyTOzgZ1GzRUB5dHxkLbcvGmPOx_6tpUlBSbMMAIC-OnEK0YMJFYdZHXxJRtepC21FA1P6WGJ_61z7XJsFaBVvNueZNSENa4eykDL4TSdYO5mjEzWvlnN1LswaTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
فیفا، لیونل مسی را به‌عنوان صاحب بهترین عملکرد هجومی هفته اول جام جهانی انتخاب کرد.
👑
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94255" target="_blank">📅 21:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94254">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPYrLFVCv_VVqEePuYnIcWrUMAcDI_brb9YhGZuoBYPUkraYFgRlVVYfrlkDUIzKPIYrjPROZE9VVb5eq8wWAB395Or5upRov7ZRE6cfrmUjml_132QrVZ7tIKY_x199Rd-lgcTYUpPKbHlz3BSsWDPngWM9NGVVwWl1rk9JQNxgrI0tAUFR-Y7mjv9IcX3BeBM9D9Uu43dlrYwUqLb2Jsd41MBGzIcr5KkZBj3VeQwk3NPD0HakPu70l9nQoRlynbGS5r5wARzxi1j0TicWSTFUU4Yvxs7otklph6wwxl7NGRWrm3mBKk5PuFDAiFsoHO6-kKBWHoUgmUcBLdLCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اینترمیلان از تمدید قرارداد مربی خود کریستین چیوو برای دو فصل خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94254" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94253">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6ZckzrDP5u3PssI5NueHTJ6qOqNFjlhwj-k6kGwtkCvnXxuQlnvax2OhHaRr-m8TnULRxy4albFcm5sOhzsigpXrHfNG-prKpkmhummy1ey4BdTJtKLgehzpqkQlj3DayYszyMqQ9l8yucd1V0ybZWU20rrrZ3jfB5QfKcUKcVbSQ_4n6Os7ShSwVZPXNrdR5fxq9OrKLtmhKwVPfi_KQ-tIS-oz6FOiMS1_ZhJuwDKuXTH35jgA8D3RT6zXwZV4wANA61M5AwlcnrJepMX9TN9g8cn-tMRaCJ2aPXdOkwLAxM9MGa50XxfO5RCdsGPioVwC29TYaEkv2jy0CvsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فوریییییی
؛ ویکتور مونیوز به لیورپول پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94253" target="_blank">📅 21:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏆
گل‌اول آفریقای جنوبی به جمهوری چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94252" target="_blank">📅 21:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">زددددددد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94251" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آفریقای جنوبیییییق</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94250" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلگلگگلگل</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94249" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtBX2r79azNhkU3XoQNdD7eyDQ6Vip52_F1xuGlbdFe7Mq6DjPS3XFx62B9R42bnThdR85hninPayiXpfLIusvM5l1S80Z6DMVFgA_EQ9Fuuw1nwp4HYjUmqazfA8d8yhF2MM-FubKp3PVQfSHwiKC49-hWrbXO_cZSGfiVdeuWzDg50ZMem3J5_iTDg68FspxtHi4GjYJPSkuVSUrzWmukOsz0gJtGG0dIHhTmFrPTCxcrxb7rqqXV_5Fxt-1VSoZSIpRWn7Ua3SlbzSuFR3stYRF-_lMtz1S5UCX5O8k9HmCbkMlc0qjv7p67qpdSgigsAM7nu8w60gUk4ExUS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فووووووری
؛ مجتبی خامنه‌ای: بنده مخالف توافق بودم اما بدلیل درخواست پزشکیان به عنوان رئیس شعام، با این موضوع موافقت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/94248" target="_blank">📅 21:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پنالتی برای آفریقا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94247" target="_blank">📅 21:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94246">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kazfHTtuQnMrGtO729QglGAk-bLbVMWjIn6Xzt8OKPFnWsOLSmW9Z1kTU5WhIBkzbL-RgZ1y15eG_bmCPloAlujZp3hcXK0nAh77Kk9OvyXdvVzPAz_htMgXSvD9GU7nddBS-RVCROR__0oGHCzSSnZgDeC2NSoV3XIPdDeLMAFm88s6Ia5YNkXOpr1hnUmBb-pDnXTSqexDdhlER4W9rHZkguRaBZPHkSFoxPy-vQnh6AwB-35hAq_hMFmTVL03uR3nrhtdZJQMQZC663fsD3wXT_k-GJgx0pqY3SBR95PVfRU14egucdhmPciIRJEMzpOzKdZTATo4d8BocSKOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇦
🇨🇭
ترکیب رسمی بوسنی و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94246" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94245">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZl4pZF_grmQ6_08AZ4n_WRsc53hJ5bsg3dkv620rnNr7mntSNE2Fho5aG3Abr12iT0LW4I2g76GDVqMxzuG6zrIhe5I2Pv0Od6E53HDcOcEqNOz77_1MUENSh3sLKfDO591aog0vfGtttzAemNCwqSWqHMgBGW3AWvlMbiWERM4oYPGYIOmTxS0gUJJhWSjBlZ5fha3qJ8QDl1LFFzXGmj1CDx-BzpdZDBNQSMdtxARvI8DbzAmhAYdTyvymNKVUmQ6ZeIhtWIOylUMKzzAu17VAH38CdGV0Qz0RHhLBtJkRIGl6kYlyOz65l2XsD3mAqpLZ59SMQcZ7a2oY9Oi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مارک کوکوریا درباره انتقال به رئال‌مادرید:
فکر می‌کنم هم من و هم اطرافیانم، خانواده‌ام، واضح بود که این فرصتی است که نمی‌توانستیم رد کنیم و من از تصمیمی که گرفتیم خیلی خوشحالم.من مجبور شدم تصمیم مهمی بگیرم و هیچ شکی ندارم؛ فکر می‌کنم این یک قدم بزرگ برای من است. وقتی بچه بودی، رویای بازی برای تیم‌های بزرگ را داشتی و فکر می‌کنم رئال مادرید یکی از آن‌هاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94245" target="_blank">📅 21:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94244">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0717ffb37.mp4?token=dWjOXzdecUPiF75d8y40TdeFWlbsu8EC3MPP4JL5B-cFeQ4blRGIns28I4EDB8RMKNd7-q3in4ajABWDs5oD5THP-udHfk5gVoqCE5WfvYomBaGBvquqbkvp_XYiHZmtGR4CkmTLekZrBtL9-notDU16aL33j8Sg_9i7VX0OmbEYA6UQUrOTu2QAi6b_2pojoYJLc3b07HZTi4Drnf1rme_PBxoQfGVzdKBF_QzCJd-Hp-ZOAsHZ8XvUs2Pp9z6QpW8ziUKiVHSqZak9UYJnI5B8MfRGKikOM2FaZ-mL1473QZq37d1fnEjIXxKnDOEnhWeD3zqhdigKHaKFTZeFlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0717ffb37.mp4?token=dWjOXzdecUPiF75d8y40TdeFWlbsu8EC3MPP4JL5B-cFeQ4blRGIns28I4EDB8RMKNd7-q3in4ajABWDs5oD5THP-udHfk5gVoqCE5WfvYomBaGBvquqbkvp_XYiHZmtGR4CkmTLekZrBtL9-notDU16aL33j8Sg_9i7VX0OmbEYA6UQUrOTu2QAi6b_2pojoYJLc3b07HZTi4Drnf1rme_PBxoQfGVzdKBF_QzCJd-Hp-ZOAsHZ8XvUs2Pp9z6QpW8ziUKiVHSqZak9UYJnI5B8MfRGKikOM2FaZ-mL1473QZq37d1fnEjIXxKnDOEnhWeD3zqhdigKHaKFTZeFlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو: به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رو مال خود کنه، اون آدم کسی نیست جز مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94244" target="_blank">📅 20:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94243">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeuYPrgNbTTld4qmiXTn5TKaHrANGHVBwIDV5uIxdmQqzdIuZ7kRBuExeJdYlOHBraDA-qmQW284oFRqSOcj05IE_GhXK_oXzxNCbILplUWIcfHBfqnD4_09x0M1PdkGsxngT_RIRDYnAMoVGBgFl3QFHO2Qgops3aEA5ojwMcGfrffcvL58Uo-KRBE6Dv9CVMxxZsRsV2EofhyF8G6nWHGfxhLUXF1xVkG18ffleFVsY-vOcCrJUCOiEOflLacFpUo7trOVPI9hfX5CCjldjM6VQVeFMkoU-f7NG_2IGeqLMWNulBuV8aXqUevInUGHW_LfUEAAIXUp63D1OkD4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بلینگهام : مودریچ بی نظیره، اون بهترینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94243" target="_blank">📅 20:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94242">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPUqdMn2xY5p3KivYf6kKQ-jfN4stZ4MWYFw33c9ehAdEN8j47l8poz4AvI1a8O8f_xDaZotKtA5A38DhPQC_6CX5GTYX89gGr_8ztVzeOM1Tb-FunqeXeO6uD1FrnRBTUyxz4PnPidN7kJ439yRAyG59qNmUWNCY_mqeHqL3zfA4q8HHRRwTLpyzk41ge1GwO50jj4VGgr27zkGe1bYSxQMBC17Q3s25F_ZemjebVz9gzLWcOIc-OzrGjnfDe9SFQNJjF5_vnZrPTlZusml9JVk7wM9cSZN5Dlhe_BwKZ41GxxdyME3LbA-HDZ1H7xyLNpwQwgFYG3dY1MbPlbvKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
بازیکنان کره جنوبی امروز دو پهباد رو تو تمرین سرنگون کردن، فدراسیون فوتبال کره جنوبی رسماً فیفا را از این حادثه مطلع کرد و خواستار تحقیقات فوری و اقدامات امنیتی سختگیرانه‌تر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94242" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94241">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94241" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94240">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbFniDHZHGSvG0htsn1VdOGtZyffcUH3Zg3SP85wH_w0CQf0bwoqmZB2PdwehlZc4yPzYFoIQYJs34my_r9OzNFMXSYxDtxUDSFvoe6ssVg82HNbK-mMXRQsJ4Fgf81UfW56Fxqgv1hMLNr9C5CuPwEkTcHLRABMs8friSw6buE_7UJlgILnHCIO5C8IuxkFkNCjwvjQbHojoG466Hzd-MsSpdqAxJvM_28QXtczslbQpjuEOs3c6jbicETRwTxzRbdlGVDz-NltSS2vDUvWsjw4NVv0AF9AzVGHRwWWiaLjPd-izs9ejOew0jYHHyR51LwzDiPC0JygTJVwlWmsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94240" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94239">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پایان نیمه اول
😀
جمهوری چک 1 -
🇿🇦
آفریقای جنوبی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94239" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94233">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZywLXbY1fQ_Zjf2wfXCPqWGYnl_sv74U1Zn5aEdIz5sqJ0k0TYelRPx59z7z_3_thf-NfwsYTcwOFW8BLmSWM4LrM-_-qQyTrE2eoQlb-dRvK47J-kQIZ6gcArhc10ro3NeZgE_VQ3W5VkzXxOu00bFEX5jazXVlEKtJXJk3hUsIx0PEofYlY5TIHpGY8TU6uTpNPyuEiEOaBtRP-90vFbdVChL9wn0beYg_9Yjpm-3F2l_hrXeGrSLvTe9LJNR4pNRVQEKbv8QNa52dw7GuIjAP1gBEzflqPba3zzCtB0pNeTq8yNdfhMbXaiQssbi6KIltJNIjM7MqT_b8cobiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVK7SXyY8a5YvRd3iTtEB7sO-nJCRRedDYb-YPYGf1RVfC4bEJfJ9RhMlTYz1F0I-P4VXI1U6FNhDww8GDywVUleSMBhujtSA0Wo37GrEZ5KJVkKSJAqX4rhqmmhPYL2ClaxEalBb7JK-9KCE4nVuAuhF5V1M6jYFPZke9AYZs-fLHKpeG8krf4bK8VFetu6R5nBbaPgyfHcHqD7NkZINgHbtb6NmLaRcR_g_r23Ey9rQ1xCySihsWGVz1W8HKzy3k0bxj3Avs9FBP1hMUUJwV9-Ph4rXY1dMr6W_CeWhQb6dOemCcwrKeNFzdRA_qBP9jn1BIO_Za-VcRFmoiv8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNM6GN57c1KGMAMsoW1pihCbxqla_Ys-AGTkqVmr5eBz3xWRGLEeO0DCxdpmNVpvy6LKPFjKhFoHbwOA76_CJnmWrvbzjLT1rPhHn3ibDLxa67434zFPSWzcCOKQvIG9KU4_kggIkx0MSmk_XIDsOjGcUYxONOXF9pZUptxX8fnSTDzFLTjaahol5tOVtqOzUV_tNfCYDwdWnska7lSWaYgJWJAs7YsERYkPGRnexHixmewHhJGX3OX_BTYnWJzpWV7s2OF_F2kgRhNb_lQcZQmP-j07C6DG-RcYrdTLBZwp33DJ5GiDGil-hIxUr0zXtGF3-9zS2MfikQRav1bBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uijAKwamhwVPFmajJlDHLvJPYgACKAFQabvuoHVQM7E4RzQACsOYMBboC3ymI3ERD7ktAyeO9X8fA4YE8Dyx1X49ah6j0VH2r3zFyG2sGCIYSUuP4IkepGPwhxdqSzcDjBXdo-kdvglzGWfBvTQx2f2CqHCCaT9oEgLQ-Mn-8H475ho0m-JOt8EDvXl6RVgfWgSmvdlooCzx76OU37TFoJs8gVhlvJ062ZtdbJ7cA0us3XGHphMX-duK67rLtr9qgA-V9UFPqhSLtSp4ALtBqa-DubV3to4cVHP7-oAXv_12Ww9kKxeRCe33kvdFtHqTuVwQeT4E91_82vBymp6Cdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqZLbaXTKH9SU7DmbgRadJQ0qeTiQ6Ncnf94O2LNad5AcQIYa3XKwidKuHrGcYcbuicpO1xXM8CvvBKc809Q0tZyq3YTOhKQTc2gPCgAe2dJYpFpV3EY06dlMR47Wd06rGT1ha3Ow5JLPilIbQeQXD5_Igs5zSE1vLbygC937HoYqlpt6ICk-IGzpIFF8_orlbnzOOTjPLPoyGAcqT2hrpZLNrtGUdfqdDGHN4mmRnqBtM_VVopbnkwujB1c_r_kqBkxMdWUbbz_CD4f6xLtQIRpznq6To93jbOg642h5iv_KDKj2POJeqadlVwZ2n2v4NkQpnm-9FSFIqYhmXMS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i91slw946d26Ji0vNF-6mJOlMxXq79Ts9i9UV5Pho0Qq9AlbZRi68sc-TrH5KnscB3WYquHR88sXxsBUPR8Y9pTSTNt1egDPWN6xVXhiTzWIsp9oeo5yiW3PKL7FjrgaTWJAk4_sPP-TeK9qnBlVL7DHwD0_o6amVt7TQ_EGwvloTT_SMy9j7wJsxHyuEB3oReGI-opXikTc0VfVwO1k1pMA-tCOiAaikUt1xptcONVJMVm0kqY3ulSZ0HFpknGeOXhWuBbpe_7Z1ZzyeEWKDcSMLwqhE15mMJOufz3Xo1yWNrBXVengqyRghHUk8PjUJwwrO5VLnfbpAg3jrND9aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای اسپانیا و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94233" target="_blank">📅 20:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94232">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiWw9IAzbclTc4MOyCMcRorN4n2W9KLAdiTBp1p3o94CEKdAU_WvBBmY2TF_AZXB0IESqDPOO5pGb0kYPhfZAsWTAK4SqhxDrZaCA7UD8d6vmGJkHY16WBl8cdYlX5F4cPIJvORIruR0WGW07SiX4DvIxF0XNFgcjVciT-zaWWmOdNQPlBCpfBbqVrH10hCoVu-Fxk9_kmjLbUhwfxUNARqy0JxZps_8RmR3KEegQRbhgBs0a7q-t9VL6nhqYS19L9rtnuwHR5KBVKPigN47DUgkXUHdNHnYAmN99B3Hd5952BQjBqIKFcPPKbCEmy8BEpOhmbgRxlxndG9gImJg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
3 گل در جام جهانی 2026 پس از پرتاب اوت به ثمر رسید که چک 2 گل آن را به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/94232" target="_blank">📅 19:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94231">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/562bcb149d.mp4?token=qZ7CkEHCza7hCUvPPPwIH4X00bmdcZjfIWFwAi-ZjTPqGvo0UknMlzekJD0uMItp6W1aFPqHuJ9gUExQQVu1y5v2K-zcflRe94aKmLnjt95Zv53Mcta0U9EjHxnUcenM9Tj_vpujyARwKTJaJYro2FfTWA2lLQgAudepk9N2FeRcaOtZrKbEyj6I4QcTSq2wbFEpOKtsqQX8hHsODNlsfNe9oMtUwyVkQJqtaHbh7o-f_d--mAGfV9nK05yqd7rjIPIaUm6bl2SdK0vZe09si5pQQEMLBDcfiomx7s_p36owXorUfXv9pM8YXo5aFkj9QGfMj0mpfq9gnHA6LYfZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/562bcb149d.mp4?token=qZ7CkEHCza7hCUvPPPwIH4X00bmdcZjfIWFwAi-ZjTPqGvo0UknMlzekJD0uMItp6W1aFPqHuJ9gUExQQVu1y5v2K-zcflRe94aKmLnjt95Zv53Mcta0U9EjHxnUcenM9Tj_vpujyARwKTJaJYro2FfTWA2lLQgAudepk9N2FeRcaOtZrKbEyj6I4QcTSq2wbFEpOKtsqQX8hHsODNlsfNe9oMtUwyVkQJqtaHbh7o-f_d--mAGfV9nK05yqd7rjIPIaUm6bl2SdK0vZe09si5pQQEMLBDcfiomx7s_p36owXorUfXv9pM8YXo5aFkj9QGfMj0mpfq9gnHA6LYfZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رفیقم: داداش قمارباز اگه برد و باخت به تخمشم نباشه قمارباز میشه.
همچنین رفیقم بعد شروع بازی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94231" target="_blank">📅 19:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94230">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
❌
🤩
#فوری
#اختصاصی_فوتبال‌180
🔻
اگر اتفاق خاصی رخ‌ندهد، اوسمار ویرا سرمربی پرسپولیس طی یک‌هفته تا ده روز آینده از هدایت سرخپوشان جدا خواهد شد. اوسمار بدلیل مشکلات خانوادگی و البته درخواست حقوق بیشتر نسبت به فصل‌قبل، موانع مهمی در مسیر تمدید قراردادش گذاشته که بانک‌شهر مخالفت جدی خود را با افزایش رقم دستمزدش اعلام کرده
🔻
دراگان اسکوچیچ درحال حاضر جدی ترین گزینه هدایت پرسپولیس شده که البته فعلا بابت مسائل کشور دچار تردید شده. از مهدی مهدوی‌کیا و علی‌دایی نیز گزینه‌های بعدی سرخپوشان هستند که بعید است این دو در شرایط فعلی قصد حضور در ایران و فعالیت را داشته باشند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94230" target="_blank">📅 19:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94229">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9605daa245.mp4?token=q60429f_1q_uhvRhSzkFkMyP-3tFrF8UcLoW_om2BmCOJNKcypB6mUANQyzpwJ7C-pE-17IChoPZ83snFaaslpL1gUKlTvhxLpjAHURLWosABBUXw572mzIfhEic7tR_-55jmd0xengOYWCGImM7Bav6c8PiEepVzAEH3figC7Y03AMfrY3lXia7dQseZE6ONpCGuNuqrkQq14vEGTEMDmpUK9Hh-ToR5voho53O7YjXHovQancwHkr-yKQrDY3fZsGL7r7emhGHE7IjeD4VwOScwDCpAforjrI1BkYU5g9NyM8-GSJW2UU4n4SpfoDyytnlcwNriC9bYXrM2Wf18Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9605daa245.mp4?token=q60429f_1q_uhvRhSzkFkMyP-3tFrF8UcLoW_om2BmCOJNKcypB6mUANQyzpwJ7C-pE-17IChoPZ83snFaaslpL1gUKlTvhxLpjAHURLWosABBUXw572mzIfhEic7tR_-55jmd0xengOYWCGImM7Bav6c8PiEepVzAEH3figC7Y03AMfrY3lXia7dQseZE6ONpCGuNuqrkQq14vEGTEMDmpUK9Hh-ToR5voho53O7YjXHovQancwHkr-yKQrDY3fZsGL7r7emhGHE7IjeD4VwOScwDCpAforjrI1BkYU5g9NyM8-GSJW2UU4n4SpfoDyytnlcwNriC9bYXrM2Wf18Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش های مربی ژاپن تو بازی با هلند که به شدت وایرال شده و به انیمه ها تشبیه شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94229" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94228">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0LKlcZyJs9fzzjRQ11irbEXfywasHeFy0q-Fjxq4R6hV-0gyhi9bXGx2R0qFd3Y9vBTEFq0NvDJuFe4Y_7Qm5bbn9GFFRrigZbt3TWvr3sqwYup4rQOfeDvU2j9Mzxc0g6V-GdeY7MTuL8xI5cJEgvJQ-72F2LEGMvvOjD27XNs7jBGt9mCJZ1acv4WYt4l_4Ob8gQFPT1KFuqvmX0H0PuQkjWUAN8RDi2E9DvRcnneNlxfPJ6oVjZtqpn8zAL9IJa52MQlkgtUt7SSo78UCH0lkhqZsJYau5C5MkHrj4KvdbRjXKnOyKT8ik3mNCap2lTUvrQejX_OIWrdDNnOiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیش فروش GTA VI از هفته بعد شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94228" target="_blank">📅 19:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94227">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLai6v-1SHgITncts2CjdLs08Mx5ZmIn9NHRt8-vmf_QmM2LqCI23aG2Qc0SCGryRBIZU0OghrOUjvYDgOG4lJuzAPVJANCeKiwJFhOCuqHJ8aVLGGXrxvuCES7UOFP9AAiBbJdIWRvI8GSHIDWRUrXKCcD9roKwaWSDQWuwE8eXBpu0Wqduf8n8w9NqeJ0cgChX-SPPD2CmdVPuc0pOn8m5ksSf-4J0qE8v0rs7MGN9qHuKWIcENjB-7WVEOeUCAl8AqgtFFGxUq3QhDoKtA8h7mN5sOb7OCPoimblZiqbsGEDpW5B2P9KNFcXfLshgCnb-TWlPQXwXuvNYxThVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آماد دیالو بیش از هر بازیکن دیگری در هفته اول دریبل های موفق ثبت کرد
🔹
او فقط 34 دقیقه بازی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94227" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94226">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2opAb0x44Xf1FyCWdrkfyNApL92GjkDoyTdGiLVJ4nU4MHBqKLqctKV4G8v4faOxULL05QhhCplV_fCmvLoDDCaOz_bzV2aJ2hOHoP9GoTXTvIm3j-qt4LBgpjy5vTsuPSdrBHVPUYJLfdbBwMMuqeC8xMsXQdg95kIgpgQLLXME1okfu2mWNW6BbGk5t-loagu7HwE8Vod0RDIikCOrbFpwXL7_Am9auX_VN8r1kj2_RuSE5RRQuxhDlG8AaalYIm4UJOrtqjGFjD7ADYaJW8lD4VRtmDvxzj7UJbXsMz-K5F-7G0DNlG-GoK_U0bhzxP4deeFajG1QB2x5C_j4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇿🇦
🆚
🇨🇿
۲۸ خرداد
🗓️
۱۹:۳۰
⏰
چک
🆚
آفریقای جنوبی
📌
📌
تقابل یکی از نمایندگان فوتبال آفریقا با تیمی منسجم و ساختارمند از اروپا
؛
جایی که قدرت فیزیکی و انگیزه در برابر نظم تاکتیکی و فوتبال تیمی قرار می‌گیرد.
⚽
🔥
جمهوری چک، تیمی منسجم و یکدست از قاره اروپا با ساختار دفاعی منظم و بازی گروهی حساب‌شده که همیشه حریفی سخت برای رقباست
در مقابل
آفریقای جنوبی، یکی از نمایندگان فوتبال آفریقا با بازیکنانی پرانرژی، سرعتی و جنگنده که به دنبال اثبات توانایی خود در سطح جهانی است.
🚀
⚡️
آیا جمهوری چک می‌تواند با نظم و تجربه خود بازی را کنترل کند؟
یا آفریقای جنوبی با انرژی و انگیزه بالا، شگفتی‌ساز خواهد شد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94226" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94224">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffc86a865e.mp4?token=J7sYhyHDgloaxP9bkPWMMoSa-HacNFDU-kxOPW9ah25RO2tsppFMujFiOitEQ2w2bxuCVT_Ubz9ZiQXt1Z0HJnQjFVFs7msy7hLBKbZ-mYjWl6uNaUJCNao3loks1yxYkKxb6_LLUGk0I6nKNizr79Tp0RIDf5fH75GZgmjhgm4TQycDaxIXZwx5gHKCIfLEYpGbpyj_MjLRrfb7KPwaXnvQqpmzVmyAJmeW2-s_zs2zFvx1T0yzdyrhqCdJwxidutpAWUaCh8WnXKHHedcgm1lLgZLQjgTVEh8P5FqSnRTo8GTclKR34vzjBdSF5H1JXsm0WmyGVTfmsOkpbx6cOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffc86a865e.mp4?token=J7sYhyHDgloaxP9bkPWMMoSa-HacNFDU-kxOPW9ah25RO2tsppFMujFiOitEQ2w2bxuCVT_Ubz9ZiQXt1Z0HJnQjFVFs7msy7hLBKbZ-mYjWl6uNaUJCNao3loks1yxYkKxb6_LLUGk0I6nKNizr79Tp0RIDf5fH75GZgmjhgm4TQycDaxIXZwx5gHKCIfLEYpGbpyj_MjLRrfb7KPwaXnvQqpmzVmyAJmeW2-s_zs2zFvx1T0yzdyrhqCdJwxidutpAWUaCh8WnXKHHedcgm1lLgZLQjgTVEh8P5FqSnRTo8GTclKR34vzjBdSF5H1JXsm0WmyGVTfmsOkpbx6cOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول چک به آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/94224" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94223">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چک گل اول رو زددددد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/94223" target="_blank">📅 19:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94222">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
ترامپ:
اینکه کشورای همسایه ایران اورانیوم داشته باشن و غنی سازی کنن ولی به ایران اجازه داده نشه بی انصافیه! ایران باید برای تولید برق و مسائل مسالمت آمیز اورانیوم داشته باشه. ترامپ دیروز هم گفته بود همه موشک بالستیک دارن ایرانم داشته باشه چیزی نمیشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94222" target="_blank">📅 19:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94221">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL-9lZTsTgUiFiRc_lbk-2jnGfdy7JU6AS1i-nwREtRKMpSTXVLKE19rEu_91TAY-DIKunUfHn7pfCF0gNF048qCDu6OQ32deYf-FS8YCRtTRfIxB1mbZVMmxWwyO80T-0p13FdVpMqwfG7Ia9C-mIFTDAg4qo1tnEwb00zk_MRDTuEywErvBqsMf9x_th7m9dgN91bhQkslo32StwNjscnwC23wTkey-mJSMNUPhmrOwiwYTrR2hu0DtH_146p8IkF6cCuWMqxsTu_PQ3CDIp1XOGABCKiCOKWwpUDuW90kEay3ot3eK6oZ4pwNn8k1X04yJdn6KUAjkeqkosUPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
مسابقه جمهوری چک و آفریقای جنوبی اولین مسابقه در تاریخ جام جهانی خواهد بود که توسط دو مربی بالای ۷۰ سال هدایت می‌شود.
🇨🇿
• میروسلاو کوبیک (۷۴ سال و ۲۹۰ روز)
🇿🇦
• هوگو بروس (۷۴ سال و ۶۹ روز)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94221" target="_blank">📅 19:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94220">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b4f88afb.mp4?token=K_ppf5lLMZnu61k3dGeDEl0pWQ8WjJfsbdUbJWMcBfe1K-3w9C_UdLZ1mDvF3AVypv485WgnlmuL6usebOjlU4QwkWBVAsnRwt-rLW4IxljFeTv3hxrWr1SSu-ZNp7KsVgzM23YaSYnmLFN5L6ll2nWHhFHtKzW5fhHnrJjxYDf2G9o5E2xol2J9_x1AMVs5zG-Lk0mm1Abo20oLj5TZ3OdL7co_ACnc_oXd5nAbE86K0dO_aRXxVWpKJlx8TfuvMtm4pWgMAQaLXVHXqC5SAWEJxzMhzHoQj3L3VZQN44DIh4YyJ88o8YrQioqtZ42LbysNUuvpVEQJcQib0-b81w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b4f88afb.mp4?token=K_ppf5lLMZnu61k3dGeDEl0pWQ8WjJfsbdUbJWMcBfe1K-3w9C_UdLZ1mDvF3AVypv485WgnlmuL6usebOjlU4QwkWBVAsnRwt-rLW4IxljFeTv3hxrWr1SSu-ZNp7KsVgzM23YaSYnmLFN5L6ll2nWHhFHtKzW5fhHnrJjxYDf2G9o5E2xol2J9_x1AMVs5zG-Lk0mm1Abo20oLj5TZ3OdL7co_ACnc_oXd5nAbE86K0dO_aRXxVWpKJlx8TfuvMtm4pWgMAQaLXVHXqC5SAWEJxzMhzHoQj3L3VZQN44DIh4YyJ88o8YrQioqtZ42LbysNUuvpVEQJcQib0-b81w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
وضعیت فیلمبردار بازی امروز صبح کلمبیا که بعد تکل خشن خوسانوف اینجوری مصدوم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94220" target="_blank">📅 19:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94219">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4N_UhXUNI72ahrNjTQWrJVMP7BGoAM3bZHBVxAouL3VOSYTzwi7WqpcuVXNE4ApDmNGb8RF9POTKTiGHh_COZqSukgS_xE33GjCuUNB1zKDUIwHl_icBLWiJG9WgxjMydQG6-C26bUMRNLg2NvJs0ygEtDTWva-45pAjV7GwyqYAIGqvLvxE8GQJnCiqOgbGHwYbZ6BaDXLZhdNotaj7D9Nc4qYtIOpZGRo3KqoFw2HAqpdDumCv6deO4y1tEe4lkwMgDQ-KyLu4Dpysb90UjC0arrYu3A8nToMMY9v_bKepfPsCDgGcXLpzHxPTyhmZWwe_kc-zO21t15pAALBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار معماری ورزشگاه آتلانتا آماده بازی
🇿🇦
🆚
🇨🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94219" target="_blank">📅 18:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94218">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462604bf.mp4?token=soRxlamw9GTngkFach18Q5Z3qylXCikdgFTUNMXBHtvv75kQz1EvLY73SvAosw0uCrkJcvY-GT2MxGQwO6j6x5du7xwuk0V9tw9IjJtUgtEiUxLk9xBn9gu-6GBYtCBSi_LtDRkXb-pK6tPDv-NPmpPLGYz10DjklMyVXf53we5AphchwFseZ5VZWLPXiFWBQvSkAix_tWcEJEE-noSB4l738JhOwGa8SR9iK32bMM92xYwqoO7XYZXnl4L8XVaQ3uj9THluXaXUPo922Q8lEU6dirZjNxj9ju0mvTmeUAEEVcQRmNVXDwH2HnwDVWU4oKd1i9YwIB1Wbaw_diq8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462604bf.mp4?token=soRxlamw9GTngkFach18Q5Z3qylXCikdgFTUNMXBHtvv75kQz1EvLY73SvAosw0uCrkJcvY-GT2MxGQwO6j6x5du7xwuk0V9tw9IjJtUgtEiUxLk9xBn9gu-6GBYtCBSi_LtDRkXb-pK6tPDv-NPmpPLGYz10DjklMyVXf53we5AphchwFseZ5VZWLPXiFWBQvSkAix_tWcEJEE-noSB4l738JhOwGa8SR9iK32bMM92xYwqoO7XYZXnl4L8XVaQ3uj9THluXaXUPo922Q8lEU6dirZjNxj9ju0mvTmeUAEEVcQRmNVXDwH2HnwDVWU4oKd1i9YwIB1Wbaw_diq8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برزیل از نمای نزدیک چقدر زیباست. بیخود نیست دوست دارم این تیم قهرمان بشه.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94218" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94217">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg8rHqVoe4d8TnrHQWl0mdy2NhcPS4fJmtTVbvS6E30KuM-Oyyp17LokVYq-QkyJLYq7D3aCqWynMpGOP2E8b5vUheXqRa2W9KkJUNFf6habqf5OaSbhAOpyYsquI8_FRLNGPF_B1Dsr1qPzk8EnmDgB-M-I7r10IBwrLyE2cBZj_Zl5eQ_FEcOE7Pjvz1Le4X9V0fDk8TkRWbLJnOZ-6hp5ELCyEYCrvASGTWsYs1IO034UDIcmO0LB-lfpJ28034mBO4mbGiNEijF_ScB3aew7MhyQLPaWfV3zhEN_IiyU16CmeIPboOi5Z3ac_IEM5gZdOB2JkUqa2PxzrijWEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیمار به همراه اعضای تیم برزیل برای رویارویی با هائیتی به فیلادلفیا نمی رود.
او در کمپ برزیل در نیوجرسی خواهد ماند تا مرحله نهایی برنامه ریکاوری خود را تکمیل کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94217" target="_blank">📅 18:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94215">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfagJDu820A3SLg9JesQlJyq7AZRsWSJUpzaYxp8uBynxGL2nm1xFzpwq0_v5B6OFgw8tgQm2MDYdN6yVuXS7KoXMT8jCIX33cOs5w8W9hVknM_BBX-lhdH8tn5IkngTTnrSmUTujz7WCibkE7YwqQz3dlnyFFI8XfCjUWMtt_cKzkuJixdTKjAJl_LEIGPs_OyVMJ7s4KFDUFRp1_zmsYts7TI_xrJGh5U68FPvTvsapdnLEMrHz_9c7F5q7yUgVoO1vwpKhISLfA-Uueuean5FP64zNyxu34dy9-mR6B_dj1KpVfoFeFS05zUqe4ny_B7W0qnp1vwY6Dj1QIDxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYrdPPb7Qnk2CKEZvEWTS4DAWk5lpBPoO0UjFc7OgBsYJ0OGyuXJjkYLNdjZUOsORRukCwrcwxa23-jeHWB5q_hSGQmLtTQkEpcG5SMjFbJWF9dTa90hCSo1Qsj1C79aoaGme6de_KBkm3WZTqih5QvuxCcMPLqrIYHlCmpIKC5_yIystTNVDEY2L3kMdyNNZ-T3TiI9Az0-nPuFa6IEm5PvES53lA22NelY4wkp3DXOG0pzOZ73MMSmn1Wnbb9nZHFBttFM8rl834yuGMnTkVzeCk8yJuZvzZGbkqpxeEBDcP1iw8Pn7Y5zdpMczoUx6x_7dTJ0-lJbX2ahEdKxeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇿🇦
🇨🇿
ترکیب رسمی آفریقای‌جنوبی
⚽️
جمهوری‌چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94215" target="_blank">📅 18:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94214">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723f2bef75.mp4?token=aREAajqpciB2jLKIKMNGAeHjRuWTf4gUZRojuAhdLQHsG7uyh_BdixX2rHHhT2sIetLUKOgeJL_zIaGOwDJBJv2MFZuprlBYl1wK2dtFATvrKDpEBvL7InotC2KXbSBP-hJIHBLk7-v7gzXEHOiew6vJ7cNEcKG0vkzb_swp4Jm9jeCC45r0mwel5DQVPVAYS-64Z0BdVjEWcXgC3E_OzRynJexKDcdEgjuy6-WC3PGZry0cv_B9sGl70TPVwjzTB8gDczY6X6YUs1zxpWpHqiaBTFCyeYlnOH_zX4oF2puqTbJlSnjCYD9VfI_utjz0cjv3LDvsn-40wjeaYDlnKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723f2bef75.mp4?token=aREAajqpciB2jLKIKMNGAeHjRuWTf4gUZRojuAhdLQHsG7uyh_BdixX2rHHhT2sIetLUKOgeJL_zIaGOwDJBJv2MFZuprlBYl1wK2dtFATvrKDpEBvL7InotC2KXbSBP-hJIHBLk7-v7gzXEHOiew6vJ7cNEcKG0vkzb_swp4Jm9jeCC45r0mwel5DQVPVAYS-64Z0BdVjEWcXgC3E_OzRynJexKDcdEgjuy6-WC3PGZry0cv_B9sGl70TPVwjzTB8gDczY6X6YUs1zxpWpHqiaBTFCyeYlnOH_zX4oF2puqTbJlSnjCYD9VfI_utjz0cjv3LDvsn-40wjeaYDlnKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تیکه سنگین امروز فتح‌الله زاده به میثاقی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94214" target="_blank">📅 18:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94213">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔥
💥
🏆
آفریقایی‌های خلاق این‌شکلی با موزیک رسمی جام‌جهانی ویدیو گرفتن. انصافا‌ خیلی خوشکل بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94213" target="_blank">📅 18:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94212">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80aa310d96.mp4?token=fgNxCpClDgPOVM_rkhyCE27PlneXjCoPTxWGGacHr5LtzZnka0H9nV1yBrfWW2qNAIdDoCWZePPMtS5z_Yrz3muWuAICC6rpKJ3gPQZTWibbn5dumC-NS5qEWVuthcpqJOHcZ7ulP0NGl2U4Go5MGHW_o_mwsE9I8BPLFqCBbk2mkjy989ee4TfxjZrm9bNeuFYJkcBw3sOWbAJ5T75vBA88glB19h4Kzs2yGcfxK4FD9sz8JgfNCPzP32LyneZWOqWLXuuJHtIGhWzTdIui4wytTxvLXU8XQC9D56RSmf1rmbtL3WkW7GioedoXEOJ9JxoPuMbdYt48H1cqBnAnhF3r0WbgJqz00ul24krPbEN0-R9dJAV7vlIm4INcqDIr_x-l0mlcXX8ZyZmxUhjJwS5FWMzhxOCoAyLmI3hXcftlzr14qB6zgpGC7xxs77U9IU-K6Fm2dGJEbNCJXcpjdyq7nr6a7GoQJWvPv2X4aPnVkhMkw6j1AsWQ2EzjbohyowqL6Y2epz5ET63ocjRMHcNxdXccvoGe95vi6bbtXMNXNditGOar32pvgblquDrM9WM8vCcQg3REzkNvAValuIYT2QKNaR-OcoT46kuiSGZ_35NeumkQZinqoGPFIHQwiBc0qThmHyo2bA3x_57Jv7OfAw4EWYgOVXTOWpTzJ28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80aa310d96.mp4?token=fgNxCpClDgPOVM_rkhyCE27PlneXjCoPTxWGGacHr5LtzZnka0H9nV1yBrfWW2qNAIdDoCWZePPMtS5z_Yrz3muWuAICC6rpKJ3gPQZTWibbn5dumC-NS5qEWVuthcpqJOHcZ7ulP0NGl2U4Go5MGHW_o_mwsE9I8BPLFqCBbk2mkjy989ee4TfxjZrm9bNeuFYJkcBw3sOWbAJ5T75vBA88glB19h4Kzs2yGcfxK4FD9sz8JgfNCPzP32LyneZWOqWLXuuJHtIGhWzTdIui4wytTxvLXU8XQC9D56RSmf1rmbtL3WkW7GioedoXEOJ9JxoPuMbdYt48H1cqBnAnhF3r0WbgJqz00ul24krPbEN0-R9dJAV7vlIm4INcqDIr_x-l0mlcXX8ZyZmxUhjJwS5FWMzhxOCoAyLmI3hXcftlzr14qB6zgpGC7xxs77U9IU-K6Fm2dGJEbNCJXcpjdyq7nr6a7GoQJWvPv2X4aPnVkhMkw6j1AsWQ2EzjbohyowqL6Y2epz5ET63ocjRMHcNxdXccvoGe95vi6bbtXMNXNditGOar32pvgblquDrM9WM8vCcQg3REzkNvAValuIYT2QKNaR-OcoT46kuiSGZ_35NeumkQZinqoGPFIHQwiBc0qThmHyo2bA3x_57Jv7OfAw4EWYgOVXTOWpTzJ28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇩🇿
🇦🇷
مراسم خواستگاری وسط بازی آرژانتین و الجزایر. داماد چه ذوقی داره
😍
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94212" target="_blank">📅 18:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94210">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FccbTx7bfMXcnIuE_38POxPCKhgA2nknpxwEIvcDD8Zk-chzEF6XrZVm0cNVcykmOizOpcV9ilxKfZ0UVb00TmQBAUhVKSI8c2rPQXf5o4MaQgY0dGlmJBfeWXRkJyyEuaITLGRZ3wTPzsmGp9DMICWYs5xaZF-3Jq_O38xDVxW5ccwP5_OA_LcdsDVylQe-l-R9-OnnFwjpC9iw5SyepDj7EY3jZ6yZo9gREEEUKpIpkCUDuKfpgOUm-Mg4lzn73ou49kuh4IINGdDdYDE5LHFs10h-5lcn3Fz8sVYnOTBb7qsmv4awC4bIYo2ZZaq1hT-SlYQ9GnOwYr91HdR2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B38LmOjwomvgBl88-Fv9cCF80OSXqrHBsaMVRdUvwr7zH2-93vM6cy2jdgkzYjKsNElDKQRUYSYhiHx_if1pVyp9tTSl4MDL6iLxmksblM-PFTfM1w7PvJQgChie3q5Y-u3SjtTVe2dU45vVbiTjh7Z32Iu37chCJEWETfW95g8QtFeyRRg4CN4159now6CIl7kwZYdQ5KA1Ohpo1hyodrSkx0vfRXUZFY1xvIDf4JHwKCDr0JuwwrPlbvPBK43q92u2eOxkc4qQt1LYMjUhqjhHMe_LqSvS0R0NIpksuqtt9QyMnDeo8HNf_pOzieDIrxpi3EkcBWu-0tJVE4pNfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
#فووووووری
از مارکا:
رئال مادرید در حال بررسی ارسال پیشنهادی رسمی به مبلغ ۲۲۰ میلیون یورو برای جذب مایکل اولیسه است. رئال مادرید همچنین میخواهد این تابستان هر دو بازیکن انزو فرناندز و مایکل اولیسه را جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94210" target="_blank">📅 17:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94209">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916898ff1e.mp4?token=n6YILFhyUhlnECE0sAKiz598Uk92QqWfH4vRNSdukF7YpFhRBW09BwMy0Ln010USehkD_YyODI5xZAh9TIW2JT_g4XmkyF5Yt5ArFiQD3WRQ5m-CaGzWDe3w-Whu1KhJixqgQLnH5AB9xaN4wEqoJM_LZzD9a65SnYqBCdZQmMnJ9I5PaGLDfLGxXSWKEUE3wrjhy3Jz6zQePZ8JSlY9Ti968kJnOM8J4OweivqGakL4sPMneHuBfGiyChb7hMhIPz2kcFRCeX8s1ZYSxB0ia6Y2YlWQZ__ZrKnNkp0YGCXOQajbzSUMI8ppGG-tP67RSvBYkcJatVg5b_WJp-NSow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916898ff1e.mp4?token=n6YILFhyUhlnECE0sAKiz598Uk92QqWfH4vRNSdukF7YpFhRBW09BwMy0Ln010USehkD_YyODI5xZAh9TIW2JT_g4XmkyF5Yt5ArFiQD3WRQ5m-CaGzWDe3w-Whu1KhJixqgQLnH5AB9xaN4wEqoJM_LZzD9a65SnYqBCdZQmMnJ9I5PaGLDfLGxXSWKEUE3wrjhy3Jz6zQePZ8JSlY9Ti968kJnOM8J4OweivqGakL4sPMneHuBfGiyChb7hMhIPz2kcFRCeX8s1ZYSxB0ia6Y2YlWQZ__ZrKnNkp0YGCXOQajbzSUMI8ppGG-tP67RSvBYkcJatVg5b_WJp-NSow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🏆
خلاصه هفته‌اول مرحله‌گروهی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94209" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94208">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dc9fa1fc.mp4?token=K6c3WpMtJqtXgjI6lqOd-lG_NPb_PkscUnXXY7EpMgPg-IPF2IICJ7Bmt4WfAYnjui9P0jMVQX1PUp-pl6TlkvapI9XHRRJXj9stUxsxiHgDydAjAkqYbnSafrZReJlYCS8JcdfK-DETgDhYnPXO_91UEB-RpEoJQ158qkVE0CIKt1FoGd13mFoqJwexnFbU3_scrGjiEd9QQvVcEt2k54cybr1izQqmAasCYAxA2v3miRhLaQqSNbEX0DOT7VNHq8s8NC6INES5qPjyoWDtjklkHJITsMSDTq4Iv8S4ghzdpXW_rC4m4LEMNeuplYvsUthNz6hHdDgQB7ITLa0YZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dc9fa1fc.mp4?token=K6c3WpMtJqtXgjI6lqOd-lG_NPb_PkscUnXXY7EpMgPg-IPF2IICJ7Bmt4WfAYnjui9P0jMVQX1PUp-pl6TlkvapI9XHRRJXj9stUxsxiHgDydAjAkqYbnSafrZReJlYCS8JcdfK-DETgDhYnPXO_91UEB-RpEoJQ158qkVE0CIKt1FoGd13mFoqJwexnFbU3_scrGjiEd9QQvVcEt2k54cybr1izQqmAasCYAxA2v3miRhLaQqSNbEX0DOT7VNHq8s8NC6INES5qPjyoWDtjklkHJITsMSDTq4Iv8S4ghzdpXW_rC4m4LEMNeuplYvsUthNz6hHdDgQB7ITLa0YZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🎙
روایت مرتضی پورعلی‌گنجی از مرام و خاکی بودن ژاوی هرناندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94208" target="_blank">📅 17:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94207">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182af5a6db.mp4?token=i_kDuL2vTmT4ZKJxymFttjubani8-hMU3VBqmtAfA_p1iD72msvLGuGWZbUdyyrLZC9D0orKY4RuhDl4R7FjdMtm06of6b2ed4lEvFiYTuyEg9LG-MBbv76rtn0Uuc3nPP0808AI1qNJVRI6MW95lnB7geL64jPlRzmJ7jFHlK_fLsCzE6ZQjj7Cdf45R86mqRfwOJ2QglMl8pgneIy-FGCIR2AzcAKd2dh9gVawBxNYw9e2X5A-cMv0GjLJ1cUZUEYJMo7rrpLxLGWpg4GTnaHT5wPFgzPokcV4pLcCjckb0plKaQbsMadXB9WxYAmKChgUb2MplcsHeUgZCBbZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182af5a6db.mp4?token=i_kDuL2vTmT4ZKJxymFttjubani8-hMU3VBqmtAfA_p1iD72msvLGuGWZbUdyyrLZC9D0orKY4RuhDl4R7FjdMtm06of6b2ed4lEvFiYTuyEg9LG-MBbv76rtn0Uuc3nPP0808AI1qNJVRI6MW95lnB7geL64jPlRzmJ7jFHlK_fLsCzE6ZQjj7Cdf45R86mqRfwOJ2QglMl8pgneIy-FGCIR2AzcAKd2dh9gVawBxNYw9e2X5A-cMv0GjLJ1cUZUEYJMo7rrpLxLGWpg4GTnaHT5wPFgzPokcV4pLcCjckb0plKaQbsMadXB9WxYAmKChgUb2MplcsHeUgZCBbZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو:
به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رو مال خود کند، اون آدم کسی نیست جز مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94207" target="_blank">📅 17:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94206">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c565269871.mp4?token=rh6XiEIZWljBCu4ljfezMAfVqQFTcJCI0IAeal4hMar4jYqqvR6mL4ppQ15OZsMlJ-_8slxbYflKHDocQfw9hc3mH3WG1QZRzJg8TwkMKgxJcd9yyiLpGuhIHYlAYeOeJXATY3vXBAlO0KMpAljdTTbQNyDFFe_2My2wrALZVicAVg_hWcqr4oEhcbs2T7d-P4IyLI3WLL_TvI_cqEY9jRNqdcISMk2jK9HAAaMxfet_J9cdj1CmDNs0ubXWZN1L2EK8gaW96oF9tMWKZHb5Df28VfwNjHXXCveEW2OljttBR7bpCzcmsLPh9ZY5ybK2yM4MUwxsc2VLgbMloS9vYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c565269871.mp4?token=rh6XiEIZWljBCu4ljfezMAfVqQFTcJCI0IAeal4hMar4jYqqvR6mL4ppQ15OZsMlJ-_8slxbYflKHDocQfw9hc3mH3WG1QZRzJg8TwkMKgxJcd9yyiLpGuhIHYlAYeOeJXATY3vXBAlO0KMpAljdTTbQNyDFFe_2My2wrALZVicAVg_hWcqr4oEhcbs2T7d-P4IyLI3WLL_TvI_cqEY9jRNqdcISMk2jK9HAAaMxfet_J9cdj1CmDNs0ubXWZN1L2EK8gaW96oF9tMWKZHb5Df28VfwNjHXXCveEW2OljttBR7bpCzcmsLPh9ZY5ybK2yM4MUwxsc2VLgbMloS9vYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
حسرت یه موتور روندن اینجوری کف خیابونای ایران رو دلمون مونده
😢
👅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94206" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94205">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvnw5eyJ1pRGKqDkwllOMNLJIettzcBnoEfSfqoUIWFCEHe78clMdxn647U5rKs3VzVCfvapQL4q1HImA_Bx994k7KL8JaocjXAXAK9LBTeCUqNSip2_EY67ZK60oFiunp8_ZmFxcqaD-dhHfNuXStnQ3kqQzvyrTHuT6y7kj1pOVchAsj-BrfqLLjibjNn9zPrQj8mRF1UEvZLBTDJFRRsRYXDbwXILsUPl25U5S9WKVVHR_AV-3ptmflnyRN_ZZ_M2KY41VZQ_2iuozE5vz_2chzfC8i-oHDkO3nz5ZWVq7F-mBbr9FOYmWSyPSeHwFhWzPBl9B4146cl0GcDVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیتر اشمایکل:
روبرتو مارتینز، بدترین مربی تاریخ جام جهانی، نسل طلایی بلژیک را نابود کرد و این برای او کافی نبود. حالا او میخواهد این کار را با پرتغال انجام دهد. آنها نباید اجازه دهند او حتی یک بازی بیشتر روی نیمکت پرتغال بنشیند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/94205" target="_blank">📅 17:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94204">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUeSnnMeWOyrHtPXjcMTus8yqPYN8Bh4KP2wxk5RE0VTemXdxURcYhm2ZPM7oykfQqJ1g8rL7sk4QfHCRzlluyjJNOJXt7fDX59j3dv9CzXlp4kTG7dwvCbNLBksAF5vrq0iEf3PUjA_-e3cvf0FQ0RNNUQKBBd_8tolfP-q6-arCwF_TlUI2qzf3onY-XyA6_pBYaPqfJ5Jb6AMrHRj2XcA52u2rkt2XRG5kNPk1YO034ERdRIUfWu0F9NeL4N2CNYDeInv41drIq9IEARov1gAbsZY4TdJ9k98PNawttLKDMmqETO-BxMmtP85B7UYItocAAtAIEh9QYH5RqGxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فابیو کاناوارو چهارمین بازیکن تاریخ است که برنده توپ طلا شده و به عنوان بازیکن و مربی در جام جهانی شرکت می کند.
فابیو کاناوارو
فرانتس بکن باوئر
اولگ بلوخین
مارکو فن باستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/94204" target="_blank">📅 16:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94203">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7bc36d5.mp4?token=mRXtv-BoidrqaP0Mx6HrsmbnzXkNwvdC2tNxObjPc-oElPerE7AVBeOrSCQWHrJSowTUXvmW9OblsIqmY6FMo_A2Cwf3z0TkdoddreCV3A8QY8okXdRUvxQzIyfU78ktG268oIB5A5GzlzgJWNHM6feuFOqY9_ik7rkECGt0--8AgRR_g5-FFo8qt1eRb6OkglWkL6gErGPYHL9T0gdKChypi5gWfY7Y8TAONZcEOEcBDMrKKx_bK1qPzmAstDbLA_xfFt-TryhSPNxqgKVX18dzSI_ZxADQGmCc61NI-wkd_HVXeWYPNZaZYLxOX6YgEw1Dq307D_IJT37W_MG8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7bc36d5.mp4?token=mRXtv-BoidrqaP0Mx6HrsmbnzXkNwvdC2tNxObjPc-oElPerE7AVBeOrSCQWHrJSowTUXvmW9OblsIqmY6FMo_A2Cwf3z0TkdoddreCV3A8QY8okXdRUvxQzIyfU78ktG268oIB5A5GzlzgJWNHM6feuFOqY9_ik7rkECGt0--8AgRR_g5-FFo8qt1eRb6OkglWkL6gErGPYHL9T0gdKChypi5gWfY7Y8TAONZcEOEcBDMrKKx_bK1qPzmAstDbLA_xfFt-TryhSPNxqgKVX18dzSI_ZxADQGmCc61NI-wkd_HVXeWYPNZaZYLxOX6YgEw1Dq307D_IJT37W_MG8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
یه ماه دیگه میفهمی به بختت لگد زدی مردد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94203" target="_blank">📅 16:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94202">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi-gbulRr-J65gd8Jr5FM321N9_-vkTL-x8u_uQguSlF7i6Yuvg4MBdyYBJVFhmGNbuyBKetDSiRaiO40MgphFNgNdq5ESbVSb5qo7qnKdYMPrUwdbmvD5vLrM1zwNWBuHiGQNnIznWf9liQj4YCYwBEPTqCd7ieBA1KOIH1gZ-huTbt6-6FNj6X8Zu5QeyMcv6ub4y4vqWXF53rNNB1IQ7mJahHm8sCOTq4Qm7XsuP-mGY-RbHMbk0UPUYUqGC1L5dw5kUTSWte6Ez2__1yiczeC4xYVp2kgdfsngZixU696wNEaNv3NbCcNzYI1uUc_CqONCrB_LUXliBOuuzNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل تو رختکن خطاب به بازیکنای انگلیس:
دلیل اینکه این پست رو قبول کردم خود شما هستید. هدف کاملا مشخصه: قهرمان شدن در جام جهانی. باید از همون اول درباره‌اش حرف بزنیم. میخوام به جایی برسیم که قوی‌ترین تیم دنیا باشیم؛ تیمی که هیچ‌کس دلش نخواد مقابلش قرار بگیره.
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94202" target="_blank">📅 16:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94201">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxEUbJGjxkEf7F40QVvcV70OT19wqLtaytFALEjc3HCgQ6BkIcRnJ4U_R0rgkuB7MnIs7bEY7Zitvkhhl1c3hDfudbgv88-mtNePK8zBJiqo2KbVnzlULKPOsRjjdCRsnm4C7XjWsDF354uMNWOrkTMsYPnaklD_0j07qh0UGe70h92rKFbmPwqw_8UutouMtO4_VT68A-wRfcRJgv8kX2vCv9Im_4NtXtWDrKcqM8ZqKXcEwfvYEqXdw1HkfiGHiaG3bgHeqp4IDBFQDWotR26qNa8YHW-XhfdF0brG-NMvvyU79Tgu23jDaeFsPSed9seSHSVpO8wK1CegSC_nEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خواهر کریستیانو رونالدو:
بازیکنا انگار یه‌دفعه یادشون رفت چطور باید پاس بدن، توپ‌گیری کنن و حمله بسازن! تمام بازی رو به عقب و کناره‌ها پاس میدادن، ولی اشکالی نداره؛ شروع بدی داشتیم، امیدوارم آخرش خوب تموم بشه.
🙏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94201" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94200">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTQaSUaSR-XPYofidNaVmZ02O1by8surcdsii_dfVsjDOGeMahXkBS5Rfd9A1IrvlhAohoGjCEFCUCgjbSxHuMbpeCZnjYeN1-MgkyVWSXYUPz4P96YpmvP6J64lKcMc_yEhzkvs2oLBoS5jZpPdcRBCQY253xtpe9OjvLnQwc9Jy6giUeKMfz7BmGADvQR6fkoMjlaKHAZsTRbMmHgUKRWotmWM91LmY4tov7vfZTp1asG3_gt-Sv_4b4xM958NuJW5cpHUjh61NnESy--HPwVDez9aJIsrt0HyYDiKY9uM3ruTb7n7VoVxWEyXVi69VjU3__iLkrFQVciIWOy6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله
جیمی کراگر به رونالدو:
مسی مشکلات تیم رو حل میکنه، اما رونالدو ممکنه گاهی خودش تبدیل به بخشی از مشکل بشه! مسی سطح بازیکن‌های اطرافش رو بالا میبره، ولی رونالدو دیگه اون تأثیر رو مثل قبل نداره. بازیکن‌ها رو باید بر اساس چیزی که الان ارائه میدن قضاوت کرد، نه افتخارات ۱۰ سال پیش! فوتبال بعد از سوت پایان، به گذشته کاری نداره؛ فقط عملکرد امروز مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94200" target="_blank">📅 16:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94199">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b65f43b16.mp4?token=us_RapEE4cYsU0szxaGyrrtEhjzfJ1HpjLO5_nCQmpm3z8LAATNlWHC9WqLjqB_4DDKvGggEuJ2G15vXP6CzojGdFgYSjlwWj4MufEB0dTptZRuqY8XhS2G3vABN_8kTU79WWNj5FKfQvr9UGrGqpy9ivQd1cQ2oVCwKTcVMJWyYuR3xe3eGDAHgVlZOViBK6xLdnLnZ3y89Y6DxaNRlZUVNzV4iShwFeOBYhjHx1K1dCzimo5Zat1PtqktgftyY99c-1sib4Z5NZNY6jaT3LQtN6YK_FkhuJhb8n6M98vQswEjkbAWLqatMSeIvGxuXnGS9FU_MKNGrVan4hT78hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b65f43b16.mp4?token=us_RapEE4cYsU0szxaGyrrtEhjzfJ1HpjLO5_nCQmpm3z8LAATNlWHC9WqLjqB_4DDKvGggEuJ2G15vXP6CzojGdFgYSjlwWj4MufEB0dTptZRuqY8XhS2G3vABN_8kTU79WWNj5FKfQvr9UGrGqpy9ivQd1cQ2oVCwKTcVMJWyYuR3xe3eGDAHgVlZOViBK6xLdnLnZ3y89Y6DxaNRlZUVNzV4iShwFeOBYhjHx1K1dCzimo5Zat1PtqktgftyY99c-1sib4Z5NZNY6jaT3LQtN6YK_FkhuJhb8n6M98vQswEjkbAWLqatMSeIvGxuXnGS9FU_MKNGrVan4hT78hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
خبرنگار: «ولی تو در کنار کلوزه، بیشترین گل رو تو تاریخ جام‌های جهانی زدی؛ این عدد و رقم‌ها برات مهم هستن؟»
🇦🇷
🎙
لیونل مسی: «نه، راستش نه. واقعیتش اینه که خب باعث افتخاره که اونجا باشی، چون نشون‌دهنده ارزش کاره؛ اینکه اسمم کنار کلوزه باشه یا اون بالاها باشم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94199" target="_blank">📅 16:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94198">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2d6b9ef8.mp4?token=aDW4qf-euuz9llkwIFwB0ep0HZ3zPqnJyFs27NIL5cBAcFmMtFhwOwcqEQx8gRIysW81usrpjBy5lkrXa-Mh_IxJOo57IL1snCriLSgSePceiPtoSisG8IHndKxD_5YLqS_K8y_YFr93jbkbQJmWUVB49fc65ciWKMbTy0kr-uR_S1geeQFeKqhQ_2FyhTMUv9LH_JZszhjflFzUCtddtxCEvwm_UrFy3NHvUfNfz9A36g11oYNNJH3evLuw5_nju7wD5E6gotOXvTYXaUiYsxpC5z7gQLqRfy4FgvIMUO4TqL-B_KC5H_qUgSu2ZyclUAMkDoze9UfYdpD1q33uL2yrrW8E_AVmDuiJqYXNJKiYZ6vKM1Zmk6VJl8zAAoBKNX1N2dWPEVp_MeqWOIseEYOwEXcC7hhjOJi_HWyCMWbrkD0yeJxALDEaGN-FInw5cft0boAAD_L1ztUpciti3OVnryYKgW6m1AEjSWcpJmD3JqneVxUyuL92csBYgET5-hVF-b8iGl05NKmZt2Q76Y5_Ib6XMuXbJv_zzSL9MtrGFTOrJjnelO-TlYW9Ay6xgnUKoD47xgZ9_EInMePXHmNEBczeXGKV4qOOVDl6nbsKjuqoY-LE1ZzLVZAC78Ow-C_BnCMif17wk20TeLkrcEDWQ1m8bAzsh5VwksUMD9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2d6b9ef8.mp4?token=aDW4qf-euuz9llkwIFwB0ep0HZ3zPqnJyFs27NIL5cBAcFmMtFhwOwcqEQx8gRIysW81usrpjBy5lkrXa-Mh_IxJOo57IL1snCriLSgSePceiPtoSisG8IHndKxD_5YLqS_K8y_YFr93jbkbQJmWUVB49fc65ciWKMbTy0kr-uR_S1geeQFeKqhQ_2FyhTMUv9LH_JZszhjflFzUCtddtxCEvwm_UrFy3NHvUfNfz9A36g11oYNNJH3evLuw5_nju7wD5E6gotOXvTYXaUiYsxpC5z7gQLqRfy4FgvIMUO4TqL-B_KC5H_qUgSu2ZyclUAMkDoze9UfYdpD1q33uL2yrrW8E_AVmDuiJqYXNJKiYZ6vKM1Zmk6VJl8zAAoBKNX1N2dWPEVp_MeqWOIseEYOwEXcC7hhjOJi_HWyCMWbrkD0yeJxALDEaGN-FInw5cft0boAAD_L1ztUpciti3OVnryYKgW6m1AEjSWcpJmD3JqneVxUyuL92csBYgET5-hVF-b8iGl05NKmZt2Q76Y5_Ib6XMuXbJv_zzSL9MtrGFTOrJjnelO-TlYW9Ay6xgnUKoD47xgZ9_EInMePXHmNEBczeXGKV4qOOVDl6nbsKjuqoY-LE1ZzLVZAC78Ow-C_BnCMif17wk20TeLkrcEDWQ1m8bAzsh5VwksUMD9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
🇦🇷
حاجی جو ورزشگاه بازی آرژانتین رو‌ ببینید. ناموسا چه‌حالی میکردن با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94198" target="_blank">📅 16:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94197">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cdbc7c6.mp4?token=UVEhOSlevnIYxKozqRpexFc3V2wzMwFq0zl0BEaUPBZyr5tXAkRzAzttTqQJ9ou875ac2mGPOgSHZCWAvvXOkCD2wQVDAz8Zw9NRyyTjwqdgfv4PE1K1vW775F0qMOXVSEvBU_agp6-1JyhGPIi_nC-s0cdgiEIBrFr2cdgw_VpC1TKr8LJBRm_zmjPrRhLyt4cgHxGrezD2hTMneY2dOT94H84Tu5PlAI7evfiv3Y9hMqnQo0b5LQSaVJNp53s323el84oLmnayxLVc19fBxx4hguezEdLLF4dHo_JgBO04df-8u9gI3FycFxfJRFQXSFGLl0ryxM4H9HE_vjbEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cdbc7c6.mp4?token=UVEhOSlevnIYxKozqRpexFc3V2wzMwFq0zl0BEaUPBZyr5tXAkRzAzttTqQJ9ou875ac2mGPOgSHZCWAvvXOkCD2wQVDAz8Zw9NRyyTjwqdgfv4PE1K1vW775F0qMOXVSEvBU_agp6-1JyhGPIi_nC-s0cdgiEIBrFr2cdgw_VpC1TKr8LJBRm_zmjPrRhLyt4cgHxGrezD2hTMneY2dOT94H84Tu5PlAI7evfiv3Y9hMqnQo0b5LQSaVJNp53s323el84oLmnayxLVc19fBxx4hguezEdLLF4dHo_JgBO04df-8u9gI3FycFxfJRFQXSFGLl0ryxM4H9HE_vjbEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلمبیا با این هواداراش واقعا شایسته برد و درخشش بود و هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/94197" target="_blank">📅 15:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94196">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7zzqnUQ_Lah1IH9dsFfXvBx_iidVZtFvrle-ZIqx5B5lY39ur5ccgNXdjM8b78srptD9y42-07FoqnEwvT7N0JSgbXgVlGgjOk32I0ulImojmzdRZZ6j90xmCNE0jaHVQxdJlYKqyNDcWjNpGiy0_b_culWBgmz381RLEOMpeg3lyQvz3Et5Ci8zuuCIlRN1gaNvjuKvHfi2m9d-kmgE5yooXCOUyrOhpfEmF57gjiAhhgPC0ymfJ2B0RFBAdNBP5NY4HpAUQc-ks_EfY00nwW4GIE_AhtOzNuHE838FJCG1l2GYCLJSlYTgpJBUKJpgHh5aQfBDeTjfU1P_xHS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
به گزارش موندو دپورتیوو، مارک آندره ترشتگن و ایناکی پنیا جایی در برنامه‌های هانسی فلیک برای فصل آینده ندارند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94196" target="_blank">📅 15:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94195">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65efc6e80c.mp4?token=NQ2DaTHsuSLyKAYIUQJ6bvIjxvYaVHqyQdeiIGuwgAmIBPkV-GFTUMKDUJREMKCKCn4A5fBHC7OkMmzGOjPlezp7z0_tEtkBxE3LV6lqqeLd1eyVTko5RupD1P5w_RiAhnyIZEzs-5-FnycWZVeHe6IgY4D5v6SxdEV2UuVHk3ALFjADrDW1YGrYQQMPHTrfQY2_XKf2OZCKWMnfzzc-3tpFyjuAGE2fLtsfvJmLds1vMcUA3XcrcCmTKFx9fR3uCpUJMZYz92Dwr2ZVi3Awkoh6nglKvza74bDN_PlQdw5xpyP00I7htR0mqk19-BWiIi-Xzqk-uIPMdQWPLtEomQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65efc6e80c.mp4?token=NQ2DaTHsuSLyKAYIUQJ6bvIjxvYaVHqyQdeiIGuwgAmIBPkV-GFTUMKDUJREMKCKCn4A5fBHC7OkMmzGOjPlezp7z0_tEtkBxE3LV6lqqeLd1eyVTko5RupD1P5w_RiAhnyIZEzs-5-FnycWZVeHe6IgY4D5v6SxdEV2UuVHk3ALFjADrDW1YGrYQQMPHTrfQY2_XKf2OZCKWMnfzzc-3tpFyjuAGE2fLtsfvJmLds1vMcUA3XcrcCmTKFx9fR3uCpUJMZYz92Dwr2ZVi3Awkoh6nglKvza74bDN_PlQdw5xpyP00I7htR0mqk19-BWiIi-Xzqk-uIPMdQWPLtEomQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
کف خیابونای بوئنوس‌آیرس این نقاشی و بنر درخشان از لیونل‌مسی رو نصب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94195" target="_blank">📅 15:30 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
