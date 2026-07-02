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
<img src="https://cdn4.telesco.pe/file/Z29MtDzD8kuVCuJ3wbN2RoolRIKGskGCZj8Ozjv9soqkW7eQTKkPEtj3G4r5i_rhUMHNL0Quz-gB5vRP2CG3eHoLIaLgFeLAMOisJzoucDBA2Y_KQKr9vaKKYF4IrXWN9HIEn3EVBhhbKh9QJ5DzhG2fr40VNv3ghKi020_B_2Ysl0SX11ngWVn0_j8dEejfC9u5PeHj_Q2GPXx36J3nY8W5An0KLRUtuTgdtPBh4Z1i4Rs76B0uI0JpSfbKpdgQ-jB2HfX7c4iQruq03uMe3fujVmsBb8R6BOoDZnB-BY7iMyNfPXp_gEPOw58hsB-MyQKCBpRAHqTzmOBqpBQR_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 214K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 20:14:51</div>
<hr>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMuVB-8aYZWdmmtfl53F9taUrzrq4PCcWd0lYeAmSOfXVcopGPSo4K2P2p4lYWgWF93k1DLnykC8-SCSGhXqshJRUr8QIx6qBCgESVWoY28VsXAcTiAO9o-jh4szirza1fTPH15WIthedVhONyamvySvMCLIndKMRqfi1f_Fg3Gqlm2mxlF_WwhlkQkCFFOEej1tDWJSQPs1VXNBMAyk1gk1FWJ9iEQ_n6I5FZWMjPgiw3dEIM5fxzROGslmjUApkUFwwhU3G6SfV6L4dzvaMAkfz2-M90aZnroJj1-6grArvuKp4RQJxnJwORxVIM4NCjrdTslklYOO4bc07cXKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwIQveqeG1Hc_7YajuUyMYssWCsnuqcVv5IkF8p39qrQXZrke3cOrWsnfjwcMMie6YGj_L4KxB6BeYKr6HACHokWst4fA8le7Z1CmVTa1Zi-volX84JIwga1rk9oo4QvsMCXAOdAyJJw_dsadGt81TqC3VE-iSnoV2QZVDiuY6QOh9BsIJcVZ7pKs82d_9zgqNFBxe2fUE0gXJdl0X6t5s3k1BaHrWgajfb9VlHHvuUuxa3DmCaiAYCedLGDIEjh4xsLCsgl8KRiQjljOUT8KBe5PFLvJsjC9bvjmrGxzMwySIwNOVbHNh6tqMPZOS6Z5wUh3UuOQjsVDIgki48IXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=nKHqSo7U5wdMvElN0G4O45aPWh93xvoe7zo3HEZzJfrvAJo__opdPXeafZASIrMt_0WgLgGwqWJuFdEc_q-k1hixkbUt-ZDlTrmvf1cKQ_SafV4UKE2tbl3J-_JfyFmhnK7nuiYqqVfDRPhbWvEKZ0Kn1hC3Id2_ynD-F8Cyu1CgWzey5gftAoQUJr9Tx0WN-oPmbAwJW42OspWuDeQwq5d4lxTBjVAS7_5uWwbSchj4DAJTdRkdUzUEztfxuPx_jlWMZ-QmW91UBNxhV8uoMylGKQN0F9uM8VerPqCyo1rLbBthPaoBQKoMOGu4GaILdPJncsmV3ZIwCNWeEbjEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=nKHqSo7U5wdMvElN0G4O45aPWh93xvoe7zo3HEZzJfrvAJo__opdPXeafZASIrMt_0WgLgGwqWJuFdEc_q-k1hixkbUt-ZDlTrmvf1cKQ_SafV4UKE2tbl3J-_JfyFmhnK7nuiYqqVfDRPhbWvEKZ0Kn1hC3Id2_ynD-F8Cyu1CgWzey5gftAoQUJr9Tx0WN-oPmbAwJW42OspWuDeQwq5d4lxTBjVAS7_5uWwbSchj4DAJTdRkdUzUEztfxuPx_jlWMZ-QmW91UBNxhV8uoMylGKQN0F9uM8VerPqCyo1rLbBthPaoBQKoMOGu4GaILdPJncsmV3ZIwCNWeEbjEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=rt0NUHGLv8I0re6r7OQMmfw9lTLl7_mkr1JOC7T-vrzuOSpVvHGvh2GOMny0LauQdbaT-IhfSLCHPi5viBgR7defWenSc9du9lm4TWVmqrA76j6sWMLkdpLACs97JBUqQB0S7bxue-JfbG2RWdKAIAhzDw_BHvJJ3DzVmPfXL9fd_F2_Twp0iv4TKvOsUO2t2bJlFr1WCVBdq7vlMzUw7jEsBLPp1PJ6s0mfwS8hDC_uJC3FrMr3H5YBFpAa3R4iFQPbn1IinAKpsnZjyOJ2KFnGcf6PWKsBZDEOdinsG_c0Zn7RtCmQEs49CFAKQegTN80xG-16jdLuAooRBWlOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=rt0NUHGLv8I0re6r7OQMmfw9lTLl7_mkr1JOC7T-vrzuOSpVvHGvh2GOMny0LauQdbaT-IhfSLCHPi5viBgR7defWenSc9du9lm4TWVmqrA76j6sWMLkdpLACs97JBUqQB0S7bxue-JfbG2RWdKAIAhzDw_BHvJJ3DzVmPfXL9fd_F2_Twp0iv4TKvOsUO2t2bJlFr1WCVBdq7vlMzUw7jEsBLPp1PJ6s0mfwS8hDC_uJC3FrMr3H5YBFpAa3R4iFQPbn1IinAKpsnZjyOJ2KFnGcf6PWKsBZDEOdinsG_c0Zn7RtCmQEs49CFAKQegTN80xG-16jdLuAooRBWlOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gzmt4xOIlxonsa4r9jH5c5bhbN5EqPpnD1_q-kbGT7wFk4wVIUu94LUpjSPJ_jKZ11mpEOcjAcRZYp5SL-znPT1ceE625rkSksYGhl3tBXF9626VJpxyGK6VKIllUhQfqF4fuQXIia58bOWtLsngDQY_qufnue7MAJGVBbl82-nVlBsuqLZBGiZ3k61cqX6asZYHDHeAF-fCWGxH8DoVWD2zEEFCDl3c2AuGi9pv5AafpodvIecztbsF0ycqlyzl8xRwDr571Z-lr6WFTXBflpp-x_niXiI-6hSrod8lrrzGq11LTJnfUt4Vcf7QudSgyfIQNrTlr_TW0uvXHKw11A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gzmt4xOIlxonsa4r9jH5c5bhbN5EqPpnD1_q-kbGT7wFk4wVIUu94LUpjSPJ_jKZ11mpEOcjAcRZYp5SL-znPT1ceE625rkSksYGhl3tBXF9626VJpxyGK6VKIllUhQfqF4fuQXIia58bOWtLsngDQY_qufnue7MAJGVBbl82-nVlBsuqLZBGiZ3k61cqX6asZYHDHeAF-fCWGxH8DoVWD2zEEFCDl3c2AuGi9pv5AafpodvIecztbsF0ycqlyzl8xRwDr571Z-lr6WFTXBflpp-x_niXiI-6hSrod8lrrzGq11LTJnfUt4Vcf7QudSgyfIQNrTlr_TW0uvXHKw11A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnhCD1ih_b0XXLpvBDIAZnB4fDiC5H8SeARPt5sTfjdSnyjh7c8SvaS22amE14lYKRALdiB1LUyndlGc7EIoSdodyk-Ix0JYYpNSTu2ESI-dyxzrG0qyzYLicA-oCr0CC2xCJ_4kEMn-oZIlH_rHa6SziBupIydZLbCPDGrTxq9e0npmBMyC-7bwNsDitoSKjVyF4qh3rNn4wd5sck8u5MRal18jsX20GRJij1ZXaYSXY4d2R4wqI2Qws0-PoAm6gdomI-mkgiGmVz2gCk-hCZaUiWFNBB9d4JBTsrXSTAVvsugLS0NYl_CdD4VS8tQuUzsNkAIL5fsjpqvLJVSu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqTkhnTZ41JnmVdIDMm5Y45F1mYe3vtoy7AaKuh7n_JVqeJ7iEUHMEvfLeD__GXNy7ulBHagzDoRqtRbWH_z2cN6XYbGJF-h0Eib26G4Z4lVYKYvMHOb4rdT6weZwNiN82AjruA_anoP9PTaKJAOmBQ5OAAop6liPSFC_hmKca35FpH7fq-m4STugYe7dMhxsOheTV4_tQaXnxiUJmsj9kcQHkVVnq8_o_iwrFXiVf_lbBxwY-6d1ILamDKKChAIBpfMkP6WN--Zeofe6qDsqWVnBaeUnlB1teM_2JP2xevHBpRe-LDIT1QGv_H7Sif_eYUNPMn-Ig_8ZQ8Ot6XNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUSPj4vuyhkxsW-C7YOxTIkqqMTxNracE_iHXbUY6kd0bM1Ml0qVRD8ekCVyROl6OsrG45gJFCwbRUTGXMUClNgTs2ILMYPjqP4g-Y70JOiZ8sDOJPfGoeUCP76Xa46oFxdEfEyq3rdWWMPX9wA4NgTlYvDMwJtTQh2snM9mwmiB6_TJWX6vf9pjqNIQZzV3CVdL7xarFz4BmX-0huY0lEH7RAHoiK6u3uu8yPkEzitgBUjeeOc7sbwARb60WcV-oYSwHCkKAHzh86SI7cCWmRdKakXOuKGsEmLEasapscfBmUvgnhE_hG19aZ9Fav0VpRKYtFN_F6Y--3aNb7rp8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Pt9pv8uvn9x4qAHmPdMCt0p5x_h-mVk_zwSNyT16xjXRkCewNzEdJ6D9Ny6IZjczopqmqtFonUiI_KFwqe7IFynHRXBuAAf4D1bd9f-AXji_FuuTF5CX3kRq1q-Z9Dv8LO436JkZ54m-jqA9vOrIb8WBeaBCOWzj00OPlxLEGw0NWk9bw6LcKEpbMeBJAo0Lxzs0CcssO5so-flZ5zLahLHWraqr_0TOdNvQ9fvrA0jBz5A4GWG9UCR9HhVyCVxiTA_FQKJD4Md_yFgjdO-IH5i2dVJYlh8vw_iK5GQ2g86nAIx0x1Zb_weaRCVSMVOQ_SPoKqZziBmUcnNJ0k0SNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Pt9pv8uvn9x4qAHmPdMCt0p5x_h-mVk_zwSNyT16xjXRkCewNzEdJ6D9Ny6IZjczopqmqtFonUiI_KFwqe7IFynHRXBuAAf4D1bd9f-AXji_FuuTF5CX3kRq1q-Z9Dv8LO436JkZ54m-jqA9vOrIb8WBeaBCOWzj00OPlxLEGw0NWk9bw6LcKEpbMeBJAo0Lxzs0CcssO5so-flZ5zLahLHWraqr_0TOdNvQ9fvrA0jBz5A4GWG9UCR9HhVyCVxiTA_FQKJD4Md_yFgjdO-IH5i2dVJYlh8vw_iK5GQ2g86nAIx0x1Zb_weaRCVSMVOQ_SPoKqZziBmUcnNJ0k0SNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=oAFdhcQR-W6EoxvYh6HHto7yMn6iaO35qobyu_qUA7onTOvslggprGLIXFdzrUhdZj_irVHIH7irFB3hRLYmV2MIWv5B3nI9S2RTg4Z5asEAX2gXuYw71nw6dxykIX7o9fhYsw-Crt3XbEqtv6mAfSWS0XKfhQT6mKXzQawpt3kuJPdwomIJfXL8dOwAuFUCQDSzvNPoYHfGzKq8lovY69fVXQGCPUpO-0CIEJF2KJp_UIYHDo39H5C02aG8MvDkQ49r916BfFXJ0lMBIPt7leCblmhvPm84IGCAxhAdOTIVe1pT6_kRHh6db9zNlZ201LWystgfVMitglii2PEtIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=oAFdhcQR-W6EoxvYh6HHto7yMn6iaO35qobyu_qUA7onTOvslggprGLIXFdzrUhdZj_irVHIH7irFB3hRLYmV2MIWv5B3nI9S2RTg4Z5asEAX2gXuYw71nw6dxykIX7o9fhYsw-Crt3XbEqtv6mAfSWS0XKfhQT6mKXzQawpt3kuJPdwomIJfXL8dOwAuFUCQDSzvNPoYHfGzKq8lovY69fVXQGCPUpO-0CIEJF2KJp_UIYHDo39H5C02aG8MvDkQ49r916BfFXJ0lMBIPt7leCblmhvPm84IGCAxhAdOTIVe1pT6_kRHh6db9zNlZ201LWystgfVMitglii2PEtIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Kl9HAPEDGqhINFhq4GTfEtJo7k21SaGHgFWQ6k93-HPNrKpWp_vG4tRaIsrHsAOpRBxN3jzbAei2q9y2C29L-dmb8skIVgQWjP5TnkR8Vi-xznKbem1o5b-7nWRqi5nZ8A5SSxkdB27HfM3gYptLGUTpY8e2M-TBjmb8HqftJmJNy3xC8WC8v47qTX7kM4j7aTyjFtcmRYDC5OCtJj0kBwI-x_MBXRaxhTCP8EDeaAdN2-Aa7xwezvXEOgWoA_yQGyRCeJVvgLbovsXtKTsn28iddpCE-FMurtxm4kRc6Y2lqEmKwzzxe5HT_ZWJ9Vzxld_lJjqrTcbtd_jOsAi6tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Kl9HAPEDGqhINFhq4GTfEtJo7k21SaGHgFWQ6k93-HPNrKpWp_vG4tRaIsrHsAOpRBxN3jzbAei2q9y2C29L-dmb8skIVgQWjP5TnkR8Vi-xznKbem1o5b-7nWRqi5nZ8A5SSxkdB27HfM3gYptLGUTpY8e2M-TBjmb8HqftJmJNy3xC8WC8v47qTX7kM4j7aTyjFtcmRYDC5OCtJj0kBwI-x_MBXRaxhTCP8EDeaAdN2-Aa7xwezvXEOgWoA_yQGyRCeJVvgLbovsXtKTsn28iddpCE-FMurtxm4kRc6Y2lqEmKwzzxe5HT_ZWJ9Vzxld_lJjqrTcbtd_jOsAi6tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=pIv9bjCEaqNjU2Bv6mAd9tiWNGfh2XbasiwmrfBWBT0og7PkLLLfYy2Exq7I9DOGQFBbSFpX-GFkMArsfad-EA0tKVHAJw1-R5t-4yDeQGICHQH0yaQvihRbIPiwTcvqFxZxLfKJ8A6EDPaOixzuSVa_LB8n8JuTqpRowx0xxRYXz3nWnxms882Ms_625QfNYLuerOeyLzO37orpCwjof6UZZJCI_Yw7bc0Dto9wDx8o59IQIOSsdfP6GiJX9c3_SCyaL0MB_uCdd2kn07Slqim8uNJJY7AUvX1eq8JeKz2UTqvOYnXNTtf1XmRwetkozjX4vUA-iiZgiV1EcMQI7Ba0ePa7KuJwXpwqpjjtNEDt2zkzAeNwkEA62GYpR2PmZsI8Yq4lYgIGBH-OAPFJI9PESkt4PqBzPWLsTiAKR1Ob7M2FOq9TKMMFkJr-tO3tX7j3AIND_svuIF_ay7RwAkpFUu6LyvRu687qwyH3yf0DTGbfda1kY0E3OCZyQjbjKzneWIJZdLulNvTxBFEdlLmu2UUaOBr0MFIglaT4bBViboUiZrb2Nm4EvviPuOR2i3T45eNd83BjaVIHavcAz3bnvrYEDKeovw8X7E_TJzF-uklbtTNf06w7xxZ-RDQUYzag50qGGVdjY1kVvZ1v3bksBR7HIBTMvCfHB1ELcRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=pIv9bjCEaqNjU2Bv6mAd9tiWNGfh2XbasiwmrfBWBT0og7PkLLLfYy2Exq7I9DOGQFBbSFpX-GFkMArsfad-EA0tKVHAJw1-R5t-4yDeQGICHQH0yaQvihRbIPiwTcvqFxZxLfKJ8A6EDPaOixzuSVa_LB8n8JuTqpRowx0xxRYXz3nWnxms882Ms_625QfNYLuerOeyLzO37orpCwjof6UZZJCI_Yw7bc0Dto9wDx8o59IQIOSsdfP6GiJX9c3_SCyaL0MB_uCdd2kn07Slqim8uNJJY7AUvX1eq8JeKz2UTqvOYnXNTtf1XmRwetkozjX4vUA-iiZgiV1EcMQI7Ba0ePa7KuJwXpwqpjjtNEDt2zkzAeNwkEA62GYpR2PmZsI8Yq4lYgIGBH-OAPFJI9PESkt4PqBzPWLsTiAKR1Ob7M2FOq9TKMMFkJr-tO3tX7j3AIND_svuIF_ay7RwAkpFUu6LyvRu687qwyH3yf0DTGbfda1kY0E3OCZyQjbjKzneWIJZdLulNvTxBFEdlLmu2UUaOBr0MFIglaT4bBViboUiZrb2Nm4EvviPuOR2i3T45eNd83BjaVIHavcAz3bnvrYEDKeovw8X7E_TJzF-uklbtTNf06w7xxZ-RDQUYzag50qGGVdjY1kVvZ1v3bksBR7HIBTMvCfHB1ELcRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s37eul_rWWdfDrZVmqFUsAh1dKNq9i0Uc_p1JU6Lk7eeTu9gZYoNLvX1AueoUDmEjfJpnWaycW9F29th1WUNxfEKeoBDFwpv6nqEfOv1K8XF8vHVNCJjl-oo0gC_Lk18b5K1rq02xPVL38jywoKLDmdIUfMwzxrycGpIPvumW-s3OjpIc4c5vyYv2-NzfazEh3tzcKPXuIsCjOiRiiqJG-s7guVS75UNAVpQM7MEnBGe-dFwLiS16hSR7JlyIXcU5GlAe9KJ8bKeDvTaaUIFF6eYRJRL419GjaWzdviQ8R6iq-E5I3BDGMVPy9PjJRemIYuifUAkXwGwc7D9IGGLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH5MCve6-VJD_NCcpwXir5hyjGZCFnRqq1l2ORZM0pnyiFrZgg-DMW8V9gRPbWQTtbsu-WBD9zFsMd2RndOnd31yse-hyQczrEHDrb-rodx1_kV-1ztOT2dl_tftsT-Lxl0PA0Ht95sJQFv2we-NmP3nUFpS8Yc-1ScD40A-R9C3imAgdTyjPiIWSNmABMU1GGQh-DOxjUTyTHSKf_FNCiLYzsyeZnihTBIyb6WAChMlr9wwazIGziQ6m05UmEH3K3CZ83wCtIEj-z6O1DHNt2Ijy53cngu3zJDni5REY77KX8wGgK44RKTK923xyjebhXxNt300fN55Hpp6I5oD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=MqEyil9GiYDpg-MAX5XVD2mGZFZ2P7LNhMgzk2yySPsnfPBP8uAjZtJrYtgUfUHwwJy8PLSVtGnWawtQ85Gm6aHXqu0kI-P4hTpy5QGjAcLrHjuLbfyonVt9q6iVdaioV9Q-KFog47FojNf4PqauaqILwh-LSrptSS8fb8PQFW0zhnhsrcYVYNJ-84SdXvg_KU5sFAuAw1K8UlQJdXER1XEnOXFyjvDUcXY9cikELBgj66Z9shFdE0pbTDsReNGo1HKaloJSe7y_yohvWWaBCxcPfvetYHfj4ZGrF23RmC-tuY9XhtYFkpOLMz3aXcKLFQrkr5dDmyRAR0dwUyabFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=MqEyil9GiYDpg-MAX5XVD2mGZFZ2P7LNhMgzk2yySPsnfPBP8uAjZtJrYtgUfUHwwJy8PLSVtGnWawtQ85Gm6aHXqu0kI-P4hTpy5QGjAcLrHjuLbfyonVt9q6iVdaioV9Q-KFog47FojNf4PqauaqILwh-LSrptSS8fb8PQFW0zhnhsrcYVYNJ-84SdXvg_KU5sFAuAw1K8UlQJdXER1XEnOXFyjvDUcXY9cikELBgj66Z9shFdE0pbTDsReNGo1HKaloJSe7y_yohvWWaBCxcPfvetYHfj4ZGrF23RmC-tuY9XhtYFkpOLMz3aXcKLFQrkr5dDmyRAR0dwUyabFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=Uo4jEnyRDn7DS2O9V_qwaQTmqmAcaEgUV8oqE_x4BbMkj7LnDRxd58bvQTbytSPuWyG7NoWaMGsVcGPFaglNFFsIm8RZiIfuw55iwNznMHdVIabAcuF89hLwA0ZFHmvsXKcytlW-Ctg3yGsQ3tROioCNc7rK_9I8XIKGArteajz19BRL2kKaEP3s2XC9KUdz0SUK6DHoDtUjEwVBuKTfaZd4MOErKQpPVvhTfZNKkYR4214NE8OMix8Wke46ajHU_DqwAeXENEI8zj-g_3n55M-dfEPwvbvhE6VW4J_-SLlh1AjJko5bQvL-CDl51ED0Wr7cIxUevIKL9LCa9ANnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=Uo4jEnyRDn7DS2O9V_qwaQTmqmAcaEgUV8oqE_x4BbMkj7LnDRxd58bvQTbytSPuWyG7NoWaMGsVcGPFaglNFFsIm8RZiIfuw55iwNznMHdVIabAcuF89hLwA0ZFHmvsXKcytlW-Ctg3yGsQ3tROioCNc7rK_9I8XIKGArteajz19BRL2kKaEP3s2XC9KUdz0SUK6DHoDtUjEwVBuKTfaZd4MOErKQpPVvhTfZNKkYR4214NE8OMix8Wke46ajHU_DqwAeXENEI8zj-g_3n55M-dfEPwvbvhE6VW4J_-SLlh1AjJko5bQvL-CDl51ED0Wr7cIxUevIKL9LCa9ANnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=uWcKFGmZyagnnRpTNBZQ7wqewQoAMv04hba5W_oXjrfS5IR5n3kOQNRti-xFy6zZsvjweKHt2im0cTTUja-7RSJSaGjHP84ppV6LTWwSgwwvG1rsUuBGvXmRAeV6o5bKkO_jdBPImmHfkiDc4DQ8nsr4LGEEImt8gP60PCz2lY2xTtdOGMhKoBXwI56DNNBWKoRr8D0GcsFpeyhxU_CbzTBe7Q1hc2i3gGIa6LhYdeStmKvMgv5BbIHLEHNSXMfpVYIKg47euPYjV8BohSu9N7qSj2kPzgdER0Ts8z8tLTVPgt4qRu-I_ru8_P7gtQ_s2hmNgyd5gNXMvwmqvSUHxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=uWcKFGmZyagnnRpTNBZQ7wqewQoAMv04hba5W_oXjrfS5IR5n3kOQNRti-xFy6zZsvjweKHt2im0cTTUja-7RSJSaGjHP84ppV6LTWwSgwwvG1rsUuBGvXmRAeV6o5bKkO_jdBPImmHfkiDc4DQ8nsr4LGEEImt8gP60PCz2lY2xTtdOGMhKoBXwI56DNNBWKoRr8D0GcsFpeyhxU_CbzTBe7Q1hc2i3gGIa6LhYdeStmKvMgv5BbIHLEHNSXMfpVYIKg47euPYjV8BohSu9N7qSj2kPzgdER0Ts8z8tLTVPgt4qRu-I_ru8_P7gtQ_s2hmNgyd5gNXMvwmqvSUHxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m880LGFQ7ETwVsVWyYdn6CwjoXnzDJYiBh_ZQQpiXTyKdHRy4LcA-IFD8J77EjiouuNXXV4xt1IJDkTWXUAP_7etjxzwrPmpGSFyS8GaqnQh2mWgpTaL-aucmXXHzbE-M1zAIxNjm4fysUYnRX8DYqZELuaa48J1Vv-_BCWuZw5bAYvoqmzLhr_x3kgACTxK_O-5zVud6vrZWNahgJr-EbclUKMJrRcB2FUEcMXvo070WpHZ6awizS7uQlv1UEFNE8iVr_ZtXorvJNf2mMAkL4KCjaHUHx8zQBn6hNruV7vd1_U4ZwOt9ktlBUBq_ky68clWo7jTKCUnhsMRsU7C7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=QbWGQoXxrJH9XmmL5laEhZK3R1BUlo22n3In9H2s0XbEKepGOKH1o7x88H3_vSjezkb7N3LKLSQLN1nU80d9y1zdcm-X-egBnKJvOfyIjWJ-0PyxikGE6mUMyWgIcjKBwwaB0tw5nFOncYrgYN1vm6--CSggGsDMrRAkZ8gVPI8859FUGPb-fS_wSZ33jUOgwIoPxJfFoYm0Xs0oKeiJqOI77k8wRx9e3qhTdM8Urqxy7QIXzGEaNFBeTEIIpB9hstNjfFdPN7rhlhABEfeEkhmGg0htvIfR27lppPyxBvodGybdxZFUdCg2HXXdiWrJUhAq4SBoWCy-sBYpFbfmeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=QbWGQoXxrJH9XmmL5laEhZK3R1BUlo22n3In9H2s0XbEKepGOKH1o7x88H3_vSjezkb7N3LKLSQLN1nU80d9y1zdcm-X-egBnKJvOfyIjWJ-0PyxikGE6mUMyWgIcjKBwwaB0tw5nFOncYrgYN1vm6--CSggGsDMrRAkZ8gVPI8859FUGPb-fS_wSZ33jUOgwIoPxJfFoYm0Xs0oKeiJqOI77k8wRx9e3qhTdM8Urqxy7QIXzGEaNFBeTEIIpB9hstNjfFdPN7rhlhABEfeEkhmGg0htvIfR27lppPyxBvodGybdxZFUdCg2HXXdiWrJUhAq4SBoWCy-sBYpFbfmeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=nbmEACrk60bARkddpqkExgCR29y10IwpdpT9ltq8Wfh_I3rqGtYuh1rOI-B8Mj-KUDrJhp_t92AzZWfCjjPL0xXAdKeCkKk63fkXL-LWC-pfTgBlryg91g8qCvKgK6-3fYo1h6ql-0MYKCxx12dDg-8uy8Lf2c5hL36DWCkttWinCIVvUIWxEe40F6FgneMcNEX_HRAzdh4e1lQBymFPnhRqBEsN2JpENIu0flLQ2IeZRcUtfxU3GTF6OCgvtF58cqW6GOru3kMOdCAoKg8QgfaCtCJHiiujeK1CeNDfTGdrydAvk6S-z73b_peC5s9o36V8turhMPfRTFQwzkxBPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=nbmEACrk60bARkddpqkExgCR29y10IwpdpT9ltq8Wfh_I3rqGtYuh1rOI-B8Mj-KUDrJhp_t92AzZWfCjjPL0xXAdKeCkKk63fkXL-LWC-pfTgBlryg91g8qCvKgK6-3fYo1h6ql-0MYKCxx12dDg-8uy8Lf2c5hL36DWCkttWinCIVvUIWxEe40F6FgneMcNEX_HRAzdh4e1lQBymFPnhRqBEsN2JpENIu0flLQ2IeZRcUtfxU3GTF6OCgvtF58cqW6GOru3kMOdCAoKg8QgfaCtCJHiiujeK1CeNDfTGdrydAvk6S-z73b_peC5s9o36V8turhMPfRTFQwzkxBPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=hi8musDHcSWuTiot3T56ZSdEzUF2McNu4FAkjprlUrPqgwJhkYZm9Tq2eKxq2EKpNL76HFZ6hImEX9NaBrNO5uANfRn6234TN2DNwW1R0HF0MDk98eIlsybw3C0ceDjqoj5nArq6rEzZZjTIoLfLuMgU91BN_ZT3oA7ngQL0nGQSbbrJw86vcRsTZ0aaekv_Pwi-NQHzOI86pncQ5pRT3PmW7LIm7MtshoyjWA6xApshjfPg3wU2hfiO0nJzVd5hZ8ZwV7KHfc_tRWF7TerK9dZ4qY_pgmCe4ohhJSeWtSwYwcmhEKrQnoiHCV2QRQLyaGJfpXbkKopmWEtKXUfBrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=hi8musDHcSWuTiot3T56ZSdEzUF2McNu4FAkjprlUrPqgwJhkYZm9Tq2eKxq2EKpNL76HFZ6hImEX9NaBrNO5uANfRn6234TN2DNwW1R0HF0MDk98eIlsybw3C0ceDjqoj5nArq6rEzZZjTIoLfLuMgU91BN_ZT3oA7ngQL0nGQSbbrJw86vcRsTZ0aaekv_Pwi-NQHzOI86pncQ5pRT3PmW7LIm7MtshoyjWA6xApshjfPg3wU2hfiO0nJzVd5hZ8ZwV7KHfc_tRWF7TerK9dZ4qY_pgmCe4ohhJSeWtSwYwcmhEKrQnoiHCV2QRQLyaGJfpXbkKopmWEtKXUfBrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=q15ReI4wGB0e6R3fwBmN0oZj69hR-1fzcnn966CJNQfBFjuhjjC8cUJGTydi7lbOQTX5L_fHRgEzuA3t_obtZfV9NF9csZOV_qRndwGfNEmTvP6zffaYSj50iY8Vix_iKaEdpgcTEstdXCuPS-EnMBVC67qcdnzxo7z2ikY-yFNApKse46aDiimzF5Y8SIPMbUg_6zLFw4w1OxAFPXnPRrM0gOj0pGJd5sU-8TlSgD7j5leWsMHpHOt2xjLtzC1nFfG1UxLPTTbKHqCYzWBBfhxphDX_UXna-P-0ZmVIm5n1ZVh1UUYLTekcLn6G0tHGPZBRtY81GtV1oeM-BwCSoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=q15ReI4wGB0e6R3fwBmN0oZj69hR-1fzcnn966CJNQfBFjuhjjC8cUJGTydi7lbOQTX5L_fHRgEzuA3t_obtZfV9NF9csZOV_qRndwGfNEmTvP6zffaYSj50iY8Vix_iKaEdpgcTEstdXCuPS-EnMBVC67qcdnzxo7z2ikY-yFNApKse46aDiimzF5Y8SIPMbUg_6zLFw4w1OxAFPXnPRrM0gOj0pGJd5sU-8TlSgD7j5leWsMHpHOt2xjLtzC1nFfG1UxLPTTbKHqCYzWBBfhxphDX_UXna-P-0ZmVIm5n1ZVh1UUYLTekcLn6G0tHGPZBRtY81GtV1oeM-BwCSoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=dbpESipbGQunWxn2s7mYqwL5KxQ-0VdAe-aSMXgvqXbFe0YOxaemL-9JN4UU2hKK0bSvL--4KX5ChgEEpJGsLNwQt0FL8R3YgS9kRkEx22gzxpmdtoou83klx1APdLzT-AIwlNhgzoGFpIKqp7MwWb83-ADpgg8UFURSEYzmwCohe_5Q0LkjZ8aec1YDI_7-ggqqh1iA3qYBItsJGMNOQxsnbU1EFjrRjCnlOdr7a5IVUcjH0tiJpMvh4LEdeMj4ha5ecwmXMvMevLH-PLg5DIgovWTJK6J35T-Wa866ou8cOJP49teXWKBReQccb3zXKQa3VYJU4BYLI54L7nPNTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=dbpESipbGQunWxn2s7mYqwL5KxQ-0VdAe-aSMXgvqXbFe0YOxaemL-9JN4UU2hKK0bSvL--4KX5ChgEEpJGsLNwQt0FL8R3YgS9kRkEx22gzxpmdtoou83klx1APdLzT-AIwlNhgzoGFpIKqp7MwWb83-ADpgg8UFURSEYzmwCohe_5Q0LkjZ8aec1YDI_7-ggqqh1iA3qYBItsJGMNOQxsnbU1EFjrRjCnlOdr7a5IVUcjH0tiJpMvh4LEdeMj4ha5ecwmXMvMevLH-PLg5DIgovWTJK6J35T-Wa866ou8cOJP49teXWKBReQccb3zXKQa3VYJU4BYLI54L7nPNTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fy1a_g45Vf9_wtm16U5e8IeK3483oQQM8OgT7xvO3k_VaJTl0HmPWgzxSURFuGe2wFv_N9t2K6g1lpp0708Pxt4-62p-rv3HRIXH5W7eiJQ_pozgU0NxVsTJPfwT5TzP_SR8xwkSwRI1ZiQK-ebovyOVaCkxlRBxU0REQjtGYmQ9hM6ttSG08Qkx05_giypbZWgHyGVmrZn5X6VtHNtMyeZF-CFwbllUVfKOp80ILofr47GnpOzbPiz4ioRV5RxotFuSXj2A3xf70jy6jdUxEkolmpVymWIZrz-T93Zv0j0l3mdM5csvc7vnwE7NXcoxlBozM73UZWOCtD3KU5VNe4FmGtvSGfz6b1wh7-v9Ho7Z_eOwhz98Cxs9VlaUBFa3rvMkX-7tobDuT7H2OH0jSu7u58CKmOTIwibJ4CqbDLk9ySfdgDReTwvkh6xE3z2CX2BAQSIf5aZOxo0gK1kmwcdRRhv_6EnePJIXVE1DL70vGME6A2gjDonbKOHUnYgFw7TNT1MzbVEQ7vGK9FPctlwYTlawJDj9Q9K2kqEKhDpAdXgDOsG2fqxDDD8NtUgZOI85xqJo_ieUpSNHJNtpOdXZbdT1O0Nfr8psy_k270iyN9KZuXW3kblKwIAqGYKeyE1VqXM173qC2gxUbil4OBTQgcY-xKFNk1AWhHW1TWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fy1a_g45Vf9_wtm16U5e8IeK3483oQQM8OgT7xvO3k_VaJTl0HmPWgzxSURFuGe2wFv_N9t2K6g1lpp0708Pxt4-62p-rv3HRIXH5W7eiJQ_pozgU0NxVsTJPfwT5TzP_SR8xwkSwRI1ZiQK-ebovyOVaCkxlRBxU0REQjtGYmQ9hM6ttSG08Qkx05_giypbZWgHyGVmrZn5X6VtHNtMyeZF-CFwbllUVfKOp80ILofr47GnpOzbPiz4ioRV5RxotFuSXj2A3xf70jy6jdUxEkolmpVymWIZrz-T93Zv0j0l3mdM5csvc7vnwE7NXcoxlBozM73UZWOCtD3KU5VNe4FmGtvSGfz6b1wh7-v9Ho7Z_eOwhz98Cxs9VlaUBFa3rvMkX-7tobDuT7H2OH0jSu7u58CKmOTIwibJ4CqbDLk9ySfdgDReTwvkh6xE3z2CX2BAQSIf5aZOxo0gK1kmwcdRRhv_6EnePJIXVE1DL70vGME6A2gjDonbKOHUnYgFw7TNT1MzbVEQ7vGK9FPctlwYTlawJDj9Q9K2kqEKhDpAdXgDOsG2fqxDDD8NtUgZOI85xqJo_ieUpSNHJNtpOdXZbdT1O0Nfr8psy_k270iyN9KZuXW3kblKwIAqGYKeyE1VqXM173qC2gxUbil4OBTQgcY-xKFNk1AWhHW1TWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmLkMlisL9Lh8vG3w12oCoM1P0OTvaKT7nSzLJQl4FjjA0gxQA0ikvaa8LsKbVPyqjSU0kwdm_TcPzcWkpf7niEtqO7NjjexK8L2p-K67wwP0OL0SXl3dBYpVtY3EID-pjcKofm07ijxV1tBmaLNNA6gEl4GAAbfxZaDo2Nio4GmcjLvV_2sCTkUaImgLp4oWcuy7gdcK2kYD8RDDX5R5vYwZEr5SrkHfbvaeg8nVXVL6t8g58v9x3XZ1v1kL9949HpL5r58Myss1vbORtJOC4vlWaT9JSoshXqT_evy5GAf3FoxVji_4eu3FkqvAfW8rcc-J-Zf5V1HWOrlI0XAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgKJqAkUhvR73L6Fr1hFsWpc-PCh-g5G1i0ckta3SJ-BnYTJWywZT2M9KGYFU_ZOdkfO4DzkFvL5WpFLvdLGwZDXSHd2vuciR8UCUeV-aQsMgKnX9pY7diNeiw9pwUK9SKUep0Aar62eKT7Wb6VfjRPJ_iTlAy5Ln_MhSf_vnBw8yiZZw4lITb0Y3iF4H9EJQiHTuY0b_8PzfEM1sft1xm_YKuqOejg02BLUCAtErq5yTc9gRr-QHyZkLXnTxVSSxAtZIEoVpVxi-cxG8YMGL6Vo6bQtXbOGHbRbTX0GMA-zd0AaWTOTsQu7DI6rHHVoYk-g6jQaLgIWX8FYHD8Yew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnOV9tJgyu6a8hMMZx2g581PpD0fjequnyUf0-vUPZNtaREIlEFpaNE534VU49TK05S0SOEzgLc4pcUwY14EPg59jwtl-XZsTXk4oSFAIgSr1zCKj9HZ2F0ZqIVIWBjp0WAv2_CEPpu_nGVi5HssYH7CYGnwoJXS9RsxjY4TF5SO6Xmk0N_c0uLpv9kR8w1iPdXTqDgB7nDzMCDPsNYgY6p3v-6kH2KfL3FOjywPN5ZCu5XoZD6Ki_r_eaksLPZagi_sVTC_4YFxNYTw2Ju8GWffq6uvfikoYzMlA-foEHd2mnp_0q6veeTibiwwRhBL-9xJCAfIbhqg3c5beZtfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=qA5RcrdG7hy88PoOqcKVg81QJUWISnQvq3EJeZlF_X_KDLmHNBfeHBCJ5ulq_svnRiw5TFoUInb9iMEYq5VSlnQADNn_SEzkFn3MbXetPXmmPSIZgGRQsceYeIf8Y_40ypS-8a3AHz-wJTjgftulA3UvQdZd_RoEyVWHo2j4WEWI5iNcONM8Tq8FnpkeXgXm21aeBjBQusvWIRCZOCTViOV_9vOUBbUOtdiydwVzA6LkADdmTY19fof4A7VHAKdya2GbqtBsHTlnW0n9Hn3UBGNZ7njIAskHVC9RyLsnr3As-xpijdby_p1vCL9ZzIg65rRfqaqimBTtlMVGD_rxSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=qA5RcrdG7hy88PoOqcKVg81QJUWISnQvq3EJeZlF_X_KDLmHNBfeHBCJ5ulq_svnRiw5TFoUInb9iMEYq5VSlnQADNn_SEzkFn3MbXetPXmmPSIZgGRQsceYeIf8Y_40ypS-8a3AHz-wJTjgftulA3UvQdZd_RoEyVWHo2j4WEWI5iNcONM8Tq8FnpkeXgXm21aeBjBQusvWIRCZOCTViOV_9vOUBbUOtdiydwVzA6LkADdmTY19fof4A7VHAKdya2GbqtBsHTlnW0n9Hn3UBGNZ7njIAskHVC9RyLsnr3As-xpijdby_p1vCL9ZzIg65rRfqaqimBTtlMVGD_rxSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=RrtSYm3WPvjXeDn9fyfN1oR9PDHwGumWTJ2_OhYY09VQ0Ito5PlpmxySPVkRcrhnsG89GlJ35nzCuJdioXoO1KmN2gz1fMqT3evQiXl_0DLyfe86hzH8LIsNe4A8f9c5_UyQEqF-oWjhPBs17CCRPFyABy7TyZXd6QjOVGMxQqTf2rkMxNCa2jA3GGpz42o7vh7Qwc9enPkowEtd7XU-FTCkewLAsDxW3yMS4TLJkCccKXViq1u7vTqD3dTLzXx4c2QWh-JZdSshWj90jXqqSvQLC7tx9gcBV7toIaXDEM8WxhFWYgy4wwMWUfsADGu6QgS4Tmm83XDvJB0Ffoo6XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=RrtSYm3WPvjXeDn9fyfN1oR9PDHwGumWTJ2_OhYY09VQ0Ito5PlpmxySPVkRcrhnsG89GlJ35nzCuJdioXoO1KmN2gz1fMqT3evQiXl_0DLyfe86hzH8LIsNe4A8f9c5_UyQEqF-oWjhPBs17CCRPFyABy7TyZXd6QjOVGMxQqTf2rkMxNCa2jA3GGpz42o7vh7Qwc9enPkowEtd7XU-FTCkewLAsDxW3yMS4TLJkCccKXViq1u7vTqD3dTLzXx4c2QWh-JZdSshWj90jXqqSvQLC7tx9gcBV7toIaXDEM8WxhFWYgy4wwMWUfsADGu6QgS4Tmm83XDvJB0Ffoo6XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=iEW2vMQR6A4DzDQbLMh1cQc8-MY944TPqdrjsNQoyN4FLlM_tmUfxvowJphUf3zCEq1wz1-HdzvuPUb-5y2brdC3E5FXOvlo1Qa8gxIqzB3v26DkR3i-IE2V_GOooFxc80eNUkRyAhOBNi2RftmwC41zTqG_wpOfs8Fl9LD4wmSZedml_tn__XOW255aMLzqVlZHtlIux7tOx-MAFj9ZIPd8N_LDKVCXYoktU4lRiyqOWKup5wsPBbWw6XKFr8NhbaZd28fswPj7KXPhXWle1cHzQ_yI-fzxVklavab6EuQJnVlfbWmEo3UpoOQfkZ2wR-eMk3YBc1lxggYwv_E7hahD0CrL--9TYVE7vf3Nx5ajubiTgkuv4SZvV3YtzS0N12_T88W6SWQVr8KGMPirtpwrkrgOg79XDMWmsi_id_zTuLmmoNneKMwdwRmH9oiToJVn4WlttIqOcke5b4A5q9uLJfZAW7EztZmicn958SI_NuffAmaR1E4Q2el3kJIHeIKe1roTckM3dNDgdja2o0Dw9SN2QOSOb9DVHLmvCE-bZwAjVfU_crsI9TTDxCrAumbUp0V8NyBFefxRXy4YWXjnuSNNfw4u5G2I7KOtrIepI0M2dITdDEKcJ_jJTcFO1jtPW1-Zvn0rcdFfJcTDibEpAFsl-K3QzvDWdzqz71I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=iEW2vMQR6A4DzDQbLMh1cQc8-MY944TPqdrjsNQoyN4FLlM_tmUfxvowJphUf3zCEq1wz1-HdzvuPUb-5y2brdC3E5FXOvlo1Qa8gxIqzB3v26DkR3i-IE2V_GOooFxc80eNUkRyAhOBNi2RftmwC41zTqG_wpOfs8Fl9LD4wmSZedml_tn__XOW255aMLzqVlZHtlIux7tOx-MAFj9ZIPd8N_LDKVCXYoktU4lRiyqOWKup5wsPBbWw6XKFr8NhbaZd28fswPj7KXPhXWle1cHzQ_yI-fzxVklavab6EuQJnVlfbWmEo3UpoOQfkZ2wR-eMk3YBc1lxggYwv_E7hahD0CrL--9TYVE7vf3Nx5ajubiTgkuv4SZvV3YtzS0N12_T88W6SWQVr8KGMPirtpwrkrgOg79XDMWmsi_id_zTuLmmoNneKMwdwRmH9oiToJVn4WlttIqOcke5b4A5q9uLJfZAW7EztZmicn958SI_NuffAmaR1E4Q2el3kJIHeIKe1roTckM3dNDgdja2o0Dw9SN2QOSOb9DVHLmvCE-bZwAjVfU_crsI9TTDxCrAumbUp0V8NyBFefxRXy4YWXjnuSNNfw4u5G2I7KOtrIepI0M2dITdDEKcJ_jJTcFO1jtPW1-Zvn0rcdFfJcTDibEpAFsl-K3QzvDWdzqz71I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo5E1hiu289CxtrdbJOOpwO1mi-I4hLOizRV6mMdGFqCVw_VxXxd8HV7ykDBHMATdGoPXcb8SasC4qV2n0YXw7jLSwfC05iFlWK4eTqJicNdz3iMvNLgpa13tXyLEW_btTOaBHpZR0RN_6DM-e4tOqj6D6y--IB8A8C6aNg88b6_6Zp8tNhNB0xZByecf89XxghY_l4J7ehywFmKhl0J2Xbge1Vk5GZFLGydCzqT55KcdnuhYc8EiXT-jvYZTEo3LmlnZV2dddZSs32_u0IdYSMfriYCEqixqR4ZNZp6u7tNDN4Y8csF7I01V-1ZrVwxCynCwZ2QmZ106m7QIWALNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=hY3hoTWEj8Db_zwG-mQx6BC9d3zmo63qpXbQ1dDwKCEAz5TNzFZKNWHi0wqi_81psfimlTn7AUFjweKzInYnq9Imz4DgBtFuyunObiwjMPWXgSQxd5Hlz_XnF14cBgq5FvEGSPS_AfzPkmeDf5VdQFo02-oSEKjhTL76eqoNxZF-n8X8nuDb6SbYCEbHmQXfXF5e-_A2e96xcjR28VH0TkDQTGy6lBXryG-T-J4-RSyWwzoALOltdkxCRFXn0qtufAtTCbd698eMtwlMUdL5fRc8HDXMv4YBayO6a_uq-aDh2aC5Arn3R_IQFVFTUGJ9g7sWjcduZ7RNCbLr5cywgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=hY3hoTWEj8Db_zwG-mQx6BC9d3zmo63qpXbQ1dDwKCEAz5TNzFZKNWHi0wqi_81psfimlTn7AUFjweKzInYnq9Imz4DgBtFuyunObiwjMPWXgSQxd5Hlz_XnF14cBgq5FvEGSPS_AfzPkmeDf5VdQFo02-oSEKjhTL76eqoNxZF-n8X8nuDb6SbYCEbHmQXfXF5e-_A2e96xcjR28VH0TkDQTGy6lBXryG-T-J4-RSyWwzoALOltdkxCRFXn0qtufAtTCbd698eMtwlMUdL5fRc8HDXMv4YBayO6a_uq-aDh2aC5Arn3R_IQFVFTUGJ9g7sWjcduZ7RNCbLr5cywgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=DvalGzgKM22wzLOHVnV639oKGCtL3U0mJxe73ZMosFJvN4LSSQuTaIzM0TxFV6BHDGucrVItBkg9DP36QdwrwOnzoYsEdVB86yblkk07CHwWnuovoIwUyujXqM8Fq3xNkuy6Cr1T5ixxyJKb3z4dTg3P3SsK213BayHGYACilEgKm_vgp4vqp3XWQW-G412fo8yvP_0FHnXTgOQc2wWYlLpgYt2a8LZQ0r-QBJzxU3r0pvcyaC_78NZSB593MJrD4GFSS9ghWPQbhGQJvKpGWqatAm_99N74HBIYRJq369vgy3iVqEwoAgRhXtxZGIVAeCincSB0SIREPBJyIcQdiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=DvalGzgKM22wzLOHVnV639oKGCtL3U0mJxe73ZMosFJvN4LSSQuTaIzM0TxFV6BHDGucrVItBkg9DP36QdwrwOnzoYsEdVB86yblkk07CHwWnuovoIwUyujXqM8Fq3xNkuy6Cr1T5ixxyJKb3z4dTg3P3SsK213BayHGYACilEgKm_vgp4vqp3XWQW-G412fo8yvP_0FHnXTgOQc2wWYlLpgYt2a8LZQ0r-QBJzxU3r0pvcyaC_78NZSB593MJrD4GFSS9ghWPQbhGQJvKpGWqatAm_99N74HBIYRJq369vgy3iVqEwoAgRhXtxZGIVAeCincSB0SIREPBJyIcQdiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=tT8v--8lyHgd42D77WaKkJL4Vh1ui7YOIhkq3qd8nnX8L_Jb7fwB_CYD1n6P3oPoy5X02bDiE4ASr0PqCLPUGl5Fpx6qT1aA2Jg40ZOow98aLvf28UJgPb2o0Zb2t_AtTE24eeGdtLuX7T74Gw5ypNkFZ3uwIvYoaQ20xELgvDYk35DWYG7H4MftBywLvqVb3Yo54Oyp7QuJIDw7u_K3bZSnA7hs2vhAOguw8aVUoYGEqPA3xpcAk3-shdRdr8sZ-0ePTrzcCiM8jQM5cs02s8Kg3FhQSmneTA_ySjFmXYkXOzyuyPgVyRS2Zh4GQrQMVm_FixYifBHwxAUfo50WeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=tT8v--8lyHgd42D77WaKkJL4Vh1ui7YOIhkq3qd8nnX8L_Jb7fwB_CYD1n6P3oPoy5X02bDiE4ASr0PqCLPUGl5Fpx6qT1aA2Jg40ZOow98aLvf28UJgPb2o0Zb2t_AtTE24eeGdtLuX7T74Gw5ypNkFZ3uwIvYoaQ20xELgvDYk35DWYG7H4MftBywLvqVb3Yo54Oyp7QuJIDw7u_K3bZSnA7hs2vhAOguw8aVUoYGEqPA3xpcAk3-shdRdr8sZ-0ePTrzcCiM8jQM5cs02s8Kg3FhQSmneTA_ySjFmXYkXOzyuyPgVyRS2Zh4GQrQMVm_FixYifBHwxAUfo50WeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6gCe86a8Vzw0JnwXWVn60hBAML2cMjt4VGoLm7jGwpg3rXJitdthKtrpv1qTJ1QxTF-UWfuqjIj4pam0peu837xdwbPoTbhFui-hMP9fr6F5exKm1BPh5gVimJ53IgSBk0rtD6CJCAJYsj_vC7D0ZTPO26OL8lP_rc2OLE2WCFB6cjCNg7FsoLUCGMSMOPR5CkyGCHSQUzAETr0SABmtPPGPvboXo9BjyVu_BnQPDn-bZ1cKUopUbdi588PxOXk9Jhx1JAdZMyB8-ffqjGPYqLUP6Z9L1eRSvUmt87rNPE22J6M-cWDnauJDdPVDSZzmNKLwbksG3XTUz6sre1sCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=vq69xTpQnZrmbj345GNkq9ewSbAwhRvSe5CQcs0aoT6TE2KgE2ZGoYeIc5C0H70z5gtrlvkGPBpJlvVnRdSyyI62ERPJlHvcQpOCcryUDX9HmcPzeDwFm9jiO6d_mjXOSX661_GNnXjt5No0hl1W1f-aXSu7w-mnzuVePbBtZANOqZ_pg_T1nxlzcRiXX1_PVk_Lnhj1rR6R66eGim-k6IB0MVGN17Z_JhLICGdzsP3zxAvdZPerd3Zp1IpiyDJX-1NGFQIp4tWJ_gOInNAg9316fv-cKKhyfqP4N-3TMGLSeSGLXePegCXYw1XxNSyJfnnMMkk3K0Woc98Mlen2Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=vq69xTpQnZrmbj345GNkq9ewSbAwhRvSe5CQcs0aoT6TE2KgE2ZGoYeIc5C0H70z5gtrlvkGPBpJlvVnRdSyyI62ERPJlHvcQpOCcryUDX9HmcPzeDwFm9jiO6d_mjXOSX661_GNnXjt5No0hl1W1f-aXSu7w-mnzuVePbBtZANOqZ_pg_T1nxlzcRiXX1_PVk_Lnhj1rR6R66eGim-k6IB0MVGN17Z_JhLICGdzsP3zxAvdZPerd3Zp1IpiyDJX-1NGFQIp4tWJ_gOInNAg9316fv-cKKhyfqP4N-3TMGLSeSGLXePegCXYw1XxNSyJfnnMMkk3K0Woc98Mlen2Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=iOmfUDo3BmM_aevVnZ8H5nYaN3RFzpLyd0I03MdfLkPU58mr8YXKsko5YeyUtYwBXfvVaxGzq7hCw0e4FpfjdMZUh2SurruwckmvT8JHCWOUDoXThMGpCRgtsG22oGHSHK85BFBHGypu9BWoJT97DF9YCC6FhJAHkkwYnonvjMzMXkKtwtG-UJnCp-PrCeKYnDX-Ail20nPPdAciQLymy9do3HGu6JEs704LX0VKDhnEFbDWCkcwV3ldoJJ0fy_AJfbgOe6pALzBem7LL6FlK3Dc9ljxKPk5jv6Lssw6hBMrpfeKI-63AefHp13_MIkgTEpZ-2-o8CJ-3IZBdZeLiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=iOmfUDo3BmM_aevVnZ8H5nYaN3RFzpLyd0I03MdfLkPU58mr8YXKsko5YeyUtYwBXfvVaxGzq7hCw0e4FpfjdMZUh2SurruwckmvT8JHCWOUDoXThMGpCRgtsG22oGHSHK85BFBHGypu9BWoJT97DF9YCC6FhJAHkkwYnonvjMzMXkKtwtG-UJnCp-PrCeKYnDX-Ail20nPPdAciQLymy9do3HGu6JEs704LX0VKDhnEFbDWCkcwV3ldoJJ0fy_AJfbgOe6pALzBem7LL6FlK3Dc9ljxKPk5jv6Lssw6hBMrpfeKI-63AefHp13_MIkgTEpZ-2-o8CJ-3IZBdZeLiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=hEBfsqA7lcyeVGxO3m4ayDZTEEmcL5XvGPyvFLlfIGzZ5fWA1fvcUJUUUVZqcapjRJK6pMdyy-CYqg6aDNNN4cZ0GspGMYaXHJwVaNvEGWlgxcA8XfkIevBtXh4JzswGvwNAVTaiCCPpTlbjGALCzRIxo3KlDWg0C3ypHQpMsC1WRFbPYWWigiPcO-JggzZ0AzEVBpEYwdlXC0-oDpwp1zSXUcrbDyCK3ofUpHYBqNo_YQz7-bNWxdpG1pYrbNxrtV_79ViToOZzO0zZyZAWCBLlH9xOoXDvJy1mRgmIwDaikz38bDBF1fdItV5KIuS6ENnTJGGpBrcdtBM7RdqEYKHYM6DwKqHM9094J3BSGGmRrAX5hbX4hf-4rUFOvuj7wa4bfWUk5c8rK43O5HxWpD8-mpTTjAPCzcqEIUENJx7-vav5muEeijApvfS2ixFAAo-yW7VUx-XBJ2augD6qsV6kdf5ZJK17mP11-Uoszq5lkfJ6aRadmtC0u9sJ2MPuoaDYLpO22XMk_RVBEjN0PIJd0HV52xqJi4a120T-vwiAcb_4_oN4XNkczQrDEmo4uj0EwuG22zLVLP6W10-JUTpyiO-j62gkid0ZMNUM5Q3YBBRn7d-J4dMaWKDKjbrNABPTquRw1Niw0oPUJ0MqSpyuTMTm9ajsaiEgNCzGufI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=hEBfsqA7lcyeVGxO3m4ayDZTEEmcL5XvGPyvFLlfIGzZ5fWA1fvcUJUUUVZqcapjRJK6pMdyy-CYqg6aDNNN4cZ0GspGMYaXHJwVaNvEGWlgxcA8XfkIevBtXh4JzswGvwNAVTaiCCPpTlbjGALCzRIxo3KlDWg0C3ypHQpMsC1WRFbPYWWigiPcO-JggzZ0AzEVBpEYwdlXC0-oDpwp1zSXUcrbDyCK3ofUpHYBqNo_YQz7-bNWxdpG1pYrbNxrtV_79ViToOZzO0zZyZAWCBLlH9xOoXDvJy1mRgmIwDaikz38bDBF1fdItV5KIuS6ENnTJGGpBrcdtBM7RdqEYKHYM6DwKqHM9094J3BSGGmRrAX5hbX4hf-4rUFOvuj7wa4bfWUk5c8rK43O5HxWpD8-mpTTjAPCzcqEIUENJx7-vav5muEeijApvfS2ixFAAo-yW7VUx-XBJ2augD6qsV6kdf5ZJK17mP11-Uoszq5lkfJ6aRadmtC0u9sJ2MPuoaDYLpO22XMk_RVBEjN0PIJd0HV52xqJi4a120T-vwiAcb_4_oN4XNkczQrDEmo4uj0EwuG22zLVLP6W10-JUTpyiO-j62gkid0ZMNUM5Q3YBBRn7d-J4dMaWKDKjbrNABPTquRw1Niw0oPUJ0MqSpyuTMTm9ajsaiEgNCzGufI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=tr73L4khyTESpgWWq0jXOqIHFe07CfNMgBg0AYU5xe_qPgbqFFUTjRCXDJBgRFyX0e43Xyzk-mYUX2zAx4g1rCapWU-q7e8LrTWOuB8Bfbt6dQl8_V-MWcaZgYuKlxN5Kqs4QgeDaI6v4NpR0D63UbMmhkFY0z5aQM2quLpIMbL0GlPLAr_lm3ph4hv-GTAS6IBzGnxHNFJHqTAHpdcFo8YHKP1FWareiZ6BKI34s9F9T6aeB-a_N3C89BWJsH6zadXLRD5oQaR3RcBzYQW3MnGAmBDVGDHRshFrwkEjC16tssCjW4QPqLmZBgUybTmIVokaPYs510dQqu_MX5TAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=tr73L4khyTESpgWWq0jXOqIHFe07CfNMgBg0AYU5xe_qPgbqFFUTjRCXDJBgRFyX0e43Xyzk-mYUX2zAx4g1rCapWU-q7e8LrTWOuB8Bfbt6dQl8_V-MWcaZgYuKlxN5Kqs4QgeDaI6v4NpR0D63UbMmhkFY0z5aQM2quLpIMbL0GlPLAr_lm3ph4hv-GTAS6IBzGnxHNFJHqTAHpdcFo8YHKP1FWareiZ6BKI34s9F9T6aeB-a_N3C89BWJsH6zadXLRD5oQaR3RcBzYQW3MnGAmBDVGDHRshFrwkEjC16tssCjW4QPqLmZBgUybTmIVokaPYs510dQqu_MX5TAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dywwK0pKHksaL_sSegRcwHbnpbif6h4W0qyqWNfPU0fOR9vkRz_cG4wD23EJ9OkCPtjAvUpLtthyOC-xQGPm5CcdO4HhfvggZksW7bRbBu_1iIkk0NJpVrSPFvgGdehL9vZqaH71Kop0kLtra4lpNs28k1GlYgMrpPuMoaPyPojdp6vJlYKeqDGoN2UryhAZ5R6j1MbW9FQh5Aywiw2YEU-G1zVGNzkqqwawPIGkcQVX2rYy_E0WUoYHlVf_1yUD6bEHsuXG0gRSklTKl7JXGlTryOWcK21WhxdCsx2rQ23s_oTXMUqzuZaeV3Tm4usk71_52uXdusGuYfErYZbyag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=dqUU0whOR3b4WthovKNYjRungWU-AOIiGfwcnzsiuJSPp_-UT3pXjXtz2sk-WdXwgfJ6EhJuzysx3BRn1561x3Pj_Gx7WiCd_S_unuy_dHqRngzD_z8XM6hX3GhIbazy9a75o2p7jg9eJFTGusrbPSar3rsYIHCxh8nZxar-3OMx_9INsKrUM7zajJ__MsFoYEmqFKrycHY9l5ZVkY2gj18JtjPJMcqXJXcvptIjDNeF3Ch2gWojrPMZRmibZFbhb7P5OJHKsUOn50N0ix3ivixUbPzyx33KvIqsXTqy6zv6hZk5du0hL5cayiAel-qoeB_h8hGPxHI6gxbNDRexEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=dqUU0whOR3b4WthovKNYjRungWU-AOIiGfwcnzsiuJSPp_-UT3pXjXtz2sk-WdXwgfJ6EhJuzysx3BRn1561x3Pj_Gx7WiCd_S_unuy_dHqRngzD_z8XM6hX3GhIbazy9a75o2p7jg9eJFTGusrbPSar3rsYIHCxh8nZxar-3OMx_9INsKrUM7zajJ__MsFoYEmqFKrycHY9l5ZVkY2gj18JtjPJMcqXJXcvptIjDNeF3Ch2gWojrPMZRmibZFbhb7P5OJHKsUOn50N0ix3ivixUbPzyx33KvIqsXTqy6zv6hZk5du0hL5cayiAel-qoeB_h8hGPxHI6gxbNDRexEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=rMKW7n4Y7EpgsQhBT8HwQK4jo01WqIESPlJL6RNXb1JDgts-3gFfIC8zbrV1VadpH_TSrysl-3A4EIboXSel6VgSC_YJq63ZeW7QHVyVd_QF16Z378Qnhkio03DxNyBd93YFOb9zD_c0FQ9xa6NgE5aaDD6aofYn8SQqy4izxCKwWJrqoB0RKOGJRxxiDx_A9kukN5jVcYG90MBRt33v7Ctpike9iMWmNl2PZPqasoHRySuhmXlMPzs2RgLvTmGSs7g51kNo7bpKYb8WXJGad823UBqSUtQOW4UthCO1Gfw8KSTBS6bwGVRASWEWlkLX35A4eSC4VX8vOTfW4GeHDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=rMKW7n4Y7EpgsQhBT8HwQK4jo01WqIESPlJL6RNXb1JDgts-3gFfIC8zbrV1VadpH_TSrysl-3A4EIboXSel6VgSC_YJq63ZeW7QHVyVd_QF16Z378Qnhkio03DxNyBd93YFOb9zD_c0FQ9xa6NgE5aaDD6aofYn8SQqy4izxCKwWJrqoB0RKOGJRxxiDx_A9kukN5jVcYG90MBRt33v7Ctpike9iMWmNl2PZPqasoHRySuhmXlMPzs2RgLvTmGSs7g51kNo7bpKYb8WXJGad823UBqSUtQOW4UthCO1Gfw8KSTBS6bwGVRASWEWlkLX35A4eSC4VX8vOTfW4GeHDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=p29sPqc4HGJhMYRNM5M1r63hO2JxdCttBzFOGv0iVOhO6EGmzPueMiBAgNEi_YfM2b6hDAU3FiTiRKYHX8TJA4zmRiB-AremBakbMBv-nXObrxqQtJOFDMEwBwiNDalm2ifx_SMK4l23kEjlqYsBKFdQo2C2VsNm3TJNhkcG1JS-1ha26Z_sD_-i8vF3hUrSeOGW4zzcEjZcrM9TwAvZEgEakHfHVoOKuD16v8zj0RZhDT9-A0r_xTVBio3W_qFuHjkE1GlmD1qJ5Hiw1S4jePoD8ne5KL_Rlne5YVLaES0bfsbPLoBafRbrTtDyYuNG9RpA_vXcSF1cgFCXAqny4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=p29sPqc4HGJhMYRNM5M1r63hO2JxdCttBzFOGv0iVOhO6EGmzPueMiBAgNEi_YfM2b6hDAU3FiTiRKYHX8TJA4zmRiB-AremBakbMBv-nXObrxqQtJOFDMEwBwiNDalm2ifx_SMK4l23kEjlqYsBKFdQo2C2VsNm3TJNhkcG1JS-1ha26Z_sD_-i8vF3hUrSeOGW4zzcEjZcrM9TwAvZEgEakHfHVoOKuD16v8zj0RZhDT9-A0r_xTVBio3W_qFuHjkE1GlmD1qJ5Hiw1S4jePoD8ne5KL_Rlne5YVLaES0bfsbPLoBafRbrTtDyYuNG9RpA_vXcSF1cgFCXAqny4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #50</div>
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
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIuSP3omEP1MqEUaUhLnh3VLZijhpIEjPt990ADCD7U-KJTpYZviTczz54OcQYFf_HUwp2z8DosvsUF4fjkUGz81wkvxD-L2rZItGp4VmsyqijEfKvfkdGGq0goiprYppOCQNclacuwNpBxkcx2lotiaWRkOa44HnFawR_u9mXtS4JGPq2jj6-NN-sd68n3MtMm_TRsQ6Z-6ih3hxjjlqXPkNfQUG0AJPdHceEn5YXN8MdFARC2Pk_aKsZM30-Urhn3yETYkl8CE8Y6_fC6HzfRpi-gYNOz2SgLz7XV0A12hoP5bCxq-fUMi71uif9ETe3Pq8brCNCNmYoA-hm_naA.jpg" alt="photo" loading="lazy"/></div>
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
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=ZpUAaVzRlEE8hNPfI59Ojt2LqwJ44XZVxL6QA7Qyd3PKkzP2yv_0m-nLHOgX7Clnh36gTrya6-c4EmMbf_NAx-nQ1mJ9pbOqb7VplvZi6LlFmuzQuyoWjeWRrf-5de4la_I3F9ojrueg_qTGCL7nauAZVPyyJ-kIxcexzaDl3-s7PQmSaNO0rBKQr9GKO46dZEofOYJavDZn2t7dfyxbQ1lF16Zs1ZeXWnJcjYHqG8XQmWWu1Io4j5ARnPhoU6m_HNLyd8-i_Id6UOkEMe-pzGCf3g8dr4DE7H5jxMkLD4QXCLP5db5Scs5aMrXA6BNZTwvC9bdZZf76KBACZFLZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=ZpUAaVzRlEE8hNPfI59Ojt2LqwJ44XZVxL6QA7Qyd3PKkzP2yv_0m-nLHOgX7Clnh36gTrya6-c4EmMbf_NAx-nQ1mJ9pbOqb7VplvZi6LlFmuzQuyoWjeWRrf-5de4la_I3F9ojrueg_qTGCL7nauAZVPyyJ-kIxcexzaDl3-s7PQmSaNO0rBKQr9GKO46dZEofOYJavDZn2t7dfyxbQ1lF16Zs1ZeXWnJcjYHqG8XQmWWu1Io4j5ARnPhoU6m_HNLyd8-i_Id6UOkEMe-pzGCf3g8dr4DE7H5jxMkLD4QXCLP5db5Scs5aMrXA6BNZTwvC9bdZZf76KBACZFLZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=XMf2-mGA-NiKBumrHNgMlUjbPbkoDJfOSqDw2JjuEC3h_PwhUN72qZy2XuYso2gQRWXLa19NyVUTFjlZdqtZZW-NqNQy67QBlvlxzSxr7BsVDuxKP8KLq4nGgmywUlLRt7_rzGlNt2UsLR0M9l6XQBh4lwQVfE65PNuPBKdD0WNoqXzewK9QYRurC09mZh8J_LWSUzkP4UM0iyTnrYMxE_gp7Irl8OirPewoYlytPWFrjTcZVleUykw-XoagwQdaTwMPnx5cSCuNZkvXBLcuavK37hfWofGtPg3ETskhOAmXM6QlXkjCqoorwD8S2G8J2OQYx7mykkMAY_BKWgudeA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=XMf2-mGA-NiKBumrHNgMlUjbPbkoDJfOSqDw2JjuEC3h_PwhUN72qZy2XuYso2gQRWXLa19NyVUTFjlZdqtZZW-NqNQy67QBlvlxzSxr7BsVDuxKP8KLq4nGgmywUlLRt7_rzGlNt2UsLR0M9l6XQBh4lwQVfE65PNuPBKdD0WNoqXzewK9QYRurC09mZh8J_LWSUzkP4UM0iyTnrYMxE_gp7Irl8OirPewoYlytPWFrjTcZVleUykw-XoagwQdaTwMPnx5cSCuNZkvXBLcuavK37hfWofGtPg3ETskhOAmXM6QlXkjCqoorwD8S2G8J2OQYx7mykkMAY_BKWgudeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=GlEEoPuN4iDN0Fa2_KTArRhw7Sy503CDlVS4PWGhPXbU6Xxl7DfGBTWvuyK4fTX8zIP6PsAJugAiN6lsFsdNkNfSpMASFWc3zOzKEvx2dXf0IoDUBB6zIIPgzVFRIEaR2g-HCGVztu2Jqsbdjrp-dDYJK6lfJ4fhmWmz579gnCzbDk_hod4la8IXNlYGv0fvAtU7UX9yLNtXXchLg6DVNzFrdxZI4VwT2PtbRQ02a9rRnFsXykieFip21f4pPhqzvh1RZanWFlf3tBNWOCbItjxU3tmFhL1ENyZPHd8u-rrOVz8UDMcBPVCn6ih8n4iD7IymXbicvI11_UV-M2OP7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=GlEEoPuN4iDN0Fa2_KTArRhw7Sy503CDlVS4PWGhPXbU6Xxl7DfGBTWvuyK4fTX8zIP6PsAJugAiN6lsFsdNkNfSpMASFWc3zOzKEvx2dXf0IoDUBB6zIIPgzVFRIEaR2g-HCGVztu2Jqsbdjrp-dDYJK6lfJ4fhmWmz579gnCzbDk_hod4la8IXNlYGv0fvAtU7UX9yLNtXXchLg6DVNzFrdxZI4VwT2PtbRQ02a9rRnFsXykieFip21f4pPhqzvh1RZanWFlf3tBNWOCbItjxU3tmFhL1ENyZPHd8u-rrOVz8UDMcBPVCn6ih8n4iD7IymXbicvI11_UV-M2OP7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=clfyVyz3waYVJwI0rwHmxKjfsJguBssQLD5ptEUjiRszExQYBHZITsIk10NXlme21RWzm_VEuWXPYSJzzDsfWn50KlEx2jaAB-s_iRZHM2-PqiH0TVqr-EtDyTYtSsQG_PaDlFV0UCq-9_26d15jmC3GP9e8XNxqXwgFOCSe1gOXT-IQKPh2grll57jVb6khDQrKAvsewqdugfZHYIWdJl7YQIehu1gzvA5j2w8aHwfxLw91pZ8FaTyyKLMF3sFobrKCM4C7rS-bjdS29MDN3YzZJmx1Dt0ju90vM-jZlg1QjdM5J9PhlEyD7X_dHWrpqmjfZt53nj0GuvkqGR-VUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=clfyVyz3waYVJwI0rwHmxKjfsJguBssQLD5ptEUjiRszExQYBHZITsIk10NXlme21RWzm_VEuWXPYSJzzDsfWn50KlEx2jaAB-s_iRZHM2-PqiH0TVqr-EtDyTYtSsQG_PaDlFV0UCq-9_26d15jmC3GP9e8XNxqXwgFOCSe1gOXT-IQKPh2grll57jVb6khDQrKAvsewqdugfZHYIWdJl7YQIehu1gzvA5j2w8aHwfxLw91pZ8FaTyyKLMF3sFobrKCM4C7rS-bjdS29MDN3YzZJmx1Dt0ju90vM-jZlg1QjdM5J9PhlEyD7X_dHWrpqmjfZt53nj0GuvkqGR-VUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFZ7rpJeAL_OnDagjU_vNcEan-kgZ8BfzX4ElyFcijP4MdoyBjYeL4zlDavNXW0BGzXIEjRUMD2Fq183aVgrLBHv9AGAxjAwvAWZC_bOouohYSEmPrGyY6WmG-V3G_9areVfnaPNi-c6K30cjgntrnhgYCLtFTcNHr5jS5Tqs_8-Ua_2bBc4gQhu8BZKwjNk2QCNdtxWCk9ANvmh48GWNcU2AT2a2Kiev5i_5xONYQAO77yLVfYSuvKZ4jkwiE26hFNCiQjvR75SPznX5mViUnzyZE8hBwT5stO6YHbnMFr_VojIWLi3aWVKtof4yhA2eT_qYbq3bndc2ED5438W2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5CDIPDJO0RjqdR-ejpNjzxF6wsi6rHdG4uZj5K7WuV-lCSNbTq_BRFVDuGE5PPMb_vb3FhpI1TbSHgPChr0HqwCXqvOTcNYmBYgDJoZMUpyutCj1KaaUUpHxoT4SGi4dvQcV6SFZitvp_zHF-GxRhy29_jlzNHh83MvyXD2Sus3MSGZT53ljgfnBZQD3D2__EjibXiMORzGA5ou0UYBwNxtgCp80gcp0GjEOrQvvx32jwmcGGWw5HmjkBqxegM9trv4UMyT9yzVQ7NC5n-bLRzdtea_ud-GuzZ-W917XPMbG3cmJU5gWApxojDRsE6WiJLuPOexl_7HkLXj5mXMsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK3Wx0Z1vMFoJbLKyJZBwn0r9XGWgO6fELDC-LAkKTHScTSOxHKOMLoNcoTZ78hhBz6LTiJUZr9iRdwsxlo1c-vm-BoXH8vABxUJKdkswLOVic99XsscQaucqJUg502XoN9zIgXeh8hiG5zTM3jDdkNRLpsaadvjRYOyAjTi1byIjjn3SjRBEjzP68Rnkh0z298xiBS1ombibDXKjO-pBZ2kJSjq-fl848pDQWfM6BCgfBz8BYPwSOQ2us3k5nmm8x8qRfl74P70LKcRBHYMI5ogT85oY9woj5XivQmnrYNwb1WLNER-dlkVRHVd3NbYMXSHnZUPLIcEoFl8ZbGZCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8T2INtYGvHx_8H1i9_r1zTzOc7Oem8nx7VddWABvhuZTf8AgMrCrjFX6_15mfJHElPc41spQVcrKttMZ0825AP4-AbBp9G8FxNUJfaaD2YCpQXIpddIUEhUfHs7uVv4ceYcKa8NIYQas2x9ezjUBAkNNOiq112a1VmBAzOrfy-4fJBCYEtLUSBPlYy3yvvlD8Q8E51pZqcsfLp00fBwpD2eSTGE_MGsvysinpPnLRIRYSOyI0ZxtaL70TmeiaPvy0-wKq2bK_SeUDV1wSmCqM0CJdcd20cv9T9_pqG2vd0Jl5apqAWQkBS2U5bmBo6ifX11q0NS6Bh01fb-n8I3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHpP7cBWVsBzSK1qFfcrFfJlqFvXyi8UgmF78c4MDUyCVHiZPWilXdkz1VeAY1Y5Q3yhzRtZe88uIV7Nx4uvweFTbrKu6ns6qhCpaqhI8U1TKinOXyAAxUlLlisZQIt1-kTdGCAoepSZEE_YNYAbCCkL0UyYZlQh_7XM2wXR5vcjRAxTuuN5II6CiI3Es0mwU8VriGumhp49K2jIynf74gGbwZlm6oILruQh2fXkyBx-B284G7cJJC-62CpwNgX1-K3Gd2x8tuencF7JkPkxtkxjus3dSN3BxAJs5U3iVV7noFVyRlr2GPzyX4rWXt_-ncTshTdn3cjzw4GIJhG_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=P-QANeaEbvLNsKbgPRqIGBxA_MWJxW8EZDqww3JOqRHqtZhu0wR9zpGfdTmFAyqZLAT1BPFsyvrm3M3whHaYqzvzusMmqjyFSpV0NKrJD14d43wvoLsQnVUwS2TvQbcWUDCAG_1udk8DGVrWDfBhbDilg_fzlYlfP-Xiva3W9RPAs_gAlx-uQQI2oO6VZaGvqu7AYOC2YIosJMinOS-y60cY-wLatP0awW8GrPBHtvM5ixbxj32smW46GdxZ6BTHlxq7B5ZWvoTYqOuSJIXaEKPecGmq06VEGAj7tGhpwao8zDQf_Wya8fy2rQhkYqzLC_2jVPNlCfps20gaRByY3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=P-QANeaEbvLNsKbgPRqIGBxA_MWJxW8EZDqww3JOqRHqtZhu0wR9zpGfdTmFAyqZLAT1BPFsyvrm3M3whHaYqzvzusMmqjyFSpV0NKrJD14d43wvoLsQnVUwS2TvQbcWUDCAG_1udk8DGVrWDfBhbDilg_fzlYlfP-Xiva3W9RPAs_gAlx-uQQI2oO6VZaGvqu7AYOC2YIosJMinOS-y60cY-wLatP0awW8GrPBHtvM5ixbxj32smW46GdxZ6BTHlxq7B5ZWvoTYqOuSJIXaEKPecGmq06VEGAj7tGhpwao8zDQf_Wya8fy2rQhkYqzLC_2jVPNlCfps20gaRByY3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJQWrKjce1hD5h8tf9K0Gqe2_14T8hP9ZZUWryiSCSaUU96rg1gu5e4zcwi60mlJOUohOvrTai_eyRYUN4BVAX0Y_thA6gMEow-rm-HNJURIo_9_l0LnI_Kvesh4dBipIqtbjgNN4b5imIJck992ge3Bw_ViNUlS1tAhBm3WQmhrO-Ow_nyunFZry3oHBxtso23TvZzUDU9fhSNejJmIPqijUMJRum9UIwTG4vdxNzt3L5TfCw7UZj-gUfCkmGVRcJCYzcvNahcvjGuhY_Z5NOSnta18xQN47hB1wGpUdfC0DLw9c_HwRTfM9HuoYm409BFIx9zhxWMEgN80mndkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDGrMR7Hm0Q01uuYaoYn8hZFsculydFx98uvZ5gc4pnkMYpoJRBpjJOTu3EE1zEueHS3J7r_h2NCKL25Y9_lcoDwk3ewaPyLOK4vWru4cWQar3cpktfnxsM2m-him6QPMlwvJ1fXIRF5Pi5Jgwiw3YnEsfFjKGLRpNLRJTdAAK13k0GS0BNJEKqyaH58xgIhNkJPh3Wgst-PYBcQ0iB-K_qf-hRhrUL29wg5MYSO2zPqqgs6Cq43bEb6zuLHd8M1z4_srjc7o_WDYXyBwutg2ZAVW6ccGbC0GBSlJTR9W3ETAJUb3QYpK_N642SrIvrbDxKun6wd40QxxDiNZwB5Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=jZ6CNkyv_VFPZd0hAQWTOn_GAGmzYeRQni5Ks6NfIQjx7l2nXrFDyuDnUDMn7Z8uYGV8ddLkPc7sdu-5RdcRDBUIHN2wEY_WpXK0CUmXD0yM6R6iO3oxbZzyHTVUZCigrnjU---o8DSUYsvJB7i-JDPW-rG8NKd5VcsSCIIakDGgB3tsKQOea7iVSDn5v5jUOwS1sIKKajKoMmwO37XEvfKdkg5ZPOMP6HHEJeD3mQXeFWw4Y-UIG5IhRFVwi7wkW1F_fmpfLc15I0CwpODOW3q3ZIbjSCaRi69-lcEoaLxW_fIngx9IkQzHxRZOnAIPUVPeP60pKa7-SA8xTdzFVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=jZ6CNkyv_VFPZd0hAQWTOn_GAGmzYeRQni5Ks6NfIQjx7l2nXrFDyuDnUDMn7Z8uYGV8ddLkPc7sdu-5RdcRDBUIHN2wEY_WpXK0CUmXD0yM6R6iO3oxbZzyHTVUZCigrnjU---o8DSUYsvJB7i-JDPW-rG8NKd5VcsSCIIakDGgB3tsKQOea7iVSDn5v5jUOwS1sIKKajKoMmwO37XEvfKdkg5ZPOMP6HHEJeD3mQXeFWw4Y-UIG5IhRFVwi7wkW1F_fmpfLc15I0CwpODOW3q3ZIbjSCaRi69-lcEoaLxW_fIngx9IkQzHxRZOnAIPUVPeP60pKa7-SA8xTdzFVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=OXG8O7q0jnJtMyfgAEAN67qoLw2RJQeNi2H-1n6bQvInc6v2bkZTzW6UXtmCJChJ3dCdBBhsTk9ay76ZgWDZNGMzlGsWIji4-b_20V3VJl-SyjZULLSDAG2E-sBd1eQVLsN3RaCLNhM-BSS-qACx1VPd9TMr9zKt99ixtC9ndy8OR9fUNobz6EaxfVfqwifDB0tCip6J0_TZlAkwclHbPBuMiMcvTDOzORfni9TyPCMQRFil266_hjScnGJn1OXSmkfg77eEum3u9xTLGPICrB3iacw1XAuXGhO7oGrIoJ-OubqfuUgvMmzNyEbB3rPdmnonIzVz8uD_88W5C4QI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=OXG8O7q0jnJtMyfgAEAN67qoLw2RJQeNi2H-1n6bQvInc6v2bkZTzW6UXtmCJChJ3dCdBBhsTk9ay76ZgWDZNGMzlGsWIji4-b_20V3VJl-SyjZULLSDAG2E-sBd1eQVLsN3RaCLNhM-BSS-qACx1VPd9TMr9zKt99ixtC9ndy8OR9fUNobz6EaxfVfqwifDB0tCip6J0_TZlAkwclHbPBuMiMcvTDOzORfni9TyPCMQRFil266_hjScnGJn1OXSmkfg77eEum3u9xTLGPICrB3iacw1XAuXGhO7oGrIoJ-OubqfuUgvMmzNyEbB3rPdmnonIzVz8uD_88W5C4QI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=Vqq4nuFQpJTWLPoojR1JEBLZGbA0D6mFkKCMwQIJD6BAlLhqR54JMA41QL-WLwDm_rqiAbpCbNJFLEMkORAEcZw4lGYM9LOt8IfJzFOwGbOH76AtRMQvQRa8T0EBWrx-PtTHPXAVet99uvdUPKo1xYuZxJAdG5emi0MtbC8VtKDxGXOAinkhBwT8GdWYmH2w1crG337ieaw9r8De9cg3l1pBnXxSAcp78hHEO6CDO_b897OPJHCiYbhVRzouvLnVS1HBK8ducn_OFTz5u_S1LjVD1MM4KSY5oQZTSrtgEuK4eGxUI9YrLth8WRp3fP3W688_mUt8puEfqgF0HeLH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=Vqq4nuFQpJTWLPoojR1JEBLZGbA0D6mFkKCMwQIJD6BAlLhqR54JMA41QL-WLwDm_rqiAbpCbNJFLEMkORAEcZw4lGYM9LOt8IfJzFOwGbOH76AtRMQvQRa8T0EBWrx-PtTHPXAVet99uvdUPKo1xYuZxJAdG5emi0MtbC8VtKDxGXOAinkhBwT8GdWYmH2w1crG337ieaw9r8De9cg3l1pBnXxSAcp78hHEO6CDO_b897OPJHCiYbhVRzouvLnVS1HBK8ducn_OFTz5u_S1LjVD1MM4KSY5oQZTSrtgEuK4eGxUI9YrLth8WRp3fP3W688_mUt8puEfqgF0HeLH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=ubfvCk01Hxxr2mYEjKx-IR7y9XG2m04YYbo-9dC5xsEHq1I7rTci1c9zavl3doXPr_52olmMlrcfDroWAdRft7p7rdCTFSGIA4LzgnsODpo_f7FRGdGWFK_uxXzFVU6CIaoclU037ce9knlieUoDnw4oVpooU8SX1E7T4MTf4ustA7a3rxQa6ROElMckrJn8RZNg3yxT39f4Qa79xksvoeJ4zds88YA7peZZ-0PIpsz92MKkL7EFwEzlG4wtASZcOz_hYBvNLwNx_iQ92G26TwWJCk0UJUEKhjqfPAtrnC7XXsMAO9Cm1M6mIzH-tLsXNlGL4b-kemTdX6YEExyI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=ubfvCk01Hxxr2mYEjKx-IR7y9XG2m04YYbo-9dC5xsEHq1I7rTci1c9zavl3doXPr_52olmMlrcfDroWAdRft7p7rdCTFSGIA4LzgnsODpo_f7FRGdGWFK_uxXzFVU6CIaoclU037ce9knlieUoDnw4oVpooU8SX1E7T4MTf4ustA7a3rxQa6ROElMckrJn8RZNg3yxT39f4Qa79xksvoeJ4zds88YA7peZZ-0PIpsz92MKkL7EFwEzlG4wtASZcOz_hYBvNLwNx_iQ92G26TwWJCk0UJUEKhjqfPAtrnC7XXsMAO9Cm1M6mIzH-tLsXNlGL4b-kemTdX6YEExyI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=t4UOOuxIuuEy5d_k9n-bjBrSj5AqUX01orI9of59DwPjf50pHDaBhwh6ckomn8sjcBWnxLkINB8B6zawamotXtX7cuWxLmg5iUS4mZm0D6qlZy_yXE8eeAK1ib9tjdHXMSCO3TkM96I6-Nfw-LEGcRGjF0dmGgmdYTLAJP9VYFzEm1oJ2lSkUJvv0Uxe6TowCQk4K_lSkEfp73LVuFmILsyLN8wHLx8x7PAvWOoJPGXhx0Mbh8oJfz4HEDpQ7FHXA6gs1vlxjFB0SM0KMUTWEBKeLFujXbQ0-eaMtNDYI8C4ZJvuQy3FQP6l0jM8IpP03XZqGHafJtpx0dSkC_kjfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=t4UOOuxIuuEy5d_k9n-bjBrSj5AqUX01orI9of59DwPjf50pHDaBhwh6ckomn8sjcBWnxLkINB8B6zawamotXtX7cuWxLmg5iUS4mZm0D6qlZy_yXE8eeAK1ib9tjdHXMSCO3TkM96I6-Nfw-LEGcRGjF0dmGgmdYTLAJP9VYFzEm1oJ2lSkUJvv0Uxe6TowCQk4K_lSkEfp73LVuFmILsyLN8wHLx8x7PAvWOoJPGXhx0Mbh8oJfz4HEDpQ7FHXA6gs1vlxjFB0SM0KMUTWEBKeLFujXbQ0-eaMtNDYI8C4ZJvuQy3FQP6l0jM8IpP03XZqGHafJtpx0dSkC_kjfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp3lgPkm1yfvZXbl765Q_W7MNKTdh3hJuxZwnasG2Mx7in8P-UFvWwm1g5CaheYmEWXE6gmAhnEVajYsGOm4xFYZH0u-NR5lOSzASxNUY4uTKJEVjWaZ0_m7DFqOrxRm1JDc5mq7UZQMqfwEyiLhDFeMZ0PZLefWclpCwayhhiyFr_sOoADJUgN9Gi-xuh9LjaPL0SGbHuaN5dEMmRkvD6KR71gzP_mA9284BG5zRbp0PpT9dQMvSlE_hl3js10mTtnsPRoioKERXldcWqS5opjZ5hIyEJbpH5HBHhMT3-1Pz79RnSk8k7UzIwxpUz36YBdUU3pWuDVKUzxtJf8Iig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv4WQPLw7SOQoSUcAtVEBYkQexSG4vkoRqRCLUBO_sY0esVqOt6hGJco-wNliDpe2uiuVww1105Du2FjlLS4TT4keWbNnRs4EoC3aakS3R9ul3wyEe403BGLRIatAsXi2AW3T_U-Zo6EVdEoVRvvFRuo67syqqTec2zEiO86bAL3fyrpQykh-hf7yTL8TwYaYufsqs34A3R1oqh04qvXpVPhLvZTxNH71SIZAdUFfg_SP_NGSVOnS4rlJy-p0MdZPANZIt2FD2_sSxcinq4MpxeutcU_q374Ul6RWB-JRXviM_qKWtNVAmC0ki3P93EJ2i7EiorJ8b4CBIO0s0rJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BRjWcX2yoj5PMr8s_RTwgXP_ZbQAGmgzjtBBMAAt6oh3biNas0GnOuTkze_CEqkEOJll9I45xHac3NVBScL9qtVCWfIOi6zxoffF5BjzqIsyLDjm7ETQMPPIY3YxddmNR8HFalkbR6aLdkSxk064dWUxjy4DlVTvbppIXwYtb6mjzNOJ8YT06nStySepKZitsX12TPnd2gkiOELhj3PxZmAja5nn_l3_KBZ8M2NTqBE0u3QfnqRXsxwm1KJS-Z6BSuehtkRXmcr3T2J0bz2JhtvQW26zHMvOYgrFNKjNyRaCZZpZcE-8rj8BQsWO6pHksY4DBMsDckqYzH2I5RxNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=bHm5fNtzYY8nKLQPzzFTY0ezLfvtz2WbqX2pYjCprX0Ros0MTfpnHYv3ykPlWXDxHNy9skXAcK37aZquSk4QESogpz-DaD8iYZZimJiZ1SsOwu5ZyZs4czQGSmm_uq5vcI0-AJaQlmQ1joOQrTAv9eEZIUNrxC_HWtzawiFLt5K0wfn10fck8fgg8SIKGkBaK-BXYdPv03mlECtefdHQ1teu3AAeSmXgC8bD55eRwB7jDBlkkE2-GgNiCLgi6iMkLH-wtRLbLPIzw0dYFJUkaM0XBD7NVUvKCpHA2VN0f2BfwxV7o8Bc0bsSs-LIThkg_ZxTSWIkI83ViSGluZnG3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=bHm5fNtzYY8nKLQPzzFTY0ezLfvtz2WbqX2pYjCprX0Ros0MTfpnHYv3ykPlWXDxHNy9skXAcK37aZquSk4QESogpz-DaD8iYZZimJiZ1SsOwu5ZyZs4czQGSmm_uq5vcI0-AJaQlmQ1joOQrTAv9eEZIUNrxC_HWtzawiFLt5K0wfn10fck8fgg8SIKGkBaK-BXYdPv03mlECtefdHQ1teu3AAeSmXgC8bD55eRwB7jDBlkkE2-GgNiCLgi6iMkLH-wtRLbLPIzw0dYFJUkaM0XBD7NVUvKCpHA2VN0f2BfwxV7o8Bc0bsSs-LIThkg_ZxTSWIkI83ViSGluZnG3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPvn7qwhOoisGQaN8ZxaKhBPcBhDOHoop18yHRO21l4ZIg8nk6k90Zs5pPzddNw9hkK8IKJ-7Qlwzaqn2gYDNn0QF4Vw_wvYxJtCq44YoI351xXeKAIOeTBlMvGhhA99m-lq8Hs5zAsT6lVXjgazzFrwWI_YmrB9dlvYU24fLBJNvM9mBGakkzccy4MHwJYVxOXIcl7ZWQ5twiQQBvfV7GxKfeZYWWXmLDhRAnvtMvaiG4ouPhiM6Y4cUkNGFotTXMnu42zb-Z8D2gdPrvorW8f8rPi9xTd31vMY71ZPXBvSPhF8PTiZwUr60rxWlrDEClL9k_fJmg8sJ6-4fkYVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=rojw7cpoAQGQPQrPbwsG5uUeBZoy9q-t-0JaR2GUugEGIOYc0Pr0UkfXkJB1dlezhN8gGhKVaFD_WS3iS9cE3nx_yhQ-g1Va5e9RglKau-B-rUt9-KMVUxilXJIQ7GU6nVCoG2aNX4IqkVLNBLukRujwEZpIwupMnmWV561hvBvVFkl31o-_O1Wm47oJXEZK5O5dhfJQCjMPVwM2We9xZAYoAC7lc89g7chdZb7tXYsfTSvqtjOuPvl4uKnDMbUHyxGNEwjbmJ5hUVp52YgNPurQIBmqM9xX_kvHxrZ3bhKKhWK4SborbArKzxPXUm-NIijpAIHbQ16L8irqThBQ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=rojw7cpoAQGQPQrPbwsG5uUeBZoy9q-t-0JaR2GUugEGIOYc0Pr0UkfXkJB1dlezhN8gGhKVaFD_WS3iS9cE3nx_yhQ-g1Va5e9RglKau-B-rUt9-KMVUxilXJIQ7GU6nVCoG2aNX4IqkVLNBLukRujwEZpIwupMnmWV561hvBvVFkl31o-_O1Wm47oJXEZK5O5dhfJQCjMPVwM2We9xZAYoAC7lc89g7chdZb7tXYsfTSvqtjOuPvl4uKnDMbUHyxGNEwjbmJ5hUVp52YgNPurQIBmqM9xX_kvHxrZ3bhKKhWK4SborbArKzxPXUm-NIijpAIHbQ16L8irqThBQ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=Fu1f-PqRCwGfGzVEWy1V64R6vvrB4RcjxLERGrHc3gY_Ej7qodAiycEdnOH2rw_8gjBFSycAXR4bSyc97T3wGGnbZrP1vOVyZZehUiib0UE36kO60BBoALJ_aymyLzCaNNoFwq3Pawxfw8IxRTmF4yuCye7JbQuuz4YaVPX8lnrvEyAMwebJb6MNupyn-YDEDsdu-KZMoiPHyx_3wSdHYWH6_4pWQxN5aF2S4DNPIsrrZteTap68_TCrAPorWL41flQ33eJTjnGJ8_ztJK3l5oq-2aiQCP6zyGrTOGnKWa5N92rHfa1NaTycXT6hPgyBZCkm0Zyvu6bngqYqzksciA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=Fu1f-PqRCwGfGzVEWy1V64R6vvrB4RcjxLERGrHc3gY_Ej7qodAiycEdnOH2rw_8gjBFSycAXR4bSyc97T3wGGnbZrP1vOVyZZehUiib0UE36kO60BBoALJ_aymyLzCaNNoFwq3Pawxfw8IxRTmF4yuCye7JbQuuz4YaVPX8lnrvEyAMwebJb6MNupyn-YDEDsdu-KZMoiPHyx_3wSdHYWH6_4pWQxN5aF2S4DNPIsrrZteTap68_TCrAPorWL41flQ33eJTjnGJ8_ztJK3l5oq-2aiQCP6zyGrTOGnKWa5N92rHfa1NaTycXT6hPgyBZCkm0Zyvu6bngqYqzksciA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=PcmkIc17MXpsslfBpAX5q_1JkOBeFbXHk_-T_NcBpOxhsj9jjfTRab5vN8p7-NXlgik0abWhNbQwgV5N3hBM9Wb7B39TxquiOet6RiBo2EpPvs7r2g-vzVoFAHqCONpj4mL8Fxc8U13uxdznomH8ZeB1FlEDz65tcGlvAAnVTKyaEhBmn-mKeBMF2lSni6WD6YV0K72tgA15KKo2lGkCCPm-vDFuDmASMS5MvhvE-U64BDQr8dR4igikNp6Mw3uRCJtW-AVPXbnIJYV6NuH81Rfc_aPW2ZD9kxP2fmUs9wpLg59yaR2pxWxySoa_ItyxeTk07MfXiImpfe3_OnIxsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=PcmkIc17MXpsslfBpAX5q_1JkOBeFbXHk_-T_NcBpOxhsj9jjfTRab5vN8p7-NXlgik0abWhNbQwgV5N3hBM9Wb7B39TxquiOet6RiBo2EpPvs7r2g-vzVoFAHqCONpj4mL8Fxc8U13uxdznomH8ZeB1FlEDz65tcGlvAAnVTKyaEhBmn-mKeBMF2lSni6WD6YV0K72tgA15KKo2lGkCCPm-vDFuDmASMS5MvhvE-U64BDQr8dR4igikNp6Mw3uRCJtW-AVPXbnIJYV6NuH81Rfc_aPW2ZD9kxP2fmUs9wpLg59yaR2pxWxySoa_ItyxeTk07MfXiImpfe3_OnIxsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=hROtft66NAEzl_J1DSS_KaTWeS_zNY46LbQuswUSGr3IEdQDLID-q4GpvK_hP6GQ1C9pJ_NPZobJAt5pvqauY-tARJ2GPfglEgSjKXulSIDcBh4KUVnFxVfNcXoqY97gZLGFGJfAu4_uDTl4Z9xMdWNto-vd3AE0L8VKwtIvue6kO2c7kHje2iFUXnP1dVJfIjiYbxaLQV6ccQSoXp8u_3auJos2EG-s4IJYuFtO7JofJwbOX3h2tnPX4BRR3uSVZJcFfh9IgIJmrdfBe5ZJltt8Io0o5zwPU32NcarDLfP3Rj9yoVOF9-024_sT8AhOqo2QhFDCIjtRbIHuTbHBqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=hROtft66NAEzl_J1DSS_KaTWeS_zNY46LbQuswUSGr3IEdQDLID-q4GpvK_hP6GQ1C9pJ_NPZobJAt5pvqauY-tARJ2GPfglEgSjKXulSIDcBh4KUVnFxVfNcXoqY97gZLGFGJfAu4_uDTl4Z9xMdWNto-vd3AE0L8VKwtIvue6kO2c7kHje2iFUXnP1dVJfIjiYbxaLQV6ccQSoXp8u_3auJos2EG-s4IJYuFtO7JofJwbOX3h2tnPX4BRR3uSVZJcFfh9IgIJmrdfBe5ZJltt8Io0o5zwPU32NcarDLfP3Rj9yoVOF9-024_sT8AhOqo2QhFDCIjtRbIHuTbHBqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=VSFE4vDM60TxV07T9YrG8RPvyfLW0_hFvKNTXh1dIIsdKadcYp_w7cjDwieSjRDefeahus2LN5yqidGSXtG19yTvHBedVX2Ua6fEy2ZXDde9oprost4GPqhQBiwRLCizVRSt54-8zx265cCH8JxLojEhxi5MbfzaLdWYGbGBhgslyHc-4Qf928AmLTu5OGT6z01LzMOSDfIWeCLT7rTsxRdKHosx_wJR1fZF-CWytqhE7S2MNV9-LjJdnToOP0DPWu3XHzQLDLkgCwUQ6ia400i0aKooQPYjBzqAbBaX_UqgyBaHo1rJxCMqS2o42MfY4i-cl3nGVuLKJAieZXb6vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=VSFE4vDM60TxV07T9YrG8RPvyfLW0_hFvKNTXh1dIIsdKadcYp_w7cjDwieSjRDefeahus2LN5yqidGSXtG19yTvHBedVX2Ua6fEy2ZXDde9oprost4GPqhQBiwRLCizVRSt54-8zx265cCH8JxLojEhxi5MbfzaLdWYGbGBhgslyHc-4Qf928AmLTu5OGT6z01LzMOSDfIWeCLT7rTsxRdKHosx_wJR1fZF-CWytqhE7S2MNV9-LjJdnToOP0DPWu3XHzQLDLkgCwUQ6ia400i0aKooQPYjBzqAbBaX_UqgyBaHo1rJxCMqS2o42MfY4i-cl3nGVuLKJAieZXb6vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtPOxavsklzW67SsEbcSx3gRDrAcyFyiZiea7vEWC5BwT5HH6eSbQDJ5XvG0HeEczBAj8FQajN0YWSUuRAHyL5PC5we84yACJc25FCa6H6Q7CY-rPeEZsOG_queX00_vUvfgns9ygCThNcUtNKduFpVlviIZco9ZWp12vnqT_WreSPT8iZJ0UCquqGzb1-0AhZFDitwOsCwmBjtBsncgI2CJcc4JyhNtiCWcg7dAeOFnM9ojcOIpVvl7f-0WmBFXmDpfUZclQfjgeB7FSvJAFOCrDipFAkdIbfnMvqRPpWdOHj5QPA5mXG8k1wOKfct9i-gYmq2UD_xqzD1YQGEWTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY6Cg-dAvUKMnVQsOBeB3U5-1VmQbsiXJDUEDZIApe7Tn8D42_lRhYwWW9Squgd4z2_80SQUWP1ClOA548WecKxMpiJvSrfaQQwmV6HlT0OGJkcoLIq9Oe3iaEtew3gkjHKbBaG5L5O8QxcU6TRx7_l0jj86RW6MQ87xc1qD-cjiZDlUIkgR2cqNIpJ4IRSX9quWulsfwZSRRBa2qJUFtypBW5LOsy7FET_PbRy8enA6xELtzYyCA06QpQSoxaTJov7BxXLajt3WxbRQw61LCdgGbmAk0DlavXCsLbXKu6uqZF1J9AnlHieOyTt2I8Gjo9Jicf2RA0wvV89ELqpaq5co" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY6Cg-dAvUKMnVQsOBeB3U5-1VmQbsiXJDUEDZIApe7Tn8D42_lRhYwWW9Squgd4z2_80SQUWP1ClOA548WecKxMpiJvSrfaQQwmV6HlT0OGJkcoLIq9Oe3iaEtew3gkjHKbBaG5L5O8QxcU6TRx7_l0jj86RW6MQ87xc1qD-cjiZDlUIkgR2cqNIpJ4IRSX9quWulsfwZSRRBa2qJUFtypBW5LOsy7FET_PbRy8enA6xELtzYyCA06QpQSoxaTJov7BxXLajt3WxbRQw61LCdgGbmAk0DlavXCsLbXKu6uqZF1J9AnlHieOyTt2I8Gjo9Jicf2RA0wvV89ELqpaq5co" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=qH3fYTll8R7n79K7NR1gpplU5pP4Y0X0kFM_hLAIV2O3NQzDT4pK-SUzS6IflPlxIThW89vPokroogY5OM3dkisGy1iXkOTmi1keY08I1Iy20n9Fme_4SVbbz0ninCT3Il4c4k5xeq-DNWCaA__nUVSEVOSNrNIWItkQzZPKm1MebhuQrqbTPUhEbHDv65Xp65I26xTCqh0Zzyg9HBfug5VeoEE_Uo86Qsfid2GclqEF3wiFK3Tko1jhP4BOnx4qE9g-G36eMFNDRTmmAqr1mZRC05mvB6QKBprOznAI52OrCPrR2cEp3MoQ3EgAAuZw64BCAXodYgSDyApHkb9m2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=qH3fYTll8R7n79K7NR1gpplU5pP4Y0X0kFM_hLAIV2O3NQzDT4pK-SUzS6IflPlxIThW89vPokroogY5OM3dkisGy1iXkOTmi1keY08I1Iy20n9Fme_4SVbbz0ninCT3Il4c4k5xeq-DNWCaA__nUVSEVOSNrNIWItkQzZPKm1MebhuQrqbTPUhEbHDv65Xp65I26xTCqh0Zzyg9HBfug5VeoEE_Uo86Qsfid2GclqEF3wiFK3Tko1jhP4BOnx4qE9g-G36eMFNDRTmmAqr1mZRC05mvB6QKBprOznAI52OrCPrR2cEp3MoQ3EgAAuZw64BCAXodYgSDyApHkb9m2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=jaC_2IxYSflThBQIjSLlD5B3tmcgaFFuNw8-ACY8eeDQJME2pRzI6qqli9dPD8SZdLYasmACTdEv3LIuv0Z1nrLWmd3Ge6IoTe1uUHINobHq0xD_0l70r-GIzXLwhWO079npXV8qzv9_xd_Z-jhKp_lX4IJsCzq_6-JM1rW4_N1tWh6EMLGoOFD-R0h_3YtZhEa95dvPP_Ct3Cq2Jsy4xu4OsVKS8VtByCyj7m_CC5MQ--atMSnpL9Y8pmzSK6gaUYdZVTGHRyroevblMybe9pnQtF1vsehyCvx7UwaPMtI3jVgg0sSwi5iakcP5zUvODTeIgJJ_ZwvNvMcwk9oPuZdRVpZJ8PmVXm1q3a1z83EdqlS7_lq3MFfkUMyAYbXNAGWYDCAqZQDb3gDO4kh4SkizFQGXzMnyvY7VCwFwghgzydlxaYCL2yVKC1OIfYj4xMANB0M-r77HL7xiaa32O8tmJhFon2XBUMPFvfICeq3pz3MSamBgwbcyITMefCSzeHWVb6wYLjL63w-YgwrMkzs5LF2u8G1Gh2a9c0nBRG9MReoTCLSin718RQPUwRTW6hhe3FwG1MRN3jbDdF1IvJ2wz9Mctl8vUuc1mwPgIPcF397C4rjVhWeFGshaS8YPjWjux4PHWtdYUm5Soz7gDsZwUy8lw_HDz2Okysk8HpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=jaC_2IxYSflThBQIjSLlD5B3tmcgaFFuNw8-ACY8eeDQJME2pRzI6qqli9dPD8SZdLYasmACTdEv3LIuv0Z1nrLWmd3Ge6IoTe1uUHINobHq0xD_0l70r-GIzXLwhWO079npXV8qzv9_xd_Z-jhKp_lX4IJsCzq_6-JM1rW4_N1tWh6EMLGoOFD-R0h_3YtZhEa95dvPP_Ct3Cq2Jsy4xu4OsVKS8VtByCyj7m_CC5MQ--atMSnpL9Y8pmzSK6gaUYdZVTGHRyroevblMybe9pnQtF1vsehyCvx7UwaPMtI3jVgg0sSwi5iakcP5zUvODTeIgJJ_ZwvNvMcwk9oPuZdRVpZJ8PmVXm1q3a1z83EdqlS7_lq3MFfkUMyAYbXNAGWYDCAqZQDb3gDO4kh4SkizFQGXzMnyvY7VCwFwghgzydlxaYCL2yVKC1OIfYj4xMANB0M-r77HL7xiaa32O8tmJhFon2XBUMPFvfICeq3pz3MSamBgwbcyITMefCSzeHWVb6wYLjL63w-YgwrMkzs5LF2u8G1Gh2a9c0nBRG9MReoTCLSin718RQPUwRTW6hhe3FwG1MRN3jbDdF1IvJ2wz9Mctl8vUuc1mwPgIPcF397C4rjVhWeFGshaS8YPjWjux4PHWtdYUm5Soz7gDsZwUy8lw_HDz2Okysk8HpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=LluAzrBKqK-JYKYhSONjcDD5QsoQYTqbagxncvkVQdgyfV8Oe7ggNGFVSG6-FRNIkcNEyX7sEODCi1tVDTu1dmkEpoijb8FV3V2uwoeXqQwwphp7qc251ZvgaMaXVwPlb9_jJOKpYmNJBdWIuA2_GY5OoYNReBazYsa7Q91l3kmCSk25livvNB8CoHzkibg7Uytq2TCdOVVxRpwWwH34QSGqqetX0Syr3zIr5ueLHnz59C0Kp1le-pdzBjNiZz8GyX5HuyivPTtQt2I0I6VywoeYhdvyukUL2BXn9nrocJxGvtOFTOeqF7-iNy2sI8lvSNWh4TXsAbTAXAmYz4eqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=LluAzrBKqK-JYKYhSONjcDD5QsoQYTqbagxncvkVQdgyfV8Oe7ggNGFVSG6-FRNIkcNEyX7sEODCi1tVDTu1dmkEpoijb8FV3V2uwoeXqQwwphp7qc251ZvgaMaXVwPlb9_jJOKpYmNJBdWIuA2_GY5OoYNReBazYsa7Q91l3kmCSk25livvNB8CoHzkibg7Uytq2TCdOVVxRpwWwH34QSGqqetX0Syr3zIr5ueLHnz59C0Kp1le-pdzBjNiZz8GyX5HuyivPTtQt2I0I6VywoeYhdvyukUL2BXn9nrocJxGvtOFTOeqF7-iNy2sI8lvSNWh4TXsAbTAXAmYz4eqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=i46om6PHINR5nOh1_hT4_KXl8CiV6891CD4UNnPEIlbUSZyDVU0qybyaHY0l4JSMThQeNv9ikQ3G11ZiJW57WhlPgnxvwDUJjRBSaqJ41oKr0lj8PggYoIu5dd1hN2kK8qdtSVbOV1gWEy77-QVF-bI_R6MnJUUAua3AqubKnieIvws1aqx6xyimPuw6MDXGf9K17YTlJbyoClHPcMnwJzD-o4om4DloxXoIfD_jtkltshqGX_MU3VF7YzwVYDh2FIWhgV8fp4KLmgoYqKTGkJyMVKD432nx6jZ-DuAFUnpi6VMtGZRftZiKc7IyKsrhqJLKstiO1mW3ryLmCrxDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=i46om6PHINR5nOh1_hT4_KXl8CiV6891CD4UNnPEIlbUSZyDVU0qybyaHY0l4JSMThQeNv9ikQ3G11ZiJW57WhlPgnxvwDUJjRBSaqJ41oKr0lj8PggYoIu5dd1hN2kK8qdtSVbOV1gWEy77-QVF-bI_R6MnJUUAua3AqubKnieIvws1aqx6xyimPuw6MDXGf9K17YTlJbyoClHPcMnwJzD-o4om4DloxXoIfD_jtkltshqGX_MU3VF7YzwVYDh2FIWhgV8fp4KLmgoYqKTGkJyMVKD432nx6jZ-DuAFUnpi6VMtGZRftZiKc7IyKsrhqJLKstiO1mW3ryLmCrxDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=DcamX8gxBkt-M0PxlHil09nPdwRyyWW2u344d74ZcdmX7iDtBcxHc--t8P1xR6X6iZZJ4Kg4HcxHtSy12bqC6pO3VpQObqc80zeGo4oVq2HDecln9nQ1UEyCuuZDtXDqy9KzZObCILIPuVKCREV7z0cz_nT6Bq91S6ub8KnBni-dfhyIKLsG5mjZGXmKqqr3X04e5On7SVWEaDKPJYq2gZiU4jVHfajq8l9Av1ULeQX8oducFumdTa8sCGK4-F4pKGFg_D_256D0vl2R3boIRbBsXqQXwtLVqoydQb7mHmsUbmlHPa8-TOmAA2njjzpsSHbfJazF8YrtUfguxMC9Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=DcamX8gxBkt-M0PxlHil09nPdwRyyWW2u344d74ZcdmX7iDtBcxHc--t8P1xR6X6iZZJ4Kg4HcxHtSy12bqC6pO3VpQObqc80zeGo4oVq2HDecln9nQ1UEyCuuZDtXDqy9KzZObCILIPuVKCREV7z0cz_nT6Bq91S6ub8KnBni-dfhyIKLsG5mjZGXmKqqr3X04e5On7SVWEaDKPJYq2gZiU4jVHfajq8l9Av1ULeQX8oducFumdTa8sCGK4-F4pKGFg_D_256D0vl2R3boIRbBsXqQXwtLVqoydQb7mHmsUbmlHPa8-TOmAA2njjzpsSHbfJazF8YrtUfguxMC9Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j93DYvVihQTjSVowAOZj4FyC1U-4aOp3woCfD4wlKIkKSsFERRF1igJONzy5jsrjON6TbBy8Oq4ql9WE1cwoJbTHWDzKD1Jo3rn-u1QXoUpzFDD9hnKECEnIS1vInokV6tjhEEnLU6F-Ik1d59WSJyTzK2jPHPdg-tgQtlXSmtoI9aSpRXEA16d8vyHCb4dS2_ZObjjA1J1VnBk5a4vCK1PDO_CzojXGMcuyz2mDrJwVJ-lpHFg1OCRdXCD7H2Uz2XckCJAyQmUYIZPWFGvPOKtyEmARB5vmrRWmWZRbdzza682CJ--WJsHoumRFYlktU1Cd-MPtXS-EpaiEFTrcMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YBeKSZy3-mp799sTjteRj1EMQ80VI7U7Md3Vf4GIbGBppyoyuD1u6c5gZrMcp9Haa_wafc6iAw1f7N42Vvi60Wf85Ywt9zNS8FcQ1JvH4QcmWwdhyd_Zg-WNIGZAj3O1_VqzGuJbzf8UVGCSOQDGnjhTg5FIt1rQnupitO3qzW0NiOM10F7cDF2Bs9Fpje6WbJF_miv-GyU3UQ_EoHIDzI1tpqEoMq9GeV0Uxo7rR372gnLymRJg3ypMP9nlR1i5srofgfuGQybU4W1U7q9724mUUhrW2ul1wjD4J8mSePQ7y5_PpnqUYM49kVJPs_jCBoCryMVYGyXm5mK000ZU8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awiqqbUI1JJK1ucyPCbgC6QjVjZquNgzMID77zA-0qGGtji0KCk2EIk0TPZnW2NANVe_pXBfkmXMagqd4Euu22DY5bg1dmK7bbAQh_YVXpvjvtbBYJAaJxsndiyVCnkvDJiFao_1rZ6l4YsgSE9YrwI3V5QcMuuxGVuM9jEvBx4MxCUwBhuK1-7XqZfTn0DOa9BozDlI-KR_QcxgTLiUd34E0Z_ZRHNe8j7XYkANvr8MC7dUW9vgtcIy4CIUe-l9LXXLemRXtzU854XTcXMqNQuXq3b_0vX119uk-NgLYRSzjZRIXn6j4vCv3BwHIqtgfV0byXGEJCyMbhg0uggiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLaUtgC2QcZ7khRuse35a1n3DIvX9fkN8I0uUN3pdUBf-VJNEDpbTMpJdY-ni8L_wVYGuu7N5_C1jFiue-m9gMMZqZuMbxypz7mEyGHC1M9x-lrI93AGyatc-dQItKGzCYfg0MRECBsHXeDCEhN1XLRrsrj7Ud6pW4dGh2zl59oOt-isuKHqjnXZLIWD4sNsH5uQVKC5DStcRziDi7FH_i8DHntIi75E7skad0P2inzVWRJMBZhy1Zg3A702UNs3JWNIPaFQFvSnkETMFnYAv1vE9Q6FiQKxJEIsbAHSMTmuJWJsaJXdolj-RuWt936dthPsMX-kyYfnGebaYZjyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJjVciPbDpoxPVBIojzVA0qoOvdWAgn5t8AFburDAHbQJ4e-Wf6qGCj08HvdBHmTRS7Sv20qxF_CD4MznLSZl90Tn_-DQ9ZWdEHmlt5XmvC5ifKz70ennfoHWbZueUxanS9WlVEQXjI-YFi4bj0zMOvC7DtX6BOoJ6jKJE8nuD7Sl5IOVN_c7rVJ_Xrk70I3rAkul6T4xRWlS5LpF6fVPzPLQgmVSACuYBLLjNa0iK_s5xhruFRVHmuw7a48iQM9ONyhes0x3NQWbdJ4iik1i_1KCD-ZuJy6FOsonUC4fZPhB3sEKumWKS558X7XAU3TVHibiC2bN8NoIqY7irNzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIBcWXLaEEZpPHrYt_kTubINW89RQMpWItbvky8l1lsLdDhhXjm4lx8daTzH9QK4_fsUjQAiywV31yHBMuHMRI9_a8Y9-30aSX3Vi-Jk4NJ8Z2rAAXh-GjWyqfjlzBBA50pft31slXPfSp14QbL0EUloMKG9sVoFRfeNZkWeADCXLK2RlTmW77RJF2xifRNHPmJlGLzOkje358G1KzVe-roldXJo8hCzqWK4opNuQyjQZIX_G8qP3kiGBAHIjlHBckBBf6_ZPQOqdJPuhdnzVtUG1UTp8IBemUQTUWEvPZGCOntsECwLtNmYsmE2jJ_b-smFxN3GPJMVmpbMwPT73w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=PZNDtIXNmcZOcd3Dsd-E7UQRQnK63uIuq5LgmZnBHDvlA6W-xsCyOIDqt39NZpQIC6N0FFWBTh2n3YNyyhEGwUtpQ6n1hD7rmwqQgHeSLYzeDhPSg7vt2Mh_kstygTsqnGXNmTeIbpgx_ZGUA34DMda6m9VFswMXJwq8P4pM5nU6EYl_2P5HmQr_VgC3-hWgnnvXd7KPhvEQ63c5dtwVTel_4Cg0nFnUp7wqh1_LtSC77Oigt7BU9IDGM-pX3nK677hddwcix_gdAm0fGmIoXD5VxTn9cWPk1OPYJsYOaFKr_MfHh1oShI0C_6PPD_BVjRpXdn3nPgEINDf-lrjvNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=PZNDtIXNmcZOcd3Dsd-E7UQRQnK63uIuq5LgmZnBHDvlA6W-xsCyOIDqt39NZpQIC6N0FFWBTh2n3YNyyhEGwUtpQ6n1hD7rmwqQgHeSLYzeDhPSg7vt2Mh_kstygTsqnGXNmTeIbpgx_ZGUA34DMda6m9VFswMXJwq8P4pM5nU6EYl_2P5HmQr_VgC3-hWgnnvXd7KPhvEQ63c5dtwVTel_4Cg0nFnUp7wqh1_LtSC77Oigt7BU9IDGM-pX3nK677hddwcix_gdAm0fGmIoXD5VxTn9cWPk1OPYJsYOaFKr_MfHh1oShI0C_6PPD_BVjRpXdn3nPgEINDf-lrjvNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=BVQ31ue0m1oOANd_AFAZg36wpzPS7qI_vNBU-FdzPoXuLUcZ9SeL9SnvZxVlVlpq8_e6DLLvQ_xdKnayKgryK0GekKYdt7CdfJg9Q3TnpL2uM0p4yw18LFVFyc_4ORGWw1uVv2sxQlOQX4Sm9twXSKblBG3bABrSw_PwPCbCo3XtPFo4Gqsjana5exFO4ubvLbBuxO1HUGEfnkMfBJrV3NInc5yw9bHk9ANDYBMSRRfMTJ6N7YseeCKzJKTAq5YV_j1JfZjbQTn-jFz8OeQGm4YrGAmoOtSX9u_7vYrF3WyxWr8CvOgHN_QOXEdvjHtg-neTKyqZ5kDo8EQaxKN7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=BVQ31ue0m1oOANd_AFAZg36wpzPS7qI_vNBU-FdzPoXuLUcZ9SeL9SnvZxVlVlpq8_e6DLLvQ_xdKnayKgryK0GekKYdt7CdfJg9Q3TnpL2uM0p4yw18LFVFyc_4ORGWw1uVv2sxQlOQX4Sm9twXSKblBG3bABrSw_PwPCbCo3XtPFo4Gqsjana5exFO4ubvLbBuxO1HUGEfnkMfBJrV3NInc5yw9bHk9ANDYBMSRRfMTJ6N7YseeCKzJKTAq5YV_j1JfZjbQTn-jFz8OeQGm4YrGAmoOtSX9u_7vYrF3WyxWr8CvOgHN_QOXEdvjHtg-neTKyqZ5kDo8EQaxKN7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jpj5NTlhl4jUyKpDMwA4HyxE15y1cv4mFp-IdzGulMoKda2XTB9H6nK6NfOms9IzXR6R5Yw9ug3uzGfxBijAbwACUZ2c8bacpojaF-4okjQroEiUKCN12WjXPFC71-kIT52Tvhwsz25goir8J4-x2GHnc2l4-gXumTLkI9_8NDMxCz5NyNI1qaoyMrqcZZKLzov3GhqGHH84W6AZqAlhFgxPpT_rkQn5HEI96KSQeBEwpg4chTt-z-SUP5sXVEJgz3IqV7Ut0M10iL1wbvuvhEXrLoBv9Q5TuFFtDg7QTteM8kbXx6HphBy2h3IajIeKEa_4g8t6phg6BO_0yASDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnw2lFU8aKzRKd_icHduT-YzUFk-jUIwXm3XwBrPPXW_566w8f76uRgkDf1rZ7PU3qxJhOxhH56j62YbZHjjUWf6mERQnqEigeyRUjCIn6VXajMw2p0lJusEutxiUeAf_a4aCdvS5C7GQZQ4RIhw_UMb4I_sO0-2XK1xwnNl0gc-JRJe4evCTSNYfS244drByVx0nS8PkRBC_L9o6nTiZpYDJTVSJPFaS6dFzWtdXF5ff-RgBgnTfKTQra8RbCAGikTqokIqxRRTFFQWfLI2UQWg9ca0RitNPhmSNgw99lmIzLiiF6B3t20Fet3utBlf4NrPr2nbRAKE5tJV6aAirw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=CU1zDsOvmnaNhVsQBMDjoY3BFCUBnz-gVG_sHxBOXNYKGZbznCRt4v6H6GV0wBW0M88K1PFLywmVYA4T8HWtYNDELv_D45WWk5Y8T4apCM-57jBxdqW4F1sBZDtepyoHRCEbvTxW5AfeN-LvRrN_RTPkkVPaw_3cwI7_d19MsfhoHGWsQ5UkhHrqpteTSVd7eDoVpJQsTnwvfxTh4n6JQhqqWY4qiR3Qyz_jps41m52pp5MDkCISQ5vYqRG_J59s-JR2dNkNYp8QV91P_ousDs1Zt-GCpmSt367zqoWz3vLjRam7EdCVVok8Y4nkm5BX7-z-lfSogKbQ97k129TE9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=CU1zDsOvmnaNhVsQBMDjoY3BFCUBnz-gVG_sHxBOXNYKGZbznCRt4v6H6GV0wBW0M88K1PFLywmVYA4T8HWtYNDELv_D45WWk5Y8T4apCM-57jBxdqW4F1sBZDtepyoHRCEbvTxW5AfeN-LvRrN_RTPkkVPaw_3cwI7_d19MsfhoHGWsQ5UkhHrqpteTSVd7eDoVpJQsTnwvfxTh4n6JQhqqWY4qiR3Qyz_jps41m52pp5MDkCISQ5vYqRG_J59s-JR2dNkNYp8QV91P_ousDs1Zt-GCpmSt367zqoWz3vLjRam7EdCVVok8Y4nkm5BX7-z-lfSogKbQ97k129TE9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=vZI4j3hDxi13OBK30gRJ0UTSNWIlyNLqwS8z5SQuqNn41kL_swL_TqSPF2pYtrrTTW6V4L27_2iE91sQHHA1rLT50IAXmZz2xwN-F_EdR1P9RUwg-qQg_Y3ghAYayBhSvDG98dI1fZ0_MxmyvmsbvNseXIl3lUBgdgvBZie-PTfPPQ7VczL2mTIlP9SeiEaDvd2NyBBZdyJzfiOhR092bmoIqtb_-HMwv1wIWLIfZr8TFOANAq3y95LmT3YBApi_gDHmrfBo6Tsj4z-BLikktG6chwbAT-YrFChrbF5lXfEy23EKiTm0Hr-mQwTip8tKoDvQGu8W4S9oxsyC1xWZNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=vZI4j3hDxi13OBK30gRJ0UTSNWIlyNLqwS8z5SQuqNn41kL_swL_TqSPF2pYtrrTTW6V4L27_2iE91sQHHA1rLT50IAXmZz2xwN-F_EdR1P9RUwg-qQg_Y3ghAYayBhSvDG98dI1fZ0_MxmyvmsbvNseXIl3lUBgdgvBZie-PTfPPQ7VczL2mTIlP9SeiEaDvd2NyBBZdyJzfiOhR092bmoIqtb_-HMwv1wIWLIfZr8TFOANAq3y95LmT3YBApi_gDHmrfBo6Tsj4z-BLikktG6chwbAT-YrFChrbF5lXfEy23EKiTm0Hr-mQwTip8tKoDvQGu8W4S9oxsyC1xWZNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=F4SwauCPE09pc9Ihuoh0bNbwKkjajmHLH59R3_ZnqP-caqtDjXL_AeT4V93bLLRU7Z5awiTrBq8F3t4mEc8cDuFNT7-yosWids68LI7jukpwfAtgwckdLS95vfhMJQoQRz_JqwaygcptOyFpGG7-alU-iOSBsdPl6qlxQB4FTIiFU3WJcxw1gA10WTGBNOd2-WjwEgzKYTd-2H2W1htmP1ye3bF-xW7MHLOX3QwqQUnoRglO5TXKbj_NAKkwWJV8mKeDLrsXwBI0gqly23YNsKZRBE8yqap3-7o5QQWNS7eu_ukxJ2N-O99UBU6Rn2UiS2N7xsww19MbLC303NdD_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=F4SwauCPE09pc9Ihuoh0bNbwKkjajmHLH59R3_ZnqP-caqtDjXL_AeT4V93bLLRU7Z5awiTrBq8F3t4mEc8cDuFNT7-yosWids68LI7jukpwfAtgwckdLS95vfhMJQoQRz_JqwaygcptOyFpGG7-alU-iOSBsdPl6qlxQB4FTIiFU3WJcxw1gA10WTGBNOd2-WjwEgzKYTd-2H2W1htmP1ye3bF-xW7MHLOX3QwqQUnoRglO5TXKbj_NAKkwWJV8mKeDLrsXwBI0gqly23YNsKZRBE8yqap3-7o5QQWNS7eu_ukxJ2N-O99UBU6Rn2UiS2N7xsww19MbLC303NdD_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=hUt-MUGRDpd_pnkG1TveHHdojXTRFj4a3LvTD6tidNgWKf7gegEXNWAOBw9xlyU37EL8AfrPZCGzVNkiwq0vaIgmxiBnBEt_Ip7kE2zZFHlG-Ske1_ugRvd-_uzDUhCFxrdmZUQDvdO8zgcTcak7dLOtIY_APzlR__RpfJD6MgWtuQyuPic9kA-QkYlk7qvlOQEEeIeAb1nud_gMAMZulkJFOU4sGnIAYF8T3QMDJLxSS87BPwPgRlfELOn5iUklVGG9HcheglccadVcbwO0Qf9Ew-N33KinKEYIeW32Dvtkb0gJEcpJ4QwBhi20Lkn-3ZDL7lQjKhxIWiQLKq9OirxA_NBc96BZ_fFEoeBfKAFTIXFTxeZAKZ01eRVKBss8yb55g99TCpgq9fDXEWMmedPTO4QLB7FrrMfxnAH9Xoni5TRnXVSkQPJLD5mXV8t_x_4GeRj8jkT3nRg45MqwR5BCm_YusPZwY99_SPER2MHkQWEyQ1XwGa1fnzfMr8xizleU4wYi3IdVKqo1J67JFj24QEgAg_Cjta-28bplO8VQaLbotKGoIOtqSDcP_iZANlpAbhmfHDr4NBiGKB-OcZy5X1q4PDPWqyFKtMhwqEaIVBKFBTW2N87MqFOc3TkXQ0qhO_glX5sp3QFDuVndQucB22fnjAE6HDlqvt26htA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=hUt-MUGRDpd_pnkG1TveHHdojXTRFj4a3LvTD6tidNgWKf7gegEXNWAOBw9xlyU37EL8AfrPZCGzVNkiwq0vaIgmxiBnBEt_Ip7kE2zZFHlG-Ske1_ugRvd-_uzDUhCFxrdmZUQDvdO8zgcTcak7dLOtIY_APzlR__RpfJD6MgWtuQyuPic9kA-QkYlk7qvlOQEEeIeAb1nud_gMAMZulkJFOU4sGnIAYF8T3QMDJLxSS87BPwPgRlfELOn5iUklVGG9HcheglccadVcbwO0Qf9Ew-N33KinKEYIeW32Dvtkb0gJEcpJ4QwBhi20Lkn-3ZDL7lQjKhxIWiQLKq9OirxA_NBc96BZ_fFEoeBfKAFTIXFTxeZAKZ01eRVKBss8yb55g99TCpgq9fDXEWMmedPTO4QLB7FrrMfxnAH9Xoni5TRnXVSkQPJLD5mXV8t_x_4GeRj8jkT3nRg45MqwR5BCm_YusPZwY99_SPER2MHkQWEyQ1XwGa1fnzfMr8xizleU4wYi3IdVKqo1J67JFj24QEgAg_Cjta-28bplO8VQaLbotKGoIOtqSDcP_iZANlpAbhmfHDr4NBiGKB-OcZy5X1q4PDPWqyFKtMhwqEaIVBKFBTW2N87MqFOc3TkXQ0qhO_glX5sp3QFDuVndQucB22fnjAE6HDlqvt26htA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=pK94VHM28cPVJLvA07mL8ofskvFu9AtRMS_XpErvV5ZBKaT14adWiUX8t_YM5W4CFd6FawpNYG9pg2n1KFgtgJuhXGM6684vk_Dmpdcrd1H0oPNMlu7gbed1r0zG0psIseT0cHc0vzks3-cxfZrThePQO7euEI1kt-UbnfiljpMlwr_7kl1UfxUKFIULs61o0eYe2m-ju6K5vC6pN3b1xNwgZr0UwEzCX-Am6aD3m_gwdrbXf3LqOdtcXGmJNKYGYfVm5qr8eTRaINAkqXw3PKUMLW3ovYwPAejGrlDgSZ5q0QJtMS1LoPvhAPoJx8gydp8aV1w5MTdpUWZFbWM306Gu-VJvO_9SrzuIz5PaZOWlrZ94QTY2NV1FEyeMaBQYkMH1uPQX9ko4XtHdt26HIKXm12S4QAgFSlRponL1YAAjE5i9_OnH_bhHYnQ9Jq9eM1iONcgmlUQiU_gaUmr8MOTTn923MEbwweJYjx-mWhHwoeENd3hEIyLvP6knV3s506repkBp8-StUXQ1DzxwDVihXgU1cwWLF23rW-ci1kH4iOQd8HQJ0gOMcPFtorr14AY1g6lUz35Y5rx2Fe0RgysZBgBRaebTf2MxIWSP8veWU85LMWHADuPnRBx_OGSxi0pmPmrQyqagbaaMXI5ivnU5o7v1mwbhBVm4yVAObms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=pK94VHM28cPVJLvA07mL8ofskvFu9AtRMS_XpErvV5ZBKaT14adWiUX8t_YM5W4CFd6FawpNYG9pg2n1KFgtgJuhXGM6684vk_Dmpdcrd1H0oPNMlu7gbed1r0zG0psIseT0cHc0vzks3-cxfZrThePQO7euEI1kt-UbnfiljpMlwr_7kl1UfxUKFIULs61o0eYe2m-ju6K5vC6pN3b1xNwgZr0UwEzCX-Am6aD3m_gwdrbXf3LqOdtcXGmJNKYGYfVm5qr8eTRaINAkqXw3PKUMLW3ovYwPAejGrlDgSZ5q0QJtMS1LoPvhAPoJx8gydp8aV1w5MTdpUWZFbWM306Gu-VJvO_9SrzuIz5PaZOWlrZ94QTY2NV1FEyeMaBQYkMH1uPQX9ko4XtHdt26HIKXm12S4QAgFSlRponL1YAAjE5i9_OnH_bhHYnQ9Jq9eM1iONcgmlUQiU_gaUmr8MOTTn923MEbwweJYjx-mWhHwoeENd3hEIyLvP6knV3s506repkBp8-StUXQ1DzxwDVihXgU1cwWLF23rW-ci1kH4iOQd8HQJ0gOMcPFtorr14AY1g6lUz35Y5rx2Fe0RgysZBgBRaebTf2MxIWSP8veWU85LMWHADuPnRBx_OGSxi0pmPmrQyqagbaaMXI5ivnU5o7v1mwbhBVm4yVAObms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=s8pIorOGioo-uK5VajH7Hj8LSrjIIz-9y9ISqE5oKYZ1LLkcLdzuOcsxY3FasiRfZrDs_PJo13PgdMS_dAQhwR_NXkc9-tXuHYlj_zbXCKo-CNuGUZ8GhDf7_0PFMLzHPCvKFOyLNfhHblFCMoSgbmN9oZW1WjZKTJfcMYpue3FZDcPROwNuqnN_as8ukopUo3Zpnxiavf7hLdShsBC4Gqo2EVCTV7b7NLqemEDI5nVDLkB7yu4hhrXVCfN-m3GaCZQPZLoQrPxAU_IPDk9TkLb-KIkoEdmgd1m8zgmpr4b9a-3gI-KVjL-9SAp_HqQm2Vat1p80ScG-PhSJveFzng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=s8pIorOGioo-uK5VajH7Hj8LSrjIIz-9y9ISqE5oKYZ1LLkcLdzuOcsxY3FasiRfZrDs_PJo13PgdMS_dAQhwR_NXkc9-tXuHYlj_zbXCKo-CNuGUZ8GhDf7_0PFMLzHPCvKFOyLNfhHblFCMoSgbmN9oZW1WjZKTJfcMYpue3FZDcPROwNuqnN_as8ukopUo3Zpnxiavf7hLdShsBC4Gqo2EVCTV7b7NLqemEDI5nVDLkB7yu4hhrXVCfN-m3GaCZQPZLoQrPxAU_IPDk9TkLb-KIkoEdmgd1m8zgmpr4b9a-3gI-KVjL-9SAp_HqQm2Vat1p80ScG-PhSJveFzng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
