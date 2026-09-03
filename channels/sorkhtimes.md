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
<img src="https://cdn4.telesco.pe/file/HVHNnZVEfZwhBXFC_ykW-C95tQbmsa7EBoa4bG9tuNn_APwdDG2dmZLZ2wjt9la-4AKAUg_6jvi9VfyrNGLzb_4gja7JFUIo2sAdYQp5-_9o1jDq3Dp3lkgyRr_HMk8dAlzJFR2ee-ShVm1Y8eVY1oJXr94mJ457tMV_a4El1A8bbmXGGzjEYkmoihil4orZUjrYwifrMTUr49LpDK5ErMFzMdvrXRndeZqtEmzu1Rp3gKAY-KVZJ9o_GYwJqzaNbBdKaSZUwACAHgDCyUnc0OxM5fWW1zaLt_G2_q6cQvVIsyil0g92tCwra3bB2BOs6DrDUV7Hyl0O1_q6D9_fcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 20:53:28</div>
<hr>

<div class="tg-post" id="msg-139497">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
تارتار ضعف پرسپولیس را پیدا کرد!
✔️
تارتار به این نتیجه رسیده که پرسپولیس نیاز به یک رهبر در خط هافبک داره و نیم فصل قطعا در این پست تقویت خواهیم شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 425 · <a href="https://t.me/SorkhTimes/139497" target="_blank">📅 20:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139496">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm3AvlVjZ9AOiGEaLk1sUeJZ7AEG9oUmbTMcSA6YC04RWmTDm9MtlfJ6MkkEg1HUNebLcjPcCBaZYcIvhwC7QjmdWf1kQ91A670pZOYb6oxk1hSyWmJfEn3_QwPj2j5R5DDlPVSJFOh2--jLsMy92Yxvy_VXNihXeS_I1S4-_ITZWrnnIpuH0ATpnSln2SauhWbnSk7utUWWlB4-6jvcUMM7-QzeM-TNpIZt9gkoLWGJ0t6A4FK1ijXoIqFh6jz_3WfV6OlFsTNlf7UlNkA6ndCLHbnwzLSNbR1KVNHWWXsGAxjQZpeWDtDtYPdVtb13S0c9itXzc9bhbWAMPSoN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🎙
خلیلی سرپرست پرسپولیس:
❌
مصدومیت گرا از ناحیه آشیل است. تارتار گفت اول باید او را ببینم و در مورد ماندن و رفتن وی نظر بدهم. هیچ اختلافی بین اورونوف و کادر فنی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 545 · <a href="https://t.me/SorkhTimes/139496" target="_blank">📅 20:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139494">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrEOnHtRVYiw52GrJ2EA4_3OfmoYSH6Kw0Oj8O2HBWWTgrEHE2tBaWblBpGEJVdbzJ8m41emcFz04IfsprMbtUs1j-Nk-fcxyCBxRncCiIXbqbwmi6WCBTZ3dz-97QgFNvroUs1NcEPMHpwMbGD8d6cmIu7ab-6ls7YqCLDRUj8W__O-SYtPiiXBIXHnoMNi9Zwz0mevKefD_ZKV0H_usluGr_ksOkQCmv3E6uCAag8uE1CINqMVbIYIDe31XCARaH5VnYLzSAwxcDWXkqYjIOCt9RN9iUMe8Ig7zqHCb121l58U7ksg-Y_tGwp0BMSQmm-keNlyFQ44aXZ7tEI1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد سرویس و قدرت در نیویورک
فریتز به‌دنبال عبور از سد بلوچی
شانس بیشتر با ستاره آمریکایی!
[
تیلور فریتز
🎾
🆚
🇮🇹
متئو بلوچی
]
🟡
تنیس یواس اوپن
⏰
امشب ساعت ۲۰:۳۰
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SorkhTimes/139494" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139493">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0ItbsYza2L6JHmpWO64WuiMc-XAzRzGaQmTLjC3ZWgv026WYvOGIshAwUwaD6yvOMHJeOzWfl0dXifFF7MwQvNGY9jUY6Mfca8jLeYCUiqQYISzgQ9YkvdvocQWTU3QSi_ZPoY7DRIh8_bgTZ_V7DYHp5wRl3hMpnT8YAKVOpCsWKCl9qx2YM2di2_8ldPrnQn8WMsaX-velFgyXSUyQ9EpikOTXhtV9mnRaW6sqRlY8TRBGlCHjhCHMMPEBT5mdM2sH9hONY0tnzCU38y5s0Tgn7WarsMxCj5YgTJueGhdSebQSsTsS8TlZrFADFQ1TckmEF-LbZgjfmZEeGwVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/139493" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139492">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlELnFD67FxjnEdC2UrZ1oxipA6vT7WVKW0rvhtP-mgPDCDqdocT6VOSMSTb3dH8RtUmzbYGgfp50-4tAKzK-C1vY5E6ULmmln3RCbeYXHr6VH7WSRLbIbJ4tYj772d7avznRGp81jLUZfrVDEFPxHq2Dg_PgW2tgY3fjREt5LvhQXOHR0kpP1pOi5StMCqIiZK30PQHMnlaPiHa6OY5G8cbUUtvWHTZqHQkWoEeVKkcsLvMgLTGW7Gu53gaq6XgjLltZUJz-Le_HBvlojpKFUFW5I0b2kffklO7s-S3UVeMn9hMgrBA165nFhtLpDbm_h7ErMAA1zH7raUVdA7nmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/139492" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139491">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#بماند_به_یادگار
🔗
💯
تا روزی که اردوبادی و اینانلو داخل هئیت مدیره هستن این تیم رنگ آرامش نخواهد دید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/139491" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139490">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC2g893onQ39syxOhE7-t9b04_q-PLtccbZdMZeva0s_9QGhpcijNYRNPNXulZAfzWXcT3a5S4ipBHew0Y-vMKi0K4m01nHyMizPs6WtbLvQodUQI7FSO9-DmLiuGJx3bfViXFM7ioWiMH3HE7M526H2TFF9vQ2yOA4NGAqnlLXRRurzWjNiqlqLe213A_NYVT5SG1B8XF9xwTrDuQR-5g24UJ8wC8JvOc-UH81ZNrzX46Eq2uHWfZXAqQUCgu5ZS0-3Yv4XEAoHEnayO5v5ZnXbbAbCPQizkp-zTMM0nNZeeLAURdDbYia8E9sOZijEouK-PvhKf1fohCUr7ivz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس امروز در دیداری تدارکاتی به مصاف مس رفسنجان رفت و با تک گل پوریا لطیفی‌فر به پیروزی رسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SorkhTimes/139490" target="_blank">📅 19:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139489">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLInYUXqLIDcMmVy5XHbfWXx0anAk54nQlck6dqxZ8hWb5YIXH-jl45fVK75a-PABnLjSQ7tY-biUn-jcq7suSMUpjRXWbQpvAlJS35iSE51cy1tRFdfmE7nnww7dHaSxzjZJSxB6BJRzC2CtxDrv8PJmlzbHzarsI3c0ZLflmEH-zV6gC8Y_oNgY8Ky9xzKQrnD68Hs8Hg2fa_9TMD87I-vdoAK9wwBSi2HdcO0OBgC_oWhZH1ZrylUNUBAVlO5AIuR1v0LlyWBePbreBL8jrmHJr93jNZ1WG77Ul-wEWJM8pMg_KUp_QWFhvY7DNq88b8gbiiqH1cpWJfHJjp0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های درست‌تری بگیره و بیشتر به درد تیم بخوره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/139489" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139488">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/139488" target="_blank">📅 18:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139487">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9PwJ3ZqR41PFX4kWw0upOFNM8LjgYOFSoFoBahCsbSvWicm0esHd3Go7M6OpKHYdBUAmMj-wch5Bk6DSWkG2Y92-uUl4ZGPkwF_TV3aiDhfXyZohhmrG8NtRcJBYW8SJQ08snd7apYXUkNd4E0USt4jz4z1m8uzAKJ8MZnQTopdbAroTSjsKmgIMCQZRMuDxpniKdkHDJQlTweKGRIFP0u1VcKcRHQijA4XGMiIPyTIvhSuHciMgDGRUCV3dY5TAwvt9m28aj_tunqdzdASnf7ILmlnzN1df9ogy-OaUJi2RoIW_yR_Q69uIwq0SaR_DwwFWPRWgpGCXzPAbEtlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/139487" target="_blank">📅 17:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
دانیال گرا مدافع مجارستانی تیم پرسپولیس برای هفته پنجم از لیست بازی خط خورد تا یک سهمیه خارجی سرخپوشان برای فصل آینده به خطر بیوفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/139486" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
خبرگزاری مهر:
🔴
پرسپولیس پیشاپیش شکایت خودشو برای حضور یاسر آسانی تو دربی آماده کرده. پرسپولیس اعتقاد داره کمیته انضباطی و سازمان لیگ صلاحیت لازم رو برای پرونده درباره یاسر آسانی رو ندارن و استعلام فیفا باید منتشر بشه
🔴
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/139485" target="_blank">📅 16:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
❌
❌
طولانی‌ترین روند شکست‌ناپذیری در تاریخ دربی؛ پرسپولیس با 20 دربی بدون باخت
✔️
✔️
کیسه کش حسرت برد دربی رو به گور می‌بری
😂
🫵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/139484" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=HrdRYNy9p0jp8nHNEeZsd0AzntHmzw4RXvOj4MarbdShq5CIB-26Nn-8xN_7lOHYb9hHtTqCRnHug96-j8zYUo6XJwJQ7NSn7PVVz3pV4jSPoXGucjT97dVy1IPjyV2FHn0RxcG2QDAiht0YlJirRDi3TDgf8khdQLd-rAkaLC4bJwdFIh-jiDof6GmLWsB_-rnGq7lxqgrKQpfat4EwbC9kYSJX7Ev8F96IF_gavpRv4Jj6T9WuRJ4GTYvsoiAO_5b7DlhRiOCmxUwAEWKYhcHpJap1KlzAEoylBDvyjA8rkgQJdRyUUZo2yh_wIipqkhb9Fcsmj4L3ft3K_m9ZQhRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=HrdRYNy9p0jp8nHNEeZsd0AzntHmzw4RXvOj4MarbdShq5CIB-26Nn-8xN_7lOHYb9hHtTqCRnHug96-j8zYUo6XJwJQ7NSn7PVVz3pV4jSPoXGucjT97dVy1IPjyV2FHn0RxcG2QDAiht0YlJirRDi3TDgf8khdQLd-rAkaLC4bJwdFIh-jiDof6GmLWsB_-rnGq7lxqgrKQpfat4EwbC9kYSJX7Ev8F96IF_gavpRv4Jj6T9WuRJ4GTYvsoiAO_5b7DlhRiOCmxUwAEWKYhcHpJap1KlzAEoylBDvyjA8rkgQJdRyUUZo2yh_wIipqkhb9Fcsmj4L3ft3K_m9ZQhRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
❤️
👀
✔️
تو این صحنه کسی متوجه نشد ولی وقتی از دوربین نزدیک تر صحنه پخش شد مشخص شد نوک انگشتای نیازمند بود که باعث شده توپ به تیرک بخوره وگرنه گلو خورده بودیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139483" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/139482" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139481">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139481" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139480" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/139479" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139478">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo5R-94qlvy-51HFMSF2n56xLSjHH1lhC15pZ7hzB_c8xA6YUkM3maxqQ1O_y9uwQfcwJnfpNT3uqE2qcqw2JmmNaKt61pTLyho-1Kzgry4DokoaXycIv6V722NNDsm73bgfiDncqRreEny7ALrT1sfiSMk5Ks6MujLesPshjwWb_PFnAGXOXSRagfW5qPq7OpCui-s-RbAR5Te_ukNurSPFldIG1l6x0N8Pdw_y695GVGP4zkI2xKFtIQVHnumWBedhIewHHYokMolxafmWtmwL5898DVcq-qK_2wuDr2Ak9IdxsHifCMU1AtrLTOzOZtUFd_Jb9Ey6lN8beTzqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سوسیداد و سلتا؛ جدالی برای سه امتیاز
دو تیم آماده برای یک نبرد نزدیک و تماشایی
کدام‌یک دست بالاتر را خواهد داشت؟
[
رئال‌سوسیداد
🔵
🆚
🔴
سلتاویگو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139478" target="_blank">📅 13:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139477">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔄
🔄
🔄
با حضور یاسین سلمانی در بازی دیشب حالا مهدی تارتار به تمام بازیکنان پرسپولیس بجز محمدحسین صادقی که تا حالا در لیست قرار نگرفته بازی داده و تمامی بازیکنان با ذهنیت آماده به سراغ ادامه‌ی لیگ میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139477" target="_blank">📅 13:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139476">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139476" target="_blank">📅 10:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139475" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139474">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
♨️
🗞
| #فوووری از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139474" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139473">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139473" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139472">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139472" target="_blank">📅 09:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139471">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❤️
❤️
❤️
❤️
🔴
صبحی که دربی و مساوی کردیم و هنوز داریم حسرت تک به تک نزدن علیپور میکشیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139471" target="_blank">📅 08:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139470">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsvU1A7tYkHdl9IMvFz-wS__-7ZtVjFXvFfcM0S3oQ_mZ3zFs1Ur9hv22rh_2wCc9FUr3QxEh9wFIGLsyo3XKYQV3KXUjAjsyzeIj0tQIpTsqdnFoo_t8QYgGCFDq3VPE_fidq5QhCLxrz6FKfnwZpF5nrsFhlnPJuTqS5Dzt0votnsa8TEcE5k8u2ySemEZewKDKEY0JCu1qRmLp39jWun8VDTPo5Ie3xGlnZKlbVbGSfgdsdpr8H6GLPEWuhX6pkM4XMWxjwds5m6MNJBisrDSmOKizyWguoheiFBedUCdqgdt8Vkr5ZzxLoBs9N4k9m-tz8b-vXs_1NqxS4Bj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
جیمی فاریا
🆚
کارلوس آلکاراز
🎾
رِی ساکاموتو
🆚
فرانسیس تیافو
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139470" target="_blank">📅 01:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139469">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139469" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139468">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139468" target="_blank">📅 00:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139467">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0X8LxkR-zoI7ukPi6zKc-wwRAHyC0nlCUMCrM8JFhuH88h-l7JEssXzmoNR8JMUj15W8i8JctUIDuNJ3tAkhiLK8ugpfd7tD0GXqiZZhficXWOYdFI09B4BHiLVxPfb7GwP9WEoyAB268vmKsw1GTo9tyUVACdxsfrEgPspkHA47pVKO_mwhcb1MtTl-dp9NWqfNVH1E68DvdS1Bng0puZy5zInDufcBFEDv67SsgE5mvXKORRP3cwXv2QfIsVwH3KWAspTeo2_jsG-UYzHAHLMuFzLM9ORLHmfnwBdcBYv3PkGhkVU04ocWH_5fyr9rzAJluH5NQaKH1-T6W25mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139467" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139466">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139466" target="_blank">📅 00:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139464">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
فارس : نظر می‌رسد نظر کادرفنی پرسپولیس نسبت به ۲  بازیکن دانیل گرا و تیوی بیفوما  تغییر کرده و احتمال ماندن آنها در جمع سرخپوشان بسیار زیاد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139464" target="_blank">📅 23:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139463">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuaMoPf2rZaLMD1S0IRQjUjCAbJHhlJdiXK8GK3TiXNNViZgGFRRKjSao9VLrtV7aSkDVf8ZuhKyao8O6lfu5odZpGkx446Wad-VrQGfid5QNqIiRK5bMXYt3ealEY_9KMnFz9Y9Uo125EUO5bLUzp_-7wWTJHdz_x7jLvzD81SDbj260q8WshyLibZWCoB6472TT0JqWb1m0Yy9WjPRMp_TWihdCgaOc60Rn0kJtjIiGvqNdptDQ6PwwIDOCi0jDnO2BYS0b_27GyRuXfLEjfyQj7kgtpLTa8P2b7aA0tmzjMpQoVXhbGFpX52efeMlZnDPN1EQIA3mKGBVL2-D7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139463" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139462">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=r5p7xDrwRI3fTbBJxVQO7ohqatT_beZWnBLrtf9GQjJ93x9zfinjntWgmQUZAt8VJP5UmKwKwK_Ebt08lThs5sbt7P2vF_k3ECoosQdBJCy1u-67E68gTrM9yuZq_pTL8dr61dVAdtareQRSSXdUnVT3BAsWuAhKZOoSuGzsK8puTCnilGhMJfa0E_2oVPQAcvDYMFm0cM6dmvvfIUnrSdBj5dgb_TBdGDlQLK9qas2COCurHvYh_K4A8YVy0TQs24q-afxwRQaJMZWU7b79m1x1dQUy0hf26k6Bi6K4XfD1_C-OS_l9weMzdG-IULOaUPoQIxkLB-xNpKygVbKMaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=r5p7xDrwRI3fTbBJxVQO7ohqatT_beZWnBLrtf9GQjJ93x9zfinjntWgmQUZAt8VJP5UmKwKwK_Ebt08lThs5sbt7P2vF_k3ECoosQdBJCy1u-67E68gTrM9yuZq_pTL8dr61dVAdtareQRSSXdUnVT3BAsWuAhKZOoSuGzsK8puTCnilGhMJfa0E_2oVPQAcvDYMFm0cM6dmvvfIUnrSdBj5dgb_TBdGDlQLK9qas2COCurHvYh_K4A8YVy0TQs24q-afxwRQaJMZWU7b79m1x1dQUy0hf26k6Bi6K4XfD1_C-OS_l9weMzdG-IULOaUPoQIxkLB-xNpKygVbKMaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
بیفوما امشب دوباره یه استارت ۴٠ متری زد فرعباسی وحشت کرد دستپاچه توپو زد بیرون‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139462" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139461">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139461" target="_blank">📅 23:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139460">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139460" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139459">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139459" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139458">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139458" target="_blank">📅 23:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139457">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139457" target="_blank">📅 22:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139456">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139456" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139455">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: ما و استقلال خانه نداریم!
✔️
پرسپولیس و استقلال متضرر می‌شوند و ما خانه نداریم در شهرقدس از پتانسیل هواداری نمی‌توانیم استفاده کنیم.امیدوارم هر چه سریع‌تر استادیوم آزادی آماده شود.
✔️
اورونوف هم یکی از آن‌هاست هر کسی از هم‌پستی‌اش جلو بزند،…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139455" target="_blank">📅 22:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139454">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
✔️
✔️
به خاطر گل مساوی که خوردیم واقعا حسرت خوردیم
✔️
✔️
هم ما می توانستیم برنده بازی باشیم هم استقلال اما در مجموع ما یک مقدار…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139454" target="_blank">📅 22:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139453">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139453" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139452">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=K0QbmmprOLReMEabQ9cniBP-p_xy38BQg7B9rfaunZ2yVva8Wi92WUS_ePlhfeAMVUPAcNrbZXHvXaXco4cuY-vsIz0r2FcDHlt4lGiSMRq6npl00Ne_X9VWVYhj5eGqOOjICvQgEHMdogURtaATnnuEsh-E0aRLzapIR7bWUKscF3GgVlZXSV8_PzhvQoieTLyyVX09x0WPUuqPHZmdnU6r0Uke7MNl1UjHM3-OrHMEaeiibMKCAH2pqnWN81w7Gx5qFy2dWyixHcVVV7zns_HTBJdSDLE3jK6MWkuzrADS2Wywu59nxogqmobZBJgixWPwvWrG5pq2B9uenmMHkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=K0QbmmprOLReMEabQ9cniBP-p_xy38BQg7B9rfaunZ2yVva8Wi92WUS_ePlhfeAMVUPAcNrbZXHvXaXco4cuY-vsIz0r2FcDHlt4lGiSMRq6npl00Ne_X9VWVYhj5eGqOOjICvQgEHMdogURtaATnnuEsh-E0aRLzapIR7bWUKscF3GgVlZXSV8_PzhvQoieTLyyVX09x0WPUuqPHZmdnU6r0Uke7MNl1UjHM3-OrHMEaeiibMKCAH2pqnWN81w7Gx5qFy2dWyixHcVVV7zns_HTBJdSDLE3jK6MWkuzrADS2Wywu59nxogqmobZBJgixWPwvWrG5pq2B9uenmMHkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط تیم خوب است و همه متحد هستیم. هواداران صبورتر باشند ما تغییرات زیاد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139452" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139451">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار : بازی زیبایی دیدیم/هم ما و هم استقلال میتونستیم برنده باشیم/از مسئولین اصفهانی و از داور تشکر میکنم/حسرت میخورم که نبردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139451" target="_blank">📅 22:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139450">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiWC39gkveSkXKHO11eKGZWaKQkBUoE5wi4lVvpvk3835UWxBHzUzoxY3ZKlUAUOaIBsRFQi6yjcFgHO8F8Y6sfDolF23nZ2Ts_Ge2yo-AME6wVvM7UC3hjq89521e15VSpGF1cJqrp8L2BEbkfOJ5fdoRw2n3Xxpm0gf-rx8XvAzxtYqhlnZ7y9I1gJjd13IICqfXCt7eXOgArhUO7qxCZeCFJ8B501eYJ_KXlvChk1QTgmejEaz7ez1MwWg22Ees8QOFLjvMhf0z4_tLateGQXYQjK3ov2cgi56AUnDrKo08byw22y7258TZczFGqlR9Uu6MlyVwwK80WGQQn1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139450" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139449">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
ترامپ: من استفاده از سلاح هسته‌ای علیه ایران را رد کرده‌ام/ ما دوست داریم با همه کنار بیاییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139449" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139448">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139448" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139447">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=nNydko4uI_tC5edbyRjWubY-UZsTpxJl0iGanUvoHFrBrbKtvDH6HuCqApSmsMZH3OYKdJc5WHXXR0Jsu7KFATCBfOCo5m0EG8wE5hDihE8UYdocbyOKBokwvkzSScWco4TioRJPgjb_y9szD7KSn39PpaKYNwu27NWY13Ut-z1BudYNtKF6qUOlXmkcdINuJNSuTvct5jJ0JoGekKj7pok3l1WvGzbkdKKFx7eUpKXeaudaRSJHyMJXS1v95pF_zTj1JSmvlRPX9pqSxsAl2_UFyJ9xgl-dp0UrHBO8296Ki_i5KFQrlu1oyOJH33xUfkDm5kXacAHrenZf7qWH2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=nNydko4uI_tC5edbyRjWubY-UZsTpxJl0iGanUvoHFrBrbKtvDH6HuCqApSmsMZH3OYKdJc5WHXXR0Jsu7KFATCBfOCo5m0EG8wE5hDihE8UYdocbyOKBokwvkzSScWco4TioRJPgjb_y9szD7KSn39PpaKYNwu27NWY13Ut-z1BudYNtKF6qUOlXmkcdINuJNSuTvct5jJ0JoGekKj7pok3l1WvGzbkdKKFx7eUpKXeaudaRSJHyMJXS1v95pF_zTj1JSmvlRPX9pqSxsAl2_UFyJ9xgl-dp0UrHBO8296Ki_i5KFQrlu1oyOJH33xUfkDm5kXacAHrenZf7qWH2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139447" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139446">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=agpQ68dgAQ8g3UlGABRMS2VjSwqQm2c0HqNfxg753l0y5Rl9nKCbMvB0KeL0kvEmMaY53Dr3xmiV8PyIOJtz_iT0yXqQ24C8xOZRxCsbtxoq_hfSKdgMolfBR1qqlkh9R-vRQvD09DdTyscc7BW9AKbZaJigFFNn8Jbb8OGyYrgCRXH3TJb0cnAcwFOvUnp7X7X5cxLVeEn6cd0W4xv1QbnyeGurFf1QNegjhxHbNYZV5T4A_CPtkOO06NcL_BnGxhxKxbJ33NXGeQE3nmLfLKx1z3qR8NPEr6ViG0_hRdJYaI69FUCpZ7txhSvAe3kxU7-foErzjsNS-tqTmlImDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=agpQ68dgAQ8g3UlGABRMS2VjSwqQm2c0HqNfxg753l0y5Rl9nKCbMvB0KeL0kvEmMaY53Dr3xmiV8PyIOJtz_iT0yXqQ24C8xOZRxCsbtxoq_hfSKdgMolfBR1qqlkh9R-vRQvD09DdTyscc7BW9AKbZaJigFFNn8Jbb8OGyYrgCRXH3TJb0cnAcwFOvUnp7X7X5cxLVeEn6cd0W4xv1QbnyeGurFf1QNegjhxHbNYZV5T4A_CPtkOO06NcL_BnGxhxKxbJ33NXGeQE3nmLfLKx1z3qR8NPEr6ViG0_hRdJYaI69FUCpZ7txhSvAe3kxU7-foErzjsNS-tqTmlImDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تشکر بازیکنان پرسپولیس و استقلال از هواداران‌شان پس‌از پایان داربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139446" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139445">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">سر لجبازی ایشون سهمیه های فصل بعد ما هم به باد میره،نه با گرا فسخ کردن ،نه به ارونوف بازی میده نه باکیچ،هر کارشناسی هم حرف میزنه میگه ارونوف فاصله داره با ورژن خوب خودش،سوال من اینجاس ارونوف دقیقه ی ۸۰ به بعد اومده تو بازی چیکار بکنه تو کمتر از ده دقیقه؟؟؟ اونم دربی</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139445" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139444">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⬇
👤
آقای تارتار بازنگری بکن وسط زمین وله، چرا از باکیچ و لطیفی فر استفاده نمیکنی ؟! لطیفی فر هم بازیکن مستعدی هست هم قامت بلندی داره،مسئلت با خارجی هارو کی میخای تموم بکنی ؟ به چه قیمتی میخای اورنوف و باکیچ بازی ندی؟دقیقه ۷۵-۸۰ برای بازی دادن بازیکن جوان و تلنته…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139444" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139443">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx6elXd5Lj1afnDNDGn7GexoLT2F-aNQx0pOUYRx_J1OBMF7896ILTVNEqMntlcp5IvO9jZrrMUP_FymdtCDbF-rsM8wq0DIU--05BWqoBiuf21OtL5VRfaF-HADJRzGdDe45VRpI0JJVCG-EL0_IFuUO-PpyCLcLBB60s2UYe8wzOIpFTuTthNOEQx-BYHJn1BU6IsMp08kb5vGx6nggGERZsQbZTf6abqL7xQzOfd-CEkwHdTKdMkRB8xJk2bmaSk635v1bYCQa3aB4Faw8-xNdadAUTcinsOB-o4eDzbOYj0OQxQcuVnOorBLwvCMhC8DUh7DOFv45QusYQyN0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🗞
|
#فوووری
از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139443" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139442">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
هر دو تیم و هر دو سرمربی به مساوی راضی بودن و خوشحال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139442" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139441">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139441" target="_blank">📅 21:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم اگر وسط زمین رو داشتیم متاسفانه هم جلوی تراکتور هم استقلال وسط رو دادیم و همین باعث میشه دقایق حساس فشار سنگین بیاد روی تیم و بعدش با کوچک ترین اشتباهی باعث میشه گل بخوریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139440" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139439" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139438">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139438" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/139437" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
✔️
بی انصافیه اگه از عملکرد خوب مهدی تیکدری نگیم!
✔️
برای اولین بار تو عمرش اومد پست غیر تخصصی دفاع چپ بازی کرد و هم در دفاع و هم در حمله موثر و خوب بود
✔️
✔️
پر تلاش و انگیزه از دقیقه اول تا آخرین دقیقه ظاهر شد و امیدوار مون کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139436" target="_blank">📅 21:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
ما به اینا نمیبازیم ...نه ساله نباختیم به اینا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139435" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139434" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139433" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
امروز هر کاری خواستن با مجید عیدی کردن از بس که اون سمت اتوبان بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139432" target="_blank">📅 21:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139431" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139430" target="_blank">📅 21:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
گل مساوی و خوردیم متاسفانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139429" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❤️
❤️
❤️
ما به اینا نمیبازیم ...گل اول و محبی زد روی پاس بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139428" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
🔴
بریم برای نیمه دوم ..الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139427" target="_blank">📅 20:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
امیدوارم نیمه دوم شانس با ما یار باشه و کارو تمام کنیم ..شاید ارونوف تعویض طلایی ما باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139426" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
نیمه اول دو تیم خوب بازی کردن و بازی زیبایی و دیدیم از سمت هر دو تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139425" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
نیمه اول دربی بدون گل تموم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139424" target="_blank">📅 20:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
بدون شک بهترین بازیکن نیمه اول .تیکدری و زارع بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139423" target="_blank">📅 20:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس خوشگل کیسه رو کرده تو قوطی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139422" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
❌
❌
پرسپولیس بهتر و سرتر و سرحال تر داره بازی می‌کنه و سوار بازی هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139421" target="_blank">📅 20:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❤️
❤️
بریم برای بازی ..الهی به امید ...خدایا امشب و پرسپولیسی باش ..حس خوب و انرژی مثبت و بفرستید برای بچه ها ..انشالله برنده بازی ماییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139420" target="_blank">📅 19:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139419" target="_blank">📅 19:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139418">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105ef18474.mp4?token=KpEMeN8HQ0LLByOhZbC3RMMknbR6PLMnwj5aGMMK-OuNj9pC2tQ2PM5RGzLt-vU4iC7M__Xo-S7-fcUXllBly_yRZ6zYCJUJzSfE4OwGNp8O7dn-t60KIu0ul42kSgShgqrlSJ6o9PrQ3vp_JkKnpQr3l60-RFrC6qfNDST3U4ITwGklvJ40Jthm_l2S8OcwI4EE7V5PX_11VKMBoXE_Gl0KFM_T1yRDX1pHdSjvGh1XOy1R9Ogc1ddmIvh90sUw0WChPkOjGFs_L9IfmE_2OUSMrDxMup7nZmOEpsmPRwGKeBXDIOsw-Ig0_QCaqcY5bYRgmvW4GbYW4ySpDDSEAzjRyQK08xfUeM4cl7n5kLTwOecFhOIHNetPbEdYRJqT3MdXnQiOsu2Fk_n95_cfjN9WuQGSpU5QjSUyqheNLJnBdd8rfvj70Pu_W0EI_1DFwhkw-LPWMkHiEbBIHpSmPjP6h6qrEdfNbInjvEycSyJX7vJiXcUHBCzJ6uFZuqKrp_yXM0F4l2CcXbcv957Rm06DJNNPMEUJuyZQ-pafJln8LQm-loGbQX7mdFdvH8EGcWWnaWGI3gH1w_M3LxShN5BBpMFeYwzh_yYt0FmAeMd3OE1dHwlHOqFa8hwIR6U2Lv-KupiHjFJk0LX8fIrHdY2RANK2rbq5U7w07Tv-zFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105ef18474.mp4?token=KpEMeN8HQ0LLByOhZbC3RMMknbR6PLMnwj5aGMMK-OuNj9pC2tQ2PM5RGzLt-vU4iC7M__Xo-S7-fcUXllBly_yRZ6zYCJUJzSfE4OwGNp8O7dn-t60KIu0ul42kSgShgqrlSJ6o9PrQ3vp_JkKnpQr3l60-RFrC6qfNDST3U4ITwGklvJ40Jthm_l2S8OcwI4EE7V5PX_11VKMBoXE_Gl0KFM_T1yRDX1pHdSjvGh1XOy1R9Ogc1ddmIvh90sUw0WChPkOjGFs_L9IfmE_2OUSMrDxMup7nZmOEpsmPRwGKeBXDIOsw-Ig0_QCaqcY5bYRgmvW4GbYW4ySpDDSEAzjRyQK08xfUeM4cl7n5kLTwOecFhOIHNetPbEdYRJqT3MdXnQiOsu2Fk_n95_cfjN9WuQGSpU5QjSUyqheNLJnBdd8rfvj70Pu_W0EI_1DFwhkw-LPWMkHiEbBIHpSmPjP6h6qrEdfNbInjvEycSyJX7vJiXcUHBCzJ6uFZuqKrp_yXM0F4l2CcXbcv957Rm06DJNNPMEUJuyZQ-pafJln8LQm-loGbQX7mdFdvH8EGcWWnaWGI3gH1w_M3LxShN5BBpMFeYwzh_yYt0FmAeMd3OE1dHwlHOqFa8hwIR6U2Lv-KupiHjFJk0LX8fIrHdY2RANK2rbq5U7w07Tv-zFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/139418" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139417">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
بازدید بازیکنان پرسپولیس از ورزشگاه در میان تشویق هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139417" target="_blank">📅 19:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1244018c05.mp4?token=nX8bgdKyUF6xpU8uj9LYjpke_bCBjw-oBA4B5srvj2gxiJFOmEdcDQVyXdJBpPWnRSRW4vtaOS2dbL8eKKW0ofHyjS9LtJ4ELc_n150mQMCc3usE52axfwsCbQRrV42aBq1NS-k-BqPiWynjOuc_WqUQKf3yZ1UJTHeOk1Tf6n1HpHEjfXYBhxzG-ET2qZBhCV4jtiaNjNM1MWE0vqNumY3aHBiSjEirk9LamAV-nVpqOQUKZKLveupzjmXhLmYtuk5ABfufdAAj7w9AqWgiB4FxQV0sZ-BoHSN843UHhoKXfiWho06yiomqzDJzYQnCYwqGeUJ8WuceHZ9X4k3now" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1244018c05.mp4?token=nX8bgdKyUF6xpU8uj9LYjpke_bCBjw-oBA4B5srvj2gxiJFOmEdcDQVyXdJBpPWnRSRW4vtaOS2dbL8eKKW0ofHyjS9LtJ4ELc_n150mQMCc3usE52axfwsCbQRrV42aBq1NS-k-BqPiWynjOuc_WqUQKf3yZ1UJTHeOk1Tf6n1HpHEjfXYBhxzG-ET2qZBhCV4jtiaNjNM1MWE0vqNumY3aHBiSjEirk9LamAV-nVpqOQUKZKLveupzjmXhLmYtuk5ABfufdAAj7w9AqWgiB4FxQV0sZ-BoHSN843UHhoKXfiWho06yiomqzDJzYQnCYwqGeUJ8WuceHZ9X4k3now" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازدید بازیکنان پرسپولیس از ورزشگاه در میان تشویق هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139416" target="_blank">📅 18:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139415" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139414" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139413" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/139412" target="_blank">📅 18:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚽
⚽
اندازه گیری چمن ورزشگاه نقش جهان توسط نوشه ور  مدیر برگزاری مسابقه دربی 107
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139411" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44157a322f.mp4?token=gHM2Dg2zaY5j4XIkfdtzljfaZYcidqO66vBQAHoq2iAsOeZbmQaLcz51bCUSHh8kdYjwgVW0bvRxuns55ZVctkiUpUpupb_TAt0X659iI-cKMEZwYO3YvbkjAOKcdIvtmeHRs4k-_ovSkxJEOVMkREukiT7SUf1jQZ7yHiSab913dfLLD2ovr3fY2do4I-J2qcNx-eh7oO8KypucBk1MUpeRdkkQ55-UzNXdUf009zWXnnkgG13ohqmbycz0kPkkw1g4hsZh-7_e5uKVVy2fCza0KxeZWOzhUxN5f7pfjCf5JgrlU9cFAYcJkA8nEQug1QNLsIw4Llbgmk2HWfNBvhxyktUZOiuij7fRWDc2jvcEcW4RhaRNQ1Dm0WyeBXrPegjHsNP12HxC5pNiQ6zl-1PzPUb74v1uS-DqGGaRtoAO_2Ni8fk8YmqB1GO3oX-tmUfYM_VRqbYhznNWomva4Z5FN2Az7buhJ8zS3GOka2lGBmlzYiqjhRqUk8lIvdmsKJ8OXowivzVeUEqNg6qnQAH9OFOui8gxRlzlafVGIi1zWXm2xD_qBoRAyVR9J4uvRTLVbDUBsMMTdJlwgxDj3Zcwy-N9Vd7FyqPjVMvk3v5jn0NqNkih7uumzDoXitLXe8797vJzfRkHSlc10XJh2-gZCJ3Zsv1uxWuT-IRpw9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44157a322f.mp4?token=gHM2Dg2zaY5j4XIkfdtzljfaZYcidqO66vBQAHoq2iAsOeZbmQaLcz51bCUSHh8kdYjwgVW0bvRxuns55ZVctkiUpUpupb_TAt0X659iI-cKMEZwYO3YvbkjAOKcdIvtmeHRs4k-_ovSkxJEOVMkREukiT7SUf1jQZ7yHiSab913dfLLD2ovr3fY2do4I-J2qcNx-eh7oO8KypucBk1MUpeRdkkQ55-UzNXdUf009zWXnnkgG13ohqmbycz0kPkkw1g4hsZh-7_e5uKVVy2fCza0KxeZWOzhUxN5f7pfjCf5JgrlU9cFAYcJkA8nEQug1QNLsIw4Llbgmk2HWfNBvhxyktUZOiuij7fRWDc2jvcEcW4RhaRNQ1Dm0WyeBXrPegjHsNP12HxC5pNiQ6zl-1PzPUb74v1uS-DqGGaRtoAO_2Ni8fk8YmqB1GO3oX-tmUfYM_VRqbYhznNWomva4Z5FN2Az7buhJ8zS3GOka2lGBmlzYiqjhRqUk8lIvdmsKJ8OXowivzVeUEqNg6qnQAH9OFOui8gxRlzlafVGIi1zWXm2xD_qBoRAyVR9J4uvRTLVbDUBsMMTdJlwgxDj3Zcwy-N9Vd7FyqPjVMvk3v5jn0NqNkih7uumzDoXitLXe8797vJzfRkHSlc10XJh2-gZCJ3Zsv1uxWuT-IRpw9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
مصاحبه با مادر و دختر پرسپولیسی
✅
پرسپولیس امرور برنده دربی خواهد بود؛ شک نکنید.۲-٠ استقلال را می‌بریم؛ علیپور و بیفوما گلزنی خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139410" target="_blank">📅 17:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5be238bd7.mp4?token=vN58ZjjICcnBzb091WuC4ck1G3ItfWoFu1gUwS1WX48CZGCpoFmuB7derwuBYYZbe6aAtvNsqVwuki9hyNp6vwkmqgEjBtXgCetDpm4OC1By_ibCVlaffZr7EnaWAe1emv4k-QZTMcNH7elziOhMIX3r1KdTCGFTQrGW13lfh4ViqxDLARsMvmE1FYNEyeUa8fRGVE-_To5tbNRWUFxQAOxMNokHLp0DnJx7AsSAO27Y0rLIkhz9yXNEFfpu-OjZxDlIII7s4qFmsxYmLVq6T42OGjVcXvnxUM8lrqaD1v89J4G4P-oF_JTS978dx_t8eunONaxH9AHY-PbnzBW6jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5be238bd7.mp4?token=vN58ZjjICcnBzb091WuC4ck1G3ItfWoFu1gUwS1WX48CZGCpoFmuB7derwuBYYZbe6aAtvNsqVwuki9hyNp6vwkmqgEjBtXgCetDpm4OC1By_ibCVlaffZr7EnaWAe1emv4k-QZTMcNH7elziOhMIX3r1KdTCGFTQrGW13lfh4ViqxDLARsMvmE1FYNEyeUa8fRGVE-_To5tbNRWUFxQAOxMNokHLp0DnJx7AsSAO27Y0rLIkhz9yXNEFfpu-OjZxDlIII7s4qFmsxYmLVq6T42OGjVcXvnxUM8lrqaD1v89J4G4P-oF_JTS978dx_t8eunONaxH9AHY-PbnzBW6jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
ترافیک سنگین در مسیر ورودی به سمت ورزشگاه نقش جهان اصفهان در آستانه  شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139409" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4db0aec.mp4?token=dKfqjT-A3wM9o3b5uWQN1eO5UFC4YWGRF-8VXarM9uVefl-43VQ1PD1a0mMUWP6ilp9P8ftf6LxSLPQoE4eaPFfZlnCMi3tMn4LcppNhj7WFLc2zgrGhqHaGbxoXFMbwC7f4KUWfiRKqLD34mr4mMfSXhbWxDFZCDv-FEQI67t8dXbYrwavXrymLLm3wLR1ga0oLAnq2mwYcLB1BuPXWi_nlSSoKTQbMKw1PvLK4mHZYerzMYjWRE8b3xasKub5XHAIOGUjSFnC3bGj4GdFTd8bqg_hyMfOgh1OXauFc-VoSkunOr7P8siES8r_uG4mHzFsSedN_cDZ2Ty4DnLHHcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4db0aec.mp4?token=dKfqjT-A3wM9o3b5uWQN1eO5UFC4YWGRF-8VXarM9uVefl-43VQ1PD1a0mMUWP6ilp9P8ftf6LxSLPQoE4eaPFfZlnCMi3tMn4LcppNhj7WFLc2zgrGhqHaGbxoXFMbwC7f4KUWfiRKqLD34mr4mMfSXhbWxDFZCDv-FEQI67t8dXbYrwavXrymLLm3wLR1ga0oLAnq2mwYcLB1BuPXWi_nlSSoKTQbMKw1PvLK4mHZYerzMYjWRE8b3xasKub5XHAIOGUjSFnC3bGj4GdFTd8bqg_hyMfOgh1OXauFc-VoSkunOr7P8siES8r_uG4mHzFsSedN_cDZ2Ty4DnLHHcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
هواداران استقلال و پرسپولیس در مسیر ورود به ورزشگاه نقش‌جهان اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139408" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139407">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282676305a.mp4?token=gYI_XBwSa7quKtMJKqBUq5zEwM5RBmBMOpz-Zr8X4mcHZ2qiUe13I8iNDVIXF2T2XeGqz25yJKxDhxZEc03QjWgT9oBTwF_868n3ZA56R6GjRz5T9SpWzprHQOUJ-Od158jjzRz19X6xdxAIMENyCpnmanDVgQxvMJe4VXw1yepIGfBL7_8_icJiVK6drCdZgHjb3I6h39Ig7ZJhwPLnkhWSEIMU2Lrl2wYH0viLVTSXRza-Yim1JJhng9JvOxQP6fa1WPSnb1mceMUV6Hv76c8xZfc3m-9h9VpORnrQMZGdiDA1EVct72TH18AmpypD37lZccih0w03J3nmjHDyGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282676305a.mp4?token=gYI_XBwSa7quKtMJKqBUq5zEwM5RBmBMOpz-Zr8X4mcHZ2qiUe13I8iNDVIXF2T2XeGqz25yJKxDhxZEc03QjWgT9oBTwF_868n3ZA56R6GjRz5T9SpWzprHQOUJ-Od158jjzRz19X6xdxAIMENyCpnmanDVgQxvMJe4VXw1yepIGfBL7_8_icJiVK6drCdZgHjb3I6h39Ig7ZJhwPLnkhWSEIMU2Lrl2wYH0viLVTSXRza-Yim1JJhng9JvOxQP6fa1WPSnb1mceMUV6Hv76c8xZfc3m-9h9VpORnrQMZGdiDA1EVct72TH18AmpypD37lZccih0w03J3nmjHDyGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور دو جیمی جامپ پرسپولیسی و انجام خوشحالی رونالدویی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139407" target="_blank">📅 16:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7410fd3106.mp4?token=ji4ZyOERjyj1cFHXAiQwl1NVoiHFMFlCrXk8b47rWqTEAO_Waw68yS1IHS_QOpatlZS9FzA8LL5Z9HYM0B2M8DSZ7hbiDr53FGfu8bDn8TT0p18ekUy1zKwl8rS_oeEGqlk-UNHMoJe0sjVeb0yCGgflMGIDExZC4ZVO9KCXuxeokDjx-7bIU_VVaunqvzNi9iL_5YEUu_iB7MBSZfRBLwsw2qpwB-A512WDU--TYHd90-bfvv1nDeY4-M-P3fF2c8wK2rOQIhCCVtgb5n3ljsqzImScume6yZIXgL79OhiUoqrBcoMk2fXAOR1GGrJ-PM64CJr-tnnssAA4U3ccmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7410fd3106.mp4?token=ji4ZyOERjyj1cFHXAiQwl1NVoiHFMFlCrXk8b47rWqTEAO_Waw68yS1IHS_QOpatlZS9FzA8LL5Z9HYM0B2M8DSZ7hbiDr53FGfu8bDn8TT0p18ekUy1zKwl8rS_oeEGqlk-UNHMoJe0sjVeb0yCGgflMGIDExZC4ZVO9KCXuxeokDjx-7bIU_VVaunqvzNi9iL_5YEUu_iB7MBSZfRBLwsw2qpwB-A512WDU--TYHd90-bfvv1nDeY4-M-P3fF2c8wK2rOQIhCCVtgb5n3ljsqzImScume6yZIXgL79OhiUoqrBcoMk2fXAOR1GGrJ-PM64CJr-tnnssAA4U3ccmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
اندازه گیری چمن ورزشگاه نقش جهان توسط نوشه ور  مدیر برگزاری مسابقه دربی 107
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139406" target="_blank">📅 16:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139405">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139405" target="_blank">📅 15:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139404">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
❌
رسمی؛ ممبینی که صبح از سمت دبیرکلی برکنار شده بود، مشاور مهدی تاج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139404" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139403">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139403" target="_blank">📅 15:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139402">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=B6p6SzHjynXauQbDhDhk2ICEIxC2COS6XXkH7pCvhrnSke-slWusO_o_xGxpjcM85xXyNFkfotmEP0hgrI0UCxeH4g_JSysrDEiwFSmrBy2iaDvPnuLiDrGjc4n8wW2yjxwf80rfvS_TMWzCkGN90hJBLfN4JrLzUD_97rpRc-2_aaTb7oHEIvXDtnBi6eYZZZl1jG_rJKLmAyQNvWfQhQgYywm_UjV1hWNiQTXERYoJSVc7h4lPTLdn00lVY3Z7MaU3wcS2KmT93t95OqTQ2RPK2MkFp2trno4xZoQ3VcSHLIcVvumspuFQHDboJc5bfC4TU3-jliTClu6wyA3J1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=B6p6SzHjynXauQbDhDhk2ICEIxC2COS6XXkH7pCvhrnSke-slWusO_o_xGxpjcM85xXyNFkfotmEP0hgrI0UCxeH4g_JSysrDEiwFSmrBy2iaDvPnuLiDrGjc4n8wW2yjxwf80rfvS_TMWzCkGN90hJBLfN4JrLzUD_97rpRc-2_aaTb7oHEIvXDtnBi6eYZZZl1jG_rJKLmAyQNvWfQhQgYywm_UjV1hWNiQTXERYoJSVc7h4lPTLdn00lVY3Z7MaU3wcS2KmT93t95OqTQ2RPK2MkFp2trno4xZoQ3VcSHLIcVvumspuFQHDboJc5bfC4TU3-jliTClu6wyA3J1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ورزشگاه نقش‌جهان ساعاتی مانده به شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139402" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139401">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139401" target="_blank">📅 14:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139400">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139400" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139399">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
🔴
🔴
مروری بر بهترین گلهای پرسپولیس در دربی‌های لیگ برتری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139399" target="_blank">📅 13:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139398">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ephAA3TMuLCYMLVEpTN2ea34H-iOX32Q9bqGMOi-QJLgizOe-tMDtfqN0WsvR-DoFhV6qYSoaEoMoRsZbTmk2qV-croAIZlYtciJIudTiZbI3M7gbGW1a3Ft6hawH4Wcph3Bmpft74PTurZhoN7deqUUoFPg_IqwBiaLFSdmAM_j05Vr7tq7PPwyQ5AqQE21vDutyW2lEuIMgaS-PnChnFrG8qgQX0GZPQdxETQDmNE_1pvPwNqcChtcbZb0XYe-6osDjS0hYx45wQe4ogWUNXRTXH5wS-t0mybj75-Nc2OiPAzBQhNG4vrAj7Sf_CqvMknCq63lv5YZSYwU337n9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اصفهان در آستانه یک نبرد بزرگ!
⚽️
پرسپولیس و استقلال؛ دربی پایتخت در حساس‌ترین جدال فصل برای شبِ فراموش نشدنی.
[
استقلال
🔵
🆚
🔴
پرسپولیس
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139398" target="_blank">📅 12:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
نتایج 19 دربی اخیر پرسپولیس و کیسه:
📊
در 19 دربی اخیر دو تیم 8 برد سهم پرسپولیس و 11 مساوی سهم دو تیم بوده، و نکته اینکه کیسه بردی نداشته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139397" target="_blank">📅 11:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139396" target="_blank">📅 11:46 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
