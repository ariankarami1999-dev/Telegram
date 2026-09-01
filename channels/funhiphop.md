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
<img src="https://cdn4.telesco.pe/file/h4bhgIienNEXV9I5gJWEIPBJVWKcIrM4fmybBnBwZL87Pwnd2QZqNKchsKbb56jswrOn46eIV-0zXEo5307VGPMZO0gIQM37c3sPkEETpDRoI2thMZhaxmDheDmuUJXb5soe4fRMC5_R2KH39CE_BukAHcbFFzF_5oU5X20uF7zRzeb198uCpe-w5z9W5EokVt2F_vCxSv8BC7k32Sm11KSPQACGAfovXthDv72GS2E0W29nByp9wA3eo3YZJT-KkLhLdLurXZdjdACZrJLmNma0NeQofFuYueWgHALzjK_TTDopj5_geq2hzTwfDZ0h9kLwxs_PjZ6mSXjh4xda7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
<hr>

<div class="tg-post" id="msg-82853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2eJyYtGj_mnyWz945tGYKaz0kD5MOlxIbvMf7DWo_hEVH3JCA2cIWrEW_h_W0l3i16j4rET5tC6LqHdFSjw8fyqX8_l30ks8GZT4ia3ygcMYjoeLXunyuhRhURwBA-_bmC1TDOX-whIa37GADb-BkGcMEzd1TfnmEjL23W7Wr-pkY1IvzTX9GZSYDNtaUEaUn4SyNtOPbEKMW8x7BoIkU0S5fnW0yJtnftQr245mt_QLR-Kkff_Wa_vG8oyo0VREDwC8G_kASiaDbY7slkTtbtMY8nrV36qo_QU_KSJTUalSc_QzOsZ-0STPrEoU99_cK8bbVyTgTBLDHsDUY2XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوام زندگیمو بزارم رو این
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/funhiphop/82853" target="_blank">📅 14:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82852">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebbef3244.mp4?token=SWpy5hM_M5deNPpoyMEzk1avoGrw-J_lOE2ZnKE-3RE2fG_vXt9bdGXzxA26jRJht6w7lYg7Zx0JDYK7pxJuyuIGzR1HmSHFqRPWzF7LQwcKnhct4SPy_wcM9Uw72xr4nhaG4EzN6TGLCx9YeKcA0e5l0FV9Lpf2TAiffvYl8cqkZti-TuhvA72l2_Vx9A7ovQRB4pezkNWPDP8ks0YsKStuL8mZe2H5Dof5HjvQB5ELe7ngGnX2Sk5hL8bAFCwzgrS0hD8_-BUEknQV-DRpMSU3HzNo2ACh0polcOjzai0_97A4kreNxyLOFzFpNhBT9KuxAwFVcFLR68raVCf5oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebbef3244.mp4?token=SWpy5hM_M5deNPpoyMEzk1avoGrw-J_lOE2ZnKE-3RE2fG_vXt9bdGXzxA26jRJht6w7lYg7Zx0JDYK7pxJuyuIGzR1HmSHFqRPWzF7LQwcKnhct4SPy_wcM9Uw72xr4nhaG4EzN6TGLCx9YeKcA0e5l0FV9Lpf2TAiffvYl8cqkZti-TuhvA72l2_Vx9A7ovQRB4pezkNWPDP8ks0YsKStuL8mZe2H5Dof5HjvQB5ELe7ngGnX2Sk5hL8bAFCwzgrS0hD8_-BUEknQV-DRpMSU3HzNo2ACh0polcOjzai0_97A4kreNxyLOFzFpNhBT9KuxAwFVcFLR68raVCf5oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بنده خدا در پاکستان داشته خودروی بدون راننده‌ای رو که خودش توسعه داده آزمایش می‌کرده که با ماشین پلیس تصادف میکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/82852" target="_blank">📅 14:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82851">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فردوسی‌پور بعد از شروع مجدد برنامش : با دیدن فوتبالِ لیگ ایران، می‌تونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/funhiphop/82851" target="_blank">📅 14:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82850">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فردوسی‌پور بعد از شروع مجدد برنامش :
با دیدن فوتبالِ لیگ ایران، می‌تونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/funhiphop/82850" target="_blank">📅 13:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82849">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxVpiC22DvJl52GuMUy4it5H-2j9byHEEdFiyTwh-oXPDnv_jOKwNBczlWyuOFpRjByiR6-UCU7WYnmjSxWTYVwU4QhskJxi-KsO6fObe1ECfi8mnYT1Xn8POK9k6xw_Nn7q4oxZMmEOTmkffXowl8CpXxYqQ1KKl9HIYkIx4qbuUsNsOUvlE2wkkUTCgbuB9ha8UT2C-ac2PVomJL3GqlKjT3luEKjxydjDhBiiHqmpnNdKZUAUGzGmOUvsfqb3hHR5f-z8hTy0IZo5OD7sCtBw1fxjSlxnE18saEyS7pYIy8dsEtpF165YmV5jB8LsAkSPcybr8FLAV5-HX35prw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه تنیس آزاد آمریکا
🔥
⏩
روزانه با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۱۰ میلیون ریال بر روی رقابت‌های تنیس آزاد آمریکا،‌ بدون توجه به برد یا باخت، در هر روز از رقابت‌ها مبلغ ۱۰٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/USO31
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/funhiphop/82849" target="_blank">📅 13:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82848">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMG0yhUilRuvpDQyn1jhl8lxuRGBjcHxLFUiudZxQW-hHE08HR58qa3vgQDzFLAh7KyvkpsQD9vOaQgdcgyih_7tCpYn0qhqn_RO2hZ8ZwMSqswozoEylQdPAm6FewR2j-JfQDxs6mEnJVx6A8ceFKxzjOu-_AjtzQN22AlDHa9P-jiqWMe3O5tiFDCeyYejXpgsp90uxqQt9aSFgagRMmKIfjXGazclelSA9_6OVj6HDLbARL2xAMpqo2JR4p98Z2utsKa1XWxGSTSbMooD4QPnS4lLX3kebaS2LiAnRTxU-t0nTfDmGOwrUMX6UcKCuxl2CpKbuQepeChbJHTxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من جای نخست‌وزیر کانادا بودم بعد از این توییت، کل نیروهای نظامی کانادا رو منحل می‌کردم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/82848" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82847">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/003dd1185d.mp4?token=A-gPRMISeIqCy8syK7FMhT3oVlH5RlnFSlsjBQ8kOmjO8urzQkVtP46p7vcEl92dTHGtH--E7ez_jyfmo3saDCGOs42eLEARQdXJYu1ctNzk7MbGCCgNK0g9I6KvNDsMCDNHZQvrykuMd9ur8JbOZdodLgt6JubnVRTl4KHceeY-FJnu37YlNb1bNFZ4Nvgc5XukbshXEnfWv5AAeSCpUxDNWVkVdL5Cnexyj9bMWMt6s82gCTP1XKvrE87Y1TXgeZW1TZtnqdb_WLcVsoWvS_FSoeiJa7xAPsC0mKzE0einOPyukOb7MXNyHfjWqMyCYM1H61q220LhrmxY5NgmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/003dd1185d.mp4?token=A-gPRMISeIqCy8syK7FMhT3oVlH5RlnFSlsjBQ8kOmjO8urzQkVtP46p7vcEl92dTHGtH--E7ez_jyfmo3saDCGOs42eLEARQdXJYu1ctNzk7MbGCCgNK0g9I6KvNDsMCDNHZQvrykuMd9ur8JbOZdodLgt6JubnVRTl4KHceeY-FJnu37YlNb1bNFZ4Nvgc5XukbshXEnfWv5AAeSCpUxDNWVkVdL5Cnexyj9bMWMt6s82gCTP1XKvrE87Y1TXgeZW1TZtnqdb_WLcVsoWvS_FSoeiJa7xAPsC0mKzE0einOPyukOb7MXNyHfjWqMyCYM1H61q220LhrmxY5NgmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری اعتراضی سنگین جهان پهلوان هادی چوپان در واکنش به حذف شدن از مسابقه ناعادلانه دشمنان و ناملایمتی مردم کوفه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/funhiphop/82847" target="_blank">📅 12:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82846">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3tlKKgE6q_beu-zd66zb22PaFVagTnNQAx_SzhbFdUQMzzJJyOsd5MJIm6eIYPF94DzBgh_ziyefP9AtE87NeWXdYIuRtOK5jN6_BeHZt1FddILKkGG8Ccj5CTommQ4DFO2gZhI-gxDhcC9B4VcSh8TWT0S_AD4wgyOqeIe0Z9YThvHQrr6FEA9q8-OVcsHCreRp0wa6wyqjXZ2k-o3KfiASRxKaXuZ4GdeqqxkPvT1SES6Sd6-hzULT52jCxdQA7L1Mg7CS1j6doEh7SI2eXZx7IGp4r9MLU-21oI8Qp7DmTTmOl3_9U9xREiWagSX75sWGwrSamFgrmDZnjWiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیپ لام جدید تو اروپا متولد شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82846" target="_blank">📅 01:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82845">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کصخلیتی ها.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82845" target="_blank">📅 01:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82843">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChXrU3t3zvr9kD7cvM4kavymleuC0loHSkrfhj7ph2mu3KZbKgKfM22M0X1SmzlhJgmLEd7UgdJoV07j3WReZRtXhxMYJCVeaG7jbCXaaAGyfrq-8Ahp_t3h6WF3TaSUJsbH3O987HsIjoFXFEUXBET1crrQ64kBVfHY_qpL_dxNYy_-9Pu1IrzXksBlg3vFRYytavJWX4xEpQSFiRcBUuTdJgVea8ho1V6F3FIGbz8by4h2_9R5bvMdK6suBQcVgZGgP69-cLzgl_QAMSvcgN3TuYYqJlmUUfiYD1hY62Kop94-M7oXzR5IJ8Egkrr5xrCCm9vDVL2YQP3zbyWANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=Gbv4Jn1tH_yo7hV2E2HeOpjIO57Mm6Z89PTolEkjgj51JZ_3hR5OrfBY_UzvIuh8nUqZu8lJDRKceD5ews9EjAnR5TeQWsBz_L3cRzteyC_Sd1NyUM4yQ23iMDMphonOj8lYRfziPdulzfYFsSI3jRPj6Rjy5VAzesEhJUebB2fw44AWIpJit7nSOwCwjTHuY0bYHMFr3t9nEsRlS_7ZycA-LlQ1LlwnVybuTi_zKFydxca-Az5QAEGMppPJgqA25XPHZOavgGs-96UKTsHZZ5YkpLFdEw6HljWCGFLNNNGumpIedfHQY-FrCzU5Ilm6MWar0jH94TWv3AJOc4yctQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=Gbv4Jn1tH_yo7hV2E2HeOpjIO57Mm6Z89PTolEkjgj51JZ_3hR5OrfBY_UzvIuh8nUqZu8lJDRKceD5ews9EjAnR5TeQWsBz_L3cRzteyC_Sd1NyUM4yQ23iMDMphonOj8lYRfziPdulzfYFsSI3jRPj6Rjy5VAzesEhJUebB2fw44AWIpJit7nSOwCwjTHuY0bYHMFr3t9nEsRlS_7ZycA-LlQ1LlwnVybuTi_zKFydxca-Az5QAEGMppPJgqA25XPHZOavgGs-96UKTsHZZ5YkpLFdEw6HljWCGFLNNNGumpIedfHQY-FrCzU5Ilm6MWar0jH94TWv3AJOc4yctQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پیشرو داره غوغا می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82843" target="_blank">📅 01:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82842">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حالا که ما رفتیم ولی ارتتا مادرجنده به این کاری که دارید میکنید فوتبال بازی کردن نمیگن</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82842" target="_blank">📅 00:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82841">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAo8REfESi0Yz90y7zD0gsT0lPq4LHIPp9RzUxefrcHkg99F2oVaifB3HOU86thXPBB2lXRFkJ5JNQRii5eDUxi9cc4_LZhaRz7irE18iz7Jt4TxjdSIiy7MXdgq4N-pI7snV0XtXeMhOCF4tkgfrOIEFnF-v8sBL9LBrti_-fCun6yF0rJyjiF0p3uJE1af-EbsobIZRI_ZTbwEgI__D91Up-JGj7KNnfd36LFt95G7PxysVrQfcKea2MALn5HWPPl_YGpQ8PVpv-V9pSB2dElY4Erx9FCNgRmr7AymCvdAhtHmR-h6fLIxrH3n7rpkh9kuzKKzfFL2o8PAlL4m8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خایه ام اومد تو گلوم</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82841" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82840">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsQZ-sGFpXwuf19mZvqnrLgkjAOTFfT5ZHfG50QPs_kZSHqKWqV2qir59H14AkEvGFQ-i0gM0JUJJ6EgYJQWDTOFJuyAjchjUkEF_5fCV75bdReJodbBDr-3aSCf_ve2XXzaqAK3RXRIbMD3wAsgVoQj8OeWfhoCa9BNK93GSKS38OLKpWoMmUH6OFBybnZdGQ1uDd5jtGu5ajzTQPVepAKXTFXFHWHUWOOHKS7HzkjT__NMiC2wNHTpCy1mp1KmjuAtBFHBxWmL1R6z_BUiYOCLUrT8PYP-LAIGKDZfZN_ZgGAvWDQigj-_RRG6OtrrrVggzFKdVkDtxr7j1UEJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشه یه نفر بتونه انقدر اشتباه کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82840" target="_blank">📅 23:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82839">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzSR3GaiGjOsBDR6oYB0ECRFRolZqmqvxfzQtKjISpoWetJsvWGlBjOTFuSe7Ge_0p1R_TMD45_m-lNKL5QwajlH3m0yLpi-ap2PfVLEB5hyUPv8SUhW9BXip2Xm81PgrB9wydLpO_2MDAyyWyovvd5a6ztnjpulQAhzfVSc6NJI_kLJDjaYHB4ThGVboHPxew2MOmFEYf77X8lNrQFh1wV5nkE2JVuJ2IUecpHRF9S9izS5f3xRQNukeREDE36rYEy2R0Nowbhwmjr_mU4w_x20oWSD4Z43CU2Geg6qy7uEM_DHGncm9mDpcr2hbbKmYSxtQ5q0M9SkReDyzOm2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این چیزا جی تی ای رو پی سی قراره دیر بیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82839" target="_blank">📅 23:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82838">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پزشکیان در واکنش به تذکر رعایت پروتکل‌: بابا ول کن پروتکل رو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82838" target="_blank">📅 22:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82837">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پدافند جمهوری اسلامی یک فروند موشک به سمت جنگنده F-35 شلیک کرد، اما موشک توسط جنگنده دفع شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82837" target="_blank">📅 22:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82836">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpMylAACAHMd4gLZiV8-GYUtYJI20DYwxvMa8wX19sfh2-ihKvnUj0FdiTUbMNkcb-cEihQfn6wD3LmfGnVUcUWEYtf2Sq79WfP1T9bn0PWsrwuJ2PPw4dSkOOnLtIVqNrGK_2YID_OPXcNawIxogTD_LXjqTawn5snBd56fjXjlTUDokwS1Qjb3VVShhr89JQ7A9TZ2WBjeMJn-1JHZSqtvnXg7Fn1aLzgsJGQaj4Mz48w92oouKsNkLddm8YjinnDolzMQhdMnpgl6KT6Yf3-8V-sFhHsDxjMjr29MbNF3VsQutEImAS8eYTeuOyKSCUYdmpY8cO8i9UhtBsVSjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک بیا تو چنلش بگو دکی پولمو بده بخندیم یکم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82836" target="_blank">📅 21:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82835">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ گفته میخواد امشب جنوب رو بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82835" target="_blank">📅 20:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82834">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEflZoaAo5sSjQSN53Zmhb0tOw6_Tu58DBQ0N4_PjR8u3zD8cwsHgVp_dkeyg_Ps9yNxTdmDV4U-5SuZIAHyFExbUY8mzIxMD1w583YeZ0MzkfF5N4bL868lsa8ykdyS2532VPCDSQjJR5qfosVPrQlnSI1JRDM-AqU5_d99Ntoss_JT1SjwBmvQmWVz2amgYIuwsS5wKhJ1Z2guBN5Pc3gnslqw-YkF1vxCFe6gxNts_JkyYTMSkDw75pDMhmyUrUD1RcXi-ta5FQk15vQ2mzI0E8w70p4YsbMeWk9DZ0Jg4zXVcM5Z2uxRSiRWjqu9Un9Bk6mb606wPsfsOQQyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمدزاده از تئاتر "آرش" به دلیل استقبال کم مردم اخراج شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82834" target="_blank">📅 20:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82833">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مسی از بازی های ملی خداحافظی کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82833" target="_blank">📅 19:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82832">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دالر ۲۱۳
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82832" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82831">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdHrZMmcaWXX_6DgB0ibtWpT1tdtJf3K8OW_I5aChfR2VEeJcQHvyAwL8aW_53mA2NZDUpKZBrtvCQX6cTU_8hqHXShFlMUCubdoP5PexXSzBbrQCMmvdIuE0RN91uquGRWmqGdr2CwJ37lXXJTrlUG1mdqE0x_ba-mEySaIa9Y02M4e7HgJ3kdYxMvv98h88UwIsfsEwL18ZBFOMhgx2iqDj1rWMFu1Q7NUeBRyH5lN43hVNmYlplVfuAJF7jt8OK3igRf8nBA2RV8mlIrZPDwet_4KJyOiD8QY4Ye7QQQaflKqTwtwvOihDBEoqgvrxA3VGkdPJcHrLf3YwsDBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی از بازی های ملی خداحافظی کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82831" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82830">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hilHw6BLlKTxNBLFnooO4g9Az9oBhEBDdM0hcNOtIUrG0n1NOmfsL-G0Hf3yhKhejggbOROJ-5ToihyXuOgRajTUhgq73CNq_KtyLBh4KFpLBx-en0GbKA5GwC7-HlBgpPEdYjFfXfCUfrbs5VUdoeIFuxU9M7ZIrb3fdozOYw4Gt4kSmEprgCxc02Ve45v_cQXI4JBYqAh0T9sUu0L9O8QdYLLZBJh4McBdnV0lSYy9Yi_W2bTufuxJ6YpzgzJCKuvapCN2WwvBbgX8wm6da2TiH1jICTuG59s0LNAs1DZpcVK9KQgqzR3f2Qga7g6pMxthpySa2xjLBG6QFcbEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخندم و رد میشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82830" target="_blank">📅 18:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82829">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شما یادتون نمیاد ولی یه زمانی میگفتن تو ایران شاهین نجفی گوش بدی دستگیرت میکنن یا اعدامت میکنن</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82829" target="_blank">📅 18:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82828">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شما یادتون نمیاد ولی یه زمانی میگفتن تو ایران شاهین نجفی گوش بدی دستگیرت میکنن یا اعدامت میکنن</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82828" target="_blank">📅 18:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921c1bee68.mp4?token=FKL7SLNkF7nm9Kr0htTS2PLLjkFAH2UoQP_4bLlpCUki6l2xkdwsgQaux-JP4ezzHxXDJJzEuCETy0IhcBBrSE4VgwWNIJc_QsvKHvI611_0BOyuS1oG6Y7SgHoxxLEApV-HPdWJdOws24yAUqOyhqC8h-LWFd1eVxkpHFyd-qc1K9f9U2ESFFcTNZ5KYZtstfZ_y8_7OZSK080vd2QmYhAV6gFMwp7YKu74hSA2GHHkacNuWpP_blptyTYbGuFMMlWAlyiwmYUiqFbvPQtwVsQn49u60QQgOdE1jtq6Nkf2i7VfdhYsa7wVyMsIVD_rG_GVORCsQYYimRcJJ1jOwIczFoOsYpbXSD_V02xqcMNjv-LSmLi57D6mhlYqqgd-GX6EEbA9fUXPLs36nJHV5TfA8TqdB0mIo7ocmXmyXginCq6iJK4zhXKgxY249xVuoT2Aeks7wcJUUb2RMm0M-0-OXBMVzj8rsjIqGuRPi2lr1M_iqNBVvNbHTVtAOJjM_2VBD93ehodttMew9ZHRI8UgQ_p6Il0Tn8CTGaO8vTh5Q7h_dbeCLYUFZyYeJp4swCME7cyhN09pUOwDG6MS1i-WM5xuUwJJk6wO0BeNGAv0cPJLJ0qix2K6gCSkQICYB4dSzveg0dUDgw5Oy-0OdKu9JBqJ3KZu-AIheZwLMOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921c1bee68.mp4?token=FKL7SLNkF7nm9Kr0htTS2PLLjkFAH2UoQP_4bLlpCUki6l2xkdwsgQaux-JP4ezzHxXDJJzEuCETy0IhcBBrSE4VgwWNIJc_QsvKHvI611_0BOyuS1oG6Y7SgHoxxLEApV-HPdWJdOws24yAUqOyhqC8h-LWFd1eVxkpHFyd-qc1K9f9U2ESFFcTNZ5KYZtstfZ_y8_7OZSK080vd2QmYhAV6gFMwp7YKu74hSA2GHHkacNuWpP_blptyTYbGuFMMlWAlyiwmYUiqFbvPQtwVsQn49u60QQgOdE1jtq6Nkf2i7VfdhYsa7wVyMsIVD_rG_GVORCsQYYimRcJJ1jOwIczFoOsYpbXSD_V02xqcMNjv-LSmLi57D6mhlYqqgd-GX6EEbA9fUXPLs36nJHV5TfA8TqdB0mIo7ocmXmyXginCq6iJK4zhXKgxY249xVuoT2Aeks7wcJUUb2RMm0M-0-OXBMVzj8rsjIqGuRPi2lr1M_iqNBVvNbHTVtAOJjM_2VBD93ehodttMew9ZHRI8UgQ_p6Il0Tn8CTGaO8vTh5Q7h_dbeCLYUFZyYeJp4swCME7cyhN09pUOwDG6MS1i-WM5xuUwJJk6wO0BeNGAv0cPJLJ0qix2K6gCSkQICYB4dSzveg0dUDgw5Oy-0OdKu9JBqJ3KZu-AIheZwLMOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Send him back
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82827" target="_blank">📅 17:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82826">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgRYHdi3oQc_G_VflZVn3GaJv8vBpPwE05BxBLdFaruNDk4ZbaqllxvpI79wN1hAoxa5akHb4HE-B6aY3jmypHSsJ481UqoS8hD_A3Ppkmruxh8Y8Or5mjnefet3pICG0IN0LMCmDr7Osb7DZsuPlcZ9OYvyCGi6UY4A4JgydFJTTXiS4mV0YVehppIKJhi-nY_CzuyxsaE1BiCSGCp4xKjGao_Y1hrmDLmr41V6Kf0fUj7Bg_YYw7bclvFST_FCNX-gt7jELJXSuwWl3vLtod7_P5YPVcoIXtVJ9Q9Ed2_Ajl8UhG38cdILcoDDOjfSQ94sPrD_RGoBLSt8BOePbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استون ویلا
🏴
-
🏴
آرسنال
🏆
لیگ برتر انگلیس
🏴
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه ویلا پارک
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۶ برد سهم آرسنال و ۳ برد سهم استون ویلا بوده و ۱ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g9
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82826" target="_blank">📅 17:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82825">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc3i-g31bgNetgABN5ccBMZhMorQ8SPvsP900nEHCf4S_Av4dmvn2ejGpLicJViHyGR0j69cRalKsZ6VgKIoeN8XSMgdCozw6Aed5SbyXykmGOFaGN4lzgRYbCOmXB1zIaZnwBuxBMRgUMFid1Lvem4JUA4b_5XdFGr7Ihv2wAzM7i57dhxZSQbU-eAM3m14KSRFm4A0INdeOJv1Ze8axCz0ZBZyV5WFUP4M5UUPl7lea_DTxNpi8UdfKp36FZceSlqnq5-D9fsar_5hejeN2W5yyrguynVkohRjQ_5DkuyfFd_PMtEhTfc3oaQ8MqfrbO5sYQyWxdOaZr9RUSVS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاش اون گوشیا رو بکنن تو کونتون که انقد تو خیابون از ملت عکس و فیلم نگیرید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82825" target="_blank">📅 17:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82824">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9062dc2e0d.mp4?token=B11KHidgrtNX62s3SLwb5bAZBAMdX01dcQl0FmD6ZnA22q5Pq1IQMUUQ_mzq0ch5ZMZth2YsSYJZIrDiUOTjmsI_V7gDbZq01Jo_ialxpvsR0savUemZo8NJXmBA79izyZwA6X0DJRzGDuO5BWx3opyxGd9aTFZDltRK4GgEsjDbpXuD4Zd_XsvU5RqqcPmmA_Vc-3eAohQmN0ioVzHQU4qe8ePBWEpB6TBQZHuguBkN-hAlNlZFN2tshtCtsYDDvxSV9TYLWZJXDng_mS3Dec2pbC-ra7ivABG6U_mQrUImgdAJ4ZsAbq2QtrcNPmqZ-PV_Wc52aygC5jNrYNc75g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9062dc2e0d.mp4?token=B11KHidgrtNX62s3SLwb5bAZBAMdX01dcQl0FmD6ZnA22q5Pq1IQMUUQ_mzq0ch5ZMZth2YsSYJZIrDiUOTjmsI_V7gDbZq01Jo_ialxpvsR0savUemZo8NJXmBA79izyZwA6X0DJRzGDuO5BWx3opyxGd9aTFZDltRK4GgEsjDbpXuD4Zd_XsvU5RqqcPmmA_Vc-3eAohQmN0ioVzHQU4qe8ePBWEpB6TBQZHuguBkN-hAlNlZFN2tshtCtsYDDvxSV9TYLWZJXDng_mS3Dec2pbC-ra7ivABG6U_mQrUImgdAJ4ZsAbq2QtrcNPmqZ-PV_Wc52aygC5jNrYNc75g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشآمد گویی فرشته حسینی به میهمانان شوهرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82824" target="_blank">📅 17:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82822">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f3af0f50.mp4?token=gT845HqaIe4uF4lEEm5D5jNSF94JiTGz5k7N4UZOLFggShiyZol0yAbKbGIn8NSGAFAPLnO50ZjXQWCJgwrAc-4I1t2cpfFRyCaWFMembw8DMJ-WDweweE5-5j7yEnZV6HbIbxqjRzVncnyqJFdqtIH9swffxDxUbDesou8qOb1rEqDQ8TodOGjt4ri2qdf2pXyE-6h3YdHjdPdF_E0FVHFlyYrsa2XgG5IlX6buE2N7wAJjKMMJ-9QqRhxD3L_TlDQVaaKHMtYPZtfFZureAvKByObPn9Xigpky0hcKZNrw_3mUV9GpvXF2ZbCqt5s37X626rTfzX3oRcGYj4uy6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f3af0f50.mp4?token=gT845HqaIe4uF4lEEm5D5jNSF94JiTGz5k7N4UZOLFggShiyZol0yAbKbGIn8NSGAFAPLnO50ZjXQWCJgwrAc-4I1t2cpfFRyCaWFMembw8DMJ-WDweweE5-5j7yEnZV6HbIbxqjRzVncnyqJFdqtIH9swffxDxUbDesou8qOb1rEqDQ8TodOGjt4ri2qdf2pXyE-6h3YdHjdPdF_E0FVHFlyYrsa2XgG5IlX6buE2N7wAJjKMMJ-9QqRhxD3L_TlDQVaaKHMtYPZtfFZureAvKByObPn9Xigpky0hcKZNrw_3mUV9GpvXF2ZbCqt5s37X626rTfzX3oRcGYj4uy6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی جدیدا تو اینستاگرام ترند شده که مردم  میان میگن قیمت خریدشون چقدر بالا رفته و آخرش میگن: «من اصلاً ناراضی نیستم، چون اگه ناراضی باشم میشم عامل موساد؛ پس من خوشحالم!» بعد هم شروع میکنن به خندیدن یا رقصیدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82822" target="_blank">📅 15:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82821">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBDCUIBhuvi9YlPATw6a4Krb7yRtIoydbdHLf6Iw7V-F5mq2fAFP4IOiSW-oVw5BCXniIeIGc9rBTyaQDQ27J3WHY3cNfYVtzo7scJG2GlyTtqhRAmtdW02WY9tbdlvGvjS4PQsMt72yzQxLRnCEI_IZ1iWI-AeC8Lwvn7PzlGerHVMxrwKWeh3F-tAjCm3nt0xJqjn7kEXoZHMVYPYGtE310WFygdthnKtcd_RaMGvWEIizSc9vk73mhAaq_uk6a_Nfm4WVXJVMK-pyPXWpj_qZSHIbD2LcS21vBRS4p-b2TuoKhTp8ylZySVM7GLIhcxvg68PRUUuO_Xa3Sjfchw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون لحظه واکنش پی اس جی که تصمیم گرفته امسال بخاطر تنوع سقوط کنه:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82821" target="_blank">📅 14:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82820">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVutIaeoB98qFT_fu3027kXig8AIOrfrpty9HsfIqzOdKUnscEtdlLRIgeg5mSL94kMbRQKGJOl_DTq-V8KQR9zQB9gxhcZ4VES31AvHwE7iGFZgjZXc-ZZXF1VGY3WqFxqydizp0dNesEA1yXMw-ilPTFcRcgDVuuSogPUyFY2sr3BIk4EHq40xSP5WKO2dQcQ1yz_yw3gJK2RPsPXuPYJ17PMA6QQAwNPg1PxcUVXiHEuf4nQTLTozwEmLneaabzf3tyuFhNYjKI_A9iQ54WRCRrjmpgjSCihlo9bNOBEEYhnlNszjxZp_br_jS5_Iz4fNI9Usk1e7h7l6ZlWimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی دوس دارم بدونم مالک این برند کیه و به کجا وصله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82820" target="_blank">📅 14:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82819">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">روبیو و ونس و امثالش کیر بسنت هم نمیشن حاجی، یماه نشده ترامپ ایرانو سپرده بهش فلجمون کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82819" target="_blank">📅 14:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82817">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbkBa3MdZbm2J0gXi07XU_sRNVlNaBs2BeTTeZMPGUPVlL75JV6cqQuE_gB6gCBZRAMJ5pHfg1UO0HHVE-Qs7vWoWMMtFSb17xARQhd0dFPiqoouDzbMG3B2UvEWp0QzmRfK0ygTr9U_Rm2S58sm5dB5GY1ZClVdDnYEJeU3klGJVsjImYLF0lQL_QAvCwvSEg750W-PAH1O74DdnarglwO-jRdWEYQYHSlfW_5iMnAbv5-cih57OHVsut6_ubdHbcPa2cjgEd1YRpE5VfxS5JVoo7b2JoIvNMWJnzzb16Kl36o2_KsRbPJifyc1SyUNgb7X3ObH04-swXxUKUGduA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnEDy1cx9Tf8r6B1w0NpIBDQVQvOJ4XDWTeyUaAsM2N40-gJ-PGegB45MRL6ip_D9wyyNodY4O3F9816Z7eeKoxU8bAytXuScfC4yNGsEZroGpdvcs57pmoQehAERr3g9ChjuPaUzA2Uuhw1D8CEql_cemvUpINlCtDIXjOly0MkElxskDwd7Az8fsMWGKGpvo8Vi8qbr5xHgOuF29Hoi_pbgopPOUfx1L0CU-JKYErgBLVURi3Wy6yZSMwOIVwPTpUvWQNF5sYEo8HDtpEtK7RSXZ2jadNwD7LV9laiVUPQHj_QF835BjZcewA0hLxxVbxQlXuxP3LKXGVblh0YMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کسایی که بیشترین فالور اینستاگرام رو دارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82817" target="_blank">📅 13:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82816">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این گربه هایی که صب تا شب تو گپای رندوم میو میو میکنن بیان براشون گپ اختصاصی زدیم فقط اینجا میو کنن
https://t.me/+CAwWLYMxGAU5ODU0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82816" target="_blank">📅 12:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82815">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHPG5fEQzTPtl_5ta8tv8hVCDXcXhwbcsmdXzhSint6nVMtIVp6gtLcl0DEEjAPBv3wzKOPGS4Yl53TqWhLEk7BG4AjbGhkzx54bFvnEcJiNShA-AgWxcTa9LBWT9ZI0RNfmp0VNPPxbyPwmvGMeAfxIzCC7kbhd84kpPnLA2guLu948MMwqIrb76IWFZqXxkW9ztryKG18lEhX4edvWsX5BTO_eUwewhfvujGZqRh7T1RPsIGayaRQvQHyzYOT8wQTTM55VTBweFzQpNbiRPs89BUhvppGoCg-zNbdFQLYFKeqBDCMkOmdNUp3zbxnixN7x-U28HOuQqYs4ptYNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من به شما چجوری بگم این سلطان قیمتش با اف ۲۲ رپتور یکیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82815" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82814">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستان عزیز جود خیلی هنر کنه میتونه با فرمین مقایسه بشه، انقد با پدری مقایسه اش نکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82814" target="_blank">📅 12:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82813">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlL2_6fGYZqq8oZPvZD1PXRfQJt77Muwyzt9S9BXb713mcmVYJbftlQ31bFMkcEZAS8NEfWkPYjN2gNLJpSXKyuC0fg1_3BnC6UU8pypBZQOcilv5tyWJCx1vnso44WlP5foqHwDFpLwY5RxkV5z4VQQyegalflMfWem66ywch1hHVmVS0DKhQWVeKvauGO4h9FbNHVqdNodk9DN5ipih41tsr9ssqDqB-1Dyr6hBXzKmkq189Z4HHRbk4FEx8ALpIPDcJkQttAHpmb3OXEiYZPsrFe69tgYDwKt5Z8768kIJau1mPq7STZlTg9nK10KnEwPxt1YDdB_wR51f1LsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میترسم از خونه برم بیرون بیگ شگی بیاد بگیرتم ببره باهام فیت ببنده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82813" target="_blank">📅 12:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82812">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StcS9bd_3rbEj1RFwmyh1Pa_zTk9C1rx5x3jMeTNMc0OlV-_v4on3C_-JuU1Hr2pxa-thYSS0uMubxBPFVOD4tA9K5-C3M3NHv_JLsvnyrYNFy-85RtmHKwGL_xys9FhpJJHsaaR3C3L3_Z72Vq2pBwbI92G2kff6r3YHaFHW381GHwJpP5E49GbwY_rPS_RXh_tnZ3AX0pM9p3eWdhRA3Lnj6vYQ53hPUd1r2LUlz7zNc28rImfyWMJy9d_LvR76FIbCSUkUsf0JCpi0n9V5u_KKaLr517RAaCaCThDpWnDi6s8jKCQvaUo-MOZTd0C2EfHfqnbXa_2ywVCwC0hPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی این بنده خدا رو از دهه نود بکشه بیرون به زمان حال برگردونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82812" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82811">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8ZW9OEfIkVohJ4vPb3ERsFgHfwNjNL92d2qMxmqETzSgR_t7S2oHLVIn22qSkv-NAfrG6gugUnq1kOtetkQDZlYr3VyZTzIu2SNjb4o0SpEhupzpd_vGa72gdz8OpTs7rlyNmHt_N82WrGtK9KxqRjUVNOpAWNgSnBWyYw0XtBmLI4HpxAXWs-o_9fsuoaYPbBOe_Zo3LQTzesy1PnMn6CEWnZx6v3AuETEUcsZgdQ6hB35KKlRMv7Pzc-NC_Pibl2gBX6Pnk1oZosyq-5_x759RR4tEVwx3V9uiH3Aw_qi-AVmI8-AknUX7edGzi12qThM0l2j5BPzfM9QUULY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استون ویلا
🏴
-
🏴
آرسنال
🏆
لیگ برتر انگلیس
🏴
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه ویلا پارک
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۶ برد سهم آرسنال و ۳ برد سهم استون ویلا بوده و ۱ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82811" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWln6Q-wwFvrullL9nRYrKdcdBDwt0UJG5J9CwYLkeCrwZwR3zgVimsRuqKkUoCVnNCklslBz9iavtEln5Bp5yAy5NQI31wt30Bg3hanfkGJWMIFZ_-gyCdVg0Vk7urS-leN1vMV3PrWQb4_a8UC96T3tJcXJEK8Iw74mHzyKnAV6HE6xpEKKddN-cId90OKAFRn9CuSiuPIyMkn5CPfZT3D4TUgBRzWde6Hez0eXAysTb01QqjOIjfRvHtbuL8pZsb8jyEop0QWsFhHc8qdgYgtC3sUOZCTtsraoIoI106oRwjmPbqwI1uvFORIouIYJ8uCcRL5yY04BFEgYSXNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید خانوم منظوری دارید؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82810" target="_blank">📅 11:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82809">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eub1tsWjYyja4aqUzlTHdUOlivNFTPJdDNV7eZ2NZDnlrpwggd0u51VbR1352MgyHvnwAbA6xqgR4UWslqPaiXDuApdObWEGwW8NPegs8cYaSCbGkNMj0fe6Ku5PJ7FoOFNBHg2P-736VSTjmm7J8DtEm5svrYK5-_ITs7-lr_IwyHrQD9OWsr_kIcuHBtSOhXD4pj0rPXXp3MLSUDEV9DgoQQwdTf1X--hVBNzWaDRVuDh7ROSu7Bk9CRcN4sS82nAPTjwIwNqGZ9GdWLJCflMCv04aUXXEqIhhj-td2bVPTdnX6gZ9QMf80K8qFeYHYVzM10uUJZdGTak0vY5XuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیلی که باعث میشه بتونم این مدل مو رو از استاد بپذیرم اینه که پسرش اوتیسم داشته باشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82809" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82808">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">میگن تهران زلزله اومده، ما که حس نکردیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82808" target="_blank">📅 07:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82807">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دلار ۲۱۱
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82807" target="_blank">📅 01:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82806" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82804">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82804" target="_blank">📅 00:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82803">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ توئیت میزنه میگه قرار بود با اسرائیل یه حمله بی سابقه کنیم ولی دقیقه ۹۰ جلوی حمله رو گرفتم و ترجیح دادم مذاکره کنیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82803" target="_blank">📅 00:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82802">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مجددا صدای تحویل ذرت و جو آمریکایی در لارک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82802" target="_blank">📅 00:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#فوری
سازمان ملل:
این آخرین هشدار ما به تمامی کشورهای درگیر است. اگر دوباره دست به اقدام خصمانه علیه همدیگر بزنید به صورت شدید ترین حالت ممکن نگران خواهیم شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82801" target="_blank">📅 00:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اونایی که میدونن امشبم جنگ نمیشه ولی الکی وانمود میکنن جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82800" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تسنیم: حمله آمریکا به لارک ۲ کشته و ۲ زخمی داشته
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82799" target="_blank">📅 23:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پرتابگرهای موشک کروز ضدکشتی سپاه پاسداران انقلاب اسلامی در لارک هدف قرار گرفتند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82798" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آمریکا پایگاه سپاه جزیره لارکو زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82797" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کوروش یه چنل دیلی زده همه رپرا رو توش جمع کرده
بعد یهو یادش اومده عه آرش سرطانو نیاوردم، رفته پیویش لینک بده دیده عه لست سینش لانگ تایم اگو عه باز یادش اومده اصلا زندانه طرف، پیش خودش گفته خب چیکار کنم حالا؟
بعد پاشده زنگ زده به زندان و صداشو ریکورد کرده گذاشته چنل.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82796" target="_blank">📅 22:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">می‌خواستیم به ماشین ۲۰۶ برسیم
آخرش به دلار ۲۰۶ تومنی رسیدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82794" target="_blank">📅 21:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkW7U-bfhCaMMiYtX30HzmDXk_rY72lLyG3rRRDZRDubb4V92Cj2-68J5XIOGJInOU4EZ8GWkfrVSJp9dcKOFe8xnI6H4T9Ldm-TcWXXG9K6VqedjpjYB3Q_r0ZeoWlGRxwGcNCm4RUMtHArjCRmEc9zvcjsk7xdSxDS-1yWpKr_lbxmOwkZW3FcOMVEYh8lltRAVQy2woRByJooa_HGSdn54xMa_AEmGMCulLbp-rgBXy26gIswddASgL6WMcDTpyO5SxJFbT4P7iTUTn1s9vH6miywHeKb7UkzTbmEE94NBik1eP7eidy3nATxfBkUb1RcC35GyFVJz94uwIKSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه تاریخی چرا نمیرسه به قسمت تجاوزا محسن نامجو، بابا خیلی عقبیم بدو.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82793" target="_blank">📅 21:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82792">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gharibam Bahat</div>
  <div class="tg-doc-extra">Danial Moghaddam</div>
</div>
<a href="https://t.me/funhiphop/82792" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82792" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82791">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrwPZ5mIRNPbObs1KPddqKS4ygyNc_qbz8ZNZa7-FOftGAe-G9gkepNATreh4w3SapyuWWLC1XS_P8F4jk7ZKb2nYuufhpEpuxPHR6bHOizz3uheIsE87nIE79rm9MEJHA4LouRuF7X_aKrrdQKKQxwph_Kb_ralhJS9QHe6Q24pLBs8WxWSlRLWt_kAwByG4uz8DS1tlZhkuBgS7P5P6026wB9Q1Sa7KLSnxC0dGtr4PUb0043nZBw5MmqAXRw_xKJPhpQszWi8Th9PZjx_GaEiXegsIvdgmWXXvCdxd6MmBbzknlqxZPfGxzzfIC_RnvQ8_6oWoo5pfWYaKYgkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید دانیال مقدم به نام غریبم باهات
از آلبوم خط مقدم منتشر شد
https://t.me/danialmoghadam3</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82791" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الان می‌تونم به جفری اپستین برا خودکشیش حق بدم.   @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82790" target="_blank">📅 20:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d776d17fe4.mp4?token=ikZQrqZblM37svNzcumSBdD45EbELDy4pZPGxDdMaQEHtqzEpdfYa95m0zC0-Y2Q8khkaenJp3zMuFLDz03D4z976ee4R1cmaTxuoxvZbZLZvYDTmm7_C396mrclb-tkRDklgZhIUVjT89_6x7di_gSMqCrKiUXbmbl8EXihS4rd_oJNCDjbpZOVFQuRf97KN1Lz8pOFKhPK4GOS9TzL0HgQIjxrwpma03wkigBlQh0eLFclyewUtrQpZYEcWC9LX5DXys0une5h8UhQtwMkAlYkv88b6J7uCx98Jyu6t54UDJfVHbIoXSDSXbQN6zK1kXmnMkqKPvcCrjGfHbdjQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d776d17fe4.mp4?token=ikZQrqZblM37svNzcumSBdD45EbELDy4pZPGxDdMaQEHtqzEpdfYa95m0zC0-Y2Q8khkaenJp3zMuFLDz03D4z976ee4R1cmaTxuoxvZbZLZvYDTmm7_C396mrclb-tkRDklgZhIUVjT89_6x7di_gSMqCrKiUXbmbl8EXihS4rd_oJNCDjbpZOVFQuRf97KN1Lz8pOFKhPK4GOS9TzL0HgQIjxrwpma03wkigBlQh0eLFclyewUtrQpZYEcWC9LX5DXys0une5h8UhQtwMkAlYkv88b6J7uCx98Jyu6t54UDJfVHbIoXSDSXbQN6zK1kXmnMkqKPvcCrjGfHbdjQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان می‌تونم به جفری اپستین برا خودکشیش حق بدم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82789" target="_blank">📅 20:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82788">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9b9dca48.mp4?token=dAJu1Ha8DDazgjMfYSK9dKincRDJFF2CsV99IchGoZPECZOV1vhKva8W1NVT4o81l6lKxIjvb1kGFWXxdIP0oj2oYMea6Ns_mOZ795ASugx7v66apJhpymHs1EGrNjcnDBE8aPocijXJi5mU09uid9O-062HBrjywnGEiJ2RhOHQ6R6qR7F3A40jlEQ9cBYzS7v8NBf9MW-adUo7HrFl4jA7kEnkcDlOj7HN3u2ouwJD18i1eNfNiKd2bfVcmWqkpWu3avDX23MUfOU0VyDr4DJSycK4wS7GOZZyixQSo4vRcBZ1uqw-0d-cUK6ZhjFQq50ruFOs2N3gkAmmm2-orA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9b9dca48.mp4?token=dAJu1Ha8DDazgjMfYSK9dKincRDJFF2CsV99IchGoZPECZOV1vhKva8W1NVT4o81l6lKxIjvb1kGFWXxdIP0oj2oYMea6Ns_mOZ795ASugx7v66apJhpymHs1EGrNjcnDBE8aPocijXJi5mU09uid9O-062HBrjywnGEiJ2RhOHQ6R6qR7F3A40jlEQ9cBYzS7v8NBf9MW-adUo7HrFl4jA7kEnkcDlOj7HN3u2ouwJD18i1eNfNiKd2bfVcmWqkpWu3avDX23MUfOU0VyDr4DJSycK4wS7GOZZyixQSo4vRcBZ1uqw-0d-cUK6ZhjFQq50ruFOs2N3gkAmmm2-orA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور ارشد و جنایتکار و نادان آمریکایی، تد کروز:
من بارها از ترامپ و دولت او خواسته ام که به معترضان سلاح بدهند، تا مردم ایران بتوانند با کمک سلاح، کردها را مسلح کنند و اجازه دهند معترضان این رژیم را از قدرت برکنار کنند.
هدف این نیست که سربازان آمریکایی وارد عمل شوند، بلکه هدف این است که مردم ایران این کار را انجام دهند.
تصمیم‌گیری درباره اینکه چه کسی در دولت ایران باشد، از وظایف ما نیست، اما وظیفه ما این است که بگوییم دولت ایران نباید توسط یک حاکم مذهبی افراطی اداره شود که از آمریکا متنفر است و تلاش می‌کند آمریکایی‌ها را به قتل برساند.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82788" target="_blank">📅 20:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82787">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqWGScJkH9PdMLp0HBqpgYcCQvOcS-ZpLXu1fRgX-xxhc8dTuytRLABXIH8BOfZK7dSq5pkLuQah1LWjhSTUnt9gdrTuTGb2W8BgLYNvopqOedugleBKQUd-XjbqcUYSY71lWQXU4tfh0_ei7iMRY58K-48jz4WjE6W-HqmHEA5JnGMwQzmfXtgc9nOBf_0QD5MQc4OAg_aRcHMPE4QqKBx5PIZQYGVghmY218jMtEH-AAWNhOMQBwNR1o28KD380LwTnmCJoS2AK0hyFn9iXPSIKJLpNCenAXNDxqdXuIaizo1jzGkvKn2FC3DEu4i5JMSgrEMqx77TGJI8_3-79A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82787" target="_blank">📅 20:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82786">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvB_knmrp3qX-EGD7qAvuvjutFFKPTC7o3TGQnGbG66CTILgaAtCigF3kQPiGAeW9lzDaylEVyNlU5EDmo1-ZQPNhngACuBVUPosrq5_J6cjHX1I22Hw9AB3Ku3CUxuefw7dm1oPvnjb0EgNwcXwVzsXidNbdRxmG_n1jRZP1BIUlUXTmmwpBUHOJVxRiigApVXuGq5_MabvuZqySx5JMu4Iuxl1RBPYLYexJu6gJG9fLpynVyNVqS76-hq-2npC7H7ZVPBiI1CZM-a_5X0u7Dv3lh6PVkYx_-IMh1C8txEaY2arLPk77Lr1ioDHAiCzbVvQAR1dqnp8fmgBA63mog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زن‌نامجو: به بهانه بقالی رفت بیرون ۶ روز گم شد بعد دیدم با چمدون من ایرانه  مشتی حداقل الکی میگفتی میخوام برم مسافرت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82786" target="_blank">📅 20:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82784">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7bTlcK64VlIcTZXsU165Ls9SsIDY60Vyf1o_awNaGwB31GKdIqT1nln2rrXhQs3MZAOiJ3cOkRtzdmx_xLeOvPxDTcvF7bmSPTXYnbmWQPoH58WhjR0Vg2jZWVUD9EHPgLltbpT0PDd04zuORNfmCOD_CZtoenBBVJizw4x-GByiY9_1KR-SeXpr69Me0PhJvT-GM6J7JGWO7tXivkfAUe6AEoxczXOZnMe0T5vJrMPOCL_5FqJ2jOZSJkO9WRZWImccLy9bYzeaH_xvk3nqBtzjuw8wyDHCe90Y-knie5nW0OJt0QkI88MGTFK8CqO7AE7pONeKBOAnki5V0CZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmeZ8TlyVYHZlsg2d4Iomcm2_sX7059Caojcb7qbndoA-MNT-fJ0MVkf4XPW4H2XjzEQO4HbSxKjIbvS4OUt9N6emvppJHnXLBMXT_AgJgHy_JuKL9fXesPBHP3liCg2rOsVFeRaFpT4oJCf8A95n8tsohS_3FAiOHfTjZ7eeaJGzQAO8L0TbK72FDvJjlevxwUGwxF2XOpUr1CNW2SSt1eN-BZnFFBzPXDS_v9ljK1LHoxoqrNYE7W5MzU007uHFe7PCPhgSnjTy7P16N9AEeI0Nqqp0d7ZrbHnwfkSzGAUjIGfoQNfRAuDlWjm14CfCQT5j65IpDQygOu6QjggUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتظارشون اینه مردم فتوسنتز بکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82784" target="_blank">📅 19:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82783">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcoHhEbyVspfvhym7EC0itHSsXOwI9CV8DMLpJwvYeYD1jEbpUYzZXpKnst-1jlkEngtSdh6oUHiwqBfc5hveKoQ5U7KsVV-qSSfiBFMbXCZIwEF_KR441IhurZBckdu-M6Or1_W_ZgpC5LRgB-M8cgirPtHf5UBiupki5xWwsDnHVgGHY4jNTMk2DUVx6sSrQ5t5i_YgfJyyRjQqj_U0o8VndCb9Edy8u2IuRYthuYFO_FHcpc6aDFiMYZOR6AcYLGShDiQjEDvPcTW48dzd32N9qYbQLkutJ_s1xvgguj8RAjrlK7fLSbtjuObvDjK_IjUGTqiDz4ttpyHwu4j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرگوسن فک کنم تهش تو همون الترافورد بیفته بمیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82783" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82781">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vd8ur9eJGNyV7JQj6CqI0V_quHODWIU8j_-RiDfsbPaP3TyLCxSBa7B0WIToZBeQGO7XISjEIfnU9vzIyk0Y4MqiiBKawBD2sZNWFnut2ExtAhW0h_m1zX4t5ohP66_17PA2X_beBdNPuuSPLf7UaQtKNX33NFCjkZ7J6T8nncu1gAD86phkqlvtuokpX4S5jWg6kyw7Hk8w405kCKGm6NX7yp8KQPIvZziu_hCbKksmoVLbd77EM5pdrGCKGBJnQIVSAZRvBhPjbsm3x6Um4b0BByqleQv-q176iPVUi8YXG1r2Wdel62hzcpx-ZTCz6gpOMUo5UliZhF7oyv3R8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBuXmbBsusW_Y47uLHjd9jEag_KkjeqfiYPmdQJuEV4YiBS4gsrdd2Lh2TEws1iUWr_lhHOX_RAcU_1QztAS2hIyRAa9mTD6AjmKgPJYVSc9DJMGs3cLGjo1tS8BWXpIZhHp3U-TJNgRa5n3rfyEbeD7DC5MQxuCFAI0xfQCMge169FwDid8o02skffOowIR1zNUkABmYa35ccIoMasPukmUMOXqcThbNzzVqtrMUeCMSkvzqaV2mv9jyeT4QuUweFAgKv_iAIu9iH0B_MC0nKt8W0VLwsJub1bXbWIewzV9oMy__pa7__QuyBQj_ow1l3Rp03D98fT9tZsOiWEJdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حاجی انگار نه انگار که یه مملکتو بگا داده و الانم تو یکی از امنیتی ترین زندانای آمریکاس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82781" target="_blank">📅 19:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82778">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کی میخواد این فصل جلوی رئالو بگیره</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82778" target="_blank">📅 19:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82775">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انقدر گفتن تحریما تاثیر نداره
اولین تاثیرو روی رپرا گذاشت، همشون دارن بلاگر میشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82775" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82774">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5T6ly2E-BpTQJjhE7gAC0KJKsW3DRlgBit3jpmJL2ktmeOObnbhjcyrvQXnf5X9eZq5EELZgGDsYeSgFWgGB0hDM95ZiOxUGninysX9WMgJrxdoBny0Hk2PvENeXQii3iznw3ZMUtbiKAgO-MJ_jbQyaQLfahJGUKheGyRheFpN3KhQ0RVESRqOQoAOxSMSNXfmMFX7TGXYslKDKTqst21gNchMV56GrufIx0TQvZjgkny2o4g4JK1PuUMS75w5oUN3y8gEj0F7Rs7_96TT6ZOSGxilxX3mQsxto-Phh4m0dYrHuy7HNecnkgp6GUN2lZHGBMgL95rC8fRhEttAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژابی بال و این حرفا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82774" target="_blank">📅 18:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82773">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tjs941IOhimWXigl9I-JBngfp5Wf1p9BYoswkJOfpctgVofzFGipPIX7NnJUV69SFGvtdBPomkxCwx7s2DxfPSTBjnTAdZSE80n-UZDfuGiu_-nqmpqWb0Nr938Lb9JFbwGJeJo0tJm-TWAvGo4O5Qz9kKkGoqB53O78Not-JJhj1rEJXRIuOjMvMYXRRcnI_QVTwilX-t7_t6UW1m5-s4USRR9nztyzsfwsH-SIY65i1H-Nz7mkSu4yQ6lF8Ap17_tTzdG-Iz00xGxOzirpngp2WV7uOsE0mb8oOwiuG2-H84m0-D7KqlY3J1ePktcJ6sH_tbVt1ZqGcGRr68HkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال داره انجام آزمون تافل برای ایرانی ها متوقف بشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82773" target="_blank">📅 18:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82771">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بیگ شگی بود خودش ویدیو میگرفت میگفت بیا پستش میکرد، کپشن میزد پول رپ پارت ۷۲۷۱۸
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82771" target="_blank">📅 17:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82770">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82770" target="_blank">📅 17:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82769">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حاجی چرا خودش ۵۰ دوستاش ۱۵</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82769" target="_blank">📅 17:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82768">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAri</strong></div>
<div class="tg-text">منو ب چشم بیزینسی های کنار خیابون میبینی؟
۵۰ بزن بیام</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82768" target="_blank">📅 17:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82767">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82767" target="_blank">📅 17:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82766">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d882fddf5.mp4?token=SuCXH66QLrgzGMs4p4J7oOJ2xG9jQsmN2wIbf64lEDnZ6UarA2edLFWh9KHMoEgTyP3n6mDHtdliUrnMopq8IzJvatGjcG4uhyrCUD4zHMvvE-5b9BZ38cqngZjwECGFYhhN7lVoeHWSfiO2woPca4V9zKfKInZsfOjTwnXBPwHn_mvZxMWal4RdHwprbf0xEmnF6AW3_UROJZdk_B6EIMcIky0r0dg3iRColM0vVq2veZiyXKnP6gBH7TJoXDRi8WGsrg4sQcq0OGVObPrjZO3Zji32qSlTXnXBE3_dtbCQMApAx1WmHCGI7zwNolrfCFpmHcQQhE8RtLuPom61Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d882fddf5.mp4?token=SuCXH66QLrgzGMs4p4J7oOJ2xG9jQsmN2wIbf64lEDnZ6UarA2edLFWh9KHMoEgTyP3n6mDHtdliUrnMopq8IzJvatGjcG4uhyrCUD4zHMvvE-5b9BZ38cqngZjwECGFYhhN7lVoeHWSfiO2woPca4V9zKfKInZsfOjTwnXBPwHn_mvZxMWal4RdHwprbf0xEmnF6AW3_UROJZdk_B6EIMcIky0r0dg3iRColM0vVq2veZiyXKnP6gBH7TJoXDRi8WGsrg4sQcq0OGVObPrjZO3Zji32qSlTXnXBE3_dtbCQMApAx1WmHCGI7zwNolrfCFpmHcQQhE8RtLuPom61Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82766" target="_blank">📅 17:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82764">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408e06015a.mp4?token=uW4_NbpULSHOkPV_ou9Jltg_rrGvwFCJ3sTYssbNlGBBRIgcl1E6b4NcWDQyVOBpgokgLrau3qRW4fKv4cDCQsxFl4GMr8iFC1WCGXIhsPWGFeJsgRJfT-m_cQ41nsuiVQOF-2iz8xHJ5uuS-dvtUklIMlN77f3UG6t2TG6tPAcm_vZ7oGJokhfvNEgm7Mq-HyUHTrg2MUDTAWFKz3jPdqAuKFglPa3AXwpuNiorYYkqV2Nx4yrQR4MtFzH814B4zYTjzIxEiR182Lea3d1Zhd64odWRJAsEmSxzWUeXUNzI6t5lbHLLLK0Rn69SBnn6A9dDbra9RQEWRAwdYHbEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408e06015a.mp4?token=uW4_NbpULSHOkPV_ou9Jltg_rrGvwFCJ3sTYssbNlGBBRIgcl1E6b4NcWDQyVOBpgokgLrau3qRW4fKv4cDCQsxFl4GMr8iFC1WCGXIhsPWGFeJsgRJfT-m_cQ41nsuiVQOF-2iz8xHJ5uuS-dvtUklIMlN77f3UG6t2TG6tPAcm_vZ7oGJokhfvNEgm7Mq-HyUHTrg2MUDTAWFKz3jPdqAuKFglPa3AXwpuNiorYYkqV2Nx4yrQR4MtFzH814B4zYTjzIxEiR182Lea3d1Zhd64odWRJAsEmSxzWUeXUNzI6t5lbHLLLK0Rn69SBnn6A9dDbra9RQEWRAwdYHbEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا محمود زد به ناموست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82764" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82763">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ژسوس زیر دست فیلیک شاهکار میشه
بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82763" target="_blank">📅 16:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82762">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بارسا نگو بگو سطل اشغالی سیتی</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82762" target="_blank">📅 16:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82761">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الوارز میخواستی بارسایی؟  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82761" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82760">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DziPIJ-tNn7Y71EuixLzI90eRdvD7uljG6kW40XKOp9YslNFlz7m4BY7SsgBqNVPitLWDLj2YSJgfnwpQyu8nStYiUhXMBXySaWG3vIedV8OiFXEw5f6pnnEN42Xoz6me-Fqes0YoV1bFxRn3R85PaY0rfK_gbZLokds6MWhxssuy8QDnKEk4qPVI7xxCSkfuEFnV7pLsP0z7vdDemL7beUQkFyxSZ9RD1iIgoZN0_aMMwt_je6o17pkrTJ8zbbhS57v8mkmriupWTazz0kqjHITsDO66r1-0pWcOfthz0w1J8fQEM_nLeEwCdWENqK32jRH3rGsFToVrbunKcgIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الوارز میخواستی بارسایی؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82760" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82759">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUFfZr9RBiHjTB9Zz1sI2Eo8auR2cKIo3Fc8kwl6-4Gc77EyDL_naiz5mQGW-Ia1SEUIpH1i_2-h_VYlVRkO31zFh-mc14FXKiZ-N4v4oTxPKnHvcnNZ194AojcpThFsjaWrOiRDnUrM3d_6nMfPg5Ia9n_p_0WR7pBHmdVGEGFbX6dOX-aTpuIs6kuEX2pbtGSyGa7Y_tmvjFaNxly8R_mHA3ziFBlMfbUOkednNxei2_enSxkxyhGY7UoLLCmk7Xo5tGSO6NEF5Wc5K7dhWFcnR9vW_S0EGu5Xdc_2dWAQywijunENnP59aGZkZdQuMxspnfTQGpnM1AcYZ_iUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته خنده ای مادرکسه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82759" target="_blank">📅 16:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82758">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d256a2c699.mp4?token=tee10gfycY1I-PKdn2o4fewmcxpAIDPR6sjN7cbh6_2PyH8ZBOk2n0Hd5SwGwcIxo4uYrPKH14ac9ZUumc-oGKkZ_gYrnXjaDFXpfGvIMidoDUbD853s4GoRrGFoKh8r14cFABMHFqfkcqbNZQmLwiPDcIRbf_JuXy9XHZotvhoZzTcvT9UUDaEj_4d539xsNKLeLMUG_Ge_vhQlyE2Jm9nKy9N-y2SMYHBH6WT2Mog7ywM8-z_qd7AqudCw14xvkBmBoSnpDBO7UfgfNn4NE2yWo_NymOK5__aTZgNGHR3mo2go-gQ-gQ5ypI4lyYNrTUp04-4_7qOGcQsKae056A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d256a2c699.mp4?token=tee10gfycY1I-PKdn2o4fewmcxpAIDPR6sjN7cbh6_2PyH8ZBOk2n0Hd5SwGwcIxo4uYrPKH14ac9ZUumc-oGKkZ_gYrnXjaDFXpfGvIMidoDUbD853s4GoRrGFoKh8r14cFABMHFqfkcqbNZQmLwiPDcIRbf_JuXy9XHZotvhoZzTcvT9UUDaEj_4d539xsNKLeLMUG_Ge_vhQlyE2Jm9nKy9N-y2SMYHBH6WT2Mog7ywM8-z_qd7AqudCw14xvkBmBoSnpDBO7UfgfNn4NE2yWo_NymOK5__aTZgNGHR3mo2go-gQ-gQ5ypI4lyYNrTUp04-4_7qOGcQsKae056A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به خلسه گفتن چرا تیک تاک پیج نمیزنی مثل بقیه رپرا، گفته دیگه من سنم رفته بالا به من نمیخوره تو یوتوب دنس اینا برم.
حالا عادی ترین محتوایی که خلسه تو یوتوب میزاره:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82758" target="_blank">📅 15:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82757">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حافظه تاریخی چرا نمیرسه به قسمت تجاوزا محسن نامجو، بابا خیلی عقبیم بدو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82757" target="_blank">📅 14:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82756">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPPoV4WIABwdVdpfV0w58vqBmAUsu0AeMHRbdH0E103Kv7iQyh4pJAWg-BRhwcjYiOM4UDO2DilR-EjSQVUQnLd9VAJdOGZcahK9lFnvc7aW64YNubIL0Cv8Taj1Ga3iuslDG0XFOpNu_R0HbJC7dkwPwdbfkiW4VM0vQoIsWOYydHKfc-7qloRC34CAEvmdqk-G10aXUlMI3dyfyIjB30tcHvqA8Nz9nZ7kxdpXOzk5I4SOViC4LJSNzymoITXYjaXUZCUgCTaykF8_x_SZohl_zS8i12NnazfQ6kWkqAMoha_TUwUX-vDq5bv-XScxD7KKEZ5XR-8HjkXgJQJGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوریا ادرویت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82756" target="_blank">📅 14:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82755">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مدیونید فکر کنید این که مهران مدیری میاد مرد سه هزار چهره رو برا صدا سیما میسازه و توش عراقچی و دولت مردانی که رفتن مذاکره رو مسخره میکنه اتفاقی نیست
کاملا خودجوش مهران مدیری و نویسنده هاش تصمیم گرفتن اینو بنویسن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82755" target="_blank">📅 13:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82754">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حکم اعدام برای ۱۰ معترض در اصفهان
شعبه اول دادگاه انقلاب اصفهان، ۱۰ نفر از ۱۶ معترض بازداشت‌شده در پرونده «میدان شهدای اصفهان» رو در مرحله بدوی به اعدام محکوم کرد.
بر اساس این گزارش، ترانه رحیمی، نوید الیاسی، ابوالفضل دادگستر، مهدی منصوری، احمدرضا سعیدی، مهرداد بوئری، محمدمهدی اسدی، آرمین غلامی، پارسا جعفری و مهدی جعفری معروف به مهدی خسروی، به اعدام محکوم شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82754" target="_blank">📅 13:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82751">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1de67eb81a.mp4?token=rv6eaY6kc6GSYlzYxsceZp38rdhfUQgTO1HjR74D__gwK4Ouz6-AU_iODc_p_K34nLXmyvg_iH_yBLfym1iHWz4ugBjogdgN22C3pEUMy2PYs7GmmJNuR14-Rmes0MLs359qrc5EQTY-DvNO3mL9OaFWs4YvcgM6RH53-dlRW-LLvLKGTUILsBt9Q-klZ1GWNkFZ5Cwv39Swl4CXVHR2pw1QUOs2lxJrxj2cGiVgwWUByBr_uU5NWmU4uBfHa9sJ8xNMeeXRS6TxhhhMRI1a1fGfSFMwUI5orbttnYxBvf4ZN19ixSb61dRNFQaTSFZEs0857045QQeJgd7rWNUN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1de67eb81a.mp4?token=rv6eaY6kc6GSYlzYxsceZp38rdhfUQgTO1HjR74D__gwK4Ouz6-AU_iODc_p_K34nLXmyvg_iH_yBLfym1iHWz4ugBjogdgN22C3pEUMy2PYs7GmmJNuR14-Rmes0MLs359qrc5EQTY-DvNO3mL9OaFWs4YvcgM6RH53-dlRW-LLvLKGTUILsBt9Q-klZ1GWNkFZ5Cwv39Swl4CXVHR2pw1QUOs2lxJrxj2cGiVgwWUByBr_uU5NWmU4uBfHa9sJ8xNMeeXRS6TxhhhMRI1a1fGfSFMwUI5orbttnYxBvf4ZN19ixSb61dRNFQaTSFZEs0857045QQeJgd7rWNUN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سجاد شاهی تو پشت صحنه موزیک ویدیو ترک "تا ناموس"
حتی اینجا هم داره کتک میخوره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82751" target="_blank">📅 12:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82750">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMDPZWzpGfiSENEKSk6MS8dSRr7n93TmGXH6pLkNI9hpJCWKkBI5ea2fjAma-nd9KEL1HTMYHJOTrfAJSfU6m-H8Dx5W1N9w6hKPZW-PuRVPAb_exSgLdRZphZUGbB1Ljpz3Ri1nvihrzwXg2mE6iSbmn9jtM-unmXEJndLpV9YEsbSo66yehhvFHW-b-3M2p9e19aQeg5YQ0vU06rcfsPnfe-Gx-MBbjN1dBZ2oSJHF0fTeEl4-egMsoa256QM4oExRstLYvGvCSo_3Qau3wbNK_bixtRHvZORuAAUFURAuxi_eHm5yFIgBBwyKwmxQyNCFuS57zUGIy2HNCoT0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس پوری و مامانش
حالا سوال اصلی که دارم اینه چرا شلوار پوری جیبای عقبش جلوشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82750" target="_blank">📅 11:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82749">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زن‌نامجو: به بهانه بقالی رفت بیرون ۶ روز گم شد بعد دیدم با چمدون من ایرانه
مشتی حداقل الکی میگفتی میخوام برم مسافرت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82749" target="_blank">📅 11:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82748">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a6fa8663.mp4?token=YBgd4qQJdS-jxraMCG4B3FSLQSpLEVzq49hEDZF2GWIBBP7BCstT5NKDYcBOMMmpsk9Jmnp4s8r9HFeV6tvMG9LfNWTfEAuDWgPNDqvrA4cgQOB135yRs3yte7fCIZqS24HkMOvt1bEJ5FMjBPlugJB3_WFv7NcR5vi9o3NKiQvkx8dJPZVDQkiQCxY4A1AA_ABYZT6j8TmLgqNzAaeNxgCiupm1FVEWbfVS8o47E13dPOoNfLRrDV_mfQiJA8w-qT8uywDJ2uGpfMMFqzS2XgLxuQe9XRKUBQ5Jl5jcLkpEm45bZLpekPVKwBhtiV8M1pVMSX7eDleWrPeTH35bqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a6fa8663.mp4?token=YBgd4qQJdS-jxraMCG4B3FSLQSpLEVzq49hEDZF2GWIBBP7BCstT5NKDYcBOMMmpsk9Jmnp4s8r9HFeV6tvMG9LfNWTfEAuDWgPNDqvrA4cgQOB135yRs3yte7fCIZqS24HkMOvt1bEJ5FMjBPlugJB3_WFv7NcR5vi9o3NKiQvkx8dJPZVDQkiQCxY4A1AA_ABYZT6j8TmLgqNzAaeNxgCiupm1FVEWbfVS8o47E13dPOoNfLRrDV_mfQiJA8w-qT8uywDJ2uGpfMMFqzS2XgLxuQe9XRKUBQ5Jl5jcLkpEm45bZLpekPVKwBhtiV8M1pVMSX7eDleWrPeTH35bqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخدا این آدم نباید رئیس جمهور آمریکا باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82748" target="_blank">📅 11:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82747">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0D8yw2Fw4wWUgAhOs7GGdMm2zW1XJPui40PC3dsHZON48jO6HIa5oIo2os_Y2B0sKfg1Ueq955nfUM1KDkQOI8_JfGpGwAjheEmIdOq0EGJCn_DWiyRN5pt_L85aY-tiaaBW-OW_E-oK-zpv7fAMVKtNRsGtHY9riij04DytCxCve7edZh1MfWGOfwXhrnJ67HwOYYJrOKsMiHeHDtqCncGrPASEz7Vag0mfD5ldjMGlxggKKHXFpAekcxrlj1iyrFeBuh6a7-Y32LQUlBZzfihjWCe16rmjr6v2FxEr8TWP5rIqNIgR61OSDZXJP_3MWaMuyJU3CsmP86wnEVU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش این عکس حداقل واسه ۱۵ سال پیشه
از اون موقع هنوز ریشات در نیومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82747" target="_blank">📅 10:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82745">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SETugRborEBE6DN_D47mEHXIfktPuwDNDGOUPEXpMmFRGT-2mYHX_rWsiNXXIRYFwHfQFNXcaQQV6dv43yHntUbNMX2odC_VoOvuyx37WxGeY3b5KWxdDXz67UMLmATktsJpeILDkggh2jszAGJLfPIepm_632n4NwxMZNr5pJKcwUiICS9FlJsbbD3vAnxPkRAZL-BbIJaPio-S9Zvr8EzYW3LgG6l3PKHvb6YFVSPuEbEw50rOa1XJwj4JF6H2YUUdi6h0VH_kksIo5dzHKotX2Vwm0my6425zDFMiE-FC0nOUmjM7JkD2X9oFbIi7qKrzEKlPP_mQP0H71wJgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82745" target="_blank">📅 05:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82744">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جدیدا شات های کصلیسی بیگ شگی هم بیرون نمیاد دیگه، فک کنم دیگه دخترایی که میره دایرکتشون عشق میکنن باهاش پخش نمیکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82744" target="_blank">📅 01:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82743">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGxRfAuVcFVZ7RSea-Hue4yHKmJoyPVj8ZQn79hJxyINH4e0N_9A38990VpZbcoAmKZxv1X8gViHwqthqeJEJWCy2IbqgGpbQnBAnGP6IJtMpd1Ex9uLVBgwS3atgQV2PbtviRBBdsSfY54wrBxrk9FWAMc7-GWPqgWBWIy-Vzj592bpZ9f8rBEvUnYUrvRsKbEqryTCKWljVuG_ES9oJn30ks_CZvcbxQ4nXkXUCsUucmeIITWUlZEnfmxLePgc7Qqv-VLPpSzSwePFmdokJ9WEbmwIP24_MFhH-ZBormicCfVuoUN5zd39GwnS_wrHqRL3cXLka4ImLMgcBJv80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی‌ رو دخترای خوشگل میکنن ما میدیم
یه یوتیوبر(aj king) میاد پیج دختر فیک میزنه با هوش مصنوعی و به نصف یوتیوبرا پیام میده همشون هم روش کراش میزنن و برای اینکه ابروشون نره کل چتا رو نشون نمیده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82743" target="_blank">📅 23:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82742">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c692bdfd.mp4?token=sNOpj3AZsU1NcMnBNnQ3KqQMPNbqv3I-pDHWewMgPZBm5mNsDMmN9C6_uSYFt-eT0zvZ6H4XLPUlhJCm4zkQjiWDawrwbZu8-ae9GKTuYjvBZjtQviZkhF8K00M7ahugpieVG4y68rfWtRbmXhVhGZrHlGuZxP7exmZ1Ws5T7gBL8yt-U_Ho7at2yKR8yMx4fuNfXnYh4FlxXT8y22I9TwXVYY2Z7oOcvGY2xxxIzUYSVuvab04HjJF7-M7K6Rdr8rqXCr5ujDo-jf3KpdohjE3GZ_maazZIZZ62P5XSZ05veDSMZcYPF952b1i0AcgYq5FyViii5_zUw61YtZZ1Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c692bdfd.mp4?token=sNOpj3AZsU1NcMnBNnQ3KqQMPNbqv3I-pDHWewMgPZBm5mNsDMmN9C6_uSYFt-eT0zvZ6H4XLPUlhJCm4zkQjiWDawrwbZu8-ae9GKTuYjvBZjtQviZkhF8K00M7ahugpieVG4y68rfWtRbmXhVhGZrHlGuZxP7exmZ1Ws5T7gBL8yt-U_Ho7at2yKR8yMx4fuNfXnYh4FlxXT8y22I9TwXVYY2Z7oOcvGY2xxxIzUYSVuvab04HjJF7-M7K6Rdr8rqXCr5ujDo-jf3KpdohjE3GZ_maazZIZZ62P5XSZ05veDSMZcYPF952b1i0AcgYq5FyViii5_zUw61YtZZ1Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتاح سجادی رپر با استعداد نسل جدید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82742" target="_blank">📅 23:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82741">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cafd847a6.mp4?token=ZN7l-UxfPai0-0RtwSzKTSPzkVwHYAg8tlE7f6awqcB7Hv2Usn0NmVBRXkwnMzELHEbwY2QH8eRsMlSlQ-Pi2zqKrz7vkOwz6PX_-53Yx6CP7vcn8OzMjM6uWJ1Mcw_5jq96dOMTnBPHZVXPWhKshWQNFpSsmnt4oDHDflEDab9b0mGJz0LBWiaJ5xwMncbUbhHMcSMC66jm_x07yie9NIH1fuySvlB3GGKO3TPRt7yOUDc6TOxRkm_rNijkJfcnLprDeD-AUqszvCISYC2kmG_durM7jW8tCiYd4rnJwOHhk5Z_OA7UETazTNjy-bCSKnIzOvqRzvAHZXEWREgvrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cafd847a6.mp4?token=ZN7l-UxfPai0-0RtwSzKTSPzkVwHYAg8tlE7f6awqcB7Hv2Usn0NmVBRXkwnMzELHEbwY2QH8eRsMlSlQ-Pi2zqKrz7vkOwz6PX_-53Yx6CP7vcn8OzMjM6uWJ1Mcw_5jq96dOMTnBPHZVXPWhKshWQNFpSsmnt4oDHDflEDab9b0mGJz0LBWiaJ5xwMncbUbhHMcSMC66jm_x07yie9NIH1fuySvlB3GGKO3TPRt7yOUDc6TOxRkm_rNijkJfcnLprDeD-AUqszvCISYC2kmG_durM7jW8tCiYd4rnJwOHhk5Z_OA7UETazTNjy-bCSKnIzOvqRzvAHZXEWREgvrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارتون عالی بود پیشنهاد میکنم پیج تیک تاک بزنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82741" target="_blank">📅 23:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82740">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-BZfjh2UfP-SOb5wAIz8kmmubWnc-KxJ8Dheot6AgU8IvT8Mvor2WTmCpo5A4iUNNR8btrP9Z2r8-dKf1_f6utavtPUdRxjxGz8tX0g0wzHAKG_6cEScE-k_5D5NUto8YIYyInbDkFkYAUaqiTtZHJPNozqsSVt52nnGcvsKWsIJuSZ1_TgI7kq6xV6s2yqz-fhXzHr_zPpZb2Np6gb71JvhUTkS0PkadU69_Z47f19DEcuoFoyLGp6z7MmEmbZUFYrHq2WsKSMteoWsliQBYLA3J5bca7GvvQwSblP_7836k5bpfIwbPCvCgaoyWIVaaltXWulGG7jPZTdw-Blpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82740" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82738">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732d114172.mp4?token=NPeNYvvn0hVyFuh2iatRBsFy23V4o1dmjdcQB4k-kIfenvfQPj5F3lGja6Fney71DWleli0EKAYivvakL7mXpalboCnEL2Vt9I9x8SXz4QzAsV1JsgyItslktEtjoORaQQrlw9gtqL-8V86PUFbdZvobmW9KGyqDSEKwBQW5HZ_4MV_c3NS0sDlecwRBQrjtkrRuoGT8A0a080HhWTllEXyLW_VVE6yhXJWTjN-fYUjwTFL0zMPXsuo3ml20VCc3hZDoFoYCCr7WejqEw_Sy_nMQ2Ej1UhNj4Hk9UcKRvUpdq-xSsrffry4w1SGxpW111bd0heOyZLPGDCPYH1QJiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732d114172.mp4?token=NPeNYvvn0hVyFuh2iatRBsFy23V4o1dmjdcQB4k-kIfenvfQPj5F3lGja6Fney71DWleli0EKAYivvakL7mXpalboCnEL2Vt9I9x8SXz4QzAsV1JsgyItslktEtjoORaQQrlw9gtqL-8V86PUFbdZvobmW9KGyqDSEKwBQW5HZ_4MV_c3NS0sDlecwRBQrjtkrRuoGT8A0a080HhWTllEXyLW_VVE6yhXJWTjN-fYUjwTFL0zMPXsuo3ml20VCc3hZDoFoYCCr7WejqEw_Sy_nMQ2Ej1UhNj4Hk9UcKRvUpdq-xSsrffry4w1SGxpW111bd0heOyZLPGDCPYH1QJiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار خلق کردی علی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82738" target="_blank">📅 21:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82737">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWlNLJtAeuIrFAI68xa_DV--Q9BD7fcolId1lLbh1iyFGlb3InnJ5GifS_xJHHvksIjhtml7Ir757TA9R-hTuNcuoawESNrMqhvTgzjaovGYCLRtlVomY5jA2Jbjqj0CXO0LMVYGjEDzTrgaZ9uXiuRkBqUHZ4zVT0pbOulC4flU6iryV-nLTIueyO0wBNgJxkwDkgIqArC4Fwh_ON5jVcVxTaTaBmEIUsSdAYTTINnCPcaT-81KmcFBXVPlXHHi-PXlRvPUD4Aicro3VcNk_uW2ufx9UZ6sX0qCDo3EcLWAg8rGMFmSIu0HMwDTb-wD2x1WVn1ie2i6T7cS-9CgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نپال قبل و بعد از سیل
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82737" target="_blank">📅 20:56 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
