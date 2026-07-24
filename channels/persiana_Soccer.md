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
<img src="https://cdn4.telesco.pe/file/YOxq070t0dZpYCmQekig9NwpN2t5iSn8K0puPFdDOuw6kYkM-iX5o93MwX78NngB6NM0MupEDeCkOhrk1WYB4Ep8Rc-yVOaJ6FDhhaT6ueRmlY7orW8ZStiwUUYv7ixUXvhDlc9UMfQE8BtvR-xSGDGBDQjc7jdQoLo9WYeF6AxAaF-z1OMkR4Qqhu2K5Z8nRSM2Dy0L5uelWHHXnhZE5YUo8JYWLqvck9Z8d0rOXCwYU8w6OEMoPChu4YUD9vBRNMVcX9KpEDsQ52S2msuZDz1Px0NMuLaDWn9TJCL8_-QI8rf1wYJhWtQmu2EuEy6RqR3lI3NZkxsXR9gFJ9txaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 563K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 13:38:17</div>
<hr>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=ubb0GwnhEtS6eg7AmX5TjFCWUTCpiASctAIvkpNcqxzS062r3TF76XQS6ytRfkp_-SuYitzLLkGei_jC2zATMHARpNOGbUq32IEoUAP-bDdIRIh3j4HxXygKKNCrzWqS5sx8qZod1rrOOCJBGw-Ic1CRJSJrbvXzfbtWkBFB5XnYVwvkKJW6DB-Ik-dLfjTKXIWQW0BcOnURbFP-VE4_lz2Q1Sx4GKaYZHnEzsuNgSuspoUWuO3XEla-D4S9lIl_XFyh4-4msC2fAcv7J5qmK8myMl_qNkW3u3LeSOT2uCD1gywt8flxWHkNgPYA4NFcuEiaiWtxF3VJbTRR7tEeZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=ubb0GwnhEtS6eg7AmX5TjFCWUTCpiASctAIvkpNcqxzS062r3TF76XQS6ytRfkp_-SuYitzLLkGei_jC2zATMHARpNOGbUq32IEoUAP-bDdIRIh3j4HxXygKKNCrzWqS5sx8qZod1rrOOCJBGw-Ic1CRJSJrbvXzfbtWkBFB5XnYVwvkKJW6DB-Ik-dLfjTKXIWQW0BcOnURbFP-VE4_lz2Q1Sx4GKaYZHnEzsuNgSuspoUWuO3XEla-D4S9lIl_XFyh4-4msC2fAcv7J5qmK8myMl_qNkW3u3LeSOT2uCD1gywt8flxWHkNgPYA4NFcuEiaiWtxF3VJbTRR7tEeZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQbaeAN36II6r40lZ0l2nDa6GHCrK9E7ErZmSW0EOnUpK_DCIASE0MlEqtt67-zXxQYzlkV58_3mp5fgt6EkH0dakZuKhg9pJCV4OlHMwmLIAAH7Y41_A66ZXrbV4jX8QEpAq2f08mzAvme7kRb1krMQW3ISrn8rOEGypazcx0yyBvNLhE3RA-gyXcw85XboqyUePHVjkN0KTL5uE8PRlTYFLLtyUxZXFzl0oIm3KK24F37muMLcqZYuRtDGCXW_2SApHwrFfaSumfwpjMgJJ-DxvRBbny77VBcz94hruFLSyyIyGgX-o43z2FuCB4ICRTDYxt6nCQ5xVW774TC_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P86JkuCTS4YODiYG70Xdhcd5o9zIVEevQw-GeSfMmvYwngkWwytxD6UonZ7cIHjJJ_DiR7JKnLaufROncBH612DBgNWIwgs6-1bGB61S1A7KcnKL_ohG2xmXw4soDgVP6lKxGRnSbPlzChR0Fmx4CD5jkVyRWS6G8hCCYOXaihsFzrBMygp-lSAKeiH4w2cMA9ai-cJaSUHzL3Z6tR2SP8IiPMEDCMQvwlOtbbc7DOFfp73-FdNezTbtvYuxZeBz7y0bXv1DjywSJuUb6tLwhV7dgwmTo4qTxUoegpSBfn-A-WjjkWOwnwPL5aGylTl36RcVF_SMgGfyUQNS7wxwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV83bXhkByfkTCGFl6-OYn7xpH3ZnBzmLszEqqTKOH_LEfdwY7-ycg1SnY3VtQ1-tmWvJL4l9QDPF89etTAGh5Fjbx1tkkGS8r-YtsYM3feulgcOUNF-KkPHqS1yv3EKLQuBEanW0ce4cNN4iT-edn6drEFR_N0sFFjH3AcTYOdLvc3wUUEpC1JB_juIB5xmkJPsmVox7Rm7i0bUsghwIK_SiNwBBOMj06TQ2VZjax8oze7PRdL2s_TSb8qBcifxOgxWqD0_CEKC0fClCFzTAooTSfnQ5RQFfYZLIACu6gYGpaxfztvfdS2ZrLMEv2PJhyLysck47u-T9iwL_aMipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=EOSC76St6nMtLm5r8bk7W1--8qpEblQ7Zuuk9hDWG952_XUnHnFEG34EbqBX7CmC2ZCc95jjg_62MHWrnCGsRJTRPTgQPue0ML-ZktQHGMEspdGCrfQu5kt8wdDnvCHySCrREen3Wmli7SJB4gr1tmBSR7tO78TjfUQWrtbLUTCgCTCzSTqMTvPgbQ-oRe1mLtuINnDYySkQLIjYFMj36H1S3-gMg0SPJVjHMTb__pxhbqhJkMpZbNoVTGRiTreQWbe2QY2bXgBXa8mlE-4KbGRC7wKnn4lISgT0Ge04BwJvMd9PibX7orQsLVaY9ZTmYLbm_LSIlrj6VpZCmOvQ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=EOSC76St6nMtLm5r8bk7W1--8qpEblQ7Zuuk9hDWG952_XUnHnFEG34EbqBX7CmC2ZCc95jjg_62MHWrnCGsRJTRPTgQPue0ML-ZktQHGMEspdGCrfQu5kt8wdDnvCHySCrREen3Wmli7SJB4gr1tmBSR7tO78TjfUQWrtbLUTCgCTCzSTqMTvPgbQ-oRe1mLtuINnDYySkQLIjYFMj36H1S3-gMg0SPJVjHMTb__pxhbqhJkMpZbNoVTGRiTreQWbe2QY2bXgBXa8mlE-4KbGRC7wKnn4lISgT0Ge04BwJvMd9PibX7orQsLVaY9ZTmYLbm_LSIlrj6VpZCmOvQ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyvyD1_33B0htX8BHvXQR7ABEALKSH-rrzRyGf7MkRkkfmnhLQAS704ojd_A5GXGogyvFC2dusymphFf2cKxof9Zv-Po_E16dTI3arg5wnYd4UA6-COzQDUixVB2Lz77SSVtEtV3rjG7S4zgTg_xuxsoUJsfjOqXCLY1C4BmW3Qv43C34zwfvHoEt_PrEkMSiXNEIw58oEvXMsrFib1km9dItKou9fV2DeFQ0IN0wuW8Rt5JFH_hWL5BPDHaLUOKpdi07p0P3cKZNbPd7I_fHMH0JJUiT2Ndd1GcW15vorFilaHYNCjLkAWkHx2DUC1Uwm4I7YsZH5GbcTNG_u-Nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neBRsu521zSxN_8an_hFOGlTsLKSSfCQwIjNt8yuckcUpRM9mP9egLmookZDaMsVF1ZD2OiNZ1EvAqt4-GxXV65O4lVclDJU9lBAFavympiKdRVJAJ15sASCDtb2pGfNX3TriXrWbBAt_Opekpob8L-2sYI2QxnU-_BeWDxFLkOOLJYjf-35hXjwQikzbAUOWS58UAfxWkpxrJ9GoocH-3Pifufda0BkPMHU0IPSGuaEMUy4d9aeWT9uJs76s4GtDBmvg1TZKWlxj8aB3IS8b3dJnKFS5B2HUMg6SAICstjc3prd28v9LTZBpD8zUe914jP_z9SRF8hlDgvDuhUM4bDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neBRsu521zSxN_8an_hFOGlTsLKSSfCQwIjNt8yuckcUpRM9mP9egLmookZDaMsVF1ZD2OiNZ1EvAqt4-GxXV65O4lVclDJU9lBAFavympiKdRVJAJ15sASCDtb2pGfNX3TriXrWbBAt_Opekpob8L-2sYI2QxnU-_BeWDxFLkOOLJYjf-35hXjwQikzbAUOWS58UAfxWkpxrJ9GoocH-3Pifufda0BkPMHU0IPSGuaEMUy4d9aeWT9uJs76s4GtDBmvg1TZKWlxj8aB3IS8b3dJnKFS5B2HUMg6SAICstjc3prd28v9LTZBpD8zUe914jP_z9SRF8hlDgvDuhUM4bDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUI-spun1GbdK8_K3EjZNthOtlMV_Ln_cIYaP5C2ZiAWA8Ud7nTyznlBiBqMwmVQBbD-nhdgByHFMT7-qf3Y_QHx8ZgTJE1fCyyGjavCrxtl5T4MdnIHWhQJemKGS9aadVtiURVjKxd6rELxCgJaL9zHe4QH1UWh5voFKzWAlWB63xtqlR9e_MEtyDz7hVA3XRbDnMw7ARSAg5yt9468QpR5yuE95W5qY1SnOrdQYO3aaJyAxuhSpTKmgoXqAqMEi-3YSWe8d6lvNFgTQiEbOZWXZ4YH-zNgNIqZmMn4jDX2COX8YESk4kM8GcPXYQ4O1TDD4jyiqWebDYDEHxqdfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj8oAPi2EQf0CYUOceZ90DqI4Oh4TB0i-dowcStoCGRLiA9cqyiunK8aAYya4h38XumcYm9SNXdo1_PY9XIy4miWQcXjOF-cubejdeYUSKK3046p25kbaaAR5Ru4cIPNHeY_32gIN1zsHNsS4Pudk-iGoQ_1IJjft8cYn436ZrxcrGoiQ1lY8YAeBHrxkphsE9qwxJao0wwzwLkgTIC-bpZmpDHO-mYB46_KsbGNvx9MSojlU_OKEWW0SXjG6yCKxtWqFayiGjUqQ21zgJOdsne4ob4KFrnc3wB5YDKl1zLgrrOM3pqGBwY2YPQnb91pKcfp-Dai6PoPkJlta7KaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t32oM1m8k6o8TlavrfrB1X1tTukTCUFgrjFJWMaVts8OTV5LLBkWf1B_b_yDziyGSuTKpFD7gwhY6LliuvnflXEjL6eQWQb-gsTSUBVIRBRsq5oud3mphV0eyLaQmbMAF9gez_oulquU6zE3tW3LoV2nHmgs-MAbY1zvZhfhm6OWwRThQHYFgAytYOtHwVo5fk9mkXCkjFi-JD90NVFqrcW_gOHKh88JRZ-EDp_n-_K2FJQ0ARbE4_vlGeSax8qqAPpVgPjvPXS1mNxpLy9ZJt_eYwPVtB5g9D9X7oGghWr8skZR9D-ChhSGTYKbUYLDot-I6gl_AlwtXonL6T-jpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26395">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swoM_8xnreMr8100hBOQH0ZfdzOHMyMO-hj3JJlH5qVpye3Hg3cHxJ_Lfgn6k866QraaqgGKAFl0FdHkhckQ0CtrMkMoDtXn8JT9MMidzsRzXIrAqQdW6_MGLcXLSFW_To5pdZcogqZqVmriF8tfaX86rzKGch2OYGJsD5Z6D3s1dXGoDvGfTeU8eutFUcTqb_S43zywa04SnOtHDw7aPgtJ-WaXDVgGrFVxu_9IKxxMBAGyk1ya6BXoBaBE0Ys0OXHoOdby9Nqdq8PCMqZ6iUpdn4GNKz1hXWEUxEsASThzCiAeGqSUIfcDc8W2mUJmoAj7Hui-MdqDJBWzaib_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
🎲
سوپر بونوس
🤩
🤩
🤩
درصدی وینرو
🎲
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع‌ترین بونوس‌های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r2
📩
@winro_io</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/26395" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrOLJ_HNg4QorUs_0hze0V7GxUumD4Mk6IRRXN8j4xRYSsSkz5lym47qtFZyt1EumjxJ0JKaHmQqVQQXc40XFXvvLKsMcx8CmQDPcFfJ9zSLSh_WTjVTmcK49O1iA6Q8yBg_FKogWyTyPCXzp1CsFtNPtW_htBHXXGfozXReEPaHOAmp8os9sPSOQTVlpPSOsqpbwd0CJSME1LST3VwkDaunXOWiO56JcvoBQd_iXPei-q7CGyHXQ1W6gh0YL8ze94hHyecWN_qdICdWBsd51H0vcUrzLUcWFfyjt3thFP6dKKIzs7RGjdM6nr8pBcCXRdU5tjcln8vRf6Ris68waw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pmojt7hyWGPFraUZ4q-FWXjsJOgd91WQUxO369ez33Rb6gD2plyMywgScDxDt0bA5ui2cTB4alkcCP0wy38sXSn5RXnlH1ZF8Rmgzxv6h_zJrC48bFG6hmmL_VZrO6H2mCxGMmIeERSFuIVdJd27rT_tjOsqe0DpsqF23Jjtl_1EQhE3PMI11qd9WKioLcOdYdRWv6LUSm0ueBSznhueh05JsIp23zJhepSvMOOgANLM6JQM6XOi-hbEPvAnfw5if1fOqkm9kIx09zPJLFGGBmz0YGpG6RR4xaJB66JAtTlhVrTNzYXJyoR-9VrWgfEuIRejYmDlOOzToLVjbxO3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdWUVoqjWY-b3rOEy7hbjrDruZjULMBKn5PTyDL-Oaca_wsMlW72DYYCjqyXhfZCYyEzpWINFLW4vJaM9XXR3VJnHNlM40M7McaSzVdalhNlXrrFtP6LG9JSWu33U3FQqNf2T3ZKOsp1N3garWiCsuqnunL6u-Vl6N3YEusbe0VbUMx4xxakNxPNSs54j2pUAYbD8HGjhZGbT_ids6s7frebdWSyF7CXXL6MIwyMqltmndmwLMEhwO_NYlbCL4zdCeRi6hDPoomVvD1RkAFNIpfLG-8-1jPY2fXx9oUz30JS2JXLm-lQpADs7HPrA6v53foStMFWQ74uoCovyZWBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDHQ7N35JbBIhPt3J6T5s89hTBNit8hUrYpHx747j8mkKwHe4DKMq_B_gCP_SVKM1mVSqtLtWAAKd-E5EK2DlbZueL-P8WyVDPSu-lwChAGs2gtSFAuTOXx7eQd8unl1Q5bqXDHUxk_BCAAcar_PJjzke0C_VsI5GBghvMnm4reOSztcPsy-5qXnLNvUILwwc8wsYOrIFmImJlFjlxsSqqsWfSB-hpOQ3hZVGo7J6k_su10j_aOBMvkOpVGZmdNNZREH2uzxbT2DObr8cH0G0fEntmCdyTqjLg6bb_JspT6MWZU4HcKRypmM0AFcuTR12MOSXWtw1PfmHfSOEP1tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bafI0AUhrdh4oop5OyTbv7ieB_uCy-vra3V3zR80ssxge8RUQFVUQK8CVNi_FUOSTbuoOG_ftvNFt6kKLFm3KIcOJsfeOxlkUfZMHTFbCN_epNp4krIoAp_M6GwX4eRUn0tGdx3M4WrazW7G0Z14qtA0mXCGmrbPDvJPkdPgD4aTnQMLcF5j11WoKhDcVFwJ4NjoAOEe33XAf-NLqcDTpxXlch-hXH-qwRqh9Oxqs1pS1wzCpah9DslGNdJFr751gzkbZyc7rTW1BTdSylJ7I7Nr4re1dDrsQnVOBq1hCJdfUnlpA4sSw9c1xcMgG6slO8jMTJsz27x_UXykWkEBwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-HGK8fXC8_8EyN4JgPJ4c5nh56YK5Imczf7Slekowi1oNOzZMiVVShjKTIdViWYfanMaHQaCdcT_poJpNXy4fX7Z3SqppAANWOIWrQybYLDi3tn164XBJ88LcVFWg42-uNsYm_pWtgpx3B2IrfDkigy7ZwhhythbNOyQ1IAkCOWnU8KG4cAoTZHFzqVo7TorH6Cn_F0N6uLjChAUSX2i4_POx1ZLOZSX1IEU5GadlW27CqBNLzQAIAV8y0j6d7FE7fKoD7cl6vtPA8uE_t2bC6WkR301mtpB6VDnsKDFPvkDJnOFBGU0zTu7EuW6BFrAT42eMLow2gJ9hq1uYdppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTqJ9chgkRZKg5mxehSFvGs_ta3VLcvUrFG2MITsDA2wBGNCZyU6Imum_JUBbeE4fHjCcpflaT2_-uwrC-Af-iOttLnJQ4XlU--eQO1oURBMbsxo09y3QCfFs0JziP1WnlbJl_UBaqVKMr2fF3YXHiakxZoVHR98c3r1mFGUNgZ0nXrr-EwAslHqksYfKhvDxYgDkhGEVIUQnQA6cZMvFxnhtussblLpAHqRGBIlc2DYKVvKBDsQbSv7DV3PKBQZnFB0nNg_49XhbVJTnVYG5Zi5GfMTjoX6tpXzVKPPoLdfGy7pQLcafAlt5-5HpYy9nSQy7l1CSc2WM7Q9a2MycQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDB-UUoU6kvIdGTeyvRitFRnl79klHv9QT1h8cpM08k-l2fJC60RheHrZQHYLzeJq_83wdytW073erZpwQqO7LwfGn8e0cB0KqXAJY-bIvWoSmznlpn5tT_PT8YG3pqVpDgX12cSY5mGawunreBB13AskehI2ovNkfb20sZlPNTtfkdNoEIlizg2jFdpOzy6WTMnCL6WIymXl5g7Ia7sEoVoqsq_jaVObUp_PwqV8biVN2VaSmGVEH4PmsM1q9VwVmG_eXefjnJogYYvBB40tq-A0_5LnklGnBr7K8zyMp-CPp-oqomtkyAuJ81v3I1CnaPGBTkzovqFNfKORAV23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STCix7UQleNaCEwRbm6zVQdaXo6pJ3mjEtKcnpmW4VL3SLuS6Ts6tGfQpfR0N5335B0mnMelh7hMg27PTZTEKgewp1ahitURFiz3oQ0G0IOXbKLgIybtVmlA_4iS5NinUFglTca8k1qVcFVdNVVKyq_jEopV3QVp-VPmgJbIdz7GRtan6RBoPEv5i_F2cGUEVf6uF_pQImWRJD1nkUct_T1UPGs_W5BxKqcXeoCfhX2drZdDR_9hpQZq2p5z7XNNt4CKFvQOPxvN5WWd-fAV-kN1kuD5gqyX12iOGipsk5YA1UEDa9xz4_C10EmOk01adNF-OXVBlc3jWk7WWghmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoaC0xkOp2Itn2OYRr5OHps5WDVLt7Ue-464SK-OlsK_SaMubqRsNjiuw8d9X9wYk6_VBEqmXxa6vSvpnNEKg7CD2YGWgv7zJWmKf6DsDHN8fTzjFkarOb_zsSx6bAm2yQO4tli3Eb35NuXca-5IAX5sqxNMMYkujkkyWappEhxU4xaX1OVc4TmIFDYbcLfdWYhCQKhvA1jJ4ncEaCc7TmCkCl-v7NqnGui3pYLTFBWTurOBHIqRJQEHlLcq401TmH1DsrGE8ocMsPOhikjnaBlXs4WZ76uSqcsdWrZRKQbDEdZXVLwWatQadSHYS51LEGveyhmNFcLwDMg4a0CGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBNHjvocCQ7GzuPnVvPI17_wTP6ZyGOsFje8dep0ZY1reympYfjdpuuYZAUzGSTuNMpebNDuGSsUXal9791UkBY6T9YVnDLFQjn0fUySMusGOjwF-UzhZ_PNHzuFsluIbe40VLwyrqdWP3o-vMtLlrWIRzrKmU8zQIYAFTR0KuqsUalC1eL7tFohPVfBalyK23X26_Hm8YdU8LPTo6vtj0TvJQ6g-11Bj2saaEjwhAy1LS9O2iqMUCMFr7psqPqDze9bGO_o3Rq5zwdc5qGdKWyYOjtfpF0PjGGpWfV-sqw_XiZISI9sK_DId9HxMyGP-tLY7NoyU0f_mPKIkdxqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=twe-Aal6lmSLjpEpIKVoNsvT40On8RkKbq1zuAtSJ24yszkUR0BOJ1dPIZTeM8kmDVmUpRJlI4AcEx5fc2qfgEhR-c2tYhGGV2kTYsUk9GEziCBT0hY2eePzgUbpNkQvUQhZZMzLwTJcwRjsmdBs29JYb-rnZWQZ_fnMkEAbAstyvGhQKrV9Of5EM9CDS7UNpCOJYyJ92fzPyJGADIe7MDyAc1yBqzhPFEuxDdJKDFha5k7czJPob8rp4Jt05g1yzt-Bki66WMK00Un7FX562-eTCbCEiSuITXo5Yu8BIXD6NkcgA8nxviwioLPeFbwwfEIYwlxv2fkOSlXAAYIBYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=twe-Aal6lmSLjpEpIKVoNsvT40On8RkKbq1zuAtSJ24yszkUR0BOJ1dPIZTeM8kmDVmUpRJlI4AcEx5fc2qfgEhR-c2tYhGGV2kTYsUk9GEziCBT0hY2eePzgUbpNkQvUQhZZMzLwTJcwRjsmdBs29JYb-rnZWQZ_fnMkEAbAstyvGhQKrV9Of5EM9CDS7UNpCOJYyJ92fzPyJGADIe7MDyAc1yBqzhPFEuxDdJKDFha5k7czJPob8rp4Jt05g1yzt-Bki66WMK00Un7FX562-eTCbCEiSuITXo5Yu8BIXD6NkcgA8nxviwioLPeFbwwfEIYwlxv2fkOSlXAAYIBYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHTWZYFZ5zD1ZWnRzLkslwLxINTQZ_jc9Pd06xVhj_Xbe8GOLlVxtMRM9pJj5IJhUJ4E8RSYAiTdYCgqpUFeWsZ2ADrkwIc8dbbKHpvnnNcTyqMKvT_vs3eVm09YFkNqWermI9e8wRKTNEHP-4YSZl7f2ZwuYPH0HMWfndH9XYd0J0fZaQoBd3i7AAnxph7zJAptF9_N58oGzYSQQyZTrkQ_HR_CBTCyZPPHkRb_ptQpX0pVVBXvBmoCq2IkWq2jXGKQV0cKLeFWKvZ3RmSkY6wqeqzB8mHUlgLMV5-0SI9HvJNF9C19HIKfe5FlQGeJRAFOILX3Q8r6CxZ_X6btEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ire9VSPqBY3GYMldU21AOm99mZbtV328E5wFi9VR_lHNwCvP0x8KqXao5qSXEvHOCTDCW9efg5ERg_v8aaW2flwkSBCsHh1-JSyhvs0uguC7eRooEhciUe-cwD8BdU5_1bngb4ZVw_XySIfyCo7D5vueKR81qkh061JxRD2phIrcX_WdKWaELe1BOaEohEBTrQd7RnlXqIeiDEIHwAHPHDRUQ-bN0ZfgLwCtJ9yRwP4qNpWSpC8x7ng5AT2yURESofn8WtKRuXpClVFbimiQfebFQi0XsgqQ8jEBOvt1C6iNvLGKsxlKIgr2QugjV1nqNwdHRZugssuwLwrp4YuqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fyf3LVEK4iLlQ78XC9DHqNFO5l_1YZBB0iBCFc_5sAGHT4ZVj6YpDDY2z9uK3_fSMZ-X_a4n1s00rxJBCj0YB0K5U1qGZrrq8u2tjumo0AJDPibTVFi-eseEsV8z4qGzstmvBetMpA-1B3TM6C-tuYNYdlQV7-euerhQdEvNd5JLBqvklF9p7AFQqxRmNUt8YorZYGLRhWzPs4qjV98u7XIDVt0lABn7sq7c7OS7U63J0HgP0jiExFh0_EkAuZBlmBrNN3BeLoTT8AQshfWSdQb2G4oWtAY3akaotzbVuMzJetR4zSusrZ1MdfdsC8jKYEfGJxr7bNSQBHvH_GLrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chOSnbt9t7jMrdcBmOuI4p4GWUVulKFcOzch2KNBcncTcYq8Z1sHh7HFIiObK_kcp3yCyiWuplOqcIN-ArygJlb0PXT8d8lL5uYts10KqOpLrGPzwhK7iI3arBnbre0E5nx8vO6ujHesNBN4a_FQLzcJq0Da1IK74A6hTvswzUYOrRLPCtMf3iam7jAOAvdg5_Y4icAFl-Xrvb54Z4tWtCMN1Z09WUvKNokcf1uSHvxv7FPcWnIbPg-unpECSBcj07L2tWTlhoqinjHzcHdvjNdLqqxjjqDpbruFWhR1PbYABW1xG_vO7CxqlvvcvMtRv8Pk9TL9rUVuNDzGPOYA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=jYWjwUze9EwEX9N-MAiScBfdzYpeZ0IkRb4M5_oRpGcsHQv78hb6gugnHl9w6KyCpG9AaNiNSHtgZqkDVtA5Nio5Z8SA24npmYuZ9UcNhmYCE94KGnh_ITVwd-o8fdxx5iY5wtwsohfL4W3oyZj1shzdPkSK5j3ARzLLKd615yC-GHs3JhDLLsrrH4DAJ3R2xLAdrurOuMHPceyLkh4v8y_1FvwIwTga43L2O0K7eyHvbQlWJOmcicm90zt9Rerfd7bu9De--3LX78MxXwxx6-mQu3FIjyy86Tyy76IK81z3m7mSui0sAU5pmYCOrzdq9aGxDLz7_BO0q4dqmfb0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=jYWjwUze9EwEX9N-MAiScBfdzYpeZ0IkRb4M5_oRpGcsHQv78hb6gugnHl9w6KyCpG9AaNiNSHtgZqkDVtA5Nio5Z8SA24npmYuZ9UcNhmYCE94KGnh_ITVwd-o8fdxx5iY5wtwsohfL4W3oyZj1shzdPkSK5j3ARzLLKd615yC-GHs3JhDLLsrrH4DAJ3R2xLAdrurOuMHPceyLkh4v8y_1FvwIwTga43L2O0K7eyHvbQlWJOmcicm90zt9Rerfd7bu9De--3LX78MxXwxx6-mQu3FIjyy86Tyy76IK81z3m7mSui0sAU5pmYCOrzdq9aGxDLz7_BO0q4dqmfb0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=tReC_iqAMh2Dhcb7mr1R1z3sPDdxU2EDGh_J2unvCqMMC7TLnKgUd5x76CUKuu0Ipq-VthzLPin6cim4duxnnRu_CZTvqKk5DlOge5nNl7y4ESH_orx02oKGmmKGDNYNBc2XFvRBEOQOZd7T_-y2KDLKYExBRyQXBp0wuGzPqNUrb4LfglmPIkiJUzuPOucdVpRIEli9B_yaW2wWFxN5dmjY9FOkpt0_JLtj3xoBhC6eDGcNUQA8e9vAhLDCMrt68NtnqMMtQ5SyVhqpCsat4drMsVzCMi3ABXm4feQ5FTz1DQ00DSbat8x-wI_79CX7TwfSzoS48eSCLCfqSjT94A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=tReC_iqAMh2Dhcb7mr1R1z3sPDdxU2EDGh_J2unvCqMMC7TLnKgUd5x76CUKuu0Ipq-VthzLPin6cim4duxnnRu_CZTvqKk5DlOge5nNl7y4ESH_orx02oKGmmKGDNYNBc2XFvRBEOQOZd7T_-y2KDLKYExBRyQXBp0wuGzPqNUrb4LfglmPIkiJUzuPOucdVpRIEli9B_yaW2wWFxN5dmjY9FOkpt0_JLtj3xoBhC6eDGcNUQA8e9vAhLDCMrt68NtnqMMtQ5SyVhqpCsat4drMsVzCMi3ABXm4feQ5FTz1DQ00DSbat8x-wI_79CX7TwfSzoS48eSCLCfqSjT94A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxup1R6uOgKsGrqptE3kRRbBI-fJ6ss4TJsnXNfu3rtieBoLBgyYZngo2jP7YzuqWjEUlfAW2eGOlmh33es47WoxYivHAH1vtkJPmCc7GwVP6qqqbvBvKel-xJqSP6JBLX67KInz78VcLG1IowsMY6L38RcgzhELNg9o664gPLCrTePdhNa0PY12irkQY4_riljRwvgI7erBsoMXQw-6AFvsmbVskK7ry6yxApRJMqiHZfxZ2KnOi2pkBWamffrGMq17QbPaajTAZFtIxQuSR0wttjzWafpIGrzFNmUzTV6Ak3Mg4LPRt9mPVFb5jWoJ5FSYR54Fcn6TRx-FRSEA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOaozIsvkTSsCcY3W2hNl3EH63tCBs2QJ2GDkfnXfyMts518coiC6ZCYRmyM3xLk2Sqr4g8FYwq7a9qusTzVlA3lFzOslPnV8RB7b6aKb_WclSV3xjoX9yBdpvzaHD2lVgJppRnEGiyYCD1kYKuApJJiN6n4msxxsuGxqTnOx1Zu3OkFUk7209CG6DP0KHOFCYL8AiRisfNKlp2ppMVn_CgZXMrFwmF0sE-XeQ8IgojVf3uBszjLRWZx6ny3ieWti0B_MiB7Sd5j06tD4bHwDmKYC-JLIOm6PspsgONOuLVCyUvlkSpiF9Y66OzNsS9JTfdZgnJpyZWWuWk-LBmJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uuh6kDsCfZoHAXKekzCB7vxvitITaKsJe9WldhQVzyM0lXeVcq9tlS0KVRJOlOQA5igFGynGfr0Y-7tvEHjt7cWSze6f82qJXYYghpZG_Rv3A2FrR7kdt1tdR8jfBxxqh-bEmCiB2Dltvb5n3Cb7CF-_iQmFshZtUglUFPzglsYq3JMZadMJzRgeLgXWiKskqaU-v64fL19tx8_23VW_t58UyKzGZR2WNfPgRN6IgNlVZAusLuGP6VnYv3zVoniJQ7DNs8wN1R-NTyQ_lcmwYhbeDDU9HrV2AJpIiiEGoLeGMio0QUhHsVPHrJIzURR0lp8sf5tu1OFs7adwl92g3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKOpHwStnorTiK4Z-SiQk3FqSMhPZj2KkaObMHwuXKbM-BtoIRixA7FNWDCNeymbMFp7THu0M8K1UuAN1Zo-hWv2Oo9_uJzjuUeuR8o3jhaKOKXHxrHU0szKu-XGRb3xDcWySelafIePI_hdX-z_cN2bpDsq9hQqa8TERvcnd9Zqat32TSBtowqewfrdOzspALGFRgEcHucS0SIWbdkFf7xhuArxAIe5wqtx9lLOHeEYeojC8mnTNFQkbml_gMSy-t-8R2DwbR3w4bNf5dgikTxEmi9p4wtTbhNWq8USU5IMGbvwsXgDJyOd4Io6Za3uuMNfIRr1mUkpIOy3cJ4QIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ0v9ovUfAqxqcvK8roBfrKC3L52A4UjnoWDdTInLl1ulSAJrq7uuXxUnftPpl-7MU3M0Tlza3W-sNLFG53yKIsmOOUS06xsU3DcjFzWkWUM7jWujsJQmBYuAckM1cHIa-5BGv2upVzmkpaUj1p6Xb5gKE0RS9QXlqZ7L9MVV35IV6Rn-BJAMTpCn-NbbpGypY1RSz6PbBKTflArbn3noadlODambS4r2ahEOqv7Q06Z9WAPgueWqrFKC4cbh-aGkAe3SuIMJx5wFJ3viBK5P-s2F6MuIPACDZ_4_0i6q4nmctjwhd1L_TY9NTNXMVl_knb_tId44kgZ4YB5phiBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZeTN5MrJMXgARW-TzZznfoYxqIrvBIIlOlSGc8scUPfI8-kED1v8dFpLJXDD7oqLx_dK4Keqgbi8xcVzy-eVlglEqwRyggo1ZgAQNKo5NK018vffRkcx6mmmz14N1ExxERRhbooVSLi5zUsGD3CCIfvbCZOew677OO4i0fP8hzn0eKy-21KBt_MTEb2mBqRSHf9JrN49ZdGBbZfDeOpgZCxNTy9A7kOJvYCBwoY2gj8y2AjJypNg54ownPyLvwobMkqqlUWKNFmOdeqzI0XBtRpj6YpRBuH1eUKLOtiq7gCFIswvLddm13YwH2zhbfI7Ddm63560i_JiAnsh2ADAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Jg4nNuwtWZ7HOpObUjAk05EC_1APtmdRdugAydHI2RNvFsDsNSO87ejxAbTdzaSeFfGqDWhqukqyZHg0SPEwOI_oXndmseMmuIMdQrzza_CVqxsPCZCvmAzOfLVOqdTkjn5kUtjIbNMEHb7VrdgpvO6bYyxcA6I2uK6HY5Hr1Q5EpvOlDaawoNY0wrAFSSx77TXOYrrEtfBe1g-sNRZLNjH9vjxyjrj4QVilzm9qsXFoo7L6iRsN_DN3Nc4Plb7RJxaxWII5R12Yppo57xuNLGaYZoldqdeuDHWa99qVUBKRan6d2dKpsE3SgvD7ce-WQEInMm7nAdOBhak_qOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdFwBPAmTSiZEgpavRRZzWR2na5_l6A7rkW7OegCTlXpaU8po4ir_Rk4OsBUJZdVJjycquv94I8oUq3aguXZLzvBhi-n94fW4bABu2UOGzeK5hFzE8Y1ajCE68UyJPHWpMuVNS_CZpmYfpkc9Pa0kjFktZHHHeHuqKU7mxosmgUAhI11EAe3_r61K7HoZUuySDW0rcMdOAcsPbWy4HZnQmgMd5grfzxQsec-SR7fMnRZn0MITF94WsV6-wGoR3iEHLNCxK54ieZMLY2UMU1ikzTK0tI9TyyavMELqJwSuni3-dkjAuF_672KYiodpIi1kSXoODJglIjcvr7Q2Nze3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=tyHMOQdAWycA6sTyxlHyo9ExOYKLa7ZW7L_g5yJV6H78ysInXpXmqdwVPR6D8op65f05PnsbUKywglaMwWOGrOOONLVVSW40_NX9lUPOEwjQSK7XdjIr_41M_5Ky5lCFzGWNTmlnnM30Ng1TFX_9z_CTJFmGiIKe0kBQo7tZlf4dTRIg9tydbyvc1FzY1TbOvxXnjt2iEl_BZHWSMcYoFeKfIWXfWOpobnmb_JXxZbJTJtk1TEcQfIb9GoFdJIjONRQo15LjVRICakaCs1FdkozqAYmKUbdu0pRxcaFlF99qKs2LWn7UvQ94F2d-b6Y6qRP5bMvxVz8eltNSz8xzi01I6pIOowKsPEEPARZFj3etff2UlV5FN5IMN8Io09KDibO1MC4eof57KmP2roqcgwQ2AsgE3muEwndaFmGi7H1LxPPC1FXnAMMNb7FK9X4o8p52umCWZnakGg7OeEj_q0zVdR8CoYEJ4oo5_ZpJmkENi8yMMMxeZ-WgdUCGezuAi_6K6V9TcJDoldRw3kg7V4OvbGHjC3SjucAOqfEbbIRvafrMngWJe8OVPuZdBasz7mBrmBC6loFkdVh1j-5ef8GzmT3ZMRySPPGhG_dX_Idej9VtmIRqW2Hd5nC-9tug1BhTCGTlSyw8UjTOfvseaM6ujggT-82ZWgWtXFadvBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=tyHMOQdAWycA6sTyxlHyo9ExOYKLa7ZW7L_g5yJV6H78ysInXpXmqdwVPR6D8op65f05PnsbUKywglaMwWOGrOOONLVVSW40_NX9lUPOEwjQSK7XdjIr_41M_5Ky5lCFzGWNTmlnnM30Ng1TFX_9z_CTJFmGiIKe0kBQo7tZlf4dTRIg9tydbyvc1FzY1TbOvxXnjt2iEl_BZHWSMcYoFeKfIWXfWOpobnmb_JXxZbJTJtk1TEcQfIb9GoFdJIjONRQo15LjVRICakaCs1FdkozqAYmKUbdu0pRxcaFlF99qKs2LWn7UvQ94F2d-b6Y6qRP5bMvxVz8eltNSz8xzi01I6pIOowKsPEEPARZFj3etff2UlV5FN5IMN8Io09KDibO1MC4eof57KmP2roqcgwQ2AsgE3muEwndaFmGi7H1LxPPC1FXnAMMNb7FK9X4o8p52umCWZnakGg7OeEj_q0zVdR8CoYEJ4oo5_ZpJmkENi8yMMMxeZ-WgdUCGezuAi_6K6V9TcJDoldRw3kg7V4OvbGHjC3SjucAOqfEbbIRvafrMngWJe8OVPuZdBasz7mBrmBC6loFkdVh1j-5ef8GzmT3ZMRySPPGhG_dX_Idej9VtmIRqW2Hd5nC-9tug1BhTCGTlSyw8UjTOfvseaM6ujggT-82ZWgWtXFadvBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unGyYLy6hAegd0GC-jM4ifYQqQlkZZzCb9wncQTe8psRzl2BzsSAFMoVvEoJwByGWwHoyBcJdlggTQMdrOTY1lumAG-Js9D7jhAm6qjtO-GB1csbCwnzHMtlJN0ERNFbGCBSHXOsCCYsQHI-H8X3w07DV0okDGKgw1oto6FD8s8NYdrutBDvt6OEY89QnQHjg5OUB5yL_0zfDneSOIY956ixyOK5Er8Sp0u5VciecC_InVnAMMEH0wCJrtgMQFo0cX2t2OdjF60eOd40jHkGuhAHt5W8HTljr7AeuUHZ752nDIPdcDz9w7iJl3z089_RHl4fHf3NNsjLbr_XTk6ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De9TkAfOOzAWELPk8s1n3Bpn-rH3M6TAmSpM6DvFF_mDnNjTYOXFORvp4SFJ7S22uH6gTaANKFEvGyaNmMf90DoFRdyFD9rYXt2J-A8EWQngkQRvFPmqAvgkU2XZmkRK2qM0fs-0PVnvxVg9pCV0YhJNGJYmxyPBVueROIM1uHvPmZam1CG6BEeosxPSnh3EU1Uk7T1nzDvch8a4HGQf-0WDH2N4RBxbmWlXnlt-crKzrgCGlDBwfDqy9QQxzFF5cUWBQtCZMlU4zLMWiR7NziBsDPCYtQZYnnav8BVb9CiHr0aaIBCsXJ1lqhdzBfIl0WDmTThLBgGgiraJaB0AeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwc-7qyEft1wT-ndxx_hdiVXCU0qBnUEGoxI0WeZ6DX8gpo_OdFnxMb0oH0SPn6vAsZzpyYRxn07UM5ZR_1Kll5C4uXFn1_TOSEiNJytzTz8nvnw3HICAIwgBDPNo0PbOM-LV8qHeN1w2moRgs6YX-WvqmrPSD_iJ1Llo5CHBdt2xvm6VIbE_oaCH81VP1u18fsIFF87e0YnEjg6bgHTI5Zc_x1EyN-5kKj8bBFe8qhqPzNksleGEhzm-MnhfGMJEVGe2y4i3AHcvVhbZCOPn1182OuBEHDhK8WzcVGeM1lF9mADv1iDUkNAShR9HqC3xh-Zx-4oF87zkNY23yBtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5eIEcnWQA65ZIy67PMpWw0HZnTE9hCnE8pQlf6JXJAuSk_YUw-e2_1AFXGSmjIeghB-LsQSdgnAxPL8ZBhgs-u_-accrEXlyVAKdZD8UIfXn--5X-kxSWnudiPIIABSgq9X2OqC-t8F6zsh7IEFbP4FpWoaFgkV0wmwOoNjwMhEUOEsA3V-G7eL11qj4lKo3MP3rjxqYTvy0HQZz_gdGtrNgtuJpJNDQCunwlQBRbPIjzYuAhDcEXdDzV4JPUTpNTKBmQk5CeqPuzfphG4DjFa2fqKzXgiaQWDPc4fPsiEzGLevtlNuwKyb1DakPfyvivAR4Fod7Vcu1JrodEPfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tswsxmnPB6gW0SLtPrQc8UCx2XI4mE8UvcZQ6787-47AMHxEFKgESesbOptTupV-lKveyGITX32U2UNblffmPHffOri-msBDFdKrw1dHymlkWnyP_xvvOQ-1liNLNKPChRm2E4N6f6dfiLxtULZxPrUw4gIN2XsVitpBvjT7lMyj0OTGFW72huJso61eAy1LajeRXBa7Eh8LVzzKljbYKjozl-mUZqEsLV6yFo7Xm84ufRrMvIuqZfkWj7F-Y2i3JqGOyOWrmpJ4wuvC9sdNANRH5b0SfJXfNIrOCQOqEnTiINsrAfaBV4ktgIMsHqzrBAbT8WkE19XHRhFYdtjzWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3aD-yQv_td-0dLRb9X9WPIU1t2oNZLJNoCX24ahDb3HpNmX_Oj7Wpn_MSEMAlFDF6BG8_5JFgREiLi9ZTMf2_0X43eXETJK8Q2jD3EBJq97ayIGPGcy43jXH-PfNqOxrDkBgrFc2OY29Zuuq3Gxj8KuHYYJc0l21B8w7fz2cva4xW2PjkRherWaBAFX4mO0q4bcqmd-z2-6WElQRdxIk09FH5ryCly3Flwh_q_tFSk2_7t1BqFbx8h80Q9zxG6-eZcYXqZLOyb0RMDyqA9wlKqpHR1HUhevAzQHMLH4vP4FZYbAAT-TbOwcAmaVyO2Q8Xf-HoyrW8k3LWGFkn_p5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqO2jwoK0cZc3hik18ZHZRy7TlgkbFS_OG1KUxBxZdjc6o2OY14MOWGbGyN-uUU7GpCNeha6OQRyhxtvc56EYvaExFG9CPHT1ZWVFBUETuNN0313Q7nvxfjLeeIxoGOV9nJ0kIfftFKITD7CcO5wyPqwFYAoiSteMomWVez1Ys2Y2cWEMRb3QoJT_cwTJ47_ZZoo3AzSozFObHeW-EPnhgbdhVXrs87JSLHYySMZzHcAgceiRZGWOSOrn-BUdhRBHUdKhvH7DAtlQXYUHG8eNgezi4XTIs9F43A-hpbQg5QcoXAc1WGc_CPR5N9XzoD86xhOMlRjDnuRmAaPvtMe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=kgdKe35U1HTFKrfD_qYsgKgMrDL2uNnldRbgc4XNjAV7c_LEMDaYsqTi2wCuz3nO85Kloxy2lbzg-tq5GoEyUBbj_Io5Ltf5m4vgRfO6LBMjXqMSQ1w4zSKOwl_HYFto2peTJ3O1FEoUcaIcaf-Qiz9mWWab2O9kGBQt4aJIW7RRS01gOCamAUt8ff3N59cIIueZWQq4m-E3q0npHKMg-eStc-vjpYtAjIzy5t9JCP9TeDFYM6n992_KNjM4dwrXVH7O7XIM5Ha9UT-Wg4WFYlW6yn83DpQW_7mYh8qTUEIXHl67_XvFpCg_ORT4KLM-umUEiUkyvd-7FTucIgKzjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=kgdKe35U1HTFKrfD_qYsgKgMrDL2uNnldRbgc4XNjAV7c_LEMDaYsqTi2wCuz3nO85Kloxy2lbzg-tq5GoEyUBbj_Io5Ltf5m4vgRfO6LBMjXqMSQ1w4zSKOwl_HYFto2peTJ3O1FEoUcaIcaf-Qiz9mWWab2O9kGBQt4aJIW7RRS01gOCamAUt8ff3N59cIIueZWQq4m-E3q0npHKMg-eStc-vjpYtAjIzy5t9JCP9TeDFYM6n992_KNjM4dwrXVH7O7XIM5Ha9UT-Wg4WFYlW6yn83DpQW_7mYh8qTUEIXHl67_XvFpCg_ORT4KLM-umUEiUkyvd-7FTucIgKzjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Fo6UXcc_C_Q99PwzYfF6yGXFDytd6aRjcbzG_bho51epeK0vR3kNRa70O22MXvqV1UPsc-qsYoszcLoBDCWsq8YAOZ8QaC6k8Cs-KV-UoOp8W-nYT2NHhF5bHt1VxK0SGy_I-xO41JvM75ToqNHwhgLmqOTtYQPbTmu9SXQw7mSleTtSuP_4P-vu4h6n_0iDU7NdiR7vDtksXgXV55o4XoAW_zwo-ezqGuJqUeXbH8VA9Je69rHSj4eQc7GTFLCn0UtJqovHi1Io-GXF8cW0jm20Tfxzp3im1PBWoC4dPgn2YngkrgCuUaQEI5PQh1H0IksSZxsBoDNnCi1wmwUC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Fo6UXcc_C_Q99PwzYfF6yGXFDytd6aRjcbzG_bho51epeK0vR3kNRa70O22MXvqV1UPsc-qsYoszcLoBDCWsq8YAOZ8QaC6k8Cs-KV-UoOp8W-nYT2NHhF5bHt1VxK0SGy_I-xO41JvM75ToqNHwhgLmqOTtYQPbTmu9SXQw7mSleTtSuP_4P-vu4h6n_0iDU7NdiR7vDtksXgXV55o4XoAW_zwo-ezqGuJqUeXbH8VA9Je69rHSj4eQc7GTFLCn0UtJqovHi1Io-GXF8cW0jm20Tfxzp3im1PBWoC4dPgn2YngkrgCuUaQEI5PQh1H0IksSZxsBoDNnCi1wmwUC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWxmBggWwQznbBepo12YLLjelbnCb8_hPGWlLv4mxlCm8eyxPWE-Fup52Dh7xwlt_2MNU09MgD9f9ag8CuR3DekXx0WQaHDy6x-nxj5E4VAx5PS5DrvFJWSUhCc6QUNWSnyIxPiIyY2i5GkLRdARYzndOUGrO07ZjEKEmCFyDs3_aceDPOqioncQOGSUvOx8KL9eS9qIWlXM5AWiaasqgwzqfjGZ5vviXWBB9hkHv6Zp2S6V200GLKu2bzdiO-POPzOoLZ4klWFd6_jcfBmWqHwo8Vz0p7jo8nV84m6PY1E4TDDQ4o2piifuFtMnXGws8vhEEwijGGkbMwrij_lHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3hsx-5lUESpKLQTlj8idWdTVFXDTttmCSflYHDt1VR3pW4QHnEu6Ww1cbq08CeE6BASxRlcPR6u8fcxY1dBfr3cdMGf7p9zJmim4TUKdi0BPkzD0ArX6jWQua1cnvbNfrLzTPbdHaC_4kcMC-Ab-gp7JjeqcixIFnK7Y8YtMs1UrbiPiIavuFhEi2MO4By_cckpWTZuGVK8TcLOc5c52CJ2x6cQzF2jGqHO6jGUA4CTlYNqUg5tJ7vBXo53s5GJ3GbGuVz8lXroHCHl4J645xR2KoCaStpWcHEHdZmUlMQjvxvj5-dLpQA540KTD_ci5r_x7P2DWMxQfoyHWSUc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgHSp4FQPT5edCGRTVBS4QeTExlLZg2kkiMvoQDm2_uQyxSODprtlQzd-pCi6KasAlo2-Sjn9XQBV7v_9JOuN41texcBtD0mxF_3NPzGZlgJlf9ewYGTkwyUlewLYA0NcSRCiBzKeQZEY3foULEt2hOzOu4rYOQ-3eiA_qQg2YraEXsmBFY9r5VKweY4xzv6Ecgewu8ELjD4PLf9XSMs7cYpjOyjjmGpPWYI4f4khLuzR8pRp5hz3ibNsetVT1slA2rPIPOYMKKiP9x1OhEbkfRdhhybMmvNDTLHmiDaHJd7wHeaMc9ZTVfjJyNzNI5yxza-O6XjFafkSXQNit4u4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voXfS-YhRjK86VpLbhCrWjLv0xUto9kt6PSW4f0w1YFa8cqfnJVC2FWSw9iSCD5K5gX8EDSz1VDmUcpSZYckxN9sTggw66OAo7EKuKUTzoQLw1yCaxGGHjI72SVtnBNyrZ-NtqcjDCG54ocXjsm2MgoM3e8FNMYJp8CsAsETzp4LN6AHB_jgapucI3iFqwigWBJId57BWwPRq8EJv35KbsM6SEgsab6KYdqhEBLraKYksZGVd5noXwQnPOZH_8si0dvIN4rOyrC3gDQgWs7fGrbiT-hxZqs_XN062NlQzuL8p30MthVhFoprZn-FC3-Rs3lC4cAB4KOnkH862ZgM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMxXLjP7tuytREexuB-ZsYJ_AP4kYCbL_4hqS5ywH7X1rs9yfAOHQ2FUhSfGXiw_M5YxY8ubwh7ZY5s9ff_DJXaB8OGvPIK-L6gueY_6Lp8C8D6TSrima8xIH0iTQOB3wSRS06cjrCImBP8iE4Uy8HfQKB6dP8-IabpwIsfSR-Lk3w1IL0tnvi8pSydox6qlYfD4L6Iz7toQLOo7csPZMQyFtpfinUyuXyQu6EKbavmONuC7bvW2evFviyfRlsYTWxpuXBlTb4K5y3Fn5uytp2yghYU_AAbqgpbdD_ku3OxGavlxdswnzNE2C2z_bTckheNvgrCRuwojdDgoDvFxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjjI4Sz79ysutr64hbWXUgDLfRV8pKIPaj7jOmtST5EI0FF9dbVJScNZgfn8EIDDkxd86CzXkXxkAeXeyOUd4pKtMX-CUwT5XLjaNqyPt32-shXraFYebK_PiDPtez1gaklRx4xvEfoCrUBQePCr5Vy-LXnyRhnQUobPM7M_BRkaP9tSTtWfMJ06NRH-Iz-vrCXoVWjJ-NFmI9zP-xbU9orxrcihpeTYSJBuEtqZIvP1aVrL5xTG9fSQI5G41y6TDX5SwYke_K0UVg4--4kKPz6fNQF_iEfyxRew7eqoS8jbBAkTCI5o1kzuw5CIe5sbJ5QjjfWTrNIyhNKRFfs55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJFb7yQgoTuZtg50X1f2eXsWSiBQM-l4suzT6WYQvpGGmfyQnXal3gyatBAFkg7CgxrAImcA9iRyt5TYOhE_NW0f4RFLtIoN9hH1l-O1pM3L7QvxKCLPAxfXlC2Y2EavJP3dvwKqC0iQiNHoqK_NmoMGurZfNss1k_79mwcM0xOkbLE2aHy1fO16xMEKYAK-xPiJG39_Ee6n7fTitxI_XJTHRDe5rBlgRHB-OX3Uv7bjxy15cBM7CbVdaOPZHL6em9RlcvqqJ3outtzMEweeLWG3ON9a1R7z6wYx0FdGN7hlrWNyAEKDqToiXslBUVAToiaLeVqd_hbaMqaskJtnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWagqnPWTc2Rgnz37aT8k3zGW4d1jGTmGFZ8aIBdnKLNywpsxBMzm5ruXOWctfQZdfNghkhiIaqThmiqEopC-AbRrqvP2cJMHnkbL2WJmCV03IEmtw8BhdBeQF0WtPlSRVbSGl7Q6cmVjwglgNRbZQzD2s_ayPwElYqFM1SwtQjF08X7AfneA-yb2TiBdRgdQzaM93xjsShm9CtK3imDiwF0PEE2S545TUvwancZBhRhq__XFSq3Y3t5gjBUHV9fwlFEh02jwT6USsRfbyI7_0FIQH_TCwRuc5kqGSCfSfK04aZs6zFPxGm1mLTluq8Daa6IzOl1k7E8X0aPwXh9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=lT9Ff4vYYJG9f8p2HWiVKKJAxp_A3bkD0nV1ij_AThBzUJlG7UVsV5odkh8-KEgZK7lsWFmSfNJ0DX--3aqFynhZ0Gr_KuBt4E1alY7uLWvo_oEcku0Es_HhtyNnd-1fe6oJMOW8UTqAyw3XJwtDnyCuyBAyeMpGcrFJKsLbWjJo21y2Or7aAqRjzG6ppeb8NtAeusM2rNZD-GD2wZ8Z9rcUF80w1b8tbjSh9k4XjWOx4rNCqw9jPyDbtxZG4xal-2dv1g5g-z_SJYXQmI0hpRDJovObcqFTpSyEMPjN29tCT5chJ_DCX4CaRSliSF6WTeD_4lSI8SNt5b7g_yHORA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=lT9Ff4vYYJG9f8p2HWiVKKJAxp_A3bkD0nV1ij_AThBzUJlG7UVsV5odkh8-KEgZK7lsWFmSfNJ0DX--3aqFynhZ0Gr_KuBt4E1alY7uLWvo_oEcku0Es_HhtyNnd-1fe6oJMOW8UTqAyw3XJwtDnyCuyBAyeMpGcrFJKsLbWjJo21y2Or7aAqRjzG6ppeb8NtAeusM2rNZD-GD2wZ8Z9rcUF80w1b8tbjSh9k4XjWOx4rNCqw9jPyDbtxZG4xal-2dv1g5g-z_SJYXQmI0hpRDJovObcqFTpSyEMPjN29tCT5chJ_DCX4CaRSliSF6WTeD_4lSI8SNt5b7g_yHORA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqOZGWiUSsTKHwQC5sB_khgQEj1I-qB4F4oZ3dw_6eLa1D5ECh4Xc4CU6yZlCwhPxq6WGHLmZs-c-an1SCbuZD3li0xHRqitd3HUhyJu64o36ru1yO6SN3tB5aJ-bYJ1xjL8R6dwQssbv47YpECPD4ZgblIXYntaItIHqepBjKzyNe0sqM9ZyFSgoP3b4StOKp9-XOFbcep3JTbFD3F3evxbCyT6FUIRuHvgv2DAS_x8pTVFTEkl-UssKeq97M9f9UjD9XwnOMS9It6Eeu87eUq1TVGOU3LEoXGxADhy3P_SS_BB8IBLmckJ_-cZkagf4ZNO5v0282wLRVIzaipoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=WP5cZfMvGM9T-_6xlIrPtU_D5oH9qVTGmzo3wWmnGet8N-u9GtguJKXOiB21rYTveNlQWEDdK5Rl-IMtt4KX5u8gsa1lggxiGnkNe-j2c2I4O3PXw2-eRb3HejzmNfC1wOrgHAIwVrBozNob6p2ACxRaCy-gaw6iRrjreTe3iU1sODyKxPy4pdsD97_0i7M7NY9yyXml1h4OZwB4oY3p_iCbLcTrVir3g1NwvSHXf2c7hDQ4Xc_l78Fy9Cc4sQ4MQOob7wiRPRzbtNyHsA7DucyMJWsEtbj1uTlJSXC9_iK_ZIxWF4PwBS9kZSjn9BbkmTaO6NkzsiR7qMqaRJzxVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=WP5cZfMvGM9T-_6xlIrPtU_D5oH9qVTGmzo3wWmnGet8N-u9GtguJKXOiB21rYTveNlQWEDdK5Rl-IMtt4KX5u8gsa1lggxiGnkNe-j2c2I4O3PXw2-eRb3HejzmNfC1wOrgHAIwVrBozNob6p2ACxRaCy-gaw6iRrjreTe3iU1sODyKxPy4pdsD97_0i7M7NY9yyXml1h4OZwB4oY3p_iCbLcTrVir3g1NwvSHXf2c7hDQ4Xc_l78Fy9Cc4sQ4MQOob7wiRPRzbtNyHsA7DucyMJWsEtbj1uTlJSXC9_iK_ZIxWF4PwBS9kZSjn9BbkmTaO6NkzsiR7qMqaRJzxVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezEvJTBJYy3r3aOs4sUW5fHR0DVs-KKxaBnM4zKggM1Ea0qZ2W706epY45ckIrWj50PJrwNwEl1iyu3V7yrXiru3_1mWP5sPpqPmHI5SNK4hsnnWBJJuLiJmqdBM_uhfYOOc3JOCHCa2JP6292jEuz0glhIpcfuZ5B4MmgCbJZPaxJf6OyubDYWCKloGg9i8jJfY2Nm718AbBn0Yo94Do-AsYeT4H55w33knxF-0Z8nOwxOKaQ3Igde7CuYzAF7BWFKmqwuyDMK6w09mL_vM84B-GeabcEXa-gdQ7l3WIraXc-BywwSSvNzU4P8ECe8bNL2jQODJtWpj9DeOQtsolQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0YfEMtBcAN6j8kBKL0rg85r5yLXXBw53KzHgkdtW_sPJ5vaM0Q_Xxu5hCTOjuI-Oufb1I7VAhiZR4OQdjFs2-lkJVDF0I5REU02uLKXaadiHklrUcwilAi-7Pagg2on8hq_lVrLyhlNTtr__rJZpDmG9G2k2z15RFC2PeQI7eB3eICV94Zi91V-ic6JvAaFjCdZOViVyZZYyDr8k1hFqbAe8eFkEcazAG5vPJszVJTTDXsg8fXO1HRoQheuXPNpzAMAbmV3aXaB7BNnASNKJFDshgSpgIvUh8gzR35UxYpPhGJvbMb6-03yOz5eF1sjdLT_0CZiQ1JLjc-kwzo6sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXddQAdZVQApQvtIKorUJwma3ukGAkc2TKOVFtyDSf6Fzg9L-wLgwlwthCqdXm36lE_eQk3I2gf-0ap5w8xTiga3JyUozxVfLM8Gx2J9df224UMQXDPCn2BoeVf6lDN0OQhwLIZ2EthakqAuA1iTV2fbXe7THs8jPsUHQnOQlpu9Bl6cwYz9GC9q3j8CsZduXQ7oJAHePqAmzaMy38bJXIqtZ4ksr1eBSuQBGm1Guq2GuBIQdReoFaPD6yz0MkxDwEetg2fCo5cfL8YxAhOLmAM0A8B1vjezRZBlDY7qqAKKD13XScSsA3yI2ao7EfIOu00X7w_XJSlZ0OROmfF2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUtGj9aFOnfv8NPzVoE1BXiJ2QjkKaKTesFgact94sBLEpoC-d2sqLed838eXhmSY7nL_a6jSq7gwWd-mgcUtwTTla8r_LPSh4CLqkGFVplgQPFApCIglplTNNluKIEXTSlM94FfZtZ23M0C9YpR5GJkLIHfub1FSu4MJnKSRPknjzXb8Fpu8MdUV1Q8XXYCKMSEsX5r4Q9qZtGSbXUyXNear6TEPHlA0oHzA162_SNxQOFH4vEw43zdFEu6IUmDWRPXEjiaPDiAy-pLOcres6WQKxiw5q5FIhlYbJ-8wT-NRm5PouWw9-aBcmOcBPd7LWwLk6wVf9sn_QeieXBALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3knMjHRJgF-dclwOY-xooqhZ07T1LK2Q1-V_YDoM0QBaJYwWUcibeQVGatf86NOwlA7z-7k_lQ2uNIsTUzWj89rihc2BTfgVC4PnGtm92IZkGAUj9IFz2s7CrpAG4olSo1_k8T-YaM941uVDhu33v--zMCQlVBNUrJ4QIJedX2GlJOGJzGc4JfV7PEmY_RBMYk3bwhjauFpqN2ImYH3CIwm_uxEM7lGELZTvejPzLwoAEwxOoQOnILEzGRDo4RgatkMGGpWJgFA3RLaF3bHyLX3ukRdDddwz3YkW99I_kfUutCYH9bpc-HIXpHSWG2A41c6cloxtLWgdmpz7uKDdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAtSJ56sD8_K302dHU9EdeoSu2F7_1-2Z9N8eTiD24icTgTh-Xdk8skxaWUkXHO7fyyePv7RXS5izFThvEdwHyOHKXmUIEz4cpyYti7XbVDOvWEfYQnYepx7Cy8rooQEhvXDklfEC4Vfm5ProPIYcHyMGZWxeQSNppCH549uCVhZHyr57TgNd0TBp0eKy6AWuIuR9TDXYDYTZJ-QRWnN3nrvrV6sP3DHuVOEIPU71tkylRSYCAOYJPEQkex4nWHzpGNTF9P18Xuxt42HXHGR58FIpZbTzMLBaURMOd3Adz1JRnlX2KuJpN1iMzw8xnETvoDWmX8smlGBtTWK894JgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=s-VQtnuE4gglz3XAu5H8yQSjqerkka_uqDTRVvq0VHywPomeXau9TKLR1cLg76Dhtvbtrmxp3lwdT8clGa7rYTY4vNAQHaCjkRlcCPsDBbtV5MFv-Srcx3cUuJumENXKMzaq1UCkLr2hGIx1ax4uaxrKCqwmVHdxC9eRTgBb8HtVDzLkX-7XzOL4d9Xua4ES9EaxZuCIpqD1mf6w5ss1iMh9Hy-rM3nupiB8f_1hpz86JOFWdcKlSMYToDhsDT3QWQPd_tqJtRLka4OB0llN5Ry905A5Chrt2OILx48eywrynLOJGvtfK4YfQgb-XSXs36WZNbfI1losUmumeVuVoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=s-VQtnuE4gglz3XAu5H8yQSjqerkka_uqDTRVvq0VHywPomeXau9TKLR1cLg76Dhtvbtrmxp3lwdT8clGa7rYTY4vNAQHaCjkRlcCPsDBbtV5MFv-Srcx3cUuJumENXKMzaq1UCkLr2hGIx1ax4uaxrKCqwmVHdxC9eRTgBb8HtVDzLkX-7XzOL4d9Xua4ES9EaxZuCIpqD1mf6w5ss1iMh9Hy-rM3nupiB8f_1hpz86JOFWdcKlSMYToDhsDT3QWQPd_tqJtRLka4OB0llN5Ry905A5Chrt2OILx48eywrynLOJGvtfK4YfQgb-XSXs36WZNbfI1losUmumeVuVoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2a6IFwfP4Zp9iNNBmNAp5tHnxH2KPcgicF7A-8biI4xwZfMO3rpbspImWsDutbSSgCCFNwX49tY9PSvNYizV9BLDuuwFK5snytGjRYA6oJS1vSTmpdiDRY-KXvkqx9_KnnZk1JnliP2WsSON3S9YAo_iMs8PX0w6q5RqELYhEmeaqIGQgzPEoS6NftFoHhZwfSKDoEHC9DE9aOw0IcVJwa7lkTLCLfjSzBhT7A6-CkSO6iQL1rqHmyB0h-biog9dpeQtlElAVMG6gs-KM-8TdlgrwasplIBsGyfUr09VNwGcpJTj0zH-wkESTomLM7hv0H1_SjToll79Q6fckbtBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_36-WzTceJ8C0TJk2TeuY5Z8TzLTwFgt949Hu3tXVMA5UjQrcABrTuifd3-cdjhSR7aWz2vDgsE58ZSrBSEc9Jq7qtxBr8W9QBKwVBq4se6XUmF2RZSbzriS83F90estio5jqRkkyc9TAdDf1Q5fWLpOYdGVs-Jp-juX3zg3U-2QFsT_LYZK7EYQEjEMDYfyOkmwJAuHuC2_dBCoUH6SqX0Q-fZeP4sPvjH053UtWkGfI9j0cExNVj7lJoXn_qWQ9NBkoToSLt91W8uK3rpIowGBZFbUJcHu9a5GVCs3kNSNKaoux84ZYosgDklxBsOfnXRXy-8jE_ReqYYOqeFUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tds6pZGBuv0AMiXV3AOXRp9fF6MTflsZCdkSMJzVQY4Wta3O8tW0tTCkWzM3z8oWEyyExvNh1xY8IWZvamc_ryxZLjt_ZH-U3t4TeF2ti6wC8m1EZ1jtfhRrRo_ISCoECt-p_YZAfHe4lLI6Q-IX-aWGOBUQCawe6zcYP-2mlPPF2fRWCXTLr7NYWJr_yPJ8d9lE9qEMKXMWyWDNkMZIJnD0oXAbAK_5aJiLmvqfxJVRNZIgG_FzRTmMF4k71Ic4SmdBB_zHI0L_1NyWRKTt4wfoDFawGI4YE6SdHdesaf0U3ip2V11Ue2ffneFgWh26ASY-yDa_qLY5xilaSYbOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR5wmT4z8-HhPtw6vhxXipgYQFM1_ylb3ZPxAYjN7fSKgyuij_9BZJhCv3QmFdH--XVbEIHZiCbGZLdTIDfRCA8OViCA7kdSuWDcXLA0gR0rHbZfgGe0qHGghaf3wnWb9ewsASCZkc7kCErOqhmjSXIcpeM-Pbl8bObGzvrpCpSyFhT_pJzHSNGJ6OFETefSLcKoZt6omxseQoKSJP7JOOXyJ58SOMwVeX9RLoVjwFqkffnZ-9M2sx5lzTcpHe_ZpPbq7XLAnkQtXsX88l5a_XQxrIdEleREEwEkZT977T61d1IDDB6StqGmkCRtSBLR-MFa0pyLqJzkB2FLDb99M7K8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR5wmT4z8-HhPtw6vhxXipgYQFM1_ylb3ZPxAYjN7fSKgyuij_9BZJhCv3QmFdH--XVbEIHZiCbGZLdTIDfRCA8OViCA7kdSuWDcXLA0gR0rHbZfgGe0qHGghaf3wnWb9ewsASCZkc7kCErOqhmjSXIcpeM-Pbl8bObGzvrpCpSyFhT_pJzHSNGJ6OFETefSLcKoZt6omxseQoKSJP7JOOXyJ58SOMwVeX9RLoVjwFqkffnZ-9M2sx5lzTcpHe_ZpPbq7XLAnkQtXsX88l5a_XQxrIdEleREEwEkZT977T61d1IDDB6StqGmkCRtSBLR-MFa0pyLqJzkB2FLDb99M7K8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=vdKOuOZzSLJv9bfeNBz4vg-gp8F2JW4IXhXVMzD9OJy7sPno9bTmVkDzqV6Ujwh8LOUQVwPeuiL85HCk-5Uk0UWWUNzG8KF42hAWirCeQXhmNIohtQ3SU6Y3dBM5l8QgSgeHcS9kumbdZJnkSZuYZHqYYZlJUa4bYaXINtsEMnJnxV1HqYJYeLN8_RsF0rB8a6lM2hPkNesjSJhaTaOg087jxbavqkUSWLyaQv2M4Yel2baDz8lMHWaMSCn5i6neEgGjzy2ZmBtBPTfniz7K6RWDANILCPtxCwkYBJcBArrsbqnPHWm7FoPOj0IaunORAzWsYA9uRKA2mnYgKs7V0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=vdKOuOZzSLJv9bfeNBz4vg-gp8F2JW4IXhXVMzD9OJy7sPno9bTmVkDzqV6Ujwh8LOUQVwPeuiL85HCk-5Uk0UWWUNzG8KF42hAWirCeQXhmNIohtQ3SU6Y3dBM5l8QgSgeHcS9kumbdZJnkSZuYZHqYYZlJUa4bYaXINtsEMnJnxV1HqYJYeLN8_RsF0rB8a6lM2hPkNesjSJhaTaOg087jxbavqkUSWLyaQv2M4Yel2baDz8lMHWaMSCn5i6neEgGjzy2ZmBtBPTfniz7K6RWDANILCPtxCwkYBJcBArrsbqnPHWm7FoPOj0IaunORAzWsYA9uRKA2mnYgKs7V0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=CPVLtDpItawOgFVJtCWx7ea-SwfTiOV5XJvOckTT5E5WhtfIwP58HFju8yk4gb0_bgp_4T34RF3VFYWmGT8MxQ0YXDdzZxTdfUBt6OUXxxwxRNcg_RtHk077bmlrCvGhPnyKcG0JpVAZIMvme8qHAdiYYcc6wCFl7lYcmAll3xCyr_YyVL9qIFQqkAg-FXD3rsGnbETK8cdj-Iex3AYLitagxToonvv_7lLRfZXRqxrob4y9itxL31WVkkl-t390JcAoG2V2aasZDXF26g41V7YmkLnl6xTIggJkuFOu66sizS-eN6bp_pguBTGKC1gWkdGvH72rVkbFR80tuufO6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=CPVLtDpItawOgFVJtCWx7ea-SwfTiOV5XJvOckTT5E5WhtfIwP58HFju8yk4gb0_bgp_4T34RF3VFYWmGT8MxQ0YXDdzZxTdfUBt6OUXxxwxRNcg_RtHk077bmlrCvGhPnyKcG0JpVAZIMvme8qHAdiYYcc6wCFl7lYcmAll3xCyr_YyVL9qIFQqkAg-FXD3rsGnbETK8cdj-Iex3AYLitagxToonvv_7lLRfZXRqxrob4y9itxL31WVkkl-t390JcAoG2V2aasZDXF26g41V7YmkLnl6xTIggJkuFOu66sizS-eN6bp_pguBTGKC1gWkdGvH72rVkbFR80tuufO6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=MIn4yGicSPoXcj-mHlxw5Vimw5Ax8E6ZZk5-L4DjnqXxGL6wVfVxoaTugfvsOhUDspuYP1bFnSXzqgY_IPhaD87bb8EfM5kDz9AdKNi9VRWQTfoyYdLPfbignyg4vMhKgEpR58KV4attQ4TZRQi8wRJeC_ZdEQYxicVMz1AQ5MbhISS2-vsslEjHDpBeBTWHN7xMKOssVa2M5FObST7WbFYRhK2CNEZhLhgKBqLviTJKBWpCeE8d3_uHI7bp5oNHcClQK5GyMuCQU0UPrX3dpOObjioLfAYLWvUtWgtDNvLSvsBVdkeoLBW1O2n5jJarEctmk_Kttj1Fe_fFgGJ-Oa3Rp2AKzKyKBaCB5sqY2GF-le5IRP8zkJ4UWNeZbkZiN0K77eWc31w0enJwo2H3ah_7f4ImuTLnGMt1f-Ppv7Xi7U2BYcrmFiWD8Y1QSgKJboLMCghJn9c-jqkp8VmqbpAvBydia-FkMAKuNP2b3cE5nDI79KokCZr8A5dFlTIXDP8GX3APi56VswrsGaaHi9Uvn7Wt5luj9PadybeKMfS-CnHewGGhfE1lEH-IPRvM3GdLuuEFW1_e4tYL06GrcpBKJECaR6gBmHhtlJlSXo_0_CopOQSmcUkte_OllF-FU56AABS1MEyyG-qwjxPg6_SXgtYoCHug9XzzJ1-veM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=MIn4yGicSPoXcj-mHlxw5Vimw5Ax8E6ZZk5-L4DjnqXxGL6wVfVxoaTugfvsOhUDspuYP1bFnSXzqgY_IPhaD87bb8EfM5kDz9AdKNi9VRWQTfoyYdLPfbignyg4vMhKgEpR58KV4attQ4TZRQi8wRJeC_ZdEQYxicVMz1AQ5MbhISS2-vsslEjHDpBeBTWHN7xMKOssVa2M5FObST7WbFYRhK2CNEZhLhgKBqLviTJKBWpCeE8d3_uHI7bp5oNHcClQK5GyMuCQU0UPrX3dpOObjioLfAYLWvUtWgtDNvLSvsBVdkeoLBW1O2n5jJarEctmk_Kttj1Fe_fFgGJ-Oa3Rp2AKzKyKBaCB5sqY2GF-le5IRP8zkJ4UWNeZbkZiN0K77eWc31w0enJwo2H3ah_7f4ImuTLnGMt1f-Ppv7Xi7U2BYcrmFiWD8Y1QSgKJboLMCghJn9c-jqkp8VmqbpAvBydia-FkMAKuNP2b3cE5nDI79KokCZr8A5dFlTIXDP8GX3APi56VswrsGaaHi9Uvn7Wt5luj9PadybeKMfS-CnHewGGhfE1lEH-IPRvM3GdLuuEFW1_e4tYL06GrcpBKJECaR6gBmHhtlJlSXo_0_CopOQSmcUkte_OllF-FU56AABS1MEyyG-qwjxPg6_SXgtYoCHug9XzzJ1-veM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=id4-P1l1zQQWbM71sD_T9D0mtEhsXCe6V9ISypfeujHmnN4YTocg6wmbo-3GnKHML1cM-aGDLJpzAOmAGYkWQg1kK3eQlv5m4gjEmmA_N_oskOFOBRFVZ4SIL1fzcpEwCmF7B3TEQMqRdwq1-URAoN92IQz2KK7TOjj9pGWODvR9v4LRPGIcUbz8ozJgESpKnErgqbN_Ur72GG4nFh-itvZ3DyzkaDlp0IDKAdfEBFB_YH2pI2ZR_WWGbuQuF_R5C-ujxBHBS3qvfzcfhifKijA0_QaEJzVkGqMwo3kzEAnKb4WGe4_nvhxw6UXPv5a217t3RJ5jPIa4Sa9IRKUYoIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=id4-P1l1zQQWbM71sD_T9D0mtEhsXCe6V9ISypfeujHmnN4YTocg6wmbo-3GnKHML1cM-aGDLJpzAOmAGYkWQg1kK3eQlv5m4gjEmmA_N_oskOFOBRFVZ4SIL1fzcpEwCmF7B3TEQMqRdwq1-URAoN92IQz2KK7TOjj9pGWODvR9v4LRPGIcUbz8ozJgESpKnErgqbN_Ur72GG4nFh-itvZ3DyzkaDlp0IDKAdfEBFB_YH2pI2ZR_WWGbuQuF_R5C-ujxBHBS3qvfzcfhifKijA0_QaEJzVkGqMwo3kzEAnKb4WGe4_nvhxw6UXPv5a217t3RJ5jPIa4Sa9IRKUYoIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADWIa9BfywoSfj9hPU5QMXNfcD1uGH9GsxSnxYuICvmde7eUM9pLyZQQi08-gkdzO_o5P2p1Y3vCJ_6uCtNw1EskUg4CAlQjLM316S9dAsJNqWkoHHQuIxIF_liyp1cqH23jGs-kEilBrXTXgU9H6Lg6Xe5U4KsOZHE3s5loyvuyXxApH5P-7AkvgguhohBq4xvxTnygV091h_zTw4OGjMA0tBfQOC5V15Oqgz0QY61qfO_cuhpHlPK3reSLv2lyZi6NZtleaRqL3OJOvCbaUnPZvNnhJZXuCM8ii9ObcKksZGy_GirVkwcN0l8gcVGvRMZyF5a_PJRTSIJTx8YENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=stBwLDJmLR45HQsuvaToZsJ5zWLbaV7abkmX0ziL_UJq1y77MINrU9AtIHonqC0J23Y7mI0ISX2uPckJazl53z9L8dto1ypPLB8_ALlCzUmfRDgbYDAL1JoTKZ4WJrwtH6FOkjl_0nJZQgXJoqPGeowFoY87l8d7yNflWZEB8WMN-pG_e1NA00E43TNlGue7NBlLK8XplpgSxKr6UmdXbUdwQY6N05JFqMvZ-nUGPVX3nJdDiU-TgeGlbEAeO-9ho_qZ0QxXlGWdbqfZoRjixA8PcW5x7RJ1y58p5ZNVu4tIXZAW3dukpL-6rZqv28KT_l5qE5PZVQChxiGIKlJvEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=stBwLDJmLR45HQsuvaToZsJ5zWLbaV7abkmX0ziL_UJq1y77MINrU9AtIHonqC0J23Y7mI0ISX2uPckJazl53z9L8dto1ypPLB8_ALlCzUmfRDgbYDAL1JoTKZ4WJrwtH6FOkjl_0nJZQgXJoqPGeowFoY87l8d7yNflWZEB8WMN-pG_e1NA00E43TNlGue7NBlLK8XplpgSxKr6UmdXbUdwQY6N05JFqMvZ-nUGPVX3nJdDiU-TgeGlbEAeO-9ho_qZ0QxXlGWdbqfZoRjixA8PcW5x7RJ1y58p5ZNVu4tIXZAW3dukpL-6rZqv28KT_l5qE5PZVQChxiGIKlJvEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=K8dyMMV4JLH9BglA9fTsGRSDr0Rc2bbOAi2TpcKIrhDvq0TgGNDwRVth0WY-l1paoxUJwPBAnXOzdYQBLsSwO3U1DTGxSqQ2QqJ5IGrxKwwwhYFj33kJUPA9o7iv92Mhaor8AnFNsiczREGjvptp0wXTsK51kF7CruT72LSJ3NS_fnwwhK2ZCYJn49edr-v-JW4C7wuMet2Fls5J-S-HM88MQfJE-vgE1spYNd1UCoMoPwL3UVfBA2F1PEAq5UHhwrfTIcRVML9oZyb954bNdRzQRjUFpuo3PSWBiQizuKcgHYpBBFBLFhuSAfhv9yToJ8-MMk2JB8ma5rsyB874IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=K8dyMMV4JLH9BglA9fTsGRSDr0Rc2bbOAi2TpcKIrhDvq0TgGNDwRVth0WY-l1paoxUJwPBAnXOzdYQBLsSwO3U1DTGxSqQ2QqJ5IGrxKwwwhYFj33kJUPA9o7iv92Mhaor8AnFNsiczREGjvptp0wXTsK51kF7CruT72LSJ3NS_fnwwhK2ZCYJn49edr-v-JW4C7wuMet2Fls5J-S-HM88MQfJE-vgE1spYNd1UCoMoPwL3UVfBA2F1PEAq5UHhwrfTIcRVML9oZyb954bNdRzQRjUFpuo3PSWBiQizuKcgHYpBBFBLFhuSAfhv9yToJ8-MMk2JB8ma5rsyB874IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFms7LjXKsxrYnTOb1I1mtincx4swfoFruO3_QE7TONFszn3f6ormhjCs4VEf129Ts6LQI1_kBE3wHeI2Lxl9Ljx3IP3n_NbkvmHjLAApz8v36bMl3YDR6XDCZqWW5LrYzEsIuXGFXXhrpmIQl1gvHRyvHqklPEHpnnn7ZrTHzFb02m05cOT-mpDl7z60v8Aet1bE8NjVM3rlmO7G0DYIm16BfJUwB6moQRdX4XF03l-yks8i2ma3jCnwmJSZsoKulnFVvIXBooi3KXn4nsCoQqLxs9W9o1lDaQ3uH98mDEobx-3MCed9X1m3mk0rzXC0uT-g43zcVE1mPFqxrzfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=TnY4OZbzaZY5wLD-YSjkzVxIX4Rb2hLeVGQ8-0jJFnFvoKCJQwM-lvSELlIBNq9WGPsAZS3hMfZe_rb3PFRLmAQi2EdQlAR7yFJ6YcO0eRuHSynspmkBKsKy0PonAfgnMHwchz3mFRqEi46EBRDLBKB0L0IB3DAK07UKWQe17dTn1iVXUS-BlN_4nDQ8tHe0LUMmaZAMx4NkuClPaFLldMaX40YrupRPIEUKbcYSA3ebsUKXYO3BKX92ZoC-FKbDh6AS0gckYXow1P37thGzrM2e7Mshp2Zf0vNscFTVVP7-64b5zzrfoZV-_B7ZNtCK_q1weOb6RRz4QmzKSVYkCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=TnY4OZbzaZY5wLD-YSjkzVxIX4Rb2hLeVGQ8-0jJFnFvoKCJQwM-lvSELlIBNq9WGPsAZS3hMfZe_rb3PFRLmAQi2EdQlAR7yFJ6YcO0eRuHSynspmkBKsKy0PonAfgnMHwchz3mFRqEi46EBRDLBKB0L0IB3DAK07UKWQe17dTn1iVXUS-BlN_4nDQ8tHe0LUMmaZAMx4NkuClPaFLldMaX40YrupRPIEUKbcYSA3ebsUKXYO3BKX92ZoC-FKbDh6AS0gckYXow1P37thGzrM2e7Mshp2Zf0vNscFTVVP7-64b5zzrfoZV-_B7ZNtCK_q1weOb6RRz4QmzKSVYkCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjloQiVjJgiFplqg4K1oCxkUDTohwDMSn5yMXMeGbBqxkrJTKF0ACvfZLraByYBBZBFU3YKcQ2xw1yHxkgeB4cDNt8x65if1J6Xihq6AOjPkdOjOHKX8x9PUK4Ov7ODRwtxn1ULIZvRsj9_AX4rkJePlwz8uzfLqqnUBt2OMvrJM3qEKyf8GkWfDJd5v2pWDnCI_b3Gn3iqkstJpypAN_qEybtQ3Kfir-16A7N_SBkeBSNEop_UqV7x8M8b1aiYw5c9fLmtxwegFXM4TEdCqRyhBsvQnjd_Eo_4rUlwFo0IO1iWzCGCMzt5eWXnCmmc0Rz95Z3H0RyVkHupIf79PPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6jhqdlu3qYNbNbMhTGyJ6RjYmIChz1QKz9VfJ3aroj_K7fFc2daYUe233bKEi1-iSKcnPzhl4CRKS5A3PA3Au5h-wrjrOJEDa-O0Zg4UnTPq1hIzaeSzf5_KtSHP1Hb6oztY4gUtJCcQGB8_87_DogOHcSJfLCMjXcNyZNUvfgfyR3uUtA9l-Phzh9x7vxsyFUjQUREFB8t4JqKAgFEBfXDmfJqT_l7DNRj0B9cy3yHrpJ6T3MRcD8m1ZdQ1HrKTNEG4beBpC4ec3Z96Dkm2vbwUInVZTDSDucBqT-P1WD5cazh03hkfDp6WpC5B9Tk5fgRufJYWyg7eXIWq5opAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCXzpVIf8HbHLy2yRBF-EtVu4nzAE_K-Oc10GMkL467JEYQnZn0sQu32WneqXEXU36dlducYY_gOWs1PzSmTNtIFyvEtRuboUIj_ykuUWHymj-W62GPPT1fBNZQF_Xr82-V9OjoWALSIQ9ZOz9jDJQZvaCKHHEcm3-tM_8jVxq7Zirzf471BMsG8Patnu7dEvNUOzbjVGce6cx-iMJ7Z8Xksa8M1SJFPPbHZZ7rQNVwtSMLSQjrhiimuMa1PFaGG75RtZRMobtctuQ3PCOmogzfiQL4yHzxqKmhK6DvSx5dPcsaJnJon4NuqIUBvgwT3mMWwEZ5v2yNSt5x76v0iJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpTvud_6tvKIUTr7RVfxbn4SCQmozCbExsjOLV0gdXzqbxflCTxt5-n-nYTgeGvqExBY0L1eg-km4_zkOt0G5YyhDzgpa4aoy5CzbsqUKQ2eHs0G1JIUNii3kgoal4JnmWXmkAjJH3G5oZyzSuuPu5Ersl9nTQVSwfnIk1rZ5x19Gg044UZzDqTFALeAbm-SE_LjtnTRUM2bBxYxNlyJ6glCVKPtUXDD6kJVKi1BkamSWED6FCHwAuoHuFj1HTzmW-Cjn1Bm5dylsCy6hCke-h2y_yRkw_FjCZCaBAD8XUha-23gmp8v-hki2dxdmuTiFUakLcLPa2OAnfTfqQVdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEBrk3N6HSG4m0KvZ3EeFueic-vVYMMXsrDU0x-BRdZD3K4OtSGDrHHcob0bT1eilzCRE9J8ytqFbdOZRb3O2-pnHUmQzd66kBqfInyR7sGKeo5vTmtQ049t79zGYP-8trnkMblhPIR6hf2n9d_dzrZrxXeQOrdlfNYmSIHcR-HZwsfdafi0ZnyEYWYVnN0IzM-Z9h2A607WjVbza1WFIsRAs966HOqXmQEGnlTN_CIkIOOD1qItNpMsfVeQ8W2UQPOgS-CwatOTCsqbMO_uLe0SvZmRoTQtUqY9p5SKyoN5YomgT7Zysrmto-tvFIfJW00IWv5V_0oJ1507zjMfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjvpaXArzsze7ipUoVQJdqtah6UCTcMP0oso9t_hVWNCsa1TTD855RI-zZS5nCqbVah5ts7dmTc3QtHp4MBERKvcTmrwcNikBi1e2skgGKLVrG0BK-y1F1QETDjAQqUyU3iZvlb2WfWhu-594EwNoIJ0HqoLbhnZ13umzujbi-HldT9XI4n2SobyP9yPSqttfqIevstWmwX7hPtHOHzdJ2VVxn2VuVZ2Ua_wU-eAxNL9I_NuWWwJynircJIJGl68bpVWWEM_HeeJ4c0BK89jBthJCmT8JMV45TaN8iBwdpzCYiA6r8aCMGuYm4hEIVL8WoIfAsMkVzO-S4TfCqBMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVICzD5ola5vbQ7atW5MrkhBU1yoq1tjxd0yYmWLo9jFqK4AISr68XADqzkk9IPafYgJiTUfUtxqpAQAu9bhE3G69vZYVOm0ninFDCYZ0gdGQm447W7DlTDWWW9kR4kDxJuNfpwpKlZdRr-va6dLEBfLwUlWi4LN8NOQqgX5uWyphmuh7TbKA0kdokuMQ9XZF3lsk-glgd5OH6J0eGsHue__tc1uUjaIao3T_4rVKEhwdCRm2aNZr3bgRlO2MSJ1qNCN5PTjZ9ijuOwp6Wl1eqQnVGlPkl27VC_wygKZMmfX3-3BIv5urw6qcnzXnZtS5bN3RqQb1231RJL47ZT2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMe6FVOEKJNJeVSE08ECsHqjuu-FQGP13PXCwuOXDZWEgX1jf06csNIxSO5TDdsPED9MLpmGNSB6ue-PnR17_2lSBIqvg-x4I038Gyd-3ShK64GkjBLRehXkdsXsWeHPfjSjo0aq6Jf72Y1u-JiVeE41pPQV1MBN5UCzOC-3hT43zI1sT2TEmWvSDU_Jdu-VXYTD-ThYzLX93MsWLiDU0tN4VlTxXdTiR3cQfdfhfzcNju1cDg4RDVJFtcNcz28SGxRAnbxpT34Q75aJiYsR3ftUKAfU9R3LxDZVKvpJJXdWQeaDSVxFU8gLn3aL3aqOLVM1H1lmTKbs4S-MpPMoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkFa3NNWYRokowYfYLEv82Cb57I8JIeiqARucT6FTIo8OjJS4LMkvfHlYzpVjKTgsT7Z5rZHMv8o6ZSsAuOZCAY--RnOIqIgL1vYD-9GNFrIGRZdl520YDWkwbJF1umwemgDyogmxsCwnmFk-vEx16G4qZQl_RG5KSHMYRM0MtQyGlTE02zlyKEYujMZmppDU0wyibwsEQDTSUK7NSDuGQ-xRJRB55ovLPAJaYc0METjhDjymGYeJpZYuC-F8qwf2rUT6HpQZd-lfsQLQ-4ynsS8q1C1rCCRoaUJFXwav_Eq5f05dbZadMOTC0WdxMK4GZJN3gKLoDvkeIFwpIYDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl2CqOSzP3lSy5bElgSrgJ0-wABilm8Zpeh1ws5PCUzgfUTIIBd-4qNKYr9H4b4f_Sv72V3GG4ZdHVXeuMkqbWgqCtQYpCiO1VCvY0xGpCUexsgaRHCbzNeuS3moY7M1hpDg5H-YVewbCGJO5fD_H3MuvS-CaMQQDKkiKvgYBnh-ALQCIICkGUbOYjHFXIrPslgUoZxVQIB8bjGmMvf7OjEQqJKSC-pMWC63Kvybbp6y4SGfNZ5WEM0tkMe0DvcS7QA6og561hw-liEkLiRqWVdE_FzyKqbsycf5pGPbMMrY5vRHy4GLWeEyL7DFdjO04kubcOs-lRf0n7Gg4it4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1yjuNyClLzJ60auPK7xrEBJvpJczXxkRlIyPZIGkgVUGLaHZygUz1hxRSY_DEtC3zToTqtoQfsNeZnC_HqFHxt182gsfU0gkiq3tBoSz8BaUMOTTKo1dAoq-rPl-t5l2iSxQ5uDOHNTNcpjbTqcFFxKW_z4C1ySuUCkDiQIwyOn2twUHY3Crbv8Nc15Z6S7vgrMIK7_1sQPE0BJh0ij9GrgCxZG7YQU-fycfgYgatw4FpBK7on0xRiI2Ul4Rm2NbEUzPvafdqfTRwI9zWpJ9FI4S3wt0RZadM-GUI8NQi_JLdIOLt6ntEPpZB7iks9RhKZ7YkU8BTKlqj8LQT-60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmsxrqnhhDn-GFObNvIoZj2djfO1BXUNPDvovOXfeSye8Kxw7oTtNHFy8NaCI56H_Q674bb_Lb4P5zQ-Lwv1eKTW-uNuLR3jzTa59PU_KLh4-3DTllzGyoafxUu-fDxsuAwLVqAAi_5_hpwV8PPDRejA9cgYmslZLbeBeSbHY_1e3bfO1SNhmAAkRIzNhp9wc0w3A4rJZy7TtLgJ6oTCQszIpu0HnbJe6ANhtfFUXg6455GM7iD4PXMS9ZqKC00iZsezjCfBR8wlvTkUI86r94TzFPJ_OGpQt8gJ7ARWzW6VlCo4_o0Wy2N26NhOwjYFz0Mopbz3Pwl0V_9EBJLrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=JqQZPlOufz1IWW0_7phtkUK9bR4L4gZyLVANEPFPHKi_OtAQCCiVeNNChzf2k9hQvsSu_xNgi71jCTPzLk6x41mOBqRVlvdbUdBJobkYzDMhNGf6ffPFdWuCTWdUy0ANWmGCWXfUeHDuC075iO39Sb_kyiS_YYjLMB2CltZJ7JeWxyfbxFqVnb1qny4wrmaI3EQ1rTFnqWdbibAEKnyrfqpjhcvWTfFWwydVWk10EEG62s-EfqVcRiNWe9iX_B90PJ5yRXaydGNvDOwYq7txdYjl5ycb3BxEB5qp6MNq2di7SlFd6qSMJSfTJrxJLuayvAZR8Lvx0rAIY3rGKanmOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=JqQZPlOufz1IWW0_7phtkUK9bR4L4gZyLVANEPFPHKi_OtAQCCiVeNNChzf2k9hQvsSu_xNgi71jCTPzLk6x41mOBqRVlvdbUdBJobkYzDMhNGf6ffPFdWuCTWdUy0ANWmGCWXfUeHDuC075iO39Sb_kyiS_YYjLMB2CltZJ7JeWxyfbxFqVnb1qny4wrmaI3EQ1rTFnqWdbibAEKnyrfqpjhcvWTfFWwydVWk10EEG62s-EfqVcRiNWe9iX_B90PJ5yRXaydGNvDOwYq7txdYjl5ycb3BxEB5qp6MNq2di7SlFd6qSMJSfTJrxJLuayvAZR8Lvx0rAIY3rGKanmOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=E-dvMTk_j0FlIvytNqKOx9IOA25WncPAY9DdeDfNXhqBtJsz20t3jHeHhJrG1uvIA-NdbgMsyrDmXdJkhQ1n_EBSqDHA2kcx-_d9QwMz45Jj0C1CdhdrsaY7JYbWsVEM4ueFjMWAWdRZzHYhQXXOv0Z1RGqfGQqb7kQLYs10q40kcvUearVnOhenS4kDyA-kACQC3lJ11nkeS0OX3hsJ7ozFiGzZBMiMUe2n0m7m_fdTcUqpWVMgLV7B9obA3lL_HU4fvmqrDOgdGilD-QWSW60wAE-35O1R_aPF9d4mxFlH1REiRl86MchbtjwvIaG75K6ZMW14tlhOdjLPisM7Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=E-dvMTk_j0FlIvytNqKOx9IOA25WncPAY9DdeDfNXhqBtJsz20t3jHeHhJrG1uvIA-NdbgMsyrDmXdJkhQ1n_EBSqDHA2kcx-_d9QwMz45Jj0C1CdhdrsaY7JYbWsVEM4ueFjMWAWdRZzHYhQXXOv0Z1RGqfGQqb7kQLYs10q40kcvUearVnOhenS4kDyA-kACQC3lJ11nkeS0OX3hsJ7ozFiGzZBMiMUe2n0m7m_fdTcUqpWVMgLV7B9obA3lL_HU4fvmqrDOgdGilD-QWSW60wAE-35O1R_aPF9d4mxFlH1REiRl86MchbtjwvIaG75K6ZMW14tlhOdjLPisM7Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq4r8FVUkfRJyOn_RjN85aBERQmvKx7zPKPh-syX2kR_OeZJnmuiYUjE61uFxjg5bxh7vzuKmpXcWQKoOGmC-yqMGIeLZbe6UKyBZ8SlzKvKzV0VJnvQJfNZR9prNt8R3qxXMT9vB93tyUqr9N_LiOTzvSA1imsZDKbDEcBcKIeOh8pK5v4OekLJhj4NokZCT0E4kjF3HKn8CO6X4meJpNIslRx6zfBXruuLosvLatLf24AONFt7YpyiypLPmacbAgr9jDJeiyShWzDZP1LvzQQhNK04T3Q9E0tmoJFpkxQUO5Bmp-LEWbFJfSdvpGGGyEPpVM5hGMTaGz2hNYKuVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFTAdY5O9bcZ16pTAilUb6rUZJTpihTyamdG1gqjkJ_QaCGJC9i8XYQJAF91Zwrp4GBjHf-TUPGbPSSd1YRuWuVqXxkVPIoAgriT1wU5Cb1AAwnEf2NYfyrCktHqogHiOAt4RAxSDU6f_kAsbTBT4aELjUTedYXTm06rqplwRVwY0oPWuUuXrPO26h4Fi7WNnBRiFnCacsRh9bv8z5sPOItTFE1yiwIDWDGdoksByI4U68aX8yQS6JDT2tuf7Qs8l0J8eHIEALTsZso-I0-F0x5okfyOEDHAPjuT_7mu5ojDeK5Jdq8JDcnlDN1153UylCuS3NglS61t60YvIx9sTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQTRT8Bv-gLZhhemxnfkGfRL4spwscVHsotccqNZtCAfd5cWbLyFqwccADE7cxb-bKxUsgVE7xuWs7zmjBLIp-QdtLwvZS-VgMW2tWVUJMlS7vI4xZ9QmvYdhhNdQfPJMtnlSeFIqYPMBZ2xzwzjdC62gIP6BMxYqAoqJo7dG7a9H0NMYdbKG9CAbz-4GLjTau4vHRmeDZpPD9FhlAmBbZhPwBW7UWIQUP0xs-KpckFwireIX8JYeNct3H88aJZXgEjgA-LdQvfBCK_OA8k5CXQXQhO0aOwPg7hUcIS6XXYQoVEOvv1EZH6XoAHekLSSHP_K0b3EL00JKPcsnknXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOPbhJd_V704BFOcIOTsEEJaCPKkbRLLXxIJEDewZYu9Px7L0pMZdMD6phb8E7hs5CTPRcQfB9jB7prWUn3Wb_6erWSe7Hum2VSCsNPT9pEjFhnxGHmBHNK4NcQGVz25tVs62UUeIPYmxP6ogy17KL8UPE8iQTr95jF92WchM3QhTX_mAqU5Z3-3ILIQ3mnOGfKeuQ0cscUSEIEyXg2KuP7P3A9qASlElSncrjcj8gIE0ul_gL7azgZcRHENtB3Aj5bpJmwiG1wXsXShLZQRXOA2vEK7-6jHpdrysVHricCVXsRVLTyquerfzXZfL481wCMYpjvCX_lDOqEvO0y1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Giup9fzULZA1yIXCVvAY-WuTkdAYO3ykzj49IDCHk8_9NsPVHwb70VjNW5ZXwy9g-5N7DMZQS0yef1a3qmVvYxekvQ87v8wEBC_UUJjd49KbSDkHQLu26VsESrkBJw_5Fi4ErP1-sNDYcaECPLkcqTB3bZjPe-u1FuF8ZeVn2kkpeHNvZAyK5sEHiW09_s-nnGndkLyKEmUuk2ZIXv_Ia3cInThYJ2maD2l94Ev6q0YWXvNIO6wctjOnMEx7edzeES-JRF8y-SVrhcLmdOSo9jopl7LH5nOm9e1cfSKICo7HNRPbx7J8ekgdY4OFP7G2nZjtiHuxjnDPtlTGHM7vTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhAyBfRu2tzI4HXCTowCkJ4tW9dX5nlwOA1rt8xiUblTM-c9CQn2wLAAj0kKziyQDB8GACBjF2-h5Eff4y2zM7m02p2abZL6E4ef-turnK2ARLf1mQ6ryT6jUes5rYPYpMyE11E3aycCQ1qDmB1pGIpry--wmSjBm_zryM6O_eUXCpNzf-S9b8VW_v9CTAqCBjNdrAvWOrdK7lOaeNvIj-XwFJYBW_9D9ZXxlp_Nh_7xxo-hoa2a0CWmkHOTZvgtB9Uy0V1uABJfKehFLLEG3L7vcEiouzWQ0oR9Z_N0PFjwT1ixoDwTA81lzF2D591s6c-f37CA4uSZrlwIY88hSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ro3YYDnpFxM6a4H1N7_OHjXHdH7UOf9UiDP5VwvpXlpfjheZXY0DyISAZ0KRclXPLu3FePRFiDtS1Iwdj6NWtHowf2eQdFbkNk44HPMI57hlxaGfA-UX6deA134fvjYuX6mshaMr_6njVnmovtsqxkQpHT4TTI2RKXJsEkAKf1OT6OrImGUY-F60TUoehgP0NQFY1tVr9MBReQSsRgUhGCyQWsnegPyEB2AvifpprFip1gpDRsiQsvUDxYGDDJt1NaESDWe9LfZc30VhNa96rQn1f4CCDmQKExK_SD1Ty_Vp_xSsI4skibAry4TiWqqK6wegbEEccE8YBDc1i7740g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
