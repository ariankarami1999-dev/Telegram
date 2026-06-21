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
<img src="https://cdn4.telesco.pe/file/SiN9eppKdy9R1kn8dBFFCnM8_cvFJs8HQu-8gEu3qkDx-yCd-lG79BXgGKubec4y05PqcldMyA-n4hXF1KmzpJX_BtSKPNe1XIg9FUxTWdinNI2Io8goKbbJBTPExYwYe_BtW813Yqn1xxs04jSLE626k2GR-sQ9ktsHSkh6yeKGdIHlr00kVGAaZa6Fk99g0HmQ19GcZA8WY8b0_Nt53TTwZjOIjhe2WrMIzt2W-8pHKbJZBrxuX4vratI0b2R-C7ZeD8mfWrziI_JXXCMx-DHzvL4WyQTJiGE2O2gvfpF0-Ikr-b2jwOKMs8XW3_lew2YgakyGvziXKnFCSmms1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 221K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 14:21:26</div>
<hr>

<div class="tg-post" id="msg-66600">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:هیچ محدودیتی برای سربازان ارتش اسرائیل که برای رفع تهدیدها در لبنان فعالیت می‌کنند، وجود نداشته و در حال حاضر نیز وجود ندارد.»
پس از حمله به نیروهای ما، ارتش اسرائیل با قدرت زیادی پاسخ داد و تعداد زیادی از تروریست‌های حزب‌الله را از بین برد و به زیرساخت‌های تروریستی متعددی حمله کرد.
حفاظت از جان سربازان و شهروندان ما بالاترین و مطلق‌ترین اولویت ماست.
تمام دستاوردهای ارتش اسرائیل در عملیات لبنان حفظ می‌شود و نیروهای ما در منطقه امنیتی در امتداد خط زرد در لبنان مستقر شده و از آنجا علیه تروریست‌ها و زیرساخت‌های تروریستی عملیات انجام می‌دهند.
آتش‌بس اعلام شده دیروز، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که از جوامع شمال اسرائیل محافظت می‌کند، باقی می‌گذارد.
همانطور که من و بنیامین نتانیاهو، نخست‌وزیر، روشن کرده‌ایم: اسرائیل از منطقه امنیتی لبنان عقب‌نشینی نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/news_hut/66600" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66599">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🇮🇷
پرزیدنت پزشکیان:
«از حق غنی‌سازی خود دست نمیکشیم»
@News_Hut</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/news_hut/66599" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66598">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=pcdXKMRTLhGqVtlLTfi2AUBpAUMXOhNtIwVc2ALN0Sj4b35H6CsRD3SDjWui8MfldFSo5xOgC0C5aHlunDY8A7VbZhvX7nEjJsx1fvRSv8Q4wDWIlp5GAQROhCJlubKQUZkEk0GKNWOMnHLolkcTaFBd54q3olG2D9ukgyRRAMVdHB58OrO3CQNlLR65swujOaosvc2YWJNPZTJMhVwVzweDfSSFaYMD1Zxil5t4k26QCnHHJDxFvnNqDYl6Uq0qAZkV7eOCpALqAjbUz142ZXH4NRVLnAD5h9EBfX0Oiw8U7K1xgtYK5Tbb5QwH_0D82KgtnVo2axkV2J77rQDuOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=pcdXKMRTLhGqVtlLTfi2AUBpAUMXOhNtIwVc2ALN0Sj4b35H6CsRD3SDjWui8MfldFSo5xOgC0C5aHlunDY8A7VbZhvX7nEjJsx1fvRSv8Q4wDWIlp5GAQROhCJlubKQUZkEk0GKNWOMnHLolkcTaFBd54q3olG2D9ukgyRRAMVdHB58OrO3CQNlLR65swujOaosvc2YWJNPZTJMhVwVzweDfSSFaYMD1Zxil5t4k26QCnHHJDxFvnNqDYl6Uq0qAZkV7eOCpALqAjbUz142ZXH4NRVLnAD5h9EBfX0Oiw8U7K1xgtYK5Tbb5QwH_0D82KgtnVo2axkV2J77rQDuOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار هیئت آمریکایی و پاکستانی
@News_Hut</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/news_hut/66598" target="_blank">📅 13:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66597">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=NyC4oFkEwF9ugK5dpEgrHhSZ6ShDiS_wRbUU-Yhe5n0-3MjJekJHH3urBin65N6RNIjJb2iydhe1lSfm-yQQYUNG3_Uho8pmkhgZh6yYEufy3FusG_bhryIS5Uncb3nUKxiUtneQJPfyM6f2AY7R4_gZeOT8TVcUTSd-p6GCwgVjP-zynV5mr5iyVOGjF_oow-Rd9aPXLS2AwjuAPamzZqKoHp8_e_GBmehUBGZGnRk0n0yYKGn36iTCIlvff0kFSWiWUmDIIM6Mgcmu8MpdE7p03NHkr6PtB4-cnBgbV-PrglU0xtkEmNbJFUGdwemB_2Za5vwi7R3mgpyMXUjnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=NyC4oFkEwF9ugK5dpEgrHhSZ6ShDiS_wRbUU-Yhe5n0-3MjJekJHH3urBin65N6RNIjJb2iydhe1lSfm-yQQYUNG3_Uho8pmkhgZh6yYEufy3FusG_bhryIS5Uncb3nUKxiUtneQJPfyM6f2AY7R4_gZeOT8TVcUTSd-p6GCwgVjP-zynV5mr5iyVOGjF_oow-Rd9aPXLS2AwjuAPamzZqKoHp8_e_GBmehUBGZGnRk0n0yYKGn36iTCIlvff0kFSWiWUmDIIM6Mgcmu8MpdE7p03NHkr6PtB4-cnBgbV-PrglU0xtkEmNbJFUGdwemB_2Za5vwi7R3mgpyMXUjnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم مذاکره کننده جمهوری اسلامی در محل مذاکرات:
@News_Hut</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/news_hut/66597" target="_blank">📅 13:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66596">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=oh3st9RosS9g-daQaYNKu8qDvZdBj2I2gu64zmRP8SlPk--S2zCA2_RqC-dJyadmDPV6gO19vJzYzHwxiVAlDgshVASAvgkJ9IWSeHgHTgxDKjO6J0o1TnNb7rTLiSsQPNlVVy8nHqNOLDYfdT67Mg-67IoBNSGrl1fWrd5o8mubQBK5enJUvsWhiQn94uLLrW1J0afFiYZxK6LIt434mo17QzPmSG4-CQupbRlpoS9iqgSRxxf8IDZehaLd3Ewut-u8YE6vEvnUi6zouvzyZJ5RFocYBFTv26FS22zyHm9H4T8iqwgIdNdtIlnyvop3gzwbWQQci72H1pRzGxgpgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=oh3st9RosS9g-daQaYNKu8qDvZdBj2I2gu64zmRP8SlPk--S2zCA2_RqC-dJyadmDPV6gO19vJzYzHwxiVAlDgshVASAvgkJ9IWSeHgHTgxDKjO6J0o1TnNb7rTLiSsQPNlVVy8nHqNOLDYfdT67Mg-67IoBNSGrl1fWrd5o8mubQBK5enJUvsWhiQn94uLLrW1J0afFiYZxK6LIt434mo17QzPmSG4-CQupbRlpoS9iqgSRxxf8IDZehaLd3Ewut-u8YE6vEvnUi6zouvzyZJ5RFocYBFTv26FS22zyHm9H4T8iqwgIdNdtIlnyvop3gzwbWQQci72H1pRzGxgpgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند چینی وارداتی
😔
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66596" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66595">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Dqu6rmzFtUgsmzumGdT311Uhm_6l728QTlo2dARcW7TSVhhEp2mtnnOsrVNQt74rJPmtlqxbcI9w4A98VO9kBloCiKo2IWRCz-hWPy_vBN5hfwdV9diGKwktVbFhnTzUz8yGtEjItF7r09r0dLLG3iuKTzYqbnxdIzDhLRBsbvLHdr0fUakKrcSNrxkP0lLU95IkVcmrnE7bH6Rn_TnTgtDYEL_lKZA7rg7smGXso2rLUuQ2IkaGAUvPZPvso2Fh20LlxJ7T-4_RAMZPKclcJRSvJLjKQTlnaVptZv-dYsVS7StZ83q2sY6nYD8WqvEkW-XtVKj1i9vTBxJ0S62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند. اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفاده دشمن قرار می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66595" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gor1Vh9vu5RrJ-gAr4gQIaXwJXzbv2VyFUtzhxxP4Mw7WRzt2XosKqNSa2LTIYjpysv2Qp4uRpeByktiFM0ouzWjpOKK_v_gV0fsxiPK1FuYVb3OLcJYWN8Cm4z5wqK5l9aRsZV506pdATZh4_PN60zV_WUfq7GtvHddkNPCnbgOCipFUO02gkC3-otP6HfhBt7YzkA50DbTiuaiytR89yYaYr2FRjxunkh_3f4YSip2Quw9NSaJWjGp2Ndc2I0FfWww414zRuf9u0GKYf4cWX3F1HYTIMmeP_wqPWTt6z3ZwWd7gWTnSa-qmy-QOzxSXX8Oz_CY-H0bEQKk4WK-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=qtcG7baG2hK37R25IMR6bV_xQFJ5wGXUbqcf_AJgmlz5fBww3HVDqATsQDEgehyHpLDPxlNVg3MBGMFiEpRRXwjyueM_dWjMRvQVxb09hZyEfU4qfT6sRuhwdWcKV8TgemBGbonx_symwaNBcB9CFDapciLnAbuAoNjDjt3OjoXdxhtmj_b96PM0zOb4o4h00MObXFnvw2OeHpfapSCmNFVMRgKBHn81R6rnQ3E-BdyNhh_SskQz-ATmng_GbqOqI3pEGYN4TZ9gAjoQ2yKfI9vj779f_RGQ__2MZVTxTcPSs5AM-aUGpzSx9kUwD4D7hRoZiRz6O7ytS-ySuaR3fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=qtcG7baG2hK37R25IMR6bV_xQFJ5wGXUbqcf_AJgmlz5fBww3HVDqATsQDEgehyHpLDPxlNVg3MBGMFiEpRRXwjyueM_dWjMRvQVxb09hZyEfU4qfT6sRuhwdWcKV8TgemBGbonx_symwaNBcB9CFDapciLnAbuAoNjDjt3OjoXdxhtmj_b96PM0zOb4o4h00MObXFnvw2OeHpfapSCmNFVMRgKBHn81R6rnQ3E-BdyNhh_SskQz-ATmng_GbqOqI3pEGYN4TZ9gAjoQ2yKfI9vj779f_RGQ__2MZVTxTcPSs5AM-aUGpzSx9kUwD4D7hRoZiRz6O7ytS-ySuaR3fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رشته کوه علی طاهر، دژ استراتژیک حزب الله در جنوب لبنان:
طبق نشریات این سازمان، در زیر آن، تأسیسات «عماد ۴» - شبکه ای از تونل ها، انبارهای موشک و مقر جبهه جنوبی حزب الله - قرار دارد.
یک افسر ارشد ارتش اسرائیل فاش کرد که عملیات روز جمعه، افشای یک شبکه زیرزمینی حزب‌الله بود. ارتش اسراییل این تونل را محاصره کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/66593" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VauJLf2UYjW6NoVVBHie_-FOVMcjUF6e2SRRjUwOBCgmtNJvLAos1vcCf6lkMIP-dmFwU9x2ykLXDq5_Kjt0S5QWjad1AjtmsWfppNRpqCjMN2Z5WjgrbAO74Rl92hZfUjVXzJyA3g55wVlp8poTtrYw8a6hZmNB3cz0vJqCEVl0BHMMj1drlYnTe4fTchPlibMf9TbE0DSUT5VVzG1VzXcbfxSQl0n9Zaa5nviD3M3vdvNt9Pe5OE_inOBXVP9PDEPIFDPqm4YV7oAESDiEB5NWejGG7GDvbLJRP-UdUMORuSo0Ww6qJMXuyKPSvfRzegHG67m4KcwYRO6o2s_voA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پس از وقفه‌ای بیش از یک ماه، صادرات نفت خام از جزیره خارک از سر گرفته شده است.
تصاویر ماهواره‌ای دو نفتکش بزرگ را در پایانه صادراتی نشان می‌دهد که نشان می‌دهد محموله‌های نفت خام ایران بار دیگر در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66592" target="_blank">📅 11:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66591">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از جام جهانی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/66591" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66590">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxume8HH2NNDee5-mJYJRAFdz5U4f8Y6oguPqhqwKZvxbzrJK4NSY8oGBVTxSMgiv2ToE1GYUnIH3bW-uScpfWB1vaz28lXMdKvYncDjrmvMRPEdiNJR7b1Fc1-tfsSpI3MIp0eVVCP8R8OBPI5H4ES6-aorSIKdDP8SsQzLfoEVPa10-3f5bQP2PLgL1JJ7nv6W4bee-8YOXB2TMwA2TlAzySAqL3dNV2Ipref9zDvpLtYf_U6je_W0evaDbJsyKrKqccig-1JWaPCFhJ_-hwYjfvXsmud2U4iqQ9Y3fSp6n-HNrJBSAgwSV43jroyJikCzunMm2nKZFnk3QzSgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاونت راهبردی پزشکیان :
تجمع کنندگان بهداشت روانی جامعه را برهم زدند  تجمعات باید بعد از تشییع رهبر جمع شود.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66590" target="_blank">📅 10:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66589">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
منابع پاکستانی:
عاصم منیر فرمانده ارتش پاکستان وارد سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66589" target="_blank">📅 09:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66588">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=XA9GMEeTgDpvQ3VGxPpyGCQrrGvTTgGNMpJknhZc2NTUKzMvRoHR7xrstZ0yTGeK1CWqxd54OdmxfvWxzyGmc_YXL1nAzHkQxHWiwABhFDK74vZZWX4GXns3znpHXU72NBlprC8hucI__4FIf46aCKTy4MPiwzxcvvxUu2C_fOruCDM1SligYl37k9orA5IvxMvGR9GQhA3tk75uovr3uUxm-cWJXG6t8QzcGaT6ArxeZoCXwOFpPB2nQ1L8yDEWhaUYSFl8Wbw08cgO8aSGNYzz_2IRRJqZ4_dVt7-mSJJUr9Pec6q589fZHYCG2FtoqxP2pe6eQ3TYeNp9edN_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=XA9GMEeTgDpvQ3VGxPpyGCQrrGvTTgGNMpJknhZc2NTUKzMvRoHR7xrstZ0yTGeK1CWqxd54OdmxfvWxzyGmc_YXL1nAzHkQxHWiwABhFDK74vZZWX4GXns3znpHXU72NBlprC8hucI__4FIf46aCKTy4MPiwzxcvvxUu2C_fOruCDM1SligYl37k9orA5IvxMvGR9GQhA3tk75uovr3uUxm-cWJXG6t8QzcGaT6ArxeZoCXwOFpPB2nQ1L8yDEWhaUYSFl8Wbw08cgO8aSGNYzz_2IRRJqZ4_dVt7-mSJJUr9Pec6q589fZHYCG2FtoqxP2pe6eQ3TYeNp9edN_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صدا و سیما:
علاوه بر تنگه باید فرودگاه مهرآباد رو هم ببندیم تا مسئولین برا مذاکره نرن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66588" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66587">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خودزنی مداح وسط هیئت:
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66587" target="_blank">📅 09:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66586">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66586" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66585">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q3oZaR4IoC_eTCmLJQ8eL4COrulmtxfhhkrSt-ue9dHhipCxJguObXCt-p9jgNyseTV-Nx4Hr8AgLEHfwqhWpjoqDttWpE3JWfDxh7-y56dWuUX2FP6i8hMZT-dufDc58BBYRvHHdS2X0HwHEtg3LcHgsPDEvyQQWHYzeSE4LpcmyKst184e8yruE2KLSS5ZIsNKs1pZ9OQ8jJdScnz5IacJycbD6_UEdnmYGqNtqT6ohCV1HCzISVK1iTacf2oEq9QVR8JfpVNRYLy9V5C8nN11mN_mMQ6iesECwRldOsCb3ahaCJz2wFFMshnRKx1TJuZX0EBHtCApYarG0DVrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66585" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66584">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K22jwwDldbwtS0slQbKl3JK7R-HKhOMBITUppR8GIb4N6FjPq6LA0QrvL2PwsBthKouqgjfC0bV1v8h0jNzux4d2wjpMFl-4bkrIA5lW94QegcCYcexfzRrEGnQbZHVzX0JpkT-5nQs9H3VHvRhBEVXAURgdFctnJzqthIW2e0p4brXBaUA2gtit8x9xJmBCzbbAzxtwgp1VkgkkDCfBpRvEY1fNnl3TFYgF3TINY8N5wdauP1QcHl-8R55M-d5c4GZ0ianioa3EQZ_fyDxi2M5LA3aUex6UM7A9r4-iZ4m9lDhjyaah0CBdymJNNtBbHjpz4GKOe_wS7wONcJHXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف بعداز ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66584" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66583">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=l8KoUBG-1rZskEZnoPvOCnKZY2Yf9i31bjGY71V4IBFAWyOpLfj2fxJpMdT87_oY04ew4COBPy2tI231kbv4FOa7H6EFLEocivhDgU3S4i1nlD3czQlzVco7IYnmj73eIJVAvOlb3Km6m9DDOJ9ohciVbC6CkIuaF91jTlcprryvH83RLLXpCpqoBdBDVe9iOzxd4C_p7wrSza-ysuaTPdv-YzgjRTIXwhBMZGN_BTVT6P20jiQQ98P1-H0iAYNCVvrNPK6Ji5J2-qntcWfvfcKw9l-ChnJIFyCRfr7gR59-n0OhcLIRbPhgC-_VocOTczxc9pNjTTSdyhDJZ6SIuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=l8KoUBG-1rZskEZnoPvOCnKZY2Yf9i31bjGY71V4IBFAWyOpLfj2fxJpMdT87_oY04ew4COBPy2tI231kbv4FOa7H6EFLEocivhDgU3S4i1nlD3czQlzVco7IYnmj73eIJVAvOlb3Km6m9DDOJ9ohciVbC6CkIuaF91jTlcprryvH83RLLXpCpqoBdBDVe9iOzxd4C_p7wrSza-ysuaTPdv-YzgjRTIXwhBMZGN_BTVT6P20jiQQ98P1-H0iAYNCVvrNPK6Ji5J2-qntcWfvfcKw9l-ChnJIFyCRfr7gR59-n0OhcLIRbPhgC-_VocOTczxc9pNjTTSdyhDJZ6SIuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی‌ونس معاون رئیس جمهور آمریکا برای شرکت در مذاکرات با ایران عازم سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66583" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66582">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDvExEj6VyEL5MQn1yCKVV6x1fr744oWSmzzRmKISzQWR25outQK05LGQKSsmt06C8LtvzJQVNY321hlCZvss6NicRHTlF7H9TiS2znZ_v_MFWuT7J9oZZn2YNhqyRgLaFkHiZzJaDLi25tJLC82uwiC-jUqOaIwBHtqRnQ8oAo5JsLIkUXWJNW9nCKrh5sA2EUMjTlYTt8wNqQEW8mdmUJ5YoRmXGSBi27PwBhnzpg5cEPijD8QacO1zQIGq8OhLZP8BBi-fgUMlVuZLcQcGb6sVc3FEkARxqx4M-6ZTEIx7QiBahuWvWdcJ5RqQImmOilyQsmEBK1qC-Bzm5Z9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مرندی عضو تیم مذاکره‌کننده خطاب به ترامپ که گفته بود هیچ هزینه ای در تنگه هرمز نیست نوشته:
«هزینه ای وجود خواهد داشت این قطعی است»
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66582" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66581">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666063795.mp4?token=d-tvcjSb541OjzLWNl_Wq9yv2oSG5SnFUsJDwZKl0vSWw5fS0vFhYt1ZsehRHVCuRuGkzrrAMSNq2FUJOOyqYDtfNrK7WTRR2SQd3SBqpXjoDkiVv3NW1uiYSwdVukIwvKtZpR-cIamz_ka1oFrvOegrrBCFCIcoQ68DrYFzOdmUWQuKtMPq3gqoQgzEOEm-LMxFjdLd3EWRf2iJk3fcFk9Tdgr8zziTLH4JAJeq8FSiWBHmkgsRMEk8M5Fjq6KP1WFAyvz6s6qhVu2YGGwn7iBDLZNH2zA8mJhOVaLluUjIIMfYgWqrmHZpfTOhvaT1utRjWN8KYorteJyA9WXPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666063795.mp4?token=d-tvcjSb541OjzLWNl_Wq9yv2oSG5SnFUsJDwZKl0vSWw5fS0vFhYt1ZsehRHVCuRuGkzrrAMSNq2FUJOOyqYDtfNrK7WTRR2SQd3SBqpXjoDkiVv3NW1uiYSwdVukIwvKtZpR-cIamz_ka1oFrvOegrrBCFCIcoQ68DrYFzOdmUWQuKtMPq3gqoQgzEOEm-LMxFjdLd3EWRf2iJk3fcFk9Tdgr8zziTLH4JAJeq8FSiWBHmkgsRMEk8M5Fjq6KP1WFAyvz6s6qhVu2YGGwn7iBDLZNH2zA8mJhOVaLluUjIIMfYgWqrmHZpfTOhvaT1utRjWN8KYorteJyA9WXPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری که در شبکه‌های اجتماعی منتشر شده، برگه‌ای تبلیغاتی را نشان می‌دهد که گفته می‌شود به سپاه تروریستی پاسداران تعلق دارد و در آن برای اعزام نیروی داوطلب به لبنان و همکاری با گروه تروریستی حزب‌الله، حقوق ماهانه هزار دلاری وعده داده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66581" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66580">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود. از توجه شما به این موضوع متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66580" target="_blank">📅 23:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66579">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=YsJNtsijSH5HsjAAX-vphUBD_zABDgOHlEghH6fJsx3uUZs5Nf_kcQuIBD0dDADFXos65cx1FYdTcrwOK32eYO-P_Diby5479BKkuSDbZDH4twB9fMaYWzhFWXeRhutxJ7jy1LtcTM7p1YdMambz0rXaSIc8bM1e6tXx0oq_6fDUNEgNcYeQNZcyI7AoJlLlRNA97FFLlRyE_vOyd8-larRf7ohfHZSojYexi3H-xcW3-qFo1WTyXV_a2PbfFbHuxqzrefDOXsZwufaGaRi76-NUw3mTGD_Wh1ReiRU4LR5cq3L1RWnItugAVJ1YQobARNMu9hV1zx_gavpVIYqYew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=YsJNtsijSH5HsjAAX-vphUBD_zABDgOHlEghH6fJsx3uUZs5Nf_kcQuIBD0dDADFXos65cx1FYdTcrwOK32eYO-P_Diby5479BKkuSDbZDH4twB9fMaYWzhFWXeRhutxJ7jy1LtcTM7p1YdMambz0rXaSIc8bM1e6tXx0oq_6fDUNEgNcYeQNZcyI7AoJlLlRNA97FFLlRyE_vOyd8-larRf7ohfHZSojYexi3H-xcW3-qFo1WTyXV_a2PbfFbHuxqzrefDOXsZwufaGaRi76-NUw3mTGD_Wh1ReiRU4LR5cq3L1RWnItugAVJ1YQobARNMu9hV1zx_gavpVIYqYew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
جدید: مقامات آمریکایی ادعاهای سپاه پاسداران ایران مبنی بر بستن تنگه هرمز به دلیل تنش‌های جاری بین اسرائیل و لبنان را رد می‌کنند.
یک مقام ارشد به فاکس نیوز می‌گوید که ایران نمی‌تواند تنگه هرمز را ببندد زیرا "آنها آن را کنترل نمی‌کنند" و به حجم بالای کشتی‌هایی که اکنون از این آبراه حیاتی عبور می‌کنند اشاره می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66579" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66578">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSnpa98KyGB-cmBn0jxxy-fnpLHLABBScCSL0A9NKbhh21EJPmCqgkPpd7g9tmnNW0d5lgBpVSUcbMYVYs2ZWWkB-Cs8mFBWBbmiRfqQm4uXLkb8O9Jlaoq8XMqDVlR8Lxb1vEZLz9rvuSGTTAtpX33ya8ktP6Vhw5JX5H0W3_1QqsLq_QF2ekbXWbhEstSH8phpsRMYjs-dz5cVSP5KGm9k7jUDpFbgSs3MIJVt8Yh13Jtm_M8oIjHi04jVzlYD3X30eC819GbOk0gVlco9KN9GVVR7tT3kELXxZz-zCtc-wfXTsYBHS1wYO3K9OY1P_lSojfyIcTH0mL-UUrnnm5xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSnpa98KyGB-cmBn0jxxy-fnpLHLABBScCSL0A9NKbhh21EJPmCqgkPpd7g9tmnNW0d5lgBpVSUcbMYVYs2ZWWkB-Cs8mFBWBbmiRfqQm4uXLkb8O9Jlaoq8XMqDVlR8Lxb1vEZLz9rvuSGTTAtpX33ya8ktP6Vhw5JX5H0W3_1QqsLq_QF2ekbXWbhEstSH8phpsRMYjs-dz5cVSP5KGm9k7jUDpFbgSs3MIJVt8Yh13Jtm_M8oIjHi04jVzlYD3X30eC819GbOk0gVlco9KN9GVVR7tT3kELXxZz-zCtc-wfXTsYBHS1wYO3K9OY1P_lSojfyIcTH0mL-UUrnnm5xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره با ترامپ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66577">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=CePrtrtQgtLbPQdtMA9QZHK6VW2rbdznqX6I4F6vWYkovoNXlE2SFven_kOgrCr9oyPUcO2yj3VL5Elso7Uhum4NycGcRMmHa39CGqQgfyjjw0jvLRZlNc6mGHtV6eP73yMuJJ-XY2sjg4lxYOBWlvGTFpl_CbtW4N2JzPqAN2NAEw-k1ZD8QgaONjKA82xsJRYXCwPMHXC43VaafZVPGhv4jzY7xfV-Nont8sJ9tyr2F3WfmVMfDvF4lBdtrA4bZg47LDDPH8DV2XnWigOBWvyQdxbEJGnQjiMGFLcn6Q3laGk237nCaBTOE97QTC7-jCJQzNFkCAXh80AE3DJ-ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=CePrtrtQgtLbPQdtMA9QZHK6VW2rbdznqX6I4F6vWYkovoNXlE2SFven_kOgrCr9oyPUcO2yj3VL5Elso7Uhum4NycGcRMmHa39CGqQgfyjjw0jvLRZlNc6mGHtV6eP73yMuJJ-XY2sjg4lxYOBWlvGTFpl_CbtW4N2JzPqAN2NAEw-k1ZD8QgaONjKA82xsJRYXCwPMHXC43VaafZVPGhv4jzY7xfV-Nont8sJ9tyr2F3WfmVMfDvF4lBdtrA4bZg47LDDPH8DV2XnWigOBWvyQdxbEJGnQjiMGFLcn6Q3laGk237nCaBTOE97QTC7-jCJQzNFkCAXh80AE3DJ-ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرار موفق یک کامیون روسی از پهباد اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66577" target="_blank">📅 21:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66576">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
منابع پاکستانی به الجزیره:
نخست وزیر و فرمانده ارتش ریاست هیئت پاکستانی را بر عهده خواهند داشت و برای تسهیل مذاکرات تلاش خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66576" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAlqS6TVlzidGu31QOSJ4Ef151VC2lwZHfyHM6ueoraJ0bdQD2jXTIW7Zo9W8d442JEWmSm6yagfgZ2begJmQgQG5qbJQOpwD5S-8QrVATWBJNV_N5_eXWELLKbmqkHzqpzgQgVwGsoma_7MQzIVj03jIF2nUHEYstEseYVP27t1hll66aBH6rAQfVzad6tF-kyoXQ_xuQOB_b-19590ef-OpB20DJwzkUinkDwi05QRNvvJ9AVZSyZkMaKJEyEXKtHEi3hJjUJoG9P4YseFQoBJfr1h-JZtaQ1glnCxb2o4klYkSP5XpU_wjF2BTcqSGV5_5opWaaELQKQMNkGE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8349099df3.mp4?token=cv1a6MCfHZIdY99mrp_z7HdIkhKoV1iSSJzRw37KGCHluv0-1b5fR4kfAwppZZBgICzbnY0F8xktWjQf9vkod0i2j8-t5GnxgfePqYUv24hXzNnsVhIMekKn8UqFVWnucBbNzjMLg1yAL6GSvMVKwhNju3ldsYcfuTyjH9FerzdCJ5-CGdd_f8NR6J1CwKmd9dcBMMCY9Q-vFxYcfF03Q2wnpcW-NUFbe3IE6ePjbA6qh1e2qFlUlCxE5Zt98W2t7pbAxq7XZuHI0bs9gspdLAX57dJCfp1A5HJpHPCaqfkgCgL_DsDpaI7uA8zClmXvqluk_QIRb68PSw2UwlvZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8349099df3.mp4?token=cv1a6MCfHZIdY99mrp_z7HdIkhKoV1iSSJzRw37KGCHluv0-1b5fR4kfAwppZZBgICzbnY0F8xktWjQf9vkod0i2j8-t5GnxgfePqYUv24hXzNnsVhIMekKn8UqFVWnucBbNzjMLg1yAL6GSvMVKwhNju3ldsYcfuTyjH9FerzdCJ5-CGdd_f8NR6J1CwKmd9dcBMMCY9Q-vFxYcfF03Q2wnpcW-NUFbe3IE6ePjbA6qh1e2qFlUlCxE5Zt98W2t7pbAxq7XZuHI0bs9gspdLAX57dJCfp1A5HJpHPCaqfkgCgL_DsDpaI7uA8zClmXvqluk_QIRb68PSw2UwlvZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
امروز در شبکه خبر در مورد چرایی مخالفت رهبری با تفاهم یادداشت ایران و آمریکا مشغول بیان دیدگاه رهبری بودم که به صورت ناقص رها شد. بخش مهم آن بررسی متن یادداشت تفاهم بود که علت مخالفت رهبری را بیشتر آشکار می کرده است. انشاالله خداوند ما را در پیروی از رهبری عزیز ثابت قدم نگهدارد.
«ویدیو هم از لحظه ای هست که آنتن از نبویان گرفته شد»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66574" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66573" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy42qJ0DmWjONP1OqEcJ3nq_e7A_2Iz5ccP24BhetHLHiZ-yQaKkSo31q7n4htGlTAr8OA6eIHuLAmnCPSwRvpt7_xljfLwAg2CdX9honVhvVwULvBoCsFPOVuZl8BW14nPhkYDqeDwlceqfpTrYs2kdf5F04uoqH7RlLf_8L80OIzlFCzB7TT87Kn2uVq9RY4lR-NIXrsWzh6UZWfSj7acqpDDcOSqMYZFOlzN5-o8QFpmFHN0myIAn3AAzY4yuuELRv0_SeD2AKX8ipop-Oh_t_F2w_qmhzi1EQBGZVTgUMPyLSv50jsS8CI1_LVhtKtgVaCVD1xX6FbRnaSWGOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66572" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
‏به رغم اعلان اخیر سپاه پاسداران ایران مبنی بر بستن مجدد تنگه هرمز، فرماندهی مرکزی نیروهای آمریکا «سنتکام» اعلام کرد تردد کشتی های تجاری در تنگه هرمز امروز افزایش یافته و ۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت به سلامت از این مسیر عبور کردند.
مرکز اطلاعات دریایی مشترک (JMIC) نیز با صدور بیانیه ای بر تأمین امنیت کامل این آبراه بین المللی تاکید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66571" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66570">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBwQeke6WcUGJDk-3I6ozpJCYTW8lp8xwx5TT5zSfKvEKPEqQD8P_dzt8nXkzk072fCItvlqCGcEDE-f6zst52qtzvot_8aRTn6mKWPxjsh__go_vw3-IJiYuIwrMxxA_H7SZtqXXCVrq0GX3vZ9jaa_nG3pY3GjZiU1qxcM0okoukvyfpdx-FLFPApfmIfRKq7l7DdqmaWJuU2ncxBxaq9h335HcHMBkj5-5MY7e9NHoDnYca-StczzlgAIyWOZtc_megsOvTQXEvB3QLewIWa-zt4UpM3PceqbfEwg2nf_jRHlXEZPow8dDQ3y8MgqiDZLDEGKS1rOSk-z9xMptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
جی‌دی‌ونس برای شرکت در مذاکرات فردا با ایران به سوئیس سفر خواهد کرد.
قالیباف رئیس مجلس نیز در این مذاکرات حضور دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66570" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66568">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmUg4D_b8jfdyILYtmqnoYQrDDI5ou7cbGF86Cj3OR3bU3m3bw-oLwqeXX-KrmadbWcv9IY0Wncf9SgmYEyZXgeXOSfNXMAYRnibA0i5-OqtAjLEt_KQB5fkOWYzaR0KvxCWQUZcFGSmHzq5htJoN6h7YzeOWaiL20hfibGFGqTCgFmDLG-pwMZXF2UxUnXSiMzrA0ec3mvWTn_CBG-eW_oFhYihOPijF6CfU8uS7Ox8KgSNHh-V3v0gm21nWQKZuNhGMnB-LApxJlELy9P-QxLjfQ9FjJkokwvciIxmf8zVLi1fAXRXL_xMzSZhCwq7PQwX2HcKLLrZ3qVHBV0l1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=S7m73mfCwPps0UOHiTb_QDvAwPn6PiB7oYukvd-gUyMa7dZnJH2PVDAfhHJRjeEwIUXP0fGBKL3jqw-tmt09Roib9C6QXp0xPUxGEg77PbNs-jFc2mMQ347BdPpGFNwThxu1CtXfEaPs2bNFzjIa-EzW-I0MO9xO0ST8HqhmkffuFzMPfXOMpJ5Hse_eaxeCYhSiJWn9es3YklHrKqRTbv0R0gGY9QkXUiIi2Or9O_ZnUzL80RFrZ5FslxafqQ2VqnPr2trYJLUWaT2T0hP8QZ6qj0h7LHPuuSYubZAbmfXmx1YpTR2JVNcsg_rEjiH3XOQhbpk0ikbHmwydpGPEsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=S7m73mfCwPps0UOHiTb_QDvAwPn6PiB7oYukvd-gUyMa7dZnJH2PVDAfhHJRjeEwIUXP0fGBKL3jqw-tmt09Roib9C6QXp0xPUxGEg77PbNs-jFc2mMQ347BdPpGFNwThxu1CtXfEaPs2bNFzjIa-EzW-I0MO9xO0ST8HqhmkffuFzMPfXOMpJ5Hse_eaxeCYhSiJWn9es3YklHrKqRTbv0R0gGY9QkXUiIi2Or9O_ZnUzL80RFrZ5FslxafqQ2VqnPr2trYJLUWaT2T0hP8QZ6qj0h7LHPuuSYubZAbmfXmx1YpTR2JVNcsg_rEjiH3XOQhbpk0ikbHmwydpGPEsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏پهپادهای دوربرد اوکراینی پالایشگاه نفت تیومن (آنتی‌پینسکی) روسیه در غرب سیبری را در فاصله بیش از 2000 کیلومتری از مرز هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66568" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66567">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhJd55tlqNxuZ7fdyyjH6CZjhuo7nh6DAbq4pTdoWAgzJ3Q3Yjpx1lBlfjs08Qe1S7YC91Ler5HBMwoEWcKep4l-THrlPVni1-jT8F_ifRf16WwFnG10DvbAu5uRz7-vrWxRSVSY6ReChQLnZ0LmqHQ-rvM4fAaY17-RN0k5dp8fDsJAu_EATCB7Km24qgZO2QASdsoeN0-hF2GHvZno_kcWT2MrmjHYy1ILeRdAA2IOjpD1pQKfqX7zP9wxq0RyQemeifgJXN0Z2aKb5bEFtVYVvf_o4Nrq63SXndh69M7t8kjy1sBL0ugta18Qp5QeSttc28LMBsC4P9H9WrJpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛الجزیره به نقل از کانال ۱۲اسرائیل:
نتانیاهو و کاتز به ارتش اسرائیل دستور دادند بدون عقب‌نشینی از مناطق تحت کنترل خود در جنوب لبنان، آتش‌بس برقرار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66567" target="_blank">📅 18:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66566">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUGVl9CLfy37So5sqBBMYbxXLuD9sCzFw6LinaXl-7w3ouprur9EyLxezhCtXSUdbfg2oUjplZ_X0oHAvAtz1UzvIPu9WAmjRLpr3If-1vgdT3-E_4zWN36eSe3jfMstchkkL8s9XV7U0cjWFdnAAM1UhsnFRJ6zPfF6Shy97y5dznAhdujuoQ8Lu3WgE5-8sFyI-JwjQ4CirCk1_OhiMJbEHRmYUIaZ0DDT-qs2V-W7zMeZ8HPlQF0FM8xPoRQnyHYw7q6qwa3qMmYFe_drpJ4nP7UnMvqFvfzHsXY_jRqLs7N2JS1gEdv6msV0803FjUb91Q_PZx-eJJCM9k9lPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی عضو تیم مذاکره کننده:
جبهه‌های نظامی و دیپلماتیک دست در دست هم کار می‌کنند. تفاهم‌نامه باید سریع و به طور کامل اجرا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66566" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBcm8SPMk6yZLjfsypx_jOBo_-wxLLUP7FK9vbQcUQQsSkpA7XL8j2a9l1IFPnwPizpKgX7rdYUqRvnYgh4baEI7KDT06ZtlzSh_Mf8lR7vs1Q3NZexZuB_BfAhqmhcm7li4IX66loHg2_5jtFdInq7zLWPq8JXipyp2Bcyc-K_488TD27FVvDRzEqYMkYDl9pOnevPzl9HzXGsBwqT_r5hzeIP_u1Jfc31NWU0LEMwKyc0YSigR3_dVl8MnrWdktStcqJrhqP7aQtg8NYvBOt2-gzXBK0xklJiL36gh_97koSM_LC-DdOeKElrtSR_ORiFt6h60HDHDVa_E_pO_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
بقایی سخنگوی وزارت خارجه:
ما به تعهدات خود پایبند بودیم ولی طرف مقابل به تعهدات خود در موضوع آتش‌بس در لبنان عمل نکرده است
-طرف مقابل موظف بوده اسرائیل را وادار به آتش‌بس کند اما این اقدام را انجام نداده است
-اگر طرف مقابل از ایفای تعهد خود سرباز بزند، ایران نیز مقابله به مثل خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66561" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66560">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e32956668.mp4?token=C6GYF2mFf8rGM7bb-t-_F9Ooe2zhlua9pBWf6bsV5dVgI5MwKn5rdAbx8t8ye8NtKxejel1tKQrz8WT5Z295nvBPx8FAm1JdXqKPqwX45PmWJ7323waOKaozMnbn3RuI7GaxVj3OdaMz61bdk91gP7xDzxqEy7jriDtvMePTl9HQypQ5PulGwKit9qxXeeq7WJlVM_BgTSqBL4MzVSCpbqsgwhpUCZM0oxQGtxoRT0zCdbyFjQEh8_h5I1I3SoWoIjtTVTTD9D2QPW0KodQMzCxOsHLDNPYz8g2oL3PLVwQvO7RG4HOTc9CJGq72o8Cg5YIVUGVTutnBKUnZyOFcvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e32956668.mp4?token=C6GYF2mFf8rGM7bb-t-_F9Ooe2zhlua9pBWf6bsV5dVgI5MwKn5rdAbx8t8ye8NtKxejel1tKQrz8WT5Z295nvBPx8FAm1JdXqKPqwX45PmWJ7323waOKaozMnbn3RuI7GaxVj3OdaMz61bdk91gP7xDzxqEy7jriDtvMePTl9HQypQ5PulGwKit9qxXeeq7WJlVM_BgTSqBL4MzVSCpbqsgwhpUCZM0oxQGtxoRT0zCdbyFjQEh8_h5I1I3SoWoIjtTVTTD9D2QPW0KodQMzCxOsHLDNPYz8g2oL3PLVwQvO7RG4HOTc9CJGq72o8Cg5YIVUGVTutnBKUnZyOFcvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چه قیافه‌هاییه که ساختین
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=liA5TZoGDz04Hq-vy6rpoNJIiuXVIZ2lCwGWbSkPIatWvaLuRDl1zLEl8OgypInRtDbxIbTclsTZt7cUbnqW0bTlVIa8He5C132DJxNyA9R_kz74EvU-07VthQzhD6KsNIv2pXu4b_U-lRweahPqFY2W4ZUmOLT-fn74_MbNwyNfXVgT5uSr-BMYGS2oeZfM1C1rqBwdKTV9zH-j7pVm5jZJ4mjCDQapc6U7vguC18ao4hF_Yaun8MPWeNdg5SKBJOfERmzItIPEvYh1Hq37Dye_6RTqokJbzplxsCrEBPQn87q2GiBmRK9RMVwqkO5Zhu4u-0rnoFW3Ze2AqOSkPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=liA5TZoGDz04Hq-vy6rpoNJIiuXVIZ2lCwGWbSkPIatWvaLuRDl1zLEl8OgypInRtDbxIbTclsTZt7cUbnqW0bTlVIa8He5C132DJxNyA9R_kz74EvU-07VthQzhD6KsNIv2pXu4b_U-lRweahPqFY2W4ZUmOLT-fn74_MbNwyNfXVgT5uSr-BMYGS2oeZfM1C1rqBwdKTV9zH-j7pVm5jZJ4mjCDQapc6U7vguC18ao4hF_Yaun8MPWeNdg5SKBJOfERmzItIPEvYh1Hq37Dye_6RTqokJbzplxsCrEBPQn87q2GiBmRK9RMVwqkO5Zhu4u-0rnoFW3Ze2AqOSkPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=H_CyeK2xd-mK7pOlufVNUFkqlYJ-JD6c2XU4h1XqA1gkRNhP9d4152RDMMr_UsNWYLXdcQ8SJsDtCFLdNvGnA9J49hf3wxcJFt6o3OHrXs7WndcS7WpVzVECmhDhrk-vfcMEjh50wCKZrWt4-BNDSGt7XUBuLAuMpEZISYjFeRbu8ORpRbK47SGRA-RvhfMnSIX-ywIu-ZeBP9Irumq81rgi7Qah68oAqXw37ZHAdSDuw6_1kZm4z3BCNvS85unBgMDmR1uz5ZsiqHtBViaTk4KZ2LevK1u8DPWPNxFAyvcjgXq0aFNlmslZYT0m5n2F458gflXr0VQYD0pFbPAtuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=H_CyeK2xd-mK7pOlufVNUFkqlYJ-JD6c2XU4h1XqA1gkRNhP9d4152RDMMr_UsNWYLXdcQ8SJsDtCFLdNvGnA9J49hf3wxcJFt6o3OHrXs7WndcS7WpVzVECmhDhrk-vfcMEjh50wCKZrWt4-BNDSGt7XUBuLAuMpEZISYjFeRbu8ORpRbK47SGRA-RvhfMnSIX-ywIu-ZeBP9Irumq81rgi7Qah68oAqXw37ZHAdSDuw6_1kZm4z3BCNvS85unBgMDmR1uz5ZsiqHtBViaTk4KZ2LevK1u8DPWPNxFAyvcjgXq0aFNlmslZYT0m5n2F458gflXr0VQYD0pFbPAtuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
فاکس نیوز:
بنا به گزارش‌ها، استیو ویتکاف و جرد کوشنر، فرستادگان کاخ سفید، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس خواهند بود، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=uorIE-wPyDDGG--GFdEYsDN_n__AzsEjshHzzlLcbQ8SLmYptFI-I5BFSp2iJlXT_Dh5YU7Tq7PoGx1E6hWpZ1g-AqxmSFK11nftp8rwNJJ-uKYnQg10WJ1OYD_PrgIDO-DiLiFolfyRff4CpgxdvNPTODNKLlBKCnd7q5xnD6yTwkabuV3qaqiHlq0OPQrS8NvMz9kps1CdFGRkRPLNta2DdSxjv8IO898iraA32jkjcZzr8jZKK2EWqZ3ebBuKzkcr7oVQIXqqp0wDLbbF4mPZHOJwZRbpLK8xaRqzF5lE92M_Lgt_d8P48t6miJsviCHh4KUAoqwgRbQxHIGreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=uorIE-wPyDDGG--GFdEYsDN_n__AzsEjshHzzlLcbQ8SLmYptFI-I5BFSp2iJlXT_Dh5YU7Tq7PoGx1E6hWpZ1g-AqxmSFK11nftp8rwNJJ-uKYnQg10WJ1OYD_PrgIDO-DiLiFolfyRff4CpgxdvNPTODNKLlBKCnd7q5xnD6yTwkabuV3qaqiHlq0OPQrS8NvMz9kps1CdFGRkRPLNta2DdSxjv8IO898iraA32jkjcZzr8jZKK2EWqZ3ebBuKzkcr7oVQIXqqp0wDLbbF4mPZHOJwZRbpLK8xaRqzF5lE92M_Lgt_d8P48t6miJsviCHh4KUAoqwgRbQxHIGreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله هوایی اسراییل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGe3GF-KHksU9YBppThzYmFMDV2olM3Rj8M831AbpLOcL5A6mPmhp6WrvMVphZTd5EpOWuyudyYuv-ac0qLsaeSGHjbhowcx349StpAjo9lIR_DhO4D2siDaCKOcJas0ZMCYx7KHWlwUmW4UcAFcnfOtuyPzSLQS76n9oOZbvSEb0A9TLenfqwkSptTc7O5xGNoK-33swKSMkrnAn1VrZkgXWtNzikukNhjCIjS5ViguBDn1FTTbhEh4B8kIvrjRr2CvMkWm9TDhb8VtD_GSEQT_frciP9NCehA-iqwuCbYUrxKTivR6wZxHwICGsfea4wKkJVnvJd4zt1ACGwByhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66551">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66551" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66550">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4LTsJM5_fmFLF969cO7SBDtjIqeZ83l2-_KJEfRdxy34VUQq_JcDnlGB2Yh37FGq_lxCWAbJcvaHGP5HmjtZXNg6-A9_BWCGPUgweSt0N7R9fDgfl9OyZBbRsNC1DsSjPgw7JJiVlnW31Kt8Pn2xrh-CfHLtH9bTji67tUixQ1vo-soiZC2n0ZQZDNptJ-QZx_Wf8TBvNVMcJEF5_RKWggkEVMZZuy-X_HpmnSGywSbdpMlqQU5rvCgBrCl-bwY9M9MFaL7clJqizY6iFKdF0Yv2wYFwM-LOFFrKQYEJZL7giFO_R1V5AOfvTR1ECb10Ew7FBPz_G7KkRJZuR627A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66550" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4X_3U4-F3fHjMVef9-2LsiuKffgz-bUQfgd_B3CszvBp1he0PVcQSk4OZCWvcNWrViTh9CbcYFhp8lfRcPFRgGkNSOhf1b5gdtN4_91c7zTKVFsBtStKTD9bGpv0gZQshscsfJi684dPJ-H-l4ABcRMjTPlFnDpVyPKn3QUbzsomHfRqBUR4DjwQ0EB1lTiyYNaKIAo5L2cLKvC4rjc2D4vMKr8APV-fFlS3EvwPKOkAW-jo-bTz1zSKaimEhV7NecqK3c-WIeLCoBq-iCsrjpNss70nQqKsL1WdTaQ_lo5thyXW4hRYcXKGaVYclmtaxflcYTpAMVbspk1OMGeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66548">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
شناورها در صورت رعایت نکردن مسیر دریایی جنوب جزیره لارک،  ممکن است با «خطراتی» از جمله برخورد با مین، تصادف دریایی یا هدف قرار گرفتن مواجه شوند و مسئولیت آن بر عهده خود آن‌ها خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66548" target="_blank">📅 14:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66547">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4x1i7gZUPSJ5rIiFyHl9cJZ4O8zq-hwBe-r6Miulc2EkxFH0Iyq7URZXiG44puHCgVuvO3lOMNTbtuMflCSWoeQwmff_rK_W2XFJffuILwJ-bv2uUeioSiT5pp_xp2o9sS8E33sr_lxcEydhxgn6DNn_X8f3R9wCUiqBZ4aTn7nfu11eJb80ung-lLrqV0WCltWweqZdQxCI2DAZaFDi_P94Spe_WlRII3WJktzGYEFRVp9WHCmIwAcuqSPzG4JmNeUw2TXvYJOlJ07A8Be05kiCZJTxOAK3fqNR6o4QFONORM34yrDCfhRwnFlrEh034japQmmSdPM2u9j6YqX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
هیئت ایرانی در مذاکرات این کشور و آمریکا تهدید کرده است اگر حملات اسرائیل به لبنان ادامه داشته باشد، تهران از مذاکره با واشینگتن صرف نظر خواهد کرد.
این منابع تاکید کردند مهم ترین مسئله اختلافی ایران و آمریکا پرونده لبنان است و محسن نقوی، وزیر کشور پاکستان، در این زمینه پیام هایی را به تهران منتقل خواهد کرد. نقوی روز شنبه وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66547" target="_blank">📅 14:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuBJ1hMKhGAhr-WNeSD4QizIF3XMFppFMy7GaomnSQDoOdAQ6-8QtId6ISI5t5wWlpTTeW1rAgS6JVF20WHIZxeI2pED4IvrQa5Ijm8TobIn-Re1KrydEJ9fq2mNEID5pg2hC2Tq251bXG1fKFfuvpyGNgk_yJ3dR9Wsj5SlDDg51HDOgv7Vt09esKBjtv0Zl8n-1QM6qo8NJUZPLFHpf0IOFxD4yVRI1n2TE1vm37kTVNkpSdrbp5fDgrBEtFlcBL--bHLooC0P6z7JpFPlPbHNVAVStDBZtE0mh_AjK9k9uNQVoA2ulo4CVs5El2bghgw5YfHHmbl3sGe3GJksgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9_bJL9sK1EK7E6y6q87H5uGxjmvUSlhFxFdkZpXVSvYgH3QiOtkgVQ0PbFWY3--0N3quBl5EgVNZZsVJmBinZ8woL5i9kEZRkWEOfZTekBacXcJ74jRKuJW5bLITsL2PLtY_LEB6Td0e7tuCohS9BaMDGyS_07-IqjohN7XHrNznribnI7XzmrXaCYSBa23xknMRvPe_8GMxssNtYmizzk-511ES99r3h-6tpnQXbiFY07zaEPCtHnQnZbzx-f2qxcnPI4tB6dgkAiOSAGwD0LIjqKTZ0D_prbMNd3BMehVyhQNUF5IK781cKyRTxfZoa7HSTjvXiiPUmYA7oKVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzkSzK6gQ2bPSlBkzNbKo_6CyLNEBD_xkuKRjsmt4VXJJubu04uQK4Npi4yssRNCHAk7Rp47bN-TeFVPQXiMYy2AljytwxaR9i5gFSyDegCxQHED2G8BprWmubD852ApY270tsAuocLcpAGg4SjzjEvihYCVDWRIzYJVepG5_cHzb-zKNdFpB9JNUnXMt8-QMla2Mma53zXqU3LT6ivfj2I6bmv25tnIiiYJ75ah6zS_CGGmI1YLU3v6yhM8saFX-feYxpx2VGJRWVLdeqySDTz-ykjTzvW-M32_mLDqaq4Wge4vfPAGJ1W6ixGQnsGD9Y3K3szY-G6sBw9CMitcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417add4a63.mp4?token=JwwyDH5wSC76yYq9Axzjw0klwpxtS-am52ASXos8ZSlJ8BT4MhbP2xOY5z0HB_gvjBfkjRPlk8hP6Mwuyx9p3-mP9LFja4DJhPXCtb_xap2dOchK2xPMlYVyYpenG5WKJCB8sE9sOHUf3audOymIZbZTYM-ULHhxDAQI_4aJ2YPuOmJnSi7Z_X6g0t6EN80UlZ11jRQSkJOPzWZe2wknBl5Dlj-KGW2tCsGLYD0KFT4m8K2sG0YQq1qRGM0EXv4aaUGFnuoDAVLKZuiP0i94A0INq8IuvinEtOLU1qoDXdPqJQi_BrmDAxqFnmqhMYtTYzCHPjlmliLOn_CGSVPxjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417add4a63.mp4?token=JwwyDH5wSC76yYq9Axzjw0klwpxtS-am52ASXos8ZSlJ8BT4MhbP2xOY5z0HB_gvjBfkjRPlk8hP6Mwuyx9p3-mP9LFja4DJhPXCtb_xap2dOchK2xPMlYVyYpenG5WKJCB8sE9sOHUf3audOymIZbZTYM-ULHhxDAQI_4aJ2YPuOmJnSi7Z_X6g0t6EN80UlZ11jRQSkJOPzWZe2wknBl5Dlj-KGW2tCsGLYD0KFT4m8K2sG0YQq1qRGM0EXv4aaUGFnuoDAVLKZuiP0i94A0INq8IuvinEtOLU1qoDXdPqJQi_BrmDAxqFnmqhMYtTYzCHPjlmliLOn_CGSVPxjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوس جواد مینوازد
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=JmnfeTBqNjd7MtRmYkAJOYnQJVUd_RJ1FXuTKEKYRh0MtDCe_VYZBem0BKTzEN7GLzwuiCNVYKWf_bC_KuD4KKtNYhmMOzvQECcWIvx2qQ5OkzoC633CsOR4xKI8YEacYHkZsfo6GFvBosf3or3hZgV7_ZQuRdlmloNQl712CxlYY-_Wfiyc6VcBmJI7WJudAlAviyATmp96hafBozrWhi-t3dQDXbkEzO1bDJ_O7EegeiDJhJGmyIyjXYA3zFMhiAYoe_v6RA_UOS5vWeCf077f4KctHmsh9rB5D3xKn50jGG_vGHfZ3pU5Siq5ep0rLiUj4jf-d5gCX8nOdAWwbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=JmnfeTBqNjd7MtRmYkAJOYnQJVUd_RJ1FXuTKEKYRh0MtDCe_VYZBem0BKTzEN7GLzwuiCNVYKWf_bC_KuD4KKtNYhmMOzvQECcWIvx2qQ5OkzoC633CsOR4xKI8YEacYHkZsfo6GFvBosf3or3hZgV7_ZQuRdlmloNQl712CxlYY-_Wfiyc6VcBmJI7WJudAlAviyATmp96hafBozrWhi-t3dQDXbkEzO1bDJ_O7EegeiDJhJGmyIyjXYA3zFMhiAYoe_v6RA_UOS5vWeCf077f4KctHmsh9rB5D3xKn50jGG_vGHfZ3pU5Siq5ep0rLiUj4jf-d5gCX8nOdAWwbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=UdpIyNuDHz0TYe9C1O9ZaBuCMzXResh8ng8MITrWOTVwdmL-5NOZ2L7Il5c_p3kZlylxNjYVTkAL0H5JTr32-2hCCaJg16_YoUZpbe4WYVmzwvratVjL6te6XTlBmJi__o2tcVHJ53-C0TiBeNyeOxAAom6X3t04CFeoJ1VCcG3vomF9RujmRfLXEDAazWZvNJZSDNqkhq5oqolxox5PCnGr4Wl0_PDVSj94r5wazWicttd0vm0SegSXQYWq0UToaBJaQoVXUC3gVNcCCQCgH4uEuxq_rYS8PQvnu7HvLMDarekqDM56toCJnEu7cxlt554lwYfPBX1_GVi4RiPWIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=UdpIyNuDHz0TYe9C1O9ZaBuCMzXResh8ng8MITrWOTVwdmL-5NOZ2L7Il5c_p3kZlylxNjYVTkAL0H5JTr32-2hCCaJg16_YoUZpbe4WYVmzwvratVjL6te6XTlBmJi__o2tcVHJ53-C0TiBeNyeOxAAom6X3t04CFeoJ1VCcG3vomF9RujmRfLXEDAazWZvNJZSDNqkhq5oqolxox5PCnGr4Wl0_PDVSj94r5wazWicttd0vm0SegSXQYWq0UToaBJaQoVXUC3gVNcCCQCgH4uEuxq_rYS8PQvnu7HvLMDarekqDM56toCJnEu7cxlt554lwYfPBX1_GVi4RiPWIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=STirPCgSfldySO6jf3nIZplzUOBv54LCTRkDUpze4fNikkeLxtI6dm7WJcxTj7YCtm2BuNDxy1TvkWd7okSEUv_Hw_wbqli2wvYIsN1GiYg3PVQuiVzbKGcM9CSX-o3cCzZAFHyQn8M1p4xrypVKhjVpoKh48vHrY_WumbuWu3ZRUCXzJjtSA_WhzElov9kIZO1a5OSux5Mh42VxlaLZaJLYaaIGXO-ne1rfYa3RW8iNn2MwyiXAs52B-9TsmOkUwBZFYhtBR8jA_EnI3rMyshwIUPsJTyprBCZD1sDyT2VJNYfTRJh-_1APItzkqEaZXTmnIZclQw_qDgWUR8jbpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=STirPCgSfldySO6jf3nIZplzUOBv54LCTRkDUpze4fNikkeLxtI6dm7WJcxTj7YCtm2BuNDxy1TvkWd7okSEUv_Hw_wbqli2wvYIsN1GiYg3PVQuiVzbKGcM9CSX-o3cCzZAFHyQn8M1p4xrypVKhjVpoKh48vHrY_WumbuWu3ZRUCXzJjtSA_WhzElov9kIZO1a5OSux5Mh42VxlaLZaJLYaaIGXO-ne1rfYa3RW8iNn2MwyiXAs52B-9TsmOkUwBZFYhtBR8jA_EnI3rMyshwIUPsJTyprBCZD1sDyT2VJNYfTRJh-_1APItzkqEaZXTmnIZclQw_qDgWUR8jbpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=h84vlLj4MdfbCec3jBYXDXVi_71FQcwSsfM506mqZp5WJrE_AEDfkEgXaWa6x3rWIAKeGXyhX7Ync-ZJNXEKJeJb-TyZCD8FSd0FvGh258zcm0S9J9Pxsn8Gk8W3h9fLlkf24KtJHgpb4yh-z_PcuPtE2tfNH9WvO7RSBFwWTpZAVL74GxsHz9DzVDBm1vyDorteQ6iPWN-3yvuSmDBvMe8_jVLmoG0wi9GS5X5YtmyuVc3AuOQ5DSrfNB0W9MW6aSYN_lkK8uZhFcMCel8vP2P0-TgzbHA1JxXqZEjfLNKW3ueoRknUjckYpJXF1sw5vpFqS-KbwyQWA8s_4zXbVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=h84vlLj4MdfbCec3jBYXDXVi_71FQcwSsfM506mqZp5WJrE_AEDfkEgXaWa6x3rWIAKeGXyhX7Ync-ZJNXEKJeJb-TyZCD8FSd0FvGh258zcm0S9J9Pxsn8Gk8W3h9fLlkf24KtJHgpb4yh-z_PcuPtE2tfNH9WvO7RSBFwWTpZAVL74GxsHz9DzVDBm1vyDorteQ6iPWN-3yvuSmDBvMe8_jVLmoG0wi9GS5X5YtmyuVc3AuOQ5DSrfNB0W9MW6aSYN_lkK8uZhFcMCel8vP2P0-TgzbHA1JxXqZEjfLNKW3ueoRknUjckYpJXF1sw5vpFqS-KbwyQWA8s_4zXbVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=qMM_CwU4QVv6T5Y9KHw_uTKjN8vftN2zfH4mSu8v1wzZ_MrgNB8ggJXEdGyUpCe2oDQvJvbw3kyST8BW2oilsVgGz8Lpt8XJmaNg_fTHDTv9UE8CQijhaMOA26WoNgVzZQLkWl6081kTnJiGnWhrGINJKrO4GLFpB9ZRe72VwNtniSTyQmXowBCuIBqAm_Kl9ivsYUVZNC1bsYIiXFf0VfEML_yUgr67NUYQIG6S47wUzK85qbbpMN5GECfr758Q3Ncba_rYtBTM0nDP9NI4-rxrlaqX-F2ka20wbffcCCgZYqCvGDXaC-ltPBQ4jZ6ARADfwrUIrhxhw67nHjMwQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=qMM_CwU4QVv6T5Y9KHw_uTKjN8vftN2zfH4mSu8v1wzZ_MrgNB8ggJXEdGyUpCe2oDQvJvbw3kyST8BW2oilsVgGz8Lpt8XJmaNg_fTHDTv9UE8CQijhaMOA26WoNgVzZQLkWl6081kTnJiGnWhrGINJKrO4GLFpB9ZRe72VwNtniSTyQmXowBCuIBqAm_Kl9ivsYUVZNC1bsYIiXFf0VfEML_yUgr67NUYQIG6S47wUzK85qbbpMN5GECfr758Q3Ncba_rYtBTM0nDP9NI4-rxrlaqX-F2ka20wbffcCCgZYqCvGDXaC-ltPBQ4jZ6ARADfwrUIrhxhw67nHjMwQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=vuYfyALv7Yel3L5P9gPNcwJmkBSor7z0609TzZ1xNIkWN4oZiKXCIOTcoLT4Vh-gFxqPxQBEeN6N3UNYYL2GeL0WZSMuh4jkwVDsgWUgLSOTAtJ6x915dfeZPZpfoNsV9kl_x9IW6HfHSM2anvcsfPoqFaOk6mz1naVf8AtGbd9v22_ScbBFZu0UGVq_Oty2_t5x7-FbqNX0n1qsDBUm5C_SDUZ5q-dy_0YN0lfpBF8hNHlyGkUxxKY0_Mf6pHLLV9PX18rxcpN19VyTH31pJgPwsWxYqmIlFjq0T9-Kl6JzTQaH234jbEZFy1UD5Y27ryg6X6h4wdlihCTW_fSqWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=vuYfyALv7Yel3L5P9gPNcwJmkBSor7z0609TzZ1xNIkWN4oZiKXCIOTcoLT4Vh-gFxqPxQBEeN6N3UNYYL2GeL0WZSMuh4jkwVDsgWUgLSOTAtJ6x915dfeZPZpfoNsV9kl_x9IW6HfHSM2anvcsfPoqFaOk6mz1naVf8AtGbd9v22_ScbBFZu0UGVq_Oty2_t5x7-FbqNX0n1qsDBUm5C_SDUZ5q-dy_0YN0lfpBF8hNHlyGkUxxKY0_Mf6pHLLV9PX18rxcpN19VyTH31pJgPwsWxYqmIlFjq0T9-Kl6JzTQaH234jbEZFy1UD5Y27ryg6X6h4wdlihCTW_fSqWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhDV0K0RHdGbth5Pi8jLN5N-Fy_ICVxUnEfoJmn6LjPD2wd_t3Ag5G56MbPjqN81lhxsJY6EzJY3KesFpXoN3E1jTx0zQwnGyUXwUGI_iPGlIUItTBptF0kvlBPJg4uPP2yimGvBpWQMfWh9N91sUDlU1XrOAWKVJ4_0mZnPRq6jNAwsoj4Ji5VC_YXPuSPA7DoAAXpQ4gL6AZ2zPW28J_iNeSGbptrPK_6fb-afAIOioi0HhKFwS0glkNwkFrrspJQBvQjI79HASOPrp5x816_dXTdTFMxgJpmTBoSlBGdhbH0J9MU2E8CDvwpyoOyL1JPT5BpLrQldAMjBE9NccQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=lz_f0qS7jkbnxSe1KIIQ-I6_yxbygQIAJ1PfyNxoWuGdAj2uzGokgxai-JlMudAxbN2RDGoaxbc1lwV_exp5rfiIHHax6-k1Ek71DWpdTUQPFSx6MSKNtbJ6ngC9zF3Dva8NTV_TE2Y6AEwTVHoBoxtv-cIRfY4w3zDMhnvAzjpcyGIylf0PgMun28xNiji1p0wSqf0OCMR6jSjZKEuIjzU9OyxGAYHcxjT69In1uKhLh9njLadZ0BhI2wP74lNxHUuQQ_p5JIS6JJMonJP4Cu6pXfG1vQ4tcWMMNQAJLbtHBtebbm3UZMecDg9ZLdD2I_yEJWFPMr8S5mkcbL2mwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=lz_f0qS7jkbnxSe1KIIQ-I6_yxbygQIAJ1PfyNxoWuGdAj2uzGokgxai-JlMudAxbN2RDGoaxbc1lwV_exp5rfiIHHax6-k1Ek71DWpdTUQPFSx6MSKNtbJ6ngC9zF3Dva8NTV_TE2Y6AEwTVHoBoxtv-cIRfY4w3zDMhnvAzjpcyGIylf0PgMun28xNiji1p0wSqf0OCMR6jSjZKEuIjzU9OyxGAYHcxjT69In1uKhLh9njLadZ0BhI2wP74lNxHUuQQ_p5JIS6JJMonJP4Cu6pXfG1vQ4tcWMMNQAJLbtHBtebbm3UZMecDg9ZLdD2I_yEJWFPMr8S5mkcbL2mwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=lCoZRPytXHG5zKZ0ODlyfPasODjNH4Z1_nROdnvOAN4YTu31pJn59NFVb9IqDzPhysA2TOCOrxDtCmrLHucNB4AO6RFjpbpXC0d_xTohymg4D9RhbFgrTpxnF2ujZ075kRBe4sN6p_Gtqecvsm68REMLsrxZGB32NDEWDdER75RBIWoHjRycbK4Sv8O1Zjvmyv_vx2CcubVeOWguRxyKY8o887bycs3iAUmY451wWbISvwIjydVB5l-TTWxK6ghyLXUoOkelLHenJbJUt9Tb8jphmpcnDqdPc7YplXaWSk7UJmiyL73H2vPna5Z8md7B0ob9q3oqezd06CjGyQw6fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=lCoZRPytXHG5zKZ0ODlyfPasODjNH4Z1_nROdnvOAN4YTu31pJn59NFVb9IqDzPhysA2TOCOrxDtCmrLHucNB4AO6RFjpbpXC0d_xTohymg4D9RhbFgrTpxnF2ujZ075kRBe4sN6p_Gtqecvsm68REMLsrxZGB32NDEWDdER75RBIWoHjRycbK4Sv8O1Zjvmyv_vx2CcubVeOWguRxyKY8o887bycs3iAUmY451wWbISvwIjydVB5l-TTWxK6ghyLXUoOkelLHenJbJUt9Tb8jphmpcnDqdPc7YplXaWSk7UJmiyL73H2vPna5Z8md7B0ob9q3oqezd06CjGyQw6fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=ENaKgNyBfFo9CB4IVR53oLI8orshELyATeKwr22U0nFa-hLDNa3Uz34GmbzoyH9qkRsaYdOUp5esIj5lGTBUPJ-lGG4OnNXBZyZU529B1NqBu9-0n66Uh6xFk2L_VtNRakseTpdMBYE_BV_9HH3TZeqRyjHJLT0yJlAgjfrmKoZvg6vsxdjteGaoU76dsbOAoVSYYdLTZyqqm6TC3NHTFALaeGU5PpxlBWcdNQDac2jMgwSOaEBSHiYaXSUSfN2LKUWwr5Vt1r06rM4ZRvYOiLgOcCaTEKhTbuLt-qJSWX1M6Kc7vTo3g1mj7PtWNN61aGpZMGH7Nsr8x__EunsDQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=ENaKgNyBfFo9CB4IVR53oLI8orshELyATeKwr22U0nFa-hLDNa3Uz34GmbzoyH9qkRsaYdOUp5esIj5lGTBUPJ-lGG4OnNXBZyZU529B1NqBu9-0n66Uh6xFk2L_VtNRakseTpdMBYE_BV_9HH3TZeqRyjHJLT0yJlAgjfrmKoZvg6vsxdjteGaoU76dsbOAoVSYYdLTZyqqm6TC3NHTFALaeGU5PpxlBWcdNQDac2jMgwSOaEBSHiYaXSUSfN2LKUWwr5Vt1r06rM4ZRvYOiLgOcCaTEKhTbuLt-qJSWX1M6Kc7vTo3g1mj7PtWNN61aGpZMGH7Nsr8x__EunsDQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=B9EDzHO8jng4rS0jI7KIuoatKr-d4fvS9NyeUxh55OJg9QaObRTChOmhKNF4beaA9kb2clsoXIwtN8iyjWW1JUhueATGrfIsaiJVWsoW7_zkNelZL1JIj43pV6qTTHHkQubKEdmsxTkmTFESxwoyVyJRd_4tFNv44Z1Z66-PkrngEYqZih_QnkyGFTz6DQl0vrvI-xHeTDPp463Zn0gyPTfJMFkUqfbwknRYC-T1vTW3-DyFgoqAVU5ngtMNtaGS6cG91bgvD6S8LvXwcyJYztSb25Bqtj0w6n1kn3WKVTFZjux0yZH9XxzgwJjDS5HIYWEms5pvRQCSg73PEps4xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=B9EDzHO8jng4rS0jI7KIuoatKr-d4fvS9NyeUxh55OJg9QaObRTChOmhKNF4beaA9kb2clsoXIwtN8iyjWW1JUhueATGrfIsaiJVWsoW7_zkNelZL1JIj43pV6qTTHHkQubKEdmsxTkmTFESxwoyVyJRd_4tFNv44Z1Z66-PkrngEYqZih_QnkyGFTz6DQl0vrvI-xHeTDPp463Zn0gyPTfJMFkUqfbwknRYC-T1vTW3-DyFgoqAVU5ngtMNtaGS6cG91bgvD6S8LvXwcyJYztSb25Bqtj0w6n1kn3WKVTFZjux0yZH9XxzgwJjDS5HIYWEms5pvRQCSg73PEps4xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=hHnGFt-bIB_aiHdtEmNbUuSlKvBd128DHNJvQz7hSew5ex7q3-qKZkz5RBaQi3GPh6wAgYONYs9b2jbdm-3bNKDXdazufyiZG5HXGlmnbEvqkfHELSKtCHPnh8WqSRqzKu6VIeM9F5GF46lAeHCSXtZtqNcac5n7At36Nr0j1YGmy-4GOuDzX8uP2UkzmDci0t77MKxTgP7EXDqlY5xOSnia-ZCEQBlA7hccI5-GOICPNqHbxfSNwTtMOTo1mZJE4eBUdJvrZ_93soou2ogctGZF-Frw_iPCElP3J7xsKTbUf42gk4WKw2DWvwGUyj1sHePKKteAWvwxNSLCReaFuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=hHnGFt-bIB_aiHdtEmNbUuSlKvBd128DHNJvQz7hSew5ex7q3-qKZkz5RBaQi3GPh6wAgYONYs9b2jbdm-3bNKDXdazufyiZG5HXGlmnbEvqkfHELSKtCHPnh8WqSRqzKu6VIeM9F5GF46lAeHCSXtZtqNcac5n7At36Nr0j1YGmy-4GOuDzX8uP2UkzmDci0t77MKxTgP7EXDqlY5xOSnia-ZCEQBlA7hccI5-GOICPNqHbxfSNwTtMOTo1mZJE4eBUdJvrZ_93soou2ogctGZF-Frw_iPCElP3J7xsKTbUf42gk4WKw2DWvwGUyj1sHePKKteAWvwxNSLCReaFuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=jd79VuF5ScQye2TvhQFrhNx83gzOw5YHr04X5LUJVZd51PRkxLIXTJPReR0pe8Hd8EhIuRL2b8SqI0KhAf7NGK2fzWQH9iCQWEQN0TZeDQ78HmcVgUANtyiJvvhGG6dBFNGeXsU5-0bq35ULavIlYLZdl8UFdPK3ZcSwDdyHpXwPoeaihlchPQEXpKArV_y7Df98qSrqqoq_ZGwGOIRKE6KVWLj5FhtBT-ARlJjsGC4EhOiJEKd1OWEjURPnl8mmE3ew1gXxZhUB_TMCrhDaoqtTVKuQ65BuPnbPL98pkDDMPqfgUpmt70qsqbF3T1mCR5V-xL873z6CcATWArhsjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=jd79VuF5ScQye2TvhQFrhNx83gzOw5YHr04X5LUJVZd51PRkxLIXTJPReR0pe8Hd8EhIuRL2b8SqI0KhAf7NGK2fzWQH9iCQWEQN0TZeDQ78HmcVgUANtyiJvvhGG6dBFNGeXsU5-0bq35ULavIlYLZdl8UFdPK3ZcSwDdyHpXwPoeaihlchPQEXpKArV_y7Df98qSrqqoq_ZGwGOIRKE6KVWLj5FhtBT-ARlJjsGC4EhOiJEKd1OWEjURPnl8mmE3ew1gXxZhUB_TMCrhDaoqtTVKuQ65BuPnbPL98pkDDMPqfgUpmt70qsqbF3T1mCR5V-xL873z6CcATWArhsjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=ZVkRkn-dxobiTNf5S4ayrepmhBXbiHFvzCF2F4AGd-1IIFSMbepRnTx238drkMW4wf1fFhfppcqIOVrxI6AcXqv4i9W4Flyx16FJbHimvlijycsYzcWBkF3LhEyU0nfQvYswYqTS7hTcfCtGMxmDDyv8tRzkE0o0E3EM6eqJGaaCAdhYr2ZiaFJ1-xFBPvNyqbrHikiCLOs1BOAHKsx1sfz5yGoCCB1ghUuRDoDojE7Flfjik9aYYIx3QOHIAamlokkT9-9ApnniKP2HoSS-eEPALWsxtfv3Qa5lRnn3dBvdrZih2w46sqZ8-xhQ1jkjEoPF8t7tZEUcmQfh3GESfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=ZVkRkn-dxobiTNf5S4ayrepmhBXbiHFvzCF2F4AGd-1IIFSMbepRnTx238drkMW4wf1fFhfppcqIOVrxI6AcXqv4i9W4Flyx16FJbHimvlijycsYzcWBkF3LhEyU0nfQvYswYqTS7hTcfCtGMxmDDyv8tRzkE0o0E3EM6eqJGaaCAdhYr2ZiaFJ1-xFBPvNyqbrHikiCLOs1BOAHKsx1sfz5yGoCCB1ghUuRDoDojE7Flfjik9aYYIx3QOHIAamlokkT9-9ApnniKP2HoSS-eEPALWsxtfv3Qa5lRnn3dBvdrZih2w46sqZ8-xhQ1jkjEoPF8t7tZEUcmQfh3GESfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=OlkGgzjwXJrl19ocZZeXCDDeErKc84yq3QMdNY3uX6v94rMpkFnkrWl-DXdBu_XDqj27ONjBA9Tapw_nTNK_1NMQ3ontDOM9sTiS8v0j5K8MgykB_9ksTxZp7NF9bbY52rSMGy7WxwyLlOkNfzEupXBup9NzD56TcArC7RLY9fEzPfMQXhepjmMtBHLBE0HQdW3ghkgTU4-fDlZG6q0voY26YzaZAPi_bRbBD0xuOcECbhC-0FAlhHIWiWvIoGbNsud05Ig0Mfke_krcbsiN7Hg1QS5hVZzGy2TKz3UhfTUsfGNuLepWVgy3_tI0sEwDi0aR39EuL5Vd6UdKDJ-GsS64bMkFGz6rzJWWYX6ceXsc0hDS3_plmoYWWhZ5RcegDT3XBPNrVIFHhPf94IzJHsJxGhbjrmYgMuwO1ySWEKT2LQ-nluIFhPeRgZ7a-Dj9-kTc9ON37vyYdPND4Kfck1W-8ZpsJSE9HxT6Zn1X0egQ2XF1KCxYYZ5Fue8wBLAIJ6JjzPMQgOwq_vD3BMEhsyoPVIqfOGZEsedXfytfWJ32LXVrPtORnqZBVDLYAP-TY6r2T6MIVwvHMDVB2jve88ZUPJHPeBACauNiFDrxjmOkTOGhhRZnFeXsaWmKFoe-SHJBwGexTw7WxDOw786Nfmgm14Td1XV_hoAZoMHmVws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=OlkGgzjwXJrl19ocZZeXCDDeErKc84yq3QMdNY3uX6v94rMpkFnkrWl-DXdBu_XDqj27ONjBA9Tapw_nTNK_1NMQ3ontDOM9sTiS8v0j5K8MgykB_9ksTxZp7NF9bbY52rSMGy7WxwyLlOkNfzEupXBup9NzD56TcArC7RLY9fEzPfMQXhepjmMtBHLBE0HQdW3ghkgTU4-fDlZG6q0voY26YzaZAPi_bRbBD0xuOcECbhC-0FAlhHIWiWvIoGbNsud05Ig0Mfke_krcbsiN7Hg1QS5hVZzGy2TKz3UhfTUsfGNuLepWVgy3_tI0sEwDi0aR39EuL5Vd6UdKDJ-GsS64bMkFGz6rzJWWYX6ceXsc0hDS3_plmoYWWhZ5RcegDT3XBPNrVIFHhPf94IzJHsJxGhbjrmYgMuwO1ySWEKT2LQ-nluIFhPeRgZ7a-Dj9-kTc9ON37vyYdPND4Kfck1W-8ZpsJSE9HxT6Zn1X0egQ2XF1KCxYYZ5Fue8wBLAIJ6JjzPMQgOwq_vD3BMEhsyoPVIqfOGZEsedXfytfWJ32LXVrPtORnqZBVDLYAP-TY6r2T6MIVwvHMDVB2jve88ZUPJHPeBACauNiFDrxjmOkTOGhhRZnFeXsaWmKFoe-SHJBwGexTw7WxDOw786Nfmgm14Td1XV_hoAZoMHmVws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=bLyZa9uP7EqLzJjxjBy-REfMSQskZy02tdhrjaSQhA1kyqsz9hK_N1qVGim6iFmm0VW-Pc606WYNrSJZofZJfYrx3V52qE2WfXEf9K1HUO2kk_tHDPw8XKkE9gYokkZeo01pvDK1PCc4JkdsnpuPGvapTISfBlKuZK4hUNWi-4dzjSQxmKaE3_7vcXReLQcbUqk5YB0WmZywB5riWj2-ykFsZx4gryMlQrzu75-kPFDXXHuktm2-8sff1FtBY-RTCWVkcmdHf-qs5vHyK0W_Elpg-sfrk4wyo3ZMSRE_qtx4fB58ABbx1a4nSlFYgka0yb1Y0iQZuUXH3ulUnOvFpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=bLyZa9uP7EqLzJjxjBy-REfMSQskZy02tdhrjaSQhA1kyqsz9hK_N1qVGim6iFmm0VW-Pc606WYNrSJZofZJfYrx3V52qE2WfXEf9K1HUO2kk_tHDPw8XKkE9gYokkZeo01pvDK1PCc4JkdsnpuPGvapTISfBlKuZK4hUNWi-4dzjSQxmKaE3_7vcXReLQcbUqk5YB0WmZywB5riWj2-ykFsZx4gryMlQrzu75-kPFDXXHuktm2-8sff1FtBY-RTCWVkcmdHf-qs5vHyK0W_Elpg-sfrk4wyo3ZMSRE_qtx4fB58ABbx1a4nSlFYgka0yb1Y0iQZuUXH3ulUnOvFpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=KngNIyF4VFD0Pgtb_VIQGSXAxFOPOYGBzsY2CFGo1sUAz3ghohte-oT_DO0SUnhvzgprMnoSNV7Eca_3zDa8XPuzvF8ooUhDmiRBQNMKFVh3V3JBZGbfBWanNC0drkNZ7Je5FJD0d3q06Dmxfw7iMkJIb2fbfygyjzV3_UkTWAID89c8oqaBDTtosBF_gjU78fLbWK4yKV4vxVrlQjZU27NTU_mPPsMCg0KxxIcUgmHoUovkXt7OE0hCZlKKDyy641lASM5-ZbFc8nDoumI0aHd5FH05B1UJw8OZSk9Zv84AoHO1yS83Kvom1GAGHtI0OH73sInLDMoOPv0NH1Qq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=KngNIyF4VFD0Pgtb_VIQGSXAxFOPOYGBzsY2CFGo1sUAz3ghohte-oT_DO0SUnhvzgprMnoSNV7Eca_3zDa8XPuzvF8ooUhDmiRBQNMKFVh3V3JBZGbfBWanNC0drkNZ7Je5FJD0d3q06Dmxfw7iMkJIb2fbfygyjzV3_UkTWAID89c8oqaBDTtosBF_gjU78fLbWK4yKV4vxVrlQjZU27NTU_mPPsMCg0KxxIcUgmHoUovkXt7OE0hCZlKKDyy641lASM5-ZbFc8nDoumI0aHd5FH05B1UJw8OZSk9Zv84AoHO1yS83Kvom1GAGHtI0OH73sInLDMoOPv0NH1Qq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=aTztU0TNeebaVe7sfGItXa36Er3Nd7G39TCWrgjJqQ6pjzqdYQ3Cmq05IXKbo3adcfoXBMxrVpyhZ5Wu1reXpytVUgHJ3KLiBqKV3bndxY2JdZan4Sca8RdW9OhS8_msFlDlBPMRhF2clhXkM-FOvMwwGSqD15u8vFQ-6hBpDtKzUb-S9Ryxs1PUkts2utlap6v5CXirbrop7viKDjw49JH9T-Y1vx9CXKMfYTa2ntCN2mxqMkcdbwLGHHD9li29H1_K_15oe-oaEnum7_OCkTvjJ0toZczQsUyYGMRZQVzd0s5MNsM7jNUPTVwqqa-zJbjop8Hdu04FQ3ykrS5Afw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=aTztU0TNeebaVe7sfGItXa36Er3Nd7G39TCWrgjJqQ6pjzqdYQ3Cmq05IXKbo3adcfoXBMxrVpyhZ5Wu1reXpytVUgHJ3KLiBqKV3bndxY2JdZan4Sca8RdW9OhS8_msFlDlBPMRhF2clhXkM-FOvMwwGSqD15u8vFQ-6hBpDtKzUb-S9Ryxs1PUkts2utlap6v5CXirbrop7viKDjw49JH9T-Y1vx9CXKMfYTa2ntCN2mxqMkcdbwLGHHD9li29H1_K_15oe-oaEnum7_OCkTvjJ0toZczQsUyYGMRZQVzd0s5MNsM7jNUPTVwqqa-zJbjop8Hdu04FQ3ykrS5Afw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=F3eOWCzeuStDSxyABIyrPeRPOWGi_3ARZh4JLj4lcWASFhOhVG2CnVw2K2GOu-O2ovjPI1_q6wTxkEpOB5GcTHZGLFIx1kglOgFMDmNmxMYfienGYopepF5-zGSoiZSnTJe0JD0GNdo0W-9ixJwVTvLMb16fXCCO8SEmXoMXRei04dGKJzvTndfJm2wb3Dlnf6ScTvZMtlDIcOatWuK-7XdobK0BIyVM7aMTx0f16bjAHcb8pDgDI1YVNdLGuHrmn04KNEFLEqXMgPhqOgCkDIqUI3mmdcuxNvMohuIqMqoGmrxmAqEG6Amj8oBUh1_jEs-gmInG9GqVhNGI4zgohQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=F3eOWCzeuStDSxyABIyrPeRPOWGi_3ARZh4JLj4lcWASFhOhVG2CnVw2K2GOu-O2ovjPI1_q6wTxkEpOB5GcTHZGLFIx1kglOgFMDmNmxMYfienGYopepF5-zGSoiZSnTJe0JD0GNdo0W-9ixJwVTvLMb16fXCCO8SEmXoMXRei04dGKJzvTndfJm2wb3Dlnf6ScTvZMtlDIcOatWuK-7XdobK0BIyVM7aMTx0f16bjAHcb8pDgDI1YVNdLGuHrmn04KNEFLEqXMgPhqOgCkDIqUI3mmdcuxNvMohuIqMqoGmrxmAqEG6Amj8oBUh1_jEs-gmInG9GqVhNGI4zgohQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=D12-uDxoR2bCr426peycL0-8u5uuB4_0L98am0kaOga5ejTQ7g-xllBzjE6E0_yJerrPEr-xuUnx2HyJx9py5dbrjxoBFaFy4KS1dQ1L58TRsze_JuiAnntKACQXaTqT6F2WodWH-KS0BtXf-4pWFyMkB3733_JbQy_fs9EpSbHr9yDW7L502VQ_727-DHN5j-58JZtgkFHrWxidfLp28vNONGPDB7q-evmJdyowK7QrHtBxkQ6YiFOo0XTLpCw_XTcSFxGXpEeRp5douFp09a7TrJVLcLi4z3B_xNaJP0THQhGFjPlLi21Y0yHCC3PK2NIn4HY3EGfgwn3mv60tNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=D12-uDxoR2bCr426peycL0-8u5uuB4_0L98am0kaOga5ejTQ7g-xllBzjE6E0_yJerrPEr-xuUnx2HyJx9py5dbrjxoBFaFy4KS1dQ1L58TRsze_JuiAnntKACQXaTqT6F2WodWH-KS0BtXf-4pWFyMkB3733_JbQy_fs9EpSbHr9yDW7L502VQ_727-DHN5j-58JZtgkFHrWxidfLp28vNONGPDB7q-evmJdyowK7QrHtBxkQ6YiFOo0XTLpCw_XTcSFxGXpEeRp5douFp09a7TrJVLcLi4z3B_xNaJP0THQhGFjPlLi21Y0yHCC3PK2NIn4HY3EGfgwn3mv60tNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzEiQQm67tceDrFSNsvw0AksT2xbhUk5uI-UT4BVkQUDf5s4BBAavhHkipkTwDlUSZg9aBVz-3li4z5cogiYPHXjclGGUjLYp8QSCH_y48dvSMgeeF0uvmIK7LnM2cimEQOqIlO4TXgthg98HlKtjbT--N5lVSKzSF7lW4VUHVRoIuxIDuDPKIuBv_Ml6EsqbW_WBpPmZVr6mH2No3IDEXs02Z2AKf59Sj5v_pt_58e-temCEY5a_19Dc25BK4KOzXmmIuefnslgjpEWS1HbVrPJ7dTHNke9cZkGxfgczWn2THp9rDr5d_lzQHFnARFYTQkaIuOHTYKNF1jTZtQclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZTRdrymGbW2_U2FOivOYW26DjXf9dJhHP5H0tgoTdzZgxgAQF9HvBLqV22iRI38IPR9e7LKrDBH-d0dIASWMSM-zGE7f-LgnRmBUpjMg9MDKUjP4PvZYxalWYlvT7dykUYHlC0TxFlf37ZwI279EgLU0Or51lusJKGNaKSDvnzd5HmCcz4iwbOi00w4wFTO2YWAIwO2fFFVIcsGwaOwQt7fdIOepsMZQWhNzdqPBP3oUi6sCNvzlgaf5nXvXJPslqRrfD9tQnDtyTiX2-jj2cFh-_SKKm-B8V-nFD7T_XzBoNiNt1ylI9FX_LawiYMS3ZjX2JSkH0MVaSxrfq9h5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkjFtY2qt9af3fdqH6HPm-nlq679JoHkOSzCAofV7G2rBg0ZUb6-OqQyEMIJlNw70dJ0TZ_Kgc-fj7QnkIkEXXrXskXkGs_Itv6ZxSeAKnfyaCY0bvEpkU2YE8v0VA7KVorOHFqyvdsqu3yp1-Il67hDiSBp0Sd7tBWS7Sa3UGnLkvlcGzd6YPJT2Hv_Jd9jBbpwPSVWx6CEfngHUFUn4WQaWfRL3OZvOGtZOYti1hTPSI5xVxN4zd3nN_FFVTO48NBH8xkJum3oVA5iAdsdq6ogQhFYrtCQZtKQgxMQTpzH9S28Od17b04q5bHR8usw3aBYDCpI-Tr0QTqoLQYCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=GmW4iQTSB2l2i4DZZkKtNTv8dfmI2tiNNK5u65FxP3Eo3lbUGIDUzLNZMakyiROtHGi1Fag6zH03LQePO5nsMlrkO2VmiV__fEWl1DW_JTo-tkQAwtkfXdRwVDBgRO5wgL4hmQlH3-sxVaFRYT2Et1exaOq5Es91s7ti3g9BxN6Ke0kPc3dyGES_vVouR7-0LzxeIR6mf__uDkDxsy6FPqnPRizCzRgra031XMBRUHUuOnIahddE-in3-N5532ECB5SvRdFBjoVa29cDHP9jyrgKHJ-eCNbUO0u83iho4GmDVJ1ShfRASP4KD_L2ryY1PO0hvfJnEDo396hFCm4xxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=GmW4iQTSB2l2i4DZZkKtNTv8dfmI2tiNNK5u65FxP3Eo3lbUGIDUzLNZMakyiROtHGi1Fag6zH03LQePO5nsMlrkO2VmiV__fEWl1DW_JTo-tkQAwtkfXdRwVDBgRO5wgL4hmQlH3-sxVaFRYT2Et1exaOq5Es91s7ti3g9BxN6Ke0kPc3dyGES_vVouR7-0LzxeIR6mf__uDkDxsy6FPqnPRizCzRgra031XMBRUHUuOnIahddE-in3-N5532ECB5SvRdFBjoVa29cDHP9jyrgKHJ-eCNbUO0u83iho4GmDVJ1ShfRASP4KD_L2ryY1PO0hvfJnEDo396hFCm4xxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم، دبیر کل حزب‌الله:
امروز در لبنان، ما با خطرناک‌ترین مرحله تاریخ خود و بزرگترین توطئه مشترک آمریکایی، اسرائیلی و بین‌المللی روبرو هستیم که آینده کشور و فرزندانمان را تهدید می‌کند.
هدف اصلی این طرح، ریشه‌کن کردن و حذف کامل مقاومت و پایگاه مردمی آن در لبنان است.
دشمنان برای دستیابی به این هدف، ابتدا جنگی جنایتکارانه و بی‌حد و حصر را آغاز کردند و با کشتار غیرنظامیان و تخریب گسترده، مقاومت را به زانو درآوردند.
در گام بعدی، ایالات متحده و رژیم صهیونیستی پس از مشاهده تغییرات در معادلات منطقه‌ای پس از تحولات سوریه، توافقات قبلی را نقض کردند تا موازنه قدرت را به نفع خود تغییر دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=f8C4RsUgddGvtJ0pmmxFYUxA_W1o5h__sHXAyfMKXJ25Dyajh-hVqZEn1B02d_OH8pPq-APgv-t0jZYnxqk2A2hvXSG6-LHtmZEXqZadwbyrwn8dFDXo1lf3XxHJLSHeR0NskO3KeZ0j6YjvCujXGFLzvHw_xv5TYyJhip691h6zHOwoKlQB8P6mfNJ-PdUeusX0MqkM1i-ZcDPpGiTt2hGDfyMSD0PeFaSROUxr2H8cwZRyAY9Lt-6l-GSSPRW7FgDb1ms5sFLBtUTahnSsr9hoEP5rvlUE-KzKbSTRAutBTVo1XoRZXQdKeVYW5VSZEhKSjWiiX9kLNnBSINSqDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=f8C4RsUgddGvtJ0pmmxFYUxA_W1o5h__sHXAyfMKXJ25Dyajh-hVqZEn1B02d_OH8pPq-APgv-t0jZYnxqk2A2hvXSG6-LHtmZEXqZadwbyrwn8dFDXo1lf3XxHJLSHeR0NskO3KeZ0j6YjvCujXGFLzvHw_xv5TYyJhip691h6zHOwoKlQB8P6mfNJ-PdUeusX0MqkM1i-ZcDPpGiTt2hGDfyMSD0PeFaSROUxr2H8cwZRyAY9Lt-6l-GSSPRW7FgDb1ms5sFLBtUTahnSsr9hoEP5rvlUE-KzKbSTRAutBTVo1XoRZXQdKeVYW5VSZEhKSjWiiX9kLNnBSINSqDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66514" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8Eqndg8btHGmYOUzjc_EmuS4fpdAwvx7146ggWeudNrqbvMdh1ynQHkxzCBXh6_twks13xol5mKYwZFOzHSCWum3brFJP4YSqsznRpioszkj7byeUuS0WLnw6jpiyn6H6i1HQKotewC9ho4-4uLFZvqIwwJfR7l24SR7vPseYeoks0j_sciJJezdwhvVjoUHqmLpO2xwKeDSW7v3iOIDXJS8P3oWiZpkD55PnvbrCQAMu9LCICAe6w6k_0VVw-sTr8oJlD1InZ6aYZhcGhoslLEUh-kZNsqX_NNe4kpwEA4WcNx6nm50_q26cVJnzQOFbrBEYGg96TyZRUEE9wtRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=ggqXPwxojSCc7iyDeJAUNfbxie-hloT_cqoqsaNLVl3N2dAJAXXLd1s-3L9hl86j2j-8LWZneE0i864xG5x40uEW6bphFyPU_Zg_9UQeP3g50vBdfzykxS5oI_qAPCGcpKxDO2E4q8Nt1qQdpkLwGzkK_Qp50EsX1XdyBa5KW1GcxU89al6OuhNi1G3rvHJcy-0TRT8yfiLAW5ijWDuwxZIxFET432zHxz1cUTcZJPrQhjLDHcGODULSk2gArK1Fr0x66nUKN7usUiVHPSZDCgi3p7Jnc8wY1MQdRP3j48MZcWLrpJtjDh8gAl-ugGRmhY6n8BWNRdpiEtEmQj4osw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=ggqXPwxojSCc7iyDeJAUNfbxie-hloT_cqoqsaNLVl3N2dAJAXXLd1s-3L9hl86j2j-8LWZneE0i864xG5x40uEW6bphFyPU_Zg_9UQeP3g50vBdfzykxS5oI_qAPCGcpKxDO2E4q8Nt1qQdpkLwGzkK_Qp50EsX1XdyBa5KW1GcxU89al6OuhNi1G3rvHJcy-0TRT8yfiLAW5ijWDuwxZIxFET432zHxz1cUTcZJPrQhjLDHcGODULSk2gArK1Fr0x66nUKN7usUiVHPSZDCgi3p7Jnc8wY1MQdRP3j48MZcWLrpJtjDh8gAl-ugGRmhY6n8BWNRdpiEtEmQj4osw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJRY-45H0WM1W3SzSQvhwQ9O0FKNVi-c32_bCSOKhEqS0k8gIq_ai1zKakrLLPXkDS2OpO6eabRK8LvK-FDFNsLshHiqNffAbZjYbovi8V42Jlz9IUUn_h6a7CRBeBrDcjyJA6mhQWXjMQfv-9p_EcHuptjPuKyMbfb0Rjo08jjfSw-DrgVSs4P38g9POCc7f9mWM7DBAPOoNrRC3ogDZ3aF7dt7Sl30GcYErT9D_cqV_XQFgTSLaGcmOcqXCK2wLcklUOuK4QKpML4shJ8_oWLK2QTSSf7A5nywqVK0Y4dtprgHrfud-HyLzwodZ18dibrMNZ0M95TqIGfCY6GFUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=QWSCXAI604pZRwvxLxJ6E9pdt0_vMN-mpeUJqKTV3SoTyDAmMjAoSMYA13rfixwCOTvZuz7dVTDEEMVvoS2GG3dRTbVtYWl_LluBUh6vbrteQSQo7w1-I2apWpXlvcWZy0P2CrHapMghKYhV0sF5MlhSBCu8Jr_bEysgNXaGavcIN47Xi10S_WTsrMAsc3ibsjDanUUEDkHZ1aVdriHkLVnmcmHuFvJprAwrqExpLwp1AeM1sTQ_OiAjI9LeeFMAU13q4K4b7VQtwk59fEbJWe1khLi2t2S_WuZLmXuJvyLrK1UdvkImlXXDJ7z7vt5AAxcGCS6-ibRHAy5F4_Ajhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=QWSCXAI604pZRwvxLxJ6E9pdt0_vMN-mpeUJqKTV3SoTyDAmMjAoSMYA13rfixwCOTvZuz7dVTDEEMVvoS2GG3dRTbVtYWl_LluBUh6vbrteQSQo7w1-I2apWpXlvcWZy0P2CrHapMghKYhV0sF5MlhSBCu8Jr_bEysgNXaGavcIN47Xi10S_WTsrMAsc3ibsjDanUUEDkHZ1aVdriHkLVnmcmHuFvJprAwrqExpLwp1AeM1sTQ_OiAjI9LeeFMAU13q4K4b7VQtwk59fEbJWe1khLi2t2S_WuZLmXuJvyLrK1UdvkImlXXDJ7z7vt5AAxcGCS6-ibRHAy5F4_Ajhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=jkM1tW4qZyyebtayLTzIuVvOSZPKmMRmquF8BK0o_-T7dql5uZd5Y4jZOj9mNh0IoUphuDShnBI7kpMul-PnAo5zV-0yX3QE5vFMGGTo0LVU_DZTj9nQAIxGh-oylcNe-p_jE5Diq5j262WvMhyGERLUWlzeYhGz-eCYW8OQ_VZ4h7uDmSt-GaiaYzx2uM-4x1DIiSQAjq_Tv4Ckadz8SCDvCCaUwFK2zD1RMV-xBjQWi7KAXzW27gTLtAdUB-9H9YNRwCJt8bM1CKEySzFa-wUakG3Uq40iKXNxD4ICYcgv-Fu3ybMRgjr8RkG-Y85gJ8JH9oec-LqF9QN4B1dDKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=jkM1tW4qZyyebtayLTzIuVvOSZPKmMRmquF8BK0o_-T7dql5uZd5Y4jZOj9mNh0IoUphuDShnBI7kpMul-PnAo5zV-0yX3QE5vFMGGTo0LVU_DZTj9nQAIxGh-oylcNe-p_jE5Diq5j262WvMhyGERLUWlzeYhGz-eCYW8OQ_VZ4h7uDmSt-GaiaYzx2uM-4x1DIiSQAjq_Tv4Ckadz8SCDvCCaUwFK2zD1RMV-xBjQWi7KAXzW27gTLtAdUB-9H9YNRwCJt8bM1CKEySzFa-wUakG3Uq40iKXNxD4ICYcgv-Fu3ybMRgjr8RkG-Y85gJ8JH9oec-LqF9QN4B1dDKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=TQJX6An4c_DlRrdK6o8HfyfeXHhXgqLClj9easv4nKhBnSUdiDJYHeI7uq_dXAHImP_WRCf_9EftWkTQawMOSl9DLBERfBcUNlArRFXyhH3T4PM4Tw1jgYaEEgED-Pkgw9ELJaKOLmUpJ4V5Lb0eAUXa8gBTvhNV4dSzh_0fr_PmRXEwp8xYxfzitZ8ez_b29PilnvIZo88I0VI83gCIho2vm7DkR9nob-b0hTYOXp5snbdjgeK358tDDBqTyA89gqxkwGWGVqV79icD8fuvjeHVfs-TvMzUiGXIy-1DINMKWaeEQ44vu5bCtfxI0a87dSRGEAEBUo7i1zt5XTvnqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=TQJX6An4c_DlRrdK6o8HfyfeXHhXgqLClj9easv4nKhBnSUdiDJYHeI7uq_dXAHImP_WRCf_9EftWkTQawMOSl9DLBERfBcUNlArRFXyhH3T4PM4Tw1jgYaEEgED-Pkgw9ELJaKOLmUpJ4V5Lb0eAUXa8gBTvhNV4dSzh_0fr_PmRXEwp8xYxfzitZ8ez_b29PilnvIZo88I0VI83gCIho2vm7DkR9nob-b0hTYOXp5snbdjgeK358tDDBqTyA89gqxkwGWGVqV79icD8fuvjeHVfs-TvMzUiGXIy-1DINMKWaeEQ44vu5bCtfxI0a87dSRGEAEBUo7i1zt5XTvnqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=JQcf0byO9xt-822mNaCDMP5w2NZAy2mOTT_djrup4dWYcjmy0QTEvbkBy4aQbhpCczQwSWkxhCQbzMTfKeY4F8Acm80Z7yJYBe6n_mEwv80WlSMByJiRB6IgME4rQSGxTJ-VXqJHMYPFsMiZFsY8yi0mrGGyzqnGEiGCyzudhiZHmZSTaGVis5bt27tM6to1_ngptI5oL3_bj9-iP8afKy3uyuOQXgzO5cnl55zfLOhqCWySxrgxZCYGgKj24fCb0R07uHRlFdkXhOdk3cL1W2pG0UIn0HHRFOYZARsCDAVoJTCqv-o2IG2CCEkEOpecs6rQ-KfD7ZQ7tZT01O081Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=JQcf0byO9xt-822mNaCDMP5w2NZAy2mOTT_djrup4dWYcjmy0QTEvbkBy4aQbhpCczQwSWkxhCQbzMTfKeY4F8Acm80Z7yJYBe6n_mEwv80WlSMByJiRB6IgME4rQSGxTJ-VXqJHMYPFsMiZFsY8yi0mrGGyzqnGEiGCyzudhiZHmZSTaGVis5bt27tM6to1_ngptI5oL3_bj9-iP8afKy3uyuOQXgzO5cnl55zfLOhqCWySxrgxZCYGgKj24fCb0R07uHRlFdkXhOdk3cL1W2pG0UIn0HHRFOYZARsCDAVoJTCqv-o2IG2CCEkEOpecs6rQ-KfD7ZQ7tZT01O081Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZC9qIC0Jy5fMdwBv2wtxgOIWKRriRBZtKASDidyMEaANDTH6RL7kVngBiYbPb_RITz4wYrp-KagzNR832U2PP51tmJ6KuKc9B6tXHsKIr_K8mb0ILaaej2usOx-rHMzDuVphPsGIJDpXpOMwGjsceGLwyA0Pcdslcl0878GOj3XIKMhTN0-YQvCxXdTZXPs5sLpw8Uy4Y0MbV6W-60ZrU68dUqagB2B5EStRQ5MsIMTL245_yAVO9ARScdgzSbZ7Mfrv30SVwpE48vGEMJnIPKuUrrRb8MBRRXJHpyQOrAaXq3Nd-5QLPLQBVNAYnBp-veujAn00IQT2aJK9uEcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6nRgCadk5Gp2zJYW514Raz1gDtzgf5AWI2rWJkknnEDT6uWOaXqVeE-Yzyxs5U4_GgJybmmy_HtIiGZVmzEBvlZHN9xzocalWC6WmcbcTVbK_cY0W2VpskMX36tnkdCD6V_AsAPsMrgatrE_xcyAmrjCnlIsSR9oyoUXjzRjuY80GmHdfJs3VmDObfremOYvURbQkjUBTA2k9kr_EXls5iSdpQiPJewbkZHiI_yS5FgmGBskxNaTTVxovyiVzcKNUM5p7m6BsCwhShPqPn7spVPv1N4WXwidNU56zlu2OW2QPyYx4c5cG3G2KFasTf0g9d3ooRyK3qGnaPNt5NPAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyoL5WeSLUVBXKDVEmulsXlOXGH58bqFEkT7PMTG9UDK8c6UHfugQbDth07ZVuiUZpDMNBi80EuxY_r4YOPkVYL-_iZvnejgGajySaGu2CnJyIjlhLnsasBrc7q_Z3dz47HWQwCW1wc7XH5V2I-t2B_UFxc4vHnHDV5cgGJf_pGG9QB5DqYOe2n20qrrKqqoUANsUIb1Wn-E6VSvP4rJAdCtey-6jv5RxAAy43CFDd47-7S3AQW5GETjoc4g0VX94DpZOiA5p9RyiazSVTjSbxlkxWnNx95HjVgBfFjgez3orDJd8Cu2XmhWqtUHQvGpPeKYL4_xKtpQi5UgxebuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOIIzCqXCBpQEPxfVKkn3alPjepm3lvjTm4FPWnRSypQeMNl42laQ6susV20uwYL-o42IYi1n7WjNtQ0EVcs4XrnbxxLFU_D3JXXqItPsg5j8ohN9wfhssryk7vyTlE95mJ3iVH5T58ulgQoGy3_QuVF9x4KLFts8Hsx__2TgK4xQWbPcSYe4lR8mLCzZdlYHzzM9FPJEChlcgYFV-FYQN1er7RHszyOIGFSKUhtUITs8AvkBUEYX4cjMZreu0n46lZr2ECMZ0D2kCaEtkXhkwIPTZQz4-YB1T-Bgk0Vk5Wqi5-dYx3FTXzC8ZubF1dIbcu0QpSjMYJGyt_9A3cJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
