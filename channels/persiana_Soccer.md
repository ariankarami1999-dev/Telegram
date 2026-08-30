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
<img src="https://cdn4.telesco.pe/file/SgUfEcR3shLhuSwninn-34iOUl9mK5wKS_vUSoWP2bc_L2sa8XUuUN2fVWx4Tw1wylhm1s4xRWB1NrwpBSNubVYjyffUklrr9Uh62Gr2HX2Jz0Y4Xff2PT6pR4TJIizSSpV7HD3PsEIEiZkz2qfcIpFf-UZwlmI1xYjz-3RAIVD_paqDFWYxFzz1r9shUowHePLg4mYIHcSbhbnSXZo6AQhRjCVhRTMhs71g3ppbV6q5XHAPrUKRd9DW5J5_ts1t8FX7ycmHnTnk-hbkHJw7IaqIo7m270fgCHz2Syq-GrRout5zbrzgEKw2uNkBaVYIsDRGXuERh36N_s1bI2TYhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 627K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 12:13:41</div>
<hr>

<div class="tg-post" id="msg-28723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=Tn-t3JNhAPR8M9HwVo_a_ZQbYzOi04Tk7_oMvhKZO8SH8iXo4zXsiVBvH_0mTZ9_vRReJYeO7-97Oha7Tp-LaCxCqfuZFYlHgcUaFHJevMVhk3K5-3Ow6zxg_KmGsWSGU_duNHYh-2mcQPkzT6goNX4CYZPtNqfAnytIpaPjPAkiWbMIHqMtXvNWOVkFjFW-awOWWqfJOqWMfWL42AaD9nRyrNa_Mn3q7Don1Gez5XkBI_NK-N15GH-1YQaVW_11exghHREeRsFU2D8Q8kRqk6lUziFOIWTmLN32j2CbDxlv8s4dZaTqj-z1Naa8Ds-l8u1mGQrflrjXzpipS5kY4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=Tn-t3JNhAPR8M9HwVo_a_ZQbYzOi04Tk7_oMvhKZO8SH8iXo4zXsiVBvH_0mTZ9_vRReJYeO7-97Oha7Tp-LaCxCqfuZFYlHgcUaFHJevMVhk3K5-3Ow6zxg_KmGsWSGU_duNHYh-2mcQPkzT6goNX4CYZPtNqfAnytIpaPjPAkiWbMIHqMtXvNWOVkFjFW-awOWWqfJOqWMfWL42AaD9nRyrNa_Mn3q7Don1Gez5XkBI_NK-N15GH-1YQaVW_11exghHREeRsFU2D8Q8kRqk6lUziFOIWTmLN32j2CbDxlv8s4dZaTqj-z1Naa8Ds-l8u1mGQrflrjXzpipS5kY4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/persiana_Soccer/28723" target="_blank">📅 12:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqijZWdUvvyrzLPaJtusJu0Vs97lg2jxbCrs14LU8ZqJe6Q1vzN2fU-kdvsc8Ol0-Y-nMGgnveeoXGwiF68MQcAIQlD9TjaSioNJU9YDttjqnTWwDOMLGMYtNO3yNk0Txcnk-MYMjIJFD4No_tkdQZJmqxiyDbcqqA3vYkX9gay8EyxPdLgLPFNLmb_TPjNSd9ribELQWtKz6VR56W5AKIbk9EKt6rdrAfQOCAqfU0wFH5TIUrolddILOywzZELhq8vW9fJJagQ_LBKVNtoLc8wZMrs8yUB3DCXvqe-b1ulB14NCNCysmkYSbmGuzmL_Ct2BkId1OCoYTb6W5yjlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
ویدیویی زیبا از پوکر تماشایی لیونل مسی فوق ستاره آرژانتینی اینترمیامی در سن 39 سالگی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/28722" target="_blank">📅 11:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFDUezmpVWoihhV5OiO4MDvKnS72PyqepGFE9Qlylgz4i9amw5DhwNNLQOFeE50CRXZDtn3h2z_85xBjmgAbI3gvP3yUwDAsUE1AceJf9fRnlTBuKbM4KDJmLT0_kbWC89N0FK2LzX-IeI40d38MKfd8rwKlhC_SsZBZhQBkgc9Tjnu8aPBIOnnbPHgnNCP-1iS2kKWepNFhdN0U9MpYR4wD-eH4QUWnJ6oUYFsyWEX7Ss1Amel4ORKfteTqDdJxvr3Qv-vPA0wNx8nq1ir8QLYQtNFByVvNZfurWjoG4ytv5078sHyUZx_gmWIFNM_uIY6gXGKfXB8hky6UkVkzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعداز جذب دنی ولبک و جردن هندرسون؛ چلسی به درخواست ژابی آلونسو امیلیانو مارتینز دروازه بان 33 ساله آرژانتینی تیم آستون ویلا رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/28721" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28720">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuXUW19fsMZhTCJfMUr273D1PWe-ypibC8UBbmLT4D5YR7ot8lCJwAk_8pRmPdQSXJ3ScvgiiY4eQdG-PxLUf0OVak74G3Hm_2dezFa0KHk-GvyWXeTSzm4PdCnSAOKlI6dZCVESVPx85TZgd7hpSgWsews_wRVNScMV3cm6m30oPIbeNSVL0TeevWhkezXRBQ7W4B0isQDqBrzbuSssp2udExi1EMvCCZ-2cs8nx7epoSFDX5YOqs_wNxfN62nx_rYY1G9XcPrsT3O9MWAc9AS91dclX8mwqf4Lf9Y-lD6QYep_OGNW0TUIFGoLHnJxv8Xf0mr14UWVQYOKLYK98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
منیر الحدادی ستاره سابق استقلال: هیچوقت دوست نداشتم از تیم استقلال جدا بشم اما شرایط طوریکه مامیخواستیم پیش نرفت.‌ از تمام مدیریت باشگاه و هواداران که این مدت به من و خانواده ام لطف داشتن تشکرم میکنم. امیدوارم در اینده نزدیک باردیگر به جمع شما برگردم. تا…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/28720" target="_blank">📅 11:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf9l4GDihPQLov8HWsMspsA8PKGTDaLcyfNNr_zgH3xeL89zic5ITOJrTTv0Cf6_8cmOAlcBg7ru7HEq7zmjH_YI8LOpiVjWrR-cgYSFi9yASsFBeBJIiexVEqujSztDYO1vSpRUf5vf3BJ-xH2X_pqdEHbe5nzpaR0H9w4sAvs76XIch7W_JW9L5XGcVj_T1UsF2kNlJVIge0IVX2WnT8W00lkZGk0ohnLtLudCK2cRE2cnaPZggwui7-Fug2d0NZDW7S2HF2-Qu6adDlw7TD8ZwIrrk4r6wxpegUel1JroeLL8hzRhw9JWw6RPcy6IZPamUnyRdelXxbwSvmEsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/28719" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4635dd1d8.mp4?token=L2pS4Bxc6CyV0JR8TdH1L_wz-PI2-omPb2kfbSi6YTgXmmHKQuY898u3u1XZFv3MjopbRvJFNFHOedDkfO73Mk-6GaO6xf74_PSOqBHEfwDi43QAanSEim7U6Pr0zbp-ak_R4NPD7qgMlESu1OqeoccFeLKlo-eRI5hF_WDFhs6ZW3aS_czievNsm2DIXXk3v8-tObTDv5Fr2xy7FWs6nmlmwIXIaJXgX9298HpwqkzVWRUjgO-qy4AFW4XrSZXvPUPaWbgJ_44N7jvsCyPzvZMHzqaGxNySvnp-UdSU6eiiP2sFq_BVtxgvSJ9Z-06tJVjdyjyQrZYnDF8lNsCPPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4635dd1d8.mp4?token=L2pS4Bxc6CyV0JR8TdH1L_wz-PI2-omPb2kfbSi6YTgXmmHKQuY898u3u1XZFv3MjopbRvJFNFHOedDkfO73Mk-6GaO6xf74_PSOqBHEfwDi43QAanSEim7U6Pr0zbp-ak_R4NPD7qgMlESu1OqeoccFeLKlo-eRI5hF_WDFhs6ZW3aS_czievNsm2DIXXk3v8-tObTDv5Fr2xy7FWs6nmlmwIXIaJXgX9298HpwqkzVWRUjgO-qy4AFW4XrSZXvPUPaWbgJ_44N7jvsCyPzvZMHzqaGxNySvnp-UdSU6eiiP2sFq_BVtxgvSJ9Z-06tJVjdyjyQrZYnDF8lNsCPPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/28718" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOhrA7lHL27Jjb2V2Wsd9nxt2Z0hYBAZRPZYCGx4tYBAew0j2mo76Yheg4UPfiYdhOsirWR10j3HGuVCaTtMMx77mXTOBllu0-q2XK1swJwiX7ZlFpDVhiXXL7XsI1nQnGG4InRL3Ghep1at2j8RTRkn7JWmxyU-SkpGzwN94Fjl0CU_QbbjdAzr9GGtz_yB5-b-13bzX9Dxm7yNFzq2gkwbO_E00RRzdqZRwpQXbY44wWqUUQpUtMRXGHn_uCzLmFqkbkByybh-jr9QWIWTdUMUrttWO2gg9NQ3AV1IuMMZwAEUhl89VxwJ2ujZEqNXcihL1PJkQcVQ4UxeV33RAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/28717" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alur9_zxePdlVigvg28sPz4Y8uGHtyCIOR69TzQfV9ctMEBGnfxv0bixXyDKNl1gpYps0FedSlPVpxnt3TudAD-IHA9YDdQtIH9twh_7TOd7ZI1T-E-iRqqk40H5D4shSpJXq_1uO0mBaIFr4Cq_T1VymDg3rdj4_-JymmAagLWPSdz0AnIwn4QingwsKQnkmtolYN7fUwF7k8KGbZgeqKg_tb6suN3qZ7r1i-BXTKCyE-l9-CYyhfJBaQeOJIA3E-d5a-j-2klCrDHcpH5eAn0s0kLIDam_neGoyIsa4auP48QAF9atxHKtkXeF96BLmzQT7J75gt2urkvyqJffzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شایدبعضیا یادشون‌نیاد ولی کریستال پالاس یه بازیکن داشت به نام کریستین بنتکه تو اولین بازیش مقابل لیورپول دو گل زد . بعد دوباره در جام حذفی مقابلشون بازی کرد و دوگل بهشون زد، دوماه بعد تو لیگ مقابل‌لیورپول بازی‌کرد و بازم دوگل زد‌. لیورپول ازش خوششون اومد و خریدنش یک فصل بازی کرد عملکرد خوبی نداشت فروختنش به پالاس به محض اینکه برابر لیورپول بازی‌کردمجدد دو گل بهشون زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/28716" target="_blank">📅 10:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28715">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d907216599.mp4?token=S56SeYxj1qM180HyEdhm8PuAqBaG0nFqruNx8rXv_3oeaCTJTwxTMk0abCUzgEDazaA8tD8rlPn5ACRPsoaYuHFrkf7ph77NWxpI5x9HIfc8fBkhXo06Ly2u6hHtOqOMC7ui54vAKmGc7QMWM1wyI__qmJyXibz5_kgAh04HUa3IgN051C3jOdYAvWdJblSVtu8MOEh5IKYMhbF5bPhPG5e4YnM_mUuRQwSoL1Wz4uEixsJzxXt882uopBYLw16tS3NDEKLA8cIF1XjSRPk8SWrk45fK-DX1SGOjqDkkrmt0HyVPwEMhr5K_g6LfaEJWxBErdbSAmbM3Poo1UojL5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d907216599.mp4?token=S56SeYxj1qM180HyEdhm8PuAqBaG0nFqruNx8rXv_3oeaCTJTwxTMk0abCUzgEDazaA8tD8rlPn5ACRPsoaYuHFrkf7ph77NWxpI5x9HIfc8fBkhXo06Ly2u6hHtOqOMC7ui54vAKmGc7QMWM1wyI__qmJyXibz5_kgAh04HUa3IgN051C3jOdYAvWdJblSVtu8MOEh5IKYMhbF5bPhPG5e4YnM_mUuRQwSoL1Wz4uEixsJzxXt882uopBYLw16tS3NDEKLA8cIF1XjSRPk8SWrk45fK-DX1SGOjqDkkrmt0HyVPwEMhr5K_g6LfaEJWxBErdbSAmbM3Poo1UojL5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد گلزنی لیونل مسی، رابرت لواندوفسکی و کریستیانو رونالدو در پنج لیگ معتبر اروپایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/28715" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28714">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUUNqNXSQ5JuERReuj269FjoLmznXwFcUnaOFj56LcW8OEtMDRdlRUGFmqbVNdOqNyxFOJVhSS-Fv-h84X_5ebAnvjbvbKlJBVqKnsBJIIk_VC7vcJ37caOrqRYji5NYzJvXJTuXlsjBrGM15MScrj_2e-4FVTYBwklHXtAPUDWaY2AF-XLQIqIzuGMnQyYI_u1AflL1tHthF8k1CY1CkxY42Ovjtvz2Jj2euaAnwtWqeJwS60PepvXvY0ca7TzK4LniAxCAudCnfAWrpT9nSVUlDNdhsd1mXPVoazz5_p1icABLUlUR-aK5U13RIpw2ir8zE2z3gSQCBkY969fGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/28714" target="_blank">📅 08:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28713">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/28713" target="_blank">📅 08:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28712">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFEd9JZNugjNz0N3SwCjEkxoyso8SLYSHXAyRxygAsTNixgcLUgtJP_fuaHFUSsYqeQpZTt_M6vdKrWVaoOrWCWEF2UZ13usWhbu7IjXA9LFe7gf6XXw_vQzB8-PVLXbPLhEUTOq3Xy1v3FMwS9iweURNYFB2tgMVtBtkDFHc1p3t2x3OtqVelKg10qT-4EZNUujaeOp2cMVL8YjdQvRNmsJRV2y3h9Losr36OXnqljHZKqKLcWaGydAs9JYB30va2FXdYUYX5pIa6qLCZHchveGz1gZxWysxiVVXJ0qrwQJEo5YAAqvyN20gIY1rbcvBJ24HMvdDZceyMP-c1FYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اسپورت: دو تیم اینترمیلان و بارسا در حال مذاکره هستند تا برسر معاوضه فدریکو دیمارکو و الخاندرو بالده در روزهای پایانی نقل و انتقالات به توافق نهایی برسند و این جابجایی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28712" target="_blank">📅 01:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28710">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1-St23F9VOy-7mVh6G94EmqPM1xDNn7df4K05dXN025ZpaHz7eToYV4j-HeKkEvlkBQjYT5RokyGCQAxJbKo1LEjM1llXXrLQVvlsjxO6IVHB0fSL4y1lMH7xazsrGJx1VZpJKnttj-q6LEButYLuxsf2Xa2cy6ebI5_2Aa66HABh_EOVtib-5mH_6wmxI-BCYYpW6EmvxX5OJKtKpdJZaeszdNyQX-M3yLCRb-UrDLq41HnjuU25Z01ZVeVcd2Z2aJteKLBFAB0wXG9WUzrvt5XXOiIahFvV-1jqpkwfV-OuXij5u_sp16GZQ9q4jrc2epfvOwB7U5ieh4gM6KzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ نبرد رئالی ها با تیم سابق ایسکو و مصاف شاگردان کریک برابر ایپسویچ‌تاون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28710" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28709">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db6agi1DZEaE8C77NxGbj9veI4v6tNJmQ14nNlw2srkLXTo0W5175CVZbg4_AeKGJCt1210JCUxhRtRkCGytPVxNAAoGlebRYJlnwlL73R9dqBsWuRHlY76yZR0-4cJP6SVNOz0g8X6pjH7GLmF8siQlXzo5dyWyH8DA4ceXi94xx_e8GPwT0ulpbPOKPjk-ltR420qsZ2L4WyI-FGoVuYFS1h5L3Nc9hy7XYQbDQUsoLg-DUgQrkuZUIufVhQ1W5DzGZjP9zLqS709LgCzIiolV1v041qJTufGUjknHvZ2ya_6A4g2AB-T4u72-UrH0VT56m9R2BGirXgjIQizOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
برتری قاطع پرسپولیس و استارت فاجعه‌بار شاگردان دی‌زربی در پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28709" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28707">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqXKs1joiX01RC3vQjhzFmVSgrYWaMdcasJMa3yfP2yDe9fscipYcEe9A6Q3BI3c_0TP4QUY1dqA9Bx9A79e0V0PGItlGWePnixUbct3Z_tFeHJGoRtTBFmyiCg1dmm4-lTJ-wEKPTMD3bcaIst2eOe657MHz1bLkvYSXQD3vIDVK9dOxkljhoqAdXU55t4lVfzWhYntcVohAFV7Tku6DK7Ch5iUnDPKH9qJt7mT0husHZfe3bkwMp9EC3h8nS-ka0NYHJlpUh48HbCDtJOnl-poE3FcG0DBrh31rBGGLIGnxOL8fZD7dqg5WXZtVWqlBcKMhqlaF8QBs9wYSycNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍁
پاییزِ زیبا، پاییز خوش آب و هوا، پاییزِ دلپذیر و جذاب‌از رگ‌گردن‌به‌شما نزدیک تره. این گرمای لعنتی بره که برنگرده. با قطعی برق دهنمون سرویس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28707" target="_blank">📅 00:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28705">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GILjbqgErOLZ7AccQqNPRDjvQUaFd4Sw4RBSj10raWsBmTrgiQ7PVFrnMiDQ2figUZzudGLo-yCOKlljsN2btBUnOHGPdI91u4QE_48IEKBPJEINSV8hz0Cl81F2Uykd_fNDCh1LGdD7KqxVV_hjwbJY8rX6f2zQBHXwc9TaE6ygu66FD43rnoong0yRj1tviJju1IKsHC7T-svPyFxA5eL0_D-g4OcEXCt5IXOj_bJUufsVFEiejM_kobwqq2z3Xxr8KBhWg54jtiuhPSLI3fqMWDb5Sxk6TzSi73dEo1aZdePFcypcHn5Np6-SSS001N9y-YAfQreUxjdKxx5heA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنهایی‌دیداردوتیم‌پرسپولیس
🆚
ملوان از نگاه متریکا؛ ثبت‌امیدگل خارق العاه 4.02 و انتخاب علی علیپور بعنوان بهترین بازیکن این مسابقه یک طرفه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28705" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28704">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-LAKuDNzxmA9P08jpROi8ZUJDtHw8JdCZymPMlxveX0PJlWW-mewb4Bwm6XgNP4VCc8NIcsZgeswnpJN6c0HZTIBSlDOteM1nEOA3TDoDWYQ5-kdkxmwGrLfMAlfzNDVC1H87eP8d-_jiWBc7c7JoxURe4bNJNHxa3hf_UthEWwnE5k2kPg5Lluxoek_BtES5qEX-6LihyoHUNYdVlx9d3NxiYuF-PF6rITQ8drnn-zy6mKr8-PBqd9lOJzBkbUahmGjYaGMJ8b5xEqxfjzA0eMmC0nDM0gsHNhWqaO6ECoveUvB2YMNQ3shgUtmZybgXDIqP466YIbjHsvw0whdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه«Novi list»کرواسی‌گزارش‌داد که محمد محبی برای‌انجام‌کارهای‌نهایی‌لازم در راستای پیوستن به‌تیم فوتبال رییکا وارد شهر رییکای کرواسی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28704" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28703">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXT9yoUGRhxyVnrUM0iV0Uxb77LDdrguXtT32ckkFUGttCwUh_PYmE6CYxgHoEY4PzfLUIKRhkvdj1ddjDMNJdI3ptofb3nLVAZV0HM-13VFcAfHpIht1ilt8gUbb_4XmpsBoUujhJlMriWLQnfDOuYAoYTEN13hdiz2scGULea6NdJPH-0-oQE6I4vE6uHyfDP_a3cQur3_sJabJGC8QeRk6AxUFro3F8WLnGKrt3NJWZYoER8wPyEzUYLanEgHA6rukEAjhIzI-K4ILJlb9aO-f_4dMMZ0aqvX96SKnAo9I9M4qCzHU03Ggb68_LNzPBJSLGecy4P_1d5Ufv4NNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/28703" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28702">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-wbx31YbpHLfZPAZ3havhgDYueCSiROYY3rQOQ8MhX9G45Ptk7zwPH_Vhnn-oVmhW79xn1tuLXCGGbtDPoyFAwncaeph9L0LHCICyurBeXjZXtJ77tDsTKFAh7_3pLEU5zX6KxwCPdXASlkMUODKPihBjKEK8RjYCzhWNP8XUXglEJhhHgYwLcu1U-EwkHSUxU65by_jM60BTfkKOiaGtorfZ_IbRHTTgN0pNLLnxIB8KaIEWT-5MKJwNwIUeHIT4ZDw_uRrI5t5IKNlPJb2YApurS-opcecQPT_reV3upp3ln-NIluRhPU6ejKgMdhKJL1_aOE7cLdkJMwB3f3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/persiana_Soccer/28702" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28701">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcYvn6W7xoI4EYnkMO2yUFEjoZrgs2VFwAVeeyiLBE354jo-KFvb4iDBj0Dl027OlO-pGGgBRtqRMNaa4_HVHFY_zgUs6Ax6-mXLWbvEeqy5F-BvnypOoSurSx2RyLRxnyEMylAT1iXZsqTfmOyMJNdggUFciLm_YqJNSghepbEpO5JjDHoTQRwFF4HNAcEWwGMQTBUkOE2HAG_5fYVJUPGT4Mu0-ndmQ4lEBl4bqkmy3Pj_kpFaVAYc7E3GtWY1--yVy0e6ZHIVGBdJtm4syt89MyBSgbueFdiFzZFyCmFrMqrzyfHHmuSUZQzYwMs4i8WX9Iepq74NLMo1GBgaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام جرارد رومرو؛ الخاندرو بالده مدافع چپ اسپانیایی بارسلونا تصمیم نهایی خود را برای جدایی از بارسا گرفته و بزودی از این تیم جدا میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/persiana_Soccer/28701" target="_blank">📅 23:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28700">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKBbK9cEamUOvexRuqdxgMUgemyIADcVXKNUe4c9Eoz1NC4ugBFwpK2oLAmzI3qSnWpH1wIQVLC2ZeIwutsAJyYS1n4ecPrgvtPdRxNcGv9dvzpv69xXneOO-zElwFytKKfKtFZ_OKOsgSXw1Ld-pYy_K-0wjpaxRtI27YHZqWguZlWVRTXdWHMdHVcuwZmRkNRshoIAkFQW3kQWggUt5Mxhjhf5IgEXg27_dgQPpQMVB-eFURseCEnfND5BIANwf7K-8dsraBE3ldc32N2-GrSdLMTR9F9PIYgMjug8BVhkbNT37CH6xK71EcTD9vqHnDE1a5rqC4Oro_lDBu4haQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28700" target="_blank">📅 23:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28698">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpaokd3jlqkU_BWZhvGMNyiHYTAsjE-5MHv9nM3JkeTfRKEo8CIN11zJtxJ7mooVAH3G1MQwSTRvH54RJsMo82udHn_of4-JcBFpkk4McGTovns-mXTB765Ry0xKbB-UEx0MnZZiPX3c-S1RkWwBk6ST8mkvBswL_9EIFi6NLlKUBvEnqnPjO8vI46TkF7hAuau6KI7o_zb7S9pUwyfNDHzTo7PZO8YquRg80teVA6kqJmeCr4ey3ssVUFKk-G0G9aFngLledekY3cycFlZWUqno-EIffFKH_MNg_5oPGqts_4jtcdXOu6WAJj3vs-En2JpONEb7LgkxS_kEgLPWoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28698" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28697">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=u4-1qbB1IPMNMpHZK4mAZq_ps-X475_wdX-Zfsx8tawfA_-lsSx6m4Yoe4ANCmdkvFZR4co-P3wrkSxNJabupfVB9ISKyGx65UhZYjZsqQ-7X4wXjXXxvePqI2_ACIbhcRu2S02r4WxTCPf-FapnWi740e_-Li5Wqt7WaLYO-5H0SGiF7xVAzVd5SyRMu7n4Aawwx3xLMWzcrAMM--dGySXSshQqXYdeznnltYSzX7mgysb18Fvz2-cU4c-aEi6B4aG8xKRWhGzjLyrwoh5xznnV-df5-Rk9Y42weibs7a1LwmKwFBWAP7JKUt2A2VFQlpHMwLQNxTrxmE_fmsFdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=u4-1qbB1IPMNMpHZK4mAZq_ps-X475_wdX-Zfsx8tawfA_-lsSx6m4Yoe4ANCmdkvFZR4co-P3wrkSxNJabupfVB9ISKyGx65UhZYjZsqQ-7X4wXjXXxvePqI2_ACIbhcRu2S02r4WxTCPf-FapnWi740e_-Li5Wqt7WaLYO-5H0SGiF7xVAzVd5SyRMu7n4Aawwx3xLMWzcrAMM--dGySXSshQqXYdeznnltYSzX7mgysb18Fvz2-cU4c-aEi6B4aG8xKRWhGzjLyrwoh5xznnV-df5-Rk9Y42weibs7a1LwmKwFBWAP7JKUt2A2VFQlpHMwLQNxTrxmE_fmsFdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28697" target="_blank">📅 23:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28696">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCcrklYym_XJXZ-FvQsQ4cb7Tlpk_a_qIRpA-K4k7MSUxmdFeRwqFcjgbffWDWgb9t0xyvUGNtSjsdVkVbhMlYdXucqmnTU6AP2QIgYl3fFbGOtxvBDVLYYNlqJ96C0rZqoIQtAsDzbN9n_OQoGcgNcXT2locDlgEWEGAScbur5ZAhTaOsJhL1mVanf54pSNcp3KE5ud3v2_AzXD7DW4Hj51_X_pDIe_xIP8oDHUCw7dcaEum1X4cgWddudfvWk-mOIVL0v2rN2nN-Zow0D-Vd8QxbUQhE8-Ig9zTpjf09wC3Y81tcXt3V3IbBAu3KLnFs9RElO0l4UbexXC2XQO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری
؛دیویداورنشتاین:
کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28696" target="_blank">📅 22:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28695">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6xRxFN01fZqAEiAMAnzas2hSpq5jYp-v9ObVRl0-OzxGGWJHGTbnz7CK-7kTEScJ8Wnzrf1c49beaC74Kjs0fSrYFKHyFcRAIc79LqmFYjC829KFse6V3mPLLYCugGgtLE6xwN1CqwuQVBGZNHl8Pfo5BBUBj8NLx3KEv_kJ0txW3BDR7C2kE3WyZaKYhxf9POVtQfNNoCRmCKs8YL2mlQk1Hc_cM7dcl5ktdron7V7q2MhvVlj0_AX28DAHdVP0fFEuiaOD6r6p7kkaRLOwbQpXN04eEwa0CrREH8oaabfBrUxiDjvUP4WpOzoI7OAImbeSNkEEStKmAb9R0f2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های محبی قصدداره بعد از بردن حسین‌نژاد به‌پرتغال، محمدمحبی هم به پرتغال ببره و نیم فصل با رقم سنگینی به ایران برگردونه. فعلاسر انتقال حسین نژاد به ریو آوه 250 هزار دلار به‌جیب زده قطعا سر انتقال‌محبی‌هم 300 به جیب میزنه بعد نیم فصل‌ 1…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28695" target="_blank">📅 22:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28694">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=TlW6PA27Dr0PHidUHwktNO2UWW8A9GzZGeEIbI-VbeJshm-UXRcyFBHKANF5q31lgQTOj7saD61CJQlY6u8HvjdTyHar7cDhkVGPujY8Xc6GxVz6J0NkZEFbdVCdVBkfVQLUe-JMDlKi2Fo8-uux5xIYj5EUyhE7cbvbTVnBroIFr5Zon2jHAwATc9cXWhf1OS1cWrLNi_Q2hpOVtGdOoBB_J5RWkQPjEO85oZoDLBluLD2VcayFy-y_nGuI7wvwW4QlExWCMrGC5d7OfA5EXx6CWqcDwzU5_EQUgxG4ynZg_fCXhU5IQV8VfO65Vp7Q6vYA6tJv_fJk7wgzpF8m2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=TlW6PA27Dr0PHidUHwktNO2UWW8A9GzZGeEIbI-VbeJshm-UXRcyFBHKANF5q31lgQTOj7saD61CJQlY6u8HvjdTyHar7cDhkVGPujY8Xc6GxVz6J0NkZEFbdVCdVBkfVQLUe-JMDlKi2Fo8-uux5xIYj5EUyhE7cbvbTVnBroIFr5Zon2jHAwATc9cXWhf1OS1cWrLNi_Q2hpOVtGdOoBB_J5RWkQPjEO85oZoDLBluLD2VcayFy-y_nGuI7wvwW4QlExWCMrGC5d7OfA5EXx6CWqcDwzU5_EQUgxG4ynZg_fCXhU5IQV8VfO65Vp7Q6vYA6tJv_fJk7wgzpF8m2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28694" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28693">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e895367e.mp4?token=FNiEiOkIMcaakbQJ7w1DEATB44CzGd0khEbaBLl-642FKMcJgsaspLLWNBjtQwhjdTHATMVcciYamXt7dQElXh_qXRsb4wB_9z-1_wQUSgIOQqU_kqligW9hpPWQrjZtcnAMQPu4hajEPlC3jqYOCrXhruooUSQp8goUOftMw48JyLz7BegqWQ1vItzN1NJUYOz2sB3Mb8K5WxJSHZQrL7UaxnQg1Z2lAfiYlr43M8jOwI9zPreQnXQyDfCt_K2jMiq7SXJ62rv4YHiervCcG3p6E2DMOhM26sSZ6QVCWTW_1MQjo7NwlHYrcskCXHkklpouUMEPKj8cHjEUWSk66Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e895367e.mp4?token=FNiEiOkIMcaakbQJ7w1DEATB44CzGd0khEbaBLl-642FKMcJgsaspLLWNBjtQwhjdTHATMVcciYamXt7dQElXh_qXRsb4wB_9z-1_wQUSgIOQqU_kqligW9hpPWQrjZtcnAMQPu4hajEPlC3jqYOCrXhruooUSQp8goUOftMw48JyLz7BegqWQ1vItzN1NJUYOz2sB3Mb8K5WxJSHZQrL7UaxnQg1Z2lAfiYlr43M8jOwI9zPreQnXQyDfCt_K2jMiq7SXJ62rv4YHiervCcG3p6E2DMOhM26sSZ6QVCWTW_1MQjo7NwlHYrcskCXHkklpouUMEPKj8cHjEUWSk66Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تاریخ سازی دختران ایران برای اولین با قرار گرفتن در بین چهار تیم برتر آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28693" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28692">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe8rXpSFObkAe_8SFkzFU2JVNtf-0ISEB0Vbk1_N181OMiOoNLYnHENKsiw_XfWvgdMqCt1sgLMOcjNH5Jz2BiL2JlU8IlQ6Wv0CWlW4WVjKEbkeFnQjlLoGVEcXxYshmxMOnncQ3OTplXDtPwz-fpXhgMm932j8bYc9-ifDtKGFr4EMdBSosvE1QIzGHauhvZgMnEjrSyvtO-OepVXDbRXoCPureJqcqowSuWBNOFA_1Xu0X70nVIuhaRpXwTvqFWbAY66tGKyM0kHP_o687jt54QbOGMiun3H_QtrCmuF1ZEHEKZ4Xnl1ZArCxMxRvV4kfxM6n7lrKqPFxYh1puA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌دونستی‌امکان پرداخت قسطی می‌تونه تصمیم خرید رو برای مشتری راحت‌تر کنه؟
با درگاه‌امن اسنپ‌پی،
حتی بدون داشتن سایت
هم می‌تونی پرداخت ۴ قسطه رو به فروشگاهت اضافه کنی. این‌جوری علاوه بر اعتمادسازی، خرید رو برای مشتری‌هات ساده‌تر می‌کنی و فروش و درآمدت بالاتر میره. برای اطلاعات بیشتر و شروع همکاری با اسنپ‌پی، روی لینک زیر بزن
👇🏻
https://l.snpy.ir/hw5zl
https://l.snpy.ir/hw5zl
https://l.snpy.ir/hw5zl</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28692" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28691">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=aZVQBIXXASzWquwBzVz6qrqH6rP0lCFHzWMQemfreugPu1qTsZbPOREuolT2_tDPZUMONbZq10vWNn1ap0HsXsGq4qbEsWRkrl7OBXVlCddmx_P_XDmne_RjHOzZ4C8FN02HPKF-lrBN_EWYYER3vyX1lmYGRHyo7IbQ6y0BqN9lNrj_AvtyJSE9TUz17zJPk5rP60bMH0HjzzW6l7JxZgHQe1D68KIWQE_ZxpKZSsErqOSsXy7MWg9H_u280T-KHm4ewh0sBjbznFfBPEAUAZDufT0529H-6rkv7eGcxPOgPn-E2_-WxCB44OhBf5haIfuczFbLsrieqMD23TFd7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=aZVQBIXXASzWquwBzVz6qrqH6rP0lCFHzWMQemfreugPu1qTsZbPOREuolT2_tDPZUMONbZq10vWNn1ap0HsXsGq4qbEsWRkrl7OBXVlCddmx_P_XDmne_RjHOzZ4C8FN02HPKF-lrBN_EWYYER3vyX1lmYGRHyo7IbQ6y0BqN9lNrj_AvtyJSE9TUz17zJPk5rP60bMH0HjzzW6l7JxZgHQe1D68KIWQE_ZxpKZSsErqOSsXy7MWg9H_u280T-KHm4ewh0sBjbznFfBPEAUAZDufT0529H-6rkv7eGcxPOgPn-E2_-WxCB44OhBf5haIfuczFbLsrieqMD23TFd7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
👤
مازیار زارع سرمربی‌جوان‌تیم‌ملوان با تریلی از روی برنامه فوتبال برتر ممد میثاقی رد شد و گفت تا دوربین خودتون رو از سالن بیرون نبرید، مصاحبه نمی‌کنم. دوست ندارم تصویر من رو پخش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28691" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28690">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuyvDxfKC4VzciZdNkfS40eekcz53Y-qqHSpHtAOV06pSeN2wG4OnF3piXkjSGrs4XvSQZhkEZIHBJZqOZKS6V_nnEYJ3-ZRtt0mwQVeOvZMrdbtdzBqx5AyQFe2Kdf8TTczrtTp4scxgcGjm-Pol-vbOBlp3VAZJ227wGCXSalhIYCFdJEbYFmsaPPzhOBJZeMeQyjDCYjiLfluMpo_gX9FOsTVjQK80mlZKlYeTrTknPhvQApwLwzIZYr72rEuHowacTd-We9D6qcGY_pNqde9CnxlZG_irO6xmejiNe3-HQR0wXEqlMb6DbcxMyOpSMmS90RZ49eWV0j7OKQSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28690" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28689">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwiTpQZHSGQ9LRqdW9HdvhUKpNUPixIed26KMnmL94ASySifVgsKetHIhMzpk2SGVXVjAZirWfkG3VoXtKtLrRLrqJygKWQwEQUYsDdH1luWseJV0XIhAZBW1caqUtHjbhnGIvH7-t51Lg-Rqamzkzr1W09yHTNVP5Bd1SyfSv69vZmGRPmixqaUFCMu_TJsh6XxWAOVzv_-_mDV-vIM6L67jPJCRPdtY5ueOQt1I-OCpsmm7-LS-ae7mT1Qu7IwJXzGVaNmLRjgU_oNyRIhBBx74Rmr-wlYzX-XuNtakmNwGWEkr4UQKqa2UpMbFEMX8EBKJsA6CiXEfKuvslRODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌ونتایج‌کامل‌‌بازی‌های هفته چهارم لیگ برتر؛ تراکتور با جواد نکونام همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28689" target="_blank">📅 21:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CW2RzCML7Qt5yaS09fFL-r8aJJGXwXSArUMa1q3P4ESMWrNwHs9TI2a2uVEYy7eK4lIJ-25YRD-hLkf4I4PZ7bKEpCJ1ENzs3aC9fNJAAeajUQg9UE4jzpyi9LSfCajqY-NdGD0uboxiDI-gh8GZyd3BwvYUSVl2kao54lcLIXIq53PnGVdzdn70D3ns1v_ckSIEl0j70d4OvwF2RNHhJ3MCvW4OsIGUnb7wPLrZGKCR1_bwCcVcf6lRzonfG1BRDIGpAMMmfJzDvwuMqc19YeNxUEkqdvqD9NeRKgY3geCQ-XEV70eIfXGH5BlI6BOxN-B08IBl9C2RbPZ9skgTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwIFvQz_uMg8nbJbeD9YWqwQ6oRlYg462Aer--v_4CXQK4QzkBGW2mQgsDmG_g6KTMjRodZAfQgUxDzIBu4mTLtbGFtLaNL7SDqi6QAFTjGgYYKVk3fiFM0aPUW4uJyBxDqOWqNJU3gswXAYmjlCQ23H9eADciuqbMEvepz_SNEA9FeqKZEHaoAEpEsOhnckZeQ0d0PsrT7LXSnXz5j1xq2fZHWXW8uaDnAARl9gSk4IKuOQOlb-60YeKNljBDbvDzdDHo01x4cUvI9FSD6ZGu3Kxkv9lbumoFvvFG3BfYzbTNN9Vj1Vbl8A00UAyMVAlTu7V4KTPYX_1Ti3k8MdPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28687" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urHvuG8BG7TNyXEs8ryfywTIMsw16NDWxLQfKu2YdDv66GQrbn4Y2mS_jporUznSH_76AbEjA0s6rPDd2mdKEayomDypKhANZymMR0M5NBSm6-ZGUYo50_f_eL9UICh0s3k-g0f-UeUGIYXqpxqQe3ibkzhMzcaIQJzcqOHpXNZbufU0vIjAqphI0oRxMOG798B9zN1_Bf3P5w56WT4SOO2_hDemxRiO2TsKsRyQNMysnPxonVTj4vgYH2NJJLHqXGZC69NMYRYGODvEjIoOVTk7nKGFfr2KOklhNG4qVj7nGzMk5ligVi1K3mUajygK_J9-ZnuntD7ThDb6hQp5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28686" target="_blank">📅 21:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3zCvWSnjJd9S0rkJbC1fEMQSJLUEi8Wa1Kp9clBn4KONbP71qJ6EAXR1Ve47NmLdqV_0_exP0f6G587Dv4EjZinVmhhuEh29XaLsqoflNRShFDnHpzTKgxumn4JXHszfG7tj6XpDZrtcu9VI_gzgi5wl7CbWcouqNP5h5dFrRWZon-nQTBbWzKLnnds1LTf6OlXS2ri0UtZ0NkOhJvnU8VTHXN6tDxsiC3zdYTEWf6TNr3ZyQGHNJwzi4yUcl7MJc7dD7yZKYlpbwLrRuwsurMqR4Az9el_WxrVLAhi-nqMluPP3AtJvY_41ppr6KyWj9EiLLAqCgcKNjCycJMADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آتش‌بازی‌سرخ‌ها روسوتی‌های عجیب انزالی‌چی‌ها؛ گل سوم پرسپولیس به ملوان توسط علی علیپور '56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28685" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=i32XvOnvVhbesMy3_H9Zg4c4aAQd4O_Ax6Z71pfb0m423ik6l8qdEgxQh96iTh4t3JX15EAW_B5q02K1io6p0eum1OCnqfEWnhODaBY1h-u37jsieVnigPPub7b9SXT1JOHCeaRxaUWY28R10KiGz4WbeDKITmlfCq55HKc0cVNliT2fvq-BZKcsXmgtEKzSX6Bn8l-4ZwwhWBdA0TfcmiG930w_OugMJ21YIbWiy8B8OjqjfbgitfXjoG2KS4EqTrbkrdGuF0q9MsinMEAHFOy18pw6_fRSyLpKMpD-zlVlYWtAMpU6S-_CxDO65LLAWuLKSOUA_sa8tZPqNv4EIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=i32XvOnvVhbesMy3_H9Zg4c4aAQd4O_Ax6Z71pfb0m423ik6l8qdEgxQh96iTh4t3JX15EAW_B5q02K1io6p0eum1OCnqfEWnhODaBY1h-u37jsieVnigPPub7b9SXT1JOHCeaRxaUWY28R10KiGz4WbeDKITmlfCq55HKc0cVNliT2fvq-BZKcsXmgtEKzSX6Bn8l-4ZwwhWBdA0TfcmiG930w_OugMJ21YIbWiy8B8OjqjfbgitfXjoG2KS4EqTrbkrdGuF0q9MsinMEAHFOy18pw6_fRSyLpKMpD-zlVlYWtAMpU6S-_CxDO65LLAWuLKSOUA_sa8tZPqNv4EIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28684" target="_blank">📅 21:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28683">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=ldc4xux3C1tP_8S0Qase95tQF4lrzwEOy3gmlOCmDvhTfn_Xz0IKyXnul6mT8iHI5KoIVSxF1_uJHMyhpJGzwFQRHIqgRPBrmK6K_G8_TsLzBUqfgDveRxdGwY7Je1T37SgJM2EWgGimB8KvRhJDb2JOqcTKW1RdxomXDooDA11kT1nCdB4L1VEReFqmX6kf8cZY2mm3Uv6aTg6pK6ycLGwzYc6vSxOwtSFn9QXbbfuDIg0T1t3dvgRm4XgorQgrAi_xcFczvf0mjVdgG-tKNor3m3qIy4ZJrf5sC6L1kM0EGOdqFgGpZI4JNBP6DJaW5xjpvwvyTyjMD4jwr5ej3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=ldc4xux3C1tP_8S0Qase95tQF4lrzwEOy3gmlOCmDvhTfn_Xz0IKyXnul6mT8iHI5KoIVSxF1_uJHMyhpJGzwFQRHIqgRPBrmK6K_G8_TsLzBUqfgDveRxdGwY7Je1T37SgJM2EWgGimB8KvRhJDb2JOqcTKW1RdxomXDooDA11kT1nCdB4L1VEReFqmX6kf8cZY2mm3Uv6aTg6pK6ycLGwzYc6vSxOwtSFn9QXbbfuDIg0T1t3dvgRm4XgorQgrAi_xcFczvf0mjVdgG-tKNor3m3qIy4ZJrf5sC6L1kM0EGOdqFgGpZI4JNBP6DJaW5xjpvwvyTyjMD4jwr5ej3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/28683" target="_blank">📅 20:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28682">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=UwOdjRk4KtiRHealZ4N-6os4WYE86l3P7bXCsUa1oqDq91iVR8lKGOPPLbJwYuLo8-SnKj5fAOwERm4xVlKm6eH1UkygiC7fcS70B_F_Fypu5Dy4IEEiUAH-9CoM6eDfRU7rP6N_QO7jbFoIJMWN5Pj_nbYR_AbSeYIV1mmXYazH8LUeadcWbz1uPW24pNAy6CYen6aUwRo74QMbqna175wmtj_pICIRyMcY97Gq_Py4XCYgUVSHM0yjPChIr-J02vkN_LCiDUikS2Ha74Wgfm7fGzWrJGUMOY6w2l9vvIHk7TWH1Q8VB90paVMK6yDawFGoKKFFmlOF_QJN1r9Ztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=UwOdjRk4KtiRHealZ4N-6os4WYE86l3P7bXCsUa1oqDq91iVR8lKGOPPLbJwYuLo8-SnKj5fAOwERm4xVlKm6eH1UkygiC7fcS70B_F_Fypu5Dy4IEEiUAH-9CoM6eDfRU7rP6N_QO7jbFoIJMWN5Pj_nbYR_AbSeYIV1mmXYazH8LUeadcWbz1uPW24pNAy6CYen6aUwRo74QMbqna175wmtj_pICIRyMcY97Gq_Py4XCYgUVSHM0yjPChIr-J02vkN_LCiDUikS2Ha74Wgfm7fGzWrJGUMOY6w2l9vvIHk7TWH1Q8VB90paVMK6yDawFGoKKFFmlOF_QJN1r9Ztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریس رونالدو کاپیتان النصر پس از برد دیشب النصر، پسر سامو کاستا را هم در شادی اش شریک کرد؛ قاب زیبایی که حسابی‌مورد توجه‌قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28682" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28681">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4zXxOq5dQirOnDBzWRB60BNybK0NowBxWXte8cXahzhOGudrwnjxIqlj28BtqKbsntw0XD0If9vbLDOVsWqxb_n6PeqNxSu1CN0IGhcSggzZ1fp5rRPzXT3kuw_Tp4s-I-dlutEUcYvjE3NQ4LC1JOujVLgWw00K65cm_E61EhwtGTkID521HXILvpSkCLpTzRQukCoRq3L_GBjxr_fiC4WI2oKKlqMdW759zaqk7HNtE_1tu0tmDC7Hukk0mA7xq_dV7MJvUkvD-FKIvLN4NNXRBkMsfwG5OCKWZeGskp96x86SiYMqmt2zfcbLyeEImfORMBrCC_icVKmDf5Q4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28681" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qh9EnJFhhR_8MVGqrqkuP5zqI0rdRPrntEvNj7q2S3pak8dymgSxQmb_5OEyMgjxUCtUwy1GTJez6llcHHSkmjaWAGl7bL23IV-fneozBSn-kQ1jdztxp0saAA5vaf_qv2vPf1x1Q--GfI4uYAqKSrsBoPWyaggdFTSMmKPYXqmT2YVmEB3Wy8VdXEAu7J6m1eX6jwElMHurH8oiPE91nBstViUlEWIfwBjVZyC7tqxKx9GAB4M6cycUlnig4bQHX5mApVy0E0k-7lE71bcDL-4PjqAM4n_7qhbdXGYN9scrdHvCR8-aTl22owOB3Q7BedJJGFoByCN7edPpkKxGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28679" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28678" target="_blank">📅 20:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uzsJ1SzPR1QcIzvJHRUHeS9s3EetlGwV838oqL0HE9Jyb1nFnRrCgKUu-CuSlGiObbICIZECZK7Ya_wJxvD0ZxS0KSUhKubvk100JGq30aHioRcvo4U1Y7YYhy7kSkIibi3zDPbLHrNWEs9EooCkGVgfmiSx5HzYU1DDfCv-3YlMDkmUZG3esKw0ar4bsDToz4WjNq-NnhBjd3EU6XOx92_5RladdxUqu9sOERXljkMCkTObIaCMu8ePxX6_KgsII5mVsc5UBsKstGf3nV9GR9KaVpuzBCBYCGm1jyLvZx6obP_pwhrfQUB-_Cm6vpO3lk2w-4WjHiq80h5pKAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر
؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28677" target="_blank">📅 18:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=ge22Sf9gh14J0ltPSfBww2FKM2SGxCxlMM_a8ANvMTX9gG-AOmJDAIsHYS4qWQGr3FbRe5Rf9JK4-ow0rgdfd5vRJI0u9o7AAiejM9-se2TQctypnk6hYiCrTMXaIoTUVRvJuy-UPAVSPMXA2Jj3FZjNJ2XWIyZf5FjAokYsHqTCPBj8CYzU95sZ133gX_-WDeJSdOPUDnGMnVA-2UtlsLWe5rb6nkaCNL1cPEWDAnMUQk_sYF5Vn8odDdyuyzgfPfQ_KH8-SClzMIV-sfg3JrN6Bi9zmbipqH2bEORmoy980vS6VmvOxI2Z53ebNOLWn5IM999buKhoiMMqFihlyEYERASHmNE74Xb0JVOeCzNhisAGxSwUy_hs-DvvTwaBvwfQLVVuJUwknrMISoy87XUgEw5mDBD__qQflvkQTTnVjftWXarfuYhkNkvt_h-I8oYw9-l7vai31Xkm9DU8Jrl7MeDgNYeOnk97CqS8E8TjVRnvM-UhlhOFrcc7cjHRE2Zbs1svjTBbnF2Xzso2Jxu1mdt7vj7JhfUyCNrg2sl1GqLtPKeGqubtax9nN3MOXO3vzz9B628RlUX8Su_luFwhAp1XSEM8xLHluHWeSLjKgyc9It1TdgiVCC6i-_HzaB0_3-qWyQ8RsmddGnHgRdDmMISAt3atAjBOxrYtxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=ge22Sf9gh14J0ltPSfBww2FKM2SGxCxlMM_a8ANvMTX9gG-AOmJDAIsHYS4qWQGr3FbRe5Rf9JK4-ow0rgdfd5vRJI0u9o7AAiejM9-se2TQctypnk6hYiCrTMXaIoTUVRvJuy-UPAVSPMXA2Jj3FZjNJ2XWIyZf5FjAokYsHqTCPBj8CYzU95sZ133gX_-WDeJSdOPUDnGMnVA-2UtlsLWe5rb6nkaCNL1cPEWDAnMUQk_sYF5Vn8odDdyuyzgfPfQ_KH8-SClzMIV-sfg3JrN6Bi9zmbipqH2bEORmoy980vS6VmvOxI2Z53ebNOLWn5IM999buKhoiMMqFihlyEYERASHmNE74Xb0JVOeCzNhisAGxSwUy_hs-DvvTwaBvwfQLVVuJUwknrMISoy87XUgEw5mDBD__qQflvkQTTnVjftWXarfuYhkNkvt_h-I8oYw9-l7vai31Xkm9DU8Jrl7MeDgNYeOnk97CqS8E8TjVRnvM-UhlhOFrcc7cjHRE2Zbs1svjTBbnF2Xzso2Jxu1mdt7vj7JhfUyCNrg2sl1GqLtPKeGqubtax9nN3MOXO3vzz9B628RlUX8Su_luFwhAp1XSEM8xLHluHWeSLjKgyc9It1TdgiVCC6i-_HzaB0_3-qWyQ8RsmddGnHgRdDmMISAt3atAjBOxrYtxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجای‌مانده‌از دیدار روز گذشته فولاد و استقلال؛ دوئل علیرضاکوشکی و رامین رضاییان درکنار زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28676" target="_blank">📅 18:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHlDvNK0UDuqtR6g3Q2c77Y7rtBn43LJcpVb7I1CBIaD1kYSfeTERFUKZHwqTezu0YMc2mN1p4y5TvVhjbp0SnUZEEK0opEmP8JzBnrUPax1iB-fMFujUNH0zQcUFUQxV2ywOJoH0GXkvphdlLjL9stRf1Px4AgzQPzRURYjEMwTF_HtYgCbFxqCCSYToo03NfqfX0nJhpKTFrhlD61UkGETZPk6rRJIP-pMKkvQ89v8o8Plc2Q5YoBXLk5oLpoU8LzbFAW-kn9T81eA3ubKBgswghtSEbomryP6zbB3JN1YzmP1LXdPBlqfMx3Cof-_XlethZcOo8EDouPcYLL4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28675" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=s8tDLlGmNbU47r7rbQdMsFubLb5psATFqTaIDHlbln7BgrKfUFJILasLNFgp-r5u3xqrMsQGs8ehyu_cf05-hcFRZYDVhNvEbN2rFgMNiUaIRjc5XQvffLhyatiNlBPOHUZQUQLqydIFdWDsbIzo0Jjd__2pH48Lc_2p2biCUaWWDID9iYgv4_t49oNOocF_1fenoB-aN8-jDEN3rb4hUpVqdkvB3MRk6pNm8XysNay7jiUfKYYmsUOlxcJ1nQSq12_tRZrKDRxhe27igLZHS2lrASzvp8YnTbL7MFQTDy4Fn9IxcfWcC_cvlF70IlvEydgklF_G32HEIet0KDFbXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=s8tDLlGmNbU47r7rbQdMsFubLb5psATFqTaIDHlbln7BgrKfUFJILasLNFgp-r5u3xqrMsQGs8ehyu_cf05-hcFRZYDVhNvEbN2rFgMNiUaIRjc5XQvffLhyatiNlBPOHUZQUQLqydIFdWDsbIzo0Jjd__2pH48Lc_2p2biCUaWWDID9iYgv4_t49oNOocF_1fenoB-aN8-jDEN3rb4hUpVqdkvB3MRk6pNm8XysNay7jiUfKYYmsUOlxcJ1nQSq12_tRZrKDRxhe27igLZHS2lrASzvp8YnTbL7MFQTDy4Fn9IxcfWcC_cvlF70IlvEydgklF_G32HEIet0KDFbXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
صحبت‌‌های‌خوزه‌مورینیو سرمربی جدید تیم رئال مادرید درخصوص جایزه ارزشمند توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28674" target="_blank">📅 17:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EId_Ora1dok7c19bGM-C0uWhwp6t2RJXEKOw10rhl7I_V0YaTdamUXL96sUuiZVHKDdVJ3M8sAYUDib4PHfwTE90DqPDT3qG1OgaJoZzCnltrD0ElDOhPkX5gC226PbXvR2q38FiA5z2PnSz-D7zVY9gOSr4payRnWoh3O7HwCmfML5bdbB3ZtycNy8tc5Ede4yVHeYkzgY9O6f_iI0D9ffHaQHHbKrPzKSoowX4E6SNGaBUrNiQmPKdOSW8voVKHD7RDTBDlKp0luEeTed0uOsgJFC36p4k9AbB9QLhNSnzGAWsxQV-QixPxt0rlBRYfd03r3pN2vFNMpMY0YovFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به احتمال فراوان تیم پرسپولیس در بازی مهم امشب مقابل  ملوان با این ترکیب به میدان خواهد رفت،ستاره ازبک دور از ترکیب فیکس سرخ ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28673" target="_blank">📅 16:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28672">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=Wsn2_bnuEJl8sg2i4EV9x9BqVPiN6JNL-fSYxaWJuz8v3Wp2LVII9wJ3K_rX_q9xq_kfdEd918e8wZaSDLT_lxs2TwRZkAJQn-_gkOrw9sZfMaWpLRfu5WvPf2e3HhkChvIJYgWCmKfkX2Yh216yBSpfghKYqn-qrM9yp-OrELnGg5c9mT-GikkduxktMHw8hcw-O80TQ39zeSdWn1i_FNZPbWXKOQ_IeCANM9guAum1ppsagUdd4KDrWEVIVYtbhrqgoTS2Rmvx5fKF3ffwI-9NVVsQJa3AVj4DkIZgEVN870LepfwCZpe--OIiBNqS3z12knuNEKTF4zGDRLJPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=Wsn2_bnuEJl8sg2i4EV9x9BqVPiN6JNL-fSYxaWJuz8v3Wp2LVII9wJ3K_rX_q9xq_kfdEd918e8wZaSDLT_lxs2TwRZkAJQn-_gkOrw9sZfMaWpLRfu5WvPf2e3HhkChvIJYgWCmKfkX2Yh216yBSpfghKYqn-qrM9yp-OrELnGg5c9mT-GikkduxktMHw8hcw-O80TQ39zeSdWn1i_FNZPbWXKOQ_IeCANM9guAum1ppsagUdd4KDrWEVIVYtbhrqgoTS2Rmvx5fKF3ffwI-9NVVsQJa3AVj4DkIZgEVN870LepfwCZpe--OIiBNqS3z12knuNEKTF4zGDRLJPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇵🇹
باشگاه گالاتاسرای با پیشنهادی 50 میلیون یورویی درآستانه به‌خدمت‌گرفتن رافائل لیائو ستاره پرتغالی‌آث‌میلانه. لیائو ازمنچستریونایتد و الهلال نیز آفر مالی بالایی دریافت کرده بود اما به طرز عجیبی تصمیم گرفت راهی سوپرلیگ ترکیه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28672" target="_blank">📅 16:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28671">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq-zt1RVJGBiy9M8N_VNfWEUfYTkpVqySqVrKrBs9MRYb1hBeLT-tCF9CXrUZsDv4UXXcuoCJnT1lzVnBNdJ3kGnMX7BEXfdjzHCizL-GjEWKnMVFszlTK5Y7tpRkZ-QGXoUQg4VBlBdlaDYd6IMscCUA92Dui1T2-E_VdAvNr1snvjfRflMejbleYT8Mt9HF92CFHfQFbe28kkdJ9QmTFS5lIy8pBczIKFKmCqkgis0m6CPRE5B3m7Z1kw3SE7YXNJ8IkET8edWReW-Qf1pBLFBAksYB6vXjSHw7QPwgSBB8N9EQAATJSm0P3GSWQs9WIo822rMVSDu5KyUThVRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28671" target="_blank">📅 15:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28670">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e418389c.mp4?token=QeCv3OOua9RLshwJ4qZqy6No7b4LMdBntECrd_-vJa3hZbwcJvjq2kqijtebEHosN6QE_i-Wmptvlw0ndMGd6y2MDOSSlIc2ekbXm7yqrnd6rUiS5rybtK_Bi61MiRiDEaVJCMEALjvZwpicQvsaDu0RVX4Nue0YNnf2W5NU3nRepF3mUKhErclfKTZJt07uD2UzpRUHOe-k6BRs19ID5zF4fDKgs8Zb5WT_jpzGLA-dzaMIKAXxXUNgd7ZRilkyZy6_52McVpz-MP9a4_3vdnfNd9ikMeRHgYJW4KaGQr8xU7HPdG-zyvhg1skZ3Yb2XCeVjjNS0p3P0pK4k5uTHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e418389c.mp4?token=QeCv3OOua9RLshwJ4qZqy6No7b4LMdBntECrd_-vJa3hZbwcJvjq2kqijtebEHosN6QE_i-Wmptvlw0ndMGd6y2MDOSSlIc2ekbXm7yqrnd6rUiS5rybtK_Bi61MiRiDEaVJCMEALjvZwpicQvsaDu0RVX4Nue0YNnf2W5NU3nRepF3mUKhErclfKTZJt07uD2UzpRUHOe-k6BRs19ID5zF4fDKgs8Zb5WT_jpzGLA-dzaMIKAXxXUNgd7ZRilkyZy6_52McVpz-MP9a4_3vdnfNd9ikMeRHgYJW4KaGQr8xU7HPdG-zyvhg1skZ3Yb2XCeVjjNS0p3P0pK4k5uTHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالدو بعداینکه‌دیشب‌گل978دوران حرفه ایش رو زد یادش رفت خوشحالی گل معروفش رو انجام بده که مانه میاد یادش میندازه اونم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28670" target="_blank">📅 14:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28668">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqzjjsHhnnCzsstLwpRTVAMdRe5g2n7CA0g9bwOQ9lHzPBr7s5Y4VR1Tb5Dl__fzWFsqmVmNsKy8sJIHLYNOJqfzWrCiVD-CHE7kRhWSW3K7Pixsgx4P8_WaPFhUel-FF_G8uMUdimHRLI_deK8cE5NkRQkpo8JwmKynjJyblNjpXM1LrUp8f7oGw_sFZJWqXpIgbV_fJaIdnrREPsmg4k3Sl3FhUG_29zcChV2bE4de9UohpNSzZoyDL6JCk8rzf_SAEK-BtMohkS10mZlEjbUCjzeSsXZ8DMXTyb_Qnrdyjygs_2ll66osLWHlJRI_aEmoXTBzD-v8DtEsVRIvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCsQ8MHwbJrTt7XP1wLl59QAXOnRHL0NAm2Swc0Ggx5gO7jJb1uw9G_L24Mp2FnCSLp2iAKfCgxtI36S-hBMb6ujzJuRyT8bAPasrIaBlSh24JTOmHX8gDQKy2KT-WVsWyfTgopTQL91RWMF9TRUVwnXiJ7uvr2KlHmKnlI4kMHFRFlT_LkOkd1I2N9-ANPW7y-FbqusG08YRLoadE8QqodF9aMDZQONPA0nuHSgKfsu7F7dtcdnTd0RDGOE2OYVafwAw8ZY-Gw3ZKVsJxnyBRVNb5zZ1qnctiQMilmCNcHrHfWrom90DQabDf9_WuJefb4dIPJCigpwo4RAtYHnqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب دو تیم فولاد و استقلال درهفته چهارم لیگ برتر؛ بازی در حالی بدون گل به پایان رسید که آبی ها امید گل 1.4 ثبت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28668" target="_blank">📅 14:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28667">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evpvrIKjbzyLCHI-IwIMBU5vgthZeBsxENf3qPUD3MobTPCK0x4A2SdrEDJosclhsflpYaGbRM6x6uj9nITOH2GF8wPI2Zrv4lrG5umuCKNd5FpcNy8Q-qtk5aJ6Rok98oQZUwdHEMaX4mTT9F-vIASAh1-2FgNUpy2-O_r2y1x1QgKiBvvCYEu3QxqzWyjVqaPJICulY3X4XCCMR1Wz6ysMtLqszK-00DnVWQvBGLndqcS6pJRJMEvawN03RqwsgLWxXxT8s2NN6Sq4vlVMLa9iOAlyle6yQuB1uCQNKOA6yx48nsYvlMZ8xyschRL--J0aOwp0apVfEOhn1ia3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28667" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28666">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=L3b8NBNb8IYJWO8lzvXXhKmsUhCZdO3BG_faxyrH8Z8S0Ugu1UczHtpCRRhgf6OyS8YFfZLtyExfamnxO8mvddDLl2uzSrauB22XHFysHzFTb0z07f12072ZmUbPQR3KMai7mwcNeXKklNKs70XImlLPYuhQO1-qte8TVKD0MTdZRhoT-9O1JVoO3xAXgcAqwBSJcDaf7Sc_tBOTFtqx4SI-ybtVSANMpXOP0JIzymlNa7vfkZcOt68wuE7Ii1mWrH47pqwL0slSlDcLmudShkk-To1bbSMlpGHoryezaAqm7Nw4OiXoD9hnmNs62T1ObmktQ7b8fBVtvGdI3cb_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=L3b8NBNb8IYJWO8lzvXXhKmsUhCZdO3BG_faxyrH8Z8S0Ugu1UczHtpCRRhgf6OyS8YFfZLtyExfamnxO8mvddDLl2uzSrauB22XHFysHzFTb0z07f12072ZmUbPQR3KMai7mwcNeXKklNKs70XImlLPYuhQO1-qte8TVKD0MTdZRhoT-9O1JVoO3xAXgcAqwBSJcDaf7Sc_tBOTFtqx4SI-ybtVSANMpXOP0JIzymlNa7vfkZcOt68wuE7Ii1mWrH47pqwL0slSlDcLmudShkk-To1bbSMlpGHoryezaAqm7Nw4OiXoD9hnmNs62T1ObmktQ7b8fBVtvGdI3cb_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28666" target="_blank">📅 13:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28665">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTyK6QmftGFWt1HlbX2KlAszpzS1z7_VSD83NHI-oMCKGRBzjarBPjV4zlw6-h5pKo9IlfQBrWQytQyRtsTF3b09QWaLZRI9Y5cEHMUSI5RjWdXTw3z9-lTy44ZKWjiCB9pIdRXT2nOsjl3LROJrhGN-oduevkDIrnNu6M8j4pg75_1xDGPsZg_VIQ2FBWpks2-OYz2Wjb3bF2UcIrI2tIP6EW3jIh33IoF-jfWVSY0WpMQ5ptB53sKW_p2FgcbS2s_VhZ5ld7_djmhUBe588s7D8BDGLiVicZ_XTmTn72W_ErUuy35y1NuwmllehEbjfnNzPpGOfcyDnaDQuJczlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28665" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28664">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28664" target="_blank">📅 12:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28663">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzVE0vahYMfuPgJqznV8oNFfPI6212gXTI-cZ-aXl2MWq9D08Yk1sZO2fGOaeiCV-18GnvGGexEGeniPunPd7zBsviFRbAYdivJxWmgvljKiz2T4eF_0ygTwGlCeulaW6u4GuIojneGEP49IhahJ7U4nn487bkay66i4cazknWogn5I8ae59v5P_WNsbuKNucClfSuAXpXzH61D5Q4O0-elaCWDdu47mduvBVgGoyuotDfBZDsi3FJ929KfF82dpMcdDb8CbpUKc-0yoOWnIHMz8P7yzkhQXlE5sqJQ_X9OeDCbCtCcc6yw_KqCVWqMqkuL9xcUS9zJJu36zXxbCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28663" target="_blank">📅 12:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28662">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on8X8LPH6b8Ql2frEtEzCP8sgSi-P0mK_--977a4C12TYfQO6F0BbgaKvcJI8UCLtfO8hv_-GIDa2QmjOxUAPVfW0iMa7DfxcPMNk--xhtLhGc6hmcy8-VE_LUGn7xiedu6-bre8XAueAy-0uET4htykhSd3mS2_FjKHlBywyT8Zy6Z6fpiLgTAlm6qflWAfb0V2-ihYhcVycd97beXPcdfaa3ls0QFxYax9-vUsrPCMKKEflU474zSEybiXeqz9wltcXisDbNR3_ERbXxzRxtpIyXmIRD3KCyLliQFmOcl9p3PyBVwjY0Ssg5q71cdRczMnh5JD1S0ItJS2CzxbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ شماره 9 الوصل به مهدی طارمی مهاجم جدیداین‌تیم رسید؛ طبق اخبار دریافتی رسانه پرشیانا مدیریت‌پرسپولیس بعد از اینکه متوجه شدند که طارمی دراروپا نمیمونه قصد داشتن برای جذب او مذاکره کنند که مهدی تارتار اعلام کرده بود که سن او بالاست و فعلا نیازی به…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28662" target="_blank">📅 12:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28661">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cb5xfPC508GcfmWc1_p0fSQ3X6IcPv3yxcDHXjYwqusISzNJWCwQvtH4d_RBmbboTCR-xPesdhS-M1MOsNA9cyS4sKVWGDzFiu7Xv4FqeHkZhdgjFPdu3fd9G7k_OiOxiMQ44dS8jGlBFp3MxW5oSVWYAG-oTTwgDZJEmpFwMf74Zw3haLuldKdYK-p7kEEPTEN_SzDxIO7XwpxeMLkjwt3hXra3by404PZd8dNgiHeuK78HQTJ9d256t1ZMd5URM7mGM4lliLV1yd8g5Qho2DSpgO8G_qsi_2V61mqYlwRw2wxbEGcdh7drxhNZxhRDATIuSXaBhxSY6Cb24Ockjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28661" target="_blank">📅 11:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8Jss75TCVGVWmehUbbd5FB3cHMtQrATzclOrDWVeBcN_baGAPuAgmYR9__AjJ32AJcKuLrpcQJOCQ8ffnvrFz6h5IF_ZiMl9m84APM2J91xRtdeLl6YPlRFtEA3RzOiRqmgoYgBbn8P4Jh_Vst7LPyuUBOTSuktM0N1kPTblxOonHJJNwc8W7nQZJ09fPAP7JoS8Pcp1WJkUTPBQOeyMVsrWgEgrTjKisJUSmEis1DjYaoE1hUR_4b4EOgINo5yPLWPN4yjXMx3pLclm1IZdzYGK6zWjx1Bo5b7PEq-cewqKEr2oEj-oKn9q6EO1a5EbnDX0mKaEXCoodZVnj4w_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهریه دانشگاه آزاد رسما اعلام شد
؛ پزشکی و داروسازی سالانه 137.5 میلیون تومان ناقابل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28660" target="_blank">📅 11:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28658">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHZY5koAsrnqhK7sFJxkpk8R35LN6YkDbyADkfM9GJMR22ZmifugKgWHMJRMBX2PkGNIub7kDGs-HjuShQM6cA6pleLcS9LVZcjzy9LCXt1UEdfLkb54qiWdZgNmqS8YcQ5A0HEyNqEmVczxwsW5mKvUYaTxZa5kYt3eQOC8Hc-h2FzunTOCxsJuOzyjyHCwNQ4dpDO3caRahD2j3smH8J4qzKYn3um3wOPstZ1jqT0G_UE4_mGi30cRFiguLmMOK8AIZo0czGwrAtYTOHpNwuHJvhuPS4yc0v7ibo5ip__1WJYmENfUGWSWiiFzis7IacSiPOWPov9Kp02T65admQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y68_srCpsdV05rg55pffqZ3lDS5wdtPTrUn8cgnZSEPyDGzJn2vJDMY4RvRvNlVX00K4srP4z2bkRT2ytotHDMli0tsUf3NEjoqjuQTmFAdkYmtFpTTa7CTw4VQZAFjKZxWsu--Zp2hD77kwibPUk-DfRwhhwq9Be6Jwg8Xn6cb5IGAHN4tZagQVXTa4ZinGlIaU_gwmnQ8JcPRTN-SpmPU_TOIdo8cf0RACV2mj_HnKNSyEtZsJQi2JEp6B5pd_E4Mcc96l6XwLWtV7Yysy_iFMlNZT52pkv6s5WVzYJNSGmGu32wEgUedy1RxlvBqLBo45Etb2k-m-uLt8vY7fZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28658" target="_blank">📅 11:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28657">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJiKpSUx77amIdtR-o0K8XznjlVRvFVrj6qSLqVUUG7FJ2zpymGeHdZvAM5Uv_vJC4yPusg-A0SbDApuWUqg5F7-_P5Vcyw1kFov2DwM71oVa-Q1kRGTfv85uSIWu4g5TdUET7SM6QEUdN0gKA-5L5C86hItm7bAYmm_pmqzxhWD5yZI8LZJFjH8GLkD-PomRafZDt_kVpjCrntGd_mVxRQWI_Bo1Qk6Dwu1TpmDJjkeq7zoxxlPNCsDXumO5wtVTEzXzfNV5IPbGkxHbQ6QINvsJtcTktDHzC-XGrFIrfHE5B44kSEZpqXyHeNlcg02lSWcvzt6X_RKk7wp8fu41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه گل گهر بابت استفاده باشگاه سپاهان از کسری‌طاهری خریدجدید‌طلایی پوشان شکایت کرد. باشگاه سپاهان هم میگه ما از فیفا استعلام داریم و فیفا گفته که کسری هیچ مشکلی برای بازی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28657" target="_blank">📅 10:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28656">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=iuGHjnGcRT7LEO3TLjT7k3pjIc7CW_cOg0n1wzH3dW17oZIdri0zSso_zUdA3BpKp2khm7xf3bbPewg3ux5vx8xuK5VqX0VvcY_PquKG5dnhfyKju2HnigdCV-J8mFHpUnEcCOEhfaV2zq-9LPGI1z9m77YGcrjAt8vC8RNzj-zPzANgocNP3U48AXXkkz29_ZYGI5vUkrZY6OpGyuGYzonQWnKXbYGUokIabmRmsmdnfKedNfezmpy4CsWmuFXMtvqB2dcdCO0CXu0CqFCAVClW2Lucfkq-5V4NQ3h5mSSthO9oGF-MAfYrj9mAj9se1BHDu0yvz2r3OHZvtWQP5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=iuGHjnGcRT7LEO3TLjT7k3pjIc7CW_cOg0n1wzH3dW17oZIdri0zSso_zUdA3BpKp2khm7xf3bbPewg3ux5vx8xuK5VqX0VvcY_PquKG5dnhfyKju2HnigdCV-J8mFHpUnEcCOEhfaV2zq-9LPGI1z9m77YGcrjAt8vC8RNzj-zPzANgocNP3U48AXXkkz29_ZYGI5vUkrZY6OpGyuGYzonQWnKXbYGUokIabmRmsmdnfKedNfezmpy4CsWmuFXMtvqB2dcdCO0CXu0CqFCAVClW2Lucfkq-5V4NQ3h5mSSthO9oGF-MAfYrj9mAj9se1BHDu0yvz2r3OHZvtWQP5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوپرسیوهای‌دیدنی‌حامدلک‌دربازی‌با استقلال؛
تقدیر رامین‌رضاییان از حامدلک در رختکن بعد بازی بااستقلال: حامد نمیبود این‌بازی رو 3-0 میباختیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28656" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28655">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=cLG1Sa_449Lz5yWZDTWTJeYGrnjgW_9AWTC6p4kL5upltrKzV_hnpV8hyNhdgLReXvPvbo3GXLYADvjbUxCtZjFVlvlWqEUnhws_l7f7pMY8RZoNA7jDN_zT92i_wkKcwgxRFnm77gtOE-vkVfjVASDBxbGAzdQz_byGoHOlRYKOyYzI8ct1GY2_V9I1G4tRMAG-IxtaL9V39-nGchGQZHno9p5maaBBgqbTLqgua6xz_NBQSzBuj6GGhw0VhciCfsBNWhoPsyUmkNfihL-qurCvmiBqsFWGAdmYxoDv5vdMKhqA_EJByqTC6o0RfDtoXJCadq_ZtQ871UFMIwiL9Q9jIh6CEi72CXaIwpdEf-sIwUDHoXgkezWxHw3b_2MBUIDnUyb8VhrAFXnYMewgwxaTAJ_YcJYtMACtvjJHGnnNI_wkXpmv7hD8av93QHbHh5YA8ycnQioly7Q9WdXAtQLXTAzKkvdE-hp7aarHddnldNi3nySpxa-DyuGeA7SBqed22TqjVUI0KNIOAiDsX7usgupeD3lsmB_JIqBL60rTeC-dtKwnDkzDIGmVBcHDHG43jqb2YYL2qZmN8x4d5hs1nb9yNy5SglM5zJajFhAd0-xeNblLPG6KDrUyW0De406wV_CBNvhl6DwiJl8iXOX28BxzlCplcjpHk4MHLcY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=cLG1Sa_449Lz5yWZDTWTJeYGrnjgW_9AWTC6p4kL5upltrKzV_hnpV8hyNhdgLReXvPvbo3GXLYADvjbUxCtZjFVlvlWqEUnhws_l7f7pMY8RZoNA7jDN_zT92i_wkKcwgxRFnm77gtOE-vkVfjVASDBxbGAzdQz_byGoHOlRYKOyYzI8ct1GY2_V9I1G4tRMAG-IxtaL9V39-nGchGQZHno9p5maaBBgqbTLqgua6xz_NBQSzBuj6GGhw0VhciCfsBNWhoPsyUmkNfihL-qurCvmiBqsFWGAdmYxoDv5vdMKhqA_EJByqTC6o0RfDtoXJCadq_ZtQ871UFMIwiL9Q9jIh6CEi72CXaIwpdEf-sIwUDHoXgkezWxHw3b_2MBUIDnUyb8VhrAFXnYMewgwxaTAJ_YcJYtMACtvjJHGnnNI_wkXpmv7hD8av93QHbHh5YA8ycnQioly7Q9WdXAtQLXTAzKkvdE-hp7aarHddnldNi3nySpxa-DyuGeA7SBqed22TqjVUI0KNIOAiDsX7usgupeD3lsmB_JIqBL60rTeC-dtKwnDkzDIGmVBcHDHG43jqb2YYL2qZmN8x4d5hs1nb9yNy5SglM5zJajFhAd0-xeNblLPG6KDrUyW0De406wV_CBNvhl6DwiJl8iXOX28BxzlCplcjpHk4MHLcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس‌رونالدو با۱۰۴گل در ۱۱۰ بازی به بهترین گلزن تاریخ‌النصردرلیگ‌حرفه‌ای عربستان تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28655" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=gxfqgCwZN68igmMQVpxw_sZ4vd4eVTmDYCYBtDQvuqxoLllf2PmIvA5rQTU2h6P_o_Ruy0DPabWTvtk_GrzoiV9Cf3Hfvx3bVJgcKu75zGui18438Sn3LEq4paNoiJ7tcwNl-WrEVlX_7ng5dGuDGhB4ndxE04SXtR5H0urmrEDQ1K6KKBrTUy7UXOHbmbUQAxFB4ZAcQNT7Bf4SKCEuA0MIsWBkYG2vsPmup7w2je75XfGz4S_-6k5vpwKNS8uqyNGUf63GHdIXVt0vC1hDr1OiEbGtQ9d2JZob1RjbahhsIQ5axH6RNvv3fCMnEAsqwn82CfVjww4purnHCa5UgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=gxfqgCwZN68igmMQVpxw_sZ4vd4eVTmDYCYBtDQvuqxoLllf2PmIvA5rQTU2h6P_o_Ruy0DPabWTvtk_GrzoiV9Cf3Hfvx3bVJgcKu75zGui18438Sn3LEq4paNoiJ7tcwNl-WrEVlX_7ng5dGuDGhB4ndxE04SXtR5H0urmrEDQ1K6KKBrTUy7UXOHbmbUQAxFB4ZAcQNT7Bf4SKCEuA0MIsWBkYG2vsPmup7w2je75XfGz4S_-6k5vpwKNS8uqyNGUf63GHdIXVt0vC1hDr1OiEbGtQ9d2JZob1RjbahhsIQ5axH6RNvv3fCMnEAsqwn82CfVjww4purnHCa5UgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇵🇹
سوپرگل تماشایی روبن توس ستاره پرتغالی الهلال در بازی این هفته این تیم در لیگ عربستان؛ نوس این گل رو تقدیم دیگو زوتا فقید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28653" target="_blank">📅 10:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28652">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giPyFsSDaAL_PmK3g6_pTFGb5rTMTPqTgERppz2CQ0bQ2VFyhu1eLCN3MrHNVlQfpqlj1PVYZobLYzCThAK1ji4cbqBImKhdL7LzDmHROLBS-UnctDHyY-LL-Zy-RE_defoYM7zbcJQEpr7uTrQEo6ahEUKjsgDB7tDzu_hLStYO7JgB6UecK3gFLl8ebVQwclUooXCCdUqLVtYIRn8u17UJ0UEUPaJ-T8FymjjeWX-HCVvLEcoDPVOo4TnO8_fbfdG1r8zEOkD2NugfgLOFKLbI2ikuO3Eyx9-BJ1GPqoasbGjEmbOOsIjXoSpd8cSYh4sxrIM5Y3Es_XoMSajoFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ دشت یک امتیازی شاگردان سهراب بختیاری‌زاده در گرمای شدید اهواز؛ آبی‌ها بی تلفات به استقبال شهرآورد پایتخت رفتند.
🟠
فولاد خوزستان
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28652" target="_blank">📅 09:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=fi2hgSBhsG3J-hjyZmM9aSQYZUy3Pbs2_RCd_xeWSY1iKGDfm1hP6t3HGrsMLFQCJnQrTNdP4wm5DjqOXNQJUDyWUT6-nvcyskP5zWoblXHyVfRz4BueIaTpCoCqugInnkCPWploKIzGznhEI-z5kmK7ij6aqeyWBKy-f4DxWnxQkuxYqDHB7Rclac8sl-r0S_ByIAkRVP2gV9LX4sYaCfXBalvdUM_McyRGx9dtCGdITWtRgFBHEC3z5YcR4MHm58TukWCLDu7xXB3Dw2PrLIF7ZTiucTkFS1dbPugZcL4r33F195u55kHiTfLEbP_JlogggrIbUew-hugHVoZmSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=fi2hgSBhsG3J-hjyZmM9aSQYZUy3Pbs2_RCd_xeWSY1iKGDfm1hP6t3HGrsMLFQCJnQrTNdP4wm5DjqOXNQJUDyWUT6-nvcyskP5zWoblXHyVfRz4BueIaTpCoCqugInnkCPWploKIzGznhEI-z5kmK7ij6aqeyWBKy-f4DxWnxQkuxYqDHB7Rclac8sl-r0S_ByIAkRVP2gV9LX4sYaCfXBalvdUM_McyRGx9dtCGdITWtRgFBHEC3z5YcR4MHm58TukWCLDu7xXB3Dw2PrLIF7ZTiucTkFS1dbPugZcL4r33F195u55kHiTfLEbP_JlogggrIbUew-hugHVoZmSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده الولید بن‌طلال‌مالک تیم الهلال در حال دوچرخه‌سواری‌درریاض‌درکنارجوانان‌عربستانی. او با بیش از ۱۹۰ میلیون یورو سه خرید بزرگ برای الهلال انجام داد. سامرویل؛ ۶۴ میلیون یورو؛ واتکینز؛ ۵۸ میلیون یورو؛ مارتینلی؛ ۶۰/۶۵ میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28651" target="_blank">📅 09:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvja7i64QDDWjpgJvVStA9PAosEMTAGGEl1iFBCBVwrXdWJfK8EL05dwoGAFXkUh0KQtWpkMhAja19PiZje_n6CwiDBAMziDwlcTEa1vdJMQjksiQgvofwCYBk9r6jOa-bDMMqAHwSH0poNDe7llWVRnh2cwHnaUuQuVahah8n_UneCX9oI0xhrR8Lt8gBDwouQw0-7K8-GpeFcgvF1gbx3CZMdQeGqx6_myT6ptB7RbNFdMjEWNsxkwTKc9SvdrKWvt5oXfQrzjYLBFimvnc2QVuwmUo5oy9WDxSlr7z_MMcy1ETT87_u5YvArjQ65FqjZagQ-a1DB072nHz3CBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تارتار گفته به اورونوف بازی ندادم چون دیر به تمرینات اضافه شده درحالی‌ایری و محبی هم دیر به تمرینات اضافه شدن اما فیکس بازی کردند. واقعیت اینه تارتار هیییچ اعتقادی به اورونوف نداره و داره کاری میکنه اورونوف خودش فرار کنه بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28650" target="_blank">📅 09:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=U8acaixhd0Rg89RFHemog87Hyd3tUcCUtg959D09x-yueEAPiCVNPBkg0BEkuue-DTUrC95deBrFS-IG2BJ2_n7SyF7aceh0uFylZI_cvVERzQaAJn-8VllDFsx9iWX2vSNYImL3MRFEJt66T_McUjhmpUyaMMF9_AXFJPyZJlYc8C3CvQZAsoruKtrIuYTUvJwT6rl9TGrrUCc7VdNYwp2X0xdE4aDxR7mAvU-VqvxQLag8ftItyYAkTMLE_b0Msa1MACtYcAsMtP401Ytnn-_7rVF_XuF4kDkkjoS9t1N2CcDmYTUQF1SAakJtihQ0Z-nraUklvga---NEqspeDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=U8acaixhd0Rg89RFHemog87Hyd3tUcCUtg959D09x-yueEAPiCVNPBkg0BEkuue-DTUrC95deBrFS-IG2BJ2_n7SyF7aceh0uFylZI_cvVERzQaAJn-8VllDFsx9iWX2vSNYImL3MRFEJt66T_McUjhmpUyaMMF9_AXFJPyZJlYc8C3CvQZAsoruKtrIuYTUvJwT6rl9TGrrUCc7VdNYwp2X0xdE4aDxR7mAvU-VqvxQLag8ftItyYAkTMLE_b0Msa1MACtYcAsMtP401Ytnn-_7rVF_XuF4kDkkjoS9t1N2CcDmYTUQF1SAakJtihQ0Z-nraUklvga---NEqspeDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجامانده از دیدار شب‌گذشته فولاد
🆚
استقلال؛ برخورد سرد رامین با یاسر آسانی و صالح حردانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28649" target="_blank">📅 09:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZCYaLXw0_VoZZue91u0y6bvpIJ6cC8qVtjpGhLyILdS0vAZaiLTx2AjouWAR0Ya1ofFM4mfAFi7i1ltVRB_72Ttcvmhq5tXp4TGaw-nrK-CuipuG7wdX5T4JqLly64FGZ_1kmicMaytljes_0nf-yTdh5p6KoRAWJ7Wg2EtuhsDGfUw6sGjDMJYfsKV7zTvrir7qafywSIqy9XQUt4QOg-NqKOG9Ip83k3qXUZACiZeRxiE-6igY7dg235oaOGXEIb0jZDoOwD66CVNmm1BXKruVGEUEGcfZqJ4OySG8_Ywy-srwL6Gi96GQCaemX8ifGvJIcbqaS83BrvEobVosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28648" target="_blank">📅 01:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28646">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT4-PYCL77_exBmhhujx3ZMAtqTiTgVLfUROnh8JgUBIDoQ3EKf-zeBnnACfqGCXgZc-MpU4vcPBV0ukWZ4DW4GJg6eUruNz9vJseoMW0eRGC8FrWNnxCz4SzlPSrJTcX46C_VCtRo_RJRVlrnzSuYTMXJEH-K8ZRufB-ef59GmnVxqnLW7l5UmdOP4iZ2W_4GweTFfEqvN7485F_0T4-x5tvoky-2_a2YOB8W7_FheD1w_M5sKovCrlzrrALUEK_QbNUWKqa6Nw93HJVPbW5nEPYtZMKfMVrJ3Mbf0j1rvZyU4INAI9gFnSPgWaXN6MWlindC09foEeAS_HQRZeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌‌‌ امروز؛
مصاف پرسپولیس برابر انزلی‌چی‌ها و دوئل تاتنهام با شاگردان ماتیاس یایسله
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28646" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28645">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNW2fjoodZMIKDQaaqjfnNIlzTin9tBfTWSDF-cR2yy-TTi262iC_SHPIlsA4HgsFs0v59a7jJJAJVresJnuZHkOEUE_8neIVTA_sBtX67Bgtw9od1q-i-O4-dRv5rc9Gtlo9Qpf6EKFjymqGXyAM9FUnKCLmKXSHKZAgBHFghlrBFZOEv2veVoaV5EqKKJ0DYDCpBMWteIKjpMmmAP_GtwaCC6IOM7M4Wm001ahJ5YxJ_t-jiuLWLdwfp_VVAYuV7opMyDFNxESg0L0zkppiWCx7pZX-44u_Zt_Dkkx2VCnmvfiaQh_qwkLMK07YuQ7JPEVC96a8zH-5ck1VkImtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
ازتساوی‌بدون‌گل استقلال و فولاد تا برد پرگل‌بایرن‌مونیخ و من‌سیتی مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28645" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28644">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EORjeolOlSguaESEW2-6s6KowAQ2c8x4YMauXxs2a9Fpjp1nUTImd9LKT-7EZH3XLSV4UIHa3Of4xmhkDrYuuT_tCMMz4Kzelpd-Sef3tvYH6MwLYcBvS06Q0wuQUMya_bsvtxd4FrCFTZrjnBe3IIbr23LYDa1aUn43qEcJDXPIxVHyxDNU9spT-fiAaQbf2H-RYkGKLdd9YJKBbjYNdJsBDGCGZn7-r8HOFXxEfUdPFJkzDG7SCHuNJEFwlSF2QsnFITnQ1hZq6MSBFm5ZLH4tD5rhkIlOLnmF82fBof7OMoHGFmhw1YVAijp8x4UzHLFlVJZp1SnttDb46MjWTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28644" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28642">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJO_980BfloZm2RCUk3IQB_gECiOQaOAO5HZha26mbAvsRns2Mc7nnyPtrA2TJupCFd0sjZmGR3ttD-TFWK-5BFORsEVeNP2afC-tSY7wmrbGALXGzBLwVZSiSMJldU2nSYHHy9eJQM8HUO-umRBtF5Gsh2ymcf201zJiw72qQd85mRtREofDLI8B80ziNBjAnnwcpnt-L2VKTKFeCU9ueaV_Pr8FxIPOCHa_rOjCuB6nkTIOpUXsiubJRTwKmzQ6-Xoc3SRTJB4vogeexuQXf1EieraKd2OtKmb3tKhe4kT6Z8IXFxnUiFY0hUagsOxml-YyYRL5q5ymwMGEK8d2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6-gkF20n9r4G9ILgEWP7AnG4hY5ans0U8te9mzGUAOl8f0jkOTfXCJ7o94m-O4gI6umMkqqtDfit2hD7T58jR-X2sR5Yn4kVn6fDlVGTtZ_9z0NswsoZCAUlDpOxZAenc6bZ9vmyNFQBTKwwnxnB5i64sMo0KXZFuvnwKj06I4Jx-n7wCB8t11MgvqaqDOtd1Vtyhqi6Wg3jI9m8aH5_Ty9Lvs53v91I6YgvP_a-hSxTGrgY6JHVfXAuU-YOMswHMwoXoY5KT_m8lgOxBPBFnjG-cbnarSWseDYwyfg1y7LMWiyjbKNsT3a3ri6eL9F-1Oxht-KVLPZe9-BexWHzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ دشت یک امتیازی شاگردان سهراب بختیاری‌زاده در گرمای شدید اهواز؛ آبی‌ها بی تلفات به استقبال شهرآورد پایتخت رفتند.
🟠
فولاد خوزستان
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28642" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28641">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISpmRaq9gw11x5ugynxAzMrc9zoLOlXHXwQ9nC9onwSPPT5LtoAntJjkK5Sgu218XRaTrWPgf0IOKpScrkEJ6WdvEQhLZsA1IKQy8vZiC_455qbhTKwNUwyml77VKIKcH3xH0tOhOb9QFbUHU22Hrv0UXwu7pQpFiNj_upRbvoUbwJsoosw1PtQHol_wPc0X11DsW1D6w1Rc065R_-RvgbJeNCAhgKAH2Qq-LcioaB7Ug006WH9x_jwlskY-teksd8IyEdV35FINpm2fP1ErI19nJq-YZO6EdjXb77qQVlkg8zs4OrzJD5dNVk1YBIH7IvgYQ7mYKHA0HdIC4-t5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول دیدار امشب‌دوتیم‌استقلال
🆚
فولاد خوزستان در هفته چهارم رقابت های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28641" target="_blank">📅 23:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28640">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffc6c7296.mp4?token=AG6UAsk7x66jyNs4b06rec4Pdp5xtB-MjFDl5vXP_xLYGz7quJNAVeYvoL8WChZj_tdfokA_SPGWIH6dpp9pwCfyQeabk-fHWVV1X0PZ7enr2UCHC98YZkHxTv-QlQICCV6-zLGutQQG2SeVM6V5tT3XwZdP2KUGi6ATci73P_fq2RkVIgKWLLZ89THdwhgvOwo7hDbu38GAGAiBPU6tiZ1cdt3FiMmoROC5QQsDGbTzLPw9qWXs7h5sort9Ylj47WZ0QGR_uw_Ey3wvKX0YxfCCzANAVsQHgpPdY5I7jAK2bV_CZOK7B81JZKCK8TA4JBSDY6igyLH1hZWLFvAFeFBv-CIYQFusIkm4DuLnuxOLjRYDzb-AzQN96VrRZHJKP5wYOPOtE6zyz1DfLWHGrH6NKSFMgNT8IvM5TaXCgHOW3wrFleH0jjvlb3loCk3JnMTXPfWmi2uhrxm11glI5vsvIlJ_c07vaPdmmkhC1qF7haofuAAXGAptcvAU1ZxUxSbqkoctTHayXLH8PHZFYkRRy_H_0trlJcBdIamQ2AUBOYcIY6-EUPKHQ8tWosJvJVNZMDrpA7Sbf32uCTZrO4E9FKOlAE1mqQyga3dA3uZL8i15M14imNQeqzco6Q6TjjMgVXX8lt7SRkwhS2YjoyFdaKNj6Mw2N7LDWA67u4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffc6c7296.mp4?token=AG6UAsk7x66jyNs4b06rec4Pdp5xtB-MjFDl5vXP_xLYGz7quJNAVeYvoL8WChZj_tdfokA_SPGWIH6dpp9pwCfyQeabk-fHWVV1X0PZ7enr2UCHC98YZkHxTv-QlQICCV6-zLGutQQG2SeVM6V5tT3XwZdP2KUGi6ATci73P_fq2RkVIgKWLLZ89THdwhgvOwo7hDbu38GAGAiBPU6tiZ1cdt3FiMmoROC5QQsDGbTzLPw9qWXs7h5sort9Ylj47WZ0QGR_uw_Ey3wvKX0YxfCCzANAVsQHgpPdY5I7jAK2bV_CZOK7B81JZKCK8TA4JBSDY6igyLH1hZWLFvAFeFBv-CIYQFusIkm4DuLnuxOLjRYDzb-AzQN96VrRZHJKP5wYOPOtE6zyz1DfLWHGrH6NKSFMgNT8IvM5TaXCgHOW3wrFleH0jjvlb3loCk3JnMTXPfWmi2uhrxm11glI5vsvIlJ_c07vaPdmmkhC1qF7haofuAAXGAptcvAU1ZxUxSbqkoctTHayXLH8PHZFYkRRy_H_0trlJcBdIamQ2AUBOYcIY6-EUPKHQ8tWosJvJVNZMDrpA7Sbf32uCTZrO4E9FKOlAE1mqQyga3dA3uZL8i15M14imNQeqzco6Q6TjjMgVXX8lt7SRkwhS2YjoyFdaKNj6Mw2N7LDWA67u4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلزنی رونالدو در بازی امشب النصر با التعاون؛
این 978امین‌گل CR7 در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28640" target="_blank">📅 22:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28639">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feNn8qadvYTcWTCsMUUPrHrDsfql_kASI07T0zvjqUSHDk7Ml5qSqUS0xj0l8Mm0ZhirZP_JjvuIaXLv8rHSZSfbUTw_s6hBAp3lUA95TvJTvt7dzNriFW4gQ-k8-HUSdomkTUEf78cqLx-rqaeHD2MddllK69C3lk18H-aR_48MDzTTO_nUdNWHPQJAk91IRlQvHM-GeypGlT76e6FRAUcuansTNfS5pa_uIaNbNZKP4EoPlvqAqS8tG0fgUdWbxnDg1Q7ZDvFcSB4r68zoMPN78WP3NIZ72YBfZeL4T1cTbmEnx8Val8rovSQw6Q48en3_FYb9QPup-gnQ7amorg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شماتیک‌ترکیب‌استقلال برای دیدار حساس امشب مقابل فولاد خوزستان؛ ساعت 21:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28639" target="_blank">📅 21:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28637">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du2W8te4PsVzjxUpiWDmjCOsKpjqtPgbAoLFC1rxnfgsnhYAIHWR7I9amSIbZ5GS_tdxg2hLfGutqTVicnva3w8ZzlAC2AmhG-z1Z1YQ5yPqPFWhAUFLwqJ_d4PI_Altg_E223Vd3tOdFfgY6NTSQyYj7Jc9qtunzA7m7YM4q2X-GYuA5yTVECIVOL5q4arZvniaGLvuXqqois_gfOituh-o5ZzhZINfivXPnF9ZmOJ0RuVVtFpT21TI1j-Is4PjvGJ3R1v8dVVRYISIzjSgGmvBMpS6JQvCQHdZfJqiD19iGngdKD8nvsKanR1NpbprHcG9Jp4R1In8dxYtBaFA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28637" target="_blank">📅 21:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28636">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17182aab77.mp4?token=v1uJD9abdO9Eq0I1A_rPx6nqaV9si-n0r-HR0Ji4LlK_GpcrkcNW51aJ9YGYhe_QSV7TODBUvo_c0WXau4cyb0rQ_pypFuhWmzLlIOCLoN91kmkwGHFh8DcErta4UALPOBx07OfpN0_-lo39oE11TBYCMEP8noC4i_r5xZ7g82nRMJM1b8nfM-38k0EinzYjzGqe3_2PGjdDh915acxTiBKEuZSnT4dnCbDkonLp1UUiC_bDcPVAOBN7DYv3cjOms04kJ9X_Jk3Uvs5s_zOIyGhIrzlSn7-Gko75i9P-KnnVNFvY5Nisz3LmPEWoKWBhFPXMDgffY-b9Q_4W6Q4iiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17182aab77.mp4?token=v1uJD9abdO9Eq0I1A_rPx6nqaV9si-n0r-HR0Ji4LlK_GpcrkcNW51aJ9YGYhe_QSV7TODBUvo_c0WXau4cyb0rQ_pypFuhWmzLlIOCLoN91kmkwGHFh8DcErta4UALPOBx07OfpN0_-lo39oE11TBYCMEP8noC4i_r5xZ7g82nRMJM1b8nfM-38k0EinzYjzGqe3_2PGjdDh915acxTiBKEuZSnT4dnCbDkonLp1UUiC_bDcPVAOBN7DYv3cjOms04kJ9X_Jk3Uvs5s_zOIyGhIrzlSn7-Gko75i9P-KnnVNFvY5Nisz3LmPEWoKWBhFPXMDgffY-b9Q_4W6Q4iiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛ شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28636" target="_blank">📅 20:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28635">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28930c27fc.mp4?token=n6-AU-4uSClrn3MSRkJ8uwOu8CEOSgJdeATEU7B1wRZtWmEo49mxAkBQ2rvVYLWV0y__y0IunneWn9eRDr_wBRw_ISy5p68_vk-ZlzjToZRKcgiv6PhrKZPvEWWJNn401ZiHYyFfwfipqEATKKYth22DuFIhuXm7HDr9cz8RBxsKMj2yk6-KepQSsROWyetQ_Z0rwrlMNXrdPt6IxopkeDy-xdzygH7Bskh1tGqfZW6ex7CyN09cpp8agDvx--Hj9HeonG_t_hMaHJH0BTaDEE71EYdDM0rtGGNe_HERO0Y3tU_gA5fCnSk7yxr3Mx4gA8yU86r1h6gTZ4x5DqVpxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28930c27fc.mp4?token=n6-AU-4uSClrn3MSRkJ8uwOu8CEOSgJdeATEU7B1wRZtWmEo49mxAkBQ2rvVYLWV0y__y0IunneWn9eRDr_wBRw_ISy5p68_vk-ZlzjToZRKcgiv6PhrKZPvEWWJNn401ZiHYyFfwfipqEATKKYth22DuFIhuXm7HDr9cz8RBxsKMj2yk6-KepQSsROWyetQ_Z0rwrlMNXrdPt6IxopkeDy-xdzygH7Bskh1tGqfZW6ex7CyN09cpp8agDvx--Hj9HeonG_t_hMaHJH0BTaDEE71EYdDM0rtGGNe_HERO0Y3tU_gA5fCnSk7yxr3Mx4gA8yU86r1h6gTZ4x5DqVpxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
ستاره جدید نیومده گلزنی کرد؛ گل اول تیم سپاهان به گل‌گهر توسط کسری طاهری در دقیقه 6
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28635" target="_blank">📅 20:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28634">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bD6fmoGMgOsRpt4HXpup0bQKbvvNnh8yx9l3mw1gKHutxmFidUxhiO0E8ppr5lTWIEyB2qrAdDtEgRXmR4sJNd-XZssb00kPwcwIxXmb_EJ0iscFUgiqEb51vPUgaX0pwDYZcWP-3DZIlVriUlnbi0FJqs3j93UHVENICuiYtPyxDoKX6BpXaXjy6D6ZiTrkb6v6dxhC4rCB0MQHaMl1gMiO2dRwln4avDlkEvxK678_R-IfyxR68zPAqGJqj_8OMFnErAJZGNq84nV4_AY2dUDneImfXrbIe1xUQIwihMRQq7hl3sh3WRMDagkvopIBw8blVXwtxOjmvKyahy0Xlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28634" target="_blank">📅 20:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mM_8PCjfJ_n-aKUxxjwzHQyjdSUlthKP5KnceOhPUT3cSnV9rbVOytC8N33Xysbm8ooj_9XiRLcrls09qjkM8POuM6WY23_Vcx4n8rQiwr0TRrvsvp9ni3gQZtQFy1lAnSLl_InP0Una3PrrhDH772ccLXj8Blqq-RPxXh3eT3wCMUKj6RW2ZzT4TJWiiZVVBef-8AIpknh17QhDK1Bu6xJbiD-hDd-4MGtTEPB93Czj0V9pYLKxHFMelmIZMt4EypgGYKpdK8Vl818N-257hTxVlN5PFB4wA5bkjPJwEU6X7yFjyckfcA40b_w4c1aamB01XsnNYQnSNxdaUa4kMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZDBzYTkoAxyN7ka30kaUhOsvpU479igxjimdhfPbhcr0WAeEpdUkpA9xXs6lHCH8qckzgfA3YZkoqKJjSDCESJh_nsCotajBdRhRn9OOMsuefzrf6Lo0zDKbh34nM0EV3l6echV62F8jP7qpTrMb9J-OmkNvpIAUMHcHjP3W7PTPJfyRQ7pT9dVMBFFPi8igCzoP2EerBKZkTcIyQsYgYMioxEY44BnW-1won13umOGuw9UfFZDS4fytyt6b9LRKuyhvDlXoZFolWsl_ALef6L_xpj9uQcJIJ_yMX0-gmtgTvGVQmkqCj06V2fHlKwWBSKCVgF-sMtrE_i43yK2kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28632" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b6a569c2.mp4?token=b1hYLZRnDUI6m-KdS_hD3M2f1ZDJtrPQ9kQwy8ttIsOXTzI6uE-agh3v7skHlp8QCpmZmX6Ol9rrF83K-OTKr2NvrDHkT6ATvhCU3uvGQSGi8LYlf7ixEX-guHM8uZ8t7udU3YktFlC064j4WGZoMClhStvRj2SBslDwzIyqBGPJj6POZF04jEJnzscqv_JnN4nQquSK1xTfIC8bPMvw4tvrpu_G9A4lGSvSvZyq4KzZYNkw_3ScHQwPw9PsxQB6cUvm2LivO2tiYBXV8-6Hp_lm8RDRHbtxQkElJRKkeMOhyK1zxNJ1zwqJekNJUz7FZrAnBRApsOS68iCPRW_1UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b6a569c2.mp4?token=b1hYLZRnDUI6m-KdS_hD3M2f1ZDJtrPQ9kQwy8ttIsOXTzI6uE-agh3v7skHlp8QCpmZmX6Ol9rrF83K-OTKr2NvrDHkT6ATvhCU3uvGQSGi8LYlf7ixEX-guHM8uZ8t7udU3YktFlC064j4WGZoMClhStvRj2SBslDwzIyqBGPJj6POZF04jEJnzscqv_JnN4nQquSK1xTfIC8bPMvw4tvrpu_G9A4lGSvSvZyq4KzZYNkw_3ScHQwPw9PsxQB6cUvm2LivO2tiYBXV8-6Hp_lm8RDRHbtxQkElJRKkeMOhyK1zxNJ1zwqJekNJUz7FZrAnBRApsOS68iCPRW_1UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28631" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=fNgQ1Muog3RlwHfNiWhyroNZvgggA_C3GRfEsKk_JhqVVkNpV4MlKd4kVUErMWRNv6DhqU1KX6G6GzG4lpqq8O3hIPpXO126UlaVNijbEx87jCYuVMQKw0st-4cNj024kGtcwwZUfsvGpXK-npVJiVyvvJbXYvqikSypzmGEVdw3EuR12zJv1O8VBsd7lSutk108ZFWn1UmSbVuPXvzsEQz97bH2c1c34e65shRcN8eUqv6qnDLS1gD5PGUQcBHLwRxXr_2bJHLQyGj-L2WUoCiFGzGHeKs6D4qMJzVEuwEKkYApfvBJfIEvKE9x6L1TrbfbDzFo7FcwKbmbgpckwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=fNgQ1Muog3RlwHfNiWhyroNZvgggA_C3GRfEsKk_JhqVVkNpV4MlKd4kVUErMWRNv6DhqU1KX6G6GzG4lpqq8O3hIPpXO126UlaVNijbEx87jCYuVMQKw0st-4cNj024kGtcwwZUfsvGpXK-npVJiVyvvJbXYvqikSypzmGEVdw3EuR12zJv1O8VBsd7lSutk108ZFWn1UmSbVuPXvzsEQz97bH2c1c34e65shRcN8eUqv6qnDLS1gD5PGUQcBHLwRxXr_2bJHLQyGj-L2WUoCiFGzGHeKs6D4qMJzVEuwEKkYApfvBJfIEvKE9x6L1TrbfbDzFo7FcwKbmbgpckwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی احمد نوراللهی برای اتحاد کلبا در دیدار امشب مقابل اف سی یونایتد دبی در لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28630" target="_blank">📅 19:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftTbQiClJksF1nWkt7NNBV0DbxlgaT7v9bOl9vQ2SyRTjmw8zP_x3DbM0-pd6fvkaSpneiHtWzHLNFWRP0VPkIHWey1ghs8bR-nVrn0uNHJoM9eemy1dT6jC4H8mBqc_H40q8_c--9pP4vgzeW8B6vxiXg_10C15kVPIhITC7HakN4Ju3ZmTbVr98gN3NPv1w7xCw38R0QZa9tAiXT7rX4fwWGMwzajVyRUDl_PYKdFLCuQeTYtHEyogBsbzRfXc8Cf6lPSr-TACY2cMD-bwxjRWJdemO7E9ildnMNWBO_NKjDNUreq3zITs4f87AKM855J1ZLuxqfyo6UA_BNM0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر
؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28629" target="_blank">📅 18:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28628">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKjnEVwxYaV6hA8g2e5pRkmoyesVD3IDo9s-o4mFGzYu0-lF8Z9uZWrkeerY85CLS2yz3dGBGJH0aHDXgj-enGEQHyBKk7Mh5Ss4qqZgzgFA5JtHdGBkXNDCqkarZlRNHdK9B4IwljcTcnxcRzaABzVv6dTuDgHLhSmZemWMjNrbjTg6O2PTov62h0Gn8mXUvBrIfn_vQc0AoQ4AfssY3P3-yzTGZDtPK0QTFDXBolBNl1wxElCPT0ZhkM0HKq311GajKX6r4hui7Hlza5kEUel8SiGg8kvw2tTvfo5Ef40liCS7DegUfn0vvoFVME8s4obg072nJx91Pd-yAxrJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛
شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28628" target="_blank">📅 18:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28627">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cug5RPA2q257mDL1fBFiV4Va70FK3-hsZMxgg556riDtJFGH_tPOjxrsQErJQuuSLiYEeRCzqfm7D0--RGVCSoU4U3hbg7Ab6gX8fJze9d7r9jCX6iJN8dMl8B_WjmZdJz3GS0tTVfFpzjGXtxk27bQrTabL6-GCNUKDzGu5_yZwuUJhIi87a-xCl1vRFeS8ZiBwhVfmNSOgDBHI7ThflJCPIolDGnkQRJkF2um2ZrYENgoDx4MmwRUz2z_a_Zt0S4m_E0m2q7KI7Tk1kILKtmiB3-fH3QsZ_ZbFhvnVMCut1LHLOnLY7Vsuu7utRB94G4QlEY8zmL5gx06PSKjN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لخ پوزنان لهستان با الهیار صیادمنش و علی قلی‌ زاده در لیگ اروپا مقابل تیم‌های مطرحی مثل لورکوزن، بنفیکا، ساندرلند و کریستال پالاس بازی میکنه. فرصت بزرگ برای الهیار صیادمنش که کریر فوتبالیش رو یه قدم ببره جلوتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28627" target="_blank">📅 17:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28626">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFz0AvGuiCJylXIgWqAv1WlLQ5rzhA4URztt32nqHF7RVG2XOSsfcDnhq5aGsivt1v4FoinpGoBTIlLbGaZa74uWsWKxzsuMJiTEN5KJWur-b7ZLNHPsO1hFeg2ZtwBGmESB8l4UGtsuTsDClSGggNyMKtjaaNLc92J3AiXf9J2SQOUXDUucZ0C0GkF-ktxX9WKNl6GSsIhQY082jPit1whfMGVSWUwqkfPn-77qdOSGBEHLLfJgBvuaOBNAzrmmrWNyf9EsAzE_jFnIsbZqcTO3uixXLlEd3iw1xZIv2QRvmgcQWgBfk82x_KxucrkJn34xvXtxqXyNqjaOG4fiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28626" target="_blank">📅 17:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28625">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwxtVDDJ2uVBu532gaYRXbx_DqQIwaGZpPXO0-5KnfcNOmQr60NSNVnkrXym1XPK4-ZTCmtG7NCbtHw1sAwrGEGXTzJs1uqOE7-605Icef09rP54riF0LE1cZ5Rr7vaZTb6h5LrztO7cTSH_u5wbh1hjis332qJ5ImHND4uC-z-BzYXoWWzMnKe6z17Oku0bDd6cIWUgv95l3LbHStwOVTLVgMaGEWuA-IS75my-6F-lPdKMy92VjbY1tWzxnT-Jiu-gSveFrGLI4vqCr95gW3wh9-WwrnexIuBH_ag-ndfX0T8wV9IS0tgvmBQy4xkbCKs4M_DoYBr-2IW3XX1pZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه SPORT اسپانیا که معتقده که امسال بارسای هانسی فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28625" target="_blank">📅 16:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28624">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO5jNhKP-0bXLPC6Qza9avbIFvXK7NyyY7TtmXE9qqee63EHvaEroPFtbXuKrZK6yOuZFOrsRBFb_k5ig4VHeZACUf3d06C70eXD1HvdsEIYjFx0hfEDXfZSoeSnVwzhLX80K7M0teNnCQSczN35jR752kRcKvRns7VG2UkOZodJZBvXamon7ih5p5H2l3ngNx7hmP-LsWhtO2Ms5y3bkTeI0p58RtwKkc3isTewBpavoMjlR-tfzEcnGRh4fVlLEZZii-mt0sueYVE6-9hHNlKoM-YFfP9x4U4YRd0iYrVUfldyuNb8jWaM0m9g0ddqW2l6nncfO6FJyj_KybNnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28624" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28622">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNNIGL9i9Gne9J-pIbNUUV_B_2E_zQABnu5jnG3RRtBrGlSIeLm2RefxjhG2LspSclVY_IuJ3y09DObMYWcM5WzAUG4J3xOnn9cfYx8TDfg_CgK6qWUHuqYuiA3HkCAlkOug4PiuFLNKbFswO9uoODASHH38Z46IqtFzob-mtKt4BrgZgildl2dSSb79S0TMizr-zlUFeHrWE4nbESlYUAZiyjFnR235At0db1aG55EAPwiysDWI4rSkP9CGCMVPWyL1YNGXxjUAaIkmcndIGnVCcYGEuU6b5iuOQLMcjpR-Yg__HBzVq_OCg0n5-kErCr2ZRN-UzRSXlZkaakb_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guqywj2tjMPkvX-uVYOUv74W0HevSXz9QhPt5gbUSlJM-aDFOApNwRDxFGsOxWP6lzuxVioxdG8VXKVvm4tpKg6LCSD9GeCa1U7Vh8SoHKf66Kuv1WlQvZpf_VDCfaqb9wX4CqQTvm9Ber56cbNdl4A7-cZqCgIl4L_-rV50usUSu6GxIPv5G2Xbn9pdb29_DyAtRT4dp5b-7GE4oo_j1AF0kTYd5MTiRDd5XU_dx7ubo48q_OYAyBp3eo-jKwBV0hf0ZsII7l420q-IT__EXF7iiuaQNch2ZYfS5Ni0nd3-D8xycLoabpdZCUpdwXDSXNpwAqHGgyQJWPM2_XiZoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28622" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28620">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQeZBLOTiKl6RFE7QTW80FTyMEs8tUvhiZ5rYIviF2WiD2pZKqplA6v-v5UvdpV4tGcsZJEfUmuGkZIJQPHJxeEHALOYyyAkfdYgtjTOVAu1msVU3JNo39EB60mnx6rtbVuNE6RRND98ze1l9KZpRvs6MN6PGxqDdzNuufpt_eQ8z98BUCer2et0kS3enrb65hosfotm2BLR6xSR3HFlao0aLlOrmviKkSIAbVXjBEzXiQmj-AkD8nTWbMM4vmICQUsytvYPbQL5SZYeProLnBxONVEXIpncKC9DMBITBUPp-75MMMRRaGJew4jN-7AdLIVs8MKbO5isoR47P7gwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده کیلیان امباپه، وینیسیوس جونیور و جود بلینگهام درکل دوران حرفه ایشون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28620" target="_blank">📅 15:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28619">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dojPIYoNJT2CeE6bYqdouNqze2povjY50BouFpXDSc11UOvIxf5YQBATvvNQLqD5BcRpfKMErM8tS9enA7GLNm3mXULzoxCe2VFNCX08yCm2P2kMObFyNEurLvzF9GGrw1lJbUdwpUF7u-Em4BfzpmtIu17guUqS6Mh7bLVpcYenBdQV5ohcNxj-NuHcIvTWBG2IacSsVTtob2jIuT4EEtwNWYkOEJyRi15owaA2p_9TlJr8bEmnQd_uqLbjzLqRSr1A1jJrcb1_l6gWsFW9QcCh1ZuY5nScg441iML3tyzxTPQ8lpyQxN7rzu8Oz2on5XiONyTcgj6a4bzbizPu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک دیوانه‌وار تیم ساپینتو در مقدماتی لیگ اروپا؛ پافوس باهدایت‌ریکاردو ساپینتو شکست 2-0 دیدار رفت مقابل هایدوک اشپلیت را جبران کرد و با پیروزی 4-0 در مسابقه برگشت، به دور سوم مرحله مقدماتی رقابت‌های فصل‌آتی لیگ‌اروپا صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28619" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28618">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_TR1MfQQcR-eqJa67jDnSmE8TT3HnNopKaTLEk1bdm5ECPm0m8t38MkCRht2qbuwIEUge3QTvPU1hbnKHrVd62jyMEVrpZg-rcK9pjXkCBzxzxVjaZGp3UDRJwIuBT8otiYNtJUILZS1UFGQb8GcsAE9CKjn0x16F2cNg1sn4WrZEAzrlB8TTd0820-hyJtOx0gKBK2J2eHD9_XsQ-vkqWtlZkLZVVCHqchf7w1P_BlsYuRIgWnnAhm96M1oo0ofd56iuTExPGZ3hCp7cL_Fp_Vk4pTZHpJXmLyxvQCYEOCIvt3stQ-9DafXV4iFtUc2z7ir2phlvzfFIkUXj8S-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28618" target="_blank">📅 14:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28617">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNbQs17xDWgXQEOOh-1oKsoEwG4Eox2z_vDtECRce8nRP_QAQxPRGOvpmDxOP30B50NM5nUmvqlGQeNecOncTD_jZH-2Q_HglrncXqXm67qy2JRCl_Pig1hIcbppon77Z_bSs-dreLyDquxKQO0VV9LvNguUbYNTOh0U1ZnPpj-syHjXwUBjTOGqqOfRjX9Y6O5PB4p27Kc1CUhIEQA7byKS5jCN-TNa-xu--X3_mLNsFGunA83h-RukFF5uJ93lphuMxqcI0atFd7nANUucl2EUQ8wFMPpykDE7a1WuE1yDFVCkLWcs_Tjvm3Khm4kJe9EQY_e7504lL9wIC0AKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛ آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28617" target="_blank">📅 13:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28616">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADgt43dE2H9IbOzAD210Cj2csvJMiokIYvIUKMAj5WrO5-UzNKxvSy9nev8M6ioMd9g18R4Kdm6aNNW5W3JCQKhC5OViybELkMRT01e9yT0HbHcxNmU0RUUaIXqiCKzuBUv7YaJFRv4AT_txkfdrUqCtHnAL3VnM_eZC4a4dx9K0xiCmf5PW15gtSXfW5A4_K3OfTNVM1ZqYmMrBToW3Qy4hq4811K7QnWeE2gju-P5PR3hkJVX_EnLrNc7LQO9aeHV1Fl_4RcV1sARrsLLmWlC-ND3nVagQ4tVvLq-TkX6NuOvOVa7D4f8x5ePXFSw_iSyakLCWyHrr7nuDR3Ar8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28616" target="_blank">📅 13:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28615">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dubHdjXBGUZDnRVbUnbkGGlKaKahAvzp4jSrzcPjp30qPfFIUKufl6VOFIPo8HN4r5x0FQYHsXauSih1P2ti9KLAO_vNLRtabB-qxZgrSYkggaNUK5TND_JILL2BLJ0uidRFUcFSQe_xIZfGmF3WmF527UFJ1YeUeeyBfB-rUxID52m-I_3_gzBhc7qG6sxKrRp2HkC-GOHdSz6lvcMgRsSTMK1VfPKsIFhkoBgS9TeLjFui5stdR1RVdoQuluDNCI2_oXK77NAXjWFl9viLMUtyBnA4zlJBIflS9dPHYGeMc8PHfeMHcfKW8bK-pgidYdkIFiSvYPXs09oFDrk3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28615" target="_blank">📅 12:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28614">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVR6l8SHSd7c9AxnSqBwshoJr0SHd7c63ruHTmpYhr2KWB6v5_7WhH03leVDTcq6lm8BvRtqqXFZussfqWJdJhNMBPHPAC_ZXZh-HbAAeZhnw5U_VZdtO3MGq6w1_V9NjjixOmkDly_8_GBOzfea-wmoyZyMkI4e9wrhgCs6Va8QWqfzFT9e6bt7tuyoNkSjNyu4LbJ5iP2EX0oOGqPMvaRoCds5U7hJipBiU8ay9PhVs_za0OZ_AZDNVZ50o1w-pc4M9nG-Zrf2v69-lAzrbEQAuqy87YnBUBMsNdF2EzPxkIMr-lIaCvsCwZ1bVSmgK2zaWa05C6rb6zZ6K_Nn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28614" target="_blank">📅 12:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28613">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhMDVdkAv88xJyVMUPxWGlflFdLhWAKTt9zGQl700BBLWMEWMPuyFisBGXlYX5s3h_r456PA-0ki3RFjK6tvMMYZgDCZa2THbiKjwuyYHkk4lhXDiYPO5E_vBR1zUpHfa-A0KkZG4y3tODVqaaAmaNRfuk8QEVTzKHJTUEY344JMgd1oCfoq4TmHcS8cGIVs8gCzXOfDQejkl-o6lge-bP7s2TYhtwHem6DbpRXdGIxNRaIaLluiKy8QMEv6n0hw6kl-TByRU1MNZGsoQfnY8ZQP2yl4zvFnsbf9MAt_Qw2XQ7zCTcKXtI5wOXj27OpkiKVKFgoQIqcT_66iFflDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/28613" target="_blank">📅 11:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28612">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVodDbjlACJpBvTzeaiDiW-XSH3xByaUvUBK-4XXznI7lmswU20jNyt9Y_3QIFmy5_oAu5AQ8GBtNcTjXAyEf-yj3t4oJ1ogWpVB84LRTSw438iMss0VnQcmYxj3aob7lrWrGwhnYWmVRgEHhBe4prw0ps8CXSq0CaObFVDi0sWUcfmLw5790AjHelcvym8qUlaDfbWDjwqxEL35H2E_fnce21MJ2TPCSduk-_ZZe4kvoHTungbUB8CoNM2MT9d57QZnxHLnfvbd-7wAwo1Xz7PZGl6f9-yrihjnWdxewM7mP7CYpzuxSkXJMqp5x_rSKLZEe8ca6KyjPjxdX0MAWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28612" target="_blank">📅 11:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28611">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5mACEJSPCxTlK68Jh2blw_ShWHJkq7IAyjX5S1dGXZ_bljhBnn8tJLJJKEY1PjPeq3_PWYa-3q0OMZuObXO4pmnrU7Bra_nvYF8vqVpWvWgc63PDHwEWHoFgZqpZJyMmqHY3kSSQ31gBFH2sCfNmjzApTVdutWrp3Q-61jb2Jw1C5bAR1VTbbaHkZnS4wR-RVdZmzMnhalse9ofrF3JA1cPYuOr4_Api3VCAoTZlIMTJP0yM-ECTMKX4FThYar-sEerhESv9iMPVuZQeOqcDbNvDALkz1igRn8Zu_oI5EnxmKJ2PStxdalJ780b_IJqw2s5UNChVwEhS6sRH-ipIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/28611" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28610">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra2DXv0ZmHV3ePe2VffYDxxKXJTbMYm9mT97pvr7rFnDA1ZE5-dFwzPT_iABBsRR24EEC287UsTnVeRPEGn41bnE5DgxX5Px31BDyP67Xw0HwQNw8Yfv2bbIQYpYyBB8OkguHzOXG2D3hcd8qKE_U2Kwk_5YyOZLNiGSyLSHWvPFJzMAn1ZAoBGC6w02dozRLY9u-8nkwL-I06992Sth-pv115HClFNA7W3RObuGr5EpIrbrhMLdCcro8WNgXKQzJc3IbWUuWEdGcgXmmUPGROpcRFaDvgNlS24rfgkqszQ1tmkoA_gdD-wuZJOXVJI6WlDMpHgESe9veorZ2QT-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇩🇪
‌اسپورت‌ امارات: باشگاه الوصل بعداز جذب مهدی طارمی و ریاض محرز در آستانه عقد قراردادی دوساله با مارکو رویس ستاره 37 ساله سابق‌ بورسیا دورتموند قرارگرفته و پیشنهادی دوساله به‌ارزش 10 میلیون یور به اسطوره دورتموندی ها داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28610" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28608">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph9Immez2x1_9s0ng99O5oux_Bcm1UT8gN5mSvK2_XjDfIWGPnBa6dPkNSr4ESxrRp8Kl9TlzQyVA52KrYu8DEggdY0o3MBl3rec0dgTir2D-NGuJ1GDg6dNizygtWM8MqA1u5KWreIonoWrY4xzL3jm9JIHbLOI02S20ZmWKRgBnwRbR1MBABOs0hdwB-byTliHJ_AohVMnAh_u-KBK6NFr_HUun3gBPNlBypAEv8P5rs51fPozLMmd8l0dO2rDC9hqPwFdZwG9iwuG9b6cvUZiY1WAPGoNX6J_5ELXTWxg0zQV7l2E4nASBFRbsnC3ekMP_dzD_v_FIGghsh3eNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ با اعلام باشگاه تاتنهام؛ عمر مرموش ستاره مصری منچسترسیتی با عقد قراردادی قرضی تا پایان فصل همراه با بند خرید دائمی به ارزش 50 میلیون‌یورو به‌این تیم پیوست و شاگرد دزربی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28608" target="_blank">📅 10:09 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
