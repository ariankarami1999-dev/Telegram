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
<img src="https://cdn4.telesco.pe/file/mswG9WrXWmyTnlM6inCcPUKERp5ISVy92UpEIGokcO7d9ep0KC2Bv11jJR6yxU_ahekZsIwnuek-wTbXb7JdQ2pG9eSluC8jf6ruPfLvJuKTcb_bjPfjE5FTkaUgj-M18QKmfglEOfbMEzcj_9pNuq7MhCOVj4uDfd2VMmcXhOTxHslKBmsmWGKFhDQ-XriC864glkL8FNu-5bnMVJneGSY7Rrz8evabqStrRSaKLfGzlgxpj26BxFxDjyHEVqcY_ZPgqguK6lUhi-IE57oXsgvkq1-vC7h9p8a66zfna5byc7f6sf0_pMGkyEhqYTVq5p2eju-m3f9dy1Z64W4-Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 09:53:06</div>
<hr>

<div class="tg-post" id="msg-663791">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcPS1yfMPhPxQnBOOksG7xqbZW9XyfHjy6jgCPeFAjYJfBNtL7ANMefiQtK6Szg7FsTsPOTQI8lhfUBIlnF40_C320eoi9OnqGmMAkmm86k5O1ChEtXe-k7jcDoZxpbSccXv3ocJ0vLdCo9qOygZnRIhmLk-X26hb1JEnIgadXIQW8ISmasBTv5NTRoXchCy-npnwe1YnX32grSVRAVZxXN3SD3ELK3goNpdPh-V_Ap70PCmrdw247ecSvLLTZbvta-EbrQCsrq0ZWFHIGbiAXVWDcaa_H8Lp6TFQtspyozs-B4vBVHNuhqmb2f8AvKJ6R_MtHWqv9yamZDbHGy4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا گل ایران توسط وار رد شد؟ + عکس
🔹
از همان دقیقه رد شدن گل ایران به دلیل آفساید، کاربران بسیاری این تصمیم را نادرست خواندند و معتقدند که گل وقت‌های تلف شده ایران درست بوده است. اما واقعا گل ایران سوخته و داوری به اشتباه آن را مردود کرده است؟
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3225956</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/663791" target="_blank">📅 09:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663790">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImyTiimkMnPEMU-EEnpvcRJJqAwS7fdLhq0mJSrFhOIrSZwFSJ9D_LUIu-KrIz4vDxpPjz_rJXn2Ri6Gqb9P-SNahjyoCmSgU_AyYrNbF18_dgjPW4Zg74UDEAUtfoqaqoh95PnGa0ENF3M9YX9Ue2KpHXQSslcDGk9Ys0AYlePx806Q41gmf3aQjU783s3c8pMN1aXBmJE7V_-54lhXxCOojcLpkZcp1kz3cp1pAeRnq-ybI_uioMiK6eHkWI2uYSe1S6GMwQITESbNCVQkTMxrNouXikQq8asQLyHyuDV7oKYJ1aMQkLF1ugXkmN3-e904m9cPqH8fBFGsn1hg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رامین رضاییان با بغض و گریه: می‌خواستیم مردم کشور رو شاد کنیم ولی بدشانس بودیم/ مردم ایران ما دوست‌تان داریم و فقط می توانم بگویم ببخشید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/663790" target="_blank">📅 09:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663789">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a952300921.mp4?token=iPmY7semxR7cMaaf91mfDhLsrwU5wbzgvvg0uULwm_L442S4fEWc7IlKXWlkLNfcJvgJO4tzc_WzlBMK5BD7TLw_u-lvSDbSapBd6IFFseqbAEr4YgGqodCaOJTGZdjGzKQ43rPeAathSFRUbbcuDWNMx_42N2VPiXIMGmOPghLFPmWwevgmQ_Ij30asPBuujFaycBGnbc9oYEJG8CaoPPvMpNCCTIz8cDEcnf82lo55cahXRK45dLvVAjHGzrMEBdLQOrZKL9Av-sc1wI7C_e8vYI5bYJ1YGc8l8S1IK0BuCL1oOg1DfjP8_2fSlhpQn-Vw0_sAhwImqLPKNKYaUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a952300921.mp4?token=iPmY7semxR7cMaaf91mfDhLsrwU5wbzgvvg0uULwm_L442S4fEWc7IlKXWlkLNfcJvgJO4tzc_WzlBMK5BD7TLw_u-lvSDbSapBd6IFFseqbAEr4YgGqodCaOJTGZdjGzKQ43rPeAathSFRUbbcuDWNMx_42N2VPiXIMGmOPghLFPmWwevgmQ_Ij30asPBuujFaycBGnbc9oYEJG8CaoPPvMpNCCTIz8cDEcnf82lo55cahXRK45dLvVAjHGzrMEBdLQOrZKL9Av-sc1wI7C_e8vYI5bYJ1YGc8l8S1IK0BuCL1oOg1DfjP8_2fSlhpQn-Vw0_sAhwImqLPKNKYaUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به اروگوئه توسط بائنا
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/663789" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663788">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
سرلشکر عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا: نیروهای مسلح برای تقویت امنیت پایدار کاملا آماده هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/663788" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663787">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BW1090oJEs26AQ7b8V2-Vb6PDX7FZNa4CC-dQm_yM80D9Jhr44n6ggjVrsV98ax5IlRTgwM4RBccfTG9R2514SwVGl_KTcMuKr_0ltmQJ33u6Ph1h7WHHJJvbS2nkeR4sTDGId_1DPRUDwK1kAFWZ5mA9yGKPk0mefxWm0lBi4kvxG68ze-NTIqHHETtjk-MTeW6vLg4XBcFtpv-VTEz8TYk15llEQL3R8ZlckRflxyHIyrf0uowRspN3TmJlCkNaDbJOrGIq2iDwWRHaCL-1lL_rQCw-sl_adr1f2P_1NGNNRr3h0Re16QkdVVjz8Sf31UdhXiOa5el1b41eqcBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در صورت قطعی شدن صعود ایران به عنوان تیم سوم، ملی‌پوشان ایران در مرحله یک سی‌ودوم، جمعه ساعت ۶:۳۰ صبح به مصاف سوئیس خواهند رفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/663787" target="_blank">📅 09:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663786">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/69803c621e.mp4?token=n9oT7gomkmCXYJ4BswhnBQcHzCQxAFI6sVZPxsZZjThu3G9Uqh5H0RBix4wcL-o5sNV0nK8aSgHsx4dRf77cM8h5rEp17T3LoBp2UvocGL_R1c9tdMBbM1SgqEbcSUDpltoaoHlEOUul5GUlv3eI1wZP6XZjG3wuZlp8m8k4uSFhmdo3FccgV9wcXhyPbuUN-62XbRQcnrMUPu8qwtp0CLUjUquVsvRUHiCjoSzjdRFJryh3spZ4CIuHe607Je3bY8KkvzpJwCsqrLXnnDbZWmCawZdUHyx4W-csXmCIgGFtEvR6_pbGEdhqdwyzZDtm2v8prP8MMZat01uWsruL8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/69803c621e.mp4?token=n9oT7gomkmCXYJ4BswhnBQcHzCQxAFI6sVZPxsZZjThu3G9Uqh5H0RBix4wcL-o5sNV0nK8aSgHsx4dRf77cM8h5rEp17T3LoBp2UvocGL_R1c9tdMBbM1SgqEbcSUDpltoaoHlEOUul5GUlv3eI1wZP6XZjG3wuZlp8m8k4uSFhmdo3FccgV9wcXhyPbuUN-62XbRQcnrMUPu8qwtp0CLUjUquVsvRUHiCjoSzjdRFJryh3spZ4CIuHe607Je3bY8KkvzpJwCsqrLXnnDbZWmCawZdUHyx4W-csXmCIgGFtEvR6_pbGEdhqdwyzZDtm2v8prP8MMZat01uWsruL8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج جرم از تاج خورشیدی/ ویدیوی منتشرشده توسط ناسا خروج جرم از تاج خورشیدی را به نمایش می‌گذارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/663786" target="_blank">📅 09:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663785">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyPU4P6oMUJN_nFGh3bfJ5a4ozt1IOLCA0DEQ_rUDIBKGGugBlBL-Ky604Vgf7R-WK5nVB9wD8ESaGhXt4fwMzx_1VF5it1_4IzOYGE1FmXQ6WWzhWDezLgLHBuR_wM30DfqgrNGd74yNchTPPWl-ETBISio3-stLMWWInlmSpF47QP4hEaF-eORuMrQ-eo8lc7e-maOzYf1kWDGnyhK67CRhUQNgj6olBOi8oaLLpwB0h9zvlqBDqmy25nkeiG4emuqnuE3tFPbuhYhMmTWa6yY99g46PoYIcodd5jXO9c9KRIpA9IdjRj8Bqo06W3P7FRENZmttwNgyNw7zOOfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شانس ۹۲ درصدی ایران برای صعود/ برآورد سایت اتلتیک از احتمال صعود ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/663785" target="_blank">📅 09:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663784">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
نخست وزیر پاکستان: اوضاع منطقه اهمیت امنیت دریایی را برای اقتصاد جهانی ثابت کرده است
شهباز شریف:
🔹
وضعیت منطقه‌ای اهمیت امنیت دریایی را برای اقتصاد جهانی و زنجیره‌های تأمین نشان داده است. / انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/663784" target="_blank">📅 09:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663778">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7tIvhiIJCBvdlqE7oDA5NH0ayBkSt31LBoncD7dIyPdq0bEnfSnWWcAk15b1uL-W8xFDHUwwFGGOVZECFSS0uJMNSmL9_Lyizs3_MdHhwLKYfIN2u-QXJhJea18C7ANvbDGdUsnkPUpe7lWtOk72L28BHUYyEw0xONUFexMKY09K_8GlGZnwvzwBhrTHOAZsBEexVPom1XkBxM6eKbqG_QiGSEU9jtF57GLx7kN-M3ggkj-7m3nJ8NvPb9gqJVpySDMXTGlUWSvkiSWhg7in6akQvtvZVIsW6T1XloY0XOTBbFgJwcdzR4I1aPJ0QBmRxXeRbgRfFHFC82LjHMtAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVh1_jhohFA1wOtqCVphjV4qlcKxppOJDyyAfkuS1sl3qI3f4rGulEsiZiuOdhjB1OtsO5REf3x1QqpfGo3JgWDCT2mAZ7gEe33Rtsnp8w5ITq9i_qh5uJnk_nwOaWAOdGxC210QgKQZsT81lIV_w5eMcyTqliPTawixDx44wbtolF9X9g923HsorfXIZmat8dPHmQ5KpRJV9daEb2gCEngABIzM4eKyqgZP3Ll0-Hsro1TjaKcA7yGf4YDdudG3ZO7QvOw9-jXsg4kQDGXaAwFXJ8aDFe7uCPzlLWmbq4gcnNrVBAS-vUXo5_y56iPxgXqD2PFnB0Vts4MLDY8QtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A10G0uVKzib0Q7fDODKYshmOAgcogMYXE6Olt8DxU6zrL5eselKsu7R7jAcPIkernNbk_vsKh1id2R65j_i1v5un-ZElK0H2jBQrNX3qwAn7e1bDh1SysAyg__wKdt2OWrjyjcQoKjPjWPNnTzIqwJchaaM2Ff7Q0Vtg9amB__kVg0Ph6Vs9mrZSIGhKtxGKWUKNzMjEA2kE-TqHPkS58oOICFJ6tq0LqYMQl8_7vaU2tB7j7yG8QHwOzSZyLffd15dJhTGGDdbHIW3GlM2ha73IyhUY8ayIYaOCssBdTmlGJJVYZMDqnDMFeASdyKC79he2nhf4crJs7yhV8zZWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hp5WDAo6AzpsbqSvbCQsBD4lSaunu9SR9UsXhbDsfCPVAQnQMoP37JBB-aYuo5o8YCGvmkV-1LloqOdP7tC3LCAPO5oD4kLjzwLa_DYZvtf0C5DH6lSjTIKVoaJXUieK2mnjiwmdfshHQXDqkkiS6hNKrj2xJHzHOHAOKxt12yyptI6irDdRnMZKd8ZRjCPEEmUBxp0oIMcapXgeZxUq7hVgAtHxyjoU166Tz-1tbX7PMPKvb3wYGyfI41_5lOOUbF4QrJFYci7NdNgHO3E_RFSLg4E_warcNn5qPOnjNa24WLE6qJQF6LJ_NAgz9LkwfOtj-oZrAwTfGtAkInXLSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfIy8GwGq-In3DosbnjdJr0vN15eoxCdrLy7brTQmK-4XzdWG46GS32CtF-TlWj_Dg14Fj4yE7ajO8qZ4EXBd58jDMZSb8ZSqJWS6Yy-QxezXGjZTpEMA8EfgVbirYq_kJ3YaDFBlGMh2pOLYuwvVH1lMApCYRrGVe-JNHbMg_jnfNhFM6_OnCHm1WlccJgJR3HV3LbvUoyf8zDEO7qcfY5Oa-1W24KeKb2L-30hHNT_UEezy2K7wlp2Z3VrGlT1CmGy0y4FQRbFf3EWbxmWw25YExRkDbVa6wzz3Vne7cANTHnAoHhFy1dCwj4FvHBpLfJJlR4uWcB6BmsItup-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wlze_yR-56jeRbFvEb0t7EMragVF0ajZOVWgFRj0MVUfak3Fph38dOl3mCpx1UC6obiWDL9V4mjLChc0HlnBiJjQTTQKjpG0JQHQo05MfAK6l3tpYLQVJIQ3RLN5_uEArEFZoqAVOgoZFq2oumaQa746sa0aA88cUqf4ShT9tWQNZQTFQxQ3xltgDO9DR41dHoFsukUSkLp3tBDDgqDZutzKP_-zzkwJ5A4LseU104rX5a6R38aRU5t4db95Jd_LUe8gB_tc5nMtS1CdT_-H8tq6cEjy1cKc6jafVnTu12DVn-jJOPBpiRTcT-MG8KFEQKbms5JPMr9HsOX-WdfLfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فقط یک فنجان می‌تونه عنوان «نوشیدنی ویژه کافه» رو بگیره... انتخاب تو کدومه؟
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/663778" target="_blank">📅 09:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663777">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUJBR1HToaQVpL0cydA-1Xz4iY44HYrA5uXKeAVh7Vrb2x7Sa56NFH18uzLEfRYL0cOWTFGIC2UYHJaIwivCMLSKb-2EieHiKF1cO_Mj3DTuyoW92cWWqhmFBXXnFVs65fr7PpIb22Nam0yjiXvJudH5q2WEzbMkJjmHfCZmcz8dbt5msByUb_dTT9zTfs9jkr0pskV-OvMt4yWan3OFlfyK2bMnQjQMlcSJKKUasBytdhoQp2oiXO1BEqz5W8LuUTNp7KFrXbDzYr8tVHG6hvNORLfMAAeiuEUHXSinZDl9WmzxzxpYERsmWCGns9u3c0weV7q8rAy78ot4oBY1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای قطعی شدن صعود تیم ایران باید ١ اتفاق از ٣ اتفاق زیر رخ بدهد:
1️⃣
. غنا موفق شود کرواسی را شکست دهد
2️⃣
. ازبکستان موفق شود از کنگو امتیاز بگیرد
3️⃣
. دیدار الجزایر - اتریش مساوی نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/663777" target="_blank">📅 09:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663776">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3b09b240.mp4?token=ZbdKETOdnu-gXgAx3wUPnkRN9TZDvFW77uQsb3bkGzwP-IncRN4kGZxHuMLEAZzLyDdfZ_P8Xw86tWuIqQ10bGRiptHK2FehIXYEybgdDXAfCh6e7vNgn9RLt3BVarfQrwNVytqimIdAACn2Emg-oaaOcvEEEn__AT_o6KgiFWHZwbwJ3Z_-EDK5KkNMWk82U7RK0cQs61ePdP3DD1qdOMPz7YVFNTvT0HKyldKCioDClZIpONo9py_rGyHfl0lR4nP7aO-GueIRuo3OIE5sBUh_a4c4-KRg9VDm9PwtjdDyWsWYC2I9vObTXaeaIKYEDqFlX_Ox1LH1kJWkoldgVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3b09b240.mp4?token=ZbdKETOdnu-gXgAx3wUPnkRN9TZDvFW77uQsb3bkGzwP-IncRN4kGZxHuMLEAZzLyDdfZ_P8Xw86tWuIqQ10bGRiptHK2FehIXYEybgdDXAfCh6e7vNgn9RLt3BVarfQrwNVytqimIdAACn2Emg-oaaOcvEEEn__AT_o6KgiFWHZwbwJ3Z_-EDK5KkNMWk82U7RK0cQs61ePdP3DD1qdOMPz7YVFNTvT0HKyldKCioDClZIpONo9py_rGyHfl0lR4nP7aO-GueIRuo3OIE5sBUh_a4c4-KRg9VDm9PwtjdDyWsWYC2I9vObTXaeaIKYEDqFlX_Ox1LH1kJWkoldgVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین سیکس‌پک؛ قابل اجرا در منزل و باشگاه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/663776" target="_blank">📅 09:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663775">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYMEd1D0f_UkS3WKAMznkkK2827Wtk5ev7UcBu5XK7h_0YLYR0w8nx4hQgYSnkoF9JR6KqYBn0tj6U-yZHSvTnMQRHTf4ph8Bgcm_LlMsRjDZ2CG01rEQPnQJEczSgD-yM7_O5VCqZaH5Jt9bjrYAgMTCbT80RZqfml7NctRtiug5_-xCv5WBTfQ8dxWbCc3xcQ5XFt4jCC3EYwN8O5Qb7iIigyQikRDXL2y3RyBUMvZWpNsV8kfCQO5kLtth81XwE5KiIfK86HFOL-TFS_bcHZqEhcYBstnKIxwRggzbSHGa4dHdBQS9oybw7SruYAzqKSANWnVX65nLMIT_iqIUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۰
💻
آموزش سواد رسانه
|
#آگاهی_رسانه‌ای
| ساعت ۱۲
🥛
معرفی اصطلاحات مختلف
|
#واژه_کاوی
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/663775" target="_blank">📅 09:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663774">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570e6447c3.mp4?token=cmO71BnYmBesiYL4SnyXxZdyQ6uE2yzUm_inB9kAGvHbxIAlGWf4KKU8QVnxiC7VuEctF6BZljYCGq5hYt2TuLXBWvk-a7zT2KgHhhwtvo62-HrpV5Qj1mwGDmunDo8FJ9l7UB4ba-RKRqVbPpD64c_RHdVzgoYsLAosOTGDT4_siEY8fg2TZDhpHIdAj1g0vf2qli6bLBt6BqEM--oRiBS1ZrxufWklVx9IlshwHH8J9R-Diu7UR-21xaAPxW66GxcQEWHgry2fGnYWji3xpwCFYJLwjC6mNDsZx_XYa4o0LL2f7h6GGdZulGElNg9o-h6J5Z7d0-hF45FTKiuj4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570e6447c3.mp4?token=cmO71BnYmBesiYL4SnyXxZdyQ6uE2yzUm_inB9kAGvHbxIAlGWf4KKU8QVnxiC7VuEctF6BZljYCGq5hYt2TuLXBWvk-a7zT2KgHhhwtvo62-HrpV5Qj1mwGDmunDo8FJ9l7UB4ba-RKRqVbPpD64c_RHdVzgoYsLAosOTGDT4_siEY8fg2TZDhpHIdAj1g0vf2qli6bLBt6BqEM--oRiBS1ZrxufWklVx9IlshwHH8J9R-Diu7UR-21xaAPxW66GxcQEWHgry2fGnYWji3xpwCFYJLwjC6mNDsZx_XYa4o0LL2f7h6GGdZulGElNg9o-h6J5Z7d0-hF45FTKiuj4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد تماشاچیان هنگام خروج از ورزشگاه: فلسطین را آزاد کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/663774" target="_blank">📅 09:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663771">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In-z9_XCTE2sw3yQntpBIUqHLxwqhquU3Epk9DucNUCFGA6L9LsY_yU1RieV3FMA48Wk_90d5WIP3p7rlKbkFWMonVBDkJrNljxmgvxL4vhSUChHLwW9Kc3MV00NsI-9imXgdbGcPB_7r6OOYD7ZZKk8Zk0PZT3sfTCR-_upXCxtOtnBCIxRPcWSAZzSISigRxRF5MlPuFOWVB7V0n7LS4LanGfuI3Csb9bu_Lyc5vQbNtDLXCpaEWbrKZDFrtozJtB3zlAJL76HaFGMOOow7LE4WzVh4X3O9kYmQbffGC8bi4djSBUipv-IYrgY8LkaFrjs8fgeYbSTiofQXCbbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">《 اقامت۲۴؛ باتجربه در سفر 》
✈️
🏖
تجربه‌ای از دل سال‌ها همراهی
🏕
بیش از 20 سال تجربه
بیش از یک میلیون نظر مسافران
و پشتیبانی ۲۴ ساعته
پشتوانه سفرهای شماست
رزرو آنلاین هتل، تور و پرواز
همین حالا مقصدت رو انتخاب کن:
👇
www.eghamat24.com
www.eghamat24.com</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/663771" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663770">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21bc126cd.mp4?token=Cj_Pw9Pw-4ypi6iLZ0PXjHguuPjqdAcMN8O-SnvtD1TYvytRmmq95yK_noGDozwuwBR6Pch9U2etAKkY5OWayNQI6VB5hsVulsNJMi5OltY9n963ZFxGScfgzEiwLBVCXqLzxPCG5SEbm-hMLrGD9c314bMlvBDicRbpoctut12i0o_zUp-8nWZoj6VeAnhOZRuuK5EHvy8a9TXdMjTrJbG2psi-mTLqgmPO76NIi7U1m88_NRWfsYhbFr9hHmHhIKvrcVKHruvsNLYHq8t3-9AapZpnji_W2t4Ad1E2MYHZANokmOvz0ai2Hzj9iLw3y-kkLtJn71YZ1j2IFYEJdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21bc126cd.mp4?token=Cj_Pw9Pw-4ypi6iLZ0PXjHguuPjqdAcMN8O-SnvtD1TYvytRmmq95yK_noGDozwuwBR6Pch9U2etAKkY5OWayNQI6VB5hsVulsNJMi5OltY9n963ZFxGScfgzEiwLBVCXqLzxPCG5SEbm-hMLrGD9c314bMlvBDicRbpoctut12i0o_zUp-8nWZoj6VeAnhOZRuuK5EHvy8a9TXdMjTrJbG2psi-mTLqgmPO76NIi7U1m88_NRWfsYhbFr9hHmHhIKvrcVKHruvsNLYHq8t3-9AapZpnji_W2t4Ad1E2MYHZANokmOvz0ai2Hzj9iLw3y-kkLtJn71YZ1j2IFYEJdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل ایران به مصر  آفساید اعلام شد
⬛️
🇮🇷
1️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/663770" target="_blank">📅 09:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663769">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdTgMouohv5cw9N1yoGiOexaP4-Y9KFwFhdCxdOVY_oXvw5sxd5MVOkQf-aEaUhu8_UMi3sY5zaKyQBeHxe_vCWBGeVjkgAWeJK7GQnazSX4smGMhAAUAK4S6t4WLqcc65ppIfRtgB3NPScJ2yEfo6-C69HLY9WKQMTxNfkLKpCfPrKEoQMYiCF8ynSiNws4JHOvkKFsm3MC9k3fJwtZ7cq1QxOnFymQ3Bxz75JcxCw92xmuCvhp8H8DKx18KUomjVZ6FHMZeLCyOFwPn7qELBQ_HycLDhOze4bvQVYkDSKA-tEZLHB9GA63wfo1Jiwy5KuD3cIf4z1ocHXArTi3gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش مهدی حسن، مجری معروف بریتانیایی-آمریکایی به بمباران ایران توسط آمریکا و میزبانی در جام جهانی
🔹
آیا تا به حال جام جهانی ای برگزار شده که تیمی در کشور میزبان بازی کند، درست در همان روزی که کشور میزبان، کشور آن تیم را بمباران می‌کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/663769" target="_blank">📅 08:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663768">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639ab0958c.mp4?token=Lc1TcJf-bSHi8AsJ5dw8IAhiM_5XqqH3Ey2dwiyns4c84dTM8VvpmcJBTSSoActB1GqkVZqPtc74Pv8Q50_gByWNA9AJ7zK5udwf_O1q75E8zRxyj0v0MWODDJPW-gl9RpCcEVWJz5t1ZlHyOeAJFATsLf-_tbdmQS6RW92iB9eB3DiexcDT2tVJDAElqEBb6THpmOtDtSl5Wwew2mKxqeNNic1iTWebKh2pMasIt7TDVA5Rx-grCPvIQR4h4qskGzc8kN7zY1VyB-P93CrRlBeWmANHJxcQHtlD4ow5krWAm4xP2F_qzzs5PWJ2I8Uiqxpi9IzFkORtpeQyw1GpIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639ab0958c.mp4?token=Lc1TcJf-bSHi8AsJ5dw8IAhiM_5XqqH3Ey2dwiyns4c84dTM8VvpmcJBTSSoActB1GqkVZqPtc74Pv8Q50_gByWNA9AJ7zK5udwf_O1q75E8zRxyj0v0MWODDJPW-gl9RpCcEVWJz5t1ZlHyOeAJFATsLf-_tbdmQS6RW92iB9eB3DiexcDT2tVJDAElqEBb6THpmOtDtSl5Wwew2mKxqeNNic1iTWebKh2pMasIt7TDVA5Rx-grCPvIQR4h4qskGzc8kN7zY1VyB-P93CrRlBeWmANHJxcQHtlD4ow5krWAm4xP2F_qzzs5PWJ2I8Uiqxpi9IzFkORtpeQyw1GpIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رامین رضاییان با بغض و گریه: می‌خواستیم مردم کشور رو شاد کنیم ولی بدشانس بودیم/ مردم ایران ما دوست‌تان داریم و فقط می توانم بگویم ببخشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/663768" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663767">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtP4OMFdnjPnBOoycUzYHBPR01NqhAliQx-whnG87lZvs0xyQfLliGH557qB3T6fSELZpM4cUllvzSfB9iiBpS4KB_u8tvu22Dnazk_JEigfqebhpmnPWkomEruIGZ8o2-bb7LJF3VHBHm5RPa4Ults7Mdq2vpaJPhbUWmS-CNAEbv3-_dIkoTbp6jGIOEsT-3vNI9q8h3egPZmAFuZ07yWfSLwyyeDwYCv0t1OarMpei7VOtVd70DySDVl9fPPCo7SUdIeZpOQasPXvC9655TGYt6myI3X94bpUpsX_LfRcnLYStdff65hUOyUj3LBG5LyZ4liimN9-LpYBXxGSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوخی کاربران فضای مجازی: خلاصه بازی واسه کسایی که ندیدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/663767" target="_blank">📅 08:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663766">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ee7eabed3.mp4?token=Nw2sGw3nf9j_002AmR--w8Nt5Vr4lnDYi4ahJ6SftUCacnt4anJqZm_82crsTtTs7rVMis-8y4Ke_XQH5u36_4cm2syccn7356UmFqxXxUuMvuw5Y1UXNVqPFA1Jjv6K1IwqQdKig9wMsuwWd2xtyo16UuNUGwNGPZ_AsoLC8vAqNGQKZDzxJumC2leu3h4PgBk_q_yrTy2lX_7eeQ4b2e57lsRZijRrFamjtBOV78UgQxL86jeAvjUJZHO9L4qgNQopyzYZEC_0E0-Ot8-vk0TEYlQg34Y9IJqIBDJbKQ4QrsffRtSp8AsE1H6_bpIlUvnLyFvftcVnyXcgVZ3Vng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ee7eabed3.mp4?token=Nw2sGw3nf9j_002AmR--w8Nt5Vr4lnDYi4ahJ6SftUCacnt4anJqZm_82crsTtTs7rVMis-8y4Ke_XQH5u36_4cm2syccn7356UmFqxXxUuMvuw5Y1UXNVqPFA1Jjv6K1IwqQdKig9wMsuwWd2xtyo16UuNUGwNGPZ_AsoLC8vAqNGQKZDzxJumC2leu3h4PgBk_q_yrTy2lX_7eeQ4b2e57lsRZijRrFamjtBOV78UgQxL86jeAvjUJZHO9L4qgNQopyzYZEC_0E0-Ot8-vk0TEYlQg34Y9IJqIBDJbKQ4QrsffRtSp8AsE1H6_bpIlUvnLyFvftcVnyXcgVZ3Vng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قلعه‌نویی: همه لذت بردیم؛ حالا نمی‌دونم خدا هم با ما سر ناسازگاری داره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/663766" target="_blank">📅 08:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663765">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ-9CJAyGua6P7IJpaeglr7c63Qyt_wguGly0sQyeBksQAkW_FVeU8Z_irkkc0Zv5cmVw8PQ6o8xK-gQJhy7xhZcZpfdltIzy6sls6xRYtEtxcqc-vUk-QcNdpvXaf0VN_PY4geVGD-iWhmpnQErrLGT9VueHkPfg2fBtianq6JUPWEedFWJOflZyleAhqM1POwO1SFxsKDWmK5ETP2aUinMv1k-_35TtHgGjiQ8D9BdF7H-1s-I8mMkSX1xbY3miIUwdyEbgeHGWZ_j3p1vLeMiGivP-CJTp4dscG7K-tHhUUXE2INFmkxl2jUOUzk9zp4XuJGYIlGc8vkjd32JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری سردار آزمون پس از تساوی ایران و مصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/663765" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663764">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NrM3e34sFzLeaiK11ky7WIcw9MMmreUfyNTZFSbXZzD199LM4nu24a9wKhG5ANM8hFCwlZ3T4qmn_2SBZ_GRgbLWt8lVx0DvmBJneeVwtrc4JkLR2Ej8xg6XpHaZtPbDw6yFe6CEwoAxcVW6s71hMLM38HywF48-ZOFq29e6AtmEqNZ7mFiwVl3aq3b_-U5ly8ctVl39qKtZ3KLT_An9VE4BdWfi2Tor3SIPbKkGa67m2E0Th8QA0o4KQHIgoXBT_lqVY8D_p8rv9Kj-tqJQ5BGXF6U2k2d4ek_R1czuKJMUyltpv299X2ze1N1W1ObTuEF7hce3BHtBMfxfUMa4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی ۲۰۲۶ تا به اینجای مسابقات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/663764" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663763">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq_hpj6FxZYsAp-BTxwlETN-9iQKC8_nBBbJTySORaRXnC1tgGzbfmXIjIcRxL51JNMy0r3jK_JTUS7xmYfzpRxucG3LFzq5LZztN3VpsB6kXPelcRMxYVSvKhgD3VzMzUqHP2pVhTOHsB_NsFI-MomXNuEEUiO3QE0T4xTYEz-3FxB2UfSnNswmWmhne-OAs5SbKCLTAtdrccXblZdAslUVnBKgGqYKFg5ljxedkRb6cwWnMN2IT-UPtUpS-6teW7tK0mccXW0XwbEh-z0bFc5mu2GsXoldE6dQduBQx3t4EmpDac8m5GodhVtcWo6n7s2TNxpAlSI6VFke6tAuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
آتش بس نقض شد  به گزارش خبرنگار صداوسیما در سیریک:
🔹
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
🔹
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
🔹
حدود ۵ ساعت پیش چند شلیک اخطار از…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663763" target="_blank">📅 08:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663762">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwmv9inYih1t8Vefjc2bxPK70dM6Ii9tqBRX6FfdLEW3FrUzJk8OYL3WiWW6-l38HchFqYpPIrKTN1X2adpg8Q_SQMMMIArmpdJfnpGsBcoru9G_nMxUbqtgbuHAo9gtEgZAxCj9V0YWdyJHfTgbOCzB0-bn6PDvc1mC0bPlQ-fDw3s-IcyuUl4uyt-y-hUJUx4aBdp-8mgi7r1oFXeqG30TjEYF6JTM1A8DKVScmUSWtstXtbSQ5haaC4oCKPgEhWTorY08VTHaOWmJC8LgblCEw0cx-cafxi8jgg-7Y08G8p8_hGUPbq7R0P20bCYemeLmxekT1EH75Vg29fp5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول نهایی گروه G جام‌جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/663762" target="_blank">📅 08:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663761">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=n5qHtEK4thDVFegX8eqNT_7kGxjU5ZNWUyVLsYV8bEbPkDvumsXV6wz-Ufqnf1wCAo8uxG-hxOrSOkvYPKVvha3VkI7cFFuagubLSEsWFDVdmivWR3msp0Ua44URpvQubrCbCQuC8ZoSD83MY9SD1A4JnZBE7ia7VLi0onysnzRgwLumN8ujPf1AfF3KQASx4nL3CMVevAwMogE211kIg1CG0WT8G5d1lRcnb0NYtil3xqcIJu1p3LbmpfxIje6t3LYE2k7a3JVrbaB9cXfL_EbOYYoQNfR_EpWXls2157hC_6qsHNj2qyDP4KDxACmCbBrKLFq-fEexMf79L8hfYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=n5qHtEK4thDVFegX8eqNT_7kGxjU5ZNWUyVLsYV8bEbPkDvumsXV6wz-Ufqnf1wCAo8uxG-hxOrSOkvYPKVvha3VkI7cFFuagubLSEsWFDVdmivWR3msp0Ua44URpvQubrCbCQuC8ZoSD83MY9SD1A4JnZBE7ia7VLi0onysnzRgwLumN8ujPf1AfF3KQASx4nL3CMVevAwMogE211kIg1CG0WT8G5d1lRcnb0NYtil3xqcIJu1p3LbmpfxIje6t3LYE2k7a3JVrbaB9cXfL_EbOYYoQNfR_EpWXls2157hC_6qsHNj2qyDP4KDxACmCbBrKLFq-fEexMf79L8hfYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسوس قلعه‌نویی و بازیکنان تیم ملی بعد از پایان بازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/663761" target="_blank">📅 08:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663760">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c672ce05.mp4?token=DL0VDhGaV4N8CnBD6rDS85DvQ0QLwl0yqj--CPSzrg8AlaCj5lOYxoYuHaZczLxESIT56lrVVAVpNNvFH-qY1Dg36X2n_2YvpAHm7Mss5AzM8uPVsoIaMNC1GASsrMTNFd9CkpjBPbcL33x8XbdHmqC_5xP7FuZzup5aKqucrrSsh9cFzAq1M0RTLxs-cawjkOJ7ETB1wjYrTEhiRHqBw5ZLG7SXS7So41SbQZ8Kq8o6p0R4I6rCx4VD1wWz_YlQ1TmbcXDmb_x_ruZ20FMmxi1JVPCH22uvm0vnTHWxhkh00oSSw1HhYy1AQNsMw7DA--hk4aTHWpe6T6I4bykh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c672ce05.mp4?token=DL0VDhGaV4N8CnBD6rDS85DvQ0QLwl0yqj--CPSzrg8AlaCj5lOYxoYuHaZczLxESIT56lrVVAVpNNvFH-qY1Dg36X2n_2YvpAHm7Mss5AzM8uPVsoIaMNC1GASsrMTNFd9CkpjBPbcL33x8XbdHmqC_5xP7FuZzup5aKqucrrSsh9cFzAq1M0RTLxs-cawjkOJ7ETB1wjYrTEhiRHqBw5ZLG7SXS7So41SbQZ8Kq8o6p0R4I6rCx4VD1wWz_YlQ1TmbcXDmb_x_ruZ20FMmxi1JVPCH22uvm0vnTHWxhkh00oSSw1HhYy1AQNsMw7DA--hk4aTHWpe6T6I4bykh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های رامین رضاییان و حسرت از نتیجه بازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/663760" target="_blank">📅 08:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663759">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
برای قطعی شدن صعود تیم ایران باید ١ اتفاق از ٣ اتفاق زیر رخ بدهد:
1️⃣
. غنا موفق شود کرواسی را شکست دهد
2️⃣
. ازبکستان موفق شود از کنگو امتیاز بگیرد
3️⃣
. دیدار الجزایر - اتریش مساوی نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/663759" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663758">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6055a2907.mp4?token=adYzsQyKPYz_Cy3_kB6cM-Is8UQDGKrVWCThCZAuYYgxRI6Ap2Kl7bigJZlmR8IykFmWQXJEUzGqIL-Y97dYJw0Tf4ituA-W-cYX8GcB3IdT5eECNwNbis6kUgfzJZrMi6YM4XAayCQQlb0EalWQOcNTwLaVwzMDe2A21GdEURMoMlJxRngOXSDsJy02qdRPq7YtCLJC0MdzDiQw3EzqY21S7O0upKK6OkYkk8b1DuRRzKnAUmNkNGifhjzxEr6YZtC1z84MK7wj3eCa53ssfGB-2aJtOrX7WaTPd5-ffT4pQs7sXb8JlTzhmS7sng2724jyXDK3OC9zUonstdPeIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6055a2907.mp4?token=adYzsQyKPYz_Cy3_kB6cM-Is8UQDGKrVWCThCZAuYYgxRI6Ap2Kl7bigJZlmR8IykFmWQXJEUzGqIL-Y97dYJw0Tf4ituA-W-cYX8GcB3IdT5eECNwNbis6kUgfzJZrMi6YM4XAayCQQlb0EalWQOcNTwLaVwzMDe2A21GdEURMoMlJxRngOXSDsJy02qdRPq7YtCLJC0MdzDiQw3EzqY21S7O0upKK6OkYkk8b1DuRRzKnAUmNkNGifhjzxEr6YZtC1z84MK7wj3eCa53ssfGB-2aJtOrX7WaTPd5-ffT4pQs7sXb8JlTzhmS7sng2724jyXDK3OC9zUonstdPeIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل ایران به مصر  آفساید اعلام شد
⬛️
🇮🇷
1️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/663758" target="_blank">📅 08:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663757">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایران ۱_۱ مصر</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/663757" target="_blank">📅 08:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663756">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پایان بازی</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/663756" target="_blank">📅 08:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663755">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بازم توپ به تیرک دروازه مصر خورد</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/663755" target="_blank">📅 08:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663754">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گل رد شد</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/663754" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663753">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شجاع خلیل زاده در دقیقه ۳+۹۰ گل دوم رو برای ایران زد</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/663753" target="_blank">📅 08:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663752">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⬛️
⬛️
⬛️
گلللللل دوم برای ایران</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/663752" target="_blank">📅 08:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663751">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fff729c34.mp4?token=AgviIZ3mPeDq137Uj_fn7v22GNVXgRntp2N0_ViJbXXM1bXLFFwCyaUyEfaSdoPL8mJoTJ9dS68nEaITO4MS--zf5Ln5-MPPxTt69R6KNJuJsSm9239p__sHEG6Zt0uqW6QgzyUjD0VgSqe0IPJzYRToKjktFldzMDppCRHNWlpIQsR_e0-PrKuP2jq3d_29ChWNlQhq_hv2X9x2g727yTgrR4aipqR7q-N3DbEK752DlNtgbeZ72CPQEMTt7D_Ekgfy5X2apO3gIklubT0v-PPTQY4Q1biRD6fuq2Bzz2VTVrUfUdWxx3EDxMGl02M9e8M3BaZrAboeiFWNuHtLUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fff729c34.mp4?token=AgviIZ3mPeDq137Uj_fn7v22GNVXgRntp2N0_ViJbXXM1bXLFFwCyaUyEfaSdoPL8mJoTJ9dS68nEaITO4MS--zf5Ln5-MPPxTt69R6KNJuJsSm9239p__sHEG6Zt0uqW6QgzyUjD0VgSqe0IPJzYRToKjktFldzMDppCRHNWlpIQsR_e0-PrKuP2jq3d_29ChWNlQhq_hv2X9x2g727yTgrR4aipqR7q-N3DbEK752DlNtgbeZ72CPQEMTt7D_Ekgfy5X2apO3gIklubT0v-PPTQY4Q1biRD6fuq2Bzz2VTVrUfUdWxx3EDxMGl02M9e8M3BaZrAboeiFWNuHtLUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه سر طارمی با بدشانسی به تیر دروازه خورد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/663751" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663750">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">علیرضا جهانبخش به جای محمد محبی وارد زمین شد</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/663750" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663749">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663749" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663748">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">توپ به تیرک دروازه مصر خورد</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663748" target="_blank">📅 08:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663747">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY54s8g5ZzN9aU5LSp6Dyj4UxpuSkUTT8LFyTslxVpUX9nQn9qu9vyhkkGaMadmsoVRjZ5QwNNThT_VeuuBE3cKIRGWOI0JW21fV0KbXA9NAdqmadp5WIsqF6jkdSyaZr_32icjQyO194kZLtZQ92LByNoLp9THGy5p_RrnpM_GGf2sblpPSMRv18fzy8BiLLwYhihgMk6muE0arOBeOghYlXbieu5QgpDKSi-LQXVO-GYJAczcimyh2uhAwHP8AZdJprClopId91TgCI9uqYYmcoIbpQB2ihNqya36bm1VHqiDoz2tF-2q8tNbMR_EzPobklaK9xtK7jRQlEEG0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ملاقات مهدوی‌کیا و اینفانتینو در حاشیه بازی ایران - مصر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/663747" target="_blank">📅 08:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663746">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کمتر از ۵ دقیقه تا پایان ۹۰ دقیقه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/663746" target="_blank">📅 08:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663745">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گل دوم برای بلژیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663745" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663744">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
مصاحبه مجازی دکتری ۱۴۰۵ دانشگاه آزاد از امروز (۶ تیر) شروع شد.
🔹
زلزله‌ای به قدرت ۵.۴ ریشتر پاکستان را لرزاند.
🔹
نماینده لبنان: اسرائیل به دنبال به راه انداختن جنگ داخلی در لبنان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663744" target="_blank">📅 08:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663743">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a0272b0.mp4?token=kcEADhTkhHeclFHtg8bNb7waouJNlNW2fJVpAmEi_xbF218KR-Z6Ojxqn3ANbF6c-hDpnj-Se4SCjh9V3QquAc4oSwcsZqZsL00FJjK4b6iW7PpOLc8Pr0725pZBh5c1bc94TrO5H76EJurTsryF3tBRbHKLsHQuuCzTOgoPEygUpvGM0pylVvhtWY2REsmmjU1UUTlEIv1RSe1M5xMGlAJZMd5FVxVrN5J_Z6wVvxQzuGrk6F7jRziZG5UobaytimC25NGVhYp900SSk9_zE6aHpMAbAJCmcYBYjFXA7QQZ42LiwypvguTCTsEHjlbi8KJZU4VGiwH1HBPEC6eLLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a0272b0.mp4?token=kcEADhTkhHeclFHtg8bNb7waouJNlNW2fJVpAmEi_xbF218KR-Z6Ojxqn3ANbF6c-hDpnj-Se4SCjh9V3QquAc4oSwcsZqZsL00FJjK4b6iW7PpOLc8Pr0725pZBh5c1bc94TrO5H76EJurTsryF3tBRbHKLsHQuuCzTOgoPEygUpvGM0pylVvhtWY2REsmmjU1UUTlEIv1RSe1M5xMGlAJZMd5FVxVrN5J_Z6wVvxQzuGrk6F7jRziZG5UobaytimC25NGVhYp900SSk9_zE6aHpMAbAJCmcYBYjFXA7QQZ42LiwypvguTCTsEHjlbi8KJZU4VGiwH1HBPEC6eLLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مسئول امدادرسانی سازمان ملل به خبرگزاری فرانسه: بیش از ۵۰ هزار نفر پس از زلزله ونزوئلا مفقود شده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/663743" target="_blank">📅 08:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663742">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔹
در حمله افراد مسلح به ایست بازرسی سبدلو در بانه تعداد شهدا به ۳ نفر رسید و ۵ نفر دیگر مجروح شدند  #اخبار_کردستان در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/663742" target="_blank">📅 08:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663741">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جدول آنلاین با ۳-۰ شدن بلژیک در برابر نیوزیلند
تیم - امتیاز
بلژیک - ۵
مصر - ۵
ایران - ۳
نیوزیلند - ۱
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/663741" target="_blank">📅 08:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663740">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqdY5WNBrDJ0i8RR5_2QESFiCtjA3vhpUlHS_SEU6hqUivvEWjrArQXEjCCNlAYOAY2HCoK0XV0WcHseFW1usqtfr_zgtyhgpqzPd-Aj15BvJiDnOySM28BWLRrsLD9wfmB0fpSURKjK3DuqUegbDajTzEuxU1WZ8n_sqoKTsArfxG-L8j-QnHJunnPAh91ACWovQcyYAOex0uklquQLEp-DXg_zkpZm1u-Q7ZAfOcayOIxhA1wx5deUDSE6S7OQjeGYwZitQW2CyFr28zcmJWw57JeeLm3lyYE8CQvvmzcPsS2utEvzanJlzzqiwE9Sb5rJwsT7lPHOvXDT8O3aOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهار پنالتی مهدی طارمی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/663740" target="_blank">📅 07:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663739">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔹
حمله ضدانقلاب به ایست‌وبازرسی بانه با ۲ شهید و ۵ مجروح
🔹
بر اساس پیگیری‌ها، هر دو شهید از نیروهای انتظامی بوده‌اند. همچنین در میان مجروحان نیز ۵ نفر از نیروهای انتظامی، یک نفر از نیروهای سپاه پاسداران و دو نفر از افراد غیرنظامی حضور دارند./ تسنیم
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/663739" target="_blank">📅 07:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663737">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">محمد صلاح تعویض شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663737" target="_blank">📅 07:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663736">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f873145d.mp4?token=Dwn274XRjxulaKo1xKriOawd9uJks5Hs3i8mWXCY1NWdytdZoeYBARH8s2T8e2hOpc5rHFs_Rd_GqSMO8J08k_TsxRLlw4nuq6ssEJQVi2l5xn3B-GwQfxU4cOXRZtzi7aQQpBi6TgsXTiS6Rl3joZfYmnyM2f7uSSHschAHmif2dlGmqfrcRxkbxD3Wf8GwGxw4ruikHDj1jKQkXd9_kY_xZ73hdqrxKq8vGY49oxv-n36wkbKrmQHInXkYJnMLWDW8QSe6WB9DAMdF9TNy4teYeY-I7ilW0HvLNZj2WpV1hIFCHCMTV4McnFnBoedm5AxJSxn2aupiDBXkApT_yBwWShSQgqJhzyhs1K-WascIbzgR5obieLAJtLHUA9zjduilf51fB9aosDtn86bZ6ts6cZXf6cP2w7mSXLOH26dcxexzT3852x6mB8OTxKxDrlu8ct4ZWVDYJ-uHmFyqgwCUMo2L5JKF60gTJNUqybKZEEfQA8QLdDNQmkNHtTFzEKPXAC1Kkqmeed7MmnZ4bW88ojccXu3-w9TVWROa5GoZ30rU6zRYFYMXqyHaYmNmdN3hdzk8trYffSB8jbpQyvfn-DCgHLAnElYXWTABZfQmuEUdamlbw_qgbNCy2fWfTXSorKU_4IcFggHJT4lPgKvUtoqvUka0VJW12yEa_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f873145d.mp4?token=Dwn274XRjxulaKo1xKriOawd9uJks5Hs3i8mWXCY1NWdytdZoeYBARH8s2T8e2hOpc5rHFs_Rd_GqSMO8J08k_TsxRLlw4nuq6ssEJQVi2l5xn3B-GwQfxU4cOXRZtzi7aQQpBi6TgsXTiS6Rl3joZfYmnyM2f7uSSHschAHmif2dlGmqfrcRxkbxD3Wf8GwGxw4ruikHDj1jKQkXd9_kY_xZ73hdqrxKq8vGY49oxv-n36wkbKrmQHInXkYJnMLWDW8QSe6WB9DAMdF9TNy4teYeY-I7ilW0HvLNZj2WpV1hIFCHCMTV4McnFnBoedm5AxJSxn2aupiDBXkApT_yBwWShSQgqJhzyhs1K-WascIbzgR5obieLAJtLHUA9zjduilf51fB9aosDtn86bZ6ts6cZXf6cP2w7mSXLOH26dcxexzT3852x6mB8OTxKxDrlu8ct4ZWVDYJ-uHmFyqgwCUMo2L5JKF60gTJNUqybKZEEfQA8QLdDNQmkNHtTFzEKPXAC1Kkqmeed7MmnZ4bW88ojccXu3-w9TVWROa5GoZ30rU6zRYFYMXqyHaYmNmdN3hdzk8trYffSB8jbpQyvfn-DCgHLAnElYXWTABZfQmuEUdamlbw_qgbNCy2fWfTXSorKU_4IcFggHJT4lPgKvUtoqvUka0VJW12yEa_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
درگیری فیزیکی شدید در پارلمان گرجستان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663736" target="_blank">📅 07:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663735">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d573238b97.mp4?token=hHW782rcJmvUCZe6mntDO4pT_bvuN70bqR_FxW8Jgn-T8d2rkJdh6FFi86WsP5sFOefLSZoU2VyhTCiz-JHOWXreOdNAW1D7z74SWbj8JUkb9l3JvzB95T58_RSW2f3yyV83M1tQ2N3WpuIqrSlG0m2IXSCNAbfr06_fNc3yhFZReLwNCFsJQ2sAzryQM3k2YQmoLqUVaMvVJ0cFUGsPYwv49W2tuxCUecyMmA_SgiPjrJZqoLMvhB0Ccwwg5OimiSQG-eq0qQU62_W1Fyerlg8iHy72fRgu9aeV8VF76tByrF78dwx5O9xBl8LTiSZ1P2Eu8UM0WY2jXOhu5Qs_9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d573238b97.mp4?token=hHW782rcJmvUCZe6mntDO4pT_bvuN70bqR_FxW8Jgn-T8d2rkJdh6FFi86WsP5sFOefLSZoU2VyhTCiz-JHOWXreOdNAW1D7z74SWbj8JUkb9l3JvzB95T58_RSW2f3yyV83M1tQ2N3WpuIqrSlG0m2IXSCNAbfr06_fNc3yhFZReLwNCFsJQ2sAzryQM3k2YQmoLqUVaMvVJ0cFUGsPYwv49W2tuxCUecyMmA_SgiPjrJZqoLMvhB0Ccwwg5OimiSQG-eq0qQU62_W1Fyerlg8iHy72fRgu9aeV8VF76tByrF78dwx5O9xBl8LTiSZ1P2Eu8UM0WY2jXOhu5Qs_9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون؛ تحریریه خبرفوری در حال تماشای بازی ایران و مصر
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/663735" target="_blank">📅 07:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663734">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بلژیک در بازی همزمان دروازه نیوزیلند رو باز کرد</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663734" target="_blank">📅 07:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663733">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSH6d2JfxT9y8pt723X1ZhXCQehyKbutrlgilsZb4mG01Ko1jPzKwApRVYy0Y9Hk6-MsDXPKhnrDFhNTPNeRrl3GYtTSSu9zZdqI0i1ksOlcyDB8C8ycK4WE-EOKrZOUsGh0JSloq38U_iXeBxZEwRml82FTNm0-IyEaiPjTbA6Hvd4eoApYnI9VusmlMOUsDyWnK43VM6Bft-wyFIqumFaFLXx9R6WisMPv8r827bMThclwj3O2sS1ORURIW4zZn60byTohTQP_ea0-rKJZTpZqros7s0CWKGCFuH1_ZYKko-mEyZMDEG8FJxX_YqN-jJzfAwU77ZIZbJ5Wiq8G3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدول بهترین تیم‌های سوم گروهی تا این لحظه
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663733" target="_blank">📅 07:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663732">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhFJJBwtEe5c6esvy_s9lGTJwNOueF8Z59GT4yfy6xBMF-uyr5NaYxtmeK9Obbn3ScOjIuVW23sSzBMpdk8FRtxCqnhw14m3UdOJNAbOdjHJrUe31w58GXod3QoNXRdu03rk3K_g5DC_bJ6_EIVFvcQ3XNIzl1irXzkL2cW0xameOz-KYBCdp7Z1QkxYShx7_u8hWWFKW87eWuSMEWrSSAtmRm3mb5VAugwk1KYyuGpLGHWRmVyt00limtqskFrqgYMaLEHp2olm5iOw5BT98tJ9ynA5mxVw36bnOuynp7AiP587QsW__4mao4PRHQOtLlUnp-c2ChEjOEjgex8YVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمرات بازیکنان ایران در پایان نیمه اول</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663732" target="_blank">📅 07:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663730">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bunIR_gFQnKdRRJi0FtnXCAUOSq60n7D3E-shIdTSG18A-PVtXfBfRu3qs5hABX9OhKsG73tADc65EePwVdcI5qV0DGqC40TYrShL6oq2K_NN9N3atiG8vusoNU9bBf2pVKjufpRYzkyacFf7iS3_a-nU55_JCfRRbdNVjmt5-ZJcGDgpm_EQNWxDTdJhggCwCW3hlmgpGSLLo7TnejwvYkFD4FAdt1Jsqo4SgOedFtkrSge4QfDWbL3nwd-U4JBYgD3wNQ5sV4S34TF14Y-JY76mfpnWimVIVAbCL6Tv2tFlixRN7Wa_8PMrS1pCSA87wW6exF-6ReivOX7Fc_iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYyXQZBw3jl8r-hihQvS-HJgPXAjAJh0HM6We7wkpiHj2a6x9IdVzucyp_5O-5Gmaty3LAoeBH8d5nJvZ-FSgGjvHrS1fA-7iosc3lB6-GYOV8STuBPhGX5aW11IXctN-uYe6te2mdXhPWq1ZVfH1OLM_Dy6U0ql2iguKA37t89YlHfLMwR1NKRJgx1jAHhinMoRcuZvUZ8802a4bRq5vG6pJCEKEC5Ze0pd8Z9RYUP12dZEBXIh_n22wMaUv22-TwBb1gehhz-huLNG4nQLtVCLVEDTnkJecDIziSh-SKbl8KBBCcG8o3goBVwX8KC4l6MkIa7pekrdEzesntNu9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شوخی کاربران فضای مجازی: گفتم این سرمربی مصرو یه جا دیدما @AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663730" target="_blank">📅 07:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663729">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شوخی کاربران فضای مجازی  لیلی و مجنون ۱ یوسف و زلیخا ۱  تنگه هرمز ۱ رود نیل ۱</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663729" target="_blank">📅 07:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663727">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2v-JZJerZiQLVcBPRPwSvgUUUgGQDx8vvZt69NBql49cJlGMS75lSZ0dVafTdQDgfD2_OH0NFo84dUExBcfvq7yxqaq0kO3K7X5lDtFvpewNsh2G8Fq1vWsjPGQ247qa7gQDzk94zDAVSQhFznepDlbkGax8cPP8Ym5GegPTwVz2QbvIMFkhT6s-Vl_bwL8bU3CMRV-5cTTz_UjMOw2F3Sva6dLML2CYTmBj5YWRYMyJoeTPswA45zo_dLSOOtYrwj7pPeb1_gkJuyJno35GMNl3fE3IP_ndTjcIOduzEV0iNI9o22_cKqXrIgG2f-ZMSqeNDy5SGbI6NKY32hQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_DBiovfiYhIBjb0_BDXCG5lA6SLC68_qp33NKFAIpNOUU-4e1koQzR_d-J5didnf26MtwvIpl99eBZR8hY3nIm8IA6vjQEQ4nK0mcZ1h8HzD50-Ktboiti3RU8-kuDQDqnZIKgoCvzdLZ2zavgvpvJkyi1RJDrXg2jho-AePLbg08A5--P_xR_YvZAQzLfpZiyf8HDWv2kP1BI8aPQ5XuJR9PWQIIu5CWp62EeCjGzgCOMjUkmUTr0UClgan0Ub3yXfQ1jsWtzMlEZVK5BoQXaDqKWkhG_o4Nq4g5rKJZcqCYkV0qFJvdsUM7q31JqR8Wf4SZiDvMvDu_ziQNUvjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مربی مصر شبیه کاهن‌های معبد در سریال یوسف پیامبر هست @AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663727" target="_blank">📅 07:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663726">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS3CZSlq7mmrfpb16Z2Dj469Ziq7iyOJ2WQ4AmQYkTHdHneVz-l9nSaHUxv9K3QSkVPwPNoAfmqClzY0tdm6QRrYZ0GrqHX2eoAftYUL-xN4Atsh04YQYh-70pqf7oiQHuWU8ImqQPczSawc5BymWb8pdYavaGcbRS_CsH-g5qiO7dKClUZ8nLdNB4-oxY8eKnAjyi9lLei3PFn-PRka0_tIkNTIThIYe60k5fZt-_0a11qe59j1etMHMimsATN-rwpiISvCwMwW8a9lUDGnI7a9NbpGpPbY2V5Z9cdkv4Z6sCiTLoK5ybWC92LhXxuD7ewmi1DdXScHs4x2Us-lVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی کاربران فضای مجازی: الان تو زمین بگی محمد‌ حداقل بیست نفر تو زمین و ده هزارنفر نفر تو تماشاچی‌ها برمیگردن‌ میگن جانم داداش؟
😁
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663726" target="_blank">📅 07:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663725">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تنگه هرمز ۱  کانال سوئز ۱</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663725" target="_blank">📅 07:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663724">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvnjYyK4TNi18ErMhMbzwMNdoVBnnRG4J10PB8em-ea7fNZqRAzV9lbJKmpL0b090L0VKmsifx5q_qZJniriJKJXzSXuatC9pRO-TOeXdl8NXnp9SEyl1itgDo3ir2gnjNAPYJaSyF4mnrJwbg9Yb_EJLsxq3bqdBubwEQnXGf4aB3RLf39zr2JyvM5QW0hk6v4bJNYwdjCmLR-rgFMy6CaehbHyP1SKxaz9MCIPq_7K8D0zPN6KskL8RZjazWHuLb5N4A09cTFzoN4t0nvZM4WCQI5F4MwaAYy5n7WKvILieyr2fdAdeqfLYFTLeSJhc5ds9kLiDtTQhMMYI21E8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی مصر شبیه کاهن‌های معبد در سریال یوسف پیامبر هست
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/663724" target="_blank">📅 07:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663722">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nkayP5kX7BP2cadCgB1AQn1TLzPowmhQGtZlvbb6eIl6ZaMk19tr-P6Mnx3uuhBReD-gIacwipdR64QNWtePE6QGpqyvgjb41sA0U2qvo14b3aBwG6e7V2tzwS_AaVcMak2OMkMyd_BHGZ6_vdspABdJ_KhRb3t9zdr0OYakz_NCJMZuPP81VY3AsblpJy11rr9pBMVuqahAusfNSZ3ZvzPk6BLxZDGln3b3hfsAc6NMyyIQY-O2_qytaYbDNu1fmGcszgehIFlvfY-Rf97_jaBFfmhLFXwPx66ZaedUG4XINZ6gyULrr3kYd5Bmhqhu1j8SCMN3TRMQsi__KhjQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CfOwe1BHYZjCpJWIZ-cdm5-hOjyOAfkLmT9xCL0YM3-AElkQU1VjnRjVCeq_YDB9uv44DyjxKxWpaDr1bYiSKq97Ca3aZn920S9pnWUcOEJJpKmcpZ8ru5uGjuLYi1XQB7mkO4x3YQFlNAC4miP_inywylfHgDP9jsGFwiDLNK9LBlha09ni-SHEPY_iVfHAW88tFM0bPReK4f5pMx8fd0A-RMByDzwrK9wrGsHAVEIcz-bT8CsjiKvU_alITSmUbP9EMuV89NExT2i9h1l7KfwAFo_273JbpKp17KI_sHXesoTFQgVETVVUaqAwEc1uCBjSmSyagk57mdE7NdylhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نام ایران و میناب دیگه به هم گره خورده؛ هرجا ایران هست نام میناب هم هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663722" target="_blank">📅 07:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663721">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست‌ کافئین | فصل‌‌دو،قسمت‌پنج - کریم خان زند</div>
  <div class="tg-doc-extra">کریم خان زند</div>
</div>
<a href="https://t.me/akhbarefori/663721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
🔹
کریم‌خان زند (وکیلِ مردم)
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «برندینگ معکوس»، «مدیریتِ ریسکِ آینده» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663721" target="_blank">📅 07:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663720">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تنگه هرمز ۱
کانال سوئز ۱</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663720" target="_blank">📅 07:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663719">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/005cc4418b.mp4?token=Q6RyMwwMsudTn40yoirLvMkHIsHDQwFfMnmcnCdq9z9F69bYHQOR0y-pRlzi-vtn-Y4PUVECK0auGhOrlMIotny-rv1N22LllfBymOtprZMv5_SaQMLkKzU9tav6PUKuq0UgKJmFB3MqBoZwaDFwWKcQ9SbeJeIDH8qecKmvzusdBr5VAjM4zmj5VACHOugBDwW_gGZA7TtqkKX50BRT3BQgBRdOJm39QiWkasD0ebLfUDEiMamJfEuDG0fM5Hbs_qoImBnoALcsDmn-x36IORNKyL-VnK0ktccPrLUBgGQsX5QK72zf38ykRdYMoGEgws0xdkOIPR00bfsBuc2MAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/005cc4418b.mp4?token=Q6RyMwwMsudTn40yoirLvMkHIsHDQwFfMnmcnCdq9z9F69bYHQOR0y-pRlzi-vtn-Y4PUVECK0auGhOrlMIotny-rv1N22LllfBymOtprZMv5_SaQMLkKzU9tav6PUKuq0UgKJmFB3MqBoZwaDFwWKcQ9SbeJeIDH8qecKmvzusdBr5VAjM4zmj5VACHOugBDwW_gGZA7TtqkKX50BRT3BQgBRdOJm39QiWkasD0ebLfUDEiMamJfEuDG0fM5Hbs_qoImBnoALcsDmn-x36IORNKyL-VnK0ktccPrLUBgGQsX5QK72zf38ykRdYMoGEgws0xdkOIPR00bfsBuc2MAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کریم‌خان زند | پادشاهی بدون تاج
#پادکست_کافئین
| فصل‌دو،قسمت‌پنج
☕️
🔹
رهبری که در عصرِ اشباعِ ادعاها و دیکتاتورهایِ خون‌ریز، تاجِ شاهی را کنار گذاشت، روی فرشِ کهنه نشست و نامِ خودش را گذاشت «وکیلِ مردم».
🔹
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtube.com/@caffeinepodcast2025?si=V1RxgFPUSLD6Meam
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663719" target="_blank">📅 07:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663718">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0cJgl-jo8NlS9BlgtNIs0uBCbj3Gf1c_uQL3wxLzgug62zEHQjkMRGWwXm3NvogN-gbIyyskjjsv8qMJOKWKnCXPgPVPD25yiJnWdYJ_Vj2cBAP60AqqWkBBn0bTksOqvfmrOBMuA6jrvces0a12Gtuw5BNr5WIOp11AV_ncXUcfPEWFUUO32gbMLORPwNpVlKdOV3TG1ZPnfiuSmXSj3LbxFi4KVXGpxgIOQTwg-8iDfMuOOkQccGFj8ej18saJ2WkT4hSzNJLf4S0C_5dQZD_yL3zbE9oJeaP_WN09eWLe_7Na_jewtLngzHfDZynFMpALhc7PPKxcx1M3q_ljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان نیمه اول بازی ایران و مصر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/663718" target="_blank">📅 07:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663717">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629bdd3c3b.mp4?token=VmWxAQpeYZ3hAnGFdHVc-Gj7KM4hZ3KBduXj-tdS4qrO3XPyrJlVjHJ-KIHGZClgprvE-i5sxKwFHwr7DOHWngkQie_PozZnW5EPgFuHBgX-Y_yagi2unQeYIMF9ZpaexNhL5aGI5k71XMdaeY9dZ6QdYE0c_PPEdlSAs_g9-yL6wj-MPXK2dxHLlNs-JET2doyWYzYLYa1Fq0o4QKx9yoGKV8FVlinKaA1p6QwA5tDCgdbysyX0EqpZ48pcn55eq6t-PShgIE5jLNWccKBQODjxJqUPep0OkBGkQ2cJuWWTXVL3wy6n1LvEFTcYDTR_5Aw62Ro01jYrshWFLmGbcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629bdd3c3b.mp4?token=VmWxAQpeYZ3hAnGFdHVc-Gj7KM4hZ3KBduXj-tdS4qrO3XPyrJlVjHJ-KIHGZClgprvE-i5sxKwFHwr7DOHWngkQie_PozZnW5EPgFuHBgX-Y_yagi2unQeYIMF9ZpaexNhL5aGI5k71XMdaeY9dZ6QdYE0c_PPEdlSAs_g9-yL6wj-MPXK2dxHLlNs-JET2doyWYzYLYa1Fq0o4QKx9yoGKV8FVlinKaA1p6QwA5tDCgdbysyX0EqpZ48pcn55eq6t-PShgIE5jLNWccKBQODjxJqUPep0OkBGkQ2cJuWWTXVL3wy6n1LvEFTcYDTR_5Aw62Ro01jYrshWFLmGbcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موقعیت خوب گلزنی برای ایران/ شجاع خلیل زاده با ضربه سر توپ را به بیرون زد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663717" target="_blank">📅 07:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663714">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZ2ePskx41U-6MV49WDbR2w20fidlHDVFDw_JcjunFCoMTMXzseNbVy1iage0BEp2MYTeKtLaXQO447EMj5JWBPFB43HNaly9WqIy1rjsE3iFyvLqXUPAVeLtxEdWfk4d0pf0l3dK7C7kcit29MKBaS7Corr5c5oiwvZeAMWSW2yPEzF2DVxibmB_CFEUMbQ3u5zssb3nDim_Cfo3sOPcMQ_NtjuzTY-qvE3oOQvGSa-6h1nQuYAmC6MFZSljk1YQjN8yMEoXMYxsx8jBPLIH6E_NjwX7hlN7d1yr_rYkDRhYITk9UYvOs2GTK8GxWC09aZvsAwe9VeDrXTQ3-iMOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxwUVYLhsASpvkS3RqrB-WLLT_RQkdP6bGDNa6wnhnG4vmgky1k10jG8D7pHj5-oTmL0dx16trMlpDbho3KoJ525tFHcTZOaBbQvDz6U-2yMjQ06hPV0wQCH2UWyB9pmrSpCZEnMP2rLfwHSVgmab50XvN1E5aWprPWchoC5LMg11IoaJY1ko9Bs5qLk18Cs3Nv9P1d5JT0GfqnIsTNgMMFc0-G8FiPAPu43tBJ6z4qkILNCmqdkXUwdnL3gFiB2RQYgWpQeYBRDNyLzRU2HP2513etVCJFa8sDJDCQfVIa6BMEwE12MAY00QlRdyrlAzKP7ARVklRt6WghIgYpg7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58129d3d5b.mp4?token=Hb1ZqAxZ2Lt0OoEypCvq5jSMNFtU_vLLmYurHjRg4H9YW-ke8VT2u7ANq5pTMUkHaMD_QLzoUdHw7aEeqCFJJeuUjMvYtfRZLfcG2kJ_Iw4UsRnZ_t0UqTtDx1EUTx0GEEBcT4uJMy3abxVrJlN574hNS5ixZZLkP_R-F6SeHBRGY5OrQf6Sko1C-1Etkc5FP4ygxh31BLIjVTczW00W2e5anBsgF5lykaPWMlyTeDKHY_9bFwwipxVoChBJOcHo28mOveOuPmBtK-7W5wVCnpoyUvzSh1Vi8HMVYSb4jnLDt5Kz1o7r5QvlEltK5-D3fuQlY23_6gkG2xZJMMJskg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58129d3d5b.mp4?token=Hb1ZqAxZ2Lt0OoEypCvq5jSMNFtU_vLLmYurHjRg4H9YW-ke8VT2u7ANq5pTMUkHaMD_QLzoUdHw7aEeqCFJJeuUjMvYtfRZLfcG2kJ_Iw4UsRnZ_t0UqTtDx1EUTx0GEEBcT4uJMy3abxVrJlN574hNS5ixZZLkP_R-F6SeHBRGY5OrQf6Sko1C-1Etkc5FP4ygxh31BLIjVTczW00W2e5anBsgF5lykaPWMlyTeDKHY_9bFwwipxVoChBJOcHo28mOveOuPmBtK-7W5wVCnpoyUvzSh1Vi8HMVYSb4jnLDt5Kz1o7r5QvlEltK5-D3fuQlY23_6gkG2xZJMMJskg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشته‌ شدن پرچم فلسطین در سیاتل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663714" target="_blank">📅 07:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663711">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بلژیک در بازی همزمان دروازه نیوزیلند رو باز کرد</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/663711" target="_blank">📅 07:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663710">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
رامین رضاییان با ۳ گل از مهدی طارمی گذشت و به بهترین گلزن ایران در ادوار جام جهانی تبدیل شد
🔹
۲۰۲۲ | برابر ولز
🔹
۲۰۲۶ | برابر نیوزلند
🔹
۲۰۲۶ | برابر مصر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/663710" target="_blank">📅 06:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663707">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPmvTyBbvGnsut5w4nLlgGe9_rx4fMoM650uof_SwDdI-6Nqh7a31mM-5mdyfaRXwqF9IwpjPl00eMegjfgckTADXd6Q5LKSGKpaSX4-U_XD0qCqUId67E0rb2So9mzujdmuP4pSF62yDBmx6HVO2bxqd8YO3iZ_EEjewMOkKKjwHetTU-oz2XWD137YWUvKZVJLk2mIpv1Rd6FclLngwaXMyCGgchttf_VRkgQtSbMy1TsjrZFeJW6hGPBKL86A-CPzlyIUGq-Est6j9JR3xoSS3iqQtN0VhRnI3qOLLoAOyyl3IIvZ-zRY_I4vIL4q5koM1ThwnX0AYL0rkj8NJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohsZmnMF7A1S9bdIrxOwFKJ9CWL6RSSqEoqGB9Ef5a98oKHtzdbdJNs-yGlssW9WzVzktFhWpOdN6Hqy-CnnGQ7f5r1B6d1SHeOKTjr_A0sYDVOVI7fJhVT-cfq0ajyLD5EG0ts1vt1_VqmMLBZpzFw1VrfXJkWuEjJmImrrJQgIv1XmOhZSjf_VPctkpO1RfdMS3BencwugQ_4dSd3xU-jXv3nsFSqD_Ba1UmAKyBPHRC8B4BBJKPFQkcoxPw0CCmv_kxsr3sy0-67OKGEa38p7ACNGR2y_0Mrftgkq4y2UJAucoyKShMTDLZvELGOxoHeOGekE2YgcuFwTXrC_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzf-shm5imoTCk1SzA2gZBxCQt2iGc0a7IeQtbCWo_CAJg5XHcAMHWmX0wbL7YawHhOP9OUFV4aSEJKJ3nMenT7-kuMnwMgqKJbd3m_inH6GXVnwWpYiWOktyC2_vmWWUWXBA6P4jVMF46_SNdgOnvfu8jRIZ6KeVhpZsigYwkwKis-b-XTRsLYI12HmKrRpSvVCgSDF5P0V577X30fYeExmv5-d7fuUlQZPkv8pa79x36UU2wySId6iXk0rXeCG6_oXasCvfq-pOq17sgFWVQvYCi75UplJJSAsj8XLPr8qrbjgXpk5rDeC042qliKPscvMjP2XkzimsBSYQXy6vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
پرچم یا زینب در ورزشگاه سیاتل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663707" target="_blank">📅 06:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663706">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگه بازی بلژیک و نیوزیلند ۰-۰ بشه و ایران هم مساوی کنه، ایران بدلیل تفاضل گل بهتر به عنوان تیم دوم گروه صعود می‌کنه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/663706" target="_blank">📅 06:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663705">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4871ef92e.mp4?token=spSuiTLFIugLuabKtz66m4TXDglsQHDBlVoG9Zry_zv2e-XXQUdYs7fenGAwF7_FSi9tRnINNYGwthBPGgvvcOAEJN2UC5mgRItr0NMEErKk-BviVLG4I04WkH78MdXgBLFG_Nq5PWl2kFtnMMzMKzZeEdzS8afS7b7SY-0fhdcjnBI4IeZBEySJoW5nKRYM_sqpH_NesVZ2WYkdxMeTs4IV7-KopJ8B9Ah9J69-ugXKCxG3AnyUyljsbjWbyYc7rm8e4Sqdnh7naR6WYnBpNUAkLozLMoxGKYhQtoiP-xfzrVbcatysz660ItjUoa_hBB-MPJo9V9pt6hKqlYK8MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4871ef92e.mp4?token=spSuiTLFIugLuabKtz66m4TXDglsQHDBlVoG9Zry_zv2e-XXQUdYs7fenGAwF7_FSi9tRnINNYGwthBPGgvvcOAEJN2UC5mgRItr0NMEErKk-BviVLG4I04WkH78MdXgBLFG_Nq5PWl2kFtnMMzMKzZeEdzS8afS7b7SY-0fhdcjnBI4IeZBEySJoW5nKRYM_sqpH_NesVZ2WYkdxMeTs4IV7-KopJ8B9Ah9J69-ugXKCxG3AnyUyljsbjWbyYc7rm8e4Sqdnh7naR6WYnBpNUAkLozLMoxGKYhQtoiP-xfzrVbcatysz660ItjUoa_hBB-MPJo9V9pt6hKqlYK8MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول ایران به مصر توسط رامین رضاییان ۱۴
⬛️
🇮🇷
1️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/663705" target="_blank">📅 06:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663703">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCLzgzTZR3Rid2SVChQvh8U4KypmECC13w3D8QHDrN2-M9Iwr6-Wek6iH1ICoxslN55ET7a8b1w84cSp97owJConHpC2EBLSqIhMofY2CDfk7oh5i4qyN-NQiEpToWVkI1AvHXE_lnPQXZTpP86os2uuJBsUYytlnvQ_yBOFZdvk6Wl8Wdd1To9XVcOKChnn74W6t4iaHZAoQL72MiGlxmD5CoAXInZ4E2iNb7RyPNWOvQlrJXsO4yPy2gv8C-LS3cr9FTConDVu7URGfwvP3atSgox7zwkHTYWZXIIh3TqB9jTsqC5t3SV31wlCGAClMBOfensNZv_ybYfhF7V9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/euEhH7OXcL6dzhf_ghPiF7xKE1h4VDCYYvZ5QnzLCAE0WRIPs5Yg_XpCXK7njl-Biwoicy20wRuiEQByLKHPKeaQGfBXVuGbETTYDaftypGuNlBPdh-zjyb4TZB71LLn24Y58X82SQ71OAZmgijDdjvKCe8XjJXqE1Wy1s1KhBwbc8pxdBbSJD_emrLIJArQviavRwPvYCHQv8za4luBvxHaRqQFYyHWscTF2yDYC2QAwHz5SGGXJ3cRMGN0B-157uQhJnsu1eB2SrxEQZBz_KNb4AJvyM7a7gCxtY3s57qzbS11Xac9Z2dGGaz_i2-vZpr-j6agD9CNUJMRuUUv3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رامین از این زاویه بسته دروازه مصر را باز کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663703" target="_blank">📅 06:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663702">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHN7CpE0oJUkXgPVud8L9Hpyt65CM-OIvXu8m_qyzvYy4XBupeaIpsns_AlStZJT2uEBB9PGSD0biNMFmcGHnbhNA32SozUPFcZ9hZHDLgSpvRMNTmpDyGrCCEixjGYJi0j2Q7Plm97lyh6Dx7O40Tm_XCdGvweYXm42x5HFnHaoIunL2s6duJU-89WzfTTFIgehoLxRiYe6zSOHn05AhXpDR21fviNsKIn73otSzdyn9zSRkBqV1kGUY8cw1J43ORnLeJZbgvkF4h92BQetiZ5xgn1VlX54-KodRPM28YBwJCuA9NX2NomzJEq9PRtgZIZRvNvzaucBeq6qoK37tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
میهمانان ویژه تماشای بازی؛ رئیس فیفا و مهدوی کیا دیده می شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/663702" target="_blank">📅 06:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663701">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f74126bb.mp4?token=r6p2K50b2n5FF_ozTOd_v3JLiWVFrHdqEpzIpal4a9w7ytyaHWms_pzj8sShLpL3LcPZAdo3TmCoP4sGqcVckfycbp4tEs-gdyni9KzqVi_cPGkJ7VU7daB2fWVbJB10agVqX3blSxy0cnoJXg0VzEzyufjoVR7X8U7C35ZDMhmm9O2jQp38yUC9dnk7_emQqLxmK-4HZMJvQz_zr-FuLtiogM92ZyK8ZnyDpNHEBIQ7DW9yxdk8WBspvuPH0rJZth9RAC8wFs7Ipr6t3yqY_-ZCA57_L38l53DwTNw-bt1uHCJA0oW8XTQyRYYvqRClIhEAIwXYE6TtFvTN12ldozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f74126bb.mp4?token=r6p2K50b2n5FF_ozTOd_v3JLiWVFrHdqEpzIpal4a9w7ytyaHWms_pzj8sShLpL3LcPZAdo3TmCoP4sGqcVckfycbp4tEs-gdyni9KzqVi_cPGkJ7VU7daB2fWVbJB10agVqX3blSxy0cnoJXg0VzEzyufjoVR7X8U7C35ZDMhmm9O2jQp38yUC9dnk7_emQqLxmK-4HZMJvQz_zr-FuLtiogM92ZyK8ZnyDpNHEBIQ7DW9yxdk8WBspvuPH0rJZth9RAC8wFs7Ipr6t3yqY_-ZCA57_L38l53DwTNw-bt1uHCJA0oW8XTQyRYYvqRClIhEAIwXYE6TtFvTN12ldozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول ایران به مصر توسط رامین رضاییان ۱
۴
⬛️
🇮🇷
1️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/663701" target="_blank">📅 06:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663700">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سومین گل رامین رضاییان در ادوار جام جهانی</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663700" target="_blank">📅 06:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663699">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گل تساوی ایران به مصر توسط رامین رضاییان</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663699" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663698">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhH7KVHtC_rDL7L1YFf8OXoYyN4vA36ZIyACBTNPPqIr626m-Px_SVr763VI-b-rli51hF4HnlWuPrX97g0LRq9q-SuWjHcnjj1Y9HFAhHS5COPmy5AfYgCfFycXIbsRLYLZqfngSDT_uhmEa5PsDKdURo7Y5IOC9utu_1rCZwnlbHBsOhz6lyHUfkaeuJRTZTWqUVY8rKDhOUrT54-HZ0J0ZuuTQy-gy51QNSG2Am_96Lq-sP_b9Dji7RY2E40cVKv58aye8DY4xOKXnNu_JB5Jn7cPRBO2aLHpufQsZyTcT6pFVo7Hq0cE_2bVnPmr-9Ny-rkyt6rErmStE0wrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه نویی بعد از گل نشدن پنالتی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/663698" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663697">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc87848fcb.mp4?token=Yb4I7OaHM3eep9m0DOKJqvLpCvRX1Y0-WJWgukFMtwWFbwhR-YyqUUz7HesTsJPwPBg7ZC_p6w7h9Xmm47ZT7GJ9wMn2acZlXxn6TnmptEjq4xJe_YI_Fm7jo0eVroy9lkIPwTZ9lyJMcEj3SYLUCmCYDVUvKLbRXsFGwa0rys7SaoF4rl6L7xBJVasVkdONjGJdyp7k4Q8QOG_WlqpQYdxDywcDmixWn5CShe9yGzdVXMSIrjOnUxrR9o8r_pD3PXsYwh3xxLCIJN8ivAWWP6ljtWKlGg5VmLFhpk5gOPjOzteeSHBe6487_smx_ae0gODKa-rAcS8E1NRzt5OetQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc87848fcb.mp4?token=Yb4I7OaHM3eep9m0DOKJqvLpCvRX1Y0-WJWgukFMtwWFbwhR-YyqUUz7HesTsJPwPBg7ZC_p6w7h9Xmm47ZT7GJ9wMn2acZlXxn6TnmptEjq4xJe_YI_Fm7jo0eVroy9lkIPwTZ9lyJMcEj3SYLUCmCYDVUvKLbRXsFGwa0rys7SaoF4rl6L7xBJVasVkdONjGJdyp7k4Q8QOG_WlqpQYdxDywcDmixWn5CShe9yGzdVXMSIrjOnUxrR9o8r_pD3PXsYwh3xxLCIJN8ivAWWP6ljtWKlGg5VmLFhpk5gOPjOzteeSHBe6487_smx_ae0gODKa-rAcS8E1NRzt5OetQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهار پنالتی مهدی طارمی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/663697" target="_blank">📅 06:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663696">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مهدی طارمی در دقیقه یازدهم پنالتی را از دست داد</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/663696" target="_blank">📅 06:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663695">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52d0c55578.mp4?token=EVzZ2SLM2vvk6L8lFM_wYaw0y4zg97DAdUCtNqmbudW476wNk36rxx92JfGipV_LF-1ae0dzXg1ZYJZ8OjSAeX62J3SZDgwihnrtAMW64EDMcMkJklE-L0fgKUJzZXrEIK-aIHtOyzeFtpDwsSAeZA5-IEvMFXqdE23j75CJOM1QhPxq_uXKq6b-9lT3v05aYsuZxDxqPTYEVQC-g9fQn8J-K3CO2AhLJoHlq8XASMW8RRS7YcfN3AEng4X1ORKr0trqG53OkIc4HY5ymVg5iu3gfO80fcq6Bh_1MdrtYYfB63NKGzXGsbs2ySFLnCZBmhxpq3wmJQmRzXJ8PgXTfIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52d0c55578.mp4?token=EVzZ2SLM2vvk6L8lFM_wYaw0y4zg97DAdUCtNqmbudW476wNk36rxx92JfGipV_LF-1ae0dzXg1ZYJZ8OjSAeX62J3SZDgwihnrtAMW64EDMcMkJklE-L0fgKUJzZXrEIK-aIHtOyzeFtpDwsSAeZA5-IEvMFXqdE23j75CJOM1QhPxq_uXKq6b-9lT3v05aYsuZxDxqPTYEVQC-g9fQn8J-K3CO2AhLJoHlq8XASMW8RRS7YcfN3AEng4X1ORKr0trqG53OkIc4HY5ymVg5iu3gfO80fcq6Bh_1MdrtYYfB63NKGzXGsbs2ySFLnCZBmhxpq3wmJQmRzXJ8PgXTfIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول مصر در دقیقه ۵
⬛️
🇮🇷
0️⃣
🏆
1️⃣
🇪🇬
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663695" target="_blank">📅 06:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گل اول برای مصر</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/663694" target="_blank">📅 06:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔹
اگر ایران صعود کند در چه تاریخی و با کدام تیم بازی می‌کند؟
🔹
اگر اول شود، چهارشنبه ساعت ۲۳:۳۰ مقابل یکی از تیم های سنگال کر‌ه‌جنوبی الجزایر یا اتریش
🔹
اگر دوم شود، جمعه ساعت ۲۱:۳۰ با استرالیا
🔹
اگر سوم شود، جمعه ساعت ۶:۳۰ با سوئیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/663693" target="_blank">📅 06:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شروع بازی ایران و مصر</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663692" target="_blank">📅 06:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8963e8bd37.mp4?token=gufdhcySd5I88SRMODJCRDKOsJPxq0ilJMlWzyjZvFYSnl1y5MraMf8ggEEUP48WUBhSxhoJSqYNi0KukHS6RouYE-ojHtSTVahiZBr_uM5IrA6s_Kn9M6JzxBAj48KF-2m3f4SUiZ6wsOPjSvblD1VySJCA0vNdWDxzH6KPgX6PDqp9s5ff7mAuonnAqlUqg1-KrplXPhZzwQFB6vwAO6ur4tUUX87RRWchMoMnOkR_lZzJL52XMBK6TO0B58K6y_ur-w0VsNXgTjjeNMTQfuxyqiSUBp03YeQfyy7FdhIOWVHng05hNq21BcRyWBUXsXbhyONUxkbojsQu35G1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8963e8bd37.mp4?token=gufdhcySd5I88SRMODJCRDKOsJPxq0ilJMlWzyjZvFYSnl1y5MraMf8ggEEUP48WUBhSxhoJSqYNi0KukHS6RouYE-ojHtSTVahiZBr_uM5IrA6s_Kn9M6JzxBAj48KF-2m3f4SUiZ6wsOPjSvblD1VySJCA0vNdWDxzH6KPgX6PDqp9s5ff7mAuonnAqlUqg1-KrplXPhZzwQFB6vwAO6ur4tUUX87RRWchMoMnOkR_lZzJL52XMBK6TO0B58K6y_ur-w0VsNXgTjjeNMTQfuxyqiSUBp03YeQfyy7FdhIOWVHng05hNq21BcRyWBUXsXbhyONUxkbojsQu35G1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش سرود ملی ایران در سیاتل
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/663691" target="_blank">📅 06:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqlbaDEh5j07WkFoYEXWbS1CLKqr4VT2VXDq15ESX0gvUUyW6wE1hJCAn_Jg-sJp8xOqdde1vzg3errzGASH0pnS26NPWaCORM2zG3BQySadmwkv2npl_IHH8f5X7PPk-WPCtwodpoZ3f1aDSjcjruA1JLy0ETpoVWZuhRBkMMWnXZsEcaPj70tx3CAg6fdaVVdik2oPMFXSyexghgoMRd67vZmnMtwI8C9oom9qAUJBghI3mLSL7Wpb5TfVxz-rBx4vXKhKzHEU2SwrPIgfczZ8SVqkDh0sabVAhcqxOOhAhOhb8l_s3w_Jx8PdHwXOhfKmHXnFqb5LwHS91vLwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنان تیم ملی ایران به احترام ایام ماه محرم با مچ بند مشکی وارد زمین شدند
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663690" target="_blank">📅 06:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ef2dc9165.mp4?token=PS2xsJkQJq70gvxTS9zUn5TlDza5TBnsFKxWgwehGMWqN5YnfBOzfm3QInjAdqphFDbGQnhIB10Fk5EOH9E3c6i9uaMJ8KoM4l6V6AETn4B6cT_-ASSG5q8AImLGQl-zA65EKN0mHkF5Nitf-2v6JR4j0cYQ5ayd4nAgC44CHafVnsQTWP3wCs0pCmgr4kOtV-igQ5jLR7H-FiafFcC5zPXgBbqczOKAaouoG3SjgyozvuctEh9GTigh6q6FG4u9A-6UIHodrr4Wq-RdxXPfkDyTOyVovfyHkWZZEK5icDs90JHFJmK4kyXeIn-aPd8ZOvr078E3DDwYEjl4Mi7o_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ef2dc9165.mp4?token=PS2xsJkQJq70gvxTS9zUn5TlDza5TBnsFKxWgwehGMWqN5YnfBOzfm3QInjAdqphFDbGQnhIB10Fk5EOH9E3c6i9uaMJ8KoM4l6V6AETn4B6cT_-ASSG5q8AImLGQl-zA65EKN0mHkF5Nitf-2v6JR4j0cYQ5ayd4nAgC44CHafVnsQTWP3wCs0pCmgr4kOtV-igQ5jLR7H-FiafFcC5zPXgBbqczOKAaouoG3SjgyozvuctEh9GTigh6q6FG4u9A-6UIHodrr4Wq-RdxXPfkDyTOyVovfyHkWZZEK5icDs90JHFJmK4kyXeIn-aPd8ZOvr078E3DDwYEjl4Mi7o_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال ایرانیان مقیم آمریکا از تیم ملی در سیاتل
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/663689" target="_blank">📅 06:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c4ee4c5a.mp4?token=kz0kJSfUxdqXzL2QIrRwphXEJrq0CAnXDfHs_AWieK3aa4z0cV_yc8z5Aqt0wAo9WHxvvcHgpL1h2m-P7r5sFN4l8ZvMhvydvTfY2j5PEaNR6GSEQL6Ct634wNpvpMUqxDVRf3LLTj-GSD09YIuoHHnH6AJsk0p-Ff25iQwdr1U1NEEqk79iXZ1UqJI-l2e8x46NUYvj7x-Rg4nAmiFaiJUoxXOOVIfUfz5WiyRheRAoO4R-UeeEHNbQerIUa3mkwlBVDS4Av6uk7p9pWhu7UHsRl9Uj7N-oonZatWy8-5v9XCfiBZpFNUL-z-SZAi0LGZ6Tud4hkm8JL2wcVgne9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c4ee4c5a.mp4?token=kz0kJSfUxdqXzL2QIrRwphXEJrq0CAnXDfHs_AWieK3aa4z0cV_yc8z5Aqt0wAo9WHxvvcHgpL1h2m-P7r5sFN4l8ZvMhvydvTfY2j5PEaNR6GSEQL6Ct634wNpvpMUqxDVRf3LLTj-GSD09YIuoHHnH6AJsk0p-Ff25iQwdr1U1NEEqk79iXZ1UqJI-l2e8x46NUYvj7x-Rg4nAmiFaiJUoxXOOVIfUfz5WiyRheRAoO4R-UeeEHNbQerIUa3mkwlBVDS4Av6uk7p9pWhu7UHsRl9Uj7N-oonZatWy8-5v9XCfiBZpFNUL-z-SZAi0LGZ6Tud4hkm8JL2wcVgne9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برافراشته شدن پرچم ایران در استادیوم لومن فیلد سیاتل پیش از شروع بازی ایران و مصر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/663688" target="_blank">📅 06:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa92b91582.mp4?token=QV_q4_HmpAiNydpgIcR8I30pDU1ih2KYJnpqAYoVbTkSbbHEmFvEwJcZ4dKRHROKOTl7NrOLa32PeFjH75C1auXEXBSHihFo7ZZZDjtZT63r6gxvCHZso7MZCQELMFmu6_Ng7EbJeOUcgI98BQEFAR7H49t6-t7v3X3YfFrTEyL0RT2MscYi96euquTO_JZACd6DQ-BDVxYa-buhaDgb5bZSbcXkA1lX3KU70CROz_wwxCfP52uaJqKVhpqeVs95ecW1enT1_v5cQxgoQVD0uDQaEKQ3dwzDWPZJYXhGFyjm5uj4wINJtCswyDncU0v800S78M-uTFW0afLFlJ1WWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa92b91582.mp4?token=QV_q4_HmpAiNydpgIcR8I30pDU1ih2KYJnpqAYoVbTkSbbHEmFvEwJcZ4dKRHROKOTl7NrOLa32PeFjH75C1auXEXBSHihFo7ZZZDjtZT63r6gxvCHZso7MZCQELMFmu6_Ng7EbJeOUcgI98BQEFAR7H49t6-t7v3X3YfFrTEyL0RT2MscYi96euquTO_JZACd6DQ-BDVxYa-buhaDgb5bZSbcXkA1lX3KU70CROz_wwxCfP52uaJqKVhpqeVs95ecW1enT1_v5cQxgoQVD0uDQaEKQ3dwzDWPZJYXhGFyjm5uj4wINJtCswyDncU0v800S78M-uTFW0afLFlJ1WWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
واکنش جالب صلاح و طارمی هنگام ورود به زمین بازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/663687" target="_blank">📅 06:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
جام جهانی بدون محمد...
🔹
محمد لقمانی عاشق فوتبال و تیم استقلال بود و آرزوی بازی در تیم ملی را داشت؛ اما موشک‌های ارتش آمریکا پس از اصابت به میناب، آرزوی محمد لقمانی و ۱۶۸ انسان بی‌گناه دیگر را برای همیشه خاموش کرد.
شاید محمد می‌توانست در جام جهانی ۲۰۳۴ بازیکن تیم ملی ایران باشد اگر...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/663686" target="_blank">📅 06:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663685">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔹
بیانیه آمریکا درباره توافق بیروت و تل‌آویو/ نتانیاهو: در منطقه امنیتی باقی می‌مانیم
وزارت خارجه آمریکا:
🔹
توافق شامل تشکیل یک گروه هماهنگی نظامی سه‌جانبه برای لبنان با تسهیل‌گری آمریکا خواهد بود.
🔹
پنتاگون آمادگی دارد بیش از ۳۰ میلیون دلار برای حمایت از ارتش لبنان اختصاص دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/663685" target="_blank">📅 06:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663684">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8867ed6e39.mp4?token=K-2Oyw-zP_JSiH30O93ygEJ7cspE5IrCmbppp-aLo0MEOSdY7QTdmT2kN-pZjTKnWegX8HLrfuk30m1cyUEat8zBxn3-WYSHoXjS6-yfLvJ2VQAzRB_26rUv6LvXEm1eP8OJkJP_BD7JUoT7jmCSP1DKo5M6vtMWa1qflOoEhFkeTz6tC0hxUuoCH7BD1zs4rn9hzPsQhe5h7kKXxCH8lroHn4LMIpZIlHd2jOH7yFOfCtrsd7lr-u1fvrvItBp88NM13VhAAYFCTY80vfXuxnz1AlQhMmeGut__zf6b48H-CmoJsiwWCBWDaQuGwdrirY4lJ8ZdvcQcn5z6ckQyhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8867ed6e39.mp4?token=K-2Oyw-zP_JSiH30O93ygEJ7cspE5IrCmbppp-aLo0MEOSdY7QTdmT2kN-pZjTKnWegX8HLrfuk30m1cyUEat8zBxn3-WYSHoXjS6-yfLvJ2VQAzRB_26rUv6LvXEm1eP8OJkJP_BD7JUoT7jmCSP1DKo5M6vtMWa1qflOoEhFkeTz6tC0hxUuoCH7BD1zs4rn9hzPsQhe5h7kKXxCH8lroHn4LMIpZIlHd2jOH7yFOfCtrsd7lr-u1fvrvItBp88NM13VhAAYFCTY80vfXuxnz1AlQhMmeGut__zf6b48H-CmoJsiwWCBWDaQuGwdrirY4lJ8ZdvcQcn5z6ckQyhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای ایران
🔹
پیش از سومین دیدار تیم ملی فوتبال ایران، همراهان خبرفوری از شهرهای مختلف کشور با لهجه‌های دوست‌داشتنی‌شان، پیام‌های صوتی پرشور و صمیمانه‌ای برای حمایت از ملی‌پوشان فرستادند.
🔹
این ویدئو،  بخشی از صداهای پرانرژی و پرمحبت شما مردم عزیز ایران است.
🔸
الوفوری را دنبال کنید
👇
#برای_ایران
‌
@Alo_fori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/663684" target="_blank">📅 06:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psulItd0HaBxpG97rJpCOhJCR3Zeag-x84tQW30H-q5Wiiy38XR03SCYr5YnSeuFdzB6pX_J-bYNGB6ICj8hgMZA6q-pCt-oB-KeCeSBl65Dybu_x7emqrkFXJnmfv_D9CBd48aWbzP5S3iOlPSyA2sig4deZ7GRHsaK4MWVMvWSK9fB-Sfe8xQHWOhVKHm8ThautIccz-KfFcbaKuy7DWwDfm2lp93MDcKrcutilmW_CZOG938QEfcqhU0RQlT2y96OviO7LdIbJY2G-YyAhk8AhrUTW9cjcIIQwrhcEuwNyLm0zvd_TVudAuPcdKwVHDjeaIEMi2Tg6oGQOk2YZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd9965105.mp4?token=k8ALQXD5XBGEND6zAaW0y-6IoC3zBqjLvULaegSjv239KomuCcRjALQmUr5suHyd4LhXZQPqWYNPpJWIoIHcKB8vMeXXR5Ec-ZJaiUyB04UEnR62-50CYalUTDw_HXBGiQMlPkeYDU0C6gPvMPUcSaZ0egK6cAjtKyGbIO0ilEtFtgDhsl3GqdN6hpwXMG_CvUVAiy-t6FB50jsqnnA3rDbotTbmbNf_XZuF0Xv8iviGDtu429TKGqtNehY1zG6-AsYjypSHb9D3UNoz0H5V9KpLD_dk-hzJ-a628kdJ3dSRer04FvI-d4yUeo9CUHSLnbJkZ1Jkf9qTnXpXxZsTow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd9965105.mp4?token=k8ALQXD5XBGEND6zAaW0y-6IoC3zBqjLvULaegSjv239KomuCcRjALQmUr5suHyd4LhXZQPqWYNPpJWIoIHcKB8vMeXXR5Ec-ZJaiUyB04UEnR62-50CYalUTDw_HXBGiQMlPkeYDU0C6gPvMPUcSaZ0egK6cAjtKyGbIO0ilEtFtgDhsl3GqdN6hpwXMG_CvUVAiy-t6FB50jsqnnA3rDbotTbmbNf_XZuF0Xv8iviGDtu429TKGqtNehY1zG6-AsYjypSHb9D3UNoz0H5V9KpLD_dk-hzJ-a628kdJ3dSRer04FvI-d4yUeo9CUHSLnbJkZ1Jkf9qTnXpXxZsTow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حال و هوای ورزشگاه قبل از شروع بازی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/663681" target="_blank">📅 06:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔹
مدیر بنادر شرق هرمزگان: ساعتی پیش صدای انفجارهایی در حوالی سیریک شنیده شد
/
وضعیت در بندر سیریک عادی است
🔹
بندر سیریک روال طبیعی و عادی دارد و در ساعات اخیر خسارتی به تجهیزات و محوطه‌های آن وارد نشده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/663680" target="_blank">📅 06:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663679">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔹
معاون سیاسی امنیتی استاندار قم: خبر منتشر شده در برخی کانال‌های فضای مجازی درباره مشاهده و فعالیت پهپاد دشمن در آسمان قم تکذیب می شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/663679" target="_blank">📅 06:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663678">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcBwkyI4tQ-Ci4nw6ygbeuLinMQ9SQiSHU20YKMgN4TX2CTfalFF53Vws9GHdJX3xZ4J-uydbwrQc8OficqvmeSRJXR-DOZIbGwWdWq11EBwWwXAPeG0Kmu42v_Mf59brS8CSUI4aum3XJsflv0t9sLwJzFfDffA6Rv-lXzQFHOZoBWlt0EgwND59m37nCiawCnwzuI0rCak85n2Gzhs8hn-Xp1QnPuh3NpvlbcdKcn8FsFNNez-BgnvPSZfPv4SO4WsfY8tYaUOGUZcbnX5L9_PEUObtG6QdPRjE_K0e32VdRkPfg_iU63KVNbFUsARnHcb9Iq3yOaNtSZHoG_YeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جدول تیم‌های سوم تا این لحظه
ایران در صورت کسب مساوی با برآورده‌شدن یکی از این شروط بالا می‌رود:
🔹
بازی الجزایر-اتریش برنده داشته باشد.
🔹
غنا پیروز بازی با کرواسی باشد.
🔹
کنگو مقابل ازبکستان پیروز نشود.
🔹
تساوی بلژیک و نیوزیلند، به‌طوری‌که گل زدۀ بلژیک بیشتر از ایران نشود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/663678" target="_blank">📅 06:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663672">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wpe-2ucmrq3HhnkbbcZ_Jl1_f8Nrf4b2g0BpFtxH-o6tPlg7ESpe8QRG8dmKJrk-jMME_d34y1HS0Q30dmuqKlSl7pvovkQLECY3TW5dNSaLTUaViuiTZnpQ5IWdc6oEI-P9rU2lD0nk46EuRShpyYYmDjc4wi9hp_c7bvdDTS8OxJutep2HJHG-XC8QUFFBVVTFUb25u-iLWW6x-u-AfccuBectQXTWKHTiEIdbU60DqsPR9YAmI5wx5W_iP5v0Z7cdDOInelLSMLas7qA-JtkgitU5HpzJfQ72JRadhZXfIvsVB1aRTF8Nco8HNYJgVtw8bV9rit-wcYK3jiXqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIONpHa4mNSslCjh45t9XuaQDtbkWrPcBCXDwj9bVd2sXXEJ-g0oQ1drk_Mfv0KWac_f3aiXtzxds7bZhnOWgSM-B-E5DUvNDCWGSHcSr3bOWgjCvSSrT8EUciI5pxPbAWj9X350pkvECVzUXl59j-Va8MU0q4jgdAa6RsylrfnEg_xd8iUogtHuxMzGz-I3jalgAX3FZqEqxL7tLm1vv7ORuNq0-wfMKQ0uMz4OE_jDK6fV8vPK9mJ3QDGYRM0_alhYYKCch7P0MiTRJmF21cQ28TYEYOzAD2SoUEDScNG18EihoUMpMdc9dBW6yJNHyVU9OYn2lcFRQMcaaGPFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDAXJ_tM3JwPUxt-Xl4z87EA-WZA8jN393ANLFUuetIcUBsiI1hlH9Tcs71K0e-vrOtbpK2r31ZPG3xtoxfJ4siaUJ3tD0O8YPMma0BjxwwOaJqtGFGUaJQA41kfUCgXfTebaN8w59K-8ti725Rxpv0hs6wJRSg8QsTxmw2DMYz_SCogNdCNtj2-dvN88zzp-LjI9cGCZ9sGqqnaUuIwhWfvK4KeR3w-0VliIsga1c43cECaVvUWXTf3gQSHQ7PXZpFT2PID7w7cOLDDMUpoxGBV9Ri7V9FMhzd6-42zZOVz6vQtoFD3ijnNyjobfX7JYi66g0Ny5wljbrm4S2-8fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Os3o5TIEcOAZQm29-_prqrfuLc9jTt-09iPW6XaURR1f8k-23faWga2tJzRjIYd-Eo8z6ARYE_j6mKmwwbPvRw1nST3LlPKRcvXOPcfNhF2yJ12SL2p7tdsYHLACSbjZE_J50lSTRsgK4t_hIlaUmVortvbjiCu0upR6yxj_OSDxbMK31uqB-BQGj7ho9olXCtfCbAtzc8ljkRoLFvUzScn7t0JskiV1Y1sJ7-qFLrWohjFtT_9AdUoogmxqItQ6iL4EhONaXkr7JVoyTkxURttGnoI_yP234m2W6G75DvdN0jZOwhRaK8cNNzvYXWolYJLyaurGF3fNewHbyxuNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLOa8ha3J9HUx1-EmZSRgV3VohXhPZklg1xgWWBkr2c9vBTeO7ubwk6wMoe94OewrrdMT4evMmR1pazNZ47ru0Cv_SmHyeVifk-R6Fc1Y1eXftEXOVO8MVuqzZQvPSXimpe7rUNYbBUS6RjFyAoSnOcpV3L0Y1WnAYolHmQaavmI50LPvRaBpJUZTnbd97DesYkd5anhdBSWLytMx4RZfL67-J7w_mpTnm9ccD1CfLua1B-tytH79XULI_7hixFNRx6fGtkOGH9gvu8B5MLK-3oCXcPGqPGcyp5FSuNADX_Cl9y9vGtQgfdQep9exSp7sKm3jUHB9qEFsusNsqKjZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aj8ORhH7RDfzJbyFoQ0vP3wsQEssPhjWu8QLP0d_JM5Tutf9rEOzkNIYivP29xdoe6_HJiNMoG3c6tiWbV1CitvnDKSRUZ_hn_uw6QTZI1XVT3zy2W8KU9EaSGys5l56gSN-OBEgSdAVOt3elI2DE-9ElyCquDwI7BiujtUhWwlO43TBGJEFOePRhXhmIHai0lpP3uNI74WI1lWLomfWaShVXWUyW4NUrlVawLNCNPkxtpiYl8yDjEqtD5mv_wN2TknEs2R4g_DMbyrBIEvdNm8LB88vkNyjY9sedYnun0OofWtlPHWdh-n9jsAy2P4T5NXZdgYp7IxobrFb53omdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
به
یاد شهدای لامرد در ورزشگاه لومن فیلد قبل از شروع بازی ایران و مصر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/663672" target="_blank">📅 06:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663671">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEBp2ZTP_y5oAEuAlczaUEXwkIU3_3h3O_1F3S1Rk-Kf0MBxzPSTDD88Eoj29S-lQtE1rUhHVj6_FpN7KFIPcTAWp2Y_N9vas6J8OO-OveCGVDKb8iAkSepgac_rqUxso1rbyEKwU32IHSI4HxEzKuCfgfLu1mcKPiTE0g0KTspKG_2r855MaSxwqXMM1mAotwKEBff2cEIZXSrKBvL6tuM4ZWP-q4MRhrG2XoVrLwvOwBeD8AuX6gtAqAB9BqJbLDs5K8yF4I2gLElY4NLZLlysau3KOn863v8bKBxUcCxFTSvz-BHIon3mNZdSIlASTMRIx7UFSIihkqEcbgXOjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ترکیب تیم ملی ایران مقابل مصر
🔹
پخش از شبکه ۳، ساعت ۰۶:۳۰
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/663671" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0wWM1jG5PJpz-YUh7XmskzJp9eScGNeSH28MkUM_CyZwlUfgI_b_NKMenvcEuJZltbzDX-OmrCaxGjF4bpYBYaTta44dDra-wHnH7ualDZ1lwLhyshGZV4PsSY2DP6ljt5YESCvWeWpJsUf-f8ZyDAyohcwFgVkC5DVkqOKAlB1x_XQHqUEEnRhINq0zcYJO2IeYfSa0YfVSu7nqbbCWhGDWe7t_eHcompphJGTulZQf_dxhcYhmFFwsvail4bXb9LqQQWdq0JtUfTq5aSVe9Oc--zEVnAPFA1HTvt8qN-gYshfx9PuiAQ2ySNI-XKqdBab9yfd-G7Z5E7NZmRx8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۶ تیر ماه
۱۲ محرم ‌۱۴۴۸
۲۷ ژوئن ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/663670" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663669">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326494ae86.mp4?token=bVIYSRTQLxInIbBhROWx7p-Es8689P4aCJAIlMUGyLyUjLJoW5m5mRVshpOwP0gWuKjBPkSI7k2e_yw2GKujiZyLkPFb5fdauek7BFjTlJO3w4REI57ZXfaP0C7BuIBDP2QAuUTslDnBpqVoLSMZ2k9G9jCRssICN6s6GCY3ydwDE5oQ1AIGo7KeexXvo23VZE8nFfiK0fdVmtRo3efh9EUiGrMSyxR-Bp9C7rbCFogqWTKLZoxYO_brxnuiecP_yiuPY_HBiz6YHC-3vpioqo90cukaTJ6-xl3nbqBvt361nJsARmqD18zPLQDrghCOe-lAZtkuNfPsDjtmwcLoDAEuZl-Ur_TB6hxZvRPlgRDyvq7n6osJ8-G2zsD_7Dukk6jFNTv-Y5ZTGfcz0zcGZSBjiZi9ZZnPZYlaLuU_h4M6wHOSGMaca7eRLRyCSpa_8HPKhlIUycSko50o6lW-qcah3aLp8a-Cwo4RoTi7pryUHEnxq-IY-ooIf-3gBeLAgOM0xlm3D5nbhcuQPLAvdFCSjtKtYHmWIqWFNllLgHzz9T6NGmNIUr2T1DPFNAY5QGy6EonDz1s7WSf73Uv1nrYe2t5kHhXO7odwyQTf52LViWf1uQNvcy_To_nYFOKo44pmCCiCQjyvlGjjP_08MlT2XIkHgsX9KVmi7lhreYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326494ae86.mp4?token=bVIYSRTQLxInIbBhROWx7p-Es8689P4aCJAIlMUGyLyUjLJoW5m5mRVshpOwP0gWuKjBPkSI7k2e_yw2GKujiZyLkPFb5fdauek7BFjTlJO3w4REI57ZXfaP0C7BuIBDP2QAuUTslDnBpqVoLSMZ2k9G9jCRssICN6s6GCY3ydwDE5oQ1AIGo7KeexXvo23VZE8nFfiK0fdVmtRo3efh9EUiGrMSyxR-Bp9C7rbCFogqWTKLZoxYO_brxnuiecP_yiuPY_HBiz6YHC-3vpioqo90cukaTJ6-xl3nbqBvt361nJsARmqD18zPLQDrghCOe-lAZtkuNfPsDjtmwcLoDAEuZl-Ur_TB6hxZvRPlgRDyvq7n6osJ8-G2zsD_7Dukk6jFNTv-Y5ZTGfcz0zcGZSBjiZi9ZZnPZYlaLuU_h4M6wHOSGMaca7eRLRyCSpa_8HPKhlIUycSko50o6lW-qcah3aLp8a-Cwo4RoTi7pryUHEnxq-IY-ooIf-3gBeLAgOM0xlm3D5nbhcuQPLAvdFCSjtKtYHmWIqWFNllLgHzz9T6NGmNIUr2T1DPFNAY5QGy6EonDz1s7WSf73Uv1nrYe2t5kHhXO7odwyQTf52LViWf1uQNvcy_To_nYFOKo44pmCCiCQjyvlGjjP_08MlT2XIkHgsX9KVmi7lhreYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
🏫
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
برای دریافت اطلاعات و ثبت‌نام:
🆔
@modaberanschools_bot
📩
یا عدد
۴۴
را به سامانه پیامکی
3000909030
ارسال کنید.
📲
❗️
آشنایی با روش‌های نوین آموزش و موفقیت تحصیلی
👇
🆔
@barsaschools
📍
تهران</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/663669" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663668">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔹
توافق اولیه دولت لبنان با رژيم صهیونیستی؛ خروج نظامیان صهیونیست در هاله‌ای از ابهام
اکسیوس مدعی شد:
🔹
در توافق اولیه لبنان و اسرائیل، زمان مشخصی برای خروج نیروهای اسرائیلی از خاک لبنان تعیین نشده است.
🔹
بر اساس این گزارش، دو طرف بر اجرای مرحله‌ای گسترش حاکمیت ارتش لبنان، عقب‌نشینی مشروط اسرائیل، آغاز طرح در دو منطقه آزمایشی، بازسازی پس از راستی‌آزمایی خلع سلاح و بازگشت غیرنظامیان پس از تأیید کنترل امنیتی دولت توافق کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/663668" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔹
آتش بس نقض شد  به گزارش خبرنگار صداوسیما در سیریک:
🔹
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
🔹
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
🔹
حدود ۵ ساعت پیش چند شلیک اخطار از…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/663667" target="_blank">📅 01:58 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
