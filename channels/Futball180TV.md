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
<p>@Futball180TV • 👥 231K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 08:32:57</div>
<hr>

<div class="tg-post" id="msg-91248">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHHb4Jz7ZGu0mquHMYrI1olD7PnKfpdAiacocXH7pELpbI1m53YP7bo4759oDf_ln2oI-GbPg2w6aeYJGEuQRzBr-yPP3FKwSnFiSz3tGZt0H3PgFyFF1kVF8SxEGbPSy4zOHYg0ExsmHm3LFoTDU883YqEE3erwkW0H8w0kZc8457N-eMuR5zBm_9RaPsZiWLyjEBksxNfK2yLfz1e8d-e-_4KGnegJ2okYCTSls8UWTGF39fznXE-UzJncKQnM_q8GdvPGnZcVPGKZf1i7ezknztTbH5-QvrdAK1_H6fIpa6CiLyAEHwoNLKqoADuCdTN4My87zrdWnKUvGDuBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
هموطن ایرانی صبحت بخیر باشه؛ در ادامه فیلم‌های هالیوودی که تو مملکت رخ میده، توی ورامین چنتا دوست صمیمی سر یه دختر باهم دعواشون میشه، در نهایت در جریان درگیری ۴ تاشون به قتل میرسن و ۳ تاشون متهم به قتل هستن و منتظر حکم دادگاه!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/Futball180TV/91248" target="_blank">📅 08:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91247">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJimWy4l-UzfXmtPiV_9ljJ0QtbWhUe-2RnVpEE0MS5B27Tjr_-TOD4_Sdg5flRbowCoIMv-P4sKdLD9K6phDkNPqTGEexnAXRDjhMb7Yvn1JQj041VJ5MtXJmC8VnjWMhkpgv1RpJEuBFoJbUC0pAl4gpU6olcIqMrvCqH1MZYwbkRhv5zq89H46582decL2Q0p4gcrrXmj4MeQwnnP0hhc_bomynFO_BqAVTEMFUkY09HshSb7ESoskEK8Li592t24awkzx_WdFPPw1t1eDYyNmZkGoWLlLpJmZil9isEEhpxI1hsSCoL45pWfzNkWmhKf1FRb55CVTYoa1IHg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب آرژانتین مقابل هندوراس در غیاب لیونل‌مسی در ترکیب اصلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/91247" target="_blank">📅 07:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91246">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74203b9c2e.mp4?token=E3vZShbRZPhoGgPHhRpnhJDuStmWoQYfd6IEIWt3ZGfMOXQ6ANMd4M_2cTVaaeoyH9fqIa099yx0J5XWJHWPuZzCvJ9QXIufI_42tRCM_WYDIY69qGDK072S7vb-cRhoAR7WX1bbGXbQ0tPM4aMt6KWMCemi7gpAaVr1Tdt_7dgZUaw6CRXbZYzyjY67M_LQCk067-S-8c7gj894NMkAgNDgF7o6Lzp7ACHDGSoDmVPepvE-NKW1xkhnzwcX2TLLNG7eeimvbPLuF4LZ_tLIgAPlKy2y1kp1zy1Cu81WXdFhmN-nonsiuaB0sZSe7tW3R-7DUsEfh0q6bYnLVi18ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74203b9c2e.mp4?token=E3vZShbRZPhoGgPHhRpnhJDuStmWoQYfd6IEIWt3ZGfMOXQ6ANMd4M_2cTVaaeoyH9fqIa099yx0J5XWJHWPuZzCvJ9QXIufI_42tRCM_WYDIY69qGDK072S7vb-cRhoAR7WX1bbGXbQ0tPM4aMt6KWMCemi7gpAaVr1Tdt_7dgZUaw6CRXbZYzyjY67M_LQCk067-S-8c7gj894NMkAgNDgF7o6Lzp7ACHDGSoDmVPepvE-NKW1xkhnzwcX2TLLNG7eeimvbPLuF4LZ_tLIgAPlKy2y1kp1zy1Cu81WXdFhmN-nonsiuaB0sZSe7tW3R-7DUsEfh0q6bYnLVi18ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو کوتاه و جالب محمدرضا سنگ‌سفیدی بازیکن تیم‌ملی فوتسال از مراسم ازدواجش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91246" target="_blank">📅 02:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91245">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4xu5G6bSsnKZ3eWOcsx7EVDbXYf3KEfp3QKtD9qfNp5ZoEQzBp7sZosY4-wdpdr4elS1uYAX-9W8Ivg3cATrkhuL9Ws4qRJhT0uKi1azJMwJfhItbNHSVupasxxkb2sfi9ZJioj-Wd3uUjT2jQJ0ckpcIWxPrnJAd3BHAeC2i2PSeksuVOuZ3ub9ey-tG6l7MNaM3a9JGzyryPwEXvqenhuFWdXo5WfZha3ju3IiYi_Hp0Fmw5JhtDjVc5L9b7z2eABkEO0zaBnqYP_7x8E0tTR75csYQuPMzvYGgQz4HCle1JkbhiwyxMSDiHa1QSfEamtg_QInMba-1-7V0BY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91245" target="_blank">📅 01:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91244">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🎙
برناردو سیلوا: بارسلونا یکی از تیم‌های خواهان منه. چند گزینه خوب دیگه هم در دسترس قرار دارن اما در نهایت تیمی رو انتخاب می‌کنم که عاشقانه من رو بخوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91244" target="_blank">📅 01:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91243">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhtBQ_rowhQU_OlWu4dJGkqRUHlJ_M1PytdTN4u5CzovtShevFGA-qE6M4rWK6Kpo7eaPVA9J8BEMNIZTCmr0jE671glJR9sAyo0XIfvPle7zGHlC6G3yeJhTgiDXExhRqW0OebfvsDdtW6MmtMucDmndGCjhh0mHBuUVBZD2CcHMD-W5Jsnxxw3ERJyBK8xdvn6c4AQJD6rmYBOGOl72-fMJhz0etm0spydsuAh5BcUi2c1Ou8e0I-UWVemU_smcnfZJFLX7LPehfrVRz7YJQGQBroyyMEwKrLRekmcEFmaQJT88hM7IjNf2GoW6_PxiXQeYnN8oTLucoOKa2ooAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجوری استایل زدن که انگار نیسان رو اسپورت کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91243" target="_blank">📅 01:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91242">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42162246f8.mp4?token=auihacECDIosX5aU0jzwaLIticdxvqO0GbrPayLk8UfpW8m_1zk4KEgHcJbZdYsTJLtW9A8d0NhNwZlb_hprEpU_AQIsa92fiPVj363DkxFcyhxg9eHOAVyYo20E2iNUFa8P_c4LfGKBxnMPkN8GzaTGOG2PVdE7SCaZPqWUm5CPheJf3jV3-cmf28yF6yqtw9h8VmQoyePmAG-c8i1KxMPVrjrLyJjwEr_iBxd8f1GLVzATQKYjoW7VDz6lddoWdmVhcfXH0oTZmANmH9Nw5MACBBDAd42VaQeHy2reo5iM3av1-bYJfp-WCotgAS0vqmVFZEeALsz0YAJozT1q0KXumLotzRbuUlA2thc_rX_CuDWhK2j8a5S5uKmSC10qh8pzunOWDXrsh4JFrfJTa6JueSk1aiG59GjbOmOkIeKpB7UK2IG4CLk_X9ek1uVPalDgZlNV3iknWMb_SFlI_XerjXNH7inlm2el3jibYxepyFRgbnJEwFtq-F4aVtaVNz6y67PFzjRB8Hi5rKJdmInEJSP_4d56__o5WdbKTZR69q8IkgmoT0xKF6EbegWYKP8ssGXgOG0PPslirsmzz3R239jdVdbGV9nLh57azB5fhjZcKWjSKj6phRCA9oz3_Sz3U7XCddGHqAI2SVW3Du0CMYmU5BBefg9-aRNdH_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42162246f8.mp4?token=auihacECDIosX5aU0jzwaLIticdxvqO0GbrPayLk8UfpW8m_1zk4KEgHcJbZdYsTJLtW9A8d0NhNwZlb_hprEpU_AQIsa92fiPVj363DkxFcyhxg9eHOAVyYo20E2iNUFa8P_c4LfGKBxnMPkN8GzaTGOG2PVdE7SCaZPqWUm5CPheJf3jV3-cmf28yF6yqtw9h8VmQoyePmAG-c8i1KxMPVrjrLyJjwEr_iBxd8f1GLVzATQKYjoW7VDz6lddoWdmVhcfXH0oTZmANmH9Nw5MACBBDAd42VaQeHy2reo5iM3av1-bYJfp-WCotgAS0vqmVFZEeALsz0YAJozT1q0KXumLotzRbuUlA2thc_rX_CuDWhK2j8a5S5uKmSC10qh8pzunOWDXrsh4JFrfJTa6JueSk1aiG59GjbOmOkIeKpB7UK2IG4CLk_X9ek1uVPalDgZlNV3iknWMb_SFlI_XerjXNH7inlm2el3jibYxepyFRgbnJEwFtq-F4aVtaVNz6y67PFzjRB8Hi5rKJdmInEJSP_4d56__o5WdbKTZR69q8IkgmoT0xKF6EbegWYKP8ssGXgOG0PPslirsmzz3R239jdVdbGV9nLh57azB5fhjZcKWjSKj6phRCA9oz3_Sz3U7XCddGHqAI2SVW3Du0CMYmU5BBefg9-aRNdH_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91242" target="_blank">📅 01:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91241">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
#فوری از خوزه فلیکس دیاز:    ژوزه مورینیو رسما درخواست جذب برناردو سیلوا رو برای رئال داده. رئال مادرید چند ماه پیش از جذب برناردو سیلوا خودداری کرد اما با درخواست ژوزه مورینیو، ممکن است اکنون همه چیز تغییر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91241" target="_blank">📅 01:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91240">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF_q938MjUaSzlByYpNwmxPXeWAvB7N2sZgFTF4MkQSy9i5H_WkFzw4SsPxnYTFSSuPyY6d2d8_XpFv54A515efYtigp40epRHAwAJ25G4dRRNd0gMsUin2fs4TxJ1-Aq-tmLOXkOOqGgope4gHmsUdAmJqHVR0XDfpWucEBNknzKEhRts_ehBim0_1UlsRGplNP2NcNfGWARZ04TBJdiTnrP5XeKnkEzODyraVsY-UOnNXgX0-uV_rIGMlBD1JL1Z9gIPy7To8Y1p9nc_AzSQirl17BQTR5QZcQVi5iotnC2_kU-gD9aDGHaGY6c6Bs1T0Yd8me1qjhy042wXYpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فوری
از خوزه فلیکس دیاز:
ژوزه مورینیو رسما درخواست جذب برناردو سیلوا رو برای رئال داده. رئال مادرید چند ماه پیش از جذب برناردو سیلوا خودداری کرد اما با درخواست ژوزه مورینیو، ممکن است اکنون همه چیز تغییر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91240" target="_blank">📅 01:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91239">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBJ7Qm-hjmULXCUeYGUIBHTdNDlM16GDkJkA2SYgeduO3FFiM98DK-idXxnyG_b_2qeia1QqA4L6k5qvhMN0Luy4Hx2QpNE4xQudJ1-dsy9Kher4Yixdgq0q9rhszGtb72P7IUbkmiomojJy7rP08rdcLJwChB3ZjoKADur36U4Ce6PM965E-Zri8rXLrgod5kikNFq4Y3RnWBQXq5AJZgdvVzKZumEzgu57Ylv_76yOziPUjw4QIR1Fsp-CzDtgjKoovwPKYyZrOMCJEEzWa9LtE9biWeUT3oCKgsza6BgKKIySnvS2yd70RkSYpPafIw33NXqbjzY2NsqMfAsPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 روز تا جام جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91239" target="_blank">📅 00:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91238">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f6380c33.mp4?token=b2h9_9ocblceELWgePWDz_GqBOwfnBTM_cRQqRpE4G-JFxp2HL6JF7n0ufbQclFwTctCukDEEXtDlyoiiGCr2ZXPeGx8ziPsA1ywLAaznyACEyoykiIJ6rRfL_-IBH7Vd6PO5qQE2AXodyz9uP6_3UWHH5EKEL87tTautA82PveqjdP8bywCHoyJBU9yZAvD4ARCWAXAQVkEqnu_WTf-byKww2vhmSErNvNAUnB-w1RceHrV8RVpYmsB9GcUIzHU0-ZpmkoVWMuQVuHud61GZ3LEHCvyzxWmZ5hRWeCmCMzo_b1_ejVPbeSQ2sJgeB6ER3U5AB5OJFwMkBEZuSSSKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f6380c33.mp4?token=b2h9_9ocblceELWgePWDz_GqBOwfnBTM_cRQqRpE4G-JFxp2HL6JF7n0ufbQclFwTctCukDEEXtDlyoiiGCr2ZXPeGx8ziPsA1ywLAaznyACEyoykiIJ6rRfL_-IBH7Vd6PO5qQE2AXodyz9uP6_3UWHH5EKEL87tTautA82PveqjdP8bywCHoyJBU9yZAvD4ARCWAXAQVkEqnu_WTf-byKww2vhmSErNvNAUnB-w1RceHrV8RVpYmsB9GcUIzHU0-ZpmkoVWMuQVuHud61GZ3LEHCvyzxWmZ5hRWeCmCMzo_b1_ejVPbeSQ2sJgeB6ER3U5AB5OJFwMkBEZuSSSKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🔥
پیش‌بینی مارادونا از قهرمان جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91238" target="_blank">📅 00:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91237">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkTh6CckpnLeWrfTkvGkThsfua1HofxR6YSb23ZyzSvX932daXT9lQgCyjW7SplsOzoKXzi3E1-y2bYsk1Py4l6OuLUkwxsps4VA7v0pQv4G2coOnwMC4L113HaxPjdbPFpD2ZPM0RSiZmVfIJiYi5ekFWPXvO1dHskC8b2CCAgL9fpO8dAqaR6Hj9l7E1vJO9ss4w0p4QXm7rvsgphhUOBCBJmzd8uLb2XcGPGZ7Fno26LSYox_0rIaHLg7C2LuIcbsRq3jgI5n0bko3zhsmSJAAaJ84fEA-0VAABRYAzNJhe68d7NyA0S-o0zdAZrvx-G_q0hYQJRsqTpuVzodnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پردرآمدترین سرمربی های ملی حال حاضر جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91237" target="_blank">📅 00:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91236">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk2RND1_OBLBPblZMbVey-M5kjZBpdkmw9VWXpbfddJwaqP-GJukxLL8d0aI43zVkUnLpb9_uucIhTFedKfHFyCRvtRdh6_1U1nwW8PcxZ0Ro8VJiwSlhwbGhRdwzMQ7hF6CszVLawxA4KtaCVgYRhdcth5NlucxkyA3HSnyf07YPzKa_U0BHhCS0UEy5mlSsaBr5CAp0DsJSC2qEAm7_iyTrZxzY00uK2BM-6ybOtm98126qVYjj2vUSED-P_K87joM-DgIVcSCRFSxgH92oAulGAXlJTqoUQXDL0YsSShdiYV54sZcJoWIBU6EJmtAxQZevL6QbIBqHTbTp5vpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیلور سوئیفت و شوهرش قراره یه مراسم عروسی با حضور هزار نفر بگیرن که اینم قیمت بلیت جایگاه هاشه، ارزون‌ترین جا 8035 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91236" target="_blank">📅 00:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91235">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🇦🇷
#رسمیییییی؛ مارکوس سنسی جانشین لئوناردو بالردی در تیم‌ملی آرژانتین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91235" target="_blank">📅 00:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91234">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOh00t2V5y_j4m4OHl6qBkHekVo4ckhJiUPmTBPkr0rHRQvkV17BcuFHGSAmPUlMrtxuZWqihImX7Y1TDh-AHIfJAEdz9bF69N7kGXw1jc6qzhHD20KP2mIKUNDAsAlIMgy9CVQ4xA2BMZhYUXNRKn-F-dMJMGLf-xli92oU9fIwBoEZLcM38W1Iu9io9TvoJJ_MVgGdQ3KyWFCksi81pwqCiwSX1xwGt17FWE26eXh6zaGCTPMTrSxwIjlEztXXxmMq3RV7fUxRHf5E7D2l9ZX8TGoxhGJGy1Eqs78w-2jCgX1sUmHHZe4oHV7SlcODveTWyYjI-nEC3gOvjdpJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
اعلام ترکیب برزیل مقابل مصر؛ نیمار در این بازی بدلیل مصدومیت غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91234" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91233">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea39da6f0d.mp4?token=BR_T5B1ulPDTvIbLIOHVF60QlvWgnR1oY7MF20_5f0Ae_dED16bNoYvtXP77qO0ALcYbY8b6OqxpMea4ydGYIUrcivj7YTTQTuoGNwzCWGmBw5lkNocHOZRvhmPsov0YUjiq7ojvt5Fv1QQQjEMUVfXz6nrk5ungeRF3ieuis1hPRAHGJsNmiovYVIXTRLvoSMMFKov-L74W5oEKePEkwJiFpGCoCj0OHMBLUOITD2im6ZAni451SjM3k6Ah1ec0R8Uc-b1ywWvfFQcC1Sba-PVo4nK_UlJ1sYJBy4JlN3xxAWXDD0bkPXDL1FlqlrngZgVyliE-4aP-VIUobacVqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea39da6f0d.mp4?token=BR_T5B1ulPDTvIbLIOHVF60QlvWgnR1oY7MF20_5f0Ae_dED16bNoYvtXP77qO0ALcYbY8b6OqxpMea4ydGYIUrcivj7YTTQTuoGNwzCWGmBw5lkNocHOZRvhmPsov0YUjiq7ojvt5Fv1QQQjEMUVfXz6nrk5ungeRF3ieuis1hPRAHGJsNmiovYVIXTRLvoSMMFKov-L74W5oEKePEkwJiFpGCoCj0OHMBLUOITD2im6ZAni451SjM3k6Ah1ec0R8Uc-b1ywWvfFQcC1Sba-PVo4nK_UlJ1sYJBy4JlN3xxAWXDD0bkPXDL1FlqlrngZgVyliE-4aP-VIUobacVqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی داماد فوتبالی و رونالدو فن هست و اضطراب اجتماعی نداره. خداوکیلی حرکتش شاهکار بووووود
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/91233" target="_blank">📅 23:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91231">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oV0pxiYMrWDDkxozU52A_IYQg1TmrWv_Qee9574iqJkWJ2rvF5VCdi-HoWHa_mafEWlysQYcLlX0JEmSjir4-c5vzqelZxL9m7N9noFOGEk6w5y4XOVo3d7K9sSVE38_J-vQDGdxYGitc2B-mNKueIwgtSd548XI4pRPUthBDBbBCEWsLn7-G26CXDFQ1AmeefC00H_Ma-HOR6gvU4026ydwTbWY7rv7nJzUGI42nBmD9tbD1WbyfkQFa7T3soBg_9oDetvVPqq4VTaOYIywKiHKhSln_yicyxBlC7ET205KxL_RZZh32hy2CyCJiMQDYcaztk6bkqm86voMGpUVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
❌
مونا آذر پورن استار ایرانی هم اعلام کرد که قراره به کشور برگرده و مجوز داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/91231" target="_blank">📅 23:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91230">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a25be77cd.mp4?token=ATvGgr9nKPtTNFbWhhWorcuSnqAu0-kkEUAUQ4Z18xBnSvltaUnjP1iHPdjub6nwlGBysTHaCnbXIebl8_lnHqal3tA8RG60uctts2pd891DABldB3FLf8gvw3IlOJ-FzR7F4kYTboQFynfMRL0xVnCYK1gpBp1vhN4UC6i2-sFwnLYU7aqcwqk4v9ZjGIh0m3gNovxaM9DIy_Yo3lX1wemOaJib5o4dH1azpJ3Qr6HQMWEqDOxc2jQueAzGGN5FV3PVonHgfRBQkmM3TW866Ge6sU5GVgnSeiHb1z8_f0YZuwXulvH3_N-S-d2qoBLZ3l3DMAV77xHIQoFTxzr4eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a25be77cd.mp4?token=ATvGgr9nKPtTNFbWhhWorcuSnqAu0-kkEUAUQ4Z18xBnSvltaUnjP1iHPdjub6nwlGBysTHaCnbXIebl8_lnHqal3tA8RG60uctts2pd891DABldB3FLf8gvw3IlOJ-FzR7F4kYTboQFynfMRL0xVnCYK1gpBp1vhN4UC6i2-sFwnLYU7aqcwqk4v9ZjGIh0m3gNovxaM9DIy_Yo3lX1wemOaJib5o4dH1azpJ3Qr6HQMWEqDOxc2jQueAzGGN5FV3PVonHgfRBQkmM3TW866Ge6sU5GVgnSeiHb1z8_f0YZuwXulvH3_N-S-d2qoBLZ3l3DMAV77xHIQoFTxzr4eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇹
گل‌تماشایی برونو فرناندز مقابل شیلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/91230" target="_blank">📅 23:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91229">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZJ-bCSMGuqaCcK_0l9hv-S3dg5J9AHqRYpSImorM8DQKoU32XNcYUXGreEYd5ZVKR-BgHiQY6pHtOF6MYinpfDvbI3Eb2RvVFFgkIvjzYfSfNpWxhEFqM5Tfngkrw2sGo9mOsKE-JSKvRtoBGK_Uln6vzArxsIRFK3nroNQ0MdTvPhgI4xUSv10ymhNXBVsePTrc4NFJXJfbdwZd4YMZm3HaFzTtXhV8kPs0iNZfUo9OkL9FHa-SvT48jqUOrPiR3fCz2bgD1423MSTKunnhCj_9m5wbyxt-gSdKsMIV07c7daQWpxRaLYcabbZcxfluZ3fW4G2xWKkVhx-BofDhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
وقتی میگن پرتغال قهرمان جام‌جهانی میشه
همون لحظه پرتغال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/91229" target="_blank">📅 22:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91228">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1050253ed.mp4?token=swLTd3OVewH61AE8Vpe8QcV2Tb86vCzBrxH_eHpfXVa0MG5rfKXJdtYyExOb-6BCZgNB6yc2EaHxaVXqtx9gNWA1UoodGletuqCMzNSAcjcCiXfXf8YJbWjg5sCShypO2BvdzRD7GXD1QAX9f1ymjED770gl9AdHMZVJhzMCurb2j2RGetc7o_fdPie0KngI4D-11GamCAqCIkdgiecU0zPXOPtu3NPflPqx3SILCnMQfWtTtsuGKR1iPz-nvUAiY3s32ftZtjSefnPW-JV2UzEc-8KkutJEIpYNGAg62CEgA8IvzMtFZk61-_K4RpjP1zbVMo90I9wXpQhceSIOLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1050253ed.mp4?token=swLTd3OVewH61AE8Vpe8QcV2Tb86vCzBrxH_eHpfXVa0MG5rfKXJdtYyExOb-6BCZgNB6yc2EaHxaVXqtx9gNWA1UoodGletuqCMzNSAcjcCiXfXf8YJbWjg5sCShypO2BvdzRD7GXD1QAX9f1ymjED770gl9AdHMZVJhzMCurb2j2RGetc7o_fdPie0KngI4D-11GamCAqCIkdgiecU0zPXOPtu3NPflPqx3SILCnMQfWtTtsuGKR1iPz-nvUAiY3s32ftZtjSefnPW-JV2UzEc-8KkutJEIpYNGAg62CEgA8IvzMtFZk61-_K4RpjP1zbVMo90I9wXpQhceSIOLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
سوپرگل تماشایی آمریکا مقابل آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91228" target="_blank">📅 22:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91226">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5RJWUVNK_EZQci7B1KF4X7EpZWqmHpzDHoa127InHadAoUhrSTEaDo0Nx9NVZb0SyP0kkdcsNZyA_vB_O-iQSZTIcjGjei5-d5neAUasEUniSjveoV9dubZGPC8wVLUdS3w5CdS-prXTrVqv8OngXRp-8sFoOcXdpVq2_4tipJled_tYDBjkcA3UqSqfUmcxagdlRjChoKuixkmX_BsRKDcTOIm5OiO4BZ4-_Zo5iyWhM36eYK6PKW4UJPaLWCv4HrJjHfJdywXzmMGDQHHynKfdp-Xq9p1j2PJdaPoQjGOnrEFsNEZ_rvKLD0Mj7uGVkoZlmGpzqoTt8APXHIA3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ig1yLKzE9JZ946dlMPIVrQF_DwFx949vaFjnNEe_ZoOOXQKZpYXovzl3uNV_nmpAkd3Zo3pX_gI_Wau8e12mbSru8Hvfx0eu49Ml2JWIHJFk7GBfyx3EUONlTaIIEyntkLqhxhIfc6VoBi0qm9H6XF2jqNYgZZwh5ZB8dBQ9JD71NRZ2bKBXse3Xj7LtuRCQm8QTjDmhbASo4LbOW27xORxAv4Tbu4sjxQ_fOnnWhBEXTp5Syps0m5EWc-g97g51i6xFQ1g0ByYq4CpFp5PpiEeVRlHBfQPvoZnBgvV3wexFrhtVKqM3c-ASeMgU-7gZgfmAM_T1ecPNH3i-wN6_Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🙂
🐸
ضمن عرض تسلیت به برادران سرزمینم ایران باید اعلام کنم که کراش والیبالی شما یعنی خانم آیتک‌سلامت از خوبای والیبال بانوان ایران، امروز رسما و شرعا ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91226" target="_blank">📅 22:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91225">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saLgKR-noc50Q8sZziQViv38JQ5ntjjdXHIY5k-nIgqrrLm50rZrscQb9jQ05RqUhPLMddfSnofwa7L7iLLnilFLv8coeafpH6l008pMkvsawVHP9Tczk5675rZuv9M0e7hgzxnPY-vy0umGMC_LbjOjL6r-JYp_GvyompAWZ4tRFbrIda0KxHuNahRNmDJ9E4FXv9SsJp9AzUNh7aiHC8-SaxAWdr6IdrGQWAjPbNnaIA2Twr5SmpcFmDYQVB5jJ_jNayELSPnB2T1KPwfqivMOiBjtP6FqxW6lPHQHt10N3w3eYyus3HWUApjsU3t4NMAWy8oZFP0AUCCps0HKxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91225" target="_blank">📅 22:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91224">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIexZwL1CIhoqCz9zfKpIEbdVF_IoOCzg472eGw9eAezVjpsrB9oVFPPt0XdNl6jvnPljvl-RAVgWYnHTCiis7IrI45gRdGzFTmuSwy1L3UAeZXHVmElyK2q6rpBRT6gEgNx6hGrevh2CTxD5FOZHM2HUvrar9v9LX25p6kTY46jHP0vSeySxBE4gTP70a3ymW3jxXo_jwyYeZmElMoJqackEMKdy0RhvA6WMtS89l7R2kQvbpYS4knyYJdZUyhVa489SgMEyLrryRKW-c5nKwcIhX3ifkfTTlbt08ho173iDeUGtPnCuDHmPNOVME47qKRDHE8Zm8ZwAOi6yUnNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاماوینگا بعد خط خوردن از ترکیب فرانسه برای جام‌جهانی، پاشده رفته هاروارد برا ادامه تحصیل
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91224" target="_blank">📅 22:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91223">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVNLVbUfy4rNO233CakgDUcgMSf71SDFXGIXp1iOVQdMunC9I_gZRZ8LWWGmhiBtC2JnRvqhJonwiys5CK6h9VUQfGO4U2F0sE4RcfIJjgAaJPbwJFfKyf3NyPhOdolDr0IvnXtxh9bjucnMep0I4cu_K-6hVbE81CcMRzlJeBmnA-1zlq2ZPcOa5CNAN7trn_RZ7_dyyOEqB0higo9VxR67UDyRPPMFgtZVkr_Q5vqD8YCAKRSzEzhntkK7-HoOYz8Lm1Q7pjIvAue39jfEN6Q0uFnmdpQyc26HYuRLp3gTCNbWzh0N4PH9KPgyrjlrJsCMC1iO_S9xru_o6I-0zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91223" target="_blank">📅 22:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91222">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csMLWUt7LvlO6Ne67vsWIcuDJQ024zwXHW4X20U2DMvzJtBl6Vv1M0IDTghFbff7gzFB4snp6ZqlfbkSpFWbQU83fpVXUQ5Y8nQ91n0c8tVH3TzxlHcorniJqwiWa6EIntluJLsDZ9tVfY5IvFqO0xL3fkarR6kEJcEZ7BpUXmIa3puBZJHq5sbMalvwZqRzOFNbGmtCkpbQO1XXa9z1hbwr74LrTPBunxzKAlXMD4IFzhaurpPZUqSaHj2XO70lM-Zp0k3Zg6q00mSKcbOm3Tgo_K13M5dNLNj5WyhXb0o_QTn1KJBmiUrXmrY88oAUIYi-pDDgyDTXnpdFRll9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیائو با این کار اگه نخواد جام جهانی محروم نشه باید نماز بخونه
😂
😂
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91222" target="_blank">📅 22:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91220">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiMUORr6HWfoo0UvwQhLGBS6bVKhemtKrEV4DJ23S4eIKjAqfY2a6u6VjZccG7obsSYr6K5iqKaUJEuztpVGaYruCLmMbX9DiC8lgNakqs-KzNzclEEjq-Kz7Eo1lsPddAQYB-OsPqX9_rqhHd1UJ3z2wSdVkIYcRCIsI7XHVpaEAixoVZR4KGk-afnNZD2H_kWpYPRi78SAJVXEBwSHllDCv-RmI_2uDXnieiLpHEAXjHSFPq74ftH2RHBnRN9LEpAG2bugKC45hG2bwo1EhCaRO5KkLFHi6f2lVftDvSACXE5Zd638MKHAF7HvEwP0CEoEh_cAyV062czPcVIiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکاس تیم ملی عراق به جرم همکاری با حشد الشعبی پس از ورود کاروان این تیم به آمریکا برای جام جهانی، ۱۳ ساعت در بازداشت بود و در نهایت دیپورت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91220" target="_blank">📅 22:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91219">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3LRoosjYGd76dVlwcGaSiZGy4rUtpciyYTjtwoKQ8QAZ1JfdABEBKLJ0seoWz_kgQddlBtozZGMykFP6jBpaOqTE-ij9_ra2emHK9BLppkNY9eOp98ptJzO2fb-VJhJg_kJB_fPVn5S5LfuVoPff9XTpnyoZy1RpoOQqO6b5mKxYvyWhSTkfERaYQY1aAI3-yLG4S4bwuUw0e_W60Nj5N69Ydtmay5mpI598njgM5AR8NU4qJMsTHyokRUDYELXGSPsZFwpsAXMCmzLjXflamYFPJvjY9EaRj6eRTMEpL2dtJBIFrQtQH6_XCwzM1zPuQ1dRj2ke29mTh-kmiyLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال 1998 مجله بزرگ FourFourTwo⁩ پیش‌بینی کرد که دلتونو خوش نکنید چون دیوید بکهام سال 2020 این شکلی میشه اما تو 50 سالگی این شکلی شد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91219" target="_blank">📅 22:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91218">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuykF0YnpAu1c9uFZTjEcI2-HMkMM0yHT5T328Hd24iop8IUoIaBzFgXHNwzd_ke9stRZd_IkYuCCGBvUUHf7jqgjikq_fN3tbrk3zcrnSx-aHcvb2KnJnXUCDXgd2R8KeLBvyJCk9t-2FIA6j4cik1aJk19rPzpO64oZgC7vXFJN07cRpcdVqmFMJdgunQuQFhxe7yK-rb4KQ_Hg7ScOwV0z2FqEO8Qym7RMSGIk7FUiVeSlMzhZ679Mw6nklpCHsBqoXv7ToOjLqjGNjXHdnp_EKz2gX5mehG-Z9S4ZPXpOH9Z7-HMOru3WjrkJUJnKbHG3HHqO9VIhCSY2-jf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناخودآگاه یاد اون عکس افتادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/91218" target="_blank">📅 21:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91217">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUzsxuMKKUVHcha-cg6kQuffn9G010sLwgcZ-pKB0ClOjGZ4ZwD_rPoMyEZ5hBJbKRIwM8_Xvg7fQ04Kufyr6M7eW8UYbK61jsXuuTnjkzcaI3io-dYgDajXO7i7cE7uuek71DZgYjQiMV6sAWS99_2zLp1fFYCJ0D2ckUvtmpI-KHEnJ6UP4ELLixaQTf2kTMCZPfFRUTItUQG0nKJL0vQEFmQ9CgyUhn8LkUnqqLGmKUdzJ2qv14-Q6yks_p4ey56iS8niUITaZBNDY38m-UkSH1hAEdxoKMVuKzY0LzbswXYeLRvyoK8asR0KE5eYF_Qthd2D_dJfr3Uc-7RjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید لاشی چه دافی مخ کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91217" target="_blank">📅 21:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91216">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm0F_tnZEjK_pxrU2lSZaBJ3KtF5NstRi2d5AGI7FpBsdleEcS1I5uXSAUDDoGzLqY2SfRQ2TW4B4MRjqIdvqF5xcHHzxcqlUF0y5on8c9ksyT3Vza2EWz8Il7K6OXiQzE3VN53ZP647lvQJhjDOIoJAbgEpyr5NhSGBRkXaryldXT32yjX3Eqqj9PNPpP5zVhRQ6j0u8hbuAARr8iLvRkmgeNJimTgPCQ7He1QCWtcj0QLlFbqaIeyYqap42-0wrf5ijt0CzB2iKxITOdAgwySocjMGxNbjHlMLCxhGinAchDBKFXtu6DGVmtDPsq99dw3o8yHOuSxcTY5p98-WYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اولین جلسه تمرینی تیم ملی اسپانیا در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91216" target="_blank">📅 21:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91215">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vH7Lq4578wQeR4KeMAt6YkcdAw38ZT2_78pFdAqAaxsywhnzfVXRX1dwa6YsOM2nIpa1ZfljYuJvt288Jod46KTzTzxhTy9YWm7U5gfVqhQNvSbyhg0gWkbWvpaLUS3Ah3aFLACjQ9Jab9VSW0ObsLg5z0xPny6yO7NJwT5iyzHt0hjG-TblGo2fwLalek34-0gcMc2nz7PJ3uly9zB1r4Ts7TEdxFxeqGpA_QUeC3Ci1uKgfcMcH-DT3F9A1zOhySjfk6Q4PdsW_kvytjqBH-FnT5JACsg6FALU_mtrl_V5Aldmx9vXapvZk2afG4PZsRajD55A07hoCzaDHXewig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنری کویل یا علی ضیا؟ مسئله این است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91215" target="_blank">📅 21:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91214">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYJsi2CxE2zXrK9_7SJy8LsY55lPzxSycIpX96-BvVmFLHJzzX_gkyE7WRpoehPLAEQd2iCseO07tZHcvLTP6K3Hgs654icvFLPx3RK41ecJShaGdOWePtQDkhBWbYF1NuZy8-mAihnr_nsHCql9JuD7YpBCWalNjEOnxriJrHS4b2Dw5fx42D3j8kaHXNXDyHSXqP6Es9L-Ytx_a9LWOVsHM4AlMLCbkoi3gUiMaMz4rBE9QPHW1HUZWdPTg5BKy2b9RXHidMWfLY2AGnhoHHW6v8kIQcx57B0LE8L6uqYLz_aDbbU2d-7L1MZEqPFevbvabE5i8nr6nPRNJaA1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91214" target="_blank">📅 21:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwdYMldv3mySnsJkxfIEK7r_lka9fa5XveecbjzuSufFJJbq_T5oxKuHl6dB1z8uYzyxrIK773_SP9poFgSUfTxkyYLQvHCBLA88pU8m9sSG7pHctSWshghQH2Zj81qKfmJgQJphItUbq3iPoqg8WolyitgJM42YxNDfl5ekDwe5NFFUP3Lj4Pq_tIX5mCT-gRtCLqf5S3frPA1qvb76CHB9f78bILdYBy7C204mQhemOPBbDDgrsAO9xb7lDBd5LA27COeeuP5z-xb1dshDz1qhZOCGB3bOuU58e7GoK14CO57DuBbxkG0AHdjQXhgnW04kODHzk8Wa5oxaT5EgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZSia1NRDIM80WACqy17X0MtYfTeTdBmgp5bgxnRS5MiBBgrsVHm5XQA9aPdTxcTvT4PASF6yvf61xeSEy0mGJ7BDjCEV9Ixgnr-WvaGDwmhfnZzsLmjU-NbMXeEdJ3lEfhtZdld7Dk78NgKoOR6HWtzediWF-pX5kCht1Ut767vBjgGEZLNtDgDpSIcn1RL8HiGRktF3xK3Tv8fewEs88LpqpHK1j9K6wUC7VupeFtQOfVIoMIgsZadMDfUukTx64ENyf0kvl9e-ilygrUjtElDjt8gW1NRa-p5z1xY8yWdZee6pM9RP0RSsO9obS2VXlcnnqkGJEsoWCmqJLr7Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91212" target="_blank">📅 21:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap1dnTkTXsFon0fjv88_waGno111j2Nh8P86fIbRGL_9K5SEACoIm7b_ZQHj6RpcW_0yW0cuulMt-KqdG-Vp2Yx1hjkDKp7IngWuRAu5ZEiOLHNGTKT0nRpe8uFekkngyTtyhqO50JIr31Fc0xpPnboD2JgYAEBBYTKooFMniSA8cPyFhlIO5q9rj-vL_OobgKM4CtTUCsG1hQSwBMUYgkcDcYADAQP0gssWTmkfREdNJ_CGlm9qrBvWGoW2ihM4p7v3XnxxZXCEe3kL7d0vdEvaXdo5Sinf4qzHgwjcQpf6UfV0ZdUMgyPY30Abg2BS_dfYLB54o3rS0Nyx_9ouRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سون تو جام جهانی های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91211" target="_blank">📅 21:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEJGa62i2MyUGM6H7__7KoO_RPTTttgMRVOXXmuANs7yvGA2ufqPy_3g8ngOQFs84uDS3T4niFXc3gT9uHo7uNFSuASROni8jkwH9YCiVZ3mflWegvCFh5syM7BdM5hKdPLQ-U49O5qqws2qnr2IjdJ9-mR1Mk63DJ3pE5v6b9ehObx8A9pAg-F8iwJ9TCT-9u4DhmmkkeIS_PRPV0uNGtU9qIUPNIK0SDvm8ePHRlhBCXup0lV7W9x_fNeBDc6EABdWJQxLpCoHZp0v2ihdUA49c1d1UKve0TeTqKKFu6S2NUfT4gxAnN9Kb6bazN8Hnb4-JiRyR-d7E6QVgWJC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب تیم‌ملی آلمان مقابل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91210" target="_blank">📅 20:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91208">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZzAMV2M9okJqQJAzAA-HSvok5oBuWdKdOqJwjpXmJFow11-IY4F60MGOPrTMSO09fHqOj554t7_0x7HjxeSTM2tnOBEwseNSqyrkGwIGLkabX7c12Z51eowEAMSVQZTwGMb6Z3wfjLo0QkmkL0LWuzXgZ4Bfd4luX2UQypEtx7AiHT7TsYVjJcK3Ldij4l-f57JnDW2FdXWoK_UUfBh2Rt13h5FFC6Vg2tGNBkZz9VgW-PicF2OttKgNc98EGE-hYeJPGGrfUWUs3c8pFcdmhCUOTbrGn7ijRRfIgK9WKvHbQib8FSDOHAXz1JXVxW5ec8e8AmBu_uhqwuuVmoQeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب آرژانتین مقابل هندوراس در غیاب لیونل‌مسی در ترکیب اصلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91208" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91204">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0PvR0BjFWfCjANfYsfu2zWQsqpBzAyehW6h4I16viPXiCeBx0fqa5RMKNaUJ-BJ2t8zHPSLsxe0V6COlteEmTOfBODRi6BC6e23K_cs4--xm5naplASsihEQKJJmuM89sQwicaXX1PgkD9J0A6cvarTMKrqjjQ-oZmVOifXNEaaac_3cPzwAKAv4lZInLuSLn56_Suf3uz6tYSHaZhy-qBJA5oxa8BDOolJgO6VWARJbFK_4nGpBnZkfDu4bjhqvo0aBDrgXclzU91oQTKNKwe9DM3zy9dDlTyIKpKw1dQaQRzdx6qJJa_cFD8X_RyA1LqoHc-XKTtq7VX-jBM5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGVYEmBKhfhtgL0UNsBLyisCNJhprD_qDab9zenLmcU18PmpXh_OBt5dhbspCj5n2oKFhTTeyJnn4jrUuSz64CJOO9AQRFfqHAkud6hT-oKx8ugqrlm0PTRLtOiyxIK0_YSqLzuQmDDgG7Nh47MKNVoJVQSJ7WeveNyARfo8I4JqfbOgxm5E5VXmE0qEex0ikSL_GdoUCgO-Kd_nPfaI53-mK37_2zd9OnpLBRpnioAn2wDRZOE7geiY1pouvRin5qJyE3N7MI3sbVgoNVppXPsmHIBF9n-fmwFxQ4XshTyZ2JP02Lp1sxKDkVt28K2_Bzcx1nYk4Xh2MZ6xUAD5cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veQJ72ZKNYu1QmmSRH5mqdotwwcsXRHTn8hlml47tvRp14vwEU0eF4Yyly5urUfNcTXUwQOpzCtRIl4DRWKsOvxSTPIDcgRNydXmPrjn8uiGplOhInWuX4_XR-nF-gcWw9QUwKGftAHR1wlOHTJZD8miriPxEiJtY2hY_twiydZ_sXxE4JKzzjhikffcJNoU1IPufbRTlYE4q7Msll6C1YA3jsIiwXixDSr692Lcvk5xvvLvLZBCHA4I2Fa33KCaLC9yst6JwU4Gh-MyvyHN3u9MFoeqZCx7ZyFcIrMF3NxR4t1044fYPMsEi4nx5RQBySmkW0ko2hyA-_XMeqK2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sg_MfaiIy9RY8KybuaQHExDeet9lM3tyECZbti3nUJZhgEdnRC-PR0MnmAufWuqHteVnY02990uvzBhOBbVTj5x0ENb1wAJxVsP_ycYkkwG0XfKJnzykRdgmyxOVAD0ucnq1YWGMLgyeY3a_NaBAATbFJGEcrf-i_lrjlu_QVfPt4kxCABrbKPGqPwzZv-AfX5FV15MZocwxxoSORly_5aAuP2ObVjNfqhLgYz0DW6dn-ItQbZSl8N7f2TBgxeaSJOCDjWFKqsfn24TBgzVY_6VWbtghNZcf-gi0z_5nWDw3sAsNirvJjsXPP35YlAIk9a1aK1K9NWg_CCpjVJIq8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکم زیبایی از ورزش شریف والیبال بانوان ببینید تا خستگیتون در بره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91204" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91203">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye5y02TQk3fpjeNrDTNRERwlWfGHxCMRIIm2B8kMm3Ml02iykUmHEbvmdbdDbGgGmWUm9oaI3EHZf9rjWqsKYR9-k613WQzFjiCscNCnm3ExQ0d_SQZ65bQNj72ST1_BtTuu7yiwYJj-Rv-gHmQ4OHKOHw1r_kAe4QTba7OFpIQGdFUB3pMkHK0u_L3AFj21BuephScIJS9R_DkYWaRSXVgH184UQSaOTMBijHTSMsmljscwFT1PAbsFNWo_GdPcHCF2ZPwkAojiUV4iRvvKTpGNJn2GnaT5kvK36wdSncUbr_c481il1gN1kLOGNH21apSbLdZKjnvrh9ewvCFpDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ترکیب پرتغال مقابل شیلی با حضور کریستیانو رونالدو
؛ ساعت ۲۱:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91203" target="_blank">📅 20:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91202">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D06zl9z2fKC8uzHMBS41g-W5zVnPis_QtKAPR6iUz1zkJ8995r8Iw-6yLNxsIRnIGzBP4m23WghN6oINtxfj3H1QcWh4F7ZKxweRn7yJlEADFstzSKybiyN4swofjrs78N4ig0u9iRSBSYdc4WF8qUCBG_j4ChzoiQ44MEklKa2GyB99FVY8EcMI_yMI9_uxrlnyjEcc2_HoRTI4Iw2SJyIk2bz3_Xcs0OCOTM-rm7ZrW9Y_fp34G9Y-GZBFpYS3tfZ58LxGuuPxvZVqQ9RFEKz2p-IKzWSJ_ihs5ouKzJgTw6wq4zVvFeqkzhg5wTwahdb62NW2tduKffR1JgH1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان رو نبینید برای آلوارز 150 میلیون یورو باید هزینه کنی، یه‌زمانی با 50/60 میلیون یورو میتونستید اینارو داشته باشید :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91202" target="_blank">📅 20:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91200">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VU1-mIo_21j0jkjHWue0VuvG-Qeuyr-chSF6Pww9qVJPNnirUMI5_W5BzP-COo2ggJetN4cNyB85rw_1wHM7cGNfjo-TZs7jTnDoyaG2YySiGjqVCeSTcMxHA2SMZGCh8ahZ6a4c_f20rdovoFyotwHH488qgQT3MRvVespxK_U0l2W56oMKH46UFq99A3Mhkq04tHPVMRysq7dWR_jWlvU-kXoREhSepSMK35_0TCMoSk4J_fgt2vPFtaHBBQcIeuqE3Vp-FMynYwLNDOvZ-K4lM6oXzPJ1S_ad2FH5cOeH3c54UQfaC3E9XZzQgjicJqX-fLRuebgO7fVY2FvMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btkrSah-t9-6Kbn9x-e7JbnWCAZi1Ti-UR8XxVRXLY7rsE8fWMMssT1K0E3l5sf_ExhsWS0UMhAKgBaCpWxiPxIqvxuQeL5aes4naozp3KNRAfvSIlfDuUQme2ABCflAGKQRPoFVqm73aFIBqmfDn7qUx65o0RAxRg0ATNDLoE_K6o7gfo_SLBhSE_zeYGLUMwfhrVqEZWLVhA-VmPozPjIHvaewYRdBKGkElb8BhXJowrL8XwYQfydq2kpV2HO47SxbjujjRwIoxy18WE91W5L6xm6ez1Qhm_KHfK2Y8mCvA3FYw_vc3Ss1hbdkmeKWEK16BkwR6y1dGuUkFI1Nng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🤯
💵
طبق اعلام مجله فوربس، ثروت رونالدو به عنوان اولین ورزشکار تاریخ به بیش از 2 میلیارد دلار رسیده. ثروت لیونل مسی نیز از 1.1 میلیارد دلار عبور کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91200" target="_blank">📅 19:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91199">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdd5cda06.mp4?token=Oeq8dswyE6gUCSOqOhP8_EM81SSr9NBIXclxRdJIpcANfgk6IFIiUbSsXZfnxepmno7TUumtaPG3T9tQiNujAFxTOVAbAJX0o-Iossiz1iGKurJOV_vPhpcHuqko86CylQwGJH-lZ5iA4gnamLJ1LSz3oxMkYeUF405FKNGFx1hLDqjh84fjHvbMiAJn3B-TtlOQFhTUT57JR-RW6HToZpjR3kpGJIFRDCK0zHLhkCk5IKO0SuErlYoynJIccA2F2pWwpe6un9XXOCGk0IpL4Lcq58If9Hx6gi2oAr6LxkVonL3FWCvOyap-p8R9QGcLjZJUQJPtwh6JBOtrJd_hkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdd5cda06.mp4?token=Oeq8dswyE6gUCSOqOhP8_EM81SSr9NBIXclxRdJIpcANfgk6IFIiUbSsXZfnxepmno7TUumtaPG3T9tQiNujAFxTOVAbAJX0o-Iossiz1iGKurJOV_vPhpcHuqko86CylQwGJH-lZ5iA4gnamLJ1LSz3oxMkYeUF405FKNGFx1hLDqjh84fjHvbMiAJn3B-TtlOQFhTUT57JR-RW6HToZpjR3kpGJIFRDCK0zHLhkCk5IKO0SuErlYoynJIccA2F2pWwpe6un9XXOCGk0IpL4Lcq58If9Hx6gi2oAr6LxkVonL3FWCvOyap-p8R9QGcLjZJUQJPtwh6JBOtrJd_hkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شما شاهد عادی ترین زنگ ورزش کلاس نهم هستید( همه تو دوران اوج )
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91199" target="_blank">📅 19:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91198">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cylms2QIEEhrWowzeOfNhKft_NEPPpuwGSoH4idbZnA1Czc0OgAxZk5SmcBO8IaKZA8NbZc9Sf4GJagPHm0R5gceQ54h0JKvIBDkvJDT4kGG4Pyj6Q6Nei85zBV3AZCwhPUwrq-BWCAJxagCFxtrtisyZyY_6lAbrLVkvBJDu0jpeWCuq2kCS_TgHnO6q2ZyJv-V5i5egYqo8t76VQMmxSp1kgzxmkNhj5vmjiqcXLRK28iOfkgUBpesJVrN4NzJTLA5-huF2DVsgvtv0PEQIn5afTh8XqOj04J3a3x0oIGPwwg2wcuXg4Zy2YhFx829JxvCRcrmg1dZhS7fVO-81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ساليبا:
اون زمانی که ما فوتبال زیبایی ارائه میدادیم و لیگ رو با رده دوم تموم میکردیم همه به ما میخندیدن ولی حالا دیگه نمیتونن به ما بخندن و سکوت کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91198" target="_blank">📅 19:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91197">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtfqcT5F_Pf_uXv8WlnlO95caJ7NXUARNt7QW_79H4kSlcxPTgKOOJkhktU-5IdL4MpM_Tuu2wBxI8kDlUnhjQXEG9G9hwJ4QOxFGw-OQ8GUnhh4jQMUyfK3jh1yNoJ_u4FUY1fUpsUHtDIFsglTQlNlvBTRFpGtN94mFG68iLL4d9aTx5r_AZ6whFqiwJVQy5DTxbnISkjWR-OG8qINJxl1mWSR5-h2U00POkaaaUsPiaGAF0Bq45ZqW9_H93t7uyzk-ppIpnk0bpmvDCcHH_era-7nKSAohslTiEIIK2beS3WuLtMB-Vu9mOzt98kmr6v4tK8MgwThikH7OTMv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
🇳🇱
ناکام و بدشانس بزرگ جام جهانی هلند؛ این کشور سه بار درسال های ۱۹۷۴, ۱۹۷۸, ۲۰۱۰ نایب قهرمان جام جهانی و درسال ۲۰۱۴و ۱۹۹۸ سوم و چهارم جام جهانی شد
✨
اسطوره های هلند: کرایوف ( جز پنج تا تاریخ)، فان باستن، رایکارد، رود گولیت، کومان، سیدروف، کلایورت، داویدز، برکمپ، نیستلروی، روبن، فن پرسی
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91197" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91196">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYudx2_QyoU0EZwfRIIuBe4xoG4Af8FoKKZuRxP3cOO9Z8_d9S9zz6-JNkVbXgK5a2png9z53-iUOLl6HzJAL5uZop7Mr9MEO5kLrpfA3s-WuzkwpNmfywhdaE1emmr6y3Ov1twAOYc2xNQ7bYjCbUJ2yeafj7ec_yg5PizSLiHNm2dvgXZ2dayYADmJsh-znTle3gosZxyrK0GPHPcvA0_mYfIOtk31eYtsJq7N3y9zbQLqnMScZnxNuxHD3GGwF_sV5r3I8xZSRe5pMPSK8eCgv6raE4hkypqZULURfSF-NoIY5yKsTgVs8R-I0gOue0athIzx3Du6N_1lt-8qbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91196" target="_blank">📅 19:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91195">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nperU1tBOzcyCWfROGIO2tfL6zdboELNnYzHpo0RwQe2L4NMIufuSFi6ybNiQ2MfrdTt2Q_AzmlOcbABV2yaHY79dykn_ZSGQKb1NhFtXQ0hQNRlEGHukIFjOeUtftQ0iGbrgtw4Ok5L0bsglE3AxOaqsy-dqNuIafv3-jbLH56xfEkhYZA7rEEpPyTjLetb5CRM-_MJzf9-8XyUl6aB5jG9De-UAyCQTqRZehXDKVdF8O1aVqv9gdp2xvM-z03IN-zAeFKbhX7aQkTpkwhsYzOfjzTWIsDrD2TsvcP4Qs1r22uucGHWceXk-U6K9_m6LZRRA4f6byr1szTgzVgZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه نیوکاسل چربش کن
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91195" target="_blank">📅 19:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91194">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10990086be.mp4?token=I1ENTcc8kn6w0_4-zdwRj48FcRdEMGeU5w47lheG4q2AVrs5NZX6aN-WxMFn_aSuOgBwNxNsrV943WugX1XI4-TwBeMJ1CYQfIBMqsYepoW_-KnrrJZY9Bn3K0_5CTr7wBUVzyTPMCI5AiE0vafaLLBIV-TOib_eA-2hKB2_ua_TRuz1l9rVx-g5R1PWDQs6pfvB0YWOfQgApbdr_FVw5A5wxS2c62NbGnC7FqeUOCeVQzdvZKiy0kso2KUhr-94Ze62tpegDBRdCuvfj6fOby_nTXz4oe_zBrkjHXfXAGlSEuTApKMy6rMdctbP0OazOgb6z1Lq_Y_O1UJCAzeTcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10990086be.mp4?token=I1ENTcc8kn6w0_4-zdwRj48FcRdEMGeU5w47lheG4q2AVrs5NZX6aN-WxMFn_aSuOgBwNxNsrV943WugX1XI4-TwBeMJ1CYQfIBMqsYepoW_-KnrrJZY9Bn3K0_5CTr7wBUVzyTPMCI5AiE0vafaLLBIV-TOib_eA-2hKB2_ua_TRuz1l9rVx-g5R1PWDQs6pfvB0YWOfQgApbdr_FVw5A5wxS2c62NbGnC7FqeUOCeVQzdvZKiy0kso2KUhr-94Ze62tpegDBRdCuvfj6fOby_nTXz4oe_zBrkjHXfXAGlSEuTApKMy6rMdctbP0OazOgb6z1Lq_Y_O1UJCAzeTcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🙂
چیشد چیشد ازگل؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91194" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91193">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91193" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91192">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fab7e29.mp4?token=VILca6qm2gr7v7hNukGoqYpIsi2sVjPj-JoQbRKFUJUmkgQTTI_blDfIAOtZe9e1IS2CQwLzkeCcz4OZBDStKdPQ9vZhuiMmYVk7SpdQbQNAOGi0I8a99BgOt7IjRxMnt3hzgZe5Vc9zxTFKXMrZvmEgfg1Fu74n8u2ooO9K7P4IOm768CzeFaHIeUQ8LyIqimt5qzjhS164FxLY-c-6Kkhr5pkideuRfjLnOlb9SGGvWJk-k1PKbaKn07MXcXgN76buZHcUswoQ3T5biEhLgfLk4MG7SIuZki4-6ojW3WQ1_W_NIeaZ5s6mo-Qs3QcQTFX8njOs4roJQAnE081aZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fab7e29.mp4?token=VILca6qm2gr7v7hNukGoqYpIsi2sVjPj-JoQbRKFUJUmkgQTTI_blDfIAOtZe9e1IS2CQwLzkeCcz4OZBDStKdPQ9vZhuiMmYVk7SpdQbQNAOGi0I8a99BgOt7IjRxMnt3hzgZe5Vc9zxTFKXMrZvmEgfg1Fu74n8u2ooO9K7P4IOm768CzeFaHIeUQ8LyIqimt5qzjhS164FxLY-c-6Kkhr5pkideuRfjLnOlb9SGGvWJk-k1PKbaKn07MXcXgN76buZHcUswoQ3T5biEhLgfLk4MG7SIuZki4-6ojW3WQ1_W_NIeaZ5s6mo-Qs3QcQTFX8njOs4roJQAnE081aZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
اعتراف نیکبخت به تبانی استقلال و پرسپولیس در دربی!
‼️
😐
نیکبخت: اومدند گفت چون جو استادیوم بهم ریخته است بازی باید مساوی تمام شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91192" target="_blank">📅 18:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91191">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tavvniJVoYpYUTjFq9885uX261S3BlX9HOUMxbQdBBkhdLWw8REHhYcnUH7rNsfBFn91pSECKHddL7psMdc8n1zL2Y7hA2JG5lGKcADhbBYo-qEdK-5gqs2Y4wxnWNSxCdrmYrK-9vzs8iqFCUey0UbjPzvT_kyvUc-_zlYtsSlUCPe0o50rTXqLigqlLq65TpyCUEJggrh4dk7sIUd5SCLLS1kUwhkelXKMufiZnW6sK5DmQm2z_pHwXFuPaXjqdJ0yz-l2F7aW7nB8f_i6Q4ZY9O_gL8TctHPzLgs8tx9xZZmQk4ZWca354c4d5sYImdktiDafDbeTDND5fxhozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع خیلی خیطه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91191" target="_blank">📅 18:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91190">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یحیی گل‌محمدی لژیونر جدید فوتبال مملکت:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91190" target="_blank">📅 18:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91189">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnsZ0G9YnifIfawEQkt5sOQxP7da35yT_rLafmTb-4WsBn65AmDY7qf7QMr-TbjEacTmwrKgGWkpUt1faY52Vp7pegnpV2zkqqq23Zqkx4zZGQuerL9DWUHeKZ135kI-C4sh6HbGaf1zLFCT-M71ifvdQusneZdVRkdFg4s4XEUIUUacXxKPqSAEL1iRLUMkxj5Ok-s7ox4RDz7KP119mtXrevJx5JFSwRFcgKTNsc3sNgyGgoR9_7DtW0JJAhDqZJ8kEkqSYw2d2ZBrOWWM3r8c16iuQwjDat4i1DUgAEK90i0MzBh1Y5o1pvGjM3vAnnRfCQMiXckO-6to0QSb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع خیلی خیطه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/91189" target="_blank">📅 18:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91188">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3kwhqAr6Q68ltTL7-HgJxw4n2AM_vdN_jGg60Ix9KJrJTTj7OMNM_ztg573JecpjGbjXGoZ8hSmim0iViDtUkQi_RqqMYqrKGb6fhiaaeEj-36cz2xEOe-9wgzG35bFkmHKq1lqFleyUli_RUSoAQCgRONEOmWVvTwtf_zgm0jOxAptYwS_op4lbYGa_qKEy9ukcY6x8spn9dBl4kghk7xbbVYzJCHIYyKtp_Cwd_pwhg0YIMRC1pH3jUBSC2x1W55l70gzyAU8hLkq8Latwpi_W6xr7p9LkqEa8G7l4w5HdmHHbaO-EiUz6sAOLDj2ytJyJzkcF-8tuwb2kEz39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
به برکت میانجی‌گری(همون خایه‌مالی) برای جمهوری اسلامی، اینترنت جمهوری اسلامی پاکستان هم دچار اختلال شده
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91188" target="_blank">📅 18:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91186">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzodrfXq9K2uEAqck-oe9IWlVPWHLFjyARqwus6tOy6GdDIEHs5WdLuVpsveRWlKGV6xb_b5DEAgWJJrz5c5JV748_hYXte1LRm2e7DN1hxYot_IPx3jAFSZSTJeRS-KidiQ6-avqERwpPEO6ZsDvsTKO7ieK2MGZgMZTsjQlFAhDF6qkBMZ_A7tpoVWmgAVZPedrKd_b3u7Okpbtl6As11ukTwf-H4ASXLy-0IAMkE2vcjIgMb4eFMHAoXrC9bACXdQS6PseVoA-9lHd8KzqBl4EUsa8yqXScCd0elpOQ-apf1QzJz67ynyW0Y4ZbYnFRQVjK0EWtzI7Vr-wfb5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلث های سه نفره خط هافبک اسپانیا برای هر جام جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91186" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91185">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niVv6pxQ0GH_Av_2qnECyvpVGomw2GpdwIrUMmuk1KHd955QxM3ok3QvCPhHykp796YTUzFU9EgsuKqS6vSRcCLXY-nyVDdxG3wPofP2TT_RGSxMiTryDWRCusaj5cAJ4jXLAMqhYltrgKBIXHaYXXimSBx7SF60H76Ktlo1TOFfpgzoqoiWnnfM8tPBOlKVLDrzX-woX_ADyukR0m32jFXWgLn_oC9b2JXsk0CjtCEVk2Zb29aaXQLQ_nJOvLPVn7DUAkrGdlng6BokEZ0H0u6NZdpZmVK8_d6VhcwbRPMvue7VlTEuMCOwdfwdE8b6jAiRTLLXAvjqpHlG9IEqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
❌
#فوووووری؛ لئوناردو بالردی مدافع آرژانتین روز گذشته در تمرینات دچار مصدومیت شدید شده و نمیتونه در جام‌جهانی حضور پیدا کنه. بزودی آرژانتین نفر دیگه‌ای رو جایگزین این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91185" target="_blank">📅 18:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91184">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d61c1cf6.mp4?token=aLUO8msBLUauVmxSADwspkcpLSxzfGK0Qc4I3dfwnyLT4so0Ejth0PNQR5HGCBlFZHFco5xDZTd1Mtuu16yvxcSxojksCtivATbqbJyyEO74pPbq1rDL912HGrS7SMNqCfNCElUo1eQ4T6CbP1VtCVXOLIK1Ag1zLgYAIXhKt-At47xh-bqWPc6VKYRsXIgv11eMjosXpSNJHG6lTbaFaJvkLlazVtZ08VtaHzPp0QQZrWJqF85qT5OpdkM1EpHb4UWbQr8KRsz_Hxzm7akMDeEmbWqx7L2gkghqxRnfOwr3NPtYhEZhib1Y_vSNH00BTIL-lX3pcfmBmzRnDQHFIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d61c1cf6.mp4?token=aLUO8msBLUauVmxSADwspkcpLSxzfGK0Qc4I3dfwnyLT4so0Ejth0PNQR5HGCBlFZHFco5xDZTd1Mtuu16yvxcSxojksCtivATbqbJyyEO74pPbq1rDL912HGrS7SMNqCfNCElUo1eQ4T6CbP1VtCVXOLIK1Ag1zLgYAIXhKt-At47xh-bqWPc6VKYRsXIgv11eMjosXpSNJHG6lTbaFaJvkLlazVtZ08VtaHzPp0QQZrWJqF85qT5OpdkM1EpHb4UWbQr8KRsz_Hxzm7akMDeEmbWqx7L2gkghqxRnfOwr3NPtYhEZhib1Y_vSNH00BTIL-lX3pcfmBmzRnDQHFIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
خبرنگار
: رئال مادرید یا بارسلونا؟
👀
پاپ لئو
: پاپ برای همه تیم‌هاست، اما پرِووست برای رئال مادرید است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91184" target="_blank">📅 17:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91183">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇶
🇺🇸
#فوووری؛ آیمن‌حسین ستاره عراق دیشب در بدو ورود به آمریکا حدود ۷ ساعت در بازداشت اداره تحقیقات و مهاجرت این کشور بوده. اتهامات این بازیکن ارتباطاتی با گروه حشدالشعبی بوده و مورد بازجویی قرار گرفته و سپس پس از ۷ ساعت آزاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91183" target="_blank">📅 17:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91182">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eda27170e.mp4?token=s1fguAUaFCc91Ga6Lazh7rUCB0ssxayVxqN2qcnPmOEfM1wZgGl2mn3YOWDjg_QK-0P7pMwVUa3M3ci3Bzoa5dIhAe_xAqKkIiCShsdgzhkfQX8YzE7AdUJg4-V3aQH1NVQWyFbZWOYrRQ3Zk1SEaeR-Sc9wy-AiK-O5_rbnqSQIC4Prt131R78CNSJc37X-1HI7H2ukkAk2CMWwvzQdPxvGlLgE8RHMl3EXhWXnBzpebW7BXCeC3YLsyF7AEz5d0o6LooZDuesNXQSoznmeDRu20MfGdBCdPAE_0Ob_7YVk6XYoUleeG1_cOV9ElrJm8fXg2IqBtRYYo3Fwp-xCAGQq-IG6m6pPEdFLClw3WjEdvy7cqO1ooNX-d99QHcMuPSsCEm3-zk2t9hLbhpnsrA_RXE-D3UP1rOCSbTd0zD_Ihm0bP61kUncpYWHpc4LO2mxToxILWDUesL7_Am56KlpJUPBPTUYuRMpOClwiw0vQkHEWf-8sAMXP_T5zYn-jTtGO7kCiMpWwQPMvS2DOgi6a-wSRgAaQP5ERwOMYzhRFf5GYSHhNdHplaBcPz9eivvkzSbNp9aXJBNLDg10Lf0_IKWh4nE1MoWRCzXeR5QaLo6cdjqnON8E9p6a9IXXF-uGcSJvD3gMkYnGkmRGgEXzPhZnhaTfCx-ZuI-VhWjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eda27170e.mp4?token=s1fguAUaFCc91Ga6Lazh7rUCB0ssxayVxqN2qcnPmOEfM1wZgGl2mn3YOWDjg_QK-0P7pMwVUa3M3ci3Bzoa5dIhAe_xAqKkIiCShsdgzhkfQX8YzE7AdUJg4-V3aQH1NVQWyFbZWOYrRQ3Zk1SEaeR-Sc9wy-AiK-O5_rbnqSQIC4Prt131R78CNSJc37X-1HI7H2ukkAk2CMWwvzQdPxvGlLgE8RHMl3EXhWXnBzpebW7BXCeC3YLsyF7AEz5d0o6LooZDuesNXQSoznmeDRu20MfGdBCdPAE_0Ob_7YVk6XYoUleeG1_cOV9ElrJm8fXg2IqBtRYYo3Fwp-xCAGQq-IG6m6pPEdFLClw3WjEdvy7cqO1ooNX-d99QHcMuPSsCEm3-zk2t9hLbhpnsrA_RXE-D3UP1rOCSbTd0zD_Ihm0bP61kUncpYWHpc4LO2mxToxILWDUesL7_Am56KlpJUPBPTUYuRMpOClwiw0vQkHEWf-8sAMXP_T5zYn-jTtGO7kCiMpWwQPMvS2DOgi6a-wSRgAaQP5ERwOMYzhRFf5GYSHhNdHplaBcPz9eivvkzSbNp9aXJBNLDg10Lf0_IKWh4nE1MoWRCzXeR5QaLo6cdjqnON8E9p6a9IXXF-uGcSJvD3gMkYnGkmRGgEXzPhZnhaTfCx-ZuI-VhWjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
🇮🇹
نظریه محبوب:
جام جهانی بدون ایتالیا اونجوری که باید نمیچسبه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91182" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91181">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtAhMJK_b_kRXss01GVdsB15BpqzMKAFRfFUHvEiyWgD0iMqDF9f1Hh31xxOrYySv10XNAcLdZZb8OfQ6T1ZRqaUqTejhtGRpJB1sTNqg8t8frl_ipxqBe7eWFH7TNqdovC5VF54wcigvjszlWsXHC4uSlmXU646sDXx4ZJsjSg-8_8j83IInYyu2VBTZZ4kaJgtzyXnN1lilXdT5DkMFcyYHCvoNa0je6BRvJZnf_ZSSjd0UqsAGgqDaMs-idmJqVzshBSWUICUdKyZl2KQUpwvhlj29D1XSpU0OutZJs_qm-LmznMuTAIaRsHnKPh_10QPeoKICw3lsP0NPepCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙️
پاتریس اورا: «نسخه پرایم من در مقابل لامین یامال؟ من او را زنده زنده می‌خوردم. متأسفم لامین. دوستت دارم اما از کریستیانو بپرس، از مسی بپرس، از بازیکنان دیگر بپرس که موقع روبرو شدن با من در بازی اصلا دوست خوبی نیستم".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91181" target="_blank">📅 17:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91180">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4803f256d5.mp4?token=pUbv8IpFGP8nNMxqtJGmh-xiJBalLw1QVeNuNQgEryQE57QWICBktheQT606UWN2L6-3067Wgy0pUOLsWnbKH_UoFF7JaRut9cLRQrtd8frXxs2pVt9yfofBnhF371UnUiAOAEjnTlumJgSf3dcgk_0niUrhcjug8J1qlIseQJB6-ISKFWwLyfubZy9nvmzcXhMCCr9cSQOF-lLylZpVJmn4KCk8Skgq4Qn0SuZMLhRdfb2ahhUlI0zmxH-Gn-Qu0sPGykeyPO0_fVQMTSgE8Kn8Lb7aNDJT686BtFOnphBrjLmLpCD1eCxHJpO_NO6MrFkotwZxgMHMofM-rlwuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4803f256d5.mp4?token=pUbv8IpFGP8nNMxqtJGmh-xiJBalLw1QVeNuNQgEryQE57QWICBktheQT606UWN2L6-3067Wgy0pUOLsWnbKH_UoFF7JaRut9cLRQrtd8frXxs2pVt9yfofBnhF371UnUiAOAEjnTlumJgSf3dcgk_0niUrhcjug8J1qlIseQJB6-ISKFWwLyfubZy9nvmzcXhMCCr9cSQOF-lLylZpVJmn4KCk8Skgq4Qn0SuZMLhRdfb2ahhUlI0zmxH-Gn-Qu0sPGykeyPO0_fVQMTSgE8Kn8Lb7aNDJT686BtFOnphBrjLmLpCD1eCxHJpO_NO6MrFkotwZxgMHMofM-rlwuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
تفاوت قیمت خودروهای خارجی در ۱۲ سال اخیر
اینجا هم قیمت فرغون تو یک سال از ۴ میلیون به ۴۵ میلیون رسید =))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/91180" target="_blank">📅 17:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa0DbPYTmuxiy1803XSQkptsmAWFK_KABhyygWqgkKVZArLuyEbCdRawQVa0zOFHTtZWge0clnXHbZgPJvGGFofTCTS3X90eGZgjAMR02Y4Eclg3Ju_DMdxLsHj9x5LnhWZ0Ftx54SHywpPmm0pAHq-J7-wj2uYIpL6dMWq4RNPX5J5LUfhb2-cUxaXWQ_2CA740JT0vQn72HJBYTDs5eodDbN64ZrHCwet1XJnhNVL7H_KocoKUw35K7yrwtWsRbiWr3_qU5GsZKmXHW9T8OQh1TwUJ-6NAGrpTjuNp4lQFfaGuVxLx-WQHCS_gkSSAJR1ztczVUFLTS-h7NxSy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه این دوره هیچ‌ تیمی تصمیم به شگفتی‌سازی نگیره و ضدحال نزنه یک چهارم‌نهایی احتمالی این شکلیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/91179" target="_blank">📅 17:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecfebd678d.mp4?token=rWjpFJk581PcAhvINH_N-4XaCKgsL-gqEEyexsOHWLVRYP_yGxZlOc3jOr947h3yuf3vMHUvgh8KadcG5YkOBTll1l-uoGciVtQGHPFemuLHehvq42or7auGCkpreh3rbPu94AuL5-9TQIrDndey8k0eANCHrQaOEB06XA0eoZGWIn6RvrulACrVWMRXuBDLBWkbnfUjg8btanjfNnmtcUPcMzx9rE_zMnKevf255ljsYBZnLAw-ABL1hOnytMxX4Vb3t9ueF_Pu78ECU1hlrxrLnuA8kcHeIuzt1Hu-j1Z29-9srnL7FB_DVeM3SzQL6lbB_TAi7_ng0WwSVSRkZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecfebd678d.mp4?token=rWjpFJk581PcAhvINH_N-4XaCKgsL-gqEEyexsOHWLVRYP_yGxZlOc3jOr947h3yuf3vMHUvgh8KadcG5YkOBTll1l-uoGciVtQGHPFemuLHehvq42or7auGCkpreh3rbPu94AuL5-9TQIrDndey8k0eANCHrQaOEB06XA0eoZGWIn6RvrulACrVWMRXuBDLBWkbnfUjg8btanjfNnmtcUPcMzx9rE_zMnKevf255ljsYBZnLAw-ABL1hOnytMxX4Vb3t9ueF_Pu78ECU1hlrxrLnuA8kcHeIuzt1Hu-j1Z29-9srnL7FB_DVeM3SzQL6lbB_TAi7_ng0WwSVSRkZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دم جام جهانی یادی کنیم از بزرگترین غایب پرتغال
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91178" target="_blank">📅 17:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91177">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09753bd04.mp4?token=FDojfLiWFx1uTgjnaWg698HjfkxqTvYk6j11ZEdrHXMQJozf5qOvsnUYm_N_m24xTYNa4vo711J9nAHV6P1BRLWa_r-DAm6eEDSl_jRG-q6aDPDvodIxnNQ_ltUIanZI7k6rOAYtK0zuqWjpNM9Tmyd_Ho6zR7RaMMwPB2EBhiSHY4_cPcU7q1RzpqQBIS1ByBkbSl2zjnVeVopxSjQUX-cegnQDtk1UCti_9jJlNca1nJgpugH3ty2w8p9yM3BxOZwSrusWXtGks_aJj4FPwg3Ng3FHYIkTJI7JsU4mS8NO46fkP8YRafrb2c7dHx1EJhLhqNZbG8Oclip2ZzYNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09753bd04.mp4?token=FDojfLiWFx1uTgjnaWg698HjfkxqTvYk6j11ZEdrHXMQJozf5qOvsnUYm_N_m24xTYNa4vo711J9nAHV6P1BRLWa_r-DAm6eEDSl_jRG-q6aDPDvodIxnNQ_ltUIanZI7k6rOAYtK0zuqWjpNM9Tmyd_Ho6zR7RaMMwPB2EBhiSHY4_cPcU7q1RzpqQBIS1ByBkbSl2zjnVeVopxSjQUX-cegnQDtk1UCti_9jJlNca1nJgpugH3ty2w8p9yM3BxOZwSrusWXtGks_aJj4FPwg3Ng3FHYIkTJI7JsU4mS8NO46fkP8YRafrb2c7dHx1EJhLhqNZbG8Oclip2ZzYNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
پرنسس لئونور دختر پادشاه اسپانیا که آقای گاوی زحمت کشید بهش پا نداد، بلند شده رفته سربازی و اینجوری داره فشاری روانی از دست دادن گاوی رو خالی میکنه
😂
😂
😂
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91177" target="_blank">📅 17:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91176">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH9yMoz5DGsLtTXHz37BErYCGv0-H8dQltC9Oga7eUCtsoIJGEBrVcQoMa1A6JMjVGM4jTuA2fRQ2VdeiVziRGtUPAO4UnaY8RrDdTl5sgCzRt8ivxHaZLePrUFAJwNBoJSxlM_LgZxwk2XGnHCLiEoaQb3aNwmiPw-4LZS9adYIkEeZiYaFwT13lDO9Ui5Bpzx4l_SHpJka23zh2mELdOSy5NZEq8a2h6_7A6xobk9NDxZBm6s62Mjq2fp63vUKNVu-R2EQPHweHOeNMYI4WmGfCbNCnKsKZRFENz2CncAmM8dXU4dWIrzxCfuhbLrUbVoavOvHB-pAweyfITGC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
از مایکل اولیسه خواسته شد تا بهترین بازیکن فعلی شش کشور مختلف را انتخاب کند
🔵
مایکل اولیسه:
🇩🇪
آلمان: جاشوا کیمیچ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان: هری کین
🇪🇸
اسپانیا: لمینه یامال
🇧🇷
برزیل: نمیدانم
🇵🇹
پرتغال: برونو فرناندز
🇦🇷
آرژانتین: لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91176" target="_blank">📅 17:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91175">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c576d4593.mp4?token=MjYADQQfGq0Hm5dzwaC3gpH84FxbvB-IBR0dGdbFPLtqZdShrRzMS8bA7Ql1nFvpVhaedQgMt4imr1peFnlh8mcwzP7f-FkHLlIqK1ssvuC7h28tuaNjtqapu6X79P0tGFfoecKIWtvX11af2jbSwdQK5urvYv2O-ij4razgBJqyDihbPyyPHBJukwuK8dGeSm4C2NW9WVRtHUrY1-vPoi9xDibZ7YBGWvWICMZ4End9XRJq591vhfZNzPhTbg9qYgym1XBnAk2usLkOlcYcdqUwn4brfKT1WJzAddUyVSBJMGB2JJYt3mqLbztcz2U-WWqQKcGF0kkw-i7q54n7CIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c576d4593.mp4?token=MjYADQQfGq0Hm5dzwaC3gpH84FxbvB-IBR0dGdbFPLtqZdShrRzMS8bA7Ql1nFvpVhaedQgMt4imr1peFnlh8mcwzP7f-FkHLlIqK1ssvuC7h28tuaNjtqapu6X79P0tGFfoecKIWtvX11af2jbSwdQK5urvYv2O-ij4razgBJqyDihbPyyPHBJukwuK8dGeSm4C2NW9WVRtHUrY1-vPoi9xDibZ7YBGWvWICMZ4End9XRJq591vhfZNzPhTbg9qYgym1XBnAk2usLkOlcYcdqUwn4brfKT1WJzAddUyVSBJMGB2JJYt3mqLbztcz2U-WWqQKcGF0kkw-i7q54n7CIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
روایت چلنگر مترجم سابق برانکو از تجربه همبازی شدن با بهرام افشاری در مرد عینکی: بهرام از شدت گرمای هوا، نزدیک بود بیهوش بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91175" target="_blank">📅 17:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91174">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
#
فووووووری
🔴
حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91174" target="_blank">📅 16:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91173">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZy6rnjtkFjnXXyBtDggwE8uHAl7Uzg5w9pf3Z3N-dBjd90y7xGBghJLCenXyS5f0I7S97zzODdXLlMzCgpzeKZQ-n7LYyeYbLr07UNTqUnCSQPpcL0tL-VsIbKiP9QyzL2wxG4NeCEKUXl9tIr0XlLY1GWBeejL18swA-jyNp533IE2HQmBEbx6DpEvdm-u5B4el_wFWNQABOy2WbMHxk7EZzEg8BT6eYRAmhH5j2rbeZeN_9KFKs9kJCBQq1B_EQiPcAspFUt0iQhpSgFLm4S0hhIBP5PyRzlHC4DNIiMtvKyY1zZ7HO6kt_C-S4FiqWH_LLz408jMWWwZ5nnpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
طبق گزارش امروز لكيپ:
❌
تقریباً تمام بازی‌های جام جهانی (۱۰۴ بازی) ممکن است به دلیل شرایط نامساعد جوی، در حین بازی به طور موقت متوقف شوند!!!
❗️
احتمال وقوع رعد و برق، تگرگ و حتی گردبادهای قیفی شکل (تورنادو) در مناطق مرکزی ایالات متحده مانند کانزاس سیتی، آتلانتا و دالاس وجود دارد.
‼️
همچنین خطر گرما و رطوبت شدید در شهرهای ساحلی مانند میامی و هیوستون وجود دارد. در حالی که مونتری ممکن است دمای بسیار بالایی را تجربه کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91173" target="_blank">📅 16:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91172">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAq90tZ2rNVUTsMmcf6gv0owP1F-ZX4_V0OTO-He1Ifwmtlb0txzUSOZFMMscdsIaOt0VK1X0k0Fb5ozVbyVswkE29dazb_Xj1SpxlysMQPv-IAzqgNKh43cUhi1Wn_hKHLDVYag6u_fC1LZCfi3T-JAfIqkFRmqwmK-lVRpkbz3w3pV0XsWjA3HlDzpTy-eE2vhzhrUpH4BGp16qBKPhXe0k9qHo7wGfaR6umho5O6K1OS_5YZYxeGwGy3D-GkM17REx2yeEjRecl6dG9YCgROA5d37t605VPqYdR6L3XbQUet8frpVtk8PMzjXt79MU3L6XuoSk0i9o-BGxygI1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
معرفی‌مختصر تیم‌های گروه B جام‌جهانی
🇨🇦
کانادا
:
لقب:
Les Rouges (قرمزها) / تپل لیفز (The Maple Leafs)
ستاره‌های اصلی:
آلفونسو دیویس (ستاره بایرن مونیخ) و جاناتان دیوید (مهاجم یوونتوس)
سرمربی: جسی مارش( انگلیسی )
تعداد حضور: ۳ دوره (۱۹۸۶، ۲۰۲۲ و ۲۰۲۶)
بهترین مقام: حضور در مرحله گروهی (تا به حال موفق به صعود از گروه یا کسب پیروزی در جام جهانی نشده‌اند و به دنبال شکستن این طلسم هستند).
دوره قبل (۲۰۲۲): با وجود بازی‌های خوب، با ۳ شکست در مرحله گروهی حذف شدند.
نحوه صعود: به عنوان یکی از سه میزبان مشترک این دوره از رقابت‌ها، بدون حضور در مسابقات انتخابی کونکاکاف، مستقیماً وارد جدول مسابقات شد.
﻿
🇨🇭
سوئیس
:
لقب: Nati (تیم ملی) / شیک‌پوشان قرمز
ستاره اصلی: گرانیت ژاکا، آکانجی، زکریا
سرمربی: یاکین
تعداد حضور: ۱۳ دوره (یکی از منظم‌ترین تیم‌های اروپایی در حضورهای اخیر)
بهترین مقام: صعود به یک‌چهارم نهایی (در سال‌های ۱۹۳۴، ۱۹۳۸ و ۱۹۵۴)
دوره قبل (۲۰۲۲): صعود از گروه و شکست مقابل پرتغال در مرحله یک‌هشتم نهایی.
نحوه صعود: صعود مقتدرانه به عنوان تیم اول گروه خود در انتخابی قاره اروپا (UEFA).
﻿
🇧🇦
بوسنی و هرزگوین
:
لقب: Zmajevi (اژدهایان)
سرمربی: سرجی باربارز
ستاره اصلی: ادین ژکو (مهاجم کهنه‌کار و گلزن تاریخ‌ساز) و ساد کولاسیناچ (مدافع باتجربه)
تعداد حضور: ۲ دوره (آن‌ها برای اولین بار در سال ۲۰۱۴ برزیل حاضر شدند و این دومین حضور تاریخ کشور مستقل بوسنی است).
بهترین مقام: حضور در مرحله گروهی (جام جهانی ۲۰۱۴).
دوره قبل (۲۰۲۲): غایب بودند.
نحوه صعود: آن‌ها با خلق یک شگفتی بزرگ و حذف/شکست تیم‌های قدرتمندی مثل ایتالیا در پلی‌آف سخت قاره اروپا (UEFA) توانستند بلیت خود را برای سفر به آمریکای شمالی رزرو کنند.
🇶🇦
قطر
:
لقب: العنابی (عنابی‌پوشان)
سرمربی: جولیان لوپتگی
ستاره اصلی: اکرم عفیف (ستاره تکنیکی و آقای گل جام ملت‌های آسیا) و المعز علی
تعداد حضور: ۲ دوره.
بهترین مقام: حضور در مرحله گروهی (۲۰۲۲).
دوره قبل (۲۰۲۲): به عنوان میزبان مسابقات حضور داشتند اما با عملکردی ضعیف و سه شکست پیاپی در همان مرحله گروهی حذف شدند.
نحوه صعود: صعود مستقیم و مقتدرانه از مرحله سوم انتخابی قاره آسیا (AFC) به عنوان یکی از تیم‌های برتر قاره که با پشتوانه دو قهرمانی پیاپی در جام ملت‌های آسیا، با اعتماد به نفس بالایی صعود کردند.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91172" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91171">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eze874oKvzeeV6rZsu8UimAKgaQs9CUNoyt5RLeLivrQdUBRv3fVCE9p4ogxodSuS5zlhySnT8pSLbEdua1NAMeQ-avcz_cD7sTSNf13IH7i6TKZyUefZMACE9H6smN_tTU7tbvHjR9BscibUQ5PjljJLoIT9QsJmXlJ0bEW4sBf3u22zPDAyH_qJrTdKclWE3ieywNvgvZWqjRjf4qmXyVsAC4bk-8nHRoTuJlvnFhJ2kx0VusV4ZY8irWrIKeIG5k8c6vSUd7mj3FXRmtOsZp14s3yueUuu3mpAI7fXtTlckR6gKetTJw1PJGtoMQwBiGlKcA4_nrfJcyWeVhRmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس‌تیمی تیم قدرتمند اردشیر قبل سفر به مکزیک
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91171" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91170">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG20bGYtOsMAmI6NJC60K7xINxjJU1H2-xOT5sKUCsFEhEpWZituejSUX-lndouwaDJYNsNopW-aVKKHINJnlCoe0OdRJTP-lRHe6ZWk5kS5X-J8D60DYeLm3T-O69pbPXTE-9JPgo-pCtto7MFPtVS1Vn_ffW0KIfN13UjLI2VZeKK0XA52MSFbzUYnsH6XQtnTV_P-LRya9vgtNKfutpbxvEA7lxYsbGvwJMwIC8ugawYK_Gi0-VMzIdGucAoPchgAGqgH_MhjvcnnzdKQx-cFHGiRsNY3TMADSgA8MVgscVwKrtZO-qT0IksLvpfNZdhCfAZ-tUk_q2CwTH1A4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامان قدوس تو عکس رسمی تیم قلعه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91170" target="_blank">📅 16:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91169">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mNrOl_xbyN2sAqTRvpWPzg3rPLPDwgsfRpTGKYtNDgG5q0ZmlXtmlk_WdfULtEpQHgGgAZdrzkoDK3Ae8hCijpfAwTdSfoCDBS8gpGF1ViNbjU7LBMso3WrPwI6FJKy_SQ-Evc77TmF3bD0tICEQUa2RTsBpyWS3xwJeONSR0v2vEBX-0Zq9_buMTFHLzqFukDjdWfx3PX3ZPdcrjGV91BA1UUydC2vHYtPQixdFSE91OFDLnkEKHmousAaoHjDn8GJ3CYmoyGkgTGi_5HDtWdAdNA_mkY4UKUaL7XwjfqMWNmS1DuZOSq0LXb2RToz65Uvtq-Rlj9uLesvatnTDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
؛ به نقل از موندو، دو تیم سیتی و یونایتد خواهان جذب بالده از بارسلونا شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91169" target="_blank">📅 16:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91168">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a405dfd62.mp4?token=vKp76OEagXc-Zsuxbi7i8i-BRqSQlm-jhuGME3GFmt9UMO3rArhcmkP9G4WZ_8uK9NZnfnLzcorY0RJ36-GtiE9_DMq6_Ca85UcdGVW0sHS-cY1HQAJGBmZp_H9VAyvdLbyZCisIHpbzJ6XtVN4laD9bMQJbP9BPsJOsQ7akV64ubVpMQsRWRK-nkRgeUihonqvhM_X_0mNjQlu30Hg0-gQXR2tmzvSBipmCXZOU6xiktfCcxz_Q611Li1ndJjbyAp7HFHr9yhNAgryc6oVa3hrKB-B0NsFUg0ZsEwFyNaGB7P1r45i1nxmkCEFMmiojbp57hrUKp9PTAaMhUAbYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a405dfd62.mp4?token=vKp76OEagXc-Zsuxbi7i8i-BRqSQlm-jhuGME3GFmt9UMO3rArhcmkP9G4WZ_8uK9NZnfnLzcorY0RJ36-GtiE9_DMq6_Ca85UcdGVW0sHS-cY1HQAJGBmZp_H9VAyvdLbyZCisIHpbzJ6XtVN4laD9bMQJbP9BPsJOsQ7akV64ubVpMQsRWRK-nkRgeUihonqvhM_X_0mNjQlu30Hg0-gQXR2tmzvSBipmCXZOU6xiktfCcxz_Q611Li1ndJjbyAp7HFHr9yhNAgryc6oVa3hrKB-B0NsFUg0ZsEwFyNaGB7P1r45i1nxmkCEFMmiojbp57hrUKp9PTAaMhUAbYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
وایرال شدن عجیب و غریب موزیک شکیرا برای جام‌جهانی در سراسر دنیا؛ واقعا محشره و همه نسل Z باهاش ویدیو ساختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91168" target="_blank">📅 16:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91167">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBuDHW4l-PD9ueSpg-fzupayl5RePXPYhawNY30SmMf7C7LjR1Y4V3fDFhcUO8nqXlofTaU3FNFJR9KnXpKaa_WFG_Rn9ok0hyX0boRs08aQWb49H3ffXFn3iuoUO5VKHnzPMBPvGU-qy5MOGZJKLsyQ-xBLKP8sS-KL8vuky1gc2SNp3WAALkUs_KEQeQoSUwvMpA6UT8mg1FcPhTEIETCXRtTcoKZWDQuKLWcmZdSlKQaPVJFiwg94ngjIg8eVEprrtVGZ8T5WSKb9_r-23yAjZhhIgXHHasd5-2Dh-2Oa9Oxku5WkcdUdbM34qmH9_yDBK_oaFx0NRwY9fnnocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
🇪🇸
فلورنتینو پرز: عمرا بیخیال ماجرای نگریرا بشم. انگار بعضیا حافظه‌شون خیلی کوتاهه. این بزرگترین فساد تاریخ ورزشه و من تا آخرش میرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/91167" target="_blank">📅 16:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91166">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5532e9c9d8.mp4?token=WA3oII7j6zr_0Bp3wMDgGkNtLQBof3sgNFt9XfETG7p8dJnN5mZiblxGyLWiVvmEMFbK-eziS26XSFo3NT38z-lEhDY95hHWtfqmGGWJztuhSqsDGpWuhfJnhj5R7PayyPIbha3nWiBvxX8wwvxhBC6wemakLV6B5A1GoveYWbXNHnShJMJeGicKzb9HsyVrl-Vm11if0xKdpIw8ibHZnXNHvjlGVXJptvS_MV6KoOAJCT0pWqpRB2XTg05MlcJ8QdplOmQBEVxYoqlJ-cIsPsj21kb4fQpAtA1SL-BTJf5-evt4BLulLIA7mee4Deo4OYZGS77Zs5YyNkrOMuaHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5532e9c9d8.mp4?token=WA3oII7j6zr_0Bp3wMDgGkNtLQBof3sgNFt9XfETG7p8dJnN5mZiblxGyLWiVvmEMFbK-eziS26XSFo3NT38z-lEhDY95hHWtfqmGGWJztuhSqsDGpWuhfJnhj5R7PayyPIbha3nWiBvxX8wwvxhBC6wemakLV6B5A1GoveYWbXNHnShJMJeGicKzb9HsyVrl-Vm11if0xKdpIw8ibHZnXNHvjlGVXJptvS_MV6KoOAJCT0pWqpRB2XTg05MlcJ8QdplOmQBEVxYoqlJ-cIsPsj21kb4fQpAtA1SL-BTJf5-evt4BLulLIA7mee4Deo4OYZGS77Zs5YyNkrOMuaHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پارت سوم ورزش در خانه؛ حتما استفاده کنید و واسه‌ دوستای گشادتون بفرستید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91166" target="_blank">📅 16:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91165">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea44f33918.mp4?token=vbP3Fn6xcu20qsXg185KCRPJWNv8JwJrBzI9rBH-kg5_alojmveiBSUwjm3IEMejx5hs6vJ9eMPsROPeDUJ57FP2FQnKNNVfeo9XbJQNii6Fi94mhprgJfPIofNU-PjePmkM8MmSBHdmMKZiZ1ZqLqRNxeeD_Zs9nYkmh3aA9npZeJTs4YIS1qffip933nR_Qq3F1JB3Jh0NbeDm1B_lkqO9Ggmcym0Z7XfMw4r9n9Tw9YdWuzDf1FHhpqoSBf-cwr88PIxEKFGSPQ3stPigdtZnV-yLZSSCgrJ2WktSi68FqQaYOIRiu-Ja2zlLJgK1bASMjwW0UW36qhdHFMP75A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea44f33918.mp4?token=vbP3Fn6xcu20qsXg185KCRPJWNv8JwJrBzI9rBH-kg5_alojmveiBSUwjm3IEMejx5hs6vJ9eMPsROPeDUJ57FP2FQnKNNVfeo9XbJQNii6Fi94mhprgJfPIofNU-PjePmkM8MmSBHdmMKZiZ1ZqLqRNxeeD_Zs9nYkmh3aA9npZeJTs4YIS1qffip933nR_Qq3F1JB3Jh0NbeDm1B_lkqO9Ggmcym0Z7XfMw4r9n9Tw9YdWuzDf1FHhpqoSBf-cwr88PIxEKFGSPQ3stPigdtZnV-yLZSSCgrJ2WktSi68FqQaYOIRiu-Ja2zlLJgK1bASMjwW0UW36qhdHFMP75A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇲🇽
در آستانه جام‌جهانی، معترضان در مکزیک، تندیس‌ بازیکنای جا‌جهانی رو در جریان تظاهراتی برای افزایش حقوق‌ها از جا کندن و لخت کردن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91165" target="_blank">📅 15:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91164">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e51373c01.mp4?token=VL8gudekwRWY3MoG-hFWO2PxCso8zV_6p5syz06j1EqZWCsHNtr6SFjadSXGPidAT3CZjOlmd4yX2yHJl8JygmRGGg1T7Seii_MnXcysInRIQERfznU0xMJ1De2hCY-lEkkdAmV7FI1y0YXzgA87B-ZGrWgsV7FFsdwYdSMn0kDKAdfoxHNAA5kHfvD6gtf-Z-IdXtOR8zo28d9AV2olYXxkh1_8A9pQA35LnrvP-WflvSTkqByJJoE5CY5FMzqPIy3k_1G8pr9osYI2RbW-XYKQaMi1DL6Uj_TnSuUHHQqhU2EMLVH5F_MB_u1asO4jC90eKlhO2QWmVxgVhc1LnBYTUglnD8OWawnceYAhKOhAGQl8_zk995AA4NLusaMDSSux6aDGklELv9j4N1rinJfSyQ9kr0gpmU1cBmXzqoB7A2EiNR5mTN5RjbdTUEY3Dv02LiLuNbnOe-d5-Vt2m2Vh2Fy6X4B7rGAXLcL335hN6AxkI9YIVuh3_R8O-Y87OC7w2XjQyhHHIjXrxDx32NjRNpB4as3BHqknE3AmnU0uMfBTMZIgmW4hgXEPHcozf8XXZrEhhYkJ0iD07RcrdBy8lBm73p3OZYfhRhITxbUlGFYQ_CqNGKCRASkwa9J_fdNFJf88HHwwtkfKPCqkSkWV7jxVrBiu1VZKQJdJ2K0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e51373c01.mp4?token=VL8gudekwRWY3MoG-hFWO2PxCso8zV_6p5syz06j1EqZWCsHNtr6SFjadSXGPidAT3CZjOlmd4yX2yHJl8JygmRGGg1T7Seii_MnXcysInRIQERfznU0xMJ1De2hCY-lEkkdAmV7FI1y0YXzgA87B-ZGrWgsV7FFsdwYdSMn0kDKAdfoxHNAA5kHfvD6gtf-Z-IdXtOR8zo28d9AV2olYXxkh1_8A9pQA35LnrvP-WflvSTkqByJJoE5CY5FMzqPIy3k_1G8pr9osYI2RbW-XYKQaMi1DL6Uj_TnSuUHHQqhU2EMLVH5F_MB_u1asO4jC90eKlhO2QWmVxgVhc1LnBYTUglnD8OWawnceYAhKOhAGQl8_zk995AA4NLusaMDSSux6aDGklELv9j4N1rinJfSyQ9kr0gpmU1cBmXzqoB7A2EiNR5mTN5RjbdTUEY3Dv02LiLuNbnOe-d5-Vt2m2Vh2Fy6X4B7rGAXLcL335hN6AxkI9YIVuh3_R8O-Y87OC7w2XjQyhHHIjXrxDx32NjRNpB4as3BHqknE3AmnU0uMfBTMZIgmW4hgXEPHcozf8XXZrEhhYkJ0iD07RcrdBy8lBm73p3OZYfhRhITxbUlGFYQ_CqNGKCRASkwa9J_fdNFJf88HHwwtkfKPCqkSkWV7jxVrBiu1VZKQJdJ2K0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
یه ویدیو از بازیکنای پاری‌سن‌ژرمن موقع ضربه پنالتی بازی با آرسنال منتشر شده که نشون از زرنگی شاگردان انریکه برای گول زدن بازیکنای آرتتا داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91164" target="_blank">📅 15:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91163">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c5176bab.mp4?token=d7afkTx6hwdIc7JINnXYX__440tQMm5jKnxxw5MWiDD9XOCBd3U41rp3dXc9nVBgg3NLCjfpuZ-XTX7HRw1cNTtM9CzNrCfU_LD4lFwAyYYSb3oGjM2R_uTkzPmUmsEy2lyDqtrnmsrl1Gxr9FGhkZdTcVJ9ccfk519say-o08GryXwJrfMYMBskUEBjIvV1HXyYc6hXM5sq2gVZc7Ec9R7K_S-mLhFOhbtOjL5MpvQ8jCbSDL8kKnds58FiR-rPHCd9Y0GYQrmvscYFRK3EzPpyjCw8rP_9owZMgVkqI5vhV4dfzvlW3e2xcgvLAl9AKk4tpgSe3z7MAw4OKc95aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c5176bab.mp4?token=d7afkTx6hwdIc7JINnXYX__440tQMm5jKnxxw5MWiDD9XOCBd3U41rp3dXc9nVBgg3NLCjfpuZ-XTX7HRw1cNTtM9CzNrCfU_LD4lFwAyYYSb3oGjM2R_uTkzPmUmsEy2lyDqtrnmsrl1Gxr9FGhkZdTcVJ9ccfk519say-o08GryXwJrfMYMBskUEBjIvV1HXyYc6hXM5sq2gVZc7Ec9R7K_S-mLhFOhbtOjL5MpvQ8jCbSDL8kKnds58FiR-rPHCd9Y0GYQrmvscYFRK3EzPpyjCw8rP_9owZMgVkqI5vhV4dfzvlW3e2xcgvLAl9AKk4tpgSe3z7MAw4OKc95aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
💥
رونالدینیو به یامال: این راهی که تو شروع کردی رو من آسفالت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91163" target="_blank">📅 15:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91162">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvvlHcav20HUYmWLJYF6q0ayrPRCCTLAfxD27OKS36_tEap-6GTXhthu4UFbdcr64gm1NL9A_Yophjyr1091z0GiP98M0_zlE-L6CkZzY2o7c3MSoROqrhX1dK4HAyBunLvU7dgTXjf1z0BGVjX-lXr1agbFVsIO5-c0xOReJ3TC8uqpGuKB79m-0J_fGQq9GCNUc9pMKwn98WFjnCxLg0_T0gkOa4TzFy-BJZoSa5jbdY2aapw1IZ3rrM51_obeHLqnPRJmplZyd-20fVO-m2a-26jDkg8M6MjaSIQAlfv_PDN1MwqxANcB8MO-PpVBnW7A115V_fyHYO83ISOtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇫🇷
عکس‌رسمی تیم‌ملی فرانسه پیش از اعزام به جام‌جهانی و سفر به کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91162" target="_blank">📅 15:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91161">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc14c7273.mp4?token=LCd9Uoj_w3mVU2k8xuFljV0msvbhc8O-QdqCyl4EbPNqGywKhhwikQWpjRr2WCc40fB6nkyfkfggTbtUVd14WCtaV6tSFA58UjC2sYe68KeVRVrcd_c9KMPBqp15Mo7NA0mX3kjQOMC2lP-Dzjvv4qCswqlrAYku_2rEuUcK9EDX9kOhzSjiSMUEbnL-1XQtMFLrinYKb-e4PYuU0g4bJzTyiZIEiVSOOaTF1-MKwRRuohi7tHN2WHs8LizQsTyp4WeQzifgre4R7gGR1ag9crxtcYREwusXNYxraSDXHK0Kf2ZUW5xravSIHPu2lTNfJwfdcamla8zAQMRdjDHLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc14c7273.mp4?token=LCd9Uoj_w3mVU2k8xuFljV0msvbhc8O-QdqCyl4EbPNqGywKhhwikQWpjRr2WCc40fB6nkyfkfggTbtUVd14WCtaV6tSFA58UjC2sYe68KeVRVrcd_c9KMPBqp15Mo7NA0mX3kjQOMC2lP-Dzjvv4qCswqlrAYku_2rEuUcK9EDX9kOhzSjiSMUEbnL-1XQtMFLrinYKb-e4PYuU0g4bJzTyiZIEiVSOOaTF1-MKwRRuohi7tHN2WHs8LizQsTyp4WeQzifgre4R7gGR1ag9crxtcYREwusXNYxraSDXHK0Kf2ZUW5xravSIHPu2lTNfJwfdcamla8zAQMRdjDHLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇵🇹
یه سری از دوستان نمایشگاهی ایرانی از بیکاری اومدن برا پرتغالی‌ها چالش جام‌جهانی رفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91161" target="_blank">📅 14:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91160">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🎙️
زلاتان ابراهیموویچ:  صحبت درباره قراردادهای رئال مادرید در این تابستان خیلی خنده‌دار است. فصل گذشته قرارداد بستند، هزینه کردند، جشن گرفتند، صفحات اجتماعی را پر از طراحی‌ کردند. سپس فصل با ویترین خالی به پایان رسید.  و حالا فکر می‌کنند بعضی نام‌های جدید…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91160" target="_blank">📅 14:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91159">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXdW3E1lQHbZWCaEGcno_EIqM3ZFmxMB_GClS8qmaxCjgrUcp1UgzrfdYBS0gL_a12OLDSfpuQdcmJsydTtGJ61Ongstwf_mYGBjOrkt_eUx9ZOZWpb2uDsNaPY7I010lKU73RLRj0P8m9qcE4aAZygPDMu94eoTgiCd1B8HKS2N6khV2MeJ7IIZU8_pJhwRhrtTtNeA9JvJCz5-6kDxvy3J77Ly_HPqGA7XKGdtrCzIxlL-qyoLeiNc-sSqe-ULcRU_V1DG6m8caQTwHGI_mmPOMydtxjKjTvXtUOE49hH0mQxgQQ-Et9ToQTuB0K9IxnL4rAkqDSyWOdtLJyE6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
زلاتان ابراهیموویچ:
صحبت درباره قراردادهای رئال مادرید در این تابستان خیلی خنده‌دار است. فصل گذشته قرارداد بستند، هزینه کردند، جشن گرفتند، صفحات اجتماعی را پر از طراحی‌ کردند. سپس فصل با ویترین خالی به پایان رسید.
و حالا فکر می‌کنند بعضی نام‌های جدید ناگهان آن‌ها را قادر می‌سازد تا با بارسلونا مقابله کنند؟ حتی اگر ژوزه مورینیو خودش برگردد، مشکل خیلی عمیق‌تر از این‌هاست.
اگر بارسلونا پروژه‌اش را کامل کند و بازیکنانی که واقعاً نیاز دارد را بیاورد، رقابت بسیار سخت‌تر از آن چیزی خواهد شد که بعضی‌ها تصور می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91159" target="_blank">📅 14:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91158">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80803a67.mp4?token=FZ2YUulJcq5HAowcyMwSE0052hdQLW9N1If8Yxn3SYWlekfdQQFwvgbq_1j793PDUI1fYxQmZncQADmywgTPF3L8LY_f0emJYGVtb7NIGk-ZW09OwPYVMXOKAMK8pzGhiGq6dejMc2HOYjKG1ntzHrw6m1TLTMAQVE9pHK8K1qnKls2JTb-cgBN6iFZV-_i1ewtHWWkitRUkOP8wfKdoInjOILz1mfjwfaZbimdB8Ab3Mxbg9iuRFrPlB2X-g4zN-7Cmg234Fd3_vFwKR4H6c48nJ0o1gaMMN5p9bRdAR3vV-x4HerCo0nT5QuNdTJAhE2WL1oukP1yikAu1ZKOiHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80803a67.mp4?token=FZ2YUulJcq5HAowcyMwSE0052hdQLW9N1If8Yxn3SYWlekfdQQFwvgbq_1j793PDUI1fYxQmZncQADmywgTPF3L8LY_f0emJYGVtb7NIGk-ZW09OwPYVMXOKAMK8pzGhiGq6dejMc2HOYjKG1ntzHrw6m1TLTMAQVE9pHK8K1qnKls2JTb-cgBN6iFZV-_i1ewtHWWkitRUkOP8wfKdoInjOILz1mfjwfaZbimdB8Ab3Mxbg9iuRFrPlB2X-g4zN-7Cmg234Fd3_vFwKR4H6c48nJ0o1gaMMN5p9bRdAR3vV-x4HerCo0nT5QuNdTJAhE2WL1oukP1yikAu1ZKOiHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
تیم ملی پاراگوئه هم به این شکل سکسی بدرقه شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91158" target="_blank">📅 14:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so1o7tNhr-JJD7DDDU4EsB4rpyNlc54hFzTJJiUh64iTgUhoZQHJjSvRI54XfS5OA0Hmju7JKeAoBKR--tbqO57qndv6tWrtFlPFS15k4XLar3qu0JY_KCXlKkGpH9o7G4jUTltycOTbGzLpNqSflCnGQZXEVm3QYEqyW-hOgWHby5crqM7qnlKP4jmCbCKlVYzq2cVuYxu7T3yC6Zf3_O0HLntHN13YL4emslITjKsLKzk_qRQLCsbVS1Jb1sOyqzuvhISGqyhnaAFWaeK8Ri_v5zV3M31t9qXO5z8qzyhs6EwUbxcy_avudd1f-F5z4N2ShcnOtJwV3HngewjVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دلیتا تو جام جهانی مجری خواهد بود
🍆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/91157" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mb3Kz6I_TObOztGx1n6tDcefeKMWpUVgaVXBsTlPAV98cOswJkbfh0SAn6Y6JTmeitgKRzEbebXwayIJPZH3tdrOwQe8rm-0_8Jcl9mhJ4yLNdQHq2V9KkrPyUlCP2cs6Uu1UKZFzziewPcZC3W4j7Ie-fCkBWjL5ZKiDwHm6PH5wjA4oyt76Kx1dHelhK_djvATg6yO3ETnSNba5i3INkLXTIwc4lF0dC8SmYdwNERg8bpJaIl4TopGsEBe-eNxb1gBCwd4PUySnCM9yGHEGQIQBSl7fp-8rqGRy830iEtQJ1SEO0h5KreGTFTmBWVqexQqfioCPq8NO-90sqUliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">11 سال مثل برق و باد گذشت..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91156" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91152">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1X9qbUY0JGjy6d5sTaRBIWAxDFqDvZUHx9bwgRaQTxoDiwcv8VA4ROrbFgMJ_384FricJZsDH3pCvYD_RkFLnjTQEQcwb9JmXNX0hF9eu1Y_NDbuTtU39aTdF7H5nouXPv88Cqm8KpHB0KwbWf2Fwkgq4y8jpjdQ2jg7RDFq5-prTDXtz2Icg2zJecHQATVGVhCaND3yaeIs8H35oCNFEOItd3lVYNtE5aE-k-M7mZBgzUobvlKMLsQgRM33bfV1B27MwacEtJLdOmZzZ65HveEN4ukoy7qhHY_rREbeFwhokvxBv1mr_KFtspTxXLYlnGRCRCfGVWMzNzfF9TBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkxiwapdMHDE8iZYkaT5ruXjSDmBzux2D2GB-DpqAcYzHDaplB7lrOwWroscLwYzoQwlknio7YJ3svdeXRa5L2hu3HDjuYfeQHB5aM3qo1HDhF2X3hzLB6rPJ1CyZSFH_YunFclCUhqWrJTkNlMPpoH_Zut2ZzVzt8zRbzt_QFOIMh1-MmwLpFKbLDNc6uwaz2eKfeYt81FAIW77ykK8x9A_j5jYQmpsaJKMc6if74wkTp50d7Nyp1ij010tcEvfRlgByNoMLwJdIq_NTKIEwXWWzfxJxyAKE2GTtWbsrJ8H4WyAB5lm1h_Icj9D6pwHGgbZApu9gWDvE-1icnFfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4ZppLH_THndbWE4jwb6DavSIWjN1yBnvLW5YJKypom5Sjvnb4gaC1tW-WnLqRl2_3IXvheCtsj7mrLW0PWHfcQstOtzYnXhi5SfTrOdJuHWlKrrSp6kVVjcH6ONpJIKQ24x9xl1suQA-YJIz00TnnV2QKc5iB_sZJlslkKCDqmQU92vaoYTYy7f0mZmV4RNGPMMuPCmVAy53XMz-qsTjpTXkCEwYcfYMYUcCBRMSywIai7SNO5EiRDHOCyyu8djqsTZTSb_1a7iGydTaR574wF-gQsYvc4E6_iV9XxLoGIIjL61K4XivGlT1apKusJ59A8dTiFXyIV5dyvUCcSZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jffC5TzlmT4oemHAZKJ1o6272k0LdAiYbKU0mXcJPChAM7E9e9qIAVierG_lMH2CRtHjZJoHyElW41MQYoA7T4ApHDhvZUbsD1eACLfNltThrX3lSyBzkIDkd-TbFO6E5NzdhxFZU6pT9wPqi59xKetjdAunci30bu9uIwpTLwZkwauBDnDW6L6-poF_QrLwudbgA47z_T-sis-Sfpt_SVuDAjwoLOpdjEgbPdSeK8rtcKBkA_fROUJwBrJx0x06emjrZ8J2TXMY96IbSfFWfoI4LdfotOf0anmsHmmhVNbEV2GRaUvdXn9Ym6Vi7V57dJJMvMjgJS6zHSEuwHkjwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🤯
مادلین رایت هستن که بعد از خداحافظی از فوتبال تو سال ۲۰۲۲، به طور کلی وارد OnlyFans شد و درآمد سالانش از حدود ۷۰۰۰ دلار به ۱ میلیون دلار رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91152" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91151">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/je-JVo_07ryXARq3WHv7oHcO8Nsv8eWbNiTsMPevTybLgLImA0-7DzldZGPrvKNTyp-Th_Cb_MC5xtLMdPvICiiXm3enBxyts0erjk4DgB4UvLtB0jN_5kI0x1LkqZPDMNyCowZ-TmjbzkjPaBK_38_LDC4pzF3BF-ihkuG4GiWfX57iZrVnr48QdMupabmDwN4GqFA7R_pDKLi-8KLFp7VeFsQpYQQi92x-q3Cl0NNfgVbhhVQ1JIhUt16tVxgoiDH_t2sTGvPWj4SPh60te4BlDwKflXKGcZUAfaW9fHYlGfGQcvE8QhbQD3va2t6xIiGVDIoIjYi-QBlw_qgaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇫🇷
عکس‌رسمی تیم‌ملی فرانسه پیش از اعزام به جام‌جهانی و سفر به کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91151" target="_blank">📅 13:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91150">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
‼️
موسی‌جنپو بازیکن استقلال قراردادش رو فسخ کرد و یه پرونده جدید به لطف علی تاجرنیا برای این‌تیم در فیفا باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91150" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91149">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtAtxlJVTo_BlFP2xUYPFRlX3EQ1z8BzdT_GdXyyUBgVz31-WR-NmMFym5JTJ3Zv3xPqMS5U5V6azzLqW2aBNAZzWMV2gjQFxp9joQW4fc_F-L-E0sQaZv51635INcvYBJ-rfIbaLk-0F8-TgCIEwz1yaTpAEiejHPjc_kvMf6w9l8E2tpSkEcO9rrOhn_gjIbm9v4GSDOVYN0RzC3raBDpr0JNzU-qUxH1w_DRRtElc70wwc9I-koteGM62NoDxGyf8GCTCrkznYhbrAYMdwSgsjGRBF06N93U1vw7sEdwP7DrcxqO9WOISjGT9MnxWDa4VDYPP7dqVeqXKKYOjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از ترانسفرمارکت، یامال و هالند با ۲۰۰ میلیون یورو باارزش‌ترین بازیکنان جهان هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91149" target="_blank">📅 13:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91148">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
#فووووووری
#اختصاصی_فوتبال‌180
؛
🔵
ابوالفضل جلالی در لیست خروج باشگاه استقلال قرار گرفت و فصل‌آینده جایی در آبی‌پوشان نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91148" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91147">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnA1pdOewl9pprM9OJFyE2MvyPa8UPPlKFukYp6rKW3fCqqaVinlMqwkuBDa9BqNsBpTJ9GxJo5fsRcd3-OaCahH69N55U1EQ-eijXos8ePBaHdr_0HC3Qi7vXCbE6uqsUwOHdce-q1jSBG_kDBfVfdg82CJek5VpG2AVmqI2UdrBhF8CGEf-qjg1ZWjTQ8rcbyQoi5FxjWJvcoJrnSgCEG1r49nwnFi4hgz7qXt7JIGpnui_HpOjxk_Elx9wVpI359Kchr0SYuPG62Dyeyg7nQO2x5B8CyIwDNU1mFI6lCN7h-NU3PdylzD4rfZ1GlbGajBDEcWQboz7qj0hddiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇩🇪
اولیور کان مدیر تیم‌فوتبال بایرن‌مونیخ:
🎙
اولیسه باید از خودش بپرسد چه می‌خواهد، رئال مادرید او را در گذشته غرق می‌کند و به بهانه اینکه ما در گذشته بهتر بودیم فریبش می‌دهد، مجموعه‌ای از افتخارات و جام‌های قدیمی، اما بایرن مونیخ آینده را به او می‌دهد.
🎙
رئال مادرید باید دست از زندگی کردن بر اساس افتخارات قدیمی بردارد و تلاش کند در آینده پیروز شود. در گذشته نام رئال مادرید بزرگ‌ترین بازیکنان فوتبال جهان را جذب می‌کرد، اما اکنون اینطور نیست و آنها هر تابستان باید بنشینند و بازیکنی را برای پیوستن به تیم قانع کنند، ما گذشته آنها را نداریم و آنها آینده ما را ندارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91147" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91146">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
وزارت خارجه آمریکا:
فقط برای افراد ضروری از جمله بازیکنان و کادرفنی تیم ملی ایران ویزا صادر کردیم و افراد اضافی جایی در آمریکا ندارند و نباید از امکانات ما استفاده کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91146" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91145">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htAdaOm-wU6ETPyg5Bqzk-BULg0wAfuCzn-jR0H00E56h2hR9IcAvKIXvoRmiVelLQJaZ7LFoijzkJR8XhdIudPqjFjTTS99IohK_wFff5cCznlLtarPLQou2Z8TgTbCDcgwxOFnt9CxDNfrt7hEhEB5aKtJqMniXClkZBIXMGtx4ab1gFiWph03u5MH3Z_fU8kNhUHpkzx9FbRY_Hqh_aTxJWsIO6QvwVQh_DNRKwFjrOyV4fPllmWlv68AqscM1ZdNuqcCKyqNBZAunHL_BB3oimNAH50MspXy0670lPr8BfgidXWQSSCj931JJ4JliTyoF3oI8lKvn9_WXGBCaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
معرفی مختصر تیم‌های گروه A جام‌جهانی
🇲🇽
مکزیک:
لقب: El Tri (سه رنگ)
سرمربی: خاویر آگیره
ستاره اصلی: سانتیاگو خیمنز (مهاجم میلان)
تعداد حضور: ۱۸ دوره (یکی از باقوام‌ترین تیم‌های تاریخ مسابقات)
بهترین مقام: صعود به یک‌چهارم نهایی در سال‌های ۱۹۷۰ و ۱۹۸۶ (هر دو بار در زمان میزبانی خودشان)
دوره قبل (۲۰۲۲): حذف تلخ در مرحله گروهی (پایان رکوردی که ۷ دوره متوالی از گروه صعود می‌کردند)
نحوه صعود: به عنوان یکی از سه میزبان مشترک مسابقات (در کنار آمریکا و کانادا)، بدون شرکت در بازی‌های انتخابی به صورت مستقیم صعود کرد.
وضعیت فعلی: آن‌ها بعد از تغییرات پیاپی روی نیمکت، دوباره به خاویر آگیره باسابقه اعتماد کرده‌اند. با داشتن امتیاز میزبانی و بازی در ورزشگاه مخوف «آزتکا»، فشار و البته پتانسیل زیادی برای صدرنشینی در این گروه دارند.
﻿
🇰🇷
کره‌جنوبی
لقب: جنگجویان تائه‌گوک / تایگرهای آسیا
سرمربی: میونگ-بو هونگ
ستاره اصلی: سون هیونگ-مین (کاپیتان و ستاره سابق تاتنهام) و لی کانگ-این (ستاره پاری‌سن‌ژرمن)
تعداد حضور: ۱۲ دوره (رکورددار بیشترین حضور در میان تیم‌های آسیایی)
بهترین مقام: مقام چهارم جهان در جام جهانی ۲۰۰۲ (به عنوان میزبان مشترک)
دوره قبل (۲۰۲۲): صعود دراماتیک از گروه و حذف در مرحله یک‌هشتم نهایی مقابل برزیل.
نحوه صعود: صعود مقتدرانه به عنوان تیم اول گروه خود در مرحله سوم انتخابی جام جهانی در قاره آسیا
وضعیت فعلی: کره جنوبی ترکیبی از با تجربه‌های باکیفیت در اروپا (مثل کیم مین-جائه در بایرن مونیخ) و جوانان نسل جدید دارد. آن‌ها به نظم تاکتیکی شدید و سرعت بالا در انتقال توپ معروف هستند و مدعی جدی صعود از این گروه به شمار می‌روند.
🇨🇿
جمهوری چک
سرمربی: میروسلاو کوبک
ستاره اصلی: توماس سوچک (هافبک و رهبر وستهم) و پاتریک شیک (مهاجم لورکوزن)
تعداد حضور: ۱۰ دوره (با احتساب دوران چکسلواکی سابق) / این دومین حضور آن‌ها به عنوان کشور مستقل «جمهوری چک» پس از سال ۲۰۰۶ است.
بهترین مقام: دو عنوان نایب‌قهرمانی جهان در سال‌های ۱۹۳۴ و ۱۹۶۲ (در دوران چکسلواکی).
دوره قبل (۲۰۲۲): غایب بودند (نتوانستند جواز حضور را کسب کنند).
نحوه صعود: پس از ناکامی در صعود مستقیم، از طریق مسیر سخت پلی‌آف اروپا (UEFA) موفق شدند بلیت حضور در این جام جهانی را رزرو کنند.
🇿🇦
﻿آفریقای‌جنوبی
لقب: Bafana Bafana (پسران)
سرمربی: هوگو بروس(مربی باسابقه بلژیکی)
ستاره اصلی: لایل فاستر (مهاجم باشگاه برنلی انگلیس)
تعداد حضور: ۴ دوره (پیش از این در سال‌های ۱۹۹۸، ۲۰۰۲ و ۲۰۱۰ حضور داشتند).
بهترین مقام: حضور در مرحله گروهی (آن‌ها تا به حال موفق به صعود از گروه خود نشده‌اند).
دوره قبل (۲۰۲۲): غایب بودند.
نحوه صعود: صعود به عنوان یکی از تیم‌های برتر منطقه آفریقا (CAF) پس از یک ماراتن انتخابی فشرده در قاره سیاه.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91145" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91144">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7YDFFEVNdJGdPltnmR19XD07r_13aDIbWjJZEqQcLJN-ySxDN2mvYCuhFvcnPpIfC43jn5bnBEyQMc-yTys43Nv2rfHSnkNpljjBEoVUlz3zpquTOQK754Uw_6mA9GqOv_arVgbb2_z9VZ5aQu5lAX84XjYkfTgHrsp_bLu8tXPxGMz1uxjbMrkgDV4qoajCjoxn_K8REkYhS75GOUJgkNoxp27BONz2-pAmkZHa5USusMg_lAW47qOppXsdJg9CyFWO11q-YGnr4haNjoMsGCweOcF3hfbfjvh1MuYCM1QhwUoVUw2gvOiwEWyXco91emxMhtcXNhbjdP_hvITwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاکا: «من علاقه‌ای ندارم که فرزندانم بدونن که روزی بهترین بازیکن جهان بوده‌ام. فقط می‌خواهم مرا بهترین پدر جهان بدانند»
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91144" target="_blank">📅 12:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91143">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR2tknDsG5e1AaAzAIgbWU6h2-qthOrZwb3aloJvtcu_sq2J7CDJSYp2G5skk2b72K-xn9kZtawoAk9n8wNVXhhY0i5rjMfbsOW4Hp90ZafCbifzkHNUw35YsBUs565YqUoTCdDssW4_y6YqIvPq9fVxcfMvd2X4RWfA1D6bEtKiY-CEYsFf-oNnvZKG810dcB_5I2FUtL4WoutyfDorZ33jdbr_DNAPmiUWW-OBycOnQQlQxMdEItgEBPMul07DLHjMNZERraJ4_ibxG71Um8QHOhHcFmthB-KF2jLDZy6jT3PN4-zc3WUZ1aKBeJAib8j5NETnOI6Z0YHLBYCfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
#فوووووووری
؛ بردلی بارکولا برای تمدید قرارداد با پاری‌سن‌ژرمن به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91143" target="_blank">📅 12:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91142">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=d5V0vhx-sc2TKp-_z-QInVwMcgx7Gsb3qLJANgoDgyoquOpGu7d9GSBUpfurgTuNsPM11kziBALmPjZY04JU3VHsL__wAzGjNbWbvQbn8rCNN9RxWAPrFCyvob55MhP_G3vBZS6pwaxIFlzIjEtygpzi_sIbWMvXmutQP9fZe50FsJ3rlCFrgnq23mR5InjOvCWTDxJhC2o2LpouNrZftoGdxkZre9pIEzC8D94Bv5RGP4OYe-Z7DwH1PKjCMnQpRfPn4I-cZBRzmnqKslXhrYOFgpR14sPi5Z5Un0M3GV2lV8H1HY21Vbf4PSrdvcVJUC4a-GK7O9pk8q9cTFq8dzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=d5V0vhx-sc2TKp-_z-QInVwMcgx7Gsb3qLJANgoDgyoquOpGu7d9GSBUpfurgTuNsPM11kziBALmPjZY04JU3VHsL__wAzGjNbWbvQbn8rCNN9RxWAPrFCyvob55MhP_G3vBZS6pwaxIFlzIjEtygpzi_sIbWMvXmutQP9fZe50FsJ3rlCFrgnq23mR5InjOvCWTDxJhC2o2LpouNrZftoGdxkZre9pIEzC8D94Bv5RGP4OYe-Z7DwH1PKjCMnQpRfPn4I-cZBRzmnqKslXhrYOFgpR14sPi5Z5Un0M3GV2lV8H1HY21Vbf4PSrdvcVJUC4a-GK7O9pk8q9cTFq8dzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی ها از الان تو آمریکا کولاک به پا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91142" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91139">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=GSDRhYcvcx7x9w8Q3fb-5ehf1iyN9sxcpjaw3sd3Ys0WSzIaQYnHdec4QWsj-LMV1nw-gtX4QFRumdLWIxvXSsbwJQcLdsjGk-67xUzVxGl7vMe349I5VhUNXgOCVGzzmcH36BbFI6mEC-Y9W5O6kNQQL7n6Pa9NzVItziqyIeXPrezUyS2CnjEpZLFaagq3tUem9YrfDBLWmbQUsOfNxsAa8m7j-XkT4jjdufckVpUsLpIn4OUa0qZPIYavqjzHzUr39eJ-We92lhs0BnPIrOgakybxlkjeqWc7F3OrMcVAuENL5mjei8zJ_MXhhXfSWVh-iNkcKKVRy40VgTfJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=GSDRhYcvcx7x9w8Q3fb-5ehf1iyN9sxcpjaw3sd3Ys0WSzIaQYnHdec4QWsj-LMV1nw-gtX4QFRumdLWIxvXSsbwJQcLdsjGk-67xUzVxGl7vMe349I5VhUNXgOCVGzzmcH36BbFI6mEC-Y9W5O6kNQQL7n6Pa9NzVItziqyIeXPrezUyS2CnjEpZLFaagq3tUem9YrfDBLWmbQUsOfNxsAa8m7j-XkT4jjdufckVpUsLpIn4OUa0qZPIYavqjzHzUr39eJ-We92lhs0BnPIrOgakybxlkjeqWc7F3OrMcVAuENL5mjei8zJ_MXhhXfSWVh-iNkcKKVRy40VgTfJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امروز در کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن
«خسرو پناه حیا کن، کنکوریو رها کن»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91139" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91138">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=qcIRJYQ9cVCpAYgvGw3pKwJg5WNpHj-_PMzPWLdBKNqpQIXng26gZxZMWINxAGeexdKDCty4fPAMcissmarok5zyVmcf1v_vRfwg-soKaV8NiXC8ub2lOymevQm9C9_RaNXRXPUOY0wJ0lH8yhL-vFgrcseNstq6XVqmcSpuWXIslcUr4dlwYtGoZarQKxW0EwBZnQdYm_ZLyVhvm8AhYn7xYIcNr0j92JVYDqJC13nCZbkWAf5b_A6AGz9XvZWo42t3DwJcprYYYnqSYJsODxxYIjz-E5cC-cknhrINTLkIxZFsycPKKXnaLE5fRW3UkG-WNVGayRzWQPkSGW-RPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=qcIRJYQ9cVCpAYgvGw3pKwJg5WNpHj-_PMzPWLdBKNqpQIXng26gZxZMWINxAGeexdKDCty4fPAMcissmarok5zyVmcf1v_vRfwg-soKaV8NiXC8ub2lOymevQm9C9_RaNXRXPUOY0wJ0lH8yhL-vFgrcseNstq6XVqmcSpuWXIslcUr4dlwYtGoZarQKxW0EwBZnQdYm_ZLyVhvm8AhYn7xYIcNr0j92JVYDqJC13nCZbkWAf5b_A6AGz9XvZWo42t3DwJcprYYYnqSYJsODxxYIjz-E5cC-cknhrINTLkIxZFsycPKKXnaLE5fRW3UkG-WNVGayRzWQPkSGW-RPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه قهرمانی تیم ام سی الجزایر تو لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91138" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91137">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAUcfKmSD31P4_qK4PNn3oJH80g_2UT2sJdRins-aTfxNsOYc5CoISd0qOSQuxW0PG0lzETt_2xECaAi3FF16z_3kbL8WQ-XE8N7FvKIlmhfLg6KqNpMmgAZUC1DFHOt0-TGDD9dADAslCSsXkcBkYdCBtgq1YVl7aOog3ZkTbvKbEcqY3T_Q7f4I6DuU1Cn_4lhg0BpDqZQHMbYx6rex28pqg4HNJ_EvBsa2Op13fma7rcRwiM6hPZur_CrXK5pOxZi3x7ZQrQltPwF1c9yz3KOaOhsueN79Ypc8rVcsEdiujlC7z_oJcN_YQwx35ejkiVE45qcJugUyyYt9ot9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
لیگ‌هایی که بیشترین نماینده رو تو جام‌جهانی دارن؛
انگلیس با 165 بازیکن با اختلاف در صدر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91137" target="_blank">📅 12:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91136">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=Ye1fZfP9ZLJ6ZX-nfeiUWMK5vID550N1sOZJkXfmpyKP69AnoTgnl2RpUlloCtn832LwI6v_Re7G6ENFqq5KP710f66QL8jSXjwWelAh9mRqfACGyoUokqG9t6e1ZbczvHOIkAe4JJW6YgPSpczkXBVVJHVvsPCAT-2oeREO7eW75m4q1iypRZW4aOrzHHVD1jccBolWs8DygTfvTHv6g_DRAd1IQMPE49RN5feeXQJ10vePd3Orr6wjcuDkOotIkt5s68HAaI0sSJpwjR_qkT4VbnkIHymGpIIFWcTJYPhdjfYhSlTsmrnFrf92aSIT51ahOQwm1hBNWZ4k-AsOug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=Ye1fZfP9ZLJ6ZX-nfeiUWMK5vID550N1sOZJkXfmpyKP69AnoTgnl2RpUlloCtn832LwI6v_Re7G6ENFqq5KP710f66QL8jSXjwWelAh9mRqfACGyoUokqG9t6e1ZbczvHOIkAe4JJW6YgPSpczkXBVVJHVvsPCAT-2oeREO7eW75m4q1iypRZW4aOrzHHVD1jccBolWs8DygTfvTHv6g_DRAd1IQMPE49RN5feeXQJ10vePd3Orr6wjcuDkOotIkt5s68HAaI0sSJpwjR_qkT4VbnkIHymGpIIFWcTJYPhdjfYhSlTsmrnFrf92aSIT51ahOQwm1hBNWZ4k-AsOug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرکی به ایشون گل بزنه با من طرفه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91136" target="_blank">📅 11:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91134">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAFYXRco2CuictUXN1MmvhcIkA2QyKZnFDv4pP9-UuMV2iIDnTRUpIc7TvB_OoUGEgvasm9dU-zPXGhqO4hYLY73UsyQ2BRUtYE0ekKnu4Xm34bxnHuziu9AZZ1vYtX3FiDILkM4xi6Lx3Bk7aWhY-axLmVXj87bAdlx_cltpHM16e05uFlX9XkOfXxhWu36c-FBn2kY-FR4Y_jryTM8eCDANrq2Zdz_j1G6TZVyeelsBmDns-91hpFLiZFAsqnhitEeh-diOkitcB27G9QroJ0vAUHuLrgfIAV4_kpHsmAwH32_wyNZgGBVG4Lp6J0OdRPN2kMMbbBr7LSGyS1UHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0vpYy0rPBs4j8lms5I0o0kxfy4f2NbeoxZbz1wqiZvzFwD5Yifs9GoMiOKSIvn0OcJ2N-6JJ6neqf-IXA-GxS-jxUXMPia5Ucl4s-VfB1046tg9VoK7JbQLhXEC_JA8mWgP_LzGX6kEpYJC9D5KE4TJy3kJFndlW0FvocQqhbCutyLdKOpC1_Zn3bqTbxlLz5dTgtkKDGbjV3LC5PCgV5byxakVLQTv49nVDl-SGrse6TyfBiXqdxLypUI4yM0dIeQdDakPJKhEWC7ZLfyM4l_P65bM9jLE_L0jk4EkNTQIsOmdf_Y8AkpDc8Fp8wLFe6j_3Yvro3xZoZMzOjr_PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
این‌چهره که مشاهده می‌کنید صدف طاهریان بازیگر اسبق تلویزیون و‌ سینما چند سال پس از مهاجرت و کشف حجاب، روز گذشته با انتشار استوری اعلام کرد که به ایران برگشته و خبرگزاری‌های داخلی هم تایید کردن
🙂
🙂
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91134" target="_blank">📅 11:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91133">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=K6dwOSMNzoNZY8SrlDSQE0Ah1OXJaHEzduWYcp5dT8l9fxWOstvPfhP1K9GzR3VCuAncAiPgigNLgnJuytNdB8-DNC2dUNd2UXrVuUj_ZpkWXaV-KtPSlqbCOSQR7aIRWKJcQMxz4nIHhZ3cd-DEWFOgsMf_mU58lw04oqizpVnDtT0bS6gVJitPMvZ5_j_IK0xuyfCqzrkNpshoYmJD1Q_jz1e-L_2HeUnqmu5tVoQiVGIblRGU0nIwqwiagPh-ue5HAcFlik7LIMcu_YOImVePCpKrHEYMKYpIDJNe14ZAjDj0h3gP4eYNMWQg-zUN0F-BVBz65NYSi2IVfztK2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=K6dwOSMNzoNZY8SrlDSQE0Ah1OXJaHEzduWYcp5dT8l9fxWOstvPfhP1K9GzR3VCuAncAiPgigNLgnJuytNdB8-DNC2dUNd2UXrVuUj_ZpkWXaV-KtPSlqbCOSQR7aIRWKJcQMxz4nIHhZ3cd-DEWFOgsMf_mU58lw04oqizpVnDtT0bS6gVJitPMvZ5_j_IK0xuyfCqzrkNpshoYmJD1Q_jz1e-L_2HeUnqmu5tVoQiVGIblRGU0nIwqwiagPh-ue5HAcFlik7LIMcu_YOImVePCpKrHEYMKYpIDJNe14ZAjDj0h3gP4eYNMWQg-zUN0F-BVBz65NYSi2IVfztK2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوستان حکومت اومدن یه سری تینیجر رو دورهم جمع کردن تا با بساز و برقص از تیم قلعه‌نویی در آستانه جام‌جهانی حمایت کنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91133" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
