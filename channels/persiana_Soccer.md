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
<p>@persiana_Soccer • 👥 460K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 00:04:59</div>
<hr>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVCnBdSGyfz9SBe1g70_UQJ7vvYNpo_6nalvnGozjj8YHZQwYWJJdfQj4VRgwv2g_0bcc1GIp_AGUsI0GEqkK__n61tHtEfzt5LjnW3Sy9Uaf3iK2BHyAxRdN3CMFqAjx0rOhT4GFHBPpivfDOOc_a8pvododuvzjuBcsMhfvgledkqlSeRJ0DqAT4S2fSGMjKRyA-51fxeOY8L00u4cJTpdggMYbpljzK7YUFgeBW8ArYm5uF1n8bdZzPuC2BsqMfvNvcVUT1LsscmJQuuq015hG5mafkCClT0uhA2y2znaRAQLVCZNrzyNl2bhAfupv0VzOgVwVS37dbb5FVNRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vct-i5wFP8bD2Z_lRkGsP0EwnTss3ur7snb6IWMc-Oq2Tk3MpHE-71MjZJrA9thVyN-NbmCAoTVcfDtdSSZ2Agfjnio9YDeFPLlbuZGeuevO-1ff9K7wcOzDA4TLqBJxNQLpTf1kR_a_PWzXykazeb2p0HkXxr8iCCEstRuBmhbrUzuRMwCRqp-qW_1QudNbHRMM_gQm_hVAWKj3qGDgmaW9hS2aA4IMnN_Oxe0TSgHYnoVd643VyiII0N3URuyYgZr9b_YDtuiDXQLq39hPxf_WC1YPj2eR-NSrs1g_8kUxm0KNpUvwtNwn6IZlwiQjKhS51R8IrMxTiPsQUXp0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI4_h7lSGAvgX2ctnn6sbtbWrkaSydQR1lt-dmdHMXiOb6gzfEquYSvSykT6btRqTHmGWcBfyl08LPLYcS5BfTaFZ3ELRqBTcXiIwtTjG5TB6rjFcvWLJljtAs2iQ7lRokYlTsPJiworUB8LR-L2c8LR7xl1ok6tXs-qsROVTLWuWSEG89RfFFOjU0QVjnXT4M_9LofuAkmDNWdCW_TDPNDn1-wUmK-mY34sXUhSJ7PygWpKQY7KoxIPT7DUH3dXv3vsd4YRFcuwPSzW5tzPaCNlbwvaG8_GhaE5SDKr5wz-iXrZt8M0k77aDuTUSK6m9aAi-jbBRR4K2yX4-Ut0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpyfazw90cjJiHPDbB3M1XEyx7JANPaBWdIvrN8y60Vw2RguV8okAaWx6Ootwyaxi9i35A6If1W3WtELRzPiPB3vW0GRfum-BTUKcHsbjRaEo2h1bI_zX2Sz2puasvtqs-LCLde-0-UIQKCmIA0aP9iOWHfbCb5YlOi3yVWj1fSWjQ7eRDnt3mgN7a6i40JhMFqIWHLwb02EQfQkMH5GOasF2PeXnwS3tPUmRY9wlnwCz_mhz4RNBc__vVAnzpeNaiyKyFSBlZLgx9CwnNT9GdE7e9MDhFU9S4xF7J9znmcu7RTYA6nfO7I9ajnv-WhPhf9XQ0iFrpt0jxFHL0QMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AKPx_JngBhysLCwTpTzHbHytCDdVfAiJF9ST6ClMoY8dZ6GhRD0FOcGGXNU9x9AI5EgEzYTnoLlFfpR1Y8XgNJiPdBvhDtQqXXGKk6dsVGSs0UciTaLeuhdSwy8yr42FiKTrBrfVUJ8YGIEthk_Vrbljnmmr9NxQzM-mYwVN4aaG3TrQji-ClpNXmIATLLvFaGXxfPXLm5AbviuI4q7f2yAor5yp3G5iGPYfGLF0jShAgB76KbLOSvOeSfb3ao5vv56xnWCCxBI4kFXy6Bi7Wq3MJxflPVUzk5BYZU88YzTiD_qJgXI1GQc0wHxYZxFxzDU8K3CuqQrYULCUQYXvpEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AKPx_JngBhysLCwTpTzHbHytCDdVfAiJF9ST6ClMoY8dZ6GhRD0FOcGGXNU9x9AI5EgEzYTnoLlFfpR1Y8XgNJiPdBvhDtQqXXGKk6dsVGSs0UciTaLeuhdSwy8yr42FiKTrBrfVUJ8YGIEthk_Vrbljnmmr9NxQzM-mYwVN4aaG3TrQji-ClpNXmIATLLvFaGXxfPXLm5AbviuI4q7f2yAor5yp3G5iGPYfGLF0jShAgB76KbLOSvOeSfb3ao5vv56xnWCCxBI4kFXy6Bi7Wq3MJxflPVUzk5BYZU88YzTiD_qJgXI1GQc0wHxYZxFxzDU8K3CuqQrYULCUQYXvpEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=EqCgSJJL_R_ifA17vZnZrAP43MKpnVEP0Nq6ZxKWcLitDXEBmd10nZK7yWyg19674tIl56w3463XR-kNkmmCbHdoQK1wwaKzPJb26Y6nsvduRc0PWzUgKOykMPW3lJggGlxyWZMQrxnVhNP253-aMU0F0jbXREoS3GZPD_QmuY3El3I9K4yX-R0Y33T-USheHKxknqqvE-5NHvdUxunjIX4BURJ00sjWwhWdV8ZJFL1KJWmAVSu9XFGiZzCq-Zzlfm4tNOVVQ-V4iAeofnmUvQbaF2QEjywaYjyQc3f4eWHut7zgE6aiKLPKPEoNQN3zDbwOIdkTXchFysgRW82-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=EqCgSJJL_R_ifA17vZnZrAP43MKpnVEP0Nq6ZxKWcLitDXEBmd10nZK7yWyg19674tIl56w3463XR-kNkmmCbHdoQK1wwaKzPJb26Y6nsvduRc0PWzUgKOykMPW3lJggGlxyWZMQrxnVhNP253-aMU0F0jbXREoS3GZPD_QmuY3El3I9K4yX-R0Y33T-USheHKxknqqvE-5NHvdUxunjIX4BURJ00sjWwhWdV8ZJFL1KJWmAVSu9XFGiZzCq-Zzlfm4tNOVVQ-V4iAeofnmUvQbaF2QEjywaYjyQc3f4eWHut7zgE6aiKLPKPEoNQN3zDbwOIdkTXchFysgRW82-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u59DIGH5jfYOFKVbSD7FlithfWTbaVn89eDHhrsG_VbFXaiHYDhlk2E1IeXPyi4WRkC0kqLkbl-5Ve9cGOPDs8A5L51uvKVZ1Ut680dqyCkwef2T-bZ6phsgH7_BIEvq43y53oku0icAANAGQmnfprDi97USiMyRJDx0f-xxSMlNwI64T5XbB4mEuBaUG2fkQlwjW8TvsA1BS_6eEFvFiQsLkBVtjBCvAxr2VTlzeoAYrlCdNxYwZhUI9uf-X_c2YWFeuZvK47vJcmwnS6U0hSybzU5P4PmMRWEFH8OJfHxcQbAkXi_ILj-_w1-k14PXLg6e9i-OH03Jh8ZWxhNe2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqESK59AIQSqGUQlvn0YCu1GMQWYzhIoTi4PW48LXRtUNsHMQFPPhhpqxbY0jbOFskRKvQbiVk20WmbURFY1TxTShytTtrfTb4rr2oLQszf5oolDuaM-TFuT6YtRX_rrFbDAMwRCa8dyeTb4NnN_kmgQb_FUCjAWMxC-qz3hh2UogE0X3tD69v-OlO6ahyiVZHuN-3oJVUUdJGHyEwFG13e_6doNl7BTOA645WRm6tPLdMxghRmNemmOWbZvUISzBGeg81KswnYdzO8EKCMYufXY8Sg5fo6s6GrPfXLP7e-fXOyAHEwxVm-khNXeC7-22Nj4nn7SY0TA8QISfBBVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrVw6FjPV_GUkuK4wGuOiaR3gK46Pq-Hx3NuI2PhmSuByFddfXL3VP9Qd_vzFXg0HwwT4g77s0azjyh6lPqWsD8DV9VTOKYZPVmTi28QnXHug6ecTJsVi5-_KUV4ntpWSxgtWM1XFzWcLd-kahnEsDBvACeq86ZSo893sG2ImDpnnd67_WPcOBIm-1Co8dKtfEur095hZ8piQMDnCsy8hFJ1cDnetxBcCUWmo7l3FfmoJSXqD4vwbuWqjlarGK02R-3RhdjtaFfi-wAExT0y4DLrEb1qE6IKc3vNnF-wLDiZMvwUr02DemS8YVRq2qAX2Uhmi38DzqmMB2Y-r4NFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-zgPegZARH6DWVgXz9UbRTG_Hx_kCKPlYZUmHTit8HDBUQ13vOTztPtlCYVg4tHiYB9Na458Bfwxetacnw2_Ee3-VdnteyRmnG2yX57vxGqiv1EMfU6aTFWPTLWPSFM2uzRz3ntiobWwIbEcMiJhrWygYRh6pFkQPGPRsWWg9_3vXT9VcvK7dZA-il8SqK3_hjGmgo1emeiAdikSXPbYBxY6HpCEPWW7M2vy-zHhMzu8WCFaR4WraVAdieRkQvxk0O6FRgvPW0uwfCtzLm2UudNgN8qK8Qs68T0pw86IOUxkIMgkg1jhEXjm_7YfkPYXooddsh7SOdSHpmLL4aMhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpQ0aEmAcPgq4-5xhU8gMVmP2XCtC4fN863Zx_HyBbPW66OFnvucLzA3M6bTB4SdVFTkia9XFSuRbhHZPX-XAaKHhwjtNHlBCTqpSTFQz7SR9bFlwBL34Hslx8mghc88hd73t-l2wJIk1il5FpWNJ9AbLguTopk1kW9QC2q2AJYhvig1k0ob9oUqxkYB3swqwJJtx03jFBDZiLBIBycMn-zcHxzgvcdnUobZMwRk1maALqap3hV8-76X83qpg81ujQTRrFyppToqiYo3rZxYGEskNg1UT7CutZ8TrCSaIiS83yY-GeyJZnkUzSPMx6bI_tN1kwN4dDVOrHYVcXOkUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMEXgwPCPw7O-ZskfCZVD8mBLyyd8keHGf7uJp2qp_A6wpHFHaYQ5D9OHpJeCOjSpDKHFwUOkIHAsz-pljjyqJUDqd4LGjy9nP1f-P_aTTMA2zqHhS2ZD3nX5BipTUKitfi-cN1oXFmJdk10nnTSvDDGd5SqbsALHwpVVmJSDzlYNiQ3yvL6zuqW742ctsSumvVzTjYV_eM2pVbqRdI8zvdXLZcwktgwYVXUyKPvHVxupzQjBbCOfMYbDCBgusKjBngTsk_Ag29FdF-mE5P5MhHlqulx07OX0YZsSFvQ6_kCvbvLQhHP6jM8jWNB72XM89XObu2Pt3lOEvSUrOa_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRXlTxKkcBYkWXPZYM35G9Uxhk_hq2_0_P0oECSQRC0tnBZmuvEd9Env7igLOg-1DRIJeY4N22wcZiY8K-4Q3qa7YZcm-PZS662uipMtNkzrNUs5RAwgzAtl5tVkic3Aa4Ket4_Y02qJMYjYi4vWQoFmGySnyWxaB6cjKjbBfyvuh3DMOqMbp94Wf2OJnNAsQZH_ob264i6lGakkzBJlxOithL5DzEmHZM4bIrmoSqqqseDSqvOYzjfZ_pxulGqurRF8TwAFI8l63IIlDwndBiPpZt13_deQXzpATrIzrI7kxo_1E3OevkbweTk2fs4Jip0qcack5BOl8M4aQmUniw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbtYseLdWufDRwclDg9ra3j5GDIia5JlODC-NA4B1PU28PLmCLchbNsbPzmMof37kGTm--0LtoIABlZm7Ob6GcpKBX7FS2ekZSSCk8UwZhDgxuA-SrMLDAn8qRDgnIVg9I95DAAGx2nsmHvhFS4yQjLE2fk0q0P64AWO2JcdaZWHDqcCoLxbDAwWe4orUylDwal6pc95RniFlzp5ZIkAPTJhP0G3shZZrteMIhpcqOG5L8xW4kBWSTDXDj7_bXD0-HnXu8nBDhUFzW_A5D5pQ-3u7155_OzSRuJlxoB4iwMbroFErXa1fP3p0FxBxWng5ZZ5ZV4qNMgs5seL8olsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVhN7eUFirKynwpzlxVYTajPrwU7zoQygdYkvLERLfju3tJAXLvnbSUZHPuaE8wsNN_kgnqLXcmwWZYFRAnQhb1N-hUAg5D02cCWEInPbFUI0d4s03S_4pXxHUCMUBoxgREimY-GidUw5CPVwcSbwLE0XEStL83vWJxXhSddGsC-fq_-u47IiXe69SGNBUvdvuZcfcQWqGoTO7_OE0Mehwcv_MNXdJNTPRgQmGQfE8npHSDv2eZ7tJ23m85_DE8J_RBr0kFmjTm4rgXvmTejnnvXhidvaoSN1dgsn12OE1oAQ0vIcLWOXjxedYaoNkg629oYxYSr2kg8rk7gwHT5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PipkfCB69lms6JTPn3-3Rs3GrdtprDN0FRTePGzhkiZm5IdkXjPiSw4iI7PKQp8fgDL94FKvVEwQyJr9aAAh2AqDHg0nGeGLEpvpjRJE1xYnP2VK_QHEp7kIxGuX6_YDS2l4bjBoBrbJA03_uPcJ706CRfTXX_cJVbcML1RWeYbRjHoWduwwoLim1mG9lc1Mlx5izEtyD9vq6SR78pLxh8WJvYvKu5j7znJ3viF3iW9LZ3kDwOeGVGaVgrfevAVt79NVAlWODrEQHkhcjNz24XD-T7imLhzOeVthlyWEn4gexpq7_HuCaHar5kCmhy4EqBpXq769TqY2zUM9Mt9_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=ius6dyI5YG4Kma4kEDRt8KHKgToBb0WlLz2ZX1alrtR8G7iz48lf38qooosznVM2kRr0iSr5GUkVVkTKmBK9fPtPa4ScMyWSyMl71pAz0ICMDkiem9We3U-Iaupr7rIJ8w3wG2bxsW_Qt7msUvHURzLv8F7wDyxdwnbia5fFB3YzFII1-joyxto0Ff3sXkR8k8BuAxvFWSXuMsK8xIjmztnl7ssdcTtp5t7x5c4MSuhab-fsCvTrP4SreJ11H-q8rIXUBYiHktSK9k0QIBiCMZI6Ql6DjgEJ-7tzYHvuCtjIw7_mlPqvImBsp_pp07c7Isfd9ETkNiu2ai5uZ8s67Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=ius6dyI5YG4Kma4kEDRt8KHKgToBb0WlLz2ZX1alrtR8G7iz48lf38qooosznVM2kRr0iSr5GUkVVkTKmBK9fPtPa4ScMyWSyMl71pAz0ICMDkiem9We3U-Iaupr7rIJ8w3wG2bxsW_Qt7msUvHURzLv8F7wDyxdwnbia5fFB3YzFII1-joyxto0Ff3sXkR8k8BuAxvFWSXuMsK8xIjmztnl7ssdcTtp5t7x5c4MSuhab-fsCvTrP4SreJ11H-q8rIXUBYiHktSK9k0QIBiCMZI6Ql6DjgEJ-7tzYHvuCtjIw7_mlPqvImBsp_pp07c7Isfd9ETkNiu2ai5uZ8s67Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obzQKmNs1eJ4LbI0Q4o0S3ybfDKY79dzELtiXC3nQw-km5B3AO_3Ov57iV-VS3mEIwpH_4GDXYGpzpNCI4jd-kd4Vg7h5jH6dALlaIaU-lvD_VcUye4XVSRcZx2F76hL3zxw0q8Bp5ivz0fztf1J2PTFIOV7JQAQNsc2r8a2BwRVOjodT9NMeRuYhMOdp9gY-UAHyYANc7csJMk-absBkRuJ7bpHcvC1quo-IHou8jZwr1t_KnZFT0q-QzJZ6eguiPLX6VuEnptaY8NNKZb11D0Jgr2xLK3bC8ykObpsvsTbMuU9Tm2VSsp4hw17wz-_3633WJvu9A_hsoF0wOryxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH48wKDkQvtoQ6g5k3YM5XGypYCiPRfk2UuX8lVDMvIskCFY8_L-sgu9JflJkQMd6H2C6lOLSftFgr4O2iLzRcNFW0Q0b9NA4wqZI5aA8x6oeOaQb4sIzCqA57aiVqmIsEioexDUGJ57DIxuQFJvI7-zw7zNUZYCAK_TChPuoUX8OmJbJuL1gVlz75bxFnGhwIy_KtapkWdR0JDqMPN3kd4gJ6N9HqMxS0eeep1o1HpV1SZq1PlwOc7BOgO1wSIdnYVJ2g7-E4ILoEDFkbdwdzdTjo51EodqQcaapxZRn9uaZvrg7VBnEwBEovXpf55ZWfUpREg9D8OosCHXrcyfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oh951LdfyGgH_bVXE2_IT8jfRngrt9IxEQE_ml5z7TWXf7Fo19NWUJ19e9LzbgmKiY6erJxmkip5ctU3892Ms6D74Lqr8ekUfoGb3Z-ba8TNAnBytBHjoNsUCBxwvTWprZfcfz2gubVvLYO8aoncfpDkcnvxJSjn2aWXrKvNAiCcRBRb-mH89X1UF1vc96OOo-vYkXOIxsOpZ9edTU5ElcuuvjdvRvYB-wTsuVaRCv9LCHyU6k4tmVOsYmleEPgbVhdNfi5bcfsPhejOVkK_0UBvevuQTp9pzLqahNw76RYgGI-MmWjgHbPhJDSQ8zVxDZfH0UjJezGkeR9WpuNaRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ4VuuJX86IZnwDx_gNlrVNs8XwWlCiDQbnydpKTYslzDNBv34gFa5_s7LilvIvrIPYzJIXgDdzDms4oVO0yb8eeb_sa-ed57pxgNwt44vz44y613YnBrnGfHSHNzMk8l0VsHHRoRxJt9068PgwQlG6yZDM4Ef4wRyx7iOsIxQrwu2HxZI3gIzZ3XNo-iMfl_TeFdbRfaFWcmZvTnSmHp4MeY4YhePHl4zWY68yOMMuli4lR-TpnyV7-LjfON6y3-_CHB6Vsv90UDkddo2TCcvYXMheclzstW34uq3KKrHqiDwy7h5qioZYtN2m2sK6_2fWTXtcIzT5ByCPQDzlK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eimQIYOmGkepOjYDH3rSdreqrhsnP52Ag3Eue66moK8nbioYst21x4daNXJ1pawMFpP2TBKrpGTsKrdqiljmrC-yJszobOlPrmH06r38whEUT6X9bB0uHVJoqeLd1F2g70LjiXnnb4rzWVr3bUi8EwVvlXM1Fw81MCMCQpQxWIBp-x7GZsFiWmaSjT8WPb9W1uo4lUBjVGAiSPQ3P5FAzUbf-FZ6u9VYGgum6oyXrymGrY0jI9IUw5P7mFPDN6WVe_5J9BkB7_QjBayGoYA2j7KdCdhPmLb9Y1Kj9nV3scsg8AY-uDSjwjl6DCkw9jk9Wu34EUv6m3gGheQmSlmLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-sfXlVuZQoodC7-z6i8qlQtP9DC-eu1k_VUW1R7wCEFtlvd-vFuyDJfUnRminFJq9osPTBGFUPiw8lJLqzC5pKBAZJrzgk3g6pgn_gdobCzTNPaaJA_JlalrDYe0cnvbh9yJICiMuW0Kh6q4sjldEKJXijE6W0nIDEcclNp5beDou3R_VDrV-93t3jlq16-rdGGSOoPfnJXwb5kDck2PzUcejiIt9T9QQuZ8Dr9eV0yWzwmnqnmbLFX-UyKx62gUBx-Lp9Fwpc8rDD16qbBsy0i5yqfIw9-1nuUIUJGKqpCiGpTmdMMD51YvhJTRKdx5HRH-PrZFuuc4UDro_mPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAqpsYOtATHNO_827NeugGBupsR5O4CTmrQgo1G-hyCUyKj0gJPZW8Au0xytNEodIsYplY2UxzWnLfeH1Ro5ulKi9aELG037kEhOIMocWi6vVGyzr6EYZD0qs8bWE2Lz2bvMCC_so3t3rZ0-2oRJju_a1rtZwROvzGOE6Em7g5opGE6efinfbX15VEZ2piDS_F4AUQV-WLfdJLbESqHEdBz9vbNmQExQ87m_MgTfqyT-7LvtJEhox7mZVUHCRKDnlc_10lSl2hIg9SV_I5d6f8vJgyYanIgRyURokr_n7Wc7d44tehg_gJF1buDZB07yBDjNKN5SWkj1WKYcTcIT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fclk5eTo_vO9IWpS1fsGQpOWfyRss9uIGOh2VWeUhNSHcF_9Ao6cXwPxbr4z5oTm7oFML2KDpIpWvZ1cXx9CL4qBbFgZyYkBQI8VUlBGmKauy_osO-i6xqvI9JJ2Ba78dNJ5DNBI_3Ct-f7tJ65Gf1TqmFe3J-UlT6jUquOpnrjvzrR_7dOIpkkfh_J4XruoN7eIF4g4AnEyB5jnxuT-8SG55OApvThi_iCzhfwIGgQvFKh2DoLr6LpIJH62XsDwsCRVUgB608oa_N74Bz45w-n-mrRlXNF3rL6wyg3u3WWJNe8Uo0OmB3jyuzRjDHlg3c_tmDYOHvVlgmVdFVgTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Muywc2SplhDS8u1EeYHrN5TezsJtEU273ggnEXPSx_B59VKMDF6deI8l2yNpbuetaatGa4wHQiTGd5VcQKnBR1xXueLW8Qx27Oh6kHTV_RxaZIjl9OUWAceyqXT_cda6UpuCLi0PcWrVsaLfaTWJLvQBHJsquHYazTbI02dH-uGGae3HiMrA2rqtxIyoacGZJrqKBJSTDJhEUJhGH_KX0rXIs93b2CnSrcvZASSqnKMEA2-lRrrXanVFjHoJIgw0ZbCAJkKp88UyhjEv7lS3xi4tOY4nj8XMJuhLgq7rN0jjfJ3mGKIQGS6DDeYqbtkt6G9NpXZeZAihwafVrRe97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7CIZ-ck0Hbi3nO373hf4lhTbPBo8mSm4WlCL3TpZQkbaJ72Eh_fy-qb3tdYf1sR-MUBzRBNZIyDQoAeK9XxqZiBPM0VwhilZhBwyBogrA_L9Ij8DQ326kfA29r5sB-C10wbFu-Pr5OaPpMVwxHY7pojKbaG1nqynt_Zu57CWz_RwqBIOC5-6u0f5bcfOBW0xEqkDr1kiFezlXyXbX4hSCvNq-8vV4UtnZVuCg9y3xgOpVSqPd3wEGhPlfHb8cY8gTM6QvSVocXwSW1U4tyfG3E2QBL5kDWijiQ0cf4enBMkNPtiCdCPTIud4vrfM4KsIvFl9QGRSU4GRoMT6bK9QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEGSA4pS1oT9c9RcMDAXA9p6nKOQUKlzwE1ISKVOjp6O8N1NZ7afmJTHd4pl5QscnloOfHZ2xPU4grk_lgMmiNEo-g_dLk6S9ItX9jlwLywEDM7_r0xftuWc_zuH6BAjlXuxVCgBkzEaxFTLUY4XhWWH557DqTv93_MydHSLvu-QTQqs5qxzqV6ZeifzE3FV_041uFB32QohyxWiRUMY342ZHSc_snvG-Pf-MtHHVgGpXzU0Tw3T-IbYklWid7-dpqoC3S17pBG04cl_n-iyjX2I7Q9wGlJhOoQyBTNLUvxNQbyLUjrwHKZ9ejKeG-Tih8DGBBj-kNJ0wbRk3xFbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3nAkhBmr3VAovE90MCx567n92djLUaEHfe2c_aOKo1n8HVIjg4jIZ4R5mgztSYh78hyWUb13sJ2S72fvOkrX_jVgKxKBs7AUROJpW9bh0bIHml-fvEi9CNIYiO3uaxyflphSm20i_dlqVyyNFq55-SFj6FEqgdmsngX-wBB0j3BYGr2DpiUxkWdYMZX1Mt4jfooVp_djEV7OdsEaoFHa94ptkf0YOc4w2RsCr0aOGOEmq4iExfehy0nTmfgjHiy4rGdrpigx0nFiTDy3_CWOCeAYI1Ad2ScIWsxDIS0uTT3ybRFYUJj2VZQUIVJ0nms3YA1d_h4gO5MlRM3jD8_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTRIQ1PWwkQiZLZvGPKYFRIX088iFAc9dddrJSzpF-hpjZfzM0gjd3q2-ZiWrEPkD2xzXFTOnYsiVvAiNqqQh9yaeQPAMovOn66mcizlNKk7BroImwfMOLGgQ_eNRrYecRlVmdwYWJZFUEc5lra92jypDVqcEoEqK82SQ6wgrW7A7e5OA6jw0HvgdPtGwHJM5DXSkHcbzptG6OKZtGlHa75YbyrC399UeCIH3bceCOAOIRDqUh_3vdKfMSoOWlmf23iueT1rjpvI7fmlNu0ICHkvs7Ii9RFSK_s0OXkeXXQu2Oi2coYZot2jdVSQvIOMnqBArCItseN5mQmFay1roA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AgXsmfcLjHUNmx7a0Ukd75E6koatQxOilYNMAyIcdeEh1HORPc73d8IObhw7qYuAsIuIKkpM5RjkBIhIYGbswpwon7Y2XAEQDiPfzEo1giKjrTo42E1vTjpF3h-Kr2VH9_l43bPDaLpvwLn7yjkRHiNMWn7fXH8hpgdoM0uBOJuGl_A2p96ZBUgAFg34l9iI8cb5TdMDEk2_SX9B3Tpm-WUe4_CHBRoAvOsoBd5-wcnHC5nUju2E3wwLC2FX91S4yRe-uFh2R4waCWIZovAbf9YMVVW4jWu1XSK6Ov2RsCEaoEhq3s8cdBbAb-pyQu3jPOhicJRbpWVBD4LMmPXPiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LU93bueojIzH9WopigVAG8hLWImvRbuak2wWnbf1FdoVZUi8oBoUHKSlhXs6ok13o_1Q7EgU-OTgeI-H9GuZUmVqqBBziS1HMA5IFJY-erUDgS59wiLGUK7UligTCV7UbzHJ_MxFKun7-PqNVNRGdVKBZRckLuhn5yc3O7lUaYAz0WlOHJL0DGaycnIAr90ZZywly6lIGsBVLPMZasyIVuQQjpCq7pmzYvBLxoYrsxOAk0dgXw2qqa0Jn0e60kL62S5eX-gnFDS9XmqemxB2DH2AErThgmIkwUx8cRsqMKofKZoIDOpe6delHX8rfc5wgFFI8GhcaoYmQNkj7sBWAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km4NDOKYuMZtikq5LTWwg9xxH32vH8i_1LB8HWCTZ5OVeqx9k84-AKbSdZC_DiGE_PYMJGjQXeM3Q5SC5uH7zBUPvHZRQaANsNDxYVqtYKtqpK_qA463SPf-pKY7M0Tzvm0R1EQ-LXZvpSkoGrqUxlBB0yOZ0ScRiv1-pChiuIauaJXRy0zHWSDrWjwMzBhSBnvNLkLhvVxB733uWrVojkW07YibOFQJxpAVLwmxBevL-ON9P3C1vvOqGSCiDcCiDjCjNYaLhmO7YVtWMGceANTqn_kJvHsrGPmxsch6OUhm9b304397dEvHEXN27wvQVJG00T-sniKHzDMKByAIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOZO6rFo4ifIdl1e9sP42YtWXSRS7L6Bpbnq-srQGl-M8RoqogZ4F8_BaqAh9a3QY9ZRsUyPY0PmC1mR9Ytd6U9KQx96gqm1XLeSdfimcZtmTrfh5PMJcSjOK38r_91lBtRdKWincwogZYErAAWs9cHjD30WK6iufVwNKIfDtf5lCHmWW0NzT1_mnRJwuZGJHMrigYucIVQaJdlSQjQGUOOLGIzZ3dXNnQRe9DvoPpyK0pA2KrYraNZxmk_mDDrUeOi-GfCAFDauXT6W0-E_2rMxtp229PdLL40or5qfw1PU1RKbRpXlOKSu_kGcxgqvPP8nWrv0yjq06ur98n6pBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoxD2EvHgGKIkzVYLVzcWKNhJ1MPOlPKypEiK2WKXH_HYHGXIqAHjP2xKJPNt3yaMVUQIlvXl4qme53kWq8VPYN-M4aKBhs3Z58sdLyf-MWEcbtK3q_jtLQlVHkIJooNhjJI4o1ZaXOtLmqubJdOKXOvS18rwpnM3H61TZMI7IyleaQS2DYmkgmbCMVZYX6Kb4ZupxOQQunLw43NCz5QHFG2iDueGwvK-zfIhCDWNm30ne-9xBnS3bJi5qtXdo33-ThKxt8udIR-KXSb-QpOUDNWbsnuF9hZEDKL5CULf5ARiMQVbLy6IXaGHRDE51nXfEZVM_Rix6T9jmjWJS-LRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3V37_eb2rA2VFp4FBps3dEfXKMi3PO_bcjtE4cEYjb3AT2jcmUD2DVa0DjycKdig0c2VAZF1mxMLWgyFozYZE0z50K79GQihdtriBjnEi7bmSNFeFh0HRnC7uzf0zIr_LVRfGHlDOu573b2c7x7d5SIJLaHXjO4oTxyqqeD3Y5p2AzxlYUo1xhaOQHx07clAJ10Q4G5yLXMahZdloMdIe5XqaL5cbW1zwiSnIkT2BWZ5HqYLzyERRXR8dDhF6aLYa8e5_iz0JLVR9tM4XgZjYNrg-Ta2AJh-8bpIPVZeBGLr3XOAvPJF-Ww3EeJi-C_Ae8cRZ77Nq67Lgl1lK4bag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ_xpLuQ58dDzCq_Flo6KyoMooU0TBbrZAavv7CXDDG2s37OKosGB5-OhhP6sGCxKIsDRzDMLZQJQpBLdM8KamjOHmVatYQ6ROQn44ksuspWgmKsIMYX1zjOQpBc2kq9QaLaKio2WlT9dQpTcRNmtRkIQ8f9nOns6TNDwlMDuwPDBjvdS_9wlAjG-p221pXjuq3gtTOpeoPRmxdv--FWeAcNSl6S32IXeFTR8M__ZUk3HCcuJJppI0ZHhQMSZoFzmLjTSV4H8FnHljy0aX6cjDR8l1Rqz9oFxLsDvhPGKvT_LddX5pwXp3pSiQmVQjXSH-pC6XbLX3Ieoochwcq36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb8PdyixY8ivUJUFkGK66d3DGAmQF-eX1ZQhV6IrNWp7nKUXH2vTLW63hNGG06IeDvMtFVf0f2NO7VdzyjdqvEwNrwyNQ_UNEW-Ufk0eARpLzBcn5VzBVewf8tWqO7TyutVh66jR4ZX1bjbzhs0zP6zSKcTlUdgMdCaqJlf686RtDduZFLmbEu6TkAajZYTvbKFQoOKH-Lqk0iilIy_NEtGt2nKH4oKnR6WEhOKqdjNADljKuU0bPvt6sogmYgaL5ihvMS0m9Gd11QMMDLnvEuNhRyUfCIPZHNl5o93I2urkbO8gPHefd8vfzcPCK0cpIVEkNvIP70hO1JCVX4wJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V741bOXcGw0-OxZcpge8SlZdclQ4hrYAVhvBez4-bmtRoQd-zeGoEfU5LXP3sgjYPS_RKcYUZVQKGNd4TqyqYbiN_Y6pt1fnYxvVN49UWsoOUoot43npfYNH0BrNQAsmfoOxGHQanODDiZcMtZkv6heH--MyBQtl1cWydF5Rgbik1HGv6gLJAlR1_bnhnfCbqhu545GAWVFjTTLlkPEPkIPXR1CqTsQDvwuit0n4n8qYiJNyXfSeBM9m-m2txXsU2haUPzcWqlQzfcVxJe8W4zFFWOORAut4BL0Xuv4nQUdTWJ2eV11mu_X5obYp-6kMxELSeXepe7dm2mJyCDwSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=ZkbWqqHX3WHMcqov6fWZIp-ZMzz3KMKOsdBTQFRRcWvjNBswuWHD3YYzSrLl34uhdU1bW7KnWtKcu2Sb2baY2BEI36JJq6fd5fh1bHCzfxJnkSs6fUvOveuwtrWFGjKWCRNdM2YmdiGCqwfMPkH_BBrOX-M5oHjJwCt193QLCLjuep-NgGRv8uoFxiZGEADqNSvgiwQ9iypL1p2fH4iPVorJ_sJ84rtausG5HzJLNcZx5c8PxnmXbQMjmYfVVYxJIviDWyAvQ9cNzCqK-tySaGbAKh8BCaaafjYCggJuBP63mNYWKkv8R6izXPBfWLzMOGLgSeWoYuAqFRZYSU4EfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=ZkbWqqHX3WHMcqov6fWZIp-ZMzz3KMKOsdBTQFRRcWvjNBswuWHD3YYzSrLl34uhdU1bW7KnWtKcu2Sb2baY2BEI36JJq6fd5fh1bHCzfxJnkSs6fUvOveuwtrWFGjKWCRNdM2YmdiGCqwfMPkH_BBrOX-M5oHjJwCt193QLCLjuep-NgGRv8uoFxiZGEADqNSvgiwQ9iypL1p2fH4iPVorJ_sJ84rtausG5HzJLNcZx5c8PxnmXbQMjmYfVVYxJIviDWyAvQ9cNzCqK-tySaGbAKh8BCaaafjYCggJuBP63mNYWKkv8R6izXPBfWLzMOGLgSeWoYuAqFRZYSU4EfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1DQZYv1GAetKdNJ0zoxnFZxV1LkCVXK0BiIgsd0bDN5iYA-7ucxIxw9qdtAPzexEPtxLlJP_flkaUwiGMHt5jTHcWq-LosTTuBHh7rV0jZT4Hb5bhxB3bKEJkVRbuL5NY__brLvJ7OKv0Ab34nfwNAFLDdwj2_MB05czWMn2gAAw5m5zp_NpUGqXEsx4JGYloUGAv8JgXMBkwvVdnjCZP9n32mFsoMyoHdd84yRYF9Gtv1vy8ngUhcebEDKw6kbswCkJfyPYdY5lsB75Sqrx2nxxXdLLuD--6_QWsLtvQT1_J1dyjPXwe7_QZ1MiKtATnmrXTrGRqmhyjqUmC4U0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=RSxpNDJ1GKZk2GlljsiV9sOqRrWuaXvBj_UYWSJlxiWLAKWxH4G4U7FvY0edwzZY7iCMn3tLf4ZRR2Z3FuiVl02M1GYoQtj5y3F6-laNZCa9jNaDWRZKRXbp_pdOs8xS3jLp2MUTMBUuBAeSQsqWod3MjiNW35z7J0Om_JoCibEJWNWLbvJaSevNbemsfs63o40IlUPcjeBNLqc3fYXzJZzuQjXuL_PWuMBxBKfkTVMPIkIu9tU-RD-mlMX6SeJ8-15L6CBoy7-yBurhXmlAPUGpCuLuFjcJMHdzV90o9YhM86VI4c8htdTiiZnO3IOO60a7V0C5FMl6RPyeiZXCjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=RSxpNDJ1GKZk2GlljsiV9sOqRrWuaXvBj_UYWSJlxiWLAKWxH4G4U7FvY0edwzZY7iCMn3tLf4ZRR2Z3FuiVl02M1GYoQtj5y3F6-laNZCa9jNaDWRZKRXbp_pdOs8xS3jLp2MUTMBUuBAeSQsqWod3MjiNW35z7J0Om_JoCibEJWNWLbvJaSevNbemsfs63o40IlUPcjeBNLqc3fYXzJZzuQjXuL_PWuMBxBKfkTVMPIkIu9tU-RD-mlMX6SeJ8-15L6CBoy7-yBurhXmlAPUGpCuLuFjcJMHdzV90o9YhM86VI4c8htdTiiZnO3IOO60a7V0C5FMl6RPyeiZXCjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=slCpkIIAQz11XQI3-UXDoCmzMBlnOGt2aecB1geLuRDIUVaCESeqMQ1fTbXvgWOkMLwDjCu1x4OJs3pmkq1qCI-_R-Q7Df64hC-DmfXB4Lzoi-Rqbh98DN4gWmAxVtU8JmY4XBxoBA_SFBTjNpuMPaKHq_Cp1D-phmO2Dz9ok-PSXjLbhIXat4YDHlR6TKBPMbFKnjkUzkk-202tyrTlBbVmct3rhKDKQWxvMxsXAqAVnFNZZ8uiY-GfUNgKfWzYNl6GyrPVeGodRA59LXwNdJ1IaAGAJgTv8pGH0fgAyKbP8PQDoDHsPqbkdqV2y3BXG4SOvUozwR3ShMalzFSf9h55XP7Th6-AXRo7ub53Y0ZVQY5cLALj7hduZ2ivklocZ_PJWTFBvppCnjcrgM849zORppG2xJ-O2IRYyzlGMYtTqL6Pn2PACIfKCnWYMZXxleHr_G2OCQVLTtYxNs48HRKp5OqvXkd6T-sM3rbSXpcC6KRBFlM8SxPwoRj-0EtKECux7kHVzk7MRc2AsQE5k8_9RVU-gFQZWVEc6c4AWPW8AEWfrmBaEafNdqpiRSLKItoGfQT2WZNwonqIN-HiooDvoXDUCDk-cZiJVQgyra0J6n4c5NfrP4BEaBpNsUzHGIlG0HYAh_RFef1YjrK84aTlkz8sBQrH47q1-o0CiSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=slCpkIIAQz11XQI3-UXDoCmzMBlnOGt2aecB1geLuRDIUVaCESeqMQ1fTbXvgWOkMLwDjCu1x4OJs3pmkq1qCI-_R-Q7Df64hC-DmfXB4Lzoi-Rqbh98DN4gWmAxVtU8JmY4XBxoBA_SFBTjNpuMPaKHq_Cp1D-phmO2Dz9ok-PSXjLbhIXat4YDHlR6TKBPMbFKnjkUzkk-202tyrTlBbVmct3rhKDKQWxvMxsXAqAVnFNZZ8uiY-GfUNgKfWzYNl6GyrPVeGodRA59LXwNdJ1IaAGAJgTv8pGH0fgAyKbP8PQDoDHsPqbkdqV2y3BXG4SOvUozwR3ShMalzFSf9h55XP7Th6-AXRo7ub53Y0ZVQY5cLALj7hduZ2ivklocZ_PJWTFBvppCnjcrgM849zORppG2xJ-O2IRYyzlGMYtTqL6Pn2PACIfKCnWYMZXxleHr_G2OCQVLTtYxNs48HRKp5OqvXkd6T-sM3rbSXpcC6KRBFlM8SxPwoRj-0EtKECux7kHVzk7MRc2AsQE5k8_9RVU-gFQZWVEc6c4AWPW8AEWfrmBaEafNdqpiRSLKItoGfQT2WZNwonqIN-HiooDvoXDUCDk-cZiJVQgyra0J6n4c5NfrP4BEaBpNsUzHGIlG0HYAh_RFef1YjrK84aTlkz8sBQrH47q1-o0CiSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7w7OJvdk3Fwd3julJtJUd__XjKLmUzKNjDQXboF2sKr9rccr1GjnPnUnplgV5Wt-nfH4JOkp_eqrz74kQyC3e_1TX4ouKTX5OjQhXBuUVZ83gDtJE6ofyMcnRlk61enpoOsLlHtdcTJGYTIrMn__rJ_bsrFHDkLViqRTt1xmr3dN_uickS3nIRZttknhnhXgEgG9D2VtWmtprsGaIxdBqA1B70kzX7D718GOqXrTA12H9iSWwzJRQIF0bUEGsz15fKlVpsrezGh4n5c7pTgcwiiHws0MlP6w5m2aOhaPAzSyGuwf8HIMK0hKLCItNPa3WX4UrY6M2UZKb3wb-6s8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=frGGrfeyEBOEXJ6SYVnninb0phFbt1omC818i08rhuDR4agCpdVlQXgx9ltZW9MLDIIi80Z0vqAfs2Q68uCXm3tNYD1Fmexn4YE9JoR7W0QxUQz3F5JIOGqkg3NhEdR0u9KiumEUEG7a2cz6hckWkFdhnAoIp1gSuOgL-ndcmsAUxYPGDwkGFllEdPEUE8SISCyyS9huaSw_UKUaPxD9d_mZbc1pHkc33TtSFM1NzxOYg-mNcMdBOBDMO3NSjdiT-eJL1-deiH6BwPeCIbE64iRVBbch1Ok3byahzBf38aXnsVrS0oRcVggzLu9bp_HbdbwSjuR2fQAYASTLO6OFPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=frGGrfeyEBOEXJ6SYVnninb0phFbt1omC818i08rhuDR4agCpdVlQXgx9ltZW9MLDIIi80Z0vqAfs2Q68uCXm3tNYD1Fmexn4YE9JoR7W0QxUQz3F5JIOGqkg3NhEdR0u9KiumEUEG7a2cz6hckWkFdhnAoIp1gSuOgL-ndcmsAUxYPGDwkGFllEdPEUE8SISCyyS9huaSw_UKUaPxD9d_mZbc1pHkc33TtSFM1NzxOYg-mNcMdBOBDMO3NSjdiT-eJL1-deiH6BwPeCIbE64iRVBbch1Ok3byahzBf38aXnsVrS0oRcVggzLu9bp_HbdbwSjuR2fQAYASTLO6OFPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=Yu4I1-UR6pjPkEtXH4krcHjGLQcAzfuKrGQILKIAjYjYVAT1tezUIIZRfRokhwyjk8PeHHetfozuO7tKwjnxvzNPFpCJeMatY1_1NE1AwI2EQn8yPH5BuY6tAoLj0PGpT6n7wQRHJZS7tOAo8NU2AeB2rvKuEqQgzPrnQXVF1qe0FrxpfK8iPwz06khz6-sk9EyzhfPYMOwWBylPT5Cfyt3kH-CRkcPDagk278-ZUzzju3ejY9Zg1PHEnqSs7d9Rxl6yD-Y6IzOXIyjgGnWTHR_rrUqAi4_Ef3leu1YR78i0Qo-ooHoS8PJgGB9-mgi4t5XqUJpUbkfKTJNwPyocVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=Yu4I1-UR6pjPkEtXH4krcHjGLQcAzfuKrGQILKIAjYjYVAT1tezUIIZRfRokhwyjk8PeHHetfozuO7tKwjnxvzNPFpCJeMatY1_1NE1AwI2EQn8yPH5BuY6tAoLj0PGpT6n7wQRHJZS7tOAo8NU2AeB2rvKuEqQgzPrnQXVF1qe0FrxpfK8iPwz06khz6-sk9EyzhfPYMOwWBylPT5Cfyt3kH-CRkcPDagk278-ZUzzju3ejY9Zg1PHEnqSs7d9Rxl6yD-Y6IzOXIyjgGnWTHR_rrUqAi4_Ef3leu1YR78i0Qo-ooHoS8PJgGB9-mgi4t5XqUJpUbkfKTJNwPyocVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfugoIbsbMo4pq081ZSxLCYSQsf12SZQiervVSMMTXXxqptruOFz9IJ-5frUMTib2cD1vnY5IUN9WwJls5bJCuYobkvJEdA6zekRndAaiW8g1uagjo9-BtrzA9dSPdKahx9ibgOcPsJryaak49yipz1nL8BTY8yW5NdbyT-JJ5pTLskp4dez3xd1JHwJkwrX7L5QlGVTIl2KnXTJEZFY2PuVRtZ9Vg1mtRale_Sla180yqdTb2pPaSp2e6sJYXPKnzW8_6KsvTWlKgg-r5HRqmYcLEX4SIwY37zC5R0BbdtDtJqAV8PsSrHWLM-H5vYmg8-vLfaTGNxm2nxP9iQR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=RgDBG4ffPY5ZuhgrLgyNA2M1IOxzu3Syl9K4_-8zx8f7G27rUoX10xE9v97ceal7KgJdyZOm5LmXjQXRyXCvay859LrqeKz9XBI51cUOjMhmBLqgDKe8KmfSWqf1EwhsvNZ9L3YyjgnRwxAjkmM_jgrR2rsOPoz2IBdnk7HMIr87Qn9b33Y4dJbfdm28Ax_SBYdWmMX9kZocYE1_7LGaSoFxXhiLoALsRVveIaOsiFZN3FPlB4pH7I4UMY1a4wdHtArm16HMOkzSUU7ZlA-I3EJ8mp-fGR_S0nGwqRtV7sa9axYKZiJUiXyvTTQXuc722478z9_TvL-5-dAOBBZ1qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=RgDBG4ffPY5ZuhgrLgyNA2M1IOxzu3Syl9K4_-8zx8f7G27rUoX10xE9v97ceal7KgJdyZOm5LmXjQXRyXCvay859LrqeKz9XBI51cUOjMhmBLqgDKe8KmfSWqf1EwhsvNZ9L3YyjgnRwxAjkmM_jgrR2rsOPoz2IBdnk7HMIr87Qn9b33Y4dJbfdm28Ax_SBYdWmMX9kZocYE1_7LGaSoFxXhiLoALsRVveIaOsiFZN3FPlB4pH7I4UMY1a4wdHtArm16HMOkzSUU7ZlA-I3EJ8mp-fGR_S0nGwqRtV7sa9axYKZiJUiXyvTTQXuc722478z9_TvL-5-dAOBBZ1qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYlGlyEMznym7Xs-HRIQ4EtSz7h_J-sE8cvUkyE_FBr5ZOggpw89uMtqPcyDwdmwolfPilZiMMTXbr1Gn0riGNQxK3Z_nUgs3hPOgyNyRsyzpH2_b4ocsq2wXOPpi1oYEMdjzq2LTgl3-utBhFS3wgGT1EXcbTCroFw4-rYYScblf7Na2evaQaZMIA4EHZY23OQfvySCzw_brvZJuYJNn32RfysnDC-jC86_JkQk5Ww8VSSlTIdnzUGxi9_YlWAe3kCJUMfudzO06NYiXKqKEm7SyY-DYbKA-UAL63rRFfG_viTVfwRrKDdX8S1LjiLWZEZsXPPPSo9O8T70CNd2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=lKoJNpbV-fjdaOMMgO4mVnKswS_xpPmp-yLGA4ZMBCqPIRxdlJht3xHM9kVz2NSBCFF9MFy9zJJYlUptTbYqUfG-7xUnvMVk2O3G9EFejmi-807PtW6jYF3gowUwFTnN231YkuXpiOvsK7Bnk_8YeVtNvtnRrqh4RBpBVQ29F0ruG7sEvndb_uoRk7qhsiw9tU5-A3FqWLCSnpiW6mCjh3kKbocmMSLfgZIC6e9b6IzIT7HkMtczSxrF5ZVgq9QEQT64yaG9vNzpj3Bk94wazSwPiZABHjSE1Qm7_KSzgxeHznl-JjAm1ADxxzesk0g9j8mVSE3-WZiZkyKOHWUfnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=lKoJNpbV-fjdaOMMgO4mVnKswS_xpPmp-yLGA4ZMBCqPIRxdlJht3xHM9kVz2NSBCFF9MFy9zJJYlUptTbYqUfG-7xUnvMVk2O3G9EFejmi-807PtW6jYF3gowUwFTnN231YkuXpiOvsK7Bnk_8YeVtNvtnRrqh4RBpBVQ29F0ruG7sEvndb_uoRk7qhsiw9tU5-A3FqWLCSnpiW6mCjh3kKbocmMSLfgZIC6e9b6IzIT7HkMtczSxrF5ZVgq9QEQT64yaG9vNzpj3Bk94wazSwPiZABHjSE1Qm7_KSzgxeHznl-JjAm1ADxxzesk0g9j8mVSE3-WZiZkyKOHWUfnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_keVjCCyfOzqJhkoHQulr7YWPwj2l_D5FBs0PaX0SR2lkrdcuI5OwTGupj2kQjsbKkIaxHENZmgmdVledkmDLL8uJSiMOVO3IE7vfcc6jmIo4nvbJpD_4gS1cZgvLUtPUwplMXjiXYOqruaiVpfhCCh4uyV4RF_30Z1fqtQZaUjqAhlOQKz42eVIUuphq7eNTJcAa96Ln77iGDzshpNHT6VaiDvfdG_U-KvXg1fkJfBB_a38XOp4nHxIUktoTgdLPBFA1PoO06PaLk9po7SapN9_o5_AKJqHN8RVZkRiD5lhdF20N-T25giXQBpGp0vT_zls3oeXcgSOZKTwDEIRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhLPOdm_zNo0kwC_q66ai-mUO_WODghoaYcQuTsLyUduMGDsMS3ALjwuYo9Glg0kaJhBeGjlfbpgRL1eG87B_rWSCT1ho-xo5wHooFQM-PhOan_FZd3NhBg8tibWes5cdD7j7fyNFQ6D5J-ns7V2j2V866_VVSzz8ryX3SGfFFw7L0F6vx8muNIulleEProLaxGNdrgxHz71QjTGZEt26S0G-aiakiW_ADLTH4ZnWtntZu-wojfzTvrs4YPQsZ0qwUd12l1QbXAFbDY5cbDbbADHsxRF1cyekrVMJQOqvYhU0vkMJs44QKAULyvfQFNYgw5alWljp8mHXGMXEXieYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJwGgF8_KDqB8GpQ4ezxAtVPugiJlAT2s6YoshRjU6_yiTIokMa2bZC2iTye6LMUx830WT64c5hDQ8Cen0cUR3waNK25RQPX-WrMKlRhoviSyyeGxmmDgt2aUXKwUehCw9MwGN1K_aX7s87l4oYPGsDSK5wBjU3dBf5BS31dHOU02R6UODeWBOi9_cn5mnjUPsHXZQ1Uz6gNK7mlAmdpOqBGYKj2hNb9ty5UbWMBgCnMVhHVQY2X4KjirU9KPyXdRM_paU-0tcjdbR-I7MwoGfghKJGuKGASzfYre5zpYG4Ud_TcjMzdEPHVduYDaDFtDnWaWtyssVHv7Q-Ra9uwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی:
ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف میدم و روی نیمکت تیم ملی دربازی هفته اول جام جهانی مقابل نیوزیلند نمشینم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25659" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzfVKAXskXYoUCoBT1pfRDodE9m1gfJL0L4jdS9wBK-AeNH_vYc15jF5Om_gSq3PhDwFCrruVtk7f4gYHci3PlA6xOZlNdn6ddbUt9KNleOhtgXKXdO4-3LcsLDEB_tSAHguxG_-3SuMJW3pYZPTU8BeO-A-Wo1JSyymx2SIKhIjACoSnnaJ-tfrqxvkf3JWvdx_DKZQvmCETIJNPBT2jWS4g8v4uIqnXIMBVxixdLtPyzceAufYTMurPGroqfMuGumO10kN1ZZajFblpyUptcUwfCR4wa4ygUHLh41EEJXYQn0D7eVMSMJe9D83oIMjI5__7oPUkbSw8aoPkuCgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
5 داور نامزد اصلی قضاوت مسابقه فینال رقابت های جام جهانی؛ علیرضا فغانی در رتبه سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25658" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=S5vVmEWGjzxy2w0nKxlvzqdVkZR19sucd4E9BGSwZcaFk3-GlEpwhHEC-6VIIOlpIABVUG1ojLPAYMM82r0-Ei_VCkbRqBJCDdOidHsAiihUJGQDqwwuaLYoneUA4HXGt9O6dLcqcQzXqxSv09RFIHMBaYCtnd-IygmQF8KKfUuHwVgkxde3Em_-hUgxUOPFvR5BOYEG00EjBjIQpaWB9_ikwl73p5qaD6lcGRI6ItdeuzEbQGNVmLCH-YzZ5OPWfIM8dSWT4F21tTlLOM9vClxXgYm1TF5IXb3bgugtSK0ZDn6emvUcDG101JG3P92DR01u5E0Yf20HumTvDDzL4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=S5vVmEWGjzxy2w0nKxlvzqdVkZR19sucd4E9BGSwZcaFk3-GlEpwhHEC-6VIIOlpIABVUG1ojLPAYMM82r0-Ei_VCkbRqBJCDdOidHsAiihUJGQDqwwuaLYoneUA4HXGt9O6dLcqcQzXqxSv09RFIHMBaYCtnd-IygmQF8KKfUuHwVgkxde3Em_-hUgxUOPFvR5BOYEG00EjBjIQpaWB9_ikwl73p5qaD6lcGRI6ItdeuzEbQGNVmLCH-YzZ5OPWfIM8dSWT4F21tTlLOM9vClxXgYm1TF5IXb3bgugtSK0ZDn6emvUcDG101JG3P92DR01u5E0Yf20HumTvDDzL4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25657" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=nj64gAtXynqNl0mwVLIUkEmkjL5dWRh0XOZfty3AV_I5wVFijQaeHUlPUR4_MdpRr_dd7nWKYM044yyvDcoXch8LicXPeixtttz_vaHYVnZyGgBEmp7MML8czTD_7-EFwap2PYP1lnByDyjTK1SyvliJIObuXQbsHClNIyGDkRmzuxxNsnBI0F23t026GvATLYvGQZPts-xyigItTMTbooIRbI5BAekbIrmvYtMcOw3TTU8Xxu52-a9SRYPlV60yZ2l2lWKIGc5wKwwK5XcNGi5PK3FgEgZAjV4S_B3uQKbWozPM8LLdA40Lghne4ttP9_Ny9lnRqhbTdkO9zmXWgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=nj64gAtXynqNl0mwVLIUkEmkjL5dWRh0XOZfty3AV_I5wVFijQaeHUlPUR4_MdpRr_dd7nWKYM044yyvDcoXch8LicXPeixtttz_vaHYVnZyGgBEmp7MML8czTD_7-EFwap2PYP1lnByDyjTK1SyvliJIObuXQbsHClNIyGDkRmzuxxNsnBI0F23t026GvATLYvGQZPts-xyigItTMTbooIRbI5BAekbIrmvYtMcOw3TTU8Xxu52-a9SRYPlV60yZ2l2lWKIGc5wKwwK5XcNGi5PK3FgEgZAjV4S_B3uQKbWozPM8LLdA40Lghne4ttP9_Ny9lnRqhbTdkO9zmXWgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسری طاهری مهاجم جدید نساجی:
من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25656" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsniO9o3C5re_kuE0qfGXG5-yXNYY8-SLLCPpqLzNYmpEJteYDX3hX89mv-NL6FUhjvLbJmhnbTw5rYOswLd5wJKQO7RA158-AHWw1jhFgsEFSeWGQPqm3-wH7wPusMx_rHIAPp05fFhyzzV6cuuRfGAgB-8bjdhmL_SPQYQ3f5mA2SHZoS3zzfrWjpet1j4UM9bw5vSWp7i2ENubldXAANMrJcFNxaJmO5heWnhyvYDP5ry5iP1m3ceM0kySRFjelBKeNr6qLOfZcRsqLaZLU4ib2cCvpiyzv-KjKmIZ3NvvUh0VmK9ldDK9LnDT7lrUi5raNkrWnKzxkbC2RLcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25655" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=kuSYrIcpdOnzN5oC4UtzihDRcQYCA3XfXdVU0BE5v2v2hmXsNKXKEQvZUNCUr5bKRxa5-poBCtYYPVUnYPky7_eeQt9Q0eaVDxpxc9C0Af1cvPyGI9qvuvrKCKp1xy5-7s3_k1FCnNXovI_cib11aEjES-8EQEEsnmMYzh4XB9fNQQgIJah03659Jc47VoiMOSKKY-QzYNEHCEMheKIApRubw39MrDGGkenkKIVrgcNdUUckpYGxaNxwK22SorJ-iUt6Jrghah7Atz3kNyHMwrXLRn0MeuPlfinp92f1Y3il9sziY9yZiIp0RA2e86lzgg5azq4vIxI4H-zh9G6Y3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=kuSYrIcpdOnzN5oC4UtzihDRcQYCA3XfXdVU0BE5v2v2hmXsNKXKEQvZUNCUr5bKRxa5-poBCtYYPVUnYPky7_eeQt9Q0eaVDxpxc9C0Af1cvPyGI9qvuvrKCKp1xy5-7s3_k1FCnNXovI_cib11aEjES-8EQEEsnmMYzh4XB9fNQQgIJah03659Jc47VoiMOSKKY-QzYNEHCEMheKIApRubw39MrDGGkenkKIVrgcNdUUckpYGxaNxwK22SorJ-iUt6Jrghah7Atz3kNyHMwrXLRn0MeuPlfinp92f1Y3il9sziY9yZiIp0RA2e86lzgg5azq4vIxI4H-zh9G6Y3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ایسان اسلامی درخصوص درگیری شدید دوشب‌پیش جوادخیابانی
🆚
خداداد عزیزی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25654" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=ZS5C5nDfXu0l8tCvwDO9bIl4ZtljReKta0iP24wkzywlJCDNjhNC7wdn-2cThfr_sXPmebtjnob2U14L1RjkIMW3HqSWxK5-b2Sb2EaK0J7eQbTkdWjUyXLlmsyNozetrZ4mfXCsaDhzkc_bmnvpFNM_nrlqbbRzkWAKuAJMSUBpq2_JwzKEKqH63q2ttUKrccVZU3SaPV8k97Y96-7QWVD0SYzETqFdOF_GCRQcHIE0prAr3QFGqDuwVbwTmFhd--5LFaXfzVS33ezWLUjNhCDqw2RD2zJGJGVygziyQu6mLRhsrAC0TWi-VPPsYWLlkJ2FwXoCuEqT-WUF9Ni2Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=ZS5C5nDfXu0l8tCvwDO9bIl4ZtljReKta0iP24wkzywlJCDNjhNC7wdn-2cThfr_sXPmebtjnob2U14L1RjkIMW3HqSWxK5-b2Sb2EaK0J7eQbTkdWjUyXLlmsyNozetrZ4mfXCsaDhzkc_bmnvpFNM_nrlqbbRzkWAKuAJMSUBpq2_JwzKEKqH63q2ttUKrccVZU3SaPV8k97Y96-7QWVD0SYzETqFdOF_GCRQcHIE0prAr3QFGqDuwVbwTmFhd--5LFaXfzVS33ezWLUjNhCDqw2RD2zJGJGVygziyQu6mLRhsrAC0TWi-VPPsYWLlkJ2FwXoCuEqT-WUF9Ni2Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند: توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25653" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=E8TjqlVdDuNVXb2jsvjt_He86Y8Ho34JadpQCBHJN3eWYZVXQNc3PoretLL5lYjJhApcS9MoCKNe2-qLG7ja1aQbtYw1Z7NO56TzovMWnwwdCUv4hz0-0F_R05CV064waTblwpKjBc65J3mdTmwNqnjsqnFs93tawh1s7by9xMs-HBkSQaoqJSCtW4-398hwsehbmYv3CMC_8F8fpTaerzzTsJtB8qmq0LQYF3ua1jRYSogFC7wDr947muGIyd-LykFM8IpLLePiBSD5gShRIyVh0Qk8aBQuxUOOd_kr2Si-Nd-hH_nd4JssjmkhdJ37-CM2gn7SJ_EsfONOP95Kk6hHoDMct7fK5ecv_i-pJ6_GSU1NsR-ewRZ6h_phJ1TuSDAGMQvZJ_yZuvCwSaxPWAG3gEu9SUH7zJ0P2mxWq_5YFsd1PM-3OfL3maLJ8m1Dkd8ryy0Iwtcbyz0693aJBtbMS4M-ToGl8k078YvvaklxP2MA5VtGv7dke0tZaJ371cZ9QNQkXG24QxqpJSij2Px1JXM349UKLap1F4vtMq_osqk0M8ygTHog-i-sN-vmh3wMGKFjmv5Y1vlRKcLqh4eqe2DqAh5HKRIQfI36ZbJxpWFteMMrxbEh0gInVzwZ46GUIuIxJam6V2yP_4wxBVcdXeFXdv0AzNTCBU2SdbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=E8TjqlVdDuNVXb2jsvjt_He86Y8Ho34JadpQCBHJN3eWYZVXQNc3PoretLL5lYjJhApcS9MoCKNe2-qLG7ja1aQbtYw1Z7NO56TzovMWnwwdCUv4hz0-0F_R05CV064waTblwpKjBc65J3mdTmwNqnjsqnFs93tawh1s7by9xMs-HBkSQaoqJSCtW4-398hwsehbmYv3CMC_8F8fpTaerzzTsJtB8qmq0LQYF3ua1jRYSogFC7wDr947muGIyd-LykFM8IpLLePiBSD5gShRIyVh0Qk8aBQuxUOOd_kr2Si-Nd-hH_nd4JssjmkhdJ37-CM2gn7SJ_EsfONOP95Kk6hHoDMct7fK5ecv_i-pJ6_GSU1NsR-ewRZ6h_phJ1TuSDAGMQvZJ_yZuvCwSaxPWAG3gEu9SUH7zJ0P2mxWq_5YFsd1PM-3OfL3maLJ8m1Dkd8ryy0Iwtcbyz0693aJBtbMS4M-ToGl8k078YvvaklxP2MA5VtGv7dke0tZaJ371cZ9QNQkXG24QxqpJSij2Px1JXM349UKLap1F4vtMq_osqk0M8ygTHog-i-sN-vmh3wMGKFjmv5Y1vlRKcLqh4eqe2DqAh5HKRIQfI36ZbJxpWFteMMrxbEh0gInVzwZ46GUIuIxJam6V2yP_4wxBVcdXeFXdv0AzNTCBU2SdbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌ بهانه بازی امشب فرانسه
🆚
اسپانیا در نیمه نهایی یادی‌کنیم‌از بازی دوتیم درجام جهانی 2006؛ فرانسه‌ای که به زحمت از گروهش بالا اومده بود به اسپانیای آماده خورد که هرسه بازی‌گروهی رو برده بود و اغلب فکر میکردن فرانسه رو هم میبره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25652" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN2KLXLRHsDqP544lVZvpakhKJnLTAFfUyz5aeTWaoRokciPYhovy8ZtA8b0eV0t92TjkzM1XRyrRsaarPEEbp-UHQ4Fy-JaDyckf5GjZoMPPA-1y6j7dZvj0k0RVFsj5VrVNiLzMFsMO0PL-kvNB8prisVZ6I1JEZi3QrWh1i0iHSMNrilxZs-cP0Gf-jom_VnwsVCj-3AtbiCEL__rp0UJzpoU7656kvQaqXXvhMlIIeMdy3cvOWNHgR-NAP7TSXRTYWDfx3jQyGQpgmPXVp8bMkvJxH81By6E8zKyvKiW7ASOL1idUrXzB2zqUbqM4HbimXeDzA-hsoFTpJK86Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25651" target="_blank">📅 09:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=q-UuYIZ5g_qXzt_gF8upk86OFUJFF_cEVz2nRud80XYVMXj1lUoyy3274q6xcarmi9191x_i-UkbCcUiA8Zcxap7cZq0nsJLCzn5xJRHMG_jQEXdYbGqngB2dYkk1tRVQ6pDl0PLZw88h0MtvbyyPk-fARFYBciGLjeFfou5GlvzXZNf19Dl4S8k2Ud63_9Wf0m8sI_yMHlQIbZJh1lO-XWRujGFq7Kn0bYG2pdacswK3PXosAYoPQOLxFTuqsMfH2Q-rssvhAvJa_u6OQluoJbgPo8TRrewOGqjq5-0uMF5KT8JsSn21vdIkkFmDVRpFE1sDTY2F9MIpYX-o9igoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=q-UuYIZ5g_qXzt_gF8upk86OFUJFF_cEVz2nRud80XYVMXj1lUoyy3274q6xcarmi9191x_i-UkbCcUiA8Zcxap7cZq0nsJLCzn5xJRHMG_jQEXdYbGqngB2dYkk1tRVQ6pDl0PLZw88h0MtvbyyPk-fARFYBciGLjeFfou5GlvzXZNf19Dl4S8k2Ud63_9Wf0m8sI_yMHlQIbZJh1lO-XWRujGFq7Kn0bYG2pdacswK3PXosAYoPQOLxFTuqsMfH2Q-rssvhAvJa_u6OQluoJbgPo8TRrewOGqjq5-0uMF5KT8JsSn21vdIkkFmDVRpFE1sDTY2F9MIpYX-o9igoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
افتادن شال یکی از مهمون‌های امشب ویژه برنامه عادل فردوسی پور؛
تعجب عادل عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25648" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25647">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFh2B6HSH3sWByrgHS3CK52OyIf-M5AOuLy8JZO8BQYDL04bFnWHe9BgIbqCA4ThGfX_wApMjwe2Wu7ONucmdqqxQeEm6wfsGP-4vP70B6y7PeDT1CStbodWmhkwr5lHUpxZ3gQJe17xzBQPDOzRqflgyyIujbOzPKuZpbPy4qkEPj5zNGaRqfbQZfLMUHPy6Q-74TV4CmqT64RsKy8O0Skuf1xvpjMAv3lejHe9SezlJxw5tvPPejEJ5wRTUGt9ByWkcMZ5UH--OHbHAREOSAZVfa_x47Y-TwGvR4hfroYvSIAyIUKlsZa_Bq1j8QLeHpow0JIka0gbVIkhGDl3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی:
تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25647" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soq1s8q_9QKgsv3ioKsdbL7EEPJmBnaRqfrw935yS0ttMA8fE_G-WqCgSjaH_1q-BxkeP4RkBfxulwCohVyf6mz4LIwry24Ofg6O2Plyhez_KGqeYmGhsWA5qGh2YeMyrblYsJo78onuPsSzWa8DQYEJc3JPKEhjRiXKFt5l7zbiUeaptOcxk9ekCCMuaLakH60_lSqZjby8Z8mwx4rcZdlGIld_XOtqw8cxa2d6DatBRAY-SCxw7OisrORNs5deXo4ZxraaoVYPFg9s6YffW264kBDWmQYgFbQ0ponnqRw3otzDGH7Uko9sxLmHsIcdMz6RtjPDC7rvcOvWMxI32Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
نبرد فوق‌العاده حساس دو تیم فرانسه و اسپانیا در نیمه‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25646" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25645">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=UT5yA9FgCTMNWqCa6yrPEgk7nm7HnN3PrHzYhOYcwI9wrZhlPQ1iWiuF6G1jCAcY91Nq3AMmfbreuu1ZKKGHlqHqBb0MulV56NEPEwpmmHo2H7RWyPlNSkU6_uaAk2KtwblZAKVNzH7tTL0--ltk7qBrm_m5IMYSJg_479AEXJJ5Nv500KJbrkZvdG7KlhkkZ2VfoBTtfivR4IKYgjDDx9x34gNKoWRzfrf94m4xLbgn9YOde9xRj8U-SAZac-RWRsvpTkTdHkP2e6ZbkE30Arc2rr7xG1zI0szj2Jc-UPKpqDvnOMvCwMX2n4WAYUpK6jsOVSAHABkS9d39Jlinbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=UT5yA9FgCTMNWqCa6yrPEgk7nm7HnN3PrHzYhOYcwI9wrZhlPQ1iWiuF6G1jCAcY91Nq3AMmfbreuu1ZKKGHlqHqBb0MulV56NEPEwpmmHo2H7RWyPlNSkU6_uaAk2KtwblZAKVNzH7tTL0--ltk7qBrm_m5IMYSJg_479AEXJJ5Nv500KJbrkZvdG7KlhkkZ2VfoBTtfivR4IKYgjDDx9x34gNKoWRzfrf94m4xLbgn9YOde9xRj8U-SAZac-RWRsvpTkTdHkP2e6ZbkE30Arc2rr7xG1zI0szj2Jc-UPKpqDvnOMvCwMX2n4WAYUpK6jsOVSAHABkS9d39Jlinbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25645" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25643">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfsoMzEoKR605QqaUlIbA8BT0GFi7Pg6O5L6GaWYNibCjEeAGPOqt6x0bUVhWhYQCYFkV0wBqSlWRsgf2T-TkPEya5eAW1Uh7yhLZJ2QoKy48vmAiAt8XafwN7z1bYyTtj5a7tBybHj_iBcMA0etPVsgB4933sYsrObEX2ve2m9zhShWefRES1R0pSr4aNj5PrcTuY6JzA-dtVMrI4AsiME4wFv5JrazBhuxcC5NP-5u0JwvqiIJ-BX2B82_ehxJrbhN6-8QKz1m1jdOg_rJxik5pCqzCmGp5u1nVMqCOjG5t8ApL0uk2uUW2LXKeelCvQTX7OUI9Suwp5SLQiVTiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25643" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25642">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=tGC1UwVgVfRg0y1yeKHVqavPT4LZMdOjK-rw_hTOcICmqjHpS2P9_UfT8HjE2JvTkwRaMll_EQ8bq9__0lTiBYnZIP-076Oj416TEhZfKFUgiYQNNhPrLuAf5n4NH8YYV67eXBxmWNjihbYP4S4ildc2ax6LyR2z1pK6cHM640i-GaTJweDmsOOK8nNJqc899ZjRNxxn9N7hCjOR0V2-aI-LecyxbdZjE2AzMU8_TvIClRslwiMbl-GSJWGIWJ6RgRT7JS5C6u3u0DZlJPSqGzbEu1f6h01xuSSQck74fC8umwRuDTy6vL3bvMg6RK3plX5vkjTrF20pvg2jEIy3sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=tGC1UwVgVfRg0y1yeKHVqavPT4LZMdOjK-rw_hTOcICmqjHpS2P9_UfT8HjE2JvTkwRaMll_EQ8bq9__0lTiBYnZIP-076Oj416TEhZfKFUgiYQNNhPrLuAf5n4NH8YYV67eXBxmWNjihbYP4S4ildc2ax6LyR2z1pK6cHM640i-GaTJweDmsOOK8nNJqc899ZjRNxxn9N7hCjOR0V2-aI-LecyxbdZjE2AzMU8_TvIClRslwiMbl-GSJWGIWJ6RgRT7JS5C6u3u0DZlJPSqGzbEu1f6h01xuSSQck74fC8umwRuDTy6vL3bvMg6RK3plX5vkjTrF20pvg2jEIy3sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25642" target="_blank">📅 00:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25641">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=TBrz9cFQa2PXyWACIv0WEO8twPdZq0N3fClmegicAUhh0YeLZcFygcuHFNtctsQ7HwLCpF9diJu6BHpAKRtW_zA8uj7DbvTEpHdqlQ7lTHwB9jGSIiF2nn86li56MPoo_Zjyh4pDUD-19zUaCm-wxc_HScZQ_erxHZydnuja3W11ApZlzindJfhgltRN618ica2Do5hEv03LWzeK2xDo4p4TnPUeXKFLCnG4Q8GitmQl-djGVCkZt7ZXt-QtTQ3f-pRQVxGiXqD7aXHkrduUxEqs2OICqVmF2ZD6TXtIZdbn-HKbJjZqaDgsH_Lv6Xm5gi-sV61WSQMvO_C72G6efQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=TBrz9cFQa2PXyWACIv0WEO8twPdZq0N3fClmegicAUhh0YeLZcFygcuHFNtctsQ7HwLCpF9diJu6BHpAKRtW_zA8uj7DbvTEpHdqlQ7lTHwB9jGSIiF2nn86li56MPoo_Zjyh4pDUD-19zUaCm-wxc_HScZQ_erxHZydnuja3W11ApZlzindJfhgltRN618ica2Do5hEv03LWzeK2xDo4p4TnPUeXKFLCnG4Q8GitmQl-djGVCkZt7ZXt-QtTQ3f-pRQVxGiXqD7aXHkrduUxEqs2OICqVmF2ZD6TXtIZdbn-HKbJjZqaDgsH_Lv6Xm5gi-sV61WSQMvO_C72G6efQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
فیروز کریمی درباره‌انتخاب دومادش بعنوان سرمربی تیم پرسپولیس: انتخاب خیلی خوبی بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25641" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25640">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHamJ-M0gzwNfBjPhNs-KUqRyEmasVagTov3JgISwielOZUHB56Lyd-tTT1XmAoKiV6BkImMNAsSsmM6LSLkAzUSMUQQFDHu6Jgsyy42kGAW5gkswZo83MGsTQgDgVjOpSX_Jh4F1KseGc-bMfHlLN_N7tL1Q5-jcNuegZ2KxsQj8KEukTy4peiMT68jlC41jnNTCywG-5NgN26n5DszwELlywgE_sCSaw8LoM_T5VhyWb2sWk0iJE8aXDLOMLDqdbHYJ08exFkxGgXyX3Hvewt5zvpeRlmuiQiIvJBLMXiNhyXJ6NEN6gk1a4IdXjzODPWtn4b6BIBDfxsIowfBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
رامین‌رضاییان ستاره‌استقلال درسفر خود به فرانسه‌کیفی‌از برندمشهورHermes به همراه داشت که مدل‌آن Birkin 40 است و قیمتی حدود 21000 دلار دارد؛ معادل 3 میلیارد و 800 میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25640" target="_blank">📅 00:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25639">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoTlZt-l7lnjzkZAWzIQYDyaqb9tIZY3YJkHOJ5f9-ixFpjrq8X_y6HitwhnSQRpaF140i9FXWlAg4oqKW47uqmgO0aTvMCIbYg0JKkBnyElUByMOLBgUYZZcGENiPu8zb_vSjh6dP5DAw3IQyw796eb6d7kyr1CI16oFQKog-M7pGfQqNSNq1jOMe_M3Wrea9BM1-jlUtoStyuWPa8ns1kkR-tSwGbnRd-QKM4lZOSg4h9YzxW_x-5HnJgbJqkQxC_L-_gHgJTBa7Vp2XRrEAA6M0SHE5hq9REKJsLvFECzIxSrkb0phPxi4i-ScoFshtqL7fjE7kTTCQUnGCksRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس باارسال ایمیلی به‌باشگاه‌‌الاهلی‌خواستارجذب رضا غندی پور مهاجم 20 ساله این تیم شد. اماراتی‌ها پیش‌تر مبلغ رضایت نامه غندی پور رو 2 میلیون دلار اعلام کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25639" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25638">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxsHz34whogG7BjrCQyTNrD9IEVTiJg3S0UHkKuqyuusZm3nHCQyYt9nszsldqQ0SnjC831ZV8OPekRyINXMSswHgg_2aXlCNKaBOoh0hPJ8wOqRe_G5-gsgNcfAzsWnpjXlvUEAjLSFcldxWZ0mPpevXdurO1HT00Qk3MehPwy8ZZEoe-ByhiRzjdv9Ew3shNtWC9tB4arEUEc_h5Cg-gn6XoMN-A_KjKLBKeh5j5UrNloX3pnilTfMcEkAJnoB9o0nTOpPrg6foV-gNR_G1b4LWbTaK_WVvddThEbLwux64z-UzKNNPqzUJcKXTMAdEWvqjEmziOyADu-dqupWmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
این صحبت‌های مدیرعامل تیم نساجی نشان میدهد درصورتی که باشگاه استقلال در جذب جواد حسین نژاد عزمش روجذب‌کنه با مبلغ زیر 3 میلیون دلارم میشه این بازیکن رو خرید. فقط مذاکرات باید حرفه‌‌ای‌باشه و بی‌تعلل مثل آقای زندی‌. گفتنی است باشگاه استقلال برای جذب حسین…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25638" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25637">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=EQGNm1PKYPncyRp4heb2pK0zKJp3NS_zYkrm7TBhNmef73dtSGi8RtROrThscmOmPkppJ1aGxntClNezXsdeWyHvfpjqjo9YrNHjEbn29EYbPqbbXJnUAQ2VZUFMoLo3v8Ie7-vRAJmrw6kqWObQSg7MDXI-rzW3gMV96vg3UtJxpCA4GXKgk6kT5zh12SDUtWPpWNaYecHZnYN2ZWAj2I4nFT6YHauhXUdGFRATzmq-dEt0BSoYR7TOa7ZPkUJo0AxrbTOXe2JM-SqrC07RuPY3Q_x1EVLZt0tSnZGzFfTaWb8etjLryNK4MyVxznEcnkjrpebMyFfK99xCSdAa8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=EQGNm1PKYPncyRp4heb2pK0zKJp3NS_zYkrm7TBhNmef73dtSGi8RtROrThscmOmPkppJ1aGxntClNezXsdeWyHvfpjqjo9YrNHjEbn29EYbPqbbXJnUAQ2VZUFMoLo3v8Ie7-vRAJmrw6kqWObQSg7MDXI-rzW3gMV96vg3UtJxpCA4GXKgk6kT5zh12SDUtWPpWNaYecHZnYN2ZWAj2I4nFT6YHauhXUdGFRATzmq-dEt0BSoYR7TOa7ZPkUJo0AxrbTOXe2JM-SqrC07RuPY3Q_x1EVLZt0tSnZGzFfTaWb8etjLryNK4MyVxznEcnkjrpebMyFfK99xCSdAa8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند:
توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25637" target="_blank">📅 23:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25636">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=UqenUtIqn3L57cIa90ufisE7lov3rg5pTd0dmpg8utzNeixON3elc03ZAE4Lx2njwcpaLRCRSvUIozt2hzAnNDoE8P65jdyMuqkNdiqjzHYVFpmUqrvV498I0S36P2npWtY3FCQrufBzQOl7-TxaG7Jn5ue8-SyzzI763Oj-__O5EPeBcjoX6jSKbpyuQvnBlAjKoymMcLZzcmvKkBSbW_SuHwGmrpV6-gdZRXV2SibUkJfDkp9KlTKFD2SEVm72q8uLgMjGRJEcV3xmaDeieft81UkJrpmeDIaOmJq6Qi9E4oiZBSw7vylqUjetSWdh-l2xQVDumBdtkLq4qv4C3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=UqenUtIqn3L57cIa90ufisE7lov3rg5pTd0dmpg8utzNeixON3elc03ZAE4Lx2njwcpaLRCRSvUIozt2hzAnNDoE8P65jdyMuqkNdiqjzHYVFpmUqrvV498I0S36P2npWtY3FCQrufBzQOl7-TxaG7Jn5ue8-SyzzI763Oj-__O5EPeBcjoX6jSKbpyuQvnBlAjKoymMcLZzcmvKkBSbW_SuHwGmrpV6-gdZRXV2SibUkJfDkp9KlTKFD2SEVm72q8uLgMjGRJEcV3xmaDeieft81UkJrpmeDIaOmJq6Qi9E4oiZBSw7vylqUjetSWdh-l2xQVDumBdtkLq4qv4C3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وسط برنامه زنده شبکه ورزش برق رفت!
رسول مجیدی مجری‌برنامه: بازماانتقادکردیم نذاشتن ای‌بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25636" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25635">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vrt0x8GgY1zwotSsw_bAb-Xjrd3P2xCiODff-zcabMPKHYaGHDacCG-z0Z5z7wdn5GH0MGk1axYGuyz_ySu7bUpZqAEeMzc5a2_lH6n43yma46BFLc4WygGs_vurGSxLPZW7mECJE8aukKY-I7uxnxLayvBIJpAYd9CpT8EWBWAlX0VOdU7UEQY-BofVvY-aeR707r6E8czzTj2LJ2agPSWaj-df1JirgCpgJiWmB-CvWltZcgNU9wXUFmQ9mQzQWjKzxtyojuAwtKs9XhIswb-GRYFlMWB9EFYK5ffhd62VSDLDiROVkoVxv1CmIp_xZ4vCE-Sn02WBCQMQZYTT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
خوزه فلیکس دیاز: مایکل اولیسه به سران بایرن مونیخ اعلام کرده میخواد بعد از جام جهانی بلافاصله جلسه فوری باهاشون برگزار کنه تا تکلیف نهایی‌اش‌مشخص‌بشه. اولیسه میخواد که در همین تابستون از بایرن جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/25635" target="_blank">📅 23:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25634">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Otlkmno7wrLZQVNVZ8xBOk7euiyzP4BXY271As6ePf0qLRik9aH5qNJVpfZCdQXYue-v4vfQSygZ42rqYRRY1XCY7vaOMOQCvGrU0bqmjoKTE9lNFnZHZz0lm7GYCbOhkzr5ENkY6Trj-HgccPnbRZbFy3WogMfx68Dd64poJTXimsGIl-vwo2DJNu7BHmVXmyVsy3TXaUcJkbZ_jX1Glp8B7Duqj4pSxTqS4p32SvmY-d9X2TFyuwlP8CIIJSBv0XH63nO8IziPMm3YOiUttznPIY6X9R7wbB_fO5JjVuWn9zQ-6zGd1NLY3Bplwk8JSTK-722XVumR5Iz5QMFw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25634" target="_blank">📅 23:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25633">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPih7I1C2Ly6L4stjGPgooSuoKh_HYqA998T7Hs-_TBzM9HuMoHoEvmfuKVGaHPHdy_XioIhy5sOuIAnKTPBInAtDi3IyZk_6ppQ7VTbuTYqR0EqnsOepr3rNPqUAJYzCly2SAf9IhbA7OheGlsWPzFYvteOERsOyHTYPJLctp0b-QG6WBgJ1CHAjWD2uAkwdyAlzui55A4fIHsuiS9OCQ5IGw0zuK6nHqfmywzoGENqijqVKw28eStui9rfl5rv9qh0ylWgyLTm5SaF0Hcm6Twq1FlHK_z_ym7r9s8-pTjpvQNd1CZO57bclEBJ9GZD-y9I9vF5yxGtIjyZhKF-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال ساعتی قبل بازمصاحبه‌کرد و گفت کار انتقال محمد خلیفه و بهرام گودرزی نهایی شده و باشگاه بزودی پوستر رونمایی از این دو بازیکن رو منتشر میکنه‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25633" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25632">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKd4BaUlLrxAiY6kKy3o9RQkcC7i6zur-IsYjSVKXNNS_y_FJBqKdsN000-5YELBNAGY17u0nTSF2ECA0o3lZ5AJZpg1iLZG5hHDbU6Tgzvd7gI9VDN_C3Y38t9VAFs9Pk-NEyvcZ8R69P9ovhYoClf7L1AUAN8CIL7-h4SIKaAi1fd8Fq3zuutsQAOWI6IJPXA_hBJfDevzKAfOQuDGYPqmii5daVCuqm2gzxfrVWc5umH9XFH44exkJN2R3JZY8z84bKYEkClTdOXpZxUkUT18BFiA4UPVO0yvfmM64cg0xmprsL2a-t1yZ6VnH3B3hMLTrXomXnog8EmKC9x6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25632" target="_blank">📅 22:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25631">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=FFXhNTEoCxIWmzECF7syUXFWLSrRVj2xbwKlJ0lScGIfo2kjYY-m7htQoAJWUUlUdkbR5kKt2rxlhmd8A0Ko41GDW8EBGEhBVFO5Ine4lG_IitHrwWPxn3PPmbpZaM4_pLmmf20d951tApV-kh44NZo600W0WAtgamIHw6GuFYdJGmQRzQUtoWY1bUPBaTmYFuMNE1I5PMTDLtaMR-Xg6_n7TwbtaS9UmTfP3NXrl_OEYqXP7D8DlY5Brqx1dADKBY4DiiaVlUZJY35Mp7UsV_YhqB33Kg6g6WB40lEnMNQfLhQ8ncgRC6Y8Lr4qWC0wad6oa_Nf23WRC6n92Nh1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=FFXhNTEoCxIWmzECF7syUXFWLSrRVj2xbwKlJ0lScGIfo2kjYY-m7htQoAJWUUlUdkbR5kKt2rxlhmd8A0Ko41GDW8EBGEhBVFO5Ine4lG_IitHrwWPxn3PPmbpZaM4_pLmmf20d951tApV-kh44NZo600W0WAtgamIHw6GuFYdJGmQRzQUtoWY1bUPBaTmYFuMNE1I5PMTDLtaMR-Xg6_n7TwbtaS9UmTfP3NXrl_OEYqXP7D8DlY5Brqx1dADKBY4DiiaVlUZJY35Mp7UsV_YhqB33Kg6g6WB40lEnMNQfLhQ8ncgRC6Y8Lr4qWC0wad6oa_Nf23WRC6n92Nh1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم استون ویلا یوهان مانزامبی پدیده ۲۰ ساله سوییس در جام جهانی رو از نیوکاسل هایجک کرد با پرداخت ۷۰ میلیون یورو. اینجا هم مارتینز ازش میپرسه میای ویلا که میگه آره آره بزودی میام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25631" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25630">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXzhiPTFr__i-Sd3RbVQmPqiTGSXuJuOqYZheauPz6qIFxrmrod6ajWtF2eWrKGJK-OZyf9Ypg20Nn7demumEQnlx7tmJGs5j9l3VB0DUD3s46C5-XbTeG9vo2Cz5-EZ7oWbMkT4YjQIHjlYICbXBQmeETGATW0dwxJefJXRj47K0qUVSVytLITxc13mu9uHz3ShuL6JvnLA0pNUQdU5lXzwRj3wfkMG-kzEY19JPoJA7A6vAQ9JRD-FS0N4S8p2rWcT0Zms4VwmwvmhNk4FudHcacRpnzxeQqQ-YEEcjsJhJWEh2cL17Boj6VcjX4PP0HkjH16E9GgKUBTQfkCj8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25630" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOTKYRclC9GufvG-KBrFJollgtFZiicpXQZpj9w__FxadafgDsvnvVKwPBRvFrAdBbHtz5rVM9Xm4Saq_jTZSZP1t7rPhaY9nUYvXdW0hum1Vbi-K8kom9zDPBKnudzaXlsGvfF8edZAIR5csvrqtcfdD7ubMD5bn-jIqh8GBx3NObxZpu-ImXVHSNkdqio_2e9hiWmQUNlUIuQ5ftY2jYze6ZtY4FTmJk8Z6xSiV8uTtOXRD6U7dgtlyf2BT8QIlftqm7FeE4waoFx6vDZjCUnTQCrDirSn59aifFyi7804DHiEV62BcBxbrmacQb6gZiOfzgUHQxcXfJAVE7TigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#نقل‌‌انتقالات
؛
کرارنماری‌وینگرسرعتی 19 ساله آکادمی فولاد با عقد قرار دادی به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25628" target="_blank">📅 22:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOrnnTtquIs-rt1fbxD7UXE83JXbHF58esCsamu9m9EswKuKOxfBlN-ThCdXqZpUaEHr0TnHO22fDJkKF7rJXyD56DQA7oKaisgswmJ5u8TPlbVCJ4dIysvm5VDm1E3F98Zfaguk5tmJxouSxa9LCEfqpmQVbC1i63CD_b1SGFOTTCTxvqBqwVbryFHsbxTX1CGRbxC0lhpt3pbtu1k95FBCsLTp8mx-C62bd7bOSytspeathcpqncurRnYD_2R38JYII94hEF1z2TbX1ZhFSuKN2rx1HUVeYJy156kAvyht_kQNK6g1xVjCUzFdbQk6PmU87HrilsZ-LKy3r_Q0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌فوری‌نیویورک‌تایمز: ترامپ رسماً به کنگره اطلاع داد که جنگ با ایران از سر گرفته خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25627" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG3EodxbgHlZ74DBFquty-T_tDGTQVp1G5H79bFH8hwyxTpaGLCr1d1xsOWc0socw-mmxCPEcPCU8-ZEd16y9v9QNLaljZiw5PnqYjNi2p7Xo1TtznrmNZp9UrXR_lomjlP_Fzun_RfVDFBkQcc56nKrvcShSPYGV9T-zVi0EEzaMQuPLLJk2ZsegqZbGQCkgxzYet_6Nzun2AJR345QW11SBBjFSbg5hwzkptKy64K0NpLGgBcAXQH6iksvSGkq0JDVOWbAlp7Jp6wIX9RqgYTvzQ0hYT4xkwApzQJgKJDXqcw5uqSprCKFghrLLIkDtGVMF1iDbAwwkKXW-39tTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25626" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25624">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HniRDmjgYr0nf7PNUNPI7QBsJ1aCwYJlnM-zRnr7aBfNkLeUGvyabY4Y0mhyWl2wogMoul8LsvZqYD8qu4X9PRWHD8ansgC43FZaYuvPcTFhWVuBO7-VbaMA3knASmue8_DbgNqNL9DseP_hAKL4ZjrUVn9cj8HR2YfLc1qs_Bg5Ts0cfSB_nonzWHqBS00RHXqG2RqaVZvifCqSPVOJqsbVrGF46uS0O_LS6Pgh5tGX3Pz4wyAC5NDIK0vanh3hghhCOgOjlUBylN1EAMNBiOuNn4tNgeqP-MP1SDzkz0c6p4IP16OdVfdreDOERba-lLNhmK9Rls1CLVdk1qgwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZQIz1LN51aMWrwi5C12KkmVC5UfGHnJSUdy_T5XOYFYFpiSPqroSQCXx2AUspBCPEyUksqYERbS3hcCx7egzLj4pZ0yqHhwo4uEkBKbEBrGlsdnQwzOMZbp89RZbqHN7jM5YB2WZCynYJgvSwY3__rZlcIZiL6nct5b_AnKaZbps6yqzc5prHkonUpVOJ2mfhHWrRvdJYjYSwnK0mhIN05Nk5ZQaiRcBWL8XPWtrvUGKs6QniiWTMywL-WQT5gq7OvE_BaiUCXe6law8yW7i6A2LtnchdRHQtaBkHFbjSCxbHcBgey_7hVcyN7MmlprJMmIKXO5fm_SVII9lmb-ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25624" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25623">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIatxrz-Xa83sJS_gc6iV5T0UNcwfSmsEuVzmQnahOGHdnu0RdP5PnlyATPUhPhpgqEUykrcbjxVS89F1HR8gpso9OSLVPXIwmFKhw1mb6RAam5yguf0ZYaQb1gc-y4qbnzrY09ttIUDTVJDrnWs92UnZ9q-WbRCf3aIJJbe2gLqlxki4Ef6FU5EipavIz2eHINHd9O9rRkKIO8L5fa1ix0dqgl73ex3TQ92ad_-mVlTJi99a-x-0mTXpJYyTvq-eUzi63VP_z5p7_IzwPaFCfhMVRED_vo22X_7B0EbhwRW3deGj_GjKFvpb9tGVh7BuQW3ptuaUVJpKupDV2bM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/25623" target="_blank">📅 21:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25622">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsMm2AhNa-fO2iYm7TrXK5qca6NlGbUotjo2ojppOEisuj4uuar3tsZvbNVnp-Cvs1Kha9PGsQOl9gbSyn3h1e_x2keT3lXC-Lz3hb0KVnskZt1Ad57N--lSdiAJybdWf4BRn6d__VN73PRKr8DpdyOgJ9Du5EeyWE8yMmpqHjm3bx3afFsBlz464NaQWLPYL3y6_TYM_SoKVIQfHUN3I9qpI6YLccHd7oFZKlPmcobSiu-YPwj0Nr60-I2-uKSDg6r1N_V-Q0iMVwaFCeaahVB_IOMzDguaLcrcg8-xusja_jvVrbf1ROZmER3rJwnR5hc9W50nJ-GIUbq0phF2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/25622" target="_blank">📅 20:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25621">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyHtMozeUOkY3Dg9l95Q7GpdkpDVQ9wXbSLswalTjTQubv0OTpwYIpuYH4yi5FzVdBga5ym4ZZWlZuIi8fkxezOcKqSmS2lvY7AIAHIVeR-Yb1TG1EPNErrXAH4IRqO0OSxfLeBA6ANYNZwGZJGzP_IY2g6Z4lhDPRyamNeaSZLEJIcV4o8yQs6kB3lNBQwQUFp59MdzF8nKk7VaoN5t9ufoMKj6uPCyVf0ZV3LfW4LZYSyRDC1MJmcW_ltZpJi2g0F7TpGZ44MywHADj5bLVjmleaR_vFA_VnA15-de2QmlSKODrn56J190OPXcCy1N2t866PodBjlY6dwuOKvedQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25621" target="_blank">📅 20:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25620">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLXTdYQktwGRC8wIf4o7nvbJv9bFDCxeuu57BwkmOpq9a9_sDj7RrczlOXc-PSd3hTiFKZs_4gLACwFA7-VlAxCckQHp6kSwwcabl1ra5AZELPh-dAKk9RDqrd9SFP5gmDGkTLafdT1JkZxaEswqCuqyXxkGslkmNTktYF1U6PTP16DFkBS9nozdKgaW5UqfqqX0Uv1O3lcLREMpZLPfezZMy-uwtnsv4PpBRHzZIxCC3qL6Ibl6YnvtGRdrvRc-mu1G2efv605XuWZXa8Vdioak2ImjPQq1FQBoPhlI89vXTi9r6jud2qVWyRXE_dD04ihTyF6TjRHDXjycN9OTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
خبرگزاری CBS: علیرضا فغانی داور ایرانی الاصل قضاوت‌فینال‌جام‌جهانی2026 برعهده خواهد داشت. فیفادی بزودی این خبر رو اعلام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/25620" target="_blank">📅 20:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25619">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKNu8a98tYFEBuQ2BB-ciOtQ-tllM4Vi50tdeOjMNzsLGDclhX2kQ73LAG6uiTHL9Cu_0rHCktHtypJmhJ4sMFol6ToXTV_y7vSa1DkkF8xHFlFV8Ca-eCoPezZe4S1C7x2l5vgbsscdAsjkKHCjjbkJEfRR-SNyv0pw0JhW9yLL_fQnlvY_rqpAGgvQjeetMAwGhESlCORf6b4iSfsbX2kUaGWpPtfMV-jHt1rnpSEXP8S3Ko3bD7wfNJqdJiFFb7ooI3n3JwCQNXYxYeeUFBmsLQtT5akk_CFkxyKjutEZ1foxI4hpKteXDYXOz9ivRjhb9UH8jcTAWRfGg9yHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال: باآسانی برای‌تمدید قرار داد او به مدت سه فصل دیگر مذاکرات مثبتی داشتیم و توافقات خوبی بین طرفین شکل گرفت. امروز آسانی برای دیدار با خانواده اش به ترکیه رفت و به محض بازگشت به ایران قرار دادش تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/25619" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25617">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f84qL0VXPLViGmkKMADWFZQkdfvackM-afOVdcdv72h81jkhzPPxJkYh2cLNCZnx6Ki63Lo8qKbtowRV6uDdBfnjQq0GHYg1HVAE0cWgElC26cRgjeCqKYeY38lhQ2BKX4VcIqlOmZl1Qr87C3a4B1foy7wcFBC2ku1W60L_M-9593nq7pPLaxbyi_dyqFshSlqMsYk-FpLshGyIldfvPNCBD_QWbA7zxDzG9YXdpCbce_c0qk6DKY67rfq8Cb3y5xDQli7njpEtLWJErrdqpHlA4lZbhIfWVwea8rHoaCTcBG3z-RdfutzHiTYUr83ik1Kl34f7P358njR82RijKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/25617" target="_blank">📅 19:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25616">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnG0QSrMjZkbdd5ZsYOrHmwubiPUXCNwSKL1AylJsdhf8_9hkfgC7_o1bIRZO6qJbfQ2ao9YCxV4DMyjkRjXhwPdrLWWN2vdYEaRNNipyuTMrc_PnpCoLg0-PRje1SvV3LINRHJnJJY6eD9Q1YZCoLCpQKXsC2nyu91Bx7uoPAVsDWVcRUkvHEfrgUT44G1Sst7Xdh9wM2g23bu18_VPuGAzOm5fd3BcoxgD7zFPNOxZhs492oR_M7_G3698qY6dmS4PBQ-uFQU90FQTPRw2e4Hj4VyMtA_80Pw4JsPWLQqtLZyU1XPJZwvcRbMKu6ye42xLjoftQZCGOZT_O0sAig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/persiana_Soccer/25616" target="_blank">📅 19:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25615">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2h_qpucV6cA97uc4K-KjfdGeTJu4swwtxskDnMGNLl6ZCuEJSdXgKnDRrC8WzJTa9PmoMG1FfE0PINNWPLSwMBvTd_-lgPQXOffCc6tVaq_CiWsWh3lq1sLj-CAx4w60XK0_dEX7l37Z1UHK0lRu8-GMPgGLSlqyG68bztKP2YNYAzQUye__L8fmcXadXabDZrbkk800vYC-a01cF2cNwvT0lAkdMVZxcCo1LnmcBsFYFNCMbbbvDJMiGqfEgOBiFuEhRywEfj0uKu7A8BH4FECzL3iYHP8mNxGhLKR_v76J-QlnQLrbB--CtwOE9Y239_XMMhO9VxpWgEZEEtAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/persiana_Soccer/25615" target="_blank">📅 19:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25614">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=SRSqwTF_de9jW_BoUBIqShAroTgwycUnObSr-stJz73r4C9dgrHuhczsDUbmK1ibXQB2-QLUtLtt-oS7xah3CfNaPUN8Fpi2Y8b02PV3Yv9zSopHD8_GBBG8t7p0tVkKjxEoVNC4zSHScKJDZE-Tq6wj0HXMSLjTljs-ftMr8z_z0amWlThWgkJtkiFAwUjo2dgx5s9xwpL5RKYPRYaVgq-qGcHzTBJFRosOZq9iHo7Dqr5oVPEATheI0-wZyPx0UnD59W56kzeZ3hZcBbjrA50UsZFlSxcriNCLLO0KQQlyqo2AWF1PV2ujuDlE0FaJHKRR88j-w2lR6px37lsr4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=SRSqwTF_de9jW_BoUBIqShAroTgwycUnObSr-stJz73r4C9dgrHuhczsDUbmK1ibXQB2-QLUtLtt-oS7xah3CfNaPUN8Fpi2Y8b02PV3Yv9zSopHD8_GBBG8t7p0tVkKjxEoVNC4zSHScKJDZE-Tq6wj0HXMSLjTljs-ftMr8z_z0amWlThWgkJtkiFAwUjo2dgx5s9xwpL5RKYPRYaVgq-qGcHzTBJFRosOZq9iHo7Dqr5oVPEATheI0-wZyPx0UnD59W56kzeZ3hZcBbjrA50UsZFlSxcriNCLLO0KQQlyqo2AWF1PV2ujuDlE0FaJHKRR88j-w2lR6px37lsr4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ یک سال پیش در چنین روزی؛
تیم چلسی با‌آتش‌‌بازی‌ مقابل‌ شاگردان لوئیز انریکه در تیم پاریسن‌ژرمن قهرمان جام باشگاه‌های جهان شد. دوره بعدی این رقابت‌ها احتمالا در قطر برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/persiana_Soccer/25614" target="_blank">📅 18:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25613">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=n8v77FFc_07bAoZu1QlgchP4CsB5MWeesVv8f9ANGLEDgb_oMbJ4w3v-RrYdEEsgyFA3TnHRMs3x69vpNHscKNVO6q7CXrjdgKip5vlkMj16d0yB9mFrhLeneXhyoB3RgDRqiWpxP60mPR_TJiME1HqV-7UFlADBWqphrkhAZbaNk0xH5s5VSNUNB9AhXC0ASCrV3rRuWfi9DZNznrDzhVGszRDB9fFJPWu_g-W5AJ4iD_eB2fcdegqz_GNTpk7ptl7OoL1-oC-84I8mWGvunOHoZZnHqa3TuxsRlzrpwJBiTMFKwCUXVmym4_0jiw5Xdfsf72Z0Elw4E9qNyaHTVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=n8v77FFc_07bAoZu1QlgchP4CsB5MWeesVv8f9ANGLEDgb_oMbJ4w3v-RrYdEEsgyFA3TnHRMs3x69vpNHscKNVO6q7CXrjdgKip5vlkMj16d0yB9mFrhLeneXhyoB3RgDRqiWpxP60mPR_TJiME1HqV-7UFlADBWqphrkhAZbaNk0xH5s5VSNUNB9AhXC0ASCrV3rRuWfi9DZNznrDzhVGszRDB9fFJPWu_g-W5AJ4iD_eB2fcdegqz_GNTpk7ptl7OoL1-oC-84I8mWGvunOHoZZnHqa3TuxsRlzrpwJBiTMFKwCUXVmym4_0jiw5Xdfsf72Z0Elw4E9qNyaHTVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25613" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25612">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVBIywIztnCxcGPvZbkvUnouvHXqIWzL4V0rYrWUmWiyJ-M_9-xmqS33W7pulY43ou_apCRua4P_RdTDCf7qg9VbJz5jtYzOOxSHmzp0qDqfyNIJ1bm5uwiKHEHmhTOVqyNbTtGav0NqqPRbiByAMUhdCR1F9O8aPmcrkNgQl7aaZ60EaV08ENnxJTZu26k0TnNg2M2sLCwxP6MM50sfsY1Y2ui0QiV64FiIGi1xj62lv8oUuh6-El5q33m5d0khGaXuz1-dr0zkecYRm_LE5laBO2QLYSIjtgoDXLzTrkD4uvPW3Ufp5W61kBhAj_OX2XPa3unQDl0bTZDmR24Uhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25612" target="_blank">📅 18:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25611">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlYDfVU996ExOGA8F49rlpK8zukJKTuePZydOWYKIAvWejljHScysVVxN0RC-rxsf6aaJJp5pGPwqvow1Rs3fUdy4VaJu2aQLgsocfhGNsp5JOyGgSMPK4L8vP-giy9pJrIXNtx-TAGLsn0nKiaNpA3FeiwAPZ-P8eso4DD7QqOzGLaKD8NZCuIak_S2OficlRsyR7kb-zcAyhLmLnskkGAK99MdwDVHQPEwH9Gh2V0Bs_MZ1PiqyuMGtXDm8eVdUAQ3QDtcqoauSpOD37I6azJsG-EhFrrneP2QPbK5BA8-Vv_mt42hClfUT21gTIJF6MfggG42Qq1c_rZkzRCsgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
مهرداد محمدی وینگر سابق استقلال و تراکتور؛ باعقدقراردادی دوساله رسما به تیم فولاد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25611" target="_blank">📅 18:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25610">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfJj_oLshOi3JynEd_slyK4RWotXo6bp4G4cVrWMas7dWNgdZJkMN0DCnUvpAxVvCNYEYoj66PO5mdhmUsOL0LSzdINoRQQ4w9aZCq92T8UHXLPG3YgOGVJuqxrWNEDaezZevY8HqnmSNpeanDcAlZ3ZGiTBGtqw4F-siRV9P4kNBdH4BaVQ5uTZfSl3ho5uc-5KiP9QeSaCS_BXM5lWxexNN5PqelaZtT-ner6z2brh4ttRgMXBMEuiwL83JY1IfrU5dqxmVyoV72ZKHNTw-ru1rfKeRnCcHygQ_xlhICtIihiWtWYYyGZYQ4fYII-yGhgvnT2wFFB_yFR7XWhaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محمد کریمی هافبک طراح سپاهان قرارداد خود را به مدت‌یک‌فصل به ارزش 65 میلیارد تومان باطلایی‌پوشان تمدیدکرد و در این تیم موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25610" target="_blank">📅 17:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25609">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTCwnIiCz1Ib_fcaBfIhoAiU9Lpd-hAtiIaE_6GXHXuS9r2nlXuSBzVJltEfHXTCWs05lJp1ki6ZCDeqLddZhPYt1m0mamW_u_tTngzxfPRujA6CDxImtTMEy19WwjVKQ3WppxX15zkiaMLMvFLVUeyX_ZYR20MHzm4maklYlq4uFqEq6BTn2LaqWmc5dq9Gt_pV-4Cewa7RlWaAtxlaHUU28MTPzkI7umFIYRahr17_0GrKZVFFRjX584h5yPjW15wMW0XKNDDdr9LAMbrDdqJwS69_40vsKLT_hLv-sY9o_hit9iu-MJyZhBd1D7MR1sPeqyTcJhaeXoMx5Hd9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25609" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25608">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhO4hEWnMs-mDYIgC1iHkpU4guFtcanHi-455U2yc4RT-FioXRGD5-YOyNe4yQuIcawLmf8KRjOtqWGwmV-QYEogRlmzRgXkz7GNbOk-Nr2o0hLSztaLtwWYqCZgjFiSEgS8o2m35qYdHJOQDy7BenyxCapjNT41BZLdmiI98xl4DuoFzscPwCtoRLbC2fmX4lTke1d55QFEl1VDSCmBdYSMmLMCpfB4Wf8GGf0gbmfAD2v7-4HByXGhHjDr1qEXf27WEsMHFuF8eOPLkxHeP2dPWNPw5RU61f5X70jCjG_3N5bEfiARSVTgLrjE_X-bVyALwzEGRxeLke03hKZifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
خریدخوب انریکه‌برای PSG
؛ لوکاس دینیه مدافع‌ چپ آستون‌ویلا با عقد قراردادی رسما به تیم پاری سن ژرمن پیوست. آستون ویلا 10M€ گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25608" target="_blank">📅 17:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25607">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA811jFkyw6EEyMlndWuv-VP1wQg8ssGwDKCDzqJ5cU6hP6Ez6QN5m70dDzhWluobMvrslBCfzUPjccD-uKHC13KcT07chz0zlZmKyso90TYhUyk28qILoKQVFjiyCql-0gfC6YW0FOaMZpurBZC77QnYZ0P-GiID-_yR2dwvpgB1b-TMrRS3mOhXAav1_ial0aI1il_Gg7btA1imR6xvWZB_LQrO5u_rRa4WQUst-7OgQjwGj_cvAxC9LBKoRD_ZvvhKscPR4C90WcU18nzuthOBpLQKHJVFLfzm58qnmDWFYW7REkl7GjCVRiXsg5Gub2MhAg_TpgVBEXFXcLGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ 5 سال پیش در‌چنین‌روزی؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/25607" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25606">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T09upmbxWGwcQStHVLYTHlTiWMi2H-IK09ZuxgixPO_JUfnNukGAl0rMehMNOdG4s-siZiMRf6L53Qr2ubY-iu5H6zKBscXQbEg1qwCX_VrDIJQJnQV8LmtIgldZ4o33MYCImtQ427ZiJyERbCNFm4Gjs3MVpy_KM6y3HoQ1TmA3f3Z93R2UHb7csSa8jFu9oNkMgNDEGjHKneTJeGSFdc9BM_pG5SW8zrwKPIbHz6tWFEkdAxeSsAdAgEdgXaECw_pA6tVxw-5TYxr7OLe6Z1GShgySoqOEdDuqETDC7zfO2Nsnbp71Vq_1Y_dA-OS6t9H66IUrE6afFCvBI6W8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25606" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25605">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IddVUBB8qBThQG-gJO5hV2q3Q57QO1B9c41zIou2XzKio31JuTC5W0CntSKZc7hihBMmKWc-1k81tRnBHZPPIReiCw6zsrlTT3r9hIm3uR22qCGNosQp_8XRICVW9vm9czhPtOlLjjJ8Ei81E-Ijsi_EedMNase8F663VGRsjIO_Ms8JvZxeuF0jlrQnN-6uFcpZ9feQOVsbesMjH3Wdl4tY681mVs2bRrkHmLXGD7v3BZjTm9dJ9CNYuri8OzXVONpEK0NjdJQ4gXCUqO7cCz6e8tIxjfh4TpgN7aBMyw1oNXCrde8ifaizuMU8Ggp-Y2VtPIY9MLS0yxCK3N4RCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاقه‌ویکتوریا همسر دیویدبکام به فوتبال کاملا درتصویرمشخصه‌چقدر زیاده:)از سِر الکس فرگوسن پرسیده‌بودن‌اگه یه اسحله بادوتا تیر داشته باشی به کی شلیک میکنی؟ گفته بود آرسن ونگر و ویکتوریا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25605" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25604">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge9xsFwdOaLGbvSbbWc6lvRE0hBg3j3ghR-AJMdyvdoEW40s7AFZk2FTXmdxrK0CfLR1KPq1qaMP0Uc_x8YdFrhEhnGfdS4Q6TBI3nset0EgENmXyq7PyYpawHjw_sdyHbgbU6AFEVgDPCpfvdWnjlOh61HV9OJjR7EsTk06c55GrNeOeQq-yFHgWq57G_JZBh4XgQ1LmvRvuAbr02L4dxnWnVm2-5sJZK_a34-5wwuzUKTYhHcI4Ucq0fp-HsKkgPQWDCyuiBTHuwYAJhPY3hDbkQAxF89IOjMjEgRCoycRKIJgCDREFyDwK20R6ezjMvmaI5yxWudeiXNuv5SEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25604" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25603">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXkTqWZFEQCMaFYEld-L2aKNMCm8DvdQtXIXe0LVUIA5Zje6_lPsPf4Hqbvf4cLO3TlfnYxtMS53Otr4G-z47txpGm8hBkqB6b2tg5GJYLvjefigaWsx2kskF_O1Sf9L32Tdu9LI7U77PnJRTy1l6Bd187R2cy0waj2JSes29fepzf8fEL2zQIFWwJAqCFsKzxLH5TxFs7c2f7NKpLf_3zp1zEKAJ1YtpnBLGhc5iw1bfto1ZQAPGhlcCpnqpZI-vVYpWItwChpjNGvPagtrszzCDawtw8L2np9dtCypMEbXqFayJLDen3uxswG79ce2r7BaAmjyZ-lsP06u2B3lTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25603" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
