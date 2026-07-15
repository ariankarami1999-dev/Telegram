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
<img src="https://cdn4.telesco.pe/file/dxqpSRbA1xS9BN8Q3JEwY6Nu9W1COBz_7JWtds_bJfEuHltUyOkbrHLi6ruPanWHZ8_i-UAFJi3KXWPpjhdJIHe2WS3FCtIj3nni1a5owFUQ-SLyfCd5HMPJOOor08fN-RDCXd6shx35kLi4XE2iCkQOstc1r0fU5AlWqkDylXlsPqI5UycDO6Nwjl4EFRw6nt2xAT1R8hV12bL2zcH7A_Gd87ujpXeqNUjojUd7uZsUOF5nWnVTmrACUtPfFEKRhpt_Pj1Jyc2pXyJaf1B37WeyZXDB6RUsuibDvNBT_ZFuB81CpoQSxZxRS5cUC-UaQkqWlMGhMXeQt9YmgjxSAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 462K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 16:18:20</div>
<hr>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr-c7cKrdsUY7C3G3wLByU264hwpgUXB5uRiaPb_ADSK-13RVet6xZM7LgbYRAz5FWTFyQ5we6k7DjXjrus88uFeK0Z9AKnRNsG9tP_YUoMhvXHt44SU6LX27b23tGIYJDfE3YDHs45e6cakCsRltgNSenwZ-dbNXCjTijlwVxc9DA8fgr9u1W4J6BqJLdDHErIIfGGOmBoy0T2w3_nBKNBlI5-0oO5uGF77Ykmp2EHUFE_WiwZxsh-_1jOFVqNGe-vV5ALfLyowxNE6xfM76ovInvAPCocqVXlDyNb8ZLqYuILlbzjEdCYcagQ_J3Q07MKQiUwdeQ7LkDz_VWB8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSxiDmUU14fzexx7FJwsNap48J9S23ExhiDuC7JLephYrW827OLRalK6GHxVSp4REtiegJIaEDjgrfchVZWwhsrmTzEvZeMOl0nwXAVksJAwzrPON0N6rG5LxW3kGz3H_LQlVtdCPH3OeaIC5lsD8Ly6DFddpUirh0ChUYBtKgrTVgmRSHoy9bc0v-gqxPmustoZYsvGuS2BL8y_h5795z81jLSHh_laxsIb3CtJeZ-ENDCc4k7aQzeX-0wGbnedKd0iB881LHoUtejakRh9FIh-vYzOCTf0wBan18Rq5qSA6Tplr3L1wny7Zaiy0TX95i-wIQgPbsCE8G4ubQPwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZX430xGFZSQM1ClqUkJGiWafk8rF1Rh4msCIaApAmWIL8mPcd6YYcmwOX8j0Qjyu_6Oiv11Gf6BP0AosnV4c9U73Zze8HZY3IdEa95K2bwcWnzhItrB_uAiWNcb-fDhX19WpdrVBkF714_hfOUpsCKsVDKf8JUJWhKxeQpHCRsGFq1aCRqhRBrkFkEGY8IvnInvnpwQw2e8Uw7OHwwHd-_YI3XXTbgngR5qUSghHvsoF_EGhtokldio90qYdDqp-wGZ-FdJUtgvuM765vgAEnZLrI8NUHnobBQA00gkz5Crg8bagkuizcwP9PVqiGH91hUvT53m0_OLfCALqo-E9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=Hl6-juvjffctWNH7QyHCoEilvcEV4ej8OmSbVGcavZcgNSnRwf-wqqx7gS7F_aqdLdOGmyniLy9DkWDR2bACj3Z-EwUqB2tG3rBDRTzYj76rDMs2Mt9jAaLbODq3TN5APqqQIoIpQByETdtkiXDLzC7Q29VKPLYFf2qVQ7fSn-NdVAav3FJ3ix5h57zl_JBh_Tlbhl5b1bS-brzjAB7_M0AHKXCVSquzl6LcQjv0dCBmLKev37qIPoc5YE7ikrAXqiHuFzSfT4e2RXjfrVGEUXT6jNDHelvtbBB0QBOr_kebzrZGkoIPm4IM4gH1ZxEs1Kbo_RwzK2k9sdBp_H99mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=Hl6-juvjffctWNH7QyHCoEilvcEV4ej8OmSbVGcavZcgNSnRwf-wqqx7gS7F_aqdLdOGmyniLy9DkWDR2bACj3Z-EwUqB2tG3rBDRTzYj76rDMs2Mt9jAaLbODq3TN5APqqQIoIpQByETdtkiXDLzC7Q29VKPLYFf2qVQ7fSn-NdVAav3FJ3ix5h57zl_JBh_Tlbhl5b1bS-brzjAB7_M0AHKXCVSquzl6LcQjv0dCBmLKev37qIPoc5YE7ikrAXqiHuFzSfT4e2RXjfrVGEUXT6jNDHelvtbBB0QBOr_kebzrZGkoIPm4IM4gH1ZxEs1Kbo_RwzK2k9sdBp_H99mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHqCBlN9Ph6eH5GT-SSLesqecRC3UittkxMKQn_NN5XScE66zhfPzSm9wgknrVtA7uHVPspd-cnXfv-EeSRUQS3-lthjrjL47-QCivSQh_SUiloTQCWesU5Es3nCqOK41eA4pMBWv086MYCYMWm8zUP1o5qI4QEESrUETcUicEaGkKeP9q_IfjbjsZSoNoDawdt-_U6rqrJaBzGr6OH3Y8Vx3Ab4tMpK4UHYa6uTvI_5PuB6lEKz_p5jWoCFULoRGwTcxi7mG9sn0qkNyGoShp9a97YZSbk6b0NJDloToO0CNnHPGWUFM3RWC7YbseaghgBqBwjfZ1mVsrM0lDexOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOGMS-zZCvpBQu49hqVFchL9Uaww5gd-7lBmAINn1E1faM7XJDizyyEJ0EFcWFAez-SqKfiIhHQoAwvBuIU7KJV9M2sbsM2iC7CrLTxpWtMBw3STz5XwVu9bywOtfJ9WBfBtL6G_6U1YdrvnMNJdZsWTrdCIA3TIF_t4jH1b_yytwMcuIO0QaGcQ8Eu8HFbMN3lQcxnO4xF9TgOfDvN-TVX7nlYXmxbELHZSOcMn4rNxDcYRQnE_ZO6MqQd5aNIiZ71XgqAmCAX3uhLtH-CD0ZgrSo6fjw0qizwBc2L-gxfqY3KiJU14Cmj7fHEbUul6FlG430z4Yjqc7kmZ5qKWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ec4JG9GNJ1s5-iXnjJfDioI0fANMJUPiaxEHDA-nmo2iUdFHhdOC6H7M64utl60olRcFu5Q6ggPfHtdvEriTwZ30cComM8Y1UVlTl4wfqj_SeuEwc0M2PsjsB_6BY2hg5-c4oxDxQdYDn8xe6hIfyjeJP6zddpottWhnhgecvfX0h3QzyIW2IIf85rCEmnhqARS74vPPoF4Sj8wCzSw_Det8z4lzjk8OUB4xIjH9oi9PEhkL0n3Q-z7OtVfIpgShbZwoNptMiUBc__08n2cPbcbLg_HxwyKiM70OdutQ3AvoW-_Bgl1f6vBH0l5zfev2lMIVrjiV0AzKQ3dhEzqakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYCCDeCYFyYFSdXBIuZJJq6iNjHNI6c_SPU0uBITIVIJmAv4wyngsrHsP_bJcJAlwI5DomkqYORiOc2W6SawKeCJvvOdcoqO_wTsR--bKfYOiSJf1_pEgggzBqeR_SnpGUu9KeI9RiG21bXt2ljw3dPDJ6I1t9O78c3N6ZxrmuPxydUxQfUXd1X2v3y7KCF-X2U7TWvtq9PPfAL0sixy4FMfIRQRwW1p4MlI2z90AytTXhWHQykdvTPwP12EWqrq0vZW_sWn4ZpSlMlfG20OogO5MJMMt9lX_m8tfn6e5n3AvJnyOXE8Q_WsU_alXTbi-7jtS2HOXIrD2vzFOs-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKv05iRbg_w5qmDgUGZT-U9QsY1kIcHKl4V6bhbevT_rm0jOOOD-1IKAUt0khezXhVJMwBrRC-DAwBmvYnK8CDltc0Mee5uF3hMUgRe6jvvCFVKywIM6RYtdhHJVeMqNIfSsj5w0ILYnDTmT82QZH-2N80__8Ou3YCwtRCK0Tlxcx85CpIbrmgqFN61tykSd633LRtkLfLS0BgVg0mhLAASdn3uNhxGzoJgNx21lp9bU-Mg7BxZdNfjVTzth4EByGXLh2pPCtHq51WSmWkEScdyUxWQ-iNc5yw1eSA2jCucJgA1L3GiPEPxY2X94l6yhwOyuqvixkMmy6UpaBpwXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRP5ammiu8y8AcNi2fu15ogD9zUs8kT9t8DbieNsB7DphgoqkbL6jebcKhDn6CPEyV4zMraZk2Erg9LVygaMaOxcCYGrFDNkAtUiVV6oN7tb-hcabQIfsEBFQi7wLnhD11D_1gA0LwbvyvlVtZsY8fOZzXYPzUlcHmxQEV9L_rZXyP5tzd4RwCsglSEKl_vZAqcreUQQfNFDB1o7kqDpobefPj89vANRAP7hmr_EoXzzCCxLOb8awR9qwr0M6-9XWsOOkiUvqNjdqJmtsogOr-iLhF2ZDxxeNApBGqRlCG1y_xVyB9Pa30kYK3lSbJSixBS3YSFD_vMRp7V82T8fOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGWRl7JGFqhG07MHgWG-Oh-Zbm6R1qv07dVgmQyl7vEHG4sMrPCQxt-Rc-hMPH1AmbOyvLRFKqTkEztfevQvl23EHB1LnW9b68iER_mNV8ieDlOuyTs6ADnZl_UsBDAw-lO3be9k2yz6AuVoLDwcNBSHjtKuw-zOJeJPHewCB8mPGuk8QMK-PrClpa9xGyQe8o4FXXJkRHaUcn0CkrBatWX4ftoxzx3KfkL-kdVsE8R2WYdsOoiisoBOBfJPsaMXOZc5KR3fv6ZHw0TiyjOa2biR1PC1yYm2OqkLsvdIbWvawJMYEXV5810UrLA7BPVXSyQRe6kwFuoE3dp9f29BWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwp-az-yU5-SQJe3gezLMywvBxvkqLEP-Zqcar38tP1tQiq5HDemCpC8YFearJw52Eku-4CbmRbU_aMa-vGoZeTMl8eXZ9gw6ivXB69Nwbv0Okik_hXUjRn8erFLcM641xWKX5NNdKBpgj1J9g2JwfLbctkRzPmWGYhYIjv7uQFmSgssXTJNuRJ7eq8Vf4n6ne10BCpekl61bAuP_P-aWKxcrD90l8tggVgq1uWQtOY2-F-Ub2I0GAZe2lOk64x0Afox9hdiDjzwCqBOTjcL7uMLRGPT9HghLZ0HS39T5dO2dPws8VTWEd-5MaqhhY8TGyrscPelH4W8Zgloll_l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap6J8Z8v22e68jgA8K_d2vFmKLN07YlB1w0VXSHUev8Aw2N3-ORX2j5_LcKSZmdeRs6WRCUKb-0Colq79JfmIsnqIUZlepDdZfJ5N0rryPxFYhfRXWgi1AM27giqMObJjOSUo1QrXnKtSOuSFYFbH3rZNBjwsm0lgxE_ZVaheI2BJ4e5LfjnpvM_4giBGITlljUWpJ79B-b5_RouC17xO2kqMrcpL8zcMVyiVQdKMdUFWejvzI8c7kNhVvwBrd3zPeL7Bod6KZXsfkttybr9Fe-Nc8qD5VuNrp9ighBhPgchnPj_kJXSTc7LZvJGRbUOjU0zQMfMDgFy6HVt5EoC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=PyaRouDJ0YmB-WfDKA1nCU-WhaZOSEu_rGlPSyw3q1zVUTcnEpSRcJAXb4H9royvOR9EyjEMF52wq2oWUlkHnXMCKv3MK4AM3Xy9tiIcJW4kw0cGCy_gmRm_pHM9TIA2dk_ZFNJskUnULFyMjm7OwyBvKcbjgwCsnrBlemRFuv8pUzEYZ3PYw_Vx6luyUST_u4XP9jlesFJpVBjnjE0CGGUR2r2fH7RrH6UfKUsyZ22vtVCdi5sdJFJTuhMjul56HP1HIMhcRKJ3kBLEdxhoijeQ7e1a8tRcF6nRM6V9QJpfa5BGVAXgKI7f8qsDoncdSMEz7T6wOZTWiic__eEm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=PyaRouDJ0YmB-WfDKA1nCU-WhaZOSEu_rGlPSyw3q1zVUTcnEpSRcJAXb4H9royvOR9EyjEMF52wq2oWUlkHnXMCKv3MK4AM3Xy9tiIcJW4kw0cGCy_gmRm_pHM9TIA2dk_ZFNJskUnULFyMjm7OwyBvKcbjgwCsnrBlemRFuv8pUzEYZ3PYw_Vx6luyUST_u4XP9jlesFJpVBjnjE0CGGUR2r2fH7RrH6UfKUsyZ22vtVCdi5sdJFJTuhMjul56HP1HIMhcRKJ3kBLEdxhoijeQ7e1a8tRcF6nRM6V9QJpfa5BGVAXgKI7f8qsDoncdSMEz7T6wOZTWiic__eEm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtWOdb-g1lc07xnC2M2hSLsZdBb2P5_9Gbg0qAdWpYKr2rksaYYCGl7H5tBDjASi2SDNLt2-8gNXbZKvX_6sw52DE7oMwn1-xJ3lP9hd0jSoET4KC8HCA_IE5-UwLy5ri9dQGplXH-iL8fYTYzyPy8EeTqtEBOWoGoCXJmsge3io-3Jw7T1PjaFbP0zpg7ahtZS7U6Uq4eXSfJPX2MEQGrL1SducwqRbcOEE7Iac7-o-95d_wQhdpbzz1JRDiUkHu0pPO7hWaCPpv7jbC0xoMatInuqKosMjrre3RN6OJIkgtRULgZt2nX0Cl21KNbAgj7SesakTwCpPx1iT08XkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB3qC-glbsoN8z-7G8g5SYBZ5DDYk8pO28AmSyIxZDI9i0rRmtoMdHIhWO0B-I8bn27jlKMo2frw6U41ZW6b8XL0Jz7v6GG-ACQIL0vNiq_l3slKzJA9EVo3x-US-YUzJByhzBsM3i-SKTAhWicuqnr-xsPY_3__PcpTtkcVWlauFH48FsicbYAtyz06iSNrGqm0yXt8tBx0C1O8rdiGOfFeEujyS-2jeOLmNsDvAyz6NbFLm7CPAA7SCEeV_yKuj5hOXCVMXGet2CmsCfpZ854RoGSu_3jKknArk2wRikwHo8ldPQ1ptheiYgBj92_-0zFEBNrzYttD7NYZWRsSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWnRT52FHCZKEA9s5TT-JY46PKw3-fXgxyOT0Ag82-_Ovhq-mo466VMzp-E3OwYcEcUogzETOfLH0T44MoobTVeJPyrHWLcnrygd4uQD6hVQ456NG2iio_gW1RVef496T7JpCjUksztdeVlhQbejSvykOyjqKGH6qPODODqXzaQHuAFkZuLS6cglU24nvoX63HqZeG2iRGVwyEcv2tnk9v6k6VtpVtjGrak4a4_2EINsqHcBfMBO0gre4ES9QtdXlkCDxqSgWXV0xxKhvp4EV3ff3itTesiMp1wLfnajxOmS6aN4YfNkF6sffxAFTh-0IWvF7vLjRDM3egLMt07QFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0ReULuo-p7yL1I9Rh-kcePaX4qgkwrbH_gOmKouwJnjaOL59f5vBoK5QPJBWyiRsa14MxxYjfqtvaSHGhpWNsF9ZqHAeb60t_qKPtU6x-Zde3eAZ_JqEj70v1yQTyI6EQ7aYjNY5EWZBEQwXtvN9AWfH3UFZy4s4p_fb1MVS-X2gksaRb_IsyKYYK5ZqXplIUOHxx47L2goCayhb8801LZOssbP2CjqjtAeweAurcos2xCq9EY_aiRrQy_NdCoLFvYbnD2yTozaNtgXJ-vhiKzOT84P7brV5ExntjslXjzelddfNwtgRbyqSISn7MVvjRqq0czVEAeUIqk7DHhftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyaNw6Y6nqRFN_Oajqw3NT5UdYXVNtRFrVkacvfg90C7zCjijwK8nLgEUjbCDVOpIwiup30mPtQwCwYWLOo33FTeOl3bvLS9zG4mVQUy2CuAR4ukXSZywFaLmFFGgKubxNBGxIqUqS_lMi08zjidR2y3kodQENVd2JqvenQx0LHjRVeDPpEmDQutMI1dMWojDGoUIhOjW9xw4oq1SLU8c4OP7krbn5nBW8YOBsNDfrM_CGyo7WWJwZoFvqt7qzGC7hiP0dGJTyE1vyhNqHFHucce0asKfERHxUxKzguku6GgOmcA-kcAMbh8zbNWLqkxtzk1r9gwhtelCb9KaXFFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=FAzRtR36fE-MXtMTQaxpKvdt0ZIeXK_SoouHeNYPzdOvKtabN0Ps7geE0XEGLg3YwkiHlPemCrxsg0UDJ8PXkSjLTv8G2sdk-PRgZ2l_73xw6z7nRnrjskLjIDcfM1ms56161Cz7bclV3zJ17rg9_L5hjHkPfxRot3wq6hrEr_NeVMGc5sV3f3YXPOLqyBJq3JAvAtB6SR-RkSxFF4HnxtlIowW0ueJ2DFSC2jeZrnIf2kxCOVyjN7CLS6HWKWtoPq5HVwhru-omnilY7UwinVu94OrZiTmtl9pRQhyq5jV9O_UtFWtDaV7JCIF4RkAuC71F5FdxLNqQAWJjuXZ2pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=FAzRtR36fE-MXtMTQaxpKvdt0ZIeXK_SoouHeNYPzdOvKtabN0Ps7geE0XEGLg3YwkiHlPemCrxsg0UDJ8PXkSjLTv8G2sdk-PRgZ2l_73xw6z7nRnrjskLjIDcfM1ms56161Cz7bclV3zJ17rg9_L5hjHkPfxRot3wq6hrEr_NeVMGc5sV3f3YXPOLqyBJq3JAvAtB6SR-RkSxFF4HnxtlIowW0ueJ2DFSC2jeZrnIf2kxCOVyjN7CLS6HWKWtoPq5HVwhru-omnilY7UwinVu94OrZiTmtl9pRQhyq5jV9O_UtFWtDaV7JCIF4RkAuC71F5FdxLNqQAWJjuXZ2pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuF6wy77hm5XO5qkBs8D0PgnericKY7Rfe6ulxDp2ulIxRFz6O5z5Vjg8pU8t8x42szhOV1DImlbraccZOcV52-JAm14Fxc0C1wEH1-5CjwXn2v7sqTk0SrNf2ueNJXt_FeZUbH9qvB3ZLAenn80pxhX_a34sxI7dQyAAosIDz5DtHS7Mob1WSYFhNTfEY6nLF8bEjBvZ3AmT_mW7pSMGQKN0VloYzv--Vv_3ItguEJTrom2AGqub0d-kGfDeCYaFSnYQEXnBTpM-SYPdh4NWfkcl0NO5eyCipGSb9e2Y7T9oOQW0Pp3CUvsN64ad2rxjdhxhX_o_AlQNhxbY-RjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJkRoIheXulO6d-j8NogDmAioConPDtxgojKSJGNNK1Psa3gHCr7aMUZM1M3Mploxs0TSvPA2PiuTjdQH2u_m7aeYDgH14Gs0gjR5lLG2DVwxNjiUGJACoCsM2V27GDhMAJTI4MuutrEw_Byx3IUnZ7GSbm_DJDh6u7Oe4U7RrAuBAyjnyHJ9YVPgRSiOWzJfzDuRgcWHTkZgwmm0nJNmH9WJhnRBgmu8oD3CZOwF9Ull_FGnZfwbEDGJBQ4K6CdiCH3HoDN8fjEeOCAEAwrTb0Cm9otdFdQVCoXOY-g9tTTzOv18jO1csovts3RLz-2TAl1enlSbpKZq_0IdWZmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=iyV13s67lvwqfTssR5DDw5ekyrJMQARUbB91y1OziNc_O-K8DkpQF1c8AJ9DXlVOwr8slZbR4a_zmvx8p2ujBEl55TiiCAUL4VK2ye94hC8uBtN5pJb1T5DYThfaW9sndh0uozWBb65WW_9vi5DlUAotElfSIESeTMPk2THWz6b1_UgP2i9gTf-_mHGY9GFi445YlePpRyMs-zI5XOIOOdr83lrMMtFC5wk4bc5WFqKuyQbHG0aOkUVIlRr3ZA1CHBM_Xn-wMQxV9WluUrEIsEHwRVsbqk_-ZJcSoVayOnPf9PR11jCfw7LnjVWGoc54n4HhoZYHnojLzetHLR0H4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=iyV13s67lvwqfTssR5DDw5ekyrJMQARUbB91y1OziNc_O-K8DkpQF1c8AJ9DXlVOwr8slZbR4a_zmvx8p2ujBEl55TiiCAUL4VK2ye94hC8uBtN5pJb1T5DYThfaW9sndh0uozWBb65WW_9vi5DlUAotElfSIESeTMPk2THWz6b1_UgP2i9gTf-_mHGY9GFi445YlePpRyMs-zI5XOIOOdr83lrMMtFC5wk4bc5WFqKuyQbHG0aOkUVIlRr3ZA1CHBM_Xn-wMQxV9WluUrEIsEHwRVsbqk_-ZJcSoVayOnPf9PR11jCfw7LnjVWGoc54n4HhoZYHnojLzetHLR0H4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PI1tdyKYEXqznEynSe2ACHsdTOEqD3rmzxl2JC7woqUWcIPPNNfL1iY4BR67dOB_DVAbv564Z2HnGw8mD5cRiM557B0Ee69j3ee17kZGB8ttaFYJ5z1BQ2H02_hKfMTkiaVrTmvYgpNwnJ3xmfYJpCwLdSm-Npi9V0uj0jYEkwLsX-82TvO8-T9QzWCJ7-M5mx01St68hAQm5KtWH0n0TEFeTfX3N2wtrjTJVx_jKuTb0HGKHBTrI3NzHKKZnD3CQiQXs7iKDCwXaCpJv3yuXA8tQ3l9TO2QT7Z29hR8BSqYQREUmEn6ZNQcmuIXrgOqsy5melbQdY5BDfj-AqY_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=U8tIxudn9CxV-LRceLzgiVmb4HcRqEEZVYP2poh0sPPxFNd-wUZpFxnbQrdsKPOKID10EhetkE7parhQ5OgjoAl9eLdeR8eUYklhWJeseR5qvL7YIOh4Y0S2hosOm7zmlf00e_T5bAtdT6ypARjAvbROX0njx1sEfJUZCwgOfQw32DNM7THXjntJg5vJgUdn3rY_WHR6l_3LyI17Tt_DNV0VDrl6xcdwll752-guBlxMDpD0fzmYFKdkELY5tlK00YkCcZMBYfBVjrnSYOdoqmjMOFpj1zFFD-dGd4f2ASv44OL7VO2mtuQKTgdGkJjw0Hi7aBovERth3jVCm_TUfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=U8tIxudn9CxV-LRceLzgiVmb4HcRqEEZVYP2poh0sPPxFNd-wUZpFxnbQrdsKPOKID10EhetkE7parhQ5OgjoAl9eLdeR8eUYklhWJeseR5qvL7YIOh4Y0S2hosOm7zmlf00e_T5bAtdT6ypARjAvbROX0njx1sEfJUZCwgOfQw32DNM7THXjntJg5vJgUdn3rY_WHR6l_3LyI17Tt_DNV0VDrl6xcdwll752-guBlxMDpD0fzmYFKdkELY5tlK00YkCcZMBYfBVjrnSYOdoqmjMOFpj1zFFD-dGd4f2ASv44OL7VO2mtuQKTgdGkJjw0Hi7aBovERth3jVCm_TUfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJfUXSGGGqeRmGP-Ydi_fC-Y4NuiiPsmBF9mYggx0Myi9V66rFcXQZ3vn3xWVYPLOC1E7aBbMHSOUqbywaS7pmS9pD4eyn841Ji-P4xBzzXYXtS9l1ID2yHlOAQghfdf55HD5eHWT6AUOowadJ1AINvYKN6JU6dbxskv0FUp0RablX9ZvvNzomYETz4rS2e3Y23JmggtcPEc13HqFF1XTLR-VVAAEj8XqUrwm9s2u64nByZo-k7onEfy8_BsAwBA_DSc4kixHqubn89j4bAhLaPkxybSRgPPVMh6p7UrTred9IlgL-dIoJQDJTRmh46bfNQksSb70oG4m-N26spVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0q5kPoTx0pv7RivkXqMlBxPN5p9WFRDnWaacSRyY77HcYT176YFDImc5cbxk-eP88lkHnC0hQK-GIJ55o5ON7xE4xc4lP94Z145kdMFuLNTqL8zj0D33rDigFony9rIF68VyOMJGTrFd8bj5ecS9eG-5-HrVJVBuXzqsmZ3CuZb4GhCWCcEOeBAfGlEWh9DJc_LAk2njsRsq8RgW5hSEr94KWqbL3jz6Wa2rko9qCjYPLwbEHyU83mvJCxL9_2tpeG1T2B7DnRmx7UZhRT3dQvS5O-yWGlbpBbWYQYEkK72OS5mBrnVtJXu7_mzByO4BeOlnpHsdnm2ZWjaSASM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=E3Yo6bby2VxbYKiu_8xzDfZi5R_M_XjZc6PTo1oPjLi6plwUM4NI64qdGPT8-Qv39xsXK7OvbKI3HsCsVpQcSGlNftcoEd2VLIVK_fz6rszvoaBJpQdoZFwfv_cal3zTNUBVAxiOHV1GRugNd-oJ_mGDuRg5D4dflhr02hvWjADbKEc3wA25t1p-bFXQ6L1_QFvWwf5oo6YLlFnsiw0-tL1bBWvadpYl-jLYf1iPK61FwfhZxgHrppA5zp09URgfBSiL1mFDktqOOK8kLhKQOySGOYD6YVm4UdRBpVGlyIQdPf7o0LxjPdzEWB74xTNvMmYoH5lJr8L9EySRK-85HHJRjW1d-OjwxKl0TrChj6sUg8ZW8xp5S7pK6OOUqxfycqDozilsAoM5k-kwZ-Qt7prkmcnVNiS9C3aC1pooQ66TSFtwRMEm38ka-39DEkYIW4sLlXGdk2ZGyyplTJeB415lIm72mgQEWy4t4qi1Gxkut2sWmkcHiqTqxWG4OP_4qYEfdeqGFtqv4lmuqdYEP0d03EmlZKw5-SK-WxIWJmaqB6ROE88jy1YjDdc0z7lXfdAqmRonAiEfuM6uloiEVha5bN9vfhe-_VnXdNLiABhDFxOJgJshB-htuEiNrCvuUtODCaklix8A_-D85ueWnxB3Ro8Ypu5z9rB8CSlX-x4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=E3Yo6bby2VxbYKiu_8xzDfZi5R_M_XjZc6PTo1oPjLi6plwUM4NI64qdGPT8-Qv39xsXK7OvbKI3HsCsVpQcSGlNftcoEd2VLIVK_fz6rszvoaBJpQdoZFwfv_cal3zTNUBVAxiOHV1GRugNd-oJ_mGDuRg5D4dflhr02hvWjADbKEc3wA25t1p-bFXQ6L1_QFvWwf5oo6YLlFnsiw0-tL1bBWvadpYl-jLYf1iPK61FwfhZxgHrppA5zp09URgfBSiL1mFDktqOOK8kLhKQOySGOYD6YVm4UdRBpVGlyIQdPf7o0LxjPdzEWB74xTNvMmYoH5lJr8L9EySRK-85HHJRjW1d-OjwxKl0TrChj6sUg8ZW8xp5S7pK6OOUqxfycqDozilsAoM5k-kwZ-Qt7prkmcnVNiS9C3aC1pooQ66TSFtwRMEm38ka-39DEkYIW4sLlXGdk2ZGyyplTJeB415lIm72mgQEWy4t4qi1Gxkut2sWmkcHiqTqxWG4OP_4qYEfdeqGFtqv4lmuqdYEP0d03EmlZKw5-SK-WxIWJmaqB6ROE88jy1YjDdc0z7lXfdAqmRonAiEfuM6uloiEVha5bN9vfhe-_VnXdNLiABhDFxOJgJshB-htuEiNrCvuUtODCaklix8A_-D85ueWnxB3Ro8Ypu5z9rB8CSlX-x4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7W0wldKSP8wOJ6-j3-KJ2Rk4gdS-ezA19GS3ayrWb8nsD8bdgUM3Rn4P0uzNqzk8U1HR2YWljO-Zhi8cewBNkS_mtx2tmeFhUQ-Ku5G2mW132ymJHR9Kim6LI5IaV0FUrbL0JMgKaGUOsVlYebdnOaM8d9qt3T6ty53CL6L65dXywZIlLR-0a1BAf_-1HD3DzGn-6-HchWgyMZ9CwgSfUfne51DAthNctoBqlwX29q4gdqixXGzAEsyLA32Vb6BdZgJYppYzFvqWcAw4lv0JMxjQdIrktzzYjYWefO-ZrLuHURtUqMK02NNQHlfxfzGzjh8dYQOi8jz4gAvDHsFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdOzsVGtKl2FbiNfkWKvP3PQ0sHDO3t4-o3_EAyLZGhV7CPKbruLtDkCkx6lC7i_zPYYIkYjEDxzeKTiMBFqq46TckZiVql5IrJCC7ICpQBMw3MrfWH3O9jQoyCUSRCLhQO2sDTpf5QLuIz7eZuhU8up6yILnUGTNC2DGxMeWaqYIPyXZo4YS8-7vfsERopmxa6APHHZMLAj_SYnBhjlVxvoSF7NmvtLbLgyiyoeGelt_G_mpjSACwK2h8RMesdXVKodsc4tpWYKQSb7EgOpk5qzQ9dBhX_Z9WOPlwD0BXLS3r175puh6PKdS2EskqfxJKAC3_RZq-H58PyX6lhk0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqpqLYLTXgCTn-PXAqNZnXPj-HgCofIr8prXJ3mTuNgMrVmxsrTK7PynZl4FM6XSX2lfAsNyAVp70iktSjmWdrVdMHkaG-lX5Aos5hxWU5Z-3UkNXxE9mfETAQx-bsO6FTYoAZSNiWg1hXwr1sqaHiMHX218fX30XqBgqSu85PHw7sPmC6EeBpyFANQhcoXCppol4nh6ZgcsJZiHVJsw41alNw6EnPjDOIWDQDh5IdJdjCb3n_3GyxsIaQ9fkw1YpHuK-XZ8qxCNDCoQueFwOXQy1raQG5oINDYSnd_Sz6dbbFtSC5JGo9PmGnv1t-6RZWttxjNxu5SaURQbY987XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHH1aWviCDaNiB4ghqu-Y_btI9X13nLirZBXRvb1iUrBMyU7jlmXoFC8bVVwfKR7orbjdZyy9lfVLw01WjaD1RzLJ_aiignfd3NITPt87oST6E5arhwRAj5H3WkyzonSEhIC47bFE06znuXzBHOFPvdPosvZ-OlyegWNocvjwFs1gX-MIbOyftyjwFnk9Uw4SS8iHsoN0aF6FhekibVA3xTMI_t-wWoqX3ccVumWfiD9b1iBUP7DOh7AXSJz17qekt-zo2CuspJwXN_eNQCx76k-GW0f1AYjqGvUO_-LQg4nePCwlgs2P_UgwdwXlcbZm8oyUqPlfsJEA6bU4Oaxug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=Hd1RcwZEax7Jgqm98dgDIjkKazNy130gz3lymyd7TXE8Tu9V2_0pkDrvS6xwfZUPqLSqFdwKw6aeWlhPzqEOJwSo_3NzrmIFJ1k4IlmMDp3f9UysR4YwYzwVxdwGAaYPJUkMVnnrqvmBESTYxZUULXpdK6XfA0024hgX4XbMr7Ztaxd5oGLtFV9imsM9SNX4Pl7M1MZsaavxzsbR60MqzhEODy8gFT3flzxTnIA8sVul8fo0Gjv4LePiIUGyjPWL3njYbDnMdyLS2n9vFR-OfAkX-C-DXflCAclo5EiR05vw4Te8KRdVa19oTtjLm84mdvMGYO0WALcN6Pyg2nKIzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=Hd1RcwZEax7Jgqm98dgDIjkKazNy130gz3lymyd7TXE8Tu9V2_0pkDrvS6xwfZUPqLSqFdwKw6aeWlhPzqEOJwSo_3NzrmIFJ1k4IlmMDp3f9UysR4YwYzwVxdwGAaYPJUkMVnnrqvmBESTYxZUULXpdK6XfA0024hgX4XbMr7Ztaxd5oGLtFV9imsM9SNX4Pl7M1MZsaavxzsbR60MqzhEODy8gFT3flzxTnIA8sVul8fo0Gjv4LePiIUGyjPWL3njYbDnMdyLS2n9vFR-OfAkX-C-DXflCAclo5EiR05vw4Te8KRdVa19oTtjLm84mdvMGYO0WALcN6Pyg2nKIzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG0A2I4XxL5MtHHy36PBnrqTX0u9TrvI-S_M99kABhOiBz7UIi79q76qUuEJP3YXg5SqNMoQqZ4g-j0aj_fXEyFH2ayVlJOzyJXbxK5wDaUce-KmcIsNgAaO6BvR1Cr3tJ0cnY9RmnpjLv88W-D_B5CI5hhZOFv8rfydf0kBX8fb0veEr7J-EY5I0HN67UKrpl1wIX5vzBdOtfCMSZwUr821EZzOOi40RiGupndzOGccqX3Us0yhZUHbROLAx7TXlMG2tQPXok_xwyHf7IbKUue2vSSzj9HiVVlyfqbs7Ubm8opDAgRvEpX69u_CDPmK9FmJu-8ZJSvxTZOl7cxRsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9LyWP9yQBQ_Fni73fibYiURArJ4ONXsYN1GhdYxoPuHBx6-88MaH6oJelTX-4pOowcdG2ixxD20cFn2RtDtkPlwkpuHixOKCR0xWo8VJcgymlHyFLUc7xsiVS7leXAXRh2aon72X8Rmtn-DH86jE6yroIdcdhTG9JbVO9tz6D_0VKQ0S-SZGgu45EXc-l5o0rbwzor5t0ispFP0c6XWy_wgAMzhz5dKEPdENm6EriNAFjZM9vfGN_qB7TV4lrdMZoJOczgRZRDca_WpcXA1M7X3rkEaRgb5UODtRSSU0USJJx8B6tfxKJiC_VT8ABVI16pLlWzrdY1GiU9iLgpNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItVTNb4BipwaMaibwzETkL4j1J6woHtqaxUp5yrC5Xb3f3FwqDPHjHSPF1Jm5g3q0ImWdJ7oHAzl44PF8QE0iZFSzyoBnwPfyEn5ihazTQQHCVY_1kbsWX5ANaZH0m0pfWX-p9cnPWiYcgC5r6GD_BdcNzx28sz8ydDNocGiPkXp6U7WSrW0A7Yy2Bre-1UCTwCI47J-vfZ5GZHED9RAVKG7RrnKd7zUZmG9G43EKXOJ11cV9Zv6o9513BzMGKPJ5wT02tKVwm7ONWFDOT9qXqsl8vC8oHvU7m8ptqcPYmA5velETm4l8aJQ17csTYstOo0g82yDKsDcGUd1rFaCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nnngD7hO2yG_tkDE92s4CZSvTd4Ozw9alDFwbpKp4cbn327gS1Y8olIeSX2jHmz718499zxTgl_Id36znppGzxG1LiL4HGMmhj2Ehm5AOjNKByRbPhApW1GvpO5yw0p39iTV7dzEU0kqmFTJbO3URVCYJJPzxk5XC3mTX0LnUrOwvcaY8xXx6ifNIvfXyiK85vwEZUsxRaKMrPqNqrZk4MAsxO03tkZ4zGEuDbTUMmvvwZB1zxcltYzv2LQ8nAJDgrwSTQgnHwQHogpk4TM7SlIWQ5iRMScAECC7ZE-iYLtGPv5ESmY4lNh1B_t8hyQsTOwlCWbNlWBDX8aE1OxYWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDBw5RpAZVkN8HDnYiMIQl0V4SoUUx9ElT3IzJAOen6cvQt726tKCg-zduL-buqpY_iajRG3FY6MbinyG9t0uIAYV2RaQRwiqJt5DP0rHlh5_2zLt-0dicf_f1sCdldjD1A3dQTnIvzUd-0PRpWWYEJQnxCtv6I3SDww8fA_FWKg0GwWKooO15wYYfM8tXqAy5Y9Sudan4tku5PxHv8RhFqzyq6i3CuF1GAXQHLuq1cJxkM3CLRQ9o0Lb1AJQxX_hb5CC-87Tg3v9pvF92_7B4cOScEsA2VMavnFrLkf5NwlzBHAsynoCoaIc5NO0PdavHuBpKyanho1qo__4ypbfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umq8QZ6x2EUxj2HGQqKdlJTR_cf49QBxwAeNqRoz4jOcLd9sKutxSuGy869ZteK6RSuedzici62-DzcXt-si1vjTNhgK6dWDmeFK8zXc7dKrjWJRfKlt7PEA5Fh3GnCJKv-oXwiCj9rRkrZlCcqTYybsbCmR3ME-ufLnuCvZ6iHv7xkVqsVLyV4fF996oQdJ7H5ghMVretznO7ZxyYgvwQRKP3eQVVkljGMX-LVHvlzHfrl3mQYKw0dvgQgIBgwyoVXdRfk1w-U1e_DKUZQMX3dTQszSs55mfPOmliVHtWckkELFQVRiXzGTfDiRG9505vKwjxQZbKhwpr3WK_Ddzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzsoTSUz2v1dbmx3T3GGI-b8bJM6zPHoVX2DmxBmQvBxUaVWTABjW5ffIy2HStKamminNYMnKwdKvsjuFLErj-jJpzGj6CsnoQDIroCvZ9IfJVR1t3F3vq0ynFBVdnALb7kQiXOshvYcS-GV1BwC6b3gjwv3ebmHhASxfrrypV--b7Hk6JsBObu2THLDWgHhHobg0nmF7yZgPPIhymOV00HgjS_R2uxp8RabWINKLklDcflskwATDplfHFDIlEC_ZgUbik831bi3_QFXYjnRzODyg-0fYWJLxHHEjH8ZV3jij-u9iMJQpAc28ah0JlBIOVbo1MZaVLOCb990hJiRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7z8-bGd-IhJmCSfgS1HNigcdsA78yS8Ovs5qX4264QnSQFGDg11xh-pVn0qrFc-NQ-Czj-Ctz6fuw20g6UADFNBgoPng0HHg1bKgovupW2P_TFNWQqEvFy0VIZ3MRm8UDVqauawrIVuIXUqSJQYtvVXlX0a7PfEwOOCsZ1UM6X7f6E2sRfUEmEOE0grBWxjeL1onoRuk1qWY8wy2Ip9Atg0bU12loH4dLV180lI0kh1WAUQsJOlComWAph0xxRirS8cVQC5iN4c2KM3-pPfWefEBYcfL9_lqTW56657hhft_P-fBl931tj2Ex4dNoSEE1UFbjNK2vOj05PDVnYAFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APgdb35oxz-rSXXjeHDQAWJaPwYxcOtoJnFZnMIapAs39f6CEvcayEPBZX7MbtEJn_eWD0WLz4ySU8T5WqOwzHQhcwsK0bBU5URQxS4PYkl4IUnl6-ypnM8h2Wy48yqReoO90ngZx14pALmZtTBUmGCxWz-yaOVjswVIo2i5bWLTHY585f6BaGrfnXPtIl86JOTAvj9_HMxQeo-AKWuu1W1QsCrArUl2BSRE1cDw3oXuiekPlFNkFHhBZwFu24KKgBbkW1-lN2haFF77uz6QZ8qWIxjZoOwWVzpbceqn08cMRzyx64zRSbMJo8c8fO6xzjFkRCFl26_Z0ZlXqz6VoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vo2KrkoClPow5rJcZ_t8f3JJ_KrI7H3TgMWfkmYbRXg8NSTYPbHOQ41uhm9fG7zmuuoBLBSDqia8K-16pHb3hq08m2PjBr5eajQBlw6RbeYuDgUmPwSfaxOi3DHKcQMy-H1478q7PZHq7ypQGrNVvBqI3FjBn5WeTbxArYWkbi6Sp_aIjaLC8paRTpONg_vUd8JTHpzhQoFFexpETK9KBGj3_trD2z8sKpzaQ-r4PQ42wcU-pwBlNdEhBy4w5LRVXxpiuub_xNlP6yLmuOZvbuL7cH2mV1nsiIwnj9JCLg9-27IQ0D1-bZFTh3IOvzOQcGMsfDIdzBPr69xkkkJnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dzn2vu8ys1Icjs5FsF28hjuwpch6Kv2Kab-x4LQJA5R8HYWMk-vQokM8qdj4E8re4QB4YWrT-on23egCzQ8YX8Fs58SxgmKmrQwpOPmGNnARzexViYwNBxDT7ns5_diR1XOBsToJtfiaaEA60BlLhExNpelp_CPSUJnDVGiAir6GDcKKnsuDPeg0x2ep6TWg-hD9LaV5MfDGY22bbcZrWTjUtJGvGjW5a2e3y5shQuj1oRZOpYMLII9v3TgDMyuK4o-dEjaf_Hz__QJJWzfdrzt_NmwhvtoqgNK1QQ5tfh_iXpSSs2epdxbMoHnZTPYt53ZOs5iBcxwqoneli-RYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hay3vD-etu7XOoi6dLGQbAwfWAQ3-ZoRVR0cXG2ob3y4dLvqqIO1cK102q-a53kSoFtT4v8zl-hNVXpa83moc__sE8h1mRPjV3Wy5i4O5EXf5iwFthQuXDGvNP_lNG2IhNi6hyY2Jg64yV8YVOsFCdLtsnRpN38w3WU3ejvYsHOfoEllBxtyqWrJ9IGxGjemfCv_yoRZJInuF3eTrEom0LIeGoMJZl4TKlw4wugMDY7Cs-HtPoa5y3y0PBSwFiCMvFPfmgyB6cbfU4524_f_DoBpdo5hsevTOniR9q0AUhkzCUIgZ7_piNIHa22QF5dg0hkOSJCuVjQQwh9O6Q41OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZYY_4IBAD0id6aob9xtG1jlOXGZpAjC50gVyXNaUsJmxPgSkbdPv976g6yofy8uA96tq2PM4G7YJzVZUsFFdawjUK5_gmA0IUqDaJVgIur3fQrojrgBoHNI5hQcQ3BQbhq8vf8A9z3hVX79VCsYbcWcAGKra5qE4FjdpU4Y9XQtMHfBEW3KaNOQ2WO5G8S-vsf_kah3hc2t9woSTmLNrAlZ4NVlc1r6AEsj8jC7HSgu65jVF6F9_ZjL_12SkVp5Z0Ahk0nWp5nTFRzMsfg2P9EvbQrFC8zpuuGtYpWPe-11Xm4iJVOGREfHTz8FsShS7ARgobB1iJWxdWlZdthuiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOqkKS6o90GeSsVo8yz0AJyl5zuaT3_sVNm_RQqFMciif3orLXWfguK9_eE-tX2wb3R9snXfqFSQfRrCsi4J12koJgVDO6SfEGQdhqjy9pxc9_2Bu2lLmUWyq3Ff37RNnJ-wnItvId1Yo-CM3TwP0qKEPjvi9pg-ZEZfNyj4o7T1PrJ983ni2P9NyRAE525tn3L_W7croEXI-iIkoyzorqBCRXNUq5CSON-kWRMghzoHFOvyQy8hTpRBZSwe-ar648aWx9jEepifV_9lZDgA3ZxX6B_7hxWZQLUI2D9ItIx6nS8MHzguTM2biqleegzz7QQTq8F4HLpxZ_i6734T1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgKKlyHHcjE2YBQE9KB3orMcS7rSjp7tCoymFUo5RmROQ8-gf6T45eJCHJzx2QjkVR15f7BsC4y9HQb3KLcIThWQZMcrGSj4HdSzoG4O5J7IGXmig56ayDLiyxS3OxUgjOLpF9NG6CkXruyATswIUofSq2tt01o8wKmH2ajMqMCmOg7JTBjuzvUqA995XtBTDFTHJcluxmiqrMN4liwSTzk0FymCaIwml3o0G11r4tgJWgtB20SFIFQC-3dyGUiXM_a9-_FlqDYg0ZGkrit7l0xs9G1CkTWnR8HFk0JpMyqiwmV5-23woImOBOhBsya16kIbJ_3-_yyTdoGjov3bjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-2hLkLdo1UknuIFjfIq7vMuxqUJqSwrvmm9zazH9zyFw7adecP60bc96I1dXYWlLxaUWrL7-C2bAH1gesUk0ajAJwT6pcnM0-vmiw6SsLsPWmB0mzAmtxtMNOuH4IUDhpIj6YQX6szC_dFLbXaKvHT8cWZNKYRZKp0eZ3M2s1mDEWBRYyhoG-3kTjKeUKtEC8mw_kWTsRbOJFLJo4vXzlvF9MqFNMYyj_QncmCqsaCQ0MnzDxbqD8dEfbdeROnuSFvh1ZVp4UqvkRDIPYI38dsKNeomzwRmHDwGU6KyyFZtoJWDPaHKbhhfo_FTMf6cMNpStgJPTWYvRsBVI2AkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AGO6yio654XpJzOjpCb5bHP0zilGaqzy9WT_uOvNRqbjz9HnqlnUAFbsxum0M3AkVRfjr_ni9a-3QxwOLkGT64v_-1wJ36kGIKYL39VfwdWkXKCmcnjXn9P_lFylStT2nd_gLITlNynEZ6QzGuMVtsr-WSPIe0tPd2eeD3a-5KWMq_OTC4SqN6FcHMx_Tcd167Jpavh05gallbc8m682MyT9yyWfWRMkNXOStPswzAw1pFx3b8d7YP-nt6iUOBThxMJ_EtjIrY89HurM_cKsuDAVjv7zTYnqVi_ajXmW8nEflg9Xf7TgMQ5RXJduQtkBaJiLZcRZJ22jDlAZN3C1ay4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AGO6yio654XpJzOjpCb5bHP0zilGaqzy9WT_uOvNRqbjz9HnqlnUAFbsxum0M3AkVRfjr_ni9a-3QxwOLkGT64v_-1wJ36kGIKYL39VfwdWkXKCmcnjXn9P_lFylStT2nd_gLITlNynEZ6QzGuMVtsr-WSPIe0tPd2eeD3a-5KWMq_OTC4SqN6FcHMx_Tcd167Jpavh05gallbc8m682MyT9yyWfWRMkNXOStPswzAw1pFx3b8d7YP-nt6iUOBThxMJ_EtjIrY89HurM_cKsuDAVjv7zTYnqVi_ajXmW8nEflg9Xf7TgMQ5RXJduQtkBaJiLZcRZJ22jDlAZN3C1ay4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=TFn3npk0L700q7n19HTeu0f1ahf3icj_H1_6v64xonXDs23oGPyPBylLtu4N9031jBgQr9WwLD8rTXN2ik91lELPHbaHwNFVqXwrJTULNdNGCuL29HHFGm3hOVcfXkxuPicBeWGGgCDNTM8c3C0z8S3CWTb8pJdITqizZvcjwuDS2VeH-yj-8tZlP5ZKTQ7CEFsCUJfkJvVcRbRtEcDL736Gz0R-oNETkNVSmBEf1DfsCxMIlkveLf2J1PZi66JcGsX--MwYqqzKqv2ZTskFQtB9H6_9_DV9voG8mMuYRILGCK3JZlqNySK69rpAgQCHejP5gARDGT9QCWyVnX8M7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=TFn3npk0L700q7n19HTeu0f1ahf3icj_H1_6v64xonXDs23oGPyPBylLtu4N9031jBgQr9WwLD8rTXN2ik91lELPHbaHwNFVqXwrJTULNdNGCuL29HHFGm3hOVcfXkxuPicBeWGGgCDNTM8c3C0z8S3CWTb8pJdITqizZvcjwuDS2VeH-yj-8tZlP5ZKTQ7CEFsCUJfkJvVcRbRtEcDL736Gz0R-oNETkNVSmBEf1DfsCxMIlkveLf2J1PZi66JcGsX--MwYqqzKqv2ZTskFQtB9H6_9_DV9voG8mMuYRILGCK3JZlqNySK69rpAgQCHejP5gARDGT9QCWyVnX8M7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXAugbFQDQvBDhACm1r9FiSOxv3O_-R6A_sCzkS6IGyY1_MIYpj0O9Fr_ppsNN5EKAhtzJI2QPCq__FSmzySzLHVunp25H0w73TcNLIqWoR3Jjf2jMzfNNMTMeOkO2W9jPgtXRg3fgElwzUnufYaQium0ILOFfwApOeKymHrXSJrgNHN3D0J5rilFOttShoulS6vOpnOVY8SN4KbU_CaZJM39PMAkzJwbJTQio4i8InveACKyztuidZIVpctnbZISK8mCJDTlWJJ8JtkEo6LNKrVo_NcANoFn3bd7BMTV-MUn2lYDACMZbP1we8c1sfmd46BNQB9MiOQWE_OYCNvAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5IWBCRPLf8gVrpvo4PWyAy0z0_whiWqkmgouw-zdLXsyTBs9dYiOsTrT1Nf4KKbrbLzamtspa-pxiXyloFDCvk0Y01KuYS5ZA53LaL2g89JlC35kHlQK6sJtge_S8e6gLoLcJU28PeJUVGgF0aAS87yhzDzyZgnK6zuWOvvD2fHaYmUaShq9YhWvlRLrBAbewRVD6GyEBD2Azn9MFy9vh0buKnLKIytiBqmYbhSY5Sy-JJz4UrJxoKXXBfwROwaDnKfXxk2deymsTqjozsxlJ5Bvk7qFdTuAipcqW5cLe8Zxzx6vQTRMtXlWQnPUfXlqIjKK10P-bXXHxt4G0xmRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUwHl_waYoE_4oAHj8XTAyFolAOpQyY2jwdqVoW7QJlws8yXKXx8m7A2oh_drdQfELNzr1z9rl4-nviAOeIY6tVQ2CcP2U6V9bcV3_bRev-M0_q-0QIupISToQHm4HMY0f_qzvdy-PbnACkhi_iHIxMd9YyoWCsd-td0Afm2GrtJtiXDXWjdLBGMpiniKNVdIJJ1SlupXaOLe7f2hJP1ODaIfqN0hmYw6DXGOew9kQfiqFsISuD7dVaoxkfy7FElZE68Nfy7Fzp2NEZDSrT9Xi_n2J8FfKZHHBewAfPtJQhAoGyOto_9yNGMkbJUxrTOgtwRI9zN4_PCYt6TQ6tksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKT8JK8-Yqxk4sDINvBqBXlZEZ1Zuv_wVO69MIuGlugkfB8VW-Fnjwr7-arlml891bTABHcZ_sb8Sc3vnU221w-uiZ3JKVf8EmIvG6nrkVjFnlRp4RCm-LJK0NMbEkNJwRpgAD42QrkVqHnd7bOM02KFsCLUZF7qGUBobikhJAPzYYLHFJZ58s492j4QClyc4vhLehr_xx1udHFNMPFbkrYBpLRzD0Fqil20RT9i7P7qZ8FO_96FWCNROBOr8bM_qaGaM3sKtqDCihvdfuy9Ss9Fi3UouzmkDhPjFuQYwfjipVPrbCZ-sM4Q6XYDhic4ewD_hSOs8ZDGGglpEBbLgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCPoc-yGOozNj9wnf-H1MKR05JjxVyPHIWjNVbD_LcuKgaXxsCHz6RUJ4z1DIvXBsmTC26JzctrgWswPqnlC67TZsfXAKB-vVZwbxFoiu8clVN9cJdfVTvxvv_sXY89d8qByD9-jifIfoECk5Rz57QyohM-q4MwSesQf84MltmNO4kvC_OqRT1w8hzDruV3qT7Ve4Lk56Oe9FW1eDUmjeeuuS_AJrdKqK97YaRYXYxCVAOTyLM7w2bwAyFmJ49uP-VKRsU0UrPNGbKKpbKIXuK_NXzVZa8Y48bvQhfHgsofOIpQbLZnV2Xow4Q6w2uWzIZVX4DBhVo2mCWlhyrAzpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxVTG4rze3pNjI4xnxz9WYvsSCxnPyBc7tiHR2IIqIJWB5htNgtSEVG5hBJ072BrCl6jgXf9_fFJ3Rk73cIiX7jqHocbVkoLUG8b41nFQa8UWzeGy2ouiD_mwAfrZEhdZR-EyySzqyCiUR3DqSAM2xDCeYq1guoFh_FhEanhFPwmeDsB7Tg-qT5mRWNaypQX9Ha0XLRFFKjJVRpe9rKzwUUQsASxd26Fc4n9C0jfnIEzRoxdOLiIIvwW6YGqTHjzjiFC8Gz1y0jVh1RpCQq7NzFpAv25WmV7SsyY6gAWZfaFs03gHSAkX8H4KBxUIodZCBInOmzceYI6FL9dGM3oqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4rNjH1IabrXTnXt52wdmMwqt7hqZZljGaQrBI4B63RFSzh3v17XAgCOeT1s5WU5dUPTdWA2tF1NbK6RoCCA0hf64u0SzKqd_Ru0A1_bpeMIz1uvSkPela1pCJK0JHSJxCI8SzwZF4ZBFy17lODqEqTo0JoMFUV4rbiMD2hxC3i8C9Xrp8t3Twu6nOXJMnXVM2GnOx0xlcdWi6l0mqG6872JKhGG04u30Vkwd7fS6OJR4VeeTa4qLGILAql__TjiItu84yinKrmK3YNZhMPnu6bUoKZSDQSTmgpTVUGwYuSqrVuqJ54uwMbZ7_nq39X-WcqqGP3VEgGsO0HSYn03KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbPzhF2k0sC7DJ75byxAz8HiAga5nhi7wFmva7lVtP6oA3vveyLptzR7nsIJf6gT3nYxt7255UrVxpbIqwBYfsrPpcR_wGA5FP6krFCk3vCIxP_JFqw4ECO034msjVV1rqG5EWp2szu4Ckk5b1I3aTBjfKOxpqKCYyBVsMRgi-67j_gOPDlAtgLmhG5txQbFyrLAkbHD22J_H7S13IixXC_9lFb4NJ3If2qBNvEqqiPu1iGa53FQjQjhCVLc_NwXVqU-YOWgYMDbK-rj15wIaTnxzJQdFVyeQTz5uBWrnsiU3Gg9ZylBK__qtuuJ-OLfPnUvHDoIeyqAzUpdrt4eSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDsIG4XoMZVz2ZmFoTa1OGMjvzfavk_CdK2lJ6r9TGoYUvcxjtIIl_RBeMD6r-slkMVi4pB1jGVFnHRrsTLk_XcOCEP2uzKPhGuBbThQm89YDnVJM6nfwBqbKGWLWaIX7kmEWb34GxXLpg-3ZV8eMaCox3OJHzPJ34Yo5jBetGvpuyADtGRa7lkIQjufPbXvrKAxjek--tx2wUA7bP6wJJGGwMmxPN263XjkzutDkLY-YiMylYOyuke0Hzxqz_tK_aoPRmRAstNyUnseDYWv72CaXIUMrlL7E8vczHs2quismqmICXAhWfETLB2Wxb1zM0EN-_8dQye8X-Egxe65sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9Ixts2618MZslrhfw9SeP4sImIIQyFbVAOB78Ez2EBtmEOLdhklIosVCkD081evpxrP6y8ltl2ZougO-BU0xB5vFpUgvZvICHOqRRJfx1EBDZv7FeBN3BxPoT43lFJX5KVvYQdSiF-XbCEPV3DLpYeFM_DJssRSc7fov3vqe-Csav4zMuFdNt0xtFWUx2llfql2I-G-6ETzaKtRVhMEKF1coOWBmIzCyR-53kmkrt7Z6eUxCT9JCd2BelTkGmRXnsx4qoie91hZl3dJ9jEY4mzJUlf2oDeP1hZe1gejvEdagjV7U9sCiBAJ_iJMWkysTJACrYThwDmUMtBHZohsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=I6d6swhzNieT940wCj16l4Es0AjK0d5VojF5Dm9L0npbkAz2P6Q79LKxQG2QP3D0ZKcq82b0L-5O-cKodfRaKupdB_6Q0MPNTUnszWvQpCAA2wnx-TnYVZstmmaC4wISLUI1JXG6aTODYhnababMKcO7Batbm19y1jJeeGDr_Lz7pak_kB3PZO50qlZ467hQ27n5ui24pCbZv-0O8ZgO9Mt3Vm-MnibtTBYfCe4bEKkmzRTiJGhrKXh-L_iZGN7HLTdLm5aSOkb5OPyD9hn4kO3PJ_TBTkT8OtwC5tkbS0-cujxKRjGWUImhI4Oij5I3EtyfjOFsmbvNXurqiOx96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=I6d6swhzNieT940wCj16l4Es0AjK0d5VojF5Dm9L0npbkAz2P6Q79LKxQG2QP3D0ZKcq82b0L-5O-cKodfRaKupdB_6Q0MPNTUnszWvQpCAA2wnx-TnYVZstmmaC4wISLUI1JXG6aTODYhnababMKcO7Batbm19y1jJeeGDr_Lz7pak_kB3PZO50qlZ467hQ27n5ui24pCbZv-0O8ZgO9Mt3Vm-MnibtTBYfCe4bEKkmzRTiJGhrKXh-L_iZGN7HLTdLm5aSOkb5OPyD9hn4kO3PJ_TBTkT8OtwC5tkbS0-cujxKRjGWUImhI4Oij5I3EtyfjOFsmbvNXurqiOx96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYtvUIObr8KDRxCMr5qEsEUgGDViJj3xHetVS24sdPF5xNPpDDZXYYVYWxCXYVFnkM9-BEraJ_5Ui9PLb73bhelPNfLKJjDfh4viXqI1_xYh3BYn-RWzmcHNs3Ct73drTUsF3Pq8aWZfiiZZqpfUAh3AD8J4JViFMykM79qqDZ_0Vz31hpRE1BsB8593IKL2qpa08Wb45XTp0COQzsZMikZwNydDaqsZNkncqtE6qQ01a8BsnVT1GtMdO4DRiyCCVCNr16jwxvNSWCPYZQ4FnbA3suGDMyttkco5oiYfnWOuO_o1PG3kCM4oGspm09qHLxJkohs1rOv5NP5SkJ7R_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f--6sSgZEWpMcjmStSe-KeNq1mrcE8ktPuvdSSuvXBT2ANJsPopZjZh0Ydvu5NTIJfaJ-Qbcvq2Uix4xKVmUaH-oMcBm2124pRZWOe74kCGkBWKqwrgj3_TasVzUQWpTZychdDwGCQwnhZ9jsPdanAEBxVl7ro2GLG7GjdqtHbfvcoBxtH2_OCUVve1tr67FY-E6DRdqpm_Lrj7VCq2WXN1Li9DOiG5eGJwylhZkmhtZE-oPRvp2l43xD09BbqmFaZBWFLsrYwKM6tegMRaah1dyZ4XNweXT4O9KIkVAncA9M4ZKSZ8Z1UDEVQmv4SMUuzD3FnkL5XHgIKy2I4TQZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVC2fnkl3TQAeJGJA9KBmS0fp4ZzniDHG4fRIvkJX-KYck5QJyJdSQQLwLMMaHLvNRMQQSFL2BUkFbvYnu6lHQd2v_T17jG0vNbfA7OF5vxagPloOz2691I0fw8BPqK0sqaRHP4ZycdHUQBb4oS3erf9cRMbJNDx9aPEg7h9FqpKhSDREHnmjcHlZgLfo1T_3Koq3E42MT3ImbzeUSaZ1v5TvFp6kR2M_8q5GjUH9PocjaRztzHAwou54IugGsJVgmkDc3MTw9CcqXSekUIhiKMvzA-gVseS2oX5JdD1fodS8bnwt6rd8VcTHFFRrUK061Wnpnn_9yhFDFOtZRHk5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqFBTxH3w1vpgagUf-I2P0jdZvcB13eh4WsmOaq831tR2tbJNI36hVBa0DZFc7K_7sYtvFQ0udpLWF9712t9mbdU4snMLBCl5BOEIxGG0f_9_P-4_kCKdORDpOHO_AMH-qozEpMgx0sLAx7XLjW5NWAB8sv4QnqPpRZHYfRF3RqVYi1i1nSiS_Tl6T5GqrcIrTeqRcPbTNF8dc-_oAVJPpf2Xey0E-tafuZgB-dbTSel-0VC0yIeaOH4EI5RzrKnZnBz4p8CJ16LLlqcnKAAg2LR2yeVioUc-I7_ixFZBl8SG2smlFvIht6ocBosXcqKJfUuBRHKdgJ_VPA6vxZXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awyPVDE521o6Fy6XcpesafBXXPt3pJzkgOIq8OXGJ-f0rBM1lpsMhAG2k2Rw0l1_byRcVfotmIiMKldgNTRvFqfQRPkd2pnNOSITqDnBPkKQehpw8rXx6-Ai4LyvJ9D4QinOLqIUQ-UI65g3QJsp_Y45jHoIOYT0U7QwjZu5tGASE4P9zonYoVUaOgFH61RiLrzvxZBKtJ2Aj391Xz53Qq2ufTOwxRrkYRQg4zGXo10v8Zha28sspLZrrSI6fSe_XTA2RtDaER4lgmOK8SlkTGdh2jROIDc4S3Z74KWBOq9c3S6YENIwkjcPH7wBrI1a4CfACxZmdixTP1DJOFbCAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPF0bNigym6ytB9AxmbGb8uBWFRdsKasCtJaeYHx9VMcXr7ae6XP3pWtY2oy53h0rcdnvuQN1Nix3OFZYc9AmXENI8F0Vdh4BkdYpvq0cgmeA46cBZ_IradXabXbxcaeAA4fetRRqTRMmgZchvSg3HTbqYnfDTn7z_up6ZslYVdw-UjBmBgoTx1rbc36iMgweHofbhWNHYf1j1IiZWo8K5a6XgnJe5lwcuZ0IxOJsEwNTPxUkIJPVmgi9QCciDT3nOjfK7q62Sx6rIa9vK-kneNadmlqev6D4uFloFFXMkcWhDTjKr57g3m3HyYrc9_uYUjNZDayEJkIgDVJ4NbOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjC5R05PG_d4MiHiZkCPaUYgzKZJqYgECz_kTmuCIXxb-p_sFLBpBnEsGQlubShP8QWlQrFWFpmdLkUocAhVI0QutGsg71LTWhbHzrb2MNrpfnLLSvqcbuSAY2INsHM2RLiDsarh_-Lx-6aoFE8PLLOSJmCgbC09C1CG0GShs22lnNmxJ5EsJeof1U4upqHs7rG2988OQcjaSkUuqoqQNw6hiIHCuWzT0f7G9NgVVqRHJCNbVFQIDGZElvGfEV_RFBURLQkzY255xXaaYA3U-1m8vaO0uG0Rvv-laK0-nkHhhynUevw67of-XS3TNfUvZ3295Bu4q82hBOC_qhU4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnVCh4YKdCAlFrM6mjgCWd-sBkF8hHfobGFzYWg1Ahvfswpez3eMDdzH107lvNGyncqFbQ0Iz7zyDKB25m-wWOv-SI1arZNZAkod1WdCHQYURT0PhZrLR9KIAOGUPc0jcQ7mNPzYxRFsvcWP9NJoeHbu06J0SDByDbiMSW70cZ2jAh9MogC4oWs-fwx9dygIbiub3YEg8GWqlZ-V56loY8Xd1ZPS6EJB3XXkoSjyFFU8M0jDFFPhMLfbSe_B5PmXY2ukJTVkqa9M9Rlql0zfw22m4o9_Rz4bWz_9J2BbSzWq4KRdt3dF5fJ9l_4PUNUC3IrRyiQMYlw9kfu9Srr4-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1z86vRJ0JQtVjEXnqmexjtrFaPTJypn5p4cA8-B_jNcVHpTZT2KOVsS7ga3Rg_PKW-JZ8uN-D86czC8kGCs5fVf508VUaSzrb4ymaoANJ25fjbUF_EID3pO_zzSbT1u3AZif1vMcX4W0TvPBGYXvy9Ooqdpm5qxAqTdAEwhoZJAl-lRzg5yDudpSBOskRXCj75wVSUVJedimxkNGtfZrOQ7_NmryJvDBrR2tLvmeMv-Oi0N-zfwoV5TpBN-VK8e4jK3vpWCIICrR7EgI_W-DLwWBlcPlD_1O53I0zrYCb1DMBNuRf6H-2hoVLWIPRB3dqAoYXrjdJQTBvH-Hv71Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYvvTEiWjHiKfzKbaB-sZwhp9WL2ehjsS80dgUEmCh6P6n_nIm9jdFxX0rJ_Oow20IEnC6LH_y7rWOtfq35bwv3ewNyWqD0Qkvva4_l_24iPBXxwdzG5AqmHTw5lb15SndpE9JM8u6pFdra2wgPGwFEgY0lsmkzITvt2bT394t3und62_NCDmv5LqeGARwGlAL0KK_zca2e6_NrFKsEFvEwJ6AplNv6t5_7hACEFjc7dMlYPhlmzKs0Q8ce0y4o4p7QgkoWtX2ryQ1LvkcyXsL7xDFExwDpLdWlbgU8J58Nbbc5_NgOD_vI4K8e7WTff0z3D-dRSEMEowhr0P6n3jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfIpBUvfm2a9eK38PJYM-Hpl-mKszGGcXf7UyTYR3aGF8SXKy3rl5zbNr6Dw1ggu3h-bOqm8ffEkda46WU7TXzconQKKDU5tjgysHpDwxFKSjlswIyzO7Uh4CiQI6_lg1DDBjTY2-6zEXL0VodYbwhVzs2Uxqvp61IWdMwXlZ_HTBMaYLm-DtKBV0TDK9M2HOiMfcqrO6sR4fBB7NvXKnhq9cjIRL5z1uI7E3CPl9S95oWvjbcfw_WaubJLoIUDP3jSbPkIQCdTWjqpsNhv4cCQIgpue3_nJnhZJDzJdecNIjPFr5aBFYZd6FOeLqO3CCnClPPYFK2-MPdDBvzGAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SH3S88YVf0wtWizmSDeD2jjZD26DVU3H2qwurJZstUTx2pjWmsJQs99bVMoHhlLbgskedP5sxX8FZanyLuDpy3S6z3Y8Gdsg8yTfZioHLkapjZHueSNzl25Y4kopA9cuCvX_ywi6xasK-bCDoULitAXhbgn6pQt1Za89r02igdyiM5oHXH6wbT9HGa96GkjthA3D3g4QpJPkybT26YHyOtVIWd8cY_XVWiyZSZ0-hXiEAasOYKJskoJu9m6nukZ7mW-B7NSFmVAOBW0r8PKB4LQ1EDFQdSVrCYn4DpTZwW6ekyzoGBgHc88vNS0zB2wntXBcYnmXyXawZKPJ5WjOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kHOHZ0lOr38JHwToeAkpXUFu2DAtb1cLq25Y06WYVXIQ7w-hcVoA91dLEouB0v04nKJgaePN7CBjGI6KfIerQwats9XTN028fCRy315HRdUuVAKUU0DNkELFzb5CN4SY4pUAIIGnmFUt-UM3D4nUoOqUpdw81ML10CGxK5A1H-TTYlbRX2-ULZ59KsKhqXRcKT_dSRlqcD65cFJjgAC-M8CixBIeDd_FTCIW9lkoUxpxcekUDSHO2OIFly8Kl7oxtOabP2xFydJA9zxOQmdajffUYxw-0ZEXCeaIPv2mI_-PGVomqLkw4Z4_5o95Q841DifRB-qXrPajeGxs2lOJTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ku0bME0JKr08XDbow93bKGIY2qit_jw-XzPDEDoFC3Vh77orWh0BnrEN2tIzu9ii8-Jy1Gl1E1s8URZTJ0mBkFIP7-Kb7_XXaWmAjvcoYoIBVtAvmx8b_YEAxQ3hhPEDSe-nU2DU-e-Xuym0T7HRbGxD4XMXulLsnty-Ct6bu04j15PZyYJzUa7Jcy-oqWdTBH47Rel1gbRCY5KW-7qAWUpzUkyyxDxhmIIRK1_4M5sMaWA7zQwaozERz4sPlA28_yghox2ZhkGCU5bruWTiULcwHp_gs-5bDUer47sFnwdoBSSFfgxIa_Ranj9M_FCFxT2mkB27zv-HIv1zhRVRpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS8PQAAtxbBKSJv8Iy_52C8NrQff7HoHiPoO0peDj3dOwjXClKncrSMgn5jKm_pwcagx7PPchr9wkI0m3QkDMStjFvUs0nCQc9LHIVDitc502PUXeVLIJNmwXi7IObXhQFSWAUaQCtdSC4v76vlxqqKATxUm0nOS-BqLy21mJ10uUYcG-X5U6xcckR7z0FPjlHidbwolDZ_CkTOxjh4ZzmAPQboZp3gYEJQ-LHpwPlve6HaNCeCjawmSRzAvfcmsJG1YmdXk7mZF6X0rAhvbn9IsJaWEAhK9PyjGevv1q1JK8iFzw61ug8KsDqUoeHDEcN0I-_z6Jitdd-BUfMdg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijO-40Srp3dI--YkFqT-FyW7lzbpUL6zAsevpsvAMwQ3Xswmxtu8FAyu4xMnitDhzVz8JzHx3cSX6MdWRBHkDVjfdg61T0FFJYrHIRXgFADn_kwxKD1TXllopm41ZPHwyZZXSwyA3PYRNMPuC1BND5h9M-LeliXBURS3SawQYKE1HxVSwdRhAbOwJVMVKuLWCQsIzQc2z2dHLfTqgdOq3WjQ-J0Y8vNVuSEysZOXSdJU7TORk7EDoUdat2rpNb-VO7x1_E6Y5pc_-jPcC7CP81WBsUAKrigCw6ZFMWRQwymQ5u5sc3UBifRIGOkNpfG78kjMzyBblYWNbn34o8KVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM7lYRYfrG11ZxrIBd4dxdJgxa_qCLkGHSHwUHQCrDCG6UNDa4S227oqZQJzzDQ8mgVl_ISpApm3KPYhM-59Yw6rJoDFipe4ZtGSvZTONieAhz8dAKLULdDbRMnN0SDgGcy5-a3YTmWT3gkB6WzZ1kj2Es6TM_gbeULMc09QIhSMX1RugBV5YyuomcZnqvM0YHSfMIAjL29xAr4NDUqWCc8KMp8bQMkUzpUM2ACCXhGjsa_5lVEm5lUGAtBdrFbK8CQ4bvEsQPtBzK-QuZHxhTrPkihx3Dbni4V4fOyhovTXbdX2yIxWKfkdoy9bun-vhfK3exZF2WAFosq6ewlMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjcjz-wZB0k0lzH0TnqqaPzmx55u36dXRvyW21qH6SQ-BRadUfTUlxBuh_s4f9HLriNlQmnMX5d7l4manlRxsPbV0PfCDiGRt3Rkfln8ux-0pKHvdP7VR0A64Wga0DtQyn4D1rQ17bn4r5ZyhNjtkI4B-Kf-_eRrOa3o7dzm277I3zcRKWftswqw5V94Sw8_ilcViZ3l5AndsasdBHLho88KwBd70LYlaQbEZRYFUuIdpzHKtygCvXGx-VMWDRNZatXTFL_wRqo-nhfNVcnTVKAke-kuBq1mFIqb3Z9Il-Q8dBCzEhveKlS9CnuGaq8JVRm16lPl3BsExlbhVyAyKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRCJbIKFLlG3ui3dZ_oYB6MQTpjuEtJDNOC_J5tkpY0f5o5gpjoK_uJhJYbKW5ltlXlUxeXKjqToG-8QJY7yxEKvX8J9hSoitftQXLcIC2kC2cnf_6DsTJIVnuGrdPW8RjJFCUiNMvcYAXTnCW2tQUdkinHsjKzrJ9jx9UKExKUQ8l4QdEYKryyxiBajbozK5JG_uVhDEAmVnjePeFJLKmIzLLzV5qR0ykOpPIRXpvVyu4cU0p76f_R-cts6RkXfVqU1OoCXQjabNUHW-f6qcPa_WWbHpLpDTNZJgb235HFSo8Gd6GNYpwAVAW5nUWVhpG9H1ESDs4vxuuFEm3pckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ouf7rMMN0KqxJ_Ke3qVW-oCade1ZWxKGr8F5tVEy3Uu46Urj-3qgYmfqnMaQW6WZbeM8eNWiLobdNplwh8VWKZdhbzK-n_z-E2HbZyNRZ7en1tCn8lXbC0zF4uWfqnTxviUQysJAlAGuTKpg4aFx6jYVxllnb1ML8yZQMFZHGYzNLZgITVGRCllR-VCpwlrjV_0b4hwkXjf8uoHKgK9LgaDDZZl06Rzg92BfeHluImx-qChM3PYe2gHRt_VIhI5MKnE-6ey889CQ5Ff_3RSflFCpAejHQ7B8xeKEMUS35gwVBKucHYLpYNDsHP4ccZyRoUnB7emCeA7wjtjG8sO1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHwEBGbn7IDPNv7_SAb2mEz7Z2zbWpI33VKEldgUVi2Ul_Bgg-9voqp3pb_geGPcN2kSLvvI6U7B6nhiIsWnpod3kDe-ckDHPD8dPJy8Xs_7Gn4x7dnZKGWvQBihXyRvh7RxdiY-Xb1sdEvKvWgiLOYOS_5NpW9uZYt9XJ-k9PYKvyf__ZU6tjWkBEIY9LNMV6UE4-veTI3I0bWIck-2jEGMRjiz3aA5fLn9HPC96NX11BUQlTI0NCGUt1nsZe70GUaD8kF9F66TQulTCFZnpFDyy9Tf9ES1UKusz5bUu5aoFibcBJ2fFi0cP4l7FLzEH6NWg-s83t9wJxpPgpvvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkiCh6oIUmfVMxl80j6p7KCP_jakeDtalrP_QH5rL8FQlCmAFQdUkW5AXpWr6UNoUdvK5dTHasVsj9tWl24q7d5-O9sOncuRC5AAXyjtipn2MKGYP4K8u96fF8-imVZK-m8QlWTJkpUNXpxTQVyAYYlNxEZzsEI6F_uNzQBTPvleq3r6-MtBxrhZFs8Y3Fl8EGkzWgJF3UKILNzvMWhxE3UudHl5FSzE2RzkK-N6BZZV6RchJRMbFIbAOkRdd0lPFt-NsbniRk1Pp9Rw2bAxwOenleFFv4LNXyBnlzjHetTa3D2NE0wLaXLMWUKMEs_rvljooyIbisrcUBeyryfubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=ONx-k1_DRYcBNiJIlt9auVzBsTb1A_YSAcoEletpDeETdGmlTeOkvt9DdI7luEU-gBae4RbOOUGJilnlg-97keRy4V4DY9z28SfSsuwQ8SIdxy0Mf2d-yxXfA8eIpAU7P9A2ECAIDGqQxUOgy897YVssle1Lk-MktTcYGKerz4qHQdP_9GjF4lJtzeB4yPdW80kroaZxxADsiiWLVlgnudLKiG3BotGdcZmkoYstLjz1_oLSw0NfDmGGMZMus0H2aI_g9eYJFlhVA3OB_sxXA_4vDmxnCO-HqJ8bCCOXnmRzNL4P0_cN_2xQO5pv3vfkC1y1_oZ0G2jNzH33B9IfAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=ONx-k1_DRYcBNiJIlt9auVzBsTb1A_YSAcoEletpDeETdGmlTeOkvt9DdI7luEU-gBae4RbOOUGJilnlg-97keRy4V4DY9z28SfSsuwQ8SIdxy0Mf2d-yxXfA8eIpAU7P9A2ECAIDGqQxUOgy897YVssle1Lk-MktTcYGKerz4qHQdP_9GjF4lJtzeB4yPdW80kroaZxxADsiiWLVlgnudLKiG3BotGdcZmkoYstLjz1_oLSw0NfDmGGMZMus0H2aI_g9eYJFlhVA3OB_sxXA_4vDmxnCO-HqJ8bCCOXnmRzNL4P0_cN_2xQO5pv3vfkC1y1_oZ0G2jNzH33B9IfAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3CACZeAEK7J5gpuUICinFEBp797KaRTVt7pYJGd7cFq4rqEBckTHdM_tSzA-gDPD-_POwwBrK0LUOWslZJ3TIsrTaa2ar09kUX-cec3GOY6ucxDp37XIAbT2WZeYr3M6OrDty1AqurDgp5PVthB74iAHqqUsHb7E-QuHws0VIKgbFVUTHJyy4hpe14FJ5-yjXcUxySHbuD_yy3arXEqEdUH3PHEDrR8NyA3gE8Kjo3KSiqYQlac1_IKXGxCkW9sMC8jnS0OIMtSKygWC_MLI_4H1PE-GPS1x4HOMhkXDhr2heOPhMo-t4o2dmalZU6h5GmJXBlyiXgL6JSA_go7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=rQgQSyCpjtQ8VG5NquNGpQVBoPi7eZ0x78AvSNI-SS_aLCSDeIM9xox1xQURo7QH4-eYFURBi1HVqhi27eUFlJ1tEdnRYGKr_-ymzMyAx_4F_-51n8GSZXkSmkc5Q1O3B-fyvygd-Jq1CHztuTwuqX_Wb-XPZBkYykQp_nh3yokeknBZek5UyX7gIJ94eRYwfZn_0yOgdMPhTTMd26kOm0G2kpFgJCx6GokdLuOhHXiq8lSm3N4gtmkvvZ-FIQuzDSX-bij-5TO_8r_z4AgvAx3jgUD59aCieAxFZWM54AqE8M6_TP8o1Sp09reGUvT6H7tbROi3Qi6ESbjAhKGHag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=rQgQSyCpjtQ8VG5NquNGpQVBoPi7eZ0x78AvSNI-SS_aLCSDeIM9xox1xQURo7QH4-eYFURBi1HVqhi27eUFlJ1tEdnRYGKr_-ymzMyAx_4F_-51n8GSZXkSmkc5Q1O3B-fyvygd-Jq1CHztuTwuqX_Wb-XPZBkYykQp_nh3yokeknBZek5UyX7gIJ94eRYwfZn_0yOgdMPhTTMd26kOm0G2kpFgJCx6GokdLuOhHXiq8lSm3N4gtmkvvZ-FIQuzDSX-bij-5TO_8r_z4AgvAx3jgUD59aCieAxFZWM54AqE8M6_TP8o1Sp09reGUvT6H7tbROi3Qi6ESbjAhKGHag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=W5DmVINXI4398vyN2XJP7VLP3nzXmHDJsNnNyyk4eLbXAbM8t5RSOtfZ-Sd6fSLZ2DBLwqqNJtSPKCsCM5ZVqsfkNV_lWaNFCwCDTSlS7Xqxhq5mrk_fKhcWRpHVT3NHgQ5i10gc2WqNmNQk5Sbqf9e3ic3MLf8xOJcdWXKV2K6L178zgMrm5bvA7bT2zFZjpxN_ZX4cfHw915Aa-nsYEILeJFT0B4qbJpsFJCX9HukRSD3ZkFXjlgP5XOS5NUhXL4ys3KvJV7cq0xeXyOUK3Rx5B9z9ZDvcEm3goZrkvzZasEicTyeo0hh7ZajxAq3Fwqa02sNqbzDI7gntPIP3GF76aQ4EWlmE6ItxtWK9FRnyuUIpNlWgpkTSX_J496Wa53uav_0H8IH1GXahWl85PeJwRZqU1HhqOJutSn4WCPW1pTiIn6x3Qktk4ma1z5kZ2F6AHNQXnEqQOhCUzfPlizq_ej1coS5bOj0U1i_dmOYcGTzftCYibvuGAYPIcKt13z-NOPImxu815jnNiECG2l9sJaZ-MdYFppRcHAg5ChvW2fgp5eph0K1Z_lO_MFB3qs3WZmpPPPh1lWm-Z79i77-cbHn_oXoQfds85mo1eKvTzh8tPgRqAcLEW68YiFrfWez-8WlRR_OIlI4VQMPkSdmWBoHaMeHDDjyDxW3nArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=W5DmVINXI4398vyN2XJP7VLP3nzXmHDJsNnNyyk4eLbXAbM8t5RSOtfZ-Sd6fSLZ2DBLwqqNJtSPKCsCM5ZVqsfkNV_lWaNFCwCDTSlS7Xqxhq5mrk_fKhcWRpHVT3NHgQ5i10gc2WqNmNQk5Sbqf9e3ic3MLf8xOJcdWXKV2K6L178zgMrm5bvA7bT2zFZjpxN_ZX4cfHw915Aa-nsYEILeJFT0B4qbJpsFJCX9HukRSD3ZkFXjlgP5XOS5NUhXL4ys3KvJV7cq0xeXyOUK3Rx5B9z9ZDvcEm3goZrkvzZasEicTyeo0hh7ZajxAq3Fwqa02sNqbzDI7gntPIP3GF76aQ4EWlmE6ItxtWK9FRnyuUIpNlWgpkTSX_J496Wa53uav_0H8IH1GXahWl85PeJwRZqU1HhqOJutSn4WCPW1pTiIn6x3Qktk4ma1z5kZ2F6AHNQXnEqQOhCUzfPlizq_ej1coS5bOj0U1i_dmOYcGTzftCYibvuGAYPIcKt13z-NOPImxu815jnNiECG2l9sJaZ-MdYFppRcHAg5ChvW2fgp5eph0K1Z_lO_MFB3qs3WZmpPPPh1lWm-Z79i77-cbHn_oXoQfds85mo1eKvTzh8tPgRqAcLEW68YiFrfWez-8WlRR_OIlI4VQMPkSdmWBoHaMeHDDjyDxW3nArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOghFvTQlin_1ckeATXuE0PgwsRnSznybbPTRT6yLXqGwhnTVSffVRlE7vX9Iw74FWRwwcmNHQtcQIicdSwxnsGv-zafZLh4WmfWzuDD_9MuG3TWztdJkRIPXm1gzOP8alp6wc0721dAFhF56lhZ_Jh6G19lL-V24hlPfd8oThTnDUuS1b2FM6VtupdRS3MxnJ_XGZ1WJX7nZ4BvnBZRgwG8dcooLxvARCk1XVKSlH_g2UH23t9peTA5tQ7qa_8AG5Wh39xF0cpak6BSF7g9bW8wS4lHwxn5A1VnJIUgnPiPhaD03U7zjux_kURdzghJHlIHXbiT7hCYcOS8C1_3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=FmWrRm3AiwYUEi_yysVM-Eu90ECno24tdItMH3hvNEjfdqIWyfVHauevCGX_7Pohl7JwR5Rko96NMwhBhq0kyFTu20pOa_FwIqpnhFlzAeYzwOCxzB2Gysdg3GsVwmFaQ9Rqv5ciPzJT1oYTNDup_CL8gkRaEIKNg3Z8b2sVnS-zDcy0OUSsyCz2WyUhnIY1CxlkDeB3lng3uFjbvLBK9_6u0bTIhaNEq6_ZwMO9vTEVNLfEYB1lM5nEULM2fvgX_vMvakUuaz66DpIT3RvMaEYJY3-Z5Ux7tQqDouDOK80zVTyFIAUOsWgGNbW4GKptWLcYanmgK8UqLyMle7JSfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=FmWrRm3AiwYUEi_yysVM-Eu90ECno24tdItMH3hvNEjfdqIWyfVHauevCGX_7Pohl7JwR5Rko96NMwhBhq0kyFTu20pOa_FwIqpnhFlzAeYzwOCxzB2Gysdg3GsVwmFaQ9Rqv5ciPzJT1oYTNDup_CL8gkRaEIKNg3Z8b2sVnS-zDcy0OUSsyCz2WyUhnIY1CxlkDeB3lng3uFjbvLBK9_6u0bTIhaNEq6_ZwMO9vTEVNLfEYB1lM5nEULM2fvgX_vMvakUuaz66DpIT3RvMaEYJY3-Z5Ux7tQqDouDOK80zVTyFIAUOsWgGNbW4GKptWLcYanmgK8UqLyMle7JSfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=aky654E-TZbPr24dJIN0yQaQv8eQa9Qvcu5UhsxxRvyUnAKc0C_x27EiS2dvPxMohu8FDoeACswrlZWm72TBZyQwow4dtvG9ZjwbjOfaW9FxVNMJRhy8YbkVKlCgChwk3FGTWCKTcXppH2y8FD3_2tHdRY7sqqLnviQjf16A6MnW1j07PRN7sr624wSENVW0CtXiQEGx3Y-fdnG26R9AnqqVFKAPZGU5_MYKVuT1K2JN6Yc4CyIMl2kczA_kRCt49I6hA63Xjtum9_CHy85PdlruG8ZWgcqjF9wL6mz1pno9e9E7z36ryBqlkcod53yhWTtCsOfh6TSOjRozH-PeFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=aky654E-TZbPr24dJIN0yQaQv8eQa9Qvcu5UhsxxRvyUnAKc0C_x27EiS2dvPxMohu8FDoeACswrlZWm72TBZyQwow4dtvG9ZjwbjOfaW9FxVNMJRhy8YbkVKlCgChwk3FGTWCKTcXppH2y8FD3_2tHdRY7sqqLnviQjf16A6MnW1j07PRN7sr624wSENVW0CtXiQEGx3Y-fdnG26R9AnqqVFKAPZGU5_MYKVuT1K2JN6Yc4CyIMl2kczA_kRCt49I6hA63Xjtum9_CHy85PdlruG8ZWgcqjF9wL6mz1pno9e9E7z36ryBqlkcod53yhWTtCsOfh6TSOjRozH-PeFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBbV3ezlMKSdJVC4lsorHWqwAqi5-ae3a31BFnykKyK9XFuVv2t2nmLy9DeELCAZENEDDq8ZkLtAoyxiR3rEnfUNDLZ2BsIG6E5wAwfJBHAX7xujX1I8PPuikta_Ti8FEBs_GSLTV97sYISn2IPXHRh41I96DJiDmxp10FNNfRYhdc8VxuaieOzRAXh4bd28E0m6KJybeVmkWFIFAbY1aFI4BA0zzPzQPlwHw1R9jOsDVMPbMJ2F5mNSLNTj4C5jnXG_1TUhBFZBZJXPXHJPx82t8RAVrbpFQFccR2J5-Vqr2AQXjX0cnii-B-S5iJa84PgAfQHrvm2HnG1_tST9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=LwonMV0pQO0Q4RFdgmcUBd74QpE2W1EyH9XkxOj3Rzk3aW5-qEVDMufKaa3r6_XMYTBwip6gYZtuG8asRULF9W2I1raMEIWHB5gvhMQ80blc5qN_0G3Fmhjtbn8nAAlTpzBh1tuigUFepKWmml4yIhYbxdINJa9ZADQNBvusILM6FLx5dfxdQyGuNBTOmkIZcYNXUEKl0LEqhqKnhxJ19KfPCMxZUYduxUxkbA8ygnDJuJ23ljsv7frFT0lHVkaYROvDpTI5x3bcqv8Dm9MFnNxUEBmS9keuIwksBIuxJHmR6X2565tj3PA1QZjkP_YAxK9I6JnNRmCL00_CtAbdyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=LwonMV0pQO0Q4RFdgmcUBd74QpE2W1EyH9XkxOj3Rzk3aW5-qEVDMufKaa3r6_XMYTBwip6gYZtuG8asRULF9W2I1raMEIWHB5gvhMQ80blc5qN_0G3Fmhjtbn8nAAlTpzBh1tuigUFepKWmml4yIhYbxdINJa9ZADQNBvusILM6FLx5dfxdQyGuNBTOmkIZcYNXUEKl0LEqhqKnhxJ19KfPCMxZUYduxUxkbA8ygnDJuJ23ljsv7frFT0lHVkaYROvDpTI5x3bcqv8Dm9MFnNxUEBmS9keuIwksBIuxJHmR6X2565tj3PA1QZjkP_YAxK9I6JnNRmCL00_CtAbdyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDpSJ2xW31yCoSAF6Lad8bCmoETlEih93QC_4GbkvUO_vZqx_on5QLKFTmp5h1uyEBbzGSg2XiedfOj4pXNokkcm--Ek3RF77ZsBREWBgiEW_ITV-caW0MztswZH3MZXgQCsn0cC_aWdtHTwKDJDsGs94K_Rm74SAqbSNVfMpBa7-VYKc1MBuRu854YSnuTg_gMwwBehtRBzadNfq2-4EXLg_i8yoLgVpnWkATcJfU8Ix_nAZMW89U8GeLqtMMVpzu6qYAafeD3MIW_R22VVMvvzplIsfuGqCdkWusg6aPEcgrLCWfYGuzY--sM9ZDIoo_jwmDajcAXYddj5poXeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=SMvo1_s8MCCmtn-PkD8b8E8EplQP8je_8nKRaQYe8xLaFHhrdn3Dr-GXvxC1llysvw8zVZlS7Ir71PZ8DeEr3tGRuLx1GKWkCan9SUjEi7EGziElK4EgygGj75hoPK8uMRyQfv51Ef7Q6-itul6KJQJVi3P399HQzs5Lr0cm1OWFCZVanV6UkQNzJmRZEg4PT7CAJWaUzcOP32M5anT1-lUWyCEXg0RXZtdMV7r1V4NV0wD9K4iIeZM0sasDgTe2KrTeCz6PnjnL-65fTaocahGM7eMkJvvbAudi_sojxlkJlAtkCqdGs_08VTK-lxZofvR--uWvCRKwqOXJqqikxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=SMvo1_s8MCCmtn-PkD8b8E8EplQP8je_8nKRaQYe8xLaFHhrdn3Dr-GXvxC1llysvw8zVZlS7Ir71PZ8DeEr3tGRuLx1GKWkCan9SUjEi7EGziElK4EgygGj75hoPK8uMRyQfv51Ef7Q6-itul6KJQJVi3P399HQzs5Lr0cm1OWFCZVanV6UkQNzJmRZEg4PT7CAJWaUzcOP32M5anT1-lUWyCEXg0RXZtdMV7r1V4NV0wD9K4iIeZM0sasDgTe2KrTeCz6PnjnL-65fTaocahGM7eMkJvvbAudi_sojxlkJlAtkCqdGs_08VTK-lxZofvR--uWvCRKwqOXJqqikxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enNZ46FRfTKP0Gv8IMmKSh9-nFfBwxA4XymoBodO2sZb_opHTtwfyKHy0PUUECo6GPNIdxeAaahkqtpDsWufSiOj-NavaI43jWZiu7ij86dhY9h_sDqqStDJVH-IIGON6IvGAkifj2xNUku_0k80ePlRmDU_kHtrob3wVSpZjEgwSvE5U75a1i2x9umcOeIbw5Pa-oae6ylZqZBiDpqII0kVL1cHNq1Yz2JhGcWWardlWWwPZXz2NAVJGRL738JXU-ENQl3PcKOWCtBrHF-CU3nP8M37p4L5EnXvu4NJSYjjPinmj10O5cqAbAJj-LXuIahMJzw-iPG44uXXiljDrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb87qfcGSIcEvkv0wzJlGFcDbNEnleY45u0LOd7Sq_6Bhy1wqXakIWzm3z9wWTlIZOPp98WXhRrPlkdNoJE_uWeRXpOxndQmhNkDzGacrjtv3pm9dQ-7PFxnwgdfiy_NZdnuq08GN4FtqqEoas8JCy2FFkWJDrEyXnFIhEf04ElJiz1NZkCcvD7y8MaVFQNDpslos0k4RaYkmwv-8a2IZgx0vHhXxSN3lpzwHqar2G_omSiLOwKqIk-pGP35T2WzAXXQvglxagpxqzpeBxR0-wxD-lbw7Heaww9BNI3R0YS0Tw3mCfbT0epTBMmEuUgKeK_06MDFF1mDZb1J9H2Dlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czlQbMsQ8bxI9xuLQ-munPL3ph4coCzlJousgeB-6S6LA93IzV3x-Ux-9a2BMspWpekk2u6mytaIFtv7bF4itC3WlGKJ8W7S8K9ecmIMd9toM4fXB6DJPwvcIlr-zA7FrN6lOuCFB8F1doftpv412yKZRFeLqv0U333QM1Y6rztAJMRpN9PHd-Y2GA7BF7GngokFSxwU7ajkSE_59iYcEKUn_ZX4PQUeoj4Pey-5KvGg_dea7p1SFdQTsfEt0wBVRRYqyMkEVy8G5bwDEOvW44eYs4KZfNOds267dsykUcLxy8ayF55xK8RE-ASkNJ-Pb_aH5cMw_PGyW7Pyw0Qv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی:
ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف میدم و روی نیمکت تیم ملی دربازی هفته اول جام جهانی مقابل نیوزیلند نمشینم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25659" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25658">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM3EKk1QmrtTIgmny_p9YHPpWFbgho6v8Pay9XBofh3JubqWLJ2ypO3sG5i49TZKjreVQD4caHJGtiE1zWh-h5aCU29GpOjMpneGHU5P3-Ey4oNgirlN454V_mFsaygT9KD3pG1znGW-yor3ZP4xxUM4QAFvZ4RjsuYj2OoNISs-UMh4y4r9KduTUmn-35CRIatz2w-KLfLuInHBtVt8SJfDrcqS-JU8PYFQrBHXJtDR0wMUgLRNnsE6tA7XIJcXHaLBIDL1AqsVYk-KYvwTVxuT9JiPgihihWp4EKQ8TdbFZrWb5d8BHdt563UqvRNQYm5Zpc21xBpneezuUCrwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
5 داور نامزد اصلی قضاوت مسابقه فینال رقابت های جام جهانی؛ علیرضا فغانی در رتبه سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25658" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25657">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=JYBWBGIWghJep3FaAKKQ5Fp5XX9U4SncwAlRymbX9FfW1iAfr1yhdWrwLboZnUJFvVuGtXS5j1-X8W-CVkbZkTpIz-NmOXDNiTVJdgzTR_X9RlBaGeNzlzdfVT-KW9i17pWwv3ehrsUqMe8kolRDcRclkki23UdJCSted_I5Omgixkq8UB-UxBrhv6NE0301tEIZJKh88QOSUmml0rT-_A-fg12idqY60uwPGNNnV6rUF9hATo1y-wO1axLcgjs14gL4qplEQSJjwU5Zx1RL4cFtMYIU342M_IcV-uQcUCHo4f9I6OHMP8z5_7k1eCKiFdda1tHHl42YCj6pqb3-Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=JYBWBGIWghJep3FaAKKQ5Fp5XX9U4SncwAlRymbX9FfW1iAfr1yhdWrwLboZnUJFvVuGtXS5j1-X8W-CVkbZkTpIz-NmOXDNiTVJdgzTR_X9RlBaGeNzlzdfVT-KW9i17pWwv3ehrsUqMe8kolRDcRclkki23UdJCSted_I5Omgixkq8UB-UxBrhv6NE0301tEIZJKh88QOSUmml0rT-_A-fg12idqY60uwPGNNnV6rUF9hATo1y-wO1axLcgjs14gL4qplEQSJjwU5Zx1RL4cFtMYIU342M_IcV-uQcUCHo4f9I6OHMP8z5_7k1eCKiFdda1tHHl42YCj6pqb3-Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25657" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=R8nn7W0mTBTBw-vnAq8un0acqMmZFyS3GA9cP0dsfNZNKvD3S2_Hqpthqh8P3hLr7g0uZ6wDik-rqdQb4xU9SmKkKpafHRaEwM3aSNT60SAXhQOwvQDo2d2A9EZjGxfJuyPRbvmoSjMdPLvMOqzAIFUA08HxiZ6jeWvNB7CqMxp0cFxG-R4-hExJcax47BMWlOvh1wTvBViwfnAmq_FvLxlpnCy4iamYHi5--Lgfk8P6RzK5WWdbyk4XH_9865AiG8MccBFtr4Q-7wTzdddRKcpI5b9Wpbtvaiiu_yuUtm9o5SAndzA0llrUqwc9EwonbCeVNBr2Xpv1cza99leUCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=R8nn7W0mTBTBw-vnAq8un0acqMmZFyS3GA9cP0dsfNZNKvD3S2_Hqpthqh8P3hLr7g0uZ6wDik-rqdQb4xU9SmKkKpafHRaEwM3aSNT60SAXhQOwvQDo2d2A9EZjGxfJuyPRbvmoSjMdPLvMOqzAIFUA08HxiZ6jeWvNB7CqMxp0cFxG-R4-hExJcax47BMWlOvh1wTvBViwfnAmq_FvLxlpnCy4iamYHi5--Lgfk8P6RzK5WWdbyk4XH_9865AiG8MccBFtr4Q-7wTzdddRKcpI5b9Wpbtvaiiu_yuUtm9o5SAndzA0llrUqwc9EwonbCeVNBr2Xpv1cza99leUCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسری طاهری مهاجم جدید نساجی:
من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25656" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25655">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaBlJPB4PMHfbxH_igUdIbDbH9GcPelnJJMykxEmh_II8v5nnxuEO8YiRDhHiJpqmKiC5GeoGHWOOip7VVZ7uXOxVzsQ0e5Ko6SoyyNOcRwX05stMS-ggOdW0Z_Yq1JiUsvcKWqeI6ejo8b0ShaB62WZLVe1czBBMwXvoejhYhtShUeis9aE0OZJGVW6jfymgTVQ6Mszdu0yo7ehG_hHyA2kqXimIxuDeE5Iy1Pg57Y6DR_O5Wl5Pt5yhj_sQrVEseh20-bv8hbGbj-yiuoqWrPr4KGWWgZQ7AzUXNiRLHIFGN-AZPp1dJ16m7I6EruE-JaZWjoBWaOI0tQyoRHu8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25655" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25654">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=PkCtT-v_8Bh478eGukRliTOYkj9YppeVlbrPZH6ojjkDWU9WnGpCXZYPSR0lJEC5Xn2da8nBtnQqiOoipA68hDgpRWFDUy7qqP5ZxFK2B3IZVmZVLMM7lFgWmw8MkUOF_HM1ErtQ2z9Ur7VX20ljcodm-OAE800oPLxtXqszlHAJ06-PpDJzZBsC4_ZUhaOpmbGTbAQ0JhymXyZW2wSpSxjSbVk3yc5fUUlJFJR93s89_9F2NgDojKTiD9lsVDOjcbMVhr-pNMpw0PISTK-ogs9aNilA5v92AspU8D1ZnA4mHv24HMw1CUNxXOtel4HG6UknKjoexd0NX2drMqRTtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=PkCtT-v_8Bh478eGukRliTOYkj9YppeVlbrPZH6ojjkDWU9WnGpCXZYPSR0lJEC5Xn2da8nBtnQqiOoipA68hDgpRWFDUy7qqP5ZxFK2B3IZVmZVLMM7lFgWmw8MkUOF_HM1ErtQ2z9Ur7VX20ljcodm-OAE800oPLxtXqszlHAJ06-PpDJzZBsC4_ZUhaOpmbGTbAQ0JhymXyZW2wSpSxjSbVk3yc5fUUlJFJR93s89_9F2NgDojKTiD9lsVDOjcbMVhr-pNMpw0PISTK-ogs9aNilA5v92AspU8D1ZnA4mHv24HMw1CUNxXOtel4HG6UknKjoexd0NX2drMqRTtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ایسان اسلامی درخصوص درگیری شدید دوشب‌پیش جوادخیابانی
🆚
خداداد عزیزی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25654" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25653">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=o_4XZPulnGhtZEbyM9AwbSB8jKAv-09spANmadTfGOeH3Iz2PE9j49y-nacEsmYBLxVzpszlm-IfEMCUaeIPthsXqSyA16p1zc9j1DdjBnfy0NVwoRzJ0P3lUZ7mTk_yplfd84qMOLATyrdGWuoVpwF6VD_XkEuDOoG-9D26kVQqEPg4RJocd3g6wH-bIl7mSxLV1RtBAVsJ_YR8qU7njxFRAoL4a4Tx8mNLge6FfY-vZlW7M_MYvUQYUVh-KJn_z4vTwEPIwuwJRFuM3uhdyyn1-hwd57VNgvTrrffnHZDwlf0gPwZmUlyvgG44rsJy0xhvXPtjndB5PXnvFFUUVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=o_4XZPulnGhtZEbyM9AwbSB8jKAv-09spANmadTfGOeH3Iz2PE9j49y-nacEsmYBLxVzpszlm-IfEMCUaeIPthsXqSyA16p1zc9j1DdjBnfy0NVwoRzJ0P3lUZ7mTk_yplfd84qMOLATyrdGWuoVpwF6VD_XkEuDOoG-9D26kVQqEPg4RJocd3g6wH-bIl7mSxLV1RtBAVsJ_YR8qU7njxFRAoL4a4Tx8mNLge6FfY-vZlW7M_MYvUQYUVh-KJn_z4vTwEPIwuwJRFuM3uhdyyn1-hwd57VNgvTrrffnHZDwlf0gPwZmUlyvgG44rsJy0xhvXPtjndB5PXnvFFUUVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند: توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25653" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
