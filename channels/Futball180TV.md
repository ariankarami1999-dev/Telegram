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
<img src="https://cdn5.telesco.pe/file/KdZubS7lfsRTbfAjkIXcZWNpnTocd6t8JsdiL96uR7uYqpQB40aC0vIDKoYCcMT_D9FIt7TuLRe1Wxo0P0E-VyYJJxQA1tGomU8q9Fs-jkyC6Leg3Uz3zQrTZ6Y_MZYwlxKsUfafeN7UChnCQH1CO7Ec59rUoVqX3uLJAKzeMcy9z9uuM2MqlGgzFm_SDWbdkATNrB0fCQJbJlI5rbnV4iSw_vIZM-l2lc6hQ8-o-qHYfhtYQzR6c1wtk-6Iz0Fmds9UkzRFaHgdVW8bJixRFyNE7C0_KwQPqBVo_Pbet7Ilealv2VU-YvSrqL64jQt558ffRFy3KmgGir8VMK1v6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 406K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 23:31:04</div>
<hr>

<div class="tg-post" id="msg-106972">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2832d49487.mp4?token=DedIFiqIfsupke_ESTfy9C3SzxL1krd_GdEZ970Yh80tJ9Vm5uzWYG5NQ4dJZo2E7TB8tr6Isvq9DZbptc_ieX10ATGqK6FlxiN3uulxjObrIMDUmg4teTgZT_slJNzdweKhZAFUhqpn7ALtapZNTHQPA0Zi20ifGDF8OJT0_5HO3rzjWqMbALdPcZI_s1l6aq6Mt_RhI-fcagTFdfYv4cgM8w6iyQ1hxXlCF6rxnLqVj1WHdScLji8QxNi3cGrfydQLeZdiLtxN3ra6ZiTTK2nPTH3PzA9A0YwZzgkK3vxmwrCupBTJ8oPklKHCyuWpDOuGXTDa5ml5IBX7weI-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2832d49487.mp4?token=DedIFiqIfsupke_ESTfy9C3SzxL1krd_GdEZ970Yh80tJ9Vm5uzWYG5NQ4dJZo2E7TB8tr6Isvq9DZbptc_ieX10ATGqK6FlxiN3uulxjObrIMDUmg4teTgZT_slJNzdweKhZAFUhqpn7ALtapZNTHQPA0Zi20ifGDF8OJT0_5HO3rzjWqMbALdPcZI_s1l6aq6Mt_RhI-fcagTFdfYv4cgM8w6iyQ1hxXlCF6rxnLqVj1WHdScLji8QxNi3cGrfydQLeZdiLtxN3ra6ZiTTK2nPTH3PzA9A0YwZzgkK3vxmwrCupBTJ8oPklKHCyuWpDOuGXTDa5ml5IBX7weI-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم لخ پوزنان به رادومیاک توسط اللهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/106972" target="_blank">📅 23:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106971">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwgMFPUZHL7O8j2-TT0lV-o6VohhHOW0P617mEGNtCyS9QrvEcjCO_i0FFucKems7i8ZWJJvCv6BKr2nRk2PZXHRBHPmmK6FnwkPMJcNgQ4ZMwbGCUOSDKt40uM52X4BmPtK-Y8yPaJ7Qsw078hHY5_4FVJdE935jU7oOJYTSVLB6pff_B-f7H3lBOHLH0spVoujEtlQdlyxjRbuASMu95v2DKL-Dvhy4yTu4JP5memOLMLSYyFtOvm_5rK9kw1pUa7J7sK4LzF67f5E2t01g0cpmlxrfx2unqYcSsTFXd1UvJknsggXDgHhfY-Dk01bOVmSIuP_qyA6E8ohbsDP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ترکیب پاری‌سن‌ژرمن مقابل مارسی؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/106971" target="_blank">📅 21:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106970">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=InCcFscUl-Gnr0uK58jvxPuurowsZ7Wait5Uh_fueqVkH1gtNAWl_psDZ9qaEmiZSy5-v9Lcf6dwbQVaetXrLz9CqhvG8ciLO-3RpU427T8vZ2sIqmLZezyP_8MoRVCJNDJKAqJ-KZP5iyDxDLoDB4Z_jcz3JlBqvCgNQXz9EuzuPyEiuVQ6mV5me6nldn1XzPmXCf08PKHFA9Ih43lP_-5byUwWCJpnsMzFaB5I9tBvai94ItV7qAi-8gGoeQOp78eM-KICNsmeddP8Plzw1ihOnUqih7Sc7I2jz5c3nWrPRmEyL5STqqQV3WMPJkENCtH3pLLTxc3F-7-N9Aeu1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=InCcFscUl-Gnr0uK58jvxPuurowsZ7Wait5Uh_fueqVkH1gtNAWl_psDZ9qaEmiZSy5-v9Lcf6dwbQVaetXrLz9CqhvG8ciLO-3RpU427T8vZ2sIqmLZezyP_8MoRVCJNDJKAqJ-KZP5iyDxDLoDB4Z_jcz3JlBqvCgNQXz9EuzuPyEiuVQ6mV5me6nldn1XzPmXCf08PKHFA9Ih43lP_-5byUwWCJpnsMzFaB5I9tBvai94ItV7qAi-8gGoeQOp78eM-KICNsmeddP8Plzw1ihOnUqih7Sc7I2jz5c3nWrPRmEyL5STqqQV3WMPJkENCtH3pLLTxc3F-7-N9Aeu1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/Futball180TV/106970" target="_blank">📅 21:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106969">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVN7ZFOY60XYLppjqR8jBSqD45bIiwxoicYSPP7P7nf-G6p8d9YmMZ7dUfT9RxzqyldgBQcGDMpThxVrh_HhnSENO82vl5CpFDQPDivY-5PmpO8iW7DzE4q1L19dfPXk0mLO-zPHF889qLLdUPFnrLevrikvPNdsearaoUqhFUpMubt-nOAzfpTWZ0gajqbZa-7VbGXFeNvxBqpZKx1JAnPtSyNp2EeDU_4K8L9UKLfYSzkS8yAnniXwj1rQLFMCySQR308OG1afuyTkcTieU3uZ14U90dQm9KQXlyA7DvvGv7OPhgeecictrgaqUxlN5YFw08Rif0w-uqs7V35-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مورینیو در ۱۶ فوریه ۲۰۲۶ که مربی بنفیکا بود:
تو یادداشت داور نوشته شده بود که شوامنی، کارراس و هویسن نباید کارت زرد بگیرن، چون بازی برگشت رو از دست می‌دادن! من خودم سرمربی رئال مادرید بودم، واسه همین خوب می‌دونم اونجا اوضاع چطوری پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/106969" target="_blank">📅 21:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106968">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh32ypLj425u0cgrpaMUtV5og-XS4Gd1u0xe2mw_sM984d1xICHCtyLTh85WtLbNB4nRuBYkowvHXa7vDgVRJddy0UNh_nE1wm6PwvYHfGjpqy6z1JBpHV2xQdWqJThPwOgcd5hviEQniT70xWcN5HxUdVDC9pRvLZ8BAemRzLwGvYs8DGNAvGDvFAKPtVTvkYT5FwCQqCVsxFwoAsQ80g_d-wa1vR7W350rZaKRo6le7BBPk71x1YcDajJ11BjBJJK_wnYS2BZudz5AVcB8YkoEKqWcoc3Ll95VpGcxSZ2sD3ldKftl7jrX3xwra3K7UDmCFbr4rn_Lok5oT4lC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج درخشان منچستریونایتد در پریمیرلیگ؛ عجب کسشری شدن بعد فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/106968" target="_blank">📅 20:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106967">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=OWSgxmKYVCguHvfApVI9QfPXy7K0ZdCwfa9V6UY-IrKou2OdnliF8lELe18GGU5iVhBGKYcOMZPipJsO01S_C43dpvEeT1CSiQOE91m4fA1UtyeN89SkeBsStzZgZe97L6lwX0zsInRsDTiFAnWjIe9viA8SsA8fglOg1h7vnZC1qAIZutlaLjA_eQ7OT2x4H2qInvPPVWAKB9VrQZAZWvE4U4sgi401tL1A_UflLl_GE304UY8RMaNxFfkE_PiSbueljB4_GxMPHrcyBiMIQ2GpSuJZUAiX8D8TFJUjwQ56vrPFvU-9wVR3ryKWjqMdqw7LedYXWW1lD4mruaGtww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=OWSgxmKYVCguHvfApVI9QfPXy7K0ZdCwfa9V6UY-IrKou2OdnliF8lELe18GGU5iVhBGKYcOMZPipJsO01S_C43dpvEeT1CSiQOE91m4fA1UtyeN89SkeBsStzZgZe97L6lwX0zsInRsDTiFAnWjIe9viA8SsA8fglOg1h7vnZC1qAIZutlaLjA_eQ7OT2x4H2qInvPPVWAKB9VrQZAZWvE4U4sgi401tL1A_UflLl_GE304UY8RMaNxFfkE_PiSbueljB4_GxMPHrcyBiMIQ2GpSuJZUAiX8D8TFJUjwQ56vrPFvU-9wVR3ryKWjqMdqw7LedYXWW1lD4mruaGtww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول منچستریونایتد به فولام توسط متئوس کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/106967" target="_blank">📅 20:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106966">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kghxmY5iStH4jZjkWZWl8pZiNmtHEjgcqreSOxbdy3jT4vMKnA3SENDBWmh1YZAgIBzGSkWR2tbH7zS8W5rFXHEpYILd6PGqa4vU7uuURHjXpcTVzrxxGeteK59L0JPf4LqfKzDKjtp9wIcUwuYpVa-OygyKfqFQ1xotDa8kOSTM3qLSQITwhfB7EPsztxKOvpH_HA_su_lzwG6RE4WJeEFZ6GMDTqOeCW54J6yT3WTfgVR-1N9pVctd_f7MOvlnHZ31FKMCpYhTE_MVwiwScLRbEt061E3JPDwk5v2yjnCrf6siALw2hkwBZuEwu8i1qgjjb18ohiDYJovG4Rpmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
رئال مادرید Tv:
🔹
وقتی پای رئال مادرید وسط میاد، برخوردها کاملاً متفاوته.
🔹
لالیگا و فدراسیون فوتبال اسپانیا اجازه نمی‌دن رئال مادرید رقابت کنه... اون‌ها یه نقشه و برنامه از قبل طراحی‌شده دارن.
🔹
دیدن همه این جریان‌ها حالت تهوع به آدم میده... اصلاً براتون مهم نیست که کثافت و مزخرفات تمام لالیگای خاویر تباس رو برداشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106966" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106965">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da8be998.mp4?token=dj3tIGBvB7kbjatfIbYEgbu6euQDgvMKrbfmbO1BMckjN7lzY9HWaA0ICNHCaPjZlzZNI4hefsWRrPqdTfD15ttjCQCZGN1WF5sHknuwY573xnMR4dIzGmWFPzRljB3pH8bJBotyGmP6G_n887c9C54xX1Z-EFqOtr2NJLInfXe63zeTGPPIIgOgZKJvRlPXCQ2CSoDyVZInb8ZVLHkRuT7p8boYVFMfCsbooBeWGElINzFK-ivw0MHUF9MA6T8i6fP0fH662L1bsrWjkkkrco2967X0nSqOtLxUIJwZ4rkx1u35Lzel028QDXUzulhZQy_vgDmL8cHEZP8azICptQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da8be998.mp4?token=dj3tIGBvB7kbjatfIbYEgbu6euQDgvMKrbfmbO1BMckjN7lzY9HWaA0ICNHCaPjZlzZNI4hefsWRrPqdTfD15ttjCQCZGN1WF5sHknuwY573xnMR4dIzGmWFPzRljB3pH8bJBotyGmP6G_n887c9C54xX1Z-EFqOtr2NJLInfXe63zeTGPPIIgOgZKJvRlPXCQ2CSoDyVZInb8ZVLHkRuT7p8boYVFMfCsbooBeWGElINzFK-ivw0MHUF9MA6T8i6fP0fH662L1bsrWjkkkrco2967X0nSqOtLxUIJwZ4rkx1u35Lzel028QDXUzulhZQy_vgDmL8cHEZP8azICptQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
حالا که بحث جنگ دوباره داغ شده؛
اگه تو آسمون یه جنگنده دیدید، سعی نکنید بهش شلیک کنید یا سمتش سنگ پرت کنید، فقط این فن استاد رو بزنید تا خود به خود به آشیانه‌ش برگرده :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106965" target="_blank">📅 20:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106964">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=X3isTsXjAh9FXdZO55seNUv3uyNvJpKwYrfMFfBJpn4BZfFKhlkfVgUAzkP4pwrY4uDocwU3YUX_GQTcQLvRlSSDMSkoVVVaTf0vkqbIKiH8uqVtTud_hOYVcjuxSBHctih70WqyuJ8HWoi-YLEMGS8P9OXthdFhIcQ29b0aCDGdNbUe2ajqJRxJBtRyOe4VTJcjOi604jnwU04QIbDL9YR0P-qqlnMMCyV5SgQU7SO9mhgVEEgQHdTBGHvblWE2-jXwiwtKoVbzN3jkPQMnZhmEolQssjpwcGuwR6y3__ykMZXB9rWcL19ftBznaJPRwfFBosOq2TWY0eQLaeHafWYZacMUMRpEOz5tDVbaHdsGx1D8OLtCFA0H86GkA2i6tO9UM0qNRJkbTY78BfF0a8IdpgMRed1VOssUd1sBCtcJRBikJ2gRo9133MBPcGTSVlyECAc0tjJYuzbHVd8slK4v2J8Ex2TzD1WW8C9jg5MTGZVtIUTAjPRUH4fk_Ag5Kcde3_FPQd77FyqGAWjfch7G1sk9SEU_UsFXNqGlY9jlgapc-eI5rxr92R4uCkO7XQMiSOZMehbHLCENk4tMZveZxWTy2TTHQXr8oJBDZUFcUE0E9o8S8o4Kx5L7TXsPtgAXfCMsKqnIy8pyIfLCXcKkoOgPml02xTQFZrSZrZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=X3isTsXjAh9FXdZO55seNUv3uyNvJpKwYrfMFfBJpn4BZfFKhlkfVgUAzkP4pwrY4uDocwU3YUX_GQTcQLvRlSSDMSkoVVVaTf0vkqbIKiH8uqVtTud_hOYVcjuxSBHctih70WqyuJ8HWoi-YLEMGS8P9OXthdFhIcQ29b0aCDGdNbUe2ajqJRxJBtRyOe4VTJcjOi604jnwU04QIbDL9YR0P-qqlnMMCyV5SgQU7SO9mhgVEEgQHdTBGHvblWE2-jXwiwtKoVbzN3jkPQMnZhmEolQssjpwcGuwR6y3__ykMZXB9rWcL19ftBznaJPRwfFBosOq2TWY0eQLaeHafWYZacMUMRpEOz5tDVbaHdsGx1D8OLtCFA0H86GkA2i6tO9UM0qNRJkbTY78BfF0a8IdpgMRed1VOssUd1sBCtcJRBikJ2gRo9133MBPcGTSVlyECAc0tjJYuzbHVd8slK4v2J8Ex2TzD1WW8C9jg5MTGZVtIUTAjPRUH4fk_Ag5Kcde3_FPQd77FyqGAWjfch7G1sk9SEU_UsFXNqGlY9jlgapc-eI5rxr92R4uCkO7XQMiSOZMehbHLCENk4tMZveZxWTy2TTHQXr8oJBDZUFcUE0E9o8S8o4Kx5L7TXsPtgAXfCMsKqnIy8pyIfLCXcKkoOgPml02xTQFZrSZrZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول فولام به منچستریونایتد با گل‌بخودی لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106964" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106963">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyjIsSWkrT8MEemGwQtXUPgiMsDvlJCbpg8LJ5-BAr-6PvAp9hhgLOUoSQDmwS72x-2WjFibeT5TnXWLYzWpyIp1x8_umqc9FW58Ay3owzbIb5CfvV-GOvCGkwLAyMWogNJdnw7qajNArEbHDmnryJ3Ew_-I-hhk5eEuU7U6CT4YAyK9P-Z-qJzmqdq5dQhyWE3MdRoJ31ZmuEsKFtV8twgxh7BeMxtCxqqcKU6nYhZBxNRv8thxNAlpSKyguXIvBAk6y_ZwriUQnUGTvqjG5hKAQbRcZgFhkGZ9zrPgcGSuTLvfjbVsMiGFyQlR6P-obSeUNsWWg8jN8OF811w_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو
: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106963" target="_blank">📅 20:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106962">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKDFhWimLVqIUDHWeV4bZD6VGJwOWbw_Yf6gXzVoDKYwEydsyWm-mzoVX_B4d_OtLSCUnEwcdJlAgRl7HtAC-jkthzpjeGHopFhmnCp5toEw3sfbWSw37TYTUaLkganb0LmL_FLwIHX2VmYHBI-6lXZIke7WFbEVMd-MdOqIBvTLfqn1fDvkms6kBo38A-XKU1Usd30U_2dtznhUF438TYrLjgnVPkftDXhmvfMyswT-7NLsCNzqq-dG6HkP1kGVnVNTpTNgBE7dDKNYsMJ6q92yQSOw6B2C57LSOrdCaAYPtKPGqzISTAlFt4s_6NHhcl56wvssOGD3-Y8vfZLLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رسمی رئال مادرید:
اورتیز آریاس داور بازی، رفیقِ لامین یاماله…
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/106962" target="_blank">📅 19:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106961">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9TyQCgZqag6oAxE0aD3izFTCA0EEQKkgMCfX7GVFkLkIgY5dJbnxNa872W4qHQ9if1HcH5AibvpPsfDfoWt8Y3hOjRcI_Ct8dJH6pXYh2PNiQRIXVeJuhEPntoP-f7tOj276oZscL4MpUVXwsns2SB1Gm2bEb1-muvbsbyZFj9XmKnCrGtsKVgVzjKFM5_GVkoo05KQIDWZU4MvodTaA21cYu6lK8QG1jahSDhMNnZb1pTsYcqiog6adi63qL_YacXqe4nW9F4_rGXfdVyH54AOycmZ-IPNCSPdDLKPPTt487FYep_tAdf62XkTEWaGZekxbcZJZl__gMgboOpL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/106961" target="_blank">📅 19:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106960">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3b_VN5d_ii3YEkXqhCOtjtwdk4Yvu2A4H_HX1aPIgW1Rjj0W_-A0knz7gdkLGaTi928fEU42-MmyZXx_oM7dAVdv96qmzz0Psv2dVIqnuQXVRzIRci-MuMqyu0mfLAjMxwiR77OuUZV9xTNhKwSekX6ybZRhrnSvLdj8ePmvdxs_CvjRKng7ibg28vjDOtoPhZTum2N4WcgecwRQ3bb8Oc7EvtWBkOJlwsgGadC-ucIQA2DjFE5hpn-ZQGde81uc2ui8aBF6ZJQAXN6xtpoE8yXPMOXwPX6z0MrryETDi6elqTXT_TSDP2CidI1JXUto6QDFdp23pp4n6x0Fmi_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106960" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106959">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCjxrM6C20cGXVeLgtD2gL_8wVALYnYR1rChDrFSMnpG191zveL9KXUEfQoVwTyGfAfvNIOPUk-ZSst1xCVGpPXTQWYx9nV2JnidqJHYa-0KzEEuQxR7-DygCohT0mTALg2CGSGVXOrgvs7dj4FvaQ1z_Y8krrcNb3KJWFJ2kA0cfJnmXfcUuttbluUcDsSwoRrq8r25_4S_dV6c3Og00wbEfPvEqY83A9abm46UqGunzOx3cs_oIQqBDZBivOBXxRTfF4hnkdNoahuSY7zbY1vgxS9MqYODfMmijpt8vujAF6YqtzYzQ4gWeMAi8b-0Z82kXT-tsNbEGSmTh20Mnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106959" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106958">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106958" target="_blank">📅 19:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106957">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دقیقه ۸۹</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106957" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106956">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رودیگررررررر</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/106956" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106955">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئال یکی زددددد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106955" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106954">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/106954" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106953">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یا حضرت عبااااااس چه توپی گرفت کورتوااااا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106953" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106952">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اتلتیکو دومییییییییی زددددد
🚨
🚨
🚨
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106952" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106951">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106951" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106950">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=TG72Y5Dfgr90mu7LVtyqu4C-WorrulQI4uqQx4rLSHEu4TAKnGJH330VZzENqNtP5vY50dTr2ynS06CzRW16yVZjEFaTbFzwhQUtv5mgzlH74ie3l14pxc756rH7jE2jvbRJykekOdK7Qc_iaOTl78u204Ug6K22hDkzDU953kXxQzKEFQwKwsfFSuhdNsh3KuqXJ68bfldJxpI5YzXjN62hgpdnstkyElqpvBslotfsDKWBtJhJhzPZb00glGdGOdHr9HTdlgjgerhbLU1SzQ6qeHIsqhMjRO8t-QyPPq3Ij2QIa6cAwGbYVr0U4_3vBVVvEGEocODfqUvJdrbxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=TG72Y5Dfgr90mu7LVtyqu4C-WorrulQI4uqQx4rLSHEu4TAKnGJH330VZzENqNtP5vY50dTr2ynS06CzRW16yVZjEFaTbFzwhQUtv5mgzlH74ie3l14pxc756rH7jE2jvbRJykekOdK7Qc_iaOTl78u204Ug6K22hDkzDU953kXxQzKEFQwKwsfFSuhdNsh3KuqXJ68bfldJxpI5YzXjN62hgpdnstkyElqpvBslotfsDKWBtJhJhzPZb00glGdGOdHr9HTdlgjgerhbLU1SzQ6qeHIsqhMjRO8t-QyPPq3Ij2QIa6cAwGbYVr0U4_3vBVVvEGEocODfqUvJdrbxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول اتلتیکومادرید توسط گریمالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106950" target="_blank">📅 19:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106949">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتلتیکومادرید زدددددددددد
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106949" target="_blank">📅 19:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106948">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلگلگگلگلگلگلگگاگلگاگاگاگگاگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106948" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106947">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دین هویسن اخراججججججج شدددددد
🚨
🚨
🚨
🚨
🟥
🟥
🟥
🟥
🟥
🟥
🟥</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106947" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106946">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پنالتی برای اتلتیکومادرید
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106946" target="_blank">📅 18:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106945">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رئال‌مادرید: وقتی داور طرفدار بارسلونا باشد، چنین اشتباهات خنده داری کاملا عمدی بوده و پرونده نگریرا رو بیش از قبل بزرگنمایی می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106945" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106944">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106944" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106943">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFjCg3MRPFQA-XZYsmyzkNhAXjx_NPyD9i8IbKAAC8vj2SEGxv3A_Qa2iG0I_MgODdcU1PtaIHP4EawDiStXPwAR-ioZQLwZdTXfJ9dCkywK3dPcpBs-v30THcB2Ywu7-ArPnzGe8wDi7FhDIlnIZqgIKGdSKMlAAqqfSyyl52MOEOlX0Zn7oUXdH-gKpNWwqkLschzWWjgrXoIaWtJPaWSUspfHXoiuVf33XsZluYkBe6y5doskT4Rh4tKDnbadxc3lH4HsWygF_66xZaAPuP-2jqoDOzKHDnvy3JeeN3_KvzB2wwTJdWljbgg3kjwUktJ006FPz8LkeTH0j8XzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106943" target="_blank">📅 18:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106942">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JV71cQYXwXjXfbms3096YhIfW0lSzWRJrJGhbOGJmHw8y9G1lUOxIxGQSGae8vO5M4VeuXzq8szkmHbcZyRfaFxX6OlkkK2bptcyWlwrDueTaSktTzPABYeeMK9vyTML989HWIfDAMp7prVcwnaEnN4RTRsZF3AGb6Nmrxa8cDdQBv0FXhFmdCISipXzxkwOm1IbF3-dNosVfq_MJTvVh5yCsS7XHDctQdBxgvJ86qDnHb63oUnTA0V-ynrra0d3EMu-EhRE8ncr3luIDCC6f9eIiNUtlBNaws81FdvOCn5wiAwunRIxlOciaklGguoZ6Q9wa3zRlSZQ59CPzN9Rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با گلزنی به ساندرلند؛ ارلینگ هالند اکنون مقابل تمام تیم‌های پریمیرلیگ که تا به حال با آن‌ها رو به رو شده، گلزنی کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106942" target="_blank">📅 18:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106941">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106941" target="_blank">📅 18:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106940">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brDLFZi19NhunRRJFDe1I_o9K5C2UjOloB4OA67F8Hf6ciAEDRPocmkj89nZaadKbziBJJplgENoznDReR484PL2wmJuFMfXKGch8u9H8p75QUZstTajUK4rlJlzzWyy_1qQGQxy2tw_0DzRcrFBk4tvqp_jodkolJqkiwebhnnfPxLmh-MbZvAlDZ4jSGCZgLKpHxTpD4e0mjUNCNK-E5nBf1vPoy2J_yNCeLBwjxjnBdKHsgyW2V33hhaUImAWH8GPBcXMtnv73Uv5TcIOLJdhp5g1sTa5wGw-268czx4Mc928WRp3M0-xxvJj9MeLZE6iGspHqCLCgSApU4HqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106940" target="_blank">📅 18:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106939">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اتلتیکومادرید دقایقی هست رئالو لوله کرده
😐</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106939" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106938">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFIrSFwUQoJaufZWoj0lIfYccfGJ9jNYzCDulVU6JNCvjWfDp42QRWOQx54eBe6LZdK8CUPDqN0qmrJOG7HDnsjGQk-JFzJ2SMnxM2Dtbe1qAlqK3Ppgu41q86Fr6rVekfL_aeplsDyBvNLaOkEs5Hv0hGqkt3PamZRIyfcPrQACbN7xZ-bFeZuNy_wRfpgGOmos-SVDMZXQ8BeFOUBZHe35hBtkzeKkgRr4E_rK96t-TfCIn_8_ATWTGzKFBdDvrLn8GpUESA-UZFMzAHAGxM0hI4hKHHsKJEKN_lw6PwkeKspH16eI_EsFMvI977YCfEtdUfZnyOMrJStD2A_R6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106938" target="_blank">📅 17:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106937">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787e254f6d.mp4?token=H-HFsMyJlW3NyXK_AQ_UJkH4jIm-N4VmhGaVqlV1krNsu2lAxlF1Qs7q1zTixqgM2j3DC_zjKOqFvX4Y9uA68WZgS8yQDHqZeA8bDiZb7ullhnfqKN-tMDL4hXa16StA04VeInMVT1glA6OcseiF617tH5QQEtiNJrI1YmD6IG-b0T3w8WDwrKHAy_mKqQ1ihqwmjGfSvS_5fBuNsDmD7hNz6IkVQm2J7YEy2X_WaP3BpyvJQsUyFRUnoK70PW5rvYui75Wwb8aD9Pvc0NjWjDl_xB-4g9PZVmQ8pzKpAUrGTFmSYzOO0a03b4mTPB3YSCg-Eau_mJBhvpo9FIZeMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787e254f6d.mp4?token=H-HFsMyJlW3NyXK_AQ_UJkH4jIm-N4VmhGaVqlV1krNsu2lAxlF1Qs7q1zTixqgM2j3DC_zjKOqFvX4Y9uA68WZgS8yQDHqZeA8bDiZb7ullhnfqKN-tMDL4hXa16StA04VeInMVT1glA6OcseiF617tH5QQEtiNJrI1YmD6IG-b0T3w8WDwrKHAy_mKqQ1ihqwmjGfSvS_5fBuNsDmD7hNz6IkVQm2J7YEy2X_WaP3BpyvJQsUyFRUnoK70PW5rvYui75Wwb8aD9Pvc0NjWjDl_xB-4g9PZVmQ8pzKpAUrGTFmSYzOO0a03b4mTPB3YSCg-Eau_mJBhvpo9FIZeMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🏆
پیک‌زدن هری‌کین به سلامتی توپ‌طلا احتمالی‌ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/106937" target="_blank">📅 17:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106936">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106936" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106935">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrB_VLCGDnZ0Kp4uzaHL3KR1b0fWKg-haGlyf9edGzGszsy0oqXxr1MfA6tJt7oDHuGKVh_sSJE9qpX1t_skLi5fUf4S9AmciyTLur7cqsPUVWdyPLAt8hkTN6VUVveBIKlF_zOGNbAJdIMrTWitSHnRE6YjP9FkbC5wn7ECd3k3EdKJL-4HHjCUnjoApBe2hOBVQHHalfJhNYxsLICAwZKGN1AIV_MH2LzmLSvxowa_1JXQrsUu2GHl82EaJ3fNQ3NoGnhkAXg1wIHA2JwknGmWZ8cVliF48ihXRulS09I1iybURstWDw1PrHDZGaGPoGId97pSNzSAlpH669eK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106935" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106934">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">برررررریم سراغ دربی حساس مادریددددد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106934" target="_blank">📅 17:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106932">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u46NjaSyhYWTsfzfpaoiWew_2VLPuUhfyV73MnRTXg3TB9BwSPs6B2cAdJmH67C_ET44NzDV1fsv9ZHc3Z7tvVaftbp3WDkFpOhS-BrV9_8SrDoOUzfcerCYcIybs6PZ7RXQQcw85LxNmXan4rkxmOCEpx6g5ttLUad5PB1NWFeT9aROp9YRrik9SAB4tnbituH_EB9xd0t3HSa2w6x3G72BVQbSoRD-Fa8t9EoWHwWEijDkul6vfZVlPUXakgkVtd8cd47Zj0BP42Slgo6pMEnDuE8aOCfIyQDjyQwVkSU9nNC0q9_vkASq29KoUDfcVN0bE55elV5okbKd6SLmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhV3KKWvIln2XvnymP5wvK3W6_tjfpfFjRbHT3HUgBaVky_RNB3RTLgZuFwN9h8tNATSObo8dKRLveXaAEroZY7g8CIVJEEfEjB5BhXPG8vXiAN8eN1VVM-1bqJy1murh6WNtmnyqIrnmvAaby_YTkLCYUMKf76AAHeHAAshZAAQ64V6wNDbW5BJj2ntoSQxZkkA2UDqJzZkZdnsLDVO9vEZXo9Z9HHZVgCtvi49lUuUlKEN_yWQuZsObPZAS4AzzWBooTyxvVETAwvCujy_5A96S7lHYG1K1mGt8tOmXwvpzcISiFsgWLSbcNxsJOQo4jLNC639FpCN15KOWmrTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
ترکیب دو تیم رئال مادرید و اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106932" target="_blank">📅 16:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106931">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=fZaSs0GoahiUdKUfBBhWGsWDX3hAA8z3n7nlUq4nFLgGcruvlf4xJNDhwmEkiQPr5l82059uzJAQitSb5TLY25A0DsMxvH5aU4J2ejsf2w3CvFF9R3naWdRwG5XC4PzKIwNcyGQAfGMEiqY_oKH8_50BTcmc5zEVyTOL51gtGC9G_3_ZZEMuQLO0iZiiINJJXHCiUCMVOoDbueIgny_MEl7rXMU58LAdhJuCs3qDkpJ6zXw2J1JCq01eI0maR1uq-J8PXLR1kXnuC9dDxPzR3WIFp43wWldtPzGABEYHwC7XdNFzhYVHHFvgUULDTzUp4-_rr84qERc2fdAKiYbP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=fZaSs0GoahiUdKUfBBhWGsWDX3hAA8z3n7nlUq4nFLgGcruvlf4xJNDhwmEkiQPr5l82059uzJAQitSb5TLY25A0DsMxvH5aU4J2ejsf2w3CvFF9R3naWdRwG5XC4PzKIwNcyGQAfGMEiqY_oKH8_50BTcmc5zEVyTOL51gtGC9G_3_ZZEMuQLO0iZiiINJJXHCiUCMVOoDbueIgny_MEl7rXMU58LAdhJuCs3qDkpJ6zXw2J1JCq01eI0maR1uq-J8PXLR1kXnuC9dDxPzR3WIFp43wWldtPzGABEYHwC7XdNFzhYVHHFvgUULDTzUp4-_rr84qERc2fdAKiYbP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
دوباره از ایتالیا صدای گرگ میاد.
🔥
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106931" target="_blank">📅 16:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106930">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=WLaoqHV3uNnr-QvDy-rK9K-LDkPWbYkXzUQPgFXrSo23JvdYk0MOUkKQfylVjYp4Arl2BIHqbznsXHJv6eJt9dkxM8k4p2YEQQ1PcWEd5yG7kqwaJDG046rEQhOn9-NI2WEYLvd9RNrmPmWheaRP8rPa1OeaUvRsa0N4D9SW9acRMUhkJ-hHQXPNTdcI5UJ-bDnG4sFLrNQY6ExtfsOV6BmHl3MaEoD2Q02QXT1fRnJXcIIIJNDVk9CKQnUI3GtLQVnKE2XBf6IB0xNt8u2dS_eDJUwezk88hT5SPmWa5ejTrjudolG8WnUEo0gFqdeeS4EpCt6ih9keYGH7rUmGIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=WLaoqHV3uNnr-QvDy-rK9K-LDkPWbYkXzUQPgFXrSo23JvdYk0MOUkKQfylVjYp4Arl2BIHqbznsXHJv6eJt9dkxM8k4p2YEQQ1PcWEd5yG7kqwaJDG046rEQhOn9-NI2WEYLvd9RNrmPmWheaRP8rPa1OeaUvRsa0N4D9SW9acRMUhkJ-hHQXPNTdcI5UJ-bDnG4sFLrNQY6ExtfsOV6BmHl3MaEoD2Q02QXT1fRnJXcIIIJNDVk9CKQnUI3GtLQVnKE2XBf6IB0xNt8u2dS_eDJUwezk88hT5SPmWa5ejTrjudolG8WnUEo0gFqdeeS4EpCt6ih9keYGH7rUmGIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
بغض ایراندوست از طلسمی که شکست
پدر و خواهران مریم ایراندوست در ورزشگاه، برای اولین‌بار؛ خانواده‌ای که بالاخره برای یک بازی زنان دور هم جمع شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106930" target="_blank">📅 15:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=mif5M5tMEPyEpYolzcVxS8yLjoUAY4ShBgbNWyFGgKHsaoecZQXbHUYaD44vT_Jer-c-l089H3WczJ_mPRchQPW_0jt9IzN0YfbYp5BHU2irpKl51zL_S5uynaOIWwz2PUTWnzw_0edS56KkKYUZee_St5UoUhXn1xus59Piakk9JQ68DMjAY1UVHq2yExLTmetVKmuOfza6TYj26jJf424No5P_8nZSZ7O5xWB7_7mWN5gUrSwsLWn9609NE-gro0QCzUqjpw6R4Am8-O1Lq-7Cv8khyLClqU0m6JQ8Q26VW6MnYSBwW-LpRAauFFOxv3B2DrCbQudwPmVRFr39eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=mif5M5tMEPyEpYolzcVxS8yLjoUAY4ShBgbNWyFGgKHsaoecZQXbHUYaD44vT_Jer-c-l089H3WczJ_mPRchQPW_0jt9IzN0YfbYp5BHU2irpKl51zL_S5uynaOIWwz2PUTWnzw_0edS56KkKYUZee_St5UoUhXn1xus59Piakk9JQ68DMjAY1UVHq2yExLTmetVKmuOfza6TYj26jJf424No5P_8nZSZ7O5xWB7_7mWN5gUrSwsLWn9609NE-gro0QCzUqjpw6R4Am8-O1Lq-7Cv8khyLClqU0m6JQ8Q26VW6MnYSBwW-LpRAauFFOxv3B2DrCbQudwPmVRFr39eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
🇮🇷
فرشید اسماعیلی: یک‌زمانی در زمان رویانیان در آستانه حضور در پرسپولیس بودم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106929" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P15GtKUD0HvUTmdzT7M4lIOTGksS0bRRBCgSCO7L9eEsAWfSanO5fVOIWJHcsrk-ej_vkqaIhftDkpmRMBMApe8T9ayU7biIp52qhXLOqCYSk7f6f_0mzsIsdk9xRMWnKhdDkOyAOwJSViD4ZYgZOWkah1PcADqWOr32DGsheuEIVZa5lg0iFO_i08emMAwcLzDn2hZvObaw_Du2zR7wSJ3XBect9wkTUHrlWNRD9EeAz72PAOKXT7NshBD4n-INXFHl8pvPdOusmP7taJGGH1kKR1C6WQn_DUiQLohfYQKLZM7qie6IyGj39Z1LgnBGpNB7QpjVLVeSrYfzB6s54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشون زید دیومانده هستن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106928" target="_blank">📅 13:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=oWsuAh_9jSusM0CT_Yq_SrwrlHTQfcrxwM0qVAH0_saOdM-SxfuQQE0LZgICltzr-lqO7QpHlvrOdETyXk9Vmt8RijW4S3LZJAGBZOpGks1woncWIvPOhny8rGhajY586fnP61wMb7iOITT76a3LKzsb8D9P-OpbNDrV-xAL3Qp-_c9TQvIdxXwiF99pxf1HGaqe7TgZ0CnzL4YVBLCCd0_4rk1doU1s42yBvXBNhDykf9yOYquW889CdajGhGnVo7MBKsb0D20IMAXb6E9J5CPK6terxKPjT6YsNYtbN0Ewlz9xf-cnSd-_sCusjbUJ-SHx323MW4nGjmOjXvw-Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=oWsuAh_9jSusM0CT_Yq_SrwrlHTQfcrxwM0qVAH0_saOdM-SxfuQQE0LZgICltzr-lqO7QpHlvrOdETyXk9Vmt8RijW4S3LZJAGBZOpGks1woncWIvPOhny8rGhajY586fnP61wMb7iOITT76a3LKzsb8D9P-OpbNDrV-xAL3Qp-_c9TQvIdxXwiF99pxf1HGaqe7TgZ0CnzL4YVBLCCd0_4rk1doU1s42yBvXBNhDykf9yOYquW889CdajGhGnVo7MBKsb0D20IMAXb6E9J5CPK6terxKPjT6YsNYtbN0Ewlz9xf-cnSd-_sCusjbUJ-SHx323MW4nGjmOjXvw-Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رختکن چلسی بعد باخت جلو برنتفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106927" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=mydwVrsJuQW1Sv0NcDVbwgNpMPb-VmirIdrnR9CYTsmoKaQtn9jYzgSWgKI3LuiXqD_IBpwFiNSWDlik46yUljlP-okigKUDQGho5znJDfKapz79PIvi-0B7m8xf8zSEYhSBsEXeiR3ihRRL2CaLZ1vIXRqNUN591BmmQHBdsqZw69H-D95nvxr1yRLYHaDeczm5FwHYVnEcA3LZqjjPiliYpOWV1qeIvCB26mnsksmN5hk45JG3iD_EfczAZ33trz2I1d-dUIlWsfLJNhhBa4vt7D7a5r5NwJZ-KtUWCX_ZXfQLKoGNn5mtjjgGVxdCqR2JL5I0IdYW2WY5gg3l9C7iE-YqPV4Jm2WqjM7ZiUz5Bewbo1KpmxXzp0GOioP6__xig8ZUjcmmkvxk9M1bpYFiPZSRfrBbVG4CAKgQ6EveeqxHxP7uC6Z0wjVn2VLsGciXzo9g3jtQR7AQq2wIBTWPsXfNCxSkgDFyQcaV7kP0uhNn98NnP0yr8wwsfIalqt5qFGEITmBNzkxoWu-jRg6h4nV99rIBaqF7FWB6uC6fjfL9k0eKy_6-78cPX7Kqx_tiQtZI8P9w0fK7OYBBDiYFoQe8eez9Ai1gJA-VrBe3pBAG1yDfg0YlGC6Vc886p9ej5dWk7mayEKUdcwL7eeBhh84MgdIX6ySRrScZOMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=mydwVrsJuQW1Sv0NcDVbwgNpMPb-VmirIdrnR9CYTsmoKaQtn9jYzgSWgKI3LuiXqD_IBpwFiNSWDlik46yUljlP-okigKUDQGho5znJDfKapz79PIvi-0B7m8xf8zSEYhSBsEXeiR3ihRRL2CaLZ1vIXRqNUN591BmmQHBdsqZw69H-D95nvxr1yRLYHaDeczm5FwHYVnEcA3LZqjjPiliYpOWV1qeIvCB26mnsksmN5hk45JG3iD_EfczAZ33trz2I1d-dUIlWsfLJNhhBa4vt7D7a5r5NwJZ-KtUWCX_ZXfQLKoGNn5mtjjgGVxdCqR2JL5I0IdYW2WY5gg3l9C7iE-YqPV4Jm2WqjM7ZiUz5Bewbo1KpmxXzp0GOioP6__xig8ZUjcmmkvxk9M1bpYFiPZSRfrBbVG4CAKgQ6EveeqxHxP7uC6Z0wjVn2VLsGciXzo9g3jtQR7AQq2wIBTWPsXfNCxSkgDFyQcaV7kP0uhNn98NnP0yr8wwsfIalqt5qFGEITmBNzkxoWu-jRg6h4nV99rIBaqF7FWB6uC6fjfL9k0eKy_6-78cPX7Kqx_tiQtZI8P9w0fK7OYBBDiYFoQe8eez9Ai1gJA-VrBe3pBAG1yDfg0YlGC6Vc886p9ej5dWk7mayEKUdcwL7eeBhh84MgdIX6ySRrScZOMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اقدام عجیب و جنجالی سیگار کشیدن مجید واشقانی با اردشیر رستمی در برنامه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106926" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1S4Iw_slfXumC44s0F5NrewQFjcTfHDpRtFwEOHoVg7bYxOzAfroQ55pT2yJqcCiMFWyMnhb3HUG2btbfNXO3pOeZq-Miq8pGqsJTJ2xVzjCYKMxK6waqy5QqEsTI5Pax8gdO8nURWyaJpEAvsGHLuTwnpV8iBe6U1Tqv8MWxb_9EpOAcTd5lTn8CTNcTERZOo4CrBbTDn6uxfkCE5lRuoARt7aPTrEYOBcKyxpVxD0A9-W7UBkQ-ToqtB9szjPy1qXUCeZeNfZphBofM5J_JeRIXUO9DRUBS6ltynF00aB1T459Hcfr-aE1xTYUwkFZ2E4L_DtCzK7g9Kes6huGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106925" target="_blank">📅 10:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز متفاوت و جذاب از تاتنهام که برخلاف نتایجش، فوتبال نسبتا خوبی ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106924" target="_blank">📅 09:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=l1Eg3UyJ6pzD48eYGAjp3KfT5ObeOu-HctqV_Dhm5NW6VP4gbeqCcIVrxFNxQs5LgZTXHy1Awj6pwVAlDdWZAiQLbl6PxiisA-lsQNNgI66_hKCIv45ju-VcgVdv2q2nr_7eVO2eWeI182_Tkq6futOT3fZpoX56NJ64FRHIyIpgfa8XASxDbUhqdQERenFdLUn-NtxRCwah6oI4pWtHDG3jG6BCgLunymPW9VhHaPgBQjJdszD5q9iqftObwkrQS3inG9bg9ptuKtLh1d3PMd2dqwLPIqh4Dhaw6i8O_uAX3AbOGFS2IOSS47pCJ8LFqKcDgNHnJEN6Sh_KxRf6AoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=l1Eg3UyJ6pzD48eYGAjp3KfT5ObeOu-HctqV_Dhm5NW6VP4gbeqCcIVrxFNxQs5LgZTXHy1Awj6pwVAlDdWZAiQLbl6PxiisA-lsQNNgI66_hKCIv45ju-VcgVdv2q2nr_7eVO2eWeI182_Tkq6futOT3fZpoX56NJ64FRHIyIpgfa8XASxDbUhqdQERenFdLUn-NtxRCwah6oI4pWtHDG3jG6BCgLunymPW9VhHaPgBQjJdszD5q9iqftObwkrQS3inG9bg9ptuKtLh1d3PMd2dqwLPIqh4Dhaw6i8O_uAX3AbOGFS2IOSS47pCJ8LFqKcDgNHnJEN6Sh_KxRf6AoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😢
جوآنا ویتژیک ورزشکار ایتالیایی در مسابقات چین یهو وسط کار اسهال میشه و بی‌اختیار ازش خارج میشه اما با این وجود مسابقه رو ادامه میده و قهرمان میشه. در نهایت از مردم عذرخواهی کرده و گفته امتیازاتی که گرفته رو ازش صرف نظر میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106923" target="_blank">📅 09:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106922" target="_blank">📅 01:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RutxUt0fN-kDnR3s3vi9Q4cCm5uQ3rOv8Sl4fNPXPjalsVATFqfkm3wuoCwC1YY9fCgLA6jV-wS4-RI2Fisq0PjtKob5ki0xw5CV3EbYiDWTpyv3w-ngbcS8y7TGB7V3QZ8z_Nmb5dad-jwhXNIqkG93zMmgwOTXV2Ae6N7CzBAza6qPivRWVRVbSTQjDvUYgBRo8zWi7VE-Tkza-81JPmWigTFduwTEmYba39IUXt_HAUoVscWeEfM3wB3g1n9gz7MJxrcqgLOjVXZywUTair5G4ZPBbll3CqhComlcETj2jGa9M9R9iB8HuDb28k40pwMSuDLG50oF4ztgx2XZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106921" target="_blank">📅 01:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571388041d.mp4?token=m1N37iKAjZKT-ctbA2B8bjKuBStgMF9zuvAbMzoxsJ3NYtn6iob2r0YHrDK17-rTik6kcMw2_qSKthJGsOrB250UON3aHD-PezeBSojRmtp5D1cvN28qrIxN0wnpQTDVicbtXHk6SX3beQaX3tmROHA5QlFpsrQyB396lbb65I7hf5scytrvu7U_tnTkb7vt0UlA8Zq9F3wSrqlOhpFPeW7lUAVSUAtNUcPamEAzJQq3FKbZGqMLfiQWJ8ueBCp2rqatE81zzYmRDQ1gFsjad_2CwJ-DflpVfKtmI2Ut8ectowAesvrJhnr_qG_YGAnBAP_164NMecGKW96wjZIrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571388041d.mp4?token=m1N37iKAjZKT-ctbA2B8bjKuBStgMF9zuvAbMzoxsJ3NYtn6iob2r0YHrDK17-rTik6kcMw2_qSKthJGsOrB250UON3aHD-PezeBSojRmtp5D1cvN28qrIxN0wnpQTDVicbtXHk6SX3beQaX3tmROHA5QlFpsrQyB396lbb65I7hf5scytrvu7U_tnTkb7vt0UlA8Zq9F3wSrqlOhpFPeW7lUAVSUAtNUcPamEAzJQq3FKbZGqMLfiQWJ8ueBCp2rqatE81zzYmRDQ1gFsjad_2CwJ-DflpVfKtmI2Ut8ectowAesvrJhnr_qG_YGAnBAP_164NMecGKW96wjZIrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
کار جدید حمید سحری از برد امشب بارسا: واقعا کی میخواد جلوی این بارسا رو بگیره؟
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106920" target="_blank">📅 01:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iitqhZeAqWIL7H_KMOnmjdmZ3fEaet__KvmJS1KyvjQBe1KktfUtty1hCqq_UemIK1gMmUm99c4WTA5Wr6jm9lj07YV1dcBfJmwkyUUUsNJG4XuKDah0AQ9XnI9OjcnL9UOnB7k6LwC176CK-AZGZ5ZIYkLxT1ecOsdo_tcoGai3QYFwF13-rzRFsJ8ZVpnk2je6WSDWF9qFRW7qC9q19HcmM0ulCvoc0oGzz0FX3LH3IO7E0Pd32PVsl8JBNhft1aIJvRwrYpFurLJt0tMPgcJQN0CXqRdPUGa0um8XzjlIjLSIK_gI8LwCNaY3HgoSb0XecLklsVg4dYZ8wucZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106919" target="_blank">📅 01:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwoqs_iI-79DrxjjnDtZ3mLVFQ_C5hfc_nlfxsCnqMI6Ck-RJa7adSvAxejqH8Vl5Ik75_J8K2HWuSynizQWiFipwHXgutceLapuuANsZfN6whWOab_i73e_rrkUq02xRnSVrAH9fe23n0olu3RoeA467QoA0yHT1VyDhZONKG8awq_vKbUJySAWfTP0PkvD4H0nGhvURfA7uVND4JnGPeoh50i5kAlleP5eWMs8Ml76rHGjXEb9B_Gcl-jjHyxSj9yAROLtcInmD6-BFarF-OMEr0MUb1n3tAW2UTTdg2OFePYis5v5dZD5iOn9HUhWbwFcEnvZfIUG6-eQonz2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇪🇸
هانسی‌فلیک: شگفت‌زدگی بابت عملکرد رافینیا؟ بله من شگفت‌زده شدم اما نه امروز بلکه دو سال پیش و هنگام اولین تمرین با این بازیکن. او و لامین دو عنصر فوق‌العاده تیم ما هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106918" target="_blank">📅 00:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106917">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veEqZBUP3U59RG_iMMpjTAqNWVO6HXPygItOG6ttmzKogzqHJSlqRaxeSIfP3RqlD1UJYRrMXmEBOuMJPRgoNPVLt_pWnoQwN91CIhc9hiKac5W6JhR9tVHctICryPtPxgAoI93Ei8NNwg_z3QLMMQmG8x1F2gcfQ3laly2Z5X9nOeJeTVjjIP00Nefbrpax_-qrVrfjLMiGuX2eL_LRNKCwC629KMSevVNuJxKv-rbNSufM4A5vizHM1ltzWHnTbTX4nU7FocqZYm-7ZkRbc9al0XxnInWFkhU4CNrQcm5BEd93GHqRJSbVzw9KhC0OfMZnlROgBzUvdH56RRbPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد بارسلونا از شروع‌فصل تا امروز؛ بازی بعدی تیم وحشی فلیک ۲۰ روز دیگه مقابل ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106917" target="_blank">📅 00:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106916">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnUR6Y4X_iynVwb0WEWyzDD0lpgme0PZS8qaaw4FVBGjNKQJl1V8Wh3Z6H8Lswg0VdEwZ7X7Nr9x3ehhDoP0a6we2KScQ2h7RHR-Idn3a6OZXXqdJjJhoZ5PDr32VnWBdpfNJ-x4Jg9bjvd-BM-0Z4ND6faF0rBHQJZimVhSF2cFNozIbexYTERe3G3P_XopgInwE7z0oNddl8snbP1c3pZ0mo-W3fGpp3-z8WcUaWWR3uJ_maoqj6UTRcyRkMpCcV2Gx71_fEt-vw1P5S00abcyppjYJv4ebMbzedT3kV-ZLf05XNI29BiF-JI6_4mz1jGOCmeejasy1HpTIpyc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
هفته‌هفتم لالیگا اسپانیا|یکه‌تازی غایب بزرگ بالندور در این‌فصل اروپا؛ بارسلونا با هتریک کاپیتان رافینیا در جهنم خانگی سویا برنده شد
🇪🇸
بارسلونا
😆
-
😃
سویا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106916" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrT4bV3Tsy3hasku1iRZk7144xthiop7npA9zsz2BI51Peu1sRsANug1d2kzJyXfVVgEAIcBi0L9ndKE2_fGrBLBQEWctonopZbH5EVcHQ6NltuSOLzZJdyW-Wf_VabtJ8-E_q3LyUPeIxqb1JX8QfS0SY7N3I1fRkJII0185FOqIAE-Fj1lfHAloG9rizymIjhLCHLjjxsE9yA0l_wRw81_QGvD1RWxFvsE7qy5-Nbw08GTBNrEoOhntfifKryUj7YDuS8dg06whO2qceTzQnrVMvztaRUbjJHDyU1sZbcWMSsjS09VKadlqyLu8ACbN-y2GSz2Xf1zSYDe7oMgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
😳
😳
😳
🔥
🔥
🔥
🔥
🥶
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106915" target="_blank">📅 00:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Govy1_SgFGvkumRjJvsfQXntfChtyseBKPyd74-1QpvYQ-jtjXEB2mJGrDAtY4YIdWHLL5oJFHmuSW-L0NZdS3iUhcMnNpl6S_7CkBmwbDNses-a-3G-L12s2iw7RzwpQd222a_HkscC6Fl_JezDIQEXY5Q2vqb0ld-NzamNByEGDzgycMfVi5_Q4Iokgx1aGjNg-ugwduZ5pU8w51Bs6JGNGBqjs4bMrOT9t3rkLfRRzmTqQAMYU305yaaavYY5lsl6Stm6t4TRcZukL45sQ6wJOmBy6Y3UKxNO1qQ5KV2xrBkohcb9f0OzF5PPK-EqejEJoMbXNDzma0We1wpRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106914" target="_blank">📅 00:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACOn4FsUJsvndic-voWweB12KwXq7cLymR-fxj3ZS7xGxYzZqEDbsWJ9a_KecR5WByHEaqLtA7gHBuGFEN1vmOp0FujjKSb2fpRup4K8NeC_yEW6pwipdwN6hzQ3QvHgatgjm4GkGJhUVTHwDeFxwu2i7RrcfIiMSdpCL7CfH8sRtnjQEdyJGwwQw4o-DUSMZRVOEKXuKC75I3cRmdLQAQyZGC4d78vjh3R2Q83l1flKa3L1ogGHyCzAOZ30iLyyf9Z4Aa0C8xuxB7UWKoKuHvVw6O1z_3Yx84UVTkc4BNfoNuQVUPMCJZUXum8RzQRtUS5KVhxZZL3GwQT51re_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106913" target="_blank">📅 00:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106912">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چه پاس گلی یامال داد
😐
😐
😐
😐
😳
😳</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106912" target="_blank">📅 00:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چه چیپ سکسی زدددددددد
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106911" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هتریک رافینیااااااااا
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106910" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106909" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106908">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=TICfVNEfXfS5YyeD7K7ntLBXXvxbt-qZD0R05Hpkh3AxFefIG_x0FvsFosMppEqRnSinxMVvwL599zTzWk8sFgaAqmLwPtEQZx5gA-wUrHx4pmBFRW23ZMjqvUQ52BzhxeLTa_3OJWmAfI49Iey5Q_LqWw1Pc_buMb1ZJKSENfxPg2HyN0lKSCKSCm1Evhl1NKmLp6c6kTE3bx9HnqK-1Q65X9ywjvm_8i5T8dm4c-JzUt76q0zAr5kL467ftQhOP5U7LEH3j_6ItW3sDzRHjVQ_Qp5A6Q29Vj0AiKlKs-lzPIsNIGRdST6I4vFceQNknXqEDkJrWQSMa82aJ3kEwkXLgDJ5Rcj5pSa_sFBrF6mMSO0l5JQyHHQPklU6DimAQzIOIyYHFWodDBnzcTXSbMqchM0RNCAdwqHkDM2jVCZ4ALCO7tL4iFihQ4VlfgRPWR9eVArDmhrSWI36SjCKprh7BNola0XC5XySDIhTmKco6WP2QB0oF33W3cnXwYLGVhHRflDCzIuE6sd4MqHrTT0ADKyywCg6VfD6_eloJHvz1BSCRIaE82sSEeIwPuY1-dO8bYgvJ5wu3hgffwrASm-prIesxSA66LjdBxl-r7Kar3EKmpWUaVXseMU1-77RLnX80p6NxVI-j17SjmQlgqcc0v-cwWCmo6sa8qDFjTM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=TICfVNEfXfS5YyeD7K7ntLBXXvxbt-qZD0R05Hpkh3AxFefIG_x0FvsFosMppEqRnSinxMVvwL599zTzWk8sFgaAqmLwPtEQZx5gA-wUrHx4pmBFRW23ZMjqvUQ52BzhxeLTa_3OJWmAfI49Iey5Q_LqWw1Pc_buMb1ZJKSENfxPg2HyN0lKSCKSCm1Evhl1NKmLp6c6kTE3bx9HnqK-1Q65X9ywjvm_8i5T8dm4c-JzUt76q0zAr5kL467ftQhOP5U7LEH3j_6ItW3sDzRHjVQ_Qp5A6Q29Vj0AiKlKs-lzPIsNIGRdST6I4vFceQNknXqEDkJrWQSMa82aJ3kEwkXLgDJ5Rcj5pSa_sFBrF6mMSO0l5JQyHHQPklU6DimAQzIOIyYHFWodDBnzcTXSbMqchM0RNCAdwqHkDM2jVCZ4ALCO7tL4iFihQ4VlfgRPWR9eVArDmhrSWI36SjCKprh7BNola0XC5XySDIhTmKco6WP2QB0oF33W3cnXwYLGVhHRflDCzIuE6sd4MqHrTT0ADKyywCg6VfD6_eloJHvz1BSCRIaE82sSEeIwPuY1-dO8bYgvJ5wu3hgffwrASm-prIesxSA66LjdBxl-r7Kar3EKmpWUaVXseMU1-77RLnX80p6NxVI-j17SjmQlgqcc0v-cwWCmo6sa8qDFjTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا توسط رافینیا با پاس یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106908" target="_blank">📅 23:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106907">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رافینیاااااا دبل کرددددددددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106907" target="_blank">📅 23:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106906">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگلگگلگلگگلگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106906" target="_blank">📅 23:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106905">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1OYGdcPgUnPTyy9X4hfC5dNHOyl_ZYjrVK9DP9kXsLIospdfO-g0kmZqMrlO2F67ExVs6vrue7E9Vsb2Rbr0ljA_CnGjTUU2GRP23BhHNHPP0Go2kJo98ydDQcQb6gvDLsw9sjGPbfi3ZOTPSbTNqUeR5dm9WR_03RZuZLqQFZLuJQpaowWI4cIDYiyKse6xTZAzDK4J0CXlxV1vtFvJlgE69c1rh9_zAfOCLuZIkzAWJ6cnnl2_ifvWiSWUVmyJH_895WDq3HHdqN2R9puv64XZKLjtE6Ax4VdIyLckrBBMfKVNvsbcYASsB9k1Je2gpnZj7nyoGjvTVTO1XDr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید زلفی و نیما تاجیک ۲ گزارشگر مطرح و باسابقه تلویزیون به پلتفرم اینترنتی نماوا اسپورت پیوستند و از تلویزیون کناره گیری کردند. پیش تر محمدرضا احمدی هم از تلوزیون کناره گیری کرده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106905" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106904">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e51312166.mp4?token=cpATrEi3tSWPlMWaMU0MpWH7unOFe_SQ2oKJyd7-x1DpYsXhzEJoSAGt3ZisYImMuhUQMrDv3kLNd35elR6K_seYT7SUChxD8DUrBepRr8w0w68Il-gYoQXGHPeD0m_-9Lt3upjZMYUaaQeGQaqjG4FikFRNWirSgiCtwSsiTxlB3mhoFxdJVFaVrYtHYi3AMGlNlWF6rpMaQUp4ifZ5ZMGXA-FRPHXl2IwW7APk9J6bfrzYmRhsvOJbWneFd_wrGCiA_8zEqHVWC5eNnupFgF9V524ollc2mRHjiSOadoqnHNmD4G3bGCpLbfXx0n3Y36v0QIxrJMi302rBlgDmV1nvw_Hdwtk51vP_tGhxcBT5FTfG9fyvJ6lUWwXRCagMK5296TXQAZUkJYP5UA18rjibqm4CJxlEaMMnsgq_KdQ55gr03LIZoGTCNU_BqQ51ncuRIJt2i3ge7Uc283o8qoUVxSINs3xa9MWbAiNa4PEdxEHW64gS8BsTjBagt4zNxke09zp2rxxC7Duy6U0p1CHy03CV1cepunNu0ClP0WvErEsjlUVFYI4C_mmjiFXZrGtevWcGds4i241aoNCmFXT2pZIRTRU6KBjzLNOPYnQuJB-H5t9yR044O6-D9uPqSUXdB5n6JxVT2riawm6YFLpc9GKK5-2z0T6r9htwQM4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e51312166.mp4?token=cpATrEi3tSWPlMWaMU0MpWH7unOFe_SQ2oKJyd7-x1DpYsXhzEJoSAGt3ZisYImMuhUQMrDv3kLNd35elR6K_seYT7SUChxD8DUrBepRr8w0w68Il-gYoQXGHPeD0m_-9Lt3upjZMYUaaQeGQaqjG4FikFRNWirSgiCtwSsiTxlB3mhoFxdJVFaVrYtHYi3AMGlNlWF6rpMaQUp4ifZ5ZMGXA-FRPHXl2IwW7APk9J6bfrzYmRhsvOJbWneFd_wrGCiA_8zEqHVWC5eNnupFgF9V524ollc2mRHjiSOadoqnHNmD4G3bGCpLbfXx0n3Y36v0QIxrJMi302rBlgDmV1nvw_Hdwtk51vP_tGhxcBT5FTfG9fyvJ6lUWwXRCagMK5296TXQAZUkJYP5UA18rjibqm4CJxlEaMMnsgq_KdQ55gr03LIZoGTCNU_BqQ51ncuRIJt2i3ge7Uc283o8qoUVxSINs3xa9MWbAiNa4PEdxEHW64gS8BsTjBagt4zNxke09zp2rxxC7Duy6U0p1CHy03CV1cepunNu0ClP0WvErEsjlUVFYI4C_mmjiFXZrGtevWcGds4i241aoNCmFXT2pZIRTRU6KBjzLNOPYnQuJB-H5t9yR044O6-D9uPqSUXdB5n6JxVT2riawm6YFLpc9GKK5-2z0T6r9htwQM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇪🇸
گل‌اول بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106904" target="_blank">📅 22:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106903">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چه گلیییییی زدددددد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106903" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106902">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رافینیاااااااااااا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106902" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106901">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلگگلگلگاگگاگاگاگا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106901" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106900">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگگلگلگگلگلگلگلگ اول سویااااااا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106900" target="_blank">📅 22:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106899">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f072da801.mp4?token=Mm8tkozMkq5BJ9KA9o6pOflZTeFJLJVpsr7b04-MLCuGHGM-JEdkRVib1KJiy9cZHfyadLl7XQGtQPcSwIanAxj--DJ19kLYPfjYdpgqR2I-xjgMee189KkDP42c9z-5J0bLX12etb-OZXaCF9r3OmdxQqhxhbQoeAX8Gqsl6NTUXde5hoFlVG1FcnK8dEcuYqAlJ5YDo6gMJIs8tV4VXSEhzXHqgO_vfOKvWn-GXN_IIaL383HI9rNIAJ1SKvZvPtUcrcvalo0XZBx-M2Q-rn-OtvlxlK071WYAgbUp8Z0nycnwqeBz0BtCfY5H8LUNfa3NAdCiXImEc3MTEITKoXnyX3WHsBJwFDKao3LUFpdgfZS44d45gkdYWiTy3Keo3C0rrnOZhoREXJyU5nf3Hds4euNkC1euacCTVpJ2II9VghSRNEqtDYzT6fDJXyhrQ_ifNWRTaVR12vdmFwZlpcBzHqK63N0LW0CxBfuu1Z45DcaJqSyfTkKybVZ2qlgIwI7vtchsrfqQYpmFCIcxAqWkC0BK7yTlQXZLVdWyx-KksUstaA8Q830LiDB6A654eXqYsW2e6r3SkuRyIIVmAs8qulz9KLwaT84jWQh6XYr5yxQAIrvjruT8ta0DosXp8GaOqaaOPjO9-tCS_473vk-0TN0F1iHiaWX-fBV5vTM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f072da801.mp4?token=Mm8tkozMkq5BJ9KA9o6pOflZTeFJLJVpsr7b04-MLCuGHGM-JEdkRVib1KJiy9cZHfyadLl7XQGtQPcSwIanAxj--DJ19kLYPfjYdpgqR2I-xjgMee189KkDP42c9z-5J0bLX12etb-OZXaCF9r3OmdxQqhxhbQoeAX8Gqsl6NTUXde5hoFlVG1FcnK8dEcuYqAlJ5YDo6gMJIs8tV4VXSEhzXHqgO_vfOKvWn-GXN_IIaL383HI9rNIAJ1SKvZvPtUcrcvalo0XZBx-M2Q-rn-OtvlxlK071WYAgbUp8Z0nycnwqeBz0BtCfY5H8LUNfa3NAdCiXImEc3MTEITKoXnyX3WHsBJwFDKao3LUFpdgfZS44d45gkdYWiTy3Keo3C0rrnOZhoREXJyU5nf3Hds4euNkC1euacCTVpJ2II9VghSRNEqtDYzT6fDJXyhrQ_ifNWRTaVR12vdmFwZlpcBzHqK63N0LW0CxBfuu1Z45DcaJqSyfTkKybVZ2qlgIwI7vtchsrfqQYpmFCIcxAqWkC0BK7yTlQXZLVdWyx-KksUstaA8Q830LiDB6A654eXqYsW2e6r3SkuRyIIVmAs8qulz9KLwaT84jWQh6XYr5yxQAIrvjruT8ta0DosXp8GaOqaaOPjO9-tCS_473vk-0TN0F1iHiaWX-fBV5vTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوووووف صلاح ببینید چیکار داره میکنه
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106899" target="_blank">📅 22:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106898">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106898" target="_blank">📅 22:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106897">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNPITAqrs_pXe8Q2eRGLCfH1vIWExZG-zsZgFDBsNyo8MOTpGZLaMI4ynDmz5vN27lmGCNhw38mqfjFJiU_1sGeMgHCHeqoP6835HJvDPccSa6_3hvO_wAYzkYPTFfJ3PCEPmoPwnatXFrRuqgNOytr2115c7Y5i2Jjl3vKpBo2lI7sIJIuUE5bVf79WqHXB5WGdayBQNdOnfe9sptJaAclzYg1cBFDX3hoblRtzQ2qsJ8twP0IEjd6mZjPWN0HWik6tqT7TIEJvNm0D1aMC4qa2VVhJ5xZ4LmXqP0NkexfyV9ldkAGFiYXYwVnfDihZlhrCY_ClUsa1y5YPT2p1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
حمله شدید دی‌زربی به بازیکنان تاتنهام:
🔻
ضعیف‌ترین تیم‌تاریخی دوران مربیگریم رو دارم. اصلا نمیدونم این بازیکنان چیزی از فوتبال میفهمن یا نه. اصلا امکان نداره یک تیم اینقدر بازیکنانش ضعیف باشن! واقعا براشون متاسفم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106897" target="_blank">📅 22:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106896">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f38027f14b.mp4?token=fK2XQLwCbSZmEbwS8OlkMl_YRuIc-S9lbvENEK1bGZ6QvtFr30dqPax4mWjLbY4_8QyI-OB45FrE1Up7HeYkFlt2hj9allbU25-Q0UrleCDinnmhh5gzASVl7BhYApuvnwBJw5dJkTjWv3tTXsjO5iwzJeT2o0g2pUWhI9Uj5VSw3aOwweyAYDWNVJiAe0H1IvWBSPVEQxvBbvskuzS28Gf--VHWHZIOTOMndS2IxZ4zyeKgEp7TD1Ga4lo5OMnSTciPxMFCCINB0c8tMvhwr_Lgzvqa8MbZVOLCzm2jwu3PN5NuwDUlLseNGxuT48Y8gJ51ybAW6P_VTRoAwuuDzkgSMpDyqLeJOGH99zrRjVLhkeJfnMWWqHimoyN_IlhmCdsjrwMEbiQtNsPBb9LDrC9mUiNcPMrGoCRtf_0unrawLW5Q0tYTaVZRrUpxEMDeHtXfow8eKipJD81rfCGkXI4VyXBOuvk28C3keRB82R-YoZSW0SMUSyQz1OQCbI9UInNdBiiNjY9dPVEwnQSlHogyWfxk8V3nKpP0V3VKul0Mp9dXXXNqSMTdy_MhRUHdqpYL7l32jyjSVz8aAJm41iWMuF74gKEviQ8FvLI3wYhCVbxR8q41PGRdrTmbmv_kB94dbA02zHdEqJ5T14qKFAC6hnfp5dUxD_CkoMvsWJM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f38027f14b.mp4?token=fK2XQLwCbSZmEbwS8OlkMl_YRuIc-S9lbvENEK1bGZ6QvtFr30dqPax4mWjLbY4_8QyI-OB45FrE1Up7HeYkFlt2hj9allbU25-Q0UrleCDinnmhh5gzASVl7BhYApuvnwBJw5dJkTjWv3tTXsjO5iwzJeT2o0g2pUWhI9Uj5VSw3aOwweyAYDWNVJiAe0H1IvWBSPVEQxvBbvskuzS28Gf--VHWHZIOTOMndS2IxZ4zyeKgEp7TD1Ga4lo5OMnSTciPxMFCCINB0c8tMvhwr_Lgzvqa8MbZVOLCzm2jwu3PN5NuwDUlLseNGxuT48Y8gJ51ybAW6P_VTRoAwuuDzkgSMpDyqLeJOGH99zrRjVLhkeJfnMWWqHimoyN_IlhmCdsjrwMEbiQtNsPBb9LDrC9mUiNcPMrGoCRtf_0unrawLW5Q0tYTaVZRrUpxEMDeHtXfow8eKipJD81rfCGkXI4VyXBOuvk28C3keRB82R-YoZSW0SMUSyQz1OQCbI9UInNdBiiNjY9dPVEwnQSlHogyWfxk8V3nKpP0V3VKul0Mp9dXXXNqSMTdy_MhRUHdqpYL7l32jyjSVz8aAJm41iWMuF74gKEviQ8FvLI3wYhCVbxR8q41PGRdrTmbmv_kB94dbA02zHdEqJ5T14qKFAC6hnfp5dUxD_CkoMvsWJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
در هفته چهارم بوندسلیگا، دورتمند با یک گل مقابل اشتوتگارت برنده شد و به صدر بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106896" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwkmjErBdLHSjY8WcEQPLsSUx0NB-cktT6Qlw2Y-ej4eH4IAhfCh6gtCWKhGaKabhCUslr4-H6ucqH81xTA0UY3vIpVC_79RIY_Lpr6u3kOaQr8nOrMm9RaOcepZ9hBU6EBmGiO99kLsNc_E-PSSGhAEALllRhhUHiHEpDJZlwRUJCZ515CmnReDGdJJz40XqJX-trDgjZdImAnbV5wujb00NkhLS-jjRjoUH-c0u6DmfbokeVvdg42-R1qbi8z_Da_UVESduN0Yio5yB3TSCe3phESdOagsNLnmcKbq5jJOuYLxCWiTadDT9knP7c3oBuTDL1fPF0lwRV9kQG448g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست اتلتیکومادرید مقابل رئال‌مادرید با حضور خولیان آلوارز و غیبت سورلوث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106895" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=ascoG8c-PqCahUVNiJiGt3o60GKTqfGP39nPGQsZyB0qwo6L_CL6dAppcyQPr4KUbKUGoZ_pDxPkOTKvc5VhMPJGDNhOZLfMGSVBslbAtbk91vYrzvdh7WKrsEIAfsQRynccl-UPhgJRJS0DxyNBi4pQw28LJZ4vOv-xx3--EVq1BAZ-KebgbOQ7Uxwd4QgFYsXe2rF1hiQr0E2jq6xewYjm_xe_Jq3QCuEwxHSWCPsgzHFDBVah7J4n7MPI1Ys0s4NmMUneYTTxBpB7AI-7camygNzc0-Ufl7enykHu152BIEYbf000_TRNUszHqP-N9kpWXl4ctfXqtlM7yYiTi42nDcBHQkMrOc23IyYiMHYUHihRebHAmYZw8qbdQpwo9MiAxABFwUKHj8MaT9dmw6vgz8rneNYynwUXOwenC3VdF44fCFkP3siz7Z1eb-vlxIQGUbGmOs741O5jJzNSnPC3sKUab1WCXM92jkRr7EcQ_ECN7c7J2q0BIpDUhAGJOFNU0VBAOxUq6gnzlrmE3OhmiBs7ZtHt7PSokAbLmeZKf7ftFh-fOKOMjlYbjmaupuus7o6gw81ETwDs3a4fu8oU9eqaoYcH5tSuOvkG-dgmWoCLWQ_wcS0Vzk3REQQO0oGZipxOoej5P_7Qhc8Ty2_42XQiiq20yZaRe5miNzM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=ascoG8c-PqCahUVNiJiGt3o60GKTqfGP39nPGQsZyB0qwo6L_CL6dAppcyQPr4KUbKUGoZ_pDxPkOTKvc5VhMPJGDNhOZLfMGSVBslbAtbk91vYrzvdh7WKrsEIAfsQRynccl-UPhgJRJS0DxyNBi4pQw28LJZ4vOv-xx3--EVq1BAZ-KebgbOQ7Uxwd4QgFYsXe2rF1hiQr0E2jq6xewYjm_xe_Jq3QCuEwxHSWCPsgzHFDBVah7J4n7MPI1Ys0s4NmMUneYTTxBpB7AI-7camygNzc0-Ufl7enykHu152BIEYbf000_TRNUszHqP-N9kpWXl4ctfXqtlM7yYiTi42nDcBHQkMrOc23IyYiMHYUHihRebHAmYZw8qbdQpwo9MiAxABFwUKHj8MaT9dmw6vgz8rneNYynwUXOwenC3VdF44fCFkP3siz7Z1eb-vlxIQGUbGmOs741O5jJzNSnPC3sKUab1WCXM92jkRr7EcQ_ECN7c7J2q0BIpDUhAGJOFNU0VBAOxUq6gnzlrmE3OhmiBs7ZtHt7PSokAbLmeZKf7ftFh-fOKOMjlYbjmaupuus7o6gw81ETwDs3a4fu8oU9eqaoYcH5tSuOvkG-dgmWoCLWQ_wcS0Vzk3REQQO0oGZipxOoej5P_7Qhc8Ty2_42XQiiq20yZaRe5miNzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
نبرد اینتر و رم با تساوی دو بر دو خاتمه یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106894" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106893">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=sA78AEhSCNGFEjkWFQLQfvp0SJ61YW5Vf9m0LORI04a81C4QV4hrE5SCKy60o_DK6bFjhCfgDWQI6QSGM6TJePe8a44BMw49K7P-XVFmt2Yln8YrFMSU-iBfbxNhXAALvH0fYz7F9gXEiXVWtqcFFMZ5Z5HjVmhOlIUwTOPxtZXXR38T7eNnidYK3jSMQbM1tq66ZW2VUgc4tWt0WG8mrGhoA-Gp3aF1DCxKrwI6CxLoCROLIX6nlLiBd_Acvrn4M9PKMcQ2QsA2M_gHj9oIbzkfVdSB9VAkPdMbmkisMRZmRPoa74DhDZ_IDJ1oYONHeG2_WG7TtWOPFOawUviypA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=sA78AEhSCNGFEjkWFQLQfvp0SJ61YW5Vf9m0LORI04a81C4QV4hrE5SCKy60o_DK6bFjhCfgDWQI6QSGM6TJePe8a44BMw49K7P-XVFmt2Yln8YrFMSU-iBfbxNhXAALvH0fYz7F9gXEiXVWtqcFFMZ5Z5HjVmhOlIUwTOPxtZXXR38T7eNnidYK3jSMQbM1tq66ZW2VUgc4tWt0WG8mrGhoA-Gp3aF1DCxKrwI6CxLoCROLIX6nlLiBd_Acvrn4M9PKMcQ2QsA2M_gHj9oIbzkfVdSB9VAkPdMbmkisMRZmRPoa74DhDZ_IDJ1oYONHeG2_WG7TtWOPFOawUviypA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106893" target="_blank">📅 21:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106892">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhds4CckjRbwJbPDKEi2XfD3ujGjTja28JQFKITqenu1yxBSXOqdb3IvFZQXaWLUOhncGSVirfsrw7vi0pqG4PXEaic_llkewbZ0omYcnXkNd81evdNmS6Srpn38dWtomeGOvsqSX6Baey4gCFyJEcaZRetYf_LAoxJIKyzwclAqts3nmCpSy7AssZAOo2jpvAw_vHF_iHiasMj4z9rU3zZQURcrGjA6Nqh5cQ6-LDdF1VtL7KKQXwQ7O8S-CDO2c6BPYAmLNKrVs7njYdYTymrjLYH1efHkGTGCPdvD02OgGVaXMkvSUgdbHDMcQJKgWsSUN9Nkybu-LKuswNHTTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
شماتیک ترکیب بارسلونا مقابل سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106892" target="_blank">📅 21:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106891">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d419048b91.mp4?token=VSoIuhrnt3tKR2XePv4WBUNFNXHFYc9dZytC9jhatieyVzjk7UoSXJX40U2H1f3E0sIUzjawEJaKj_UObvuVSf2TQnKvXQa7H-o2I5-_qhcucJh4vnfXw1gnkjCa9EAVWjV27ptShfw1kKXc2V-Ti-8-tZLEpwt-lrgKi9fOYtyYqWTm5x9Y083hz2di0EsMpG0kHZwlVRw0JD5yQIfsAUsYl5DRnLOIeb2DP5dai4YxfWnIVhNsmOBV8VTRF5xBwIoZGfb4ljvhosOrTolxGzOKUn04cPMrk_PMhMKSgQvRUKhfk8_5kjyhaIv9z9iDUUQf_xxSh_nPYDb8dAudow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d419048b91.mp4?token=VSoIuhrnt3tKR2XePv4WBUNFNXHFYc9dZytC9jhatieyVzjk7UoSXJX40U2H1f3E0sIUzjawEJaKj_UObvuVSf2TQnKvXQa7H-o2I5-_qhcucJh4vnfXw1gnkjCa9EAVWjV27ptShfw1kKXc2V-Ti-8-tZLEpwt-lrgKi9fOYtyYqWTm5x9Y083hz2di0EsMpG0kHZwlVRw0JD5yQIfsAUsYl5DRnLOIeb2DP5dai4YxfWnIVhNsmOBV8VTRF5xBwIoZGfb4ljvhosOrTolxGzOKUn04cPMrk_PMhMKSgQvRUKhfk8_5kjyhaIv9z9iDUUQf_xxSh_nPYDb8dAudow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
گلزنی محمد صلاح مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106891" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106890">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=Q0_iTCezoR57gOMj3mQf1WMG_8yOfxHcqoqGXR9i2RbSReCRD-qS7y862oKg_Yddjx741Q8xkpct93VPDnOOlVvnxYvCOjFneE8iBxQQRmLNCOB51or60or1mdZkDrHejJjBJjtK49HGOc-4x2begr_LDp8HaWFv-jAoRnKDqBaVEN8HTYWZZVdCahMB0LdepUaplAu-EY4_FvFBZsJ3sxx7PxvTbAlNb1qgpvc0qXk36AkhET-SglmEbsUjtCDvrZmafEc4T-Bjvl_NBe5t1jKCmiGGoyQhB88mNhHFpXaadcGLBQrzi4Wgt0LtCIFTPnVxFo610o5Hk3bTQ8bbaUPkhAEBs9okD-jJzcPGKN5tzpXdPxULb8bfnguKi5Mvm-bUWROm7fsplM-GgF-vXTIiodYBCmib6xr38av4T2YDGgiMvvJZd2b7UsS2dAuKtbx_ioLukP05uqzDi_TTlWdNcOa6Xb3ht1ZQxsedygp7y5szNNkJq9lIssFasgGR3vunJQ0HnWH7qz26CY6WmV4DJ2NwQfpZAGx7DuUG0Tl9ada71c5k6eU92XC39BOXHz_ialerNR1VWcpsn-xhoPEBTis9ogVwany_QaPYYVNzr4R0brSrisXo-G-ym4fGuvRtDShRv9q_X2cHiFgZ8hTl6SkGAjybpajPQKEwpoM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=Q0_iTCezoR57gOMj3mQf1WMG_8yOfxHcqoqGXR9i2RbSReCRD-qS7y862oKg_Yddjx741Q8xkpct93VPDnOOlVvnxYvCOjFneE8iBxQQRmLNCOB51or60or1mdZkDrHejJjBJjtK49HGOc-4x2begr_LDp8HaWFv-jAoRnKDqBaVEN8HTYWZZVdCahMB0LdepUaplAu-EY4_FvFBZsJ3sxx7PxvTbAlNb1qgpvc0qXk36AkhET-SglmEbsUjtCDvrZmafEc4T-Bjvl_NBe5t1jKCmiGGoyQhB88mNhHFpXaadcGLBQrzi4Wgt0LtCIFTPnVxFo610o5Hk3bTQ8bbaUPkhAEBs9okD-jJzcPGKN5tzpXdPxULb8bfnguKi5Mvm-bUWROm7fsplM-GgF-vXTIiodYBCmib6xr38av4T2YDGgiMvvJZd2b7UsS2dAuKtbx_ioLukP05uqzDi_TTlWdNcOa6Xb3ht1ZQxsedygp7y5szNNkJq9lIssFasgGR3vunJQ0HnWH7qz26CY6WmV4DJ2NwQfpZAGx7DuUG0Tl9ada71c5k6eU92XC39BOXHz_ialerNR1VWcpsn-xhoPEBTis9ogVwany_QaPYYVNzr4R0brSrisXo-G-ym4fGuvRtDShRv9q_X2cHiFgZ8hTl6SkGAjybpajPQKEwpoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول اینتر به رم توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106890" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106889">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/102cd70646.mp4?token=MGr58kk5G_lEqI68jYPJjM9TynPKvgevCKsybCSu8iHixrE5knMp1wv86QMTTBzxk84mpypowkJkmTwmxYPSOTAFLW9FwPj665mHhddwzp3-Ci5mrwJyVNyrUxW6qhK_kr-qrW1IpqzvCB9mz0StQ5LJSquOB06DhzcG3zSVZpSywt8GReP_-CsIfC59bhjKrqivM2VsOt_vh7Bldb2N_bMBZABjH3dkcW0k3NussZEyByIz9qmeY47WIiAX5xuK9Z5jODTjnTDQMUOkpZv-DY_HAJQiBL7LmfCJswKbdTCFArlIBTW297WverVlYIHUih3acMLZAoMzJRXDDavDgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/102cd70646.mp4?token=MGr58kk5G_lEqI68jYPJjM9TynPKvgevCKsybCSu8iHixrE5knMp1wv86QMTTBzxk84mpypowkJkmTwmxYPSOTAFLW9FwPj665mHhddwzp3-Ci5mrwJyVNyrUxW6qhK_kr-qrW1IpqzvCB9mz0StQ5LJSquOB06DhzcG3zSVZpSywt8GReP_-CsIfC59bhjKrqivM2VsOt_vh7Bldb2N_bMBZABjH3dkcW0k3NussZEyByIz9qmeY47WIiAX5xuK9Z5jODTjnTDQMUOkpZv-DY_HAJQiBL7LmfCJswKbdTCFArlIBTW297WverVlYIHUih3acMLZAoMzJRXDDavDgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106889" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106888">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=O45H7HsXIRGLkvJo0ucp-03HZxSYXq_npdlH9MflwlQEuNUS1w_m8zbeaIozacBtqsUnTEoIlL9VuJaZD8bohCb1OkvjLxnI6qeTMMXIHj3XAaTPYVxmMM1TNKPNxxT7UAxP4z-VvWw6DRKDj0oKhSgiqBR9y2_O_1gktm6UcZznVWrtO5FN-OQtTV1etaIrq4iqMpnZEYJmtbqT5qwisWce8p5RNrgRKpn8hPNZ3LEYIVl-MH4fwANaP1_qtUF0L6Hcyg8mIOdzdQkUVifu0B5b4ZE8yygvmoVLf2u8tjsPMWfGafU6Hym2cpU14kBxOvP8eB7tU7ahEEAhg0STPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=O45H7HsXIRGLkvJo0ucp-03HZxSYXq_npdlH9MflwlQEuNUS1w_m8zbeaIozacBtqsUnTEoIlL9VuJaZD8bohCb1OkvjLxnI6qeTMMXIHj3XAaTPYVxmMM1TNKPNxxT7UAxP4z-VvWw6DRKDj0oKhSgiqBR9y2_O_1gktm6UcZznVWrtO5FN-OQtTV1etaIrq4iqMpnZEYJmtbqT5qwisWce8p5RNrgRKpn8hPNZ3LEYIVl-MH4fwANaP1_qtUF0L6Hcyg8mIOdzdQkUVifu0B5b4ZE8yygvmoVLf2u8tjsPMWfGafU6Hym2cpU14kBxOvP8eB7tU7ahEEAhg0STPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
⭕️
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106888" target="_blank">📅 20:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106887">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=XoZZGdGjhZGt0h5AgOZk2tQ8A3p_hC7fiHO_YMkfRvPYZKShdPAJajQz7UW_VhGTDK6LePVMZzJo-vcZjyI_EWnFNK9_Yy5S8b-81RhNkQm0KXXs4KtdCg188obYKXsaIxV3ryU4FoNpVxuMoiSdMh0MgyJjDetssDuVjaZvsCTiLbZETVHlDAMdQH-splx0qrnDpAnvBTVYekCq6t3Pchtcku6ElV96cnyPtMYDRTHKdcu4rH_vlEoYQY8-rIpz1JbDxz1Yv48Wr-ofREde5P0lerQeMVC3P0bCjd1o3QmU1rM58r9fMBjLYxrRtuFGXKYorcUj_5mOJkrHiB8AXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=XoZZGdGjhZGt0h5AgOZk2tQ8A3p_hC7fiHO_YMkfRvPYZKShdPAJajQz7UW_VhGTDK6LePVMZzJo-vcZjyI_EWnFNK9_Yy5S8b-81RhNkQm0KXXs4KtdCg188obYKXsaIxV3ryU4FoNpVxuMoiSdMh0MgyJjDetssDuVjaZvsCTiLbZETVHlDAMdQH-splx0qrnDpAnvBTVYekCq6t3Pchtcku6ElV96cnyPtMYDRTHKdcu4rH_vlEoYQY8-rIpz1JbDxz1Yv48Wr-ofREde5P0lerQeMVC3P0bCjd1o3QmU1rM58r9fMBjLYxrRtuFGXKYorcUj_5mOJkrHiB8AXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
انتقاد کاویانپور پیشکسوت پرسپولیس از کامنت‌ پرسپولیسی‌ها در پیج السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106887" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106886">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzIQrkqFXDOriH3RS1eUflGbWq3_sQcqQqnEQ9gEU1_AQw8KhXDV3a26BpECdGdNn53eDmaTy_RIThMIXwTbF1yccWiZzUb47vFxuyGZvezCNZRiddVIVh0eFEry0OOUDafOKSC8NxMkIc5rzcOebyBK8P09tMoRnlD_JsRcoEG7jJqSb_BLsW27mSJm7q8x0ZaxTKMBMAyoilDZz8fPLu58ui1L2UxvZ05cG9jb1FAzsFT09EtLsN6Qt3B5LvlzcovPc1VZdq-jfixCwefjdGDEdJUbA4XeovFCALr2_jqV9I03-fDzpEDX5VUQ3_dHd5I-r0XNGLZ7n0k2MoGwa8wU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzIQrkqFXDOriH3RS1eUflGbWq3_sQcqQqnEQ9gEU1_AQw8KhXDV3a26BpECdGdNn53eDmaTy_RIThMIXwTbF1yccWiZzUb47vFxuyGZvezCNZRiddVIVh0eFEry0OOUDafOKSC8NxMkIc5rzcOebyBK8P09tMoRnlD_JsRcoEG7jJqSb_BLsW27mSJm7q8x0ZaxTKMBMAyoilDZz8fPLu58ui1L2UxvZ05cG9jb1FAzsFT09EtLsN6Qt3B5LvlzcovPc1VZdq-jfixCwefjdGDEdJUbA4XeovFCALr2_jqV9I03-fDzpEDX5VUQ3_dHd5I-r0XNGLZ7n0k2MoGwa8wU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل‌اول آاس‌رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106886" target="_blank">📅 19:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106885">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947613cda4.mp4?token=SHhol9uVRommG19GqsL5xHkUHqAQMj3NAfabxlXJFJkLjjURVcL-mQCfcKeUX8T5HjpbBFVDGfDkZtBi2gi3i_453Qtfvnfxsm6TTn3mdr6JnqSRuF6zBLRTpp2EKOHAWb3kBAjc5VBItLdVqrobkEM68deRZPt8hNlnVKVXJAfB_X42mfqnRQrj8PX9l0EfEV7rr1VKb1oCxONoi9IxMmTQ524nTMTQjhrOEmB1X6FQ6-WJNDY6eHk87jexoqXOaV0TJ9VJUSc4wW61JeGgpTZ3_GBR-GgUI7gHlVQNJIcCp8gNpFMvHJiS5XEpLwSpO0DAmOdQji2kCv7jYiMN1zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947613cda4.mp4?token=SHhol9uVRommG19GqsL5xHkUHqAQMj3NAfabxlXJFJkLjjURVcL-mQCfcKeUX8T5HjpbBFVDGfDkZtBi2gi3i_453Qtfvnfxsm6TTn3mdr6JnqSRuF6zBLRTpp2EKOHAWb3kBAjc5VBItLdVqrobkEM68deRZPt8hNlnVKVXJAfB_X42mfqnRQrj8PX9l0EfEV7rr1VKb1oCxONoi9IxMmTQ524nTMTQjhrOEmB1X6FQ6-WJNDY6eHk87jexoqXOaV0TJ9VJUSc4wW61JeGgpTZ3_GBR-GgUI7gHlVQNJIcCp8gNpFMvHJiS5XEpLwSpO0DAmOdQji2kCv7jYiMN1zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خواجوی گلر پرسپولیس: الگویم نویر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106885" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106884">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=NrZIj_uI3KG02uwP60rFgDAJagiVcoXGm2bzo1OSpkkl25nd8iGaZekfA-tPtednXLmcziu6r9ePXHN8erIIfTTwD9USYhQ0yn_-C7VeEMR8YS95RtODqSckCdpKzq5fW8mfLY2_n2hU8pi3t2ynRCPzrWAivyhgFW7Ty45qa6ff-XOtiv0XzCDYKGcyEIno4anQobQoM_6iqCJ6FClw0hz8uUoPZR1v5NIzv0EogdvJUsbjwbPgoc7Shq3sph5cAR9CzIiYi5UjD_Hylm27otgdLqpzZfx5gwV-IxmUEG6NNzLvA8_XOiygE64ccf3tSO5r6ZIZxm2VaRuJ3lpLAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=NrZIj_uI3KG02uwP60rFgDAJagiVcoXGm2bzo1OSpkkl25nd8iGaZekfA-tPtednXLmcziu6r9ePXHN8erIIfTTwD9USYhQ0yn_-C7VeEMR8YS95RtODqSckCdpKzq5fW8mfLY2_n2hU8pi3t2ynRCPzrWAivyhgFW7Ty45qa6ff-XOtiv0XzCDYKGcyEIno4anQobQoM_6iqCJ6FClw0hz8uUoPZR1v5NIzv0EogdvJUsbjwbPgoc7Shq3sph5cAR9CzIiYi5UjD_Hylm27otgdLqpzZfx5gwV-IxmUEG6NNzLvA8_XOiygE64ccf3tSO5r6ZIZxm2VaRuJ3lpLAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های جنجالی یاشار سلطانی خبرنگار، درباره چرایی برهم خوردن توافق پایان جنگ از سوی نیروهای سپاه و جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106884" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106883">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOJHDVTg1WLi3GXbw9-6lLYM_lLWgGDxrJj205v59BtCNenURHqeN0OWHEH-baEuuTmr7KFSGnTW6gERtIH9qtjn62fFYKjs16M2xjSOjWt1g8NPmQl0xLliLXRbEJUXuqGEhKBG1dIo88OYBdhKv1gWL8QbAiLUxotXszT0HFCESRexKB8kQOTdcwKF3A0Mxv4pTw6D9n99lnYEXWSQXJuOZRi5jtlo00maQEd-HAd3tzt3ewooF1yZh5BwWBaWuKMENuTmtHE-864O5zi874V7G8w2VCn9XD90uSYjBBjDaQcENh3YOy7HGLcj7W4ZTT33BC4IZtUNu5T7sfPhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکار جدید کاربران برای تأمین نقدینگی به جای فروش طلا
🔹
با روند صعودی قیمت طلا، فروش دارایی برای رفع نیازهای کوتاه‌مدت نقدی توجیه اقتصادی خود را از دست داده است و حفظ طلا و استفاده از آن به عنوان وثیقه راهکار جایگزین بازار است.
🔹
وال‌گلد و بانک کارآفرین امکان دریافت وام تا سقف ۳۰۰ میلیون تومان را با پشتوانه‌ی طلای کاربران فراهم کرده‌اند. این تسهیلات کاملاً آنلاین، بدون ضامن و بدون چک از طریق اپلیکیشن وال‌گلد ارائه می‌شود.
برای دیدن شرایط وام کلیک کنید
برای دیدن شرایط وام کلیک کنید</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106883" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106882">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da8b096322.mp4?token=Tb2yN1X8XNtxWZWUtd0lSW1VVYGCd9fNnSEJcmF1BtINNSXLWyR0qkkgAfqyp5nio8Z0F8Hz115cCBbxj5463DdfvoapmgIlMzXn5p5BZrCgfHuaAxf1UpRJR0xkr8TKDTLpU4wMU0RnssDr7lLbZJ_uwLluWLcJ31W5uTu1T1qlXpmWqoErtm2k_ZRLWHyN4DiHP7ICDh1Vm2pAoZ7MummoUmFQQNioaeBBd78xsCnJn0VcrbXa6M5EEcDOVDi79bGfpreHqx1VqRn-_rMbVyqIOSzNb3EVEff4UQmPGBaT663ebbHTxgAq4fmM8wCHMU5EUBMa_pvEwotE7T-Ylg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da8b096322.mp4?token=Tb2yN1X8XNtxWZWUtd0lSW1VVYGCd9fNnSEJcmF1BtINNSXLWyR0qkkgAfqyp5nio8Z0F8Hz115cCBbxj5463DdfvoapmgIlMzXn5p5BZrCgfHuaAxf1UpRJR0xkr8TKDTLpU4wMU0RnssDr7lLbZJ_uwLluWLcJ31W5uTu1T1qlXpmWqoErtm2k_ZRLWHyN4DiHP7ICDh1Vm2pAoZ7MummoUmFQQNioaeBBd78xsCnJn0VcrbXa6M5EEcDOVDi79bGfpreHqx1VqRn-_rMbVyqIOSzNb3EVEff4UQmPGBaT663ebbHTxgAq4fmM8wCHMU5EUBMa_pvEwotE7T-Ylg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106882" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106881">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARHIq_6MXWioWypeczexF6FT6UnVGqYUbx-IN5HuFuurOsMcgceR3HzEQuQSxhO6TiAupxkI3i8nkbudHDOBaLENBucWv6Y4sHyXTrXQ6T6CHfnqlqR9aOxGEkRQ0HS7kq0TUIO8LfLQvyaCNjl32aosBBDS2lkbpdQz1ObxJP4GC-8fTirR6Bf3ZmrNJeF0gDD1kVY08ycUv2O0846ueRqMOKk8fOOfyODlBYnVCifNj0C4q7-Pzrf9HqtugmOEoadeAaxPdxO3rTDhACm4pp-tKsr2MoyKJETw-vEszuneVtvwt7W6Rml_scntMe6aIoFknEZEUzzrU1aWbMeNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اینتر مقابل رم؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106881" target="_blank">📅 18:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106880">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=aKLZyNi12saXo8u9JaAbaMwFgMYQ0KO8gpSDbODyPssuhUEjO1LhuoAcnvnl3NmW6_5UJqHbtdyevO3_8gEv97xcZn24bDkl7zPouV7qo8kvSUD3L7uibUAJSRrRgtBi6w668BfUgP0VkR8vkDqyUPXJ8Q3GLYthFdA9UkXZf57EWvku-3oIHFGI5VUReliaiqZ1eRVz9fhIECI7gsGEgtyDcPg_lB3v6ZMQ4r2J7ItUFNq_TJ5uVgiodvlzbqN0KdPNnt2P3_oXl0i9Ipgm30O7JisESxOi_JR293gSIHzaK8yOMyjbA4IZXrsEpVvjH8Q-jrb357F91zayoDeM-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=aKLZyNi12saXo8u9JaAbaMwFgMYQ0KO8gpSDbODyPssuhUEjO1LhuoAcnvnl3NmW6_5UJqHbtdyevO3_8gEv97xcZn24bDkl7zPouV7qo8kvSUD3L7uibUAJSRrRgtBi6w668BfUgP0VkR8vkDqyUPXJ8Q3GLYthFdA9UkXZf57EWvku-3oIHFGI5VUReliaiqZ1eRVz9fhIECI7gsGEgtyDcPg_lB3v6ZMQ4r2J7ItUFNq_TJ5uVgiodvlzbqN0KdPNnt2P3_oXl0i9Ipgm30O7JisESxOi_JR293gSIHzaK8yOMyjbA4IZXrsEpVvjH8Q-jrb357F91zayoDeM-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106880" target="_blank">📅 18:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106879">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگلگگلل آرسنال دومییییی خورد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106879" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106877">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3613208345.mp4?token=TRcy3AJF3q29jchudG7ywZefpsXs8-xz1wkC7caAya2tdfdZ759s4058pVMiB1XsZbQtRWY9kWTaRkZtsYgLUfbKVblI2_iTO9YwDnJP_pcJDSfSZpBGC9Z7mtf_GqxoqfL9ngExwf2aEQS8vWroWG13T_5WNaclE9QB0rh13KSbXTN0fU4xXEISgslDbz8NX2n9_7Ycwx8ZzazcI3fOAl-fjQfLy1ZGyhdK8t4NrSTDUN82R3tZUBdQeC2FesAkJxugLCx9pB1ND4FbRd7mlWZDXWLp14O3Fa-zIPhA7Tr-vx_7fmrdiY89Tf4lMwPWYrF23Hwi9tbZwnsmusN68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3613208345.mp4?token=TRcy3AJF3q29jchudG7ywZefpsXs8-xz1wkC7caAya2tdfdZ759s4058pVMiB1XsZbQtRWY9kWTaRkZtsYgLUfbKVblI2_iTO9YwDnJP_pcJDSfSZpBGC9Z7mtf_GqxoqfL9ngExwf2aEQS8vWroWG13T_5WNaclE9QB0rh13KSbXTN0fU4xXEISgslDbz8NX2n9_7Ycwx8ZzazcI3fOAl-fjQfLy1ZGyhdK8t4NrSTDUN82R3tZUBdQeC2FesAkJxugLCx9pB1ND4FbRd7mlWZDXWLp14O3Fa-zIPhA7Tr-vx_7fmrdiY89Tf4lMwPWYrF23Hwi9tbZwnsmusN68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل‌اول برایتون مقابل آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106877" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106876">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvagjbnbH_-9o_2F-ai49mxQ6myt2IBh4bDLkrT0uyUSK_04p7bwk4BEnHLUCM5sjtGDhlnDTduDXqzQIpjWvWWqBECP9aaa82UnLXKZZ6uCaV0qvrk9VpTOd0hvVb9sjH7cvravyB4rmn15GKUHL1Wh3dYchIkL3XIPb0ILMLTTh_ZV_ntr7SsaHmBvKvn5grqt9hvOnuXz0yDhqEj2zTNqkLcYgSccF6dUNyvyOXYeTqSLRFeL0mYtoaSU5fbfJr-RnFqd1PaLTjM-Q3bevUG4Q9t6lvxJd-B_JYxQHK0KI0HGN37ydNv_41Tnao0cnmAVaaF1SPCTAzA3IbY9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106876" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106875">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slkNaUNY1pbmbGryZ6E0533xgc0mZ98gVzLjdPuONZ5-2uFWw2OYFGPOfuR-zg2tojRUpE-GmbqirXGNKYLGKmlrEp3U2u2ws4OnNdDi3Cg4mR7E7miM-dx13ZDeC6Eq8EQiFSQgPmVimhlH93VotVC5ANEHu4_LtTQLisbDzvivkgdUknEDrtUzgnm7jd6Rm_SH28AS7sdbHVDtokV1BHJioQYNaRfPIb3IBwIufAUVS8BtJVe9NmX4B6uOaAuIjyPfw5riJTT6OGox0DefUw_lW4UjVFGscEwOM4R51eWX4AsrQW8l8mw8uRzWOJK9V_SmUEG2YK4aRNEom7cFOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106875" target="_blank">📅 17:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=Zqdvly61n-ce8-PU4tfUjmK-mMfl_7WXSijjtasbEPqEyeI5iKhbiYA-gus31iPBvtt5lWhpMVuCyHE3zNZ1FAsel19bqhXtSyHZr0sPxJnL-fvtdNSBl0o2qn0YBafN9UOreB2gtBMOIH5ODsMByDlR-wf--Uz3iWc0osWSClPw8pQSPSRvoTCMJPnc_Hx28NELUtOlz6WQ0SaUCxCMN7JEZUMO6NZEhCDgM1YpnGPPlOfkvY9HI_bgUYCV_IL-DE6xkNyEYQG_40RGbbW97Fv99KMvjPyqUvaztYln9NHHsLdLhBGfDrdSWRsuCYPkfXTB141M_Qu0z1IDnWEEmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=Zqdvly61n-ce8-PU4tfUjmK-mMfl_7WXSijjtasbEPqEyeI5iKhbiYA-gus31iPBvtt5lWhpMVuCyHE3zNZ1FAsel19bqhXtSyHZr0sPxJnL-fvtdNSBl0o2qn0YBafN9UOreB2gtBMOIH5ODsMByDlR-wf--Uz3iWc0osWSClPw8pQSPSRvoTCMJPnc_Hx28NELUtOlz6WQ0SaUCxCMN7JEZUMO6NZEhCDgM1YpnGPPlOfkvY9HI_bgUYCV_IL-DE6xkNyEYQG_40RGbbW97Fv99KMvjPyqUvaztYln9NHHsLdLhBGfDrdSWRsuCYPkfXTB141M_Qu0z1IDnWEEmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
‼️
🎙
ماجرای دست رد مهدوی کيا به قرارداد ۲‌.۵ میلیون دلاری!
🔻
مهدی مهدوی‌کیا: مدیر باشگاه داریان چین بعد از دوگل من به این تیم پیشنهاد قرارداد ۱.۵ میلیون دلاری را مطرح کرد اما بعد از جام جهانی به دلیل عملکرد، خوبم آقای عابدینی رقم رو به ۲.۵ میلیون دلار افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106874" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106873" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106873" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCZriqln-52lNlXjJRjSYu1ZDhinU7o47tNn8g1q-S241IcZvHmFeFAKMVMuoB1yIn7Pk5BxJYV1zC5WvOp5geYQiVpOFzKmsmXmdymi_5qxlADbLVfYEDVK826s_eiCMxcVIZig4P3ttbxRJohDDgxflul0iNjC_UuvXGHNdjE51qE4wCN1QvmPrd0xJFvTo3XRII7tvFJdx0o1Ju7ehugtINlyqBF0WUz2FjD7iziyLf1dtzGw0TBLeXC52kibLublma6EfCkIShkxpDiZaXc5Bpq7MoL3uBpDlPzU5iT8JRCHbu0tIqs3x-juTwQj_NzhXa-mwYRMxC1lSHEsnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106872" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106871">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGvR92hAQEX1uV3mQ3KgjHpKNuVTNBiz0qJQFrEbavmjD5bCjP3NMcw8Rljh4dhhKHqAhPPaGjEkpjJv1rv7DjmvyI3mWdeMQ98s5PNNeW0LKFfqw_fWkJm6jyOlKaDbhCjRk1yfe4TCVuyhpjk46jW7ZERWtrDCobV526-U44ue0n9g5kmQMqbgNmA6-HHkIAWoobXy8dIO96LuCNmbWq6eUOp021FHahWiyMUwFI3o9npzdI3p3LG5kumFXF7UvfekZaB89qJ6jj6HeIF-W2uJvPNYIj6z-9-thDBUrVrouDAQNPa0IGBLVqqwKev6Pgq5xMfMqL5qAqnkFNf1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
ژوزه مورینیو در پاسخ به اینکه آیا از شرایط بارسلونا نگرانه :
🔻
از نظر تاریخی و فرهنگی، رئال مادرید قابل مقایسه با هیچ تیمی نیست؛ بنابراین من هم خودم را با هیچ تیمی مقایسه نمی‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106871" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
