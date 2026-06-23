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
<img src="https://cdn4.telesco.pe/file/t81a61ha7dw951owfe-wfSmRb9ArlCuFugppRJp3lToPy1Kddk_m6kP_ADQy4Jf6-nBZDGs9AAUICR0xxDtRbC_vLH29K1yN8RzLgbF5WCQMVqV4JwUvinF_IWroRHPpt8wIMBC_fwELPtEl4WRw9JQ8qQbl4DCBfFKTTfbK7cKQ133McaeC46uG9yhWj2ZXLJ6ej5PMiD29mTZ9BIa4LAoRE83f6CK5XwcvAenRA2MwDDeajnCykUgIGDFDQ4_23qP-Yjlxz6sh-t_1plwtJx06QqCtmhoRK9gbn50wAshSdn2i9RAXPx4VDZw3PgYNMMi_Zps2LTLuPrT7pn128A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 00:41:14</div>
<hr>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=qU8mOqCIN9G4DbHiiEQOiPrc-ynPll-Te3G-zxctFx4gLf--KEPEB3rMXlu3_g_7i4vZ4p9UAmMxPhbeWYtLRRU096cnz63ysRYdgk4l0tCBPXfxTTD5sgFV4Ro7H_Ov3QofHj-8Gsl--f01izRyfg5WbXFZokbGCVnEN9K9FL6qcMJJXUKFqk29_LUWo0eohPNXjchnWTw0cKhjVZcUsdIXaS7Huq3bbESjSWsZ0xVLvVSwWQbNns_8NPqZLugnFtm0iin8Z95-CnfqPAy8VahJAyfGTENBaJ_lrskHmr2FNn1pf8IR1vDI89wBpQIrVX5Lh92evywn5wzuq7bgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=qU8mOqCIN9G4DbHiiEQOiPrc-ynPll-Te3G-zxctFx4gLf--KEPEB3rMXlu3_g_7i4vZ4p9UAmMxPhbeWYtLRRU096cnz63ysRYdgk4l0tCBPXfxTTD5sgFV4Ro7H_Ov3QofHj-8Gsl--f01izRyfg5WbXFZokbGCVnEN9K9FL6qcMJJXUKFqk29_LUWo0eohPNXjchnWTw0cKhjVZcUsdIXaS7Huq3bbESjSWsZ0xVLvVSwWQbNns_8NPqZLugnFtm0iin8Z95-CnfqPAy8VahJAyfGTENBaJ_lrskHmr2FNn1pf8IR1vDI89wBpQIrVX5Lh92evywn5wzuq7bgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZnzcXi4VhY_axKvqoYRO2rfQnf7fLayxJmCB05UkLqK7j48x3RGororqUIAXF5Kqq3umjwVbub3SAo3kuSf_phg0Xvg7jFj32zT8fKys3Xn60JVvz2rt1Zj9WXvoIglTkTOsqh3hIl0kMO9c_OaDsiTXJRBiV4SGm3AcvLwuISPNJb4BKtMdGBNtli4pmeAudprAf4MKXtXBflqSUnVRmrHEQ_1AYvxam9SDhk4PVuKXxjWX_ay-XpgPwV9ZkIPsH-pHLe7lz2kc5Q0Poo5Tz_sp9zj0sgDIhylyeKzAR0i106ddi97lUePfE9J610v9sQjfH_fQtfAQjP8V1IrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=MTI0eR_6nXzd3uJpbAw-ApIQ_6iTECTej3gEMe5gxhsKWI6E3hggEAtiB7Q00rucEDmrn1Um2DUaEa5jXViCRW4LC26rkIElhZOAOsrVtugBQaukP36-1XKKXejx7DT4as5e8YAw4L-G8hB3x3HAB-D0Ki6-Q7UMXtta98uB1I48WJ5TZx1jP5TtUayiDFPG65gXU8zQLEhWoOiOpKIMeYWeBwxKMIusFLLjbEJuIA1FweiBTrik0fLK5LwFJbYMIJeKl7DAupTIEFa1rlPO03KKGXNYvbLfw5BNi3jD9_0Ko77idTefbdNiXM56jMGmAUhKNGMBm7wkJDWAv6wnBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=MTI0eR_6nXzd3uJpbAw-ApIQ_6iTECTej3gEMe5gxhsKWI6E3hggEAtiB7Q00rucEDmrn1Um2DUaEa5jXViCRW4LC26rkIElhZOAOsrVtugBQaukP36-1XKKXejx7DT4as5e8YAw4L-G8hB3x3HAB-D0Ki6-Q7UMXtta98uB1I48WJ5TZx1jP5TtUayiDFPG65gXU8zQLEhWoOiOpKIMeYWeBwxKMIusFLLjbEJuIA1FweiBTrik0fLK5LwFJbYMIJeKl7DAupTIEFa1rlPO03KKGXNYvbLfw5BNi3jD9_0Ko77idTefbdNiXM56jMGmAUhKNGMBm7wkJDWAv6wnBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlMIOJlw_iShtuWZ79GtAT_N28fkQm0ROkVh92OISlfVGBSXHWZtQc-8ZzOjL20RgyRrOYDqrP3xeNOyHZC0gHpsiEDbpF5-gxF3E0V1QaH-WtMv4WjqNXExmBgjSb1_hgGx4ffQbzO_22VmknPdouRL-CfE2zNmG6luI2O8jfakT_EQVMzpA9et5BLj4a-c79IoAyyubf3vfZzj4nk6c67cRlsr3RcrVs8hz3EoPWuQq3fJKxv_uUZQJEMxC9JjEz3k0HyCFftHFQovmSooFLetAOSlduYn2zOaFE0YSbPdDQtLxUUfUbSJLOhTLAJh3tgUOJZJ0c06uAEYOErTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y11U6RkLxI9_lsLYqvEiPpmmokN4Q3TUaMc7oSCAmglU71GrvS-xTTY5y44Q6W3KhduxI2KBRimwlN8lDxRb5L74KuxYlXoZFqFQ6yH-xhjKnWR7pIVwaNr8pNK7JfRdeB8nnH5HoqvIeiApTXhIlv1UGoOtxzcJuq8UPZdA4_LqkE_cs_dBCL_HNmcW5qPUCa0E2-TSgEPLlkv8SOcieLCBnvzxaWdTSp7bNU4yDAKdz156J2NqIT_aHSshE8NKlYTiTT0Hr8sqqKLceIG26agNx7PpqneylOyz_Xp5n5NFqyvxL-W2UuF8DzBMWrW0rd9PJPpt5ViaFpTD-V0rAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=ZxAou3ppvF4Hg33_kLYCs8Gb_UFPxH4hBcjLqwko1UU_hdXg-ZqIJzk7Kg8Mf1IPmjj2Tm3VHNgExsssYmD4SEBN0TjSuK3Y714ga-0vR6nQd-g_pxkH1FFYWBQnUqOHiylrCLJ7rB8kkKmzzKbiHGQ9cWHy1krvNSSLSOu1Haw_H7trZUR4moxgdE2qt96GZUaL7OC-FQfd-Uh_ARjtQlgPoHtnOpXI5Gaf2UbB-hkG0AMQt5Nb0droy17T8NhBgB2bh7gg_DB0mwBHek0fx03dPD5sG-X9_1xNhFnBNt95bKOW4G4LzNJ2gOmdl01C7cCqSBzJOukticKu4HJOJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=ZxAou3ppvF4Hg33_kLYCs8Gb_UFPxH4hBcjLqwko1UU_hdXg-ZqIJzk7Kg8Mf1IPmjj2Tm3VHNgExsssYmD4SEBN0TjSuK3Y714ga-0vR6nQd-g_pxkH1FFYWBQnUqOHiylrCLJ7rB8kkKmzzKbiHGQ9cWHy1krvNSSLSOu1Haw_H7trZUR4moxgdE2qt96GZUaL7OC-FQfd-Uh_ARjtQlgPoHtnOpXI5Gaf2UbB-hkG0AMQt5Nb0droy17T8NhBgB2bh7gg_DB0mwBHek0fx03dPD5sG-X9_1xNhFnBNt95bKOW4G4LzNJ2gOmdl01C7cCqSBzJOukticKu4HJOJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS6__bZMZuKC-DVp2Ngh8b93p5rnHVz--dfFvmoob3lOKw3VwC076eG0BSN-TUU9OMUNA7EfIkcKDepiKcT7CVvTUs7JpXppJgvQ_EczHNDRENYEM6VwXXQch2fFnMbyLV-N02bUjWcyqWKdtTXsn5wItdM0ZKlQ1m7PzWmMiBFfdOZEPsq23DhyqWzfDEFnMU9zilDyf7G5GSX4wHn5VFoTdhlEiZm7-103qITwdX9xbV0_1dkXawWmcniEk5iKM1IGP7kWStoeq8KFXR6_mmHN1KchRTx7xwAPTLdhMsh6bBbTiKCgm2lR4AATbFfl2yMfYLlGKiaNuu6D6WCphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/24164" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=jASTI8FApPvTDYxNSsgtPiJKnIQWOVzTNJ6S6f6Mk6GwkX4Biel3aO0twCVHfYnCZVdzjfVsQpwdztIqMNQ3VUMYx75x-GAQ76WnifopAwUwctDj9UgHABQIHZwvFhVJSHX-Q3M0o3D-eyEajPiVbuxKBIc-sbcne2hQVo_OHy1YY08C0jLWN9brrgHAWyP9m6wcKyEYixlqa_dTMP4lr6fTq5JhAHuJxSoaR2pCopLpKKyv278Sv8o9_LaswZ3Q45pO44cOhnaILN9bjUvxoSrkMf4jiJ9TmSaJr6zpP9eQtAlFupX8vBMQb3Kglt3bE95n5roZDCy93slS-oJLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=jASTI8FApPvTDYxNSsgtPiJKnIQWOVzTNJ6S6f6Mk6GwkX4Biel3aO0twCVHfYnCZVdzjfVsQpwdztIqMNQ3VUMYx75x-GAQ76WnifopAwUwctDj9UgHABQIHZwvFhVJSHX-Q3M0o3D-eyEajPiVbuxKBIc-sbcne2hQVo_OHy1YY08C0jLWN9brrgHAWyP9m6wcKyEYixlqa_dTMP4lr6fTq5JhAHuJxSoaR2pCopLpKKyv278Sv8o9_LaswZ3Q45pO44cOhnaILN9bjUvxoSrkMf4jiJ9TmSaJr6zpP9eQtAlFupX8vBMQb3Kglt3bE95n5roZDCy93slS-oJLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4DDaN1wdOiA-Kiu4GQv6nJ4d8OuowsIpduPgmvIpfXf7uUa8sJpf_Y0QWzBtnP2xgYZKHOUg8hmIAyF1X0SeWlbBXRCFwx1CKAX_RSDOtOZW0ifo-FhM3pdzGG_9MWCGmoDYp4COb5qfwPScUMk5_b6aqQeJ2EwfJf67nmuxg3BmVbNBtYByQclupNqx2toz9ZjWBTc-XuV5yknVcQhjlUAhGvXfTLTG6603wwdaX8adjmcdSK--YTDmWWgluBueobrGVyfosxsfmsqX5MCohSFgk2jPfCVzydkJWNGiAcphmunmvJbbmIv7YEG0FsKW8bj435H0zOjfFUCJCs6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A99sybUhim6GssUmN9vlZr7W0IitVolySeDiWP9a64tNrIJiW5q7VCZDcC7XzWPxAm93XoYjL9BJXufgDUOY7xMoh7E53K0wRnlTy4Jh6P6GFTCBbjmWii6nuhoyICLn-7yNxLWlEeBYOktFgN2XIP_tKVCx6i6AG602NHsReqdzSfkSARrTJc7EBB8B8iXZeVCRel8UWSqZJytfa-7jDesSYW17Wvab-PdbngDPBIrmbKoaRvE-P--NhIK_sb7zkxFrLsHajHvPfkot5e7uFAA1lkL8C88RnG4abxRfKbGmS3Zz2HrxsrlZU7WXlQqEH_qoI0rP-owmT1Rar6plJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE-eYuyTSyKSO1UxKdcDolsGCoR_LEwXJj94prPg_7E5fTjzkTOLuYj1bWfrT3fkK45G1NB1RwGJ6Qa9xOf2rt6LccBScngUi1vujxLPh1vy8Hv1NChzvvVDBpX4cLiZ2k2m6gG2wTZs0v9LfpRHfMTQoZ9XMP9xtjatusRQZ8zUX8KcyH4yIYIPD4sjAJCg-Zn40UqI3v6h0sFMVrPO14PdMa-N-bOSD6LKL2LBX5v28TM-q2B--vy9680Mrn6NlDV7CHZrkco7X5dwTjhWuawKOcrXtlFbNj8Z3vdaLcCCPFUR_KpWOeiCX62INFJxqFvqgjVAZR6v_yzXH6Q2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ8NVDecq1riAmI5S5tNfUVp9A4gWuqFDQltSY2aGC6oUgMpbmjncJ-qO0jKwCzID4tyQJfI8hGYeqIoP6D7mmKaPizs3xiNpPPt7Pr9mbyWL9CQQbK-EA5n09voB1AAHBw7u5ZbEAD3-WPdYscYDF6KYn_aCY7ZBGm5f9DChF05FUP2sXq6O0E2f7j9anM9HJedWPrBeZWhobSw1EVOJyZQbZvuJCVUqnMTRqwCVLav1F59kkbUUXsL6IH7-aDKUr1PNgFvV5zh348CKYm2XQBna1rUng_VkgaHPF-79A7qg4LloRPQE4mtdvQlAPm4m6gJWBWqMxLP64nw8vweJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuQerpssYYINMYVgDlhWs_KE0U1PJqbtCSrHb_LRnHM6-ETyHcEXbKXP8YMVQ2KZNMyARCa_RhFBg4vpcAE_qIuWTaJnKP3fFcpBxaKvBKJHc_Zb2lEh6-VZ9g0Xnm70OE9Sg--odKs_opQZCJHOszlgqHhQ5SgiSWV8QQ20KDbkcV4CKlD0dmG_RUQeJkbjJatcZf-GhsaRbddWvplklc4xzXYMH0tBm7mPWNkGJ2Ugajv0bh7uPuZrmq3Ib7NhVK_GWIViQFHN9a1zMCYZHguY4UsngOeROwKLPEnvoVTZkuxjDgJQc7EsJ4TMlAgBpyBsBiHtu4bzXBw6tdWsdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gp4HzEQ5CKneBxPzY0NB9FHa7gPJ34W_LwwkVNKC-xRzGMQomPwWE8Hv0W04bFgjwxHzJ-JfzN1SHp8MiOk80ORVEU06M6110GXfOfK-TIhl8M3Yj1o-qjWe5wBf4amLa7dfJ9xPsq5kLuzu9MwBxGeGUwVweWMcA5043XN7VxV7ntZOgiqCUJG04C5W0F8PFKkjnGqG_5urpTRaJ55KhgmF7lL9bDsZGXn0YqNiOvyk3tD4P-_PZUJzfX5kpjqZpCBN7EbMBGdZDTcsHwmtYUKtxg606RYD5LSwbZo114wYElVo0BNws9YI8lQTyrwoGWU9Pr_mN5k9ydHF2-LUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EA3JZbOFDe50rqHbunqPuIQqpDYu_P8Y8deaQe2hl9ud-ob9ZiRC8DypfqiwJCpb5L7Lj9Awp-PjoiCCDwRJSaBpyJCH59gQaULiYwxX4HshhWqzxd5aTBnySGv3VrdHD7ygEvE6xbS2YSsZYV27R45YVK2hi_hvDGFCsUmhpSjgzEXbF8OHsChzknAe94L3XRa738HENVFrCJ9Vzb5zRkHAVaVzTRaR4q7wVnTfkzTU7amaEQh3dQIKQ0_Vn-dqjY9v71qFeOR_2kZORNf7hpMEJXjt1PR-Qp4YCyYMTlK6ADzeHTfahpc1PKud81mQZEuc6oY3pCyqNFa58w9y3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p94E9RXa7sWWEwVB0DECrPVmdCegA43fXRx6FOe_gKpNR3nl5Q7Zt1XYaGXgyzzRz5k3e8afYTW51YALkmRUYTsm2o3Pp82tUAsKFxz_J_gYmZlYdQczGJ5K6lZpwaUSsvJT049C_m0WkjBVppm7v5spWNXu03HyhQLhz1R1SxdbGmFOy0lpErMtEOT9kGFKLU4JZUY-kk2Tm3IGhLePaigr0uZf02Ucu361--k5wHAFHPPEN4YjE1vdyk_PWRaqSRh6Z3H742ZzQFBrK58ldgVsHwjMG5PlU9cU3ZhgTUnB_Mr7d9XLbuW-8PZ2lfpNDT9uldxyMxVv7shbRw40xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=daDlQ-Bwohrakz53sArQkuw9qgAWMiv3YOyfoUFBP_QJ8BWPaNv5Orr_mhxm4gLVUoNYKfORu0RAwsJeBOQRcszIQBfABKY1bhIKvpmH55ydKOP4lMH7U1yyO3fF0KdSKbZ1pt9xBNB8UlzXcJUfp0bXe2Y6-eay-StMWYns45VXDPvUWEisbPh2CVTgBgmUB3t3c3kOc4MgTj_mDCHU8tuhZbymUcAW_iOUbGf6H2F0SzoxHhoHR8sBHX05ZG0aoVkx6zJlKLnoRSsyombQ0go4cN56gnsq60h8cF39S-2X4pEah2EPn5g0RoQCPmhs3rU15YtPKG3L53mYoPX5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=daDlQ-Bwohrakz53sArQkuw9qgAWMiv3YOyfoUFBP_QJ8BWPaNv5Orr_mhxm4gLVUoNYKfORu0RAwsJeBOQRcszIQBfABKY1bhIKvpmH55ydKOP4lMH7U1yyO3fF0KdSKbZ1pt9xBNB8UlzXcJUfp0bXe2Y6-eay-StMWYns45VXDPvUWEisbPh2CVTgBgmUB3t3c3kOc4MgTj_mDCHU8tuhZbymUcAW_iOUbGf6H2F0SzoxHhoHR8sBHX05ZG0aoVkx6zJlKLnoRSsyombQ0go4cN56gnsq60h8cF39S-2X4pEah2EPn5g0RoQCPmhs3rU15YtPKG3L53mYoPX5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24153">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔵
👤
باشگاه استقلال به نماینده رضا غندی پور اعلام‌کرده درصورتیکه‌این‌بازیکن‌حاضر باشه که قرار دادی 5 ساله با رقم‌بند‌فسخ چهار میلیون یورویی در قراردادش ذکر کنه حاضر است که پول رضایت نامه دومیلیون‌یورویی او رو به‌شباب‌الاهلی پرداخت کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/24153" target="_blank">📅 21:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WenGE_zY5OIr2Bb-j-r7Nvle_7LFDr1xUI70BQtISooLAkH6D1L7Y6G1b6eDwlw4Dtu2rIUb6YmGUsm5cWFGrRxE_-ieeTXL8HRFEZvXyT-8cst9BoIprYUBSeRN8fHcP37T0KQZimWRxjhvnPCotEzMiW6yZlVrzJtwOio6mZHLTnsUdDtR6Qc4VIz8uo-RVOMG0EYE1zWGZp2gqVAllKHj6mba5S487L0IDTZeE6-bBRtu5W_uY3ozGRfXYi7ZNGfWIGQhl3qqwpRzJqf1qkW6yJ0ON-amK39RVIycPagQXqjoYrJt7fH04pSz_Uxpf-1hin7yB4ahNyVodVqTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=rKFkZPTfvi9fyvTNvxi8dSAIG_-uVkrjR41hBoijg_5okOxWocLYL89DFj6UEVtPXV18yClCkmImMCdJL1YTfcBmB1F5lB6BTwEdhhxk7ld2XWyGbHwI-s7wu7Xc_n2ciA3Wfk4ygmVK100V-n5xOdARTBMe6PRU3Y-7X3GBlt8N63nWFc6sHrFmPnlSWFpYd0hy5BQ4G0W4Y33hed53k8sBqXWzAyWNMsrFIEH8UNge2PbUxomPNBiEGcxAHwW_WeE_2YXbHko9Pmdcdmr4Z0lX8wR1CdGOAip3gAeI2oxCBlhAMOin8XTG-toVtzlKmdXCvosIJfG8aOy6hKrFmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=rKFkZPTfvi9fyvTNvxi8dSAIG_-uVkrjR41hBoijg_5okOxWocLYL89DFj6UEVtPXV18yClCkmImMCdJL1YTfcBmB1F5lB6BTwEdhhxk7ld2XWyGbHwI-s7wu7Xc_n2ciA3Wfk4ygmVK100V-n5xOdARTBMe6PRU3Y-7X3GBlt8N63nWFc6sHrFmPnlSWFpYd0hy5BQ4G0W4Y33hed53k8sBqXWzAyWNMsrFIEH8UNge2PbUxomPNBiEGcxAHwW_WeE_2YXbHko9Pmdcdmr4Z0lX8wR1CdGOAip3gAeI2oxCBlhAMOin8XTG-toVtzlKmdXCvosIJfG8aOy6hKrFmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=BcDT4Xhh2GfQzG1CkduqQtxB7fGgOy8lN990qG27kEjDmmPkvL_oXoqS66_2FFuSix-m6rQDIHJ_Cg35UyspMP3o_WLjlFwEPTIBlJyTFpGjWk0SZXCiWUCnxDLMYbyRS1eYsfNa0g9SeGb609Jyf0C-8BnwT8KK66UO74_R_aVlHfDzqyvs-GqSjg8yFxZ0i4OjpY7t1XIomZqWlWEsm8H2O7WIWANK1_7TlerO8h6LeoyK5CyCMgbyYqX2_mu08b_U4DstChjB0-i-n4yWPu4vRanQs1_p4eJepWv9VKdWZvCEOf2_XUP1Xhfy_PAjrNEzHmMEciULl5Nh89BhPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=BcDT4Xhh2GfQzG1CkduqQtxB7fGgOy8lN990qG27kEjDmmPkvL_oXoqS66_2FFuSix-m6rQDIHJ_Cg35UyspMP3o_WLjlFwEPTIBlJyTFpGjWk0SZXCiWUCnxDLMYbyRS1eYsfNa0g9SeGb609Jyf0C-8BnwT8KK66UO74_R_aVlHfDzqyvs-GqSjg8yFxZ0i4OjpY7t1XIomZqWlWEsm8H2O7WIWANK1_7TlerO8h6LeoyK5CyCMgbyYqX2_mu08b_U4DstChjB0-i-n4yWPu4vRanQs1_p4eJepWv9VKdWZvCEOf2_XUP1Xhfy_PAjrNEzHmMEciULl5Nh89BhPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=YB6oapvWxEPloYZqvht2LKfQ4LldoRd-7M-O3i1XR9ah3nyVeJTfJSd0SrJANZ27S1ftbxoBQa8_Djoa3yEzd8OsN5dSj2IJM3N1F5SotJk9beev-Jmiwn3jQfpu9DBhZnHfdue_ImJcmErfyxRaWkLXtIdFHb3r_IIXPOHsnRIIVj9y3l_sxunURS_tIiqjhoXc0zX7wXEkciXCuYdyabCO9931bGiIKEIP_HvroxAY3T_6ZYYnm1IwJd5klqfEQAv2ZW8PINBIZyj3GPNU44vyu05MTjq-6IMFR5L6X8Dt295TLH9AB1pFfDd_rjNhL8Eq271ly712uBo3Sc8TdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=YB6oapvWxEPloYZqvht2LKfQ4LldoRd-7M-O3i1XR9ah3nyVeJTfJSd0SrJANZ27S1ftbxoBQa8_Djoa3yEzd8OsN5dSj2IJM3N1F5SotJk9beev-Jmiwn3jQfpu9DBhZnHfdue_ImJcmErfyxRaWkLXtIdFHb3r_IIXPOHsnRIIVj9y3l_sxunURS_tIiqjhoXc0zX7wXEkciXCuYdyabCO9931bGiIKEIP_HvroxAY3T_6ZYYnm1IwJd5klqfEQAv2ZW8PINBIZyj3GPNU44vyu05MTjq-6IMFR5L6X8Dt295TLH9AB1pFfDd_rjNhL8Eq271ly712uBo3Sc8TdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/24148" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVTyNoxZBn1rlomAAE7xR1wx2bNnJkLX82Cca8GCC4t7R6J2UPbHd9euxov9V0VPrKZmEYtZbFmK_ZFYhM6UzhSbZzZZAEgfvz_npZT7vVl2sQN-x4UHl4CSeyOcR_cr5F6LJADULsPI6vO947gJ-cMPbOx0WkmsZl6RrtV4Cpj2XoYcQFh2oOFZdoyZFPHBnOll5OmAdxv-lQ47fFhasmIP32sQSHCZcXIj3-aXaCq3g7mfHwmKdmm4NNtz2ioUciH2cNH0LG68DAGMZsuOYrSVta7D7cCVK2Lei383zj-q2IVvxLzARqjaMbAvR3yMVINozohOyCQf_nZ6jxMntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJTIZFFyqDackxs_Ap9Y8gl9w-f6ZKUJwgZJGWOAORX8tUilO_adwdoqvoZ8bPCFG7mIlVZU9ZSDYnOwiHj1DRQxV76XdI5sHCv5Vq4pZKdBBIU-6NEG8VquYJnhbTNZ6gChTNnNadTXIaQ1UMa2IQcRL90sTdKlwl31yd0gu303cDcddnrFrNRsKa8r6dKVZ47jXeYXD-Qz3Wg0NWpVmWWcG8-MbWLpGldU7BTSqEymq8RYeRZ6QV4gyFJtg03lf7a3dVKLJQG_SyzszalXscRwjiaeB9Qheuqjy5wctrsKRB81HFeeNHjM2FJNahuEceQbqRDs6VpQ1rrrd0pvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس دقایقی پیش نویس قرارداد رو رسما برای دراگان اسکوچیچ ارسال‌کرد تا باامضای آن اسکوچیچ باعقد قرار دادی دو ساله سرمربی سرخپوشان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24146" target="_blank">📅 20:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heBR88bjuIccDJFcuFnFxKZTEh35ti9FqB2nP30wSj9-LDfdS4KQt2JybYKsmr2W492_Cetw2JnjsJWP8O2vy7nwQLl2MpcDPRuchIxzEiHZCLyGCEz5P7fAPYFVApXb8x-RpLUC4FVQf4z4gfHrFNI2efCivZDgFPWWfSznXD_qEofizZS3SWbeZDP0uBFcRBuUlBzZzQpQR4Qc_d4ScpUST_1AerSGno_PqfXthMw0Cdlb2vHbATCLuclCRKi2iN3j9PkFAAqq9vk9APgBQ-adH0xeC0wJqM9ZzIsZ2I4br9KV8HmkR7mWa57gIogdqFacXB66oWbSjhi_8WcCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا؛ باشگاه استقلال امروز باارسال‌نامه‌ای به باشگاه شباب الاهلی امارات خواستار جذب قطعی رضا غندی پور شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/24145" target="_blank">📅 19:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7hrkHKV3koEc3KicXdJv13vhkZGGru6_RHDwfejsqT1vVi_QhT817YpVwrL-b0czD08u4cs6_8yNumZP9OafBRe8OmaVCkV6xwtB2oxIMsFCHqsFjNymwkEiwDvtUdnM3095HBqPETYeEWQgznqlQO_dHrh1XmZ4DZRRqFMCZ8eR4IZfxgBFceoR_JMDlBH8qMkCWghECsLomR0c4W7GQxnYKLssWYjEVI5qeNhA5tLKtWHInTeYG2dAFJMLN-_sMFGfhzX77yCcOcnf1ZWz5-BqZtfmHjEm44Qd2CTFrVCMhGgmQBu3m8NPR8T8LWqCo0vixk93KUmCtoRJL8spw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m629BVl4aQT4V_OoVFNxI2m5FQtYdx1O2aLqi7lj_gb48AY9aubMuT6OSb-ls9lKTYtKUg8yjFC7L-kXAN3nXzU9Lqqc4G3sSD1OwxaDzl0R3a4R5G-aKhOfyI7E9gKbEmWyBR6Go4S57skrfRm6DbO01-B938ycFd_SqrlG7AcJym2MPpOFTukIGUUZqGCFwgEQKumz3B0FmPGyTv64YiIOCtaPJAO576Zkbqj6XB-ncrbv4E1IUnHllPMGY2kfnuLKbk70UAh8WjSy9MoAE1WwWi1hazuhe2Ib4vW5gboDPo4WIwaL2jc-XErtMWBqIIDWt7ogxmjrZRPXCFxUfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/24143" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFUjT9EDzBhJYKIo4yJOyOF-o4mXew4L8GDLWajsdKl1szUybkQ7_OXVs1NLQKXA0HHxvVBMPh39vAFF5gsY1jVVshAL0RDZB5UgGDmIZitFKgxRksxIaf3A0XOOUZPwoPHpF8-dhwm8VnaqxSO2CCkbij262cquas7Y0OTA7k-PAkol_5jOUspWfW91zIdSQkrU3YVfvur2j5uEVHO_7oKejxKWIOLHv64docyD6eMOALj4LqfH5KocCLtm6MwlKEqK7AzKFA-maP-hpMzHHK-oGjR-ioyoZkDjodm-B7-beqpjmALp76w41PMNeeZ0d47W-U0gPRYvkJBnYBHgJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/24142" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24141">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA6993l6G-hORO4goUIigGrTcwz0NFlha1w7ITcD-ul-99TOQrjt0oznV32Fktr8wxqGS32_FBaNLDKnuS62DKsA84mOMYQ_98pa9QOkUXpRk6v1Q7QnH1W5ufCfCp8STESkMJLlC1Z7ZHYfarKouGoJ171DOa4HhRLrE9pd1WJef1c5FAjEpXO4aqTY_KKfqsio7WKjsCux4fCadNoequWRw3HntyqW_PWWZg-DQFYkppbx-qVOQyPSx95fivngd29uDYJXl9GmSDcMrcjdmpW971fDaAEie2SMiAGh1r9QFYi9reyCK49m9kNq7gOmg4kB0Xtrb_vdpIuUrA4uVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
برای اولین بار در ایران
🇮🇷
تا
0️⃣
0️⃣
1️⃣
🔣
سود اضافه روی شرط‌های ترکیبی
🤩
ده تا بازی میکس کن، سودت رو
2️⃣
برابر کن
فقط کافیه بازی‌های موردنظرت رو توی یک میکس قرار بدی. هرچی تعداد انتخاب‌هات بیشتر باشه، درصد بیشتری به سود بردت
اضافه میشه
🛍
🆗
تا
0️⃣
3️⃣
🔣
سود بیشتر با 3
انتخاب
🆗
تا
0️⃣
5️⃣
🔣
سود بیشتر با 9 انتخاب
🆗
تا
0️⃣
0️⃣
1️⃣
🔣
سود بیشتر با 10 انتخاب
همون برد، پول بیشتر!
میکس حرفه‌ای بچین و از ACCA Boost
نهایت استفاده رو ببر
💵
💵
📺
تلویزیون لایو برای پوشش بازی ها
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
🎰
همین الان وارد شو و اولین شرط ترکیبی‌ت رو بساز
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eG2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24141" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=kBexNI4uVbkqonrG3Ac8OrGFTA02_axG5u_djrRYCvA42f0QohO5A1AMo7HBIGglBq-VDEtJ6jS2NgxUP_frPuF03H-vS5b8PdKQvQfjizhK5rll9QLcpfLoqBKRNeM8VzogFXCFV8Tc9QGbGY1D3Rin5kZrg3xvKJb7T3w4ZVgU_Sc1ZvBk_s2fCOks07lM2RvLcaNCWSb-xM_TlKDWtx9HdBdwSGYm90uMkUxHWidT3oLPGUaleIxNn4m7j86eGqW2K6JNx0MSnanBJNidp6S_VKXwd8Pycp3bUpQpSZweJVxj2Z0uYpgnp6nab0F661sYEVvhCRcbwbuB9kk5yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=kBexNI4uVbkqonrG3Ac8OrGFTA02_axG5u_djrRYCvA42f0QohO5A1AMo7HBIGglBq-VDEtJ6jS2NgxUP_frPuF03H-vS5b8PdKQvQfjizhK5rll9QLcpfLoqBKRNeM8VzogFXCFV8Tc9QGbGY1D3Rin5kZrg3xvKJb7T3w4ZVgU_Sc1ZvBk_s2fCOks07lM2RvLcaNCWSb-xM_TlKDWtx9HdBdwSGYm90uMkUxHWidT3oLPGUaleIxNn4m7j86eGqW2K6JNx0MSnanBJNidp6S_VKXwd8Pycp3bUpQpSZweJVxj2Z0uYpgnp6nab0F661sYEVvhCRcbwbuB9kk5yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه ابوطالب حسینی به مجری شبکه افق که به مهمون‌هاش کفن‌هدیه‌میداد؛ فقط خنده پشت صحنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24140" target="_blank">📅 19:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGbsabvE6uffl7ENLEZ0-tpXcQWzgHlKmn2AXFgE7Iw1OyN-XdzoEyL9qrGP02Z6DPkzPJRRkYSfWmMcFT6XshIFiX9REFub80BCGiPDFgFXLBrNTk3Srsygg7XhooY8A3yEV4umaTWGabBDu51pKyc3SgZhKrXZDRqkar7hYgx1WuoQiSZgpu0e2Z-5jFfwpb5KMF5YQgTNG1yRtcILhZwTzvNYJe6UadXcTQHeRxJ6Gtdd1yj67d3GQWQiRGCT5xHLNzIDB2O5o5Nr8tD-0SZnQBRppjBKWOqLspp4s4vs9BJHcSiMXXTTBKyKJVZLkJn8gA4UX6NiYLUPhccPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24139" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1BgN--q2txIqlPpgxgg3VFdy8f_v5YhYsflVN1srrUCsh5cxWmKxkFe66BSnC-hYVOSwb3bN3HhZ3qwIqeCR3Aps275CDsdNsLz4X_zf_33zMPcZiuP_HM2kZLWizw-TTP_C-Hfk_RfMmE0VcMLq989NMGMaF7FdQfu_15izCdlBzoPRl3Kwb6en5uKlqfzZD-Vg1g4-tAJ_819FXMNQxFqPp1W8bsh7VJcRClvyVJIkdjZwMPxqVXc-3LA5nOwzzKO5PrC6in9NFDzmXSxY1zEmol4ZP-mItdP8GQC8Ro-jlIYY_fZZSeqC6AtVdM6i5pq5wWchoAfNDmhmxVPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
بازیکنان‌تیم‌ملی آرژانتین اینجوری از گلزنی لیونل مسی خوشحالی وذوق‌میکنه. از اونور کریس رونالدو گیر یه عده‌آدم اسکل و احمق و تازه به دوران رسیده مثل ژائو نوس افتاده. وقتی رونالدو داشت تو رئال و منچستر آقایی میکرد تو دهنت‌ بوی شیر میداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/24138" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to5Fkj-8eOisV1OJSPxogOLe3J6SknYGweLu4gkblOM1SHQo0c0LKwaWnZardh5orMlN9ovHLqKnhCOvkDDdSXV1we6kyHXe87wu19ftrlmIkEXTEqNBRwu9bKzveeFj1UILx3tm9jNlE5RXxD0XmkC1MOkk1Ir6QSjlUXyXhj1AwPOxZAPYZk25FEzFeXHbIlsreaaXhfTlWchHx-vErSYCFoEHx-MmS7mHesGccfPfhO9Lye4wwirVJ3oNMi1wL0HB3gmnmFlwCPc5UMcb8NNQ6_iqXQ9kSRJYQHAI1weZCIebTPeN0gPNEfnY1jIfVB4n4-T1zsb9KQOcJloZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo_RDBCwe2NzzLGkGc7-8BvxaT-Usq7AxgPo36WHEFjVaYCl7YFFRLWEv9oHhEYq93ruXK4pgDwFSZhtRJd5BwngEE9lSgLUBlOE20QJ1vMZda-HY5AMMmO9H2U9KtFgAyh6AXn6unq8vyi2B4hsH3nJWTmSh96F7LBeeFOMOUKyB-sIrDkPKhLDWEY14fFJ4tBcjNZ2qkVHOywHE23sWOZFqsawZU-bqqLYqtJ7-MaEtkKz1P6gfgRGiyOb2XYkZu99ZkM2TJXu0cJtDJOjqxUKb2ZVdRSJfkZGcpPaIAA-CR92Xc_MB5XoYLTkbK9tJQSJbQf1zLq_9-dzRGQCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoCDMwdKPSjlUPWL7adVK9p911HEDUwe-zNqDGSPyBQtGIblUPtr5f7XW2B2nsFlP1JDpy6baOFOed7VCO9q4-tLOuvJ7s0Rjg8T9XDCcYIeb_Egji4_oM3DI2hHhTbdeEQ0S7T02uxS2V76a5-kcPYpn-ezl1ljVneKcTQW3f3tGXnSqfV2Elq8-07YuUbPQpku2eHpjst2KNOnDktMSxd8LiyxjFYum4Irin_wkWjBljphzEpveaonOaVlzjjolA83HWPPri3QbOxwwwRnLIJc8s_sS4W9guthhyQptEi6NRv4sbSRgMtd6hElD09HMAVYCCuPTUKAZrJpvoa0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHSC5VQGLLz7WH5RYJXweVm2J4ZaMMrl3pGC6cCaafLu3kSfMasZwVkm7sdJCGMeKA8qvAdxYv2RFJJk1c_x0uzrjWPCr19RZhExdRBtJgudbdmndQv2bTFJ_wTrtyJFN2ljdyIpYpOiIgoRxa8yVPB_9xiTAzvqEdMMaA6fF-0OGp8bwOwotO5aqM5EhZNHSWqTZw1-Oa92bCQi2uQ8XI-CqGeiTi6i1y0BhaZHAmBnHhH31QMXIXWXkQJO30jW2xriNjT84GsATNzRyuISPBgBWRaeN_A-cWPnq-CNzQ0489N8Z_6PxaGi6XgKqsT4tgR3MUxJ5-oRgIbDd150CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=lZIN4n4ImoL5J2Kx9bMsieh-yhmw4h4mNvrGvcdJvS9tdpYTygFKlZ_TRolbMDR9Q57KXcpnF9brXXsMpe0HmUmt4445quzYQtRSRZoWXbJg0OLFq2vOfcAyF106hlv5ZRGspnnaAgZuadwtObxCt5JGK01hAPDJcwoLmLtkFTynMbFAeJAVtiZtAXKtwmnaqNGLnNqN6b9Juf-D_HsSWgKFy9c-y_V_EG8bGUT2A8U7Ha5h10mb3NGcdA5BC7YJkzorHLCBmupW_a--DSCfta2-vXLGcU37-57UJmP_MUDNpudSCNXRzhZVHsZUZce0d6rlKNdDQgiaZlxIrH-KFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=lZIN4n4ImoL5J2Kx9bMsieh-yhmw4h4mNvrGvcdJvS9tdpYTygFKlZ_TRolbMDR9Q57KXcpnF9brXXsMpe0HmUmt4445quzYQtRSRZoWXbJg0OLFq2vOfcAyF106hlv5ZRGspnnaAgZuadwtObxCt5JGK01hAPDJcwoLmLtkFTynMbFAeJAVtiZtAXKtwmnaqNGLnNqN6b9Juf-D_HsSWgKFy9c-y_V_EG8bGUT2A8U7Ha5h10mb3NGcdA5BC7YJkzorHLCBmupW_a--DSCfta2-vXLGcU37-57UJmP_MUDNpudSCNXRzhZVHsZUZce0d6rlKNdDQgiaZlxIrH-KFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
زلاتان‌درخصوص‌لئومسی:
من تو دو تا جام جهانی هیچ گلی نزدم ولی مسی تو دو بازی پنج گل زده! براش‌خوشحالم‌امیدوارم همینجوری‌ادامه بده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24131" target="_blank">📅 15:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKfTRWJJg5DCs6mITT3Ntdcai-Va53n6L7YJzdKe3WQvLtDzQUsjQw0ZhwKFAE0Fczj3oq0jRJYDJKVQq1Cu1dxoJIr0nkz_s0oXoeey2th3sSvHsiPew1FbltP68IBA-9tbd2t3AKyoFjmFRt9hWD-5OqUyO66mmCbCjLQpv-TZYCkIVtP--fSQgLMh3uZvdx1j6JJAlk1xJd6to5nsOXc7DEA9EJyq_1U1orDj6AUu4Xe582wbBm7iEpJd1uxafwmibK48SYC4wmk7GSXFGc3zK81qtHu1ZlMFc2seZZhySH72IqQQlJEE3Fuk2gQeXO6Xf7CWc0JxF3QHyLdfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
فرمانده روبرتو پیاتزا درتمرینات تیم‌ملی والیبال باقدرت هدف گیری 100000 از 10؛ عالیه ببیتید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24130" target="_blank">📅 14:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_UNC4P5iBhAWjrjbn8o8zt8AF1VCD-Sq_IV07mibhsoWbUlT_UvEJ3tBJ5109EqWIf2qvpHQnJOT5ztGURTzjYbRdTViTxSpOUKsFxTj5qG3nZFBzc8JKP1JWRxNlN_RGrK8RxGwjr2eSQJOBBf34O9XWMN9zTwuG2fKTIrFb6VIkqfDLyZNY5UVIzLP7ALnyVU42J6xFeJfeNPi-jCuGzD8VwJI6HLzCRdq6WCzTChat3sMKINX0Id_-M2O3czTeW-zkCdE4GDvcZaxT2Bq1KY2nQXCYJVROfYVDQsQfhDi-PT9JvOa-CA8N4OUnA9-uiM-YaI3vjHa07r_qnfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24129" target="_blank">📅 14:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyWIvp6OCl7OmmrxjsFDOEzvOGXHU792AE7qRGvtZ0QJzAU2n_jQ1kkXQ4FRD-E48ekKIA32a2E1b-74Rp8wQKwOfUWdCQ6rMxRtxQRNcSqqLouwfR7h2rl3w8yvepm1CCclKHUi2souH_Lhgi7kxMED6pqM__YUi9wCXXDkBCsCB2FB3RelDH39n811GKH3CrRZHQ84we5-2W2Jmmi1UOdhd_P8QtPdCKyCJSwMEhEDfP_D324zFgpv63Zbcb8FrTsfBytcIRCrbJR_v2sQwo4JRqBUSAHN-1ZHG60HGBwbFdATEZ94GH8iqCkHEjN86j8vNQqEBI6Il8Fm-xaU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24128" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=SkqINIV9FuuGyJ7oHb3b8VgAzpBH2Gg42uclFGFE61dgvfQjGqDvpkpGe3q-4dHRT3qhzbhyBeDeGt553BDz76y9cMxjKpui2q5Omh4E6ItYLWMjbiTlHKqni6f5lsALxFSuIZ167_lbUhaL0Zoua4mKot6bu7lrIj544xdLV1c27KnsbYZ81QuQKNqovJnnkplX4-aFhsTi-Yo4B-UY90kufL30sGQijS4RhmoVU86HljOykN8CVUGGAqt3sL3wCFl2BaRwP9i8pfN7MNLWoRYWLKyJawNsQgILC0bKMEfVzPFhVpPbWJyZpi8wZzE37PbWikTcprVlhmEuxoCPqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=SkqINIV9FuuGyJ7oHb3b8VgAzpBH2Gg42uclFGFE61dgvfQjGqDvpkpGe3q-4dHRT3qhzbhyBeDeGt553BDz76y9cMxjKpui2q5Omh4E6ItYLWMjbiTlHKqni6f5lsALxFSuIZ167_lbUhaL0Zoua4mKot6bu7lrIj544xdLV1c27KnsbYZ81QuQKNqovJnnkplX4-aFhsTi-Yo4B-UY90kufL30sGQijS4RhmoVU86HljOykN8CVUGGAqt3sL3wCFl2BaRwP9i8pfN7MNLWoRYWLKyJawNsQgILC0bKMEfVzPFhVpPbWJyZpi8wZzE37PbWikTcprVlhmEuxoCPqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جادوگر غنایی: هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24127" target="_blank">📅 13:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-CNWvxpe7Q8y_g7W6DBoSivj0t4x7D_6I32XgluBx4HMHu3e5Km1YNMZMb4LZdznj_h_9xFiqMZKgA-hg4LXP97Yc1oXkQfZfB7OQEDj1a4c8R8YhN9CFYw9Amt0UtvffoTED1jjlJowCB-Y-FZfgdrCR4kQa-OjTzDqeS761nwgvuWWIuBKKQ59ytVzlG_kHhoW0jyyyyWFBS_8mVakshcc08K2jq-kcSwqP9j6-oMh7WGkJvKEVhZpU9hLED0E7j7haf_O7sNM5BDcsjoL1dRcRv4fNoHPj9VadxKLafM69JS6-jhvAEkm12yTsMW9lg9n5XEuGy2Lev9IzFZ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سه ستاره جام جهانی 2026 تا اینجای کار؛ رقابت برگ ریزون لیونل مسی 38 ساله با دو فوق ستاره جوان فوتبال جهان این بار در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24126" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyL-ohdiVxnOWJQwY2PGxei1vnSxixHmio7LpF0z5MtvILZJoKqjMSc3ti6MkUKjDGzAFyPsXl6i32T2eptlwhHCKbA4tRSSinqHKnC43L-WlOfl793iTcDyamv7CVHRCQcHO291OYYodvO1OUQqjq1Yq4S17MIUxaU1BcCHabZuKT4sihjlrHwIbg0WO3_5gr1xQBpQp5poUNJcM1EwAsDeCHOXNHXW2P26eLN7dK6B0zw8512keqbh8wcc1cLP95M3x5KdocIqZMaqxuYys4EdgvpgtdJnNV6tEhPZl_pCsFOxmoC7b0yTtKzwa7nWtkaBg9JctMjMRKnokQIatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از خبرنگاران در نشست خبری قبل از بازی انگلیس-غنا از کارلوس کی روش راجب باخت سنگین با ایران به انگلیس درجام جهانی 2026 پرسیده گفته اصلا یادم نمیاد. مطمئنید که من سرمربی اون تیم بودم؟ من یادم نمیاد به انگلیس باخته باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24125" target="_blank">📅 12:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAkxtwbJ8s6DUKig_f3sa1l47YMEoLaMxwF8gpPVopEscaq-jlWlrxDKChDxVS4XeSqeqst-GNCuilu2hNSAlzeXlCehJCYDeVbebxFZ3wpkC2jfPRUQuGo-fHo4LwGqc_iqqwvdKMIRpQS6Whg0cY1gA0dWDWP7PgfCB1qBJwM3JmjDAIeQKJFxRfAn4AqkiZWXmpgwt_yxAPl3-j4pLW79QVl1r2gc1DBY1vuDauegLl4zrM25AnLNOC2LAU8WJZ_z63_6E5tB0bxlCw0QTc2YkIn6NvOMI6kXh5fYolQFpD9ceT7_N0__0E1tBI0cXYt0qmSiiLprT8g5clu7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24124" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6mIYG3rfG8_Isfi8XXJSVUgBHctdP4XkqqY17_moElxukY_S719EIj6btyhJSa3JzQxoRd50xh6A3Spr8KRCBjDvzVVq2fSVOFLiy4d1xcjvn1DNxZQtR7y3Fc27kT3O4hQocwgEjdMfZ_3QzCcrFilXFI0luWQ3P_p8hn9EfMdDe3bQa0Z52ZxBzTWDDEOt7BXCL7S2IwmH2ZGIEpa2LKcjvznjV-NxvegUF0zHMMToL-rqC7crNOpB7SS4b0iDRd2oxyTZYTGbH-TVCpUfGmN0k3gB_bseVomvvH__vlQc1i1el6NVLiuh4hG0ETAtISTBg7KtsNknET-_e9Vdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24123" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIg_F57X4d9EqkR9zI4zYl6K7UBYcxqkS_VcZN9J0iWKRgq7yYh_xlR855BXQBInSxacu6FsKuxRgd0mlSm9f8MC-2_EyEWAe2F1TQtvFAkmQTxRqLU11WvMvvfSQf9aXmv1NtuHNQHTXP8IEis685qW0pLBUq3qiN8UwJ0R3dgsk7N5F9vlytYOd8dcw9_kzpKPzWAXz2XfoJTU5bsSainnkigMkh8xNNnxgSebNdg62xEdzUht0hVWHKb6dHtw1YIbNjadf3Uo_1NgSDPPrTbSADK_-b1H83U8wuJ6SpZeiR8jw5zvwod_qItwsntZyJ7roNLRanF_a2eiK3D0wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سه گلزن برتر رقابت‌های جام جهانی 2026؛ ارلینگ‌هالند هم بانروژی‌ها داره غوغا میکنه. دو بازی چهار گل‌زده. اگه هالند درتیم بهتری حضور داشت که اسکوادش بهترمیبود و هردوره درجام‌جهانی حضور میداشت قطعا الان هالند رکورد کلوزه رو زده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24122" target="_blank">📅 11:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2Bl-4R2zeNq4qL5lgI0HslX7ujk8p0Xbij7TM1XAE-5nwp1ogZoI_C1S6hLher-3XzHcNx7sW76lXbaYyFMaLow-p-oKg9G4_9ujHxXSWQDf-qKy0Ibi7ksBz-nUxwzzEt8llmyhd2SAmGjzqYk-PQrsgk2aTSIyod9T6fHMWc44Zz69ewSKrR-ug6Oknq3z-5mB8_VrKZZIzKdcmnClzUmQwps55fQ0QEOdj-En7SsuuRKxW9cEbjQd5k4KzK7dH0qqW0vAwCCBQm_XTGzqS7nEVcOeLbNcpT0cb2_2CwZMI3wXumpNkvJ4ITQqhsdF1i7zVRAPALtSudZV4vm9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24121" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=CvBaQC4L4S-IHfNsyCP9pdH8f0vvfIBwzxLtqcW1GX98DUK0faiyw_cuYto17_YZSfIIrlHGnV7adEgZXhfa8ybbDgkmlZrzKCBtNYU0SiukSaIHZz-9b0ITObf5Bb8EddE4hYt-5zMOFiJVcHvT2QWT1O5Jp2LM6Xg8s8eL5ZP4-q_lE5dMQdx_zcubAYg-nTXvxNIxycKNGv9DO_fA8gBM5xWau7vPetFXC477lLUg87nemaD821cMfP5pCwXAWM7GEv0aUdR68604h_dL-T2edS25oZeE7rkDrgFR6ALzouo1sgdVUYzyqzUAIxLK-Wbx7aeYO_S9Tg2oEy3lPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=CvBaQC4L4S-IHfNsyCP9pdH8f0vvfIBwzxLtqcW1GX98DUK0faiyw_cuYto17_YZSfIIrlHGnV7adEgZXhfa8ybbDgkmlZrzKCBtNYU0SiukSaIHZz-9b0ITObf5Bb8EddE4hYt-5zMOFiJVcHvT2QWT1O5Jp2LM6Xg8s8eL5ZP4-q_lE5dMQdx_zcubAYg-nTXvxNIxycKNGv9DO_fA8gBM5xWau7vPetFXC477lLUg87nemaD821cMfP5pCwXAWM7GEv0aUdR68604h_dL-T2edS25oZeE7rkDrgFR6ALzouo1sgdVUYzyqzUAIxLK-Wbx7aeYO_S9Tg2oEy3lPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌اونور آب واقعا عجیبن، از دخترای کشور خودمون بدترن؛بدجور روبازیکنای ایران کراش زدند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24120" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFvKj-zls8P5SYFoL7fk6FV4lU46Te1M8k049Wz5T7gduEUGifmTYrcwQokTQ2wc5MbZmdgXPKImg5Js5RseaShcLCXDqJnSb5dpaOLDyfU4yApF4u9aI2zEoGIlyzXvhtanJKhpi8n0Uiv6iYG-zidbUZdWWakiw4oPc0TTZijUCeZggNd2ZjHy2VbFF-XjLSelrpjflJamqiPqbXIXkbnUOX7oviKSgOM2aZ5hijnViPC2f_h8qPBRScLlPxrtOwMGdtpIeg2XYPTUnfJlOzuRkRK2tRruUom24AYb1KblpruJLYXchn59A3A_kxMm6-9DOyBhe7RjTdG-7Li5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eR2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24119" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZI-jJZXcb53LPbFS5YPRhfn27tCC0m8cD_rOGiCAr_TEzEFLznOAQR3VPEvQcwI2u4cIiRvfWRZ83l8HN3qOKJQnFAu5_dp-dADAAeniPl02TamDncSXQKVWq6dlanQteAUvFiM9Oj35OJ2iryOoaxPID7vM_uH9WDNoL30m-NcmrXg1I9p4JHQLAI2DU6ifUb1V52asAjOG0w1TDYcOix1HSJ_rMs_wEFP7AoK5TWW50csJ7Vduy02eWV2M2qPq4ot0fRTBKl7XCdazzdn-2pbAKzEFXO2UkKvQR6SUNQaA6At9U3J_EwDGatULi-I3wiUz0vD8zIBsoMCt1wawqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛پرسپولیس 5 تیر بمصاف چادرملو میره و برنده اون بازی روز 9 تیر با گل‌گهر مسابقه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24118" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_tIUqFmzcLBy3QeT4Mj6Pu3239La9NZKj7X1Dr4yaxwfk4MZGIU5AfuYH1jvUHu1k2bmwpxd4MGUNZJYA_jTHBOUze_gkUV_0z90RTIhROpqn2h14yC2wTufna9vT4DCZrECQKBG6t3X2hIqWyb9D0GsD9CrLhEZ2ObXbzwBB7kG569SLuX-_zqhM1PD5sp5P-iuNb2v0qa1HmIsImDn9Xdl9GChnWfEgaEbqUhHPXZ3_WwF6YsTsJsSsnGQQsbpJ4cGNbyWgcPdqSHmJPTXsWxiCL43a22hiuc5Wtclp0-D3ULbXjuMdBF8jolCbgnCRKTHTVonvXNnm8LLlHzGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24117" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbn4KrNPGIhW5Bx4Ts2I9rp6bFH9BAc94vzAbURxHB7i4Mx8OE3YskqSkgSmt0Ii8-IUveH1Iq3F_8sfs9eOOTuseNuqKBckTYRiAYA1YDu-fBqNhzTWkpqmlDrzChdhubkju_Q8EpAuKfh4BRNIbTv2mA4QYpbmN-HwVtvnRYTawzA_TAA63rVmAeXmZn4of18l_74riUmgUyPOE8YVxBqPLsEsl2PVgnuMDdMc7u_XK3O6oljR1L5VFYoSM6C5Yqs5oYyahvpi1K07_lHYexwvQ1pWtFKRgdGaJO-Jd8CNZ_HQYLklIb_HQ503tH8wIRyrwN7MrI3OwhUqmSH6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24116" target="_blank">📅 10:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=KsU_TcWRQdk5pamTFT23MLedlcFQTwSCB3ThSfqK4t9g0cohUXuIVClCiEuJbx1OXC99aGDH0aVF63QeLzdS8ltFWfCeYkKuJ1uYJw_PDDTFuM4ZFqNAVuXEIYoFrZ3iWwhUe9v7mGgio7N1RyLWPDQUuEYl4mswFr288NgBu2Me_qXRUo6FYEpUgzt6V8TC9P5BfomdxasWL_66xuLYHMGZw4_2D18RaxQS_p5gC0d9FjESsw68ziKppnAFpjvqt5EPTM-lv6uBQ5N796iTfrGQ_niHCWDHQuPF-K0YPiJhdH5gb3tLWVfOc5A8OyXH_gOlx1Oy4V03tXhVlF9AXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=KsU_TcWRQdk5pamTFT23MLedlcFQTwSCB3ThSfqK4t9g0cohUXuIVClCiEuJbx1OXC99aGDH0aVF63QeLzdS8ltFWfCeYkKuJ1uYJw_PDDTFuM4ZFqNAVuXEIYoFrZ3iWwhUe9v7mGgio7N1RyLWPDQUuEYl4mswFr288NgBu2Me_qXRUo6FYEpUgzt6V8TC9P5BfomdxasWL_66xuLYHMGZw4_2D18RaxQS_p5gC0d9FjESsw68ziKppnAFpjvqt5EPTM-lv6uBQ5N796iTfrGQ_niHCWDHQuPF-K0YPiJhdH5gb3tLWVfOc5A8OyXH_gOlx1Oy4V03tXhVlF9AXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24115" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=oEDuFwByvhyPnSdRBjspDZnLybK_30p0Wrr1iC6p6wVRbvVlZlN7PrfsBUlu30aZL7JObI-94DuWtjWOb5c7i7ojjjP1O0NNg0pJs3eD0smMU-w9ThRFicmAqlZzuipClssdEUmZ6B4hwSGllgc32TnBGNfLcgTxUSl_A8CuKwv2lceSwGLacEhj6WWND8JXDpwxG-eDANVBXM16vDx6zIvAQLNKDAz738sF2wn_XzXL0PTz9U6WcrBjW_vAwxXx8kfqlbt3jxneDih08hedS2UuTlRlmORx1cgllXoXSSdahwjRQ5aU4d6U0clGmtF815jOCAfitgRyqPDcM2iYuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=oEDuFwByvhyPnSdRBjspDZnLybK_30p0Wrr1iC6p6wVRbvVlZlN7PrfsBUlu30aZL7JObI-94DuWtjWOb5c7i7ojjjP1O0NNg0pJs3eD0smMU-w9ThRFicmAqlZzuipClssdEUmZ6B4hwSGllgc32TnBGNfLcgTxUSl_A8CuKwv2lceSwGLacEhj6WWND8JXDpwxG-eDANVBXM16vDx6zIvAQLNKDAz738sF2wn_XzXL0PTz9U6WcrBjW_vAwxXx8kfqlbt3jxneDih08hedS2UuTlRlmORx1cgllXoXSSdahwjRQ5aU4d6U0clGmtF815jOCAfitgRyqPDcM2iYuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
عادل دیشب باز هم اللهیار صیادمنش مهاجم ایرانی لخ پوزنان لهستان رو به ویژه برنامه اش برای جام جهانی دعودت باز کرد هم به لهجه‌ای گیر داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24113" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfLvnNUIFH7bcTPPHetBT3xLrBWppO8ngC50ObYHU5NdnZ6g335AdTPNAKxCQUZN33fq-Pnm9lf9G0mG4uL84yzWwmJS0idTq-WoTpQe_A45ZGA_2wKlaK2Fq13TLUXkdbjYQaZP0OoP9uyoadVQ_ObGnlTjKQEyV7660wUrEyFNWKhX_5Ej-a7bk5CrKppKKEt1smbDHWVemj53niJkisi2Yf_9I_VKr7ThnCPOIx2fUYWRtboIZ1TPJ4UWbiQ-lgPHDj7F5bcUrNyNcTAJ_Kd5y7n-TNXU4rKudPv8rmfLw5ojrbNORHCoU4Y4MHGvuoCp-tGySFQ_z-V-bE0HyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24112" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2atGpAvrrhomOoctZfJJButodfBCG-LJZaHfx9Dm7_cqY8RCTJh_Fo9HDiQJg4M45PjMYmbhIgSMT6eJSD_1L0tM_2RGAnjRr1u8bKuqBexuplI16cbiwAFJbT5ijAsTxMb14VTAXMfuoh3WLlbPncCaqiPka4jA7Q5EsOafHCWzEueeTrz_UocSYxfK-Vz7scx29i8arG71j3i-i9cnbmkBERGzB_eKSXcXHmeJ3mQvqj3Z_l5nkY_6U1KFP4s5BdqNKWFbY7coVzvDe90DviLRGTuVPtnwmJleBzK9qEj_fpqT3NireqB8GgDGCaSbz2WiKWkZXjhlixX142BMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24111" target="_blank">📅 09:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH_0N36gxODM2WYyE54cF8z42hNbC-GvAaS2GEtwDVtJn0J9K-KiR4jXXoLS2XMmd74AYdWF2GJ_liWfoGg2033MGyh-4lk55P7pfNj5tZMiAEOt47lrsNN3u9TLI2M4iW4wJbrcd-0ivbpb0c8vmGUFD52c3iBtgedFDplZjavLAh7MufDWLAzMWGr11OPDgvIzdccQMOfpxyRVbIt4gor-5jfo907zQiVxB98yM-PtBSli7TqlDajaNwCINSps4wNyp44wtCfJqw84727FUIUFX7EQw4Yx64AHaxKzGXU47IoLJBOW074AqCJiqS_oanD1jpw0W2nzn4mZEai4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌برترین‌گلزنان‌تاریح‌رقابت‌های جام جهانی بعد از هتریک لیونل مسی و دبل کیلیان امباپه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24110" target="_blank">📅 06:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24109" target="_blank">📅 06:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkMGWvr-GqI6nItzLzxwtE9cF0SoWvKo8XCUtr08-yfHdOmKi8ZW0uJU9WfXgnxMVNDhZ-4QWxhrUC45zYTBNmfL5gbG9ANT6XSqjjzu0KLXlWm1Wgc1iIYsNuQb7UJZ3PVvgIjMvwCbWWBOiZXGsmdZPZvuECTyApsx_kf1fQXPeSU6j79Wn1JMmbLHCl_3GTzdQ0CMfBtGBGhbuyvOUPcVZgPYRbpzYYugNGNGv8YfTBMOQ_zVEBLBJgQ6FtmERuPhEjBRuAGX9yru0-FnfWOogMENDsHrbGegrhpwl-AKYIoBY_feRWVpEFSAoBW9clttYBdMFV3Y5TNjlKG5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24108" target="_blank">📅 04:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دو تیم عراق
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24107" target="_blank">📅 04:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwFnUB7j00PR4I2yD-aOZNXjQ1s_Ze9WXIWbr3LuyHTRdKmezak9d8UQ-7yza2rTc1PEw5qEKVOWIqexiT4JOiSQ3KBbt_6GeY8VmFJh2b_AbrgPS7sCwJMjUHh8SdUjflrv5Y9GPnJArwO_0dKxvsZSc6ouZOQHFlglZz1Mb-ywNTBMaIIBq1c0o2Lc0bKlX4hjcjHuUZMegjHS4wvY8fx1lIaonh3TwuZe0zuh6oZl09necy5FWOGMWxjOpw4dR6p-krieibz0hHLF2DvuOjl6KOwPQB1615JuoyjxYdBBIvBxV377OSg4JWE3BG_EjUTGyEqK-r8QhXUkjsMuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رومانو: شماره 9 فصل آینده تیم بارسا به احتمال99درصد خولیان آلوارز خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24105" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sc6Z0hAHX-aG50-JMZgEBANVZn5hU-y6JBIcUHgqSKn6NHCw6qkR-qEcSwKT-sIBTavRT3qWzBv9RLBOgcxV8ydi0LxKaZJU2IDeVDY_POxOZyoN0RgKVKf-iEkRrxYbo9B8sdZKwgZTzBPfvaE4GDvsalFstROhu8fX0VXk8o8c8OWDGdxf9yGCN8P1pVQhR847cM_xyVozAPkD1_HiSsJ_MrVjrXd-3JTwYezthXlOgS4mZ_4fAroMQ5QQzkBJR_iSf7374m3YxJ9NCf2VQbX79s_E1b_Qx4JGf57mOolboFJ3Vwb_ofiLucmQY-J8ONr0EAsZEmj0IaaGYbwmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیشنهاد تراکتور به مهدی هاشم‌نژاد: 3 فصل 250
🔴
پیشنهاد پرسپولیس به هاشم‌نژاد: 3 فصل 180
‼️
ستاره ملی پوش فصل گذشته تیم تراکتور بزودی تصمیم نهایی خود را برای فصل آینده خواهد گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24104" target="_blank">📅 02:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24103">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsRHbO3G25-OCzI3L9J_3ESulU8-5uCNe4mmJpCL-TW5OPE-JbLkHCAzBkPbMQLemj7QErXQ4IbS5W3JQxJA4DbhCY4OsjJHitHonBLQV4ldNqlwsN2wGB-IEAkg48XzlVOc5b8_iuvcPZmFfKKnTgesIuNq4PTHo0RAOzyhQW--Vxih5-g9gPzRbP_GXeJra_jcS8nLTt_tptKUuxLlLXL_1QmGvZqguwuO0Ay-MhFh3bEZU5oZdtNDTIBm-GiE-E_inExv6MT9WrtHK3BlovS7kJdbHscii94eURaazchXuTxmBeWlpI7Tvm96K4UHazvx2RWSUtKrfdaYMY_WxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی
؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24103" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=US2IB5tKTtkMv78ZH3FZPBjEPtCGlpDEobL9s3CnvX1lad4TvcCOE0Q8kWyT89LO7WT8gs5vAU-4TiIks-NXp_h_w6j_0gvreglpXa4l7caSjVD87cJuimVmWMeurzj5Du33TwI4Fi9DadThkm0KyhzFDofjVyxdQq1YDA5mB6yLcdUSFwY8yYtmE7vC_aF8WGujd4qlUp5Fg_0oswXE9cR1KLRO4Pu-_DFDeXg5lCHCwFHj1_UbDpbR-GGvI_sUwNU2K6cGkZ8yGm94tq2bcu9OkLa6eixC-QEupj5ppCJwoauw8KKqLJxRml-lN4b6bjmiMat1Es04Kxw5brLItw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=US2IB5tKTtkMv78ZH3FZPBjEPtCGlpDEobL9s3CnvX1lad4TvcCOE0Q8kWyT89LO7WT8gs5vAU-4TiIks-NXp_h_w6j_0gvreglpXa4l7caSjVD87cJuimVmWMeurzj5Du33TwI4Fi9DadThkm0KyhzFDofjVyxdQq1YDA5mB6yLcdUSFwY8yYtmE7vC_aF8WGujd4qlUp5Fg_0oswXE9cR1KLRO4Pu-_DFDeXg5lCHCwFHj1_UbDpbR-GGvI_sUwNU2K6cGkZ8yGm94tq2bcu9OkLa6eixC-QEupj5ppCJwoauw8KKqLJxRml-lN4b6bjmiMat1Es04Kxw5brLItw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمله سنگین زلاتان ایبراهیموویچ در ویژه برنامه جام‌جهانی: من فالوور ندارم، اونا پیروان من هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24102" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24099">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czHnjGNF6fR0lbt0l59_8FdYE7f8OPp-u73cJO8l5-8Jq3R4kKC3Zuib6KGqFhkOBSkfUBx5ZGmznaSfBKc0e7LpcuYUNt-HuGYMIWT9HzniYYBsb7-b-jupTgq17NVZsjZ945RCCgIjngl0wQAZwJJ0OiHrFWuV-D6RjNYqbVC2QjJ1BcxhsjigJYw14rOex6Xp1Zc5FLLHOnzAHVjQwXoF352n7Xn5pNRoreaAPfxqQ2-iJ4ALLQERTaQrUqKjLrHBJ5yP5bD85VNS7rBD6B-AHRTrlXDdFoLrWYEEDazHaRw6ZNxVLGmNhzHZuehUo9XlzWi-zW57rlWLXkGEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد: میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24099" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8ingsfV_CuKNKCASIK4L6NAqvx5Ui0acIfbuGh0oASUlqWgzquu4s-nOFdZqrz3zOxnztfMQSVxwTb1FBKaFF2kMQpsN6hxGju2z_lDKBeNCtUA7-8gwniOCNV-Pk-ZjzG4rtc5an94kYfX2kq-P2BWS95s_dm-cga_TGTtJe5WBQW7B5MJnOTTT7-AO2M0dNQ91jkM7EBSGKifZOZ3MnNDk_9iSyk4Y15txzEV-bQ8U_4cdeI2icvTx-LuXuhBdkRVv3XKlCnR843rMAK9SgsV_czd7-nL7HD_UoNdevxni1qtpLNb65_uXgYHbvT9qscH_tG3V0ERl5S-g6DOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اگه فردا دراگان اسکوچیچ قرارداد خود را با باشگاه پرسپولیس امضا کند بلافاصله یکی ازستاره‌های خط‌حمله تراکتور رو جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24097" target="_blank">📅 01:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=oYkYNPPWHWHwY5OSRqZN8gtBIgw-G-E0dpdt53L5rw7Vx-0ZVFL_lbCTYLM1stodGs0vCflyfPqZBzbSJa2Rv5pfyMvR4UpdGg_cdJWXG3p6U4ekQGuQXx9Fdy9g_Yt1qEmZJatvqjjh2E3pfC3wf1gRYMVlaoqeIiOy_R5Hh20c5uvme_dZ9mQ9QKo0FKoLTEantybIgjbrif6AVMI9o2a7jSjRnWYpEpqOK-f8C8uUHqEJ8u_HLV1AaTT2xep90LDwur4rNMHVDSIULDhnlEcsDiY-XfDASxWuKUSRc8sdhZ27yqijbfHvWJcWq3PAIuU7vrhZRe299rco-Kua2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=oYkYNPPWHWHwY5OSRqZN8gtBIgw-G-E0dpdt53L5rw7Vx-0ZVFL_lbCTYLM1stodGs0vCflyfPqZBzbSJa2Rv5pfyMvR4UpdGg_cdJWXG3p6U4ekQGuQXx9Fdy9g_Yt1qEmZJatvqjjh2E3pfC3wf1gRYMVlaoqeIiOy_R5Hh20c5uvme_dZ9mQ9QKo0FKoLTEantybIgjbrif6AVMI9o2a7jSjRnWYpEpqOK-f8C8uUHqEJ8u_HLV1AaTT2xep90LDwur4rNMHVDSIULDhnlEcsDiY-XfDASxWuKUSRc8sdhZ27yqijbfHvWJcWq3PAIuU7vrhZRe299rco-Kua2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#فوری
؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد:
میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه و آلوارزبسیار سرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24095" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24094">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=RIDudqzstwGCmaKkjNOUFkQcqgjPxBTwb0pQAlvja2PAXcI1mFvY3XaEJLfkHyIwA-jFTaZJTYfd0EuvWyfZZhUHs-gw_hVNEsoOZPR17N2ZKPG1TtBGndDUi0a2Ym3VF0Gct7tQw6DnlAv3uiaDWQc-m0E5qkPR_SD-rTFbP2hgiIXGs5lmeyfmIvi_VUjqjIrMCqmhb3cWB7MS-TVUsjSuYYXDO81IaZiIunu6IK2jvxMVR2dY-2ObvfO-N278Zau0_X5038zv4OwXoNBWgtLzzCwJ81lkinfYxlhAc3P5KEY1q_nq1eUaes_d9tGtNE3hnCt4aBXC0mIk9PdvNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=RIDudqzstwGCmaKkjNOUFkQcqgjPxBTwb0pQAlvja2PAXcI1mFvY3XaEJLfkHyIwA-jFTaZJTYfd0EuvWyfZZhUHs-gw_hVNEsoOZPR17N2ZKPG1TtBGndDUi0a2Ym3VF0Gct7tQw6DnlAv3uiaDWQc-m0E5qkPR_SD-rTFbP2hgiIXGs5lmeyfmIvi_VUjqjIrMCqmhb3cWB7MS-TVUsjSuYYXDO81IaZiIunu6IK2jvxMVR2dY-2ObvfO-N278Zau0_X5038zv4OwXoNBWgtLzzCwJ81lkinfYxlhAc3P5KEY1q_nq1eUaes_d9tGtNE3hnCt4aBXC0mIk9PdvNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
صحبت‌های لیونل‌مسی کاپیتان تیم ملی آرژانتین در پایان مسابقه امشب مقابل اتریش در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24094" target="_blank">📅 01:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24093">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKcZQ0UVaL6tGOZ5iAcvh7GDXy2oI8h6x6NclD7BKP-QUpola0Y8nvHJ1OWvKNRZdnZme-IdnmoZrINkEPX_0nk3vkoGfWexkkiOWaNAfQQXjXzCrWG_k_7dx8I7HxjG51L512uendHavJz6zBaCCWEn-Ldo74quc3ea8a13QGOChSWWmYFyzJ28c7W-3GjG7aOqoX0izgFg61oyuZgi5UahYV4H3yl917I1CHya3ybTDxjaZrT7d3AbKY4MULMA8HD6_iDPRl9SLSqd8dfOln3SJGxu5E139Y80CKsvK0joLCh-IHxh6RrQaZVKTeWIxjpPnJmuebU-KywGU_mrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف یاران رونالدو مقابل ازبک‌ها تا جدال مجدد کی‌روش و انگلیس در مسابقات پایانی هفته دوم جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24093" target="_blank">📅 00:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zigf4nicRy4J6XriN44uzHCyDdit03YleO2-EO0AA-nU7sgiB8jy2_WjwLbNEzzS40oPcmMVl9ggNAW_jImUo_Hs5gvHq1SWtuitX_HXg7ciYm6_tdd6s51DMewUEbErpoViUMb531uGXL0DYaANniMscWv0REydNL3zznd4dgoJ37jwHpQpOgnrdLr4TmG1e7cqi2gOyG7EtViibvAi_fbkWrNno6h9nG4UXAPFIesLCHl8h3VKzCwmlyxFP_QrFpd5oj-s-0Kl-qx4sersVSn-zWeeAWp06U-S64lS0twY9AvmxoeLMZXSYphl_kmlRZpLX3AdjsNwTT1DuwNskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از درخشش ادامه‌دار مسی این‌بار برابر اتریش تابرتری‌مصری‌ها با اثرگذاری صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24092" target="_blank">📅 00:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXIgYLGAsSlEIPcMgoYWaHsNmM-XjKsCgFln-joyXNYeQmiN9yp5KI2F5LEue9ARDyMi6PMdrTT7dZX5vTh3H913TmZATHmggYsiaknElNzwrUAVcU4DQ5e4MhDJMbde2s8NGkpJFpYs3z2aSS4NOE1N_Jkq1fZqimHLKO1M1qIRliOG4grFrSn-nSpKSfmjlOeMi-s0qEgCRGYngnoHjVsJy1TTxzHIX4FwoN1WaVS1c0mePyZV3cwje39TS3GXjPSI13LC92XRdjiJwDzurZQhqVZ1WdD_Wljf02ww_3KQUmeWNgE7k42aCZiSObda2qhz81YITlqWCXE7MLy-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بادرخواست بختیاری‌زاده سرمربی استقلال؛
عارف آقاسی مدافع28 ساله‌آبی‌ها در تیم موندنی شد و حتی به‌مدیریت باشگاه اعلام کرده در پایان پنجره قرارداد او رو به مدت سه فصل دیگر تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24090" target="_blank">📅 00:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjobh0O1Z65grlWLnkTRljp8PfYbB74PasET52QP5FvwufvWXwC4VWUrszaK4BBEj8R6RAM5y7NDlpCGiqA5gSis7E_St0DUV9xeyXKlUOpr-imn8JQm9OYYbP28kSWG7SCkypJKJyhhyPxqtqhND6dPPaSKuGGqT6Rlfqu2CleWhbp7DjKJQk3MgB3rZBzj8mn2ZO0YFHUoMaUT5bcMlhqbi8YcoDKeZV8BMjkG8wPaQNpQyzdwkQ6qQgHyKmxSnDoBcezMoQQVdjQlDfPtBVATPffHUAOnBx5D7NGhAtWXiBMOanOS1QIe0gnYTF3k8caHgTveMl6L3RhZKUU06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تافرداشب مدیریت باشگاه پرسپولیس تکلیف سرمربی‌ فصل‌پیش‌رو خود رامشخص میکنه یا با اون دوشروط دراگان اسکوچیچ سرمربی‌سابق‌تیم تراکتور کنار میاد و او رو میاره یا با اوسمار ویرا ادامه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24089" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24087">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxelhZMkoPIWgMmO5JV-k0gi-K7aTY66XiqbMTosDBnGu8x-U-6EgxehdYeu90NKBkaOvHGFDb4roKoUGjhDZci5A2qUSTSZdJZ945QPs5vOxKG0LdzyY5C7FKO-Yb29rcnsHgmV8bfxJeW3VKGgpOnyg88UpzRxaXAM0GCVHKKY84AZyryaJlxlwex-XPlj_SmtsS2kikiNgs69vs9u7WC6J5hnt7ZQA_pYZL1mLhZR4Mu5arOGTy8UrgAViQVaoQjd6mMatDqVEHPMnFYzvq-lRO1hqe2jEwNLm9mgQFzN8TjBsZ99YrZYNy0lsm_TvEycVpbd203GZ_YF3CsMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CT4QKYHjrhE0aX0PsCNwig_wF0DZOuk_lGU2LFG0CaQppizEkc1i4vJFw1Vo5bytX3_sTtiMEehoQK55-Mw-092_2uxCZ2DdOBPWa2L3uwJRKy8cXJzCnPAOEgOx8vohIhIcxHRbbzIA6gWAjzlnDileorE3BAslOjlzVx4aJJIc9BzPoIjBi64xikJVFKIYBqVeCGBfmzcgfkAkmWquAhFzY0CePIwc1cOGZS_48yDT2rup-vPajmCdFKAzS-HNeX0Kb_bXLpQeLk_dD36_6Ll1aaBRCaQBpFM8XRtEXsZff7m0Cmc7h16VA6_WV865O8sj5xGhhXMKxABkqdSL9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
چهار تیم ملی که تا به امشب به مرحله بعد جام جهانی 2026 صعود‌کرده‌اند؛ آرژانتین امشب به لطف لئو مسی دومین پیروزی اش رو بدست اورد با شش امتیاز مقتدرانه به مرحله بعدی‌رقابتها صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24087" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24085">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7535185668.mp4?token=kb26pFrL5l1BQIPH108siDRnWYokJwcmcV52niIYY04RTBClig0cM4ho6WfQNSmhk-uHdvnh4vsfKDD30LQGUkgePdXLldVbq9id0MFmFEGvRZIGRXDSX7obapqnoTMh2_3NKyqg9Hz2Asb09GDp-FOVoLZ6guFVzEYnfcD_vbyx89OwtEVfAD3Wyjxf9l8RJMaqKNuMyVFQNuWNd5KwOAqZSpDsosHJSJ_h86TJHFFg301Oe36aqbq19XZtOUfqZhLFj83AMASZAQjB3JtlUJKDJocGcaVTBIidoLtTvhhyABpFp6_zWZu4qydjdp0ECfvUeZCGCIOIe5CRe7mV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7535185668.mp4?token=kb26pFrL5l1BQIPH108siDRnWYokJwcmcV52niIYY04RTBClig0cM4ho6WfQNSmhk-uHdvnh4vsfKDD30LQGUkgePdXLldVbq9id0MFmFEGvRZIGRXDSX7obapqnoTMh2_3NKyqg9Hz2Asb09GDp-FOVoLZ6guFVzEYnfcD_vbyx89OwtEVfAD3Wyjxf9l8RJMaqKNuMyVFQNuWNd5KwOAqZSpDsosHJSJ_h86TJHFFg301Oe36aqbq19XZtOUfqZhLFj83AMASZAQjB3JtlUJKDJocGcaVTBIidoLtTvhhyABpFp6_zWZu4qydjdp0ECfvUeZCGCIOIe5CRe7mV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24085" target="_blank">📅 23:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24084">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh6M5YCqaU0CMAoeoo93-l3iQUqDho1hDpXijR9G5JwKSFZW31ijETvtqGv_TC7T1arEClxC-HA1SacKyRNostqbOHvv86t1AJqzxh_kXmq0ofO2DqtSovDC172YyxIi1_SEPC1ubuQJqDrxSoMa9dW8D0sgvjnJexnCuiy0hv2vuJwmr7iPYeY0sSPddy3QXcWfrZB4c6CQVZxz7lBR9GuTT52ZT4A9POyMk1M6GwDWcCmeiK-feuc9ohlzu5eR8gfoH7lceGhX_Xmkt_37AT8gNaanBE2izXtpl86QoZGUDlVD3j48cpRgflZU1mN0G-msC4UEKAiGM4nDiNN51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24084" target="_blank">📅 23:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24083">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcqVtL6wtXzrjZZAeBAaFynhJR2PbF0XWvqNA3AyXUt0ewtOQbulmsus2iJTq2p-O4rqGk-W3UiC2nPKoopyqFGZipjUvISmEmFf4LjVo2fDQwlHL1qr5ElA_dXn7GpiSTZEoUCIJVaMmKhsyMR7v-DmMmG_QNKzvT7mmrB-Vtrlg-fCx4Jldusq3Se2qksn_SEFqDYhNDXr2NBisEBr_41vTlgwzpi406bHz34lzrvd9eXxbyTS6ZfFRNs7-wTm6NQpCmFUKODE16IOPYe609Rnov7b9Q6Cu7mfpdulq9TLD0UTLSZWM_ePejNP349T_JfmgGKIP4xNZXfaU4L-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24083" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24082">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxw02Fi-H47F-9WNHuCtgdc5WFZPon8n9jWYetErHW-3y0xqYT-mnHAvxRO581OjZQEjuQc0FlFJV9mJcKwP4auYv-IO-fzf3oyJX-Y0reFDw5zVeH5J6pe7xZLQqAy3E4k6S4nSQnzc9shJL_YVjPAS_fi18hz8T1qIZ7BO8o7LQTRF37geJ1ptgs4Vnw3F1tN6kzp0Yd2ifjGcF2oQKfeVUb-EGPMJHvbwnlY87koWRrp9nnUhf3bZiCBfw_1yvwAtCh1lxnbycLjG6HEJYlrGiavsZyzBVU2qsEl91e3scuvknxu9TeKrZMy2ZxLV6Kml3BnJ9JSP86crZHfvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24082" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24080">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK-qN0u9VbPnj5DH3YtwtHKb4qeHTt3yCRzC2q2QR5K8sei73opavBbD1kktqdolsodCO6JuZZmpWA2jtDcEbA3F-YFfhoZ53wWazffehGMbqnlUJi8vdQAeTihqoaO7lVOoAdLnvlT6EPB1BdRKMGJikRB6grCde6x3UiICCIr1kTzRXBY27OieDcARX5YRAihXopq8DeQfnPpcZsXZjK6g1BZHFuD_RnyRdtBtPB-f2JS2c7dvF6oXwgv5on7xyEotwyGEgZUZzvbCcSyMLr4K66G38Ghi-0gKDau8AkghF7teLAZtkwugNUfGKWE2jIXWStVkvZwhN3eI8JnCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
شروع طوفانی لئو مسی در جام جهانی 2026؛ دو بازی، پنج گل در سن 38 سالگی؛ این 18 امین گل لیونل مسی در تاریخ جام جهانی بود. آرژانتین تو این دوره جام جهانی 5 گل زده که زننده هر پنج گل این تیم توسط لیونل مسی اسطوره‌ای بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24080" target="_blank">📅 22:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a48741736.mp4?token=mJjXNIqKkafjF1Tz7Sbi7Wb6HipTd2m0Q2d2IsvUVOCblRdBkpmJM1Pr9S-UqYkS1w5UpMJkfDBB0PDFi2BIU-uxIZCJEXuw0-Y76Nxf2ZKKTxg6P1zkDDacMlMTC5BrlbOVijhF0pvUPTzOl_rkBoP_mJPyMWcqtI4PHLERCYR4bv3u8dUP6zXYGr4MrlpBr81APdZaLXvFfLWZ4YL-ztLXv16Rpc5JSDcFIxsrCjBQ621ihzleFVro0wBPZtBZGyzcV3reLGxuQ5bmoSqLxiKZWEJnaS7Sz9GQVlEe30XGRB3104HIoT3msZT0h0GFUTYXT0BqoEYTbZSa2k5Enw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a48741736.mp4?token=mJjXNIqKkafjF1Tz7Sbi7Wb6HipTd2m0Q2d2IsvUVOCblRdBkpmJM1Pr9S-UqYkS1w5UpMJkfDBB0PDFi2BIU-uxIZCJEXuw0-Y76Nxf2ZKKTxg6P1zkDDacMlMTC5BrlbOVijhF0pvUPTzOl_rkBoP_mJPyMWcqtI4PHLERCYR4bv3u8dUP6zXYGr4MrlpBr81APdZaLXvFfLWZ4YL-ztLXv16Rpc5JSDcFIxsrCjBQ621ihzleFVro0wBPZtBZGyzcV3reLGxuQ5bmoSqLxiKZWEJnaS7Sz9GQVlEe30XGRB3104HIoT3msZT0h0GFUTYXT0BqoEYTbZSa2k5Enw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24079" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=j9rMynU99gSSMDffTpXjxkPxutzpwrPnS_Vi2yvDt4AurQ7nKJ8pJtg3Fp4tL-lFO3bP0SPE-SQga_429QUvo_WIxGkP-lnsd_e673y-XCIe_ovFpdl4nw-DNBheo-305MmXczfonGn0-Rz_VKhsyfGRE8GSDbW8bQ6RzEiV146P917GsBTCbMmrBJb9RR646jYMtQyGwL7YlF2mN5Ty4Ytn7RG_EitG4mthMUrz30NcOvqhKdTq9Nnxsg-qvm_ckiLkPmDWnxG76po5eoKbR7924l0np3t4ciFsXBDWoY787ZCVZ9s2HMr_26lr04RWOMU7x5CLeHMYB8Vn7QKEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=j9rMynU99gSSMDffTpXjxkPxutzpwrPnS_Vi2yvDt4AurQ7nKJ8pJtg3Fp4tL-lFO3bP0SPE-SQga_429QUvo_WIxGkP-lnsd_e673y-XCIe_ovFpdl4nw-DNBheo-305MmXczfonGn0-Rz_VKhsyfGRE8GSDbW8bQ6RzEiV146P917GsBTCbMmrBJb9RR646jYMtQyGwL7YlF2mN5Ty4Ytn7RG_EitG4mthMUrz30NcOvqhKdTq9Nnxsg-qvm_ckiLkPmDWnxG76po5eoKbR7924l0np3t4ciFsXBDWoY787ZCVZ9s2HMr_26lr04RWOMU7x5CLeHMYB8Vn7QKEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24078" target="_blank">📅 22:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24077">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn1d7YVkK6bTkn5ItQ8SDryXNIv-fD9_4LbYWnsbAEQCmkXA859SkhSzEBP-numoR6C_dKHXCip-RnNqJ4Dvv2IS0fdmjtJc6Erf7Hm0H85CfzhCut7H1KoFl6FrsBhAoJ0C_ZJswILJmdLAIOfmGxhe6THaarOQWJEX3Chqb4Fknh7-hfa3s6HbX0805nrqTHw1C_HtWUlnjWgsW15-IvSfdmh5DnCh8JyZBOOfisQYYeFqp80L5kCb2omjgvjlpzP5g2R61_HNFWuVhwXQii6rYxX0y0FCU6_9h3bgeqytsu_dD4FeEug47HoY5TBkwYY8F2Lz_oyXeRtJjjbv3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
باشگاه استقلال: سیاست‌ما در نقل‌و‌انتقالات تابستانی جذب‌ بازیکنان جوان است. باشگاه با انتشار این‌ اطلاعیه‌ دست رد به سینه بازیکنان سن بالایی همچون محمد دانشگر و سید حسین حسینی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24077" target="_blank">📅 21:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24076">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruQ2AH_iGjOBHT-in3aMbjzpR--CESe485Nd8evVwLavgdscqH1620qdihXqgjaKFaPOilgfGQFE5Nt0yr_2dL0ipnPavnQgOmpS95oyHWh7jKx7Pzui7fbqB5iK2g_M2kiYGCh7lETIassw6qAXDOnjtAt6LeJEIzBpb0Mm7lj2dH1KTtVqF6QfmSuo47RNE-mHkjd65G85tIUNe829qcAmRD29GbjhuyELJ7nr3s5eKXTw65-KJ4iLak-a1ZwHySv24Iw_CPE2e3YrPN577pkJFtdQFPNuodGVws2uU_7yzMcSGACCWcfG7awwEezsbfoJV8RAojgK2t_JIntXQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24076" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=qks88s04rZroq10tjFcpSXGOh0l0Nr4YT20fus2AodYL3l-GtFicZZOvNqZoNOTSEiO8X_U3f9FUJPx6JRgBa75W4rGJ7wDYKOPGTRkIjF8mRn7UzR0noz0peWjqUEmtE-VgsT8wTMd5yDJE49LzfB_YdZrjTIv0Rn8xEyoFFEr5Ricejzd-u4q8By7ApknDD6Boqo7xGr72B9jjz7Lt_I99PO43nL53-EZoMXMHuoIgqGX69jWMRHLpFmmNVRCzIgbSWk3lGFyz2sOaPjpZHsygcEA88uNV6Ztq4rEADU06TMQbaZItuD9pH7m2hctk3RNqFbzcWhc9yhXNI1wmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=qks88s04rZroq10tjFcpSXGOh0l0Nr4YT20fus2AodYL3l-GtFicZZOvNqZoNOTSEiO8X_U3f9FUJPx6JRgBa75W4rGJ7wDYKOPGTRkIjF8mRn7UzR0noz0peWjqUEmtE-VgsT8wTMd5yDJE49LzfB_YdZrjTIv0Rn8xEyoFFEr5Ricejzd-u4q8By7ApknDD6Boqo7xGr72B9jjz7Lt_I99PO43nL53-EZoMXMHuoIgqGX69jWMRHLpFmmNVRCzIgbSWk3lGFyz2sOaPjpZHsygcEA88uNV6Ztq4rEADU06TMQbaZItuD9pH7m2hctk3RNqFbzcWhc9yhXNI1wmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24075" target="_blank">📅 21:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b9463294.mp4?token=A4wXG3EvkD2rfmPWOp5RnZJVFhoqOkSf0LwasFVUNppCSC59TobIkC8TkKYPEYAW9saR6ich1HfJ0vM2pC-qTbvWH5TrFZaQDDDaro8pArWH6ibz0xfkoO-YD80UcZdN795gbfZCdWZlAR2ZhvkWNLdin5qdXE7EiR5oE_9gLr8oSPhdm1AdqbwgVod630nUl4ZYH8SsrQVF-ez7Do89IJDi7vTX2U-DLtr9ceFnlLcflB9iT1XaPtWjvMElwjQdoVaSggx5hZkhWCZ6_Z1RFmZopBQ94H2Kp7yHG82_aMlw2Gp1Ickx4Nup-zvHnmlB2ggavzETOsbs-gqqnIRWCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b9463294.mp4?token=A4wXG3EvkD2rfmPWOp5RnZJVFhoqOkSf0LwasFVUNppCSC59TobIkC8TkKYPEYAW9saR6ich1HfJ0vM2pC-qTbvWH5TrFZaQDDDaro8pArWH6ibz0xfkoO-YD80UcZdN795gbfZCdWZlAR2ZhvkWNLdin5qdXE7EiR5oE_9gLr8oSPhdm1AdqbwgVod630nUl4ZYH8SsrQVF-ez7Do89IJDi7vTX2U-DLtr9ceFnlLcflB9iT1XaPtWjvMElwjQdoVaSggx5hZkhWCZ6_Z1RFmZopBQ94H2Kp7yHG82_aMlw2Gp1Ickx4Nup-zvHnmlB2ggavzETOsbs-gqqnIRWCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تکرارخلق‌این‌صحنه‌تاریخی‌وشاهکار امین حیایی دراخراجی‌ها در بازی شب گذشته ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24074" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxjU6Nn0lo7be0kb0yzIRRnA3P8g7DwS6Js4FCQxpUe4PUjX18Fem8O_WYOUO7deEvhcTOEwl_Ck3NmSlwsTVYS7Z5LRbf7t_a3A6EYkTEw1khSAQyGQjmUvCNk-nYw2b-wlGNN7kNbf5dePc5UeFS2DUkysFlTzmiXYlqDh8Ja_xobBnXKd6ZbXSKONbzuqFSubCW2YIXTDRn_QVwUeJUTPgIL7Z0GFsVApIgLhRhZuUfVAJS7ZbmAI8WR9w_iDalsaMG3LiLOLGCr6rz8ME8wD9NEJ-xU_EUOra1q9eACYkCTF4PvmnEeS53ZN0Y1OT1ToVZ7XbcE7JjruK6qSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در دقیقه 9 بازی امشب با اتریش فرصت بثمررساندن هفدهمین گل خود در تاریخ جام جهانی رو از دست داد و پنالتی‌اش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24073" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24072">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دکتر انوشه مهمون برنامه جیمی جام اسم ابوطالب رو از قصد میگفت یونس یا چی؟
پامپ که برنامه جیمی جام رو ساخته، ترمز بریده و داره یک کیلو طلا بین مردم پخش میکنه،
هنوز سهم خودتو نگرفتی؟
این کد سهم: pump
اینم لینک :
👇
👇
👇
ثبت نام و دریافت طلا
دیگه خود دانی...
@pump_vod</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24072" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=R4mDpddvacX19K-jz5rv5AXD7b8VigAAwY448n0_LrK37dgwl-e6gdxFiHJfWVQsfE3YX63lMre71IsljOsWZ-Gue0yJjsOoMNLaTIShyHK7TaEhm-WBvMAWF14S_siYrHLVHAeXx7BLgclGNg3gQK4CC1eknihmVsAKMqhrm8GU0r_ivq2ZBnB0t7lAN_gsL7_Ekyw5A32Zet9fPqjjisEVTP_6-hqWl3t3t33TP7gbSA1dnOt4EETFEraS7aBadkS1R2ZYNXqNvP2Yf_bFftdx_dYFi-55CM8n7ZUsLqPUpCWhS7RzDZM8-HREz9K1OO8WRs3Slei5dmmZuwIsNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=R4mDpddvacX19K-jz5rv5AXD7b8VigAAwY448n0_LrK37dgwl-e6gdxFiHJfWVQsfE3YX63lMre71IsljOsWZ-Gue0yJjsOoMNLaTIShyHK7TaEhm-WBvMAWF14S_siYrHLVHAeXx7BLgclGNg3gQK4CC1eknihmVsAKMqhrm8GU0r_ivq2ZBnB0t7lAN_gsL7_Ekyw5A32Zet9fPqjjisEVTP_6-hqWl3t3t33TP7gbSA1dnOt4EETFEraS7aBadkS1R2ZYNXqNvP2Yf_bFftdx_dYFi-55CM8n7ZUsLqPUpCWhS7RzDZM8-HREz9K1OO8WRs3Slei5dmmZuwIsNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24071" target="_blank">📅 20:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u90EoBgkWwEE_aiZ6d4eaHIglxEfGxi3BMyOViagcE8AkMB26y6WOng5_cbHBLgA9EUokrNBiRLC-RFGEyBRPJ_-GPFtFzq4eGV_GFLYcVtsBsNipKw9IkDCs3luok5DJaM4d8IWUXyqkwXNleEx7OXd--j4fOGmLMbdaBItsLrXrcpFp8mxTb8S7um_MoT6UITkkg05DYfLa7mjCL4pXxyp8gJ-h0nB9_-emLoluvZX2MeTaI9kODkMSBricmp6ddEv13OhlMpMiNeL7-eLdEXdvsYjQnGszYs2JHj_ofOFuqm7c5-ejnZwNWf0ZdiN29jvxaZ4DIL45EGoy_xzaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
اولین گل مسی تو جام جهانی: 18 سال و 11 ماه
🤩
اولین گل یامال تو جام جهانی: 18 سال و 11 ماه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24070" target="_blank">📅 20:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=Ius_aFgk-pc2x50-vTVD507vtbg5lvAmTsKDFNbSU23tOe8miP7bSS1blCyO6L5KTnywCBha2ngQT3pcde5hHPrDdsCC_OoDXsHIUTaefLUON3Lc7DcPOp0RHKycIKFaCmlIZ65eBzHnN-HplAGSDg-Ygf9hkS4eEQLW6kBMiujrpDRFqeFWCzKK4zLINSzXNzNaMgGbIbFefJ-J3GxhTt9Kxdxn6sk44ALxZKkbA738r14CSMkJGl2K_w9gMbs6GpFFgP6hjDR6gQhU6SzXN9nItp0J9Yhfwql-JRnZ0w5MS2XNOh-hRPrUWzmkVkMrL5gIpxEc1BkLxmVyzKSxRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=Ius_aFgk-pc2x50-vTVD507vtbg5lvAmTsKDFNbSU23tOe8miP7bSS1blCyO6L5KTnywCBha2ngQT3pcde5hHPrDdsCC_OoDXsHIUTaefLUON3Lc7DcPOp0RHKycIKFaCmlIZ65eBzHnN-HplAGSDg-Ygf9hkS4eEQLW6kBMiujrpDRFqeFWCzKK4zLINSzXNzNaMgGbIbFefJ-J3GxhTt9Kxdxn6sk44ALxZKkbA738r14CSMkJGl2K_w9gMbs6GpFFgP6hjDR6gQhU6SzXN9nItp0J9Yhfwql-JRnZ0w5MS2XNOh-hRPrUWzmkVkMrL5gIpxEc1BkLxmVyzKSxRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24069" target="_blank">📅 19:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24068">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr1E2c5ZChT1-hFHa23Cc-LUflYFn7a1jM9jD0l6gWuuU6dLLDO_TUaeIv_puIx5BET7Db8FDi7RkW8uoKq_AkF1JAm-THoiQgPPeibkypsdvo0HxLke4g_1i_qstZU9jdOb7sKZ5UjZDWM7cn6JS5NjbVuAn_w6CwJYV9TBLAyfbnw_IOOFu1VJOARS2J5-fnUdlP1anxdFsVGoT5-MifzxWBR3Y6pTwTs49kDDYR9UvlUVIrQhfWIg4nTFtbP3FM89Lrf6ip2VmMG0DKnYtwG7P6uSd9_GcHmBWR2e01GNarz4IEYUCfH4mtg7l7iLivaSQFcSgSxFqPstokoqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛
شماتیک ترکیب آرژانتین برای دیدار مقابل اتریش؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24068" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24067">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUQyOOhwOZjcawN7XBNat7nEduUfBdTQJDjWJvWvYsOMDzhd5J9jHPB1vHdJBTnFPRVhBHkO7BosxnRFQsIpnHSLqhaUtpxccQ901EO6Yr3ZyoByGcTWJMBckcSmbLrfdpaC1MTZSyS9NVkdELwRUj-_6uCmeuJpEnq1qgjIdGb-allB9SvrzUpx7D_Mft75N1bvIoVUOegTu8uL78xeBOmLmCLpuqYgP4KTy6UZC6EMkPc4ZvwhWvD8EWHT3RUmqXY-rY6T1WXQNLkl4ce2QYIfHagCbslpC2BqfJdEcnajba6Q9k1-bRkdehsA67BnT3CMTwdYNtF5i_tGFwgkSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24067" target="_blank">📅 18:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚽️
خلاصه‌بازی اکوادور - کوراسائو ببینید لذت ببرید ازنمایش گلرهای دو تیم؛ بازی‌ای اگه قراره صفر صفر هم بشه اینجوری‌بشه‌قطعا به دل تماشاچی میشینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24066" target="_blank">📅 17:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24065">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa115feff.mp4?token=n2xPJTj64nG1jWYfWE3YgP9i8_lWFMyGmAEO5OHjmHAQTzfOkaQLEUhIWkYxzMnY7nXtfywFJydBzq7rsuS9KdUE3cjN0wNdw0Nq66mIcmM5nWT0vQqLnINygICfjAnpFYzAngpMbRbVV-m_sansFxJxAR7aSsyPsvphVyMG91q4jCjdr4LjRMfE99fjm8D0APAIzm5h9VXaLb81rnSXA6X1oUXp3az8VDrspBHlD0VyT1eIvCkIrp9S8WNazGGVKS3HYStcD38KWc6kMj14JIKGEswqD5Xkn6J9WOxLQyZLOLZgo8COM3YZh6y5B8RbxbpOJeZ7ERv6cj4FeOzlhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa115feff.mp4?token=n2xPJTj64nG1jWYfWE3YgP9i8_lWFMyGmAEO5OHjmHAQTzfOkaQLEUhIWkYxzMnY7nXtfywFJydBzq7rsuS9KdUE3cjN0wNdw0Nq66mIcmM5nWT0vQqLnINygICfjAnpFYzAngpMbRbVV-m_sansFxJxAR7aSsyPsvphVyMG91q4jCjdr4LjRMfE99fjm8D0APAIzm5h9VXaLb81rnSXA6X1oUXp3az8VDrspBHlD0VyT1eIvCkIrp9S8WNazGGVKS3HYStcD38KWc6kMj14JIKGEswqD5Xkn6J9WOxLQyZLOLZgo8COM3YZh6y5B8RbxbpOJeZ7ERv6cj4FeOzlhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24065" target="_blank">📅 17:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24064">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZzRz6Plvvvv9SvRpjby_2CA1zhJQOn7mTme76449AsKq8wr3PWbK3_gU8ItutZ3WJ_CM6lKPyZjjuMyVW1TrLvI2p2tlz-UJyx0geWzd1xo6uIvTbRHmcCBv8DyDHlu0LEgSI7FX-RohPf2dY6G2olMGLPe23uxhaa72WkDABekg7PNHkFeh6qUwxsN22bDbS93kHEgqwjeqLGrNtcZlM9E8b7Ya7lZT03eB3NJFnsuvYmecG49G76nXQvjdPsvkZMvnoU-XRqWRbuS8hYAgM14D-24s8ISr1BgDbCbjtVyIn8IWILqXtvcZ05hZHbqfP8tEdFidp34g7bqlU_vjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24064" target="_blank">📅 17:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24063">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5Duqj2Hyfo3Fq7jQPf_Cq8gANc0E0dAmQCGxogwBI8Yxw1zmE6skZYGZHzLyOPznqFI5JL1C7oe0IC-DBl7Q9vmWoco5-XW5CRrmxb_YP0u19sMJKXzqp3pE-cSiQo2uUB8-8ra4oanl2Axj3Gjqyz1clSioOf76fjsoJR7GAeLRgfHCVSATNyO1-a-UQPqxvi-Gp-9vMGTq9Nxokaa544hYiqzacq-Tm_tE84oRO1QKrXqcZ9QVOSYCS7Tm8qpS2v3Yk7vp1ZC9nRtbqXhBbwazng765vw1SOamfcM29VzaDM2UqSEYijw_UUEbnaJ2lxbhcd5E81Pr1WHol9DoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 گلزن‌‌برتر‌تاریخ‌رقابت‌های‌ جام‌ جهانی؛ لیونل مسی به رکورد تاریخی اسطوره ژرمن‌ها رسید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24063" target="_blank">📅 17:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24062">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBydA0I0poFVtKvSRCTbbgdznlXoT4_4b_h_pZ3md3yHedCJhMwOnzy4hpAF_wrrxwpi9lSqVS90mWQP99VkTmH4keP1eesg9Elk2zCPEUooC8wrgyeFxdqSM5Kj7LkyZfG5NeAwDCTVMWSsMWfKDgqKkj3ZiGkDFypixM4BfVKRfPOLCHE733zIp4sSQ4U_cMOCpj_83IOfpnPt_hM6HAEjab10oIlyW4qZl4RgNAID0GW2XgJcCTPsxj_N8mKYhv2p7tZObVzTKKy2bSz46O-qtnTcbC-pYCGq54NcybFQJ2w4zmZxauLFFUPSIp6cotvlwH7bRDq6YctaAPPlQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی وینگرآلبانیایی‌استقلال با انتشار این استوری‌خبراز موندنش‌دراستقلال رو داد. مشکل پرداخت مطالبات این بازیکن برطرف شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24062" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24061">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f988706b3.mp4?token=nU0WwdT2vjn6Soc9zjgKVCZYOo_yFUNORINR4zDG-pXJ2_e9O7qwgoqHtrypwcyn2YS62fPECd9Ypm4BpwPn34GlPfKBe_QveSWmF7fGs1gW20Lo-XHJAUtIN6lOm7Ck_TTyBhE-aG4hyUKeZ3WGdxNxC-VvYr6FZjug1Kt0d9nkZovgzwNVnqQo0-3NuoK5L4oVHH71_P-N6-_UoM-3KvREFC8TRTb6ypRdUHJqwRq_HgG_RgUGGTl500jVjGXJc-dHqjLJEa3FWH6QdgeX709Gs0KEabST-ZCrTlnwwi6xoNPcDizOFHqvO_Go0pSHyZfegOCFHUPZPEdoygwYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f988706b3.mp4?token=nU0WwdT2vjn6Soc9zjgKVCZYOo_yFUNORINR4zDG-pXJ2_e9O7qwgoqHtrypwcyn2YS62fPECd9Ypm4BpwPn34GlPfKBe_QveSWmF7fGs1gW20Lo-XHJAUtIN6lOm7Ck_TTyBhE-aG4hyUKeZ3WGdxNxC-VvYr6FZjug1Kt0d9nkZovgzwNVnqQo0-3NuoK5L4oVHH71_P-N6-_UoM-3KvREFC8TRTb6ypRdUHJqwRq_HgG_RgUGGTl500jVjGXJc-dHqjLJEa3FWH6QdgeX709Gs0KEabST-ZCrTlnwwi6xoNPcDizOFHqvO_Go0pSHyZfegOCFHUPZPEdoygwYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24061" target="_blank">📅 16:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24060">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyHZlOtam_u0AfiABQcZUHJV-mHxAZ8MCMuwLa7EljPWWnYNCtcAwIBBqULlWLcyP9nRc2JbmBfBP4wv1CvBcwHJCDYtai5at2hF7NPbOh7U6SD2mGfhA3rah92nl1Pw5cUd7G9QVq_wvg4QDcAqCYOojq2BG1nuILiOm19CKFEtC-88dGPPzXqrakGCQtxo8d7epYoVM0gcTKxLy6uNdNaWq7auhwiR_yJCgHDPozlm101GiMi8FTZjaYrjfi5kxLSSXX6Nd8pJ41m3BReZDSw7VwCZU50ClF6lF67ppvWT1RJYdEPYei6l-n4mEw_h-5Ody6-5iu79mO1ia5vweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24060" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24059">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLOc9es8fcnF7SvVsYv2tFtq9SnhTJ7pa_Wv5RC78YHTl1ss42lxwnA9W65VciLirXdkfDqL5DQs9v3orT2PL28Vwviq7HlSuAeWgbIbZlHr2r35X8WgBC38WISh-DP7fN1w5zbHSfAMQN4xGBkjPV1QjSyGOnp5zwx34j3CRpWe5-pUZ5gTdUNM1ZEfooIYEcIkgoC20UZu_PO6ZaQSxZLeIrCjTcV0MLv94zX26FJYDYaMN2D8VlNuhtwHhYrQYsePYHPT4pvSENTL3VkTbrGVtfEOCb4PA28QagZGLoTIyN6gudmZSBzlFihjspSWmxXTVd4uhqJuwYDWNA33Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24059" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24058">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y55ubo7WmN5OHxr3enZwBO9kUbHfEwqXZdTuknUYxDYbBoEfpn_420_lkpOuqitmbnbKgW9ys7YCxrbhp7ltARtREN_S6vPJDf_HsAwzTnb_cXUFuOXb3TQ28lgTi7uBKBhhCxf1nbvVWmW6wKpKKidnEg5M4h5XmtELAc18LPxv35GTYc8vU4VXT4CGKCrQY23u_tBDmIK7IXgYlmQfGiNg0G3rNorjsz9PfF-j1Kbj-roByemy84G6fa1xGJDpdOjjsiShPc7SXypGqE1QpfIU6IJPrZ0d0l51DidvzziyC9KOzQODVDK1i7N4Bh4zUh6NSHrQSx93l01yCBMSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمام‌حالات‌ممکن برای صعود تیم ایران به مرحله حذفی جام‌جهانی؛ازتقابل باعربستان تا یاران امباپه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24058" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
