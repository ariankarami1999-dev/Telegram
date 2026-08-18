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
<img src="https://cdn4.telesco.pe/file/iAPiwbzVj1zNLbp5VekDiDWwcDIAa4-kO7InvCF31_TYaNR6iPbUB1nYAAg_C-I7XjzbQK7r5n9ZcTnq_Ym3t4Y-ZHTvHEJoueZGFyeV2nmihtIqxa1FwB3yjhSgyT4wiyruIqQpQlcsx9TYWCaEDKMvsJQZkjCIBsjtr_e-AS8mzGB5UQV8D5mSaXwra7rNmDQDM234XbC7Iy6NgAXcaERU3tXwaRS53I66IVcqo5hREI_buZZ-uOq7xmt2RPQpBCLghANbNFdrq16RlrOSCmaT349gxGqKsuYdTvvy_O6T_bAvwFYHgKlj65KKKKaesBhS-E5rzP1cCaszJhCQeg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 120K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 11:30:13</div>
<hr>

<div class="tg-post" id="msg-70221">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e66075a5.mp4?token=PlIYzeOHIWJrLHgmwhBF_PE8lOnLtwNO4G-Bn2AFiVEaf_RMod_4V_uHMN2i3vnVGQIqV7OyY8ahRoU_oWyrEpNLWtKKWVtUBb1U2BrhthbuIbAJxYxf2Ud7ZvCGh9BEVu3PNqJswjbryLvmWRSAkjTXkO4SwYB8Nv9ey0fEvElPbNJ2rQ84tzvM56DPNL-A3-oXDXf9YBv7OMpZJVpxJrd51AdY6XRp7LF2dSVSA6LpoQMo9zhRFg755AjZZ8mpsZK8qqcziVxfcY9STDEzHgPHg3-NTw2t17oMd_t4yFuFWslJxIMbhGlRjq5IA0yVFi3n14omabuJDf6Pm263lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e66075a5.mp4?token=PlIYzeOHIWJrLHgmwhBF_PE8lOnLtwNO4G-Bn2AFiVEaf_RMod_4V_uHMN2i3vnVGQIqV7OyY8ahRoU_oWyrEpNLWtKKWVtUBb1U2BrhthbuIbAJxYxf2Ud7ZvCGh9BEVu3PNqJswjbryLvmWRSAkjTXkO4SwYB8Nv9ey0fEvElPbNJ2rQ84tzvM56DPNL-A3-oXDXf9YBv7OMpZJVpxJrd51AdY6XRp7LF2dSVSA6LpoQMo9zhRFg755AjZZ8mpsZK8qqcziVxfcY9STDEzHgPHg3-NTw2t17oMd_t4yFuFWslJxIMbhGlRjq5IA0yVFi3n14omabuJDf6Pm263lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایرانی های حاضر در ترکیه:
@News_Hut</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/news_hut/70221" target="_blank">📅 11:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70220">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a948c02f.mp4?token=sCOi0-sEjk_LxhkiZOHqYve-UlEN8aAl5yaWFznpu3_Bnw9Ov7lAdUSkG1Ny4_9HOaIjZ0EMUeRmzEjRz2f9LOMgQImK5TR_aD0WeSxN0Q8AQekorZNloF6LpbmKXOHnflqtuTAfQdntttmxXChW-_SCzDvhCbkyEKpDNMHH5yJsPDatGknAsKyBCarr5IKJ27F_uTYBy_6FYrqz56Nbvpd-jE15_cfWTDRnIvWBSgrJ_P6XxEpl595bPlR_bEvn1COSDCvR6JIItwOX732ox_3enk5X0Eegy9_WglJFYBBgit9Y_ZvOAi5vxEIYz6PzsVCJIEesESchG5brM9sn3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a948c02f.mp4?token=sCOi0-sEjk_LxhkiZOHqYve-UlEN8aAl5yaWFznpu3_Bnw9Ov7lAdUSkG1Ny4_9HOaIjZ0EMUeRmzEjRz2f9LOMgQImK5TR_aD0WeSxN0Q8AQekorZNloF6LpbmKXOHnflqtuTAfQdntttmxXChW-_SCzDvhCbkyEKpDNMHH5yJsPDatGknAsKyBCarr5IKJ27F_uTYBy_6FYrqz56Nbvpd-jE15_cfWTDRnIvWBSgrJ_P6XxEpl595bPlR_bEvn1COSDCvR6JIItwOX732ox_3enk5X0Eegy9_WglJFYBBgit9Y_ZvOAi5vxEIYz6PzsVCJIEesESchG5brM9sn3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇯🇵
وقتی میگن ژاپن تو یه جهان دیگست یعنی این ؛
اومدن خیلی جدی یه سوتینی ساختن برای خانما که تو تابستون بپوشن و با خیال آسوده برن بیرون تا گرمشون نشه یه وقت
@News_Hut</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/news_hut/70220" target="_blank">📅 10:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70219">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4716008946.mp4?token=jVCCZ9uIsdeJjjFB4Jao73IJrOu8xtzydi-WNNOF0_HLxulCNAYknPAFEyUq2k-pzmIuEFZDSYQo9u3AQV9nWqGPMuMUreFD2kBm2CCfhEEbB82XR-3zYAozLphTWgLmkI1VxjHJSejs5kXcP_UvFifQt5u3RO0hPtFy_GCfcXheP1ItU2yTA9_zdW7pQtSgozALM5HBeqCfhr4SeNZ_jsCBbHj_7UITA8jayAdN79NMAKpxh6k9r_2N23TUiEzRjDboeNJhUYyOcZa3rOVBE4qS87ih4yHmVI4ZaYuf6MWPO3a0mf-UR2FMn76Bqu_Upw6jORNeCjnu6eI68yH3Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4716008946.mp4?token=jVCCZ9uIsdeJjjFB4Jao73IJrOu8xtzydi-WNNOF0_HLxulCNAYknPAFEyUq2k-pzmIuEFZDSYQo9u3AQV9nWqGPMuMUreFD2kBm2CCfhEEbB82XR-3zYAozLphTWgLmkI1VxjHJSejs5kXcP_UvFifQt5u3RO0hPtFy_GCfcXheP1ItU2yTA9_zdW7pQtSgozALM5HBeqCfhr4SeNZ_jsCBbHj_7UITA8jayAdN79NMAKpxh6k9r_2N23TUiEzRjDboeNJhUYyOcZa3rOVBE4qS87ih4yHmVI4ZaYuf6MWPO3a0mf-UR2FMn76Bqu_Upw6jORNeCjnu6eI68yH3Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلاغ کینه‌ای؛ سه سال است که دست از سر این پیرمرد برنمی‌دارد.
یک ماجرای عجیب که این روزها در فضای مجازی دست‌به‌دست می‌شود؛ پیرمردی ایرانی ظاهراً نزدیک به سه سال است با یک کلاغ سمج حسابی مشکل شخصی پیدا کرده
طبق روایت منتشرشده، ماجرا از زمانی شروع شد که پیرمرد یک جوجه‌کلاغ افتاده از لانه را برداشت. از آن روز به بعد، کلاغ‌ها هر بار او را می‌بینند به سمتش شیرجه می‌زنند و سر و کله‌اش را هدف می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/news_hut/70219" target="_blank">📅 10:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70218">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7Eqn4nYOPNHuXafBofUgTECH2VrDCyAMk1RbqavfYIJ5efWd9BkfJdFE-GF2Y8kLziVx_In3jmf4yQrE8b_vmQ_FYnhbqeQ2aDGfkBmGrIx-wRwMCeg3XhhWrcnGYGLGprfYQOMogFMcN-ihGk5qM2X_YSqQLQ6UMhINSK1sNIiiytYH1BVibIe8G9mZJfTgWenn98UPZZzNkpkBVaXMszeSccpaGyA1jt5-3uPbxJ8nXjaOscfah9iGA1WrDFTGqeYMFh3z2JkiSH9rJuzuqfnmrxlyr39LmszxJxIDLCY-mkBtVSGbNsVtjII5lN15WDvsfO0hwm13D1qVpWt3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ساعاتی پیش سپاه‌پاسداران به یک کشتی در حال عبور از تنگه‌هرمز حمله کرد:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که یک کشتی هنگام عبور از تنگه هرمز در مسیر خروج، مورد اصابت یک پرتابه قرار گرفته است.
این برخورد به موتورخانه کشتی آسیب رسانده و منجر به تلفات جانی برای یکی از خدمه شده است؛ سایر خدمه نیز تحت امدادرسانی گارد ساحلی عمان قرار دارند.
تاکنون هیچ‌گونه پیامد زیست‌محیطی گزارش نشده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/news_hut/70218" target="_blank">📅 09:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70217">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=D59WOwmgeU7q9eafSCsJ7uNWWS476cDgVIbIHHZ6OQTMsfWLKVOr1ABaLFJeBK8RTUtyfNCZ0y16a7IqP81S2WdyibTzZLT7f6MUI5zbWFyJONGssXP4zXRwojmR1e67Hc__KzzbxZDdbN1lc4RNPdEOWSdxNHpVSMvVILz3IyTWTOYAbctMu6y9hu2FGVr6zeEcEJQm4fm62KQbT9BjDN5m9B9nPSSAQj9w1Y2QTJn87YAVaJseOodNU0hzjxJGGqdWcbK2Vmt_xjTn_ZqnEbLbd2-4luQoz_8R0oqtMBPRr67NaDJgILYv20i9aA7951qseDcQDPtHjzGv-f2sYjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=D59WOwmgeU7q9eafSCsJ7uNWWS476cDgVIbIHHZ6OQTMsfWLKVOr1ABaLFJeBK8RTUtyfNCZ0y16a7IqP81S2WdyibTzZLT7f6MUI5zbWFyJONGssXP4zXRwojmR1e67Hc__KzzbxZDdbN1lc4RNPdEOWSdxNHpVSMvVILz3IyTWTOYAbctMu6y9hu2FGVr6zeEcEJQm4fm62KQbT9BjDN5m9B9nPSSAQj9w1Y2QTJn87YAVaJseOodNU0hzjxJGGqdWcbK2Vmt_xjTn_ZqnEbLbd2-4luQoz_8R0oqtMBPRr67NaDJgILYv20i9aA7951qseDcQDPtHjzGv-f2sYjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بخشی از صحبتای دیشب ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/news_hut/70217" target="_blank">📅 09:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70216">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31325063ce.mp4?token=UPTZANFOgZNYd82wAjAhpOSa8k5s-1_4k1jq06gPPFrweEUMnLwjpIVCXHPytrEuT3vM3_1wZRenzEAXW-GAzistlvH3rrLJQYLYRq3iSewchQD0d5urxZEQQNNQI6fqsWWDcZJBzcjXfoux5d3GFH2CSQaqZUhXg5BV3GyCA3AI4PUTvCqzeY5IZCgKp1lJTR9yUL7o8SwLXCqviPgkNXTkO55y6rtBs-2hZr-gvTO5hhrf-W16VvzEHqAu6Ki9idimLV-AoKMdtwH4lSZc9o20z2vxRUJNrkCMDs2WTR4ObrL9RiGNEA1Kl822-q792MoBzLJloBv78z4hcqI_Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31325063ce.mp4?token=UPTZANFOgZNYd82wAjAhpOSa8k5s-1_4k1jq06gPPFrweEUMnLwjpIVCXHPytrEuT3vM3_1wZRenzEAXW-GAzistlvH3rrLJQYLYRq3iSewchQD0d5urxZEQQNNQI6fqsWWDcZJBzcjXfoux5d3GFH2CSQaqZUhXg5BV3GyCA3AI4PUTvCqzeY5IZCgKp1lJTR9yUL7o8SwLXCqviPgkNXTkO55y6rtBs-2hZr-gvTO5hhrf-W16VvzEHqAu6Ki9idimLV-AoKMdtwH4lSZc9o20z2vxRUJNrkCMDs2WTR4ObrL9RiGNEA1Kl822-q792MoBzLJloBv78z4hcqI_Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
گزارشی از مجتبی پورمحسن:
همزمان با تایید تماس محرمانه دولت آمریکا با فرمانده کل سپاه‌، ترامپ، در پایان مهلت ۶۰ روزه برای توافق، از تهران خواست تسلیم شود.
اما وب‌سایت اسرائیلی وای‌نت، با انتشار جزئیات تازه از زندگی مخفیانه مجتبی خامنه‌ای، از تسلط سپاه بر جمهوری اسلامی خبر داده.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/70216" target="_blank">📅 08:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70215">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/70215" target="_blank">📅 01:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=uqbcHlZZVa9NgLE0yKiACf6ydZ3ADJ80Kh9e_wKH-GjJAhDvtqMbIoT_wwsyNmXSXTxWMtbCUJl0Z8fVEWuvnrPNw6FXgESlC0um2Nfy7jALIv_bXyFyGrmGeLeScz9IWVggEHZMAvY99dJEwG9FiWk6H07gEOz0fF54UmPNYHemIHMA9wM6yc7U1x53KdIaK2m2wN-Mdqp1GTInIdkyeuwuoX0YYL-AVnq0HDEJe5snFZC3uQTDNUYg6CHU7A0gyqZrz8269qmp_-LY3fFkn2Z6fjBP-LgM1sQh5wfvw2zivfxGndwPzS3YUMZaMuR3AxMUazPH83o_BoQNDrMquA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=uqbcHlZZVa9NgLE0yKiACf6ydZ3ADJ80Kh9e_wKH-GjJAhDvtqMbIoT_wwsyNmXSXTxWMtbCUJl0Z8fVEWuvnrPNw6FXgESlC0um2Nfy7jALIv_bXyFyGrmGeLeScz9IWVggEHZMAvY99dJEwG9FiWk6H07gEOz0fF54UmPNYHemIHMA9wM6yc7U1x53KdIaK2m2wN-Mdqp1GTInIdkyeuwuoX0YYL-AVnq0HDEJe5snFZC3uQTDNUYg6CHU7A0gyqZrz8269qmp_-LY3fFkn2Z6fjBP-LgM1sQh5wfvw2zivfxGndwPzS3YUMZaMuR3AxMUazPH83o_BoQNDrMquA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a26
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/70214" target="_blank">📅 01:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1x8L-GesbWFhlqM6mb_V-zyQgiRGiUNJpVWs3An2x1mQYuEGsAfTqMMCBIsOJrgcLcn2P7QF7Wv6VRDm92MG39aaFVMV8llIlnP4-9-uUbK1E1A-cBr_kLvhzA2Wz22CE1ZO0_eaiVMwBLY0epRlBw62obcY1BgxJgZ9jVfAmvK3GiTa0qRsIcoBHZap_ypn_zPy1VLDYGf8r_JaQh3-UeIlo85VyZCAn6PlZHBDGDic3qex9d-7JaSnNENaf7UrLofmVpG8rGwJE5XUmHOqqgkhc9CVSfFZJOmOLyu5TFZiiNAzhB-InMxHAJ4GWUvXvtcpIpmMKdri-4hBIpvtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید املاکی در تروث سوشال:
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70213" target="_blank">📅 01:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7cb5678c.mp4?token=Vk5KKRW0DXPs2qax_-nesr1e3D_nXNZl6naQak3MVFh5XkZupku0gpgEMHYOGZAGqoj2kBlG00jzY4QXnNtEuGi6kwgUaRu1et-mHkLbgWfAD8macUmhdoyoUQhgeQEVJCOK-MpesxVchprX2awKYaqseGs4vvXbEb7oSgogyJB6qvANRthHy6M1wAgiGmX0OeO7Yyw0uUbU6wdje8nmy6lzl8n8oiwM8xpIrU3G7t89qY-6nE_48eikA7vFB-qH7ltnYUnujPM3m1q7yLAxKQGCuqdclhZGZT_t3oZM9ebuzjtrgQpATR6qGb10zpl0NuC051GUHGFpm_Emminw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7cb5678c.mp4?token=Vk5KKRW0DXPs2qax_-nesr1e3D_nXNZl6naQak3MVFh5XkZupku0gpgEMHYOGZAGqoj2kBlG00jzY4QXnNtEuGi6kwgUaRu1et-mHkLbgWfAD8macUmhdoyoUQhgeQEVJCOK-MpesxVchprX2awKYaqseGs4vvXbEb7oSgogyJB6qvANRthHy6M1wAgiGmX0OeO7Yyw0uUbU6wdje8nmy6lzl8n8oiwM8xpIrU3G7t89qY-6nE_48eikA7vFB-qH7ltnYUnujPM3m1q7yLAxKQGCuqdclhZGZT_t3oZM9ebuzjtrgQpATR6qGb10zpl0NuC051GUHGFpm_Emminw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🇺🇸
جرد کوشنر درباره ایران :
ترامپ فعلاً فشار اقتصادی رو بیشتر کرده
اگه ایران حاضر بشه توافقی رو که درباره کنار گذاشتن توان ساخت سلاح هسته‌ای داریم جلو می‌بریم، نهایی کنه، ترامپ حاضره یه توافق خوب به نفع مردم ایران ببنده
ولی فعلاً ایران دنبال انجام کاری که از نظر ما منطقی باشه نیست
الان آمریکا با بخش‌های مختلف دولت ایران خیلی جدی و بیشتر از همیشه در ارتباطه و گفت‌وگوهای خوبی هم داشتیم
البته بعد از این همه سال، اعتماد زیادی بین دو طرف نیست.
ایران داره جدی مذاکره میکنه و این مثبته، ولی هنوز به نتیجه نرسیدیم.
ترامپ هم عجله‌ای نداره و وقتی توافق درست آماده بشه، می‌ره سراغش
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70212" target="_blank">📅 00:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20632f388.mp4?token=Qf1RLoXsRl_BnVVoLYucXv0X6uU7GiIhWAGBAKUM5RrqCkeEXVi5PTy1VQx3YKRclyw1h1dBIMSUvNZQEV-H1uVXASECMPEovoZaTfdSoAVNcwM9JPyKzt7aWOPF0nbzowNGL9ZWohsaXgcMeB_c_77KoEoypZ1mLIuF7RCrtP_KTCrfIryT_-EfuxI-9BOmUskXKb1N5IKi742HI9qlWapeoOBYhLomZQjnpXnNTGfSFlqNoD_L89gcjG1h-xswPnIlS2eD66K3M8XktVyC52DCqs9mEUeYWRWq18k1Bnt-Rl21pp-q_429XIVNxFcSjhYkfW9ZVK7F7OZTv-37Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20632f388.mp4?token=Qf1RLoXsRl_BnVVoLYucXv0X6uU7GiIhWAGBAKUM5RrqCkeEXVi5PTy1VQx3YKRclyw1h1dBIMSUvNZQEV-H1uVXASECMPEovoZaTfdSoAVNcwM9JPyKzt7aWOPF0nbzowNGL9ZWohsaXgcMeB_c_77KoEoypZ1mLIuF7RCrtP_KTCrfIryT_-EfuxI-9BOmUskXKb1N5IKi742HI9qlWapeoOBYhLomZQjnpXnNTGfSFlqNoD_L89gcjG1h-xswPnIlS2eD66K3M8XktVyC52DCqs9mEUeYWRWq18k1Bnt-Rl21pp-q_429XIVNxFcSjhYkfW9ZVK7F7OZTv-37Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
موسوی، نماینده مجلس : بنزین ما اصلا هم ارزون نیست؛
اگر حداقل حقوق مارو در نظر بگیرید، برخلاف حرفایی که گفته میشه ما بنزین ارزونی نداریم.
ما با حداقل حقوق، میتونیم 130 گالن بنزین 3 هزارتومنی بزنیم، ولی یه نفر تو آمریکا با حداقل حقوقش میتونه 750 الی 800 گالن بنزین بخره.
ما اقتصادی داریم که طرف یخچالش خراب میشه، میره زیر خط فقر.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70211" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7953006a94.mp4?token=O2CJqp4uK3uY3mEqnIDH1pNtNH9frZpyCBxnpsQjz9xaZcRoaUTJJUzUyRmUHPbnzx5hMrO0ll4cp6WYa6BbzcMt0buNJqviIqC4L3gAmhnHXvwf-9wjxM2MQeUewKtFArPJPBZEgK8SRvpLBpSypq6Ob6_frypwtDTtrW0zf5i0x0HrhfYD6C1Rrn4VsmHYeKrlgaVarH2dOVHqkVC1mQLPgaE1zUEo1q-pjUcbi2SIA2CGpwkHuFGdn9x9pDkld6veFpWOFs-Y7PuYLMAJclQLK_JhV33qhJuhXGuny_eh5E69LtT395xvw3Q0Mmr0WudqSLkeoElcM3BLdS3f9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7953006a94.mp4?token=O2CJqp4uK3uY3mEqnIDH1pNtNH9frZpyCBxnpsQjz9xaZcRoaUTJJUzUyRmUHPbnzx5hMrO0ll4cp6WYa6BbzcMt0buNJqviIqC4L3gAmhnHXvwf-9wjxM2MQeUewKtFArPJPBZEgK8SRvpLBpSypq6Ob6_frypwtDTtrW0zf5i0x0HrhfYD6C1Rrn4VsmHYeKrlgaVarH2dOVHqkVC1mQLPgaE1zUEo1q-pjUcbi2SIA2CGpwkHuFGdn9x9pDkld6veFpWOFs-Y7PuYLMAJclQLK_JhV33qhJuhXGuny_eh5E69LtT395xvw3Q0Mmr0WudqSLkeoElcM3BLdS3f9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی، نماینده مجلس:
درباره احتمال جنگ زمینی با آمریکا گفت در چنین نبردی «جنازه» نیروهای آمریکایی نیز به خانواده‌هایشان نخواهد رسید.
تصرف یک پایگاه آمریکا در عراق، کویت یا بحرین می‌تواند سرنوشت جنگ را تعیین کند و به آن پایان دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70210" target="_blank">📅 23:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70209">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa369bc00a.mp4?token=UrHSy4lnR2j_l4OtmC8khcJTAqrWurwQwpQ9KfwEZmgu-vl7LGbVdZqA3u1FIy7d7f8oQwhfJvRuI9thnb2H5nDcdY9P1wsvQ6DyQ78l3kYJ6ETCfiVGnT5tHVFVsh6-K5mDHsYv5ClF_9-DkqyYhdgslHLt5Yov2qaeC63BY24-51meozvDtHPO3606l69e7fgSUUlDA-VPpzT7NduUC6UOoTcos3lpj1QQvt5lxfew79PsaN2BUqNC6PR2YZPpDHtmq3puc7mGeDFM-nk1jt-X11DuV50Mp9Kw4J_Jq_pPKIk6tuL0oZWayoS5keLBMSklrI6DhTAuD0rrsoE3vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa369bc00a.mp4?token=UrHSy4lnR2j_l4OtmC8khcJTAqrWurwQwpQ9KfwEZmgu-vl7LGbVdZqA3u1FIy7d7f8oQwhfJvRuI9thnb2H5nDcdY9P1wsvQ6DyQ78l3kYJ6ETCfiVGnT5tHVFVsh6-K5mDHsYv5ClF_9-DkqyYhdgslHLt5Yov2qaeC63BY24-51meozvDtHPO3606l69e7fgSUUlDA-VPpzT7NduUC6UOoTcos3lpj1QQvt5lxfew79PsaN2BUqNC6PR2YZPpDHtmq3puc7mGeDFM-nk1jt-X11DuV50Mp9Kw4J_Jq_pPKIk6tuL0oZWayoS5keLBMSklrI6DhTAuD0rrsoE3vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری لفظی ترامپ با خبرنگار سی‌ان‌ان:
🇺🇸
ترامپ: ساکت، ساکت، ساکت. خیلی بی‌ادب هستی. ساکت. از کدام رسانه هستی؟
🎙
خبرنگار: من از سی‌ان‌ان هستم.
🇺🇸
ترامپ: شما «فیک نیوز» هستید. ساکت باش، ساکت باش، ساکت باش. تو یک خبرنگار جعلی هستی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70209" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9432d377e1.mp4?token=H_kiXViWXMuDdVGZmufRPZRJwVFrZuSyCdOmAhisswfNhsKj3nXlU55x4FFKktUC604Dxt3SnI8FR8brXmfJoxIASAVOFuVTGAvjQ0eaiFkVSRF84EecranX1pxWjUEsKQV4bP-k83v9sB2FmDnXhEkl76xIsTS2iPQkFjckaf4yyXVLJwaUoWM-b8wmPc1UXOz1uDRqIW_L8rMIfJt_bNIq0V6uclpw3yEG3NT7srIJcrcJJPPTWLlgn5t46hOWxCfaAuIMfr7thbF2pSxQgVg_uoT9tAXvG_kZHa0OTAAo2yabW1b1opTlpj1ggcsihEpK3Gqrw5BImw0SmHeylA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9432d377e1.mp4?token=H_kiXViWXMuDdVGZmufRPZRJwVFrZuSyCdOmAhisswfNhsKj3nXlU55x4FFKktUC604Dxt3SnI8FR8brXmfJoxIASAVOFuVTGAvjQ0eaiFkVSRF84EecranX1pxWjUEsKQV4bP-k83v9sB2FmDnXhEkl76xIsTS2iPQkFjckaf4yyXVLJwaUoWM-b8wmPc1UXOz1uDRqIW_L8rMIfJt_bNIq0V6uclpw3yEG3NT7srIJcrcJJPPTWLlgn5t46hOWxCfaAuIMfr7thbF2pSxQgVg_uoT9tAXvG_kZHa0OTAAo2yabW1b1opTlpj1ggcsihEpK3Gqrw5BImw0SmHeylA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:ایالات متحده به دنبال تمدید یادداشت تفاهم با ایران نیست.
ایران در مخمصه‌ای بزرگ گرفتار شده است. وضعیت کشورشان آشفته و نابسامان است.
ارتش آن‌ها به‌طور کامل شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70208" target="_blank">📅 22:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70207">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae2f33929.mp4?token=eHxIRDlt3Sfr7qK_RoU0DM_yhrtbdlCQal43zS-TUiiPV0t8oAxr2v6Mmu6quEgGDD0VXb9gTGrstjtDRSuAj3rN4a_dSPLeJq2mO6SJhEeTfD6ymzzu0YUp6dtffdjCj0d5zvnPDxSX3ptHr4D1cNCM2f39LUtGxHOqZFW53xYuwuTORFAWz63ZRK4lR0vfQ9YjRvIuNIFnllUow23YDTIurLPfsnsxAm2r9OZvuU2su-Cut9_DONHdp2vSKssKU2_x3mEUAuicHN3AbuO7k7y-8h-as4WfpfwlNr8hBas5R3zZbess9KQ3U5vpHlzkMXP6NYdFWvSDZA4XMa4ylw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae2f33929.mp4?token=eHxIRDlt3Sfr7qK_RoU0DM_yhrtbdlCQal43zS-TUiiPV0t8oAxr2v6Mmu6quEgGDD0VXb9gTGrstjtDRSuAj3rN4a_dSPLeJq2mO6SJhEeTfD6ymzzu0YUp6dtffdjCj0d5zvnPDxSX3ptHr4D1cNCM2f39LUtGxHOqZFW53xYuwuTORFAWz63ZRK4lR0vfQ9YjRvIuNIFnllUow23YDTIurLPfsnsxAm2r9OZvuU2su-Cut9_DONHdp2vSKssKU2_x3mEUAuicHN3AbuO7k7y-8h-as4WfpfwlNr8hBas5R3zZbess9KQ3U5vpHlzkMXP6NYdFWvSDZA4XMa4ylw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما گفتید اگر عمان مانع بازگشایی تنگه هرمز شود، آنجا را به شدت بمباران خواهید کرد. آیا می‌توان گفت که صبرتان در قبال عمان — که یک شریک راهبردی است — لبریز شده است؟
⏺
🇺🇸
ترامپ: فکر نمی‌کنم رفتارشان خیلی خوب بوده باشد، اما ما خیلی راحت از پسِ آن‌ها برمی‌آییم؛ درست مثل کارهای دیگر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70207" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70206">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9810e545.mp4?token=p0xU687pSV1cucnuii-_t2C7aJAxp_sn0ZtaZPXtNn8tYhyMzKk8RUzQZy26duTSS18iOvIsb9Loa7iXKe08JP6uxXEofEO0Xbq7gS94ZIdRCuXl5SouTqUjXlAKi5_OEhGoCzvTayDGqIGRwy6WuUyZTkj5jZXVrEH1Hw_f4bZ94GS-wsL9qQtONYm6tE7QTr2vXlF5BWVPrSy-5P3TOUIglrFyNvfsWNStXTDDhDdg1kPEpnnemP7CRCaT3-D8r4fyPkZRC9b4cBVg09mVHexqak4svF0Yji03XZygnmflS9fF6ZwIKARQlhGJo5VKR2LmLYyT2M6haPee0n_gOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9810e545.mp4?token=p0xU687pSV1cucnuii-_t2C7aJAxp_sn0ZtaZPXtNn8tYhyMzKk8RUzQZy26duTSS18iOvIsb9Loa7iXKe08JP6uxXEofEO0Xbq7gS94ZIdRCuXl5SouTqUjXlAKi5_OEhGoCzvTayDGqIGRwy6WuUyZTkj5jZXVrEH1Hw_f4bZ94GS-wsL9qQtONYm6tE7QTr2vXlF5BWVPrSy-5P3TOUIglrFyNvfsWNStXTDDhDdg1kPEpnnemP7CRCaT3-D8r4fyPkZRC9b4cBVg09mVHexqak4svF0Yji03XZygnmflS9fF6ZwIKARQlhGJo5VKR2LmLYyT2M6haPee0n_gOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: اعتبار تفاهم‌نامه امروز به پایان می‌رسد. آیا به دستیابی به توافق با ایران نزدیک‌تر شده‌اید؟
🇺🇸
ترامپ: بیایید ابتدا کارمان را با رایدر  تمام کنیم؛ بعد که تمام شد، به چند تا از آن سؤال‌ها پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70206" target="_blank">📅 21:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70205">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4e1ff391.mp4?token=DulpzRUXaNydUtB4xcdwCapkVdG3gsxMeWDxyodfB1QKqhAokrJt685_Ukoig4CYbNFagghyomEn45HCP2ef8kvvAGXww_Kqbbf4m7NC1m_Id3piGxXjumiGZV2ORpB3zDg9FrxxtFEz4fvPXilciBDSv6_35qcZs63V8XOPnAHUlm-6MNdNAz99BEx_TYl5ArUUAvN_d4awN7bYhiW2HKCD58x65v51MqN9XvefZrMLrRtY13bEJOk285K_IFqD4LhI2xFMdKQ0WsHdoVbKEwdbdnNg8OdaOlPG6qa5j7Aog5yvw14TdX_fcDVED9UzSPB9WkuYQjuL6WSCsaFrz1HlMO33otUbgbzppWuBzFisgq0KGKuWaLQy429mXsIibAIipSnfB1CHsqaDHpM4RCTFOJY_l8GSm_Z9r9cYHtaSTQJQjOBlsBUDbPCPsm7hBr4dZIaDXs1x3_2Iu7GNUnv0bsORAQJPR5-nUtFVwCSuGsMCOJkTFUUQYMF53mQLJ4IcAfEH76sCiLqcHqF8uDHdrISCJej4toVV5RyecGsOs2S22ns4t5keovdH3ORlVW7bceYV5kVX1dSm8MHu5jLqAtlguXpE5H8q2Zp5NV61yi9CPTvdeA-8wh51v9Ul9LR5gLlURxs0bDhf_TFuBHXZoWkEfbzMY3QrkBb4550" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4e1ff391.mp4?token=DulpzRUXaNydUtB4xcdwCapkVdG3gsxMeWDxyodfB1QKqhAokrJt685_Ukoig4CYbNFagghyomEn45HCP2ef8kvvAGXww_Kqbbf4m7NC1m_Id3piGxXjumiGZV2ORpB3zDg9FrxxtFEz4fvPXilciBDSv6_35qcZs63V8XOPnAHUlm-6MNdNAz99BEx_TYl5ArUUAvN_d4awN7bYhiW2HKCD58x65v51MqN9XvefZrMLrRtY13bEJOk285K_IFqD4LhI2xFMdKQ0WsHdoVbKEwdbdnNg8OdaOlPG6qa5j7Aog5yvw14TdX_fcDVED9UzSPB9WkuYQjuL6WSCsaFrz1HlMO33otUbgbzppWuBzFisgq0KGKuWaLQy429mXsIibAIipSnfB1CHsqaDHpM4RCTFOJY_l8GSm_Z9r9cYHtaSTQJQjOBlsBUDbPCPsm7hBr4dZIaDXs1x3_2Iu7GNUnv0bsORAQJPR5-nUtFVwCSuGsMCOJkTFUUQYMF53mQLJ4IcAfEH76sCiLqcHqF8uDHdrISCJej4toVV5RyecGsOs2S22ns4t5keovdH3ORlVW7bceYV5kVX1dSm8MHu5jLqAtlguXpE5H8q2Zp5NV61yi9CPTvdeA-8wh51v9Ul9LR5gLlURxs0bDhf_TFuBHXZoWkEfbzMY3QrkBb4550" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دختره ول‌کن رامین‌رضاییان نیست و یه ویدیو پر کرده و حسابی گرفته رو رامین:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70205" target="_blank">📅 21:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70204">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=mgt7ciiPL_ZaFStablzlw6fskFXLRsXiKpzFLo5EJcwvouUbVO1InuxJVO92M2wF258u6K1Q0lCKxzt9dGxakBufhUdPY2_e4FfKVfvku9rzuoF-2DvArP1Y3mh_Vmb2vK8nFCnuWkz3Q_DAWBckyBhTdH3VATgIbp2YevLBZ1gflw5DSo5tvnsRLyeUJ2SSutAdSui1u96QwQrXi4bw6yjd2Xvt9EjmQ_nD0zKkAqimUaBRmo5_xQgwbi0MLpUuP0Qr8xCTm-eNhm0NSD_MGxjuLjXjsYLShoPHnbkNBDCcRwBrvK4wgT6pB74tU4wL6_Yn0lpSWX8jhVOBzpk93Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=mgt7ciiPL_ZaFStablzlw6fskFXLRsXiKpzFLo5EJcwvouUbVO1InuxJVO92M2wF258u6K1Q0lCKxzt9dGxakBufhUdPY2_e4FfKVfvku9rzuoF-2DvArP1Y3mh_Vmb2vK8nFCnuWkz3Q_DAWBckyBhTdH3VATgIbp2YevLBZ1gflw5DSo5tvnsRLyeUJ2SSutAdSui1u96QwQrXi4bw6yjd2Xvt9EjmQ_nD0zKkAqimUaBRmo5_xQgwbi0MLpUuP0Qr8xCTm-eNhm0NSD_MGxjuLjXjsYLShoPHnbkNBDCcRwBrvK4wgT6pB74tU4wL6_Yn0lpSWX8jhVOBzpk93Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
صداوسیما اومده یه برنامه ساخته به اسم«با عرض معذرت»که محتواش تمسخر ترامپ و کابینه دولتش هست و قراره از اواخر مردادماه پخش بشه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70204" target="_blank">📅 20:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70203">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇮🇷
فارس:
یک نفتکش اماراتی در نزدیکی قشم توقیف شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70203" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70202">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf270f369e.mp4?token=bnaDZhP7e7l5JzulGs1IHH5s6-t2S5M1dv7AGZ9WI73mNtgAXGY2Qr1SBz5Re3bflVJrokgX1tyeu46ZVor49wQjEnQwIhIEBnnOzM0ZaLSawvQe2O5MQ1vMiuJMFk04UI7ar8xVlb7bBnkNowTPqu6cwdfbzrXjB_cBOm2gybJ_dgltdON4L31mg-0NOziPOQJD6fELoXR2K9xmXKff6L3QHFHOpaL01tZqWwRH-6KyVZ8qWY5-7EdxUSlTCmQVAgNhBDUS8VTaoV5W1wn3uva9N7jv6VS3PIBh6BvMQvrfn-K3jy5DAx6KStWl6vlpid9CCQQNdVHR3in-sphgig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf270f369e.mp4?token=bnaDZhP7e7l5JzulGs1IHH5s6-t2S5M1dv7AGZ9WI73mNtgAXGY2Qr1SBz5Re3bflVJrokgX1tyeu46ZVor49wQjEnQwIhIEBnnOzM0ZaLSawvQe2O5MQ1vMiuJMFk04UI7ar8xVlb7bBnkNowTPqu6cwdfbzrXjB_cBOm2gybJ_dgltdON4L31mg-0NOziPOQJD6fELoXR2K9xmXKff6L3QHFHOpaL01tZqWwRH-6KyVZ8qWY5-7EdxUSlTCmQVAgNhBDUS8VTaoV5W1wn3uva9N7jv6VS3PIBh6BvMQvrfn-K3jy5DAx6KStWl6vlpid9CCQQNdVHR3in-sphgig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
جمهوری اسلامی، شروع کرده هر کسی که جاوید شاه میگه یا به مسئولین توهین می‌کنه رو بازداشت کردن!
یه نفرو دستگیر کردن، حالا جرمش چی بوده؟ توی کامنت اینستا به مسئولین فحش داده
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70202" target="_blank">📅 20:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70200">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNKRYtFYfpHhsbLIiJfB6wrKkD6inwPUSXe2BhLsOSGNhEp9wr_xOwXqb4R6pL3c9HaeyBBm-Ld2nuwxTmfURxcw6j0jBbxtHWMU_13pEZR7TPNsIAwMMt_NYhfVkf_AdoOpYgWQmfSCDvY-pTXlEZkKZNwb5YOpriF0jsVMVKEUD0CSCPKQdj5ivrfGhbyGxzCuuGidUCsJSmHcfiWZjiJZSaI6LbEXY9t_gYj-vE5LRQWOpLq_CNNiZn5X9NUQGuX8o8dd3-a6KFIhYGDkHwLZx6w3uauGuWbT5w2DSBxI6F5RfWGRroDyR0oCxfpb1KmfySDvcndVcQzGcIv0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imWt3CzLgE29o0wn3Jz8VIU2BLQOOePpWGtpPCovFRcw8ky9gFKBK_pd5uf2p5K4C0_aXs_csYWNHTZKojF_cY1nQjfXzwHiTWzHlKiRpX8Z8hsTWs5SEF913n5gMRyWDHTYinJ3p2luDXKeZ4b5bC9JcA1E60tzifVvm6vnjVS0XMzA3zizH1X0bon_tLv9I_NFCzTUTlaA3oz07my7lcU_lqvAgZiDChDsq6sWg3Svw1qYwdG0FT_M8Q5H7NMP9IIO-7WSqVs9MiiWu45P_96_9n0lcE4iCSSLkUvep6HhAw9LtKfgrPUQmsg670HuwXalv2ZhNZTplTb2v7eWFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
استوری های جدید گوهر فرشاد و افشاگری های جدید از رامین
رضاییان
:
جول فرشاد: رامین ازم میخواست تیری سام بزنیم.
رامین ازم درخواست محتوای جنسی میکرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70200" target="_blank">📅 19:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70199">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7157f499e9.mp4?token=K57-b9dmZbp7spgTruUBd5Xg-Gc6e5BoIlufkCeXtUMqdWdjxF2-_psB00ecs-hM9YRNMVQZL9Q3FVisVRnhO3BPjxfjREYCiowkqlcpQxCT22HC4C-_9t6eDTOzkRmHm-A_K9KsTwTZuzBlgHJdnXutIiHQRIJpgLdzvoOZTuYYoxcgo-Bdy9fBpt4MITJVIbNSjg9vogJRc1piThLNgdFe0ar9Vqp_Cc7Nx58syFeOF9jooe3ZnRuNcnCn6tSxA5E7ciCW8wIeOl6al_cMNwsQ3ha1byrqehtuYa2MqFLvzGVSG0fqvREPgFZdVGs94oW7SbGz5TtTyifP6JTxvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7157f499e9.mp4?token=K57-b9dmZbp7spgTruUBd5Xg-Gc6e5BoIlufkCeXtUMqdWdjxF2-_psB00ecs-hM9YRNMVQZL9Q3FVisVRnhO3BPjxfjREYCiowkqlcpQxCT22HC4C-_9t6eDTOzkRmHm-A_K9KsTwTZuzBlgHJdnXutIiHQRIJpgLdzvoOZTuYYoxcgo-Bdy9fBpt4MITJVIbNSjg9vogJRc1piThLNgdFe0ar9Vqp_Cc7Nx58syFeOF9jooe3ZnRuNcnCn6tSxA5E7ciCW8wIeOl6al_cMNwsQ3ha1byrqehtuYa2MqFLvzGVSG0fqvREPgFZdVGs94oW7SbGz5TtTyifP6JTxvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
فرمانده کل ارتش:
«اخراج ایالات متحده محقق شده است و آن‌ها دیگر اجازه ورود به خلیج فارس، دریای عمان و تنگه هرمز را ندارند. همگان باید بدانند که پایگاه‌های آمریکا به هیچ وجه قادر به بازگشت به وضعیت پیشین خود نیستند و ایران هرگز اجازه چنین اتفاقی را نخواهد داد.
تنگه هرمزِ مقدس، یک ظرفیت ژئوپلیتیکِ خدادادی برای ملت ایران است و این اهرم قدرت هرگز به وضعیت سابق بازنخواهد گشت. یکی از میراث‌های رئیس‌جمهور آمریکا، فعال‌سازی همین ظرفیتِ تنگه هرمز بود.
ما از وجود این ظرفیت آگاه بودیم، اما بدون این نبرد، آن ظرفیت فعال نمی‌شد. هر هزینه‌ای که در این مسیر متحمل شویم ارزشمند است و ما تحت فرمان فرماندهی معظم کل قوا، با تمام توان از این ظرفیت حراست خواهیم کرد. این اهرم قدرت، یکی از پیش‌شرط‌های پایان دادن به جنگ به گونه‌ای است که سایه جنگ را از سر ایران دور کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70199" target="_blank">📅 18:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70198">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70198" target="_blank">📅 18:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70197">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jzbfu74JilEFdYP-rdu1x8fRPMhFE_4o5Zhcvu6iTKZC-NIEy8fALcZKdAU1a5JWs8KBLs3PzyUdGtUDTtdtDP90vS3BR1HA4DBDdNQc9yAQMFNgGSqROreUuMuEYmMSXhOD68mJLuualYbuIBL-4kSLjgO5cZh6tNYYlBwAIzK3DgulSyS_vcFbAyZ-f-gLECG4CzzA1Pusu1DVzkqnR4KPUD9uifUU_vmyKpp_sqI8-uPcaPI1uB7tdL02wjLWgaMEHRqCwCQgEKD5JT6mWg_UVwxeZq4P5PHBtTpFjuIcBluFFiTlWqbmHZUxihQHVCJI3iDC6NBnsYl42HOZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g26
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70197" target="_blank">📅 18:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70196">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBR9xLhr3UI4rGwRy5x-cyQdyF7IgWsEBYgTqnlrOR92BH3T6nh5baG0DLENBrbZnrD10HKwWIormzbVe0B96p-J2bZNatj_eh7UhqX8VaybuaJNWrzp872ZfP_nrMWfso4X7eqsvQUeQUCidkpXz25FrjYtoDpKYyU6NaUiCmbFSzs92L5P32-PExjSxYluYcAY908cZ_D2JYBqT8TzFZuAllKGaSn8BOFnHKaDrhP8zG_grZjT0zY4HL56wnvUEGtfkSdNsD4MjK4hsJQBeXQAz1ixJ5K7hvQFAXicg1Uxrt4YuenWzSPGC9VEDPLP97xtyXLWdabnno64RtVtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
رویترز: ضرب‌الاجل ایران به ایالات متحده؛
ایران به ایالات متحده اولتیماتوم داده است؛ یا به دیپلماسی جدی بازگردید و محاصره دریایی را لغو کنید، و یا با گسترش دامنه جنگ مواجه خواهید شد.
به گزارش رویترز، این ضرب‌الاجل — که گفته می‌شود حداکثر چند هفته مهلت دارد — از طریق پاکستان و قطر به اطلاع ایالات متحده رسانده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70196" target="_blank">📅 18:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70195">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af0d57a79.mp4?token=TxCUB0CocfcewxqZFHQTEiQCVHUZg8ixvKWBimVBn7vhRT7xsdLpdhza4ujL2gA5oIWjan4FXpeRXx0HXJ7Dreu6wElgMPOxjWRZZ64CPtFLuX2PGOgp69r_UAQUVetoIoLGSQSd58dxdrs-iamJyDDr0uJ8YfPkn7YO1K30iVD0S-2mtc0DmlOKOrgrX0QztfHpBiPKZH46nJvapAZvWNrkaSe3rAbMx12gNOTiel782b36hrE5_nHjFt0lx_3tODOp0H1WZ8wokarJi-r3H3egQ9ZC6B3JdarwCeV5LG82KGAAyly9KiCi7gk0SXI3HoDnaEVlNtYTmiwKLmyKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af0d57a79.mp4?token=TxCUB0CocfcewxqZFHQTEiQCVHUZg8ixvKWBimVBn7vhRT7xsdLpdhza4ujL2gA5oIWjan4FXpeRXx0HXJ7Dreu6wElgMPOxjWRZZ64CPtFLuX2PGOgp69r_UAQUVetoIoLGSQSd58dxdrs-iamJyDDr0uJ8YfPkn7YO1K30iVD0S-2mtc0DmlOKOrgrX0QztfHpBiPKZH46nJvapAZvWNrkaSe3rAbMx12gNOTiel782b36hrE5_nHjFt0lx_3tODOp0H1WZ8wokarJi-r3H3egQ9ZC6B3JdarwCeV5LG82KGAAyly9KiCi7gk0SXI3HoDnaEVlNtYTmiwKLmyKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اخیراً عرزشی‌ها این فیلم رو با موضوع «فیلم لو رفته از نشست مجتبی خامنه‌ای و پزشکیان» به مغز نداشته بقیه عرزشیا قالب کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70195" target="_blank">📅 17:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70194">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:  ما یک کانال ارتباطی مخفی با سپاه پاسداران انقلاب اسلامی داریم.  ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم.  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70194" target="_blank">📅 17:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70193">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db02877d6b.mp4?token=X20XmLT5xBFnECpNMymUHdPF_QADnqCiG733pgJVUctZcAY1RHvpmaaZUdnhhfcRXELSv5vYgWsDD7ICHWi1-R56f74M2YsguqQ0Irn2SpmPz9kxscSBlNQAuLB2fbiwc4cT48YVODLtTsZ21uHy59C9mbhpLW3usnyl5AVtChBFoETgNYMdY2vrBEREpddUeSGBG_0eP9VSj_xXgWzE_1TbXPZdN_Wq1t9z1MXs4jXeBGT2iW3VZzzAIi-u0g0QbJgADX-9zE-nOg2pH-J453bIHSlcuq9FmoR7aHsbNs7zp1MciGLjsaiTJ6t5q5UstWycV3gGs8TsQiREWmKPsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db02877d6b.mp4?token=X20XmLT5xBFnECpNMymUHdPF_QADnqCiG733pgJVUctZcAY1RHvpmaaZUdnhhfcRXELSv5vYgWsDD7ICHWi1-R56f74M2YsguqQ0Irn2SpmPz9kxscSBlNQAuLB2fbiwc4cT48YVODLtTsZ21uHy59C9mbhpLW3usnyl5AVtChBFoETgNYMdY2vrBEREpddUeSGBG_0eP9VSj_xXgWzE_1TbXPZdN_Wq1t9z1MXs4jXeBGT2iW3VZzzAIi-u0g0QbJgADX-9zE-nOg2pH-J453bIHSlcuq9FmoR7aHsbNs7zp1MciGLjsaiTJ6t5q5UstWycV3gGs8TsQiREWmKPsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دزدی خونوادگی یه خونواده از فروشگاه؛ از دختربچه تا مادربزرگ، همه توی دزدی نقش دارن!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70193" target="_blank">📅 16:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70192">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy_nDMSCk72-259resnuwInUgbLH5TDSNBsTcPFtFGnWTrToGTMfrb19jPzDL4sUygbB6ghgC1dWjrUXXNXqEMlCkvfR-EOLONmXxfzUcpzWXyu9DSEaHRXgNNQcHm4e1P7a9sZyLlPzNcsR8H5ZLZtvTKOQxNX8T_Hy10fzcI3T-dfwKbE8a7MZ5LwcJa5R2T36M1MRGt2wUDI29lMfF7y9V8DAEw5L_OP24uwTYas5aY56q7PoBxBIbiRJwDwicQI8vyM3edyDCuCvorHxqIPnM1YR75PgIsaDQwTwvonVg0SexE2epSiE1o7D_zHm7Evj5UaU7frdPYo-OLR5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس‌نیوز به نقل از ترامپ:«اگر عمان سد راه شود، آن‌ها را به‌شدت بمباران خواهیم کرد.»
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه گفت که اگر عمان در جریان تنش‌ها با ایران در تنگه هرمز سد راه شود، آمریکا آن کشور را «به‌شدت بمباران خواهد کرد».
ترامپ این اظهارات را روز دوشنبه در مصاحبه با «تری یینگست» از شبکه فاکس‌نیوز بیان کرد؛ آن هم در شرایطی که مهلت آتش‌بس میان آمریکا و ایران رو به پایان است.
ترامپ گفت: «اگر عمان سد راه شود، آن‌ها را به‌شدت بمباران خواهیم کرد.»
ایران هفته گذشته اعلام کرد که در حال مذاکره با عمان درباره چگونگی بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70192" target="_blank">📅 16:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70191">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4155a42fb1.mp4?token=OZmkk1NNp3h906Gb6cs9f49pJ2ea7tZLyfTcNIyM7TuEf6bVtrg-tLjXfeiQ268qTh4qf1jCawrzGwoj7zbdElL-s1Dn4-r9OXjTu_nJj5yzL_zn8hfUzShT8EgIWcS1AXM7l_Zx4FoOSvm218YpVU2yZUbncxtXFj6RI-yiQxtsUvXBZkgMRGbgau99uRxqnFPO3UeKOfX2-cxtOEPHnIAfQQgRSxOTxeZpw2pfO4pmCQ6GmWD7TBOxYsBNe7xC8xGt9vqVhpCSigbqjOhG4Wdtwnw9W4TQedNIIT6A7hlpCYmGUjXIApd6UuBFmuL9XfNumB0aZQT9vvjwatayxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4155a42fb1.mp4?token=OZmkk1NNp3h906Gb6cs9f49pJ2ea7tZLyfTcNIyM7TuEf6bVtrg-tLjXfeiQ268qTh4qf1jCawrzGwoj7zbdElL-s1Dn4-r9OXjTu_nJj5yzL_zn8hfUzShT8EgIWcS1AXM7l_Zx4FoOSvm218YpVU2yZUbncxtXFj6RI-yiQxtsUvXBZkgMRGbgau99uRxqnFPO3UeKOfX2-cxtOEPHnIAfQQgRSxOTxeZpw2pfO4pmCQ6GmWD7TBOxYsBNe7xC8xGt9vqVhpCSigbqjOhG4Wdtwnw9W4TQedNIIT6A7hlpCYmGUjXIApd6UuBFmuL9XfNumB0aZQT9vvjwatayxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یولکا؛ رهگیر پهپادی روسیه که برای مقابله با پهپادهای اوکراینی به کار گرفته شده است.
این پهپاد با تکیه بر رهگیری خودکار، به سمت هدف حرکت کرده و با برخورد مستقیم آن را منهدم می‌کند.
مزیت اصلی یولکا، هزینه پایین و امکان مقابله با پهپادهای کوچک با یک رهگیر ارزان‌قیمت است.
ویدیو، نمونه‌ای از استفاده این سامانه در جنگ روسیه و اوکراین را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70191" target="_blank">📅 15:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70190">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2a93816b.mp4?token=CNjqPxD1-RwB0SWOry07ZSdsWB5AjYnpKQBsRPlJiBLVERznho-q-m23cJUcU7tkPhImFTNcbcbwND-1212YE0-Wl8osbkSMTQxmiqRTXBQa2dDfekJRGHmx0i9es1IsdqE1T-yUm7k-hqQSDUJGym1_pdeakq6YLNkgHdXXc0Z2_dsLAtwsVDo5PxG2CiOuVOehbMQW_jQAklODnbuE7LfZXr00AQwYOQByd1xcknJWNbqYqMM9SdsoFFm--0FJQO-5hmHySouBv66yjb8hLhYXzRALxuqAMozVyqndmJQbgMvkdwvg0dcQd5LruNPp0OnI6whDK26-xAh3cSlouw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2a93816b.mp4?token=CNjqPxD1-RwB0SWOry07ZSdsWB5AjYnpKQBsRPlJiBLVERznho-q-m23cJUcU7tkPhImFTNcbcbwND-1212YE0-Wl8osbkSMTQxmiqRTXBQa2dDfekJRGHmx0i9es1IsdqE1T-yUm7k-hqQSDUJGym1_pdeakq6YLNkgHdXXc0Z2_dsLAtwsVDo5PxG2CiOuVOehbMQW_jQAklODnbuE7LfZXr00AQwYOQByd1xcknJWNbqYqMM9SdsoFFm--0FJQO-5hmHySouBv66yjb8hLhYXzRALxuqAMozVyqndmJQbgMvkdwvg0dcQd5LruNPp0OnI6whDK26-xAh3cSlouw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما یک کانال ارتباطی مخفی با سپاه پاسداران انقلاب اسلامی داریم.
ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70190" target="_blank">📅 14:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70189">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5140e7e1a.mp4?token=rYcpmPzBtv6CORoUcU9BYC3lZythqmDkAgn40_68RBK89KGAXZ5ueG7J1QsahMVazO6tkIS74LRyf1WbMKaTH5qryV9XQpDLQms8Tu-jbipEICEkqNCCywvd6-V6s9UO5I6F5ldseQJYziHgB-L4YwpIjKXRKKItdnIZfdfrRpgW9R0bdX1EhsrCigIdQemHZx8ojaUdunFdoPlvOck1nCgMZvwmvJUQtKPboiueO8uC7aCtsAq1xyVLwgNNhUzAO6JST02djeXodEOvXHbHTVLLr_8QURMmiFGdUf_L7OB9SXOL1U6xrVaI7-nNmRz4rH7zG9YKvBiKXuP9W9b_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5140e7e1a.mp4?token=rYcpmPzBtv6CORoUcU9BYC3lZythqmDkAgn40_68RBK89KGAXZ5ueG7J1QsahMVazO6tkIS74LRyf1WbMKaTH5qryV9XQpDLQms8Tu-jbipEICEkqNCCywvd6-V6s9UO5I6F5ldseQJYziHgB-L4YwpIjKXRKKItdnIZfdfrRpgW9R0bdX1EhsrCigIdQemHZx8ojaUdunFdoPlvOck1nCgMZvwmvJUQtKPboiueO8uC7aCtsAq1xyVLwgNNhUzAO6JST02djeXodEOvXHbHTVLLr_8QURMmiFGdUf_L7OB9SXOL1U6xrVaI7-nNmRz4rH7zG9YKvBiKXuP9W9b_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به شبکه فاکس نیوز:
اگر عمان مانع ما شود، ما آن‌ها را به شدت بمباران خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70189" target="_blank">📅 14:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70188">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1480b179a0.mp4?token=CL5AR1JtknoMv87iPkgm_PpUpmZQtvGFL7SVfs03Ocy1GcPR4dA-mV_6-OzBlElFbh_ZUwGuEJnnnHl3qne0GXMhgiI_FfqFqrSjk7cnXMNu3DgH2hxnCPF9QBTwcz0xIKQeVL-sljK6ub-dSfknRmxcht2rVpljCZBNd8IUXCiG1EElhokTv0mVBIb5gKI6YdnwXsioIaycI5XRy-fWr5OfciWzWaAo1LX2isTyzRG0a9cPA8gjRLv4EzJ-dxIxcVT4HbVRowX3MqFnFsHMkqIDFJHBqDhgtQfvFXEVZfvjycJ2ZsVbRx2bQ5DGUCoN4hrOZ0h7NxCnl0N6zFoDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1480b179a0.mp4?token=CL5AR1JtknoMv87iPkgm_PpUpmZQtvGFL7SVfs03Ocy1GcPR4dA-mV_6-OzBlElFbh_ZUwGuEJnnnHl3qne0GXMhgiI_FfqFqrSjk7cnXMNu3DgH2hxnCPF9QBTwcz0xIKQeVL-sljK6ub-dSfknRmxcht2rVpljCZBNd8IUXCiG1EElhokTv0mVBIb5gKI6YdnwXsioIaycI5XRy-fWr5OfciWzWaAo1LX2isTyzRG0a9cPA8gjRLv4EzJ-dxIxcVT4HbVRowX3MqFnFsHMkqIDFJHBqDhgtQfvFXEVZfvjycJ2ZsVbRx2bQ5DGUCoN4hrOZ0h7NxCnl0N6zFoDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به شبکه فاکس نیوز:
ایران باید پرچم سفید تسلیم را بالا ببرد.
آنها در بازی پوکر خوب هستند، اما در حال نابودی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70188" target="_blank">📅 14:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70187">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmhEi4ISno7nELNrDqlQ34lHO1CEjixqTzy4Bc2CQTktI4KXq3S3d6ROnidayIB-RtxrPh1U6rMfkg4psxHK3tR3zLKGhzS9fC23bEMHBSCPyexUMaJ38F9K3QTKj4c2kOTGVTavZTeYsKRj6hCn8j9X4s5MXAhlw5KbczWnZjdlWsGZ5QAwl-V6pmP4t7-Eije2MdpwWl_UD2oEm8PHd9dYVTCwXFZ-OHr0RS9Fp6SL-BlDuwqSqTyWxd8Rm58T7x1w2QuVTkwB_ZPdHRUiAmf6BfNaRZFS1yKHSwVGZ0FMdf-GfhUt6oblPNaN1PeDJVNnuj18KCIesNS08qwxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ترامپ در گفتگو با شبکه فاکس نیوز:اگر عمان بخواهد مانع‌تراشی کند آنها را به شدت بمباران و نابود خواهیم کرد.
ترامپ همچنین وجود یک کانال مخفی غیررسمی با سپاه پاسداران را تایید کرد و در ادامه گفت «هیچ عجله ای ندارد»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70187" target="_blank">📅 14:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70186">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnaCOeujyMJrihK4l-Oc4lLng9aWdOHQLQWyDNZMP8fV3C7ZLeY7r9YYO5gkexo56iNnmN9kJQWslhXdmkNqFFbB4gGLjdL4ZSEHUoXoeQz-5_m9Q2sSlWNJaCOvRFdOLRTVsi0KQgOOOpxACLs-GZd_cUypeh6kFOgS0Jgu_nqN3YljwU0_xUdAZzmqMMhegYSXAMl9wfLrv5ixirvkdPLkvBDMjsgSB_-u0zIkvgGAPrCxZYTr8u-R9ZjjW6n6ylAOZaxZgW4ZEmYJd8M9NMCr22xhNlNcHww2NGJsnfSGPJ5ou-Hl9WMfg1BVQA1D5hkNb9pDEOdahb7q6zfc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
📰
وال استریت ژورنال:رهبری ایران ظاهراً جنگ و درگیری فعلی را پایان ماجرا نمی‌داند و خود را برای احتمال یک رویارویی گسترده‌تر و طولانی‌تر آماده می‌کند؛ هرچند ایران همچنان از نظر اقتصادی و نظامی با محدودیت‌هایی روبه‌روست.
🔴
آماده‌سازی ایران برای رویارویی احتمالی گسترده‌تر؛
بر اساس گزارش وال‌استریت ژورنال، ایران پس از آرامش ایجادشده در پی توافق ژوئن، به‌جای تکیه صرف بر دیپلماسی، روند بازسازی توان موشکی و پهپادی و تقویت ساختارهای نظامی و امنیتی خود را دنبال کرده است.
این گزارش همچنین از افزایش هماهنگی با نیروهای منطقه‌ای، تشدید فشار بر کشتیرانی در تنگه هرمز و دریای سرخ و افزایش تهدید علیه زیرساخت‌های انرژی منطقه خبر می‌دهد.
به نوشته این گزارش، جریان‌های تندرو نیز نفوذ بیشتری در ساختار نظامی و امنیتی ایران پیدا کرده‌اند. هدف این راهبرد، ظاهراً افزایش هزینه هرگونه حمله احتمالی به ایران و تقویت بازدارندگی در برابر آمریکا، اسرائیل و کشورهای خلیج فارس است.
در مجموع، ارزیابی مطرح‌شده این است که تهران درگیری کنونی را پایان ماجرا نمی‌داند و خود را برای احتمال یک رویارویی بزرگ‌تر و طولانی‌تر آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70186" target="_blank">📅 14:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70185">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ygb4laiRUG0Pu4onXoUeXa5NIWzWXOUnFav9alpFFzW3W5RjtXaR0j3-hkuZFQ1e4YQsUnT_PI3YmzcSjtfgR_TK1lD3sUo9uJ6OEiF2Wbc_IPgUHPTmGeFFhkbg-i07K8aCkBq6aF1ldGBNIN4cef460a2IAD5nca6rGSZELVtbj9wJGUIOCzZsxBx1SKXyYRdEuQT5F_o8tn9MjI4GqBis5pI334T7KeNl4quXt4bdOutVsGfepOvi8O6rGeRJk_6SFhXOZGT5AutXuP471chLre3PtcFPOysQ8UPMIBJG53D1gGGezWTj41txePrkt13KoAsXqCI8pKuoVxqOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
هدف اصلی این است — و همواره چنین خواهد بود — که ایران به هیچ‌وجه و تحت هیچ شرایطی نباید به سلاح هسته‌ای دست یابد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70185" target="_blank">📅 13:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70184">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎤
خبرنگار
:
آیا جلسه‌ای داشتید؟
🇺🇸
ترامپ:
جلسات زیادی.
🎤
خبرنگار:
جلسه‌ای درباره ایران؟ پیشرفتی؟
🇺🇸
ترامپ:
🚶‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70184" target="_blank">📅 13:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70183">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4BnMB25mDWXE_PrOTz9k6kXp_pBAqJchO-jazDtRu4-doSsLacln_akZ8EW8kLtjfCXI9_PMP6ApYnnpIrMcxb81-qiALQidlPaO4Omt24NTSkqm2Ml7CDO92J1hotlwuuCXmWxbvS8gJo4yj37YYX6eo57aRY0ZCB8m-J2qoTFmA7K91dYW_dLTEZjaF5-9z-0I9wiM3N3qLif5ZhxMqUPrm7gCyPdNoRQD-2e35uOwsufMQa013kM893u8FJdgVzxVMnHa5-zcqF7B-8jdD65ap52P82GeVrpOPE9xZXqdU4b7Vlv1A2jPwPcrqdT-OwBAW79DfG-0uWWInlutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی: آتش‌بسی وجود ندارد که بخواهیم آن را تمدید کنیم؛
آنچه در پایان جنگ و در یادداشت تفاهم اسلام‌آباد اعلام شد «پایان جنگ» بود. آمریکا تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شده.
ما چیزی به‌عنوان آتش‌بس نداشتیم که حالا بخواهد تمدید شود؛ ما «پایان جنگ» را داشتیم که حالا وضعیت جدیدی پیدا کرده است.
مهلت ۶۰ روزه در واقع ۶۰ روز فرصت برای مذاکره به‌منظور دستیابی به توافق نهایی بود و اساساً چیزی به‌نام «تمدید آتش‌بس» وجود ندارد.
قطر و پاکستان به‌عنوان واسطه پیام‌هایی را ردوبدل می‌کنند و با ما در تماس هستند، ولی این به‌معنای مذاکره نیست و تصمیمی برای شروع مجدد مذاکرات با آمریکا نگرفته‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70183" target="_blank">📅 12:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70182">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3274b73d22.mp4?token=XdXl9GOIrP0bguhOIV5pkKSwgQot6RmEZGN_uFDkFdK3fgTwjMb2J095Vants3pIEk8GBtHwfxxcEtSQ1QM2VqlG4foF_GRpcoZqTbtYY7pJfqJPDtWOLITAni2a2DsOqtBRgNUNuQOUg9yuJcgsy1mATJqIXoLUtgocOFHw4ZlxQoVF-TPKyZrpbW4O5HgpjE4e1YogpVan4obcygqF2BhzaX9lbUL6OQ1ondX6unPF2m4x1D3jCP44SwFJ3OzxxBBkJtJ8Vqq7jVQCH9Nk_NM59CaiTdY3lNZ-x3MshjoYCishxOA0LvDvmuMUrGdMSOZWyF6Iq8JYyFePN2BqXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3274b73d22.mp4?token=XdXl9GOIrP0bguhOIV5pkKSwgQot6RmEZGN_uFDkFdK3fgTwjMb2J095Vants3pIEk8GBtHwfxxcEtSQ1QM2VqlG4foF_GRpcoZqTbtYY7pJfqJPDtWOLITAni2a2DsOqtBRgNUNuQOUg9yuJcgsy1mATJqIXoLUtgocOFHw4ZlxQoVF-TPKyZrpbW4O5HgpjE4e1YogpVan4obcygqF2BhzaX9lbUL6OQ1ondX6unPF2m4x1D3jCP44SwFJ3OzxxBBkJtJ8Vqq7jVQCH9Nk_NM59CaiTdY3lNZ-x3MshjoYCishxOA0LvDvmuMUrGdMSOZWyF6Iq8JYyFePN2BqXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی که دانش آموز ایرانی استرس کنکور و بمب و موشک رو داره همون لحظه وزیر آموزش پرورش و هیئتش
😵
😵
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70182" target="_blank">📅 12:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70181">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70181" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70181" target="_blank">📅 12:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70180">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V88nIbZVqU-Y4fNWZ-PSmfEqLcMAKBr2rw9wQT8XM3SO8BtK-fjyrbG_hxbJ-PobBJzSv1rH761UD8Ubbm6wC1Ru_06IeD7t-EGnd_i3GcGDiaWe-l8JNd7i4llGCmqfOi2D8-lDDw9W7nRzmr4SbHkiRUA7rFdSQ_CPaWDdbvhgywl_tyLCt-Byq3qfH9H3krqfgQg65DuDRa-uCr5_KNuzwXt5NLHThElnBneI7_a9kta_X-U57kpdwUoX1BagUopTWiR_UFMwoNc8dTIwmItki_4fYrYULbLJ4U2X0G2ncW1KgS4dY91eDliA-seTPirriwNKv1q02Yv0Go2lIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r26
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70180" target="_blank">📅 12:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70179">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cd85b555.mp4?token=uuyGfrvKYGZUsEPJ_W2NEI-UHE2mDtOv37ObufFp2pwV8RxsE4esi7uGbwwKYKHil9yK65yadPlldyr24YAePJZGQfOqp_s7MsbhozlP0UUzB3I2CW5xb0uCFQTCi3lPeFrlbr04PlooOTefeffLPMmgkr1EO4tISQytSO4lZUGf0rhVhRsGUUd-GOdzG5AUg4vkqRh0r7fkURb6CNQEWUN14W75k9pDgH5vaC9sl0RzlSaQhDhBnxvq7Fr2UlyGZSWw07g2b-B6vz9G8AIMKzcTi8cpwIYbD8DY6rEHitoZUEjqZBcPrlzic4R6CqVlns9KIO75OMpNw3Ej7J360w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cd85b555.mp4?token=uuyGfrvKYGZUsEPJ_W2NEI-UHE2mDtOv37ObufFp2pwV8RxsE4esi7uGbwwKYKHil9yK65yadPlldyr24YAePJZGQfOqp_s7MsbhozlP0UUzB3I2CW5xb0uCFQTCi3lPeFrlbr04PlooOTefeffLPMmgkr1EO4tISQytSO4lZUGf0rhVhRsGUUd-GOdzG5AUg4vkqRh0r7fkURb6CNQEWUN14W75k9pDgH5vaC9sl0RzlSaQhDhBnxvq7Fr2UlyGZSWw07g2b-B6vz9G8AIMKzcTi8cpwIYbD8DY6rEHitoZUEjqZBcPrlzic4R6CqVlns9KIO75OMpNw3Ej7J360w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
کارشناس پدافند هوایی سپاه پاسداران:
«در روزهای نخست جنگ، ۶ تا ۷ فروند پهپاد «هرمس» و «هرون» متعلق به رژیم صهیونیستی به‌طور همزمان بر فراز جنوب لبنان در حال گشت‌زنی بودند.
با هدف قرار گرفتن این پهپادها [توسط ایران]، شمار آن‌ها در جنوب لبنان به تنها یک فروند کاهش یافت و بدین ترتیب، آزادی عمل بیشتری برای انجام عملیات در اختیار حزب‌الله قرار گرفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70179" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70178">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe1c04e38.mp4?token=MCoqv7SWNZNwWp0w1igDGXD7yHzDk02p9BAkCjPLtdPJEtsbU4M5iNcmvnVf4P7T3hIu2_2BD-8Y7baa9O2nswO2kez1I-8nC2zhSBnceb3FHIKtXficlPrnsGy2eQY7do3LVQ2_JQ2PDlIdtft6zA0npDBuJ2ZZhBxMrQUU71Z8u9BultZ23YLeX_YdRxsJRBX_VIZoB7FhF0nB1qiKsSkWCUX8ch9YKhJ4jQnosVWLti6KOYtVLa7M1BCo1Hzm_v7Sfo2QljcbHaEg2c9R4itxQGPjRS4EGMxr7sujcYTnT9tdcYwT1t7Z2WSoFJ8nd-gQIDb-YOdZ6DZRcGZPKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe1c04e38.mp4?token=MCoqv7SWNZNwWp0w1igDGXD7yHzDk02p9BAkCjPLtdPJEtsbU4M5iNcmvnVf4P7T3hIu2_2BD-8Y7baa9O2nswO2kez1I-8nC2zhSBnceb3FHIKtXficlPrnsGy2eQY7do3LVQ2_JQ2PDlIdtft6zA0npDBuJ2ZZhBxMrQUU71Z8u9BultZ23YLeX_YdRxsJRBX_VIZoB7FhF0nB1qiKsSkWCUX8ch9YKhJ4jQnosVWLti6KOYtVLa7M1BCo1Hzm_v7Sfo2QljcbHaEg2c9R4itxQGPjRS4EGMxr7sujcYTnT9tdcYwT1t7Z2WSoFJ8nd-gQIDb-YOdZ6DZRcGZPKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ممدانی اومده یه ویدیو از خودش منتشر کرده و برای شهروندان چینی نیویورک، با زبان چینی صحبت کرده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70178" target="_blank">📅 11:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70177">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b0e3619.mp4?token=OxUorjIl0B9C1do_8GF-o3t3VNCSNiCu8EaRa1KDIQRdtybHN61lBI8UULaUv0TrsGiEdpw5ah2dsOEywJ9UWTvyhG7MSF_i_8QATTtMxX4Tzp2WXHWYBIDgti_Wye3b3CEMg46slKziYGiQ26HQWVnLl7b3fMZr9nH-EnPuhTiybUWmS5-n5FM0uObM4Erevze-1DRqrsKuDVrZNwlUF00J0zBj6zjZBZ7wf59NNPyL5DeEyoeCwTf6y_KT6hO6rWjhOkSM1BfUATz9r9M5FjfZTjNSy3oba6gPyboyqURTjKUgrUIf48V5Ey_U2dvUZcIcMiMY7fK9RGKGvxHukCK2BVlXGc2r7iq1Gs42Uu0SMRU-vxFvjkrERTVkjfufR2S0FI2PXOtSv_UxYkydcZuR0HbeX5fWcQtP1uZcZDAyxOD_qne0Hi_TFarhsuQlmu_9h7LNBC_wmw5efmWhuoF3zmUw-0BdAAgH3HNNujJB5fDZTfjrKLfdKyFYlM6Wqwk5cmhSzYojr-BD_ySalydB10FaOKyJyle5BnfyIRJTg2yB2IMFASTOf2APKOGL5Tt9DdYK0nAOPOyrETA-b-Y7HeZlszVSzKVepQw7Ejar8IrbZAeAJrelMT6BhWYN7-TNdIzNuxHnSdt_q4L-Fu3ag1JP375j37nPYnRP_W4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b0e3619.mp4?token=OxUorjIl0B9C1do_8GF-o3t3VNCSNiCu8EaRa1KDIQRdtybHN61lBI8UULaUv0TrsGiEdpw5ah2dsOEywJ9UWTvyhG7MSF_i_8QATTtMxX4Tzp2WXHWYBIDgti_Wye3b3CEMg46slKziYGiQ26HQWVnLl7b3fMZr9nH-EnPuhTiybUWmS5-n5FM0uObM4Erevze-1DRqrsKuDVrZNwlUF00J0zBj6zjZBZ7wf59NNPyL5DeEyoeCwTf6y_KT6hO6rWjhOkSM1BfUATz9r9M5FjfZTjNSy3oba6gPyboyqURTjKUgrUIf48V5Ey_U2dvUZcIcMiMY7fK9RGKGvxHukCK2BVlXGc2r7iq1Gs42Uu0SMRU-vxFvjkrERTVkjfufR2S0FI2PXOtSv_UxYkydcZuR0HbeX5fWcQtP1uZcZDAyxOD_qne0Hi_TFarhsuQlmu_9h7LNBC_wmw5efmWhuoF3zmUw-0BdAAgH3HNNujJB5fDZTfjrKLfdKyFYlM6Wqwk5cmhSzYojr-BD_ySalydB10FaOKyJyle5BnfyIRJTg2yB2IMFASTOf2APKOGL5Tt9DdYK0nAOPOyrETA-b-Y7HeZlszVSzKVepQw7Ejar8IrbZAeAJrelMT6BhWYN7-TNdIzNuxHnSdt_q4L-Fu3ag1JP375j37nPYnRP_W4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک شهروند اهل فلسطین:
لعنت بر ایران که ما رو به این روز انداخته
عامل تمامی بدبختی های خاورمیانه و کشور های عربی ایرانه
اونا ما رو تحریک کردن گفتن حمله بکنید
اونا باعث شدن نزدیک دو میلیون نفر اینجا آواره و کشته بشه
کاری با مردم ایران نداریم اونا هم مسلمون هستن ولی حکومتشون خدا لعنت کنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70177" target="_blank">📅 11:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70173">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4epd75gUEVoh_WmbhC9hy8cfKGZ1rXwDhQs03sGN8RPAXxfSHszxOMTWYdawmfQ0uVpn08MGhW41SVrtMjLsWS9Ibb4U7pvS3yrv05FVsB0Hi3rPJfewQo6Yvp3sMEHd1859U6JtpI-50Tk0WTiag19Ijqvcv9TkTOEyqF8jZ69O5kU35KXs2Z6k60uoP5GZXkKrf_PgW_MCBG8AhWF_FPhQDqqP3QsinFl2MlbI7_wkZPZ9iznTuQeKkG5oTUWI7avM8LQVJWAJ0TSP3oA1ko4CMhS188utc4pKcDPc53ejxUcauF6SeVR0jv7HAZaiOgFVpdVIpLNBNDYKHQZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168e601701.mp4?token=vtcnc7KDE6Bjtx6d20p2pUnEiMMFfLw5261p-8C0tKcurGlcyOoMAAvd9ntOXbPL9Yw05cv80cbrVASmxqLNzB2hm1ChYzQTdlHd6Qv6mskPgsAsKHYWgrJktod90aUBQx98SygX-nyMUp9b2Foq8QwZmdS68KEVVvlSAjQUwu3cTSZpDkhp4_RlQkFZCPrIugQqumsuNbey3qQ2fwbq3WsOe6R2kj1zT5rf1XeqdDcy2coB0a3lKZ0l-MqzntYgv8lZr9B8-A70PnqWm5cFVDTPHhSZgkSgfQxqpuFjZm4CDPXLaqNSf4Dd1nH10qivhWNguudTYSw_g_Cg_HuPqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168e601701.mp4?token=vtcnc7KDE6Bjtx6d20p2pUnEiMMFfLw5261p-8C0tKcurGlcyOoMAAvd9ntOXbPL9Yw05cv80cbrVASmxqLNzB2hm1ChYzQTdlHd6Qv6mskPgsAsKHYWgrJktod90aUBQx98SygX-nyMUp9b2Foq8QwZmdS68KEVVvlSAjQUwu3cTSZpDkhp4_RlQkFZCPrIugQqumsuNbey3qQ2fwbq3WsOe6R2kj1zT5rf1XeqdDcy2coB0a3lKZ0l-MqzntYgv8lZr9B8-A70PnqWm5cFVDTPHhSZgkSgfQxqpuFjZm4CDPXLaqNSf4Dd1nH10qivhWNguudTYSw_g_Cg_HuPqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بالاخره عکس‌های عروسی رونالدو هم اومد؛ این دو زوج خوشبخت تو همون اتاق نشیمن خونه‌شون تو پرتغال ازدواج کردن.
⏺
جورجینا میگه اونا عمداً اتاق نشیمن خونه‌ رو انتخاب کردن؛ همون جایی که:
صبحونه، ناهار و شام میخورن و زندگی روزمره‌شون رو میگذرونن...
اونا میخوان 30 سال بعد، وقتی بچه‌هاشون به اون میز نگاه میکنن، بگن: "اینجا یه اتفاق فوق‌العاده افتاد؛ مراسم عقدِ پدر و مادرمون."
+اونا تو خونه‌ای ازدواج کردن که تو ماهِ 7اُم سال تحویلش گرفتن و ساختنش هم 7 سال طول کشید.
+تاریخ عروسی هم 11 آگوست، دقیقاً دهمین سالگرد روزی بود که واسه اولین بار همدیگرو توفروشگاه Gucci تو مادرید دیدن، اصلا به همین دلیل هم کل لباس‌هاشون از برند گوچی بود...
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70173" target="_blank">📅 10:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70172">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
📚
كارت ورود به جلسه آزمون سراسری کنکور ۱۴۰۵-۱۴۰۶ منتشر شد
؛
داوطلبان کنکور تا چهارشنبه ۲۸ مرداد فرصت دارند کارت آزمون خود را از سایت سازمان سنجش دریافت و چاپ کنند
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70172" target="_blank">📅 10:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70171">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b010614a.mp4?token=UcUbWpBfv5f9oVUDaHIkomaDm5v3owgaIGJzalmnaRn6ol04kUwh7WJWwfXWV_26CCVi3_wZqnNG7qM3jOmMjDvMSmXXB4CoDOACX8_7vnlDy4DFK2hfn7LgnKVWR-9ohdYjfAhAj2_ncvT_fnkAgxaIMbznupsuGvNXLy0u-qbiCCd5Ls-b2DCl-V67gpsJsqCvWcMEM8yL98RWywdcxz_PswfOfsknhuNAGbss2sdrOOShFE7JA5i8njVpBWqalq0zYnk5VI7fu8UsM3pO7_eA406bg8ByzwC1TKpkzqw7iulVX8gWAssu8RlAmD3VcpKaicrq-ejr4zNBJN2LeZM4ruvRLSowdf9k761wBKEOwjImO5m_DGJEa8771XR3RF75bOg9OxHsqUm--pBPypgPnYdFqMX2Kom7yEoR6DB1EJDuGCayVK2cwyv9X52iC1hs8MEf0UnIr4IjRcDH42e3j_CuUPgpb8hgrnlm1VL3FsFVBzdFdqDiH4Fjewn_3Y1E4b0b-fMbzfZoS6HvRYZMSXcPePBAf0c8lZbxbWtT5qEYzHXyEz45r9vNtSIf9I7PUv9hjorDrl0zEUSM4GCx1uG-yPeDvcgbuqsbm9eVG4bNBxuvz38dRVgqa84d7-d1vRDuPHXdJzJmU3hHi7wKPNsm_a2U3bqYWFMC5K4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b010614a.mp4?token=UcUbWpBfv5f9oVUDaHIkomaDm5v3owgaIGJzalmnaRn6ol04kUwh7WJWwfXWV_26CCVi3_wZqnNG7qM3jOmMjDvMSmXXB4CoDOACX8_7vnlDy4DFK2hfn7LgnKVWR-9ohdYjfAhAj2_ncvT_fnkAgxaIMbznupsuGvNXLy0u-qbiCCd5Ls-b2DCl-V67gpsJsqCvWcMEM8yL98RWywdcxz_PswfOfsknhuNAGbss2sdrOOShFE7JA5i8njVpBWqalq0zYnk5VI7fu8UsM3pO7_eA406bg8ByzwC1TKpkzqw7iulVX8gWAssu8RlAmD3VcpKaicrq-ejr4zNBJN2LeZM4ruvRLSowdf9k761wBKEOwjImO5m_DGJEa8771XR3RF75bOg9OxHsqUm--pBPypgPnYdFqMX2Kom7yEoR6DB1EJDuGCayVK2cwyv9X52iC1hs8MEf0UnIr4IjRcDH42e3j_CuUPgpb8hgrnlm1VL3FsFVBzdFdqDiH4Fjewn_3Y1E4b0b-fMbzfZoS6HvRYZMSXcPePBAf0c8lZbxbWtT5qEYzHXyEz45r9vNtSIf9I7PUv9hjorDrl0zEUSM4GCx1uG-yPeDvcgbuqsbm9eVG4bNBxuvz38dRVgqa84d7-d1vRDuPHXdJzJmU3hHi7wKPNsm_a2U3bqYWFMC5K4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثبت تصویر یکی از مرموزترین و کمیاب‌ترین گربه سانان جهان تو ایران
:
ویدیویی جدید از گربه پالاس تو ایران منتشر شده؛ گربه‌ای فوق‌العاده مخفی‌کار و گوشه‌گیر که دیدنش حتی برای محیط‌بان‌ها هم بشدت نادره.
واقعی بودن ویدیو توسط منابع معتبر تایید شده
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70171" target="_blank">📅 10:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70170">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e92b4117c.mp4?token=hLLNEAYxlawnFFTaZmG6Vu_NR4o_suD-qSc2-bd1dwz_midUpzb4odZGB709Vs_WWNYv_A_hrRFQhj0oKZANetD7Dr46_qn9CCQZYY3VyRAiI0M7j8Rk8O3M0rhLWZsV7W994A4ls-yLpJ_F9jTpsYlxJHhyqT2PeHcPL7fW8c4OQnaYGyMOhqlT6tcA44R-9zrF82samlH7jT4wMSzusE6RJk-yPTurTZE9ulNorp2I6eKgFArqTHA_JtR3pVLTFc7izsm0u_akmWJ5oag5Cu9EcJuObsonPxx4USdZZt-r_SnU15jH3s3V6rmTTwLBfKv3I-kPogE41tb5zpzvfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e92b4117c.mp4?token=hLLNEAYxlawnFFTaZmG6Vu_NR4o_suD-qSc2-bd1dwz_midUpzb4odZGB709Vs_WWNYv_A_hrRFQhj0oKZANetD7Dr46_qn9CCQZYY3VyRAiI0M7j8Rk8O3M0rhLWZsV7W994A4ls-yLpJ_F9jTpsYlxJHhyqT2PeHcPL7fW8c4OQnaYGyMOhqlT6tcA44R-9zrF82samlH7jT4wMSzusE6RJk-yPTurTZE9ulNorp2I6eKgFArqTHA_JtR3pVLTFc7izsm0u_akmWJ5oag5Cu9EcJuObsonPxx4USdZZt-r_SnU15jH3s3V6rmTTwLBfKv3I-kPogE41tb5zpzvfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
آریایی‌نژاد نماینده مجلس:
من تو مناظره ای که داشتم در وصف مرحومه مهسا امینی لفظ نامناسبی بکار بردم از خانواده ایشون و همه منتقدین عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70170" target="_blank">📅 09:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70169">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
نوید محمدزاده که پست حمایتی از فلسطین گذاشت مردم گرفتن روش حالا حمله کرده به مردمی که بهش انتقاد کرده:
قبلا از فلسطین حمایت کردم و الانم کردم و درادامه هم میکنم.
چون اصلا با اسرائیل حال نمیکنم و تا همیشه فن فلسطینم.
ما حکومتی کثیفیم اونوری ها میگن اینوری هام هم میگن وطن فروش
کله ببرید تو زندگیتون.
به بشر یکبار فرصت زندگی دادن چیشد که همه تیم کشی کردن و چرا انقدر باید راحت تهدید کنید ؟
من نه طرف اونوریام نه اینوریام من طرفدار زندگی ام.
میتونستم هرجا که میخواستیم در تاپ‌ترین جا زندگی کنم ولی اینجا موندم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70169" target="_blank">📅 08:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70168">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70168" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70167">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Yp58K6R9QH5hhXZX0UOUhmfmVgwrSinTdstvwyU_fWJ--TuOiAyXWZhq8Wc01Enh4lUt0-dcSDJX1VM7tVd6SoFE7J4_p07jm8vXLEZBObC0Q5UzhgLuNXDHLdc-F57MNI0L-25PBwUAbiPtSpV4ijyL3RTn7KeUmuIOMshEWFmyB7nep5uOIbwaUJtB8Gg31VfrDgbrT6sKpD91JSosexZ4vjclDpcUixXpkejqbE6ymbxTXKoCUzKfoI5dPvYJgw9tSZXeCULK0zKnQmHU2ced_e4KymtMehAvuck2DPsBKWHD86RtoXXPow4_y6aStxMHlb4kz9gdBqrfPKQOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Yp58K6R9QH5hhXZX0UOUhmfmVgwrSinTdstvwyU_fWJ--TuOiAyXWZhq8Wc01Enh4lUt0-dcSDJX1VM7tVd6SoFE7J4_p07jm8vXLEZBObC0Q5UzhgLuNXDHLdc-F57MNI0L-25PBwUAbiPtSpV4ijyL3RTn7KeUmuIOMshEWFmyB7nep5uOIbwaUJtB8Gg31VfrDgbrT6sKpD91JSosexZ4vjclDpcUixXpkejqbE6ymbxTXKoCUzKfoI5dPvYJgw9tSZXeCULK0zKnQmHU2ced_e4KymtMehAvuck2DPsBKWHD86RtoXXPow4_y6aStxMHlb4kz9gdBqrfPKQOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a25
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70167" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70166">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ulu2uJiAqTzMcLdXW8h32JJ11cin-3-afuTczgC9MvCvqrtvVB5QaL3bzncZULna1esNjLHv03a16Pzpqfkl4pT3dZNhHlOuzJn3MNKpfpwCxDNDaalrK690bGXr6eplVCX2wt3ePcz7NOjgeUVKGzKHHAwpD3poB0yJ__YeWz0QssthNJnZkEPmmObWlvY3_CNlaXg0Uz_jMsb5JSMLmd9LTIuFAN1hdQOHU9barJhenXAZ601vl0BgSvJlOZvrvKNsWnlLg87oBodx9MTCRheV8FOjbkLAsNm_8AORRbHnBBmPzILBYVIwYjiXXFG2siqc_dzckYcQInvGCveu4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
❌
مارجوری تیلور گرین، نماینده پیشین مجلس آمریکا:
در جلسات راهبردی درباره استفاده از سلاح‌های هسته‌ای علیه ایران بحث می‌شود:
بله، درست خواندید.
این واقعیت دارد. من حدس و گمان نمی‌زنم؛ من از این موضوع خبر دارم. و این شرّی مطلق است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70166" target="_blank">📅 01:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70165">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKtfteYqP4RRh-miu7Ex4K_9d6FJWxBtRDl1bsCIrW-S4KCii8dt5vo3JXMsyMTmN_vF0DfdnlbMFNm3UoPg-Ff9iNAhwZ27pX8A5Xd5q6corgRJUH9vuwCrL9ZbBShxv-RjjhlmE9AKGXMua0qUAwQ-pJrXKN3qatXO5-JbC2dTjO7UA9ZaWRw0WmudG2Nu7aoTjnqqYOUd7Vp_PKp66V-0CLOJWqeVkG8gIp-fplvvSsberh0aQZbdfIgvsRJEb0gyIVFrhAjHxBYMsTy2_VxDeiG_SdVFHAH_nHAoHYqMs78Qcm0KIQgzUSJEqVGQR2OIS5PCYNojTNe0Vqk71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
ستاد تبلیغات انتخاباتی جدید نتانیاهو:
🔴
مجتبی خامنه‌ای، زهران ممدانی، رجب طیب اردوغان و نعیم قاسم را کنار هم قرار می‌دهد:
«آن‌ها می‌خواهند نتانیاهو شکست بخورد. نگذارید آن‌ها پیروز شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70165" target="_blank">📅 01:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70164">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uk2G_mk98SNc4TosBfzX0XJnBcvbPgr5EunbpmQ4w13fhlpMLLJuc7-rMinwEhT-xLetgMxW0IaY9ZkHX7Gqa2yZVei4EV4jm6hHvCedhbbfrKKjZsEfz6OPWZ0cpgqSWLqY2_M9kQj1Eg5DuPFiK3Y9Vfr-8BRXapERwIga7NRu_SSWsh2pNdLPnMuLbI_4Gllu0-MNYPczNlaQLTSpNWFJedkm9kZlHx3svf1NnxeSFt4dj_KPpVMk-aulpDojk0ty2CMt9h0nagd7BFkrktp9i10lK5R5MMs-BoVhqm5j92d-azUsOfG9MQeEWOuq0PZb0MkTKsF4vE3HYC0q7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
🇮🇷
#فوری
؛مهلت ۶۰ روزه مذاکرات در چارچوب توافق صلح ایران و آمریکا در اسلام‌آباد به پایان رسید، بدون آنکه توافق نهایی حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70164" target="_blank">📅 01:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70163">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uqy5XI3dSWuwZHhUdhcrcOgld3zbYHT-DvLJLE9lnrfBZxWdI2Bs1nZvS-UNeT5o0GM1kBzU-cXU_-rWc9Eabfxv5hGQDjSsESRLFc4xFJhwfshxL_27HZJyN_jg4FcUKJ4pNCFeiuRc9U2bSVQZy2oXM_rXCJoGv2zv7YAVS0-0JtxWchdreknbqsuqP4-H3valZkccdOYOitLNcEzCZdSfzwJRoBhCv3dMmemyEq1WhRJysjMmVbqcGcGojZZ6gBk8EtEQOK-4pic1VqAheBLEXLQlMvaiHy5uBHT9qCANNlWRs22pM7m_EeLuKehwx4q_nLQ26leJ50K4nRWiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
با توجه به رابطه بسیار خوبم با کیم جونگ‌اون، رهبر کره شمالی، از اینکه ایالات متحده مدت‌ها پیش با مشارکت در رزمایش‌های نظامی مشترک با کره جنوبی موافقت کرده است، خشنود نیستم. این رزمایش‌ها نه تنها پرهزینه هستند — و بخش عمده این هزینه‌ها (طبق معمول!) توسط ایالات متحده آمریکا پرداخت می‌شود — بلکه پیامی کاملاً نامناسب و خصمانه به کشوری مخابره می‌کنند که در تمام دوران ریاست‌جمهوری دونالد جی. ترامپ، رفتاری محترمانه و عاری از تهدید داشته است. از این رو، و با در نظر گرفتن اینکه برای لغو کامل آن‌ها دیگر دیر شده است، به وزیر دفاع، پیت هگسث، دستور داده‌ام که این رزمایش‌های نظامی مشترک را به میزان قابل‌توجهی کاهش دهد!
⏺
اگرچه شاید موضوعی بی‌ربط  باشد، اما اخیراً از رئیس‌جمهور کره جنوبی پرسیدم که آیا مایلند در زمینه خلع سلاح هسته‌ای جمهوری اسلامی ایران با ما همراه شوند یا خیر، که پاسخ دادند: «نه، ممنون!»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70163" target="_blank">📅 01:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70161">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8Ha3tDq_vwlAEsaPRroglyfz8rjlv_SJr_pbUXMa9fM3CgIXYmiT5FQH39vJuELgQW2H4MtgvSbYVfKXlbe9N8WRQ5MmdS7w60ojR6pezqfA5EI1d7FwZKzuf4Xd7xh6Y23dLdZgGEOZPg5pX5EnWu3ze-XwsypY8NE6r0r2YqKx-TEu0x9b5qjkN0j9z-blgis_WasM5UD8_WCwM1G73I7TSUTDNQWWc6-XDSiG47hSDYQ9hrqNeyFQFF97KAuN_3vDaKhvxrounpufcPNyKxgxDHGq-dJ5wax7SNRJmEMt4APvOn3-oORDOUgpu3IBlXUvYlevPooBEE1a1I5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d94596467.mp4?token=eNujtmU_7AgbEG-FsE3UqFmWXtDWa3FIh7rEb9d5hgn_VafQ-_m9F--UavyES5U5QyX0Jc3m51RDZzr416uZpU6dL0CuBFokrj6n2MpqrcrIEB1Nh3cmyJ6flKWL-DxWyEzYkrvics8dzai7lipccQWeuWIABOmEa5RzZ_GXS3hDT-SG-9ezUSwiXecxMiVeS-cBsNM0QwLYW2EFrG5BybPPhwvRnrqaeCgJinwTTfA5NEAAWeGcWswQTjyCi33gmVbKe1TRVAUIDnej3RiXWTNThwTn-rbtcOilt-QHKD2Dx1Fal-XvBEZPwK95uLrTWAUNd2hRBcycnlIcCOLgug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d94596467.mp4?token=eNujtmU_7AgbEG-FsE3UqFmWXtDWa3FIh7rEb9d5hgn_VafQ-_m9F--UavyES5U5QyX0Jc3m51RDZzr416uZpU6dL0CuBFokrj6n2MpqrcrIEB1Nh3cmyJ6flKWL-DxWyEzYkrvics8dzai7lipccQWeuWIABOmEa5RzZ_GXS3hDT-SG-9ezUSwiXecxMiVeS-cBsNM0QwLYW2EFrG5BybPPhwvRnrqaeCgJinwTTfA5NEAAWeGcWswQTjyCi33gmVbKe1TRVAUIDnej3RiXWTNThwTn-rbtcOilt-QHKD2Dx1Fal-XvBEZPwK95uLrTWAUNd2hRBcycnlIcCOLgug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام:
یک جنگنده رادارگریز F-35A نیروی هوایی آمریکا هنگام گشت‌زنی در آب‌های منطقه‌ای خاورمیانه، توسط یک هواپیمای سوخت‌رسان KC-135 Stratotanker در هوا سوخت‌گیری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70161" target="_blank">📅 00:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70160">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fddf8c9b.mp4?token=RejpxnZ_k3EcGJNO6K_2kjK3U8gx9VZR_zjIkGpvmdAoa-QfZyOnL83UEvNf63V-pupCLAfBnkzSI_08ZPmkdTaY5zme23U7RlQMP4pTNmiOpSbFQ3_Iad52xIcU1aPKmCH5niLqWpg_mjTzdN7GvvUQQJd5z3mrSLoimQ0Jarmn6MZ7yCJC5yyTZsvTV0eSl73n1S_phY5O5iWJATBNk7J9QnqkijpIPeVffjku6maUIQ4kn_EatIx8QRLptGZK2JL04G7NCVCcC7WpB3bx-y0PO7h-U-CPDeyxKAxL46cWqgxnsVsfaEua5KdkIoJvDWv94MwgWYO6oozPP6rQMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fddf8c9b.mp4?token=RejpxnZ_k3EcGJNO6K_2kjK3U8gx9VZR_zjIkGpvmdAoa-QfZyOnL83UEvNf63V-pupCLAfBnkzSI_08ZPmkdTaY5zme23U7RlQMP4pTNmiOpSbFQ3_Iad52xIcU1aPKmCH5niLqWpg_mjTzdN7GvvUQQJd5z3mrSLoimQ0Jarmn6MZ7yCJC5yyTZsvTV0eSl73n1S_phY5O5iWJATBNk7J9QnqkijpIPeVffjku6maUIQ4kn_EatIx8QRLptGZK2JL04G7NCVCcC7WpB3bx-y0PO7h-U-CPDeyxKAxL46cWqgxnsVsfaEua5KdkIoJvDWv94MwgWYO6oozPP6rQMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
قالیباف:ما در برابر آمریکا پیروز شدیم
منظور از این پیروزی، این نیست که ما ارتش آمریکا رو منهدم کردیم؛ منظور اینه که آمریکا و اسرائیل با ۹ هدف مشخص و اعلام‌شده به ما حمله کردن، ولی به هیچ‌کدوم از ۹ هدف، در هیچ سطحی دست پیدا نکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70160" target="_blank">📅 23:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70159">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e64058ea.mp4?token=eoohbPS7wTnAzJZ9FB63RoISXuyWAalpwLYSCMTLD0hP3lNCsYv6O9oW23sniSdzzH68P9U3P12rdgn-VbOuXv-6RaZkdcjvB8ybG4zWLQcRncdthCyv93agbWIT1uC777mNBdXh0ffHR_TSl7ZJrMqf2diOEa4I9GUekf_10HZUNOUaNy_cXUfRzJxx6pQOdFC1b3ViJwhotrHFRliE-cMX8ggeV0UpFnQ9-2zyirp0XlKel1sps7XSgr6d_Gih3WjKGrYiPbZtNpaf4UAR8J6c-W0YI8xxzIaoa9JhTzBIKxYyqci3pSCYpYOJrGsK9Y2gvspV1Pz0rTJ8aDvSzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e64058ea.mp4?token=eoohbPS7wTnAzJZ9FB63RoISXuyWAalpwLYSCMTLD0hP3lNCsYv6O9oW23sniSdzzH68P9U3P12rdgn-VbOuXv-6RaZkdcjvB8ybG4zWLQcRncdthCyv93agbWIT1uC777mNBdXh0ffHR_TSl7ZJrMqf2diOEa4I9GUekf_10HZUNOUaNy_cXUfRzJxx6pQOdFC1b3ViJwhotrHFRliE-cMX8ggeV0UpFnQ9-2zyirp0XlKel1sps7XSgr6d_Gih3WjKGrYiPbZtNpaf4UAR8J6c-W0YI8xxzIaoa9JhTzBIKxYyqci3pSCYpYOJrGsK9Y2gvspV1Pz0rTJ8aDvSzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ریحانه قاسمی زاده مجری صداوسیما:
جنوب ایران،فدای جنوب لبنان،اینو یادتون باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70159" target="_blank">📅 23:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70158">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8ucGFpt7ywa-nhHqwBhPxRySBEW36BKgtZLod8LdjmY9RheXOg8WAJiGn6hLebg7ywl2c1u-6PmsiHEJI76tmA9Dgv9AmhNkp7tRa6QYrn-5OOEkt0-tKLuy5aEf0gqHAXn7xg_lhzcKp8aYeI6jWY6KFZOPSUw02lSWD64zTHmkfwjlsUYqg-RbXWD0UtMzSPamTyPu3e94LiLityvECgI1NMYfFSMbO9oWW1cEzMmPHe5dzabQN3jfgnZddubIisGFbE5fy8eVcWz02xMmytW31qHqTKOB1WoEoYRdQrUZ7VfdvuLtCzK3dHziYWtOfd4bDnJKKoEK03foE1x2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
آسوشیتدپرس:
ایالات متحده در حال خارج کردن آخرین ناو هواپیمابر خود از غرب اقیانوس آرام است؛ در همین راستا، ناو «یو‌اس‌اس جورج واشنگتن» که در ژاپن مستقر بود، در بحبوحه جنگ جاری با ایران، برای جایگزینی ناو «یو‌اس‌اس آبراهام لینکلن» عازم خاورمیانه می‌شود.
این اقدام، غرب اقیانوس آرام را فعلاً بدون ناو هواپیمابر آمریکایی باقی می‌گذارد؛ هرچند اگر نیروی دریایی در ماه‌های پیش‌رو ناو دیگری را به این منطقه اعزام کند، این خلأ ممکن است کوتاه‌مدت باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70158" target="_blank">📅 22:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70157">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0bb40eea.mp4?token=vfmHAXCOs-Ix7c85MIZj8yrtEuAYC7D6onVBeaZl-xaJ8xjSKaqPd_ODLleGlNetoDp1E3zzx5wSDsnKK30W9pfjvmo6_0n-4oG1tuYnb4hEypehUzxejdZPvmHP7oPesemQeY7XbzQyF0n5p9gIu2p-c89pqHU-0beIJaP1YJk248my6aP9w0qqCoRaPFaJYBs-ARyptpwM4k2kOpegSzhiEjCv2mmXnhneHmbuKolLsNN63b9EeuMZXnEKMCRJy49vsFaKliQ_G9BaF3pWUL1dWRaC0KujNsJoFY_0e5QnVZZmtj_Lm9BKBY1knfAxqD3YPOEEHrtpPUrsZT7RUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0bb40eea.mp4?token=vfmHAXCOs-Ix7c85MIZj8yrtEuAYC7D6onVBeaZl-xaJ8xjSKaqPd_ODLleGlNetoDp1E3zzx5wSDsnKK30W9pfjvmo6_0n-4oG1tuYnb4hEypehUzxejdZPvmHP7oPesemQeY7XbzQyF0n5p9gIu2p-c89pqHU-0beIJaP1YJk248my6aP9w0qqCoRaPFaJYBs-ARyptpwM4k2kOpegSzhiEjCv2mmXnhneHmbuKolLsNN63b9EeuMZXnEKMCRJy49vsFaKliQ_G9BaF3pWUL1dWRaC0KujNsJoFY_0e5QnVZZmtj_Lm9BKBY1knfAxqD3YPOEEHrtpPUrsZT7RUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
املاکیه دلقک درباره کارولین لیویت سخنگوی کاخ سفید:
متوجه شدم که کارولین لیویت فرزندانش رو بیشتر از من دوست داره؛ بابت این موضوع خیلی نگرانم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70157" target="_blank">📅 21:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70156">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbbbc717f.mp4?token=Xc-KjRvAGZqnaFmP2cNqVqMmUSZ14XLNdbFuOcNKEVh8yRJQtTe_Vwa-e1yd1tH-glM0S4Lku0C9nzC70tRcpU_PX488CHiJW1ybMu5Ekns2obn_hJ4UiMxZY4QzPlg3MJsQm2ZuwTzzZ-tUg_pscoaWpdw8hkR7zgd90fLMkYv5IDmKnlMwhsdBYaIQEtJd-i4sqUuidcQn8qXHEVh8-l_KUPNtEspAR4IqTOmLQagCIC7weSVb6MsdpK1VnNUjycEfCFn6NuKXjs12HCybRXhLXakJEkdlXOnIMH1ZjjEF4WM6Fk_52WnSdWisTdsbHYUDlfEDS-h6_7Xi_2GxQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbbbc717f.mp4?token=Xc-KjRvAGZqnaFmP2cNqVqMmUSZ14XLNdbFuOcNKEVh8yRJQtTe_Vwa-e1yd1tH-glM0S4Lku0C9nzC70tRcpU_PX488CHiJW1ybMu5Ekns2obn_hJ4UiMxZY4QzPlg3MJsQm2ZuwTzzZ-tUg_pscoaWpdw8hkR7zgd90fLMkYv5IDmKnlMwhsdBYaIQEtJd-i4sqUuidcQn8qXHEVh8-l_KUPNtEspAR4IqTOmLQagCIC7weSVb6MsdpK1VnNUjycEfCFn6NuKXjs12HCybRXhLXakJEkdlXOnIMH1ZjjEF4WM6Fk_52WnSdWisTdsbHYUDlfEDS-h6_7Xi_2GxQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فرمانده کل ارتش ایران:
هر ایرانی ای که بتونه یه نیروی آمریکایی رو دستگیر کنه یا بکشه، ۳۰ هزار دلار (حدود ۵.۶ میلیارد تومن) جایزه میگیره
😳
پاداش نیروهای زن آمریکایی هم دو برابره و به حدود ۱۱.۲ میلیارد تومن میرسه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70156" target="_blank">📅 21:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70155">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f4c542f7f.mp4?token=C_2I37tGHbkOocBtMVuVA9-OoGXJkdDI1MSZb693U6jOuIQIsa6T4BGh4TYtVryBlqnfoim9cKJgkMhcvrlXfCexBbXfue_wp0NIP4z2GF-wQ2CRhF4xszY6DlVt8ShFBrTCznJ045-3M2jYgVTZxE4alE5HEn2Ep2RjMCrdDDQXL-WUZO0-W-ktCB4V09VqeG7U-qP1bifvQBq06iwNNsrlmxeEx66OcbNN5QNq0sMxhVa8famLIofy1T6jtdUt-x2eMJAQRKVy56BbR1_Htrl61QwZ9ZXdLrczJOyfJ-gmQJtdq-dd5jbsVSTkAx1S5rgx3kLbpbiZekN7ijbUGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f4c542f7f.mp4?token=C_2I37tGHbkOocBtMVuVA9-OoGXJkdDI1MSZb693U6jOuIQIsa6T4BGh4TYtVryBlqnfoim9cKJgkMhcvrlXfCexBbXfue_wp0NIP4z2GF-wQ2CRhF4xszY6DlVt8ShFBrTCznJ045-3M2jYgVTZxE4alE5HEn2Ep2RjMCrdDDQXL-WUZO0-W-ktCB4V09VqeG7U-qP1bifvQBq06iwNNsrlmxeEx66OcbNN5QNq0sMxhVa8famLIofy1T6jtdUt-x2eMJAQRKVy56BbR1_Htrl61QwZ9ZXdLrczJOyfJ-gmQJtdq-dd5jbsVSTkAx1S5rgx3kLbpbiZekN7ijbUGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار خطاب به پزشکیان: نوه‌هاتون بهتون نمیگن کاری کنید که مدارس مجازی بشن؟
🇮🇷
پزشکیان : ما داریم کاری میکنیم بچه ها اگه مدرسه نیان ناراحت بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70155" target="_blank">📅 20:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70151">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf26ef809.mp4?token=mcrOw7wW0x0VMaxipZ0NWQ8tm6gLRpYU2pLN_klTRMV_BBF2dBgsoBW4WmOZiWRIRPhNtW1YLm-sfbL9Df-YOv_tkGYbPF5JmTb1t6V7mmQbFq2qrRRzHaVW5TPw9vFC8wSQluE4sqL16pSxNKF8pBkxri6Ko-_hxetB9sg4Rc4V8FAYpis2q6mpwJYkJTtg1nWu237uSaHXg7nx976zjgznjRCX0-hsw0gAWZVhny5DxmtiV2w6pwYiNXwpdkxMNGpbTi-ZGGEOwInUrOV37BPgWiJN-UjT1D2MR3iKp0do_knGJJS_uweR-jFmDt-7ovMJkN8rv6fvom8dKRhxDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf26ef809.mp4?token=mcrOw7wW0x0VMaxipZ0NWQ8tm6gLRpYU2pLN_klTRMV_BBF2dBgsoBW4WmOZiWRIRPhNtW1YLm-sfbL9Df-YOv_tkGYbPF5JmTb1t6V7mmQbFq2qrRRzHaVW5TPw9vFC8wSQluE4sqL16pSxNKF8pBkxri6Ko-_hxetB9sg4Rc4V8FAYpis2q6mpwJYkJTtg1nWu237uSaHXg7nx976zjgznjRCX0-hsw0gAWZVhny5DxmtiV2w6pwYiNXwpdkxMNGpbTi-ZGGEOwInUrOV37BPgWiJN-UjT1D2MR3iKp0do_knGJJS_uweR-jFmDt-7ovMJkN8rv6fvom8dKRhxDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🚀
🇷🇺
امروز صبح پهپادهای اوکراینی به یکی از اصلی‌ترین مراکز انبار، دسته‌بندی و توزیع کالای Wildberries حمله و اينجوری داغونش کردن:
این فروشگاه اینترنتی که به آمازون روسیه معروفه،‌ سال پیش حدود 75 میلیارد دلار کالا از طریق این پلتفرم معامله شد...
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70151" target="_blank">📅 20:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63850d9e4e.mp4?token=lxWLW-sfT5saKFBYloCcnYSCWgrcHN64RHNJsRGNA4RSNshqME-pnUwBS5y6o42mdOMxCzXATnBUox3vtTLlji58moBDZx536Uzj6ZHPMg9T3zpZ7oakZgzU32drscW8CqHnzxUMjhsx4MqZonaVGa6ii02z52qUgiGmDFyGEna3iTQGjq-io0oTJMpCu7IK7Qv7c7tvJMHQnLRIocxm0AcKveJ2cWIhIsslsBVrZg0xvFH4OfEMaweC4uA0EUq7IfN2CSkV1M9qzs1JP41fSOOOXzjFuWNCRN1OhzGipYJxFPFPiA4dE-LXFfHqj79A3a9QGN4giu4g09RonShe63gjj8poqPrE7MR5W2J2tA_ghgyNqAhKpSd5B-p8MY4R0grVFjdtVm-4EU5CLKkkDpxDfI_mQKLvST2nRogGVBQGThlX114_0Yh9Y9OhPqelIqFLKHQU2dJ7-WMXucRuG_d6fAbk6ivsIfY6TIz7anWnJAJX74ioYkFApPv9Ku9C3t0LXlDecw3QJaKbfv0uuvnMA287xndlmzhBqvBuRk9vnC89AflhUIwbwHuWaU0A7uz9wMwmAnjEAcR9lbFkdE_BE221TKvdqSzrP0hjpsCahb8aOK772yUw9vAWFR9lFBnYMkUWq2Me72nslpn1EDxdaFM_5KAdnYTN4z3iK1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63850d9e4e.mp4?token=lxWLW-sfT5saKFBYloCcnYSCWgrcHN64RHNJsRGNA4RSNshqME-pnUwBS5y6o42mdOMxCzXATnBUox3vtTLlji58moBDZx536Uzj6ZHPMg9T3zpZ7oakZgzU32drscW8CqHnzxUMjhsx4MqZonaVGa6ii02z52qUgiGmDFyGEna3iTQGjq-io0oTJMpCu7IK7Qv7c7tvJMHQnLRIocxm0AcKveJ2cWIhIsslsBVrZg0xvFH4OfEMaweC4uA0EUq7IfN2CSkV1M9qzs1JP41fSOOOXzjFuWNCRN1OhzGipYJxFPFPiA4dE-LXFfHqj79A3a9QGN4giu4g09RonShe63gjj8poqPrE7MR5W2J2tA_ghgyNqAhKpSd5B-p8MY4R0grVFjdtVm-4EU5CLKkkDpxDfI_mQKLvST2nRogGVBQGThlX114_0Yh9Y9OhPqelIqFLKHQU2dJ7-WMXucRuG_d6fAbk6ivsIfY6TIz7anWnJAJX74ioYkFApPv9Ku9C3t0LXlDecw3QJaKbfv0uuvnMA287xndlmzhBqvBuRk9vnC89AflhUIwbwHuWaU0A7uz9wMwmAnjEAcR9lbFkdE_BE221TKvdqSzrP0hjpsCahb8aOK772yUw9vAWFR9lFBnYMkUWq2Me72nslpn1EDxdaFM_5KAdnYTN4z3iK1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت این‌ روزهای جاده چالوس:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70149" target="_blank">📅 19:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b0bac1f2.mp4?token=r1GGrXOpQ5FVnDGWNmFbzqOtpmh3-sMiI6s-obJYwHZotGglQD4v7fXb7493ywV4f51XFeGqNpDE5xv9dvY9EyxsLgZjRh8UBcs16cEjaQrVpDYH5PpW8hL8081968Wb4jTx5wOdrecrHmmf3otu4jP5hH_yf744AmmZVq0oGxOXT4tQn9JFoc1aYIatDIien1mkQz3r8R5m1mMIUCIAfJk28MpQS_Yl4-0997fQ156Enp9TbEu_yzXpWUzAn10JUBh5ds1Kanxoo1PYNiU_aSM69ZstOvslW6WbZiOaarrt2vIrKiRKHhHTCKzus8ZK5sUxzLk1x7vNuBGlynNASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b0bac1f2.mp4?token=r1GGrXOpQ5FVnDGWNmFbzqOtpmh3-sMiI6s-obJYwHZotGglQD4v7fXb7493ywV4f51XFeGqNpDE5xv9dvY9EyxsLgZjRh8UBcs16cEjaQrVpDYH5PpW8hL8081968Wb4jTx5wOdrecrHmmf3otu4jP5hH_yf744AmmZVq0oGxOXT4tQn9JFoc1aYIatDIien1mkQz3r8R5m1mMIUCIAfJk28MpQS_Yl4-0997fQ156Enp9TbEu_yzXpWUzAn10JUBh5ds1Kanxoo1PYNiU_aSM69ZstOvslW6WbZiOaarrt2vIrKiRKHhHTCKzus8ZK5sUxzLk1x7vNuBGlynNASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محمدرضا نقدی، مسئول ارشد سپاه پاسداران:
پیروزی کافی نیست. ایران به دنبال انتقام برای خامنه‌ای است و به بسیج دستور داده شده است تا فعالیت‌های خود را در خارج از کشور گسترش دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70148" target="_blank">📅 19:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f0e41933.mp4?token=bVB-w7j-HseVPynYaLVAtBjTztv49J7qMAL0Gs3t0mEfxrJe1Ji0_Rvc-EjYZ3Kzk0cs-cOUC28BmweWHOsWb38L7L2Pq335fbnGIWuriEHOmpA9OXxkygscNMFBPJCM3M2wCCkeBdEm_3aK_Kaulj7wgTxllHnKIrEmAH9P857kpXzDD8INcqBJN33A49_n1mZtuFJ2qf1HUuSCwArK-3eprUNpYhe8-je6-kwQ4U6EPNphKNBzQlwlrcZ9n_mllLIGIsfuoRYMKcu_9UZW-Oy9Dtdui01e7POYEN-KEqHbQfY9zx3-3VHf_GgNvnQ4b8f0bgSDFN3x0AP2Lzcnsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f0e41933.mp4?token=bVB-w7j-HseVPynYaLVAtBjTztv49J7qMAL0Gs3t0mEfxrJe1Ji0_Rvc-EjYZ3Kzk0cs-cOUC28BmweWHOsWb38L7L2Pq335fbnGIWuriEHOmpA9OXxkygscNMFBPJCM3M2wCCkeBdEm_3aK_Kaulj7wgTxllHnKIrEmAH9P857kpXzDD8INcqBJN33A49_n1mZtuFJ2qf1HUuSCwArK-3eprUNpYhe8-je6-kwQ4U6EPNphKNBzQlwlrcZ9n_mllLIGIsfuoRYMKcu_9UZW-Oy9Dtdui01e7POYEN-KEqHbQfY9zx3-3VHf_GgNvnQ4b8f0bgSDFN3x0AP2Lzcnsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیمان طالبی مجری صداوسیما:
نمیشود بنزین قیمتش جهانی باشد و حقوق ما ایرانی.
حقوق مارو جهانی کنید و ماشین ها رو با قیمت جهانی بدید، اونوقت بنزین هم با قیمت جهانی حساب کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70147" target="_blank">📅 18:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgmDDYyalX1afLYC2994vVdIV2b7FHdYbR0aECfiQrPdm6jOEZhRx5jRykNmZoMpjhz57ZUbU51zIh5Z-OhMHPh_3-uyLl-XjCzReprhmY6sTMjECop8RNUv3WWYNy0K35SGWgKhUavwFj1FjCFOQK3hMC0iDxLnVxCjxfDAlYuEyQ1a8dXuPmngleXY08tJNPRByaLQy8JpqmedzE9KiTXSRFHpNXQO8s3-r3OE-pXGJLnm18CqbHTNHsSRU_rFfRs_HNpxM-1B42nxqGtSL-Un5lotLXPEvefSM7LMGZotKcD9e50Qi-oiAt4crfx0ygGUJ969G2y4TKB1gsNo6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در ۷۲ ساعت گذشته سه کشتی در تنگه هرمز مورد حمله قرار گرفتند؛
طبق آخرین اطلاعیه مرکز اطلاعات دریایی مشترک (JMIC)، از زمان گزارش قبلی آن در ۷۲ ساعت پیش، سه کشتی هنگام عبور از تنگه هرمز مورد اصابت قرار گرفته‌اند.
دو فروند از آنها در آب‌های سرزمینی عمان در حال حرکت بودند، در حالی که فروند سوم در مکانی نامعلوم هنگام حرکت به سمت تنگه مورد اصابت قرار گرفت.
هیچ آسیبی گزارش نشده است و هر سه کشتی به سفر خود ادامه داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70146" target="_blank">📅 18:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70145">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70145" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70144">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIC1exRzqrtKrGxsRO29W8lKYm51E_-PpD_cKrthmf7sIgPdcbyXWhmW15HRliPj0w5NKWEcArpOWaqRiCnas-57t3yE28MpnvmXguv0qKJ7g5J5ybQ_aVvaDdeySQWi0rz5cNH9CXDv2ADh1lf1C9efCwpB4BsqTH_yrCwbRuIOgvC2ZlXUbZolZ70YzG6hmmSU4DNPbNuHdcen2brhA8MIcik-reuCyYrZ_MQMcV7yzUzqTIza31KFVJEpbdiJ55yO3ypODH4B146QKrzozZFMnnLxYlgIig4aNuiWsMI4cO3EhhX3INXAwd9SkzmQcYEBZaxgKOCsI73Z2Eewfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g25
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70144" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70143">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f965699a0.mp4?token=ui-4n45RFWuiR6bK6GSV_Q1dk0gBk5vkeTAR4dUSfYfbuHXrO91H5FjIUhRY6wHZI0Wyp4fNaBrNaEzvwandAPS7yB9EVnZIDpaSz1GFs3CWupcR-R_F__BUgFVSJXr1Z4cY-u30mKwmkWFWEFdlR2t7gdxqdVcyfOSiRZQftCfylK2Lnd0jxQd9AJiZY_XZcuPjAKLRCMN49T6P1S_34ceM4Ak6fDAPZS1Pclhu_H-KnBoXwmj5s14zd4EoPGDaWt6hi6Nr9PTSw96SfWz8QAt-_kFDQjn4zxpFA1JNvtzNEHPz5zbeVSOT3y08GBvcnfzMWWvCXQqISxiuYZy4qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f965699a0.mp4?token=ui-4n45RFWuiR6bK6GSV_Q1dk0gBk5vkeTAR4dUSfYfbuHXrO91H5FjIUhRY6wHZI0Wyp4fNaBrNaEzvwandAPS7yB9EVnZIDpaSz1GFs3CWupcR-R_F__BUgFVSJXr1Z4cY-u30mKwmkWFWEFdlR2t7gdxqdVcyfOSiRZQftCfylK2Lnd0jxQd9AJiZY_XZcuPjAKLRCMN49T6P1S_34ceM4Ak6fDAPZS1Pclhu_H-KnBoXwmj5s14zd4EoPGDaWt6hi6Nr9PTSw96SfWz8QAt-_kFDQjn4zxpFA1JNvtzNEHPz5zbeVSOT3y08GBvcnfzMWWvCXQqISxiuYZy4qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: از سال ۶۴ درگیر مباحث لبنان هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70143" target="_blank">📅 18:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa40fcbf2.mp4?token=hzN36YJH4x13vNHMDGaqj4VcP4WeXY0RlsxAaUnuaS6DiJWk_CuNB2UWJJLpviikKuvTeh25ujKxsQotxPDw9gxWDhys8ZS-ugI7BS9hrSebQDaAA4_wOO_6SZNF3_WuKHqGNX5GL9uAx3MCvC6iAAicOtSIUaNO9vt1L9DfVgEDd8gsgsilaEhfuHRdpG_F8qz7pV7H4haWAxSdecyjPNBHk8C8GIw2h-sX0NardT2wfh5q8wm5VYH_AAnaKLm7S9HUUM1ulAW0gNDybh7FdoBCBfgDVf7g_0cS5ENgLWNSBcsrOTbP43iY4DwsGQyicrBUXbHfP1GWJPW6Q1NyHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa40fcbf2.mp4?token=hzN36YJH4x13vNHMDGaqj4VcP4WeXY0RlsxAaUnuaS6DiJWk_CuNB2UWJJLpviikKuvTeh25ujKxsQotxPDw9gxWDhys8ZS-ugI7BS9hrSebQDaAA4_wOO_6SZNF3_WuKHqGNX5GL9uAx3MCvC6iAAicOtSIUaNO9vt1L9DfVgEDd8gsgsilaEhfuHRdpG_F8qz7pV7H4haWAxSdecyjPNBHk8C8GIw2h-sX0NardT2wfh5q8wm5VYH_AAnaKLm7S9HUUM1ulAW0gNDybh7FdoBCBfgDVf7g_0cS5ENgLWNSBcsrOTbP43iY4DwsGQyicrBUXbHfP1GWJPW6Q1NyHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مجری صداوسیما:
تاکنون ۸۱میلیون تومان پاداش برای قاتل ترامپ جمع کردیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70142" target="_blank">📅 17:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70141">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1YVBSX2YBJxInA-_tvGOMiOs0JXJ1eyok9sP7OpnYpteg1pd3l5Fx1MpSl80FdkzwNQB2C4K93NTs00kYiBsB-Q0lM9Ewoy0wKbtoeC5EWx3Z1svAXetxjcz3y9qjrF4nANB89tfTGPpFS-6VJJsElqA8K_Pj2xf7rFInys50MyYiHvbgaCyJyjTFr0ux7NP1M_rccbxzrqMVAp5LaK-FMhrbXnBWWjTuQEN0eXalfZwaB0BSJgjSYvo7PVCEzff5Q30xwrNJGDMmjp7ulCjql8j_4PRLUjMWRTH_Mk1X8onMxrGvzYh4mTDlHm3pTb_Z7Ur7SMRs7s8wrvz7DOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:دولت ترامپ در اواسط ماه مه، از «نیچروان بارزانی»، رئیس اقلیم کردستان عراق، به عنوان کانال ارتباطی محرمانه و غیررسمی برای گفتگو مستقیم با رهبری سپاه پاسداران انقلاب اسلامی استفاده کرد. مقامات آمریکایی پس از تردید در مورد اینکه آیا مذاکره‌کنندگان رسمی ایران — یعنی محمدباقر قالیباف، رئیس مجلس، و عباس عراقچی، وزیر امور خارجه — اختیار نهایی کردن توافق دیپلماتیک برای پایان دادن به جنگ را دارند یا خیر، این تماس را برقرار کردند.
در حدود ۱۰ مه، «تولسی گابارد»، مدیر اطلاعات ملی، با تأیید صریح رئیس‌جمهور ترامپ و معاونش «ونس»، با بارزانی تماس گرفت. او به دنبال ایجاد خط ارتباطی مستقیم با سردار احمد وحیدی، فرمانده سپاه، بود تا بررسی کند که آیا رهبری نظامی با مذاکره‌کنندگان سیاسی هم‌سو است یا مطالبات جداگانه‌ای دارد. بارزانی که به زبان فارسی مسلط است و پیوندهای عمیقی با تهران دارد، در ۱۴ مه امکان برقراری تماسی امن را از طریق تلفنی رمزگذاری‌شده فراهم کرد؛ تلفنی که توسط یکی از مقامات سپاه به دفتر او در اربیل آورده شده بود.
سردار وحیدی هم‌سویی کامل خود را با تیم دیپلماتیک ایران تأیید کرد و اظهار داشت که سپاه ترجیح می‌دهد بحران از طریق مذاکره حل‌وفصل شود. در پی آن، آمریکا پیشنهاد مذاکرات محرمانه و رودررو در اربیل را مطرح کرد. با این حال، مقامات ایرانی به دلیل نگرانی‌های شدید امنیتی در مورد احتمال ترور توسط عوامل اطلاعاتی اسرائیل که در کردستان عراق فعال هستند، از پذیرش این پیشنهاد خودداری کردند.
بستر ژئوپلیتیک نشان می‌دهد که ترور علی خامنه‌ای، رهبر عالی ایران، و درگیری‌های ۴۰ روزه پس از آن، ساختار رهبری ایران را به شدت دگرگون کرد و موجب تحکیم تسلط سپاه پاسداران بر امنیت ملی و سیاست خارجی کشور شد. اگرچه از طریق این کانال ارتباطی غیررسمی، تفاهم‌نامه‌ای اولیه میان آمریکا و ایران حاصل شد، اما این توافق به سرعت از هم پاشید. تلاش‌های میانجی‌گرانه موازی از سوی پاکستان و قطر نیز کاملاً متوقف مانده است؛ چرا که به گفته مشاوران آمریکایی، مانع اصلی همچنان سیاست سرسختانه ایران در قبال تنگه [هرمز] است، نه عملکرد میانجی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70141" target="_blank">📅 16:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo8d-J2MS_EUECxtKCO2ZB_Cbwh7KbvK7ds9WkGwK_4q02LSd9-rVeMTOAWiLySDMYOeAcjychuvPda7iX10exhgTx9djXv6ITpkS6ADZekX6mUBKTE--0vNCmQ-RYkGZ4pwyNKuuV0f1_Zr1tAvstvXu3hBBtIUFuPzGKEL8pQMg9vazhfFUU95cs9CZOVoiLsYNRM_5QXYnxnQOQ83CHmIKS5LvgBJUZXpAsnZu2CWUKlOM1MWM23LbGie_-XaG_vBQtoeTuZl3YxjI_oeAQFJ9p0S-iHSuLBS82SGLDgX9oswB8cgO4LDPo5GZCihhOSFFIGGeU61pdcHd4qsdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
کانال 14 اسرائیل:
🔴
ثانیه ها به شمارش در‌آمده‌اند:
تنها ۲۴ ساعت تا پایان مهلت اولیه ۶۰ روزه صلح/مذاکره بین ایران و آمریکا از تفاهم‌نامه ژوئن باقی مانده است.
توافق موقت متزلزل بوده است - موارد نقض، تنش‌ها، و هر دو طرف قبلاً آن را لغو یا به حالت تعلیق درآورده‌اند. هیچ تمدیدی تأیید نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70140" target="_blank">📅 16:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70139">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1685ca6213.mp4?token=V-K0aaeuT2S7NZU98PMsR-X2ck2CNsG4BFxENj2sOurkDmEtWf1gdkNhlL6-RkGVmlVh06i0_jljD3OiKztMlQHzL6MEPZpD5XcwoEjfNpuP_AXrmUPGQ8ukYALyx85k39nGoGsj8_WnXosVBE5r9rZTv6Ct5LD9VKC9VV6Dm7R51iEO_f5fEK_ZZ4jNr-JBLx_S8KBjMzt3stPPaHM5rOAAKch7WDbBbXV8lLEre5GRUZAB8z7bsV8TSSjfZ3w5HBdcLF3RqMtHCLPtSs3l99AkDRyPMErhPhZnpaM0RThVJLcMd1P_MmzyDJZpoH1Wkul05UZXpEq45xsHZo6XzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1685ca6213.mp4?token=V-K0aaeuT2S7NZU98PMsR-X2ck2CNsG4BFxENj2sOurkDmEtWf1gdkNhlL6-RkGVmlVh06i0_jljD3OiKztMlQHzL6MEPZpD5XcwoEjfNpuP_AXrmUPGQ8ukYALyx85k39nGoGsj8_WnXosVBE5r9rZTv6Ct5LD9VKC9VV6Dm7R51iEO_f5fEK_ZZ4jNr-JBLx_S8KBjMzt3stPPaHM5rOAAKch7WDbBbXV8lLEre5GRUZAB8z7bsV8TSSjfZ3w5HBdcLF3RqMtHCLPtSs3l99AkDRyPMErhPhZnpaM0RThVJLcMd1P_MmzyDJZpoH1Wkul05UZXpEq45xsHZo6XzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیف شاهنشاه آریامهر و ترامپ از خمینی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70139" target="_blank">📅 15:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f147bdc.mp4?token=uUg4DdNI5zJ0okBN54A3Z5PhL23bak3g6T8ElK40FmpF8DJcgtvd3AedmF25ScuoW14Srxq147cJGU95Dn-j3OUmOxSdFjE88Q5gKVeAv_p8doLYLh8FQpDcyT4CBcu0uLGsJjAmP-qtiYGSCeeAnVkaherMG4n0OMzbNXySBpw_IXjrJpdWUnVC9v0cShIk2AqKAFjh_qn4A5kbySTTt1kCMA9-v2AU8dsNhnTXneH3oVdAQknGybYj9HTqfzEcSRyUlch6Bm0-YRdZT7LF1Toct-roMiLSymBzPZ-gRid6Y1NFVxb89tsVJknPLaJCfDkX1QPShVKpw3bvQXpvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f147bdc.mp4?token=uUg4DdNI5zJ0okBN54A3Z5PhL23bak3g6T8ElK40FmpF8DJcgtvd3AedmF25ScuoW14Srxq147cJGU95Dn-j3OUmOxSdFjE88Q5gKVeAv_p8doLYLh8FQpDcyT4CBcu0uLGsJjAmP-qtiYGSCeeAnVkaherMG4n0OMzbNXySBpw_IXjrJpdWUnVC9v0cShIk2AqKAFjh_qn4A5kbySTTt1kCMA9-v2AU8dsNhnTXneH3oVdAQknGybYj9HTqfzEcSRyUlch6Bm0-YRdZT7LF1Toct-roMiLSymBzPZ-gRid6Y1NFVxb89tsVJknPLaJCfDkX1QPShVKpw3bvQXpvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مایکل مترینکو و کاترین کوب، گروگان‌های سفارت آمریکا در تهران، درباره معصومه ابتکار از اعضای دانشجویان پیرو خط امام:
یک عوضی تمام‌عیار بود؛
هنگام تعارف شیرینی می‌گفت مرگ بر آمریکا.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70138" target="_blank">📅 15:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig6TgX7tcU12LtNTU4zCKHWHn2NyjAOa9Ybskd-VbeoWrvnUFhw6omFvNTQHyftBJFgs7JOKuLNw3r1pV3DRIU0LAPJ2LXbA9kIOaKPP4yeFa3MWQnlPe5QzkW5oKBsPaodYAAYcB56egTIo88uIDqfq7cX9AsYeCP6D_tMEKFvMMnOL_2UDkl0X7r4LLVpRm787Y-di3AcQkS-4B9l0OnQDkJN1-ej-prFxFWrX8eIoSw8h4bHkpu6EkNHfwKSs_qxU4YsQdUh8XVHg2XhP4Q338iITXI1Uw8s_U-8OssJz4jYXBCXn-dQaQ0qCa1R-aRzxkql-AAQPLnaDsswhYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سند ازدواج کریس رونالدو و جورجینا:
در صورت جدایی و طلاق ، جورجینا ماهانه "100 هزار یورو" تا آخر عمر دریافت می‌کنه و مالکیت خونشون تو مادرید، به ارزش تقریبی "6 میلیون یورو" هم به جورجینا واگذار میشه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70137" target="_blank">📅 14:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70133">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HWjv0D0zqEzd2uwG0-edw9lcvKS9P0Dic_R6ILSP4etKS82lnjMF-eN_ObDDuCAwWme-3PkDBHFexwQRgRQimHMl3101UeeO-YMuPbfdhd1x17RJypRdqamDAK-C_BFwbcQgTM-siK3sp1EM0Zm-huM_6rqnl1Wi96MPhm7aVZPNHCuDN-uVIHdqaBiIa0LEizacNm0aJ8fTIgBfMvPKv4gCezMr5pWwYDw4qKIOtbaZcoDlt2gUcuXYFQ5iZRXTBRCgWy_b1kvuiqagmNaR3CkY-cPUJnTj3pzCZhGYpov4SPLGO1OB6gnN7nO3zSt5ExUzJUNS5ZJcZ9SdyTd6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKual8wEzfIytzGp6Tz2EOA6dNA5zYNrux5h6Zb6ZSdy_gMhKuBE8VkgG2togFMWf_5OxZbypm88Y_U0zitz3AiHiJJAN2UquPWjluuB9OyAqXMCxmzfpZAYP65_sbppyovPmzUa8JGLGABPTmimwChcDHpXP9lCkaB-ZN38LfSx7lKwj_VgJWqmxhQN8KG2C8XiPp-DW3_MREpQkvmsUI0uw9d28Dq8rW_IkG8ND7xaHws-SJUhRM4Nx9pBT_WiqKImucI-a1j-o_mFKQv5fKeG-tVH9XwwlIdgZzdA79xObUzIaEUVB_UKBhLTPauYRDUSHTRWfeAysogspDJPXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b276eb7f.mp4?token=k_2uAU9yTjhSmOx5O0xfWP0PQEmk2J1jvMzgzliUOKNDGKDdclGcKlQ83MbEEZl4dn86hNFFWIi2IXjrkT0jGgSET0nN23373zLnACxRk86XLyzQJjq-4KWqc8gzf7BeTkpm3O3dpPRS5zY1cdxGmj3ztzqBKWDTnJYXHso4Pvt0Mp9o5JeBop_tgiE3e8Kzipwe7ax2G354TM-tSt2gxThaFl49jgWvxqiwwVGmyES9sNSbCYvvY2VTCiaT30OgVT2ns3GgUNFfe5H9a3asCrz7af1qewykx1YGbgNoap23j5kVRlbTJUwQx-uR8UA52tIk-V_ORaTyRYHQOmZtEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b276eb7f.mp4?token=k_2uAU9yTjhSmOx5O0xfWP0PQEmk2J1jvMzgzliUOKNDGKDdclGcKlQ83MbEEZl4dn86hNFFWIi2IXjrkT0jGgSET0nN23373zLnACxRk86XLyzQJjq-4KWqc8gzf7BeTkpm3O3dpPRS5zY1cdxGmj3ztzqBKWDTnJYXHso4Pvt0Mp9o5JeBop_tgiE3e8Kzipwe7ax2G354TM-tSt2gxThaFl49jgWvxqiwwVGmyES9sNSbCYvvY2VTCiaT30OgVT2ns3GgUNFfe5H9a3asCrz7af1qewykx1YGbgNoap23j5kVRlbTJUwQx-uR8UA52tIk-V_ORaTyRYHQOmZtEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇨🇳
اختراع جدید چین؛پدافند پشه‌کش:
این دستگاهِ قابل حمل، با استفاده از هوش مصنوعی پشه‌های درحال پرواز رو تشخیص میده و با لیزر نابود می‌کنه.
قدرتش هم خیلی زیاده و می‌تونه تا 30 پشه رو تو هر ثانیه بکُشه و تا 6 متر هم پوشش میده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70133" target="_blank">📅 13:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70132">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8ff4c5f43.mp4?token=RuduVCxs5TyvKs6gCpPeUQ8ASnP-vSOXknf4AXMZjQEKwyvvzp8DBrdIDvsxpR7NCXdPDFDflvm1Tm3FRFMfuxkzbH9tV-toy4D7nyVZcn7VkJeiXfdZ07gixlkQ6IhKmEucAUeFKy5pnXzpJhmsr4OpLJkp-Tfqy4kq6eIXMkHU327KpofwenERJu0BCJaSd9XueLKk8zb6xp8YT9ssvkEr0nssVetyfxAJt2o-ZYWVZm42cejxn0Y7lXtpRmhsXh8y4oz0GhwIGR2mP1sTrHfiUlxkY9OGnuHAYofv3tDmeNdUwgqpBEQerBuXJTAei4WnUikXpmXA3zb5IM7P7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8ff4c5f43.mp4?token=RuduVCxs5TyvKs6gCpPeUQ8ASnP-vSOXknf4AXMZjQEKwyvvzp8DBrdIDvsxpR7NCXdPDFDflvm1Tm3FRFMfuxkzbH9tV-toy4D7nyVZcn7VkJeiXfdZ07gixlkQ6IhKmEucAUeFKy5pnXzpJhmsr4OpLJkp-Tfqy4kq6eIXMkHU327KpofwenERJu0BCJaSd9XueLKk8zb6xp8YT9ssvkEr0nssVetyfxAJt2o-ZYWVZm42cejxn0Y7lXtpRmhsXh8y4oz0GhwIGR2mP1sTrHfiUlxkY9OGnuHAYofv3tDmeNdUwgqpBEQerBuXJTAei4WnUikXpmXA3zb5IM7P7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
صحنه‌هایی بر فراز منطقه مسکو در روسیه، پس از حملات پهپادی اوکراین به کولدینو و دوموددوو.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70132" target="_blank">📅 13:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70131">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
چهلم بعد از ۵ ماه؟
در روزهای ۲۷، ۲۸ و ۲۹مرداد  مراسم چهلم علی خامنه‌ای برگزار خواهد شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70131" target="_blank">📅 12:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70130">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e871b80a60.mp4?token=Ez_Y5-PiL4YO4xLGt2eJW_-X91fh6V3fz0B4FRFYJ7FAgmghC9GyqRHr9uHOQNc6xrxSj37LC4CE7Rl4ijU_hMS70rymZAZtvPlTWUJrD0sG5ek8EtdpP_IPsDOHz5j7j0oZHpmrlL-fr9Tfe-R1Yu7KhEYCWQB2D_7rWh7Jr7pbZAg40i-gT2EzGz1sBZY2129JiwLkd7u3nfp8WQLceeqPhy1mObGvMVvZdDXMmUUP8YjCfGjSmvOKKG7NLCokNevyh7eayQL8Tp6jMKO14esIEIhpKAiAJcf38v3piXcrdFj84bZ144YExJW7Pw7XeW7WQzx72IkdZ5L3AgKCIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e871b80a60.mp4?token=Ez_Y5-PiL4YO4xLGt2eJW_-X91fh6V3fz0B4FRFYJ7FAgmghC9GyqRHr9uHOQNc6xrxSj37LC4CE7Rl4ijU_hMS70rymZAZtvPlTWUJrD0sG5ek8EtdpP_IPsDOHz5j7j0oZHpmrlL-fr9Tfe-R1Yu7KhEYCWQB2D_7rWh7Jr7pbZAg40i-gT2EzGz1sBZY2129JiwLkd7u3nfp8WQLceeqPhy1mObGvMVvZdDXMmUUP8YjCfGjSmvOKKG7NLCokNevyh7eayQL8Tp6jMKO14esIEIhpKAiAJcf38v3piXcrdFj84bZ144YExJW7Pw7XeW7WQzx72IkdZ5L3AgKCIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به یه خانم گفتن معیارات برای همسر آینده‌ات و مشخصات خودتو بنویس؛
نتیجه نهایی عجیب و جالب بود!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70130" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70129">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70129" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70129" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70128">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lutjdHz2C81eXHEn_SsNClDOy6hGcTm7zLX0f_nKp2TOgV7VNv2UW3ZAzeS946YOgv84bODTGjKA8d3WTuXUwgp4F2LSiGZkXK1BeNg_kWstn-9hpTfsg7ZULwSSHz-mOlk_EEZLZfu8mWNrHSGrAVcnNZWEhQNaAbE9ogdp0utLDrXaiQ0ZeNbpKvEuZ4mFTMhyCM85wExQoxc4AjOxz_IGiN14vPZ26WLNUi0BtDSAZEkPyrSqUckq-a9qjmpx7X-K8oA-K3uf4SAdKDyWS6c_-pjQudiEPy5Z26hSbVwd7inqs_cUFgCJN8JmHA_xqTnWsBtoHfMcagiZWYUEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r25
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70128" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70126">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a53c7e6e.mp4?token=mM0ZxJep7ao2vu5WArGYIAibU5WPXQl8Nty1yW183QxgtUj_F7BiJeGfJXyKMlOFvY8BSiXtMkiPEpNnxp5hLZwR_p4wcybHvFk4yx0uDRCCfsd2DfNlTQ3O9VgzUfkxDyi7Ydsz_JqnflJWEU0mv4wSVBp-BVa4MvDOGgWniQTYANImlAI-kGmmxofnHYLzi66beqL6G4k1TRjbJgBsMQK1ILD_cJObRdHUPux8NTli32fb8uhxJSAzIK6Tp2Ou_fv1tWX8Juz89HOSOzSs3xo_2CH5wkLm_1GvpXkuqTaoC2SQpTJAiiQOT_iTEeyMZWmJ8oxzJ3RxsMo4NzTV2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a53c7e6e.mp4?token=mM0ZxJep7ao2vu5WArGYIAibU5WPXQl8Nty1yW183QxgtUj_F7BiJeGfJXyKMlOFvY8BSiXtMkiPEpNnxp5hLZwR_p4wcybHvFk4yx0uDRCCfsd2DfNlTQ3O9VgzUfkxDyi7Ydsz_JqnflJWEU0mv4wSVBp-BVa4MvDOGgWniQTYANImlAI-kGmmxofnHYLzi66beqL6G4k1TRjbJgBsMQK1ILD_cJObRdHUPux8NTli32fb8uhxJSAzIK6Tp2Ou_fv1tWX8Juz89HOSOzSs3xo_2CH5wkLm_1GvpXkuqTaoC2SQpTJAiiQOT_iTEeyMZWmJ8oxzJ3RxsMo4NzTV2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
شاید براتون جالب باشه؛ کلیپ سمت چپی برای یه پسرایرانیه که بعد از سال‌ها تلاش، این حرکتو زد.
اما کلیپ سمت راستی یه نفر اومده با هوش مصنوعی همین پسره رو تبدیل به دختر کرده و گذاشته تو پیجش و حالا میلیونی بازدید گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70126" target="_blank">📅 12:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70122">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vitZlNPxJNMFe20pAi5KoGxPrpeWiht8quXjR4rY4pz8NbDpYdWtEaIqfDtaiZEPDd73ioLhKfjVfth3fhMvcKta1N3jr9XcqbHtV92sqEXmuOgdy4li05-ckuoJNn8g1lK8uSnXs0ygk0q2Uw3JkxNnb0DuY1brQvCn2X6eabpl0ynjIPfhRypRdSu2PIqlr7diKqcMX_pWEfQ5NE_f4Q2gOr-pmRopgt1stwQuQGCAaoUK6Ztapn-WVZm_QXCls76cI4RPTX2OQeOKJaLbrqJzUQEU1iyO6btqYq4uavnm8ZDVde5-9uufGUp6FXOymGIsDdJayz__QMj2bSst_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhFsGK9IvWKTqe81dPNQWQUEWS4S1N3Q7f6ExngzIzlCYj0l1_k-1hqT9RxC_gBx9iwXG_bxf1bzXVX1akAIaCSyeo6S2jgGuSBS4q39ssAabecXH4Xe0fr0Mod6-Hx39XorA_cihcsBO0YP4r3HelvjqY4pLwe8Dys09Xj6kjDW_XkZGizfN4ZQUnef8k8eC408Xeo-VAJWc02fyMoUtYljAzX0cRuW2-kGE7AisEic1lP9tn7E9QQ4vnyZCIzvwAmdkHJm0GlrU55ldzGJtfhIeak6yu6Rche5moy-_6SfVlD6E0d6TU5w3SmT8G4jN0F334HkYvNlPzyqosM9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUyLmlZMQCVy6HLdRA_unRhEBg8i5PmqNdCLSq52X_majRi1IJ8SqKLsajLCZ63JQr-X0NWMP5JSx0FXEm_CxvThcC4IAkpjEZ1IcmetOG2sWFO6714j-G4cceTotwX4O3r_vbhzW9fgHRzG8kX2AwuGcbRNvZxHDw5wBgI6cHLzoEzWaerfTG2jo4o3xvZcqyCDn7719aNV-XehOC6kDQrY-w2ysvo1dDUqMXAhAQnfycZbGyrYOdMbOrp0MqGg26cgoDuSWkNHOxAJpA9WzELqR4Xr-mR8sLE3ylb3DOWn9AglU6BGDwn88bE3zLxj4nlUn-DCpWchNQT3dNfo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wh7OPnvemFhDf9PXw9G6gVKJG9_HdDGYbuaAbyJxRa8-ddj4ZX5LmvogIjfsvbK02X3LW1eIOJit3ZVq_dwAjYsVbuHFOiC2Yw1v4U7pQE0c0m76aPeNHg3yYvQleI9nqMlQEoBPuaJadsn3pMwk97XZauWwTUghGut8mHm2adYc4-j-06UFNgJAVQMtbeMxZ77JPfv3qSY11_b74jqf7QbeyycTSy2E0neZtq7G6NeTF6Js4ZsLcpYo8Fr8cvpal_fuCDdPZRVcK0LZOjBF99SUrkFwE_s-ad1tqxQ4A8e2DBIZOfjihSry_NvkPQJwHtt82434_iOhIPyhSmVT8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👀
رامین رضاییان رفته دایرکت یه خانم دو رگه ایرانی-امریکایی به اسم «جول فرشاد» که بازیگر سریال ایفوریا هم هست و ازش درخواست نود و ...کرده.
خود بانو "جول فرشاد" هم با استوریایی که گذاشتن این موضوع رو تایید کردن:
بله میخواهم تایید کنم که این شایعات درست هستن. به زودی جزئیات این ماجرا رو با شما در میون میذارم.
اون (رامین رضاییان) جلوی دوربین گریه میکرد و از مردم ایران طلب بخشش میکرد ولی تو دایرکت از من درخواست هایی با موضوع خصوصی و نامناسب داشت.
خطاب به رامین رضاییان: میتونی منو بلاک کنی ، عکس پروفایلت رو عوض کنی  و هر روز سعی کنی اکانت هام رو هک کنی اما نمیتونی حمایت ملتی رو بدست بیاری که مدام بهش دروغ میگی و بهش پشت میکنی.
‌
‌
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70122" target="_blank">📅 11:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70121">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad5ddb268.mp4?token=Q0JOEvVH2tZV6AvR4JuEUPFAox8i0SBCXXsS8dSvIgvzVB-9M27HjMtlyG5DrIrKmC2hr4uBLL0ySu1gYf5gHhpjdplYVkZlfpchOl8Orf2g2ilU7msBtfQ0EDb31XUjbyok5Ev8WxicFd9Up4LnwKdQaXBvdd8YM0PVKGJGJPdQdM_GH9Ps4viOoaMWXVDAEJ5tTf30S7LhJv7cD_noomDbSgI3pBSbTU51qQh4yzUpefLTMGHDCmCpHHFpZvFtEeU7qOsULJLcHfvBQLB7BM_6jIRZ6wiyRvXQMY9dDVTDe5jTJvWd-Xk0pGoGKNNWBETngKPQyV4b3nK9RsQvaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad5ddb268.mp4?token=Q0JOEvVH2tZV6AvR4JuEUPFAox8i0SBCXXsS8dSvIgvzVB-9M27HjMtlyG5DrIrKmC2hr4uBLL0ySu1gYf5gHhpjdplYVkZlfpchOl8Orf2g2ilU7msBtfQ0EDb31XUjbyok5Ev8WxicFd9Up4LnwKdQaXBvdd8YM0PVKGJGJPdQdM_GH9Ps4viOoaMWXVDAEJ5tTf30S7LhJv7cD_noomDbSgI3pBSbTU51qQh4yzUpefLTMGHDCmCpHHFpZvFtEeU7qOsULJLcHfvBQLB7BM_6jIRZ6wiyRvXQMY9dDVTDe5jTJvWd-Xk0pGoGKNNWBETngKPQyV4b3nK9RsQvaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی چندین مرکز توزیع تجارت الکترونیک در مسکو را هدف قرار دادند و طبق گزارش‌ها، انبار "وایلدبریز" در منطقه کولدینو دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70121" target="_blank">📅 10:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70120">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61d35336a.mp4?token=p_Mdyl7NWxlq4XW6IuhAIp1lua07IX6KZsSXT787P3Nh5W8_OBqVDHBMSBT_PcaS0MZta1EKiZ40A9pQ1qNT3t8ovYHHM7qKCJHcGxQwakzpCj9_mt4YxBLGbYY810WJ5HVb1etXnhX6DY7ogxB0lwLEbp2YsF74Jo0iByPhk79q9MLsLY9Mjl6dHYjtIZy2DP9dfapvhUkfEWzZ6rse64GYYJ5hKebs010BMYuFATvDLoyBWmtZ4YLj_mWk4coDtT2X832ApLCyaiML47f_ATFEUrR8ostAq_eL-BZFinHnj7GokVbtg9c-PBJTBaXo3trLs1mjzqluMawh_YKz2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61d35336a.mp4?token=p_Mdyl7NWxlq4XW6IuhAIp1lua07IX6KZsSXT787P3Nh5W8_OBqVDHBMSBT_PcaS0MZta1EKiZ40A9pQ1qNT3t8ovYHHM7qKCJHcGxQwakzpCj9_mt4YxBLGbYY810WJ5HVb1etXnhX6DY7ogxB0lwLEbp2YsF74Jo0iByPhk79q9MLsLY9Mjl6dHYjtIZy2DP9dfapvhUkfEWzZ6rse64GYYJ5hKebs010BMYuFATvDLoyBWmtZ4YLj_mWk4coDtT2X832ApLCyaiML47f_ATFEUrR8ostAq_eL-BZFinHnj7GokVbtg9c-PBJTBaXo3trLs1mjzqluMawh_YKz2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از افرادی که وظیفه نگهداری از جنازه علی خامنه‌ای رو داشت:
زمانی که محل نگهداری پیکر رهبر هنوز مشخص نبود منو بردن تو محل نگهداریش جای خلوت تاریک و تنها بود، تو اون لحظه تمام غربت تاریخ شیعه رو دیدم بعد با خودم گفتم خدایا مگه میشه رهبر یه جایی باشه که حتی یک نگهبانم نداشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70120" target="_blank">📅 10:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70119">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvVaS5wCUMPpHfhlPIGGSlWXVd91upDZtA6Q-nsXds9tuI3Sk68X5Ewm3IXpUt9I4cQsZMIhKffaXcDxRrk4lUmRMN-jjF5jnZm5OLDgG3bxAy71iItEyddxZ4SKKP3r4J9jczRMU33GWBFZ5dFFh5W0Eu6daNs-FR1o_byj8xsriWX2fQSO2SFekYqWqwmnHtiAQl2ZS3TTrTIQzYPt8F8MDwscLHhZ-VqTCUoMCljk1lePsK6FPaKcEU1Irj5-UENInWTxxNFYq2Sj9BuGnv-IohvAzXsyTzPOFRc-h2uoBE9L_-AlR25pP2oGxZ4Ak9fiCjFnoDjT3SFaE7tGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسره:
۵/۵/۵ با یه دختر وارد رابطه شده و نزدیک ۱۳ روز باهم تو رابطه بودن.
بعد از اینکه کات کردن، آقا پسر یه لیست تهیه کرده و خرجایی که کرده بوده رو فاکتور کرده و فرستاده برای دختره.‌‌
اونم کل دنگش رو داده، البته جا ۱۹۰۰، دو میلیون براش زده و گفته فقط گموشو...
لیوان یکبارمصرفم حساب کردی مشتی؟ باز خوبه پول اینترنت و شارژی که مصرف کردی رو تخفیف دادی
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70119" target="_blank">📅 10:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70118">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6731c5b6.mp4?token=WSVB2Trsf1vXqcYy-0wzK70l6C0WjhPD0UxqF-By-7pFktwAvx0hTLUZrBQV8NtD_tTcTiT0_WhZlXIWbtyu9SXBS_eOplzmWUGD7f7Th43O7BHJ9i2bl-3XxxYzinFK2VAQUkMBOvbcuHyZmIufXeSMXkza_Q-AomF3lTEsbUZ6GwkhpXEh1TAFTyNmlURizyEcwjkbnADdAOD6TWu3IzGw_sAr-ThNxsHutzGJWQTIpgeuG-XZ-J9SEH8wrP2xL85x5z_A1ch1uTd77bFjqMRQoScNd6MfzvNI0mzlijZgSl2qoNL-hPRN6TvbMIaCAi037YgXdvqiLVwvBcSajA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6731c5b6.mp4?token=WSVB2Trsf1vXqcYy-0wzK70l6C0WjhPD0UxqF-By-7pFktwAvx0hTLUZrBQV8NtD_tTcTiT0_WhZlXIWbtyu9SXBS_eOplzmWUGD7f7Th43O7BHJ9i2bl-3XxxYzinFK2VAQUkMBOvbcuHyZmIufXeSMXkza_Q-AomF3lTEsbUZ6GwkhpXEh1TAFTyNmlURizyEcwjkbnADdAOD6TWu3IzGw_sAr-ThNxsHutzGJWQTIpgeuG-XZ-J9SEH8wrP2xL85x5z_A1ch1uTd77bFjqMRQoScNd6MfzvNI0mzlijZgSl2qoNL-hPRN6TvbMIaCAi037YgXdvqiLVwvBcSajA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
احمد آریایی
‌
نژاد نماینده مجلس:
مهسا امینی به درک واصل شد!!
اونوقت رئیس جمهور قبلی ما اومد گفت مگه میشه یه نفر همینطوری بیوفته بمیره ؟
بخدا یه ادم عادی هم میدونه ممکنه یکی یهو بمیره اما هشت ماه برای مملکت تبعات اغتشاش داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70118" target="_blank">📅 09:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70117">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=Ac2cXII5etKnJuGWvlhvxDl6xNUKeFBou9xjuM5wrZE7OKKNMj6M6bkSWsNBPdhI47VVmKUhnv2d5psGIGe3llu8Y4GFZLz4GS7e2EVoxsUX1fvVtid2jA122wyukIM6ywk941m1pgX86owHkbJzjBF-gRUIM6s-G0_PavIw_cvjANbytvBMUAG2pUf3gNPo7RMh0ceJAmM3pocCaQ-WSs1RNreEWXIxaBzoXlonKIQoDs77YW-_co0fMn9YOMJSRqeo6GzBrfMBRoXH6GzLK4RR-osWALrhGT8n-bus5a6scAnI2orqSYwtfxWwTyjhy1wPUuKBb8dhHf_t10o05IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=Ac2cXII5etKnJuGWvlhvxDl6xNUKeFBou9xjuM5wrZE7OKKNMj6M6bkSWsNBPdhI47VVmKUhnv2d5psGIGe3llu8Y4GFZLz4GS7e2EVoxsUX1fvVtid2jA122wyukIM6ywk941m1pgX86owHkbJzjBF-gRUIM6s-G0_PavIw_cvjANbytvBMUAG2pUf3gNPo7RMh0ceJAmM3pocCaQ-WSs1RNreEWXIxaBzoXlonKIQoDs77YW-_co0fMn9YOMJSRqeo6GzBrfMBRoXH6GzLK4RR-osWALrhGT8n-bus5a6scAnI2orqSYwtfxWwTyjhy1wPUuKBb8dhHf_t10o05IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسنپ لیستی منتشر کرده از حواس پرتی های مردم که وسایل خودشون داخل تاکسی ها جا گذاشتن :
261 هزار کارت بانکی
178 هزار کیف
137 هزار موبایل
یه کنسول PS5
لباس عروس
یه قابلمه قرمه سبزی
یه قفس طوطی
27 هزار ایرپاد
و پشیم ریزون ترینش : یه نوزاد شیرخوار
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70117" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70116">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70116" target="_blank">📅 01:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70115">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=vhZJRBcxIipwIbTQ1iZVElOadO47NwWsgRFmSYpgIflfaPKfr4J32f0hmbQnMl1ylAvfeK_SbgV2DUmjy29m7C2gAsAvYdyUSKnr-nIy8R06IPlIKDUNc_1SLWh8NSezQacq6lcRSIMqQt__w0iVFQbtlrl_qRmWlojT15h_9AENdNI4imrW8jq9YslvE5HwWr6dcZpR9ddOmSYnXW7yEnY5pc78E_ihtPwTXk_54p8pZ0yVV9DHIXE1E_Q-TmtWLqek8QVqGOC4SwsrrswVCXxV6ItARrHAlTz6VuM_WE_cv36yIVPOj_-c6TPUNTzeyiVagQhuYSHWiLX4PXCnpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=vhZJRBcxIipwIbTQ1iZVElOadO47NwWsgRFmSYpgIflfaPKfr4J32f0hmbQnMl1ylAvfeK_SbgV2DUmjy29m7C2gAsAvYdyUSKnr-nIy8R06IPlIKDUNc_1SLWh8NSezQacq6lcRSIMqQt__w0iVFQbtlrl_qRmWlojT15h_9AENdNI4imrW8jq9YslvE5HwWr6dcZpR9ddOmSYnXW7yEnY5pc78E_ihtPwTXk_54p8pZ0yVV9DHIXE1E_Q-TmtWLqek8QVqGOC4SwsrrswVCXxV6ItARrHAlTz6VuM_WE_cv36yIVPOj_-c6TPUNTzeyiVagQhuYSHWiLX4PXCnpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a24
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70115" target="_blank">📅 01:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70114">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkCqiifEHmKP92cO8RtLBvPbSGdnAOCX_XNCsrrUa2tOlgmBBCy8LoZzVxN8VgV6h6RCqQvWL0N0UwHhox83P981H12R7IGP9iX927HS3kOrKSR6T8xr6IS8h-AQj9qMRWwTbPksw87VMMXCoA6kDy0nStIuzVH6gc7yrsgWZaEwJg8hgsmd3TLY4pxeawh2Ip_Apg7OY86OoCWanT7mMRLw9LakXLrIY_twPd6OEUkG04qQ_B0YjlWAKzv2WMdnLUVXySNACmhdJBZmw0B48OOf7cKdXQAsDn4x54u5JQ8SyzO1ZyhXj6mCl7qbPXzZ6Hcc533horbqy0vGjfotTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
〰️
فرماندهی مرکزی ایالات متحده (سنتکام):
در تاریخ ۱۵ اوت سفر ۱۰ روزه خود به خاورمیانه را به پایان رساند؛ سفری که شامل بازدید از شش کشور و همچنین یک ناو هواپیمابر نیروی دریایی آمریکا در حال عملیات در دریای عرب بود.
دریاسالار برد کوپر با مقامات ارشد غیرنظامی و نظامی در بحرین، عراق، اسرائیل، اردن، عربستان سعودی و امارات متحده عربی دیدار کرد و با نیروهای نظامی مستقر آمریکایی وقت گذراند. بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه مشغول انجام مأموریت‌های مختلف هستند.
کوپر در جریان حضور خود در خشکی، از نیروهای دارای عملکرد ممتاز و کسانی که قرارداد خدمت خود را تمدید کرده بودند تقدیر کرد و بر مراسم انتقال فرماندهی «نیروی ضربت مشترک ترکیبی - عملیات عزم راسخ» (CJTF-OIR) نظارت داشت. در تاریخ ۱۱ اوت، طی مراسمی در مقر این نیرو در اردن، سرلشکر کوین لمبرت فرماندهی CJTF-OIR را به دریادار دوم لیام هولین واگذار کرد.
کوپر در زمان حضور در دریا، برای دومین بار در سال جاری با ملوانان و تفنگداران دریایی مستقر در ناو «یو‌اس‌اس آبراهام لینکلن» (CVN 72) دیدار کرد. او پیش‌تر در ماه فوریه به همراه استیو ویتکاف (فرستاده ویژه آمریکا برای مأموریت‌های صلح) و جرد کوشنر از این ناو هواپیمابر بازدید کرده بود.
در جریان آخرین سفر کوپر، او برای تمامی اعضای تیم ناو لینکلن سخنرانی کرد و از فداکاری و شجاعت فوق‌العاده آن‌ها تشکر نمود. او همچنین با نیروهای رده‌های پایین‌تر دیدار کرد و به افراد شایسته نشان و تقدیرنامه اعطا کرد.
کوپر گفت: «گروه ضربت ناو هواپیمابر لینکلن تیمی قدرتمند از آمریکایی‌های موفق است که با افتخاری عظیم و بجا، به دستاوردهای خود می‌بالند. تاریخ، این مأموریت را به عنوان یکی از فشرده‌ترین و تأثیرگذارترین عملیات‌های دوران مدرن ثبت خواهد کرد.»
ناو آبراهام لینکلن که پایگاه اصلی آن در سن‌دیگو قرار دارد، در ماه نوامبر برای انجام مأموریت اعزام شد و در ماه ژانویه به خاورمیانه رسید. این گروه ضربت با موفقیت هزاران پرواز رزمی را در حمایت از «عملیات خشم حماسی» (Epic Fury)، مأموریت‌های امنیت منطقه‌ای و محاصره دریایی جاری آمریکا علیه ایران انجام داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70114" target="_blank">📅 01:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70113">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF1a07XO8jFXIItOVeJYERoEBjZdII3QSzHQzV12LYS_fEWI4QSxHwwC3hfOCtaLFw9FgNyDXO4vcTkHE9pQBjIgk9tK9PlCz0spU3toarg0JyRF_ZYFjbZw7AVFSTvpmgclUu7_lJo5ST8fMYxys87DoZgMFafK9txGV7RPSikNqvTunupE8FaWs6V6PejFhirT4ouEmBYW6c3zyROqF3IkfYr-_ZkSJVNeSobbYir-B2WHZXZh4_H8-Ms0vAtzjb1DTNUNvVozgdrPli_4Qu5iMiM3bU3Y2ZfXy9Yniaofb1t15SQYpLOp2_z8JRWoUpwrA1oRMwcSEa8gEC21HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ با تصویری از خودش با کلاهی که شعار «ترامپ ۲۰۲۸» به سر دارد:
«ما پیروز خواهیم شد».
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70113" target="_blank">📅 01:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70111">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwP9P0LWyHST_3sy_49Yfhctx6Hi5VKjB6or_fekin6yhCTk6_fZ3XBFUGr5YdOJ0o0-P5t_gdhPXRCpyuXX0MXo7oZtzM92GrJ87uR1mIddB7oFRfLj-eLZdE55i3xO3hhAow0QTHQByVjIlxnSClW1zPwIPrUIbVExwKf2sQ3yMQJjWJs2w5RQKOKcjJCwG9gNkuuMvG0Y_q7wEAsSkvcB_WUHboJPOBgf_sngWCjC4AIFJtxJ8H1XrZdp8TeQtmrYw6VBqyUS65jicRLJ6_F5qO-OFUoYV8wUZb2gDCKS9WYU2YvLENGybdNJw98FXx4_q2xH9mvHeM4orEyeig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0a274391.mp4?token=h2H2BuO3w8xHpVMDJ4dDyTrAKtC4ResMwDXzJT3rDa8Vbdy4dpBf1ej5LVZwzWKBI6EhoGuIi0stQlR0ncKvYC58QuNuZKmfnDhQoRPOwu2EIBMcR5Fm7hOtR-l1fN5ZDx3_TeXEhEdpJleWIYBd-pYDVsJdvjIXwtX6wyb4a13u1dgGETmOolxaULPoVdwAaMAwK7CdHX5QIcYV328eupCpaPgPQ2wHxRZkJmC-8G2Q8tSRaNNalqTP9XjB8OYg1D1A7rfAcLuO-O7D8mvYzmOGzK-m7xzf-gZT36mSBBj9h33MKQxtNCpwSjLuyqKw64lzEcM-mAwCf8ZeShtrLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0a274391.mp4?token=h2H2BuO3w8xHpVMDJ4dDyTrAKtC4ResMwDXzJT3rDa8Vbdy4dpBf1ej5LVZwzWKBI6EhoGuIi0stQlR0ncKvYC58QuNuZKmfnDhQoRPOwu2EIBMcR5Fm7hOtR-l1fN5ZDx3_TeXEhEdpJleWIYBd-pYDVsJdvjIXwtX6wyb4a13u1dgGETmOolxaULPoVdwAaMAwK7CdHX5QIcYV328eupCpaPgPQ2wHxRZkJmC-8G2Q8tSRaNNalqTP9XjB8OYg1D1A7rfAcLuO-O7D8mvYzmOGzK-m7xzf-gZT36mSBBj9h33MKQxtNCpwSjLuyqKw64lzEcM-mAwCf8ZeShtrLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70111" target="_blank">📅 00:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70110">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
رئیس سازمان بهینه سازی:
🔴
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
🔴
دومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش ۱۲۱ میلیون لیتر تولیدی روز بین خودروهای موجود تقسیم شود و هرکس بیش از سهمیه بخواهد باید بنزینش را با نرخ آزاد بخرد؛ تقریبا مشابه روشی که قرار بود در کرمان اجرا شود.
🔴
سومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش سهمیۀ بنزین به‌جای خودروها به مردم اختصاص داده می‌شود؛ چه خودرو داشته باشند چه نداشته باشند.
روزانه حدود ۳۰ میلیون لیتر به حمل‌ونقل عمومی و تاکسی‌های آنلاین و غیرآنلاین اختصاص داشته می‌شود تا قیمت آن‌ها تغییر نکند.
تقریبا ماهی ۳۰ لیتر به هر فرد می‌رسد و امکان انتقال و خرید و فروش آن وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70110" target="_blank">📅 00:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70109">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3808337972.mp4?token=MQS7UAF8NGVJKsBIfdM3jWuEp-ytBakSe9oxXJwoXkCkOfjkgDc30q0dWAvfuXtLKNVFpqUgpnPZHX5E4rqha7X1LTlTWQ4y8XuDGGVWqFvZQFQCXnSxO6Nf-1RoT46jyLkWcebRVqlQ66cQKSzHmm_2hku63CYZ2I0k_-sEE_jjWY00QdPTl3yBkeGwooYtp2LcoGUYBrdedPyHu2HU2zatvWgjWlYsi9XWjFgCJNNINSiaEUbo2s32ERQug20Mr9RD_yK4biGvDqp-0WjVZcQdLHf36qkdCPuyqt5SilZgQW3XEju7zvhgVkPMVZniH2X6FDMhhr-e-Xt6WNg1mhwvdYiBeTfQGbxYsoT06G5w39PtHD7XfW8IqdoWwdRu_bMRdg4b0Go8e1a_i0lBStWYX-sGwncitoBeHdoEQWyALm6FEFd_k-Raa6NyopDLG40_67oMcqGKJxpiKs50cUYsYvfotDhmNXIoEcW9MOm5qhgDTX228FwVanwrEJftQC7QCVJY0RiRilkeEoRrZBz1J4-KpaZK3Thqlk_TwakkIJd8NvdEnzvHEa4V6aM4zuxF4ivd0J2p1wk5ZWrVgQSJzvft7McxsWUu3XZRggcjSa8XeFIqDKXdE2w0QpTKemlt5NKskgwIzyTIrjnvZspI29UpjBYLmqtxtfHjrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3808337972.mp4?token=MQS7UAF8NGVJKsBIfdM3jWuEp-ytBakSe9oxXJwoXkCkOfjkgDc30q0dWAvfuXtLKNVFpqUgpnPZHX5E4rqha7X1LTlTWQ4y8XuDGGVWqFvZQFQCXnSxO6Nf-1RoT46jyLkWcebRVqlQ66cQKSzHmm_2hku63CYZ2I0k_-sEE_jjWY00QdPTl3yBkeGwooYtp2LcoGUYBrdedPyHu2HU2zatvWgjWlYsi9XWjFgCJNNINSiaEUbo2s32ERQug20Mr9RD_yK4biGvDqp-0WjVZcQdLHf36qkdCPuyqt5SilZgQW3XEju7zvhgVkPMVZniH2X6FDMhhr-e-Xt6WNg1mhwvdYiBeTfQGbxYsoT06G5w39PtHD7XfW8IqdoWwdRu_bMRdg4b0Go8e1a_i0lBStWYX-sGwncitoBeHdoEQWyALm6FEFd_k-Raa6NyopDLG40_67oMcqGKJxpiKs50cUYsYvfotDhmNXIoEcW9MOm5qhgDTX228FwVanwrEJftQC7QCVJY0RiRilkeEoRrZBz1J4-KpaZK3Thqlk_TwakkIJd8NvdEnzvHEa4V6aM4zuxF4ivd0J2p1wk5ZWrVgQSJzvft7McxsWUu3XZRggcjSa8XeFIqDKXdE2w0QpTKemlt5NKskgwIzyTIrjnvZspI29UpjBYLmqtxtfHjrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
وضعیت کنکوری های امسال
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70109" target="_blank">📅 23:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70108">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
❌
طبق گزارش های غیررسمی سپاه لحظاتی قبل از سیریک به طرف تنگه هرمز چند موشک/پهباد شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70108" target="_blank">📅 22:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70107">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrTnoeOKUA5vjiOCen8onenqgdBwLR29BraCO25gxHWhtjJPvxxCJRABV_6fKrKjlEV7oekr9xmequ5FlmUGwIzG-YgKclZThYxLB1Z1nzPyVYEmlaG7GuBLcZ17BHit2bamfLrBhIFH3qrjEG0Qnzh9YQl1WymHmGaGk2T-xw5zfVUDm1OT__qK4WjT3FOsLQ7j9PdbR20cyhOjY_nVygvaKj-YDxePczTguOAY9SLkZPmFlJk_wpUook0h2FM0KE-3xgQv-5sK1Kh7n4aOzRhNpFJoCZYg8yqcSpSUs20PodeQypUeuvHPJm7lE-3YdD8dPvOKnopV4EUVr5jocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
با وجود آن چهره‌ی غیردوستانه در این عکس خاص، عکس‌های بسیاری هم وجود دارد که در آن‌ها لبخند بر لب داریم؛ من و کیم جونگ‌اون رابطه‌ی بسیار خوبی با هم داریم!
رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/70107" target="_blank">📅 22:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70106">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c505095a40.mp4?token=J4ia2gR8wNUKNzV5DpK2RpEE46NAXCeHNeg7EMzUSNWo6_jSEu-ZkdQbgeLWpWq2Yiakn8tJbocvSiBrDWeyTno09WqnYOKNA3YzqgQM3khRu3AWBEZUNP_fjK70MdFt39cpGaC5U7Cd8ECoxSv7_MXaCMes6-LEVIXi09x4gBH5vvSUVFXLawDwyzqmWexfL9D2qbLrcRhlRjI7H27LwfOpMD7JEiy_qYoqmJsd-KcWziSHEKdBQW9DrGQHPtIIy3azbxGmL5Op6hPw0wuq1Ct1Fm8b3kQXLl2mINWuSSgumslST1KLFkd9Q3TsbpPkTYEM52HEzmmOibMU_gyrsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c505095a40.mp4?token=J4ia2gR8wNUKNzV5DpK2RpEE46NAXCeHNeg7EMzUSNWo6_jSEu-ZkdQbgeLWpWq2Yiakn8tJbocvSiBrDWeyTno09WqnYOKNA3YzqgQM3khRu3AWBEZUNP_fjK70MdFt39cpGaC5U7Cd8ECoxSv7_MXaCMes6-LEVIXi09x4gBH5vvSUVFXLawDwyzqmWexfL9D2qbLrcRhlRjI7H27LwfOpMD7JEiy_qYoqmJsd-KcWziSHEKdBQW9DrGQHPtIIy3azbxGmL5Op6hPw0wuq1Ct1Fm8b3kQXLl2mINWuSSgumslST1KLFkd9Q3TsbpPkTYEM52HEzmmOibMU_gyrsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب یکی از هوادارای استقلال داشت شاد و خندون از تیمش تو مصاحبه تعریف می‌کرد؛
که یهو رفیقش تصمیم گرفت این شاهکار رو پیاده کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/70106" target="_blank">📅 21:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvz7s8NtWrWNflSvxUl8zRB5LFFrEHpnAH5whEnHZl20sCXqMkFyyge9YX4bC9ga6l0B9JcLRjMKb8iu0JGBWGyUgKm7_P4US4OMsYG47q6-a16yJUpxS9yWN39v-F11B0sUvNnJWbQZensOaJuGPllYx9JuBSQ5TP2g9rmw3-LJPZQJSgpsXGn-216HGc5gqsP33tu9WDZ8c62xyc5DRKuIg_N4E5kufPRueW-XTH84mvQTqx9prq6PaESjyLrR_zxah0DO6QMFR15RQJ3Po8yia6WtaaMOS0LJTmrcI74kWzlZLUuqUJP5f0BRuWEs2PCTwK41_CWLdyvyfUvDKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dfwaWnxwCeAi2O9uro-m1l8hEOg8Lqj01oA0AbgUMp3cwZmapZlLYIE_9p71g7Mf3PeLFB9dQlEowJ39sOTFal3O_NlWnBgzmzx_YskuJ6yOcSsLfy_WS9qR2I3BiJj04ehtuGUgd0_cyvKwhBuZxqXYZuWZNao61mmyEKe-jg0st2XQ0qGVv_X8uoHPcIbA7MEkQoilBTLY86jD9fW90bNvEMvluG4QeaicjFbvCtA0MWADIi53R5nv27tBrDJ8ZjoaPD9Q88TgRmlUbNVDlUIOQzfHKao43gymsfqWDD6n7M_luk_Y6IoXaZqofBR3QEqO4dHJurKFeuD4CYi9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVtgxs2mmsU26RRS2Wj1e_MjxE3Y4YiZW7Ve2xtDubIOwKd0P4vWWl6lwt68QJa4pWzqgorHp8BOX6sZUR5M-ijF01bIWlc2yRfI7c-L22KuBjS3TnI6c7WHR3pfyagEEGR3V442SR_rSwEZQ-_K_s5nyduMk1OZjs1vMIRzBJQ7wbun2XVnQV0WmcEshnRGRhG8691vAD1TWR-T6Zv4N3Y4c1_CfW0NH5Ss6-UJuMrvSKLkMewIhMT4833EOyTPtCUcfx8o9CfJ7RN5NhJ6f00Av1uq8ZQszQud-sHxQtvE_lkhF46hr7U3Y42Dm5GK8Lxqu3pOVWe1i1Z_OM1sbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست و استوری نوید محمدزاده و حمایت از فلسطین
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70103" target="_blank">📅 20:52 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
