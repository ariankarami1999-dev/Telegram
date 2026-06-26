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
<img src="https://cdn4.telesco.pe/file/GF-xu6iFIVpSV9z7HIaSBtJY3D--QlQqFiEHza23tlxtv_Tpy5G8oEHBfyyYCJjUl_o9zS3IeFkpcUukoqxQs8SQoZ4G64ApaTyj5B2pn869DMyhC7TQn4IJigR3dSW1KURFIRfTRP0c_yL8p2o2uB0BcA4aSA_gAIUP03zpWQTCKbh0WS6c5mufhtn0vtGB9l8SAI-FXi_KzKEY2_nIRZYLakqNt-XU3tROjkshUmDk4Jm7x1-E6K1JtnEt-AkSVChHQ91qxDQpTxKbfvQbYuRzR9FcZY8KByvn-9ZZ2VJxErCIhzzfh4UcQV3j3pLC8HTbrgrXOk4G8pDhycXnag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.28M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 06:03:55</div>
<hr>

<div class="tg-post" id="msg-663320">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB-DLqyoxjSmhk4qUCx-KDCr86CleHspGnGlQITC4kqnVayka4w5vnkfM4pYf5Qd-5S35XDS9xgs9HhdGHCeiHKJ03zz8b0gFQDQRF6DAzKw3s7gfHIUI2-wUA6iE8Fs24noJGF_oVAhNUKaVLgJPmbCLnQHfJJGXskO-4bE19j80Pkst50c7j_XbK7Q4MgZ7QziUjymUbSeJNO8KDBhNJlKDQEwBcqavqvlpHIQGgE7R4ca8mjOig-Fgf4TvxKl6cd12EVju-cCbGeZ1Aq3AIOvOVnBzhRODq-xtgbwSgVs3sTdRjGHz47UyNeY_r543ACrcv8ZH0qHf5JMeRGTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بسیاری از کسب‌وکارها تصور می‌کنند مشکل از تبلیغات است.
🙂
✔️
برای همین مدام پلتفرم عوض می‌کنند،
✔️
بودجه را افزایش می‌دهند،
✔️
کمپین‌های جدید راه می‌اندازند.
❓
❓
اما سؤال اصلی اینجاست:
اگر تبلیغ شما به آدم اشتباه نمایش داده شود،
📌
بهترین تبلیغ دنیا چه ارزشی دارد؟
🗓
موفقیت تبلیغات از طراحی بنر شروع نمی‌شود.
🌐
از شناخت مخاطب شروع می‌شود.
📊
سن، نیاز، دغدغه، رفتار خرید و مسیر تصمیم‌گیری مشتری...
همه چیز از اینجا آغاز می‌شود.
🔽
🔼
شما برای کسب‌وکار خود پرسونای مشتری تعریف کرده‌اید؟
⬇️
⬇️
⬇️
مشاوره تخصصی تبلیغاتی</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/663320" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663319">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db555e92ee.mp4?token=phoO7irfU-3SDLwIaJYhlK-L64y0QaB_dhje9GuVzL1cGJJeuNqAC1X8tLXT9ZEgwYOeLLka9KNi4Y5JQSJoW-OeaYHweGl_MuR8PijdV2IS9VTwGh3dLGorF94c3TWhLKsjC7xQn8FumBZu_BcdpbXecqnYefgL2onoINPBTy-gp4hTnvep5dVo5NxXC6b_AQIzRNEi7OMaTV2PJywfQP2q5jfF-OMtLLOWx4HJWEKVBKTF7RgBol80aDtomtf0uRF2-RRQ8RUH9O4fxGEM-xIByCHkGx7pbcCgycgTtodVb77w11jmVKmZA2-3crxBPbWpnPOzqkElYtIubh0Wow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db555e92ee.mp4?token=phoO7irfU-3SDLwIaJYhlK-L64y0QaB_dhje9GuVzL1cGJJeuNqAC1X8tLXT9ZEgwYOeLLka9KNi4Y5JQSJoW-OeaYHweGl_MuR8PijdV2IS9VTwGh3dLGorF94c3TWhLKsjC7xQn8FumBZu_BcdpbXecqnYefgL2onoINPBTy-gp4hTnvep5dVo5NxXC6b_AQIzRNEi7OMaTV2PJywfQP2q5jfF-OMtLLOWx4HJWEKVBKTF7RgBol80aDtomtf0uRF2-RRQ8RUH9O4fxGEM-xIByCHkGx7pbcCgycgTtodVb77w11jmVKmZA2-3crxBPbWpnPOzqkElYtIubh0Wow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لپ‌تاپ استوک وارداتی
-
به قیمت دبی
- مناسب برای کار و تحصیل
- 10 روز ضمانت برگشت کالا
✔️
-  ارسال رایگان به سراسر کشور
🚛
📌
مشاهده محصولات</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/663319" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663318">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔹
هلاکت یک نظامی‌صهیونیست در جنوب لبنان
🔹
رسانه‌های صهیونیستی خبر دادند در پی درگیری در منطقه بیت یاحون در جنوب لبنان، یک نظامی‌اسرائیل کشته و تعدادی دیگر زخمی‌شدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/663318" target="_blank">📅 00:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663317">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yx4W7OlsvK-cRlJhWhtqYdUvjBWOukQTltSoOSB_pdExwOsA1ThGI-e-LWrLpcvSKfz95wQD7ottZVXXE_oZUznUMe1kws9jC86nfFmzy_KkY40gKZ_n61MHFN4nSSyi2HfVKrCmTZ5UWf2mkxYaCV41mjhqP2zUOMJXgCbVSImeB7tvEtxbwiBf5dD0hc2guGsl32OpjGWnXJesTW91sE9bMMExA8BFVI3VmcOZwdD9JpwQvWtk9bEPsBTfGzgou6WlFtcz7ntJA1wsOUdqiMy9te4b44cRpdfwzP1EVVjSoEN_YRGjf79Kk7VN_91wUU8e31EAtyiVMZBhw9d03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تاوانِ کارهایت را با عزیزانت خواهی پرداخت...
You will pay for your actions with those you love...
#WillPayThePrice
#هزینه_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/663317" target="_blank">📅 00:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663316">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2457382848.mp4?token=YxXd-LkriFKxSGSfVd8uL-zJ6JzN5R4kXkL4XdRnZXPsnyTjLZ8vyNkJKQv6z12J7CKex7AawLTwIvK66LWsZH7OvkDMPw06ys91Ji92bUuxLrT-9oEf-571ZAAprEaAtim72PtuoSowGkIMrd0iKmlH2eH2cjSQlaiUZJC1H4egSPD3afT294wcjAgmrws-K-tozItc4Qq5Hq3mKsxfSXYQ1RAABudYoKrW1V7qdpuD-c7cx5b-nTHXXukXeIg2Y0SLPNEwUvx4_8o2SqeQcIdDpNwPMSbHbwWSyeafIpp7n4Y4ML158t6o7xRSzdJ0tFtV22Vk3InqpFTfrBndBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2457382848.mp4?token=YxXd-LkriFKxSGSfVd8uL-zJ6JzN5R4kXkL4XdRnZXPsnyTjLZ8vyNkJKQv6z12J7CKex7AawLTwIvK66LWsZH7OvkDMPw06ys91Ji92bUuxLrT-9oEf-571ZAAprEaAtim72PtuoSowGkIMrd0iKmlH2eH2cjSQlaiUZJC1H4egSPD3afT294wcjAgmrws-K-tozItc4Qq5Hq3mKsxfSXYQ1RAABudYoKrW1V7qdpuD-c7cx5b-nTHXXukXeIg2Y0SLPNEwUvx4_8o2SqeQcIdDpNwPMSbHbwWSyeafIpp7n4Y4ML158t6o7xRSzdJ0tFtV22Vk3InqpFTfrBndBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
چرا دانکین دونات هرشب تمام دونات‌های فروش نرفته‌ رو سطل آشغال میندازه؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/663316" target="_blank">📅 00:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663315">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0062b337.mp4?token=uvryMF8VlFGrStaTg9SRXYRSadwSHqmep8_lhlKgc9uI_HT2Jdkz2uGh0TKOepHh8G_MZXPeO-Ljj5xhtIKOqKMNnyLsK-zVgIgoGCIS6-Ayivw6zLeLF36XOpC8LS530rkt2xpoZvQyUUPBoluMr_PEuXZmxScPkHK7tHWrgNRzzTDl4SaRQauPaVUOjWCa0xu_zUfebuXCGb9ttZQLVseRrPbFTE0XwJMu7w7YdJHgr2orH2hsQ01fhy0J3yOMjyAWRtMpNWP2npOZuTu4b8kvVZZnDpDbYINtiKevPbyJE6HUe0FpCUz19I6pd8LQzvTHgRXkKVrMptc2aoA7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0062b337.mp4?token=uvryMF8VlFGrStaTg9SRXYRSadwSHqmep8_lhlKgc9uI_HT2Jdkz2uGh0TKOepHh8G_MZXPeO-Ljj5xhtIKOqKMNnyLsK-zVgIgoGCIS6-Ayivw6zLeLF36XOpC8LS530rkt2xpoZvQyUUPBoluMr_PEuXZmxScPkHK7tHWrgNRzzTDl4SaRQauPaVUOjWCa0xu_zUfebuXCGb9ttZQLVseRrPbFTE0XwJMu7w7YdJHgr2orH2hsQ01fhy0J3yOMjyAWRtMpNWP2npOZuTu4b8kvVZZnDpDbYINtiKevPbyJE6HUe0FpCUz19I6pd8LQzvTHgRXkKVrMptc2aoA7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شهید حاجی‌زاده: قطعهٔ شهدای مدافع حرم صفای دیگری دارد؛ ان‌شاءالله خدا ما را به آن‌ها ملحق کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/663315" target="_blank">📅 00:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663313">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRQwyCG9KwOo5KZRG5L_sqd6-TLA7P5k9uSAqa1R5zv9B1_dgDcz7tUMvaqQGElbmp6Ik9uaVTR9qNAx_l4EXqciiEC9wxgpwYZYNZP0wMF086gyMyoEanLie6Ha6TvE-zcdZjUKgLoKo4S9_Xyi_a_Q4akS5GYiz2CuFEJsmr3FCRkQe7dGmSKGZf-HMwcQ10nmQeAf7PTiOsNRiU18r8Squ660KrlvQTgV9ZipKAoKZtaxGb4OI8L-cpGtHr2Yv6L5wVup_Jh5adMZX-Atlivntp0fwKrveaxx1gLVxDCSJULTNf2ig-ftRHrjyUjQo5S8bUgZr6vdxLP6Nov8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyErAp9ysG2CuFCFyv4hLIXl1zbkvnq6sIDuhy_QKO7dp92zrZmQCaFV0Ap1Uc4kpWzfEvB2NJZzbZY3Vuy1BEqkU3E1CVuncuUp30l_RC4VqZkN0l3E2WJTEFFNo7nv7zDHmU--9Vif9OAmREgA7xkDZhVPTdBO_yGq9GZwJAP_FfNDO10GE57fp_sRVN4mJdliaQHSTnff1CQfkHR5fNmEuHVimtny038-qf6B15oE9IFBc0BhcAWhXZg5HLJzFH9u1mSR2LTp_S1M2xUCFsf0o5sTCMZIjjM2jPXxNUAB3HP5zkTYamPFp7P1qo5blOz1bAbldhQ2BmUNWlAUnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
حضور محمدجواد ظریف وزیر امورخارجه پیشین در مراسم عزاداری شام غریبان حسینی(ع) در منزل سید صادق خرازی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/663313" target="_blank">📅 00:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663311">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMP3ApDFS7Am2Ud6f79TpelUvst4UYpMIxW-p5ks74ExHJ6Kux6fgJl69ruB8ZZ35SHzbDiHlPz235gL-QE3DrsLIeG1EBwL1hHGe9qb8TTA4txWbk0onTL3VG9tEh-h8-0ek39Drec_9RbzwOOVOmQEu9Sl3ne_T5O83PtCv-AwZbmhhM2x1qq-t8PR3R9DSqPCmH4Y7GfwcgyEwYy1OuXVIrKrfRAbZX7HcYRxXnCRNUPqDlZoJoJq8sPh6NzvKjHGex2-GdlnwOytqDGa4YrXCYmz55iXmBkZep3hmUohe_ap716h-XKN8SDCauZf9T4ADhf9Iwap5Pgt8xHXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
رهبر شهیدم شاهد باش هر شب بجای شما فریاد زدیم: مثلی لا یبایع مثل یزید...
#خونخواهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/663311" target="_blank">📅 00:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4wh0hy0TBKt8Odl2Dj_gmjqPl5SmkepUKC5Z9_sUKVMXjOz1K5bHmgHRcC58F0a3RwKzrSIlhxE5VLmRpvG0ptQvQO_AJ-pnK1SJJEO_4URPW52pYz_X36P_COlMfU9xzjYoAH8E2lCsz6ORCkdxcsnBDw4PK3rp5Y2o3yJcdldVKaI5c3ncwe_oJgQJjiqM0GRfNkScax55CeHntSOOMco19cjti8P0Ro_BX3mDSy5sDwnqjN5XEllaMhTubf2g9OB2vvE4znohyGivgUi88JUMW1bsyLmZeSFC3_qtTtfW_WIW63xRxZrt5N_taKAwyvns_hWGbna8koFmgjLIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/663310" target="_blank">📅 00:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663309">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b38bf7fe.mp4?token=k7LoM1yWnysw-uHGpEMvtTGbjJqNho7QVL2-nFDgR37gCSbc9bbOU4mhxM3jzrJrUg_gq0vC6Dld4tssSXWqol8ncecUp44he9j5VEzGlX6lgzK77tj-dOue8zqiRS0tgwL45WoCU93DMCXamGp-9bH6x1GKAZp-VKpRu9pKDy5hLq2bnzp_jlBbuISk-FGgzRLV5PPwX3xO1K30bt3-0TjWxi3-U_AzQQtYD1UKb-jfwfsi20h133ScrrBZ0f8NNHeCacMWUMhJUVzraVR43GeCDbcNV0dzfNkS2XaLHuKh1oxfgHigtwLFW38GkkpJddrNE4Z0p3VmPcgZUOz2kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b38bf7fe.mp4?token=k7LoM1yWnysw-uHGpEMvtTGbjJqNho7QVL2-nFDgR37gCSbc9bbOU4mhxM3jzrJrUg_gq0vC6Dld4tssSXWqol8ncecUp44he9j5VEzGlX6lgzK77tj-dOue8zqiRS0tgwL45WoCU93DMCXamGp-9bH6x1GKAZp-VKpRu9pKDy5hLq2bnzp_jlBbuISk-FGgzRLV5PPwX3xO1K30bt3-0TjWxi3-U_AzQQtYD1UKb-jfwfsi20h133ScrrBZ0f8NNHeCacMWUMhJUVzraVR43GeCDbcNV0dzfNkS2XaLHuKh1oxfgHigtwLFW38GkkpJddrNE4Z0p3VmPcgZUOz2kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شوک بزرگ برای جامعه اطلاعاتی آمریکا!
🔹
خلبان جنگنده F-۱۵ ساقط شده در ایران برای اولین‌بار فاش کرد پهپادهای ایرانی با چینشی چون «عروس دریایی» و «سفینه فضایی» حرکت می‌کردند!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/663309" target="_blank">📅 00:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_-J_YhV7ok4Gs4n1u_SxwRIQw6JnzkktPlqOouZXKypv0UMeFu4GnmcR2IVKRNc5a7HMmfCW_uBEEqWNoXILxpOa1BCGe08R7ofJvqDdVu0rH0Nk3hXyhtw-OkBkCNgxde3v4KWu3Bt9zCla740hN7Hd4u61MpR1NT1y3CAqvOJAx0GWPaE5tAcgY1zKQNpcG46UwXlgqFrYiJkFs5kw3gPE7ne1g8nf5oJVdm80dCywzaG44Hr2xrT5YtUiBHkBn20j0CRQIrEbdEJHPTvEbeslSFA5o2RYtVXhId2LYzc-waCyKCQRzml02r2DaHQagNPk9YGFh6B9WGAX9nEpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WhW8YII5zeq1xgTL6_bbHVOagr99ZOg5iVOJJxQ7tceYj1noDHru9XU4L9jAoMH4tXNIyevcIFTgQJfok-gXlwb7fCe5a-C-D5Y6OIx72zRjgOoHM1SVi17Kf036nFaZ7x97j4ZLiuyAnU6OBILsXBJfcddbljHBSci39oCFo7iu_-VpQZDMY69Ev0tg5EXyGULjrKnpIV6xO4B-PfMQED6CePU18mbnSVD0VfTd2nrAzNsLGN4ZfKUQIAXB2xJMRR7MVu29-kyPVOLNUUbH_comwb83pIRM95x69VoX6ehGCvCetkNuPWoidt7s9DzX557BRRr8oUuuW0WBLKVvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwk4Kxeh6x48REK58CBuf2VqYNDvX11B78eXaWigHGbfMGYZs7An4AEhH0O5I-NoAwWSeKhlGgvjc3sHnOk9wQRoJS139055RusxRIvf1XSjES_gaQEF-XsF70MLN3fQ5RcAEm_g5qLtbQ47qckbsZ5Tr3_ExUbf-wnxZnXub_4D3IoMSCJJUsm7FrjBksOfsHWUfJ3JX-5Tmc3_LVyNTx9sb2v5sCJB0VW5-SxIcYRjPWVyq-GBcxtt4N8E7xivg-Y8RJk7H_qQNsUncwcK8D58f-tF12nq2mBnfMqu1N_SAvee_rt0OV34qUVlmx_uyUSKOm9gJEWn3UWqPhbLVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصاویری از خرابی‌های ناشی از زمین لرزه پرقدرت دیشب در ونزوئلا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/663306" target="_blank">📅 23:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
پاسخ قالیباف به ادعای خرید گندم و یونجه از آمریکا
👇
khabarfoori.com/fa/tiny/news-3225621
🔹
ادعاها درباره حمله ایران به یک کشتی در تنگه هرمز
👇
khabarfoori.com/fa/tiny/news-3225665
🔹
مرگ ۳ تبعه خارجی در ساحل نوشهر/ یک نفر ناپدید شد
👇
khabarfoori.com/fa/tiny/news-3225565
🔹
ماجرای جادوگر غنایی که بازیکنان را طلسم می‌کند/ جادوی سیاه چیست و چگونه کار می کند؟
👇
khabarfoori.com/fa/tiny/news-3225623
🔹
بازیگر زن مشهور جان یک مرد را از مرگ نجات داد
👇
khabarfoori.com/fa/tiny/news-3225534
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/663305" target="_blank">📅 23:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
حمله توپخانه‌ای اسرائیل به جنوب لبنان
🔹
شبکه المنار گزارش داد که توپخانه ارتش رژیم صهیونیستی مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/663301" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
پرواز مستقیم تهران-دبی از ۱۰ تیر ماه برقرار می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/663300" target="_blank">📅 23:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔹
حمله توپخانه‌ای اسرائیل به جنوب لبنان
🔹
شبکه المنار گزارش داد که توپخانه ارتش رژیم صهیونیستی مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/663299" target="_blank">📅 23:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc8fba96b.mp4?token=GJ_-3zDwAliIZLFRtLiVsXlASBouqTQFjG4i5phMwIZ8npCs2l77KYfGBjHL38VY-Tt6vm6T1CBmjoRN7KpNyl8wk2LLcFZVgl2vXCfnBzZgJol5mxowKa_iXHNgkGXrdbzVZ4idjNtjuGopYE3mZYDKsczv5bac0kG-qu3sb04cuNkPSScy4W-XN3Q8TzY5hvEnmVG3mcA3YG-dzCrHzXhsCk1KLVEq6Bp19IrItwv7Tz7RM1y7cs8_MljZR4MIodHaRv1o5DFF1mKGI9Sp6nsgtFP4UwBPup1c_YPHmYknHpL1eg-7sn04SszRx5H41gwoGPqQ1nlITAXaPnf5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc8fba96b.mp4?token=GJ_-3zDwAliIZLFRtLiVsXlASBouqTQFjG4i5phMwIZ8npCs2l77KYfGBjHL38VY-Tt6vm6T1CBmjoRN7KpNyl8wk2LLcFZVgl2vXCfnBzZgJol5mxowKa_iXHNgkGXrdbzVZ4idjNtjuGopYE3mZYDKsczv5bac0kG-qu3sb04cuNkPSScy4W-XN3Q8TzY5hvEnmVG3mcA3YG-dzCrHzXhsCk1KLVEq6Bp19IrItwv7Tz7RM1y7cs8_MljZR4MIodHaRv1o5DFF1mKGI9Sp6nsgtFP4UwBPup1c_YPHmYknHpL1eg-7sn04SszRx5H41gwoGPqQ1nlITAXaPnf5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویری از برگزاری مراسم عجیب تعزیه‌خوانی در تهران که در فضای مجازی پربازدید شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/663298" target="_blank">📅 23:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109eae93b5.mp4?token=IeSLBeOx7Z6EpvhBgFm9Lb12MJfG4b1raLojfuubMkLNHYrNwtaIbvQpsChzbwrHF1fREXZFyQ-Asf_WTOVSS5dAJcn_K8cA_2fpP3LJ6qrfZmP2DRyaf2uOZef8IHxgspFtkEHoR0AMxPiqN-6lEBjPf-RHGvBWOihCTI6yULdBaYxcaSmkjkbwAeo8KsLbZizC3M5ty4gYnbRAkyMqJGJa-9Yg1LZRI43j-C3jHUm4sNUT0ffDawKvf_6vy5rylo3Lk2-Ww8xwHNWa6_STyFJVrECc8oIKMOzC2vZR7w2WQF1F8qs-wN4X3RHuq8vKyQ-fuRbliFMOT14uoriAaQl1f-3u2tJpGcdhKT5I6hf21CcaQsPE3x5DRqt6S5lMxi-abs6N2Ah7oGYBYz-c2xztpa6S211J_lNsisN_jgdK0RUIV0U6LHWGsvZgxP6ED9LrE4XNZljDdfSfJ-b0jrWp43qZM4QX5Unb1XindP9ge0RdBR0NKzJTY8UZ4NNQVx8t3Y2VEAGDfQpU3wmVZo3azaQe8NmRqAfuBoAd-sQvt7HztHLBYfqpAXWaosH7uCHmHraCiuc0E1e2Y6SG9bXGJroYpJ-mJ4HKIs4z5xrQ5So7o5OtdxaSoqnJRJQklZ-gO0p6BdM4YS5R79lqWMOd6rJsQB4k4HV6GAv3KBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109eae93b5.mp4?token=IeSLBeOx7Z6EpvhBgFm9Lb12MJfG4b1raLojfuubMkLNHYrNwtaIbvQpsChzbwrHF1fREXZFyQ-Asf_WTOVSS5dAJcn_K8cA_2fpP3LJ6qrfZmP2DRyaf2uOZef8IHxgspFtkEHoR0AMxPiqN-6lEBjPf-RHGvBWOihCTI6yULdBaYxcaSmkjkbwAeo8KsLbZizC3M5ty4gYnbRAkyMqJGJa-9Yg1LZRI43j-C3jHUm4sNUT0ffDawKvf_6vy5rylo3Lk2-Ww8xwHNWa6_STyFJVrECc8oIKMOzC2vZR7w2WQF1F8qs-wN4X3RHuq8vKyQ-fuRbliFMOT14uoriAaQl1f-3u2tJpGcdhKT5I6hf21CcaQsPE3x5DRqt6S5lMxi-abs6N2Ah7oGYBYz-c2xztpa6S211J_lNsisN_jgdK0RUIV0U6LHWGsvZgxP6ED9LrE4XNZljDdfSfJ-b0jrWp43qZM4QX5Unb1XindP9ge0RdBR0NKzJTY8UZ4NNQVx8t3Y2VEAGDfQpU3wmVZo3azaQe8NmRqAfuBoAd-sQvt7HztHLBYfqpAXWaosH7uCHmHraCiuc0E1e2Y6SG9bXGJroYpJ-mJ4HKIs4z5xrQ5So7o5OtdxaSoqnJRJQklZ-gO0p6BdM4YS5R79lqWMOd6rJsQB4k4HV6GAv3KBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شهیدان حاضراند!
🔹
حضور و غیاب شهدای ناو دنا و جماران در شب عاشورای حسینیه معلی شبکه سه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/663297" target="_blank">📅 23:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b09e48496.mp4?token=O5UiKfhht3yT84Cv09GTLaWOnNCNZ8O4hlF4zxXeN-pBmYeiGVp8BkldYIhfoz2swHmB_yUJAI22rw5O3b4nPyxTpvVB3aBul_AshLyrqoAsbCB94403O3phEnknJCRILtJo96tqcFSpXVyQsnWxQSo_zzud2x3e1ZzNdCBeRZE4sNSL-o10fMnILRPwBOHOO0il7A0B685nFTW8X4TvlaxY0RkR8SG6IoDJBuOQxvAPd0xTu-llfGdJ6vnIX7A52IP_xQdxpwCnXbvOY59lIBtaLmgR4yc93CwFIM0Tg7HW6HQhW4tlyGTIjL4cyRx8Esil6Jkj2GYqsCps6V2v9oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b09e48496.mp4?token=O5UiKfhht3yT84Cv09GTLaWOnNCNZ8O4hlF4zxXeN-pBmYeiGVp8BkldYIhfoz2swHmB_yUJAI22rw5O3b4nPyxTpvVB3aBul_AshLyrqoAsbCB94403O3phEnknJCRILtJo96tqcFSpXVyQsnWxQSo_zzud2x3e1ZzNdCBeRZE4sNSL-o10fMnILRPwBOHOO0il7A0B685nFTW8X4TvlaxY0RkR8SG6IoDJBuOQxvAPd0xTu-llfGdJ6vnIX7A52IP_xQdxpwCnXbvOY59lIBtaLmgR4yc93CwFIM0Tg7HW6HQhW4tlyGTIjL4cyRx8Esil6Jkj2GYqsCps6V2v9oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
یکی از بازماندگان ناو دنا:
فرزند یکی از شهدای ناو مرداد ماه به دنیا خواهد آمد؛ دختری که هرگز ندیدتش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/663296" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b845c7b0d8.mp4?token=JGMvq7aZXCoXHnwqkhK1l3mpFkkSPe1vhVmtqcpxeB6VaActI-TVytBWH6MNLHCIZG0TIIpMm9u7eMIk7HqdowHYUoPZ8fLGQ3ZEIzgO39YscjDk5Q3vGUv9hh4sbVcJHKFeW0bpaTjmNz561LaDGuPyfAV1iWJJorbGMc2ujHpLXWM3uM2xk0Z4z_Mggs1_XAp8vohsi1sjSV2OttunheHdFHgeaG1g-7Gk6MQoftwPkwfkK6bMUYKrQ53M4CGZYziZBI6i4J1hRqDoVT4wgqB9o9wSel2vxyL_gdyWcDEin1iDcfgAH64qAQ-L2LeXPV8-YdafxTeYRDrtg8y8lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b845c7b0d8.mp4?token=JGMvq7aZXCoXHnwqkhK1l3mpFkkSPe1vhVmtqcpxeB6VaActI-TVytBWH6MNLHCIZG0TIIpMm9u7eMIk7HqdowHYUoPZ8fLGQ3ZEIzgO39YscjDk5Q3vGUv9hh4sbVcJHKFeW0bpaTjmNz561LaDGuPyfAV1iWJJorbGMc2ujHpLXWM3uM2xk0Z4z_Mggs1_XAp8vohsi1sjSV2OttunheHdFHgeaG1g-7Gk6MQoftwPkwfkK6bMUYKrQ53M4CGZYziZBI6i4J1hRqDoVT4wgqB9o9wSel2vxyL_gdyWcDEin1iDcfgAH64qAQ-L2LeXPV8-YdafxTeYRDrtg8y8lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بیست و یک سال پیش مارادونا از پله درخواست کرد تا چند ضربه سر با هم بزنند و این لحظه تاریخی به ثبت رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/663295" target="_blank">📅 23:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGvWmfXgHFAsgTAMbogUyZEyoEsSAyDNwtUwzpSyyitOdyT5vAPT-v59imV3iqMX42EtoPoIadnHwigMkmNnez68l22b5Vf2VlcNyBmQ7PKFvR3AqwqC6dMhVwxvUkoGxPmjzbi7Ht9ZeCcjIrC7VGUHWWwP7G0UWc5thchgVP6mp1CBkyxVyc7Le5u8NeASV4f997Ssf-fqGoAFzQynWcvJmvRInTfZ9MJDEot6nveH1r0PWvX0ZiGdLFR4GNYeNvEm8MyAsifwCkvHMHMFBl-ae3dHaFqtj4-qjITXK2UG-aaB986YMrEDrE4AAoz65UyAZskPnJk4GRRGJ2rv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
روستای حسین آباد در املش گیلان
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/663294" target="_blank">📅 23:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHzGVgLVZ9O7S2YZc4cJ7cMQPPVyWWSEBhuuRS4KGT4yRPn25e3c72yiAuw7v6BTNoQ_pxObPOMx3VPTRKvSmHsBzApLzLnxmUcsXFm2z_BhrTXYlvYhzmPMXjf8QZ7aXV030JaZF25Rt4XwZZLv95_gntunKHUQ49jMyGuVtQp6xrJJYPaNsc42Klko0RghXUUCxTQtZtnt2NePmxBNF54m5SAsOhJ9nwN_VeB2NGuS7BWwUUx33P64rfvJXJWpqAae0WWGwVy-L1UOhHPFtWKn2JIQ8fbeOPi9SeNi1Aafaj3qIZKFyxYQHdy7xU5CGUMh4Jt6OBI3w8lIkg9-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
رده‌بندی جدید خلاق‌ترین بازیکنان جام جهانی ۲۰۲۶؛ رامین رضاییان در رده هشتم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/663293" target="_blank">📅 23:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usdpCGQfiZDNa-zVTQFZb4Dtrf_RMuM87kog1UXjAJ9ZGJ6OfQB-fyJh3pWBlIau4OWx3uH8FDKA5k1RYfftx3c5mI3oON79nGLq7ay0FCttWCiyct4Tia29QVXq7NfLACpw-rN8immuR31rihC2b2Kkgfv2fJy-0tMgo_h7nBMQmoRVFFDNLRJzj66Noc58nQXCJsfdONjqzddx1h72jhJByDAvJKeNvo64LBrrax_GjfYGF6hEAzQT_tMYOy79kXzoIBrGrTGRl96Z7OzkcNQu9xEYpV8svFuXBxSgf2Efk4-HUfxJGIeQZz5m5rwdZ82oYG6J3kUo9hzLZ_V_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«میانجی مرموز قطری» در مذاکرات ایران - آمریکا کیست؟/ ۴ سفر به تهران در ۱۰ روز
🔹
رسانه‌های غربی "علی ذوادی" را چهره پشت پرده قطری‌ها در میانجیگری میان ایران و آمریکا توصیف می‌کنند. اما او کیست؟
درباره وی بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3225646</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/663292" target="_blank">📅 23:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6bc653804.mp4?token=I2b17-38Qw3bNmqi8svZYsTyIHfC6G44eQnm4eYlelt9KpIyBJZCpQA3OlUpXMhbxKD2QeEMQ-c35FsHyowBo-94nlGcW_mgZRm99-gXw1jzpBo-9HP5St7wUkT4hbMkjaLcGOVSZwEYsiNzhxLzp9qXoN7wfEuk_M2M0O9KkVdKJV3i8p3YR-6Jp1oeiZzs1fMSVTFIzYTZmjri2IJRckTOz3z4Df2n6DhncGMkAAngXDshbhqQHrA_GhBRZeJpNjyFHKF2tYsSJDzdwWTXtvhhjWjxhVtsGBQ5kxgnuC80G6hwWAwkMpQbNTAwXVF97h-ukSDV3-___uSKAWiWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6bc653804.mp4?token=I2b17-38Qw3bNmqi8svZYsTyIHfC6G44eQnm4eYlelt9KpIyBJZCpQA3OlUpXMhbxKD2QeEMQ-c35FsHyowBo-94nlGcW_mgZRm99-gXw1jzpBo-9HP5St7wUkT4hbMkjaLcGOVSZwEYsiNzhxLzp9qXoN7wfEuk_M2M0O9KkVdKJV3i8p3YR-6Jp1oeiZzs1fMSVTFIzYTZmjri2IJRckTOz3z4Df2n6DhncGMkAAngXDshbhqQHrA_GhBRZeJpNjyFHKF2tYsSJDzdwWTXtvhhjWjxhVtsGBQ5kxgnuC80G6hwWAwkMpQbNTAwXVF97h-ukSDV3-___uSKAWiWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت‌های پر بازدید وحید اشتری از فعالین عدالت‌خواه در خصوص توافق اخیر ایران و آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/663291" target="_blank">📅 23:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663290">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ8ITfykQTON1amMdII5S7f2RmeBouve_B0PUHdWcrR2QbFnrxyTRarDCz9fn86amPh7aXGSZ1LzmA1PbB52wGpH1lRwGacGUmM5cw0i313ThjIMrVibhSBcor6PdubTe0n4qOac8gx3k2EBZs0K90DBefMjdBGWM_-jUOb5aD3UZZp0jjIYtOPM_j4FmMVNdXbTiVT91jFBZ26gA-6PaO1LYoTaLrw_Z_WUd6J7t_2gCjQWsThu8ZYTCOedWJgAxrcGDLYngGvdXxavKs2bY9e75YoWvAxpU-niYUBcFxFnYHO2HVBN6UsJdo4hkIqLd5JMojFlFzwzLpXrlOwJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حضور ذوالقدر دبیر شورای‌عالی امنیت ملی و سردار قاآنی در مراسم عزاداری امشب در جوار محل شهادت رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/663290" target="_blank">📅 23:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663289">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pE62BlQ2KSP_vzNWCrPf0LOzf-fbTQvzM4BlbausboddoG8kRPmVTZByyS3UXXOA5FTpZW4Fm-mlt7bXhhAvcxevim2kTBlLgk-lBp8ha6OkSczMipzC0yIN-amo1VlOR2ZdR9SipGL4qXTSnO9LQl8YEqcdEpt1fnOxCfaCGosqJbz5pq8Rs8x550NkdckdqTB3y_417LkItDYy1-j4KhqZ02SrxZLNny7P4WGBxk8aYWc5WIoZNG9SBClfpbXSDAZLA9IqDgXy70il8Px_aIh-Ts5XK0GpxW4g1rRDGn6VjiLgkNMaAHLClI1J98Bi_lfuE7RG4UvFN-EKXtaJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطر زمین‌گیر شدن تأمین اجتماعی با کسری ماهانه ۶۰ همتی
🔹
گزارش ایسنا از یکی از چالش‌های کمتر دیده‌شده تأمین اجتماعی پرده برداشته است؛ جایی که درآمدهای ماهانه این سازمان با هزینه‌های اجتناب‌ناپذیر آن فاصله‌ای حدود ۶۰ هزار میلیارد تومان دارد.
🔹
در شرایطی که تأمین اجتماعی مسئول پرداخت مستمری میلیون‌ها بازنشسته و ارائه خدمات درمانی به ده‌ها میلیون نفر است، کارشناسان معتقدند تسویه بدهی‌های دولت، تقویت درآمدهای پایدار و پرهیز از تحمیل هزینه‌های جدید، بیش از هر زمان دیگری برای حفظ پایداری این صندوق ضروری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/663289" target="_blank">📅 23:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663288">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6kfZzlxSlElXdvf1HqQ6yZ0U9WM1SPUHoBZv2upCcATVgcPIEjln07YCxaQMuY-iW1a4WCMevCLhxhPkM1qy_alzYIov8OskFfkzy4E7kBWzKt4_vCgIsIqQwjZKuy0gUsotb8_7QmEuHXRY11yY7h0AeoGz6zjYBRFeqhSbS83_6FNIP0e40HMECSmOOsGrDSRKQPZzSsGieu96PonoYq6jhvkMYrGiQ2WkBKHjSl0yQUb1rPypi1VyAcgGyr4NfE88XOGFiwHtr3fu_WmaLy7-cu4Imp57EyOAmY6qvgwMnOPrrzHUkk7dRoETfFhH1_46___1j0MJXOs_70Cng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری مهدی طارمی از سیاتل آمریکا به یاد عاشورای حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/663288" target="_blank">📅 23:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663286">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTrOk8APJ-j4iSgQ1A6LU3DNyk_K1OyTUDPzL80UA4UMaYJe-4CRVkxXN5CnO6CqpahE6BmU_FqGO9YHlMRGDtbu5878wqWgejDw5deZ_xGS9sfltVMJbVSKZ8nkTs4DpaiTC_fqKLNskVOEMEbfErYnHw_qGcj8GD6baAz-bKmhwcztBE_ObuLkxIv2ag2J6WwcpF74v3qTSXnOwO_f2eS5Xcx7p8Yo3DAu8HCBrWBLDJwgMPUzUxXy7737ERQY35Q9oaPLCMJv8MpzeAM5Jc7U8GnBbaLFba1p6odlH9qeGLUplF19u3JGbHviZ3PmpZhlaN6oQL6acy5PGNWFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
شاهکار تلسکوپ اقلیدس؛ دقیق‌ترین تصویر تاریخ از مرکز کهکشان راه شیری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/663286" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663285">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrIZepILFykH7fX9YFkCVYCefD56awyxZgyz9WRFYB-dfwoyp6V2lrVBlVrY3XMdKyjuOmk3uWzxYX_UwCCMrp0b-0M6Gpc1gbOn2UsK12_p84Yo6PuGHTaOVN3U1jiiJ0Dy0ocLR086hVAWiMrBfuIbxhaFkgTOsU9GonKYrjieRFjH8EwhS7bn8ThKNmehEReU1ZjxNKRU_SLwAEqi9gAQKrSsp5UtIB3B172cSLF3Ax02CzgpbY-bJIGW70eHESuSnDcT9hK7wJ4pTLqDCKBeb_OwOhAZvt6hPAUEExFLjukzOf2e6vJCI5DulhwFv6dOe1F67jpEutPFpjrzpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بعد از انتشار خبر حمله به یک نفت‌کش قیمت نفت برنت دوباره افزایش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/663285" target="_blank">📅 23:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔹
ادعای رژیم صهیونیستی: ۶
عضو حزب‌الله را در جنوب لبنان هدف قرار دادیم و به شهادت رساندیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/663284" target="_blank">📅 22:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔹
تیراندازی کور تروریستی در سراوان ناکام ماند
🔹
ساعتی قبل تیراندازی کور تروریستی در نزدیکی مسجد جامع شهر سراوان رخ داد که در پی آن تروریست‌ها سراسیمه از محل گریختند. این اقدام هیچگونه تلفاتی در پی نداشت و خوشبختانه شهروندی در پی آن آسیب ندید.
🔹
هم اکنون آرامش در شهر برقرار شده و مردم عزادار در حال برگزاری مراسم شام غریبان شهدای کربلا هستند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/663283" target="_blank">📅 22:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663282">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef52fa42c7.mp4?token=T3p3RUQApkiYH2KE0ukMl6_4RF_7LtkbI_zk2bVVhOjivnc7VBWjOY7RnBIOcFscW5YObkDtzndr3D_Kq8VE9paz93iehm_qZHn4x1WzwjREJt1U5i41AFOAkHwDAFWo3GVGJrvMlkiYgM0odYJr_5IpTIoiA70KdYjvr5Fc_u8rrlnUHKc3HrSKXZotxMn3Fxy0gkSdNXDbX9M0oyGEghntd0qs6BaNKM0Z5VkXe3iKFllU_rr5ElYnjnZk5blhUgC5EYAlsZIPVbEZAxe_atA8HgKtCIu40t08yAOYvpyDJGWI--Fbjysjy6CB0fnlsh_TqOuv88STggniwuYDbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef52fa42c7.mp4?token=T3p3RUQApkiYH2KE0ukMl6_4RF_7LtkbI_zk2bVVhOjivnc7VBWjOY7RnBIOcFscW5YObkDtzndr3D_Kq8VE9paz93iehm_qZHn4x1WzwjREJt1U5i41AFOAkHwDAFWo3GVGJrvMlkiYgM0odYJr_5IpTIoiA70KdYjvr5Fc_u8rrlnUHKc3HrSKXZotxMn3Fxy0gkSdNXDbX9M0oyGEghntd0qs6BaNKM0Z5VkXe3iKFllU_rr5ElYnjnZk5blhUgC5EYAlsZIPVbEZAxe_atA8HgKtCIu40t08yAOYvpyDJGWI--Fbjysjy6CB0fnlsh_TqOuv88STggniwuYDbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
نان قندی و روضه‌ اول وقت؛ اینجا پیرترین حسینیه تهران است
🔹
در کوچه‌پس‌کوچه‌های تهرانِ قدیم، خانه‌ای هست که حدود دو قرن است صدای «یا حسین» از آن قطع نشده./ اخبار تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/663282" target="_blank">📅 22:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba374eaa7.mp4?token=JrdAFBeo6OSnCfhMm2SKOHgszQptioWHaF7eUjlW0CR3ZRFj-bwBoJ4Hk5iHe_TwRP9foScgB49Y8XIIpq3VHU52KdZXsANInVn_VaUWav-0evS5PWFeY9ijFuLgnZOuCGLZdpmBqu_B4dQAOeU6OS4rUBExLbMvEDsHXJcaUgsFbHa_W8d0RPxGc4Bip0M50p1UFxKXo6ps3oxJkDNy0CJmjx6ZOgaunkxGDR1EzjCBAWnwVyyqIU2QRGiO4o5KNyL4GqIDtvl-DWi6Ow70zi_sgPA72cl-Z_wBjISJ5ZWD3oXnZ_IzZJETIuQ0M4aUkh1ORmgZsbbd6NMOC_1FKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba374eaa7.mp4?token=JrdAFBeo6OSnCfhMm2SKOHgszQptioWHaF7eUjlW0CR3ZRFj-bwBoJ4Hk5iHe_TwRP9foScgB49Y8XIIpq3VHU52KdZXsANInVn_VaUWav-0evS5PWFeY9ijFuLgnZOuCGLZdpmBqu_B4dQAOeU6OS4rUBExLbMvEDsHXJcaUgsFbHa_W8d0RPxGc4Bip0M50p1UFxKXo6ps3oxJkDNy0CJmjx6ZOgaunkxGDR1EzjCBAWnwVyyqIU2QRGiO4o5KNyL4GqIDtvl-DWi6Ow70zi_sgPA72cl-Z_wBjISJ5ZWD3oXnZ_IzZJETIuQ0M4aUkh1ORmgZsbbd6NMOC_1FKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون: مردم دقیقاً برای جلوگیری از جنگ با ایران به ترامپ رأی دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/663281" target="_blank">📅 22:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEPzuwlO7E_fiaAKm8n-w1LMKnvmGIfWwEwAVyBnUS3qEsm6H25csH4S-IcbTSWaf2wgk9mg2YaR4IXJgjWSMipVa-Qr_RnE8KdoITkAglvvCYWSuBhQVfN-U0OnLocSBMH55ho6wET3hzvtxTDssCouKhLtj3UjZljEJKDy1kjlhHfD-oNAbcpA5hxMyYdzagc_ZMaQtvBc-9OecLs3Obhc6zQ7QQH-eVtIZAQc0-J2dVS2HI3iH6FifW9moF6VLtKwnriJnK_F4qY-wl-d5TXfRPi3n2Loaw4xbeiZ0mBzv0m8dwRos-HxldM2rBFM0EE2JGSxpHPs4RBp0eQItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نظرسنجی شبکه ۱۲ اسرائیل: چه کسی برنده جنگ شد؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/663280" target="_blank">📅 22:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663278">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujMp5pWYwdul2ei5lR9fqEwJB8aFCSo4lXTgEXNstFUh5Q1pBOkoe3QPgXzDTW2bn0Ujti66ol7P94wl6cGUoj6cFV_4kc8tat-ryQf4Ig_rjXJX-v4cge99YEBDRVJ8wfdpnV2ou7mX1Dgp-VC44jQ75qmvuzFkeYrUPwPHE8wlJuvVt_91mGsaxAjZ1z6rvWgRF5h3PRl9QeXFFHv1yUi5yLTetp8GbM2jMnd2fWO2kDEygCDcXjuOc3SiM1wkAQNwkPTuSKd12P1U97XIbcfvqzsRNm_8wPUQki174olyhmn5pGh0ZZ-8A39mzo9x5z_4GASfv0f762s0eXaObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رییس شورای اطلاع‌رسانی دولت: رهبر شهید، پیوند عاشورا و وطن را به باشکوه‌ترین کلام یادآوری کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/663278" target="_blank">📅 22:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663277">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/663277" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/663277" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663276">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/663276" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/663276" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663275">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWa6H8lEb9skTmDOUnPjBoZceSkHKMgLMXR5SHT_lck10w0Y1QgJlBdJnC329LwQerRdAi84vo0C7rKW-M2XM4wMdJCjy---LvGitGkgUxMY9e-c7MKJELyGyY1Hy6suP749Rr9Xc3LRrZN7Pj9Dt1IbH9LT7e-GrmZQCS0BUZFsFxQ28-JCH172jlTT3CFnxSrWQli8F2nlSbPFUspin55udV0a6Ns5FMa6LcpEngY7xyAfQOPb4qanE-1aNSTvDslw-9mBG1dawclfhm8trShYpFvjT6L0dLKNFsk4PWmf25cC66dTiz-qyDKe9WrCX8f5Ri2-t5NguuMy1pBmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چین رسما اینترنت ۱۰G راه‌اندازی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/663275" target="_blank">📅 22:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663274">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXY0q_bUX_KuhYS4dNCBQ5s8xZDexb7Ag4YNOw2pfwxpNvdasL_nEL-cBZs4yIwYYE7PF-jU1Tu6WbFe1o3DITsa0IlvTgPrGm-4jrt55jd8zgegh3iyicupXqNDPlwmHkELKhE-DTBsC8mck6yWYrKvW8DoP34ZZaFsISKCj3hpt-3RafXUbzWNb9sXmO8OkenKj3raoM-85MqAD_q-pEVkGv5omVINJ71XWg0FlDhKc11go-io2tBDsxagi452cgCat6CXFjxB6SIZx3qSeHiK2JBjySD_I4bibNkYIFaXP6fSlcqatLnK2vTWbmJKlTdQLUpJ3bu-7YImnk2zSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار نهاد مدیریت آبراه خلیج فارس(PGSA) در‌مورد تبعات تردد شناورها خارج از مسیر اعلام شده ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/663274" target="_blank">📅 22:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663273">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b5075bf04.mp4?token=Glsz0z3jAR7QPrcTyrus0wpr18GvkWlotWd-UQuri1whHSHHN8uhtYhpC5RDBs_jgPJzhBE4Qod8d4hXTODPaKkYfayosKmJ4uZsi1HpOxkw7Lg3sSvSXWTwb58AQo877D0x8D93vQMP80R3QMYarnLHU66pUZuQJR5qsk94Y-WG_SePtaBIlJyJXb1pCht5zs6Iw-yyrS4lOF2S59FjMiaSRN0EsBe0HQLisqi3Dh3KwzG2NoDkpNm09jRay_uf4z5vlXfYEFpV54nMwK5Fk24NlxuTlyxO_Zv4HCtNiH9JYWhQOuua5Ujf3Uw-MRtd05fzTPYfgb4h9d9QFWsOLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b5075bf04.mp4?token=Glsz0z3jAR7QPrcTyrus0wpr18GvkWlotWd-UQuri1whHSHHN8uhtYhpC5RDBs_jgPJzhBE4Qod8d4hXTODPaKkYfayosKmJ4uZsi1HpOxkw7Lg3sSvSXWTwb58AQo877D0x8D93vQMP80R3QMYarnLHU66pUZuQJR5qsk94Y-WG_SePtaBIlJyJXb1pCht5zs6Iw-yyrS4lOF2S59FjMiaSRN0EsBe0HQLisqi3Dh3KwzG2NoDkpNm09jRay_uf4z5vlXfYEFpV54nMwK5Fk24NlxuTlyxO_Zv4HCtNiH9JYWhQOuua5Ujf3Uw-MRtd05fzTPYfgb4h9d9QFWsOLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شهید طهرانی مقدم، پدر موشکی ایران: من یه چی میگم میخواد خوشش بیاد یا نیاد، گریه امام حسین بکنی اما رهبری را کمک نکنی این گریه تو سرت بخوره. تو همان ابوموسی اشعری هستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/663273" target="_blank">📅 22:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663272">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a025695ca.mp4?token=IbqTncq6JIfs0gpqnHjPNjVotgXlk_BEA98cjKFNDooeDx9ZSamvEj-fyRLDXyaGxARSEOqvqrgvrJ0YuO19S3sVaFUPeNcW8YiPYhukF25zulVXUHXHyJAZokguVCagGKFXIjsPJvnH1XqS1gGa7B6aVkGI7r0ZExkdjfTFW2HP4sprWGWfbgx_4oetUTeTUp7QAbQSwgnXGgnTQ7CGlq1Tlx8etyxVeKLI4J6CApUxKIBDMj9sGPMHXkU3rqzn4B3LeJ-j4wyrpcM0EkDQmZor18Bn8Jm4PlswCpE2EVjOSZEtY4AxeUTH1ShGx1_twodorUh2J_GWK0h6VOQpJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a025695ca.mp4?token=IbqTncq6JIfs0gpqnHjPNjVotgXlk_BEA98cjKFNDooeDx9ZSamvEj-fyRLDXyaGxARSEOqvqrgvrJ0YuO19S3sVaFUPeNcW8YiPYhukF25zulVXUHXHyJAZokguVCagGKFXIjsPJvnH1XqS1gGa7B6aVkGI7r0ZExkdjfTFW2HP4sprWGWfbgx_4oetUTeTUp7QAbQSwgnXGgnTQ7CGlq1Tlx8etyxVeKLI4J6CApUxKIBDMj9sGPMHXkU3rqzn4B3LeJ-j4wyrpcM0EkDQmZor18Bn8Jm4PlswCpE2EVjOSZEtY4AxeUTH1ShGx1_twodorUh2J_GWK0h6VOQpJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات موزون بازیکنان و سرمربی در رختکن مکزیک بعد صعود به مرحله حذفی #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/663272" target="_blank">📅 22:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663271">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔹
اختلال بانک‌ها بعد از ۳ روز همچنان ادامه دارد
🔹
رصد گزارش‌های مردمی در شبکه‌های اجتماعی، کانال‌های اطلاع‌رسانی و بازخورد کاربران نشان می‌دهد شبکه بانکی ایران از فاز اختلال شدید عبور کرده و بخش عمده خدمات به وضعیت عملیاتی بازگشته است.
🔹
در میان بانک‌های بزرگ،…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/663271" target="_blank">📅 22:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663270">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjzlmDYZJCBoSlAapW8kK9PfL613qv1WNhD-LNzSF22QpOjnFuoVZX_OMrLwDeyhiJybFoT17Qd1QojIv6uBJtbqVeAcvPX-G_MAY50eJyQO_-LPZNwhG3Joex6ehHQXCPU1_coDlTcdNrvgs8zrQlq7c5_2BiEYZZi9fki-eX9YuUFiSX_V3fqgcR6SAda_mgo3cTdzW9nOaYornRzCbYavH2hrj-0asTLuIQd0oqJbR87ZyPJegKjfC8v0hRC01eeInQ-hK0bRrwHGVckh-41pq8AayYw2YgWhbwI5Lbv7IYBMcWM-OTgJ_s5Jb1RaWETp23OP8SgZZ1y-1BCwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_اول
▫️
امروز با خواندن زیارت عاشورا به نیت شهید بزرگوار
محمدحسین عزیزی
، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/663270" target="_blank">📅 22:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663269">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔹
روسیه: آماده‌ایم در روند تصویب قطعنامه مربوط به توافق ایران و آمریکا مشارکت کنیم
🔹
ماریا زاخارووا سخنگوی وزارت خارجه روسیه پنجشنبه گفت، هنگامی که آمریکا و ایران به توافق نهایی برسند، مسکو آمادگی دارد که در توافق بر سر پیش‌نویش قطعنامه شورای امنیت سازمان ملل مشارکت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/663269" target="_blank">📅 21:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663268">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔹
ادعای وال استریت ژورنال: ایران روز پنجشنبه به یک کشتی باری با پرچم سنگاپور در تنگهٔ هرمز حمله کرد و توافق اخیر آمریکا و ایران برای بازگشایی این گذرگاه حیاتی کشتیرانی را به بوته‌ی آزمایش گذاشت
🔹
این حمله که به پل فرماندهی کشتی آسیب زد اما تلفاتی نداشت، تنها ساعتی پس از هشدار ایران به کشتی‌ها مبنی بر عدم استفاده از مسیرهای تأییدنشده از سوی این کشور انجام شد/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/663268" target="_blank">📅 21:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663267">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5bc0db45.mp4?token=a0DbvJqLlXZgm49vaRMTSZ0xRFJs26iDoyy9-LluOWGqRn-q1ZzjyvGJjlb17DeGj5BBCwuR274F6e1HWyvUQ6-UO4MLbqRGynFEJ62xMKoQjCaM_JkxI8wcNHKvPz03s6xmJJGH2Hbhqwl6_ThJGve1qTzKSSpH4_wAfBxn2sasxihzrzw2wrXQr3gyMsBJO53JnwFkowDrkmIrFIYFUQURxoveopBsQX_L1f_7shrBpzVc345FSGVUmuFA67pcIDF62dv_Zu4uI7t8PZlV2_GXfHlm2xyIdz8d5nE-srHpJY75mLpCsQScoMl4-hGvssJkQuxOY8lhx6AlPqUnHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5bc0db45.mp4?token=a0DbvJqLlXZgm49vaRMTSZ0xRFJs26iDoyy9-LluOWGqRn-q1ZzjyvGJjlb17DeGj5BBCwuR274F6e1HWyvUQ6-UO4MLbqRGynFEJ62xMKoQjCaM_JkxI8wcNHKvPz03s6xmJJGH2Hbhqwl6_ThJGve1qTzKSSpH4_wAfBxn2sasxihzrzw2wrXQr3gyMsBJO53JnwFkowDrkmIrFIYFUQURxoveopBsQX_L1f_7shrBpzVc345FSGVUmuFA67pcIDF62dv_Zu4uI7t8PZlV2_GXfHlm2xyIdz8d5nE-srHpJY75mLpCsQScoMl4-hGvssJkQuxOY8lhx6AlPqUnHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویری از آیین شام غریبان حسینی در حرم مطهر رضوی
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/663267" target="_blank">📅 21:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663266">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°(منتظر)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3u8lCRnQqQ2NY4HdPoHhEkoD-GcmkSw6CablO70Wn0KmA6R3TfGNktF95-ZSToVk2rYMjC1WSpP8kFkBF0gIFNB5zPurIoJezgsdFdhEWAKuG3tc1JDK5bCaCSwpXV3dMBPUmFoYbLv9rHdDvn4aogtgPbZUne1ztV74IsMqBOnQv8zg6AqOPXt5UrxpUNAWoqYxvBwQrKJUbY1S_lmW0RI8cFv53wn4plXBkRPi4yzfcsTg74V59bB0Dx_8Kg0uDFmiVnKfwdzYDInwVd94kevO2NNQh7wusdomjx8871yEcm7US_ApFiH7YZ4U7Zq2p7y5tR9fmxSW9B7l1AwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مداومت چهل روزه بر زیارت عاشورا
چهل روز زیارت عاشورا را کامل بخوانید از امروز
چاهی که انسان در خودش حفر می‌کند، در چهلمین روز به چشمۀ حکمت می‌رسد.
از عاشورا، چهل روز بر حسین (علیه‌السلام) و زیارت و محبتش مداومت کنید، روز اربعین به آب می‌رسید؛
اربعین روزِ مُزد است!
آیت الله حائری شیرازی</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/663266" target="_blank">📅 21:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663264">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔹
سازمان بین‌المللی دریانوردی: طرح تخلیهٔ کشتی‌ها و ملوانان از تنگهٔ هرمز به‌طور موقت، پس از حمله به یک کشتی در سواحل عمان، به‌تعلیق درآمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/663264" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663262">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔹
سی‌ان‌بی‌سی: ترامپ گفته که آن منابع بلوکه شده ایران برای خرید کالاهای آمریکایی، از جمله محصولات کشاورزی، استفاده خواهند شد. ایران این موضوع را رد کرده است. چگونه می‌توانید شفاف‌سازی کنید؟
رایت وزیر انرژی آمریکا:
🔹
تفاوت در این است که با اجازه دادن به آنها برای فروش نفتشان، می‌توانند پولشان را به دلار دریافت کنند. آن پول، پولی است که مستقیماً به ایران می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/663262" target="_blank">📅 21:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663254">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2921aa36ab.mp4?token=TxaskI-Lfru6Huy8A5eiJlc-X13wuw5cwIhaiml1uV7trdGbTjxx9blJYjo1xPMJlLEDsgPY79tMhhwD7uuTPFbGXb6qO8tBjhMMBfryXXLzCS-lTseoMGOPWAKca9ts_i2zHYDYpXd-zLwjJtA4ndR19coYA_hI2zBr5itPSbizpi0VuE5YFMPzvkC-PlRfPV7CAQMxElMH0xz3aTLlfygtDb1hxzb4xCDVQznHtuf7zbIWpXJ53vQUtC-mKWwpFTsDNN5_z6LiBW5qhWWr1YPrHr6TrBkBWE6yPZuYP4iHPAYNM1z3tWyOI6tH0dtCQOi4geoxfGF8vW2wpiorXzwSv6Vo2F9n4MlgKfjvETM0l6bV6DbctMq9_PnTuLQrUTD8x6JzP-qSvj_e0a-M1OzqDs4dUfB1NTXvPx8dTJlcPIpVUZSmLyHcqj45ViV4xWVFZKeOzRIe6Pt28B4MsO8KJEeq89c1lZDI0mXKDD2SWwNKK1yiQjc_0MBbUMq79Ex8zDipiWxgbqY1fUSWrwCxqQ5lWPEUVX-wq1G54kNjjKbLBCNN4_xji1Pio72y300QQV7CfjRdJ2kQ4sHQ7BvEdgr1lBuK27X5jDerYPpCPfBhlhk6H9ixP7q08OTaS6LSM2hpex7DfKJkJablr-foRjUnv0ObyK4YqlSKKOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2921aa36ab.mp4?token=TxaskI-Lfru6Huy8A5eiJlc-X13wuw5cwIhaiml1uV7trdGbTjxx9blJYjo1xPMJlLEDsgPY79tMhhwD7uuTPFbGXb6qO8tBjhMMBfryXXLzCS-lTseoMGOPWAKca9ts_i2zHYDYpXd-zLwjJtA4ndR19coYA_hI2zBr5itPSbizpi0VuE5YFMPzvkC-PlRfPV7CAQMxElMH0xz3aTLlfygtDb1hxzb4xCDVQznHtuf7zbIWpXJ53vQUtC-mKWwpFTsDNN5_z6LiBW5qhWWr1YPrHr6TrBkBWE6yPZuYP4iHPAYNM1z3tWyOI6tH0dtCQOi4geoxfGF8vW2wpiorXzwSv6Vo2F9n4MlgKfjvETM0l6bV6DbctMq9_PnTuLQrUTD8x6JzP-qSvj_e0a-M1OzqDs4dUfB1NTXvPx8dTJlcPIpVUZSmLyHcqj45ViV4xWVFZKeOzRIe6Pt28B4MsO8KJEeq89c1lZDI0mXKDD2SWwNKK1yiQjc_0MBbUMq79Ex8zDipiWxgbqY1fUSWrwCxqQ5lWPEUVX-wq1G54kNjjKbLBCNN4_xji1Pio72y300QQV7CfjRdJ2kQ4sHQ7BvEdgr1lBuK27X5jDerYPpCPfBhlhk6H9ixP7q08OTaS6LSM2hpex7DfKJkJablr-foRjUnv0ObyK4YqlSKKOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
لحظاتی منتشر نشده از دیدارهای صمیمانه خانواده‌های معظم شهدا با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/663254" target="_blank">📅 21:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663253">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f8e53946.mp4?token=isHIqA2VEIH8panfVvHwUu-Qi2mCbQODWG9UZRSXbI2EFYndmY7ZKttydDL09jjgxq3drRL2cCFZ5DSATkeqmaANp4mwu4r8-VcUXx3cFHkzeZ8eHDPWqTJrTPGzfVyv7O3vi2KNT9nctLwWCRm_y6DuawCnOpRe-aa84HSXeqXsadIChl-T3Kg8XFif66ILyk2pWvT6HfoJbJ4Imb0-TKYqsYPa_xxz36kleGCPw_JWbeFUI3BXcmwY3yVKvdELAeqQhttVeqlaNcrzKy_ob8jwFbHPb7AMxPpd6AzM2UDtvGK_-4K8a7o5K7taqOrXC9koEazGKspGj8iq-f1KKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f8e53946.mp4?token=isHIqA2VEIH8panfVvHwUu-Qi2mCbQODWG9UZRSXbI2EFYndmY7ZKttydDL09jjgxq3drRL2cCFZ5DSATkeqmaANp4mwu4r8-VcUXx3cFHkzeZ8eHDPWqTJrTPGzfVyv7O3vi2KNT9nctLwWCRm_y6DuawCnOpRe-aa84HSXeqXsadIChl-T3Kg8XFif66ILyk2pWvT6HfoJbJ4Imb0-TKYqsYPa_xxz36kleGCPw_JWbeFUI3BXcmwY3yVKvdELAeqQhttVeqlaNcrzKy_ob8jwFbHPb7AMxPpd6AzM2UDtvGK_-4K8a7o5K7taqOrXC9koEazGKspGj8iq-f1KKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
فیلمی قدیمی از عزاداری مردم اردبیل
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/663253" target="_blank">📅 21:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔹
وزیر انرژی ترامپ: پول آزادشده ایران به دقت پایش می‌شود
🔹
رفع تحریم‌های نفتی علیه تهران، به ایران اجازه می‌دهد تا نفت خود را در بازارهای دیگر به فروش برساند و وجه آن را به دلار دریافت کند.
🔹
تهران قادر خواهد بود روزانه بین ۱.۵ تا ۲ میلیون بشکه نفت صادر کند و با دریافت وجه به دلار به جای چین به بازارهای جدیدی نیز دسترسی پیدا کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/663252" target="_blank">📅 20:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a2cfe27a9.mp4?token=X1Kzg2GMUN2Kzl-r5_Zjn--pWiyVM5xUb_xMWgQ3Il8bsx6wD_PjzXjREBU6XatdtyHY-AdUMDJaL1jkawhQINmXFil74ZBuPqpBnb4eiY0jiTcc28cDKXugf5Q6jIb5OA1ceUTurQo6dmXT5ak3rnY1jYnQvQglq-W7q_5Qoo7QL-dg7IAm7zjN5BtATyQ5EBoTo9cYN9Hgpz5ABl14fkzRHYbARwQfUs7JRpqg1y2fOr-r6_TZof9Fo56yqTpEcWHrv5nS8VHmI8pusfVCyBmWdnV4fgnp-ZHzeWegIWrU4BtAUErV-s_E6I_0iYPvz6rtSezZMLnWCMA13eHdzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a2cfe27a9.mp4?token=X1Kzg2GMUN2Kzl-r5_Zjn--pWiyVM5xUb_xMWgQ3Il8bsx6wD_PjzXjREBU6XatdtyHY-AdUMDJaL1jkawhQINmXFil74ZBuPqpBnb4eiY0jiTcc28cDKXugf5Q6jIb5OA1ceUTurQo6dmXT5ak3rnY1jYnQvQglq-W7q_5Qoo7QL-dg7IAm7zjN5BtATyQ5EBoTo9cYN9Hgpz5ABl14fkzRHYbARwQfUs7JRpqg1y2fOr-r6_TZof9Fo56yqTpEcWHrv5nS8VHmI8pusfVCyBmWdnV4fgnp-ZHzeWegIWrU4BtAUErV-s_E6I_0iYPvz6rtSezZMLnWCMA13eHdzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: نمی‌شود برای امام حسین (ع) اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر و گرسنگی باشیم و نسبت به این مسائل بی‌تفاوت بمانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/663251" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663246">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f284bc3e.mp4?token=P-Pu7uKeO5OUlCGKa9AzbAlwLCoO1Uth6YRyFvaeEWqjXZ34A38LDtkHss1h04BaZaYjNi4s6-AY7J2GD4gCX3FdpLUIGMJ6X9RovosHePvvWdncqexTCOut9e9piqpLMDSG3L-tdoLRHrbsnkCqhVWSo_hsS_mecCtdHSZaPd_jDl3TCbdkZw2oDUPVnhkjeKMxUOAgWt0d7qjHqlKNoZ3rDUkZ1UmasDPT1Qe-L1fXYCCih0gMoR-FTa4CT_nFxKZM0rIn_tnouCW38mxYdB7AJ8ReHsbqvbxZ6fm3WQsmw1Zp9K9zwt_tYDcaLxnZ60VhpqHeTORL7WrfsdPGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f284bc3e.mp4?token=P-Pu7uKeO5OUlCGKa9AzbAlwLCoO1Uth6YRyFvaeEWqjXZ34A38LDtkHss1h04BaZaYjNi4s6-AY7J2GD4gCX3FdpLUIGMJ6X9RovosHePvvWdncqexTCOut9e9piqpLMDSG3L-tdoLRHrbsnkCqhVWSo_hsS_mecCtdHSZaPd_jDl3TCbdkZw2oDUPVnhkjeKMxUOAgWt0d7qjHqlKNoZ3rDUkZ1UmasDPT1Qe-L1fXYCCih0gMoR-FTa4CT_nFxKZM0rIn_tnouCW38mxYdB7AJ8ReHsbqvbxZ6fm3WQsmw1Zp9K9zwt_tYDcaLxnZ60VhpqHeTORL7WrfsdPGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری هولناک از لحظات اولیه زلزله ونزوئلا و خرابی‌های ناشی از
آن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/663246" target="_blank">📅 20:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8xHBuwQwMvRHg34kmhKKOJIyAgKnWbYdM9-5dYzHt2EyjmUaoYBpoI-douT-FJLn97LwFjp54mc3HYBEVKcOOa9oaoccyK1yWJY7wE0GXrlVFb-aAgLYpPcvzcxq5kDhRj8_37QXmuBLBCoG1k0ZpwElDFXD6DQ1rv44SGXv5M_Er5MS3snv7NCEa9PvvcEql-4KOZ7TIiCLhKlIQ6LnUX322-Uyq2wsspDXY3H25W6YSvoy4ZIr4xIeAROPw5qj3x4LN5-xvefxLK8e3V2Ee5kRPBIQS1QQif75eLkI2_Lyllqc7Zig-D65n6Fb2EuB_UYegHYrgDmZvrIAM0zwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر رهبر معظم انقلاب بر روی موشک‌های حزب الله
🔹
حزب الله لبنان با انتشار ویدئویی، تصاویر حملات موشکی خود به مواضع ارتش صهیونیستی را منتشر کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/663243" target="_blank">📅 20:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔹
پیشنهاد افزایش ۲۰ تا ۳۰ درصدی اعتبار کالابرگ برخی دهک‌ها روی میز دولت
معاون وزیر رفاه:
🔹
قیمت کالاهای مشمول کالابرگ ۶۸ درصد افزایش داشته است.
🔹
تصمیم نهایی در این باره به تامین منابع پایدار و غیرتورمی بستگی دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/663242" target="_blank">📅 20:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
خیل عظیم حضور زائران و ارادتمندان در حرم حضرت سیدالشهداء (علیه‌السلام)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/663241" target="_blank">📅 20:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔹
بیانیه مشترک ایالات متحده و کشورهای خلیج فارس
🔹
صلح در منطقه مستلزم مقابله با تهدیدات ایران، از جمله موشک‌ها، پهپادها و حمایت از نیروهای نیابتی آن است.
🔹
ما بر اهمیت بازگشایی تنگه هرمز تأکید می‌کنیم و اینکه آزادی نامحدود دریانوردی برای امنیت منطقه و جهان ضروری…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/663240" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
بیانیه مشترک ایالات متحده و کشورهای خلیج فارس
🔹
صلح در منطقه مستلزم مقابله با تهدیدات ایران، از جمله موشک‌ها، پهپادها و حمایت از نیروهای نیابتی آن است.
🔹
ما بر اهمیت بازگشایی تنگه هرمز تأکید می‌کنیم و اینکه آزادی نامحدود دریانوردی برای امنیت منطقه و جهان ضروری است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/663239" target="_blank">📅 20:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663237">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔹
پایان ست دوم | لیگ ملت های والیبال
🏐
آمریکا ۲ - ایران صفر
🇺🇸
۲۵ | ۲۵
🇮🇷
۲۳ | ۲۰
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/663237" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9e97a91b4.mp4?token=AbNBGIYpBa7Jv9euJHNfO40i6fdaQa0-Cfv75DBzdOz_B64VBwBpMnQ0HNx7ljvhUma4bXKwQrhmFyo0KmF-v7IcJGuqVcfb50miINjCn5xVdHgMsXDHcpVDZhCsXYdIt5Ek1EQwBZwC7a48XMq3YnzBA_CCkJL9KNwP_mxrRemM5znUDC2vzsWndZXamsdafnNmvLqEzV622wH7E-aGV7grW89XL9IxMGn6MsLswbPe92HcaiSFgV3cn2r4qJRAq3AZ2zEx3o7q9xYLiw2i_JDrIaU07FdZ1FxA2PtKqhi4gDSCVhjMWTKFYn5C6AnLYoWHAPrbTiyDCEU2dYC95jDin-US33cEZMFPPGS_3R4JYPYD6IFdDsplzFyOt72M-8SJwvrRhiirjoFhTr8tLnTxwXcxOVXnpcMu-bO57XA0u1Q_GrzXbigvsfGSwOSUAEjVEGsiTUmbNU5Y4uhH5HAIMnOj5OUjFTZsU1coSjDesINXmLAgEARyCixRufqJSt4PGXPTOkPUbx9mbPxt5rrAawLRtNUBSsFz82eA1tEB9NoPuOZYO61uvMFh7aDn8Qktz93DrYcRUjI1xeHhJ1M9L_LzdCy9LKeDA6vUIOjVzpUMuPIKD0oDKIjW1kpb_r7FHQ-M-hjafCSVdkVuvCnBwMXerOhu8S4GoB4V0Ys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9e97a91b4.mp4?token=AbNBGIYpBa7Jv9euJHNfO40i6fdaQa0-Cfv75DBzdOz_B64VBwBpMnQ0HNx7ljvhUma4bXKwQrhmFyo0KmF-v7IcJGuqVcfb50miINjCn5xVdHgMsXDHcpVDZhCsXYdIt5Ek1EQwBZwC7a48XMq3YnzBA_CCkJL9KNwP_mxrRemM5znUDC2vzsWndZXamsdafnNmvLqEzV622wH7E-aGV7grW89XL9IxMGn6MsLswbPe92HcaiSFgV3cn2r4qJRAq3AZ2zEx3o7q9xYLiw2i_JDrIaU07FdZ1FxA2PtKqhi4gDSCVhjMWTKFYn5C6AnLYoWHAPrbTiyDCEU2dYC95jDin-US33cEZMFPPGS_3R4JYPYD6IFdDsplzFyOt72M-8SJwvrRhiirjoFhTr8tLnTxwXcxOVXnpcMu-bO57XA0u1Q_GrzXbigvsfGSwOSUAEjVEGsiTUmbNU5Y4uhH5HAIMnOj5OUjFTZsU1coSjDesINXmLAgEARyCixRufqJSt4PGXPTOkPUbx9mbPxt5rrAawLRtNUBSsFz82eA1tEB9NoPuOZYO61uvMFh7aDn8Qktz93DrYcRUjI1xeHhJ1M9L_LzdCy9LKeDA6vUIOjVzpUMuPIKD0oDKIjW1kpb_r7FHQ-M-hjafCSVdkVuvCnBwMXerOhu8S4GoB4V0Ys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
میانداری مهران غفوریان در مراسم عزاداری امام حسین(ع) در بازار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/663235" target="_blank">📅 20:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhIMvLatko6Eh2mB9ARZdvg3GvDBzdLmTy3L6tYX3S6qf3noix5v_Ig83lU5eO12-kcvSD7jbQKpnlZmS-78aKkpcYHdBTI0QmdzhTWh2SadZu00v9kxSN-lc65AVm8r-hEVZC2H_JLkrmeBZgTwVT5B-uARXpWNLnraCEPmpATa9jWfidceX5Gy4Y6aStFYt8ikbAh4vQAOioh_fE2GnPE1cPuO-gxjRM6BuYp4FkO2eETecZiQPDPZ9NeuI9Ll9RBLArwrQET4f5cppxx5Nq0vtSGHCgfaKSKm54TFEex_4waTHYeF68emEP7_GXGlG3a7U-cQrK6ChYm7TyTJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzx70b6jDBQ5QJTFdrdczABK59qmgcoXesM3vv3QSPv3-IPBugrew_JoSOYcerqCQF_0qSCFXz9hkTk6frdvvCw_yo_fFxgbspAPB81xPq5ap2DvY3MOWZWr65oQbfkkXheoYU9Hfa3HtvTOGPx3_4jyt7p4LJXKmTdkd2vfLVsYoRqLJ2o8yWZcXpFMvfwwa_ax9uU4coUjrN8g5zVxwNBN6Pz4BFkcaEmZACUcsuEypB4pRZ5tCR5w6cMPsNOcgbkL5yNUwA5s-M-A2YDlOq78RiJ4AsPA7Eqj9YH2Yo_re8BAsIe5APUY_39TwqY2B-DzwZh3kuSZKWW3ZZv5Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7TtmBElongEPZ8rOB0K4MxghOB8STTWdMX9CiXyBLr8lP_65OhLKjdzTKTvEH1kvJjNym7iygijpiPCm8LYDblM7Bq0YZJvnmTW4EbIKpxJxnOmoog584d_SC9CJf3PGOtr6-YKxZuKClUrxWvrv1QX9z_x-2VWwSwxDzZi7nYmoD5bRPRxPVtPb2yI6CrYsH0spdUIoGGY4jJvr91cHIkGIPypu0KvVZCJcf5mRD_dZ9nOwCTDHwbLeJazJFiJpAUaKjQGYzGhOZ6cS6VEQ_aGVjBeR3VnA9Z0VIKW0sN9iaguxjjlwV_yfa13DcB1jq5V8Jak1yMABnaX5iMtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqhkTbm6asnhdLYDA0UfOR5cU6Y4rWUALkWQ1PIXPRLbxx_MyWesx-Asg6cOX4YiW1otrJaIncUR8OD-Se75SA9WFrtO6VmU9bGrVvc1gu9aQznu2J-N4gTI6CraDYrqiGUSc0v1WG4Uy8Qh50jM9TSBSpOhOOzO2RaHZxGuMOoNfE6NHELvuI2ZNFZ_vvLRmfmIHzTdDVGP6PmaCPN8Z1NXN2PRsss9Wo5AUOgdMrncbcn8sciYrRToBMzhE4qlCnYq80HiuooHP6MMOYcOPxknnk679zN5UleHZnEoqE44F684jKlQA21_ZMoSf9V7s92eQdHno_y-zyK42n6yCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
پایگاه متروکه شاتل‌های فضایی شوروی؛ نمادهای فراموش‌شده در دل بیابان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/663231" target="_blank">📅 19:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663230">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔹
پایان ست اول | لیگ ملت های والیبال
🏐
آمریکا ۱ - ایران صفر
🇺🇸
۲۵
🇮🇷
۲۳
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/663230" target="_blank">📅 19:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663228">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVG0y05nUSefl0eNaZ77SsKVd2XqpGTEt6Og2DALlbW25Sc0DKV9YBCIK0StsMSKcuhZ-3wryZ0FxD7CUAytfBpLnzdIuL2hF-aS09rZ6qgktO2SRZ0R4s9Ee_8GohdzEBjh9BmgijQXNNs-D_7_WTrgK5-MF5w0hSVSXfOxx7qvnsMLaw8msChuA3NK_DfXH9y-6oXkjMh1AUCFV1bJbxPHdkS_WjGrpEF0F0sHNVUO_r7W8mGJqdEWThUCAZixc9EBM7rDa7xMK8OfE7e_wmpZJxhd_WsSUHRUm64MHP8NsRgCIrDwYjeQJvTI6VdjOXdEv9W8ecHb2KfGno0RQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت جام جهانی فوتبال ۲۰۲۶
🔹
همراهان گرامی خبرفوری؛ برای شرکت  در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و با لهجه شهر خودتان، پیام انگیزشی و انرژی‌بخش خود را به تیم ملی فوتبال ایران برسانید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و با صدای واضح و رسا، حمایت خود را از ملی‌پوشان کشورمان نشان دهید.
🔸
صدای شما می‌تواند انگیزه‌بخش تیم ملی در مسیر جام جهانی باشد
👇
#برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/663228" target="_blank">📅 19:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663227">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm7lCxfGpYE0wAlp52eh2Tz0Y2H9rU72HHYyqPizS5KYrncyN-7qPAN654vBkOIl6Q9MEwCFhqSMLgQP_kDMGeQ2OVUVMmNtO2HCJT3GivDWFX9wFWjlRale9Z9lYHs6tCI0YYFxvH38tjVxlyCNPzK5u1vy-7VFYfLDxF5H_FXKGCfixx7z42Gm4iWB67Ydpa1-kXEh7ojgI7OaBcOOtEi_ZUDNzbtGrHKzcIM4_KSMdkc5L13dyl1qIMvrkbqadbl6UPpXDh4SZCadOsIlmx6S6M8MfqRM8wA6v7ljt9EQ8fbUDaZkpzJPm0IXRJxhcHKEDw52ANnjx9z0Zp0BAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عزم ایران و ارمنستان در جهت گشایش مسیرهای جدید تجاری و ترانزیتی
🔹
نشست تخصصی رئیس سازمان راهداری و حمل‌ونقل جاده‌ای با معاون وزیر اقتصاد جمهوری ارمنستان با محوریت تسهیل تجارت و ترانزیت و کاهش موانع حمل‌ونقل بین‌المللی بین دو کشور در محل وزارت اقتصاد ارمنستان در ایروان برگزار شد.
🔹
رئیس سازمان راهداری و حمل‌ونقل جاده‌ای با تأکید بر جایگاه راهبردی ایران در کریدورهای بین‌المللی شمال - جنوب و شرق - غرب، بر لزوم فعال‌سازی کامل ظرفیت‌های ترانزیتی و لجستیکی دو طرف تأکید کرد.
🔹
رضا اکبری گفت: جمهوری اسلامی ایران به عنوان یکی از مسیرهای اصلی ترانزیت منطقه، همواره از توسعه همکاری‌های حمل‌ونقلی با همسایگان استقبال کرده و ارمنستان به دلیل موقعیت جغرافیایی ویژه و پیوندهای فرهنگی و تاریخی، شریکی کلیدی در این مسیرها محسوب می‌شود.
🔹
معاون وزیر اقتصاد ارمنستان نیز از آمادگی این کشورش برای رفع موانع حمل‌ونقل جاده‌ای، کاهش هزینه‌های ترانزیتی و سازوکارهایی برای تردد روان‌تر و مقرون‌به‌صرفه‌تر ناوگان حمل‌ونقل میان دو کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/663227" target="_blank">📅 19:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663226">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔹
نتانیاهو: نیروهای اسرائیلی در جنوب لبنان آزادی عمل کامل برای مقابله با هرگونه تهدید دارند و حضور نظامی در کمربند امنیتی ادامه خواهد یافت #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/663226" target="_blank">📅 19:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663225">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx9WRA4Ge33pIOUfz2_TMHB5BFQ0PP3U4Do5L04qAbroCDHwcO3oP6X5EAYGvNnwKtwdnXyvhKfD4Z82PaRYfrLLlmrcMrLUdVwXPG94-H_59RFavPhuoD4k256JNAN3HyY9ulR24_BVZ1TGYwljwYxAVeguiA1Zo40wfSsjjdYYJxLL7j_ccDlXTXlt-9jciMi_ZJ1SlIiTGSR61u-vyqah_V1xGaUkbGGwlpKus8B3Cm9NqV6An48PQd5BlLomjuyjmMMefl63AmCntG_YEMn5VRo5Oun4ft5qaWYZCPuf_tp5AS2uitiL0Nk0myPajD9BOto4Zjls1JnFMqqcHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جادوگر مشهور آفریقایی کیست؟ / ماجرای جادوگر غنایی که بازیکنان را طلسم می‌کند/ جادوی سیاه چیست و چگونه کار می کند؟
🔹
انگلیسی های خرافاتی به شدت مجذوب نانا کواکو بونسام شدند. طبق گزارش رسانه های انگلیسی، هزاران انگلیسی به دنبال پیدا کردن شماره یا آدرس جادوگر غنایی هستند تا با کمک طلسم های او بتوانند مشکلاتشان را حل کنند.
در خبرفوری،بخوانید
👇
khabarfoori.com/fa/tiny/news-3225623</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/663225" target="_blank">📅 19:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663224">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔹
نتانیاهو: نیروهای اسرائیلی در جنوب لبنان آزادی عمل کامل برای مقابله با هرگونه تهدید دارند و حضور نظامی در کمربند امنیتی ادامه خواهد یافت
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/663224" target="_blank">📅 19:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663223">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXVRSl7cyEtY0k1-DL5cUV03lcOjLL0MLmzacVJtneKbR_zisXiMSPfCrai1noMxFiR4bVcbVsPsRl8OTVxACJASy_46hqjSkYYaqjPaPsyvonhw_By6Y0d4KpHFPX3L8xcR4ziZ2EWyzZT_X30aKcftk6LgtXk9OU1gk4Dl3TRQluOzM4iAcCWD3oLmBiam3zLqNDvvM8i2Xe6XJKZLj7pAEDDBmVP6OXb9jQUN7ARlRDogUDM7cA-UfNI4hhcF7NHpUUcBJmzHJpDaq2Z3BT0oX1X_yF2wf1zdVOiB4HX_RIJPhUIgH2Dxif-FqRcYvMIuo89Atz69xkiwJGrO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/663223" target="_blank">📅 19:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663222">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔹
ملی‌پوشان والیبال با مچ‌بند مشکی و شعار «ای ایران» به مصاف آمریکا رفتند #ورزشی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/663222" target="_blank">📅 19:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663221">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔹
گزارش‌ها از وقوع حادثه دریایی در سواحل عمان
🔹
منابع خبری گزارش دادند یک کشتی باری در فاصله ۷.۵ مایل دریایی جنوب شرقی منطقه «داهیت» عمان هدف اصابت پرتابه قرار گرفت و دچار خسارت شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/663221" target="_blank">📅 18:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663220">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329af23c18.mp4?token=fFq45O0CBpk9RJx8vdkbY6xjAYY0CPBOk03vE7b4rzAXGK8llj8qL9Pw4oFVwCNvP7frBr-DnlI91t9g-Qc0Fpy9p73bDtbvCJ-duggvB7SKycGwD641-YRYDvpHELCoaKlV6ayEc5hnZz_-ccQlViCr9DcpYiocEsL0PT2Ht6WnhjQZGGuYa9tzdpm4VCL2XL1fiHmLCnc6sU6-Lujmghy5Qij9HAL-wb8u7vSAhxph3T-a_ahlD35yyU-DnGCUION2bJrUanI7wIfdnH07DRYZ2fPaT8xvKbuNMD9KB5Ku0RHodA5PJ_Psr-0xcRkbrZjSvO0KjixSp0NLlBjjpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329af23c18.mp4?token=fFq45O0CBpk9RJx8vdkbY6xjAYY0CPBOk03vE7b4rzAXGK8llj8qL9Pw4oFVwCNvP7frBr-DnlI91t9g-Qc0Fpy9p73bDtbvCJ-duggvB7SKycGwD641-YRYDvpHELCoaKlV6ayEc5hnZz_-ccQlViCr9DcpYiocEsL0PT2Ht6WnhjQZGGuYa9tzdpm4VCL2XL1fiHmLCnc6sU6-Lujmghy5Qij9HAL-wb8u7vSAhxph3T-a_ahlD35yyU-DnGCUION2bJrUanI7wIfdnH07DRYZ2fPaT8xvKbuNMD9KB5Ku0RHodA5PJ_Psr-0xcRkbrZjSvO0KjixSp0NLlBjjpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ملی‌پوشان والیبال با مچ‌بند مشکی و شعار «ای ایران» به مصاف آمریکا رفتند
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/663220" target="_blank">📅 18:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663219">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f38b22475.mp4?token=joO0QsAtQpfKPEha3Nd74A0czlwrNFkgGxGaBLsx06KH_DmwovE1CetWd6l-C6G2dggCrJqK-VCb_Wu2DFVLb6uEt5lgJVzVE08wGeZaEJV3AMm3EOpvAbE6PXg_DFURzLd4DvKT1h07ERDpTNQbC19F7Gs5Vdo8UfQqfi7oKrIbt6_x5PgYR0NNAlYbtiHgqSzCRs3iqTD9vhrhT0LQXiGWfEXwb5B7vcYLQKP9ePBg4zSaMNVra8GhEAqou5Upt660W9ujFHhRHgFe0b2waetGKrCFWnRXpQNBhZ6rGrhSxod4IFMKa44IaZsLyc26-RXsIXo_qfFgV0dmBQ-Dbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f38b22475.mp4?token=joO0QsAtQpfKPEha3Nd74A0czlwrNFkgGxGaBLsx06KH_DmwovE1CetWd6l-C6G2dggCrJqK-VCb_Wu2DFVLb6uEt5lgJVzVE08wGeZaEJV3AMm3EOpvAbE6PXg_DFURzLd4DvKT1h07ERDpTNQbC19F7Gs5Vdo8UfQqfi7oKrIbt6_x5PgYR0NNAlYbtiHgqSzCRs3iqTD9vhrhT0LQXiGWfEXwb5B7vcYLQKP9ePBg4zSaMNVra8GhEAqou5Upt660W9ujFHhRHgFe0b2waetGKrCFWnRXpQNBhZ6rGrhSxod4IFMKa44IaZsLyc26-RXsIXo_qfFgV0dmBQ-Dbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ویدیویی از زلزله ۷ ریشتری ژاپن که صبح امروز اتفاق افتاد
🔹
هنوز جزئیاتی از خسارات احتمالی این حادثه منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/663219" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663218">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFigtNwqyAZQsJEXm9KI-JpDjNiEJTUGx1K09Hd5qyBUkV6-NNpUYlgw0a8lkPnxCrLYtoZNdfEppTf7EqhnGyTx2uV47I60E8WDEn8ww1T1XGdCHdONm9Y3f3GtdEAByopRwABIDmag75QMml8H93AGrunQK64fBKSlAWecshsL9gEw2ECf2kVgvifm9jNzw_SRnkjVUhyo2ZPDlN_V6k8XzP0268mMJq_fXvobPe7Fas6-R_e4enbQkbMTv1uUxQvrH2RD0NN3GrdL8Grn-a6OpVB-EIGtAzvO2nXbrOWZr-UDIxmhILQ-uWIH9XUtqpyYam7wjnngFQdqdhuGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
توافق ایران و عمان برای تعیین چارچوب اداره تنگه هرمز
🔹
در تماس تلفنی میان وزرای امور خارجه ایران و عمان، دو کشور توافق کردند که گفت‌وگوهایی را با هدف «تعیین چارچوب اداره آینده و خدمات دریایی در تنگه هرمز» آغاز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/663218" target="_blank">📅 18:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1PANeAU6g0k6lQUcKr1XYdmo-Qxu9do1g85AYzDm4jwCXx46S1OkOcN9Zoskah_DtNYHP-8sh4E224issCAW7dQLexwb0UuhqpXCmYwnIjOwSDeKovLjDNwichx2h_DiQpZaetsqD6LogQXQuYMpBx2ZByvF58rMx5nKa1Tpg00w69mMpEzOim6YrNO04f3lKuC-94ookstPgsq334tlh8Zn3TbmR3MAQykhjtk4q1SWOLD8MRPTToNIPnYI3t6mhEIUrwv5H6rfD5loCYmp769wjFysuVMwJPpnlR86kng7jBwAtHvB13wQGZZY0l5_Rp6f-8qSyaOXYGepm0LLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
گزارش‌ها از وقوع حادثه دریایی در سواحل عمان
🔹
منابع خبری گزارش دادند یک کشتی باری در فاصله ۷.۵ مایل دریایی جنوب شرقی منطقه «داهیت» عمان هدف اصابت پرتابه قرار گرفت و دچار خسارت شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/663217" target="_blank">📅 18:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663211">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgSYexz_vwAz5yjiCynA9DH83dw-sB8rP8vOvE2kWRF57FQ1eU-o7s0Z2qWs8poAUI-EHz6Lt6K0uuHU6rdAgr1Z6SbQWHajmu6UM7Eq-l5oTRjo4awhRtQ62UGAczZ0hIZ1CI7ZHQOYVB_1fnuaQZeEBrtaAoVqDvCnyk1jDUwLs64gZB3qK-ABsKMEwb-zcLKe5rE4Ui6HDY-ZFSRNdGu7IMPgnVU-TkJIu2hZ_3iKOf7SjrAuL_EdprU2bUeztzmAOlOeMd6kyJPlOEnzRtyL1zEEwxsX2sDSu3Rn9YMbVzEh7-lZwd3BJ52ru1GMleLAkDKWx9GVOjLpXbRBlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UeUAmXpceufRqzA0-d2BForVIirYADndyC2RRc4X-6Ll-uZ8psZM_gavQNgN5JZaJMaOt1aFf38M__oH_zpSmT7eaffLz-NQlUfwjSD_KV6a8gGy7_aXDhO3jOmuGT9xPJfcMdPXmL0s9lO6U65udeb_Y1Pf75599kMyQzfIuH_oFzrAffw8dXdxYsM8ENb7S5wZbvD6-2Fsi2MeCV8kOQyxhxPEjtlc5_oGDsoWROrJY42g31lflSb4dsv3O5Jw_kPpHFxBrGBeG8l292nfe2PPIX_lPaQNUycio6gEmAqpFTPwN08fy_B_nHUpUrghLY9SAXMbsVWFHD4BIxZfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xrmqas7PM5DP8DfTn0H-4Eu3_kvpPGwS7VA3TMTzqhbxFR0TxKbGwwFZsPOXJ415kZ3MBLli0D2a-wgLXcgtfUNYwHDuDTmUnXKdWGJ5aS9RzXws4VHUe9BYJjMezJSw4Ddc0RwiEdnAEHZ-e0IdA0-282Fw6RIvUDWm-TF0VkCtxs1JI00UOjvBBe910m_269Ty4i4NzttOMsz65QFMdCEomqFb0E2EqMI2DsqGVjCTQBu2wlCElz6Bpj5iJ3tN3ZA4-GMNwBhHS0VS2JNl7QCY3NqpRfs-HMg2AtxdlC9vv9ULbZbW-PwWZGzqI4LHss2u34mGLB2TeI7T1klSBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfRdYB3_gMK62MpR8N8g2PCY-SVp00qeJOhRdS6c7QXSE06dQeWFOIV-F526vtyZ6NfZ482SSGc-LmT3KUCzFmmMqsya_uxj5tgJOH2sP_ROJw_akvK8plAP2qkROsFjMD5xohWYouYDVG0_fwbxjAmg2biLmvZR1TU243vFD50ZlE-H0v5COj_0XpwThvz42OYTtjtATgwgS3rf3-_YYMByZwzVjP2IkrXllsYiJ1Q0mNrh9EBgjqhG73NLHJm7LzVqQdcqsm1-WmARLgaFcoO4_hKn4EnDXR97-tvdQ6Ocn6pdVqK42Pjj_6M19nZwcHnmRjUSIbV4vH8Ged7SXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sf-cdkIEN-mOIsCpePIPPCj5Lj1RiaPke9V2ZQuG4Xf9TKuMJIDgr-mNAdAX8E5S8pJ4Mld3Z4zHRWogvLJEar-FP-Mu_OAXLkUHKDhwWuDgFKq0SPMW1XuO7k3aPkPwNnUwtFyCvJPWsQRmwEVv7nSa1KsyJun018X_zR4YdoOSV6RdUPz_b7r0Qgy0NXwhwCOrHOa_DsoeG6_ue7NgtiulKOIpIzdc5hKE63CoBrejSfrmO2l7J604Ej_sAOMeC_FZHMtuJPaqRPZNIGN6TlUFtvX2wtvT286sfYm2z1l8BW1A1kQAijKjzLA8y5Dmx2qVzoy_AGdKQsjYBUpEuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
مفقود شدن بیش از ۲۱ هزار نفر در زلزله‌های ونزوئلا
🔹
در پی وقوع زمین‌لرزه‌های ویرانگر در ونزوئلا، گزارش‌های اولیه از ناپدید شدن بیش از ۲۱ هزار نفر حکایت دارد. عملیات جست‌وجو برای یافتن مفقودشدگان این حادثه همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/663211" target="_blank">📅 18:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663210">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای وال‌استریت ژورنال درباره طرح ایران برای دریافت عوارض در تنگه هرمز
وال‌استریت ژورنال:
🔹
ایران قصد دارد با دریافت هزینه بابت خدمات امنیتی و زیست‌محیطی از کشتی‌ها در تنگه هرمز، سالانه ۴۰ میلیارد دلار درآمد کسب کند.
🔹
این طرح با مخالفت آمریکا، عمان و برخی کشورهای منطقه که بر رایگان بودن آب‌راه‌های بین‌المللی تأکید دارند، روبرو شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/663210" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeAQDeZXaDbnMAg7KZvaxtM53ezWYUtDAUOpHYiIVnE25oHrotHr9alqgOm7sO4sehU4PRJk5roZUdWeyuJfwUBEv2f1Vcrp2nuKJv38eO8BVpHexp699K2Jz_Rdo1oAa37T8lx129CA0-xm52nSAXrlCsvGPmL5hK_gHVXevr1sNOwWXy52A4U-JMMIJZJARYmsJ5JlhFyUBzJkhhsag5a7aQUCFVRoI_UYaoXez4BH5aMEianrWWv4uSll86ajbtS5Xk93byjqIsMhzLekv0xaSYi_su1tWqhmGS9VJOQ-97giGbNHsh1G0Ybg52IU0KytTlFM73q2mnhRTfHDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
لیگ ملت‌های والیبال؛ ترکیب شروع کننده ایران مقابل آمریکا
🔹
بازی ایران - آمریکا امروز ساعت ١۸:٣٠ برگزار می‌شود.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/663208" target="_blank">📅 18:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663206">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b88b3e8d1.mp4?token=scG3L1VJ0a-85K4zXTgFdASjXReOKRRsjbUN0KXFFgPnUVxleFFRYfVEM_NJ0xCqaQRsZln7TDIwbhZcBlkIPJdubXF3TTCdaZ2syqygdlUYj-ykXUNVUAwuD9S-YoA0Gm5EaYFYVDV5-vir3NREEofZGwVWM9Z9KpG4SWI4o1q0F5fjmKMTdzQ5X_jrPM-Q3-v44iUUdAmHKfFYmpqAc61dMPbPqvJXOtHUp_H19AClfb5PZzYflpngA8mFRVEw259xRYfAv0-uimrZYoWsxd2ox1WYVHjUr16_YQjoL5hIqfFNRuj4vkZJda2iedIna24jCuebtStj1P_sBOMxbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b88b3e8d1.mp4?token=scG3L1VJ0a-85K4zXTgFdASjXReOKRRsjbUN0KXFFgPnUVxleFFRYfVEM_NJ0xCqaQRsZln7TDIwbhZcBlkIPJdubXF3TTCdaZ2syqygdlUYj-ykXUNVUAwuD9S-YoA0Gm5EaYFYVDV5-vir3NREEofZGwVWM9Z9KpG4SWI4o1q0F5fjmKMTdzQ5X_jrPM-Q3-v44iUUdAmHKfFYmpqAc61dMPbPqvJXOtHUp_H19AClfb5PZzYflpngA8mFRVEw259xRYfAv0-uimrZYoWsxd2ox1WYVHjUr16_YQjoL5hIqfFNRuj4vkZJda2iedIna24jCuebtStj1P_sBOMxbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
فیلم رنگی از عزاداری ظهر عاشورا در سبزه میدان تهران سال ۱۳۱۰
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/663206" target="_blank">📅 18:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663205">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbLIKuKl6cW0bkAO7NNt0AkUKTvagJbxv207StYAuQkS2pCmddq6l9VQ3A8QLSjtch6bJZIosFXlRkOqX5zDMh6VyupoRTOh5q9BfzYJo-MUQwB7SDWMc2btO8VS1iyDYQTxHNTfi5eYOOPFEHJLmXH6o-zVQM3ejIsmc7rjfxBjuoXSG7zUAz7P7CFI6oy5zikaOV9aaW8xstzU9hFq9QGYPFw0puS7dHXEdAQCav4qC5UcC3riH_yc5wkKMK8kozCt5PkFUG5Rdjtrila1WNM7RC-Jr5ocSMW17MbrY4Xz24HkXAhK566Rf5rVz8eG_DwRhI9MHJVzzTOy7oOpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مردی که راز بزرگ پوتین را فاش کرد، به شکل مشکوکی جان باخت
🔹
خبرنگاری که برای نخستین بار شایعات مربوط به رابطه پنهانی میان ولادیمیر پوتین و آلینا کابایوا را رسانه‌ای کرده بود، در شرایطی مرموز درگذشت.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3225606</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/663205" target="_blank">📅 18:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663204">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-SUnRkpWaYWK7TGsbDo7wKqAyYcTWwNvGTWP31bgCRpVIvP8BAzbAhCWtW6mfaVgjZVCdCbXVgdANfbi2JgCvSFFBiAim3Xcwpy0K-A_ijTm4uZo_bF6WCDJM7uym0Bpx_YpvrKsIHveGLF6qIFB_m6RRMkcXRRF-90llE3Vi9bkPOCCAHvvp01W2kBhl5W4LOrGF8lZ1ad23C0s7BKl_0fpi1AW2tnxWLowAxClBpVJbhX4fxYobGNdZWd4hqgLdzzMy3n0rUxpRMQqzqxizlL4NriYaGflKE_BDLugTCcigsaBanC0rv80V_gx4c2hb8Nhj2QhtdFUt3Mi8gG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سقوط ۵ درصدی بیت‌کوین در ۳۰ دقیقه؛ پایین‌ترین سطح در ۲۱ ماه اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/663204" target="_blank">📅 18:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663203">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391d9fa18f.mp4?token=NtPLjqqGx6mnGx7ODto_rHeeVhBH7n98YtWFgrQBamE0YwM6Fw7hoKfixRH-lMaXnI4Yaav0dcFq8BN_ntn1KKU54YG_0khTU5YbFz5kAkSTk-QoLTLhoJPLcusl2gKiYDkSoxGROKJPVLC5cAUWSRTnE_TYuLZ0c00VgPYgdNL2vVbw-7JnqdvMSYBUQuOMT9esmSyGE6qb6Bxg9pXBbhQfqI_pMCHrFQyEynODVFtaD-ouBXKEVz2pVsHBsIJkcyITaLMJZML38JOOVXTlPa8Jbo6NikQEVbpDXC4uyZ1BzjLWbNb9V2_oSDog2UPGUmFb2pPkdFVHYXI5ZfPWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391d9fa18f.mp4?token=NtPLjqqGx6mnGx7ODto_rHeeVhBH7n98YtWFgrQBamE0YwM6Fw7hoKfixRH-lMaXnI4Yaav0dcFq8BN_ntn1KKU54YG_0khTU5YbFz5kAkSTk-QoLTLhoJPLcusl2gKiYDkSoxGROKJPVLC5cAUWSRTnE_TYuLZ0c00VgPYgdNL2vVbw-7JnqdvMSYBUQuOMT9esmSyGE6qb6Bxg9pXBbhQfqI_pMCHrFQyEynODVFtaD-ouBXKEVz2pVsHBsIJkcyITaLMJZML38JOOVXTlPa8Jbo6NikQEVbpDXC4uyZ1BzjLWbNb9V2_oSDog2UPGUmFb2pPkdFVHYXI5ZfPWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
خاطره‌ مداح معروف از رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/663203" target="_blank">📅 17:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663202">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02b627be.mp4?token=e4vUV8lZ_bmO-OxoU228csUbXBdpfDfeLlp5ts7DzN_KjWpjVdUt3o_Gb2CuKKtfE26KCRJUYRbkj29n2Cj2E0263RLRyDvsh70TFjLwiwkkmroIg6ileUMMKUeW45AvZJQf9nL-zhSbuHaKT-3lpgc2JHu7H_TJ_0_7e4ZbnlFKBwcb871LZ8kKDQ6e9IX6CZfljjOQK4fUpwAf_PvXUKXsW-VMwkwCbbBLBi4pel39q1RkIuLp0tMgH7Vt3BZ1h7ExLxovlDgM8po48-Wo4Js2F8pf6sjlnjHURHJ6zn-H0mUiRqk83YvG2zlRKH94VO2qbtqJTXVXmaNm-Ky-pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02b627be.mp4?token=e4vUV8lZ_bmO-OxoU228csUbXBdpfDfeLlp5ts7DzN_KjWpjVdUt3o_Gb2CuKKtfE26KCRJUYRbkj29n2Cj2E0263RLRyDvsh70TFjLwiwkkmroIg6ileUMMKUeW45AvZJQf9nL-zhSbuHaKT-3lpgc2JHu7H_TJ_0_7e4ZbnlFKBwcb871LZ8kKDQ6e9IX6CZfljjOQK4fUpwAf_PvXUKXsW-VMwkwCbbBLBi4pel39q1RkIuLp0tMgH7Vt3BZ1h7ExLxovlDgM8po48-Wo4Js2F8pf6sjlnjHURHJ6zn-H0mUiRqk83YvG2zlRKH94VO2qbtqJTXVXmaNm-Ky-pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، از افزایش شمار کشته‌شدگان به ۱۶۴ نفر خبر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/663202" target="_blank">📅 17:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663201">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b20ce1d3e.mp4?token=P9HTXVM9bztDC89oQJfGql140vAsXQeCyx_2LPXgwqSLMrsJojVGRcPlV08s5Bqu8pIYmhgjqWqs2EdzJ6WnbfXR2p6gFIB-qEn4lWBS63P42JwWo4LxYcY9gRSpOiS4GRbQeCHaJEM6ABp2dMtRVYA0tkH6KkhXJ8zrkMHARXg1dzHeIo9rcxU0yYx_HrzoDV-sB8pTlXRa7S8kl6UjIMifaPHiV3k98GoittvqIxJeX6Fck770SYqALlSk9_nMDJ7X2w6t1OxncGxmUT2UEoFqz2_iqcYUpnUTB1iieaTQB3rMLZjYWvS9xQB6duZejaaq_YOZgmyxi3lcXfArPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b20ce1d3e.mp4?token=P9HTXVM9bztDC89oQJfGql140vAsXQeCyx_2LPXgwqSLMrsJojVGRcPlV08s5Bqu8pIYmhgjqWqs2EdzJ6WnbfXR2p6gFIB-qEn4lWBS63P42JwWo4LxYcY9gRSpOiS4GRbQeCHaJEM6ABp2dMtRVYA0tkH6KkhXJ8zrkMHARXg1dzHeIo9rcxU0yYx_HrzoDV-sB8pTlXRa7S8kl6UjIMifaPHiV3k98GoittvqIxJeX6Fck770SYqALlSk9_nMDJ7X2w6t1OxncGxmUT2UEoFqz2_iqcYUpnUTB1iieaTQB3rMLZjYWvS9xQB6duZejaaq_YOZgmyxi3lcXfArPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر علوم در اجتماع شیعیان ترکیه در ظهر عاشورا: من از کشوری می‌آیم که یکی‌ از اولاد حسین بن علی به دست یزید زمان کشته شد و هنوز پیکر او روی زمین است. شهید حضرت آیت‌الله خامنه‌ای
🔹
و فریاد لبیک یاحسین توسط شیعیان استانبول
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/663201" target="_blank">📅 17:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663199">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e9c4c4b7.mp4?token=FxOl2ibW0c-TxqzRmLjqsIcauhT6OUNv2Quj2SRbNc8ZhziYEthwnMb4iu27JQOLmBCMN8-TJxSlYa7NZFeq_BFpg7xRmMxcy5tjD5iQemdywOq0At6cF0iT153BxvnfJmt4r2exN2RCwI2f96nGA5pFNzWzjfUZQo8Tqvn1J5UGJKgVq5-jyPsMId1u2orSVYVMKlccsH4Niwgfl36dxjr4hHNnYvNoy2Q17DKX5rYOIdlnOT9xjyYSpGvenneg9XPAneuiqxyzQCH_0zVy2tOCY36n2NJKs8C3yG9dgb_Ur99I7TZasP0rMuhcL-wlDWH4ypCH4bCB0dYP9f-bvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e9c4c4b7.mp4?token=FxOl2ibW0c-TxqzRmLjqsIcauhT6OUNv2Quj2SRbNc8ZhziYEthwnMb4iu27JQOLmBCMN8-TJxSlYa7NZFeq_BFpg7xRmMxcy5tjD5iQemdywOq0At6cF0iT153BxvnfJmt4r2exN2RCwI2f96nGA5pFNzWzjfUZQo8Tqvn1J5UGJKgVq5-jyPsMId1u2orSVYVMKlccsH4Niwgfl36dxjr4hHNnYvNoy2Q17DKX5rYOIdlnOT9xjyYSpGvenneg9XPAneuiqxyzQCH_0zVy2tOCY36n2NJKs8C3yG9dgb_Ur99I7TZasP0rMuhcL-wlDWH4ypCH4bCB0dYP9f-bvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویر تماشایی از فوران آتشفشان در گواتمالا و برخورد گدازه‌های آتش به گردشگران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/663199" target="_blank">📅 17:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663191">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUxrQoG_GNkqQ_4VyhBrR1QUyW2PsbhqajTCHSfVy1JL5OvXvgpBkkx0t5ZBJaKDwSubCdH5kudvlwDHVc-YrWiA7dtdN-x7g4HcQNPNJw-JcplGlMY7j1WFrxgUeWOS3xhW31d_U5xR-GcEQsCKWdTRSSwk5WL0EYw0ah8FIjRi4_5PFeQaJbtSSIAjnW9EPkJF_cpuKEah0eoGRSN0JB0411pQDShR7BhPD5TDU_d9WaKCz03xQC54-HFfWJBKhw2Hms50G4leMSB724prG0WcJ2oxOp-HrQ5cBuq2_x4SA52GKBfPFROTKbAz90FXSCbAaWR4FjRHfuKdo19_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4qPgIAwTagL0OAj0Hu9rNHvIrPKyy7j1UmYr4d5a1kWzBu0G4R__cZh5B3KpJnOGAlozufg9xwj3vDjj-MQnV34djG6vff-xSvQE6lb-A-jbwj_TPUfZBRKfAT3AwHe7tI6On3g9Ts2vLUg9adFXRLV5DhzH6cRLYVrJwO_exJKqumpSM2bEmYnBZMiUtv8ARsu2eC2eOaCN-iPo8rdBwZyATVybzUzXokUW-CI2trUr_RaCMQPtq_C8f_0AIcHI18-U5s81pQsEcnyR6ED6jMenwwSR7VUL0ZRMGlVpkFcE-xdZahBKJZIGQ5Rlx_mGjYvP7t3g09xZYib0Rlb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X22HXmYcGT3t7pmWNul5AJS5fmPXq9aU9IeiUUyYt76L_ttiRIRvloJwI72qTBCZAAF5wuwVLx10DZF1WnWpNN3cTq-NFLhHUqosrXh5ZSaW4SabPjmZKkSOKJmdvn9leiFxM7z99Byl0ODuazNytyVTweMmE_Jn1AmemUkJw9sGsJoFf7POozt7tXx9huU5Bx5OJ-V5lzW4pxwX_6ghV_FkxiR7_jF4oVL4xV8txqpWWHgr3QEcCI5k4RrhGwDWUenuX-Vu0iVczpu5S8VC9qr0C6wYs7qNAs8zFwwlUYAs3TvFeY1Ofx6kItVHoIPG7hgZSVbpP08gneVkjDtDDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozdoOen3FwX3f9vHB_mdJG2mvgVwItfay4_5Ihv2_RAUDwONlXwMdLOqVBhTrsJ6xy01bHIuEjNCc1rP8kBiRhQgLwFGZ8AuoX2Hj4XvheeLOQmlH30-7xOXiTSb5DcItBCsZ9hQLM6GLxQGqKCS-HkrvR6yY7dpRAGs8lvJBOXWEpA4q_SXGN3-ZFSZ_0kCBVfiZrAKIjIbmbTqOAYzDsh_DVyxvy2nvYUoJdmBm2RwgfxC-eU0sL1VLNql0DG2dI6dcaprGvCkYHEEiKfTloDk4tGODL_BFGCUI3aNBrJdTcxAAw6h2n5suNKSuZsBZDxc7Zrr5Bw8LZYU0XaJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPmYkD4RDh2rfb1fEL3ER1mVmVJxxfcB7YdoTMszrUOxi_iw4x6dXqxwvTQNTGb8K2hNCMIkBtIgzvEUeYpPm11luedtFx1RG_A__RtV4gF1H8Dw45exR2AwGhhRfUHvbierhr8ZS8F3NmH0uHfuKmRAQ_zvsDMhUOEQP60Skq2gSMUP0drHnly7unwXcUJmqx9CEY6eZkAgxAdxgzF6CTdeHhcg5bVYtidBtPw94K_gPolf7nj_qWBbwoYu1V6svxZ3vpj4bNNBHYJ5PxaOFQxmyIyHHlK3OM_jHcaVPb3j6Db5vdWGkCe-Ezq4NIuevPElfSq3G587ESqflulhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNWnGNctYBnB19oJUNnlLgRFNlgn-QVwXpif8UmsX_ZqyWqSHG5SjcRx8HeDwGFgc-qRJC230WgPyhKZKmCBAbAtysOH8ITcvV7FxbPmpu4OsGlaQ0K9WXCU7-NieMkoF1GeVFKPH3sVjwOFLwqQ62qyUhEO7UwHH4Lt7Wx7I6DZJN9Md__h4FGNpbkUyOCb24oGuEa3vBT9k1YEnj5JKr6K9pAb744gUzWjoLmAyn6bK04qT5O3QM8ErXw42BB-Pi7YXUUc7WvhoZFBhyF51iwUlJaNizlXiYunk_ry_3WvRLowCp54l-eY7N5SwGRwoQV8J2akqjzZkkA62IGvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAdDNWuf5nlylX1jZhAihU-_bQqEaU6WFdFDGl4QSOgmu1w9eVZm1o-gTsUrPqDKnwf5r7W4-NOCE2J6hE3wjwLoVdojHzzyFqO4YA6MG757eA5ZsevTVB5nuIn7iLM0lK-iogT5JppZcfdkQt1uTxNZ58ylFdGUDdMK0Cxd0ceQJhnTQlOJLjS9DtcPyUePAItaVpgzAvn0EplS5ZvUbdZ9hB8vMGFdhXiPLP2xyRCYGW_oqakjfn455GdlLasbRp4KtIgBXkxWQLKRmjyKURwtQeO1_axJIpLoVEur0ryQ7xqxzB-qaXK_CoZPa-CdiTWaxn7APC8ORVOxiZH8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpyaKZiU2p4RRGARmvVJs-AnrMDpI8xvGOH2JeZ1qahPNQbaGPuLIDyB9hRVpWVZw-ssmQ_9XvxFH0xPaLDp6aqBMOWK0_fivhdX243KgPG1_M8-bS8RAFr_kTy8cDo1gxONeiuN3Bh9dTBX97tRJ_2xZtLqw8tzehKrwWKJWsyK7tLSMcOcLnCbrHnZfpYZX57ZhiaqclEJy-wmgZk2nn6TeCzMAY9foKaG7P6GceDDhVZkPyykowMnItQ4Xrn9e7qKeZwGGcYhrRKddwcWB7l4-nNOljQVyRWhCsd_s_NiaBOwrBkcd-plFkLydB_OY5YfPpVMHKrof66H5V19PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان حسینی
🔹
عکس‌های ارسالی شما از گوشه‌وکنار شهر؛ خانه‌ها و محله‌هایی که با برافراشتن پرچم‌های عزا در سوگ امام حسین (ع)، شور و شعور حسینی را به تصویر کشیده‌اند.
🔸
تصاویر خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/663191" target="_blank">📅 17:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663190">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
ادعای جی‌دی ونس: توافق اولیه ایران و آمریکا برای ایجاد کانال ارتباطی نظامی مستقیم
معاون رئیس‌جمهور آمریکا:
🔹
در پی مذاکرات سوئیس، توافق اولیه‌ای با ایران برای ایجاد یک کانال ارتباطی مستقیم نظامی جهت جلوگیری از تنش‌های احتمالی حاصل شده است.
🔹
ما به دنبال راهی برای کاهش درگیری‌ها بودیم و طرف ایرانی با استقرار یکی از اعضای سپاه پاسداران در کنار نماینده‌ای از سنتکام در دوحه، برای حل‌وفصل اختلافات و مناقشات موافقت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/663190" target="_blank">📅 17:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663186">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfae89a7e.mp4?token=l1MHSjwX4CwOdnmbypjFR4qevopD1XCPOnfpppviQEFuV2LeUUcgyiM1QtxffF8OM2aXZaTr-vFj77xmDvoVWZ6CtIKvL9-jLoYLvGQz5tF2ydpy8CtwkigtCJfFURjHcXQlVES8jk8p3cfDXpg1ivk-xOrm0Qv1M1XUpw_ip-9mqejFInhbqlILxRApY4TtcS8ON27G0jZOC43PBohQtJbu-lv7YC7OP_D1Th38i81kwovFOv-mh9aQPVD5OJ39rtnbALsAsaGdKWoQ6ASZ_4yJp2HR-YwbbQ_1fQUSw5zYRuAgizNqtzLUmXTLRPO9mZmzb4TCNTpR37GYenPQAwAuc4L3Msiny3phYJ7KpFWkdXAdrWVSM6gUXUvVR-W_-tSLmT46lK5vro_mtmE-mXyw_K__zmlIXM9iwf4f7n_PLPBgzcOxPWbVme8N6RpE31s9H_nofgZ7N_Jg9dpdwdQdv2uNbbrBLZ-OXBumb7ttS4Vbgo4l7-aIjpcX3czkU3mJhdHj_zcNmCUWSR4dZ7EAwOghNLjgs37lE1rSc_Qh3njNa_PHtDFWXS2TY3GhScrySLwmg6LQn7uhPqfua86HB5GL8FGXJwP9PqVLpbpOq4sGZ9uwWqxDv2BoCtXEFFOwxa0xKuP6Zs5EZ2YfsmhqGz7so8ep0igKU1l7mgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfae89a7e.mp4?token=l1MHSjwX4CwOdnmbypjFR4qevopD1XCPOnfpppviQEFuV2LeUUcgyiM1QtxffF8OM2aXZaTr-vFj77xmDvoVWZ6CtIKvL9-jLoYLvGQz5tF2ydpy8CtwkigtCJfFURjHcXQlVES8jk8p3cfDXpg1ivk-xOrm0Qv1M1XUpw_ip-9mqejFInhbqlILxRApY4TtcS8ON27G0jZOC43PBohQtJbu-lv7YC7OP_D1Th38i81kwovFOv-mh9aQPVD5OJ39rtnbALsAsaGdKWoQ6ASZ_4yJp2HR-YwbbQ_1fQUSw5zYRuAgizNqtzLUmXTLRPO9mZmzb4TCNTpR37GYenPQAwAuc4L3Msiny3phYJ7KpFWkdXAdrWVSM6gUXUvVR-W_-tSLmT46lK5vro_mtmE-mXyw_K__zmlIXM9iwf4f7n_PLPBgzcOxPWbVme8N6RpE31s9H_nofgZ7N_Jg9dpdwdQdv2uNbbrBLZ-OXBumb7ttS4Vbgo4l7-aIjpcX3czkU3mJhdHj_zcNmCUWSR4dZ7EAwOghNLjgs37lE1rSc_Qh3njNa_PHtDFWXS2TY3GhScrySLwmg6LQn7uhPqfua86HB5GL8FGXJwP9PqVLpbpOq4sGZ9uwWqxDv2BoCtXEFFOwxa0xKuP6Zs5EZ2YfsmhqGz7so8ep0igKU1l7mgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
آنها
انتخابی نداشتند…
و نباید بهای فقرِ بزرگ‌ترها را بپردازند.
👶
نوزادانی هستند
که از شیر مادر محروم‌اند
و تنها راهِ تغذیه‌شان، شیرخشک است.
در این روزها نذر شما می تواند
🍼
سیر شدن کودکی باشد که چشم انتظار یک قوطی شیرخشک  است .
❤️
نگذاریم
هیچ نوزادی گرسنه بماند.
💳
5894637000012820
💳
6037991199529904
💳
6037991199506100
🔖
IR
710170000000216780692009
📞
*780*35260#
🔻
پرداخت مستقیم
Mehrafarincharity.com
⭐️
مهرآفرین باشیم
|اینستاگرام|
وب سایت
|
پرداخت آنلاین|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/663186" target="_blank">📅 17:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663184">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4882bbc4f8.mp4?token=BVZxd-_EpmqAnMVTmpjvvkM8xNXb6SqcudfpSyhS19GqZdpZ-bW8WrnxER7hR4MBjAYoFWsTnjMiVCtQuLE_KADo476IAHNZE0YrpVjpSH6-gh41s4Oab0MuEUr7x3ciT0g1pxT6zkAzEFVQ4cVDVBL7E2lRYWAAuurAxmMvgSa1liPy6JKIn6DUMay3P7cFNYAY2oBr6dukGnd-PN3Ntd0-BohJ09GTtCetxDmfTXTCHj6wudI3Cm3GQ7EFnT9ISrZZQOEqsZNqsE1NFgx-HVGbU7nIwNKda46hzPwCLe3ShvF2s4yWOkxBCYVzhZJSTs8wE63vCvzl91K8NZW7gkwTxGbGleSnMfTxPDvgcX3WNQ-2H4oCBc4cD6Q_syVDXfhuYt7MUEmdsjlmEKca4eYpYSLLX7SBuR7_p5AJVkv0hzXkq7b0mp9zoGkiyamU1aeCyvawIkshD1sN-6vSZ_dMmkLTUbzgjNh4swn1OF-U8ipl9dEC6jPkjnUKNdCeVo5V70jRZNp9z0cYRlZIdSinNuYNoIvm-a-fzBRrrdCJIq5k9EGVbOipz2eBdvop6eHSUchsXk2zqNn1a-F47XyMAbCNawXcrIQHOX55hSnx-OgE_uryAX4TVFVa7C3nFZz0Ap1snzUQChmLVXtB-4kodV2zcnopisX3zHKiqjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4882bbc4f8.mp4?token=BVZxd-_EpmqAnMVTmpjvvkM8xNXb6SqcudfpSyhS19GqZdpZ-bW8WrnxER7hR4MBjAYoFWsTnjMiVCtQuLE_KADo476IAHNZE0YrpVjpSH6-gh41s4Oab0MuEUr7x3ciT0g1pxT6zkAzEFVQ4cVDVBL7E2lRYWAAuurAxmMvgSa1liPy6JKIn6DUMay3P7cFNYAY2oBr6dukGnd-PN3Ntd0-BohJ09GTtCetxDmfTXTCHj6wudI3Cm3GQ7EFnT9ISrZZQOEqsZNqsE1NFgx-HVGbU7nIwNKda46hzPwCLe3ShvF2s4yWOkxBCYVzhZJSTs8wE63vCvzl91K8NZW7gkwTxGbGleSnMfTxPDvgcX3WNQ-2H4oCBc4cD6Q_syVDXfhuYt7MUEmdsjlmEKca4eYpYSLLX7SBuR7_p5AJVkv0hzXkq7b0mp9zoGkiyamU1aeCyvawIkshD1sN-6vSZ_dMmkLTUbzgjNh4swn1OF-U8ipl9dEC6jPkjnUKNdCeVo5V70jRZNp9z0cYRlZIdSinNuYNoIvm-a-fzBRrrdCJIq5k9EGVbOipz2eBdvop6eHSUchsXk2zqNn1a-F47XyMAbCNawXcrIQHOX55hSnx-OgE_uryAX4TVFVa7C3nFZz0Ap1snzUQChmLVXtB-4kodV2zcnopisX3zHKiqjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
در این ساعت‌ها، روضه‌ی عصر عاشورا را از زبان رهبر شهید انقلاب بشنوید
🔹
به سوی پیغمبر صدا زد: «یا رسول‌الله صلی علیک ملیک السماء هذا حسینک مرمل بالدماء مقطع الاعضاء»...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/663184" target="_blank">📅 17:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2je81J0VLKXkzT-Xo2c_cej9sMdkdDHhYVcCVd4dFXgIZhWw15fMcuiaMsPjwxao8z_5ERb0LJqayZGgEhc03R3ogO4Oii1vPQdzkvqME7xuZwaXoW18EWuaQwlQuTeyII5eBlEVjpHvIFHvFRNLTG1_v-0oKg_uc6muGCgRHcNHGsdkBu0lDVbEsC95RbHDdqaYOPvAFzIPA_UtozOoGWYQuWBUe3azGHBjoXP5CEVWaO4DLR35A4gsgKlkRniWb7xc4w46JMX3QpiSWSE2COcztp1TspWYUrcu0HWJBTIuslPPGEgHpaR2HuWNZBscrP80tPtj-lRQaYY_snMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کشته‌ی شیوخِ مقدّس نما؛ حسین(ع)
آیت الله‌ مجتهدی:
🔹
در کربلا همه داش مشتی ها رفتند به کمک امام حسین علیه السلام و شهید شدند، مقدس‌ها استخاره کردند، استخاره هاشون بد آمد و نرفتند
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/663183" target="_blank">📅 16:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663182">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5de2e37e.mp4?token=RNlyfbSH5a2THxUNpf3pIAMSO2xnJQ9P0KSyNGDCx3_NHWF14znLK8Rx-5xA7pM5GkKYjYWL7a63-N5LhIB85HPAY-En2VkMhzEXMl4t3Gbwi4XcSRPmo0wOnHji52SPHBJsJgpJ9V85PzeVhextV5TvZXNCCZXUwqKH2CptMVflmhtvj7EVGfv7BJvFUqxxYSrlUasuYrfWkz5mvP415MOKeiih6DUQzdXPBlD1bMH8xlmIf9SBwj7n5doX0RTLD71aqlBtTdTXM2mqjd5cNCB4_6UNQDEO6OzgzT1gS9-yA7Qj5vOFsKNtAVZhTwOm0WJ4PT2u-I_ynbHfDym8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5de2e37e.mp4?token=RNlyfbSH5a2THxUNpf3pIAMSO2xnJQ9P0KSyNGDCx3_NHWF14znLK8Rx-5xA7pM5GkKYjYWL7a63-N5LhIB85HPAY-En2VkMhzEXMl4t3Gbwi4XcSRPmo0wOnHji52SPHBJsJgpJ9V85PzeVhextV5TvZXNCCZXUwqKH2CptMVflmhtvj7EVGfv7BJvFUqxxYSrlUasuYrfWkz5mvP415MOKeiih6DUQzdXPBlD1bMH8xlmIf9SBwj7n5doX0RTLD71aqlBtTdTXM2mqjd5cNCB4_6UNQDEO6OzgzT1gS9-yA7Qj5vOFsKNtAVZhTwOm0WJ4PT2u-I_ynbHfDym8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حال‌و‌هوای ماه محرم در میشیگان آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/663182" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663181">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMrR3cU1CT6NB8P7sp0lfTxXLQ-nkI4oP81jS-MeBlfCWVpQfIiG8e6W-9yIxDUSU2FNG8Ziqh6SEcxw4MP86PbFrcABvg-c7aFmO5jskJNUG3FAmS24ts5kSFZ9R6HEe8IHi_kqne87alo0z1fMqcNC3_F7bLfS7jzlHEC6DPStdvZLvoP1rD-XcxXUg3M-8r9inx8j6whXQ-uJeirNH68fsVBfHquBXdH_FoIh7W5ul9iM_a3hAi66rNZGtFhNz8yeRuEZAZHpnCT6CDbiu2jNiFjnbcOJ29A3U8Qbcb9sAWv81ytZ9BKP64K5359zNY5J7Uph2Bto0LsGqxhsEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
۱۲۷ کشوری که هیچ‌وقت در تاریخ به جام جهانی فوتبال صعود نکردند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/663181" target="_blank">📅 16:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663177">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6MMsD9WQgRHFkjxsUcEYJjgXZX4iPorE4YBCFB3Ye3UGm8H7q9ZUQSuJkt-uxX3icwR16XT9Za9PNfRg5-G8T2W_hsQnpT2UVVTJQrTRcW9JsTE4jYGbWM4Koh8JgJ9VCTVY1-c2VPbi1eIgk2AxkC69MTIrdR57usUI73YVijlTF__pSxF1RCY65cfLxVLj5-HaBWFjaqru_fked4P0T6C-0fZP0V2TrA8Z7OzDDJNf_a70WdBQjXXb3S6e0KLXd1oDXVi5n_jvd22d86HH4h4YbE1YL87RlQ0Te9yav4yRKiPmZ7z168AQ2KNjeG5t8IkKHDpa5vVIHk_Iwky2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z679zFNjxiTxkjC5gNjbIJkT_5CE69NCPvfQr0Dghx0AmeLpBaTDv6XPvcrcA1EO8cCJlTinpObS-_zkIXSq-WKfJ-bNY1FSvDHYAGC-qQqDzbsATzYiHtjGT9CJ9Hhz2Gs4fSpjNIVM2pHZiTD0dc5eMWFbSRGkIgNdA2sTaFvH4UZ7RWlLcRVA6NAnvyKKRix5iRRxIx3w9-h1XZoRKeKnp0HpqekNfmh77Z29xUJ1uvC6xaKsxhEzmlrd5sDEsGBN6uzzltcCusgbRcDwazjyKSrBR2k_AK-XWroWd20nvcXJ7yq8KPbVh4lbbzSYmCrUW7db5vVx2lx_Gx8cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLFP2YUHMhAKG-Kd0xiyhwOsvtMQKEXICvSf2rafN8X9LLIV05fN0XBj_OaL7YiWsCIJpT4t2OH0erV7g46XqdYeWtD1jK_lQo9na5T-5p1NT3JB0vtbF-9G2olblMMpMnTgkC4ShlfFQBZgLRdbEa4JsxzdNAFH52Kuuv-7jKbLpVpG0qUKPMYCFd1l5nI-PRoheEp2_JdOSz1rIeQ2l3U2MeR3hv481j4IdvgTYguFHmma9_bD8LJMowL267PoBn8TghoX5codqpimAGXR6etQAsDyRD2o8ZrNloS0HLgZDDIcHrRCUWrTI6TzIl0gjOWQkzHOBJ8xoMqzRFCgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUmVNGLl-hbQeonal9yTBNK3Ubep9vNIppz6bBY5_rgUNxuUpdtpsRXKmRNiP4sfvtCk9BwTYVv4L2bWXTMth9ZXx9G911qOiaEu8IeTX4cQFvHcGuRJR7vIvO-cpO9sDbN8NsdM6KBW_AdMX3G-kONJWSo-EAMsOninlQVHvAjAkx-_2Taw-d_4V7Zqzi79Ztnlz_2UxZMhVe2URBMQxLfAQx1rHUMYy8a02SRFPs-3tLh7jV-A1CbE-VjLJQ-WOnNYJVvTMIALh1uzSRN92l2m8CLzRWOkZOO_xgiQM24NKfQyy6IpsTC9bXSRijW9ZP1S4NH7S-mQ0H9unRNrug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
مراسم عزاداری و بزرگداشت سالروز شهادت امام حسین (علیه‌السلام) در صنعاء پایتخت یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/663177" target="_blank">📅 16:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663176">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
از تبیین واژه علی الاصول تا نقد توهین کنندگان به تیم مذاکره کننده
حدادعادل درباره پیام رهبرانقلاب:
🔹
کسانی که مذاکره کنندگان را به برخی عناوین متهم می‌کنند، اقدامشان منطبق با نظر رهبرانقلاب نیست/ پیام رهبرانقلاب نشان از اشراف ایشان است و دست طرف ایرانی را درمذاکره قوی کرده است
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/663176" target="_blank">📅 16:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663175">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKyzJSbdJcREiHtuZ3JsMzLMxF1BHv9pGNhGnjUMqOO306cRsy488wlP3sGDzlWwFvJGpHBAYCOROxZSunvN_OdnjSouHm04MqeBHBeWhuLV2EVx_GfxZsQG__GRgalhUWW7LjAQ5nWBa0-IRwET1saEKKE_A7of3aBN25ooqLvrLHSsfypzRoNLtw3NjKj_TUhwcrba22GTGM2ygiwuyqHIExjKoXlOXLo9OlxpBlkIoC1zdnwBjDBVI9D7U3azRaxjIZWWVkESm7IZsuF965KE1S649_WGsY4mrccpqFP2qM5olqjs7m7Zr-t02MesSyyv5uXw4dkicwoYpzyW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ترامپ از اروپایی‌ها در قبال موضوع ایران انتقاد می‌کند: من از ایتالیا ناامید بودم
🔹
من از بریتانیا ناامید بودم. ما از آلمان و فرانسه ناامید هستیم. ما از بیشتر آنها ناامید هستیم. اسپانیا یک نمایش وحشتناک است. اسپانیا حتی از دیدگاه شما هم وحشتناک است #Devil…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/663175" target="_blank">📅 16:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663174">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c36f8657cb.mp4?token=bh_tjfadTWwgbZL1_XWSPtWd2evIRMm8USekyUQpapnBPGbFZCdd4alr71di1reYACpcfd6sRviHpc1wdteFDFBwXhOjBC3QNvBEOqzDZ6xmlDggNnDwiWzBb3pbJyHx8hYWRJelcHjJchCTxHw6_AgBYtOnu60VaAzFcgxT9DiIcC684R2VA3hmK9ysngMh6iwRBXRl6zloMLWhyRh_97K1H4xERsqPbcd1W5E7d_ohk3QbCaVKHiOId3TmMQGOB4owkoZLOCBP8Pnc3iYz0X5-IASGi403gddW_UldK4vA4E0Ly18XU7JEe5wV1uuQdeji-vWa5mcnAdK4DOm9MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c36f8657cb.mp4?token=bh_tjfadTWwgbZL1_XWSPtWd2evIRMm8USekyUQpapnBPGbFZCdd4alr71di1reYACpcfd6sRviHpc1wdteFDFBwXhOjBC3QNvBEOqzDZ6xmlDggNnDwiWzBb3pbJyHx8hYWRJelcHjJchCTxHw6_AgBYtOnu60VaAzFcgxT9DiIcC684R2VA3hmK9ysngMh6iwRBXRl6zloMLWhyRh_97K1H4xERsqPbcd1W5E7d_ohk3QbCaVKHiOId3TmMQGOB4owkoZLOCBP8Pnc3iYz0X5-IASGi403gddW_UldK4vA4E0Ly18XU7JEe5wV1uuQdeji-vWa5mcnAdK4DOm9MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
نمیشه باورم که وقت رفتنه...
مداحی مرحوم حاج حسن جمالی
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/663174" target="_blank">📅 16:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663173">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">🥀
زخمی خط‌های مقتل| خط دهم: وداع ۲ غریب
🏴
امروز روز عاشوراست. هنگامى كه امام حسين(ع) تنها شد به خيمه‌هاى برادرانش، فرزندان عقيل و خيمه‌هاى يارانش نگريست و كسى را نديد.
◾️
سپس به خيمهٔ فرزندش امام زين‌العابدين(ع) رفت. او را ديد كه بر روى پوست خشنى خوابيده و عمّه‌اش زينب(س) از او پرستارى می‌كند. چون حضرت على بن الحسين(ع) نگاهش به پدر افتاد خواست از جا برخيزد، ولى از شدّت بيمارى نتوانست. پس به عمّه‌اش گفت: «كمكم كن تا بنشينم چرا كه پسر پيامبر(ص) آمده است.»
◾️
زينب(س) وى را به سينه‌اش تكيه داد. سیدالساجدین(ع) از پدر پرسید: پدر جان با این منافقان چه کردی؟
◾️
امام(ع) در پاسخ فرمود: فرزندم! شيطان بر آنان چيره شده و خدا را از يادشان برده است و جنگ بين ما و آنان چنان شعله‌ور شد كه زمين از خون ما و آنان رنگين شده است.
◾️
حضرت سجّاد(ع) عرض كرد: «پدر جان! عمويم عبّاس(ع) كجاست؟» در اين هنگام اشک بر چشمان زينب(س) حلقه زد و به برادرش نگريست كه چگونه پاسخ مى‌دهد چرا كه امام(ع) خبر شهادت عبّاس را به وى نداده بود زيرا كه مى‌ترسيد بيمارى وى شدّت پيدا كند.
◾️
امام(ع) پاسخ داد: پسرم! عمويت كشته شد و دستانش كنار فرات از پيكر جدا شد.
◾️
على بن الحسين(ع) آن چنان گريست كه بى‌هوش شد. چون به هوش آمد از ديگر عموهايش پرسيد و امام پاسخ داد: «همه شهيد شدند».
◾️
آنگاه پرسيد: برادرم على‌اكبر، حبيب بن مظاهر، مسلم بن عوسجه و زهير بن قين كجايند؟
◾️
امام(ع) پاسخ داد: فرزندم! همين قدر بدان كه در اين خيمه‌ها مردى جز من و تو نمانده است. همهٔ آنان به خاک افتاده و شهيد شدند.
◾️
پس على بن الحسين(ع) سخت گريست. آنگاه به عمّه‌اش زينب(س) گفت: عمّه‌جان! شمشير و عصايم را حاضر كن. می‌خواهم بر عصا تكيه كنم و با شمشيرم از فرزند رسول خدا(ص) دفاع نمايم، چرا كه زندگانى پس از او ارزش ندارد.
◾️
امام حسين(ع) او را بازداشت و به سينه چسباند و فرمود: فرزندم! تو پاک‌ترين ذريّه و برترين عترت منى و تو جانشين من بر اين بانوان و كودكانى. آنان غريب و بى‌كس‌اند كه تنهايى و يتيمى و سرزنش دشمنان و سختى‌هاى دوران آنان را فرا گرفته است. هرگاه كه ناله سر دادند آنان را آرام كن و چون هراسان شدند مونسشان باش. چرا كه كسى از مردانشان جز تو نمانده تا مونسشان باشد و غم‌هايشان را به وى باز گويند. بگذار آنان بر تو گريه كنند و تو بر آنان.
◾️
فرزندم سلامم را به شيعيانم برسان و به آنان بگو: پدرم غريبانه به شهادت رسيد پس بر او اشک بريزيد.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/663173" target="_blank">📅 16:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663171">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAQsUFQ8mAyla7DO5zqqskGe7JQ8c5YlsL1Wno158FhrbJx6eKSTZ_Q-qY05O0rOCq25ZaFAsdod0Ntt2MFsSRqETOWxMsbxvk8T7_3TmZlQ4zqbCpRoZ5mAhC8-jbFr6nkKf-mPD8vJrVaIYocf2T-uLJa1hiqAJJE10U_1XzWkNgnEMUx14QVtbWbQeqfm0tNNE8yso9dbPwWXq2NqxNCn7zHJStpLvklZw4MySX4Sn0gqhzpkiy2yagUpeIH1VkOsVkV7JjoMjI5ZvF0rOJjjQaXxZljaweWyz_NMtDybuVpWIWE6ZoJKutLlbTWzAvTlLaPXf4wZR4B8LuTA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmZP-9m3qCCO3502vflEhX0sGhGKBAzlxL2V7K9DSREq_OlcXo7MyzzNRHxixd0LeTEBE3WD-0JrfXpQpQjoIUmrYZFw5cy4cnRUID_DTsrk6KPZuTWYqjNq_xYU8sBHhrSHGQFzvlO1R9b4_Iy6xZKTBChR9inGZEK0IKk_L7v4WO2C04d-Er9A6qfhq4XN6AkMlYRO950_rL7KwC2RuzTgWfuJPMoteGoyKC7ucI4qH7kQBY1r2J3hp3c0hBG1Uilhflc5WBBuy_gG2CdESIpu5k4i26_alR3wDwz-KbQfreGfaFF9ePeEvoC7_2eb1bDMnZHw9ZXOjw9fXZ-jXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
ادعای کپلر: عبور از تنگه هرمز با مسیر عمانی ۲ برابر شد!
موسسه کپلر:
🔹
تعداد عبور و مرور از تنگه هرمز در تاریخ ۲۴ ژوئن یعنی روز گذشته به ۷۰ مورد رسید که نسبت به روز قبل ۱۰۵ درصد افزایش داشته است.
🔹
این افزایش به دلیل پیشرفت تلاش‌های مین‌روبی و استفاده بیشتر اپراتورها از مسیر عمانی رخ داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/663171" target="_blank">📅 16:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
تکذیب ممنوعیت شعار علیه آمریکا و آتش‌زدن پرچم این کشور
🔹
قوه قضائیه با صدور اطلاعیه‌ای، اخبار منتشر شده در فضای مجازی مبنی بر ممنوعیت سردادن شعار علیه رژیم آمریکا و آتش‌زدن پرچم این کشور را «جعلی و کذب محض» خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/663170" target="_blank">📅 16:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663169">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8PuXg0n_q2kbyHmHnSiycNse9OM7C3TOUI2cT_maJuGKlFvghEIH4UFxjv9mhL-PMRr3J671EdLqZJvfFb-9oTIXmbnQEmNlLzayG6rxsA0CAfPe8TNskqjT_Y_5vLJKK7j4kxTPonIzlPn_tEk5Z9_dcQOwmqACmKC3UwmuzLkD4pLlW0jNNpt-QupC1h-QazAInGV888jgnomxQBfs_NnV9NeYVVmVyConBqqa6LZmbQWVvP3L8-BGa7gITGpMFF4J1AV6cB5jz35Ywi5-hFcCFuALic7po8lPPnfjkfbADIWSDXssrocrdHTn3nSCnFypG3W_BQFkVJe2w5T1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
واکنش قالیباف به دروغ الزام واردات محصولات آمریکایی
رئیس مجلس:
🔹
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما صرف خرید محصولات کشاورزی آن‌ها خواهد شد. جالب است؛ تنها محصولی که ما در حال برداشت آن هستیم، همان چیزی است که شما کاشته‌اید: دهه‌ها بی‌اعتمادی.
🔹
این محصول، ارگانیک، فراوان و بومی است. اما ظاهراً آمریکا تنها سویاهای تراریخته، وعده‌های شکسته شده و یاوه‌گویی صادر می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/663169" target="_blank">📅 15:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663166">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت ناحیۀ مقدسه</div>
  <div class="tg-doc-extra">حجت‌الاسلام میرزامحمدی هیئت قرار / @heyate_gharar🏴</div>
</div>
<a href="https://t.me/akhbarefori/663166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🏴
پک
#هیئت_قرار
ویژه
#روز_عاشورا
🥀
به احترام ذکر مصائب ذوات مقدسه، لطفاً بامعرفت و در شرایط مناسب گوش کنید.
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/663166" target="_blank">📅 15:52 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
