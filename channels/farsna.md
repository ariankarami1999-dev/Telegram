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
<img src="https://cdn4.telesco.pe/file/NHHJfyRGJ8Abw4zYKd-7kQtVdMe6pRwiOCrMKOt-VSkYrgGT5mR6XI25aLo3chNfD8zJS06cCHVGV79Hzx8bPlqI0zu7TJUaR2kL5ZxK2pR3GYVjWnAjRqdu7yz76Q8xdfsK8HraLLK1cmVx9Y-wbU0O6lfpYFZcUDrA438AL4efGnzan2_GnEaBa_lHg-WamVsoa1y1LJgB4KnRAvrxqKFDKDYIhCvzRbcep6ZlLPKVZmd-0Lv8M6_Cyc1-wUZKxAvmxly0KALJY0Jzwz2Llb8UKzSh9nAY_YFc0cA1Ps3USNq3ozocoUIB9dXauUR5kLPhO-mdKh8AAashQjFv8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 00:24:30</div>
<hr>

<div class="tg-post" id="msg-465571">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5001bb0671.mp4?token=Vfq-_18hmSlXInJc6YOlPYKqZcI_zeX3jXwtnbG3D7Z4BBQ-mzbo35X-U1oBHcp5xpQNakqZf3DlFOiQkcZW5D_1tQ8p4uo13wRRBE_60wLGjvp0WYW5Ui2AxXDw-3GIcZNmMc6qiqhxsnfbesktLTfp-MtV7oZMtgSDR6P7gLUADo3s9T7zjn8oevP9GIlF6o4RX2KlIJvZpb7y0s0W-EQP_zq_yRajCC_tzy0xXuUm9YEP1mAOCtJLFgylvuu_YfGdfa5U5ndlKSNJcRx5Zbx05MeG0YCP_qVA78o456VeGWb4KLvWj_RVzas6d_dIq6R92qdnBOe1fLcBpMMMIzUac1RM7hcKjksF9XCoKC-Ae4NpI0A0AzA0maZxt441Xa8uSmv_yWdRw8km3DxCvkJ_HrxXpSxkFKFLKTEAtJmHSUqgEPAa6MPuyKurnqFdEiKUVOx7EB5gDkeM4cIF5pKTlXWcLgUx4P2QDe2a27ePf-yVgi4rvdIA2gvFTt0GncGTNSnnpvAeHF9i179xafLAkTCcFzuNqDxjmxGXuvMKo4E3ogKKAOf0NGtGhrpTYsV8ev6PAN-TRP9WC_ogBVA1JbTHxGC9vM6RppRwb762CvEtSYaJdrdbVPutbtOpgqS_a5zlahQNr0JnlNekW3u6B2zMXcmJoFcUVUILkVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5001bb0671.mp4?token=Vfq-_18hmSlXInJc6YOlPYKqZcI_zeX3jXwtnbG3D7Z4BBQ-mzbo35X-U1oBHcp5xpQNakqZf3DlFOiQkcZW5D_1tQ8p4uo13wRRBE_60wLGjvp0WYW5Ui2AxXDw-3GIcZNmMc6qiqhxsnfbesktLTfp-MtV7oZMtgSDR6P7gLUADo3s9T7zjn8oevP9GIlF6o4RX2KlIJvZpb7y0s0W-EQP_zq_yRajCC_tzy0xXuUm9YEP1mAOCtJLFgylvuu_YfGdfa5U5ndlKSNJcRx5Zbx05MeG0YCP_qVA78o456VeGWb4KLvWj_RVzas6d_dIq6R92qdnBOe1fLcBpMMMIzUac1RM7hcKjksF9XCoKC-Ae4NpI0A0AzA0maZxt441Xa8uSmv_yWdRw8km3DxCvkJ_HrxXpSxkFKFLKTEAtJmHSUqgEPAa6MPuyKurnqFdEiKUVOx7EB5gDkeM4cIF5pKTlXWcLgUx4P2QDe2a27ePf-yVgi4rvdIA2gvFTt0GncGTNSnnpvAeHF9i179xafLAkTCcFzuNqDxjmxGXuvMKo4E3ogKKAOf0NGtGhrpTYsV8ev6PAN-TRP9WC_ogBVA1JbTHxGC9vM6RppRwb762CvEtSYaJdrdbVPutbtOpgqS_a5zlahQNr0JnlNekW3u6B2zMXcmJoFcUVUILkVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد لبیک یا سید مجتبی زنجانی‌ها در شب ۲۱۴
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 348 · <a href="https://t.me/farsna/465571" target="_blank">📅 00:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465570">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udKW8ownpLau4CGqDu-wKCJmzjJ4Ozj0n4kkFl0qKT4-FFNOuo9y2_ErKxrDde8JDPfexeVedXL6GxhGL8jrpnbVHeSuaX3Ap9piyaX2xs5VKPoSUE3F9VH8W5MAaxvaDwBDFoevJPL7nCLRLc4n6lMg3Astz1gpmFHnweX2xxLNJyfP6ABytg-NANfaemECLO-l4yvdarW92gZ-G-xiJcOTVXzAmI-mZ_RW9phjGLE9rfxkNKX1ma0YCZTN_ueMOye8uI-D98Ts9k0jJdGgR3-YAGmGfRj-sFkUgZL3eaOlLuQWpGaQozuxRpMyjN35bitu64EG7T_mcKxs88cXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیک اندیش تا نیکی آید پیش
🔹
در زمان پادشاهی انوشیروان، ۲ مرد به دربار آمدند و جلوی قصر ایستادند. یکی با صدای بلند فریاد زد: «بدی مکن و بد میندیش!» و دیگری گفت: «نیکی کن و نیک اندیش تا تو را نیکی آید پیش!»
🔹
انوشیروان دستور داد به مرد اول هزار دینار و به مرد دوم دو هزار دینار پاداش بدهند. نزدیکان و درباریان با تعجب از پادشاه پرسیدند: «هر دو حرف یک معنی داشتند؛ پس چرا به یکی بیشتر پاداش دادی؟»
🔹
انوشیروان پاسخ داد: «مرد دوم فقط از نیکی سخن گفت، اما مرد اول از بدی هم یاد کرد. هیچ نیکی بالاتر از دوستی با نیکان و یاد کردن از نیکی نیست، همان‌طور که هیچ بدی هم فرقی با همراهی با بدی ندارد.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/465570" target="_blank">📅 00:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465569">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESsQ5Dnf5NAea-OW8dHwm5ykylPeXme-m72zTpK-VR7C3UXUsXbimBFlFQ38COiqGZtarduj1nb9roMo25SU06qIhfqhM0S8FQnfs00JYIyFiuAXWTEbT8fynMbnm2xG6MYMfeWAc6lZ5dzFnsNkzsJp48J6Gui_1GobbiVN6Vw_aq8u42fjT0u4yPzcxVnMgyC8hDE6YpE8nZRn7ujSNaLzAAW_V49D8oc-crMJ8Vd1ttS70u0zbsb4jcKxt4vB9dFqMWQEJZ1isvK7mToLiZPpgSx7F2zb6iwCg6btGjhNWtnsAJbmHT8Oh6Xl6dNruhqPcTcoEdfTPc_9o5W9sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/465569" target="_blank">📅 00:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465568">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63025fdec.mp4?token=EoAXjgFdMMt6Db6fekjhVGsOJfPtdcsgHTQBRZ4HAgTDkRUkLCc29KJm1lG1uMNov4FEB_Lqw7CaQ7vsTqsTN8sNTH1xJjaaIlQYUZYKHJim-m0-7gcGuhqYFN5mjGFgJwuVdZTepUasW7XReVsTVTbvEBEDOJn-fs6Umhda_t5Hq4Rj6Jdtzc5CulTYpoSgtejO4CS4GA3uD1M5ESq9hcUC99vDMXCuczl28tPEJJx9BQFu5xSL4475JShGaRHRhwRTrFSb__iFxE8bPEEX9bg7i2o77IK5IW1Ihe4llcMy4QAVeORz5m4YXQpxgRQ4D7u3wivA25pyBcMnhiGpiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63025fdec.mp4?token=EoAXjgFdMMt6Db6fekjhVGsOJfPtdcsgHTQBRZ4HAgTDkRUkLCc29KJm1lG1uMNov4FEB_Lqw7CaQ7vsTqsTN8sNTH1xJjaaIlQYUZYKHJim-m0-7gcGuhqYFN5mjGFgJwuVdZTepUasW7XReVsTVTbvEBEDOJn-fs6Umhda_t5Hq4Rj6Jdtzc5CulTYpoSgtejO4CS4GA3uD1M5ESq9hcUC99vDMXCuczl28tPEJJx9BQFu5xSL4475JShGaRHRhwRTrFSb__iFxE8bPEEX9bg7i2o77IK5IW1Ihe4llcMy4QAVeORz5m4YXQpxgRQ4D7u3wivA25pyBcMnhiGpiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد امام و شهدا در مسیر بیروت؛ سفر جمعی از شخصیت‌های فرهنگی، هنری و ورزشی ایران به لبنان با حضور حاج سعید حدادیان و حسین یکتا
@Farsna</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/farsna/465568" target="_blank">📅 23:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465567">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUbKuKUsSEwbPeWp3EDwjV5y7hv6ej9Xy6J8TMdoUU9HOOkzVUGPkjyFKXcLSnjD2wSNhiWKvGVXAm9AHHM7EkuiaD_sQK-ndw80WE3M2uTOUVAn2vK3K5yRljUNjgqkOCG4gRJ5EaJtg_AMKHrxYmoiWkA5JYa9L5i_Nbf3EsYw-sXtTjANgbMXy2JMyVIt3H1LklK-qNDfCLwKqTI0YqWVzEWry7wvpewUkmpyS7hUe5WBKvr5xKtZtZDcBSiiGMwARokkbhc5rSYhodlpv0iVp0beRiqbpZaohe0OIBz62vJnBuoCqs7OsEfEmsVVfZ_FdaCpBQMwiVzNJ-9Vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای احساس «تنفر» ترامپ نسبت به وضعیت جنگ با ایران از زبان عروسش
🔹
لارا ترامپ، عروس ترامپ: جنگ با ایران ممکن است منجر به شکست ترامپ در انتخابات آتی شود.
🔹
ترامپ به‌شدت «از نحوهٔ پیش رفتن اوضاع با ایران متنفر است» و آرزو می‌کرد که «اوضاع سریع‌تر پیش می‌رفت.»
@Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/465567" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465566">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70242d6d56.mp4?token=OlFutacbH2qpnvd0yjNkkuOPKz6HkOh8oHHR3xP0tMLaMw1qBIxYkdTz4yVgi9zMuA6BSX0G2xv5i0SMYfN54ASHhU10Ud19GB6QD6DcPCHwHws8N7i3l7FHaL83sqLzkxfMHiVopRIJSCE7b3XaXuBBWvW9FPjtkjCiDPJYb5mbYgO0vBwt8ZC1zcHBEiFon4r9c27UC8uwVdw_r7Fs4LRpfIMMaBr02TAhIcz2kBJKPTkHia9VfzbaWH6twlmrV4hC33FAojA7U_F0txkrnxXP1f8uj5PbgV83M9n0qLsJ4xAf6zd2jlSNy7LDX-LF98Fh12Ri_zdCxdJvFUVsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70242d6d56.mp4?token=OlFutacbH2qpnvd0yjNkkuOPKz6HkOh8oHHR3xP0tMLaMw1qBIxYkdTz4yVgi9zMuA6BSX0G2xv5i0SMYfN54ASHhU10Ud19GB6QD6DcPCHwHws8N7i3l7FHaL83sqLzkxfMHiVopRIJSCE7b3XaXuBBWvW9FPjtkjCiDPJYb5mbYgO0vBwt8ZC1zcHBEiFon4r9c27UC8uwVdw_r7Fs4LRpfIMMaBr02TAhIcz2kBJKPTkHia9VfzbaWH6twlmrV4hC33FAojA7U_F0txkrnxXP1f8uj5PbgV83M9n0qLsJ4xAf6zd2jlSNy7LDX-LF98Fh12Ri_zdCxdJvFUVsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ وزیر جنگ آمریکا به رسانه‌ها بابت افشاگری دربارهٔ جنگ
🔹
وزیر جنگ آمریکا: همان‌طور که می‌‌دانید فضای اطلاع‌رسانی هم میدان جنگ است اما رسانه‌های ما کاری کرده‌اند که رسانه‌های دولتی ایران معقول به نظر برسند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/465566" target="_blank">📅 23:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465565">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6cddf678.mp4?token=Nj7d7rUeaRQE_O_p0xTOYmr9lKVjDNkiypERnZiLwLK2aTWOnEkHYuWCfZQ33ftRdwsjchmYEkDgrXcjNs8mZs0apSkIrnrPZkS7XLnt8F09nR2wZMTFyezoaUi_ST8yp9O6P3_NbmIO30amrOgOkgMIAQdLI7jm7XbYsEEpYG1Rpfcvj4rx1vmSrzwyDL6w3OnQME0jZTuTwysp7kCGlnuhZXuAunDx4BZwxO8aENDmkJm1bCOKSJ2hwlyoiEFSHObOh_F0P-2_48SqKGiSgKHe58qgkubV253nNRoIHg1N_bXtZ3oQvL1RpeKwi_7Ar4AglR3NTa4emGG6UrlPDbB9ueHGmZkgVr1Pz9IQFDaSYXNV5L9JC7_yJHYnOel7b9YJR0Vh2vDq_i7baC80tqL7jmMgKwOo0aoNkczQTvoXhVNQoPY31lWDRueOJbryi9nNVSKcEkWwzCZgwkFLs2j-uucTDS-G5L4lJiRByNvH5DN16tvbml_bSkTx2MW1lAjAErcLTAZZ4MkMxfbEMkiWhJFoGkq5MGySvG5AdWeICCuLu0C77AORtx8l3WCstfmxS8m3Jft2l_WzoKwZIAi04WzRx5ff8nxV79paR5GtgL5vILrWVTZIc_iuVBvNXNkzimDr1nKPDrrQWW2yaJgN0gp5fNYzMGHZ_wj8yPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6cddf678.mp4?token=Nj7d7rUeaRQE_O_p0xTOYmr9lKVjDNkiypERnZiLwLK2aTWOnEkHYuWCfZQ33ftRdwsjchmYEkDgrXcjNs8mZs0apSkIrnrPZkS7XLnt8F09nR2wZMTFyezoaUi_ST8yp9O6P3_NbmIO30amrOgOkgMIAQdLI7jm7XbYsEEpYG1Rpfcvj4rx1vmSrzwyDL6w3OnQME0jZTuTwysp7kCGlnuhZXuAunDx4BZwxO8aENDmkJm1bCOKSJ2hwlyoiEFSHObOh_F0P-2_48SqKGiSgKHe58qgkubV253nNRoIHg1N_bXtZ3oQvL1RpeKwi_7Ar4AglR3NTa4emGG6UrlPDbB9ueHGmZkgVr1Pz9IQFDaSYXNV5L9JC7_yJHYnOel7b9YJR0Vh2vDq_i7baC80tqL7jmMgKwOo0aoNkczQTvoXhVNQoPY31lWDRueOJbryi9nNVSKcEkWwzCZgwkFLs2j-uucTDS-G5L4lJiRByNvH5DN16tvbml_bSkTx2MW1lAjAErcLTAZZ4MkMxfbEMkiWhJFoGkq5MGySvG5AdWeICCuLu0C77AORtx8l3WCstfmxS8m3Jft2l_WzoKwZIAi04WzRx5ff8nxV79paR5GtgL5vILrWVTZIc_iuVBvNXNkzimDr1nKPDrrQWW2yaJgN0gp5fNYzMGHZ_wj8yPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور هیئت ایرانی در منزل جوان‌ترین شهید مقاومت در بیروت
@Farsna</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/465565" target="_blank">📅 23:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465564">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎥
تصاویری از انفجار داخل نیروگاه حرارتی دمشق  @Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/465564" target="_blank">📅 23:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465563">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc64f223.mp4?token=UQYS3TcMsBf3_CEYrD3ITzGVD2NHX3_nkfrncRcw9S2qKW3SCTW2MHxSK9WwH9jXSxBa-YbGO4xpf5Du0JoghfnCogvJFylqcTQ8TRulYdjv4hEbI7ZIc1qMDAb8XAAj6bU9QfpLO_yQHrHDxWtTsjZykeDru77OVI5actJBn7QZ5A0hFMIHDvd3BT9Y4r7fUuADDPPxWRIKvWcKBpiqQRclzUNdDKakw6LntHfxylgyo02EyFhdkVDuvaQRV-NeVcfGN8o21Ce9_kkOxJBPM6c6Sw3NVdzXnOybTIuCKlJ6WNaVvbe5lgqzc3TaIl117AGrNeX53nQJBqZQFhhk4ji-eR_Rq9d72ttjWMS11yqtZ0PvJLJ00i6JZU_0azuiwaU0ixC1uI0wpD5x0vbpxfuUXqaQk6vRmdxuPU3PYJN3AFXxOtkauuymG30VGm9H1dv-92AByrRzVLvIlUON28OQ9lBr2cHpO2WJFtgSkM40P3aFy0kCgIermxT0W4Un0Rt7ggVX3aFnGLGsGKETPrh3HnvVTlvlo7vW6HRIctSaVhj5ZBA3pa9gKJH76Qex1FwkcE4CJD2HSim0fwNz2lLrE1Rve3JTLlc_AcHI4DPKFBO85Zbl6QY7ajBQjXZnwgz6LXLC4Q2bkGFu0Ec4uKVls0Fls2M4TomKqcJmdUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc64f223.mp4?token=UQYS3TcMsBf3_CEYrD3ITzGVD2NHX3_nkfrncRcw9S2qKW3SCTW2MHxSK9WwH9jXSxBa-YbGO4xpf5Du0JoghfnCogvJFylqcTQ8TRulYdjv4hEbI7ZIc1qMDAb8XAAj6bU9QfpLO_yQHrHDxWtTsjZykeDru77OVI5actJBn7QZ5A0hFMIHDvd3BT9Y4r7fUuADDPPxWRIKvWcKBpiqQRclzUNdDKakw6LntHfxylgyo02EyFhdkVDuvaQRV-NeVcfGN8o21Ce9_kkOxJBPM6c6Sw3NVdzXnOybTIuCKlJ6WNaVvbe5lgqzc3TaIl117AGrNeX53nQJBqZQFhhk4ji-eR_Rq9d72ttjWMS11yqtZ0PvJLJ00i6JZU_0azuiwaU0ixC1uI0wpD5x0vbpxfuUXqaQk6vRmdxuPU3PYJN3AFXxOtkauuymG30VGm9H1dv-92AByrRzVLvIlUON28OQ9lBr2cHpO2WJFtgSkM40P3aFy0kCgIermxT0W4Un0Rt7ggVX3aFnGLGsGKETPrh3HnvVTlvlo7vW6HRIctSaVhj5ZBA3pa9gKJH76Qex1FwkcE4CJD2HSim0fwNz2lLrE1Rve3JTLlc_AcHI4DPKFBO85Zbl6QY7ajBQjXZnwgz6LXLC4Q2bkGFu0Ec4uKVls0Fls2M4TomKqcJmdUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی عربی سعید حدادیان در محل مزار شهید سید حسن نصرالله
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/465563" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465562">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458ec4c8a8.mp4?token=N3OK8TAVyIzuItHEsQhnhYP3muS9YtgGytRt7ZCsQHuv78a0v678_xepeyNLEDibtGxJGmMucdwUOkE2GcoA2z3Grr2nWzXE9KNPud708gbKbDnzC-h-mfYiCmajAzodP16lxaCXbAQwBvVwIvQ9lhVOcfMySnXke7YUDotQlQbkr_GhTuo6cYE7e_IUlkBK0UN1NkBsT5s5yEMUO437w8TpZXObqwPDR6myZiwL-Hbe3EITG3F1xMJtlLiP-Vc7nR1sC-IXp3jD_ypEjRoB5PPzW_EwhJHaBcL_WFUzR84k-y_p8bAsmrbGJ648P4aDBu4sPZYynHFULeJ-UMAShCkKmoGaZxhKCo1Fj4m7z5W4cyaZlbj-o4suIOGMR-hWtvxtICnEeOco491IQi5RDEvFotkRItNTJwNhI9CBhrbvGWXQDy-YK-j39XsUcX5l5Mv1lkPvU6jv5hfOLkwm3-_GlPQZyJBDsvDaKH3Bvb0ldvSpMjkY3jimThE4Qav561CAcErCX_G8Gu26cU1GsmxZcnHpIlNArpa6IYz7nLbE3bghjjVUlGEzWYi6yEmGDz7gwzveICow6YIFvh9wcPqexCmft7WvWMvfqxU0QbaNTlDD9EYwX-F7iJqtrtNG1WchxMQuNS7tnK01AvCd0i5lRtmlSkbiXdOHYa98Qhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458ec4c8a8.mp4?token=N3OK8TAVyIzuItHEsQhnhYP3muS9YtgGytRt7ZCsQHuv78a0v678_xepeyNLEDibtGxJGmMucdwUOkE2GcoA2z3Grr2nWzXE9KNPud708gbKbDnzC-h-mfYiCmajAzodP16lxaCXbAQwBvVwIvQ9lhVOcfMySnXke7YUDotQlQbkr_GhTuo6cYE7e_IUlkBK0UN1NkBsT5s5yEMUO437w8TpZXObqwPDR6myZiwL-Hbe3EITG3F1xMJtlLiP-Vc7nR1sC-IXp3jD_ypEjRoB5PPzW_EwhJHaBcL_WFUzR84k-y_p8bAsmrbGJ648P4aDBu4sPZYynHFULeJ-UMAShCkKmoGaZxhKCo1Fj4m7z5W4cyaZlbj-o4suIOGMR-hWtvxtICnEeOco491IQi5RDEvFotkRItNTJwNhI9CBhrbvGWXQDy-YK-j39XsUcX5l5Mv1lkPvU6jv5hfOLkwm3-_GlPQZyJBDsvDaKH3Bvb0ldvSpMjkY3jimThE4Qav561CAcErCX_G8Gu26cU1GsmxZcnHpIlNArpa6IYz7nLbE3bghjjVUlGEzWYi6yEmGDz7gwzveICow6YIFvh9wcPqexCmft7WvWMvfqxU0QbaNTlDD9EYwX-F7iJqtrtNG1WchxMQuNS7tnK01AvCd0i5lRtmlSkbiXdOHYa98Qhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاشمری‌ها در شب ۲۱۴ باز هم قدرت‌نمایی کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/465562" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465561">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54986f0b91.mp4?token=P7o3sD5I_azaRD1nADbCC4BfKaDgIb8rH6K6onypW1mRz7PZjRygc2MW_A8AYYiasYTwIPFLPVxVl3jDmqJZu1Vf-8EdRhV7BFWKHagTMfTxm2mD3VEXo-qGqePprmYdgUyKq_LJ3Ig4eUGcr6MxTw46YWVcVCndLgFT2ehr_A4t9ZsyJfIwFMCkC8lFxgI5fYYhYii3b6y47P6AKgPRXWu5fhh_EhiM3M4v_YxmkypuL19Gz-u7xs0v2IjiAw08IhyGQSr7uME1AaQkgWXjgZeDW5ScoXhVOIQa5iW1_-BeLzsJNU4fEAYx3Bay6uure8oN9bcpkjYcrTf4FEMAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54986f0b91.mp4?token=P7o3sD5I_azaRD1nADbCC4BfKaDgIb8rH6K6onypW1mRz7PZjRygc2MW_A8AYYiasYTwIPFLPVxVl3jDmqJZu1Vf-8EdRhV7BFWKHagTMfTxm2mD3VEXo-qGqePprmYdgUyKq_LJ3Ig4eUGcr6MxTw46YWVcVCndLgFT2ehr_A4t9ZsyJfIwFMCkC8lFxgI5fYYhYii3b6y47P6AKgPRXWu5fhh_EhiM3M4v_YxmkypuL19Gz-u7xs0v2IjiAw08IhyGQSr7uME1AaQkgWXjgZeDW5ScoXhVOIQa5iW1_-BeLzsJNU4fEAYx3Bay6uure8oN9bcpkjYcrTf4FEMAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار بروجردی‌ها: پرچم خون‌خواهی روی دوشم، وطن نمی‌فروشم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/465561" target="_blank">📅 22:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465560">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6uPKukTV6yHbE-JBvoQRfGYVj23GVjBCO_hASU7Bkmw9bCVV5MVE3C1BPJHT98UQJFcal_TE5a5sS-JqxmEEutNBaE5vw75wU8xnvNNxDFUd8JJRn2bIwQRfRgaRLf_8XKTyK6T1uqPDs09X7NtjAIBdUV6F88acsT3hXw59nirRpXgvZopmcVfysL0QXv364pY5dbFALonV2twtoBOH9fAZSbnXuwoCWxDfNDaqo9Ur1R4BG36PHgPuNlC7tsOKNprsYDR7sKUZIax-0SYb7VGgMPZk2or2Z019vLhu2Qb8MXwDDAxQ4GHIqP433Rt1CRgNIRBpbZ6FKgMWpkIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کتاب نظم جدید جهان اثر محمدصادق شهبازی منتشر شد
🔹
کتاب در نگاهی از بالا به تغییر نظم قدیم جهانی، افول آمریکا، برآمدن قدرت‌های تحول‌خواه، ایران و جبههٔ مقاومت و نظم جدید جهانی می‌پردازد.
🔹
کتاب با بررسی عرصه‌های مختلف سیاسی، اقتصادی، کریدور، انرژی، فناوری، جمعیت و سرمایه انسانی و دینی، زیست‌محیطی، مدیریت دیتا، نظامی، زنجیره‌های تأمین، چالش شناختی/بردگی ذهنی و نبرد رؤیاهای ملی چهارچوبی از تغییر نظم گذشته و عرصه‌های محل نزاع برای شکل دادن نظم جدید جهانی را معرفی میکند.
🔹
کتاب با بررسی ایده‌های رهبر شهید انقلاب در این‌باره و ضرورت‌ها و لوازم نقش‌آفرینی در آن، تلاش کرده مهم‌ترین عرصه‌های محل نزاع که مسئولان و جوانان و...باید نسبت به آن حساسیت داشته باشند طرح کند.
🔹
پیش از این کتاب‌های خودسازی و دیگرسازی، کدام  انتظار؟ انتظار انقلابی یا انحرافی و تشکل دهه پیشرفت  از همین نگارنده منتشر شده بود.
🔗
این کتاب را می‌تواید از
اینجا
تهیه کنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/465560" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465559">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOTxxe5s8UMQdFmOd_NavedvljN8UTXnt6Fmy4NfjBq20aHvxS8_k4IWgm81zKRkZk0BNKUhhVUW8CVtkXElwb8Z55IdG1dP1OsoyspLJvyzmfe1vMl4ie4pohxbqM2t-Io_Fkp8ODUErVBc4JIV1vNafFZg9y3Np074Fbg_bBxE4p7e9XnwrmdVLI9GWZTJz9T11AFiwcoYm5nmOm8OKBHCbbV0IXrDSuLXMElFHwVvX8nCDqFRLKlZkHlfDzAhYlGLe1qZgCC0yVRXTdOJCEbm77T2AJiu3SfXYwUHYeF__buj98lmbNgZUyeNjowV8WalyoPJp9lsZmyVB_VDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور امنیت ملی پیشین آمریکا: ایران تسلیم نمی‌شود
🔹
سالیوان، مشاور امنیت ملی پیشین آمریکا: تهران تسلیم نخواهد شد و ادامه وضعیت موجود، ضمن بی‌ثبات نگه داشتن شرایط، هزینه سنگینی برای آمریکا به همراه دارد.
🔹
باید این جنگ را پایان دهیم، دور آن خط بکشیم و بعد ببینیم چگونه می‌توانیم راهبردی را برای پیشبرد دوباره منافع آمریکا تدوین کنیم.
🔹
می‌دانم که اکنون نفت بیشتری خارج می‌شود و می‌دانم که ما عملاً نفت ایران را محاصره کرده‌ایم. اما معتقدم این شاخص‌های سطحی، چالش اساسی را حل نمی‌کنند. چالشی که این است که ایران تسلیم نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/465559" target="_blank">📅 22:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465558">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb259f096.mp4?token=sJd7OxLoCqDxouAW22KiX75d_DaO6evPvX6k9roPlKorOhFMJLoDzKrsPvw-nVO7ZpTh0gAxYgpBRGhMp82loM-vOLQ_zjAhqzfflns4mFG11fl6RYV48EhpZw1kq8i0KB_wI6h3v_jG1qXOjrV4McBwLMCzIL6xlBhUlRWazY8LEjMvfyKzRqGpp2Yy03doIpj8SFjxQOTofgEUT8HKPpL4D_yVfqUDXaqB2XtzoZEBtG1dp4OFiEchKdRECp1CntiN6Uy1NSiX_faI1_9Ci3X-bkyGUdyvSXYTrT-HXPOwG9GvPKD3gdk8KrG2hH1BtjDnWYaB_nU4hGEzotWPeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb259f096.mp4?token=sJd7OxLoCqDxouAW22KiX75d_DaO6evPvX6k9roPlKorOhFMJLoDzKrsPvw-nVO7ZpTh0gAxYgpBRGhMp82loM-vOLQ_zjAhqzfflns4mFG11fl6RYV48EhpZw1kq8i0KB_wI6h3v_jG1qXOjrV4McBwLMCzIL6xlBhUlRWazY8LEjMvfyKzRqGpp2Yy03doIpj8SFjxQOTofgEUT8HKPpL4D_yVfqUDXaqB2XtzoZEBtG1dp4OFiEchKdRECp1CntiN6Uy1NSiX_faI1_9Ci3X-bkyGUdyvSXYTrT-HXPOwG9GvPKD3gdk8KrG2hH1BtjDnWYaB_nU4hGEzotWPeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: مردم آمریکا فکر کنند که چه چیزی باعث شده ۴۸ سال آمریکا و رژیم صهیونیستی از ما شکست بخورند؟
🔹
آمریکا که بودجهٔ نظامی‌اش ۱۰۰ برابر بیشتر از ماست و رژیم صهیونیستی که مدعی قدرت چهارم جهان است، چرا با این همه امکانات شکست خورده است. @Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/465558" target="_blank">📅 22:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465557">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b9c1b7bd.mp4?token=JPMKcCGK__JZ9YBtRPrPvPhh9qF_SB6O6gVCiBwPJTfMrgZHxr5PcSikn0IOg5T6eSm3oVc7HaT5anYebZNrciZ84fUma4EsRY7MPjmGZla18umJ3kx4K43YjgU_79HpdQtyo-8EFB0PJYKFCk_lll75wsBg4U6c7E_-lclKngpdzboQBeUWwMpaqIl8kQRjxi_KfEw1RJZXZqK1booSYykvZ-RCDDrYSWAivJvWIUWrPNyBEQzXFJnnzxApwGZ3nt1MrZKO6vGffzo0Ww4hQCfzJZG9V5LcwR_MpjIDEYdnPCNJrJYUX7_X-mhKXZburQSJxxzxy2qkUX8a_-aQyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b9c1b7bd.mp4?token=JPMKcCGK__JZ9YBtRPrPvPhh9qF_SB6O6gVCiBwPJTfMrgZHxr5PcSikn0IOg5T6eSm3oVc7HaT5anYebZNrciZ84fUma4EsRY7MPjmGZla18umJ3kx4K43YjgU_79HpdQtyo-8EFB0PJYKFCk_lll75wsBg4U6c7E_-lclKngpdzboQBeUWwMpaqIl8kQRjxi_KfEw1RJZXZqK1booSYykvZ-RCDDrYSWAivJvWIUWrPNyBEQzXFJnnzxApwGZ3nt1MrZKO6vGffzo0Ww4hQCfzJZG9V5LcwR_MpjIDEYdnPCNJrJYUX7_X-mhKXZburQSJxxzxy2qkUX8a_-aQyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔹
بنا به اعلام برخی منابع رسانه‌ای، تصاویر فوق مربوط به انفجار خط لولهٔ گاز به فرودگاه حرارتی تشرین در نزدیکی فرودگاه بین‌المللی دمشق است‌. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465557" target="_blank">📅 22:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465556">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
منابع عربی از وقوع انفجار در فرودگاه بین‌المللی دمشق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465556" target="_blank">📅 22:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465555">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f525e09ca4.mp4?token=XWIGFhNEdkAP1F-jJmn93889BpQJcaFN5raDGLzL2nsd2Ov5bGJ4qnIf1gh5tPvuouiNo5sJv8qAEsX4fE6ZyIyyVg1F0nOFVUF2J7WRrpfgXS5GXjxNf7KYOkeRhdcjJde7tdBzqUsaaYAga89MTC-HJlsHeKsEvGTOxQUyawGI-Vt2U5afKFmVerbjxTS9W3YKpEDsRCXjEbDwzT1ewkRzA3-pLmKIp9m-zEimiSm7jLAQz5BaVXQw33CPC8g0p_7YbfW4ADdiAEPBR8uXEWWOXfH-CKlLVLsm3YMXRsSnN71v7KLLOTsIPjMB3KtBkk015qThRuSUy0VCVq2L8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f525e09ca4.mp4?token=XWIGFhNEdkAP1F-jJmn93889BpQJcaFN5raDGLzL2nsd2Ov5bGJ4qnIf1gh5tPvuouiNo5sJv8qAEsX4fE6ZyIyyVg1F0nOFVUF2J7WRrpfgXS5GXjxNf7KYOkeRhdcjJde7tdBzqUsaaYAga89MTC-HJlsHeKsEvGTOxQUyawGI-Vt2U5afKFmVerbjxTS9W3YKpEDsRCXjEbDwzT1ewkRzA3-pLmKIp9m-zEimiSm7jLAQz5BaVXQw33CPC8g0p_7YbfW4ADdiAEPBR8uXEWWOXfH-CKlLVLsm3YMXRsSnN71v7KLLOTsIPjMB3KtBkk015qThRuSUy0VCVq2L8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: مردم آمریکا فکر کنند که چه چیزی باعث شده ۴۸ سال آمریکا و رژیم صهیونیستی از ما شکست بخورند؟
🔹
آمریکا که بودجهٔ نظامی‌اش ۱۰۰ برابر بیشتر از ماست و رژیم صهیونیستی که مدعی قدرت چهارم جهان است، چرا با این همه امکانات شکست خورده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465555" target="_blank">📅 22:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام رهبر انقلاب به سی‌وسومین اجلاس سراسری نماز، صبح فردا همزمان با قرائت در محل برگزاری این اجلاس در حرم مطهر رضوی، منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/465554" target="_blank">📅 22:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465553">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a3b4e4b7.mp4?token=gNewoZ-nZ6hKVdghEGQy_L56Ey6udfdfN_QgJeCySypxa2ZRmCrG7eT5qhJuk3l4jTPwyzpQ1TXurkzZi89DyqDhwVFaj4joIdu8ODHp_l3h8PimVyljOWJXgkCXofdaLLA-66A2i90J_96M_C6uVPXfHPsjTXTJW9XwnwZKZOVP_5RMUG3Ts-MkMtKXJH_ydq8_ygTtyKcDIUdM5FzVt4l6C0szw6-zhpMkNEb3xLLMR3hiZxgSj4qCs0qsjH8nMIa5yuylgHwlWoehxUm5o1PS8Zq1E-dLTFgqd9w6C-0GasQeE2qru1h1g5p5nxtpJKReHVuDJVfGWsRf5g9Ryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a3b4e4b7.mp4?token=gNewoZ-nZ6hKVdghEGQy_L56Ey6udfdfN_QgJeCySypxa2ZRmCrG7eT5qhJuk3l4jTPwyzpQ1TXurkzZi89DyqDhwVFaj4joIdu8ODHp_l3h8PimVyljOWJXgkCXofdaLLA-66A2i90J_96M_C6uVPXfHPsjTXTJW9XwnwZKZOVP_5RMUG3Ts-MkMtKXJH_ydq8_ygTtyKcDIUdM5FzVt4l6C0szw6-zhpMkNEb3xLLMR3hiZxgSj4qCs0qsjH8nMIa5yuylgHwlWoehxUm5o1PS8Zq1E-dLTFgqd9w6C-0GasQeE2qru1h1g5p5nxtpJKReHVuDJVfGWsRf5g9Ryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی از وقوع انفجار در فرودگاه بین‌المللی دمشق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465553" target="_blank">📅 21:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465552">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd0fdb7957.mp4?token=i0bpyRzTezWT8vPnVeq5NT7dibEj5MaeFk6HkcXfrj9DrA-R4zkmbgpFzrAj15m5i3rwjQGfD7y1aGY3VmBNbNG9uGJudo8J77fpJi7fN4nyKTHHbKAxNF3z2TxKTq-bfdtNcEPMYfwyst1nwUVaMwqgfwMKD93ej4GzrB7p2Ukzi0lYcceJtO20RVqfmHf2wtc1fC6y42UEdND7thJ8mzhd96AWI-BwG0pX63s6riaJUl3_FcxI4WAv9sJuTuad-LiNLF3fdkuD7Jkah2FlEnQ8xSlZmsJjI7_8AQmtF1WebmUEO5l90loRhLEYNDM-C6RTgYBmts-o53t2qgHAdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd0fdb7957.mp4?token=i0bpyRzTezWT8vPnVeq5NT7dibEj5MaeFk6HkcXfrj9DrA-R4zkmbgpFzrAj15m5i3rwjQGfD7y1aGY3VmBNbNG9uGJudo8J77fpJi7fN4nyKTHHbKAxNF3z2TxKTq-bfdtNcEPMYfwyst1nwUVaMwqgfwMKD93ej4GzrB7p2Ukzi0lYcceJtO20RVqfmHf2wtc1fC6y42UEdND7thJ8mzhd96AWI-BwG0pX63s6riaJUl3_FcxI4WAv9sJuTuad-LiNLF3fdkuD7Jkah2FlEnQ8xSlZmsJjI7_8AQmtF1WebmUEO5l90loRhLEYNDM-C6RTgYBmts-o53t2qgHAdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: الزیدی شانس نداشت با حمایت من نخست‌وزیر عراق شد
🔹
رئیس‌جمهور آمریکا: مهم‌تر از همه اینکه ما عراق را ترک می‌کنیم، در حالی که این کشور نخست‌وزیر جدید و فوق‌العاده‌ای به نام علی الزیدی دارد؛ مردی فوق‌العاده و دوست من که من از همان ابتدا از او حمایت کردم و حمایت کامل خود را از او اعلام کردم.
🔸
او در انتخابات نامزد شده بود، اما حتی فرصتی برای مطرح شدن به او داده نمی‌شد.
🔹
من در عرصه سیاسی تا حدی از او حمایت کردم و در نهایت، او با پیروزی‌ای قاطع، تقریباً به‌صورت یک پیروزی بزرگ، بر فردی غلبه کرد که از نظر من آدم خوبی نبود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465552" target="_blank">📅 21:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465551">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53baaadb89.mp4?token=W3uPnV5582Y2YpdjW_qZoEe8kXcCVPlQ2duT4oSztZrbOUrDu_r4ZyBnY9VWdWrSNk-d3fnfkCKIQga5-V7vO7Gyib4-XZnkC-uUGlktKLKiZ9pKYr810-f0cc7ikshWgNcU-hKy4ReWSZLbD9xNJyYxWtloYc4Q7URI66lnmIVKbJUB3LRl-eivY5DfrPTSDFzvQbUfs8Su03YIb0gOog5dADJzj5ku0o1EcsGQH_cEgpXm-ax2Iv58hQRBf8b2VSFYKt8csJxQrlcEbFAMNZRzfcnMdu7SOx40kvhFl9UEqtZ33OsSitEaDbIbSd3DgzFo0ujc4aleksjzBgy3AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53baaadb89.mp4?token=W3uPnV5582Y2YpdjW_qZoEe8kXcCVPlQ2duT4oSztZrbOUrDu_r4ZyBnY9VWdWrSNk-d3fnfkCKIQga5-V7vO7Gyib4-XZnkC-uUGlktKLKiZ9pKYr810-f0cc7ikshWgNcU-hKy4ReWSZLbD9xNJyYxWtloYc4Q7URI66lnmIVKbJUB3LRl-eivY5DfrPTSDFzvQbUfs8Su03YIb0gOog5dADJzj5ku0o1EcsGQH_cEgpXm-ax2Iv58hQRBf8b2VSFYKt8csJxQrlcEbFAMNZRzfcnMdu7SOx40kvhFl9UEqtZ33OsSitEaDbIbSd3DgzFo0ujc4aleksjzBgy3AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما ۶ ماه است که در جنگ با ایران هستیم؛ آن‌ها ۴۵۰۰ کشته داشته‌اند و ما ۱۸ تا.
🔹
این ادعا درحالی مطرح شده که کارشناسان و ناظران اذعان دارند آمریکا آمار واقعی تلفات و خسارت‌های خود را به‌شدت سانسور می‌کند و اخبار آن را به‌صورت قطره‌چکانی و با پنهان‌کاری…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465551" target="_blank">📅 21:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465550">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5977566b.mp4?token=MJqhY6JJSiUq8p32oVBkp3AU3bqlVCfzSekvTYUuiv7-uGxHf_aqQjLLQkOESdgt5TO5sz4mpMl9mknMmRznUQ7PiD7tpGNYfkWODYc5MsxyqWVKBLjP62w_sQQ7qGSh2yroWmjM5Lh6rpWejouLQPMCOvMCGosCtYcMPIlyDuY59pAEJb7QLv-_c7pl8MZLNo3NP-89YM_yBnkUZZkytyA9ZTl_MVAXSzw2JxEz-BRbt2nrtYXa2R-g0O69AOInkKDP5SYLkuN4TtG2uXr5vDndry14dp_gbX_rbkrd8cZxCoIBZyE7v3REdQgxsbYWtXf_FUPGnkt-pO0mW-AAKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5977566b.mp4?token=MJqhY6JJSiUq8p32oVBkp3AU3bqlVCfzSekvTYUuiv7-uGxHf_aqQjLLQkOESdgt5TO5sz4mpMl9mknMmRznUQ7PiD7tpGNYfkWODYc5MsxyqWVKBLjP62w_sQQ7qGSh2yroWmjM5Lh6rpWejouLQPMCOvMCGosCtYcMPIlyDuY59pAEJb7QLv-_c7pl8MZLNo3NP-89YM_yBnkUZZkytyA9ZTl_MVAXSzw2JxEz-BRbt2nrtYXa2R-g0O69AOInkKDP5SYLkuN4TtG2uXr5vDndry14dp_gbX_rbkrd8cZxCoIBZyE7v3REdQgxsbYWtXf_FUPGnkt-pO0mW-AAKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما ۶ ماه است که در جنگ با ایران هستیم؛ آن‌ها ۴۵۰۰ کشته داشته‌اند و ما ۱۸ تا.
🔹
این ادعا درحالی مطرح شده که کارشناسان و ناظران اذعان دارند آمریکا آمار واقعی تلفات و خسارت‌های خود را به‌شدت سانسور می‌کند و اخبار آن را به‌صورت قطره‌چکانی و با پنهان‌کاری منتشر می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465550" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465549">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P51mb_P4X41CpgXKymsf1WzXv4zkzkkgsLjWvBWEIKSYXSkLB_2rLDVSmSnxHiNQOkW-7k2wPFmz7dqLUO0Uq2rUYAYl2rsQ8qFuCy9zC64SwKuHxMAkg1KvLT4uIliT0LwxDhZouXL10tCzv-KzQ5sKDR2IqZ4x_Qc5wZPVFgfl3aqRAzdfUvrKJVCV1a7-lFlBffXhFc_lmdVgEWQgvOkiZufVo7WbtZo3gOCYV_FLLeRjRZ9iV4EMVcczkHY9vcuhDYowopNIrRQaY-9PfFFWKGurndWBlkePCSLLl_RkH62XrYpGEefZqOIxDyOyoihIug-d1eYx077hDCwY6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف در پاسخ به گستاخی‌ اخیر بسنت فرمول اقتصادی جدیدی منتشر کرد؛ اهرم‌های فشار ایران بر اقتصاد آمریکا
🔹
محمدباقر قالیباف در پاسخ به لفاظی‌های اخیر اسکات بسنت وزیر خزانه‌داری آمریکا که مدعی فروپاشی اقتصاد ایران ظرف دو هفته آینده شده بود، توضیحاتی درباره اهرم‌های فشار ایران بر اقتصاد آمریکا ارائه کرد.
🔹
قالیباف در پست خود در حساب شخصی‌اش در شبکه ایکس در شرح وضعیت شکنندهٔ بسنت نوشت که دولت آمریکا در گذشته وام‌های زیادی با نرخ بهره نزدیک به صفر گرفته بود. حالا موعد پرداخت این وام‌ها رسیده و دولت مجبور است برای تسویه آن‌ها، دوباره وام‌های جدید با نرخ بهرهٔ بسیار بالاتر بگیرد.
🔹
از طرفی توان و ظرفیت خریداران اوراق قرضه هم پیوسته در حال کاهش است. برای مثال خریداران بزرگ اوراق قرضه آمریکا (مانند چین و ژاپن) علاقه کمتری به خرید اوراق جدید و یا نگه داشتن اوراق قبلی نشان می‌دهند و به همین دلیل نرخ بازده اوراق رو به افزایش است.
🔹
قالیباف به بسنت گوشزد کرده است که نقش ایران در بسته نگه داشتن تنگهٔ هرمز و بالا نگه داشتن قیمت انرژی و همچنین اثر‌گذاری بر افزایش بازده اوراق قرضه، خزانه‌داری آمریکا را با بحران فزاینده روبرو کرده و تمام دردسرهای او را تشدید ساخته است؛ به عبارتی آمریکایی‌ها تا حل این مسائل از طریق احترام به حقوق ملت ایران، توان غلبه بر این مشکلات اقتصادی را نخواهند داشت.
🔹
نرخ بهره اوراق ۳۰ ساله دولت امریکا روز گذشته به بالاترین نرخ از سال ۲۰۰۲ رسید و با روند فعلی احتمال برگشت به نرخ های سال‌های ۱۹۹۰ و قبل وجود دارد.
🔹
قالیباف همچنین در پست خود از تصویر David Zervos مشاور جدید بسنت که روز گذشته منصوب شده هم استفاده کرده است. او به زدن حرف‌های عجیب و غریب معروف است. برای مثال، او سالها پیش ادعا کرده بود که از اصلاح موی سر و صورت خود تا کاهش نرخ بهره توسط فدرال رزرو پرهیز خواهد کرد! انتصاب زروس به عنوان مشاور بسنت، دستمایهٔ طنز و استهزا توسط فعالان بازارهای مالی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465549" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465548">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7c192ff2.mp4?token=ge-m30W2Upqo3R0uQ6fTJmCulMHgucaZekITtt-fyhXdjtGdRAnzI7QGEbMww1BlGjHSu3KyY-hGj5OY5bCx12DpmVaZoCHeUTh7bKRB_A5-7Udi3RGd3A7pSXG1yAVUUsjRwBXw43jpJX5v5HW-yl6xunso_BVEdciJMYDd9thX1oEaW79nF2ghLSaP0pl1ASmou0N9TDqPHEp51Rv7gv1VZpu4naBs0j5Z9DHOu1DPqjVu9YCnRaPBgRyAcH3gsy52RUiePpEofGql9OHl2EK6AJCBpQhAG7ThZP5AbaaqL6D3ja4yOns-GRhrZ7qowHMVQcYb2pKjnmxn_-arnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7c192ff2.mp4?token=ge-m30W2Upqo3R0uQ6fTJmCulMHgucaZekITtt-fyhXdjtGdRAnzI7QGEbMww1BlGjHSu3KyY-hGj5OY5bCx12DpmVaZoCHeUTh7bKRB_A5-7Udi3RGd3A7pSXG1yAVUUsjRwBXw43jpJX5v5HW-yl6xunso_BVEdciJMYDd9thX1oEaW79nF2ghLSaP0pl1ASmou0N9TDqPHEp51Rv7gv1VZpu4naBs0j5Z9DHOu1DPqjVu9YCnRaPBgRyAcH3gsy52RUiePpEofGql9OHl2EK6AJCBpQhAG7ThZP5AbaaqL6D3ja4yOns-GRhrZ7qowHMVQcYb2pKjnmxn_-arnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادهای ایرانی؛ تلفیق مرگبار هوش مصنوعی، رادارگریزی و دانش بومی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465548" target="_blank">📅 21:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465547">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-mMJu6PeWHu6kRf4EgR4F0h_nVHkveyMMeNqn9LT5PyFJcq2YksSQPgIelV_AB52ItmFtYKXKgnVO64rM_R4M9MOirvm5YMt3HNyhsxA9GWT967n4VH9w0vxVYq28XAUbaO5ic2d3Vi_JFcPEqGr4wdEdPjE7er2AbdaG_09b_8GpNLwNTVEgNxqvsmrlaA7K01oNm7rO-N-SPaiwYeex3932la_cTmZ2c2DLn6l7AXurC_4gaDFxEba2vpVWXqIGDiItFbs238P_94K5qGeV1yE7He-ELkEUoxoC50RydcNA_TpWdTGtarX0awXtT207AdhUhLdYLRLvD5Gh_m7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از عراق نرفت؛ فقط شکل حضورش را تغییر داد
🔹
با وجود ادعای پایان مأموریت ائتلاف آمریکایی در عراق، تداوم حضور نیروها، تجهیزات و همکاری‌های اطلاعاتی نشان می‌دهد واشنگتن صرفاً شکل حضور نظامی خود در این کشور را تغییر داده است.
🔸
علی الزیدی، نخست‌وزیر عراق،…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465547" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465546">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/481095a354.mp4?token=NvyB4LexxN9FNtvtOFkDDkKDgs2dkYJy4PRz4_sl312Zgjv8h0gI9S8VKdEKcXc4pu-Gm8bREGUqmVU7lvwsvTjYuUwwyDvBKqtWvNeUScf_WsmpD-ySfckFF9zyxllVGqWUIF4cO_Nn4T6sUJ0AjoovgLk3l_PnPCOzaxWT5yDpIGzqTDrvTDSLzBxVniJo43xvyq_535uO8MMAFiAeNyOCBSTXD7iMXqKQNA1RjVHCLqyK3JRvBzzmemB27N01HSxTpgAbz7sme1U2XutIYeOBJGX_suc4ZEIoJKN4qDYosvIL11A0M-GbZ2rWHNMqhR-VCm8uU6S57UJb914cpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/481095a354.mp4?token=NvyB4LexxN9FNtvtOFkDDkKDgs2dkYJy4PRz4_sl312Zgjv8h0gI9S8VKdEKcXc4pu-Gm8bREGUqmVU7lvwsvTjYuUwwyDvBKqtWvNeUScf_WsmpD-ySfckFF9zyxllVGqWUIF4cO_Nn4T6sUJ0AjoovgLk3l_PnPCOzaxWT5yDpIGzqTDrvTDSLzBxVniJo43xvyq_535uO8MMAFiAeNyOCBSTXD7iMXqKQNA1RjVHCLqyK3JRvBzzmemB27N01HSxTpgAbz7sme1U2XutIYeOBJGX_suc4ZEIoJKN4qDYosvIL11A0M-GbZ2rWHNMqhR-VCm8uU6S57UJb914cpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاسبان خون چگونه جاده‌صاف‌کنِ جنایت متجاوزان به ایران شدند؟
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/465546" target="_blank">📅 21:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465545">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c793a1b7.mp4?token=Gk2ZFbZwPdDrOQUZ-5Gzs6_uJsO4xJpaQy7_WS1MIIOt_V7PLLymTaH42xeHMnArC2P_TgjWpcVp00I0tF746IURoQVhOViGjql7zfm97L6XelUUHvYORqrY1XVO3BH-7CuddyeLU1FSxDczP1CF28vxvW9tVkNOWHrTt3EqpQfhIV9fynCNPGiJAjAQULBm-h_DGYG3P4fbiK9bNOQ9qdulfuHjHE84LfQiR-lgE49gHL6xn27qRjkott_4ka2-7k6URkL-hyoXDP2BCcadXvrLh7R1u2a8iG9TDDVMHlQ31D85G-w5Oo2iG0B5yxZ0aTYnEdO-Q6oNHQ2P4RbnKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c793a1b7.mp4?token=Gk2ZFbZwPdDrOQUZ-5Gzs6_uJsO4xJpaQy7_WS1MIIOt_V7PLLymTaH42xeHMnArC2P_TgjWpcVp00I0tF746IURoQVhOViGjql7zfm97L6XelUUHvYORqrY1XVO3BH-7CuddyeLU1FSxDczP1CF28vxvW9tVkNOWHrTt3EqpQfhIV9fynCNPGiJAjAQULBm-h_DGYG3P4fbiK9bNOQ9qdulfuHjHE84LfQiR-lgE49gHL6xn27qRjkott_4ka2-7k6URkL-hyoXDP2BCcadXvrLh7R1u2a8iG9TDDVMHlQ31D85G-w5Oo2iG0B5yxZ0aTYnEdO-Q6oNHQ2P4RbnKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عراقی از هدف‌قرارگرفتن مقر گروهک‌های تجزیه‌طلب در کوی‌سنجقِ اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465545" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465544">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c651ef6ac.mp4?token=Kzo7nHH51rmfr4Ritoo-mc2phWRGWtyAsgXwnz7ZFLtwywtM-Ophl9wUSDBnfb7975uz8Uv4g8Ro6NzS8SBwJKZdb_z3lTPogrfu0k4JPYONYQeaQ_WEQu_08h8MhYD5mprhNUQRoVgXQFfxNKfss24cSg7GG3H0goRRVVwi1RUKNH1yIX_bEkcOXzlQrk9B5quSFTClQAKvUWkgQqEoEqeAUYQLKMfX1l3bVFZjygpr1cgQZURn8SsmK9DRyn1lyYZUkfuanoXunIjl-JJNgpyfy2UsGA6Oz_JDvdlOCmelE3ta4jNQUDx3oj6knYn6uBc1aXtP51Kk0tiHKdslTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c651ef6ac.mp4?token=Kzo7nHH51rmfr4Ritoo-mc2phWRGWtyAsgXwnz7ZFLtwywtM-Ophl9wUSDBnfb7975uz8Uv4g8Ro6NzS8SBwJKZdb_z3lTPogrfu0k4JPYONYQeaQ_WEQu_08h8MhYD5mprhNUQRoVgXQFfxNKfss24cSg7GG3H0goRRVVwi1RUKNH1yIX_bEkcOXzlQrk9B5quSFTClQAKvUWkgQqEoEqeAUYQLKMfX1l3bVFZjygpr1cgQZURn8SsmK9DRyn1lyYZUkfuanoXunIjl-JJNgpyfy2UsGA6Oz_JDvdlOCmelE3ta4jNQUDx3oj6knYn6uBc1aXtP51Kk0tiHKdslTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعدام ۲ عامل شهادت نیروهای امنیتی در مشهد
🔹
علی همتی و مجید نیک‌اندیش، از عوامل میدانی اغتشاشات ۱۸ دی‌ماه ۱۴۰۴ در منطقه طبرسی مشهد که به شهادت ۴ نفر از نیروهای حافظ امنیت منجر شد، پس از تأیید حکم در دیوان عالی کشور و طی روال قانونی، بامداد امروز اعدام شدند.…</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/465544" target="_blank">📅 21:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465543">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50adff3b4.mp4?token=KnzstAetKE9lCAEPWzvlYPwdMGoIC0DNRGukchGrZ7HbbsB0sBmvPyt2gdibQuCV9LykAJSpZox6hn8qTo0hpIfhFHoqFENs5zcldGuLi64bAJLVx_KD0SS5cXyvVOgzqbryObxuSXf1Vpbc7BADHlP9B1SGWpHixSJqp3jO3JkGDRi_38hjDk9I7NJGFPx93A9bvHJFxQF1TAO1738bWnV8mRaQK45GyxOjNbJGkXOEAmEzmaLbTc9UMrk36mZDsXckN-YQc8p9uey-OcA1z3B9D9ztORPzadVg7Z3NRitvqLiyr-sobyK-dX-C0IEC0Gp6ajLnd7ljlhrZHoIfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50adff3b4.mp4?token=KnzstAetKE9lCAEPWzvlYPwdMGoIC0DNRGukchGrZ7HbbsB0sBmvPyt2gdibQuCV9LykAJSpZox6hn8qTo0hpIfhFHoqFENs5zcldGuLi64bAJLVx_KD0SS5cXyvVOgzqbryObxuSXf1Vpbc7BADHlP9B1SGWpHixSJqp3jO3JkGDRi_38hjDk9I7NJGFPx93A9bvHJFxQF1TAO1738bWnV8mRaQK45GyxOjNbJGkXOEAmEzmaLbTc9UMrk36mZDsXckN-YQc8p9uey-OcA1z3B9D9ztORPzadVg7Z3NRitvqLiyr-sobyK-dX-C0IEC0Gp6ajLnd7ljlhrZHoIfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: گاهی به اشتباه گفته می‌شود که قاضی زن نداریم؛ درحالی‌که اکنون برخی بانوان قاضی هستند و رأی صادر می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465543" target="_blank">📅 20:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465542">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190e86fd1e.mp4?token=Mfr8FDRmtulQGTMDP_4LKpWV-8LkUKrziV_7r7s319NWv9BmWhLHE-ZFJMQ_XC7xMZHt3QHriHWAxew_AjYA2pD6A3iipV80_Ss_5D-G8o6YrQ9UXgDDgKwQJGzbVzVNE3TX-R5D6HfWVv7XeNUHNNFOKYELvKJA4LezYNNKyiliVTrJpBSw8iTNigWUSsPm1doBnZMHBy78pBFfeMb9YbGJD2a9bmOTgHJ0mpH9UVwMb1MI5l6fgWiSp9xT956c3ZVjPyoSB1DBW7CdBCiFZ7BztJtH2jvmlydu_OQaDycxLGBmP4XGI0E_374gDi3kaomcpDUDMK1EYpAkU7DttjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190e86fd1e.mp4?token=Mfr8FDRmtulQGTMDP_4LKpWV-8LkUKrziV_7r7s319NWv9BmWhLHE-ZFJMQ_XC7xMZHt3QHriHWAxew_AjYA2pD6A3iipV80_Ss_5D-G8o6YrQ9UXgDDgKwQJGzbVzVNE3TX-R5D6HfWVv7XeNUHNNFOKYELvKJA4LezYNNKyiliVTrJpBSw8iTNigWUSsPm1doBnZMHBy78pBFfeMb9YbGJD2a9bmOTgHJ0mpH9UVwMb1MI5l6fgWiSp9xT956c3ZVjPyoSB1DBW7CdBCiFZ7BztJtH2jvmlydu_OQaDycxLGBmP4XGI0E_374gDi3kaomcpDUDMK1EYpAkU7DttjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شبی که خیابان‌ها روایتگرِ یک نامه شد
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/465542" target="_blank">📅 20:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465541">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d25557e7.mp4?token=IwQUQyAzWnjunUV2PUygcUV1oatp3nPNUAxZYk-FtU9Aer2kOoUgrunpf6LsfGAZpv5AOnTiHlc49E9d_6BGgN5IZaMlDjH2rMUFvoCSbBo7MF52drmt6txiQUepjwp5oOuJKK_CfO2Ta8rSWImePDGKBGBjQEEDwEYfZuOq7QjagGNH7rPNHColRJUujaNHjIvciDffHny0Tt0ca94X85eUvi2NGuOZm_pDCcHd2MNusjrirQ9rdWtKsIst8HKW9R0iCPkopzz8z37OiIMDMLdYixjpF9SrzUgnCqltUPXpDQ9heF8e3-c_8aw38FCCoXYIJbBa1omN2gnDBlraNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d25557e7.mp4?token=IwQUQyAzWnjunUV2PUygcUV1oatp3nPNUAxZYk-FtU9Aer2kOoUgrunpf6LsfGAZpv5AOnTiHlc49E9d_6BGgN5IZaMlDjH2rMUFvoCSbBo7MF52drmt6txiQUepjwp5oOuJKK_CfO2Ta8rSWImePDGKBGBjQEEDwEYfZuOq7QjagGNH7rPNHColRJUujaNHjIvciDffHny0Tt0ca94X85eUvi2NGuOZm_pDCcHd2MNusjrirQ9rdWtKsIst8HKW9R0iCPkopzz8z37OiIMDMLdYixjpF9SrzUgnCqltUPXpDQ9heF8e3-c_8aw38FCCoXYIJbBa1omN2gnDBlraNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: برخی قیمت‌ها در بازار اصلا قابل توجیه نیست؛ بازرسی‌ها متمرکز و شدیدتر می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465541" target="_blank">📅 20:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465540">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJjr_bTzztG9faPJX8gXRH-bcRwBg98Y0Hf32m7LTrGVTFGyhke0MrVb1OJklHusumCxCHMXF8R7vIvXdyMW8W6mALLqjyMs2QW8QSuTv1dw4u8NtZVNZRKMSIM30ptMLur-FBzKSoAf8g9y0GPtSUpP1uvHudwuy1kIo-ILoVGZKn9sTEO-ZM2cGory-HEFVBFELqw_UpChBuGgs5rn_hrdXKuP9B_po3PnMG-y0GfMJaLftfNrkpMWeMb_HDtep8Pjp2dgmBIC41kMWriwX7zXxfIVrxZMHSjW62oWnu8iLWEpvU4_FNHs77_KYaxDL5KkjGTm4IgEbLuLby8eeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس امنیت هوانوردی اروپا: آسمان ۶ کشور عربی خطرناک است
🔹
آژانس امنیت هوانوردی اروپا هشدار خود به شرکت‌های هواپیمایی را برای پرهیز از پرواز بر فراز آب‌های خلیج فارس در محدودهٔ بحرین، کویت، قطر، امارات، عمان و عربستان سعودی تا ۱۶ نوامبر تمدید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465540" target="_blank">📅 20:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465530">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbyDCpbJNwoxK523Zpm90WKw9QV8_AbSZX59WvCdxKx9-PRcjmYHd0-QPEpTzcP3GDC-wPVZ_Uigo6Ja9Uz3vbemXdFq9FofPkVe3CQScUwxPfU1Wowf6ebybCn5vR9hCBkD0xEyNThh0Ci-3t2Wd4fBznELFrzP5Y16AJZeNgLx23miHUpq_-sc0bV8xNrhr77qrpxf6pXzqoZlxepl_97Ft6cvLSsduFSmiLpj6OLWV9S78forh7rJAXZiHxTsWQr5eVvvRl5opPXhA3CYw-DTdbjqcgBeyohswifnJZkO87Zn0wniGwi1SoV83Zv9El4XCfftY_S-ZHBKM9ZUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZZfs0s05Q3tvbwqh5hxxvsDvSxag2rQyefbyXYAQS-Bu8bc_FlRKBAw6L_R1r42m5Za8rhwAqDVZFP0A9w-KcxeLFe1KMTPdMDxGU4oxSbQzdzfCJnYO5fFsupUvT6uFWWTXo3KXR2vnR-v1M5Fbxh8vDinHKSEFGm9XvSP8Lk92KwPL053IgLTqvZwb9SDwh9-_4Ft-5edhXsYAOtTqSczrSs93KX8VPPLEGBLd7DPjkexbcYLdU3jva3lpIUMcPku6Gb0MSsq3FXFbcLGxtUKSjlyRx1UGFVuhhG1icHVI6aMlwDJDQhkUvHkJayVJFdO33jqbtZc0SrXqMbppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmFuDwqM3NLafiODIXUpBFEUerzfAUrg7NoIsOVAZrj03wBARnaXMmDy1iZ-0kW9cGrOo3FNbb5t-C4MqrWJkK1DI_N91agc6HlBaIaNLQUQai3jRGRHN4q5QHUokSlDfLiWQr6Y9tmYPJmCeHP52eDHZV7M3QA3CVUaeWqIIOFBWYzQuoDHnaEkVvWnbjjQD6lTsH-HdebJsr3VFuBoj_p7sJv7k_7gTxU5U5SuagkIQsSgYUdinlgrXvyTNQNXHF802jw3SAoxeeHYWTg6a8r9utfYisuJ0S1bWI8ArciDlDsOWM6CRRt9mgGHjGH74D3CN08gm01Z0pMAJobCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBwnhVpySWq96j3qPxA7yZ1Aije9Rm2xcfyLau8AoYaPWlb8A57rKFnf34o2c-XFhmLMDIXYni4WuVwtS5MtFCDE0y2m4fksdg63cCMLbpwURLLfdc8M834f8c8do07f7ChL_SibU7kfan8R_KfsqTjkGMrlekRI0ykJD8yT4UMZtC9fdQVtWfE9y0A0K43p19j3glsddOmvCrf9tpVBH5kgQBVfONCWLVjp7AR8LA1ozmdnPksbpUZm2BIPCrXcNqqX9le7QeFCFrd0ObqLY1BMB8OOebvHDEbJBBaXEWmlnvE0KVYimn69gVpKwB5JxYyBfdPG6c3I79lNm9S0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hb2Qcj01HHGuKWw9YgKa1m6IFADU7IqHD81gYjNXRk_nrZ6Yl74oxsKLylk0Wt_A1WupUMiOw7Fd6n6jR9OT0CeGB4US1KfAiyx4lAUk2hqsvdo94NgzbsY5disaJXkYgO4OZBtg__ZGXH7iehWqKa5Ag0gr2e3A4IeuT0pWb5qoVrV5xmx-JHG3PLfLMlEROGiv97rSX0jbZBdQZr7bSeujoofm_YzhhymRDrk2sfx8nPXx0EPHw9lMI6oYJLsV3TRga6RP7i-hETNZVRsLQOFqc6lRklWUNXwDskmlFfu7oLsMko9kh_RxM72jw_g9pS4JSpVonbfZU6rgMAKKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ln5dwVNpRRj-GGudR4J_6F4LTYCwjx2UuCOktjqHKBgqYa9pmiOV485ENxzAzMcgO2nl_nbE1TbxwRe0cIWlnEaagPU0_YeqJqpsnbckYDNP2GjqM9sVXVwHVL4hMnXrL5OOe79imz6edPnMd81h72AhJ2XgHYKN7pCEx7uaIWoWcwOxiBnQjlWnMH9bNjbsOOgEVxbds_QvWvwXRrynAjTiP84zBNFfGdwviY8xvV76i5Ru8zd0pTqe-HkMiFRs9roQDJtuBmd3W1bcy23h86cziAGmw7Wvxe_4JkNAJliiGTwphJJspy9THA2Q1erMvXT2o_08UU0VOuTpaBy12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ab2h-oD7Iw8VVwUVLNe3AbF3vGlAD5EoyFYGdT1KUczHQ68IkW73IlEeIXpaoG1s1UpuSWh4eDdEnzhHnkciqWlVtDRWlbrCKHaGoHePrwhUY1TlcOTigfOj2Y1E4pRk9OyqoRsCk3cPbKr1kxJkfgfEZ4EcMmc2huSlVTE-bDa2fHJGfnVRNijTCTJuAJw7Jat9A-szI3l1yZjp_4E-2E4qOZ9_nYi69RkKRtOGr-ecQl-jFOuoVnWrmNZZkdPx36dLlRmcqVzYPcdYQTgLykmGvys8e8vwsweWbhpj2wyk-u_jKkGSMd1gLzY7oaWzKdx_8taTw9wwHxr2o4Tizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhfW-rt2ev1qd6zuICwbgORZCaACxK6RVISeC_u2yGXfR-6R2UQ9y-ApOmjYW54lbgimigkoDwq6OHEJVYnWa9tkV-_QP9ecxdFUmXaHJT182iHcK3pxS1DjByP54fkdVSqdII-GCsDv_1v4H3c-SjqbL-JWNvpf6c8_sZY_q_FsuNUBwKYyVwrmAjCUV-EckdDJN_3VRafHizKJrfoiDzq2k7uFVv-e7uTRRHdkWR_zTEHkBVzCrIshLkV_hdEtvReq-8TFBVTFcIpSqNT-qpHxF4BJBAVcm09fiDtRtkjOdlu5aLXiy18pVLui8GlR-y5lGULHY_8cf4ugtsTFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKaPCDKSeQ203Nnb6IG_nUK6ch9TW8TGl6zsJ4GCpvKE_cKA5mk36GDpgvr93YnUDld_6-Y2q6KnhoYRpAueCChG0LoxxLfMHP5zW96I4c4wm84Iq0118-qhGTkQDjR7rg81A5VZRdsxKNhfqNBrR2_F438k32fp-QxUO3UMvNLepuQNcyeyPGEQU_6xO1l6Vmkc7gGhcSTZV6AgXEal9g106PtfsrIlQSPfWm1qcSHzu7CmH4sscG-AmOXZbBNZv1Gw7LeI985Zp-6ItV54SenRtwOfuT7TMuDS4l-lWuCRJoamqK1jDB_3nxSNa2CfjtpU_TPFCd5yVjtV3DlL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tln6NXZABIlpUJgpiUPGxHXjMcrubJgGGo1_Vh8KOTNnmwdHF02anX-z8ScYRJtOt1-3XQEN56tCCDm-gjMpEsFvFGRr9VC5r59spgQMFKXQGHOBMTle4Risxzzuz1JEIuHSDmPrzze0gKyazFhRRzGGcM6uXM3Vl4mNZyY5ADVCL8I6d5tKIfUDoA-fuKvO7EnlMLkHT8mbE3LmIAOk-QX_RONjEZtbHq8_3b8AUHENw-VFqHC-lv1Q5eENDHb4vACwSCWXgl4SiMynL1vzV2FoPJZTl1m6BjdQ35708c-6IdGH9VVF8V1lmBLICTm5YjgspZyH8yv5Fwx2YLywhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احمد ناطق‌نوری درگذشت
🔹
احمد ناطق‌نوری، رئیس اسبق فدراسیون بوکس و نمایندهٔ ۷ دورهٔ مجلس، بامداد امروز پس از سال‌ها تحمل بیماری، در ۸۹ سالگی درگذشت. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465530" target="_blank">📅 20:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465528">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2ZssaMzaEYGSE2k3vcFKZEKybHAH8WbZBZjGRiwHIAUeYZRVNY5ouKuUrvNm7gDSCFsv6xxoQV8LLbkGwXkT_8Ow2Wj9jaGAx_xYEOOOdXV9lqT6OUgqP6jdDZG5YzsE92g8gIlRhZO-TB5yoyrC_djX4l2JO38UHpR7hBIBEhD3J4xSDL67KZ5Z8s7fj1CmRpDMTlWBZ2FnNcYkoIbW_b64AH109HJ1ab3NC1P_Cte7Ixt2FxI4-CT-1XvdQjt_BU2ulvH3RTV98vHdIJKKRFApC3jXtf9ShCJ7XHXcf4XBCrRKHPLk2CalwbqXTHymh6A88u1taPuQYQ6SWaNqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس پس‌از دو روز فرافکنی علیه ایران: بمبی در کار نبوده
🔹
پلیس مبارزه با تروریسم انگلیس اعلام کرد هیچ دستگاه انفجاری در نزدیکی محل استقرار نظامیان آمریکایی در انگلیس پیدا نشده است.
🔸
این در حالی است که پلیس انگلیس روز یکشنبه از وقوع یک حادثۀ بزرگ و احتمال…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465528" target="_blank">📅 20:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465527">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbaf08f2a2.mp4?token=iAnZ6pbWF_cjAkBwnwpbpT9ULSrTOUH0F3sJYcwQowELOfcEs6QwA4LN-80E3L-OnkIgWWVwBbLdMqVnwWUoFoZAXPH6YiVVmpK9uum24JAQm3OkINPdA7Hxf7L8iXgt6vH6gDrulveigK9mw4SLC3w8FX_RPOiJLV-vRUikKstPoclTZbIhPIe0_wlR4SewBY3dapvZOV9aUzowaP-2RuNxjS0O_Fi8_dtupZWaXqGy7Z8cIV5ahBMnniTMWFby9o2uP8Acvp1SQfCFloef-SGej8UPHE4trLTqMnCZQYsh7rMIDejyW0gAk8TmGbYi-3_2hXKsVI7GjvV8TVg8OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbaf08f2a2.mp4?token=iAnZ6pbWF_cjAkBwnwpbpT9ULSrTOUH0F3sJYcwQowELOfcEs6QwA4LN-80E3L-OnkIgWWVwBbLdMqVnwWUoFoZAXPH6YiVVmpK9uum24JAQm3OkINPdA7Hxf7L8iXgt6vH6gDrulveigK9mw4SLC3w8FX_RPOiJLV-vRUikKstPoclTZbIhPIe0_wlR4SewBY3dapvZOV9aUzowaP-2RuNxjS0O_Fi8_dtupZWaXqGy7Z8cIV5ahBMnniTMWFby9o2uP8Acvp1SQfCFloef-SGej8UPHE4trLTqMnCZQYsh7rMIDejyW0gAk8TmGbYi-3_2hXKsVI7GjvV8TVg8OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: روند بازسازی واحدهای آسیب‌دیده سرعت خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465527" target="_blank">📅 19:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465526">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌ عربستان خلبان مهاجم پرواز دبی-تل‌آویو را بازداشت کرد
🔹
پس از فرود اضطراری پرواز فلای‌دبی در فرودگاه تبوک عربستان، مقامات سعودی خلبان متهم به حمله به همکارش را بازداشت و تحت بازجویی قرار دادند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465526" target="_blank">📅 19:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465525">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6_CMrI4qdNGDGtUKxi0VbyDORjoEyJx9cUJMM4WvubzfR48QAnR5pnFnG6rQZdpqppM5ITTlTZ6Ez-5raLTOanZMmimSssi0cjf7ccRRhEWQLOVFOSWzx1Cf28RmzaWsPhI6UiJtIvkwpbdK7zhTWHsT_qxE6Y_CETS44j24I5L5W_44qeRLBzvbShvYE794xPvyRKPjkfapiQiraEBEyZIrdnECccuLTUam8hn236brLhwWTBD_CZ6852S4d59sxZSg8DaoyQdSQHqQlyixlgsucdy5qTnG871_fxStt4T1o24ulRGYCAHtC-WHiNzC_BPx29eIPLrv7RRcD34LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب کشاورزان شارژ شد
🔹
سازمان هدفمندسازی یارانه‌ها: ۴۱.۸ هزار میلیارد تومان به حساب گندمکاران کشور واریز شد.
🔹
این مرحله از پرداخت‌ها شامل کشاورزانی است که گندم خود را تا ۶ مهرماه به مراکز خرید تضمینی تحویل داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465525" target="_blank">📅 19:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465524">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd034e6117.mp4?token=kny9GU1Ty-F5BGrbqs2n1E-OpJ5PA7-Q2wfWeilB6blSMxLP8KL7pHGTjr5Yi6d9bAUwQLQCIkCOiX9yba8TowpZEIrjmc4G4BnfjjO27PHdtaBgX0s5UGK9oVUO32GLlhvtE3fQj_33Uttnq5Kti6UuYV5PMjwQwlqVK7J2CbXonameKrbUsK1Hbx3RnUS5JOR0tOPN_1Ep83gOr8pFJk0Y_O48sh8qlBk4CIR9gqoDEF3d7sItahi2GAHpdCiq3rNH9sX6TWiqfIhaFmwovV0PnAN78QGw0bFbHSli-aZFWGD5CSoT-S6O4zpcJYQa_yjTbQGUhYV4lZ_P70tCmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd034e6117.mp4?token=kny9GU1Ty-F5BGrbqs2n1E-OpJ5PA7-Q2wfWeilB6blSMxLP8KL7pHGTjr5Yi6d9bAUwQLQCIkCOiX9yba8TowpZEIrjmc4G4BnfjjO27PHdtaBgX0s5UGK9oVUO32GLlhvtE3fQj_33Uttnq5Kti6UuYV5PMjwQwlqVK7J2CbXonameKrbUsK1Hbx3RnUS5JOR0tOPN_1Ep83gOr8pFJk0Y_O48sh8qlBk4CIR9gqoDEF3d7sItahi2GAHpdCiq3rNH9sX6TWiqfIhaFmwovV0PnAN78QGw0bFbHSli-aZFWGD5CSoT-S6O4zpcJYQa_yjTbQGUhYV4lZ_P70tCmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جهش بی‌سابقهٔ قیمت سوخت در ترکیه
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465524" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465523">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تعطیلی معاملات شبانهٔ تتر در صرافی‌های دیجیتال
🔹
طبق اعلام صرافی‌های ارز دیجیتال، از چهارشنبه ۸ مهر تا یکشنبه ۱۲ مهر ۱۴۰۵، بازار تتر-تومان هر روز از ساعت ۹ تا ۲۱ فعالیت خواهد داشت.
🔹
همچنین در این مدت، سقف خرید روزانهٔ تتر برای هر کاربر ۲ هزار تتر تعیین شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/465523" target="_blank">📅 19:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465522">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23998377d.mp4?token=eI-ZBWu31rDIen4QLl4ifapWosXhUIXDX-MFFZVkVVQRl9QNiW4XYR_XB65_dDbVBwi5g5R6H42GsWz_bQs1_9gfhV5KVHBrhsFjt0Sc40cw6I49hZCG88663rSRh1lJB-M5TEL9RlOeOdaiMranRX8JCf4dCz3oo10X9YnUzBF90XEIHowtoUqGYWc4NbBgVNRE3otlMri1YHaceZXycI7ih0_Mu0PlxXQ23DPdRon8LRNDIfLSYP2zbMmm6NVGtnfa1EjniKi2GI8xS6Q2u3Zp0AYQLWzsqLCWQMoUbzTSY709raojiosRYxTtptocCHTa_IlBZq63KKl_XnC6UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23998377d.mp4?token=eI-ZBWu31rDIen4QLl4ifapWosXhUIXDX-MFFZVkVVQRl9QNiW4XYR_XB65_dDbVBwi5g5R6H42GsWz_bQs1_9gfhV5KVHBrhsFjt0Sc40cw6I49hZCG88663rSRh1lJB-M5TEL9RlOeOdaiMranRX8JCf4dCz3oo10X9YnUzBF90XEIHowtoUqGYWc4NbBgVNRE3otlMri1YHaceZXycI7ih0_Mu0PlxXQ23DPdRon8LRNDIfLSYP2zbMmm6NVGtnfa1EjniKi2GI8xS6Q2u3Zp0AYQLWzsqLCWQMoUbzTSY709raojiosRYxTtptocCHTa_IlBZq63KKl_XnC6UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحشت اسرائیلی‌ها از این نقاشی‌های کودکان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465522" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465521">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b5d339493.mp4?token=FYs51i3wkghcOIHmWXwR8P8vSpbH638QsYojoJiwJp9tqJQmdvFd6h3laNPWhX3m9qRopkAK02wYA58G0OpQZfIt6sHy8rOzFB565LtQbypMH1MX-K47u0QMMQB1y2-C10XenISTEBp-pZFSx3oLnQk5G_33dBxlnOjWGjeVvShGXJ9C7XcJwjZp-EKsy_TJsC1U65Iyz_2Ny1Wbb4U2VvpH9XmxB063c8gMYZ9VNLO5rzB5Fka-i3ylm6LcDogsOYJcVi4ZOpda-g8I2ROEQJmYwX1a5YdMWtnreuoSEZGC-iobbILD7M5eR-td5rV4udT5UK7iCpK77maQtVg3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b5d339493.mp4?token=FYs51i3wkghcOIHmWXwR8P8vSpbH638QsYojoJiwJp9tqJQmdvFd6h3laNPWhX3m9qRopkAK02wYA58G0OpQZfIt6sHy8rOzFB565LtQbypMH1MX-K47u0QMMQB1y2-C10XenISTEBp-pZFSx3oLnQk5G_33dBxlnOjWGjeVvShGXJ9C7XcJwjZp-EKsy_TJsC1U65Iyz_2Ny1Wbb4U2VvpH9XmxB063c8gMYZ9VNLO5rzB5Fka-i3ylm6LcDogsOYJcVi4ZOpda-g8I2ROEQJmYwX1a5YdMWtnreuoSEZGC-iobbILD7M5eR-td5rV4udT5UK7iCpK77maQtVg3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در مراسم ترحیم آیت‌الله شبیری زنجانی
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465521" target="_blank">📅 18:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465520">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmamSXUbuU-ABTIx3t_BCyvXPQOXUlRhXmiq03OR93hmwBy5rkkBUl5cL0w2O7aE-G_xpsBaIuVnsyUhVL5VdLqO0kbCZ7JTrlaKVmwr15lmco2gsUY4-bsipBHXcI7v21Qv3pabSIOZ1Jm_P7Fa-RU81c-5lEEdGh5Mr8Z_TcoUnIAFpohNutUtHCgH2ypkxe92rRc8CRF52qaJlZAdLL5nut55A4e6RPPgPaBFqFYfHHFffyjPG63EPwmE8emYPUUUHrkU88chdHsqDBllFSMXFIPNf8cm9X91YmXFbz4a8mnEJUW8Jyxn9tojy7NJIgNJl3zkscerp5AhBEw06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از عراق نرفت؛ فقط شکل حضورش را تغییر داد
🔹
با وجود ادعای پایان مأموریت ائتلاف آمریکایی در عراق، تداوم حضور نیروها، تجهیزات و همکاری‌های اطلاعاتی نشان می‌دهد واشنگتن صرفاً شکل حضور نظامی خود در این کشور را تغییر داده است.
🔸
علی الزیدی، نخست‌وزیر عراق، که این روزها در پازل آمریکا بازی می‌کند، نیز گفته است: «با تثبیت کنترل نیروهای امنیتی بر وضعیت امنیتی کشور، مأموریت ائتلاف بین‌المللی تحت امر آمریکا در عراق به پایان رسیده و مرحله جدیدی با محوریت حاکمیت عراق آغاز شده است.»
🔹
هم‌زمان با انتشار چنین ادعاهایی، نشریه آمریکایی وال‌استریت ژورنال گزارش داد که «تعدادی از سامانه‌های پدافندی و تفنگداران آمریکایی در عراق باقی می‌مانند.» این نشریه به نقل از یک مقام آگاه در پنتاگون نوشت: «آمریکا قابلیت‌های اطلاعاتی و شناسایی خود را که می‌تواند در داخل عراق مورد استفاده قرار گیرد، حفظ خواهد کرد.»
🔸
شیخ علی الاسدی، رئیس شورای سیاسی جنبش نجباء، نیز روز گذشته گفته بود: «این اقدام آمریکایی‌ها مشکوک است و آن‌ها شرکت‌های امنیتی دارند که برای جبران عقب‌نشینی نظامی آمریکا وارد شده‌اند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465520" target="_blank">📅 18:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465519">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK5uKzn3RxnJA60tQ0fQCPSAwgwbPOJB1TzWwojuF-maqHvkAa6lxTrV2UO3w7tNoZc19DbBHaz5zi7Jr8C-ru-4lQKff4uLAfE8vunSI-T9GB2rnNIR-hIWmI5hEUAOe03ESZ1o8VO-UaRauwurxDAXRO0ZjkdqtUnxvyfl_qDdQSYys5f8ZhtjVpCLeySnl0na7LYTn60F7gr7Np8UK4aluhlhJjDIwNssMn4KuAYhTCBd9mektGXUXI-xP3nofZWngGNvVOY6lal_sBk70_W6Iw49G8Qsa1ykd4fIxh6xTPtFw7Ztcds1xYeMl6aoUVJ1MdYqFQUi-MBhM8T6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام برای خرید طلا و دلار ممنوع شد
🔹
بانک مرکزی: اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
🔹
بانک‌ها باید متقاضیان وام را اعتبارسنجی کنند و منابع بانکی را بیشتر به بنگاه‌های اقتصادی مولد اختصاص دهند و بر نحوه مصرف وام نظارت داشته باشند.
🔹
در صورت انحراف وام از هدف تعیین‌شده یا تخلف، مدیران و کارکنان مسئول به مراجع انتظامی، نظارتی و قضایی معرفی خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465519" target="_blank">📅 18:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465518">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۱.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/465518" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۰.pdf</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465518" target="_blank">📅 18:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465517">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دعوای دو خلبان پرواز امارات به اسرائیل را نیمه‌تمام گذاشت!
🔹
رسانه‌های صهیونیستی گزارش کردند که پرواز امارات به‌مقصد تل‌آویو در میانهٔ مسیر کد اضطراری ارسال کرده و در فرودگاه تبوک عربستان به‌زمین نشسته است.
🔹
به‌ادعای کانال ۱۲ رژیم صهیونیستی، علت این حادثه…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465517" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465516">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو با دعوت رئیس امارات به این کشور سفر کرده بود
🔸
دفتر نخست‌وزیری رژیم صهیونیستی در بیانیه‌ای گفت که نتانیاهو به دعوت رئیس امارات، به این کشور رفته بود.
🔹
در این بیانیه آمده، این دیدار بر تقویت روابط دوجانبه و چالش‌های منطقه‌ای متمرکز بود. رئیس شورای…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/465516" target="_blank">📅 17:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465515">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfkWnLX6SKIIPQUx41aGdaaLvbXVN0IJMRuXW58FL3zIeSUc7SiZZUlEytz_BpsevceWh_vGKl8GElgpZ5TVdeTRdDFJqTFVclCxnHITOWBGr8WGxjTQw3G1n08W-j44a-BmyeHu9_HpYKNgq4_1yS0-mvIyrlu63N_IKnThxCmb86t29Ww4dA7CPeR6fPXksW5FwzOMd-kaFgOaS4107zor1_t1ZKEJDUmOPjS0t6LPKMESHUOtOIwFeGl4bJDqD_FBE1NUwsd22fYi0G56bp8SahmktLTE__hHRK7bahqgb6spiV7-A6QFtmuwOWAaoHqqQzHMVCH8YRAfpUs5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
یمن ۳ مخزن ال‌ان‌اجی آرامکو را منفجر کرد
🔹
تصاویر ماهواره‌ای اثرات انفجار در تاسیسات گاز طبیعی مایع‌شده (LNG) آرامکوی عربستان در ینبع، در فاصلهٔ زمانی ۲۵ تا ۲۷ سپتامبر یعنی ۳ تا ۵ مهر را نشان می‌دهد.
🔹
در این تصاویر چند مخزن ذخیره‌سازی آرامکو در ینبع منفجر…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/465515" target="_blank">📅 17:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465514">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F63PsHY6uuzZPPK6Js2WtMUwZFEG99oWrLUAmvG9MZHxNKJ_UpzA_F1u7CNb_ALYNfDytDsGUyden7aqvj_SrR0i18be0BpJrg3jwx9-AKc79nupcKk4ACMGXrXV1_8w6YdADAgJCT7BkMA3zCQpqaZS5p6_4k87bTaRKjog6VhoRLccALGnvvH1Q8u_Byeb8lIFOMPDxEVQ45WhWDf-hA3hHgrsID2Bl_DsTbCS5i2IgjspPnKz5JE_hekbO9o7qcRemDhCraqDnhYRR8r5FidGrIufeQ8oNETMgXNzZ7HmfvkFyaQ4wZuGn2S4esqsd0rAX7Uaa4H8xCUOlz3_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ماکرون: اگر انگلیسی‌ها بخواهند به اتحادیۀ اروپا برگردند، این هم برای کشور خودشان و هم برای اروپایی‌ها خبر بسیار خوبی خواهد بود.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465514" target="_blank">📅 17:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465513">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_5Q3yiFe898ddUWjZeS7a2XryjzFdX_YdBCI_q4REep2B6dFV1xNtpUNdbN67j1FoKFC4K7jhw43WBeNblkuD9Igu5C1wagLga3H_PaIBgdF-j34T7WjQPf0XvfGLwFweAVDFF8GfGyDPTYiSqRYzc9YWnVFxze6h5ViAgecFf1YP9mVVDrGZJKIi-MHwTpKlo2NKjgX_gQQEhuzQlFQPZkVfdpdr5fiC2pzhAt2qFi5MB2_WQzYNFiqsoXT4jNa0snoDEbAe0WkRenzidR69eFmlAqzznFk96wvZL00jpCP3hhzn5DiZNIBi1kE64SUpmNPiAGRqL2YUXbFANdtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرضهٔ ۲ میلیارد دلار اسکناس به بازار ارز
🔹
بانک مرکزی: عرضهٔ ۲ میلیارد دلار اسکناس برنامه‌ریزی شده که فروش یک میلیارد دلار آن از امروز از طریق شعب منتخب بانک‌ها و صرافی‌های بانکی آغاز می‌شود.
🔹
تمامی افراد بالای ۱۸ سال می‌توانند با ارائهٔ کارت ملی، تا سقف…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465513" target="_blank">📅 17:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465512">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd68e1dd1.mp4?token=F2juKH7zo6rtfit7P9INs0Bl3pE6cFA6W6OQref3zq0GqH0-S5h83OdlyuR7BvYsPlOykNmzPWPDurBXkezMYd_41Iaj30ZVdyH4ruTcTUKVvTfSzDhbLkjJaowve6OSlXqKPB28z28ozS3o2_AndGo_yFx84ByfnTrEqu_Z2lVHNpMIXuaQG5NPgZWRRlRHRurCm1lzG6Aa6ehgn19WbIR61zrCVOlPfdgsBO36FB5JfpA5ncilKbz4oPJ8jysZaZi-nrqGQJyo88Em4M6wpJtRk9ulls4fVnqOZz_by6P-nZ765UGje8fapAbh5XjYgcZbftB8lVWWt63BLAARJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd68e1dd1.mp4?token=F2juKH7zo6rtfit7P9INs0Bl3pE6cFA6W6OQref3zq0GqH0-S5h83OdlyuR7BvYsPlOykNmzPWPDurBXkezMYd_41Iaj30ZVdyH4ruTcTUKVvTfSzDhbLkjJaowve6OSlXqKPB28z28ozS3o2_AndGo_yFx84ByfnTrEqu_Z2lVHNpMIXuaQG5NPgZWRRlRHRurCm1lzG6Aa6ehgn19WbIR61zrCVOlPfdgsBO36FB5JfpA5ncilKbz4oPJ8jysZaZi-nrqGQJyo88Em4M6wpJtRk9ulls4fVnqOZz_by6P-nZ765UGje8fapAbh5XjYgcZbftB8lVWWt63BLAARJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماکرون: اگر انگلیسی‌ها بخواهند به اتحادیۀ اروپا برگردند، این هم برای کشور خودشان و هم برای اروپایی‌ها خبر بسیار خوبی خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465512" target="_blank">📅 16:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465511">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20f2524b9.mp4?token=CJsPju8PZdHI5N8jVaXWGSabp_fmYRM9yVbguLXs6_cQbEpLOP8uLiWajLn-JQObV4TSQZ9wVV4MLSMuh9PYdgOZCvW57uCbo0tXIFEinjv8YADD9e8046bsfxCTI7JHLVK_HVG2m3Le5W7n_P9ISEz_aQmhBix04cszxXUpX8tJCq_eE5wMnDbACID2tOuvpw2avJFvyF2yK7rO65ZvKNuiJ7VWvGIRsDT1Kq0QIO_Nso9IExi9OCe4TKTMXN3owarZN6Kj9hJ8jMnF0oshlIl-r1v-hCbA1An99wEoE5UyercwYNEyJQ66sqvxW2yUDlbS0P266lhTle1qm4JzLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20f2524b9.mp4?token=CJsPju8PZdHI5N8jVaXWGSabp_fmYRM9yVbguLXs6_cQbEpLOP8uLiWajLn-JQObV4TSQZ9wVV4MLSMuh9PYdgOZCvW57uCbo0tXIFEinjv8YADD9e8046bsfxCTI7JHLVK_HVG2m3Le5W7n_P9ISEz_aQmhBix04cszxXUpX8tJCq_eE5wMnDbACID2tOuvpw2avJFvyF2yK7rO65ZvKNuiJ7VWvGIRsDT1Kq0QIO_Nso9IExi9OCe4TKTMXN3owarZN6Kj9hJ8jMnF0oshlIl-r1v-hCbA1An99wEoE5UyercwYNEyJQ66sqvxW2yUDlbS0P266lhTle1qm4JzLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن ۳ مخزن ال‌ان‌اجی آرامکو را منفجر کرد
🔹
تصاویر ماهواره‌ای اثرات انفجار در تاسیسات گاز طبیعی مایع‌شده (LNG) آرامکوی عربستان در ینبع، در فاصلهٔ زمانی ۲۵ تا ۲۷ سپتامبر یعنی ۳ تا ۵ مهر را نشان می‌دهد.
🔹
در این تصاویر چند مخزن ذخیره‌سازی آرامکو در ینبع منفجر شده‌اند که شامل یک مخزن افقی، یک مخزن با سقف ثابت و یک مخزن کروی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465511" target="_blank">📅 16:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465510">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس افغانستان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSIivA6ZxPh5aIXv4tglufrO3BxZq_B2NmfR-GRx9wojtI-YVnQTHe_3iC7nnIrCPZjLDPegnWT3b69ntbD1CZkce9JWk6_y4LipLYPDQSUwSOdCr9eq9wSY33wpzSnTUtW0rSamWvsCOUBns19kIO0c2E05INe4wTZmZ940S6nRXE3nmxwltHyTU3IWnAngkopk8Uk4RNDRhgUHOQBQxwDomiVrbUrgALomXbh06rE7104AG8wxl_VXxqBUPDApamozYtWmjPLH4uG3qb7cSF8MOTryTBB1IAYmhQg3xQxTcv3ohn49Cl-vw41w475FLdCxPdYh9G6kTwdZl2HW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان زیر بار تحریم هوایی ایران نرفت
🔸
طلوع نیوز افغانستان امروز چهارشنبه اعلام کرد که به‌رغم تحریم بخش هوایی از سوی آمریکا، طالبان به شرکتهای ایرانی اجازه پرواز به افغانستان را داده است.
🔸
چندی قبل وزارت خزانه‌داری آمریکا در بسته تحریمی جدید، ۲۷ شرکت هواپیمایی ایرانی را در فهرست تحریم‌ها قرار داده بود. به دنبال این تصمیم پروازهای ایران به کشورهای مختلف از جمله عراق، عمان و ... متوقف شده است.
@Farsnews_af
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465510" target="_blank">📅 16:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465509">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30bd7bd1b4.mp4?token=BWOYhNsF1LKxkSXvGC8axMK6W1Y9W0XBM0kKzaDIHO4MkhA6BXpPjMd0w6AiQEUR6okJQsiHlrV_pkVwU-Ihjve1HDSYsaA-LoGHq0OFQwtA2I17CICnIjxfi5AALO6yHOLP9fV3TyLn6p2IBAMCv3iUWMtcYKuaoRuk0dpobifHFbvyLqXIubCNWQOeUCwA730DhDYfaCaXzI_swwMHRpY7avYDr1CEm5kIlGDVAyvE5vzYCBv5FGfII3m82evcT9LVY4YMk1Raux_ojxAZJj5a-7Au3_U_idllJ6trGAfOshf09WOA794Ckp8VQbLrb-HcOxLLAfMD_hLzGkf1ZGSPbj0ZUwl92qSBCOj5sn5il3bXipdO0GPd7Ki3y6ou2Ru-HLV5WhyPV-Qz2mla7Njo1-fbm0kJorSFVpVWk_2ncoqY4XqkDW-jLiOxMz1785JPKXtxGmFTUFy_9AIAa9ElUr4eM-euU4yHRlCVYREZZVGZnVX7EnL7KolkTNxHWfDRe-9O0fniOxEQLe9kEiVQmRwXgYfpAWrCtw80IjBNxAFq-YpwVj2WYzLtg-FxpXfHlYLIf3-xxcqZo8YhQnKhEIPP1qzcbENCV9HSwhGB7uzmJoPN0nsn81pflKKgeWAWX-mbg0uE3fc_zh-pUWjrBsaIqdT-aL5jG1LLLCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30bd7bd1b4.mp4?token=BWOYhNsF1LKxkSXvGC8axMK6W1Y9W0XBM0kKzaDIHO4MkhA6BXpPjMd0w6AiQEUR6okJQsiHlrV_pkVwU-Ihjve1HDSYsaA-LoGHq0OFQwtA2I17CICnIjxfi5AALO6yHOLP9fV3TyLn6p2IBAMCv3iUWMtcYKuaoRuk0dpobifHFbvyLqXIubCNWQOeUCwA730DhDYfaCaXzI_swwMHRpY7avYDr1CEm5kIlGDVAyvE5vzYCBv5FGfII3m82evcT9LVY4YMk1Raux_ojxAZJj5a-7Au3_U_idllJ6trGAfOshf09WOA794Ckp8VQbLrb-HcOxLLAfMD_hLzGkf1ZGSPbj0ZUwl92qSBCOj5sn5il3bXipdO0GPd7Ki3y6ou2Ru-HLV5WhyPV-Qz2mla7Njo1-fbm0kJorSFVpVWk_2ncoqY4XqkDW-jLiOxMz1785JPKXtxGmFTUFy_9AIAa9ElUr4eM-euU4yHRlCVYREZZVGZnVX7EnL7KolkTNxHWfDRe-9O0fniOxEQLe9kEiVQmRwXgYfpAWrCtw80IjBNxAFq-YpwVj2WYzLtg-FxpXfHlYLIf3-xxcqZo8YhQnKhEIPP1qzcbENCV9HSwhGB7uzmJoPN0nsn81pflKKgeWAWX-mbg0uE3fc_zh-pUWjrBsaIqdT-aL5jG1LLLCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: مجلس تعطیل نیست
🔹
نیکزاد: فعالیت مجلس برای انجام وظایف ادامه دارد و نمایندگان تنها ۲ دیوار آن‌طرف‌تر از صحن، وظایف قانونی خود را دنبال می‌کنند.
🔹
در هر جلسۀ وبیناری مجلس حضوروغیاب انجام می‌شود و  اگر نماینده‌ای به سامانه متصل نشود، غایب محسوب…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465509" target="_blank">📅 16:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465508">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcVl1MHUvRcJQ7wnDmD-ztRX35wuDLklMnI7hPIOF0yAi9anrb-GHIRzuLkTBo4PjBgAPxNQ469qW-1Iu9WvSYLKSyHDx7_JbTqniiI28UgOzgR8i9tmyEBOHkUsBW111a8lFbmJGBg4joNwTIQcCnBm9-G4jX4L2MNMuFMvQn6GnJcrT9HQE846oTtH1gCbRaRzY3PGs9LMBc3vIwpQcxjSmjxewbt2VMnQmiHmFXVNhsomcYKjkM0raSHk8-t9cmnEsH-x2gTB8cyC-q3icwUuqpU3FzdNyvtWVV8SAmxGYb3UpRYkFNBquR4_IfUxlaeC7KjcsvzGyQ9dh2ydng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی سپاه دربارهٔ نامهٔ سپاه به مردم آمریکا: ما خواستیم مردم آمریکا دربارهٔ جنایات ارتش این کشور آگاه شوند؛ وجدان انسان‌ها در هرجایی که باشند قابل بیدارشدن است.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465508" target="_blank">📅 16:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465507">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6237e3f751.mp4?token=rs8DjTxAVBf6H5dnRVQzHoWQxkb2VPFADR9J02rI64z1hF7zhci7q4MgGmA4JyAOseGGyg2n_5rYGarEmA3CM2s50YjZ_JM9y5o3o7qXzCoJScWqzi-a8Yci0IeAJb75iybBDvIVGA1e341kU9P1jVqLmOZ16DphTC9gn92wkuvJ5j-eKRDSRMcBpfKwh0Ot9LWssRXh9rtLnH0nfsdWXfEGLvZnprc8qypXb1WoVlvs3rM8WL7viMGVa_CCNKgNJFvXD7PudDsbNQ_DqugHmB-qBnXsi1X4Plip7ejzzPib3irj_RG68ICFgyMctow-gezQ_tBSEdaRQBsBN0hpzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6237e3f751.mp4?token=rs8DjTxAVBf6H5dnRVQzHoWQxkb2VPFADR9J02rI64z1hF7zhci7q4MgGmA4JyAOseGGyg2n_5rYGarEmA3CM2s50YjZ_JM9y5o3o7qXzCoJScWqzi-a8Yci0IeAJb75iybBDvIVGA1e341kU9P1jVqLmOZ16DphTC9gn92wkuvJ5j-eKRDSRMcBpfKwh0Ot9LWssRXh9rtLnH0nfsdWXfEGLvZnprc8qypXb1WoVlvs3rM8WL7viMGVa_CCNKgNJFvXD7PudDsbNQ_DqugHmB-qBnXsi1X4Plip7ejzzPib3irj_RG68ICFgyMctow-gezQ_tBSEdaRQBsBN0hpzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا با پایگاه‌های اطراف ایران خداحافظی می‌کند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465507" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465506">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvcChXxzqWcCTCYObArKUYl2-pECI9avGs0rXLLMHCeL1BQhqT6tedwJ37rdaZTn7DH12lJyGr1nV_2HPNMEt7QMZ6WyRqWMOzV1NPFBnJpNPVfYaRDx_xKXAEwQlIJ9MjoqEsu1eTRl0Is5wgFWRHJV6B0y4H0EVtY_bKxEb4dAKriwzmQAMZBxiBEkKyjCcu-rMrviqCPZMkPdrVd-VGIR1qM8J1IByjUn_7aL4Y0WAL2pAy8E1XQq3rJE4n8kcEXE4Az2P7LG29CJBIHFbrs-Famr4dnOP9jWhQ2c1gSFQzYtCvx2uFm_R_n_iBS5ahCEXk_tknWkp1RVFs-Y7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگزاری مراسم دومین سالگرد شهادت سید حسن نصرالله در لبنان با حضور حجت‌الاسلام پناهیان، حاج حسین یکتا و سعید حدادیان
🔹
همزمان با دومین سالگرد شهادت سید حسن نصرالله، دبیرکل فقید حزب‌الله لبنان، مراسمی در مرقد «سید شهدای امت» برگزار می‌شود.
🔹
این مراسم با حضور جمعی از چهره‌های فرهنگی، هنری و ورزشی ایرانی که به مناسبت دومین سالگرد شهادت سید حسن نصرالله به لبنان سفر کرده‌اند، برگزار خواهد شد.
🔹
حجت‌الاسلام پناهیان در این مراسم سخنرانی خواهد کرد و حاج حسین یکتا به روایت‌گری می‌پردازد؛ همچنین سعید حدادیان نیز در این برنامه به نوحه‌خوانی می‌پردازد.
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/465506" target="_blank">📅 16:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465505">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_YWoLPhANbUVBtyRSnY-M5NxCcCsos_nYIi_HxaL8YGNf65EP7YoEWedAfmzRNCOzb22fVtB-wuMU7P5_c82DiH7tNHTkW-B542qadyzVDEcjbknSc5rKHu-C1royxIOrQnS1v9QmgXmcgLki-oAx5DBUYEuGoxZALEERR6MAhNKulPEAWXAZwJoD8fQtZEYfEMecVIGo1yHZJ1AsQqLPG0OPTNGMvPFpzLRY-5t9t1RoUyWjkzODO9n0YSyiiVtjzJ61DkCxsh5Xz-svr9td_s_qfNiEWHJBYIGKHXIWU1CBHeQcW01OUTSKx08W7iuJUNCYwYwCtaYtXWytOhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
روی مهربانی بانک ملی حساب باز کنید/ پرداخت وام ۳۰۰ میلیون تومانی در بام
🔹
بانک ملی ایران در طرح «مهربانی»، وام قرض‌الحسنه ۳۰۰ میلیون تومانی با کارمزد صفر، ۲ یا ۴ درصد ارائه می‌دهد. امکان انتقال امتیاز وام و حفظ دسترسی مشتری به موجودی حساب از دیگر مزیت‌های این طرح است.
مشروح خبر
📥
دانلود
#بام
، بانکداری دیجیتال بانک ملی ایران:
📲
https://baambank.ir
🆔
بانک‌ ملی‌ ایران |
@bankmelli1307</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/465505" target="_blank">📅 16:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465504">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/465504" target="_blank">📅 16:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465503">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4300abbaf9.mp4?token=NbfZktAkXMXTvgcPG2uyKyTIUuO5W7XIF6CPBkqN1pM7JmWpnF2kuu8HAyNCZ3qFY0l-f9fSvhOb3zBq6mrTYiQyt3MKMFrcESWK0K0eZV49dVNRHjd27Iq8HSmsqzyyUz08dD5bO9JcN_ZWNIuSgzkS7Mb-zh9e0BRiwiuAAjVZtiKC45GCI94cqS48lhE_PE1SbX6LZEZ782xgv3zFvL7GEInM6moOy-i9ivFbpZBJnWKP2z-f-DLvPpT_CL_jPiBP675igjfk4pF0DlMNVarXzAGytHVzJ45vexh4kf_336-A_6A7wNy7VNn6jPoTSJcx0WFJsJcjPk3ASrAcuIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4300abbaf9.mp4?token=NbfZktAkXMXTvgcPG2uyKyTIUuO5W7XIF6CPBkqN1pM7JmWpnF2kuu8HAyNCZ3qFY0l-f9fSvhOb3zBq6mrTYiQyt3MKMFrcESWK0K0eZV49dVNRHjd27Iq8HSmsqzyyUz08dD5bO9JcN_ZWNIuSgzkS7Mb-zh9e0BRiwiuAAjVZtiKC45GCI94cqS48lhE_PE1SbX6LZEZ782xgv3zFvL7GEInM6moOy-i9ivFbpZBJnWKP2z-f-DLvPpT_CL_jPiBP675igjfk4pF0DlMNVarXzAGytHVzJ45vexh4kf_336-A_6A7wNy7VNn6jPoTSJcx0WFJsJcjPk3ASrAcuIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رادار میان‌برد چشم شبکه آمریکا کور شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465503" target="_blank">📅 16:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465501">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1c9a63dec.mp4?token=BSYnirCHB5FZMirW3EZ01toK80xYZXzfmaITyyIrOU_7lWEGxsvCSjz7yWpPWnfM5ZR57HXby-Uv7XugE7-6Pskw9MInCcQ-XsbD76RdH645gfhtU0E2aBZZij5KLC8DmuY7YXVV-tjep1ls9xFdSmZwPMdHzt7Ijvy5Db80_38ZT2eK5dPkbMy1xmFKB_QSVoK6TR62380ihiSLsf-aRdTcYRFVkoVrJEbRjA1yjH2R0cUor5xg4P8K-FBo0cuRC-fAxb-t20OaOjgqGKJaslTUiipOPM2BObsKznSrvkYg2uzmRktQoTIjAyRFxPlmRaPKmQt4ottTzFFZ6EZgyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1c9a63dec.mp4?token=BSYnirCHB5FZMirW3EZ01toK80xYZXzfmaITyyIrOU_7lWEGxsvCSjz7yWpPWnfM5ZR57HXby-Uv7XugE7-6Pskw9MInCcQ-XsbD76RdH645gfhtU0E2aBZZij5KLC8DmuY7YXVV-tjep1ls9xFdSmZwPMdHzt7Ijvy5Db80_38ZT2eK5dPkbMy1xmFKB_QSVoK6TR62380ihiSLsf-aRdTcYRFVkoVrJEbRjA1yjH2R0cUor5xg4P8K-FBo0cuRC-fAxb-t20OaOjgqGKJaslTUiipOPM2BObsKznSrvkYg2uzmRktQoTIjAyRFxPlmRaPKmQt4ottTzFFZ6EZgyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طلای سنگین‌وزن کشتی فرنگی ناگویا به میرزازاده رسید  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465501" target="_blank">📅 15:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465500">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbFB9qS4BPPNoxz7r8axT3jioHDJrJAuAGifK9xRcAKW5hbKnfHViwiFdaDqPHrdNnjIckBcPpJOC9J8WMeBhCDAHSSuyB3mej4xzy_2cHcZ8KCYDTzgc-Nm_twm-xaFRf1-R7rcynyJdbNdowjfkQQWPj60moNQ_4WBK-9x-R5Ky260Eby-e6d1SmBFyRtgOhtTvFYJYwAEcZwc1QfElyQGTNJNbEHws9N3SNxilz15tb_fZIjVXfSx8uJuwgGMgdxGeg1y3KwLKZnDXLmvqZVfFns7as6QFOqDQYho8zhRoDiEy5krk1dl3BppUabs71-uLZlnxqwHiB8F5MGqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: نحوۀ استفاده از کارت اضطراری پمپ‌بنزین‌ها تغییر می‌کند
🔹
تا ۲ ماه آینده مردم می‌توانند به‌جای استفاده از کارت اضطراری جایگاه با کارت بانکی خودشان بنزین بزنند. @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465500" target="_blank">📅 15:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465499">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIkyjiY7yQyJpa0EDKnfg4p7OTA74Uk8fPDoBHdmP0ycqYzFQ8z5mUelfA-tRxknSPTGEliXZ8KTNacwkagCZIJSw94ziDzHLnZoNTkGco5VHylzIU_06mm_nFKzC5z6puPQSAbgtZo9b2Dtw3gRT2lVEhPdGYHP9-XYDqlGnAjV9X6nH05erM7wS79Ssu0HiolvQpIQ4ZmV8_5qXw2cFDY0J9bCnSw7Umv5uOC7gCyo6qEbRxR1q9xH-n64xdqnl9zElBlLZqV202SpQY-fMzQ8joe6yrrOE-jWHRWZ1rrDSfEfade8zGS3QzDMFTdI_TacOp_qhAeYoz9jHThGjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ روسیه، ناتو را به استفاده از سلاح اتمی تهدید کرد
🔹
سفارت روسیه در ایرلند به ناتو هشدار داد که در صورت هرگونه اعمال محاصره علیه منطقۀ «کالینینگراد»، از هر ابزاری حتی سلاح اتمی استفاده خواهد کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465499" target="_blank">📅 15:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465498">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c26d94481.mp4?token=TfcFrs9PcfgLPFc7PRhB9yTvwKyTpDRu7ggWGtIoFFeRRmO_dQzCiNYKrrvpG9U3YSpcv8KDO8uOxh5FD9gmJvMEJFsdfvV3YvIzMPtq9ohPmizOYg8FhVaoz5n-K6SUvfsH7Ie8cqM0uIPq3J7eHidBG0WyXbTkX5RT-Z8NpdQ-IK72_ffruy6QSG3vBK3026hhQK3yty1W4jA4D1Z4gVj_f6d_tT1n2HCW6AWHEj7BptAa3AhqEau5iONYyXKMnkSeRTKy-3QFHFx3SNvwieivBzQqeP8Bs5m7OUy7mNEQW20s02XWzjmheqxQe_80R7vt250olML3035KtmN2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c26d94481.mp4?token=TfcFrs9PcfgLPFc7PRhB9yTvwKyTpDRu7ggWGtIoFFeRRmO_dQzCiNYKrrvpG9U3YSpcv8KDO8uOxh5FD9gmJvMEJFsdfvV3YvIzMPtq9ohPmizOYg8FhVaoz5n-K6SUvfsH7Ie8cqM0uIPq3J7eHidBG0WyXbTkX5RT-Z8NpdQ-IK72_ffruy6QSG3vBK3026hhQK3yty1W4jA4D1Z4gVj_f6d_tT1n2HCW6AWHEj7BptAa3AhqEau5iONYyXKMnkSeRTKy-3QFHFx3SNvwieivBzQqeP8Bs5m7OUy7mNEQW20s02XWzjmheqxQe_80R7vt250olML3035KtmN2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه رفتاری در مترو سالمندان را آزار می‌دهد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465498" target="_blank">📅 15:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465497">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">استانداری فارس: انفجار کنترل‌شده فردا از ساعت ۱۱ تا ۱۲ در معدن بولوار امیرکبیر شیراز انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465497" target="_blank">📅 15:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEr5ZeReEEcLt2QKpc5HTpeBxaCyp4zMZ-R4UxdH5ABIoJxAVDrxxzvCoydCu8O499mPbvNS0ReUdcoqJVzz6dkYc47JSCv18OO8IY5WBgB4BLQloibp1JCTrx6MGv0T32b5rx71c9i2Q2Ca3szvTfdZBGAg5PU3HtLqQUhgkLXTVsJB97xjk78A4Bs3OZNvdZhqsXo7zazmpBsvYc46HJ06-VL87xL0PYsMV4scFkjTnB0rs79pYP0DK9zLYExmVUFV-QZ9JS-axK1OYv_IhH92mbRKH1NmXauujfZav9dCkM6PkQ8vViczaid6h91D5yKYRmPkheLLfUgmL5fGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«
سرزمین فرشته‌ها» نماینده ایران در اسکار ۲۰۲۷ شد.
@Farsnart</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465496" target="_blank">📅 15:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در حوالی بلوار جمهوری زاهدان
🔹
دقایقی پیش صدای انفجار در حوالی بلوار جمهوری زاهدان به گوش مردم رسید.
📝
تاکنون منشأ این صدا مشخص نشده است و اطلاعات تکمیلی متعاقباً اعلام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465495" target="_blank">📅 15:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465494">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در حوالی بلوار جمهوری زاهدان
🔹
دقایقی پیش صدای انفجار در حوالی بلوار جمهوری زاهدان به گوش مردم رسید.
📝
تاکنون منشأ این صدا مشخص نشده است و اطلاعات تکمیلی متعاقباً اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/465494" target="_blank">📅 15:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465493">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71476756f2.mp4?token=KXv0m2x3MFTVE96TpLs--0Vc7Lz8wvgwhD--2RfEjYDKVkzyUvtydS7RmlTVEh8KCApJuf__954wzkoxYfpfLOIkKQjHxy5TGqPeBA2fWEfN5zgeTVHyKMDR6Ag-iJ48FksYx1QRZQXL_VhNB3AQUQRWjYVPM6GElNOsp7UgcDafeQoEQFgExPogvM4uGQeVqXq85yL4uo71ThpQQUuJb-31R60P_8T9grU6SD_o7L9JSGorgAMjfzT571h2miIdEeD65qSFXHuaTJvGvHkXr4Qe7ScakOIkxZECXY-7f08e7CYJmloWD-mfiv29oV5CSfuo3HURFczud3Ev25KIBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71476756f2.mp4?token=KXv0m2x3MFTVE96TpLs--0Vc7Lz8wvgwhD--2RfEjYDKVkzyUvtydS7RmlTVEh8KCApJuf__954wzkoxYfpfLOIkKQjHxy5TGqPeBA2fWEfN5zgeTVHyKMDR6Ag-iJ48FksYx1QRZQXL_VhNB3AQUQRWjYVPM6GElNOsp7UgcDafeQoEQFgExPogvM4uGQeVqXq85yL4uo71ThpQQUuJb-31R60P_8T9grU6SD_o7L9JSGorgAMjfzT571h2miIdEeD65qSFXHuaTJvGvHkXr4Qe7ScakOIkxZECXY-7f08e7CYJmloWD-mfiv29oV5CSfuo3HURFczud3Ev25KIBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش همتی به صحبت‌های وزیر خزانه‌داری آمریکا دربارهٔ فروپاشی اقتصاد ایران: جوجه را آخر پاییز می‌شمارند!
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/465493" target="_blank">📅 15:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465492">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedefb8419.mp4?token=UnwrSBX8ZHbpXlLMX_iIZN7VUd20PXmaqfSToXyGvLpkaUm6n0HUeX26-DicaA0fDN2mi_htBIBvBQc-gaIv3hegdvkTvqgWmi50DYEXGEteWl2KZe87VuugUajw3xNdUnzDf5Ix7Z_zKgXIRnt_hYXJZYd4JoHz6QDfUcqGzWlKRpVBqxQIHPQfPeVT7INxDNfgxGdaU5W4Tn-zU3ciJ_2mZ5KIZnfuswJYS0-OP45QJH5ThhK3pVHE10UfFfgXw1FM3Fw6D6wSlrCwYRXZi6XXN4SQKBnLJr4yiJRb_7rMDDyySFJnsM9LbPTBYXVfHukH2MpHkdE2ev2EoHlaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedefb8419.mp4?token=UnwrSBX8ZHbpXlLMX_iIZN7VUd20PXmaqfSToXyGvLpkaUm6n0HUeX26-DicaA0fDN2mi_htBIBvBQc-gaIv3hegdvkTvqgWmi50DYEXGEteWl2KZe87VuugUajw3xNdUnzDf5Ix7Z_zKgXIRnt_hYXJZYd4JoHz6QDfUcqGzWlKRpVBqxQIHPQfPeVT7INxDNfgxGdaU5W4Tn-zU3ciJ_2mZ5KIZnfuswJYS0-OP45QJH5ThhK3pVHE10UfFfgXw1FM3Fw6D6wSlrCwYRXZi6XXN4SQKBnLJr4yiJRb_7rMDDyySFJnsM9LbPTBYXVfHukH2MpHkdE2ev2EoHlaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
محل‌های استفاده از طرح «تورم صفر» شهرداری تهران را بشناسید  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/465492" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465482">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHLiMJhpHdIEP1xO0fVlPuREEMceDsbnrWfZXISC2BvBSp3CkbuRTlybr3QrL5oI8p2FNI9t-rBidhXZYQu7XGtqCzcMYzzRE04645pv5NiVC7TW3WRhP1aABHTnQaXEErSIofMlcWYxJ6z1prENmn8g4RA0xINs9hkASs2IrPqwQjyNm3cgDHsz6z4TG-ZZaTgzxDzaBrKwhmXZMiIezDUzLqugk8KbKFfWpvrFT3mdBGdQ5PfUktlwlmqfIUFjjcvWdcKuZfTBXrTvQrv_jErF4OSp_aZGs3PH-qH6Cf_Z2TY2dfRxsrbmP7a1QcfDRaD8SqRSQstQCOI1RYfefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atwR5IsJhxk9NKsdJhjdAO-NSueRpUl5UXwDYn8Iolf51yIFFHJ-dzGtO74EFuOt9ST540NqfYv-tXIVzO_RH4CY8GLHtKk3zxiXL_Uqz2fQ2eIVCSvOpLU9zptH631qFb-BXiVeT6sXzn3O5gPcXTrprvDM-pPaGWNa5JhRpEt-v3kWOCff8ju6Dvlgmdi5YQJSe6-Au4YIT9cKuYyz_7AujHHMdZcv5pZEoqfvneXvgtAr9YTGzIn7pCqLzpeQ1-bNGxRdDvUfKKJAFstQwqkl0SW5RCkLr_Th2zbyIES4O2fLkOvU-GmtsuiiB5kCN-2xAZwjQj4QsYornhUBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1wbTozMZZD6ugolY_zrebLGeX95j527jDDQ6Cd5Oyi8NB2yMub3RToYN3voFaOiVmuPY7Ke51o-2hOohpnINonBLMWXbdDpJJ3Lt-qxEl1Bp-hC-D1dl_PGEvMs8NexVk2HRByHqd57QbbBzREiSA-LJCutddX1P578xtsUUB_gziwykZO5fS68d4stnytcnNPnEh2WJnxTRRW43c4OLIbl_UQJUnArxAQN7s486TS9xaEJQzU6VJawd1VFlsTRe5y-gdhs16-nxNKhrMwnN_KCJ7UBhvQgb8odXGnJkVrNBFaLAt9YV-EU2Jd8JuAxxe-df82bfyu4RsobsQfi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQtFrlH2tSM_2QBzl_Ips7tRqwM_ZR1CzekuwSNN06Ny3ZTtnBnMFTfYMESzdUSrj-vVSaCxBj9HW_djNyu8dyRpqnLnT2T754qNtN2xJvFThRaJ0Hru34vF1TlsUfIw5zqo7il5PhCe1ovcRDVsppyuqd3MH0qnwqoVocU6YoDAVXR_r6YQLFEtRlpq5vseTRKQFy8SWjrbkrjIYEigyyVQ6RBH74LLyPk3vjpDLhQ7GP0T0MVexvreQJoJMpVwvU4w_wN8tLfmlZ2j4xnffgKjUEZ5_BnwYZV879zRDluR28UWDgbSldeF00_3PhVHlhvMY1E8Iek2mFWrZEPtXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNLaznn3_VJ_81XRR-QOnopWQI7Dw4yDAcG-rJsyplLvswxpq5A1FZ4QN-3sBYnA6_Bhl8mStGk3qTTATUvI-q3X0jeGQEAdnzUwhMxqNdHq6yzJe35JrFNbecJlfZHD4k3BGvkmL06OIzzgiI4-vUWTWSinJp77x7ODfkyRwfA0XaFwYVSjx2OOBLY8k7luR-uB5N2SOUyCtZQZbzvJDSk9FmrwMeVEHMFlQC6dJ8rUCOQ8QBc9Md-Y7l77AoyrJFOXpigSMLh1soImV6_CXSJw_AKtMNivkhBiSr3ejkTBFylh29_MFnsFMXTLDXXGDSXriAOKBwfL7_3jnTKrXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdkDJ62sIBhqv2MB8jYRgX1mBYhESqhGGS_B9_j7Uy5jhXU5SIzLGTQy3Tm3_kf-LiplX-x0tzzl0CYBneh2go1cWdIMP0XoJU76kT_4bHYlplz6_lEedEUzFmPiEUxxeR6-aGnPB9-yHGBa4BVFWb1C57uBnipI7kc00BCtcH1h1mSBch-gnZZkXx_QC1e0D0AozFgl5bDPGodbqhwtYtY833Qtpr8F8lhiFqzwtfYm6WpvE8rcUukY_1No3qVbgYXCGUb55n7i8oOb9rkKfh__lR9Kr6YJpoiHFRzlyIAuApTYrHCQNs3sets0MtPbymLIN-2wmlGVfezIAeMu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkdj6UWD1DQJ-9gNkAfHj2cy-M8K5D24WD00pYOy6phDjHFwR1xFNHe7dCm4KFPKfLZ56f24TUhiHg8zVQUS7ZDUxlQhb7p4T6QSM_U4MXpaZLBR0MnQ-pvomPiY1c-sHHWGrtL_R_0H-uFR6CHD0HwQDB_cD0O1VZYShTwUrIV2pgCkzA2FgZvnVzdGsg3E8rXX4r_t4zbJb0o81x_L8_faE70ClPOih-hpVgfPalABeOFj13RTnC6fHYVWCRHVax4iM_j0_DKjrzwcN-UbIteAqTOY5GCWJpVorTY4yBOIE2l3IHfTytj4j3aDklk3WNWaAd1N8pwVBxVSSLhFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L0v9SHiB0zqnVFhAT5Tw5hfONMLkc_vE2OBXWfgoeQ4QIvrehMnaoWx7RwqHMk3wc3oRl7268ZnFiJ2BKrtI-Lr9FHA6s7gzNmoCT-MMOhpxMsHaY6kSEKrxcvmaUXFSBmaGTyFp2lAyxOttgD-7vDGo4WBK0k9MC2SmH_Y1FjTzeZWnuJD6KfoLFcar5T5vKa9rrCuonOmS0AOQ058_SUJIO69lPC0p2aw4htMxq4qjEUQk_XX5X2d1uVEJ9-jjroJKMv65LMD9xYQJ1fbNkOGoz25HbVOA1Nbb2Xyl_M9U-12wXsiSmGBa4ZzYJw26C70xIePHn-0SvcctsiBiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqihNawNpEBBBQKVK0O1k21ZbBUu1qmL5CMMVMzzvlG-JkfmERgm9iq1_kZXzWyaLzkoxQ9DEZoNp4ktYO062BONLipwaSm4cQ4W18xLTDj0_EnC636XVwXJdNKW2uf83cqSehdntLOpfdz9dMO_gN-Fsnwi3NIZxfyM4k8dygFN6jFBz0qe48Gpc4WUaV18ldQfN1eEQOyD-WQCRIvTY7ugggMsPSaeLzVPd1fj_4njkFBd3tFtg90g3HlaI7Bv2TrZEopuy6eO42atiEL4bbhjqGWwY-Cuv2lvPbXybmn-zTFwCqKNHmtV_Ss18yOHmSJNWZQLgajtK0pYNyi1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYYnGpN16NaXc1Q753bk13x1qlkFuao188aIKWLiMZtPZnk9NKqbFSJJMcsmQbMkcMVnnRkVZU9DM-7XW0NpxbhP3ywQdODTrgTYr2oSDp9omV6SnZmYzP05XGnOFwYfZu-v6a84JLSDnVAVG9scgBWrFokfHKCngRgqBJt4NDnStLUXp2z2Enn68qvJUPZ2COQNjhJfZaKE_5aJz9aJVPLdRNSHISCcjBFMJ7Ffo8GxMrZzXwPJ4jXifG3Ab5rdKg9TzXHP94-4c4MjxWV5Ucoe9hcq4czrJctDcXnpJqSdrOlRKmOQovOqpMgXw_8nOJT153sBvsYVWsyh_A1DxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی شهرداری تهران: اقلام دیگری مثل مرغ، رب و پنیر به طرح «تورم صفر» اضافه خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465482" target="_blank">📅 14:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465481">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4e72c264.mp4?token=MeUf4QkLDykCQz183E1ZO00-Q5T7ODB2nj7S8pnJg0kGSBBYbVxhIpabiz5kO005H38a0LKaMLP2UdefxygA22dgyYUmRg9YXhk3TDQSmMXBI1jZs4DYhr6VQp6Zb7oWz7RfWa-m8Mt5TxQhSXgvLitviS62Oq4Cbpk8FggwuaZFwPQm-SVnrTTOyGG8wF6QWrTL7xrAKSvDV-WIIt1tczE1nM33qUlvWhX3lTrxpJOY2R85BgkLip3BDScBYS6UwuPguua7mh5wWQnE3lJAxMLLg-Ssk8jj0cwWeWheJslpv-3he0xOrN8SQhcRTaxokSJFWjU0IDlNyGilLmUBSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4e72c264.mp4?token=MeUf4QkLDykCQz183E1ZO00-Q5T7ODB2nj7S8pnJg0kGSBBYbVxhIpabiz5kO005H38a0LKaMLP2UdefxygA22dgyYUmRg9YXhk3TDQSmMXBI1jZs4DYhr6VQp6Zb7oWz7RfWa-m8Mt5TxQhSXgvLitviS62Oq4Cbpk8FggwuaZFwPQm-SVnrTTOyGG8wF6QWrTL7xrAKSvDV-WIIt1tczE1nM33qUlvWhX3lTrxpJOY2R85BgkLip3BDScBYS6UwuPguua7mh5wWQnE3lJAxMLLg-Ssk8jj0cwWeWheJslpv-3he0xOrN8SQhcRTaxokSJFWjU0IDlNyGilLmUBSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا  میرزازاده اولین کشتی‌گیر فینالیست شد  امین میرزازاده در نیمه‌نهایی وزن ۱۳۰ کیلوگرم کشتی فرنگی با نتیجه ۱-۱ مقابل منگ از چین به پیروزی رسید و فینالیست شد.  @Sportfars</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465481" target="_blank">📅 14:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465480">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a41ec659.mp4?token=Yp02HMUwZX4C0UqdGN6ociD_Uxa_8KZv9gsHHdelz8LC6O3iQv3DfWzp3Ql35JG0VLQCz8G9g8bUIuaPmcgKCUWEIfYk7U5shs6_3lrxsNDubigxWwysrzwa7oAVNpAyGgvs_y4Sfh6dm3d3rISxOa6r-kXceZCBp6pP-0r1DBK0HlgfjKo9OjQ9CslhiRFwvqzMLeDhSuw0RRvUKtN1CSwH-JiYi0MXjxZpUIixkMhKPN0PvBnNWxa0lXK68s17I0n4K4sGHatvHZzGpWwhnAzWgVZguoEJFcPb9R8TqxcLvuM2ir_nisguEklruonpTRNl48JHstIAsOKFay5Sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a41ec659.mp4?token=Yp02HMUwZX4C0UqdGN6ociD_Uxa_8KZv9gsHHdelz8LC6O3iQv3DfWzp3Ql35JG0VLQCz8G9g8bUIuaPmcgKCUWEIfYk7U5shs6_3lrxsNDubigxWwysrzwa7oAVNpAyGgvs_y4Sfh6dm3d3rISxOa6r-kXceZCBp6pP-0r1DBK0HlgfjKo9OjQ9CslhiRFwvqzMLeDhSuw0RRvUKtN1CSwH-JiYi0MXjxZpUIixkMhKPN0PvBnNWxa0lXK68s17I0n4K4sGHatvHZzGpWwhnAzWgVZguoEJFcPb9R8TqxcLvuM2ir_nisguEklruonpTRNl48JHstIAsOKFay5Sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرواز ایران و پاکستان باوجود فشارهای آمریکا همچنان برقرار است
🔹
درحال‌حاضر هفته‌ای ۸ پرواز بین ایران و پاکستان انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465480" target="_blank">📅 14:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465479">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOx-Wt5nMeeT2F7aIvX_Tn2ohduZ6kMSbRlO3B1ciDh_VxoZ4oaGPLoMzeDawLIlanmOUsD6vOnqlDjlcbkrIsFkVqT5VEaq37LHrNYPCI2WgtgyBqDm8_b0UCJWOZR8_-2VRikX-p6Xod_1cs3JHnVuEGIobh-3VlHugs9oF1vzhw7iAYqdDd4bklZ5Y2yZLKHKS8EHvySLrJ1_1Hte6z2NeF5g9pLHVuv8QH9xJz5hRnqd22JgSzfRb_5t-g45RZaC21hCv1ZKXB0jkFCf6nSeTri5G_tWmrVGpGg7Je6pd-8xLetVLw3FvVAm_7HssyU7OHWnzJDeZxWb9kLhiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای کشور بارانی می‌شود
🔹
هواشناسی: امروز در مناطقی از شمال آذربایجان‌شرقی، آذربایجان‌غربی، اردبیل، گیلان، مازندران، گلستان، خراسان‌شمالی و شمال خراسان‌رضوی، همچنین ارتفاعات البرز در استان‌های البرز، قزوین، تهران و سمنان، رگبار باران، رعدوبرق و وزش باد شدید، پیش‌بینی شده است.
🔹
همچنین برای فردا در شمال‌غرب، غرب، مناطقی از سواحل دریای خزر و ارتفاعات البرز، بارش‌ها به شکل پراکنده تداوم دارد.
🔹
روز جمعه نیز در مناطقی از شمال‌غرب، غرب، ارتفاعات و دامنه‌های البرز مرکزی، نیمهٔ غربی سواحل دریای خزر، موج جدیدی از بارش‌ها آغاز خواهد شد.
🔹
در ۵ روز آینده بارش‌های رگباری، رعدوبرق و وزش باد در مناطق شمال‌ و شرق هرمزگان، ارتفاع جنوب سیستان‌وبلوچستان، ارتفاع جنوب و غرب کرمان و جنوب‌شرق فارس، مورد انتظار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465479" target="_blank">📅 14:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465478">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6abeac4a.mp4?token=JJzEMM8jUcIyom_YkIM4S6wMAHpA0Kk4gWw-SL60jt2vT7INrdJHVrlyahV36UxNak08l-K4sXKxKofrhlgi-GXM6zdswwHaV1JYh9OEFJR32TtxxgnPDBQpZ4Ja8wamprhtPhAdGr0Z7oU5hnmCr9hWj7ind_TtWSr07YXNTgcFCogCdoCH6XMeGqpppeWVn1Hns0j6i3blNgUkm-hphB6Fp0Tg92EmjgAemmExI4EGBOvdfrUSbn-3rpby5ECUFG-KnifSGfDFHde449bQa0MOvJ6aeSn9TiI9laSPmoS72PWzFw_d6-S5zpUXdmVK5T5djprSVtv6kGvyXASMdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6abeac4a.mp4?token=JJzEMM8jUcIyom_YkIM4S6wMAHpA0Kk4gWw-SL60jt2vT7INrdJHVrlyahV36UxNak08l-K4sXKxKofrhlgi-GXM6zdswwHaV1JYh9OEFJR32TtxxgnPDBQpZ4Ja8wamprhtPhAdGr0Z7oU5hnmCr9hWj7ind_TtWSr07YXNTgcFCogCdoCH6XMeGqpppeWVn1Hns0j6i3blNgUkm-hphB6Fp0Tg92EmjgAemmExI4EGBOvdfrUSbn-3rpby5ECUFG-KnifSGfDFHde449bQa0MOvJ6aeSn9TiI9laSPmoS72PWzFw_d6-S5zpUXdmVK5T5djprSVtv6kGvyXASMdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم اروپا هم هزینهٔ همکاری با متجاوزان آمریکا را می‌پردازند
🔹
به‌گزارش فدراسیون حمل‌ونقل اروپا، قیمت سوخت در بخش حمل‌ونقل جاده‌ای در اروپا به‌طور متوسط روزانه ۲۷۰ میلیون یورو به هزینه‌های حمل‌ونقل افزوده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/465478" target="_blank">📅 14:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465477">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF-pcahEDB2X_V_5ZZPHIBjMow9uEJ9Mu8PjEmBqpicUkws7r-ORNInjnHT56_5NxgR3RDZvGpEb5SXCmFUNmMOmx-eHzVME6_HOOctXi2UsCyPtbDjtcIcT49iBlJvHDx7VDGtJ6OvuAkQVtEdeAlFSL_PACb7eUL9zKjHmt9rR5soRgdkNMoBiVKYqtNuzSZRS9_IZvZy3h4hyOlt37ALyonBM9AQGvrJ_Eoq_sOtrD2HU1IYML16NX0zDkx5fcjAbuFNhVeOMDHDKCUTH75CXNvTzICqFU0YaJcykwrZ3AWRhykfqR36leWInFgc538mE9fzBOFKAztn9QMmJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
در ۶ ماهه نخست سال ۱۴۰۵ ثبت شد
💍
اعطای وام قرض‌الحسنه به ۹۵ هزار نفر در بانک صادرات ایران/ رشد ۲۵ درصدی پرداخت تسهیلات ازدواج
🔹
بانک صادرات ایران با پرداخت حدود ۲۳ همت انواع وام‌های قرض‌الحسنه تا پایان شهریورماه ۱۴۰۵، به نیازهای تسهیلاتی ۹۵ هزار نفر از مشتریان پاسخ داد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#تسهیلات_ازدواج
#وام‌_قرض‌الحسنه
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/465477" target="_blank">📅 14:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465476">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ3FZlhBPPPGJ_j9y75vKJYqWXO17NQNPDUjv4b49Uok-l4Y5E4YWAQdjyfnPDXHfW9EZ96mc6aOtMeaSfsar9HAXnAF_gpKmLWe8fhp-NWGvMVSQ0n4OSlu331aTi7ir9-F4l145cP5F2FwyEZ-90LTaNL-kcEIYYKI3-DdvJu8sL5wrW9AJ_mFUp87Q5YiaPy9nNJ3ovVip9t3f6DNgd6sSagItn7wZkCr0G2VJVr34qcucAj2Pbj0tUNiL05HbRMtWKP7Qrju1a5xBkHNupoH3DWdzqojqHZN9MMEzwaCAsgZaTYwrE7_s8Q7Jj959YxloqL9M0X3rsWtRQp7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/465476" target="_blank">📅 14:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465475">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/465475" target="_blank">📅 14:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465474">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار کنترل‌شده در تبریز
🔹
استانداری آذربایجان‌شرقی: احتمال شنیدن صدای انفجار ناشی از انهدام مهمات در تبریز از ساعت ۱۳ تا ۱۵ فردا وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/465474" target="_blank">📅 14:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465473">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf3cf9fee.mp4?token=EkwEdVsRudictTKD7YF5NySvFUxs4V9ldVQf8vJHj7kyija9E-Y4mhRvcSCJLrUJPRCS_YmzU6I3y3yjwv6ERRnK38IiyAauNEsMMdmKIvGY6HZyYW7qpt3bpfHYFU5r-s4waR-3uen6Jfmp_SBIwSFYaMOeypaP9Ls3lMxPmeJ5mnxXOAmz2yfc_HGmv2_Ry90PUgrzwD-akWD01wqHB9WCKkyEsvTq8xJ7j7ZMJWdNEUcc-b2iGjcbzUeFicxk3yiEMSAzY9yEXogIHlxYKVG_wpnbcD6R1Ma3UDvIZ84Y47qZvUEzPqnXv-RzD-R_U-dlZIReKwT0GmgG3qv0hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf3cf9fee.mp4?token=EkwEdVsRudictTKD7YF5NySvFUxs4V9ldVQf8vJHj7kyija9E-Y4mhRvcSCJLrUJPRCS_YmzU6I3y3yjwv6ERRnK38IiyAauNEsMMdmKIvGY6HZyYW7qpt3bpfHYFU5r-s4waR-3uen6Jfmp_SBIwSFYaMOeypaP9Ls3lMxPmeJ5mnxXOAmz2yfc_HGmv2_Ry90PUgrzwD-akWD01wqHB9WCKkyEsvTq8xJ7j7ZMJWdNEUcc-b2iGjcbzUeFicxk3yiEMSAzY9yEXogIHlxYKVG_wpnbcD6R1Ma3UDvIZ84Y47qZvUEzPqnXv-RzD-R_U-dlZIReKwT0GmgG3qv0hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: در هر ۲۴ ساعت در تنگۀ هرمز درگیری نظامی وجود دارد
🔹
مدت زیادی است که ما کشتی‎‌های کوچک را مورد اصابت قرار می‌دهیم و مانع رد شدنشان می‌شویم اما آمریکا پاسخ نمی‌دهد. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465473" target="_blank">📅 13:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465472">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ6IjV3iSk0j69giiTkfopKH7eLyk4C41iC1mDC4y1aKpHIURokkEAX7idFWL6_YaPsyWnfYslTRIQ3mHkh3zc9lAvc5fHh7qZSBiC2kFE4VgSjTK-cGCAQafVmZR4oHHkNyTPunBtcHweWv8ugUM-_1OzniWNNa7g9VjBDnX-xc54SeWptfuyCrXGlnEa0P9LFcmTN90RKXS_0J7ZdqgREmPVdZ8ZPMVdaNphUyJ4uLM5PwE4BNNzVILJIQPR1KyXMiOWT_79BehXHtjeiYSZA5Gy_NMVED0y3y__RJDp_0kYaTGrnQVW0f4DasX2snU8h_w-yUei0bqXISfTNVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای دو خلبان پرواز امارات به اسرائیل را نیمه‌تمام گذاشت!
🔹
رسانه‌های صهیونیستی گزارش کردند که پرواز امارات به‌مقصد تل‌آویو در میانهٔ مسیر کد اضطراری ارسال کرده و در فرودگاه تبوک عربستان به‌زمین نشسته است.
🔹
به‌ادعای کانال ۱۲ رژیم صهیونیستی، علت این حادثه…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465472" target="_blank">📅 13:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465471">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f5666f54e.mp4?token=VEdV2ugXyStA3b_e44qR1VpQWdVyjMTsfh4fSlnRLABLZq4YRbvX9e7jNTS7V1faVhnCTZpTGp6FyMOiRGN1TMCeEVHIqvIVGW-NCOMce4FiWDwaGdUqPdmkAaQsfXD3QhUBe6xGl6N4CT1iRNuMXPzJTMJcnnmmX-NOo-WZW1iCE_seDMs2Ss5MkW_kGXblRj9chMyez1JuP5B2MHe_KI2SIcDJOGpiRi1SdS0yzEnnyaat4TytDKviOW8yT_bq8GGgEZ7iMXDzrbbzxn4cwyoyjGKpzapVRPqbWXL4ww3SPR2UeuksJHClc65m1jnlGLwBK2Re7zv54q1FIzRT7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f5666f54e.mp4?token=VEdV2ugXyStA3b_e44qR1VpQWdVyjMTsfh4fSlnRLABLZq4YRbvX9e7jNTS7V1faVhnCTZpTGp6FyMOiRGN1TMCeEVHIqvIVGW-NCOMce4FiWDwaGdUqPdmkAaQsfXD3QhUBe6xGl6N4CT1iRNuMXPzJTMJcnnmmX-NOo-WZW1iCE_seDMs2Ss5MkW_kGXblRj9chMyez1JuP5B2MHe_KI2SIcDJOGpiRi1SdS0yzEnnyaat4TytDKviOW8yT_bq8GGgEZ7iMXDzrbbzxn4cwyoyjGKpzapVRPqbWXL4ww3SPR2UeuksJHClc65m1jnlGLwBK2Re7zv54q1FIzRT7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: در دروغ‌گوبودن ترامپ درخصوص باز بودن تنگۀ هرمز تردیدی نیست
🔹
وقتی که تنگه باز بود روزانه حداقل ۱۲۵ کشتی عبور می‌کرد اما الان روزی ۷ یا ۸ کشتی بیشتر عبور نمی‌کند؛ آن هم کشتی‌هایی هستند که از طرف ایران عبور می‌کنند.
🔹
دلایل ما این است اگر تنگه…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465471" target="_blank">📅 13:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465470">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHpzhRB69pWfRUf0tKaH4HUDu6y5nv7Xw64ZIqpTuP8m4R-ePlLrbqp3ABYjrnGfYc3Io50vmnA-LYcLroUvylDNwdys9wx-9M8YvZqI-Xkt2oq7Tj0Lz-ptTX6WhrRqzB18rzZyt9n_5VdBx2rWGekUjXqBzb3T6dAMnroArxD9dawLsqOj-0aJhHuqpxpTv14EnDFFgya6M8Y2718bbzu-1PquXDWGkJyfCX8-iCf36-Hu1O-KVnmiouLTjZ-y1oXahzdy5NvTf-kMamaX3bxzr0ZyNYutM9IJLnimyzu9ULXYUoMyCQyoVjh5IIeviUzk8fCJLNmM6uKLTba7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای گوشت اسب و الاغ روشن شد
🔹
سازمان دامپزشکی کشور: تاکنون هیچ مجوز یا موافقتی برای کشتار و عرضهٔ گوشت اسب، الاغ و استر صادر نشده و هیچ تصمیم اجرایی در این زمینه گرفته نشده است.
🔹
کشتار و عرضهٔ گوشت این حیوانات تخلف محسوب می‌شود و با موارد شناسایی‌شده برخورد قانونی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465470" target="_blank">📅 13:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465469">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d1782b96b.mp4?token=WCPqpIUgagEEuWh9q8iRB5KRdo3QrqwcHPnAYooaATEvgjnZwgmp0h6Feqn8PgjrmxCv64H0oNm1H6wtL0zWd3jccRg5uzI4ftrf0D81mro7ssBRcXucBzS6QVzx30esHPjvAXx9XiWa4Guq96Ke2IDi3ct-TMuMEkQ2cspo00TB28wbRUaVRcv1o1f5Ga_beBaLZxgYKOR9GIGDaDFA2aeWy39dJN61D1h7jplC8tNQNUrRBvTYHSyyGQ9zZX-IVYhGIKx1Xxuf2PMBQRwObfTV2c-SnbJyxQV6OmK4TTv9x6cNwmEX5aDXHXJ0kjsW2QoHr0gIEunGnyO2Ev0EFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d1782b96b.mp4?token=WCPqpIUgagEEuWh9q8iRB5KRdo3QrqwcHPnAYooaATEvgjnZwgmp0h6Feqn8PgjrmxCv64H0oNm1H6wtL0zWd3jccRg5uzI4ftrf0D81mro7ssBRcXucBzS6QVzx30esHPjvAXx9XiWa4Guq96Ke2IDi3ct-TMuMEkQ2cspo00TB28wbRUaVRcv1o1f5Ga_beBaLZxgYKOR9GIGDaDFA2aeWy39dJN61D1h7jplC8tNQNUrRBvTYHSyyGQ9zZX-IVYhGIKx1Xxuf2PMBQRwObfTV2c-SnbJyxQV6OmK4TTv9x6cNwmEX5aDXHXJ0kjsW2QoHr0gIEunGnyO2Ev0EFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین سوال مردم: آیا دوباره جنگ می‌شود یا نه؟
🔹
سخنگوی سپاه: ما الان در جنگ هستیم. به اعتقاد ما الان آمریکا شرایط قبلی را ندارد اما در دنیای جنگ همه چیز محتمل است.
🔹
آن چیزی که مسلم است اینکه دشمن با توان ایران و ارادۀ قوی ملت ایران برای ایستادگی آشنا…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465469" target="_blank">📅 13:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465468">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mO6GPm2onqp1WyF1HGcsT9Em_W5n7Tq1eJQUp-xVk_gvGudfs0LCMuARRWq5HO17cTFrMUZJ7wqNz-QpqxmT37MZnAe_wo2A8RNOpzk2vcIgdGFTjlpm1j2MtCB8ulgt4Lwu2bJWX6BEOh4Hm5qVSG5x4DFnH62IX07ttVeWF8CEbKL0QyhVMFlX6EI3Pmq2Qpmit2mmalxCeLpDX_0QxQCV0s2NalhwINsecRaWmbQ1jIxUykGercpSGlf59TLul1SC7zZkLaZ_cl1Otcqxx-l_uoaHSHsuuUrAwry4Eo1Sy47Udn8jvd1bZ_hCFZDtOaB4VMPKaKLk_QRDJlQ41Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعام هنوز درباره انتخابات شوراها نظر نداده است
🔹
علی‌رغم انتشار برخی شایعات درباره تأیید شعام برای برگزاری انتخابات شوراهای اسلامی شهر و روستا در ۲۴ مهرماه، پیگیری‌های خبرنگار فارس از وزارت کشور و هیئت مرکزی نظارت بر انتخابات شوراهای اسلامی کشور نشان می‌دهد…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465468" target="_blank">📅 13:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465467">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzwUzMcbgslW69XXVfcuRob28AqYo6gsBYxn6pEH-8zVmQaYgIQDIhjp97Z_RA8de5TNTJtVq2NpuAtl3J5XtEgay3cvctB1n5XTRftbagSIv5rncg-6Xq5GqQ51YXfPIbwnI3fUly5J04G3sZ0fvYEIo3fgITDwb-YRWl6IOZ1N2D3pYxV-l0V1uKIK-hWR7xjPK1Tf3EQgf7t-0fclniLA6I8Mst2f9PtXZtAD17mXEO-juOVFBdC6rXxJMJkt-JeLGAlJjbDNKH--1Y_nhYFcRQKFQNqlRpAk794_KjuoTgqsjU6GzrRq_gm8vf3lp-4_opK5YFL5xRGoH5jHGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش در تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناخته قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465467" target="_blank">📅 13:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465466">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF-tqikOshohQLbP4k8UP1eBKvsL-f8td3x5ssTJne5_C9T-9VgTnRZrIPmsCxeLWiPkAIkPS54Kh2rXl8IQN0U9GUxBrqSMfNdVkRHqC2PAKwISh-cEYS37L-2Tqxw3KRSztJFOx4ilL7HfmyFnu7YKBME44b1na1J8_MaQ_W5K6n5k3zghuRCys2KewKeaJAn5w0OlsQuCQ_t78HPbW6unfaLh7OSt5UbUz5hbtDEW6Loo9_F_cxYkB-XaDz0kN11PfJrQ_Kz2_xQkIX6MiMyoAdFNg-Q_m57QciC78U3rL79FtJwL93-1ceby7XXD9MS4S2-NK01xZ6tpetG-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروازهای فرودگاه ریاض باز هم متوقف شد
🔹
منابع خبری از توقف مجدد ترافیک هوایی در فرودگاه بین‌المللی ملک خالد در ریاض خبر می‌دهند. این سومین بار در هفتهٔ جاری است که پروازهای این فرودگاه متوقف می‌شود.
🔹
به هواپیماها دستور داده شده تا در حالت انتظار باقی بمانند و هنوز دلیل این توقف مشخص نیست و مقامات سعودی درباره آن توضیحی ارائه نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465466" target="_blank">📅 13:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465465">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">افشای عملیات جدید موساد برای اجماع‌سازی علیه ایران
🔹
اطلاعات دستگاه‌های امنیتی ایران نشان می‌دهد رژیم صهیونیستی قصد دارد با اجرای یک عملیات تروریستی در منطقه، مانند حمله به هواپیماها یا فرودگاه‌ها و قربانی‌کردن غیرنظامیان، مسئولیت آن را متوجه ایران کند تا موج جدیدی از فشار و اجماع بین‌المللی علیه کشورمان شکل بگیرد.
🔹
دستگاه‌های اطلاعاتی ایران اکنون روی خنثی‌سازی این سناریو تمرکز کرده‌اند.
🔹
هم‌زمان با تشدید تحریم‌های آمریکا، برخی کشورهای همسایه پروازهای ایرلاین‌های ایرانی را محدود کرده‌اند؛ با این حال، پروازها به چین، روسیه، ترکیه، ارمنستان و پاکستان برقرار است.
🔹
در عراق نیز با وجود فشار سنگین علما و اقشار مختلف بر دولت برای برقراری پروازهای ایران، مسئولان عراقی فعلاً درحال مدیریت زیرکانهٔ افکار عمومی هستند.
🔹
در ادامه این تحولات، ساعتی پیش خبر ربایش یک هواپیمای دبی-تل‌آویو با حدود ۱۰۰ صهیونیست منتشر شد. برخی وبگاه‌های صهیونیستی مدعی شدند که پس از درگیری داخلی و تلاش نافرجام یکی از خلبانان برای سقوط هواپیما، این پرواز با فعال‌سازی کد ربایش توسط خلبان دیگر در عربستان فرود اضطراری داشت.
🔹
چند روز پیش از آن نیز رسانه‌های انگلیسی در ادعایی ساختگی، حمله به یک پایگاه آمریکایی در خاک انگلیس را به ایران نسبت داده بودند. محمد محمدی کارشناس رسانه، معتقد است این اقدامات می‌تواند در راستای آماده‌سازی ذهنی مخاطبان طراحی شده باشد.
🔹
پیش‌تر در اواسط سپتامبر نیز سناریوی مشترک عربستان، آمریکا و اسرائیل برای نمایش حملهٔ یمن به خانه خدا با هدف فضاسازی علیه انصارالله با شکست مواجه شده بود.
🖼
اما چه موضوعی باعث‌شده آمریکا و صهیونیست‌ها سراغ عملیات پرچم دروغین بروند؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465465" target="_blank">📅 12:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465464">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8642079dec.mp4?token=LaTpOaNl04Gn9jy4uSVSfmRj3DfFBBZUWqg77iWmlVWtySkO8aPiAbdmFJ3F1UwYc_kGlzcxIFDlQ-5SWc8aiUeBTfY_JBmgEkTig5oIbUE54j6nYwPPp4KwkjIOh8JyykQt-1agygwvPGdaInMvNivG5MBO50CamD9Ge4jlVIcCMb8otWY8CySHfk_47TBZ2uLGXRgxqR5Jqp9W4Zo867QiyY-lCmPMnadcdWwlhxdmZGgL4fwSCypgPbZOATWRRiZRWTgXV61wKcTADVKMmCKr--nXmUteE4fxFLMfw4egNOlhijFWgw6HH72HfjepQ-do8RR38FqXz5Ub3fKLxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8642079dec.mp4?token=LaTpOaNl04Gn9jy4uSVSfmRj3DfFBBZUWqg77iWmlVWtySkO8aPiAbdmFJ3F1UwYc_kGlzcxIFDlQ-5SWc8aiUeBTfY_JBmgEkTig5oIbUE54j6nYwPPp4KwkjIOh8JyykQt-1agygwvPGdaInMvNivG5MBO50CamD9Ge4jlVIcCMb8otWY8CySHfk_47TBZ2uLGXRgxqR5Jqp9W4Zo867QiyY-lCmPMnadcdWwlhxdmZGgL4fwSCypgPbZOATWRRiZRWTgXV61wKcTADVKMmCKr--nXmUteE4fxFLMfw4egNOlhijFWgw6HH72HfjepQ-do8RR38FqXz5Ub3fKLxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر آراسته: نسل جوان شاهد افول سلطۀ آمریکا خواهد بود
🔹
جانشین رئیس گروه مشاورین نظامی فرماندهی معظم کل قوا: فروپاشی رژیم اسرائیل را من هم با این سن‌وسال خواهم دید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465464" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465463">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjdn7uUIFHptqi18QV_JjZXfIUX95ZPdGLmAeodmDPhrj6TFpXBAckls0KUVi9hYqSXC2KmdkoLJEX5q2ygiDP66HEGUOAltPpUdoZpXXr-pb9sC2I7UxI5zqN8McD5j48c1Vk6tMEiiorBNF_Eig-Sf4UOzCJvXm9_KbdWubrdQHr1YFIZclRJmglwCS3VSsiTtVvvC50wjSMunUJA4HKpuR2PIdKlzwMqNgupWCNTge5RcNVS-6GRbEKw-LKbFQWqiLxsyydKQB6Zhl6XpGlIEq5bQuWSFfMw6QE2wwRc2MfSu2emTb-YHF-1moXD9Hvn__ZoK0akexxB1f6rjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردشکنی صبحانهٔ بورس
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش ۲ درصدی به ۷ میلیون و ۷۴۶ هزار واحد رسید و رکورد تاریخی تازه‌ای را ثبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465463" target="_blank">📅 12:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465462">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00999b14b5.mp4?token=sWu-QyPz0vPujwFzTqiBasvDNgCl5vlUJIss-Y_Wk65dasmyraeQcDA0a74I4dJF3JpT2FjacjK0EVq2qytJD_xGluJ-NdM1-70MAIP_5mmd2LRO9dkiPHzHqAql22PZpHHpTVWG6anKFHna1KnbGjD298jpZm8TqnN7tOLMdBOkV5kQtPvFAuQH5kIePkwivU7mWQmYye-ialp7DLs9g690157vCOOvGT6_3BQZ2UYzmTNK6-dINisjWjyYREVNlU_Nj41eQAcs7UHvBL5aUjUxaGqbz5HMZ8L8DVo_QJkYOFwvafaNyPBBe2cR0RSUiqKZtxqxztqd2IHPhN-zkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00999b14b5.mp4?token=sWu-QyPz0vPujwFzTqiBasvDNgCl5vlUJIss-Y_Wk65dasmyraeQcDA0a74I4dJF3JpT2FjacjK0EVq2qytJD_xGluJ-NdM1-70MAIP_5mmd2LRO9dkiPHzHqAql22PZpHHpTVWG6anKFHna1KnbGjD298jpZm8TqnN7tOLMdBOkV5kQtPvFAuQH5kIePkwivU7mWQmYye-ialp7DLs9g690157vCOOvGT6_3BQZ2UYzmTNK6-dINisjWjyYREVNlU_Nj41eQAcs7UHvBL5aUjUxaGqbz5HMZ8L8DVo_QJkYOFwvafaNyPBBe2cR0RSUiqKZtxqxztqd2IHPhN-zkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین سوال مردم: آیا دوباره جنگ می‌شود یا نه؟
🔹
سخنگوی سپاه: ما الان در جنگ هستیم. به اعتقاد ما الان آمریکا شرایط قبلی را ندارد اما در دنیای جنگ همه چیز محتمل است.
🔹
آن چیزی که مسلم است اینکه دشمن با توان ایران و ارادۀ قوی ملت ایران برای ایستادگی آشنا شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465462" target="_blank">📅 12:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465461">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcztMYnpsbTAAr9WQ_-iMay7bkIbZGtk5_mHmhj_ontAOw2bBbqNdyFzhMp9lCWhTygO1w2rY6fCaapO-W7ivrVHfYYwBKZU9XYkvfIP5NO8z22R2D2cfVaFvXB9uXjq4t6jZGyZ2yHk1JqWZm8fjFIffrNq5r53ylAEScUYUF2X41RqNVExFZ5uYqNUKjeMluB5OiPavXprGZ2x5MrzTF-wqJxpOoyorNSyIFOAfX7kzVfVrWyDCEh_HxEbCZ70Ky5appjz3C6mugvMySAWOKkNv4OMcbCeJSA31XK7ecoIUJzprx7Ks0mD8QMDrTAjGmDdJTMBxrnW9wl2V4k4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاصرهٔ دریایی حریف تامین کالاهای اساسی نشد
🔹
با وجود اینکه دشمن با جنگ اقتصادی و محاصرهٔ دریایی به‌دنبال تحت‌تاثیر قراردادن ذخایر کالای اساسی کشور است، اما بررسی‌ها نشان می‌دهد این فشارها تاثیری در زنجیرهٔ تأمین غذا در کشور نداشته است.
🔹
در این راستا وزیر کشاورزی اعلام کرده است:‌ «امروز میزان ذخایر بسیاری از کالاهای اساسی بالاتر از کفایت تعیین‌شده در مصوبات است و جنگ نتوانسته زنجیرهٔ تأمین غذا را متوقف کند؛ اگرچه هزینه را بالا برده است.»
🔹
معاون توسعهٔ بازرگانی وزارت کشاورزی نیز گفته: «ذخایر برنج، روغن، نهاده‌های دامی و گندم در وضعیت مطلوبی قرار دارند و تأمین کالاهای اساسی بدون وقفه ادامه دارد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465461" target="_blank">📅 12:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465460">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhS8RLdF-zu9gPaPAXB7L2-YbYXC1MeKZpd_dgt2h_TOFCYjjKkffLV8un4LMdfZpVBH1dyzicoqmhAuixn60n5RNZKhXQ9k7ygKDkPZczXEfqfBaoQnET-sR7J62w0hwCgBkk8qlOpelUXCEoHrb6RA7L1M6RGII7yqLkkMt0fyenW3fSh8qHbsBKxKktmlof2B5XQ1hP6vj3GgjpcJkkdmQhgGQGvwgHVDPXZaFq0Tz3jKWH3SKxQ2mVfbY8Vh_GeF6g4FvwM5JRKlE2u_zfsMgmb-Jj4Bat_JfSYdbLYmbD4-6tRCzZ8LZQOHrmJ_dnMgBDyGKvuwd6SEGr6Mdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌ حمایت مجلس از طرح «تورم صفر» شهرداری تهران
🔹
سخنگوی کمیسیون اقتصادی مجلس: این‌که شهرداری بتواند کالاهای اساسی را با قیمت مناسب و بدون افزایش قیمت در اختیار مردم قرار دهد، شایسته تقدیر است.
🔹
اگر کمکی از دست ما در مجلس و کمیسیون اقتصادی برآید، حتماً کمک…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465460" target="_blank">📅 12:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465459">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841242913b.mp4?token=pAAG8hpfPliwbDoeWQ8QQVaLdwzb7hFBr-60_DE5H4wt0OioQ2g4jLe1ZuVBSgtSlJ-tcrbi8BGu0UT2_evczhuHytG_M38eML28xprVlz38Iqre_rnnPhXUuS2hJozmwLInuzepTLByNMnpxB6eb5m1YbyIu3nFwljIgcox-CxJcx1hffC87z1e2KvOd1iYrw87a1HRGN_8vC-LER1qNfZhMI_RSd4fWpwmJ63CmLs_wpNv-Dk9y3TPrMbT01EhQbsxfKWwpKtcSkBbkPERmVWDJFtghqm5T6m2ftX9OVcAalXQn99ZzVt6qa76mCwVXNJslP1jJ7coRb9dO5UhiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841242913b.mp4?token=pAAG8hpfPliwbDoeWQ8QQVaLdwzb7hFBr-60_DE5H4wt0OioQ2g4jLe1ZuVBSgtSlJ-tcrbi8BGu0UT2_evczhuHytG_M38eML28xprVlz38Iqre_rnnPhXUuS2hJozmwLInuzepTLByNMnpxB6eb5m1YbyIu3nFwljIgcox-CxJcx1hffC87z1e2KvOd1iYrw87a1HRGN_8vC-LER1qNfZhMI_RSd4fWpwmJ63CmLs_wpNv-Dk9y3TPrMbT01EhQbsxfKWwpKtcSkBbkPERmVWDJFtghqm5T6m2ftX9OVcAalXQn99ZzVt6qa76mCwVXNJslP1jJ7coRb9dO5UhiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر آراسته: نسل جوان شاهد افول سلطۀ آمریکا خواهد بود
🔹
جانشین رئیس گروه مشاورین نظامی فرماندهی معظم کل قوا: فروپاشی رژیم اسرائیل را من هم با این سن‌وسال خواهم دید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465459" target="_blank">📅 12:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465458">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b8d09462.mp4?token=cxg3hyDNG4B1AMAmXFZEyHXw1iAjTYCHSWkwwXXh0F02vieUdlm1UCCxJwv9IiB2y4xnPsxI8mT8yblWVB6P5ohBj-gD5ANv6c-yXU49FSSrW52VkUCXOtIvoZIjHKI-9GLNFWgsyq-Al3CPWfMcaNiT2DUQ7db8mo9cHU4jM_TfNxAwg8MjSr3CgAGIcZOVfz3_yi0cQ3vm_K4x4sw8rt3C13JE8kSmWRCvPCFxqlK1LwRQsJl6tWewRKShK0pVyPCK8w1C1hegoPJlWSktyDFmJ_OfWIW-Zvg6SdMYhpfLlDdD5Ji9GzC64aJCJCRXlORETU8Br4GIiyMC5pcvxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b8d09462.mp4?token=cxg3hyDNG4B1AMAmXFZEyHXw1iAjTYCHSWkwwXXh0F02vieUdlm1UCCxJwv9IiB2y4xnPsxI8mT8yblWVB6P5ohBj-gD5ANv6c-yXU49FSSrW52VkUCXOtIvoZIjHKI-9GLNFWgsyq-Al3CPWfMcaNiT2DUQ7db8mo9cHU4jM_TfNxAwg8MjSr3CgAGIcZOVfz3_yi0cQ3vm_K4x4sw8rt3C13JE8kSmWRCvPCFxqlK1LwRQsJl6tWewRKShK0pVyPCK8w1C1hegoPJlWSktyDFmJ_OfWIW-Zvg6SdMYhpfLlDdD5Ji9GzC64aJCJCRXlORETU8Br4GIiyMC5pcvxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌دفتر رئیس‌جمهور: شایعۀ موافقت دولت با استیضاح میدری تکذیب می‌شود
🔹
در فضای مجلس شایع شده که دولت با استیضاح وزیر کار موافق است و خود دولت این را گفته.
🔹
شأن دولت قطعا این نیست. رئیس‌جمهور از همۀ وزرا با تمام وجود حمایت می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465458" target="_blank">📅 12:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465457">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bb34abe68.mp4?token=opT81etFWU6cS5l0_GZAZQ5d_RMXWsGCH4djpGUcAUBx-S-uDb1bsmmuUAxDrfLmCKLcjNvfou2vvnCJ1HCTsGjygaKMogqWWiwllau-3ZQEpA90yqBS-AbeHMxukUaHfQonNT8bjEAMXBno58t0jcwJUfB_rlGiygpVlc6fsRtg4A00lp1IuI_KSMY7hxuWx9518fntWAdYXdfoGymqBYoltkrSP3RCK53OWHyxJJX7VfF8YLd0z5ztrAPJ_iMcjSdd89a-gnD8tu5_e_A5IJ5CqsFTXD3bal_MNy9lMRNamoyH-3ZfFOlISCAQgm0-JJV9ggFsHbjAPzgTEkf25w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bb34abe68.mp4?token=opT81etFWU6cS5l0_GZAZQ5d_RMXWsGCH4djpGUcAUBx-S-uDb1bsmmuUAxDrfLmCKLcjNvfou2vvnCJ1HCTsGjygaKMogqWWiwllau-3ZQEpA90yqBS-AbeHMxukUaHfQonNT8bjEAMXBno58t0jcwJUfB_rlGiygpVlc6fsRtg4A00lp1IuI_KSMY7hxuWx9518fntWAdYXdfoGymqBYoltkrSP3RCK53OWHyxJJX7VfF8YLd0z5ztrAPJ_iMcjSdd89a-gnD8tu5_e_A5IJ5CqsFTXD3bal_MNy9lMRNamoyH-3ZfFOlISCAQgm0-JJV9ggFsHbjAPzgTEkf25w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌دفتر رئیس‌جمهور: شایعۀ موافقت دولت با استیضاح میدری تکذیب می‌شود
🔹
در فضای مجلس شایع شده که دولت با استیضاح وزیر کار موافق است و خود دولت این را گفته.
🔹
شأن دولت قطعا این نیست. رئیس‌جمهور از همۀ وزرا با تمام وجود حمایت می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465457" target="_blank">📅 11:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465456">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj6jaKX25oS4GbUJpYNNSt1RZeay7S2h12qh6X4n5PbXF1oY5Vck8srqnyuTgHYqhePYeJ3mfsN9IDChJbzQGYc0vusLXglBGbkHWZo1-MifY3LUGZ5CTAMRaxmhK1sW2CnY3EFJ72f1ODK0PM_KsoSyuyvM95SacqzRqRCcAgUHJfqt0V1KBPDvL8YiMfIFVbwgYOGUDn5wDoQJX8F0SFa9N-6YtglptgIyeNEkFUZJD0c8FYTof7xcwtohuuSpIQ0qARLyrQt1oD3HqwUyGf_kgVVcsj7WsJbkTmNaqTF2fK8wQpZ0kdoGAkNalaoDCpht5tarTQfvRxvFWYyl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقچی: طرح ۷ ماده‌ای از طریق واسطهٔ قطری به آمریکا منتقل شده است
🔹
امروز یکی از واسطه‌های قطری دیدار مجددی با ما داشت و دربارهٔ اینکه چگونه می‌توان برای تحقق شروط ایران راهگشایی کرد، ایده‌هایی داشتند.
🔹
آن‌ها این ایده‌ها را با طرف آمریکایی هم مطرح خواهند…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/465456" target="_blank">📅 11:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465452">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IId7nFNTG1ryFgIeRDn33MJcpPVXJ0zL9rc2RRoO4qi41zs0NGP05rSlN-Eqxg3Skh2fjw538d4K2BL4gVfDJymqRQGwEcYVE8RPiz7xzsaUwQ6un3d8YRv9ZB4TJDn2HpeW-SsNMYQSmtX8espz2j7fSSXlkDEtw0rc5ZvIqPuMDNksENWnR15U4ETSyyE_ZBDYNNXVYCOlCm2pvDfxwZDBUv_G3it5X1gRPV6DX9TDQi_NJE2S5mCXfz5ihG-NrCnmTPleksq0v4Q4AroShdMqhS5E7tIVJeoNLOybGOh4xmdGyJo3q85DXGvjL7nnZuMBe3vtU-mZh3t0LH2WVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QapKlXAfXj__d-toRR9u0PXzzaYNzaiTEGPvjIEZg2hVKGGCd7W7R7Zrkuapjl6doLxiThNzGwVafSdce9cS6VaamHDRqT44J0Ys2SOextiC6PjlrtXcnpVboVv9jJTxZ0ZtdnuyRR9b4SIXT6Xj0MSJTTI5ea8_SriAUb2VCQhPQTJ4Hx71g2nkGCVbSjaJjcZvspKP_MCHeBrVPtoScfPLDKfi8LloW_V94flN70onK42vNbvWt_Kv8KGYaIqqOOZ8woDs471khsJrJQBIEQoe13rJ0rBmXiBU6YUPfJkzT4fzdbAZ9MDbkgoVsW1k5AFU7qd5V2ti96GNmZu9VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0jW6nqrN1g_2EUSKRg9SKA3XudPOXBxutphg60_sXn5lsf4mNrdDpudCLBT6ds_VXSq0Tm0yw2AzMz9NfZ56OG-vWClfX0z6fYj_GNmso0xXY5LKIx4R8b61_E9GoDzB3JtLFMswKI1jb1cOrDhpel0LHe2l3eJuI4SdhNmWkRZBKSz537ksRuYaaLeHBm8hRCqBHfeZQFudYcgs3zcrpX9t5GjKMcIK6dzS-TMuAJg-Ty6YCUcpH7_J91ZeXRP6laKJc8fhT1RNXxjYUbdEOIqjIw6ltE10EIbYCxgUnOmbKZboPZey3Pj4tqpAtnE6ScwTLdSnMIwN379zYJsRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZUOdUm7cxmYGykq1k70UDM20a3pDkPplTvUliAzOHVK5tV8hzKfhUsOJsuyykVjNG2BaZmm-Lgl7-yR5uTYGY-SeY6oROVzlipomz7V01S7EXnblR3loSanJU_NHEUeaJiwN5RlIPHi_OJG9AgbAijlZ5RLN9lQCz6cbNPR3DRpqD22jQzk-aC1wEGzh1HjtapXo3RFN_kQJSOJlDGg4-XtNmSeJQFIP-q6I54HrhFDpoOGLc3vI7CeOKbznmKlpBNAR12VVhr3VHobC3lmRH5g9Ox0ta0OS0MbWuWPclu9uZ6ROc2KCdNWSSxAQBO-hAwVwrCS-xTc24tnmcSsGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: اساس و پایۀ اصلاح‌طلبی، انعطاف‌پذیری در خود است، نه طرف مقابل
🔹
رئیس‌جمهور در دیدار با فعالان و کنشگران سیاسی اجتماعی احزاب اصلاح‌طلب: پیرامون مسائل جاری کشور و به‌طور خاص موضوع مذاکرات و روند آن، طبیعتاً باید با جامعه گفت‌وگو و از ضرورت مذاکرات دفاع کرد.
🔹
بیان مزایا و دستاوردهای مذاکرات، نشانه آن نیست که ما در مقابل دشمنان سر خم می‌کنیم، بلکه نمودی از شفاف‌سازی است. نکتۀ قابل توجه در روند گفت‌وگوهای اجتماعی، پرهیز از دعوا، ایجاد اختلاف و شکاف اجتماعی است.
🔹
اساس و پایۀ اصلاح‌طلبی، انعطاف‌پذیری در خود است، نه طرف مقابل؛ لذا تا جای ممکن ضرورت دارد میان تمام ظرفیت‌های سیاسی موجود در کشور، همدلی را افزایش داد و هماهنگی و انسجام ایجاد و آن را تقویت کرد، زیرا چنددستگی باعث ضعف جامعه می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465452" target="_blank">📅 11:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465445">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTOYd6RtOlCxb4NwIOoYcmrRLWccAOQQrux5sF-iTZsxI3fLMYRj3qyOi8fCPEhn4p3PZCIuNlNr4nMn4z_vCv0wmAnbuOoYOgymL5m9XZZVf8TfxJPAUuwV98mbUJiADDDFlU1JQ6S4BLwRuDbh4py7a_ARZyVAsbLMzRAtqNq-wPzKb2wqd-LD6M-20v9u_GWNdKfcqAP0PCYGZhxLVuIxu20-wRBTmbpyOIAVEjLq6Bo9OjCTGuivfG8-kUhDZ3YgonC8ML_jbGGYogqIO--7Cb1KQ3wETTux4yl18DyPgZCeJ7n8gujURLusFqv1UYXDysu3_OtdoGOkkFWu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1oYxsSLDj_pkz1WcMJscUnNZhN2Shry0clZNAw_eB1vxMy3tnSnAirKHFUDUtAokS_lI4T1fF738QnWCZCvtvhz4lRqXBskJtBG5I6mf7LDfm1FtgZaFK3H405j_Ljqpx8YoDU6IcVPiB49GVUbi3WO225LQdT05oWIAv8LcFcmVgpXJETdXWvonBViJaHxV_UvL97r0pcEuq2_cUQtm7gO8RmN_iGiuPyYBhJJ90s8PSHIflBJpY2Fy2EaLkbephxTaa0DWvwXLzwJ67RRf_Ggi73lo_-8F1iU2_cCqVRwpJkz0oexZBbpt8eE-49Ax9gBw_5wNLDij-vKWrTCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpLfgThHfLNhuasaSegN4Uzinl_UOrc8gj8n6YWGiASjoYDWxYs4e8LRs3L5NpNbiRg8bdDkD52UbKFVLoC9ahsGXf7iL-sEvGAd5NKATeW4C5teGLIdAWfnjPmEU9uCZxcdr7MUHMUPDPgWZnX-V2oWbhwq0B_JXQDBmlxf5fXtYy4GA6mEPp3-o4efC_fORXV8fRHFjxvEgudM_iERSCkUxb1ISFomRRo_cKfIBl2xaVmLJNePlm7umRnFoBade5VxKUuKYhJkzAleTPbR0C5kLpqWakw3YOuAc8gowidOi1yx7Wt5YY5-QZDApDtqpA9DVd_FO-vMCMQeAANUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxV2VwrCm2PhuSdyDfAwSVe7kBn_cHPFzTyRk_jzVmwgeNb4HzJADMClP3RVsGMOtyMDI0tp4u8FgytnQnEtA-kADVGkzMgjcnpHOOkCnrYdqZscrVmCBdJ91bslc7Omk_zuEh6TCEElCQrfMG2w0bATniuvGgQO4dI_KXY4j2mdk5Ta4bH8gP7oVhQv0u-M-xjDxgXRbcW3CKT16_Y4UnqyWJv3sbwV4h9DkKJQcjiiwvkugV0kPjqTsKynzdhKvvocWED2BqKsJ1NxaNcuRx1cSimIh0UrBswvv0soBOLNHuKo47XVb_6rOFl46BWyUcxcLXZrSNeQdpVV4IEf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TeX11JKX9c90a6DN_Vk7tnvYe4YQ2BQokIFy1Im8LbL-a6mZmjsI9ALe_v_feO_y2EVmqXDsDmsOAULyqMtwAuvKYENrol5nGgoP-YQlnhAjDHDvYZV3klSsk-NE-h8ZdR32ITvZ122gQGgEHjmYaUN2wXAGWc2PQty9oeWfUF3cIl-fj4LS8p6OBGcis97Pe2hrosq4q2hXGQEP67J1PEGlUo0K7wFFQJ4z4PESiRnSP9Ty6FwEOVf3p1tA4ILlEcQ7MuChNJ8j9HRvmL-R1hFIaThPmBtL6sn5_poSafI9cUtkdhGiwg2i4htTBHw1cXQMaEUYhI1tm4ulOFQwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YPFe7F4gbOJ6jxMIqGS86CCFz1PnO_od6YGm13mh-CphvCKaoBEEIRrfUJF4rpsHuaL46dCDsz_kInFV8CdnAh8CXTci9R4h4Hvb6OaLV_9MMIg6fZt5RtYeiM4FMVkH8_M70_AAhQh0wJcuIQiY7wrnMbRbnxeUktrowgoWW__2cottfhH6zOZ9Ev0oUJnEWdA_XYRKtbjmDzi3wuuUhUxKe99eH2j6gR0NW6Q-DYvYC5ihcI5b8OLwMt3Vy2tB9yLNWuOJyJvYIUXA4Df6LOMmxSqxGXPjhvzr_KRl79635QXg2C78ZPOCrdw1vJJpGeDko7MzkMHnFCdO1b3P4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo0rxAqCm2NYuDDt-TohRSVbzw-2ssTE3kC4hhr_dEdUdveBImJX3eLHx0KE6LuaWhZFhOgHBqMsZP2lRvwxXws8xhpe7Qpl-nrQh42MBpV8FoK08IvioiHZdzL5EcOGsjOz1f58VLTMroPs3zUXdaP6laV56ynbsR_vGHNM5Vs6Hgq7ZzvJH0JoHY0OB3COl2Z56Dg5uSP4X1jkXcZSaVFs8X2uN8b5rnC4jFXoFIdyCwjTWm0Pcn7lTPzqK6gN1ZBvhrlycqZszPF385u-_wqaSjv1Q4DBs-fZrCesLOX-Z7MikDvaGKT7llzr34Tw-kJOebNM4-1iZ5988U-Dsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن برداشت انگور در دامنۀ زاگرس
🔹
براساس اعلام جهاد کشاورزی، امسال پیش‌بینی می‌شود ۵۴ هزار تن انگور از تاکستان‌های چهارمحال‌وبختیاری برداشت شود که شهرستان کیار با حدود ۲۷ هزار تن تولید سالانه، سهم قابل‌توجهی از این محصول را به خود اختصاص داده.
عکس:
عاطفه گنجی
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465445" target="_blank">📅 11:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465444">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3624d64f.mp4?token=HBaQyFqiFan8Ub_Wy_v6bOeyAIaEapF0VZymxNlfcNjsqVOe96uHPjAELdrHaBJZJQmXGk045uJ7qsP5Jovz_BtC0DNcjI5n6Z8isFagokqoDorfmoo1vsKca0rQkZRFxdOLs2M6-2kBLq3jfx0p-pvp-6JqjlviFYw1VSPxiiWP3OIzInh3OjNY9lgdqeewGpQTjbdc4izIkjY9UW1HCDcJgm079ipQnN_EN0GE1vViD0I_GCJpZVIR2xiivOjQeR9Xy8IGrmPvajeesF3ywmO4PvMHCzdaReQ3_JU8_p7ZmA8esdLTah8BSF0KhfA0qJ-noY8lH2VOAzLntt2XTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3624d64f.mp4?token=HBaQyFqiFan8Ub_Wy_v6bOeyAIaEapF0VZymxNlfcNjsqVOe96uHPjAELdrHaBJZJQmXGk045uJ7qsP5Jovz_BtC0DNcjI5n6Z8isFagokqoDorfmoo1vsKca0rQkZRFxdOLs2M6-2kBLq3jfx0p-pvp-6JqjlviFYw1VSPxiiWP3OIzInh3OjNY9lgdqeewGpQTjbdc4izIkjY9UW1HCDcJgm079ipQnN_EN0GE1vViD0I_GCJpZVIR2xiivOjQeR9Xy8IGrmPvajeesF3ywmO4PvMHCzdaReQ3_JU8_p7ZmA8esdLTah8BSF0KhfA0qJ-noY8lH2VOAzLntt2XTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقامحمدی: «گروه‌های مسلح آموزش‌دیده در امارات و اسرائیل» وارد کشور شده‌اند، مردم در محلات مراقب باشند و تحرکات مشکوک را به شماره‌های ۱۱۳ و ۱۱۴ گزارش دهند
🔹
عضو مجمع تشخیص مصلحت نظام: جریاناتی در محلات استقرار پیدا کرده‌اند تا عملیات‌های ترور انجام دهند.
🔹
آمدن نتانیاهو به امارات را جدی بگیریم. طرح نتانیاهو این است که به‌جای اسرائیل از امارات بجنگد.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465444" target="_blank">📅 10:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW7dxSzC_r-ZFu-iSIx3kSs5XyLyTRler_XOnZQvAORKCB_9hUGZjjHTO2UHHxE1_vNfHeVx7I__ue62ItGSDuF5ZIChtLDDE9iGh1zEMdipOIhuIKfRl-XtYm8lKhvuU5YMDku-bq5-ArUlrgr8bMvWayKxoxI2PVdUAUzvc9rmwWMPXCOVtQ2u9zc9AZ1h_dgCqVukoKzNrz3h--WX7g64kxBOSqgvt5fv2EPDahlp6oKPWvqWWMY515aagQkK1o4WdZL8E9xue-nVe04YLHtt_PpSicqkYTKoFmh-FCmjrbivNXpT4cpjzwr-KNnZ86azNIao1at4DWd0ot7p1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر اقتصاد: دلیل جهش آمار واردات خودروهای لوکس، تخلیۀ اضطراری انبارها در شرایط جنگی است
🔹
به‌دلیل شرایط جنگی کالاهایی که ترخیص آن‌ها ماه‌ها زمان می‌برد، ناگهان ترخیص شدند و آمار افزایش یافت. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465443" target="_blank">📅 10:38 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
