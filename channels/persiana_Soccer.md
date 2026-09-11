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
<img src="https://cdn4.telesco.pe/file/Mm1QRsHlM6A-W2CyiV4U0RNaha1SWCnq-H4Ys1A5fIadHeRKqNDpDVjeAIwo5nk4ydeo4cxbgjlD8KtKq3tvZcR7Eye-9-aDMfTEqsmZRQazNEiE8uACIcFDjFeSn24OOS818GhOzOWdKPnMb418RKkenDd6pkQBvNKp6bd2E3iTzGAPn8B4sD-LkKGbpHEoTvqmTSkubi8V13x3_tP-BaE6n41U_gV3JAdDsbSY4cgUSqdPmV3QzElN1jTrxPkhkjHXqYPt-rFbcpuJ9CJm-SXu5MWS777BW8pxgMBxlbUfzB6RdC-WxelAjeCN1cyI19-kABnD8GxG8RowLPs7SQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 533K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 19:04:30</div>
<hr>

<div class="tg-post" id="msg-29542">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaxcjMdHCybd0JMMB_CocShk0M20zcfGqNdOnvCrAPADNjQxO2aGEUZMtXHmXVP_LwA9Nqhl1b-aGSNXP8EpwjegfGVp5UuiVKbh_lPu7cL31V3BFAdKQxAeFeMBUkET3D4gnrYiCqr5xndiLi-zcsHInN8wEOAKUjoJ7pVEttEKXCkUeDVyqhqJC26CsxNWMZJdL4S31l131ssztlWdSD5q5ByJ_L-CUnRR8bj0_okYFlu4ipSasjd3EaMivuuOJgCIqcIq1BzMZI-bNKEZviOaydesJSvarRSo5PafJoFRsK-sNNAI_k-dY6UnZSQ6ra0rkZMJ-SZvL-3jzy1qkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت برگ ریزون؛ تیم فوتبال بایرن مونیخ  12 سال و 9 ماه‌ست که در مرحله گروهی دور رفت لیگ قهرمانان اروپا در خانه شکست نخورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/29542" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29541">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP2Q4YfIQynAdJB0B-XtJFbHGb5bW-sj3rXAKEG57K-jN0qCjHpS-7qfD8kGoh63W32d2yEv25_zFge6_hAAS2QO-IGsPelpx2lomqrdSndQAqGC9MXOF4JaXdZ1H2ns3xPoXu-aE046CuqpeidqEPf2ZeZ_lO_ip_noio_uUnUyFqy6HDwmjQE1BzwAmvN86moc62O1y08d1SpHJKIecp_VtolZscvglbdgAn5Plh4q5LtwGfP4u-GIOaVyxjorqpEtmNl8q_rRMplrhzHc8cqhzkPxjS8Zye89a8wr8X8JfkJDS2Y2H7c5cc0ytehMuqvh5RXHb3WBgvRX3o7Xpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#فکت؛ ازشروع‌فصل‌گذشته رقابت های لیگ قهرمانان اروپا تاکنون‌آرسنالِ‌مدل‌میکل آرتتا در وقت معمول "۹۰ دقیقه" متحمل شکست نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/29541" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29540">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBNKSc6Hd6ZylpIbk4LDvAoiEC7psCAPk5Wl5jGRLDry1yLNcO0ImNTh9iHsQfOBkd1JHHRawC8uGhSgO3MXLaNnTjjzf1LZVbCZy_ZL8MMd5194lq41y7ROOlJ9f9H5xAL2MI9ckHQoFg1zgVbgkG9wlXNsxjizdHzffBVLUFWXcU0w4Xmgcyv596GbDzlqCfSl3vQaRGhLQJBGt4t6QK05Hq4zJrI2jVvYeeNdkpt8KquZxtoujWnSVeii3BLzEuKOjK-I7QArbYHONGK8rxyLFBKNF3gXcQVemLMOwCXizk6Aw2XDF5RSJKO2QkXHaPwopcE7-qHM48dzFY2qZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛
فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/29540" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29539">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=AUFEpWiT1nXasc1gCFEY5O7FM3xli7hoenfEhP5OyCagh9OBd0tW20-ISKtUOmlLDJAtJL1oEupcTgegO4LCJkwuwGHCujbRBMmT5Pga23GdPqzpGPrFGK6oAdsIp9uf7_Ra0vYiVeR4ZFiQk976u3WEv13FTCijFbr-OfwZIPpqH4ddVQLxzeWpgOkaGoEdYT4Vndeu9n10OMXs-1nOq7BxloBML7J07lxI_t5tyyhShxi-X-hytFJ-G1P2icd4Y4FlDK2gb9-45W7gLIclh0vaveb3QVvdE1mSCuzmCe0YUxDHtv84pfcBPbBhnd_GQsrIYmOEgxMxlnM0l-_SNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=AUFEpWiT1nXasc1gCFEY5O7FM3xli7hoenfEhP5OyCagh9OBd0tW20-ISKtUOmlLDJAtJL1oEupcTgegO4LCJkwuwGHCujbRBMmT5Pga23GdPqzpGPrFGK6oAdsIp9uf7_Ra0vYiVeR4ZFiQk976u3WEv13FTCijFbr-OfwZIPpqH4ddVQLxzeWpgOkaGoEdYT4Vndeu9n10OMXs-1nOq7BxloBML7J07lxI_t5tyyhShxi-X-hytFJ-G1P2icd4Y4FlDK2gb9-45W7gLIclh0vaveb3QVvdE1mSCuzmCe0YUxDHtv84pfcBPbBhnd_GQsrIYmOEgxMxlnM0l-_SNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/29539" target="_blank">📅 17:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29538">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwBjM2XuuyqRtympqjaJgR-0NPKJ6XRhN6mkI8OmE72ezKIC2VlEnRekMkqjSv4PYjMDneboyVt1FDJ7I0T4kr6l0may_8vlCOkf7VRpq5let1VkkzKD5odEi-NDwWHegCpuEdRymlcsURkYbG1xFB6aw6Y8KqhvsViFP07cCMZUUJ8B1AMCRxxDWy8lp8y1FDPAADY_b4VSTjaFkLw63QzsA5K0U5nY-BhoiMYeoAFx67ac8FLtTv2m9pxbqIaJxfqhQr4BsIxI-pybXv5_SAep1X3OdpUGuSnMl_3FLM-lZq8QLf37IClF2sUcXvoIKvTo4gZzAnSfvsGSN6EWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌مهره‌های‌هجومی‌استقلال
🆚
پرسپولیس؛ تیم مهدی تارتار تاپایان هفته‌ششم لیگ‌برتر با دوازده گل هجومی‌ترین تیم لیگ بوده اما استقلال سهراب بختیاری‌ زاده هم عناصر هجومی خوبی دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/29538" target="_blank">📅 17:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29537">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=CdyBquaifLGzmm6XnjVwrddyPqc21Y1vzbE8pHxqSe3yb1iArdDPyScTaGOaZ2LlNfvaJ42sIBVNwETvd4GsU7pRDBFJtXYMfXu3niqSj8Lh1-T2OI0bjuQ8N7X7roN8fA1VQ69a77E8ypvliWvjrFqv9hewshM2PUPwxex9G9MNPTwB9Jm8ZlEQHR8fdtJFzGlMCXGEiLJh6zAaLEqMjXd13Y_B4a-v71i5-A-mkpCGhTos5pQEE7A3m9Tk5Wqice0W1R0z1NvWvIF6751tSsjlKJANG84Z_JWzZW1DrRYgchiCiTa4GxH_WbKWJtcBWeh77I-qeizgxwV26zNF9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=CdyBquaifLGzmm6XnjVwrddyPqc21Y1vzbE8pHxqSe3yb1iArdDPyScTaGOaZ2LlNfvaJ42sIBVNwETvd4GsU7pRDBFJtXYMfXu3niqSj8Lh1-T2OI0bjuQ8N7X7roN8fA1VQ69a77E8ypvliWvjrFqv9hewshM2PUPwxex9G9MNPTwB9Jm8ZlEQHR8fdtJFzGlMCXGEiLJh6zAaLEqMjXd13Y_B4a-v71i5-A-mkpCGhTos5pQEE7A3m9Tk5Wqice0W1R0z1NvWvIF6751tSsjlKJANG84Z_JWzZW1DrRYgchiCiTa4GxH_WbKWJtcBWeh77I-qeizgxwV26zNF9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی دوباره شهاب زاهدی در بازی امروز جوهر داراتعظیم دررقابت‌های‌لیگ‌برتر مالزی؛ این نهمین گل زاهدی در تمام مسابقات برای این تیم مالزیایی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/29537" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29536">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFSS5c09ZBwuO2ve_xawZPmlyCMWHE66DLrCqL0JgAL4rsrbXoiuz5gM7toXWdzkitpt8QEQIHSBuuIvWmY7MrsVhYE0gzNXtSMi33_iHHQ8MmXC_mioYgpQR4ap_w-5fIANmpMKQXxrMPCkSvveyo1h3JRQ4FmCZ73FQTNAbyrtMY-0VdbpCPyjWw3-5f5xacTjJyptJQMt0GHSMAvJWedUVQD5kqfVrkqO7FqZXKu1Zt9dOlr9K9K7HKYWK8hBpVjDq6AG6ZG3Dp7u3HZGuwsavusF0MXpboLC2KlK1UikCO4yeVwGovxOFQPSppNqky4IzWO26XPkax6Q-l1IGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/29536" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29535">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFreexE0WqW5djYX7ex-gH6PDilVaHiIdO_EXhLOpzV1foJCFq3SnZtQ_TFdc-76WhIoDye3dFNz1U94w6bg4VwlSgkAuVTrw1OJM1gSVN-xeePF8d6cRHdJhLN2CaaGlw3FgkkTd_ZBqzyCHERxFIbUD1B1386Bao0_KhxY0jxW8yppMFUZrXCAasuhykIkMzhlDB_w0mrPDPfYimvZPqC6yAshdDE60f7TBRgJtKFjxhrKmj9G6q4RmgtfM82m99AiBy1SWyH4e_w2ui4XeoPeIw39_sqcbHVyy_m98Ay5yQSI8V81GK6E6_kcEGg6t4dKzDDLI7jZUpxcRtR24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کار انسان دوستانه یاسر آسانی با خرید یک خونه برای یکی از هواداران استقلال از زبان وریا غفوری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/29535" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29534">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJTg_4JWhJMutSF9juR6v-Rx5cLiBDQtajl6fzgShEY-VxBE1hG32VPMKd66p_3TGE2Uw5f2rG_uZkoZNtwebfd1iUdpwVFBzIPY9lp4oCaf5T8gM8COxceDj5IB3YPdJVJqGDiiHcSriw3YD2AZnA1tJ0q-25IrYPkjFtYEpyuvdufZS7nK-ujz6CYUzaTCn5Z6s4kSshwJTt4zCY0YLJfBNsjc6Cr4Nu1T4tMASS557iRJ5oScfs4BSYVhuyazv3ppJsletOkmRS6t1nEDpriyns3-I0qoGximX53FmL7xy63_T0hMq73PjsVyQwBl6gjculXUYZyhDXbn0d8lDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به گفته کارشناسان؛ علت اینکه فوتبال محبوب ترین ورزش‌جهانه‌اینه که شبیه‌ترین ورزش به زندگیه و دیشب یکی‌ دیگه از این اتفاقات افتاد. دیکتاتورها وقتی سقوط‌میکنن که خیال میکنن دراوج قدرتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/29534" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29533">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQEHSIGQh0yonWPhUzrLjLdL8qCbrSSwfKIx_6VHp6l4WdA-VzHad3Wbp6dptdzFiKPHZKtOeqWCZZABIoAHJx7sdNw4X42e7MxtrzihI7YtmfiG-TOjpgWSnmdaZ_XhadxRojcCMXBJLgCB_-0tIJYiTr24tPhglFHF7Vk4nf5GElMK-R-MX1YiRNnnB9ch5KgGDfl6_Q8zOJPukjEO6hgJ3rEufnD9Pew3KV5zOeoGbAVq6gVxByFkG6D2WeH1FLQ7PlGyNFR_ng1jJrBQpj1qB7gzJdNfMX49irbgZYnk6wulH_mxgovptPfFZUbrPrTMyO8Nfk1l_eLrF1Xx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#تکمیلی؛ سران باشگاه بارسلونا به این نتیجه رسیده‌اند که میکل‌آرتتا سرمربی‌آرسنال مناسبت ترین گزینه جانشینی هانسی فلیک در سال‌های آینده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/29533" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29532">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcOnzwTubvczbZKDNId8hvVMbURi74q4ontiv4FzGyQmURXi4PFsR7mhvuPv_lzDR2GLaIZ3bHHGdBbMCJoDBGgef6eV16wWjeU1i4Scv-iHjZzpkmpSU8JXVj7V6K40aqm_Ayw93xmvMm2Equyu7uzdYKV9Pg2sR_4NhuEWrsRekK-gCxAjgXUmJhQcVkcH_OsYKUjeKkQ_Yf3I3OMEa6aAbHxKXLLyy-hdWbCUy6AdkadyXptpc1biVsMWwB4vLo2i-gpSfl28-5Pa_qSURzpiNthP8_b5wzf0raP3CEvm8VpJbWj9z_tMQ4XIO3rjRQHCjWG_v_7hkotwZW9eJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/29532" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29531">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnJw2w4DJtno8WyGWS2NHq2uvpo05Qh6Xic535DCJWWqYXKzm8Drd1jAYm0Y7guJ09Jrmzh178tTukf4OSwviEA0py6_wsPe4ucWmcG-xRM1FGJh4_O1y3chc9Jh0P3XCeCOJoYyA7wbiZGOxwGMkcyviADrBaz2jd8DkLPjvAkFDtJPL1TRGupvCm1pON2Tm9ELC_DOwMkSDPkqEh8JKHgVSjH9QGhTaF1gt2IPUnuUFFcvGjXufTJdKAtXx0QDirLfO96v6Cuh7e_rqt5Z4nzhuUcGJcI_5kMq1L0IdxyfjrFCF-4JFhK0eEmjQR1kBbTkNaiiZ9Isf08DsF3byg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته چهارم سری آ ایتالیا
🇮🇹
ونتزیا
🆚
فیورنتینا
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/29531" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29530">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlZ3m7HcstAgGq6u2zIswX5Ocnw4_VaRKoQl0I-Hx5liFrRXGmQT9pROxMVGJ-NcQ6aYCdjQFcR9Ddo9af3ZC1N1QftKhcbu_68YGL5tgNz1WK4uFXHsar9HpH6pnmE0h8riHe4ZEB_l5o9Sz-ouzpNJydSJxsSnJwBsRh5bdCL5Kay5uQTjdHgaAlzNu7pnr8-h8fNV9FLaL_S6i1zaoLy510nTfASg0Nae8w37YS6M0e387qQYNT2RdTUOy0wyVfd202bmruCrDLaEChKwOE8wgwn_nxmL-eFhtUldpMdkKXCCE8y8EO11sYsVmxCSigbNdssxSKYR6qKMNk9Aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/29530" target="_blank">📅 15:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29529">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ0RoWd-uja-3y3E3UU3aXBOfuBRlqlD5I6dHEYD30MX6ll5bpIkTtZUhx_9KrySE89BxcWMKYP_PTDTc7TFHyoJNvlUbWgiE-jPyC9mo-q5VBTujmWhci2e276rWCTcvLIW9salSUz7HhxVuMU9Ere_c77XcJLVRF4G8SFOM8K321tjkz2-pZy5JF3fKeWx_OZRtSOaJKmabcTb2UhazjXO0LZniN5ib5fKp16IZwNFZak6AMsqeIx1AJd8-sUbNMY8KM1r39I5LG4-FTHurWTgTnlu58cUuCqTHyJPnct42ECKzCWhnt7j2tOJ2tklGf5QtzK9KBPzDI67vARo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/29529" target="_blank">📅 15:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29528">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzboc6U4X11RlH3G5ZhtQjv5EgX1joUiAsrTcFja88QW5-4DD2u1q_xotxVUk4JqR1LfNbQw-cZjf9whNZAQLhit92Iq5bbM1N67h90PLnlQntaqtsL65TdzPjR9d01pezB1H6I1iYIQ8pv_il-dFZtEFztGHmRISFd-ERcycGdz-AqfYMK7uD4BS_STvBp5dODAl1ITmcz0pavHDM1eLGpOEDfP6xxVUlk-Pik_FpUw9Z90GqrmxkpJ4aiGwiUUPjzDkLweIs9ouMkBk1_vaPc0_i8vX-d61vsnDlrJhPXjBdSeOVoPv88ruXaC1FmfmsfHuW_bw43AdT5IUYH2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/29528" target="_blank">📅 15:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29527">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU-16LJajKqUzJ2QQgHb9jVqa33w2Pvcvpxs0HE1DBnyrUTSQrRZE-9r2cWqCps-6wLZRYyf6HoWt49sBudEHl64PPvzvGtG0Q1NEwvdX4HsNd-S1te2BqM6afjLu655lobu-EghEvuoHJ_JFLcmtb__Yo79Bjfga592sm1sU6_WtaDNTwsSbi2z9vZK5Bg61ZqQu-ErUy2d5a4naJ0EJOM5b0yUbf2p587wz9dxdqrl00UnkCEsrgIwRGPrjzewmz9YXOycYTmgP6sSyGdUY49PGzZfexHu4NUbgzEOeZfgnDyNvIgiWNtKFYVBX5SkVBwTNn4SDwMCN_NM6oZHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/29527" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyPy33Fsj0bR8V0MqfsAAMGhhCxkDQIAIKe2Y3KMKBpGRH3SkdVVBbEh6myOxxx65ODO6Mw_eiqbFrGg6ERx6bF1QmkydVa7XOEHV_Ct8tJk-OTG1WV1fxG4ZMHShR8vkNSZc35Ym6c64oAmsEU6ynazlipw2jwRImCwop5QKfeDenlvTN8S2zdfEFhwwCBMDSBpuq4sUSJLj6mJX4ZgodfdEnoWjbrll_lt_yjzo9mrKoZP5vIxcDzFH9-9aoyOSzEQCMi0Q5j2ruxcqguRkbvpChchhcP8636cweFU5RX3ASehYdBy6e__IBLh9PTkGub4n_ZamLxTC0C4KQccVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات؛ یاسر آسانی ستاره آلبانیایی استقلال مشکلی برای دیدار با السد نخواهد داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/29525" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcOqjuaw0ozs_tmLUvj9Gcqkkn5c5X8xU1j1h5n4QKb3NABHVljFA26VfX6R3_skcmtMJjyCRiR8B9wTKr1LZQflvd7Gq3KxfmHjtt9ihxOw9VPcpa-hBmrWGaUy0Shn9dIzx3VALJjSCi0iXynI6_i0xI4F3nZN5fEut1GELItw9jTU3hdDfjcvmsIxUQF4S3eDcmIrh8UUrDyRwDSp2KkP5qEmoEeJ1YFB722TfUSgmTWvltKq_gXUZXujzSZpYYuG6Grc4pvN9mUi3-Ifr-TTLXJG4W-avTmoaA7WA_teZRC1ikDN_cg_q6zP8lIMivC9nHWRCyaIxkhKuklzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئیس‌باشگاه‌فنرباغچه:بااستعفای‌اسماعیل کارتال مخالفت‌کردیم و اجازه‌جدایی به او نمیدیم. حین بازی دیشب یکی‌ازهواداران یه‌بطری میزنه توسر کارتال که باعث ناراحتی او میشه و بعدبازی‌میگه استعفا میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/29524" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHhgE38MKs2fQJabHfAuDehKJ_IVrKqmYGtXi1MtoWepo4SeNeAEPXUckoGLXgI-6SpqLxkiHWo-0ERm8uk_D3hfajFwtJ3eorhdwxHUcQVpLiMir1nMXPwLIXNPOFZHOsroB3dCMAh2B1mMo9KdP_p1YJ5oSY1ejHLqX53RxUjHuzY42XbQJj91Jny0xhF6Wdd72sytvQPPNBohqzIbXrSWD6a2fZHq8FS5Nod2HAxNjTX3PYPgWqMZK4yLwGJ-8LiuwRdNbHi94GLVwvIZ7lRi1Brz4lBJiaunKKYSCR54iPp-dq-TfyAlj2_OWzt3XFC_urAfXfk0P7GCyp-WCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر رسمی باشگاه اتلتیکو ناسیونال کلمبیا برای خامس رودریگزخریدجدید این‌باشگاه. قرارداد خامس یکساله و به ارزش 1.4 میلیون دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/29523" target="_blank">📅 14:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7MqCbQH99GDyI6ANWbprwVRqiR1B5Wxk1eaA3gB4okKHs4fkOWQg-WwtCiqahmAk6Qlg-NHsY0RWzN5Jm_1nGRCp8YPYwJjyEHGpMxfyB831uVUFAjUMOlbnJm1WneKxPU3wUl715eIhZdawdw7AurwAtmRcmWwX7ydlia8ljBBmyc53ah3WFf_YySHfcnaum_HyroNxYpWQykOkQ2dKdHCFBceUEm_eOkldH8OXCo3xvKjIgouMox9wQbTgVrCG2EkzcOVr-8bdngJiCAbtZFbLrU5qxdPHRxbpBXljKN83bFQL8XlC7c8XW_C4fKFZZkZWHRcs5VF0aX9yy3P3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/29522" target="_blank">📅 13:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjcUi92iXvt2btCtfPraS1WWDYRAu_i5PyjNjPB34Z3eNrORwRSiH4TgUHstO7AF46vEwMlvRqkW4fU2U4r4YkrkIDuVsHwKS6KjgMJcjOXbxOtnUhDInLCHOKZkDtmLf_74KGV8nYJCYm3mX9WHf4QeQ6GpO_9Mqb5Uy3xGN-qnT6f7QHZrS7qpZK0xxliQ_Dvrnxj8fFmWqkY7qb1Lv9ue50X90QB2AWT0E_8y_9YVLqJ7Dc2Jkc1Aqy61MeCAVwTipFr7Re0xwWzO_8yE3QuAkscLnBkGxT3jhPEs1Q_dLTZ8RqjuhY_yEgIu2f05SIVBttHJGlIxo-L10jF63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lvs-x-meWay4WZsgr27l7C9rgeFAQhzmqFa0CaUcefsK493nfwLRVuV0t3anB5TG4oZUXjqlaCURayNligdt-jlCP0XqgDZaIWOkW7MdmMH8gwnFPuC56SSMOEsLEvAW23roO2SkW-lbjSihY16N6EOzweVedFpoDbmOZqVJiECDqeXjXWlYeht7Du8Yu0yOrub3M_en3iCEaOkz3TXV-8d8B-YOdDU_qI7qKuMEbyzryZcdCs6p_A4C4tf-MAk36PDOnkiz6s1EIgafdKL1Nip1cN3ugRH-ViEYyNvX6SWYztowBpQJBL5Yigo8GxX-vFUX_7gmjw2yFakd-4Fpqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇺
دوخبرنگار شبکه TRT SPOR که پیش بینی کرده‌اند امسال بارسا قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29520" target="_blank">📅 13:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6AzB_UowzcgK0oEmyZ66yDB0O4YbG-jvdxsF2-BQtV1PptY_t0XD1FlcWHNyN1n6HGJrOM6TsDbIGmpwOoPh_-JtQnkjNkiYRZG08LRL-yBl8wgdfpTd4hXQWUyIho8GZiRhl6isViZmgYvd_-smuBZnSQ06Gc-im0bEj1QVeMP70oMXuHcbgGUfRVJuvCer9kODXuSxVbtjiyfeXCDy0pOL8v9FAPoShKvWvZ5fS0tfmdNApvD-RNGCfZR4UmOi8Sid34nfDkpZcGix-r1jjRoXayNnFzlGufU8e1eVZV_qdl4wfdwAQxmyT3Yo-chhw4qmBD_WcemtZ58nRP_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
🇨🇴
خامس رودریگز کلمبیایی باعقد قراردادی یک ساله رسما به اتلتیکوناسیونال کلمبیا پیوست. دستمزد یک‌فصل خامس رودریگز 1.4 میلیون دلار امضا شده. خامس دیروز درآستانه‌حضور درسری B ایتالیا بود که دستمزد باشگاه کلمبیایی بیشتربود و پاسخ مثبت داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29519" target="_blank">📅 13:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2FfLcRbCmgcTgJBSpfM2lVDua7oXx0MvjDJ1ESLSVbejHkLiK6pJPZ7jcpVvRwMDSBN7Sj5SqUPbchCzR_3175ZkN3V_ytt5LaVTaFG8TYWKZu4nloToZfjoTDQ8npP6f9eY_yIn2BeTd3t1AIQlGnzV_xAf3QQAsjXb1VVJ6Zry6q6EJa7D3taEy-G9akA6qG43jzSM3EOvzLQpw2cbktW_cfETiXV22oAZ0z_LbNZfhXiwLytcPjTP32vgj37kxbw0kgMeXKUDY4I9E5BfGs4Ti8DXsway3yB6hHcbaU4-TT9h5_xLhdFHmPBqXOaw0zJnVtzdttVnEDytVfUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب استقلال و پیکان از نگاه نشریه متریکا؛ یاسر آسانی بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/29518" target="_blank">📅 12:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
نجات دروازه‌ برگ ریزون آنتوان گریزمان در بازی این هفته تیم اورلاندو سیتی در لیگ MLS آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29517" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJmGW_SolXxuv5kTIv_Wx2TMeRxKosnIAM6CvyQjGBaSLuiqWjeOeTJavau3iyexVtYWgKOl-COgh0NjkocruJiRbsPQ26RMluyqiQmVTUkkyX-EpzAbdfWAGlzGnZbsutWbL71cQTveXdEckPkVUJ7X3aIJGaeys9gxwX0VEDJTdysEsToGsx9EoIhTynDeKLhpA1kSFN77hlhh7P8bOlBHXQauC-Urnir4beWrq7jl9ALYrlfapsU9JGsaZjIL9zpznsu2pDYOzoMKVmLUrfz6cCK05Jl-9DWyHYKbhepswjrdS1PZvyxg_Va1r9XK_Pg-1m4J-BSl1YW59kwtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29516" target="_blank">📅 12:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP9CuWr_6VVkV_sYfAKQ4x0THsWx0JPi0uPfg07RYfAUk6vbMj1GXq3OKF0sDeUj_oJoKxjA0rJ9l2HjCoD3r3nc3wV30-JUZ1P-ki9oEJ1x6fJfPHtMOgcigA16RLJuh4s34AIb6RKBd-9xn7AqkTSb4Tjzr1vUdAyUN1ocIk-z14ll8OlDdoIF8LVAQWZ2JtduAY9ck0j-NzLEssTsSAU8Wh4UcOqczfdravuQrmCwLzfclPJbbpK0YTJXI8sVfQFNY3NTfQxrKrWaB2Pt-wJG-a8ndhd29ZGwWOGpMZWX1pP5kI2WXiGQF3ChcdUV38uC9Jt8MQ0lQZB4FLGsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29515" target="_blank">📅 12:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29514" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3wkhJVRbLFLzI33JQ64cIeL2MYywWq2k7dYudYPz2eKHnvdj4jtVE6l7E1-FDQCCqolFb-S3syiQ0j5BdSbYYydajYyHjkWeIYRzfhnTmEoFFsp8RSqKlcfuATRpLqcbXGU8IBcULUEzi_TgJ1EfGPNI6YzbCEpt6CpKJRSJpdUoWq40lFBmOrpLflMlexj4crshR5YWjcqJ_RySCL1-uMIHwWBXXhbJ5xQFnEkjp2zy8f2sf1lacqTaNG8uu_ENnb20H2dfX3b9JTDC-BdrLF1ZBfqvT1rCeV_BVLqp1lh1gpMJ_pxu-cORyY9_Wi9m33XtdchSHBdhw2lyPEdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره منچسترسیتی:
یه صحنه تو بازی ما با پورتو هست که روساریو داره باسن منو می‌گیره. دیدن عکسش قراره واقعا جالب باشه.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29513" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2CRFjQ7KnUDcDgP9cOsGv3m2Rt3jsPTXKVkJ6F7yrjKuMHZt4hrY_ijH2tio67fT2u30eWsRycuZYpGKEPyJ3h8Ji4a0_cv3GS7mtV_AduyOi_WSfYbNYe5wheW1mzUf3fEvfnJgOz5lz0d5hEMsfqSFHeewUZQ_6luya_2z3JNhdRqwv4yJolp3RidhpiFA-QRzVEYa-sVHwRvIf7lXgcBb1xBFJl27mr7HgJBKnWi6C_UVMef-i0o-wTntiqum-h86_rZvXsstxLAvfGxEPgIHPT696sx8ZDHb6JzxGkv2Krq4qdK-5soizhD8WokATIJvvVisdjYSnA6SU0yeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دی‌پائول به لواندوفسکی در حاشیه دیدار بامداد امروز میامی و شیکاگو: تو دیگه کی هستی احمق؟! من‌دوتا کوپاآمریکا و یک جام‌جهانی بردم. تو چی؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29512" target="_blank">📅 10:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ30_tlNYP_9wefwghcNfOyrpu98VCCjjqjjBK6zVWJfbm5WXDjjle8ukDEXmV166mTAT3MBURM3bQ1WI1CXsaUuPeEGe9GXM5PFOayId2cYd9JBhl-QI2uZ-uTsItcmxH8p7qWQIc-9EpNP5Ty4SfkFUATOkfxdaEh-rkL29Q0NE1oU3xSQTkOHUS1rFk1q7Fkd6miVuTCXEJSSUzdTxln2eBk-KzYSAmupYWyfraOHqpJ_p518vF00WsB5tcjKND59yLpixBTheubdb088Q9nAYxkR58M8SAYVRcZQwAxWcH5RsNRN65-BgGY3qsGADHTDhQTwESWBDHloMlsjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس:
اگر کریستیانو رونالدو سال 2018 رئال مادرید رو ترک‌نمیکرد ما پنج بار متوالی قهرمان لیگ‌قهرمانان‌میشدیم؛ لیونل مسی قابل احترامه ولی بنظرم رونالدو بهترین بازیکن تاریخ فوتبال دنیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29511" target="_blank">📅 10:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29509">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=t_b9YfyXXBwxWvYlac64pRM4UUOcR7dI8fBtEBxRnLPxfBzDjhQ03wJtETOvj9PMwqNdfFUAuncYuO6BQy_SbLIx165MrgcLZNV2pF69hNGEP0ACgatr-BazPIs00gOjYrPhO7DG5zNJW5PZnNyNu8MwkNgL46hg08Zgex4kLrmrOxtaqt8YjP4gD7lcdD4wPeMFDMrnPZP2i_QfeoBUEggAxJzlOPOauyC3xTerwhgVMLbB4To8g2GsBwmYFmIl31Saeir1vmU6_k-iMiLVcu9IoRpbdzje-jD3l6_MN6bCo-uDXe5C-7BpC8Q3q9N6YrKyMjdL2_nHXq2R7FMjbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=t_b9YfyXXBwxWvYlac64pRM4UUOcR7dI8fBtEBxRnLPxfBzDjhQ03wJtETOvj9PMwqNdfFUAuncYuO6BQy_SbLIx165MrgcLZNV2pF69hNGEP0ACgatr-BazPIs00gOjYrPhO7DG5zNJW5PZnNyNu8MwkNgL46hg08Zgex4kLrmrOxtaqt8YjP4gD7lcdD4wPeMFDMrnPZP2i_QfeoBUEggAxJzlOPOauyC3xTerwhgVMLbB4To8g2GsBwmYFmIl31Saeir1vmU6_k-iMiLVcu9IoRpbdzje-jD3l6_MN6bCo-uDXe5C-7BpC8Q3q9N6YrKyMjdL2_nHXq2R7FMjbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب سسک ‌فابرگاس سرمربی جوان و موفق کومو درباره بارسلونا مدل هانسی فلیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29509" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29508">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=izb1RTtewSIevB-eeV_rnhLYpJ8ieqtFs8QBC0SpOxflgoeMV_AxS4mpH2UAkWLkSI6zeM7R6o7I15sOTnLuAgzbXa-BiOk9ri4B_1_ZHmM6Y2OpLJh1qiOGfORPrYk6lJrTSMXYWQVuR1Sn5m2t3bzAnoJJyiQYvuYgrILsMBeiVXZjan8Vvzsmk86Q7Hc4KCLRkGsArE3BoegCFuYE2GO7Hkfw2XfKn7ywNrJepCXG1NFIWRo5y3Fo68INhcy1ZLBgrgG8yEcdW5cF56uZUwqExqr0rVqcma7-SV_CW78NlO5is3y4U6CXWti-7foOzWrMtfc956xSx-2gMJBrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=izb1RTtewSIevB-eeV_rnhLYpJ8ieqtFs8QBC0SpOxflgoeMV_AxS4mpH2UAkWLkSI6zeM7R6o7I15sOTnLuAgzbXa-BiOk9ri4B_1_ZHmM6Y2OpLJh1qiOGfORPrYk6lJrTSMXYWQVuR1Sn5m2t3bzAnoJJyiQYvuYgrILsMBeiVXZjan8Vvzsmk86Q7Hc4KCLRkGsArE3BoegCFuYE2GO7Hkfw2XfKn7ywNrJepCXG1NFIWRo5y3Fo68INhcy1ZLBgrgG8yEcdW5cF56uZUwqExqr0rVqcma7-SV_CW78NlO5is3y4U6CXWti-7foOzWrMtfc956xSx-2gMJBrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از واکنش دوسرمربی بزرگ دنیا پس از پایان رقابت‌های‌جام‌جهانی 2026؛ یکی نایب قهرمان جام شد و دیگری‌از آسون‌ترین‌گروه‌ممکن‌صعود نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29508" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29507">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29507" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29506">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=ei5w0t-zUUo-y31fFj_kK984QUx0Cgde6zsdAgNbFMwbFy9OyhnKAzfrUPInCN8UVoV3fmK9m6Yq89kg6jtU80nKyJYPQIjDOSHcEhf81ERo2YFp1reT6pDzOsfWogxCOAlRZTzlhgQC2WxreGKc5CPigJKtSwh8zJzk8vVNgOeS1bkcfI5_SogsgAEpJ4eiY0ZTJzwVJFOugjJAA--KYN0rpA_rWwlNSnv2VLK_ZX8UjcOEvuFqra3vvBPDueLjxeQw9rstB5Id_1iBeZLXMLj2RXpjRyktB1LAni9P2SH3gmU1pbXZktM5Zhd36Q8JkIZOgOwnoqYc5nAUefyphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=ei5w0t-zUUo-y31fFj_kK984QUx0Cgde6zsdAgNbFMwbFy9OyhnKAzfrUPInCN8UVoV3fmK9m6Yq89kg6jtU80nKyJYPQIjDOSHcEhf81ERo2YFp1reT6pDzOsfWogxCOAlRZTzlhgQC2WxreGKc5CPigJKtSwh8zJzk8vVNgOeS1bkcfI5_SogsgAEpJ4eiY0ZTJzwVJFOugjJAA--KYN0rpA_rWwlNSnv2VLK_ZX8UjcOEvuFqra3vvBPDueLjxeQw9rstB5Id_1iBeZLXMLj2RXpjRyktB1LAni9P2SH3gmU1pbXZktM5Zhd36Q8JkIZOgOwnoqYc5nAUefyphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرفان‌کرمی گزارشگر دیدار تراکتور
🆚
استقلال خوزستان: گل عارف رستمی به بیرو بسیار شبیه گل ده سال پیش کاوه رضایی به این دروازه بان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29506" target="_blank">📅 10:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29505">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59654769b7.mp4?token=bF_45DXNAA5EjUJY60iasuezeGmZd8ek_uRUA0zhsCJAQ2yAcOVvq1YVsbmibmXxb42oO2oWLqRVRYwLd8tsbQCiULoJS_WNiISB4gazUfx_zhVNuheM80Ikc4Xs0O2QPVEYVO1qKnuHIxss1zIi6O30nPpxIHxUiC5ff-jU3gyANX64hY_vmOItgOkO_MMSu6TZ1WNcqaaJetpoBC4cZ0MZhSEuQeh_zludApTJW99I3psTysM6NNWaCZGUJX7metCsyfSawxyiHlNNRow5OXOcpLxv0Yh2clF74ZtFmX9HXH6lQj7bHAinIggVGpIhMg9bYCL4PGk8LsNq8ft_9KEar0vOlmI28rKa1KtkqVj0m5c1DANizTiZ0eG2KjGkJpk-jMk0_2BZqG8cdFHL4IEnVZGrot2JT5VD03Uf-UtlKEnuGLEGOZbANsQSSqu4OrbcnHWUs2opcE0bsGKlk50Btrmf3QtmYH_1YEn6tJ68g5ABkpjFfaTlvAt_RX-wUTmfxrVuCHOiqFmMGcpP7ak37emfaz60adM3iHHJuH-Ws-VGFNabG7DvYc3NzKHGc88TuFjvLC7EeoGBuX2dOsLXn6fVD4IJywIpW4DmTclcNq-7xwhURek2V4c_3OPpXC84_7ejnWUKO4FMbrs_rxOLKKBTczJ6P8kUyv_g6r8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59654769b7.mp4?token=bF_45DXNAA5EjUJY60iasuezeGmZd8ek_uRUA0zhsCJAQ2yAcOVvq1YVsbmibmXxb42oO2oWLqRVRYwLd8tsbQCiULoJS_WNiISB4gazUfx_zhVNuheM80Ikc4Xs0O2QPVEYVO1qKnuHIxss1zIi6O30nPpxIHxUiC5ff-jU3gyANX64hY_vmOItgOkO_MMSu6TZ1WNcqaaJetpoBC4cZ0MZhSEuQeh_zludApTJW99I3psTysM6NNWaCZGUJX7metCsyfSawxyiHlNNRow5OXOcpLxv0Yh2clF74ZtFmX9HXH6lQj7bHAinIggVGpIhMg9bYCL4PGk8LsNq8ft_9KEar0vOlmI28rKa1KtkqVj0m5c1DANizTiZ0eG2KjGkJpk-jMk0_2BZqG8cdFHL4IEnVZGrot2JT5VD03Uf-UtlKEnuGLEGOZbANsQSSqu4OrbcnHWUs2opcE0bsGKlk50Btrmf3QtmYH_1YEn6tJ68g5ABkpjFfaTlvAt_RX-wUTmfxrVuCHOiqFmMGcpP7ak37emfaz60adM3iHHJuH-Ws-VGFNabG7DvYc3NzKHGc88TuFjvLC7EeoGBuX2dOsLXn6fVD4IJywIpW4DmTclcNq-7xwhURek2V4c_3OPpXC84_7ejnWUKO4FMbrs_rxOLKKBTczJ6P8kUyv_g6r8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29505" target="_blank">📅 09:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29504">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=Lk8xypvZi4DTkiDDhwj_qlkNo7lzOc3gIyQeZzgryYkwiYv1jWytkPggPY970sMcDKbGhtFLvnl2IZtZRNMbDgAeDwY98XvbQPhcnDuqesl_H1Hoao_c0oVGzRJBYKn17A5zuGbRuGZleRWmjDHo81ZVF-y_wbczwD-VAHsEkoYEYFAK-k3QBXncfqBh4XlnYfMWw8fBgtSTZLdiNcc-PdWiZODLR1pGDjbkNii8y4z1ZembkT8hZRjWFx9YCpyl4jFpkZ3MtkCo3xPUk7I1ZcYggvDVg6i1PgJhiuUula89Ev5bojevhkjHGYSPojmJA2tQfFF0PKio9q7sjgY8WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=Lk8xypvZi4DTkiDDhwj_qlkNo7lzOc3gIyQeZzgryYkwiYv1jWytkPggPY970sMcDKbGhtFLvnl2IZtZRNMbDgAeDwY98XvbQPhcnDuqesl_H1Hoao_c0oVGzRJBYKn17A5zuGbRuGZleRWmjDHo81ZVF-y_wbczwD-VAHsEkoYEYFAK-k3QBXncfqBh4XlnYfMWw8fBgtSTZLdiNcc-PdWiZODLR1pGDjbkNii8y4z1ZembkT8hZRjWFx9YCpyl4jFpkZ3MtkCo3xPUk7I1ZcYggvDVg6i1PgJhiuUula89Ev5bojevhkjHGYSPojmJA2tQfFF0PKio9q7sjgY8WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29504" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29503">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95470742c3.mp4?token=mDQeajxW_DfLK758ChSertkZPZsDgWld2kqgRK-FftU-YWGwSutuzv4gu4ccPnASTbHR290vvQhIto1DeHuPmwFmrqdLldzbvCNayaqp0Yy-Ol74T47pZf5d1iGlQIqahiwB-_CH3PPcHHW7Y7zFruZgA2RobgH_1G6GQCdWf90nv7vaQ1KEMmqdusebXoLWN9zXYGvtC3qUSryiIXmDqhdMmPmWDwGUOppQ4pODw_ziob5e8J0DB0B8NRlN7dUrgdtdBoPnJm0grT5SDTUsGvmLSe9UfCu6rVfMyVRQ6vKeT0Ml79okyZEj4v91xbjozlPEjWbGatZUrPR42981SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95470742c3.mp4?token=mDQeajxW_DfLK758ChSertkZPZsDgWld2kqgRK-FftU-YWGwSutuzv4gu4ccPnASTbHR290vvQhIto1DeHuPmwFmrqdLldzbvCNayaqp0Yy-Ol74T47pZf5d1iGlQIqahiwB-_CH3PPcHHW7Y7zFruZgA2RobgH_1G6GQCdWf90nv7vaQ1KEMmqdusebXoLWN9zXYGvtC3qUSryiIXmDqhdMmPmWDwGUOppQ4pODw_ziob5e8J0DB0B8NRlN7dUrgdtdBoPnJm0grT5SDTUsGvmLSe9UfCu6rVfMyVRQ6vKeT0Ml79okyZEj4v91xbjozlPEjWbGatZUrPR42981SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇫🇷
درپایان‌بازی‌بایرن؛ خبرنگار از اولیسه میپرسه میگه حالت‌خوبه اولیسه میگه‌نمیدونم، خبرنگار میگه حست‌چیه دوگل خوشکل زدی؟ بازمیگه نمیدونم من همینجوری فقط شوت زدم توپه خودش رفت تو گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29503" target="_blank">📅 09:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29502">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgwo1kX9_WIj_NVT4O3rW6Pe81v3YbmDEUD4F5I4LuXXOp0aKtfum7iVJv2XpUccPxx3261TsCkKov2rzpqDMUID3OJ2AwM_v8J-fbsSZt1qIeqONNtLxe_b_UkCdLwIJNjNmoC4InX9qVeWcQ-MUyAASOJujVRZlJvbOTSqEBsLPtXj56bij7gWh_9OMx-wlfkk7xecHwnb-JlzsQOpDgo6YMA-ZdhM_m5NOlJHHibniKlm-tnwnEtDaGDmin9if5UWOJoJfMIDIJs6mHPrprGvdSX3pjXBXu2SOIptAvFyvQppzYQnImK6G1U1AzxtVM0RG0ZT-xnzhvxULprj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/29502" target="_blank">📅 02:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=DArD41qI5-mmlyfC2GiMg_z0rXJu5Ib8YvWbiCTrzMaSqE3i6YZfR0Vo-pjmv4vqWB_Z9ukzAMUZ6teBfdBJRxJYDShiJi84jNZyxaWt5HzT71ZYCCOOQOrBbj6xQTAVLMUu0Et91TMIlvr7fBvtoyQjAa4svm_cxhx9qxEAWJ4nac-gVYC8UcpJdPQuAl8S2rMAFIzaAZOAuWjv96RnzjTs_uc94_igezBmOuuuO7xAJRwJUNYwSmTZeZ4-mUCdbKpKpf4XZeR4gWEcItgENtZ8Zc-g2yISWRkzzbdxD6JhtjmdMomJHKLSTlnSWePjrn_NOd0UhNduIjzIiALg4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=DArD41qI5-mmlyfC2GiMg_z0rXJu5Ib8YvWbiCTrzMaSqE3i6YZfR0Vo-pjmv4vqWB_Z9ukzAMUZ6teBfdBJRxJYDShiJi84jNZyxaWt5HzT71ZYCCOOQOrBbj6xQTAVLMUu0Et91TMIlvr7fBvtoyQjAa4svm_cxhx9qxEAWJ4nac-gVYC8UcpJdPQuAl8S2rMAFIzaAZOAuWjv96RnzjTs_uc94_igezBmOuuuO7xAJRwJUNYwSmTZeZ4-mUCdbKpKpf4XZeR4gWEcItgENtZ8Zc-g2yISWRkzzbdxD6JhtjmdMomJHKLSTlnSWePjrn_NOd0UhNduIjzIiALg4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گل‌های‌دیدنی‌بازی جذاب و یکطرفه امشب بایرن مونیخ
🆚
بودو گلیمت؛ حتما ببینید از دست ندین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/persiana_Soccer/29500" target="_blank">📅 01:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIpRo1GGEbxOw0oKqgn4vpwSn833-sv_I-eRHe6RLLuro0i1umi62EhBQKabcqPdbP0brgAZRnjz7CTGy7Nzas7ONYX6rEOKWa4IbQ3L03i6W7rrC6KuHes9BgC_BTm3l92OL3xuzJMiExj52YIq27FUf3qPWcon0Ai_jscQdJclHaymvf9JfLUc7DsfV87bRDOQsTNWVJmjLCBjI8_ImLNt_ms3ouunPh0LH4reHRdYR3FO8uABtUZIPCZP_4NGuQaJW3Hzjsoq_keZ5PvONq05lxJwbu15dONOkR81gLSCnfzroFe1NiPvy0f6W8QJbn_mNAswbbLQnFMnvusXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/persiana_Soccer/29499" target="_blank">📅 01:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29498">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivKrwtlbILpLX1AS8lX_BTiVEni2yuScQiaJ0RXxg8CyZV62LiPCeKnnFWv3LnqHFy927PyFLEKbrpoQU7xmBGj7mC_Dc3q6-PGLO9jGHGK1IqX5P-npLqNVVfJnshueFffYAZRtsqnJpFGBqCn-gPjAVl8dVBX7xlFOkIPd-RqHdG4x5-RtO_aQPWPTB4B_v7WcBYSUxA-iGkYuXfSYnPKSxspiTHsqOoAFFSOhtEcXZef4KkagM1vZmOUL8aDUmv1crEI92CtaEUil7yWWqMSTgFgftrsgs37o75_2-lpBHNkAXEjZa2Ut20EB9N55Xm2Lpt_jmGShoWnOoWO2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/29498" target="_blank">📅 01:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29497">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFaCNyQKmRpZQRmIjPGZ7yl4myMCf3PBqaAEhvztsAbAi0oYt4dZ0WazxqGmvE3CYVtp0mU3tJp4TAyvXO5jJNZ_7nTKfnwDnnl5IWFuMff42baE20pqbv2wZTGNQL0K6zDpJENgRFI_kY8rnqHg-HyXU-eYOq7z948lFNNfhXM16mr7ZyRW4w1rtJHgwbRKOi2MW1r5UYzKf5iSjfdH8LtBkQW8UtORFSQ7AsY2xscIfwiYOydHTIl8vMgEmBsYblEZTVV9aN-8-dzDE-aCl9k4OpFFSOuS9SrZ7XFhPDcqB8LhBjlVwSZK9vGR-FLuQa0Wi9dmKpn820aLr-ZXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ مصاف یاران محمد قربانی با تیم ژوزه مورایس در هفته پنجم لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/29497" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29496">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgDveMCsnu9oaZ-hqpPumqVjEVXmBoHvSXgip6Ro9LmV7fV6bGOJSKmNbNsm1mr0flTSB_SKgFTFaFClK9SRbGzjWsy5zJ2xAloL69AdTClC9zzHleKyQBmTAFaC8AwGNLmEZbl7iBWqqUqxnI6m3isZlHK464l3RuXFKNozgCwT8vpr4uHqnPyNdjsPf6Gv4q3wBOf0qUnKUFbQuBn3v7dsBOGsuGLPGu7DbWl5kp25c0grPT-rBhhUMI-40uEn_LOXoe0qThE_gr8X4UszKOnrRWK601mjSUv3L3h2Vyoh_ldUs_IWL9Y2d5J48nCy6C9W2leSFt_xpbHiI8qCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد آبی‌ها با تک‌گل آسانی تابرد قاطعانه‌بایرن‌مونیخ و من‌یونایتد درگام نخست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29496" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29494">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29494" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29493">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29493" target="_blank">📅 00:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29492">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM73zCvRta__xd_Y-HGxaZI64X8q-idC2aCuo-H9kAWM5EqXFlRFifgOBL1xONTfif57vmng_C1lOYlZa06GBJn131z-vzh0CaAmPsPM5elGmVJ0WoVSd7zjmGnNOzhsGWsk5qdsx6NVZq4LGw7zEXB0DF6XY0A5Gt79_OOoKyWoNSCZthRG87zzrc5tyL29wXl7iwj5UZPlC0LAK9eWLC0PD_xmOoxpT-OOiySA-9STUfA6nXvE5ZX4P8MRjGTQVcqZzDJF84dGGp7pf778iZjLzbYixnoQCccxSCH-8L-1HvDlXiN3dHy2gjdjOCV-JOit8ct6GB2c_BDpK9ho7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29492" target="_blank">📅 00:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29490">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YrsGg0GD2xrr4xJGhdsSr4wqqm3xFz-rbJUSFzXQ8LCR8Neb59AItwwFMZ-HX6bZ5RGR-Hhz8WxP_prKF30KGWhtv3cAXJxW4B2WX1bgUZg9CD2NxnII9BmVUXhwdC7yETt2fP8Iom2hgrqdtke3p4Gdtn0tZrfLW07CrdI1r9b5XF6lqHy3scDd06ZVB7vP0e2vvlLODudroRZxcivG9O1V_tcf_Y8SmemUJvfGsd3M5SdBY-GHN4U5b9p2nI7AlzVb7k5HJ_Dt0VWIqvOP7dymDfLiUPWv_cclSNhfGDkYVSUkBnejEjc7ETSEEcKdt3hogzLeT22bi53dQ3US8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2fW9Ih_7AF1fy2L9R6dn1i17R-fbY7RMrtvVilrJktwyedrTLzMOPU81PX85pHZxsK9kvtR2_ZdcDAcbKV7kOQolfSTaPsI2PJ-b5g_Me-y_jd-0BhiqeHE_pEklitsFLgwT7mJKITAM4yLA358BawikTUOmdL_iM87mVeQWWrbipbRpMq1pAC88_upkYy-6_vcdymy71ZNsgnB5SkxbgSwB-28g48cb7adrpg12Sn3ASEBVjeBAzT1qj6lgqFrcGyC0Sl5RAD4rMndjdhQlOEiM2d-7u8uInhtbRPvzcrF5qHpttwtsorSiGcaefGvBhXpBdgVjvqvKPDKqTxlUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29490" target="_blank">📅 00:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29489">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/29489" target="_blank">📅 00:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29488">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PisG18Suggq7i-KPD21Uv79LkUI7P826nEeV-HX0b_Ymgqwj17_4Fbv0xbQuFKVirsEZlhFgCmHMKxHyRUqZ75sxwyQjiJ620X86y8MckyfDdZ5rhy-LRDULgBFRVauZu7KrARXlkunh0acSu6fzfdfpZ353JXKPsZg170EHsJOjWMP8J-9wngFx_SdWM0iL_fDceg1pScVeEl0wnvfMSJT_CgN-uosUaHfCjnkyju90kZaTCRmmA98DLpy51mauHYu8l0gMUp4OW3LN17I5snftanUNFs4Rs_f9WRrGXhryTF3KSMGBiDMm2LMkC9NCbRpUNY_86dDFmrKKjBJZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/29488" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29487">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLH4OQhePi2rb8Hm-3QkLdbXtZmwCgFX2UQbsgGaQRQ-xB6gFlM41qmaeom0CYMQbX7y_-7lrbte_whEKZTk1n1y1S3NnlV3vmJ8TvirlkFMEI_2YR0o9eUnOQd3AeHLdpYwagHta-iHDkxI5Ibe211JclhLMwmSuvz75TKYEdqFBTuguE84Jv8_EysFUo3rWR8-0YtRDMoPAV8hbXeTWR6N20u3T0DcnejGd21yLuQabAoif_sV1DsHLddNx-bJqy1GQr0Ix9X82gyFIQWsIsNGtGRdfuycrhWyg_git8dJNMoENwkSPZ31CsQ1567XNoEXS4eJOQkgOEc190cAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تقابل جذاب دو فوق ستاره سابق تیم ملی برزیل رو؛ فلیپ کوتینیو از نیمار جونیور برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29487" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29486">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8AcZdAkWLWZ2h-WCUcW1L2jydAJhn4OOfvjGcDV1H3Y4Mfkg1ele7Pa0I5zX4MvsSZRiASAGVMBkdwFsm2vCv5WRAvMox_K6w7oN8MlP_coJybBeA1pRIRz5Y3VserGDQdzZk7azyCObUhs1Hl6_J8LH4vsI2zR666ORmrDV2uwdWJaNb8WTVedR1gveHkvoMJu-5tGM1QlVHuBGYGzeomOMbPpcgCYjcqMCEJNsQ7gmK9OshtBpEfdvFffRgDcOGSNymiaigqCyctgdD89vN9i0aE6AHcUdHlHz-MIwjreei3mn61mjPglgTOXuKmMUlTxYxA3SPtAO3lF5L7lQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مکالمه و پیامک هم گران شد! از فردا ۲۰ شهریور تعرفه بخش قابل‌توجهی از خدمات ارتباطی افزایش پیدا میکند؛ آنهم تا ۴۵ درصد! برای مثال سقف تعرفه هر دقیقه‌تماس تلفن ثابت با موبایل از ۶۲.۵ تومان به ۹۰.۶ تومان رسیده است. عالیه. همینو کم داشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/29486" target="_blank">📅 23:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29485">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qV8mWsfdo-0u0UZpQkvClqsuxbg57VexicTMRqcULF5E_V6RNgZMBO0m0SrFf9O0qHdTISgLGxZQP83YTUCjHTWwBrtFdTgZqCsyS9S3fykbRVDusCDYUepUGCsvI1qeoGSKOMHjqrwNzm345G20WoDWqrSGb7yE1YDRkILDkkOfrFuwN2n7BWCP7LLWTFqgvAcS1eCkPwlPrcl1g5TO8pDfKN5WRsd3baRqwB95IeNgOB-XJ2ExkDbKxfHfAjKZimjHHTQSZj3-g0I7U9wKi-CnhF3JQYeVDASfEFnyvkux-pXxggCpeDBQfuj5CZPbT08qHfY_XduQ3oLTENS4WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/29485" target="_blank">📅 23:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29484">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBSa3PmbHP_DUTF4s_-1qomH_AZQOFbL0d6kATj7EMLSNHin9MxRGz3njIWtMxqw7-rUrZgKA-JAt_KPN6ho3UJmtMdx8hcCS9XWG-X7bkCHBuBa_Xc-A4KLUtmb2PIMv3vZ1fq-4_4zmJe9zGA84wY_pbqmTPK20oKtOrfdXG3nwvUG1IisaqOPmFpQHYM0oc95ciZT1atom83quPIfB-Lzlcnj82A6_kp2XL4ACqj0nu_-rAF_wgkcWp5j4s2xBircVVZU-6Fqmj0O-k2dNDYescqsr5-9Q7lblaXOZTrxREpASYFsKOT_xtjI1Hecnm5KaWWywgo2owse-eUF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/29484" target="_blank">📅 22:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29483">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRQJNrRdDemTp4mp96774UKTjU0XLLt6iY8y43ME_WOOKp6S4UadUKD9H56j08b9m8N02VWhmADLZijqka3U39ThAwkY9q61uYS6ziu3b4PH9CAz21J3dmJ6crHOHnMDBAM4MCXgp1V_cxH46C_jyhafSVeTz21rWpzplh1yerP-yXAwmcgpm3z8LWclSFjOwEZRtvdpfI4Tnw-y8eTiDH6dPZ3TC1l3pkJKrDKU8gv-dL-3bKq1Ni6G-U0h9TFMyh8jAIHHudqEduzd5VL-mDAxqSO8AuizBgoFSrgGgfUnzXDVTCRVaWavIo6Yj6DIw3Hf0NpvgdOkH6CWQZnTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ شنیده‌های‌ رسانه‌ پرشیانا؛ فرشید سمیعی مدیرعامل‌سابق آبی‌ها درتماس با علی تاجرنیا رئیس هیات‌مدیره‌تیم استقلال‌آمادگی خود رابرای بازگشت به استقلال و پذیرفتن سمت‌مدیرعاملی آبی‌ها اعلام‌ کرده و به تاجرنیا اعلام‌کرده درصورت‌بازگشت تموم مشکلات حقوقی آبی…</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/persiana_Soccer/29483" target="_blank">📅 22:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29482">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At9OEt7s-P0mImJFpuvFaJGwdJdrAUA2Nh1x2YuJg5v8apKTMQwC3SuKD0wmQ-XxUWQ6FjBmEPJztPkxrw_oQsg2_uNzrU4djjxHBqxgD8tNeZqnt2gA0_hbUQXz3yV_xDuXou_g1dqa73HRsAoVuBGiOA2ZPvtGhAt9aA4ElU_q1Rjw88qZ4xokJ5gd8IqNRFRD6YcjrC-JZ-h_rgeOP7qIKEGuZUx3NXgoxFmx9LDPXpnvYHlK_DIDmM-zfqxKHVW1Ucjkyuz9PPaH-K0x6a2Lr41itNXgPjnpAWzlk4OU_IyTsdNjnlmAlvOsF_FaP0JmMnbnenJY-ZtKt2b7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ابوالفضل رزاق پور از مدیریت باشگاه فولاد خواسته با انتقال‌اوبه‌باشگاه پرسپولیس در نقل و انتقالات نیم فصل موافقت کنند که گرشاسبی بابت رفتار حرفه‌ای رزاق پور در این پنجره به او قول داده در نیم فصل همکاری میکنه تا این انتقال انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/persiana_Soccer/29482" target="_blank">📅 22:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29481">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFMaoTJJ2XCbN_VWrBs25FRY9lPfVzEm-ATrQ8bFJs3OqIjOx4mNLXQR2PWUN9zYjlX2e8nun3CtvTERdoN36qLD58fuqrRpMfoNYj0_Q-rYqotoZJFj2JmPMFtaPyErDjDB5W6dXkKxzEom-BLEkf_RYY4FCRuy9Lvo20NcrtCeggevfhaWx8J9YKHvdDq7HoiqwF5u2t9QfD9r96NX9Iq1rVApsNcWRo2yae5PQ2REFwk2U884DD0PGEIaBD8LnTfGO8kklY_1z04-l82vp5gootij9BUJsxEdmdzmBS0nahkoSrqoGojNWFMUw6UmakC-zDsmqFdZQu9dpMAnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛ خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/29481" target="_blank">📅 21:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29480">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q08bj5VbovLU5G-OVJE8KLAFCWLGygzZtoZz7VGnybHfsnFzE5WVMgmemWDcsHFYJa_lqKa5EVzk24ZaCP9j13OEFk71s86yogNvSP2WLIhBMISeKso859z4Zhq6upoobAdGn3qWm_Sjkc2zYSSLimB4djgZc4RyDHx0ENr-fdFDBcfgu1y8ictuofz5ZzgDOcNCGG-kEMDAg1T8DmPfWWUscp71lYDWMkVX20rZj4XT9v11PhaOMt9PWKjuUnxlyrZI3Ft5BTubbUZzrq71uOREILckUznraeCGAdD3rHPIABUOyjNLwb1dD_SrW2ERR8TgiqS0YtuQnq_PUHol6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/29480" target="_blank">📅 21:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29479">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-Vv_2eg2jj0Ejpfc5ECv1TM_6keExibmQDe8NC80JWNG059-jXeADnGlfN3m_F1tGkWaTX_OvHOP3asE9MsS7KcDw-Lq9vDnqqYvx2NTrg1Z69dd8yzp_Sc0edmmU-fYpVrVwe6HHqP-MPkjuy0rHMAYd1b5gk0G9gsfSjR9hX6sVLy3mOcTKvzHE1GgdjmmIBqXYg_91NOOmYbSdwNNXwJeY4KkNhYrof9fvOjJVSIsenNXBGxBJpLpFE7a0j8lu8TCiA_U76otuX3lhd0raskXGa1t_8di4Ibw7chg-LXbp6ea9qcyaRXY2jnpLwg8e6AvaBGAghYVeBmORIBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ درحالیکه باشگاه پرسپولیس و کادر فنی اش به شدت به لغو بازی با خیبر معترضه و اصرار به برگزاری‌دیدار برابرخیبر در روزیکشنبه داره تیم خرم‌ آبادی تمرینات خود را پنج روز تعطیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29479" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29478">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-piF1Dvh9n6MFRsIkZOM8UU44udIPeN0Ns8XVcWXSiaTHb4dB8_q28T7t8gYgMkQO75zzJqMgz6AQNQRCQ_K6Zcd_L8SQdg5W3zBdTaPUS05LbtPzocuajQF_dBCC5Z3eYpH2iyezIOK7Jb-yos57BLzmCfcVEIbocOo2GzAVbLLcd4LBZD_6nbqrWFrXAIoY5axuioZaxY8_g4MNNG3TK5MxK2WQoDER-LBUGuyXOBFi4txf6svvh9SWg2zDWtap6ULQk7QRszrvvKk7icMXVhY7zHRfm6llgMhfV6KUXHRIxAohX1X8SypoFvWL5i7U4pzm7vhc4-haAskYgYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29478" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29477">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alCsuupyHk7DyfIfrlfMNHH2Uhs8ZnFci1-81_zxOF1q2-D02E2Zs0pvfi9UEwKWGZjHqPzjawKGMTu5yVREqb5rHiwcPROytKsE6f7X_v-8makyyYVHsUwGiUt9mt1ALUR1Z_x4MamB1HwpGVgk-qBOEPXOJhDBd36UTPVIk-86A9yWirRdYwV_a4K4x7pmCESCTql_mbQ-HOlkdcqn8tRy8Iud7NzN_44ZaV4QN1pud5AfLWxhlWTi4qrBTpGOWiBkqZk-VP1KPLkIdCwrvoVKXRrKGAX8eKUgTsQNJNoKNQUVjKEWQD2lL-JgQfwL81QCUR7yb0CWDjMz8DfbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇩🇪
بایرن مونیخ
🆚
بودو/گلیمت
🇳🇴
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29477" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29476">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKJc9KQS-SRfRa7PcATvlNy0x0jDm8QESgPvYjNYuo1wYYQbUzTsnEOfobL3DBuXtcu82WX3o_KgKR4Q4tDbDx7IsS6NliBRJUuI3xdvj9srOEPGYNAQ1mmfWpoAJPJRlbIXchS2ZN3r4V5J4yIO8WXT_JbNB79dLnqusOZjbp3z7ASUyV4YPtPB9wpv91a7GoCahd7lvqIZvmuJ4IGS1G5WkTRao02IEFr0iHqfGUbWXgYmRpKpuEKUQWQjEkz2SXVtX-eLOihae0YGy9uWOC5iV1ErYDjyafuJsZfy4EvshA7AzTIUTASlp01La6CnKxRmf8LUtRX4x6x_xV3MSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29476" target="_blank">📅 21:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29475">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya43awk1tJb12HXYy-01cngsM4WI33ZeVrLu5bSAfRnztw0uCqCKjctTdF63ZkApPSNHYBvs1DOmUFTOWJA-1XtHOZFPJbJWgKi4LUBev_MAV6Msn9Il3Bj-5hl8X-hnWPpvHt8iVGXCZ2sTFYWVmRyOApCXWZRBywbxB19-bi5t9ipJdTds_P2Se_2zAMTvNUtyJbEYok0cckFLLaVQcG1hbvgLZYRZ_sCMtxjOvK_B5S5c_Gpba4T2z2T7-RUsAJFaq9pglTlerNGcxqvkP7pq3jUhry5qV3t9XVSFDwSQYKIen0V5JvYqkN2WbzA8bHowy1VtOWPD5w1Yn8Bd7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس هیات‌مدیره استقلال: بعد از بازی امشب دوستانه اختلافات رو حل خواهیم کرد. صالح حردانی بازیکن استقلاله اما باید قوانین داخل تیم رو رعایت کنه. او به تمرینات بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29475" target="_blank">📅 21:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29474">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=Rsracwb3ectnY9cBoLysYe0LnTF-cRguq7_f2PVXO3IUtdyxMxWwT0kwv42SbauZnS04xtqtw9i0lCcEBEJOvs08VjyxKObY-jhtcSs64KbmijSCRfhprUekawoqP6Bu3nsLFyrjOA49SGDdfoadqtreP2GADn1SSK8vmALXbN-eGLnIq14zC93LNAPiMjEng7HdZpd2N8sX_7jDynljQiHUzYhn9TZeYPEb9oImLRgekH6aESfmZ1sdFq9DrcCaxffj2H7lPxVJxsK9zcGR8mbzoVJkbAH1BprMdFZR2usX_o-mRLI7v1lnh_6VkCT_-FZl4wA2vrkDsus5ADZn8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=Rsracwb3ectnY9cBoLysYe0LnTF-cRguq7_f2PVXO3IUtdyxMxWwT0kwv42SbauZnS04xtqtw9i0lCcEBEJOvs08VjyxKObY-jhtcSs64KbmijSCRfhprUekawoqP6Bu3nsLFyrjOA49SGDdfoadqtreP2GADn1SSK8vmALXbN-eGLnIq14zC93LNAPiMjEng7HdZpd2N8sX_7jDynljQiHUzYhn9TZeYPEb9oImLRgekH6aESfmZ1sdFq9DrcCaxffj2H7lPxVJxsK9zcGR8mbzoVJkbAH1BprMdFZR2usX_o-mRLI7v1lnh_6VkCT_-FZl4wA2vrkDsus5ADZn8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی در دومین‌بازی‌خود برای الوصل 70 دقیقه فیکس بود و درحالی که تیمش 5 بر 2 تیم خورفکان روشکست داد نه گلی زد نه پاس گلی داد و نمره متوسط 6.7 از فوتموب گرفت. هفته پیش هم دربازی برابر شباب الاهلی نمره 5.9 گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29474" target="_blank">📅 21:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29473">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kuc6kJLety1KXiXxNa7ea4ZQpI41feil3IVjLoHV5Jyb0Nlqfq_vdvpNQLYEAZS5fhT-73T4sCoNjvjDI7O_enZ1LbjHaMcb6OUHuE6pL5gN3eRnSbm0LBLQhxnk9yIdJ4AJQPBmKnay2VhJyPg7Cou_zdqGtG6xRk4Hb0Tz3gAXa67HVR1FpHM1qzTB6M_RQjw39bB-34ttI4hboVzGBbo4F6wKJc0zf0Tk9qjsa3SycBUbC2ETo3mWFtSyyVRyfL3UTs-LkDEZBbcpnBbI5H8Fljxys6BTnv31TOoRF-I5kcQBDkBVYAJNn18iZCCmvw0hUhp0_etfVsbS-P8d-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29473" target="_blank">📅 21:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29472">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMq0eNz5Hd2VEos10jY-VkWW_ABvt6NedCRF5Ni5Q3wZUu-GzYnZ5S-I9Zilry_oxuMYYivABWQutWZY7AbWFpzrPwKn8saXef5wmAw-VjVpiM5fh3d71Nllqe2BvsHYuE-Upaa8tXp8iTkCyieVOk5294VBoVGq4PjWwYSn1Mtjfi6WnGLywgBiKY3KLGOuqowt4-tveuXNR_70UsZheett9imqrLCjynfUsrcXcTgInz4gz5PN4p-HJ6lobkQ4Amj8QNqz8F5uQzOREF9k0myepUZu4KV-RFHoT8p7QVEumjotP2gwKZUMoC2g3hcFaa24dyhZrUifARIAt_4tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم لیگ برتر؛ پیروزی سخت و نفس گیر آبی‌ها در قلعه حسن با گلزنی ستاره آلبانیایی؛ آسانی سه‌امتیاز بازی‌خانگی‌روبرای سهراب به ارمغان آورد.
🔵
استقلال
1️⃣
-
0️⃣
پیکان تهران
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29472" target="_blank">📅 20:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29471">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtWuk3PloBVWtGH8orS-XgJESeqkkHP3kZ8A5DMbRGEPSPQrWQa9e9TTfc7hJXiAOgJiaWz3KDqyMr-FkED5d2xJul8mzA-TKl7RqQaYNH49Dsobf7M67zg3gRMKoi5avqSOLpRcG9Gw1A_8w6IR7baK9ey6N6HzAeC2kkNfASlrmxiyrQmn_GcjNjA89_6CvQc3iqZYVitBLwq4Pd9dHJ-GbgsBrUxHVg9ImYLGl_xSmDEUJ7hYaQjoeCRKMOvsWBOOArHSJI6KYCxmbVpirzjt0T3thRi_x3uf8fVTxEIhsMMoNhNuxV02LqR25dt75hxwg4dd0mkI4YQ0fqt__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سومین گل وینگر خارجی آبی‌ها؛ گل اول استقلال به پیکان توسط آسانی از روی نقطه پنالتی دقیقه 76
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29471" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29470">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=CEbCMNKYFLxxehC_Mje8aL3i5kkRiZmHU_rcyAjARsP0EVOoKnwrXITuGnfp0dSkv2KUL_IDSPV81_BfHrA-zW9fWTbEo8eWtESMne1On4F8klaEztpwjhQMBLoNKTF9l3p4fQPyYkOrAY9Tk1xJDaxNWUnsR1AjKUpSYgXKLie0-vEiGJTbnnXLiU4x0VH_E4zGl4LANgQfAfvWembhJNalSBYrCr_ZV12saqB9BKqsg3Zaz1xMzqin68rc1n0UQEDwm6YBtwYDFBHthai5ThekwgwNH4JoAvNtHp0rmpyFSsaG9LnJm42z9LOj7r2C57UUKTwUmOIwBCmp3JAGtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=CEbCMNKYFLxxehC_Mje8aL3i5kkRiZmHU_rcyAjARsP0EVOoKnwrXITuGnfp0dSkv2KUL_IDSPV81_BfHrA-zW9fWTbEo8eWtESMne1On4F8klaEztpwjhQMBLoNKTF9l3p4fQPyYkOrAY9Tk1xJDaxNWUnsR1AjKUpSYgXKLie0-vEiGJTbnnXLiU4x0VH_E4zGl4LANgQfAfvWembhJNalSBYrCr_ZV12saqB9BKqsg3Zaz1xMzqin68rc1n0UQEDwm6YBtwYDFBHthai5ThekwgwNH4JoAvNtHp0rmpyFSsaG9LnJm42z9LOj7r2C57UUKTwUmOIwBCmp3JAGtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29470" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29469">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=EP2N0e9AqkNqf0GDYGjBOGV7oL3T2DoUQFZFiYUaAF1BvOY0ovEkq-xohKhfS3DX8qxOAl89cuvUy_BKpsnZovA8w8faTXuxFoAzBy6PyIj8BV-sjMwodEh5eqssCSIuSuIqNGYWikRz1vbfH52JtdZwzcpulCbsqaxhQXcWPh4Pn9FTG8mDr_SpPF92NGYxeo-46VnqyiNy0tY2o5iJguK7_TDi1LfoSdUauumNtTqrGBLgUUEGdxxx7jlA-v1wXuooHxk4ah0TT3ZNuALqw172gdmDYWW1E7cRkrh2dPQp55Ff8mq7I2sMpZNBO8pnxzrzt_xLpDWsCDXAVOtzfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=EP2N0e9AqkNqf0GDYGjBOGV7oL3T2DoUQFZFiYUaAF1BvOY0ovEkq-xohKhfS3DX8qxOAl89cuvUy_BKpsnZovA8w8faTXuxFoAzBy6PyIj8BV-sjMwodEh5eqssCSIuSuIqNGYWikRz1vbfH52JtdZwzcpulCbsqaxhQXcWPh4Pn9FTG8mDr_SpPF92NGYxeo-46VnqyiNy0tY2o5iJguK7_TDi1LfoSdUauumNtTqrGBLgUUEGdxxx7jlA-v1wXuooHxk4ah0TT3ZNuALqw172gdmDYWW1E7cRkrh2dPQp55Ff8mq7I2sMpZNBO8pnxzrzt_xLpDWsCDXAVOtzfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماتیک ترکیب استقلال برای دیدار مقابل پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29469" target="_blank">📅 20:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29468">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=cQKz5xMye2Cio6euvzq6_qmOKKzuizVIXc8JE7QGTkcQwGJ-UEdE8SdFTiOOOv5VFamydgCrpdJICRSvwdAocD04EG2ta8iRqrk_JMcqRf7fbsSR0M47O6W_6gCuzmRgGtmpI6hvbrf5sWK754LUJb19tWC_Dxyf8YRybA-ys4J38y-YQ1TIfFh-UEka9psrbVDL-YBMpc-sY3jNIo59NelQrF0EVRMvS99JEX3kH6iugS5l7-zZQng7Q7P-l0lIHoPk9nGUtnPQTZ-K-ASVYvpltQxZX_6FE3fg38Uc_Gl9s3V2sKeUNB2VNGlxag7fxnMEvUwiHdKJ5p9VPMlx3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=cQKz5xMye2Cio6euvzq6_qmOKKzuizVIXc8JE7QGTkcQwGJ-UEdE8SdFTiOOOv5VFamydgCrpdJICRSvwdAocD04EG2ta8iRqrk_JMcqRf7fbsSR0M47O6W_6gCuzmRgGtmpI6hvbrf5sWK754LUJb19tWC_Dxyf8YRybA-ys4J38y-YQ1TIfFh-UEka9psrbVDL-YBMpc-sY3jNIo59NelQrF0EVRMvS99JEX3kH6iugS5l7-zZQng7Q7P-l0lIHoPk9nGUtnPQTZ-K-ASVYvpltQxZX_6FE3fg38Uc_Gl9s3V2sKeUNB2VNGlxag7fxnMEvUwiHdKJ5p9VPMlx3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛ شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29468" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29466">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LpWibsOZ0Dta3b9A5iU5Tn0_pVhKK2Znq69Yx4vuHvbWYRoc21LHGFGEfe1qp93sy4039Mofs8Y-MMkRs92y0kXJZXEO1cBA1XZ_BwvDq0bt3EMz3oTsZPOlwWiTsfYMwiqBeoJphtmevQ-GqiihF4jRkk3E7akvEZZCPGBn4lnV0i0IZyoUPixDl49f0g7lmW4_wVV3pix4ZRhkVkenCeI0TBwC5jyCca5cpfD0M-HDhUUkaYupuE2Ww3JFPS-h0k6JpqzXAslf0M851oeZnPY-eeg7ZXh1xbXtUAQcraW0CzvxGwmCueGS4xtf-FpRKUxvufq3g5dVG-SCvNi79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcfsndwPJCGczQuhiQuDdadagn7Exsaxos8w0lq1lZEq0Cq2aE9Xs6iFf9LsVET80U6CORZt8YJgeJwBDtV7opNkv2k8PIR3t8GV7XN9yy8buENM5uyg7TioxhbPjQkuW1Bgd3Ls-I2BV8wyrCZRu4h1Yqll9ZYiNnzOcoLRCbIrk1pfWwQPGm-2vUuBKnacn4nldIj8yY30QnMhC_tDm0BwL01qkzaHd9aXdgQHtlQwzJkt2QCol9xXPfIanfI4K4xrFZAYOB3Thwf1f3S1AdVr8sOrqXBBGGzVYQS_9gNdyf0MS9JJiLlZ3fglpPMxV2OSYr95G43jP3PWJ2rFkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29466" target="_blank">📅 20:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29465">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyztu8rxUqxYpXDq234wzqK52uENZwei4bp1CXiQhuDNEqxgvRAVWAlkysZ2SEXEAo7rEG0g3vAN2ojR7oB75uJKSEa3N9ZM1qsWG2rv2C6Gr4W7DpFMwZDQg0XNf4hSoWuNRkIctmN_wO-RPJeFXp0i2e-dqyq9TlvZiOo-RUmata1poh-ZbKDDrI_y7TiSkfZttmZlqU5YJrA4ryiXHsiYlYqdM-UR43EOdrGHHAJa8NeOoXjczvU2Gua2tXZ0IcwMirjz-7GEwp8ZAXL_bHUZaKzTCVFK1500w6tek67kKYGNSEJtz0vTuQpXbBQ1slf6LSC4LyPCBtYPG3jpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29465" target="_blank">📅 19:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29464">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbzRvPTEOL5Msr362rN3QI6TgHuhQiTyMA4CTwc_bFrnHKUVt3W6LuLzCGxdfrmwXXE4vhhcwHMubZfASJcwO3AS8AjzIHkKQxI1JgRkRyA0V1e1e016v6vAR6BOzc0rUNQHQc2qrulVA3MT5sr4O6Q86UrmSZ0H43oJC9zTCq8ZFw0ToqPQ0DBNj6kgy7r9np_oblLcmrpTHtX5CqrYSHww2Mex_KAuo2ev7f0aATb39FAxHN61U-q6FWJcT-uS7rJbYCM0RF8AxL1fW0mzbcM1EgP3k-Ul8AYdpftFe2wWHVUa1_la2wATT-EVzqzmaVq1_vRToOZ8lScNufwH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویو توییت جنجالی وینیسیوس جونیور در سال 2024 به 490 میلیون رسید؛ وینی بعد از اینکه اون سال توپ طلا رو به رودری دادند یه‌توییت‌زد و گفت برای به دست توپ طلا 10 برابر اون سال که با رئال مادرید قهرمان لیگ قهرمانان اروپا شد تلاش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29464" target="_blank">📅 19:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29463">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5EgaORmtu_yX0AnDb-ML3ci7Oj4kUMEarQtYcjuRR-gzsVPdJ1VaYdOt4VQoVZBAYJ70j1e2lDbvbmDHRFR9XriqR12VB6KbJVpvLboPJoX6lBtjVu2VyWD1qruZKSwo1ZO8rYhDMFzHcj0GcFtCjXdVR_VlLurzRth5-PripfRy2_1rglRIpdL3-_X5euxI-vV-R5HAjE9g_g1913T3um5RcMxW7w3RT-T5XX-xbMu1fONnK0bjwxU6_dY7cqhFGE9axIvHwznrVpHu13hH6KYk5Tm9_MxT7l0MQBSwgzGlvOtk4NzcqdJXQgw367J7avumUmw87-65_w-2PeiyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های تیم ملی فوتبال ساحلی ایران در جام‌ملت‌های‌آسیا؛ مسابقات از 28 آبان شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29463" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29462">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf5ffd776.mp4?token=I8vWODffnY5bnRc5VFPERt39P_oWzIW_7iDNNMehbzygo5Pw8sn_vOs8RdlDIhOsUX5gWxGCGikkdLQ2K5YplY6UVLFIslk56JdakHg5pTikh2ZTncHY8qSvI7f1VwFKqjRG4z-avwVsAk_lr8t5j2dH_P3mmmopFCYwa3wSP9NzIB1nTcaj_xpfkj7nUFD2NUoW8oh0LuHV1J55b2cppc6zGHiWREWqk-hsGKVejuY9TTMpj5-_yKfScl3GK3ZAB4zeFRRBfArgkPQnfo4yegLeBb3Tx6fk73pKwMYJQe1RTGA7EB-jN4OZ8hQ-piBU5Y86rfYaY69SBG8iFvHRJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf5ffd776.mp4?token=I8vWODffnY5bnRc5VFPERt39P_oWzIW_7iDNNMehbzygo5Pw8sn_vOs8RdlDIhOsUX5gWxGCGikkdLQ2K5YplY6UVLFIslk56JdakHg5pTikh2ZTncHY8qSvI7f1VwFKqjRG4z-avwVsAk_lr8t5j2dH_P3mmmopFCYwa3wSP9NzIB1nTcaj_xpfkj7nUFD2NUoW8oh0LuHV1J55b2cppc6zGHiWREWqk-hsGKVejuY9TTMpj5-_yKfScl3GK3ZAB4zeFRRBfArgkPQnfo4yegLeBb3Tx6fk73pKwMYJQe1RTGA7EB-jN4OZ8hQ-piBU5Y86rfYaY69SBG8iFvHRJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
پاس تونی کروسی هافبک مس به امیر روستایی که این بازیکن قدر این پاس برگ ریزون رو ندونست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29462" target="_blank">📅 19:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29461">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb94cff9a.mp4?token=n6b_gM-Q67t3aF8ZVRzy7CgS_wBCOK8Cl0ou_aXJ6DlEFkQWcQyor8xNE-bP7IyBHII3iR5rvWBe8K1P8WKL1GDL8gDfDErLlEbC1Gu3sbZmwfI25vqj2ngT13QIVcndzYdByKYR44oXVibRlAmnXSacmIq2v18GQ_r13mXRDT_kbRMcOwrWai6OYHS7zSTudXb6ixcMVL3ovm74RwHkrtSOHwM70G8ZEQMBZZXcNnnkFWvqQ0-vpVZ0BylBHGXb1mBRlRhA4RarjnWtU6u6zpeaKS-bOtzVHpVcNfmVrlT_3UN8GbE1OzUiTbxzm2qa3e51h9aLhE5T28SbddekPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb94cff9a.mp4?token=n6b_gM-Q67t3aF8ZVRzy7CgS_wBCOK8Cl0ou_aXJ6DlEFkQWcQyor8xNE-bP7IyBHII3iR5rvWBe8K1P8WKL1GDL8gDfDErLlEbC1Gu3sbZmwfI25vqj2ngT13QIVcndzYdByKYR44oXVibRlAmnXSacmIq2v18GQ_r13mXRDT_kbRMcOwrWai6OYHS7zSTudXb6ixcMVL3ovm74RwHkrtSOHwM70G8ZEQMBZZXcNnnkFWvqQ0-vpVZ0BylBHGXb1mBRlRhA4RarjnWtU6u6zpeaKS-bOtzVHpVcNfmVrlT_3UN8GbE1OzUiTbxzm2qa3e51h9aLhE5T28SbddekPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصر پاییزی چهارشنبه از مدرسه برمی‌گردی و تلویزیون رو باز می‌کنی و این شاهکار رو می‌شنوی. یادش بخیر واقعا اون روزها همه چی بهتر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29461" target="_blank">📅 19:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29460">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=UwpvHIbl3aOyz3LEi3dVcNjf8hoEq9jSHRPgiykNQ5mhUcFgWOSMMtzcSFHvR4XXwn_CwJE2E0EprRe__ijXisTChV0ColppT3AgXhdikXIaQhuNci1uOinqQuONYc0OYLksltx8xOcGf1XEWD5OOfy62qntzjRVLaUAu8RvEdqEO8NbuU0RYiy73oaaDNGFL_xbNtRiO607H8gZ0sLel2qVjunqJDWbME9rSwiADlzVmIepAA1Za6H4bcOr4VdeP_r1fEszHdG71BOuLAFrZoQs3DJcaA7-ogTOhCV6RZtEh2wcCQ2G9WXKUT1O5BFpg82iWpx-OOCcyCm-voUsJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=UwpvHIbl3aOyz3LEi3dVcNjf8hoEq9jSHRPgiykNQ5mhUcFgWOSMMtzcSFHvR4XXwn_CwJE2E0EprRe__ijXisTChV0ColppT3AgXhdikXIaQhuNci1uOinqQuONYc0OYLksltx8xOcGf1XEWD5OOfy62qntzjRVLaUAu8RvEdqEO8NbuU0RYiy73oaaDNGFL_xbNtRiO607H8gZ0sLel2qVjunqJDWbME9rSwiADlzVmIepAA1Za6H4bcOr4VdeP_r1fEszHdG71BOuLAFrZoQs3DJcaA7-ogTOhCV6RZtEh2wcCQ2G9WXKUT1O5BFpg82iWpx-OOCcyCm-voUsJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29460" target="_blank">📅 18:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29459">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=RgT2n4RgM9XwCcT-Gj_DQV_GHsm332w5BKLeOFqJw_HA99t_ZnOUklZgWDhO7AFCxQL6t8XeX1PUY4fsvT-FWOyYi50Pm8bnptbyVRGZOUyZ8SIAkl7ExaJfxRpLeHR-oZ4bEkb8D6wUTj6dLHPwgu1iMnHh-Ed96iRmVliBfneDDoVXhwzXJBgOOya-LlzyQBGhGA9_gxRzqHn--lgSYQehJW4ORuShBttycUXJFnaZBjy-ugkl5AP2CKnSzjJxS2KV-fhq8wApdVQptEaB2lWVdbIaq4eBj7Q9TtK4WtLLl5o-OTkJ3iiyDSYggCMFvSI66X9tsiCRFDuKVSUavQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=RgT2n4RgM9XwCcT-Gj_DQV_GHsm332w5BKLeOFqJw_HA99t_ZnOUklZgWDhO7AFCxQL6t8XeX1PUY4fsvT-FWOyYi50Pm8bnptbyVRGZOUyZ8SIAkl7ExaJfxRpLeHR-oZ4bEkb8D6wUTj6dLHPwgu1iMnHh-Ed96iRmVliBfneDDoVXhwzXJBgOOya-LlzyQBGhGA9_gxRzqHn--lgSYQehJW4ORuShBttycUXJFnaZBjy-ugkl5AP2CKnSzjJxS2KV-fhq8wApdVQptEaB2lWVdbIaq4eBj7Q9TtK4WtLLl5o-OTkJ3iiyDSYggCMFvSI66X9tsiCRFDuKVSUavQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29459" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29458">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071cf92014.mp4?token=a4Ont0u32AFyQ62bHYFgY5HZFkfG-H4xWp15kyL4W4F9nrVqOEsuqW73HVMK_QleWMt312Y2QCYg7I1KEFUkNanZ-2Zmvo-wJWAUSJvUmkzgOcfUZ77E3SSRlt72wmoMsvcYLOqcC7jhm5FwUPDEdU2p9zHh2zcxIxYsU8imFxnAk0YIFiG95DPFZ0lR87OS_e67TADSzhnA7olVQ216fxpeNH65ifQIhmUBLwcUM0maslt1dbxzYkEoObc64cHLVvGQ0h3Vg5hoTMSGGG82VGYu_u75felrqvYM6DC1eHKlS-zX7e0-Ie8ow1myxonSQRN-OeTjnntVfS3FFnQyij543EGPNDhSE6vc0dYsNSUKlgfjnCYFCKWbOaG7Br48ndzXJ9B3CkxVgcWCIdJGP6OwUO96zObNmDG9_1dMMQzKIWlj9_4bYIHz8seCH-ZLxS-AqGGhth3gtXM4tZ1vAdHiotKnkILUX53739WSF808JWST53ncYRYL5tMEA3jIh78nZ11L7iH2jCM-mrpcDS5BfxqYvRZBHwGFggMVVqVwyGfLVI0XtbxxaMMUs6km_qFPu22xjh7kzlntg96ytqyPu9wi-za2nok0qEHlldLTrn7oRU2oMCUIAfAisbedjx65Y737ukq9IBICBLzyxxBcMu5CZlIbg0mtt4lVeRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071cf92014.mp4?token=a4Ont0u32AFyQ62bHYFgY5HZFkfG-H4xWp15kyL4W4F9nrVqOEsuqW73HVMK_QleWMt312Y2QCYg7I1KEFUkNanZ-2Zmvo-wJWAUSJvUmkzgOcfUZ77E3SSRlt72wmoMsvcYLOqcC7jhm5FwUPDEdU2p9zHh2zcxIxYsU8imFxnAk0YIFiG95DPFZ0lR87OS_e67TADSzhnA7olVQ216fxpeNH65ifQIhmUBLwcUM0maslt1dbxzYkEoObc64cHLVvGQ0h3Vg5hoTMSGGG82VGYu_u75felrqvYM6DC1eHKlS-zX7e0-Ie8ow1myxonSQRN-OeTjnntVfS3FFnQyij543EGPNDhSE6vc0dYsNSUKlgfjnCYFCKWbOaG7Br48ndzXJ9B3CkxVgcWCIdJGP6OwUO96zObNmDG9_1dMMQzKIWlj9_4bYIHz8seCH-ZLxS-AqGGhth3gtXM4tZ1vAdHiotKnkILUX53739WSF808JWST53ncYRYL5tMEA3jIh78nZ11L7iH2jCM-mrpcDS5BfxqYvRZBHwGFggMVVqVwyGfLVI0XtbxxaMMUs6km_qFPu22xjh7kzlntg96ytqyPu9wi-za2nok0qEHlldLTrn7oRU2oMCUIAfAisbedjx65Y737ukq9IBICBLzyxxBcMu5CZlIbg0mtt4lVeRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
👤
ویدیویی‌از آنالیز عملکرد فوق العاده علی علیپور در فصل جدید رقابت‌ها زیر نظر مهدی تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29458" target="_blank">📅 18:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29457">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipA6hbJagnm7LtahCgwEWq7aZRYNEJqnDbJAbjj7kkXgiErpufQvdsq7DuE2rkDJ5eAXIThzSjXKSY3zaB_Fn9AhzEq9M6Q5SUzx0c-_PFpOdqHjev7dSIzjwuDQvmSqem4P1mFKGJ8xpmDrv5ih8KE_YaIYEZGA66flHHOw7FbxlsBlLb8tKb4G96ue3-JHnxZys0c8tJDbpONk--p2zLEDJ58S9aZCpOFPDeDXYlA51VthnRFxGuasLbxQtC_vGlnjQndEa8z_6AsUqovZK7GemxMfMvx_GXY0wik9AITNDfI8r79ZD2jhR007rWfpX-Hp8jjwhRBHbtSaX0Wg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29457" target="_blank">📅 18:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29456">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxI2jPJ_jiqJPNOjmGobLM_pRJ04NpesRAf9sJpmb2UochXQ5p1zUW8-Vm-QAkegGGObu08ysZ9Lca0lMTTHCBToxeJvCWmYXKS2DZ_HWj9Plr1RKa1_ptdboe4imO-pSuZT-5bdv_LalsgAZMlMTNHmc1ulkNqJh1xDUY6UGGBWTYySJRLIy6BPLo143ZIgeUzWfnaa0LXcQLk1Op3JD0qGxKtKEjGOVw0BtS4dm9RPlr3km-Dx3BE2xqZBNkXlQnNZn8VRwoXH5J7wmEyfZ98zxRW6XxfKZmwuIJQqVd7XAQE5xs8sm6qIlfgSreERg8FgTaWZOyzq9In6ocH1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29456" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29455">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6yyqP60ZHEhcksY0niVTyoOKGra8sDTN-4GOZVTEP7UrKBcEE3YXjICo_EILZGkMmROVx94L9y4lxcP6hu3QA6bR0vcnXk7YEzZuCD5KOfHDs3FULsQdqLscRjbEXBCznYUUXSROLkcCbYR4OeNua-jlFOlIg_5q_LHLfj2M2fNKGA7Z2Sk3JdzvEPBa7xOUL7w-dOIip6Ajs6GmOt_uBSvvHv_CXtQVb5-PvqwmSn1TXXqkhFxlb62qyvNkKuOcLDlWf0a2yejT8i4KDA3GH77RJj1DBf8url0y7crsvdj9Sf7X0itg8NiFPagS7ycqMshEEjCLeIZCaSlvta70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29455" target="_blank">📅 18:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29454">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1PkdIzOKukMUfZrlimvXYIDsP1hOgLsYrvD8ShKReeM5M68zulUDsjNyIuyQzv5Ol3BavyM-XS8R2dbTCYINmGNhEYY1neKH22yVpJ9WFxqbxymKUckkJGh_4OfkVD4wQQjULWeSnI7KUpyNUBL1kehruvjS1XMHXoSp3k8T6oamFEvV0FTgyw0HZpD-X1WCIpA4TnfJiTvcKrbB7Adztu8KJADT6eiLmRrTpeLTjNwo5BZLyyQHR7bKT3gRSu3ST3-MZp3z57gVKdrWzjHPFO3TeP4vjdVfjxfkeIR6MpoI6SfWWypmw933lWB4anHpg6F-hPwun99lG3qEnuwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/29454" target="_blank">📅 17:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29453">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPCbyNLalWpERf_dtC7rzDxe4bUcFV_v3FBKM_1pkregPN7T8J71kHUrFr93Qi7AbVqfyOQhMlQ6iylRPlpKGQadKIeXQpmjKT439MId_HX_HcohOSPCQ_eVF_a6PQr6xR2RKpq-dxE0mcAn-oM4hC8r4MNf2a6hwsomlkc_nI9jR5lAjWt1ZOZA6GVXDK4HUvbdqb6JssgdPsIgiHFvNIaw9oGoHqKdejOeY0onnBQEst-Yk-pSp5QPtHwGhPZQW7r8yZBRWE25Efc9DZybhJFp6mq_6R6-Z9iaYIoofnISTYCHfV4ObEh_nYeHNzfKbf5CD1qhjHUhYBU9UyXNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29453" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29452">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MowC5Qj4DHL_R9kYVoflxfCzXNT-dlrzskJncVR5yRB-CXLWI-coUQA4rBfbywCn9mfDiwJVemWUQ733RGyRbZPWjJmqwOH_EPD42Sv5n6eOcujahJd8XKk5YuIVsQk7QJSvXx3DP2Vd3BT9YlARDPZirb4J0_mtGLROwt_NbE3XqzhW6DrUJpXTZtcdAlZ_zjjbcVIUEUtn07w7he7nQ01vYNxk7DoW9ycAykDwMqCl5PGumFiLsdZACE6XW9gEXWeREKaB-bCwDqxtvooHMapmCiMrnmjLxULuvA-mxR1QIkFYBhBHRe0P8YTVpmDhpLwPhSb67wzdBparQe749Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29452" target="_blank">📅 17:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnjEBGyRV6qfzUhOxxufx8nRzZYIAm7YeHWPKvm2X4D5f9eftMGfJtxNYS95HOpGp1wf3jeCoPEPNsEzh1OFrDrFTQa-wCre8--g4-hPXQ35OmXQEkAzbfhaoN0tyoXAQliGlJo6Hi4zeVCrgq_wl8A2e5xaw-bvBKi0LRBeRwkVxzvz555C9ZmO_XFE9d6tdJy3beJPVWJdX4f1OBUyzGMeYLDL6F7qmmAnrEkEVz-KII9q5RPL_lu9wVHyLegc7h6MrEaB1m0QcdOw8mB8pfhOiAV_glXeICEEP2PycQ7Qj_e3LbTbDAK4NRNkhNH2oJ1ZTjUSJqoqd9r9fdDQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29451" target="_blank">📅 17:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=CBF46yTxHa3F-d5hVsrD4P9MzdMv6zPwv5JR6y6LIlvoUdooVj1igTfKjfPLKk_YxbtiKtDjnlB5E2VMMoUtGgEXos_zAqfMxbvWw4CN2olb84n7je-Bi7P-sJSWJiJAdZAHk7OgYVDjpu5rB-QaQpKkyYxBtXP5tk6ozPdKg2Rxar4XopuY7f07j9ScUetFVNhWtLJscF5qC3EAHwljG7y5-1n4KHlWkspEVojJnSIcz5oXcJ_w9Sgs96QoXDlIfwC6Oj_lzej8BAv2Wph1v1EvFBcYhHleXYqWoM0OVZawggcQUP7k17-EmXKWts-odu-CrJ05_LhnEA5ntm0-pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=CBF46yTxHa3F-d5hVsrD4P9MzdMv6zPwv5JR6y6LIlvoUdooVj1igTfKjfPLKk_YxbtiKtDjnlB5E2VMMoUtGgEXos_zAqfMxbvWw4CN2olb84n7je-Bi7P-sJSWJiJAdZAHk7OgYVDjpu5rB-QaQpKkyYxBtXP5tk6ozPdKg2Rxar4XopuY7f07j9ScUetFVNhWtLJscF5qC3EAHwljG7y5-1n4KHlWkspEVojJnSIcz5oXcJ_w9Sgs96QoXDlIfwC6Oj_lzej8BAv2Wph1v1EvFBcYhHleXYqWoM0OVZawggcQUP7k17-EmXKWts-odu-CrJ05_LhnEA5ntm0-pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صفحه‌رسمی اینستاگرام AFC با انتشار این ویدیو و موزیک تولد 32 سالگی مهدی ترابی هافبک مصدوم‌تیم‌تراکتور روتبریک گفت؛ ببینید چه اهنگی براش انتخاب کردند. بیشر بخاطر آهنگه گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29450" target="_blank">📅 17:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lREIqVwb2glN94M1VpfGY1TYZja_tOm4Gkn0MugAMIC2QbHVClUpoLMLNzPMh3_j0ZWB6wuv11aXL_2PxcuJ1PY5RIRhDwXXduJcXFNpqLGSyp2i5b519C68bMYJrOc6k8KvBy92Z8FIq_DXJMU5JU_ep3wcDm1IaZCkJcAJ6NZLmFFH1dkbdG1xtowYeJZZJE9jaf6zgl3TgFBYuIvI2m7IYJYfHlwodso4TbQXXL5GC5d4C3bwvc_4Hara4TYSmCjNbDyxAjTEmWr3Ey88jrvKXow4-cvWMHONpYvS9y_a1rJBLSzGqegjFa4CL1NVHUVB16sMJf25aGGQNXeVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
قیمت جهانی سری جدید آیفون 18 اعلام شد؛ آیفون 18 تاشو قیمتش حدود 600 میلیون تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/29449" target="_blank">📅 16:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFvNKZbsgOU6VYYoKObMH48nupUdPl1D16LeaRYopBbn4G1AgFfNJdWhEyJAOpYiDZnuxksrve99rcgAMepOu42vjeEcMg8NXhhoOmo4WXr2wyLOc_DWTrxEAwZx0RsHv35qZPf-WIcyvh-ihdrqiykuwULdMbHHLKwkCfcmAk6NKwnMVuloh36sYdYSUvy7her6JEI47y_GcO6keqxzZIY69JxxIHvWXzF1FjGxvVww57u6WfkKYhj5ffufjs0xUarU_Tvhil5nMU5GK_gvar3J-TqlHry6K6yrrkTi6bmrVKoX-4SwzWyGISksVDyBJ6utFEJBkkRXZxx8fhMU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارت‌پروژه‌جدید؛آرام همسرسابق‌سپهر حیدری کاپیتان سابق‌پرسپولیس رامین رضاییان رو فالو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29448" target="_blank">📅 16:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ql-BHSoeqaWrbTl9qwxoqBSc8cKAsC0FKltTlS0K90cbLFH0KI_-6ycxOigXEGvqqPgh5r14UjZunp02WdEVzeNU0OxTXWaBfSUAtaoCAnAyujhtkTPl-Emf-OF12q8mcj0pnrWvMZ-Ags-lPl4UNxoKpr3aqaQlpv-Sd7eh4CBk9Vrirl4E20wS7SCxhkLDsfdUcvWuSvAs8n4bGMNWlo7Wf2Gi5bWZqAlVNRP2o4lNJpYGl3MdLHP2JF2J_JOy2rx2xXtDNpQq6nwpItw_Db0JS1TMVhBBY9Kbf4EfSwm0B0R624cfOLdzGOpgp5NyljMcikDINxqZORc_95egzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛ مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29447" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29446">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX_bd5epRKwDvlOtEgjA8lVWlZQPx8X-vTzovwIoWpY6-34YKX5UnnPbx0_id1RRSZqL64BlHyobU7_t_YmznnJ4xuvhZJOD8jOnTwz2ylpxSMtbvf0rA1b56AJ3dRoMlhuLyYbHE2gc2CTSbA0aenMysFUaq_yXhBvlKzIVre_Z-uM0_YJTalQntWPdxKONHW9H6Pf_1EpiBVe6G1b0DUHZeySQw2sbHPW5wbXpJBUPU9or3ydyo4LQf4vmKA27HhJhD8xiywKgRZHbd6Swfz6hA-WhJpwABRcDcvs5uPwxKZW4KxHNt908C4XWEWO4AZl-nmOoDcTqa0ilTu1Qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
خبرنگارباشگاه‌اینترمیامی هستن که اعتراف کرده بخاطر اخلاق تند رودریگو دی‌پائول جرات نداره در پایان مسابقات این تیم‌ باهاش مصاحبه کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29446" target="_blank">📅 16:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29445">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB1DVa1tL00hItVzvZ2uqBAdZ5JYfES-oKqqQIBqd4BKmCDEYtQsI9b4klhh5Uyfe86Xsp0Qv0RvHP_u0OCPuZdt7Ic42okxdiotQOlbYo3DAu_ZjhCU2F39p_DEHBt65U4fkO4BAOH265sqOvDrsk9izft9iKj8hmPXc8KjwjmSE7rJyXUWY7DNAWC_9xuLfsZhkETJSI1T6OPNn4i4qwBHO5uBxsX30Gqa0NCRe-0XoWJWz01ERm_HqidoNW_eBy01xctLAjQA8qKl_FHNUV-UZbO5bGnlNT0Zsb3iVi1LHOR8wJYMlGAvNdX_l7oR1XOCo-CyxDlZ13vzU2W-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29445" target="_blank">📅 16:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIjHoOk2pw5H9AM8cSVYZ_92E3a0Djl3g-Dro6uc37UmjsAjObiNoYx1Q9DqCMsWMBD6Bj-REXMiYFJN0e3a3qJAa1WrNvIUuL-gf7wET1S9bG7RR3zS6weZFjLpehJ0n44sI2114UW8LzNTT4RyvAEfTsEO9Dr8x5lD68gBNeVPWoB9DPADQB0UnmVhJMnEpHt9H0WA_LMDWF2RqpgSwFfrsVj-b-S3oQb5xkj8qsT7ldXW5-bkF2Jlwv-d7qPhUr5bj-MVYN7NvRekZQhBwlIYxIH2zvcjulE_uMusd6fCiaJ3d_v2tzjIxCh5CK7_n8XsDb1O_kYjaZ8CXpkblA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ وکیل‌پایه‌یک‌دادگستری امید عالیشاه؛ با شکایت بازیکن کهنه کار تیم گل گهر از خداداد عزیزی ممکنه سرپرست باشگاه تراکتور 6 ماه‌به‌زندان برود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29444" target="_blank">📅 15:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29443">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afef3ee6a5.mp4?token=W7WD-k76akTx2gFfnUCSSXCDR9nDl3AuEcb1HZAuhhPksDAc95rff45DS8WbKTeuzCGP91KGSUDmMxr42t3fFlXnj5HWEtumt4n253hk-4OwF2ZfgcQpN2T31_TiRZfiRo5vh1wQRXA-8WhCdrCPfzAFkx_xQKGbaMmplWUQH-kEPcn2rMopDun-7EL3CntlHD7fJl7mVpX3jy5jnvecVVVfQdk9GqaYfl0YHL2jMdsQ7juqfNV-TuKAbooj5ev1tYpQjYBgy3B6l1utx3u5U_WGIHJaIB1DNhL-i4eQGyGuVLnoOi_-1mpnDaNRjC--vNid20XFN-3M-tU4BE4aYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afef3ee6a5.mp4?token=W7WD-k76akTx2gFfnUCSSXCDR9nDl3AuEcb1HZAuhhPksDAc95rff45DS8WbKTeuzCGP91KGSUDmMxr42t3fFlXnj5HWEtumt4n253hk-4OwF2ZfgcQpN2T31_TiRZfiRo5vh1wQRXA-8WhCdrCPfzAFkx_xQKGbaMmplWUQH-kEPcn2rMopDun-7EL3CntlHD7fJl7mVpX3jy5jnvecVVVfQdk9GqaYfl0YHL2jMdsQ7juqfNV-TuKAbooj5ev1tYpQjYBgy3B6l1utx3u5U_WGIHJaIB1DNhL-i4eQGyGuVLnoOi_-1mpnDaNRjC--vNid20XFN-3M-tU4BE4aYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلایه مهدی مهدوی‌ کیا اسطوره فوتبال ایران و باشگاه پرسپولیس از عادل؛ سرنوشت مسی اردبیلی که در ۹ سالگی وارد برنامه نود شد به کجا رسید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29443" target="_blank">📅 15:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oW51TUV2cTExu8_XRFK6yICp2ia0SU4325sBPI-hbj2_XnevGTJ40i4QzNZLG2OXC1ata1wpbbe_r7F6vks0V5hrbrdhmloydoVEDcevYJRM4_NMrbxb5f8Hgv7ATUOGajqLQbJOJ8GOKAZzwQCPbJJnUeHGqOoa3rv2q5n7tO3FWy_ZrQkhPDzDU-XTTsZyUfZ1Ga3hO9uLlLd3Sp7pVHvmJ12M6kWSmE4QvXd-k3NwmU_21vxMNOwFtsMriYynItz9iLvi9DqrTdjgAeraLshlrDpeqlZvwbANy-0rAGSstMIv_LmsYtBzd04Vt6VKZvkfIZtFEeT0DkmIb8f2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29442" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29441">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWljmdcqVLLV0ZL_A9KGomgxHw93XlXqQWM0wjweIFtS42JxnMAAHKwkAOAOEmHribyeKAq9Ciblbe3bASEDh1uew8BrTkEZVY8FqZP1OlvrzPspQVH1RtMNv0BnQpzB9AI9ughJlbVBaOJwQcjmyfRFHzywbTp1_H7NTS3pIpBTfnFwNGoA0IWn10SEiuV56LVOKAu-iweHmv-pwshBkQWxUha_ziyBVSpTsRHaGGgRwqc5tSzyP_t5hDFQPY1-MvL0lUYesX0KDMmdMQsV5ULIbiiiBGs3bQ4QyEWcvt6MiTy1cmo4Dwc-gPUAWo0JA8KGCYuHEPerM666VStyOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29441" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29439">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0R3vBpdMlRVlQukkLqcz3ZHkuBxeGp5wWdvAD1hOxSoFaUV1jAGHvndhsQEOORvpJAAMd_FclGEvPQbnpOxabhyRdBAat5Ttlb0ikiKfiK-htiKnEpUCASUBB7wtwUSdJk--p3gBgy_axM8jA7jbHaAi16x2YZYkkm0M8g7WJxW8myd9HDTtllVSz_C0XHJMosV8G6RbM8P6bb3UvAgbV-8zhHo1CFbGekBVa8jQk922juZWb-bxs02TMxvYoe5XO1-CWlJO3Gw0GCNIlYoEPlrHJxqX5j0AtKPG966MHiKxOdnF-4nWxVmZ69e1x6pQcat92VVkmp2efuEItaRbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29439" target="_blank">📅 15:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29438">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9WXm_dfnWtSM0ZHKxgTp6V0A3zjVs-fP22D2qGEXn36U0FmuqikHaZyA4mQOzZtarQliPxO9284EJSqmNQPyeGee0Xt4tHPPlr3jKPKddwsga-MK5fjdc6sKLkxpE-5qAFmadY3piT9_4fmLzKUbRGMsS5EQAhGu4pnEd--9D3kgrvkj57eMwgNx1CRIX0xLv8IhXyvUUwf6ctWyzbE4Fue-GikHTbsYMvIUj-O9_WiwgbQv-LZ_h-ZZe_B283eHM0N9prHcguY6RzKKRBiKe8TaA--R4xocLLMkNMtmEBHmDIaF8a4gp7rGtBUfWQnZ3D1hZhkEJJkJGfBFRdVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس:واقعا موندم چرا بازی برابر خیبر لغو شد. ما چند بار اعلام کردیم هیچ مشکلی برای این مسابقه نداریم اما سازمان لیگ به دلایل نامشخص تصمیم به لغو بازی ما گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29438" target="_blank">📅 14:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29437">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0b_D0J39prj9aj1-PyHI0dbE4WuIyhztKECaM6oSWGANIw60Nv4Scvqa30VnldP6Qn1zGuwcxTUsBVL3u8kGRbwGZchiokOz4x2C6raJy-2PDdZTZI98-J9Q7qqtK3-UM4r0il4nZdwY6ANxmtn7JwkeeUSilS7WYb4un_-Nu7Xx-VT93qZoxVqXJCOe6R-r9_VV31X-8Xh9FJOhcro1dyMW1CI2AfqC0Jo6w9TeC72YKXWbbYJDxq6zEC-AiDCBcQcL8Uf3i0K4tfM-VjPqeiyjOBKgHZOWeZlFRgbLUyy60kq-zDFcme9_SrkwliBbMqH4hCyDsfWbM0X4u2uZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29437" target="_blank">📅 14:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29436">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIHRyaxwSZZD0yWifcKDdqlEsZAMVwxzALHEvG6GauqucrN88wf4-UcRgMmJ9lvJrP2Tdn9EagihjSvKCprgosx1koxPz-tzMA36h8mlZYkP8CXo-gZtQ9-eDM9k4q1Zg-1N1HW3peQSvSOXOvxRZ06AvY0vzCPktQ4p2eTWYqGiRnDDbGpGdpJguPMBz3KO_aTj74tUGOIjMtZbalu5rSmgYQo1WDXKWWu9CDNXUKGJOzHvEHSeNndYthE2h3KkZ--9e5xtsKPrGVbrGO_N-957vmSoPRqiLqm9LQovMlQsjjKv62IMdvI9X8LMCklcf7un73GOdYeBrgUjNXUKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛علیرضامحمددستیار مهدی تارتار در پرسپولیس درروزهای‌گذشته‌با فرهان جعفری و محمد قربانی تماس‌های مفصلی داشته و از آن‌ها خواسته به تمام‌پیشنهادات خود پاسخ‌منفی بدهند تا بانک شهر در نیم فصل مقدمات جذب‌این دوبازیکن رو فراهم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29436" target="_blank">📅 14:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29435">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTPIY_7YTOEoMvuQrHGEk14Iaj03uztjHPepUvXuiyecITjGx39tx0QSj1U_WQ2v_hYun0xogI5s30qDuUj32ODRUvTJl7WYGlw-pd0_1P3THzfwRfcJyn85w67yMbCQCufOiydLWXPiaLOuXP5ZR0Vjcm4X98xgYV4TUiZSRCKbzg3ogQxb8784JV3DgSgYTB-44TjAO-R1pTxUIBb7722bf_tynpHlUIw8w4uK2g9NbCy498ktR2_IhXgHfY6KFe1cWdv3gVvg4HMc59X8wDmPUJtFxzyVgL4wf73IehZJbmNn9ZBtoHAdwF-AJwLlYIp4lB2edm7iItrHU9sF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
بعداز حمله‌شدید هواداران کریس رونالدو؛ دوست‌دختر ژائونوس پیج کریس رونالدو و جورجینا رو در اینستاگرام فالو کرد و برای او کامنت قلب قرمز گذاشت. دوست دختر نوس بعد از اون مصاحبه علیه CR7 توسط فن‌های رونالدو به قتل تهدید شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29435" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
