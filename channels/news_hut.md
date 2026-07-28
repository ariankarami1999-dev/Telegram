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
<img src="https://cdn4.telesco.pe/file/tii12tyDIUX0tYNVbOdNprZNALc3QaI_S2unNAZ9L21VapsfkSipwbXxvhKrncfo_g2jQCGjqRjlS1jtsKijNKHsEBYdpaPdZTttcFwIJ_oRLzDDeZwxMvWrGTaQqpwbUVbA5O-zN9hXSwDgJx-hPmgWongNbmoDpKI-Tw2lfUSsxs7sJvovM_ZvQZQrRKmq429lKt9_mEmcGoGrfZc8BfFsWyTEhixEprGRegjrgyvvWZZRWDdGy_HGDyQOTz4vU2XFhGP58vWonSBrfvPwN9aakEUgBMjsaZg7q6M8ltyX8Qg3iw4AhNKN9zVoPv27jzMKxc_SKkxbcHMS1crInQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 143K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 03:22:13</div>
<hr>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=MsCAC8akjb_WkApy_1obh2DDhThBI8hZNmbbmj2x3hLeMImgnwiM3v87lgpamc2V7US03KSq8XtsE3SQjEBDlVjiiUAHIqtzGxhHWopU02CBibWsEUCTBiU1cJXElnM9cmBPAEuLKoayOVYsWxL81uX0y6N2tC27ibWuK7Kus_fKgcCVSmQ2waVT60AH2ha0jEoiWE8TfklDVxyBOjSCd6PiLmyYv8BA7Z9BYqxEvkSMzfvfVnYHh8Hv-Cu8G1bSr5BASuMqrR1FKXF8fWJol2OTO_hqGItQuHZu1GlNo9os_lCzA3h0k1_e80NhEuxHMoN55cZvTpiFZ1LlYO74BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=MsCAC8akjb_WkApy_1obh2DDhThBI8hZNmbbmj2x3hLeMImgnwiM3v87lgpamc2V7US03KSq8XtsE3SQjEBDlVjiiUAHIqtzGxhHWopU02CBibWsEUCTBiU1cJXElnM9cmBPAEuLKoayOVYsWxL81uX0y6N2tC27ibWuK7Kus_fKgcCVSmQ2waVT60AH2ha0jEoiWE8TfklDVxyBOjSCd6PiLmyYv8BA7Z9BYqxEvkSMzfvfVnYHh8Hv-Cu8G1bSr5BASuMqrR1FKXF8fWJol2OTO_hqGItQuHZu1GlNo9os_lCzA3h0k1_e80NhEuxHMoN55cZvTpiFZ1LlYO74BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWnjfiksSHODzqsjSoMpCGguSDcm6QH6LoZuHS4DlYqIeB4G2s_yXlAfGZpFXGvmJFTcBmMBr-QvLaFtN9f4SuZVr2EF6iO9rAndrK_2bu_vjF_qFVJlVv13KxWEIe3j_eWKvQLrKXxbIoFcM7H5NHGCt3tmwu_8Usd3vLRTlturEqIRqLBwpdM6lAQOic0X_NLucPYeTnEglw7uTBvgIOTcCTM6AJ0RVxFAmEIGKo2b4mJxCu3Zc9Scu17JRmH_e90fs54nac9HMNn1Jipiu1qHMekKu22qrJ3vGaTHUCITWT_TbYplR-S5ZGyEaArE6AnJR5NFniRvUdjEfOKHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVws3qCMpZh3ZofX1NPDxICk8qY24h-ezbXDH902NCBC9HL1fWDc0DNHrgT7gyvF2JP_eYtFjH7_mpU11YnIpCFC-TdPAvyEPqE5Xe3dtruNkvwAJHJTnaTmnGFEXyOV_XPpuE0EuQsCq_eDbcxQ8eZvdMcfpT9D_eIePZ54mmtzEIEZ2pXbNfLf-ZTI6KtOSXZQFXGdv0gQb2-p-MrqT6hYYW1-0ne5eb5US4rNOwNPRyHrVsWxj9LwWlB-rHGbeVc66dYY14wbG11svc6wCuntukoL7eMvcd-haocadL1AhZbrGSqKnPLBy-CDD7uvthPmX2ru63xlj2oPboD7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=e5Z7cTrGiRopGnM4yA-2XTQO-vtKynYKtuCVbAJTkTipYB2efHuq20og6LqfDlawB7ndBmBDqQ0uiwFPjsZ_QAw2QES7aBMSGeF6dIPfsPOnN8QRdzf7E3PyOcb_ro9WGD2htlCwuXmQSUoLQ3It8dhD8geM7tmIKc512fs6RosO55owexuNbQ-K0dzI_Q8Zsyi5W34-ASbynfBcq5Z_FyF2nTvfI77v7RJb0RagpQ7YRVczrSV5rJCc1dYMjz7khW3bSvN7j82g_5Kk8gi1w0eA_luMnPUdKfNjvHZ4CW9dVqPFkKMR0l5O1KQbQ1lqOHGAQkxgym9pp5iw2UIcgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=e5Z7cTrGiRopGnM4yA-2XTQO-vtKynYKtuCVbAJTkTipYB2efHuq20og6LqfDlawB7ndBmBDqQ0uiwFPjsZ_QAw2QES7aBMSGeF6dIPfsPOnN8QRdzf7E3PyOcb_ro9WGD2htlCwuXmQSUoLQ3It8dhD8geM7tmIKc512fs6RosO55owexuNbQ-K0dzI_Q8Zsyi5W34-ASbynfBcq5Z_FyF2nTvfI77v7RJb0RagpQ7YRVczrSV5rJCc1dYMjz7khW3bSvN7j82g_5Kk8gi1w0eA_luMnPUdKfNjvHZ4CW9dVqPFkKMR0l5O1KQbQ1lqOHGAQkxgym9pp5iw2UIcgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVPNx4Zlp3YrRdTdV4xsRDe0Q-Qy5BtS6q6MeCeqGQocKvL2iDAtp-j0Dwb6l-T43h-0dzXBxuNAQQzT-YfDVeh64hyKzXygctRuJT4hmSMjEZ52AmAqjaCiTOoOG5QOtbXfRGPUkIWWNDNwQxNGGlrBBgl6sa26EbwaikLNVH8UpaXwxmBD5aPxS8bcRyQcVNGzak7Le-oLsuy5VHvobkPNnfVBKObeuXTbQkZXJWskfegwXKl3V2x872GlSeV5Ky4jgOn1-_dqIdC4fuqd2Vx9zCWDPsZYYMYHuh8367iPDuF1tJJ2a2RaoJmafJCENsglL1J32pk-OC8unAuMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl9Lw5bw4Ch0NaP6EC4PbNHSO9wHIvSvQsl0BF22syZ7qFAO8TI4ugUonPz4CCjuder3T4MdQAiDrfsUr3Zz4CzKdEr36wW3iQxLdV86rBLqffBJwT-2n-s5b704NWzLB4OLS_h5wcX8LfJzHb5XNLadO38TuPo82wFRt38PAZtdz8NGybxRROs-gM8L9_BiloxdBiXQwqJOphrQ-19lbp4F16yJpIL3pqckd7bEcXYmo5jmYc6qs_khvhfdzmbVhbecEkJFursVcd81yTa_3GJEK32oEprQ7Ge9-17MdBPqn8OYPqVhnS5lJKJNydDs_lgYMEIL4PwP5RHdT3G66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lnZ3sOx5obt7dheNfL6aWJQ8GqwAOXfrLFpXxOv8sALRVJU0FcjEtwxMOjfJ_FQ3s85u4D-Qo0IOmE5zoZOf6mEoHTRAL7WKgSZUFl0M8kSnpWeVI8w5NtP6Gs00Jk2GV1ZRI9lIrUZ1QnJlCYawdlAoG7G03BKLxlUMO58ZIht-y062D8J-edCWcF-XGCYvt5tC6XA3DmFid8XF9Mx2rahG7I1P7uUk9EDOKt1BpTDrGiXU5mWrBv1Ps77fhs_rBu0qYUaTi1iSK8PDm1vHumIOg_C6M5A-_2HcjCwx_zIaCzKr4bbgZ8CY8iBADCZOfuJjE0PQMfL64uVxZDcR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pAGmPjSdxWBxi3ps3gKf_XhO0xrjwWHBp84ZVyq3oDbHTA2-9vLm5wj-bBFVQOlwD3dQVIYEmqqIxW24ZGj6GGl_HQulaI3oDh2vix33S2FNMC1_OVA1xcltpm8V8-u4KCyEfkrfXcy01p0aI0TvGzPwZSlShYIpSyo9Sr91UVUflLd9WzVNMhL83JiM8RMNm2pO5LcLQRblet6QnDEAQE0CHH8yDO6y6IHFs8oaRyn8bC_vcTIRgZwvLMGsNH-O5ppSDQVQw_k0q7JfnwhnNXVRWSX3WaRwgnFYgGuSXssEqWpGjTr--GNcGLLmVutmMGAyiGwEiq2uG0SnGx2Xcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=rXWhJc1M-9nS3RSejfFDvkTBmZdmVRmWEH_Q5f58LsKE65da8CKr45p0ER9540ZT_8TpVtte5fbZXLeri05cF3P-_C0IDqy9YUiVVB1q92yI2QMxbLXA4_w22IZqvEbx1auMt3FPwC-JHhaqCJZzEQTxZ1vU5J7pCGmmfkIItODLSTQ2frMuzuuNmcxSSfMnXs6dyEMHYeM6pdLCiuufj3z6bFbqpdzzUsy5vk-egFl__305-6HIofQDO5xt156BEAb0df74mPkiOrGMfqvQbZUh5sVRaVkvqbob0J2u3luSP_przCoQ30fiQHiBBwM7fvW5fkNkbPh1mXYYQ2RiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=rXWhJc1M-9nS3RSejfFDvkTBmZdmVRmWEH_Q5f58LsKE65da8CKr45p0ER9540ZT_8TpVtte5fbZXLeri05cF3P-_C0IDqy9YUiVVB1q92yI2QMxbLXA4_w22IZqvEbx1auMt3FPwC-JHhaqCJZzEQTxZ1vU5J7pCGmmfkIItODLSTQ2frMuzuuNmcxSSfMnXs6dyEMHYeM6pdLCiuufj3z6bFbqpdzzUsy5vk-egFl__305-6HIofQDO5xt156BEAb0df74mPkiOrGMfqvQbZUh5sVRaVkvqbob0J2u3luSP_przCoQ30fiQHiBBwM7fvW5fkNkbPh1mXYYQ2RiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Np6jWug_8XF6bS8b50_H43Tqn43_amxN1woYDpAFeoMwygHWGfsGrxqJYha4fyROPt_CgN62_9k-lHq7BRDXUqm5cOZXS6c_ezTBjiPtLIF_eZ7LP4dCso8hJ4-Zn1p71BHL-cbZGVhvTggNC0e_qVLFsvsa2QA3ye0hk0VJHbOonKbK4Q0xOdWrgZKtR75_j9BeVh3GRxcjoiQJGLF9N8N-rp9gm_rdbdmQRUderYLI-H-jy5nhWhH1kE9Myxq1uEt4_9DUB4HgUrbNB6_r5E76Br2HWl_8Uu-kIAq8-KVnBpt0Vbq2_hHGINFeg_46qqpdOnyREzIrdwj5WMX_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=ikgAPoh50KyX-H9CI9yXR2kL12Ngb_gzEUGGrEoIOSMy3vxtuFxSNxKYtggn61HnBaQQl6wRc8FGYxqizKoyGrs6X46D9oL_K_bX0N68WS4zb72D0q1QdJVU0C1zWlnoBiA0dCh--RirRdfhqPnJfiofq0b8E2h46Qjxg52mU5hgXY2FST6eqTIbDsG4KbXuwgtSeltJ2qSKokm-kU_qOfqL6qup5UX6YNDohHwZ4VbvDkNLzmb6Q7F1xJGCmNL5OMetXf4hq8bH1P3HlnnL1IxvfP8R-DzOhl0vt1LBSFz6ZPZm-QEkRXPqy_qnoNbXznA26QCTYUV-BmiN2vk3jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=ikgAPoh50KyX-H9CI9yXR2kL12Ngb_gzEUGGrEoIOSMy3vxtuFxSNxKYtggn61HnBaQQl6wRc8FGYxqizKoyGrs6X46D9oL_K_bX0N68WS4zb72D0q1QdJVU0C1zWlnoBiA0dCh--RirRdfhqPnJfiofq0b8E2h46Qjxg52mU5hgXY2FST6eqTIbDsG4KbXuwgtSeltJ2qSKokm-kU_qOfqL6qup5UX6YNDohHwZ4VbvDkNLzmb6Q7F1xJGCmNL5OMetXf4hq8bH1P3HlnnL1IxvfP8R-DzOhl0vt1LBSFz6ZPZm-QEkRXPqy_qnoNbXznA26QCTYUV-BmiN2vk3jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkS-Y--LMqBwb_dh_RiFQs2vYgFWEOLgoGld3r-ux-L3aWfTcHCuR_AZxI7UYexSvO_vpmUN0st4-wKD3L1J7SQTQHSmZ9FjbnMQR5RgJl2OZFAy-R5VmQ-Q4vqUk6zwQLWtJs1lQg9G6YaHH_7ZJIEcAimEQ7bbr2MJZR9oBvJuN-xgztXz0lK6PBKP2p8hDyG05dLB3pUGgJssTqh2GkfBsgcx-lhO_t2haMuhg_oEHfi02DrL3Z4ljcCzi_WBBqt3Ees1ncv7AmL6xvD1cIzPBHt686D_XTQmaWkL73sVd65s5wZIaTzSLKQ88PqIe81BsnsdbKX2K9OgtcDFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzRI1UxUcIRXPMIGEClm0EjhRtcABYh2HdAzpL8okEhlmS_qanu5tLODnx9pa2BhAkEJ5XiGild7Achl17JPzQPPuWurgMML9nZJK3Tuf9auvkZ0HcWvLyy3_sF2_8tHabvcROgn727ocCOTqZPhNRj4VB4REs5vgaInx1ooLsOz2r_gHllm1fPp-ouRksNskShMPT6JFza-HfcGE3C-whswP8s3GZkg0L3BymypfGbn1QB_cHSNtX-Sy7Tlv5yJ1J_T61cs-7qBm9SInJL-p_cK0NtITd844QOMlQeXPMD2kT2w2EbZT7w7fNl5Jqj1IBPL9Q9A1J9kjSmrwqLWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=BtT2WwjG4dQHr9ULjsSmTogNC2YOTkSp5-iUlCQXnPFAF-h6g6N_xbQBmAxfr7LO61qsz057e4LFuyVeqsoZzXU75DJV9A2hf16cb2cdF90-UR47VyKHz3UyxoGktNHGsfxuZWbwHNGrmQXUu_r76lSWUd9-ruMSuyE_sibiivf78BkF-AjzIvRuq3iVQjLDO-r6Txa8QvlRRi6VqClOL_l3Ztr2kfWCBGYjeE94Mf4zGIUpsNkFPuhGgaNdQBTp8dZbFZD4lhwDBG21mpUbS5aeKHw3NY2rFedN6LLixESIdQJ9VFUeGM-g3ckZb2AA-ZQFAE_mIIP-pknarpWJxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=BtT2WwjG4dQHr9ULjsSmTogNC2YOTkSp5-iUlCQXnPFAF-h6g6N_xbQBmAxfr7LO61qsz057e4LFuyVeqsoZzXU75DJV9A2hf16cb2cdF90-UR47VyKHz3UyxoGktNHGsfxuZWbwHNGrmQXUu_r76lSWUd9-ruMSuyE_sibiivf78BkF-AjzIvRuq3iVQjLDO-r6Txa8QvlRRi6VqClOL_l3Ztr2kfWCBGYjeE94Mf4zGIUpsNkFPuhGgaNdQBTp8dZbFZD4lhwDBG21mpUbS5aeKHw3NY2rFedN6LLixESIdQJ9VFUeGM-g3ckZb2AA-ZQFAE_mIIP-pknarpWJxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR05wUIC_0pcfEDyziHdTodgJN0vO6IyaX2Xk0JuqCuPgcMRC101Wp1qoXB3TM0iFhLiV3lPG1eShI-k_mX9IpcfRMu5B-E2sgr8qSCU8Xd8_7noC95aZW2ajt5zn9Md_FKxAYtJ99PQWqYfjfLJZiG3ZNq_7ryy1eCN0UqlMOgMxJ30QYxjiNU8IvBgccGZ3CSu7q9LR3UMuuZzWuV4GE_rzrXSM-znM-trUCk1qFKbDT2CIrlgxF6TxA8btZHs5okit-AemwbSlCSHliNbJZJaJ-gBnIKTLjlObXZVPjNMfY6BxdMpMxxArlbSdnb3WspIK9G4kO73VsfPLU1l_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=b1ERTCW-BdzyD3P8gcVtcPKScPVz5hpTuRVJYMXKpldd_BqeCtdPGBr-NGrIkb4lmH59cG4b_6i7fWlvO5WJrCiqGXrc2jcS0-m0BTatzE8orHmmemrgESkzy8ErBlCJgifdN1yhEoApJefxnJIW_RXuQhQseAhejG7qBmlHULwQi-PeUHXhqX8CmD2V69mgqU1NTO_ZwV4aL0_sz6rvWcxY3OG9NaZvPG6Exh8XuNN7urzyv4sXvUg4ZTazbxNrD2I7KQXvslbSiV_KDcXZSNkkCJgORk0SeTVPYOVB_uJcmIM-3_KhC069ev5aQKz5nWZXZMeesQt1i3Zx2isLzKFf7mnK_8NJud4_O9DAF6to_fHPHy9bYtDF0NVJtFFycF-nm08yqpBfk8jZz7U5fBD-HnDnJULkjKhbqiO938ZFXd4UGE4konCKSQbnjEXanwy_xPW6qCYMqctb3NDlVvkv38VvV4dYN4VfJlkIErbdC6zJBdLEbVysGT8ESQXFB4_dxEWIeGPmrpOPpgSyr_RpavyEjOAwb9iSPCepdMmoOAtfVt92ZDulcIbVgm5EJWwJ42yCr5KnlVoSG6uhoE8Lq6R9xqGKIyNouKsEMEm-DZWR2RSxUVsZpZgEBXTO3YaU5fvpsJxO9JhbPbQomi6jJQeSdPEdWG0dmevNdvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=b1ERTCW-BdzyD3P8gcVtcPKScPVz5hpTuRVJYMXKpldd_BqeCtdPGBr-NGrIkb4lmH59cG4b_6i7fWlvO5WJrCiqGXrc2jcS0-m0BTatzE8orHmmemrgESkzy8ErBlCJgifdN1yhEoApJefxnJIW_RXuQhQseAhejG7qBmlHULwQi-PeUHXhqX8CmD2V69mgqU1NTO_ZwV4aL0_sz6rvWcxY3OG9NaZvPG6Exh8XuNN7urzyv4sXvUg4ZTazbxNrD2I7KQXvslbSiV_KDcXZSNkkCJgORk0SeTVPYOVB_uJcmIM-3_KhC069ev5aQKz5nWZXZMeesQt1i3Zx2isLzKFf7mnK_8NJud4_O9DAF6to_fHPHy9bYtDF0NVJtFFycF-nm08yqpBfk8jZz7U5fBD-HnDnJULkjKhbqiO938ZFXd4UGE4konCKSQbnjEXanwy_xPW6qCYMqctb3NDlVvkv38VvV4dYN4VfJlkIErbdC6zJBdLEbVysGT8ESQXFB4_dxEWIeGPmrpOPpgSyr_RpavyEjOAwb9iSPCepdMmoOAtfVt92ZDulcIbVgm5EJWwJ42yCr5KnlVoSG6uhoE8Lq6R9xqGKIyNouKsEMEm-DZWR2RSxUVsZpZgEBXTO3YaU5fvpsJxO9JhbPbQomi6jJQeSdPEdWG0dmevNdvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=UNMGwj7gC03ZnQrTg7popXZhrS5AznRUEAZUsrsFWwEZm_SFERCy1wMt_8F_6QAqElBt4F5i3BpNc9QCHEGoqtvKKmNelXRPOCWF66EzuH6QhelvMiPmMDiQjBje3FpHJxa1zldTHGj0D0uUMYLGuhe6Gk-vrp1naegnWYt-T6-dr6lHwZlihTjEG9KK9yePGbw18IEAE2ZM3W7y36RIhqBsnM5aJHzpQr_sDDKmIoyReTKAN7LQeIrErYhIQpvFAzilGLjWTwth9h40ZznnfT0r99ZoP86ld4DPUMT6L4g6c62jBuGzeTqou5fKZCjleyYpUQfHLf-fsgs6yApkjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=UNMGwj7gC03ZnQrTg7popXZhrS5AznRUEAZUsrsFWwEZm_SFERCy1wMt_8F_6QAqElBt4F5i3BpNc9QCHEGoqtvKKmNelXRPOCWF66EzuH6QhelvMiPmMDiQjBje3FpHJxa1zldTHGj0D0uUMYLGuhe6Gk-vrp1naegnWYt-T6-dr6lHwZlihTjEG9KK9yePGbw18IEAE2ZM3W7y36RIhqBsnM5aJHzpQr_sDDKmIoyReTKAN7LQeIrErYhIQpvFAzilGLjWTwth9h40ZznnfT0r99ZoP86ld4DPUMT6L4g6c62jBuGzeTqou5fKZCjleyYpUQfHLf-fsgs6yApkjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7bhz2u6bn17WVsRkXKQIX5wh3hh6Wd_-PgDePYxLlmA9vvmwFfgy0kFA8OKZGAalAkEVcSfSHHvzr78ZfKQDLem7dlS-ejM_JQc0Surzjcq5PibnRF8yBVRV59o1a27lVaPc61OhG7ihVcon48vVW1toHcKtRr6H9YzAfEl4drHg_ZNPIMhbruAzcvB5alol22SwCWL7N1G7wiPONlZb6KcLQvca39DGdut73PVd6M6OdT1qh1ZuxXYxGfk06JQvlBMrUbZAwcer067LF2MH-JZfknGCvg5Nc4HU_GYQEaEcxMOMZrJNcL_bJiBl43_mgjdQuGbQPDHAvl3KIRe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ckZkSNOoKvY2rZG7lu6LEAWnSVmlLh0DwAL6SGH622OkKvGnuR1GtMLhoNpYVtGY4GKQuKknQDZy8swwlSVEGN9q7JedgYBXdjuk_3FOmZPUSu3_D0_C-Y2-XsVHpKzjlKHpVwebeP98q-RN8dR3MNudJlW0keK7uXeTt4i113wBLAN_duULKhiNLGbKlsCWosjXqk8j2r68Jk7zQNTQ_FOFZpOLiWQoN0iTS-P98iiT2Ug78Wyid0aZT7XHc4GybvrRkLDKhc1x3ZnsGB3Lp6KViwmAg8GV2PrIL57nklp_GK2spCHAa2iTsuVFsO1h56_Vx9LCy5-pdHTbt9D_7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ckZkSNOoKvY2rZG7lu6LEAWnSVmlLh0DwAL6SGH622OkKvGnuR1GtMLhoNpYVtGY4GKQuKknQDZy8swwlSVEGN9q7JedgYBXdjuk_3FOmZPUSu3_D0_C-Y2-XsVHpKzjlKHpVwebeP98q-RN8dR3MNudJlW0keK7uXeTt4i113wBLAN_duULKhiNLGbKlsCWosjXqk8j2r68Jk7zQNTQ_FOFZpOLiWQoN0iTS-P98iiT2Ug78Wyid0aZT7XHc4GybvrRkLDKhc1x3ZnsGB3Lp6KViwmAg8GV2PrIL57nklp_GK2spCHAa2iTsuVFsO1h56_Vx9LCy5-pdHTbt9D_7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=olxu8Nrga83Wo7VslO7KmfUNyEXk7WLfV1sEF4J4lyV_y5xa0hUkX9EVuETXuN838Pm3ATpQj-t_JlbOvALbZUUCmC_h9QoZYgU7M7OD-wwPCwmOZWmIKEbgO7sI_y2i0QEe4HJwvz7Iaej7qTQeYidT6ebjdldHd408Vv6rEcqQ0oc9puMOUxa3MdJVHCupIPbDye9Rvq8Dp27RBYJiNdw-BQ6zNupWD8fynLQyvfjsGzwlNrKIYR7RzzJY8H-NzgN_iN7wiei59q00meaJ1uGfovWUrheq4n5VSJwWb5_wXyc2UCSo6I0x_f3YTVnDEt2FGbDwLl_YqYSJjuc9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=olxu8Nrga83Wo7VslO7KmfUNyEXk7WLfV1sEF4J4lyV_y5xa0hUkX9EVuETXuN838Pm3ATpQj-t_JlbOvALbZUUCmC_h9QoZYgU7M7OD-wwPCwmOZWmIKEbgO7sI_y2i0QEe4HJwvz7Iaej7qTQeYidT6ebjdldHd408Vv6rEcqQ0oc9puMOUxa3MdJVHCupIPbDye9Rvq8Dp27RBYJiNdw-BQ6zNupWD8fynLQyvfjsGzwlNrKIYR7RzzJY8H-NzgN_iN7wiei59q00meaJ1uGfovWUrheq4n5VSJwWb5_wXyc2UCSo6I0x_f3YTVnDEt2FGbDwLl_YqYSJjuc9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcJRossjPrWCF_2utB-vq8DPX---v9i4samIEGNEWxIeIAn-zXh2XL3l6PLdO8WiFx69-BFkq2WBjUmzwePLgwCBbciH3IXmbpjIovUMl6urt8xChM4oWfgJ5Obm8291G_4lnBqR_auR_oVaobJkOcSsDGErJhqJ89igdfpLCMXr-mu1e2xpK59s2ZO5WSWIkClnBAJhXkYZjxQ9ryrgfzn5FNYbU_vxQVtDR3dYskQ1YVPA2w78x8q70hZdp82eYZanLeKdHBU3WNj0pYZShJ_p6fk_zxyAQ2gFIQUcjoV16J44aPiTrxR1Hcn3qeQ-7aMxXkpXSicSjs6t-WsA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=kqfyNLZz3s8e7SS__MER8a3cWGqbXfw3EVTvou_rT8XTdBAcQqWgsT0Ai9teNV7B2aEQJTXLAjI7dae0gHM5kUHA9RON2AfP296Cj_zj_p8ZzeZ1BININqew7qBPA8AMgptldMTL8gXSdrso4cKPi5jnVq94flk4OPDZazrmXwZ9EbP_XVC6aY5LwYvTRECMRL3L1CRSkMisO95QwngAz2pk-es1rxqto0GBR4uL1L89Chu31vJbLC-Dv2HdctgBP32D5h9BsmY8qVkO79M4cT4QhJvT9eQ2yMbvQ_QKAq5wuDXRidr8q2v8J9ffwaHkNmL01po3xsTCGzQ1TGtAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=kqfyNLZz3s8e7SS__MER8a3cWGqbXfw3EVTvou_rT8XTdBAcQqWgsT0Ai9teNV7B2aEQJTXLAjI7dae0gHM5kUHA9RON2AfP296Cj_zj_p8ZzeZ1BININqew7qBPA8AMgptldMTL8gXSdrso4cKPi5jnVq94flk4OPDZazrmXwZ9EbP_XVC6aY5LwYvTRECMRL3L1CRSkMisO95QwngAz2pk-es1rxqto0GBR4uL1L89Chu31vJbLC-Dv2HdctgBP32D5h9BsmY8qVkO79M4cT4QhJvT9eQ2yMbvQ_QKAq5wuDXRidr8q2v8J9ffwaHkNmL01po3xsTCGzQ1TGtAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd3VJf2AHOds4t5Y6OqXwn8igGQQjXeC5ulU6ftmOAR7t6pi-tyUEYTf_DqzsjpHhOfVa61WxPM_p_g9-rguNjNqrhlDniKpNL-VA4baS3NUkPuD01P6xKwZ2YoR2yvxrGahVwHmRjvSU9yyZe4KHVljKxkleKR60vRz0Ov3b4TDHV160jq-tfZph4lV7CDTzYxEJ5yQShj6_NGv2RXuPXnbe-qfsi-OH3eUGykmbpVRodx27RKal97SBe-DhgXnEge6iDu1QamrVWy3luXVyPTY8T60_qtN-BkB482o5Ic-nKYaPKleb4BAnvHP4ieVBK88jf6DIBzOCBMs92rQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT1NRc_RjsXBMseCDrrznSjALBWXozTYvD9dsKPHMQUgAQqK8tLvE2l9nqijdKnHWajGHuSZDAmxLFvu0MUYO46UfMzPMqfwtnX-OF-BbP48ud5qCGpC5v8nnxNV1PY6zwnNcyxch8Nx-ao93ICKONA_iX9tYa6VINHc1SM5LVJSu5DY4gyLa1Om39tfkSHRNJq2MjwKTBly06kahkTOs5CltQwnvNAOc-LiplDsjwG9u6vh5hrMdzMJPt_pdRMpY9FtP-4Zo8AZTbSqWUXs69461c9I5-6pWIyAZf8-q1gmZwxgBwvCmhs3x0DnQrAsjJ0iULsgvOiN2EKmIBoHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFoNV80J59si8gH975sWja7wnBr6HdwRB62NoyPe7BHd41oVW-QgUhdAqxhZj-wMkGO7ipw0nLFDjZSLwmIUZgXX19D4euO7LhQm4f89lA61h_lp7gOZXLgSGDrRyV7vv4l8JwEK0mchC0Wnau9M0yH_aMbB0QR1v-cNyHyl541udJVt-vrLgGGW-HckQ-5d94jloK_QUyzimvC8JmkcItXEzi7ABnMuwe4cgkgqCfKJH-5doeGZ0Y0GzrftCJDEnDQSALmbQu8sgRNbyrp8__KHMhHHgPyhouP3WqGlY_KrrugvlwvvNVIbtlewNOfIXPHoHHRtTEgwzrMbKMAnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_vpNPdi1bar7Cp9v29IZsx5RAV5K9_3LO7hijc7PXuqaftRfccDZCS2ZTZiJhOJGrM1A9nRpbJ3fIrSMHzagXu8dt1JHnUb9FhGm-i-pN037xsRnUvA5T6kkRCbqBrXV5WAkGiN8N32P7JL86SOCdJZg8Sz_Ai59nYjzLcG1yUg2ZxsP_a-rpJ9eOwk_Nwe-86R_yZN9CS_tkih51jZ94QgOk9qaLvhGfU0eUnV2QZKPP1ykx3OSQY-q9-nNZ8NpsVAl8s2JPmmMUwVrJyliIkjFScpdn9vrcTnhHF1yxMp6GVzeGpIoVy8jbHpYR1yXL_U6j7wqa7_sXQ5nFNoFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=me7a7rdBIhEYdc_qc75hGgenjXYMZbxy1RLWd6zettnmhDrOxeax_XfvHWEhEGysYWebV0nTrNXUIk1YdybXes7UzrQ56LVpt20DDZyDHZ4khjBpX-2OhTYfdAk8k-LnVGe4I_KQ7muQuVdO49CKwdfY9u7cl0adBfD33TioxPLOBh-MQyy2GqoYMOq5EkGW1nPKu8XmimVaCi2rzgGGkpGu8A95fFl50NP4g3WADBqIDSR1Q42vOeBpWRz4QMMz5L9d9iVkdOi33Y2yLhHLmkPDemiCEGk6Z_AGRtbftAxyW9McFg4xJjnagyFcNXuBHIgU4n0ly2xH1y7Wv_YRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=me7a7rdBIhEYdc_qc75hGgenjXYMZbxy1RLWd6zettnmhDrOxeax_XfvHWEhEGysYWebV0nTrNXUIk1YdybXes7UzrQ56LVpt20DDZyDHZ4khjBpX-2OhTYfdAk8k-LnVGe4I_KQ7muQuVdO49CKwdfY9u7cl0adBfD33TioxPLOBh-MQyy2GqoYMOq5EkGW1nPKu8XmimVaCi2rzgGGkpGu8A95fFl50NP4g3WADBqIDSR1Q42vOeBpWRz4QMMz5L9d9iVkdOi33Y2yLhHLmkPDemiCEGk6Z_AGRtbftAxyW9McFg4xJjnagyFcNXuBHIgU4n0ly2xH1y7Wv_YRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5CNlrwVWJWkb-7uhQcbASBHQ3TLpJVpKThZKxyEgm0C5o1arqBT6vA0BwG0MSvbz3mlDU8nIWvKgRPO1u44De7Rvp5nCJc6NPP5yuejFtiDDTezPW8klrzXhOGsrfborG4iFHOqOs_Lu5fCQw1vfd1j8P8wzGCEMIY_YWBiajzYt-93NelY6YiMNBKL6bWRkvTZLpFrPVDuTr2kD0qWBAAlAajxQC3WEYTZXEY4Q9VSih55aBTfEVQuFknsRx2IXQH2BTXT5g11ry8uxKShgI1d6LOcy8IBIiqLq0pSd9R5Ppk_ydcCzpRSh2uX6gkySdxccazQCNVjSXgk37r9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=VXFpKoDg_Pl-TY5xwhoNoROekeyW5wiYjC8wUQ6cpQFwPWXnSnCJe81Mmz3uy9-0G_lPCeGj4cY_9Vi-Z06VQYuoQUYYhketzrYSXaKGYdG0s7HX1EO6Akx_1AX6WK8LVfcgLKVwPDwjD64U3fevEZ13J6kdHdcdTjZqG7SLXVuX0J-GusOCz7UsTSX7j5kNozteR7yHKtVixjFFHIDZ2pv30PC9y0nrveqbfuHY6THnZFMU5Os2BqQcqXUZTIRFNzZq27vBnSnSXHEVWgmzW2sVAP629GfHgQXYOWAQ9ANJU9vFh4RjBY-yVsAzLRmoSSYn3MnkNLPer6oSEuPp0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=VXFpKoDg_Pl-TY5xwhoNoROekeyW5wiYjC8wUQ6cpQFwPWXnSnCJe81Mmz3uy9-0G_lPCeGj4cY_9Vi-Z06VQYuoQUYYhketzrYSXaKGYdG0s7HX1EO6Akx_1AX6WK8LVfcgLKVwPDwjD64U3fevEZ13J6kdHdcdTjZqG7SLXVuX0J-GusOCz7UsTSX7j5kNozteR7yHKtVixjFFHIDZ2pv30PC9y0nrveqbfuHY6THnZFMU5Os2BqQcqXUZTIRFNzZq27vBnSnSXHEVWgmzW2sVAP629GfHgQXYOWAQ9ANJU9vFh4RjBY-yVsAzLRmoSSYn3MnkNLPer6oSEuPp0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXAkiY75luyi5wJMK5BHo2Kjwt2EtZRsvBmQtKWwSONFV07v1kXA-l_cF7XKjxHtdve_8rALHV53u0YVqzFV1m1ErggGEJYpuKPKXI2zwyUTL_XhGpIRpvFgtSjNCQoSWjZaMmdRhHsRSP9Ivt4e7NOuHNyN4jv6qTxpSGfcvybyOGkbIVg0LyuKiypNkbSFHAI1zgPB6UAGDaJTV_ltEXBbT2zp1Fqp93283y5aEWwWB8nrhp1X29MvQ8yziXimdYlekxOnnZtqRMBOKbP180Sh3PWu_HcV_lyAi5kRUDuWZEgbFBQmKrXEo45LR6S-1_8OOdT413OYKK_3UtU2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GG5IqvMM2cHc4AVjR5ot2hfbSteYgrHZsOE80pMshCKiqcpxz2587sN6TSkswhQ2e0jGhTITgaNxymd2BuGVzyhLgxqLWHlY2JhWSsCFAnK2gdoyR4RyoIs1jD-3H4pArntdO-_0-ck89DXKjUFk90E6KbwMy9d8C0qwroeIWp8ONawPWe0mgYZ_Soe4AJ88KAf2BhvNqkSWQgZomjXS_Ky4Gvjidus_2C6RSW0VSILrC2BA934jW34Z9UCqxFPnuefbWxl1TepCJ6IykDwPoSS0E-dC6hOKHRe7h89gbhZwb0H_vAFMcJFA_5n-sBnk7CERAN3FnKqhHf2-KI3iOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NokYCFgi3cZfUO9EJ-vUh6XiSurSBIVnmvCqjTUInouHcQXswzwMp3THw35X0NlcDXhOlXt48genrQxWoWcTrBNAogX_Y4whI6IQB3xTox8OBZUishnVf84T6ZcWdDI5Xf2btXqZmoPOcoGKswpVHrEVC0-WMMhj_1CjcK16wTRDTWpcey4W7SExv3TYrFVptpjEJigo2icYtuxJndTZ0z0VRB_pAOFsB_mHcEela5GhM0wmKJwDJrBkY3ws1nSjY4Gm6EUGJSzHdV5XsrzkeVKWfw46WbzRE4mqqyOlIQO2MbHvuS4jCY6IPn9K9DkmSusyLPqWzoFXP8szBa8ttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGAECeL2tBt-oLCGYrrvaTKpWfPdb2gn1pYVSzbhFKXWhk9p2blQ8keDDGNwTAHNqFLz1PUyj5FpEYL2lFLj-ru1L69wMJbxWx-xY7bXUmwIoSHUHGMBr2_cTusPEXYuO1gZBBbsP2x8rseDP-OyUGfFFCzIHMANgfRpHNL2CQO0qGGyJtabfL-8IletdLyS0TbLBbRYB37oOIiAJ0bzs22rj2og77VZI0IXTZNlWEFQ51DvnHJcnW8_fZBNrRUlezxaK6hyb5zqkhXGTA2vPlBFhR-96VCciSFoO5DKpY51EW-95OalcORFL2vS6BFJBKELawgJ9SST6HjTVmhvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phX78U6n2bxjwRoDbD6iqE2mgLc-ZCvaVfvraJFCdjcgwZ1T8obkcDqLq9N4Bxkre9FgPPjYaXSA3paFXoU-6OPu0CzbIsG2WqI4YZkQvwupz5EZ_jZ-WmDfAbdeGex0cpmhqW0HueBTEfhKj8OYOWk-lbfZP3VXN58s_k7whhWKCcIeg3k9mTKirUm0oppr2w64SRVHbXXbmHXkODQzE5c8tuG3JPJCOmaOjEqbNYcJNtmfyS71mWXgZLcnR0HtYmdqJTHlOh_cY_Y2lijbiitCos6vfkfS9WxCc-VAgpM-ki4dvEGQhlR64Zhymc1hMUYZSZ4k-44HrcN52hzoiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUQZuPUp_u6cDaC8h1PoaT3RD_9woxt3f910SgM3b2w34wVcGa01kijLNkwgLZIdaMVbDqdaaYj_LimZtto00oCovgG8Ngg8mBD5n2CJYUYHt1-kXEuFkiHfpvVB2Xr3bHkPbSE6RX2e7BbatdpwACS-ASHXoA8F0SwGBWTFsZ2IIU3lZB4P_y_NlhlEcx_RxPXFzFNbpITsn71pjZgF1M3vyYxNSzz7xJ2OmFrJlcKDY94heDS7zP3vZVwRwycoxTIofC3VWtamoKxqVL2L5arjip2BOI684wzqksIcfoxLxVbnGY6SL-GH7y_gMabsaCBhJFtbFbuVwFQxCfiZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRp7ufrHeulCktDj6jGZX1nwcqSfP-ySPqORieEtf2lb7uzngO5GKkT8euRoeQ3CF-2-hQifNXb6M6WBH_l6H_XVLDXyi8NVejwFXpwQ4D1zS5C3ibLjzpAuDJDzhQSSe2EPwlXVt8OUWe3M4p0IqU29BKRcJgw4qM9spJVM6QdcjmzmdugvblPITqj9qMQqSnzbZnF08r4eMvFBMHzic7UW3y60hd8lD2m-Rzki3bz7IwA3H93hRjoRWojCk4hkABNlYrAPSO1UH_hoYelPtrC--jpWBpAsT8UkS32dK3susghMEfPuJnouQSRheRLX7298PzdD6zs7C26HoQXJbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=MtTeS2hDWl8UbWrheQlvhDLu_TfEh5HMrKkx0oLQKq2nPr4jwAHShfCJk4LfYIbHPCIcme1eHB5rQ3nOaoICModTdGE2J-AQBB0m62AV2OTxQgoPuIuCimONW4KYJCvbgNrMKJnjRIYUKOkhuffwuvi-1_T5X3F4CD5gnWjtHkGVVnrUB0YmNGWbmKqhE04H3PkzyHQpsMMRIYvwDzTL8L5rMkVMEoVg2jFv9DSgG11vHyoxwrT3GGw1588f3V9NR5qjffi4oSNiWqYWc5-58F_c21fRS8ctfvrokxlAWqaMVyGQHGziUtd6UVizDVriqDRq0qo1QVcNA922WzLOAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=MtTeS2hDWl8UbWrheQlvhDLu_TfEh5HMrKkx0oLQKq2nPr4jwAHShfCJk4LfYIbHPCIcme1eHB5rQ3nOaoICModTdGE2J-AQBB0m62AV2OTxQgoPuIuCimONW4KYJCvbgNrMKJnjRIYUKOkhuffwuvi-1_T5X3F4CD5gnWjtHkGVVnrUB0YmNGWbmKqhE04H3PkzyHQpsMMRIYvwDzTL8L5rMkVMEoVg2jFv9DSgG11vHyoxwrT3GGw1588f3V9NR5qjffi4oSNiWqYWc5-58F_c21fRS8ctfvrokxlAWqaMVyGQHGziUtd6UVizDVriqDRq0qo1QVcNA922WzLOAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4rlSwOunsUYhMNibT9xh_5vrVEuG78ktCHLiCTVEEgEv5FoUY-GDy9kBZQ816tkritacbRX-CKbcZ7L1h0NxzMHuLpdCawCB1lnz0hEXs0Hyy_3ujSLADL0ckL5fw2kSTcY1vcY51EwOR3dOxcb9ffIQv3VB5mQoDB08F_Ff5XlVW-VpHvYinVMNWwMx2LkFJqV2_p8vtKf0i1kxH5AowZZCfAY_YA4koSr7LPxbLLjPCIynHGoSdF_l239oGhWh78DY11pw97WXPSwKUkjHGqwjnro6UHdtNAdHeORdpNYJnstO1MMpk-Fy0vs-CRQdDv6d5DcBOsHoqOEb7vDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=pLOV8syThoreSyXQAUwurIp4OBWjwqcq6OJ3vkGVCX7xI4n7E1LxVOLvM1GXDMnflIjHsZ0RuhpHB3ttCEaueaB2aAihFwAofZ3G19TTjl45556EV-cCDAnO5V5oxlfSX594HQq4cOKkZehfXv9jUaZE2wLnQ7_UqTaUG8kgxf9scCSJ03lpgA0kdBgYsdp9jELOQnGyiAiaAdvYeXmASAJox_eKaL3dwPvk_KHKc9qchGzHXOw2bSCdx4Aqdo0gyUARgTg72uXq7lXrQVrQHKywBcRsFDv47p_vGg7929hr9frFBeTg1g-lYwSM8WQsX_-Z1jgsaSUYL1T2d-gpIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=pLOV8syThoreSyXQAUwurIp4OBWjwqcq6OJ3vkGVCX7xI4n7E1LxVOLvM1GXDMnflIjHsZ0RuhpHB3ttCEaueaB2aAihFwAofZ3G19TTjl45556EV-cCDAnO5V5oxlfSX594HQq4cOKkZehfXv9jUaZE2wLnQ7_UqTaUG8kgxf9scCSJ03lpgA0kdBgYsdp9jELOQnGyiAiaAdvYeXmASAJox_eKaL3dwPvk_KHKc9qchGzHXOw2bSCdx4Aqdo0gyUARgTg72uXq7lXrQVrQHKywBcRsFDv47p_vGg7929hr9frFBeTg1g-lYwSM8WQsX_-Z1jgsaSUYL1T2d-gpIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=iZBbDQWr-Cq3xoiYvkPaahd5V80n5x_-4oYdo7ydgcV077oeQcU-hZub3viSak5z2algtZ8Oi4IbiNRaDyK32RhfUnAZ-0BI4XnlytVowiTZiLoxY_aYI4sV17SiURdHcdEXqmb-i37MU0k04eSTc3RbHs-BOsGYICVN79Gi2ValnfHNcPZYEnbRwr4WkiITliRRhIHqH1yPUf70sBfwZts2Pnl7XeiU1Qc-ZGjvt92r6DEZ2MLb2b0pA35c-kLKHUcgdSllzKCKR3YuOLSoJVCDStBht4WU3i8fEDM1VP8-rWq4yqt7w4NJWpcmFnJ2WDy5Xe6KKGAq5YBX7z4eSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=iZBbDQWr-Cq3xoiYvkPaahd5V80n5x_-4oYdo7ydgcV077oeQcU-hZub3viSak5z2algtZ8Oi4IbiNRaDyK32RhfUnAZ-0BI4XnlytVowiTZiLoxY_aYI4sV17SiURdHcdEXqmb-i37MU0k04eSTc3RbHs-BOsGYICVN79Gi2ValnfHNcPZYEnbRwr4WkiITliRRhIHqH1yPUf70sBfwZts2Pnl7XeiU1Qc-ZGjvt92r6DEZ2MLb2b0pA35c-kLKHUcgdSllzKCKR3YuOLSoJVCDStBht4WU3i8fEDM1VP8-rWq4yqt7w4NJWpcmFnJ2WDy5Xe6KKGAq5YBX7z4eSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=g0AjSRRBjnr6iERyyMirujriSn5MJuSy6aPd7CgxyKCTFlIC3L1bNmfKxpOs7k224AWdw9Z84cTNA0fHXszOTOFA1p7FxuVPtExQvkOYbtf-K0L-El1o_GNstAywVUOFUHBwP3vyy14gril17u_jUdWl0CKZfLvBPGGRehSLg1iLgQ2I_gw3u5mDOMj7QAyyLv8DrY5Ro299-4GhIL_DFwuWhSxOKszSTMUl_uksNEW3c_fiAuA8MCov21B1j4yKCZjKHS8CoHRm21k9OUWPDrjv5AxT6yX-6yFLWxUjs_Gkj16ECX6ma8YzDUTG1HBXR-G_XTRufj0yqw0qiUqqgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=g0AjSRRBjnr6iERyyMirujriSn5MJuSy6aPd7CgxyKCTFlIC3L1bNmfKxpOs7k224AWdw9Z84cTNA0fHXszOTOFA1p7FxuVPtExQvkOYbtf-K0L-El1o_GNstAywVUOFUHBwP3vyy14gril17u_jUdWl0CKZfLvBPGGRehSLg1iLgQ2I_gw3u5mDOMj7QAyyLv8DrY5Ro299-4GhIL_DFwuWhSxOKszSTMUl_uksNEW3c_fiAuA8MCov21B1j4yKCZjKHS8CoHRm21k9OUWPDrjv5AxT6yX-6yFLWxUjs_Gkj16ECX6ma8YzDUTG1HBXR-G_XTRufj0yqw0qiUqqgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=DB9cLRFefIRcFusophq65Xz22ou2blueKW8_YLIVgsnsWPkyz7VEAnmV_gx4RFWWyyyiJnzxBfxQlroCMwmGApxx0X1o3UKScGSO_Yw8NfV6AhPV7QEbrbSzx3PgKIcsThRBqhgKJRSXFUyg2WZE-yTSc4ylstTSV9JYgAMSRlYcpRn1ETUlIvl-Zvjj0DX5LBhH2Hpe2_NXdQhdq8OdDocXZTbSFPqugqCLVP4zmNIEZ1apIvFYeL02RZVFHxR0qaO8WQvimY940Y0j2mnJoNSlfTo8FPJPf20ciM8OovwaThfd0_NR6HvI5kFz9NBhJVlluuuK4UuH54E4ANUDQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=DB9cLRFefIRcFusophq65Xz22ou2blueKW8_YLIVgsnsWPkyz7VEAnmV_gx4RFWWyyyiJnzxBfxQlroCMwmGApxx0X1o3UKScGSO_Yw8NfV6AhPV7QEbrbSzx3PgKIcsThRBqhgKJRSXFUyg2WZE-yTSc4ylstTSV9JYgAMSRlYcpRn1ETUlIvl-Zvjj0DX5LBhH2Hpe2_NXdQhdq8OdDocXZTbSFPqugqCLVP4zmNIEZ1apIvFYeL02RZVFHxR0qaO8WQvimY940Y0j2mnJoNSlfTo8FPJPf20ciM8OovwaThfd0_NR6HvI5kFz9NBhJVlluuuK4UuH54E4ANUDQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjplJrRO65BQkK9EFiTdJV-WYuFKemwAuR8buldu7XbhjLyksP4qzzLXtyXlJqbJ1IrY2i90Ap62nSI1J07d1vQzZxqR16L6joka6Fx1tuIGFffOyNOlzg5Zwm3_LLeo-gGym-rBURgJi-fX22Mt003PtfNhUMlD6VPzOGA0VSJsgHQ6GQAIRHBn7DiPsW4nN5bS-w9n_ILXM6n6rLf2mC6EAzgcSoLOgR72aYAEUZGMONMzPR1Ex6GjtvXMoNYbXYd0RakE8RlPSAhNh01_655LvuwsQyiXl6CBSJODbedQNrEE2KHEroAZcrFri30euubnqrkitK7v3sw5aSZQZLxUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjplJrRO65BQkK9EFiTdJV-WYuFKemwAuR8buldu7XbhjLyksP4qzzLXtyXlJqbJ1IrY2i90Ap62nSI1J07d1vQzZxqR16L6joka6Fx1tuIGFffOyNOlzg5Zwm3_LLeo-gGym-rBURgJi-fX22Mt003PtfNhUMlD6VPzOGA0VSJsgHQ6GQAIRHBn7DiPsW4nN5bS-w9n_ILXM6n6rLf2mC6EAzgcSoLOgR72aYAEUZGMONMzPR1Ex6GjtvXMoNYbXYd0RakE8RlPSAhNh01_655LvuwsQyiXl6CBSJODbedQNrEE2KHEroAZcrFri30euubnqrkitK7v3sw5aSZQZLxUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI7AteD6Xa0N6ZTKuXMAi8pGi9QjJgD_vQMvoyJJKbywcG5jrmr_YfiuEi6bZOaJ1TdhGxILNW4_BrD9u-LNK8ggMLtXisLS2Iyf3ub78xRS338sn5isd8QZMgKY3KpUg11lJq41_xttykhBxtSmOQ5ggJo99dTw3p0P-0AghuXbfwvB1xbzt9Ik8F37I7gExsB7TaBBH9NMBF5xvV7eQg6Ij9U2I6JGV6e5DVxoEL_4JglIgIYv_WkIcw4vROYGAsQbl7_KWKGBaEsC_0nakb919kwlbpoTmleUyWRrCz6F_zMKNucs-Ok_l9_zNZAupx8LQ8k4kcVE6GaCfq19aeto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI7AteD6Xa0N6ZTKuXMAi8pGi9QjJgD_vQMvoyJJKbywcG5jrmr_YfiuEi6bZOaJ1TdhGxILNW4_BrD9u-LNK8ggMLtXisLS2Iyf3ub78xRS338sn5isd8QZMgKY3KpUg11lJq41_xttykhBxtSmOQ5ggJo99dTw3p0P-0AghuXbfwvB1xbzt9Ik8F37I7gExsB7TaBBH9NMBF5xvV7eQg6Ij9U2I6JGV6e5DVxoEL_4JglIgIYv_WkIcw4vROYGAsQbl7_KWKGBaEsC_0nakb919kwlbpoTmleUyWRrCz6F_zMKNucs-Ok_l9_zNZAupx8LQ8k4kcVE6GaCfq19aeto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=o-3NujBurP5G3n-chU6SA1qhwbDNQ9ndMUqDTa36MFfCCJOQWJGJWlN0shz4V_dvxp2C4hGVprSK8uI5hLK1hA9kcmURlELouRUbc6ZpwVEeTEXQckVqh_apgnImwc1qlG5297r80reCQiKWNh9Ds2OgrdqWJHhOvyhvYD-gdFwpVI_CmbZ3naMpHYyB2cwVUMCU8zNXlKi3fo9jnV4Mf0zji_rh6dviDUdKC_srMFcUzHUM5glHQKZ5blUL7T-Z9XmNsIY9HisKlziej7xnAkF4Vmop-NHb_NdtZYvx7x1ba3PG1eVYWM6s3RAf03FP9zELIxyBkSeqBedyUSkpHZ1EFwTrtpxoEJwbL4nAZJq52YwzKd19qhr2VJp69u5ezCL0uhlJVeUBNeTjIsw2Zc01ItIDBYn8l6qGbBXJLRtz40Et5q6wPTV9-qQTYaTMaYPoBSRSIHmfEg0IymrZdRG3uveuzBMZqD-pT0Y4fgmKXV2haehHTqK_0u3zn8Mbgx77mCmiMqEeC_YtHSUI-E18ZE8_RUvSS3s_W23N2SIXAxyNmE4WluglDLUvyGvn_zquMx5Uef9nFUfnfMRtKHmdDfnFW3iT5HlmZr9-GSgTjf9sMEKiBsFc5xKMiGYZvN3D8bENfpusrRg5sO_KHBmoj6WO1WZ-XeMwHNAt-Cc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=o-3NujBurP5G3n-chU6SA1qhwbDNQ9ndMUqDTa36MFfCCJOQWJGJWlN0shz4V_dvxp2C4hGVprSK8uI5hLK1hA9kcmURlELouRUbc6ZpwVEeTEXQckVqh_apgnImwc1qlG5297r80reCQiKWNh9Ds2OgrdqWJHhOvyhvYD-gdFwpVI_CmbZ3naMpHYyB2cwVUMCU8zNXlKi3fo9jnV4Mf0zji_rh6dviDUdKC_srMFcUzHUM5glHQKZ5blUL7T-Z9XmNsIY9HisKlziej7xnAkF4Vmop-NHb_NdtZYvx7x1ba3PG1eVYWM6s3RAf03FP9zELIxyBkSeqBedyUSkpHZ1EFwTrtpxoEJwbL4nAZJq52YwzKd19qhr2VJp69u5ezCL0uhlJVeUBNeTjIsw2Zc01ItIDBYn8l6qGbBXJLRtz40Et5q6wPTV9-qQTYaTMaYPoBSRSIHmfEg0IymrZdRG3uveuzBMZqD-pT0Y4fgmKXV2haehHTqK_0u3zn8Mbgx77mCmiMqEeC_YtHSUI-E18ZE8_RUvSS3s_W23N2SIXAxyNmE4WluglDLUvyGvn_zquMx5Uef9nFUfnfMRtKHmdDfnFW3iT5HlmZr9-GSgTjf9sMEKiBsFc5xKMiGYZvN3D8bENfpusrRg5sO_KHBmoj6WO1WZ-XeMwHNAt-Cc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfSisRu_CVcbkehBG-05bzOea3UAMXFgmk0-TG6NoBtKUHZVJlhCT42iMFXIQiA6XCYiw3mAyfvTCIvanZqFUHlWvxBYhj8w7GGyGaCzvJ5P6wzJpgqsQCgs6NB3cbhngTtss6LpjArXPZ4gTl8reKNA38TVQnl6rtEY5DkMr1hlvBw-7EfcFte2txRQHcEXgUqQuQ43TA0KJIB4ASSfEtFMjWp5zHMItThSk7Yyzw-SCXxub7afuJWYAE-UmckGKTJRIIKHyczo-87YbJvd1UqnW81Z7g3M9jSs8L2Je1TfoydLcgipYi-0yPIajqJvhr0lZ_TnScv17AvTHHNKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSkE2kE7qlMjRdjfEgisSSdCaa-EHu6EU_btOfZqkvCoIwRSxicrBrx7pAvaTkE0aqvGP0retqy84pjm-_X1vBHBvCC7o73ttxNcq1BueLVzOyn14_NhpfgDKWnEbuM5cFw_Zs7SCTsSLQCk1kdre9g6sWK4H_YRvfFCxJgWHxS_gLvT-XJwGIT3GvB4DPlTHyILd0CiriCI_lCQxEFIySUWfEYEzrltFFQS0MO1msEKNWFqL6L9q2NCW22Mz_XvM6261_kbVgnk1uj_IqdBIFTX8-1znZQ1I4ARaGTDpqoW30-4y_RUHLq345ldjb641SgPBl7_SIdMBmM69mEQLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=Ao2SPYlAPq7pFUpSDWupFkuB2q9rVRnMWGRAogFSkhPwIgXf1rQER_3qLwvsdRf0LOv4lTnjACUDT9fjKJmJjST5c2ndudulYEWFnIZI_uqXrbv2ML-H6Uspxk9XPRg4TNYKhTW7ge51H0mRUpNPz9A0oVujirE0NSSVs3N8e9lHkrXY1SsHXpK-g8x3EKkRlMoPk8gec_3kn_6SMGNxLS3NH8MfHqkrJ3s_g_bzvXzzMqBupNY3iXdKwSzpHHfUVyzrodqpnPih2m52G4NJrPRhL1uhC7FB2_6PuQrsg23Ldi-iOy5AAyh0bL4xQAEbCf7XCf4niZdMKJ8CuY0QeTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=Ao2SPYlAPq7pFUpSDWupFkuB2q9rVRnMWGRAogFSkhPwIgXf1rQER_3qLwvsdRf0LOv4lTnjACUDT9fjKJmJjST5c2ndudulYEWFnIZI_uqXrbv2ML-H6Uspxk9XPRg4TNYKhTW7ge51H0mRUpNPz9A0oVujirE0NSSVs3N8e9lHkrXY1SsHXpK-g8x3EKkRlMoPk8gec_3kn_6SMGNxLS3NH8MfHqkrJ3s_g_bzvXzzMqBupNY3iXdKwSzpHHfUVyzrodqpnPih2m52G4NJrPRhL1uhC7FB2_6PuQrsg23Ldi-iOy5AAyh0bL4xQAEbCf7XCf4niZdMKJ8CuY0QeTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=rYBjWzqCYKmuLM_4Sdj3V3DCHmByPxOnQxaVWKwYHBfWZf8pPIYWeeBU2dWrOpGXA-TrDaQ9U0AjGwuNh8zs5DIBcAS5uhx-ovW1l-d7kIUOlx2MzUnhdJrI4sg-zqMF_PLApvKcVXUAV_LVMh_vYH89iHrKfuFayTeafxvmH4v7sV3qmbSpbdI9Efe8VPmvxKFcGANJ0m4O9sn2XHWj_EETz2G6kvIPszlB6iaE95mbRBi1MlE8NwcN2lZILBEuIGta53GSwZ2CrOY3J_gbq81dRFLw3qe0mqY6onEopDchx2ad7tNK94jdK3bB_lN-pqLfsATat5jmCgYiN12K1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=rYBjWzqCYKmuLM_4Sdj3V3DCHmByPxOnQxaVWKwYHBfWZf8pPIYWeeBU2dWrOpGXA-TrDaQ9U0AjGwuNh8zs5DIBcAS5uhx-ovW1l-d7kIUOlx2MzUnhdJrI4sg-zqMF_PLApvKcVXUAV_LVMh_vYH89iHrKfuFayTeafxvmH4v7sV3qmbSpbdI9Efe8VPmvxKFcGANJ0m4O9sn2XHWj_EETz2G6kvIPszlB6iaE95mbRBi1MlE8NwcN2lZILBEuIGta53GSwZ2CrOY3J_gbq81dRFLw3qe0mqY6onEopDchx2ad7tNK94jdK3bB_lN-pqLfsATat5jmCgYiN12K1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=mip9vGDWf4ifiqNj3vQl-JKbaF9srW7EqWzg7c5fi06pj5V3qsj1xrbL9NDKVPdXoz0B0Lzi5IuBhizbGYXlxb4B7UXmSvu0DuJkmem4EbNBRZDfek_hwlycjt8Wo6S0P9-Xc9ZvdVbDMnVpR773z_LntLULvvX1TrFwp5sYYYn6Tw9sFZBI2ykBqQatQYKiQWgd5j2fQ3dPeZc_M1CYWECZVgrMhlXB8dWrk3eUgR5Hs8bkbVEAq_Jg51ksHBP4lo73UsJtuDx1BYJ06M-JBUUeNgfJhFcApPHGMHop9njV0c7Rht_wFLC3or0AYzAA48Ze1IYWe1lwjXrV3Yf6BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=mip9vGDWf4ifiqNj3vQl-JKbaF9srW7EqWzg7c5fi06pj5V3qsj1xrbL9NDKVPdXoz0B0Lzi5IuBhizbGYXlxb4B7UXmSvu0DuJkmem4EbNBRZDfek_hwlycjt8Wo6S0P9-Xc9ZvdVbDMnVpR773z_LntLULvvX1TrFwp5sYYYn6Tw9sFZBI2ykBqQatQYKiQWgd5j2fQ3dPeZc_M1CYWECZVgrMhlXB8dWrk3eUgR5Hs8bkbVEAq_Jg51ksHBP4lo73UsJtuDx1BYJ06M-JBUUeNgfJhFcApPHGMHop9njV0c7Rht_wFLC3or0AYzAA48Ze1IYWe1lwjXrV3Yf6BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=J-fR-GJSY4YCZSZwNPiUU-QuzLIT2aNzKGB0GOSjg4wcp2Jkvqu_S7gpsOXmR8lxOOaeLm29BXozlS1ntd-uiVybChrGfTxSpOS1EF7j85S_w3jgABHVPF_2FQqBPeAMDyk4DsEy6x26_DvSiljLTzZ6LaP2oSx48M-FtzLiJU74SrjChkBnis4Cx0-ZMSFKcie54L8K-4TL_ddT6jIxakwRvMXeIIkXU55W9YAPE2Gj10pS1vSzCgrIAqvMpFNPjqgKCNaiB6yK6CVZR37G8Wn8o41rkwoju7Yd4vKd0M98VzFa48RO5pjUS3lZJEm-HJkWkYFk75bFvvhsPhffvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=J-fR-GJSY4YCZSZwNPiUU-QuzLIT2aNzKGB0GOSjg4wcp2Jkvqu_S7gpsOXmR8lxOOaeLm29BXozlS1ntd-uiVybChrGfTxSpOS1EF7j85S_w3jgABHVPF_2FQqBPeAMDyk4DsEy6x26_DvSiljLTzZ6LaP2oSx48M-FtzLiJU74SrjChkBnis4Cx0-ZMSFKcie54L8K-4TL_ddT6jIxakwRvMXeIIkXU55W9YAPE2Gj10pS1vSzCgrIAqvMpFNPjqgKCNaiB6yK6CVZR37G8Wn8o41rkwoju7Yd4vKd0M98VzFa48RO5pjUS3lZJEm-HJkWkYFk75bFvvhsPhffvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=GtLomSbwVvBpClrzQzTwjmDrehfS8VV1r-JgseVNMMrd54BVtGfmg4g4sWxJDxlTBacSmsu2OQQbSIrbhQVb7-rHPkV0NwVnHTPGUC4jY8DtI-L4wVhM-ttaeQ7nI7fR1ZLCirIvoFh-dYGDkhUw_MycCYcJav-rp3qvdt5uJ8Xo5XlXhI75Tf_WRL40dLslNOM9l7FMM41P5ilxPBwvpTyOTOPvg3OzezFbiaUmqp1vribr4eDbGeDNic5hDjacCLyL2gROxwcRnArmGN13Hqm_wigP5fmR_2wF2GT9LuKSQBuTUyElBEKc96tp-oQmwDoUXhgPyD9mgEKd2LLT0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=GtLomSbwVvBpClrzQzTwjmDrehfS8VV1r-JgseVNMMrd54BVtGfmg4g4sWxJDxlTBacSmsu2OQQbSIrbhQVb7-rHPkV0NwVnHTPGUC4jY8DtI-L4wVhM-ttaeQ7nI7fR1ZLCirIvoFh-dYGDkhUw_MycCYcJav-rp3qvdt5uJ8Xo5XlXhI75Tf_WRL40dLslNOM9l7FMM41P5ilxPBwvpTyOTOPvg3OzezFbiaUmqp1vribr4eDbGeDNic5hDjacCLyL2gROxwcRnArmGN13Hqm_wigP5fmR_2wF2GT9LuKSQBuTUyElBEKc96tp-oQmwDoUXhgPyD9mgEKd2LLT0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=QjeowC9st-Fx96JtbuDF9oYduHYTiDm_pgE4yyGpny1CYd2RZqsrP4XVypWS6EeEwIUlEibAZdH-3HVBXavgvsiv8A0LtX1fPPp-NvU4Hk33gP2ODwb7x4NL--GyjmgYfqVeRO__9UIQ4-7XjXfhDFgEqOcCcsad8nf3Zt8XRGlDggMKKlU6bRw1czGIeZrmkipeQRVQ7wmS3Z0mJawXsy3mHBivsnMGw8w19MetrbjYZ8RbbgCwVJo7iNvGZ-Y4CzZTaIn5pNBw_tRfckKaKepabRZc9ZVtzPrnIINyR74IHcOofzkRRigVehSs_qEZpU10iK97TxX_T-hJC1r3iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=QjeowC9st-Fx96JtbuDF9oYduHYTiDm_pgE4yyGpny1CYd2RZqsrP4XVypWS6EeEwIUlEibAZdH-3HVBXavgvsiv8A0LtX1fPPp-NvU4Hk33gP2ODwb7x4NL--GyjmgYfqVeRO__9UIQ4-7XjXfhDFgEqOcCcsad8nf3Zt8XRGlDggMKKlU6bRw1czGIeZrmkipeQRVQ7wmS3Z0mJawXsy3mHBivsnMGw8w19MetrbjYZ8RbbgCwVJo7iNvGZ-Y4CzZTaIn5pNBw_tRfckKaKepabRZc9ZVtzPrnIINyR74IHcOofzkRRigVehSs_qEZpU10iK97TxX_T-hJC1r3iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxqn8dwMcvXLIdZSPKYqfm361sQ4hghS03d1Nm6ps6tIkeTQLuQz3_rBv-WK7m-2dkYncsDLzWvfgczk8ED0W7kWagK5hRzs6Ui2rzZrZCHHfwuZxfpQRy9tEslff5dL6agB8lxD5Ep6g36ffnMUUNr5uYvQlYmBhGrsJE29eD4fVIdm3IcDSZp-WSbM5QEOlwIJQwcUufYGsHSbK713ai8c6excZIzWQVmYJX-hfJX8i_0HohNbhC1YWV4881qc_z2326IvTpYjQKWaiH9g8M-QNFs6GxkInUZJ0HevO5X0almoIDwOClJmyr9KfaD28MYZV5c66iY7AYigkgyTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFulj_JiNzR4USKZnA-xlmAP9hKDBXMkIe5TguKvIGhzbLPzO_lh1iIB8IDqNH7Did8njSe5Lbdhrs85Woe0HKxGN35Jf8GVWTrtCHnAm5IXss72VKP0TGxh4_knZwa8rJ9_VnygMZDNYFDxo2Vb1Y0niorQrXWwIu3j7cpTEbcHPI2MIO6fs4eq3F3WsjbWNAjFFzn8jB-Eub0BpabDUfNQU6FiucndHhg6ygFYELkO5dCmegs8NvI-5SBE03HjpGHrUSsfQgeLaaL_qaUlUtPm0J5GHUapRvS-daEox3xyJHY97e_zgjeiMm1DtHw7FSsuZmAkl_YoJJVRX5OdhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=oycoAKqsGyNTT9TsWQhDDOQfWmJq2gvT-8JQdsF8w6UGkTzua9AmpZ2CL1JkpQO4DIYB8JX-SJUcpWmNDFL_HLWjpDJIeNnk_zSV6EvHGd5U2TCo5PpgTPA02_wNKhIFgmPrm1wQcxjA3dpZidTnnM2Bv_ViGoGI-vhJC30ErFbOC5m2jxrFwSHVYwLUXwgO34IXUoTX4qdmIHOrfG26a-NuykMTDjuta1TiO4zWzyU1aHZMsqZuh3IizIPbmA15LjuCg5GzYBcdxSubWr2RVP3Di6dTkqi71HuOdxgO8VxtC4oNK45XjxwQ7DNrTjCslk6AKnIGmNe_olwNnri2Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=oycoAKqsGyNTT9TsWQhDDOQfWmJq2gvT-8JQdsF8w6UGkTzua9AmpZ2CL1JkpQO4DIYB8JX-SJUcpWmNDFL_HLWjpDJIeNnk_zSV6EvHGd5U2TCo5PpgTPA02_wNKhIFgmPrm1wQcxjA3dpZidTnnM2Bv_ViGoGI-vhJC30ErFbOC5m2jxrFwSHVYwLUXwgO34IXUoTX4qdmIHOrfG26a-NuykMTDjuta1TiO4zWzyU1aHZMsqZuh3IizIPbmA15LjuCg5GzYBcdxSubWr2RVP3Di6dTkqi71HuOdxgO8VxtC4oNK45XjxwQ7DNrTjCslk6AKnIGmNe_olwNnri2Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=HKQFMRWyJ5EYGsg260nhRP3LSDI0lLqIbVGcJONL5SL0AuuPYKzpU56sz6-k01nSILbWBeY3DfQjmXLdhe08o84vWIHce72bn3LtV-fvAYR27pWfi-wK58VVX5QaN4YXxLXBbajsAj81oRoGv0nKncrgENnZTkO4kL7U40bGKKVt6oH6JsfFWLD_2fdS0gA9WtUCs71XQvU4HWvkdYturJdWOePnsia9sZ82uGdrRZWTxxaQFtFznx9x0Wgi4_dOny1UJu9v6N9YRCwDC1d-5g7lTwbjZZb12UbNLyA5oWj858B_d-7qwm-eWYgEs9x4rTAogHon63l3-5Up_6Avy30qKgB_Qfcb5Je_TVUKoQJkFyItKVl9qsfMFzAlo9dJJFVq1QQNL6Xd1XwCwCAoA5utA9wcEFs5jNTx39f1I_MrG48xIgd0_LxeHKjQ31FYUic_6vB7ZETMVbvN4He3HwUCOjqZGm1BHrIBVWuAcT0suzdKtL5yUcOQwUfC5MJtx6Spx4B_tvUvbbCHqZwgH46vbftUpN-wjGx98IJPxExJ1OOTy7SWdok4C2BmCaFGTO-BJJIHrKAYypPbqHg6IbhUGn8DVQGF9D5QzRAR6UjkmAdvdNlb-2MhmmnhoCx6jNuYJS6QsBFZpqdTzmI876WExyEcLTxYRnMJsFKiFsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=HKQFMRWyJ5EYGsg260nhRP3LSDI0lLqIbVGcJONL5SL0AuuPYKzpU56sz6-k01nSILbWBeY3DfQjmXLdhe08o84vWIHce72bn3LtV-fvAYR27pWfi-wK58VVX5QaN4YXxLXBbajsAj81oRoGv0nKncrgENnZTkO4kL7U40bGKKVt6oH6JsfFWLD_2fdS0gA9WtUCs71XQvU4HWvkdYturJdWOePnsia9sZ82uGdrRZWTxxaQFtFznx9x0Wgi4_dOny1UJu9v6N9YRCwDC1d-5g7lTwbjZZb12UbNLyA5oWj858B_d-7qwm-eWYgEs9x4rTAogHon63l3-5Up_6Avy30qKgB_Qfcb5Je_TVUKoQJkFyItKVl9qsfMFzAlo9dJJFVq1QQNL6Xd1XwCwCAoA5utA9wcEFs5jNTx39f1I_MrG48xIgd0_LxeHKjQ31FYUic_6vB7ZETMVbvN4He3HwUCOjqZGm1BHrIBVWuAcT0suzdKtL5yUcOQwUfC5MJtx6Spx4B_tvUvbbCHqZwgH46vbftUpN-wjGx98IJPxExJ1OOTy7SWdok4C2BmCaFGTO-BJJIHrKAYypPbqHg6IbhUGn8DVQGF9D5QzRAR6UjkmAdvdNlb-2MhmmnhoCx6jNuYJS6QsBFZpqdTzmI876WExyEcLTxYRnMJsFKiFsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=vq8jTRzWxEOCvf7206Wbixj3ZFYmR9tSLRbtXX8I7GajMIhAYs8PiflZa3mXz3IyCfWQSkIvufHAoGcCIbt65nxDvdm--Y1hnjFmjsmPiryiHakAGGtQXvlMdr77g15Dw9j8LknoZDjiwTpv13Ku2n2rWQKNuzMYCpva6t31gcx7tkHpiqqDVzHGfxA9viAtUIDgiHQwQ2cCedQB28hNt5G_nTsb4lAdLoN4yKQe8KeiHAeDfcV-mgjbX-g-Uu9FkDfvgTyiqYGdsgApUEtgKcZmVhk_Up12ZPS5hKRWjTyNtqF12O8gFifpullcjS0RacCP1TLoKQLVOsJFAexr2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=vq8jTRzWxEOCvf7206Wbixj3ZFYmR9tSLRbtXX8I7GajMIhAYs8PiflZa3mXz3IyCfWQSkIvufHAoGcCIbt65nxDvdm--Y1hnjFmjsmPiryiHakAGGtQXvlMdr77g15Dw9j8LknoZDjiwTpv13Ku2n2rWQKNuzMYCpva6t31gcx7tkHpiqqDVzHGfxA9viAtUIDgiHQwQ2cCedQB28hNt5G_nTsb4lAdLoN4yKQe8KeiHAeDfcV-mgjbX-g-Uu9FkDfvgTyiqYGdsgApUEtgKcZmVhk_Up12ZPS5hKRWjTyNtqF12O8gFifpullcjS0RacCP1TLoKQLVOsJFAexr2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4pBCFwRvvt5kS0gz6hKHlyzGBOevxTq2oRwjM2ifxFnWip0OS2vsbEXwNLUJuVk55dRQI08Xj-z0g55N3tmtHE5NRG8gqc82OUy_CRNjCwLyB7oeDWu89OK_-rVfgcTBtb4pzIEZE0LdRw9IJ9yIEgslAeuA_2ReYxiE_UsJnssi1GD4nOE6Tjzinf7Brbi23Pihk0BRSVs3ZbSUGXBtxgZF01blFkZna1firvN28FgexuLCe8vcYUj1xEbOgfZQS9c7lWBWvt3xgy5qyq9aiKJ7FAiEOodSeOmuNxXiRhDLTNFo4TTzrmnN0iMo0YVGPhU1_XeAy-0Ueqk7J6_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=Tu0r1z4YuAHz7AMO-GnZb-nFSpehsEaPJHjmShXEmGDQM2s9A9X7k8Z7GrAR4u30l9xJXEQWntwk24eSh__u0XYRGGYhrHex_zwvWUCtHsMgaEyffrwSTB2cN3kHODFDc366zHVcSdKn8REesVd9zjt6PzIpfFOjMoFACnpW70rHqn2jrHH8u3ftyc6GqW5M7YdIYLoft6FDlqzzBMwSvzyMN-LBxJCQod94ZfAzBsHRv7kBu2bBrfJGDM4bXSETY7IV2p4iP_Rn4Mq77yaJlO57OnSMLXSJOv63NYezlFFKeP0i0u2mWDKW564oIsjahj_XHDVUK8iDpd89DS2cUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=Tu0r1z4YuAHz7AMO-GnZb-nFSpehsEaPJHjmShXEmGDQM2s9A9X7k8Z7GrAR4u30l9xJXEQWntwk24eSh__u0XYRGGYhrHex_zwvWUCtHsMgaEyffrwSTB2cN3kHODFDc366zHVcSdKn8REesVd9zjt6PzIpfFOjMoFACnpW70rHqn2jrHH8u3ftyc6GqW5M7YdIYLoft6FDlqzzBMwSvzyMN-LBxJCQod94ZfAzBsHRv7kBu2bBrfJGDM4bXSETY7IV2p4iP_Rn4Mq77yaJlO57OnSMLXSJOv63NYezlFFKeP0i0u2mWDKW564oIsjahj_XHDVUK8iDpd89DS2cUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdsbe81osTFb4pOrF4_Uo6icxw-Q09sFiWXlnPoajV_h0TDHeDQNoX5k8rZPDljX5bDu9Qy2--x0RoxUVlJULqhSzd54MhIJvcYKp2biD8L7n6XnvAEXpTKA--U3p8IgT2xRAFNO9pMEOUXPbmLjb42yJy1D_jG8AmzdO9TRxk6S4JH3yBC3ptHRjvnj1HKk-FZBoST-yVCC37fxCKefLxSumde51pChikq97NSTRkx7V2IEcC49bOswwRjskatp5LNEV_U8Uhh02wKywJ0Yl5xaY-yM3FQ10KVZ0fp235DRAhXCgaQahwf4Yf-mjtl_yrd-JZhwhBE8S1WVEUxFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMjM-qCDSCDoAAvWSIOzOuchlUMo25O2F5EYCbXoSIzX6-peOSiywf5KV8WuMb4DjBhSovjQp0HmAMyCyAiWhW9U6lj-8PeGNCWY4aVqt5BBWnBYVIdMid3cufYiNdqBle0_yImu9_fnoZMeS5zBA8Qnqe5y1k-hdydPlQ7esy11go31bbYLssm_ssDSf8XaIJpdm99TtjNxyIsxCJLaN3ZE6yUQ_3ZiScTey0S3hRZH0diRcrWvSrXXCLJxcpXszwxE6zqAZwrErypbzenTk7JS48UolhSMWjamY47GnFCMHxVmwGiaIXTBnYrNeMyBSwqlfzmDpVCItBaprksHwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=t_zVuX0gF1ZP9OxWDedlp7Eg7xn-RcQwKs-jWYuuTIZAyZ1crbvr1voPKxFBMh-UlDC79iAgIvgvjt7cV2VTnYXweuI5YuuEBQgrBzQKfkZAnEcvhBb2z78j4QpIgDJhzDSsJEUyoavMAX45f3A8bLIxNqNFiony8vg-izNo-pKg7en93oDcje3Zike5IMNsC69WInixeHtl-P4MqpP6bER_NDQecRAL2h-RYY5xk-GgagQoOSm9kufLKUIhcIiLxL7WStS3dDOg0wra21vGbptR_nfwMJ3ryJbemitgSx1yV6SsNcgWWWt58NiUJBt5gvK_Loonzw0JVxrGDaiGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=t_zVuX0gF1ZP9OxWDedlp7Eg7xn-RcQwKs-jWYuuTIZAyZ1crbvr1voPKxFBMh-UlDC79iAgIvgvjt7cV2VTnYXweuI5YuuEBQgrBzQKfkZAnEcvhBb2z78j4QpIgDJhzDSsJEUyoavMAX45f3A8bLIxNqNFiony8vg-izNo-pKg7en93oDcje3Zike5IMNsC69WInixeHtl-P4MqpP6bER_NDQecRAL2h-RYY5xk-GgagQoOSm9kufLKUIhcIiLxL7WStS3dDOg0wra21vGbptR_nfwMJ3ryJbemitgSx1yV6SsNcgWWWt58NiUJBt5gvK_Loonzw0JVxrGDaiGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=OPQdSbO0ZbNByC6bj3Ue_c328e777TVUEKkeJVhVdrD2HNab8bqqpLTv_QuOLrIvVFhq4FGueJEEiYv4e4XLZr3aQS08VMLzR29VvXc6lxHC_hs23-xF11zisJlnGH_QPqQQCWhaBIhtsUvloTrPg_L4T3D3VexO77AVOYbebtDMqhdbWRntExYeI1m7XJT2FjZgMQhTksfdkm8VAFpVaDsIijlWTBgKXjjK1QtyfyVT6_ukX_OwUZkaJJolJOi6fGKFzMo0JuezogV753eQbYh7wLlnR5j3vm43xesTfQWW4sNQ6lgYjVpA8OT063p1EOjIc6xvaNKBH42xaVZ4QA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=OPQdSbO0ZbNByC6bj3Ue_c328e777TVUEKkeJVhVdrD2HNab8bqqpLTv_QuOLrIvVFhq4FGueJEEiYv4e4XLZr3aQS08VMLzR29VvXc6lxHC_hs23-xF11zisJlnGH_QPqQQCWhaBIhtsUvloTrPg_L4T3D3VexO77AVOYbebtDMqhdbWRntExYeI1m7XJT2FjZgMQhTksfdkm8VAFpVaDsIijlWTBgKXjjK1QtyfyVT6_ukX_OwUZkaJJolJOi6fGKFzMo0JuezogV753eQbYh7wLlnR5j3vm43xesTfQWW4sNQ6lgYjVpA8OT063p1EOjIc6xvaNKBH42xaVZ4QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FIDZnWMfgj0XyiMsCCH5fGlJNcGwn2kfHyhUXhXqVMJtfLO-BOn2S3SdJiTnjpowg9gXblhgINkDR3R820GUm3zGEVI3U8WD2Dy09Ic1LubF86BjaLtzr5SCMO-MDk0Sh7sHHkstU7KPn2txNWxmypevc8fFzrJfCxFY6ihONDg3Ni-_VGwTdeCWhonGif_mS9Y-V_2_j3rtuKh_ZXoE8uINVxGnAbuA5vi10_iRHcuJowvEGkLboZCnBQtMnH_yzbx-Z_I8LUCn6YycCyIUP-HsGVbthqVTgD16zv6azxzG16EjGF4M8OcCQYqNBVZwxeUsZlN0YqgvPiziNg5R0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fB1rHcsA7xF_UnpEyAGMm_97354R-_SrcIP6EmaJJk5Q3aWpEEPtuR2NX2lUihvywcozR2xKoJLzu1x-I7Z5YwflR5S-C6NIYMzUtThMO5m-Bnz62ysUQ24mx-4pjl2X6AwKsLvn8Y_4tqP2e6GSgtKhBwlq2FqqphNH4_UGBqdamLELkserntDZUY1PnUAd_o5eLyD8OTSf6AK9P_mUkpfGKPeRHgyz2V1umuMM1reuC03vlVTxeuYw-BgaCsTiiiPDQmCqze1TAXJYR87DO7pRk4ERB6BFiGkJdGG-sCkuaroAZfqNu8JmcwgHRtUBu2sjoINpqwEi2HtVMkhQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvBphJowgokDWewFx1SzBP8_jY_Dt9HPvkWhKAQZMUy6CIe01aqNdFPp5JzztNsFcPs58-oRWH315_ETFUh-SPbQlpGSoLo_IFZ9yirJhki9nxuRBNu0pt5LExLRksVC08aKC3Wr9gxlfBT890XAvQZRaynZvvzL99gXzjLvsmV5BeUQA7U89wGVKADJc--ETLMy6oZG5LMh1HTtmjWofzoCs2syH0x9FnRsHMIDwrgapbgPnm6raWEpQCz9uO8jIN9HlYiZBoCEIEKNpILvFNumz45Hduh1Yz2V_lgCdTf6EtERzg9xKitYU_ax5wGd2u13C-cZH_URABE0KlGe-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=W-QMjc_AwnAlvSVWK8ssaKEqP8rY3Qv-oUrI_KkhbDiMStN4_6xlqPAJLTZUMQkWNVQm9lOrBqVuNUv-IZa37O5iZx8wMOv7xy_tn7UcL2oVEqHH4AbtKnd7vRaPfeTUx3yGcATk6FiuiJWXiUJWyE41Ec8GBtx_eJU08oMLBKFF1YcxGdn6V4Xekcgq05jA-58EdPW8Y82uk36tRwS0Y7-h12R5tHvLTdtJw0igigEscoPPRQ1fcLsaiXhCwj-JRUggBJHt1aL2Y70ogBxkwfJniMk6Qw9AD-RnW64vnAO3PpdKsfpw53O8LGKtgmEU6SvCRRK7WrKlktNjhCuWQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=W-QMjc_AwnAlvSVWK8ssaKEqP8rY3Qv-oUrI_KkhbDiMStN4_6xlqPAJLTZUMQkWNVQm9lOrBqVuNUv-IZa37O5iZx8wMOv7xy_tn7UcL2oVEqHH4AbtKnd7vRaPfeTUx3yGcATk6FiuiJWXiUJWyE41Ec8GBtx_eJU08oMLBKFF1YcxGdn6V4Xekcgq05jA-58EdPW8Y82uk36tRwS0Y7-h12R5tHvLTdtJw0igigEscoPPRQ1fcLsaiXhCwj-JRUggBJHt1aL2Y70ogBxkwfJniMk6Qw9AD-RnW64vnAO3PpdKsfpw53O8LGKtgmEU6SvCRRK7WrKlktNjhCuWQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=kSpw81xIxrCNfukiWgTE-ZiaBCmB9rwDuXrcE0FjEy-fRfTaUDswvrL85HoB_LqE7WecojKcFasigfl3VSzAozeJNncUL7qyzk2vbXqgiaSWcFNrYxR3tdtHez4MNqCa2wMCPAJyqZl8TPeXeNgJfuSgSt95jbEDt0gjGZlbdPNgZ8-97VkJW8YBOFE5oUWTIoJ1GQqFQZVHod63Y3y81NIUsf292TjEsP3pRavXn7k_bmZHra3fCm4_4XB-vjhrii4LsvhUoagamDSgq08H_OPaZ94uGSuQHap7G37jW-WQ7lYvLLP3FT5LDvqJ-lUWihEeGVAkiY1q4AyUo6sbbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=kSpw81xIxrCNfukiWgTE-ZiaBCmB9rwDuXrcE0FjEy-fRfTaUDswvrL85HoB_LqE7WecojKcFasigfl3VSzAozeJNncUL7qyzk2vbXqgiaSWcFNrYxR3tdtHez4MNqCa2wMCPAJyqZl8TPeXeNgJfuSgSt95jbEDt0gjGZlbdPNgZ8-97VkJW8YBOFE5oUWTIoJ1GQqFQZVHod63Y3y81NIUsf292TjEsP3pRavXn7k_bmZHra3fCm4_4XB-vjhrii4LsvhUoagamDSgq08H_OPaZ94uGSuQHap7G37jW-WQ7lYvLLP3FT5LDvqJ-lUWihEeGVAkiY1q4AyUo6sbbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Cbs7BEn07RVI-d4nYGT4cZ5r49kGurJpi3LBZQMD5aSUhPBK6e2AHrxDponZukK_A4lTU_DAz8ApR-QWHfABF4H9xPOEFQs5D8HsfkCrja_DdKRIf6luLo9oBYLp1A3a74fW0LifS93FNnfV8zvU2uVSN7foZWaTzdVvv1j0BoUU8twntQJRzHNryTJKi3gqETX3LO_0_1csZD1d8hYzbwbGOovZEtryqv9XBzWme61qgQsrhqBd2R7b2A4q5g26AjR4ypM9X221Lg_zIHMqSBmCsO70USVmnSCiEY6aKtw9Wu-9wBHJNzGUqpWLh_tb-11LrbLHzNOY5r18Qn75-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Cbs7BEn07RVI-d4nYGT4cZ5r49kGurJpi3LBZQMD5aSUhPBK6e2AHrxDponZukK_A4lTU_DAz8ApR-QWHfABF4H9xPOEFQs5D8HsfkCrja_DdKRIf6luLo9oBYLp1A3a74fW0LifS93FNnfV8zvU2uVSN7foZWaTzdVvv1j0BoUU8twntQJRzHNryTJKi3gqETX3LO_0_1csZD1d8hYzbwbGOovZEtryqv9XBzWme61qgQsrhqBd2R7b2A4q5g26AjR4ypM9X221Lg_zIHMqSBmCsO70USVmnSCiEY6aKtw9Wu-9wBHJNzGUqpWLh_tb-11LrbLHzNOY5r18Qn75-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E800r7JM_090JMuJKBkndpWId--WF5_gU2nDDi9-SkQbnBbn0AQYPIj3nGZ0AU_2pHK0mfNLUJsa6K_3rmqyZPhxM_lOhQfMAAlt9c5BBpcxFO3jaT4KQhq4ZrzGaem-9HaamVHlYn_QBH-w4SIk6iVBTtp4-KGtiL4IQoqCPrRMW3wvxc8z7b5bv8UD-xNp3JS-h0AcyRzJ8zfborUgjQDHK3yDhWG82JJwuzi1nXLCPfi_IDQJci4cbu5f5L_1_KSNdDmjslSFhHuKlToBOmrRX5lRJIlJYn3Gk5d3MEPifVGTmW2sXL_AY3zwvDnE9N8-r4Cbb1zdNCo2ZezFJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTM3ey5spKGWLh0pppfgV6Z4JIdKXZVgmWH_dGuBfKU9-va0BMTaQL147gDFSjU-JmrnvdeaL-U2w1TPVpYM5IsJIxMcEbRO3WDa5NpYm1Oxc00x5X0XnaC3143GMNNqOoaVBLEf2FUJ0VXcp4I8Ggj1Ty2JpkfpBifGSGLNGODEcVTePySZDzk3xKDKATV5TRMoNtMC32LpMxJ9JEQn8JOH-rMJQJQ67eIHezSctWeRa9Cl-g5gHBUosUZ1ubAB9Tv_F63mgXDMZhViO0DxJR5nA1_R0bIOdhE5udsb42_E7NYfjn50xXNs2h0N6NfbJ0FIHGj0xuFYolPr1Y1xFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmeVm5QAMpHYokg1YoXdqnr6uF-Uj0I3_hyIeum1CEfj59d9CfiBMTk5FKmF1vz7qLumyjbbctsrFxViIFuzL5_sXsngPFgy4stk7Nv-lCDhEs7z4BdShOlDPs0BU5kPn8kVWtXmfHSAQbGY_lpTy5dcxCq7Oq1GNjlktjURjvvVGvYs0F7V9A8TSLDr0lStVjvFH20I9LjqTxnY2Hr9rzDmkQEliR6PHUv6VTC_kYUos9N_JZPv8KF6XDH-Dfrdhi64ON1F1KVgq2iRzuTpcNJ-L24t7J0XKoa1CmIDwd6Sw2Sk9qbnGV4qKqfnBXguwKq6LlCHsSSz1HVtsyLEvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=YXwJOWQNFB4_vwKBB9pajddd1vHOxuUD1g2DdwOxKi0lHd8guGReFCb4mA5Z85VLygwW1oZwOwP2fNahMwnegNFrnStireD3jRifuwZd3Ww--3z6_tWJLSOR0oEBHPSQPD5lvk-Kwj2hoQ9mZwbvWEwGUjCKGPFv9hPRjbvQxQGQsvLLbmB72rJMJPE02k9d_Rb66BV9T7Rk-nQrNWouQBQ1F46yZx0eKY-dkvS3Y-WNZJYA6TJORilA9DSGUpdDTyquz9DefdjXwWMyGo_clcalQFaWzALT7X8nd8DrT669KAXKFw04C2MInKHBxb16abEQkKzjv9pmzd3AXhf79A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=YXwJOWQNFB4_vwKBB9pajddd1vHOxuUD1g2DdwOxKi0lHd8guGReFCb4mA5Z85VLygwW1oZwOwP2fNahMwnegNFrnStireD3jRifuwZd3Ww--3z6_tWJLSOR0oEBHPSQPD5lvk-Kwj2hoQ9mZwbvWEwGUjCKGPFv9hPRjbvQxQGQsvLLbmB72rJMJPE02k9d_Rb66BV9T7Rk-nQrNWouQBQ1F46yZx0eKY-dkvS3Y-WNZJYA6TJORilA9DSGUpdDTyquz9DefdjXwWMyGo_clcalQFaWzALT7X8nd8DrT669KAXKFw04C2MInKHBxb16abEQkKzjv9pmzd3AXhf79A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همان اتفاقی که در ونزوئلا رخ داد، در ایران هم در حال وقوع است.
مردم فقط آن را نمی‌بینند.
نمی‌توانی به آن‌ها رشوه بدهی؛ باید شکستشان بدهی. و ما داریم حسابی آن‌ها را درهم می‌کوبیم.
مذاکرات دوستانه‌ای در جریان است. ایران می‌گوید: «خواهش می‌کنم، خواهش می‌کنم، محاصره‌ای در کار نباشد.»
سوخت برای مدتی پایین آمد. بعد، آن‌ها درست رفتار نکردند و من مجبور شدم برگردم. حالا دوباره دارند درست رفتار می‌کنند.
هرگاه کسی جلو آمد و پرسید: «چرا داریم این کار را می‌کنیم؟» فقط بگویید: «چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست یابد.» خیلی ساده است. همین و بس؛ دیگر نیازی نیست چیزی بگویید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcH-cQLBclmhRFuRRh8wo7Avx-jM2E7pDpR6_Y7cCParfapPn1dZS8r25crQSzaULkAU88o0XxSfCwCRsNBsQtXswu2oU9gewAqXkV8_HBFcSdlThTTi9JJlAqPcb94yPV_nKgTRE2ACX6WQ8qTnG2Qci10cqX6uLGx58r45a0IUTMG19A8J2plRD2spVliCOO3Q_Aj40D8mZTUyYBNvRzZZ_sIa3PYvQlJIsMzvCjY8i9FBGLzHQI2lxNzls_QsR6akz1NWwDwIIadARGQq2FrSnwVn1ZaLsoL0oQ0SslapugrsOjjNqFLbVaYmQdIYkhi4f9WXFbFVoiUp8SbMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=R6TWY0TbqyTosarSKTADnRAD-fU4Jvw2F17sng0tM2wSLnjIVd0EZmgHszcP7xnRbPZFQqYksgosbg1R1U50ZfShKIp3W7msko_mqygr4dI2hNXKZv1Eqx7GAvpPbxTip8OAmN9hnQ5OtFMT6RM9EbO3jC1vNYwI910YyCyd18LwmoY1h73eyoFGnF__IR7WYX3HBt18XOyPmEaSN5wHvZnlaNET7sAMmfFn0rJXuTCpAuFtZJoPW4Wb_Ceg1dSigm6ugpAW_xX1v1LoWg00ps1wOrnkx6w1HAM-ABqCDbKRNh0zLW0920dEBglpOJPxC79nFZmWDzz8MK4xFhQsvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=R6TWY0TbqyTosarSKTADnRAD-fU4Jvw2F17sng0tM2wSLnjIVd0EZmgHszcP7xnRbPZFQqYksgosbg1R1U50ZfShKIp3W7msko_mqygr4dI2hNXKZv1Eqx7GAvpPbxTip8OAmN9hnQ5OtFMT6RM9EbO3jC1vNYwI910YyCyd18LwmoY1h73eyoFGnF__IR7WYX3HBt18XOyPmEaSN5wHvZnlaNET7sAMmfFn0rJXuTCpAuFtZJoPW4Wb_Ceg1dSigm6ugpAW_xX1v1LoWg00ps1wOrnkx6w1HAM-ABqCDbKRNh0zLW0920dEBglpOJPxC79nFZmWDzz8MK4xFhQsvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP1xaEUp7LU91mldZWtZgBOXmvH0hC-4Ybm0Ch0BhT_rjbU8hlRAEKaeUEpT9aBrMRuOkFNUPwAKsEa7t6WLEBCmSrZEigEsi-Fw2bYsJ2OFN2JH1DSkO1iRExDk9Ayy9X01085EKZ5a1IUq4vCsBeBk2VCSJG4iZ9OkN1SyURf9v00ZmUCO60PyM3p_nobZTcN3lENyvrXj61m6m9obrMopuJmvnXL6_FBU-t4T1vLncXKlnzu37MftGbGLbpNr2CapImZ9c_rOZuuXg_DacjYD72_e2KYIB1Q6UTA0hNeEkUaFKyuFnETSOPMahCYTkTt9UPN9foJObqdDst0z2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=wBJPmy2G2UZy7J7_lTsmaD-ivtT3Evq9AbTV3n3YGEs3bWNBePA8m1xhD_0YeQVnJa6BqVmpi9ZSajZRyHTd8_wXuJa1twRBaJ_URPp8NhaoBcFDNcCvEOTKUHSSLdx99OO0OUoZkgHRn9BEBCmIkb2odvHUiH87tp78NfnCzlnu-TLcmbWrvYBp_lywdBbwVC-RQke5Qj6JjgoCBFpZVtuaa8OvcZGER5g8R5sWwEnJAD1-lx5DtPI7wvGU2gurf8L8iGsc3THb4lG2RYkGRW00FBPbW9kUuCuG4nEgDRuj9NYH36613POVbBjKboEdkYen7O3UU9YT8nk9Nr1BXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=wBJPmy2G2UZy7J7_lTsmaD-ivtT3Evq9AbTV3n3YGEs3bWNBePA8m1xhD_0YeQVnJa6BqVmpi9ZSajZRyHTd8_wXuJa1twRBaJ_URPp8NhaoBcFDNcCvEOTKUHSSLdx99OO0OUoZkgHRn9BEBCmIkb2odvHUiH87tp78NfnCzlnu-TLcmbWrvYBp_lywdBbwVC-RQke5Qj6JjgoCBFpZVtuaa8OvcZGER5g8R5sWwEnJAD1-lx5DtPI7wvGU2gurf8L8iGsc3THb4lG2RYkGRW00FBPbW9kUuCuG4nEgDRuj9NYH36613POVbBjKboEdkYen7O3UU9YT8nk9Nr1BXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_VEC7_GFrHdgjVJiSuTj7tPJzv6R61XMEzXM5CdVWTcHO4WK8sU4qW6t8eUdW9qfSvdVU8XESvVCTAU47P40bJlxSjlLf5U71vdbOwKOt0yfZvdJVbfVvcrSnPQkZ4ZMaHBTxtox8mbdHPn-oFD21XcsZde7MhmhpRYJICdd2aO_GENKfVDj9FTEff2rlvWUDAp48q9rGPUFMFX5qSGEpAyR4W1p1BvdXTBpAZVIsYKnHmPnFGozkqO485bTn6GbEohUIL7VdOAEuHg6lvNCLRMwyCCadCf9LHprgSAPpiobonKp49U9aJ_VeaRiiFtAq7yAtfBADUfCTfJ71DOqrtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_VEC7_GFrHdgjVJiSuTj7tPJzv6R61XMEzXM5CdVWTcHO4WK8sU4qW6t8eUdW9qfSvdVU8XESvVCTAU47P40bJlxSjlLf5U71vdbOwKOt0yfZvdJVbfVvcrSnPQkZ4ZMaHBTxtox8mbdHPn-oFD21XcsZde7MhmhpRYJICdd2aO_GENKfVDj9FTEff2rlvWUDAp48q9rGPUFMFX5qSGEpAyR4W1p1BvdXTBpAZVIsYKnHmPnFGozkqO485bTn6GbEohUIL7VdOAEuHg6lvNCLRMwyCCadCf9LHprgSAPpiobonKp49U9aJ_VeaRiiFtAq7yAtfBADUfCTfJ71DOqrtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=Kus-qUG2cW-8Fa5roP5JcwXYWlkUYu52AZXr_g2hhG1A-W77wKSwlSuMLkQ7bRxKaHiRX5romNnnAbwX7Tykff3eB2y_CDvPmId2WN5kE7pFNcMQ2yJJjl23NzpggLU7QU2fu-EpV8uZfnv7tFbigQG9VHMhPiUoPiy-Fkr27muIBld9jXoaymHX2iJ8negx5haSeACK-Gz-i-h2qXVVRe2nKLSuGf_pLN8GQihKXvvwLcZTFr7JhTgiBBvTNqywfbZd_aBxJpxIKQS7fbezN1KUc1zh8QubqfSJ83sLcuxeeNaChtAtmrTNQNl1_pYPTiv2KpTboJW2xwXXabqZaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=Kus-qUG2cW-8Fa5roP5JcwXYWlkUYu52AZXr_g2hhG1A-W77wKSwlSuMLkQ7bRxKaHiRX5romNnnAbwX7Tykff3eB2y_CDvPmId2WN5kE7pFNcMQ2yJJjl23NzpggLU7QU2fu-EpV8uZfnv7tFbigQG9VHMhPiUoPiy-Fkr27muIBld9jXoaymHX2iJ8negx5haSeACK-Gz-i-h2qXVVRe2nKLSuGf_pLN8GQihKXvvwLcZTFr7JhTgiBBvTNqywfbZd_aBxJpxIKQS7fbezN1KUc1zh8QubqfSJ83sLcuxeeNaChtAtmrTNQNl1_pYPTiv2KpTboJW2xwXXabqZaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=eTNp_bRoBG7hBpC5ZOi5GOvTNCGw7XWH-tmMCxS1Bq88A_JpaJNy3qd2Nyr5Y4R4w9oqTHcu_HTe6xgrO22wR2MWWcT7X7lE3GAI0AvFTpZkp1IDpNmFwDiHoYZ5TZwMCzqGt5-giwS69Jsf7pb6-UU-CCooJroOWc52BYYVIUdALPmlVGVmC-uIcmoMFXZxQOcIgHvRPjJet0VM-DBrDXeAABLzFfLXvrjLnnsLlGN695NCVmVHCttUddL8Y-o12yk_WYYT0tmJAPTp7m7Gxbo9RSrKUxxcVXa4gNMslJAmoFUKMWQgCs04pNCQTXmAbslStILjGy9fVI6pqP8wzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=eTNp_bRoBG7hBpC5ZOi5GOvTNCGw7XWH-tmMCxS1Bq88A_JpaJNy3qd2Nyr5Y4R4w9oqTHcu_HTe6xgrO22wR2MWWcT7X7lE3GAI0AvFTpZkp1IDpNmFwDiHoYZ5TZwMCzqGt5-giwS69Jsf7pb6-UU-CCooJroOWc52BYYVIUdALPmlVGVmC-uIcmoMFXZxQOcIgHvRPjJet0VM-DBrDXeAABLzFfLXvrjLnnsLlGN695NCVmVHCttUddL8Y-o12yk_WYYT0tmJAPTp7m7Gxbo9RSrKUxxcVXa4gNMslJAmoFUKMWQgCs04pNCQTXmAbslStILjGy9fVI6pqP8wzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG9nla7wwPp0c6uRY2pPD0Sa-n2ynwi2P_jraACBVd56RTPdG8MaJ1i-RUrBXNHCt4O7X-HFibthFVTBJ2v1cqzbkS3Xv8VqKaqmgnIxpYGx_LFdKvTGYUmX42y8BO_1A8hCQ7ZDBnZcyGqUsTq3TFUdncPwQJejnQkFQ8LWzMlNmHscdGCmNKlh1j6z3r7PRaMlQbRaYWpYmKUVidexBZAZPUV8eJYDIGIqgh3NwOuuuIUPbOi0HV1D7-oqY8MVDoRY30mJ3hVEalRz_-EbjEBl3L2pIpSnkRPdCcyTFOQUjkEIDCRxTHzjfOfkK4lCom_w5Q02eKGh0R8qqOU1DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=JRkQ3Dd_ouff2C8h-4ZCHKnNt6Ciq9Pj_N5rCzgv577LY8hd8s44KnAMIdXXNqqvpOqDixC9nknn82V3Mv1qLkkiqcNwOaWZzW88mNBrqXrLKq_gwHU00y7GZLObzh1cuOs5RusMNrzKj4_1x3RApBJcNocIsOoYdTwL9EQXhmJiAJ17FLbF_5aue75bLFTl9RTnryJ6Q1M2AhhzBL6NRrnLGEgaQR_128Ug_wS5RENbc64UtUYCXgVVmwlbKHU_3u4pCvonvUr3qddgW1EpjaG5sqLKe_QKT-loxpwmm8T2myzyg0DKlJSCbgqdwAxf1OIq40RRpPtefLkz6ripAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=JRkQ3Dd_ouff2C8h-4ZCHKnNt6Ciq9Pj_N5rCzgv577LY8hd8s44KnAMIdXXNqqvpOqDixC9nknn82V3Mv1qLkkiqcNwOaWZzW88mNBrqXrLKq_gwHU00y7GZLObzh1cuOs5RusMNrzKj4_1x3RApBJcNocIsOoYdTwL9EQXhmJiAJ17FLbF_5aue75bLFTl9RTnryJ6Q1M2AhhzBL6NRrnLGEgaQR_128Ug_wS5RENbc64UtUYCXgVVmwlbKHU_3u4pCvonvUr3qddgW1EpjaG5sqLKe_QKT-loxpwmm8T2myzyg0DKlJSCbgqdwAxf1OIq40RRpPtefLkz6ripAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=oO_KsnQERsqeOUSXq8H4srkcOrqW1apdkmn--BndsMWzZzT0NfeiPZyY1EFCWzKLFBWQ3ykbm7j0QeR6ZUYk5k6GutJY7VXPlWW5jygvbtBw0CtF9k_ixFxpKE9ks96wKJmTYiP88dT2LW0OD1y-NPk-L6hDP6-MpI5DPSdqZtoeTSUGxy7u2UyIl44fE9twzAdM46Fjv-oF36HzkdHmTNf1o2EUe-Le_K2YuHeKGKktkT9REmdKxK438UgMFGIyGf8UezvyWN235qiQZymj0aHJ1qTp14ZaAVwh9Dy5hl1jPECaJWMnxREHONc4dyqcNsKfsCb7GzHGHQzDIqMo-xszqzG4Ntca0MP-umYQYdfATeaqUVjTzBq4pfMyaT80-AX9tjHDhZT5PmCAOKEQ-VSwvHsI6I207QphSCc6i06vpucSVN_3Iz-uxmIyUeACvf928aqowVSo6B10WxtW9NZ34zabJwn6Cq97KDSTbCIzW-8rX1JCat3q6qOO2ShuAdEmeHv4DdVCXGMalIsj3impKLWsOkWZGMVwgmBWZljQ2f24Lpvy3u-IFxcE0Xq1nUngQd8BJ6wAtSKzUOHIo_GD2C8A3aEmaMoerLgcQP-OM0cPHyTWbODaOQxelwjU8T4OqB7KxCYXrDg2olhQIMQHbIFW78H8SjVvaMapNWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=oO_KsnQERsqeOUSXq8H4srkcOrqW1apdkmn--BndsMWzZzT0NfeiPZyY1EFCWzKLFBWQ3ykbm7j0QeR6ZUYk5k6GutJY7VXPlWW5jygvbtBw0CtF9k_ixFxpKE9ks96wKJmTYiP88dT2LW0OD1y-NPk-L6hDP6-MpI5DPSdqZtoeTSUGxy7u2UyIl44fE9twzAdM46Fjv-oF36HzkdHmTNf1o2EUe-Le_K2YuHeKGKktkT9REmdKxK438UgMFGIyGf8UezvyWN235qiQZymj0aHJ1qTp14ZaAVwh9Dy5hl1jPECaJWMnxREHONc4dyqcNsKfsCb7GzHGHQzDIqMo-xszqzG4Ntca0MP-umYQYdfATeaqUVjTzBq4pfMyaT80-AX9tjHDhZT5PmCAOKEQ-VSwvHsI6I207QphSCc6i06vpucSVN_3Iz-uxmIyUeACvf928aqowVSo6B10WxtW9NZ34zabJwn6Cq97KDSTbCIzW-8rX1JCat3q6qOO2ShuAdEmeHv4DdVCXGMalIsj3impKLWsOkWZGMVwgmBWZljQ2f24Lpvy3u-IFxcE0Xq1nUngQd8BJ6wAtSKzUOHIo_GD2C8A3aEmaMoerLgcQP-OM0cPHyTWbODaOQxelwjU8T4OqB7KxCYXrDg2olhQIMQHbIFW78H8SjVvaMapNWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=t4TnF4lvHZMWafHRylduNZvFvQlpXUZIbblMkmYqJYZpLGiAnWo6tVIJlYTW_s08_QhNZXEFkfEHVGL4F364jVRQkBGFQsKWRHB66n-pWT0lHoBOxHh6O-39L8KatCWuhSAdeGj7JbqpCqtREs7hBATwakziv5ORJVL5ZBnBCT1NMkGSzmxIP7yKIdzxrV0SaEpVJz3YRIftWnXSyUrRoe1awSlr8PnmmsXmdCZcvoM9W7hHlbGGMNxw2GRvkhf7cwAA_ef4fcDZXrPYBzuIYZFeVBOaonG12bWuFUgHg1mUVqK8JYNk1qf48xjp2rK0AQNns1Tsdqn352joIEpXyDXcNhFL2H1t9Wm1bza_Fn_GtOJSuJgPBwPWWiQ01i1fYpmIMdel_QYPTKIofKhIb80v5d8SwXcrLeeDeqr7i034dW4q7AqFu-559mO27TNvUCgMAgnO6rT6_hZPA9dIcIqR6XxYDwQLbSOi0cUuMDkXs0pfxdkSHfg8tjTOyX3_yuHvD2xx53oJ16uk9vpJH_22TeTO8jZLqSKUl_UriS0twxNW66lNJYy0__PZGjoxXbSPczeXnNcGp1r51vIlmpm9mByQPx7ZEhOryAlUHkLc0XibQOtyMUfrskEu5EgRaJaRgxYOVET3jgYitk2sdeJOISLzXgcIUjNp94Q4UgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=t4TnF4lvHZMWafHRylduNZvFvQlpXUZIbblMkmYqJYZpLGiAnWo6tVIJlYTW_s08_QhNZXEFkfEHVGL4F364jVRQkBGFQsKWRHB66n-pWT0lHoBOxHh6O-39L8KatCWuhSAdeGj7JbqpCqtREs7hBATwakziv5ORJVL5ZBnBCT1NMkGSzmxIP7yKIdzxrV0SaEpVJz3YRIftWnXSyUrRoe1awSlr8PnmmsXmdCZcvoM9W7hHlbGGMNxw2GRvkhf7cwAA_ef4fcDZXrPYBzuIYZFeVBOaonG12bWuFUgHg1mUVqK8JYNk1qf48xjp2rK0AQNns1Tsdqn352joIEpXyDXcNhFL2H1t9Wm1bza_Fn_GtOJSuJgPBwPWWiQ01i1fYpmIMdel_QYPTKIofKhIb80v5d8SwXcrLeeDeqr7i034dW4q7AqFu-559mO27TNvUCgMAgnO6rT6_hZPA9dIcIqR6XxYDwQLbSOi0cUuMDkXs0pfxdkSHfg8tjTOyX3_yuHvD2xx53oJ16uk9vpJH_22TeTO8jZLqSKUl_UriS0twxNW66lNJYy0__PZGjoxXbSPczeXnNcGp1r51vIlmpm9mByQPx7ZEhOryAlUHkLc0XibQOtyMUfrskEu5EgRaJaRgxYOVET3jgYitk2sdeJOISLzXgcIUjNp94Q4UgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKbeOjBa4PiirNFgmCtX2OyvtWHrPbwHttXEWW03NjCeCEuOYHUJaruJnE7u7SfaCZsucPatldVuQjxGrnfZQKBddim6onkAIAiUOjjC8bOs9ahfZHwWQ5rBbVrnQYOEJmBOj2lNjzCUly5DIRywudcq6ZVIoRzan9mRDrWBq79cpzZ9PTPouq05yCh7P5P_LqmutgOifpO5cFptIQfN9wyaFWNSC0xjSbi8oVZDGtmPIpGmu-DKuNCspRi9DQ4kypaPkkgPmp9JxGV9jJtNX34FeODpKPK3pP8mlQNIeRvJ0nMiLPpR1m6mBzef8eMCs6QYZhcjswvIDafsajho9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBggh1U-HRe37i3zi6xTKgSDjymOX3rCFQI9Tiqr35KM82zrFl3OfE0nLwKEGHoliKMcgXmYJmcYU5nvFfah0wCWb44-RJatVeqvKiFZYmYCnNnx988dGjUA3TWf-RVhsgTz2LF7o_6P--mj9d-C3J2u6FrN8mYBIE1AOAEAb47S76qsPSFjbjP7ODbLb3_O3xpm8O7DFoOk-c0JUdoou60_JO5VUv6r9pA93es4Vc8c7vilFj-azcwDfIFjBYR0HdE-fsP8p7EN3HD8ccHOcow7vbMgTtAMzjMRk-b7pjlyEndWxyEz-bbAmA_QGSeMsktwEwtMFtNVWq2AiTWtQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqP8_d699DZEhLb-vYzhxYwbUtQp7_V-W6sXy7XqwW0fZXCr9JfopcZcf0t-leMF8GzlsMrnGHFMSPjqseIIF7slbHRBtAtL0CuhHlTxzVRFc6ZGM_q2QzUFsaG8zpDdM78u-x9Sa0oqdTN8O0YwUNJ3aNR2pkzzb91eJaZ-B_YQ4VDQuw1mubxP0fnPbB36_uqB1lv3FmrErCOgBcLPJlW6-2u4sqg3GJVLFHxkDmVbArUgWXFFpFHpqi_4dS01-xSQNdsbU8y8RAcSV0R716erzshRWkEfijLJRkikbQoA-4_rUkJI4--HUgCXHYUgzVMjGZpySiaozwZRF-OHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=PkKwWE9zY6g8T2EeZpq2SSPH6nQcZFDPmYlEzAA7JaWwmUA71dHUy60-xTZQaXxcvX9KpJAg795Tlfo6bxdF-oVHMpM1OfgVT2C9TXhEbe09bWpu3MPh44ZwTiE8b4QGxn5iS2cD_57yHRmHyCoQ3qzGi88nOKPdNrZo2yJIvUXgt0YKGjauL7zrlecWC1fCC7iJZ-4D9ZO3dXhecHrJB51wr6xkgJReUjB4F8vtYg8EgHkQc8y3RN_liw9ByHfARY0xW40QweTvbMWz0Id2zpTdEg0tQetP988gLHCNpF2NFG2CdfprNaoA-vhIdW2Hs7VdwwSaG0kd1GDAmpzBWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=PkKwWE9zY6g8T2EeZpq2SSPH6nQcZFDPmYlEzAA7JaWwmUA71dHUy60-xTZQaXxcvX9KpJAg795Tlfo6bxdF-oVHMpM1OfgVT2C9TXhEbe09bWpu3MPh44ZwTiE8b4QGxn5iS2cD_57yHRmHyCoQ3qzGi88nOKPdNrZo2yJIvUXgt0YKGjauL7zrlecWC1fCC7iJZ-4D9ZO3dXhecHrJB51wr6xkgJReUjB4F8vtYg8EgHkQc8y3RN_liw9ByHfARY0xW40QweTvbMWz0Id2zpTdEg0tQetP988gLHCNpF2NFG2CdfprNaoA-vhIdW2Hs7VdwwSaG0kd1GDAmpzBWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=THJVcJdQScB8xXeEuU97kUanVXEObOvCkjT3cdC2EOFVEKSssVvjdXhPWP5oIG10qdOfOb1FdqCer3DyUscKcTsu7RN35XnMdFt7yrG6MRLY9CzBrGDPA_4ZFFzlYtShmexYdbhJ_dqUDndLFS5h02tm4X7Drk5czyK0ZOo1QMMEdl03lQWjgKFt6YtD9I2-YA5yocNeZPLhW5C5RlifSafq2c1V1tOxQ_5e8VuUPYO0_PMWyDTArItrhgWJTj5Q5h_uKQgfmGgyreLhAIhnqkUeGMIu9Z1SVpCeNNJq4NxC9PyV5IJNOFDW9dWBaK2dJwPlqgX7YNxJKOXDy-Kn8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=THJVcJdQScB8xXeEuU97kUanVXEObOvCkjT3cdC2EOFVEKSssVvjdXhPWP5oIG10qdOfOb1FdqCer3DyUscKcTsu7RN35XnMdFt7yrG6MRLY9CzBrGDPA_4ZFFzlYtShmexYdbhJ_dqUDndLFS5h02tm4X7Drk5czyK0ZOo1QMMEdl03lQWjgKFt6YtD9I2-YA5yocNeZPLhW5C5RlifSafq2c1V1tOxQ_5e8VuUPYO0_PMWyDTArItrhgWJTj5Q5h_uKQgfmGgyreLhAIhnqkUeGMIu9Z1SVpCeNNJq4NxC9PyV5IJNOFDW9dWBaK2dJwPlqgX7YNxJKOXDy-Kn8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
