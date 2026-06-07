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
<img src="https://cdn5.telesco.pe/file/CH1tcVEJret5meoBP-vGYlqORPKg7tV7eRGo4e48DFhlV0SOS_OnuaK7y2Ji0TzslvxCtA3Z8mJodGOXqxai-QQhqhq64yDrvvZ2-BdMZKaieE4xDT1-fc67mOiEIdV_D5EH3ngQoaZJVGJ2xb178UfSmNLGRoS57E7nkF_gu_fXLWQOdDrASiiieC6wSZsNlSMxMqfoC8zNSR2fz-EkO5C25D1UeCWwI-sG0X71vUCgFDCkTc07C9MYKF2KGgFtywwZLzrrZCxNNbxStRMHeJAZro_MqhFrsifixFO09fAcSUnsnB39xPdooZzbXcblnLD1-A5WfCYb826UTzyVBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 244K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 18:19:09</div>
<hr>

<div class="tg-post" id="msg-91319">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ساسی هم دیده کار و بار خوابیده اومده ادا قلعه‌نویی رو در میاره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/91319" target="_blank">📅 18:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91318">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoF7S2fmSWm9LYAhpWe6v5uYlr6yZqkzqby08CVIRW9TfMzl_jPXMTiuPyJ-1V22AFk62W2u3U5d3754RcYVlSGqbnoHRjpYC2NEtPS01v5-gjzaVbpFABXcXXFjJgIWViAtyTSqmRlwozfxoJ_Z00Kt9SRmVc8mUfZKOja5zgxFtrKkV1G7cD7ucA41wA32dGdXeZrK9M3X7TGH5NfcxXH_RPfeXgGsNla3B-G8SK7XfsKC8YUCByR6m9FRf1X1i72bmaFaDCceT2iU6fvmFlEdi1vazx51aorgN2qcXP-r8xMoLXNjohGshskm-6CCXn9ENJ1ddzUdtWehgIuFdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
🇪🇸
رومانو:
ژوزه مورینیو به اندریک گفته فصل بعد یه مهره مهم خواهی بود و خیلی هیجان زده‌ست که با این بازیکن کار کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/91318" target="_blank">📅 18:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91317">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFcCcChpv0xCk8pafxNcyMc30joFo6cnAQUKasZOMNhoM2TxJ6wF0DcL6Rhn0GrlwsekLewq8xjjbF4_C_kQy4yH1CKvZ6k2nsO_pCP3wqzY4lvu6TviPbcXzh6V05tXgvKzx1yJlcyGMj_-r6iUgPMxQvZjQFE-UGj_HeEELBJkSmmbrQLS9RLzPokg6-1j-aWvnFPHNa2ATeee3O_x7bAuafAGRWEENF7dHfT6X8z9thfhn5RwefR9hKnaKh3b8WRgVZLDH43nFYgVCpnF9rNkR4mQQ4A4EGt0AaSByyNubKGU1RaZ5UlXKy3D8lLkYh4P_TjL4wgf2JkDnQUWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
فوری از رومانو:
پاری سن ژرمن حتی حاضر نیست برای انتقال ویتینیا یا ژائو نوس مبلغی رو مشخص کنه!
هدف ناصر و انریکه مشخصه: نگه داشتن همه ستاره‌ها و تلاش برای بردن یک لیگ قهرمانان اروپا دیگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/91317" target="_blank">📅 18:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91316">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHOH6kKJaHcKLljicZ2WJRverYS8iDkN7GEk0m0vitFiujUBH9G1j2xRIIw1aU-5Y1SJyK7xK5_WSW4PFiTOV39Uym-E_IdiuNTk1eiiol0MRUevMRKQZTZaumvY4KCqdwgfZQaRNVbb7rd3pJlQ5UCCSpb49jH0XSWoj_AEzIf6-BpLnxtZFhIdGLx8o9JkRidP-WmPF8OVPf4c-bJ0RSvOwkaiavI0mK8j4nseura1AlhxJDN3Hq7cRRzOo9gBZL-g9_yGulOGAo349xH7QdakwOgDqzw6dNQRVMX0pdlGVDRQfkbvqyfNnqAmjEd2dhBeShJrYW8SCKmnedDUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
رومانو: در صورت پیروزی پرز که قطعی شده، اولین پیشنهاد برای جذب اولیسه تا روز سه‌شنبه به مبلغ ۱۵۰ میلیون یورو به بایرن ارائه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/91316" target="_blank">📅 18:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91315">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXVBzDsAxjjKNwgyQp5qhqRpRp-MLCP03x33Ag6ThAhldUkmuOO3CU9l0wdnoC7QbvCPqFVtbmEx-QvzxuPqohn_PdAXqX3QqLxfnblQ8ZZJ5NGEQlIcmwFoVkvSH_4TogPF1wRtVF2WN0jfW-gmu7dpBcyxfmRlPb6deHTGg3yBa6sP4062oXPVIFtY2lbmwqqRC2mGhmtjLFm_eW5krNsI2WRhEW8olnsHGFdzheaA9PZW_0oUgjXtJElzxsgCnVXg_knCMLhnwt9igFSLFOBzJ9mDoSUigttOyGEbYCcCSh9jlGuRPbmeyaf2epkaAcq3LLdkntCmetIeCR13ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
رومانو: در صورت پیروزی پرز که قطعی شده، اولین پیشنهاد برای جذب اولیسه تا روز سه‌شنبه به مبلغ ۱۵۰ میلیون یورو به بایرن ارائه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/91315" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91313">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ab97717f.mp4?token=qz1SL16xj52FUzp-B2GTUV8jc6YJZSj-k7lULy206JCxMyXgOYPI0pfXqzSWLtUMzJB_Co3dFCocpw7YXHiUy-cpiHdMo6chv_2wlLPN9LUzow-x3Wm_c6-DsUnlmPcT6miQJ4DLoDKhHXrsNDVhg05leODBOC8O69QkRwCvySpkF5HGmduc1qWx_QSoTzIPtMhHL6a4YvNO_dZ0Mt_cj1afAj_eGLRcwJz7VTF6c_DJikysC8oewl36MdbyUb14CAgCuTZOJNnxLL469PLKUx5z1SRMKYwVdWBtjtIX4_7gcNjcQiCjtroISZm5EgGsv7J_s-aJ8cvRfM2qClA-Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ab97717f.mp4?token=qz1SL16xj52FUzp-B2GTUV8jc6YJZSj-k7lULy206JCxMyXgOYPI0pfXqzSWLtUMzJB_Co3dFCocpw7YXHiUy-cpiHdMo6chv_2wlLPN9LUzow-x3Wm_c6-DsUnlmPcT6miQJ4DLoDKhHXrsNDVhg05leODBOC8O69QkRwCvySpkF5HGmduc1qWx_QSoTzIPtMhHL6a4YvNO_dZ0Mt_cj1afAj_eGLRcwJz7VTF6c_DJikysC8oewl36MdbyUb14CAgCuTZOJNnxLL469PLKUx5z1SRMKYwVdWBtjtIX4_7gcNjcQiCjtroISZm5EgGsv7J_s-aJ8cvRfM2qClA-Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیدترین اظهار نظر وحید قلیچ درباره یحیی‌گل‌محمدی و رفتن به لیگ‌عراق
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/91313" target="_blank">📅 18:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91312">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
سخنگوی کمیسیون امنیت ملی: ما پاسخ قاطع و دردناکی به حمله رژیم صهیونیستی به ضایحه خواهیم داد. امشب به آسمان سرزمین‌های اشغالی نگاه کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/91312" target="_blank">📅 18:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91311">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW9FmuNF2Q87La0T-14q06NgmWRSzbxyx3pwgRG-sB_nC__JWv7ddzZU2nvEhDM0OOeKjkdeeSRq1Kg_soThIGGj-IoLcEOiomhzHXlZjlN9bM86YgffyH3NIV9moiF8aoj2LUeBqzRvoBTCTO6khiwU2vxHW9PnKGoQjA0eO9snMjHrGa5tamQhB1JPTDEh4rL5diAtXKf_FmWsR88f0ZrEUcsnfMKRQVn59pIII0BLH3YQP0dZlZuwirqb1H4NpIwnYBOfMZBFmWKSESTpzg8fNHp9WOSlQbLcwgKTQVfOmeOMv8uP1SxHYBQB4iP10m1wKNSCSt7J7qpgK7Aoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضلات مارتین اودگارد در تمرینات نروژ قبل جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/91311" target="_blank">📅 17:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4446042f.mp4?token=J9DqsH0p1GsBmkrO1cHeO2j7c1Z4gEepMk2KL18VMK5hNxAF1VaeCwC-RIiKCA_U2Jx32sKuFP1v07f_7KVp56H4oPwiylkdwlf-dVtuUPrU_Y2vWY_I11bJOOAcwa2VSTLurvU53FN-pQPTrlf8HXmDXq0eSf6fv3JJNG8k6RN1zEQu7xIWsw1mwCoB3MHNqzxXfL178bIO0nwx2sla3lYP7hhpiFSz7ksvBYOtLdkCZGoLpu7CQmRTP-rCR1ae7uxwW_Svwl8hgbNMAcQ0u8OeJ6kDHYDrHFF0zUM8FrHACWq-LP2wHFQwpQx_dskYhYM4SoguGEoSYJWU53xQ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4446042f.mp4?token=J9DqsH0p1GsBmkrO1cHeO2j7c1Z4gEepMk2KL18VMK5hNxAF1VaeCwC-RIiKCA_U2Jx32sKuFP1v07f_7KVp56H4oPwiylkdwlf-dVtuUPrU_Y2vWY_I11bJOOAcwa2VSTLurvU53FN-pQPTrlf8HXmDXq0eSf6fv3JJNG8k6RN1zEQu7xIWsw1mwCoB3MHNqzxXfL178bIO0nwx2sla3lYP7hhpiFSz7ksvBYOtLdkCZGoLpu7CQmRTP-rCR1ae7uxwW_Svwl8hgbNMAcQ0u8OeJ6kDHYDrHFF0zUM8FrHACWq-LP2wHFQwpQx_dskYhYM4SoguGEoSYJWU53xQ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره باشگاه رفتن و معایب خاص‌خودش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/91310" target="_blank">📅 17:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91309">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUEsi5VJzMxBL17Qwox_Q2fRjQidBVVli08p3fu41R3bjpgSQzhkFetggKDE8mItmNcLXLL3HyGr8XLtSvcQ9RKWZw3tCeQUixXZgrEK8P5YYMLaztc3y4_bVS2Tu9q_CzQwNOBl1A8VEm8ndxmciqNwtVn9FGoNYxj9HxJs3Jg_yRlNAxeqcw2Mhk42BMR0a9JWHuis_pHJByZvB1Ow5bHjAw1lMDeb2NNYUMtuNYSnOdQ643UKqyiOxjZXXWhGOFO112qeGT6WMWcOAPa78ubjiX2kBH7Iep3ce9gRSAeHk1MRC1lU78R82oDR5A-9_03etvgORKNC3S6B5z7JaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی منفورها وارد شهر تیخوانا مکزیک شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/91309" target="_blank">📅 17:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91308">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxdBLZBnQnMUOAysOv4i-S4gz1bUNmBEsxCjr7f7mu3sqfSeSHJHooH7rBrQGdTT88P3Q448IJcg9Fga-iQYVuZo-dN9IR-GPRyd3ckl1DHqQRJqvl18JY0__i_cRrp-fSIGa8W4eKfc9tE193idm3vwkIOKPLj4SOIPOn5_8niDZRb8a0zGR99fOaDZFBs1xlD6JnYlSTLC5MqxaF5hO4CdbYi3qFK9eQKnZziRGMPxpB_Svb1MPeA4ugziC1rHkL8kQOGCxUUtuNsPFSOk3X-nWSB16m9a0-NVprlEZskWiqBWxc2mzqFWsN_py3Mxgm1d2yxyeAYgy51rJOyR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره قراره این رویا به واقعیت تبدیل بشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/91308" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91307">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VYzT-T6xgGswDmGrzyL0Mu-eTzybwoElr7b_-Tx4d8M3LspIcuw-MDAonDSeCK0FJIsgtV-6FyAU4MGAo7oxGKRia32Gmjm8dH8Hw_I4r74tE2MErw3cv6aMsw-AuwlXIb7Pc7Di6VIUYfglwFEztCldr6d4Fp5S_9yht1OxDKYsVeb7tvT7zzvAwa3ru0dwtV6RS1sSD_SvJrBkw7vRu8HkQZ36EXsO4PuICqQiFQcOAoE3WXWifZB-Msq4fgCfb47aGAmByODD2L9JVO3pnePlil0rFuzDLf4K5th7El2rVPkFhmQQWAeiqLAIOfYNUOVInB069eNhA8rKBpVSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#غیررسمی
؛ الیوت‌اندرسون ستاره ناتینگهام‌‌فارست با قراردادی به ارزش ۱۱۵ میلیون یورو به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/91307" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91306">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmCf9laSKxJw5YMabKvbhoQIJDWO9NjucbTtd2QGHbmndTxJGuFUXTdnHno-NhjHsRyeKx2OjJecKgDRBn-j--MtHl4tMSCcy6oJ80nPld228eEotmIh9Fpoqu5b8MZqKBTKy6ncn8ibYLpNT_rqLJgjq_eaJz-y5fC4f9_s0XbI2G58p793ROMTiACfwHFiKSlA_d2eSQb1Ir6JinF8ciwC_mOfF2t0dtyrCfKSGrSvm-b9epEIAiLXxvbVf_vORYr9OGHfrwMOawfMeCgGYnCrG2wqBhEE5WZ1Nn9q2jhWDB04FqUtg_uCHaCr94PuKIeP2bkCFvy3WI4GYytWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
شرکت آدیداس در حال آماده‌سازی برای عرضه نسخه رسمی بازطراحی شده لباس سوم رئال مادرید برای فصل ۲۰۱۴/۱۵ است.
❤️
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/91306" target="_blank">📅 17:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91305">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpWHnhBTNYsujBWeV2fJgQb67w_Z63vbR36Cnbnw9vgLc0YGv0gP8wDMGglgL_WLsOuLoxyoNpn5_ll-57NVpBKnLm3CDFaDN9hhsMkN1DfHYvVaTIvJW-RNhyx78mdkZk5BV5975qutYux4781PZIsFkC6ZAH1pVPbL-TjGny74NCLFgb1Ve0v6zzzd9PHRUvoR5l10e3KBNbuU1AZ9maOighIk9LnfbHlYo723vamkkHxG_BXAUJblGYf202Bn7epwZpPYx7Qrij1anFgKcoq6v3cxCIYzQZB_p7z6JzKMBLhwE_1-nZ3Pe8uV09KBX0TFR-bXSeGnM8qFuiLFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینو پرز برای نقل‌وانتقالات تابستانی رئال رقم ۳۰۰ میلیون یورو بودجه تعیین کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/91305" target="_blank">📅 16:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiy1DoypKKYFoUDwlHWGYTDzJQ3Pqco1q92mo-Onmr57OMUr5bxWVfFF2_-dKHCtOetw0I-2-bAoOgMkyQvX31sSNz2jhZCAKiUZ5zao1QDSWNm5u_HV2dEaeceHcYZ4UxIncCqvbP1a93x3eFtnN4K-x8WZK7mRNpRDB5lb4_ttFmk17Gn94jEOffo-ezz4tYoEVsv5S0DyIU_k6E09TuPkzRtNZ2OKkPU6VgceI5pFRHb4BO2_KqegkOpABtW73B-63EX8C4dmu-fpPEo3vQ_xCsi6wWY9Dn4mUm3alOkj0t4usVc-IzdVXinNndYyZOQZQ8RaloODAV_va4QdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو : پاریسن ژرمن اعلام کرده ویتینیا و ژائو نوس تحت هیچ شرایطی فروشی نیستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/91304" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91303">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfmQh5WdrMLfZ2X-ykJELD4Usvq1frOXeDius--5hcHpz35a67IyyZGxhtaX8jme5o7EGwEjr0lrJjPDVFJ0sgdbWWZSMDmfAX1izT_RZNXJ4LAgu7WbjcxVJSTURIkT3xNCzoXYMChSm73yTDbQ_-j5GviYaWXhV0htT_IzLwMgy_h3WgJa3WsxTyjgb8kVth1Fl5Ea3eUdF0rbWaqoPQLY5ndfRQhtyNtLlMshOvzHyhfkLPHdyWvJXzduhjwIDzffvOt17TfYhlY-52VYyHPEcUO8vlXCadoXlkOthRfR_5TYffcRL2kILRTfJ4uERKk-60jz6FlY7uDCs5v4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
#فکت
؛ اسپانیا از فینال جام جهانی 2010 تاکنون هیچ بازی را در مرحله حذفی جام جهانی نبرده است.
· جام جهانی 2014: مرحله گروهی
❌
· جام جهانی 2018: مرحله یک‌هشتم نهایی
❌
· جام جهانی 2022: مرحله یک‌هشتم نهایی
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91303" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91302">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7bOGioyTcjyA1UGJAbkwLd-Ogh_JeQFgJOx6VmGL0Urck8LmwWXIWt3kHOqV1NV_sm6qJCY8NuuoJszKg6tgG6FK2cJlDwaJ0aeYVXj9TEUkdpMvesptBgf-qoxNJ1adcceHrT2ERSWjCEcF1JLpHC6fGglpcnfu5zqWTN9Kjt4x-MtBtDrBeX5Np-DT6ssi92lm3eYHDf3WXLhL-rjglXO-oVyMtbQMV9WVl4kdjOmlFpFscXDXfqDd_Jhdr5KZ7QqIV1B0wA4efXzMSvxiyOfOuE0XHlDeAJfWApZkQCuB_PLQ2djJJL8TFNMRInsCtd8sW6XjUJSrXWnOCp_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت‌های سکسی پرتغال مناسب برای انواع و اقسام مراسم‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91302" target="_blank">📅 16:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bcfec576e.mp4?token=jsb-DO6po5VnN4nMXISZuSrMynrScyLF_j_x7qIoP40aJCxKDUO2NpVfx3YtwaVBN7qcVLMY9eLtXosCn7FWPl55njnnhMTa096iFJHgSvbpkrpxLMg62AiMpusLN9L9v1KfdXlHNMwaQ3BRxa3OlYuwkNlDeubbcNl1osEYvvyZMZM3glcMY9BYyW3ICkpUdppEv2XRh3K9qTPjfAIowsHD8ZiV-nEPfwzcLaW8LxZok_RkBfPiwGTPiOqui7ZCMTeNulw533H_4KcQ16oK5jJ8S_dv3h2iWTdyQHyJop5AguS2iuz-b4nY7Z_xd8IfxaTsCnwOKYzdE6knXcKLpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bcfec576e.mp4?token=jsb-DO6po5VnN4nMXISZuSrMynrScyLF_j_x7qIoP40aJCxKDUO2NpVfx3YtwaVBN7qcVLMY9eLtXosCn7FWPl55njnnhMTa096iFJHgSvbpkrpxLMg62AiMpusLN9L9v1KfdXlHNMwaQ3BRxa3OlYuwkNlDeubbcNl1osEYvvyZMZM3glcMY9BYyW3ICkpUdppEv2XRh3K9qTPjfAIowsHD8ZiV-nEPfwzcLaW8LxZok_RkBfPiwGTPiOqui7ZCMTeNulw533H_4KcQ16oK5jJ8S_dv3h2iWTdyQHyJop5AguS2iuz-b4nY7Z_xd8IfxaTsCnwOKYzdE6knXcKLpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
شیث‌رضایی مدافع سابق پرسپولیس: در دربی معروف آی‌بدو آی‌بدو، علی‌دایی تقصیر باخت رو گردن من انداخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91301" target="_blank">📅 16:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91300">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db9b67547.mp4?token=sWwwfXi_naZcJRCh7XFoQr4EaxmmEhCo7xrRF7C8ZsbURERhaLDlHhAV33C7FVZKC3Ctku0THEkgIWIL7BEXHjC80mrDYDbgxpn-ocUug4ALCUlSp1XWwZVFlQ8vqsy3k9PdnyfolShy1JO4lES4_VYG7JmydJHaOh7ntD6KYYV6gx51EjHmyati36QYGqIBgGZLfjWeUWliry7a626ZnbPF1_rgwKD2LIbtNRJ0oj4iWEKQqNUUu53i9NERa0DJp7FuXhaTrlioONOxERJYEtMOxGjuIGUOmVPL_ZJb0l5yDOd6EX8zVoEryi-DP8VvbtTtX53Nyg3iScn8ucLqlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db9b67547.mp4?token=sWwwfXi_naZcJRCh7XFoQr4EaxmmEhCo7xrRF7C8ZsbURERhaLDlHhAV33C7FVZKC3Ctku0THEkgIWIL7BEXHjC80mrDYDbgxpn-ocUug4ALCUlSp1XWwZVFlQ8vqsy3k9PdnyfolShy1JO4lES4_VYG7JmydJHaOh7ntD6KYYV6gx51EjHmyati36QYGqIBgGZLfjWeUWliry7a626ZnbPF1_rgwKD2LIbtNRJ0oj4iWEKQqNUUu53i9NERa0DJp7FuXhaTrlioONOxERJYEtMOxGjuIGUOmVPL_ZJb0l5yDOd6EX8zVoEryi-DP8VvbtTtX53Nyg3iScn8ucLqlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
🙂
تنها چالشی که واسه تیم‌قلعه‌نویی ساختن و پسند همه مردم ایرانه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91300" target="_blank">📅 16:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91299">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcJkMuepDCQxH56mu-bX1vOMnqklHmK3dkCPjWJM0fBMLERnfZg1uqQA0UDh7GzOmBcjvIzBQoypfUpHN9PBj9Bp9nHaL7qmxMDG1ZfdOxsQg0sl-Z47-P11Lv4ma8At5h7OT-Igfw0hFKwX7QLzDOC9IhcbjxJ6f2BS8gDug1sP_KC1-GmEDliPk0zQC70a30zzC9U9RD5bYxDA-Ebrmrk73YTZ1r0XA9Uc0FVs_2OlHibgs9FQELsVqUKoHRhpZ8kMEouqlS4bZec956cDPJVnugoOsBQh_LrD90_llr9-JeSPi0zwyR2UeUZwe_28dzAqN_ndBNU470ToYA2nGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای فرانسه دیگه بیخیال رایان چرکی نمیشن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/91299" target="_blank">📅 15:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91298">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjDYBYu5CXu56aYMkGV0nj6TRePV1EYtVmvPHglXoC0QRiG2xIXCYLfclXyui9CGRJmTfsqYvDS8EFg9ZlqvsHTP9unQpHV-h1HgiEGQnxrG_9v-JRTOZZyx--MorKUUwY46iBUy7VBxg6MIUR8iKkcF4Cke1REj6SttxWRpVN17Ldi3pX7aBvBGeidsbge1R3dkjwRG21yBoPfV3AQYeMZm3JwUWgYmluDyme-nEaeayyk68YnCzg_ayCma7HyAv0GMONdERiaBdvEAvzSqhXHLcYsdHZsHQcdgoJrmIS2qQUSSFUHeB_T2qd2Z8lZDXilLo_Sc-3JhmcPce6WMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمیز از نظر پسرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91298" target="_blank">📅 15:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c920142fb.mp4?token=nBEBtGH5vkGB99XhGdGvxczYLgstdujaREWncObVP0zlSqZRKnMaDOkAt77DRntnDav0_sq-QTomK-CYoJi8wivKWk0kN5EaxYZJbhMhC3RWOAQfu4Tv5zFpoWsuZ9wUFYpgMesfE-w6nkSfTjHEEE1Brcb1DLYeYvLjY6g603p3xRWnHIVnAAs82CfnO6oMCzEr-VGe5zFQErt8Tg-vXPDMQzKW23dOKMq6dTTKls1Z73qLCuKcW9RWtsUeea2U8t5oY_4kFPyNUk9hWBleFDIJE_ryD_DuipMSiZ_Y3KFvkvjO3_C1hgjvg3m-QffSqnUI415bFXn-LhSYmOWVCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c920142fb.mp4?token=nBEBtGH5vkGB99XhGdGvxczYLgstdujaREWncObVP0zlSqZRKnMaDOkAt77DRntnDav0_sq-QTomK-CYoJi8wivKWk0kN5EaxYZJbhMhC3RWOAQfu4Tv5zFpoWsuZ9wUFYpgMesfE-w6nkSfTjHEEE1Brcb1DLYeYvLjY6g603p3xRWnHIVnAAs82CfnO6oMCzEr-VGe5zFQErt8Tg-vXPDMQzKW23dOKMq6dTTKls1Z73qLCuKcW9RWtsUeea2U8t5oY_4kFPyNUk9hWBleFDIJE_ryD_DuipMSiZ_Y3KFvkvjO3_C1hgjvg3m-QffSqnUI415bFXn-LhSYmOWVCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه نفر تو ایالت هرات که ادعای پیامبری میکرد، این شکلی توسط طالبان بازداشت شده
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91297" target="_blank">📅 15:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91296">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeAFcVZhgybxxA_CqFgzeu6OLwNwvgih385HFkprbIgVT8H6MC3DDldLfQ2ubfIhd1ahTkaq8k5DYBj3EQNNFPxNN-ZF9hintf96wpVcCSJq_Uat0e3WXv1NQ2YKvO-tkSpwBHd8-pjjfFRVeFKanFpgJQXFMr_E5vkhWMBUWjnZCi0WYM8uuAz6WomQFAiQ7oEMGalSaVGY7PdaFbgftoroEYpWpnzb3htKn-x-R82vuqDs8k9obPQg0xwHtA-QcQra2K-L__nnJTHvRbcsMkekCwNJqQKGEw9OxHyWQG3srfG7pbt3ghqOZUdui-EQIz1xIatc70Q0-d7uSsYd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 7
🇺🇸
استادیوم آتلانتا (Mercedes-Benz Stadium):
🔴
موقعیت: آتلانتا، جورجیا
🔴
افتتاح: ۲۰۱۷
🔴
ظرفیت: حدود ۶۷ هزار
🔴
سقف متحرک به شکل گلبرگ‌های گل
🔴
یکی از زیباترین طراحی‌های ورزشی مدرن
🔴
صفحه نمایش دایره‌ای عظیم ۳۶۰ درجه اطراف…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91296" target="_blank">📅 15:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91295">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Onay55DZDmx20RsuJ-vX8V-q4Qq8Uhgs_odbFAWGUbqZoVvWHRzn7caTwsC7PvnLcwAzRxjNEwhg-vM__KOjDknvEa3Sl6R2Y-O1LjWXwoNdk8cBJ_In75ZBPWDAxziGVEJuuHFza0C7l6JyiSC5Y298ez-u8x12gvR2u1aDAMmRHdxP3Mz5VUEQD18-yIlcpqTQp5rSHCj1C2SoPPa5N7h5_05NSLHa0HA_8t2Ibw6c6WrT9aRme4ayhJWvAMum0u3BqVK_n7n6TDzWWDfCmkW6PAXffjhPoibR0E6HCnyBwBd5AagIinSZ4COj3iPg77cHh08E_m0a5fOuSh5XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 6
🇺🇸
استادیوم منطقه خلیج سان فرانسیسکو (Levi’s Stadium):
🔴
موقعیت: سانتا کلارا، کالیفرنیا
🔴
افتتاح: ۲۰۱۴
🔴
ظرفیت: حدود ۶۹ هزار
🔴
یکی از استادیوم‌های مدرن اولیه آمریکا
🔴
استادیومی هوشمند و دوستدار محیط زیست
🔴
دارای فناوری‌های…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91295" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91294">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6Z_NlXMAnHX5Kx-9Zs6DUV7xpkBKrMFXgAF9a7gWAUu0hfyXHjEmHk92rg0SHf6aCOk0nNoXImdPaM71V_ibNC4PDrH2W9FKEgyOXK1xJz_02JMs-0f0OSl285JUiCJV4HNxh9cKiXtt_SjFZtrmXMxpjtbc1Ml_9XvB92GAi9AO97XRZ4oNI7eMkbKoLkOjmyLhfdEODwFsjE2DhtuZpyz_f0jzsMi9Yu5aeo59LnMwfaxBOLEg8LIqbHNVpcmA4hKqo-3l9IQBZ1mOkt-OMvIKaXacb85JTZbzgfIoS2LdO4oMTLyDC57i5srGSq2owrMlb6d628q2QziTdHHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 5
🇺🇸
ورزشگاه کانزاس سیتی (ورزشگاه اروهید):
🔴
مکان: کانزاس سیتی، میزوری
🔴
افتتاح: ۱۹۷۲
🔴
ظرفیت: حدود ۶۷ هزار
🔴
قدیمی‌ترین ورزشگاه‌های مسابقات
🔴
دارای سر و صدای بسیار زیاد و شناخته شده به عنوان یکی از پر سر و صداترین ورزشگاه‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91294" target="_blank">📅 15:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91293">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2aCCnG2nv82574PlJ7Xu-UCtYWhfTRl0wnK7KHZGWPbidbtSdEbrATdIUV0xC12IrcNmZjnRuq8Xu3RBZgWnrLkkuv4aT_BmR06EdCBpY1O7VYe_FAmO4Dy3XYxqLNH25sz0xB_Mg8gOiHCKdtOfJL7uWzTsrard5jShl3GLestTTEhdRaQCWevLzcZDZ_0lRLyiD0O1cz8URZYfHEPzRFBqatqYlElKeid8KMao-BQQ_Ir3yK04LcVl6CLVDdqJJHdwnlKSRTo9iQ5AFFOlRIK0IjzKmS5VLlZlkHfxcX11iQCUISwhReF_4zUXUwbZFpOJoetJtzT1haRmLGwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوناهم مجری دارن ماهم مجری داریم
😔
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91293" target="_blank">📅 15:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91292">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bmvg0vPoEL7CTKsGNoYIy1EWfoqFE-s-0kbC9WB5TjN-H3b6d_9-Mu64kczmVTjvaF89NRlChkJmtDZaZq52DliaoQXv7yU78APRYYkH3pK_F6nQ9Xncx7yECtsgYWHJD75L8JLxe9QZoCNRA3ovX6DWQhysUMJdCZ8n1Tc3Y-2peZssR1NV-aj-StuIgUC1o_Z0o-ZXQI_t2-ID0XYQCh6ReqMoF9zJ1tD7iGGQJicQpzCOCk5NP-9y08Wdlnd0bnurtWwr0-Q8I3WbnyW1NhpfXM2HFpbOWkDPq--JXwb28aGSryijkHPNb0kYzVOD2zcUxVjhjR6v_GuVmEACsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 4
🇺🇸
ورزشگاه فیلادلفیا (Lincoln Financial Field):
🔴
موقعیت: فیلادلفیا، پنسیلوانیا
🔴
افتتاح: ۲۰۰۳
🔴
ظرفیت: ۶۵,۸۲۷
🔴
جو بسیار پرشور و هیجان‌انگیز تماشاگران
🔴
ورزشگاهی باز با سبک سنتی آمریکایی
🔴
خانه تیم Philadelphia Eagles فوتبال…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91292" target="_blank">📅 15:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91291">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrl1uiOdQKReH03QfqshUzVnF_fb3xp46muNtA3qI24h6-NtXuNxyV0UolhSGNx5mWUIvvDq5Mrpy_QAoQYo2mXNVFMuYXJeRA-WZFNHq3FCFzsicfNqoc3ZFexe5zCj9PN9JWlUgde7vjgRpKPmx9V_Z4ThPlqalQifh4fNLXRS69eKn5s1-BNFBGbGZmWnKYYFj7ES03sUVjZI76h5MCwQfnrewg6q4p0VR2zm9SuXvKSeAesqyxI84Iy2IWb-JCKXl2BWYULuK_wfwTe3_z-y7Vrgzo1AEdIGKAXOVdazs_eb9L9Vr0pDo0OherWwHwRSrdEVkr4KcsMt1EB2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 3
🇺🇸
استادیوم دالاس (AT&T Stadium):
🔴
ظرفیت: ۷۰,۱۲۲
🔴
ساخته شده در سال ۲۰۰۹
🔴
استادیوم تیم فوتبال آمریکایی Dallas Cowboys
🔴
سقف بازشو
🔴
صفحه‌نمایش‌های سه‌بعدی غول‌پیکر از بزرگ‌ترین صفحه‌نمایش‌های استادیوم‌ها
🔴
استادیومی با…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91291" target="_blank">📅 14:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91290">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC9baIl9ATl7AZZEbx-OsouxMEmsdJz4-4KjlURTQXlcw6apyMUI5H033PY2Z-QuwnD-IOWC65dOSx66b11Sj_66cjhxtHBKqfR-BhP_8cTACzAUanijYF3oU7KBAU9JEc94wd0Z8mXoqQnSQwwXUVjRwbhforHU7GJu51Yol_bCXCNXpItvSHFeheb30UX4upXXyQhAqcG_NYOeRknM4PM0OI5JNXNqTpi3x7SK4_jTd6aEiEFTPICGny5e-GqLJZZGI6KqLErRFs_GPKFGdGbN-6D7CEhxOr_vZ50EtZV-KGGEEEC13XjPa1Jrx_eFPIrQyruqiWwmZJe_HlQhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های جام‌جهانی؛ شماره 2
🇺🇸
ورزشگاه هیوستون
🔴
مکان: هیوستون، تگزاس
🔴
افتتاح: ۲۰۰۲
🔴
ظرفیت: تقریباً ۶۸ هزار
🔴
بسیار مناسب برای هوای گرم
🔴
اولین ورزشگاه NFL با سقف باز
🟣
خانه تیم Houston Texans فوتبال آمریکایی است.
✅
میزبان ۷ بازی در جام جهانی ۲۰۲۶…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91290" target="_blank">📅 14:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91289">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfRHxoirZXIahbYe28mEMRco1qVFzODMXyLdqiRSBJhqY8I9FraSnYjZ8Z7rt87o68Y8ghfv-QM7ThFPwqLtXF9ro4Qx3nGmZ8wgysEUheyvKsOKApw2X-rPno4aF8YhVuZqjLg2Bs9JRR8w0NoKOi_P6BLYc3i9o9mPCuwUVcNkrPocdx4YfHhAPM3fHf8_saex1fH8I9uALGQdwLm-Bss0rSxXt2-P1uyF9qKOJ_pyXf1onV5tfSQDdZACLlqab79W4g34Z1__8vpyNGVaplsQiFT9Pk1JM7ipogd6rox4XGK4hoCqbFdbvpAxNrRqu-Hbcd_MgwnN6XILzwSStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی ورزشگاه‌های جام‌جهانی؛ شماره 1
🇺🇸
ورزشگاه لس آنجلس (SoFi):
🔴
ظرفیت: ۶۹,۶۵۰   /  افتتاح: ۲۰۲۰
🔴
جدیدترین ورزشگاه‌های جهان
🔴
سقف شفاف
🔴
صفحه نمایش ۳۶۰ درجه بزرگ
✅
میزبان ۸ بازی در جام جهانی ۲۰۲۶ خواهد بود. ۵ بازی در مرحله گروهی + دو بازی در مرحله ۳۲…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91289" target="_blank">📅 14:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91288">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7J3MV-ZCG2QOQoQBrmhWX7tiuoI-Lv4b4BOT0I3sA8gB3WhNzjG1bhDc9naxyAL3GExakuOqAjXnNfpMebnPQkr7MTrQzV35heuuionUEBNDWexxjV5gkPIjkVqoe5qs4FUu_CUUKonACPKNFY2tf-XPA3k34Ye5yq322ZhRbnqGyI_KMufx6N2ToMMatMoMpnd6bEV9-aCuV_GaJchqEGWWVAhFBcHTm_Jwz_A5AYNwS3kHdYQ77ZRb1m79H8FcFCasn-EckfkAIE8fH6yMRDInOHC9oA5lnONh2gXUOYC8EabAGU4uJ1bGJYHd5ZewFX3iBFInlmUCYSu3tEBIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی ورزشگاه‌های جام‌جهانی؛ شماره 1
🇺🇸
ورزشگاه لس آنجلس (SoFi):
🔴
ظرفیت: ۶۹,۶۵۰   /  افتتاح: ۲۰۲۰
🔴
جدیدترین ورزشگاه‌های جهان
🔴
سقف شفاف
🔴
صفحه نمایش ۳۶۰ درجه بزرگ
✅
میزبان ۸ بازی در جام جهانی ۲۰۲۶ خواهد بود.
۵ بازی در مرحله گروهی + دو بازی در مرحله ۳۲ تیمی + یک بازی در مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91288" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91287">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Vuixj07J0skaWGNHY0eRO106f2Ddp5aZsV4F4zrr9_4lRyqAUXSwB2ltgphXAiv70snJOqMVYoEUI4_7633B6YOzzhL652B6A-jiSk4RdA6IUdFjoTPS8m8s0gG_XrvBcTbny2ReKG9JA4ftYKX4grKjm6G2R56pqNcY9Gl6VOwG3vTd4SSxZOomHONFm_rvgiz_my10KXQIbFMa61Rl9ACd1tYI35z223ORYuJuZMlvxgoSLRIMNP5l2DwlBoQfxpsuJFwnpSw-rxbvvrhBLgcB1GXq15Qaxowd3x2kFFVaJTCz07vp44rIUZEeUHS-PMUih9uCNJ9Lvzkc7-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤩
#فووووووری
؛ رسانه‌گل: الوارز پیشنهاد ارسنال رو رد کرده و اعلام کرده نمیخواد به لندن بره و دوست نداره در تیم رقیب منچسترسیتی بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91287" target="_blank">📅 14:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91286">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIa7CXYMTyQPNs_D7rRncmfTUEKbc9se8d0hYgmvm7p_5J_4UynKAE5_rI2KXsA5vtorvzydTtnqBVJ-KtNrNICtZIuZsHbgtHne3tIlL5zoak6ybZaDwRjnRfpFudJDtdhJnFJnUpeKAwWnEohScYIQ7prHf7XpkPHJ_QdjNQnAz-OjYa2fqkESI49UhQ7vmZnzR-U-xLWDIk2OUGZsfNDzHUOEBDIUxEUow0thsfyJPZkWCLssaMZL_q5PJ11yX_XfK_Clg7siHzn4-T8JqtJJFdP7g1FSM8PKWsObj0uxBjJnV9M_F6f5PMlf2NnbaHbgSCktHWbjL3DVumQ3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ براساس شمارش اولیه انتخابات رئال، پرز بار دیگر برنده شد
- فلورنتينو پرز 65%
- ریکلمه 35%
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91286" target="_blank">📅 14:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91285">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdeda036cd.mp4?token=uYTkc4dtfG3p-_5oWVqNF8IIzku7re0-SUTt2PO5z7-9HV9HLstgsgaaCFo5DPONka5tspbdEbo0iYSL6XCcLOkpLrZQh6tIKYx9VQiZzlgs2tq4Oyt4Y0CtZYtFM_H5EkhHi_l55DLnl4WukQ2oWf1ZhoHy41RmnuKFkpbTK-iIYnan1zZt07AM8fMuRKWdq2kx3LNGnozCoQQ3nfIJ_PeW0Wn7Fb7OtbLtsKUhds8ZUSysMvQgkT8Y0LQ_yc4eUwvqiByQnmxU6DewN4g4EgGbwlDuGka2ZXsKldaXPQ2S71TmwvRxZb8lP4SxMyQ-Jz9nCpmxo_V7TXBrI90c0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdeda036cd.mp4?token=uYTkc4dtfG3p-_5oWVqNF8IIzku7re0-SUTt2PO5z7-9HV9HLstgsgaaCFo5DPONka5tspbdEbo0iYSL6XCcLOkpLrZQh6tIKYx9VQiZzlgs2tq4Oyt4Y0CtZYtFM_H5EkhHi_l55DLnl4WukQ2oWf1ZhoHy41RmnuKFkpbTK-iIYnan1zZt07AM8fMuRKWdq2kx3LNGnozCoQQ3nfIJ_PeW0Wn7Fb7OtbLtsKUhds8ZUSysMvQgkT8Y0LQ_yc4eUwvqiByQnmxU6DewN4g4EgGbwlDuGka2ZXsKldaXPQ2S71TmwvRxZb8lP4SxMyQ-Jz9nCpmxo_V7TXBrI90c0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
🐸
قر دادنای شیدا مقصودلو زید مورایس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91285" target="_blank">📅 14:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91284">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f03b77a9.mp4?token=Spo4T-GCMRqS0ebiiw6Lhc1eJpgJ9BKJ2llKo4xDSuiYSeW3de7bLRmBcOIW-nh70QB74bHOM6o_aivH7cL2GyOaOU71cg2sZ8epXf3EIHI-OxS2RZy43PQXCS_jGbEKHMUR4qRqoY9gQR25EPtgIxSE11AKisVJuDyQ5JbFJ7MXytezLmLp8rdpFCQN1Eib624iG_OrgjGUizefhfy5QntKbS6jY8wjhWfb9m_Ijk3NXyPof2TN-mGL4qkZEsn2DjMEygGNKiqGtIXAW6Y_iY3Xkvj6lhDfpgc33io0uwpsJyF07b70RQsco2TJCtHn0AhlFw6nwzU9fBs-kfO7WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f03b77a9.mp4?token=Spo4T-GCMRqS0ebiiw6Lhc1eJpgJ9BKJ2llKo4xDSuiYSeW3de7bLRmBcOIW-nh70QB74bHOM6o_aivH7cL2GyOaOU71cg2sZ8epXf3EIHI-OxS2RZy43PQXCS_jGbEKHMUR4qRqoY9gQR25EPtgIxSE11AKisVJuDyQ5JbFJ7MXytezLmLp8rdpFCQN1Eib624iG_OrgjGUizefhfy5QntKbS6jY8wjhWfb9m_Ijk3NXyPof2TN-mGL4qkZEsn2DjMEygGNKiqGtIXAW6Y_iY3Xkvj6lhDfpgc33io0uwpsJyF07b70RQsco2TJCtHn0AhlFw6nwzU9fBs-kfO7WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن مسی ماشالااااا چه بدنی ساخته
💪
💪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91284" target="_blank">📅 14:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91283">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a8cca451.mp4?token=WubxATBxtX2FhUcpDCa1i1XhJBvj_G1YNpoG9vfjvDp8ofgs0W_K1KLiAMBr50TNNUIIIk2sfdN2tjcs70scN5aOs9VBTVWu9Fp-n4JNBp9gjqSuL0XmnsMkIuLMflQ_khZo7mkW3FplKIcR-ZgNUHMqglNjxJjoaDwzf3NCI3L1C0y9IG9RCpHkdqW7dlnfJpwdZm_kVGkZRmyP6a8dgFdbsDIqQKi4GMD903JmfQKZQtSvehG63Is9agDWmPfAZ0xxKcSNmnoU-6Y6T3srTuioBSaKvIdfiRMSgJF_TNVS21gLHIsliqmdgYyUpvUKAXKgOWrLmdUvSKfR_FlJMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a8cca451.mp4?token=WubxATBxtX2FhUcpDCa1i1XhJBvj_G1YNpoG9vfjvDp8ofgs0W_K1KLiAMBr50TNNUIIIk2sfdN2tjcs70scN5aOs9VBTVWu9Fp-n4JNBp9gjqSuL0XmnsMkIuLMflQ_khZo7mkW3FplKIcR-ZgNUHMqglNjxJjoaDwzf3NCI3L1C0y9IG9RCpHkdqW7dlnfJpwdZm_kVGkZRmyP6a8dgFdbsDIqQKi4GMD903JmfQKZQtSvehG63Is9agDWmPfAZ0xxKcSNmnoU-6Y6T3srTuioBSaKvIdfiRMSgJF_TNVS21gLHIsliqmdgYyUpvUKAXKgOWrLmdUvSKfR_FlJMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
بانوی جذاب آدریانا اولیوارز مکزیکی روند زن برزیلی رو تکرار کرد و بدن خودش رو پر از برچسبای بازیکنا کرد و از دختران سراسر جهان خواست تا قبل از جام جهانی ۲۰۲۶ به این ترند بپیوندن.
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91283" target="_blank">📅 14:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91282">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34842d0797.mp4?token=NtLvrNlg5YCGgOQCwD1FhRmBJK1pAgqrkmm89OTS254v1-0MJgfM7Yl16fKTiyiDp8CBE2XZDNnYTK2N_5x8dHuVGdDSioXi5zCN49Rm5Nn_HSbE0ylwcHEzvRG1xIedYBN4onmfbCWacISDyvzyL8dN4Z8LrgVNB0Rq7h1sn8Oaa-bfBJSYtiGdiaqyPaAYLynmYiWOwcQlonB2i0WGUfvqDHVxpi08BOJaRlkgbX4yXMFdCgKzs4hUmSdUOxgmDQND3lua5ulcGL0ROcpULwAHfmsEpDAqj3KvYmcWmOJw9IwRe0BC27vssuHxpKVjSmgkMJnmcORtEjfTYWj6WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34842d0797.mp4?token=NtLvrNlg5YCGgOQCwD1FhRmBJK1pAgqrkmm89OTS254v1-0MJgfM7Yl16fKTiyiDp8CBE2XZDNnYTK2N_5x8dHuVGdDSioXi5zCN49Rm5Nn_HSbE0ylwcHEzvRG1xIedYBN4onmfbCWacISDyvzyL8dN4Z8LrgVNB0Rq7h1sn8Oaa-bfBJSYtiGdiaqyPaAYLynmYiWOwcQlonB2i0WGUfvqDHVxpi08BOJaRlkgbX4yXMFdCgKzs4hUmSdUOxgmDQND3lua5ulcGL0ROcpULwAHfmsEpDAqj3KvYmcWmOJw9IwRe0BC27vssuHxpKVjSmgkMJnmcORtEjfTYWj6WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
گاوی تو تمرینات اسپانیا اینجوری رو پای رودری تکل زد که نزدیک بود مصدوم بشه و کلش کیری شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91282" target="_blank">📅 13:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91280">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_duVhaZv7-2G3XkWSzY93Ya5PKeMk1DSk4VLcWFayvO_6ToATtQJcEewrtxDA6bu1X6TrxEozoTclwoqkCzSa2MigLZKyK85gsSv28nYSMvggiFhHtCk7RgUU1v26RqS3eqCwLJMypXCosrR5eBkfCyEMCWPSu_4vCtP-oDcQC588N7OoMmuHhGFGXSE7JBfgALiAp2vG7qDZN3VvoiOMUTu11f2bWTh7b5rZGV-cwum4m81-ZUmqPz58GZFvMwF3CLb2KV16EZPyWKwm0yfPhIPyC9hCKPxn-ah_Xbc4OQiDmPY3rcJ3SujU4saBcfBevqID4nQxgY6W6F_2fyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRAPlIA81URX-VwwRkZhPe8k3GhqQMPXIe2uiGYEu-rBHVYxH0jkyNTt7xUVkqgE-29DVaVKFUOA0Rkob9CnxRNY-7q0yPQyzWJG7sZioMD_nXTOd_C7RN2cHWcxUn4GF3U4ePJ1lor6CwQgV2VoXDg1HNEoO4NMSxG4vJLM_E1E2wKvyTdi8FO6dY4n35di8xN8k16biQUCu2Z3rt25O1Xf2qqSFGGRMtH7xYeo8W39cXeLNtngFrIrUCwzsRGN7R4-7PxZiopJmBvjcTH2AFS268GrTBcVl0wEHIqjb9OEI6luN_VHdWKKI5P-zExt95V5KjYola_3frm6J6t7pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل مو نیمار برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91280" target="_blank">📅 13:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91277">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onYxRtm1JlXgTy6sC9-lCTdjQPE_fY9PDt0HqIgFZm_AeXgfrTMpX1xfWtPjdZ_s6kn58zXKG0OvoWDr8ttXNGmJqQGrU-V5Tv6ovXOmkbUAwwz5vF3h1QW1UxcTFi3dZPEpdAl0uhDKbIqREiKvHK-xpUm2y6U1V-Fssih38R8T1MhEoaD6fJJRHxfsrh1akJguRG9ny1XNUfZ6VfpnrQkQNdm8M7K2tsjGJxb39aRawgO_Av0DRSeeSheEM77WsskQ0UkOcwqqvhXJ_HhQ3jbKD1wPK8l1Dl7IdPnvdcLR00HZfEVYGuqdD93hmTI1ihJVBPg-_bwowOa3C3ytzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfjyFCKaB_Uq29L9FF9-WhcVuKLHxz3dMVs6jMaS26xzdnNbXtayCWZY8m32602rPybWLvtFXMOcmdOxkDpphWXBXE1dSknkrylpW4SqRfgY4kHT7JKMYZsItlOJm3sNzTc5OOI2r-M_LkOBSruVCzUqhO47Y4gXOdflwjwKee3CZfvlEcrMUcHhDycR3HllUWv4doJXL600u5Nd5U3sJYi4Ed-wuO25c4Pz9tdHeqXskxm8va0mGoHmf74BkwdIjGfZNG1KUSm4WLU4nG4oJSDFbc6r9aN-O6YR2M4G71s-ozleXEH6i5r9-dMGyE_nA9tgbAzmGBMu_VsvE51oKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tp_mDHxZ31Spi2GjybNfI9Htx9xahsF1LwHBfOSmg3tCQGzf6rFY1cXsNAd2IeOnuDlAGOFIfbxbarI09q4Fqn3c-DPnqk-IA5FF_LZ18x254wBdcYpqBUx-65J-v8XpvHVUVQJRDs5LrPGSrA6SSkKRjVhs_uG0s27HmVmNKwM1VFYl3y7lfpgAXXRLmiy75bWbPeioNe-aP0xPttSTDfFsxgT2zA8uOI-ejYroNDZCLUNzSDLf0OyoUglVlOcaoYhIEHyWvjredxtWizDVtIveAK981HmX-8MUCwCXXFfxXOcHXWB2nLwg4q-iz7dlWejQxqEf8zY5fJlYwnQ1Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور پرز و ریکلمه در انتخاب ریاست باشگاه رئال مادرید.
کی رای میاره؟
❤️
فلورنتینو پرز
🔥
انریکه ریکلمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91277" target="_blank">📅 13:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91276">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ffdac381.mp4?token=e9x6iGT-1Lyu84BQdvZbq3Ew-Xuoq6PwA81qaG879PNeBQPmcy5foAt7LYZVUIqCCwOxZw2evDjOPtOR4gpa3H_39P3juMhydJ65mAyFwupH92PVDHyNMn8EeEn_-rN1OmsO7ztQyXSIBX8AoBRYzZz3-ehWMztRd8z876jYR814bj45hSXGIwtd4DpCILmacSP1tt68qXB-1lhq5nV14fOSe1G-D2FzKSD5hJw9aZKelCacn5-iTxVKj3pxYB_s0AkUClhjgDER8brbNk4D1jTmPWVh1ODjSF64WcLxJAEU7OdRU_ATqnpc1UG6gY592z5PFBwtxjHJTm-nHCHBqTxZs3xHwK1qHzjNwWiPUmj5q65Pqcfx0O2C0V17Ywo39n2zQSWU9dgpjAO5-PNH0PxRrLJ34mYa5UfD6j-6IlY4DAKbs97LBx0nrezUtqLcpFvxGoeCyqBEdo9OfWLG3OhugnEKbpxF-IIp6rR1dXSH2Cld8oqKXKaId0svwIyo4RNeKtOsewEXaOPG0U5PF-tEyT-o-D8SJHzar9akHNFK2hKogInxc74f7irAPhuB9D94aNvqfIVBj0SI0cKaY8baIiTwgIyfmg3VxcuVm40gICOrDHmCI_kQ0QrKHmmE4qJmWG9AnllOOIfcAOa0tQLwHD4C3udxmISXp1gAT84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ffdac381.mp4?token=e9x6iGT-1Lyu84BQdvZbq3Ew-Xuoq6PwA81qaG879PNeBQPmcy5foAt7LYZVUIqCCwOxZw2evDjOPtOR4gpa3H_39P3juMhydJ65mAyFwupH92PVDHyNMn8EeEn_-rN1OmsO7ztQyXSIBX8AoBRYzZz3-ehWMztRd8z876jYR814bj45hSXGIwtd4DpCILmacSP1tt68qXB-1lhq5nV14fOSe1G-D2FzKSD5hJw9aZKelCacn5-iTxVKj3pxYB_s0AkUClhjgDER8brbNk4D1jTmPWVh1ODjSF64WcLxJAEU7OdRU_ATqnpc1UG6gY592z5PFBwtxjHJTm-nHCHBqTxZs3xHwK1qHzjNwWiPUmj5q65Pqcfx0O2C0V17Ywo39n2zQSWU9dgpjAO5-PNH0PxRrLJ34mYa5UfD6j-6IlY4DAKbs97LBx0nrezUtqLcpFvxGoeCyqBEdo9OfWLG3OhugnEKbpxF-IIp6rR1dXSH2Cld8oqKXKaId0svwIyo4RNeKtOsewEXaOPG0U5PF-tEyT-o-D8SJHzar9akHNFK2hKogInxc74f7irAPhuB9D94aNvqfIVBj0SI0cKaY8baIiTwgIyfmg3VxcuVm40gICOrDHmCI_kQ0QrKHmmE4qJmWG9AnllOOIfcAOa0tQLwHD4C3udxmISXp1gAT84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریاچه‌ارومیه که حسابی جون گرفته، این روزها میزبان پرندگانی هست که چند سالی از این مکان مهم مهاجرت کرده بودن
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91276" target="_blank">📅 13:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91275">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIew5V6CLIzoKRuFUg96npKy1gxpA9RYber9w_-8l_aoTJqK7WD_wlVnr8dlrNichrc1xvwB8ZXhM4bh4tI9YdziJ27ITKHd5qe4Rtphb0DEI1zF6NVjPZU5-4JxMTn0ZyiCv317vGoLUpJ2IvTwzcAXLGT9DRDPpNJkcfNIXhgZWCoSZpB2yooK3HdAVDwhi9z-G20oANDL105G1Ky4Qa6oJzmTAjm7KnwtGY1IprOomjCJ41-WseLkMj2SYvg_D4faFfz9VA5WGH9z-1HsbjpYfdlh0cRUw2B_cuBz7-9XoO7E-A0m8FtLuTvUH4s57NDVFgaRHrKNyChItb_1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ماهشه امیرخان؟
🫃🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91275" target="_blank">📅 13:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91274">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpZFZdM8ZmyNqYe6D5kXOiGUrcu0WzfCzy8aH3kh1ThxAEchG23LxuTvaVz0_fEnbEwpcO4Ye1Ph2GKT0BUaq-438a3l5f7gnVAgoNESR9YJvjPOZ2rm3sqP7dpky4vK67eLZ_Hug0VN8vDUzAw5iQHapFYABvJ1f76R1CSj8gGPEfax2EtRPgpSmcU1BAV8oPPxzkh7ZjNKwvmksUKezgQwb0U3NnVP-uQfssdWPUNKHbPSBP7D_DOWnvRO9xMQI00tSdR8HYgZEOr4v_skY77U-2Ivftf2YJfITiwdI5Y7XY7_jjzR_3y0Drju9P0haFtRKBrVRkKvaMVLQLXXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولو شیرا:
ساوینیو و تاتنهام برای قراردادی تا سال ۲۰۳۱ به توافق اولیه رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91274" target="_blank">📅 12:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91273">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPDe7ttricRMdWHdtug1rpOrUyQSQfsIbBxX8xT6aZXFVkL4H-Iti0qWyvtH9654l_XlurcKjvhagZvjc-JoDKbaUvTr1ZjOZPG-0vN3TnwlZ9RCDh9l0wBaFnKvyRPtKir_33CZe_KIk4PpwzpdasW8JLkdTB0cimYkx_ckGi9G3b_hAhes5spvFPGGbJExVHM2Ky6og9awi-QRYsvfx_GXbMQi8RZiGRZjx3h8aEmQM3W7DyIjuNdCLQOkFLpD3E3DZnMqDR50Cb4jL5cQPuDLmi-gakI8dfD8B9u0dAXokKcL5JJ6nyot-Pfp7Zjt9jTQJSNPxrlUBfYne0jBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز جام جهانی شروع نشده دارن شاهکار خلق میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91273" target="_blank">📅 12:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91272">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b9ee999ec.mp4?token=TO3-sm8xB3pQiIN6ba6jBdqgB8AmB7hrm31_gMwhn7Ub7wuj3bVHzp3x5FE4erK7tlXCPH0y0_oHzUzUywklXHkSZoMuWA6zy2FRZhX3_umwbAlE0gFUJFIlsiSbU2RNuneMsv_4oa7FHIB-lgJHFVwAOor7x_O1ZEri3Ie6EolzXED-8bHi4G8UOMXYxYkV9qzOD88xSJzQe2IDJUh9v2wEuy-k9Plh_ObbJvMeEnNeRocrJZPuQOrEXNOP27_3OK9SyS7byM0ywFf0Nlki9XeNkROwpI9b9OAsxN73W5WeRzp9d3-ucHR5cpGQUWPc13KyFczaAY-xY9_LDRdSkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b9ee999ec.mp4?token=TO3-sm8xB3pQiIN6ba6jBdqgB8AmB7hrm31_gMwhn7Ub7wuj3bVHzp3x5FE4erK7tlXCPH0y0_oHzUzUywklXHkSZoMuWA6zy2FRZhX3_umwbAlE0gFUJFIlsiSbU2RNuneMsv_4oa7FHIB-lgJHFVwAOor7x_O1ZEri3Ie6EolzXED-8bHi4G8UOMXYxYkV9qzOD88xSJzQe2IDJUh9v2wEuy-k9Plh_ObbJvMeEnNeRocrJZPuQOrEXNOP27_3OK9SyS7byM0ywFf0Nlki9XeNkROwpI9b9OAsxN73W5WeRzp9d3-ucHR5cpGQUWPc13KyFczaAY-xY9_LDRdSkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گروه E جام‌جهانی فوتبال
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91272" target="_blank">📅 12:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91271">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">😂
جمهوری اسلامی پاکستان دسترسی به اینترنت را بدلیل اعتراضات در کشورش قطع کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91271" target="_blank">📅 12:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91269">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIGxNhVTZqVSJNK3TeSEJgx-JWtjzCFGFv4qbygyOr77oBtUIzxWKClQ8ekQtAqy2NPlbBmZUz4_LCbFoSQuvjWMQ6_pec4-65Rjad_IEUljXaFgr6mMmRrCW41U-zWdlIb41KvG2v7gsB9jkKj0H3kfo488TBgJCfzE3WBNYFAvYRMfpufQBvmgU3byrTEDoH-oJ252eP2rLwFV-FntvtvB6rDPcgF4PkR3Qx9aTRFsMGqT0gExS9V2fIammWC1a6vx3kWHm55yZkZoAUNKmjWWL-YkySMlSFNFYPE4i0FkK6fG6Pe8EmeIlU1mH4RslbCLWdgBMJhQq5fmbC6ucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
‼️
🇪🇸
هفت‌سال پیش در چنین‌روزی ادن هازارد با رقم ۱۰۰ میلیون یورو به عنوان جانشین رونالدو به رئال‌مادرید اومد و‌ در ۷۶ بازی با ثبت ۷ گل این تیم‌رو‌ ترک کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91269" target="_blank">📅 12:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91268">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1881201.mp4?token=v-hubd2GBf5LyrpImbveqNT_JS2BKzS6YYO9LZXA8ZcL_FB1kaV3PfCq9Y3ArroycTIRSyXAmUTchHVoLMZodpclrP-Twk9ZZKui_tYiUVB0GkLPSaAdOFXqEbbt3L7PuTqYDUXTyguaW7JByQWLZrHtO0UqCkHPdiFLMdFiJ6s5Yy4ZwX9MxI2Zk30QPlbFuDROgT9Q_kjH1MVtG4gIURBSYeCrWdE7w-wkPBBoV-YRcFEQ5JLcqZiZ5gfiQdXD6GMXk--HG7jsmF-inHXW6ZLYPRkMChR30xHnP78hLRDegXlHYfMJkKVau4r8JLnXYVVclrP4z0iqRfDI8br2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1881201.mp4?token=v-hubd2GBf5LyrpImbveqNT_JS2BKzS6YYO9LZXA8ZcL_FB1kaV3PfCq9Y3ArroycTIRSyXAmUTchHVoLMZodpclrP-Twk9ZZKui_tYiUVB0GkLPSaAdOFXqEbbt3L7PuTqYDUXTyguaW7JByQWLZrHtO0UqCkHPdiFLMdFiJ6s5Yy4ZwX9MxI2Zk30QPlbFuDROgT9Q_kjH1MVtG4gIURBSYeCrWdE7w-wkPBBoV-YRcFEQ5JLcqZiZ5gfiQdXD6GMXk--HG7jsmF-inHXW6ZLYPRkMChR30xHnP78hLRDegXlHYfMJkKVau4r8JLnXYVVclrP4z0iqRfDI8br2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باباها جام جهانی امسال ساعت ۳ صبح:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91268" target="_blank">📅 12:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91267">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2e6f956c.mp4?token=QzGyQtROXzZpFW9aEPhalJXN7eT0R_njiwt-2GvyT0wOCrxEPLCDrA_EaTDEXgSTkVEukOoaAKSndqqzVuPF_KoIvow5I5Cvrcd0TKStsWHAstZ0dzsxIurUimr_TcLA2jwLPJp55ILQ-zZKdFQLQnr7zxc1mPJEAlWjxw4Y76tycG9X9OQJlY6xggdZ3uFvFUvlAlFefmY3QXLS99xN-vYk15CAGw08TT0bMMy13__x8GqG43l9CCxSjx-XRgwTxlGKpndh6UjfuwvwqEeSCDynSiYpAmXrRSQtnVUKJj4p__C6A2xU3k2Uvef_w1-2EY_rK9Ee9AiEA4O0s7WFFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2e6f956c.mp4?token=QzGyQtROXzZpFW9aEPhalJXN7eT0R_njiwt-2GvyT0wOCrxEPLCDrA_EaTDEXgSTkVEukOoaAKSndqqzVuPF_KoIvow5I5Cvrcd0TKStsWHAstZ0dzsxIurUimr_TcLA2jwLPJp55ILQ-zZKdFQLQnr7zxc1mPJEAlWjxw4Y76tycG9X9OQJlY6xggdZ3uFvFUvlAlFefmY3QXLS99xN-vYk15CAGw08TT0bMMy13__x8GqG43l9CCxSjx-XRgwTxlGKpndh6UjfuwvwqEeSCDynSiYpAmXrRSQtnVUKJj4p__C6A2xU3k2Uvef_w1-2EY_rK9Ee9AiEA4O0s7WFFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
رأی دادن فلورنتینو پرز در انتخابات ریاست باشگاه رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91267" target="_blank">📅 12:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91266">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDWiRALm1TAbN5bekzyRqUHvacIePwSmOLM4iQzuk1EE20q-6LhxCrWQJpPOE4DcpAZa-0E3c7aU0BizwuPa1WXikhMhoePkIihRyxgcmcTLSsoRedNPm89fQLdkJ3Z3HvnIBZKgkHYWm0p3YYOg_dj1-7sE1K_XDnEjYE_N1kxBFzrsefGO-EK_moB66_VVd-rSPNs-4luLbv1_F89Qo6WakazGbS2N1lPIw2k6bGf1nXNo1SG77Co9CNjDADPjpouX8E0ycP_n3xsvJFx9GuufUqDyERQC5sKZn_R3cIjNvJnicPAert9diCtBw9xYZds7QNqTxBlgHFPdis2DSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
«سال 2003 پِرِز به خاطر سیا‌ه‌پوست بودن رونالدینیو از قرارداد با او خودداری کرد»
+ بازیکنان رئال مادرید در فصل آینده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/91266" target="_blank">📅 12:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91265">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6904cff7.mp4?token=VtEByax7j-CQu25aEfj30uK36aWDQ4h1mZSh510axRHre_JD_mjr-VoeqY8pzAIf-myBLWwpI1oZg9dBR_-Mry2jMkSLje1wGQjS1R9NMEFw2XnX9GCs1nTAj8QUfw4BVP0hGPmvhOzRHLfKr6y2rNanwuWw-QmNZJNaa5yoyMmVedl0kcyQMkUF-YdMcA1NFouvkqh_u6zqrDmE-wy7AL-tdTVGDUrRmob-YgEmz88HJuFrxKArvCwC39fgfWNmhBn29CukJfP927UNuw7JO_xZGPkRwMiH6Lm2kEKaO6C7gTbhMv8SvsKaPtXg37BR-zfRNGAaCiSOHfGiQSwqZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6904cff7.mp4?token=VtEByax7j-CQu25aEfj30uK36aWDQ4h1mZSh510axRHre_JD_mjr-VoeqY8pzAIf-myBLWwpI1oZg9dBR_-Mry2jMkSLje1wGQjS1R9NMEFw2XnX9GCs1nTAj8QUfw4BVP0hGPmvhOzRHLfKr6y2rNanwuWw-QmNZJNaa5yoyMmVedl0kcyQMkUF-YdMcA1NFouvkqh_u6zqrDmE-wy7AL-tdTVGDUrRmob-YgEmz88HJuFrxKArvCwC39fgfWNmhBn29CukJfP927UNuw7JO_xZGPkRwMiH6Lm2kEKaO6C7gTbhMv8SvsKaPtXg37BR-zfRNGAaCiSOHfGiQSwqZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
پشت‌صحنه تصویربرداری جذاب از نروژی‌ها به سبک وایکینگ‌ها؛ ایده و زیبایی 10/10
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91265" target="_blank">📅 11:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91264">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4K8w_7A1rq-47WUrRIhf4abSM_f1mfdpgD5KsA0jPtvNqfsqUsieEMnSuhKloWweJ-59w62iQnzZycV7H-gjMxYR56Z2IF5vE6EUKwqPXgLaJz6od89c0VbrD8H5yEc2P7U2cajLRFWKPGzlltKH11Bnt6fBedT2FHiLB1cqqHYkS1-lHudTs6dcby5CwR_jNsakDqX6-SyB9loJkIyyniG-KsdhAT-8cfkfmcqlxlKInxqjVZ7REPuymSp0adJ2Dh-53Oc4HPWJin6Hr1TKiExPgOTUDKlD7TPBME_lZ7T12tvP0B97uJJ8MCm7DP0Z6CbFeb6MA2z4cH7jlQltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ قرارداد جرمی‌دوکو پس از جام‌جهانی با سیتیزن‌ها تا ۲۰۳۱ تمدید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91264" target="_blank">📅 11:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91263">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9lrwmYNm0_qbST-I02lfIU9loyBPF3Et84K0YVvvr7tTLzTqvjourxAuwPU6WPnTWNswk3tTpzgsHpZX52_ibCZgZmd3jpw6Lo3RFmk6wdNocpWoq4SrfFTuOaGDYEisjqhQnmZb1osSsnA1koydpoldjJufhbdeOQOywlgk4WG0nCBC7ag3VCq7COuCqsy2xudmSou7XPZPHW_swHtIe_ZadL9R2QIbAqNKUqhKuEKtrrp1sLswuH6eZemm4ZZRMr32tKa_8kjYMC6aYZRxouYkjNoiOV4iLH0joH2lc3czP8PoqJgO1sp8CuYZHH-LD0m53KGwbZo-YL9al85dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Milan 2009
🙂‍↔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91263" target="_blank">📅 11:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
❌
امیر تتلو واسه ماه محرم درخواست مرخصی داده که بیاد مداحی‌ کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91262" target="_blank">📅 11:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91259">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goa2rjRrhyVWEjek0vsDiFstBeN2BByJDTJc6oEyv4icpbvDoeueMvRidKGG-rDNck8TvDhk2_T0IA9RmFOUD56MPZZDyxvF8tpwMrgKAICxOrMIFlxfFLCHrURslDhiWoq8J_TW9r3L4bZB5irtnANa2oWNwJL5hTlqnV6am_-ml0HjyTl-2fkg6pPVwh5CbwaezQwRR6SaZjL4vhD1nBHdm4Wiv0AdDDu4ZpBKhtlGApsoU-zdebpTnNSW9v4928uuwkshURcxk2kzHo4Ib40U5kS3IAPiw2QE6-VJFNHbwXsX8AFRo2K3qzeKodAY2hAMNnwPP675nPiJzAuyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhTqvPoFjoLwkbxq7SasmuUzuAtF6epoqtPRl8s-cnacKE-HN82aQG7_Q9EmRWQoSuxDE5Fi9ujeWpMbuzUoKdTK_6ocAcuLMtnLKg5KQO5yZUkqI8pMeBkG-SHQKNz36aTwYUI1uFK1YmlSVZiPBnGKXgPg-4bHvLxrLn3Phw_SEBUUkmGwdkrkBBwPP5yh3qsdPBiu2Ci2sG4bOmPXY_-xFpuPJVk1wKgP5tyNlALw2GPkrZoDwRFW1EeIB4ErZlNKp60pldiCOupdxboT2LE5sskv0GHjfWRe6dik9kbX9FasKYSDWgu3txX1f7PZexrk3E-Phj3e0v1JRf5MiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVIa2jRzGxE2L0PDsBy-4-oCCXchm6HSoIof73kW4Xh3Q8q7jR4FRgyyv4b8l47xU6M1PstJxPW2VWLRY9AJ36eb6toslrUWCpWWpMO5n6iz93azmRsgWEf2peOgH3oiVHAzQJoj2mgIld1bko4jWF4Jyzp-7dYw5CGzA72cg5kXw-UoFfMptKlLMP2Yp6BMhBFTm28UptfDrJjHRIQieRpKGWggn3pKkvwf6Sn0glTZ9R-kLywHXHr4N5nFlmDY_QAlp3aT17EEp6tZnbk5EprmO8vKLUdiMSg0a9DEJk8urfbYWlLbEk7E7pFn9gI2EbVF_OhnalXPZaBeFdf-Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسم ازدواج عمر مرموش ستاره سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91259" target="_blank">📅 11:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91258">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b13497284.mp4?token=ttupcLOzAcN9wiJSHtK8wY67HZQRgVHyav2ePqHwnomeO5HCEj_3vu_It5c0WYnGbDZv5cYPSz1v-l4Zk9IcOSBIw-z6SDM6c_483Ld_6IH57mOxPc9lCf8e7k4dDzr2VbZnvFGFVJrCpojUx-CBofnXBnS4gJRPt2j9-rqF7eEdUE5pVbWEQZbp-NxFJRcoZ0LeSJHIl6ULfOBpQtQObMJ79S7JZixcBkgE2zjvViCbMiwUWVfUI6xrKbNp3LWZsMGdOWsNLgMf_3HEgNbCHf4cK6jdRh4Ax8YLkcLGnGyyKt7JeKFLCnYnjZjcawyOfl8d5ADzNqHEagSO9pUONoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b13497284.mp4?token=ttupcLOzAcN9wiJSHtK8wY67HZQRgVHyav2ePqHwnomeO5HCEj_3vu_It5c0WYnGbDZv5cYPSz1v-l4Zk9IcOSBIw-z6SDM6c_483Ld_6IH57mOxPc9lCf8e7k4dDzr2VbZnvFGFVJrCpojUx-CBofnXBnS4gJRPt2j9-rqF7eEdUE5pVbWEQZbp-NxFJRcoZ0LeSJHIl6ULfOBpQtQObMJ79S7JZixcBkgE2zjvViCbMiwUWVfUI6xrKbNp3LWZsMGdOWsNLgMf_3HEgNbCHf4cK6jdRh4Ax8YLkcLGnGyyKt7JeKFLCnYnjZjcawyOfl8d5ADzNqHEagSO9pUONoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
امی‌مارتینز دیشب حوصلش نشد بره رو نیمکت آرژانتین و شروع کرد به عکاسی از بازیکنای تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91258" target="_blank">📅 10:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91257">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea9b401d.mp4?token=RYjfAHB0tCSc0LwMT92Wfo2gGSgP-CBpPv8zATz9QmO-Cr9Fc3SqAa-KT2P-F-f2-06HUVNQqha1lM9H7Y6WPNj0D1rK6bzOPHnrmYvR-bhNs-PDzuSkN8_mzC_tt4TFz151Vh_tdHw7-1yIP1owzA2G_Y4qyHqFiuC9tcyxGaPN6GcrZ5WTpsC0TUQrnx4b_SR3YE3DW_AmwiEbS-2Nhk8OWhO3Y14a48TdM_lPGnqs_K76ykjmHwDChpvmcscg_Is-6h8aEkAoFBZtIJpZNCourbCS2l-bPyYi1GhdWonFDPoDtHIwDsygB9KbaEXkDEbiwBmukvXJ2s-fmmZflg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea9b401d.mp4?token=RYjfAHB0tCSc0LwMT92Wfo2gGSgP-CBpPv8zATz9QmO-Cr9Fc3SqAa-KT2P-F-f2-06HUVNQqha1lM9H7Y6WPNj0D1rK6bzOPHnrmYvR-bhNs-PDzuSkN8_mzC_tt4TFz151Vh_tdHw7-1yIP1owzA2G_Y4qyHqFiuC9tcyxGaPN6GcrZ5WTpsC0TUQrnx4b_SR3YE3DW_AmwiEbS-2Nhk8OWhO3Y14a48TdM_lPGnqs_K76ykjmHwDChpvmcscg_Is-6h8aEkAoFBZtIJpZNCourbCS2l-bPyYi1GhdWonFDPoDtHIwDsygB9KbaEXkDEbiwBmukvXJ2s-fmmZflg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">30 ثانیه از اولین بازی لوکا مودریچ در جام جهانی
و حالا اون آخرین جام جهانیش رو به عنوان اسطوره کرواسی و رئال مادرید تجریه میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91257" target="_blank">📅 10:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91256">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a80a11077.mp4?token=uHl0Yc21a0rqFq4Ecvj4V0pbA56zZZX_JhAEfTKp-95KhK49bfSpKnsEc_VcsCu8DqXdqv2c_r-vzjQChjTO14_tDME6TyHke8QHfBMG1juC5qJ8pu9oiFc41N_w0GJIkqBvIj2NW26YX4KVyIpjFeWQ1e2G3LGUU_CUMVAiibZGhHC53jG7JlfiDCjD6vh1E83an6aO8Q5SyFnBsFNL64iDOr49xGyLHly_MhxMxs-e2M4ApvUmAVGSbZ_vLYyVxLWnWnz9wtzfAmT5fekk46Vk8BdnUSZWeJ17rD5j3jF1B_pCdex3akITTtawj5TUIB9QeTHUX4lTWhxH7OyiWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a80a11077.mp4?token=uHl0Yc21a0rqFq4Ecvj4V0pbA56zZZX_JhAEfTKp-95KhK49bfSpKnsEc_VcsCu8DqXdqv2c_r-vzjQChjTO14_tDME6TyHke8QHfBMG1juC5qJ8pu9oiFc41N_w0GJIkqBvIj2NW26YX4KVyIpjFeWQ1e2G3LGUU_CUMVAiibZGhHC53jG7JlfiDCjD6vh1E83an6aO8Q5SyFnBsFNL64iDOr49xGyLHly_MhxMxs-e2M4ApvUmAVGSbZ_vLYyVxLWnWnz9wtzfAmT5fekk46Vk8BdnUSZWeJ17rD5j3jF1B_pCdex3akITTtawj5TUIB9QeTHUX4lTWhxH7OyiWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی تاج: اصلاً برای ویزا درخواست نداده بودم که آمریکا بخواهد به من ویزا بدهد یا ندهد؛ خودم هم کلاً نمی‌خواستم به آنجا بروم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91256" target="_blank">📅 10:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91255">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇲🇽
صدها نفر روز شنبه ۱۶ خرداد در بلوار «پاسئو د لا رفورما» در مکزیکوسیتی گرد هم آمدند تا رکورد جهانی بزرگ‌ترین «موج مکزیکی» را ثبت کنند. این رویداد به مناسبت چهلمین سالگرد مشهور شدن این حرکت در جام جهانی ۱۹۸۶ برگزار شد، اما گینس هنوز شکسته شدن این رکورد را تایید نکرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91255" target="_blank">📅 10:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91254">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
😡
هواشناسی: امسال سال خیلی گرمتری نسبت به پارسال هست و به طور خلاصه کونمون پارست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91254" target="_blank">📅 10:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91253">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇪🇸
دقایقی‌پیش انتخابات رئال‌مادرید آغاز شده و تا امشب مشخص میشه که ریاست جدید این باشگاه به پرز میرسه یا ریکلمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91253" target="_blank">📅 10:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91252">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e8a50238.mp4?token=u-8MvWI53pyN1Do7cylI20OuekmUPTL9WpN9-t39DSUtMp8XtybExgXC5QuL13dMWgC_2T3Io9PL2IsE3Kwu2mH-9WFTjQ7LA9-zHYmOS5TawBwTPjdihjmV0NuBZRW9hI7MYxQ2KLUhjuG894NdDqa6ujPOJipO4rG4rw5RCR4KkGAxwS2oQFb3lAUcd0RoTn68vM0fkcgSlkMA0BLVO3g5ZhA0cjtapUlOlUUP5CuX6Dcz1Jrjbwh3JaHdEa7wa2r2MNcMrEnB6bcBXvUgz27cq1Z6MKEf4xvk35OxtGqhaj4M716kyjmkEknaiF7R3y-Th-QG7GSBRSbooJt9EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e8a50238.mp4?token=u-8MvWI53pyN1Do7cylI20OuekmUPTL9WpN9-t39DSUtMp8XtybExgXC5QuL13dMWgC_2T3Io9PL2IsE3Kwu2mH-9WFTjQ7LA9-zHYmOS5TawBwTPjdihjmV0NuBZRW9hI7MYxQ2KLUhjuG894NdDqa6ujPOJipO4rG4rw5RCR4KkGAxwS2oQFb3lAUcd0RoTn68vM0fkcgSlkMA0BLVO3g5ZhA0cjtapUlOlUUP5CuX6Dcz1Jrjbwh3JaHdEa7wa2r2MNcMrEnB6bcBXvUgz27cq1Z6MKEf4xvk35OxtGqhaj4M716kyjmkEknaiF7R3y-Th-QG7GSBRSbooJt9EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
واقعا جای چین با اینهمه استعدادش تو جام‌جهانی امسال خیلی خالیه
🐸
🐸
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91252" target="_blank">📅 10:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ffffee7d.mp4?token=T2kK6yBxU5hlbhUqIbHQEIYcbsoFhvsyaWb2WbcrZcVIf46kBIjA_xRWMknSc5-_ldQ2xmONTWPjF4Az3Gn8vVq-fmfhTBG_zVjBIKyaDgkqeZx6JKsTmi2sMWvH1Yu1Zd2_mhvrR0W6e15Q-yobrAt2h8ptWxfDXi9ehfNT28eqjw8K07C419XWRN8xv7uHiCq5V8NAe0lSZplAMiny92YGdY5PdOWXYcspJcDqEAgpNHiPRGuwm54W5flqOuceoMuygWJaHoPBciQNF6dpVRQzURbRBpPQdfgnD115YdXkxIj4_zpW8LCbJMu-nt1k4kzWn_pGEog7_FsIkyb2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ffffee7d.mp4?token=T2kK6yBxU5hlbhUqIbHQEIYcbsoFhvsyaWb2WbcrZcVIf46kBIjA_xRWMknSc5-_ldQ2xmONTWPjF4Az3Gn8vVq-fmfhTBG_zVjBIKyaDgkqeZx6JKsTmi2sMWvH1Yu1Zd2_mhvrR0W6e15Q-yobrAt2h8ptWxfDXi9ehfNT28eqjw8K07C419XWRN8xv7uHiCq5V8NAe0lSZplAMiny92YGdY5PdOWXYcspJcDqEAgpNHiPRGuwm54W5flqOuceoMuygWJaHoPBciQNF6dpVRQzURbRBpPQdfgnD115YdXkxIj4_zpW8LCbJMu-nt1k4kzWn_pGEog7_FsIkyb2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇳
🔥
هوادار تونس در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91251" target="_blank">📅 09:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91250">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f42ba19fd.mp4?token=u89k_Jlycx1kOo58gzZyfhhO1K8SV1nnThyR8N9fNO1Vilirjvz3Q4tWllHXs7Q4G5zIfum9OSWgho4p2CnYOpkRaklaK1cHyNVRqIaZZUlETdXG8fuQ6QS8qNttiaG5PHLV80-QP1Y0XEkYmeEaXLYGtbXhwR7jmO3ljmH8_8wniRBDlC6Y77OnfBiPXXBbUiQ5smoD8zs_8duBHdtt9drjVCcEV5I60QH1uK0ANJL_xxJLLQ3DQ4WNUcpIL8-JoOPAd4hQsxtVMininPotsODNnATG7Kc0N1vEfN7rqOa4MDJXEJd7U8qZ-3jbe5Y8cQ8x9ePFLla-kYpiRC8jBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f42ba19fd.mp4?token=u89k_Jlycx1kOo58gzZyfhhO1K8SV1nnThyR8N9fNO1Vilirjvz3Q4tWllHXs7Q4G5zIfum9OSWgho4p2CnYOpkRaklaK1cHyNVRqIaZZUlETdXG8fuQ6QS8qNttiaG5PHLV80-QP1Y0XEkYmeEaXLYGtbXhwR7jmO3ljmH8_8wniRBDlC6Y77OnfBiPXXBbUiQ5smoD8zs_8duBHdtt9drjVCcEV5I60QH1uK0ANJL_xxJLLQ3DQ4WNUcpIL8-JoOPAd4hQsxtVMininPotsODNnATG7Kc0N1vEfN7rqOa4MDJXEJd7U8qZ-3jbe5Y8cQ8x9ePFLla-kYpiRC8jBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پارت چهارم ورزش در خانه برای دوستان گلم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91250" target="_blank">📅 09:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e859cb5ce7.mp4?token=MAWeTnRyNOv-fIf6c_AiEKseozcDlFgN8P8lMAMZk55iKbVZTyUSAbG3cHNs1evXDwc3Lw3DcsEn2h6Z6yRCJMpKLbS6qyUBgQobjea69Ef36zf4YDVfEpJnxZZHk1qRvHC1T--ZNf4qufvlXa9F3KPfQG2WzckVxLay2RdA-OaSzEs5W7ryrWAWInIFIE_atGp3oCCLdTCnAAfUl2lR2iKRAJkS8T8C0U_q7_No6SwnczlACWfZeA78NdneB0reeZv6oLt5ZyarLOA-hSL2FEIKe70s3ywvm0rmv9C2RjcQ0vXAUnKrS2rtVznhzK7mC9kxAFIav_n3yDCxOzXkmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e859cb5ce7.mp4?token=MAWeTnRyNOv-fIf6c_AiEKseozcDlFgN8P8lMAMZk55iKbVZTyUSAbG3cHNs1evXDwc3Lw3DcsEn2h6Z6yRCJMpKLbS6qyUBgQobjea69Ef36zf4YDVfEpJnxZZHk1qRvHC1T--ZNf4qufvlXa9F3KPfQG2WzckVxLay2RdA-OaSzEs5W7ryrWAWInIFIE_atGp3oCCLdTCnAAfUl2lR2iKRAJkS8T8C0U_q7_No6SwnczlACWfZeA78NdneB0reeZv6oLt5ZyarLOA-hSL2FEIKe70s3ywvm0rmv9C2RjcQ0vXAUnKrS2rtVznhzK7mC9kxAFIav_n3yDCxOzXkmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
به‌بهههههههه یچی آوردم عشق کنیددددد. آقای کوکسل‌ بابا برآب کشورش ترکیه چالش رفته
😂
😂
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91249" target="_blank">📅 09:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjgUSPG4mSWhBC_fNe4p_BaTemIYj65TZhsTXkKn-b4xlOEvkWTimnNIgfqs75oTxv41yoqVRaqAdfg3ofE3D7C00ZH3aGdsgh24sL_AloFuVrj6YHX9_KG99kQF1jpF7kZ7Rf261mAgAdBe9JsdPLE1rgs4U_alTFv_dIwFgQyzgZ0pzXEVhOUZPZ_2hJulp2uPbYmVR-RKIlC3NoIB6o3ohlo9fxn0qhT3lDajFihflwaVMiElHtKfPGtPuxXNE-1UWP_YQp7PwyV85xNj1tzT_2qf4CFtr0I6WpZmtK12F9FyvBK3oi9TR_muAPSmulLVOsOja7mxqJbUh8tdJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
هموطن ایرانی صبحت بخیر باشه؛ در ادامه فیلم‌های هالیوودی که تو مملکت رخ میده، توی ورامین چنتا دوست صمیمی سر یه دختر باهم دعواشون میشه، در نهایت در جریان درگیری ۴ تاشون به قتل میرسن و ۳ تاشون متهم به قتل هستن و منتظر حکم دادگاه!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91248" target="_blank">📅 08:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91247">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q07VqdNa3vjyFrV6Xkk4MLbXnz6S95KRTkgTnXZe_kSwbgCloPV5cSHnW0_yCpLr6uyErb-lOLrGbyvd245aacPMOB9aQNX_194OgZe2W0lhPjjR_Er8oeV1xDTVXKMcy7zk9Cr0svZ4jz5D6meKmzyaSxnEioe09RYXpf0bd1Pxu6gLS7cTlV9lQeJv9O1lB-ZXccpwiO5mze-qeupI1Nfne3nER79QxBWKhlq7fwLIlbvcEVtPnWsK_TqNo9vfOqMUhV12Eute5lftvwpTpjBI7KZaCIRsnO5Id59KHqk6TJ3azMuAABogd3WGY39NmtuM6_1g4h6lHHHM23qM3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب آرژانتین مقابل هندوراس در غیاب لیونل‌مسی در ترکیب اصلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91247" target="_blank">📅 07:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91246">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74203b9c2e.mp4?token=uAKEJ3j5M9pyqJhXQ0aVOHp_S5K3_1dF9igsL6B8KTWDG0n8oBdNaVJnlkosewqJI3CT7rQ-fl-m-msRt2hLZgAC6vj5AEgclaIFN2aofrRKQ050Fb7ddk0Ubl8nccUs3GnuV2XKSHxH5nR0VqFjkQeSZ476GdATfgKbVHFWajugAxjyW2oar490ysRTl2aLGYI-oAAP6fAmxBwDzS_q7LLl9T4rI0x70ZD6Ci4EtOv7WRSfqoi5tUulpDmaCCX7VpLHtyTEIZIWRagtoQdY6wBLEgclHrzZrxnXXbUqSIxPIW35ZyynL5JWi8etnGb39C3zaXkBCB66XmTgKYryOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74203b9c2e.mp4?token=uAKEJ3j5M9pyqJhXQ0aVOHp_S5K3_1dF9igsL6B8KTWDG0n8oBdNaVJnlkosewqJI3CT7rQ-fl-m-msRt2hLZgAC6vj5AEgclaIFN2aofrRKQ050Fb7ddk0Ubl8nccUs3GnuV2XKSHxH5nR0VqFjkQeSZ476GdATfgKbVHFWajugAxjyW2oar490ysRTl2aLGYI-oAAP6fAmxBwDzS_q7LLl9T4rI0x70ZD6Ci4EtOv7WRSfqoi5tUulpDmaCCX7VpLHtyTEIZIWRagtoQdY6wBLEgclHrzZrxnXXbUqSIxPIW35ZyynL5JWi8etnGb39C3zaXkBCB66XmTgKYryOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو کوتاه و جالب محمدرضا سنگ‌سفیدی بازیکن تیم‌ملی فوتسال از مراسم ازدواجش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91246" target="_blank">📅 02:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91245">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMhZ4ogfbcL1NysqBP35aqIkK3tfNBPhVCZqRq4NY4dMHUwenJNr11_ushnNpUzhVmWFV5bmXHCiCgB7MIuXyQJkhikAR7tcAX3Tml4OkhCzMix0Ws5b5VT5zW4Mma5p4NaD5M9wZdIbrc7SfVadBtF5fDuIaz5z0p_TbrAurlHGdm6pXl0NRyQPlpCcjIMvmzF3d3Xk9R0KyJPg7Dh5cCgZgU5g8htahLFJD-RiYl4KsLQcx9G0BozSUuE3NX6WYvSRuVBiOt-RQHzZ5GkWTZupCHpLIhPMQK7Fbblkjfi_FjuACGJbJtJUQKV1th2kaj1SSBZKuZtS9TbrZvj3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91245" target="_blank">📅 01:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91244">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🎙
برناردو سیلوا: بارسلونا یکی از تیم‌های خواهان منه. چند گزینه خوب دیگه هم در دسترس قرار دارن اما در نهایت تیمی رو انتخاب می‌کنم که عاشقانه من رو بخوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91244" target="_blank">📅 01:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91243">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsZC0a-J1DLCYBh-d2wyWCiPFuKgCzjWzXAeE6Fs3LF27h4geubn_oBadL2COnwODD0u1jblA0eSkj5wWRF4qjVJLo0uaGCEg4l372hq3ZMJck9J7nElUKvHjlh_TmxuCf9AGIUPzbDUaK4QksQHm4INEl9VVs1lonbOZn9Zzbjc8lbcTcc0WWrqd88FwZb0AlmW6--p9cl7kxlp3YVhsAi8QtGnZXoiHNGQ85DdQKPqXmqpTN44ofoZTXjd83cTghuPXlWUi3XUDB5G4YaM2bpJhzQogyFxbiI--2vW9geCxhnkf3qIZLDighiRlDHEcA26cClIB6qgC_MsXeyfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجوری استایل زدن که انگار نیسان رو اسپورت کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/91243" target="_blank">📅 01:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91242">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42162246f8.mp4?token=T4iVMx8lC3UOe3WqP95lGjn4CaoybkE0Tksj2n6gZOkq7eZnAHk1GfkrEDeNhbld0kNsFNH3dUSyGmt-qJEhdK88LUEuaETq3FfGLz8acSJth4dckWVsObCk3AeXzPM_7NepCoGCrRCJpzu9aHhQX4SL1EaL3U2vAN9PkKaEzNgV6I1xLlbT2VxhhQUSWtXzg9S08YZn_zXeO471-U32m4Hz1LHGrVsiEelRXTPAjUf5dLi8YynKzkHLRFiXM_TTGB29ZOtDxicggnUqUgROLlDNnUMNUA128dC9XUWlM70osX3m-01S6mhPgYofhVOw9PUgwgLoAz9DQqwUfXCGw6pZ_ZH1iy8vYdpi0Z4VtRvOhVi1JmE_N9jS3KK0kePTPiVSxhbxsvSxUwXWxv1lFouq7-Yf_iUVh1I2S-tjdeHH1D8CQnFJGvkTyy7niIAxY0Q-1CwMBNYcOtggXuyTYjz4kgFkpNkS3vFvT0O2K6tESe4aSdr6Qr4IrbzT51LSqIH6tmBQ7rt7wGsyWVh051mTw0wqqBrv9cxIX0leNx2NAqWp99A9ctqczMTdE1m0ujCNjTyoFnc6mq1QQvun1SF4G1_wLtaMPdEtZi1nq3zAtO_0KRxQczZE8LEfrN1yTk5iNvopHTvvOys5uNhbsSIrBfi0YeyV5W6lHuXa0Oc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42162246f8.mp4?token=T4iVMx8lC3UOe3WqP95lGjn4CaoybkE0Tksj2n6gZOkq7eZnAHk1GfkrEDeNhbld0kNsFNH3dUSyGmt-qJEhdK88LUEuaETq3FfGLz8acSJth4dckWVsObCk3AeXzPM_7NepCoGCrRCJpzu9aHhQX4SL1EaL3U2vAN9PkKaEzNgV6I1xLlbT2VxhhQUSWtXzg9S08YZn_zXeO471-U32m4Hz1LHGrVsiEelRXTPAjUf5dLi8YynKzkHLRFiXM_TTGB29ZOtDxicggnUqUgROLlDNnUMNUA128dC9XUWlM70osX3m-01S6mhPgYofhVOw9PUgwgLoAz9DQqwUfXCGw6pZ_ZH1iy8vYdpi0Z4VtRvOhVi1JmE_N9jS3KK0kePTPiVSxhbxsvSxUwXWxv1lFouq7-Yf_iUVh1I2S-tjdeHH1D8CQnFJGvkTyy7niIAxY0Q-1CwMBNYcOtggXuyTYjz4kgFkpNkS3vFvT0O2K6tESe4aSdr6Qr4IrbzT51LSqIH6tmBQ7rt7wGsyWVh051mTw0wqqBrv9cxIX0leNx2NAqWp99A9ctqczMTdE1m0ujCNjTyoFnc6mq1QQvun1SF4G1_wLtaMPdEtZi1nq3zAtO_0KRxQczZE8LEfrN1yTk5iNvopHTvvOys5uNhbsSIrBfi0YeyV5W6lHuXa0Oc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
به‌روزرسانی شبکه World Cup HD
🔴
شبکه +Mifa از مجموعه GEM با هدف پوشش برنامه‌های مرتبط با جام جهانی ۲۰۲۶، با نام جدید World Cup HD فعالیت خود را ادامه می‌دهد.
📡
اگر این شبکه در لیست کانال‌های شما دیده نمی‌شود، لطفاً فرکانس زیر را دوباره اسکن کنید:
Yahsat                 /          12034 V 27500
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/91242" target="_blank">📅 01:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91241">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
#فوری از خوزه فلیکس دیاز:    ژوزه مورینیو رسما درخواست جذب برناردو سیلوا رو برای رئال داده. رئال مادرید چند ماه پیش از جذب برناردو سیلوا خودداری کرد اما با درخواست ژوزه مورینیو، ممکن است اکنون همه چیز تغییر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91241" target="_blank">📅 01:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91240">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elKnxLnUJkt01VBPn3mYme71AKljMGO5IyITIo7zuxCDsbOt--K4GRm4bf2zwyvB6SlQSnz1G7rXjETeBBe1TdSMXDVP8t9cW7rpoc-0LjeYdIT6QEcs1fCN3gMxRX-DvTVVVpZHUK5Z62Q-ydDuF5e3cFfH8t1JRc3f1NmwPl8FGxf8a7T8QA-wIr2fnIT2RyV89o9nzkR8Dfh50MBnteBX3qP8_lIpnMJC7UVt9R0datQXkdqofAQPJ6Ml2vlmjKlW0g3-33Ay-8wcSCqIla9YOxYVvC9FhlYhcuuIQuJXkIhukoV00EOrlJUN6iKqAfIp0fH7Jhp9pqAE4cUw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فوری
از خوزه فلیکس دیاز:
ژوزه مورینیو رسما درخواست جذب برناردو سیلوا رو برای رئال داده. رئال مادرید چند ماه پیش از جذب برناردو سیلوا خودداری کرد اما با درخواست ژوزه مورینیو، ممکن است اکنون همه چیز تغییر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91240" target="_blank">📅 01:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91239">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3-wZGjnbnmS5jP2HMEVUDKQOFIgkS5pZIX5T3X9Ga8gZINgZ7I8Ey0_y2WNwvtUp40L_pIlqZtDrMKDtV1DxbkSZAG44Mcws7g_pxemcQs9wUzFYkifVNvlleYSvM2ND9oMjLFbRKkbBkIrPM6-AoWjZ3K00tRzKr8IGQhmwsw0JbhH-t4ANFuLQB0vzCn3IGDuZYOpeEgVruvB4Un3ucL9k-0Xw3jLSCeO4r3zMkyrCS6aC-7rK8eXZstSVSh2Yl-QOY7lL6jT7RbF8XoSWoCUOqidLjE-Gq5v6vWZ8Q_cnjli-UI5-wCaD65S1BfH3f_pAI7L6pV9cBGQNdALGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 روز تا جام جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/91239" target="_blank">📅 00:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91238">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f6380c33.mp4?token=gCWbRjW4n-NCFVeu1HZzgPwq0xfiY9crI1ycMlRnWSAVM13yu-7PuMlHTBNutJJMW28fueca8PPIGsoJLXKTyFufgp1DCpqftM9ENfWHmwL3BmXZxIT0bvtGiMilRLIcfeIUlV2c_12xI-5qJEllGvmLqdqqY4Xfd_AZSKDDjOoJNwCilr_bYzKy4HCcom7jgmA8BmUBJr0PsnHVxhH_FlQiS2bFEptZHhOlpZDFkgL6kHjNsZipCZ2kZv7dl2yZxyXU1Vt618iU9SB9K_DUnSn_-SoI739oXULigtLXfwZ0T36VA8HH54qjstcWH57-89dkCLukBitVz5U1r5z_Q4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f6380c33.mp4?token=gCWbRjW4n-NCFVeu1HZzgPwq0xfiY9crI1ycMlRnWSAVM13yu-7PuMlHTBNutJJMW28fueca8PPIGsoJLXKTyFufgp1DCpqftM9ENfWHmwL3BmXZxIT0bvtGiMilRLIcfeIUlV2c_12xI-5qJEllGvmLqdqqY4Xfd_AZSKDDjOoJNwCilr_bYzKy4HCcom7jgmA8BmUBJr0PsnHVxhH_FlQiS2bFEptZHhOlpZDFkgL6kHjNsZipCZ2kZv7dl2yZxyXU1Vt618iU9SB9K_DUnSn_-SoI739oXULigtLXfwZ0T36VA8HH54qjstcWH57-89dkCLukBitVz5U1r5z_Q4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🔥
پیش‌بینی مارادونا از قهرمان جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/91238" target="_blank">📅 00:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91237">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeV1MoSnp5TTT-54fmN3BWAKpWbvAVRWgCxkS5XSLf0AzBrfsG8JDDdnEo1bgki6H5_7JlOYdjR_BJvgyBpFO_oQiaXUSNKjSSSeY56jYbPt20-R0E__TI_u2bCVOd1CaeBO2V5cOvx5RfbyrjHGZWLjna-5HI5TNmOMNaXRG7TTnPYe5ZdOX48E-wB39kh8WCl0ZvlAQe24-xCktPFGnTtXTFV4z36VSUIJE79xMsI8qmiJjUJ1zMu0CjVPemo9c5PxgqoKPv1phjbSygyrGt9XJjrJk7QCCqbAtfxBMK6cJcBx66MqJXRNYsBo1j4ObcevW24fwnZ5HNaaDPnFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پردرآمدترین سرمربی های ملی حال حاضر جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91237" target="_blank">📅 00:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91236">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn5wYrWvEqmon6BlftghEzx4kQ0h4nw8nbRXiEetIqajoPlW0aU32oqsAyQgeoXQxJ7CjjCDaumWdMBWMrwcbbXxOLn7_wWtAijWfeSOabBmXtk4Gq4N8s-drBdnPhj_GysHG77HJ4-pAvWdHSHPGYjyoDA0JjgYmylesHw9HcIONyC0ZuPUI80HAbAWvDiQiOVh-6tGlbjbh8nalclrUmSsrntWfIvdSwhCboHYBKL7gPa3TyGK5enC11gp3KO9GpsePfHSx3jsKa49WmkzO3OJwQC6BydRmY6GZ8zzfMbuaYgz6I7w8Gm5lOtAv264SmpTe92t5GxDJdDEm2_cGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیلور سوئیفت و شوهرش قراره یه مراسم عروسی با حضور هزار نفر بگیرن که اینم قیمت بلیت جایگاه هاشه، ارزون‌ترین جا 8035 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91236" target="_blank">📅 00:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91235">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇦🇷
#رسمیییییی؛ مارکوس سنسی جانشین لئوناردو بالردی در تیم‌ملی آرژانتین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/91235" target="_blank">📅 00:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91234">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo0_rTQw6mkxtmh72iaecy33JKnmYl5XZwtsMCrZE5ZANaGIboz607ZXpgcQYKK2AmoHwpa8xe0v1fQ0TPQcH5ihacOy41hh4iCM0mINeNVAtuGPRFVflafdDJxbaslPYIlW6BNkF9YWg1sKH2ht8r2mSwm4zQ03Arl954CmAqRy3RzdDQz_iERC4ph4XTuW5mwjpgzhkLOKXf_6GeDjxz7YJghqlqq87fC2Q2MUqGSz6e71kAraxQFxTHZeE7VvztrCGw2JrIEII_aRvwen5f3SuA8pt-ad_hoerunPjW17AN6mmF3O08zi8-SjRrSrc6jBwxh1735_SS-pRoXuWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
اعلام ترکیب برزیل مقابل مصر؛ نیمار در این بازی بدلیل مصدومیت غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/91234" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91233">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea39da6f0d.mp4?token=RCu3j8lDhGca6EhjIvtshn1L7cNr7GlJJI921D7-1a8ph9UH1DfO9SqxxcDanlLBf5l-JQGILtmE9C96D_jXhOyMvTbL0ZiHdjkHJV-VxipbSFiY5ksfUz2mjgqOkIvdfoVnJltb4tv-BGXfiSJyf9K0cN4k8MllJU2YriyqqEtAbqif86vVro0rgwcWonqTSGZeCTpGi1VBafIONvWYQd4h7p8dqudrgSkKRaUEiZkbA-xzIGOqsRBKcMPcjz3bGcDnSZIiMrmJCsyi0C0aL5M0ScznOSOWlwJvCoqf9Wr3TPF9Wl8c0Fms2dc0TxPL049avjuKfd7Ax3Bv6TKo5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea39da6f0d.mp4?token=RCu3j8lDhGca6EhjIvtshn1L7cNr7GlJJI921D7-1a8ph9UH1DfO9SqxxcDanlLBf5l-JQGILtmE9C96D_jXhOyMvTbL0ZiHdjkHJV-VxipbSFiY5ksfUz2mjgqOkIvdfoVnJltb4tv-BGXfiSJyf9K0cN4k8MllJU2YriyqqEtAbqif86vVro0rgwcWonqTSGZeCTpGi1VBafIONvWYQd4h7p8dqudrgSkKRaUEiZkbA-xzIGOqsRBKcMPcjz3bGcDnSZIiMrmJCsyi0C0aL5M0ScznOSOWlwJvCoqf9Wr3TPF9Wl8c0Fms2dc0TxPL049avjuKfd7Ax3Bv6TKo5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی داماد فوتبالی و رونالدو فن هست و اضطراب اجتماعی نداره. خداوکیلی حرکتش شاهکار بووووود
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/91233" target="_blank">📅 23:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91231">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B07-Awvl1jSURY_sFITjrqZOMCeiK5iRlKgA5BBXjnWAcAnPutD8OIDhlwohkc7qRg7IKZ95hhWYmQPZreQdTD3VzEb2JcftoMfqVreYHBgSo2LWXnY5KhRTJGxNtpCOxZ-J9oiYW6RFbHCTx3_cvre4ulyQ2P2zyhHDC46jVafEMI4l9KRRYGIXZmCX0jwFgEcfZTyVE0vXR11VenhxsdP0AB0kt0KVQfHtM1XbtlmLlJ6qvFVTRXHfIoUtGJ5r0l4EEHX14DxM1JmYzfVer80IRTIy65LS7Ec4fxt9diO7Mqq0phfJY24IEpRNqRU-X4mxCNC2DhIF-8qPtC0xQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
❌
مونا آذر پورن استار ایرانی هم اعلام کرد که قراره به کشور برگرده و مجوز داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/Futball180TV/91231" target="_blank">📅 23:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91230">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a25be77cd.mp4?token=dGsKAbMwGVtEaqHVyEJsDgi6GjTU-CbU02H8Y3NkRrJ8o00BoQeD8rHSkoshzRqZIgU_I2p7_v4PhRi9uUqlTJ38uHZSqkaBmdC4W26kExYrOaHFw_Cvdj_WPEFYJpStc2mikDA8XG55ExJg8HsViqmcBLM70gBCQSZ4hxGxaow0DgyZeG-U3lreUDWWItfY5N7Tt1N3SgLSWLQhqnqzZHW-2skpWi0wW0egNfnxLVx_uVykucAHf21FLAp03ZUObQtji3lmo-_k0UpzSTKWLbhNrC_K-6OT2RMWOM8OscLvhQ0wVstqNXDMXmeTbgoCEa5a7sAs-TfQz_oYJaq09w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a25be77cd.mp4?token=dGsKAbMwGVtEaqHVyEJsDgi6GjTU-CbU02H8Y3NkRrJ8o00BoQeD8rHSkoshzRqZIgU_I2p7_v4PhRi9uUqlTJ38uHZSqkaBmdC4W26kExYrOaHFw_Cvdj_WPEFYJpStc2mikDA8XG55ExJg8HsViqmcBLM70gBCQSZ4hxGxaow0DgyZeG-U3lreUDWWItfY5N7Tt1N3SgLSWLQhqnqzZHW-2skpWi0wW0egNfnxLVx_uVykucAHf21FLAp03ZUObQtji3lmo-_k0UpzSTKWLbhNrC_K-6OT2RMWOM8OscLvhQ0wVstqNXDMXmeTbgoCEa5a7sAs-TfQz_oYJaq09w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇹
گل‌تماشایی برونو فرناندز مقابل شیلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/Futball180TV/91230" target="_blank">📅 23:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91229">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fXNJeDB2sxvVT2EZFUIa-pCvaWirm6S9LrP4tsN6axG547ZUryT3V567Yk3fhfPte5GrBOyDqCl6DLl-zjaiLY4eyMSxp8La4hAtPZx20GKPtUFoCEao-pzlFInNdkqn8s7Xi54njXOOD_nyv3BOJ9c3zhwlBMr0clMfuMvXTS1erdSAzezAQSfPZ0tvCS36JZFerbnEftESaXyjBTHWVWlKrvXqAL14JaVlEE37OjRPmjlH7jYpOZl0v64xcTwkXHiCeycol1N5koiin1LB1qj4tDjG8aeNWukSdkLDSgVh8yj8qXbTh7GsZnfDgyK8EQ0uNc3mJqPC_f7yvbmuWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
وقتی میگن پرتغال قهرمان جام‌جهانی میشه
همون لحظه پرتغال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/Futball180TV/91229" target="_blank">📅 22:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91228">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1050253ed.mp4?token=sWKAt3mVuEV37Fx66E97CEPFzi7jlogNAViu2tkeQJTZSkoBWvGdi6K-2dnWljGWXJQH9kMmcmiVL3VoHDlVJ91U1i-DM8f28k4WqbJYJ9whAbKigJio7lBSM-8ENYZ0DWc-y2KWpXDGtWZA3L-5YiITfezpJTfLwNQDBfNwlYOgNjYt4x-6iWk3whJg1Y1BiLr6CQz-PtSEnP7z--xpmgb3Z5LGdqYyO1Jkbqep8dZOVRh0pnfdJcyPvah4QtnrcXHj6zf_6ZVP_iSd8KUc9gSF_DaGrkde68zeGyPg4SRO64VEk3uFQtNJcoJsnxl_EjkYORKhUSzMuw0ftx_TTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1050253ed.mp4?token=sWKAt3mVuEV37Fx66E97CEPFzi7jlogNAViu2tkeQJTZSkoBWvGdi6K-2dnWljGWXJQH9kMmcmiVL3VoHDlVJ91U1i-DM8f28k4WqbJYJ9whAbKigJio7lBSM-8ENYZ0DWc-y2KWpXDGtWZA3L-5YiITfezpJTfLwNQDBfNwlYOgNjYt4x-6iWk3whJg1Y1BiLr6CQz-PtSEnP7z--xpmgb3Z5LGdqYyO1Jkbqep8dZOVRh0pnfdJcyPvah4QtnrcXHj6zf_6ZVP_iSd8KUc9gSF_DaGrkde68zeGyPg4SRO64VEk3uFQtNJcoJsnxl_EjkYORKhUSzMuw0ftx_TTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
سوپرگل تماشایی آمریکا مقابل آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/91228" target="_blank">📅 22:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOkPekz4fKx3IXySvFAHOPfGdohItEYqZ4ZBX924fZuVllPLlWsSbLTrWgvg6cXAZgw0navCpXGsLjJJCI7DvbIHdmPTysmu3E2pYjQvoEuS-3sKagVdcgzZVH2exvzxCilwivZpaJ3oO_12_i6gdFPHu5KbFhzn4LlQQE_pIbSEB0Vc3UNabR6J-n6iioqMFFc8TA6zv85xI9U-Vs7rWlCl2-iSdAOZd0XuNqhHUDsc34k_2BlM1Gb8r49rnQKgcXounFW7vr30nr7VtW3AFUbxL5qFK2uGvHF2e_wvlRA09pVmSq0QGJj26K7aDbKJcdkMYeEou9_xkY9m4Krlnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPleLXMNKDZOgPv4m7NUbx34xWpLbR9zdUXf5pvJTx9pqA6G2-I-Aw5gZA-RzMuZdEoOTQImiXhlWm9TqNkT6sZ_fQ4a2WB1DTOpE5Zb-ZGI2C9n9BAFH7-1FNxxg7Id5GE99CW3IibIDuEK9TCKEgfk3B06qGxjgS4Uf2Xooc6MOnaiguQMbuObTTfEg5aDxS7LYBTPI2IwW1l8Jw0sZKAhM7Y8wGyCqDlUJVHFx5Akfl4UIuU4Mti8v4qaW-c0fVNOf_Jk8XTe8HLiaFdq1PStMuu_aDfEm0bU4A2yPeowlroE4vyt8XnGuyvl5CFI4qp7wconfMXIrCAziDCfRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🙂
🐸
ضمن عرض تسلیت به برادران سرزمینم ایران باید اعلام کنم که کراش والیبالی شما یعنی خانم آیتک‌سلامت از خوبای والیبال بانوان ایران، امروز رسما و شرعا ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91226" target="_blank">📅 22:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMVO-tO_OTicrHfhVAzjUG42o0F-IMc98scWQc_6Lz-Bits3JmWSx6l9bYBIZwRx_XY9VHGIIMpN03JSW_eW9Tp-qjFydGKBBYTP5ck_rgeC5Hfu9QBn3WKk39SWCUYFeciyRXJuX8zISfXs7w8ScXKFfstJiuGNFC_avPQAuZJg6_UtxHVTGnR4ptuH1MI_n4es673zLGm0YrfsXqjg4bteb6WNAJYIsMgYqeDFbiqo5rCp7cDNRQOhoTJN0aLR-w2yEFPAfosECwS69c1zIu9iFpk7XFrRS-te0wKL1cOjlFlgKsLfSn6uYBaBCtPqis2KAFAK7rahm2eAs2mEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
شرکت EA پیش‌بینی می‌کند اسپانیا قهرمان جام جهانی ۲۰۲۶ شود
🏆
.
⚽️
• این شرکت از سال ۲۰۱۰ هرگز در پیش‌بینی قهرمان جام جهانی اشتباه نکرده است:
• ۲۰۱۰ → پیش‌بینی قهرمانی اسپانیا
🇪🇸
• ۲۰۱۴ → پیش‌بینی قهرمانی آلمان
🇩🇪
• ۲۰۱۸ → پیش‌بینی قهرمانی فرانسه
🇫🇷
• ۲۰۲۲ → پیش‌بینی قهرمانی آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91225" target="_blank">📅 22:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1RGLfwfROBTWwBDTtaayX1EmyeyuT8LuPbS63p5wpM1xzfOELknhvydFFZIjTGHSVlT_XEvDfqorqWJpc1RbaAOvWkDozJgeVAo9xDLtR8YVG5gMOm2DQApDavy0ZbfzlAS2VwVsVyONAxV63iRKwIrJCMI82c0hq3pMYHdiSrzZ7lgro8PBzb4ZnvHJPDCUeqVqprm8mzi77BqmmiAWJJvzRCGgNPVtXiR-BifCRz6XPxz2vtfrDFEmT5hZ8sBz4Wa78pEhEVAY4FHUPFjDfy5Z9fF8AmNu1p2XLAmlHKLf39g-ToYjBnqjPNTmQDtQy75Ok1N_tG418oMbm-0wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاماوینگا بعد خط خوردن از ترکیب فرانسه برای جام‌جهانی، پاشده رفته هاروارد برا ادامه تحصیل
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91224" target="_blank">📅 22:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSpg8kmTIsUG2GAZX3oPEoF_ssmhFnvv2vgAPXy2y-kIVG7WErgauyIH-RA35M__XqSTR36owNwx2pmeiEcdJGRZujrTMKB24OUP3XgF-Bu3PbnlhjAWIuyI-yaZ8DTXS9upsk614zxVOOM6sHGTIpgOX1V0pJrBJZc8-MwIAGMM9ANhfg0qAtg2acxAfG1QpfN0VECYo3A63F1YTImgSsKLgVMAOTr7YNHrrdm1h8Rb3aMwt7Njlx-r6o1wlQZ0771_xIdta5s6K-TzXBVVixRvpmxgHVeQbB3DuQAnIRDG2NEOcOUisg77etQvtI1gipRrm8XdkrgWJZzm0-NWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/91223" target="_blank">📅 22:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlAPu-xwKsFBn_aSOF45uc5svH05zBJi1s2krsML4VdNXjoZm1I0yRuidetNh5EhcyKG20RTwoy7kiq1BU__y4eLZTTux-_BFN_8U7TR3pVPB9LuTCoWdVwqhVuUtugAVb6WQzeLUdZtYPwrYxuFASpMaAyEgLx6GyOW29c3GBVxzIUq9HdU9NzLsEf8z-sT53NZJGWGQBPZ_A0T-_REh5YaQXsqWtOS5ux0G2aPDLG60EnJxw-2cNZab7Pgv2c0ppOGaEPg8-qfkoUK5UkNSfu-7PvvC-I2fwPkHJKrzh7YGUmHB8L1lkeBWTsM3ltR6f0STxJSGmrAt5efYRn_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیائو با این کار اگه نخواد جام جهانی محروم نشه باید نماز بخونه
😂
😂
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91222" target="_blank">📅 22:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoYDNLvCSOx-IyD3lC51hG7veA7RIMwwePvqn_6dWmQjpFGKIhy2F2GO4-0o3vkxyryvM5Qqj6MJrK19LGffCaf23j3lEfhzgsZ2T0bQZVmPeERrAP8pRcKn6n_SQAhnAxpswQIQBqE7K0pfGDVV5jnbL8TEb11_kE3kDBLohiW83vUG-UyT5N3nHD8tYXIgqAPTlG2GROnE_Ej_-NUGdxaDN9PIP2l7l0yPFsSi6JlbK5n5mLf9umKLAkTQHkmc6Ssrolcympj7ZuB_S7bjYxK4fKlfiovYb5Al0A7jAlbyXLTEPmA_a5BlRr3oZ9SCRFB-I8CVMNkPlpSPXAsQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکاس تیم ملی عراق به جرم همکاری با حشد الشعبی پس از ورود کاروان این تیم به آمریکا برای جام جهانی، ۱۳ ساعت در بازداشت بود و در نهایت دیپورت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91220" target="_blank">📅 22:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91219">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4yuM1Ra9hddTdt5TffpAnMQCBGhxNCz6uS1QJ8C_nHXf2hjqmyy7azP0zPegJ-w7Dl6pLV88dBFL1lArY7KHfPqR5NJjnJnae7Fjz1dA89qVLkrAXpjNt9aYfH0fiJ8CrIBOTbuL1gcS4kBY8Mqudchj6BXF4xwLXAmzdVuWm_0Mk069ayq73PhRPvsadmNjQUz7q7itRWiLY6R6JfwypT-aDBTBHh0hTeIPzYxjkfif8D5vKgMpKz35A7Od9cHtkpS-n8mGHCnH9hEVyPwhpaQzdAscZ--ofpwGZqeFBneLPajmunjasdhY6HXJ3alXo4v4wd06PeCTO82RPyGAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال 1998 مجله بزرگ FourFourTwo⁩ پیش‌بینی کرد که دلتونو خوش نکنید چون دیوید بکهام سال 2020 این شکلی میشه اما تو 50 سالگی این شکلی شد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91219" target="_blank">📅 22:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91218">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdGe7xMSGE5RfPBVrlF0COEAOfH5CDdc9hDDEoruM8n6jcpGaXMST1sM8WxeUWbUR_0zv7gd5yuIhbmYmCuUVXK0t-adkiBRGd86XWa6p3W3bsuz9F6GBpbcZDS1rxL-jy9SeIMkV7inZ1yRcj19JLKDMbb0CdUk38cyoaxrAnxWufOKmsR9npc-GZtEimS6LerefTx_tf-PJ5Dub-nwfiJpNaDA8i6ts3yhHc7Wpx5mmetMs9fqz6J4b0XLn27pMgHFXGj_C77xbrxMPrOLJ7C8UpDQPOQmoMOMGimgljSDCPy8xXSGWzv91a9u_F7rGjp2eeaB9KzceGouJzliRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناخودآگاه یاد اون عکس افتادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/91218" target="_blank">📅 21:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91217">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFEtDHWrS-F4CGmOMN9EC9aOYtpSkJlBq0NTd2RpdgntCJdfvd4IUpuW4DjJKVxnmUPcewSKrWoj7BDRiuZzGligApcM_h4dMyFxEKPkTOaJL-GkeM3-f5tICpLZ4ziyVKHHO-HCEgGYXv-PT9_ct6c77Q87A6cQBrkp89V6KxvHZsatLfp1UkUmazNncOtwMoecxRCmjf_4EthzO8gvICunvMspisvRKIwsZcv1xn5Wtq7gGrauvh8qm_d-qwm430MJf-Zh5lX4Npf_sZm71f3RBfQPO_PdoVHX9AUQXapA6UliHuoRtT8HnO9JVLDxUwBkFzjXyN7GUyAkF_8YhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید لاشی چه دافی مخ کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/91217" target="_blank">📅 21:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91216">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArEtzUGmVzFEBS48xLC-VCppAkW0UKqehOJfY_6M4eiQBnCh4EVyGiGDpVii3NmAFxeFy8DI__dlBXk7P7u0Nxv5XZpx-WQZRlX2Lm9hvTw-wK_Ls_dxL-5upxTP3-bA3TPv1Y5mMCQqG88x4QKnCWy-4FgGt13wxrGliMUN-RiZny9jWgy6BxvAPcDZcIKblg8ezKekQBYOik7fFAuNwl2o9ycaFnHzr-sZxROYaWNxrXDHhrwKayr9cRDxJgaNsc9KeurOhC7aTi4hnQ3eBIoloFfd39b28xgvuAx34yQDLmmNWj2KDVB7e1JSg_UEjmTbjWROywUpl6I65cjCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اولین جلسه تمرینی تیم ملی اسپانیا در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/91216" target="_blank">📅 21:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91215">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZqKcs7aU-b-f4Jg2QS0w15Qq_7FWe9z-tczbKOMV_g7itX1Ww0B8mOXl6pnOsmxKz4HbDU5g8QuDRkXazrkZNe9k7rVLT0mbrXw5vUqqfmO12RfZAJVE83TG04LuKifLs5vqpPWm2rrPxsOe1RgZtUsOBRtHqV8LSYcsfCipAfgZJjZpCMoGcE9aKqwOjcg5P5r9Rf_fBRsaPHIYk1cJhLBadOqoo9bMSeyOQkEOUypwvcyqWkxpWs8uDYZgra1l8tsf-kHkAGxGzuc5DkJZq2GLGOHplrFvtpqaMV3-9GBQ_87XkzVCDDEtKTcIYb1SZBaD2b3LU2nkbX0pgraPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنری کویل یا علی ضیا؟ مسئله این است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91215" target="_blank">📅 21:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91214">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXGvi_rsFkF7FZSqmg2psxkzvDqazNfQmT1baYwrbiNyr_8ypQj_uB7xnNmCfMXFPQNEto1yulwaqV6i_lYQWCnNOXG18--nDZOXNIxzQo9uV03sTBRrO5utXPYY-JTtyEOmKIcHYyQeeU7Kc6777xj-YhqMd-_GT96ZUYe9YNFZ9h-f0weRpjmVYOPWgxiIHI5CJ_ujdSrdcOVD-OPJrrkw0zDjPb1ebnnCVzFbO-zLfRzHwV2pbVn6-_RbHwKAok5VeYgNz0YlgkH61CV6zkHyL0_iVETWVzBlSwcycRkO8gbckkKqIpd1_HjedJJ--UDEeLI8R-dUzvsUiMMcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91214" target="_blank">📅 21:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91212">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PV2Ms8BnqJ4LTX7Vr8DJxaUSRJobH6x1hwyf87_Qbc_AsK79AmJOvw4RIoFo3qegW1kpX9kHW5jZ7o6bwRFbV8ZfeKrvCWYIl59OTv1vVfw17OJDqOhcLSfl7dTxiKrt8PUlQXflmDEIAjsRDXpdIN5IuEbbiou8DYs9K1Ra06bBWPOd2i9Zg3be_3-EtB7IlHO6o04vzj_S52YJEZmkUneDSgkryH-wkmDi_rSW2WbcuFELZBpYL014nFVQaKelsvw1HJ86uAOMcxHAh_aKIDS-FbzbDxxTMagALWl5Jjj4cgWwcDkJAbjmFCL2AcD7yZgd6cBc9ISJEJ1s9Vmlzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1EaJz5sQCB88P1kzPjQRtwiSF8c9faaAekXdFv5zKTkCBMYZOcL9hPuiKFS40btNW9jeCNUvZwpmHPEt_dC7ulQBvSJDaykj2FdTC8mgnVoYTuwKCm7pyQmluqPByhIjuof-x-d0O1zfJPhMG0iLMyhm4pyP8OfsuPSfzJRNuFkhmkGnd3qyyjBMzpH7djANZw_LasY1Sr36gANAdU44-IvkNFli9a9bpBmxvRZqLqQwLk-wTOWlMT9HMJjFqrjEuk2muZycA56aQaGhij65ILLq0nne0A65AOA6UF7U5lPiSG6Hy8xmMPsOM4v_mCF8G4RLnBN0DbrTxHUKkpWmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم‌های اروپایی در جام جهانی 2026 و تعداد بازیکنان با اصالت آفریقایی آن‌ها:
🇹🇷
ترکیه: 0
🇧🇦
بوسنی: 0
🇭🇷
کرواسی: 0
🇨🇿
جمهوری چک: 0
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند: 1
🇪🇸
اسپانیا: 2
🇳🇴
نروژ: 2
🇦🇹
اتریش: 4
🇵🇹
پرتغال: 4
🇸🇪
سوئد: 6
🇩🇪
آلمان: 9
🇧🇪
بلژیک: 9
🇨🇭
سوئیس: 11
🇳🇱
هلند: 14
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان: 15
🇫🇷
فرانسه: 21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91212" target="_blank">📅 21:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91211">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgPZyjZB9mgkDaBs29-Y2WJrZViG8zGtvGrjRMBz3_hZud3bn-6IKCaP5RazejyJ9KZPg6dJyaOMuopvdy-nL5gHBgLjBxdZZPwEtUzyApUc8UWUEjWKzWQ8XtccnMraeqyzKZ8fxml93GJ8iHsUbQnUI4Le3XfnnGa20wusOIzdqrA1r1oOaBObkwfrtdQqfQlcoq0BajDyrj2zTWDoDDt1PWTGbgdFkqZeCORHBDoGNgMN1AZOAOEC9T9ZNuQ7OgkJG6isekcJ2KX18C8CPGttMuvR-HRsHMrOS8Whjn3SFXZ_vJ9RVCfcCsdJbKZy60GvmTUSg4vjWOy4i-335w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سون تو جام جهانی های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91211" target="_blank">📅 21:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91210">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmU4PUfw92iyJcd51kT4lC-zNpY2Tr3bV6ikW6mwIHoN1LvpvRiMmLYMqv__GjP1-EbcbwVj6hWx9fuHYIHOOgJco0SJiLwG0XkzaqZcUSi09_BUZuy9dgReW6msaxwaRx03DCpTN6JhTdeI1FtuJt_XNQJz3vfvBukwCB5kvDypjg1o3deCmkVdfs6UOuCx8ZsvYBz6PozL47ndVSI9RXf4G4G_Mcv_baQJMRXRcfeoY9VhrkluzDLKZ-mQcBoL79uBBJHaHhGSevN13tlkI-aEXcQIMDmFBZ3wFQ225XGn1-ICYRGypc__gycLQgqFP8xLRaPOgeS8EAavdxvt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب تیم‌ملی آلمان مقابل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91210" target="_blank">📅 20:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91208">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qha4r_x3KIkQxOr83DT689B2YP2vo97GP5apPilF-moB6Rk736sC2GOaz1GKJjsIF1hxDatIHPi_JdxYTs9OJDSe_axRBGfO_EsPG1hWLKbjb3j5cedbFWsdrwwf_XBvMbBLrCehZ2M6loba0xDRiTuhEPR6GdvNOc3FTompgdxUQdnP4zu55iUPViA1Tugg0zF7SOp-rBHKgquBVpfaslZqR38zWXAWSVlp0zLgzBwG9UuHouMC3P19XRnzGvO9xUACGCh94pmCpXbPuMhJ4rWTOXKmSfj1u7GhQodiPm2eyi6t5Te7BN1ao557F1bpVQG5uVuz0OXW2Ay4HxIO0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب آرژانتین مقابل هندوراس در غیاب لیونل‌مسی در ترکیب اصلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91208" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
