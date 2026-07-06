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
<img src="https://cdn4.telesco.pe/file/C6txvn9JkJnSBQm7zw2oyDdriv7RnqhI4NJJF7OctIE5w0hLwzjNSnM4-vGp-g2_cn-K5YX2cG-pSb_3H6g6BUx0jjtAM904zGX_V9b2zljUqEnkvbriRP8lPd3-oHja_iGeS_FUX51j1UYSbTLUjV5_lIvIs08DfcAej4btwslyj6QiJv8JYnIZmc-WPAN2quJ78aFwo2dLFof2cM9aLE8A0EPIxnPNAJGHzLAqk9cM5NIJgqO3GJM340h86q1f4jc_L0vzJ9-6Z5WRj3krroZ8wBYOaeB5k7qYZPmfaVva224aGUNbkbNcIFF26ZMVQ5S59wG7NouV33HGZGzxAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 02:28:55</div>
<hr>

<div class="tg-post" id="msg-447759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0690d9ce.mp4?token=erudLzww1Pgsd6tdI8y01SyoWEK8M2Jr99cR4y60L1fuZnIH9UEaCh2s34F6ZadfkNVbx4TvElkM8lu4uidyUPgBIZ1WziZwZ2f9zjzE0BZx_zioneh9dOkRWY-iBz3tZK72nnwgspA6YVriVX6WCIsnAg-w9jgW6ry4aH2tdS9YT6SSnOnWsS5R4Fv5jQmLU_KXzMUsKiSfBxcoAcFT4azcT0eZHWE2WaN7YmwDl3J4IB8dZuXRU5onbkHSCU1TXPQguNrQHOk3Wjccy7QXVW1VSwkZN6CIksEUaf-IklchuQ8yLbwmobymHT4YLw3G01vlnUXTx3nP97cjOQy9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0690d9ce.mp4?token=erudLzww1Pgsd6tdI8y01SyoWEK8M2Jr99cR4y60L1fuZnIH9UEaCh2s34F6ZadfkNVbx4TvElkM8lu4uidyUPgBIZ1WziZwZ2f9zjzE0BZx_zioneh9dOkRWY-iBz3tZK72nnwgspA6YVriVX6WCIsnAg-w9jgW6ry4aH2tdS9YT6SSnOnWsS5R4Fv5jQmLU_KXzMUsKiSfBxcoAcFT4azcT0eZHWE2WaN7YmwDl3J4IB8dZuXRU5onbkHSCU1TXPQguNrQHOk3Wjccy7QXVW1VSwkZN6CIksEUaf-IklchuQ8yLbwmobymHT4YLw3G01vlnUXTx3nP97cjOQy9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگواری زائران حرم امام رضا(ع) برای آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/447759" target="_blank">📅 02:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikuBquKy13veX30hmoCs9qusJBle72PsOj6ijFGfqvGhliw-rAdo-xHXWZlRMinoDzcprsVeOwZN776nEWrFdHVcPUMnm5fPM50joHemAOuXMwcyTSC2N1e0jwrKeuVUf8oelCL9IFam1vHG0fcd209jOz5iK9v8nHOCSU44nU38eXCcbziybEjV6tcliD1IrpHIqiIJVYylgKDaugjF0XMlOoD9ROSEraSU_lvmPwsD2TMBLAhaN9EmCPjyuBjOtrB6Q5LRxFTXvT3DzgytNvYbV7aKspkV_yfxwhkSbIlnBBe7DDcChpxVLKftxBqXLAsQ3GfVf2yhRf-p1P6aVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">التماس رئیس‌جمهور لبنان به ترامپ برای خارج کردن اسرائیل از این کشور
🔹
رئیس جمهور لبنان شامگاه دیشب ملتمسانه از آمریکا خواست که برای خارج شدن نظامیان صهیونیست از جنوب لبنان، به تل‌آویو فشار بیاورد.
🔹
جوزف عون، که تسلیم‌شدن به آمریکا و اسرائیل را به مقاومت در برابر اشغالگری ترجیح داده، گفت:‌ ادامۀ اشغال، مشروعیت دولت لبنان را تضعیف می‌کند، مانع استقرار نیروهای مسلح [لبنان] در امتداد مرز جنوبی می‌شود و اجرای توافق‌نامۀ امضا شده در واشنگتن را زیر سوال می‌برد.
🔸
پیش از این، دولت عون با
ارائۀ امتیازات بسیار بزرگ به صهیونیست‌ها
ذیل پیوست محرمانۀ توافق بیروت-تل‌آویو موافقت کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/farsna/447758" target="_blank">📅 02:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447757">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qArV90BOczv1u-TOFJam6lslv7Ry84d-vRb0b3YCeDHZ6Osi7YuMKiXUmCqQIYQ9i1ULsrDegultl_yM8OhbHuT8Aa9pDwUgoQkGwy-75tf_0Klke81NlJWKqHpyQI-L9c9uLRfdCDFVDSHrbb62GtElzYB5B7M34yBkrd1i3bBHn81wZwEmT21eBHz9YEH5qlR_dPuVP7aZa56-S5Nu2tlk6zegg4Zy7y34wbIT2CHy65jB0635E3qLsCrMZkEDQpAmqbQcwY6GMjpy1F-p9LNCCI3CwwzX5BKNZVUCoJM0UTC7VsZfo90BIp9b2NJSxSYg79L2HA6hIeoP_Wp3pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو: این آخرین جام‌جهانی من بود
🎙
کریستیانو رونالدو:
‏
🗣️
من ناراحت هستم، اما تمام تلاشم را کردم. این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ ادامه دهم.
🗣️
پرتغال قبل از من هیچ‌جامی نبرده بود اما حضور من باعث کسب سه جام ملی شد.
🗣️
نمی‌توانم تایید کنم که این آخرین بازی من با تیم ملی است یا خیر. تحت تأثیر لحظه یا احساسات تصمیم نمی‌گیرم.
@Sportfars</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/farsna/447757" target="_blank">📅 02:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb0e831d3.mp4?token=kPaT_ESC7Mc2x46jCIzRMcXdV6YFafngz0LS7iBBDbZuPvuKUb_4nkXJmqNG0KA8Ac3-SBJBvB0c_a3_XGdbEMcsEkdiVV46YHZw7Su7W1ACGbLU0BKMKGgZvQ-9t7MHh-UYiKo3kRDhnQcEwpyAEPK8VqxEHg-hbDS9nzzaZgKDPjxcUrFv4aXYXQtQ4jcGSCPpqSa17ZBoC8cLdS9D9ZG0NBquV3jJX4sy52VzWU39Lz_EUB8utgvrbzbA7ZjUEXBf5TgRYNDN9zckVtL13fKuR0SPoZucPEhs1QTN4lXERYCrkMG17nHH_tg4FBHDZD-rV1PPZMhlYEQTd_lPug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb0e831d3.mp4?token=kPaT_ESC7Mc2x46jCIzRMcXdV6YFafngz0LS7iBBDbZuPvuKUb_4nkXJmqNG0KA8Ac3-SBJBvB0c_a3_XGdbEMcsEkdiVV46YHZw7Su7W1ACGbLU0BKMKGgZvQ-9t7MHh-UYiKo3kRDhnQcEwpyAEPK8VqxEHg-hbDS9nzzaZgKDPjxcUrFv4aXYXQtQ4jcGSCPpqSa17ZBoC8cLdS9D9ZG0NBquV3jJX4sy52VzWU39Lz_EUB8utgvrbzbA7ZjUEXBf5TgRYNDN9zckVtL13fKuR0SPoZucPEhs1QTN4lXERYCrkMG17nHH_tg4FBHDZD-rV1PPZMhlYEQTd_lPug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ممنونم اگر نروی، میمیرم اگر بروی...
◾️
گلباران پیکر مطهر امام مجاهد شهید توسط مردم عزادار در خیابان آزادی تهران
@Farsna</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/farsna/447756" target="_blank">📅 02:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba1c4bcc.mp4?token=vxsP9nGRW591MH1qHXggBFVcuC3NM8y6TGYfyUgtc7CEr-RR_sJC8gIDxs_vlSx-kGdwofwG3apMOsXpZlwxxTT4JKEdUAnsOPGMDYcFMaG_6pR-t888v6dxR9cwGDDQP-64P_zsNBGLyvYV9xrz_t7_Q0bEzR1lxFPALCV82QSezsDNZajvQzyst5jjEx4pNEe_rGVzZINfDSgM5boDq24ZiaBOZpg1A7gSsK4qe5z1EvebG0VJYhvpsO5ghD6-ulq9N-aclWJRw2-kaBKSbxL7C7Jy2EsQ7v79B2BOPel5-faX2F-ZqfmB5RyNGxURJTT9ojHdV7DT2XiAA9OJWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba1c4bcc.mp4?token=vxsP9nGRW591MH1qHXggBFVcuC3NM8y6TGYfyUgtc7CEr-RR_sJC8gIDxs_vlSx-kGdwofwG3apMOsXpZlwxxTT4JKEdUAnsOPGMDYcFMaG_6pR-t888v6dxR9cwGDDQP-64P_zsNBGLyvYV9xrz_t7_Q0bEzR1lxFPALCV82QSezsDNZajvQzyst5jjEx4pNEe_rGVzZINfDSgM5boDq24ZiaBOZpg1A7gSsK4qe5z1EvebG0VJYhvpsO5ghD6-ulq9N-aclWJRw2-kaBKSbxL7C7Jy2EsQ7v79B2BOPel5-faX2F-ZqfmB5RyNGxURJTT9ojHdV7DT2XiAA9OJWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بامدادی حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/447755" target="_blank">📅 01:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b606cf8c9e.mp4?token=kZTplAIBJMRXSSZ30K-C48o27wXFYFYNlrIbPqcDh586OYXVmSEW5E1V0TSb1cydkRORUKb4InjfGDVopVeyQ-5n9Yyzp9p2lB1Dly3Hf1noBTU9C647GTpJDoA4UOv-rEJ_pezbuDdt81bGKjrtDBcdBGa_6CvMPCpr83Yu94uni62jVvmjJjYVfNYc3Es5KSRBa1_k47YUu7gD2TcPj5gv_Zf4ytkjlemwRUXahRrxbToHGes8aODtFKVN7qMO-m887JivIennb3R4QnEGFLXfM7m6JxkzTWZ3p4xuZdBdKozoxNSE0hX2gKdavDDFj-ctfVefQhtJjjfnZQZq8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b606cf8c9e.mp4?token=kZTplAIBJMRXSSZ30K-C48o27wXFYFYNlrIbPqcDh586OYXVmSEW5E1V0TSb1cydkRORUKb4InjfGDVopVeyQ-5n9Yyzp9p2lB1Dly3Hf1noBTU9C647GTpJDoA4UOv-rEJ_pezbuDdt81bGKjrtDBcdBGa_6CvMPCpr83Yu94uni62jVvmjJjYVfNYc3Es5KSRBa1_k47YUu7gD2TcPj5gv_Zf4ytkjlemwRUXahRrxbToHGes8aODtFKVN7qMO-m887JivIennb3R4QnEGFLXfM7m6JxkzTWZ3p4xuZdBdKozoxNSE0hX2gKdavDDFj-ctfVefQhtJjjfnZQZq8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زبان، از گفتن حرف دل قاصر بود...
◾️
هر کس، تکه‌ای از دلتنگی‌اش را با گچ بر دیوار سپرد؛ شاید نوشته‌ها، آنچه را اشک‌ها نتوانستند بگویند، روایت کنند. نماهایی از این روایت‌های دلنوشته در مصلای امام خمینی(ره) را ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/447754" target="_blank">📅 01:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OduDiyp_L5jZJF720nfVH-T7TCY6AQox9qYCysJRDtR5Gfg1TlAH33tXxMJ0F9RfG9EyhIdh4GR1kESmGmTE4ZPwJiQtR9rWFEOCEg7IKpFmLaiU5K1V9HPmEYwRM_j0S0nusfYq_FBA0tKTf71bHy3cYMvykLF-fObSCM96F9voBnou6VMMWDMVZwg8Rm6KNE9ne4FD0AT3fzN8OuBV7rGfzR6mbOP5Y9UqqXxBpu2Y5Ngt8NdGSXoF4u7fFLBx_nEBhkPANIjte_ZIk_INuLWKurhRq4QGOww7ylDHEhdBqQu2JTrpZ4vv8kggT9p1hheq8nkHREPn-efKRKjxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نمودار مراحل حذفی جام‌جهانی پس از صعود اسپانیا
@Sportfars</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/447753" target="_blank">📅 01:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447752">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de640b817.mp4?token=hxqIR9eqNaec6NurzNAawjKWrvWahlSQpzzwfvuQdHaezhFGyjwAOUQ_ODJHjghLZMhYKcarNLhpPazEO_oJBbf57XU1Nk-VJJPln1T5g8bJSbR4IJA9ryFyKnjsb9pIEalcIPrxoPNcH7sBSqBUnWhUykUdjxTaBn-kdOgPyXTF5qyzL8d0EjTVTkM74wxmE-1oZU_gTin6GP9nRkh2Hj972_oXwh2ep8Ctz9Hpj1ib-JVEJYkKdLtsIoj1EkikWCJKBRG7ZNYJdApZ3lRY5vpUYAvrt9OP06wS152Yi5jIs-gxPuH0C_2b1nH4RH8jdide6khcb4CIQbBGxBG5Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de640b817.mp4?token=hxqIR9eqNaec6NurzNAawjKWrvWahlSQpzzwfvuQdHaezhFGyjwAOUQ_ODJHjghLZMhYKcarNLhpPazEO_oJBbf57XU1Nk-VJJPln1T5g8bJSbR4IJA9ryFyKnjsb9pIEalcIPrxoPNcH7sBSqBUnWhUykUdjxTaBn-kdOgPyXTF5qyzL8d0EjTVTkM74wxmE-1oZU_gTin6GP9nRkh2Hj972_oXwh2ep8Ctz9Hpj1ib-JVEJYkKdLtsIoj1EkikWCJKBRG7ZNYJdApZ3lRY5vpUYAvrt9OP06wS152Yi5jIs-gxPuH0C_2b1nH4RH8jdide6khcb4CIQbBGxBG5Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم | لحظاتی قبل حرم حضرت معصومه(س) و شعار مردم با فریاد ای پسر فاطمه منتظر تو هستیم  @rahbari_plus</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farsna/447752" target="_blank">📅 01:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE9d3aYsnoOBwazn3E3ROahwqCKx_32tqfWfKcVJCF3C2_8egQY42TaQlmiHRnIInFe6ERGPZ9xxucGrzL4AoV6eL3nIBRhzoobNUnUijfvtGD-Hi83WkeZYD2sEyBeoZtdde3G3ENrybL_qcxmDZC-2tycOu9-6q0Vm9xn-P6vknPa1D5UmhcSyc3MT9KGiMwtksafVDmKG7XbxR49Fgpy2AESI5rXGJCv8wI0R13yr8BxnRzBFCcrWBsf_cynrD79rsjd-SN0N9tt6WWo5n-S3sk0i64VDzQFtnWzmf6-9jUxjK2nD4g86WJADmZXNJ00sqM2uVLQ2Umm9FN93tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
استانداری کربلا با عنوان
خیر مقدم به اولین زائر اربعین امسال
به پیشواز تشییع رهبر شهید انقلاب رفت.
@Farsna</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/447751" target="_blank">📅 01:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4598f64be3.mp4?token=eOV_qoBGKCDkAv2QNNg3Fd3tlkX4Jial2Uoq-DHLZngqini6EXZeyqP1ceOrbmpjHOTu56HsqT6J3ry7XLka79hvsoFq_AGlGFjXzBPggMjggLwYYQVGcs_M4lLW1Kt1YVZYCxZK3IZfxjOF8Fhvrym9rcDQ0PuqO6g_fYSmFwjQUzy7sQC9PQEyzGMDHX-J9DNOpXAibbbk5o5e1617YYqwa5hCqXIhN3XzCMRuipM1qVMQ3pSJt_lh15YEagY7MBXrHHk9IZRQA-MwQfFAgnGT4XOe0GZLB7ZeBxMtmGnnXrJdUqwF5iQNG6elc6xeMxJoPJPmFQiDJd7vZ1PX0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4598f64be3.mp4?token=eOV_qoBGKCDkAv2QNNg3Fd3tlkX4Jial2Uoq-DHLZngqini6EXZeyqP1ceOrbmpjHOTu56HsqT6J3ry7XLka79hvsoFq_AGlGFjXzBPggMjggLwYYQVGcs_M4lLW1Kt1YVZYCxZK3IZfxjOF8Fhvrym9rcDQ0PuqO6g_fYSmFwjQUzy7sQC9PQEyzGMDHX-J9DNOpXAibbbk5o5e1617YYqwa5hCqXIhN3XzCMRuipM1qVMQ3pSJt_lh15YEagY7MBXrHHk9IZRQA-MwQfFAgnGT4XOe0GZLB7ZeBxMtmGnnXrJdUqwF5iQNG6elc6xeMxJoPJPmFQiDJd7vZ1PX0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مسجد مقدس جمکران ساعاتی قبل از آغاز مراسم نماز و تشییع قائد شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/447750" target="_blank">📅 01:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edec66bb71.mp4?token=UGxQDHEd6jA5b4OiLwsEm59QsidRg_wtCgZY9_QHGiGcR8X63nzjKwcOO-I9j_QOWOjfSDC9eEXUGsZk8hZjyccpA02C0nhI775G455iKRvYe6dKGrRI0k2dksJIizDDA1ErXtB74DtAKgHm7rjUOyu2UtNP1YaRsZI-IGeRe2-pMxTa-bpixc_4X7yKIGO8rOdYYhP3p-hw2WBZzdexLk54qhg85nWMoLo53qqiMkxR5_mKMm1BivTNkYOWww1F26qMZ5yFcGEN1tv6ZHxGRLOBLfukWkQGrElHPsePyxwBlhw6g-cgZkAfEUWxL-dVptihYZ5vz7Ew7-qcngdtRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edec66bb71.mp4?token=UGxQDHEd6jA5b4OiLwsEm59QsidRg_wtCgZY9_QHGiGcR8X63nzjKwcOO-I9j_QOWOjfSDC9eEXUGsZk8hZjyccpA02C0nhI775G455iKRvYe6dKGrRI0k2dksJIizDDA1ErXtB74DtAKgHm7rjUOyu2UtNP1YaRsZI-IGeRe2-pMxTa-bpixc_4X7yKIGO8rOdYYhP3p-hw2WBZzdexLk54qhg85nWMoLo53qqiMkxR5_mKMm1BivTNkYOWww1F26qMZ5yFcGEN1tv6ZHxGRLOBLfukWkQGrElHPsePyxwBlhw6g-cgZkAfEUWxL-dVptihYZ5vz7Ew7-qcngdtRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج جهانی دلدادگان رهبر شهید در مسجد مقدس جمکران هر لحظه پرشمارتر می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/447749" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d73e666c.mp4?token=PtUqmKE5pgB5dLeWRv_X8vXUARjsICUsOTHm2UmlKMMSbeeacYxExtJDM4duIvL22FsKCdZwlKdv4SBpl3aMTd0N0frWVElZQCAdx3LQmL0BYxt5o7zuD73aIIyDOgDEhu_EZ77rsrMBrYmIxY6Fdra5uIHJ3kJPAsNy6idhWXumuzhXAzbYFmlJ64fQCJUlzljMbkILsMmovt2OpOjfrD3R8gnPFFyHVXvXHu_RVBmSFjHYWGHobV6oyfjhOzBRNed_HeqJNabGtQaW-rx31bIDJuZA_dBgUdu8Azs_vFRasoH4Vn-DRVNeWQuFE-Lcjmm2-DHNbglu8d7SeNLPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d73e666c.mp4?token=PtUqmKE5pgB5dLeWRv_X8vXUARjsICUsOTHm2UmlKMMSbeeacYxExtJDM4duIvL22FsKCdZwlKdv4SBpl3aMTd0N0frWVElZQCAdx3LQmL0BYxt5o7zuD73aIIyDOgDEhu_EZ77rsrMBrYmIxY6Fdra5uIHJ3kJPAsNy6idhWXumuzhXAzbYFmlJ64fQCJUlzljMbkILsMmovt2OpOjfrD3R8gnPFFyHVXvXHu_RVBmSFjHYWGHobV6oyfjhOzBRNed_HeqJNabGtQaW-rx31bIDJuZA_dBgUdu8Azs_vFRasoH4Vn-DRVNeWQuFE-Lcjmm2-DHNbglu8d7SeNLPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
لحظاتی قبل حرم حضرت معصومه(س) و شعار مردم با فریاد ای پسر فاطمه منتظر تو هستیم
@rahbari_plus</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/447748" target="_blank">📅 01:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705f58c0f6.mp4?token=Uh06a_9ZlPU-J3X0GzVYyzT9YGxR-UDuhQBv_Amya1OZ5bAYZIEQf9D3_fydgVq9ksxgFRuXhnFsRs2GCOpL6i2LNBD_E65wn1whonBcWzXa8J-6uz69cY44WT__10JFGU3qsSud2djsC6cCHAuW3j2XuhU0Yh4XM2L6StVjem_U2HtviiyyFAt0z-dQVJ6yqsQHWzHbGbliOX4t4S7RU2RfMdTkKaawsi9WQ6NCi6oIegVYvrO8bQLqJVo8oiUUNuHyA6sL4JwU4xU6hvBYEzBCag8Zj1T8opssUkmuOq119axjnrPTljYvqPs-jVp6X6whYHWahMLQdAEaUUTyVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705f58c0f6.mp4?token=Uh06a_9ZlPU-J3X0GzVYyzT9YGxR-UDuhQBv_Amya1OZ5bAYZIEQf9D3_fydgVq9ksxgFRuXhnFsRs2GCOpL6i2LNBD_E65wn1whonBcWzXa8J-6uz69cY44WT__10JFGU3qsSud2djsC6cCHAuW3j2XuhU0Yh4XM2L6StVjem_U2HtviiyyFAt0z-dQVJ6yqsQHWzHbGbliOX4t4S7RU2RfMdTkKaawsi9WQ6NCi6oIegVYvrO8bQLqJVo8oiUUNuHyA6sL4JwU4xU6hvBYEzBCag8Zj1T8opssUkmuOq119axjnrPTljYvqPs-jVp6X6whYHWahMLQdAEaUUTyVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از حضور مردم در مسجد جمکران، ساعاتی پیش از آغاز مراسم تشییع امام شهید  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/447747" target="_blank">📅 01:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447744">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2346d154fd.mp4?token=vZVsEABVce51RI9pqyqDIujijVN2T_RKVQ3W9GwWl_CWa8ghRSOgbsplzvUvqXqkS0gH-4jU0d_N-QdoeDR6SdJy-nKpyuzxhhQ5tAskjLz1QE83nm6SbgT3ICOAEIVPx7Un6MBp2IDP32e2qtpO2EKvtKFAA_aPoVKGxkDM5YhLvhBZ9PlfpKWsnA1D6GGDn4vs2gkbJwH4rwIHsDP7oVN0afMQLco5FOuqwuDrx_FlkcYB5hwBUf30z1RNH7YaNdMmvVvSVs8Wi4a4O4eYPzqgf0oVltk1f2quwvZq0k1alWeXPThtwfz27S_QPBVLpLkAqolV9A_BJtm3Sxo7QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2346d154fd.mp4?token=vZVsEABVce51RI9pqyqDIujijVN2T_RKVQ3W9GwWl_CWa8ghRSOgbsplzvUvqXqkS0gH-4jU0d_N-QdoeDR6SdJy-nKpyuzxhhQ5tAskjLz1QE83nm6SbgT3ICOAEIVPx7Un6MBp2IDP32e2qtpO2EKvtKFAA_aPoVKGxkDM5YhLvhBZ9PlfpKWsnA1D6GGDn4vs2gkbJwH4rwIHsDP7oVN0afMQLco5FOuqwuDrx_FlkcYB5hwBUf30z1RNH7YaNdMmvVvSVs8Wi4a4O4eYPzqgf0oVltk1f2quwvZq0k1alWeXPThtwfz27S_QPBVLpLkAqolV9A_BJtm3Sxo7QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ساعاتی پیش از آغاز مراسم اقامۀ نماز بر پیکر مطهر رهبر شهید، سیل مردم روانه سمت مسجد مقدس جمکران است.
@Farsna</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/447744" target="_blank">📅 01:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447743">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de20f9d08a.mp4?token=vFPtP2iPBhaWGjmvpx_k7fKuM5sSgU0ko9W2HjFMCAL3F081EXuhk9ksufy0Oq_bgONCIaLQznyynNWh5TZRMqUOAUQFm0g3MzwBXSFbN20nqwlLiyS7XgzrvjGKMJu_YJ1oneP_peyk2TOHsk-xGYd87GBaFtoduiB7pIGo48Soz4es0T22NLIcJOkj1I9KKpRcz2S9EbGjCj7_FtJq1GHRTA64X4QpSd-YktMvekqfLcQsGO5jou24Ci7lle9RUdZCo6oe0UabFv56GyBjY8FaI9lRG0V_79ghC0ICjYL4q18qjUz2kwHlZdaRNfkN_FDBOjeag9sYFnV4glxQiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de20f9d08a.mp4?token=vFPtP2iPBhaWGjmvpx_k7fKuM5sSgU0ko9W2HjFMCAL3F081EXuhk9ksufy0Oq_bgONCIaLQznyynNWh5TZRMqUOAUQFm0g3MzwBXSFbN20nqwlLiyS7XgzrvjGKMJu_YJ1oneP_peyk2TOHsk-xGYd87GBaFtoduiB7pIGo48Soz4es0T22NLIcJOkj1I9KKpRcz2S9EbGjCj7_FtJq1GHRTA64X4QpSd-YktMvekqfLcQsGO5jou24Ci7lle9RUdZCo6oe0UabFv56GyBjY8FaI9lRG0V_79ghC0ICjYL4q18qjUz2kwHlZdaRNfkN_FDBOjeag9sYFnV4glxQiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از حضور مردم در مسجد جمکران، ساعاتی پیش از آغاز مراسم تشییع امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/447743" target="_blank">📅 01:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447742">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be6e3ce38.mp4?token=omm6Tsn6Iy3Gcb65GePBKCdPFIoJGVLgiNPkoKRGuzjxCepiec_nF9K10CVhyaSoHx7ncW3_qADvCpQXP6fOZTxqhPAPDpwEJ0ya_ZU4_ODS902BB5qOm3VJjywA4-PAawDvdKezMSbJC9V-f_evKtZSOmi5xQ7w_m8mImOK2-Jz9MsNJByL8WAK8TStMX-Rv9is26VC1LMFKGzl2sqWabRztlw43Zmbc66GdXfF4q_QVc1GMX01i3k8X2ldmvfZ1adK6ippcdVez0HWPKP2L6StzgdY5RJ_Wrl32vRTHcuqXD1CyNHLmgtmZnjIUVKZQZmZS-36pz1KRmS_qPUfuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be6e3ce38.mp4?token=omm6Tsn6Iy3Gcb65GePBKCdPFIoJGVLgiNPkoKRGuzjxCepiec_nF9K10CVhyaSoHx7ncW3_qADvCpQXP6fOZTxqhPAPDpwEJ0ya_ZU4_ODS902BB5qOm3VJjywA4-PAawDvdKezMSbJC9V-f_evKtZSOmi5xQ7w_m8mImOK2-Jz9MsNJByL8WAK8TStMX-Rv9is26VC1LMFKGzl2sqWabRztlw43Zmbc66GdXfF4q_QVc1GMX01i3k8X2ldmvfZ1adK6ippcdVez0HWPKP2L6StzgdY5RJ_Wrl32vRTHcuqXD1CyNHLmgtmZnjIUVKZQZmZS-36pz1KRmS_qPUfuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت در مسیر منتهی به مسجد جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/447742" target="_blank">📅 01:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447738">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p48h0SsklRIKGxE19JOUR56caC0RxQs3acnewoJcGs5JU_imHo-2YMbt8VkKXwK8supk6IEGjObhprsN62GreDNbhu8x4qI-MUfDqoVYgS2WiH2KHsZ8-xHqSB1ln-hWKRJwQqteuINRD8ahAwlzJrAsLMBSFgNzFeA5UOMMm9ftfzEmGL9Cy0pH8ZSnlWtFBKBw1wb26PEZcniTLwZ1_TB8DRakZnTS2oLzPEkb0YV2bZqSjlJUsi-1C3AnVgAP-5E_p49xfyoQLBRLMX8wEj2S8854Y4YSnsYTwhf9liRUXv_7HCoZS0bTfjEg5rKm_hvot39CV659gubTy9B-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcXZPDm7Ozfv9HWkXdgKOGVAT3eRBc345Oyl3P4onxLELlvlUgZa9FSbwjbJdgHl-f58R5n9paI7Jqd8-P6_cogkLcwZR254PJD-6HgyAlpRo31aqz2K2Jf7LKwppTooz8r2C5xwCsNjRl55SPlRfVkKcI07xFgEcAle_tKkxIhFXhqxbaXQ0DZzwR2oOeKNgS_rP00D_FfjCKGjDsvTc7NTd2bR9tl966L1o6ywzmzuSX1S3Ts6HjFmBHF1VsLT7Hcm_6qf5c3uVVqbv79ixfMHfFe41KflYBR6E71TNyWIBEQ6DbYVuWv2NnUpXhZmDOf7BnWN3K93gtbn-wdMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfAABwvLl5DbbfsjiBRlWb_Uh-pBg2ZlpLxI0sarR_T7x7yujMZZLAoQQnkAkBNdNxSBcZqwoO0Jk5BwNGQySa668fQJHjHkxuiPpOXVz0jF8nxiMvBaj-VFznztA8j3SajeoQw_Q69CUweUPKYhOxlv0AteHuHm-mCJisFnXnm4xKQYMYROFYOq_9pRHX_ZVqZyJ6ZtwfGGnGcXRgUKTlnoEAkHOSggc7u9d6iQbT3kwZu90EnCM9IrJTa6HYUYiuO0U7hlXFLkgD6DsnwU2qG8LoJm8xNOQPh0ViE7MlJkprLPggBXYuuxOMMFE4_V9exXed5H70jsTH9hQ2YXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NulEDn0jEfZUuz7tbYRdbKuehp2lq_KXN5Mfvn_T2ClaO0bIrBpOYniv_TM33ZMlvFCT28l3ATQUCTS4FHN9oXICm-ldxOeeecL3tdYHJgNS9sMds91Yk1OUww4QKcBeEoIcwq8BiwkScilOS9copt8HEGsI5Iy4P4Mvtb5671pAL27DoAeB1Jm9oWPqZBKQoOpCUJfH_7pQmmfHQAoxv3xQBS34wjLn69dpF7xizL8lm773YLuPZpkaPmR9ZFgPqOhTBmviigQBHnAc5tKUauzOXJV2U4Cx7oeCMov937tNZ1d4DxLwYebOK7L8QNQ2xKBG9fnhvtWbExyygAGWmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۶ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/447738" target="_blank">📅 01:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447728">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwUuBY3ddvD0wcaBCpNojNyycup3384OaZoOtSt3NLyu7O0vXigVQ-QpgN9UW3z07O0X9HNOimQ7mvoJjeHHUa6gPWuUKekYPESKjCnzaYP5R7y5srFxBfkpMDzTD9iKb1zKCdrmclGD9a3nkrAWW3iNSPpFVrtCA4sjg9thND1Vbg2lAbbmSyq-TDZSTGNs88TD8JCvzqzoid8wvQUkfs9x5kdMB0gYQpNmUOhjhxx73UEoxJYixmQ7_-q6vYdDsl6_Xd6GdZVntkjWPC1Z0bLMS4qg-ZQMj6hrI0OQqgSkjxSCzoGOgprEMxKgIrQH7RYceeGhn58fpt5T1qqHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vS606CWzhtUCb_48Qgj9enIcl-MZtcagkkEkZiQQ21bH_pwLMUpQuGvgDCcH8Ktk01lDIfK60eHiY8pG4sNA5MYeJagJJscOcGt7-Q-iJaumwUa0R_x6Hkd1T3nLbeoHygzUsz8WknebNDe0eJyJ9bP7EhG66cn2jrNjrpcz-74CnACoYHkztD0cx7DPqqkajwfot3Rcw2ETiEDUwf1k2928P_6PePIpUGrG3Fs__qwZ9O_lyggDhZzeSw_Oa47Eoc9FkR73mBjGJ_vCGP72vPImv86LIhbwfDsqQX94_nmJuGc99IF3V49iZsP5dHXUSfCPsx44d5lTSaAO-RkR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-vcZWDTZ4IE6SBWyaCIwMCnCum-0qTG2veZ5wkAiVVHlAp3B_G2YtAWPGxdzQ5SKt_eZ536DHlsbt_8WDOIHdZd_xU3F6CqQzxWVBjrtNsrdRBURUZY6ZwUet_Y2aH38Np5gyV7wnF5G7wHM8VzX9nlSqzDJI_owvGrZ_vB8wmJtDplc3j44QhW0jCTGJRUs9-yHhG0t_Wpb8ZXQ1VjzZcfx_BCoNBJwRhXhDw_VyZClIQ_lxk-O2sx8dMDKqYMm05lAgHN_Ogv96pVWHpNXNfl_PlI0xbjUO_l2xbfAcYwbIE8jb7qaBvfDJItjGCfN2Wu_ZVxKRW7Z2HjVI_jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQ7bvTI2EmF57X3ZtbYy589YmPhGokyJO3Ty-aM-DIxF6OAe31bWSd0lr-AAbxqRtw9vsfVlereSrznRzqIKIrSOKuOszT-DL3Umitey0sb8drcxHlITrMLriqAhT6KWqCVntysa-L3J7RBh5sqSsGL_FKb7zDSNAueeKf6TePm_ESBd3fjx9HY2RG7gFZOr6AUdZyl3jfnayCgbyvQRXSIIyUyi840bPGoyOv3vRa7xKhCie5fZpytqu4691wS9IsGMMNXxEyRgUpphYLOBvG04q81NClqDtCTXelhFobtyiSLwUXAJyVtP2v_fXGk53i1OtVJ2WKp4g_c_fRBZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoxzLU9mwIPzlvaPvmi_vAynq-7FWm20sYMK9Rexr1QbvCmvkRNR661baKnrE_rVsmCzJQo_I9NqAoxseUcTfDqI7P1RnkiEbwgDL4pi4fxvH0uSjBctOPcDyZz66BYunFxza2X9HquiQ4b7UD_zXLprzpaNW_zUuzkuSNo1MHXJm0DuJJC1kzxjYwPQrwvr_ukByAbXVUyczqyi6_QsEWqnOb_q7pofGaA6kx9AK6gKNVkKrZd55G0S6vPHEk5qT3-Tkslwebnp-Wfajbo2htVJFU5RGqmwteMCzLGX2LBGMTPG5CX32k8Je7XIQyIMqSO_sk_q2LY-WouHyM00XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kx9oEIYdF9KJPBlZVDUdImkyrF0X1K9c3ZCBBWPJvP6A8oUsOzfVV949jSubteSDVbW-xIbLjetDdVQF9bhYqNwoeVKl9uD91-eX2MZ0efXuZjD5qZopz2Zltg70mF_AHleuo6ObRk0_xsavCxf0mUWZJYHd98uHYwpdTZAPiLi7G-TkjssSYM4wGtPqG65deZUAeQb-0oIyXv-ttBBOXH1OpK7fz2SBzbzwDZOvwvbgSQ9Iv9rQzMJc3l20kiDYgIy2OXQE05tZb75iVra-HY_rhWDFOGuHVGWm0_PwNALjlHwEBRT1kH8ZuyF7dwHFq-wIuAjBI71F_CIzzn9-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOv4cZ1zIAn3KN9YPp-_G_CM56jDdPdpiYRy9jv_siFX5qE1PNztoLae_RP7iqoRBH8qy-kZpNuWZlMsGNi23E-hd9gmm89p-y_FxrMp3QaYYY500V1hmryCYu6fEODlydnKXpDIdYY57LjVU5Zv7n5jlFSVgAOiZ1dvi9W8OC4_ZkrQvqT0kfrD5VwEkGbMrrCuOnwLFNKf6EfC7m1dD36fvvWYyUWkDrLV0UUq-yrqFab5jQ0iRUr1uvZR_maxjK28JNAhhDx8RoOHOaEC0wWZdkuOWtTsvITzWInnvJaJhXCIgo43Z0mtRk8t568fxsa7cXJSQ1lUgtg_Zbz4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwa4Vvpq8Ti4HtpVYcxmUHJQMy9HJ1svUmfbwjdRPXANiIJ-KBeKz4cUvaFfrUKOaQ7OykWzE_mf3qeopmEPVNd6i3h9ghBlCOvqOBxk4Eql9mI1zPaTHuCU-KD5Zk26rkgX4XsA0g6ilSQG_X3y1zi7p1OX6Fje-i3bckfXNOMjlEbkaHGFGhV5jsXMrxSDlXiBpeITdQ3fIqm2waPoMqjBmp8vMg9IqDfs1l_81ViJNUy1k9LONrur03TFHt1BvIbN00EyjF7CRoIYoDhCCyNaFcRiBqcwJJeqxVmiUt6in8iZXZAuRE9aOEkGgT-TUUAb19Rtb42l2O2Q3WgpUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icdUn6-Z0R-w2irvAew4f6p846X7TvEVz0uzGjvS3xEpkoUEGVeCvTradKGP2wubbOL2hEXo95tTxqUIuknzCetpCm9K3pDsqlwz0cJw_oQ2n8jyrzIo2ULNwqsBpGqfbXjHzoGzbjzPZzEsOZx4jMQwUNV0PjGfL9d3RcmsR1l-UeTUBmmUo4E59YpK-AZanQ39o-gx7qWs2U1uvdVWPm-ou4dHZtDiO8RYKOtotgBD-9FEuA-57Ttx47pfEvth80kqWGXv3GXs0vQrN6kiT5TbsdQbX5s99ycVNDXSPFLjg_ZLUiwX0an4ye_xJ75AGOlQ-hmT_2ojYZU-CYTC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnde7_VrF_fjt02MkJfHmYZSPm4msfZpOdtlSY0RIuhZhfcN-MELo7aS7GY10SX1H0-ciUCSdctXl6PTANhYB-SEmoc92REdbRfz8LwSSdyRxhqO1RTu2vG6H7Ew3CvxWs1BX1cC3Ao5JoccaKRBJmuevay5O1L1divStma1kPoXKDY7QFkVndaMUJjuot9qpaLBXZW4XxFTBXLTQIpB5GOOiB7CfsoOW_2hWNdbfQWp1QwxZf7DQDezy3vkYOWb6Cm4k59daZTX0pwGZ41LgXrLSZ3uP5SozFJMcLAiIfySqzczm_AQ8SuLMks-CT1S8o8JaNbwcHvHD0S3j9zMbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/447728" target="_blank">📅 01:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447727">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdRdy7UAylsgedBtJFchDKj0w0yRButWQK711DNs4VJQ1SSqjDH-kk29lp1omIAjnV9GZr898MrrBjmntZho4Bfj1oYnYYflWFLRRo6yAZJNJWMeEcJd_RRt_Tz2OtjgxiXyBYR-EtpNA0LsLo_TkcttAv3L2y5bKoi_uWcT2Nt5MwVCzDjw2WcvqNTIJM-_DnzZzDkMG8YF2mgc6oXOjWG5VTcizEXrHrCFNPclx4GyLF_XJTCKyjHDlYbfGzGXYohRVQxQKLK1woCbtAlkWXI_j-lOR8o1adJwL3-8HFpNeUagilcc-0YuEBa_NLNMl_dPrt3PuTyyzo5mHwv7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام تشکر و قدردانی مسئول ستاد وداع، نماز و تشییع پیکر مطهر رهبر شهید در تهران از مردم ایران
🔹
سردار حسن حسن‌زاده، مسئول ستاد وداع، نماز و تشییع پیکر مطهر رهبر شهید در تهران در پیامی ضمن تشکر از خلق حماسه مردم در بدرقه آقای شهید ایران، نوشت: جلوه‌های اندوه، خشم، حماسه و خونخواهی مردم ایران در روزهای ۱۳، ۱۴ و ۱۵ تیر ماه در تاریخ جهان اسلام ماندگار شد.
🔹
قدردانی از این وفاداری و ولایت مداری ملت عزیز و بزرگ را وظیفه خود می‌دانم گرچه پاداش این حماسه‌سازی تنها نگاه و عنایات حضرت حجت بن الحسن عجل الله تعالی فرجه الشریف است که صاحب اصلی این عزا هستند.
🔹
اینجانب به نمایندگی از همه دست‌اندرکاران و تصمیم گیران برگزاری این مراسم از همکاری و مشارکت مردم در برگزاری این ابر رویداد تاریخ معاصر ایران که نقطه عطف گام دوم انقلاب و شکست توطئه‌های دشمن است تشکر کرده و از صبوری و تحمل آنها در قبال اقداماتی که صرفاً به دلیل اولویت قرار دادن سلامت و امنیت زائرین بوده، قدردانی می‌کنم.
🔹
همچنین از همه دست‌اندرکاران و عوامل اجرایی و خادمان این مراسم عظیم که ابعاد بی‌نظیر اجرایی آن در آینده به ساحت ملت عرضه خواهد شد تشکر می‌کنم.
🔹
برگزاری چهار مراسم مستقل استثنایی از جمله میزبانی از هیئت‌های سران جهان، مراسم وداع و نماز تاریخی در مصلی بزرگ تهران و تشییع بی‌بدیل پیکر مطهر آقای شهید ایران و خانواده ایشان، جز با تلاش‌های شبانه روزی همه مردم و مسئولان میسر نبود.
🔹
امید است همۀ ما مشمول توجهات و عنایات ذوات مقدسه حضرات معصومین(ع) و شفاعت امام شهيدمان قرار بگیریم.
@Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/447727" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447726">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a074d8b52.mp4?token=ndZzYg2ulpnApJ7Rd0M13LWJC2ylj5CbVIfsWzItVSaE-Ga65s-mLUzl8aSSGhSzpBTiJz_meW4eo4hDyYrDG0P2r6EgwjTlldwjDvVjQOJhPmrlPiifiR8lYdhaf9IjLGsVEkd66jcqvREi7iiOaIEaWMvmMaVtKADIqf9YCOP6bBz9_4zF8x0D9ueCRtCw0oMaULGcGx4wvzEBt_rEbzlIJBTzt2bjBDFicZHYDc1SZozYuAoOS63GFYmwTckh5uEmJtJHfdxCMbZH4O0ByKjpoIsHC8t4Yz9W4oSPTvcHpejaCGMwU2e9fOuclsQTBt2SsNM1PGqv3UP45h7Bhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a074d8b52.mp4?token=ndZzYg2ulpnApJ7Rd0M13LWJC2ylj5CbVIfsWzItVSaE-Ga65s-mLUzl8aSSGhSzpBTiJz_meW4eo4hDyYrDG0P2r6EgwjTlldwjDvVjQOJhPmrlPiifiR8lYdhaf9IjLGsVEkd66jcqvREi7iiOaIEaWMvmMaVtKADIqf9YCOP6bBz9_4zF8x0D9ueCRtCw0oMaULGcGx4wvzEBt_rEbzlIJBTzt2bjBDFicZHYDc1SZozYuAoOS63GFYmwTckh5uEmJtJHfdxCMbZH4O0ByKjpoIsHC8t4Yz9W4oSPTvcHpejaCGMwU2e9fOuclsQTBt2SsNM1PGqv3UP45h7Bhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از مسجد مقدس جمکران، ساعاتی پیش از مراسم اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب و خانوادۀ شهیدشان
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/447726" target="_blank">📅 00:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447725">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxEUe8kpWR3akSeZjMr4LWPTvZGjaNSeAO_Efpt0QF7Fa3lCiPjNKrv2nzdo2jbI7Q5owFm6hwZLtmx9RRElx6YCnDqH6_Et9xOqnDdXOift_4sd6RDWO699EDmqfDCS-UfuV2iGevPPVfwbM851K0iJxK31V8uaDTBsDqrJJZjwXO61qb04tk4PHDPZvD4djBvIVIN9j4ltUnoLvKWKi1xq96HjCbCvHbkXoFuOMhCoMH4scFCXY4YSAOsNHOhr4Fii5pxG0G9bweoZZwpY-36MeM5q15ty3kiSvF2-bFV2N6K7ipfHIQ7pChJTwVH_IxnnEarcNIbQ653QI0mrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: لفاظی‌های وزیر خارجۀ آلمان علیه ایران، فرار رو به جلو و تلاش برای وارونه نشان‌دادن واقعیت‌ها است
🔹
سخنگوی وزارت خارجه: لفاظی‌های وزیر خارجۀ آلمان راجع به تنگۀ هرمز شرم‌آور است و از حیث وارونه‌نشان دادن ماجرا و بازی با کلمات، شخصیت «مفیستوفلس» نمایشنامۀ فاوست گوته را در ذهن تداعی می‌کند.
🔹
آلمان باید به‌طور کامل به‌خاطر همدستی‌اش در تجاوز نظامی علیه ایران پاسخگو باشد و غرامت مترتب بر اقدامات غیرقانونی و مجرمانه‌اش را بپردازد.
🔹
این نوع دست پیش‌گرفتن‌ها نمی‌تواند رژیم حاکم بر برلین را از مسئولیتش به‌خاطر مشارکت در یک جنگ غیرقانونی و جنایات جنگی ارتکابی علیه ایرانیان، مبرا کند.
🔸
وزیر خارجۀ آلمان روز گذشته در ادعایی گفته بود جمهوری اسلامی ایران باید هزینۀ پاکسازی مین‌ها در تنگۀ هرمز را تقبل کند!
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/447725" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447724">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e31d74c9f.mp4?token=NPieSdHPRt4QK7AAM4ymUjt1Ffb5A8W8YMLYwkdKgGt_IMdeGGme--fDFLQbjWNW1caj3SiBi37Z6cu4omRDxLjKkVaKvhjA7dGA7wpfzO0BFQ4AvSl2Ek_eNiJCO25YT2EPSKvEkiz8hiEoF-Qtuf6aMuA9lv89_LtgB_BXikQWsPcAlgQJA0YmT5jZj9awU4ASziJfdTiUUbunI8KTzYoNqe5AFvXTQUhdBdgXIYlfoKE2nEH7G_gaf1xuXJIj59OryhmMl0EuoDX8jwXN14GSVGWu6NtGh7SsUiYf9OqS99Ptg-l-VKyFsMRerMabAqOX7p8O6i6ddEts38RUxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e31d74c9f.mp4?token=NPieSdHPRt4QK7AAM4ymUjt1Ffb5A8W8YMLYwkdKgGt_IMdeGGme--fDFLQbjWNW1caj3SiBi37Z6cu4omRDxLjKkVaKvhjA7dGA7wpfzO0BFQ4AvSl2Ek_eNiJCO25YT2EPSKvEkiz8hiEoF-Qtuf6aMuA9lv89_LtgB_BXikQWsPcAlgQJA0YmT5jZj9awU4ASziJfdTiUUbunI8KTzYoNqe5AFvXTQUhdBdgXIYlfoKE2nEH7G_gaf1xuXJIj59OryhmMl0EuoDX8jwXN14GSVGWu6NtGh7SsUiYf9OqS99Ptg-l-VKyFsMRerMabAqOX7p8O6i6ddEts38RUxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این خانه میزبان شماست
◾️
طریق‌المهدی آمادۀ میزبانی از زائران و عزاداران امام شهید است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/447724" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447723">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d88011533.mp4?token=Qkkxm8rveFwyn7HsHwsQwOij3QGK8E_ufDhdPo9mzrTmAXU4b2HlRRLmIaAh75ZpnW7aBPiK8A7lL6BPvOy5c2qsS58l648ATmYY9GD735-Os8ifA-A_B4_EsGku-wseVxnSGUbM8g82cRZtYR-AqmaOghcLTrfVx0vspV8nHH3Skh7_aMJ3ZYTnxNeuAkrakxzWY5wK45_XmCJb3QXeek3UpGK4qZtaKHLDHrik2Vg7PPK6XWkqtxT3Hg28J1pz9jxKGapdiSM4P71Psm-_kgHd3svu_N7zOSLnHUl4CK9djTmxk0atV9ZBWY_GLdjNAe_AZ_VjqyuaV2Hz437jTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d88011533.mp4?token=Qkkxm8rveFwyn7HsHwsQwOij3QGK8E_ufDhdPo9mzrTmAXU4b2HlRRLmIaAh75ZpnW7aBPiK8A7lL6BPvOy5c2qsS58l648ATmYY9GD735-Os8ifA-A_B4_EsGku-wseVxnSGUbM8g82cRZtYR-AqmaOghcLTrfVx0vspV8nHH3Skh7_aMJ3ZYTnxNeuAkrakxzWY5wK45_XmCJb3QXeek3UpGK4qZtaKHLDHrik2Vg7PPK6XWkqtxT3Hg28J1pz9jxKGapdiSM4P71Psm-_kgHd3svu_N7zOSLnHUl4CK9djTmxk0atV9ZBWY_GLdjNAe_AZ_VjqyuaV2Hz437jTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌های سرخ انتقام یالثارات الحسین(ع) در مسجد مقدس جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/447723" target="_blank">📅 00:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447722">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pednNIMIeH_oJy0Fpn4EYORAOyErhMWCR-ibGjj49ZLKzlvhmdnGXESD_i6DlF3OA3q0uHfeQHFEKQbsA9THlDflYqtBWEcXkFl23KU_nEazGPgBWcSBq2bO9NQAEH4W49osdw0RHSmGYDypV4ajtu5q9NvAE5WrB45z0kBx8Yp_7uxST0mvP2ZNRapS69dynzCigv-vYN_P-Ntt7kh2R0VeudaiEO6U57BXOGp5wzLxnyGFohDK07QFKCJ3mlDaYuKwbRmpTTOOfJ86kWIsHpFyL7xWC16pvXRshcB7mZIG-cE-Dd03bTpqEPnKX4q4FNx1kY9M8n3D83M8rcxDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکانس آخر رونالدو غم‌انگیز تمام شد
پایان رویای جام‌جهانی برای CR7
مرینو از نیمکت آمد و دقیقۀ ۹۰ گل‌ زد
⚽️
پرتغال ۰ - ۱ اسپانیا
@Sportfars</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/447722" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447721">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8180ac8e2.mp4?token=o_DMb37GPgqNogObrjhmgxWrWmaPj9Y8YK7edlNcVmkZDDAocPU6yf602bG8LHAhDBXdDmDoA4O6a6J90l3qY7TPHfYILnvMTmy2Kb0SznN6TJTX97yOrM-BvinhdkO6j5zyF95e2Z4PSPdpaA4BCEmn8O9bG4Mpejzhj-lk2_IBX8YiY9-i9ur8WE-TgTPvVsWXh7dnFgefxuIENnEqGqhq_YuVsy8zJSM6doeAzeJpJpbhswQZNR6Kedi-WU1DcuXs81-5us56EFo_xFnCFnKsccD1yqbqwSIJZJNS21Z27nDN7-sTLMcRqQbWa3pwLL_N70dDLi4wk6qd5Myh8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8180ac8e2.mp4?token=o_DMb37GPgqNogObrjhmgxWrWmaPj9Y8YK7edlNcVmkZDDAocPU6yf602bG8LHAhDBXdDmDoA4O6a6J90l3qY7TPHfYILnvMTmy2Kb0SznN6TJTX97yOrM-BvinhdkO6j5zyF95e2Z4PSPdpaA4BCEmn8O9bG4Mpejzhj-lk2_IBX8YiY9-i9ur8WE-TgTPvVsWXh7dnFgefxuIENnEqGqhq_YuVsy8zJSM6doeAzeJpJpbhswQZNR6Kedi-WU1DcuXs81-5us56EFo_xFnCFnKsccD1yqbqwSIJZJNS21Z27nDN7-sTLMcRqQbWa3pwLL_N70dDLi4wk6qd5Myh8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسجد مقدس جمکران در آستانۀ تکمیل ظرفیت
🔹
خیل عاشقان رهبر شهید انقلاب خود را برای شرکت در مراسم تشییع به مسجد جمکران رساندند و علی‌رغم اینکه هنوز ساعت‌ها تا شروع مراسم تشییع باقی مانده، صحن این مکان مقدس مملو از جمعیت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/447721" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447720">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2015a46b7e.mp4?token=G6rTIvUTekO3j1U8ZsIs-umHLkUiDZxBVdo37emXJ50UOCVOj__5yVTcqlWUhrf7wEPFMGAuYY0Pr15uMRUc4qnVtD-1sLwiVFM-tALrZMFisYMDmmMsJrN2Hs2CVF9oTIKdu4UxDbtLRY6dfXzxMOnsIYXVY9SUWcJnRJ1aVCf7m1wyvS9aXEv208oAjqE8zpTWfSqYvVxP8pzUHrPzXIsR8kfyLG-7q37MqBY1DYm4l6Unre9cgJlZ8H3fOtyw8ou8y2zGVPXaDGmjMOeN53DgJMvLFAxEcQN_t06be8bn2vxswANsOfqfz7vh6EHxzI9-YcsjXxjmyeSZD_d_pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2015a46b7e.mp4?token=G6rTIvUTekO3j1U8ZsIs-umHLkUiDZxBVdo37emXJ50UOCVOj__5yVTcqlWUhrf7wEPFMGAuYY0Pr15uMRUc4qnVtD-1sLwiVFM-tALrZMFisYMDmmMsJrN2Hs2CVF9oTIKdu4UxDbtLRY6dfXzxMOnsIYXVY9SUWcJnRJ1aVCf7m1wyvS9aXEv208oAjqE8zpTWfSqYvVxP8pzUHrPzXIsR8kfyLG-7q37MqBY1DYm4l6Unre9cgJlZ8H3fOtyw8ou8y2zGVPXaDGmjMOeN53DgJMvLFAxEcQN_t06be8bn2vxswANsOfqfz7vh6EHxzI9-YcsjXxjmyeSZD_d_pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب انتظار در جمکران
◾️
هنوز ساعت‌ها تا آغاز مراسم تشییع آقای شهید باقی مانده است؛ اما شب در مسجد جمکران رنگ دیگری دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/447720" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447719">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76860b664.mp4?token=R86EmahZdQ88lTtDFeq3M96qDmH64PHXjanm5a8S1yjRn7Ut9ixAIowXDfb5dpqrkKXEjBJ6mGZNmMYj3Xwt9jFmYIOKDVNANQRz5RC7CIeVRuPmOf_Su7flMeKQEWENIVlMx8Kco7aEn5Pj-s14C1kNQh8PVBMql3qqPBVjS5ZFROib3QXzAbcN_pC_0hNq76Ty05NGhIuxDEGhBPzUxVxOleA4tGWpsvoZcHQoNQCZU6dsi4PrzAznqbOVAJqQoVt7EyEghA4TvmYYbAmuHJ7O-m6nk9c-2UV94Iib_63xeXWTICZpLHDmhPm7z4jZpXeULjzBILQhFm3Puoec5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76860b664.mp4?token=R86EmahZdQ88lTtDFeq3M96qDmH64PHXjanm5a8S1yjRn7Ut9ixAIowXDfb5dpqrkKXEjBJ6mGZNmMYj3Xwt9jFmYIOKDVNANQRz5RC7CIeVRuPmOf_Su7flMeKQEWENIVlMx8Kco7aEn5Pj-s14C1kNQh8PVBMql3qqPBVjS5ZFROib3QXzAbcN_pC_0hNq76Ty05NGhIuxDEGhBPzUxVxOleA4tGWpsvoZcHQoNQCZU6dsi4PrzAznqbOVAJqQoVt7EyEghA4TvmYYbAmuHJ7O-m6nk9c-2UV94Iib_63xeXWTICZpLHDmhPm7z4jZpXeULjzBILQhFm3Puoec5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
حضور عاشقان امام مجاهد شهید در مسجد جمکران، ساعاتی پیش از مراسم اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان
#باید_برخاست
@rahbari_plus</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/447719" target="_blank">📅 00:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwnxHlYxq_H-gJpBKbQw7tkeGeqoijIODxI6zQs7IFcD3AEkww3VxOtV-fzOnyb2p10fc1K57iOqypkEillt9oakc-DGv5Jpb2VJ4PW0RhRibNuMiCr_CvtJKSaFpfoHBIfFm9rJUzUGAlYCdlyr7wbQqgaCMvNj7aWAxgeKIi50RJga6b78cjSgM-YvmDWcS0swfJ0Qyx36ZbBvTD98vTJ5LhEHwQxOq0VeQh8tpdmHO3hM73JymQElC1vV79PJt_HmwRFEJ-dSxDwNqSv5xo4VOHuySdabFrtDMciDY93Ymy6-XKU30oKbwN4gjJvA5hlF0pK_DLOeLdfGZn-QWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l98NzqQq1pN5XQeE7PMSICDHxbdDMS1WyaLZ7WmGjTWeErbsPjotH9orZd1wgedaNoxXVICPX-CXmHffucrDqjY5K0s_fk2yy21d8-r7PepDva4-pG3Mze976LMd8t8AyA8K_L7yUl8r0q3wqKst4jPcX4o1FO3jb_cvEAxsMZnG3emCoQ9XNcwTfTXTA6SkMcB7p8b5xGwTQegp_9utRWYVf3A2EjQcsGJSyh-ZH7fAp5vPcFetEYIEAvKd49_EgH_nvvhMhfCnw5HMV633-j_EZeqqYI1crHZG07Vf3jcqhuDa9LXG77MXAcVYl4_c9H7vj6WbY0IJmzIKI34AMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atpnZsUY6U9S6dxGaG5kICQkhPlR5jh7KsSWV9BR9GSDVvZ3kjvN0AGSUvdX_kfmXUQKoNObQ3tjnLo_aXHKwjWYh9TXFOddTP0l62NVydz-hN-QpPKUoW_CrWKI6ikd5gpdABuooq7KvwYRvb9nnBxK8d-GuutBgdoAV5aYkDhrToF3dxNF1z3lRdpNMIhIenoAeHZOFZeY_plRwytFrVbM8A-dNWbHSsaeXN0Ahv23VJogZV5y21wzU6WmbDiVucDhWt3jA8WnbnsnOmjvNK8EDPfDjqh3DAO_ShYAJ_hswGyHgFuk37CoFxYIGUleiVP6TKetG9dRxzZAbNFZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOXHHKRhlk0aVq7ryPnt2CdZGxxFpbfDa0uenJPH_fHFkNk_E-oExDiXMsqaVdKCnKuUt6hfIvHdwb8fomT8ycglya-JVQhkkeX_emWnBzisZGVAcjcTc_VaJ7XjF8ryHoVWl4DjM-lwT2tgmNTiPQYZd98EMpwDW3y86HZsCYOUgWDLgg91ZykufO1RVbs9rDhWsLaFFZ9Dzdvea8qRtdBNhSqqgxSLwHQkBZcZrbrQbWBr9RBwBkTrJyt3d_Fj6gOrLPvgRJ1PXdgG7ZQ2owMZlhrDz3kWk7Mh7Cq6xWUHERYVholI6aZDdwCWRX8J5OcfmxTQaUVlG5cVnjFgkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHa31FneFzJLd1ZJYlqn04huBBRF0EYwjwcZ3mV-BRjQQA8tMLT20htlQsttZyi2xAB1j1TQGpdHfnZ-5x4WU70mfIeYY5dF4IE7SMVJNylkaCSv2_MPo1Ehx5RkByVOKiMnSQwAeDqErN8TWC2E8Kl6nYdzLZD2j7_SCsYaZlMJ6fg1RUTmk-4mbNCqeT-Oh2qLXQmo4HdMC9z3pTta6XWr5N_bS4-1le6ElE0zg6lQya73E_OGTxryvLG9ziX1w2RkTDw9wXaJLW_4LYZqhzrKLUtcCtBCvvM5VZczFADbhN1NSgILBGy37N0R6tU9RlO3xcWcnEpWChAmd85CTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSONQvr7zYsg3s3354r6MQV6C8PZgOHjhRKBuL_N617Jxp9fK7X2JXQGCFSG8ZUQQYAuP7k2wo1a5aI68GFt6fwgI0ZFw11bQW1KWpYynjTf9aEDwnfyDI6PXPhEVYpEVBspLfNCouR5cWnbLZyWUnCFlz469ZhIUvudha3oXSb5xikV87aZYnW4qVSJAy1oPZkNpt7HEirsJODK1khdNEIt-_Q3Sl9zEJyf5_mrN6gpNFp9u2d2Fz4lHkOesUh0MfNLC6kwrIzGEWVfiGW5MamCV8-MqFCHI-3eNru_j_OKLv48A3mR4y5vat4jDmTkIBiEwhmJKAUSJWgizsVLmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqpcyO6pqlfLXEKKIGoda7c1xRF_AW0qRHCzZ0886aAtcrzuuEp3zrCNPHFajCpycopsZmget1rWSkbr7hktEPnGxI1jlQN8RJ2k1WmqQYiSUvbvfSaQx1Y_YUcl3C5LXdpFcgTdHOmo72yGdUo9_UawqChRkTzVn02I3HHHP6PC-bmVzrlF4HRetJycD8aFk_ysKF0aLsOSbDYvoQt_h4ADapXyXbWzmBCy5QM11hUdK9zMg2IdTlHV9PBw2vQUBkCWTsgjWvgxG5avMNLKrsEUE2S_sdNHqu9YS2u_uGPMHRImjoG5kyjE2epV2NoFOnHKpLZIm-bY9xsyrZJHXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHXYEf10jE09WabHfBoC4OaktEzrLqVQSIan6L1jGUzgvWtPpqevgh5jXI4yVw1-HeJOmLI2mfkRv3Mnu0oLM3vZGvYVc3Wd0vdYI-PEDNwaiX1_vwHVWIvkGDN64jveVLLoDNp0L1DMMinvU0dcLIsN-YHAK9duaV-i7lPQ7xku9nqJnqhMmbPhUA2odbFL0o1tyvPW1M4cMEn5shAZizY3hNymoaE9Xsame2UrO4H5Q6wZ_gaIcgxgwmgMdv57lzj8Bwd8k8mHUSQRtw2B9PyvRpGEAD3FZHg-Nk6G26YxM5TvxRyWRohx7x_ob-B0SOwA2w9VzMtBZuXiGz8DCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/deitNNG_zGcjb396_rkTaE9-ivMyeBI_Fh9OnFM0VQ3aNALSkmG-I9_4Rujfz8ybE8zxwdY23s5TmgkHahnz1_Co-3sCS5ji4KAsHtGV0Hn0ksQhqUAD8Sda86fp4tvf1BFjlGCa1kONb__F5Ua3cx73TpFUnMEqG7H3OnRDSNIIRVOu-65oMC6AANZodOmE5LnClmopncJgCShLPLm6m1zTntS3Xo5TdY4gl668LUB6UP0FPjFTVIopqjyiFL_u-tF1ell9oSKMH5k63Rcm_HZiv4i_Ut6TnTn_LyuWft-TrDWf2SsszSI6HRBBLWuAs4rKlsIPvDFRbQO-ZGYXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vrSpwjN2m4b01vmXLdq0nf2I24tYD7r1qbhoSjPntWjSdrM7gTRmvsQfXQbFx_Wy-3aEc26c6p4t0BSh4sC37ABergeVleKNKNIBG0aWeQOgO5wi3Hgkp2Qklq0nv8Eawb3sbX5hk2ftgxdia4PuuTYEcEFl2wyW-zMaiRN5jbBSu6pXF7ql_Qa7xTH18czTpPaBXagITPQcMljeef4ULFJxw8jLGLXErlGqTbsE6WaSiN8GQgY6MgXA7A_eRDdtOfhqUe8raOXd0T8yzb9VC6l6dwEnvZsPMQxrJc8hyElUeZqAa8_dohijXv2Rx9O8p782zZyTO9xRykFea8mUUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای اربعینی مواکب قم، در شب میزبانی از عزاداران امام شهید
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/447709" target="_blank">📅 00:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc10d9e65.mp4?token=vCrGLplFBMoHdmji_A6EEtzlf5f7UzV_RPcctdT8jUvtCO4gPaqphx8meo1XMGKb9yvi3wIo6Wh29g2rVLBoe0tGWtjqUmTjEHW-7O37W3VSvz2xdwdsODWSsp-HPpUKj8NRzwoZlFA85UeRtd4LnBELQoIFhPWdUGZz3ZmravP3nqhqEQfNvmfy61EED9_z-91Lakzpc0Ouos-ydHNj0SaJvHNocz8maT6xtegymAoy-QmwiQdJiUnVpPwFuwicKdI_jqorMUHhWJh9ZBO7jDMK4Uyo5oMm0mmFkwVtsB7r9vnNRxQ6Uw1U5LUtoy5KBuURkl8i4lkVuVSKLfnDfW69ZaCKh-XAJhkyf60Tttsg3lYdpXY1WtU6UwiRxE9Zm1JX3r-HeLauRMqp2Cbfj8E86hyeGA_I5L-ts1qAZH3yHNnFqk4a9kCVpK7tuRwllzqK-hiH3RhKw7ZIioj5pr2iy24QQ6_v0v37dG-m-DZUPqksJxy3gqS6dNovbzx9-6ABACRytW_NfOD6ZuU2TsGSw6_c_5WRHT8csNUeYN4klPor9GXdK0BDVT9aYXtXYiV4rXFmSPpppNBoMoQi7YnUUHygEvV7Ix18O_TSccllHd_lDKfcMfw3h4VXr2g8JMa7tKLnMEnzTKEs7g92ubGJhm5Gddp397_L7UbgTAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc10d9e65.mp4?token=vCrGLplFBMoHdmji_A6EEtzlf5f7UzV_RPcctdT8jUvtCO4gPaqphx8meo1XMGKb9yvi3wIo6Wh29g2rVLBoe0tGWtjqUmTjEHW-7O37W3VSvz2xdwdsODWSsp-HPpUKj8NRzwoZlFA85UeRtd4LnBELQoIFhPWdUGZz3ZmravP3nqhqEQfNvmfy61EED9_z-91Lakzpc0Ouos-ydHNj0SaJvHNocz8maT6xtegymAoy-QmwiQdJiUnVpPwFuwicKdI_jqorMUHhWJh9ZBO7jDMK4Uyo5oMm0mmFkwVtsB7r9vnNRxQ6Uw1U5LUtoy5KBuURkl8i4lkVuVSKLfnDfW69ZaCKh-XAJhkyf60Tttsg3lYdpXY1WtU6UwiRxE9Zm1JX3r-HeLauRMqp2Cbfj8E86hyeGA_I5L-ts1qAZH3yHNnFqk4a9kCVpK7tuRwllzqK-hiH3RhKw7ZIioj5pr2iy24QQ6_v0v37dG-m-DZUPqksJxy3gqS6dNovbzx9-6ABACRytW_NfOD6ZuU2TsGSw6_c_5WRHT8csNUeYN4klPor9GXdK0BDVT9aYXtXYiV4rXFmSPpppNBoMoQi7YnUUHygEvV7Ix18O_TSccllHd_lDKfcMfw3h4VXr2g8JMa7tKLnMEnzTKEs7g92ubGJhm5Gddp397_L7UbgTAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعای شهید؛ آمین شهدا
🔸
در این فیلم شهیدان آیت‌الله العظمی سیدعلی خامنه‌ای، قاسم سلیمانی، محمد باقری، سیدعبدالرحیم موسوی، حسین سلامی، محمدرضا زاهدی، محمد پاکپور، عزیز نصیرزاده، علیرضا تنگسیری و مجید خادمی حضور دارند.
@Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/447708" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EScmgDJRgKFLXPuUOD9H8Nh4822PsZI0w-Q1O8zKsOUUGAooBKn7IRjeHjjq3MV1lMZt-h9b0P56C9JPXwHwSdLSBtrgqjile2zy1zeONrBaHmUp8iZRIyuVOeQKw8_9JJK0g2Nlu_DIIkhCdC2DJn0xLznZ0cR2Mv-zzx8_D8vJJzCwOcO3ewpKgYZkuY4tu-tp5msg_QVh9lKjFLzzVNKrYoqsFiMPKUaSGYwDB7z5mFj1HEP3sQG-ZPIH8VWgf7sRqtW2b3SgYkFSosxDGEkAQEHekq_gIeNtrSAK-q4KaiPWFN0x3meNxoqvLQG-u3Je7KFufeGpYoebQy59pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| سه‌شنبه ۱۶ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/447707" target="_blank">📅 00:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hte9q_CfKaECUwgF6Sh5CaYuAvtWZXAoCjRE_nQDfb4Yp7G8PStsXC-Xo9IYxdQQWOE6FWJB__rLJg646sz1PTiyhSLDuH_pNyHRPyeC2EK-wcDQOeQpeDhodDw9xF0o1EZfowu8PsA0duxf6PqhI2sXEWVaYWHlZgwlCq_uTvJcc2RySxcNDkhTqpFEwZdwh7XKk_wH4DUkniKHdtAR96FqmJ_8f4z2KEFJ5dDg57JYliAqlD9GmAoY7xZVWmdjx2MoV1kL5NogLp0kMP4kWPICq0JyNCE3-4vHAiilCZ2cM-XEWkoUp90N_wZn8LF0MejzK3fOv0ovBMCiSRpgkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نماینده رهبر انقلاب در شورای دفاع:خون رهبر شهید علت بعثت مردم شد
🔹
امروز، آقای شهید ایران خود به میدان آمد و با خون خویش حجت را بر همگان تمام کرد و مسئولیتی سنگین‌تر از گذشته بر دوش همه ما نهاد.
🔹
جوشش خون او، علت بعثت مردمی شد که امروز یک‌صدا فریاد زدند: «هیهات مِنّا الذلّه».
🔹
رهبرا، ما تا آخرین نفس بر عهد خود ایستاده‌ایم و هم‌نوا با شما میخوانیم؛ «سِلْمٌ لِمَنْ سَالَمَكُمْ وَحَرْبٌ لِمَنْ حَارَبَكُمْ»
@Farsna</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/447706" target="_blank">📅 23:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907de65e2e.mp4?token=NNpEsqe-p5dBhh86cWQ5TakMISP_0Z43fJj-x3q5N5xhMrUmLaeNz6fmclIUe2uQfMZ67hSUFtY2ITqtnubic6Lrv3LrwFcHtrhet6WKS5dCpsP4msH0tGLJB8ZE4dW-gr9g8BWEYWs0W8xooRfnw3HIBoYz7OGYSBPCIfvs9jRqruJ_-uXLgKVOFjqKaWzBaKfKLZsLbK8G4lOJmw3eVoYIjLqgJASq-srTqV5Un5qUaj_ebSmd7OSFNbOqWT_ufn9yKquXup3TyX-ENvNjc0M-HPuXpmlaRcVTmApdBrS8OtuojijQ1gGVkS0xGCuLU0moesMWoPxJIBAoMqkc_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907de65e2e.mp4?token=NNpEsqe-p5dBhh86cWQ5TakMISP_0Z43fJj-x3q5N5xhMrUmLaeNz6fmclIUe2uQfMZ67hSUFtY2ITqtnubic6Lrv3LrwFcHtrhet6WKS5dCpsP4msH0tGLJB8ZE4dW-gr9g8BWEYWs0W8xooRfnw3HIBoYz7OGYSBPCIfvs9jRqruJ_-uXLgKVOFjqKaWzBaKfKLZsLbK8G4lOJmw3eVoYIjLqgJASq-srTqV5Un5qUaj_ebSmd7OSFNbOqWT_ufn9yKquXup3TyX-ENvNjc0M-HPuXpmlaRcVTmApdBrS8OtuojijQ1gGVkS0xGCuLU0moesMWoPxJIBAoMqkc_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیگر در امان نیستی؛ حتی در خواب‌هایت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/447705" target="_blank">📅 23:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b07596c0a.mp4?token=MyyDIJ50uQVRzDY5ZcOL8ws2EGQNdhQUgdeBfw2FNwRvFnlU3Vx38QXhh-KDfiL_3XQZyTCora2URVcJ5p1qA-8-xZQ-gqOKpkqzQcNmDr8M8VycBWa4JhjxRq8a4jVbD4toxq0E9o325E0gPpIMY0Lows8jtHcTTbVU3PFzVqzixB2hX4C5gG3yM1_UG51vSceJci1BkZWZa-umSfQZOVj06pHEfjQ2rITT7yVYZtky7REcVAn-NaXPPgJsRiAO0SfgVHiWvSycmOIDGM72LVynB8iCC0lkEYRN0zRVnEWZWxXVKa1JcWjWmDSXw1j5Iemr0txO2JJUhNz668sGkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b07596c0a.mp4?token=MyyDIJ50uQVRzDY5ZcOL8ws2EGQNdhQUgdeBfw2FNwRvFnlU3Vx38QXhh-KDfiL_3XQZyTCora2URVcJ5p1qA-8-xZQ-gqOKpkqzQcNmDr8M8VycBWa4JhjxRq8a4jVbD4toxq0E9o325E0gPpIMY0Lows8jtHcTTbVU3PFzVqzixB2hX4C5gG3yM1_UG51vSceJci1BkZWZa-umSfQZOVj06pHEfjQ2rITT7yVYZtky7REcVAn-NaXPPgJsRiAO0SfgVHiWvSycmOIDGM72LVynB8iCC0lkEYRN0zRVnEWZWxXVKa1JcWjWmDSXw1j5Iemr0txO2JJUhNz668sGkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به این میگن فراخوان
🔹
شعار جالب کودک انقلابی در مراسم تشییع رهبر شهید در تهران.
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/447704" target="_blank">📅 23:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDgzB6oD3F7xxDGsXRToVg-zlKdm5jBi8YCgSac0Jp3LQBndOwD1QQ5ysW4pLjHO2DuK4x-PQt_ILzHtiOsSazBBYnOZBSmytCu2KFb2L6gAfAF2kl5TEH7gOSCGaMibb8p86dVLaUBM9Ov3mT-67cwS4t43_kIeJ67CZpSkv3EwcScnIxMQYr4cYiIynaXKoyCP-4QDK5c4adrsZT6Gvh__T1s2hLctIf9SfARI2lGi5iH0WD0akpLbrg-C3-Oi9D1W4dbBH5p-llqBmxgHvD7lHrY0QGZwMeLKGeAn0dnF_1ZUbmAs119oviMMC75mt1a4Cjrg4j-_B-wsIlzhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکای‌نیوز: تشییع امروز خارق‌العاده بود
🔹
سردبیر بین‌الملل اسکای نیوز که برای پوشش مراسم بدرقه پیکر رهبر شهید ایران، به تهران آمده بود این مراسم را با عبارت «خارق‌العاده» توصیف کرده.
🔹
او دراین‌باره گفته: مراسم تشییع امروز نشان می‌دهد جنگ ترامپ علیه ایران بی‌فایده بوده و ترور او نتیجه معکوس داشته و حمایت عمومی را تقویت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/447703" target="_blank">📅 23:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf5179a07.mp4?token=JajdW5AX1JtAd1nFuOKi7lBit2g5X0GRgFeHvSLzRN-g89El5Snp2l2DQCbdxFPG5TW8PloyoifMRv2ajtwaelZXzBi2NQ7iI6o01cRzEezaDMvQzI21Xi3Ik1RaCOpuYO0DdFfFIFU_3XjAFRdr8s97alfruZQXmCfI36j32Rb7DGbw_4nat1vI63vydEk5DoHodNP5xp2RgxZwLFXoavmCGSSIXynz_UuT2von6D8QUWen6BgiTQV5srGxI0H-gv_Ch55QDB8JTPkUjvVBBnwjndJKNEfTQljW5SvgKZ2vBrj1csDMMbwpGm27VK6YfBacizpxsx4ROTQda_qbaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf5179a07.mp4?token=JajdW5AX1JtAd1nFuOKi7lBit2g5X0GRgFeHvSLzRN-g89El5Snp2l2DQCbdxFPG5TW8PloyoifMRv2ajtwaelZXzBi2NQ7iI6o01cRzEezaDMvQzI21Xi3Ik1RaCOpuYO0DdFfFIFU_3XjAFRdr8s97alfruZQXmCfI36j32Rb7DGbw_4nat1vI63vydEk5DoHodNP5xp2RgxZwLFXoavmCGSSIXynz_UuT2von6D8QUWen6BgiTQV5srGxI0H-gv_Ch55QDB8JTPkUjvVBBnwjndJKNEfTQljW5SvgKZ2vBrj1csDMMbwpGm27VK6YfBacizpxsx4ROTQda_qbaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال و هوای جمکران چند ساعت قبل از شروع تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/447702" target="_blank">📅 23:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447701">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be5112c1c.mp4?token=Lmeg696LZ5ejBt1CYb-jZF5VI0wtdL4cWtolIsKdv1f11tEV81cydnrgVAqfEPpavpMiI9WI_-ZTSdGAQVLyWmUq2AxxZT6IP328c0t8yT7JbXK1s-RRG-s0G7aCNw8nQvbHRRTlwuSg5i6t0y4-Hcl8EeF_ue_58rfbIIuTkhPNgOzT5n3Jtwka-eRqhZ9CfZGpY4qIXtSPFmwQGs3U-Peb3fg8FC6TqWfdMZPTN2l0xhJeU1lfAVO6ql_mHaTHgLb4szUCLa8v3XjEl9MjCt0sqi0tAZw001a6agavujZOWp1Ic-1TxOLz711zwoXXf04RlInW4CpgcnZb8Enr3F8dlpe70qA6uhA2WY3hZ2t8fXa2tjfinpKwhL_su13AQpQQ7OLVxX6EWCGh8Q_iEGLCYP0iessSZ10GiFkVDLS30xZVxkRgjCi3C32DEdek3qNsmqtUPgjH9Zs8qaVirXO7jxz3WSnxag8oZU5zkv8HIPUlESxjmQSnDmja_XQ_q6bRhqFnsEkS9i4wVsU93ebiRXOs-K2256lFUosOFg44GNM8z65_9BYDgAWZE8dnVPVeHSP1EStL4aezn54dBgiSLoTV8CabBCdWO8yV1FAlEOCkOSVxVnQ-BrOLMAJDVLCOpMgZBLIVUod_VD0nlP3Rw0nFNllLvGh3ieZel3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be5112c1c.mp4?token=Lmeg696LZ5ejBt1CYb-jZF5VI0wtdL4cWtolIsKdv1f11tEV81cydnrgVAqfEPpavpMiI9WI_-ZTSdGAQVLyWmUq2AxxZT6IP328c0t8yT7JbXK1s-RRG-s0G7aCNw8nQvbHRRTlwuSg5i6t0y4-Hcl8EeF_ue_58rfbIIuTkhPNgOzT5n3Jtwka-eRqhZ9CfZGpY4qIXtSPFmwQGs3U-Peb3fg8FC6TqWfdMZPTN2l0xhJeU1lfAVO6ql_mHaTHgLb4szUCLa8v3XjEl9MjCt0sqi0tAZw001a6agavujZOWp1Ic-1TxOLz711zwoXXf04RlInW4CpgcnZb8Enr3F8dlpe70qA6uhA2WY3hZ2t8fXa2tjfinpKwhL_su13AQpQQ7OLVxX6EWCGh8Q_iEGLCYP0iessSZ10GiFkVDLS30xZVxkRgjCi3C32DEdek3qNsmqtUPgjH9Zs8qaVirXO7jxz3WSnxag8oZU5zkv8HIPUlESxjmQSnDmja_XQ_q6bRhqFnsEkS9i4wVsU93ebiRXOs-K2256lFUosOFg44GNM8z65_9BYDgAWZE8dnVPVeHSP1EStL4aezn54dBgiSLoTV8CabBCdWO8yV1FAlEOCkOSVxVnQ-BrOLMAJDVLCOpMgZBLIVUod_VD0nlP3Rw0nFNllLvGh3ieZel3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی گرگانی‌ها در شب ۱۲۸  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/447701" target="_blank">📅 23:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447700">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0073f2bda.mp4?token=niTUoOLR90U6NeagL0K0ag0DH49QrHo1EQIupcFuebjsm4NRyZ6LsxS1sf6iCRCAvbxtYFawLVrq7yipXm9Kq3gWhqPlis1R1VpLi63mMTiQJwjHtefrCoE7Ue8I_nf261hml_BET6TeujbJkoYEc5bDH5WGLFuROCxr14D21cKFZHq82xBA_waSzUwo_qMBeE5GI15KZleW32cRQys29e0rz4EZpm1eQ89uLmCVWkBwyZUXMwfG9VUFptJwuMA_9-qdlQ3u3ChfITfBSzzL3X1x5gEkCqHwUVP9M0KshBWONcSvzKCmsKr-Ll__pdwHHsW14iHWZ_hE19Ci0O2qPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0073f2bda.mp4?token=niTUoOLR90U6NeagL0K0ag0DH49QrHo1EQIupcFuebjsm4NRyZ6LsxS1sf6iCRCAvbxtYFawLVrq7yipXm9Kq3gWhqPlis1R1VpLi63mMTiQJwjHtefrCoE7Ue8I_nf261hml_BET6TeujbJkoYEc5bDH5WGLFuROCxr14D21cKFZHq82xBA_waSzUwo_qMBeE5GI15KZleW32cRQys29e0rz4EZpm1eQ89uLmCVWkBwyZUXMwfG9VUFptJwuMA_9-qdlQ3u3ChfITfBSzzL3X1x5gEkCqHwUVP9M0KshBWONcSvzKCmsKr-Ll__pdwHHsW14iHWZ_hE19Ci0O2qPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاشقان امام شهید در جمکران منتظر آخرین دیدار
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/447700" target="_blank">📅 23:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447699">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd89a66e7.mp4?token=g0G60xMtDfrp4tpHJU7vfaS-UMzL_uG8vWD5wOxUOMhMKDpE4wZsKuTkrLeF7XyYGmFR3iE6Mtn9L_eJRFJY_MgjjEzpCmMNfNNkNsmf6UpTBq7AEPzKT6CdcdiNWzNcPK34qEmEP6cHi313wt9USzrKUKWhi74w63kf5vZNkEIHY_Oq4pILxL64Z87NJyO4NcoADrrW9Zk8gKZCWthEtLPGbiLuGBSmw1yoXpAnCV_dtq8jPGLbqHMNSG58LAHtsHIYrdVUY1IOGazhRKace8HDeqYWSKnR2hdPIa2AlQrdubcxrcKkqtAE5aub3WBHPENHNYb-JHfMhZK0orkmOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd89a66e7.mp4?token=g0G60xMtDfrp4tpHJU7vfaS-UMzL_uG8vWD5wOxUOMhMKDpE4wZsKuTkrLeF7XyYGmFR3iE6Mtn9L_eJRFJY_MgjjEzpCmMNfNNkNsmf6UpTBq7AEPzKT6CdcdiNWzNcPK34qEmEP6cHi313wt9USzrKUKWhi74w63kf5vZNkEIHY_Oq4pILxL64Z87NJyO4NcoADrrW9Zk8gKZCWthEtLPGbiLuGBSmw1yoXpAnCV_dtq8jPGLbqHMNSG58LAHtsHIYrdVUY1IOGazhRKace8HDeqYWSKnR2hdPIa2AlQrdubcxrcKkqtAE5aub3WBHPENHNYb-JHfMhZK0orkmOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی گرگانی‌ها در شب ۱۲۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/447699" target="_blank">📅 22:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447697">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa2cdpJbCE20sVeQec7PRqnICK0kEF1Jwz0JfndU8Zsc265-Y9jQPamtnZrLPb3dQOpzphECi6VY0m91z20YnW-tJWcwC7DQngzONcosF8U0tVm24wXjXItEw438y_INO9LhygMPM4mrr9Rcd2xKlL3aglNThkvmnJePOh6CVe0OCbD7Vs7bR0Xcn8carXD5iQmwSlTxfNxOnnaBzU7ZgFr8d2xm1EN8gLP4eHuE87LSG6csQAWLdivVOBc1B3j371SqQPUMOxj4R-Gv-m4ZCGv8DhELt2UGhIRQB1iRS1ka2UjU6KLB-W6HUhszfcVD25aDHmIFN_ygCCV2rhxntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی در پاسخ به ترامپ: با مردم ایران با احترام صحبت کن، وگرنه با زبان دیگری پاسخ می‌دهیم
🔹
ذوالقدر: به رئیس‌جمهور متوهم امریکا که امروز ۹۱ میلیون ایرانی را تهدید کرده است می‌گویم:
🔹
پیش از این تو به‌عنوان رئیس یک کشور بی‌ریشه با تاریخ ۲۵۰ ساله با ادبیات مشابه از محو تمدن چند هزار ساله ایران سخن گفته بودی و نتیجه برایتان جز شکست و استیصال و درخواست مذاکره و آتش‌بس نبود! ایرانی با زبان تهدید بیگانه است.
🔹
پس با مردم ایران با احترام صحبت کن، وگرنه با زبان دیگری به شما پاسخ خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447697" target="_blank">📅 22:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd48407210.mp4?token=JVNkxWBweSG_NLbqG-OQUzU8EiETIpPvt5gsidY9qSHC39XQX5FUNn_bhNE-9dEIASGRHCYmxYTtb4eYCzxmJMy9FT-84Y5Df4BSYbmRjsYC8pvaxplZB6cVDqFL0ihRwDWw51RBgd0_mq1rEhy6T39VbIq9csNq9kyBUVpjblMvRuZ4I3F8zrR3pgYAE43bzCV_st8dCo9I3v4lWC-HxHm8Bj1_rwtdhj5qp_IS4suKsRuDpytcIHejvPdbWXCfrUHJrqqx2sXq-YuzIKE43lIi4kyhey-Oax-ua4rLGHZMROwv9sVKUsm_D_eZ5R2iy2a9FJo4a5JEnB9RFrEXGX7HRmufIUk95UBcsPWyHv0rpYxSLgOLXk05LnmGYdGka_PugtoGVmJE5u1USv74G9UeE-PSv-9IbDMrUl3YzNpOfId_pg0m7QNErUGbXDcMbRypwM8uQ3JYJrRd9TWM38ck1nTCuAQVBszttQEzqm7XmoFLy3tDRzZuj2jo9hlOesz2J6ir-gcNkrsXCmoRKkTbfTBYQm56-yqFN_Re3gzxJP3sx4dpIdE_oumInxPPRmDssuCdwsYPWwtTJhM9wIwMozT6ttjDjKGHFZNEQUnWaV6KQK_boovaLdrR1wgSIstnKUrx1n2_1ncG0vM364A3ikcSaOLVNiiHj3rXd2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd48407210.mp4?token=JVNkxWBweSG_NLbqG-OQUzU8EiETIpPvt5gsidY9qSHC39XQX5FUNn_bhNE-9dEIASGRHCYmxYTtb4eYCzxmJMy9FT-84Y5Df4BSYbmRjsYC8pvaxplZB6cVDqFL0ihRwDWw51RBgd0_mq1rEhy6T39VbIq9csNq9kyBUVpjblMvRuZ4I3F8zrR3pgYAE43bzCV_st8dCo9I3v4lWC-HxHm8Bj1_rwtdhj5qp_IS4suKsRuDpytcIHejvPdbWXCfrUHJrqqx2sXq-YuzIKE43lIi4kyhey-Oax-ua4rLGHZMROwv9sVKUsm_D_eZ5R2iy2a9FJo4a5JEnB9RFrEXGX7HRmufIUk95UBcsPWyHv0rpYxSLgOLXk05LnmGYdGka_PugtoGVmJE5u1USv74G9UeE-PSv-9IbDMrUl3YzNpOfId_pg0m7QNErUGbXDcMbRypwM8uQ3JYJrRd9TWM38ck1nTCuAQVBszttQEzqm7XmoFLy3tDRzZuj2jo9hlOesz2J6ir-gcNkrsXCmoRKkTbfTBYQm56-yqFN_Re3gzxJP3sx4dpIdE_oumInxPPRmDssuCdwsYPWwtTJhM9wIwMozT6ttjDjKGHFZNEQUnWaV6KQK_boovaLdrR1wgSIstnKUrx1n2_1ncG0vM364A3ikcSaOLVNiiHj3rXd2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حمل پیکرهای مطهر شهدا در مسیر آزادراه تهران - قم
@TehranFarsnews</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/447696" target="_blank">📅 22:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">لرستان هم فردا تعطیل شد
🔹
استانداری لرستان: تمامی ادارات باهدف تسهیل در تردد زائران آیین وداع با قائد شهید امت فردا تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/447694" target="_blank">📅 22:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447693">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUhqflrPWks6sOnpJ8kqiW_4p7ToAPN1TX7ab7YscLSEHYvG6XUHypZfngjOC9vgBjvq13ok-Iw9vvbQCeMt7ockPxeD9YAUsEgKRSY5c0Xm5YeGD_lQ0yPtYOqHlDzqcMzMHZtUmPlrIxgdHybtcVJCPX99xMlUFZV_4Wr7rhIjcG9biKekV4bi0w5JcAicIn60nwHV-c3mXXFU3gNy0M8v3R3U8N83Mdyl3EGYYpMnaw-cHDkBhWugopoL36LAyjJqVZRhony5cCgx_6MnsbVX6wBZAEfHkHVn-C0AuvgeYIblrD88DbV6grK43a0SsizqwSIFWmFH4YnOzWzeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محسن رضایی: ‏ملت بزرگ ایران، پس از ۵ دهه، امروز نیز با همان صلابت و ایمان روزهای آغازین انقلاب، شعارهای کوبنده‌ی خود را علیه آمریکای جنایتکار و اسرائیل غاصب سر می‌دهند.
🔹
این شعارها که با خونخواهی رهبر شهید توأم شده، به خشمی مقدس و اتحادی پولادین علیه دشمنان این مرز و بوم تبدیل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/447693" target="_blank">📅 22:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سخنگوی ستاد تشییع رهبر شهید: نماز بر پیکر قائد شهید در جمکران، بعد از نماز صبح و به امامت آیت‌الله جوادی‌آملی اقامه خواهد شد
🔹
بعد اقامه نماز، پیکر رهبر شهید انقلاب در بلوار پیامبر اعظم به سمت حرم حضرت معصومه(س) تشییع می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/447692" target="_blank">📅 22:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
تهران، آخرین سلام را گفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/447691" target="_blank">📅 22:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a509ce5c59.mp4?token=qBoo-YpS8gASO9_CWGzmUAzszXHi8wD24Oo2GflQK6bpICYVV0RNH3HB0BovFMSxhC0d-iQNqYOod1oGeSaP5XSYAHYS-YEMncDcq3OPjtxL4orEyN24kO--fZqmT-g4w9MKf3vaS5MyGCapBLvyqYvYpgbKr-Vj-PRHjM2gjM-TkfsFOOMVlIv9uVE7mA7BMEgzh3MV9B5eEqTW7-H3-w6AHbPRA4HUzSQtel7sufefIKAwwz7QUppFw1ZgQPTgxOwPCulgrJczPPoMD3dI38fyU5-Y0tGFiK7SJvnkgTNLXkJ0HIIOPKKBFitbM9oWW_oVqEl4KkGlQPeYtYnZKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a509ce5c59.mp4?token=qBoo-YpS8gASO9_CWGzmUAzszXHi8wD24Oo2GflQK6bpICYVV0RNH3HB0BovFMSxhC0d-iQNqYOod1oGeSaP5XSYAHYS-YEMncDcq3OPjtxL4orEyN24kO--fZqmT-g4w9MKf3vaS5MyGCapBLvyqYvYpgbKr-Vj-PRHjM2gjM-TkfsFOOMVlIv9uVE7mA7BMEgzh3MV9B5eEqTW7-H3-w6AHbPRA4HUzSQtel7sufefIKAwwz7QUppFw1ZgQPTgxOwPCulgrJczPPoMD3dI38fyU5-Y0tGFiK7SJvnkgTNLXkJ0HIIOPKKBFitbM9oWW_oVqEl4KkGlQPeYtYnZKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایانی بر انتظار ۱۶ سالۀ مردم قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447690" target="_blank">📅 22:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN8k-VOg-TTeVzJXMpxjn5qtuqna23w--CdoyLdDn3LGReCFWr4NwkGGvljNy6fn5jtgM4ns1NrMwSDe7v2lN3IeuvKXMIN8iNFIzBuLH1dTJfWx8PxeTFySL8SsfGVuHquJ33FKicA2ochi2AkSaiRQb1lTjFr5N6x_3619nfPCHZgDhPfGkjLRYS-kPq9KOuvXPaHXn7oGj8pfzLk6TBvS1YWtArf1dG1INW1ORjPlhAst5eekkqQ4mWidjmoENK0ig_OY9AFJFSXBONTOQXMhQjCLEmEawoG-DQWplxsxDJAmiyAEHSMTTIBp9kj6xJ347pYVYtIxRgnia0X6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای حضورنداشتن سیدحسن خمینی در نماز رهبر شهید
🔹
انصاری، سرپرست آستان امام خمینی: سیدحسن خمینی بدون تشریفات متعارف در مصلی برای وداع با رهبر شهید حاضر شده بود.
🔹
اما دربارۀ نماز بر پیکر رهبر شهید، ایشان به سمت مصلی حرکت کرده بودند اما به دلیل توقف خودروها در مسیر، امکان حضور در صف ویژه نماز فراهم نشد.
🔹
او همچنین امروز به همراه خانواده در مراسم تشییع حضور داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/447689" target="_blank">📅 22:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phBmj4cm48LYGsW7heJNgPL6jh11MY3PiD8IkL3-NoJA8WPVmDPMUD_wypIKwHbACgsBUe6L6LUYoGreebWTgh9jouL0Ei8hLF7WJ88gvCh__9LdsNNXFCl27HErhdjwEP6rc0atGbtLzfodGW8eoerWsNDIS1yOq2UuMZRPy2Hb77ahQ3IGkzAOqsuFQB303hzGoJqtme5-4yxgGJ_gsNX4h9HTBWXalHe4LqoVAnMbXA0gckd5bt2k17-D4tt_Tu7uJb2cppBzThyAgTd9qXhv5G-zLdws_JVM2GrU26lz9p2qVsFdywVUz1xQh62m1uLVa5EZB08KsombzUDTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: قاتلان قائد شهید امت به سزای عمل‌شان خواهند رسید
🔹
رئیس مجلس در پیامی به‌مناسبت تشییع تاریخی رهبر شهید انقلاب نوشت:
بسم‌الله‌الرحمن‌الرحیم
ملت شریف و قدرشناس ایران!
🔹
داغ جانکاه فقدان رهبر شهیدمان و آخرین روز حضور جسم مبارک و مجروح او در پایتخت ام‌القرای جهان اسلام با تجلی وجه دیگری از بعثت شما در این مقطع حساس و سرنوشت‌ساز به حماسه و شعور تبدیل  شد و حرکت به‌سمت پیروزی قطعی ایران اسلامی و جهان اسلام را شتابی دوچندان بخشید.
🔹
مردمی که ۴۷ سال پیشران و پشتیبان انقلاب شان بوده‌اند، در ۴ ماه گذشته هرشب با ندای مرگ بر امریکا و مرگ بر اسرائیل نفرت و انزجار خود را از قاتلان امام شهیدمان فریاد زدند و «انتقام» را خواستار شدند.
🔹
تحقق وعده الهی قطعی است و متجاوزان به خاک ایران اسلامی و قاتلان شهدای این سرزمین به ویژه قائد امت، به سزای اعمال شان خواهند رسید و گام نهایی انتقام از مستکبران با آزادی قدس شریف عینیت می‌یابد.
🔹
ملت مبعوث شده، رهبرشان را بدرقه کردند و همچون ۴ ماه گذشته دست بیعت به سمت ولی فقیه حکیم مان حضرت آیت الله سید مجتبی حسینی خامنه‌ای دراز کردند.
🔹
باید قدردان این مردم بود که در مسیر نورانی امام و شهدا ذره‌ای عقب‌نشینی نکردند.
🔹
دنیا امروز فهمید انقلاب اسلامی و جمهوری اسلامی ایران، پاینده و جاودان است و با پشتوانه‌ی این مردم، بن‌بست و شکستی وجود ندارد.
🔹
این ملت، از مکتب حسین علیه‌السلام و تربیت‌یافتۀ امامین انقلاب اند که در ۳۷ سال دوران زعامت رهبر شهید انقلاب، نه تنها روحیه جهاد و مبارزه را حفظ کرده اند؛ بلکه ساختارمند و محکم در برابر زورگویان دنیا ایستاده‌اند.
🔹
قدر شما را باید دانست و از هیچ تلاشی برای احقاق حقوق تان کوتاهی نکرد. چه در پای لانچر و دفاع از کشور، چه در عرصه دیپلماسی و مذاکره به عنوان بخشی از مبارزه‌ی تمدنی و اصولی با سلطه‌گران و چه در عرصه خدمت به شما برای گشایش امور معیشتی و اقتصادی.
🔹
امید است توجه به توصیه های اکید رهبر شهید و رهبر معظم انقلاب در کار بی‌وقفه و موثر برای مردم، با همت مسئولین محقق شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447688" target="_blank">📅 21:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تمامی ادارات یزد برای تسهیل حضور مردم در مراسم تشییع پیکر رهبر شهید تعطیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447687" target="_blank">📅 21:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ادارات بوشهر فردا تعطیل شد
🔹
استاندار بوشهر: به منظور تسهیل در تردد و بازگشت زائرین رهبر شهید، ادارات استان بوشهر به‌جز دستگاه‌های خدمات‌رسان و امدادی و بانک‌ها روز سه‌شنبه ۱۶ تیرماه تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/447686" target="_blank">📅 21:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447676">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmF04z4AA__fdCuLzj-0Y1GE75Bp6GCABMf4cSMOTbKsddznhh8OpV3HYSt4TV6tbV_Htb2LdW6P9r0fSZ0LDnvEXCRWLFvAHXgFJQx1HLvSiHwDd5XyGb8jyYJ-8m0fYVhhG9Gaea25qNfCDRGD2NJKbzNbZ3OSydUW2bgfrecFUneETKERalmvonekgoUOtRIQbeO23ssdj70skNvqVsUkm3AcgJ54tKSXs10eMt1pL8mkgwMMxViUvUU5-dYw2NFizdMM4o6sm0Gcbuh1kiNL8dEHFq4aSosW5kk43vRA-E5jRXocU7nLogzg_SM9TP4oAQerfIDJZyFVyrKkZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXo70wkP9Xopxig8JXkl-_H2PGZqqXnrH18wfqEIBXSb3aE9srwxAMI9udZOkU93-TKZb-u0h_nyR_K7kX6oE4hf0wbvfITvf1fkafKUthI921qnDUEFzb4zzGbTV-0IWoudHaLlQqTyOp_Bgmhw4ulfyQI20I_ms9hjjAaPEobisILDXluNJGZ72jSKcOzgu8POdvuuQFDUzjOc5m7ceiwyROHVR0WF9X9eWDzYlvlF8856GCx1mKE6Bed9L4JlgG4YkWH41_bW-tgYD4jbHzvtgTKlSjA7OtEAK_PMJmL8OiARmxjiYyR19Jgrei_ijwbISSQrGPJ5k8ww8GgkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJVftn60MazDwRVjDb3IgNvHVgObeoYbTE71amZihbE77931VCM8kTTEHHCoA3hSP1N8-7nyd0kszXKatEOJc1-BdBdH4crBGldY7AL5xoJAj63mGSdIO_HgbfCvvtiIv2QqIuv5wcJ6IfXWoYaGCh1LfPG3h7s9vKzIw86L0xap1MZ-kkPtdPxJ66J1wFRrNUEUWkW0OK-K7L8nKSmcq-34tAKJBQhkpDYYYIRG7OC04WsgHSX3pkp2TQacMegSsFjEpHaVqd9uliLLaBx4LRVs1SqIkn3f4El045DiQl9rpvpn91f3QppLoB2-vXlxezKpiFNp7FNAy_FA_BjLjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hS_ga9BjnPPjoXDiRrVLNzsVDAjMqhGtcaKS4mNdPwcvIwVVW98wFYE6i1hrGZGYASK8NDVqttXEC6ILrseqge7NlWm84b5n8K4WE4OA3Yt0ul889hicLrNz8WxPthdZhoFS6cbAdNj3SRS3ycxI_1gCfumoGTjpb65PBYl9G_KA1E2zD7pwvsOBjz_jPxXVfPk7SgXckCNq5VpAY6FzzcQrfMLR4Pa1MgBNls7R7cj6j25NoNIwWVJQCP8IgICkVuiIzr0B029YJXZOd7-TzGaOIyKXGnUJuT7lo140rwE759Xvz1OSyottwRZmK6a6NoiZQMurAP3XwJ3jnXgU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDR6hhsZMMAZEIU_8xqLnlWpf7QwaN3geWI0FZtAdq12uaX5aoBR38byyyUqBM06WLQ4Rcn8yOwUDmQf3kfWDTE9vXS69eP_m8f4HHGKNyjt3e941z48186TbHhqvexL1WixpX6QoiYIpSoeGmg4OL_G71cDFTzk7cjqcRztRLWiWU0LL4Vb1ju8s2DyMzSS4u5aLHq3wZL8o0fy0msElC5pz52ppC7jWLs1ApqDGBcs37NuQHT9DEMHB31VgKKEdDg16cMttefyWdD3l3SAI98Q9k0nnH-ioX1W-RQvZDlUEcfZ1gMOz0dvp1VUgOcABx0ABgTijJaFHQexni4vIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbyN9Q7JiZ0CgUpHgSL3MizJSG6YRJztBYriWgACuMVLlbVhALQdsfjhj96zIIPgJCN5Whawcvqp_UhoG6OBSIuCaQGxm71TBvINP30yLF3x4VRo75wjf4PaiVvFUIJJjyVZAupNbirotsOd-9wqEhp00ejZ-lJSRfe6FQibXlAuNPMfGKYmWCQ2Sc-mFvllv7sjpczeZcF4zG2Kz8VfUJDShE4N9l9N5dhkwyN6Vdvx1Jlw6HVdNkfQBsAieChp-PY_glWiBR-Qp3i93xIEhYmx3oQA42S5y0PQ9L74kXNhJDN8822v9ZHgdYEjG823Jd5Lvx3J57IceyvWwfQQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unT1TV_ilEIYGaYIA1-RhBVgRQceGA9yOsdtLQIKLUS7EQkVE5KkbFZXD5OSMeuSOSaojcb4fiijm7yoJwX76iITQU-2NdH-1W9pGCKReLVQF5sFpLdBrMTb7DPR04Gc_jl_vkDU9HUUj5Za7U4AYvUHwJ9Dg-lbsjWXYwLI9-M3RAqUcOoqsO--zKc0iPK8GmnMyn49Aw8t-xZv6mESt-IqlaaFYfelLRs3xWTda_16wdLtLNDUPRLQF6fDNzBidIXB1gQvI2RODF0l0Sz3pBBs-Rl-Ji785BH_qcY33a_zzjPivzzVCbffvc_ApRzmmidSjjh-2EuswIOPDQBBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOkxUFk_MrjEvpulassqKRK_IN5fhwQJcsKrOI4YSYL--YrkdnCv_p05ejpTs_4BkzwuVWwROFhfJXyCq8EN26QuB6btfr-TrzvTOWew_12ibcbqAjFejsQgbUn8TJXxEbhaE_CIhjsCB4E15Za1HAjk60pY0C8UtGBYMI219mH3VPa0wEDnbU3OXqZo8IcAxT31Ts-2TfCJOrwScZn8N4MeAUqTT7Zz4nsXFFwY_Tl-3KoXVWQY8jVT9_BT0jOssZccODmqpiXKB0iirv02emJoPFMs6pqNYq37ZyV8rLkcSNDp5uWxZGpgDtY6pYQdX-lmrYiMfw4DajCig9fMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0MM-F9mA3sUyhZSnm2_o-IIOQSfdtHhSq_txz73K5budy1Uqf0Qo4mNJcF_HBMZT0NYhZ6W5RCWJfZ7MDyi99nQoLJVNSemDtrP6X_8J1GOCRvmW7wBIsH1T_1YgPacMasLf_sBAB1hD6Kdc1hC1qrdEuh5oolsZg61QjxwCTWw_kVpPLLUfpxLrh0FsVwOJgHk3M1yyoTWlxXLGJPzazwIFMsdMil-F0h6KTAh_vJIeVDBQCYSz2SKsnIv4nZh_9koHMM3qJc9bWlMgSuVIWWxlIro3hwCCpiehkP16WCDIZvd98IgaQF-MQyZ-0nsrKz72RKQuY-U67RWI8lC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6z3wOmt1bn10BPPvYApjZ1idQ-NliVcl3S6swCSMmURwKNinl6aWdu0Q_d2gLi5y435OsHV9jJkD7wk3A8BJrkjrDzme2xxve2ZCKT_QY3qiJfRSUFdZefMN928FA-m28Ldr_tPfnnk5OU1Y8KsQgzplBUChDRL5F7maSzY2-hwMbjdfVjmHdWdvmC0_Ik6j9WyxjBkkSG3A0TQuIiBzwpebJi-SDzfH6VWchAfvDFNhKKB3yhN7uYCR-BtOTwKcFXOlq6UwT8oA6lMflxPCB8oq3c0Z1dU8_GpddKgt1fP4DNycvalj_aidSrt6mBFkliflAudYBcPiOzDU9vcqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
حضور مدیر عامل محترم بانک شهر در موکب خدمت رسانی بانک در مسیر تشییع پیکر رهبر شهید انقلاب اسلامی</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447676" target="_blank">📅 21:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447675">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/447675" target="_blank">📅 21:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447674">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKbHp58W-qdzS3r9Fvkgr40RuRtOM_C0r598bjqiXQvJBwSyql1Zr-z2lb3P0k8zIe71AnUUafuWSzf79wdLfTF97zjExkHF8wscbhFEWN70D1RgNavQYvVwof2FD6uJsLhnHCS5C9rqLrpUwJ9o06Vl7uNtAgCewYsjA_KiK24wzbZOKqZaxF5bpj4dJ01QBhdJRV_utgNLBmp825086UQeDaV9PYotI6k5Ie5PqSeWMyY30H3-eKi5ntljWYcCGjEFZIOVPmJqLEs0LVXdbaP3MmQUPzm6VtNIxhS5iVGmrZJhdOVhnIb5Wg_2LIwUQN3SQNHoSs98mx4ZJ_LXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس فیفا: ترامپ دربارۀ کارت قرمز بازیکن آمریکا با من تماس گرفته بود
🔸
فیفا روز گذشته اعلام کرد محرومیت ناشی از کارت قرمز فلورین بالوگان، ستارۀ تیم ملی فوتبال آمریکا را بخشیده تا این بازیکن مشکلی برای دیدار یانکی‌ها مقابل بلژیک نداشته باشد.
🔸
بخشیده‌شدن این کارت قرمز با شکایت فدراسیون فوتبال بلژیک و اعتراض افرادی چون توخل، سرمربی انگلیس و یورگن کلوپ مواجه شد.
🔹
ترامپ امروز تصحیح کرد که دربارۀ این موضوع با فیفا تماس گرفته زیرا بالوگان را ستارۀ مهمی برای تیمش می‌دانسته است.
🔹
در ادامه اینفانتینو هم تایید کرد که ترامپ دربارۀ این موضوع با او تماس گرفته اما مدعی شد این تصمیم را مطابق با آئین‌نامۀ فیفا اتخاذ کرده.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447674" target="_blank">📅 21:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447673">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv5thzjrrqW4Cdy55TLrmy92seALbROJi-1FdapXzFTDKgENRBq5nFY8FW21uxZXv1jkDQt-FMvZ0CrvaeLY_MW1kwNP8HDgKZr-T34A7Y0t6e-gBiPgHHbocowzJWKZufiR7VwF7LG_AkE_4Ni2GTZPelY3DmEGxT6NIVodc091n9jL_UFxMJKWjycrOe9kYrykzEp_3ynS9VvbONTX4umklqmRxNaaXHmSi35P4Ipiy-gTEFwHChVsla9H6ZrHiiG5mK3Kqe9OKut4FLzK_VIAlFGRFUtch0xriMSmchkzkrylPzKS3ksp1VwfGFOm1TWYrzcqOE_zqI9FOWpkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بدان امید به تشییع آمدیم که صبح روز ظهور برگردید
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447673" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447672">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_Gcaj6fsie9wTVrZG3fZRWjZjwL2BDKN8D0ITJQ7zrazvfczhOexKCuHhKPioou0jKTbLhu9lGQvJdv62_gYorUAu5vzYMl3R78uipSEG-pNAqnUw87uqNvdfR2MQyNJdMw4wtWA3hq06lpBxZP9oXVm78ijJHQb7HkcyyzNxWy8bvu3ugo1ObE8ozfxz64CMoVfhmipWFiLyqUdJ2Vw8hFqHIeepuzsPM5SkWisL3yJqObcfa_sdZ-Dw5oLwrfm9tHk4F-jZn_WVggcJqmDJDatpLq-G9UhmhfDJh2pTudsaeCq3Df_1sjMuaogHsEOI7fks2dSxNjeIGSKuc6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رسانه‌های جهان مات عشق و علاقۀ ایرانی‌ها به رهبر شهید خود
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447672" target="_blank">📅 21:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447671">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a9851feaf.mp4?token=pmP6abOl9d1_qSwXk-Lw2zc-bm0ggLmc6yEeXtFmrVtmzZsGzPQT9SaL7SomFQZZW2Gf7FYBpRA40AkjAklGJ1iV8iehPbJzs6IygiVcPWbICHx7elfpPYg5JxLPzbEWoPEWZ5NLOhaFzNVe0hd1Bi7DKaxWoe3FIF35fwBs9VR6cddaUGUFe-ZeMXdz48TsPFqgWLWp1meZ-OLrdFeeh-y3FKtM2n1brL-A-tbS9KtNwWHo1XCMkZ0_e_EGBys7y7570cGm-llbxDJ2BbbIzJmo9KE4ABO8O91uVsWQ7U1wAn9CNTxCRlSGsjnT3zOq--26SIRrE-jjMCCLvUJ7UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a9851feaf.mp4?token=pmP6abOl9d1_qSwXk-Lw2zc-bm0ggLmc6yEeXtFmrVtmzZsGzPQT9SaL7SomFQZZW2Gf7FYBpRA40AkjAklGJ1iV8iehPbJzs6IygiVcPWbICHx7elfpPYg5JxLPzbEWoPEWZ5NLOhaFzNVe0hd1Bi7DKaxWoe3FIF35fwBs9VR6cddaUGUFe-ZeMXdz48TsPFqgWLWp1meZ-OLrdFeeh-y3FKtM2n1brL-A-tbS9KtNwWHo1XCMkZ0_e_EGBys7y7570cGm-llbxDJ2BbbIzJmo9KE4ABO8O91uVsWQ7U1wAn9CNTxCRlSGsjnT3zOq--26SIRrE-jjMCCLvUJ7UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم آمادهٔ آخرین وداع با آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447671" target="_blank">📅 21:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447670">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c6a70224.mp4?token=SRdsv0xB1Xxh1uyn5quflZVLUo4ullJ3sVNUZGfteghwXUqJqvkToNYkmLaDOg-iqKimJXwtaONwacw29I-qORHMfAs_eGQPtCusj9JCG_bkxOGQa3QXH7U4m1o3dlNYPQBTklsu-pMDuI1Lh-v43dOFZwh7R3DFvgFaIVCe2xJSC-_yhEojMxWk8MG6_QovGimdczmeO4fE9FxMdZkIFjaBntIkPn2JgrP0bF3372-RKZL0ah93szbs7iGsuWpw6JH2pwzCuOcI81j_N14KravIVb7sgnfta7hY_cvni5JwpRxGx1k8iHXhCkyHnxNsdBvcEb5wakt4c_3rzNqdRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c6a70224.mp4?token=SRdsv0xB1Xxh1uyn5quflZVLUo4ullJ3sVNUZGfteghwXUqJqvkToNYkmLaDOg-iqKimJXwtaONwacw29I-qORHMfAs_eGQPtCusj9JCG_bkxOGQa3QXH7U4m1o3dlNYPQBTklsu-pMDuI1Lh-v43dOFZwh7R3DFvgFaIVCe2xJSC-_yhEojMxWk8MG6_QovGimdczmeO4fE9FxMdZkIFjaBntIkPn2JgrP0bF3372-RKZL0ah93szbs7iGsuWpw6JH2pwzCuOcI81j_N14KravIVb7sgnfta7hY_cvni5JwpRxGx1k8iHXhCkyHnxNsdBvcEb5wakt4c_3rzNqdRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خشم و آشفتگی دشمنان پس از تشییع امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447670" target="_blank">📅 21:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447669">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d743ee26f.mp4?token=pRlAY7VLbHDUhAbAmB8D4RoYFC5Oq7g_sGfrfWrtk0AtT4OrrOeDD1DFBER_obfgbyKavdTkwchU0w5rq4KJQrdDN4s1bTWa7YZoZWyaEaTdUZtYqXXDM358RcGo85iWavamowjumw3Mz_2ClD7JIL2dKq5TiTVxa-c6qtqxqp4MWQrRM6ZT_-y8nKRDaQCRHBKGrMio2LA8CSwtM2w0BaLuBB2CmrIP6KEUMPJq-0BE7QITboIUOfQruBXJbkCGXHUQDMWhqBlXmplunbdijAu5ujkeXuKKXoBrHmn_kDQ71GHcCmilWJoopSxH6UroyChkEotD0bCW6PyELJv3Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d743ee26f.mp4?token=pRlAY7VLbHDUhAbAmB8D4RoYFC5Oq7g_sGfrfWrtk0AtT4OrrOeDD1DFBER_obfgbyKavdTkwchU0w5rq4KJQrdDN4s1bTWa7YZoZWyaEaTdUZtYqXXDM358RcGo85iWavamowjumw3Mz_2ClD7JIL2dKq5TiTVxa-c6qtqxqp4MWQrRM6ZT_-y8nKRDaQCRHBKGrMio2LA8CSwtM2w0BaLuBB2CmrIP6KEUMPJq-0BE7QITboIUOfQruBXJbkCGXHUQDMWhqBlXmplunbdijAu5ujkeXuKKXoBrHmn_kDQ71GHcCmilWJoopSxH6UroyChkEotD0bCW6PyELJv3Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسهٔ امروز از قاب نوجوانان و جوانان باغیرت ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447669" target="_blank">📅 21:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447668">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5cc9d0aa.mp4?token=Ay6buQYAJTY4b0vgeMkXFI4Vyd_biRspP7tkcAXF3zySXmurq1gw0MvRl9NfMgZeqOJqSSQLpC8GV9kt-HexWPDlGvKTEWjgN_AarJYPZ25irF8EC0juW8Y5BR-Mf9K1bIYFcllr15Hn2g1VQXnkyJj2vSEr-IDhn86dO37F9wFHGE8cERxmaCwxbuz9uDyBd5G_3dWYUHVbT4SWMcj32HLQ5nJBY55GuFouCKxeyXg82wt5RuJzgK2TCvg3gDxYbeP4tHGNxEtLMXo9uf9rk1ivOqHHTgaBQPnG5SICvaFEPAG6BRvEiqEGcgrvzomPW_bu61R-MWXTz6-aem6DkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5cc9d0aa.mp4?token=Ay6buQYAJTY4b0vgeMkXFI4Vyd_biRspP7tkcAXF3zySXmurq1gw0MvRl9NfMgZeqOJqSSQLpC8GV9kt-HexWPDlGvKTEWjgN_AarJYPZ25irF8EC0juW8Y5BR-Mf9K1bIYFcllr15Hn2g1VQXnkyJj2vSEr-IDhn86dO37F9wFHGE8cERxmaCwxbuz9uDyBd5G_3dWYUHVbT4SWMcj32HLQ5nJBY55GuFouCKxeyXg82wt5RuJzgK2TCvg3gDxYbeP4tHGNxEtLMXo9uf9rk1ivOqHHTgaBQPnG5SICvaFEPAG6BRvEiqEGcgrvzomPW_bu61R-MWXTz6-aem6DkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب حماسهٔ تشییع قائد امت در رسانه‌های جهان
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447668" target="_blank">📅 21:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447667">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e22d09f3a5.mp4?token=KYYzLCUuB2amqYkStwDmCPaUgG3WObaftcF_ld9YsizIiQeR0YexFQS48Y5l3YGhjla0RMZNG3sDhDsaP4-6WtEn9Kc2q-CTlR42EwJ011Qex8Ov5Kw-B029UIQ-uvjkI2yDxODzcwg-qFfGGqeW7rEMkmsFOkn7chqjA3wPqZQEj_LmnCrkYtCxjl_CC4UGypBRv6W-qbMPoQM0iP7tdc-S74B5vEOTzjPvGOXrtwvPvEr3ExXiAjunTfTFIMcz4xe6z_9pb33w2z6Oo9W6TqlljprEz2LMuWRjGlhWweAozVABbgWVdz_2ENSOeegwD73MVxwzdkEdpfZlE1_ZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e22d09f3a5.mp4?token=KYYzLCUuB2amqYkStwDmCPaUgG3WObaftcF_ld9YsizIiQeR0YexFQS48Y5l3YGhjla0RMZNG3sDhDsaP4-6WtEn9Kc2q-CTlR42EwJ011Qex8Ov5Kw-B029UIQ-uvjkI2yDxODzcwg-qFfGGqeW7rEMkmsFOkn7chqjA3wPqZQEj_LmnCrkYtCxjl_CC4UGypBRv6W-qbMPoQM0iP7tdc-S74B5vEOTzjPvGOXrtwvPvEr3ExXiAjunTfTFIMcz4xe6z_9pb33w2z6Oo9W6TqlljprEz2LMuWRjGlhWweAozVABbgWVdz_2ENSOeegwD73MVxwzdkEdpfZlE1_ZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مسئولان در بدرقهٔ تاریخی رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447667" target="_blank">📅 21:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447666">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎥
پیمان امروز، ادامهٔ راه فردا
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447666" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447665">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7cdff38f0.mp4?token=XQ7dyimHUsZaw19Odf94LLv5VaaIqOpUKq57YcNaPp7fx9FpHDSLj1aJqj8fZ44ro-Vlq1mqhkjBzDg-fm2vaJqZBYqcYVejRw5aHXLzx0DQzYFSL4VtlVeFbcdHVxzdw3hNaYjN3e2e6E0xI_SYPEdaYGjQrg1zGUxZglmMGYMqmEdLRf6RQDF_OzjkpT54ey285vP5WbAhe7dCvgxNMrS-VfwkWUnGZx8cMLcGe2_NMrCFlRaOshchFIuDxMmFNLsv6IwzstIX7eCnDikxLKXrRC0Ww-yR76PALC2ZM1l2QblVbH74EihpSSvKKOj3jBFoGwRC5SLFMIZYKAP9Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7cdff38f0.mp4?token=XQ7dyimHUsZaw19Odf94LLv5VaaIqOpUKq57YcNaPp7fx9FpHDSLj1aJqj8fZ44ro-Vlq1mqhkjBzDg-fm2vaJqZBYqcYVejRw5aHXLzx0DQzYFSL4VtlVeFbcdHVxzdw3hNaYjN3e2e6E0xI_SYPEdaYGjQrg1zGUxZglmMGYMqmEdLRf6RQDF_OzjkpT54ey285vP5WbAhe7dCvgxNMrS-VfwkWUnGZx8cMLcGe2_NMrCFlRaOshchFIuDxMmFNLsv6IwzstIX7eCnDikxLKXrRC0Ww-yR76PALC2ZM1l2QblVbH74EihpSSvKKOj3jBFoGwRC5SLFMIZYKAP9Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از زوایای متفاوت از غوغای مردم تهران تشییع رهبر شهید در تهران
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447665" target="_blank">📅 20:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447664">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7a08a3b8.mp4?token=ac8Ywtr9aw0FfFmjDMwB3mh50ysP6V2LH6IX8lix6JKRQWORb_JcBFG6RhPobiL09HONenmW_y_6pTd7XBmxGepVx-82dxnrfDkgS6BskJoyvqZ-UfzKb5gWejjtRzxzFGEREDFiqWaaNZc3qnUATs_4xuqryMCTW2Ul8Z8K_KjQqwp7vXxqznsfM5bQygYhl0Nb7XxNPx2bBIBheaGP31FIOIwde83ltxqRk6CkJSG3NUYsVokjGY_h0E5zVJfn4QnoH16I-FoQv70UBCGiv6lcn7RINIoBRTm8Vu_LwFuKS8VQJeOA1vmRpggLPzyqdJBgQvm79FDqJiOMMenqFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7a08a3b8.mp4?token=ac8Ywtr9aw0FfFmjDMwB3mh50ysP6V2LH6IX8lix6JKRQWORb_JcBFG6RhPobiL09HONenmW_y_6pTd7XBmxGepVx-82dxnrfDkgS6BskJoyvqZ-UfzKb5gWejjtRzxzFGEREDFiqWaaNZc3qnUATs_4xuqryMCTW2Ul8Z8K_KjQqwp7vXxqznsfM5bQygYhl0Nb7XxNPx2bBIBheaGP31FIOIwde83ltxqRk6CkJSG3NUYsVokjGY_h0E5zVJfn4QnoH16I-FoQv70UBCGiv6lcn7RINIoBRTm8Vu_LwFuKS8VQJeOA1vmRpggLPzyqdJBgQvm79FDqJiOMMenqFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ملت بیدار، هم‌قدم تا آخرین وداع
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447664" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig5mMZ_yddDFDUU2Lc-tyyIAYliuzg0wkuKtZGZSsJoCsEHyecoxSxqJgjnbvfrEs1-kRgfU0ktZFnW0VZW9buxLa60B4z2IqshWqag8qXhlRFVA1JCaZDIxKRemtT3PlZ_acEdud7lxSJ2mwOkgmirWniZQ18Hgj5pmazKxLU-P6DaaJ-bYQqhlHw0_nk_v02gkm2bF9J4EINIRPtkpYlsbn4vKSZYjLeMaygrabe7lH4FMWVlie8dz67YpcucNP4h6JVwBuH-C89hUihkp8-I3XaNo1amsm_ebUmmpv7P2VMzuDfPKTMfvu8AYUniwx55QUEP3AeiskkmZR-PfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از حضور معاون دبیر شورای‌عالی امنیت ملی در تشییع رهبر شهید با تصویری از بردار شهیدش مصباح‌الهدی باقری‌کنی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447663" target="_blank">📅 20:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHk4qT-DNYSHzYYQuRSQOcv_qZHxNxY_M65rGf4pSZ0zKjcdbhuZAqPjjwTPw0NEOSVZaX-E3w5DR_nLH00hw2-tham29dKLOUJqzVAPcg4Q_4KPJucfApAGEZGUUpJhJwcw2ZAckJnj3koFHT0QmByJQzQyYmAUSDG2y4md3U5lVnk_Lgkdm1XeatPP7KFNqAhE4L0n9uDC7VtOWxyYCgBFdzq3KJYuXcTvXOAZ--a-Et_2l2JYOQ0slw-4mnL07ZQAvVDpOzlvMiROXuCJcJZj07TZ7EfXswLCXJ773GPh8dEIrfQ2d6DsoCQI72MlCHd651-_QPF6XILap5RTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
برنامۀ
بدرقه و تشییع آقای شهید ایران در قم
◾️
مراسم وداع: سه‌شنبه از اذان صبح در مسجد مقدس جمکران
◾️
اقامه نماز بر پیکرهای مطهر شهدا: حوالی ۶ صبح
◾️
تشییع از مسجد مقدس جمکران به سمت حرم مطهر حضرت معصومه سلام‌الله‌علیها
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447662" target="_blank">📅 20:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28240ed893.mp4?token=LVLs6QTabwFR0PTIqPqDMtZeSFwPU5ySIeOiXXH5XpBi-qzTjN7rQQ6hkB7fJNRHcDA1NNxx1wDRyMOzB03UxFbPpES1k5qu1l67dkGs62gPgv5DlVARm4qoVtfEvlpa1nCjPtEBkcBJohCUFXQj3DfQdndxNZGl8le9wDt8UxpQgxw94K5PG-RnN_jsnv4YYShrMGaUNe9-z-hLpAaLbbsfNCEiOjkRh1zEQwvNuZueMWrtCiWbTvSDDNMDqd5fQLtuwsH1rErskNsGGL7RW9s-JG95QdUdFERLodmbdUtj6lzNycnay5sjcheUgoC-BmFZAr0n9vWwWAQxu5vDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28240ed893.mp4?token=LVLs6QTabwFR0PTIqPqDMtZeSFwPU5ySIeOiXXH5XpBi-qzTjN7rQQ6hkB7fJNRHcDA1NNxx1wDRyMOzB03UxFbPpES1k5qu1l67dkGs62gPgv5DlVARm4qoVtfEvlpa1nCjPtEBkcBJohCUFXQj3DfQdndxNZGl8le9wDt8UxpQgxw94K5PG-RnN_jsnv4YYShrMGaUNe9-z-hLpAaLbbsfNCEiOjkRh1zEQwvNuZueMWrtCiWbTvSDDNMDqd5fQLtuwsH1rErskNsGGL7RW9s-JG95QdUdFERLodmbdUtj6lzNycnay5sjcheUgoC-BmFZAr0n9vWwWAQxu5vDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب به قم رسید
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/447661" target="_blank">📅 20:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447660">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234f9e8b93.mp4?token=TY_zOluxhmfdNqOQGFc1SDHe02hPAi7CZkNDREQj_bFSLfTXWlly7kGMukiu-TkohiIjoK-VnnTrKqSwesbmEUCNAFiKSmjev4TFpNfF0XvDlwKLSRcc4K1ikykJnyxsJEUtTT5VMXUUrSEkQ6ZF8UOLze_PCLJcdUEg6mEAGHaC-YU-1Nf7ygXFQ6Kq8j26GfJTUBX73W1Rkq3Va9wJ7O5xvYZVXhv-WH4C8N3gxL6WsyjbeARRuYgBW3B6EyVm3l5feZr3pFVl3om0xqfua9VbjoW9647Y97D_yd3nHuhEitJgKDO-RcunrL9hHG2ewrOcesSQUmOatZq-e1IcSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234f9e8b93.mp4?token=TY_zOluxhmfdNqOQGFc1SDHe02hPAi7CZkNDREQj_bFSLfTXWlly7kGMukiu-TkohiIjoK-VnnTrKqSwesbmEUCNAFiKSmjev4TFpNfF0XvDlwKLSRcc4K1ikykJnyxsJEUtTT5VMXUUrSEkQ6ZF8UOLze_PCLJcdUEg6mEAGHaC-YU-1Nf7ygXFQ6Kq8j26GfJTUBX73W1Rkq3Va9wJ7O5xvYZVXhv-WH4C8N3gxL6WsyjbeARRuYgBW3B6EyVm3l5feZr3pFVl3om0xqfua9VbjoW9647Y97D_yd3nHuhEitJgKDO-RcunrL9hHG2ewrOcesSQUmOatZq-e1IcSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور جاماندگان اندیمشک هم‌پای تشییع رهبر شهید در تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/447660" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58de79d79e.mp4?token=aNWUmHvZCiof8S7h6JRXvfYqjaoO8-4OA41fH7LbNbA3stZ0GeZyvO2iq6T0RZP6GXd_QnL6t4655QBbUlS9kMZMnMedKM6QPZcXfTzs6c5V-_qWEYPcNEBm7NxqpAD4moG-M0CupvDxsLXdqwEAfP1UxaBQ2IuOB4F8oWszfn25NAQf7E_727d1du_PU8pxE0djc9kNI5sOLpKS6LLiLoZYub6HF0pAgdISUqaCNL9hdsR_ILhae9nuRcnRJhn7AiX5gBMT8JB086W6ksNx_AG_PKoiGGUjH0TkYWfMApsiE-XNL9crPLeYbOFypRwbyVmA4yv2FHodbckHaBpbSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58de79d79e.mp4?token=aNWUmHvZCiof8S7h6JRXvfYqjaoO8-4OA41fH7LbNbA3stZ0GeZyvO2iq6T0RZP6GXd_QnL6t4655QBbUlS9kMZMnMedKM6QPZcXfTzs6c5V-_qWEYPcNEBm7NxqpAD4moG-M0CupvDxsLXdqwEAfP1UxaBQ2IuOB4F8oWszfn25NAQf7E_727d1du_PU8pxE0djc9kNI5sOLpKS6LLiLoZYub6HF0pAgdISUqaCNL9hdsR_ILhae9nuRcnRJhn7AiX5gBMT8JB086W6ksNx_AG_PKoiGGUjH0TkYWfMApsiE-XNL9crPLeYbOFypRwbyVmA4yv2FHodbckHaBpbSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی متفاوت از حال‌وهوای عاشقان رهبر شهید در آخرین روز حضور «آقای شهید ایران» در تهران
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/447652" target="_blank">📅 20:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe680719c9.mp4?token=G2ZIDqRYljxYCvTNpzWtkA5T6p2BUoobRua0MiDVJTaet-FQMnwRXNu9qrROLdxJV_AH7UUW5lhR8m-22wPBigmMGTSVsrfXG1sjv44Gs8NGEhUXENK2lTQ1n8yxeAN8qbzFQ0JgygrjN3DMHgs8l5mQNWjJoyoi7dY5CQ8Is3givxu-RtcD8x4Xwfe5rLMYdpEt-93hiJRDe2Zxt2hnie_4qnuNAGCJi3Wc4DQhA6mkRRv3ZacqrjYhNKF_kmt8meEw_H--4ur-d-4sHtCLWQp7jcHqGPQ7LSEpOv--pFOe3xj4FuTe0cSf8P0XX5QYv5FtlPkCcFV_owRymbJtZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe680719c9.mp4?token=G2ZIDqRYljxYCvTNpzWtkA5T6p2BUoobRua0MiDVJTaet-FQMnwRXNu9qrROLdxJV_AH7UUW5lhR8m-22wPBigmMGTSVsrfXG1sjv44Gs8NGEhUXENK2lTQ1n8yxeAN8qbzFQ0JgygrjN3DMHgs8l5mQNWjJoyoi7dY5CQ8Is3givxu-RtcD8x4Xwfe5rLMYdpEt-93hiJRDe2Zxt2hnie_4qnuNAGCJi3Wc4DQhA6mkRRv3ZacqrjYhNKF_kmt8meEw_H--4ur-d-4sHtCLWQp7jcHqGPQ7LSEpOv--pFOe3xj4FuTe0cSf8P0XX5QYv5FtlPkCcFV_owRymbJtZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیندگان آقای شهید را با چه لقبی خواهند شناخت؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447651" target="_blank">📅 19:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0065bbda57.mp4?token=Jlr3LHawkuYpP0W1zbQtxLmJOiVeKt-CyUmMysIX_PeHJZKIIxXKVw0lQLgdJ7TPlXiAstAjVoY4SXvITuEvVzBGk-0tNyPs6B72k4nqMU5rUjNdCqdCxUqPBWy7PFPMzUwxFLl5OmmgEQLteGSSUl05EM7R65bYOP7xG4pGhR9Ti-RISGCWTAekQtj9XHfSbHaEaxVocdSHyIx_7O7NJzTIcTdlFg8Vb1uMd7WIpbhjAECZ-DltLjxPQd5-C_ZXJdU4YKH0lDaqnhgm75rswgNY_nNwuadMncVKf4fbOorEF35GbIaoYjP7PGKHy8X2Lk1B546cLcH_NQ790GCovw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0065bbda57.mp4?token=Jlr3LHawkuYpP0W1zbQtxLmJOiVeKt-CyUmMysIX_PeHJZKIIxXKVw0lQLgdJ7TPlXiAstAjVoY4SXvITuEvVzBGk-0tNyPs6B72k4nqMU5rUjNdCqdCxUqPBWy7PFPMzUwxFLl5OmmgEQLteGSSUl05EM7R65bYOP7xG4pGhR9Ti-RISGCWTAekQtj9XHfSbHaEaxVocdSHyIx_7O7NJzTIcTdlFg8Vb1uMd7WIpbhjAECZ-DltLjxPQd5-C_ZXJdU4YKH0lDaqnhgm75rswgNY_nNwuadMncVKf4fbOorEF35GbIaoYjP7PGKHy8X2Lk1B546cLcH_NQ790GCovw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر ستاد آیین وداع رهبر شهید: از مردم معذرت می‌خواهیم؛ برای سلامت و ایمنی مردم ناچار شدیم پیکرها را از میانهٔ خیابان آزادی وارد مراسم کنیم
.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/447650" target="_blank">📅 19:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447649">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXFujhFooi15CniFRTsxmnOJzS7IlDs0FN8RyOjQIja-A0Qh253DZusfcJHlUtXprvXahoG0uW9ZH0UBU4iBCvr6msHMhfbq8V__5QHgKfBXsjH4HWj2feptEDuJO82uWZzSztqhI4OKYlj2wfPab3RBiqvOwfYbJ8t5yXm8AlsN1KhZXdTKhib626QqMOrGs6Fys9_oRiZt_sPZKQQqxc0wXh3DIUL49J_qn7Lsz4Q7xlgsiXEjOpYGZQ7cFQ-ipyXx_5u-K5_WzuSf-nBKgpNWroFHHUH0lIQ4TS9RGqxe6qLaOWOKZhFGHJxvFAQ3PxjQgJ9TBsyWXJ00DXWl5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: دریای عزاداران در تهران به آمریکا و اسرائیل نشان داد که تلاش آن‌ها برای درهم شکستن ایران شکست خورده است
🔹
رسانه انگلیسی رویترز: مراسم تشییع پیکر آیت‌الله خامنه‌ای، رهبر فقید ایران «فراتر از یک وداع ملی» بود؛ ایران به جای آنکه پس از جنگ ضعیف‌تر به‌نظر برسد، خود را «مقاوم، متحد و مصمم برای شکل‌دهی به آینده» نشان داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/447649" target="_blank">📅 19:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447648">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
حماسهٔ مردم مبعوث شده در تاریخی‌ترین تشییع
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447648" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447645">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سمنان تعطیل شد
🔹
استانداری سمنان: به‌منظور تسهیل حضور مردم در آیین بدرقهٔ آقای شهید ایران، سه‌شنبه و چهارشنبه ادارات و بانک‌های استان سمنان تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/447645" target="_blank">📅 19:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzzOq59KVkt1lExnD3LYUm625rgbYv2n1FIlkYdUUKtn25lzn_DkmINrZLf0_lkcCvqcWIqE0btFUnknGOSuipIJ6kHIG9sQIAQd4JI0EXYCP7Q1I8_r-UW_Wb38ElkMNQbmhDskg-gHhNip_jEUZUgNonmqP8ChI9-Vcd1WYBwo-guShcSnNCMNQR1RD_Ck-Uf5NlBREI9Vf56DrA_RyOSHzCGtSm3JW14dRPC4_kiE_KN5v0VMeaWQfRL56XoH3LAsWrvoQSFJSrcTObnm7BmWCTgNp1IbMaIgou-PiuFok88ZLUgaOxgFT645naxKHnVAyKo2j35403JLWxA-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuyxOomXF71csvyrOpYgHMKM_TI8axA0qpvsv3kvDzZXH-Ntokgo0atpzcBrYOwRyzlasPuhwoIK8ncM2j0akwt50Th17uuZZxiiYWht6YwWUGqd583eN1j1mPueUOtsTlAzESD0-WE5htOiKWumkwqcgVvn7sJUZnNU16X0ZA8YGsnqjfr2uEkQPkefGTW_rUFQDhQdgNje2T04XZcR0Jxh6efQyGBkPp1apBr2aapjluZVDslDIyUhj2eSYGdfxpJ-zD6KekJTDxdFQdL_pJNpG0lapbFZztXgQV_ptbWKx03GjmyZlotuByiEA0b7UWoMuPi2kKBUy6yHdKNJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4IPsQEHw9jLYAMq2SJT2nG0yKg9_jVVmLhlS3vzjzGQyBoYUFus5RLWHBXBDkCpvMzX7RN6oi7UfkVdgKbQypH7NsFjdC0coQnt3A-msPvzIbvQjTXCe54Uweio2O9Kp8lNHppaO5T19qUrYbwff7DiWPO0QrgQIBRa5KxS5I6kazFZyx_1WVDdvRzklI4gUNYa_lMYpaAqm7tB2Yoau0bWyqO8kIb1on9oBGgI8TUYtRfvnCizmhA7h6hYwyIMDQwveS3mnUT-2IbeCZSeKI35jhH8TlbtZ_TZEyxrSHQ_m3d1jUhxvI2k-zSt_e-NXmL-0x0bvOgnlwIhQ5Zrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkB_Jqi3vNujLYLS_HWv93E1MddvpE9cuCmf43pSrM-iC_5XhCZMOdw8cU8AYos2_X9lK43yDWOxFMYsz_x9jvSGwawlFXaiojAJXRa5RZLJ4egYz0_7r_YvGHp9Jeuk7ER8AUbrHOikOOKpw2r5UWZlKJb70EpZgavGaa7PCxbEpk1fZkeSX4vEltM1JjGBgsKKbhtnkOyzcwFVSEV0srNX539un4tzIqpTBicwv7xUSqOEQ4iDVNt41tpAqsglu0dxD7Cyy1JDihSN5S0KvK4qN7w6SbKs3BUrRJWbNorysVS3N8mHpgPWhwYrtTz8AohXNUtlPLPQ009GEnmaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzGbIbRK4pL2eWYMdY4O7CIB1sXNCUiNo765wDGX8cfGb656bWod6pXNTqBGu3BHxA6pIDovtkab6iWlILdhm6_7fsuWrq81vNbVSu-hxi7CepDsEp7C5F7TQLIx7-Au1WskdBBduVuU99_fzNAfZCLlKja6hmOUizZhs86OVsSwuSJaErZEdYg9CDKREkqmXalnQRmAvSNOWRGrL9zU-MTg_n3L-CdQSSXf6ojJp0EkOFYkP7vfRKh75f9CsViIH8JkNAkS072LQtQZ4tF7IaeTeRzCyLiEt5wuf7CsrmehMQpNhtsPc8EjzNat3Jpyre0ULyWNVXURizKB8KY8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QW0NBw8hmX1pT9Cmbxa_iLTmdM4YP32aaHlIJq87AQc88UDDiDuyigtkXlVVk7BBW3FUGYl_k8KWo8t0PvB3OqAM0AcyNUKcMVxmv1NyZq75-s5KBVTE6dS1IOeuXTXpsqHYqen6oGIVPjml0CerqHZZfzsy5bY_li_Xbowqzxh3lPG3QoigbA89WD1bgEJdilUu5KJuSInmom_yDuZkvTuBr7C6GD7XJrqDyrgKC6D-NHg9A0THRirVy6uDkgByL3gkNdsR9pMYOxnHNFi2psY7xnFaT9ZJ2m4BgHl5Czbtfr7MXhWTDJgC1kTbaiUq8LVCOH8MDNLfdSWmfT1e9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CffmTnrcYkVV6E2yNtgC2nLxlaVQe1pZY1mi2OE0Yq1UmEFlvC8dsu8rVtruZVcaB_vReveXgDW7Cdwx66A6JlF6yRmaYCSPhSgbYqK-ksZ1iqgpIZAvEtZOOhyPmuCGbv0y3hGumIX9EEdd1wZUZrXzfNBwWx1A4hWAK2q8QEgqvHejQBP7-wrS30x2z3XvqY6VD2vBWDYmioKcsxIGIUG2IkCfschpY_YNvuC_vTpmPReh5L_1-SEBqMp8i5KPrW7Ul2FO3Vbrthyr-RCNuaaW26F__tijczDseBO7C8-pi9qfcLz_0kvjD-GfquXU2bk4yMdPtuKKNwxCJl9h8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین حضور رهبر شهید در تهران
عکس :
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/447638" target="_blank">📅 19:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ادارات مازندران به‌منظور تسهیل بازگشت زائران رهبر شهید فردا تعطیل شد
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/447637" target="_blank">📅 19:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نقض دوبارهٔ آتش‌بس در لبنان
🔹
منابع لبنانی از حملهٔ توپخانه‌ای ارتش اشغالگر اسرائیل به شهرک «قبریخا» در منطقهٔ مرجعیون واقع در جنوب لبنان خبر دادند.
🔹
در این میان به‌گفتهٔ وزارت بهداشت لبنان تعداد شهدای حملهٔ هوایی ظهر امروز رژیم صهیونیستی به شهرک «النبطیه الفوقا» در جنوب لبنان به ۴ نفر افزایش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447636" target="_blank">📅 19:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447635">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c18cb1906.mp4?token=MSbv3wHDiMxjggq4_C7guknNfrFKnho0f1z3DeqgO4vhlaeekm8INDsTRk6myhjP9B3dQLCIuaEC0sqaAhx1FwghAnZ8jihvbW0vj3iBhesQmgMfCIFS74IT0DvvnOa1u-eM0oXG8BQJD-jBGY-pj4wXJL5bBYqtRQ4avjWA59kN7rOin5AKEKHd6AiwqclbqnWo6udIlYU_ldBt87vumQrHGcnO1cNCKSVFI2bwJux_Cjaq5FpmvL1hxNzRJGknS6edTifz4g6YI1IGDW9Mqt5SQsIfH0AqhjOrXbzfqLIqZgvn6vWd8pJFMtCNbyQiRlQf1yf2kSDA1URb4nlbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c18cb1906.mp4?token=MSbv3wHDiMxjggq4_C7guknNfrFKnho0f1z3DeqgO4vhlaeekm8INDsTRk6myhjP9B3dQLCIuaEC0sqaAhx1FwghAnZ8jihvbW0vj3iBhesQmgMfCIFS74IT0DvvnOa1u-eM0oXG8BQJD-jBGY-pj4wXJL5bBYqtRQ4avjWA59kN7rOin5AKEKHd6AiwqclbqnWo6udIlYU_ldBt87vumQrHGcnO1cNCKSVFI2bwJux_Cjaq5FpmvL1hxNzRJGknS6edTifz4g6YI1IGDW9Mqt5SQsIfH0AqhjOrXbzfqLIqZgvn6vWd8pJFMtCNbyQiRlQf1yf2kSDA1URb4nlbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به‌یاد ماندنی‌ترین جملهٔ حضرت آقای شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/447635" target="_blank">📅 19:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447634">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8W7YmCa3Oi1BLoarZO0MQF-WuOe2j_9av8jIcpGZaexwOUwHOP5YSDNrjvV3uxMCeR0Wc4_AWszisvmlFzSnuSO4sDh-xQRbp6JcYLN58PzlqPP65LtMs02D-v4jxTGe8oUsFXRpML7PFSYpZQrR_AbSzd8vhY_NPGX1Lw40qzblXGu8Gfw-7ryP3PXR3Xt5qt85t4yEGmNMdZ0vAkjKhKWcZqrW9LycDe2c2tJrDGH70szTilKGEapcmKCXFzJWtIOwo4CDsAOkZDGI_Rc90Xsr0CSy-HXgyX_lRjMRRWMNAJKZzTqqnVcLhpBO8_-P_KZhnJ7aG4OKv2VRUE4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
استوری درستکار، سرمربی تیم ملی کشتی آزاد، برای بدرقۀ رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447634" target="_blank">📅 19:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd45e1cdc6.mp4?token=HbdW5z4KKt1x-r-bHdAlpeUBah48ijbTxe45qqxCCqWPdkgJA7AXqbJvTy85-7lhUTGVErDjHNcuSUn0paeJ_0A11v3JmimHg99pmUIYN9UWsa3OTA62IsyacMGa9j0-QdZOXSR3ofZk5xL6kYWXK0H-DWKjp3YgPK1CbZVAMX7CwuRwrrugOVoCAg_qRPxVSsnuS9rquyY4PGKiYltzNauZj0ei0JmEwfGD7kpk_l6Hyl-GhyEPu6KpMSxXaEtsTj1KstcYE839gsy25cLOUYM4j6ucpcVBGBhoy8BdQ9kkR2DL-8rUt42rkgwC8sTIz6Pic_qztc_KpdGN164O5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd45e1cdc6.mp4?token=HbdW5z4KKt1x-r-bHdAlpeUBah48ijbTxe45qqxCCqWPdkgJA7AXqbJvTy85-7lhUTGVErDjHNcuSUn0paeJ_0A11v3JmimHg99pmUIYN9UWsa3OTA62IsyacMGa9j0-QdZOXSR3ofZk5xL6kYWXK0H-DWKjp3YgPK1CbZVAMX7CwuRwrrugOVoCAg_qRPxVSsnuS9rquyY4PGKiYltzNauZj0ei0JmEwfGD7kpk_l6Hyl-GhyEPu6KpMSxXaEtsTj1KstcYE839gsy25cLOUYM4j6ucpcVBGBhoy8BdQ9kkR2DL-8rUt42rkgwC8sTIz6Pic_qztc_KpdGN164O5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا دیگر این شهر تو را ندارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447633" target="_blank">📅 19:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447631">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTDDrMNYrJ8W82kFMK0ZzmuE-AFsaL3EPzMWIsbx99ELAgSXJ8I9H3DLgslJqBFSAFqOiphLKzXhVH7YPWXrxmRpX6ec-uW1sKtfYfpbQRbNgG3PxSkak4lrZOdGKTEpunEByu58JkmDcHyQUdsFfSIS-faYC6frFcN5_GByHThTZ9BluZf_OPl4gG8S16mT-fdBWyiPuMiJawtqV9Fhg6nbf7cFTdysrKWNMAJH6nOQ2iDA8FL5IzRozUr1P-VJq68ch9G0TlJB--Saj58Pv7BQa46RMZ3sTm361St91al_yuEuJic9rnk4KqB80OjMlB_TUrVlq7b8cjqNporteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رفتید سوی بزم شهادت به‌سادگی؛ خوش باد بر شما سفر خانوادگی
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/447631" target="_blank">📅 18:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447630">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f5e3fe8a3.mp4?token=XwUNPqD7mNiUioMrkNejsUQdKnTofLeYh2vSNcRR07AF-6eRiL4SATWXw_S8CqBPb1pDk-E5nUxN707wGnXu5r2I9J4dysxGvqUtxFWQclYNaZuofVIrt_TbnPZ4zSCcd7ZLupcWuc11FHbcnWfBKxJolvqxNZWNmKhLt2YLy5KoKJZNh48z75VAN2sMyb6WmX8PTSlGok3-hUO1-jxPel3hkSdFBCvQXBzRouZp0fv4Q_BVFt1m_l2rI_N21Q7k4h9NH5BkY927Ag4MVyMZIWjS7O7UAqTwLg35pcpJxXOkIcKLLrRZ-xp1hbNXZ9Y7H2d_pBn16M18O07oz5INig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f5e3fe8a3.mp4?token=XwUNPqD7mNiUioMrkNejsUQdKnTofLeYh2vSNcRR07AF-6eRiL4SATWXw_S8CqBPb1pDk-E5nUxN707wGnXu5r2I9J4dysxGvqUtxFWQclYNaZuofVIrt_TbnPZ4zSCcd7ZLupcWuc11FHbcnWfBKxJolvqxNZWNmKhLt2YLy5KoKJZNh48z75VAN2sMyb6WmX8PTSlGok3-hUO1-jxPel3hkSdFBCvQXBzRouZp0fv4Q_BVFt1m_l2rI_N21Q7k4h9NH5BkY927Ag4MVyMZIWjS7O7UAqTwLg35pcpJxXOkIcKLLrRZ-xp1hbNXZ9Y7H2d_pBn16M18O07oz5INig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبۀ مراسم تشییع رهبر شهید در حرم امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447630" target="_blank">📅 18:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447629">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پیام مهم فرزند ارشد آیت‌الله سیستانی به دفتر رهبر معظم انقلاب
🔹
آیت‌الله سید محمدرضا سیستانی، فرزند ارشد حضرت آیت‌الله العظمی سیستانی خطاب به دفتر رهبر معظم انقلاب نوشت: درست این بود که پدرم، آیت‌الله سیدعلی سیستانی، بر پیکر رهبر شهید انقلاب نماز گزارد، اما وضعیت جسمانی و سلامت ایشان اجازهٔ این امر را نمی‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/447629" target="_blank">📅 18:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447628">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr2Vh690KK-upwtvZx0ZAwWw7S3n9ZJGur_Y3NMsgkgXDxnAl_M0B2W84eUxErdYpgHWBIhJmbQy1oWBfLKXMXrnAa58lJJbzJrqNvkeXNuugMdA_2kIdg6u1vDC9qYU0vciXyCRMaqjRnezHUr4Pl2l8rhELh9ghPpCx1QCmyjfKkZqdJyqYTAW8Z5JOs8sLcVwt3Z1wMUw_CgruZyxUqDqC2KiizbA7JenVAZxA1UKzwkC--NWrg56d-CsBX1UCd6tR4Z_EBHNZ4lzXb_8Whl2pSQdTlFieE2cEkbKT_vuvcX0F_b8ZUwTo1YIPjUdO64EO8l3_r9uRWlW8wigJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حماس کمیته اداره امور دولتی غزه را منحل کرد
🔹
دفتر اطلاع‌رسانی دولت حماس در نوار غزه امروز از انحلال کمیته اداره غزه خبر داد تا اداره امور را به یک کمیته تکنوکرات منتقل کند.
🔹
دولت حماس با اشاره به اینکه اقدام مذکور در راستای بهبود وضعیت داخلی و در راستای منافع عالی فلسطین است، تصریح کرد، هدف از این کار، کاهش مشکلات ساکنان غزه و گرفتن بهانه از دست رژیم صهیونیستی است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/447628" target="_blank">📅 18:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447627">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb-4d8E4NX9Zbx4e24XooIUspBS8PuhHw-fdVEnSNmXlkdLL8SDbaEOZ97t5QqrkUlvm6Qu6fYufON3X1jMHanOx9--0wawenbU0EdtdDCv2Z1vOf8z6ayZxYacoDbL8Lz7ktRVifP6ItvjioDHgU-S7vPeo4eS0INbsMJVeOtFYcgLuFlJUGStVPYP3HmcOz4SgUk66YLBwmvG4ZhsDVjZgtN6J_6UI-vZH0ieDRRKH6mabi-XFRjzKo5QCW2IAJaYwMzprNebKaV54rZemLOHnatF6jJB9YHcyB-zVJIakbFGmuf_fO3EazhcDgEF_zNM0o3UC9KUbMqk93VSWgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
استوری مهدی ترابی، بازیکن تیم‌ ملی فوتبال به‌مناسبت تشییع رهبر شهید انقلاب
🔹
ننگا به ما اگر که ز خونت گذر کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/447627" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447626">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309edf5817.mp4?token=CUrpwcvTgyw8uGlPY2slMooHIuVBHSzhZAIsL64Znq3BHre3VSQcXQkb8QRixyJ8GeUyMZLUGh_RMcLz1ZOtP97sqyBNZoG_QPQd1i7CkOJPlAW1UXjnWyx0ZvLsdXwW3s6vTfXQ_FeTUd1r8i22U_vD37sbfBTJ0ImmaSi9LTwj8l9zJLrp3ZyfU-U6i2iuvHFx_RVuYSCZPqwhu_C3m1TQAHv-LEhfeeBLsQu4F1W86uaqTnw41XfbD8a7pRcQ00kjFN_ZYDccUgy2_XIo16sL6qL0cnunjMLCkW5PTcPtHbfXo3aL5Np47sxffqSrIykuGBzCwDTW8_VH_MIKZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309edf5817.mp4?token=CUrpwcvTgyw8uGlPY2slMooHIuVBHSzhZAIsL64Znq3BHre3VSQcXQkb8QRixyJ8GeUyMZLUGh_RMcLz1ZOtP97sqyBNZoG_QPQd1i7CkOJPlAW1UXjnWyx0ZvLsdXwW3s6vTfXQ_FeTUd1r8i22U_vD37sbfBTJ0ImmaSi9LTwj8l9zJLrp3ZyfU-U6i2iuvHFx_RVuYSCZPqwhu_C3m1TQAHv-LEhfeeBLsQu4F1W86uaqTnw41XfbD8a7pRcQ00kjFN_ZYDccUgy2_XIo16sL6qL0cnunjMLCkW5PTcPtHbfXo3aL5Np47sxffqSrIykuGBzCwDTW8_VH_MIKZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: تنگهٔ هرمز یک ماشین پول‌سازی بزرگ است
🔹
ما امتیازاتی گرفته‌ایم. اکنون ایرانی‌ها باید به این امتیازات پایبند بمانند، اما سلاح هسته‌ای در کار نخواهد بود. ما قرار است مواد غنی‌شده را تحویل بگیریم. من به آن غبار هسته‌ای می‌گویم. من دنبال تغییر رژیم نیستم.
🔹
نیروی دریایی ما بزرگ‌ترین محاصرهٔ دریایی تاریخ را رقم زد، باعث شد در طول ۲ ماه حتی یک کشتی هم نتواند از تنگه عبور کند. و سپس ما محاصره را لغو کردیم چون به توافق نزدیک شده‌ بودیم.
🔹
ما در هر صورت پیروز خواهیم شد. یا توافق می‌کنیم یا کار را تمام خواهیم کرد. ترجیح می‌دهم توافق کنیم چون نمی‌خواهم زندگی ۹۱ میلیون نفر تحت تأثیر قرار بگیرد.
🔹
ما می‌توانیم پل‌ها، نیروگاه‌های برق و تولید انرژی آن‌ها را در مدت کوتاهی از کار بیندازیم.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/447626" target="_blank">📅 18:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447625">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/559e520b6f.mp4?token=RXiyArXHK3icTOaaEpfT24Ug9-bY2ERFpSdw1C9r9h4AIJaCdDkli8B3Fil1QplM7qcCxBo1KJo2ou4r1JQ3AMLJuZGD4_ZNlXuFuoDl1x_TBp9_FTPdEu26XoWhoGDdvUvCFtlwoAE4KDjzOmsKO0CgusDZfyLtJSdiY6Zy7uR7WTphELtURhVckkEZ2Ez3FiorR4VILnOfTm2ZObrAf8H0LGtC8ewGLr6TTXu13sMs5WKPV-EsG_H7dUDNBYIvk9gcKb4LNSTfA4WZD9iTlCzw84PjTxIXMEHwVsRlqvKK8lAKXxq7vfRPUzy4lLlSW4LBoL8A8Rx0e8zs6Z6_mj82gTFMWK1NV30emx1Pd2R4_mmvrMIXXJn3VdM2Bg8F1F0Yd7OZJHYhmqUVRZj5HIdTKZ1hOJ0M8B-Du9bzff0ZME-GT_9dh1ceFgJN0w83CjSMe_lrqQKm5ImcOIqaKjVzCaVx6CeOgl4P-DpAdvGH0pN1UArxm1J2R4QPweFgktSvFCqZMYfPFzsmPjBbnKBXKckvkXaWWXskQtEvzWJhJTxKOpjaQPeMEThPNXfpXhY4Apt7io4uaNR11IJcUpELk1ecdXDeuVmmyjnmNuaY6M_9SnO9H_eaZ_bDpFkmmjWPJHY3Cu_n7R1TEFgw3PMadNh9E6VLGqW-k5YkadI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/559e520b6f.mp4?token=RXiyArXHK3icTOaaEpfT24Ug9-bY2ERFpSdw1C9r9h4AIJaCdDkli8B3Fil1QplM7qcCxBo1KJo2ou4r1JQ3AMLJuZGD4_ZNlXuFuoDl1x_TBp9_FTPdEu26XoWhoGDdvUvCFtlwoAE4KDjzOmsKO0CgusDZfyLtJSdiY6Zy7uR7WTphELtURhVckkEZ2Ez3FiorR4VILnOfTm2ZObrAf8H0LGtC8ewGLr6TTXu13sMs5WKPV-EsG_H7dUDNBYIvk9gcKb4LNSTfA4WZD9iTlCzw84PjTxIXMEHwVsRlqvKK8lAKXxq7vfRPUzy4lLlSW4LBoL8A8Rx0e8zs6Z6_mj82gTFMWK1NV30emx1Pd2R4_mmvrMIXXJn3VdM2Bg8F1F0Yd7OZJHYhmqUVRZj5HIdTKZ1hOJ0M8B-Du9bzff0ZME-GT_9dh1ceFgJN0w83CjSMe_lrqQKm5ImcOIqaKjVzCaVx6CeOgl4P-DpAdvGH0pN1UArxm1J2R4QPweFgktSvFCqZMYfPFzsmPjBbnKBXKckvkXaWWXskQtEvzWJhJTxKOpjaQPeMEThPNXfpXhY4Apt7io4uaNR11IJcUpELk1ecdXDeuVmmyjnmNuaY6M_9SnO9H_eaZ_bDpFkmmjWPJHY3Cu_n7R1TEFgw3PMadNh9E6VLGqW-k5YkadI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی؛ بلندترین فریاد مردم در تشییع رهبر انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/447625" target="_blank">📅 18:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447624">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59aaacce4f.mp4?token=fr3zgN9zckXKG7TXPWMNf95ZooFXQhy9a5mApao7yJwGBm7_Xd7_1hRHSBYvJE19hEXfqB3H3A5fqoEmnywJ9hC6LXeivpBOWAv9khKHFmEFtNT582ebEUntE7pb88dbMTHlFMhke8JOPs2GXPTEbjaIznxREIkvwUBOGbBC6hj8bNcdHfUkJQtJBewGKU119mzn8PaJKRxbh9eJoiRKn6WlmJj4t-jasKrF83tK-XVN1DZgaG5MU6AmydzDNxMvYuUV6nIib1tBGmCXGSqc_f8lI71pWJ3AJ6tzzylLBDL32AImyKVPEBpqpNhMoyxN_qKtCV6n8D-uZ7Dzzgn-yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59aaacce4f.mp4?token=fr3zgN9zckXKG7TXPWMNf95ZooFXQhy9a5mApao7yJwGBm7_Xd7_1hRHSBYvJE19hEXfqB3H3A5fqoEmnywJ9hC6LXeivpBOWAv9khKHFmEFtNT582ebEUntE7pb88dbMTHlFMhke8JOPs2GXPTEbjaIznxREIkvwUBOGbBC6hj8bNcdHfUkJQtJBewGKU119mzn8PaJKRxbh9eJoiRKn6WlmJj4t-jasKrF83tK-XVN1DZgaG5MU6AmydzDNxMvYuUV6nIib1tBGmCXGSqc_f8lI71pWJ3AJ6tzzylLBDL32AImyKVPEBpqpNhMoyxN_qKtCV6n8D-uZ7Dzzgn-yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم! آقا از تهران رفتند...
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/447624" target="_blank">📅 18:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447619">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmiA_Qct5vTniXJAJaqLtGqo1mVdxwdO5hMapaa_NPcyoL69yKg8WCF5r2NrH0g-JIiJzCsvCubQnCUykNK8qMTJZwTYGWtVJ7U-OmPnG53YLL-JubjDeikOqkFlrJr_GmJBms4LfkLLwPDmbxiLcf4IOxbHTYzRr52EEfYHuuEXtAYXFtVMY11KyZRieAY4wcwksHVVaMTIJ62AhEc0665KgfSNcX7T6o87ctFGbtBXeTmlCaH63JLtHocjKzaheNcdeAuKeZHkSI0ZlZqr8LStWNaDHHSeKpBhFFk5nTQ52Ipo5m_sS0ZDRNKM8FqFJQuEmbVYdzYwMPDH8ThSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffaGgtGg4-Y8E-f8RavQsBeEutBe26db3OWOe8_lxKLjO7m6n9Uy8J1ME8qIbBlgQjdqxazk6Pk5xzmSO29XhyI9lPgDUuzyKcWLuxuez106Fb0vf27MvVwQ9cm-89VC_Zjr5W-DGOU0fXtrYy3aL5pNMY3G6Rwq3Po4QCr9Mgf0fYxjoBP5q_x6pPHUnPcbOsTXur43Jh3yRBhgKt8UeSLr4CoKoj1xdn3QH_DawxTjmSdq_6hQn1_5olmQ3Mr57GBlslB7ih9P64ULYDiboamlOEnKOo5noGoNwuW3yQUv24gR0f66kziwdD9JLHTW8oM7sQo6TsoJIABPXMmiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uN-t2kjf6wg-tSfuV3NWDtXxL_VJUCmgcW3lsooouj998jNSMIwkatXcWlRTSg4XwlZc4zYQ4W9J_qbJ0FGimEH89ticurMXz03jSu94lyY_d6yxA_u1JBAZOHcRs6D5Pc3Mswol_phtEF5rv4w0GQZ33z55sbHM7kFxKGyIZdQj3cS_gQDbGDKN1CqrmvbS53I_acXDdhYM3RJB6MDr3FL98mcStO37Jp5d2CZ0EAbDBtUA_HKgzyFt2JgaqF0Ne3CZeWZNagiSWOTXrKKloQK71b6-ooy8IKxrDQvR1zhqrng6AiXIpg8KODbjuo_XytUvR12-Jwp9583fOKr9EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOSIohxyuPDxoPOeLk_NFbWzhTb6NaO41UR6N4rZg76jwt4VICVaLuzSsPo-iU1eZa22O8HUhhxo5tYplKg5oJhbUX_0x4O2uQs0eEaKra9Q0Lzz50DKosHwox-yivn0R8xoM5HxilsQqOq_AKfU4EiCD-Ocha4KRl0hfRoP5n9S8D9yVsSFzfGtJ4V5Jb-x_AVoNONtTtcfi7HVOppX-s-vpatJDKJHWTEvUX6Zk5GlBumq4Jk5IgaIbIyvcmCyBEKOtIuts9bVj16LtlG5Pfk6GTTxc-Q2sI04g3OlyQ2EGSqqiNBYr8zHHwGfgLIm5D378dQIIl_3SAjEFD3PUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bY68LBftc8MF7B01vy6enWl-r2qIh0DeY8Yw_7cjXfa8h7Czzz2Zcx4y8U5m-Hd5kZy5zAfCXC8P1MyxhMkIzYLiS5KNdxNRCwOJ0qhoA14YJzTywUU0HA45XITH7Xve20C346BWryiNaLbzbGfKR4U1Oc-bMpopRNFlJYGTUnm5a4Nb_us2kelw_VUvxidYn-yqv6JCOl56uk0FtcVYVL-e-9xFlb24Gc9HZbihKiPgNOS5Bn0IEAe3SleivB_Bj3xHK5v9syxd4R1iF0IUquz4_76GuXeT7HPdS7q5ZEShOp1IT7j6qWzpluBKZtXYK469qqDULpJPoDN__8rC4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع یک ملت؛ تهران میزبان باشکوه‌ترین بدرقهٔ رهبر شهید انقلاب
عکاس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/447619" target="_blank">📅 18:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447618">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e4aae075.mp4?token=vU90c7Q5vN2LkGJ2JioHSsx31mhln-Y4pq7QhCYdzjR9KdCZuptt9BqBURRxhcpi9TIb9LNFrLFZj1E8sEa_iQSdCnax8fbcRz2OKatiWYTCRRMTnGUM6i2mrh2_U7dyFja16jTugr9EIOOQ8QAgHYDjq5vtlD0fzeqpxnRHuPIcTQEBGLBRbvAGo1UQR8PDnJ1ECHmn43CgE1OViyt9NN7MSJz0ndOh5tIHTYbSvyRbWBKmsz409InDrh4l6BfrPnS51LRFcULhdvJ_XTyE1Jp8lCOH3yHAZAaonB7Mc1EqMYMes_VkGhdiNBujTdY20Sp8nLTHfHczgf_NyKqqiiyE_m-xOpuofEhy50q201IY8vKLVUDeGYSQ8i5v0Qy7ptYya3vl1-Koy9e9tGJC6Bq4AuOyKjIiDSGlfZoT0zvO4KhMSg5KmgZHbkCq2heksI8B3DdXpksj4qJz9DEVdW0Q3AUIk21d1NTV3bdL5DSMEt7pt4JwpfcUL-2TipWLu-mxY-3I0TFVSPL0bga-VG6l78XNiG8fz10w3J8lhOXX0dU-sBBq5EcQ1aY63Nc6rXVQfMxamchGbQhIMCFmP1RO1OxQj_A3Hkh4E2_x0KnO7-xQUo5kKW0ktUpat9TuhIjvtDkJu15AwfQqRDEJkviu_EfCTI5N3FT8uwcJQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e4aae075.mp4?token=vU90c7Q5vN2LkGJ2JioHSsx31mhln-Y4pq7QhCYdzjR9KdCZuptt9BqBURRxhcpi9TIb9LNFrLFZj1E8sEa_iQSdCnax8fbcRz2OKatiWYTCRRMTnGUM6i2mrh2_U7dyFja16jTugr9EIOOQ8QAgHYDjq5vtlD0fzeqpxnRHuPIcTQEBGLBRbvAGo1UQR8PDnJ1ECHmn43CgE1OViyt9NN7MSJz0ndOh5tIHTYbSvyRbWBKmsz409InDrh4l6BfrPnS51LRFcULhdvJ_XTyE1Jp8lCOH3yHAZAaonB7Mc1EqMYMes_VkGhdiNBujTdY20Sp8nLTHfHczgf_NyKqqiiyE_m-xOpuofEhy50q201IY8vKLVUDeGYSQ8i5v0Qy7ptYya3vl1-Koy9e9tGJC6Bq4AuOyKjIiDSGlfZoT0zvO4KhMSg5KmgZHbkCq2heksI8B3DdXpksj4qJz9DEVdW0Q3AUIk21d1NTV3bdL5DSMEt7pt4JwpfcUL-2TipWLu-mxY-3I0TFVSPL0bga-VG6l78XNiG8fz10w3J8lhOXX0dU-sBBq5EcQ1aY63Nc6rXVQfMxamchGbQhIMCFmP1RO1OxQj_A3Hkh4E2_x0KnO7-xQUo5kKW0ktUpat9TuhIjvtDkJu15AwfQqRDEJkviu_EfCTI5N3FT8uwcJQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت جذاب از حال‌وهوای مردم کربلا برای بدرقهٔ آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/447618" target="_blank">📅 17:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447617">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6db0b54b.mp4?token=WXeAB9MucN8GgO1yL9l9Gz35VdYQj-QcNiSxy7Z_vWH3G48gbXZ9GiQZU4zo9kmATczJVyfsdZi-H2j2qs4sqVvwneKZVP1kQ1pkt6FwDzZWS72GgnBTtEm-LQVo1R0WBN208lUT2lHQdL8Jvhzq_bo2-x0g8I5I35eWfqtbNfyH3ESANWJTNg2twJXVkc_BZqysg8l_mMcSIMbEtRuRNwQBszktwR7ms5wk_N-ggeq6oPRnE_5CZrZJca2X1m7cRkT2XzRbdLaBhHeGLDjueeq4J9oGOAbpj_HBPTbVNbizks9u0zt2cE7E4A1mgKAuLPnIkPpOOhL0nBTwy1rWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6db0b54b.mp4?token=WXeAB9MucN8GgO1yL9l9Gz35VdYQj-QcNiSxy7Z_vWH3G48gbXZ9GiQZU4zo9kmATczJVyfsdZi-H2j2qs4sqVvwneKZVP1kQ1pkt6FwDzZWS72GgnBTtEm-LQVo1R0WBN208lUT2lHQdL8Jvhzq_bo2-x0g8I5I35eWfqtbNfyH3ESANWJTNg2twJXVkc_BZqysg8l_mMcSIMbEtRuRNwQBszktwR7ms5wk_N-ggeq6oPRnE_5CZrZJca2X1m7cRkT2XzRbdLaBhHeGLDjueeq4J9oGOAbpj_HBPTbVNbizks9u0zt2cE7E4A1mgKAuLPnIkPpOOhL0nBTwy1rWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تارا اوگرادی قهرمان ایرلندی
ناوگان صمود در برنامه پرچمدار: مشت گره کرده آیت‌الله خامنه‌ای در هنگام شهادت برای من نماد ایستادگی و مقاومت است
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447617" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447616">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2xaHFna-re32QI_MF7dFPD29e8_wBtTSzinR1GtpYFrErQuoNi1aqOqNprwmK2u-FLyFWh0OxwkUa9tbn8Yn_SaYBDTdKrWT0zCuNDfo0SKXfXJqueL8Zk0Hp20HxwodruKx5GnwxHAmfwYqnDMw0T7Eve16OiZFvqB2YL8pUlZ23eyyLp92K6kYyeO02heSkFiesXcKRDcdaksgslzE97TlLRi8Kv2-eZmG2SE7TlVA6wz-dMZUH2L4eJaEAaXMHsqLXAbUEVWKaC1A5ewUMoEnd2FKP4DJ3nUeTOVGbOTMJmYIZWD9LXbAt1Ls1yzSCD5aNOIL_s9irk1RsbOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پردیس احمدیه: ای رهبر شهیدم راهت ادامه دارد
🔹
پردیس احمدیه، بازیگر سینما با انتشار تصویری از تشییع پیکر رهبر  شهید انقلاب نوشت: ای رهبر شهیدم راهت ادامه دارد
@Farsnart</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447616" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9065214fb.mp4?token=W6efHQDSs6QiQSY9OsYC-UYo-pOx1XICR1Wa1WMD0RhtKdZE54tRgLIi8ymEf6khlunjZRAcQBTkKScpbgmtcQYaVK3d6XPD5tZBYuXigzFivl0uipBv7aBqm5qAqHmdF9ixuQ-n1Vf04Rcmx1xFZ7gh-PbkCS-TJtgbK7aPDPAoRVXJq7QDCNCtkyVt5M7ZOgiv9bTm14YUaoES-_kl5gtNmj_t0aBe5SNGBhTNtfCfNbzQVLbCHHvpZta37Sh-fKLL-Ty7iC_Idx_Pdh8rT10AAvejirGPlXLLcpo5pO1WRgUOFKCbEzkiTMR7NWIIDWs9XADVr9YYH07h6CV1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9065214fb.mp4?token=W6efHQDSs6QiQSY9OsYC-UYo-pOx1XICR1Wa1WMD0RhtKdZE54tRgLIi8ymEf6khlunjZRAcQBTkKScpbgmtcQYaVK3d6XPD5tZBYuXigzFivl0uipBv7aBqm5qAqHmdF9ixuQ-n1Vf04Rcmx1xFZ7gh-PbkCS-TJtgbK7aPDPAoRVXJq7QDCNCtkyVt5M7ZOgiv9bTm14YUaoES-_kl5gtNmj_t0aBe5SNGBhTNtfCfNbzQVLbCHHvpZta37Sh-fKLL-Ty7iC_Idx_Pdh8rT10AAvejirGPlXLLcpo5pO1WRgUOFKCbEzkiTMR7NWIIDWs9XADVr9YYH07h6CV1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر لبنانی: تا نابودی اسرائیل دست از خون‌خواهی نمی‌کشیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447615" target="_blank">📅 17:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447614">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13492af301.mp4?token=sVRX0cQHqBG9yOSDvjX5jxZcZ9EXkBEZOV-cdz-x5moOwYiTCYWgfRfh0zWFGK-9zyji92BXK0lcHw34EoPPvoa4L50Q7KlgWWkG8OyKO5PAaiu6i9l7PCA6ikHTiAO1GVDMr9lJc4KoYVl0mEaE9_9yOLFQTVRhaUoDtlPYGfdsk7MLzU3c23l_kEVJTtjV41qqTmEoNz1r--jegKqjToO9gW0I4K6Ndgo2GY36CT2Yg6_dkcFShoKOhonAGLRKyrMM6s6pl4YSfYX9c89fvFRF2rhPzh1HNUF1IalrvoGMO9CZf3fElLCjzoQ2o-Fw4gn4yChrPkjaEFo2VDmzkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13492af301.mp4?token=sVRX0cQHqBG9yOSDvjX5jxZcZ9EXkBEZOV-cdz-x5moOwYiTCYWgfRfh0zWFGK-9zyji92BXK0lcHw34EoPPvoa4L50Q7KlgWWkG8OyKO5PAaiu6i9l7PCA6ikHTiAO1GVDMr9lJc4KoYVl0mEaE9_9yOLFQTVRhaUoDtlPYGfdsk7MLzU3c23l_kEVJTtjV41qqTmEoNz1r--jegKqjToO9gW0I4K6Ndgo2GY36CT2Yg6_dkcFShoKOhonAGLRKyrMM6s6pl4YSfYX9c89fvFRF2rhPzh1HNUF1IalrvoGMO9CZf3fElLCjzoQ2o-Fw4gn4yChrPkjaEFo2VDmzkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام
پناهیان در برنامه پرچمدار: در تاریخ اسلام شخصیت جهانی مانند رهبر شهید انقلاب نداشته‌ایم
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447614" target="_blank">📅 17:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آزمون کارشناسی ارشد در روزهای پنجشنبه و جمعه ۲۵ و ۲۶ تیر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447613" target="_blank">📅 17:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55393f65b4.mp4?token=WFjplgX0GYrVRLaC-sstpz50JfL0I2PSfPJtshLC3LCr5C2hjJonA77AlC4jae1ZxJmM0dMbSLqqp1LT6rPDPMuuCY5dBazok9099P6DQkmL4PsumoUXvviXYI3Vc8Czfn_PlW4Qwg9OUTW45H6S6mIf4JuDTAWlMYe-V0FZ2rfZekHSdSaBW_anE927-KiENJLhvzpHG5r8WNFs9yLO6vU5pqSpnW0bfnowj3krlKvLEVMMgJOU4t2gbiuVkLknS2yFsQb9L3epjEL21DsbNS9J8B4s_yw3JtXMWp6kFTYG1xIS2WLasvFNfrvdYo_lOe5nzfCd7rQhVJ9iK_WlPV-vzDXNJC5d1oms6ECQxXa3CGc2ngiL45PG8W6SeAmyq3MsFGASUMCJYFLVoEkw0YexuUd3TIA-Cx60nenSWQfOadKpJ8rb7LUOZe0LE1K-xIBhih8BPSGcrkUY3v7eMjlkyG9AfH3buceraEhYNK4ZX2KTwUQIfs-BPY0s-crgK2ioKOEKyzzNcL8yjaJaA5Ra3CG25pgYCjpXTOpSPsDDCK91FvANq6_mP8mMJIygVstJvfOUuVBaOO6_HLStevzFk7Sn4eHncYwldWQ_ihiU5SaR0Fv2txQ5CgaZlIjOuSQoaNtutj1E5eRNrVHP2_9sLvK8Ce0-1JVpUgnsjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55393f65b4.mp4?token=WFjplgX0GYrVRLaC-sstpz50JfL0I2PSfPJtshLC3LCr5C2hjJonA77AlC4jae1ZxJmM0dMbSLqqp1LT6rPDPMuuCY5dBazok9099P6DQkmL4PsumoUXvviXYI3Vc8Czfn_PlW4Qwg9OUTW45H6S6mIf4JuDTAWlMYe-V0FZ2rfZekHSdSaBW_anE927-KiENJLhvzpHG5r8WNFs9yLO6vU5pqSpnW0bfnowj3krlKvLEVMMgJOU4t2gbiuVkLknS2yFsQb9L3epjEL21DsbNS9J8B4s_yw3JtXMWp6kFTYG1xIS2WLasvFNfrvdYo_lOe5nzfCd7rQhVJ9iK_WlPV-vzDXNJC5d1oms6ECQxXa3CGc2ngiL45PG8W6SeAmyq3MsFGASUMCJYFLVoEkw0YexuUd3TIA-Cx60nenSWQfOadKpJ8rb7LUOZe0LE1K-xIBhih8BPSGcrkUY3v7eMjlkyG9AfH3buceraEhYNK4ZX2KTwUQIfs-BPY0s-crgK2ioKOEKyzzNcL8yjaJaA5Ra3CG25pgYCjpXTOpSPsDDCK91FvANq6_mP8mMJIygVstJvfOUuVBaOO6_HLStevzFk7Sn4eHncYwldWQ_ihiU5SaR0Fv2txQ5CgaZlIjOuSQoaNtutj1E5eRNrVHP2_9sLvK8Ce0-1JVpUgnsjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی جایگاه پیکر مطهر رهبر شهید انقلاب در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447612" target="_blank">📅 17:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adf4cb623.mp4?token=LnubIs8PfUTga4FY0IoXuIFZZxGR4ICbb-VEbax-4Z0YMsB8-4OS77Ddd2_itysVFMXDd7-uJ3Xr01PFgXMI88wiZ-99i6AkHjNdCctTKidMmeLYMz67EIOAP4pM90yTLb7jTv0OyJ3wDyrSU1-GRfNfeahN0_2vB2vbvPnsD5C3CsUKI0VUmE1KCJvpthsZu6WvL0ZrdCKwJduOzTVbB4Paji3MsVAHXuqK7NhWsfu7hbU5Dx-vd_b0fISpFgqGDMRoqrrlUuvdM42Fs_8iLKS7mJEylVCS6xF-wEm16yCMHMomWYfQL-p7x6yD3T_nktrxp9hXjbjiByfRHA2qXRL9ZaeN3J6hwdPchKb5GbRuXvhtSnYdnrmCZmL02flaHa1EW52APnkrQZpKi_toRqvQCEMaBT85z2qN2wxdCyuiqCA08Rx_Nif1yxXMc2vaqh4jv25lV1Gnp2UUv_TZDqlCC456Yj12QL2yFvCW79kKwGHfBCX4PC_fsuGqszrFidBuCJtxssNRWUImgj7akrV-HsCHPma9StmZf2QZ1Qi8uL540D1W3HrMjFJys4UdezPHCQuG0rTSXZJnotnTHawYvV2d5iY9Nkbrg6GXBMVgELzdG6MTJBZLDoohI1c-A25PEg6_3w2OpHvSTaGeZ0cIGa8F6tLjlfdc2vrQ4js" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adf4cb623.mp4?token=LnubIs8PfUTga4FY0IoXuIFZZxGR4ICbb-VEbax-4Z0YMsB8-4OS77Ddd2_itysVFMXDd7-uJ3Xr01PFgXMI88wiZ-99i6AkHjNdCctTKidMmeLYMz67EIOAP4pM90yTLb7jTv0OyJ3wDyrSU1-GRfNfeahN0_2vB2vbvPnsD5C3CsUKI0VUmE1KCJvpthsZu6WvL0ZrdCKwJduOzTVbB4Paji3MsVAHXuqK7NhWsfu7hbU5Dx-vd_b0fISpFgqGDMRoqrrlUuvdM42Fs_8iLKS7mJEylVCS6xF-wEm16yCMHMomWYfQL-p7x6yD3T_nktrxp9hXjbjiByfRHA2qXRL9ZaeN3J6hwdPchKb5GbRuXvhtSnYdnrmCZmL02flaHa1EW52APnkrQZpKi_toRqvQCEMaBT85z2qN2wxdCyuiqCA08Rx_Nif1yxXMc2vaqh4jv25lV1Gnp2UUv_TZDqlCC456Yj12QL2yFvCW79kKwGHfBCX4PC_fsuGqszrFidBuCJtxssNRWUImgj7akrV-HsCHPma9StmZf2QZ1Qi8uL540D1W3HrMjFJys4UdezPHCQuG0rTSXZJnotnTHawYvV2d5iY9Nkbrg6GXBMVgELzdG6MTJBZLDoohI1c-A25PEg6_3w2OpHvSTaGeZ0cIGa8F6tLjlfdc2vrQ4js" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با  اهالی بازار کربلا در آستانه بدرقه آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447611" target="_blank">📅 17:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuAlyq3N9lHWqH8xPV1cT_KXzlQOrCo_M8oSpchY7kFJJx-_7MS7a3ltInIM_M0vD2SE8tB38qKXxrEkrNjc_nNbfpKefnlhuGlccJ5TmaU_XShAMFjYTuUxrkP4h2fMpUmDFXH_Y6qBZIYXpJwtmKd8RquetGngu9YYjZ62hTLGEIqppqaNtKAE3OLR6DSt2dwgYQwdh1pvVgp4jfPMYzzPQdBHXx7TUF_wYP0GG7onb8Lbgfnunx0qfZN01qtITpIzMKHvS-6RIDQJ50JDTkbTo6X9Baq3deI7ehO_KhVUu9yTr3GDV0iNJjFdQyxQgxQwwIyQ_OtUsU5TK1P2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQib_V58LoIcPpW4aarDBYnia5bHKwMYGSsnlBEaNfxSZpifEej9Tw_lRPdoPClA8Pvz_ec5o2xEBNvYVl3tBw05GLxD2Ysx3pfV5O3DyinrYOiom-EMVMgzg6Ld8St7sLHerPZb9o5IMbC-FOfJVJk_-ajGiKcQrXrI-fNayYXao6Dil015dkNPmOIyfN6BrptIMxvqyWsG4ZPenAiAzYpzsR8lCA1fHMIZz8jqiZWljTHAX_-u9Ld-toX46nbx6lTULvZOH0U_DNoPHoJXgKqWkyjgFtEvEDlrPkpTjms8yS7T6HV4ApETithJbFupLkZS9Ebe_wxzHp02SJ09xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzJDh9LpfCAPvnpEqg3ogT9OedvQNuO29a0UidajgVlnRh_nhFOawX4jrlwkB5spS1LT7DP251kUZ9pnMPkjW5E2pOotuxSDmguaW9X6aQFMoKjhufO3qBnvduQhZbGSg2fjPOQHdfr7boi8apCpHf1ujSCFGTtKKEDb8XBY1IpmPCxi7oaitUROvksYzuFqvqEw4stF7oPkY_EZOdqvMJzLyokWthxC3PjrTWh0w8PV8Su80HxEdL3nqaDANhL6mQuuvlow1UTF6RoutV6os1ANpVpAAcYIX7UUkpU09quc4FGdzVav5sF4mB0DnI8ovY24coBh2FwR4NqzvGLtxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTaNXl7YNbtNagGCtosddvZbHiU6TQ3sIymhq43TAN_QcHGUJXNaKFo2pneeqLg92VoHgmCP_fSqSq6ao58Jy6oePxkQhSANNk94ENX_UHR0QBkiOZT-mO17uovVlyhU2RIOWtxvbu4LMDss27__0scIXrgH2SQxoCusjrKW-n-5XNvuecv3QKFpw_v3Ot_vWr02QuK2KB9hhVRYGHScJ2MQ5e9LlNGqJa3m3MoDMB_62LJyZsw3_MMJYAFlcSgJff0qzx11N8O10PGLCx_LE1cb3mPPSor3sVmVla5Wuiucc6m6n2V9dCcMFyES-N0cyGnF2fosoG8yyxs1mEoC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTlEzfxkPuGDNNeVchqw8x4lmVpxo8CRryLmtZW7kSU0KS4fS5chV1Z_E6FoK4Q6YkSK-qnSU-SHDIqjQ-rSr0uutWj4RoV8zCIkF9llv4MpekAvl9bkh7v5mdpKa5ewUPQh8EjBFHzhBSLL-HmgKitlev4CYI4TlH74Bys_jvH1yAHRXpuRzrdPAn1Bk8uKxIQOvNwp6A0VdSUuEU7OWlyIHaYN24puq58oKGTZfVvtNiG1HBnrSQLhPG1CoCVGF-GSHd6RnAGRht62VBoySDD9QzZg43XbHYGJPll3Pj0OmfBxSGS48S5ll1_imPRh5S9G8FN08pn5QreOSavehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9M99hCwRuXgGM2faZDO7vWeiya2lSN1Ta1TLhF5rMEQCVSKJ50nVO7hnVOpqaZpSQlfzTO_OH25QPNBLrOloDWr1KTKJ4tWaMA3ycAQBWthUqBmdg3ArqAeHi4s32T_OaZ8pqQW6P0ohyTFDAL5LrIt1bEmv8LPFqd7g15xVTgil3cJt67E3xH_6D2QpV75Pn9XpXBOOFenO75XBJ2sOVHtrUHnKaQnxGOBB4aOV1wAX3AB29Mz505alE7mchVuiMAZnMNBD03-NrdkFfVbpeT0kiWis-vXC3jF2sMwE4FlVa8U7GlB3R_K2CFvo0emjgaBmHfyb9U4QvGgQRFARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ciC4hLUrJsEIIpXE3IliOs248prcTLCgcWEqrEi4hCZmu83ZTuGsdmCk-edZqsk3wgKsIQd4m-WwdVLDSWOSMadlq75HxsREx3vPi-bQqN95ibUAW2XA4fiJ_m6klF7RERybH7gk8Boz5AWnO5Zeo3eTRSFVEQLWDfmWsjXOc9NsKGuqhgIbE9TMozRn91dSiLQ3bKffp97eGsE7YqGMaCBp1bkWvt9HbEJwv5r8QOJR4UNV5-PHdr4JeFs7hQt1Ka3DrRyR9d6G1h5uZMTae-I2Iw_7TuUcX1wZaOKH7EDEoptDkSZ6BBwrbtE9c29iz5EHujou6KJQCRgqfwnnSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سوگواری جاماندگان از تشییع رهبر انقلاب در خرم‌آباد
عکس:
نگار ده دهی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447604" target="_blank">📅 17:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24be751d00.mp4?token=ME1L9-X1cilY5DwhW9Jpm9hk40rIQG2isbxg1ehJZ0AinSCQ5Behq2bhpN21LZBESsIapADzPcR7nGTDrWb8P-F_rDry-BFB6rT9EeJ65WScZT_E4xUCiToD0BtBRzZwR_eLOig0TNlrBVFL8TGvEIYTv58Rbk-a2regi-W7wNaU-XkqszogWktCZGOdKjpTRaWARDGo47bWifmcExGBjihpkrcNuQqCmHeQKFJ2GtLxnh5xxaAJJvfZADn-tKdjjxOCkC4A55T7wGd38JLPQAxQ-lgwUoV73VqkV7Mx3wRPQcXbQAriW4PPm5tGMhuSipSCf79hS_QYD9yYfe8MVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24be751d00.mp4?token=ME1L9-X1cilY5DwhW9Jpm9hk40rIQG2isbxg1ehJZ0AinSCQ5Behq2bhpN21LZBESsIapADzPcR7nGTDrWb8P-F_rDry-BFB6rT9EeJ65WScZT_E4xUCiToD0BtBRzZwR_eLOig0TNlrBVFL8TGvEIYTv58Rbk-a2regi-W7wNaU-XkqszogWktCZGOdKjpTRaWARDGo47bWifmcExGBjihpkrcNuQqCmHeQKFJ2GtLxnh5xxaAJJvfZADn-tKdjjxOCkC4A55T7wGd38JLPQAxQ-lgwUoV73VqkV7Mx3wRPQcXbQAriW4PPm5tGMhuSipSCf79hS_QYD9yYfe8MVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: در راه رسیدن به استقلال و آزادی نباید هیچ‌گونه ترس و هراسی از دشمنان به دل راه دهیم
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447603" target="_blank">📅 17:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAGix_A9JJtL_hI4DB2kZlQfuGFc5YjTV0ZqnLpqVDZohB3xRAZtf3yPVQAlYDDbJM5woojvnhmp62h5LGDyhIq0egfSVJZT-5k1PWs4cLdocFZIDrv2Em8vRTu5eSlfgd_GXY6yXF-mteERq4fRYj-Hbj6ISc5Q8_2tI5xzLfwX6RuRxqOposAfhkJepKiWBK8YNTjK21D-SquEmWwWvJCRwz-dmr7a0vGd539_SMsAgX-QAAgOwc31JGANatzZ1L4zH-Noc5A1PZkcBPuVUQ4XMCGwP1Piy5vbaDzId-o7GEBupcltwMxI5R7NTOJVqz450VZrDFwFCjsyaialow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخواست نتانیاهو از ترامپ: ترکیه نباید به اف-۳۵ دست پیدا کند
🔹
نتانیاهو در گفت‌وگو با شبکهٔ فاکس نیوز، ترکیه را «رژیمی آلوده به اخوان‌المسلمین» خواند و گفت به‌نظر من نباید اف‑۳۵ یا موتور برای جنگنده‌هایشان در اختیار آن‌ها گذاشت.
🔹
ترامپ ماه پیش تلویحا موافقت خود را با فروش موتورهای جنگندهٔ اف۱۱۰ به ترکیه و بازگرداندن این کشور به برنامهٔ جنگنده‌های اف‑۳۵ اعلام کرده بود.
🔹
نتانیاهو مدعی شد که چنین اقدامی موازنه قدرت در خاورمیانه را بر هم می‌زند؛ توازنی که به ادعای او، با برتری هوایی اسرائیل و همچنین موقعیت آمریکا در خاورمیانه تضمین می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447602" target="_blank">📅 17:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447601">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee2d813eb.mp4?token=ved1ib29lWWhMA5ALQhU0C07ZQiFfZnIp75Uq1i_rUUuwMaLxuHRRiRAKQgDdWz7K1eaOC10KUJAnbRIYSfVUgqG-4Ognfa_LFUooUwwSky8BmgPDq92j2YCBqti3kEd9hocN0ZnGbBg0igTv4R4_CRFcbfPTQcKNzAprUjhPSlbQnZfYB9HYklFadQbnEioqi22-hODbLJTjDj3QbesOMN-r2GLSwA8Q7FVpjjnM9f8ZiIa8pA33yB_9NCSB16BESjmjqApYSnK69cawIyor9eUm58GWT4VbXl25GAosWvb66KXiRGRqmSVCQhTSEFI1oIeZ9ZmnNbjJHkFJmn1DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee2d813eb.mp4?token=ved1ib29lWWhMA5ALQhU0C07ZQiFfZnIp75Uq1i_rUUuwMaLxuHRRiRAKQgDdWz7K1eaOC10KUJAnbRIYSfVUgqG-4Ognfa_LFUooUwwSky8BmgPDq92j2YCBqti3kEd9hocN0ZnGbBg0igTv4R4_CRFcbfPTQcKNzAprUjhPSlbQnZfYB9HYklFadQbnEioqi22-hODbLJTjDj3QbesOMN-r2GLSwA8Q7FVpjjnM9f8ZiIa8pA33yB_9NCSB16BESjmjqApYSnK69cawIyor9eUm58GWT4VbXl25GAosWvb66KXiRGRqmSVCQhTSEFI1oIeZ9ZmnNbjJHkFJmn1DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر باقری لنکرانی، مشاور پزشکی رهبر شهید: تنها کسی که در سال ۱۳۵۸، در شرایطی که دانشگاه‌ها جولانگاه گروه‌های ضدانقلاب بود، شهامت حضور و گفت‌وگو با دانشجویان را داشت، رهبر شهید بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447601" target="_blank">📅 17:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447600">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvJSobr74M4u6gzMsYs_yIgAlONTyV8StazF4EBHiGwvlSaZAEajFk-6n2Se_KCKTTxqaRpp4Iql-raZ49co1KngPPCoATjgF4bj1j1cJPxQqAn4aQpD5RP1cP_ZzmihsDV1D8-Fh1lXLtWxXlPDfVr_yKLHanAcrovcfYeppE1vxz0uhA6tFrWV5GhfBuynCj-akBSmj8G6z0BFbFp9cNfPCRiD2f1nCJA8Ded-grjIFaYHq9Pw07RB-ylmf3cVPty3DCcF5QooLxAS1Y3E_DBQ-2yLpyUAc-KcwVjaywY99-Bb0i793aS3sW39yAGCpzDqZN2OEa0cdUwaYY0EsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام دفاعی پیشین انگلیس: ایران قدرتمندتر شده است
🔹
توبیاس الوود: ترامپ هیچ استراتژی نداشت؛ صرفاً یک نمایش قدرت نظامی در مقیاس عظیم بود اما در نهایت، امروز می‌بینیم که ایران، به‌نوعی، قدرتمندتر از قبل از ورود آمریکا شده است.
🔹
ترامپ هیچ جنگی را با ایران نبرده است. حکومت همچنان سر جایش است، موشک‌های دوربرد همچنان عملیاتی هستند، پهپادهای شاهد و مابقی تجهیزات هم همین‌طور. و همان‌طور که می‌دانیم، ایران کنترل کامل بر تنگهٔ هرمز را در اختیار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447600" target="_blank">📅 17:24 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
