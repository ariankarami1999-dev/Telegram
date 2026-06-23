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
<img src="https://cdn4.telesco.pe/file/ONWm_RBiQtHKKk4qpirnmPYnSDcPFu7acWTLAJ-_JCScXByFAjIZZjfKsKSQuUAFsPhFObPTrGNIVvUVArI2ninB2Jr-CEj5ejdOCkpirJUwvTPo5TAb67guXSPSWh_-Hge2T2DQNkYAY2-pt-7alXRP0K4fgsaD-j_wS7yCYqeptJmfMh8ZlR0CaXJjgd2oWqx0tg16n-ZaH4ZnYOKegg2olLM4oQhzro4kRT_N4A0Rwkzh-rLJ-UTuFumakpUhe7Kk786Vb_4iu8xYrYF-aaGtlFwOBQe3cG6IxJNaCRbhR-Nso_ERh_P8eXLoOEX2Yxf8Z9ShZg-a0dG7E5k7Ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 312K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 03:19:16</div>
<hr>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZRuFP4VdpZhSj1f9TlDscExBlnT8_fOH8KfuG8W90ANPgcdA3oyYuMOORdLaFkkSPAWmgHSct3BYLy7WDafPLxKtjLA0_KrV9YE5FQ-uOTrUOvm2_b8W7jUT7-3Dk83pAUJs27KtFtRW8wNITF3Mhvalx7J-AFEWhYj5cAgsFrknUUUurZ8PQQ5TWDrsfGwe8lgi8dFX2D7epYIVG-h76pjuzC6hAbYScCaDnUu7JtppCOPHOH8mubNdMqI7lFBmQB6guIn6F6yG-kcDdVEtbkKi3I2ksTfiRzRQnPbja4jHUjrHu8xCc0qa6cp4fic7yQaT23z4joUxrpswc2zmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK4OrHnt4U9XhVqeM6e-pXlt0W1Ul1Cmr6cT06fsgWvvARMDW4rJtYjP5EpXofOswrkLaO8_cnQrAY4uKj2DLHWP3ilsPdv-A4ii1ZrwxP5Wlm5wTyvYbkhCTQysMOEp-de_YvWx-VJHqpPMjR8A3rex1wdCDwMx440q0M8uu-LCTe_W9oMw0DtQ9gxrkIh9-hIdPep5YnBfy4LXiYzbpryTzDcx1QqYV1pONPckAtneSORcmXzwXHnssEM0VVmbdhbYQUCEXQOE3YzUcqJFfzG813IxW8B7IZhCU-qdUxgARm9GrjRK6HUNX_ASIosfW29GJBotpvKgDqZCTK04hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhIi0YwxXbRzQ5ZVjEQ8HtQqT52L3vzEHcy80epZwUHp2CD_qeNyThv0dcVNCRsyIL-I1ns078tfxzlZ7VKEL8pNMCr5tqre-yXz3u39T0jmjwTPGPL82TNb-fD4UYEaf4ACOXkyq5-TEFsptMQ37EV1CGCirizO5Ht_2MPUryN-bzGjBVn5dCZxe6oOCG9wWt97CgT97O5C7N4RA_xnBfsBO0dEe_ZUhsVa82hdnLgIATeG1RZkZ-BCyziaveUOPFTxxhq-N5pWx-GuMwOoMIKLx98tQli52QpsrGexK8WVUUqSogO_sCO1JRCZo05FtYZWdWZ2N04LuFFZu_TU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOsoFGsby7C-SF3jX_JD46TLxRs6u5VnV_iFKatOOPWCLPlJwCNrmgig0PtWNqncMSUd914OCoXD61OtdHydERTbV0iVs7gApBHSQTTUN8mBmU5FFaXWnxPRAqdkTawVuKift4OvhjeXQ9lcxpJyQtAXtGDu2ZFpJVVAQfbJwSdYQoaDLVq0ETleM3KOAoB0olPGN6qdHIRhPa6bEUmTPcTqK-mIsc0F11qVvQe3U-RdcDFWTPOCplIW06lrVZwaByTZX4BGJN2HbjiZrzFSvuIwIgwD5Rjm4Zxg1eihJbDDRxXz3kgUxpJTuABpLQUIJPO0AP4iRlUNQYhqi9zDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaU6mvZmy78P_38ekQG-qNTB11bw6U8Npd25GE-uFzK4WJuE8ykKgU-3gkJFVUjBuZR9dVK8wAAr4vBzFwZTo5sGe7VfjnQ3TDSgFfymd3-zJwV5lmT-20VSQvqj2qpztPFVtEfZ_yZzlYgHpH2F-2GcrvcjhgTZs0ECOmyRwHDh003nvCT2l7hcfT284jLug7ey69oWxsy31Y_mWl_lvhZ_SP5r7pTKMhDCy-2lzW4kOcOwlXzTZ1a6pq6rh6PY_vAe2k86CVqujdPWE7y-8xsHae-KoQwwl1zlLBR60B91uk0tGQ5w3EuYU5pAn_TPOpCOSJXBUT5_BDZC7Dnefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=NVBDm8h4Uc5aUtAMlvWVAeE6gOL9y0PKc-8fDRRsfq_fjsdbZMaU2EX0n_TDAOPJMgy30qEyXTH5gp1Vpv4R851RvQlBcTbf_yEaTR6w3lcwuARLn5tG_IxJ9Gl_8g1UQSk54zr1mqZllCg8j8QWTaQvrTMu1t0Vm6lFV2M70IgK3K09672cv5lAYZLBlp_haRqZYFTfMtzmO4V_Y-M6U39ZMoh2X6rYvQ_Y-XoN-O9dLl9QelyKaEimxfd_pqxuKvJ1kx8stSi0s0o5EKekFcXKvfsgqJr7J4Vb4RQuTyVAdAgFhQ119yv2P4aZKi2kIZG5n67JPqNCYHURHLRe3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=NVBDm8h4Uc5aUtAMlvWVAeE6gOL9y0PKc-8fDRRsfq_fjsdbZMaU2EX0n_TDAOPJMgy30qEyXTH5gp1Vpv4R851RvQlBcTbf_yEaTR6w3lcwuARLn5tG_IxJ9Gl_8g1UQSk54zr1mqZllCg8j8QWTaQvrTMu1t0Vm6lFV2M70IgK3K09672cv5lAYZLBlp_haRqZYFTfMtzmO4V_Y-M6U39ZMoh2X6rYvQ_Y-XoN-O9dLl9QelyKaEimxfd_pqxuKvJ1kx8stSi0s0o5EKekFcXKvfsgqJr7J4Vb4RQuTyVAdAgFhQ119yv2P4aZKi2kIZG5n67JPqNCYHURHLRe3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glg8DelYFXKBAPzxb3oLWfdINmq_Ss1H2UoeDNA3M9CNLW64fR5boucyzlBnS1zL5Gq9_ptIyZIc_N6JsHm82SxF22T3sF742y-iLM0SWLQ1U459m9JWJFkvERAXvSlP96SV7cx9WYcYs0dZ9llGP5DndIbeFKVRFrFR6e5O0JmCDTZJXiykvLXx79nd6k1DFhNIyQ2AG3U6gdnspS3i7s9m8IBeI9PXtRLg1O9qSw5emIjKFyFs0SqNQTlt5j2wl1OUMyZHybyBVPgQsPkNPrjxuOPzCBex8XFcgsEe2laOMmOBF3LrU7g3bFc7l_ShvhJUaP24j_viBkSR8AsL_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24173">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdKQNMneHC6rG5P8ZONW1aB_qn7YbKtyFuxhki1o-KOpKvrSAfWPXkK9k3nOqpocKmA6NXTAAb3vodrU-Db_liA7kfANGeY8clUnp2rpUpvu1hcifnsXsHDotqjaQbkFeTg0-qY1W0VSIAnAtdjOq-Nn5tD5wHJJ9vvKZx-QxsuJwBaL6sw7OcXGrsQ1HBghnjCaMdEiOZ6bnNmv_fAEQqomIg_aFUOwt05mKJVWqKdzROVEpzWie7W4FBZkE_DVDCsKKFYoHKdIkMf6oOwQf1e8mkVzN1DoWOQvtCn99Xqec4NBgOp-Gn8GisaheefPB3iUeHXi_EhqP46VDurqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت‌آنی‌میتونی‌برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا eA2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/24173" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=qU8mOqCIN9G4DbHiiEQOiPrc-ynPll-Te3G-zxctFx4gLf--KEPEB3rMXlu3_g_7i4vZ4p9UAmMxPhbeWYtLRRU096cnz63ysRYdgk4l0tCBPXfxTTD5sgFV4Ro7H_Ov3QofHj-8Gsl--f01izRyfg5WbXFZokbGCVnEN9K9FL6qcMJJXUKFqk29_LUWo0eohPNXjchnWTw0cKhjVZcUsdIXaS7Huq3bbESjSWsZ0xVLvVSwWQbNns_8NPqZLugnFtm0iin8Z95-CnfqPAy8VahJAyfGTENBaJ_lrskHmr2FNn1pf8IR1vDI89wBpQIrVX5Lh92evywn5wzuq7bgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=qU8mOqCIN9G4DbHiiEQOiPrc-ynPll-Te3G-zxctFx4gLf--KEPEB3rMXlu3_g_7i4vZ4p9UAmMxPhbeWYtLRRU096cnz63ysRYdgk4l0tCBPXfxTTD5sgFV4Ro7H_Ov3QofHj-8Gsl--f01izRyfg5WbXFZokbGCVnEN9K9FL6qcMJJXUKFqk29_LUWo0eohPNXjchnWTw0cKhjVZcUsdIXaS7Huq3bbESjSWsZ0xVLvVSwWQbNns_8NPqZLugnFtm0iin8Z95-CnfqPAy8VahJAyfGTENBaJ_lrskHmr2FNn1pf8IR1vDI89wBpQIrVX5Lh92evywn5wzuq7bgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZnzcXi4VhY_axKvqoYRO2rfQnf7fLayxJmCB05UkLqK7j48x3RGororqUIAXF5Kqq3umjwVbub3SAo3kuSf_phg0Xvg7jFj32zT8fKys3Xn60JVvz2rt1Zj9WXvoIglTkTOsqh3hIl0kMO9c_OaDsiTXJRBiV4SGm3AcvLwuISPNJb4BKtMdGBNtli4pmeAudprAf4MKXtXBflqSUnVRmrHEQ_1AYvxam9SDhk4PVuKXxjWX_ay-XpgPwV9ZkIPsH-pHLe7lz2kc5Q0Poo5Tz_sp9zj0sgDIhylyeKzAR0i106ddi97lUePfE9J610v9sQjfH_fQtfAQjP8V1IrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=MTI0eR_6nXzd3uJpbAw-ApIQ_6iTECTej3gEMe5gxhsKWI6E3hggEAtiB7Q00rucEDmrn1Um2DUaEa5jXViCRW4LC26rkIElhZOAOsrVtugBQaukP36-1XKKXejx7DT4as5e8YAw4L-G8hB3x3HAB-D0Ki6-Q7UMXtta98uB1I48WJ5TZx1jP5TtUayiDFPG65gXU8zQLEhWoOiOpKIMeYWeBwxKMIusFLLjbEJuIA1FweiBTrik0fLK5LwFJbYMIJeKl7DAupTIEFa1rlPO03KKGXNYvbLfw5BNi3jD9_0Ko77idTefbdNiXM56jMGmAUhKNGMBm7wkJDWAv6wnBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=MTI0eR_6nXzd3uJpbAw-ApIQ_6iTECTej3gEMe5gxhsKWI6E3hggEAtiB7Q00rucEDmrn1Um2DUaEa5jXViCRW4LC26rkIElhZOAOsrVtugBQaukP36-1XKKXejx7DT4as5e8YAw4L-G8hB3x3HAB-D0Ki6-Q7UMXtta98uB1I48WJ5TZx1jP5TtUayiDFPG65gXU8zQLEhWoOiOpKIMeYWeBwxKMIusFLLjbEJuIA1FweiBTrik0fLK5LwFJbYMIJeKl7DAupTIEFa1rlPO03KKGXNYvbLfw5BNi3jD9_0Ko77idTefbdNiXM56jMGmAUhKNGMBm7wkJDWAv6wnBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlMIOJlw_iShtuWZ79GtAT_N28fkQm0ROkVh92OISlfVGBSXHWZtQc-8ZzOjL20RgyRrOYDqrP3xeNOyHZC0gHpsiEDbpF5-gxF3E0V1QaH-WtMv4WjqNXExmBgjSb1_hgGx4ffQbzO_22VmknPdouRL-CfE2zNmG6luI2O8jfakT_EQVMzpA9et5BLj4a-c79IoAyyubf3vfZzj4nk6c67cRlsr3RcrVs8hz3EoPWuQq3fJKxv_uUZQJEMxC9JjEz3k0HyCFftHFQovmSooFLetAOSlduYn2zOaFE0YSbPdDQtLxUUfUbSJLOhTLAJh3tgUOJZJ0c06uAEYOErTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y11U6RkLxI9_lsLYqvEiPpmmokN4Q3TUaMc7oSCAmglU71GrvS-xTTY5y44Q6W3KhduxI2KBRimwlN8lDxRb5L74KuxYlXoZFqFQ6yH-xhjKnWR7pIVwaNr8pNK7JfRdeB8nnH5HoqvIeiApTXhIlv1UGoOtxzcJuq8UPZdA4_LqkE_cs_dBCL_HNmcW5qPUCa0E2-TSgEPLlkv8SOcieLCBnvzxaWdTSp7bNU4yDAKdz156J2NqIT_aHSshE8NKlYTiTT0Hr8sqqKLceIG26agNx7PpqneylOyz_Xp5n5NFqyvxL-W2UuF8DzBMWrW0rd9PJPpt5ViaFpTD-V0rAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=ZxAou3ppvF4Hg33_kLYCs8Gb_UFPxH4hBcjLqwko1UU_hdXg-ZqIJzk7Kg8Mf1IPmjj2Tm3VHNgExsssYmD4SEBN0TjSuK3Y714ga-0vR6nQd-g_pxkH1FFYWBQnUqOHiylrCLJ7rB8kkKmzzKbiHGQ9cWHy1krvNSSLSOu1Haw_H7trZUR4moxgdE2qt96GZUaL7OC-FQfd-Uh_ARjtQlgPoHtnOpXI5Gaf2UbB-hkG0AMQt5Nb0droy17T8NhBgB2bh7gg_DB0mwBHek0fx03dPD5sG-X9_1xNhFnBNt95bKOW4G4LzNJ2gOmdl01C7cCqSBzJOukticKu4HJOJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=ZxAou3ppvF4Hg33_kLYCs8Gb_UFPxH4hBcjLqwko1UU_hdXg-ZqIJzk7Kg8Mf1IPmjj2Tm3VHNgExsssYmD4SEBN0TjSuK3Y714ga-0vR6nQd-g_pxkH1FFYWBQnUqOHiylrCLJ7rB8kkKmzzKbiHGQ9cWHy1krvNSSLSOu1Haw_H7trZUR4moxgdE2qt96GZUaL7OC-FQfd-Uh_ARjtQlgPoHtnOpXI5Gaf2UbB-hkG0AMQt5Nb0droy17T8NhBgB2bh7gg_DB0mwBHek0fx03dPD5sG-X9_1xNhFnBNt95bKOW4G4LzNJ2gOmdl01C7cCqSBzJOukticKu4HJOJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS6__bZMZuKC-DVp2Ngh8b93p5rnHVz--dfFvmoob3lOKw3VwC076eG0BSN-TUU9OMUNA7EfIkcKDepiKcT7CVvTUs7JpXppJgvQ_EczHNDRENYEM6VwXXQch2fFnMbyLV-N02bUjWcyqWKdtTXsn5wItdM0ZKlQ1m7PzWmMiBFfdOZEPsq23DhyqWzfDEFnMU9zilDyf7G5GSX4wHn5VFoTdhlEiZm7-103qITwdX9xbV0_1dkXawWmcniEk5iKM1IGP7kWStoeq8KFXR6_mmHN1KchRTx7xwAPTLdhMsh6bBbTiKCgm2lR4AATbFfl2yMfYLlGKiaNuu6D6WCphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/24164" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=jASTI8FApPvTDYxNSsgtPiJKnIQWOVzTNJ6S6f6Mk6GwkX4Biel3aO0twCVHfYnCZVdzjfVsQpwdztIqMNQ3VUMYx75x-GAQ76WnifopAwUwctDj9UgHABQIHZwvFhVJSHX-Q3M0o3D-eyEajPiVbuxKBIc-sbcne2hQVo_OHy1YY08C0jLWN9brrgHAWyP9m6wcKyEYixlqa_dTMP4lr6fTq5JhAHuJxSoaR2pCopLpKKyv278Sv8o9_LaswZ3Q45pO44cOhnaILN9bjUvxoSrkMf4jiJ9TmSaJr6zpP9eQtAlFupX8vBMQb3Kglt3bE95n5roZDCy93slS-oJLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=jASTI8FApPvTDYxNSsgtPiJKnIQWOVzTNJ6S6f6Mk6GwkX4Biel3aO0twCVHfYnCZVdzjfVsQpwdztIqMNQ3VUMYx75x-GAQ76WnifopAwUwctDj9UgHABQIHZwvFhVJSHX-Q3M0o3D-eyEajPiVbuxKBIc-sbcne2hQVo_OHy1YY08C0jLWN9brrgHAWyP9m6wcKyEYixlqa_dTMP4lr6fTq5JhAHuJxSoaR2pCopLpKKyv278Sv8o9_LaswZ3Q45pO44cOhnaILN9bjUvxoSrkMf4jiJ9TmSaJr6zpP9eQtAlFupX8vBMQb3Kglt3bE95n5roZDCy93slS-oJLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4DDaN1wdOiA-Kiu4GQv6nJ4d8OuowsIpduPgmvIpfXf7uUa8sJpf_Y0QWzBtnP2xgYZKHOUg8hmIAyF1X0SeWlbBXRCFwx1CKAX_RSDOtOZW0ifo-FhM3pdzGG_9MWCGmoDYp4COb5qfwPScUMk5_b6aqQeJ2EwfJf67nmuxg3BmVbNBtYByQclupNqx2toz9ZjWBTc-XuV5yknVcQhjlUAhGvXfTLTG6603wwdaX8adjmcdSK--YTDmWWgluBueobrGVyfosxsfmsqX5MCohSFgk2jPfCVzydkJWNGiAcphmunmvJbbmIv7YEG0FsKW8bj435H0zOjfFUCJCs6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A99sybUhim6GssUmN9vlZr7W0IitVolySeDiWP9a64tNrIJiW5q7VCZDcC7XzWPxAm93XoYjL9BJXufgDUOY7xMoh7E53K0wRnlTy4Jh6P6GFTCBbjmWii6nuhoyICLn-7yNxLWlEeBYOktFgN2XIP_tKVCx6i6AG602NHsReqdzSfkSARrTJc7EBB8B8iXZeVCRel8UWSqZJytfa-7jDesSYW17Wvab-PdbngDPBIrmbKoaRvE-P--NhIK_sb7zkxFrLsHajHvPfkot5e7uFAA1lkL8C88RnG4abxRfKbGmS3Zz2HrxsrlZU7WXlQqEH_qoI0rP-owmT1Rar6plJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE-eYuyTSyKSO1UxKdcDolsGCoR_LEwXJj94prPg_7E5fTjzkTOLuYj1bWfrT3fkK45G1NB1RwGJ6Qa9xOf2rt6LccBScngUi1vujxLPh1vy8Hv1NChzvvVDBpX4cLiZ2k2m6gG2wTZs0v9LfpRHfMTQoZ9XMP9xtjatusRQZ8zUX8KcyH4yIYIPD4sjAJCg-Zn40UqI3v6h0sFMVrPO14PdMa-N-bOSD6LKL2LBX5v28TM-q2B--vy9680Mrn6NlDV7CHZrkco7X5dwTjhWuawKOcrXtlFbNj8Z3vdaLcCCPFUR_KpWOeiCX62INFJxqFvqgjVAZR6v_yzXH6Q2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ8NVDecq1riAmI5S5tNfUVp9A4gWuqFDQltSY2aGC6oUgMpbmjncJ-qO0jKwCzID4tyQJfI8hGYeqIoP6D7mmKaPizs3xiNpPPt7Pr9mbyWL9CQQbK-EA5n09voB1AAHBw7u5ZbEAD3-WPdYscYDF6KYn_aCY7ZBGm5f9DChF05FUP2sXq6O0E2f7j9anM9HJedWPrBeZWhobSw1EVOJyZQbZvuJCVUqnMTRqwCVLav1F59kkbUUXsL6IH7-aDKUr1PNgFvV5zh348CKYm2XQBna1rUng_VkgaHPF-79A7qg4LloRPQE4mtdvQlAPm4m6gJWBWqMxLP64nw8vweJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuQerpssYYINMYVgDlhWs_KE0U1PJqbtCSrHb_LRnHM6-ETyHcEXbKXP8YMVQ2KZNMyARCa_RhFBg4vpcAE_qIuWTaJnKP3fFcpBxaKvBKJHc_Zb2lEh6-VZ9g0Xnm70OE9Sg--odKs_opQZCJHOszlgqHhQ5SgiSWV8QQ20KDbkcV4CKlD0dmG_RUQeJkbjJatcZf-GhsaRbddWvplklc4xzXYMH0tBm7mPWNkGJ2Ugajv0bh7uPuZrmq3Ib7NhVK_GWIViQFHN9a1zMCYZHguY4UsngOeROwKLPEnvoVTZkuxjDgJQc7EsJ4TMlAgBpyBsBiHtu4bzXBw6tdWsdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gp4HzEQ5CKneBxPzY0NB9FHa7gPJ34W_LwwkVNKC-xRzGMQomPwWE8Hv0W04bFgjwxHzJ-JfzN1SHp8MiOk80ORVEU06M6110GXfOfK-TIhl8M3Yj1o-qjWe5wBf4amLa7dfJ9xPsq5kLuzu9MwBxGeGUwVweWMcA5043XN7VxV7ntZOgiqCUJG04C5W0F8PFKkjnGqG_5urpTRaJ55KhgmF7lL9bDsZGXn0YqNiOvyk3tD4P-_PZUJzfX5kpjqZpCBN7EbMBGdZDTcsHwmtYUKtxg606RYD5LSwbZo114wYElVo0BNws9YI8lQTyrwoGWU9Pr_mN5k9ydHF2-LUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EA3JZbOFDe50rqHbunqPuIQqpDYu_P8Y8deaQe2hl9ud-ob9ZiRC8DypfqiwJCpb5L7Lj9Awp-PjoiCCDwRJSaBpyJCH59gQaULiYwxX4HshhWqzxd5aTBnySGv3VrdHD7ygEvE6xbS2YSsZYV27R45YVK2hi_hvDGFCsUmhpSjgzEXbF8OHsChzknAe94L3XRa738HENVFrCJ9Vzb5zRkHAVaVzTRaR4q7wVnTfkzTU7amaEQh3dQIKQ0_Vn-dqjY9v71qFeOR_2kZORNf7hpMEJXjt1PR-Qp4YCyYMTlK6ADzeHTfahpc1PKud81mQZEuc6oY3pCyqNFa58w9y3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p94E9RXa7sWWEwVB0DECrPVmdCegA43fXRx6FOe_gKpNR3nl5Q7Zt1XYaGXgyzzRz5k3e8afYTW51YALkmRUYTsm2o3Pp82tUAsKFxz_J_gYmZlYdQczGJ5K6lZpwaUSsvJT049C_m0WkjBVppm7v5spWNXu03HyhQLhz1R1SxdbGmFOy0lpErMtEOT9kGFKLU4JZUY-kk2Tm3IGhLePaigr0uZf02Ucu361--k5wHAFHPPEN4YjE1vdyk_PWRaqSRh6Z3H742ZzQFBrK58ldgVsHwjMG5PlU9cU3ZhgTUnB_Mr7d9XLbuW-8PZ2lfpNDT9uldxyMxVv7shbRw40xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=daDlQ-Bwohrakz53sArQkuw9qgAWMiv3YOyfoUFBP_QJ8BWPaNv5Orr_mhxm4gLVUoNYKfORu0RAwsJeBOQRcszIQBfABKY1bhIKvpmH55ydKOP4lMH7U1yyO3fF0KdSKbZ1pt9xBNB8UlzXcJUfp0bXe2Y6-eay-StMWYns45VXDPvUWEisbPh2CVTgBgmUB3t3c3kOc4MgTj_mDCHU8tuhZbymUcAW_iOUbGf6H2F0SzoxHhoHR8sBHX05ZG0aoVkx6zJlKLnoRSsyombQ0go4cN56gnsq60h8cF39S-2X4pEah2EPn5g0RoQCPmhs3rU15YtPKG3L53mYoPX5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=daDlQ-Bwohrakz53sArQkuw9qgAWMiv3YOyfoUFBP_QJ8BWPaNv5Orr_mhxm4gLVUoNYKfORu0RAwsJeBOQRcszIQBfABKY1bhIKvpmH55ydKOP4lMH7U1yyO3fF0KdSKbZ1pt9xBNB8UlzXcJUfp0bXe2Y6-eay-StMWYns45VXDPvUWEisbPh2CVTgBgmUB3t3c3kOc4MgTj_mDCHU8tuhZbymUcAW_iOUbGf6H2F0SzoxHhoHR8sBHX05ZG0aoVkx6zJlKLnoRSsyombQ0go4cN56gnsq60h8cF39S-2X4pEah2EPn5g0RoQCPmhs3rU15YtPKG3L53mYoPX5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24153">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔵
👤
باشگاه استقلال به نماینده رضا غندی پور اعلام‌کرده درصورتیکه‌این‌بازیکن‌حاضر باشه که قرار دادی 5 ساله با رقم‌بند‌فسخ چهار میلیون یورویی در قراردادش ذکر کنه حاضر است که پول رضایت نامه دومیلیون‌یورویی او رو به‌شباب‌الاهلی پرداخت کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24153" target="_blank">📅 21:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WenGE_zY5OIr2Bb-j-r7Nvle_7LFDr1xUI70BQtISooLAkH6D1L7Y6G1b6eDwlw4Dtu2rIUb6YmGUsm5cWFGrRxE_-ieeTXL8HRFEZvXyT-8cst9BoIprYUBSeRN8fHcP37T0KQZimWRxjhvnPCotEzMiW6yZlVrzJtwOio6mZHLTnsUdDtR6Qc4VIz8uo-RVOMG0EYE1zWGZp2gqVAllKHj6mba5S487L0IDTZeE6-bBRtu5W_uY3ozGRfXYi7ZNGfWIGQhl3qqwpRzJqf1qkW6yJ0ON-amK39RVIycPagQXqjoYrJt7fH04pSz_Uxpf-1hin7yB4ahNyVodVqTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=u1K_E4OA40emKzlx69XfrIUGpS_X2K48cq-o716WwrwLTIAfaGjz6wRuYqTZoraOQXtzuRPAK4uQW25GQi_QPeTRXhNvx3SpnwDW2CfUjrtE6iAThO3Y9AMDltW7c8MlAW3wO0xWF-srWTs3rPkaiTiogFQaudau2-KwgUFv43vqmQf2iS5NtI4JagVhYEzO0pTSmrER8fgmS92KsFN_uLlYyCNhzvtYRN23jv2XPFK0Qoe-szWzFdRfOr-VNvpL1V66tOd-bWnvqksysBtrGudA2i0jr_gClrrGWoGRqX1FsCuRApq3dfMnpyJNjFoRqVXzmR-y7RH5uv4YfUg6vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=u1K_E4OA40emKzlx69XfrIUGpS_X2K48cq-o716WwrwLTIAfaGjz6wRuYqTZoraOQXtzuRPAK4uQW25GQi_QPeTRXhNvx3SpnwDW2CfUjrtE6iAThO3Y9AMDltW7c8MlAW3wO0xWF-srWTs3rPkaiTiogFQaudau2-KwgUFv43vqmQf2iS5NtI4JagVhYEzO0pTSmrER8fgmS92KsFN_uLlYyCNhzvtYRN23jv2XPFK0Qoe-szWzFdRfOr-VNvpL1V66tOd-bWnvqksysBtrGudA2i0jr_gClrrGWoGRqX1FsCuRApq3dfMnpyJNjFoRqVXzmR-y7RH5uv4YfUg6vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=KY2EL0mP44PGXb3JwIaGIdhX1q4jooXeSfsq2P7RhlzB-OrbSZ9FDBhEwrBnJbEDju6f_atkCDW4wzc1txYqYT48xJxhFn5RhAha0LW-tCmZ34A0cy_TJ9hsB3JFWtbFQ7vzkBXqJ7ZuQqXsBRiwskwsaX2wRbaddb8dIwwfMjKtzucdxNXgjzRoVRdEjVEaVmikKt2OBSXK-Rs-W4DKeQpCVP9XjH4InwKwafmdSwJoSP1_rbeNdUbKZnRw7D_WS1_i3_BbwsP_oaRG-E4eGTNO6E014BRntY0Tf81B4EGKeAa5RxZ6ROwCUyRTAMgKBJBB78A81EehyTax9-ynBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=KY2EL0mP44PGXb3JwIaGIdhX1q4jooXeSfsq2P7RhlzB-OrbSZ9FDBhEwrBnJbEDju6f_atkCDW4wzc1txYqYT48xJxhFn5RhAha0LW-tCmZ34A0cy_TJ9hsB3JFWtbFQ7vzkBXqJ7ZuQqXsBRiwskwsaX2wRbaddb8dIwwfMjKtzucdxNXgjzRoVRdEjVEaVmikKt2OBSXK-Rs-W4DKeQpCVP9XjH4InwKwafmdSwJoSP1_rbeNdUbKZnRw7D_WS1_i3_BbwsP_oaRG-E4eGTNO6E014BRntY0Tf81B4EGKeAa5RxZ6ROwCUyRTAMgKBJBB78A81EehyTax9-ynBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=kE6T1TCdRI4Caeh893kxFFtFJBjfLgpivBllwR183Q_UkNhI-tax0geWIn1WZyNBdo3pM8IzOOpYydbbztrrD5OZ-OC79SSiOTzkcWLb7hEW_JiwPBnc1zBMlIDhDHYdKUVgtVTFWtcrnTgaq84s4auuEri2M_WYnHaYhU96NHE8uZlRoNTFQOkFqeXBYyIVncI2muLlxNY4cZPcO3ytHboWplyKT05idlQbQeSLc7-d1DPdfXHR8o3t32Ma-2EwgiaCfFUt2zHZfDo0J3oVyY01xgJJ9_-klfJTEac-DdpcYiBqzgQd-QZGQQu-hX0UOHFDkr3yjbeuFoQwtljNOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=kE6T1TCdRI4Caeh893kxFFtFJBjfLgpivBllwR183Q_UkNhI-tax0geWIn1WZyNBdo3pM8IzOOpYydbbztrrD5OZ-OC79SSiOTzkcWLb7hEW_JiwPBnc1zBMlIDhDHYdKUVgtVTFWtcrnTgaq84s4auuEri2M_WYnHaYhU96NHE8uZlRoNTFQOkFqeXBYyIVncI2muLlxNY4cZPcO3ytHboWplyKT05idlQbQeSLc7-d1DPdfXHR8o3t32Ma-2EwgiaCfFUt2zHZfDo0J3oVyY01xgJJ9_-klfJTEac-DdpcYiBqzgQd-QZGQQu-hX0UOHFDkr3yjbeuFoQwtljNOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24148" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJozQrNpsiGsghSDrZZlHS-0bHBdWTzV1nEyqBhbzwuqyJFiVYRa550gTn6UemdbNJxkCeAf_mqRrGqED3tUFL8qCSRnZHm9LPt21CMHA1K6uxYK5kneN-5m8qCliP_PnhteO4z22eFYpuj0zVe4zJYpuBzyUD6R3CD-2_HqsGDb2DQOOeoN4ApJXubDfJpLZbBGUZYHkgvVZ-xW5HT74G54Eb9p9W8_a38uEWXHuOgq5293s_h27PX0IUKzbPdEI5DzBMYA1cVLH8V8HIzXh5m6VolN17GoT3DrOjmH7l3kWkgqiIRH0A89tz-GtREJZstmor8FYuiMEuNBKQZ57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIjM4Uveb9tBCy6PjkqCbNNGeUzREpKrWJcb0WM8CgF2hT2_NLoL0VIbpl0MKVXuEKtvvRxD-uITmoK2ni6oUUrpDGYjQldr5uaimq69ngyShAsHcDUiRlvCDt3v3phlfkdQMQXm5GBUrD5jfKmIUXp0-ceMqFFy036aM4jzScPTrxg50hOvm0I-sZ2CIRWdH0_1JWSdSFHrS5LZs0e_GL_9-i95KqAcR3J-Wmwc_untOE3de8_H5cRwq0c8Hy_951XtlUoiBGKMqFJ3B2mKQ3Li02kCbl8dppilpCLU_aKe738NhH5B_CtDq9J0lL4kTUxtUe_6kBngfiQp3Ur7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس دقایقی پیش نویس قرارداد رو رسما برای دراگان اسکوچیچ ارسال‌کرد تا باامضای آن اسکوچیچ باعقد قرار دادی دو ساله سرمربی سرخپوشان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24146" target="_blank">📅 20:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqSoPcLz2lVq5kxJRlJZXS4OauAwOtn8IxsfcfE8Wq9Xd_vxKRtUl2rN0V9NMsD5iOaf-5yaK-pSsEwIQ5orujlidskYqn_CQJ5sK5aObRzEHXgQKcOPEGVfhS07SeX0odMbsTrQyL7kJkA6x1u_ciFRr9Vw3FCF9IpatXprToZvbCeSgMGkvq9tIU3UqLedKvc3hw41CMt8H7tSumYQZz-lWDkq4DlPNoELpU7lPQtTkMYG7E0aZTPvJ56AjHaK_dNp3uDZvB3RGz-FHJrNkNzDLEVM6JuZmj7PoUe3o9T_MST0WJRmvDbYw4twdllE0zGwk4PXKuEky97oJ6OKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا؛ باشگاه استقلال امروز باارسال‌نامه‌ای به باشگاه شباب الاهلی امارات خواستار جذب قطعی رضا غندی پور شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24145" target="_blank">📅 19:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHWJIBigvt-IVyPLESTWgM7NI2OILMXhS21VVigMwDkaPQb8KU9XXgtAvlQAsX3522CebS-FEobUXvHy3J50a_F7lwuvOyILSP4lMZ7RG41yvgt-CYtsuwSkiorfDXQkYZ5OcUQahfxa1SLcARKvBsVOau38JGdBrsgk2qgqLimumSYkUPU4xUSjd__gBcS7153h_FMwCY1E0nYLPh0_Kff8Wcv88dHLd6uQ_jpkvPxHq1MjeOkKio-A3T5-1DKx56fSlqNBphoNq51ApNiOk_pe9yD7Yby5ZCbNljbKw_e2BsLYgBdtlMN1lQzZJcEimfcUs2BgaYwJNEBRKN35Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDN5R9Xqa_wrbhfW2yUqm8CYGZCik_eRt25zhBnEdN7wdt573cdgJOpRo5KENopt6GlcYGYyZIn2QO2GXGPmEgmw8p1yTyUh8izPLlX7JKKB5A0kD3VCm-SzZG5bLHaeJvp-Qz__qVejUFAcVAkFKIwSjLV5kPjQSkGB1DVrpnNN7u4rdfuyGX0LuO3bmjzbpCO4143vWY_b1idy2Yvp0eJBOakhqLTXl8zgGcFlW_SC20wGsZpMVCcivZxTYTMwEeVCaa8UgG9wuFdsRf2ECWCBi5LP0RxXZR2sXBwBQAVxtuTlsKOGpbOVjonmRjwnT6SdUWEqC_wTLHSKfAbKVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24143" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igXZWKkWf-ZQFpEtLVqNc7BEyhCmWDDaT6B51ZgB8MupoeO2NjhcyOaBjunpZ-Y1dALEjCSz8_TA0STzVgPxuMPkFyVY4XVHs8vGQSB4c1W8YeSticZvd7jaXP9gxb-0c4t6-A8yDvhWaRMkBf0WcrMkkWws4yljxpbh6AqCyZr1E_G7TqbNvmwyURsZCDRTOFO21OsmWNardWusV7FE-iK5xnlBhAiggeJyXTr5S6EgHOR6NcMTA9G_YJxsANVEGzF4DvgX-P2NkMn6YhzScArJGrnNx8J7nH2yrrOUrEwDUe-JA69DzBfJONzSKLO8fsivXRffPOsL3b_59aREUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24142" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24141">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7QhlqRzAtRZ0JQObi4_LoFRuOENr1A2VywLddvfj0Z3bV6rHSrea3TpCY8akF2se9MKXOu63NwjeE4yLKhLIiWdoy9i3t_Mdiqb6Y0UKt6I12WpsLaYif831-eNSskiSj8YJDlV3XwbN-EQIzxJBRt39vrUuusEBJR46JG-77rX_WOBhodXvwF90WUtBA1iHMWT2QkscSghP01DniY_6xbg_gVH6aDx0wUtsyUhiVvrNcBHI9z5e_yjN1jW2Xck6QDyJyBiF2row88ZWi7jblhjl_kKEgepGQ2X1xGy0iEhqDmxD_9QSrWJOgPPY4bj-d3ObTkBN5lGbjxqHScfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
برای اولین بار در ایران
🇮🇷
تا
0️⃣
0️⃣
1️⃣
🔣
سود اضافه روی شرط‌های ترکیبی
🤩
ده تا بازی میکس کن، سودت رو
2️⃣
برابر کن
فقط کافیه بازی‌های موردنظرت رو توی یک میکس قرار بدی. هرچی تعداد انتخاب‌هات بیشتر باشه، درصد بیشتری به سود بردت
اضافه میشه
🛍
🆗
تا
0️⃣
3️⃣
🔣
سود بیشتر با 3
انتخاب
🆗
تا
0️⃣
5️⃣
🔣
سود بیشتر با 9 انتخاب
🆗
تا
0️⃣
0️⃣
1️⃣
🔣
سود بیشتر با 10 انتخاب
همون برد، پول بیشتر!
میکس حرفه‌ای بچین و از ACCA Boost
نهایت استفاده رو ببر
💵
💵
📺
تلویزیون لایو برای پوشش بازی ها
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
🎰
همین الان وارد شو و اولین شرط ترکیبی‌ت رو بساز
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eG2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24141" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=gEpxd2AwEoNi1GcYh0HDDj1Q2j20pg2DoETfAOPH5M8i3VVH3ORYgAjbl1Gj-uKxoZ5b5zoc37jBXrNrz9ZvUU80iu73RDJfUzVef9DmM5euWpV-tR_Gmb3sr9qi47Mu3bwhZQLt5RptdA1GzRRZnLKlTH6XAyV0NMLPIQp6TCeuHjaguBrQfBOE5w6Pi7hUlwXVr8HWMqeLNSqA9_j9L5KJ1PIVq0mGzIUcUKlUzEDndOma69844grMDICJh5FnhO_D_zi1B8yIrEypWJv0o_PLbtKEGSCgzIUiBxK-wW_vZW2ppaAGDQYNKQMueHqkE_E-Z4hiF1h595la53eDNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=gEpxd2AwEoNi1GcYh0HDDj1Q2j20pg2DoETfAOPH5M8i3VVH3ORYgAjbl1Gj-uKxoZ5b5zoc37jBXrNrz9ZvUU80iu73RDJfUzVef9DmM5euWpV-tR_Gmb3sr9qi47Mu3bwhZQLt5RptdA1GzRRZnLKlTH6XAyV0NMLPIQp6TCeuHjaguBrQfBOE5w6Pi7hUlwXVr8HWMqeLNSqA9_j9L5KJ1PIVq0mGzIUcUKlUzEDndOma69844grMDICJh5FnhO_D_zi1B8yIrEypWJv0o_PLbtKEGSCgzIUiBxK-wW_vZW2ppaAGDQYNKQMueHqkE_E-Z4hiF1h595la53eDNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه ابوطالب حسینی به مجری شبکه افق که به مهمون‌هاش کفن‌هدیه‌میداد؛ فقط خنده پشت صحنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24140" target="_blank">📅 19:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbB5R3lGhMRAXYu_h8xXK3FwT6QkB7rJyvluAz03eGsQwHHH0DX03WXuRB9TutQJKYQ7gvcY9_i4qcGrekY2DNq3WGUniB3URYVVm-FAlRCiyHLS7-6I9CFi0N_rfw6kdqAlIyKMQhm7mR06qvAwInptIXBjJo8eOEXpS4_ACgwegTSNMaWMN_eu1RbHKjWCMPvpI8QLhqTm7HGtiXhhkSj8nJlkhGk_CM7ypH559DMuluLq6ElUUvtZYSI4mL1vtm06_Vn0zcvEqxQMTgqU6WmlrIM50rzzIy3iw205p-F0nvI7xmziadwQ8v9L87rhLw_0HS-CdEfeN_79OGvMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24139" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbZ8K5tW--s5Bxl6AiXVPemsQYLkE2k70M4ylOatFGyPjzCGlMvZ1OaLFlkSOuKjPKGixYBE_m47IkpmpH2DMuZETdvQ1Z5HGKwo4Op6jGjDXI2YElAomDPi2_mtW5Mtp0s7FseZwcGBuvxxeayy8jv2ugIpCu-mUNygObSXDpQ_orlAXJKKvGVuLGI1_AVdxyBh4xxAR-pg4YjrRgkn7hn-EA8_UMEPIYle5fIQ0287aAOcLHBdFvqYrkRMJ105iZAdukmeABYOcmB6H-W4uHqqW0kjcbP-_aTybjZ2m3BTZMrqSVfbmztwEKY5w24ei3voy5mht9keEzwPTs8siA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
بازیکنان‌تیم‌ملی آرژانتین اینجوری از گلزنی لیونل مسی خوشحالی وذوق‌میکنه. از اونور کریس رونالدو گیر یه عده‌آدم اسکل و احمق و تازه به دوران رسیده مثل ژائو نوس افتاده. وقتی رونالدو داشت تو رئال و منچستر آقایی میکرد تو دهنت‌ بوی شیر میداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24138" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afdhj8GrZj-9h-jmMqyU04GDRhJV99ASnaXXmjAEDquV6m7Xf60MkLTTokOYlVzLDyBoya3iser0h2wz0JE5zviznoV9XLFceAK7scZoKJ8fk1Wz_TIaW2rA24KMJMEAdLPY-A0iG8eb-R8JZuN1VyYkp5s9bTeN5t_U4bpS3G2BwyTlyGFG84uEawDV5Ym0NbO_XjT3N3beb8G8J1u8fPuYiqB7ERP9_P-bLGbi0ZFmwT-FOFYJGTO1knj8y9d3JVx2Ky33oJ1jDq9UqDRF8iftmwyiURx5nFWnyHIzQYCuCuO2yBHb3Vb7u4j5blcxD3WWi9jitDYYIcJIu60YDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYapBwbC72LduglbPry_IxThx3pkAFx2FOJbPt7-32f8EUWMw19UOQthkI3iWGsab6qcS_vmm5e4wUs10agv1zvPtMaS6AZmeFjVBVWBVRPB4D-C77zIARHEhW4IdNOwz2pANUJz_KXeZDpLzz6qxME9GmUPFf5U4zHtJjo0ds-QIhruPwsyUU_D33Ci4mDDZZqUBA6kV39OdiCM-ZcANkkdqP6krcHywCBtHNHisI6o7yN54uqze7no6PIcccVKUYSLe55-wAkMjRbGfKAPizsjVCLhRhnFKCIV5ACbR8Q4DQ5NwnRVSyJbblohPnYdC4hdwWAgovT6-wzWl39d5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcfdlGu2kt3QIdXlywVCVq8ldaj_JzTguQlxZ6eY1Z_eAdNV_v9Z862hVDebzFXmTqGdOYrvU16OYLAWd-fodxNrc8-Qa_KXkbFd5OtCfSuNXlWguGhAaBIL3XSrdjBhTsFbQWdTDA9xKVj2Gfft_2BZ-Nmh-l2Miw-1QyqSJjv3zS1D_hGxmRIyr7esb7tVNDTOu0nY8TfC3qVBRkd2BlgHlr4RIR-i2DeNo3EwscuqO8G64LyWloNi4np9eEJeseehSAcP1D2t0_5bM5_WoTWO7E1RgLwXLacn4JTUH60hWCTxBaWi_GMrjMUQpAYHtLGLzt55d9ZI-4zgAX3XJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubtvKZVkFGNe7BUr8BFm6ZPfjo_QRHzZAJ1X-No-nwl8LfXtZk5HOylLsRs3rFBLoH563mNj2I2AEaDKCy1S42GkyGb3HbI0mUeraooHWbbWUoVNG67Ng86o2s5QFKNs25hvV6Wgn-tQBAIbIDh9QTLbw_f6J2H7KW2aSssbojz9waM1_mG8VmWnN8IRK10YFYfJ4-Fi8i6YpP3A2Se15p8m47n_Ga7GFZuEk1RwBSpSMRVRzQftX4KokjZtxjgB0ZYj8hQ72_a-V3v2yenj6dIwSP4o1n908qtnpj_fKfBvuYLg8s6joLIwT6dLyS8LsjUawN_WlQG-vdHfMCfU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=omk-HpOe3w3LQoQsYmSE8JM2slRoD8Kq-rGSn1eU6ovd8EYc4hKfxUzyXJTP0u6iU_3zCr8n57pxtOsTTXuSO8X14K-kJdk4Hl-4L9qoZtJP9dHRyWTZvRsxg89v9p9uASeF7eYlQWOtFtbOYd_6V8fJIuwXh2Ev0iA0m6UIEfbQ1MLc1N4rrNqGEaqxYw4e1Kci_ckMht4RDeRSkjOe2yvV2Qlkk8PIX4kwlBysncgHhUydQ0XsX1gmd9olE21EUf0KYmT8jiRZWbxLr1AbOo4JSKT5tOPZ06f6DFee1qa6v1REWYucAJqKsgtwkwUZ2VjrSL2jQMAnv4l1mK1qTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=omk-HpOe3w3LQoQsYmSE8JM2slRoD8Kq-rGSn1eU6ovd8EYc4hKfxUzyXJTP0u6iU_3zCr8n57pxtOsTTXuSO8X14K-kJdk4Hl-4L9qoZtJP9dHRyWTZvRsxg89v9p9uASeF7eYlQWOtFtbOYd_6V8fJIuwXh2Ev0iA0m6UIEfbQ1MLc1N4rrNqGEaqxYw4e1Kci_ckMht4RDeRSkjOe2yvV2Qlkk8PIX4kwlBysncgHhUydQ0XsX1gmd9olE21EUf0KYmT8jiRZWbxLr1AbOo4JSKT5tOPZ06f6DFee1qa6v1REWYucAJqKsgtwkwUZ2VjrSL2jQMAnv4l1mK1qTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
زلاتان‌درخصوص‌لئومسی:
من تو دو تا جام جهانی هیچ گلی نزدم ولی مسی تو دو بازی پنج گل زده! براش‌خوشحالم‌امیدوارم همینجوری‌ادامه بده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24131" target="_blank">📅 15:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_l07spVsbW-Dwfpfi3d2VNxxi8PIicTntSwK8TkPrMhXWuXHQurgrWSMh7qejCKKyG6xXsxBweQ6pw_YDP7ZvTGQEMK-0XFH4sdU7KPbfeK7dE9v_flOhEq4_93FFOcCj3epT0SiAHtlMKTr9OfUNEaBume6KCx2FUYUnJFZPv9YILSjyAqsT4sPiuktQEOrdXZfBx0oCo0FMcEEXiCHOHrGky7YLKqI1or8uhQ7FFuvSPmctSBWvTjKqOyUkR6PGFIj0esvpJ6EjK10T4YyysPFRebySQ9O5JEfbDnp8YJqvY7EfoNuc2wNu8tu-CripVCbR0mQBq1NO642IOxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
فرمانده روبرتو پیاتزا درتمرینات تیم‌ملی والیبال باقدرت هدف گیری 100000 از 10؛ عالیه ببیتید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24130" target="_blank">📅 14:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyOGx3VXZXgSPfAUjp2aFT6T69yDEqrDvHxiOY06SuxTLcp1v3HhOfC-V2QeV2WHSEDAycoJ0YzyVIPDymKOJMLrLda4OUi53tA8faBCLRRT06ilIb6GxfbwrbcyM1GeE11KJUrYL7sYuOvxzcRPr0fUfAQdA7_0rCzjbJag_H42jCuJeEZtJSSQNM3uO_0J4olBqihGwkuhHuvnpNFTf3I0W2Xm7h0rCU44pLp4wIY8z3YsQ_XfXXGZgTWONP8xYsJKCMja9kpqluZubnQcSP4ohylmx-Jjk06xVi0TcQjdXD6WWYMH0F7A5q0t8_YVmr59sDlJNDN9okBULno_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24129" target="_blank">📅 14:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMz-azbY_UKA8YaXap4LuzpDlyx2RtZz-AQ3WyT5v1fk7JMI1cyRBdcns76rACHXnoh6jPSEZyWNO9W9FkLoD9ntkpEAFzT6swZUVo-Z6lAEXKvu1B7KGUfFWBsGNN5SAxGkI8u6pSLV5DyaaoN5RihwquIGX2qfwYvysaY5uDlOWtn9JZt5Ccof18SfJZVHxVSyuCQ-ZeXLhOKKd0qTQxlcALl5dQR1cBHVDvluLpDt5zgyIzc5v7em8K6mAm38Xq3ChMimFPfWZUgq_yzNk1ZycXO0mnVdMHTXKp3YuJt7GlyJXBoDRN0RjwrGUaCvReFUBYh8uk0O3VMm_b5hVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24128" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=T2KoUx5dBm1AABnoqBPuvw0UjOV6GacE5Y-LiWdKfaDdH1_7gQPuwXMydZxRwTyiDACseMiZV7eyvmnuzOp3ptiHKzkAyPnYuB925zHWKBeFnEOAM-yZdY7WYTYQsGMbCeHFwgWKY8nM6aRsno64_xA9Lf6x7T0CF4Fl0Dsb8ponaGzS-9fTorIIuT--7zK2b16zK7dfCT1PMFvBp99flgGLzmLS14ZqNZxFHVx9pndHuZUV6Mq4G__Pbbz57HEELUvItPX8vondNTEgzhPl9bj_2O8EZrcgr-PZEkBdcJWlbefXWlzM06udDtNa8kS-Eup6Zi8tlUxakPdtr6NwWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=T2KoUx5dBm1AABnoqBPuvw0UjOV6GacE5Y-LiWdKfaDdH1_7gQPuwXMydZxRwTyiDACseMiZV7eyvmnuzOp3ptiHKzkAyPnYuB925zHWKBeFnEOAM-yZdY7WYTYQsGMbCeHFwgWKY8nM6aRsno64_xA9Lf6x7T0CF4Fl0Dsb8ponaGzS-9fTorIIuT--7zK2b16zK7dfCT1PMFvBp99flgGLzmLS14ZqNZxFHVx9pndHuZUV6Mq4G__Pbbz57HEELUvItPX8vondNTEgzhPl9bj_2O8EZrcgr-PZEkBdcJWlbefXWlzM06udDtNa8kS-Eup6Zi8tlUxakPdtr6NwWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جادوگر غنایی: هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24127" target="_blank">📅 13:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkIELE68VKzP4npGLgxn17CAXUtlxXByiW3k6zi7sYyuRgbr491IXkh0a-r48uno8Fc9VojSXD-F_gtOl2yurgmC5eAy3l6GE2g0vZ137Pc9Qt7nwHIXRjJA_nA1cvpKBwQxc1tt1e_cK6RLrl5S41K4NOd1mg_7t3nj84RJoZ3DnRgsFp4I7LOivaEHj2rc_t1H6DOmC08JYKOkBvJeF7TyAPNbXXW2AwpjU09lFzx4xesj0KSy_Dai24zRf7C-b_QQYaFs8fVvE3AYjMqt-CfjOBbOeOtOW88tJQEs7D6yemcCF2a12kJszIrQUUiNPH27qOmRF57-G_Q1uYsAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سه ستاره جام جهانی 2026 تا اینجای کار؛ رقابت برگ ریزون لیونل مسی 38 ساله با دو فوق ستاره جوان فوتبال جهان این بار در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24126" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi3ZUdtVy8H0Am2Sc7pTt_eDPMT6Gzm3HpurkTaqXpzhk0UGNCQ33rXM9tda8tTMMj5IA-WRhk1TzxG-1kg4OuphyGtR__nKtI3MZ1Q67USg8unDT0R3FVgRI2MhUKHMDpIQhh8-8O-lYgp3spsUu4248MzGBkgD_Fe_N2Rz8qTyMULT6ApxaEIcDntJsDmPfLh2QSOGfvUcv5gWyJPlGrOkVzulqoB32Ll4VugGAlt2Y7XchrTfQIavq7lQ1Yk-uLXcPuEnRIM-pUqV-RivFj34lKcsrTYn0Z9dmMAdMRJl4OBEjeSZh8TR9Uwn_fQQUu-BO2_e57Fw1YgWGkPe6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از خبرنگاران در نشست خبری قبل از بازی انگلیس-غنا از کارلوس کی روش راجب باخت سنگین با ایران به انگلیس درجام جهانی 2026 پرسیده گفته اصلا یادم نمیاد. مطمئنید که من سرمربی اون تیم بودم؟ من یادم نمیاد به انگلیس باخته باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24125" target="_blank">📅 12:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAw9DPrTBiHYx79nmtMnuLQcIQ4j0nkiPJjhdI67iPm4qVLauwuiH6kKLbLl2yB1gjooeIkWkqL1QCkSiYsRN93i-NUxd2mXox91kYWXeOkvaOjJHYzKYvPPf9pYEPNF9vRAxu3uXKwOH2WL6NfWTrDfUL9XDX5uPVkAQoRsitgIW7C_6HGrXkvWUl2HpMDdNnA7YuGiVF2X-iaY40g4G7fPcgOiFc1EzySjIKhFDmVZj8pNw_IeMXGgGAbIotfxzdIgMSnAEiJwy6Kq-JhGGe_EaehEcRb4DnTNkDvaqHk3QfBIyCLRRieJmxzCFcbwLA_r-7S5HZi7gOxEKLMg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24124" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYJHfwDtPPJS0ljUdbehkrkA3aVQx5uN_zvgzjDC1RaaFWDC5VMw9gRpAQcTMQvASzB5HRMNMwJxNGT2RVm3lxrNJY7Li4a-CmKycpuLbaDv4aMlkwILHsGob5CBa9duYEH1G-yWntVTM6xl1qyi_cmOcwpSzTnikg2aN9B4H6Ha4Ft1kD0i0jmUr6ZUberWG4UbuPzzBo0cx9MWRxdg3v3npj7NPJ1Lhw6EA7HmlzJIR4Cz6MeC8Czw60FnxQfCtMd56agJ4L88Peur4Ud0oN8ex-nCnsme-h9Q1sMv7OqqW8Dj_C5Ry8_Nu09wAAJCQIbgG8Wk8RCQuF7zwcuuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24123" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkObh-DVKik2s4SuJ8DBKhcUC-QXWqbqSzQvtavvHPBSbR8wvwVL-CrVtpFMrmk07uaO-T_FAWmpWH7AmRHMNoYCxwpmyL618U2nZbUyfYzo0NCwGA0VN-weQP60JCxzUhHImlKOOLzSoZQ8OoN_p92g8zmQtv0_WaeryyWnkgmVcieS7Iiey-Xbq76b6rNEJy0eedJj_px-2xvaE-pca-06brwv1FyNlQ0lzIpfkGI-gSHn9qEGWjMZJgZF9tGQ8a3JZCI0KH6Zib0F1xvfhZuS-N0T2aolTf8oDRQCAXUisbJw4Q5zXHFAQ1B62jak69Z6bq_n3ZnJKV37DGPRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سه گلزن برتر رقابت‌های جام جهانی 2026؛ ارلینگ‌هالند هم بانروژی‌ها داره غوغا میکنه. دو بازی چهار گل‌زده. اگه هالند درتیم بهتری حضور داشت که اسکوادش بهترمیبود و هردوره درجام‌جهانی حضور میداشت قطعا الان هالند رکورد کلوزه رو زده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24122" target="_blank">📅 11:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDeLUvKsN_f9kLKklc9GQDY5p0TNmzpByrKnpnfK88ubqgcUrL8VN5qhRqfA4FDnxN0IzLImaDhxjk7qr0RmWIDMNqzDuUpGvdpbkbt7NSQs7SNWbWHX1U0A8pX6yEEdbEVHnbwWiS51ONNaWEYASJdPRRnH_3ESz7fBEzA5P36TAcnQkTGbqasOfoKSrv_inrF0BiQgMdi_jp57A8ZV0ouBtln1KS4UhnX0G0deA5zSxY6rQ7Pq8ugJ8gxuBUlwiWxdHWvW2TmxY0uUBWicDLl_kPcy5OM_1QeD1YrEgJxQ93tNAb43LbCZ2ypEGO4XuCYnTkZHhuwF3seJG97xYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24121" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=jX-nUNwDp7UdArcs-6MJFxBoFj5YjZwXpMxyrFil9SEViB802f706oKVKX4236ULrBB_gkSI-hFskcIQH-Gd_njJDvLzFTh2CQjXnHiOoPBg0eBle9axrCJIfZzvaSa7qK_XxDw4x1aXyEsUdAe3U4lMzNmAH5enKZ1teNthbbr3WinGS_7Ih6Vv8FPI0O5rnL062GlM0DasNxX_t11k6opNNaXPjfEZdMY0QakT07XvpW6HBpum3IU5Z7ZbiwP7wCC4JO_YFUA5qbAn10MLR81RXHNPtmqoJ-nrxI7RwPyZNB8fjOAWrxbbOXZy3Oqa3MfMuzbXt6kxOV1XYWNzZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=jX-nUNwDp7UdArcs-6MJFxBoFj5YjZwXpMxyrFil9SEViB802f706oKVKX4236ULrBB_gkSI-hFskcIQH-Gd_njJDvLzFTh2CQjXnHiOoPBg0eBle9axrCJIfZzvaSa7qK_XxDw4x1aXyEsUdAe3U4lMzNmAH5enKZ1teNthbbr3WinGS_7Ih6Vv8FPI0O5rnL062GlM0DasNxX_t11k6opNNaXPjfEZdMY0QakT07XvpW6HBpum3IU5Z7ZbiwP7wCC4JO_YFUA5qbAn10MLR81RXHNPtmqoJ-nrxI7RwPyZNB8fjOAWrxbbOXZy3Oqa3MfMuzbXt6kxOV1XYWNzZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌اونور آب واقعا عجیبن، از دخترای کشور خودمون بدترن؛بدجور روبازیکنای ایران کراش زدند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24120" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24119">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thBxUZ-GVwkh1hzU8UON0ajW_a_RIhuBfIumVqmWol-RAaTstgdW0DNEJgvZoj63D_ewR0hdaH6SEQK3UXn-1ccGt7DRtCji7wjOA1W1hSt7Iz_VUGfohpp3c1plQ5lrCthPu1KQ-GRHezRgg7KAUqfq1N9rpTsDrwBduO37Oucmxrj908-sUGkLG9feTirKffyYGG5h07yuz5Xxe7KbsvWXRbXZl6veu2HYW2sNF1ABbK3JNWUBhOEQ1-IW9znf7SE5B6_tTTYCv0M3OVKkp-yNSTjhzBtaxOjjEI_Y7uz_Sii_gdJpRGcsiqzy0c4MNKKd9c3NszJGIyfYcPIHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eR2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24119" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awxPq7bqzL6xW_6IY_cDwJHeUYJM0MN934FdByOfs1s6os98liq3qG0zE196kwBUidW-2mGH4uUFBXtFIpSdX5tbZzENQnhfJCyaezyCWSArVujaYURVL6Mck9W9nJWhVGrmjsdLoGuWpslUOwODAaNDbK0YyDGpr3vBqHdSiJL3rulNixcnV373uPXDSCm3p5309UdsTn2rYTKNra8PRyCxb7bmisPl6BW7x3lCRsJNCMHXluhnA07b5bQhgiGbxjc4hvtM2S5LJIc9ckfvaO_iDmydrocH9OGU-IqRMZxt4WCT8dhHl2wavKabQRNjXM4cdgTjk8H7pxx7rcIYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛پرسپولیس 5 تیر بمصاف چادرملو میره و برنده اون بازی روز 9 تیر با گل‌گهر مسابقه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24118" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohN4cB3xNIbiuZPV4PQkDnX0Wb4RepbiIFaGdXRInjpyn6BrpDuUzf6L_K2Iv9p03vtCf7fbx_jvlEOOSGg2XHlAHk4TEk_HNwiZbrVpzlmP5DoLYAlB4Ubxu1kWRjkdt5sHhiBpop6LMVXrgZMBjvx_Zztp7DZHrAE9XHytQuyBXhg9EMK1ZgyL9OFrmBNqV9HR_VdE4i8cdefKPze6dodtd0qI0GLgnmpljLUQyXgjac7Sx9ieJyFTlUQkLooBpT8JFwykAZ-nw6Xe1f7dnG5zRei_RRntyENHkLdZKfTEzTgeXEdJkmGjS8__YjK0MqAQvEG32af2zCWHuL6LZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24117" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbn4KrNPGIhW5Bx4Ts2I9rp6bFH9BAc94vzAbURxHB7i4Mx8OE3YskqSkgSmt0Ii8-IUveH1Iq3F_8sfs9eOOTuseNuqKBckTYRiAYA1YDu-fBqNhzTWkpqmlDrzChdhubkju_Q8EpAuKfh4BRNIbTv2mA4QYpbmN-HwVtvnRYTawzA_TAA63rVmAeXmZn4of18l_74riUmgUyPOE8YVxBqPLsEsl2PVgnuMDdMc7u_XK3O6oljR1L5VFYoSM6C5Yqs5oYyahvpi1K07_lHYexwvQ1pWtFKRgdGaJO-Jd8CNZ_HQYLklIb_HQ503tH8wIRyrwN7MrI3OwhUqmSH6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24116" target="_blank">📅 10:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=KsU_TcWRQdk5pamTFT23MLedlcFQTwSCB3ThSfqK4t9g0cohUXuIVClCiEuJbx1OXC99aGDH0aVF63QeLzdS8ltFWfCeYkKuJ1uYJw_PDDTFuM4ZFqNAVuXEIYoFrZ3iWwhUe9v7mGgio7N1RyLWPDQUuEYl4mswFr288NgBu2Me_qXRUo6FYEpUgzt6V8TC9P5BfomdxasWL_66xuLYHMGZw4_2D18RaxQS_p5gC0d9FjESsw68ziKppnAFpjvqt5EPTM-lv6uBQ5N796iTfrGQ_niHCWDHQuPF-K0YPiJhdH5gb3tLWVfOc5A8OyXH_gOlx1Oy4V03tXhVlF9AXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=KsU_TcWRQdk5pamTFT23MLedlcFQTwSCB3ThSfqK4t9g0cohUXuIVClCiEuJbx1OXC99aGDH0aVF63QeLzdS8ltFWfCeYkKuJ1uYJw_PDDTFuM4ZFqNAVuXEIYoFrZ3iWwhUe9v7mGgio7N1RyLWPDQUuEYl4mswFr288NgBu2Me_qXRUo6FYEpUgzt6V8TC9P5BfomdxasWL_66xuLYHMGZw4_2D18RaxQS_p5gC0d9FjESsw68ziKppnAFpjvqt5EPTM-lv6uBQ5N796iTfrGQ_niHCWDHQuPF-K0YPiJhdH5gb3tLWVfOc5A8OyXH_gOlx1Oy4V03tXhVlF9AXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24115" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24113">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=oEDuFwByvhyPnSdRBjspDZnLybK_30p0Wrr1iC6p6wVRbvVlZlN7PrfsBUlu30aZL7JObI-94DuWtjWOb5c7i7ojjjP1O0NNg0pJs3eD0smMU-w9ThRFicmAqlZzuipClssdEUmZ6B4hwSGllgc32TnBGNfLcgTxUSl_A8CuKwv2lceSwGLacEhj6WWND8JXDpwxG-eDANVBXM16vDx6zIvAQLNKDAz738sF2wn_XzXL0PTz9U6WcrBjW_vAwxXx8kfqlbt3jxneDih08hedS2UuTlRlmORx1cgllXoXSSdahwjRQ5aU4d6U0clGmtF815jOCAfitgRyqPDcM2iYuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=oEDuFwByvhyPnSdRBjspDZnLybK_30p0Wrr1iC6p6wVRbvVlZlN7PrfsBUlu30aZL7JObI-94DuWtjWOb5c7i7ojjjP1O0NNg0pJs3eD0smMU-w9ThRFicmAqlZzuipClssdEUmZ6B4hwSGllgc32TnBGNfLcgTxUSl_A8CuKwv2lceSwGLacEhj6WWND8JXDpwxG-eDANVBXM16vDx6zIvAQLNKDAz738sF2wn_XzXL0PTz9U6WcrBjW_vAwxXx8kfqlbt3jxneDih08hedS2UuTlRlmORx1cgllXoXSSdahwjRQ5aU4d6U0clGmtF815jOCAfitgRyqPDcM2iYuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
عادل دیشب باز هم اللهیار صیادمنش مهاجم ایرانی لخ پوزنان لهستان رو به ویژه برنامه اش برای جام جهانی دعودت باز کرد هم به لهجه‌ای گیر داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24113" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24112">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfLvnNUIFH7bcTPPHetBT3xLrBWppO8ngC50ObYHU5NdnZ6g335AdTPNAKxCQUZN33fq-Pnm9lf9G0mG4uL84yzWwmJS0idTq-WoTpQe_A45ZGA_2wKlaK2Fq13TLUXkdbjYQaZP0OoP9uyoadVQ_ObGnlTjKQEyV7660wUrEyFNWKhX_5Ej-a7bk5CrKppKKEt1smbDHWVemj53niJkisi2Yf_9I_VKr7ThnCPOIx2fUYWRtboIZ1TPJ4UWbiQ-lgPHDj7F5bcUrNyNcTAJ_Kd5y7n-TNXU4rKudPv8rmfLw5ojrbNORHCoU4Y4MHGvuoCp-tGySFQ_z-V-bE0HyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24112" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24111">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY2Rd8qs7hUTD_G8jogCJAsmiNoYvqNPNGDFrIWnQPwLSdHBoNoDf86-OATKXpjftZe55i3lf3UeEHISHOo_N6aTx_8fV64sG19mBMZTQpuDJmr0ke3N6nt-uH0-KOeJIzwpNTiq6K8PngLzRUEJBoRSha2TOAVlvdU1W1yb9Irdq4LNLwenJvt8K6DS6YBOVMUDzlDw2KoTwTfBgSXdim76IsdKSyNwQkWg5k88EOpZxVDQIoSO96Qt6PZA1BHscTbx8SzzxRnypqdJm2t9VCYtpjGbpCtsqKLflJGHh8NhVMUT9MCVNzx8QaHcjbG-VtA8kOr0ZF4JBCbPwF3rvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24111" target="_blank">📅 09:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH_0N36gxODM2WYyE54cF8z42hNbC-GvAaS2GEtwDVtJn0J9K-KiR4jXXoLS2XMmd74AYdWF2GJ_liWfoGg2033MGyh-4lk55P7pfNj5tZMiAEOt47lrsNN3u9TLI2M4iW4wJbrcd-0ivbpb0c8vmGUFD52c3iBtgedFDplZjavLAh7MufDWLAzMWGr11OPDgvIzdccQMOfpxyRVbIt4gor-5jfo907zQiVxB98yM-PtBSli7TqlDajaNwCINSps4wNyp44wtCfJqw84727FUIUFX7EQw4Yx64AHaxKzGXU47IoLJBOW074AqCJiqS_oanD1jpw0W2nzn4mZEai4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌برترین‌گلزنان‌تاریح‌رقابت‌های جام جهانی بعد از هتریک لیونل مسی و دبل کیلیان امباپه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24110" target="_blank">📅 06:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24109" target="_blank">📅 06:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkMGWvr-GqI6nItzLzxwtE9cF0SoWvKo8XCUtr08-yfHdOmKi8ZW0uJU9WfXgnxMVNDhZ-4QWxhrUC45zYTBNmfL5gbG9ANT6XSqjjzu0KLXlWm1Wgc1iIYsNuQb7UJZ3PVvgIjMvwCbWWBOiZXGsmdZPZvuECTyApsx_kf1fQXPeSU6j79Wn1JMmbLHCl_3GTzdQ0CMfBtGBGhbuyvOUPcVZgPYRbpzYYugNGNGv8YfTBMOQ_zVEBLBJgQ6FtmERuPhEjBRuAGX9yru0-FnfWOogMENDsHrbGegrhpwl-AKYIoBY_feRWVpEFSAoBW9clttYBdMFV3Y5TNjlKG5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24108" target="_blank">📅 04:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دو تیم عراق
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24107" target="_blank">📅 04:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24105">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwFnUB7j00PR4I2yD-aOZNXjQ1s_Ze9WXIWbr3LuyHTRdKmezak9d8UQ-7yza2rTc1PEw5qEKVOWIqexiT4JOiSQ3KBbt_6GeY8VmFJh2b_AbrgPS7sCwJMjUHh8SdUjflrv5Y9GPnJArwO_0dKxvsZSc6ouZOQHFlglZz1Mb-ywNTBMaIIBq1c0o2Lc0bKlX4hjcjHuUZMegjHS4wvY8fx1lIaonh3TwuZe0zuh6oZl09necy5FWOGMWxjOpw4dR6p-krieibz0hHLF2DvuOjl6KOwPQB1615JuoyjxYdBBIvBxV377OSg4JWE3BG_EjUTGyEqK-r8QhXUkjsMuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رومانو: شماره 9 فصل آینده تیم بارسا به احتمال99درصد خولیان آلوارز خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24105" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24104">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sc6Z0hAHX-aG50-JMZgEBANVZn5hU-y6JBIcUHgqSKn6NHCw6qkR-qEcSwKT-sIBTavRT3qWzBv9RLBOgcxV8ydi0LxKaZJU2IDeVDY_POxOZyoN0RgKVKf-iEkRrxYbo9B8sdZKwgZTzBPfvaE4GDvsalFstROhu8fX0VXk8o8c8OWDGdxf9yGCN8P1pVQhR847cM_xyVozAPkD1_HiSsJ_MrVjrXd-3JTwYezthXlOgS4mZ_4fAroMQ5QQzkBJR_iSf7374m3YxJ9NCf2VQbX79s_E1b_Qx4JGf57mOolboFJ3Vwb_ofiLucmQY-J8ONr0EAsZEmj0IaaGYbwmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیشنهاد تراکتور به مهدی هاشم‌نژاد: 3 فصل 250
🔴
پیشنهاد پرسپولیس به هاشم‌نژاد: 3 فصل 180
‼️
ستاره ملی پوش فصل گذشته تیم تراکتور بزودی تصمیم نهایی خود را برای فصل آینده خواهد گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24104" target="_blank">📅 02:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24103">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsRHbO3G25-OCzI3L9J_3ESulU8-5uCNe4mmJpCL-TW5OPE-JbLkHCAzBkPbMQLemj7QErXQ4IbS5W3JQxJA4DbhCY4OsjJHitHonBLQV4ldNqlwsN2wGB-IEAkg48XzlVOc5b8_iuvcPZmFfKKnTgesIuNq4PTHo0RAOzyhQW--Vxih5-g9gPzRbP_GXeJra_jcS8nLTt_tptKUuxLlLXL_1QmGvZqguwuO0Ay-MhFh3bEZU5oZdtNDTIBm-GiE-E_inExv6MT9WrtHK3BlovS7kJdbHscii94eURaazchXuTxmBeWlpI7Tvm96K4UHazvx2RWSUtKrfdaYMY_WxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی
؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24103" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24102">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=US2IB5tKTtkMv78ZH3FZPBjEPtCGlpDEobL9s3CnvX1lad4TvcCOE0Q8kWyT89LO7WT8gs5vAU-4TiIks-NXp_h_w6j_0gvreglpXa4l7caSjVD87cJuimVmWMeurzj5Du33TwI4Fi9DadThkm0KyhzFDofjVyxdQq1YDA5mB6yLcdUSFwY8yYtmE7vC_aF8WGujd4qlUp5Fg_0oswXE9cR1KLRO4Pu-_DFDeXg5lCHCwFHj1_UbDpbR-GGvI_sUwNU2K6cGkZ8yGm94tq2bcu9OkLa6eixC-QEupj5ppCJwoauw8KKqLJxRml-lN4b6bjmiMat1Es04Kxw5brLItw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=US2IB5tKTtkMv78ZH3FZPBjEPtCGlpDEobL9s3CnvX1lad4TvcCOE0Q8kWyT89LO7WT8gs5vAU-4TiIks-NXp_h_w6j_0gvreglpXa4l7caSjVD87cJuimVmWMeurzj5Du33TwI4Fi9DadThkm0KyhzFDofjVyxdQq1YDA5mB6yLcdUSFwY8yYtmE7vC_aF8WGujd4qlUp5Fg_0oswXE9cR1KLRO4Pu-_DFDeXg5lCHCwFHj1_UbDpbR-GGvI_sUwNU2K6cGkZ8yGm94tq2bcu9OkLa6eixC-QEupj5ppCJwoauw8KKqLJxRml-lN4b6bjmiMat1Es04Kxw5brLItw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمله سنگین زلاتان ایبراهیموویچ در ویژه برنامه جام‌جهانی: من فالوور ندارم، اونا پیروان من هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24102" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24099">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czHnjGNF6fR0lbt0l59_8FdYE7f8OPp-u73cJO8l5-8Jq3R4kKC3Zuib6KGqFhkOBSkfUBx5ZGmznaSfBKc0e7LpcuYUNt-HuGYMIWT9HzniYYBsb7-b-jupTgq17NVZsjZ945RCCgIjngl0wQAZwJJ0OiHrFWuV-D6RjNYqbVC2QjJ1BcxhsjigJYw14rOex6Xp1Zc5FLLHOnzAHVjQwXoF352n7Xn5pNRoreaAPfxqQ2-iJ4ALLQERTaQrUqKjLrHBJ5yP5bD85VNS7rBD6B-AHRTrlXDdFoLrWYEEDazHaRw6ZNxVLGmNhzHZuehUo9XlzWi-zW57rlWLXkGEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد: میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24099" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24097">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8ingsfV_CuKNKCASIK4L6NAqvx5Ui0acIfbuGh0oASUlqWgzquu4s-nOFdZqrz3zOxnztfMQSVxwTb1FBKaFF2kMQpsN6hxGju2z_lDKBeNCtUA7-8gwniOCNV-Pk-ZjzG4rtc5an94kYfX2kq-P2BWS95s_dm-cga_TGTtJe5WBQW7B5MJnOTTT7-AO2M0dNQ91jkM7EBSGKifZOZ3MnNDk_9iSyk4Y15txzEV-bQ8U_4cdeI2icvTx-LuXuhBdkRVv3XKlCnR843rMAK9SgsV_czd7-nL7HD_UoNdevxni1qtpLNb65_uXgYHbvT9qscH_tG3V0ERl5S-g6DOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اگه فردا دراگان اسکوچیچ قرارداد خود را با باشگاه پرسپولیس امضا کند بلافاصله یکی ازستاره‌های خط‌حمله تراکتور رو جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24097" target="_blank">📅 01:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=oYkYNPPWHWHwY5OSRqZN8gtBIgw-G-E0dpdt53L5rw7Vx-0ZVFL_lbCTYLM1stodGs0vCflyfPqZBzbSJa2Rv5pfyMvR4UpdGg_cdJWXG3p6U4ekQGuQXx9Fdy9g_Yt1qEmZJatvqjjh2E3pfC3wf1gRYMVlaoqeIiOy_R5Hh20c5uvme_dZ9mQ9QKo0FKoLTEantybIgjbrif6AVMI9o2a7jSjRnWYpEpqOK-f8C8uUHqEJ8u_HLV1AaTT2xep90LDwur4rNMHVDSIULDhnlEcsDiY-XfDASxWuKUSRc8sdhZ27yqijbfHvWJcWq3PAIuU7vrhZRe299rco-Kua2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=oYkYNPPWHWHwY5OSRqZN8gtBIgw-G-E0dpdt53L5rw7Vx-0ZVFL_lbCTYLM1stodGs0vCflyfPqZBzbSJa2Rv5pfyMvR4UpdGg_cdJWXG3p6U4ekQGuQXx9Fdy9g_Yt1qEmZJatvqjjh2E3pfC3wf1gRYMVlaoqeIiOy_R5Hh20c5uvme_dZ9mQ9QKo0FKoLTEantybIgjbrif6AVMI9o2a7jSjRnWYpEpqOK-f8C8uUHqEJ8u_HLV1AaTT2xep90LDwur4rNMHVDSIULDhnlEcsDiY-XfDASxWuKUSRc8sdhZ27yqijbfHvWJcWq3PAIuU7vrhZRe299rco-Kua2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#فوری
؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد:
میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه و آلوارزبسیار سرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24095" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24094">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=RIDudqzstwGCmaKkjNOUFkQcqgjPxBTwb0pQAlvja2PAXcI1mFvY3XaEJLfkHyIwA-jFTaZJTYfd0EuvWyfZZhUHs-gw_hVNEsoOZPR17N2ZKPG1TtBGndDUi0a2Ym3VF0Gct7tQw6DnlAv3uiaDWQc-m0E5qkPR_SD-rTFbP2hgiIXGs5lmeyfmIvi_VUjqjIrMCqmhb3cWB7MS-TVUsjSuYYXDO81IaZiIunu6IK2jvxMVR2dY-2ObvfO-N278Zau0_X5038zv4OwXoNBWgtLzzCwJ81lkinfYxlhAc3P5KEY1q_nq1eUaes_d9tGtNE3hnCt4aBXC0mIk9PdvNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=RIDudqzstwGCmaKkjNOUFkQcqgjPxBTwb0pQAlvja2PAXcI1mFvY3XaEJLfkHyIwA-jFTaZJTYfd0EuvWyfZZhUHs-gw_hVNEsoOZPR17N2ZKPG1TtBGndDUi0a2Ym3VF0Gct7tQw6DnlAv3uiaDWQc-m0E5qkPR_SD-rTFbP2hgiIXGs5lmeyfmIvi_VUjqjIrMCqmhb3cWB7MS-TVUsjSuYYXDO81IaZiIunu6IK2jvxMVR2dY-2ObvfO-N278Zau0_X5038zv4OwXoNBWgtLzzCwJ81lkinfYxlhAc3P5KEY1q_nq1eUaes_d9tGtNE3hnCt4aBXC0mIk9PdvNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
صحبت‌های لیونل‌مسی کاپیتان تیم ملی آرژانتین در پایان مسابقه امشب مقابل اتریش در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24094" target="_blank">📅 01:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24093">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKcZQ0UVaL6tGOZ5iAcvh7GDXy2oI8h6x6NclD7BKP-QUpola0Y8nvHJ1OWvKNRZdnZme-IdnmoZrINkEPX_0nk3vkoGfWexkkiOWaNAfQQXjXzCrWG_k_7dx8I7HxjG51L512uendHavJz6zBaCCWEn-Ldo74quc3ea8a13QGOChSWWmYFyzJ28c7W-3GjG7aOqoX0izgFg61oyuZgi5UahYV4H3yl917I1CHya3ybTDxjaZrT7d3AbKY4MULMA8HD6_iDPRl9SLSqd8dfOln3SJGxu5E139Y80CKsvK0joLCh-IHxh6RrQaZVKTeWIxjpPnJmuebU-KywGU_mrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف یاران رونالدو مقابل ازبک‌ها تا جدال مجدد کی‌روش و انگلیس در مسابقات پایانی هفته دوم جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24093" target="_blank">📅 00:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24092">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zigf4nicRy4J6XriN44uzHCyDdit03YleO2-EO0AA-nU7sgiB8jy2_WjwLbNEzzS40oPcmMVl9ggNAW_jImUo_Hs5gvHq1SWtuitX_HXg7ciYm6_tdd6s51DMewUEbErpoViUMb531uGXL0DYaANniMscWv0REydNL3zznd4dgoJ37jwHpQpOgnrdLr4TmG1e7cqi2gOyG7EtViibvAi_fbkWrNno6h9nG4UXAPFIesLCHl8h3VKzCwmlyxFP_QrFpd5oj-s-0Kl-qx4sersVSn-zWeeAWp06U-S64lS0twY9AvmxoeLMZXSYphl_kmlRZpLX3AdjsNwTT1DuwNskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از درخشش ادامه‌دار مسی این‌بار برابر اتریش تابرتری‌مصری‌ها با اثرگذاری صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24092" target="_blank">📅 00:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24090">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXIgYLGAsSlEIPcMgoYWaHsNmM-XjKsCgFln-joyXNYeQmiN9yp5KI2F5LEue9ARDyMi6PMdrTT7dZX5vTh3H913TmZATHmggYsiaknElNzwrUAVcU4DQ5e4MhDJMbde2s8NGkpJFpYs3z2aSS4NOE1N_Jkq1fZqimHLKO1M1qIRliOG4grFrSn-nSpKSfmjlOeMi-s0qEgCRGYngnoHjVsJy1TTxzHIX4FwoN1WaVS1c0mePyZV3cwje39TS3GXjPSI13LC92XRdjiJwDzurZQhqVZ1WdD_Wljf02ww_3KQUmeWNgE7k42aCZiSObda2qhz81YITlqWCXE7MLy-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بادرخواست بختیاری‌زاده سرمربی استقلال؛
عارف آقاسی مدافع28 ساله‌آبی‌ها در تیم موندنی شد و حتی به‌مدیریت باشگاه اعلام کرده در پایان پنجره قرارداد او رو به مدت سه فصل دیگر تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24090" target="_blank">📅 00:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24089">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjobh0O1Z65grlWLnkTRljp8PfYbB74PasET52QP5FvwufvWXwC4VWUrszaK4BBEj8R6RAM5y7NDlpCGiqA5gSis7E_St0DUV9xeyXKlUOpr-imn8JQm9OYYbP28kSWG7SCkypJKJyhhyPxqtqhND6dPPaSKuGGqT6Rlfqu2CleWhbp7DjKJQk3MgB3rZBzj8mn2ZO0YFHUoMaUT5bcMlhqbi8YcoDKeZV8BMjkG8wPaQNpQyzdwkQ6qQgHyKmxSnDoBcezMoQQVdjQlDfPtBVATPffHUAOnBx5D7NGhAtWXiBMOanOS1QIe0gnYTF3k8caHgTveMl6L3RhZKUU06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تافرداشب مدیریت باشگاه پرسپولیس تکلیف سرمربی‌ فصل‌پیش‌رو خود رامشخص میکنه یا با اون دوشروط دراگان اسکوچیچ سرمربی‌سابق‌تیم تراکتور کنار میاد و او رو میاره یا با اوسمار ویرا ادامه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24089" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24087">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxelhZMkoPIWgMmO5JV-k0gi-K7aTY66XiqbMTosDBnGu8x-U-6EgxehdYeu90NKBkaOvHGFDb4roKoUGjhDZci5A2qUSTSZdJZ945QPs5vOxKG0LdzyY5C7FKO-Yb29rcnsHgmV8bfxJeW3VKGgpOnyg88UpzRxaXAM0GCVHKKY84AZyryaJlxlwex-XPlj_SmtsS2kikiNgs69vs9u7WC6J5hnt7ZQA_pYZL1mLhZR4Mu5arOGTy8UrgAViQVaoQjd6mMatDqVEHPMnFYzvq-lRO1hqe2jEwNLm9mgQFzN8TjBsZ99YrZYNy0lsm_TvEycVpbd203GZ_YF3CsMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CT4QKYHjrhE0aX0PsCNwig_wF0DZOuk_lGU2LFG0CaQppizEkc1i4vJFw1Vo5bytX3_sTtiMEehoQK55-Mw-092_2uxCZ2DdOBPWa2L3uwJRKy8cXJzCnPAOEgOx8vohIhIcxHRbbzIA6gWAjzlnDileorE3BAslOjlzVx4aJJIc9BzPoIjBi64xikJVFKIYBqVeCGBfmzcgfkAkmWquAhFzY0CePIwc1cOGZS_48yDT2rup-vPajmCdFKAzS-HNeX0Kb_bXLpQeLk_dD36_6Ll1aaBRCaQBpFM8XRtEXsZff7m0Cmc7h16VA6_WV865O8sj5xGhhXMKxABkqdSL9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
چهار تیم ملی که تا به امشب به مرحله بعد جام جهانی 2026 صعود‌کرده‌اند؛ آرژانتین امشب به لطف لئو مسی دومین پیروزی اش رو بدست اورد با شش امتیاز مقتدرانه به مرحله بعدی‌رقابتها صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24087" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24085">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7535185668.mp4?token=kb26pFrL5l1BQIPH108siDRnWYokJwcmcV52niIYY04RTBClig0cM4ho6WfQNSmhk-uHdvnh4vsfKDD30LQGUkgePdXLldVbq9id0MFmFEGvRZIGRXDSX7obapqnoTMh2_3NKyqg9Hz2Asb09GDp-FOVoLZ6guFVzEYnfcD_vbyx89OwtEVfAD3Wyjxf9l8RJMaqKNuMyVFQNuWNd5KwOAqZSpDsosHJSJ_h86TJHFFg301Oe36aqbq19XZtOUfqZhLFj83AMASZAQjB3JtlUJKDJocGcaVTBIidoLtTvhhyABpFp6_zWZu4qydjdp0ECfvUeZCGCIOIe5CRe7mV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7535185668.mp4?token=kb26pFrL5l1BQIPH108siDRnWYokJwcmcV52niIYY04RTBClig0cM4ho6WfQNSmhk-uHdvnh4vsfKDD30LQGUkgePdXLldVbq9id0MFmFEGvRZIGRXDSX7obapqnoTMh2_3NKyqg9Hz2Asb09GDp-FOVoLZ6guFVzEYnfcD_vbyx89OwtEVfAD3Wyjxf9l8RJMaqKNuMyVFQNuWNd5KwOAqZSpDsosHJSJ_h86TJHFFg301Oe36aqbq19XZtOUfqZhLFj83AMASZAQjB3JtlUJKDJocGcaVTBIidoLtTvhhyABpFp6_zWZu4qydjdp0ECfvUeZCGCIOIe5CRe7mV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24085" target="_blank">📅 23:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24084">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh6M5YCqaU0CMAoeoo93-l3iQUqDho1hDpXijR9G5JwKSFZW31ijETvtqGv_TC7T1arEClxC-HA1SacKyRNostqbOHvv86t1AJqzxh_kXmq0ofO2DqtSovDC172YyxIi1_SEPC1ubuQJqDrxSoMa9dW8D0sgvjnJexnCuiy0hv2vuJwmr7iPYeY0sSPddy3QXcWfrZB4c6CQVZxz7lBR9GuTT52ZT4A9POyMk1M6GwDWcCmeiK-feuc9ohlzu5eR8gfoH7lceGhX_Xmkt_37AT8gNaanBE2izXtpl86QoZGUDlVD3j48cpRgflZU1mN0G-msC4UEKAiGM4nDiNN51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24084" target="_blank">📅 23:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24083">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcqVtL6wtXzrjZZAeBAaFynhJR2PbF0XWvqNA3AyXUt0ewtOQbulmsus2iJTq2p-O4rqGk-W3UiC2nPKoopyqFGZipjUvISmEmFf4LjVo2fDQwlHL1qr5ElA_dXn7GpiSTZEoUCIJVaMmKhsyMR7v-DmMmG_QNKzvT7mmrB-Vtrlg-fCx4Jldusq3Se2qksn_SEFqDYhNDXr2NBisEBr_41vTlgwzpi406bHz34lzrvd9eXxbyTS6ZfFRNs7-wTm6NQpCmFUKODE16IOPYe609Rnov7b9Q6Cu7mfpdulq9TLD0UTLSZWM_ePejNP349T_JfmgGKIP4xNZXfaU4L-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24083" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24082">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxw02Fi-H47F-9WNHuCtgdc5WFZPon8n9jWYetErHW-3y0xqYT-mnHAvxRO581OjZQEjuQc0FlFJV9mJcKwP4auYv-IO-fzf3oyJX-Y0reFDw5zVeH5J6pe7xZLQqAy3E4k6S4nSQnzc9shJL_YVjPAS_fi18hz8T1qIZ7BO8o7LQTRF37geJ1ptgs4Vnw3F1tN6kzp0Yd2ifjGcF2oQKfeVUb-EGPMJHvbwnlY87koWRrp9nnUhf3bZiCBfw_1yvwAtCh1lxnbycLjG6HEJYlrGiavsZyzBVU2qsEl91e3scuvknxu9TeKrZMy2ZxLV6Kml3BnJ9JSP86crZHfvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24082" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24080">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK-qN0u9VbPnj5DH3YtwtHKb4qeHTt3yCRzC2q2QR5K8sei73opavBbD1kktqdolsodCO6JuZZmpWA2jtDcEbA3F-YFfhoZ53wWazffehGMbqnlUJi8vdQAeTihqoaO7lVOoAdLnvlT6EPB1BdRKMGJikRB6grCde6x3UiICCIr1kTzRXBY27OieDcARX5YRAihXopq8DeQfnPpcZsXZjK6g1BZHFuD_RnyRdtBtPB-f2JS2c7dvF6oXwgv5on7xyEotwyGEgZUZzvbCcSyMLr4K66G38Ghi-0gKDau8AkghF7teLAZtkwugNUfGKWE2jIXWStVkvZwhN3eI8JnCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
شروع طوفانی لئو مسی در جام جهانی 2026؛ دو بازی، پنج گل در سن 38 سالگی؛ این 18 امین گل لیونل مسی در تاریخ جام جهانی بود. آرژانتین تو این دوره جام جهانی 5 گل زده که زننده هر پنج گل این تیم توسط لیونل مسی اسطوره‌ای بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24080" target="_blank">📅 22:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24079">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a48741736.mp4?token=mJjXNIqKkafjF1Tz7Sbi7Wb6HipTd2m0Q2d2IsvUVOCblRdBkpmJM1Pr9S-UqYkS1w5UpMJkfDBB0PDFi2BIU-uxIZCJEXuw0-Y76Nxf2ZKKTxg6P1zkDDacMlMTC5BrlbOVijhF0pvUPTzOl_rkBoP_mJPyMWcqtI4PHLERCYR4bv3u8dUP6zXYGr4MrlpBr81APdZaLXvFfLWZ4YL-ztLXv16Rpc5JSDcFIxsrCjBQ621ihzleFVro0wBPZtBZGyzcV3reLGxuQ5bmoSqLxiKZWEJnaS7Sz9GQVlEe30XGRB3104HIoT3msZT0h0GFUTYXT0BqoEYTbZSa2k5Enw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a48741736.mp4?token=mJjXNIqKkafjF1Tz7Sbi7Wb6HipTd2m0Q2d2IsvUVOCblRdBkpmJM1Pr9S-UqYkS1w5UpMJkfDBB0PDFi2BIU-uxIZCJEXuw0-Y76Nxf2ZKKTxg6P1zkDDacMlMTC5BrlbOVijhF0pvUPTzOl_rkBoP_mJPyMWcqtI4PHLERCYR4bv3u8dUP6zXYGr4MrlpBr81APdZaLXvFfLWZ4YL-ztLXv16Rpc5JSDcFIxsrCjBQ621ihzleFVro0wBPZtBZGyzcV3reLGxuQ5bmoSqLxiKZWEJnaS7Sz9GQVlEe30XGRB3104HIoT3msZT0h0GFUTYXT0BqoEYTbZSa2k5Enw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24079" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24078">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=j9rMynU99gSSMDffTpXjxkPxutzpwrPnS_Vi2yvDt4AurQ7nKJ8pJtg3Fp4tL-lFO3bP0SPE-SQga_429QUvo_WIxGkP-lnsd_e673y-XCIe_ovFpdl4nw-DNBheo-305MmXczfonGn0-Rz_VKhsyfGRE8GSDbW8bQ6RzEiV146P917GsBTCbMmrBJb9RR646jYMtQyGwL7YlF2mN5Ty4Ytn7RG_EitG4mthMUrz30NcOvqhKdTq9Nnxsg-qvm_ckiLkPmDWnxG76po5eoKbR7924l0np3t4ciFsXBDWoY787ZCVZ9s2HMr_26lr04RWOMU7x5CLeHMYB8Vn7QKEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=j9rMynU99gSSMDffTpXjxkPxutzpwrPnS_Vi2yvDt4AurQ7nKJ8pJtg3Fp4tL-lFO3bP0SPE-SQga_429QUvo_WIxGkP-lnsd_e673y-XCIe_ovFpdl4nw-DNBheo-305MmXczfonGn0-Rz_VKhsyfGRE8GSDbW8bQ6RzEiV146P917GsBTCbMmrBJb9RR646jYMtQyGwL7YlF2mN5Ty4Ytn7RG_EitG4mthMUrz30NcOvqhKdTq9Nnxsg-qvm_ckiLkPmDWnxG76po5eoKbR7924l0np3t4ciFsXBDWoY787ZCVZ9s2HMr_26lr04RWOMU7x5CLeHMYB8Vn7QKEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24078" target="_blank">📅 22:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn1d7YVkK6bTkn5ItQ8SDryXNIv-fD9_4LbYWnsbAEQCmkXA859SkhSzEBP-numoR6C_dKHXCip-RnNqJ4Dvv2IS0fdmjtJc6Erf7Hm0H85CfzhCut7H1KoFl6FrsBhAoJ0C_ZJswILJmdLAIOfmGxhe6THaarOQWJEX3Chqb4Fknh7-hfa3s6HbX0805nrqTHw1C_HtWUlnjWgsW15-IvSfdmh5DnCh8JyZBOOfisQYYeFqp80L5kCb2omjgvjlpzP5g2R61_HNFWuVhwXQii6rYxX0y0FCU6_9h3bgeqytsu_dD4FeEug47HoY5TBkwYY8F2Lz_oyXeRtJjjbv3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
باشگاه استقلال: سیاست‌ما در نقل‌و‌انتقالات تابستانی جذب‌ بازیکنان جوان است. باشگاه با انتشار این‌ اطلاعیه‌ دست رد به سینه بازیکنان سن بالایی همچون محمد دانشگر و سید حسین حسینی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24077" target="_blank">📅 21:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24076">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruQ2AH_iGjOBHT-in3aMbjzpR--CESe485Nd8evVwLavgdscqH1620qdihXqgjaKFaPOilgfGQFE5Nt0yr_2dL0ipnPavnQgOmpS95oyHWh7jKx7Pzui7fbqB5iK2g_M2kiYGCh7lETIassw6qAXDOnjtAt6LeJEIzBpb0Mm7lj2dH1KTtVqF6QfmSuo47RNE-mHkjd65G85tIUNe829qcAmRD29GbjhuyELJ7nr3s5eKXTw65-KJ4iLak-a1ZwHySv24Iw_CPE2e3YrPN577pkJFtdQFPNuodGVws2uU_7yzMcSGACCWcfG7awwEezsbfoJV8RAojgK2t_JIntXQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24076" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=qks88s04rZroq10tjFcpSXGOh0l0Nr4YT20fus2AodYL3l-GtFicZZOvNqZoNOTSEiO8X_U3f9FUJPx6JRgBa75W4rGJ7wDYKOPGTRkIjF8mRn7UzR0noz0peWjqUEmtE-VgsT8wTMd5yDJE49LzfB_YdZrjTIv0Rn8xEyoFFEr5Ricejzd-u4q8By7ApknDD6Boqo7xGr72B9jjz7Lt_I99PO43nL53-EZoMXMHuoIgqGX69jWMRHLpFmmNVRCzIgbSWk3lGFyz2sOaPjpZHsygcEA88uNV6Ztq4rEADU06TMQbaZItuD9pH7m2hctk3RNqFbzcWhc9yhXNI1wmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=qks88s04rZroq10tjFcpSXGOh0l0Nr4YT20fus2AodYL3l-GtFicZZOvNqZoNOTSEiO8X_U3f9FUJPx6JRgBa75W4rGJ7wDYKOPGTRkIjF8mRn7UzR0noz0peWjqUEmtE-VgsT8wTMd5yDJE49LzfB_YdZrjTIv0Rn8xEyoFFEr5Ricejzd-u4q8By7ApknDD6Boqo7xGr72B9jjz7Lt_I99PO43nL53-EZoMXMHuoIgqGX69jWMRHLpFmmNVRCzIgbSWk3lGFyz2sOaPjpZHsygcEA88uNV6Ztq4rEADU06TMQbaZItuD9pH7m2hctk3RNqFbzcWhc9yhXNI1wmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24075" target="_blank">📅 21:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b9463294.mp4?token=A4wXG3EvkD2rfmPWOp5RnZJVFhoqOkSf0LwasFVUNppCSC59TobIkC8TkKYPEYAW9saR6ich1HfJ0vM2pC-qTbvWH5TrFZaQDDDaro8pArWH6ibz0xfkoO-YD80UcZdN795gbfZCdWZlAR2ZhvkWNLdin5qdXE7EiR5oE_9gLr8oSPhdm1AdqbwgVod630nUl4ZYH8SsrQVF-ez7Do89IJDi7vTX2U-DLtr9ceFnlLcflB9iT1XaPtWjvMElwjQdoVaSggx5hZkhWCZ6_Z1RFmZopBQ94H2Kp7yHG82_aMlw2Gp1Ickx4Nup-zvHnmlB2ggavzETOsbs-gqqnIRWCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b9463294.mp4?token=A4wXG3EvkD2rfmPWOp5RnZJVFhoqOkSf0LwasFVUNppCSC59TobIkC8TkKYPEYAW9saR6ich1HfJ0vM2pC-qTbvWH5TrFZaQDDDaro8pArWH6ibz0xfkoO-YD80UcZdN795gbfZCdWZlAR2ZhvkWNLdin5qdXE7EiR5oE_9gLr8oSPhdm1AdqbwgVod630nUl4ZYH8SsrQVF-ez7Do89IJDi7vTX2U-DLtr9ceFnlLcflB9iT1XaPtWjvMElwjQdoVaSggx5hZkhWCZ6_Z1RFmZopBQ94H2Kp7yHG82_aMlw2Gp1Ickx4Nup-zvHnmlB2ggavzETOsbs-gqqnIRWCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تکرارخلق‌این‌صحنه‌تاریخی‌وشاهکار امین حیایی دراخراجی‌ها در بازی شب گذشته ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24074" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxjU6Nn0lo7be0kb0yzIRRnA3P8g7DwS6Js4FCQxpUe4PUjX18Fem8O_WYOUO7deEvhcTOEwl_Ck3NmSlwsTVYS7Z5LRbf7t_a3A6EYkTEw1khSAQyGQjmUvCNk-nYw2b-wlGNN7kNbf5dePc5UeFS2DUkysFlTzmiXYlqDh8Ja_xobBnXKd6ZbXSKONbzuqFSubCW2YIXTDRn_QVwUeJUTPgIL7Z0GFsVApIgLhRhZuUfVAJS7ZbmAI8WR9w_iDalsaMG3LiLOLGCr6rz8ME8wD9NEJ-xU_EUOra1q9eACYkCTF4PvmnEeS53ZN0Y1OT1ToVZ7XbcE7JjruK6qSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در دقیقه 9 بازی امشب با اتریش فرصت بثمررساندن هفدهمین گل خود در تاریخ جام جهانی رو از دست داد و پنالتی‌اش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24073" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24072">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دکتر انوشه مهمون برنامه جیمی جام اسم ابوطالب رو از قصد میگفت یونس یا چی؟
پامپ که برنامه جیمی جام رو ساخته، ترمز بریده و داره یک کیلو طلا بین مردم پخش میکنه،
هنوز سهم خودتو نگرفتی؟
این کد سهم: pump
اینم لینک :
👇
👇
👇
ثبت نام و دریافت طلا
دیگه خود دانی...
@pump_vod</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24072" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=R4mDpddvacX19K-jz5rv5AXD7b8VigAAwY448n0_LrK37dgwl-e6gdxFiHJfWVQsfE3YX63lMre71IsljOsWZ-Gue0yJjsOoMNLaTIShyHK7TaEhm-WBvMAWF14S_siYrHLVHAeXx7BLgclGNg3gQK4CC1eknihmVsAKMqhrm8GU0r_ivq2ZBnB0t7lAN_gsL7_Ekyw5A32Zet9fPqjjisEVTP_6-hqWl3t3t33TP7gbSA1dnOt4EETFEraS7aBadkS1R2ZYNXqNvP2Yf_bFftdx_dYFi-55CM8n7ZUsLqPUpCWhS7RzDZM8-HREz9K1OO8WRs3Slei5dmmZuwIsNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=R4mDpddvacX19K-jz5rv5AXD7b8VigAAwY448n0_LrK37dgwl-e6gdxFiHJfWVQsfE3YX63lMre71IsljOsWZ-Gue0yJjsOoMNLaTIShyHK7TaEhm-WBvMAWF14S_siYrHLVHAeXx7BLgclGNg3gQK4CC1eknihmVsAKMqhrm8GU0r_ivq2ZBnB0t7lAN_gsL7_Ekyw5A32Zet9fPqjjisEVTP_6-hqWl3t3t33TP7gbSA1dnOt4EETFEraS7aBadkS1R2ZYNXqNvP2Yf_bFftdx_dYFi-55CM8n7ZUsLqPUpCWhS7RzDZM8-HREz9K1OO8WRs3Slei5dmmZuwIsNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24071" target="_blank">📅 20:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u90EoBgkWwEE_aiZ6d4eaHIglxEfGxi3BMyOViagcE8AkMB26y6WOng5_cbHBLgA9EUokrNBiRLC-RFGEyBRPJ_-GPFtFzq4eGV_GFLYcVtsBsNipKw9IkDCs3luok5DJaM4d8IWUXyqkwXNleEx7OXd--j4fOGmLMbdaBItsLrXrcpFp8mxTb8S7um_MoT6UITkkg05DYfLa7mjCL4pXxyp8gJ-h0nB9_-emLoluvZX2MeTaI9kODkMSBricmp6ddEv13OhlMpMiNeL7-eLdEXdvsYjQnGszYs2JHj_ofOFuqm7c5-ejnZwNWf0ZdiN29jvxaZ4DIL45EGoy_xzaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
اولین گل مسی تو جام جهانی: 18 سال و 11 ماه
🤩
اولین گل یامال تو جام جهانی: 18 سال و 11 ماه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24070" target="_blank">📅 20:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=Ius_aFgk-pc2x50-vTVD507vtbg5lvAmTsKDFNbSU23tOe8miP7bSS1blCyO6L5KTnywCBha2ngQT3pcde5hHPrDdsCC_OoDXsHIUTaefLUON3Lc7DcPOp0RHKycIKFaCmlIZ65eBzHnN-HplAGSDg-Ygf9hkS4eEQLW6kBMiujrpDRFqeFWCzKK4zLINSzXNzNaMgGbIbFefJ-J3GxhTt9Kxdxn6sk44ALxZKkbA738r14CSMkJGl2K_w9gMbs6GpFFgP6hjDR6gQhU6SzXN9nItp0J9Yhfwql-JRnZ0w5MS2XNOh-hRPrUWzmkVkMrL5gIpxEc1BkLxmVyzKSxRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=Ius_aFgk-pc2x50-vTVD507vtbg5lvAmTsKDFNbSU23tOe8miP7bSS1blCyO6L5KTnywCBha2ngQT3pcde5hHPrDdsCC_OoDXsHIUTaefLUON3Lc7DcPOp0RHKycIKFaCmlIZ65eBzHnN-HplAGSDg-Ygf9hkS4eEQLW6kBMiujrpDRFqeFWCzKK4zLINSzXNzNaMgGbIbFefJ-J3GxhTt9Kxdxn6sk44ALxZKkbA738r14CSMkJGl2K_w9gMbs6GpFFgP6hjDR6gQhU6SzXN9nItp0J9Yhfwql-JRnZ0w5MS2XNOh-hRPrUWzmkVkMrL5gIpxEc1BkLxmVyzKSxRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24069" target="_blank">📅 19:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr1E2c5ZChT1-hFHa23Cc-LUflYFn7a1jM9jD0l6gWuuU6dLLDO_TUaeIv_puIx5BET7Db8FDi7RkW8uoKq_AkF1JAm-THoiQgPPeibkypsdvo0HxLke4g_1i_qstZU9jdOb7sKZ5UjZDWM7cn6JS5NjbVuAn_w6CwJYV9TBLAyfbnw_IOOFu1VJOARS2J5-fnUdlP1anxdFsVGoT5-MifzxWBR3Y6pTwTs49kDDYR9UvlUVIrQhfWIg4nTFtbP3FM89Lrf6ip2VmMG0DKnYtwG7P6uSd9_GcHmBWR2e01GNarz4IEYUCfH4mtg7l7iLivaSQFcSgSxFqPstokoqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛
شماتیک ترکیب آرژانتین برای دیدار مقابل اتریش؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24068" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUQyOOhwOZjcawN7XBNat7nEduUfBdTQJDjWJvWvYsOMDzhd5J9jHPB1vHdJBTnFPRVhBHkO7BosxnRFQsIpnHSLqhaUtpxccQ901EO6Yr3ZyoByGcTWJMBckcSmbLrfdpaC1MTZSyS9NVkdELwRUj-_6uCmeuJpEnq1qgjIdGb-allB9SvrzUpx7D_Mft75N1bvIoVUOegTu8uL78xeBOmLmCLpuqYgP4KTy6UZC6EMkPc4ZvwhWvD8EWHT3RUmqXY-rY6T1WXQNLkl4ce2QYIfHagCbslpC2BqfJdEcnajba6Q9k1-bRkdehsA67BnT3CMTwdYNtF5i_tGFwgkSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24067" target="_blank">📅 18:09 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
