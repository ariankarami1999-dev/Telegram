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
<img src="https://cdn4.telesco.pe/file/FZiO55tkzNDD_2W2N9PRMP4a3ovaw9p9oXugPRwvLkw2HgwNS0VJOr9Tp3P87fRStl7HSn8cYGm4XKwwfs4NvqVriHMJjNWC881AAfyiAgh_nXgRP0Fs0McOLW-P-vi8iVf5zEQ5xmTRwbZT9SCr6yjmYpygGO8K7-EzEIyE_KV0eT22N7xwlgFhn6Pj1UEmCO7_WCt1_QJem9NxKxJ049a0F9me4x6x8V5YmW66BM8sC8zNOttEDhZsBcCVjVtS1mHFSPACJgaeL3vs9BZ6fcq1O7mtBVV48SsGtLOzyvvgSMSh8y6YL75En27R89UHjH2yBMIFxu9JDyKqOnO-kQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 455K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 22:38:16</div>
<hr>

<div class="tg-post" id="msg-30311">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI3okQLUpKvBDEXx5ZFq2ws74Vv-T0Vfu2yDFK_i8ES1QhnR28dmArTebQlNVqxb5ZInlof8AUIshCebOSp79OkfhkzXNVtBNYzAgfuf7D8Ja5LHrtbXSWcouot2j8gzDW18ZCuWtcc895MScCJLqqPNMbHCkL52YEcejpatkgRWrAeqfwvv3YVNElO0M-1G2QBW8WSB6hVN7KiucXmm1cwtoQgxjVhXDRXeRDh70PUZRSUgdNH5ph1_914RYlbbyYRzluIPTn0ZQzxLsGHTmXpqN3dyESDAzC5KDG_hi7c_YYBeEYXN5a6DbmGJLfFdRDHxFXJ7hhPj3EavUI9CAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/30311" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30310">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=jv9k-Yvzud9pXEoLCoXhQZd8ywsBEcvwaRunwFC3eo_y7rpNx5e7WQHAuwlHYN53-tfsowm2mOzGGj9PPCSLZW-vuXDRb3hRXrXywcAfcp5hFlBzIe7o58FqYlcDG_fSCLoJLM4tC0hnWbYf6vSc6q9FIkuXrK5plEWZ8vqNQmsMPeCwTFCrv884O5xTsWTJ56XmVbVSmmWeayRFCQWe8yLjrmf4iPGWCD3TWY3sZTCtWNgnmG2fryp0LYbNwKXpZWQ7XwbBdnoty0DFqS9jjGhpG5NqakzsRHDfgcRJNPhd_euzYSoWX8YL9fDuDeNN4Lcg1L3LuuCscRlL4Nz9GjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=jv9k-Yvzud9pXEoLCoXhQZd8ywsBEcvwaRunwFC3eo_y7rpNx5e7WQHAuwlHYN53-tfsowm2mOzGGj9PPCSLZW-vuXDRb3hRXrXywcAfcp5hFlBzIe7o58FqYlcDG_fSCLoJLM4tC0hnWbYf6vSc6q9FIkuXrK5plEWZ8vqNQmsMPeCwTFCrv884O5xTsWTJ56XmVbVSmmWeayRFCQWe8yLjrmf4iPGWCD3TWY3sZTCtWNgnmG2fryp0LYbNwKXpZWQ7XwbBdnoty0DFqS9jjGhpG5NqakzsRHDfgcRJNPhd_euzYSoWX8YL9fDuDeNN4Lcg1L3LuuCscRlL4Nz9GjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های خسرو حیدری کاپیتان‌سابق تیم ملی و باشگاه استقلال درباره حضورش در سریال پژمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/30310" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30309">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔥
هر روز ۱۰ میلیون شرط می‌ندازم که یا میلیاردر شم یا ورشکسته :)))
زندگی عادی شده. می‌خوام بهش یه هیجانی بدم. توی این چالش همراه من باشین قراره روزهای هیجان‌انگیزی رو باهم دیگه طی کنیم.
🃏
اسم این چالش رو گذاشتیم قمارباز دیوانه:
@ghomarbaze_divane</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/persiana_Soccer/30309" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30308">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETe4zAZsiuf8XA50eZ7n2UayqnpYFpOF06ljJ-pdGJunD-dfKJr8fyybwUyrQhSBitKBeRDvnaTP1q9vG3dG6UQKgnn2XxkwmwHZGVq5QCTlTBI5mwM_fYcfZXTrVYfdLdP3vGPC_4Isn96pwjz16PN0Oye-8ecaV6LZZ5PxWpR0XRtnK-Y9XnW7trGOXGWt3590b-Dj2SfdRSrUEYm7ThbNHtIAJqsBzqBTMdhHniayR-a6NxXMKRpezezSoWGMMZPzN-bYvsMVnzIEYKZI7D9hJHMyyWV9eC9cS8_5MCY3239zCFHmscnwqFMCek_7Fy0aI2pATT4YlTPJBadnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرامریک‌اوبامیانگ‌مهاجم37ساله‌لاکرونیا امشب به‌این‌ شکل گل پنجم خود را در فصل جدید لالیگا به ثمر رساند. انگیزه‌وچارچوب شناسی‌اش‌خیلی قویه. این 414 ام گل کل دوران حرفه‌ای اوبامیانگ یود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/30308" target="_blank">📅 21:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30307">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=jFIFBXuH7zDE_p-oqMEs1altpIcBojUjRWSwXEGzr1UWTt8QwG--FBXO5Ez53IDWXxKosL0mr1dkyFVV72XxKpVuayQzOGBFnDafGNyoEaZCUBLFsrM7pOTQ0axtSxeKASatJF4z_0GFvc_Z4Cgab_36DCSayuEE96c5Y0QOUCNlnd2iyspMY0QSOs_tJMFKvIN3CQLLYIGgKeNNwcj8a8oDNEYUs4XNhirM0P1zMMwMeQH8SA2V7UvhwfRHSlwf4OB0U1nDjoFDDRR8-DVc-QlnIwXSUwVf0V-TDDmo3wb4KV1b03tOcREdvIGy1FYFeVxOvIKXTUg0hyfVaqj2kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=jFIFBXuH7zDE_p-oqMEs1altpIcBojUjRWSwXEGzr1UWTt8QwG--FBXO5Ez53IDWXxKosL0mr1dkyFVV72XxKpVuayQzOGBFnDafGNyoEaZCUBLFsrM7pOTQ0axtSxeKASatJF4z_0GFvc_Z4Cgab_36DCSayuEE96c5Y0QOUCNlnd2iyspMY0QSOs_tJMFKvIN3CQLLYIGgKeNNwcj8a8oDNEYUs4XNhirM0P1zMMwMeQH8SA2V7UvhwfRHSlwf4OB0U1nDjoFDDRR8-DVc-QlnIwXSUwVf0V-TDDmo3wb4KV1b03tOcREdvIGy1FYFeVxOvIKXTUg0hyfVaqj2kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس رونالدو: ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/30307" target="_blank">📅 21:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30306">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VALeHTp71FVkFAvwXJWo79M4O5j_M1ItcASYo8CGOyWakdRdc1fDulediJuHTx3r1u8soJ1rTkrS1CeswV1X12ojdYDQlQ6-kdXQpoGkz_uQcpKErKnfHehHWtzt3d1iVWyUtxnHHPTq5s_2gPcuOBX03q6EkpU8vJ1xdaDTQ5Q45to_t-6gjYVEr6907kM5IfujnwR4mZVssYK_0Je3y5kEG9-snegM0yNZKoVi618NroAEaEupqiMcWlER6GF4mNHswSxcDFOm5aQVjSMTPqVFbVqlvizkPwRqjPTLQUvocVkvcKBMOHyGp8N0WAfezc4M1GUf0n8_WusHot8Ptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بهترین شروع مهاجمان بارسا در تاریخ؛ رافینیا با ثبت ۱۴ گل و ۳ پاس‌گل مجموع ۱۷ مشارکت در گل درفصل ۲۰۲۶ یکی‌ازخفن‌ترین شروع‌های تاریخ بارسا روبه نام خود ثبت کرده و مستقیماً پشت سر شاهکار لئو مسی در فصل ۲۰۱۱ با ۱۸ مشارکت ایستاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/30306" target="_blank">📅 21:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30305">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EleklL-7a0y4-i2aRdFE41oTTs6RoSm78VjpUv4gEusvh4eOpHiU41ZvHxoT9reoIfExxsoonXhFVBEjYAyoGSRxtIWLXwef7nsmjDEm1eCqj89Hy3ZQX8YKY1d29PaBnucF-M6AhC6KsG3T1IeI-CKJzbgtpi7TSal_qBva0KVS-XfPTuKF4D1EXbL1OwiKN-21YbTvVEmB4KCCwPw_OHVqPq1gdqENO6qqs8cyXbYsMLEbhLiNLlv-GlHzv_bp5SSqHPgyX0wmL7xigzhrlHMA18GmSD2ERz2ZJwvrVY8kfb56xY1KnuGGpJqN1NoRyfMZjE3Oecaje5-hQztMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو:
ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/30305" target="_blank">📅 20:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30304">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
موزیک‌ویدیوجدید ابوطالب حسینی با بیت کاگان منتشر شد. خیلی‌خوب‌میخونه لامصب حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/30304" target="_blank">📅 20:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30303">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=uzD3gk2Q6FO9IrT8No5vwf0ArX-QiuU6KIpx3iPFAppEWAt23sAugibNak7ofVwU3vrOze-Wehy8TQS6VS4nX36IO-HhAUcF6Rf_03J4G7m73tH3kF82Re-RnDK90K7VkFfp_mxrhVNNx2Naz5JI64xjWlqFjKogKYgWzRBw9iVCo0-3RxZ4aGvHarxbHJcFqJ51S_S6ErZxOdgxQo0UpUVqmN9xXY_EBlZa48vxG7loS6KKqVv8yS9gZ5d8K7dDxgPWP5hlFHkZCSE1yqKST6-NfH-W9lDkiGF0QKM5deT3NtnXd0UvB91gxjUNnW6G74DYLe2SwVaFHFNzjH95AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=uzD3gk2Q6FO9IrT8No5vwf0ArX-QiuU6KIpx3iPFAppEWAt23sAugibNak7ofVwU3vrOze-Wehy8TQS6VS4nX36IO-HhAUcF6Rf_03J4G7m73tH3kF82Re-RnDK90K7VkFfp_mxrhVNNx2Naz5JI64xjWlqFjKogKYgWzRBw9iVCo0-3RxZ4aGvHarxbHJcFqJ51S_S6ErZxOdgxQo0UpUVqmN9xXY_EBlZa48vxG7loS6KKqVv8yS9gZ5d8K7dDxgPWP5hlFHkZCSE1yqKST6-NfH-W9lDkiGF0QKM5deT3NtnXd0UvB91gxjUNnW6G74DYLe2SwVaFHFNzjH95AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/30303" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30302">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=vFFXEBy6RwwBbQy-bBNCpIY1rRRSDGf1YCXobafrYWTtUTC5qy-hnW1HNyZDKJNeYGfUu1wC4RC7BSz4YlaJOG44XOGbM625NxM5nmf-U-qfN5jaVKZbkQhQDM457RpcOvpLp0LoJ9cUo9qp0siYIPYVhDcXawmafmDAQ3GZgOC-EdWkO0lswjUHr0eDKkaaLKAXSoRfOdgTAI39evAb799yjc6_NihBGzLnM4hYsy3q58eSe5SN5bvX1vVYUjEzXLQ36sVLNoco5mNx1J2z4r5938H1oQgJhDcZM7f7gYYNZ0HTQeeaAVTymchzUbbad-hj1gp7i88T5jNnK1NAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=vFFXEBy6RwwBbQy-bBNCpIY1rRRSDGf1YCXobafrYWTtUTC5qy-hnW1HNyZDKJNeYGfUu1wC4RC7BSz4YlaJOG44XOGbM625NxM5nmf-U-qfN5jaVKZbkQhQDM457RpcOvpLp0LoJ9cUo9qp0siYIPYVhDcXawmafmDAQ3GZgOC-EdWkO0lswjUHr0eDKkaaLKAXSoRfOdgTAI39evAb799yjc6_NihBGzLnM4hYsy3q58eSe5SN5bvX1vVYUjEzXLQ36sVLNoco5mNx1J2z4r5938H1oQgJhDcZM7f7gYYNZ0HTQeeaAVTymchzUbbad-hj1gp7i88T5jNnK1NAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره مهدی مهدوی کیا از قرارداد یک میلیون پوندی اش با تاتنهام که بخاطر سربازی او لغو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/30302" target="_blank">📅 20:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30301">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=jvITuig-2B-OcVBKQPeaACGQQBbswBZrewl8Nhqipyl9fBQUuCAIWogO_vu7dfqleLw-UggOewgE1kehjCGFRlYoTM9ozpctUM9EZu8tnGFf5zlrkSw5n-WSO6J-mYu6ciM2DcjbJ0m_bMxbBsis6EA5V-JcX93t-DOPNUKn_uh-3FlnAtH_uZ2yBFMoOGlanw63us7m7cM6tsukj8vUctajl2icHjff_n_z4184NBjDKeztNSrDit98SQ3_XTMuhYv6H5BAyLgH5iX5DBlEWbH9pqDuhsaLyHxIWUVqMdusj_WcGDcdiJ9wE2nMVdAJCvnR-miQ_XJOwkUhvV9SewZagqgV2ovRRRKvj-g0UOd9g7bYAjYAETXtnPgChBH51Mh_VAE1nZhQa5byRUPp3UZZVrRwJV4C0hfCMkg3TBwZSsRaG3fShiVpUI1me46EpxLRlwhy00yZqEuqQQh1gWzsTIavnJfejGbqn206l18g2JwQSITd0U7PkvNPNB4-WukM61loI0zy0w5pgWcgVfm1q4IWGxaBL_IyuSMTnp1E-5IIswc0QZW2raC-TTREtgx1jSxKGSgt84T_u0cL3yl1PbGPYiwsXkooZRYJgi3CQy7q5jQro_L-I3rdUwYBh2o7hS2Lh_Jr_5gTy5jlNagueWtd9LSjNL0NedA-NlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=jvITuig-2B-OcVBKQPeaACGQQBbswBZrewl8Nhqipyl9fBQUuCAIWogO_vu7dfqleLw-UggOewgE1kehjCGFRlYoTM9ozpctUM9EZu8tnGFf5zlrkSw5n-WSO6J-mYu6ciM2DcjbJ0m_bMxbBsis6EA5V-JcX93t-DOPNUKn_uh-3FlnAtH_uZ2yBFMoOGlanw63us7m7cM6tsukj8vUctajl2icHjff_n_z4184NBjDKeztNSrDit98SQ3_XTMuhYv6H5BAyLgH5iX5DBlEWbH9pqDuhsaLyHxIWUVqMdusj_WcGDcdiJ9wE2nMVdAJCvnR-miQ_XJOwkUhvV9SewZagqgV2ovRRRKvj-g0UOd9g7bYAjYAETXtnPgChBH51Mh_VAE1nZhQa5byRUPp3UZZVrRwJV4C0hfCMkg3TBwZSsRaG3fShiVpUI1me46EpxLRlwhy00yZqEuqQQh1gWzsTIavnJfejGbqn206l18g2JwQSITd0U7PkvNPNB4-WukM61loI0zy0w5pgWcgVfm1q4IWGxaBL_IyuSMTnp1E-5IIswc0QZW2raC-TTREtgx1jSxKGSgt84T_u0cL3yl1PbGPYiwsXkooZRYJgi3CQy7q5jQro_L-I3rdUwYBh2o7hS2Lh_Jr_5gTy5jlNagueWtd9LSjNL0NedA-NlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنالیز دیدار هفته‌قبل دوتیم اتلتیکومادرید و رئال مادرید؛ ژوزه مورینیو به‌این‌شکل‌بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/30301" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30300">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErVHx4tnYPzar7d__KKHvdX15DFHMDL9OGwQG8XEryn2XSXnsq2iEd8D82-f19zEzq0DQK1W-jCvJSL2lrcu2V-DCJgsILz33KxPlDdJBN43tnGm91PUSa4POH0vE-tHOMRWCHkwnq6F2XPDkwG6vfsn9jhwJSTtsMRARYTBXC8t71_8_2GXTsxLcaA4HvAGdkm9GFMHeFxifBa2rAKBtQcFr26azme9u6T60_4su_E9lF0jGnK4ILJ0d9moa47k5Oliqm_-v5EvAKkXx81a5Pm5dyfmsJkV5onbYIOkUkZDSGa42MZZodgbDiy1yl0GtN0r6G8O0VpIn_Sw1CfoYdS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErVHx4tnYPzar7d__KKHvdX15DFHMDL9OGwQG8XEryn2XSXnsq2iEd8D82-f19zEzq0DQK1W-jCvJSL2lrcu2V-DCJgsILz33KxPlDdJBN43tnGm91PUSa4POH0vE-tHOMRWCHkwnq6F2XPDkwG6vfsn9jhwJSTtsMRARYTBXC8t71_8_2GXTsxLcaA4HvAGdkm9GFMHeFxifBa2rAKBtQcFr26azme9u6T60_4su_E9lF0jGnK4ILJ0d9moa47k5Oliqm_-v5EvAKkXx81a5Pm5dyfmsJkV5onbYIOkUkZDSGa42MZZodgbDiy1yl0GtN0r6G8O0VpIn_Sw1CfoYdS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 88 روز از این‌ویدیو تاریخی از خوشحالی مجریان شبکه دو روی آنتن زنده صداوسیما گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/30300" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30299">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opzTjExt0ATqUr4p3O0DPJkgobr9_j366IdbO0LMa5VU4xhUCd7fZClxonHtbjNysc2OXOiXYW5ARJIoc1YgCsFCmS_KZrI3JscRHMFaZXH-99P4wji1oEK-KqlVF8UufEVQcXxsawuWs5XUTMb5wery0KUCXn9uUlnAyD1pIzZWAX0Wb5H2Lg-0d_hF2CRaq2Ce7amEi3x1-3e9HS3AyW4bSlAiKd3VZ0S61Vu1635zvnZECh_OY-QE4RIrB-uRYn8dEGPzomDnAUirVSeibKnH6zSIWV0HlaZimllTwT-O6ls9_KoXa9836WQoqk_5Xm-OwBob33gYZiOvxmhTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
از تحلیل و آنالیز تا پیشبینی رایگان
از مسابقه و چالش  تا همفکری و گفتگو در مورد رقابت های ورزشی
✔️
💥
هیجان ولذت پیشبینی در کنار بت بازهای باتجربه و تیم حرفه ای پین بت
✔️
🤝
همین حالا در کانال پین بت عضو شو تا در مسیر موفقیت کنار یک تیم آنالیز حرفه ای به سود و موفقیت برسی
✔️
🤩
آنالیز دقیق رقابت های ورزشی
🤩
چالش های نقدی
🤩
ارائه فرم های  رایگان روزانه
✈️
لینک عضویت
⬇️
🌐
https://t.me/+IxmGEx4ep9A0MzQ6
🌐
https://t.me/+IxmGEx4ep9A0MzQ6
🌐
https://t.me/+IxmGEx4ep9A0MzQ6</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/30299" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30298">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPufOWyrNYxBjfUgQKhEnyxqrIiNe6JPbDJ8b4Z1CHenU7q2jnmeZmc-TyUlaKLDiUv7xR6b65S44sB4E_Q9MJhYChEJOiL-PyhlTk_IJeaY6yTAD7Ykw8P1t4qIt4-aKLkASzVQuAF_l56HXW1kWASiS47RYr3BuD7luSq3SuuD_HEc2NdygXZlhBPRsImbGbOXH_GlxJ6FuthX_xkFLpDobsFApijsB_JIezdQyTbLePCyC9xTsiF4U_NLclWJLgEBun3PUuR9dlZ5Js57-ISOJpfv2-4x1imYHzaonb6FQT9-ihuXcVehX6BltjziBY1KpT2eXd8Cyeba2pi_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادگل‌های کریس رونالدو و لیونل مسی قبل از جام جهانی 2026 با بعد از این جام تا به این لحظه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/30298" target="_blank">📅 19:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30297">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbQ6mamsydrF48lmLl32XcaQ-x7KS2kQrt4hqDfu5FkcRY0GO_fouNtb44gnD8YePC7BOlW02wCqIUYxZMcwI6U4b_gIGjSzfvp3MLYnVDjv9bzTFNCSIrxah9qbyUypeJnY8cHSSUTInzY6RpQAeeVtS1rrG9m_FpZb89Fft8OvJC9Qff0HeVj80XaKvdVfuXBcZHGilx8wLkIBP8aaR8q08xvnXdUBDMC58ERQRj5jTRA-cIZgvH0y8PKYj7wYcXUVoSDki2w-6MrsuAKw4u64kgUFQ0J3LjnbnrvSGUbNHFqsDdng79XdzWCD581tVrqi_RLRdLej4r51pKC6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/30297" target="_blank">📅 19:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30296">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiGDuBkYnJWEnNT7ph4FHBsL6BBIBwDGtGf6dR4UssVYklQ_hJ7UkKr1GsFGGv9mj1aAwkv_M3qMaOmQO71PDfTxo4quI3KoGWiUHHGTuHVEHdrqq2xJq5jwI1F7SK1rloQiW-p4QbCXfVPaCc5Ey5wLxQS15ul4I2P95lM4b59SC_qj9HNerLWE5o1CGek3A3DOLiT9fIPw1ODDmFnl-lEVJ7fdjXH4TAp33IpDNgFkiXbu9K2XcX1nakytbBS3EbJ0nSoMKwL9ayoPl_2yLt2hvyGxJ1ibbQg96pmyKqMXDNGgWeX3aE2paq9ejnuh3aZY8TCXgHpGbrKRYpNvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/30296" target="_blank">📅 18:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30295">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBMEH-7NL5NmkF6G30_Yur-A2fMoInsMHfIyfctlJ0WFzn5YwyPqlaZk2G5Qu-WPw1aZecHlQSN_WHuyBohF7APW7ZsDcnY0zhd6QEjvsw6RNZgC6frQhS0TRRELG3ZlFyXI7DJcj8Nq3FyctgiQICAk1yPFTjzjZURYgw12tMm-_ut1Fe6gVNoBzJwzUOUuyZXjweOe09wjF-thXvKkzPudVWUw9Qt3mrROFIcZFQoBFVL1ganCqNaqiuhGbJoOnvwHeM8eTSDshmgFPHC6op3i6E-HAl50hsLWIGJVX7aetlKjVhBd0bk0nMRj3IOIYeXI19rtJnURe4TtttwdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/30295" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30294">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=t_lWrczdLQHBy3XjoJ8YcUhc3ahr3kTn1ZudzCUpaCR9AEXvNB4SR18n1slalMHni59pqhYuzqEM___1_SPGL6RPauOP21TCK_0c5zdqtc0l4eOE8qiVT-Cj_VQwxRkVkKXyek_MNPwJ0PEIUqfPMdogLVf_-YFZ7IYTy-XhEOchjXhvZ1d_y9JR9V8og_oEvXNI3AfY1LbDbpRlddG-rIt3rZrGotA4WNmt1JXUd0GKHXZcJcCklxBAQ5kPXnxPP8oeBS0MsHBMyEh_c8cjBvqlHIrbnfSm-_G_pp1-2NofuWNiptl6jL1diRLRlOfnYJNDs476xI_Yg9pKHUrLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=t_lWrczdLQHBy3XjoJ8YcUhc3ahr3kTn1ZudzCUpaCR9AEXvNB4SR18n1slalMHni59pqhYuzqEM___1_SPGL6RPauOP21TCK_0c5zdqtc0l4eOE8qiVT-Cj_VQwxRkVkKXyek_MNPwJ0PEIUqfPMdogLVf_-YFZ7IYTy-XhEOchjXhvZ1d_y9JR9V8og_oEvXNI3AfY1LbDbpRlddG-rIt3rZrGotA4WNmt1JXUd0GKHXZcJcCklxBAQ5kPXnxPP8oeBS0MsHBMyEh_c8cjBvqlHIrbnfSm-_G_pp1-2NofuWNiptl6jL1diRLRlOfnYJNDs476xI_Yg9pKHUrLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛
خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/30294" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30293">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=ATmKJKM6C7IUJuuOJ52Gthk4w4139Pk_fct0z0uLVm7P8FN-93CPLJpBfbRMU_KSF3GRYX8oOQQPgIN0h2q34vlpE4dh_1xQSLBvq0tVPTV2BsGZPoYViJiuBeDdvCQ1rYWPOjKTjiIymJFBm0WqRRrk-Hf6v2rtMkvmthK8jcnZX4k6PyzHTd-dxbR4KnBDdqVP-jzQKMHQTckn4GMlAOP1B8T4BAFGte_5pFIyf6GPQuyNzDTqsgT2DsTOGK2Mfgy-YCTIGpTVJNQZ-Ag1zK7etcggywbIINL1TjG80dytq7vw_0tJbENvVXTTk7Ade3hG6zziNLZoD3WDbk3fbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=ATmKJKM6C7IUJuuOJ52Gthk4w4139Pk_fct0z0uLVm7P8FN-93CPLJpBfbRMU_KSF3GRYX8oOQQPgIN0h2q34vlpE4dh_1xQSLBvq0tVPTV2BsGZPoYViJiuBeDdvCQ1rYWPOjKTjiIymJFBm0WqRRrk-Hf6v2rtMkvmthK8jcnZX4k6PyzHTd-dxbR4KnBDdqVP-jzQKMHQTckn4GMlAOP1B8T4BAFGte_5pFIyf6GPQuyNzDTqsgT2DsTOGK2Mfgy-YCTIGpTVJNQZ-Ag1zK7etcggywbIINL1TjG80dytq7vw_0tJbENvVXTTk7Ade3hG6zziNLZoD3WDbk3fbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 3.5 سال از این‌گفتگوی تاریخی علی فتح الله زاده با محمدحسین میثاقی روآنتن زنده گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/30293" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAhmuTQ0YZ0vlQj81311dWCpWbjqBu3cAbMz3j9oc_KjY5fbcEwMLzMu0i8TvJK4SFI2uAS-nQ9fSxeiZjHEha1xDx-5m_qrJ2CsEVp5F8n0OSDv5AT4Hwu74AZB8gP6rRBHjYkHoum65jhoA0tzTsC888toPK79EoTaoJWQAFao-edj2ZplXpI8x5bvFkhjt8aJc-pIK1deMqs09Y3Vp9MAzW12Z_OBTEIrtlxsOI9kgA4vk-ppcQvQrRMqMNG6OhNoi0wt_bw8QAZwVDnFMbVBiq3WIq627LEYVrZTqoK2s1cApp4FDkrT3ui23VYXKagrcH2QdYoMUfh-JgysrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی، ستاره‌ی پاریس، با رد اتهام تجاوز، مدعی است که این پرونده یک سناریوی ساختگی و ارتباط آنها فقط در حد بوسیدن بوده‌ است. در حالی که شاکی بر ادعای خود پافشاری می‌کند، وکلای حکیمی می‌گویند امتناع او از انجام تست DNA و بررسی گوشی، نشان‌دهنده‌ی دروغین…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30292" target="_blank">📅 16:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30291">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv23Z7rhs3RCxr-dOJ8N-ijV49pI04tFCDaSlXazK6xMs4UyFekJfNfbdsPaN4C3kSAhTx0bkwr3x51_2Rww-XeE-6GpYABZihq45Xy739Qarn7UszLUqQuJVVA1kQ6kZ3mwgsD5ZNQorz33rSDXf0GSMFCH7RKVfwOdkJMh25QwaR0GEQh0_T2wnfGqOuKLg6jC-FKf2O1rP7lWHgz0hKXGGKw0g39_RRQ5QVxOqtRQz17rk5lALDojpC9N6R5aphxYIIlpJZE-kUsa_ihp-3_C5Odt70M-PzKthZXzmUl8KdfKbDqB8jmneDRfQJKe4PZDJ2HH00EBgrKsq1dmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/30291" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30290">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUDyXmJ36FEU_MT25i-4u2knrfB4Z6_u_NWWMF_Afw5iZgQaT0XdDyusTKGid2kVNa7HftQUvjaOSzzCkPTNRn8_XvDVXbuhEiIwc2-4f8YmUryyHL4icJz1PdDDSFTDuWk5KTBdXoTj1Xcj1zQR8iMHVIbR4xdcNQCjoRizIVfhvS-TrqNKj7z7lBwBHpPJgA1lB1mklHsaxkUG_YmlVozdpFtO51-GRmE31NkEu7Fm8VQFRXlkFm_B845O0k0ZgVvua_ax1ah_Wgxo3xXzBAFXnCTtry6bTr9wvajXPYXHvvtOGtJgx0MjAskbVIwvX9_UOtvWC6q43YyEcBrLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ظرف24ساعت‌آتی رستم‌آشورماتف، جلال الدین ماشاریپوف و یاسر آسانی 3 بازیکن خارجی استقلال برای حضور در تمرینات آبی‌ها و دیدار حساس مقابل تیم تراکتور در هفته هشتم وارد ایران خواهند شد.
🔴
اوستون‌اورونوف و مارکوباکیچ دوبازیکن خارجی تیم پرسپولیس نیز تا پایان هفته وارد تهران میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/30290" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30289">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2_l66wN5k9CQOaT6Rix9G-x40nZ3C6o1igDBgQXGWLus28SsllypWOFnXPhALtyfblsvo2I2rGDWpbLo9hcK6709slujCkPEITmWsGfEEHuWeaMJzxreIkwg_zpZAUxMYPhiGSs2THcZQRHkeGoqpAaVyxLn52CmZFbAAPcbYSC4ukSLt96Z6B-MZQKApWh1yakL6HtxB6Dx-W4F5R9pDhEUpPSSOpq2vscrx_bQvP_ejXvgkwRNekvfSqAHBVIY-h2oGa_i2f2cYbdnYvtMUOkTNUOix5O2VAMr9sgjtiXVu7jn9PSdKkpUVBEpQ9h5gzWAMwItCUaRqXcYgc_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تیم پلی استیشن ایران در فینال بازی‌های آسیایی مالزی رو دو بر یک شکست داد و قهرمان شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30289" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30288">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmC4UYlR37QuYf3tPuFAYC-L0cLbLgCoSbMJlBxT5zUZEIYy1U-YUcNZr6YrZixaPjsYeRHbL-La9pxwItW97qyCbEotYXi19yl9rkzAjluyr5kcji80xnaziqniCfpe6JR66oyGZykGa3VTalkRXBhAl0YwxlptGGjerMeoxuMA8GVe7tHixFbav6wdGTF40rZ8NuDNYXvoxWHlwEo3pEDnuVlA7SaYWNVGJU0Rf4rpKZeADwlqaK4LRl220FcriVBrYHHfUSGQARtU5GHErvKEffhL8Z-M7zjys9oZfqUGjvHhSLK9anOX9QOMSGT4II_YXEEgiLSj81lUAr3mbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه.تعدادگل‌های‌کریس‌رونالدو با مجموع گل‌ های رافینیا،امباپه و هالند درکل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/30288" target="_blank">📅 14:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30287">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_ERqF_zsYr7LAjZng3d4yMUGh4wvNqoEJbWpn63QFDWc4Gt3uRe0PWXC-JXJMqg_EPw77uv4G5ML_uiXQNkkRLGmWUoEqD94uNF1LOWOEYvWpB8SPCI2OkqcdH_pjx0JRFEeKND0a1lc4AopSO7xBHtjQnxea0xGnRV8rz7WPsqyXn1xV80IwW1k5tPTc85AwDM75xx5T538GORcWiJ7xRlsr8kFuhGj_8aDHqRpmdGIj65jht0tzx0oDJi7-rfETkuV-P9c46r1gB34TB0RoFd28XcWfXyeuJh_D9wovjcwaJCnRExK-5VF28elc4-yTy0Y2c2fdl8boqZxmmPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛ لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30287" target="_blank">📅 14:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30286">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7GaLUhaogIXL_lGBaVzWoPNVCq2KprvpCdDXjUaE0cRKujMGFFE7XoeB0oGsbJSPjHZyXPIJJXRmVBvWA3v-RfqwkSu3U0WqevGAFInQOhEodtbUsbT1MJPXCraA-z3FdQEpulefUWuqdUwIm4bmqtqlwaY5GCLMAsaxiq4Dz1vMCffg3MlM3B00cmBZo77mrVXjZlkvYlrM-6AAIdhdO2uDeN20bIAsHJ0UhUk1JCvDznl9WkeoPXMSAj2c15dwOA4RPRNGLDKzbyTF_EYAjgRE2gcB1r_HQflGhFucquUGhpiQ6tdPaHGNJqn_Msu_k3jgjPJz9-TxelTyCR6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30286" target="_blank">📅 14:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30285">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVv945PSqUUNZO5M09_SD5AFoVPXDuSMoO1r8hda6fEWwXXxMRGRpFMOGPWpoLzlPzSUFdHGRcPWW2Vh9yOYXnYzGLs_MrCejKjmjqrHDQ8WFKtWPvY3Y4zUwh-bxCBIZvpsPyPSOhBn2QWA0Zanr_QoYRgf2LI03ijLmoOs7-i4Lx_FjuYBo4qdVeeqko3D-2Ls2k2vZzwL6IMHCPdn4-PMY_wNHmIDrdae670qihZNJ17qkqYx85K-MxogbCzDdHCpfLddYuiE7GakpY1W7XghFswCiwUUOglnFwzB1kx_-n0gqwNvdbZvZedEx1x46rpvmuvWWDCvL9OyXr9LXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇳🇱
تیجانی ریندرز ستاره هلندی تیم القادسیه:
نمیخوام وقتی فوتبالم تموم بشه باز کار کنم به همین خاطر تصمیم گرفتم به عربستان بیایم در کنار کیفیت بالای لیگ این کشور آن‌ ها دستمزد بسیار بالایی رو به من دادند که زندگی خودم و کل خانواده ام رو تا آخر عمر تامین میکنه و نوه‌هام بی دغدغه میتونند بهترین زندگی داشته باشند. یک‌سوم‌رقمی که باشگاه محترم القادسیه به من پرداخت میکنه هیچ باشگاه اروپایی پرداخت نمیکنه. از انتخابم بسیار خوشحال هستم و میخواهم سال‌ها در لیگ حرفه‌ای عربستان باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30285" target="_blank">📅 14:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30284">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1454042688.mp4?token=XlSRuonoHIW1K2SpNjqBWi9Tu7Lpyoebea2PHg3Z76RfkuvgBLV3THlUICi3NLKg798j_tcRv8E9XVp79fHaM9DyWMdbxjfyv-xE5ZQMvqXT5N3vRmRMeR4R84ib73q4wqadCha57eZLDJXETfn8Di_QBd77q22_-X-8WpmIldHJWI2D6hyO5S2nPAyTwVTVZgJPUKdVkJJ7NU7lY_8Se7kEncv1Se3LC5gZBO_jmQTJQsaK1VasaHPgomcfy_UBzuI56FB86GbiRZVUD2gKUJl_9DtzDfP3Ru27-PT1L4ZAAu_4eYN4PPu9zlObgjUHvFXLojhogoob9PzUuH-lfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1454042688.mp4?token=XlSRuonoHIW1K2SpNjqBWi9Tu7Lpyoebea2PHg3Z76RfkuvgBLV3THlUICi3NLKg798j_tcRv8E9XVp79fHaM9DyWMdbxjfyv-xE5ZQMvqXT5N3vRmRMeR4R84ib73q4wqadCha57eZLDJXETfn8Di_QBd77q22_-X-8WpmIldHJWI2D6hyO5S2nPAyTwVTVZgJPUKdVkJJ7NU7lY_8Se7kEncv1Se3LC5gZBO_jmQTJQsaK1VasaHPgomcfy_UBzuI56FB86GbiRZVUD2gKUJl_9DtzDfP3Ru27-PT1L4ZAAu_4eYN4PPu9zlObgjUHvFXLojhogoob9PzUuH-lfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنایه‌گزارشگر به قلعه‌نویی و حسین عبدی بعد از شکست مفتضحانه مقابل کره شمالی در بازی امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30284" target="_blank">📅 13:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30283">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30283" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30282">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=ZO9ikl4UkvbHgx71YS-QjLXs1sd67T-iYNYKIXvxB1yu8M4Mkt4KpuLAjIW6zgP16nW9qQFY1waSWRoua_-c7EehaJC_Q-vgwEag1zRQjEJh4azEuiiytDNm33rTd8trhAVkFWXn387IHCmsifgAxu1Wt-0ptvq5nDrzdMAVnLQbnbw5jqKHPAGU0CkfqTYM7DvLemW13eaPGIZWlKF_9B2q2xMdcD3FSIDY8CLCXhcLsd4arCqV-dDkPsqYV9i-cHDglNXLRZuqdEQZm-ug9LFSCxUlLPQv7v1HWiHFStuL-KRngA430zkIjiA33idpRxWKJxVv7ClpmkDTL4jBQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=ZO9ikl4UkvbHgx71YS-QjLXs1sd67T-iYNYKIXvxB1yu8M4Mkt4KpuLAjIW6zgP16nW9qQFY1waSWRoua_-c7EehaJC_Q-vgwEag1zRQjEJh4azEuiiytDNm33rTd8trhAVkFWXn387IHCmsifgAxu1Wt-0ptvq5nDrzdMAVnLQbnbw5jqKHPAGU0CkfqTYM7DvLemW13eaPGIZWlKF_9B2q2xMdcD3FSIDY8CLCXhcLsd4arCqV-dDkPsqYV9i-cHDglNXLRZuqdEQZm-ug9LFSCxUlLPQv7v1HWiHFStuL-KRngA430zkIjiA33idpRxWKJxVv7ClpmkDTL4jBQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانی بیخیال هوش مصنوعی نیست؛
این چه سمیه که از مریم‌امیرجلالی و حمیدلولایی ساختین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30282" target="_blank">📅 13:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30281">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW2CtsLE1ItLlOUbMxLsJJ4UJ1H3CpH1fJPu_puz5Cpi9hkz1UPu1hyqTtcPQEOUro_0mDfnMuEpRMQFhCEv0cPKout4Ez5utJRb4uhsyQlo3F421Soy0gDIK-SIbQSYnyEosnbYiy-SwXCQW9RD0sYj2uNqZdYV73W50FwOcTbn5qqte1bErB2PIGvcoU4HDlmymL4i2v5O1g8ASDhbmNI9tOenH6e7eOEht-iY8YD92bkiDlonfkeN3RbRWA5tCGauH6AuRtwzHNfPsnnl0nwY7XusYnSUx6ky18yjn6o_Sor4SAp55HbdwX8BmsJlwkXgaJqtxs9Tpk18LLyrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب بوکاجونیورز برای دیدار خدافظی کارلوس توز فوق ستاره آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30281" target="_blank">📅 12:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30280">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdxqiBgH9FFC21EcaNdq2W2mWKuHTomyQNwMPVpL2IYhegtvRjBhaTj1p0VAr_4T2mwc4va6yqyOjzUyQVRuqkHJebNwIxFH7fID_UYJHi-KDVeQgLB4EclROlJvj06zvqSxSchuUQN3XiD5KBflFZ5aUFJfecG9aykx9Qi_7eENjyodUAQp-VIQeHqDf8VTmh6q1S1Sel27R1yzvIugNDfkxyHXlT0-meX4IhSGbSaSBPvXoyiRdazXKp9tjNu9bmAbRh7GjOj0lP83SambiIKcmH6JaFoS6hM1AgOsMc79yihG_6a0KuGM1ah2pPP4skcA2kLg8ta7P9p-qWh0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناس شبکه CBS ترکیه:
«رافائل لیائو فکر می‌کنه برای‌تعطیلات‌اومده ترکیه. اون به دید حقارت به‌فوتبال ما نگا میکنه انگار ۵ بار توپ طلا رو برده.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30280" target="_blank">📅 12:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30279">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk2abAWzJkKs829YuvdjMvfeV_TbmdtR2mP88UZETptnWk57-MP6F-Gfob4V_uWQ5Exc_PdHwFQA0gLNqyC340umgN5VQqcuKa4iQlhTlLgpL-vU_KQIaMKdXH9VDOprxuw0UZ1KtPy4yu6DDciW6BgfQoveL1WEtxoLNF-m49O8GQ688oofYUDOJGQO4oa745Xs-UZRnndY7ATIY1tZJGLjFhA--wxg_vcj1ObLzzPn7Z4ySNUCDb-qwQhmoYZN-shnK5LSAU73fq_jCr8p2Xh7HWngozLlCeAGbsvbl2lKjoLj4FlnzwmZVfBwSpxScEccgo1CvimivSDAKYhf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30279" target="_blank">📅 11:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30278">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIFSkZoz-WbxOzm20Q61utX0FfcHlal950jkjH7CiM9KMSuLrN2BxBtzbim7Jtpfo2vaPVrDjB_i-y9EqHAyfspGTZZPBvTIhMOj08h6eGybaM4Icrc2oVs-Yeft9-BBhoZ4bBTOH-hqUvo-FzF7BTPSKgbwMsWoonG1ChQORzArZpsvxDU3D0DD9BU_JMVw3n_zRvfcmFd6pFBFS0ejdS6NeYDHj-38HZqk9WMHQMqmo202vXN2oqUYlhiv25BWtT_Oo1KnHCjGPD2aaVrysVKdklX15DGc7Kw4ncIN4glSBtuoY00v-54uSe6ZyJunwS2ERUw-mAlGtSkGv-0Rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30278" target="_blank">📅 11:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30277">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0JySmYOH4bYHCcSM71h8eSLmb6kcxzC-MHetlU_5_idMrJquuuPRcB1NTtWs6ms0GXj0yXPdgS6Z6en1abSB201z-GrJLAPctY0k7cfwZI8GFvGENpXvtjZICuO1uyqZg_BfHUsrolIQl3IZorYhVbLA6PVPd2-pCcDJbBrlFUuXEaUUXzvAtmHo-brB8sOVpBGMLwNS8BEM1z-FfjJFVmSRsNx0R9KYVcAuFUtdgOD9Fy2eU2WUhLvufLMYYztkWnV9QuTBAKSbU_u5wD8sfOAM8BKIvC36crHo41Mu7W2SNwqZkBRVV0ZGWtQtsYXvP-s9AQW2WVAvgmNCU-54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30277" target="_blank">📅 10:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30275">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBeFeRdsk6n7gNBRhwWWZZGzJTwVKgg3oGrqKpUCOw-hDm2TtOjFs3PTJd7qffb7Kf0fJTAR1pgtEWgiKYgcPHj5adHLVRaho_TbTrJIFSn2zOKdihIiEWCnmLVUOCRSAkDAOZmw1gn2P-REfi0DUiKHa9jdogGsTwK2-i9mwcVFe-ovaaoxOH9vamV_P8pavLcnPiIDT4QrYCyUdjO2ozitFZvI9H9LkTGx0ydFPMtvRQDjje0Wv-hVGL4oqKF2JekKQB3-Fs-Iwacb77F_VYfKQ8BLmurUKDiNEVYLXJ9cwsZ137wACo-Zk6sEU4KZg1kEEJICl86g0mt8w0YHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCFkiE2-5bIgIN9tddfJ--hmG_j3mcYwVHw1o5HxYW-5aJLJMhCWBSpjHITW978zlBSKNH9KJhGzjMZDPX7ka8SDbrPkI46uGjNglrzmXkLvTMqIAr05qy91C2SMFjp3suJ7l9S7VBA8aoKP5gnRvwtm2dNm38Oy7BQQEY9tEb1x3NXcHpDsbf0LsJlBq5sceKZHwjz3FYlGsv2F_kYNbQ79l9O0z3C_kPQOaZnD81_hNJTY7JKR3kUhUR3AB8Y3CLUKMZL8MloDz0cu6vx30K7h_Kij0y4RC_4w0U4c-FjguXfIjxRoQX5x0li0uX7BpJMZA0w0n10jl1WbBAEUZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30275" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30274">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWUCg5QmaHkvsoTVoa7-_c8Qeo10w1auaQSq9rrgv1QVufYpJCKlVIZsFg9KVsqf4hNBKXycPHgb9Edgs02v7DZEft50Dc6ymyiEk1p55cs4tpZ0KEtBEsYmAhnemU3jGh8qVdxb4BL96DAKj9AGXakYORe1ZHZhOk-fWt72s7-NhpMfs0iiRV50peJo6cCbt0gvbh175zGNyglmQToUtLwo0-LgA1bzobJeJ3eb-sHDiBoyNH2FRzbwK9bbs4ZXl0ApRgNr1jTVCDV73V1xlrEFTYynGYzV-CI00DxCR0p59F_VzFGi51cLEG9IQ8v8T0q6Ux7W1pGF_FI2FuwJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30274" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30273">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POms9G8rtCtxaG5Tl-wrri24hJrKuES0O8gw2otGYHALBAQ7Op03kQjWkTUcVRUSePRV0I2E_0vekDHfLdhIjym8LzKvpB3Dy1o9p_OIpLfHRvS1Ev-jXGEqBvr59YEe6o8lRl6mLIZN3OO9KiCxXMdisnkhBbXJ98cVJarzUjHfxdIEkAobaSL3IMehOeWSTdrGVIeu9niRNGvsm12oZnVxBo2t2vVTHA9Fu4QgNHZqzZFBCYW290mmrYxahX1K4sQFxDMDmamJhJzkKjAxebt_ZDMmL9woh_o7Aq4jClRnDdva0M3LkDt5pOJhaniqOHAX_MogKAIQnK93pqld6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤬
گردونه شانس یک فلک
👑
هم برنده باش هم لذت گردونه رو تجربه کن
🤩
واریز کن
🤩
ازپشتیبانی کد رو بگیر
🤩
گردونه رو بچرخون
🤩
بدون پوچ همیشه برنده باش
🌟
جوایز بی نظیر سایت بزرگ یکبت
👇
⭐️
آیفون 17
⭐️
ایرپاد پرو
⭐️
پلی استیشن 5
⭐️
300
💵
جایزه نقدی
⭐️
و هزاران جوایز ارزنده
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r1
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30273" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30272">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3EHlt82Y026fgD_0-K2IyR86chZetenfQM7Aghl11XQ9NRWRTGer1ncqXVT77UrcMYZgol0m7QDRHaL9F1WPuCBXcqyGb3Up1rWNlBXWTjDm2SYTtfHOwywlVR5MVn08cgtT7BHgQjPEw0qmM3oios22WnFoMovFkFxKkrElzflnkNzRHHQL5VPEHfB6o6zYXnQ9iW7j2MuP_GPj-WHSPmdS4R0cqOpaQgy4ChsZQTmWqJqIfdpkrmkVNMaQAn8j4g9D6tUHnQRRUWTtrm96NmND9qzNH-8UBvWB_Sn-vgNc7vCUuca8mKtg_8l-30IEAHW27FrZ7ks5Uy76bbFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مثلث خط حمله بوکاجونیورز در بازی دوستانه خداحافظی کارلوس توز آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30272" target="_blank">📅 10:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30271">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=VLkNNAIZ7aCh-SO_i3GFAVih-ppCaokwxARz4hJcbQUIcsfwFxpD7mhR3AlVxxlqrZz0rKtcfoUQTQhDurFTkJNCPUJSvDnQqq2852G1GluIyn0aybRzRD6BUytv91R92EfhcnS30SqV-SHUyWk3uGx0IpWef8L7vbGf7uH3Gfw8PAdE2EaD5u1eMieYRr8iyuuTuW4ZpOeL4qREbDmQxlGYhmQBVPdFY-YIf4jyHaNHX6jDgbspwo3BLu3nJc_8zr6vZwgwynrbSWdY9wjcc1Aqt8kKaVLhb_uDjoZP7HiCtwntlMlfHBxFpxf6oKYNvyee8LfkhVWFwxzaH_sWviKu1jBOk0Z4IeuM7gnBd_ZRdpyia2kq7tolzxnk3B9Bgi_0gBtZ2OmJdVMo-icGcHiMjwD0sjnoLg1tSui4DdY9R7efgqZMrRA_RZf2FTeacOcBI7-FSLaxcbpmv7ZPUo5g4nnxujbqFscvMzbGlyLjrl6Ipe---Fs9pNACmrYP2gylml8LrP1E8DqRpxd1sNK1SRSEarXV-9TrM5kWQzar-PWiPs1VKWNSSh7spOwOz_ixoys5h3ybVF2GV55Ua5ExbnL_D2t_qUe3JS92pGI1eAmGM2gEOMCInyOOhwNH0MUcGy8AZvU26RGR1ZKIDzGCBy0_-hH0_QZJ6b-bOYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=VLkNNAIZ7aCh-SO_i3GFAVih-ppCaokwxARz4hJcbQUIcsfwFxpD7mhR3AlVxxlqrZz0rKtcfoUQTQhDurFTkJNCPUJSvDnQqq2852G1GluIyn0aybRzRD6BUytv91R92EfhcnS30SqV-SHUyWk3uGx0IpWef8L7vbGf7uH3Gfw8PAdE2EaD5u1eMieYRr8iyuuTuW4ZpOeL4qREbDmQxlGYhmQBVPdFY-YIf4jyHaNHX6jDgbspwo3BLu3nJc_8zr6vZwgwynrbSWdY9wjcc1Aqt8kKaVLhb_uDjoZP7HiCtwntlMlfHBxFpxf6oKYNvyee8LfkhVWFwxzaH_sWviKu1jBOk0Z4IeuM7gnBd_ZRdpyia2kq7tolzxnk3B9Bgi_0gBtZ2OmJdVMo-icGcHiMjwD0sjnoLg1tSui4DdY9R7efgqZMrRA_RZf2FTeacOcBI7-FSLaxcbpmv7ZPUo5g4nnxujbqFscvMzbGlyLjrl6Ipe---Fs9pNACmrYP2gylml8LrP1E8DqRpxd1sNK1SRSEarXV-9TrM5kWQzar-PWiPs1VKWNSSh7spOwOz_ixoys5h3ybVF2GV55Ua5ExbnL_D2t_qUe3JS92pGI1eAmGM2gEOMCInyOOhwNH0MUcGy8AZvU26RGR1ZKIDzGCBy0_-hH0_QZJ6b-bOYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛ مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30271" target="_blank">📅 10:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30270">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=sngtkp5Qym1YBSYvbmdIt7pHsq_C1B5fXBzdhdf4YVgCqDc5acyXQvPns4mIO6eIguPFSrfATS-a7tSBbqolcRW2w_bhDLwEvJrePi35hEZzaiDWmJcJb1cqhWJrcGOi1Tg5LNo3oEjevLWLtoq7Hje3pob7SeFRMZI1lSjYZ6P7JEhUmIF9Z70olN3m5Q8jtlnNbYPU6cvY4A6MspXbxhMIH0c7ifqFLEyvijqn52inAPBLnaUzbKRCNBROktzJzdswDLqA1R_K0GcCEh_9BBIG7e3njqb6Jbu3X_7NiByMFxZehHyAfWi72v1tlcbZPhNsIXbIW05Pmw9ne8JGqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=sngtkp5Qym1YBSYvbmdIt7pHsq_C1B5fXBzdhdf4YVgCqDc5acyXQvPns4mIO6eIguPFSrfATS-a7tSBbqolcRW2w_bhDLwEvJrePi35hEZzaiDWmJcJb1cqhWJrcGOi1Tg5LNo3oEjevLWLtoq7Hje3pob7SeFRMZI1lSjYZ6P7JEhUmIF9Z70olN3m5Q8jtlnNbYPU6cvY4A6MspXbxhMIH0c7ifqFLEyvijqn52inAPBLnaUzbKRCNBROktzJzdswDLqA1R_K0GcCEh_9BBIG7e3njqb6Jbu3X_7NiByMFxZehHyAfWi72v1tlcbZPhNsIXbIW05Pmw9ne8JGqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛
مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30270" target="_blank">📅 09:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30269">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=Z7dqT-9j3v7q-7E-m6ROEIjV-bHUEtkjx2d5oMMTNQoq8M2uqerHhalOB2tsOGCi3tZLSlk7XLE7D244K7ffh7H9uDALOQ9zLsfY-RdrTOWrkXsp4_nyrIEXvCpfPOo7omWDMr8-_HxihTDzqm-XiVINmIm0GflZ2EMRScCdKhoT5h-dMPLCtqW3TS4ucAYluio4C1cFIbpeE3h6BUs9K-ly7UMuKjmcEPO5eiQXnpJ3oh205UFTc9zi9-2N4lTLSc-xrN_JP2qz9DqWN9TjkQJTNbCeT66EEzpDn0oF7N6f-GNsR-x5f27IG5kdQPAZm2A8_V7LtOo6u8iM5SAsHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=Z7dqT-9j3v7q-7E-m6ROEIjV-bHUEtkjx2d5oMMTNQoq8M2uqerHhalOB2tsOGCi3tZLSlk7XLE7D244K7ffh7H9uDALOQ9zLsfY-RdrTOWrkXsp4_nyrIEXvCpfPOo7omWDMr8-_HxihTDzqm-XiVINmIm0GflZ2EMRScCdKhoT5h-dMPLCtqW3TS4ucAYluio4C1cFIbpeE3h6BUs9K-ly7UMuKjmcEPO5eiQXnpJ3oh205UFTc9zi9-2N4lTLSc-xrN_JP2qz9DqWN9TjkQJTNbCeT66EEzpDn0oF7N6f-GNsR-x5f27IG5kdQPAZm2A8_V7LtOo6u8iM5SAsHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌‌های ابوطالب حسینی در قسمت اول برنامه جدیدش که هر هفته سه شنبه ها قراره پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30269" target="_blank">📅 01:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30267">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-ojI5rTqTEJl1-6O8uT_eDMO_393YAl4-qUgRax277zc12_OUWvGt0YXpnKg2E2uLttoEAu7uEAd_kOgvszTax7fLFYTCUb-0Tqeh8OGIBJjvSvILM0-XLjkpiwsu_kUpn_-8M6UJps6BQOFzu1Wx8VGeC-1Afd9eZI-U_-Y49DLbRMxNNOlSp4UbNt3e4b24EnVGq9ER0ZqUWw-JiuuqFwLZ0DUrr02wyEjwvg8hdNIS_vz537P7wWtqyPBEKaejVz3DJdBPu_mdMg8nT-CnU2ev8qTzMig2tLrAVvEenp2g3sxabOOuThD6f8ujK_bxKz09KRN7XWOPrA3GHXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ بازی تیم‌های امید ایران و کره‌شمالی برای صعود به ‌عنوان صدرنشین در ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30267" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30266">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=LPJQnBpYuPah2pvJOtyk6tDW-qIz01ttGgdEYr4gRV2yt9SZoZ2LsNOf4ZxhWVDTiJdZmRQeKbp1i0WNVkSYFa0LcmZjyo_lziD360tJORMX6jceIo5DwOzx7Cj4h8-UhJL5hmFPY3uCZowqXxIoGYngdcWijeg8i5TbYr2u4zBtx4DY0TpPBSm02La5OXMHWQ6P_fAJ2L0DDFL9nD6MG52i0edOnPbbqWIEuKT3ldlQsGyJkF4_VGL0QY33SOEVzQ0Y0b3Pr_0ogHbxqAoJawKkX1qS0-tY8oIEdV7ZzJNmcx5Drygs9HoierxM7cleVbHFaLG63boH4GYEoLqZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=LPJQnBpYuPah2pvJOtyk6tDW-qIz01ttGgdEYr4gRV2yt9SZoZ2LsNOf4ZxhWVDTiJdZmRQeKbp1i0WNVkSYFa0LcmZjyo_lziD360tJORMX6jceIo5DwOzx7Cj4h8-UhJL5hmFPY3uCZowqXxIoGYngdcWijeg8i5TbYr2u4zBtx4DY0TpPBSm02La5OXMHWQ6P_fAJ2L0DDFL9nD6MG52i0edOnPbbqWIEuKT3ldlQsGyJkF4_VGL0QY33SOEVzQ0Y0b3Pr_0ogHbxqAoJawKkX1qS0-tY8oIEdV7ZzJNmcx5Drygs9HoierxM7cleVbHFaLG63boH4GYEoLqZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
توصیف‌های عباس قانع گزارشگر مسابقات فوتبال از لیونل مسی فوق ستاره آرژانتینی تاریخ مستطیل سبز که تنها یک بازی باقی موندهه که از دنیای مسابقات ملی برای همیشه خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30266" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30264">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3H_w75awVsNbH85_Ly9anUSfAlPcxvBBjUahMaxkBwEkPIia9Qt4W4ScctoYsBfmtK0uF-EEu1olu5pc3sg4zlqxT54nW08jX0ZsdNZV6_YGXJ4CoXo19BfbDdXYDMrbs1RkTax5zRSTM5d04gNOVklFPNf8iy24YMASSyytxQ-1uFEr8kV4_H_5bwY_3JU8CHupZR_xLtF6iukN6iBXuWzprdhIdLk_zuiR0GIB9RQlWgBlRjVWvaCiXEL0uAlwNsYhB__3E6r1A8xA_be7xo1Wk6bMpRZ7xouBEsRy3XAUx4UVCGU_hGAwXRBtm7iUFwVL3tUuQyQIUYNok9RCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30264" target="_blank">📅 00:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30263">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=PEu1dmKUkQEB7VjcCG2G7GQHG1jY2h9vl2kL3O46dAbz826Zauxl_GzxEU9Gl-smdceh8oDQ6J-Qll0GzcXjUEYJQUFVKnDj2he3vrqHDBVab4pN4GLsMNCsfpMMv2CYLp05JuoJEvMQmTMxF3w0taUZRj5Nt0-EI1BGiVGTnYNjpUEizIKE1yhvr0_MmqsqVmZLTBPwAJmQM6ymzt6EllygjRiiLaL3KDlje-dcMW0K_IQUZBYFXYCQZRJn_-RMGlhm3NMr-PlLSEPzeP8gp_VDODdynYAfmup7_x7M5xL3VNirhn66a73qDannC9-vbSecbpk5aiTtZj54xCRuEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=PEu1dmKUkQEB7VjcCG2G7GQHG1jY2h9vl2kL3O46dAbz826Zauxl_GzxEU9Gl-smdceh8oDQ6J-Qll0GzcXjUEYJQUFVKnDj2he3vrqHDBVab4pN4GLsMNCsfpMMv2CYLp05JuoJEvMQmTMxF3w0taUZRj5Nt0-EI1BGiVGTnYNjpUEizIKE1yhvr0_MmqsqVmZLTBPwAJmQM6ymzt6EllygjRiiLaL3KDlje-dcMW0K_IQUZBYFXYCQZRJn_-RMGlhm3NMr-PlLSEPzeP8gp_VDODdynYAfmup7_x7M5xL3VNirhn66a73qDannC9-vbSecbpk5aiTtZj54xCRuEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بالاخره‌تابستون‌لعنتی با گرما مزخرفش و قطعی برق پیاپی اش تموم شد و وارد فصل دلنشین پاییز شدیم. باشد که روزگار هم روزی به کام ما بچرخد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30263" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30262">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeArt9pYK9gK8aml4KNH2W2E5T8LURxwIKwBWWilEMVfsXNXimGnW1Btsvm6Sga6Xfw7_C1WH5c_LL_PEMs6iUhMJquROBnXbW1qN2evHp-obheU1dRcCobsBvPMS5s97ODip1lsBLi48M7SAZAoz0KGnRqwnSP3cU6ANzmAusWbEx03G87ZSPeVNNfYdHkWpJ2emhkKMfEm9bz3qvDOMb68yYRlZhTCEkU8zdb9kV6iumg3X0pnvOG48Xr1eRYWtqQOgmC8A0cOU7rD1TvaupFoThfGL1YFznfuUVoapC7yizYowrI3rWGV3JCXrGSmMW29OimYywiqdRstMqjnkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شب گذشته تیم زیر 17 سال النصر در لیگ برتر عربستان با نتیجه 2 بر 1 از سد الاهلی گذشت. هر گل النصر رو پسر کریس رونالدو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30262" target="_blank">📅 00:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30261">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlpmFKT6ow2sFaIsw6NC0gnQLIFxCMVuRK2tWpHtGEzn4R2M5k0X_IAOvTyO1hoQBbS81EJBRCwushu-NojxkzyWHo-wK-w0RMVX6oLNGBaz7IUbxldMK6YMSiPWuF51IY64-diPG7PAK6KEOPQE7KXHy5dfZJqXlZ1kZw0TyvVcvA1C2cziWeBH26GH3tazrXvcW8zk36AOuC6FVYAAWpdpQ-qXkCYh_7DGHswO9bo3TMqq_V61o9hqbo26povild1NeERVLwCNqEUvUC7dJGJdyRPb1lwBk3j4u-UfomUP_kCG1TMIdhXQ5wvoWJTau2saZ_bh_GiCVJsU1btxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام کمیته داوران لالیگا؛ لی کانگ این ستاره کره‌ای اتلتیکو روی این صحنه خطا روی فده والورده کاپیتان تیم رئال‌مادرید بایستی اخراج میشد که داور جرات‌این‌کار رو در ورزشگاه متروپولیتانو نداشت. به احتمال فراوان مسابقه این بازی محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30261" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30260">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJIYSPKzNq5pfaZn8oN4kTSULncEx6k0Du-8xRHvR50f-lAZWw_6bjeURdop5N3QxBSpbjuFxvv-Fj8vMEEQKDOTdVotFF-RAuDA_DBGXu8HpjwKCP9o6JEAwPY3SiRnGiRKIP2MKpMZY5VKouQ3fG2yT2YuLGqYFDzOdplKbrgs108u8fgeoQ1QwbFsIJ3S9elHWx3eY-bzRWYFP_ajM_JAsJCFC1r3jPdn80w7TDeoqXRKSqDKh-rLRLnGCVT0bamws4OulIKqvnEUFpIWVaIEbiA72CmKAPti611n-8DKW3T-1FZlHQUE1tt-XkMAGirkXzZUPaULgUYvb97Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30260" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30259">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
چالش فوتبال دستی بین تیوی بیفوما ستاره تیم پرسپولیس با زهرا خواجوی گلر بانوان پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30259" target="_blank">📅 23:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30258">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R69BV5fdyhwWI20U-uFORHsaz1tX3VTKjbkbp1p7P5cwnHDOrjtxnx-ZMC_ga4TAtt3NzvMr6sgJu2v0lAbckx_vuOOBSSLawimxq2reczlAbcby-sV7X8dO1aAEkmu2LdR6sSn5TTbqyFAj7LdCxOrFXA50ngSLcHdykbOTDpFAez58erHt5eUW0LWtv7SSwDnJJpVhW_7xcP-bfcpV-Ao-9jSoYl0rQDm_7Vd_00fCHsCM1s5Me8s1Whk0qo0quWwEOhp2DBm2L-PiwPL2nnM1AQ4pzcLSX2v3B00X0IHqRv-96ThNJr6IuHSXDx_sj9rl6_XyXEu_LTJuEqVQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
در جذاب ترین دیدار دوستانه امروز؛ تیم منچستریونایتدِ مدل کریک مقابل شاگردان روبن آموریم در آث میلان با نتیجه چهار بر شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30258" target="_blank">📅 22:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30257">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQBa4OBtE5jCxz3oRV9rxUWFj5FvduadPMgcOqfiozt7VmhhFAphIwcJXbw9jjMOcMezlsEfKmvmKNjUh69hxQ3aQFRvDhcUaXLe7OO6nErmYYCLjf84jcYJ4c-FFVE_VuwOQZ7rU9CAX2j6sASDPX78BUzKwWVjoxy6BNZ5pcdp2O9XN2N7Krme-x5o_8BInbm10BB4AJgyUimheferf70CHplvkdrQ4y6Ea3raFXXD847dMkKIqmCBBVRgaVyvaldLGPAYBzF54fIb1PSGhZr83xzT0H6QTncsr8F1zdC3tqs4sbJLnZFlB2MgQrNNNZlUsPMzKDJBr49vAKdAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30257" target="_blank">📅 22:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30256">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=GZD9DGxTFmjhjdSXMaZOmjkRcEOCHJnqqNHygUaplkOvK_csFzF7erMTndHAar-mOceVu60n_Psin9xxtP_LfVaN-DRVYmkWWTSrl5mbWc5z7g8vDKEovj-poipTimix_47KhxkaAIlGLIZRBeVvQNc9c8Ytac0c_eXtyKHUW7TOe9zgGWqlM5x53oD0HjBK7UbcS3iZ_uFzuSQdh8PM0WrrjYtO3KX7ZM4lJm0Yig2GvdxRJCUTsmaGQUp6CUxjWr-KBGxG52AlexfPOKBe8lby6tpfLv0xpB-8_2JV6aOJXRBvlDWP4bKfhMxPX5lbJsERMDfT3OcSw_WA-enG2ZrW_-aNiZUmi_ds7v97bkYmLmJe2tlKKnv_hjWxJ0BpdXlsh_Gh8KN2ebVi3-tcBQVkC9Ig2Dki4iKmMP1TLoaIHKL5tc_yyVSDo15bkBQld3euyRM9TvFZjQLqnbzuK7aEinCYjNoRe-InkxftKLsGpmsOXiGitKAOEkjAMqQdzaSjM2r-dFYInd7p2vr0CEAT_1tPb8fn2SOj385S4eajS191n2mVHYXKUoSA9B_dr6PrAr4wXSdUXvAgCf85TP4VIL_xPlv-DBn4d674TOm4E3_4J33QankYsmxN9_10j_QpQiZwCmzivuX9wS1zDUQNVEa_8MtO3wQ63aZ6Kak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=GZD9DGxTFmjhjdSXMaZOmjkRcEOCHJnqqNHygUaplkOvK_csFzF7erMTndHAar-mOceVu60n_Psin9xxtP_LfVaN-DRVYmkWWTSrl5mbWc5z7g8vDKEovj-poipTimix_47KhxkaAIlGLIZRBeVvQNc9c8Ytac0c_eXtyKHUW7TOe9zgGWqlM5x53oD0HjBK7UbcS3iZ_uFzuSQdh8PM0WrrjYtO3KX7ZM4lJm0Yig2GvdxRJCUTsmaGQUp6CUxjWr-KBGxG52AlexfPOKBe8lby6tpfLv0xpB-8_2JV6aOJXRBvlDWP4bKfhMxPX5lbJsERMDfT3OcSw_WA-enG2ZrW_-aNiZUmi_ds7v97bkYmLmJe2tlKKnv_hjWxJ0BpdXlsh_Gh8KN2ebVi3-tcBQVkC9Ig2Dki4iKmMP1TLoaIHKL5tc_yyVSDo15bkBQld3euyRM9TvFZjQLqnbzuK7aEinCYjNoRe-InkxftKLsGpmsOXiGitKAOEkjAMqQdzaSjM2r-dFYInd7p2vr0CEAT_1tPb8fn2SOj385S4eajS191n2mVHYXKUoSA9B_dr6PrAr4wXSdUXvAgCf85TP4VIL_xPlv-DBn4d674TOm4E3_4J33QankYsmxN9_10j_QpQiZwCmzivuX9wS1zDUQNVEa_8MtO3wQ63aZ6Kak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2011 در چنین روزی؛
وین رونی فوق‌ستاره‌انگلیسی تیم‌ منچستریونایتد این سوپر گل دیدنی و به‌ یاد موندنی رو وارد دروازه سیتی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30256" target="_blank">📅 22:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30255">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgWaqT9Moo19C3zb05Z4RBw90wkQ7tV8XL9xPLDvvFD2_WBGYJqa6E6zXfepTMcPtjUCeAwGo3JUSlP8cJ6EESKnmI32MNFuMg0WI668KyQ07ZKLC8ziameV6MQLnrAi5cMyI2p5fvWZUalbhfISGHOJETGgCUYMexP2EVmA9c-RGhCRGCGA4MzClM67sB6Gfynlqova37pfCVZp_MCR0PU7N120yXv1nGHaJqQgPkGzRm34PCexBga-kv5ANExn6JuBBTleVdGqV3J-3n14m7o4zXbMuvLyKn1xBufQRqYALlDMRay4q7qejkSjAK9heZXvYTEXBPsy7-lWo8RS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30255" target="_blank">📅 21:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30254">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVkQjKp2-wgOOmFnihP5ldPqDDe3fv9Snw9l_ZDW3rpqWrWcjxFPNUsTVGhW4eLkwEC6tyP6QRfARV_bmhxUY-CeD1VZ6reeDbSckBvvaeqr0_cgVxyKFV1TeG31oHY9e56A92yKBv024oziiuTYMmBzkcjrXjbik4aj9zW-HxBL1lOrvTFh8TLJ422LkvoAcuG4CumdimxI5qL0NrME4wqusbWUAIq8PL41BT2GKlv_4jrEFi9YuYBOsx3bPbJTeYWl_PCRDOth_T4T0ZNRwlDVaIdrjbWQmSVjOSJjOUlnvZlk8poLj_vSChhrssS1K_tO33xAcwMl2akvHa4isA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛
لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30254" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30253">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkjQlfqjzmCtThYojhLKm4pQP3KxA22kOYFTvSNC5ASkvqWmfWdB6tDd-6iv5DxZTNLJV05Bp4fq1hVbk5MQdtuWZnQ8LkP4eyliZH2Z00MlRqNfuYZEeWdu7qKSeH1oqozIo0KkB3kxcXEk_6DCqzClusTDnx9YgcYgh1qW2Irp9WBIBCXHnQc1FbUUmv-pzZBwEISNotM3EBiqRLLx3y7ed75NoToVq1fWrmNX_6ozacSxn3MWbN75YL5vP80bmSm-6h7XgMET1SqjVS0j87bUXpx9s5f4leP9LUd-pBvsHCDpJ0gSLlLA-YCXmjGKxrGYS2fdFu-Xb1vlNhxJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30253" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30252">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTJqFga6CVxsNe8y-B0B8s_g_i-ue3m82W3dCfpYt3Sxg67RmYb_e0Dhutw-7sEBa0J9-9uFTjUo3j3AmHoh1R-wvdpY4YR1-WrCshFZ7gi53-CWYBYwujzJ1X9SjA_p24mRAnKHVzmxIjeHaTg4pJ6LuoCo_0mdfnbDwjJ1bSTAjGyYFmW9mfoh5slIzFi5KEWcBG-usOtjiNOzKcHEzWMmxT0ZYaeXcBFB4Yx3rQFgetsLjVIQCSirNrHtRsblxwMGgsZ7Y36djNCK2zF0MLC1Vxh6rhSRnkAnNDCc7ZEDObljb43lyAnRBeefpyqr2snTwn7DCiCQJ_rvnDrycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ خدمت سربازی فرهان جعفری 28 آذرماه به پایان میرسه و با شروع نقل و انتقالات نیم فصل از ملوان انزلی جدا خواهد شد و راهی یکی از دو باشگاه پرسپولیس یا استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30252" target="_blank">📅 20:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30251">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80HxDVBJ7wapiJQR5Vdjf2GVcpvEC_oGfyK5zvY_DXMx9GFxCwjlREEfQt-y1AjEkeQG32GNLWi5yojjeogRpJRdNI2QDPq0W-OuaqrlxgIsLpdAhcK1jEXi4P2JP3owEnkq2YDZgcHqoMYUmqMgwhm42JsZkHRAGjv0g3PZjGDxH8oGDxDYod5Aqn2zZsqIGKFWAPoZf5mnQAdrLEZ4dBKL-SrCBfrcA87D-llFUashTUuPHQsaGQJfAfJ5yyxi318tAAquAkxsWeVOoGriY81CMrID2upLpEvf3CpTR9jxDy5Va96yoCVBvehPpHsfuk3i5P7C-bZjHJthMPg_AkCIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80HxDVBJ7wapiJQR5Vdjf2GVcpvEC_oGfyK5zvY_DXMx9GFxCwjlREEfQt-y1AjEkeQG32GNLWi5yojjeogRpJRdNI2QDPq0W-OuaqrlxgIsLpdAhcK1jEXi4P2JP3owEnkq2YDZgcHqoMYUmqMgwhm42JsZkHRAGjv0g3PZjGDxH8oGDxDYod5Aqn2zZsqIGKFWAPoZf5mnQAdrLEZ4dBKL-SrCBfrcA87D-llFUashTUuPHQsaGQJfAfJ5yyxi318tAAquAkxsWeVOoGriY81CMrID2upLpEvf3CpTR9jxDy5Va96yoCVBvehPpHsfuk3i5P7C-bZjHJthMPg_AkCIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
هایلایتی‌از عملکردخاطره‌انگیز و فوق العاده لیونل مسی درتقابل‌خود با منچستریونایتد و کریس رونالدو در فصل 2007/08 لیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30251" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30250">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=DnduHoiIVAP5KGqfUi5if-_n1Zz4qKlink--FVDjzeRF3FA4usdELjRmCVEQ4XYtWIdhr34RSSxq92Lmm76bGVpHzjk-SmmE2TAK-oE_p5pp0ZW7HudS1VwFCE5Rlc2rgRAvANZnpLMLj6uCH5VlTSFWsjH8mFqv2tzN6fIAo0B-hhKn-VGpHz7WxEB7DyBTdomL73PTyWEhccuk6OwYKPbkzjazVS6GBaQm_IBKO2-6I4OanRtSeA6Ed7XA_4f2uRftxS_lm7FyWNULfAY2wJXHc9-r7FUdiXDMqAxvRtUELAM6BWbx5-IfeWdBOVIxgGCtUeL7E5IUCupXGkmTz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=DnduHoiIVAP5KGqfUi5if-_n1Zz4qKlink--FVDjzeRF3FA4usdELjRmCVEQ4XYtWIdhr34RSSxq92Lmm76bGVpHzjk-SmmE2TAK-oE_p5pp0ZW7HudS1VwFCE5Rlc2rgRAvANZnpLMLj6uCH5VlTSFWsjH8mFqv2tzN6fIAo0B-hhKn-VGpHz7WxEB7DyBTdomL73PTyWEhccuk6OwYKPbkzjazVS6GBaQm_IBKO2-6I4OanRtSeA6Ed7XA_4f2uRftxS_lm7FyWNULfAY2wJXHc9-r7FUdiXDMqAxvRtUELAM6BWbx5-IfeWdBOVIxgGCtUeL7E5IUCupXGkmTz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از اولین‌مصاحبه‌کریس‌رونالدو 18 ساله با زبان انگلیسی بعد از پیوستن به منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30250" target="_blank">📅 19:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30249">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw3JTdBY8YOeCyQ4iBdJVCBKl-ONghY5AFXJtHBNk0HK3Sg2-F_t6LQ3g46sRkIT1I__qtvo8pDxIULFHEdDD4TMmJ812wkRbcfWKBDZ3bfcgHHYPErQGMJxrl9YXOXCkHFfLgFL56tllgQs0_bP10aUt6xlA8wuI6BHC-GDm1J2N7r5G02FqfpUKt3rXFLv1TLc6_-FO4XeZmD50OMoKfL0frl0_vKVI-NzQSa26DpuQyInrxzsex_RckrdywjhSxxd-0kWysMDsQmV_APfRTvKGiDD56wBYnFyMN-UMux_6hibhaQjWB4pAlkWSj7Q7-L8Kqk35sb65ipbfqiz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شیخ دیاباته آقای گل سابق لیگ برتر:
استقلال باشگاهیه که حتی آدم مرده رو به بهترین فوتبالیست تبدیل میکنه. حقیقتا من‌قبل اینکه به باشگاه استقلال بروم هیچ تیمی بدلیل مصدومیتایی که داشتم باهام قرارداد نمیبستند اما اومدم استقلال پیشرفت کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30249" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30248">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=HwJS3YMQP8x7hvn7zSPrzbPg9BiWytKIHYrYLNVt5Srlb4RXYdnuxNXyffqxcFqEPcxSakdPvZFM7oCmgB5bci2yU64U3uZER6fBcec6He8rfH_KEpB94jvlPODOYtRfP2i5O79H1rhfvFdSOWJ7fl9qmudWh7tzByGGEX72NILaQxmCijxI9fEQMTcSw2jX_85ucWVIjzPGz1-BLIggGVGr3mwvptcRIfsc3iQnKk_KZuoRF6AFBNj6Yj8qNIAH2ieOXS3UKp1mkD8PA5K5eQHiYogmZiP0dvDnzNENWwFZ1ka78tWXpaUIyCy3_YvFOt9jGKRau2g1nIKrvEJUaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=HwJS3YMQP8x7hvn7zSPrzbPg9BiWytKIHYrYLNVt5Srlb4RXYdnuxNXyffqxcFqEPcxSakdPvZFM7oCmgB5bci2yU64U3uZER6fBcec6He8rfH_KEpB94jvlPODOYtRfP2i5O79H1rhfvFdSOWJ7fl9qmudWh7tzByGGEX72NILaQxmCijxI9fEQMTcSw2jX_85ucWVIjzPGz1-BLIggGVGr3mwvptcRIfsc3iQnKk_KZuoRF6AFBNj6Yj8qNIAH2ieOXS3UKp1mkD8PA5K5eQHiYogmZiP0dvDnzNENWwFZ1ka78tWXpaUIyCy3_YvFOt9jGKRau2g1nIKrvEJUaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30248" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30247">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKwDTXLl_wf7kQvkmqm-Cs8sCOUs_E6npX_jN2xy6U0MOpYpAgGku3cz68Fwu2yjNF5p5EkfW1v34slRWMk6u3QDjlY-e50xmAh8QkVo0YXVbTa_0l1rYsmZVndWluj367Gh-9m4PtmV6GKuCWij3TdFbXlNXRDJ3mJB1GGqBo42LnSwMNmer-7mk_1HHFAk4s-oBhruNSMbQxGKlmK1eTGHmqIShDWTkytd9njcadc8SMRF7O7_lpVbG6FkULlhttUYefFrcl4nD5GioYp7YOa_9B6hptP9K6QNDc4ofa8lLtAMX7z-FuTp4Jurk0qAguBeJaxK0gPiyUCvH_Sp9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30247" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30244">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTt241CirAY43tRq5r-Y7USbqCZ5VZGuSQ5NdHpMANKQ81xy7WJK0z5BEIRgXFGD2EUDOOHQVkrHXgOVGG4fOyVkQOapdwsJArqtjo_ErC2_l7Ga83Q0eW8DTVGcAHPvuknSo5UPHVM54FOXgYEkWgrF2b7oaYdmDJSeZCn6v1eAgCXql9toY_F8MOXZ57Z_kXcxAXhZIfI_e39q5Sxoobn7Bf1MAyhOUInCCIwZ4SxUl2ebM0FqfvZsoF4ozK0TP_Y1r8lFtVxjD1biIPUyUOCPwTQcosG1eahYSJSZJpHe5J4wIbgL_D_43o_Wt31krCNyUZd8G-NupWtIJMCiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCjFyjNf1XZ5_GxevCZRMzC5Mt0MRLr68GCN2grHHc91d8u7Vw4-EffxgQUONuILSLteD3TtPL-9B1GuCX6phVLrrGigpMHByydchAlJSVuknWLIUPiF12Souoa2u9LXDfWbWMYHKKHBU8BDdK4LcqZ-vYEBfXUapUSb2RUdOinMpzPnNiRuqBVctpjEDt1yRzbpbh1G02066_w9PXC7bqrsXE5P6-uLmeKHQryjKNsYNFWMz4DBUn3s9GVEW7xLBsnEhErEKCaZOlz75Z-SGUlQBYThVPQumMcsgYIrt0IL4_9mEXMQ7Oqg_jQyKDRxI_F7rhg6S-7YuKjR-nv0rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
برسی عملکرد خیره کننده خط دفاعی استقلال و خط حمله پرسپولیس در این فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30244" target="_blank">📅 18:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30243">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrGIrnhSsFMWKyMTC6TEzv19FrQOzQ5O_N_CF2n0OwEsW-JXNwcYkspxqHHx0QBwlBB0cE5U480BHhxRXj1fsRWywAmJ3r007hEEtJfc6BOAYTIDFmo3zvgCb3UYMQPKX47tyPGBEMXPN0lkL9IFpNcAZGff0wukTPBGoQ6lZvhEMnt3fTAAZeMXtARKxOA5ON_NfYWLAKNxmC-dm1FugVg-Egpqcbt-AECVreSE_l9zFLqpg_rfp2kfGJiBO81J5GkFgmHcXXHo03wZosjWkxcj4tBqsYIadjxyA2_YkmbSo8Ti2vARi4AjB1lc7tWsi-_-zA69-VXDieI4rzID1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30243" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30242">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ0GpJlgAV1yTEgX4iMqXaWxdOIUlPdUkFnLecr7uDobJd7I-4fNdfV0VdkqRkc_3ZyHdPJ6g-XZY7VvcC_v10jH2_FAeD0RGQsqW8R0DK-dJpDqKoMz9PaSjqxHO8sODFTEfbF2AsN_lFVgM21w1WHhvPeqChf_kLvR-ECLUBUo4kaE2xtXNz0K63eMZ9TF9JRQoCtNlhG-FT5NoWbYUUylDoW3sBPqDgR2C-wAk9Nk-2PzrehvRreMb687yrRemllZSgbvI6rBo5HPVd06W54CI4At9eRuGsn517dETpR2rObKL7qREmggjPvPeAImntitzWksoyBuhSPHI0-ccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه ستاره فرانسوی رئال مادرید رسما داره از تمام تکنیک‌های نامزدهای ریاست جمهوری مملکتمون استفاده می‌کنه برای کسب توپ طلا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30242" target="_blank">📅 17:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30241">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io0Fvf7PjejCEeIuaw1Uu5TR-lEtABfVpJ72TgfpmCIUYR2P2dHs98AI9UE1ZqKbUt30aodVX_X5v3cNZs758tMybttBYE00Xmewh9saGaPgzIyV_SMmVTJbpQUE8lgxRwAHTxiiL8FhwLCgr75VX4EbgeXf7eLOrXR0ScBCfAJ_Rbdn-KjYK_Olra4VpWsxnOXELBYqLfS3FDRWSl-lPnpUMmM0cPsjdzxkzwtA52jR1Los0PNqfxipchYx8ubdSb7YjlJkbJ5qxGHoo5D-x1ELiPWhim68Q-5vunWs99ymmx8aflPzqbjx7wTBoYaVJMFT851kSTPzDSXIvVABpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30241" target="_blank">📅 17:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30240">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZviw_8hubdsHVNp12BR0iH5mVN7ZpYRDWnvBW_fAcEjbBUjpu91AME_NQGuKRTjEEL-Irqgd6UUNeGMtYr92QCoOJnz8Dbe9Os0Kz5Fjq4Pdr95n7nMpMZQhM8l0RWdxrOm-xhOMFCgMB2-XcT68WGeL84LMAwolz0hCwEC4LKP-xwdvNiSSGCXI2c49zUvpJh9OwiYaiOiv5t-mpMu-_Wpa-oxOvVnId5mJyqk1M1SUiwMMxpfX_gq_zYIT2zfmrrKEFnh9PWRSL5Q9s5wJqWUkeTunpZaspygzPL-eaE7h2jZSLwfSZfTx3UMYJg4p2rXPrC4m_7IQBu2e1kJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌حضور دریک باشگاه در پنج لیگ معتبر اروپایی: رایان گیگز ستاره سابق منچستر در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30240" target="_blank">📅 17:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=V5ch3EjY35VvJp5MPvCy5eCgjfUZgOLsOY1EQTz2l5ZDz86gtTNA_Hk5r4LBVobDYg40pEUImSgpapwo5pU5jHACq49mslHhym8VBfFhQNm5A2Ax6BVBZePyjmL-ja8snar-QSqLce_LyPgiggmP7Kxh1_pgirwIMoK8gfLPW60z6OsR5SSehrSCAs35SSHVzLPaAhjfsNjRHzy7cHlCSMx3AhJGdt56ED5dtrkNdHcffOhvbqZg2GdK-bSDa-9N81y6gIcJTPRIVjgvHvVVIIIdrY8Na-C0OAv6m91R9MtP128NyLnYm-14Sn7k0GoZvwrSPhR_ndezXzu6nQXflA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=V5ch3EjY35VvJp5MPvCy5eCgjfUZgOLsOY1EQTz2l5ZDz86gtTNA_Hk5r4LBVobDYg40pEUImSgpapwo5pU5jHACq49mslHhym8VBfFhQNm5A2Ax6BVBZePyjmL-ja8snar-QSqLce_LyPgiggmP7Kxh1_pgirwIMoK8gfLPW60z6OsR5SSehrSCAs35SSHVzLPaAhjfsNjRHzy7cHlCSMx3AhJGdt56ED5dtrkNdHcffOhvbqZg2GdK-bSDa-9N81y6gIcJTPRIVjgvHvVVIIIdrY8Na-C0OAv6m91R9MtP128NyLnYm-14Sn7k0GoZvwrSPhR_ndezXzu6nQXflA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30239" target="_blank">📅 16:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtyDO--rCqMVhHtFjtdKaKPjojjN9DhkVvr2lQpiLdb-LPzTX55g6a8VEWPUR2zaadE6EePRiI9nfOPSCjKiC0r_J1Qe1NcjFkVkcJEcggPQZR8CbJLGjR2SPV4NyOfNrnnSRlQQZrZCV3zmJnFPIBt37Fb6YMI74bwCsWIifQgkThPvVLEJxOzGAThnOgGA7gzW6ksFl_QVwTtRM0j8AkYfi3ZDSZg8AcoFRNV0itKm9WhwQfscqsOHL6o8wtxD114Eyi6raIH6vzbdEqWUXj4DXeoZmy3EdKnHcc8h6eFd_O-cnMO9IVvOVNzGHLe4BumL9I3xmOH2MG3wqgVjzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌مارکا: جانشین‌ خوزه‌مورینیو سرمربی فعلی باشگاه رئال‌‌مادرید درآینده یکی‌از دو نفر میکل آرتتا و سسک‌فابرگاس دواسطوره اسپانیا خواهدبود. این فصل خوزه مورینیو برای رئالی ها جام نیاره در پایان فصل قراردادش با کهکشانی‌ها فسخ میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30238" target="_blank">📅 16:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=a2amPv3JlqoUGmzT2lxDMFziDa_WRMZdQZgCS5uj0gwd3g5vt23M0oLyon3nNWFUCoslUGiybn_twunJ3h_hauP4O4poh38_-6pThu93cVsnWn_LVu38d3QV_UeBzSFQMT8OpDKjcpFe3p6rYMMdOiCfOudEpPT-m1uA7TBnkBHRm9nVEZAdOPWxp8_Pzg4FyMhMsVwJnlWW1L5E-IFWGNp0K4hhTjrEivuJvuWOPbYSUOWJWrh1ilrWkp2301thT5-NoxBwA70H3KFT76Z6PeXJ5dAHneLVe83Y-MHNaS64EVdQvTE87x6gq1dp1nRlHhTBRoiYXVtOV56hKQjQ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=a2amPv3JlqoUGmzT2lxDMFziDa_WRMZdQZgCS5uj0gwd3g5vt23M0oLyon3nNWFUCoslUGiybn_twunJ3h_hauP4O4poh38_-6pThu93cVsnWn_LVu38d3QV_UeBzSFQMT8OpDKjcpFe3p6rYMMdOiCfOudEpPT-m1uA7TBnkBHRm9nVEZAdOPWxp8_Pzg4FyMhMsVwJnlWW1L5E-IFWGNp0K4hhTjrEivuJvuWOPbYSUOWJWrh1ilrWkp2301thT5-NoxBwA70H3KFT76Z6PeXJ5dAHneLVe83Y-MHNaS64EVdQvTE87x6gq1dp1nRlHhTBRoiYXVtOV56hKQjQ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعریف و تجمید عجیب و غریب علی رضا علیزاده از نوید عاشوری بازیکن تیم گل گهر: اگه زن نمیگرفتم میاوردمش پیش خودم باهم زندگی میکردیم. عادل میگه چرا تموم مهمون های ما اینجوریهه.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30237" target="_blank">📅 15:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30236">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4IsjKhSBTpNBinhKTWDLkVZ7AY1EWLWTPGRk4D2rEZr-K4aywPiah3j-5JljUEu4rr3_yXMKRmEFiex0r8x1TkiJWnYnU2j3YQhonJCjYGVKf5_Wyx4n67PDNBq3QvI3JY5hsw2lD7kwYtD4Y8DDfPOlq-gDgPE4MuBH1MZDdWW2ew9518nr-tYnPuPv4cL3wrBuQc_aJuLi5ha8c-VoSmujDiWlRIofqWNqqPQC3sBNWvRPNJBhqlYIIzjYxcHMYMQ7kZWPXnhk5OAGmuTj1LW55AnhabqPwakwdbTFCRxzmpEBZTzjJjrx5R7WghoosCKsssQhFSbN6FVdIORsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
درشب‌پیروزی پرگل و چهار بر صفر ترابزون اسپور مقابل گالاتاسرای؛ محمد صلاح ستاره مصری ترابزون با ثبت 3 گل و 1 پاس گل یه تنه سه امتیاز ارزشمند این دیدار رو برای تیمش به ارمغان آورد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30236" target="_blank">📅 15:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30235">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emDuzrOqec-Q9U0HpKcNqjjmE7ZvIyqhiOi_U5DAgSA-0QRiXRqvjM6oTdn1_x8p7DIJvRHo93FFD_5BXlFoKPZru0FlRrOqmcSauxvFezYWr-fgar3UTISVYZbAFthtdZ80gpCta9ixEmQG26pUyprwYVL12H0dzPwf5S7nICtuJZTQV9gR61J_0PBUgsi6nuVnaZVcT8O_VxLWjr3lVVoHk98D3crCtIzhrvrZ5nr_aFmEv_m0QCGCF3qfCXRjktVQGV6g7ia_gouzwP2lSOi20FmWBdMjA8n_0grIZVl7jTQzX0bdhhO6Kjn9HoiLO7xZUkkJJs3dzH4yVqBSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30235" target="_blank">📅 14:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30234">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=N1VdWEYvIoC_G3AKHZ6uAkIgaSNPVvcFQcv0WDw5eNQ3nqOmzj9hd_8Oj0T1NufD-FdV2mFZ5ZI_yQZtwuA4059TbJNO5eZosodiahrZ4ZOrXab4oFdb9edvd2CZB-lMuofcBfZvr9igFXXC1CNzv_r9EUsYpcs6Yhjig8wbXkHjpcFUEFMEskW0D5Oi3ButWRyTGuGllrPhV6zi7M6p1-j-gsmC6IyCS2oLjFyZ_pQ5sfliuUKA1Jj9wLC0QZPhs28l6sklZV180EFOJHvTaKhgu9OZoNspz-Bj98HknxXECdAUNcUEl5tjBunEHFfC9Au0n7sqK_ykBSPJdVHA9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=N1VdWEYvIoC_G3AKHZ6uAkIgaSNPVvcFQcv0WDw5eNQ3nqOmzj9hd_8Oj0T1NufD-FdV2mFZ5ZI_yQZtwuA4059TbJNO5eZosodiahrZ4ZOrXab4oFdb9edvd2CZB-lMuofcBfZvr9igFXXC1CNzv_r9EUsYpcs6Yhjig8wbXkHjpcFUEFMEskW0D5Oi3ButWRyTGuGllrPhV6zi7M6p1-j-gsmC6IyCS2oLjFyZ_pQ5sfliuUKA1Jj9wLC0QZPhs28l6sklZV180EFOJHvTaKhgu9OZoNspz-Bj98HknxXECdAUNcUEl5tjBunEHFfC9Au0n7sqK_ykBSPJdVHA9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30234" target="_blank">📅 14:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30233">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWM36Zj8GoG6KjuVyPs8dArZooTCGh0RFwwwiQcxr3ltptg5HSRXpa6TdRq3wBH2aDL2KtnMhjlUe4JqoidUduJeFFiTXH6w2EAI-M2fzQv4HkdXhTz4KVqSf2hRm1VpRo5LbYJwsUEZsTjlVeY4LACMbHWee73b0tZxHemHvn1-tvomrRVu7Uz8IxmMr24JMfw7womUk5RU375dOJcqlE7CwWcYvhuKzAmHTvMrVp2Kgx0BOfJqlan72ZMaD1EqHY31xpOgBzFviy1st8guWrJRSGGdoulfM63C0rz2HZQwwvP3GjMPHp9NaVAHCiacmPdzmtLsJHrEYlz_PpGEpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👤
#فکت
؛ آخرین بازیکنی‌که تونست تو یه فصل باپیراهن‌باشگاه‌یوونتوس 20 گل یا بیشتر بزنه کریس رونالدو بود اون این‌کار روتوی‌همه فصل‌هایی که برای یووه بازی کرد انجام داد. از وقتی هم که رفته هییچ بازیکنی دراینمدت نتونسته‌ازمرز 20 گل‌هم رد بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30233" target="_blank">📅 13:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30232">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=aYhooqPpaAY8kuAclxgyymWt_ZGg8MsTzPJ_DK3VPz3wI19SWWZKVncVf6ZlWNodr4lgOv18TUmOOC0S4WgaOohJKcI1qfJjjYOxHPBTna0mIY0uKD_XAfiuHYkjYKc9IgEZtnM9SGsqzHOyecu2GxC-oLMto9mlIJLZrLx0Oe6H5YeIvLdei8eIXqR9n00BIRq0tfVOo9lLHaXyYGuLB2qj3x09JwDezXXV3cJjTLUuiwib19SMQMNYvxuKSesho3JbDoygfIBby5gPZCAUaf_0eEsOFxaCCjfNaCBlSZWUBpG1jtckWnNLdoyZDw5b0muDikmLA4fdiODGX74y5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=aYhooqPpaAY8kuAclxgyymWt_ZGg8MsTzPJ_DK3VPz3wI19SWWZKVncVf6ZlWNodr4lgOv18TUmOOC0S4WgaOohJKcI1qfJjjYOxHPBTna0mIY0uKD_XAfiuHYkjYKc9IgEZtnM9SGsqzHOyecu2GxC-oLMto9mlIJLZrLx0Oe6H5YeIvLdei8eIXqR9n00BIRq0tfVOo9lLHaXyYGuLB2qj3x09JwDezXXV3cJjTLUuiwib19SMQMNYvxuKSesho3JbDoygfIBby5gPZCAUaf_0eEsOFxaCCjfNaCBlSZWUBpG1jtckWnNLdoyZDw5b0muDikmLA4fdiODGX74y5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30232" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30231">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTImJLELp3Ah3BCLP5uaUYPyONSHld20bIhR-gUm0GM0whmJZ_uYLWoXWO2gaHZu1ABJg3bNkPOJ25hfyJRQFUOushMc_SBIQHuiFhLmnNjwzX0YRTOAaMtXzMJf1oofCbsGgvhSm9tlpLZM2ryD3rU1C4udBBQ0wyfhYCfkGGK6OhWjceHgCAp_IeYDK7M-RjTBwb3VHQ2_nThScvr7sZxni4OeHv5s_xlfXgdCQpnwfpMoWk1sbI4njyH0FzV2X3t-0rwcvIXoAZPYzJnsk9lTgP3DKaozjD1yoT2MpwzhCOM4hNM2D2aXKCR8bJakQUPAPckRPIvaNIv94GIYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منصور عظیمی معاون ورزشی باشگاه تراکتور که ارتباط خوبی باستاره‌های‌ایرانی و خارجی داره بعد از اختلاف بامالک‌تراکتور از این باشگاه جداشد. در طول سه سال‌اخیر عظیمی‌مسئول‌مذاکره با بازیکنان بود و مذاکرات حرفه‌ای او باعث شد که تراکتور ستاره های زیادی در طی این چند فصل جذب کنه. هر باشگاهی عظیمی رواستخدام‌کنه از همین حالا نقل و انتقالات نیم فصل اول رقابت‌های لیگ برتر رو برده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30231" target="_blank">📅 12:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30230">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRKu-6Z3ND9EI3JZ5Doou6s6tTDwlwV464mNiD4PfqXVTzcL26m5hI2oh3X1mojRboPvU9pMBiCvKIXRFs3u45PrqN5KAdPY9FKW5KfPwbxktkNyZSz7P-eJGExgvtW9XXw7HO03mchFpQDU-RvOfrGLQxqGBuUae3h6J6rU4JCfKQZymtH_sYH6JdwWtP3I-gFNTlDN4vBLer8aK9ZReTmu1OAvAIQu5JzxeajjdLkwBCqKXjtub9cNc_hdznrPWFgm4sS1tXXG3tWh3i5XJWMs0IAbyjSe0VcF0Cj6zZIdN-bg2KD70U2vfYJF2khD9a-mXzT1yKo2NcxFntNcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30230" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30229">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول‌برنامه‌جدید و فان ابوطالب حسینی برای‌حواشی‌فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30229" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30228">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: توپ‌طلافوتبال به بهترین بازیکن دنیا داده میشه نه‌اینکه‌بدن به بازیکنی که فقط 80 گل‌ زده چون که برای‌گلزنی جایزه آقای گلی رو میدن. اینا خیلی‌ متفاوته! بهترین بازیکن جهان کسی هستش که وقتی به عنوان گزارشگر یا تماشاگر بازی رو بخاطرش میبینی لذت‌میبری…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30228" target="_blank">📅 11:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30227">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utvyYo3IloR0KfptJ3zy_QGh6LEbLl_Y9SrFf0VLzLciGWIaw8vNxCvXJSyaWktLwyhb1RV1QAhDlHxXDIWd3oj96kqAfs1MhCUaoTT5jJy5cGUHunkRjL_1l-K83ei0fqhq0z2HkYXg7bVfEviKjb2SYVNaktGIYkWF83SEEjNo93EpYWGR2tywZ4lGHAzkCcVsIbTTzi0-kJoTSizjOmLDbKmSifFJ6IhNHL8IuTSDcN-JnyuY3bLRR9_hiEhJc0lG7bpp59HpbKaocob9k64KnGP8i-_hD5DJsG3VK_U5LiN9ON0JYCA52XZ3TsWJkIOjNfcTQrW-MoBm8u_Eew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
مسی درتعقیب‌رکوردی تاریخی؛ لیونل مسی حالا تعدادگل‌هایش‌از روی‌ضربات ایستگاهی را به ۷۵ گل رسانده و تنها ۳ گل با مارسلینیو کاریوکا، برترین گلزن تاریخ فوتبال از روی ضربه آزاد، فاصله دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30227" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30226">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇫🇷
ویدیویی از اولین تمرین تیم ملی فرانسه بعد از جام جهانی 2026 تحت هدایت زین الدیت زیدان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30226" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30225">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=iYauBD2E93WXjLCsNGWxmBzUl8Oti5PbpjTOmKVmReZEI-E3bKPYKIP0HRBtSFsIYsEiz-AEybw-gRw7m7vQsQW-NHGsYo0jSeB-ms89JSRbDOur_yzrCNrur2fjyYn0MXdvt-2UzOn7VDPFf6cLPbFxJfZkyIZ8hTAbSSZfmoawAlhGL5Q96m6gnsa6jeiVCXBpx6tM932NFwnsjuVd9ua8mhxRQuP98HydNtIcY49xH-eJhaF3_xsxmQ3V_6n3yGNsXHP4tz4JNQPpVos1zV5dFisQ_KWDEbXddApDJp0jieG3HGGP1aOsCVeKdB0K7xjqXzsSUIjDXF6exCWtcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=iYauBD2E93WXjLCsNGWxmBzUl8Oti5PbpjTOmKVmReZEI-E3bKPYKIP0HRBtSFsIYsEiz-AEybw-gRw7m7vQsQW-NHGsYo0jSeB-ms89JSRbDOur_yzrCNrur2fjyYn0MXdvt-2UzOn7VDPFf6cLPbFxJfZkyIZ8hTAbSSZfmoawAlhGL5Q96m6gnsa6jeiVCXBpx6tM932NFwnsjuVd9ua8mhxRQuP98HydNtIcY49xH-eJhaF3_xsxmQ3V_6n3yGNsXHP4tz4JNQPpVos1zV5dFisQ_KWDEbXddApDJp0jieG3HGGP1aOsCVeKdB0K7xjqXzsSUIjDXF6exCWtcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده:
من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30225" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30223">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619db5893c.mp4?token=N0pt_F6CGqm9jJCYvEm105c1uKr6o_Z43nrWSv4f4EtS17tNmsPmQ6U8vlZbhIMH_I16nXGahaVkFcmWdI1__KEyauO9QWNyCcho3FZhv-0VY07Sw-nmjgyKMAZMryTED0yW9gh7aWqQ1tk1a-S-6Cmv40Urmau61DnFlswyzkVIn_u7rk7vAR4lB8oIWHmHbzQqF0D470xHz8aQPYbHu1cq_qdDnaKOiNSIJPmUJAg0YMtjCOFGcS4CW-ZoGSkLGylmY-m0FDl8QQtWobh3HcXY9UuT6JrfwY2i5TH5bHXzm0YiRi-ZJTABdlUT-Er1qSG9ivtxpecRSSgdidvW_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619db5893c.mp4?token=N0pt_F6CGqm9jJCYvEm105c1uKr6o_Z43nrWSv4f4EtS17tNmsPmQ6U8vlZbhIMH_I16nXGahaVkFcmWdI1__KEyauO9QWNyCcho3FZhv-0VY07Sw-nmjgyKMAZMryTED0yW9gh7aWqQ1tk1a-S-6Cmv40Urmau61DnFlswyzkVIn_u7rk7vAR4lB8oIWHmHbzQqF0D470xHz8aQPYbHu1cq_qdDnaKOiNSIJPmUJAg0YMtjCOFGcS4CW-ZoGSkLGylmY-m0FDl8QQtWobh3HcXY9UuT6JrfwY2i5TH5bHXzm0YiRi-ZJTABdlUT-Er1qSG9ivtxpecRSSgdidvW_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد ضیا مجری‌سابق‌صداوسیما که بعدِ اتفاقات 1401 از این سازمان اومد بیرون درباره خداداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30223" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30222">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=GLVialAN80yBbMC_NNJBtdjongaHQ_r1U_RWsP76pUTvB73yU00R4UPoTOgIsJ7AkA_sFosicB7y8ysBNnoVWrm2JT6fD0DofnTUQlrco4Ux79tFCwAI0gr1NGNSPrBlLRWRMlAE2tZMJFvIs0W9bDJjRDBfl6yXORwEF2NGA4eL5dFVUfq1smyC0ec2Ke10x-Lgv0kuk2v3DG2KVgaoMtWTPEsH4S51_6zUvTMzJkkKRn18b_T-wrbXDucvKUem6HlwWgIZyntZpMQXhtO6zUVmokVUFVnSA9DBIwINnRXkF77VBeODkAgPFBzgqu0XEjSammcirWf578PCTeQ73g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=GLVialAN80yBbMC_NNJBtdjongaHQ_r1U_RWsP76pUTvB73yU00R4UPoTOgIsJ7AkA_sFosicB7y8ysBNnoVWrm2JT6fD0DofnTUQlrco4Ux79tFCwAI0gr1NGNSPrBlLRWRMlAE2tZMJFvIs0W9bDJjRDBfl6yXORwEF2NGA4eL5dFVUfq1smyC0ec2Ke10x-Lgv0kuk2v3DG2KVgaoMtWTPEsH4S51_6zUvTMzJkkKRn18b_T-wrbXDucvKUem6HlwWgIZyntZpMQXhtO6zUVmokVUFVnSA9DBIwINnRXkF77VBeODkAgPFBzgqu0XEjSammcirWf578PCTeQ73g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس‌سنگین‌ابوطالب به خدادادعزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30222" target="_blank">📅 10:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30221">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMXHYOeVeb1wJt3JwEi2m5tOzPj82jtXXsKcUKbyJKYcsx4SJR6M2xeM49fyME6x-sABvxHL6fSj-nvb4-KVprEJqlAg1609pc9MiSZfVoJE5YGmqNYmdY8xdnOGR-EpXiZ8P7iuB2bus6nLfqXQmaz5MKnyd7i1gaKkTdh1eo5Q3B_e62f7x5-f5h3ZrdtBxxvWbqSWT0APsYJDdvDU7RLhPc36N0FxugXvL8eCHASdTOhtgJbh1-4wIAmvgJFOmtVcndHUjmxe88ak7u165i50fzYagJLwfZIa0lUtJmDy_ziE6Nv5r-3UwGTf4ohPSjBMgR6CnezRyD0n__l2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از علیرضا بیرانوند در روزهای آینده در سالن تتو کارها. این‌بشر شده کل بدنش رو تتو میکنه مثل بدن امیر تتلو تا بالاخره معافیت رو بگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30221" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30220">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CulxWW9I0j2SHaT48nzx3qARiVv9M10sGPiZduy12vNVT2PiGdsOVKumWrcWmcPDvR6XGDQxE2IkknXL7WuPryVLMGeXv70ACY53jMBndXRxLMwyYprU5ERfmWda5M4uXa-ih6wpHkU8EORqATPR0VVQNhq2uxuPdW_07jDa5A9a3-nE6ho2eImguxk_hfF3Mne_O2CNq6FEQobEbe6S-NDMLwG5rUwO5Nwjp7FUmLX0-LsT0rGAVOZ5cZBU-KEbNPYQqq0p09dgYe0EmiViaC-stYSgQEYFCYDP7Uddda0mAWQijx7_XUiJntTJS54srEBOg13xSAkFyZqwbOld9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری مدیربرنامه‌های یاسر آسانی در تایید خبر ظهرامروزپرشیانا: همیشه به‌آبی وفادار خواهیم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30220" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30219">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=lfGoG-ghErTX2AO_762wwrq0DwnvskFwj0TY5OWmVAmYjTeyBok18HPgNvCgiaDO8JfKF03pOEsaXo6Va76qRdEkfgknyMms2bmsPbLWPK4Osnu6kpMzGo4FIStvj3URTIRjIUnto4suwm_q-iLyUFtzajprHLJTLGclukTQcHnK0koaoPndRHhF1k6T-xkH1_G-PGyK2kaOfiausLnfqPJ22Tmfg2LopOJs-M3pcp8A0fJCa02applQLnqbunYEPCkqw_dUSvFjnXP_rjtvjfm6kaSSAlGetoA0QBmKLvCByt80ZOMuiTXpjIuL887-rFHWRObLsv6yir1OlVzDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=lfGoG-ghErTX2AO_762wwrq0DwnvskFwj0TY5OWmVAmYjTeyBok18HPgNvCgiaDO8JfKF03pOEsaXo6Va76qRdEkfgknyMms2bmsPbLWPK4Osnu6kpMzGo4FIStvj3URTIRjIUnto4suwm_q-iLyUFtzajprHLJTLGclukTQcHnK0koaoPndRHhF1k6T-xkH1_G-PGyK2kaOfiausLnfqPJ22Tmfg2LopOJs-M3pcp8A0fJCa02applQLnqbunYEPCkqw_dUSvFjnXP_rjtvjfm6kaSSAlGetoA0QBmKLvCByt80ZOMuiTXpjIuL887-rFHWRObLsv6yir1OlVzDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی‌هوش‌مصنوعی‌از قهرمان فصل گذشته لیگ برتر؛ رقابت بین دو تیم تراکتور
🆚
استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/30219" target="_blank">📅 01:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30218">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnOO8hyy1bj_oOITWKxIXyNrH8GFpmJ3TIAW8qsv6IykcWOGsmzr66rSQK-Qp2EL8YQaJ77FbpVtI0nQYssFnu512muoSzuR9pCdvTZdn-pvAFBUq8dzBU9rVTO-PYurczSPI2AAcg685ODQOz-aplj69YprZStz45KFCkY_kWhqg62j5PHxP_a5SRaGOCgxzhVTh7508fujVC3nM82Eij7EoIcUEUbPkbVSIhNMuKGE_wV8c-M4pgcPQ8DTqSYDXtP-zHQB_B1pLRTzcVhPZnlGMbEPKah9Sue2PyVvSNgAUyf2y5JJtx6FP0LzbtrJZdCaDIA5SjQKTG4NM7_vHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/30218" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30217">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCAl3JgeTaFr-AzrjRJcnmNuFdPejKVLyQGctzt2z3ivBqNxdqVJlGC5NIxY3QoVLyXwsMBx--Q3s55CZkT-wHPY8hALdSOy0YyGyeVJz6mLKMReFm5UNKcplDC78o5xhkzZ90naCB1QKL7Szr5tvH-hBm57ktmOnNV2nRxEZgPb-VfImGqme4M8jRiLGkpjhnYYSxgCcp8hoO7SWU5nNhu2fi36YZIBKPsi_M0AaIRTojTxlBGz0daZFFfiFHKIbhKAqfxAF_8lsi1n4TecY1rOti4TI-yIJhk9tTtMpo5NvaWDm1xSyQuMIhrL5rf8CfBoipEFOAdXbDUPj55Taw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها: رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/30217" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30215">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30215" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30214">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=rPoWKnNok4wao_eN1UMFD2dpCiiO914o0g4FJwMqNYj8n4UNizhcHVkzhb8qobekljzf6sNBXKK5Pqo18sn8EpXaB_1BUZAuTFemuzsLSPUca4ghl7isTeVH2TdPm_DGnvj0lLTV7AI-1JBoVMF37AKczwuAz6Qm9EeA3xAhaQPkPL2wJJ-Uh5EoKgP2KvMlD6rkCpbFIq-5Fe-ypTgehBfdx0SJYuVHykfDDs_FYG_6Ue6DK1SOQgpVB9F7KciEJ528G8WXSpj7O-JAc--l31VysQeCSzycl8TFky9VsGfHux1uZ7GETVYQn8E5GFA6wMzkfcN2t95kC8Nu6D3dz7tBk6QineCg5vBwFWDmJEYRjopUtojyjtnC-UN3d1z4RPKPS8lkBcMYUDGEnXUMnnMlUEXM69DkpbVagrpgNxeuqGWQb5TTZhCgUAE2_0KQ0Jen5M4eo0RvS_Hw2KYkMzw_KmjJdeSnVFGXU5ZP_Kpt6EoutKHMGXQKLAt-8RAgcqPVxytudd99PlnCv7zGlhYFS1bpESwdBO6Cs4lS8faTy73wC92LvEAIVYDJ8WUH7lp1n4faf3a2l6tz-8mcBhfMCYpi2EIZIbfwfDi1WAW_e9e7hUniZzN1HYewpAAjV-wrMekr8QIFWtqxSYsrr---m9UzPCPFsutg0u4DEjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=rPoWKnNok4wao_eN1UMFD2dpCiiO914o0g4FJwMqNYj8n4UNizhcHVkzhb8qobekljzf6sNBXKK5Pqo18sn8EpXaB_1BUZAuTFemuzsLSPUca4ghl7isTeVH2TdPm_DGnvj0lLTV7AI-1JBoVMF37AKczwuAz6Qm9EeA3xAhaQPkPL2wJJ-Uh5EoKgP2KvMlD6rkCpbFIq-5Fe-ypTgehBfdx0SJYuVHykfDDs_FYG_6Ue6DK1SOQgpVB9F7KciEJ528G8WXSpj7O-JAc--l31VysQeCSzycl8TFky9VsGfHux1uZ7GETVYQn8E5GFA6wMzkfcN2t95kC8Nu6D3dz7tBk6QineCg5vBwFWDmJEYRjopUtojyjtnC-UN3d1z4RPKPS8lkBcMYUDGEnXUMnnMlUEXM69DkpbVagrpgNxeuqGWQb5TTZhCgUAE2_0KQ0Jen5M4eo0RvS_Hw2KYkMzw_KmjJdeSnVFGXU5ZP_Kpt6EoutKHMGXQKLAt-8RAgcqPVxytudd99PlnCv7zGlhYFS1bpESwdBO6Cs4lS8faTy73wC92LvEAIVYDJ8WUH7lp1n4faf3a2l6tz-8mcBhfMCYpi2EIZIbfwfDi1WAW_e9e7hUniZzN1HYewpAAjV-wrMekr8QIFWtqxSYsrr---m9UzPCPFsutg0u4DEjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منفجرشدن عادل از حرف پوریا پورعلی؛ عادل پرسید مهدی زارع تو حموم چرا اونجوری شد پوریا گفت من و مهدی باهم بودیم که اونجوری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30214" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30213">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIEvecFVkNC50HT-88Sw6NPXPRAaUsffVF8BSdp7XQ3amWDRksi43XE0UEOT9Ord9jfzsScgV5X7unVYsxvXLT6RAU90NU-Cylf-sRygZPJ4O_okTufL45Qp3jFdstCyXDxK077HRtoM_yg_SSnBDwQ07WItPsO6rhPaIWro28QD0QGmzObkS0BZTwZwvoNlVYpTuSx8BgOaRTBBKa0WMGHfUqxGnFVQ1fJwh7jmJD8zeWxOA6R-pXdA9UFVKhRDD1rHa4Cl7_eseJ2uKCRNW76qh9OjQ-SEx_6WeAj_ZC4r4BZxf6ekOXGFqYxHJ3-pjsY0AKMtk50Wf6ndHvkeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30213" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30212">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGcRq9xRVr5onlqIaekUbwiVu9kThlLJHZxaTJWpXeh4aKptKpwi-ScGXL7ft3mmMw0pW6LyUpHfJk5rchrh8oE0KcCmqZkMfVUvDGNYn3ERTXrZFpbZSBqL7lv4HpvqQs8ajxaIo7Ih7afm4Eyu8MdMOUHvXweAO3eAqUTbNu3NAibuiOxUXLm-kzRJrbdURUcWrvg3UUMV33InNJXbtML-u0XQqLVhn0Q-d4U1FS1j6Jzo_VmooyzBiygJBtr4QFEb-H0umm7IsqPpx1AG9gu806vXkj_YdVx_OLZ7vhHZEOysxtPLCt6mkUM8JnfKZRV9aTWT9j-E6JcCWR8iYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/30212" target="_blank">📅 23:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30211">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsM1KTYCBQfDesssMpzgYbf3C8aomi-cssrHFoNow4mGTeTZSKOzlBDv7UW0sXc5dUDm0Fs4_tjg-Hupc3TvIgV7PWIsBn0rDKo3E-lgzIWYb4AhkFFfvVZ9jFsSXPbJgejzGahbHR9lhsCyfiT0smK-sLfIpDp1bOYE2UQ7V70uNWNNVm2hBzikXfsPQO3w1Y6dZ2WPEye86M72rIgZC-xXv10qsoVrWLrV424QnjS2E3LTIDKt4akuTeDs1MNeXJfYYMp0NS23CpD601WSRmxfNelTg7v0Q1k4n6axzo0vFDNDHEbxgXRf34BZl4bcbEnCVDJYw8h4w-wcwi0uYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/30211" target="_blank">📅 23:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30210">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=Py26OI54OyL_BMmeDl8TFR8Tc4UvkoRfnNOriJh01AMc4wqVguqrJfPSDnFhq17SUv0_FNpC2XmP-zsWztlGigiDX_ypK80cJna6UAWCSfYIBPpzwa2Hv1t9ecOAHKpfECg2ce67L6Tb74HAmxXZUVvGmPDjBcMnN8q9mlV8vbe_hB5KCTKsy3kXyU4s6IyncXMvBfev4WrxF5tiUtVjRXHb0koL9wGGRej3rHrPOhBuXA1057gZOnWsR4E7ENx-AlFwa8VJhCndbGdG6iAxD_yrnZOHDVBI0AreVDOqVJQZWY-Ltn6XR0Wk56a3bCMdgmgSiKzxCJM77qO064GSYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=Py26OI54OyL_BMmeDl8TFR8Tc4UvkoRfnNOriJh01AMc4wqVguqrJfPSDnFhq17SUv0_FNpC2XmP-zsWztlGigiDX_ypK80cJna6UAWCSfYIBPpzwa2Hv1t9ecOAHKpfECg2ce67L6Tb74HAmxXZUVvGmPDjBcMnN8q9mlV8vbe_hB5KCTKsy3kXyU4s6IyncXMvBfev4WrxF5tiUtVjRXHb0koL9wGGRej3rHrPOhBuXA1057gZOnWsR4E7ENx-AlFwa8VJhCndbGdG6iAxD_yrnZOHDVBI0AreVDOqVJQZWY-Ltn6XR0Wk56a3bCMdgmgSiKzxCJM77qO064GSYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/30210" target="_blank">📅 22:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30209">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=Cbml5PvWKTOJ2jRG98lk3b_x4mVqTXrxMo_S4UU_GIjdxD8uRT1fX9TDaVNWMu57eQcqDI-tgIMqnOZ8ZWwCReQT-10_66XLs69Bs6IKSH5MtnNcrHg2GyVse1-dcYt78wQ-x-X_b2tymmtreDvL_PsUW7yOS6FpwWjsoyz4DRH3yIMuCivc7vPXCuk7pVyRly_rKBOyhHEMvA3cFTjI5hDdJBTadYaOeem-ix3RqRQFPA9etoCwbN-EkNf1Jl8691lH9NNemAiOS-IgjcRwHdN8g2U7Jvpjydhh6kHyB_bD4L7tvyMonv7jeBkerwdOSz7f5G1mm6JR43ecuX0ZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=Cbml5PvWKTOJ2jRG98lk3b_x4mVqTXrxMo_S4UU_GIjdxD8uRT1fX9TDaVNWMu57eQcqDI-tgIMqnOZ8ZWwCReQT-10_66XLs69Bs6IKSH5MtnNcrHg2GyVse1-dcYt78wQ-x-X_b2tymmtreDvL_PsUW7yOS6FpwWjsoyz4DRH3yIMuCivc7vPXCuk7pVyRly_rKBOyhHEMvA3cFTjI5hDdJBTadYaOeem-ix3RqRQFPA9etoCwbN-EkNf1Jl8691lH9NNemAiOS-IgjcRwHdN8g2U7Jvpjydhh6kHyB_bD4L7tvyMonv7jeBkerwdOSz7f5G1mm6JR43ecuX0ZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌جالب‌عادل‌فردوسی‌پور به برگزاری دیدار دوستانه شاگردان امیر قلعه نویی مقابل ازبکستان: دیگه پدرمون درومد ازبس با این تیم بازی کردیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/30209" target="_blank">📅 22:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30208">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3DmbIgkc4FhOc57jirfg77yp-vjOSJaIy89ONJStyqjOoerVbj1g1IbPde61E71HGiu7gjuZOxjvk30Rs8NZpj6d52F6NLxP5weHlEIRUcbiEhymVcXxqULqqCl7pFEevO_9NOHqWvZzCs2Fy_IBQGi3EsBkHq2qJD6jJPwaH-OvevfZlaGMACaGCLhIkuDrThDsBn47sAylpOa_ooJqznicFQ4tupOnjIVueN9K428QVPEje8_OKTWMmJu42onT8ny6WdbPTsVmBeswvnPIWKoaEM5ygsJ8BOpl47t5OuJuQgReOBt3v3Rbkit34IhFN5E93lKeJemKWuPa3cqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال2022دورتموند هالند رو داد منچسترسیتی سال‌بعد منچسترسیتی‌قهرمان UCL شد. سال 2023 دورتموند جودبلینگهام روداد رئال‌مادرید سال بعدش قهرمان UCL شدند. سال 2026 دورتموند آدیمی رو داد به بارسا، یاران فلیک قهرمان UCL میشن؟
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30208" target="_blank">📅 21:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30207">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLMl9g2AB5UPAHo0ZGpb45s80QZkAMkiseIPTDfu6WS6xlPIB2qpWMcqNDxdLYvRpDnInpJWY5FLggOt31-yL2N7lyhU2q5jywofAjJ8GStC8LlVu7UtO3cEGvNxrChnWKH-U1LOfJoyKImPxH-qJxMxZ7ewm5ck9XjAfuXoL4vHPQhLw-PcoxLbuK3Ole6iRhwarpjS0B0vS2WPY-QT-JNllmO_K9Lt1E71xRPN2-Z-5qhvPqdsq0L-n7H2BS3tSseq7wMMOH8uH47r7L2nML2seOBff2uRcguJMlCOy2l0Hm5uNl2MXf6Jr_tJG8h6by9rkiivz1O1j4FMjP_9jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/30207" target="_blank">📅 21:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzehomNUX5pueu-zQ-7UcY-y9Dl69GuhxkyutgHjSoHmxaeMYSRc-NyLpI-BqTAt0lDLX3pDi7EQSlQaVgdhZNK9TUsQAtY9zkNpO46KbvEciMTe9WS-yLbUCFw9u9ecXoT-QO0jZ24qedKFdY4B-JIJMAGkQeT51zuYHEIQCQe8znVyL546MkSVDEq2XLOBkJPZwBHzruWTA_UOxtBdgL8P4LYBFoVu3CJYoX4aBpRwz__o2D09SQFoRr6RGdb0Qq5IqlZqjqutpNDjLkPoCP4MwOI0wdUWBwReaXtxA9OIAH0wjBni7pKfC2KW0_IsRlteYCAgCAgeRWGEmubVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i49UdMQiudEige4gYeG_RwR9T1YxwSYF_viS6JoMIySN6iRfwPHfX7TQ7IWLrYWrPjY4rKw2onpzc24qypyBrV4Y9NDqrFiP0Op8aRKBf2CtbXLYwUNCj5WMx18hIm_NTNFEeCtEtgRE5rUalZEa_DsZykq_3SOsVmFY6UX2YW6Uc0UbroUQyW59OGbJTK0Z76xruDve70QriP_iFj0QihSCMqbedlh_BHYmFDJs0kmQyOdIA0ky9lNw8ZaeCr9ssYS-wo0g_3fVWTxsrHFVtRVZ5LgPZOFJotE6HyOE9hssrtwKbS0KsJrvqRlDejG0loLCum88BDrttasxYKihIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج بازیکن برتر لالیگا و لیگ جزیره در فصل جدید تا پایان این‌ هفته از نگاه سوفا اسکور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30205" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_u8GFnHTmt2GYyMSlq_r_F0F9NwaJPCa2m_Up0OzT94MTLyx0uwbQ9C25X6xVqqvJYHvIMqUHK5yo393n-F2G9lSEhheBQ5rMmFdoLfBRGpx1v2kuq_yWdTc35DE7-K1npNJcgdY54PoZ68d21hxmwMejxJoF93jvD1keY3X6qzYcmEZNAxvyTNI_u22q7Itf1Uig12moex9pZWHFJ-7e8rNM01V3HsfgJfUtoMXFIM9kfC8UpRYLgBna0nnCRpmlzCFvlkAnNOJ2oEO62yIkpAUSxSSaT6nU5vuFYELV9jiNmnAbOCsDReYfWxYJ85lKhQnwHoyAdihvCa7qBbwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشود عربستان‌ سعودی و چند کشور خاور میانه‌ در آستانه‌ شروع رقابت‌های جام ملت های آسیا بافشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30204" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
