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
<img src="https://cdn4.telesco.pe/file/s_eoxiJp--qJNHzDngtVVa_VYLSaiLtqTANDTTZTaIf269bt4pxV7aGtUkGLbYu0TOZwtcQ1yuSCvJewufIp9GogdzjABTC1QYUKbdhmSVWkvJbfcddKl5NDzhpK-NeVZBsvxwqnKASvCS1jLeXLuuxoddxiolPwd-090JhKQLm6-l64OvsqqOwQlGfyG0GguuPP_muoHf-xeVVMXnaNjY2Mq8zqrdNkrJHiYBPHKQmGut3qkFXsw6vKHNh7mNGMjcfJwZBRHiZyxBaFRFJsueYYo4kt1c6cSIu14QONwkU8BQizeszEmXeD-NyxyAXGV5S6WS5Uf-22TbdCmXiF4w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 03:11:38</div>
<hr>

<div class="tg-post" id="msg-79439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/naya_foriraq/79439" target="_blank">📅 01:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
وزير داخلية إقليم كوردستان العراق:
أربيل وبغداد اتفقتا على توفير ضمانات أمنية لحقول النفط بهدف استئناف الإنتاج والتصدير، استجابةً لمطالب الشركات بعد الهجمات التي استهدفت الحقول مؤخراً.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/79438" target="_blank">📅 00:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLQbIjj57M9NuRCoPUcOk7RnT2ZGH3ZUI9uw6y5UdQX1f4J4iaCsPyEMCzLnmiUL2Bf4k_DSYcvlu9LotIqrEDwqpddgCcGQj98QNFcrk6925odLMCgeNeFhR9GYn5veFvBjsig5IjzSBD7aaUmOr_lp0xkI1Xwkqu_wa3m4FOi2cizFLugtItD-3o3iLXP27aeR6fM6k8413Vrb060DtiBRKQO_nNfG6_lrd3NacCZK-brCHMjnjMu7AoPWJcsqsIRLTh68rDUwgtCObj25QElbX02Qd7kmx6--huDHc1xSlIfRT0Kxjl-vrLJpzpg9IzmJE9z59IUNWnY1QMvptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وصول الوفد الايراني المسمى ميناب الى سويسرا</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79437" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9HrE8eGACe_z3mTJAExQWy_n9VfdFvlm-39G7YS3QT0aSzoS3A-zLmLw_2Irkx8Y7hp5XDRQLUcRElzSWtU7W7Kbq5275rNmOnpKgp3JLA1ijFNw6OQXd9_maAyc5Q9XeLlJCvztQwgHhHZpmv1Vy-_Pe8ROA5u9tU3cDk5PEINTrDweHXIzyE8IhbQJj3ENturgPQxCak9yHgj7IkFtA1xd2FX1eQ-seNeF3f48N-657Nzv69J0-3D8S4BDaKXhkItm8XaYz06ZmRU86oG0NW4iSNyQO3yo6KYX7qGTe4yZnVfIMiSicmh671qt_tHpMXguNgmCSJQUiIm9UqkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79436" target="_blank">📅 00:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b774e6bfe5.mp4?token=lVH8qaKwn9Qy4MWVDGNPq9JtZLLrcUowwasrOw2F_w2O995cbsRrPsn-cQAROPH8uxphA2U2aRyCcXqLMCLHXJ69XUhH5_MwendWZfSgxoelBn8cpK63hkmoWlTPlyU2Or2B-XLgaJwrKfKEE4LWTpI8Q0wpi3N04aHMaFhJnrfb0B8GV2MHKzcBI46PAMxC7_5zsD-ChgAiq78bDAMc09Nm1mMTSC7DlOFHeyVeRtmiKvI6YLQlsPyO9mUo5Uio5lp7IvJeeDqX6ymRzJteVH8kW43QVlCi2LB3Tr4Ep1wc6fzK0ifZtHM2TxxSZNO-5us7GxplPxa-aXE9JPortw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b774e6bfe5.mp4?token=lVH8qaKwn9Qy4MWVDGNPq9JtZLLrcUowwasrOw2F_w2O995cbsRrPsn-cQAROPH8uxphA2U2aRyCcXqLMCLHXJ69XUhH5_MwendWZfSgxoelBn8cpK63hkmoWlTPlyU2Or2B-XLgaJwrKfKEE4LWTpI8Q0wpi3N04aHMaFhJnrfb0B8GV2MHKzcBI46PAMxC7_5zsD-ChgAiq78bDAMc09Nm1mMTSC7DlOFHeyVeRtmiKvI6YLQlsPyO9mUo5Uio5lp7IvJeeDqX6ymRzJteVH8kW43QVlCi2LB3Tr4Ep1wc6fzK0ifZtHM2TxxSZNO-5us7GxplPxa-aXE9JPortw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وصول الوفد الايراني المسمى ميناب الى سويسرا</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79435" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d0f703ef.mp4?token=teElIwkIAK3b-GtRyjscthYBif18m6-k8Ew4ZyCORy6lKkIUHkeTYqJNRRyX95iVUNncjEE5hGqjZ-jQkqpNfDBueOT00wjhkKvF06DRvPAYYWPIbwPtNng8UjFWsrC2-82nA-xk6NLO0NRFLLsxvSIIHZ8-F9hhQzCK4SW-qsMfDKTP61HN361R4_FC7m9PkSKTS-t8BXvOUWAK8PRVrmSkojz25ecLTge2ZXNwhbCqf8yTRhoA61R0CHeDvMcaBX063f-c8JSo6IyemfIYD4AiUMi8XDrYYSFHmqGRbMJWEvYhXpVpjFR0eBGDIqWzNI74MM2z2r0FM-3l0xw9JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d0f703ef.mp4?token=teElIwkIAK3b-GtRyjscthYBif18m6-k8Ew4ZyCORy6lKkIUHkeTYqJNRRyX95iVUNncjEE5hGqjZ-jQkqpNfDBueOT00wjhkKvF06DRvPAYYWPIbwPtNng8UjFWsrC2-82nA-xk6NLO0NRFLLsxvSIIHZ8-F9hhQzCK4SW-qsMfDKTP61HN361R4_FC7m9PkSKTS-t8BXvOUWAK8PRVrmSkojz25ecLTge2ZXNwhbCqf8yTRhoA61R0CHeDvMcaBX063f-c8JSo6IyemfIYD4AiUMi8XDrYYSFHmqGRbMJWEvYhXpVpjFR0eBGDIqWzNI74MM2z2r0FM-3l0xw9JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
فانس يغادر واشنطن متوجهاً إلى سويسرا</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79434" target="_blank">📅 00:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌟
مجلس الوزراء يقرر تعطيل الدوام الرسمي في  الوزارات والمؤسسات الحكومية كافة، يوم الخميس الموافق 25 حزيران الجاري، تزامنًا مع إحياء العاشر من محرم الحرام، ذكرى استشهاد الإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79433" target="_blank">📅 23:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
تعطيل دوام الرسمي ليومي الاربعاء والخميس في محافظة البصرة جنوبي العراق</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79432" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تحليل نايا...تلة علي الطاهر.. لماذا تسعى إسرائيل للسيطرة عليها رغم الخسائر؟  تُعد تلة علي الطاهر من أبرز المرتفعات الاستراتيجية في قضاء النبطية جنوبي لبنان إذ يبلغ ارتفاعها نحو 700 متر فوق سطح البحر ما يمنحها إشرافًا واسعًا على عدد من البلدات أبرزها مدينة…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79431" target="_blank">📅 23:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETCpjeBNprNLxYlmI3jM6NQ2eFpw5aKIvB9o1YxheG869kuWIZEwhI911RIxjQZD_-vK3SXftR0wuJXpgCqkGAs1xi3_MaHRVYDxgSwEEfpaQdtMEALDruUsrYuKiNWAaTPhqQwoIYfTfJeHO3b_cAUUPO-TfumfW_5h1DWXIUIDqY-EhfbGC1jC5fUqpSdcU9lzpSw9Ov5oPFlUSqwUVON5B7UXA6hTliSDwGmjOeSCsIHxhKTZyy7Jbyrq6HDNP61CLuYBle5f1FOasJJdq_NRDtvBMPSzx_8lAAwPw2MWzu4ay5s3UpZAryWKVxXOEQFpxzdaIVu662E-QMEeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الصحافة الإيرانية من اجل لبنان اغلقنا هرمز .</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79430" target="_blank">📅 23:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIXampKgeatHH4_HPlRxDbrK7qepOwpde8ir4_xABlPGkAOPjoRdrSBjk-HR-IvSU1ge24ZsFGrLgDmlgYfJXz4X7_JZo_QRvhW5DFCsZSuiHZk0Kx74tpqdMWE6NPeFW-XsRlWiCqNY4pMA6UAuXValenyeMvitR9zovtbQ1WikXI0yaprpogNxKMwmCgFIXqUB7T3erx67fvzJNqTh6V6xP5SVSaZ5ferj661C9GP8Lks-5wRV2QSL6y5qKS58EFMknOcKyf0DclONXwOz4tvQzM1ZOhFFL5rkIr0K1dftc4tG3ntrS6pWAf0zWVo6bbhV3fvcC6tAKK1go9lnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب
: يجب أن تفرض الولايات المتحدة رسوم المرور على مضيق هرمز ولصالحها.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79429" target="_blank">📅 22:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79426">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_syNEPDH2y7Ka5zIeJh9wfC4M998ZqmfeF04NUNl8KyS3vCP4cVT-6xpCrd6Kj6YR9bHAC4Tswatz1hzWy53CHYWuofxajdepUfRRb6svTtLtK10wBfqSzK6LT13SabFhPMPFuvRz6P3efOvRBhDWhpRPHxeoP7SNA8kcl8Eobc2pb4X-pF9vRdWWBommwHL4W94PyLmDjL9rTzgKqXuMm5SBPFW2WgWQ1on586wiMdqeDrIKlPX7I3g3wt-v-oUSDtRFxFL98Z1_Zp5v3lQHqTA0efkbkA7Gb3V6K7TzzLXqb6-9bvTTadsAepyqDFrVvWvFW__YLmisJtgftErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajztNUnKcpqeElPw6_ttgy51RUjZgo9fzF1dZsTjQltlqBkixcSrxPJAJAnjeZjIh5jmBCuB1kWk9YEDErf8izPtFJb0J2-8GSLVd2ff6EaN9O9XNvThvmUGI2onqNx8KbuiO4nRmMCP-TachBQzcqJJqH7VluKUcywadZt5K6V2Tljp2JjIq9Yih4bJgxpDx4BRD7oZIsm1XZ-TwFjbV5yNJXdo0ZCiW7T_V_6iBxDTLCEUC5shh9BIY1O5OmG6SVuPr1ogUARkrroLrXS8eTDm0H_RDulZg_d25h3wWDGpe5dhbPmXtZWhb1GuZrmw_ftuNYl4RIyzfAbG6GKuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBdL5mhG7StfICFWE7DsmCmXdYWdaje6c3LCkw9IL0VNC4V185rc6dy985OEZZX6urBvBMlCwUeoMumny847AyuruIo5gBcvsrI6-ooXMSQQdkpWx4H-eXhzddmCk06z_4nyZ704piHoaeokeiQtDC3VOmAHTb2-6TUl1rSnm9qt4IqOv-STEFQ4HZeWGy0jkKw_QLydzTSIT9WlRczwKvjHidKs-L2pwbaV6CTSS14-Ijb4Omin57y0jmDq75T2c7FywHYL6FPzAsL5zOusI7swqQ6SDl6Kue9FzRE9cs4pqG0Xmxz8EurHRFD3xtan6l08zfLPcQLnTmlntw0eQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
إشتعال النيران بالقرب من قصر الحلبوسي في قضاء الكرمة غربي العراق جراء هجوم بطائرة مسيرة مجهولة العائدية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79426" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79425">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يسمح بنشر إسم أحد الجنود القتلى في جنوب لبنان وهو "دور بن سمحون"قائد كتيبة 52 ونائب قائد الكتيبة ، بينما لم ينشر أسماء الثلاثة الآخرين حتى الآن.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79425" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79424">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭐️
إشتعال النيران بالقرب من قصر الحلبوسي في قضاء الكرمة غربي العراق جراء هجوم بطائرة مسيرة مجهولة العائدية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79424" target="_blank">📅 21:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79423">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
حزب الله:
لَن نَخشاكُم ولَن ننكَسِر... قطعًا إنّا غدًا ننتصِر.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79423" target="_blank">📅 21:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79422">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79422" target="_blank">📅 21:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79421">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79421" target="_blank">📅 21:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQEXLpy9XoynKDncRG4c3qTXIOXUUieUTD22KhqurR5hEg2GqmIZXInJC7LA3y9Knwy_OMMHsilbmKilBl8_tn8RIvzyBkNUFt40ZubSFARbKBDSeKbPbn4CCrwDF-0UIK0ZqrDABaYlUIraZzTzcJ3RGo07vDRMKUL4Lhc3u8EvAwsRwoygh93_Z0AuciVmkMCCeydcKw1nwUpiLIso_gEDMk-3_v3VpvhBsVcIulgSqIrKxwDt5s7IoVtvFti5rU51awJ4L79-RxlijY5G0yVeGnWVHm-7Fx4ZNhMYc9OleBvQ5jWc0M5VH5LTVB5xzc1iPWbjiq1drSaX3av97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله..
جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79420" target="_blank">📅 21:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة كربلاء المقدسة تعلن تعطيل الدوام الرسمي يوم الخميس المقبل الموافق التاسع من محرم الحرام.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79419" target="_blank">📅 20:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f02dc4e97.mp4?token=GApenTUyLjPSFjgxTXiUImL_iiTVjeAAGCxMyUxZ-lCawcn9GtpGYgooaOaUaEsWQ2qtmg7GFKJy8c-7A7C4c0VAtVZqcjWCn4hABKQ7LONRFFMAisiRi-M4aXIyGhE5UT6M9ZGq_8zCpV938ROnfYs5rxwXKm2PUssdPsh2r8pgGVDHQ5aK5Bbh8qi4-3ws3xkNHhQ8fYEn6YWT__PaWnPnt0Ie16nOfIXQjk9hAcnAuhsRFIGXP3VhztItkSxu5of48DVMlPczN4eiFPEXft85LEZGnjneX93hcIrXh11Y0IE2clmfFBCIlhIEtbAk-Hjv9n380eWYtLxMxsv9tE2e5WzZraTvLPGTyZ2QmH_CDRp0klHmfOH-3KlGkdVS2ecVe0BcB_5AzVZWALFCCunMzyoe7i2qhqFmTFQxrPok-6Tn5hvONBZ9xOgJgB-dWTkv4d-Hx-pPIvuJ3KlU8SoxFeE7nFMe_mOlftcEY5I__O-CrXtCNgzPoEOl0vXr4JCU-scMYLKDk8oIbFykn0JlyAm9j1EMpjyBMQ6n_1rbfBlcyOLTzmUFhSgfXJ__MRY8zKr5BUmIDpcGkjPRJEPM7-XkWZOLefCKEGbADpU6TeZ-9s0LIqeF5bF5XzowBeI0H8z3Mv9D-XWaf0dqpHezmtuwniEcTl_L6argqII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f02dc4e97.mp4?token=GApenTUyLjPSFjgxTXiUImL_iiTVjeAAGCxMyUxZ-lCawcn9GtpGYgooaOaUaEsWQ2qtmg7GFKJy8c-7A7C4c0VAtVZqcjWCn4hABKQ7LONRFFMAisiRi-M4aXIyGhE5UT6M9ZGq_8zCpV938ROnfYs5rxwXKm2PUssdPsh2r8pgGVDHQ5aK5Bbh8qi4-3ws3xkNHhQ8fYEn6YWT__PaWnPnt0Ie16nOfIXQjk9hAcnAuhsRFIGXP3VhztItkSxu5of48DVMlPczN4eiFPEXft85LEZGnjneX93hcIrXh11Y0IE2clmfFBCIlhIEtbAk-Hjv9n380eWYtLxMxsv9tE2e5WzZraTvLPGTyZ2QmH_CDRp0klHmfOH-3KlGkdVS2ecVe0BcB_5AzVZWALFCCunMzyoe7i2qhqFmTFQxrPok-6Tn5hvONBZ9xOgJgB-dWTkv4d-Hx-pPIvuJ3KlU8SoxFeE7nFMe_mOlftcEY5I__O-CrXtCNgzPoEOl0vXr4JCU-scMYLKDk8oIbFykn0JlyAm9j1EMpjyBMQ6n_1rbfBlcyOLTzmUFhSgfXJ__MRY8zKr5BUmIDpcGkjPRJEPM7-XkWZOLefCKEGbADpU6TeZ-9s0LIqeF5bF5XzowBeI0H8z3Mv9D-XWaf0dqpHezmtuwniEcTl_L6argqII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
جرافة (D9) تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة
#أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79418" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭐️
بلومبرغ:
‏قال الرئيس دونالد ترامب إن احتمال انهيار الاقتصاد العالمي كان سبباً رئيسياً لتوقيعه اتفاق سلام مؤقت مع إيران. ويكشف هذا الاعتراف عن نقطة ضعف رئيسية للولايات المتحدة قبيل الجولة المقبلة من المحادثات مع طهران.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79417" target="_blank">📅 20:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e205a6fd.mp4?token=lTEkRngXAjTVIzzOoaDwUmm3f7Y8I61Vamv4--L2T8lk_bq2EdI5oNzZORYI4Za0RZi-VQq1AhaNjYrb3lg22DA0qw6ZEmd7xI2dDeEPesSo_k_1OAN24zG8h_to42k4vcz1tmf9SespPJbeuEkZ-9bsJZncaWMuqIfFO0mcaVNPN263nbL3eTzYUF2AQlQICGv3n348_bTUbe2cM2llnH2-tPsXdgrTIDnjsH7GYa69DKO2KgZ70S5NSqlvV2Ex26u5O--c_zFalJm0FajHqhNZ8VvIS5pecw_1Sc0p2WgGw8E9yAh90AQvKLcd22gJW2wXyBKQlhWfUohO8VHqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e205a6fd.mp4?token=lTEkRngXAjTVIzzOoaDwUmm3f7Y8I61Vamv4--L2T8lk_bq2EdI5oNzZORYI4Za0RZi-VQq1AhaNjYrb3lg22DA0qw6ZEmd7xI2dDeEPesSo_k_1OAN24zG8h_to42k4vcz1tmf9SespPJbeuEkZ-9bsJZncaWMuqIfFO0mcaVNPN263nbL3eTzYUF2AQlQICGv3n348_bTUbe2cM2llnH2-tPsXdgrTIDnjsH7GYa69DKO2KgZ70S5NSqlvV2Ex26u5O--c_zFalJm0FajHqhNZ8VvIS5pecw_1Sc0p2WgGw8E9yAh90AQvKLcd22gJW2wXyBKQlhWfUohO8VHqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
هيهات منا الذلة..
أبناء البحرين يخرجون بمسيرات حسينية تحدياً لعصابات آل خليفة المتصهينة ويرفعون فيها الشعارات الكربلائية بذكرى أيام إستشهاد الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79416" target="_blank">📅 20:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79414">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Emy3mwmPnrNBLSfpWGkr8wrnxb8ut1YUrq_mqjQbadEpSKFfMwOwsHWyE6_uJ9wzJyn2JaJoE21PCk2CLobamqK38tVxQ-qZuDOdH_c02Oc37Rxw_A7CnMmtDeQHM5QKQ2aT6oKZV1f-pDjQo_GEhkHsCfbff3DvxZzA4g1YRa7RvI51UnlrcyXuDiV5zhJEfzLPapFzzAUpjFbunykjP0njBBUhMzMMvgX3hpBj5wsCQqD9KxKdILOZ9gj37i0srG8RH-8tkfptvdU6ftRoBvelgbm-pA__dOCpyS_Yle2GAh0CgQ38XayYRMAKPE9QnSiMGOqTZTSjjRICAq4W9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الجيش الأمريكي: تبقى القوات الأمريكية حاضرة ويقظة لضمان الالتزام التام بجميع بنود الاتفاق مع إيران، وتطبيقها بكامل قوتها ونفاذها.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79414" target="_blank">📅 19:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79413">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcO94VNWx1-rMXOBxMwCuhSnrHBZZXOUmaJoVU8hKo9XFh0qop2OwNXgL0u_RFpAybq69krGhpa83iVqg_wZnvv5Q6TPtANFn3ixayjqk1Xt2iuDy6iM8BOqSzDresWats-Bo38Y0uUc6koltPMdMRZ2JuhnuBgHL3nSUxFIIepp5-eS0PuxO9rTu0e1sCl_1ft3p43vU1VgluNUAYnVb7RA1V1ZccQqyDbegcHbA48HSQ2sxgvd-NMSXluC0J9XjhhRPMkeWsQDA_ktDHGtPd2AjC8eqfjj0OiNzcOsSr3cKKALKP8FhipdZQDRyYwu676QW303Z-zajzuwQrS7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز.. إعلام العدو: نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79413" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79412">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTtwEUvPEeVSqANcVcbR2XAIwIzENn8dvkDcac9qx-cnKWRnwAEtas9TmsaEzRhekhgSsBLFjYXaYCJHTFuNUnJQiVUgN2QUNpe8dZPIVomlQvDP8we07TPH2H9uK4QgT25ixu26cus_8JBcsHVJPpygHFlyEpny-tz4dPlukXRyMcYE9aoP-VC_XE4R71uL4TtRIbTreI7i1QKdavq8uLrAzCUFRlmwqRR8aFDUJ8LnramMOAY91VLAvdz_Jl4kXocf4jI7_dktdXSD5RVxW7YXGOoYbT3qN--M4VzHBRu8AYxdmmjKhbn4rxyFgKgxcYz8jU-jNW2otiWVrZ_PsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بن غفير يتحدى ترامب ويطالب بحرق لبنان رداً على فشلهم باحتلال مرتفعات علي الطاهر والمجازر الحاصلة بجنود الاحتلال:  مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية. يجب أن يحترق لبنان كله!  ‏مع كامل الاحترام للأمريكيين، يجب على إسرائيل أن توضح…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79412" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79411">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هزة ارضية في مصر بقوة ٥.١ على مقياس ريختر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79411" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79410">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf9pBzmCu8aUmJPr-oY44BEZ1o77RRp16Q1FC1v0GmFyOWTa4NO2E4zkwEiilmVgSCUxiIxpAMzVvYLMKs4ph7LF5-4LAZLrLaJBznt5tMXi0Gc9s-9wiJuYY91XjoLGuwBCB6Q6dbmIdHE89p02wZzS0o_CPe86QVW0R3ok1AaSUUdZmVoe5h5gsnP3EwX463enTcf0eAELPizgkkiS1ZXbgjK1HjV9r9YJ5tIvTeJJ5dcmcagLeZypET-cL4Hkr4kU73x8BmgL3GpY0u6_kkEiTFpRUagoJnfDu36nXrF09dC8ljce1JRQxzmPBENfwxxJU0_W_a0Ni1QafUGqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
⚔️
لاول مرة
تنشر منصة كاف التابعة لكتائب حزب الله في العراق صورة تظهر نوع من المسيرات تشبه لحد كبير لمسيرة صماد ٣ اليمنية بجانب العلم العراقي ؛ لم تكشف الكتائب عن طبيعة المسيرة او مواصفاتها التي ظهرت بجانب مقاتل يرتدي ملابس عسكرية تشبه لحد كبير ملابس متطوعي سرايا الدفاع الشعبي التي تعتبر اقدم مجموعة عراقية مسلحة ظهرت إبان مواجهة عصابات داعش في العراق .</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79410" target="_blank">📅 19:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79409">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">أنباء اولية عن مهاجمة قصر الحلبوسي</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79409" target="_blank">📅 18:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79408">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجارات مجهولة عنيفة تهز الگرمة بمدينة الفلوجة غربي العراق</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79408" target="_blank">📅 18:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79407">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجارات مجهولة عنيفة تهز الگرمة بمدينة الفلوجة غربي العراق</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79407" target="_blank">📅 18:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79406">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuFdUAl-eyWoh8d6wWFLWLQ8tEJhxTjwuPbUU_S4huRiL__G8KKvcK_IwoLLorYFw9LiinPzt8Ms7sxZaD6ZIgbI1mHHYkIn2QSZiS2BNij9RCWCa86JC9PwPj63ob4MsExRVLoT8JFSvHCEuBRrhsOyY6ZmVxZRZG6SrpTS1kvfCSrglXgFuYxtnQpvw7Mfgc2wG_5R2SuI7XZAjHU5c3UePRE7s4S6M0bzSHwgzNFeoD6G0f7uIDKWKIvJrciCb-jkZwaZsaovMWuugDsKpjhc8gVOrEPEZlHx6ISHNmveU9ucy5mReS86gH1CCsAs1pS680nWC30wjZcPOuPQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙃
🇮🇷
فضيحة من العيار الثقيل   زلينسكي الذي لم يحمي سماء كييف ولا خاركيف يريد ان يضحك على بعض دول الخليج التي فشلت منظوماتها الأمريكية بالدفاع عن سمائها في المواجهة الأخيرة مع ايران ؛ من خلال التسويق لمنظومات أوكرانية مستخدما تطبيقات الذكاء الصناعي وفديوهات…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/naya_foriraq/79406" target="_blank">📅 18:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79405">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني: غادر الوفد الإيراني المشارك في مفاوضات "ميناب 168" إلى زيورخ، سويسرا، قبل دقائق.  يتألف الوفد من: الدكتور محمد باقر قاليباف، رئيس مجلس الأمن القومي الأعلى، والسيد عباس عراقجي، وزير الخارجية، وعلي باقري، نائب الأمين العام للشؤون الدولية…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79405" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79404">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز.. إعلام العدو: نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79404" target="_blank">📅 18:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79403">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌟
بيان صادر عن العلاقات الإعلامية في حزب الله:
في ظلّ الادعاءات والأكاذيب التي يواصل العدو الإسرائيلي ترويجها بشأن مزاعم خرق حزب الله لاتفاق وقف إطلاق النار، في محاولة لتبرير اعتداءاته المتواصلة على لبنان والمجازر التي يرتكبها بحق المدنيين، تؤكد العلاقات الإعلامية في حزب الله أن هذه المزاعم عارية تمامًا عن الصحة، وتندرج في إطار محاولات العدو المستمرة لتضليل الرأي العام، وفي سياق محاولته الواضحة والمفضوحة لتخريب الاتفاق بين الجمهورية الإسلامية الإيرانية والولايات المتحدة الأمريكية.
فقد تجاوزت حصيلة انتهاكات وخروقات العدو الإسرائيلي منذ فجر يوم الجمعة 300 خرقٍ واعتداءٍ موثّقٍ، تنوعت بين  الغارات الجوية من الطائرات الحربية والمسيرات، والقصف المدفعي من مختلف العيارات، وإطلاق القذائف الفوسفورية، على أكثر من 25 بلدة وقرية، من بينها مدينة النبطية، وقد أدت هذه الاعتداءات إلى سقوط أكثر من 111 شهيدًا و176 جريحًا. فيما تشير المعلومات الأولية إلى استخدام العدو للقنابل العنقودية المحرمة دوليًا.
وقد بلغت حصيلة الانتهاكات والاعتداءات منذ صباح هذا اليوم إلى الآن ما لا يقل عن 180 اعتداءً، وأسفرت عن سقوط أكثر من 28 شهيدًا بينهم ثلاثة شهداء من الجيش اللبناني و35 جريحًا.
ومن الثابت أن هذا العدو الكاذب والغادر لم يلتزم يومًا بمندرجات اتفاقات وقف إطلاق النار، لا في 27-11-2024 و 08-04-2026، ولا بعد إعلان التوصل إلى مذكرة التفاهم بين إيران وأميركا بتاريخ 14-06-2026، ولا حتى يوم أمس الجمعة 19-06-2026، بل واصل انتهاكاته وخروقاته للسيادة اللبنانية عبر الاعتداءات الجوية والقصف وتدمير البيوت وترويع المواطنين وقتل المدنيين.
إن هذه الوقائع الجلية أمام العيان تُبيّن بصورة لا لبس فيها الجهة التي تنتهك اتفاق وقف إطلاق النار وتقوّض التفاهمات القائمة، بل إنا ما يرتكبه العدو الإسرائيلي من اعتداءات ومجازر لم يعد مجرّد خرقٍ لاتفاق وقف إطلاق النار، بل يشكّل عدوانًا موصوفًا واستكمالًا للحرب بكل ما للكلمة من معنى. وعليه، فإن المسؤولية الكاملة تقع على عاتق الاحتلال الإسرائيلي الذي يصرّح مسؤولوه علنًا وبصورة متكررة رفضهم للاتفاقات القائمة ورفضهم الانسحاب من الأراضي اللبنانية المحتلة، وعلى جميع الدول والمسؤولين وفي مقدمتهم الولايات المتحدة الأمريكية ممارسة الضغط على الكيان المحتل لإلزامه بتنفيذ الاتفاقات ووقف الإعتداءات، بدل رمي الاتهامات يمينًا وشمالًا.
ويؤكد حزب الله أن من حقّ لبنان وشعبه ومقاومته الدفاع عن أرضهم وسيادتهم في مواجهة الاعتداءات والخروقات الإسرائيلية المستمرة، ولا يحق لأي أحد أن يسلبه هذا الحق الذي تكفله كل الشرائع والقوانين الدولية، وأن ما يسعى العدو لتثبيته من حرية الحركة للاستمرار باعتداءاته أمر مرفوض ولن يمر دون ردّ، وأن طرد الاحتلال من أرضنا هي مسألة وقت.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79403" target="_blank">📅 18:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79402">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز..
إعلام العدو:
نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79402" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79401">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
غادر الوفد الإيراني المشارك في مفاوضات "ميناب 168" إلى زيورخ، سويسرا، قبل دقائق.
يتألف الوفد من: الدكتور محمد باقر قاليباف، رئيس مجلس الأمن القومي الأعلى، والسيد عباس عراقجي، وزير الخارجية، وعلي باقري، نائب الأمين العام للشؤون الدولية في أمانة مجلس الأمن القومي الأعلى، وعبد الناصر همتي، محافظ البنك المركزي، وحميد بورده، نائب وزير النفط ورئيس مجلس إدارة شركة النفط الوطنية الإيرانية، وكاظم غريب آبادي وإسماعيل بقائي، نائبي وزير الخارجية، و... أعضاء الوفد الإيراني.
ووفقًا لتصريح بقائي، المتحدث باسم الوفد الإيراني المشارك في مفاوضات "ميناب 168"، فإن هذه الزيارة تهدف إلى متابعة تنفيذ التزامات الطرف الآخر، حيث يتم اختبار كل اتفاق وتفاهم عند حلول وقت تنفيذه.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79401" target="_blank">📅 18:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79400">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
بيان صادر عن بحرية حرس الثورة الإسلامية:   نظرًا لجرائم النظام الصهيوني في لبنان، وانتهاك التزامات الولايات المتحدة في تنفيذ وقف إطلاق النار، فإن مضيق هرمز مغلق أمام جميع السفن. نؤكد أنه تم إغلاق مضيق هرمز، ويجب على السفن عدم الاقتراب منه؛ وإن فإن أمنها…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79400" target="_blank">📅 18:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79399">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f58ccb.mp4?token=tFh5kSiY3yyT5ja0ckFBjsnPle2iv_4oJwNjPMuP374HBpevYOQgxGtUk2YZ-mgOkEOpw2y7Ahafr6juamY6Nw4EiulO0R9iBGla0fWPeoeE6U9QaXizKbGASf-eWhV66oakRwc5_EfIJaZ4k9dCvY9AXq0p1y7M959d_2_qNiMQ6hj3su5TF6boU6jfJ8zdlYqvjQQcbZsaxwRBl81t_0GO10W_Nw6s_xum566Sn79hdsA5VxnJLcEk-hPOMKKsa1DJeNWXgOrXg8BZn9m32-2al941v2LSXRpUD294i7GEkadZoEy6_UGna24CC3l3RkD0xrMdzpyg-DYZExFkTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f58ccb.mp4?token=tFh5kSiY3yyT5ja0ckFBjsnPle2iv_4oJwNjPMuP374HBpevYOQgxGtUk2YZ-mgOkEOpw2y7Ahafr6juamY6Nw4EiulO0R9iBGla0fWPeoeE6U9QaXizKbGASf-eWhV66oakRwc5_EfIJaZ4k9dCvY9AXq0p1y7M959d_2_qNiMQ6hj3su5TF6boU6jfJ8zdlYqvjQQcbZsaxwRBl81t_0GO10W_Nw6s_xum566Sn79hdsA5VxnJLcEk-hPOMKKsa1DJeNWXgOrXg8BZn9m32-2al941v2LSXRpUD294i7GEkadZoEy6_UGna24CC3l3RkD0xrMdzpyg-DYZExFkTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في بغداد تناقش الخطط الاستراتيجي لبناء العراق عبر المغنية شذى حسون وأغنيتها الشهيرة للنشيد الوطني  " ناعما منعماً "</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79399" target="_blank">📅 17:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79398">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThzGIwb2YbvNX2T70srj126iV5_6AEScONWQAttomx2AIB9kl0GofX3JDPm-6CRPf41Ae8V_-Jx7vT1NLwnPZMKa2r1yzlBRIWg0BBvz3c5FgwJWth9seFWNt_P_66ZS-J2chn3MBjgfpjgSajr_eDVKB8XRVzG8kvgJF3rY40kHhQq0YwzscF9gE-bcwcnplLGHwdtnuTLDxqsXMf_FkKUV5dOmaLG-ws67xnEfyzbDIS2oyxshXxCN9JV7pfIuql4I8VYo5uhyfnyFZZpDNgiuCX3sY7P96KeUdikXf0P_zLdVz-Uqi5vKF0jWcGef_G2kSCStrPhXfZZQCzO4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في بغداد تناقش الخطط الاستراتيجي لبناء العراق عبر المغنية شذى حسون وأغنيتها الشهيرة للنشيد الوطني  " ناعما منعماً "</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79398" target="_blank">📅 17:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79397">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
الخارجية الباكستانية:
محادثات تقنية أمريكية إيرانية ستعقد غدا في بورغنشتوك بسويسرا.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79397" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79396">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7S3Vyar_gXRnljuLn7VHbIMIODzsWnTVkNlbkKqo7xrub99O3oRpEuCaGvfVLoqREVzRG_HrPZAsd5a5qmLlgN6WFBVVyWlOzVB3UsIgy9WD-XL0-0dzsLiO4D2Du2Cjwoofqgccqg-mhUf94JeXkB8RMv0g6wD8-KMLSAcbNuSWnIIV2nhpnpuMd3SC2aT0mfsv2e4sqPslOVnSLV_Rsyyh4P_xSaW-hW-6GGOGa29cE0PVTF5qixg-W3-OGNAkk6xGcRJ3DNnQHy8Wzu9KAwvcT-3enSzgLWPrvbLn2e5VctKagH048asiISPoZODuHFe5bSiTeB_h5kJMEwf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب يصعد تجاه ايطاليا:  طلبت رئيسة الوزراء الإيطالية، جيجيوريا ميلوني، مرارًا وتكرارًا، التقاط صورة معي خلال اجتماع مجموعة السبع في فرنسا. إنها لا تحظى بشعبية كبيرة في إيطاليا، ربما لأنها رفضت الولايات المتحدة الأمريكية، وهي دولة تحب إيطاليا وتحميها حقًا،…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79396" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79395">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
🇺🇸
ترامب يشارك تقرير يهدد فيه نتنياهو بعنوان "ترامب يملك أوراق اللعب في فرص نتنياهو الهشة لإعادة انتخابه".</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79395" target="_blank">📅 17:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79394">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
بيان صادر عن بحرية حرس الثورة الإسلامية:
نظرًا لجرائم النظام الصهيوني في لبنان، وانتهاك التزامات الولايات المتحدة في تنفيذ وقف إطلاق النار، فإن مضيق هرمز مغلق أمام جميع السفن. نؤكد أنه تم إغلاق مضيق هرمز، ويجب على السفن عدم الاقتراب منه؛ وإن فإن أمنها سيكون مهددًا بالخطر.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79394" target="_blank">📅 17:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79393">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxQt47jkRA-9HqIU6g-2aulrB501KrhxqpGa7AwxoGjFeiHyXYdQ8NzkIOrQ9yL27Vi4vP-sPFMwha5-JmEiJkYgbz_8hcc0WpDWjyuPTXN5gQFqoBpMI0DpHPjgt171sT9uDzOftvNwlpyjEzvvrkN53zFXvDKFq04oy4tvJ4D9yHqgLOkwQzPNq9FeL-9wQ95rrBYASg5fo4HN0ZC0pFHOlYLrAifZFIwKwwlzGwWscdjlZeWQZZxelWN1TglvbC7-VVgAbPmLHmPwzHswF-WoQO5Z1gsna1sdoG1_wH-vJdl9lasTjGip_O90eNoFraJCRTsdd4Ou60jXePJsEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
ترامب يشارك تقرير يهدد فيه نتنياهو بعنوان "ترامب يملك أوراق اللعب في فرص نتنياهو الهشة لإعادة انتخابه".</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79393" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79392">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قرار الخارجية والتصريحات جاءات قبل بيان الحرس الثوري مما يعني عودة عراقجي في الساعات القادمة إلى ايران بناءا على التطورات في لبنان   ايران من اجل تلة يقاتل بها حليف تنسحب امام مفاوضات دولة كبرى  يخشها بعض سياسي العراق بسبب تغريدة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79392" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79391">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فانس: الرئيس ترامب قرر منح المفاوضات فرصة وذلك خلافا لمواقف بعض الأطراف داخل الحكومة الإسرائيلية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79391" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79390">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فانس:
الرئيس ترامب قرر منح المفاوضات فرصة وذلك خلافا لمواقف بعض الأطراف داخل الحكومة الإسرائيلية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79390" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79389">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اعلام العدو:
ما تحاول القيام به إيران هو رفض أنصاف الحلول والأمر الواقع في لبنان وفرض حل جذري لمسألة التواجد الإسرائيلي في الجنوب. قد تكون هذه مغامرة ولكنها قد تكون ناجحة أيضا بالنظر إلى رغبة الإدارة الأمريكية بإتمام الاتفاق، وفي ظل توتر العلاقات بين ترامب ونتنياهو.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79389" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79388">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وسائل اعلام تزعم: عراقجي يتوجه إلى سويسرا الليلة برفقة وزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79388" target="_blank">📅 16:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79387">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وسائل اعلام تزعم: عراقجي يتوجه إلى سويسرا الليلة برفقة وزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79387" target="_blank">📅 16:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79386">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وسائل اعلام تزعم:
عراقجي يتوجه إلى سويسرا الليلة برفقة وزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79386" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79385">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">في محاولة لمطأنة الاسواق العالمية..
فانس: لا يوجد دليل على أن إيران تغلق مضيق هرمز.
جرب وادخل
😄</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79385" target="_blank">📅 16:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79384">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
مقر خاتم الانبياء المركزي:  ﴿وَإِن نَّكَثُوا أَيْمَانَهُم مِّن بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِي دِينِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَيْمَانَ لَهُمْ لَعَلَّهُمْ يَنْتَهُونَ﴾ (سورة التوبة، الآية 12)  نظرًا لنكث الولايات المتحدة العهود…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79384" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79383">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5lHGwrbBrHF7FtJ2EfjjZfkfc7XRQ6oehpgLihFGRZo60GSPpxRYA7fl6oP3Q0aqqH_kdF3ir2b0D6S0LbYUiguza5Ym3V8_SfsBolHMbvhWSaHwHphiA2MUT6cEdDypdDLeHMc_gGMmAXmhQnmAffWtcbBHju8BdlAjoPgEx7eCQsztruqVIjUdSbjDBr7Hf-uGPMQYn3JO9oVmA9F9UdhnYoefTS5GWnPetvhIeF0m-BhBaKhAoeMNA1tHJfQVSe_7l69NtJxewFh2dClw5Wc_zjnngZxuUrnhBX3yzzUdYMNmNYYAVcx0fHaHV-wVxGPNhTbbPwDUBnHsd3yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">على الرغم من الإغلاق
ارتفاع اسعار النفط بالسوق المجازي الى اكثر من 80 دولار بعد اعلان ايران اغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79383" target="_blank">📅 16:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79382">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مقر خاتم الأنبياء يعلن إغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79382" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79381">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مجددا.. النائب عن حزب تقدم (مهيمن الحمداني) يطلق النار على عمال بناء كانوا يقومون بترميم جامع الخنساء في الحارثية ضمن العاصمة بغداد مما ادى الى اصابة عدد منهم بجروح خطيرة  متى يتم حصر مهيمن الحمداني بيد الدولة</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79381" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79380">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مقر خاتم الأنبياء يعلن إغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79380" target="_blank">📅 16:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79379">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مصدر امني لنايا : اصابة المواطنة (سناء محمود خلف) والدة زوجة النائب (مهيمن الحمداني) بطلق ناري في منطقة الفخذ ضمن منطقة الحارثية نقلت على اثره الى مستشفى الاميرات الاهلي لتلقي العلاج وبعد التوجه الى المستشفى والبحث والتحري تبين وجود خلاف بين النائب و زوجته…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79379" target="_blank">📅 16:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79378">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
بحرية الحرس الثوري حددت مسارا من جنوب جزيرة لارك لدخول وخروج السفن من مضيق هرمز وإذا لم تلتزم السفن بالمسار البحري جنوب لارك فإن مسؤولية أي حادث تقع عليها.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79378" target="_blank">📅 16:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79377">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🌟
فوضى واعتداء داخل محكمة كركوك بين احد المواطنين وعناصر امن.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79377" target="_blank">📅 15:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79376">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🫡
وزارة الداخلية العراقية توجه بتشكيل لجنة تحقيقية عليا للتحقيق في حادثة وفاة شخص يحمل الجنسية اللبنانية كان قد أُودع التوقيف في العاصمة بغداد إثر مشاجرة مع أحد أقربائه.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79376" target="_blank">📅 15:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79375">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة طير حرفا جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79375" target="_blank">📅 15:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79374">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrOlyOv4VQwb5s7OCxjwqg45HepwC3Swt-G9_kDzs837JE-o3Y0c3ncPd1M3Oi_ak-PwbPEYmbuQHX1CXYAcRytBweAt078_H_bx2kY96nDeRldwxb8Yxuex-X3Lw-_gZ5rEze7W3ww5aEBDm9MNDPNe7-Mo1ReA0lf-bvRh8j00RBSKOFh_3TOFTQTENvdOrRx0If1-mPBOBCC96OwYTTyfwzPN-IC7kG6TE9G7bC-RzihEZzfZUzQScKaipfXVB04opZZtDuHBQKtCoqcB9ir7BIkOu_FhF7Dn_GSBlOVKQqIzG4Fy_w-nfhO1acbF9BMq0SPbijgyBEOB8_TR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
عائلات شهداء مدرسة ميناب ترفع دعوى قضائية رسمية ضد الولايات المتحدة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79374" target="_blank">📅 15:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79373">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inh8EctQUZXu77Y1gkLHVa_RWaumdsfEmVpmfcgRyjH72vZzEbYry_C1crQnCApVfUrGf5sH3Zoi9JXO0gcVBxydgKD2s2uZqXzPTdXvHP6oiubPZGQ7U1pF3urZ190ID5bSBNxTNUq1OWp4GZ6z4vQUndnUm5Jlp_IyZeybzaxc4jEaY6s7HFu56mNiLXu9J5juEjwO_Mq1ChvdskIEofAW_VP3hQMI8e-0O6Vco1v95VcRUW7Jb4aEnZgXGNx7NMQxsBxVULXxTcIJNX65oSvpJ0TX9l_hxt0yb9MsNTnbE4dGDo4TTEN0WvWn5od4eLiK555HfWsKe-MLi2GUUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب يصعد تجاه ايطاليا:
طلبت رئيسة الوزراء الإيطالية، جيجيوريا ميلوني، مرارًا وتكرارًا، التقاط صورة معي خلال اجتماع مجموعة السبع في فرنسا. إنها لا تحظى بشعبية كبيرة في إيطاليا، ربما لأنها رفضت الولايات المتحدة الأمريكية، وهي دولة تحب إيطاليا وتحميها حقًا، عندما يتعلق الأمر بمنع إيران من الحصول على سلاح نووي أو تطويره (لكن الناتو فعل ذلك أيضًا!). حتى أنها لم تسمح لنا باستخدام مدارج الطائرات الإيطالية، وهو ما يمثل عائقًا لوجستيًا كبيرًا، وذلك على الرغم من حقيقة أن الولايات المتحدة تساهم بمئات المليارات من الدولارات سنويًا لحماية إيطاليا، وغيرها من حلفاء الناتو "المزعومين".
الآن، بعد أن هزمت الولايات المتحدة إيران عسكريًا، تريد أن تكون صديقة مرة أخرى من أجل رفع "أعدادها". لا شكرًا!!!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79373" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79372">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇨🇭
اعلام سويسري:
وفود تحضيرية لإيران والولايات المتحدة وباكستان وقطر تعمل منذ أمس بمنتجع "برغنشتوك" تحضيرا للمحادثات ولا أثر بعد لرؤساء وفدي طهران وواشنطن.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79372" target="_blank">📅 15:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79371">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fea425d27.mp4?token=DK_vjedG2yxGln2dUKusK1jH6laC2ZtYKjgqzZeEIu5l4LmnUA6puIMyONvfZcZ960BrepW-Vs0QRycFOFbAbxl3KLMBh1DDFVqqSCZGuWJ3LVTfHuxptSsBhJzwkLlKnM0sskP-4z2cVnWFSHxoNQlVm12tW60jmyP0kaxgJZgmrA84wRmM62iswtvaOJQpgeN1O1hdzbAfxYTX-W_EKfIWQ2vJEfYLiXNiWb4tRT9ZESNNUWS2hrqOl1t9dStW1m0Nt2yIbtgAEYn5HexwIqVxH82V0hE3OHKd9LKhZLizchh6Ll87vlxM1bX-NAkx03F2qjEh4QGQ_wMHpI3Ybw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fea425d27.mp4?token=DK_vjedG2yxGln2dUKusK1jH6laC2ZtYKjgqzZeEIu5l4LmnUA6puIMyONvfZcZ960BrepW-Vs0QRycFOFbAbxl3KLMBh1DDFVqqSCZGuWJ3LVTfHuxptSsBhJzwkLlKnM0sskP-4z2cVnWFSHxoNQlVm12tW60jmyP0kaxgJZgmrA84wRmM62iswtvaOJQpgeN1O1hdzbAfxYTX-W_EKfIWQ2vJEfYLiXNiWb4tRT9ZESNNUWS2hrqOl1t9dStW1m0Nt2yIbtgAEYn5HexwIqVxH82V0hE3OHKd9LKhZLizchh6Ll87vlxM1bX-NAkx03F2qjEh4QGQ_wMHpI3Ybw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
زعيم ما يسمى بـ"المعارضة الاسرائيلية" يائير لابيد:
دفع نتنياهو بالخطة الكردية دون مراعاة رد الفعل التركي المتوقع وتأثير أردوغان في واشنطن. أردوغان أعطاه درسا</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79371" target="_blank">📅 15:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79370">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGaq20Z8PH8RBtiv88bgsNHMHhFAcU_nlQ9f-mRTsPeNRNROOy6uSxRPTSfMWDEshFjFFrvfAvTN1AmusHc1rmFIYpVNkmL7K7BG6bn9MZiTsBsbBFz0fc9fG2VijacNI6yVbWJpGTisaQ3u3DZxvDast-Nax1mhXNBOl3Uj9gdfUcRyC6OxRu2VNjOV_OKvhCeNuBys7TNYMr1FJTLIaq-LwJXmxaYAOJMOEPAT3UjzsWpWkmre_3jSYTaO8W2DEcuEZgLKYqAd0ZHyCu6oj86168Bi1Tf2kwNI970Jwza6ajGINiJsESkWBry7lROgjSF1IvUV56OSMazL3A5TdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
المنشور الأخير لمدير عام كهرباء الوسط علاء الجبوري قبل اعتقاله بتهم فساد والذي سارع أدمنية الصفحة إلى حذفه بعد الاعتقال</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79370" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79369">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e875b0f6c7.mp4?token=ZH2MbOs29kRFf0YcPm5tbDaWLrs45YC5GedKZh3F-E1EoMTm1EH58oWBAA84TYPE3JVY5WzjGO7m3tv1rznWSV1UBZlEiE7afvhEE1twaX1lf7UybCex5O-JvaSzR2aDUzcrDTfA6Mjkz8k4kUwbfERRHQe54t2DsoFU9kNDL52I0DBRg3sv0aPIv8tmAJrYcB9GKxoDw6g0h0n9sjZLelb0ykj6hq4cMPuYDxl8-OicD5R5jDVpcSbk2HaWCJXbLbMq8n2U29ns8Hh49RUhxeegY2h56faXwRpqRy4RCB0cfwN_PYbJa-CPRUAjelgtJWXoIaDODtgtTOpj1cKrgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e875b0f6c7.mp4?token=ZH2MbOs29kRFf0YcPm5tbDaWLrs45YC5GedKZh3F-E1EoMTm1EH58oWBAA84TYPE3JVY5WzjGO7m3tv1rznWSV1UBZlEiE7afvhEE1twaX1lf7UybCex5O-JvaSzR2aDUzcrDTfA6Mjkz8k4kUwbfERRHQe54t2DsoFU9kNDL52I0DBRg3sv0aPIv8tmAJrYcB9GKxoDw6g0h0n9sjZLelb0ykj6hq4cMPuYDxl8-OicD5R5jDVpcSbk2HaWCJXbLbMq8n2U29ns8Hh49RUhxeegY2h56faXwRpqRy4RCB0cfwN_PYbJa-CPRUAjelgtJWXoIaDODtgtTOpj1cKrgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
فوضى واعتداء داخل محكمة كركوك بين احد المواطنين وعناصر امن.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79369" target="_blank">📅 15:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79368">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
🇺🇸
السفير الامريكي في تل أبيب مايك هاكابي مجددا:
لو لم تكن اليهودية موجودة لما كانت المسيحية موجودة، ولما كانت الحضارة الغربية موجودة ولما كانت أمريكا موجودة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79368" target="_blank">📅 15:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79367">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏴‍☠️
جيش العدو الصهيوني:
في عدة حوادث مختلفة خلال الليلة الماضية أطلق حزب الله أكثر من 50 عملية إطلاق باتجاه قوات الجيش في جنوب لبنان. سنرد بقوة على أي اعتداء</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79367" target="_blank">📅 15:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79366">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ويتكوف وكوشنر يصلان إلى سويسرا</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79366" target="_blank">📅 14:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79365">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptWYRFsenMRZ0snD_PBdlhwBjS16LUuzdFcmWv3-lR3nfuVaGhpILvyF-6A4ASQ0BXxDA8pOp-6NcJQCWCp9pYm6aOeHQnL1dPoFTBLqPYHzB6EyENp9QYAfDZZCGVJ0fukRJUbujg-xyhgogvgTS3ba0usS8BD-ageY_JS46ySvNQ1zZ6p5VYGWkv225z0_v_uDgmjnYuYSI6OIxnpFlwRSBRMtd1j01pQA2_0OuiCwA5lMa3qLmV3W2uRFE0lTZ84AdZ5-Ykwth_4114nuvAS2LpURBHr7HRVktkxm_4jrowjSQXXs6-nXnyO0tIofQmCndS45e0djljpIOXHJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
حزب الله:
ملتزمين بوقف إطلاق النّار، لكن لن نتهاون في التّصدي لأيّ محاولة يُقدم عليها العدوّ لقضم الأراضي وتوسيع احتلاله، وسيكون مجاهدينا بالمرصاد، وبكامل جهوزيّتهم، للدّفاع الكربلائيّ عن أرضهم وشعبهم ووطنهم</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79365" target="_blank">📅 14:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMXU5NNRUFLPsntyJU_hjRzoUWy32KY9i5untVivKg7o168NVInDOV1hQtdxZF5CtZTkrlGhY2Bwa33eflIA1Yizq6F8ZURfKSGUuVdJ4PoScyOcIwEOwcim8B3eWiYCBbUrDCS-hRuSfSlLwM6CqP80i67xvjydSnjKunCdsBETTm_tiELb_n3Rtg5735wLfVU-Qce5-CdLwGLP84oPBCVWD5MgF0xvKvnpMVwapB0Wec2L_4vQlmm0vj5PDzxXWuaxgEPf-PGeGndbLB8eotR1viUTZ1STZmhanmwACgUfEHWfFVtDkvfixpO0J2KhRQYYsMQRApB31_BcA65Z6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب
يدرك الحمقى اليساريون المتطرفون والديمقراطيون مدى نجاحنا في حربنا ضد إيران، حيث هُزمت بلادهم عسكريًا بشكل كامل. استمر أوباما في منحهم مليارات الدولارات نقدًا، ولم يستخدم جيشنا المنهك آنذاك لما كان ينبغي فعله لكبح جماح إيران، الراعي الأول للإرهاب في العالم. لم يكن لديهم أي احترام له. اعتقدوا أنه، مثل جو بايدن النعسان، زعيم ضعيف وغير فعال، وكانوا محقين تمامًا في ذلك. أفلتت إيران من "القتل" لمدة 47 عامًا، حتى جئت. ثم تغير كل شيء. أمريكا عادت!!!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79364" target="_blank">📅 14:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79363">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7ZHJJrHRfj2RPUkyMywpMy_X6Hz5WwbQWk1RjgSF6Iwdb17k-m7ybGHEIhKtf1Vchz2y4jE95F2kMm7SMPHI9TnRkGthysukvjepgtLElX3UVSKkmsFQw05pw8AwZpNpepZqxm2CX66L8cKEyaCf7Paq56B-hkGbPv7zvYYHxAmzcvV6UHzAbGu2PsBKTF0A7EfhSUDBTVYoayod1zqwOPW02YHM9kUwgdM1Y-nuvoqdrQYEwU30QrOh4Y8wUMZcamaoUUAwuTeT3uvf4wq7JffaC0W9e_ti8U0eKfb0gQDO4J1v2gdubDd_3kw5S0WfvKkkWrS0SugUI3xO-2RxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🏴‍☠️
المتحدث باسم وزارة الخارجية الايرانية يشارك تصريحات لسفير النظام الصهيوني في الامم المتحدة ويعلق:
هذا الاستعراض المخزي للتحدي المتغطرس - ضد العقل والقانون والأخلاق والعدالة - هو نتيجة حتمية أخرى للإفلات المطلق من العقاب الذي منحه عوامل التمكين لنظام إرهابي الفصل العنصري. يواصل هذا النظام حملته للإبادة الجماعية ضد الشعب الفلسطيني وفي جميع أنحاء المنطقة بتجاهل تام لجميع المعايير المتحضرة. لقد حان الوقت منذ فترة طويلة لكي ينهض العالم ويواجه هذا التهديد الخطير وغير المسبوق للسلام والإنسانية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79363" target="_blank">📅 14:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79361">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">من بغداد، من أمام السفارة الإيرانية، اجتمعت جماهير المقاومة الإسلامية احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في مواجهة قوى الاستكبار.
آلاف المشاركين لبّوا دعوة المقاومة الإسلامية كتائب سيد الشهداء، مؤكدين أن خيار المقاومة ما زال حيًّا في وجدان الأمة.
في رسالة واضحة بأن نهج المقاومة باقٍ ومتجذّر، وأن إرادة الشعوب لا تُهزم أمام التحديات.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79361" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79360">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇨🇭
‏سويسرا تقرر تمديد التدابير الأمنية في البلاد حتى 22 يونيو في انتظار موافقة الجانب الايراني على استئناف المفاوضات.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79360" target="_blank">📅 13:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79359">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📰
نيويورك تايمز عن مصادر:
مسؤولون غربيون طالبوا نتنياهو بوقف مهاجمة لبنان كي لا تبرر إيران انسحابها من التفاوض.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79359" target="_blank">📅 13:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79358">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تحليل نايا...تلة علي الطاهر.. لماذا تسعى إسرائيل للسيطرة عليها رغم الخسائر؟  تُعد تلة علي الطاهر من أبرز المرتفعات الاستراتيجية في قضاء النبطية جنوبي لبنان إذ يبلغ ارتفاعها نحو 700 متر فوق سطح البحر ما يمنحها إشرافًا واسعًا على عدد من البلدات أبرزها مدينة…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79358" target="_blank">📅 13:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79357">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
مقتل جندي إسرائيلي وإصابة 11 آخرين بنيران حزب الله في منطقة علي الطاهر خلال الليل.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79357" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79356">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌟
🇮🇷
وزير الداخلية الباكستاني يصل إلى مشهد تمهيدا للقاء مسؤولين إيرانيين</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79356" target="_blank">📅 12:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79355">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdcf3568f.mp4?token=NbONZCHc4A0A8Zh-X-eRnR6oMznqZVmaQpQMh_td2EJ131PV0hktxOyCJdW8-OF2sINVnhl5nsm25ZS5aJOuD7VKnsMJDASPPW7u_A80swRPIPSB0XKkAi4FcfZ-EA6JUWvFAJoIkpc5-NgapUKfZZNhdEQQ-hYUfvBC_j4pDHaN3I4BQ4tfKPF0wEQUTT6X7OaHb5scLhut3Q5JueBzn1xfIiozuZJKt1KsVHpu6nhBFL0_UC0RNJtajW4QI7yDD6jS_8tNYdEF1dDaztPq9HfzqrjEBYB1XR3XkXqkbTQW9zuncNDUv7LtsZIhpe4TEUjureiIkqpfwMC_0xaaxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdcf3568f.mp4?token=NbONZCHc4A0A8Zh-X-eRnR6oMznqZVmaQpQMh_td2EJ131PV0hktxOyCJdW8-OF2sINVnhl5nsm25ZS5aJOuD7VKnsMJDASPPW7u_A80swRPIPSB0XKkAi4FcfZ-EA6JUWvFAJoIkpc5-NgapUKfZZNhdEQQ-hYUfvBC_j4pDHaN3I4BQ4tfKPF0wEQUTT6X7OaHb5scLhut3Q5JueBzn1xfIiozuZJKt1KsVHpu6nhBFL0_UC0RNJtajW4QI7yDD6jS_8tNYdEF1dDaztPq9HfzqrjEBYB1XR3XkXqkbTQW9zuncNDUv7LtsZIhpe4TEUjureiIkqpfwMC_0xaaxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
مستشفى رمبام في حيفا تستقبل جنود قتلى ومصابين إثر المعارك الجارية في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79355" target="_blank">📅 12:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79352">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtOy1x0TMOeHABjhEElBEPZaUktrNjTaGqpeZmA8UScqN3VjvEeETZgzFm0mpuWXrS5zy2IUtMYi1HWSfRJAeLG2POoxh55Vv1SAe8MDGOQEaPOxmhMNkfIHx40ojL7dIXyXxJAfEFW-0aszg_8IAGp3zFVIwZ22-ZeTLlufl68_y__FcV9pWB6hqUvtNXQWwARCRS5Liz5XJdnhJfhPSp7thZekbZUYB_kB3UoxU3zBD4DvhLRe3OXWQ7a41wWXIMajVwRPYxrx0E5WJpC2xShSupfCfoCoEOUwsXpKdqToxjLCHMICOswCF9Jw8oelxDIaFhk4TXAMfDsKBdF2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrOx_4dNUgnxlJ9t1FR1eLCddwdObX-sRjKqKuoOsgfIdrDJMgclXU2ZUlIlibXc6w8gZSQQxNL1Lx4Xvb1VOnpy069CxKC4GLzSnSKoCKarfOXshWEFKz8KErRi18QRFzdC3UsPGZwoezxiy-KTcowdr0fH5vWWHnJZbeC4HWW-kSto-P9z_9Tx9-wza19qo16MCi-uNcCk51-qwMrxHHnNO6dTWd5JU149jL_WAg5m881LAeDtHQXHOPQ7bofIxQAnxJkCWtY1dsBhyp82tLRq3WDObkBkearE0xmzZDUoWYwld8wcp7_HBKeCq61wpG_jM3MfCS8p1tkSOtEZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQmmiuwHg9xl4knJfLQOCbkjFeHQaK7m0HaTphAWpgJnsQtxhuLMKlRyV2dEbm7vOf3UV-XMifKlZU_Uxpa7VFs-K5mwY7FaIEzmA6F4Ww_P_L7py0SSfUGHVSplX0Pxsh4CpaTLLhntFqLb7DoUpuazN_95N4Xr6aJMboIrd9OgtFBT-qYLKYuHKcodCZZaJDjVEgGzCBFS3N_BQ10Zv8AStsQCoFViUe-3L5q8K2a4NYQQpf2DRibeGtF-QlYDUSV63z_bbrRabnlNXvz5gSClXx1BLvZcFLGRDETMcl5t8p_zxXMMXWsWwoG14HSyJEAxFnKYXOSRPtLTaK64Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇾
ضمن حملة التصفيات بين حكومة الجولاني وعصاباته.. مقتل عدد من إرهابي الجولاني إثر كمين على طريق منبج حلب.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79352" target="_blank">📅 11:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79351">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f9366af54.mp4?token=j65JENdLTXhC9lpvBHi1DLQk1l3vdMwp5idiUVXo1oPIPQZnyT4FybnAoMaDF248ZAhpYYv2dD_8uqMpxjst4tGXCv6-zrxUG0DJun9p-p06HDHDwu-DkNdyFxmou1k7w98LgqhYqXQ1XCgUsMU44KAsmDLmXl4jJ8Z-VcJao_9o6Ha9o9C5p4fkye7I9Lwn1-lzMO7z9KlT-Sh8l_n870wyMmNLOW3Du5-oZntcMssTZ-o8KwcwX7Flp34yqRheCPxLxExUe1ujWC_S5sB2Noawy8kgBdynKiB4wOr9Nh2b5qwQeypLSsUEp5w7SYGDGzUtNRXbFYQbDplA0za1Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f9366af54.mp4?token=j65JENdLTXhC9lpvBHi1DLQk1l3vdMwp5idiUVXo1oPIPQZnyT4FybnAoMaDF248ZAhpYYv2dD_8uqMpxjst4tGXCv6-zrxUG0DJun9p-p06HDHDwu-DkNdyFxmou1k7w98LgqhYqXQ1XCgUsMU44KAsmDLmXl4jJ8Z-VcJao_9o6Ha9o9C5p4fkye7I9Lwn1-lzMO7z9KlT-Sh8l_n870wyMmNLOW3Du5-oZntcMssTZ-o8KwcwX7Flp34yqRheCPxLxExUe1ujWC_S5sB2Noawy8kgBdynKiB4wOr9Nh2b5qwQeypLSsUEp5w7SYGDGzUtNRXbFYQbDplA0za1Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
من منفذ مهران الحدودي مع إيران.. بدء توافد الزوار الإيرانيين لإحياء ذكرى عاشوراء في العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79351" target="_blank">📅 11:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79349">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFvAC6wWwPcmwXT7BEJxItKps-2ecZTp57bleowOuUX5ulpE-pE2wYoYTg180RT_c8B-9AmixDTid5fGQsuMzCdOx7YJC32CBpxgHA6fchENln-Q4Ni70j18ClpOyMbz2EDcIATBBtWWpssT--F2OuKlhm2qWqM4vZ4uYAaESwVVsR4jAbdO2IB8E0vVOIjvExpgiY5CHUtHblG3n93ZTVpo8ZITFTpKWgZqh50KS1qPfUK27XqqXJfeUIvazKUKoYY3HtbqcfOqdcUODxEGwH3QDIZ8cYGU7AXRxV-5D57mukRV1ee470VityfsYsm5g0tKJeyVBQjdkGt5kazSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
هيئة البث: مفاوضات ‌لبنان⁩ وإسرائيل القادمة ستحدد مناطق تجريبية جنوبي ‌لبنان⁩ سيتسلمها الجيش اللبناني
من منجزات الجيش اللبناني إغلاق قرى وبلدات الجنوب ومنع وصول سكانها إليها ؛ الصورة أعلاه من إقفال بلدة العامرية في هذه اللحظات.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79349" target="_blank">📅 10:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇷🇺
ميدفيديف من روسيا: أصبح مضيق هرمز "سلاحًا نوويًا فارسيًا" وسيتم استخدامه على هذا النحو.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79348" target="_blank">📅 10:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79347">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896e6400c7.mp4?token=Es4wMPQevZdH8PwZoXM6QTWR6KOFgK6EvvTWI1g5oNDJTKcltMpuX4itZHJ-VOE2LCEowLfI8Z0cNF14hUA1XSJwt87MPD3AsbUBUeRGNZEteQ-yyh-ae7K8UCOQ4nr91FJFMOoAm8JZbO20PNsaBjPDqloKf4DU0Nthpu4-I-BD9zoxK3EY4Xla2JWmrPbc2MYc1LlKgcO5IUnqGzQEcXvQnSo9YqGaaIf8jruO13IpX-H80u-2ilJnfKCKW5UTOoGo-QPpNqNyO3RKQUCPm0F_Zf2z6gRyuaWEqhMf-zjv7UA9QmzoQGp5brVn_IlKluZFc_bWKsanNqm8lfRfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896e6400c7.mp4?token=Es4wMPQevZdH8PwZoXM6QTWR6KOFgK6EvvTWI1g5oNDJTKcltMpuX4itZHJ-VOE2LCEowLfI8Z0cNF14hUA1XSJwt87MPD3AsbUBUeRGNZEteQ-yyh-ae7K8UCOQ4nr91FJFMOoAm8JZbO20PNsaBjPDqloKf4DU0Nthpu4-I-BD9zoxK3EY4Xla2JWmrPbc2MYc1LlKgcO5IUnqGzQEcXvQnSo9YqGaaIf8jruO13IpX-H80u-2ilJnfKCKW5UTOoGo-QPpNqNyO3RKQUCPm0F_Zf2z6gRyuaWEqhMf-zjv7UA9QmzoQGp5brVn_IlKluZFc_bWKsanNqm8lfRfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
لليوم الثاني على التوالي لا يزال الكيان الصهيوني يستهدف الجنوب اللبناني بغارات مكثفة وسط اشتباكات عنيفة في مناطق توغل جيش الاحتلال.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79347" target="_blank">📅 10:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79346">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ed7f3d48.mp4?token=K5JHYSXkhSVGAAppvk818pZn_j6yPV1BXlBpX-TZYvQrg1yL71f06rBnq18mHO_onXEO6R_CjhM6CEAoxyanh9hBVOBFyv282N3b_otcL6tQCzx9gKI_ZjhjfjN5f5s_jeOhy6xnk_bpwAzmr70dc_fe-aBAFhglqgYsgTjyjIGhxTK6hWAmxA0uopEbkvt5jITHbOKvEeH9fHg4Rk4QNaiSrooEcFF0hdgMCpTNCcXgU6a7liCF0nZmXKZmCKfFsBYooQpiBKx_mS75QKvJDz-1JaNt2twkiGJuzgQu9NAJ4Hl0A2RugfBFKvYdKguP9enbp6fyYtVwLBbSPTOX2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ed7f3d48.mp4?token=K5JHYSXkhSVGAAppvk818pZn_j6yPV1BXlBpX-TZYvQrg1yL71f06rBnq18mHO_onXEO6R_CjhM6CEAoxyanh9hBVOBFyv282N3b_otcL6tQCzx9gKI_ZjhjfjN5f5s_jeOhy6xnk_bpwAzmr70dc_fe-aBAFhglqgYsgTjyjIGhxTK6hWAmxA0uopEbkvt5jITHbOKvEeH9fHg4Rk4QNaiSrooEcFF0hdgMCpTNCcXgU6a7liCF0nZmXKZmCKfFsBYooQpiBKx_mS75QKvJDz-1JaNt2twkiGJuzgQu9NAJ4Hl0A2RugfBFKvYdKguP9enbp6fyYtVwLBbSPTOX2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب متحدثاً عن قاسم سليماني: عندما ترى جنودًا يتجولون بدون أرجل، بدون أذرع، مع وجه دمر تمامًا، فإن 96.2٪ منهم جاءوا من إيران.   جاءوا من سليماني. كان هذا سلاحه المفضل.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79346" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79345">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bd28a2f5.mp4?token=t9QNwQxabntu-1ewGW5HmVrV-WLLtincTtbp0KVpLorSzxeKpk-7vv96gMLNdukE_Umj9-6UbZoQLlT1LKRP_YTrl_SmZLL6V-w8sLhcGce2oDbLXFF9mEUv9InTL_-dmUPKJlx29xyBgs4Oe_g6A0LpPT-bjbzFBlRJqByW12bo4FfgVVOjKjO752wuqTO0eHP8X1y9CRwB1Pql1D3bLLDTxLCH7cgIHcbLuRsxUgnov81Fgw_vZPAOdyjdOZnKvFues8b3XH6InzO3GoeWJzkRyr6YkhLfRjyItcj5uLdDmSQ8uAy1lD7l6rgyq67n9Py9XCeI_wSRiwW8UaM6UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bd28a2f5.mp4?token=t9QNwQxabntu-1ewGW5HmVrV-WLLtincTtbp0KVpLorSzxeKpk-7vv96gMLNdukE_Umj9-6UbZoQLlT1LKRP_YTrl_SmZLL6V-w8sLhcGce2oDbLXFF9mEUv9InTL_-dmUPKJlx29xyBgs4Oe_g6A0LpPT-bjbzFBlRJqByW12bo4FfgVVOjKjO752wuqTO0eHP8X1y9CRwB1Pql1D3bLLDTxLCH7cgIHcbLuRsxUgnov81Fgw_vZPAOdyjdOZnKvFues8b3XH6InzO3GoeWJzkRyr6YkhLfRjyItcj5uLdDmSQ8uAy1lD7l6rgyq67n9Py9XCeI_wSRiwW8UaM6UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب متحدثاً عن قاسم سليماني: عندما ترى جنودًا يتجولون بدون أرجل، بدون أذرع، مع وجه دمر تمامًا، فإن 96.2٪ منهم جاءوا من إيران.
جاءوا من سليماني. كان هذا سلاحه المفضل.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79345" target="_blank">📅 10:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79344">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd20de2869.mp4?token=qf3Ls91PckcGRlCzNtiij0bdvzb8ZLTF3JclfYOAFDTCTZzGL3mWd8-Qkxk99bCkRNJ2k8l1IBfrKuwl9RCIbN3yzthJXTTfg8fx1D2dKB0in9RYRupjurci_md2Rc-O0LYzWCaBKTEOkjaztoMbs3DEOMe5OIbirNcFNWxzUav4Va5VHoekEYQjBAUz4lQO0F7Uuu7HEjVk1IlH5bMSrJPYrrOSPfmbjrXJZrQcjnsmz9w--O56PCcFD843ubpWJP6-q4lqJHpmV0SDQmOq7nX4rPytAwDLGQNh71VWBDrKf6N5RgjjkKmGQmByjNEgePK8S0OWR4dGT85j1wMweQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd20de2869.mp4?token=qf3Ls91PckcGRlCzNtiij0bdvzb8ZLTF3JclfYOAFDTCTZzGL3mWd8-Qkxk99bCkRNJ2k8l1IBfrKuwl9RCIbN3yzthJXTTfg8fx1D2dKB0in9RYRupjurci_md2Rc-O0LYzWCaBKTEOkjaztoMbs3DEOMe5OIbirNcFNWxzUav4Va5VHoekEYQjBAUz4lQO0F7Uuu7HEjVk1IlH5bMSrJPYrrOSPfmbjrXJZrQcjnsmz9w--O56PCcFD843ubpWJP6-q4lqJHpmV0SDQmOq7nX4rPytAwDLGQNh71VWBDrKf6N5RgjjkKmGQmByjNEgePK8S0OWR4dGT85j1wMweQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
لليوم الثاني على التوالي لا يزال الكيان الصهيوني يستهدف الجنوب اللبناني بغارات مكثفة وسط اشتباكات عنيفة في مناطق توغل جيش الاحتلال.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79344" target="_blank">📅 09:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79343">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=LvCHADY_buJ7zi9DNcTu-f2-NfMHF3GQsqdVq_cU2RtqjD6F2gwC8daE-UzGT7iElyfmNFk0lZJwC-qYDNXUK9vUnxgQ7jdD-eLIpyOeUl7IPhX2pxlj56dMMFw1LXNejmWDCcAbGsd-JCwrbAMvypA2RMi_awr9ko5a2_KQ5Ig8uQhWR90atsWJ0AnuOe_KVp6ttIR6FVlsM_assvoGiBvbVgDdwFwT9Meo9MSDDc5QChGYD-oDWZW4emDXgAnFIzc5NLQZyu9yjOzC6xzylv-G_rtnuSRJBxjO_F3ypOYT6vddwqH6mR6AODYLmamTOrR_qDfVDHMY300k0ZVb3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=LvCHADY_buJ7zi9DNcTu-f2-NfMHF3GQsqdVq_cU2RtqjD6F2gwC8daE-UzGT7iElyfmNFk0lZJwC-qYDNXUK9vUnxgQ7jdD-eLIpyOeUl7IPhX2pxlj56dMMFw1LXNejmWDCcAbGsd-JCwrbAMvypA2RMi_awr9ko5a2_KQ5Ig8uQhWR90atsWJ0AnuOe_KVp6ttIR6FVlsM_assvoGiBvbVgDdwFwT9Meo9MSDDc5QChGYD-oDWZW4emDXgAnFIzc5NLQZyu9yjOzC6xzylv-G_rtnuSRJBxjO_F3ypOYT6vddwqH6mR6AODYLmamTOrR_qDfVDHMY300k0ZVb3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
لليوم الثاني على التوالي لا يزال الكيان الصهيوني يستهدف الجنوب اللبناني بغارات مكثفة وسط اشتباكات عنيفة في مناطق توغل جيش الاحتلال.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79343" target="_blank">📅 08:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79342">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REnPhWTrLNO1QITJ1Pcq-4B-ry_D0zbix4l0W7rSsOTa1r6FbV69stLwk05R5TbryN9fe6bfLMe8PrdYgsoYOwSWuVPASTTDZRZsw61ZZXzOAZ-0ajTGC3KjY_AEgoN-kbBoqnQEsvnWil8G_4ieEo88PFJjSLhK1kYUHEphRAhWX0zlZJYaMs2Zi3MWJtPJrfywQ10ThNGHABVF8faD3gwrCu3Rpcq58YGgesaqW0S7KRAKZ-kSRKnCzrRXKVTtgCmTOkgPFZJ79jlmqiECBu12N3kXKL0b5y7l-Hi0xlHdkuLYvWNeLJuoY8k2jNUuJa2Xs8ljXu_ondWk9RCEwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
🇺🇸
انتشر قبل يومين خبر عن وقوع انفجارات في قضاء داقوق التابع لمحافظة كركوك شمالي العراق
وبعد البحث والتدقيق، تبيّن أن الانفجار ناتج عن عملية تفجير مسيطر عليها نفذتها القوات الأمنية العراقية لجسم حربي عُثر عليه في قرية جمبور التابعة للقضاء.
وحصلت نايا على صور حصرية
للجسم قبل تفجيره، ويبدو من المعاينة الأولية أنه من صاروخ كروز، طراز BGM-109 Tomahawk الأمريكي .وتعيد الحادثة طرح تساؤلات بشأن السيادة العراقية وقدرات الدفاع الجوي في مواجهة الاختراقات الجوية المتكررة</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79342" target="_blank">📅 08:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79341">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
🔻
🏴‍☠️
إعلام العدو معاريف :
لسنوات طويلة، كانت إسرائيل القوة التي سعت جميع دول المنطقة إلى استمالتها،واستغلت تقنياتنا ومعارفنا، وسعت إلى التقرب منا، حتى وإن لم يكن ذلك علنًا. لكن مذكرة التفاهم هذه تُحوّل دول المنطقة بعيدًا عنا ونحو الشرق، نحو الجمهورية الإسلامية، باعتبارها القوة المهيمنة في المنطقة، والتي يجب الآن احترامها واسترضاؤها.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79341" target="_blank">📅 08:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79340">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW66hjMnSOihgatKtsgq0zaMI7ruB4kmZ2Mu73hTNJZG2DuWAO_Wv3lWJboNafv11IV8HVpl8IHR0MfZf4XAG52TOgtRZJjWG30ZXTeub_zbvblj9UiVOmj6c3mobCabIoWLKwfKc_sFKtoJgf3iTLonp9-4Ja40TrD03R0Eq7S8IYGq-s_p_Zrki_BNtIyReDkUdDYmn4h1uDo4nOz8r3Lo53RgC7GWo5A_oot5v65T6BOYolMn4HIvvXT6OxeTq6mZ9J96HqrwvlCsp8HnWAD87hXea1vlzsomHSgC5NrmqATCy85_TNOQAMm-9qLQ-yfDum2mgu4tYtTa5aCAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
ترامب متأثرا بتجربة حيدر الاكرع
تم تنظيف ٤٥ نصب تذكاري و ٢٢ نافورة ؛ مراسل ABC حاول تخريب النافورة من خلال وضع يده على مطاطة داخل النافورة فتحنا تحقيق بذلك !</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79340" target="_blank">📅 07:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79339">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7567afa506.mp4?token=vu1mgy3Spuvz8OPrRXyH9yUEis_GWcyYp2cOGai9SDpy0rH9Ub9mBuCxpsnn6Il-_nTGAVT2luSNWGXmBfTCphP8fil8H9fRQSiWSo5KIBiy2emFTUn8h-asLt22oni0491givlM7Gc8QehicecUJ77W69uuBiozKRwAPtd5lBgRr13mK6uX8fxcAzou9c-t7eWGQ961khzb5Yxa0HHPQP3WRKrRIIfDxwTA5HDZVKHp5PqYoUwVV5unWhAd1BggtuNOhcG1q6Oh43mWBWizFQG7tV8y3VohYUKrdMQsr3C_kZJewqcOdRDjRNSdCGvDI9tXyd4ZJZstN_RjhWQadg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7567afa506.mp4?token=vu1mgy3Spuvz8OPrRXyH9yUEis_GWcyYp2cOGai9SDpy0rH9Ub9mBuCxpsnn6Il-_nTGAVT2luSNWGXmBfTCphP8fil8H9fRQSiWSo5KIBiy2emFTUn8h-asLt22oni0491givlM7Gc8QehicecUJ77W69uuBiozKRwAPtd5lBgRr13mK6uX8fxcAzou9c-t7eWGQ961khzb5Yxa0HHPQP3WRKrRIIfDxwTA5HDZVKHp5PqYoUwVV5unWhAd1BggtuNOhcG1q6Oh43mWBWizFQG7tV8y3VohYUKrdMQsr3C_kZJewqcOdRDjRNSdCGvDI9tXyd4ZJZstN_RjhWQadg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
اشتباكات ضارية تدور بين مقاتلي حزب الله وقوات الاحتلال الإسرائيلي التي تحاول التقدم واحتلال تلة علي الطاهر جنوبي لبنان.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/79339" target="_blank">📅 00:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79338">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌟
🌟
اشتباكات ضارية تدور بين مقاتلي حزب الله وقوات الاحتلال الإسرائيلي التي تحاول التقدم واحتلال تلة علي الطاهر جنوبي لبنان.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/79338" target="_blank">📅 00:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79335">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBLCDqBePOOd22SP9uxTgilILxNJ-FBT8Vl853PqNlIfucFgL4USM0t8WEz_nQpDQibPF0ztbrnlInjFLRHwVq1nB2-NxCaAsEBziZYrWdYnIzPK7t7GQCL0aus8FAEKpyPMrOY1e9eNbAaPqGcwigreI5qThzg72O468KRzG4LozKj6MfE0kFp9yo8N_PCrPXoGa6DvkB3LizZbga9j6XpScolmjxXf12WAEwXlPrf_sAydnWzpz1znMB_cvWYLH0F73p9nqCm5gT2k6EbPRaO2ySQ5rJ3_kOfAE2ZVyjTSE3Ks29NUeDnOrwlWymkG5beeqhMhl-ELEkN42BVXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zb-XOiN8yWa4yegv-EMAESkK21lo56xspW14YY3mDurcVP-o6iGRaBsXCBEJ2aCBKjhzr5I3kUe-AdLxVWjCILtAmGhuqMkHrBetXTOirT7YZaGb52dczL8jmzjpOSB7DgWxvNi0KRkhfSNZCIXHCG__epjbSe7_hydhho-AR48Kpet7D52b1QwWO8DxsKO41jLbdwiUPZRH3Tz_ueQendY_zCdZpTNMbgYEbl3nP6XyORBs7JfZeBI2izyUTFeN9K-SQobJqn6WQqMKgojP0qcwd2yNSV_-Ez5jXP39F-Ie02XJqiUkDKQaS4c3WiDL5U5BK-614WvsbHj7Nn7kkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">التحالف الدولي ينفذ عدة ضربات على بلدة دارة عزة في محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/79335" target="_blank">📅 00:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79334">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa1b4e7b2.mp4?token=fBEy51A_JfkpecozNOAuqXDQQrx9fl6G6ILmHnSw9WVbUywip_zF6uBdjvkZ5QUd_5xRmLtAGaMIGMuiU0FSYshHQyNClZFbl8cNMTgPbhcHgcdCpch1ydvacNFdJ3yck-tp0JFWFi6NQgG1HTtyqvNOY8YXPGDZE4v_XQ2NeVe4u7ui6lVP1Qjm0f9pvkuerxHfgC10EwSoOW4do3OnWjL_wR2zyUbiwbJTmVB6wfEqQll7YAA5ChwXHkKV9k7N5fAiurRj-OqsXvqNU9TECue1R0NkQQzMA-jGMuLcd_Ha6Ha7v7C2BWuOmHm94HtA6XAnW2cvz8z75-t0KN5RYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa1b4e7b2.mp4?token=fBEy51A_JfkpecozNOAuqXDQQrx9fl6G6ILmHnSw9WVbUywip_zF6uBdjvkZ5QUd_5xRmLtAGaMIGMuiU0FSYshHQyNClZFbl8cNMTgPbhcHgcdCpch1ydvacNFdJ3yck-tp0JFWFi6NQgG1HTtyqvNOY8YXPGDZE4v_XQ2NeVe4u7ui6lVP1Qjm0f9pvkuerxHfgC10EwSoOW4do3OnWjL_wR2zyUbiwbJTmVB6wfEqQll7YAA5ChwXHkKV9k7N5fAiurRj-OqsXvqNU9TECue1R0NkQQzMA-jGMuLcd_Ha6Ha7v7C2BWuOmHm94HtA6XAnW2cvz8z75-t0KN5RYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليل نايا...تلة علي الطاهر.. لماذا تسعى إسرائيل للسيطرة عليها رغم الخسائر؟  تُعد تلة علي الطاهر من أبرز المرتفعات الاستراتيجية في قضاء النبطية جنوبي لبنان إذ يبلغ ارتفاعها نحو 700 متر فوق سطح البحر ما يمنحها إشرافًا واسعًا على عدد من البلدات أبرزها مدينة…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/79334" target="_blank">📅 00:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79333">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d41c5588.mp4?token=FKDwRChpgUA5byYLU2yUuogJpf2hyy_rPJll6LiiVUmylmxoxKIs8SZv9qrXH2t3TfmTb-yJQf8FlZVBqq0F3aESuza6Zk1BZp-b_ExlOd8UppmsNaYQkvTIOvmApxZON_3PGAdHQvPuLl8_MqyBvOlUtKOIOPQXEbergXmZqGH1FEiOfkkUllqmxauf6piyptdC45jxDWIq3jercH0_oDowU_2OjhZR6u2b1W7GL4CIAyBqRfUPjUSEHX6oHonEF4hGndNhw79kpkRc6p9IMESW_VbRnVtn3dMMVc6kyEIK2221JymodmIJQo5IuhfVVQC-y3UpNX_qcmM9EaA0lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d41c5588.mp4?token=FKDwRChpgUA5byYLU2yUuogJpf2hyy_rPJll6LiiVUmylmxoxKIs8SZv9qrXH2t3TfmTb-yJQf8FlZVBqq0F3aESuza6Zk1BZp-b_ExlOd8UppmsNaYQkvTIOvmApxZON_3PGAdHQvPuLl8_MqyBvOlUtKOIOPQXEbergXmZqGH1FEiOfkkUllqmxauf6piyptdC45jxDWIq3jercH0_oDowU_2OjhZR6u2b1W7GL4CIAyBqRfUPjUSEHX6oHonEF4hGndNhw79kpkRc6p9IMESW_VbRnVtn3dMMVc6kyEIK2221JymodmIJQo5IuhfVVQC-y3UpNX_qcmM9EaA0lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الطائرة F-47 قيد الإنشاء الآن. لديهم خط التجميع يعمل بالفعل.  يقولون إنها أعظم آلة قتال تم تطويرها على الإطلاق. سنكتشف ذلك.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/79333" target="_blank">📅 23:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79332">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqLWIr4j_hlZnIY0X92Xur7xB6gcW6r1jOhRT-gajrEhi01L-0LxOWAKPkwbHnfKV2LQYymCurwqMlqTmxF5AFP0H1axCHuT4g5-cRvXw39unNXtANmkKgzuvY9cn8mnGpGJtDasJ2fomxaz0L5t0S6p4QYh2j7Zq8zguWbn2LxuQuM3YpqkdM55G8dR9UOVQyk-HExxcQ2oO20p4diYOMd27ZCHX4I8hEYXUeKIIz9OBki4rtYByCEE6S6CLp_HcYsLhrJgqzCv3g32Gi9imiqVl90a32bFjuNCG_82r0H5fhWNoBHcislytHSvimCRjLtj9es6S-gVrX724jXIzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماع دوي عدة انفجارات في محافظة ادلب السورية</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/79332" target="_blank">📅 23:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79331">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/642865aff3.mp4?token=uyzW-9KkLXsITSPeiagyLtcHGljwvFtrfL8-jfgw534SDiKKShRz3eO-niCkcjBR-4WTOlJTzj77qAB9PXKER01P_JnJZA-g6hcXoQeBJwpV4hq_CgIg8N0lYhj4vRQa0ITIw1TwnrDpKiyA68cmf4dNWp-I7GvZ5r3HQ_5kcQKR-yBNNH2vX3hBWLl4x4mngC2TUUs07i-UuYj6TbXnkkwoU9-tHBsDN3aCkqbAI8gmkRR9chuBDBhNwd5qZIUMLrskNuZIUDzbBojn1S5DVjJYh8S5w6BPQN7gu3VixETErGts4wm0SlIV0RQAf1lB9jVr2mOwPajcyrr6XmOkgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/642865aff3.mp4?token=uyzW-9KkLXsITSPeiagyLtcHGljwvFtrfL8-jfgw534SDiKKShRz3eO-niCkcjBR-4WTOlJTzj77qAB9PXKER01P_JnJZA-g6hcXoQeBJwpV4hq_CgIg8N0lYhj4vRQa0ITIw1TwnrDpKiyA68cmf4dNWp-I7GvZ5r3HQ_5kcQKR-yBNNH2vX3hBWLl4x4mngC2TUUs07i-UuYj6TbXnkkwoU9-tHBsDN3aCkqbAI8gmkRR9chuBDBhNwd5qZIUMLrskNuZIUDzbBojn1S5DVjJYh8S5w6BPQN7gu3VixETErGts4wm0SlIV0RQAf1lB9jVr2mOwPajcyrr6XmOkgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب: إذا كنت سأضربهم الآن، إذا لم نكن سنضع قوات على الأرض، وأنت لا تريد وضع قوات على الأرض، أليس كذلك؟  إذا لم نكن سنضع قوات على الأرض، فمن المحتمل أن نفس الأشخاص سيذهبون إلى أعماق الكهوف. يطلق عليهم اسم "الكهوف الجرانيتية". إنها قوية للغاية.  إنهم يدخلون…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/79331" target="_blank">📅 23:32 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
