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
<img src="https://cdn4.telesco.pe/file/dv-1XR8JlYFVkT2OgS5mIyi95tsANhKtya1QbAm7_KdArqbMF03M9DfoXxFkuJyMSLPDp3L40_hrNEnQKt4caC598MzadwmZnx96QoADnHFrCsNDLrwK859BjlncACKVbGJuDjlz2SOiNJVJF_rXb_TaYwfvkvxwhPbB8O9zxxobLY_vTJwqZij49-JtriG1WYxeYRTB_moC_3jpYAJmWQs_hzKeiJXSI-mp5cbTqofPD4fsZmgP2qwqPENtIj7KsZGneSEWQga5fhVXtPNsrCDE0TxSej_fwNJfI8YF9AJ8-p7mbINsv483FldF78SKDNL8gkS2P4MtG8LInqwFgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 20:42:49</div>
<hr>

<div class="tg-post" id="msg-135365">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/135365" target="_blank">📅 20:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135364">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
محمدحسین صادقی پس از چند روز عدم حضور در تمرینات پرسپولیس، اعلام کرد به دلیل مشکلات خانوادگی فعلاً به تهران نمی‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SorkhTimes/135364" target="_blank">📅 20:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135363">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/votkoAzFzhe4ZJno-JetF6WI2fjCq8a2mmQQC4gv1zgVoH2azre6NwcpQXP0U1-ZuV9E8-4p5K31RPN0sBJ7OK9jxma_jZxvw9z0oxmg49AggFrnJ1RpfamoQ9RkEUWB6Lui370L8oaMfWzs2B6loH9ZhOLdMtC4x2I3McGuOQJgQsQ9ykMaIFt0O7SsD0vrPkEvX-x1Mxtbdz6qwN-rF8cS8FQbFdPqhwhutO_WcaU8xpmTuPQFLkB8X4DhQ1m1LPTuA_fWHrfQ_L2vMqAn0jA4fp0B8QGu7DAURwtn_t19udGRa4iwmVbC9_qAT3C2IDLY90WdHdCXy85fK9qUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
این چرا اینطوری شد
✅
پ.ن بازیکن آزاده ولی کسی گردنش نمیگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/135363" target="_blank">📅 20:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135362">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
محمد قربانی: با باشگاه الوحده امارات قرارداد دارم. رضایت نامه من برای باشگاه های ایرانی 2 میلیون دلار و برای باشگاه های خارجی 3 میلیون دلار است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/135362" target="_blank">📅 19:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135361">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/135361" target="_blank">📅 18:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135360">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3Wx8OudkqEk3NXtdjrf2heFSPUXo8ScN7DnAiaTtS8dmqkmkgxrP2EEorWZCsvAZQABMgLtePz66_gdRGNDWkIaIzrCxbaxkCkIq1liUmBDZyZ00CxL-JviT2kYRVnLp8nC6m7WaB42HPUMMcK_4_n2R2KGoMXpZQPCiQ9AgrnNssNjLRoxJP_b6wzO4Y7R5QpNb4ltmZH1fjMSvhf9baeS3AmfsGwR_6b1FhFzS2ORyrc9-AHVa4A3QOpGBztorIERk_bLLl3jqK6-Ko_A1FD9iKDEXYGjazvebtwK_Ksb2FpPNed2sqkTj7QVmxdzT_P--Zsk7a4dRluScXk0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سنگین ترین و غمگین ترین عکسی که تو دو هفته اخیر میتونستین ببینین!
❤️‍🩹
🤭
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/135360" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135359">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bef21d0f.mp4?token=QHgIIb8b8eB4qRNHAPITL9wL1GGSD4dWyS6ry3ntgpizacPjAQTGZhG2MFWjLZ-PNrZhukq2Yp3R5uMERRItI1JEK8Zhn0OrBPaZsmmVGC6CW3bt6ZsIPSkGGoMC7t-l96soj3iNZvovVJ3TV-YafbkgzMKSBnDs7JaJbeY-RdmY7nW1eysih_zth-y4BKqbbnjb9F34dtsfYZWLhp_P_8IAIG4s4tWg0OVgFg9EO9jSAlNuMFm5lf_M3-02rsiSeoGydEl5b2XX02YtXEKTWGfPrNplWh9oD-2Rz0iZEcXPypW9sXQFgd-z0SzObahaVkZ256uZkuO_RTQQWkG6nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bef21d0f.mp4?token=QHgIIb8b8eB4qRNHAPITL9wL1GGSD4dWyS6ry3ntgpizacPjAQTGZhG2MFWjLZ-PNrZhukq2Yp3R5uMERRItI1JEK8Zhn0OrBPaZsmmVGC6CW3bt6ZsIPSkGGoMC7t-l96soj3iNZvovVJ3TV-YafbkgzMKSBnDs7JaJbeY-RdmY7nW1eysih_zth-y4BKqbbnjb9F34dtsfYZWLhp_P_8IAIG4s4tWg0OVgFg9EO9jSAlNuMFm5lf_M3-02rsiSeoGydEl5b2XX02YtXEKTWGfPrNplWh9oD-2Rz0iZEcXPypW9sXQFgd-z0SzObahaVkZ256uZkuO_RTQQWkG6nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
سعید مهری : برای جلالی آرزوی موفقیت دارم؛ بازیکن پرحاشیه‌ای نبوده و به نظرم حتما موفق می‌شود و توانایی فوق العاده داره و هواداران پرسپولیس با آغوش باز او‌ را می‌پذیرند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/135359" target="_blank">📅 18:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135358">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
گلگهر سیرجان خواهان جذب مجتبی فخریان شد
🔴
مایل به معاوضه با پوریا لطیفی فر؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/135358" target="_blank">📅 17:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135357">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
باشگاه سپاهان که تمایل به جذب نعمتی داشت، طی روزهای اخیر مذاکراتی با این ملی‌پوش ایران انجام داد و به توافق نهایی دست یافت تا خط دفاعی‌اش را با جذب او تقویت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/135357" target="_blank">📅 17:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135356">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/135356" target="_blank">📅 17:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135355">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
گلگهر سیرجان خواهان جذب مجتبی فخریان شد
🔴
مایل به معاوضه با پوریا لطیفی فر؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/135355" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135354">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/135354" target="_blank">📅 16:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135353">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCbHhf9KN5vOeCKSbH0vtGLmfgsuukzsdmYquA2Gh2bYg4r5nwQM217BqkzFHrHJtpX57O5Xpy9zEBut8ZUDUHxmgwgR0ITjon9dLBaFasJtb-L210_R778ht5s0a-27un6lN40k2wcS9WWiobn67OKnQxLJFVlh1pA5ZWGmL5BR7NP9jeDDgGHJ0r8RXYjR19MRc05nHQbna2XKJpnPDXOL6qWvNXlqElj7x7uzqkGAPFW21Qrt-gH5r_9Ep_ZoQun-P1PzzF40hXcDt2MtfMiiyzktbVs9kYgyDAKr-sRKq6STHIcBmVvDHF3wkCzIlPZnAoBtS0hacPFSvbpqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/135353" target="_blank">📅 16:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135352">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
✅
ایگور سرگیف مهاجم ازبکستانی پرسپولیس دوست دارد از تیم جدا شود!
⚠️
اما مهدی تارتار او را برای فصل آینده میخواهد و روی او حساب باز کرده است
👀
ایگور یکسال دیگه با پرسپولیس قرارداد دارد //,تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/135352" target="_blank">📅 16:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135351">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
❗️
تارتار خواسته امروز از جلالی هم رونمایی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/135351" target="_blank">📅 16:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135350">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
تایید شد
🔴
پوریا شهرآبادی با قراردادی ۴ ساله به پرسپولیس پیوست ‌
🔴
باشگاه پرسپولیس پوریا شهرآبادی، مهاجم ۲۰ ساله و ملی پوش تیم گل گهر سیرجان را با عقد قراردادی چهار ساله به خدمت گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/135350" target="_blank">📅 16:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135348">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0slEpu0QG9Xlx5Ap8dEYkpdIEVxeiRyF5Rjwv7TGDezODUacchOqRJannMECt7Wj79M__33llqTMntAcfRZPzmqcmMol-DrzJlx63lG6s_B8DDnZ3-xIYb5YgjpsOmhPN-ZbCq2fnROR0FYWbXf0dMGG3BzmfTLncWfNH4fub7ipKhuTAsdhjz0JnBXsmURkSWxUoxrtSzviPMtzT5yNQSGWRSqus63m2nMTlfFmvNw7rj6Nvc23UklERqfHfFiz0JTRVykxYerRfI4LRDC1Wlda_DPgMkvjtCdC_zPaXLb4upmF-ZOI2NhM2qkyF4-zAFkwmTIJMAu1hVhw024xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
شهرابادی، طاهری، پورعلی و جلالی پوستر رونماییشون آمادست و فقط منتظر تأیید حدادی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/135348" target="_blank">📅 16:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135346">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
❗️
در حال حاضر دو طرف مشغول حمله به هم هستند ...هم داریم میخوریم هم داریم می‌زنیم ...اوضاع خیلی بدی شده ..حملات سنگینه ...احتمالا به پایتخت برسه حملات ..خدا به همه رحم کنه تو این فشار سنگین اقتصادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/135346" target="_blank">📅 15:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135345">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
میلاد سرلک پس از جدایی از پرسپولیس بصورت فشرده درحال مذاکره با گل گهر سیرجان است و اگر اتفاق خاصی رخ ندهد این بازیکن بزودی به جمع سیرجان ها اضافه خواهد شد.
🔴
🔴
همچنین گفته میشه مذاکرات امید عالیشاه با مدیران نساجی مازندران مثبت پیش رفته و اگر یکسری مسائل…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/135345" target="_blank">📅 15:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135344">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
❗️
فرشید حقیری: حبيبی‌نژاد از پرسپولیس پیش‌پرداخت گرفت، ولی تارتار گفت نمیخوامش و کنسل شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135344" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135343">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
فرشید حقیری گفته مهدی ترابی هیچ‌جوره به پرسپولیس نخواهد اومد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/135343" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135342">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
سازمان ملل : شاید باورتون نشه، بخاطر درگیری‌های مجدد تو خلیج فارس، ایندفعه خیلی بیشتر ازقبل نگرانیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/135342" target="_blank">📅 14:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135341">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/135341" target="_blank">📅 14:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135340">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
بدنساز یونانی پرسپولیس پنجشنبه وارد ایران می‌شود
🔴
پس از انتخاب مهدی تارتار به عنوان سرمربی پرسپولیس، وی در حال تکمیل اعضای کادر فنی خود است. پیش از این حضور وحید فاضلی، علیرضا محمد و اینانلو در کادر فنی سرخ‌پوشان قطعی شده و احتمال حضور کریم باقری هم در…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/135340" target="_blank">📅 14:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135339">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
تیتر روزنامه گل: «گل‌گهر به پرسپولیس پیوست!»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135339" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135338">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135338" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/135338" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135337">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NfyNKd69Z59n21YhREHkrppQIggki5BH5D21iGm-t73qHrqpG8bEaRhDbw89GCQAuoYJyxoRfpT6QQO_X0JNhWHrsDPLWoKsyLC4NMb6lnCL8tRpgZPAZCmnM50zKaVhg017jF5_zFtIkkeYxROPMI3Juvd-V6w8Yqy1pwPTgu3OLC0_lMOqS3SeJQFTZgJ1K9_n4Gma92t6UEFTZX26FE4xNq-nS4RNyRsTYsbM7B6WnKFn-WCa4uMtAPDcpV-xcoBCvSbCbQvwyAswLXFk2A4wy_zRzvJHGyFJwgzRxczS7s-1Xp6CvS8ElTZ-_3ioTmjr3MF4TJwPl0BYhYidOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوق حساااااس
فرانسه
و
مراکش
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
🆕
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/135337" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135336">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
باشگاه پرسپولیس در تلاشه تا مهدی ترابی رو به پرسپولیس برگردونه.
🔴
البته ترابی مشکل سربازی هم داره و باید این مساله حل بشه.///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135336" target="_blank">📅 14:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135335">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
طبق‌شنیده‌ها: مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌ مثبتی داشت و حالا درصورتیکه‌ تارتار تایید کنه هادی پرسپولیسی میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135335" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135334">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
علیرضا کوشکی به نوعی فوتبال خودش رو مدیون مهدی تارتار هست
❗️
وقتی فقط ۲۰ سال سن داشت تارتار فیکس میزاشتش تو ترکیب پیکان و کوشکی رو به فوتبال ایران معرفی کرد
❌
باید ببینیم تارتار میتونه کوشکی رو راضی کنه بیارتش پرسپولیس یا نه!
✅
گرچه تاجرنیا همه توانش رو میزاره…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135334" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135333">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
گفته میشه شانس مازیار زارع و مهدی تارتار نسبت به مابقی گزینه های داخلی بیشتره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135333" target="_blank">📅 13:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135332">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
محمد قربانی: خودم داشتم بعد از جام جهانی به اروپا بروم. درحال حاضر سه پیشنهاد خوب از اروپا دارم اما خب چون مبلغ رضایت نامه بالا است باشگاه ها کمی مردد میشوند. باید ببینم تصمیم باشگاه الوحده چه خواهد بود و تابع تصمیمات این باشگاه هستم
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135332" target="_blank">📅 12:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135331">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135331" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135330">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135330" target="_blank">📅 10:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135329">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
محمد قربانی: با باشگاه الوحده امارات قرارداد دارم. رضایت نامه من برای باشگاه های ایرانی 2 میلیون دلار و برای باشگاه های خارجی 3 میلیون دلار است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135329" target="_blank">📅 10:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135328">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
بازم تایید شد
✅
محمد قربانی: بله باشگاه پرسپولیس به صورت جدی دنبال جذب من است. اما مبلغ رضایت نامه من بالا بوده و این کار را کمی سخت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135328" target="_blank">📅 10:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135326">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
❗️
شنیده ها : فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
❌
❌
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150 میلیارد…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/135326" target="_blank">📅 10:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135325">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
فورییییی به نقل از CBS :
🔴
علیرضا فغانی قضاوت فینال جام جهانی 2026 برعهده خواهد داشت !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135325" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135324">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
تارتار قراره در تمرینات نظرشو راجب باکیچ و بیفوما اعلام کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135324" target="_blank">📅 09:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135323">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMAYVayrQVZOyVmnVjCj2j_8_fP69et_Ork8nrjSR4ii_RS8hoR0n_noRuMb9jtzFisUosFzxfBJE4-3MdtsC4LPTWykOI4vvmmVjwvhGzhKQxjE_UB-qrqDtOVSl62-H7iE94YoNj2FP2S773PFjP-3MrnCALlGFZ8F9FiwOG6TNqUbts6uEF4sdeAIAMKXljy0H3UULo4CyAqGl4I84YcUohNbUeOoR8WvSw4bJHUg-O-IbCGkZzemRfPNpsxH4fI0skZvq0CKyp17OFiOBt2JUtjq-ldtaUbXUsyMVe1BpzQRN9t90MNL8G2NRYepT8WBi2MPgVqt9zks33SehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیتر روزنامه گل: «گل‌گهر به پرسپولیس پیوست!»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135323" target="_blank">📅 09:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135322">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135322" target="_blank">📅 09:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135321">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
مهدی زارع، گزینه جدید پرسپولیس!
🔴
🔴
طبق شنیده ها، مدیران پرسپولیس مذاکرات برای جذب مهدی زارع، مدافع ایرانی تیم اخمت گروژنی روسیه را آغاز کرده‌اند و این بازیکن یکی از گزینه‌های اصلی سرخ‌ها برای تقویت خط دفاعی محسوب می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135321" target="_blank">📅 09:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135320">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp0CPZWS8K4zH1PeWWVdaanfyYbN8gyxA2Vqg4eFeWkdVJiX6RPnusNpWW6PFqzxn-PUpRr5kpCYPqBwLGAizmUl4hZaw0u2ttQcwv-oix945mmy81efRodkdUso-3CynqJ4D-Me1bv5UxMonE36jrPzIPSsOMyipq-8nAj-AuVrjuM_bAtjT6pxuncNkmKrGE6E2bnhQ1cgEWjZqp5lVDiGFbpUdpxxZsb0FVnf5Ibh9q8XHWBKXLQO4nEqpjXhSM_vAPZbL59pMQz6jhAQTvg7J4BTi9DOOttt24MIxDfpHK8a7ST75JDyAbdUbAnWqoFo0fegW8DYHV3CDX50lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی تارتار کادر پزشکی گل‌گهر رو به باشگاه پرسپولیس معرفی کرده و احتمال بسیار زیاد تمامی کار پزشکی گل‌گهر به پرسپولیس خواهند آمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135320" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135319">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135319" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135319" target="_blank">📅 01:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135318">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy4AiyCW9YhXDVNj1gV9QU7PDtgy_miXm0NhZfgD-li9EmJNz-nZwuXCgt0D5lFUTrhtiKVLcNWVLUum2qwcjyk-WA95P0SWHweI2beDrojss16rR-t_2cu5de__o36dZIA_7OQCGh5G-5-vv6aVr3qX9BKWz4_6XNxrz9bO3mBIhIAJ4XPPhdECBOT5OreL3AdWyz-AGqPuncuVqjWcYy8XFEv9UHaVgvkRrlBZY0cL5nzJkeXtYDSi50oq2O-8rg-3lAsgpyqvAEXUsqZD7RsWAPGvMxmFZsE3VCSu4KTKhfKIQvKgR21lIrTM1SA_A9qY1cPQyuWMsMoh8zZ6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135318" target="_blank">📅 01:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135317">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
🔴
مقام ارشد اسرائیلی به الحدث: ترامپ در تماس تلفنی به نتانیاهو اعلام کرد که حملات امشب به ایران تمام عیار خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135317" target="_blank">📅 01:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135316">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
❗️
طاهرخانی: کوشکی رقم خیلی بالایی درخواست کرده و باشگاه داره باهاش مذاکره میکنه تا قیمتشو کم کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/135316" target="_blank">📅 01:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135315">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
🔴
علیرضا کوشکی هم‌اکنون بازیکن آزاد است اما باشگاه استقلال در تلاش برای تمدید قرارداد با او است. پرسپولیس کار راحتی برای جذبش ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135315" target="_blank">📅 01:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135314">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
انفجار های چابهار خیلی شدید و بی سابقست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/135314" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135313">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
✅
ورزش سه
❌
علی علیپور در حال حاضر باتجربه‌ترین بازیکن پرسپولیس محسوب می‌شود و این موضوع باعث تسهیل در تمدید قرارداد این بازیکن شود.
🔴
هرچند که او احتمالا انتظار دارد تا پرسپولیس عدد مناسبی را پیش روی این بازیکن بگذارد تا او از نظر مالی هم شرایط بهتری را…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/135313" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135312">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
🔴
موج جدید حملات سنگین آمریکا به جنوب کشور آغاز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/135312" target="_blank">📅 23:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135311">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
آکسیوس: شدت حملات امشب طی ساعات آتی بیشتر از دفعات قبل خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/135311" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135310">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری/ CNN:
🔴
حملات آمریکا به ایران ممکن است در ساعات آینده آغاز شود، تیم امنیت ملی ترامپ در حال تصمیم گیری در مورد دامنه و گستردگی حملات آتی می‌باشند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/135310" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135309">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
❗️
نساجی برای خرید ایری ۷۰ میلیارد پرداخت کرده و دو تیم استقلال و پرسپولیس هر دو بدنبال جذب این بازیکن هستن، احتمالأ رکورد مبلغ رضایت‌نامه تاریخ لیگ برتر شکسته بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/135309" target="_blank">📅 23:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiv89yK9kmld_vUgvST4US6t2lFXYH0rlcAJS_IRJyw_0y2UEpDlf5yiQAr2bSWi05-p55eAm0JOWVXBYUrzX4LzuORTfekY5D_k2O4A-k2EVGwwNZzCSIDmZx5-ZU-kNR616rCeEmgVe4HcnHZ4JUcG1CQKR_KAMAD1CoBFnecypASa15E1WVHM8UWrHBYMf7zd1DVbHHwT4jZiCouOM6yCqSqPikyjwU6HNTLBZYnGnXJVz0i4DKPkzc__H5PWxr-dv2atvWv0bHzB4R_jHDIrG5riI_KxcK8jsSJOhxAuqx-LO_SCXbzxdX8R8Qy1YdmiXplPpO6BAIBcDg3ihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
خبرگزاری آنا: به دلیل یه سری مسائل حقوقی هنوز از جلالی و شهرآبادی رونمایی نکرده. بعد از حل شدن مسائل حقوقی از جفت شون رونمایی میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/135308" target="_blank">📅 22:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135307">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
ترامپ: حملات امشب به ایران ممکنه خیلی بزرگ باشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/135307" target="_blank">📅 22:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135306">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
گویا باشگاه استعلام‌ گرفته که مهدی ترابی هم اکنون بازیکن آزاد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135306" target="_blank">📅 22:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
قدوسی: مذاکرات با احمد نوراللهی در حال انجام است و مدیران باشگاه در تلاش هستند این بازیکن رو به پرسپولیس برگردونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135305" target="_blank">📅 22:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135304">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
غایبین تمرین امروز پرسپولیس:
❌
پیام نیازمند ( تیم ملی )
❌
محمدحسین کنعانی زادگان ( تیم ملی )
❌
مرتضی پورعلی گنجی ( مازاد )
❌
میلاد محمدی ( تیم ملی )
❌
دنیل گرا ( مازاد )
❌
میلاد سرلک ( مازاد )
❌
مارکو باکیچ ( نامشخص )
❌
امید عالیشاه ( مازاد )
❌
علی علیپور (…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/135304" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135303">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
غایبین تمرین امروز پرسپولیس:
❌
پیام نیازمند ( تیم ملی )
❌
محمدحسین کنعانی زادگان ( تیم ملی )
❌
مرتضی پورعلی گنجی ( مازاد )
❌
میلاد محمدی ( تیم ملی )
❌
دنیل گرا ( مازاد )
❌
میلاد سرلک ( مازاد )
❌
مارکو باکیچ ( نامشخص )
❌
امید عالیشاه ( مازاد )
❌
علی علیپور (…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/135303" target="_blank">📅 21:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135302">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
غایبین تمرین امروز پرسپولیس:
❌
پیام نیازمند ( تیم ملی )
❌
محمدحسین کنعانی زادگان ( تیم ملی )
❌
مرتضی پورعلی گنجی ( مازاد )
❌
میلاد محمدی ( تیم ملی )
❌
دنیل گرا ( مازاد )
❌
میلاد سرلک ( مازاد )
❌
مارکو باکیچ ( نامشخص )
❌
امید عالیشاه ( مازاد )
❌
علی علیپور (…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135302" target="_blank">📅 21:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135301">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
نخستین تمرین پرسپولیس زیر نظر مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/135301" target="_blank">📅 21:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135300">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIR_vwxQhUZSriO712pXxD9iFToM5WkymrOF4Hqsd8cbt1zOaB36d9velYj2gVY-ttOeWC1j9Wc8ey4SsyviAMRQfEWkYbxACZWufn68gxlGltWMOTuTx4bmhfIabr_O3REeBe2QhxZOYtqRzqMBfmyiI5kRvKuvuSZfsmVkXZAFvcesTZrET8H5KfB4-4asa1cFEdo4soKpoLPqiWsalTYT3i4MT2U2lypAAPVl_zFt89S1iRmQ2MUbMH-u_xbDbULILXeZkIUnXyiRsM27ADz5SuR-ZR-oUWCsOeqF4bDtxe4_fLe1dr4JvAUJgvd-p9attzNVw7DPrrOVw-pawQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نخستین تمرین پرسپولیس زیر نظر مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135300" target="_blank">📅 21:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135299">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEDw3hfZIptpdhttzf_CMY7I2OQeAmETXRkFHILbxm7gY-4-WK6rem1aJrfc-qQqKkLVfUXMsxL1acEJT4-B5UZWoRW9cVcEnk7aH2MZrjeVUCwuc1fdJjCd728YQLf0PfE60rX3xYpbKa1wNOm4D4JDIZoGW5DYN6EubVVwbHEZaFJhTG9357cqm3eRscNKdAVk2e5FP3HVUhVIxvSaVAJfG0Fq_CqTiBlhm_i-yH0Vu7VZI1cdJyAAi78nyU29nMc2vQfJjjuseppsSEdy0wDfWwREqGc9tzLkq2GU9GCAxbLq_Oq2jdwp2RPr0io_oSVQz__0BH5OsLpFKV_hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه سپاهان که تمایل به جذب نعمتی داشت، طی روزهای اخیر مذاکراتی با این ملی‌پوش ایران انجام داد و به توافق نهایی دست یافت تا خط دفاعی‌اش را با جذب او تقویت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135299" target="_blank">📅 21:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135298">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه ، وقتش نرسیده که از فوتبال دیدن پول در بیارید؟
😉
✅
@FuckBet</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135298" target="_blank">📅 20:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135297">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jNo8bTn8Pgu-pQlBnPmaufBHipEjQa0sfgNeWI0jWN8j1HDUcIOLCVx_NgoA5k5f3wq5ZX0YINKoPVjDaIws81nPuJpsyjoTSdol0dTUxiUW-BX2LGBf-FL2ztEBhN_FxEJ8cW8r1g0JEi8FL5u37TreC3RuGHXSH0_GzjOYEya0i_3THUaiGjCIyEJZ0fqYrIbiF1559Yml14FD7UFhWqpSdpDnAJ3Qmn_L_UGTw4249qZuUj21hwd-RGz-C6ghxPZHU4Gze0Vvrkoj_jbe1FrPX6IsUetagNMYZ1esJQAP1DBqV0F0Q5uQ8_8gKY2eFOdGisflxu3TMvJe0zbPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی نه ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/135297" target="_blank">📅 20:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135296">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhHGe8zoDVhN_7IaxgFvHicNqUGyOlAtjZo--96M52It32YkekFdS8KCnYfG50XFnSlWSPf1dF6tIhp5RcX3iGScoe8Uk-tV6vXg872nksNCWEkHRm19SStSc2qs5tQ_Ln48e-AOA-kOqH9CePoZPgScmsdRG7zrW7Uoemuz5nSMkvugcJn-7R278iDeeWPtFpkJmw0cPZN7eHXt8d0SCPaTU9Vf33I9lVThqkxaiVeMlul6K5oBAIEO6dl4LjIORDUOYTRrR-A2peE3uyHGAe-BCxmnTzZlmsWUiqXoPMugm9fs6heDXgxvSXyYnOtzK5bPqJM3P_e6YrNNYf3wiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مراسم معارفه ی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/135296" target="_blank">📅 20:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
یه هوادار تو دایرکت نوشته: امروز دم باشگاه بودم آقای خلیلی گفتن نه نوراللهی میاد نه محمد قربانی رضایت نامه هرکدوم دو میلیون و پانصد هزاره//قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/135295" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
باشگاه به خاطر فشار هوادارا فعلا پورعلی رو تو آب نمک خوابونده تا نتیجه مذاکرات با قربانی و نوراللهی رو پیگیری کنه و اگه اونا جذب نشن پورعلی رو نهایی می‌کنه/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/135294" target="_blank">📅 18:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
❗️
شنیده ها : فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
❌
❌
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150 میلیارد…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/135293" target="_blank">📅 18:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
🔴
علیرضا کوشکی در حال مذاکره با پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/135292" target="_blank">📅 18:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135291">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/135291" target="_blank">📅 18:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135290">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
شهرابادی، طاهری، پورعلی و جلالی پوستر رونماییشون آمادست و فقط منتظر تأیید حدادی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/135290" target="_blank">📅 18:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135289">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx7jZqUGPLqNy5V77pfG-tYFFvS4Ftk9zOFiWUdCR4Yme5QjoX3TXgUj1MBnYglDzKXwIrC8L_3cMoidZKh0OYmTdNZ9DoJAlfdu-vE4NdML-xOrx1D3hRszncicqi89D_ggGe_r56_00uZDiJRKrdoGXa-VLG7N5lsKb_O-uCWV0XUwpvrjBZp15AgC040ViARXGkkBn9GTvt1d-BMfH7a6qOgMhUZMzZZkfSW_iJWBGZMYybBIE87_dZzzK_pBQbRvdLVOLmLvx8VnEPlkRS-n1V1AW6_SnDbkNtKxAtwib4ZaLpaZdSHDnFYjpKBHgoWEbF1vs3kqlI48TTu9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید
که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/135289" target="_blank">📅 18:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135288">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
احتمالا باشگاه برای رونمایی لایو داره  وگرنه چه‌ اصراریه که تاخیر داشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135288" target="_blank">📅 17:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135287">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
باشگاه ماهم عالیه
❗️
طاهری، شهرآبادی، جلالی بستن و عکس هم انداختن پوسترشونم امادست
❌
اما باشگاه میخاد یجوری رونمایی کنه که تبلیغات داشته باشه
😐
مثلاً لایو بزاره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135287" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135286">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
🇺🇸
ترامپ:
❗️
دیشب جزیره خارک رو زدیم ولی به نیروهامون گفتم نفت‌ش رو نزنید ممکنه بخوایم جزیره رو تصرف کنیم چون از دستشون کاری برنمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/135286" target="_blank">📅 17:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135285">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
باشگاه به خاطر فشار هوادارا فعلا پورعلی رو تو آب نمک خوابونده تا نتیجه مذاکرات با قربانی و نوراللهی رو پیگیری کنه و اگه اونا جذب نشن پورعلی رو نهایی می‌کنه/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/135285" target="_blank">📅 17:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135284">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
تایید خبر دیشب مون
🚨
🚨
🚨
🚨
تسنیم: ابوالفضل جلالی دو ساله به پرسپولیس پیوست.همچین پوریا شهرآبادی چهار ساله با پرسپولیس امضا کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/135284" target="_blank">📅 17:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135283">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
احتمال افزایش نفرات لیست مازاد پرسپولیس؛
🔴
وضعیت نامشخص چند سرخ‌پوش
❗️
❗️
فرهیختگان: دور جدید تمرینات پرسپولیس در حالی از فردا چهارشنبه در زمین شماره سه ورزشگاه آزادی برگزار خواهد شد که هنوز تکلیف نهایی برخی از بازیکنان این تیم مشخص نیست.
✅
✅
اگرچه مهدی تارتار…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135283" target="_blank">📅 17:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135282">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
ترامپ: حملات امشب به ایران ممکنه خیلی بزرگ باشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135282" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135281">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
❗️
#فوووووری از ترامپ: آتش‌بس با ایران به پایان رسید و از این لحظه هر دستوری بخواهم برای زدن ضربه نهایی خواهم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/135281" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135280">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
مطابق اعلام سایت ترانسفر مارکت؛ تا به این لحظه مهدی ترابی و مهدی هاشم نژاد قراردادی برای فصل آینده با باشگاه تراکتور ندارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/135280" target="_blank">📅 16:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135279">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
🚨
🚨
⭕️
بازگشت خانبان به پرسپولیس: به‌زودی....!
⭕️
بر اساس شنیده ها، مدیران ارشد باشگاه پرسپولیس با توصیه خداداد عزیزی به دنبال بازگرداندن مهرداد خانبان آنالیزور سابق پرسپولیس به کادرفنی پرسپولیس است
🔸
آنطور که از باشگاه پرسپولیس خبر می‌رسد احتمالا باید برای…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/135279" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135278">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/SorkhTimes/135278" target="_blank">📅 15:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135277">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/SorkhTimes/135277" target="_blank">📅 15:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135276">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
البته این خبر هنوز رسمی اعلام نشده و یکی از ادمین های ما در نشر آن عجله کرده. جلالی گفته امروز، فردا با رسانه باشگاه مصاحبه می کند که پالسی است به نشانه امضای قرارداد‌. این مدافع چپ جوان به تازگی تمام پست هایش با پیراهن استقلال را در اینستاگرامش پاک کرد.…</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/135276" target="_blank">📅 15:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135275">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/135275" target="_blank">📅 14:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135274">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
با تایید سهیل صحرایی این بازیکن به عنوان بخشی از مبلغ رضایت نامه گلگهر برای شهرآبادی، از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/135274" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135273">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
شنیده ها :گل‌گهر برای شهرآبادی 120 تا میخواسته
❌
ولی گویا صحرایی + 80 میلیارد توافق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135273" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135272">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/295a60cd54.mp4?token=JpHB-Xq1BiwnApIfMAz-uFV_t4OieWKlQqm8UOMuyEXF_rp5gH5VnUgWlP3O0HI3yC3bHqgsGtL5QeflRVBHTXQRqfX5QIriPRz6CMGdDMEle24aUiAnedzXLJW3hHqqCmNvz6hwDFRFJRT3yA5kMM5tFgNqsMD8VyDD1uEhtoQfwcd16BpPSnn5Q_pygHnXb0gjTv3QcmKVX6m5PxaD3fQp9T-xWkO9MQvv0L4GB9DF4kbKJah2ratSaN3ZXDsfxW2yU9DmdeaDcyPm7sTko6BEhSdRRi3QV8gKatbx6BACk14zerLTU-9AuGU2-tfcBuF7oyUgYsKF-3pBkARIGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/295a60cd54.mp4?token=JpHB-Xq1BiwnApIfMAz-uFV_t4OieWKlQqm8UOMuyEXF_rp5gH5VnUgWlP3O0HI3yC3bHqgsGtL5QeflRVBHTXQRqfX5QIriPRz6CMGdDMEle24aUiAnedzXLJW3hHqqCmNvz6hwDFRFJRT3yA5kMM5tFgNqsMD8VyDD1uEhtoQfwcd16BpPSnn5Q_pygHnXb0gjTv3QcmKVX6m5PxaD3fQp9T-xWkO9MQvv0L4GB9DF4kbKJah2ratSaN3ZXDsfxW2yU9DmdeaDcyPm7sTko6BEhSdRRi3QV8gKatbx6BACk14zerLTU-9AuGU2-tfcBuF7oyUgYsKF-3pBkARIGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سهیل صحرایی هم وارد دفتر باشگاه شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135272" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135271">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135271" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135271" target="_blank">📅 14:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135270">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135270" target="_blank">📅 14:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135269">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGZTv_WVdIq3tgITbmzYAj35R1Hm86GwgrzV9toikdJ2Ji5PcWD93kwNLu41dD2Ip01XNUvNYhp8B0XiZZ4TDumvgF82QRFSShBmw6u_joMmHWuVNikOO9W59cK3LhO0Xw1S_2zHxo058SXNe2rccubi3XKsKDQIcTyj-YrqGmhOCluTgwR1BRSqQoiMbaqKLGOv57te0xQkQLw2m9PBIWtigOJ0q5n_BMEAuGUDllkAqQtVxeBYKW3hnnhzvzouDYz8_pu7GHoKuixywVbQENQHr59znZWWxmkL6r2Ku7K1iC8Ksm7k9wQfPgzpG8l7JsjxqNUxYzG7bKBXCalhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💙
ابولفضل جلالی با قراردادی دو ساله رسما به پرسپولیس پیوست
.
❓
نظرتون درباره جلالی چیه ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135269" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135268">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c56bb19ad7.mp4?token=de3CgfYH35trfQu_IX-_9hI04FlR4NpXvuoaRSc7XpYXww8dgvZVp4f5F5Rb9Y7SIXxw8ZrmyYZBuxI_vI8GB39ulRuEt-90hOGYyDHYJZoIrV9fhdF-5IoFt3NNKMSwhlF2j9qJ5sxjSJvvzw5fTyjkpDlrlVJ_2H_wqCxHDOeArmzCXPWEfPUtagYr3775kb8byePZck-o1LIVCPuLinJEZmxRqniwtCeG8cGIuuB2YzXksMDGKyw8XrTMvMnWaUAIHmTj2luhNRM4AvKf0itq7NZuY5Sg1d-SoFluc1Bj7FO9S-WOh4Eu_i2CLE3xEjVcN5qyIKq36vI7FXMPHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c56bb19ad7.mp4?token=de3CgfYH35trfQu_IX-_9hI04FlR4NpXvuoaRSc7XpYXww8dgvZVp4f5F5Rb9Y7SIXxw8ZrmyYZBuxI_vI8GB39ulRuEt-90hOGYyDHYJZoIrV9fhdF-5IoFt3NNKMSwhlF2j9qJ5sxjSJvvzw5fTyjkpDlrlVJ_2H_wqCxHDOeArmzCXPWEfPUtagYr3775kb8byePZck-o1LIVCPuLinJEZmxRqniwtCeG8cGIuuB2YzXksMDGKyw8XrTMvMnWaUAIHmTj2luhNRM4AvKf0itq7NZuY5Sg1d-SoFluc1Bj7FO9S-WOh4Eu_i2CLE3xEjVcN5qyIKq36vI7FXMPHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پوریا شهرآبادی هم بعد از جلسه با مدیران پرسپولیس، مثل جلالی بدون اینکه با خبرنگارا حرف بزنه، محل جلسه رو ترک کرد و رفت اردوی تیم امید.
✅
✅
خودش گفت باشگاه اجازه مصاحبه با رسانه‌ها رو بهش نداده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135268" target="_blank">📅 14:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135267">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=Tyf0v2d8KIjO0JUglG2ykjvFSFfORhmGuG_hO425Y2USLIEEdKJuJkDrzDctSesuxoKRBOTex2S9Tb3jLeYH24YZNP3hKjmAJ_T7wbXSMwC9QuVk9plZ8pCKGie9JGIMX4Oz0cIGPZu2Akju8FTPIeuAUOc_3hNB8-sKkdxQ_xsxg9CETJubdmRFrDo4BqWOLbRniI_m_I1_gIMXMplXbyz87p_QrxUYtM-rhVA2RKSaCmlArXnVUwFXE5Omhf8rAod90smyJ-xWEWgY53rOAxQKUweCIJXyQaD0FSpOP5tCC5999Hy97cyl1bND8UAF90qLr4TLPIZNpxDT_m4ajA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=Tyf0v2d8KIjO0JUglG2ykjvFSFfORhmGuG_hO425Y2USLIEEdKJuJkDrzDctSesuxoKRBOTex2S9Tb3jLeYH24YZNP3hKjmAJ_T7wbXSMwC9QuVk9plZ8pCKGie9JGIMX4Oz0cIGPZu2Akju8FTPIeuAUOc_3hNB8-sKkdxQ_xsxg9CETJubdmRFrDo4BqWOLbRniI_m_I1_gIMXMplXbyz87p_QrxUYtM-rhVA2RKSaCmlArXnVUwFXE5Omhf8rAod90smyJ-xWEWgY53rOAxQKUweCIJXyQaD0FSpOP5tCC5999Hy97cyl1bND8UAF90qLr4TLPIZNpxDT_m4ajA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏅
جلالی هم اومد بیرون… به خبرنگار ها گفته با رسانه باشگاه مصاحبه کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135267" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135266">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a7269d75.mp4?token=b28fHRGzal_1iGuLG4DDrgVqUo4zliKebgpZExgd8mV3AFbPUOLUM9sqwBnCckso4-lCbcgvMpOcVGU6LjkdSsIzmPKiQ6f_2Nbz9ldUNTvQiHATzIysUtrCeWD4HrP-p-4XjeBV91-2eWDDAS3Dm3rRjJt9hQAGHV9jCKKbsTdtg36PSWLqP6-SCEmpFVL2ZVXBvk9ttlF685z3qOzb4engKuQQCGOiAMD2BWHKbv17AhqSg57JUKYG0owXnlXELV9DMUwTys9VJA5Zp_LOnJ3pHYMswK-f_RNX_xROo7jC0CY6eqaNH5tS6R8uvzN8WF_8TB-Ni0C9EXtuBO4bgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a7269d75.mp4?token=b28fHRGzal_1iGuLG4DDrgVqUo4zliKebgpZExgd8mV3AFbPUOLUM9sqwBnCckso4-lCbcgvMpOcVGU6LjkdSsIzmPKiQ6f_2Nbz9ldUNTvQiHATzIysUtrCeWD4HrP-p-4XjeBV91-2eWDDAS3Dm3rRjJt9hQAGHV9jCKKbsTdtg36PSWLqP6-SCEmpFVL2ZVXBvk9ttlF685z3qOzb4engKuQQCGOiAMD2BWHKbv17AhqSg57JUKYG0owXnlXELV9DMUwTys9VJA5Zp_LOnJ3pHYMswK-f_RNX_xROo7jC0CY6eqaNH5tS6R8uvzN8WF_8TB-Ni0C9EXtuBO4bgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محسن خلیلی برای عکس یادگاری با خرید های جدید وارد باشگاه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135266" target="_blank">📅 13:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135265">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx-605qm9Ky7OqJFiPGh-gn3YWrrNPei--3FJDTW5z7li3hyfi6pppUU361X1ixkOod8bDvZVMRj84cDqOAiofvPL1UH8w-twzYmg8N2d4cocxLBXLflI3WjbsjdT4GUnaOVHN0fSdnY6WUSvYkNvO1TIQnR2YgG2CayB7n-20rt46fqNp8_lrzdtGHBdMM87LtbFJB0VjvjPDX6xTNi0IPAasz9pX6RimUxHkT40fEi_5AQRzoBP1b6XbLk1DzpcUWqnSM9JQ0bHP44W3Gk3sqz89PNo1IGIWIpHuDDfp3vVRdRI_ajjEiZ8jJRM8TlJDAk5VgtVeF7YajRluxU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
نظرتون در مورد ابوالفضل جلالی؟؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135265" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135264">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ba7ad723.mp4?token=PveN0ZtFeMoj-suSgsKFI_zDiHuRCZ73Pq8yv-BwDiKUva0VE5vyNdF2sPT1mW25smmd7Noaz_AP8M4W2N7MyLB9DE25Ruydd-Uil_9jvrisRCpQswffdmFPxuAUbmVyO501mQJBH87LEb9YNLfwpH1h1tqKUTSTCDmLK7OylPgY7WK5FEPr29OCHgSZUaSmyq93_tPRKO6JjZ3ilV2qGEmv2hMHZet3Nrtg5cZuTJwvouCCXRFf5ubB0CLTVIwpHOs0Ihog7hvp26e8ilOq4jXPd2ev8W5gepjZePIR3Wv4U_r0r3YzizpCAKdbBAu5fB5fKjqIHT1g2ueagXNmBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ba7ad723.mp4?token=PveN0ZtFeMoj-suSgsKFI_zDiHuRCZ73Pq8yv-BwDiKUva0VE5vyNdF2sPT1mW25smmd7Noaz_AP8M4W2N7MyLB9DE25Ruydd-Uil_9jvrisRCpQswffdmFPxuAUbmVyO501mQJBH87LEb9YNLfwpH1h1tqKUTSTCDmLK7OylPgY7WK5FEPr29OCHgSZUaSmyq93_tPRKO6JjZ3ilV2qGEmv2hMHZet3Nrtg5cZuTJwvouCCXRFf5ubB0CLTVIwpHOs0Ihog7hvp26e8ilOq4jXPd2ev8W5gepjZePIR3Wv4U_r0r3YzizpCAKdbBAu5fB5fKjqIHT1g2ueagXNmBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گل پوریا شهرآبادی به استقلال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135264" target="_blank">📅 13:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135263">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
پوریا شهرآبادی برای عقد قرارداد وارد ساختمان باشگاه پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135263" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
