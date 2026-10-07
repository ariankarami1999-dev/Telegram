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
<img src="https://cdn4.telesco.pe/file/QvX0uhb0ClCPHSw-Xm2PJPLQNI0B3_pXXWi-7A76a7qjhRg82DsmhAOwB4E8UdYQi-JLbM7_sKBghWxKzVIqTHQDSCXItJ6N2OEFXv0UnTRGpRQ4_38Q3RF4QCzTALNrjBZRimvDTC7R-QQ0LRgakt0gyNJEyk1qQIDJn3zPv3ioj4WLH5if_BfIHfKJAexOJUoJVGwZrJPnyLoTHjAYQ6ynmohZVYBIPHCfzEQ0rssJ7b7NVMDG1fiSAhLnQ__ILUbT3WYz81drtm-Z0NbzbDDuCMFwVQtvfVA9tGlXa3TEhfook6t3NOM0D9oYDB12t0hl9Lt9bnN7POPUjMoU_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 500K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-31153">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPlWzZWKpB96_hbeFNbCI94C8G2Vq13CnwVERBlMKS72ioYCIgpLGmuYT-muhJNgk7HAMq9pcXeoZJD6iCQksYJswjYRUmtMTBSTVkmzw-QPvI6JhmjxedoUbBjA170FEX5OZzs2HEEIDKYP4u4IfDYTn_2pBX2NP_ISBtK2EFCGCOAxIyw9oF1CLJm2eFDN1N7hbHN07ZPraM26EX0vaZkTqv5FpWixCms7-PCJY85J1D1l-MZPNn1u18spvzABtFAF1N6zl9soc2l2_pPNYJknfMEu3tniStObHEcygMfKo0kv4LguRCkw0ezbT7rPIa6_3uDoEeizIxcG-mI4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ادعای‌رسانه‌ها
؛ علی دایی و همسرش دیروز برای‌حضورتوهمایش‌یه‌مجموعه خصوصی رفته بودن قم؛ امروز دادستان قم به خاطر حضور بدون حجاب همسر دایی دستور پلمب تالار رو صادر کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/31153" target="_blank">📅 20:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31152">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=gNeftPnxFtCtW3VsJnghVIZjoN04m9Mgz40DvAYG4YBc7WgYcStgJTlRmdjKnmFlsRgNxx503YwkkiB2aHGxRFw-vuO1Bt-tcFc43orH8tzlDTe61973pIYyPZpQguK3wmyp8DSfdSyESEFzS498YR2HlKtL6bMPoFUmKtFpdfBx7wCUEc29mTkzBi6jYEbQrt3r1_WTGJwuO_KkoTlm7PzdfZfqBSulHvVUV3stmUoPScXMf5hTA1lRzKPwAHs24SpFxCLPokkVfz9PusnWpSNs2N-VwgRrAO_-3ZF7aPnHZd7Wlrpba0HSNAprt87NYREi_NNsxctnr0HELcbP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=gNeftPnxFtCtW3VsJnghVIZjoN04m9Mgz40DvAYG4YBc7WgYcStgJTlRmdjKnmFlsRgNxx503YwkkiB2aHGxRFw-vuO1Bt-tcFc43orH8tzlDTe61973pIYyPZpQguK3wmyp8DSfdSyESEFzS498YR2HlKtL6bMPoFUmKtFpdfBx7wCUEc29mTkzBi6jYEbQrt3r1_WTGJwuO_KkoTlm7PzdfZfqBSulHvVUV3stmUoPScXMf5hTA1lRzKPwAHs24SpFxCLPokkVfz9PusnWpSNs2N-VwgRrAO_-3ZF7aPnHZd7Wlrpba0HSNAprt87NYREi_NNsxctnr0HELcbP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید شد؛ با اعلام حمید مطهری سرمربی فولاد؛ رامین رضاییان ستاره این‌تیم 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/31152" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31151">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBISdLGaBq1-UQTOVGvsJblreau02yRfA54MCsWVHMTmPh1JyoOixe0ZO6TV4gkAu7moGIx6ZbUM_K8ZhiXJxKXYpH8AFSVbow8pXIUUJJLOAu84eoFs8W791s5JI7Kr6tuKUlxjwCxE41jNi8DE_q8grzb8eIHndioNGFfddQ9KW9uB09Bd0HDuVr7QyxPAmFgvg8GRy9ZxKPthKYQbvNQQrV9ZJZgVvC5UvtV8tLpXgLocqoq0tbl5Bc1XCM3HdfZpNeukULCwPh1rmgKQKaTadks2qnsRlfgxPt9OTJt-1oJZjsJ-QfrLpH9iuatRS3havYAIl8oIOEEEBXCHDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پدرو ستاره اسپانیایی سابق بارسلونا، چلسی، آ اس رم و لاتزیو در سن 39 سالگی از دنیای فوتبال خداحافظی کرد. پدرو تنها بازیکن تاریخه که تموم جام‌های معتبر مستطیل سبز رو برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/31151" target="_blank">📅 19:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31150">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=e3Mh9ZoWbiUclu_QTpb1RIrLSijbQL0_71SC1ytrD2kAOtLB2cjrDIQePOJwimWcjG5r188yrSMM3Lgtduep_Fa8kTVqcjQaQevRF_LI8KPRdPXplfYTt_Uw3oV29cGAFaXzH1DhN7FFxLo9nzlYmuRczjnMdhn7gByWTZy3RXTYGJmdxInYVEqpPIVrk3QA4qRqkc71hE4Dh0XSDbZ0pWZfpP6h2-NjcOobvaHn2N-1mPRsUWH4N2XvisXIZ_nCpnAPueufSSLBe6Ef9zCWaS1IoGnNLbyoOigeUyubFZtbCr0C_q-yTSfC-RYU-nMu6Lq0GHvT41hVxvi0Zuqrvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=e3Mh9ZoWbiUclu_QTpb1RIrLSijbQL0_71SC1ytrD2kAOtLB2cjrDIQePOJwimWcjG5r188yrSMM3Lgtduep_Fa8kTVqcjQaQevRF_LI8KPRdPXplfYTt_Uw3oV29cGAFaXzH1DhN7FFxLo9nzlYmuRczjnMdhn7gByWTZy3RXTYGJmdxInYVEqpPIVrk3QA4qRqkc71hE4Dh0XSDbZ0pWZfpP6h2-NjcOobvaHn2N-1mPRsUWH4N2XvisXIZ_nCpnAPueufSSLBe6Ef9zCWaS1IoGnNLbyoOigeUyubFZtbCr0C_q-yTSfC-RYU-nMu6Lq0GHvT41hVxvi0Zuqrvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصبانیت شدید نادر قاضی پور از سوال مجری صدا و سیما که گفت محمد رضا زنوزی مالک باشگاه تراکتور ثروتش رو از راه راند بازی در آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/31150" target="_blank">📅 19:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31148">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ5VFYd03Fh1z9xYT0ND51vGq-mhxFqDsTclKrq5BQQMFjbnWG09wtbBIknMqQO2IutSDJfVUF8YyRkWY-Vjps2bsNlz6TKf3Q8QW9xxNtKENgPa3Rg5GUrhFJ-RaYWhKrvbg-pQk8G8Lk5p4hPkShyfNEASTwN8EDDU9TJu6DiS5x_gjr2dMOB5P3nu3plB0-hk2EEoYcO4rGyHCfeQdFQX3LKW9oZKfFWM-D2UtRQuISIk7-sLWUVn6P27rB1vnthRvM2TiF6YbW-46NQppqV8f4Uq1P8nF2ooU1rjWzmJN9FutD4vltMLYxOddQ49LdlLqVkVBzhIC-7XHHp7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رضاییان از بس گفت تو دوران حرفه‌‌ایم مصدوم نشده ام. این‌بار یجوری مصدوم‌شده که هم کشاله‌اش کش اومده هم از ناحیه خصوصی بدنش آسیب جدی دیده که ممکن تا اواسط آذر دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/31148" target="_blank">📅 19:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31147">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6e0CMlq-7Bk0XlfJdjdBoyGf5i3Lr93DZUB_UQa3eLTRiC_8WhBoMEvGo2dRT9ZpH3gCX8uF_lGiwWxAP_7KXddcXihzasbeJCPcdAC-A21x-4ub-zL0p-eJXGrJA_56xHelMCn_y_tM8H0jWCm6u7qFRVk6LhGIJjPmfck8v9J-7JhsucXv7gamboN_-vLOxDN1jMdI99Ap4s2J6Dl1eReE9791AOmdrNkyCFJqbaCDwx8S0qHAqnWtXdH4KUzO27wpVnYg1mj_bqoKJGQ5OOfosSh8W7bpZYrpj7vHZdGMekf2Asvvh-D0sfbVL9xgIZ_LQFH8kFfvnfQJR0OUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدِ 3 هفته‌کسالت‌اور و حوصله سربر فیفادی به پایان رسید و از فردا فوتبال باشگاهی شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/31147" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31146">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=s0L_lLL1QXvJ_C_Tv04njgoHEVgS1T6BfLA6rCtygXzx5SWQ7F545pD4ktEyT4kI5luWGZoGdn9DMTc-uVFoUzTWxPui9h6gSE8x4sH3luHmDAh3VR8EMWAWGc62N6nrNjJDHEsQAmOYCTY4VPsF4BWfKkOQXbMnwj3Rk5W6GAHFgE6cgKoithdp1q8J7_NJX16nuBnoWprx2jutKrpbr8COHOjruTZrj3ll-7FFt_Dp20fKKIQpKZNeKjQPrTeE2bnZrBJLwvXYy9zFCC6NE_6Uyw4zgUwaoSuUB584XLKHSPBEq6QYZt6Cd-xu-0p0eaxtASQxDpcUYV5pYdGD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=s0L_lLL1QXvJ_C_Tv04njgoHEVgS1T6BfLA6rCtygXzx5SWQ7F545pD4ktEyT4kI5luWGZoGdn9DMTc-uVFoUzTWxPui9h6gSE8x4sH3luHmDAh3VR8EMWAWGc62N6nrNjJDHEsQAmOYCTY4VPsF4BWfKkOQXbMnwj3Rk5W6GAHFgE6cgKoithdp1q8J7_NJX16nuBnoWprx2jutKrpbr8COHOjruTZrj3ll-7FFt_Dp20fKKIQpKZNeKjQPrTeE2bnZrBJLwvXYy9zFCC6NE_6Uyw4zgUwaoSuUB584XLKHSPBEq6QYZt6Cd-xu-0p0eaxtASQxDpcUYV5pYdGD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/31146" target="_blank">📅 18:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31145">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuTBJw_BYnAnCQ_0YXB0Jd-cgM02QIaNGfb_j65IvzgTxWke0neYlci-JjJQCbOVztalh7eWFk5SltWzyctwEuP6Vt7SUkPigmAJ8kU70uYnUIiDgwXMA7YwgBhHhPAfim_1G69EuHJvZLkscxaXiF9hv2jrxXJJ_whw-m2P4IONAor9uVxjCyTk2qYl9KL81Jp6FClvXoxmn4_ySbV9lFf61NV8Ekmg7oaBHn94RicnIt0FpgwM-K459yOFHywJBR2CkGllb6cXpN7OOASFlXv-whayPgMmgRD5IOqEXwRFK46Gjy6r5g3f0a_zdSDV0Ca8W2sqI0XmqYqd6pQRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇫🇷
نمره‌ فوق‌ العاده‌ و‌ خیره‌ کننده مایکل اولیسه ستاره 22ساله‌تیم‌ملی‌فرانسه و باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/31145" target="_blank">📅 18:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31144">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=Sgu-YFZbbNG8WqGYlFC_f5UsNk2eCiZN3vowf1HhXufX8aBaRrvhaGY4h9PlFxcFkw84LfkkLg4WGbkqQfwZEmznbxPJqfM2dNlPefKEhhwpvRi1dn_lKCEQRJrY7Vlvj0c6bYRhz22zqYZ1_-FTTbiEZgJ5fXTb_Hlpv-RyRU_FBxz41qMBP5r6fIKLMPTLIQi_uIVphN20TaIj7BGxyKzoGCZtK0Y0VW_eYthx9sGoJfem7jCY3DOdF-mNwziD7tPMN_Cb8ytTVJ8W-O9uVBP3LEp6EN_MxlVn76pmOrBSveu5nqCYQvCWtWz1iFg1xr3o372ouuiJ-m1sxGu27g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=Sgu-YFZbbNG8WqGYlFC_f5UsNk2eCiZN3vowf1HhXufX8aBaRrvhaGY4h9PlFxcFkw84LfkkLg4WGbkqQfwZEmznbxPJqfM2dNlPefKEhhwpvRi1dn_lKCEQRJrY7Vlvj0c6bYRhz22zqYZ1_-FTTbiEZgJ5fXTb_Hlpv-RyRU_FBxz41qMBP5r6fIKLMPTLIQi_uIVphN20TaIj7BGxyKzoGCZtK0Y0VW_eYthx9sGoJfem7jCY3DOdF-mNwziD7tPMN_Cb8ytTVJ8W-O9uVBP3LEp6EN_MxlVn76pmOrBSveu5nqCYQvCWtWz1iFg1xr3o372ouuiJ-m1sxGu27g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
استایل جدید مجری ممنوع التصویر صداوسیما در عروسی؛ ایشون سال 1401 بعد از اون اتفاقات تلخ پاییز از سازمان‌صداوسیما قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/31144" target="_blank">📅 17:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31143">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=oStreIUSmjq7Lxp7wiAD-aESc_rYCvg1-klkVYBQeJS_MsXVDI8UFXmGWo8X68GnOpcmA6bv26EsVUcpEQp1xde7ZdZugGX0ipoHQVAXKOix1diSg_A1jXx0hiJ_jP6HSCqZJYmM5Fx8dmFTDV7f9z4SXwzis_wFWt2OiHCQw_UCYESCdVEn5nZJ3-60w5ySBG9fRt44gpeNguds-brXWhfyBRTVJUMG3srQQ8toAImmSsOEva4vT6hp1C_YktKsnGyJNRWuSryDy8LaoUx_kydtic4jLh7u2pgrKcq7_n9OVkpcR1SA39kJYtmB0Dny26SM4jJFoxuRjiNFaex5Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=oStreIUSmjq7Lxp7wiAD-aESc_rYCvg1-klkVYBQeJS_MsXVDI8UFXmGWo8X68GnOpcmA6bv26EsVUcpEQp1xde7ZdZugGX0ipoHQVAXKOix1diSg_A1jXx0hiJ_jP6HSCqZJYmM5Fx8dmFTDV7f9z4SXwzis_wFWt2OiHCQw_UCYESCdVEn5nZJ3-60w5ySBG9fRt44gpeNguds-brXWhfyBRTVJUMG3srQQ8toAImmSsOEva4vT6hp1C_YktKsnGyJNRWuSryDy8LaoUx_kydtic4jLh7u2pgrKcq7_n9OVkpcR1SA39kJYtmB0Dny26SM4jJFoxuRjiNFaex5Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های جالب رسول مجیدی مجری شبکه ورزش درباره اسم یکی از پسرهای لیونل مسی که چیرو هست. چیرو به فارسی یعنی کوروش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/31143" target="_blank">📅 17:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31142">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdMh2pZ9d5Cy256DhUEN3WVexc7e0pdhLiIN8ErLR2nAGRRNKXv3BDphbzZhib3ZnMud_QLIwhcRZAGmaVEe7XA-WdrRhBfYAg8FNHei3B4ekwqF52Cbs2XUHhOoMdqQ6QbOdQUI-PZym4Iz-nmsoEeoOBrcJ8AbLGCxP1lde9z1jIVwcC2XCfWOVqpoNbYjkv_KzGUUFxiFSxnm-voLnR37_VvlNySKqI4dBtcFxmUFxyStuKLWjRiPt98_YcuQvg1gt7z7vdXnK6WRXVxpuMg2kRpgWKLhDoQK3s4O0NBMBI9gorWnbv6ka1HpmP-S1BhlLmaQGaulCXb7s665Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌عجیب‌دیفنساسنترال: کیلیان‌امباپه تصمیم خودش رو گرفت، اون آخر فصل از رئال جدا میشه و میره لیگ انگلیس؛ امباپه فصل بعد تو لیگ جزیره:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/31142" target="_blank">📅 16:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31141">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=FDmRtarpSfqiOfAUCscJhaIsimAe-sBePokzHGhDHO_l33VquEHayLXngcL-HCUOA7G8K3bGkRCNPz4XtTrtrr4mnOsfc22Y1sZq_knuA6oZnYWokTnYb_teY_IsWetwGVffbxJhq_AX9iAKGktiqKFyNhwoHYjeczyQ8rR6CPNuSyDi1-HlboqIuoC3YfVkOD45Q2KtRqZ8_THm9Pn1tYkALE6c5gDSnW1hxbHrKqyHC47IaFlOrkXBBjFuHQlc26K9XxLOzwJAkgNOWAYUVA3ZpMcNl6j0F5wkPhHZ_j-LQgmQ6wnxXIpUu1A51aSzJx1XmfCFYvzAClrcYEFzJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=FDmRtarpSfqiOfAUCscJhaIsimAe-sBePokzHGhDHO_l33VquEHayLXngcL-HCUOA7G8K3bGkRCNPz4XtTrtrr4mnOsfc22Y1sZq_knuA6oZnYWokTnYb_teY_IsWetwGVffbxJhq_AX9iAKGktiqKFyNhwoHYjeczyQ8rR6CPNuSyDi1-HlboqIuoC3YfVkOD45Q2KtRqZ8_THm9Pn1tYkALE6c5gDSnW1hxbHrKqyHC47IaFlOrkXBBjFuHQlc26K9XxLOzwJAkgNOWAYUVA3ZpMcNl6j0F5wkPhHZ_j-LQgmQ6wnxXIpUu1A51aSzJx1XmfCFYvzAClrcYEFzJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی شدید علی آقا دایی اسطوره مردم ایران از خدافظی لیونل مسی آرژانتینی از مسابقات ملی‌.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/31141" target="_blank">📅 16:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31140">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_UgXFnhO_n-v_nGSFZDekIDuC6pubj2SyzT8xZqb_5LoB2zdGiPUNn4jE4FpScJfscYnZYo5pHsVOXjl1uRDPDbT5XGv9Rog1b-GGn9APSHnwGhg-aQJH0_u-xBYXbFBaP18Mt-AckZ4ILMN8OJFvGMx8SslZHdQyuvKxmidd8frK1fHMOd8m-DDGfg1zB54cXjxo6SASD_JRH1jsq1ogBFYgH2xkM7NEuqCzAHcytLqgGNvoCUMK09bM4776heMpkeVX04r5adanMGBMd56BNwNk8-wlNoufm5MyevfY0G1LaxhYNeVU_VhpIvuexyUzMrMjSeMlJhrg3PCEJvtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه آرسنال دقایقی پیش با انتشار این ویدیو خبر از تمدید قرارداد میکل آرتتا تا سال 2030 داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/31140" target="_blank">📅 15:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31139">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY6o0NN_5LXrMcgx5KMvg0_8P54ZmiqbbAKF4kMjTOHY9fUB5rzXwZmpXGcfkSzBY-1bmM3MzOFZNwTvGbhfl0R3SksieZlwkNUuhzHwiTIbIj5r6eIsBcKMVVma9o0saUYALXPo8yCVYSeOpPD66I_L2Z944Ugueia8JUPWq4K4jjDxRt8bStFIgHNFjEvH6MbERuHVSQ6kmkPTHIRjoZMMcetX_wiyL4Golv1yOzepgHwRIm9ypt2cw5H6Rq81_jk5HxUAMVWIPZwRgUJSCmtqfHlxRqspv1Lc3FZZFZrRvyo9WKkFkExTaJlgoFVV6HB3BNwZfTNXOL1pL71BJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج10دیداراخیر استقلال و تراکتور در تمامی مسابقات: 4 برد استقلال، 2 تساوی، 4 برد تراکتور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/31139" target="_blank">📅 15:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31138">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=MBr4EUQbBlH_LGlXMxG8_Sa31waBnoKHcr_pndlVbE9HojPgxfrgDRi4UyHpLiW3-lWDKvtBM82bA7eUc2qOftqGoWqvKx1zOOhfd7mi8kzaC0t9ZV3YaqBoaaZRildyZ-hID0dwAu1tcVyqglZml8dETLUruE-5nFv9YWkfnu91IMkrlncG4Sm7FGLLZcFXG-ZUQIIwvx4jzv8tlkQcRuGXrf9OYPXEHy1HG_epZiwpoGdMKHiOSnJ0QxYCVsH9DFyGnCVsbB3m5EdPeg3n4Y6pQZU3NAv9D2OW7axBpTEVJaWz-tshSKhhzNxzFzCSBKfUYEfHHcj1Zy5-GFtedQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=MBr4EUQbBlH_LGlXMxG8_Sa31waBnoKHcr_pndlVbE9HojPgxfrgDRi4UyHpLiW3-lWDKvtBM82bA7eUc2qOftqGoWqvKx1zOOhfd7mi8kzaC0t9ZV3YaqBoaaZRildyZ-hID0dwAu1tcVyqglZml8dETLUruE-5nFv9YWkfnu91IMkrlncG4Sm7FGLLZcFXG-ZUQIIwvx4jzv8tlkQcRuGXrf9OYPXEHy1HG_epZiwpoGdMKHiOSnJ0QxYCVsH9DFyGnCVsbB3m5EdPeg3n4Y6pQZU3NAv9D2OW7axBpTEVJaWz-tshSKhhzNxzFzCSBKfUYEfHHcj1Zy5-GFtedQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
میکل آرتتا برای تمدید قراردادش تاسال 2030 با سران باشگاه آرسنال به‌توافق کامل رسید و بزودی با حضور در باشگاه قراردادش رو تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/31138" target="_blank">📅 14:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31137">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bk0_A1dIz8896DME9_MRnRPMtH850PtekveykQ43oxI3yCKdlyGAUEgbabgpxw8IVLbvb7qzl51Lj0XrzmnAJs4jc471RnnZXhb4GTFAP3ZN93PcADJJEitSRbD_3y23TVk9CbIq0ZaT_7FeHufuImG9fz0xPUDofdPhqGbPfLYKbneMnEvjJGhKqs8tzNYWfkbedTIAwNQ5Q3pJdxL79rSKPuD9XZHnh_cQYVOZUz6F398vgVcwWxJPLmtMAeUJsItOYSNfkxrfMfnCQ3MDysJZyjzB8Y8GDWZmpBZRBU4_uYtRtzi60XdLsOyYgCaEuGqC5Bx7gfFuLXRcQxcIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/31137" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31136">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoMjIfQFWhG_jypaF3fzl3olyVFkRniKVSWBSCJAvErrBaVD-bG8jEoyk8YerXLCRGce_ky4o-QEf8WvduiUA1JFbZZog1pRa34kxF7_JrNRA6WTudof35TD3EZwDDo7Wuw7g73oq9dS4fWF8CShFkU9BY7DeNTxAQpfScvA7eT3z9mP6g9Apa1hidryhEJ_9eBuyq1-YM-B4UZMVmLL2e5CjX02vSQXbP7Aiu1rOewf90njdcilYUUxxxNbcIC5WmvewmbzoDcHddl-X9fxNT0-9qoFgXmj2CbELIFGU1Fqxo0e3wh2F2AJN6FoFKAA-VNYp6Gq2ZDSNC6J3WIqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛ پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/31136" target="_blank">📅 14:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31135">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=ZZVcbJye7Tcz2TDk-ibqD_qEm65AGx74Ygdy91VLNoocaf3viceRSB5Pt_axec8IKY9868yk0QmDa1IRqVy_KCf2VyGUsoSBabOtn7HJl8rq9JNiJiK5t81PaN5hVOgyV-e3M8P7DMbzCADwvO5PoqWUTMm22kSfKss0muLkucRJv2iGxMQkFXbypGS6sg_9uHhFp4vBXRXUcWvZ605kX4NRQAMNVwU5sdz7SVpvcFRxS_WW3IKm-tR6i6aj4ZOVzOXUSap6UmHVHmazZvxE08gDKVZItevtiKVxLrzeI1YBXoAhwo9tKwpBXLrz8OEl1_f-HPR7o3EK-RDcyOOTOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=ZZVcbJye7Tcz2TDk-ibqD_qEm65AGx74Ygdy91VLNoocaf3viceRSB5Pt_axec8IKY9868yk0QmDa1IRqVy_KCf2VyGUsoSBabOtn7HJl8rq9JNiJiK5t81PaN5hVOgyV-e3M8P7DMbzCADwvO5PoqWUTMm22kSfKss0muLkucRJv2iGxMQkFXbypGS6sg_9uHhFp4vBXRXUcWvZ605kX4NRQAMNVwU5sdz7SVpvcFRxS_WW3IKm-tR6i6aj4ZOVzOXUSap6UmHVHmazZvxE08gDKVZItevtiKVxLrzeI1YBXoAhwo9tKwpBXLrz8OEl1_f-HPR7o3EK-RDcyOOTOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه‌ارزش‌بازیکنان دوتیم تراکتور
🆚
استقلال بمناسبت بازی حساس فرداشب دو تیم در لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/31135" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31134">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=AiaZte48_mk0XFU_L1HAz3gdyahxDxcuziqut6rH-YHZg6atB01s_hBcgzZxs8uXxCGQEu5HYXxZ3lwzzaqckpML9xUnmOyCpX_CJwiNC03gwiI5T8QkPRxMKYgl33TaWVILmz9WlUKOIPCbRfSLGq8ct55Pn9QvpF60GDgwgbGbAn5UgIt9hDRHYYH1qDome0Kd_FhmJyfhJiSHKnIriXaJVwbnQjj2DmP58rFoYB_9S7DaJ8QJgfDnYB_Nd5msPUnSIb1PsAp2gNVx6Y6oJ3fOz7KNunilSF5L4pZDjhgASd7pqEmRaTeWv4TYA-cxZEp-pUx5Ok2yIsViCC1jG1J8HZ_U0Pbl-HaK3zORoc6xRY0jCDLQI5A2gWH412v-MracB8Pi9mPRF9guDHytwzg8wltv4VrT5ZDRPlX5lIV_mZOdgGahNKOX55UU_8Ctja0eSMKCUF_ypkfhXTPK0UgsuwtMyJAg7v7bVkWtJ84bmjr3ccICJnt-fRy070-5x19qLWCU-IOae6vn3Hs00yZ86xVo5Xl4m4f4z0CwAV6Ot_FFmYNdXQiCrOFJc1SzgS42XnOr0cjBoG_a8E8jXfjKX9Be9Dm6BIz4i98RZRVX--gS-5UYgKv_ThBzc4KSqQnFMZlemysyoqVcpZFEOLm8B7h6T_vjl6vEaACJ6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=AiaZte48_mk0XFU_L1HAz3gdyahxDxcuziqut6rH-YHZg6atB01s_hBcgzZxs8uXxCGQEu5HYXxZ3lwzzaqckpML9xUnmOyCpX_CJwiNC03gwiI5T8QkPRxMKYgl33TaWVILmz9WlUKOIPCbRfSLGq8ct55Pn9QvpF60GDgwgbGbAn5UgIt9hDRHYYH1qDome0Kd_FhmJyfhJiSHKnIriXaJVwbnQjj2DmP58rFoYB_9S7DaJ8QJgfDnYB_Nd5msPUnSIb1PsAp2gNVx6Y6oJ3fOz7KNunilSF5L4pZDjhgASd7pqEmRaTeWv4TYA-cxZEp-pUx5Ok2yIsViCC1jG1J8HZ_U0Pbl-HaK3zORoc6xRY0jCDLQI5A2gWH412v-MracB8Pi9mPRF9guDHytwzg8wltv4VrT5ZDRPlX5lIV_mZOdgGahNKOX55UU_8Ctja0eSMKCUF_ypkfhXTPK0UgsuwtMyJAg7v7bVkWtJ84bmjr3ccICJnt-fRy070-5x19qLWCU-IOae6vn3Hs00yZ86xVo5Xl4m4f4z0CwAV6Ot_FFmYNdXQiCrOFJc1SzgS42XnOr0cjBoG_a8E8jXfjKX9Be9Dm6BIz4i98RZRVX--gS-5UYgKv_ThBzc4KSqQnFMZlemysyoqVcpZFEOLm8B7h6T_vjl6vEaACJ6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از روزیکه جواد خیابانی وسط گزارش مسابقات یورو 2022 ول کرد رفت. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/31134" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31133">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdhTzB_6mpQu6afZbl6gRn1U1bD_ADCsxdrqDSR_CvZy7K56D4m_YsB2i4Lx4Ch8W1z0oqwzx4Bw6V5z_iVHmydrqwuVe2x1-s9JBLXXuCn98ll3jqZAh8Q1NTjpIQ5mOjUlfm_K8uJR_QO8t_h3ssjHrHUpLxEkgNyLBbTskHPLHHGkpxRxtFGm5fC2mrAA3y9XkqS_GEGCHmwwU-ZPbUDb1__WtGwLvW7JgEdyz78McT4AnDJRDifxagV2NYgoCkTq7VCe5__71QuAlH_gv1PQyjchN56yH4fBPull4dbZzwQ07TPeRt3CYVYo8ZduHKU183_kLQjRpnpFpL9FKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌ن
ام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری مثل قهرمان‌ها
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع و بی‌دردسر
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته، همیشه پشتت هستیم_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!
🅰
r15
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/31133" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31132">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXRRVMn5v69f4xB7f6mh9u_xXIKl-OjYx-yy-mt2YZEg6SjoVi6rYMvjH2KezXr5MaSvoajKlx_Z0sPnARNeBvGTgXStP_49HELx4QMB4I1jl5Qb_RVnAGSHQlEcnTtC0bWfDJSOMk8sQAy_nxQN6hD1QeEbSOwg4hYixU6db3hjNm9LU3XYTURGVH_BYMDZpziubAMcSJe0W07OE_z3rqbTT276oTwoCt2LGraZFHBlFCw1WpFgAZg0yiN9HMQn-mWlFw6zq4flnUSDrtvslryA9alv6GjyPKzCJ7EhRNOygjteyRDQPg8As2t_m0j-ailWlVUKSGe7_F0BSVpOiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فرانچسکو توتی درباره‌ افسردگیش:
بعدِ اینکه فوتبال کنار گذاشتم و پدرم رو بدلیل کرونا از دست دادم، همسرم‌کنارم نبود. بااینکه بهش اعتماد داشتم همه به من‌میگفتند همسرت‌داره بهت خیانت میکنه.
‼️
من تلفنش روچک‌کردم تاببینم راست میگن یانه، کاری که قبلا هیچوقت انجام‌نداده بودم. بعد از چک کردن تلفنش ديگه نتونستم بخوابم وانمود کردم که هیچ مشکلی نیست، اما دیگه اون آدم قبلی نبودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/31132" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31131">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccUM4g8C7HAzSIvQuAAlNnhoJ4-xz4s7QQpN8PAZi9o-E9_A-RyknjHr8XpqMYzwyBxr_zCq6TAJ7JHlaUk--q4KrlIiBFeIfvYoDiQbZQ6CiuPZsUUjiQOgHizK4_z9cQJ_ovkHSlEvCLYJp2FJ0NSpUGw_3xob29D-rVRNYUqDzv8XVqf0xDsL0WctpjrpOomO4DHO1rVuZ8R5Zt_Mo0X1mRrGljbf9C9CxDsKemdsDN4AibBj1yw5FooiFEcJgyfsZf6hUuidGzRRIDkUCa03Q9AJAp85yRgWZE0Uvs6CMnPFM8HvL8QkicZsVNM5QIQi3OqsX5vGKL73EAeH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/31131" target="_blank">📅 13:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31129">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=v9hjvaPTJg1W28x25ZgwBV1avj4Cu6Zm6VEUscvDsNqnD7v3dKrzXaNlEcveFnEIyHsQOnuaE4HQzTztp0S0Pg8hsYkG96Ssx5DtisBh7cwpOZqoZvhRV1EiBFY0BpE7Nc96fXEmwnjEXJMHeOZ9-ddNrWG5D_4A3JE6QHVl-8mwvUi60kl5EC9lOEvTra3Cbd_rP-vMpWuvohj14o9-f-2SBPeHeYeDEWWP3vmFkxSTS49VHxFMES-1Enl8JUc_kkUbPfSBEe8UH9HVO6uTinKZYLS1Rp4XIqxOknO7T8tUJV5CQ221U0aGzTtdJ8SOf5ctACxssYXbP7J1b8I0zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=v9hjvaPTJg1W28x25ZgwBV1avj4Cu6Zm6VEUscvDsNqnD7v3dKrzXaNlEcveFnEIyHsQOnuaE4HQzTztp0S0Pg8hsYkG96Ssx5DtisBh7cwpOZqoZvhRV1EiBFY0BpE7Nc96fXEmwnjEXJMHeOZ9-ddNrWG5D_4A3JE6QHVl-8mwvUi60kl5EC9lOEvTra3Cbd_rP-vMpWuvohj14o9-f-2SBPeHeYeDEWWP3vmFkxSTS49VHxFMES-1Enl8JUc_kkUbPfSBEe8UH9HVO6uTinKZYLS1Rp4XIqxOknO7T8tUJV5CQ221U0aGzTtdJ8SOf5ctACxssYXbP7J1b8I0zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دو ویدیو از علیرضا بیرانوند دروازه‌بان تیم تراکتور در پادگان حین خدمت سربازی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/31129" target="_blank">📅 12:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31128">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf4oBqlDzTbxefKEvp1PcasCn-Xy5ZmwbZSCYWhXDVHxcac3375WySnBIgW3Jj5mGOiPcTAwfsv8ssUVtewYAd8PhTUPdy_oLoAhezidmgk1B13PLfvPmV8qLqUGL0-s4mSMOgjuNjCVW1rFHl69cm8cmbINKXzL4N3JlzxC3wV2FnH1EWoJlm6MC2tVvXuMb9eKXgJsnqsI5ZzTh5a1wbKwEzFZMla76xz_DQhvg3qRdRiMMLpMSnhcxaNQPmdYlKJgYHa4quLRcZ_qaZTLKKzjfuosWlzrJ8b2M77ceu6GJ8BDxlZQtAZmxevgTAkBu2NPAv5YVIt7jpz4HeaaEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ رامین رضاییان که‌دربازی با روسیه از ناحیه خصوصی دچار مصدومیت شدید شد حدود یک‌ماه دور از میادینه و احتمالا دیدارمهم مقابل تیم پرسپولیس درهفته دهم لیگ رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/31128" target="_blank">📅 12:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31127">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgOJmVgXa_woLxfHtP51Uu7BVvbCAzKAqD5tLnSpVwdOO4FNIxMO1UP-Wnnfj1ufVdElTz9XKA8OmeTotfc-oWDmNij3vqnYibAkCutz0sJ-xskLwtuQsxn6Hs_2iejbGAX85mT3FKjpxO5qy3eMXQ03HsOw3jcYWS76AwPFll9J4eHsKIOnWlhiCjfbRkGhTDJy7s8b9u_poeRwMwN7gYlh0GMyneRVHFWo6oUfFMj3ciRTri8qOQ9R0WiLEk-HueqmtV2XBgSSHi73UvPP6om8tPZq1zxiDWdkNPxVdaFgdHfoqqOdoAa0qCOgl5Cd8iP5lqKom4REMeIxlG2f0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛خبرنگارباشگاه النصر امارات: کادرفنی‌النصر از عملکرد مهدی قایدی رضایت نداره و تصمیم‌نهایی‌اش رابرای قراردادن‌ستاره 27 ساله‌ خود در لیست‌ فروش این تیم در پنجره ژانویه گرفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/31127" target="_blank">📅 11:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31125">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=AXPYohmAFAGTuab58Uh0vGpfYBe6oxOm0hGgje-y4vz3NPeS3lfLYBBE2ZtEc5E8fbfijK9UXDoXNe-IWLLAY38KfL1H7154YengyeZrrfOljbaG3qSgM1jzGa5uh59EdDuQ9UnhESLFQlmYkwToNX8Q4bKQ7ul9LTpa2r7zwFA9lTdn4iFpWmZ2R1ZmnGGkZeSqgtDD0sCk_e3dTLZNZ-WxkRhEt9LuDdJFLAfCDWYvIQCuoae6f4M72SH-li-xzJDdLhC0gsbHipEQ26VsSz2FdKMoQzzjGOFVvdaka2iP8aXEoQ2XXEwCh81X_pP1zxZB22_55TFUCmEki6UAYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=AXPYohmAFAGTuab58Uh0vGpfYBe6oxOm0hGgje-y4vz3NPeS3lfLYBBE2ZtEc5E8fbfijK9UXDoXNe-IWLLAY38KfL1H7154YengyeZrrfOljbaG3qSgM1jzGa5uh59EdDuQ9UnhESLFQlmYkwToNX8Q4bKQ7ul9LTpa2r7zwFA9lTdn4iFpWmZ2R1ZmnGGkZeSqgtDD0sCk_e3dTLZNZ-WxkRhEt9LuDdJFLAfCDWYvIQCuoae6f4M72SH-li-xzJDdLhC0gsbHipEQ26VsSz2FdKMoQzzjGOFVvdaka2iP8aXEoQ2XXEwCh81X_pP1zxZB22_55TFUCmEki6UAYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تشویق و خنده‌های آنتونلا همسر لئو مسی درشب‌خدافظی لیونل مسی با پیراهن آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31125" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31123">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owHfS88_Jj5k0yh_l6j8HzL4EHsfGPv7thZCnQuYJF6-x7CI5yZoxOGz4672h7ltssDqotgM1AZoWsfrkMEl4VASeI02bpbSubdc0an4mervmcMBDt6BYOsc4rBeSLfzKE4o85TbzSFXh8Oi4M0WTMd2Y4fChX0ILfz75Vihtu6w-d3l1sLAWti_QqnlIO8gglk3b5LRVrEyKjW3f6xEO9MOxbZVdjG3caSycZ9iUn6oO_1fxfBipC_AcKnUMCVGcj_LHMGmBbeP2A5RIBuC2rifhRQlIhQzGdW-5-wsXnhZF1WY6h5AZKnVEh0eZb3-CeH2Do1-tUntwbs-_zwDQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دو تیم ملی آرژانتین
🆚
پرتغال در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31123" target="_blank">📅 10:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31122">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-kjEgjAGpLhgs2vOZSxxJekqoeLeWmkhGuQB0-ZFo2yRiPhWX6a-3Zuld4CQTRHYuia3hUYUofCElvhoihqWp4nUrxYrXvMDJlhS_I2MYigt0fpCUsng7m4Hj0_uGS65CHlgzq9Hc3Z4cI0L--Cblk4NjeWwdExlTuV6BaEboh6tRSKco8Ug7AxxmLWI5iYViQL4uHEKuVTu6gXWLw0Y8LNlyyaWSoVRz0cSBsiaFJdrdn-BxyNT9majCRMmFQ5T0Byh5eLuKhE7K0MtRMgqk5BHxdxqf19YNWIXOS7Y7wrhoMpcuhgkMvVJAbUbUshdleqi2JYQd86KPnavqOxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام 126 گل‌ملی‌لیونل‌مسی به تفکیک هر کشور به مناسبت خدافظی همیشگی او از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/31122" target="_blank">📅 09:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31121">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmc9plMaryI3V4yw0hamRfzQog4CAaMQRorz88CrzyDQr6JApvIgrXUuB20R2mLYDFAWjPZEiDWkYF9KneG81AeZhkrCR5T-LZfCFfJdnd42dUfHCc8MMXYanpoJimSu2ma8q6PbovxXnFULbNDBDzI3lKabiQtOGbJQqhn79rlXZbSm7M9HCJ-3jgGQOS1EkN7TBoGbs3tBB__Qjj_9rpK2KVqXEutg4gJ556ua2Ipz_x3Mtf6DQwWO3gW0JbRxeQQVPZRpSAe1AUp12TbgqVnSH9HEsRjvurZLD8MsbGZC_dIwO716BmKqfVYNIymtb1_EKBW5469NZxQ5DRoOkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هایلایتی‌ازآخرین‌بازی لیونل مسی فوق ستاره تاریخ برای تیم‌ملی‌آرژانتین که بایک گل و دو پاس گل همراه شد. دقیقه 10 مسابقه متوقف شد هواداران لئو مسی روتشویق‌کردند مجریان شبکه ورزش فکر کردند لئو تعویض شده. ببینید خودتون عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/31121" target="_blank">📅 09:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31120">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📹
گل‌های‌دیدنی دو دیدارمهم و مهیج امشب رقابت های هفته چهارم لیگ ملت‌های اروپا 2026.27
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/31120" target="_blank">📅 09:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31119">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioWsJ15IfrdVYkAibWRob0ONDOX4XyfMk37NDEv4wNnLrBwsmuokvhAWNCKZ3TBes3nf5hrnfE7FJ506iQ6Onu2ZmkTalyc-8yS0feBoe0zhlfRWUdDHSHQmEUCAqzgT0z-737VDdQeJm9f0jcbA_HaJDPzfi7VnG7kFabU-qDQpFelzi_hasNaiM9G7xX7cVawRRvgSwfl-tmvppmzmOsKG5-NOphJqrX0bTeS30gTFLJlYUSU6zybqvYp5p-eIpYbZ1oef3oz6X1sXVrYd2fruffNayplImWFuwVV6s1lZpQKK7cWG4okyUefkIgWfIM0OpZcZkt4Gtfo07n0Xmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ شب خداحافظی لیونل مسی افسانه‌ای با لباس تیم آرژانتین و فوتبال ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31119" target="_blank">📅 01:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31118">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9IvyAUKgdwkMmA2Ac77u8KAAUN1ClCgq8Y_Fmgc_g3VCmJuGRAkuHVGIFJDlqY6-B3GxofqGNPt3o9MJ-TykZDE49r3lA2xXgajdnwSPY6NImah41SWNnJwicbE3PiHU8LeTsubQw09GYXUDuw0j8PscPV5sJK-8HkntBm-GihgyaNJ_fQMwiTm4MAfvwDLYwNxM5KbZfQr3akt8GA6ft066PckYBtSSg1cyHpUWramJ5vuEYf5YcrdQmefbHUjseUhcAqmXTOAblEDOgPt0cULKm1uAJE48kGX9MibdryFf2BJjU9QIGmsbcjNn5qZFhFyu3R-4uJMTIRznAvDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌‌دیروز؛
کامبک‌اسپانیا به کرواسی با دبل میکل مرینو و برد سه‌گله سه‌شیرها برابر چک
🟠
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31118" target="_blank">📅 01:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31117">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
هفته چهارم لیگ ملت‌های اروپا؛ پیروزی ارزش مند لاروخا مقابل یاران لوکامودریچ باطعم کامبک و پیروزی قاطعانه سه شیرها با درخشش هری کین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31117" target="_blank">📅 00:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31116">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTHMhpf70uMOtfj9WNqItY0uniTJWSt0VvyL2lCq-Cn3lK3_DSWYy3pTRlchS4e5XpfqYxoDld3B545U_TCjiMY0Y32MzMjR5op8L221JNIEpr6ASuZ37svXs4Qcl1oldnR_OKdU5MY9-oy8cqdUKPYgxB6GzpvM1sUtMwyZ-4-kVAl2t9QgyHuf1b56Di_qdvob5yj2NYrzyue1KCh7Zk9-313mnxOliXfrl6BxVhha8axHHTDKRYI4LMHvqKIML6_-4GPJtgM5iLicwotCJwDFBvWoNrma9IssPVhy_P4U4dBxaCs6u4-lZAqeM2v8KihE4TRLf74fv9RhoqaRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31116" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31115">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMZ6F-eFg5ZohXG5gekzo80jEb5EmTrmCuCKSKKiBTNnN0DkG9SMwwm89qzLZyaX4wMgIPILDssGSu3mqW3iS2pMsZXGTkYBIhW8w26uSllwwrjFg7xVR823cWqLHMXk3NNN_NTXRov7qTDWqH3UU4xTaaNdjw7HKM8Pt-vSub1IcrLZW9ja2mbf-C0iiR4YQtBv17alPHUwZ36jXLp5aOEgKrLpjQDVl_iEsxEPELRwNk9Q7-YJ4wTe23iEQo0NbHHlX16a8QUaH0OHBbJJ8KoHDWBW4U73vn_RTvbLMr2ABaVq9mbXE0yfMbkULLV6Ax0gg4TlyuVBaiVb0g7y0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31115" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31114">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4KSkbYttIaPMEz2j7KPFw0MKPlj4XqqCqAslYQ1ceDMlknl3wZ2KJb0-uDiSiz2QSaconjg4WwEWv-GRpRVMRtQZ8z8udLz0u5S-peuBQPPw870JLzCJ4LHKGCwrcWnhkcrYMVJK1licQnGfGbVBzluQvLp0AWWr4EIO0H8KpOAEDqwzBS-MDkblLR1TuxDXFAtrHMqoK3D6OMMuqSv4R9hInfkDg-g4yBfeesD59R3t8wTvrbu5v-VGXQuLMar9WfwEna6kj8e2Pc1XICPrEbFX2QAPDujU4O88t7jatE1AQY1VN1GrhdGOkBgYpUXRBDGbbrD0GJkcG3zMz8TKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته هشتم رقابت‌‌های لیگ برتر بعدِ تعطیلی چندهفته‌ای‌وحوصله سربر این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31114" target="_blank">📅 23:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31112">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fymoXSmy6GbEvNq2t35qrKZuYhCfY-0g1d3t-VOa25H0h6euWezs5C1J5ZIAZTrlZvMlu560rdC2o3eZHhu3F6_IUhwgI5EEJ2UHz0Ky_IE4d34Bj0w03AkFTVjDO3Ea-hD0BtzUZSg5vJXa7jPcgfgF-1JIwoqJYn9uocpg1uaa_KbQruQ9kxnQZeRINDkC-DsBKn7KhSeQkJS-gU52JbgpUql84nX5zsnbmRni52iWS8x90Rlp3Nhiu71XlOSbxYhExnCE5kMqizmeUhqdr2U1zAzw18wPxPn7ZMmA3tuo7fIj165JX6EqWYXaBRg4RfR6e5KJ29Mm95LwYf_i1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGQtmUsUVeVAK0hX3AbX5rw9shLtjxak6f5z-1ABAjk3iOMSC1NnEQjoyCp4kVF24gzDDSlqiK7hs1rJ25-F4Im4rbUecIyB4Q-j7S2y_a6z5Y8gLBL0PYQxpQCeGzc5MznpyrtQHmRCuIsZuNu2zPuT6soRlPD3C_oA93RgdTyKfANr30OG0N3mAg0rGjVguJXEaUHFB_9DLx885TMu19zZPYuBaCy8BHuxY5Ssvy8pvuhXZNBJ59GoUy6QSMC2pmX1L8HF40YT8YgSAHw5g156lN4yhK5CtKGY1j4bHh1mJp2OxyK6eK7mzpNUJ1Nb9i19Vqeb-nSbinIdqkbGYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در آستانه چند ساعت تا آخرین بازی لیونل مسی برای تیم ملی آرژانتین؛ دانشگاه بوینس آیرس دکترای افتخاری خود را به مسی اعطا کرد که بالاترین نشان افتخاری این دانشگاه محسوب می‌شه! دکتر مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31112" target="_blank">📅 23:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31111">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUY8vOQmvbVYPA6a6wA71Cmrp56bM3MPWWOFiFYvnKyhM1vr4j0OSgAVb5Vl3Agwes820Y7ww_dTsbIjZkwJBT_3IgrhElTd7UEfDtk_a9fsozIi2SMS0tcoeFwoA-h_E0gGzqBTME5oruuAVcmjvxqv_l5hzwXUXdPqZOHnAZs1KKSySK57D2hrcyg1sYqSXc8QitDlSvC7g56f7uRzOZEouUBITNganAYiY-CDnKezYAk6fPKb_-O4rWgjhy1zyjukHPTQqlkeE8oclDy9TLuYDypaDzzBhMFxoTYL0WXUfmRqeA0fTa0agbjAp5T4-L_4sS3ZYgO8XrmQjnPX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
مایکل اولیسه از ابتدای‌فصل2025/26 تا به امروز در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31111" target="_blank">📅 22:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31110">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/befsjb6LPIU45ECfKOcv96G007wx86AKm3tvoQN09jnd5L2Ay5NPNZZsLEAK5nLOelZ_zTeVlNJv7C0-O9lm6S1z_1JJ__w47ySHqvSExW_MMcYS3KdKV5mkPcNAYCTdZz-csjyJs54kvLVR2zeQEm3xtFRs33TkANKph9yDc-VNFR3TBQoUbedaA34prXjtbFvBPf-0ZR8El6Dz83EyAees2S_zcVur6sJ_p1D7RSiaK3P3VGzV82ST4I7UXknLsJQl370pR-Y2MRIfbvUeC8qMfJ6Q7Lp8mwbVabZ6U8UXCZc4u7P4hSVODW1M8R3UoJWuMjyn45H8ivJoQa7tPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31110" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31109">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnMsYoIwGCxd35fgkFD9Bcx7ewWpGXbkIC1rpaivbUMXeRtdggapFfpXwb_QYi3aa2Veo2RQzdOe3gUsI2dP4NxtKuLuh7gRfA9s56YXjzJ_yz-H18RgZfD8oDAmT3HHuOj0K6rISDdx4sVT6j8q7C7j7xfJkFXiPH7N4toGmaFG_VChDD3LaesZTC5tBzN1h1UnNWxdbLFilQvdYScKGAKt_b3D9DfANPgnz658AZa608pay12X-4VAxYQ0S5jqvNSDazf3dRwtNhKYkjf8WKbhbyw8KEtjh-EuMFUcjW-IkGIgxwo0_1I61Wl_4XS42f3HvBOFCnybmujlHeyFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
آب پاک کریس رونالدو روی دست فدراسیون فوتبال پرتغال و خورخه ژسوس: تا زمانی که این آقا سرمربی تیم ملی باشه هرگز به پرتغال برنمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31109" target="_blank">📅 22:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31108">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAXQfPWJHHgsxa_Zg41kMRbqn1uZqAUghpcHVf5LtvzaFaeJkaMLz5mRY73ULiETmE84h9A5dDbh0MgUbun1SXyjFAUvRDJJ2-mfwpuuRbmfTY6KxT1747ni_hcr50_TAFf3MDAr9TIovk1hYZm0wAS-79TIbCnkdxbBlhZfeCJdRaA3ppUE487zc1bedPaHNnbODVsyVBNMPpariPYvOLAuaeqzXsHMbcGS-G2d1X_L4wFgZDHazULeuI0nbhQcBoZ0V1HQn8EnCUOHl7vKUa5z4R0g-tewActnv2DYNN0Sa_hICMSOOpjjfPVVLX45HRyBb8PvqXEn8HWb5SkR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
وضعیت پشم ریزون خیابون‌های آرژانتین رو ببینید که مردم‌دارن‌میرن‌سمت ورزشگاه برای تماشای بازی خدافظی لیونل مسی با پیراهن آلبی سلسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31108" target="_blank">📅 21:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31107">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9YqOMfU-6d0Q1s-FMP5L7v_I8AefklkVL_3f9UmxfDaZPiDttymmWcMEqjkD0GPw49s-kIBDu6tpprL90l38jKb1XUWSbdGqukWB4yhdFPNcNBAREvQ5d57xCmvN8QrkV7bIrzESOhonKBN_us3-4a_dz47PTvN8fBl4iS3CNB1x9zUlPG-owEoBcBWNd-2YbriK2OIFKPT4ZwrVPITRWhALV0BLayIXIztaD9v3fSMziKJuB60HuS9JreVhS5NnjpsUGrm409kflulSH5QmV1evIf46COT5_pHsEZzi42zbHi2u86_Qm1d3Gakbpt_nOIuoOLM45d8Sc4_NqTzhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وقتی بارسلونا رونالدینیو را به خدمت گرفت، این باشگاه چهارسال بدون‌قهرمانی در لالیگا، پنج سال بدون قهرمانی درکوپا دل‌ری، هفت‌سال بدون قهرمانی در سوپرکاپ اسپانیا و یازده‌ سال‌ هم بدون قهرمانی در رقابت‌های لیگ قهرمانان اروپا سپری کرد.
‼️
باورودستاره برزیلی همه چی تغییر کرد. جادوگر درسه فصل‌اول خود، دوقهرمانی لالیگا، دو سوپرکاپ اسپانیا و یک UCL را برای هواداران به ارمغان اورد. یکی‌از بزرگترین‌ بازیکنان تاریخ تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31107" target="_blank">📅 21:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31106">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=M4ndKCMCadpZpssdPfx6KNZbqlQt2DxAi248UiumACCzKd0tCu_03OU59C7OEOssV-7Tb039h4477gWaB-OoujD6CJpu1oXdPzLDo9C-t7Uq0mP-4A7yG6Ne1f29TRbTRUcNWtHExqY0rV4pAbm7kE6KHI0xkBKQkeRRbV7tpbt9s2pRRrh_dKJXbaQ6jKWBYl_86Nmw8a1rXF3NSNXqWALwVxT3qssa8GBT6krH-Dy3r3nAVGYuYYrNcSa0GKC1bMAw425Q4W6YGSRXWFIZgu3hEfRiKLOWcHQ2fmSpcm7yOQVWNIPh8u5LmKFnWZQt6Zes9LbhWfGSYE4SDxl7s3Ns14f6nmyCET_H_FbFUyypZhxKR59KHhuOVRVsDWASQWCjABXnk5RaozYeEAv5AFNcaYKpqX4t0gu3kCIZHKJPvibc4Hz8ysYCARzgt2CwN2Dbr6RMcpYYYxKgsXOvFIhv2JCKCIguX-PXGFyVi1jBztuG-xeK2IiCLDmOb9zZjfqAwHaiPCqs2ckJlVXWrMAZONCxsovmbbmZr8hSACkK_JdYrsgy0TbWKTH538cKkO1tfLlPptfJeUZMMH_52bg4LRq2nPyd0UQIMMJBez-PwSOV17n9t_dZhF75mdTufGXTkQ93sSJntnmOUA3X-SRqhxWdLq-DRmltDB6x7wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=M4ndKCMCadpZpssdPfx6KNZbqlQt2DxAi248UiumACCzKd0tCu_03OU59C7OEOssV-7Tb039h4477gWaB-OoujD6CJpu1oXdPzLDo9C-t7Uq0mP-4A7yG6Ne1f29TRbTRUcNWtHExqY0rV4pAbm7kE6KHI0xkBKQkeRRbV7tpbt9s2pRRrh_dKJXbaQ6jKWBYl_86Nmw8a1rXF3NSNXqWALwVxT3qssa8GBT6krH-Dy3r3nAVGYuYYrNcSa0GKC1bMAw425Q4W6YGSRXWFIZgu3hEfRiKLOWcHQ2fmSpcm7yOQVWNIPh8u5LmKFnWZQt6Zes9LbhWfGSYE4SDxl7s3Ns14f6nmyCET_H_FbFUyypZhxKR59KHhuOVRVsDWASQWCjABXnk5RaozYeEAv5AFNcaYKpqX4t0gu3kCIZHKJPvibc4Hz8ysYCARzgt2CwN2Dbr6RMcpYYYxKgsXOvFIhv2JCKCIguX-PXGFyVi1jBztuG-xeK2IiCLDmOb9zZjfqAwHaiPCqs2ckJlVXWrMAZONCxsovmbbmZr8hSACkK_JdYrsgy0TbWKTH538cKkO1tfLlPptfJeUZMMH_52bg4LRq2nPyd0UQIMMJBez-PwSOV17n9t_dZhF75mdTufGXTkQ93sSJntnmOUA3X-SRqhxWdLq-DRmltDB6x7wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رودریگو دی‌پائول ستاره‌آرژانتین: هر جور شده به مراسم خداحافظی مسی میرم و از دستش نمیدم. اگه زنم بگه یا من یا مسی!!! من مسی انتخاب میکنم و اگه بخواد بره خونه باباش‌هم مشکلی ندارم. من با مسی رفیقم و کلی خاطره باهم تو تیم ملی داریم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31106" target="_blank">📅 21:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31105">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhgFJvJihhPPHATk9hYnWzFJq7svjq_QBDPt38b4ahDsebvaETqZW5Use887Y9eFPWY9aNXYFMI0Kliw-BdU5B39L-9orK4rYJhdIIS6QZT9eyqjWSBeaojXod8XkCnK3CK3cQIrQyPwlS-o0EDuM15oIQNmYI6_qHKOguptheudufKlAwWjTepeReovDd8_xFyl2MSp7hj-995Z6RWpPhHXCPfjR6618-36gG7B4ZzYKaesDzkcgu96OwkriWf8z1KzhVjfhLZrqAwwsr3Z0qtce0XL2yaNxnwIiFts8pBn-I8a7CGTVwFg2eFiIL9pA64wo_B4I-96ch1woqprLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31105" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31104">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RM1UDutYAt1zOJP8hhIYpHTc5r2i9sZ09pi1_t6SPwvHBbRBGEXZ6viwfkY3k5YlGSw94t4Ndj-EZQlCdyoXEclGhLdLcuXUNsq8nxx6TU_oIiYHELQkLuRVK8m57mijhKTZfg8VV1bhSpQEQH7felLVYUwKC8kL9i7xcpYrdpJovepFtyCjW337fNSZlqciYv9GH8AYO4ykvxDTrHyFcNjPWgCeBjDu_AjAwITzix5ADHnTx-iorlrSnrfkLYami_Lpwv7K-lhj6PRmYP_j1rEbPUAgw5zptLb0SH-2VkK9cMJXxayunE0qTpPRJXpApl9N8POfsG8EbXIE3q54cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش کریس رونالدو به صحبت‌های ژسوس که گفته از او عذر خواهی نمیکنم اما در فیفادی بعدی به تیم ملی پرتغالی دعوتش میکنم؛ رونالدو: حتما میام!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31104" target="_blank">📅 20:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31103">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq9mZO8smURIyBViopRx164IVH2DvGN9eXZlWF-wdU09Mj17nSkMRu4l5ywnqGxiqB4FYPCUzQeovRUtX7zF5wwb4neyFkMUJMPhUuywa7jIorYg0VOTGww_TdUAvKiYniytUCSi5x0lEBV8JOsh8c1LtaE_8_9zA_cbe4Lwtv-ROQ0jaae2QCRSMmjzKXoTJwNHxzE9145uI84IvYOshQJRq2yPaQEQCWAipNZ57o1IZNfrbUqcMlBmKlR14e3tMJL5Fsx1897q2UK2yPmRmCoEg1gihs98zCYcTlaTLbFzkfJVvBCJj0hhlDcBvmpb7deuGNyOTwoBQNR9qzkzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی باشگاه پرسپولیس؛ حسین کنعانی‌زادگان و دانیال ایری به دلیل مصدومیت دیدار روز جمعه مقابل صنعت نفت آبادان رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31103" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31102">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCzkMopNDBkC6tM_iRfa4O64_k_IqXrIubyvP2ve_Qap4mhrDMKv2s-WOiX96WNbzv8QH4hPPbesSK5YCPP7smE7rppeU_4YFpkPftNa6YNkEpVA05OKFkOP_EPHP9uhok3jyJnwu9yd_MXL3T1aQ5sGiwZfXSRUj3U3gL_BG2YvYLhxBwpE9v6V1FMgylNjYWlqcQUDQULBkVQ4oMAdNq2ff6jI3VzbNUYHDlY2vdbx1steohD6FyG1pW1QWkeiq35S4FZYyLbeiGtpIvgY_0rFfbsX8AaJGs9iVfhdoeAWrq88Bjd8qq0uJdrzp4jYBklYFMPDH5zd67VreF9z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جود بلینگهام ستاره تیم‌ملی انگلیس که این هفته یک گل و سه پاس‌گل به ثبت‌رساند و نمره فوق العاده 9.8 از سایت فوتموب گرفت به عنوان بهترین بازیکن هفته سوم لیگ ملت‌های اروپا 2027 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31102" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31100">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV3JhpdGLvEeOKtca_Fdif8J_h4FuYhcXrH20CUW0wN2ZIYCbGtcA-ty-xG4BNgidTCCAJUiAwmKslCx9Xhh_APodPh2-Z1wwWmDzWYcAqtGtraDdkPjylqwMHm88E2aHUwRWLtr4R7tzsofnedi8xL3-YjAKYPce6oYpUXCHubCld5rqL0wgUEAGfsdEHaX-9WGSDUkVveuKFxhloKT1tUhb0E0C8hRaNc3Q7kFrL9R4pBiZH0irunL6XGTN7HXWufKiMKNyyKVHeDdRXphsZ2w7BJ72sM-DvKweaY-XofDHJrkFI3H37kBUrRPO0oDkBKT9ZdMnKX5I_m3VObAig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌خانم باتیمای‌بزرگ فوتبال ایران قرارداد میبسته و ازشون پول‌می‌گرفته و در ازاش با داورا سکس میکرده تانتیجه‌رو به نفعشون‌بگیره. بعد از دستگیری این خانم اعتراف کرده که با بیش از 40 داور سکس داشته و باعث صعود خیلی از تیما شده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31100" target="_blank">📅 19:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31099">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbEBBIE2SrRzKJr4fl7ewsXAe7pO1CpA5QCkXkoanzMBuKKlupk7VBJRTurGPCfhPtIlylh_QFDVJrT2Q1Zvd-9qKZ98kroSKylFjQP8w59CrPo9HfimbKxNWzAFGPnJd3yAvgBBWeZaF3nnGB6K3eTp1ZkgpsCbnGx0u-imcIQGUrZFOY0vEjaB1s_8kuBuIsKY5bis0wfnWS7G9WHDqhDgoKdqxH0IZejcyU1x6Q3daHMrTHHo0PYgp8v6JJA7NnvE2mcmeC3RrF4Ef4VA8nj7GjvjFeLwK8bdSLqH3cZTXaBIvAFu3H2-vjdAWHBSBR626j5MIlxqfEEABMEBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
فدراسیون‌فوتبال آرژانتین قصد داشت که بعداز خدافظی لیونل مسی شماره 10 این‌تیم رو برای همیشه بایگانی کنه اماقوانین فیفا اجازه خالی موندن این شماره درمسابقات رسمی مثل جام جهانی یا کوپا آمریکا رو نمیده و باید حتما به یه بازیکن تعلق بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31099" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31098">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3iA7AOpeXcoKMy1pol3wMuRImWkWHCoOUtTng7SfBa6IsyZ4g8GCQWi2eGjoRUTfAVWJ-6MA8tgWlbpTWEvgbSjzynHaf5rcI878cdc9zXwafsgTPhSIbMr4elbxSUf5UCmGAHTCwgYdwd8pXGqBu77pEo5b7c9__52wmtLWKGqFykLPBEL42zY37A4XTetPBYyOSAGQyiOSK6jZnx_YATtFpd9DeALAFBz4B6q1pyF3O5qufRAGkSIylne5_VN9d-TSccpju5mcvCa3ZAATz1Ep6St_0F9rznZn299iVceLaX5nJluoSYhJBLAmct_btc4IZ9IEX1-wsAzECFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
فابریزیو رومانو: دنی‌ کارواخال مدافع راست 33 ساله سابق‌تیم‌رئال‌مادریدآمادگی خود را برای عقد قرار داد باباشگاه آث میلان با کمترین دستمزد "سالانه یک‌میلیون دلار" اعلام کرده و درصورت‌موافقت روبن آموریم کارواخال به جمع روسونری خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31098" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31097">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWE8UHykS414iMUZDsa47gYFgrUXWa5U4y3SZsxnD4AmjRwSAdufAYUXzzWa_71S4hXgtwsJmT1w5MQ84Ut9lxr2zicyww34FKhIcE-b3lHdNL92pNO8DRaFuEZGpAKj-MFvrhkOzny5D6133Lk-RBW8ZR4RHuQJC1lfbEuaJWKmo7E4CyTlmywECPYpkJIKXs9ShQ8v0qMnf36EraS88Eq-Fqhu6ZqExkvk_5Ew1eBMK1kZv4Oz6jr8dN0JCk_XtejHz2m7ASavV_o7qaMYTcDZXhAEEfm9CyZ15JeymaOfHbP5AySd9Y9TKkxyLrL_Ll9ZbtAEDPqPuxQ1NMSTBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
امشب فقط یک بازی دوستانه نیست؛ امشب قراره که برای آخرین بار لئو مسی با پیراهن آرژانتین وارد زمین بشه؛ پیراهنی که باهاش قهرمان جهان شد، اشک ریخت شکست خورد و در نهایت به بزرگ‌ترین‌آرزوی‌فوتبالیش رسید. بازیکنان بنین گفتن امشب فقط میخوام از حضور کنارمسی لذت…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31097" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31096">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=ovy7ufO18H0EYAhOPRz_E19VyusEn4X6jbmMnm9L7vxusgKAql73Qck2R9QL_QYnBFasIEVkTgg2nluGGcbD0G-yGw36at6ImHhTJ8VG0ytwTmmAoK0Xt5xpiaDREtOC45kvA7t3jPZnRkivZZzVbETPRMITqEKt0qw_9VxuFm4plY4Huwlzlfnf-FqTX3cwYdIomYhKAjlDb8cURW7reSvyMDH41v1SE4R0TGK3J92T8HyCrtQUTD3mT-gqN23BhiLZ6G1M53YTSg9XehRiKOb3_Pa9SUpwGYEacb1GGq7MCWtLp3Thp4jmATjf7oBJaxRIvaoqIJ-AsudQ_sb8Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=ovy7ufO18H0EYAhOPRz_E19VyusEn4X6jbmMnm9L7vxusgKAql73Qck2R9QL_QYnBFasIEVkTgg2nluGGcbD0G-yGw36at6ImHhTJ8VG0ytwTmmAoK0Xt5xpiaDREtOC45kvA7t3jPZnRkivZZzVbETPRMITqEKt0qw_9VxuFm4plY4Huwlzlfnf-FqTX3cwYdIomYhKAjlDb8cURW7reSvyMDH41v1SE4R0TGK3J92T8HyCrtQUTD3mT-gqN23BhiLZ6G1M53YTSg9XehRiKOb3_Pa9SUpwGYEacb1GGq7MCWtLp3Thp4jmATjf7oBJaxRIvaoqIJ-AsudQ_sb8Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ شاهکار زین الدین زیدان در بازی دیشب؛ فرانسه درحالی یک هیج عقب بود زیدان در ابتدای نیمه دوم مسابقه 4 تعویض انجام داد همون بازیکنان کار رو برای فرانسه در آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31096" target="_blank">📅 18:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31095">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=lXvQioOTOxh5A6KJOApTQc5d-AcA3e0Si3NXjcgeJHRpaxt5FCk4U0l5jaZsH5cMb8rMVNNB2P5kSUrL-mrr6L1b1w5Tu0KvoHsLISf89phVMcCcvyeQf6jTk0mbUZN9NqLMPE8z_vDVsDTXwbyH6ciPjBmNBtex3JZEpbHasnQgBOHmxGc7JKED35XV5XdjORNopYFj23q7UP81gTxFEGqkRE3131ftZBIo85GFzQaVEv9E7-W9nw0hBwCLkOxZAx44cf9iDJdWCO-MOZ8U7-6J1w6sllbK1_NBBhtUe6GvECtDTZf83cYK1tuESfqmO0_Ultm_StiNkTZKUYCC6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=lXvQioOTOxh5A6KJOApTQc5d-AcA3e0Si3NXjcgeJHRpaxt5FCk4U0l5jaZsH5cMb8rMVNNB2P5kSUrL-mrr6L1b1w5Tu0KvoHsLISf89phVMcCcvyeQf6jTk0mbUZN9NqLMPE8z_vDVsDTXwbyH6ciPjBmNBtex3JZEpbHasnQgBOHmxGc7JKED35XV5XdjORNopYFj23q7UP81gTxFEGqkRE3131ftZBIo85GFzQaVEv9E7-W9nw0hBwCLkOxZAx44cf9iDJdWCO-MOZ8U7-6J1w6sllbK1_NBBhtUe6GvECtDTZf83cYK1tuESfqmO0_Ultm_StiNkTZKUYCC6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی از سال 2005 تا 2026؛ تیم ملی آرژانتین راس ساعت 02:30 بامداد فردا در دیداری دوستانه به مصاف‌تیم‌ملی بنین خواهد رفت. دیداری که آخرین‌بازی لیونل‌مسی باپیراهن تیم ملی آرژانتین خواهد بود و این فوق‌ستاره آرژانتینی در پایان بازی برای همیشه از دنیای مسابقات…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31095" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31094">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUjaqAXc_OFXb-iHDFVUYzBe_63u8kiBLBnPeGKAtwQs1CqtbFMT2n1twmL6brlajBjxoYNXyXY8upsmbKg2--g-I9hvtwlIHj_jbyBAw-3k1Iw8kLJNbzaDv_j_eRDkbZw_kPaav_oOjZJPWZMDRxvvX6ORdCs2mZoaYKyc4hHPN7we5ivdwocISmpeRBdIOhc8AehZfJIrqHx_7o3IqoG5xXAj_bN0uWOfsrpLH-GHcCy7kldg8BSJzcv56RDOXID4qnICbtg-S7Jq6wwD_F06gOlCCcz4WxBfp6Lz5EkjBnJa5OCcD7r51Ca43N0j7vAK_0-XVdP-NAmkQBAAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو:
نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون یورو دریافت می‌کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31094" target="_blank">📅 16:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31093">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=rWdIK2um-kdWwC0mLPXLpDUuWKE9LjmN_kSI2cwnUaNCG1kZDHsEsvvwTPHtk1H5CKsr7PBw9WX84j6rQ0xM3ta0V5iyJHwm-Z0Fo-cFV7epJT5DsC7brI6fdI7SOBiw0tHjMjQf8DQADSYcJkwdNA3XEbc6Bf54adtZU9BXYVrTOKrEQINi40s70TUOAJAJMLy5Fp-v23xE017NyuDycjA3EJwi2-B-1kfnwKDxyqUJe6RF_77cpINyAp3Rb_Tsi5wut3V9mzr9i5l1Q645coIWknmPYduC6QiZnDbZmzuGcHBIWY8MO-JT79ImytFBs6kaTwUR6abXmop7iCy6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=rWdIK2um-kdWwC0mLPXLpDUuWKE9LjmN_kSI2cwnUaNCG1kZDHsEsvvwTPHtk1H5CKsr7PBw9WX84j6rQ0xM3ta0V5iyJHwm-Z0Fo-cFV7epJT5DsC7brI6fdI7SOBiw0tHjMjQf8DQADSYcJkwdNA3XEbc6Bf54adtZU9BXYVrTOKrEQINi40s70TUOAJAJMLy5Fp-v23xE017NyuDycjA3EJwi2-B-1kfnwKDxyqUJe6RF_77cpINyAp3Rb_Tsi5wut3V9mzr9i5l1Q645coIWknmPYduC6QiZnDbZmzuGcHBIWY8MO-JT79ImytFBs6kaTwUR6abXmop7iCy6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیدواژه‌های تکراری امیر قلعه‌نویی در چهار سالی که سرمربی‌تیم‌ملی‌بود؛ همه‌ی همه مقصرند جز ژنرال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31093" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31092">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1YYHLSAzJ7LS5uIhYnpKOjt7rEOdqsrEI_Ofn5uMRNDZ_ZC0VJSaHB03jmppKqiExIYSRV-dtOCzLljL7O-7B9SLG_c6lmAfY9p5sFiBAbK_xlJWMR6fMCDOEIdMA9VYBzH9A_IGP_40xmW-intOMMv4V1_HPotuPGKA-Mh-pl6sIajeIqJFiKA-mkN2skHaL2tZuYMgMX6mEeFJaLOK0kvNdutl7Tk4EV-eX2qpfDAqyO1Zp7tFgYPTchKc_I3Rjn_AWiK1zhs3RAfHTyMfvs92PJGFNmRiUeLdFbrVE0ncE2D2gg7BdRzcWLsw0WtljbOamzyr3Mvsp3sO-1vag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تصاویری جدید از دوست دختر کیلیان‌ امباپه ستاره فرانسوی تیم رئال مادرید در فیلم جدیدش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31092" target="_blank">📅 15:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31091">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM5qH_IGpF7Z59NGzwP8DSCK0P9K66NsfEn6eFw8QRtV_2qEYy_i5a0quFSIRhpExeGZNAGFqFNKyFCKvduTKZ89N16jJIySg-BDyY9A-8Grz6Yms4EX4mHEa2qIIicdcvppPC3fLzwO3OEo-G1WwNR2c0bPUzCKRppRopmm013d_gkCGD7iaVS_2DielLJN1rf5MidNS-pUSqS_LrR8l2KbnsoazW4wgRb5EZCZxRAHCZ6g-swndM0MIbTIT_2dt79iH_zuD90meUdFMe8Qx_1IFA7ecxT1_NSsPED04A-16-vHCrkR1RrMSnbLUIctQlWnl9isiv4AV3RGSbwM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31091" target="_blank">📅 15:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31090">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=rtfO5QRojk4p6fXaIwv41uJZbMGow_-8Y52MgvOcacGpQnbOxGAkuqMt_Ul3NdzEoh_VUkXM_to2HNzpZpw_L7IrkfVQP6WjZVNsDJloRA3Se6LG1N0BDhpP_AhDxN_wyHo8JnqPhY20-CGhO9YBcLGUbMNosga-TgywlWYLxPjmsSKXkYSCV4xLyDnWU1HHsJ4YrrflzcY_yMLGHoRs4WyCaKr51s6zOMsBA5mRnaTD6ZV9KgmIZV2bD3S0VwshGL8IRiP_HFbVa372bJ3ovtpvJDqUuxxBA20SfsIHPKz7FLDn67aUtv5ygN2vdwz_Tn_CIIpbCqqn67oJi635Yijz6TFLHE4x0rOyIh3NgFsTZIMKp-jLCOD10xmTqBOX2T6Tb75q-v59oK5bKEjRAirqKuwA-1mweldy7aD0i8Np6fOG5tWy9SzN0fiXRjAexEv9BdoiCFDvITdQHJRCZyR3z9K9YwOOGz4t3s19hUEYj5GGlmk408lOVHX4KICzg62VQsOzo5msjf9LwC9R62GTdczATMYRbATIw-I5tMx0KeRZf_OPTWlWYxj5nS5lVOC4zghj-2kBTjXXHEn3pYmFnRQXQ-nNv9D6CCHXfmEjRCJKeaN2WwIBs2MQoc-ZeAM2h3GCSf9_d0xxJbY3fSCsKL9HT6gI18awyaa3udg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=rtfO5QRojk4p6fXaIwv41uJZbMGow_-8Y52MgvOcacGpQnbOxGAkuqMt_Ul3NdzEoh_VUkXM_to2HNzpZpw_L7IrkfVQP6WjZVNsDJloRA3Se6LG1N0BDhpP_AhDxN_wyHo8JnqPhY20-CGhO9YBcLGUbMNosga-TgywlWYLxPjmsSKXkYSCV4xLyDnWU1HHsJ4YrrflzcY_yMLGHoRs4WyCaKr51s6zOMsBA5mRnaTD6ZV9KgmIZV2bD3S0VwshGL8IRiP_HFbVa372bJ3ovtpvJDqUuxxBA20SfsIHPKz7FLDn67aUtv5ygN2vdwz_Tn_CIIpbCqqn67oJi635Yijz6TFLHE4x0rOyIh3NgFsTZIMKp-jLCOD10xmTqBOX2T6Tb75q-v59oK5bKEjRAirqKuwA-1mweldy7aD0i8Np6fOG5tWy9SzN0fiXRjAexEv9BdoiCFDvITdQHJRCZyR3z9K9YwOOGz4t3s19hUEYj5GGlmk408lOVHX4KICzg62VQsOzo5msjf9LwC9R62GTdczATMYRbATIw-I5tMx0KeRZf_OPTWlWYxj5nS5lVOC4zghj-2kBTjXXHEn3pYmFnRQXQ-nNv9D6CCHXfmEjRCJKeaN2WwIBs2MQoc-ZeAM2h3GCSf9_d0xxJbY3fSCsKL9HT6gI18awyaa3udg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هم از ویدیو کامل قسمت سوم برنامه فان و جذاب با ابوطالب حسینی؛ عالی بود از دست ندید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31090" target="_blank">📅 14:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31088">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnFD_op9mDtuzdK8gzkYW8QtXQ0wxx2uvMrvD682BCa-IluJ7BhpAfYG03hTGi-CI0z4EnNNRmhC4DOztzhNLvmyzMhHSk3j8WHThuZKpZDXxWdixbqhyvxgE4pQVnF_8UF54MKOGXJet009gLUosuQpn57K7nfELKqs4324n6VJQIOyBWDsE8pPh7EaY1IIdvHESyWgBom3rQ16CqjRNas1t4JO2Vhtphaxi0YckEJO8bg8dwI9mZ2fyxno0P_L5To3NzcnrN888eyR8JOycNF6C7YwbLvxvHMWmv2frRNp6PEKMLWa6L60_Cnd48_SDpvHnsAsD1qAOXNZAk1gKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m5QyipKKrHZd7xKwoMdrBFYbR9a9gJEjip_--JXfLZmhgUUjj66WJ38gBdNHSROB79jKXw9N0jgJmqHDchoyRMS2iYPGaM8RA5ntym8hmkwOUKo5pIs9v7mLROS8fh3QzyKY5Gv8mi-22epdVYf3xRymLfgeMJDvX4QHp_TziD-spzqMClziN4ArCacEyxHDoXOnKcsaUc3Cn_pFV8ddRfzNVJDgbFhIiJJYvPubJdeknxyZIjVSntxVo5URCDpHWG2DRICX73dbqsW1mFGkJL8uKR1VBoIFnH9kgVMHwXT5KvW61EGhXCigZcb4-I5yKZBHSqfU0SfB4qk25fSwfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31088" target="_blank">📅 14:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31087">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDs1VNBYhfwQSqoOHfVqSuHRC5TmmPXAytUXHp8bG3vc50kItmqgd80IsI6mu384jK2c5eIyRZYm-_mKEpikKhhl-2R-G8Uek5IufWzyrAi6qesKM53OfwAKcOce-gj9febtPJpoaYosqmiIOaHj-LnK2Go8tT1CVltXJDevsAt1SUnyDh48P8ZEqb2UfqnX3G54tWBCsswn3xuINNjeeZnLU5LA7pZbMrA6DhQ-t38nEEVQlKEjEqNII5DSCVxbB4x-iWBHAXf9qW6StaTcZxajNbOuQkbLKXi_W52SLtbvbBnl6Q8qFTFtzHDnYlWQaEeNzsdXX5FXcSxPwReMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31087" target="_blank">📅 14:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31085">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAe42OxcmVMDtazmcS-LGCfTwa4FR6qjxjSYCVAoJ0nz-Qw0_UwnzwyAQEhpEGJxGMhTwiSNjWO3ZNfJfkRyahuU6Zqf5bQBcNUJuScSjbztjxAsUvHyORdDPua8eVOFNz6dVskNfltnzs-QCzjtu2T4KHVvRgqN4535UWJZToYyyyWtq9I4EjL8Z3hJCkWt4kx2noKiFFyz9mY6iCggzuK9ZmvIPXofRXvnFVHBpQRJE5SGXPbEy5NXBttgiAyc359m208GCaK_LHgIkP-IbnWkaDlwykZb_fiHes41w7J8Xbuy0GiO0L7Un3x-GaIQlLzbhN90P52hLJIFN66eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PemXp5HS3rdxYLbgwmmqhWcFcfmlrFRV2hBPI8RrzVhrorD309aP3QjIHFL4B24LqkpOm5_rE0JbY__3LSjokDNhJRvgbnDdvKecxBwFlJeBcKFv6zc4hTQmUgsUNFxeVek8XKVyUXa8oUnlRxp4sCks84pr1j3G7El2ytVBRWIBVmYdA3yHnV8MDnCmQTmtTDFnUkpqEAOOYRwFsbRuIMzv9I_HQmE_KfH64C5XtOgzB9OsKdO8moNzvllAC91rp332vitWl0gF9pTZ0IbFgPX7W9UOHAg5p0h3lto4IaWTDToXK3zGu95XvQDl2yuCI0xvHN7J7vRoXQQFq7vebA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31085" target="_blank">📅 13:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31084">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ccy-nM3KRXFtQBbpZp2DJbANggagrdGmhS11urMeUFQSgNaeKzU13U5Yv3O0SnuurgTewXPVn6268PhdSLeLzLb6dimWDSqk6as8N5r7sUEK4S4tvIuDmXTtBXvW3ovCDGHAju4wKVQWkFrQ1tW1D_YcmqnBV-K0rJTvdmtrqJC0jlqABQ30E-pO34zqjg-AX2Q3NUud0-N4J1s0S2OiO4YirdNya-qV2lYDPxtzrSTysgtPciumEmGmKLBuy3_4njmDl4NiMe08__Zjur34udDkPCCvknYWOs9DrjBtp8um1qLzSUeYnWTXvSvJe-brnr2jB_j7VrAbu5BvwTQPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وکیل امیر تتلو؛ دادسرای تهران حکم به آزادی امیر تتلو صادرکرد و او بزودی آزاد خواهد شد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31084" target="_blank">📅 13:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31083">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0_uODcEyHAkx2j-8RPri99IW9hiIPrZ887cni0BSStT-cqWlF8kMcB3GnsKmmgOG1lQhSqryshEUZkUV6G4lTMnZtTs4LZoIJfUlSKPdtVN7NaZhbUs0MpSHJDqmsl3s4CyUO_WnR_ZkCNSfmRlfX3DVZROKOX4tWkTrluNXlKLLuX1ySV3RhO7CtfWBdMBcfsJ1Z34fAbK2Ci38eoXXKlaFb0eX3tjnYziOfGIRZauPHGTX1anN98xI9Liy6iRagq6fxG1YUFEg9apNzZozWv9Qx-WawZghp4HbFHU4y9uoU-UZmol7jfqPe9Vuq-DKgiSoeJ9MeZ3-Bl7A5JV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31083" target="_blank">📅 12:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31082">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA66VgrPa8C6yEQWVnJfbRnSEIf_F1D8vhZZG84xHU69TtFOzUWGe7tIYzxmj6_zSONKW9cn2zwWcIQtUhOWWwK37XUtYYZjuByzAnLsJS6p5aqQnePgr7QsOuc1piteOtKvKcPvoPqk0pB75WxCcHMX6caEwiuIiD8H3xo6rrs98ExzXMyHTfk9YZQKIfaSK4XhmHS0dPZrp_3ef1jxHDj0bpXckZCTelC-jTKVFZIRtevnJlFC4MJGMG6FwVZVDQC0vxB4GXmshDieXfDlwCmObEZURglPpT3S_ldCdNHMkTUDOayrV0WswM2sF8VP9PFzOm_MIxjPu5pzb2KVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ تمام‌خانواده لیونل‌مسی درمراسم خداحافظی او حضور خواهند داشت نه تنها همسر و فرزندانش‌بلکه‌برادران‌خواهر و مادر و اقوام‌ دیگرش نیز حضور خواهندداشت قراره‌این‌مراسم به یکی از بزرگترین خدافظی های تاریخ فوتبال تبدیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31082" target="_blank">📅 12:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31081">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=F-g0lwgStpdH3oemVUbGGI7LIctnoxJnKMWiSJ-sRVrvpjGtChbIOYyFophCbJixk5fbkg_E2ssu2c_WJJijMHM-w35kj25HD5MCjmSmtbO4i31nmLOx4VEVA9WrOIg3c4F88Tk8Q4EMggxFc206uEPpttPj9sFVRt5Dw7b4qiBAGYw8i4dqThjZonDtTSXOoNaNn29FyoljhoGq5t5TMkVvAUnfW7qUv1Imnfk4I1NyZZHnjhRQ6uSbYegz0DGCa-XFXGQjQ7pB_3EUv9CFzReAeDJ9rcmI3Xr_fPEbmmREb4XUN_TeeDIrf3Z9lRWbzZjRwJGvZmtvQm0vWqchNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=F-g0lwgStpdH3oemVUbGGI7LIctnoxJnKMWiSJ-sRVrvpjGtChbIOYyFophCbJixk5fbkg_E2ssu2c_WJJijMHM-w35kj25HD5MCjmSmtbO4i31nmLOx4VEVA9WrOIg3c4F88Tk8Q4EMggxFc206uEPpttPj9sFVRt5Dw7b4qiBAGYw8i4dqThjZonDtTSXOoNaNn29FyoljhoGq5t5TMkVvAUnfW7qUv1Imnfk4I1NyZZHnjhRQ6uSbYegz0DGCa-XFXGQjQ7pB_3EUv9CFzReAeDJ9rcmI3Xr_fPEbmmREb4XUN_TeeDIrf3Z9lRWbzZjRwJGvZmtvQm0vWqchNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظاتی فوق رمانتیک و شبه هندی در شبکه سه؛ روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده؛ قبلش داشتن هم دیگه رو پاره میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31081" target="_blank">📅 11:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31080">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXm_v8qJbnC6y__cFaGi5Dg2hfYVURlcMR4gLmoXcUhCmfJBtmPfZcGk7TOCYsuyCBduiokqMQfn43MY4-11srMjeG1uf9CBhwpprmhmztWSsRuFiw963OUYZaYeT7vuTXbr9JagsORhtFDUMzm9mB9zHbNptreG3BKM6n0y041EdvO75qzpyOVilkcbBkG5bwe-lLM_0-Hi5-M0E5VQrLDvRm-mK1v4wAGR8i1SyeKG59vudySluja6ZIQJpGgIuJuamQv8Re8ukfCG-aQ-0TjrHL0DXl8Zm5Vz3NkcQzdGHDPvTfLIiaB_5nUeaCKAwsS82dfJEHPOXR0_xiE7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31080" target="_blank">📅 11:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31079">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=LPtTV2iQEACH74JTOpYvM4DhItwd3BSx9VJWjWaWBpLrEJ6vUee9ceUZdxbdQwxKNJrZB2MYk1Kv4CMI3mGI62hJB4BXomcoMZ_SrSCX8ULdjFvW0-ft7-Lk0I05Zn4XlbzK05DWj_gI7ZFLtQQULZ0cIuCwkTF7DbNkaJXw0LuRpHBDns3L6NGJ6pisvcS23q5LFAExwxCuzYnG_mT1wV1uFMA46GsajUFmiTad2OFqnuGZA1ZU3Q9eH0wbP0r_8Ddu1D8S9rcYwBZsN7QmUwDK-4BxLzjDHkRf0hGTGR10rNcNRgAIxBzO9AQyO-FLExyEiRBAxgn4Xbz2Zb7BMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=LPtTV2iQEACH74JTOpYvM4DhItwd3BSx9VJWjWaWBpLrEJ6vUee9ceUZdxbdQwxKNJrZB2MYk1Kv4CMI3mGI62hJB4BXomcoMZ_SrSCX8ULdjFvW0-ft7-Lk0I05Zn4XlbzK05DWj_gI7ZFLtQQULZ0cIuCwkTF7DbNkaJXw0LuRpHBDns3L6NGJ6pisvcS23q5LFAExwxCuzYnG_mT1wV1uFMA46GsajUFmiTad2OFqnuGZA1ZU3Q9eH0wbP0r_8Ddu1D8S9rcYwBZsN7QmUwDK-4BxLzjDHkRf0hGTGR10rNcNRgAIxBzO9AQyO-FLExyEiRBAxgn4Xbz2Zb7BMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
25 سال پیش در چنین روزی؛
دیوید بکهام با این کاشته‌ تماشایی در وقت‌های‌اضافی‌تیم‌ملی انگلیس رو با اون همه ستاره و اسکواد خفن به جام جهانی برد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31079" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31078">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXvOSNXMTFG4UJAOsL1-cPR_RmF1aKEhUTRtJsHTfaAgJ_j1sTw4sIL3E9dvZhNg7vxVmqrYzB_iHNWh3FL8fKCp6To-kM761MBJPlXpL3dB--3j5sHUft60WuT0QDVZn6PPG7nvlXkvTY3Eq8LqLkDzHOej5xtncoj67owH3gNbC97X3x6K0ucN9f40DgxSOJvolNVXeajE1LFLwirpQTYUDYp1kdu8CTuRbxXJC-DCksQE6_nCwFQj9Ky_TIkBkN-gubnZc01OqqPwOPxRp3OgI47wy2ynXFUXYdV_4V57XvdShtxWUKy98ESqpuMMB7qFGGuHVWeXvgAj_8NF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛ وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31078" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31077">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=VCWpSs55It7GnDqsqHtQWauVSt8qCFaJb7r4JaOyNnkMbJ4IWNy2S2uooXUoEya13QKBziunq2Ev8Pqv7FwMQVi2pGXtf5ulDB6jOlfamM6ouhD2Hya6c1lw4yD5rPzBHWqJ4UKc56knLQ6r5m2fANujIYEElOl6RXumaW09934sMhhyFosibnkbS2CneN6yvSdDKBpkCvL939CehiQaO6QB9Ju7LD2AQTCcS-s-j83JwZzc3K3T-6fECXbipucOWpzonFiuj2h0QBO6tz7_b2BzYtavuN8a8c-NfNYJk32QNktHwuacpQ4IUhNf-fvRjERrFMqofxLD6qHlTT1oZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=VCWpSs55It7GnDqsqHtQWauVSt8qCFaJb7r4JaOyNnkMbJ4IWNy2S2uooXUoEya13QKBziunq2Ev8Pqv7FwMQVi2pGXtf5ulDB6jOlfamM6ouhD2Hya6c1lw4yD5rPzBHWqJ4UKc56knLQ6r5m2fANujIYEElOl6RXumaW09934sMhhyFosibnkbS2CneN6yvSdDKBpkCvL939CehiQaO6QB9Ju7LD2AQTCcS-s-j83JwZzc3K3T-6fECXbipucOWpzonFiuj2h0QBO6tz7_b2BzYtavuN8a8c-NfNYJk32QNktHwuacpQ4IUhNf-fvRjERrFMqofxLD6qHlTT1oZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک دقیقه از سوپر گل‌ های چیپ و تماشایی در مستطیل سبزروی هنرنمایی فوق ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31077" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31075">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMp_GyImQX1ya8GkDGS4tG3-EYaBD5sJE3XbkVSNy-yS1X0brfvr0fxDuqW-_HuA6CdpfadGc6mBDeM7EqfxJ9AfBGJDw4a_VuIgTUVNsNjhHb5VN6r1lgBpePdMuDDdXAACMFNe4SzxTNQ2Q9dTbPaxfzKVjUqqiWnI9oYNjR68f1gbYywy0Y02IYUabiPjuFVrzZiPgfSOgxyMrf_5v4DOBanAdjgxPK_Bbc1R14ZyykQ3T1cMrYpkf6XmBfIc39dRLF9DGvo59SjCobi29RBfXi-DneZ86agvt0fcZmzufgNPwVfDutS10H549CpcRXhRCXdjghs6wzuG83Pw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
خبر خوش برای هواداران بارسلونا؛ با اعلام دکو مدیرورزشی‌آبی‌اناری‌ها؛ این‌باشگاه با رافینیا دیاز فوق‌ستاره‌برزیلی‌خود برای تمدید قراردادش به مدت چهار سال دیگه به توافق کامل و نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31075" target="_blank">📅 10:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31074">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCEzx__j7M2t65a2aZIjbWW31pevqLbrp5JgS150lZef8xHD0qDEYx2iW-wTOZubo-xWUPz-WrOGBkQVQDVyLrBDvOVHbCLkx8S-shGhmItFaKwS82_2l6jp0VKwvT8Zk7oJuWYXdABPl-3n0naMwrVTLiDA24pUINREWuRU8tPpOGQhlROagiM7M_2AsCZhm3zPI5IWOAtjGAxb9mqFZOwNtidlu5jSAL8_3iMoGQKnL-A5oAoSo23--pqojREqx1BLSbGGpo418DwPuaMp_dGaIlH2cNm6spOqwOcPwapkBfL0Qv4r1wCcynV-JR-6TAbWbcxXiIHWjCLoVy9BEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛
وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31074" target="_blank">📅 10:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31072">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSjBhZUBqGfFpy0kOU-ntr7ohpR22cyZTeffCLI6Fwg4TBV2P3APFieToR7tZRHMHDbAGa7yVfCiFk7LX1hrl4QUEO0HSZS1XhcakRQ7EkRxdC_TBZ1xkCiVh655Ht5HcxnWD4DrKq7Kx4L_9iECbS_Dcs5Pj1j-mDxVSis7spspxjgW09inxiEYgCNIIwk72e9DKP2QpnvdvLBBtTcwKlWSWMc8nb9Hn33bilfm42d7KBuDj2MZbIdEVcfeha0hlWiDdriEs76U643LdpGx5IKGWuffBdP4F5Rd62_ohs8svwdCcYwsfuSnhVkTmSubgdZGqpOM_5TlxnbbC7z3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NjiRBwu_E8kO7jKIR8vuqcLEzy5CZ1efiqIynffPDgwGCWekOvYKfIhs1Zb8xg4bCsFztjBOg-J5pVyyJfzVAGFlgggMMmaHnyZpiNe5DPDUG60p2TXSXOkG_FmeQbKA2k0pm85voBQD_UkgysmSM8yME2FJ9TV42Q5BIdCLMZg5RfyWQHTujPlawrb-_f_sabdvdH5lFFk8dL0BndCNFSG4ozVRhd1xqXfeAMy7iEE5DcDAMjcW8GnkBVRsGbx2UjmpKJQ17NmmozM_OXdITjhr5ApXqQsezqaA-xlqEYkKwOEfLxINVBOYrx3AcBs1xzk1pxKURNxwOZ6EoCGhtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
👤
سنگ تموم پپ گواردیولا برای لیونل مسی: تنهاجایی که ۶ اکتبرخواهم‌بود آرژانتینه تا در مراسم خداحافظی مسی شرکت کنم. من به مسی مدیونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31072" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31071">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=AJj4770JY9dY42JGp932XPHLtj8neb_1nLw042HfX9bkYRc0rfUgnve_Dl8lZ4wHw6wAzz2uZB8eXWnTYCXS-un-fxeRqIaMETGAja_9zu6WEbRy6IgU9H9JRT4hS6L4I08WPHvm_cFW0Bqwtn7YYRjeEl86ZdZqoi81i6WTX9JZQKWV8qrcpndy9RaiMmKES2F3C6l-5XtnlyPvEyg82nPYFsvYvoTlb6XSQlQI4dyjoMHyojis804ufX2m3c71UICByOqXtGpXeFT0IsZ3C5wBWJl_t0uZZ_leNq_TnIR6JvVcL3YF2YDHkYYl2-oWORLr-vs25XfTlEH1NQc5zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=AJj4770JY9dY42JGp932XPHLtj8neb_1nLw042HfX9bkYRc0rfUgnve_Dl8lZ4wHw6wAzz2uZB8eXWnTYCXS-un-fxeRqIaMETGAja_9zu6WEbRy6IgU9H9JRT4hS6L4I08WPHvm_cFW0Bqwtn7YYRjeEl86ZdZqoi81i6WTX9JZQKWV8qrcpndy9RaiMmKES2F3C6l-5XtnlyPvEyg82nPYFsvYvoTlb6XSQlQI4dyjoMHyojis804ufX2m3c71UICByOqXtGpXeFT0IsZ3C5wBWJl_t0uZZ_leNq_TnIR6JvVcL3YF2YDHkYYl2-oWORLr-vs25XfTlEH1NQc5zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌ های‌ سنگین‌ و جنجالی ابوطالب‌ حسینی‌ به هادی چوپان
؛ هانی رامبد دیگه‌بهت برنامه تمرین نمیده؟ ایرادی نداره بیا خودم بهت برنامه بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31071" target="_blank">📅 09:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cymJPYPtV0WHlsNkm_SsA4o5ddBCu2pWXgsOlFh0iRuspbbPfLkRVeZafQN9kMuptykdCzmgTRAfFPUBj_6j6VOrDUip6AbltkoggpMp8mQqnAkURuOS8Eo7CQD1Wwp-VNEwj7Kti7QDV-Mr73lFGBricfROCVhuNT6_Lfm07JDZw5Ml6D00wbRUIsGd82s36iZYi3huvYuS-W8_0iNBtdKzkjWHbW3_2r_fVNhrw7O0-uj03hYMXZuQDyGjKAfhqLhLRo5QBdJ6tuRWhTt26Ummri3cHDR70xrzQD6aEyohEG_Oq50mAma2ZLOYNjbWmtxxiV0L9udIZthYs5YfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
جالبه‌بدونیدکه؛ سال 2013 تیم رئال مادرید میخواست تونی کروس رو از بایرن مونیخ بگیره که مخالفت شد اما سال بعدش این انتقال انجام شد.
‼️
سال 2020 کهکشانی‌ ها باز هم خواستن داوید آلابا رو از باواریایی‌هابگیرند که‌مخالفت شد اما سال بعدش قطعی شد. سال2026سران…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31069" target="_blank">📅 09:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31068">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAXLfjqF9QNnOEwILYbWLA3fOi2354l2brDYKMTuHCGGNGMLMqjNb0V4DDdL6aRhdm3oNDwahiUW66x-0jLqfINEGKBMceSni-ZtPLwR7YkVzVFpDOqhO_kMJv6tPmdzvsQCBcBKOH4gnQfcSGgj6j6QYkXOgRIkOV3gf3u2vO-COFMvJcmfXYuhDXRvUkgPuBUJ1jen--r9Qy2wIzWyfaiJrh5hCJuouA6S3MUm3kQHp9uu_GmzUnlD0L6u_DOcWJWQUXnHPKlB9_nPG32BEVbW9l37-sN4uttzqgkSodyJ4HtBfeYi3nMSYZMlJYFuiwwrDZ6GSgf714a6L__lXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31068" target="_blank">📅 09:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5fnAwm9z5TG9xpBw5Erb48ZUHDZVY6rEbQUGJhyIdxgNRE3DW3G0QcYJdOv4uUYYdJtbWtrYUgkuqzH_eKDWm6oDdZublVMSuP5_3whApyZOPwDxkn6RfaS-lK4nvesDMM__HzkpBs1-oSb3ieH2Co73ch6cb6BuZdDyDJo3kP_rd5CYX94JYyhZEmKPVV_3BX8TV0BL-zt6ugGIiNH5dSCOvhhGFB1ZEIYcYzC3X_B_FrojH1z_mbLwHFwRNhDMWvd_PkzKGxAoNvFltS2v4Ifr36a8eeqOhvdV1pm1ok7vVgdWjCF3LFl239I_I8r4vwCK33BYaCT3mk1NfiX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84daabae54.mp4?token=RF_LGsBKkAhBajlMfEtfJyNMPiT4Q7XSbxEgnKo-SH1u1DjcL1C1gpWkAgvb5EpRLNBKnw8t_Gh6wNKOHoT2M2qurKQNi9b0441RJrZfyANevR1rJjm2cEsUrnmZmAW_phQEkqWrIgwAnJCRNwA4on357sCFNjA4UH5IdSybtLQ_2wHPT7rB6Z2TCno6ZNAzjCjPMilfxMzHS76CK0iSaL5Gwn4nG--aaIoUk5crmOGvsmRuEdbmFTimIBYva54LJkTtZMmmYPYg3g48n9BQfzvPgYj9mGHnLxnq3Bsrk_tOCpfxVbyyfzqGiTcqNuxYvQ4RoTBsckcKxo3TbJz1Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84daabae54.mp4?token=RF_LGsBKkAhBajlMfEtfJyNMPiT4Q7XSbxEgnKo-SH1u1DjcL1C1gpWkAgvb5EpRLNBKnw8t_Gh6wNKOHoT2M2qurKQNi9b0441RJrZfyANevR1rJjm2cEsUrnmZmAW_phQEkqWrIgwAnJCRNwA4on357sCFNjA4UH5IdSybtLQ_2wHPT7rB6Z2TCno6ZNAzjCjPMilfxMzHS76CK0iSaL5Gwn4nG--aaIoUk5crmOGvsmRuEdbmFTimIBYva54LJkTtZMmmYPYg3g48n9BQfzvPgYj9mGHnLxnq3Bsrk_tOCpfxVbyyfzqGiTcqNuxYvQ4RoTBsckcKxo3TbJz1Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب دوتیم فرانسه
🆚
بلژیک و دیدار ایتالیا
🆚
ترکیه در لیگ ملت‌های اروپا
👤
شروع‌فوق‌العاده زین الدین زیدان با فرانسه: چهار مسابقه، سه پیروزی، 1 مساوی، 0 باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31066" target="_blank">📅 09:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31064">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbI2IUGc_bDN24ld6GsgrqdZBWfmS4zc-C7D5feWHKP1hJ3LyygdhGhDJLArGOBzUqUQQFl_ojaHHRydG7eWz3bbQl5WDTVTzkWxup211OmZk9YMKHFmDT5K_NELl8NeUBkHsv5dPHuUB5AxE6gYBKH0yzA43UUlu-UuFE7tQScjn_0Y6PVN65xSeENiA6UU-ICIHijFqpEjhbhQoUGPEe2eE8nE9G8YxdypRIqVtVRAA9l2m4x1Gm_WVcd7A2eykHzqXyos7qyK4x1uToeGEKB_6we9FenLWJdh3ccS2decwsWvCpgm5wzu-yKluWxPl_oTY94UgTBjyiNeqVEzXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برد چهارگله خروس‌ها مقابل بلژیک و دومین برد ایتالیایی‌ها با مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31064" target="_blank">📅 08:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31063">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUbieAxC65dy7opfyBU9xW_nB068eSCS0s4Uh0dvXOzP9dc6GbWZj0q3_e7EwZyGhPvLA3A9jL_hnu9Q-QM2EbVbQ-6VPRMm_K2tJsRLqUEBABgZaz82wsWxpyZ9LZ9o-ZFI7kfbGCHTdJr2qTYrCCFOaJCurmwl690ickIGHKyT2mu17UYkDXsGenoB_M9GBknTj4pitBfhPo0CxlXXN43WHy8gTy_5rOt50EQ_Egwe4-Zaq42xEELXlak-wA5HItMvRagYTWtdxLan6gFCVi2fVe8TLz_E-TMJqHuSsOYJyxOnu8LSE1YtP376x2BbLhE-KVJk0S1hVYNrQKWPoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31063" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31062">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=EOSIWkzJekJ5IJDNgWhKSShSJlxpqk_XhkDZaF0j1ati2AcG4WRDVhCLy0zebPSNhpXXxv_1GqPOys1CeX9A_VLKkslqJ45rAxFk8L_c_vCouoGceutIonnvAyTHaHpZGF9YYlVdJYVcuMj5l-lrD9hNASYIYkXR6CkiherStf8ClLQob1qPYO76Xqs24H2UoBjVhThqlr8tSh1t9jHe_vrO-CryN02Gby-qPmnbQG2UrpJx6pcmVVK_GJ4V4IYrnFUIqU0e8ZWmWdDuTerK-3rvz2NQcSj9TMlqZmP89BfxDnzS0nyaGckjDPMtSafIXjg4wIbTphAj2SOmuqZuPGi6ACl5zNPQFuW4N2N5BgcByy2gdu93oHvOGLdi7Y4ELWO5SPYy1pNyUcWsgqRAnBB87bvS796wTK-NqovpUHShKBoAz0wXg5kOH3V-Ls0k9UZmZgd3sx_4Ih6BZ-RSqu_KhtUqLNJpdQ0YBHfOgBJY_w5C3enUNDUtgSXMXw5eW8FpZMn00Iqp-rNLkEydOVbkBYQRrsJAZ1PPuO8hm83CzUsFxT96XCukHjApZuRH9U9O2kCOhB0QtWu4rYBMTPYwVTLgcjCugOclRveDOnMGekhBmkZwBiZZQVVofGvqnR4QwyQD_yCnbp9Jmxl9dvbt5bqSYdWlEpuwo0hhcws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=EOSIWkzJekJ5IJDNgWhKSShSJlxpqk_XhkDZaF0j1ati2AcG4WRDVhCLy0zebPSNhpXXxv_1GqPOys1CeX9A_VLKkslqJ45rAxFk8L_c_vCouoGceutIonnvAyTHaHpZGF9YYlVdJYVcuMj5l-lrD9hNASYIYkXR6CkiherStf8ClLQob1qPYO76Xqs24H2UoBjVhThqlr8tSh1t9jHe_vrO-CryN02Gby-qPmnbQG2UrpJx6pcmVVK_GJ4V4IYrnFUIqU0e8ZWmWdDuTerK-3rvz2NQcSj9TMlqZmP89BfxDnzS0nyaGckjDPMtSafIXjg4wIbTphAj2SOmuqZuPGi6ACl5zNPQFuW4N2N5BgcByy2gdu93oHvOGLdi7Y4ELWO5SPYy1pNyUcWsgqRAnBB87bvS796wTK-NqovpUHShKBoAz0wXg5kOH3V-Ls0k9UZmZgd3sx_4Ih6BZ-RSqu_KhtUqLNJpdQ0YBHfOgBJY_w5C3enUNDUtgSXMXw5eW8FpZMn00Iqp-rNLkEydOVbkBYQRrsJAZ1PPuO8hm83CzUsFxT96XCukHjApZuRH9U9O2kCOhB0QtWu4rYBMTPYwVTLgcjCugOclRveDOnMGekhBmkZwBiZZQVVofGvqnR4QwyQD_yCnbp9Jmxl9dvbt5bqSYdWlEpuwo0hhcws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه‌استقلال‌خطاب‌به‌فدراسیون‌فوتبال: شما جام قهرمانی فصل‌گذشته لیگ‌برتر رو به ما بدهید ما خودمون نمادین اون روتقدیم شهدای میناب میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31062" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31061">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=ft0APVoZlXLf9IESMi3tM7nHZlcqaXTGA1BzlO7e7VJvO5BaHxiQ21vct90PnbXU5pqiqJNnChUOVpX2vNYqUcfqbi6gy5LWJf2BsSxPwyim0-xBj-1NIRhlKkIgurdU9cQsC-S8q0WZ2ShAjDp3BojjkwWqp4hBO88YqO5tAuv0yvhDexMK8WvixLYCSBRtVgPKKJYhd94THTzAFs4K2YEoOXdefi80aYIjAYPEzFofox8StJ0yDl8BIKdDvl8hve4Oz_BgnfmtBvrwB6Uivsn67T7tX7qIhuqc_cIYQjlzy-mssBmOoXKIIAmKda_vgDmF9nwIJUKrF8zjA912Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=ft0APVoZlXLf9IESMi3tM7nHZlcqaXTGA1BzlO7e7VJvO5BaHxiQ21vct90PnbXU5pqiqJNnChUOVpX2vNYqUcfqbi6gy5LWJf2BsSxPwyim0-xBj-1NIRhlKkIgurdU9cQsC-S8q0WZ2ShAjDp3BojjkwWqp4hBO88YqO5tAuv0yvhDexMK8WvixLYCSBRtVgPKKJYhd94THTzAFs4K2YEoOXdefi80aYIjAYPEzFofox8StJ0yDl8BIKdDvl8hve4Oz_BgnfmtBvrwB6Uivsn67T7tX7qIhuqc_cIYQjlzy-mssBmOoXKIIAmKda_vgDmF9nwIJUKrF8zjA912Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل برنامه امشب عادل فردوسی پور با برسی اتفاقات اخیر فوتبال ایران برای دوستانی که علاقمند هستند برنامه رو کامل تماشا کنند.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31061" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31059">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsF_IaFcfWyguasKCSZmtoDRkF2d-P1OP49jaKltKL__OtinlkzsBKDtG0EPrhSwCTLwDLghz98MquSWpPpuK-gOGWn98PoX1yw6-so1govOfGG-egIhTE31nemCE3TebPyrn2ZsntTniqhjK6JjDDmoQHnscoa18zRZUcgns13uWTw5vkD_KZ1k5baMNEc6VzAi8FpplvMgatlRXVUKjG-5H3vEu23EC1zLC5l54z3Id1h04EE01j7EqokJr0S02maOnYosnFoHiISoTFmVVAfkmEC-sP_Qa0SDlT5iWhPSOBqLE_RIx-J1rpjGUzEJGtz2M4TO9x25mqv6MoBb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روماریو:
امروزه مد شده به فوتبالیست‌ها میگن بهتره شبِ قبل بازی رابطه جنسی نداشته باشید ولی من باهاش‌موافق‌نیستم. من‌شب قبل بازی با همسرم میخوابیدم، صبح هم که بیدار میشدم دوباره باهاش میخوابیدم، آدم باید تو زمین احساس سبکی کنه. به بازیکنان توصیه میکنم این حرکت رو بزنند معجزهه میکنه. دو راند نیم ساعته قبل هر بازی توصیه منه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31059" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31058">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edc763594.mp4?token=LrdtxAVskKktZC4UMfi0LjiCXRDbzlYfHb5Gv3hFK5z4sdix_ORjvqHUd6P3WE9a0HTl0ajxYHyfJ65wiaP--C6HBJI9sD9wEppl8Z5MnBr2cc44aIMlMM9Gy3UZIbkUqOQr2ji5JykOqi1l8Hie6TqJuMOB7HU-MsWDYYzPo54ekquIH39Hoq3mOhnzWTDp7tGAbHe3bIJ7ry-cG1yXYkovz8-ZNvEl-PusS_jsX-N97hHoPlMhk_k2PnCcEvUB4TNbcxK1tD52Ek7ZCIqSJY1ZpswQdcdmV-VWK-GCAR693f9xd6_tQnelFaj_gyTCTPiDuEiwLYbQ29-cEM06Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edc763594.mp4?token=LrdtxAVskKktZC4UMfi0LjiCXRDbzlYfHb5Gv3hFK5z4sdix_ORjvqHUd6P3WE9a0HTl0ajxYHyfJ65wiaP--C6HBJI9sD9wEppl8Z5MnBr2cc44aIMlMM9Gy3UZIbkUqOQr2ji5JykOqi1l8Hie6TqJuMOB7HU-MsWDYYzPo54ekquIH39Hoq3mOhnzWTDp7tGAbHe3bIJ7ry-cG1yXYkovz8-ZNvEl-PusS_jsX-N97hHoPlMhk_k2PnCcEvUB4TNbcxK1tD52Ek7ZCIqSJY1ZpswQdcdmV-VWK-GCAR693f9xd6_tQnelFaj_gyTCTPiDuEiwLYbQ29-cEM06Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ تیکه های سنگین عادل فردوسی پور به مجریان صداوسیما: توکه‌حامی قلعه نویی بودی. رنگ عوض نکن. حق انتقاد ازش رو نداری دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31058" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31056">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇪🇺
درهفته‌چهارم لیگ ملت‌های اروپا؛ شاگردان زین الدین زیدان باطعم‌کامبک‌مقابل‌بلژیک آتش بازی به پا کردند. ایتالیا هم بادرخشش کالافیوری ترکیه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31056" target="_blank">📅 00:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31055">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIGu_ghFD4Ueiq4oQW4GBRNLN6OhEVlCowLx5FjC12SEW0SUv1vUbyeO-w8gA-BjyUfC2xyl7I7FnWdp9RvJFHEpVCjdmbQnCnejjA3s-cMXu9YeGfy4UFhtNq9GG7EzMCpJ3nO11zSbtfuR_cYtiIoVkLlvio6c85Ls_ilOqP6NCBV4jfRMBIVU4hAwbFtx_4iafDBrnVa_geVimXnBcDKGpfcDyGj94RK63m1snuCk2NPZFzW_oA2tv87GxUheXl7n9wbIS5GlD9w1t5lAO0L944aZSVa3n8CzuhFUOAUpNTD0uQmmCWPASIf5VMwvJ8Z0oFRFXZgS-EZvnhhGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31055" target="_blank">📅 00:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31054">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyJCn9kB-TM5xWgvIRoskL2UloTpOvfb4Hs_Ri0F47Oj461REC2YYYfZ70XArrg0TvBRcWwJ1jS5QF8LhdPCLVnoataMczHfoh2vnGSRg4P-4ySCZcB_x8YpVNkNgjsYOZESgP70wKrd9KRn6JUUnynDswmMpULQjKnrleuYmkZzx10cIRjfhSKZbQ9yPVXTXG1gIvkBYo7MdIQ2jyigSkSdkoL5X_fV1IOn4JUOv_4sUyNbMnLZg5tcnBOq9-eDJgzF4LsO3AKOPmOCyLmrcqvsHJEYguRBgOOCIblGWfkyDDZwEKkY1PURVShS5R4zKGE1_cmvm9-ZQ7oVCmrKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
از کیت عظیم و ۳۰ متری آرژانتین با عبارت «متشکرم ۱۰» در پشت آن به افتخار مسی در میدان شهرزادگاه لئو یعنی‌روساریو قبل‌از آخرین بازی ملی وی رونمایی شد. امشب مسی خدافظی میکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31054" target="_blank">📅 00:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31053">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=aDhPPC25TVuniefcnFVhXw5mJ0tH3_4zr1i7yF7vHwE8ZQK--4PSWxQztFkHFhm5gauLeT4a_mGO9mrsmaJMXY2-yIrww1Xm4mEXePvISr--v1PbyD22g-5rZRJEro8APwVB9R3EPFXimMl1ouPkKA_5hk_5Oo7TrU1puFe9Kksodsqrj6E2SiCzVUWwR52FRibe5i9UK9USbTBVHeq15S33B31eFss8gTKMljq0zNOHEUwVNrIgZrdGvKxizt4aUryFq2_PoeBBoYJK6ZZDooqXp3zwYYv0ILz8TcD1Os0IgJiuFFV3fBRecvF6WCjt5pIwPBzXdnv2ReMZrl55gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=aDhPPC25TVuniefcnFVhXw5mJ0tH3_4zr1i7yF7vHwE8ZQK--4PSWxQztFkHFhm5gauLeT4a_mGO9mrsmaJMXY2-yIrww1Xm4mEXePvISr--v1PbyD22g-5rZRJEro8APwVB9R3EPFXimMl1ouPkKA_5hk_5Oo7TrU1puFe9Kksodsqrj6E2SiCzVUWwR52FRibe5i9UK9USbTBVHeq15S33B31eFss8gTKMljq0zNOHEUwVNrIgZrdGvKxizt4aUryFq2_PoeBBoYJK6ZZDooqXp3zwYYv0ILz8TcD1Os0IgJiuFFV3fBRecvF6WCjt5pIwPBzXdnv2ReMZrl55gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ادامه تیکه‌های سنگین امیر مهدی ژوله به فدراسیون‌فوتبال و کادرفنی تیم‌ملی درباره حاضر نشدن گینه بیسائو برای دیدار دوستانه با تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31053" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31052">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nor_v6qrVRVEQVolMjLvQ2Jlu_zNbCFA7qjMgkiih-KEHUxrde62P28mY5Pux4jaj6BELtDLwlTIs2IHizRLsY_Z0y_u66U5P8BAFqLx5UmzJKhKN5HrF7vPX94AyGI78BM6AE9PRwkspxJebg-oEhPaTsO0KXdStPJEe7wyVu-r4PyMk3-V3RIq1fNwWic7yGpnbNBFkzZ-6SeefNeOvXvHSOLyzsijuSq5EFjWSIC0aFPqMN7vPGZ4lzD8DPXv_x7tzTYWO4CtfRnJqKx-AltMC7nHhHjZaSxRuVydswIgfc_27GVGzm2gOOnAgRn6svUhNdfzvS9pSTHPlU16cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31052" target="_blank">📅 23:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31051">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzYM_nGty_9ZSaMKXf0WhY42EgKXzuVHlGJW6Q2Xd2bO49LvaeMj_k8naJISBmBMAw7sgt_UuZGEQ5E_ltss6oWyG6qQVfB3KH2Z67OlZpV5XAzMCUE2mrbfDcbl_kncZH8ogQhTAQNHhhQMjp8Ff2Fqo2MP9PYjKx5AjtmGGN4PMRPQTbhWmaKyrkLNUdz2HkDUkF7LvipokZ4C5T5iZIr69jgpu6_b5SgaUqARfSrvVwvKQXst3zV8RMgSyxTUwwGsujjwQt7N_UxOA8l8oTrg6KhTtDVslCvFT9g4ZjthWnTMPgSNCtl0n-uAgYk16-MSEjwALYSr7-WfksjSOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31051" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=loJLGEkvemttRikPmwYT3rzFnaTp-tei90ERc7lb0TbUDQouOc_V5dr0TRDaEA-VW_hNLCK6kixI3QNkevZXqvszbETTbpPbe2DMc8NBL4zmHA1A9RTydc9McNKvZc_ytlHt0gcXMnggP3BvJUaAVVSpllzeXJJv-QYEWJiy_FlmRL4rQZj0kvZ8a66zQ1sJyRMb19m6kLxuLphrMCm1glwo7VTYV212wz67XRcrtjiLdMSfSO4UFV3BvSm2HM_bJEystpYOnItdalJZbroC1iATCuPriOwGf_TSyGiPCHgkL9U2k9_v0M0YKzibMV-d2UARXazAoQh3HWpwH4hyiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=loJLGEkvemttRikPmwYT3rzFnaTp-tei90ERc7lb0TbUDQouOc_V5dr0TRDaEA-VW_hNLCK6kixI3QNkevZXqvszbETTbpPbe2DMc8NBL4zmHA1A9RTydc9McNKvZc_ytlHt0gcXMnggP3BvJUaAVVSpllzeXJJv-QYEWJiy_FlmRL4rQZj0kvZ8a66zQ1sJyRMb19m6kLxuLphrMCm1glwo7VTYV212wz67XRcrtjiLdMSfSO4UFV3BvSm2HM_bJEystpYOnItdalJZbroC1iATCuPriOwGf_TSyGiPCHgkL9U2k9_v0M0YKzibMV-d2UARXazAoQh3HWpwH4hyiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری جالب عادل فردوسی از تعویض عحیب تیم ملی در بازی دوستانه مقابل تیم ملی روسیه: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبوده گفته خودت رو بزن به مصدومیت تا تعویضت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/31050" target="_blank">📅 23:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtfFqvqT3PZYq5UUuc8lk8ZvYedftOnUjuBp9XTDRFLu3zrekp0bGJy3bdLAi98sTtc886FrfRNF5rOHGYQ82AXlMEW0BBhCWChTOImAKFu2Swb3WvmwOwCnmfpSJb-ZZKoE1uZQDrq6ZOnaQyGCLfwBvevJrL1o1osCQO29UVOjVsU-PQCrPq7zd4teUmCJ2RiVttPPhlnutmGqhJeHFxb1iZnDIGg7si4GIWtc67M4OstpKAaD4clJaFOevdOoKEBXheGmVzH8c56Vd3OW0NEgcUndColeEAtAjzUutatxrt9Iyf1w1CadFfNByZem42MNqfCJuTlafAY7AnZ2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سکانسی جنجالی و جنسی از فیلم جدید دوس دختر کیلیان امباپه که سروصدای زیادی به پا کرده. کانال دومم داشته باشید کاملش رو اونجا میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31049" target="_blank">📅 23:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=Q8kVz0KfdUOb8MD835BnVJAOnK0dl7DQbiryqJs3oCLmCPe4UfsXWs55Sb9RWiwDLTrmrqE4W4GysgMfRNlJvAmGRU8hKbZPCVwQCVKAl44fRUH1oSQR-4u7gWWe1Xbb77XwR8ce9HDpnZSqhgcl7dp3snBwDIShjnOFOHl6tto0Oxq1VyeSGJNbLtFjOPiUdASAHZquUCZQKUj8Qbv2dfCL3PAbKzXM8HC66bONbeI8sVvwFxWvTO43yeHlAX5K2f5v2yeLTLoLc1iOyLcQWHfQD1zeyCisVKdJ77963F7FBuWnDsE-FOyZ4ojL18wawXpWXs-9CgqFD3FcX40hfRYXPZkWLZVkUxWi02_PH1SplVPeAdMk66ZJlGuBAmRGiGpVqp1Ln8J4LLCAQ2aH8YHgv75EzNJmEVAoD3d6JO64PQwE24MR2qPwU_ZBxRO3nqcMO0So47SzDKcaHsBnlgdbQ4erlkQqyY6e5b5b00wDgZdPs9Q554ISnjz8cYYjDkDg68aljD37nPygjBwWFZodS3h7e74s8cqTPXKGmSUbytzoFvPQcx328L9HAge-04xuDFyj9By6qwxlUL_y2HMCJTI6uaIjwE_hjpxrAKJhpwT-7xAJNIr9Ivg4IHcQPdW8ahP_4tOEL_mgmMHToCefqNq_b9OaDtEuozyefkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=Q8kVz0KfdUOb8MD835BnVJAOnK0dl7DQbiryqJs3oCLmCPe4UfsXWs55Sb9RWiwDLTrmrqE4W4GysgMfRNlJvAmGRU8hKbZPCVwQCVKAl44fRUH1oSQR-4u7gWWe1Xbb77XwR8ce9HDpnZSqhgcl7dp3snBwDIShjnOFOHl6tto0Oxq1VyeSGJNbLtFjOPiUdASAHZquUCZQKUj8Qbv2dfCL3PAbKzXM8HC66bONbeI8sVvwFxWvTO43yeHlAX5K2f5v2yeLTLoLc1iOyLcQWHfQD1zeyCisVKdJ77963F7FBuWnDsE-FOyZ4ojL18wawXpWXs-9CgqFD3FcX40hfRYXPZkWLZVkUxWi02_PH1SplVPeAdMk66ZJlGuBAmRGiGpVqp1Ln8J4LLCAQ2aH8YHgv75EzNJmEVAoD3d6JO64PQwE24MR2qPwU_ZBxRO3nqcMO0So47SzDKcaHsBnlgdbQ4erlkQqyY6e5b5b00wDgZdPs9Q554ISnjz8cYYjDkDg68aljD37nPygjBwWFZodS3h7e74s8cqTPXKGmSUbytzoFvPQcx328L9HAge-04xuDFyj9By6qwxlUL_y2HMCJTI6uaIjwE_hjpxrAKJhpwT-7xAJNIr9Ivg4IHcQPdW8ahP_4tOEL_mgmMHToCefqNq_b9OaDtEuozyefkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل در مورد بالا رفتن سرسام آور و تلخ قیمت دلار از آغاز هفته اول لیگ برتر تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/31048" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=MbBUbgMFXkKsshPgBkwMNwrNQjrrvIgSYJealMLUTHk6FBGzyiQP_MtOctFsZLYx5-3py-FAcJyOicL_1wsmi-g3b1D-6nOdE6eGeaAux1pcJ656qXFwJ6GsJeQsCSJ3xl8mJ0QLIg2jm-xZ3C03GU-PxNfmCbWRv12WvJI2IeWBj9mhL5ZNDeLIgX6P8oL2mUDzgsiZVJU9k5jshj_la8uCJXiDcwsyFvyR6HTSSKqX8ikLi8z1i2AwYuJN06sixR9luk2RC_EdsagDpYNbTWW0jpH-Nb5Rqq6ICvvH03sPc6EWRoHLXn-ZLX018t2vO5dyUeoH8kipc2GTRSNnvC9YFzNIfFGm_We482zp3nqMTsr23rd6mgNpgzhCLL7vCHpnUieCNrYqTYMDlh-nO23sXGi_IjrRqvxublGG2f2ECihZUTqe-x4U1iS2N2DkK9fudzx5YAnnvoTnESeSlJAM7pipiFpXQl9js4BrFl3Y86T4mRk1oH2yEY0X-dE4JHmmh9eR9p107wgTSH-P2YxbIPBroU7QT-ndItAVfudgPsKlzf4sI-Y_GeHFux3ANC81aah3Tf-czeEnDLl_LKLvqUv7AvAhl3M2dbQAHVjK8fXo1BQOTCwBKCUnLX0Qiz7sbh_23wy88uCqsQEtrITU-W5heXBeRtmu5udb8mE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=MbBUbgMFXkKsshPgBkwMNwrNQjrrvIgSYJealMLUTHk6FBGzyiQP_MtOctFsZLYx5-3py-FAcJyOicL_1wsmi-g3b1D-6nOdE6eGeaAux1pcJ656qXFwJ6GsJeQsCSJ3xl8mJ0QLIg2jm-xZ3C03GU-PxNfmCbWRv12WvJI2IeWBj9mhL5ZNDeLIgX6P8oL2mUDzgsiZVJU9k5jshj_la8uCJXiDcwsyFvyR6HTSSKqX8ikLi8z1i2AwYuJN06sixR9luk2RC_EdsagDpYNbTWW0jpH-Nb5Rqq6ICvvH03sPc6EWRoHLXn-ZLX018t2vO5dyUeoH8kipc2GTRSNnvC9YFzNIfFGm_We482zp3nqMTsr23rd6mgNpgzhCLL7vCHpnUieCNrYqTYMDlh-nO23sXGi_IjrRqvxublGG2f2ECihZUTqe-x4U1iS2N2DkK9fudzx5YAnnvoTnESeSlJAM7pipiFpXQl9js4BrFl3Y86T4mRk1oH2yEY0X-dE4JHmmh9eR9p107wgTSH-P2YxbIPBroU7QT-ndItAVfudgPsKlzf4sI-Y_GeHFux3ANC81aah3Tf-czeEnDLl_LKLvqUv7AvAhl3M2dbQAHVjK8fXo1BQOTCwBKCUnLX0Qiz7sbh_23wy88uCqsQEtrITU-W5heXBeRtmu5udb8mE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فلش بک بزنیم؛
به وقتی دوست‌دخترِ کالافیوری اونو درحال‌مصاحبه با یه زن دید احساس خطر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31047" target="_blank">📅 22:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRv1uhCQe5rbnGE7LSQUtg0fhHywwalGGXApFB4spHTNzCDHLQDuGhQm93Jl2D-v-6xjkvpfIiza90MrdYsgTp9yPW8A9j5BEXCTu6cwKLe5hRB3aAyqtnWk-3mpjKNl22tC_z6kNEunBvSUnl-bO27HVZ-KLZ9PvEuVbrDnNvEKyDYJW597mXI08X9iq6wf0Kisf3xM4M-6tC8vBECvVBqs67RRRk2jjR_SL1iLiY4EgLaiDI3J0Lwj-r7LOpfNdQdS73uWIB8Zuy6MK4FZXyDHrrQ36xS7OKo2jojLa3oSh6mhRR2n0mz_soh69sZ2Cvi2t4p7FDQ34GHZdn7ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر امنیت داریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/31046" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=MeWMhXZ_d8M3wgxm4Z60oRzDjNf7mhLBz-ViFXZbRj7GJ9THKH_aEkLmgYqL1QaBs0H3IW8rpVfvopTepxgLb4I8L9GaYGT7_PDmgZaIgY1Sl4ePg5BhwgYLBumqcJdw4fC15bNKT7RlqHKSrCKgzLs7er2u6S4LRYM5lm4G7M1Qt9mUNV-7_5_jdqB7z2xTKWwOOTZOEedHU-W9zRUgJuCeQM4LQ7CTxp2m8J4XOL5by2p2djJAylIqQ-ZxQXR8u-v-B00HisL4Ae8J43OPFR2Jd71Ef7CKffSJeApTzsVprnLFtI3rB7dPunSw4Umf_cGVMm5I5w-gaQUlQbp2Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=MeWMhXZ_d8M3wgxm4Z60oRzDjNf7mhLBz-ViFXZbRj7GJ9THKH_aEkLmgYqL1QaBs0H3IW8rpVfvopTepxgLb4I8L9GaYGT7_PDmgZaIgY1Sl4ePg5BhwgYLBumqcJdw4fC15bNKT7RlqHKSrCKgzLs7er2u6S4LRYM5lm4G7M1Qt9mUNV-7_5_jdqB7z2xTKWwOOTZOEedHU-W9zRUgJuCeQM4LQ7CTxp2m8J4XOL5by2p2djJAylIqQ-ZxQXR8u-v-B00HisL4Ae8J43OPFR2Jd71Ef7CKffSJeApTzsVprnLFtI3rB7dPunSw4Umf_cGVMm5I5w-gaQUlQbp2Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین ژوله به امیر قلعه‌نویی: من یکی دیگه فرصتی به تو نمیدم. در طول این چند سالی که سرمربی بودی میدونی چقدر خون‌ها ریخته شد؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31045" target="_blank">📅 21:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31044">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfRpgx1peHhEOUL0YMTyYB19ZDhLFUTblSCy0vfERZwcnExJfUs8qK-8w7ydumU_gYpsNKp2JCarme7B4xyF0wzHkx67xroRqNpvJ7FLd1zRM6UWQLK9vgvRl_KWPtIRjNWUDd2P5jQg2rSa7_XAsRWxEtr_7n7oFhQUZAedWcrZOGodA97NnrrcBKjMq2R9cKWtrWiwwcPLAiqte_KZnFgWNaHe_9UsjijNU0CjZmBxJD8Vcfwc_JyFh1eVAB76cxyP8fvKsEUPXtz9sAtf8RkHU8ynPEi9MEhR3YpbWVoc8jDpvMgjMCHsU99waQEMn_4DX_rPhd2jRo7ZY2EMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مدیر ورزشی النصر عربستان: با کریستیانو رونالدو برای‌قطع‌همکاری‌به‌توافق رسیده‌ایم و ایشون درپنجره نیم فصل از تیم ما جدا خواهد شد. مقصد بعدی فوق ستاره پرتغال فوتبال اروپا خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31044" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31043" target="_blank">📅 20:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNGXCnPfyzr3ydRAa7uXgYVfByhvkZmQoDHQvz1SnyEvTBaNHfFi3K_6SOgJOoFAK8d_58wLDrX_mfClpbgDnB3qNB-V626f-fzV6MpkE8Byzx3MpQBpyesijv_b7EAUpUHQpZX6nHxO_fdxSu2nZEjsWZuSmMvAXP8g0Qc6ZaJMfUdQ2cGzZobYgDw3dunf7NnCe4PH4Rb99r-lp-NTxur9IsIa6ESeju-qySO96hDpE97q3aWEuxIZmaP7PwVphEUZVf9uVlXLhjFF6QxMurRdpRhBPID3tmMx6ltHKGUanUP1enbJaBI1i18ze0IEkieGl_CV47BcP8qy_pCEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان پنج لیگ معتبر اروپایی تا این جای فصل؛ رافینیا دیاز فوق ستاره بارسا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31042" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh6qZic_xpxUe41QufUeDrfLFtMwAZKRQWpe-TUbWmAwmK9rRW5BSuq6lisIJxSQe0p3i8U0LIP2oi-K3ciUan0MurKWi_bTB4DGiI9GdOB5skfJpZcIE4vEVnI_c577m6KD1YdDNdDbQ1XnsMbcSg1xQkO6lx7CqlImV_JZWVd-BwA2r57ffbJkRM1npGHr6W8DaIGiLAevjHr18fsB5bV9gKSpvUEUpJ5DzbOw8MXB6hhmppkFOqz0uYdCpc3nQnlY5PFR5iCXP1NSXwiujMLuaiK8BK4NbTEdI1eK_H-VaWOVcoOzX-CNBetEfg0HYuQ1WDLfVJdjmJIlXC4BjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیر‌ه‌کننده و درخشان جودبلینگهام ستاره 23 ساله انگلیس در سه بازی اخیرش برای این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31041" target="_blank">📅 20:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31039">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=a_7wOrymEdPZATBWgDSZ9FeRBhmpOtiQABevy7ydiqaEp9cPx0kdxJv-xtGt18pQF7LTIH_Lv78G_q3AEP7YxAAQcs9D1H4by2nGnEyaIiaSzL4l8Uym8cCmTSWGLPJaEQli4IRWMgoq_zuCgwB5lCbenKe5HqgZd8cUTu184SgnHbRrXsN1v29H2SPTNYPM_zaYlpEdxoLdm9-g--t37Tb2_dvLKVvL9Fv8hvIoOAwndMyB7S8BqjgxMMRPEEZASlELCa2Kk1q5J3eVPsmMaSh3M6x21EDZAqbv3aXqvg1a2pFzN58uh7-oxAOH3D3jYh0xG66LlCmY3ivVGOu1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=a_7wOrymEdPZATBWgDSZ9FeRBhmpOtiQABevy7ydiqaEp9cPx0kdxJv-xtGt18pQF7LTIH_Lv78G_q3AEP7YxAAQcs9D1H4by2nGnEyaIiaSzL4l8Uym8cCmTSWGLPJaEQli4IRWMgoq_zuCgwB5lCbenKe5HqgZd8cUTu184SgnHbRrXsN1v29H2SPTNYPM_zaYlpEdxoLdm9-g--t37Tb2_dvLKVvL9Fv8hvIoOAwndMyB7S8BqjgxMMRPEEZASlELCa2Kk1q5J3eVPsmMaSh3M6x21EDZAqbv3aXqvg1a2pFzN58uh7-oxAOH3D3jYh0xG66LlCmY3ivVGOu1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31039" target="_blank">📅 20:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31038">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKC5Rz3SCGoYH7y8yuQ4uqjsypolR1eC-Uno6AEfn52nRrqC2Y6STlToK3zl7KWnS6ZqtCYA741OpHpM0sq7mYv-e9_vtAFC5UEolL8Pxh4N8FxlrWYNwD8djFFd0xaFsdAC1cHF9ac54KIYgMv_zxtdNkNMoJFfzLJUhoZpOfHWcUsGlcx59CEadE1SxYqv9VCv-f6VheJ045XA0G2C1CXXfH6C19wqYa3PdQ992qWELrfBRpOOIXtaF2-GtT5Ow7kZvoesJFGE-VC6RSgMwuN_BGEfIrGs7QaOr3dIgSNGTTN0SLxgUEsbqHmfAgM61K0b-5y5STdj_ROJcZA1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31038" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
