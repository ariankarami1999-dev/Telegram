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
<img src="https://cdn4.telesco.pe/file/Stt9jNftXn5zcfBtr0ac7NzkrG1s5KbSxM6OeHggpuyZxFlMLGTCZn2Jf5-RcJKHUd6ST-VBvxIUWSsinZr4QdZS12KJcJlozHDlZA08XEIejrrmKVlvzkacXWizAcswbAlGxZQE-qGUSeBpkh1i2CAwQtVSYWw6uFwpHX6x64QLXVIseGCQGQdPaX0mRx71ROVttEQXnS_6CnTV2ZkIEOlBDoy691CXcAIyMUeCKVuIeW_HXGJIR9jbEvmsa0IgOzSRt3l3iDA9LszYFuw0R8TZYB-vtof8_kRye0t1UkHMf9cCRB3KBJAlIug3c-c-q8V_M4v0WomkRweX9y4gKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 02:04:20</div>
<hr>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hqgcr5PWQPPXA0zKvwrpLIZDCrMYRPbir-rXHyvp_RrKE041istFZqZWTm0fzjILh0oYwnyxeBGCO1RsvgtGd6X7LPWAcv2kAYc710dfdio8rtjAikSXZMguqpyhCianznb3tOiLUa627qP-F5_WEf9vzwnG3nDuJFslJy8kF3D2tAqUMvQXNpRb06Toieb0__x6mYfCZrVQe5OI54yZ4IgMC_NwYWKTG9O9WPXgM8yO9X6sp1LYY7fXOWHUC5cZHb1-FXt8YhDseVmpC7X_JLlKzX2AKLEstQ_eiaENW9y2_NXyuLKvKresrgKPR32j2Hodgudfl4ffTyhjpP7lVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 677 · <a href="https://t.me/SBoxxx/21061" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یعنی همه چیز دیدیم جز قهرمانی....
هعیییی</div>
<div class="tg-footer">👁️ 829 · <a href="https://t.me/SBoxxx/21060" target="_blank">📅 01:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21059">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/SBoxxx/21059" target="_blank">📅 01:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=m-NaQ61a9y2MLpTrElDB6XgydWnpOnxp2In9qMJG7RDuigYgROOQK_iTnDKSGMIUZAAkByUu87r8o2OZKi-YkxjS6A_LBxfvTAbhaa6deo7dvaJmZtqovlWfSzA5P1kZbderXjDIyFl6iGhKsnt4mWoDBLKnLyVUMMawf9KDq1vz0hP5Bv1sy5bt_oj9GX2rT84Gvj_4mHvFTP3VlYH4o2E8jvd_q955JCP_xtlumnAhgtpBosZFSfeB8q_k0OrUQJQSZNZVWR_ZmOD1BzVe1TDtki5n098FcuHsY4albuHDoeQiJh32qlXQawKmUn8nIVvbU5SI1Yvdcg3Wii-g_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=m-NaQ61a9y2MLpTrElDB6XgydWnpOnxp2In9qMJG7RDuigYgROOQK_iTnDKSGMIUZAAkByUu87r8o2OZKi-YkxjS6A_LBxfvTAbhaa6deo7dvaJmZtqovlWfSzA5P1kZbderXjDIyFl6iGhKsnt4mWoDBLKnLyVUMMawf9KDq1vz0hP5Bv1sy5bt_oj9GX2rT84Gvj_4mHvFTP3VlYH4o2E8jvd_q955JCP_xtlumnAhgtpBosZFSfeB8q_k0OrUQJQSZNZVWR_ZmOD1BzVe1TDtki5n098FcuHsY4albuHDoeQiJh32qlXQawKmUn8nIVvbU5SI1Yvdcg3Wii-g_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/SBoxxx/21058" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=cNRl1AUCDPk3ynUPi4TuY6DZqc3KUEYSksCaSZfcFF1O6NM3dLevw_Dh-4sbmur_S6AQ5Q8bPW5OYgmZyjMm3Wkwfc9ruGAY17h3GHBnzeqwvJZ4zJwlG-qBO0XoJbZm_K678kXjyViYWoDhntFNzHJqx6fsaJhEo36ij2NlXSCWUJ2Z2xVdqfv6Fb1j-yEXYsASebq1LLyTeWBsvj8BomakApbJVkL4MwWDVjcT1IIZmeEg0aw8Q_kUAqCCDq9dRS-3tYxRKJ8I92TiYVfGqmwDGfpyEqFS-qZa_8rCX9IsORma2BGSLztWwCVdcO3Fh_Kctvs0aUJlwBg--1W0vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=cNRl1AUCDPk3ynUPi4TuY6DZqc3KUEYSksCaSZfcFF1O6NM3dLevw_Dh-4sbmur_S6AQ5Q8bPW5OYgmZyjMm3Wkwfc9ruGAY17h3GHBnzeqwvJZ4zJwlG-qBO0XoJbZm_K678kXjyViYWoDhntFNzHJqx6fsaJhEo36ij2NlXSCWUJ2Z2xVdqfv6Fb1j-yEXYsASebq1LLyTeWBsvj8BomakApbJVkL4MwWDVjcT1IIZmeEg0aw8Q_kUAqCCDq9dRS-3tYxRKJ8I92TiYVfGqmwDGfpyEqFS-qZa_8rCX9IsORma2BGSLztWwCVdcO3Fh_Kctvs0aUJlwBg--1W0vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستندی جالب از روند ساخت و امکانات شهر موشکی یزد!
بخش عمده اش به نظرم با واقعیت همخوانی دارد اما در بخش هایی از تخیل استفاده شده مثلاً بخش مربوط به نمایش طبعیت و روز و شب برای کارکنانی که 500 متر زیر زمین حضور دارند.</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SBoxxx/21057" target="_blank">📅 01:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9AII-bhifzApD9vBTUbwMPwz1503nWYWZeIw6XoKL3_yVq8WCZkCfF0a--7uk_QD6lDnoTJnBTU88ErA4P93gZBXnwvlEDxzwDSMi2jA7UWAVzFECQS-o3zg-U4MriXh6HMxjI04tTqScNeGemSSeck4QtOiRPF66BarDOG3cANwcdoNqHgw-o4qG3twiMoCYEp2VfIk38aFtodEuYcTx8aGrq_NS6s5zpEqiCkXFFpvXGYBBxLrLfZogutJIaDpWRLEChNJh-wkX_2M_mNRSsz7tiQJcTP_edMKVC2Pwbiw-mBUqYI27pjyrXIOjD8VRNUhk4ueUquwwK-bFInZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SBoxxx/21056" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم  که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/21055" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7235f04196.mp4?token=KDKrpIJNCc7opdWc4UiA0FISha9q2OcVpu4C5b8jEgATv9J3FBfHO0n4x2Z_UCRCupRmptQEHHOzF_hcsXu4M7YbsFi_97gFymThmmxUS6D5j7SN8Gw3ghjyQNFTGhTvNjjS2ChKVWwvb8FnQSZeWP3i5sNhz6kmFrWwgxJIOogGZVfPP-kI3108QGwVtUHGjTZnfkhx3yJYu8bPx1CRa7t-mmVoivH7ZTUwquLdEjz-66IV2KGh_oDLzwgHgy2Iw7sYAIYrPMtlsDj8aXGqzZwURFeYYvLdC7utFa0meyGi6gOPPvXf4_F8RdVELEuSzVgB_xGaac4mShgYmCc6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7235f04196.mp4?token=KDKrpIJNCc7opdWc4UiA0FISha9q2OcVpu4C5b8jEgATv9J3FBfHO0n4x2Z_UCRCupRmptQEHHOzF_hcsXu4M7YbsFi_97gFymThmmxUS6D5j7SN8Gw3ghjyQNFTGhTvNjjS2ChKVWwvb8FnQSZeWP3i5sNhz6kmFrWwgxJIOogGZVfPP-kI3108QGwVtUHGjTZnfkhx3yJYu8bPx1CRa7t-mmVoivH7ZTUwquLdEjz-66IV2KGh_oDLzwgHgy2Iw7sYAIYrPMtlsDj8aXGqzZwURFeYYvLdC7utFa0meyGi6gOPPvXf4_F8RdVELEuSzVgB_xGaac4mShgYmCc6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم
که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/21054" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaRn730FVlq7BOC8iJj_QF6Vs6tAEZlBt4UJ4btxrq6MiV1GfUKobjtVJ402EFJycSGcwi1TdED7xM0r4xQQ7qnJx8fJphBuFji-1viyGbSWc0WmRiDx0x-033GcQYRA6EPVlg-0r5RdPeiK4cVl4kSlyWbevnZUe5FtgXKR52A0r0A0qosVqGxT5NDcJJVfmvQt8V_cIFzzJ7efdG_Mq28bwTeQwcVJgxSnzuVlXuxn8RNhBtoK9Hl0bqfpNDYMcwTiDnsER3NI4lwI92BrX1grxp4h1eB2YAyQj31q6i_1Mq3yixEl872vHf0zeAyoP22CQA6pT2f1658K6n1EtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/21053" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/21052" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSqv88Db4xRkyIgQB9d-pyTnBQlGuJLzLrIHadXh1jFGJQt7w5C6puLali36U9p3Zt68ix4UrwVNh8nbT7W8RazVTrcD1UkC1vXjYDwwmrcqfito69F6b_oh3dV51uAfO4NSvl2Qh1tOIqDXRySEp2T450NLg2SAXdmllbzcQS4AmqhlsEiAbb8aR0w9ZDx0zKU-NtC9F1yMGrrQ6saaXnlU-SM_r-Rrh5-gBD-IufqE4Xiz1DMrX2fpOgNry_74ufa6XD9F-XM0emyO6-oA-yL1xwTV4TDNk0pLDR8Col20syjZEw_dSl1IPmeTYVTGMET5kUUeNDCH4JgWKxqIdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/21051" target="_blank">📅 23:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حریم هوایی اسراییل هم بسته شد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21050" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8H5xPSHIArNZW26qX7o_SymkE5qpeekHA61RnJxCen3WERgKAtNtreohcaTZ24E7eHhj1zYjl24mE67Q-KSAvnz0CeVdWdEUirs0GUBWEHA-mdbJPZImiY9ZKr3xCLy6FD01Nd6-SOBZB8cFZBNYSeHqleHgq76VarwVCUSy6hT5s-HBrk9J8SVMhkzZMHeFtwwWPxXIk2bgm9x_lcXnjzux4mf9E-UmYgtSAq9X5ORGH81xOfIaPIXpX4dPqseYOmLMYP39n2-rcSQmcg2M1XDHrfQq_uWldBDaMH9oWQQItypYpDM0osodsdm28gGcNsWPpa8eQjRn-gnKXjmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:   صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21049" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قالیباف:   هم میجنگیم هم مذاکره میکنیم</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21048" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین  شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.  در بلندمدت، اختلال پایدار…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21047" target="_blank">📅 18:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21046">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIg0wrCiLif7oy03QzoGPAF3t1f_pjYKGsYwRCooYhs1iQWXYDVK4qxZbiPxeMs0U48ss7NPuFkVNK_0Ae25tinzj7dmrVR125a6nN6w5NL4ixBlWr3OVgBILJJcO3eVysFwMrkuKyGSFP5N4lMikYjaUs00B8XwquKjtcaMpvQNuH7OwS0Ho9YXo0lDg3P83LQCpQfLVaGfTbkqH7JRjs_O3iQ1fSE7yczcB3IpNngo8dDnrKh4wJNsk51XBzRVeqYwYmKL_xwqLutFsGXpE8nC-7-n9svXLhshAz9m-7Jj73aL6fdNAC1EBS6hUATovQKuBsG_H1uVMV_NJtv-Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین
شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.
در بلندمدت، اختلال پایدار در عرضه می‌تواند سرمایه‌گذاری در خودروهای برقی و انرژی‌های جایگزین را سرعت دهد و وابستگی به نفت و اهمیت استراتژیک آن را کاهش دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/21046" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21045">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ به فاکس نیوز:  برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21045" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/21044" target="_blank">📅 17:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21043" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21042" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/21041" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی
#إيران
، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/21040" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رویترز:  در این ماه، ایران فرماندهان سپاه پاسداران انقلاب اسلامی، مشاوران نظامی و تجهیزات مربوط به موشک‌ها و پهپادها را به یمن تحت کنترل حوثی‌ها منتقل کرد.  یک پرواز شرکت ماهان ایر در تاریخ ۱۳ جولای از تهران به سمت یمن پرواز کرد و بین ۱۰ تا ۲۱ نفر از پرسنل…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/21039" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پوتین:   رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/21038" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21037">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا:
براساس اطلاعات دریافتی، آمریکای جنایتکار .... بار دیگر تصمیم گرفته است با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران اسلامی را از سر بگیرد.
هشدار می‌دهیم چنانچه آمریکا علیه ایران اسلامی خطایی مرتکب شود، تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.
اخطار می‌دهیم چنانچه کشورهای منطقه با تداوم سیاست دوگانه در قبال جمهوری اسلامی ایران، با تجاوز شیطان بزرگ به ایرانِ اسلامی و مقتدر همسو شوند، همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21037" target="_blank">📅 14:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21036">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فایننشال تایمز:   عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21036" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21035">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/21035" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قالیباف:  جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21034" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21033">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این تناقض را نمی‌فهمم:   از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،   و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.   آمریکا دشمن خونی…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21033" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21032">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRaefipourFans</strong></div>
<div class="tg-text">این تناقض را نمی‌فهمم:
از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،
و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.
آمریکا دشمن خونی است، اما با بعضی‌ها‌ کم‌تر؟
✍️
پسر سوم‌ خانواده تیبو
@raefipourfans</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21032" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21031">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قالیباف
:
جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21031" target="_blank">📅 12:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21030">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBwaZmtMYSAnFvgERj-vC6Kb2s4I-a5jjHBLQtpDPdBp4kZAxBvfG59nMVFlapRPy8zIG28oN5F87Q9tp17xL5ZdARkxcKEni1UT2XdeNP024MrZ-6EPr4dgPkFHQ-GQVQifAUjIKXkKmS1e5G6mRhAleVoRB8yCCCP2U_fr7lq2I4UNfo0CryH_eKhlEbwwkEzf6d2TnD3j8EyQKyHStfjMQanXqnVH_OIHT-tTtP9ZAzVX8XukxZpfYElK9W5rTzAb5aBl96QCLVsDHTOxoRfUJi5ygTrttmNDueFT0G1d4lOInLHwXYO7p_TyjtL92YjRDi8dfyCEKQDea5gpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21030" target="_blank">📅 11:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21029">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانال 14 اسرائیل:
آمریکا گزینه‌های حمله احتمالی به یمن را بررسی می‌کند</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21029" target="_blank">📅 11:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21028">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHdLH7tjUAvvbuWfhezmSDyRiYtXtCX6hccrUPjWxEEYYjVmtcrUCKI2iRLvnnGtKJ6dxIw9T_2wnbfgs_4u-fZtp43fyFmoignthCRh3l1weS2CY1nrgy4h46JciZjP4o37T1DdddFTIBqzbwY5xq7mN1-PhJxPhohV8hwJR1BFKKG3eTujYNumc1rDq5k2I_6sml9DpH-e9A8gkSzIhHqe7XsWqFu3CgSO_vQBeW1XK249YjzN3gEmlye1Fy5nXtgRSL7L40FwjSp9i2K3IDJMfn6oF4vPhs6fDIsqIhe3UALs6cBGT6J9t8GnAwlx6gr8vJjpDM2ayJDej1bLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.  یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.  ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/21028" target="_blank">📅 10:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21027">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.
یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.
ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون تن نفت در سال است.
آخرین بار در ۱۶ و ۱۸ ژوئن به شدت مورد حمله قرار گرفت، زمانی که هر دو واحد اصلی پردازش نفت خام آن آسیب دیدند و پالایشگاه مجبور به تعطیلی شد.
تا ماه اوت، گزارش شده بود که توانسته بود تنها با حدود یک‌سوم ظرفیت خود مجدداً راه‌اندازی شود.
اکنون دوباره مورد حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/21027" target="_blank">📅 09:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=EpcIRLne-R6mx8fQ1TW8tYEV4J3shbUS1WyloOa4w6y0GxAfxiCq7w2Mk4ivpENuyPFpTjyTHXd7_LgKWF8Fxc9SFIvywQKeqrdPozHW4f3bJD43pDuEvPZx4LFMsxKdM3J7QszdKBmAlvrlfrpkkeUCflrgr3SZuBgIpO340UwbzMbTo0ia-ZKE4eQ53aE6Evf6Q_3LeKTXFNYgYT60S03zc-nvAQaOcyCa0of6QDHSYRlgHptD9TNm146ofqCMlubMMFCuubnBzHTXmCBrzWJFI-ft1YQj52eZooNcybr1MlQc-5HYTOxpxFgKkByRo29zFBFXKY9DQ0dle3IQRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=EpcIRLne-R6mx8fQ1TW8tYEV4J3shbUS1WyloOa4w6y0GxAfxiCq7w2Mk4ivpENuyPFpTjyTHXd7_LgKWF8Fxc9SFIvywQKeqrdPozHW4f3bJD43pDuEvPZx4LFMsxKdM3J7QszdKBmAlvrlfrpkkeUCflrgr3SZuBgIpO340UwbzMbTo0ia-ZKE4eQ53aE6Evf6Q_3LeKTXFNYgYT60S03zc-nvAQaOcyCa0of6QDHSYRlgHptD9TNm146ofqCMlubMMFCuubnBzHTXmCBrzWJFI-ft1YQj52eZooNcybr1MlQc-5HYTOxpxFgKkByRo29zFBFXKY9DQ0dle3IQRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امروز من در بازارهای مالی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/21026" target="_blank">📅 09:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=EKgXJWDD5Cnh3BxUXKPDvScbkQvEVS-B-3oStg1q3BltJNO--igFMNmOkdT7Wsrk7EHq-Kgp13uwuc8uAsCHp4XDSZCH7EKwdtTeWOeLZEgWqh63yhekzdD0_NCKzISWPioiHDja8Az86I8ZO1yhlgYV6ulHenQphNDe9vHUHWTteRY4F36sZNrqf207AOGIO8axTD7iVYQf53kMLq9TjZDy-LCU5Pf8G3uQE2L0uvebp66M-X4aY2IBFZNCKMaObfe5G0P_LV7sfpahnirFqRzncT3YPcAGiKvAe1Culd7Gf-3x-olCfB06djWVNlKJ4g-GRnJYb6ZBvJeo3lskZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=EKgXJWDD5Cnh3BxUXKPDvScbkQvEVS-B-3oStg1q3BltJNO--igFMNmOkdT7Wsrk7EHq-Kgp13uwuc8uAsCHp4XDSZCH7EKwdtTeWOeLZEgWqh63yhekzdD0_NCKzISWPioiHDja8Az86I8ZO1yhlgYV6ulHenQphNDe9vHUHWTteRY4F36sZNrqf207AOGIO8axTD7iVYQf53kMLq9TjZDy-LCU5Pf8G3uQE2L0uvebp66M-X4aY2IBFZNCKMaObfe5G0P_LV7sfpahnirFqRzncT3YPcAGiKvAe1Culd7Gf-3x-olCfB06djWVNlKJ4g-GRnJYb6ZBvJeo3lskZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله موشکی دیروز حوثی ها به فرودگاه ریاض</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21025" target="_blank">📅 09:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21024">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=FTqO8DRy0-bf00LjddL0hPcdpYV49y79fz9T7k39T78GcCHGmDVRRay_It2Tebd0xfPvTwQg1EdQy7eMQYZGi5fpc2CoAtoLZEjeVKe0FyB0Ek5-Pe7T6lSotzQ7PsmTVbZR4oTDirohGKjOAXrKXiyVSn33aTGt3-16acLMqVWl33k8yfIowh-I8i7jALWfZP3_SyR8YaVUmgQAMKHkd4-HgfqrZ9QsNGpRxcn7HYIC4Sl0XTslR6Ce3PEmm9JPdMMqrjRkrn5pyk1wug_TBa37mQaCENjjs28PVr8b9b7-k-b4ckw_UnKL_3XQvmB-PCoFV0n3U-1hbkWTA-4nnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=FTqO8DRy0-bf00LjddL0hPcdpYV49y79fz9T7k39T78GcCHGmDVRRay_It2Tebd0xfPvTwQg1EdQy7eMQYZGi5fpc2CoAtoLZEjeVKe0FyB0Ek5-Pe7T6lSotzQ7PsmTVbZR4oTDirohGKjOAXrKXiyVSn33aTGt3-16acLMqVWl33k8yfIowh-I8i7jALWfZP3_SyR8YaVUmgQAMKHkd4-HgfqrZ9QsNGpRxcn7HYIC4Sl0XTslR6Ce3PEmm9JPdMMqrjRkrn5pyk1wug_TBa37mQaCENjjs28PVr8b9b7-k-b4ckw_UnKL_3XQvmB-PCoFV0n3U-1hbkWTA-4nnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/21024" target="_blank">📅 08:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21022">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ می‌گوید باسن ملانیا باعث «نجات» هر دوی آن‌ها در پله‌برقی مقر سازمان ملل شد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21022" target="_blank">📅 08:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21020">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وزارت خارجه آمریکا به تمام شهروندان آمریکایی اعلام کرد که سفر هایشان به خاورمیانه را فوراً لغو کنند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21020" target="_blank">📅 02:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21019">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">محسن رضایی:   محل تپه علی طاهر پیش از حمله تخلیه شده بود و عملیات دشمن شکست خورد</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21019" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21018">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.   به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21018" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21017">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.
به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21017" target="_blank">📅 00:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21016">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">موسسه مطالعات جنگ:
طبق اظهارات مقام‌های آمریکایی به Axios در ۱۵ سپتامبر، تعداد عبور روزانه کشتی‌ها از مسیر جنوبی، با انجام موفقیت‌آمیز عملیات نظارت و مین‌روبی آمریکا، به حدود
۴۰ درصد سطح پیش از جنگ
بازگشته است و عبور کشتی‌ها هم در طول روز و هم شب انجام می‌شود.
عربستان سعودی نیز بنا بر گزارش‌ها صادرات نفت خود را بار دیگر از مسیر تنگه هرمز منتقل کرده است. بر اساس اطلاعات منابع تجاری که رویترز در ۱۸ سپتامبر به آنها استناد کرده، عربستان برای بارگیری‌های ماه‌های سپتامبر و اکتبر حدود
۶۰ میلیون بشکه نفت
را در بندر رأس تنوره در شرق عربستان بارگیری کرده که انتقال کشتی به کشتی آن از طریق تنگه هرمز انجام شده است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21016" target="_blank">📅 00:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21015">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=TzjvWeA5mgiuKIFedo8sc0PKy4M79yUEPPhORmuQpEeSkmAJQeu-ROY1pS49AUp-Lzuzqki_OCMd-KJhIilBCDfTlpym8PAX24ZXIJm8kfcpjIrJ8xTsRCHfQn3qeVG-N4zcI9hgAZ5s7CiEETRfyT6u3jxYB67p-Hu5WrtiC7lRB2bZpJ60hzl9XBN_5RcmL2dCvpzYIP5xwJ4DWXBkkiR0ZBmfgKPanXuWN1aZXr4-oEKH5RzZPIXxRxXW-JkoJWP-cQ2Z2jIHr1zQErYamD0JXUeiIWfn_j9FH1S8wR7j39yTJJyCn2yTkGIWMDRrdLFxU3YCfoV5qRf0PDclqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=TzjvWeA5mgiuKIFedo8sc0PKy4M79yUEPPhORmuQpEeSkmAJQeu-ROY1pS49AUp-Lzuzqki_OCMd-KJhIilBCDfTlpym8PAX24ZXIJm8kfcpjIrJ8xTsRCHfQn3qeVG-N4zcI9hgAZ5s7CiEETRfyT6u3jxYB67p-Hu5WrtiC7lRB2bZpJ60hzl9XBN_5RcmL2dCvpzYIP5xwJ4DWXBkkiR0ZBmfgKPanXuWN1aZXr4-oEKH5RzZPIXxRxXW-JkoJWP-cQ2Z2jIHr1zQErYamD0JXUeiIWfn_j9FH1S8wR7j39yTJJyCn2yTkGIWMDRrdLFxU3YCfoV5qRf0PDclqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه ترکیه گفته که ترکیه می تواند نیازهای نظامی سعودی را برطرف کند!  یعنی در این شرایط که عربستان بشدت به نیروی نظامی نیاز دارد هم ترکیه دست از بازاریابی برای سلاح های ساخت خودش دست برنمیدارد!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21015" target="_blank">📅 00:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyQNOcxIuwZnTs9zNMQvKGT-d2vp_CiDnCJamJWAVHpg1sYSJktUGIRLKi8meVl2zYrCe25koNzQM6jq2N29njo6f8OB_eYBG2EB15MJKkjmsc5avrK-YisgPb2tTek_gJGicRMXJo3dzfwH3B5cyX5ToIm6K6gl04rzajK_AY1UcUn9iMf6jcov7xF0MxFvlGVXEGr-xO8SW6C9xpMYwN2_tiXPcDa3C38CHppOOkg3Yp9_Xgr5LwB-4OBkFbgg-HMjMeN_S-lZDTZRIF7Ief5lbjXjQfH0SeH7OadumBxYYaog8XZ4FnLpgnGSWqhHEKQnYZu9HAipdIZpZScaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:   این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21014" target="_blank">📅 00:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhA_qHm-r6DPaGlSpytJAXx7kjwVt4JmLu9Sc2-7SyYIdTPNNHw17qamTvgJq692M2ZP4DyilGkh9fqEPpBRTlYRLZXALAxzyVtcg2i_eSuNTs40-s1ztDZTM7_cKGc2k7dNdgEcaOZkn3U5y7hDFoyy8IJs5Eaikx16Ewved1I_wk9Z06-QHCzG1OoE6NMQhlD8Bux-z-TEW1c4Bd8EPEWiMZH59Gldci-ieMM-V--8Oowi997mCNXytfrzqd9njW1iVYHmlWe9U4xSiItSd5xvcFcyCZs5FjZBeS2mtOLqYR0iS2Cjdo-lNLtj1rZ93eaABo87lwqHm6Z8LSX7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21013" target="_blank">📅 00:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:
این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21012" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21011">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صداى انفجار در تنگه هرمز شنيده شد
گزارش‌ها حاکی از شلیک موشک‌های کروز ضد کشتی به سمت شناورهای متخلف در تنگه هرمز هستند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21011" target="_blank">📅 22:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21010">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">درباره دیدار مهم رهبران چین و آمریکا
دیدار دونالد ترامپ و شی جین‌پینگ در ۲۴ سپتامبر در واشنگتن، در ظاهر یک نشست دوجانبه میان دو اقتصاد بزرگ جهان است، اما دامنه پیامدهای آن بسیار فراتر از روابط تجاری آمریکا و چین خواهد بود. در شرایطی که جنگ ایران، بازار انرژی و رقابت فناوری بر اقتصاد جهانی سایه انداخته، این دیدار می‌تواند یکی از مهم‌ترین رویدادهای ژئوپلیتیکی پاییز باشد.
مهم‌ترین موضوع برای بازارها، احتمال تمدید آتش‌بس تجاری آمریکا و چین است؛ توافقی که در ۱۰ نوامبر منقضی می‌شود. مذاکرات مقدماتی اسکات بسنت و هی لیفنگ در نیویورک نیز نشان می‌دهد که دو طرف پیش از دیدار رهبران در حال تلاش برای حل اختلافات مربوط به تعرفه‌ها، مواد معدنی حیاتی و دسترسی به فناوری هستند.
اگر ترامپ و شی بتوانند حداقل یک چارچوب برای ادامه این آتش‌بس ارائه کنند، نخستین واکنش بازار می‌تواند کاهش ریسک تجاری باشد: سهام و دارایی‌های پرریسک حمایت می‌شوند، فشار بر زنجیره تأمین کاهش می‌یابد و بخشی از تقاضا برای دلار به‌عنوان دارایی امن می‌تواند تخلیه شود. در مقابل، شکست مذاکرات یا تهدید به بازگشت تعرفه‌ها می‌تواند مجدداً سناریوی جنگ تجاری، تورم وارداتی و اختلال در تجارت جهانی را فعال کند.
اما مواد معدنی کمیاب شاید از تعرفه‌ها نیز مهم‌تر باشند. چین همچنان اهرم بزرگی در زنجیره تأمین عناصر کمیاب و مواد حیاتی مورد استفاده در خودرو، نیمه‌رساناها، هوافضا و صنایع دفاعی دارد. آمریکا نیز در مقابل، محدودیت دسترسی چین به فناوری پیشرفته را در اختیار دارد. بنابراین این دیدار در واقع مذاکره‌ای بر سر «اهرم‌های استراتژیک» است، نه صرفاً تراز تجاری.
برای بازار طلا، نتیجه اهمیت ویژه‌ای دارد. کاهش تنش تجاری می‌تواند بخشی از صرفه ریسک ژئوپلیتیکی را کاهش دهد؛ اما اگر نشست به بن‌بست برسد، هم ریسک تجاری و هم تقاضای پناهگاه امن می‌تواند افزایش یابد. هم‌زمان باید نرخ‌های آمریکا را در نظر گرفت: اگر توافق تجاری باعث تقویت چشم‌انداز رشد آمریکا شود و بازدهی اوراق بالا بماند، اثر آن بر طلا الزاماً مثبت نخواهد بود.
ایران؛ مهم‌ترین بخش پنهان نشست
ایران احتمالاً یکی از موضوعات حساس مذاکرات خواهد بود. واشنگتن از چین انتظار دارد در فشار اقتصادی علیه تهران همکاری بیشتری داشته باشد، در حالی که چین همچنان بزرگ‌ترین خریدار نفت ایران است و روابط اقتصادی نزدیکی با تهران دارد. گزارش‌ها همچنین از تلاش آمریکا برای اعمال فشار بر شبکه‌های مالی مرتبط با تجارت ایران حکایت دارد، هرچند واشنگتن تاکنون بانک‌های چینی را در موج اخیر فشارهای خود به شکل گسترده هدف قرار نداده است.
برای ایران، اهمیت نشست در این است که چین می‌تواند بخشی از اثربخشی تحریم‌های آمریکا را خنثی یا تشدید کند. اگر پکن حاضر شود در زمینه نفت، شبکه‌های مالی یا دور زدن تحریم‌ها همکاری بیشتری با واشنگتن داشته باشد، فشار اقتصادی بر تهران افزایش خواهد یافت. اگر چین در مقابل، بر ادامه تجارت انرژی با ایران تأکید کند، یکی از مهم‌ترین کانال‌های فشار آمریکا محدودتر می‌شود. همچنین شایعاتی درباره کمک اطلاعاتی چین به ایران در راستای دقیق تر کردن هدفگیری موشکهای ایرانی منتشر شده که احتمال بحث طرفین در خصوص آن می رود.
از منظر بازار انرژی نیز موضوع حساس است. هرگونه توافق آمریکا و چین که به کاهش تنش‌های ژئوپلیتیکی منجر شود، می‌تواند از صرفه ریسک نفت بکاهد. اما اگر ایران در مرکز اختلافات آمریکا و چین قرار گیرد و هم‌زمان اختلال در جریان انرژی منطقه ادامه پیدا کند، نفت می‌تواند دوباره تحت تأثیر ریسک ژئوپلیتیکی قرار گیرد.
در نهایت، اهمیت واقعی دیدار ترامپ و شی شاید در یک «توافق بزرگ» نباشد؛ بلکه در این باشد که آیا دو طرف می‌توانند رقابت استراتژیک خود را مدیریت کنند بدون آنکه وارد مرحله جدیدی از جنگ تجاری و فناوری شوند. برای بازارها، همین تفاوت میان «مدیریت تنش» و «تشدید تنش» می‌تواند مسیر دلار، طلا، نفت، سهام و ارزهای آسیایی را در هفته‌های بعد تغییر دهد. برای ایران نیز سؤال اصلی این است که آیا تهران از رقابت آمریکا و چین فضای بیشتری برای مانور پیدا می‌کند، یا اینکه واشنگتن و پکن در نهایت بر سر اعمال فشار هماهنگ‌تر بر اقتصاد ایران به تفاهم می‌رسند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21010" target="_blank">📅 21:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21009">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ممکن است برویم یک نایت کلاب اما آنجا شربت بیدمشک سفارش بدهیم !</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21009" target="_blank">📅 21:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21008">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">محسن رضایی :
دکترین هسته‌ای ایران تغییر نکرده، اما خروج از NPT ممکن است</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21008" target="_blank">📅 21:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21007">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsytnCpbhYS8A6Yj8ROlj6bvVu8bHY2xMDeGd4HksRu1WtSwfVYpxonP0M9PilM_ICmVSED3RtycqGZS444X7urDTDGFeJ8B87bmiLELLW87GlEwoPoxg4-MI6vGUEC788SnLRImANc8bSNG6m9NzrsQU406idUZuO85W-X4cK-RyP3TmdnndxijVHd_2-aYPG-M7VD3j0X7aUUhz41xOt6f9qBtYXcF5hdEifWLzbMko4BigmT8vUHTOAA3N9mIwNTK-BNca-vObkuQXzCIKv3jv0BkUQiOmVwJQ0aUwwRGJgroDlmKcbvxX1M18lNvkgCisFzcP89bVbHhAv1lEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21007" target="_blank">📅 20:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21006">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21006" target="_blank">📅 20:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21005">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21005" target="_blank">📅 19:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21004">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو  با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.  این نابرابری،…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21004" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21003">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwPEF6DNmLZ_OlEVym9OBTzUkYRV6WKvU21SQuDZu4GAz1sevxXKsoeat9ojd3-GGLttwU9zIcAaLERzlbW_vYTpPVixCbcTc120O-ALL7rjdkIMyEDJPzIf_Z0ySrntFjUIBkFEBhe4ntnqhBQXXxUdQ3d8CReYt5NqbmQaGOg9vEWnWkFXcnvq08DxGyNy18M93FI_AEE-UDknZoVeXgBxRxSD47y__QBRTrAJDfSTYLGgIfUTlMkDf6sGcD78i9MYxpNMaS5A6GfI926-4We0kDjfcil-OOl_TtThJmlHlXvabzL1tV6qxNdilqWv5c6D5Li_ivkmHeXFKW6Q_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو
با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.
این نابرابری، چالش مهمی برای فدرال رزرو ایجاد می‌کند؛ زیرا رشد دارایی‌ها می‌تواند مصرف را تقویت کند، در حالی که افت بازار سهام می‌تواند همین اثر را معکوس کرده و به کاهش تقاضا منجر شود.
🔗
ادامه یادداشت از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21003" target="_blank">📅 19:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21002">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">محسن
رضایی
:
خواهان
پایان
جنگ
میان
عربستان
سعودی
و
یمن
هستیم
و
معتقدم
یمنی‌ها
نیز
خواهان
دستیابی
به
توافقی
با
عربستان
هستند</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21002" target="_blank">📅 19:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21001">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCo3eUD1z2MluzZM0Y-WJ9LnQbQzXnEJ5rffV4f7ALdkyCTWtsAOY5thMqL9Lm-CjPOZZ5cJ4npUwgymf2Se8BSoVGHQdd3g9jMYE_C9jff8c6oe53ji5JN22PfecLTFV74LfKSgpg7KzXS-u7nR6kBkaAi3pY-fhvjVCRktXLtcMjRQNUnCspNj51_HUiUflcXYYwUkjpBnF_RX5XWKAkqKKzD09ub02qW08bi06LyIWsZ7kSgk5QerJ4mMRvIm6teOGIMGvZj7jYE14vilA1a9GiZV_oES6I8TUSY47oxyyHs1KF3d1KWqFW8fbXxzSiwXwb3YWwkB5QTGqawd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت نتایج احتمالی انتخابات میان دوره ای پیش رو در آمریکا</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21001" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21000">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">WW3 is loading....</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21000" target="_blank">📅 16:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20999">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20999" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20998">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:   دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20998" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20997">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/20997" target="_blank">📅 14:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20996">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzj0E0I2FinZmOLYYC2vihz1mBntpBdZszS4MwJcPQEX2LP3LgaJ-T7ZAlb1wsUqLAJH6vjCSW1fkXt0C0cjYF1_iLu66XpwHrKg5G53AJC0yGzP8neQLcNCqscLPVhuAB1Tkl8g78_HEx17_vDIak72J1xQphlagVaX2FWXJ91G6PZiBVtGe9OFS84grPEvTrAdnRbvw2dVWnwnaaZV_T5IxYSUqswBsjxb1B1bLCQBMAV5v77YRU1jdeFrHyW4jKm4EYw3f01QGQAeiirkS6g2g9Hi3UZdejNP1UfYTCIVfYHRJKslyGU9gw_ZM5lg-7TqCxGnnT7kM4EjCYq_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش های موثق، ترکیه چندین پهپاد رزمی و شناسایی برای کمک به سعودی ها در جنگ یمن ارسال کرده که دستکم یک پهپاد کارایل توسط حوثی ها سرنگون شده است.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20996" target="_blank">📅 12:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20995">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترکیه مجوز فعالیت بانک ملت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SBoxxx/20995" target="_blank">📅 10:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20994">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آمریکا بسته دفاع هوایی ۲.۶۸ میلیارد دلاری برای اوکراین را تأیید کرد
وزارت خارجه آمریکا
فروش تجهیزات و پشتیبانی دفاع هوایی به ارزش
۲.۶۸ میلیارد دلار
به اوکراین را تأیید کرده است.
این بسته شامل
سیستم‌های دفاع هوایی برد بلند، پرتابگرهای متحرک، رادارهای ضد پهپاد، قطعات یدکی، نرم‌افزار و پشتیبانی فنی
است.
اوکراین هزینه خرید را از طریق
کمک‌های مالی اروپا
و
کمک‌های نظامی خارجی آمریکا (FMF) که قبلاً تخصیص یافته بود، تأمین خواهد کرد.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20994" target="_blank">📅 08:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20993">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حمله موشکی حوثی ها به ریاض پایتخت عربستان</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20993" target="_blank">📅 06:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20992">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">منابع خبر می‌دهند آمریکا و دانمارک به توافقی درباره گرینلند نزدیک می‌شوند.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/20992" target="_blank">📅 01:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20991">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">منابع خبر می‌دهند آمریکا و دانمارک به توافقی درباره گرینلند نزدیک می‌شوند.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20991" target="_blank">📅 00:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20990">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGuGR_XPcfYFjzHZvKhuJoin02zLRvynwi3KqgKbxnpQXyvxbmVRZSoMaplX-tb4zl66Gy6NLvZRMNunqpT_NlLU5D-ZxqgOpNXnoCShrQ8BJBlJON7mgX2P08Gug19j9V6uGqt_JAQ5VskH67sJyjFSpQYMYonjPkAuk7IkDkTf_1w3chnuDMawmK6ETro6gfyCPN2JQb5hQgj4xlfxzkwYVgDUbINO2UMtoDoF6G1dtcnBg35ITQsTlzTns_2fiakui_-HjQYaaxXtn8xBkqALqN_AI8WA0oZ4hJXGx5kToYfABfnpqGA86FlLEb-fv1ei2l8BdfuVIPpbOAtkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلامتی همه پورن استارهای وطن پرست!</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/20990" target="_blank">📅 00:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20989">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbWoQNi1moPqDtHjT5Q3qMi7Zfu-JAmb4eM8oTRReZYHubxdDIDL5Ay23PLRGtOizEraY5-QaFlDRrlyvlt7rx_XOZkqi2dOD63gANihS6U5IPOwA16RoJWAZ50MVuxQLJStVtzXzxbtI2QetO_6Tj6yt_8zMnL_dk72-1JJFBVSciNgIvkXVB8Y7m3VvMfPEhr6hLirGemOamz0EsWjLGTOv2bQH5POob1Bs6OZCBAAybOEowXM1sNGqahkp1bqQFnN8iSwKhhAHI1fy61Diu1OunbpBzwUocC_vaMDzSpgr5I7WaaDzdvAn9e1UqQKBpCNbESp7jjuDmYzO74z4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثی ها قشنگ دارند خاطرات کتاب های دینی راهنمایی و دبیرستان را برایمان زنده می کنند!  فکر کنید اگر این دوستان ما نبودند چطور یاد طائف، مکه، مدینه میفتادیم؟!  همه شان را زدند.  یا ذی الجلال و الاکرام</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20989" target="_blank">📅 00:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20988">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUFK_Qf51uAB2ERQXoFSgEqUGbM7lkO9gFujlUZufLHSTu1GGrURdmiKW5yz50bPb1Bq0ZPn5tcdwsc4EsyxkiYrIKpt4xnDv2To-53LMfZ3OL2LGUIslGPbttta8MWV-Tc-Oq3fh-V8yeeimlDiboctfJRGorwzOXUeAu_Dz-M7dcxrq-308p0SOebS6o_9CuyqCxoHTHdI-AfeI3QiL_gt72NwhlsNd1cPJ-icWA4CUw-OnHlsCNwFVnirp2eASHiDEoILevKG6lRDrr4SPbT453SEoTu9bEaKVjXga2tCxrewtzaMDykJ3S5aT8w3X3ay2YXVKVV9Yr2sjaJfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته‌ی شش مقام آمریکایی که با اطلاعات داخلی وزارت دفاع در مورد آمار تلفات آشنایی دارند، تعداد سربازان آمریکایی که در خاورمیانه و در جریان جنگ جاری با ایران جان خود را از دست داده‌اند، بیشتر از آن است که پنتاگون به طور علنی اعلام کرده است.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20988" target="_blank">📅 00:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20987">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حوثی ها قشنگ دارند خاطرات کتاب های دینی راهنمایی و دبیرستان را برایمان زنده می کنند!
فکر کنید اگر این دوستان ما نبودند چطور یاد طائف، مکه، مدینه میفتادیم؟!
همه شان را زدند.
یا ذی الجلال و الاکرام</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20987" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20986">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجار در طائف عربستان!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20986" target="_blank">📅 00:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20985">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20985" target="_blank">📅 23:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20984">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20984" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20983">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">العربیه:
وزیر کشور پاکستان طی ساعات آینده به تهران سفر خواهد کرد.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20983" target="_blank">📅 18:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20982">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران
انقلاب اسلامی ۴ موشک کروز ضدکشتی به سمت تنگه هرمز شلیک کرد</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20982" target="_blank">📅 18:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20981">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN6PR-wWPdBFITs5Fn-2aTv2HWAKbOEilotTDUBHxyFd4pjr0idAscUNsi16p9fNmV1svFuSWaaohb4AON4NsdoB5iKGSzV0Man_s0elKDTOQyLqu5gQuIKxVziacDqDeKzLUDLf2P6oPsPI4q2i6dbLRCwLBlhOSARKDL3P8_CoQGL0vpIpL4_ZzPEvkUze1UaoH86D3Hv7MGPmTBokhappth69pKVTKf4KVRVcKDzbuHoDWcvWhOE5J5n4p4q-RsocjP0JkNpLIegkIyrApKWPl9HSmXVVeMK-uiReHV5dF-WbTHTRD99qH5HDXGml_68907qP_a5QjRXT7k9KUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیه دکتر پزشکیان به جانفدایان:  کمتر مصرف کنید!  (پسر پزشکیان هم دیروز همین را گفته بود)</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20981" target="_blank">📅 15:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20980">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=AUQvOXT4qz5uFkXQETZLfqVW2DlE0hWZUY02hKA9-Egv-Cw_U34IhmXocXdSOvR_sMwyz5hvfXllnx1VNu8qBqx9HsBKr0kmgFmEqgY5lupSkJ_wPGtlftkqRhP5m7MM75_GSzd3GLXm9w1N5E3ooRxE9-gLHw8GBMqgUtDFPWtfkjXxqgdUaUvI6--SHSPI0mW4lYOmIa0iusqFwT4KcvQGN5PtnYefdiJ2yvd8oSwWIF2QOICoT3vYxknoAEN7zeTSffBa-oLp3ORmGjlCJW05RaGA4rGSBGctidi16OiIeeT_yTLrtHVwJkjL3B0E10R7dP74BUYR8tSufFrV9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=AUQvOXT4qz5uFkXQETZLfqVW2DlE0hWZUY02hKA9-Egv-Cw_U34IhmXocXdSOvR_sMwyz5hvfXllnx1VNu8qBqx9HsBKr0kmgFmEqgY5lupSkJ_wPGtlftkqRhP5m7MM75_GSzd3GLXm9w1N5E3ooRxE9-gLHw8GBMqgUtDFPWtfkjXxqgdUaUvI6--SHSPI0mW4lYOmIa0iusqFwT4KcvQGN5PtnYefdiJ2yvd8oSwWIF2QOICoT3vYxknoAEN7zeTSffBa-oLp3ORmGjlCJW05RaGA4rGSBGctidi16OiIeeT_yTLrtHVwJkjL3B0E10R7dP74BUYR8tSufFrV9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اروپایی بودن همین را فهمیده که یک لامپ را خاموش کند!  در حاکمیت قانون و مدیریت عقلانی و کرامت انسان هم اروپایی بشویم یا نه؟!</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20980" target="_blank">📅 15:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20979">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:  امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏   ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20979" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20977">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:
امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏
ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20977" target="_blank">📅 14:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20976">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یادداشت بسیار مهمی است و نکته اصلی اش این است:
جهش بهای نفت و افت قیمت اوراق قرضه به تنهایی موجب تسلیم شدن ترامپ برای پایان جنگ نشده و احتمالا هم نخواهدشد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20976" target="_blank">📅 14:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20975">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جی‌پی مورگان از تلاش برای پیش‌بینی پایان جنگ ایران و ترامپ دست کشید
جی‌پی مورگان اعلام کرده است که دیگر برای جنگ ایران یک
سناریوی پایه (Baseline Forecast)
ندارد؛ چراکه قیمت نفت، بازده اوراق خزانه‌داری آمریکا و قیمت سوخت از سطوحی عبور کرده‌اند که این بانک پیش‌تر انتظار داشت عبور از آنها واشنگتن را به سمت دستیابی به یک توافق پایدار سوق دهد.
عبور از خطوط قرمز اقتصادی، به خروج از جنگ منجر نشد
در آغاز جنگ، جی‌پی مورگان بر این فرض بود که افزایش فشار اقتصادی در نهایت دونالد ترامپ را به سمت توافقی برای بازگشایی تنگه هرمز سوق خواهد داد.
مهم‌ترین آستانه‌هایی که این بانک در نظر گرفته بود عبارت بودند از:
• نفت بالای
۱۰۰ دلار در هر بشکه
• بنزین در محدوده
۵ دلار در هر گالن
• بازده اوراق خزانه‌داری ۱۰ساله آمریکا بالای
۵ درصد
شش ماه بعد، چند مورد از این سطوح شکسته شده‌اند.
ناتاشا کانوا، رئیس استراتژی جهانی کالاهای جی‌پی مورگان، در یادداشتی در روز پنجشنبه گفت:
«شش ماه بعد، بسیاری از این خطوط عبور کرده‌اند، اما استراتژی خروج نه‌تنها روشن‌تر نشده، بلکه مبهم‌تر شده است.»
او افزود:
«برای نخستین بار از زمان آغاز درگیری ایران، ما دیگر دیدگاه پایه‌ای نداریم. واقعاً نمی‌دانیم پایان این جنگ را چگونه مدل‌سازی کنیم.»
هیچ نشانه روشنی از کاهش تنش وجود ندارد
جی‌پی مورگان معتقد است شواهد چندانی وجود ندارد که نشان دهد واشنگتن یا تهران در حال آماده شدن برای عقب‌نشینی هستند.
به گفته کانوا، هرچه درگیری به جای کوچک‌تر شدن، گسترده‌تر می‌شود، دفاع از این دیدگاه که اختلال در عرضه انرژی کوتاه‌مدت خواهد بود، دشوارتر شده است.
در همین حال، عربستان سعودی پس از آسیب دیدن خط لوله در پی یک حمله پهپادی که از عراق انجام شد، خط لوله
شرق–غرب
خود را متوقف کرده است.
همچنین شبه‌نظامیان حوثی همسو با ایران پیشروی‌هایی داشته‌اند که می‌تواند موقعیت آنها را در زمینه کنترل یا ایجاد اختلال در تردد نفتکش‌ها در بخش جنوبی دریای سرخ تقویت کند.
ترامپ نیز روز پنجشنبه به Axios گفت که در آستانه تصمیم دیگری درباره این موضوع قرار دارد که آیا عملیات نظامی گسترده علیه ایران را از سر بگیرد یا به سمت پایان دادن به جنگ حرکت کند.
ترامپ گفت:
«یک تصمیم بزرگ پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آنها [رژیم ایران] را نابود کنم یا نه؟ این یک تصمیم بزرگ است. هر اتفاقی ممکن است از سوی من رخ دهد.»
بازار نفت، کاهش بیشتر عرضه را قیمت‌گذاری می‌کند
جی‌پی مورگان ارزش منصفانه نفت برنت را حدود
۹۰ دلار در هر بشکه
برآورد می‌کند، اما شاخص بین‌المللی نفت اکنون نزدیک
۱۰۵ دلار
معامله می‌شود؛ در حالی که در اوایل این هفته به محدوده
۱۱۰ دلار
نزدیک شده بود.
این بانک محاسبه می‌کند که به ازای هر
یک میلیون بشکه در روز
کاهش عرضه نفت، حدود
۴ دلار
به قیمت قراردادهای آتی نفت اضافه می‌شود.
بر همین اساس، کانوا می‌گوید بازار در حال قیمت‌گذاری ریسک از دست رفتن حدود
۴ میلیون بشکه در روز عرضه اضافی
است؛ آن هم علاوه بر حدود
۱۰ میلیون بشکه در روز
عرضه‌ای که هم‌اکنون دچار اختلال شده است.
تصویر کلی بازار انرژی با حملات اوکراین به پالایشگاه‌های روسیه نیز پیچیده‌تر شده است؛ این در حالی است که ترامپ روز دوشنبه گفته بود کی‌یف و مسکو توافق کرده‌اند حملات به تأسیسات انرژی را متوقف کنند.
ذخایر نفت همچنان یک حائل ایجاد می‌کنند
مهم‌ترین عامل محدودکننده برای افزایش بیشتر قیمت نفت، حجم نفتی است که همچنان در ذخایر نگهداری می‌شود.
ذخایر تاکنون
۵۵۵ میلیون بشکه
کاهش یافته‌اند؛ رقمی که به‌مراتب کمتر از کاهش
۱.۶ میلیارد بشکه‌ای
است که تیم کالاهای جی‌پی مورگان در ابتدا پیش‌بینی کرده بود.
بنابراین بازار در برابر یک شوک طولانی‌مدت عرضه، نسبت به برآورد قبلی بانک، همچنان از
حاشیه امنیت بیشتری در ذخایر
برخوردار است.
کانوا در جمع‌بندی گفت:
«خلاصه اینکه، فعلاً هنوز به اندازه کافی ظرفیت ذخیره و عرضه پشتیبان وجود دارد که قیمت‌ها را مهار کند.»</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20975" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20974">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خلیل شیر غلامی، سفیر ایران در ارمنستان؛    «ایران رویکرد ویژه‌ای نسبت به مسئله تمامیت ارضی و حاکمیت ارمنستان دارد و این را یکی از مسائل حساس خود می‌داند. با توجه به اهمیت منطقه سیونیک به عنوان یک مرکز استراتژیک برای ارمنستان، به ویژه در زمینه حفظ ارتباط با…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20974" target="_blank">📅 11:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20973">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خلیل شیر غلامی، سفیر ایران در ارمنستان؛
«ایران رویکرد ویژه‌ای نسبت به مسئله تمامیت ارضی و حاکمیت ارمنستان دارد و این را یکی از مسائل حساس خود می‌داند. با توجه به اهمیت منطقه سیونیک به عنوان یک مرکز استراتژیک برای ارمنستان، به ویژه در زمینه حفظ ارتباط با ایران، هر پروژه‌ای، از جمله پروژه TRIPP یا هر طرح دیگری که تهدیدی برای ارمنستان یا روابط ایران و ارمنستان محسوب نشود، از نظر دیپلماتیک، مشکلی ایجاد نخواهد کرد. در اجرای هر پروژه‌ای، تمامیت ارضی و حاکمیت ارمنستان نباید به خطر بیفتد.
علاوه بر این، حضور آمریکایی‌ها در مرز ارمنستان و ایران نباید تهدیدی برای ایران باشد.
اگر این دو شرط محقق شوند و همچنین منافع ارمنستان در نظر گرفته شود، ایران مخالف اجرای پروژه TRIPP نخواهد بود.»</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20973" target="_blank">📅 11:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20972">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20972" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20971">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">طنز تاریخ در این است که پیمان دفاع مشترکی که عربها با ترک‌ها بسته اند دقیقا ۱۱۰ سال پس از جنگی روی داده که میان خودشان در قالب شورش «شریف حسین» ضد عثمانی ها درگرفت و اتفاقا نخستین شهری که عربها آزاد کردند همین «مکه» بود که نامش اکنون شده لقب پیمان دفاعی اخیر!…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20971" target="_blank">📅 11:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20970">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RistPgfgJKJerrU3p3z6ntcGjxYqd5R9pP6vEnLud1KW38KClU5nDZ56h9x1F_Zadqe1Zeaz-QQuKZyk4oA4YKyIj8PYGLLW0zs6Sx1ZT6_fluxmMezKGtr6JKH7s9ciUBxVksE8cMSZahOO0bL8WrUBA4K0MA4LNfzTP4AVyaWkVLQCzX56v8VxD2uyxHjbERxCaL5aD2ILvCLn0MArg1uJY-XSISF5sLadL8k3MN-20kTQdRiXfu736oVa3-UiGHZPKyP9cS5Zt7LIWByJP_En7gK899HRL1Mitkk10ceSXyjldAe-P7TnIVpvTMcqet1cM_07_PLupWn5Qt_XHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.
پس بهترین استراتژی برای امروز:
خرید پس از یک اصلاح سنگین 400 پیپی است.
محدوده های پیشنهادی:
4366
4355</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20970" target="_blank">📅 10:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20968">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRtLEv7VROn1vVjEjU0wMCAa2zZHGcc0Knzpg5Pn-6dvoi9KsA_6fUmqB0ziprCq8uFQGHmth95ixluft0Ae8qv1HLoNinNjx35AR_Gy3NZgzgNf_5FSK7MbRI5z6FiA3leusry_F3B00DDwghNqhLL95wSW9HLFRNnCrVm8SlmHRYFI5164G1rPKwVVQXuR_HtoA59TYNvH5VG5X_RUaQk_k79hsPardvsIJbJiyAsbDdFerdvQVNXXdlajgUdtywo9QLVWUQss_wVY2Z2JvIgG5UXHyO4ztiUE7OswXWpMrNsWWOYSFwBFnF9m1w9YptfLOoMLkdynwef-WIhUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد و انتظار یک اصلاح نزولی قابل توجه (دستکم 400 پیپی) در طلا داریم.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20968" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20967">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر دانشگاه تهرانی ها</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1dc786c4.mp4?token=AbbvkKAJbvWPa9oOCrF1tCKLZhS2Yy43E5KC7oxx01vlToBouYS9BYWNRoSH1_6cKhrv3RKkBxNAFnDSipv_zYfgwZQpSNeerbXf5w6PM8n28AanKhvinMKVDofZBKbYXKRbPhUGdqz4p72zWe4yVRHxB_KL7H7f1LO37Kv6fFCFgsx11uAQMQAx4LHtQ0iFik_p-DZYw0ufl2QgjiVQTvgWeLR7kagpcSXJ-auo0zi1Z0XMBBofbNG4erJoEhKrB7Gp8sblnHWLKWZSO6BQ4-2TzWvH_OR7EE0Cgld9J_5PTGboEIVd0XCai7x4g5UeEpqpsX5ANiSxN6QrvVYOyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1dc786c4.mp4?token=AbbvkKAJbvWPa9oOCrF1tCKLZhS2Yy43E5KC7oxx01vlToBouYS9BYWNRoSH1_6cKhrv3RKkBxNAFnDSipv_zYfgwZQpSNeerbXf5w6PM8n28AanKhvinMKVDofZBKbYXKRbPhUGdqz4p72zWe4yVRHxB_KL7H7f1LO37Kv6fFCFgsx11uAQMQAx4LHtQ0iFik_p-DZYw0ufl2QgjiVQTvgWeLR7kagpcSXJ-auo0zi1Z0XMBBofbNG4erJoEhKrB7Gp8sblnHWLKWZSO6BQ4-2TzWvH_OR7EE0Cgld9J_5PTGboEIVd0XCai7x4g5UeEpqpsX5ANiSxN6QrvVYOyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهریار میگه آدمهای پیشه‌وری بچه‌های گرسنه تبریز رو جمع میکردن و می‌گفتن: « بچه‌ها بگید خدایا نان بده». نان نمی‌آمد، سپس می‌گفتند «بچه‌ها بگید
#استالین
نان بده» و نان می‌آمد.
اینها علاوه بر بی‌وطنی چقدر کثیف و کودک‌آزار بودند که با روح و روان بچه‌های گرسنه آذربایجان بازی می‌کردند
_sheshgalani_
@uttweet</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20967" target="_blank">📅 09:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20966">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خریداران جهانی سوخت روسیه در برابر لایحه تحریم‌های ایالات متحده مقاومت می‌کنند
پولیتیکو گزارش می‌دهد که واکنش جهانی به لایحه تحریم‌های روسیه که به تازگی توسط کنگره تصویب شده، سریع و شدید بوده است:
مسکو هشدار داد که این لایحه تنها جنگ علیه اوکراین را طولانی‌تر خواهد کرد. هند قول داد از منافع خود دفاع کند و پکن در برابر آنچه آن را «حاکمیت گسترده غیرقانونی» نامید، مقاومت کرد.
این لایحه که هنوز به امضای ترامپ نیاز دارد، تحریم‌هایی علیه رهبری روسیه، بخش انرژی، صنعت دفاعی و شبکه حمل‌ونقل که سوخت‌های تحریمی روسیه را جابه‌جا می‌کند، الزامی می‌سازد. این لایحه همچنین به ترامپ اختیار می‌دهد تا تعرفه‌های ۱۰۰ درصدی بر ۵ خریدار بزرگ جهانی این سوخت تحمیل کند؛ بندی که از پیش متحدان خود واشنگتن را نگران کرده است.
از سال ۲۰۲۲، چین ۵۰ درصد از صادرات نفت روسیه را خریداری کرده، هند ۳۷ درصد، ترکیه ۵ درصد و اتحادیه اروپا ۵ درصد. اتحادیه اروپا همچنین در آن دوره بزرگ‌ترین خریدار LNG روسیه (۴۹ درصد) و بزرگ‌ترین خریدار گاز لوله‌کشی روسیه (۳۲ درصد) بوده است.
از سوی اتحادیه اروپا، منتقدان لایحه استدلال می‌کنند که این لایحه اختیارات بسیار زیادی به ترامپ می‌دهد؛ یا برای ایجاد استثناها و معافیت ها برای شرکای بزرگ روسیه مانند چین که واشنگتن به دنبال گسترش تجارت با آن است، یا برعکس، برای اجرای انتقامی علیه متحدان ایالات متحده که ترامپ از آن‌ها خوشش نمی‌آید، مانند اتحادیه اروپا، با استفاده از خریدهای نفت و گاز کشورهای عضو تکیه‌گاه (اسلواکی، مجارستان) بهانه می سازد.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20966" target="_blank">📅 09:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20965">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به گزارش برنا، در نخستین ساعات بامداد جمعه ۲۷ شهریور در محدوده خیابان دانشگاه زاهدان تیراندازی رخ داد که این خبرگزاری دولتی آن را «حمله به یک ایست بازرسی» توصیف کرد. برنا اعلام کرد در جریان این تیراندازی یک مامور نیروی انتظامی کشته شده است.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20965" target="_blank">📅 08:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20964">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
نیروهای مسلح ایران به آمریکا درسی خواهند داد که هرگز فراموش نخواهد کرد</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20964" target="_blank">📅 01:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20963">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حمله ایران به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20963" target="_blank">📅 23:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20962">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک کشتی ترکیه‌ ساحل اوکراین توسط پهپاد مورد حمله قرار گرفت.
بر اساس اطلاعات اولیه، کاپیتان و یک ملوان کشتی در این حمله کشته شدند و ۱۳ نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20962" target="_blank">📅 22:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ساعتی قبل وزارت خارجه آمریکا قصد دولتش برای فروش ۴۸ فروند جنگنده F-35A به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را به کنگره این کشور اعلام کرد.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20961" target="_blank">📅 21:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ:   من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20960" target="_blank">📅 21:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:  طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20959" target="_blank">📅 21:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:
طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20958" target="_blank">📅 21:28 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
