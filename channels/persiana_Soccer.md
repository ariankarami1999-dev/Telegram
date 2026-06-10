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
<img src="https://cdn4.telesco.pe/file/S7F72QmCcMignJQwYJ957PtKh_B6xkSLNPTi-Xtw1sxwipbJDiawWGBOtKlnalxhjy-WbOgjouz1wX326XOknVklEk58MQA0CmmYz7XVfM0Hs3OSV3gk458Bh5olzdiwb3p71Hp61iwJxufpbM_gJ6e33-Bvh37hOawS4kcFRmajkPWRKjsRqDcZn7MmBE8dAIr-XyKm5YvKIjJUilx4UWrk3uYVPGFr546HVnd7n_yfuXi3VVxckwL-a53UqftUG_so_VqP0ZQN5EtLjLDMkLfjFPqT0t9K2dtrZknaC9qqlEBVSOyWvj4SJ_0pL2ic7bj0_VgFSKSB8Jz48wskqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 179K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 10:30:37</div>
<hr>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHrqAePgVYUIwz4sN0O6r908xzPNpcRGE4mNUcfNqO97WuNKPY1kRINNJuja8K8moyWVLaOTCxtD_ABTMehnG05SARHNF7lLRBLK8cRk1khskTzUFpvXtUPTGscpCf8o8byjPPpS_t-QMnaVqV6mEZmhH3uloPZoC19ZfqQurgeasLmQUCarDnAwQeHkTP4-xQwZ7hmtt8y0seIOt8RSXuN33vvK14CMHbB5hW49xyyVUz6IM-1Kx4KXU4KTcbKIRPFer0N4qWBbKBVN8tG8W8Vo2de8GEWYns_DylxkUZSrWvEdEpmhyRS5naPDhR7Wha2oVDns9rPDZSI-IqWJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل گرا مدافع‌تیم‌پرسپولیس با دریافت چهارمین کارت زرد خود، دیدار مقابل ذوب‌آهن را از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/persiana_Soccer/23101" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=bYRaBCr6-i7PoEepHAp95bdi_-rWC4xe6gBobb65RJhrjHW1v_cz_P_uxNa4SQOnfbHI8KFA1HXmW01XZauBaCSEDsvpdfiVTYtRaKWeCjHzcCv26C8kl_wAnLsIvT3w2pvCcSgV--M2B4nzfORpuUxO4kv7pWe9oNsQG2c0cXpdUGBFaAborq_JrrAgDH5lW0Ego20XK7Luh6GK0Cc3rC31-A70rW8QRMm2ACU8YiKdeb8odTszOsECh58s5fkJL8aV_YoQQWH59QfuXG3feEqGstLO3dwu_A8Dwu2zWOVHT544_aMwsu1yXqpM5sBjyhCAHbMgawidJywLyy_JSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=bYRaBCr6-i7PoEepHAp95bdi_-rWC4xe6gBobb65RJhrjHW1v_cz_P_uxNa4SQOnfbHI8KFA1HXmW01XZauBaCSEDsvpdfiVTYtRaKWeCjHzcCv26C8kl_wAnLsIvT3w2pvCcSgV--M2B4nzfORpuUxO4kv7pWe9oNsQG2c0cXpdUGBFaAborq_JrrAgDH5lW0Ego20XK7Luh6GK0Cc3rC31-A70rW8QRMm2ACU8YiKdeb8odTszOsECh58s5fkJL8aV_YoQQWH59QfuXG3feEqGstLO3dwu_A8Dwu2zWOVHT544_aMwsu1yXqpM5sBjyhCAHbMgawidJywLyy_JSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
درجام‌جهانی 2018، آلمان، مدافع عنوان قهرمانی داشت درآستانه حذف قرارمیگرفت و در حالی که 10 نفره بودن کروس دردقیقه 95 این شاهکارو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/persiana_Soccer/23100" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇧🇷
👤
به‌مناسبت‌بازگشت نیمار به تیم ملی برزیل؛
ویدیویی ببینید از شاهکار‌های دیدنی او در سلسائو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/23099" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeHZZsyPEmUtUTfFjAoJp5VBeOVbfotiLxbDsCW0OvHPHMBFqISgY1Z_aqmvsYR9Xr8Bveq7GqfwLP-fQJxgY9jdj3E4QM8RpeHpEtFrlJB8QGef4vZUlBhUTZDc-i7M8VVpF1stdCkb0poYoYZAn5v1StIPM-zUjrM_nI0skchJDoP3wBC9p08aBjASGOco8m01CrDwGtaER3irj97pSuEAiWOW4uv_KAcCLHpO6Rt_rKVlVEQ0uGNMnEYIDgI_ObTDPDtHuvRnt6U-5tQ2fNYzvXGQjpc0eoWbGACDp8wxXie4sviYwTF2JaVmDXAUB06vYJXnB49J_kAemntS8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی جوایز تیم‌ های ملی در رقابت‌‌ های جام جهانی 2026؛ قهرمان 50 میلیون دلار میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/23098" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kaja2h9isXmDyyu5UtbBbRKXhEJAjCzPUAMDFy6nbAe8Y2rbfIbEwyKxkM9TTLwv9H206MHXkctcaXff325ByE2r6GANLmhynEhSUgxxNY6_zHjV3YMlNEsVQb6ZKVlVfPUSJ9uM4qkHDv2Ml5JE2VaYh3v0oJ4mWBTka3qhcH9RUO6d9Zyr4blriFi-lxHNv8Yg7Y0Dv2UOMguHmbA84ylYCWBcAyN3Gs9aOJO1sWQ3C9azFSitsUu0GsRLPRUPRUA7DOLpcqA-LKHn0W6EaTUkvYIYZfmBZ1oCTb1CDkeHTn9pMNFF8Jlz1NZwQULzG2gTifvGO2HneqAZiEnBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان:
بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/23097" target="_blank">📅 09:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=JE7pqzMyZy-6tZZoRCSGi5UMENG_1sePkofZ1Za0GMz0cPvK4mMWcEDOqjYf3jvd27rJJvLQ_COqt6kPjq8kwHzT21gLk4wgFMh73PgKnWVcNIsmj_lfJkMermiOIDGdqKn3BVpCQM_1exYFOWS6fN3gLyxkQ5fN_3uedn-n881ZtngdjqK7Usx-UMplxRjFiHlhILFcE-wr-n5tHcSepK-cJhf3ItDSucOSUzSxVlJovHllg_zNfV-pK_AfbNfDJQlYX0XWW85ahOHDlcUpzh-yR-8JytN384IW6WhdtWbjxoRtaXSNecCnaiulRwBY4uF2cW2kYyFyDmfKL7d2TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=JE7pqzMyZy-6tZZoRCSGi5UMENG_1sePkofZ1Za0GMz0cPvK4mMWcEDOqjYf3jvd27rJJvLQ_COqt6kPjq8kwHzT21gLk4wgFMh73PgKnWVcNIsmj_lfJkMermiOIDGdqKn3BVpCQM_1exYFOWS6fN3gLyxkQ5fN_3uedn-n881ZtngdjqK7Usx-UMplxRjFiHlhILFcE-wr-n5tHcSepK-cJhf3ItDSucOSUzSxVlJovHllg_zNfV-pK_AfbNfDJQlYX0XWW85ahOHDlcUpzh-yR-8JytN384IW6WhdtWbjxoRtaXSNecCnaiulRwBY4uF2cW2kYyFyDmfKL7d2TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/23096" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=lalrzfrNTtIlUTpPKXY5RF2eBtgauJCSULPXSid7goDuoNStlmBZ4plC4oWdjThhDZXt6gRcaCUBjg1ceY8APk-gng3ph3HleB9UkcANr5NcCEAkUWcUWz4pPVOahGBanXJedGngwrexfEXuecgl7U_eaPDZCNasjrX6H-tfi9pLC2YANxMro72jVx6-24N5j6V4KZTClPbxu0-TxTzIq0d4xQFEmtmfOS-auzOvIn3_m8QqJsVV-i6bxckZqxpaCfJ3-JX5rJqt4nP5YOjmhHThGPo1Pbbpj0kMXJrH7uTbXoXQA1NeCChf8G-XAs_GHorFJyj0W6kczWSY7woTHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=lalrzfrNTtIlUTpPKXY5RF2eBtgauJCSULPXSid7goDuoNStlmBZ4plC4oWdjThhDZXt6gRcaCUBjg1ceY8APk-gng3ph3HleB9UkcANr5NcCEAkUWcUWz4pPVOahGBanXJedGngwrexfEXuecgl7U_eaPDZCNasjrX6H-tfi9pLC2YANxMro72jVx6-24N5j6V4KZTClPbxu0-TxTzIq0d4xQFEmtmfOS-auzOvIn3_m8QqJsVV-i6bxckZqxpaCfJ3-JX5rJqt4nP5YOjmhHThGPo1Pbbpj0kMXJrH7uTbXoXQA1NeCChf8G-XAs_GHorFJyj0W6kczWSY7woTHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحنه‌ هایی دیگر از موزیک ویدئو شیدا مقصود لو همسر ایرانی خوزه مورایس برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANE26Jvjlji47TEnt24oP7NKGc4OJpokUeBujT-_NtmB37TsLA4xki6XNgOB_4FO6PU6C4l3SPbxXlUUdOHUejN_cXN3JEOp9Yc8GQWcm6fw8SgCLhKgrDO-Ey2KkZPbovuWJ6veguacRrvjnCNljSWEsKZ6KP7cEaRAP4BeRJqiw7SEzshcqhXwMUHAV4Y3Y4Q9zxLndxoG4cR8w-W2y2WkABC1RkZqeXCsbmfTonnCMVOTiLYzgNEOtHZtDvvLono2pL0daM-WDNseQuRmirwWX8WJoL-qG2nFt2kUE5mHEZhNzZbmJIAPMygkRqeKSkyeuoKOEjxtQe70teRTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doe6HpzWEAmBSP9CwHU5QfPf6ThasTg597v4qfLe1S6TTzTqtxravLTib2eTO9czTm2Ah1UvFnPOy0mpiK-AUf05suGVrmKgm0DdSLxdcbD08YpFl2I7AxV5PrRShH7IdshaEONBsN2UPhPMr2ipUbP-9FZ62T2STibAwVFLsVf6rEaFRjwwtRYizxzw2gPg29tIu65fwunauEEr-RoaMfTNMLBJc0wDalZmx8fiHoKcct8xitwZsya_BmV5ZJUMmuBu2gDy40-L9jdB_uA9dLBUGbIy76tqVu-C5TCiIN6n2UoZgHeJRkd7fcLUhxHAgCnSYlCu3d2-QLWIkTfKXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه تک دیدار دوستانه مهم روز گذشته + برنامه مهم ترین دیدار های دوستانه امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=HA4d4fv7K-1azLzlgghx3fgS9uZ81sy0dnRWZKbPPBZursahM6Lm1gu65vEsGRQ8KGY5Q5zu_bVnZ5xhK_6AFRtThtnUq8N8fkMKX1ifQZkVB8YNoq983MzZPAhpO84WjNARuv7Msk9NmnRqYwMCZW39yYO6ILpvHy29xxK6jZDAdhTDRCFOtEYsn4nt2lKX9NJJMZyW_uAI9eVcxgX0LAKrpn_x-62nVWnT0IwEwzv9Ywd_JeHoGw-T0TtVLf-mcSlCI9HymZmmgcutsk1P6EICJloTbP6nzeP_hVq0pt0Mue27b8D64EqA2C61sAUMK5tFYtjc6Z0CbeRD4qUZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=HA4d4fv7K-1azLzlgghx3fgS9uZ81sy0dnRWZKbPPBZursahM6Lm1gu65vEsGRQ8KGY5Q5zu_bVnZ5xhK_6AFRtThtnUq8N8fkMKX1ifQZkVB8YNoq983MzZPAhpO84WjNARuv7Msk9NmnRqYwMCZW39yYO6ILpvHy29xxK6jZDAdhTDRCFOtEYsn4nt2lKX9NJJMZyW_uAI9eVcxgX0LAKrpn_x-62nVWnT0IwEwzv9Ywd_JeHoGw-T0TtVLf-mcSlCI9HymZmmgcutsk1P6EICJloTbP6nzeP_hVq0pt0Mue27b8D64EqA2C61sAUMK5tFYtjc6Z0CbeRD4qUZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcUtERQv1AgZCIzvtSRW2ZINcSj2t_Z_gK9XVuiPf-OvQ_fPehHUcOkAgo0CFTVP-MJt3uymcTJZiZQqf9-x6Ro1hijnvbIfJjRDyqUMD9S4kY9aWbZWxz_yOZaIZWz-XYs22R1Pv6CX_L443FWL84FCGSFXTBAPyX29EaVw4PncBvrzvED7SzIhjnTD5-WdykvYQdV4IW1_cEf2bW-1u4w-SZbtKQfh3VBaKZlsu7Q-Whux8QOeSIMa4OOslJeVu2OmK_ZAD0Qyf4_LydKec_dPenNuin_ZnvI1p6Fh0QRCHStuRIvMKO3arFA9UgaobWOuJ5F9FwwFqjAf2f4tVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bz4a1_mlJug_vAXN64iUKagOWQDlox8OgPY37iTjBLGm75T9WWabPC594McxfjtVriZYy0rzLOER8_VAUQeMaGRsLUzSGWt4qASPe1-dggs0cPF_UcGfpp936FVh6jtJP6lbsU1OicTaOQDWrCeItb0s0eVdY5oRQeGG0XW7ygGGYUMZeCO8uK_00l0hXs3kSyltx_OBjgbm2ZDpYc2x7nVVKSOQmc4twtcrN-QMjN4akG6WwTUhOV1FaQ34C5VLHALau4e6WcpcoI0Y4MiByV_NvQd1eBZM7Q8xxAWp08ICett3eHZlY4vilNggMLzG87oeup5NmZQ3_ltm4Vjytw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌باشگاه‌های‌برتر لیگ قهرمانان آسیا بر اساس آخرین امتیازات کسب شده در 10 سال اخیر + پر افتخار ترین‌ تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfeD03qy1tcb-6wbXOcoz_OBjZmtacSKMqVRxY8QDwNIZpNFMpyRAKWWAQQ6eG3khOREu0301xJUSMo00ZVYSd-zAh3l4JDEl8Dbwu6lPsgOeoRLWAGJK61KTbmTVUbUNiT5t3Dh3-kb8iiSidlpQSYhfkVTqZMJSO17Ez8s3xu5PsOH5ZuT-cxHnIPPPqAYkE_oplROqjZd20FGecKFGmtRf8-G6TV_v9p1tkrm7q4-_Pc6hjcldlXEBXVmJDQ7DvsbT7wfUsIQzwbBydy6Nu7_gF9z66W1oPD0ffKteTg5bzF_n9ymcby_YvvP4BzZ0xjoh2mvLxo2e1o4aQacyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5366993444.mp4?token=n7p3CH5ib-APxWqDkHb5SNkxDiFChDRFwsUXIn4OnG1WxclA94ZYA6HXy0qYTAU77QWf39coUhAguK8d9IQJ-EeXLQ3_8c1CY2h0HtIHvkN_GDBjd59FAYEzZR8CNNtgi60_70Dv4dEP45PSjYF38A7leHkKyK1N6ogFpKusTj-NkjmketPcErozg7fXXj6iHC5l8RKqY_TEz6sd1tXK-GSsgKBnMp4FS9gbKCAq_Bq8qwUFTKRoe1ALGxUxEU1SMD9QAAMg0Fb-u0pfYDoAUAF104pKxcqgV1yuZXbdu6iSJRCeJCm168sRWcg4JASiKIZASAmagn5CiK8_izVGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5366993444.mp4?token=n7p3CH5ib-APxWqDkHb5SNkxDiFChDRFwsUXIn4OnG1WxclA94ZYA6HXy0qYTAU77QWf39coUhAguK8d9IQJ-EeXLQ3_8c1CY2h0HtIHvkN_GDBjd59FAYEzZR8CNNtgi60_70Dv4dEP45PSjYF38A7leHkKyK1N6ogFpKusTj-NkjmketPcErozg7fXXj6iHC5l8RKqY_TEz6sd1tXK-GSsgKBnMp4FS9gbKCAq_Bq8qwUFTKRoe1ALGxUxEU1SMD9QAAMg0Fb-u0pfYDoAUAF104pKxcqgV1yuZXbdu6iSJRCeJCm168sRWcg4JASiKIZASAmagn5CiK8_izVGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
جام‌جهانی‌داره شروع میشه اما همچنان با بزرگ‌ ترین غایب رقابت‌ ها؛ تیم‌ ایتالیا با شکست در مرحله پلی‌‌آف مقدماتی جام‌جهانی ۲۰۲۶، برای سومین دوره متوالی حذف شد و در این تورنمنت حضور نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23086">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XevjfzmXyK09z3O4UBkLV9jw-ZNxGbk3TExdXVHm_aodB90AF3aWc4D_DKmpbim6t43QDQzslRmN8zRrmZbdYHqPr_OTbQk4EuibAub0zwyEco5fNR8U_uc-RriCcAeKTL34L6k2rXv3hw2wSKeK5rXKoFUl8xU8d7WQEueSC_Aeb9G2bjWAQsLrHRZYSP5dkf8ADBwD5UaawiAX_P8BLUVyigZcQkFLpqBYeKGB_Oe6ey1PkBf20xVy-L2mFIV9ygJ8OQK55bm-xn_UrWRKNqGcLSvKvLNaCHKeoT3qAfRfE6KlItz0KJX3qEqNC0FbyzeI9Y8YPqWVIXYvFI6AlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/23086" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4CmPKkCYd1EIodInutxIk7_QSzFT_GjyZRWFluSl4Bqc_lXaAq8Zk1w-ENeYirS8g8piNQ5pktsLqmIKUcF510RzwY0pN7GtntIonCagxAeO09G3wHbT2xMNQ2iTpQyVVljuRFuqb_IsMvd3GHCF2G6pm2kxNdZdNGwQFTF_YzBSVanB78C6Zew1fWQV14w0JWBi8GEJxVx-YeOHGLJmMNUqSoZdXNuRGn3bwWtP-ykjsz1zLJDNKfcrspNTwT_2aCf_FLydFvmeQVjcztEyAhaWrFao1Ta7cgj0_KPXC93TO1uu0Yx0djSz_Y8-S9GEt5RUTTMkeM5NwGQ5xpLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m84KOmFAZll9W9oPfFSok7x24ob16TLN10dakY8CyH2KQKKQPVt4nf1RTa1TBLd2uJjeRbbS0z9gZbfEHOJ_7KIiJAAY_c3er1qmt5DrZD__2M8XF0jNC7fnd8M0lNh7Z3-2oQA9Sxf08krPiIMUUG4y2xo12oDWxv4bHw1OBtRqN8jp9kN6KlrOpeGWns4o6lswjH32MiXfCUwQGwE24OJSUJlOMinnWz17x5VKZ_835VhLP4F-kqPtJ_vebZEzfbnW_tXsIxsL6HtzADy0_iEI2JS9AJfnY5dvRd_s9tBt8FgChQYkWKkpXMARhaNjaEPWrQFrucAsa5ZxNzvUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8NnlobTVtP38jBfCiSwojBEw-tg1KADprRcAnZB_MpR7uReafHbHjOU4-c_-kICrGdsaX9BxjbBeigLPvwXFAcQe4W9POOMjiqfz9jca7tIPsxNEARntfmzmrcnvA-RT4qAkxVSpd_xauUmGHZY1ykUWFnT1g-ZQ7JFiENr39LAXY6QSMfA7mhi46uzM5FxowoQ_stF_gvHUm4qWd6bjfxl8ulbSAmZIv1NX5D5Pwt37xqlFnzaCe6qZCxAcUB-ZVADx_9hTDddtrP1cHek7tOPatS4_2Mm1MSP0buo-T3m62MQln76exJPZRD8IYuKD7Wih5zFMRl2RNx1JsoDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAh6RKnCrrvLOXBQtQCnK3XQGOUrrUB-J87LqMU5nFW75xi01zPojgY2bIp1I0h2aoVwRcLiGtbxq7z22Jj3CRvN94jJGudylfwAY2fx0GSHFddiLSBMskCM26RBp6hCTn1yNnZE_nbEn9kBeYstZuI89VjZG42sX8uFmfEYM10EmG5PZluaKXY6CnF2aWOvFRMz0zZjdmo-uHuqS-0M4eo8RDvROq8Amr-8Lf-_kMbNn9LF-HS7Hn0TWW8e1Rwh71H2eB5QdTEa7syRi5DO_MZNQf4Mg356d2JpPoUlGXNaM2eOPODDD-pZityUhRl8j06BQ0ylBAP2vJGAKeEjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye3atitMNV0WY-XZq5shaSOjS8QA5HoLqWlKs7gOOI91xY-ULMo-Wuiydu0v_3oasepdc-vm1o1Ttj-Gprw9MtfpRFzYlWEmrjh3OfAVL1KR0CeqCwGRyQIrcCeA-XJ8IYD7gVn9GWqeRKd8OVaVJIYCuSIHezrO2yDS3ThGO_vXg7ZFVKOF6auuz-YLK8eRvcYqi4qkjsm9VmXBV-8V6sagoim3JFmI5BxCMmAWwccJYMM7zzIumi27o2L4nkxZH0PNbw2iiLxtLAL7SWNq-7NoWOdqmZvkn2Rqv5whDHPbfUedNN4n0kbeFG9C8u3G6g2xeR3rThFnbI8iow0o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Plqo5dYzzZn7C0XERP1tJjpRAE7fNuxvzIrzLkeqba4ol3peoN5tshFzSu65oL_qATS6q0ki2Ftjp727Geelz7XaqpIsGk6ML4K-Ux4mmikM-gI4T9eZkpUPiY8ebcumEJKTwraT5wP1kh9Tb5qRYjUp1cYYTWYx1AMIR4qxI3y-F8EMcDQBQQ23oImcDsIEF0TDFZttlcHcssZ-1R5SlU4rL7ZnN5oRwvY-NSXKaNgSYJ_oXnKLzr_MnQo-y7oeZhH-wd0VrmGOl-O3ZJf9hQJXAPrIecKJn66s18YlywcyddLFwBgdOPg5QoPse2gYjkpzii1REqGnqvC2_dtMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLjS6iW5XOmFxeKOiR4Qr_MJ3N7LeMaeOwzTDWBhIcJ2SaEgPEWCFDvKgjJ2g2nu2sVnhMTEk3UGFDHlc-9no-y2zfAV9SfIkJXNCl8B57GIO8kT-jkXHNm-tWjcq0Yw0zSDTIlSV_ZOlf0giTgtKSW6IXmPCJOo9TP2rX_H3dUOzlFA7aGW8R0kLIjwupvDZJ7Hibaaz-nFqrruIFUvHeBdBA8PVf-9deBdkb2KejT_iAseyo0kV8CyAAZnazpOxYin8FSWRTSXCQcLVDIE8l3VqfgErbKmZxiJ-7e_IkaBSXkY9OjjTOLcLEtoM135itOWypxSGO-CN3sUl6eF9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO843QxLpW9tiA2D_1aYkZQSz-6q--JIEMb9MuEYsEcD88nPOgh_egqKgwltuFc5u3eSpr_64VKHjTcm1L0h5ujTQKa5nRUAnV5A8PZ3DJtvu3UuPTHGhO1yo85y0dhAbklw0ElDDL4QMJo4zO-Z2OfH_oyM4nza-bSB08hV_EnhB2qHQZ_NE3mMtuQPITBMjS2SXTFfrN7FFuvlk94vvTbsFGF0laofJOTJ6yWyMqhRoKWj2D_JJUEB9Ng0aWoVLvVZrHkc3ZAZg3YyO5m4qgJBha916xzyl-4aQocxFK_iiDqtyVndLJZEqc8rO6xErWwyYNGgZpGTklWf92WqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER3FZL4ywMZE5rFgqrSGpx9UzGaiZhYSf2QEO4wG0u9x5YLaNGSNTdG5ImyJottFklcDg97tP9FIqDpu1nqzUOhNWRcrSVl_AvatwpeV0AqNUvJMOsYOOH8MKt3IroItqIstSk78PPTHeH2z8z9BgYaSfwLYIX8m--cSdxnvyb7WlzUggk9qSgwqv1-Wrg2PWE81q00lq16E-09H7x7ucSzLaewe24CWjKSU5fYAzLXI_96TQ7EVz9iL1WdLkxC-B6HFUKTyNThq2HmzYhXdGW4I9hAO3vY7b_OK_rZGfNcMQbU-6XH46yBdkeJtbZEJFW_wmbcxudXIVf5Pf22l7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUXHXJennlwGp3PUUgx0uPtspOTR0zFxEoAoO1SyzDGDjS-7so32S50sYr_gr_Ct3wtIbEG5_1fHtrjYqn6qefPn9aQnxzasVsqGHqiw9ym2hyPAycB8ur25QfY9IaQgIJtFIGpe6R-t2NFr-gvkRvl6w_ZH4oHYEKuijfvgjl0r6XuMQdNlGZJ007XAbASiHr2EzF07x1AslMoT00UeFRLiBnKoWU_wRcHHCSRcephSHAH10rFrQgYb1nTsXijJO-8BedlqLLoAMI0a5rYjGjRZzavUfJbzeiS0ZW6qMYIp-q_JQwZ_B9t1J7Wbt0zKFJRTof5LMffTGfXdFrkuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAdZGmKire8HXQYUqgfjTNTsy4OXXxZKkKL2HjBuoywfYDXiUFBZnpxXzJhCwzBXgWFhNWr5venFSpinDQdNXmJxiLZQMjSrOTSIFYGcwnyVntyWcupoKFziboS72B6KwBWpgYpakn4LT819wTq5jpOvoR8FneF7AevmeLZivIx_CybHZaGkB8XSvanie9-77QG3nMEczBK8CJR6ZlIuaimIds2h_v5PsMRpQLkDt4kDvu3R0OqbHHAd5ppROymfsL-Da_Q5TukKm0tEOKM7_2NXi0l0Hc8AGRqZWrAYyC5WL0YO2ddgNocc3ITxXi7Bqjmtl9F0S9hmTQDuoh2p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbtQpMFb69pQY29TrKXa38ea68p0KD_Aq0eKWTwUetTrvZOIsyLYcvNVHOV_hPUqQiVnIt_CsG2qYZC9AntLbg6I7QI1qKjU-amS7jO9olLmhUwLQvQMqGgOqoU3wMGJIheqw6BQToMO10l4CzszTxnDuNTWlgK3Zl5oXZ946WWqNDiLyjad77-EX6rTyCrJRyEQRUPBqS2ycbYHZPJDBmeO37oaxF8krvnc8jeEMaXzcO4IuElJscABbFj0lOLiA4xLGmsKA9-02cZO3wemZS5i5f6HXSDjOo7kNR7x5TxqDHuhFQyWqT4DUqu9z-qo5XxY9POsldj3XuBsRaLpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZejtzpaI82aaI1L3M4xYLVuLelSrmSjbIFqzyo7kmr5SMXITBCuamZccrapxWXeAxVjB1HtMgkbjm0K83xHaenG8jaDRZsOc-WHd-NA_8ITGUrJtx4yIuOUq_DmvoFj1fgl3Zxvtm9iAkgVg8STLvERcqY2wAbgXwJOax1EVdhROOlwkOHZMVinLdD8BfL-7HxShlxZkxsrLJRA2FWT2QiolbcFg7NHy5VEVPu02gHIwSiV9KYymPsejDrhqiGUjPvFWY8IVeBfg3uFF4q6RfOzK4HjdQqaP25I26QhNQu9_pBBiHfGnwFmRa7xJ_EWIPifnrpB-I1hgQFAwDZUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJhnBDPI5iIM6C5gm2rD-56UlQDdJazck37kZ0RqTrfnYlU_zCkG_6SkqwNRexll87dcUsmhz2tx7N7jqLQDgKyO9HMmm3Ew7fw-uKkhVcyYuhSEk0iisP3k1wxtMRZPiZz39JnSKi-NyNeB0ocThvxyQUng08q4j871VXJEDOBnpqsVGd2gkLVALslCAw2mebAmuC9Mprrwu-e62VAw11ig1wl13vNFOCd8PtMkM5KWAqolSMS5SH-2Ek8XDMYLsi6krvTGIFYkSCq9jq47c-bffgSQNkjKutKKTWCqH1BnnZA3-jI-1aOwduVbt8go9QhVAzmDeW574Y4UnemP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5NXqAl42yoLBK80Q-OdoGd1zuheAsu2yE5NE5Fnk5cUiioEx5_5dMH3l1SW-9IYeq-zMd-XWtAsLqQfT3bA0m-KeeReawGLj_My6sX51V63ctDoiw1F1bBpqNOWUBtvNh8Q5y0WmTswNzjmuAK6c3PrH7VjrwYjt7xbV_v6sHtZ4iGodVCauqUjcxBklRgglJu3FGFuZ-1Aqd52Artyl_tj-t67QRymBND8Bm87e0y-5eEq1IkQYvGi2WVy9rpZBqDvnSbl5z3OBG0qUhLpvNRN4vXkTgBIWzYcIbEqLerg5l_-tvXZTbFdjE514rV0vpPri99t519RRInyXIIWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUpPcmgf9sxhx4C2q1xqYlGfzsohmO4roNTOku2X_UjcHcV98Q2QwaLs8_B0ZfrtK3AB2tKPV0hF514ySnVeuVFmWvnhDTwi1QoO5gAfbOvgZAvX-f2sGdj9pu3GZy3jF8W6o4faI6D7a8EZeIJZrmqaHYF0SsKkGhYZuCLUZlUgCHJIurWIOaXzZN5mFygP4Y-QKjuOcvNcvnzP5lhRikHTkSndB1UfEFlR4vdhatxoripJniLFQQ6-dyZ5t9pc61Q-cqP_Kngi7T_3mzldFMj0xTcIeopnX8eZUgdG6rTdkIPeln17IvTMKmx1pYcdud38FTLgKSz2YMxHqsG_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsF4ta2b8NiaVBaZC-7TS6WPMJR-E6kII_i4vCxRfpCj2CNJGt_8e15oEDLwgugjhZhqnWgRVw-beNAy90b9lD2-Oj_vCRE07wyV5lG1W-WEgJqu9n7cFZyo15zgJsKMwGIB8xjR8BMMk15BBQyOlLwX62SIWe2TJ00lQYiWFPmxt2coRQuwVrMTC3BL4jrqRixxAdFv5GWT2D6rMr9PIbKbYyQkzLwxLFGNRno2alOJWKjWBVX7bxx3b0uXZ1jO3enIr61cOApZV6qpnB4AsQfNXqgqiHwPsyQlD6oWQTvIQuUkhLz3KHEoIY32iM9_xrIaO9L7jezTQnVgEe84ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyF-7Z2LvhwUKK-Nny-1LCkegydzNKrJDJcUjpclvw4FTdsm94KkIyiizIrN-L462RBPeScC-pOmk2eQS3_gMsaZe15Xw_Foi8NVrUyi5xsa_Qj4PRLqmNKi-qkIng8icRbuQDqEtRo6kQCoctPzfG_4h8O0khe1pfxQN55mXxRtszOP_b-e86naHZsSafGBz4KyF3yGjOoZ9RZjukVvO40sbGg25BYbpTJMwIX7jaZMvij-1VTxCzz_dYmOrnLElhrKlFVymSYS4xv4lH7Yxis9wqGk_9X8w3b2dAB7LmrXXyDESnGFhnDZ_M9HODRzUgtCsPisD7m94_DDFGzTvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp74hPxsVbXsmDwIUx9pm7UbUrNYaROSdmDMIHFFqqL3jREpwkoVF5mfi61Mh9GKR_uMiLsK7-Jww4lWToJBDdtCzsfAajt1d6VtMdj9HAXZMSi_rOvvBIaic3H7AOAkVgiDHuFcwiH9BR18LiDjDdTqhjupVLRNRciavus97q35CQ0Vyu2q54uJFIbXa3pgEFRWz_BmT5ms_7DoHBDkgpDvyaB8p-uwa5evW9KN8XvnQVqdBEUQrY8PKYomv0JhuJDI2C34iTjqKww8sSYsYluepBpkD8WxclWsI0nVhNu_LOjhGPTK3KxDm_8H3CCS-0MbPsLqluO_JUqAkA8BBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTWHWs0hptYdxNwH2yF3Sgn_PdYQObFWrw4Km_815OnKCUMOWqyPbBG3OsGb8Clx69_SK_D2cGjYQonKW46BExemizFDwj732piKn8a_p-KNQPH94V1TDIaN8V-0hBiLrKHgauRMJyLZn9z85bD3oYSx6rnJL18aQq1loE9XOhE6nnBx86AUmSk_dz3LVQz9Qvt9L6MSSzWkm5UXGAFO8uWGNrVlAGi5RJskndudBW_wXVeZCe3OpP0_KFD-Sv8x8ZuyjpfgImndsFgT27j0HuZqlhmOa7xPVwriDFOVg5RZUX5IkMNzifnoyORCuX1IKr0NzFXs2UEuRd0ma5SYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=YXQMvT36xYwCS-MfkgVE7NywzAG1LlrDUGIaJU_pIkCNc8VjSzffjJTnvDPM9r22dQVG7rprcM9h42R5zLLeVgb7lHxRywqwyEV7KFhr1CrmgiveHYvhjNoLUz7mQku0aPzCjnBBM7jnxj5R_kUlS41yhXJ4c2HM1KexEnUvCjQBYZGqT1JRJNNcf2kB0q_9e37nF32-NGHxNPnBHn4wZJ57f0YEl3ZQ2PV-MK-qe3FXAJQvRTrg0ZDDRlqV8KV8Yxwej-zB3agM25gWvCxrquM4Nes65hlCH3hNDWSel2eZ8R6Yh_-9FEOSpx_j-TDUtaj5CsDLna259zHBj6cLDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=YXQMvT36xYwCS-MfkgVE7NywzAG1LlrDUGIaJU_pIkCNc8VjSzffjJTnvDPM9r22dQVG7rprcM9h42R5zLLeVgb7lHxRywqwyEV7KFhr1CrmgiveHYvhjNoLUz7mQku0aPzCjnBBM7jnxj5R_kUlS41yhXJ4c2HM1KexEnUvCjQBYZGqT1JRJNNcf2kB0q_9e37nF32-NGHxNPnBHn4wZJ57f0YEl3ZQ2PV-MK-qe3FXAJQvRTrg0ZDDRlqV8KV8Yxwej-zB3agM25gWvCxrquM4Nes65hlCH3hNDWSel2eZ8R6Yh_-9FEOSpx_j-TDUtaj5CsDLna259zHBj6cLDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8TtL6ajxX0Bly-4B_RCIl2jeKthBgrSQDnLW6-vxyLJQ7PCEChhkCFZR1z6hLaBrApN5X6T8AniZIjGUQItNODW9N1u4zAa_pbP7ANF5yD5XC_tNDwSDvcihd7xYbIXv9Ve13VO7WOKvCs0-vUSz-Edn8RRQaN6RxAGap-2T1v-nnX61OFWbE1nXpyz668H-7JpPtGjQAef_GqswRt3ftmtbtnB5r2ziwDKOW-Ugto3exzEmVpTVnaY8nHP7o3Q7ygT3iMH8g3W-QzZQ-xbPj0kb2mD4TB5DHxCEoDKDE8rDD_kyGphLvmv6J2C0464vrJ5pH2ci83LRj7kUyNmzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-rCjhbE14Wf-3MftN0inCCbV8JdsfMnx0RlUjwOnY0yBdlIUcJoc77besrwEqQzmaBoqk0Z51UJ5gLZsYpvTQSmKLZzsDB4tHJDnx5P7ZcZRNKb6Eu2BPGpUz3e223PY1YP1lSoX-dLy_dd7XROEJ7UdLH02ysDAqAL6YnfsQn-steD3Rkq-GrJPTeO6OF1drX_tzLSbRxxFJuB2oD7XXtF7lDmkhPsfldBZAMmQ3syEEYDaSo10a6bWHc2j4kagtOyldpXT3-2wjN0GMwDAZadp3X_ETeuT3zUQJo7MIPg1BgNw7qISQBNA_lebBbMv_jKmCHzxB2Yhy674bSt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYuriZaOrGO81Us0O3t3A3L8-wAr3V0MNhZ4VFh7kp5UP4KmkoaSpzDkE5fpelga41IiN7ZmoKIZYDaQYaBJCDpenOIZyY4RGTBT3y8ZWefQ1D3KNHwf2pl9CWs0MyQvVHL-b7qwp144xweLuhDSPRsjBqQ_Oprr7a9mYbrTllI7-AK8MIRqRdfbDzXQCdnheKP7W9MhuAwiWi9dG8NodR1nZNFoubU3UJ84n-FjfEO9HlHwJqbhsg7WZqyi2G50y8Ce5PiEhar0K-glNFRuwsttmuoNb43FQn7olxtFwprV14cbTobAH5eUTwlkWIztoey_YA7aYh3Z1D9OLPPDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYrajnCPnIm4W9BaYf_j75yD1Y7x7uVfljqWS80B9xKi1XTmebUPRQgxGK8q2xSB5fhc5HcgK3bL6VbxZE9F06eya0oEWQRj56WkEhuZALsA2NptWj0oZYJBUTTHsFnc0a_clMincfe_i4cl9pOgeDi4IxRMnMPLsKnOfZsIBA5TybDwOlv_upqs_YXBl5Zoeis2jOlgUfAVJ3TZucGQ5KMr6DxdOrltg7fRx1csoPucqCif32ALLlPR2Qvpa35Q16rNqgl3vcJNmNZLt4GkLDmvO4C0vfYw3YVrdVNS1aew7G9qaXJk_I4tLUlQWSqy_DF8Scv05YFGINMXRvkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDKEXbwrP73nV1zpDd7UsaS1Oi2IuvU88z2fxotFTvLkpDwOKbXfTlqKn0fRfyZpYDLrqiKAMw_KY9MPPTH_jGavv8MzzK6WkqkJLqQGESjLBafdLmuskMtc5PomsB9p3qlMj7tItRRsLleMwHuY8WI69HFGFjHMPUG_YOXSGjY188-OyGVihvczrC-MUGhhXz9FSGruiWCP7BoNyoRsuE3vNNbL1Y93ZSm5pMZrDM8C-4XiObgfBgRHE-7Bi7p02OrMkJjitD280tvHaLhlRSxBKxiZVaVYqmpJ-nG3Y0wfltCHyum4tODknNdvB01AoWbVkYNyiuNephljiLWnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVt4e-We8f5fJOsYq3ZVzQzi8staSJpS_BMoXe5ke4W40oOnPwPcLJmcUIexi5I6gHx78VA2xUtwiCm5cCbRpDKM0FhEH9crTOSrB6GOeLd8k47kIuO_kI5nsaGK3uvQ74hV3hszZI0GzQcpZo1wJDzCNb9B-EA5G9jplJTKOi6NhirjOPG4V0FwCRYXLA71a2TcCIR8gv3xmhSQM7_EtaC7Ez5w2OpQlDu-yLNFAD3XaqOTwDa0nBwSzYrr7d2zdEmuxJudRHTE9u8qnRVDhgi_NKgj30R-QHkSeJYF09ji6yUV77wi-i8a9l00gruaSMU_D3gJjJUolKhDZIGeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK_TarTXIE6DQwKSb1IflMaugbj6Wttv5FXCL8GAGzCUKEvIthGrx0FF2jFGGzV3FW-6q1zaL_HAk3xhI3UTWVOzFGOe_uxnUYnIHwMChu-le-i8cotuAwH2FJ2W9QQVIufKs7DUE3YQy7AS--oCwm4bBx3ZEHbyt5nw0GW2--KYfuEgquOL1AaLH22Wxozonhi6bVtsvH63mok_-Cyo2pkIfgPCUS9Tk0Grq0OOPC7mXgppM4iL65s2vrQHCsW6l_tPnxK8fr2rxaujilj-if4IntxAElQoikgsuiNTAzlhr5cJQeLIT77jfLMw2zSAS1-bgRTghRkuKgJZsj19Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=pwyxSEQSsmXPSVTnYxbxQ5vh77SggNwVVpkLgLshejWes207VyiYKnWNX4gmM7kVowTuc5hkorpIQ8-MyVRiAo8Ux6EkssoBCplch5xPSgIeT5PslHUqbPz1P6oxrUD5Mg_ZA7b7uARW24vG0CgW-GsPVNBhfz8tXhCOFsbX6IrEcU5WAO9Sp3dXWYrvcRAp-QK_D9c-0B_T-yCGUPspNMQ9uHhQbxXRd-aXW6hWPPeimGQO_0h1ZX2YYxUds3AdyI3JR_dAKWdy30Ytt4rbnioGrYJilDZeM6EyPZYxeLMPrBVJptXVfKO0ALQUNK8Ra6I2biUGl0LyqYlHw0TOVlbhOBk8j4SacpqPpJn64Wk8-hl64VO_1BD_L1gNlURimSIkTvMeDttNRo2LSGJLxv_PIb95szGG4zrXNMrKxOATS4FCQOvRM2GneIn350kKMeG1121cx4ikmXCSVSh9byF6EohyeWXoivE0JJ4FUqUYBwiOyztWLsO6Bv6GAtCYNlfyc3JuOkko4J6gwc4zYXPeUsY0NPtnuj2yr_JC6GpMlQ4Z7xhLNR8aaKebjraelWI2MRhuyiyOLEMgGGPlXk6Oh-t4CxXHtse2m1f3X3Pg_Y99V5yhvpJC_aDW7yLVyBZLq9gkx0BOOI0vvADiHs4SphrtTddOcckOKdT4z3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=pwyxSEQSsmXPSVTnYxbxQ5vh77SggNwVVpkLgLshejWes207VyiYKnWNX4gmM7kVowTuc5hkorpIQ8-MyVRiAo8Ux6EkssoBCplch5xPSgIeT5PslHUqbPz1P6oxrUD5Mg_ZA7b7uARW24vG0CgW-GsPVNBhfz8tXhCOFsbX6IrEcU5WAO9Sp3dXWYrvcRAp-QK_D9c-0B_T-yCGUPspNMQ9uHhQbxXRd-aXW6hWPPeimGQO_0h1ZX2YYxUds3AdyI3JR_dAKWdy30Ytt4rbnioGrYJilDZeM6EyPZYxeLMPrBVJptXVfKO0ALQUNK8Ra6I2biUGl0LyqYlHw0TOVlbhOBk8j4SacpqPpJn64Wk8-hl64VO_1BD_L1gNlURimSIkTvMeDttNRo2LSGJLxv_PIb95szGG4zrXNMrKxOATS4FCQOvRM2GneIn350kKMeG1121cx4ikmXCSVSh9byF6EohyeWXoivE0JJ4FUqUYBwiOyztWLsO6Bv6GAtCYNlfyc3JuOkko4J6gwc4zYXPeUsY0NPtnuj2yr_JC6GpMlQ4Z7xhLNR8aaKebjraelWI2MRhuyiyOLEMgGGPlXk6Oh-t4CxXHtse2m1f3X3Pg_Y99V5yhvpJC_aDW7yLVyBZLq9gkx0BOOI0vvADiHs4SphrtTddOcckOKdT4z3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6EObi0fixtq2bBt8hKh3Le7MNv28M9mKK-Jxb1Ql3b3uytNnSN0k6b-PDMUlTtkqnkYwJj1nJIbX5G8CMPO-7H3C9eJCfjo7LQF6E9p2ESzCywgkEOPtXCsnEL_K3ycHekQaba2c03QdF6c2fhPwJFCKYLR8bMXKYNoW0jeP59oQ2SaZEDy2DEIYNsmuID0GVYN5VcdjFHbR7e8jewneahU93--JeN-nm5s1unXHqEvi5lTSA2hP1d3CKS-m6XGH7ETOIHsUeY1VeinAlXpSCh_veDL97Keq-98mLz_bDRoihxU7lkbHU03pNBmJkMyC-IxpSIeH5DZxwsN_jR9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=VMA020DkLDExPOXYuqSjH9wjugdk_j8H7qcEqc0RIPur4KFFnHVuNyUnvLKd-t1Pr8zYHfyZGblatPc-AN4D0vm0809YUygk70U6Cwb9umAUAxndtnwel2xVVzBm8Eu8acimiGL1iQCnTcX4EMHSa5Zt2mV-VQ28Owdd3N8C00KCG7IOujVhf_iOc073b7cPHrefyPzUalHFHlbhfwAQd1fUkXTfLHKZECrr0clasnZWQBWCkk631ZZ_3ARd2vo7gE92J69IJoFpjgySRQ6eAnn4I2mCEx6XQWJLHJYtZoGaNw_1r7dHlIM1b5HFFoLUScFFEokUBZNKian4TpR0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=VMA020DkLDExPOXYuqSjH9wjugdk_j8H7qcEqc0RIPur4KFFnHVuNyUnvLKd-t1Pr8zYHfyZGblatPc-AN4D0vm0809YUygk70U6Cwb9umAUAxndtnwel2xVVzBm8Eu8acimiGL1iQCnTcX4EMHSa5Zt2mV-VQ28Owdd3N8C00KCG7IOujVhf_iOc073b7cPHrefyPzUalHFHlbhfwAQd1fUkXTfLHKZECrr0clasnZWQBWCkk631ZZ_3ARd2vo7gE92J69IJoFpjgySRQ6eAnn4I2mCEx6XQWJLHJYtZoGaNw_1r7dHlIM1b5HFFoLUScFFEokUBZNKian4TpR0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC1zQa59ePLvuGc4_F9MQnpWgGmSq2Sv7Wdv6nj5CwovRbT3gepsE4FDF4JQ9Spy9TLQaNa7kFhe-iSr0udrejSNIiPIrUdEOqhlLHalN0uEsejlDzeXdVaV0XZeLdL7-vHbNFFyWV1s6nUjg7PQH2URJRujZx8ZSAvgWt_J6gCaCfutC8RzERg6XijHgRmQVr1YQYCEKHWxmyjXFkMfHXUiY6J6ZIFTx4_NECKl1fGpnfnWgmunLzUrC7OFzm8pQ06Smfms33m9nLMWgbVzK-y9xbq_OgYby45Re2CKjGidmP3mab8ZzdU9jtw-7QGgHewVBtRF19R0htmJjqlUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr_C6RIsmtzdNySy48NR4-IrQBR64dq53ASA4bJc532lQEh09HHT8TVA2sRXw-a3EKAyerYfgwkBodsnbqLzoj6erkjFLpTBcEwVyfa_V-UurWauC0-_zkFIkkqpWj2_AqX1J9N5e18qt8TOq-veL93IPqUtmw4OK_ivCrxwdh5QJd60Ay3Kqvp8O6R9AzAE5wB9BG7SGPqFidm-OSoKwWhG-dTYhO-n47QxL6jMp-GqUAP6AkScBQTr_sn6wNcg4Ism86UkGU2q0wB64uypBkLMyJGetY-ejwpLc_Cv43Uvjna0odcOX7I9f29EngnACp5gSQL_ygcuoDmzJAOwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc2p2nF5fAu9kgfXNj6vvn_1LLt3i550E5AXpWhsZZegY4C_aq7Wue5xQ2s9aiHOXF835AjYQF_Tf2aYQcoVtsYmgo-spZYqbDzzwB-MgNqHTB31efkT6W6vVQfJ3d6oVtVJA-AReWKG4RntKURNO-1K_NuUOrH17XmcRI5n3ibQqTwwdNsASku5B2wDtcH1lCSU_Rb_p7NyNVLPZuXZFxscot1iKjJnGJIGiqv8kefafrx0lEfsH4OOJ4aY824dg0hC40TUrw7PnYQqHITRChFxQ0jXvRE_h-AHnabDQx0W116GcDzgWI32dPRFwWA3Zr-E_Mymmn0eRlfGxudBXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We0ca-RC2iRrDuwr6h686T5pvFtfrwbKFqgo-6IgLAKC7sSTuhpW_qfxKrwCQMUKcnsH07_4gBAu_GJ_TlA6XTd2kF7Mw0_cQz7LToThdQraeROP_Mm8SX-jDrTf1cJJkb__t0qSnszbwDD6Eb3TrClhDnAMFeUJH6zW7EI03CFRGs3kt0TRddnHii15vQFmVRUz84cxoTXjLbMI7hNsPWcnZH0mOIt4_k0E8clp8GyC4mkk4MepKoTnkMrjr_gOn9l45axkMTI730PMzLmjolQWmvUWi3GAruIWAZ14GB_Wr4GrBUG4ZOdPJ5LAxQh_WnfBKjlyt5OXyXSO1UTYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=ET86-QzhayqAbU_kgiralxCyWBnVs659Ssm78gqFitwtrpY6TeEE7oT-O0VUTtBf7OrdVsZVNaSLESl-pjWaDHra4hJk-haXw2Yu_X8L-dSvyeqOo33hgQ2Q8zhJuu8Ly6NQ6q4gnuvfmUtRZwdL-AWJ0wwLThklf8JX-qHUaY4no4apBKE38fBFC44kTiYmo55kd-M3Dz75zDuIp_XTHN9MCNLliJRp8TnCBgoomlmnpmsBJv0uaBMCJj0iYCHTbUNL5Uhl9N9kIWDcLz3KeBZtN1cAH0rp8eBcXxjr5aplBhC1_q7WckydQjBDPeYQ28MT-uFr8YEYqhjQ5h77xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=ET86-QzhayqAbU_kgiralxCyWBnVs659Ssm78gqFitwtrpY6TeEE7oT-O0VUTtBf7OrdVsZVNaSLESl-pjWaDHra4hJk-haXw2Yu_X8L-dSvyeqOo33hgQ2Q8zhJuu8Ly6NQ6q4gnuvfmUtRZwdL-AWJ0wwLThklf8JX-qHUaY4no4apBKE38fBFC44kTiYmo55kd-M3Dz75zDuIp_XTHN9MCNLliJRp8TnCBgoomlmnpmsBJv0uaBMCJj0iYCHTbUNL5Uhl9N9kIWDcLz3KeBZtN1cAH0rp8eBcXxjr5aplBhC1_q7WckydQjBDPeYQ28MT-uFr8YEYqhjQ5h77xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOp9jht6-pE-ryGEdBxPVVW1S3AXISTQifKQ92DatwA_zIwMHeB-KbUi7EtsFRkvs8mrvkeQwf2Js6yRTKPp2A3SwkOHtinBv5uWmfP-TYJ9NjZrmBavpXKdg1K_rrfPW21k4XAuZj8UeSYPXGQpfuGFTYpJO46N9kF5E6wc9utE_pmHtxeq87VEPjExunJhTOPitEXMbyCctGYqSW1adYB1TMYeyX1iZGfqXr9oLShF_pyMZDwN8OZZNLE0KsY9pWiFlJz2VIZkOk-HEeaJQEKmT7crCegXdbOAaLH4u-_7l1R_B4jlEiS0w4bc8I9xGu9PwX8ybtrcXDQDSdSwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUTbKOXghfhiCVbdd2azJRRTI5IJda6S4wScGXgUBAERVg9FItWlKOT0bFTzXzgipq20lT-efIE09uqAGLk6GQLOXKXlwaSMJW4sBXyHw0mFOtItX_JBa1jfKHbuCEqcppZckzah5LPHxlXvzYxuN20bcjqyUgvyJ28MJMYSI6OHmPMpX9AxONmuaomQ3eAKKmpdDipDtbIjdfzn4BMmA0n7ngcrbnY_FWSv2Qb1Bowjh98gbFbW5nVlD9yKSBGtDcWQdoBHT0sBX0d5UFLiHCBG-KoThMNFLpZSN9apQTjlHWw7hwKki4C6g-Ngmt9mUhS5fajJrVtfG572EbPNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZASDItMMlb_NfezxM88Q20PtaTNCwIrDPDsJLh9-cFsg5zCvxRuRWtSrx8FeDrDD6V_bmtxG7F8ckC3hnCpoL6pgJnEYAhDu0ArHVj1V81hZHtw9mNADJD_G2_kIWP-URHkkB32ikxS5NAnAnKVam84Ru9BNFgoaYLSRF2GPiQFIZFEFBSYrDFUp6s1vMd57grmolSAktsHHmKz9_QtDfMdpRauZX69knZX5i-KYNW19Q1bjN6shIe_mIc_Dq7pwJHgR9ci_kgzXYdjKK55D_AQe8HO93TC50VDstaPMtScIC28tG0YJnH3eJkaRO5VI2CQoJaUMeHdRpPI1YA3Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy0b52DorsVaoYLnQfV-Xd1YE3QixhCQkFV3kgand1TG7dxKVa8bihOTT9AlDS4JN4dki4uGR2uWIBYXKfVzxie1qtGkVN8hBu-w6KllSYUVe39y6mcj3CLjFXttkfpvFX_6u5KuqS0bby-pyviMZQsCA-4aBuMjVJSDb_LWxdjFEhzJkThWdxm5hgM_tURKBf7kHDa8fA6s0H5lYLrpJUQTajO5JPh09zIgbw12riy1NLYaFueFf0sIApvVukvw-fYwfc9z4o84s0KY2OxntpcANgTiGvYdWx2OzPM2B1687mb3dvcjx9GAFd-eGf_e_E3mTtS6d6kp2N8bXMlbJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiWqMVfXBMKmOjRFgaJLfLdkqWw6Wm4RWeVZ_ALp-cEli-bSfSUVUshIv94mHqGimVJP8jKIwXleknD967Woe1hyKDZX7EnWdDz3tuYZ_BXiZYOGYtjmxzn-XiN0GYGBewRBB9-KtByaAkE6qB8dz3mXP_1b51QVlw9vHfqbFx8Ucb8h2qwa51uGqviVydxsSguzJU-PyODWVkucq-XEYyUR-RAOs6lWKAKc6HINLtSZyWTODgkarbQBS02oPYVZC2n78L3dXlIUY2yXGbt3BJhLfxyYeBTWqvVuF0q6MOII95R80Mk9OJEwL9KtRLpLlLS0HtIv23Bl8DE7N4Ti3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=OsaJ4xUNs272Rl8GJn5kvQ-amXRQWoOi-jpT0jS9QF_1oYvYKtUoQVVvoaSpeYOktmCpj6f7zX1-CRDuh-syMSBG5CrajJTW2JS6Nee9Q9eD_otHotoSFDBLHibnD-1QqdM_ZCq8DIPxROKvj7YR4Mr7ZJuH6TNT2EsndFMR5PukhW6h7GQYRCoyNrW_-YYk5L_tIpQoWF-eM92lzWNMBPjpGmHiMvMnXzW7Pumo_asYqj9DyzPnZHJId0l0XxnB8nfOa8Hjvtx_RcYZLPVrKYinF63DveblzVdgBsMSKELJq20eSWHBGi7lRl6rHIjyQuBDD-RJX8f2_px_2Z34kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=OsaJ4xUNs272Rl8GJn5kvQ-amXRQWoOi-jpT0jS9QF_1oYvYKtUoQVVvoaSpeYOktmCpj6f7zX1-CRDuh-syMSBG5CrajJTW2JS6Nee9Q9eD_otHotoSFDBLHibnD-1QqdM_ZCq8DIPxROKvj7YR4Mr7ZJuH6TNT2EsndFMR5PukhW6h7GQYRCoyNrW_-YYk5L_tIpQoWF-eM92lzWNMBPjpGmHiMvMnXzW7Pumo_asYqj9DyzPnZHJId0l0XxnB8nfOa8Hjvtx_RcYZLPVrKYinF63DveblzVdgBsMSKELJq20eSWHBGi7lRl6rHIjyQuBDD-RJX8f2_px_2Z34kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DV-Qvyeemr-Gx4S2U7CKtVvN9ttwJw-wMXoS94k7l7-HZF6dxN4-QL9Bs4RHyYz8SkKQYSTbmJmWPYweKuhRSZ2saCirqDceote7arvkwTSsM2_q_-kiLUbdOeGIHplgShiS3TGWpE3tGzCc6rUpaNDXQWbzi75rTM7LGJsK7cu59JNNMqTziFKGlRj5iubSZ4Vq7zyFbsMR2XKDCiXUEmeYEDXksTR5JfI6wdB-JpGkaL9ICzfDthkYPhcgNbV14j-oAHTB2URwn4ocC_DeE5uplmPuTFItPeVjMPIg0UvTBrdXk2dMeDn5EhO9Z3sCN5UaDQan3mMDdgzX6GAwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKxRoOmveSRe71VXE_kyX1ST22lL7CSuxE7M38Al-SE0Y7IRrwgxmzZb0tDISG_hBjhLxE062zrgyNwh1DwHhrRgRr3NJ5MlcxcUIllBRWU_mOb9IC8kfkWPZxjNfCASZPSmm69SXNx3m3GFVOFNBjGehXfCn-VM9AvTYSsFRCyT-hQfKSCFuH4EbgrpdAe4T12CNw47d5XkNYBSF0zxawmU3Z6Em3njFG0gymyghIYkyd1vgYPeRt_c3Mg5yFp80PGGDE0jC5nPRR1I1LBhBJPRVGA40jA7QPWFgcKHpzLS6g2gZf1qUEs_QuSIKMvoFMUgzSevzzv-QztZs0HQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEml0Klo_9ib8DRfs9aV_1iDn_ANq7wSxLcUh_BL1NBlpaImYWwTwKTypcufFMcc8U3IMf7ElDsdKTYJ7uXs8qAY6z-zHo1ejDlcv3fKjeVtw-gyp3no0urvxdSmyzLghV_fsCUON1yORfoDfm7Zbl4uLuF0_ymzUcc1ZcytHr5PvVz222qO-p8-_DGCJlqlmx7w0XzSuZ4rPRwmmu2QBAxM6t0wzCrzHfiVGtpVZLkcYEolVJYdrsZm24f1ecgXiqu17dsUADS0vvnqMOjY-tQMfDXU6c-JNlSjPTC2o5All6fAf4w2DZq8As5LOa_of5ih1hRjqxp8w5DayOWB8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVt73-4UsQHoMgKYfAbUkFSVSfgPDEKl6uZDWlHFH5JldgrJ3H9A3T--N_RyNniNpM8yEDxQOaSF5_ZbvRVbPcz3ceb9OKSuCu12ZsJxczxNiTHjX8BZq2pILUyF4AYFpoqRluQ2ov8b6BYz4NXPYxo1klkicH2jCKZ4flXpMUHdVk6v4pcUtK5Ic1B8pP7YcsVKWuQlvCv5lszkH0zGIzbN615gTLgpdnFaq-nwipl27YRuX-igPjc6EBcMTYjei9Hf094Jedv97UrscK3TfCFRXXQt_ZqF-5Kftzz4RVibFO8R1uCdJ4ul7zOc9w_lyPcqoL1cBGDI5MgDBMUrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmKYOr-Zo1_H3y2bDcyWusPVqQ9Q24bkY80gJN-J7WGLzkbWDPtTHWJzvDSrVVL_WPQESmUIZyX4X6LPf6_irD8aP_SAR-NtiVFfWlNSUtJCrtqeGzMhjLLyp81zzqoaO2EJPjpDVNgK6LYB561mIuoQuCFZUy14yLyLEgx0D6goYzvirUroJ0rqu3BTTRD-tsE3dBOR8ZFl7X3kgyS7JjOSsLoM0reC_UM2MJom0SjP8yt-BfFFu0ULscLeUk4jZg2V9r9oo7uIQjOKLazmrxVBid_eVYVcVcTgTXsasINZiAtIwbDhu5sXuIzgl-NmHLFbV14eoDq5UzdpbBi7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDjBQYFoPy_YDCB4GQfq994GfTj01vuMqllIJrTOMRsWgiGjFkvEuCgBQ0G2TSGD_FawzxaHLWGNtYK7xWDvwlgd6CAON0yR1TmhTj7_xANkPM-p1G3MoJ9n-myGg70dSUjK_t6hCve7wO77oqilzjcP5LIlg1NqOMtohlV_WsEmeo06I3w_Y9Ee69o-Qw0GKtkHv_WQCEE2DW0UkzeGg-UULT1ueNBZHdmYbESVv68HvVSXCnpiAbEtUmUsRhZJpxmKLHxvYG5-DMy7cldinH2FTbBXm4xMzPbS7Uy1ZAmG98eLk8DFAoFLOnBA1h9CxfuGo7KaUmSYnC0bHT6uZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv4WfdKOLqgz0YFNYVIBvgNYcRbKgaJC6RvVRAOQqNyQWHTTyy1SaKOYzC7GuTHXDRyiNHQgyHKjQ7499cECDX9yKuDxrWZ-cj_zTUrt4R9gUKRg9HsW7Ji7LcaFDE7bP6wg6sWbYwVUcwFy65L2BQVm-gCEEqyfrDkwnG4EnP7_F7BOhSdDjuh_DoWKRMpXxghIfiAbiDnPfdZRp6gU4z2_dUoeSUHf3wk7khERQKbdu3W924gWu-SPCpluXd-sum50BbpgJvKzfODF1kTsHPOW6rGM8HPvBbx49gv7iL6CiWvJ7tRsfK3xpsqZx57fF10qu6DKMecWGeWiFrM7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc41hIEfXRZqSgmwGZl1FezZIKhavAcW9Esjso1UQqAafX4IoAUD3rBcSFWN-CNE6aFhhHAcPWjv9G4BUwRahtIuNABRdvLZ30ZhK3Bctw4cIpx2Ea7-dBCxZrslxkyQ0OLCQXkvjQnF_fCI17KlASw-UVcx0FALwRa4zzNqN4DdahmeiO4UuP-_szsPDwe2ykKnFYvnubvVmPmNYNVzo1E9p9VfA-HdfT3YE-Zulelj-rm1szi6fBVpdikgRRNG1qD_8BxXuqHMaCQViBsZQS2mpYGaYIM40sGDHLQY-Z-ElxP8UORe4UKgC8g_mWptmb-pkT1M2FDjxvDWGC2RrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=WGU_iotKvH4zIzPBAIleHm1SU37C8INf6C2x74NzXNXt8rCC0lFjzXRRq4MWlCZNCoKbZ0H2SnWuQ7TQ2YFKasFVG3hSMQFtFca6S2HueBUl37Cl_3eyCML3pduq6ndiFh-E0vEckRrWNo03HC4Lmz9C3lkLYmRq74UazCYAhFDRg8IwkczdzTXv2OK9YcppunCou7WroBqQ_cOpGB1l69tgBa_yTRLKQvkLWX6tOXlndRfnKn1jLTtVIFZleTxwR_1sUmKpSxAkZ_RMBexq-PvGgdq0At-aXIx8IDOGNVL0-2zFazlR0GQBXPas4eAIwjE1sv2HdyxbjlPdS_GZuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=WGU_iotKvH4zIzPBAIleHm1SU37C8INf6C2x74NzXNXt8rCC0lFjzXRRq4MWlCZNCoKbZ0H2SnWuQ7TQ2YFKasFVG3hSMQFtFca6S2HueBUl37Cl_3eyCML3pduq6ndiFh-E0vEckRrWNo03HC4Lmz9C3lkLYmRq74UazCYAhFDRg8IwkczdzTXv2OK9YcppunCou7WroBqQ_cOpGB1l69tgBa_yTRLKQvkLWX6tOXlndRfnKn1jLTtVIFZleTxwR_1sUmKpSxAkZ_RMBexq-PvGgdq0At-aXIx8IDOGNVL0-2zFazlR0GQBXPas4eAIwjE1sv2HdyxbjlPdS_GZuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6agKUjXiMgh3GZnMs4Ga31gNLEabqMAPDBeWBOBqe8rL0GUmptP_Yo_pp5m80k5uGgXkhdKA9SY7d_Vk-XujD6lgB82lucPYiS9CmL-vCgANhiJXFwmqtoOowvs00MvmYrHNFeGqXy4JaYV9iXAiCZXkR0PN7D4CVwvP5OciGGxy9FrE1uoUfBUCBQrxI4H_UNbfvi6PKafEdPcmYax6-WLeLEEfwvx25AAY9dv6A5Xg485Jp0MyzKk7z9tUKQ1ld4LWSkGEO62sA-Cx_C2UJQAnjvnjl26uJ4b1WSQXjOuRnvaBNA6lntK3z6i_y9GQ5V3kNH2NogfEk4O4Me9gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=Lm0xFfWxwFPC4SwjeXH_DI-DKeL2jN0mxUGSj1FZk7CtHnVw8LsdcSQiMRfrMqK_T6hnZ3p_-tQ9FH3tYhcQ-xdH8hr9nV_8KvOz_y3UW2QbuGcXWkD7d4FIFxQta8tNcTqcKqySJurHZyZAAFapIx3W64jMOckYPT21JePla5Mv_J4SRTp0Nhwaul1fZoTlWRRs1lP2BaAZptSbtl3FDtOBTvdkFz6wMNzHjob3pTK8nlXU2iOVWTFG_J4ZJQHsthTho34Y-4FAC_P5IbOW5MZh8Ey5zxqoN4mnCUjz6PBSMRpvZi8RbRbCjOG2vkDWOZh3RbAA4HmiBRVDdvw1GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=Lm0xFfWxwFPC4SwjeXH_DI-DKeL2jN0mxUGSj1FZk7CtHnVw8LsdcSQiMRfrMqK_T6hnZ3p_-tQ9FH3tYhcQ-xdH8hr9nV_8KvOz_y3UW2QbuGcXWkD7d4FIFxQta8tNcTqcKqySJurHZyZAAFapIx3W64jMOckYPT21JePla5Mv_J4SRTp0Nhwaul1fZoTlWRRs1lP2BaAZptSbtl3FDtOBTvdkFz6wMNzHjob3pTK8nlXU2iOVWTFG_J4ZJQHsthTho34Y-4FAC_P5IbOW5MZh8Ey5zxqoN4mnCUjz6PBSMRpvZi8RbRbCjOG2vkDWOZh3RbAA4HmiBRVDdvw1GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=R9DWG9LJ7mC7hqz0ZeB2m93lvL2zREzJHeaoohnKGOlRbQi3Tzf5HRT7SCam26T8lYCX_WuU9iMcHMaVIqXxtstBwhz9TmkK35v6IcTGcqI7TALZX3t3r1yyqjZygdo_72woBvpbLCTob9_EQIFUr0XDkbbg_I1CKp3WlWimmbtAS1cM2d9xamRmKyw2BanXY9StHnCoOWcYfVm9z7Le-tXtIXurBk2Ik7kRJmpQ80hnac8nKvdoaSiJZIkL_8uNP2IbMtg0E7TyUV6GlTEn_why8aWrCy4bdnXh7xkulAodXjJ1mWKa574Ch0DXN9BVdJnNOURmYWOoLwXcwlSsOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=R9DWG9LJ7mC7hqz0ZeB2m93lvL2zREzJHeaoohnKGOlRbQi3Tzf5HRT7SCam26T8lYCX_WuU9iMcHMaVIqXxtstBwhz9TmkK35v6IcTGcqI7TALZX3t3r1yyqjZygdo_72woBvpbLCTob9_EQIFUr0XDkbbg_I1CKp3WlWimmbtAS1cM2d9xamRmKyw2BanXY9StHnCoOWcYfVm9z7Le-tXtIXurBk2Ik7kRJmpQ80hnac8nKvdoaSiJZIkL_8uNP2IbMtg0E7TyUV6GlTEn_why8aWrCy4bdnXh7xkulAodXjJ1mWKa574Ch0DXN9BVdJnNOURmYWOoLwXcwlSsOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FkZMRjYJFsSwEys9hDibrGqgRC6sIOFbGW73iSonNJWstAxDx1HIv650vqtEzQhdQDbSO_oWaIbqFAw43_6x4AvV1BfJacYzJUm-aS5AUaq_haFmgVngyYzDckwIs0LerkQBXM08--kgGtuH79o1jNfLXSQjayGadzZFn8KG_Nl6psITy3A6qldCuZVtuRVS3IfPH45KjLUzG3LrZNUNke2VbX6DfNOAHgFreZBP-SVFx9gaxjvvJ_C3A7ookHv_pANFnU2XFVi26zvgpmYCxUGPxhfG0o2ZGvb2rNkReP7eieggOhx5dK8YpU1uO8pa7bnryJbDvAlxPP6SJ2VFuNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FkZMRjYJFsSwEys9hDibrGqgRC6sIOFbGW73iSonNJWstAxDx1HIv650vqtEzQhdQDbSO_oWaIbqFAw43_6x4AvV1BfJacYzJUm-aS5AUaq_haFmgVngyYzDckwIs0LerkQBXM08--kgGtuH79o1jNfLXSQjayGadzZFn8KG_Nl6psITy3A6qldCuZVtuRVS3IfPH45KjLUzG3LrZNUNke2VbX6DfNOAHgFreZBP-SVFx9gaxjvvJ_C3A7ookHv_pANFnU2XFVi26zvgpmYCxUGPxhfG0o2ZGvb2rNkReP7eieggOhx5dK8YpU1uO8pa7bnryJbDvAlxPP6SJ2VFuNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf1tCUHEIqU3tNhvxZX-0-UTysIA3EtJyRejJGkh3NGYg9mCwB74XXgIwHyjDiPHDRa7wmLJwbLLZw3tvYPFEOXU5zdTIne93hOtvtlB4rvi-ZiQmQs0nrx1VsH7d8oRQW8eFTkHkM5Kn2nFdppHG_wjWkEn0jAOVj1hNbu2giNz8NtcKZwgo6FPkTqek3idGQEqgG6YBm_71yhOOzBmRUdI7HeQhWk_09aN3CyqKO91qcYM4u8vw7pvWhcvFn6ipttvMf63-jUBF44Naq53fC8_KTgLmjXmBwW2ar34iwlNO0x63DpAWP4tmGOYbD-Cool_5ynH50k3tHPS7tjUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUWuFaeLdhchGyKO-4SGAHsL7qjPyuSvjfw3sH95IIOefkHQAdJonXJsim_2LoEkL0w1G2UvRVqNUed7p-2MpHeJTk_H_RYRBC0Id3JrTklmE1j8eQNBnkAXD08nmSZFMSpX8OewOVKnFPNNjtMMGA2AyUx_AXFAz-ih5idxZjO5BZpOatRC0YZb1c5JCoUvuf7Yw9A4QHTPWaNBlPe45pFeAaYseW6AlkhoAWNj0lsBKWOBqoXVMlNuu4NgcTrnv59nm7sxdplLFsthlf1vuXkZh_UNV9_0UygsqCJT-9Z0RYIim7JytvGDVYtCHMrjh9OfR3RF1FQ9c8LkSdEm0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhN0ueolcSFgSVrpAojA7bWf-IWsVopJhka7x57gch7vUNU38kgwbXvlLjIN3S30kRAra10V0SCz4ZG96IzXqd7-Wm5mwmTWRNqyQ52IhI3aqTnKKO5jGiaI7B2WlBjoVka-dCupAze3-1m-jnUBE4s72LiygKgzFe_uar-Ot0qSp2uTIGVQIkNyPA_ImYpfE-dArHaETYon5mMFYX3D2m82HGGye9B1yyjPnkbBx5ac6o8yqcE2W_PG5kiOJfc3mxVFkff_C63SoEZdDivt6UkogzQVwoBWv-LQQcvk06t27s4bld4dVFoffHykjzTJWoCvK35tIXWO-SqaHLf_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=e-ieSiH8q_FDi9NBQ1lWp_JVxfTy5tLadL50pL-NsLzRA6igdNwUpJT5lfDHrA71GsvR_1Kcnqb-HVXzNNx7rVcMk0gWQBzf8gsDK_Q5Pih6YsHyCUO-lBYGOc4aE6AoSafpqjs7z67sRWMr37LxZ5ECZALFYNwnCJHrdMkn6Ts3De-lJa-0N2IWPsiCZHg535n4ZCBOcplmxxCOWBVXQbmjMSp-cswfUYhcbY6knlEharE4c8gHRsKs_FBH98AGyNblEpPmwoUNJWvS_v7BKm7tw-9gu6KU7GqoUqfcf4dFvCGZ86E7GVoSplFDVOHmiM4m2sp6sAc9w00nB3fJcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=e-ieSiH8q_FDi9NBQ1lWp_JVxfTy5tLadL50pL-NsLzRA6igdNwUpJT5lfDHrA71GsvR_1Kcnqb-HVXzNNx7rVcMk0gWQBzf8gsDK_Q5Pih6YsHyCUO-lBYGOc4aE6AoSafpqjs7z67sRWMr37LxZ5ECZALFYNwnCJHrdMkn6Ts3De-lJa-0N2IWPsiCZHg535n4ZCBOcplmxxCOWBVXQbmjMSp-cswfUYhcbY6knlEharE4c8gHRsKs_FBH98AGyNblEpPmwoUNJWvS_v7BKm7tw-9gu6KU7GqoUqfcf4dFvCGZ86E7GVoSplFDVOHmiM4m2sp6sAc9w00nB3fJcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0eg7pv0kbcvv4V_aN67YwaBNXiyMry94jcDFzHyldWZA33vNWCXjaS_d_uvgH3HjgoBz7RXpSAe40RcLWy942u2NMn7hjrJvtoRJQrPl6110Zno5xhMvUHjPGavAYkjGkjY22Mk_-ZK_O60FKg80gjKVU-UGwFGXv-iuLw5HUPkZinqP2F-fguZe0VV1Jh_Sjas_qDsORGzBCBdorSFUXdrUylQX0OVO-PoviEi-UXCBMzRslEoKgYvN7vq_FD1LOTmH1vGBrl6qOjDeP_9vAIJb3uwY1E83LN_tBgFoW4uyFzolzcuI7vT1EYDOSEP9dqtGhlj1HkyGIwHFju-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8bY-Lr0bcPLNFli0NQvw3OfE8rThANfOBx7KkMx3BlnVaRQJaqJuhvUx2uxWIM9ofFaAP3Q4L6xrqzZJhB_Ty4zCyPx6ibpmv12EZbAKmLw7PWL_TH8WqaoE1caO7ek02d8WvhS28RNEYEa7mwM3Dwy3eHqDn9hB1CDSAi5BplCoT_BGsFsFfRtZaoeWed3knDmx2d2-QD-H17qpV1Ne45oDQP-IbO_eQyr9eLxEKNtD5TbZYfGPOWz8cY3Gec_GJspp3wHx2TCsMlXMDIIyzCbxfbzLCFuYr_zvZgFaA45lF8ffVJ8vfrq910ZLebfxHg83Xuccm5SmKlei4hqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6CVVJht0mxnsmrknP6_vNOxwrig4s4yDAUmY16bSKdQbqcTSVLGBPd73QkSMs6ZMa_VlUkIvuqiNgrP8gJd6auMw_uZJLdY7DmYSqyv_gEAYDRNKfPFvWLWljgJFS-eu5D22D0zWkYiS4O1Za-8N1EU7vgaIIk_eLhjL6ud2AQ04Cral0g-6UOLyZKdHojNxb1J5-r6frrXLAVfNrbYJzYgmY_fBKnjDiqFrakPxyOvG7kGXIin-jFE_IGnu1RGJ6-azIXwmwUurWVeWGDefb9EajIo6CMQbVxPZoI2cLGI7mPmkzPFAZXGqBnVDDbUMvFD4pEaI19rRPiXyH9Frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEg-ofGkqScP63EH1eLSVmXb2_e6AY-SwkTDP-eFOClGUz4YpOLkynsSPrzZ8my8uiZFUeR1IblssjwDq_9izQIhZH0babPeCpg75QYgIvkj78moresyZs5eS25eq2K-yOReRlTj2fSOnYCK5w28-YlKMTYakka2L8kVAJe7NH_zNbVUZqvsFWFopLENnaqF7ELcjGWqyoY9JfdGbIyCUXiYX2TDIPyawsFvsoSqZ2UG3H5ZmRfF66xf4LvbeZi6wjr2-6or9OyjHpMNXY4yX9l8nmIB5nCoqUB5xEzRm6JtKyY0yl6uAO-WoXP0xACIiZrV8RNOutcGf5rdHDT6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dff65-FLmwIVUpLDSFAmManpqB5QSaN3lCNolU_-HEmST3ChOTklbetzKj2aIAbnO_S8Oiy5dajoWAr6WWAMXXDT6oQt4lAT6pOcb55ludP69TQMeAR8-G1ne4Ci6Ezoz7VD5qieL1b7-ZU8YT1KyWD5eQTXW1OgbS39VDYMC3WeBEK36FS5ojFdPS0yPTqPAbUjh6hsKQ9OOezb0ZtKCPwvSgI8GGrOGCxh2IQWAi-C3AZj1ZSKVhAoFtUgoWAAk6l6hrFqR8M232bRKtC6q12yfVa7k3RLik2HGtt3bMjKRs_AExmBYnADHSOZ1XeZDIVFVNQlv2rkXFJ0MdZmPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=jjze-Uyl9NpDFPDOllIjIgaX4DxOJPoHV1FZ3qwhAfg86C3LuiZ8Ie8WKJPNvHaPriGH-WH_ytef5ZD_GA_TVYIXY0qfGndK7KxxZjDNUC7zMeSEO4ywSfADUNBTjRoeZgYdgm8Y9WGBB89TPJ1hffZE3vu42XrWlHCgoI1ZntQ8_swYyUmJo3rXhuOK9NURWlUwKncWJ6cM-j6udNiojlkjJkgUbxV81hU54gMh6gkYArTDsCD7PJJuUZc-E52upwhCdx5iBoEnTvjMtDFNSF0YwJRopzmPYImwktx7IDhLg_kO4BKZ17CnIzbG06ZrfjObuC16uE92lJuQfSUTIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=jjze-Uyl9NpDFPDOllIjIgaX4DxOJPoHV1FZ3qwhAfg86C3LuiZ8Ie8WKJPNvHaPriGH-WH_ytef5ZD_GA_TVYIXY0qfGndK7KxxZjDNUC7zMeSEO4ywSfADUNBTjRoeZgYdgm8Y9WGBB89TPJ1hffZE3vu42XrWlHCgoI1ZntQ8_swYyUmJo3rXhuOK9NURWlUwKncWJ6cM-j6udNiojlkjJkgUbxV81hU54gMh6gkYArTDsCD7PJJuUZc-E52upwhCdx5iBoEnTvjMtDFNSF0YwJRopzmPYImwktx7IDhLg_kO4BKZ17CnIzbG06ZrfjObuC16uE92lJuQfSUTIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPEhEL5KNU0vxoq6adspIfsCuo8w3tDWBqgI4FKCWkw47S85hYlSblwx74U0sXPo3xVGFh5iZk3If5-60tdAxrLleFV3nTy86BK92yQiK1HLSOCdGy6ZqmfwA9NNZ2-1h4iQd-qgBPBxkdwpOlp7uD7uTphIFp8bt_-m3np9lfGnbLnf7UWSPYYGtlujg6uAqdNhNw0oaeXmNB3lgugkgxqbJIkHGKMScKDrcuxhwCzgurXx-G1LH4PE1_BNin32w_h3NoeayKdBTHBLD29OohZpJBg2oaM0Owps0dUSYR284vF_4eY36qEFw_9gZIg-h-bTLJGL2hiF5bRh1FDxMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiIeK-_OjEMmJOnRRY66T-RbWylupbXldULDdA8ao2zin1Lr9MwBcSqSgJN0V8f_8M9fLD5TSEFnZ8okt4OcS3ex0GGIFeNX6cptQH4BgebbcNlHJhhid5qWrg6VIuRJAKxq4O74zdi2-ZNpW-5GW954UDk_fXreVQ6dcC6LsYSNG0S7lpxgRR8VSFl3QPWd48lycCYRp2j3oZ8YaCUygcxcU86hLUZ6pP4S_LfR-vu19IYSxk5eHIP1xfJsAJ8wDb3jQ_gsUXZBjfXGKyf7wf5M9MC28NPnJVB81-CDQPrCYBaUQOjzztYk5brxVeaEt3pTYoKQCFGq2CRmdV-eTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=inJmta8y9DdkOmGw0F7mKhvvERJPGiLQEX0ogepHIaq1k6-ItJTt5ytwd9ompn0RRUoROy1vHiMsDr9Bt4twvS9Dw6mXesLWM13VKe_nYeqMGoBiRHV_AvgCsneT8GKJsAqNofwSkrXfzEqHBBpxXGjITfc4czEs0S2bjn3j2A6qNhnjGmOZHcSXtL2EPhFwMbMp19adoq7kpqqyuapZC3zL4ltshUlB_BVmnlsPhTAAuCAZbtukjlM15hUTEPJaBfvk1ZrMZgj1kengvEKTkq8-4ecINQ0W4cXFtP3x_TY81IWu2GdU_2SADrvRZtesDsibOODqiJkwO_xf4ZImRoKT822ike-HS09c709j_KcZcpImycJ1W-b7B4doIfGj-h3XD1Syn-tqescIfYEpNcUybm_UwZE0A58TITCvXFtWUuo8QY7-4Q5dZBVWYP67m5XLxfP9cSzMkG1_FEnR01sNWxkXJEz_y4smfMoFBaTTkTxMib2aIqGFFh67YgDBoFdQ3D1LhEP_lyfdKBQwvUPi7AYkLDOoDpHkFKx3nmV7Sum66NrpzHzwq3rIqynQcu8vtHCeWQnDVTSM87ceRGn-uf3alBBbXQVokLwrnDIyg_wHBBBIwc50QmZpGS7ODJmKL_NmD5AclI1ERnhWkNyZkpBibMNIKCKnsy6cKsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=inJmta8y9DdkOmGw0F7mKhvvERJPGiLQEX0ogepHIaq1k6-ItJTt5ytwd9ompn0RRUoROy1vHiMsDr9Bt4twvS9Dw6mXesLWM13VKe_nYeqMGoBiRHV_AvgCsneT8GKJsAqNofwSkrXfzEqHBBpxXGjITfc4czEs0S2bjn3j2A6qNhnjGmOZHcSXtL2EPhFwMbMp19adoq7kpqqyuapZC3zL4ltshUlB_BVmnlsPhTAAuCAZbtukjlM15hUTEPJaBfvk1ZrMZgj1kengvEKTkq8-4ecINQ0W4cXFtP3x_TY81IWu2GdU_2SADrvRZtesDsibOODqiJkwO_xf4ZImRoKT822ike-HS09c709j_KcZcpImycJ1W-b7B4doIfGj-h3XD1Syn-tqescIfYEpNcUybm_UwZE0A58TITCvXFtWUuo8QY7-4Q5dZBVWYP67m5XLxfP9cSzMkG1_FEnR01sNWxkXJEz_y4smfMoFBaTTkTxMib2aIqGFFh67YgDBoFdQ3D1LhEP_lyfdKBQwvUPi7AYkLDOoDpHkFKx3nmV7Sum66NrpzHzwq3rIqynQcu8vtHCeWQnDVTSM87ceRGn-uf3alBBbXQVokLwrnDIyg_wHBBBIwc50QmZpGS7ODJmKL_NmD5AclI1ERnhWkNyZkpBibMNIKCKnsy6cKsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re64v_vPPaDIiqqMWCeunp3BMDRQYQsrhmhrwOu4I2_MQLXLjiCf4eRYX749IIqrv_Sx4Oq0KxJsGbcHT9fzkApvwldHGGV18xrCysrMLJvkoZzYcFzyosWtF_4Uy4dWHfMEZoK-l_XiEMPTu-m_0FN1xFEXGiohgMFqm7vA_mZr4GOLdqmadv_cs136iwOijkUj4_62zxEU1EKbB64g7VepJvyUouZPSgmaJZsTm_BQvNHAK0S80u9ZiMHdGTxbBhHVaBySLg_NjbG5yCJWYLX3jgOIl83spx5UCyp0bhFK3Rb7yhTWv1tg8ldLyjIByawsSKOYHQDjMvg0pS4Ulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odPLxeplejxS_ZOJNoyhB18yXLIOHpoAnG5PucARzknrns-V4IqL_l_B78Z6RCkjKnU9vNXIPZCZ9PHfTQ3NsC3i80j2MXYjbAxDMnojSr9F6xGBkQpJY-IGDzrIOiA0h0GRjvCCkC5aeHc_B3T7mSkHIVFDGeq7FCbCDt5KnOeIR3smSkL0xITSqo29oiuF2hr7s1fmjTRGtgcNPiIoT02BnwLMSgNXQvKpePkGA5hIOHjV1zjHvjuCJL3UDs3YhSD2q_gI5jbFsL9og6BRJjuXcOBBMYIBLhlYKXJBtNplWO0YYyomk2WT8TRnWqPVg9ku_hvKeYCL34QJFgV4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=timWbGBp0Ehm61ApSvdgK0sLVFpMTZGmXQ8d7cwz9C3xiZnBZN9jWeT27Us44xJQZ-0YyB4zkH0jX5xwOw9q3SKh4YnT8AUWoAFWXfMDpaZ5Uf4rmMaMEPwQInp2jm42u0GScZTW1r7HGrEciJx6Sjbn97TNS4jdmPaHGzwnc6mRFcD2S9iEW5A5LHEnnTEWMTrgpPxgIZe5LzjKq1QVnUePOj6uikdEOCe0Nu5Mr6pprKh1cXkxiDe696-AHepuLqY5IfQ1pbxwewjkQxHEHykZ0c884T0MR53sXKwRiaEsogGLeobBLlRr0xy3C4LooAQH7C27Eff7SbuJYEKQZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=timWbGBp0Ehm61ApSvdgK0sLVFpMTZGmXQ8d7cwz9C3xiZnBZN9jWeT27Us44xJQZ-0YyB4zkH0jX5xwOw9q3SKh4YnT8AUWoAFWXfMDpaZ5Uf4rmMaMEPwQInp2jm42u0GScZTW1r7HGrEciJx6Sjbn97TNS4jdmPaHGzwnc6mRFcD2S9iEW5A5LHEnnTEWMTrgpPxgIZe5LzjKq1QVnUePOj6uikdEOCe0Nu5Mr6pprKh1cXkxiDe696-AHepuLqY5IfQ1pbxwewjkQxHEHykZ0c884T0MR53sXKwRiaEsogGLeobBLlRr0xy3C4LooAQH7C27Eff7SbuJYEKQZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_07CxeSi-zRD3MP2sjEXNrusg32S2Bglw_fkFA3hTO0yh-l0kdbsi2NtcmDf7a9ZyfZPxv-StduaFBRUdF4VNxAo7g8TWrDNhmwxgXkpx6TXn-wQFG12QZRzkYsYJsH58Bqihta4VoY_WtBBDoBR3FVUkdrimcC_Oblr8EK0J-Co3d-Fb2aippJnLf5FF1xVC-egOE_tZJv1klUnCqtlKAeq6ErkgMAXFeJsmiGy4DSOddC4j-em7GtxKBO714GK7nUGCfrT3ofsgR-7hLau9N3u2AIJYFWhzhO4HMfPXt_F9UcEO0VrF10i445fB94N272M-ENI2-6-_0-l2YdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR8DROaZotEQeLHXPLaHQNNod-7tS2KeQxGoX8kgTMKT_LLHrVKQzD34G8rXzyIxyKxNwQ9DX4jJr1rda8COIvhqUwvPnxgdWuKezZ3vzNxvER5WmfJ3wsw__3bwBNV2U4vNfmUQyQN7kn3DlKff20OsDtMi8BbO22iOiOjQbkzLdQJpDkj4KIDDHvd0Rc5FqAm8oFUUYMSMQpE5_t2m8dxbpMF-R0r8SmJbfpzFXExgcBU8E4fNvNRwHvRsdno-LPgGbo0AFyr77OX35oJdimUKo682GJfCLTMomLJsqgx13eK9MK-bbLrKo8Uc__6Tp2jCtM-qVPyE5aUBNv7RyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=N8cCMZnasqOFsRHKWq5_UJd38FHoxESX7pdwT4kPSX5uN6J4jYi3_qxTcoCfpH7oVX-65lRTq_yGMm6l7010_qfLs7pAGihKQiQy9WJnoU3iSGO0vv4k3pcammCOGgyGtOgNHIeeI1s-QgZ2KUxH9xFL7ysmo2ky8VADkL7xDr2vsxFIUGVsNfrhcCJoflXg4LKNaslfGjP9SgjSgmF4M6JggLe-RBYFEqx6S1wBcHfXb7hCpiAJUfaRIqHPossTcMqI6xlUluraSTdIoaDGBam4PtyoG4PTIwwYY9nPFXfA3AQdLgPdQzh9gv-GxCfOfxhjrHjC_hJcKR1_46QR9kKd3to8DxzWL3gmOsEVBS95ase6F0IuGnXCo3-nKan1FH_2dPT9UcKW6A7BjctINVv_BaAIwEBlJnHxWE-YhZMtzvAT7_n5prGAUBP75cmaAff_epQorlOPma6ziEnISjK_tRNeCvIk7GzueJbz-gwuQ8DOkHtSXnT56ztmG5dKSw8hPSlygtrp-5pntXuGetaKpRGK6-WCIZ7jHv8kcVVJc2Er0HAqHGBoE1BriURpeLXHjymgEzMBB1zpjXMWxlnE1S-KvtI57gdHEXTEzfxBdeyiPSqhnapQvscxfErgIfFJC0y6EIzh_md0aZaeNcwy83J2-kUul6c5IoSjmUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=N8cCMZnasqOFsRHKWq5_UJd38FHoxESX7pdwT4kPSX5uN6J4jYi3_qxTcoCfpH7oVX-65lRTq_yGMm6l7010_qfLs7pAGihKQiQy9WJnoU3iSGO0vv4k3pcammCOGgyGtOgNHIeeI1s-QgZ2KUxH9xFL7ysmo2ky8VADkL7xDr2vsxFIUGVsNfrhcCJoflXg4LKNaslfGjP9SgjSgmF4M6JggLe-RBYFEqx6S1wBcHfXb7hCpiAJUfaRIqHPossTcMqI6xlUluraSTdIoaDGBam4PtyoG4PTIwwYY9nPFXfA3AQdLgPdQzh9gv-GxCfOfxhjrHjC_hJcKR1_46QR9kKd3to8DxzWL3gmOsEVBS95ase6F0IuGnXCo3-nKan1FH_2dPT9UcKW6A7BjctINVv_BaAIwEBlJnHxWE-YhZMtzvAT7_n5prGAUBP75cmaAff_epQorlOPma6ziEnISjK_tRNeCvIk7GzueJbz-gwuQ8DOkHtSXnT56ztmG5dKSw8hPSlygtrp-5pntXuGetaKpRGK6-WCIZ7jHv8kcVVJc2Er0HAqHGBoE1BriURpeLXHjymgEzMBB1zpjXMWxlnE1S-KvtI57gdHEXTEzfxBdeyiPSqhnapQvscxfErgIfFJC0y6EIzh_md0aZaeNcwy83J2-kUul6c5IoSjmUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=nGzvSO77UZs-e8vP-H_wbGIPkGoAxHt1AvYk5_yiocVAF0IMopHPYdUn7ZUcWZ0COB0EoBwub1OriIsKt3ZOtXf1uJywBc_vjQHGglXdeoijHdrtNR-GQ6Vc2p3jwd4qZxT-PTSH-iT37G5R3qku_QXR5c8SCPK46wz8r0E-7UBJt_z1ZKs4fZHpgceWwBTa7hPS-r7dnD_pc8BtAtObnVKeztATWTuKrz_LrnPD1no5cpdOMb1u31QC6J_4sx1Le-SofhY-1MTKAM1OmSEC8DUQgEEJgyi76g18ElXHtc3ArYjjR6_p6lLTx4SyUZjZaeBwoB6Ue1ML3N5qHpELLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=nGzvSO77UZs-e8vP-H_wbGIPkGoAxHt1AvYk5_yiocVAF0IMopHPYdUn7ZUcWZ0COB0EoBwub1OriIsKt3ZOtXf1uJywBc_vjQHGglXdeoijHdrtNR-GQ6Vc2p3jwd4qZxT-PTSH-iT37G5R3qku_QXR5c8SCPK46wz8r0E-7UBJt_z1ZKs4fZHpgceWwBTa7hPS-r7dnD_pc8BtAtObnVKeztATWTuKrz_LrnPD1no5cpdOMb1u31QC6J_4sx1Le-SofhY-1MTKAM1OmSEC8DUQgEEJgyi76g18ElXHtc3ArYjjR6_p6lLTx4SyUZjZaeBwoB6Ue1ML3N5qHpELLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4FIVhS-YThZo06mF9GkT0nHRFmPIZMJ5hTsWYVeRXqY75mR3Zi4xwBa8lo-yXr9Eg_2d_3h7_km13ZJt3KAvczORmZjSjeUpxoziuIJN6CQMQnqGd1ySxo1evyrVyhudWswh49R__HrjHNdGUFs4mMyR9sgb2iew9qRGeO2cRvLPIwDPi6xOJlLKiD2HXyfn8wpacox3L8NMkhiLo_2TK-lSkNirBZHvXkZ8UucyAXTYlUIc_Y4v9A4dvJssFgWoW4ktvY6mGCyY-CEo-gSr47_BJeML2tLmWYS4IsbJF-Oo34VqVO2kttImiimWHCjs6ju2kqs182Ez9OCO_brgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxIs1l2YZU5jktTFrU1p50AaTK9S25LMngPLf7eRXdVkzh5btezJbTc2KODwTDeHQH9Hf-nRFRLyuV1w7NMpCNw2eRdfJf9cfSPubJhoJIEnSr2ldZdNWK87wM09JQbv-s-uwSc9qCatYB4xrGKcJ4kWGWCmG3dhsgm-t3xqpb6ont-KXctre-n89Yz0jNSDRNrBeWrsrj3MoCEurN4mi_5Tj2hQ5EzMQT__yBcTmJ5n2iWVlRo_r1cR9TV3d8jeN_oQ3aXUdWRk7R4kDC_v-q1Lxa7w9i2SvSM8CDA1svx4N3jbvdONMAQlnwYzlnsit-RzYXtyNltP5M3x9eUDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xdh_nmuaUqj1A8J92nRHi7ii2hUJMkM3RlhG2AdIhRsPm7KQIeloWHbin12TBP0GRWiuChmX9Vtxzx2H6D_PRsIOfwJPG5ZkFR0KEhpuScYAQPHHmk7oWR3fSHvtrLfDUistHbkPlSzjjuF7WcP9RDwiEs4aC0SbuyCqQiCil9VgFwMoyia6idcJAPxlnu5jAwKtuCKwfSbUq6HL444X3HRL3sir2lu9hV0Xb0LO5cYf0ZZAQ3kQRNjYlpIf5uCyQXwV6rFb-Vh-OCQV7PWAHqw6dHENAFVCzUEmCIM5bWfRdi9rDgBVqci6Omhh7UxPMt1IbQYu7ZdcNTB6XKG5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiOch3wozT814MhxS0xaoHNhP34mjnmSHcU7QN4bigoTgKZyxG9Gc12HVLkFnbqqtQ_jww1W7W0cuUwBhFrFyuYYHFvZW7xn4ulrnKvqm_OstTffbV_SAul9vsfzujJIJAdpKkMuPuuP4E8myWoEnNZw1aLHvsZ-jjro2tKJfmL2NefbBtdOWGwUsX6e2ZAMVtVTbFUkGsREmnAiEUfzF7zy8-PXIq0ngbCe5U8Z4Avp1h_kZ2ZSgJllpomBWR3ECl-PnXax54nVP9UmpCAMEWFGLvMrpX-AGG7HOZ_0IRSwByDsLkkHnox1xIZR6QXmpgKQf5oKWHQwy-VpxlAjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsWNfiL19T1iR4sjTy7FA9IVeDDavgHYAsS_xYfHelx2kPA0ePJXFXcbfPA5NO0gxsi1TYXzVwkf6qR-l-3VuTVNoYupq2NWWiezBglhns0ObRRGQd9C8PIpkrJM632wc2l3QfPv1RE_rHyBFv7sDfbAfNEbgJNf29tTsan7nD5T4IjGB71N7UTugHeJxyK7akUjUrpOsm133w840ClSIeyy1woM6VHs8BKRZGvsNUBqN-lk5sVGjMUgFRMJ3F_fwreOdsEo1mK9tPLhUfgfB0sTSvxqbvhWJDtvjQGn9PRB3gS4M0Zrnep1My_oXjUaK0IQEmQjkhtw3wrLf5RX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A53T_hL8fpKVrhVjUzdmK6kq4IFRkLwXZNVZ0dX8qpE9nfaOl-HK9DBxxhxxa7oAZDrhJh9-uMBTI-1wLE4GXnb0ElgvSk1VQjeiGZyW60dGQO8TglS_fshHdSBRcNVNQHslaSOgR5wovf20gzYtovvcc1H924xxWTcOPCVqO3-P4pyBgJDtTtnNb-CPix1APcqqPGyqVvURQGwWB4IpwhMo-UfHv9wxlzxIIgtX4fLwwoBkJZj-TuTy7zrgLAQHcKjSSo8gQpayI8BndKxFpmx8RXhus8NVyftKEUbsR7J6dgMr5zmo_buab_TJ5oLtqAP614au3Ysi08HiMnbl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=XFAnkQNZz826K25gL1DHaPQ06K5_tlQr5X04JHkJE2q6OrSuWj935XzqH2YWf_rBLK3KcrlZYlD2h0VyOQS4DJ4bPo_LAR_Xfr_Y1h4xm5LShUkPQxNUw8IPYhp1z8pNveP98EV-x5Pnsb6_LeaCBYEj4ORdHOheaP8af81K6JgXtaF8EmvuoAbieO_9nYeN-orMfH4NzhuKxfNuYNgtsiif72k5Xjj-WFd5Cp0BN4N7NGLpe_GbNleS_oMvI5iAfdEpnAj2sKxUpyKRAz-YVEjegYpqV2FP9PNqo0UA2eHASDhQl8MwfJQOg6vo_VULEksFgKAiENv5qsik1tzh2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=XFAnkQNZz826K25gL1DHaPQ06K5_tlQr5X04JHkJE2q6OrSuWj935XzqH2YWf_rBLK3KcrlZYlD2h0VyOQS4DJ4bPo_LAR_Xfr_Y1h4xm5LShUkPQxNUw8IPYhp1z8pNveP98EV-x5Pnsb6_LeaCBYEj4ORdHOheaP8af81K6JgXtaF8EmvuoAbieO_9nYeN-orMfH4NzhuKxfNuYNgtsiif72k5Xjj-WFd5Cp0BN4N7NGLpe_GbNleS_oMvI5iAfdEpnAj2sKxUpyKRAz-YVEjegYpqV2FP9PNqo0UA2eHASDhQl8MwfJQOg6vo_VULEksFgKAiENv5qsik1tzh2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pymmFrpEjP0Kz3TaLyPaD0Llmp5437K6LEl8T23IFAcPqDxbuxdWARq94mMfEREjGMeHk7mzlRSl7-AiwW35m9GXqJMbt5fbFUOgY_3KcY0ra7P3jOt5dhx4gigPvJSYpS1xOkFfkUOVN22fZrK7RxtCcROQjGxnklW-EBdPnzGaFiyso3IonPFE0yLYOA9hoOMfKt3QMfeNzQsFSlUtOmZfOpkn75J7kIvhPTW-kYHbKwiIeP1Z8QXrrUR13GgsHz0HWlLcKwKZApo8VUwAEVTZc25Qb6-2dSjnHzTMlGwrjzMhaszKtoKJHYNw4xWLGSjp4E2eFCKMejVsLW0i6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=irTWlWEoovhj_vDCqcINYh4oVe1RLkUreXxdki01BFGI6jFs1cvgekgIc9jdMnNq_gZ1hS54MiNC9mkTGIuVpORDK5RWXLnzhryUyMWVp6fmclylvNIfD1Iw3KhK71jV96_Yw56Y4-yM07VUO5v5sA9kMj5Ki11hebLkRfGvGjMOkkkjK70lXg_rROMUE6yxPGIWAHJUV4EzVo3jgANXkmQNVy1AGitcwH1XHnyfSjeaPEyUihBEiWS53m393d6du7Lvnvd40bQNqBmof2VG9DrLykrQ2cFaM9TpKyx8tdGtH73PUlUtv1pcgtUFzJ4g5t-wyQb5yJE-7Bj498lNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=irTWlWEoovhj_vDCqcINYh4oVe1RLkUreXxdki01BFGI6jFs1cvgekgIc9jdMnNq_gZ1hS54MiNC9mkTGIuVpORDK5RWXLnzhryUyMWVp6fmclylvNIfD1Iw3KhK71jV96_Yw56Y4-yM07VUO5v5sA9kMj5Ki11hebLkRfGvGjMOkkkjK70lXg_rROMUE6yxPGIWAHJUV4EzVo3jgANXkmQNVy1AGitcwH1XHnyfSjeaPEyUihBEiWS53m393d6du7Lvnvd40bQNqBmof2VG9DrLykrQ2cFaM9TpKyx8tdGtH73PUlUtv1pcgtUFzJ4g5t-wyQb5yJE-7Bj498lNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnS6qtAUa7R27Y6X2vQoTfjbRn0OnV4jFRuIH8v0T5xWHjAWCXrBNt3Hnj8rSSscagkzMVmtlFVFy7zbuXJYUtehXVRNu2I4x99DmOW-wc9NAzRUj2l3haOG3Adxeze9YxM5hSccNosfThXVo6rxCe-vpT6_NUJ86HVVf2-VYTx4DbXKu_jIUl77oVsX1Nma9tfw2oc69Wn80um7cQ3fvpgm7OZZZISNbSyysC1U8UR9vrXZQLZFmYeRiPx2by2N70VWD29vl6UiJw42M1yigpizfnVjc13gSrzkU2WSSSmTVlE2BZ8Fi4aZ06h8kx_Qtfi_GN5kOAVDWbHW8kIK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfwliRIvYOJTqjKkF4E4phsqjFy48Lzt6AQsNYPdr_5Mr-KAq6wPFi-N1ZlRnNNrhYY4n5mSf4XGlLyF8_NarOHads5Vruijt5xGuwW7dY_8iW1s0n8A9WxzepC7T9GbRbLR8LpZ2VzLZvZH_qvHv8Z41ltYFCnA5uTIp31lSPwf9AznLUd3u4CuRUgWaq2eM80d3_bRkx3Zm_2T1pjKyTanj8nXEo23Wqs2DpV0pxYPejXh73N_GzE214ZHQQXkMqnplEzXCMNAKXZTkE9lIxx_4Omqr4pckGORTAjd05orQ5GnzDyZ35s63biT5gNpPWwog7ILnkVKD5hJO2Ka0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=IuITdJ48IXpnpFixMXmK3NH-mPoSL9UY6OwP-25eQWNI_nYrIloytGhRlzDBOLoXFJ8yspiXu4LTp_z6cJS6a6JF3H7APaAKPRixivKT78F_MxHOl-Blj90oJTb3sGZAnW3o7j3vo0ebkgCS9dCfPm_EI8diYYPQ97W_thvPkEIIMZGe8Dsr89HpXxylNi1UUtrJlNp3CKJjCtrtYeeEzIGxx4LM3CdiGDu7ehs2oQyZ8j3iSfsq9SXDIM5gPgsPoChn6gM8biMnD4yv2iNLxLTTl3JnbFqzmxBY8Id1wBzzVe2q1t3-fUA058tAYj9UoIR_y3WEWeE6FbRUD4iQ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=IuITdJ48IXpnpFixMXmK3NH-mPoSL9UY6OwP-25eQWNI_nYrIloytGhRlzDBOLoXFJ8yspiXu4LTp_z6cJS6a6JF3H7APaAKPRixivKT78F_MxHOl-Blj90oJTb3sGZAnW3o7j3vo0ebkgCS9dCfPm_EI8diYYPQ97W_thvPkEIIMZGe8Dsr89HpXxylNi1UUtrJlNp3CKJjCtrtYeeEzIGxx4LM3CdiGDu7ehs2oQyZ8j3iSfsq9SXDIM5gPgsPoChn6gM8biMnD4yv2iNLxLTTl3JnbFqzmxBY8Id1wBzzVe2q1t3-fUA058tAYj9UoIR_y3WEWeE6FbRUD4iQ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
