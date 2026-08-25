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
<img src="https://cdn4.telesco.pe/file/CNoGlY32KlQEyH1R07cQGT2ieZH3v4eL2WPNNiE6emna2bPfHvWmFDCqdj7TS7vQmdQdkrqpD516ONQOAePBl4yr3HbYVQRapflXXpMJzM85O1ZfujGbQk2wYrW4Ll-oNpcVJukhSOYYaDT7wa_MhJcwbNRcAJQmiMaVqU0MEvQTGG260z01EnKAiW9FwiZUHiEyPMI7SWHsdErtKZlVOrS7D3grZimzG6I4aXmhOjXVizTmLeesVddA_T1NBRyl5PTNp7NVAb4AGXaockfQipl8qj9mvVBu7e5iKp3DG_WLoQWNzDMl0R9c3dndIShrEpzPthlVK5myFpZji6YV4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 21:22:35</div>
<hr>

<div class="tg-post" id="msg-684295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای اکسیوس: زیردریایی‌های بدون سرنشین ایالات متحده تنگه هرمز را اسکن کرده و بیش از ۱۰۰ شیء مشکوک به مین را شناسایی کردند
🔹
ارتش آمریکا با شرکت‌های خصوصی برای پاکسازی یا انفجار مین‌ها قرارداد امضا کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/684295" target="_blank">📅 21:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bee9553dd0.mp4?token=TkzAC3jruVQaiZlrKUM7IV59xAXBJlyBY-5miVRYhePulno3J3a-9Zs-SdeIZgSzxgOPV2VKneeFtH3XWeJJTbEHGkNnBVKymVJW6vYJBRpBdmyTLwCDCF195XQUgNwPfLhmVNYCM1DDkRCk3ETmCh4S35j6mixEKktuNhLTFv2yLnvm4EY25dUo6Vlmpd0U47ynbdAgBR7EZP-mEHSc2V75iKkwsn9UqWyBhg-mBThJWvd3kN4C1fzqrBCfJrzPDwiwAhktKi1QGhiLJrSIN9vgnASmOT2Sx7gh5jHKGHRgrz9kQqX7WxeqilMMCx2pQS9NB726KKZtiYTFOeeD_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bee9553dd0.mp4?token=TkzAC3jruVQaiZlrKUM7IV59xAXBJlyBY-5miVRYhePulno3J3a-9Zs-SdeIZgSzxgOPV2VKneeFtH3XWeJJTbEHGkNnBVKymVJW6vYJBRpBdmyTLwCDCF195XQUgNwPfLhmVNYCM1DDkRCk3ETmCh4S35j6mixEKktuNhLTFv2yLnvm4EY25dUo6Vlmpd0U47ynbdAgBR7EZP-mEHSc2V75iKkwsn9UqWyBhg-mBThJWvd3kN4C1fzqrBCfJrzPDwiwAhktKi1QGhiLJrSIN9vgnASmOT2Sx7gh5jHKGHRgrz9kQqX7WxeqilMMCx2pQS9NB726KKZtiYTFOeeD_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرقت از کامیون در حال حرکت در مصر
🔹
ویدئویی در شبکه‌های اجتماعی منتشر شده که نشان می‌دهد افرادی با نزدیک شدن به یک کامیون در حال حرکت با یک وانت، اقدام به سرقت کالاهای موجود در قسمت بار آن می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/684294" target="_blank">📅 21:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎞
کلیپ ویژه| حفظ وحدت و انسجام، پشتوانه قدرت موشکی
🔰
نگاهی به مهمترین سخنان حجت‌الاسلام والمسلمین طائب در چهارمین آیین تکریم فعالان مساجد سراسر کشور
🔻
رئیس سازمان بسیج مستضعفین:
🔹
با پیوند زدن توانمندی‌های مسجد و محله، مسائل محله را احصاء و آنها را حل کنیم
🔹
چنانچه محله مسجدمحور شکل بگیرد، وحدت و انسجام ملی دوچندان شکل می‌‌شود
@basijnewsir</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/684293" target="_blank">📅 21:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963ce9c3d.mp4?token=maPsNf9rwsAfmUtU1QTkgRufJvqrZhUVxWrd1qlGWstpIpIxNOCVKKF7ymlnUFGUs67ME7em3_zkhN5gFkMDkfN_OgwblRsOGcGe0XCEe6IJxZd1F2S73Bqrcn3A1Jc8HoYgMathy5y38Hb-xdF0cqR01qPHfd4QCOyZWF00gTJzwD6pjDDk-WaJG1oBFns7pmylkHB44nCwM66LZOjv1-RC5vxk2yycnbtU83n5aG40Hll8PsPVJWz83qm50jO96aRgPdgf-ye75u_vkMVOhMydiJmdLYgEGdHf0O-kZvAHJJvH7Fvk7SUfJt1XtBldEZo2LnkrPDy04RmCf_NFehTpepdjVIJak7EhPwxbix95DQfVmsPWjjqBqmFC-IVs9lET8PWuRZrrYcxep6PpL4ZuKf8zlZvWxgE1S1Ud3muKhXIf7bP2XgRHg_A7hsAVj_3jaSwKfdD2k92scHD0NBziuk_onR1jxJqkTDQV7DAvv0ASD7y1xxh_fx3o-Fc4ALPEoPdBBUH7k1-8cv9S5_uAK_G6ipsjym1qbeUIPNGcjQL1RjxvXNK17ZS1i4yYuZyfmwiP1hC7LZBGkVUPP_WPJ0oFws1wBjNOVhoCDxKXrZVefl68uaqR3OSR58EgcVJ4zDDosC4mxvbtI8oqkwb-IWUXJARvvv-eNMdOy_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963ce9c3d.mp4?token=maPsNf9rwsAfmUtU1QTkgRufJvqrZhUVxWrd1qlGWstpIpIxNOCVKKF7ymlnUFGUs67ME7em3_zkhN5gFkMDkfN_OgwblRsOGcGe0XCEe6IJxZd1F2S73Bqrcn3A1Jc8HoYgMathy5y38Hb-xdF0cqR01qPHfd4QCOyZWF00gTJzwD6pjDDk-WaJG1oBFns7pmylkHB44nCwM66LZOjv1-RC5vxk2yycnbtU83n5aG40Hll8PsPVJWz83qm50jO96aRgPdgf-ye75u_vkMVOhMydiJmdLYgEGdHf0O-kZvAHJJvH7Fvk7SUfJt1XtBldEZo2LnkrPDy04RmCf_NFehTpepdjVIJak7EhPwxbix95DQfVmsPWjjqBqmFC-IVs9lET8PWuRZrrYcxep6PpL4ZuKf8zlZvWxgE1S1Ud3muKhXIf7bP2XgRHg_A7hsAVj_3jaSwKfdD2k92scHD0NBziuk_onR1jxJqkTDQV7DAvv0ASD7y1xxh_fx3o-Fc4ALPEoPdBBUH7k1-8cv9S5_uAK_G6ipsjym1qbeUIPNGcjQL1RjxvXNK17ZS1i4yYuZyfmwiP1hC7LZBGkVUPP_WPJ0oFws1wBjNOVhoCDxKXrZVefl68uaqR3OSR58EgcVJ4zDDosC4mxvbtI8oqkwb-IWUXJARvvv-eNMdOy_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفوذ سایبری جبهه پشتیبانی سایبری به قلب صنایع نظامی اسرائیل؛ Novamill از کار افتاد
🔹
جبهه پشتیبانی سایبری با انتشار بیانیه‌ای از نفوذ موفقیت‌آمیز به شبکه داخلی شرکت «Novamill Systems Ltd» خبر داد و اعلام کرد که با خارج کردن تمام تجهیزات کلیدی این کارخانه از مدار، عملاً آن را از کار انداخته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/684292" target="_blank">📅 21:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59db84866e.mp4?token=uRZI7GASI--yHUc_remM5DUnVEkGeGq8kIQaqLPUj1QO3HfvXB_krPVljhhmjKdG_5yAnU_yNwot_MxC1Grl0eQYfvguzKFrH7Cg-gSMHFw5Ceno2j3YIWFI0GoOgUc1ctpsu43mnjeVaN4lnqINbG5B5jK4viPqIKLtUzxDWzSdQxt-gUrCfJYC1YE4Y3-DPzdcI6i8zvB6nz4MDgDYAOlFxfJTclz7xd7H0XWimY053JTx-e84QcRl3vgcKIn7Dn3ImINvg1HrH4jSYY1aHrYpnWaBPM_1VJH_r7Md04vvWtWH-u8yOsSmytvzIDM8_ZHfGGQdjU6terubtGY31Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59db84866e.mp4?token=uRZI7GASI--yHUc_remM5DUnVEkGeGq8kIQaqLPUj1QO3HfvXB_krPVljhhmjKdG_5yAnU_yNwot_MxC1Grl0eQYfvguzKFrH7Cg-gSMHFw5Ceno2j3YIWFI0GoOgUc1ctpsu43mnjeVaN4lnqINbG5B5jK4viPqIKLtUzxDWzSdQxt-gUrCfJYC1YE4Y3-DPzdcI6i8zvB6nz4MDgDYAOlFxfJTclz7xd7H0XWimY053JTx-e84QcRl3vgcKIn7Dn3ImINvg1HrH4jSYY1aHrYpnWaBPM_1VJH_r7Md04vvWtWH-u8yOsSmytvzIDM8_ZHfGGQdjU6terubtGY31Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: برق صنعت نباید قطع شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/684291" target="_blank">📅 21:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHiJbLO3IvKtEumbjIGAxz6Xvwu877t1YBA7kzmxonM2MIEWOa7xa8yUmMmtr3lJCsrJ8f_DjpH1ciH2pUoumixlbynUI8sGOBk3f3ZhpHlect5B7VceYFAaRZeKOEAASrpRPrUEr76O2KmCBX4vQe5cMJn9F62aUPQeKost-7aPfMH3gAYMLoPxvkRW4gIU9TZKC2MYKr7ZY74Mz4HrtBUl6jpWnUuVj1n_Duxy_hjhjVkpsdQWp8TUYiLuK-RvmApUUu-Cw7hkLogSyBclEEajlJIcz561ALPfHy9WT6i33qy6Ogb-wcQzWrUtOnV3MMTex-eGorVuMHYYkiPINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خروج یک هواپیما از باند فرودگاه مشهد
روابط عمومی فرودگاه مشهد:
🔹
پرواز تهران به مشهد هواپیمایی سپهران هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/684290" target="_blank">📅 21:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684289">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای قرقاش: حمله ایران به کشورهای عربی حاشیهٔ خلیج فارس به هدف خود نخورد
نشنال امارات:
🔹
انور قرقاش، مشاور دیپلماتیک رئیس‌جمهور امارات مدعی شد که حملات به کشورهای عربی حاشیهٔ خلیج فارس «تنها بر معضل» ایران افزود. او گفت که بار دیگر تأکید می‌کنیم که تجاوز ایران به کشورهای عربی حاشیهٔ خلیج فارس به هدف خود نخورد.
🔹
قرقاش مدعی شده که این تجاوز، معضل تهران را عمیق‌تر کرد، یک محاسبهٔ استراتژیک اشتباه بزرگ بود، و موقعیت آن را بیش از پیش منزوی و تضعیف نمود!/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/684289" target="_blank">📅 21:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1cf219f41.mp4?token=pD2L8eWeanY2O3rq3vJ_qCYM23CkR44P9-Mqp7KUKa_L4exlqL_qYSakSpG6GHyM1VKzki6vo9BbCEfEXwcirjrM4EdUUqi9zXWX6tXXynVJOAETgAzH1mcxSScghLvPbUh5-RqZbr-jwej3n3QNE0BmP1dLS_Wm8uu92Kdh5tFN3J9AJJBJGeg12XG1hcGS_Yx-G-PYVilyQPOSTWZxGLweViOjJy59cwbMykONHkg0IoDzfGJ6mM-2_aX7DtQ_pryF6YHsQmTj3gq6OUPoGWe_Lz3mbE9xTD5rxBTVDW_dAQsXESK-4aYPMXV8La7SBBKf87e4A7qPl6eZWkKJMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1cf219f41.mp4?token=pD2L8eWeanY2O3rq3vJ_qCYM23CkR44P9-Mqp7KUKa_L4exlqL_qYSakSpG6GHyM1VKzki6vo9BbCEfEXwcirjrM4EdUUqi9zXWX6tXXynVJOAETgAzH1mcxSScghLvPbUh5-RqZbr-jwej3n3QNE0BmP1dLS_Wm8uu92Kdh5tFN3J9AJJBJGeg12XG1hcGS_Yx-G-PYVilyQPOSTWZxGLweViOjJy59cwbMykONHkg0IoDzfGJ6mM-2_aX7DtQ_pryF6YHsQmTj3gq6OUPoGWe_Lz3mbE9xTD5rxBTVDW_dAQsXESK-4aYPMXV8La7SBBKf87e4A7qPl6eZWkKJMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ایده‌ای دارید، اما توضیح دادنش به هوش‌مصنوعی با متن سخته با ابزارِ Squig می‌تونید خیلی سریع یک طرح اولیه از ایده‌تون بکشید و همون رو به هوش مصنوعی بدید تا بهتر متوجه منظور شما بشه
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/684288" target="_blank">📅 21:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684287">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcba318382.mp4?token=pGcF-0q_VauP5VZlDINCoBPhWQvM3URsV8pGoZIXZmAU_DZptfdm-ydjLEaIR4lwMeiTaQnEXoYK7IgV5sgLwD_Q7ECs5Y-5qr3yY37oE--Mk-K3Lkbh3t4e8lpvU-gMuF28x8TJ4lVKgTJ6da5Cz4---4n6REDv0CsllSGhiQtEx32Ey3c7ga4g5IhHMgQJS4Qn3hUXMpqTFNA3beW4Pj9YnSsWAcrXlDXVsUg-GG-SHC8hwq7jiOdVDhTLxoputXvL09IlgP1t78tBU-NsjLaB8O58DHG8IVwGn02kV8h-xUEUvkFTZJYv3gZfF47xWDaFeReEHzX4TU7CpHZNrmhW4czF4XxQqvoEsRs6OM2jRf_NOmraS2EAOf3FAUj9rLrKldzWkhsvqtqJ0wxV4mkYnqUTB07KbD6BOiokesrrtr1GnUFgUa1F26l6BG_ZWYFNg0jxHWVHFHNTBzgnjYmrZN4EibzEqruz8L0OnGkmNBTfNonE5KENj2dQnyOvDmsbBE7u2YQJfSEoYLC39aR0rfe9hJauUngLGsjkDxI-pJMI8zFQ8QjjWxaZUFAppgx3dtnaJC0m6kHFl6wVBe-uiNmPW2SZuWoZn-43cQi0yE3ORkmmldP6hwFLelJyeftb_2i76C38ZB1WmsZ4JbsBVM_P9fwg_6lna8bzOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcba318382.mp4?token=pGcF-0q_VauP5VZlDINCoBPhWQvM3URsV8pGoZIXZmAU_DZptfdm-ydjLEaIR4lwMeiTaQnEXoYK7IgV5sgLwD_Q7ECs5Y-5qr3yY37oE--Mk-K3Lkbh3t4e8lpvU-gMuF28x8TJ4lVKgTJ6da5Cz4---4n6REDv0CsllSGhiQtEx32Ey3c7ga4g5IhHMgQJS4Qn3hUXMpqTFNA3beW4Pj9YnSsWAcrXlDXVsUg-GG-SHC8hwq7jiOdVDhTLxoputXvL09IlgP1t78tBU-NsjLaB8O58DHG8IVwGn02kV8h-xUEUvkFTZJYv3gZfF47xWDaFeReEHzX4TU7CpHZNrmhW4czF4XxQqvoEsRs6OM2jRf_NOmraS2EAOf3FAUj9rLrKldzWkhsvqtqJ0wxV4mkYnqUTB07KbD6BOiokesrrtr1GnUFgUa1F26l6BG_ZWYFNg0jxHWVHFHNTBzgnjYmrZN4EibzEqruz8L0OnGkmNBTfNonE5KENj2dQnyOvDmsbBE7u2YQJfSEoYLC39aR0rfe9hJauUngLGsjkDxI-pJMI8zFQ8QjjWxaZUFAppgx3dtnaJC0m6kHFl6wVBe-uiNmPW2SZuWoZn-43cQi0yE3ORkmmldP6hwFLelJyeftb_2i76C38ZB1WmsZ4JbsBVM_P9fwg_6lna8bzOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماموریت جدید بابک زنجانی و دات‌وان در جنوب؛ تحول آبادان و خرمشهر یا...؟
🔹
این‌بار صحبت از هوشمندسازی حمل‌ونقل و ماندگار کردن گردشگران در منطقه آزاد اروند است. در این ویدئو خواهید دید دات‌وان دقیقاً چه نقشی در آینده اقتصادی خوزستان خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/684287" target="_blank">📅 21:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684286">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5raGA17JMh_b3gXB25J0ADnV3UFRjtoobYRxdTZUkHQmadV0d2hqDUmB5iVHcLhXdj73ZKlFZrnwpFFMbHqG57sq1uJjDWu7OCkYDZzd0ralkGdaq7WywfPfBhTHuXpC8WmjcMyQoi1-bQBBcesaGe_EaOU3qIq_aP1r0qCIkOcSxIf_bu1KX8dM9bkc4C5R5vjpQ3UxB9M8XoMKhq-LVkHAJKhT8ioVfnCMAYxxKjOxRUJfhVhuyVeug9YpH7VVHz-ng_VzNeKAdklMazLdnfsn4kwuobO1Rb9uuMJQb-2o_ggwrf8ojKCdsAo7jGMYxlwGh9zASWE1-i-Jda-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/684286" target="_blank">📅 21:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684285">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b5f882c9.mp4?token=TqKqMNZ0ocJPuFckIcWPv1sVe_AVa9X-PyacuGmJRjCriLiE9eW5XoBKXDmJsS2WhEeNVrhBX9gLL20GT1ldr-zgv2JDhOCXYj0GdAwLzJSsT5j-mBJS9jhnwk4FYmI9cgDQIVbm0ZWrxE37o9wHLcjddMBfinGk7mnoGH0XFtHu03tpuhDpmNSGNnXR6LXk8MNaUmZq61gNDrN3duq_vzBhXxic5jsvAaz02NeCAgAluxjXAW9b8QRcJ8AotRrKx_qXw2wORDd7wrZ07i2x-oLAAtkGx_iXXUyv7BiIwZeCmiVsAaSzurJBXKJP2UGBSL3q9PCllcbgV27dHk009g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b5f882c9.mp4?token=TqKqMNZ0ocJPuFckIcWPv1sVe_AVa9X-PyacuGmJRjCriLiE9eW5XoBKXDmJsS2WhEeNVrhBX9gLL20GT1ldr-zgv2JDhOCXYj0GdAwLzJSsT5j-mBJS9jhnwk4FYmI9cgDQIVbm0ZWrxE37o9wHLcjddMBfinGk7mnoGH0XFtHu03tpuhDpmNSGNnXR6LXk8MNaUmZq61gNDrN3duq_vzBhXxic5jsvAaz02NeCAgAluxjXAW9b8QRcJ8AotRrKx_qXw2wORDd7wrZ07i2x-oLAAtkGx_iXXUyv7BiIwZeCmiVsAaSzurJBXKJP2UGBSL3q9PCllcbgV27dHk009g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طعنه اردوغان به رژیم صهیونیستی
رئیس جمهور ترکیه:
🔹
جمهوری ترکیه کشوری نوپا نیست که تحت حمایت دیگران تأسیس شده باشد، کشوری نازپرورده از سوی کانون‌های قدرت جهانی هم نیست و حافظه تاریخی خود را هم از دست نداده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/684285" target="_blank">📅 20:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684284">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwwtcTwTmU9_E1AB-v12qjgmD47x7gVPt9ZfTsp-ghGVJNy6GI4NHyubCdyqQ8y3LFHtxbkGA3zVmGyEZoHcnmjNxpcEDWL7JWxClCWLTnYsVVwh5H3GVe_tGM9qSFeFXLtsXo3hc-9u__6ouFFpqH6Lyi4vFYzt7pe07Lik9--V_WVAlYfPOmJ_4tKC8MJokvzJtsTSvbiiPb22SnHIaCvO0d0Icb62gLbhwrAgMM6PXEYgZ1VxhMZlIkoXFBHnXF3XR-zu6bYnxcPzwKlkQnr6uUbzUmYijV_NXLUDK74f0_iUE94egcUcq-rcV0aKBWQ2J9n3nFzJBK6OmZO1_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برق منازل ده‌ها هزار شهروند آمریکایی پس از دو هفته همچنان قطع است
🔹
به گزارش روزنامه «گاردین»، شهردار شهر گری در ایالت ایندیانای آمریکا اعلام کرد بی‌برقی هزاران خانواده، نزدیک به دو هفته پس از طوفان شدید، «غیرقابل‌قبول» است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/684284" target="_blank">📅 20:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684283">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdtPZo_wDQQMXa1M7KVLL3ql6AiwBk7J1xhRSuqjsNUJyHR2JnhzSdu3PX-_J1DvO1hqqvUgk2LX-HeHJhaJkLBww4wYxFZOXHPPh39fEPagtZW13-VXEJ3kg0ICCOlHo-nxhMxnxV4uxzOypCUBtXYijovquc-mvMAcQYqfo8iT5kD6AcAgZrXy6HvCmGyWF6kaht5vo8BO23NBk6ZxtvkuBo-K0HUQeL29se4BRsVPrg2cfoQmggJ6-6GIZ7CM09X0hwDbBpRhTGDUL8pBvS7WYzfuDrEbtZbWxkr3BgZE7JAZMWQ1hTyXDiLhPxD2pIOLtK1HLFrI7gMYnZoBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای بلغارستان: ایران یک عملیات بسیار موفق جنگ ترکیبی علیه ما انجام داد
ادعای خبرگزاری BTA بلغارستان:
🔹
وزیر دفاع بلغارستان، از سیاستمداران این کشور خواست هنگام اظهارنظر درباره اظهارات و مواضع مطرح‌شده از سوی ایران، مسئولیت‌پذیری بسیار بیشتری از خود نشان دهند.
🔹
ایران یک عملیات بسیار موفق جنگ ترکیبی انجام داد که متأسفانه با کمک سیاستمداران بلغارستانی همراه بود. متأسفانه، این عملیات جنگ ترکیبی ادامه خواهد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/684283" target="_blank">📅 20:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684282">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TimiOmV3cyMFFAVq252778K9NKLPa01zIbzjPvKxtPRHD234kY154hz2VQ5MhxV9BGoCd-3b5xuPoalA2fBLn9NWepX0Jd9u2abOwNFjtDxXrszCv25Fv_ARidqZ7yUCCPH4hWgNYbxdlb_dn379aNtijujRQhp7mT1JNGlOrfqbBNzKS6HrkzFkVkCUkbHdRla69Fw-iHABKwaky8Dx3LzwweV6ZaYLbCg-xX4VDOY11c8VqMrKlXftoCNjP2hL_cXBocyDjpIS1wELPbUcsgqGzAGpget84YRh4kGMsnMS0j-xh-9YxzvWEH0l93_Olq9QOdzcFCC4QAMpMFvShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجموعه آمریکایی پژوهشی بازار سهام: کانادا باید شروع به فروش ۵۰۰ میلیارد دلار اوراق خزانه‌داری آمریکا کند و به سمت طلا حرکت کند
🔹
نکته: ذخایر طلا کانادا = صفر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/684282" target="_blank">📅 20:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnwKE-x09TeujDpjsMPiaQR_x_csb0JY9yFVHFeBrOhoUniOCV_V5M4HBMzE1XKVeQtIlT-Kofs8oDXxcYov2z3v8UxAm4G9TZ8VmAz-lrlxnh1fpnMsb_Z5zuxXe9jlmb5wjbX9ex3yRQoTyc0Glq_7qtHXuc9OzjI-M28O5BVZq7d4VxMFUi8f_ClQ7qcBCsosafSqc9ej5IgBSYZcPZgOA6CiqZBPHPs67JNsXV7i-NIeQcM5cKdl9ca51Ca9k2x--HbkW7rVc_RwDdE_FmZZT9GE-HBBgemAz_ZUq0LBGEXuZGYVbOvpO2rxWTEYDWMpftOcE8dM0f7dkxX2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: مطلع هستم که رهبری، در مورد سیاست جذب حداکثری به همه‌ی دستگاه‌های تبلیغی و رسانه‌ای رهنمود داده‌اند؛ بیش از گذشته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/684281" target="_blank">📅 20:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXFtJ6Tf2VD1rS4XsLhmlsIU-7dEfTh-kzV6Yeq5EoIctyz2ylR3-WNerJ6CKl1RUIl5Voy7bIgbJBlCK6YLSx02j9WJmjs7sa62rz3kClmr1eDlyuouM8cMldbnLTSa-xt-TUF6O32Ios0Mu16GiJbOMY-FL-UqvIPf-vfSwRwKPKXoaLSJRo6-KkFt_btyxR_9JTOFmSW_yMt-WEFE_VR_hGJ_hO4wGNCSoCn4E8QiSu5g8uJb8Y86bKyaR3Rjdq_Two_2nNDXep4jb3cYQjbJAao6kjDRwrEM_AvrTZBcKl1-FvaUhvs0lIKjOT2gXrmGFrCCt-Tm6ByVaToi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد ۴۰ برابری پزشکان زن ایران طی چهار دهه
🔸
طی ۴ دهه اخیر، شمار پزشکان زن در ایران رشد چشمگیر و ۴۰ برابری داشته است. تعداد پزشکان متخصص زن از ۷۷۴ نفر در اواخر دهه ۵۰، به ۳۰ هزار نفر رسیده است.
🔸
همچنین آمارهای فوق‌تخصص نشان می‌دهد این آمار از ۳ نفر به ۱,۵۰۰ نفر جهش یافته است.
🔸
این رشد در حالی رخ داده که جمعیت کشور در این مدت از ۳۶ به ۸۷ میلیون نفر رسیده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/684280" target="_blank">📅 20:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سخنگوی دولت: سهمیه بنزین با نرخ‌های ۱۵۰۰ و ۳۰۰۰ تومان بدون تغییر حفظ خواهد شد
🔹
تاکنون هیچ تصمیمی برای افزایش قیمت بنزین گرفته نشده است؛ هرگونه اصلاح ساختاری نیز با رویکردی تدریجی، شیب ملایم و بدون واردکردن تکانه به زندگی و معیشت مردم انجام می‌شود.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684279" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684278">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de944fba7.mp4?token=pxqiMDfLcWozdXDi96-al7T0enO6B57AtDleLoEsIUVZIr9vqtqNja_Ye_TOWH4FNbBPEIAsFvABayZ5NDgc-LgIkdHjXcFIlu_mn3JWjme8juf_3NQP0vIJoQLmgFh2oL1mUN5WGN8sWK6QTc1CKoM7CxZri_sDg_GEj3aFpE_n-SdWwYGxtnVjSYk_9wAj4bqqdWjgvv6NCaGRaGZOE8dGoHjybAmdjZEYMXLnivP6E9tJcBSuIU64Z-KKL9AMP39tTbYtbHNqMRn8Cy-gz8h32EoYyWOEG0ixVuJXY_vi1a20x0adfjYvdcM1Zj_ZGEunD8_4WzZPpZ8USGg6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de944fba7.mp4?token=pxqiMDfLcWozdXDi96-al7T0enO6B57AtDleLoEsIUVZIr9vqtqNja_Ye_TOWH4FNbBPEIAsFvABayZ5NDgc-LgIkdHjXcFIlu_mn3JWjme8juf_3NQP0vIJoQLmgFh2oL1mUN5WGN8sWK6QTc1CKoM7CxZri_sDg_GEj3aFpE_n-SdWwYGxtnVjSYk_9wAj4bqqdWjgvv6NCaGRaGZOE8dGoHjybAmdjZEYMXLnivP6E9tJcBSuIU64Z-KKL9AMP39tTbYtbHNqMRn8Cy-gz8h32EoYyWOEG0ixVuJXY_vi1a20x0adfjYvdcM1Zj_ZGEunD8_4WzZPpZ8USGg6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب مسجد تاریخی ابوسلیم در غزه
🔹
حملات هوایی رژیم صهیونیستی به دیرالبلح غزه، روز دوشنبه منجر به تخریب گسترده مسجد ابوسلیم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684278" target="_blank">📅 20:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684277">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
وزیر دفاع سابق اوکراین: در جنگ با روسیه به تدریج شکست می‌خوریم
میخائیلو فدوروف:
🔹
اوکراین به‌تدریج در جنگ با روسیه شکست می‌خورد و تنها چند ماه فرصت دارد تا تصمیمات اساسی برای تغییر مسیر جنگ اتخاذ کند.
🔹
اوکراین فاقد چشم‌انداز روشن برای پیروزی و دچار ناتوانی در نوآوری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684277" target="_blank">📅 20:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684276">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r67IIfv314TsOVPmFepkVQr3Uzl_GCfqtveVM3t_uhP-ljBDzcnqQ-NYPXIKsQZywmBrKHr6CFVcvOHiD7gwJLS-20_j5Jpd2_QeK_Qw8ISMgH8gKX-spJsagvfjZ9dQXwi7OyTl_lsbL7XCv2e3o4VFlC48NrZ5wpKaFdhNW51LvlwVPGxXk3GeXAfjDl5mK12j6IqW9X3AwMqaB_AJnLSWqHrMSP6gi5AhH5SheVa13yTFFWbMeky7qnRJq7uUZsdLKj8mirhk3B5WOxfmV2FTSMnzePQBYiJWUaU_x2oMftNB1Y5j6ti4PfYXhi3FZ9NCO-cQJF0whquXXoeFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
البوسعیدی: موضوع مدیریت تنگه هرمز در آینده بررسی خواهد شد
🔹
وزیر امور خارجه عمان امروز سه‌شنبه گفت «مذاکرات سازنده‌ای» با عباس عراقچی، وزیر امور خارجه کشورمان داشته است.
🔹
البوسعیدی ابراز امیدواری کرد که به زودی ایجاد یک گذرگاه موقت در تنگه هرمز و تمهیدات عملی برای بازگرداندن ناوبری ایمن را اعلام کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/684276" target="_blank">📅 20:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684275">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e43cd1c9.mp4?token=RMCm8VvMfC-OiPOTyoW-ExfJ9vcvg7JWH1KyD9doGh7ghrNGIPfXS4RobDwKgo3aNC2KGdT_HrMVfI6mItvYsdlSYXX_NpkbOgPt1J1-gt136NEor8jF-5m-EPd6olyn5lP5Qn-bPnXVoQxrz-2rUwtYbR_mOnDhnt97NRTCQw3O5Gw9Nbjno3QXFq0uuH1PanQXvSUVorKLvgywjUsNQObdT_4Ktzhe0D10VwcsyYHHY6kJ2ixDRJkZZ5Ij4ubPejdNlp-u2dY2Pzrg-s5W5EyCewqQxJ0vEuYijF92K5DyurHfkQrk5Nv4Fhuo_BvMj7P60HiQk0K94ociOp4kDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e43cd1c9.mp4?token=RMCm8VvMfC-OiPOTyoW-ExfJ9vcvg7JWH1KyD9doGh7ghrNGIPfXS4RobDwKgo3aNC2KGdT_HrMVfI6mItvYsdlSYXX_NpkbOgPt1J1-gt136NEor8jF-5m-EPd6olyn5lP5Qn-bPnXVoQxrz-2rUwtYbR_mOnDhnt97NRTCQw3O5Gw9Nbjno3QXFq0uuH1PanQXvSUVorKLvgywjUsNQObdT_4Ktzhe0D10VwcsyYHHY6kJ2ixDRJkZZ5Ij4ubPejdNlp-u2dY2Pzrg-s5W5EyCewqQxJ0vEuYijF92K5DyurHfkQrk5Nv4Fhuo_BvMj7P60HiQk0K94ociOp4kDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: صداقت پزشکیان و اعتماد مردم به او باعث شد این ۲ سال سخت را پشت سر بگذاریم
🔹
از ماه اول دولت، افزایش ذخایر کالاهای اساسی را دنبال کردیم که باعث تاب‌آوری در جنگ شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684275" target="_blank">📅 20:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684274">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbCo_AfqGjInnpihShw2vTslQ8BQrjeZAQagALb-TBlMrx8joajk-iBcK2wDL5Ya3ny_XuZhLigT35PP5Nrvk0G5vZ9hqEhpkvrUNtYPGOAx0Ilk0D5NcL7K5kOrhsY5dNcWXnx37GLAQOv2O1sHRXqKyz5VcVHJx30InIW2PG8yl0uQZ5tB3F-DUtq6G1Xj7Vz3FXDi7XyPxOBN8I6QGQQ70VSLVU3S_tSKSFZwG5WB3yJ3hrcWN-YBGppAFCHV0iSHCZhnEyBKnIvN1lc9cg5pBxKb7Ft06Pv4Az0ZTSqIpVAys11R6p6FgHpQiHzpn0ZKJ6fhszar5olJRgdiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای تلخ پسری که اخته شد و به عقد امپراتور سفاک درآمد
🔹
اسپوروس یکی از آن افرادی است که تلخ ترین سرنوشت را در تاریخ بشر داشته است؛ سرنوشت تلخی که قلب هر شنونده ای را به درد می آورد و سبب تالم همگان می شود.
گزارش تاریخی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3240346</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/684274" target="_blank">📅 20:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684272">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
نتایج اولیه آزمون کارشناسی ارشد ۱۴۰۵ منتشر شد
🔹
داوطلبان با مراجعه به وبگاه سازمان سنجش و وارد کردن اطلاعات خود، از نتایج مطلع شوند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684272" target="_blank">📅 20:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684271">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqRJturpT_T2FwNsY-W8X_smWuSGKOI8AbWGIPSFX35PnHqenCpSZkRWbVCE1oJ-i5xwQNWgI9b-rL10gKY_hlY0bsYgNz5kUkBmhRmL5UbZsv_RBnKwxPqJbzx_MYpjr5w_wxbNCaJwWLnc5ccDG2jJ41L80B9Fp92M555xLcYdX5q7Yn4Pf1THKQX6cD2GVRp_0RhmTptk2eh11CHuWZ3TcN_334kGf-MBMEpBQG2FYeELOonbx86g-NWdl1l_gPjv8EFSGWzd22-5qMyePvQy19Ace0aNol1zvkHuF9hvEysvozyxGJ12icNUOtIp6CdfHLMiEld2-azBFPSL2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیکزاد: قیمت بنزین افزایش نمی‌یابد  نایب رئیس مجلس:
🔹
مقرر شد سهمیه ۶۰ لیتر با نرخ ۱۵۰۰ تومان محفوظ بماند، سهمیه ۷۰ لیتر با نرخ ۳ هزار تومان به ۵۰ لیتر کاهش پیدا کند و سهمیه ۳۰ لیتر با نرخ ۵ هزار تومان نیز به ۱۵ لیتر برسد.
🔹
نباید برخی افراد بدون هماهنگی،…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/684271" target="_blank">📅 20:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684270">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_GUZo-NfEKI-59veiuvVl6bjbIA1-ppl7fXMsy77fcxaW-EBysgRE6KsZMyfSCgWEPfYOxw_MmT-MMNuJiesuNXtwXaobHYRMuPPEsiBBulIBfc5wUz1tyGjHFKjxYNv8HxfqLdlHv5URbEo_jgrpiqAIrmvZdKE3gj_c1ibQ0xRkEc4oQWMNNudHJA_WMU0tZctJWuvLgcCMhu4mgFATjAF3gHjuOVSPRHpNRvCJTbDKZZrFWtZFFkO3pJJHdcQO92c1arDocYLupKU5AyRJN-zio1Jvh91ea40SL9x7LE1Pb6pER__-40h2-bIoIIVZhvTjK4jiHS78BS8yZ-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت به پاکستان
🔹
آمریکا در بحبوحه جوسازی برای تشدید فشار اقتصادی دوباره به پاکستان و عاصم منیر رو آورد تا منیر بعد از پیغام و پسغام برای درخواست بازگشت ایران به میز مذاکره در سفر تهران، به پاکستان برگردد. رسانه‌ها در گمانه‌زنی‌های خود از احتمال بازگشت آمریکا و ایران به توافق اسلام آباد خبر می‌دهند.
🔹
هشتصدوچهل‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/684270" target="_blank">📅 20:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684269">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">04 Ane Manaee (1403-08-03) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/684269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه چهارم
حجت‌الاسلام امینی‌خواه:
🔹
دوازده تقابل بی‌نظیر در سوره مبارکه محمد؛ مرزبندی ایمان و کفر! [2:01]
🔹
طلوع نابودی در قله پیروزی: سنت الهی در انتقام از زورگویان [9:15]
🔹
جان‌سوز اما جان‌نواز؛ وقتی زنان و کودکان هم طعم شیرین شهادت و جهاد را می‌چشند [11:58]
🔹
وعده شهیدسیدحسن نصراالله: اسرائیل به ۸۰ سالگی نخواهد رسید! [18:38]
🔹
از شهید آرمان و حججی تا یحیی‌السنوار؛ خداوند قهرمانانش را به دست دشمن معرفی می‌کند [24:31]
🔹
دشمن احمق ما را تهدید می‌کند؛ ما در انتظار لحظه رویارویی هستیم [27:58]
🔹
حق، مانا و باطل، میرا است؛ زندگی بر مدار قرآن موجب ماندگاری است [36:06]
🔹
نقطه تمرکز دشمن، قلب آرامش یاران؛ رهبر معظم انقلاب، ایستاده در خط مقدم [47:08]
🔹
پوچ‌های فریبنده، گل‌های ساده؛ آزمون واقعیت و جذابیت [50:35]
🔹
از قیام حسینی تا سکوت صهیونیستی؛ شیعه واقعی کیست؟ [1:21:51]
🔹
نازدانه‌ای در ویرانه شام؛ نامی که جاودانه شد و ظلمی که نابود شد [1:30:18]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/684269" target="_blank">📅 20:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684268">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b8679b56.mp4?token=WYNncPdCmwfL23yUgL54FIoODYFDpvYiFRqLgY--8cNyWGrRMgn-W4hgvEV8fLEifBtCMMhYJdYUZnQlTCJTH5U1bQHvmpEprUsS_xN9tXOmwLna-9lNJCz_kuAysYZnnvYzg3vm7vFXhqwLywk5ZDfQ9no_7o92Q0Fhlvffi8Qlr5wKomJaxvq_nDOdpOZ3lFqbx6g7Cl2xATb8FPHzGwtRdZToUJsZK2a63iGViBa3F8AGnhmAeYOVF2gK_Qk4aj_s9WgNQWWcBadhhWvap8FljJ-KsKzbUsx0PpAcbDgubc2mesY71I-wti97LdfrpErB1ugqi37I_QzOEAiKwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b8679b56.mp4?token=WYNncPdCmwfL23yUgL54FIoODYFDpvYiFRqLgY--8cNyWGrRMgn-W4hgvEV8fLEifBtCMMhYJdYUZnQlTCJTH5U1bQHvmpEprUsS_xN9tXOmwLna-9lNJCz_kuAysYZnnvYzg3vm7vFXhqwLywk5ZDfQ9no_7o92Q0Fhlvffi8Qlr5wKomJaxvq_nDOdpOZ3lFqbx6g7Cl2xATb8FPHzGwtRdZToUJsZK2a63iGViBa3F8AGnhmAeYOVF2gK_Qk4aj_s9WgNQWWcBadhhWvap8FljJ-KsKzbUsx0PpAcbDgubc2mesY71I-wti97LdfrpErB1ugqi37I_QzOEAiKwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند، پوست سیب‌زمینی آبپز رو یک‌ دقیقه‌ای جدا کنید!
🥔
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684268" target="_blank">📅 20:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684267">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
جلوی واگذاری اموال بازنشستگان را بگیرید!
🔹
محمدعلی شهابی روزنامه نگار و کارشناس حوزه تأمین اجتماعی اژ از تصمیمی عجیب توسط مدیران وزارت رفاه و تامین اجتماعی خبر داد که گفته می‌شود صرفا به دلیل انجام قولی است که احمد میدری در مصاحبه تلویزیونی خود داده بود.
🔹
شهابی در کانال شخصی خود نوشته است:
سازمان تامین‌اجتماعی برای ضمانت خط اعتباری ۴۱ همتی بانک‌رفاه بابت پرداخت یک‌ماه از معوقه‌های حقوق مستمری بگیران، سرانجام این املاک را برای تضمین، صورتجلسه کرد:
🔹
۱۵هکتار زمین در شهر پردیس به ارزش تقریبی ۵همت، زمینی به ارزش ۶همت در مجاورت سازمان حج‌وزیارت، دهکده گردشگری انزلی و‌هتلهای هما؛ تمامی این املاک با قیمتهای پایین‌تر محاسبه شده است؛ ناتوانی در دریافت مطالبات این سازمان از دولت و یا خط اعتباری از بانک‌مرکزی، کاملا مشهود است. این بدعت خطرناکی است و از این به بعد و با این اتفاق، دولت دیگر هیچ بدهی را پرداخت نخواهد کرد و بانک هم پس از مدتی آنها را تهاتر خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684267" target="_blank">📅 20:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684265">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBewE93Spbbp64NpDMudUcBMKFLiL5RgV1FEnntvjp-zTHB0dWgW_j0mukN3j772eUe8ejxO7qrMGJ9B7l7R_w86tzi0HLXCmOcIMFPBREebcJIVkr-_oQL3EzPU658XK7kdA_qN9Y3KlP12y44bm1KogM1wo9DUBRPI42-nKsXml46NPUVz2O6KBzMdBtGKdnZdf60nZQ_ENT8qoS9DJSIKSUmuIEXVH4zdjMk-LRPus3WvEekOidu2qvsJs7-Ll1QYCV6MnnoTBX62pBFppgHBAdgi2VyoQbHRpCfx64clk_I_FGgKhtM37aJ1MHjbH_1PQ6vTklMgbrg0VK4CEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرزپاتاید؛ بخشی از مسیر مدیریت وزن در اروپا
🇪🇺
مونجارو (Mounjaro) با ماده مؤثره
تیرزپاتاید
، در اتحادیه اروپا برای مدیریت وزن در بزرگسالان واجد شرایط مجوز دارد؛ البته در کنار رژیم غذایی کم‌کالری و افزایش فعالیت بدنی.
براساس اعلام آژانس دارویی اروپا، این مجوز برای افراد مبتلا به چاقی(BMI بالای ۳۰) یا افراد دارای اضافه‌وزن(BMI بالای ۲۷) همراه با حداقل یک عارضه مرتبط با وزن صادر شده است.
این موضوع نشان می‌دهد درمان چاقی با آمپول لاغری، بخشی از یک مسیر پزشکی و مبتنی بر ارزیابی شرایط فرد است.
در ایران هم تیرزپاتاید با نام
زیکورپا (ZCorpa)
، محصول
داروسازی دکتر عبیدی
، در دسترس است.
⚠️
مصرف این دارو باید با تجویز پزشک و همراه با اصلاح سبک زندگی باشد.
🔗
منبع:
آژانس دارویی اروپا؛ Mounjaro</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/684265" target="_blank">📅 20:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684264">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد:
🔹
آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/684264" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684263">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e44fe662.mp4?token=ra8LlSZcJ0MRFKxYHi6zeTbhe5d7oPUg8k1xBoeJWtKjJXBxIum9Dygrb0M4RhaBACcsEx6GZcXamA5FD7nY1qAnsc_GV2Ray3yaajWLN0bCCZ9KzDw_yl8XOCRTkmuZE4HX41c1CtO3yvOyZ6uxtYRehi_zpGwbsb8EByBSRnkx_pMlIfv8f8ZgSl_EkFGQcYf7xabhr_bvUzhGb6ZYeVc5qMJjUBGpNVG8yrhjlT7oTGO_5up1n_ENJtHb0KTtlhrTV2tZvR8-_gVc8NXt2ebp7238fBTTqIc9luLsZlfbKjJIyin5fWDWd1wDe_lJSaar1Anu-QckDDP7rYZ8ahYDdKpI_FM0ZKZSkoK-sJSJm3Ayo77gTjaJXS_gdLQlRPkGcHotjJs0bVJlElMNfmSE6B4EZoEeDW3mYthSULkmRV8WpAFC0O34KLMzvVx7ZOHwRi1NW8ADfL_qnYU8LkLqezEtz36EasGOYqHg4JwWWqI52iykTeAlvToW5vUzbgJYJy-eeugUapIcCrwFu9RZb0TDwUAWa3utj2hM-dgnXYruII-piwLllJsQ2l9ZkUWizi83i14BLjOCOlTqfg8_ypcKta3f0DUGbLDDdoj7pYRYT-vR0fzZpoU-HMKsIFi5pX5lncDiizf8nqR7szinvj27B83HPzQo5YlCp5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e44fe662.mp4?token=ra8LlSZcJ0MRFKxYHi6zeTbhe5d7oPUg8k1xBoeJWtKjJXBxIum9Dygrb0M4RhaBACcsEx6GZcXamA5FD7nY1qAnsc_GV2Ray3yaajWLN0bCCZ9KzDw_yl8XOCRTkmuZE4HX41c1CtO3yvOyZ6uxtYRehi_zpGwbsb8EByBSRnkx_pMlIfv8f8ZgSl_EkFGQcYf7xabhr_bvUzhGb6ZYeVc5qMJjUBGpNVG8yrhjlT7oTGO_5up1n_ENJtHb0KTtlhrTV2tZvR8-_gVc8NXt2ebp7238fBTTqIc9luLsZlfbKjJIyin5fWDWd1wDe_lJSaar1Anu-QckDDP7rYZ8ahYDdKpI_FM0ZKZSkoK-sJSJm3Ayo77gTjaJXS_gdLQlRPkGcHotjJs0bVJlElMNfmSE6B4EZoEeDW3mYthSULkmRV8WpAFC0O34KLMzvVx7ZOHwRi1NW8ADfL_qnYU8LkLqezEtz36EasGOYqHg4JwWWqI52iykTeAlvToW5vUzbgJYJy-eeugUapIcCrwFu9RZb0TDwUAWa3utj2hM-dgnXYruII-piwLllJsQ2l9ZkUWizi83i14BLjOCOlTqfg8_ypcKta3f0DUGbLDDdoj7pYRYT-vR0fzZpoU-HMKsIFi5pX5lncDiizf8nqR7szinvj27B83HPzQo5YlCp5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تریتا پارسی: اینکه تحریم‌ها منجر به سقوط دولت ایران شود بسیار بعید است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/684263" target="_blank">📅 19:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684262">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
کانادا تعرفه‌های آمریکا را با تعرفه جواب می‌دهد
وزیر دارایی کانادا:
🔹
کانادا تعرفه‌های آمریکا را دلاربه‌دلار و نرخ‌به‌نرخ اعمال خواهد کرد.
🔹
از ۸ سپتامبر، کانادا بر واردات ۲۷.۶ میلیارد دلاری از آمریکا، تعرفه‌های تلافی‌جویانه‌ای به میزان ۱۵، ۲۵ یا ۵۰ درصد اعمال خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/684262" target="_blank">📅 19:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684261">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نتایج اولیه آزمون کارشناسی ارشد ۱۴۰۵ منتشر شد
🔹
داوطلبان با مراجعه به وبگاه سازمان سنجش و وارد کردن اطلاعات خود، از نتایج مطلع شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/684261" target="_blank">📅 19:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684258">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: جنگ اقتصادی آمریکا علیه ایران، حمله به حاکمیت ملی همه کشورها و تعرض علیه حق تعیین سرنوشت همه ملت‌ها است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/684258" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684257">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsJXuHHZbYknsV5aC0UROsQybFWuTX-7cnpHpiE2nIIuf91OTsQtL401mIWX1D_uAV3Hh9H_-QKzhzXJv1uvbLVxVQ6vDQ_OEahKQzVld06B59IwwyofPMCxfzyVcVe7osmpLL1fZpqX1qSHjR4eubuzunyznecRnQxz5p3NOwgSHO9WeDb28QYNenrJgZzMA1NzEfCiTWxcedDGZHtVw5ax89tLeKMUOMMZmVAiOX4Z0CQa6aqOWFN4AIdeoVSIeqxtHhD67-I3s7ib1s5dmvifNxRIwmWi2MZA5l8JO3J8Fp09tW3UP2Jb9eozqxKf9SxYu36szgMTuOIUiCPOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران و عمان بر تداوم همکاری برای امنیت تنگه هرمز تأکید کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/684257" target="_blank">📅 19:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684256">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZz8tDD6Qizdp397pV1JrAq7530v8wfQOgQUCllfs39TUFIWleR5nFWOtwPcZasCKE98LW4qCvCbM7OEgrgkmTf4UjykLFPmfc-EZwbrcqDb7iR-K2XVg4hxK4-OxcAfyxGh5XBbJF9_NNRq3ZQ6NUI7rnjAWII4jNh1dlN6WrXs1j-0XYNnBCSj7yqRJyesFXxnPjqrYeNiDSQlddw_FFp5MuObOUMX-TpXD2QopLp9ZJXOPxbufHkJaZIlC9CJ8SZLNPbSVnY4bmnSrMAX3WQ7IiFP_SWVXUhziuTt5-aPpcMa1Xl0bMBRSnZxQippaGvLNXm1uwVSIXbz_KvwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: ما از طریق نیروی فضایی، تنگهٔ هرمز، کوه‌کلنگ و ۳ سایت هسته‌ای ایران را زیر نظر داریم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/684256" target="_blank">📅 18:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684255">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzKMZOPZ3TgqL99yR_TjnkNJLH2m8-CXwfASXr3T5cLOrQ4e5SyUczMaR95xjpmIKvZlTNc_rlvdjhohKVHrbin-qQlHS3izSm5IWczGKHeK2ssfZb7W8NafutR8rcnytjdeHTfiHMUCoPcgS7xxEnruW0xi3VwNT_thp-SEcGyVnI_wBeWuBdMleIMSAENb2qre7nsdhY-82hSInoBEv4cCCejZm5ceMCmDmxXLeomvcTug-uNLD1mwJRwpgNlO-tJQVDB2045mLV1WD2HtP1J4cfeLtuSx8Af_P1twxd6--J2KVQlojzV0WJektUIdexINAPImWfcS4eAcUnL9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در جلسه ۷ ساعته رئیس‌جمهور با رهبر انقلاب
چه گذشت؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/684255" target="_blank">📅 18:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684254">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تاریخ نشان داده است که تلاش علیه ایران دقیقاً نتیجه‌ عکس خواهد داشت
الجزیره انگلیسی:
🔹
لورنزو کامل، استاد تاریخ در دانشگاه تورین ایتالیا گفت: تاریخ به ما می‌گوید که تلاش برای منزوی کردن ایران دقیقاً نتیجه‌ای عکس خواهد داشت.
🔹
آنچه این جنگ نشان داده این است که آمریکا به شدت تحت تأثیر اسرائیل قرار دارد و بنیامین نتانیاهو، نخست‌وزیر رژیم اسرائیل هرگز به آمریکا اجازه نخواهد داد که به توافقی دست یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/684254" target="_blank">📅 18:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684248">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hs2E4wGSNA_wk8CbpEXg3G99x8W9Ubjp94Fi7yjIVBdDJjFw3x4rFUh3UuERToUGSP1CMK08N-tL18uAQorVpkW96lV13v9Z7CJMsT1R74x5LuLYyG5DLaButIPvtmpaZnbLyMhbdGAAPPbyl-LYUkJxM60siYwjlRH8paHecGAhkhdzddQag3jtMn1DzzLebeyOor7Sa7N-gHGC5rWQckZatI4ucOuLInVVL2REIbIngHGJHClR48kb4ICYs162mrC0UU3VL3k-1S5FBI9JIvjwrvdq1JZlJH0G18blBR-O2D25SHrNnCYJMuiIfnR1E-L8nwLYmf5Fm8kFCGwk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USrL69gO4I3e-e0ICBwrZsEmu-A5BGTEUKnbklaQPBkmaRHRUh9FnQMJb_9gpH15yDP6AUiynpFO5X6cmeRTsoi7nR-JBjRCaAS8mjv4Kk3w7sbL7gpQidARBoHQSqSWrr-zR6Kg4wEUvY4GQnI2Fl2yBKgoFhxVXWtQPZy2qJF5Ovnx2QkgWRllXVBhCXhFPuHNvVU5E59Y0yzDzrOTO15tHdN0mh8OaCjAE89GrhGkjrKBw7DHWJfUzh5xQhDe1VL54aVKFe6YsDurvLaHCcoJim-K_Fk2_c3l_Q_cvNBue_RxwjGvf6ZZ2r7rEOSWXJkUuGHS5eEcPR_ESG_y2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLVG6J4mRFp5tvCw54aJ-70lnZ_4GS8xThSxlLbpMojH-RCcb2NbKnhad3PqdmHC7cGgpMmBAGSDn0FrXBZkfKpep3f_H3W3XzWvo0LGCH861M4kmA5nChISGVsBYfuzr3yrQmR7zZk_tUwB7p-M9fBSv0hDYc6aZh5Dx8glqDYG18dkmpmnSe9IuYvit5HbqJ1jniZqC7ng4GAct-Mq2WDU1SFcld2dV7cYUcMkit-zkFxfzIefDxAR0-v33F-mB7xi4N88uFV6ut8OOoF3Xeymh2jjrlqmPrdOwQj4FrkFo7p9yEWX90Ntm9aoQIklmFqfaMV1puyCNI2luoW4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHRv4m4V9ygbWyW_x5sCDQf6uEPgnBxPe6rIEMfQ_37f1SVoIpfrOnrMFWdCGIkgi9xvauyOZC4P6pdQeuv6-tKWM0l2lR_CkyalMMMk6zmRHHU1iarIsjfbEKt8jEAFnFQzKJx_b_VsByCwzoeYbN0EGlD9OqgbZvERAyUpVd3QjNfwSik1kJGq8jGutIuTKpVh9W-gpP-1gQop3vGHT7BqKL9wAkxtwTZpRa1DMGMAHkvD1R8YBHXZL0W2s7xRYZBdmLGZwEK-EW_rvvD6JNALzW0dU9aFoCopqLew-bD3hpTgXUNxlw8Q-nudPztU7XPAnT9Zxh6415pa02yfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6PkBPha4_UBz4G8G8p-9pDbS7DZ-fide7iWnzRggjJofToh0napo-NVuiIVaIvL-n-s4VStwOiFtrsLQiNXaVxhaLwUic17tK8g5Kf6Q3mRQF2VJllMWQk5LcJkxkWgvhaoILryhy_bjfbpCLJNWrpRf5xefZA1sEfUGqxDyiKdaGXj6k3kqzvAXUdo5IRWyCpEQTCm12EIcY-MCaG-NvNO_br3P2-XSr663AGV2dfNJpg2UjkwC9xlT6EvmuJkY0fqiYdy5dOnWdZaUpMr369GNAykrLti4syEIvmwHuOEn3PnqkXzVyWQm1w-gktYcUSUtxEovwyqEDlXyk1iTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgTIXw2s8A2CWqBPlJrQzJx10qMYjLzH4v6AIU5aS3uYwsREumBtt6Al9CyYkJFsrd0rIf_h8714cW1sYwGpH_zr-ZFXrGAO-UFashgoB-r_kuS5hlfAY38L3Ed13j4Rng_cZ7Dtpox85iIMsrUePHoIu3yUlfABKfempemTWrIQXLYu0k-erF58pLCIyxZeQy2hAxp4e8YggoLMlbnbqFFnjcUb2oU592K1Z1Kx8Cki3_cnuDJTk34dd3TTC9PvXFKcIlknzU334lU9a2kcnbnCyECKmGVQ1xdrG0W7pvg6FoPuPOcNwHU7wGgGFnkDgHWZCrf0K-p4cuKvgnhsnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۶ مدل خمیر در کاربرد که خیلی به کار میاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/684248" target="_blank">📅 18:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684247">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZzFyLw7-Am2yzxd8ebj04aZ5yRK4Z_hyxaT3CLU_n1zD0e2amaUyH8CXX8rhuXo5ZX92-IyOcG3Qk7yhvpVPgubKQIv8kGdc-MVXR2u6fF3bAIur50nEVlYjf6vUo_DRvmQfuK3dsz963lw6-FE-qEBiBUgjm3-0vkPO4_60I2eOp-HVCzax1UWO2WzDIukmh3T10csdEvaNERwlnvGFWf0nlOiqxPtqsFvVIi8O69E6lJbl6ZyK7H9gmvIX3ytBGopl1ahySFtM8aDDLknU5Snd70tG_AE9j30Lqg7jtWqkxYiSjiBgoUST_YgoUgx9J6_1una1OrDBNbpZEcZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
♦️
عارف: تنگۀ هرمز ملک ایران و متعلق به ایران است
معاون اول رئیس‌جمهور:
🔹
نباید اجازه داد افرادی که حقوق دیگران را نمی‌شناسند یا همه چیز را با تفسیر خودشان معنا می‌کنند، درباره حقوق ملت ایران تصمیم بگیرند؛ این همان چیزی است که در فرهنگ غرب شاهد آن هستیم.
🔹
مردم از ما دفاع می‌خواهند؛ دفاع از ایران، دفاع از نظام، دفاع از ناموس، حیثیت و منزلت خود و همچنین نشان دادن اقتدار کشور. این یک راهبرد جدی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/684247" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684246">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
پزشکیان: امضای توافقنامه از روی منطق و آگاهی بود نه از روی وادادگی
🔹
تصمیمی که در شورای امنیت اتخاذ شد، مبتنی بر خرد جمعی و تعامل میان سران قوا، نیروهای نظامی و سایر بخش‌ها بود. اکثریت با در نظر گرفتن اصل حکمت، عزت و مصلحت، توافقنامه را پذیرفتند.
🔹
هیچ یک از افراد وا ندادند، چرا که همه آنها توانستند جنگ را اداره کنند و در برابر قدرت قاهر اتمی جهان ایستادند. بنابراین امضای توافقنامه از روی ترس و وادادگی نبود، بلکه بر اساس منطق و آگاهی شکل گرفت، اما عده‌ای کنار گود نشسته‌اند و مطالب نادرستی را مطرح می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/684246" target="_blank">📅 18:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684245">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ترامپ: کره‌جنوبی حاضر نشد در خلع سلاح هسته‌ای ایران به ما بپیوندد.
🔹
کاخ سفید: در حال حاضر هیچ مذاکره یا گفت‌وگویی با ایران در حال انجام یا برنامه‌ریزی نیست.
🔹
پروازهای ایران و افغانستان افزایش می‌یابد.
🔹
مسیر شمال به جنوب کندوان مسدود شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/684245" target="_blank">📅 18:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684244">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
واشنگتن‌پست: ایران طی دهه‌ها تحریم، شبکه‌ها و روش‌های پیچیده‌ای برای دور زدن محدودیت‌های مالی و تجاری ایجاد کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/684244" target="_blank">📅 18:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684243">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot5w8-P5TPw8XOvyKH7yKVpYGeFOEJ2ECj3L-0ytmZnV3V9XrY-wcSjFaSOQW60zeAxpJp1XrynH4P5Fo0ueq5uztQjtrvGG0QKhmICu90oFGV_FhBrBkIoAI2dgJ_ujaXc8ZKT5F7cj1ylQBoO4aZMUXWF6pUr8DSn8sNOBQqRqKFcNhIub6S8K6GClsLWnE-dHMb1Jlupw7HS5vdSu2iJCW_VdZY5GY1HdhIA3jKLD9Q2uxrVZSI1XS6Dh0ack6Gne5hZQvi5edLsfV73Y9EG4f4llZbmVNlr6zASivb_TXMyijvMvBFSayNx3eTw9d4Xj_zUEjBx5Pb3uh-VHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانگین ناوگان مسافربری هوایی جهان
🔸
بر اساس جدیدترین آمارهای جهانی، میانگین سنی ناوگان مسافربری هوایی ایران به ۲۹.۳ سال رسیده است که فاصله‌ای دوبرابری با میانگین جهانی ۱۴.۸ سال دارد.
🔸
کشورهایی مانند کویت با ۸.۸ سال، هند و عربستان با ۱۰ سال و قطر با ۱۰.۲ سال جوان‌ترین ناوگان مسافربری هوایی جهان را دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/684243" target="_blank">📅 18:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684242">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ترامپ مدعی مین زدایی کامل تنگه هرمز شد
ترامپ:
🔹
نیروی دریایی ایالات متحده به من اطلاع داده است که تمام مین‌ها از آب‌های بین‌المللی تنگه هرمز برداشته و/یا منفجر شده‌اند.
🔹
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدیدی کار بگذارد، بلافاصله و به صورت سیستماتیک منهدم خواهد شد.
🔹
از طریق نیروی فضایی، ما هر وجب از تنگه را زیر نظر داریم، همانطور که کوه پیکاکس و سه سایت هسته‌ای دیگر که قبلا منهدم شده‌اند را نیز زیر نظر داریم.
🔹
سیاست عدم تحمل در مورد کار گذاشتن مین با قدرت کامل در حال اجراست.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/684242" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684241">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBW0YVREZHxOVtn-dMN1bSsC53cIvMyOTEzX_FcJGWN5kS7NScJuSmtCEnJv1kRB5g481KwXOoCWojZPAS8OBn4fJdR8Yl6DEh7U7w9GYNVyW7UvgAwBNnScLUKWYBbfbpO7e-Xfu3M4aKn3bUqtyj3rmkD1X4BVT_A-ocKLfMBSBSEk2SDSuqV3hj8KXDYkJEFlN3DOA0PHB2SP4Jk7R_3Cps9Vd1RpmyptcNx8EFNfJR-27EBoSNX0RyWjoydgPrjt2OGZoWYVNU0infwgWfybQYJo-ZEfgoRTMnIrBroXFDGB4U2drIs6USIWNpBcKuiaZbIo_zrevCfKRhdY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشتر افراد اعداد کسر و ممیز در انگلیسی رو اشتباه می‌خونن، بیاین خیلی راحت یاد بگیریم #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/684241" target="_blank">📅 18:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684240">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52ecbb56d.mp4?token=lNgP00oVY9x1QFGpHwDUjGQaWUFdiogRg_UguYiJNUW16BlpcmTWnSSbQp5CIEqLRFg1_brgy3YRW_Ihzy8ChBzxxFU3kXnGWxTFdME5PeR_7tlYRGJLXUgq-qA_S9Fox3XdK_p4LvvFFRxGjyRKgGqRhR8R2Nq4mslFu9OLi7N_wDNHvLVBq5IjFyJFIGj0F-VcpBwipSBCfuzMvnxP7sW4OZ04N1ipZ96I6SU7k3mgGlvRtThqRNdG7SnltHZjfp1ZOGCpKfLYFnloF5yzfGldZQ6XeK_X8wmsGuwM8_YrU6mH_b2ieK6iMOX47QlWtLOiutDtePAHO5N7W_2iug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52ecbb56d.mp4?token=lNgP00oVY9x1QFGpHwDUjGQaWUFdiogRg_UguYiJNUW16BlpcmTWnSSbQp5CIEqLRFg1_brgy3YRW_Ihzy8ChBzxxFU3kXnGWxTFdME5PeR_7tlYRGJLXUgq-qA_S9Fox3XdK_p4LvvFFRxGjyRKgGqRhR8R2Nq4mslFu9OLi7N_wDNHvLVBq5IjFyJFIGj0F-VcpBwipSBCfuzMvnxP7sW4OZ04N1ipZ96I6SU7k3mgGlvRtThqRNdG7SnltHZjfp1ZOGCpKfLYFnloF5yzfGldZQ6XeK_X8wmsGuwM8_YrU6mH_b2ieK6iMOX47QlWtLOiutDtePAHO5N7W_2iug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقدام تحریک‌آمیز وزیر افراطی صهیونیستی در مقر آنروا: «حالا من جای مدیر نشسته‌ام!»
🔹
ایتمار بن‌گویر، وزیر افراطی امنیت داخلی رژیم صهیونیستی، با یورش به آموزشگاه وابسته به سازمان امدادرسانی آنروا در اردوگاه قلندیا واقع در شمال قدس اشغالی، علیه این نهاد بین‌المللی دست به لفاظی و تحریک زد.
🔹
بن‌گویر حین ورود به دفتر مدیریت این مجموعه با لحنی تحریک‌آمیز گفت اینجا پیش‌تر مدیر آژانس آنروا می‌نشست و حالا من جای او نشسته‌ام.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/684240" target="_blank">📅 17:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684239">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
نیروی زمینی سپاه: ‌اجازه تحرک زمینی به دشمن ‌نمی‌دهیم
فرمانده قرارگاه حمزه سیدالشهدا(ع) نیروی زمینی سپاه:
🔹
دشمن در جنگ تحمیلی سوم تلاش کرد با ایجاد شکاف و نفوذ در میان مردم، شرایط را به سود خود تغییر دهد.
🔹
ایجاد ناامنی، کشاندن مردم به خیابان‌ها، نارضایتی و فراهم کردن زمینه نفوذ از چند جبهه، از جمله اهداف دشمن در این تحرکات بود.
🔹
دشمن همچنین تلاش کرد با ایجاد اختلاف میان اقوام و مذاهب، از جمله میان شیعه و سنی و کرد و ترک، انسجام اجتماعی را هدف قرار دهد‌.
🔹
آذربایجان‌غربی و کردستان از جمله مناطقی بودند که دشمن روی آنها حساب ویژه‌ای باز کرده بود و تصور می‌کرد ‌می‌تواند از محور شمال‌غرب تهاجم خود را علیه ‌ایران آغاز کند.
🔹
ارتش، سپاه، بسیج، فراجا، مرزبانی و نیروهای امنیتی با هوشیاری و آمادگی کامل در میدان حضور داشتند و اجازه نفوذ و تحرک زمینی دشمن را ندادند.
🔹
نیروهای مسلح با جدیت و تمام توان آماده دفاع از کشورند و با آمادگی کامل در میدان حضور دارند تا اجازه هیچ‌گونه تحرک و تعرضی را به دشمن ندهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/684239" target="_blank">📅 17:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684238">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d98341d4a.mp4?token=mfdPd5PWL4tJodqukdNgC7cyjmwxWIe4-Fl372W8WoGbMTEW1RJW30lrPdr3nUUGIRZKaTmxPV7Paw5SzV83kYcmKGeoRwznwXhx3GGr3WSI4KRPdS-14trkyf4fczBOAN3Lz0MKuEAibgEjh6S-lUiZPKzKDkMX48Uq4MWURBvYCQLFXareQ6cI-AMulHz8BKVrp5uUMD_X63OZxb2O8ueEsnf2lDbWmNM4jRbQ-L6uVcl3wh4Yc3i1zY7ummBpGmf-KwHDrO3lcV3qTW1WyBih19aisBQI-wM2on4hDc42pvv15KX2T0o5oVwawOFrjIE1Q62CIhqtb1qNSN_hMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d98341d4a.mp4?token=mfdPd5PWL4tJodqukdNgC7cyjmwxWIe4-Fl372W8WoGbMTEW1RJW30lrPdr3nUUGIRZKaTmxPV7Paw5SzV83kYcmKGeoRwznwXhx3GGr3WSI4KRPdS-14trkyf4fczBOAN3Lz0MKuEAibgEjh6S-lUiZPKzKDkMX48Uq4MWURBvYCQLFXareQ6cI-AMulHz8BKVrp5uUMD_X63OZxb2O8ueEsnf2lDbWmNM4jRbQ-L6uVcl3wh4Yc3i1zY7ummBpGmf-KwHDrO3lcV3qTW1WyBih19aisBQI-wM2on4hDc42pvv15KX2T0o5oVwawOFrjIE1Q62CIhqtb1qNSN_hMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طول یک روز در هر سیاره چقدر است؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/684238" target="_blank">📅 17:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684237">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6031ce11b7.mp4?token=EgtLuRCPZpAzzfxsVizW1u0xTnJ1K8eTnN5g1Aa3Y1uvFEEjliEmwDz7zFI9VWme4VfZzD2p1R_7jzI2YEV7fiCC1AoTnRAWEWEZsjXJ97nIdgMavN2AU3z0nw9TNSoTbfRqFuJJqhmjs6xP2NhnBfdfaHLdhCOg64nFofCVVlvbzOUpJwYSWvVgZd6TI8NcqJFVGLRpH7MFXhyP06OsCal0jLJ0x0Blg7-JMNHPdKJJYMkaz9agA5Td3EfCU41aOtivIVNwx7S_0jGRM8yJYglgtjO-NPvUFWHPjV8BCtHeotfAIxUNx7EMaXykmBF9HS75jFavr1ERWvDp9gmPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6031ce11b7.mp4?token=EgtLuRCPZpAzzfxsVizW1u0xTnJ1K8eTnN5g1Aa3Y1uvFEEjliEmwDz7zFI9VWme4VfZzD2p1R_7jzI2YEV7fiCC1AoTnRAWEWEZsjXJ97nIdgMavN2AU3z0nw9TNSoTbfRqFuJJqhmjs6xP2NhnBfdfaHLdhCOg64nFofCVVlvbzOUpJwYSWvVgZd6TI8NcqJFVGLRpH7MFXhyP06OsCal0jLJ0x0Blg7-JMNHPdKJJYMkaz9agA5Td3EfCU41aOtivIVNwx7S_0jGRM8yJYglgtjO-NPvUFWHPjV8BCtHeotfAIxUNx7EMaXykmBF9HS75jFavr1ERWvDp9gmPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تندباد شدید، تریلی ۱۸ چرخ را در لوئیزیانا واژگون کرد
🔹
وزش بادهای سهمگین در ایالت لوئیزیانای آمریکا، منجر به واژگونی یک دستگاه کامیون ۱۸ چرخ در یکی از بزرگراه‌های این ایالت شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/684237" target="_blank">📅 17:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684236">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
نیکزاد: قیمت بنزین افزایش نمی‌یابد
نایب رئیس مجلس:
🔹
مقرر شد سهمیه ۶۰ لیتر با نرخ ۱۵۰۰ تومان محفوظ بماند، سهمیه ۷۰ لیتر با نرخ ۳ هزار تومان به ۵۰ لیتر کاهش پیدا کند و سهمیه ۳۰ لیتر با نرخ ۵ هزار تومان نیز به ۱۵ لیتر برسد.
🔹
نباید برخی افراد بدون هماهنگی، نرخ‌های بنزین ۷۰، ۸۰ یا ۸۵ هزار تومان را مطرح کنند
🔹
نباید با اعلام نرخ‌های جدید با اعصاب مردم بازی کرد/ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/684236" target="_blank">📅 17:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684232">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تسنیم: مواضع و شروط ایران درباره تنگه هرمز به طور شفاف به واسطه پاکستانی اعلام شد
یک منبع نزدیک به تیم مذاکره‌کننده ایرانی:
🔹
برخلاف آنچه بعضی رسانه‌ها گفته‌اند عاصم منیر، فرمانده ارتش پاکستان که روز گذشته به ایران سفر کرده بود حامل پیام تهدید یا پیام مشابه از ناحیه آمریکا نبود
بلکه به دنبال باز کردن فضای مذاکرات بود و به دنبال این بود که شروط و مواضع ایران را به طرف آمریکایی منتقل کند.
🔹
در دیدارهای صورت گرفته با آقای منیر، مواضع ایران به صورت شفاف به طرف پاکستانی اعلام شد.
🔹
بازگشت آمریکا به تفاهمنامه اسلام آباد و اجرای مفاد آن که شامل بند ۵ یعنی ترتیبات ایرانی بر تنگه هرمز می‌شود، جزو شروط ایران است و این موضوع به واسطه پاکستانی اعلام شد و طرف پاکستانی به دنبال انتقال آنها به طرف آمریکایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/684232" target="_blank">📅 16:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684230">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682ca1fe88.mp4?token=ZzW5JVrMtURj2DAP0v8lanWOGdwuyc_zvCagAdwJp2cTshox3mXSE20crWXeQf8GsrxGIq-dzdpHlCbbzJxdthcohR4rdnn3jYL7mOyJtZHViTGaBWq5s-Hh--nfJhYgmsN3ABZC-epx3VwRnzvX7TTYOo78bNVstE1XryfNuDftMY2rTS-NBNfsuCX8etyxFx4erXCLC6Ajk32ga914Vd_tj-WQcrot-UgSh244BXQs-rhYlns6va4sxOC5TZuGvGdx38T03jdwDqFrLym6Npo8jSL2xxiL-m2UVpBZPmnCMVoA8UkSYjtOuPojk-goI-4PEmF_6QNxvQ9e3TqSdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682ca1fe88.mp4?token=ZzW5JVrMtURj2DAP0v8lanWOGdwuyc_zvCagAdwJp2cTshox3mXSE20crWXeQf8GsrxGIq-dzdpHlCbbzJxdthcohR4rdnn3jYL7mOyJtZHViTGaBWq5s-Hh--nfJhYgmsN3ABZC-epx3VwRnzvX7TTYOo78bNVstE1XryfNuDftMY2rTS-NBNfsuCX8etyxFx4erXCLC6Ajk32ga914Vd_tj-WQcrot-UgSh244BXQs-rhYlns6va4sxOC5TZuGvGdx38T03jdwDqFrLym6Npo8jSL2xxiL-m2UVpBZPmnCMVoA8UkSYjtOuPojk-goI-4PEmF_6QNxvQ9e3TqSdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
از هزینه‌های زندگی تا نگرانی از آینده؛ بازتاب تجربه‌ها و روایت‌های شنیدنی شما از موانع ازدواج.
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/684230" target="_blank">📅 16:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684229">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-b2TcP-8KTeHOvGh2Jve6ObLw0Xj26EZmwRNZtsH9qjWmg3gzManh3FC6Ri2YIpvFtmennR7a7o0k8FYBpzlAHD5oj1DgQAbytEhhtBTMgT51WrwAlyfJz9xSFn1wu0jjZqzoMmgCXX05sO1GOgUj_oSkFCyQ04sZC7h4F7JWTO-VjtQ_da73pH0KyzZWHmLJPlFit2W33C-SrgeiLXUqHg_mkGujxOZXprf0SLVXTRe8hZjytFFgv2LDnVoh8wHUl0QC6riLoSRUhJlmyRBNdz3RtYDm8v6shOl3aWQwMpLl2FaB-UBj1GZcSuYbQLUEq3ZcSnYe-vVBT9X43TeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استیو هانکه: آمریکا کنترل تنگه هرمز را در دست ندارد
استیو هانکه، اقتصاددان آمریکایی:
🔹
سال گذشته، ۷۴ نفتکش در ۲۲ آگوست از تنگه هرمز عبور کردند. امسال، ۵ نفتکش در ۲۲ آگوست از تنگه هرمز عبور کردند. ترامپ دارد مردم را فریب می‌دهد و حرف‌های بی‌اساس می‌زند. آمریکا تنگه را کنترل نمی‌کند. ایران کنترل می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/684229" target="_blank">📅 16:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684228">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bcf58e60a0.mp4?token=CzkgrzhUAUGO0MbCKRr-qe7NNwwL19YSmOiS4gjYy1RjMN_wOEPDR28FkbumHW7O1B8C5unfvXCP_mObbRR_w3pE1bhQO1RpJ9q_H1R-yfwVceaHt0EUCHcFLZqN1ewW1cN5Hdqe2N-zh7tjCEOhyh5IcGMDqFDPnp3MrH9sZ7A8ijPQQoM4AJK-C5xcmwbaEuY25-EkFWsPpGyELWMSK33DLmRIIkg94C20juB9W84MjOZHrbLIOr0vbXmNo3JuyfxCL-0xffynFn7ega_HUCmSA_Ay-Cr1anrl9_6nMW84o3dWd-dPPa4a8ye45_UHcSnw0pbxFywT6GXnz0JSqmD_FK9uZ65fxS6_VKrq7jij71yMiLPLft6uIDvykjK40eOKHYojMs5sWFaAbPR3idq8g2NnLkp6Q1XsWzXskD78z8uwVaqnmbGm_6MHW0_w8aaN3itwEH-_HkFa-ceqElcqlchUexFtiiEOYMdhdM5LDaq8OmW7fFJPY-nGx6C6azJID8AOlqFb3-KXHUS0l3LKTV0EUhJSFizHqXm0s9e22R_Gi4foq4Vu36jcEPCgV7fa1-HekN2-uNubMmoE1G6b1HcxbW4FICWhPcFd0vyMopWK4VXBThm677W7UNgGL-axbowRXmDBJaSA3_7JMV7LBJSFq8GT7fEKkvbgWUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bcf58e60a0.mp4?token=CzkgrzhUAUGO0MbCKRr-qe7NNwwL19YSmOiS4gjYy1RjMN_wOEPDR28FkbumHW7O1B8C5unfvXCP_mObbRR_w3pE1bhQO1RpJ9q_H1R-yfwVceaHt0EUCHcFLZqN1ewW1cN5Hdqe2N-zh7tjCEOhyh5IcGMDqFDPnp3MrH9sZ7A8ijPQQoM4AJK-C5xcmwbaEuY25-EkFWsPpGyELWMSK33DLmRIIkg94C20juB9W84MjOZHrbLIOr0vbXmNo3JuyfxCL-0xffynFn7ega_HUCmSA_Ay-Cr1anrl9_6nMW84o3dWd-dPPa4a8ye45_UHcSnw0pbxFywT6GXnz0JSqmD_FK9uZ65fxS6_VKrq7jij71yMiLPLft6uIDvykjK40eOKHYojMs5sWFaAbPR3idq8g2NnLkp6Q1XsWzXskD78z8uwVaqnmbGm_6MHW0_w8aaN3itwEH-_HkFa-ceqElcqlchUexFtiiEOYMdhdM5LDaq8OmW7fFJPY-nGx6C6azJID8AOlqFb3-KXHUS0l3LKTV0EUhJSFizHqXm0s9e22R_Gi4foq4Vu36jcEPCgV7fa1-HekN2-uNubMmoE1G6b1HcxbW4FICWhPcFd0vyMopWK4VXBThm677W7UNgGL-axbowRXmDBJaSA3_7JMV7LBJSFq8GT7fEKkvbgWUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکار بزرگ در پایتخت/ گزارش خبرفوری از سرنوشت تلخ گردانندگان بازار سیاه اموال مسروقه
🔹
امروز در مرکز پلیس آگاهی تهران، پرده از نقابِ یک شبکه بزرگ از سارقان و خریدارانِ اموالِ مسروقه کنار رفت.
🔹
پلیس آگاهی با یک عملیاتِ برق‌آسا، زنجیره‌ای از جنایتکارانی را که با کالاهای مسروقه، آرامشِ خانه‌ها را از بین می‌بردند، به بند کشید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/684228" target="_blank">📅 16:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684226">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f2484b4d.mp4?token=CoMVnqhqMr_bhQNqBoGVTNZdkscwCS9c1XK6Gqea2Ld7BhkDTRw8uKqrPWdXBbKis1fgWyoldyirF9H9mrqipm5OIz4aNpBkpWY4nhzA9Ivw4MgFIgzTN44TpSuSJScikehCwtHpy5irtHlgGVVzZrJUVeh_Y8-EbjIB09CM013i8P7a5dQnxg0m1KK-PGPbbS5LD8fa21S-Vbvrv7kEqZlixbYM6bEyABHvCAqkRlXIeU8-sdHiYk2emv0jJQnblMIc41H5ZevUi1XIQoJi3jjRCVCSH13xw2Fu-5hGgIlK9HFhkm1JRFlFZUpNSu91jjvP60k2u66tk_IwR0RuCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f2484b4d.mp4?token=CoMVnqhqMr_bhQNqBoGVTNZdkscwCS9c1XK6Gqea2Ld7BhkDTRw8uKqrPWdXBbKis1fgWyoldyirF9H9mrqipm5OIz4aNpBkpWY4nhzA9Ivw4MgFIgzTN44TpSuSJScikehCwtHpy5irtHlgGVVzZrJUVeh_Y8-EbjIB09CM013i8P7a5dQnxg0m1KK-PGPbbS5LD8fa21S-Vbvrv7kEqZlixbYM6bEyABHvCAqkRlXIeU8-sdHiYk2emv0jJQnblMIc41H5ZevUi1XIQoJi3jjRCVCSH13xw2Fu-5hGgIlK9HFhkm1JRFlFZUpNSu91jjvP60k2u66tk_IwR0RuCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن باشکوه یمنی‌ها به مناسبت میلاد پیامبر اسلام (ص)
🔹
میدان السبعین صنعاء امروز شاهد سیل جمعیت به مناسبت میلاد پیامبر اکرم اسلام (ص)-به روایت اهل سنت- بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/684226" target="_blank">📅 16:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ایندیپندنت: پدر ملوان ناو هواپیمابر آمریکا در بازداشت دولت ترامپ
🔹
در حالی که جاشوا آویلس، ملوان ناو هواپیمابر آبراهام لینکلن، بیش از ۹ ماه در خاورمیانه برای ارتش آمریکا خدمت می‌کند، پدر نیکاراگوئه‌ای‌اش در فلوریدا توسط گشت مرزی بازداشت و روانه بازداشتگاه…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/684225" target="_blank">📅 16:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
آماده‌باش سرویس مخفی آمریکا برای حفاظت از پسر ترامپ
ادعای سی‌ان‌ان:
🔹
پس از پخش ویدئویی از تلویزیون ایران با عنوان «بارون ترامپ را کجا خواهیم کشت؟»، سرویس مخفی در حالت آماده‌باش کامل قرار گرفت.
🔹
این ویدئو حاوی ادعاهایی درباره نظارت بر دانشگاه بارون ترامپ، وسایل نقلیه همراهان او و مکان‌های استقرار پرسنل امنیتی مسئول حفاظت از او است.
🔹
سخنگوی سرویس مخفی به سی‌ان‌ان گفت: «ما از این ویدئو مطلع هستیم و در حال بررسی محتوای آن هستیم.»/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/684224" target="_blank">📅 16:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684223">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd86e0708b.mp4?token=cR0nzUKPrdsIxOpRqOEfggE5wbROKWxdyReYhmnRb5noZyRHa-IFsGjKB9wqF7WJDIoLJOs-Er6zL0O0ULcwN4vupp1cX7CabqJ2fPST3c7Zw6OiQ6XU-vKDxTQpUG98-pj8GDI_0fbXjDABkcBf7AON7V3kY4DO3Vb77678RmFff6QdmUc2aLeh1LHlDgzIYSsZ7TXQbKp9nDJS_FhhVtK_83My0_Ui01zvCNPrejZ9PAtY2cy76A6ZltZljnCQhnSd-sBt9on5qBRQdWxzR9q6X2yRNQmSC_SHjNKciKphwMtfFB4zQXk9MoB60G_ZoPuOhox9MwvmQW4U4VRwc4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd86e0708b.mp4?token=cR0nzUKPrdsIxOpRqOEfggE5wbROKWxdyReYhmnRb5noZyRHa-IFsGjKB9wqF7WJDIoLJOs-Er6zL0O0ULcwN4vupp1cX7CabqJ2fPST3c7Zw6OiQ6XU-vKDxTQpUG98-pj8GDI_0fbXjDABkcBf7AON7V3kY4DO3Vb77678RmFff6QdmUc2aLeh1LHlDgzIYSsZ7TXQbKp9nDJS_FhhVtK_83My0_Ui01zvCNPrejZ9PAtY2cy76A6ZltZljnCQhnSd-sBt9on5qBRQdWxzR9q6X2yRNQmSC_SHjNKciKphwMtfFB4zQXk9MoB60G_ZoPuOhox9MwvmQW4U4VRwc4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سواد مالی و مدیریت پول مادران در خانواده از چیزی که فکرشم می‌کنید مهم‌تره
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/684223" target="_blank">📅 16:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684222">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سی‌ان‌ان: فشار ترامپ همزمان علیه ایران و کانادا به بن‌بست خورده است
استفان کولینسون، تحلیلگر سی‌ان‌ان:
🔹
ایران پس از شش ماه جنگ همچنان مقاومت کرده و کانادا نیز در برابر فشارهای اقتصادی واشنگتن ایستاده است.
🔹
به گفته او، مشکل ترامپ این است که فشار آمریکا می‌تواند همان‌قدر که به طرف مقابل آسیب می‌زند، برای خود واشنگتن نیز هزینه ایجاد کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/684222" target="_blank">📅 15:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnrDbjQTdtd3dxRzZ8q8LuEMa2sjAHKw6R56MEz5uVgH9ZGvVafQUAbz663VZaVr9jooI0YCunvEOkVn3mBSCTf171bA1tTOFEPF8elqPvI50MgI8DIm4KFC3j04I9wQhgkvJuVZziw8Bu1N8_yHuFRb6g7ETBmpLPRkgvlQzfTsU9Pru4__psx9TAf9Qx9-SIB-hqKozEqs6jNte_8ZCfTnm4NgZ0sXbeJqNJagRikBjcELU_wHpXOQKhRayyd1dftbWOx9yhWcjqDD9pu-XGRdCEykQ11I4TLDgw_ZAOQyAIryaFTWFRTrsDcSH611OUgr7eCd-35QpyhhV9_C_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ کاری که ممکنه باتری گوشیت رو نابود کنه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/684220" target="_blank">📅 15:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684219">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5w6WHICnO3ZIdSA0kKPcdh7-SFHPR9PXQ8qnKjNRMPc368CLL5hvzR-gsHSbmEoNB8cezl3P4LT7x0NpWjC9G2G_eFDjTnb_kUoBcCU24CYBcf2gsrRmYoHWgkjPogzWpgeilZcvKW6FK1lXIkNWxHcyuH6jmPtwwTKYuE8reJqt6gsnSp3ySBRjSe2cmaDJZ6ee33fsJglk6HTPIzqimJQ41U_Yc2WV5bsK3PTnBziC7zoXAkSljaM7OXb0_W2q-iY7okavXuCCQcQ8e8_P1llbQFrGxUx8u-TNP9fjL3rXkzhnLY64qVzj0MWzZRPBBxtAprg9KA2_IG6iJ5QCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگ‌ترین عرضه تویوتا توسط هماتلکام در ۴۸ ساعت به پایان رسید
🔹
عرضه ۷ مدل از خودروهای تویوتا توسط هماتلکام با استقبال گسترده بازار همراه شد و در کمتر از ۴۸ ساعت به پایان رسید. این خودروها در سه کلاس سدان، کراس‌اوور و SUV و در سطوح قیمتی مختلف عرضه شدند.
🔹
در جریان این عرضه، بیش از ۴ میلیون بازدید از محتواهای مرتبط و صفحات فروش ثبت شد و بیش از ۲۳۰۰ تماس با کال‌سنتر هماتلکام انجام گرفت. همچنین اختلال کوتاه‌مدت سایت در زمان اوج استقبال، در سریع‌ترین زمان برطرف و برای کاربران اطلاع‌رسانی شد.
🔹
هیوا میرزایی، معاون بازاریابی و روابط عمومی هماتلکام، این استقبال را نشانه افزایش تقاضا برای خودروهای تویوتا دانست و از توسعه سبد محصولات و اضافه‌شدن برندهای جدید خبر داد. هماتلکام همچنین تأکید کرده عرضه خودروها تنها در صورت موجود بودن خودرو در ایران انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/684219" target="_blank">📅 15:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684218">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jviRSZaR3VmgeluuCiYS4zb_T0N5gqAzvCbQV2rCkK9K8-yxS_OV78LQQkYpptV-O0jPPHKcAiJy2vgL5JcD5P_RXYvk1lcyoVkwLEUHElZh7HkKbRtMW3CQ4KXmzPFiP0V1EgrXTaqX9uWMlsl6MY5N2T-cKCDgMqhIUW2jGIBwedMqbt1K79A-yNowWv2hcxOHBWNGSwmDR8K913lbsCJfmNZSuFRa0JFud0v5LA2kMHmlmlo8_POggRw26T5sYUmp5CAW3xZPmQ4962S4K867P-qV65ODuHqS05rv7t4BPRVS0S6E_4X9b75m3U6ZtoaF0zeWC8ta_AL8Q0JCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت کاهشی شد و به ۸۹ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/684218" target="_blank">📅 15:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684217">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قطر: تلاش‌های ما برای بازگشت ایران و آمریکا به مذاکرات، ادامه دارد.
🔹
عراقچی با همتای عمانی خود در تهران دیدار و گفتگو کرد.
🔹
وزیر امور خارجه سابق آمریکا: نتانیاهو نه فقط در آمریکا، بلکه در سراسر جهان به اسرائیل آسیب زده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/684217" target="_blank">📅 15:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684216">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e9fc883c9.mp4?token=hInm5-yeHjEpKeW2VYhcZSBFCU60KSxIlKfJLHsTLtudGitbkBlyQp5BD1FNiKvrRQEhN6H2BJrtO6cqn3y_QpoZDfKMwMO8RvsbRTkLFiIlwwj1DrSbkc7cs4T4Ic7o0HvxwcbrtAU3HsyncRypBZWfzeo8ysvyWPuIG2fEc3FG5CNgueVfITg4ldRAC6h5BZbbtNCiPtZzPmkj_Xax1SvEKpR8-9VGDSexco2T711dxjvYanrVdmfzy7ubWfZ1mC2E6tFs0oFhehNPZEWBm4ssHS4qDISjNpjbGzbForf6L53YTuT3-Oqve5W3ot4sqMZ3bQGRZwXZvNZkRSSvyAcLpJTeB4I7YC3J4vyDeoxrkxIoydHWCyck5qixNtG1-20TBseKLk28S-DgC86UEooIOuFto-aUXaNTLXocGFnMa-uAciXTcLilu2VGVSuJ06CtCybaHz34SNlSCcwMe9dj0Nv4hsTXrdXTjzN-GdLbFFv4r0LtBRF0kMOlU1X55CLGOVpuyGxRwSN35M91qGdGZc_4DmlDkM9ZLCp4UzKn4XhNJZMsnVwFw1f3fBwY_-Bq2OC8Plqb_2VQF_GzHXcCzcjbIMwQlpZLHRNGfUZAZyLGAHjWaYt5LYajdLv1JxMMfw8j0fd_faNkzt97RjNlQNeiinRRCQN82Vc3Dek" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e9fc883c9.mp4?token=hInm5-yeHjEpKeW2VYhcZSBFCU60KSxIlKfJLHsTLtudGitbkBlyQp5BD1FNiKvrRQEhN6H2BJrtO6cqn3y_QpoZDfKMwMO8RvsbRTkLFiIlwwj1DrSbkc7cs4T4Ic7o0HvxwcbrtAU3HsyncRypBZWfzeo8ysvyWPuIG2fEc3FG5CNgueVfITg4ldRAC6h5BZbbtNCiPtZzPmkj_Xax1SvEKpR8-9VGDSexco2T711dxjvYanrVdmfzy7ubWfZ1mC2E6tFs0oFhehNPZEWBm4ssHS4qDISjNpjbGzbForf6L53YTuT3-Oqve5W3ot4sqMZ3bQGRZwXZvNZkRSSvyAcLpJTeB4I7YC3J4vyDeoxrkxIoydHWCyck5qixNtG1-20TBseKLk28S-DgC86UEooIOuFto-aUXaNTLXocGFnMa-uAciXTcLilu2VGVSuJ06CtCybaHz34SNlSCcwMe9dj0Nv4hsTXrdXTjzN-GdLbFFv4r0LtBRF0kMOlU1X55CLGOVpuyGxRwSN35M91qGdGZc_4DmlDkM9ZLCp4UzKn4XhNJZMsnVwFw1f3fBwY_-Bq2OC8Plqb_2VQF_GzHXcCzcjbIMwQlpZLHRNGfUZAZyLGAHjWaYt5LYajdLv1JxMMfw8j0fd_faNkzt97RjNlQNeiinRRCQN82Vc3Dek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراقب باشید! آن‌ها با «قانون» به شما حمله می‌کنند!
🔹
آنچه امروز پلیس آگاهی از آن پرده برداشت، یک کلاهبرداری ساده نبود؛ بلکه یک «جنگ روانی و حقوقی» بود!
🔹
اعضای این باند، با لباسی از جنسِ قراردادهای رسمی، به دنبال خودرو نبودند؛ آن‌ها به دنبال «خونِ پس‌انداز» مردم بودند!
🔹
ترفند آن‌ها ترسناک است: آن‌ها با تظاهر به مشتری بودن، شما را در تله‌ی قراردادهای «حق فسخ» گرفتار می‌کنند؛ جایی که شما با امضای یک کاغذ، در واقع دارید اجازه می‌دهید جیب‌تان را تا آخرین ریال تخلیه کنند!
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/684216" target="_blank">📅 15:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684212">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q45kwsRgofpKZs3k-ixUtxwEhCW9vjryPB4aWhhPEX9lHmmza939uGEW7EvUEl3JlOCOA07su0GwSx-9IeqTwj_rFayM_m4kD3cBHatNnEQWNoCmhFc8l4PaOrrnijb4rfxzyaONaBadmMITzNXxYm4G7HkGMsQd4XoPjd4kZUEoKOuObFJFEoPjVg_pTMJ3mxl4GQ2XJgakOggBYd44wfmVcFS5BVmqzQ7tDzO4TEhtLbqZV_uuIWin_-w1n0l3mPHSZKssTSGzqA6xq65E62btbdet34XrJe49aUIMWApktM_886DrV9IbOXloUJPEEJqAiSCYh7K7N1gtlGalQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XL5mQhIC7nlOgGP6It6afKwHGf5Q57kOYPZdQU3bE5CH_unQ8r8VlI_fnzkkVYcyEQFV3IPw-8f91nmGd33YFoPfq4fOLjHWX3ptKb5Br5WfZb5waboRyaFmBl9ntkU4yTCj8ImIgtHeZEeuDwRAhAZ5Tly0l-ZkL9crw8Qqog7dc3wPw2hwBiEbBWL8Q_ZYipkVLdZJOy41ce91UF1nD37Vgm1nOb0cvDjK8qQGaxTeYp6nBfK3UP21RIPYMIqPfpqqIDo2yKEUOzdj_sX9EWt1D2TpeRznrFEJpuRz8f1xW4lw6mdxL82uHJX83OsEdGi-C3Zh9JHpLxSGXDRLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjZ4p9Q3T5TcB9cPwMKQikxyBuyxRZyGS8-d0mOPLEJnoKs3P85N5ksk_VkwDU3aY5MhADX3rOW50zHfGs_AdH9EhtDTOkwuOp1Q-ui5Th_wyFAemC__4Xv_1JUpknie4exMKTNfGfzUzyuhxMt5jg-bp0moeP6bSmxWLuM_x0A2u5qV-WhoohnJ3MD23aQ2K3PVP33ZCGhkA4goD1yuQ6M9WlDc5XMpbnlTa36FNjXmFlJB4lHDkL7Jhbj0pcVEAsA7l-tXugZQwgT5G962zMuJBZWToJn174zlj56d3zd-IMSKfs1JwgBQg8MVXhydqv7GUGoC3bRh1Ln72eLxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsXW7cgUVvktP475A1m5Qv8uzGmbJSb--0YvvXIVkhnKvgXToWRdSu4Jzr-pW2bu9nffslrpS5P7rQWO1j524VPtUmQnpVCKpFaIpS_k2BiCSGzDvFJ90wBBXKWxP5yUG4Vw8V3fDP2kSTO_VbCov90OuhKZAFTWdfcFpBd1ZFwrQ9bOiD24HpjoEPCgOlRbCeewa2hmLAqW5Bz-RKzwdDQtuOMYxF_Vxq-SkzBqXWlEZc2cTmN3puvHPTsWjXrMjFAYBDqcQw7bH-WKKoD6VmdeUEeFmcvYR84M0lP7JhSNIA_rTmfu0x9_fIgap5bvtg9a-IyujON-COrLtwELDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استفاده از گوش‌پاک‌کن بیشتر از این که بهداشتی باشه به سلامت گوش‌مون آسیب می‌زنه #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/684212" target="_blank">📅 15:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684211">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3X0qHFAC88rbXSXQOg6dI9Ro9y0dYTVYVTbIVlfA1d9hiiI-0HReMV8d8gNMHNm54Xa8QfcYRipUNqxF-ioDFVsy_WfWEv3pUaAQ8pkIcC9BKzOak3kFbdAV4Zwi88-Onqo5bmWM4Vs6QxWlm5-039TXPNCaXokBN_sMwlh0WfE8lf0Krxo982XNi27vZ-AjgZsyxDg5U9wDc8wvmp417bB2SG5ZQdv0JtUq5NgMCeEEB9sUL7SiBtYNKM3EfAkqGnvRrI37KzEYxCLeSB5m6iHs5JMLoKeR4w2_C-LFLO0XaSPOcQvebYictTInYhxak_LlPe0HavLsj54l90asw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از ظرفیت‌های علمی تا حکمرانی نوین؛ مأموریت معاون علمی در کرمانشاه
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور در جریان سفر به کرمانشاه، از پارک علم و فناوری استان و شرکت‌های دانش‌بنیان مستقر در برج فناوری بازدید کرد.
🔹
حسین افشین در این بازدید ضمن آشنایی با ظرفیت‌ها و توانمندی‌های شرکت‌های فناور، در جریان مسائل، فرصت‌ها و قابلیت‌های موجود در زیست‌بوم علم و فناوری استان قرار گرفت.
🔹
شناسایی ظرفیت‌های علمی و فناورانه کرمانشاه، تقویت ارتباط میان بازیگران زیست‌بوم نوآوری، حمایت از شرکت‌های دانش‌بنیان و ایجاد زمینه برای نقش‌آفرینی مؤثرتر ظرفیت‌های بومی در اقتصاد دانش‌بنیان، از اهداف این سفر است.
🔹
این برنامه همزمان با هفته دولت و در چارچوب رویکرد معاونت علمی برای توسعه زیست‌بوم نوآوری و حرکت به سمت معماری نوین حکمرانی علم و فناوری در کشور دنبال می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/684211" target="_blank">📅 15:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684210">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz1gwEyuyrXP1AB0qozsq2Pvn2gwnl7gxHdrrM2ehDeKrlzlrgwq4ju4-67y9kqQYlAEGDQQET-RTXu_MZ5Yc4fusi_cbTXAmMzz02IZ3OLYvGviiI2kZzwtgD3a-BUoR4c4_19fFwYqv49wLE9z-eR7yHg5AaoZv9BbM0X2PTJ0V_rCGeBD5AFQhYnocQlkWFcwnaHP-iU9WBPzaTr9K5wtSQuptpygXXXAWZei2-IUoVsiuz9-9OkEEAei_sgvGbAHw5Ip3uTIZ6ckvAlft2WLmFmCe5pEnbpfl56SWDPmwRx8GrR2Erdt7-H9tJRUAFA1jsOFkTkTkQZpLqV1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
واگذاری سهام «سیمان تجارت مهریز» در فرابورس
⬅️
نشست خبری معرفی سهام شرکت «گروه صنعتی و معدنی سیمان تجارت مهریز» با نماد «سمهریز»، با حضور مدیران شرکت و خبرنگاران بازار سرمایه در فرابورس ایران برگزار شد. این شرکت در راستای سیاست‌های دولت در زمینه واگذاری بنگاه‌ها، توسعه نقش بازار سرمایه و مولدسازی دارایی‌ها، در فرابورس ایران عرضه خواهد شد.
⬅️
مدیرعامل شرکت با اشاره به ترکیب سهامداران، برنقش کلیدی بانک تجارت به‌عنوان سهامدار عمده تاکید کرد.
🔗
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/684210" target="_blank">📅 14:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684209">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ترامپ دوباره توهم زد؛ ایران حقوق نظامیانش را نمی‌دهد
رئیس دولت تروریستی آمریکا:
🔹
ایران حقوق بخش عمده‌ای از ارتش خود را نمی‌دهد؛ وی مدعی شد که ایران دچار یک بحران انسانی است که باید متوقف شود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/684209" target="_blank">📅 14:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684208">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
جزئیات نسخه تازه مصوبه مجلس
🔹
بر اساس ماده‌ی ۱۵، همه‌ی اشخاص حقیقی و حقوقی ۳ ماه فرصت دارند تا فعالیت‌ها، قراردادها و ارتباطات جاری خود با کشورهای خارجی را با سازوکار جدید تطبیق داده و در سامانه شفاف کنند.
🔹
تولید اثر هنری بدون مجوز از نهادهای قانونی کشور،…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/684208" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684207">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سارقی که گردنبند دزدی را ۱۰۰ میلیون قمار کرد
🔹
در این ویدئو روایت پیرزن مالباخته از شب حادثه و اظهارات عجیب سارق دستگیرشده  را در
#گفتگو
با خبرفوری ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/684207" target="_blank">📅 14:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684205">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUU0dI7OZ5NZ91cCc6h3G5u2YbSKJ3rArVjwXDc3xuujV9vw_qmSbFZ4u_6U9dKVvEVQPqc3-Lez2_Ermwx84vh9Az4oI535QgBfSnidzlFcvxpWbpQconpeJV44Zhs80oS-2FkyEiSI-rc7RHm1EOFS7A__DV1Q0gljLS0PL_TiQ4e82A2a30wkfY2o1xz3TsGQsdLzThTeRNw3Tykx-czawxtRk1NzoaJY1-SB59iHnWfSsYPHoxo4UwrIU4mURUxLx2KWqbwtvHw1P2VOuCOvwRTEpyn6nwTWGH7Jx8mdQ04dlhA0gfV8BsPZpNKMK3USwjyRfox7b5I-rK9cng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونس، معاون ترامپ: باید به یاد داشته باشیم که کانادا یک ایالت... ببخشید، یک لغزش فرویدی بود؛ واقعاً اشتباه لفظی بود؛ کانادا یک کشور است!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/684205" target="_blank">📅 14:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684203">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEIwhkpEl3PVzz8PGd8zs9e5Qw4SotXbL3qWGJvdRKMiZ_bPtpofuwFLzxHxbUi6HkkC5RsNQ0x7WC6SgVNtbwOVQzpn_M3Ac12CzoRpMVVmwKqNRiSf606z1JS1Dv6lEjGPPLAvjVnK1HnWNkCoyg3jerHEqJSwsOsVjBD1cttmK_hCwhdalSzgAuo2fSauGDmuhQBIe7YmMkaSEUMz1KMc3Jaz-Umcc4gvG8JeEayO-2EmZS-a3L5IdCT7XQxkX_qDER6jKHLBzOo8aefnzw9ZEA2y70wJRGmdDmdyOBqj2yuKTHNsm1WtWhGlaw3NeWd6dRviHouWul1KXdDSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاکسی‌های برقی بابک زنجانی به آبادان و خرمشهر رسید
🔹
فارغ از تمام حواشی، پرونده‌های متعدد و دیدگاه‌های متفاوتی که حول عملکرد بابک زنجانی وجود دارد، راه‌اندازی ناوگان تاکسی‌های‌برقی دات‌وان تریپ در منطقه آزاد اروند را باید یک تحول کارآمد زیرساختی برای مردم جنوب کشور قلمداد کرد.
🔹
شهروندان خرمشهر و آبادان که سال‌ها با دشواری‌های رفت‌وآمد شهری در گرمای طاقت‌فرسا و فرسودگی وسایل حمل‌ونقل دست‌وپنجه نرم کرده‌اند، اکنون فارغ از کشمکش‌های رسانه‌ای، ذینفعان اصلی یک ناوگان هوشمند و پاک هستند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/684203" target="_blank">📅 14:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684202">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین دلیل کاهش استقبال از سالن‌های سینما و تئاتر چیست؟</h4>
<ul>
<li>✓ کیفیت پایین آثار</li>
<li>✓ عدم تنوع ژانرها</li>
<li>✓ افزایش قیمت بلیت</li>
<li>✓ رونق شبکه‌های نمایش خانگی</li>
<li>✓ ضعف اطلاع‌رسانی</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/684202" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684201">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
مدیریت هدفمند عرضه ارز، بازار دلار را تعدیل کرد
🔹
بانک مرکزی با تنظیم هوشمندانه عرضه ارز و پاسخ‌گویی به نیازهای واقعی اقتصاد، روند بازار دلار را به سمت ثبات و کاهش نوسانات هدایت کرد.
🔹
این اقدام در راستای کنترل تقاضای غیرمولد، تقویت آرامش بازار و صیانت از منابع ارزی کشور انجام شده است.
🔹
تأمین ارز کالاهای اساسی، مواد اولیه تولید و نیازهای ضروری همچنان با اولویت در دستور کار بانک مرکزی قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/684201" target="_blank">📅 14:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684200">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNByrrhWdEe-JRD4s7ZhQr9C4PCsdfuFDtNr9uESDlFYXf9KOouBpSPR4qLYsAq0aWwu37RJi0trSUUU5GHsTYAKQg5JdwASEONka2lb-3KVPqAaabn9p_3jpkkn3GJjeXIy67RLmv0PmZiKOn0-ZDmDUXhvkRC75JArKanXl7tqv0YeVvPdT0ueLxqC8KG0FEJAmV1KPuXJVkrQqmCp_pLUzAmkice_Jc5Ht-fMLjK4_n3Wx9g06KEU2AlgYL3c5gYMv1UH30CNnC648p_hXROe3D3O5hZq93cahXmuVm_hybu0Hc-2ofSikA_aYISx3d58sTeZI1zz7sFl6vHMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/684200" target="_blank">📅 14:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684198">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e71e6b12e.mp4?token=QI5KuqpgJa2G9p1yTtVlzYKRXes1i5g7W2Eoe0StNYqO4YR2QXfAc7UNhI33zCfxDlHlt0tMe4C4-r5McS6rQJIZ8cFRm2u7qnWsM_4AaQPJ_7bNufnuHNjG12ItyQFhS4KbJTOulp7CTV4x6l1NlbzEA5SmmsPk0v-fkdUbhaGYKVlwZ2svbYMsHjHhjffXeWYJ0F1CLy7y0tqXul5r4PtrMhgnAqZYlUqIMFyYfIIlT-j1eA1AE1RVxpQBr73hDzmH1mJnlTJuNV9YNh9ByJKAeK0hW3kJtIOupWjnG4mVdTasH_ueU8ABESv_mJlzg0M9JQJeTYtvlnLTRT4Lpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e71e6b12e.mp4?token=QI5KuqpgJa2G9p1yTtVlzYKRXes1i5g7W2Eoe0StNYqO4YR2QXfAc7UNhI33zCfxDlHlt0tMe4C4-r5McS6rQJIZ8cFRm2u7qnWsM_4AaQPJ_7bNufnuHNjG12ItyQFhS4KbJTOulp7CTV4x6l1NlbzEA5SmmsPk0v-fkdUbhaGYKVlwZ2svbYMsHjHhjffXeWYJ0F1CLy7y0tqXul5r4PtrMhgnAqZYlUqIMFyYfIIlT-j1eA1AE1RVxpQBr73hDzmH1mJnlTJuNV9YNh9ByJKAeK0hW3kJtIOupWjnG4mVdTasH_ueU8ABESv_mJlzg0M9JQJeTYtvlnLTRT4Lpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با یک بشقاب و سوزن، مدل لباس‌های قدیمی‌ رو‌ عوض کن و لذت ببر #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/684198" target="_blank">📅 14:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684197">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: آمریکا دیپلمات‌هایش را به خاورمیانه بازمی‌گرداند
🔹
بر اساس یک سند داخلی وزارت خارجه آمریکا، بازگشت دیپلمات‌های این کشور به سفار‌تخانه‌های آن در منطقه که در جریان جنگ علیه ایران تخلیه شدند، ممکن است از همین هفته آغاز شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/684197" target="_blank">📅 14:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684196">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
سامانه امداد تجار اتاق تهران؛ همراه هوشمند کسب‌وکارها
🔺
اتاق تهران با راه‌اندازی سامانه «امداد تجار»، بستری غیرحضوری و شفاف برای ثبت، پیگیری و رفع چالش‌های کسب‌وکارها فراهم کرده است. فعالان اقتصادی می‌توانند مشکلات خود را ثبت و از حمایت‌های قانونی و بسته‌های حمایتی دولت مطلع شوند.
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
https://digitalchamber.ir/emdad</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/684196" target="_blank">📅 14:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684195">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjjVIc76rCFyJzwZWkU76a26EFuIr6kEnu8njIYSBfmCjPr0xGa1WMV8SY00WDDxz1taM4AeQ_JEej8K12WYL2cgn9RA0vtPj2PTiHkaR_ZoEmKKa1Bo2fCvn5WG55txuh0UjJU-nP1LQ027VDBa9_0FrIhHkAa7X19sD3S0_BVJcbrcIXDOw6qyQMS86EgYJQL8YJLJqlkE-qYDUuy-ZvrCUVlBiBQDaPaCBOGuVPfnCw2pePiaJewzngXJ4z3GO88Lp7pNi_MdMOPKRJRWAU3JtFR1HSnxGS4rIE61VElFWQMHB8EIyQuKZ2XmWEmBSvTyKk2UKblcXmhKiaPr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به اطلاع میرساند شرکت توسعه منابع آب و نیروی ایران قصد دارد ۵۷ دستگاه ماشین‌آلات راهسازی و سنگین خود(شامل انواع جرثقیل، تراک میکسر، کامیون، دامپتراک، بولدوزر، لودر، غلتک، بیل مکانیکی،‌ پمپ بتن هوایی، بونکر سیمان، تانکر آب، تانکر سوخت و...) را از طریق مزایده عمومی به فروش برساند.
🔹
مهلت دریافت اسناد:
1405/06/11
🔹
اطلاعات تکمیلی در سامانه ستاد به آدرس
www.setadiran.ir
بارگذاری شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/684195" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684194">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای الحدث: فرمانده ارتش پاکستان به ایران پیشنهاد توقف محاصره دریایی و لغو تحریم‌ها را بر اساس تفاهم‌نامه ارائه کرده است  الحدث به نقل از منابع آگاه:
🔹
واشنگتن در ازای توقف حملات گروه‌های نیابتی ایران، پیشنهاد توقف محاصره دریایی و لغو تحریم‌ها علیه ایران…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/684194" target="_blank">📅 13:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684192">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a712ce05a.mp4?token=bukpgLbnLEMcP5EPbCF51ADILIZ0arZ6euRZSP6QK0vAmjLV8dcRO9ratbEOShGHePu4GPM0WIUEJiyHjPskq4HbJjBtObQhiCYXyqJxlt7_A7chaiTQ2pdYJM8bDD4S7Gn_gqsO6BQUKdVTXZU2ZzRnYl8lWD-Wx3l2AdknBdvNw2ouPwwDhnyRzGmtCYS5T6zmaXJaMf2ZkwqXS6d4tIy49K--CRUCnCjOWB8o5tEd15kZRXWBQBUoLT7m3RYpJHY98_faMQdHzBQY_rGKZUUtW7oVdGmDlFMqX15VWZFoLjmfZ9Np9C3GHWqyrC-WOYWhyYef_3QfLJjF0vvisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a712ce05a.mp4?token=bukpgLbnLEMcP5EPbCF51ADILIZ0arZ6euRZSP6QK0vAmjLV8dcRO9ratbEOShGHePu4GPM0WIUEJiyHjPskq4HbJjBtObQhiCYXyqJxlt7_A7chaiTQ2pdYJM8bDD4S7Gn_gqsO6BQUKdVTXZU2ZzRnYl8lWD-Wx3l2AdknBdvNw2ouPwwDhnyRzGmtCYS5T6zmaXJaMf2ZkwqXS6d4tIy49K--CRUCnCjOWB8o5tEd15kZRXWBQBUoLT7m3RYpJHY98_faMQdHzBQY_rGKZUUtW7oVdGmDlFMqX15VWZFoLjmfZ9Np9C3GHWqyrC-WOYWhyYef_3QfLJjF0vvisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا اواسط هفته آینده موبایل های کشف شده به دست مال‌باختگان می رسد
سردار عباسعلی محمدیان، فرمانده انتظامی تهران بزرگ در
#گفتگو
با خبرفوری:
🔹
ما قول می‌دهیم تا اواسط هفته آینده تمام موبایل‌هایی که کشف شده به دست مالباخته ها برسد.
🔹
وقتی میلیون‌ها تلفن همراه با قیمت بالا در اختیار مردم است و در استفاده از آن دقت نمی‌کنیم، سارق به سمت سرقت وسوسه میشود.
🔹
دوربین‌های سطح شهر می‌تواند به ما برای شناسایی سارق کمک کند.
🔹
اگر زمانی ناخواسته با سارقی مواجه شدید حداقل خوب ببینید و خوب توصیف کنید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/684192" target="_blank">📅 13:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684189">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
حالا زن در خانه چه کاره‌ است؟
🔹
زن هوا و بوی خوش خانواده است؛ یعنی حضور زن در خانه آن حضوریست که علاوه بر خودش، برای خانواده هم مهم و حیاتی‌ست و اصلا بدون این حضور، خانواده به معنای واقعی وجود نخواهد داشت.
🔹
«المَراَةُ الرَیحانَهةُ و لَیسَت بِقَهرَمانَة»…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/684189" target="_blank">📅 13:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684186">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d8c30461.mp4?token=ktwiDvQxFl2PdLNxDKs-l9E2ijO9beI5zvwXNfVO5cC_SRP0xrJfHXb11AgMKvQwjNTeXgdCYGF3QspkJYh2ZfSduYGo-tj6cajk-yiQRh2Fr1jtFkXOAYJ4yjFYSAOyJ3xLXW-dWfKCVv6p2Sv6BPhVJZU1PP1h8Vcz8tfNeWc2bzGgndLLjnIuVGjacAfIhNcxVDoOQSHYzo7aNDgMazcj0p_m7lYjc9kei8qkwhZDSWnC117DjDYTT-KHhgLBxfGtPKSzAPoXyokU9gx3_Lu0U1MjRJyVcLON8SSeM0jaeA5Mk-YXMJGEYyqnEsQ59TWz8HDn44zwTDTeHHYgOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d8c30461.mp4?token=ktwiDvQxFl2PdLNxDKs-l9E2ijO9beI5zvwXNfVO5cC_SRP0xrJfHXb11AgMKvQwjNTeXgdCYGF3QspkJYh2ZfSduYGo-tj6cajk-yiQRh2Fr1jtFkXOAYJ4yjFYSAOyJ3xLXW-dWfKCVv6p2Sv6BPhVJZU1PP1h8Vcz8tfNeWc2bzGgndLLjnIuVGjacAfIhNcxVDoOQSHYzo7aNDgMazcj0p_m7lYjc9kei8qkwhZDSWnC117DjDYTT-KHhgLBxfGtPKSzAPoXyokU9gx3_Lu0U1MjRJyVcLON8SSeM0jaeA5Mk-YXMJGEYyqnEsQ59TWz8HDn44zwTDTeHHYgOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پادشاه جنگل‌های هیرکانی
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/684186" target="_blank">📅 13:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684184">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4d927062.mp4?token=TEDktf_sWsmFyRNA-rKOAdyv6dnm-CIb-u2ZE6r_d48KGsj1ZY2v5SL0VwnnrG6MGh8Y9FDanEdYBsiny6_YBAJndk1jLjf5ncpmqXHMjcCAiD22cXjJc7fIxSvp5OoZRaP1ltRk7V5wldjYTAzPdvVQDq3rLVhwtZPZPK-k_L7oEvxrqbzB4klctkNtkFao4JHlefzId9OlMoXeSMk4UoXwZYtuS_gOWHlMPflrd7uw1x5q86WbjuI-5DqlloOn0afhCwKwZE3HDOkeY8YG_x_vMzvWVAMUx5rJ4HPLUQoXxmd6Bg6dsql5LtUjUxHSaQiriwYPorLrEt2n50pUlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4d927062.mp4?token=TEDktf_sWsmFyRNA-rKOAdyv6dnm-CIb-u2ZE6r_d48KGsj1ZY2v5SL0VwnnrG6MGh8Y9FDanEdYBsiny6_YBAJndk1jLjf5ncpmqXHMjcCAiD22cXjJc7fIxSvp5OoZRaP1ltRk7V5wldjYTAzPdvVQDq3rLVhwtZPZPK-k_L7oEvxrqbzB4klctkNtkFao4JHlefzId9OlMoXeSMk4UoXwZYtuS_gOWHlMPflrd7uw1x5q86WbjuI-5DqlloOn0afhCwKwZE3HDOkeY8YG_x_vMzvWVAMUx5rJ4HPLUQoXxmd6Bg6dsql5LtUjUxHSaQiriwYPorLrEt2n50pUlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیده‌نشده از اصابت موشک‌های سنگرشکن به ساختمان شیشه‌ای در نبرد رمضان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/684184" target="_blank">📅 13:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684183">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
هشدار پلیس فتا درباره کلاهبرداری با جعل صدای آشنایان
🔹
معاون پلیس فتا هشدار داد کلاهبرداران با کمک هوش مصنوعی می‌توانند صدای افراد آشنا را جعل کرده و با درخواست فوری پول یا اطلاعات بانکی، افراد را فریب دهند.
🔹
پلیس توصیه کرد پیش از هرگونه واریز، هویت تماس‌گیرنده را از طریق شماره‌ای که از قبل در اختیار دارید بررسی کنید و رمز، کد تأیید و اطلاعات بانکی را در اختیار کسی قرار ندهید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/684183" target="_blank">📅 13:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684181">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e70222e5.mp4?token=UOv-Sk3F2AxlUyRcamkwi_VpWQfPHDCFQ-aFl1ecCVhfQ4YBQsnDdxPD6rXuAP7SjOWSpcSF2ZS30qRhMJu4WkcaOpR2h7KakRSMNY5_DLRYNuTMxL0s53SlW_uYqJHB3fvhGlF0ewcz7AEm53XkPGu1A5UA5sL1awL1odkcTeK1o7IZMG5J1zm1Iu1pPkTtmb52RM54NWj8ZptaFX3zY-3CRGPpiKC0LrFUqrJ4PoHG_Sz_S5_6TlcPDbXmf7jBssCIh5zpjXNr1dlq7hF9OsWo1CXWV1UbumbXAVZ2asCc-OZV6lq8XKapHEqeXNPzVzqiIfTbYbtL_6sMdItLzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e70222e5.mp4?token=UOv-Sk3F2AxlUyRcamkwi_VpWQfPHDCFQ-aFl1ecCVhfQ4YBQsnDdxPD6rXuAP7SjOWSpcSF2ZS30qRhMJu4WkcaOpR2h7KakRSMNY5_DLRYNuTMxL0s53SlW_uYqJHB3fvhGlF0ewcz7AEm53XkPGu1A5UA5sL1awL1odkcTeK1o7IZMG5J1zm1Iu1pPkTtmb52RM54NWj8ZptaFX3zY-3CRGPpiKC0LrFUqrJ4PoHG_Sz_S5_6TlcPDbXmf7jBssCIh5zpjXNr1dlq7hF9OsWo1CXWV1UbumbXAVZ2asCc-OZV6lq8XKapHEqeXNPzVzqiIfTbYbtL_6sMdItLzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین: با تحریم‌های غیرقانونی آمریکا مخالفیم  سخنگوی سفارت چین در واشنگتن:
🔹
تحریم‌های یکجانبه آمریکا علیه ایران مبنایی در حقوق بین‌الملل و مجوز شورای امنیت سازمان ملل ندارد و پکن از حقوق و منافع قانونی شرکت‌های چینی حمایت خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/684181" target="_blank">📅 12:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684179">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
لحظاتی از دیدار صمیمانه سرلشکر محسن رضایی و فیلد مارشال عاصم منیر در تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/684179" target="_blank">📅 12:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684178">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOyrtkaYZHUNqgbL5wulRXE-ai9aa_pymeDDaWkD73UOIOWe5DZsTznJsoIzZcrEubjNaLbvRSVnO7nuje67E_FAvtUURUnjmPLE_yT_n-dUK5hhqC0rlA6-N22VJfaG19p421WJDrHKGlj9CvxbMdzQMuXR80wp5RSwGZbMOeYJS2SHusghQBLjAQuwGPaflO55jOhUjjNKKFgngDWHJhZlzfcExTy2TbNfC-3CY9RtnabRaPWdu-aaONt5StJ2DXadrR5pRam642eklMm7nxuAiIze19lUTWbz3JysiFhPDOJkbOb3ZXkXZJG2bybu1ZHp6qT4daIVnkeer0Xccw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/684178" target="_blank">📅 12:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684177">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_fcyk6fflA2R3EJkdbts1EjPc-PWswL1s4-qoeA149MC_XgODWEsjvQuUI-IhYiKOK2GqfU69wDBC2MYircN6IyrN7SdBv5Yen1WqYHZV2iqtR_JeXB0c3d7G5NtvBbkSPjQFdbb7jossuiviRvXEoddVlPEt3SqedUpB6pgmUAV2gV8x5yTUExMC3dddIfAdDYHKaJUf4BQmYwFDBCADiHF_j2CFB-lgfYg6XKI5jYcg-0utQIafROxb9V64BuYYF_AUWNDw9z4QjVGqxAL-p9j33qu28mvEko188R2wNTBnFL4lF8LRTIn7SOasQ-FGNzS8Fdi93YWLvFHK9aOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمهیدات جدید بانک مرکزی برای تقویت عرضه و مدیریت بازار ارز؛ تسهیل خرید اسکناس برای فعالان اقتصادی
🔹
بانک مرکزی در ادامه سیاست‌های جدید ارزی و با هدف تقویت عرضه‌ ارز، پاسخگویی به نیازهای ارزی فعالان اقتصادی و تعمیق معاملات رسمی اسکناس، تمهیدات جدیدی را برای توسعه دسترسی متقاضیان به اسکناس ارز در شبکه رسمی بانکی به اجرا می‌گذارد.
🔹
بر اساس این تصمیم، با توجه به تقویت ذخایر ارزی بانک مرکزی متعاقب اجرای سیاست‌های جدید ارزی از اواخر سال گذشته و حسب ارزیابی‌های به‌عمل‌آمده از تحولات بازار ارز، از روز سه‌شنبه مورخ ۱۴۰۵/۰۶/۰۳، کلیه اشخاص حقوقی می‌توانند با مراجعه به شعب بانک‌های عامل ملت، تجارت و صادرات، نسبت به خرید اسکناس ارز تا سقف پنج هزار (۵۰۰۰) دلار با نرخ توافقی اقدام کنند.
🔹
همچنین اشخاص حقیقی نیز می‌توانند با مراجعه به شعب بانک‌های مذکور، نسبت به خرید اسکناس ارز تا سقف هزار (۱۰۰۰) دلار اقدام کنند.
🔹
این اقدام با هدف تقویت عرضه ارز، پاسخگویی مستقیم‌تر به نیازهای ارزی فعالان اقتصادی و تعمیق معاملات در شبکه رسمی اسکناس انجام می‌شود و ظرفیت عرضه ارز از مسیر رسمی شبکه بانکی را افزایش خواهد داد.
🔹
بانک مرکزی همچنین اعلام کرده است سایر برنامه‌های مدیریت بازار ارز نیز متعاقباً اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/684177" target="_blank">📅 12:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684175">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
عرضه ۵۰۰ میلیون دلار اسکناس بانک مرکزی به شبکه بانکی؛ آمادگی برای افزایش عرضه متناسب با تقاضا
🔹
بانک مرکزی در راستای مدیریت بازار ارز و با هدف تقویت عرضه اسکناس و تسهیل دسترسی متقاضیان حقیقی و حقوقی، امروز نخستین مرحله عرضه اسکناس ارز به شبکه بانکی را آغاز می‌کند.
🔹
در این مرحله ۵۰۰ میلیون دلار اسکناس در اختیار بانک‌های متقاضی قرار می‌گیرد تا از طریق شعب منتخب و صرافی‌های بانکی به متقاضیان عرضه شود.
🔹
بانک‌های متقاضی تا ساعت ۱۳ امروز سوم شهریورماه ۱۴۰۵ فرصت دارند حجم مورد نیاز خود را برای عرضه در شعب منتخب و صرافی‌های بانکی به بانک مرکزی اعلام کنند.
🔹
بر این اساس، تمام اشخاص حقیقی و حقوقی می‌توانند با مراجعه به شعب منتخب بانک‌های عامل، نیاز خود به اسکناس ارز را از مسیر رسمی شبکه بانکی و در چارچوب سقف‌های تعیین شده، تأمین کنند.
🔹
بانک مرکزی اعلام کرده است در صورت افزایش سفارش‌های ثبت‌شده از سوی شبکه بانکی، آمادگی دارد حجم عرضه اسکناس را متناسب با میزان تقاضای ثبت‌شده افزایش دهد.
🔹
ورود ۵۰۰ میلیون دلار اسکناس به شبکه بانکی در نخستین مرحله، در حالی انجام می‌شود که بانک مرکزی بر تقویت عرضه و پاسخگویی به تقاضای واقعی بازار از مسیر رسمی تأکید دارد؛ اقدامی که می‌تواند دسترسی متقاضیان به ارز را افزایش داده و از شکل‌گیری تقاضای هیجانی و نرخ‌های غیرواقعی در بازار جلوگیری کند.
🔹
بانک مرکزی همچنین اعلام کرده است این عرضه محدود به رقم ۵۰۰ میلیون دلار نخواهد بود و در صورت نیاز شبکه بانکی، امکان افزایش حجم فروش وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/684175" target="_blank">📅 12:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684174">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4awvj_M8qPDhER1BHbXoauzvRio2HU86LJON5pWOuHBBSNPU9IaZ3D4xZXaUYVaFxK6MtmVOiVvop0TyMUsGirPwvZngg4Pbctr6_bxKoFJmasPcw4aWCrdq2D9OHY747nm3Z8XkdtYfqeehVrMfsVc7pAOUc7Ubv7xkR6JLAUyIwX8RHmZU7Bt8ggwUX69bToigojsASHVTTWEVMr4bhB6lXpocFADCp26Dj67IHZ3vfNgs8tbf_eM4pzeCE6WaDv0SkrOjUOlaAPQ02ZrGKb64m4PD-ol3DhxybM9rk9XIzbo-KjnEUGEdTqbjPG_av3bjHXta2zEY5HgBuYCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروهای داخلی ۲۰ درصد بیشتر سوخت مصرف می‌کنند
🔸
مصرف بنزین خودروهای داخلی حدود ۲۰ درصد بیشتر از نمونه‌های خارجی عنوان شده است.
🔸
در ۱۵ سال گذشته موتور جدیدی در خودروسازی کشور توسعه نیافته و ضعف فناوری موتور از عوامل اختلاف مصرف سوخت است.
@amarfact</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/684174" target="_blank">📅 12:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684172">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845a0dd0f0.mp4?token=AwReGE5FO_5e-Q0c_cI8WX6dPzT7d-KeqcJlzxFT8TDu1rZ_sNhNkTycDk1pnI-mQKUUX78cEJpL7krNiN1U6uptjcbrroCURcZVA5gHrIelvPPriDePnp5FYnuRi-4Zzq3_-Mo3ds1WiHtnOtqtiTL74MXxNmMzxOFWtBjF_kobn8PwW5dZ_JW3nAbtmerhr-RX2_P9HFp-ifmB5mgrP5DPhYq_-NVryF42sb3JgLgroxF24xA-LS14O-EXPeKvjvucsCO1t6DZtsklJNm6r-ThJUFVsOatez9-VeclkGhDscq1dY5hd-SOEswQqd_iIvIwGlbM8bwwqNy7gw8tLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845a0dd0f0.mp4?token=AwReGE5FO_5e-Q0c_cI8WX6dPzT7d-KeqcJlzxFT8TDu1rZ_sNhNkTycDk1pnI-mQKUUX78cEJpL7krNiN1U6uptjcbrroCURcZVA5gHrIelvPPriDePnp5FYnuRi-4Zzq3_-Mo3ds1WiHtnOtqtiTL74MXxNmMzxOFWtBjF_kobn8PwW5dZ_JW3nAbtmerhr-RX2_P9HFp-ifmB5mgrP5DPhYq_-NVryF42sb3JgLgroxF24xA-LS14O-EXPeKvjvucsCO1t6DZtsklJNm6r-ThJUFVsOatez9-VeclkGhDscq1dY5hd-SOEswQqd_iIvIwGlbM8bwwqNy7gw8tLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس، معاون ترامپ: باید به یاد داشته باشیم که کانادا یک ایالت... ببخشید، یک لغزش فرویدی بود؛ واقعاً اشتباه لفظی بود؛ کانادا یک کشور است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/684172" target="_blank">📅 11:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684170">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d754d5d97.mp4?token=Rm4poEJBCOCCO8zAQxC21LnHwSW77kvBghMUUQlUWU-tm8MpF219rSYE5SMGrhsbTef-eKvs30wtl_UvCD1-rR5JrKK-WxmASaWsIocqvGHDPVnQXLFQzqwHR202mOFGH9sZkhg-fBzKvr8PLJhSPmXT58cp03kvkEa9oFE-mud7zX0pmFRPrdytOLK2ZtaqNRk0wh6eqUYwO1TN9kmNSOQ78OaINHcWS9N8F8ahNG4FzNlHYGWuH5r0J4WC1LOEsjEtKQYHNKBG02gURifJCZ7JAQoRAVzv44eo7oZXmKKkaSybLPCzcCG0hI0UDlXpsO_4--JgGr0hq46gCuV2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d754d5d97.mp4?token=Rm4poEJBCOCCO8zAQxC21LnHwSW77kvBghMUUQlUWU-tm8MpF219rSYE5SMGrhsbTef-eKvs30wtl_UvCD1-rR5JrKK-WxmASaWsIocqvGHDPVnQXLFQzqwHR202mOFGH9sZkhg-fBzKvr8PLJhSPmXT58cp03kvkEa9oFE-mud7zX0pmFRPrdytOLK2ZtaqNRk0wh6eqUYwO1TN9kmNSOQ78OaINHcWS9N8F8ahNG4FzNlHYGWuH5r0J4WC1LOEsjEtKQYHNKBG02gURifJCZ7JAQoRAVzv44eo7oZXmKKkaSybLPCzcCG0hI0UDlXpsO_4--JgGr0hq46gCuV2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تابلو نقاشی نیست؛ لرستان همیشه زیباست
🇮🇷
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/684170" target="_blank">📅 11:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684168">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3a673c1e.mp4?token=XldwbjvfstYH4qge2_S5_rOYQZje-dVEFxMbvRnmqMU8cjEDXe7vuQywQhuC18I55NHrBbChnp2obkQp-3BaVQmYmReKGprWLm6S4RKs-3587i7LLKO7Js3EY__nHzLU0MBLMf2oYErboAG4HcDTY_HnoSaGS-dwAsfN9pF200l4L1Fm4YFGrIcKRI7KfM4JdtxGPw6aJJ_NIM3sIRctEtJ0mUOOPf5ljQprS7KGBnXYHRrFmKxDFbRmvEjlsSgeJbnuaRFg19qNmeLzG4JKYPRwUjK8nFsf2f4AKfn2RQ2AM1czBAocJYbBnn0sKAolFSvkKK25RJGNTSn_nuZInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3a673c1e.mp4?token=XldwbjvfstYH4qge2_S5_rOYQZje-dVEFxMbvRnmqMU8cjEDXe7vuQywQhuC18I55NHrBbChnp2obkQp-3BaVQmYmReKGprWLm6S4RKs-3587i7LLKO7Js3EY__nHzLU0MBLMf2oYErboAG4HcDTY_HnoSaGS-dwAsfN9pF200l4L1Fm4YFGrIcKRI7KfM4JdtxGPw6aJJ_NIM3sIRctEtJ0mUOOPf5ljQprS7KGBnXYHRrFmKxDFbRmvEjlsSgeJbnuaRFg19qNmeLzG4JKYPRwUjK8nFsf2f4AKfn2RQ2AM1czBAocJYbBnn0sKAolFSvkKK25RJGNTSn_nuZInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
بازتاب تلاش و خلاقیت همراهان خبرفوری در کسب‌وکارهای خانگی؛ گام‌هایی استوار برای چرخش چرخ اقتصاد خانواده.
🔸
مسیر راه‌اندازی کسب‌وکارتان را با ما به اشتراک بگذارید؛ در یک پیام صوتی ۳۰ ثانیه‌ای نام، شهر، نحوه شروع و نتیجه کارتان را بگویید و عکس کسب‌وکار را هم ارسال کنید. روایت‌های منتخب در خبرفوری منتشر می‌شوند
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/684168" target="_blank">📅 11:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a9dbd2ef.mp4?token=rXCqNPRnW-8AEkYsTNcuPOTpfz5LC47bwEcQUPY1LSCBqGRKIaZenLYv1j8oMql9xmwtCj0f3Ffc_I3As57or4DaVIFJJKvv3dkx8FDCqU5mI1DR_nQirovEd81v3veTyiVHgg0YNuM3PckOXknSTpfZClxGlEUKNme7t5GyMkAHpuCejTO7Emjv01nD8c4N9IEh35ETcTS6Y-AFU0noWTnmiUqnxv_g7A1EBUAWbSmzLC1vm9vnwSPor1QyTobCxWx8KXs4fs3iTkNED72-CMUXEm9gNp-5KNjHqhSP4MgznOLn70OpvN3jyNbQsVqWAddjqTAI2-7VgW2ylJfRsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a9dbd2ef.mp4?token=rXCqNPRnW-8AEkYsTNcuPOTpfz5LC47bwEcQUPY1LSCBqGRKIaZenLYv1j8oMql9xmwtCj0f3Ffc_I3As57or4DaVIFJJKvv3dkx8FDCqU5mI1DR_nQirovEd81v3veTyiVHgg0YNuM3PckOXknSTpfZClxGlEUKNme7t5GyMkAHpuCejTO7Emjv01nD8c4N9IEh35ETcTS6Y-AFU0noWTnmiUqnxv_g7A1EBUAWbSmzLC1vm9vnwSPor1QyTobCxWx8KXs4fs3iTkNED72-CMUXEm9gNp-5KNjHqhSP4MgznOLn70OpvN3jyNbQsVqWAddjqTAI2-7VgW2ylJfRsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد نامزد مسلمان سنای آمریکا علیه رسانهٔ نزدیک به ترامپ
السید خطاب به ترامپ:
🔹
تو نمی‌خواهی دربارهٔ قیمت بنزین صحبت کنی؛ نمی‌خواهی دربارهٔ قیمت مواد غذایی صحبت کنی؛ نمی‌خواهی دربارهٔ‌ خدمات درمانی صحبت کنی؛ نمی‌خواهی دربارهٔ این جنگ تجاری احمقانه که اقتصاد را نابود می‌کند صحبت کنی؛ جنگی که در حال نابودکردن ارتش خودمان هم هست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/684166" target="_blank">📅 11:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyYaIGsGPANFQ6OhPTZUvCXFKDF8LIxIjEBGvCDQamIcQ5fAguofRE1BB8NtHz2Hb5Hv6HFvPN-k6_PsmVT1vJye1f3_jcI4o8ob4hg8e9CAoNkmezAeCYlDZ13GtZ_CjF1V4if1uJN0BcTYk_6YPIOeWxV8g-hVGxKpYDWTS7keDpCYj4JNgAqkkHEgEEkyZaaKd44ddQa6OnqkoYpu3EAuql8NWIAzCRUCB817twaSiezqTF7Y-FZmBsLRMNKLcgEu83meEOMCN3yfUUIU2VMwQJMSlheKnGRKWdiR1DaVcjNLvP1bTlG5VDVM7kJMTtis8kj0m6FbY3HBSIdfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhxoASpHy3I4FoLw9v8cCuVj9xogo0NiIhz7Q4Z6sPawQK15Sw5ry8HIip1Dvxt2pYp-cANrD5DmdVLZ-r_pzfG_3TRxvHse8ovIgqIVpMCIG41a-YS9tq_1nsG3kNHfGyBeMNXJUhJIagiCJXTuDdAhfn7TNNVeZRYa9ljPHfOBCeKU3JX-4v4_l_12xFzwzbBlzBSbnmGD_efyNjqP7svKiG7nfT0PoOAOF0_uOBN7phYsnUH8FWTtxycDtwZNaAGZ0Dlwm-v2xdvwIiMjm6V6Pv5ugENTbNZRFFy3gOEtKt-tcOWgxZzvd3iFIlDPTpoVFXBfgbAMMH5eM96ZAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نویسنده سابق گاردین: مصاحبه درباره حکم سنگسار سکینه آشتیانی ساختگی بود
🔹
سعید کمالی دهقان، نویسنده گزارش جنجالی گاردین در سال ۲۰۱۰ درباره سکینه محمدی آشتیانی و ادعای حکم سنگسار او، اعتراف کرد مصاحبه با آشتیانی هرگز انجام نشده و متن آن را خودش ساخته است.
🔹
او بابت انتشار این مطلب عذرخواهی و مسئولیت آن را پذیرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/684164" target="_blank">📅 11:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684162">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097af909b6.mp4?token=KwdtMT4hAMfvWU1zlqTKzVy8a-1bep8k1R7qwKuwdUllVUs74oQflWYz26yJq0Isv5kBh6x6P1_RDSOl8oqTpIhK9bJ0gTGh29cLEm4KeOphQsftp96i5EXD78uVXDu1UEteCAZABLlFcU88DUGIU327VBFqvpw_DnQLvh1t4woTiLqd1whNDRL_8GFdvCYJDx8-K4xXmdv7Bk4Bc4gf7aCuhbXY4bXeKomzApqeIGBjPoeT56Ni3O7VLrvToCmPL5Z8jeymE7X_3ClTzGQ2dlLdQJPVojcKiaKCYaWfsiOrL43d1webLUoS_KmZ_LYNJMWc8PvINxpFEEldkX0fwa40Yq5r-BIpZVk-Byq2WdbJY41BfBENAp2ShFJeaXWm8XdF7jSpx-kx6tCyaBSIDOiybah2c4Oozl1fF4VmcFQiePsNwTRa36ZgKqmgCP14CAU_E_kOvTbiqiw1sbykoZMCtDdCdQT5f9LS2Ttv9RaGy1zwJXvMFY5QhprxYKXZvdwfSb8R6HSwhXCf9YGh3q8Qi01Pxo103L7xILgjh8_qTjE8lUQNT2uMexwNGIp9yY-R9odBA5wW_UAS9DbBR60r-L-XyvUFJUuvrgdR3JxW8anbKDyJXVJYg5k8KJRZVQQU0JrpAJ7ML3WcrS2xjSbP_oGSW0FV-hC1HNOdW3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097af909b6.mp4?token=KwdtMT4hAMfvWU1zlqTKzVy8a-1bep8k1R7qwKuwdUllVUs74oQflWYz26yJq0Isv5kBh6x6P1_RDSOl8oqTpIhK9bJ0gTGh29cLEm4KeOphQsftp96i5EXD78uVXDu1UEteCAZABLlFcU88DUGIU327VBFqvpw_DnQLvh1t4woTiLqd1whNDRL_8GFdvCYJDx8-K4xXmdv7Bk4Bc4gf7aCuhbXY4bXeKomzApqeIGBjPoeT56Ni3O7VLrvToCmPL5Z8jeymE7X_3ClTzGQ2dlLdQJPVojcKiaKCYaWfsiOrL43d1webLUoS_KmZ_LYNJMWc8PvINxpFEEldkX0fwa40Yq5r-BIpZVk-Byq2WdbJY41BfBENAp2ShFJeaXWm8XdF7jSpx-kx6tCyaBSIDOiybah2c4Oozl1fF4VmcFQiePsNwTRa36ZgKqmgCP14CAU_E_kOvTbiqiw1sbykoZMCtDdCdQT5f9LS2Ttv9RaGy1zwJXvMFY5QhprxYKXZvdwfSb8R6HSwhXCf9YGh3q8Qi01Pxo103L7xILgjh8_qTjE8lUQNT2uMexwNGIp9yY-R9odBA5wW_UAS9DbBR60r-L-XyvUFJUuvrgdR3JxW8anbKDyJXVJYg5k8KJRZVQQU0JrpAJ7ML3WcrS2xjSbP_oGSW0FV-hC1HNOdW3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اون چیه که مثل یه شربت خنک وسط تابستون به دل میشینه؟!
🍹
@Tv_Fori</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/684162" target="_blank">📅 11:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684161">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b84d78758.mp4?token=q-Ywizx8rBGt8WEebBLRssDhNjN7sZX0Oth1VnVU2GESZdLue30is_ITzXYPLAnxQoK3kewupRPthFkota8joMHFuAK_JDS3xe9XYcbwzEu9n6Ht3UcPaaxea0aX3a-uOSAMRq9nviFsUh1fXVRnQWQx4vremv9hZ0TwdIJ_CU1KUWx_Srk8X4SGjn4CYZMBvbMGwtU759R8MnF071GozBBf1PdTbbmSM9Co4rX6x3DzPSQvgR2yydt7GTmjWwgS10kPZnnFAOZ2PiRQuYgy8cDdYF-bjKB6buNxT5cqgRBtQPseqghKm_cKnBf9bDx-eIG_pg1Ecjs5Ga7LWrjAgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b84d78758.mp4?token=q-Ywizx8rBGt8WEebBLRssDhNjN7sZX0Oth1VnVU2GESZdLue30is_ITzXYPLAnxQoK3kewupRPthFkota8joMHFuAK_JDS3xe9XYcbwzEu9n6Ht3UcPaaxea0aX3a-uOSAMRq9nviFsUh1fXVRnQWQx4vremv9hZ0TwdIJ_CU1KUWx_Srk8X4SGjn4CYZMBvbMGwtU759R8MnF071GozBBf1PdTbbmSM9Co4rX6x3DzPSQvgR2yydt7GTmjWwgS10kPZnnFAOZ2PiRQuYgy8cDdYF-bjKB6buNxT5cqgRBtQPseqghKm_cKnBf9bDx-eIG_pg1Ecjs5Ga7LWrjAgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبدیل دوچرخه معمولی به دوچرخه برقی
🔹
هواوی موتور برقی جمع‌وجوری طراحی کرده که به بدنه دوچرخه متصل می‌شود و چرخ عقب را تا سرعت ۳۲ کیلومتر بر ساعت به حرکت درمی‌آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/akhbarefori/684161" target="_blank">📅 11:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684160">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEb8UmQuZImhxdpHseMkK92OvleHXHNDG0QeCAsdQiHScr9wBgIz8ST6wHtbk_aP3JDc_5C9KpX3XZK_V7pcTODxkgs-SiBm8deDHM8FOFBpPZIc2mCaMu6a-Lg7WE6G490BtuFcKL8FHt4o1caAKIOYyBmeTy6TlskNmepvJU77RNxLxFoNB6-nUpnCid5r4nMfeCs1EYLgXm_bUMsRThm4lEfE1ObtibqBzZ9xwqfANqbxZwS8zNXckzxZwUM-Vr0w31mRclsR1akbftCgqLUQZl2OTs9ratMWrQGs28MqctMMxQ2kNFG1Ud5HKu86JyRpmGfKguVVfPWTbMEicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار مدیریت بحران نسبت به ناایمنی «بازار پروانه» در اراضی عباس‌آباد
رئیس سازمان مدیریت بحران شهر تهران در گفتگو با ایسنا:
🔹
بازار پروانه واقع در اراضی عباس آباد از لحاظ ایمنی خطرناک و پرریسک است. سازه‌ای که به این بازار اختصاص داده شده، برای این حجم از تردد مناسب نیست.
🔹
خطر ریزش سازه دور از ذهن نیست. ۱۷ عامل ناایمنی‌ در این بازار شناسایی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/684160" target="_blank">📅 11:03 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
