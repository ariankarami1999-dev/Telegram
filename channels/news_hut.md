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
<img src="https://cdn4.telesco.pe/file/GtgpS4OSr6-C3lKDcBTpU0TTIzrlOuB0-an4VuSbr0DROZgN1gtvmWYdfD_V9ATD7KXqbp_IEQRXEBe0BmfzoDtujY1DI14xTM37MwOM4nkeg7BZp6guvijfJb_YWpMy8ZtN7jDLejTy9cHEffsNzOL0U-q2pACYNvSMoweHj8l7IdJ1BAjKQ8l48fMnOPQTcv3iWcprBh0r75E2oIIC7VIRGNQX1nkH2iIG8bG0YljPFRw_H--WsKRujNw-GiXM9nENIxq74GuBRARD-8tmrA-mpikxcYiMHJw-IqQpnYiAFcLa2W-pstEvb9couoX1bHzYQikI6UACRdLUpUVi1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 21:36:08</div>
<hr>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=pagtbWNGi06q7SvHMA92r0tlSAyzPgUIuzyfqLaysrrwTmlGDDwtrJLlJrwC0nH8Hy0HhSHaIEkOrbkGgwreOgeNHtgq15CRGyEBFRgVCGprCrKHEyZTPubFxIdh9mG6Pq3fscYIoL3Y8s_Vqv7dU0rG6SUk9DO7cviZGXnoHm7-3aApWuHvQOtBhoMkfmsJCLkh52BigiUIkujnf1UMb0KTeBfeseMR4VpX2VHl0ktjA-REf-pjw8oh-XbiClXFfhiTF72lXwHMoBYze6ZQscRM_9UHBxZDkXYTfVAuR1NKXK8LlwMpWJzYQAH-LfJE-mheDdn0yv3v4YvJmua1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=pagtbWNGi06q7SvHMA92r0tlSAyzPgUIuzyfqLaysrrwTmlGDDwtrJLlJrwC0nH8Hy0HhSHaIEkOrbkGgwreOgeNHtgq15CRGyEBFRgVCGprCrKHEyZTPubFxIdh9mG6Pq3fscYIoL3Y8s_Vqv7dU0rG6SUk9DO7cviZGXnoHm7-3aApWuHvQOtBhoMkfmsJCLkh52BigiUIkujnf1UMb0KTeBfeseMR4VpX2VHl0ktjA-REf-pjw8oh-XbiClXFfhiTF72lXwHMoBYze6ZQscRM_9UHBxZDkXYTfVAuR1NKXK8LlwMpWJzYQAH-LfJE-mheDdn0yv3v4YvJmua1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8KMrJMrSqeADz7xqtE1sehGPQyw16MYXOFOEDeoDFpfuFfBwCp0Jh_S3ztInHcyI0pu97wkNj-et4mza45BQLOgeB1MVoF3IcLcpu1il-Dxy_4yI7gqjcc1_S9-v0oFd2lchmM8dlijFIYV9K_lzegZ6qWGHDlOZT55SWrNH3pTlquM42F1vBQUX5ftlzH9m-iJJCNwA0lWA8dkn421XqtTsHUGnqrRDh8qjmmG7EphqualUHs4BFe3OYvtHdY2rsyGpffotgZwAqKpiXR9BpGMG5mTQL0iRyHoJoHGWBe5-ngGBWAnvm41R-N1VuV4vL_AFsV2-P1rmF5ugKWn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KV8yrRWd6bcOPlPLHkmTl-itH8illelxyH99UavFuI7Efgr99T1Bq7DGyeKYahg2tVBexklkpuvRBkzbZoSbbgsKUc62F2eTqOQHAr7zZJNswCCSmb3y0XnUEPNjtdsQdiD3khIws_TrQwYI8EzA3SUiBg-bUsYOQyTNv76lgcbOeJelrlg1Q18-Bv0X0lAn9-v4y3KWmrEg-WDUSv0udfe55wnZa6n8iHpmUVrL-xjsuqoZAsDID12-TSgnXyxELiHZj5rRFQRAX8PUZN7ChHYIFzZtRf-u1lfY70NA_ubwmRU-BA3ugEMBpc8HLGcVaEJlMwlCd1xZEEWh4o-MKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAM3pt0tJaht_Ro9SDqWpeYfByIHM2e3Dp-IvWnuviXnS6WfnJ_72Uftif7uCvs7oOLBeicX851YIoCcH7nWM-F6xijCgibwaUPAIDFTOQ3xjwa97MjG_4Yx6dPv9eenM75veWkAVPKcMHbxiyxijaw_r7j_4nvvmyBcnY2421-LkV82T4-xYJuJ4eBqulS2TYbvc8FTPxJkBpmsPPryLRbf_hf37zbxYzl3b9tUqZnzh6yuJL8Vde3Kh_0NwZpktVJosYYhb3Rl0jEtIjE-sbq28mSpyyzHhhO4R5gIFyjEWsFa7JUwg3BrCQb-43bco2ysORNIVCSQV4xfB2qw1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWXqgtVdeEtlH480L06Tcgx6i_FMRLuiiFJgJp5dA9t_1dd9HCrR-akhDqi2PLSC2fRod075ShkQpFZq8ZSaTTiK6WGfzzCvkLIRU8xVBg9p_LoZbc-Y5pvsgZOqRsYdrNiRC-8HaWNRjdBtZcGO6Cuej8f7ZFWXMW3BtXgaRk-wH5AxLZlB16yUdenBhrFPvA62JsMT4VPF88o0TTbja4zsSZrnIJw5YnjZfczrJCz6lU5nEJ8aroU6j_352vFYS9UBs2VHlnQM0duaL_c6KuWWU2CmRSOpLMMoUY1BEexjoWm5k76PSNSFe-mHgExnoZI0j4Xp8DYbLGQYuy9fXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quxvzbJAjYCCk7ecuy_ywPjqHeKQDxqHJ8BVnqc7FkU0kNqinZLdE82eZOMb3FO2eSP7GvPgrB7KXueTDm2OH0s5a24-2YJYyDkpRDS8gN4BDXrW_hDrpgy7warZOTxGUpedHV6ZpJM0LBbnb5zEDI20DfVx0V6vwrudPqfyGBRcEOtm6WQDrFwohpyGsAyq5PpNP7gU-Jwimf5bfVgDRsF8L_5m8pfguFlUN92dK3dbrcrmFkkRhTvgU5p3JpMB3WYUZ3lat2BUEHW3mupHBWG6xCVa25_XRvQj1XFVQDsOT7AVzJrlYo4IHfF--2-kY6hzovOFb3na_x3EJXk5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=BPdQu5xi-GjZPCuQ-jqOzv2g0mk9YVrl8ZUm2uscfewlr8zXFaFclcii6uVCvPeqWhGI5du0eGlDz-MiamlwFg_jh_q01Jv9N98zZgyEGwLiBfjVrdo-FUE_Lt9yvJoMK5Z11pjZKH3EQwMXyBEDv78DigQVKp_Dw0-rGxQUW7TIdNvUy6sosqmGhwjzU8mKWpQpjGNv-jGZ8pANqMZ_SOrGomOcIdzeMorANfLbqH3tvKsN1s9ymy-Gjh4Lw2CGNZhcQhvfr7yyITmMCMT5JRZxpJcQE8qJHsFIb9F-4NVlVZMTXauqdNXQHdRjvGy6H8LxaQTH2NKrJ15gqV3Whw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=BPdQu5xi-GjZPCuQ-jqOzv2g0mk9YVrl8ZUm2uscfewlr8zXFaFclcii6uVCvPeqWhGI5du0eGlDz-MiamlwFg_jh_q01Jv9N98zZgyEGwLiBfjVrdo-FUE_Lt9yvJoMK5Z11pjZKH3EQwMXyBEDv78DigQVKp_Dw0-rGxQUW7TIdNvUy6sosqmGhwjzU8mKWpQpjGNv-jGZ8pANqMZ_SOrGomOcIdzeMorANfLbqH3tvKsN1s9ymy-Gjh4Lw2CGNZhcQhvfr7yyITmMCMT5JRZxpJcQE8qJHsFIb9F-4NVlVZMTXauqdNXQHdRjvGy6H8LxaQTH2NKrJ15gqV3Whw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=bbalWJXusDVvu7Svt3osCUTP_EmeC2MCsJ48HAW8A08hDESQENvLi7HhqPNzT5eMmenMAO-29cRUdX5x9VsBdNMmQLwhRulLeaj62KMICXdS3MHJtD2hz9jgPHcm48YwuEcPcb28-0n4uLHEkmPJZDqB0XPQyQKzpbx6r4nyuTudCktOoh2-PkCV-mepIG7harJ0tjF8T3sAgcgfbBdWyNBVJ8zw2oEX9o4PvrpLujtyuVyNcGlpRRvMVzUR1YYWF6fCgs0Ix2JlVz480mFrmZZtraGP-ef5ntijsQBNZEUN5aumUF3s__DILN7vDJvDZLpcJ7aTFS3pY4KTbeaH_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=bbalWJXusDVvu7Svt3osCUTP_EmeC2MCsJ48HAW8A08hDESQENvLi7HhqPNzT5eMmenMAO-29cRUdX5x9VsBdNMmQLwhRulLeaj62KMICXdS3MHJtD2hz9jgPHcm48YwuEcPcb28-0n4uLHEkmPJZDqB0XPQyQKzpbx6r4nyuTudCktOoh2-PkCV-mepIG7harJ0tjF8T3sAgcgfbBdWyNBVJ8zw2oEX9o4PvrpLujtyuVyNcGlpRRvMVzUR1YYWF6fCgs0Ix2JlVz480mFrmZZtraGP-ef5ntijsQBNZEUN5aumUF3s__DILN7vDJvDZLpcJ7aTFS3pY4KTbeaH_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نفهمیدند رفتنش فقط پایانِ یک پادشاه نبود؛
شروع رقص طنابِ دار و بوسه مرگ بود.
عکسش رو از اسکناس‌ها پاره کردن،
و از همون لحظه سقوط شروع شد
و نسلی که خیال می‌کرد وارثِ آزادی می‌شه،
وارثِ تحقیر و فقر و چوبه‌های دار شد...
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=lwU8DNLGsBfraOIHBq3_lQFiWKJb_zkBSSRqqz6DLzDo-NxTvGpHS_xrjWBOELJ7OG3O-LxC9cxruW5o0h6RmBliOGruki-4w2XowzZZb_O7vGAvNyY1cSwYNhnfyWfDtATCPAZpoIFiKw0BeEny4fsiU7eapekS_uqbXfZJZziaZYI7GqJ37TXPy7jMU0vGGqwugiM-OqGYdMStoi1mzHiPow4yc0fmeKi6x3PVeZ-6ucBGUexOuPqG5uqe9kRt8_mnJkroPyC3rQIm2oL_R-WDJ4x27AyfZ259b-B216fscCk9yDFd65-MlRU79EFm0AYcn-qofa3XBgXa_6VjHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=lwU8DNLGsBfraOIHBq3_lQFiWKJb_zkBSSRqqz6DLzDo-NxTvGpHS_xrjWBOELJ7OG3O-LxC9cxruW5o0h6RmBliOGruki-4w2XowzZZb_O7vGAvNyY1cSwYNhnfyWfDtATCPAZpoIFiKw0BeEny4fsiU7eapekS_uqbXfZJZziaZYI7GqJ37TXPy7jMU0vGGqwugiM-OqGYdMStoi1mzHiPow4yc0fmeKi6x3PVeZ-6ucBGUexOuPqG5uqe9kRt8_mnJkroPyC3rQIm2oL_R-WDJ4x27AyfZ259b-B216fscCk9yDFd65-MlRU79EFm0AYcn-qofa3XBgXa_6VjHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krxVMbbD-b9Fwuz5FsKZYNm3kNf1p5lhEfLs70-VF1Kcg2WBkBzfKOssYd6S-PqKQpZtZAGXN1rBW6az7gcvP2VfMV-ADOhTaPteip8aY1MMIz_oaE-bK4qLWJnsbBh1oWAuvUeAlYNKnDowL0AJVZjHiQLVMJeL-QnU3fTpC2onudC2Yu-rl57_R3Ka7wJooaA7zrkae1DiLZ1s8N_eBKt_I7D8afpybqyk2VQFr04OqFZK_flbrl31s0FLIuqS5OKCBeqT0MYg1OOH-WMl_oQLWPf2QIj1w-mrS2CskYHYqNukBhFxyOyfDBdlCO6O8sTZzow5CPtENpsoAzuDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=m3lcvhFppsqx7nOibf1MH2AX6CoKq17Vlz0JbFbGJN0PdUc7Bpbmds0sLVib5qYHL1qqW_3zfrmGo-apX1ZBimtPDq-KI5mTyOh0VVQu4B4twLEpAD8FELD5tby84xISQ_PVXK7dd6yp7rB9BUcRYqNBLXiEb134hm7pDIE9PGaykQ8KakiE1JH7gQ7S-kqcAiDF9ZpLbOGqMxGcdwnMmdKATvAxglyAvveqrXae33msAfM6a3JAuDDSzzd65uJ6Fff-6dpK2hDVZHsNueJ24W0z_gLSI45Z0zhJq17R5JbUw1pLUpoP7oM2Bnm77IV5ywahH9VXG5PSTst2WLs4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=m3lcvhFppsqx7nOibf1MH2AX6CoKq17Vlz0JbFbGJN0PdUc7Bpbmds0sLVib5qYHL1qqW_3zfrmGo-apX1ZBimtPDq-KI5mTyOh0VVQu4B4twLEpAD8FELD5tby84xISQ_PVXK7dd6yp7rB9BUcRYqNBLXiEb134hm7pDIE9PGaykQ8KakiE1JH7gQ7S-kqcAiDF9ZpLbOGqMxGcdwnMmdKATvAxglyAvveqrXae33msAfM6a3JAuDDSzzd65uJ6Fff-6dpK2hDVZHsNueJ24W0z_gLSI45Z0zhJq17R5JbUw1pLUpoP7oM2Bnm77IV5ywahH9VXG5PSTst2WLs4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
صادق خرازی برادرزاده کمال خرازی اعلام کرد عموش بعد بمبارون خونش زنده میمونه و تو بیمارستان بستری میشه که موساد میره بالا سرش و با گاز خفش میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=GgEkcE6otmZrT3AjNBYYqaIQTfPy7APys7lJol-IgEeCQu0YxrsszG-mPJ9mgJDT73QCEXkGM-sAebkaYj-IGaUgbqX7evJ5iKk09UmOgh2X0pSDZpPbFmVluUoucVj1x9HoaYbtU91czJvxp9AbONMS-Q_8z0ub_5hnxl-we4GpRn8oo64bX00taDFeXXz1AAucC9LdvKaNwra-WRwH3wf2_Tx4Juo4ytYKpiwX9OUuqDlr_7u08ZtyL9DxoVsyy8dAA4EmoLOAg3lx8Em18uF6xJu8BlITLQoxGZg4g5EspbkU2sJpt_M2Hvjew2LCmo4cSCWRU0M4P-ligj7XrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=GgEkcE6otmZrT3AjNBYYqaIQTfPy7APys7lJol-IgEeCQu0YxrsszG-mPJ9mgJDT73QCEXkGM-sAebkaYj-IGaUgbqX7evJ5iKk09UmOgh2X0pSDZpPbFmVluUoucVj1x9HoaYbtU91czJvxp9AbONMS-Q_8z0ub_5hnxl-we4GpRn8oo64bX00taDFeXXz1AAucC9LdvKaNwra-WRwH3wf2_Tx4Juo4ytYKpiwX9OUuqDlr_7u08ZtyL9DxoVsyy8dAA4EmoLOAg3lx8Em18uF6xJu8BlITLQoxGZg4g5EspbkU2sJpt_M2Hvjew2LCmo4cSCWRU0M4P-ligj7XrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=thksge3Hv2N1-k4oh4a7n04qtYbdCBsjdXEo1ZZBsORx6KT58zcBu_u3DkopQv8L40b28yEDWUtxXfoLVo498-6tSguQeCeXlgtUiGl4Xll5xc8QEURtwK7nEKK-BC5M8XXbymPjrHUz83xycjtbZ9J7U8-EJugZphRuDfa-g4X4w8gY7Nn8qA6o4LhDLLCuTTi8J4RPO7eCwiB61bQtNBh8tgqxVbxAHALR-NfMoGPN_Lh35fBCbFIqotGoFevgK8vo10dPqXITY9tIWhevnFI4r2Ef3FgF8MAl3G8ydPIf7b2zO8MEvrPYk_J3K6UGSTgEx3PqtSwqxaz781oAig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=thksge3Hv2N1-k4oh4a7n04qtYbdCBsjdXEo1ZZBsORx6KT58zcBu_u3DkopQv8L40b28yEDWUtxXfoLVo498-6tSguQeCeXlgtUiGl4Xll5xc8QEURtwK7nEKK-BC5M8XXbymPjrHUz83xycjtbZ9J7U8-EJugZphRuDfa-g4X4w8gY7Nn8qA6o4LhDLLCuTTi8J4RPO7eCwiB61bQtNBh8tgqxVbxAHALR-NfMoGPN_Lh35fBCbFIqotGoFevgK8vo10dPqXITY9tIWhevnFI4r2Ef3FgF8MAl3G8ydPIf7b2zO8MEvrPYk_J3K6UGSTgEx3PqtSwqxaz781oAig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=XLfulJ4yLvKWk7dBQ8AgbM3h5Iplv3r-LIX0dhEaP7jLNUh7eZ8QfKa0-KINZSu53ODlhl62WYvPFB9k9ezu2dwDXNrdKxkPtWOs6NutL70mCP5fuTeA4La5OVB-7wPVZAS6bRrXQyMLB7mjPQfnSPSTXBas7xW1mrzT1RDT8WJYhFko70xGR-ozcGb1-bk-86cAYvmjjHrm4XgCP8Ib278aYNNsHLZ0g1DOZhlOzUYYTVCx7X2Ho_gi_tYpHWzQkXK-j-d8qZ659bN233KhR7v_q5SLyTVud_FvlQ119fWqdleabShvIqKK7aFoPEhvSDLkYFhZVj1T5wWSrvlcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=XLfulJ4yLvKWk7dBQ8AgbM3h5Iplv3r-LIX0dhEaP7jLNUh7eZ8QfKa0-KINZSu53ODlhl62WYvPFB9k9ezu2dwDXNrdKxkPtWOs6NutL70mCP5fuTeA4La5OVB-7wPVZAS6bRrXQyMLB7mjPQfnSPSTXBas7xW1mrzT1RDT8WJYhFko70xGR-ozcGb1-bk-86cAYvmjjHrm4XgCP8Ib278aYNNsHLZ0g1DOZhlOzUYYTVCx7X2Ho_gi_tYpHWzQkXK-j-d8qZ659bN233KhR7v_q5SLyTVud_FvlQ119fWqdleabShvIqKK7aFoPEhvSDLkYFhZVj1T5wWSrvlcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=B__oPwVIHAMh4iJW5hYctSkBUOZh7ajiNt3BgeBNo6WcQucmqpvbYA1wwoeaPmUhLytLTsH5E3jjGObZlM1ub9jG9eV2_bYbsMTYarr5qeiOQuauaTA0OPszAEKXs70qxbIrbbKM9a-UPJQDNW1Z1nLL_Px3w931nCQEsJ84ZT73Zha1b6pfpP_gupjrxcoQKkk9s7N5wFmYM29E9r88dDOBpbiB0XQtxDU8ls9lwHKxVvn14Do5t63we2MMItmy_SFfBIKQEoCgmEnPyKAVDWH3gyilDXoKU7SL8HDcg9_iUfryuov4-HlW-cQ7qSV3YD3Z-9Mb_Sf4gRr9gzGjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=B__oPwVIHAMh4iJW5hYctSkBUOZh7ajiNt3BgeBNo6WcQucmqpvbYA1wwoeaPmUhLytLTsH5E3jjGObZlM1ub9jG9eV2_bYbsMTYarr5qeiOQuauaTA0OPszAEKXs70qxbIrbbKM9a-UPJQDNW1Z1nLL_Px3w931nCQEsJ84ZT73Zha1b6pfpP_gupjrxcoQKkk9s7N5wFmYM29E9r88dDOBpbiB0XQtxDU8ls9lwHKxVvn14Do5t63we2MMItmy_SFfBIKQEoCgmEnPyKAVDWH3gyilDXoKU7SL8HDcg9_iUfryuov4-HlW-cQ7qSV3YD3Z-9Mb_Sf4gRr9gzGjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgC2Gh9lAPm-Sytlwe2MJTZn0rqvEs3J-UCCWAPQrj0nk6V4ZkS58U6al_JP2ND2Q4Y87FE0ldZt8J3Xiyec8Sxd90KdvKgTYbDcym4oF3igqADc03jFYzWqZNELx3H9ctOfbM09GKwN46UusthHhmknOZO1NuOZ7qrarPkPJdi43TpuDlFXA6WHTGhclawMrmnm9sDLQJ_73i1LTO03BacuYhZtnj4Rp2ZlM0MrmXAcU5WNs46JXijcKFYel5x3_ystu__2KakJ_jdEXMIi5ErfkKpMwou1vSqsJVfTKqF6ulhoD2JopNVfjzPh-TYPwHZVuRyDILZwTjHYX6EsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuVa4pik5EfxKduS_tZMDPZQZmR0FmuHUqNZPwjLmzCTCysUaFlXvbWe9RtnOeuVecweDvbNo3EKJ8SLNa7ceVFmHrIFwEVNDOc2umjrie3zAPvMAFKR7QdzrJPJMh5RKfv0xTbQgSfKDXqarxmMNjCNyLVv55PEj8zabG_ekIBddlfA9saLnlK66DJpq36Z_wN38m37rArC0WTewgzyp5Tqx9BMNe9QwUWVrNy0qvdTE2R89ZYgKFbDjNB0D7d3MlZAPF2jrJammzPL45Oaep72HtyB-H9aehmyqH9Mvxob2tmRJoTMebg8rBfYBvQc4WJxq3FPwHEi9AD2tRJPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvWRSqtPgJWEfT1gkr_wSEesoZpL8nGvhH4NcMUpsB31gE_Lyv85edsGJuXtiOXPZdAXipPfWsjloB1n5i1L472bCmQfxHOjcH6H67k_CGjgIwzkJpiGBiSqxH7BG9skAlyvVcQgL6QgbfoYbSc_6JEob2SPj3O7H8_4ioDTHhZNr_2vDJK-CXYnsF5TDavFFhYD1Ds7CI-VXq8Ic-QOXiaJKOembwg4uPE9hNeLrho8c0qi5-f7Lw5ck2yY_b6fGsaqUdqv5MslcUpiSZMhWlEmEfafS-QfdUPf4SdTy2c1rcjk9aDfdVTfZtYdJvMl-nkbi4w66FKaeqoG-H_r8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=bynGzpRYPjR8mCLsLwumKO0O17RBUGUCAP4Bc0HyzoE4NRQIZSe3T606qyWS46_T1KSbWB5DCT4zTazMZGnT4jfvv_ijhsmSzrnhrEIvsC_bkl9AnTb2QWq7l3_VH4YHzQAIy8MjhVuCsDdnRTQv_4F220VA6tnu9nh9v8I5i56q_ELelmP3gFNTnf0JkXGN1RmncW-U-tJZzl4DPTNnYG7fWO7-D1YNrDAx8jW-h1RXLGweQscT-xitxRI_vDl36-fWfjIFLhuvQm1iOqftngGFMM8rdqbxcKqpxIIq7u3gjmrUpTF_PBCU83oQTGq1_jxf427W0U-b5dgOegeWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=bynGzpRYPjR8mCLsLwumKO0O17RBUGUCAP4Bc0HyzoE4NRQIZSe3T606qyWS46_T1KSbWB5DCT4zTazMZGnT4jfvv_ijhsmSzrnhrEIvsC_bkl9AnTb2QWq7l3_VH4YHzQAIy8MjhVuCsDdnRTQv_4F220VA6tnu9nh9v8I5i56q_ELelmP3gFNTnf0JkXGN1RmncW-U-tJZzl4DPTNnYG7fWO7-D1YNrDAx8jW-h1RXLGweQscT-xitxRI_vDl36-fWfjIFLhuvQm1iOqftngGFMM8rdqbxcKqpxIIq7u3gjmrUpTF_PBCU83oQTGq1_jxf427W0U-b5dgOegeWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlf3k9TXdq8D44ve_uadCLO5tJwOJMbkafc9XA6e6ITVCvjqOgP4Ln681-ffb2P8hxEq9KPQdtfoictJbf77s8tFiz91JzG3to4o7cf58YM1J2cQMhc-0sFBHWoZXles4PGF3y172UR7QIN9zlGpSScw5vp-x7JGmebZyvScbzB_Ij2XIcWbCaB5SWDCER6GzkZsdJg14f_KImnxIA2u3jJKyi-9nr1qt7gFzxjiH4DDuDd2bmD7fpa1ZmQMavSPJnCVK5qDqzx2EBaWFlRV8Yp7saR38PHmjeJysQ_Wjsag2t6Kr69l5We61lfi12YNkQFDD0NCL0BnBNc4En3A_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhYx6bnAVroOoIUDEcnLljcxhNe8hxDSN1CsHaSeIenouILd2uBxEN35iOLtpwLBgQVSzJMde5AH3J7FMHeJ17Be6dXf9BsSXm-C3mRE7cjvwDuYjnyS18WMB-dGdCOBZ1PxcT8VLXofX4q1b7vUE0MtpBC30B5-stb7jF2QVPu_4iiiL5GIK5XGS1WUmDCcTYZNQKs3_ofBbD4CUCQ5tDtvhXbnD5XY9lENJNB-W9OlMw9Pki8wrXx4_RpAMTxyu6GOlcFLj4JOm9JuviODvCFzBZCqHyP9JFXuLOF4FTVOhuoJf9hV8bSgMtydZu9z5ZLmagKHKtwxvugnth73oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJJn9gM8OEL-Wy9GzVzbXm_kop0eBm6ncb_RsketF2hyZE82D59rBZuX2DTCRAwl5lAx6bgykV23BhUPxBXz1Yg_NXFC3o53-wSYdp-T7iqzOP5TfM9BWIpPydXFF2aEchRdowAAJzRW0eT1KPlYWnmUDrYuq9HH3is-WWsCfqWyeGwL1noKgenMWLyt_UCaD1zm3K34Hr7wn5QQQXgo75MiL0_ATLhWGQUp_HKZvak2Sax24i0xX0xfJM77mHL15_5eqLSsPc-3Gm2hR5Fc_gvl-8v2Z5KWWDpgVKRGbThCIZgnyCZF-j6QWD99rZz4SFPKBwWfolhmZx3m2Z0rcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuNBMKsztCCxFntWtE9Go0oZWamr6oy5ffPJtq5HdcUq-UEjFzsAxZ8y0cN6RbDWeMPaechVP0Wq9TG2WCPyRWvGopbkkxyLkBeK2Fk44Fz25d2zkcBO1qxH_twjufgsTgR1jOQeUQmk9BaTpgzQDPcZlYOq2snXt0HuTjwNxOK3r64k3oR8Bj0xo4oYp2Z_1V4WHJE3-ZU8PBrjSyA2Y3txDaX_dV_ogvyNUPtF888E4mtdZJW0chxhAUCMKznSIEs_on04KGs9zib0mErS0mNeA7iR01ZASabG_uxvwgWCXbSRfside9smgBQN5c69kMCtdYfb9zqEGzt_mY8-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=vROHQbrofqC8f5Eub6OjVFWswotnTpL84naxoI-X0Bx3_XGbz626zZhgJ-kLhakr2fBCOOgOXLGyGNaIOIX3xHpD9kP4-P_XTPSqScQ9bIeVrYocj4KKFiPzMvvyfh3_YewVaVXd3pKrS6H0eGAvmv8pgk0h0KR02aXxL9QDoExW3bna17UXDSt_uM3Nbp-ijWXkCCxChYI-roK8BqpphzuqEW0hS4WJALt_QLFkFAW9DId7ijVfI-id29hfLomlCVibJTPsj0ItBD3R2tCEo-2qyUN-yQuxKDgDU7d7W8fGd9_byFqCde3bK-5t2tflXibVQzEGTFccJwY48lnxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=vROHQbrofqC8f5Eub6OjVFWswotnTpL84naxoI-X0Bx3_XGbz626zZhgJ-kLhakr2fBCOOgOXLGyGNaIOIX3xHpD9kP4-P_XTPSqScQ9bIeVrYocj4KKFiPzMvvyfh3_YewVaVXd3pKrS6H0eGAvmv8pgk0h0KR02aXxL9QDoExW3bna17UXDSt_uM3Nbp-ijWXkCCxChYI-roK8BqpphzuqEW0hS4WJALt_QLFkFAW9DId7ijVfI-id29hfLomlCVibJTPsj0ItBD3R2tCEo-2qyUN-yQuxKDgDU7d7W8fGd9_byFqCde3bK-5t2tflXibVQzEGTFccJwY48lnxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=WAw2DcCDrbZlVGbpVUfOaXJmHUidctfUd5CQZq4PU501SsVAbe5vcTSdt_iNQze7iAGldU-osUoii1Wjl57uM5GEiAH5CPLdSklLz25rzPMECVkhdLyxkOUZ_m3YtVj_ECikHibsKFIzQUeYIXI-z_2ezCuBbqSVOAwe-B_DIII1fLKVA4T4hqlsXsVUYdHaljV4ZeuqY7ikZCntTyYzjY6d7UJLOnNvTjOFECSHO0A7-fB2CCkJpHfCu1tO6jHcZteYp6cHvSGk-fPpITwe6tOecu4ETw_Gi5IF62a4YkhPwsX-KhFnAsDOP0D4BaRSuBFmtdwk3WhrIjDHo58OkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=WAw2DcCDrbZlVGbpVUfOaXJmHUidctfUd5CQZq4PU501SsVAbe5vcTSdt_iNQze7iAGldU-osUoii1Wjl57uM5GEiAH5CPLdSklLz25rzPMECVkhdLyxkOUZ_m3YtVj_ECikHibsKFIzQUeYIXI-z_2ezCuBbqSVOAwe-B_DIII1fLKVA4T4hqlsXsVUYdHaljV4ZeuqY7ikZCntTyYzjY6d7UJLOnNvTjOFECSHO0A7-fB2CCkJpHfCu1tO6jHcZteYp6cHvSGk-fPpITwe6tOecu4ETw_Gi5IF62a4YkhPwsX-KhFnAsDOP0D4BaRSuBFmtdwk3WhrIjDHo58OkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qrO7cSrShcbA7oEVSGy5OWRjzxGLCxF-edMDWKn1RPt9HA9KJVM3fXvMWYGyOQsPlN68UOuZ0g8AHCZgyZ7L3BWLKZtMlLzsQSY1x0O0QdGP7qSCPQLv0GaI9GUDiVk0GA1dmY-QquKn3M2ufhxBj6mgV7dTo_P12UOu8c6qVOv6_vBlLp0jPzhbm7XZCQh1DPPQ7kSRx7BqnELKKgbLNgcJHjiavAahFoarTXpMkfnAlxY3UENbDS0V1bja6AbgWFiYB539GxTZ0SpjFhldfLt2L2yEb19ChY_es5VRk8i1QiKevT7Ghc24Xg_jMvOSAxlKKD6nFUghENAHiByVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=bmeQUMzzfPvIFKaz-fS9PGQcBlz-yfpkevRSptqMVTtfJBKrtFYgPsh2HHysCkNaEp_NrbtB7NbO401hMXYy9ZZkFAzrC1ywb2Ox7DfZKX4jitwc09brkZ2H1zBo2d-25KOxEmXvPM2cv_Ja3yVNHPQQscKicPnURCmR4yfg86ndE4W5xyb_mTBylYG5I4JUeD8s-x2VXIsj2DGu0V4RnpqFwmx6_wyRYw_WGkMVAjHMdpRpMnzR3xYHCtETcT9Ie3-qUCJ_WmmviFqBS-0cDnsmzLzcxkGReZ_hkngA6akJxr-zGW-JNT6S4fCAyC1lwdukVE13v21gFiWbW7fg0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=bmeQUMzzfPvIFKaz-fS9PGQcBlz-yfpkevRSptqMVTtfJBKrtFYgPsh2HHysCkNaEp_NrbtB7NbO401hMXYy9ZZkFAzrC1ywb2Ox7DfZKX4jitwc09brkZ2H1zBo2d-25KOxEmXvPM2cv_Ja3yVNHPQQscKicPnURCmR4yfg86ndE4W5xyb_mTBylYG5I4JUeD8s-x2VXIsj2DGu0V4RnpqFwmx6_wyRYw_WGkMVAjHMdpRpMnzR3xYHCtETcT9Ie3-qUCJ_WmmviFqBS-0cDnsmzLzcxkGReZ_hkngA6akJxr-zGW-JNT6S4fCAyC1lwdukVE13v21gFiWbW7fg0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6bycQ0H_-bQHyYXuerZVIJXGJPtf5k8WsGXCSgJHv49PhG4nmXW-iQu-VJCQd7kWV55iEoHQ0ZOChaxQNIVrTDcT--J8rDU55g_m26OMG_NMnIZpPd0f6iFRIYFHk1nhbD4p8gvzjIjALxeOz3IOea9vWUXvSrv6ZeDqWRxgCcmcWD1rM8_Iz5Vsla0ptPnx77bdiM0EkQ-flrpXVVYi0HCEmtenVkLCLPkeQxFy3QSW0F96Jw7YioerOXieHpnIekFPoqu2AwO902ThPjSxMerVsP40LwQyS5TY0Q2LN_-f6eQZJKXTU804dKwVekKZ_IwRG4Ibo8HGvTu62LO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=fmq7Cf1vlTWCaCaMMoWsYL5AIxycGj1UpJ_8fbMxKwiy2kGKb2CrACNNFdPZ_fF8phlvqmTt3CHQDfXQ8y9Xh9EAdfwOPbHB53yh4MRnkzB5m9UptVmL3uBRRfxHBfQSGNx8rbRbOhav8asGBbPtjZZFvDdG1DB_NExg8aFIOGmXRGBGUTK0odRK6TvKHhilck7U2rkJjzckJelSie6r2SPSycFUAjDmc2iTSPuSu6jD8GkxvFN1PgtsYOBruVtq5fYmWa6nrhvjA6qsXBIOsf1CeWqoU2rz6_RLp9XMA4Xjw54Ec9NRfnxR5bH7bznRQt9f14clatG_QSNvOJMIUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=fmq7Cf1vlTWCaCaMMoWsYL5AIxycGj1UpJ_8fbMxKwiy2kGKb2CrACNNFdPZ_fF8phlvqmTt3CHQDfXQ8y9Xh9EAdfwOPbHB53yh4MRnkzB5m9UptVmL3uBRRfxHBfQSGNx8rbRbOhav8asGBbPtjZZFvDdG1DB_NExg8aFIOGmXRGBGUTK0odRK6TvKHhilck7U2rkJjzckJelSie6r2SPSycFUAjDmc2iTSPuSu6jD8GkxvFN1PgtsYOBruVtq5fYmWa6nrhvjA6qsXBIOsf1CeWqoU2rz6_RLp9XMA4Xjw54Ec9NRfnxR5bH7bznRQt9f14clatG_QSNvOJMIUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkiGCAYrMkEcIiEKerwXI8yjSyj2J_fmpcZhuFpg18dKLC8aRWNPupQyzQBC94UtZ0i-FT4WLgPW_ikcb2awnNCecJHV8fRKP3e36VNEcFmrli29iVY7CFsQ5s32ulgiJ9nEO71uQRh_GWAcWkVzIbseopNmFHlJf4Lygu_xGxoqMj3FELFHzeoVdFDezSNew66jdm8Ub0-0TpMG1VtIyenIfdXXl1BVSUI4QVPX9UMkvq5giNL-xhXNbzk_SPZeOQvXddNfajOkmVxY35CMnoVvOq2NKAQXyqS7MzJ4FJxsFh0lGPQ9Pgd3nLewM8mpDdggUk7vFLYR78Zn9vD8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=TV1CAURQs7xXGewauEo1OieCtfTCLA85O_hXLNtW0uI02-A-SuDM8VzTa-mlS1qnvHBxQQsB0stw-kzMtvmUWrlr7DGE2BnxIXXHSaLpKC20KtEXcJlCAVQ6QT4EIVpj-Zrj-HyG1K4u2N5saqJUFXaOfvVKpj21lsq2ZzZxywZsALT4-NVljYJOlUm0ZeyDgHnHqaLXf0i-ugg9W2L61lMJFg4RheNzZ0e3RlIuwyAmEwxgyk_5FKV27jh_-EpnBdcGjTB_y8S6q66F4jurvZwXMVhbLFAeBY5MYOb-obPWA-ydmDGoBDLQ_0vdPc1QZZMf4e_QlhMzqZ_4GN7zkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=TV1CAURQs7xXGewauEo1OieCtfTCLA85O_hXLNtW0uI02-A-SuDM8VzTa-mlS1qnvHBxQQsB0stw-kzMtvmUWrlr7DGE2BnxIXXHSaLpKC20KtEXcJlCAVQ6QT4EIVpj-Zrj-HyG1K4u2N5saqJUFXaOfvVKpj21lsq2ZzZxywZsALT4-NVljYJOlUm0ZeyDgHnHqaLXf0i-ugg9W2L61lMJFg4RheNzZ0e3RlIuwyAmEwxgyk_5FKV27jh_-EpnBdcGjTB_y8S6q66F4jurvZwXMVhbLFAeBY5MYOb-obPWA-ydmDGoBDLQ_0vdPc1QZZMf4e_QlhMzqZ_4GN7zkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=RR0M-EXg6dStrfMYMge31464-CeqbtF-pWzL3bkFjiXQAp0EemhecQ8cw2oWHrasQrara9M2OvXjGbpzFfz0MAQ-yfxEH5J9_wRoYyO2_-eFE5rE9mLr25b8RH3jCKc3YZ_OvSbHhqBYz6HW_d1pNsaXvukz_8xKk851h4kD7DVDNEJ0zAOco1q6jmoSgP-FA13girPQoxvAABWtiDq4Bp2QIFEyYoZsL-dg_0hhMp8iZ_FjDYSorY64e1MqSyY2WQbamppCG1LrPDIl2naixViz5ZpPEuagRUH9jY1aZmX-d9T9lHs8KO0gWUBM4Ylb3X8UVVrq2_vIj-Lzv7qI5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=RR0M-EXg6dStrfMYMge31464-CeqbtF-pWzL3bkFjiXQAp0EemhecQ8cw2oWHrasQrara9M2OvXjGbpzFfz0MAQ-yfxEH5J9_wRoYyO2_-eFE5rE9mLr25b8RH3jCKc3YZ_OvSbHhqBYz6HW_d1pNsaXvukz_8xKk851h4kD7DVDNEJ0zAOco1q6jmoSgP-FA13girPQoxvAABWtiDq4Bp2QIFEyYoZsL-dg_0hhMp8iZ_FjDYSorY64e1MqSyY2WQbamppCG1LrPDIl2naixViz5ZpPEuagRUH9jY1aZmX-d9T9lHs8KO0gWUBM4Ylb3X8UVVrq2_vIj-Lzv7qI5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5v9prUd6fW0e0c0c6fuwf-kaqH5hqs84SaNI3TxM1esoDIgnO2bIa-OcBj5lhmMwGGnZ1fY8BvZsSok1ZbnIclzk9WPgk-cpFKsgPOCGKC7WmDVnTyO9J9WSmn-YZAl768IADXwBqxjOJy-wb0Sf44EI4S4OvMYWPIAtiFX5qALrMQLTnCPcfHCnE7HLsxN16bMJqLG1lMLYJGzMc_qxyHIEqYgwDNWMr-6q6pElTkYu_M-g24Att-khQr_aVc1oFfIEn3BK-z06KbK-6nPZmIiMHpui6IiJ6ru14YoSZxyTi3O2D_ESwCXxc6qdsxbZQTjv_u7B6KvS260ea1hBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=d24cpcV0R3G4J2Vk4Y1cQd_1UIJywKgvO7xazAPOKf34xR0dMlwAmi2ELLTWN9XpHBjNCI3xrsWvzTK_gB-lop2rD4K7Tv74vlsMpNL8dXf1TuBRhftGRhcxDR9NUznthjUfTLBwpjMxSUB4IpOraB3MePNbr-g1hxRjWsaN392vDBS_cachKjV9O0EZ8CNxtnHnSfOhF4gpoIvN-VS1Z8SKTuV2FHjqzefRehUu7v4s1rPOuXcpZm5-5Zx14EGrk3mzreOEFmXUzGPGVWbtEce0x-E5vZeMnO-K0haU21sRAQZnRZ0ItA1FYMBpu5RyUim3p7yBmkuR6-r9y-v4zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=d24cpcV0R3G4J2Vk4Y1cQd_1UIJywKgvO7xazAPOKf34xR0dMlwAmi2ELLTWN9XpHBjNCI3xrsWvzTK_gB-lop2rD4K7Tv74vlsMpNL8dXf1TuBRhftGRhcxDR9NUznthjUfTLBwpjMxSUB4IpOraB3MePNbr-g1hxRjWsaN392vDBS_cachKjV9O0EZ8CNxtnHnSfOhF4gpoIvN-VS1Z8SKTuV2FHjqzefRehUu7v4s1rPOuXcpZm5-5Zx14EGrk3mzreOEFmXUzGPGVWbtEce0x-E5vZeMnO-K0haU21sRAQZnRZ0ItA1FYMBpu5RyUim3p7yBmkuR6-r9y-v4zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USF8VBxHZ3gBczowkfLLV0iF-qadbVVOElilXlHiVPSTLRh3Go2T13RDusSNOGATIHOCSWhwxepfjZ00jBVI95vAi-RGZRolIrjUszhJaXiANfxg9t1NwCZBELU1ENWIK6ZEwzGJIk5Qe-0sOPDfG8DEtEuIkl9BmkoLkr9ZQS3luKdS0JbpxR3oRBh8S0zMPm0Grc8GCiETyglKMBm8dCMnTb0bfvg79epvvoO-9cpNhyu2RboYpc7gBdSOSbbb2-8HWK0hGuJqw-1xqeOk5PgL2F-BZXBYPC36CrJcFIYs8GJxpeFwOdrVm7pBD0YcPqE9VtG6Mp71rehhwP99Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=BLzzbhjzNg4GLSmpnoY4lcZ7siQpUEvxGZHrX4n3iSO2Q5TUT_TmqMtpkNS78ubxClJqTU-SBWmmHWg5G7RNuXYoJ4DHasfoQ7aeGNai-PZ8NLPJU6iwN0CsL8pM173MMlEt_B7RJePfPDwBSgyq5hsUvxM-dMnHNgOJvmwFJgX2KYKHXSssuQ2T8enFAqlK5zb6VHL3nPgqleDL_DzM7a-z9049yv0fY2hiVo1-QCpaJxJW06eA9HPoIlpkNS52Q2oa4wE8BLaOcfCvJTdkt68QAqEsTtMJbuIe5DTDw5p0DNrk6YZ8ZuFewwLgYsHZ-K6t_SIElmHGtJ103G_4XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=BLzzbhjzNg4GLSmpnoY4lcZ7siQpUEvxGZHrX4n3iSO2Q5TUT_TmqMtpkNS78ubxClJqTU-SBWmmHWg5G7RNuXYoJ4DHasfoQ7aeGNai-PZ8NLPJU6iwN0CsL8pM173MMlEt_B7RJePfPDwBSgyq5hsUvxM-dMnHNgOJvmwFJgX2KYKHXSssuQ2T8enFAqlK5zb6VHL3nPgqleDL_DzM7a-z9049yv0fY2hiVo1-QCpaJxJW06eA9HPoIlpkNS52Q2oa4wE8BLaOcfCvJTdkt68QAqEsTtMJbuIe5DTDw5p0DNrk6YZ8ZuFewwLgYsHZ-K6t_SIElmHGtJ103G_4XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKR6IKxUkvBX6yv8euuUj6X3EjCfKHssqXZJh1gs-K6pZhtt9jOn43LSDYLFZJgo9z6zeiWZz1taGU6GaX_qh2D7eytH__W2JSJPKbCWy_2AI5Gg85dMdcxDW9Up3g0A26JDC3_HzIT5hElGLSzUwGsK1aUI8U-GYDhpxqvJaIWIdMDp0CAlIJ9IBDKnKpFjbZtSRC-5VsqaLyLRVV_GjyQKpcuNSjyjtemNq97V0R7ODH6ePXiIHv7cElzGgsagZ0-9ik39QTz-2FpFoboqYRNW9VDv4v-Yt8HC93plo1MbzVafr4EOvMeGeF_RIkL5P3OcJTL-R-u-5bhkhkKdKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMDKX2_X7Mtg6HtkqeJBx30t03t1n146XODJbdVxvmNUmMKo6P2jqPVlLdQP8Rlz9rC6LSoPBd1wzwfC1kGjQ62z_IV7rXqar4wlHUp2HUbnXw7CmdhiDs_tYYQRQY6elwyxIdUhrJfXc590tK_k-z67QT-Iyg4aX7ocFppLb11_eKtq-9pX_ab44hWefveTz4gs5ZD77iXUxeyLzcJBebUFTcS1MYT7doxK-sqTHCt2Umbjpn_5ExpW9SArslhkmP1udOaOiImyEYuB5ZQWWiViYbN6l3SYXxJditvQeirrXwhvt4Uumanl13O_Dd2zTC_MfMIief7JgMqMlDJ7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOg3ZO23vL1uVuXZ5w4EdvTvOpERLuKmtK6Uzc9hkX0vE3ne9mDSgihWICYxuDIkPB-rQ2kCnWfzsHFQtkWmwQNF2K7Xb6KUJQrxehhAdLZf1orp-P1-gicwxBLjiPSgXLZE8h-AN2sKF-mn-RDnbKp6Z1i82SrQOuYF7KBws8a_L8-Vgpi2yWWPYaSUpMsXNze0aMMYkYxO4mFnfnwbyuvrSFq_mXs7kYpwXc69HvSJ2uODzz3dOtPNwbS4LNQbdaGZwT6UuAy4pHnK7aWJUNl-KyrFr6PWM0Wwami2q3hhHbFTviP7nYQw0JCViSNH-d-gREDiNIj-mRggFRkFWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4lxkKfgO6lhMT2OdaZBinjubGe1yquxqQ7Nkh6F4gdLzAUC2D-_jmGEuOXqACdXqdz5q4nXtKXP2IC_2fEl78YDZ8uHeRpQWlzj6MvVsqO2OWCiEEV468W6H4i6mIFzawmqgkUEQStm441YSOvIhKTThoKDpet0P5jltscnJHNXO24uoJUtybQzkKcsM8e6UJWtf658Jxi1TNz7PlXF_6XqVFXSgdjzsZQQJx59TwHTUJ2z-NpfJ8_XspUmR0LMy6FrZgpsoEw0AxNemegdnNht5mL9n4wN-buk_lw3JimLQlERPZLuUMdHnUk1trS3_xnzo_YPs-k6iwy0t_6TrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRJuvfBEq3JTV5ZrnnAXF9wZQv_TUeT_OHVezyW00lBpbjYTwEVv6iPj7XHJETk5DO_6mFNVc9xslP2eddB5GW3DCj3UAYhm16RBM8ETM7rBnFlowxhJ3reLkXgPZyoCiuKenyVT0MiX3E1PLaFzifsj4CunSVEilU4iAfeNfSpTwrLnTC6U_9L50anX9URYyW5rplP9dPwgjxUvmYQtEGT-KsgqwuNfAlcD1EJ7HE8-RFX50OdPd4VfPgsPtAocYaWMq8fwZ1GNeMOx2ANwUuobMVYjqtiMo9lxIXUAwD7F9bxmaQejuBG2AGvQpmfKdhyJ0WexB72lvbgFuZh-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_MZ_Yl3Xzc_esS4bUl0IZva0BfhtJjTx-2V5mJO7aOAoONBCTgtqSaWIMhMQuK1gRqmb0n2MvbtJi6DTpndd61fbOob8Cw2XDsFRqMTlXelgzoYtLVJDog8_6cij-53kQNTIOtSMGBGLfbu7vL4Vy3rO7w7tGWZxaLZcqyvoZzwUeR0brKoX7le8J_stQpuYBtV8a2IxLK7EWsDd8E8KfC9X5W7ijOo5kzfnpfSkLzhFhoil7bHaEaaGaHPVgZC3dZl1gTAKEhD_KGDvyv6h09_HMvDl-NzUNIOjsK7dfdNWdnofzc-W37bIjAIM4n1VoWYi2YsNCOC1rhYLI4caQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBqbyzi3MeetDPIhcTtJGtKZYbPT6uTV2ozKOqd-_TNNe9N01riu_mTCcTtBlyB55vIICKZhYfvGZNIzNwAwPjJmWQrDTKHHSnmPA-JPpcqTzXZyBGBkOqIcwglci5NC0Z5dI6ehXdV1CyOQ6nc_1AGtHp-laQ1G2STpjUoAtuUyjtNXqbHZ2TLUKjdcYCC6qczxcEqUaULeU1iUTdGXDOpQwcP5uLL7BccWwFWkIQv88OGp2DMmSf6sXhRWRK5xSIxMfcKAPo9dHRtIMC82kwl7HPj1BW4ejB8QJTB_VsguXzjMy3-OgF73rWR_0VVhUog9RLEuOfEFhORc0RqcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=MC1eSqjdgKOS15ivT9P7xydZCAXww7csgP1LrZkfUidbS3bq250HSQYzds_JJb57atxEAKyRYqnl8Y9VTlxOOywomLARQ1mGync9oAr-pujCpI3_UCNj3M_uItENhsFJLFKIIOdNgNwRDyqa35o4Vcy1-SMF7PlsDxaCs6Tuf-1_bR3Ef97nxaI5eR7DgBW-ntDH2dZORo0IGIMe48_POSrP91Bwn0Z-AvlOWaI40rpUcG-SNZwOjLmUkw4E2sm0SXg_zTfB-0c83fYwpR_BrNG6URsUlL4uE3v5K4d8Zqus0taLTpLkjEif0h5FSAt4o0EJuY5yerXsewb-9wwt3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=MC1eSqjdgKOS15ivT9P7xydZCAXww7csgP1LrZkfUidbS3bq250HSQYzds_JJb57atxEAKyRYqnl8Y9VTlxOOywomLARQ1mGync9oAr-pujCpI3_UCNj3M_uItENhsFJLFKIIOdNgNwRDyqa35o4Vcy1-SMF7PlsDxaCs6Tuf-1_bR3Ef97nxaI5eR7DgBW-ntDH2dZORo0IGIMe48_POSrP91Bwn0Z-AvlOWaI40rpUcG-SNZwOjLmUkw4E2sm0SXg_zTfB-0c83fYwpR_BrNG6URsUlL4uE3v5K4d8Zqus0taLTpLkjEif0h5FSAt4o0EJuY5yerXsewb-9wwt3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a527peS28adrEIRPj7jxvVPclRo6ujHhOBj_9XAFYIkmKax-C_TDKX1Sh0hADuoeZoEoslEcpQ0ZjquS3rkVEJHJXYoMfmq7NnCoWVbD1MohrFkNcS0Nj12esIniKJRfDIUjtD6GlfiSSnbhE4g9IHg3hGWRnhAnGgVEnCCkGWoMsW_snkLBofpaKJ-RTJP7cWP61sDKV1WD089Si7QL35B8rJnqqTfykcmbE8Y7ocpX6Irt9i9HEdfOAlc_zblIxt27CZhWrlKwsOi3JsgsORP7cF90bIHL5GC9uEhhoQ0Tr5wXv49ll7M-IgCctAAnPwc7DJxShaWvApeI3vi56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=K0Ul35GJJgj8bvz4AiT8B3va1sSF-ng_phtx2OHuWqFQJGRFTF3ut39d7Cft3YuMlmYfdb3cXBN52vXhwo85HhIKR5bDJJYjLfowZNq5ndyRh7jn4a5Er5NA0NkTcAewFelTMWpgPA7aM8Fm5NS3Q758U8xka4x8U4Et9lUjm5FvZN338hvq6OVyUVRjLEdDH7YF7DYvsZpnb4YghQ1QDOojP0rApt_KUhUgOzQrqqcNt3Fpo-KxhqlXGPhAiC3VGOQlyD0RyMmP6b35M_APJ8ur1Ohu8N-cKjI0nUabUpjJMF4ka2A1MHA7WRiBaaSuG9K1clQjrnOYKgell27xFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=K0Ul35GJJgj8bvz4AiT8B3va1sSF-ng_phtx2OHuWqFQJGRFTF3ut39d7Cft3YuMlmYfdb3cXBN52vXhwo85HhIKR5bDJJYjLfowZNq5ndyRh7jn4a5Er5NA0NkTcAewFelTMWpgPA7aM8Fm5NS3Q758U8xka4x8U4Et9lUjm5FvZN338hvq6OVyUVRjLEdDH7YF7DYvsZpnb4YghQ1QDOojP0rApt_KUhUgOzQrqqcNt3Fpo-KxhqlXGPhAiC3VGOQlyD0RyMmP6b35M_APJ8ur1Ohu8N-cKjI0nUabUpjJMF4ka2A1MHA7WRiBaaSuG9K1clQjrnOYKgell27xFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDAkAtsjuPg793ZbgPFIRQyKrlaATBCTnCZjFkI_LYA9phA5MJD2J0b2cPndJ35VvPbpoXg7MPNGsGI5ZDgGm0-6Jp2vN4j8621wIUzSHOXFPQsyGmA2nCJFTo3tqWOYn5s3dYhTTCTde62ynxAXJy3cXyYJT__7jH4EaNvO3TV80us0TM8V3tdojHAjhpkoWAEtbQkGNL_sl3hG-mIbPLYj7etqHf1tuzWwFflOJkUDS6nar7z4Fi8i7-zf7xLEExdADZUgOVJTqSPmKEj-ImLBdOz81rnk7r1_EzGMv7jE-KqJMOAwxzDm8kvdwYW31jHZsOdV1kAxpS4_UsDC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOdgX1o-Ik5DAqyedsOnWvslXfMfJpCzCNacGsYzRIQzYTE9Y5yCsg99U5-Dac0ItH76EwMzKBXrXIY3CaZLOJXlzLT6VnMQvhDI6Z_RRVOBT0FexwrZ6oUoGuqwiUhzJRdUjJS3zqRDTwqxSnLWzZobyVToVmdhxIjJ9KMq-qxauKekjNxAi9575Xg-WDYEkJPDw51NvFIy4u6OfpVvNfiQGoG0ybaiN7ivqnN8bUBLrM6IzEUi53R597487WWZdk_QvibtnL8-RLThEvpNF774D600YqhFlc5_ov7-vRwWWm5EEqIzvZQ5U4UItKRH6QuHzPbKDZM8B-HwSu0wgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=Yk0Th720Me9nAV8XqKZsCapV0ULKGCZ1QLte8tA_aE7nb8N20exiZW2xUl9LY3nWhsI7S9yGoJpH5s2mRaHmxoDeH9hU85O9bE_XBsXRZBIJ5QmsW7-8DvVGAYKBumJmy0M4qUA9H7mcbYbj1szUlhGVN05h9qfapK3oRfa48NaFC8cZNbyqtCFMytodCkj3rqRNzUaa3vzz4K4a3GIXFA4JarFDryQPZ9ATTROqqY8FoeH2oprlADulBRW-10YHoMrvtjKgIIpi_L2VzCIQL8omrBvRHtf17-uyggvSIxp-P9iERd05PWOpnvh1haC5CIg66n_WHz_FBPhT7zR7AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=Yk0Th720Me9nAV8XqKZsCapV0ULKGCZ1QLte8tA_aE7nb8N20exiZW2xUl9LY3nWhsI7S9yGoJpH5s2mRaHmxoDeH9hU85O9bE_XBsXRZBIJ5QmsW7-8DvVGAYKBumJmy0M4qUA9H7mcbYbj1szUlhGVN05h9qfapK3oRfa48NaFC8cZNbyqtCFMytodCkj3rqRNzUaa3vzz4K4a3GIXFA4JarFDryQPZ9ATTROqqY8FoeH2oprlADulBRW-10YHoMrvtjKgIIpi_L2VzCIQL8omrBvRHtf17-uyggvSIxp-P9iERd05PWOpnvh1haC5CIg66n_WHz_FBPhT7zR7AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=S8A1LjYDD6_0p97-6SjQkglFq6ANaHde9U-SwNmONQUJVP0ga331ijxZRSh2MbXjsM0jNnNZgnx-Zs3w3tL03iYICnjriRGa139FhrTuE9lV4LW6pHwPs9_wDrEIjrsPLg_3sPuWDhDAqHCJfWhzvsJ_iyvzcbNAptcoEjTnwzuV4ejoAFkYPuXbLsx-Lqn8Y4TRzXQCkuP6Vz20R5VywN7ukiqgEyCPqkp_GNZzZGYeckmjGLxJlZTtT3iovq4x6bzfxwtz5pxa-ZXQXtgpiMBwiTIqG6W_TgndZPG2idaEm3Bjv3aBtt_ZSACUC3gwoDv3nnmqZsvBG3tWqovyrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=S8A1LjYDD6_0p97-6SjQkglFq6ANaHde9U-SwNmONQUJVP0ga331ijxZRSh2MbXjsM0jNnNZgnx-Zs3w3tL03iYICnjriRGa139FhrTuE9lV4LW6pHwPs9_wDrEIjrsPLg_3sPuWDhDAqHCJfWhzvsJ_iyvzcbNAptcoEjTnwzuV4ejoAFkYPuXbLsx-Lqn8Y4TRzXQCkuP6Vz20R5VywN7ukiqgEyCPqkp_GNZzZGYeckmjGLxJlZTtT3iovq4x6bzfxwtz5pxa-ZXQXtgpiMBwiTIqG6W_TgndZPG2idaEm3Bjv3aBtt_ZSACUC3gwoDv3nnmqZsvBG3tWqovyrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=fOguvYV_8kbgj5mzV3TZeMfaFDO3a39TsiPguocbg6BO5ERKLJP9yjWYpoUOEvCCNc0T3REWzRwy_tmXFO2u5AdeQJzuQNXlBsFxBNSNwpaKab0E2LY_BDo5K2CpuL3qr6Rh6O241_U_WbN2DCwfP1EU3TWbhVvMPTfrDD_LcZWOPpW8p0Ko_NYvSwroPGDvgOFcJH0H0PwCUuUVEnlENNtMrYm517ldtrYDWAH_5aKNov3r-J8DMtgPb5w66M3lANODPWqxA2rAknw8WvKPIqTOX82DhFbsjTayQtm-SrXgDydqp0bDThpAaDvvMi6CdZgEgoYMcUsUVuQp3KAJw7VtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=fOguvYV_8kbgj5mzV3TZeMfaFDO3a39TsiPguocbg6BO5ERKLJP9yjWYpoUOEvCCNc0T3REWzRwy_tmXFO2u5AdeQJzuQNXlBsFxBNSNwpaKab0E2LY_BDo5K2CpuL3qr6Rh6O241_U_WbN2DCwfP1EU3TWbhVvMPTfrDD_LcZWOPpW8p0Ko_NYvSwroPGDvgOFcJH0H0PwCUuUVEnlENNtMrYm517ldtrYDWAH_5aKNov3r-J8DMtgPb5w66M3lANODPWqxA2rAknw8WvKPIqTOX82DhFbsjTayQtm-SrXgDydqp0bDThpAaDvvMi6CdZgEgoYMcUsUVuQp3KAJw7VtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMZHrVWp8Qwl3SDYl5f5IBbVcm2yJTW0Q4ZVihDXhmhIxCVffxqNnuiyzuj7AlTEKdoAJIhlfuO2RMxTL69bN8NGLf2khUlZtQrkjST2PBRJMfJCRT7h13OSz6VQfzCU051ME_fuMPzzg98mvqCdK3vrIT9BlP_2mMcz1XsgPNvbpbUN-bPlevpTnecOMIP_1_nBqi1cTXgWdJLzjCe_AzjM_vWR3g2S14NyvXBH_3kBbWq7qhpTEtC7E9SLrXICbkh2DJ3fyVmi8sqNifKs5kaSh8Md6n5YE54fkE4DJr2TVSp-cqP7-k-fBMgRwfQHVDtjuY5yc2lEe6rgUWq1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=NzmgzE3Js7TLnVlnK3BMe3rbQu_IFAaSkN6R7DBsOuAFLUfCMetw2Nxx46qR_lkeBgaYgur0Ey25wTAxr8-UKQLs1FQxbqU4LpX0d5KoQfUEIY5KyJ7bXBS526jdEyJKRj0Neq9EXjGN_-2x7WuQTU-yJJcTWnLJSNgpIT1imV2dWAes6tUe2wmDYvnCcF-HOhYiwY6DUyhl-e_9MvnmtgLe-yUoHLUwXNIHB2UAz8sgB8WfjZLr2pfs6lSVlKcdaNHqaaR_g93lNg1mwijEX6iDjEq7lj_sKvjo6cLcFFLSkakQkrAN8e5zLRM8m5i9cYM2W1UVCqWlOp6rnaCwEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=NzmgzE3Js7TLnVlnK3BMe3rbQu_IFAaSkN6R7DBsOuAFLUfCMetw2Nxx46qR_lkeBgaYgur0Ey25wTAxr8-UKQLs1FQxbqU4LpX0d5KoQfUEIY5KyJ7bXBS526jdEyJKRj0Neq9EXjGN_-2x7WuQTU-yJJcTWnLJSNgpIT1imV2dWAes6tUe2wmDYvnCcF-HOhYiwY6DUyhl-e_9MvnmtgLe-yUoHLUwXNIHB2UAz8sgB8WfjZLr2pfs6lSVlKcdaNHqaaR_g93lNg1mwijEX6iDjEq7lj_sKvjo6cLcFFLSkakQkrAN8e5zLRM8m5i9cYM2W1UVCqWlOp6rnaCwEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=fS4JdhcShcYORJ9khyRpSZp0r_Fkv6lJk0SntE5l5YDq7bf69aifPF5hMVa-eLqDFUlIjsiS4gAZ7E2lAW0WE2Zfj68-Q9V1RCMTvq_eRBXlYGqWWISzndrpVC1T2WbRxj_86E-0VZ_cV6dktHtPnmsQkEZ_HUu8Tey4lOpUUu4oYph4_ZNgAGmHNi9aKBeCCZD0MG66VboCa3AY9VSrtuW2HUV4gqK2NrIVbNO_BocCcPeQ0ZtoUbRZY3xVwC5bdUOPyHXTNH5wnAz-85Se1S-Qsl7-ODHwOzHn_t_yyQKlg0tiFBM07wLqTxtS1o_jJJ_MB0ZK3WHkuplC1Xgu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=fS4JdhcShcYORJ9khyRpSZp0r_Fkv6lJk0SntE5l5YDq7bf69aifPF5hMVa-eLqDFUlIjsiS4gAZ7E2lAW0WE2Zfj68-Q9V1RCMTvq_eRBXlYGqWWISzndrpVC1T2WbRxj_86E-0VZ_cV6dktHtPnmsQkEZ_HUu8Tey4lOpUUu4oYph4_ZNgAGmHNi9aKBeCCZD0MG66VboCa3AY9VSrtuW2HUV4gqK2NrIVbNO_BocCcPeQ0ZtoUbRZY3xVwC5bdUOPyHXTNH5wnAz-85Se1S-Qsl7-ODHwOzHn_t_yyQKlg0tiFBM07wLqTxtS1o_jJJ_MB0ZK3WHkuplC1Xgu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=UgD0kxgC_0AaLW00IBSBeRNuu8Jbt-bg2HXJPxwiyjvWVDpsII7uaGyOt2z6G4Qee61HmFWTLcbHBHcfY-3If6SS35hpPURRowzBCi3U4331BR6vRy5Ewh3kKeRzmUgSTYKfshWGo7GtEYK04OFHwFuvD-RhdJ0U9u6m_f_vCYWs8yOnByjUIfMtasdfuhFKNlXgnaRSaBJzqSknrDHRJrHHFTyzDEq8DSq1BhGdmwCQrb9i7qk3RN0jj0SWK8F2oIaJ2XxrLzqB4jGLutY5IziKf0fqC_ktJtuzoxsBR2lcRFWWCrOl-pMsXH3Kf-3cFXnDwIqFllUNVXO-tZ1NrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=UgD0kxgC_0AaLW00IBSBeRNuu8Jbt-bg2HXJPxwiyjvWVDpsII7uaGyOt2z6G4Qee61HmFWTLcbHBHcfY-3If6SS35hpPURRowzBCi3U4331BR6vRy5Ewh3kKeRzmUgSTYKfshWGo7GtEYK04OFHwFuvD-RhdJ0U9u6m_f_vCYWs8yOnByjUIfMtasdfuhFKNlXgnaRSaBJzqSknrDHRJrHHFTyzDEq8DSq1BhGdmwCQrb9i7qk3RN0jj0SWK8F2oIaJ2XxrLzqB4jGLutY5IziKf0fqC_ktJtuzoxsBR2lcRFWWCrOl-pMsXH3Kf-3cFXnDwIqFllUNVXO-tZ1NrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ebfkewKrgXyaJSAiTFJ4qjGZ5tXfAYOjcOgy4LXhV3r7zAsiFjIDio0xmWDKHiK1d0dGemhybFcdTjKVid2nBld3vFFUMVEMbChEQqIo5luqf5B3lFzf-BY4DNp0oBRpdlhYNiNUB2ExXMYloK5U05M87V1nw4lBbnNKenbipLTbf1byU9LRVAAJnzvAee2QicoGGKxyuOW_Q0C1oJsQYx76G4Kj-j2Gfr51zyhHMbEyu9CEaz5z36TUI47dDSOPcYYKFRkqNhgxTTFu2zJUrMf8G1Bb4-RLetcZkH02cBEgckgACeoXrZhEuh5hLtcz6gSjrnOdy4y6KOU7fw_vCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pCACejpT4gdoj_HTTuZ8zxfJcX8KevrtcmCkKEK1Bld0T2ORcepFzY4ZIyWWNUQsOGsIsrrAm7DHLV04-muqDjwFzW8bEHYbPc69g7FqmR2OEFIgV3cb5HKh3BW00MmDUSL6RCBBi6eVdMw5DS5iMZuYhx-4NMt7ptboL3N5OIAK1dFeZ_VeioeoADuaFYdc24j2KG2rjKVxbGtW2FFfAiV5HO41DAZmuFaX1exdZJ1oA9GuuZgxdoGfss0OEk9-Z_hYDlKxVPMJaQiJNv6qZNaFkCXJie9v698SH0j_Sv_C2bmw4Pki5IX1XrdqXE_xOwbe8pDgoz7hk1HWGlDlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oj7717sTFRiA-pIynLohutjUKvIkXOnTIrU1YjKsJHpyMBQqPq7aPI_6K4_6100yb2cVyliFH3Uiqb2e8b14b43FtwjgBB6hARmUvm-Tn-W9Ig2jt7oYdBW53f0FJkmXyZBo5eTKPSIzs4ytSx7xYSQtiFE0-XLxEYvojoVyJXEu5xcbtumDYWUU2O6geYn1jVNUV7PdUJjOqVLv1myP4jeiCqsXuwlRPskqdpPtas4BC83e9xSQgV0Wx5y46bfAqmq-ElPKf6eyt8mj9OsAkxAOhLly5poJbYDEFGEkapWDS8y6LzsnI9l0j65sMDTKxsoQP1UgidHIjCtuAVfZrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=ml4dqwZQXRmwayDKdM3BaJ3K2_HDZ7gRxzP2sqDWgiFJD7t3BRIdeuzlovNPMBe99jARnL4CBilDJt_Caby7nCvhZnpC2AxV3ONt00Lvs8CQOHNIzxgVO8GJkunTWdseYJiuD6ZrI4YdpWoFL0070h8EoB6xlIHrY4xLPhn3KuTOqXWO2U3a7qmUqDJky8VZI3kry8d6plz-bgje6FXiC7fU7rdDrnf1hcPZJu_cdAikkWIj90z0qFJdvdpPHREaoCSVtyzXGJaSrKAsG95yYBVdPlpH8U1ZOrHYJjnFR0bjeCRdifgg2B6XpPwgMIvuT_-pRA6BL93KhuWKCW9qDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=ml4dqwZQXRmwayDKdM3BaJ3K2_HDZ7gRxzP2sqDWgiFJD7t3BRIdeuzlovNPMBe99jARnL4CBilDJt_Caby7nCvhZnpC2AxV3ONt00Lvs8CQOHNIzxgVO8GJkunTWdseYJiuD6ZrI4YdpWoFL0070h8EoB6xlIHrY4xLPhn3KuTOqXWO2U3a7qmUqDJky8VZI3kry8d6plz-bgje6FXiC7fU7rdDrnf1hcPZJu_cdAikkWIj90z0qFJdvdpPHREaoCSVtyzXGJaSrKAsG95yYBVdPlpH8U1ZOrHYJjnFR0bjeCRdifgg2B6XpPwgMIvuT_-pRA6BL93KhuWKCW9qDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Skd_xTgq33dmSQhHEb41v_hs4NhFYnhiR9a4CcwStORKVn06Wm4zsc0Ns301i2w96HAUEQ5YXKf7VOYS0Mh_zRN1eGn8JFGzlb8xFkOgYp0hkcqZGKxIwoJuWM9Ll2cyDNrJ00JoysZYAKWtog7a1NbG9SCJeHU5IWXHz-Qvxa2_NR4M1eDHtwUxVM0caIZVbsETo83p7ObfdXz6K-ylH7DFp3sh26tCaB8TUIvd8fXCFmXBobcIWFVw4_g8Iog6H08Gi8_hrb6k5ZRbyIXs7qA2O2Z3G5LyKXfglYmrDyMWlz4v-PXeBmd37AMpK9mlOT7Q5JpfpOfZmfE-T3HR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=A30nJp5bAWVY0w_m_ygbIup95dqIMysok6yAoWMl-pneuTRPQzH3ESpQopJPHKe6yNQLvtCIZfM3dVYyDalTDGc2LPbuwZMuEk-hQqYTHXpPFi2jgxSkJzIDOrcpE29qRAIPNo0ZOI32S-zYQnRWxhVUXlXoFBvdecJAi-1ajnWEzS5qNVr7Dkb_ss2mD9LzYZ_KTJONgOEAToQ4etfjylLPsHaTfu2PS9QiYchbAwKlUqU_437J2sncu3wKhEELWCOlop_ILuKL-Zhk5D3F2OOL8I7xFcVDmKfPABjuj8LumgQO84EXjgvx8OvueZLH_l4c5nsdOuSRBUfa13RTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=A30nJp5bAWVY0w_m_ygbIup95dqIMysok6yAoWMl-pneuTRPQzH3ESpQopJPHKe6yNQLvtCIZfM3dVYyDalTDGc2LPbuwZMuEk-hQqYTHXpPFi2jgxSkJzIDOrcpE29qRAIPNo0ZOI32S-zYQnRWxhVUXlXoFBvdecJAi-1ajnWEzS5qNVr7Dkb_ss2mD9LzYZ_KTJONgOEAToQ4etfjylLPsHaTfu2PS9QiYchbAwKlUqU_437J2sncu3wKhEELWCOlop_ILuKL-Zhk5D3F2OOL8I7xFcVDmKfPABjuj8LumgQO84EXjgvx8OvueZLH_l4c5nsdOuSRBUfa13RTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=N1z6lcEA9n3TsKhdyIKPdO0zt8iDP7mMeUZGYyEFwtYJA0qPD9IojTH_gC0n793zkjqaw-Y4MSQf-zUy8Vttn6h_o5RUh8x_ms21POhUezwGwilVvUjqxkDD5HobLuTJwZvH_j_n7IlRg7kirNHNAcRVA-iXT0pcqmMI2G6JJM1t4d0RMROFsTZZ5ZN7uuiLmjbZfqF-0IDf-j69lNUt4wRPB3LC2n36jbU4zzg97txQnYGL1mBF64tR3fW8MPva4YUCIp0aUCkhDCgIe_HEXD2wWnclkNcgYPDqZesBJr5piGfxEI0MNtZEZIzRRIFuks1ClI1c1RwwxPllQbFpOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=N1z6lcEA9n3TsKhdyIKPdO0zt8iDP7mMeUZGYyEFwtYJA0qPD9IojTH_gC0n793zkjqaw-Y4MSQf-zUy8Vttn6h_o5RUh8x_ms21POhUezwGwilVvUjqxkDD5HobLuTJwZvH_j_n7IlRg7kirNHNAcRVA-iXT0pcqmMI2G6JJM1t4d0RMROFsTZZ5ZN7uuiLmjbZfqF-0IDf-j69lNUt4wRPB3LC2n36jbU4zzg97txQnYGL1mBF64tR3fW8MPva4YUCIp0aUCkhDCgIe_HEXD2wWnclkNcgYPDqZesBJr5piGfxEI0MNtZEZIzRRIFuks1ClI1c1RwwxPllQbFpOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=gxVMVC6du7LJGuU3lB2ER__4b2bEAZGyeQotN5mZEB5PjWVGo1xGiO6r7YrR4Vg2_-XVRLY3VFLzxQ1jsut_4BPMNcOkQHCtCOLrHTq3DlIdUONcriHUXUaqr3Krm_EUJ-g2ZQAXnZYrHtRNxN1BOOFaPFAMJWPN2iHRkGv3OWJdnbVn-F-xsalQ_-6PkhA_WPj_cRcVy97P-odpBmuptXBaPGvjZ-GGJsNBb9NmD_w8fmfL1d7tS6vP7NlzR_lcTnPSafcCcEbOsf8MjX2oyKlt3-Swu5ItYF1mRhBnMyUcbP_rGAXi2wHWTXGz_C8TTvfYuuGnkAJ7qYJr0zFVMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=gxVMVC6du7LJGuU3lB2ER__4b2bEAZGyeQotN5mZEB5PjWVGo1xGiO6r7YrR4Vg2_-XVRLY3VFLzxQ1jsut_4BPMNcOkQHCtCOLrHTq3DlIdUONcriHUXUaqr3Krm_EUJ-g2ZQAXnZYrHtRNxN1BOOFaPFAMJWPN2iHRkGv3OWJdnbVn-F-xsalQ_-6PkhA_WPj_cRcVy97P-odpBmuptXBaPGvjZ-GGJsNBb9NmD_w8fmfL1d7tS6vP7NlzR_lcTnPSafcCcEbOsf8MjX2oyKlt3-Swu5ItYF1mRhBnMyUcbP_rGAXi2wHWTXGz_C8TTvfYuuGnkAJ7qYJr0zFVMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhtPL5q_m49T5omI08NXtMNVg0pgcBYbCaQ0E2lWCTJFevvp8UaQPgvMmNUueIFCu4lsXegJpnNijIXJnRj4h4lBlHIMvDiyKS9e2SxEabHdeO3IZcTFHcFLFFj4q_AtYHexSfHyUB2qWjExh_k3fOqSOrXUevwjVsyFNGDUeq2pMer2j_OGUIZmfdWw5XdirXhvrX9EonO8fuxewHSLN-S_4lZ9XIC-JEApd4qOAQCR4wLz64QJCtbzuapSQ8UrXeLmJV_Mp6Gw73PEQG_Pl4xFo-fnrvbMdGFsfj3CqOzeV17QgX1k1l64rMKB5HUSYBkZwWbsjKwChXSWDdeYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeAsL3U8u12ijKkloZCJIPrOFXqy1KB8lXHnPkc5uOs51tDXi_3ofTOUsNgMLJrv2pjslS4aciy3RqNV62zUkPVIn-a4reNrJjsMxfO-99ucp9bsV0IlkL30taPoEeqTKYK7Lp6fpaoBYly23ebj_6LKQe12Mge0W8F6SDAkuT3PGtUkZ1EFC46zAfTT1S4bZ8Jk_H6pIUK_nO9_GiW7h5zoZuERdGWozPlX9eKG_EHOrQa6KpQDWVbDXhzqeAhhzo1nILkD_Ima_IyY0KIN3t_Ymh_Tq4UZE_IDuHk77--sllTds_vwIE67KnWvjV6A7iKeOO_v_n5rt4cT9lgOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx_QLe4zuFqkv3VpKX4_bmjYcozPNwCXCdlBOdDoIiapsfs8uULxN9OGyE4Y13M6kfxayEiBrbo8zfkhdXsvFh9caC65B5bCC5ftsPYoYG2TATphj8JNwCSiOGRuD-onEvq2LoMv2Gi5iLurBbIXNgF5mZ98--N_FtyBfwEm2sQZqE9SB5-EWOxHkVHn8gLcI7cDcJl_YH6EbXkmSsdEX5qUz4jj_PncCFfcsyywIr5pEmURyX68vjzA7vDH5idjKM0DazoUrkTu4fpyngJf4-Ta68XRMy8B2Xj__vFHx8vWbsXakQkOKyDlPtsdlYZgu3FGyk7FF-ISbFWCqv9aVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYdJnifhIpcgf_H81JrnkUHkGVcJLrqLdnY6GIgFOod9HdWdgqFU3RczXAn4AzVmvG8eyGSwo_7H337sOjz39r4iNSTk_S0ZlrVe320Rm53nX6FpRJX69_Mi_SgMvxj5GYvEFVKw5YL3RjJfA6bPorXMeFv8S5xhB69s-Lvs7vmr106p8a6d2KbTemKE_HhaUalpds3NXDlyTGUMtRv1QQzK-_qZhg4kGEikB8XYDRcxyEB159iEfSxtBSiFdqlC-UgcxR5tX7i3pSOveuOyKbrmh6c8Jae634Bf_LTI7Rl4SPDg-d79Y1tOgbgzZWmx9birMr3RP9CAjE0h6qu4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=K5lETd8GvzlvuO-Gx9E7ZM2pYEtl0mxhgRjJf_qa2M7hQVMNOy3P0ZO9q-LJ_87esSV9t2nxPY0iZlkOGhhIUsvMoJmGRgr0FVmaRrF-UT_xum_eue6DLdAuwHu_y0iJx2NXAZIBxM8w7IYCXzvmuHQA6yybLUtRk9Y11jVaIox-HXpMti4L7UOUjAapx6GFpInf6INsp-IXw7E62JOGo4F2w841kFzHi2p2VKoW3VSTjgjOhAzMm2L1Qh0W02-oDkGVV_j9Fsfyawm2wUGQoWobg0CQbhIPbCqs5Yewaf7XHcjvpl0f1NrukIjN1lntWl7EDzmuja6MS6SFTIbfqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=K5lETd8GvzlvuO-Gx9E7ZM2pYEtl0mxhgRjJf_qa2M7hQVMNOy3P0ZO9q-LJ_87esSV9t2nxPY0iZlkOGhhIUsvMoJmGRgr0FVmaRrF-UT_xum_eue6DLdAuwHu_y0iJx2NXAZIBxM8w7IYCXzvmuHQA6yybLUtRk9Y11jVaIox-HXpMti4L7UOUjAapx6GFpInf6INsp-IXw7E62JOGo4F2w841kFzHi2p2VKoW3VSTjgjOhAzMm2L1Qh0W02-oDkGVV_j9Fsfyawm2wUGQoWobg0CQbhIPbCqs5Yewaf7XHcjvpl0f1NrukIjN1lntWl7EDzmuja6MS6SFTIbfqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=FiVk5vX61xVgvULQx7C3L3F2_ijO7uzfEfmzNvBosSxs2lH3jxF0YLWhV45fD1aiCuu5DYuxeF_sL_FQTQfxgj5s9V8BAZPAen7emkfxUuacYojqo1K9FaPaq0TFoa4mZQJ24oq3V-17ZHUIxfxAkCSx7hBRQyuShFobnrPFpaX5Jz7GeyONgj47dsu7TVaDPeY7yW8L9eiOz7XVhbZiWufxS_H7mvNtblFgQzJjTJ1lSJCN5goe4iVgNLB23b0wBela6l9wYxHWm1JDKunHSu4LGMcs21-O8_167TVk0O5yZHmHxf8Q5tpGQ_QO_YV-wZj_16thZeuGIzGGdcCqNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=FiVk5vX61xVgvULQx7C3L3F2_ijO7uzfEfmzNvBosSxs2lH3jxF0YLWhV45fD1aiCuu5DYuxeF_sL_FQTQfxgj5s9V8BAZPAen7emkfxUuacYojqo1K9FaPaq0TFoa4mZQJ24oq3V-17ZHUIxfxAkCSx7hBRQyuShFobnrPFpaX5Jz7GeyONgj47dsu7TVaDPeY7yW8L9eiOz7XVhbZiWufxS_H7mvNtblFgQzJjTJ1lSJCN5goe4iVgNLB23b0wBela6l9wYxHWm1JDKunHSu4LGMcs21-O8_167TVk0O5yZHmHxf8Q5tpGQ_QO_YV-wZj_16thZeuGIzGGdcCqNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=RiAXVlC0IXoPgojqZ1GrGLW-ieKmcrMJMnQgGDDJnPm-psw6PfOhHaxag2ay6ClIFkrXGPxAiVkVABxvbTgVxH_zJqxT2jjERKtsZ9LCsP5TSp60MlZhb9Q4ELFyltCaSuy8Sme_Z4bcZ2K2ghtc2ezs9saU41CMkAzV4_DZIl-gSXf-N1iG6UUKlKtpe2REi0IRx8xSS_pQco5cwb7lb2ue4rtSj0Plx95MBU5anJmaezcS2Ian0dvYbCJ9GyLg8zQeaBSBPy9Mtq7tf31woNucdsF2wiMHpJ2dNnnbfBO_JVdSc07f2ActiFl3CHc9vY1_jcgwF7eQnlqCYAKp8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=RiAXVlC0IXoPgojqZ1GrGLW-ieKmcrMJMnQgGDDJnPm-psw6PfOhHaxag2ay6ClIFkrXGPxAiVkVABxvbTgVxH_zJqxT2jjERKtsZ9LCsP5TSp60MlZhb9Q4ELFyltCaSuy8Sme_Z4bcZ2K2ghtc2ezs9saU41CMkAzV4_DZIl-gSXf-N1iG6UUKlKtpe2REi0IRx8xSS_pQco5cwb7lb2ue4rtSj0Plx95MBU5anJmaezcS2Ian0dvYbCJ9GyLg8zQeaBSBPy9Mtq7tf31woNucdsF2wiMHpJ2dNnnbfBO_JVdSc07f2ActiFl3CHc9vY1_jcgwF7eQnlqCYAKp8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS540ouf4N1USlP5K94RknOtSmnIpnm-_FZ8_E9QNVuER3sPHcousU_XqypzPfTCdWe_GIwvZlHH1bkHTMnjW0BI9jT6XUPihCbRrlOVYgYXW0c52IGrMl9lRkyrbkzudTRGg3Edyi3jme377sDL1LwHr3uLWW8C4Fts1p6WdKqdEmfLNxNSEsyhBy2jFrwk94zL-wYtU6Mn-Ml14RHk7ahwkvce5U00BW0ywCGbcuV4oIYmxx9wHC6iQzJAuGhhTx2Qn3PzDba_UNqdfnaHeYTcFZPTQ9u7c4aF17dUjCi7TkR_Fa_nybOFTuW5HE6XMpKTOLUxCVDVl2vlwn0c2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=fgVOeWgfRiFTtq1wIVH85IK2D-sjxSgQZt60v10Ix9LkkBRiijyyKoqJQnQgZqrUvnNUr9KvxSFwKrh5CnAGR31VZR2foGC9_BMEeDITERjcMTTX1YSgDWcsDeW-pUdtV-SgS9rtHTxgcnlLJ3FTGk8kO3rZoW8R0PdpKjdEFbbqzo4az2h4Aom5Uy6V2BinRcv9c7zf6zCuhm-7s-Bcr6pX6JEJl7iVJ6gd6qmB_MWIWwU8-1V9a5kFFPsuYtUGtUd9z3Nwg_-cBZFYZXjjtDF2-MJX7cYu95L3DJHBW4gWzaFz6bNeCuaF-SnJY-98jcorxTTPHTQyKypj-YoefQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=fgVOeWgfRiFTtq1wIVH85IK2D-sjxSgQZt60v10Ix9LkkBRiijyyKoqJQnQgZqrUvnNUr9KvxSFwKrh5CnAGR31VZR2foGC9_BMEeDITERjcMTTX1YSgDWcsDeW-pUdtV-SgS9rtHTxgcnlLJ3FTGk8kO3rZoW8R0PdpKjdEFbbqzo4az2h4Aom5Uy6V2BinRcv9c7zf6zCuhm-7s-Bcr6pX6JEJl7iVJ6gd6qmB_MWIWwU8-1V9a5kFFPsuYtUGtUd9z3Nwg_-cBZFYZXjjtDF2-MJX7cYu95L3DJHBW4gWzaFz6bNeCuaF-SnJY-98jcorxTTPHTQyKypj-YoefQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=bccZWK2wCASGqhPoiyLK0YdbwUUG8dV2sjJ7v2UkAG9al45SAryVQIQZedfR2LHZCh0_KCxJKRYOPz7e1Idgei9U7NZj2DpMXCMTVvz0cQnparB_9L6UrzYDoUJ25MbVgQdoV9Pufieum3UeI36e2FSUOLKHvMTW6avbNd4yspslAylLo9DY7v2wmADdgmXmOyFnELWJAF92GSK-lZ1zm05ShF17PBRSXZBptcsRzTejwKlJLW_atD1gRopkmqspNXdUPrHGdAZsChAaVEeOhtBtH3fXqerTxBp3xDAvXdEpmNjELq1S-fQcFAmkHdTMcAqc4xvrUmYioUM3ONW-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=bccZWK2wCASGqhPoiyLK0YdbwUUG8dV2sjJ7v2UkAG9al45SAryVQIQZedfR2LHZCh0_KCxJKRYOPz7e1Idgei9U7NZj2DpMXCMTVvz0cQnparB_9L6UrzYDoUJ25MbVgQdoV9Pufieum3UeI36e2FSUOLKHvMTW6avbNd4yspslAylLo9DY7v2wmADdgmXmOyFnELWJAF92GSK-lZ1zm05ShF17PBRSXZBptcsRzTejwKlJLW_atD1gRopkmqspNXdUPrHGdAZsChAaVEeOhtBtH3fXqerTxBp3xDAvXdEpmNjELq1S-fQcFAmkHdTMcAqc4xvrUmYioUM3ONW-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKhnRy93gcAdO7qnhbE2jZh_38bspSoY_OE-r8kTcrJybT1nDHunFU_QSJm1sefr6OE_5qW9R7pyUhN11yC91ZgSDUgSk26gAb45zlM_usMcR7YtLdtmJKMzo44RGojIRoZ67FR4FP2HqklhXgbuDlzNSP0icbKyaNFrU252wDWaEiZEfxQjNfS4lIroF1vALH_6AFe1MxgtvWAQDkHCgH3HbFpZuBm98hwXbRvEzGY4T6n8Rhmkj-oslg23suDdqCrxhepoFIgejTC5mZA0S4GNmP_5cFvTnxG4hpwBzWByvNzxYF_4OXybWWUK1kchsmcIiil3lWXaltdGW8M01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=BBzQWpSNby8pHVOmAiz3NhB4ah2Z0qZxel0ixbrUUYjJzNsfL1NgqsBLdrs0bOAfIBxt6IPIDsP71iXRrgKx3BQr2l7buknAIg1awaGJaExCK4A2AEuK9b_TpHWUBr-UPh8wwqFn3fsVcCoZy7HtwRYT3dUSxtcOfwcnZCTg0F1vqPDgi1Ik4t9P5stn9U6lGyQF5qfK458Qsmz4Ipn48QkNO6bL8oMNomG3G5Ip8pcHwNm-9KaOTLV18uP6RgSJhCRYzhPO1Sns-B2cCBuNAPt3wilSrCajmnPP94otiUX_hsbwDgtNb0yqIjueJ1YlAFovDMiOkvpolhBFULeHOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=BBzQWpSNby8pHVOmAiz3NhB4ah2Z0qZxel0ixbrUUYjJzNsfL1NgqsBLdrs0bOAfIBxt6IPIDsP71iXRrgKx3BQr2l7buknAIg1awaGJaExCK4A2AEuK9b_TpHWUBr-UPh8wwqFn3fsVcCoZy7HtwRYT3dUSxtcOfwcnZCTg0F1vqPDgi1Ik4t9P5stn9U6lGyQF5qfK458Qsmz4Ipn48QkNO6bL8oMNomG3G5Ip8pcHwNm-9KaOTLV18uP6RgSJhCRYzhPO1Sns-B2cCBuNAPt3wilSrCajmnPP94otiUX_hsbwDgtNb0yqIjueJ1YlAFovDMiOkvpolhBFULeHOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghGAO3uTbEledSllHl-adhXlKjvvvn1Mh2EHX1rKPmugwbxBEdPvYlRyDc6Vm6i8zJagmdXUP0T7IIr3wJPGwh6ue6kmYm-k8NXN95T1d3NTr6AIMHXQ92GMeSS5VGdhQKgRWaTYj4TWhey7MpHb7VMve3WVfh08J3Hnhh52DnpceeCNbz23GlfsldzxbVnmMomozVOdfnf-5dtiWwOOpme0VWtm5GyxYkJXGndnk3I0csItJiIN6nkXK4st3mAGZk2X6XyzSDcGFu67MmEib16QWn4B4eV3lrO4duUw_q9ZToKjIe8OWr-PHEf1zEMF-dDzREesNSSRMHnFDwK-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn7qg5x042PnI6vkkCPePqAjJ8if6bYQYzIehhh8vrKfTY-lcHzYFryvWTVOOkr4yCkz-387m7UgyrJZ1OA9NF5U-YaYOFFDlDkkVpbSbY7Xax2KvDHxKCS5p7IDDFheH6sdZvuWCoeP2-gNooEvHvgwwXGC07AwTBawxVPMImgYnWySkhCeuUigW5_TlkOfLa55-x3bEZUmFg4aMJ9phtqIGdfFHAr5_8fiq-2ZYocl45GSEYt55M3ezLPoWNikcwsvhHfnNSBFTVFwEJIvdx-p8OcK0y9pHqdUclLITuK-_FUa_EeQ3Rhx1g_3eW8W7Pw0A0KdB5wWwnwj5karuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=bVgQTIIDWxBTZpm8NTO1YwnCC5vQjuHBSsjTH_btDzzXeTfGHq1PcNzxmDUGq356giHjbDZjaQccg0Ci8VuLBtdd2mqHm87ERHxo8xIaR-3Z9NJnbfhd5a6ixjxF5BP19Er3rEgZ9aMBZOdPPI2vNOKvK11dbX8wEeb39hf99JaDiTaYOqLqJv1EAXj_rp4G5100hBsq4vn5QvIwQcOfWXI7TEiL_pclZ3wzQCxTJtdU12BXx-_bMLbytc6WVXcJAcGkN4ZeDpJ3yitnNpGappM1t2VBtLSHRjXZc2Q26NQ2yruesrxr_Kv8ohzYkUylrX7qEu1cOQFTRL1oLC7IrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=bVgQTIIDWxBTZpm8NTO1YwnCC5vQjuHBSsjTH_btDzzXeTfGHq1PcNzxmDUGq356giHjbDZjaQccg0Ci8VuLBtdd2mqHm87ERHxo8xIaR-3Z9NJnbfhd5a6ixjxF5BP19Er3rEgZ9aMBZOdPPI2vNOKvK11dbX8wEeb39hf99JaDiTaYOqLqJv1EAXj_rp4G5100hBsq4vn5QvIwQcOfWXI7TEiL_pclZ3wzQCxTJtdU12BXx-_bMLbytc6WVXcJAcGkN4ZeDpJ3yitnNpGappM1t2VBtLSHRjXZc2Q26NQ2yruesrxr_Kv8ohzYkUylrX7qEu1cOQFTRL1oLC7IrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=RpHvfwOAqWRB1YEIBIdGWg0hYY-s4MWABb1Fc4l2DwZoinA-9kYgC5fDpWH9vU6uNJwiVVSQvUtB8x-EmBoxYlUs9Ye7aJ3XN0ZkV0NTn4xEoGnkWipFFP7Qw4aSmIlYrJuiNaP8N2KjF1iy8akaKMX_Z4ySD5RRtXgD5nVW6WeGT9Ul-9-B2yVAT07jD6pQvYbGYkpj19HoDMPDIEDnaOlK6SWpdjE_t6Tyd2v4Os0G4hI3oo2kz0z6u6lx_yissIInmXlTraDi__uYwRrSg2-reEB26ckuMpkRiSD_H9KBqaSbxhNalM3JSWIdYgH4aVDzQjmbcaovhDpd3zlRMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=RpHvfwOAqWRB1YEIBIdGWg0hYY-s4MWABb1Fc4l2DwZoinA-9kYgC5fDpWH9vU6uNJwiVVSQvUtB8x-EmBoxYlUs9Ye7aJ3XN0ZkV0NTn4xEoGnkWipFFP7Qw4aSmIlYrJuiNaP8N2KjF1iy8akaKMX_Z4ySD5RRtXgD5nVW6WeGT9Ul-9-B2yVAT07jD6pQvYbGYkpj19HoDMPDIEDnaOlK6SWpdjE_t6Tyd2v4Os0G4hI3oo2kz0z6u6lx_yissIInmXlTraDi__uYwRrSg2-reEB26ckuMpkRiSD_H9KBqaSbxhNalM3JSWIdYgH4aVDzQjmbcaovhDpd3zlRMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT0upY2i-xcrwmjR_vVvlU48MMClpfPmI3ibwwPLHVmJyUSCq3-9veViqZaqOIrDLG1JJEKWKCDCRNOBPdgcTBphxhejlre7fa79UmY8q0Ve2lEd6PdCx4pn764JHzy5dOcp2YP2zIFNjoExPi2i8AtEue3OS6NJp7Nzx2ITfWm00eY8T7l5cMqeQieYKrdz6s3CYiJ6MBOHNP3M6xJ9SzU72LAnvChvIrQ_RPxo6ZhbI1IFT3D1pnLmVKWsbHnEYDvhYA0Q-D-nEg78a5QqJ673Fe5QEZncOxAlczy502UpZ1KJGigwiGY-kf_Bmrk7wTV4Cbqsnhh6iUccvuhb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGIShCw5TLAF0IZCMTO8-02bh1ZuuNlJfDhyYd8oPf6trXmpcP-gJz7Y11XU0rDjZkOeNkO7OR1SkEwLXWgCxKUp3g2669LQVCNRZqFJhVYHgI4JtBk3_KIor5hynLLLJsa82KxIZAMEAXnpnxRunNlFtOxPmFZDWcQOOesigwYO8euQh_hma1QM86mJXCxP_Q7P0cC9Wm_C5BM-7D-kMiURu-_serXVmUUto2WJE3VK-_v1oA4h5Od3BCgdCr0RlmLXFiY8dMZwfuGgTaGQ0Q5Gthv1RcjmRlNZNTHrATeQySsTrC_BmDo0u0phnoylPvcC5jIepHd_0yB8qDECvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=Kh8b3AO8yDE6MW3571pBvWbeIIUm__TqiXfDlZ6kzkjMEth6a-BVrIT2sbQkTFR1bgnZNhTjdPmM4RJGqRv3qjMBoM7nrgeXBn1FCT8eV3m_Yy28FOmlMBZyo0yX8qn71KW-xpykxLxJqjc1ZAvhXpXlOgZwHUk6sVMQ8n7eJTXA0p2Wh2hNuhYQmbhpxS2DZ9XtIDfHBwPnILjimZSa7Sxq5qo4JRmTCnkIbSKWLubBJz97DcAEXJuvXyBn0FayJf7UZwQ1UD-P4vtqp7E_Sh-ivGUUrGBitONLPvNfSSeVthukyA_FlFH37DrI7-HCtC_-EGIO_5I61gWGWlfWHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=Kh8b3AO8yDE6MW3571pBvWbeIIUm__TqiXfDlZ6kzkjMEth6a-BVrIT2sbQkTFR1bgnZNhTjdPmM4RJGqRv3qjMBoM7nrgeXBn1FCT8eV3m_Yy28FOmlMBZyo0yX8qn71KW-xpykxLxJqjc1ZAvhXpXlOgZwHUk6sVMQ8n7eJTXA0p2Wh2hNuhYQmbhpxS2DZ9XtIDfHBwPnILjimZSa7Sxq5qo4JRmTCnkIbSKWLubBJz97DcAEXJuvXyBn0FayJf7UZwQ1UD-P4vtqp7E_Sh-ivGUUrGBitONLPvNfSSeVthukyA_FlFH37DrI7-HCtC_-EGIO_5I61gWGWlfWHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
