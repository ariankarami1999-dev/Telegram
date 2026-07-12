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
<img src="https://cdn4.telesco.pe/file/UVE4kDOR6uh7OvvoDUfGIXEaULS_ae5vGc8mSAzYrelbWk1gt4_Lc4dK_Rr_yDCzocEo25LoQyOLjVAyU1R35VACJl6sb49IaOqOPRmvPtjufM001mHfI4nK3wWTiflKjiaoGUNTZ-sVu5ACHdu2zJGmuB0w6Du8iZLx7Pr79RTH5lxF9y6BMNvDQIio6Fok9ztIyK4CygvczkAORQVu7jQ-vToGBQcbPCuJdLrFFkeXGu98o74J3R-RNXoTaAuEulT9JcrkIomqPTiVADI7p5KjSJstfgF9lzQNvi4Ain8vB2HrVO7Yd-hS5UOXTyr8aqVynL-fiCHC5jrWiE0Zsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 435K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 15:41:54</div>
<hr>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIyfhm4-xXY6hvSXYdouxvh0AaY3xNrF6NIKkYjfCuzh1FCDDqW7pOFgjMNdl6gGVskEldp8z4rIIzJ2D5tx0xNtMd_A1-wB-4GYC8qOgo-wWcZgL9Ana6Z-7meWmW0Obb4eY8yN2VjGxVLIVrbTKCipv3Ra1JTj-SJP9xcw5XZaYR-ZllCvsv33NtB8ceO4Je92YEHCA0jTJAxv_r3FfedmjSuwX1xuC7D0dXnqS54NVOzz1XnBEShTY9N-bOeUhcDb44Qbzy-f6tXRTS8qcIiXpRdzJu5U_6660J6EHiWFJF2enXhAqBT-q6ALPrxUEpDR2dwtSAGmXHVXb-lo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reO2uPjupq_eo93p1GYsEVDFlQFxvS9JD6Cxh8Nnxc7-4XHa0NN1IAoT2ZLXXSPQ1cRyzFuoQ14DIJt5jpuVey9in0v0vEcKvzTNEt_bupskG3jp9aoe7cwJ8Fq9vw9yQao_wwpvCDWjU8C-37tgyyi3VbHj76HUk7GH-AeRB8m6WbZ4QiKzMYY9WhPqDmpdS6KAOd1LJww-50HnMboCVCFEX8jAcF91Ak331d0m5yzFqDHzziExauNUvyKi9rCPzsHJNa7Eb6gyoLZjPCBavWjqq3OtUFq65VTM2fHCn4CCpyWi8EfI1VzkRFVnI-I2SULs1JgOIIpo-ZT2BQX_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=LZiq8C26xUqwWxclyEhVH04X-F22nB6ruYfYsVcuPlR-qL_KvyNknJeljeJeLL0bKGva1LT98IeSblxViIhkzqFT88Ucsg8_pyuiVU2tqqpiZzHJvXVG9QMjakJdo59DgJB8K7r47cKii6V-zfvOiNwBa9x9T_-_j1GhJ3vHxfb4aeEO9Yda0baYHD1cgh93F-G6XPiJ6mi4HGW034x8eL7HEHy7jePehmUqmRNtjojJAZS_U4OrdSOub-RjPM8uPDJgwrfgdpXShSIVX1CUZIfTqfVB_AAtUTO2rmu9z-0zOzHN7BWjlW2ud9rUG6k6d3zGHVC8FHqtPr8DTphgbVKXO8RG2cN3r-v2VBPo3FTiiQpmQkflqZ-0UjqVDCT_Fyw8Xbyyy_t357qAcB0T0WZerMEGAhPdJiGOYoQgUX0VI4_q8S4alLHXFMyLFtmoUPd-vHAkUn4AcqmQpfjxxEeoTRaq-scowcWiV5dhd5pIIf3vGMZtEWFcPspl2TWqMBqCwQc5KrHh4QZU5oPPit2BG2pQVERPj5TcJeMs3q6GVCgS1wKf-gwnE9gUtHzaGJ56QrrLELiDCinbX4EqV9957cuII7s2Q9hEI1qdJ8ppExin_xVWLCfQ7iSw1NBRyjwb8im9FjJXO5LF3YGkulfBgP7ARlzV7m6ufzvU2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=LZiq8C26xUqwWxclyEhVH04X-F22nB6ruYfYsVcuPlR-qL_KvyNknJeljeJeLL0bKGva1LT98IeSblxViIhkzqFT88Ucsg8_pyuiVU2tqqpiZzHJvXVG9QMjakJdo59DgJB8K7r47cKii6V-zfvOiNwBa9x9T_-_j1GhJ3vHxfb4aeEO9Yda0baYHD1cgh93F-G6XPiJ6mi4HGW034x8eL7HEHy7jePehmUqmRNtjojJAZS_U4OrdSOub-RjPM8uPDJgwrfgdpXShSIVX1CUZIfTqfVB_AAtUTO2rmu9z-0zOzHN7BWjlW2ud9rUG6k6d3zGHVC8FHqtPr8DTphgbVKXO8RG2cN3r-v2VBPo3FTiiQpmQkflqZ-0UjqVDCT_Fyw8Xbyyy_t357qAcB0T0WZerMEGAhPdJiGOYoQgUX0VI4_q8S4alLHXFMyLFtmoUPd-vHAkUn4AcqmQpfjxxEeoTRaq-scowcWiV5dhd5pIIf3vGMZtEWFcPspl2TWqMBqCwQc5KrHh4QZU5oPPit2BG2pQVERPj5TcJeMs3q6GVCgS1wKf-gwnE9gUtHzaGJ56QrrLELiDCinbX4EqV9957cuII7s2Q9hEI1qdJ8ppExin_xVWLCfQ7iSw1NBRyjwb8im9FjJXO5LF3YGkulfBgP7ARlzV7m6ufzvU2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDObvdSp8zY6p6LC7ow0x1a_0bV83UC1Elnx088WXaLd_u0qWQGVKzGw4t-2b9GoY7ATLMyBJcRQpEIKhhsIcBWKPPDWnDvSSzoJyIyHCAHpNxyiFf3WlQpRYQb271smZPPo0AC6XG6hGvRI8uo6Dyl7lWGaxqNY3yvKWSehWbPdTNSc5kp38tZPoCasaFr_JYSa8NCZc4SlL7RZ8knsSE6rFybCschcULan_o3rIxaTOyJYxYzkdPlefgGU-hwcbznt3Trt6s4risoUIvWrMps2yj_MwHy3SWHupWUE1KMywMbAsUq8E06QecMR42A1E8uiVHNfS7Nw_NS-ddlzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6wXzthsNyrA1uOoPxZ3XrZ6XWhtRvU7g2sVuHWzXk0z7m0JWg5hdMZKJrku1jm1kYHFYvSZdCwgljV_0AzsbNXrdth4LqwYFlAHf46Heepfrq5My1SIRceH541IHbvAKKfPvrwb02D3kiRDR3jv-tkmz5zxX4mbRS1Z2hoejZGdEuBcJPkTbw8gKN_joFoQe_4L7r_k7TJodee8Rr5t3P8XLcBZhnqCUcbqR9kx4SYhfTWuksJeuP72y_lUzmgzy-B7VoZea5yeiCclqIPL6Qa6AB2zqPOFnw-KmkAYbA0WNJnnw7YSOrzY4-E6MAEmuBZc-YkJ012q2_4JqFHhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkZ1Ldb1GlfROK8STbZawO7U2kpYNA8Hr-weRwtjf3ib5dT3JpTvtrRWk4LwsOg3aqCgGyfgErdgrJC-iw9ghIlVHvNqRNTsKpiUHxPUNKDRtAQZH2Nae0GMO_aFSHBgPGDPLjTNvWudSCtnZ8cNT0j-WRq3OH370synbj5T1Y7a7NFTlIAUfTGA8OfKdmDwxv2PzC4LOhX6MRJBJa9jbzixBIWfzqhzPMbIJgELmsI35fPEWCtnVg_aN-4XRzbO9HTCJOt-Ao-HWfeUt0cX4bvZCWOgQar-DAmTcQ3e6_6edpSYVMFblxFKfoz0sP18eXOW0wzD2J4nIR1xL33S9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErXHRkzj1mAxWJQ_ujYPoMLm0TdgFWQ_W3ek6GjauM5JCEJWNz1_HcsKEX2oH4tREVkskr3RmORCtyIq3xpIn2SjsAevKvq-Bk1LGP8HLHPWBgFZbtXViLqN6cwYtpagNQ4XUOiQpBjn14Hs6CsvzPLuzo0_MxOJr1Gn2xIqYiL0G5_sUKJbdwzrfJTnAxrxi45EfMkLtv2WODo82cbPyt_gUoGs9X3Kl9TyXDMRsqMHchFZTK7DxZYOhnlNlg4vvmoRXqLPnPwyu_LTbVRrkzxpnMUj4FeiVgVqLGZmsc2CV5D-ftHXbhD95YngJp0NQmJD8acDms1ddjLfFRLEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3yn-09Esruwb5e6Gqybdc_8FsQJRfidqMVtdIGxHeD-wqTdqAKXl2GUzUlXGfDdmWwDs39dNFiHFzbz_UYb8ysFXo20zhs2IgW5D-XZLFM-K_THQ71dSGUWOT-vCnqRJlj7HobrHeQtQp5jyyCk7CFRFSw92ZMMjL3BvJIJYERDv1TbJgMlRHEtnoTDv81smrHziog2JfY8-5oxGV2ohoRE9RqEl95OBZKQxgjlFHDPNRBVvdHgXwJ6KmQKRimVFJlf2fPyjGVvsAAkXRTPFRU7cw4m5-HTP4fzNly3lGFZ0EGsQ896PJ1t1A52UzSYQsv80JSg5vtKyCYpVHzYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pirnEhanEAfdU1fFgMrlDSrHTWqVc9_8CX53tnuyVivvqxBNwVT59aRqjAxaQ3z1nNDHZv_q6gqS4DHE4E925jLKZv2EPdYWXGjaXa9z16Ekk2bviYc67MKKkEMaWlzEyCqPqR7yGjShx_Ca-t1Aeudy5vkljMhhjnGsAA2hw-6c9yExYQIIa91AJT9AJHwyvklPzk1N6K-0c6UmIGICYbC1QXlooidCx8602rrpoO7LAl5xwUzdZ82EHmh16xv-Dd2mHY3Ga778z-k7BacvvDz3ACqSdyFVFiuEkAdRxjPdfaz4JDU0Qbwe7tIdZQux4cqg7svitn8QYZ8vWS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=I80nTItZNdTCKkfuSLXF8wcSU3FnQl5Feis8oFZZVxoKFCjgDmxdAtmJN-QB7Dg1ZV-3QsTRbX7KHLrFpn_7vGtN3Me2zCgmupIUrFRqJ1KBH4WdCjp7M6DV3cQZkZ44LWT2cznpUfnZaO1p3flpz0DvcAH7Zn9P_A2SU_OhFdgpjZ7c1zYIPGILWATPIJCK2hexTXt-zhvojkPq9DdFAEfh29sMCcpGlT9HSZCt89DolNZ-oWsXKjrBUk2Ay5d1yrKqQEt0_MXsXIRXy8csBWrr0llyz3UiX8v0aVAglAKth_CrcmnLL4SC8dvdQbFVqGlw0R1I8Crkv6vImf-B_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=I80nTItZNdTCKkfuSLXF8wcSU3FnQl5Feis8oFZZVxoKFCjgDmxdAtmJN-QB7Dg1ZV-3QsTRbX7KHLrFpn_7vGtN3Me2zCgmupIUrFRqJ1KBH4WdCjp7M6DV3cQZkZ44LWT2cznpUfnZaO1p3flpz0DvcAH7Zn9P_A2SU_OhFdgpjZ7c1zYIPGILWATPIJCK2hexTXt-zhvojkPq9DdFAEfh29sMCcpGlT9HSZCt89DolNZ-oWsXKjrBUk2Ay5d1yrKqQEt0_MXsXIRXy8csBWrr0llyz3UiX8v0aVAglAKth_CrcmnLL4SC8dvdQbFVqGlw0R1I8Crkv6vImf-B_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIN5sYFGN7LxeDxtyjk4r0VxcfOGKcmWH9o7brbG2Obdw_ZzFq20G3yDVsM5evEuKz5xVXFZjnfVGeaYauFkXf4iiH9pkrRFf9HyVK7T9Zhf6ssCjsxaFe1FmWJoryD_xYjJHIeGfWUkGLgr4fiWjJeDiNvnzH5cuTvwW8KM8JP2DWugOrSj1PeAh_rXvTywr4vr05f6xksVR1-3is8i6GQIXlWc8dbiErfB0hm3t_sxedKo_DYGDMsl0mQ_zlhmRuUd9tJlAFh2fbwlI_f4KVSU8hS6_gCNKAWHgojqO6knzefD4UUnBLCIxs_hadnX0CpkPXG7N-51daOQ0m0dpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjs5bxTjsfcFshbPqq9BCg5u6eOW6GOx-hsPflui3N39Zlh9UbNwsktDzrbecJmsJ9OBIT_ROIhdjkz7DDOSDu4jxaA2U8XiQVUNXBqU07bASFXexGfeOVvywAn2ArCEqd18YDN30IwQ2TIxQ1aw3Fr2JxQiuml0_IJetemYwBWnU6psXQLBpOssK_IxE79Nz1pPu4aWmwnC2q9__geMP1JmfXCvGmHQUfGbCnCRG8rG8VH1wW-F80j-EhkXG70nifxoN4edUFdpcteEz6WoW-esrc90iN68vlAJM9Q_Vh90hl5tH7Vc4HWw5ltb3_c_luSiVVzoCG4Bh7XZ_7WHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsc7_WqgsnCTNwdAUYGxmBWY55pE1AomIYjgbVSmBqOrhDNC8uk5h46_QChUy4PrYuyqt2kH3JwWXS2TVV47Qe3wDAGEB3m3Cg3m2Eo_4qxKQln6yzIFmh2wlaVQ2xkPvfDw9NfUtbbGiuLL5yCzkHmOni0AGEC34lmqhSLf2aqymrHOtpehmjIuH_eEQt57q9Q105p2CzoYJYo4wSdJvjZX6Qg8Q-SjJ28_4u6P_hGjAXJ9PddkFHTxXXMzIQ2E_SZMgrCGJqBUQWQiHDklkCn8haW_35EOzSksdTf0BSPwmDlW8fUWBOgEc98rTRjXnafxG2FcF6yzGdISelWPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1HiyRluZ4h5anybNnolz0FOwTte-vkFoFRBKmZD7OIJvSibUTsPrtUFCoYCLjfc5IvmFFWzu4Y4pfBP11veo7DpxwdxjxCh4vuqvzv9zix6EY1Zy0-k-zfQlujErOticqYAAYahrDBZLwd0oY7iDv02Etj4S7UCXf7vpa4NFD4FNYsyKgew-OyLkl7EzVbYuJ09KPKqC5Te72Gi1jK-asMwMPJCS86SXO2qFv9f5V2XwnlIKT2HXFrowIlzSQATJJtqYSxPw4JhtBjab-7wpS0yhAgQJhl1ioQ8ctC9VAkXDr4M7tWPFavF_k5zzYu02C32riK7eIbR9R45oVayRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAqn_FqBQkc8pASUX7A3Gya4EGqekPhx8T-2MFQu3Z7oJO-xkCMZUyFAxFsNzYvGQZHvEO0msBXhvAejcejpXwpeheMUWhu8rtiArmOei0B2-FqOe9Ycgq6N-npig5HVWG3cLuFSlqJ9eQjTI0LORLyDgxLgxKkoARRmnAXAwuJcCX_14fPp7leoW1pWsOE8y7n1ukbYzMJztuVZ7mPtWnPw6hwVfBWHvLkLeRWu30hnuOQ8Jp_Osol1YJOWqcqBAXHuILUrCLaDjN7m_tgRmS4myUuLoBeWNb2wJ-kvU_Fg3JifLs6c6E8yFZKXpZ9YFUMlLORwBaof2TiocILW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=Jfp8QO_FYyNUIA6g3BRbLf1ZhOlYPnKGM_VvctUXKCHzb-AHcAzsFkobU55jfdYREWZgZZZP3urR8LAAsjFGt5orkRjLm4EyfYbbJ7HBRy2j4yqwOPyLryGlk8tVGJzZpMChXcqvOC_u8q_PzZZyoz9GFY2bBdhiTvkluMq-6jiQBgWQRUmhplvlN22yJey6o75EgGif_r0z-Yb8cmlPdS5er-Nu6ISmAIrjKD077ysTpuY6vgLifJ-uNMKBFjwDnI5ALPdJbQQeJ0QSrCVWKhRrMHKLZQ6VgnH0L_Z3Y7gZ5xr0ErTTzpXqH5zA4y3zC1n4ACGXZTNhDApUidTh7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=Jfp8QO_FYyNUIA6g3BRbLf1ZhOlYPnKGM_VvctUXKCHzb-AHcAzsFkobU55jfdYREWZgZZZP3urR8LAAsjFGt5orkRjLm4EyfYbbJ7HBRy2j4yqwOPyLryGlk8tVGJzZpMChXcqvOC_u8q_PzZZyoz9GFY2bBdhiTvkluMq-6jiQBgWQRUmhplvlN22yJey6o75EgGif_r0z-Yb8cmlPdS5er-Nu6ISmAIrjKD077ysTpuY6vgLifJ-uNMKBFjwDnI5ALPdJbQQeJ0QSrCVWKhRrMHKLZQ6VgnH0L_Z3Y7gZ5xr0ErTTzpXqH5zA4y3zC1n4ACGXZTNhDApUidTh7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ0fFUEwtXThD_Bv9YSbe00ozW1FlX2VHDBEO0xAlk0YHKOG_TlOMgaZrt8Mm1A2pEDNdl2sYV689lDIRRTS5aRAPEsWLziZoOFWZ6dbY1hY43PnIwD5zvT5C0aM-mXo7Dr4-jjbHu4l-P8zbOGICd6Vlco1U0ArtFktsDAWLB7LBX5MzQcNBPhVVr-vHI613p2cijbpRmSTgu5sPUJPCG9nFVkoZD6xYc6Bga3mCijBULOh52KmjUCNYy6zGWnGBdPOrD_jLvSgFg1qAgb2XSQgT3yLggiy8ATWePHnXEZ0LBC41YEJt0bhHcbACwUo3LDF8TsnuvGCQszfqzCuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری بت ویژه ی فینال ویمبلدون
🎲
بدون ریسک در وینرو پیشبینی کنید و از تماشای تنیس لذت ببرید
🎁
🎾
فینال تنیس ویمبلدون
🎾
🎾
زوروف
🇩🇪
✖️
🇮🇹
سینر
⏰
امروز ساعت 18:40
🚨
ورزشگاه سنتر کورت
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
بابیش‌از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
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
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=KgXG4BM7cQfr2otAxhJT2U7jJSwZf6qFvKaUr4UoOBKMiWjqbYkERwtX0pb3pwrzh53TieTbOA0jNvDzwGrUssjxayiwwinoj1KTA7td6c2zWzPcQWmfisSFtP7tCLW__YY1Lu9zYM3WdAJWCFXRRlubC0-jLU6DQp7PvYozvSFDBfk513J2KoEkYiyKA0Jmqunrq9etJQUUtrNLTo8qR8YqVeFXGCIPfn13B1C7LNsSDNxIrHGUWxxJ_XYw_p6MPPmFFyucOwv6mBFjDfEoxBq6CI-A933ir0x9DgfhQJg3EVWQxRKJzAIQ-LcyulBlBnZN1FCtRUIljDcx0u7XEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=KgXG4BM7cQfr2otAxhJT2U7jJSwZf6qFvKaUr4UoOBKMiWjqbYkERwtX0pb3pwrzh53TieTbOA0jNvDzwGrUssjxayiwwinoj1KTA7td6c2zWzPcQWmfisSFtP7tCLW__YY1Lu9zYM3WdAJWCFXRRlubC0-jLU6DQp7PvYozvSFDBfk513J2KoEkYiyKA0Jmqunrq9etJQUUtrNLTo8qR8YqVeFXGCIPfn13B1C7LNsSDNxIrHGUWxxJ_XYw_p6MPPmFFyucOwv6mBFjDfEoxBq6CI-A933ir0x9DgfhQJg3EVWQxRKJzAIQ-LcyulBlBnZN1FCtRUIljDcx0u7XEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHzX5qbytv8r7vor81kh7ev0yq2p8HD6K-375Wpu37JYyMKFGulSz29efNMArGHk3athr0tOj65QJF3wdIaXgTnOdb7Zz6S1jNu3DKQrGoea5avRQmu37XF0sE4zjhJOwMrlcji5k7Q7ExHrxcHFD0NCCSZYwdrftEcZlewNchIEy7YXTXHZPbCqgqDmuEnVJQyMFRXTli50QMF42X8Wscg8g81oq-8UgaqlRADRZMTDAdRt3Ah411QluJrAt0xm5GfSfpsxjyfJ4ITQx9CJJ-BL9uaHDY-cir8fHQzl0BYwJqbQnuQ41AcjjU41WsI5tvrArFaQG0iu29G0S5vgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjkYM5kNqZ8OfF1LA0-dxlE35i6stmGFjVQNP8G1XR4NQEE3-x0FaIb8xTMfRnyCTfWxSUdL1LCC0z6V0rn-KPrN0AEVobb9ryCuVjavuuYd2c3W9M1q4D7csxaK8nWPy300mNYcSlBwZ070tw1wCZJqxEUk780Ac5TzbF-UMecUHvF6qJXZfP6iyA8RYJHyu9a4PhmOUgNmVoMJBD-T59WnUaqV3eXIKd_T9YwAjZOnZnTSvLA_FsKMeNRbLoRCII-39a1GnqVgyAJmUoh9NfMw3Re4I7u7J63qwL2jAhgAX87CbsOVRL_RZedaJIAjdzjfnkwy5CnftfCx3KgE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_j_kptCKXSiPEEGiIf5YYdSrSnqmgR13RFH5h2gyLTCXUV78C28v1erYj1vvq-QEQ_JOGqj71vgSZ7B28jtDsAEwE5p50TZIT5J7fqpxVCIs7MPH4mepvn56wgGWIYMQXIC5iowtfn97kND4YJ26ETiKY58IKJZ3jxUM0JRxRw8rwHyWcSzArpVb4WMC1qIoC4RADcgo_MPj6jqYaQVxE87OeVryBs4ShzDOLhTLEhSdBsgRS4hiG9-eioKecf29_fPp26uMQIK06jMnjJA2o5FbDdMViyYD-8Un_LAAitP0YaS_EkG34ycfbGDV7EsgbOVH0Z-gKvbUQVkCiqiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1-RgkumQMhyONcM4YamG7DcL5gQbQjD5kcV35QWp3m6MuAi5FkonpYilB6f9mxlN14ZDW9RRqf7XQu5ewJ1XLnZksHPTkrPCXYAzyr_DE3XMQlVQ49LmjJEPkS9ISADPb_tcS_XA5xIxEkcC5hv0GtmpXEvsN5Q0zn2pjgupG9nf8SeLTItCI9ajovyKGepjwZLM0StTleW-Ce-bCCtEjulnEL9mBssQxt63BiK3LriP-egxYbr5HHkS68-QH7ZzoCNJWYdvBdZtNW2rMkD_DXH1ZIrAERL6dYZoAmX1dNLmfGZh9hrgSxFjXAmmyNoN0qZXZmPR4WHnh_DiB88jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iipIDfJor0R5Jk99q0-b8TRx6xpnuPY8G5BIO9_qDTsJpS-XtMaRJFJy-sfaYgxh0DkZTixX8-aqlARPMIR-ZDe4GWWoX3C-HaAhYfAC6N4-1X_RP6Ob5G9rjrPx0WuMRUVDn7RMRcSIvtEwjo5mHWjqLaNk2ya-Ci944aceD3B-K4227NqOc0jKqYJFImBq_61FLlSUMQGl_SjzR-LvghBsDC8uyUGADvVmLVYJzCMGcfaABWjmAmkDCrsV10o1rRQ_Y3jyeixiklcIHqa0hgLTIHAJ5I4-qiX4B_uB0hECISF1NbexT1lbxNAM94SLBkzWMpIGZagBx5hkIdvFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGyJitRK6n80XPkkiAJusw97KlmdbEL4W7ziwmD6d80h2I3zuYtT-wvV5D5h1lU5P8Fqhz27OnGlO76G_n86Ib2eG0nV_xZ7_4BPmx2Aq8URE0joWg0FK8LoguA1xgPSPc4LYYfrcIrwVFOh2iIQRvBqQqN6lqGyK8IdwvdmtyDLCcOHgeWpR16R4FMDOm1-vvVjYmk9ouG-LBWxuz9eILZu7Fc9XkzXd7OZmIzjJ04ifqNh63I8fwnubkQFbV7RE92x008o2u3PLr4nBwnBkYDtXqesnz4tQ8els-qz0UzHjcM24hDgylQwKHA_hsAqDAgRBRHpZDCYzJECdTegYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDWxq-dYXKStF5Gwun2NBi9DWW_asRlG6GumOEfuO5mgcnz-mu9KjeJz5gB_4JV4ZLDnRTaaD6xQMjfhC-u3fU3HODTJtuVElOJh2RLBbrFY1A_GxOucHuO5XerMRONVxaw7i-p3mpktXOpYwqJNHmKFJ_1xM8XxA-MI5nQQ9M-jB_c2gOkikDnBn1jXGVxAEPhcYrCmotbAShLav5dh5-a0frvCZEHYvAE3TOU5BzbYZsfBQNlRHouXjXxGzLAO4Np-fHZCW6CH1QT3Hwr4n3ACDfcwhE0sxxynFOqk6r9bZukbob5km0WVLV815wsMeMLDtvU-C1VW13EqqAvhmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcR6_mOgBqhmIbQicjw1J6gb8yD6_gpOstgH-R4PTvYY094kvb2PiMrh3Qi1zbLUxFF_E-Fssrk8PBC7fxZ3FkLy77teYRYIW8LIM_q60vhVTy49_2k29bnuwdd8ni7frxYV-iRCNrpPjT-nX9wu3192X21NnoNZdnvCcj6ikypz49azy7tTr-q7amkCDdnMrGgHL7O7k-nyz4aaLnlbq2tkmAQ-Hmjh5HJjBg0DMGckJEOu8i8BYCHFUAYso0zmt_pLmClII-bTOVePh19316-rzJciX35d8v4eyKAR_IG_mvfBgPBHUqejUqpsTLM_stajbh3VXbCxaXRa1HicCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=pL9TK0KcLod7lysk0yj1IJooTJgDR-Uc_YiPItVx-6p0Cq6-Rdkbc7plcvz6oCa-3n38nRKHjn99oHa2j43Pw-bX5qJ0Pm3zpvbSLFKL-NiYmtUPG2qI5pLMqtTNMAgXqw1TebC5GUgtxM_NwuD2CPV0M4jypBlwozxkYLNoO9Pj3MdDfmLT8b-wM0F5nCXIxco4iSSMHxRj3iVGM0uL2q7ZdIe5EYPvuHqhlE-ZEgBx33k_5gK5X8opQjM_5PklSMLJKXDRoDfZ1OCWs2oOQih1iaDIa3e7I9BiEKqjqkWuANztIJjLjjvkJYU2D4u-9lX-loyO6PirBlHq8UlCmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=pL9TK0KcLod7lysk0yj1IJooTJgDR-Uc_YiPItVx-6p0Cq6-Rdkbc7plcvz6oCa-3n38nRKHjn99oHa2j43Pw-bX5qJ0Pm3zpvbSLFKL-NiYmtUPG2qI5pLMqtTNMAgXqw1TebC5GUgtxM_NwuD2CPV0M4jypBlwozxkYLNoO9Pj3MdDfmLT8b-wM0F5nCXIxco4iSSMHxRj3iVGM0uL2q7ZdIe5EYPvuHqhlE-ZEgBx33k_5gK5X8opQjM_5PklSMLJKXDRoDfZ1OCWs2oOQih1iaDIa3e7I9BiEKqjqkWuANztIJjLjjvkJYU2D4u-9lX-loyO6PirBlHq8UlCmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVmUmyPjNl0I2mBLko5We-64VyDQEvFzkkaifS1BCkpAAgDD-Wgpn4E_PYykD61kjdHo4g68f1fU6b4fMLB0MaVkQW9q9XUW57M-6lkGG-wZS3qFmYdKmYXzE7u6vXdqhQVM4Im1I31-0cxD30a5NtyGHtk6nPQaicTv7XCdhrnHYklTSXWn_vdhg_ibYR9u7ZQgoyqNcbHvhX3-EuQ7SHQm5esH-pcpEBioR8PKu7NpNSkPfGCbsO-UE7vvRx5O948PL1i4iURS7l3WTVE2bNh0XcmP79Zy7KONxD-cXweQe0Ev28yak3i1SLPYljjmZl98PtQPTanyjJxNLLBwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB7xiHwHTNQQo96gOqhJlBsdZAqdhHF1HeiGHYLwoODgb1YC18D9I006agHv_0VBx9hFCvE-PmWKcY-bbe5ACCd42JYk2x51uEeWCuMbiHfsXMDdO-xabS3NklySabtfg6Lz2HihybkyL4YZOleQoUAnivpz7cI57I-awkNJjAMPjgVz0FJF1d-M7BatHkyXWOiZEmObc49y6Gkh8LoEJvR4LFrqyAyYZ-1Qepetl8Xt7dBd6FV_4Y7AH-Z5yCY_ATj21HDdv7gifRsXTmmsWJOPGZU8ziy566Dh6VQbJHOkqx8x8Imxq1Tau1wThdAzgAiXmHYxT4fCeinHDg-Z2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVBlmIuV7RH-1sWKuWEjwBePalO3uaVrpyWMCYjNFllnRgUX2MWjIiqGYc_ugk_xBrr95h18DaAQx6asvK6C5ViNegif8WJffLRAfBP0TcoOP3CAIq4nrKgWPAEtmgeSYy94-SAjk3t6U5akz10oxQgfcVd7gERA3ih6hofJ-fyEC0dZxB1mXJdTNVGC3w3yFzTjNCN0tWDCaMWR4kDV-pkNfQPWYi52gLp5yqvK2jdUDk7Kd05TVPqY814MXnoRn40EmEfqPmwBr4ep4nZjSdG2dfVoZvfG7asSRvC4dSDBLDExPpynmufUCuSBpiv9gaGYkCr_kEkJUmPqPGtZ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDfKyLyfRzX8XBsNTUtaTGBSFVj1c36VcVrjdAI5a7rDSMckeNEX8uiZ89hD1rHEp4IlPstn43PP_303cxt9zYZ6648KvJltnd6ukFTjp3ulSsY5gxRa-cofkEDVmgrhKYf3sW05fEdLRap3H3xQNLRaXWHeTsnuHoeNH2n3_PGNeVl8quMtG-Ksj7chbWnDHAhasA2F7FkPEoA1h4Og9Mkp0NoVay7dw4kTF476_Z7FVGquoR6nvJqZvxwgwVSslANTOdG2YPMxGY3JZ1P_U94oUOW0V6aXPry8oSIaBln-WGEd2mJZ2tTic61qKbTH_JHW1IUUxXzl9AenFBuP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nncQmIqs21lHpXKSBZ84_bv4i2jdEBTC97gkq7oRT6pcXt_qycqvfHjkvWwhDopMKWlbl6ZkcGIy_h5kZHwXuQXWmYjSVXAUyQW1Zl_D7vPo8UBWDhr65_stntabzm6Csl53k0MYZeJL7hV3t7RsYJInliKDXd4aHKoiX4Agp_3s2c2nm6MPLWOVLDrWa253A5d2qINFmIxKsvF7ZjY0c04mxhfdUug-qlzGn8dlkKuI6omhncNC1XlI75I6F6CgqzfT-HLEvqShQfTyGAhfn9tK3WiPMH4yZvC2hpVk0TickbCRINPmTIf9GvXyK9WOETthB9rF4Qda4aXlmRkO_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHCTmcpEyGF-ViCbF0Waz42bWgwfiMjNI6cdpTz0SBUNqSKFyv6ZU0o5Hq1xpBljr2KokuXT0MHX8-T4xJMRHIUkGnvyJoGsdCsqtEs2NS9Ocd-2N8JgWkcV2MeSv6aVwE7I58JEoq1iicGeMtzXnZnl4TBB6owbK9U0s7rAcvVEqVoc_WIc3-u6C24wpvEEkMM5znJ1hi5VS5yCK4KcmFsmPdhOr2QUUUcF-zMmW9DMKlAwWb-Joav6_4ocbxHkDKtPoyv5FMnAOWHAMo2KcS4smtFT_UewphhUI5CJeYdIaBo-4ncl6dPJ9cPNnX4L069yqHbxzArfs1d3UwRQzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdYpDBUB1mtYs4uvw1KeEW5pr1GWocRYj3Co1tT3BRjV4yWfb8EqYj6SH5bXwIU-J-DQmmxfhRFNexozJj9kJHAqpzM6NkyumsbbBpkhBRMIGlI5yjPhP1j30u7x9WnGLeEwyaetAwFN7EVC0eTM9uDyL5kix8IU6B11J1tuYHzHpvZtah_tYWCRNb8TsNm-5O20i5rdWTSmPN3SvAICdxztA7rpRGqg0YlVwsZCS9B1Kt3UozWVLAY6GcPztVxolF7sCxgoL-JtIC1GYCaaJcdgr-BYGqVYDXk9KSbctqWALYLH5G9Hog012tRF7rJFME6Gl_dVBNllYaSaIp3qFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8rIdZJnEVI2cSgqZhwTOAYK4gQR5bBzB_c_6-2-QCABiW2q1c9T81Yi7UNHteQMwraplMcTOFEGF3j8BvkuejX6ClVW6b3mp3Zdz17zsI-RuouOVo_MZzOYLFVF3mkmKLbVv9Qu1CZcPl4b01Gprug4qbCVdaMPw30vgGnnFH2UwiOUJfBQTlYt_CXRo-c7pxt-DcHV1VvjbTuK3fMyCl-4n2Glcaod_ljTgHgV6-IH6gQP6uOsXcqk_g-xLiH7q1jtydkUfv4yDwBZ2Uo0mOMNe387QWv5N2NXYx6_NJsTAlhGm1IMedcCViTq5o6LPfUnJy6i0gjIQA4h71YNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrIVXFRhXC7eQ5YnRg0BmH7BzdQ9BqF6uj_PSVYzD_30xl1eGtWeDUrq_c-epfQebuzggU9Kl9BJObox08kQShb9U9JWEe9CqPpfxLSbb0omab8SPYBJYecpHGva7OLgLzVDRCvJfpQTqj8_SK8qB6bvEc1la9g9kcQHQ6XpfUZgOO1HZGeck01ZQcFEIIQa13Sn93IPSA73NiI5jlp5pxxCOvmV5MnTaUVQ5430Nha8nrmn95YQU0bAoshDQn1TwfhOgh-oaBK76FleUM8oGAwvJ8_tyOd1-9rRm-ubws8uPEULY6R2wtq2m30AhUKf6CYJOzKtGsNb8p6HDlvVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=ZYlxQ1b60J5TcD4Ci1cq9UXT4keYEYSqyB7WD_ZyQq9ROboKkqrzQdAEzyDugdQV-Xa4qBggCbNtHNNv5ESin--LwUCRILhuq9B09aPHP4jaA-onOTdTW6mZZQEJhCiEGEuSPKqi-QPvndhE_aBboa7HPvW5IwvdJsYByrh2gjl-F5K_2UYrT2iKRZLuLmyB4OQAT3O6goFfge72JftZ0ZlIn3lTlxiTgyVIPhJQ4Y_e5VfyrJTKSKENRQSyYo6cUDOLgU1_U5ZAQoYfSVZ4Hkc82t-uZPpG6xOi6p9Zmg4evXgrXaeT-aAu74-4jc_Rh6LwjdR8zwEw8VR4AdHNGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=ZYlxQ1b60J5TcD4Ci1cq9UXT4keYEYSqyB7WD_ZyQq9ROboKkqrzQdAEzyDugdQV-Xa4qBggCbNtHNNv5ESin--LwUCRILhuq9B09aPHP4jaA-onOTdTW6mZZQEJhCiEGEuSPKqi-QPvndhE_aBboa7HPvW5IwvdJsYByrh2gjl-F5K_2UYrT2iKRZLuLmyB4OQAT3O6goFfge72JftZ0ZlIn3lTlxiTgyVIPhJQ4Y_e5VfyrJTKSKENRQSyYo6cUDOLgU1_U5ZAQoYfSVZ4Hkc82t-uZPpG6xOi6p9Zmg4evXgrXaeT-aAu74-4jc_Rh6LwjdR8zwEw8VR4AdHNGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQqNu8F9JEIMOBaUPM2eR5qo0SEvFoEp76BA_LNrYPEydoxE7b_JZa-kybezcYlFbBhe4u0K70ZdT8UxxXyttMfI8FXJJleBGItUrxsoVIKTLOMfPHxuIBhLKreBF5so-ohV7xD1-sYCYRnEvMTA17FDxldKcaL2jS8m8nmKBye89o8SuJDYIilHHhnKG9U79xvQlCsh6IYC4l2Kbk1GFfxyVhfWKg-Cn1cJvQRjPus1I-4V2VDHnP65ibYCeEuKDOVFZC5w94PpcdzrTqCSJM1q_ft83mXRqF_qTzzbEkHt6FtN369cmcUt6F6hJ9mqJ1_vf7Yak741MLISJdtwfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=RpY5gKGkgWle53qV73Jze84YiUT0K3gXfUE9TRoFa0kFxKtQSGbY2afyxkmo_DQC79ppCYWE0liBTy_iq0hwZfeR0Obbq07xuFwvVqea1Wnrc-PThpGUt-ntleWjERe2wwoYQgen2pEIrUTxbOzh7typ8WmttU_-vC5pYBO33o_VmPDq10jBlJdHNlsR6btXHRy_l1qtAuIcniuxYRFLw3iveySWrQJpFyJdOlhm1BqShIBaPfjZEym0X1S9JK4HprZsuKVHHpVP2r6HwmODRCPs7nBZky8yIA-5Na2EyAj7hs8rTfhFDuzvwHVtd_C89sfEjyVF2sJ2i_XSvdJT6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=RpY5gKGkgWle53qV73Jze84YiUT0K3gXfUE9TRoFa0kFxKtQSGbY2afyxkmo_DQC79ppCYWE0liBTy_iq0hwZfeR0Obbq07xuFwvVqea1Wnrc-PThpGUt-ntleWjERe2wwoYQgen2pEIrUTxbOzh7typ8WmttU_-vC5pYBO33o_VmPDq10jBlJdHNlsR6btXHRy_l1qtAuIcniuxYRFLw3iveySWrQJpFyJdOlhm1BqShIBaPfjZEym0X1S9JK4HprZsuKVHHpVP2r6HwmODRCPs7nBZky8yIA-5Na2EyAj7hs8rTfhFDuzvwHVtd_C89sfEjyVF2sJ2i_XSvdJT6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYGzmOgKkMjHc6WAyLN_7FhJpZy525Tx2916UA6kSCf6Saq7-p0whB_YraQn-6LBSHfNnVrAYlCKf2wqZFyR4_9vHWUmvvlDfHXJB_2p8LXn6bN-B7BxagBTXPGDriHbN5tAMGC4H43BYs-RwL5h0t8IzK0XXvnGWbsck4XylJOlI5DPfVAGlMDN-zJDp4OM0r0OTjO7pA8wel0wBQltMPhVzOL7n6msb_vdgJWOjqQmJ0nwYAFbV6yO8u8v3yXpFPcJftguGjXCGNkMU_SwI1_ubvqcHBr8AJ9606NlkkC_Jw9RrIhb1uOLdd9hPHTA-0RAEs5_Nh3zqsfR-qqOUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4q-v3wSKDyLKMS6IAYbLuOs8AaLcdLuSce7s8aoOqFwTY8dakWi1_I6RwzcCh1c7cccTTfgd68y7c5is-jHGFlwqTpTd-V4hJ-KXZUSaRWKNoo05AqUK3qQL3pg1-KENxMzxpHGV0ZHWjSqmX-DwXOHA9Xe_ACMU0ChLwxqau3IljPD1UYpbop8CVvVXOyss0OeYRMU7rdTHP9-Fvv7k2ieo5XjsOWMNYJpVabFDyad_EjUPs_3m4UCFYex1iGkv53PuLyuxLCAiNtSPR3b6eP2fxzRTrGv3JHsxaJgJpcgs8-nPvzqTzvCPORuWgAvYk0fRWnujXkeDly8cYf02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJNrHrOyR5Nb4-hnwVmBRnDyWW2lszjwA6tkntkXepLdP73Gh2FOgQbCvWvAQ_4tgdD8h8N8TXZ7sdQ7aGlLwSmY9xgbZmL45sYTk1-twCOfYrhRDXC89oFSAK-nAuBqgc-vXapbRJugDW5VYRcDIceAF8JiKVv9T4k7qHwHDgOrXJua4O60-9SyHycmviu83OLzkUA59TTONFMsbLr7OEriX2j-mGKgTuE3bfNTKCaTDMJwzKaU8UDz4W2V58PLaLO26rA_r0_uFuOQCHBFtiqgSiVJakKGCxOW9352E63a4_6Ow8U9MPp_xkmmHDBDJb9THjN_5soAc02ser9odw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=h_Ob_UyrlI_7REwqOlOFpkZaaQr72g6xG8_b6cauUhD6ubBScr2D1iabNK_lWsennTMRFzvp04MpbIXfbVpePbT2nXbaDM8S3xld3NfZyvDp2xvkOqK1EouiM9LrYRhenEcqzWQ-IvysB7Et2miQ2A5YkVG7o_0xUh0xilWXOtHnQB8eMcBXTnTbjL_TTjVSIV5o0DGz9qx65prdHegptrh_6bUmnYZnft20hQKunPnR3mGirJG4PQQ-WNL4oSUVZBBI2p2TVeCLu2DpHfnvsOnKCkivoamMMWS1ufNdQAgk8DX9yqfbvdjEQilyDLxuUPro-qhCW5tKWJ4k7QjMWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=h_Ob_UyrlI_7REwqOlOFpkZaaQr72g6xG8_b6cauUhD6ubBScr2D1iabNK_lWsennTMRFzvp04MpbIXfbVpePbT2nXbaDM8S3xld3NfZyvDp2xvkOqK1EouiM9LrYRhenEcqzWQ-IvysB7Et2miQ2A5YkVG7o_0xUh0xilWXOtHnQB8eMcBXTnTbjL_TTjVSIV5o0DGz9qx65prdHegptrh_6bUmnYZnft20hQKunPnR3mGirJG4PQQ-WNL4oSUVZBBI2p2TVeCLu2DpHfnvsOnKCkivoamMMWS1ufNdQAgk8DX9yqfbvdjEQilyDLxuUPro-qhCW5tKWJ4k7QjMWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfXss_gFu8hfglirW-Vql4gGtGkicYq7y0H5UvtKA5y3TPgogPMOnGxK-IyKBZXDOCvULQ77IYqcXwwdewrDiF1dntHIZ3fgOr2NEcWW3RiCwIr09dpHoNvG6GWiUMBv8TRkbE2yYUiwu6fzmGo1LdZpR7Wxl6K00eXT9YrTCAJg9TBMvgL27_KlltDWFq0LoGEYIAaeBx65j2uDJ6iklUbh_S78GQaCzH4ql4iNk4VWBVuq0wdo5ozQDlbpVvliauqw-AxbwxYW6ZlcrWGvIiv5HCKjsrSeZ6k4gvNkghncNhtuWRn8Y-HPa4B2B4xATl8AzY-PMbTBCqShU9W4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPYUJPPo_fGac0ZzZV6oGIObtCxSKgeVPG02r5K_8xi-5FAwq6YeCm7qQ206uqH37NFYitnn0sR3yuxexTMbQKGROb8S1yz5PLO0J_uAV9lRToQv917mfG2XqUvSvJkebvRDlON8hPf4UUcpgGnTu7TEH4dppdTGh3AnmWasaJPaLzyMQNbcMuLl7YUECXR72fSxPoJOP3sEw-JLXcHie9epBg247p879dKq7gT-eyGiZoQU0_5CCXUFqf2GMVMD2JI7uQXkLI9aryXkvybqf-NGX0DK3122tdaBSct_uWRm4c27OQsl3nxdmky5oZhNOV_GP4lxBbXMsh7x8imLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLxzuWiA94mcjQhq9SUA4SadJXnTYCJTVdYYRf6l6JnyrEBcnL8eTxSAoT4zQxLAQ6d92vLLn91K9IKcZKsueqH7qvdKylBgJ6117QFh1jse0ZlZKew1KO2G-A6hXXCdZTY2f9dAgxdnbL7iiPhqkSNHcB_J4eIUDjWVZx7V9HjAIyqKHajUtgLBFkwNKPgl7p4mHpS_WOvgbJcKoXrnwbRzWJTbmMMWwpd0ro7moeeALRpBBdsw0FvF1wkcJ8J79iMnpiZc_CdFnRJjU2ZiJ3gMbw62t5P6Tkbl9-9F1NeQb4SZIaqQE-UyfiRV0iiAjyxOyCUPcL2TH7GAImYGCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r674Y_IOb0rkL0ibeZXeKv0IITTd_4dIW2jF-igZXPZXN_TgAAo1jEwYGCOu2tHZpafpRoTfAWCblnbYvvE4aPY0mp1-iQxX3Tsu4yIk3pk8GvgzJ-R7KwoVaxEHlSDqlx7ddaeLaUKX522S_aDz69gAgzlTk5ciqKh0NkRkQctCrMTwci1HSwW0MbDeJqkGfurgeiE--oTxM3Ykqh1z-vraWS8fCuxryBj3PBFBus9WvZh5HdL1XtrfY-hjmvYLf9xqmnW4sWy6qkllgoez6taeQdJc4qlBZTadoGDRlqnKsuU2-X5i6k0kowCSobKMmA1nPelSXfDUGsfsntxDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hauj-VdR6FvlZg5hceZhPFQzrsqMBIhfP6MdaXByJbcQ2RjulWzMPRMz-PP631FqfltQeA5j0ADOBgkdwmYf9Mj_x9im86iUvRJNB37g_Tp4UEMaWU8Yo30QIQ0cthmyBn1Tz8GrDt_6GIvq4ij4R_WtdeZ38_4WqQke2wvEpM9ZJvWWiz6BF22T4XrRMqdeK-JtZuB4hGgMSVLbK2OFM0m-7HrvOSbBUerKdrgSm4CpUdeLJ9tLCNhPSvrKhVFQSxjS3JRmkKy2QstB7t1urVZoE2jn4fCoFFnOmpUAIDmGJAOnnGyV4uzAIngxZJDAq0DIIdcvZOlQZ3TlcLgpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daELsh-fAvhWY_sGoX4f2JIccwoZhZYQpVvSNbL087qL63TM1tnUQyNc5Lmc3GECmTb_xBAsh7xIPqDpaFsqRou8vbivstr4AyCQLiDJZY-jS9UiLjPrgCxxIaNm-SYq7_XuAmiaDeS7bw9_HP1B3p95bvVlRg2_i3TezApgFlOWjfZHVH8lWwcOLgSbykV67LbvOeak2PS6r3cJ-35HQzEZYZaqoJ49mKJ_jTPMj8kC2FNMz-PW6yqGT3jM4HMo-1qsel2PCBdWUKRWYoLk96y0nv6eYe7XV3tcVoTAGqRbwsxblfzHrPknZMr0Kmsx6TR7DOLiR3LrvcGLTSYVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkoO-egyX8VysFFVU2-_GI_OcyuWKv_AZBbsMSrhQ6HVogKZXS7766tVKi8F_hgH9eFEtPM-2MMCKwSVHYx6z-N072c-qQkAFc7tIo0FbNMvWs3Dgno1VOSIEAucJlegzYgLw0oaECJ01TDUiiKc5e-cIV2atrgVkmbwKbJWIS5ksirgREj-A9I8Qb3Kx9UUTfIBOt1S0UH14qNRlZfKyTl2iexl3hEu3V5XM4wp0os_9hUjMNsqjVVB8cJByQ-kldBRzoGxY6S_TjLPdeL31ydv5xoduOu3AY6x_cspFwouJsSCANUmGk5LBcmddTxiCLggJjRH1-mkaRhdIa7Reg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxODSSNv1eqSlMK3En3LWUbQTdB7U3irBABBA3TClbFpkDLPLcAWf5zsSxFoXbEC8kTvMJ7DpP9FLWkJT6ZwEEuhRLYSk9H-j7bHln0dDZjxQ3ZGRj6BBNrjhKO4IYAcB92OErquAb_rfPJ4ntf4IkJbZ7qkuEAM2Tq4g0iW-43O7yYHQefDaknRsxK3N1zwVb3jA71qMkM_8HOWtpjM0u8vh413EdvR2XpAE6lQPrGjQ2ETHtmi93ejMtjr62TOcTIit3lrZz4QJoD7yX5AI2Pej5OIk5tu3v4lcnEBdC6HSRU9-IErrYd0yEO15IcH5JwXa55_Ubk0bAN2Ea1Aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=c2SjTZWEROV8mv2Z7Qaw1IWe4CO1sQH0kWK8nxtGymy_onsqFnMxK6hSWjppq6GmMO08fjjh1cYBukW6MTi0aU14OaRKKwh1Fb-GYSCLnCnCTAqZToYDcqq7CyfC-LFde3BS-t5dAcNVqGhieuD3Bb3ANkRbhu6YiZHlZrw9AvVnLKv9ghlBqxqa502-p4v4rEDlQ2OUtdden3EIY_sSUNOaKTN9W3y4ZwDfI5tMfBEZZxDuuYtirxE6HzAN0z074rJspY8yOwivgNMpAN0YC4efiQ9cA3R_41Hb_nDvOJfZ3e2MHWHRFLQbH4bzfgynA489EFCCnlevPvfiQD16dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=c2SjTZWEROV8mv2Z7Qaw1IWe4CO1sQH0kWK8nxtGymy_onsqFnMxK6hSWjppq6GmMO08fjjh1cYBukW6MTi0aU14OaRKKwh1Fb-GYSCLnCnCTAqZToYDcqq7CyfC-LFde3BS-t5dAcNVqGhieuD3Bb3ANkRbhu6YiZHlZrw9AvVnLKv9ghlBqxqa502-p4v4rEDlQ2OUtdden3EIY_sSUNOaKTN9W3y4ZwDfI5tMfBEZZxDuuYtirxE6HzAN0z074rJspY8yOwivgNMpAN0YC4efiQ9cA3R_41Hb_nDvOJfZ3e2MHWHRFLQbH4bzfgynA489EFCCnlevPvfiQD16dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZiYHlUF91g8byu1OuDnxzLqpeZYinNMUiRvyD5ziKroJmcUL-GiWiLm0XmI77CIzl_TSsiHfUeh-Nrvkk2U_xAmG8yrQ8hOehUVGPvKNWVqsVSz7w3TjXRgyI3H425uLdaZguW2lr-FG4pQuhHsZr2Axui6F2VPAr8KrFexKrxZpezGK0GqIuuBKUPG16Z8gLbVZWoPjlnIl8g6rUZfNRA8JMpD9_FrhhWgCRCIq6Hqa0X_AivPPHvtMem-uVfpkiCXWTJzckl6p6nWVWn3V-i-lkd36gKul7KJpzGgMC6tPf7_dMxfUvsVMr7pPTu1MUCBi-8M4j-n7A-4Ab-Z4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viYttSQ6j6ivqIi5g8ZBungtWydaixt0W5-Chi8b9yk3qlm9W_vAqCKN7dPtGMdUej8_yoBmoRmfFAYojv9H1LF2Ye6VQ3n3bLP6lWTWd9qMZj7tV7DFO0fprSszptiq58a4hsRnmSZm8ISv18qFSvUBW3XUjcybbZYl2FMeZqPeYtiS8Cji2q77PqFLnIUm6c75QktS31ySq2CPChpdbmzhNs9eaZkfmg66nLd8ZZzy0iBFoCFLgRv1HLC01tEeOFrh1awy8BR0r4DPCFl3GD3GLa88Upp3kBWtPcTLS1GHiC-AOsVe1KYFVIGEqPtCzdsMUoqXSbuwqsMgRtNwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLhumDobCi-mcUY7zAP0u2CxIHdOJgx5ufB09ehoUEjrKQ-REC5X87QcwP6z8Afq3DAgN5s5WWyHc8IeRjEuWRMRzV-hOTa-QwSJ2JWerH8eZ8uFeNgHeW0WZbT5slL90vHi_mPBwfG9TJm1HIxPELvW9YCksD2aRAwudIKyWCJXqqHmMkpX5dCAstHMN_kX4KxXE0J5MzubcEjnnBV7bhkiz98PfURa5__nux_sxUZOy1bAorZ-3Xi2MsDriryFFvdoFnann0rfrsRRi_j-d5bLyEnTbd-Kpdy33g5WS5kIpBPfW1PoCuyj3aDZ4bP9BDUT2UOg6o-vQuGMTa6F9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6d4cu9Qk0BkNa2LE8FAH6lDN0PmNGElorcg74VEIa-wdc3fWZDUXOFzNNPnI9ilzeeO2mSnMI-XGT0rqMcJ_ETo-Tlm8ZyR3SZHSVjhNenTMSV-aqbW9NPWrqs60xf6pZd-TGNKuMdNoUIRIDoJ5vqoQKongcj1mLzWRirRZpQvoOYAXU_L6r3FdO7OpX4nLbywjr1h8XezapWCoQgh4BGVzkJDRGn0tSqxabZlyZ5NtgVwXVkFltzAKLOrHCkc-JTbYaw9wPnE9KfMve2cThpssygNAsMOwuH5P4qwhgTejIERAMdvtphFHSz5oFlgRptuxz1DvO0mD1_d69qoew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb8zrXfBHSJzjmc9w2XagkrSa35cefnjo0D_0YeJ6pDAajSQdO2vTTHLynXFZ_7lt5qzvTVgN4yS4SLOrJHwCGISduCJuvXpop_-7MsfSWvReeUmlXdDMBwSz9TjEzvHxY_YgbAY6LytmbfV18_bwFivIdf1J9QB4y1eGsGzRh5nbRsynpT73t-mQSS92I9vDlHstJwTa92ndn2-jwfdOhUaOJh7G7-NbuvrBH-aY2SomPnDmEAQInlTqLSpdUTX2TfG8awzP_SifC12WqaIyIDvMU_B4sGs9n0Whq9Tedz3xcRKzJjQMpw0R4ajjOLGM-OEvV0WifNcCHYdWolBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huk6lDT_KgREd8PTdls3ssr5pB4UupVBf3doDbFRlipkWQSBmRnuyScGZMW-Pz66ol_qHQsi_hCzUJLFvUYyCDGDKiu3uwYQpKNw8je5N_BQbByhNa0uZOCJw1DTsL-DpBFpmTRvL_btQSyj__1VSDjclQ9SCdvFkSAwTbb3RVJ-DF__iBoxpR9R8ieHgV0mg1YIeo4WX-Go86gbrq9BIdf756TOPbwioKRuXQXPTaxPC8Kk-B6fAleiX8sHSqjZ4uPx7_j-CcNyvFDNheUQ_sgrgvH0aNyMgwfAOAoyylcKyFp7XSWREW4Ptx5tY4KF2XxU2QfRfej-YGA8_TmCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sirs4yrDCc76DzTlnzHQ5eIU6k9MQ28q1rVu8YW_rXALDGka2yHMBM0-9HySqlSfBSAo_JB9XWlS2PKWh5ggsyTvwM284ZfJbX6ZSRUe8CpGdtqafSzDsmKZ-FnGFDD62mJVUQga76AazuJr5lIWc1xw5o9IJVaPhnxd4GKCpeZuFqdMZAhXpMpEjkadiC84tk6pJiTqwFhmZAKT2A2CC-8Ss_zqu6ULmkkzbynz95caaitsrJaZ_qTibx2tUwO6Bd2y959i6tqPwHlG7aByQyV_UDwggXQ3qIT_s3Y-pTrTMdwllOjyZ1YmIXFtu5UzpBMY3aadb8NtAptRWfQ7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV2r5qkUfStb863P7hCzM5_6ZM5LTzEwNCctbVel0IIJYpHQoSz5M37rToeHa5h1-gCQ__H0UXAbjUFBRvZJ7-gFlt_BTyIvxuhZ3ZzLM2HOAAvQ2CA-z2Wxf0KBLpk1ipI4Vv_d0bKNGWHxfcspen7XSFt4tHQyh2J5_2P6NpoWgkgvxS78XeG8fG4Esf_HrtzwauTjAcN8Aobz5pvhbHf94S3JT3CzHSZI3z9U0Y42qe_MErkfBeboF1sjwdb_-8n4MKt2geJo2d_P7-v2_IAeYyRmZsr6nDxyR-19qZSB2pMvdnpzh-kX80vvxH18iCLgRgvI12_7cPNWPhHslg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5NhP8Ll5y_XsjI9E2j6JAI33LAF5fLIgBUN3EdIq7ezU_MpPc9aPNFz2DjtzUpQhPxkuofie5yl3muF4zNPP_Lu03-svyhEKvBYFouU1zmoiv9KxO__9T7TYHwDE6pWla7jtULFHG_tW3CEcFXSgUQhZ0siIb9BDercpQdfqcx0jGQIcD-6t_2EyJfhEYHGK0G7RD-aSgF6tsQAmjvNxhvro57csBy0Wp6T0KUJYB7zVd_StVYbxKSbVgi1Fvjnw95ZuvmjStRJfsY6eDKqgG7KJquKwz7uxkfjDkx5uBXj2OlmspI6oYnJVXtwJwiQIu-HXSasEvIjjx9cm3gKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiGPhfhCCS6PTHO4V0rksqSV4fWtOZ6rfK8mf5AMWNvlTOvTvWyWah2dZYm1H3u4hWhzBqoMSD2j1J01JKhwjpjDjZ-cbECZC6ur-B5XkO15gpFby-tnvmVSZNYxgS5I5J-cd7MrzXfzwYsHO5v1rpEpCx1CImslD96Lt4bno3RRUZFSPZS96IzyqRoj5XCc1hj_WeQ1FqtZkSM1RMjFq98EZd6uX2uC2h039q1B05Ae6qFl-oi3BMcN7_y-VQNqTz9VkcnQV2G30aueoezn4_G1BzCanEFCmPiCk5MhjTyR7RzzDsL7-XReL6V0q8xKlWkSXEwwp_AAm4FH0KDDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2Hca-QfuLzcvkfkd3ofoIV0-FEUHgWGbq_PToCjbdw3RuhP31bz54UAMVDov2TFA_u-2Hdoa8Xj6sSB4t7c4YbGxdlaNuJZ5FuT58xrpo4Qfzi5E85S5zZhAyeOCgSiUbQPi6qAgeiDXEwc_e7r4ZEZgsP9KKdVDsvVGef9hcH3_N5voANZCo0AE4YxJchHX2z0sp20xm05YKdE973XrYnxPheXyJlj9Sn8--qoOoDsh6iuw3eZfk0khMS4_8Nyl6fscr6MkR8BBL6puAEvnGqqSpKjtEBRZHUW87M6qVBWq-2j6xgO7txGiC0OWE1afq0vGLACAdSbYl3GLJB8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYuuZqW22NvJuEDS_9Y05cLAUX6lQUyMk9uQVWrgJ7d0izZAcz0oJBWxo-UyennmAqokWBjar5sD1T32-ucngJOnG4kVpXVETk9WF7cUrxNGMF80AGjhFLPQSY46mI8KYgcbE5moSJG-tIzZKD4m3b6KeZ0Lu5U8I5LZN_KmNnnal5jRcNgWqnBAD4N_rf8lMJHdWc3xZNfC840QickY-PTT31c8dsZxt01LsrtqjNF5DMhxW71vADZJJ6MwcFceXHJftJIm4fREx196sGLqJ4--HXfLqXSGJHKHOBpuDEbNC_hvnuVKAvIEggtzIZVGg-Oi7N24Arh0sWSQ09qH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOTIOInR6QRkkpLp_CfS41G-YTJVtcgC2RKIjnnf_05jwwAg-VvxLdUkg6lmUPQWAf5_jV5aRYAVYWP2pgDmZJ0oLSFhyMeC8d8qrMI5WcJATpOgqWkLe8MYecsyP5syfg2vliIrPFMX-FedAZd_aucmE6DI7uXgJmSU6QJLqEr0B6BzOoxKZR0OB1Jfg9BqSB33zp_ws-4bCRsdLcmh-SNEFwalsXbFeJNbBCg8ErYNlkAEyp-MoPjMiF_-C_fmQ9dBZEVULZVYfbluDSPm89XOKlE5yamWF01aCeuW0M_IoIMbWt58nA2ZVP1Buhepux5yz2plpooG9NQFYiU6fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etb5L4KJJy6zCxyMgt_3F6Pbu3LxS7mqRJiWh3hfs3fBssSJFz717BVK4cEx6QAe6J8RwgEfXrYRkYOpA-l016oOfSNA67rWKkYgnQld8CSi8a4oHVQ2MGemMRIMUXSJZN352pw78_C6ZV_6y8YLzB-YuUFJUk7p7NwpeITKtl_nyQKAu0sPXXFqrde7asVv8M1h-lbLC4lf1CbMaG7LW4HnSTSPjkfwk0Qf79pKDx_4CGzYcmsboL65Y4ogEE-bzDmhATYxwAUNpx052H1rPP1pqZWEG2XYNBUgJWYbm1WzUm3uiDPBxqKXCerGprwZ9djSFKp3qbzh0lYNLwGeiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=BqV3VVRBPY_t7KeL3tDGslvb11hHxiXmMSvnusU8oj4iqiyVH_0JslFPeeGFWCq9ctxFDTKZVftvvwehHlipFht0CjSDn66UoBpt3x9CllTD7zUsPdwEMN5e2lgQc7W4L2XUodbEvdCM67pFr8hCnWlJb1ShytUk8kOsgTFZ_Sbw-uvL1RXDBWJPXhopdltoObrfTJUd6MxZ7JvKGX_rQMCSk1q4E6ZvRSj4BoBc4qYw3n81nL3kUWeqbNV35gGnF342i-CV-HTW4muDaaD7XlT1HgXa2-RotHjH2wuVMXlEDRXg_o3AOrIvzULRMqOw5HN9DcV7vObsTwF57yLirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=BqV3VVRBPY_t7KeL3tDGslvb11hHxiXmMSvnusU8oj4iqiyVH_0JslFPeeGFWCq9ctxFDTKZVftvvwehHlipFht0CjSDn66UoBpt3x9CllTD7zUsPdwEMN5e2lgQc7W4L2XUodbEvdCM67pFr8hCnWlJb1ShytUk8kOsgTFZ_Sbw-uvL1RXDBWJPXhopdltoObrfTJUd6MxZ7JvKGX_rQMCSk1q4E6ZvRSj4BoBc4qYw3n81nL3kUWeqbNV35gGnF342i-CV-HTW4muDaaD7XlT1HgXa2-RotHjH2wuVMXlEDRXg_o3AOrIvzULRMqOw5HN9DcV7vObsTwF57yLirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsB5rU5aCPL2hc4mnIOwO0GM6ZM2OnPlY_Af3sMwTPjA1bQXii8_UiE6DvMVPpCTWagXD4Do65OJtF3mPBP2CCm_QCGKfmENeMBcvJL8lG8KguoNTIwRb8KjJlr_XKqekgExlCqmh6CIlJXeBLkJQQzGpks-0Ut3onAmw7xNHdZOa2o_9W1KUuebl_EDxf9w5yd4S_Hqb6KXC4_uAmJcMEzZtDQ8Ome4q0TGf72iGWtVL2WYL4_RNoh0y5dgKkU1D1_ZeXRxAYzGqgfyDSNWKRdzlx_cABxZZikNtzu29shtPFE-yP77tcpbrxUNxEby293aB3QdKTMvGIrlo0dImQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkfHlajK5jwDLyyvd8T4uSocPu-DZ_D1LTktMRI1DegzPfwtf-Lx8L0k0lZTqDx_KzVEMrjhRBXXK6N2EUcvZzXW9zU3PSSg5IYm9_883A52DQ4n1935vDrBPqGy3ATvvsQkgZ8AQMJ7r9jjqXBlM2oFA2UseI7w7bIM0pMHfSiKZDAB2c_7EBLXy-ua7z_RJIvMQJ5D2HN1ARMyLGGY9TQ6nnK3n-1BAjKcnGmmIDv7PMgEHUSaKeTLF7WjEJElVBKNuQTP2SGNiiOxPqsF5_7BWq6TwT1r6JQ4FjcAjcZZjqs5rofNQAfOd_faYvAEUDSS9WgGNGHZl3UwPOzoYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7sA2qbNsTjvVGePjA1JBr4Ijj53s4hEHgOaoOXtNt14tXPr0N0pXzH-nNequTidq-dUEVWOYgGZENC8l4FVQul3agcCE-QVs7SJXC6qFSTpARUB5w62pF9t1M2dB_KJI6uZkZNrWKKEXpcu6EK6R6GUxT-BAO_UgB4jx8fKgYkUzd6KqMVNpWZ41cWZmHqjsBbzLLyZ5CcNkI4HT5J3ARgGLGdfqqWOQln0-6tBDjrPLyhdcw3IGf-mLH_mrriL-2lBYEY1N1Ifk1P5XRrrzmoLhttlQ0PmDt2J9QbVoHmVeShWoueEkw26rOf2pTbviFa9f8K3O1exp073loXv7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sgc1uTytoxlacxPY4yJyLQI4gnLUAEmygf2m9ouRCmhsMtWX7aoUiJJsuoA4YLOc1_MhWD9fg50tC7azGUApGcxo7PZaM82oC8E01IYa80wHGJm3Ma8xv8FvHWk-xlwa_HioKVYJAz8oQKvOqjAdH6E5cP-uXQgp1KC6S-rXO4BiVAAkIvsypUtQvLAvEmm1DtTkEUWwfnqCjPFsBGQdn48vYedD5kEcDO7scY7afzD4j4sqjWalUJR45cHQ2dIUMEXpc-fLvd6kfxEFNYAYmYtiQj1JYMC5r_Kvm9lAT4XoBU0P6lhlAlzDZrloU9xf-qTMFB2I4DAI_nAWFtIj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHbk6gGecX2ZdhqE10HWDqy-JitbAM_5BnCO7_WjHRJntqxr7WG9PMLgAsY3_zAv37sfM-vZbTyPyFAGEGY3bUl70vqmBrLMc5PgmVOMWCA4EJXGM9pkSgeFfw-ph2t56vDrAKFEwBtBvqTZbFKYo-MOJ_mf9vz9f2Q_W9y24ZVSngiZ10nqYSk-yaxBhkowu7z-eYOEv3Hws9usIaj5WBZ1IxZcR2w2bCbW4tb6ro8TRUvvdptSuaqzJYCb-ynJlv7YW83ma81SSVsVjLHKzFEv_6Z4siNumdw3YQxb03cj1ec1HI52f68aYxPme3sUKVQ79Q2KnaIcHtkAxKB7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RO00sYMqW3vBi_NL6ag4JIeEE4xoGPDcXAHmU4akrcPmi-k51e3-HynwR2TUw_f3pYg5kvp7xOCJp04U_nTm31StmNuvE38OEGgyH5n4054-WvBCwui60bRz6joSNJ6IO5SvLaVHpUGa1HDct60zHg4IfDa1e7Rrn_wUfvYwPMEbU56ySIn_A_gmycggjR1CWOtlLDUXYChKeOuMHV7ROuHDmU819tED1A3u-sJxSqjKWREp3GTILxU0Xo032sQCoyI8H2O7UnlsfpCe8UcgMsc08QR7f_bghgV8pMeqtembqjexgR3SBBP3DFq5dI9rfWy1z1YptIxsvgaakT28WQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=eWKUr9WrL8pd4YfAFfg9SvWaP1Jip_Akn99cXDuJ-SbwwV5BclV199CcXDMCgsPCRLFudsAn29Y1PWNXNs45HWYU-vYNh73TURwjkO8RwtGR3thB_UZPIky3sQo7XiaQiRpE6a51rcGIlkXrQ-UsuBXDg6_guZBE2l6AIvl558pkTiKK3tb9hOE5FmAXX2yJJ028eP__p0sLv0ISbTpjvyDC9YtqNZdu0KkHmlX1j8TgPzrx_eecaDer5ByBK66sXJbmip_GLJNF724JgjC7f2tDywpnYGoswKNZTCkX2QegdYbvhUCvCstlyOeidpwiKlIME19p9DXusCxlOOCmXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=eWKUr9WrL8pd4YfAFfg9SvWaP1Jip_Akn99cXDuJ-SbwwV5BclV199CcXDMCgsPCRLFudsAn29Y1PWNXNs45HWYU-vYNh73TURwjkO8RwtGR3thB_UZPIky3sQo7XiaQiRpE6a51rcGIlkXrQ-UsuBXDg6_guZBE2l6AIvl558pkTiKK3tb9hOE5FmAXX2yJJ028eP__p0sLv0ISbTpjvyDC9YtqNZdu0KkHmlX1j8TgPzrx_eecaDer5ByBK66sXJbmip_GLJNF724JgjC7f2tDywpnYGoswKNZTCkX2QegdYbvhUCvCstlyOeidpwiKlIME19p9DXusCxlOOCmXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4RRRtgyyaa-T7RDbIfcil_bvRg2QR1oIJG1He6xGengrj7VTkI9RCLWiaR0kwzmS1SrfKM2bTILxZLbxWlnKr-2ZV0wJ5DVg3fm4Q8ycbLrsE1vtj9x-iYQKc9_-GW1_AvV4ek4_2WFfe-jFZdjKPNiGVOEJ0TTZQB6wOj2ZSJTMdzdShebIB3XiRDHohRc-LldDj6D0guI_5UBIH20KD34S3LBVy6vu_XnZLt8JYyIxT_9MbuEo8EiT1ISvzyNttAhGfEYbtkxFXPxA1i4gFoZiiac33hUSKaQUp9FIqiseceZeQxRTSPG12JdDne7rbae7iHwVlB6UvwjyG6wmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1fYeyHZNobsfXk1epSsg3GS_pV39erPk3VFIGP237f2-6ACXztV0yuV6iaaoZ7akn7XOBvFfjQbogNvsJQXoxEtETKiGJCiPUkmqw4Xc7CQpPY6WTEAfvKV1oFRyO6ERtfBroLTl9G7IDpfWOLvJNha8jGOSRcJ3cnvx2fFm1kDFmucEMXsn7GHjR9XbTOc7ogOtO9rHT2bfHIEZSdDMJjWeRvVdwmWvNTxwK4_8Sc7L610nqNMwfRCDWvzuCirkPgZRgyTUIfyS1qWxD0KEuIltlmPYFzhFX7HMzfwon-T4NDbr8xSjsHahBuv1-VQyZ1R8hkz48cYqyJu8XRFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKYyKFKzw2IKHfGjwcyjtgTXe8m_7QhA3cx_bKw2IxrE0j3d3urv_DDa6E3q_EEAeCgTEmBdVw5WztppUuNq5T0Q2EPtbBJLihmlCpAwe2QH-Rs4RC4ly8IqiperRCMDkFIPQ17lMVCJ448AiNjt4UGwwQanuUunvdf4JfRmU_PZPKZoI9t-WE2Dd7Vc_CEkDGrvj2O7cPion6Fc7yP90vljcxHZc3WnjprG1sBSArMFepADLBvocQEde80NNDpgGkuBPxJmwcNGUemsIanSOvb-Soe6fnR3uwewkZ-XXeptQ8bWOYjFt06tKJxinWr3grEYry8gLT_Qby4ciYTumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0yFJ_52zNUCtCI98snD9lGf3Ikcjq16OEnS9VaKSKC6fDeyvSGSV6vFn0EVHvfIndbfOYpTzy6NPPT-OgPnaIDQZXsBiMO34cikvX-zvqYlhWmVV3yBVn-tN_XLhNlvQjnZsqCDQCfWmeIaWYlNN4GSQNn1bhC9yPtlVG94YVgV5FMhf28ZrJDMdQqj0cJcrfIqka7LaHxrJM2p8gLuE7Zz55h7PQ02Q6NywRulnJwhkfdgGIUDM9tdWvHlV51FzLjd5yDn8dbE9NtKksY2nCNxPpW8x1xRuqsMI3k-88UFCR_YQC-ZcXURSCynaD-_n9Gz5qe5Ib4eUaDiP1WyBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krwur6LOFRwCwfk_Y6fzIvaOtdYBSOqy8mqvU2J09-G9Lf2oN6JsP6yQyFDDnZqcEZ7AtdSOY1BCUkag2z0wRdgkppfkG6CIMXhddWxJS-vvRcA5tZaFCxMyYCL1hc9XkNtrkU4gZM01R6nFTxvZed-YpJumdHLvrLLF31hOVQvUbIyQ1A3-Cr4-ouH_-iOdwNxeftFw6ykIo7BftDku9oIWgKMWeVYqnVHqpJdTUd7t7wzhzkXtK4PC05g4IU9V0B1rWAJwbccpYILGsV-2UdB77bnZTzoAGqywK8D6q4XqePv2MLoglgickkID9sDJiEFO7dvDcadoxt8E7gE82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGrmrJaN8a2cICWf7XEvSuBtw5t2Itg0Qipu2zB--O2wam1ECIcIIg7GfkxDCVt7MJ09PqITU4ulO_911sFbjZOPKKotTwRNomzpOMQH3t1h2MxbAyRUd8-CMgUIPw4HDjrOLoK4HoMT4AlKlxnNdjp5AwtJwx7BHPM2ADA5qHUSPhwTHiqcrnaPLrAiuIgejEOu0jM9YO-3W0duiWHifa2pKTNDksL7RQSbSIoAW-MioU0iP_27jabdPE_Xn3c8OslKFuuVKeh9ixQIRwIpMjgCLM5mbDqV2xaXNhr4vudFADZjf8D1L-6F2iRwjPlx-jFMQlH5Vz8b3-BIb8xlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Irb4mv7JKbuMpWVQwGqQ-icimRVeOybm2vkAyKPJUDXfiPhDGkAcfEE0qhwWrvXDWKyEUCP7kaJvV05mUiq3sMBfhmqjOEKL7MuGgQt8_ah9YJICKtWELjLF07GOXUZF4k3ZB-fg0KfF0ZB7k184VPbf72UlEvCT9B7Yr3fRNilf-BmOY3Zp3P-27b_7kq-ZRzyRdvVSisUtQQfkiXqoY_Di2JbHpLyAK8zi7TCr4Q7hQnyyslIg_BCocM4vxWZclSyvfecIA2iJ8DC0hEaudpBZRbFTUGGsCJQlEFGKk9nc8b9yhkNlf63zTY5nY1xV1r-95g2oco7TiPeapKpyZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=Owq49JLSAzZpybdQ8qTvJXGHr7ejfzanITYq3Gw6qMJIld0KCvm2TXfUqOu7eKB_4MnwcCsvYEXpZeIweiOm-rifAG600hYLuDQubln5iZzj9pyxIjT2dJXRmvjipTnsJj254NyyJM6PvTmmU3wf5XCn0L5XsPrGkT383dotei7jjwb1CXUWsiTiIJFH58CtSsqcFA6dzmRBNdGw4QSq6mjG6kX2WP7-qHiOy7gNWykSxZMZCGICoM000wNCQHp7L09I0ODWlI1P86g3NDJaYCmYAihh3LadLIGpMXfZb2PsJMEJuuikDy0_VJBTRrL8eCwAnaxRwkmPFtOXl-UW4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=Owq49JLSAzZpybdQ8qTvJXGHr7ejfzanITYq3Gw6qMJIld0KCvm2TXfUqOu7eKB_4MnwcCsvYEXpZeIweiOm-rifAG600hYLuDQubln5iZzj9pyxIjT2dJXRmvjipTnsJj254NyyJM6PvTmmU3wf5XCn0L5XsPrGkT383dotei7jjwb1CXUWsiTiIJFH58CtSsqcFA6dzmRBNdGw4QSq6mjG6kX2WP7-qHiOy7gNWykSxZMZCGICoM000wNCQHp7L09I0ODWlI1P86g3NDJaYCmYAihh3LadLIGpMXfZb2PsJMEJuuikDy0_VJBTRrL8eCwAnaxRwkmPFtOXl-UW4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6kZw2SgiaMaZTO1f914IcZ-uKr5GOfDjeBCfScUep6rlJihDNXGF35zdHe3Btce5jibtJnaMwulQgrupQLatZ4xkbgN8UGz_eoCvpyFzHwU19XcfAGoCJTul0sMv-Htf2dPFwWLw14VyISQuSIR0dqpLcf6m28w9pY6bcXEU4I0qnZYOcGUrUt7kpK5RZGRG_ddLALK1mSxnCm6bSFbxpePsXll92LagfPhaMwc7IDnb-7jTw83b4335gy78Ovg-bvqkTWczQRIciWGwqI2x1yH8AKByFdaD3LAzeoFlTaDelkEbS27Rj2slYrTEH4XYgUvwpyafJp-kbbc167hfOe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6kZw2SgiaMaZTO1f914IcZ-uKr5GOfDjeBCfScUep6rlJihDNXGF35zdHe3Btce5jibtJnaMwulQgrupQLatZ4xkbgN8UGz_eoCvpyFzHwU19XcfAGoCJTul0sMv-Htf2dPFwWLw14VyISQuSIR0dqpLcf6m28w9pY6bcXEU4I0qnZYOcGUrUt7kpK5RZGRG_ddLALK1mSxnCm6bSFbxpePsXll92LagfPhaMwc7IDnb-7jTw83b4335gy78Ovg-bvqkTWczQRIciWGwqI2x1yH8AKByFdaD3LAzeoFlTaDelkEbS27Rj2slYrTEH4XYgUvwpyafJp-kbbc167hfOe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKnIUB4gWHSNYU8CA3xe3k6oLU_uZ_Ez6T0GA1VxbKcfva3GSSuzrB5XqTYVUoX5I0BJiLATzxR-wekg-LFQDXt8DQLmMcnjDCtOYqcxZE3OaVSEFxdRXv223uyZTKYil8wsFV-Cn3QudCov6ASyTE0airHYIhlV6cqe6Bd27zlUxbKrpXyS8szjT0uFcR_ysJVwmfyhrwaSF-okMeOrCrD5HMMaRDD3DNejqWGeJthmDxK9qGd1qVKqYWyhIz6wQGZG-_7srVHfA3eWlStiZMw5h2ix0mUsGXfUOv7ybx5QERw42DMRt9yc7VpXD6GvBpq9RzWtXkcR35WnuEVCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLzPnyuXX34sBHKZ8jLj9p5YPT_OvUbIBwXTvl7NYCUeV0CE10tpULrZr69WG5V8m99D4JOXE9zjCaAQhKMLRCxPAer8UAprIdWn27pg0sjT3taugY2sOXSp4d_-SPYicxbDS3pnWYMswSf325DN4rQ_LThvtiGmVfJ818Ckrw8O7Sw70LyRApdKHGy2xmt_KcVOEGqHus3gOgDdscK0YR2a2tGV3Oo70sOkEIjBUrwazSYteKvv3dTVrakj-7pGB8u-4uesHUd3P0kwf9wS137QAI5wk-BVpRAQcDmAAyHQv636GKubQ5r80C--tvEBlGYjrIcMffKXXs1ZGP-uSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=COiqahDRODcAQEsCag5RkjM-S_WR3tOBcQAX2dZ20t5c_cRZLCTNGP5yz165PmNQwSabannvxpKoW9SRiF_rMFnPu1AIJC6TCf5vIPMGV-h83So0mS3NvF9fbiCKSs7nh_tmxdkOdZYWC40_LhdX9xGuIuJ8MQKRfUEXk74dVRXlKfC4GG2cSzWVxGbPGw3ZecNSJ6DabNXLIufbCkGTU6Dk70pp4FWHoBrCNG58DHlmLwVlmsq5UBHpcfQaBx5UEsNXlVr6jQ2HgQil3UqBk0PPpjDZ4GqYZRF647ioiFXhuhvYrbJu3GKmfHj8iWOXnv4LnbQGhDwxSS74s2HApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=COiqahDRODcAQEsCag5RkjM-S_WR3tOBcQAX2dZ20t5c_cRZLCTNGP5yz165PmNQwSabannvxpKoW9SRiF_rMFnPu1AIJC6TCf5vIPMGV-h83So0mS3NvF9fbiCKSs7nh_tmxdkOdZYWC40_LhdX9xGuIuJ8MQKRfUEXk74dVRXlKfC4GG2cSzWVxGbPGw3ZecNSJ6DabNXLIufbCkGTU6Dk70pp4FWHoBrCNG58DHlmLwVlmsq5UBHpcfQaBx5UEsNXlVr6jQ2HgQil3UqBk0PPpjDZ4GqYZRF647ioiFXhuhvYrbJu3GKmfHj8iWOXnv4LnbQGhDwxSS74s2HApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6uOESdBXm4MhSW-t32GfsuvdA1LBz1Xb3MbhwnJTPP39MQcYycxBQtfrzNCyaQjTp433lmn-3F2ESMpx3VSLwfeK1JkrzylruyP-bqwYfp8lUhg3BYE7z2-UO9f4oTsGHrwxAQ6iD3DpJgQ9DWHs36T9LPB9QKcbw3ZK5zIA_ImkGuREgnSiXWTuQbSYeUZH1DyY1z-y8kpEqKmzs2s_8rTqXIk9LIefGQxe1jNwPDUVRPhfcFaJQPUW3zhP5aG-fwA6D4QKLYi-fovc2gd4ObZXbgV00UMuzhuqhUcinfJvZXor4HAW29Xtqs3SmN-1CTBDePXsHiPlN3IiX3G0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RULdgkyrydWf-0kNtAsQoAVwNVtlNnA4Th7HiegSEeXqQYf_0KUP8xRT5mfyB9pPXHxnB9aOajG0aJniy3pJWyUYx-EIt090hXfc5UTJzHerfVmOVOeNeKRkPevYLp0-h7FEpa3Cj9EEHiCV_5ZhDs-606cWD5vUcXYAa7WRg0e_CdxDxjVZXnZpErxu_scUg9nVNU95y0jpLJBM3_-7nvyMGyzb_qmkUABolFoGSYaI-__4VmRnQxYLQpUOdHK4mZ5VQa7IXsFB6s6k2REkoTYief2vCaegMb1gD4CWeKpFn5bWuqHzO1qbiRcSYeOWJczjDjHyxCxRvMDJPXmLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf41UWSzp6nPcQ2232nX3hwi64R0DJYw-4c-wESQBk1pgYOhTYtxF51_KO7xBG2P5S96_lYkqkpl5bAM5KVjl96uXEGYdoDyi6w-rpFiZGGzLFeREGUuBO39Gs7WHwHZR2Lx_d-kcVI59Ydwg-5QF6xPE_mHpYxWVfAVDlSOu8NPkdZuHQKwwWhyAmIWKtaZy1uhponDttn7le8nYBAcFdULxyBqZGMQymKX69KrSzcpE_LhaPs8YseiJNftjh1MG4DksEnLc6n1Z0rfqRGRnc7gMxVpTEFc7_XXQwfUBxThBM9DDUKuydOM3GfDF-0yUASKPzDvs5-AM65ftclcCK3OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf41UWSzp6nPcQ2232nX3hwi64R0DJYw-4c-wESQBk1pgYOhTYtxF51_KO7xBG2P5S96_lYkqkpl5bAM5KVjl96uXEGYdoDyi6w-rpFiZGGzLFeREGUuBO39Gs7WHwHZR2Lx_d-kcVI59Ydwg-5QF6xPE_mHpYxWVfAVDlSOu8NPkdZuHQKwwWhyAmIWKtaZy1uhponDttn7le8nYBAcFdULxyBqZGMQymKX69KrSzcpE_LhaPs8YseiJNftjh1MG4DksEnLc6n1Z0rfqRGRnc7gMxVpTEFc7_XXQwfUBxThBM9DDUKuydOM3GfDF-0yUASKPzDvs5-AM65ftclcCK3OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls6Mkm1sTJyZ1tvT3dSd6aW1nPvXRqyBYpk1q9giKH3om5M4IMQuimNKVKT1v22vfbw80mp3Mb9sCMgePc9rFRUkgimnr5eFBREd9-fiqe8lNCZfX_jrYwAH3DVxjvxLNjv6bVdjIvyZrN43AxtIDzI9w49OQg-XoqiObGW178oJoYu9n0XlHgF4iRK4Y2bPCaw4TcxFYB01HZkaVDnH8y7BIRgYDG0AtybaHY9q-R2QqvgVY9SLu7iMz27aCJ-BFK_bjvwI6_q6-elO9NMad8k4vaM8aFt5gCWHV49i8bt0Wi5wJtsSN2nomeAGzkZ0UH4lfEIprEVmDBNKWbCwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_HmIss10zXrGOVEr7iquklP1-FhQbExM_GZFZWr9TdZqxlC3PcmujpYp6g24_UwziJ8MPXOiXR4-FKnUp8NglRDiuLhUw8md_IprarqsXgR_FCTi3foLcEpt0s7W4OnlIzu6GhO04G2WVA2lwwSJhVguDep6bl6v3glFAFHNmWsW3Om8nmEGZrqJgh3dWI8GylBuZbVMJgiPzeDFuisK7E7A4A2HuWGXcOuIL82X-MUJ8AUWHcNpPBojeBf_e_OenqtNOPXiQYOwfejXXFfPMetc3aAAehG2S4mqKZkWVB22vDSj-P8KLcMLepKXAhYq_Lggli35iU3AG94pnRoLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0FkXkxCe68OI6Kd4gAUqjXrcUews2fIOPJKy47OuRVvqgSH9uVYd0cDHFce50TE9UpVxZEDNROandjiyvuQcFmEEUkJXwcpUHoJnTuR7M6LWpqdNvEiwJAiEY2-f_n-y-MSRkGJ1bUqddykf0G7UhSp3FfVGH3CdQeFOpMl7h9vRG3Fenc4HQ3d6GFUFbpCOpQ2oyfcdqT_RoJGwasbwA4cMAYNBQu2mnnnm93Gi5ZxMpGOAHI8HuXpUcVMKQQMb-Gn4RHTtuRsGwU1O-sOjFO3VDgg-d2HyoU9TYDftjUejn_OPoOmuGntN6qa3cA_yXJlM-eRpy2WBTmhQtRx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=gT6qw4do_z6ckQ7Cky8RpTGz6I0s-sgAaciqNi8GpsZq8zIOM95DBOGvpl5tnoMP2V7-0msrMCT2X9L3wFY-davhndsVcDH42lz_0G7mo9NWHCxJAn_jcSI4jbHKP1HktHCUrHWKKdmpl9mZV08J2HFyvWajvULkDZ1sjrdfqwQOAOo50-3D_b_OxM2wFbRAQ-OFZT9poIjd8f7t1bBSTbgBvPEe28Ili7pcHsds6Fg7Xk3343XnlCz3ynMSXUPKygeOdVd1282-yluuyxZBiJ9QnrFyFz764wuIu-yq2jjVZJgbqpdd73Pi7HZehRFhFAGer_kk3bHq2F4yaR71rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=gT6qw4do_z6ckQ7Cky8RpTGz6I0s-sgAaciqNi8GpsZq8zIOM95DBOGvpl5tnoMP2V7-0msrMCT2X9L3wFY-davhndsVcDH42lz_0G7mo9NWHCxJAn_jcSI4jbHKP1HktHCUrHWKKdmpl9mZV08J2HFyvWajvULkDZ1sjrdfqwQOAOo50-3D_b_OxM2wFbRAQ-OFZT9poIjd8f7t1bBSTbgBvPEe28Ili7pcHsds6Fg7Xk3343XnlCz3ynMSXUPKygeOdVd1282-yluuyxZBiJ9QnrFyFz764wuIu-yq2jjVZJgbqpdd73Pi7HZehRFhFAGer_kk3bHq2F4yaR71rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=hiVYWBF9fuwDRxIyO-uMqGe1337c0zl_f1cLhdSVM7MTyrYFgmz8GXms4xvbEOSCb4HPnBXw2bHiGKmZx5DiBE28M5O1dYp4wNRyx7SpGAlOW45MBME7QBbg1OXOnqlk7CGhYEtrK-uTdw6nQfKKfKJZxrDg9sCd40Xw_ROqxOTtNi87wndq6zF_2i726Hfi9IH9Bkl4b6g_EIAy4vagKiLRQFMPbGmNO2mWGh8rSmlvmhAvpYRqpNVvf8XNdg85Sg4QZa6xyW4oDUiTDd-4gttM6_JjbCbxmjJ-7SGH9tJBgvMLHuEnqiuqHHItmXc35xLyeTnWgkhkoF3v4ernyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=hiVYWBF9fuwDRxIyO-uMqGe1337c0zl_f1cLhdSVM7MTyrYFgmz8GXms4xvbEOSCb4HPnBXw2bHiGKmZx5DiBE28M5O1dYp4wNRyx7SpGAlOW45MBME7QBbg1OXOnqlk7CGhYEtrK-uTdw6nQfKKfKJZxrDg9sCd40Xw_ROqxOTtNi87wndq6zF_2i726Hfi9IH9Bkl4b6g_EIAy4vagKiLRQFMPbGmNO2mWGh8rSmlvmhAvpYRqpNVvf8XNdg85Sg4QZa6xyW4oDUiTDd-4gttM6_JjbCbxmjJ-7SGH9tJBgvMLHuEnqiuqHHItmXc35xLyeTnWgkhkoF3v4ernyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmHBSH1VEwtpEMY_9xQvWaA_UCj2mfRVbst4v5kqx2v6wGeQum7QOgmH751tp-MAKyIjhHsHr2klavNTaq2aKnmdBRk1TTiGbOqIlKsVpolOa4xo4GFIDpdLlKjq-2Jzgmhnyy7nfT9pciNfaO4h83TB1L_F_4dh6SZ2PzMMeHHfYnK33QmeEV1tRK56e7oKNFji1Qc9DYuyIZCDV1OT1codloHSyf6MeVL-BLFriE_dL8_CthbKjoczNNtzrKYmzRulClvP4Dy9mfFAwlfNuk2y5RY4DyvtT1ZlE5QWY5dO9leWr7sEu0KEi8Z1pOJxXV-UCtmXL30t4fu1pThygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npl9iLKcc-62r_fwPGthkNo7j9fk19udjhC5m5A9frZYXDNXJi3YNkD-wMUT6rPlPh9pzB4HV4GQoiPS__VO-zZBf8EYsJOBvoTe1k4F3EIGTUdpZ1akLaQNlFHs_tk4tq2zm3ktM_fPp3bC6iLfdNk46-7mpA8BXBKLdUVHNoP8zwCkREfkqF3ewnPqDqE48BvE4l6kMrpQdsE-20GYRf6x2z9rzKIAL9AmLGS5tjwparZe-mHts41SCxcg2UegOjO2FaipuQe9DAr_-0N80P4ubjjPA-LITqVpkfjp2cenXkVIcPz9W0YXLXLhQvynHoJ7xjai2TawYBXqdVHSxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=k8aifj3Jl4GCXUHPzXFql1Qin9AgcHSN3WHu0wziczmkajKsUdm8RUFhh36RGeXs6o5MVshlyfxiUxq-mYUHRXAKrX3qjVp6vZwhSw9_8U0Lz6GKEIBbDQIF8VQRtMONdmdGQCP5Fu5l1ikcHtorPzr-gszg9sqlya5bTlWj7kONdvN5xXaBka0KkYqmU60fgVIv1yf9bxYrlAGSKJAkTYkK9dRIPpfftlFChb0iqV5WAJOfX9_hR7Pr35J9hcrKkumG6Ci_g4XCtuXqV193SX1qnvlzkn6XEFnYToJYAPnSkcWkKYiHP_2I4TP_5DPQHDf6oCwp2MRoSZCH5PaRGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=k8aifj3Jl4GCXUHPzXFql1Qin9AgcHSN3WHu0wziczmkajKsUdm8RUFhh36RGeXs6o5MVshlyfxiUxq-mYUHRXAKrX3qjVp6vZwhSw9_8U0Lz6GKEIBbDQIF8VQRtMONdmdGQCP5Fu5l1ikcHtorPzr-gszg9sqlya5bTlWj7kONdvN5xXaBka0KkYqmU60fgVIv1yf9bxYrlAGSKJAkTYkK9dRIPpfftlFChb0iqV5WAJOfX9_hR7Pr35J9hcrKkumG6Ci_g4XCtuXqV193SX1qnvlzkn6XEFnYToJYAPnSkcWkKYiHP_2I4TP_5DPQHDf6oCwp2MRoSZCH5PaRGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4Ze-lzKvx1NJE6UXBTCh_Ei-nZNY_kLFfy5vkXhX5vZugjJIHW87eGfk_IyrANxzep55DlxhugBD2UauJ7hBcsJv8fSb3Zuj_xs4RNa3T0G_MoaBjb0stoRbLa97xiBBZMw2NPoecxOw1zMxzhPWfJPdx3NtNa9fqWIEIU7fxTO1qpioKzZPXFjiKfXpRvnu4ABjcKBIRwkUKds_qQ8-SJ96Jtof0QBHaTf4XSzUTiJYS0N-I6uAUoUPsdAoXruO-ZI4_A6SbO4i8MQse_wUw6JAY_yijhc2LeMe-iQmHLkKDzAS1SjoWi2yKNQdQ0g8B8u5f0ONf_IXnJZl7vSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
