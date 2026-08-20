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
<img src="https://cdn4.telesco.pe/file/qovZddC4287OFJZgCLiaiQUnxmyITpvjClvoHhWTOKiVMOEFRkepVeNyW40SNyJNBJQURj_Xp44k64YpLs46adx6LhoWBa70N4wVN3ped1ZSWJrhFnHB-tk8U7EG1pEQry78AZIv1CdVuAbBCWtb7AN1BExEK7E0vYiQb7wFq3NKbLgOnqwATxxkjNpzbjGyEJFVRNRJOjTe2l8Fo9LQ2gzodtETFW2Dx6lIBwlvXyO1wOWO5l0ANLyLYQQmL58O5jDpsmIhy5-05bQajj11cPbJfVG95dfDjZJJEwjRgRJ4emo_pSb5b-scKD4Bv2FMoo5z1oEqN2nstm6L91wjVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 14:48:29</div>
<hr>

<div class="tg-post" id="msg-82388">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jldppwXg69bFAqwsf5_2Hr5Q9mD5LAAThKnO4db_ZLwPyXSwlLplEU2onur6cGe6eUCob_zQPWiMyCagBkL-5wr3hB5-o4aenFcuzVD5fEzyurHAM9UeC9B8DTqatsMa0I0tb2YT5rhIa2IvTXbsCPUzhzxbLi20op--VlCy9HFLS8Lh1Y-pBo-jAUMRFOWwQeu1tBLe5cJviqNj_8MteQtLwUOfpFOKJIAnDLJcINyAvyFY1kqM2Egt4EpedktjSJlLef64cWXMXaL6ywgBzpgsqywTvWrdXE4QeuKFxf_aLszl7hlGTXVJHBbxdsVxqF5FXzvC1XxGBEWGuOBkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار رو به جلو اگه جواب میداد دیگه کسی قد کاگانو مسخره نمیکرد اردلان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/funhiphop/82388" target="_blank">📅 14:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82387">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b2647e03.mp4?token=ec91ISQWlQWUD-82IcvL2sk0o05WkoH0ezE9w88kjGp6C6cfur-CG54nXfL1dejc-s3_oJhTOqr-1HSeuUjuWcAXNEQ1TynMgWUqCpm_0We3RrHM98PrmpOLeYcaqXkHSeKUKs3s53B6Z3zvQwxuFO3LrgC2MAaPqOU0jGpgbQXU0bfa5g9W4g9naJBF80RtSIr8wmHwjn7t6GjakW-_7XKIWhIW4uEKPvpZvM__cEGFmUkluv4G763DQ4LSmhbCY1pPdKquU8kTX-sbZrNgW83fsnNYI2CYB8FphEKBYsLJpJkIzzVQkO5HSjqRii4HB9NH2KRYBgvO_8RVY6AI4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b2647e03.mp4?token=ec91ISQWlQWUD-82IcvL2sk0o05WkoH0ezE9w88kjGp6C6cfur-CG54nXfL1dejc-s3_oJhTOqr-1HSeuUjuWcAXNEQ1TynMgWUqCpm_0We3RrHM98PrmpOLeYcaqXkHSeKUKs3s53B6Z3zvQwxuFO3LrgC2MAaPqOU0jGpgbQXU0bfa5g9W4g9naJBF80RtSIr8wmHwjn7t6GjakW-_7XKIWhIW4uEKPvpZvM__cEGFmUkluv4G763DQ4LSmhbCY1pPdKquU8kTX-sbZrNgW83fsnNYI2CYB8FphEKBYsLJpJkIzzVQkO5HSjqRii4HB9NH2KRYBgvO_8RVY6AI4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازه میفهمم احمدشاه اون زمان چرا این حرفو زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/funhiphop/82387" target="_blank">📅 14:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82386">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جواب کنکوراتون کی میاد، کد واسه شارژ ایرانسل لازم دارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/82386" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82385">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvIiHnKbz8cQn59ZvWfBRkpv-kYXgnFNGjAVcj_tdByFphwrElwAi1oAOO-td9IxKMtMW3rUNx3E6MVrHQKkWXQrT75CRz8MXvhDoAwXFZjVqVe3b1Ugl1X6jiD62uU-HnUI6dRwJrHA4Xsj9jWaGCIi1qp_jOyAO2X789Xx-NmmsSF-RCCPx98luklyMbtqu7jyGhKiwR25MWEmhydwc7O8wNCk1ATNnTnEn1jQLzMGHDVu57zxPRwI_hpiSsUPUoz36usW17uTwuxKO_54mxRwcUTURYCB3D7u8gtiYa82fKYpTPcz-guHvuzEAtndbF7y_u4A6AO2d8tTcZJyRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی ایرانی هعی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/funhiphop/82385" target="_blank">📅 13:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82384">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کره شمالی حدود ۱۰ تا موشک به سمت دریای ژاپن ول داده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/funhiphop/82384" target="_blank">📅 13:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82383">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">به چین بگید یه کپی از اقتصادمون بگیره، آمریکا میخواد اصلشو پاره کنه</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/funhiphop/82383" target="_blank">📅 13:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82382">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b86b48a5c.mp4?token=eCymOBUsWPtvw9Vo-RnXFRgL8dbPUOldvfZohUlA4ZA81pWVDFgNKZKeyP3K8siYjTEjzEHhlYuQpV2DBsI7PHbOFbsn5Bmi1bsZpU6dpT8irl3_fcJDIcI5CTKiusxCoRy3VaYbR58hIVHjazItBySMrYvdyQ1RSSsqJMq76bseWd34Z8LTmliBI-5HQ9InIkevU47Po-dSxo4r3kZr0ggIeN6ywmddpdUpgvDI7CPujwATRcorh6xTwP-_ZCMffOubG2q3LYOgGs_A0DOuBYUFIY1hSDIqQU838V_FMjifE5QSVSGxe-jbZsvb8h0Xm11vFO-voQrNhzsJRjpc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b86b48a5c.mp4?token=eCymOBUsWPtvw9Vo-RnXFRgL8dbPUOldvfZohUlA4ZA81pWVDFgNKZKeyP3K8siYjTEjzEHhlYuQpV2DBsI7PHbOFbsn5Bmi1bsZpU6dpT8irl3_fcJDIcI5CTKiusxCoRy3VaYbR58hIVHjazItBySMrYvdyQ1RSSsqJMq76bseWd34Z8LTmliBI-5HQ9InIkevU47Po-dSxo4r3kZr0ggIeN6ywmddpdUpgvDI7CPujwATRcorh6xTwP-_ZCMffOubG2q3LYOgGs_A0DOuBYUFIY1hSDIqQU838V_FMjifE5QSVSGxe-jbZsvb8h0Xm11vFO-voQrNhzsJRjpc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر زن شایع ازش درخواست آهنگ میکنه، شایع هم تصمیم گرفته این صحنه به شدت فان رو فیلم‌برداری کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/82382" target="_blank">📅 13:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82381">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urP2DlpCT-_3bJBBK3VAFUucps6YwVEYsXyeDJXTZJHO1u_h7gTqTN3q3IX-_9S3z6ABGJQxnUS_lEc0BR2Xl-WYh-XIhmg8J8pF_XBewS2dXSLIAAPGtqgBbzJOgsS9vJnmEDVz_vikAOq3QpviLyeUbv5Sh8Sp417-rbnW3zVEsBUdRwSXGRCmvfXLuSNBE_G9FMIfwF0K6eldIK_zVvgt_WfbVG22UNp2N8_YL84rajPC_L0jAChD4A7BP6Fg1AYDompOAWM71loNKeiAKNoAUI9o0MY2c2b-WiecN-hhgebRwAql7tkVGvW1KghyoNQ-txnbZKpnQW_IJT_P8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر پر کار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/funhiphop/82381" target="_blank">📅 12:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82380">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عارف، معاون اول پزشکیان: قیمت بنزین تا محدوده ۸۰ هزار تومان افزایش پیدا می‌کند
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/82380" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82379">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVG2q-vDxA3TCvGNsio-6I1kf8__NCVdDVHtiPYyz3VLvBhX6FXPGqcDUc_j3yf9l6Yqn5x2JDddnSi_8nLL1xUustvCrcdHaKbX_Wp27hkod5pFvRoDawYmFPwlwU_F8hLsJCLIW9kSR8_9mdWcSmvMJXkOasJtco718wqACSRI0UeoIa0eJPrMrOdB4zSFJEZgbALromMzlrvWixqfdxAwPeUnRt9F7ub2lkwfQFRuuxGf2Kg2IRjziX8fsQc9muReDl8NgFMS9QEHZPox8iAEN39hcoOqSt89E_Fbx7_DkZGe3OnFO80Uo4rixXFm6YZDJTB1HH1lrLdz0h-hCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری رضا علیپور :
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/82379" target="_blank">📅 10:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82378">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45111cea33.mp4?token=hiJZsLMZqpuyI3_az6YbA7lbjKQBcI0Y6ny4rLrFgBLAnNishPIUJ1irNfAJWUVwSjlGopM2dsLUYeZVVMIU71LwxAV1jYJbYOk7iTDCjpG6cYojjnzdvycmVIg1GLfD3-jFKdvc_rU4lRAhkqhjqs2GxXfv2ideKuwv-cDq4VhYhGEUD5ITawY8Y5AYAoUI2gH5EQIB84YQ9-64yDCKpsXd6By7V7A9uPxmpst6pqj3eraxlmKqX1q5HiRHq3Gjo660EpwrhlL1jp3avzEY9CfXLPN-TMgi0AoBJaY3fDLPRI5R8II_svUUf_BepW_HndDRCj5yHu1pekMcAujz7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45111cea33.mp4?token=hiJZsLMZqpuyI3_az6YbA7lbjKQBcI0Y6ny4rLrFgBLAnNishPIUJ1irNfAJWUVwSjlGopM2dsLUYeZVVMIU71LwxAV1jYJbYOk7iTDCjpG6cYojjnzdvycmVIg1GLfD3-jFKdvc_rU4lRAhkqhjqs2GxXfv2ideKuwv-cDq4VhYhGEUD5ITawY8Y5AYAoUI2gH5EQIB84YQ9-64yDCKpsXd6By7V7A9uPxmpst6pqj3eraxlmKqX1q5HiRHq3Gjo660EpwrhlL1jp3avzEY9CfXLPN-TMgi0AoBJaY3fDLPRI5R8II_svUUf_BepW_HndDRCj5yHu1pekMcAujz7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشته شدم
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/82378" target="_blank">📅 10:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82377">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3dil1aMCjP55vDnVDDNPmDx86Y9M9giEKX6fKI9T1k5L4mv3ZbcptdZOKtchSxe03X1W41PTzJVJNIJ2fEO01uwDUVuLQNVC2Et1HyKztHAY3YEQDR2uO7DCgfZE_KVLCt6wsCJSXd6Ch_8iJoYvFiUNRgyqwsRZMR0FeEnR1UqsP4eErzQfwhdxKlFjgzLBTFipCeaYTQ3m0HVnZVU22mzcNI0FfbwVZfPAwdgY-x7K-R9J8LKV9Z51GkQQAaLvJubSTgb-005Hg3eUGr37fmp3tqpirxYitTbXzvuYd0wGchXjfNCb9gCj-M4_4WJNYvD8uhMrf9tK4m-XXR5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس پنج + یک بت‌فوروارد
🔥
⏩
از روز دوشنبه تا یکشنبه در طول هفته، رقابت‌های ورزشی مورد علاقه خود را در بت‌فوروارد پیش‌بینی کنید و به ازای هر پنج پیش‌بینی ورزشی حداقل ۳ میلیون ریالی خود، در هر هفته یک اعتبار پیش‌بینی رایگان ۳ میلیون ریالی هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
btwd.link/51
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r29
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/funhiphop/82377" target="_blank">📅 10:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82376">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دکی هرسال یه نصیحتی چیزی میکرد برا کنکوریا امسال انگار یادش رفته دکتره
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82376" target="_blank">📅 01:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82375">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF7kifqobdt26sPFpt7pPIaPYzwPMiQ3XW_RtIuR0S5Oq3J6aLn0nwh_ayd5lpe2JHC_vDA1zsrkWjLPmtOe61Pr8T8SmIDjy0nhr_cdCzXlqrPCEyOBQfMdxulnjaeWA6i8whlXxdya1OLVLg-P1DnYf3he4SbZx7gbIh_UXdrZxAi5Gc4q52FCquBG79VKbV1nXPFOAuct1a4JewPHjVmU37BVS9kUThQrhYwZ2CoixiG8p-9pyBVlcoAF4l6b5f4TcmcEr7Q54Giwzq90J7MwsgHUEFHJV7ltnDrX_hWcUhGvL0Y8RwjIFoKxppncC-uLghkVfMM6TDStkFQ7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا قبل از فروختن یه آلبومی که هیچوقت قرار نیست منتشر شه(پول ملتم پس داده نمیشه):
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82375" target="_blank">📅 00:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82374">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9019847c.mp4?token=MgAiLXOaOdvihngApfaNU78pMDmDBVlSRYFlGHwIQrfvZdj9aw0YAU0TnHFhF1i7pRK5NYdy-nfPTY1uTpxmKeTjCyu3yb0FtvWhNsIueNbTh-VdRDjmd_Ix6gJRR5Wkcsj73gwoyo24KP2AhDjSh-1ZqSfp83h6k05JXcTRwhuy81IPZXqw32GWRqmktPr5HmJHlo591B5o6oUToc9Ll5_T55gRkG16Pp8NreGN7T88a3DxRiJa7SWattROJbq7xtEC2dg0BLhw3krFj4leGvI1X5XXq3aFJFQqHOgNaDJG6cDOY01EqCHKOjE3eqAkH8D2PUmJ4rYBwnSDFRX_gFxB_dV4xpKBVs3aZ04c9Roz9QLLmhp3Gk3N3wrwQ72LHEaLxpfMi7ldg19gAJwOdmSLXAsgIumOjSp9KZ0nf-zOfWWumY_1Ig-vkT-mjKxCX8InOskmigC1B0EeeJk1_xXN7f4Zma69I9XmHy7ThwlYHBgiJQaymqiSrRonR3qQQGHt8s6JzO3CYloOOBgzCz9pKquLjHcL07SBDmyFd9NgKSkiVGWrUXqhXRIt3Xc7ItADKo3d4l91oMVVii3GnVenBhxGIu7x6w4dYCzm5Tbg93pJsQGz4XEoLJT8fu7JZMkBWAxmHGPs9S0bLr0dsItZZOGbg170FWiKGDy6b8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9019847c.mp4?token=MgAiLXOaOdvihngApfaNU78pMDmDBVlSRYFlGHwIQrfvZdj9aw0YAU0TnHFhF1i7pRK5NYdy-nfPTY1uTpxmKeTjCyu3yb0FtvWhNsIueNbTh-VdRDjmd_Ix6gJRR5Wkcsj73gwoyo24KP2AhDjSh-1ZqSfp83h6k05JXcTRwhuy81IPZXqw32GWRqmktPr5HmJHlo591B5o6oUToc9Ll5_T55gRkG16Pp8NreGN7T88a3DxRiJa7SWattROJbq7xtEC2dg0BLhw3krFj4leGvI1X5XXq3aFJFQqHOgNaDJG6cDOY01EqCHKOjE3eqAkH8D2PUmJ4rYBwnSDFRX_gFxB_dV4xpKBVs3aZ04c9Roz9QLLmhp3Gk3N3wrwQ72LHEaLxpfMi7ldg19gAJwOdmSLXAsgIumOjSp9KZ0nf-zOfWWumY_1Ig-vkT-mjKxCX8InOskmigC1B0EeeJk1_xXN7f4Zma69I9XmHy7ThwlYHBgiJQaymqiSrRonR3qQQGHt8s6JzO3CYloOOBgzCz9pKquLjHcL07SBDmyFd9NgKSkiVGWrUXqhXRIt3Xc7ItADKo3d4l91oMVVii3GnVenBhxGIu7x6w4dYCzm5Tbg93pJsQGz4XEoLJT8fu7JZMkBWAxmHGPs9S0bLr0dsItZZOGbg170FWiKGDy6b8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاش بعد از انحلال گروه تیک تاک منحل میشدی مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82374" target="_blank">📅 00:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82373">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رضا پیشرو داره رو یه آموزش جنگیری جدید(موزیک) کار میکنه که معلوم نیست کی میخواد بدتش بیرون  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82373" target="_blank">📅 00:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82372">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKPDIVa_dAB6YP7Iki8RfrfTdETm0KGM884Mpjk6ECYd1nM1O7jizHZv2wJHOQ-KBLwBH--U-76xLqKrQsIgjJ18jNusLGgsIwr6T08QRveoUaF2VLV4e_ZYPd96eqJ2p0_xiaOPqGXEMP3CNT4owd0XNa3pqbte-Fyyc1ebL-B9uGnQxtMUe4ghE0d-kNmwAKJIwWHo3wYTvhk_4G9xF9-XBDcOWsGYSUce32qXi88jQdp3z2hZQGVKamwctzL2xow-vkEhny1-qA81JtkiNiTOu7vjKo6Bt6YufWgsBP24eOuqY6a3AJUemff5a-la_8PHeT0LR8nEdnjCDb5Ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82372" target="_blank">📅 00:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82371">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6215c87b9a.mp4?token=LGZ6mOdy3hoctjYpPyw9hQ7RdT4YMpQ-pXSrGorhF6xIJS5_hWRyNeOfc4AFFtmr9Ax7HiABXr_PusWydFHU4KIIEgpJ9lcvZygOdw4_aR2d232A3aJhC2Wjl_FsYRbQZB8AKvD1IpFxnBSLwzyVx1iKcELByx4FtVIZ_JHTg6IDG-i131UfdQnxZ6blISlLy6S_66vIj6g4FeIrdGyMWRTN-0o2WQ7u46AMCnhGF91QbWhyNEHluEqDXI56-SaJZE7XH72NmalXUTDHxyt6NUyyGvuD2W214yIxBLCRcx1v5j-UFJZ3j1q_H7c007-_U8Wctl2WyzXQh5y0FTI9wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6215c87b9a.mp4?token=LGZ6mOdy3hoctjYpPyw9hQ7RdT4YMpQ-pXSrGorhF6xIJS5_hWRyNeOfc4AFFtmr9Ax7HiABXr_PusWydFHU4KIIEgpJ9lcvZygOdw4_aR2d232A3aJhC2Wjl_FsYRbQZB8AKvD1IpFxnBSLwzyVx1iKcELByx4FtVIZ_JHTg6IDG-i131UfdQnxZ6blISlLy6S_66vIj6g4FeIrdGyMWRTN-0o2WQ7u46AMCnhGF91QbWhyNEHluEqDXI56-SaJZE7XH72NmalXUTDHxyt6NUyyGvuD2W214yIxBLCRcx1v5j-UFJZ3j1q_H7c007-_U8Wctl2WyzXQh5y0FTI9wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم تو اینستا تموم تلاششون رو کردن که همه فکر کنن این پسره واسه عربستان سعودیه که آبرومون نره، بعد از این ویدیو فکر میکنن افغانیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82371" target="_blank">📅 23:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82370">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKmbF4WylsCyPIu9vqRZS3eNvVOna7bg1jq3uhHvCaFAnU-e6UiryqHna86Ba5sCmQ52dEL3qUS03pkTNXx66SmJFUt6cd-feRoigm2iSbGUrrzP-ufzAKZ5-bgSSOYXjPPGuSHsBjdXlv1FfB7AVW8EwmhlW0lBFaDOe8fNcMqfsR3XoE-LAQcQA1WoCH_opuiJtnms94qqzxXwE5MxvAZQZlzmQMrzA3bDjykzGU-M3iX5A8DVb7xFwtU7QiUGT-2JKmfLj5wd_KVxq6x8gSh9S6rS2IkHfwSp0-D4rlDCJCcePBjU4rIh__p3sytK2hOqLGAoEBGi_tfhHw-RPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82370" target="_blank">📅 22:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82368">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
نه خارکصه خجالت نکش بیا اونم بزن
ترامپ :حمله اتمی به ایران؟ نه ما حمله اتمی انجام نمیدیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82368" target="_blank">📅 21:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82367">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سینا ساعی هم زندس بچه ها</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82367" target="_blank">📅 21:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82366">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304e080993.mp4?token=f9H1BqopR4TOhztx95lKrXPXC4sLZBTVQ3MRW746pttKiU9RvF1L4rnSd-98loi4Ejtx6A45oJIVsIpllzG2K8FVttxgsmDQjL83k0g0PwlxI99lBM5nwGN4SI6PZGhPrFMZYHeibuG0i8pYvGklTFt0e3T2ysHA0N_U-n5tPvnfNzp2wlLCfwFykA2K6hNIEimXtTk27HQqQnT8mbSUxPDzp8l0zlg0CsXehk0e7ZXpcXp86glmbx58QUV-D27KhLlQ5yOtncsQ-PVtShYDGYkVinDdZ3me0rb4whQl7S-iCmaUCsSeYo0GsAVtVz4RO9YhVNf0Fj4p40rzLemsaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304e080993.mp4?token=f9H1BqopR4TOhztx95lKrXPXC4sLZBTVQ3MRW746pttKiU9RvF1L4rnSd-98loi4Ejtx6A45oJIVsIpllzG2K8FVttxgsmDQjL83k0g0PwlxI99lBM5nwGN4SI6PZGhPrFMZYHeibuG0i8pYvGklTFt0e3T2ysHA0N_U-n5tPvnfNzp2wlLCfwFykA2K6hNIEimXtTk27HQqQnT8mbSUxPDzp8l0zlg0CsXehk0e7ZXpcXp86glmbx58QUV-D27KhLlQ5yOtncsQ-PVtShYDGYkVinDdZ3me0rb4whQl7S-iCmaUCsSeYo0GsAVtVz4RO9YhVNf0Fj4p40rzLemsaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران آپدیت جدید داده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82366" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82365">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هیچوقت واکنش بیش از حد ملت به یک سری چیز هارو درک نمیکنم، مثلا وینیسیوس جونیور ریش گذاشته ملت یجور رفتار میکنن انگار فیلم کون دادنش درومده، والا بخدا قیافش بهترم شده دیگه شبیه میمون نیست، چرا نمیکشید بیرون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82365" target="_blank">📅 19:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82364">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پوریا آدرویت از وقتی نصیحت داداشو جدی گرفتی رو آوردی به ساخت کلیپ طنز و از رپ کشیدی بیرون همش تو اکسپلوری، همین فرمونو ادامه بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82364" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82363">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLvi5XJ3LXMTx4VmxNVbJi1AM4g6mqrJtOh3Aap79B9j-DRJq_PYPSH0YiDw1s0DzaJonCZLWxuUQN44CaitoTpq-COkn-U_Gc1rNo8d45b_Fl-Lced7cK6bprlFVL_426FtfpyOqgACIBrT4BoUUm_f15vDMBo-MU3tXlBhb2x-CWtrKtY8eYu4Iax0Xlh3HzSN9P-xeOWrExCRXZXMP3Dkp_2ev_YD98c1EluB_LmMOn5dG36ooyyr59RzR6Nr-n9CjDcSJzGX9WX3FrVKhhomzKl5tThUrgk5EFffNsTFcZR14PZMRyyzsfR0gQAiVf6BzshTavIcD1zcgMaVQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا خسته شدم از بس عرفان پایدار با هرکی آهنگ داد دنبال ورژن بدون عرفانش گشتم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82363" target="_blank">📅 18:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82362">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ناموسا خسته شدم از بس عرفان پایدار با هرکی آهنگ داد دنبال ورژن بدون عرفانش گشتم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82362" target="_blank">📅 18:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82361">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN8npAXezRg6Y5trWEcOhaFRq477UyhWyiCnZ6qAYBakwnSsa7p6YurJ81Qwh75w-pcslhe-UlH_-hkmUFzHrJ8rcifeGTcUfAVXE1azoCZ-SlO3DWOTu_PI9gW27Y-4XjCaT6aRwehtWhzWxeQK7wE0Rqe5tj3ZTytQgVepmSsedPv4-HD21-gYxtRqHkmQ_cij7IshpC8BP7PWjZLjAjhAepFADrRf8g5g2sxknAnS_tO80vCTWozh1krqjcFERIIU-sXeoM0dxJ4GugGm2Z7VjQWoebFdbCa69gx6-0BVZTYTl1_ksQjF7ZLVvtCw0l7FpokqZdbfiH3A8iovbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات یک سری تحریم های تجاری با ایران وضع کرده و گفته تا اطلاع ثانوی با ایران تجارت نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82361" target="_blank">📅 18:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82360">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قالیباف:
آمریکا به دنبال خروج آبرومندانه از منطقه‌ است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82360" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82359">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fb611ffd.mp4?token=LPU0itcYMRccNNDvQG38EM7TtmSowNt-1RM_FSp_e59w-dnv6RHQCnjnyKGdv-TLKWzcKmOtQhpR_vbITEGBVfXXzQlEsGmUFTTHeHCTiLRPQ6naNpzEM3HlvA7QM3yy91VlC2VEjHqM82hBs_tSUODCu76qbZLMgn7fWS-QpfUe-1Uypvdmk1wEF4urKkUbCH3k2Cox8dgHOBOIHwR69u8y39r_NJZaPT4Zt3YhRqsWUc85JB1bZdBUEbVpDSu71qnBjDLitDqyKX7dKxS7u4mlL8_FlYqioLMlr9RrNcCuYPgi3Ln960AZqoT1tpEpQPDipriGvciMBwULuIzFCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fb611ffd.mp4?token=LPU0itcYMRccNNDvQG38EM7TtmSowNt-1RM_FSp_e59w-dnv6RHQCnjnyKGdv-TLKWzcKmOtQhpR_vbITEGBVfXXzQlEsGmUFTTHeHCTiLRPQ6naNpzEM3HlvA7QM3yy91VlC2VEjHqM82hBs_tSUODCu76qbZLMgn7fWS-QpfUe-1Uypvdmk1wEF4urKkUbCH3k2Cox8dgHOBOIHwR69u8y39r_NJZaPT4Zt3YhRqsWUc85JB1bZdBUEbVpDSu71qnBjDLitDqyKX7dKxS7u4mlL8_FlYqioLMlr9RrNcCuYPgi3Ln960AZqoT1tpEpQPDipriGvciMBwULuIzFCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانی شدیم رفت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82359" target="_blank">📅 18:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZXifVNnunUY-PL9vvfEnLqZfn01YpTlF3lSVIUg227q1AVJPtac9lyXrC7MwsxQ-vBQ3F3M2DFS4CrOyGtltX6zl0-4NhHPJhUyFL15Nidhgv3p-4ae-b3C1k-We9BxDVwxqXjNLB5J99YuSsGlQCEiaxSfES7NdAot-R7Apt_tRGGwBOX8fs9Z0UUeolTpZZu2vYJHVsJk7yalaXQZNeacLDr9tq8l_uKi2lG_qFnxpOptQQ6zPXirsF9dHmEwuYw8MADuaCnuKKNVK9_i_vJL-P3tqDSVIfIQDADVReeD0OjFmzWRXQObZpBAxO-lrHpJRz60JEs2LSpXj_iIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید - مالاگا
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
㼀 ورزشگاه متروپولیتانو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۷ برد سهم اتلتیکو مادرید و ۱ برد سهم مالاگا بوده و ۲ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g28
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82358" target="_blank">📅 18:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پلیس فتا: یه پلتفرم فروش آنلاین طلا با ۲۰۰ هزار کاربر ورشکسته شد و علتش هم خالی فروشی بود!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82357" target="_blank">📅 18:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">باختایی که دلار داده بود بودش سنگین ولی حالا برگشته با یه کامبک(دلار برگشت تو کانال ۱۹۰ت)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82356" target="_blank">📅 16:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4162625b6d.mp4?token=pCAwSUVvrsw9GJ1tAYRyUw5G2zwwZtYgqhuqU6LstwOAqQO71LlAgksBmZWRDhXpdIvRjRfw5bpAuz-blXrY16Wcaa8SDFj3b8-jm0ujTt0WJIodTVp3b9rVApnyMqbFbYIqm2XHrE_rVL4iPtA6LQBTJo7BJAirilC_iMWEGotaM0UCF-A9aAKOcXsK60971XBB6TK1kkQBCCFZFJfFdwk1wX3TFAaW2Ry4_QBs9XfpgppggmannJ_wg8dBTWN6pAJ9ddYAz99KV8uFwWBQQyftK4Zdg6TN4Wy65z9NKVqMIySTyH7eGC9VJM-U51Bh0HwUltf-ILnTlA3cCaSG5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4162625b6d.mp4?token=pCAwSUVvrsw9GJ1tAYRyUw5G2zwwZtYgqhuqU6LstwOAqQO71LlAgksBmZWRDhXpdIvRjRfw5bpAuz-blXrY16Wcaa8SDFj3b8-jm0ujTt0WJIodTVp3b9rVApnyMqbFbYIqm2XHrE_rVL4iPtA6LQBTJo7BJAirilC_iMWEGotaM0UCF-A9aAKOcXsK60971XBB6TK1kkQBCCFZFJfFdwk1wX3TFAaW2Ry4_QBs9XfpgppggmannJ_wg8dBTWN6pAJ9ddYAz99KV8uFwWBQQyftK4Zdg6TN4Wy65z9NKVqMIySTyH7eGC9VJM-U51Bh0HwUltf-ILnTlA3cCaSG5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زید تلخون رو تو یکی از تیمارستان هایی که توش بستری بودم دیدم ولی یادم نمیاد کدومشون بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82355" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رضا پیشرو داره رو یه آموزش جنگیری جدید(موزیک) کار میکنه که معلوم نیست کی میخواد بدتش بیرون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82354" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82353">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf1vWLLQKjO9b3rNjgasAqpWS2a-n--tCpI3GHOPyetgneKmM_fBLVRpxmvoxdCPLiUYS6udweBgT4IrnUGn7qDy9XWAANN2yW4Q3KMRPJAzSaIPHsJs_DSsZPHFNDofXEI1mOE2JjrOXf7giclZiYI6hF1cpbCPL88ogJ4PGO04pRnnEfEDlDx74dwGU0TlxU7OIzhrkaWnBYAziPB6ciwS-FdC1xhp1UimqICRN7aA8jUgkRF3Uaej-FDM8UVuUI7kI10ltCuGxbxtIarT2ZkCiGYAM5YCfYeYjHXQ2VhJpZM51V5Qq2LhzuC2pLpD35UjpiY1_3f6QDd7zSXxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دلی که دریا باشه کشتی میده
❤️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82353" target="_blank">📅 15:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82352">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوستان ویلسون کلی ویس داده ولی از درک منو شما خارجه، اگر معنای فلسفه رو بلدید خودتون برید چنلش گوش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82352" target="_blank">📅 15:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82351">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng0ix_kQpD8a0JDePmkcBxUukkVbceo8tChjJe5PzXqpBLeqncKugW0TkUSAPrWsBmdzAQ4GFkZh6j5oPD9AI-iODHbKm3nuuWuSBNyto6EbjJ-O0gbq8ay9qeEy2lHWkJhhEw1dZZc2s3gyoUKO4ymBkPk6n-bTlzZgGcJQNOjONp9sz0kV0eAoaFyLxYEWLSX_CWnqpQVi714qI9WhwvOyNcJlOs8_hgaOKr_lbA0OHvjO3stKeCPVTdrGrQUFtDsXLNgfS0xeelkFDKTiJYgZKZWtNbSNzhUC_SJIprJErr7t1DNFnWhWvNSjL6MXANBj-DmZj2dVvMhwUNmMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری این زنه که یادم رفت کی بود و حال ندارم برگردم ببینم کی بود ولی به ۱۵۰۰ تصویر مربوطه و داره راجع به مهدیار صحبت میکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82351" target="_blank">📅 15:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82350">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خب کصخل میتونی آلبومشون کنی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82350" target="_blank">📅 15:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82349">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb3975ba9.mp4?token=hTyq3qfiAX-m2esxnqLUsvJ_d-UqIkMw9uilWXjaBL_yCYIst7ibHkVvveOO12JqOubPpaetNXl9987DApyjabOTtsyD7cfZlUME9Cp-e-t9CDE8BHWTqDRDNNJJLbNHDr0u5FOHBYplwykbPwe1ek_22IrfuYInLDX2aU9rIU_uwlHh6XBd9xmgNB1VjYcIhsP5VdS1Euu2x-Peq7nUbkVZGt5bAtDjqYJ__n4WMV5x7ROFcVamKqyyYpk8aXyyGxmGNom485t_vL1vZBZRzf4_qPN05XauU1QFrDnLDoN2JNeN95z5X1g1TPEFUnEmbSrTLgiaKeFNSl2nF9EY0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb3975ba9.mp4?token=hTyq3qfiAX-m2esxnqLUsvJ_d-UqIkMw9uilWXjaBL_yCYIst7ibHkVvveOO12JqOubPpaetNXl9987DApyjabOTtsyD7cfZlUME9Cp-e-t9CDE8BHWTqDRDNNJJLbNHDr0u5FOHBYplwykbPwe1ek_22IrfuYInLDX2aU9rIU_uwlHh6XBd9xmgNB1VjYcIhsP5VdS1Euu2x-Peq7nUbkVZGt5bAtDjqYJ__n4WMV5x7ROFcVamKqyyYpk8aXyyGxmGNom485t_vL1vZBZRzf4_qPN05XauU1QFrDnLDoN2JNeN95z5X1g1TPEFUnEmbSrTLgiaKeFNSl2nF9EY0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانی شدیم رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82349" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82348">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkCixDChY9J_53QJf20WoVp0XeNzmNf_svDs6SuK8vfNzA8qDfN0S0rDhXPigqFqQT_bEJsDzTRnv4l0kaW_aUKUkleFKYxOgZUbQdkECYaKldPGz2VRF0kPXAuPu--x9-sNYd6QaATpycSFAPtS6uiwCGP0fIL8VqMBwRRONAhYFSMnSr4PzeC_yrr5jw0tq_S8okFmvO75O6A9wg9lycmsaI8E_KUs-wOz1v7LhkK7VC7AFd7YWb3EDW4XaCSLlJSiJRff_jVcAtHK2J7Cgb24BK5lFdP6x7TPK5JnC3nD5RFf37T4cyV3hB715CN4S7r6RUCGUQJK_JTT5diyUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82348" target="_blank">📅 14:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82346">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1960c566c.mp4?token=gr9ogwbE9zZBWaZJyVdR59-QZW7hLqrfv5izBkac1F2Vgq4CMwMnorHithH08LaIPv4nDXBoEpEp9NmrNrUHHBj3Ngiy1l5nloUh-QjBE5-dPOaA-6rhb2kIf3VNTHmvorDt2kXAAVS_QWu177XF9r78YwNKWflfp_tWkitGHGUN2E3V3pO0RBXmeznd6Cg0sCOUXv-pXxjQ4oaU6cw1AFPuDipchT9WJvY9fgtm1SWXUp_f_NNp61VMddKpU3ZLSEY-PB6aeyRV_PW02BacKhotHq38WdGmKCVTRYtnwGpOQHo0HAh7ZESHE5_ZveyU7HPBpd3SVYp0vp9EIcP6tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1960c566c.mp4?token=gr9ogwbE9zZBWaZJyVdR59-QZW7hLqrfv5izBkac1F2Vgq4CMwMnorHithH08LaIPv4nDXBoEpEp9NmrNrUHHBj3Ngiy1l5nloUh-QjBE5-dPOaA-6rhb2kIf3VNTHmvorDt2kXAAVS_QWu177XF9r78YwNKWflfp_tWkitGHGUN2E3V3pO0RBXmeznd6Cg0sCOUXv-pXxjQ4oaU6cw1AFPuDipchT9WJvY9fgtm1SWXUp_f_NNp61VMddKpU3ZLSEY-PB6aeyRV_PW02BacKhotHq38WdGmKCVTRYtnwGpOQHo0HAh7ZESHE5_ZveyU7HPBpd3SVYp0vp9EIcP6tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرومزاده رو هم گرفتنش.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82346" target="_blank">📅 13:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82345">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET0CFbr3G46YaZI6Jxd3dlB08fcnCU_YMHpYTBqWN-CWTsxFD0Rj1dxFhIUwYeOMTrbwqK8JOYWObRLZyrI5Py-RFO97harRt1HEzn7TosNBF-JHiP1lPBHSU0z41wvNvP2IpXcp4GJEY8xSP_l5LpL4CKkvY1uvLd2mbqP4GBNVGFaBuJGBEdHM_a5jA09ZfLX5N4yoYfDJpUltoMOQq93MpfCRHV8I-z56CmnVtWPOOcTCvPPb2DG1RXtV6--U23aoo9Y7xoOnxgM3qrQVZQ1vHXUzJsulx8-i90WNCsKmRAMlrZn72u2Mbb5TC5T7z2KIopZhOUxQddCkvnJpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نادر دهنتو گاییدم نادر
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82345" target="_blank">📅 11:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82344">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a33e0eff.mp4?token=uUFkMiXePQrlHyoQWGEsI-lp_-MrQ3-Ucoyt3Qt6ROi-fVepZlDZaYpwRKEf5xU5odzEl5yRMZTlWckUu3VbgeSS3rKrelusP8J53ScmOiMeSUPOJv_ewtIc0s4QIhEGL9DaFWS5u95crtWc6xL7V5vuzPEh09edRmDo91gcutiNGqCiZuaSnJsKgzDuZlYR-vU52kb4sfqjBnlbszQRKFhQD0-C87tgcf6VeOGjPY3V3PON88IipsnY-Ju_YEppSY3n4Jicw_VSFKar4rEDQnqFAEgXu_4W64jmnSLSJQeL2ildxpCQhcZosnp80Zumno9DhkR9vTpozJVyLuHw2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a33e0eff.mp4?token=uUFkMiXePQrlHyoQWGEsI-lp_-MrQ3-Ucoyt3Qt6ROi-fVepZlDZaYpwRKEf5xU5odzEl5yRMZTlWckUu3VbgeSS3rKrelusP8J53ScmOiMeSUPOJv_ewtIc0s4QIhEGL9DaFWS5u95crtWc6xL7V5vuzPEh09edRmDo91gcutiNGqCiZuaSnJsKgzDuZlYR-vU52kb4sfqjBnlbszQRKFhQD0-C87tgcf6VeOGjPY3V3PON88IipsnY-Ju_YEppSY3n4Jicw_VSFKar4rEDQnqFAEgXu_4W64jmnSLSJQeL2ildxpCQhcZosnp80Zumno9DhkR9vTpozJVyLuHw2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین دنبال کننده لیگ برتر ایران :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82344" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82343">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhVU_c_ivzQFblZHgFseyhvd9qExvPTXoZeGEMAuhmxi8P2Yc95IHfIm1F1Fui3ZWE2TxZmpUE9elO_V21z9CTivRJh6kC4GkD9eBkM33TXhnWrH5NRdEr7ii6hV0ngcWaO0pMNS2kVEctWR2fys5pMu9Yn4Pyh7EysWrN7fyZU_shFQ7I0VqFioTk5Q2SyqM7ir_5cyrS8F4FC-Kmt6pQUGWj6E_emLeGG_TN3-7BvXSXrHjtkpfPr2L88sm6dX7wKqFe6KVgcbqG1Fwmcvw3L_QUkxcsKnME_uP0oZKRu35Zywr9Hx3E0kwfkKgzOPm3kT_5jHFMAj6gH33NlY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید - مالاگا
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه متروپولیتانو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۷ برد سهم اتلتیکو مادرید و ۱ برد سهم مالاگا بوده و ۲ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r28
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82343" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82342">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400ac60101.mp4?token=GC3om5rmK3h6VITvZZSSkIdFv8w1LF7RTtAjgBrhf3faeL4VuqA9XRIizqxfg8yhqBX0mWL8VGEhOoIWczk-09Wa93di9rhi1nzeIkguzvFjQjUAgS0ywXLrAZ1CjAaeZ7R5UgQnQUjq5lareHjdH43KNLf03Gjz-Uor2Zt1plYRItXnE4wOl5P5YUzMXe370sOLag9wM018tg3LxBULTpFPIqJ9p_UEdGCCAhUYd7IftodXWW1Ywc-SoWRGo7XO740ZGn1ADohbdh9mpRb_QQp63-NbZ2NwP_e72kLg3qo56CZD0I14AhKCwpvPactugLrxa2mJjJSOeVu1Ov3gfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400ac60101.mp4?token=GC3om5rmK3h6VITvZZSSkIdFv8w1LF7RTtAjgBrhf3faeL4VuqA9XRIizqxfg8yhqBX0mWL8VGEhOoIWczk-09Wa93di9rhi1nzeIkguzvFjQjUAgS0ywXLrAZ1CjAaeZ7R5UgQnQUjq5lareHjdH43KNLf03Gjz-Uor2Zt1plYRItXnE4wOl5P5YUzMXe370sOLag9wM018tg3LxBULTpFPIqJ9p_UEdGCCAhUYd7IftodXWW1Ywc-SoWRGo7XO740ZGn1ADohbdh9mpRb_QQp63-NbZ2NwP_e72kLg3qo56CZD0I14AhKCwpvPactugLrxa2mJjJSOeVu1Ov3gfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باورتون میشه یه روز تو همین ایران خودمون
رئیس جمهور تو دوربین زل زد گفت:
دختر بچه ای تو خونه شون انرژی هسته رو کشف کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82342" target="_blank">📅 10:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82341">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTRfU4J_XH2BrXfK_YGQmtjwDHDy2e5CrmMM7kNTUfulMCtugso2QZOJd3nIVEr6b447Rdxk9Z06DYgyYGfHnNIN908cUHamjqiGkhYOX0cgtr3IPzznYy0mtDhXZbpvh_qC_1bXX_29acj2hDQNsHPU6Fyh9HwqIQ216M-e5htmqzXj4kNpcWO1Z9RCCrU2r6tBRZ_7X4kv7hMDWTVA8aoxFxGWX2fllc7AxqK1G1mBrbzvSzKn6er7Yy9LunrOZEcOWwDloDpoe7vQVz-UqpZRrMXQhzDd3HK0BX67di2Uxywd4NwU99htAuXR53l2pvw3YlaZFBZWXA4QhWv2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراکاریس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82341" target="_blank">📅 01:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82340">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/om9JFeeUOamMYsTPRwrcRERRTc1zxC3TJyiFJ9Fccoaoytuyq1Z7RgaA_tx5x9ZsQMNrO_481HTDTTLYQQLP4NL1NBSzVYJ2lpNj4U2UUpZCr7vhAvFj6U8bVJs9PvnfVYPGNb4_REVnG2qDlsZPMJvzoQo3bDP6VJ-roZ9UEpmfpgkBOOyxjLitDMcSzZMDKT-88ID_ZdpEurHVSh2R3aFeN2iIdO1xJI1El1GRkMN6dVgPFNjFWG3KuPoeJMcquEDunu8_P-ZeTktSjTYRM1CSNJD3tlm5bJcwxfAPGs5zrhoNEAUz7ia_vF2ShHzca55MBzoWJ7eQxLuFOYTNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والا بخدا همه پایینیو دوس داشتن تو لباس بالایی، آبرو ریزی نکن شیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82340" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82339">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fee2d429.mp4?token=vscIthOb-aJTeU6IFeOcoHowwoUGL2hIj5fDjEHlnuprESL8w3hQeGAahn5IIoeJTvzuU7NDF3H_omyXpFz1S5w8SNRZq8SmKgOvqHFdE2unL6ZCKygZEt5cPiMz39mC9BG3RbwQXfJIGSV1kBybRDRZcCsyGloIGToZ7Hy_rObc6U19KvdkhzKT7luFuNMYIbu-8TiL7qIIkjI9f8hJdyO3oZ7t2tB9q_QprapqToHJWjhDglRJQNkC93qFxAcLbHkR4wcBnBfPTSx2x4i9EnkwFWh1eGlrPQ8EL3iUwx1lZviAB07yR4TJ2a3IUPsW_aintn6XPbtWE3D1ZOQmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fee2d429.mp4?token=vscIthOb-aJTeU6IFeOcoHowwoUGL2hIj5fDjEHlnuprESL8w3hQeGAahn5IIoeJTvzuU7NDF3H_omyXpFz1S5w8SNRZq8SmKgOvqHFdE2unL6ZCKygZEt5cPiMz39mC9BG3RbwQXfJIGSV1kBybRDRZcCsyGloIGToZ7Hy_rObc6U19KvdkhzKT7luFuNMYIbu-8TiL7qIIkjI9f8hJdyO3oZ7t2tB9q_QprapqToHJWjhDglRJQNkC93qFxAcLbHkR4wcBnBfPTSx2x4i9EnkwFWh1eGlrPQ8EL3iUwx1lZviAB07yR4TJ2a3IUPsW_aintn6XPbtWE3D1ZOQmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه کافه تو آمریکا جلوی در ورودیش تابلو "ورود سگ و مسلمون ها ممنوع" گذاشته بوده، مایک تایسونم از لج رفته داخل کافه و شروع کرده به نماز خوندن
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82339" target="_blank">📅 22:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82338">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چرا این بلاگرا که میرن تو خیابون به ملت میگن "میای بریم کافه؟" به پست ما نمیخورن تا پدر موجودی حسابشونو در بیاریم</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82338" target="_blank">📅 22:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82337">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این یعنی تعویق
کاخ سفید: مذاکرات با ایران تا اطلاع ثانوی لغو شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82337" target="_blank">📅 22:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82336">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه 2 تا موشک ول داده تو امارات ولی گردن نمیگیره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82336" target="_blank">📅 22:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82335">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHxZXkaGheBOpSWCXoqtRWizdav-w3s5t9y4Cnygckio763bfJpLA9g9HVNtFZTiAssl--7PmFEivNxddotPuoUKB95nhudTYkP7JMMH4Vfkd5Djo9rqrIs9LaTzrAIfCV2VYk_KY0CNgrgxbwKDLO3MEcc0rwD8UErXIQLLOt4Tl6fvAbVRre_iU4PiEUo7yqKE3Yszuzem2T3tu7GKi28WaeeJFfe-_YEFvUOYRv--Ja4pHKHf356ibVm_VRwGoATbcxi8SfD8FBkueYgKmZK20RiEngKdoctFeR36u5VJ9Wl0cJ1OwLy2ug7DQ6G3dXIRXl76CvnsdRFmndVInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ های جدید کارمزد خدمات بانکی برای سال ۱۴۰۵
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82335" target="_blank">📅 22:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6qevKOxsZHnlVtveYQQMbWcmFYkxXKN_NXMuQ5ZhBDp7jqie8CqqLmOc03CGuG-LJmiYyVHWgeCx8SEOrwYq15WpyQlKU76mnjFFcsrVf30ZXWkQUPFz6VRW6KTuI4nH9wPcfyppHPxS_oAXEgsIeg_V8Xe01bmZZWie45UdcnVnOQXLMReLs5ncXyYLecxNmNzixGbvw2ZltOhy2JWKs-qCxviM5_Xuo90WHsJ4at-L6nSM1kBDY8lkqDVgqAGMDbeSgJzr1hlSyE_hKSpxAmaoF3DoOHFbRmLs8DBJydfkdIx-348FlwQj8y4hkcL1F4dQZyrF_MnY46v4x8JzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AztH2DvH1crR3MpjQcXYp7kDtMGUFrl7OJYPAbL2q89i0_t7l53BkDshIBXtUp7xPMXIZO_YyeLXqF_WjzZclP6qjjfZwyBse6B1Ff_SszwHbzc7ynCWVVY8-ljoEj8e-oYGjW60_9bL7ZwfS5BjWqN_zWr3hB4RZGywsBrdaV2uwnCXoWnp9ezvLN3x3vofxp-0ZzBqCwFeH595JirXfyNmlxZeqH6qij5aCaSYRtRjfbDcFwcqaDla7K2cA65hKJfzJZyY1GGo20nX7-qdimW8zuKAITavlf2Y2oZaMXmxDCxQO4fpiBz3OURW6vU42860G-NF5KMWTQwFPT4yZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد از ازدواج رونالدو و جورجینا عکس های عاشقانه جورجینا با اکسش که هنوز از پیجش پاک نکرده همه جا وایرال شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82333" target="_blank">📅 21:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7u2fh_4g7N7bKLUvPNvpvhO4xzs9JS93QFSWOEaQg7ggDHJ2lrAHzYSPRz2jWxj_PaozllLPZhFSj-60ZD1nRNFDkDFf4qiHUITUVg3fxDtXQN_ycuwrTPwGzTNzT4FoYrLTVl3LqDr1-CH6mLBcZ5ut6TMAf58e8WkLZvdaMp70udI1ftZW3YktT89xyCsoGNAyIEqGOV69ifdlIdMc65UI0LwRZfrCLCtIafcJi6iM1lrhV6QQu-NrcpAAFWpoJdly18Vm_gE2dbYRCz0IJvaXfgq08HgNtp_WP8OrM0G5TA-G0psxPZX8E5RAMA4l9qZvHvnYyuQ89JBmwRWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان وکیل بند شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82332" target="_blank">📅 20:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb4KMSUJwd-wQscTP9q9NLPCoZd_ql793RhH1tkoUMb239XPqxgZ8ePWF56Gb4AhmnoRM6CnaqYGhkqHnOsHy9I6tS3JuTDbmrYheTielTV_NRXjR-vhTXOkF-W6L6g7gQnaCaEDhNOKSAINpEjNPpkqBNC9reO3t6PRcmKoeBM5Qbs62pmvT836QMQyQA7RJkdVeWqnosLEs5d4o2glNIO7MwkPV1kPlGiJbAZ7ZNpfC6e3zmjCM6CjZ8kjlztUK7lemBy-Y-Nnem4Ieold5zCVjzuhBAm0hweJRQtdlE-Cn8VjS1_ogMDrv5YJItUIkA93kpfi2Vj-kMV-xuI7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبرتو کارلوس به طور رسمی اعلام کرد که به پیروان دین اسلام پیوسته و مسلمون شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82331" target="_blank">📅 20:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82330">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HZ6RAVBFB-HbDpmjxy3D7PfowOtIPT1HG1QT7P5UhhZ-QGZxlxbLycZjrTtEgn6Qd66_Z5xBW8Maky0P05Gq2_OGe607PUADzYYPZ10FzPdTZ52GvymJG19a4xNCDPsYAuadywRGnPS8SLILFU9gCFObw2Hr2cQozb3wPnlin-jh4U81yZRjSS-5PoDuwbkhsLk41-nOZMtV5cE2BOTjJva6-iY5gCqyy_m5zZ4aG4GWhHOw-d1nMzIGBrb9oP8s8nqraGDjI53qjLlLUq7TV6xBPvG4DiEwIyhohw5H6aV0RjpzADVDVm7YdBBJQ74to1lkVu3ZxKhYtzzG13AsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم بازا کجان؟! همه این پاسورا فقط 250 تومن
‼️
هرپاسوری که فکرشو بکنید رو ما داریم (بیش از ۲۰۰ مدل)
👀
تکی میخرید اما به قیمت عمده پرداخت میکنید چون مستقیم از وارد کننده میخرید
🛍
•
https://t.me/+5t_pd5JM8E0yZDA0
🔗
💬
مشاوره و ثبت سفارش
@Ad_Parsi</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82330" target="_blank">📅 19:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82328">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9efb4780b5.mp4?token=NgwlpMSacmVe6txSwLQDoRBfraXPVW6HX6itx1Z2Qqi95KmoIopUinw4os-lPCE5K2wg_35bymfIwWoNal66TkLr9YqDmxYmLL19d35aCs2nQrYhVZ4YpXa14YAy9-q2kQSegVtAsysovGFA93mP3EH8zbr2aB1METi4RTAfc9G2Uwv-fL9xzMCqxbcEJeR-Mj-HHxzlcWC5n-BubVu4JOBn5QFhSpDOEBx-yXlZMdhD8O7p5bZ6L6ENysIdBgrk8pBgMpcLuaWyDheb7cJcSR1dQK-5eDc125_gheffXekoZSe57tzbMdzJobaxhZoQp8ywgXeNtwtFmsKx7rAT-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9efb4780b5.mp4?token=NgwlpMSacmVe6txSwLQDoRBfraXPVW6HX6itx1Z2Qqi95KmoIopUinw4os-lPCE5K2wg_35bymfIwWoNal66TkLr9YqDmxYmLL19d35aCs2nQrYhVZ4YpXa14YAy9-q2kQSegVtAsysovGFA93mP3EH8zbr2aB1METi4RTAfc9G2Uwv-fL9xzMCqxbcEJeR-Mj-HHxzlcWC5n-BubVu4JOBn5QFhSpDOEBx-yXlZMdhD8O7p5bZ6L6ENysIdBgrk8pBgMpcLuaWyDheb7cJcSR1dQK-5eDc125_gheffXekoZSe57tzbMdzJobaxhZoQp8ywgXeNtwtFmsKx7rAT-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا بابکو که یادتون نرفته؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82328" target="_blank">📅 19:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82327">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvnoZ9L0oc6VBxCe20qQd4rhjhETVz4YRqPcDgysr5ji4tkT0drRpGdUTQuGiu9z2Ak8yCxEqQAuJsUvw5DWu4sX5jVJakKuBiNNOZCmGnn-TtGegX-youSzjyN6-WyfsFMVy5qHwjTsjm9TW8gCRJfvg20QFgJ25pYUJN0IB084jVNFVwJt8oKMWrSVLiHBCm5Ro-xCnDfJrtWWqgjLmV4WF6HDXM63a2B3Py6Fbjtc_oO2mY_m5zPLyik_-UEOgqB3YflWdNF1OjQKGjkZIb5eskijYCYZztKupK58xitfRtIBBUwA1ys9JUXU2vJPDfIJXYcn720v5aAZdagVrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای خدا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82327" target="_blank">📅 18:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82326">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9336e75d1.mp4?token=hyc1N5HZO9MCd9V8MvgwNRiUiyh6r-y34fmR9BsHlfkIzNndS71s8Xyp293jo-Pzx4VdC8ab-mJ3xOgUiF-12f_lPSgNUIgtZxkim82UgIcrzsdIvlBKAsN8hVrrqtl3V8CLKJb9cwy4iFQBbpe2F4Qu4M0J7gcAiCi5pTOvPrwNFkthtnap8j1vbklRrlLkPaO5bsTlEDlaV2jf_bD6AEO0pQ9TwjREiohAhZPgbfTBxfCorICooi3aHXYksHSI2nb8q3zN6x0BlxvF4jM-D5JkxpbvO6c0wtqyYdDJqroGzWznBtGXsg_8yvpox_IMt9NFbgz32GypAxLebdADoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9336e75d1.mp4?token=hyc1N5HZO9MCd9V8MvgwNRiUiyh6r-y34fmR9BsHlfkIzNndS71s8Xyp293jo-Pzx4VdC8ab-mJ3xOgUiF-12f_lPSgNUIgtZxkim82UgIcrzsdIvlBKAsN8hVrrqtl3V8CLKJb9cwy4iFQBbpe2F4Qu4M0J7gcAiCi5pTOvPrwNFkthtnap8j1vbklRrlLkPaO5bsTlEDlaV2jf_bD6AEO0pQ9TwjREiohAhZPgbfTBxfCorICooi3aHXYksHSI2nb8q3zN6x0BlxvF4jM-D5JkxpbvO6c0wtqyYdDJqroGzWznBtGXsg_8yvpox_IMt9NFbgz32GypAxLebdADoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ معلومه سگه پشماااااش ریخته
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82326" target="_blank">📅 17:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82324">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A0vYQZW5dj__5udcPjE-f6AftdUOXd-5mgcFbbC9PRA7QedEaa7M95zWCewJB7IUrNc74Y9o4cJtXCQKJU6KJNGNkuToIBg_vEAWi4EVBo54_bRRdpVuHPiedlBcIN6dtopanK1Iot20AeuZE8XFLrFplybG8E-tgljPAqNnPAk4t7Ep6pGA6dwBXi7tPBS_XCPAf-5KEIcE_R08rUBQhKmeetjVf8Sjxmv_UZ49pcZCJ5rfxxBZauX9CIJSKjiUlu2dp9roWkux_GJ0usbtZ88yhgj05Rlm2Q5vHUCX0Djbzxgf8tpvbLkPHqdX9N5Odk3HqCqKQI3nbwx5Z4dg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUoJp5Cuu67LmdQSaR4fi3nWIDmnMIY1TtK0_65eI_-hfHf4dxXm861bk9yxOS9yTKGstV0LR3oys-TXxXcLfJX-gkKl9wR-ZBPySwMQNskF3KWUSeFtuyhaEk3rWw1wYuAvEQzdhkMCRbIrJwHOJPVFGHiAgulqyZ7NMd0HFm8RjOomWLeVWx6NwcBkI8bUpElJljLdtI0wGDaSl6IqTTH2tJHAzQcA3aguJytcDLB_8TSOSnSoYlp7uixp8DqssOIWBf_VFME_Ax-vesMaFHgkME3bXKCkTuV2Nz5tiRN7COj_W-EZuiS5ObccR9DACocMqiLUDzE3kB-mBuLwOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جام‌جهانی با ما چه کرد.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82324" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82323">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRRRd-7r1RjC6YOaLW-sSFdjYPqT_pPCrkelCvrMF7BaxTM-4ic0SwandOuYea2PDrH40juAY7QwKw1KzO5UrCIN_JfpsOwAK6menFOrTie1a4LNj_2B7ZBtJppc5Gh0kGnjOhthJK6kWDWKXBNsB87Q8RM3XHKf9OyZycoSiFPxMUMozP5LZvZyv2Ay1DKon-2nnCjABk0jRRhgRwP5EvCD6bD-ZQo_8UDvKnfOkU-iWQlm5dh4HOQHAJsss40kulo_ZxIHQweTRV05TOvxRCZYBKid6Uk04iDR-OxoydZyZLZ9sJeyNtKaBxJcGXMyBPAqeSM-Rf17Tkj_cKaJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بلک‌جک زنده
🃏
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای بلک‌جک زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BJR20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r27
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82323" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82322">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شورای شهر تهران: به زودی اسم فرودگاه «مهرآباد» تهران رو به فرودگاه «شهید خامنه‌ای» تغییر میدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82322" target="_blank">📅 15:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82321">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">طبق تحقیقات جدید محققین، افراد باهوش هرگز ادمین فان هیپ هاپ نمیشوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82321" target="_blank">📅 14:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82320">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_6CZqdvAUSDYMIcnE0UTen9SPZD_JWtwFFnhNDNrftmh6iV34b1L9vdEPZ95EQNAez9PYn1GDE60f1qzSI2ApdkALJguar-3T3nCmHqI6Lc-SO-uh1ni9cPtKdYsXrjYFIkm1NgE1nsuglz9fLW0_5jaVskJYSDIVq_OwBOPgPOQ8sLzHnA81pDCgvYHiGiCg6Y-GFtSZqR8BbkzfIrvKUuBs3DLt93P0sxiqHo8GTgp7Gtwq04xbqUlGLL-PZjD2vZ7UrvleBjlGSgxeD-qgNFxhZ1V0J4npRIOo0LTNkIqU40QKCR_95HnLQWgK14Ek8I73cT1TS6WY2Hjy2RGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی کاپل هاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82320" target="_blank">📅 13:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82319">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwSRPI8lermKgF_VB9TidRfGLSdgxIBHsCYhlKKRJcvWsWPSu6pUWoeYkvxHw0frDIlOz3DMXXWHu_PwIsH-yG-cXfDGNmZ2s3oN0qD1eOyLnkGrY1XFjTLHwlEGYTrYq_laAvcGETeHtE9ExQvwx8g63d9fMdojtD1MB7cdlms0ebFNekcERwIsKD0Ub8cRr2psKOwUCE0IXszHgKy3q68yrjEaR0rE9APdCrAcFtvFrRJEtn1ujvdxbVK4qp3Y7OjbPYJebi4a9JjoltFMFNx47yVioUiooVQw4qmoYVkWHDCMlAofvIZoElcGG2yXRuJKg1H8Poi1eFw1f7MCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۸  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82319" target="_blank">📅 13:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82318">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombRoKe( Leandro Trossard)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0GKFfzm92i4nNKvKn3zoXZXCKrB0KWrKYAvxxU5YZHiZQIOdzCp-OoYuGMv6yx0UFrkx3UzepIx8HAKq08Meh6modf0U00xHUAqlBnn0X4BqvuD3iicCgPmdMaGp7cJC1xF_HAHnwh_fUBkJUQemWY_dPGEjB51IgM7GynYK4uHDAx9C_fJb-cfWd4A6HiZ6i9v6DyTbJCDpC2IdIlBO_2MbigFg3OXFwFi8QYqV3_xGnSDUVhFbYBt9k94a8io4aZl8wFZ9pjVqHTy4n73MVqwYHVMglTg2BJeRMZVg0tqbo9_zUk2GQeK89RSnw6Fgs--VzT1zmh0wK5I8r7-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت خرید کلمه (رونالدو) رو هم تایپ کنی نمیتونه بگیرتش
😂</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82318" target="_blank">📅 11:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82317">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr3C3DXkY_jt3nFROIAhEPwuXpK_V1FEQn_UYl0DXEOPAHgo7IdM68DSpDoiCdAzsEcpgVEvQ3FA8D4pLsK3DiJunKfVG10-W8-xA_JOa87rYCOLF6fOgkVQMrx9m0wjcQ9WPiNI62pmPSFn38M7yGnbThGbFuNc8BjKonQ3Wwk8zU7X34pARCnvQQQS-yVfJr4_kzpNOhtCnljfOI7h-UnTkZOtbY2yous9n2mn2cJU_QZ6Ag1bUqVganZ9jtVgMKW73PtqESaZa0VgoP84wcNAodluvA21pHaUaxb6b7VANa630b2bU__tRcar_P7hwSWSD9kDTUtMQmbMc_W9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت خرید کلمه «مادرید» رو کامنت کنید
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82317" target="_blank">📅 11:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82316">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSjh63P3HXHqarCUDEf5ltqJzA_OWJ6qgQqnO1lKekLB216u5BSxmeeOEdcFu4yQWRM7x18k40cCJV7YmvUjhNTWL4rjZ_o41EklNdldmM5Rj96HqgKYo1K6TPqylUZhTPPmKcA7S7ZEBAHb3KwmF5yj1za1ppyHQgbguLgYtZT7Kq8Y6CPD49Lt66Yc_gOdxngafQsZcww6SzSNjSo4qnVRJq-meca6VuOSYQdZzPvXF5Ku8g6pX4qRgQCrUyczdUoCWCIf-ymXyEd2eut6-J_ChuhBr-JA_8lq7GInuG9taUyUkuS9lQ6VmhgjGvFc1fGwOWoP1Rcf2KPaW6fl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بلک‌جک زنده
🃏
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای بلک‌جک زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BJR20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r27
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82316" target="_blank">📅 11:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82315">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترکوندی شیر
👇
🫵
🔥
🔥
ماشاالله شیر
👏
👏
👏
👏
و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82315" target="_blank">📅 10:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82314">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82314" target="_blank">📅 02:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82313">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ee8dd4d7.mp4?token=SsIeejTSeYnjjGhd0954-Xa3YK4iMLIVzpYu1G15QnRJpjv_rZfQPyNGqK0Iyc5Dh5aCQYlVhwty2gwKO9eWLbKN34k_cokNfIYkE77CjWnKAaCGE4r3zyllyDg0O2eRbJaF4gNbSDbvFAEAgCO851DUPwEviyPyeMeWftUVnwgSvbQ2v7gBYiZXEKMxaZ-xBq6XPrHNEV09vu_kPVIsvz-bwa3kzPrQ9kr85afTe3l2nWgBjGX4VSGcRvRkuAa03mFkR-jYutPNoIokr9V4a93Zh-LdzdwpClY_TYDnjE_Hw1xmZ10iheHupktJdnA4wsarCpkr5x7BYUTg4nT-kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ee8dd4d7.mp4?token=SsIeejTSeYnjjGhd0954-Xa3YK4iMLIVzpYu1G15QnRJpjv_rZfQPyNGqK0Iyc5Dh5aCQYlVhwty2gwKO9eWLbKN34k_cokNfIYkE77CjWnKAaCGE4r3zyllyDg0O2eRbJaF4gNbSDbvFAEAgCO851DUPwEviyPyeMeWftUVnwgSvbQ2v7gBYiZXEKMxaZ-xBq6XPrHNEV09vu_kPVIsvz-bwa3kzPrQ9kr85afTe3l2nWgBjGX4VSGcRvRkuAa03mFkR-jYutPNoIokr9V4a93Zh-LdzdwpClY_TYDnjE_Hw1xmZ10iheHupktJdnA4wsarCpkr5x7BYUTg4nT-kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما: ۸۱ میلیون تومن جمع شده برای کشتن ترامپ
ترامپ بفهمه براش ۴۳۳ دلار و ۴۰ سنت میخوان هزینه کنن برا کشتنش خودکشی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82313" target="_blank">📅 00:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X90-tRXFeHDfnYbUScso6vwXZ9YMYRhcJkugMDcwxleUYmvrAzF9rBW9GrVWC3tsVWaaC9ulOjF_IjVFbkMuvIqrPOr1uGAmne111PnqVEmAirrVflYlh-tWpmSUIISSuWuOrA2XBprIUDlOFevXBMtlR7gj97Yicbvk5E-3HnGZXl4cCrj_rPWzGKMsSJF5t9aNMNmhZ620aXFRBOmY8O8KR9K0AUnoWSnotkRNjEEgm1eK9Par0LeSeHWtQCmCvKy9K0eNtQkWypSlWgTLoUBXY8aEZJ3jTSQyszVWJ-9dbVlOhxFA4pqJNJ46jQwdiGcrPtjdmqyG8nWszADOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم جلوش شلوارک بپوشی بی احترامی برداشت میکنه میزاره میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82312" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رودری تو این جامعه ای که زندگی همه وابسته به فضای مجازیه هیچ پیج و اکانتی تو فضای مجازی نداره و هیچ فعالیتی نمیکنه توش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82311" target="_blank">📅 22:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWNc4akx9__SD7OKtEkLK7lnhUERiTFA8PRGuQwL8XcZkjBhaDu7z4_DN3RlADOV1dJEwdRZComFZKsFmOY6pqfYJXRk11dDNW2JDs3YoyDq3kZi71qkiyR8uUzVfnY8FyXq42WmBje790l3kzDcltRzEnmUvDlIIYGnF0qDyqY1wiioDnSlLSVZuaxgELTQW4dusQKBKiiPKKclboo8BFojyKQr4ud3wx0J66fBPI1d3B7HUjMf454yYr7QFAcblnEt6FzCMtezu0i2bCaBFA0aFKI674bXGqy2gR0IGNOD-1WzHdpWTT800Tkg5TQc74pwCcMPpUa7t978iz3IIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی همه جا مالباخته هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82310" target="_blank">📅 22:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82308">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGkRFSTckJhHcjD8rgBlCA28UiDyEGTY5o1UuuVOPERkm0XBkR-t6jW0aFoJP6P-63j7gOzVUa6aMqa89tTLQTADUJBbpnKqK4KUkhWMDH4g256Eb66Lckni_kElCDtiG6-TiEFIsB6GTPvZaLDpWF_021ppgrXe3Spqij5jcQO6fVoW5mV4rz8CjqcjdSZIrOXts5_o6w3t9zb5uC3CmQt4lSZcbMusKIWP1dwVpHW07TeDPLYpSGTzoufUyx79akqVB49_RP7JTpX37AKFMv53XAgsVZehH1r76ZIlGp1yCcQ8uG0tm9lIVmW4TiNxgFo8m_opte87cSYX1caG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtoyaKLBNHCLBCsnaPlFlPn38U6ZDnnCZ1qQs1-_aFPBxPnEAmpnRzZOykh70j0wIUpjOOLvPXOFw1YtyM5hYJ0AzCOuUfm3vM_O1cAyk90SJIjUmesGIv-CrDTs9ZiHnlwVou8zI2oar0u6rXyvUbEx5dXwGUHJe1GoKMR1ihC-55KLJ6-JQ0MGpI4E8ObhBTSpTHlTK3IIpQ9I94rKLErU_tMFvFVoD8-YIURM2JPwqtUvHE7glQyDAUPK5EjuvIWYii7iv8B_2EOTqFyQg5Vx1S5Qnz3V8av_VCKCzLoqjsQ8oX1ilHvBvHc05dGFmNR9wp9l2b2B-jhaRw29eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونفر تو عروسیشون خودشونو شبیه شرک و فیونا کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82308" target="_blank">📅 21:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82307">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اسرائیل مثل همیشه جنوب لبنان رو زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82307" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82306">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این چه دیس کصشریه کچی به خلسه داده  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82306" target="_blank">📅 19:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82305">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این چه دیس کصشریه کچی به خلسه داده
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82305" target="_blank">📅 18:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82304">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpOKMQVMt0LrgDRQCYpuyNHjuGhYgLiBSkhnWbN9ADb-GdEyd_bBiD-oMo6Joa9-EnUYIOu6GQlf2oLEkj9ewb_eWGpKSxXC5VrLCcwRvBGgk7dvZlIXSrzeYCEyiJz_cPt6sKDO5wRxRB6Zve9Ac3vSbjpMeQWBwhC5TaUMJ4CxQk7vOlAKDfwJA6viEIfv6WSand5r8e_5ZNKErpqXNDHYtdWA6FRYS5LKXDL-lLWzFjDSjJD1UYaogo2TuwD5B1IhQLChzZiMdQJEPOgSK4pfpxR3bqiWKf1kmc14gVThXrHvicuuPNZqOt6uJwoJ7hb8eYNUAyZfyT_CftnlYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لرا پرچم بالا
🔥
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/82304" target="_blank">📅 17:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82303">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U43yUw2lZrO049h75ILRynebMf-0_YTSJefbET1TTPJ6ddkzk93WiiAV0a-T8rs6emEsGqBm9_9vd_yp_0vTR3SFFPjQIIncolR3ATASIoB3B3kmdmXpF9pgReS0LFQzL8tPFlMynbVhyXO2iozrgzoZb_zVwfHss_zJOydD3a-q6oI8f9YkupcxusO3iMM1TSfnX3vFrKm360VsmN_CUs-fgJW-AzXfJEZwEc97_4PVrcofbiRu3XlnFJl4qjGj1qOFEMUl9NgrJB8H4kZBCK7x89h40nY5vkov9Xmf6m3-ADxHNJiI7Th8-IgSVpbStlii22ct7iJxj4-DHwyJaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تجهیزات و پوتین کماندو هایی که قراره جلوی مجهزترین و قویترین ارتش دنیا رو بگیرن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82303" target="_blank">📅 16:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82301">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=alJAgQKMHHCOiBXqtd9GaAlK5FVI79O1MmVrh7epJph0ycdjfCgJIEG4IEFuXc2YCQ3D-F60D4nnR_Joi2_soB2RDmB3MrM5TyT2y7WKQU1Qw0cpU3Pz1LgfsrQkqhOuV6njQMZOteinHFckrzsRCB_dZiHM1icgZJK6lMCrZV-Nw0AbSWgn8MK5BN6g2ZibsVnNqw8aWYR2XB1MHjKDbB6wPFlYPBAScyBYSVG0oKJ5PkNkOhXgomB4rIJullfq0WulQLVBi7DgiwvRdDRzpGqabl2G6-o4NS7OopMT7YJywxfG6vlBE_LnUNUDtGz9kCihvgFcOsxbl6vR3jsACQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=alJAgQKMHHCOiBXqtd9GaAlK5FVI79O1MmVrh7epJph0ycdjfCgJIEG4IEFuXc2YCQ3D-F60D4nnR_Joi2_soB2RDmB3MrM5TyT2y7WKQU1Qw0cpU3Pz1LgfsrQkqhOuV6njQMZOteinHFckrzsRCB_dZiHM1icgZJK6lMCrZV-Nw0AbSWgn8MK5BN6g2ZibsVnNqw8aWYR2XB1MHjKDbB6wPFlYPBAScyBYSVG0oKJ5PkNkOhXgomB4rIJullfq0WulQLVBi7DgiwvRdDRzpGqabl2G6-o4NS7OopMT7YJywxfG6vlBE_LnUNUDtGz9kCihvgFcOsxbl6vR3jsACQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صداوسیما یه برنامه جدید به اسم «با عرض معذرت» ساخته که توش ترامپ و اعضای کابینه دولتش رو مسخره میکنن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82301" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82300">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSr1d6IgSn_QRZ3V9AoWhy2FEocnLwtPSRTilkfFR7aj3aQ370953sBwFMxoGb0FlgrdLShsrHXIhK68J0xa2enaF7HoTz5i09Mnk3yHzMn8ew_4MbBmhNHEvSbnhSlpC0JEFyJe3CDr8yyz-ECWKNAvpjOxVxgTN5k0QrnS9uy7f1ICGDgygZirEE0YJxi4MUCeX6gIamr2d2tUvOBtqKDhpJ2NSAIN5o_syqP74bNftrUwjs7EBzJVTX9QSGHtuO0aebgXD13RdXNtLoxL7cQluN_0gvsIyot9lG2Y-fWKRt9_9eah3up9YQfueaEl0ArUqFLPWm1EdHedP-18fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r26
💻
@BetForward</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82300" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82299">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شایع این پست نوید محمدزاده رو لایک کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82299" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82298">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXCj9DdfAFa74AYGIxjNood2kvPCccnCBB8LBKh3-kWnTZcBgzPP2fTwpM8CEcNTpKK8KIMXTutJUYifJR6J3uxpOOwoBeJ2S6L6UUFsiFz8l895bOPcfg02fl7ecxkPwp-eXyZZyKVCe_j8SSG7psZAiUFWKZZ1fBBMTcATpeFsIoDGKMXQxK_5zixYHbBZ1cwPUyu0die73EvZpzs94Adi5WnksbPNVdtmPxNxakq2TmGNWY-Vch2OLXY3wlmfQt2hiLrXwfSy1T2fs5tInnttK7uGC0wPwUWfxSy7n4JkFwY4dZkVTIEb4z4iPNTiIo-8G8ihmpKsguDfOka7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82298" target="_blank">📅 15:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82297">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کار کنید حال کنید حال کنید کار کنید و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82297" target="_blank">📅 14:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82296">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFdQsOJrhmMV9lf2InJW-Y0cmVdCpfUjaXzq7kZtn0p9X9rzNMdxUm_7Mup4VTbR-68rpLhacMmne4Hx79hSqp15NLNB9Xanc6ciOgD_vkm4pqK3Ro-Uwq8xdbejIlLR7k-5DBQBx2k9edlRLhat__ebU9gdNI5aFTo2v7mR0CGPY_2p2de9r9B6qVnue8XmJjhspoy8TmXgkS_P6pgvzUgzAvJ4PlEbFK1prHYCoPdehOW7d8Y7cUViBWKA_iXHWwbt8h8llEHjexDnURNdzOu1reBxHzaImSSncdBdrrBF8LyNANfscnP6guVGOLKIMfcqMA0NIh6sNRGmLPhw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری الیگودرز لرستان، کف رودخونه رو آسفالت کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82296" target="_blank">📅 13:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82295">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJuJbHiTEDP20exeOYLv2hP5HZaGK9VZU_gjQ1rnuL5qfT1GsHhlotd3i-KBG-8MRHQdIJWktglzcN_jEVocdMVr0SwkQU8xUkwFDW52DqZJEv4fznL4tze7FywnG5quhiveyTo9bZHmmcp003CmaFGcUauYeevWLTq7rqyJUK7NqcCXahwSaBvZNnWZGlCybtwW15hOAR8OQw2h2amzkxZd9pFi0akSP313yq5FpO64Q4u3hbNNClZ3fJckPT9MJ7SL_x_LzJWQcZBYrSJeTpQ1z683evX5pRMjfOMYDYSQLnDxkjpQrJhUAsaectj4aUtGhGYJ5GFWA1IF2ehyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک میلیون نفر نوید محمدزاده رو انفالو کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82295" target="_blank">📅 12:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82294">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oytn90IOk4VDCcZ6DGhtT1ypckhZGmR0sPzU8jLwkUJd1iPjtSNAfbh3Oq-KPh7yLxW139_oEEsm--YpuhtuA-SacQznSOZalcnPlQm9Utz6PNA3Ey_wSNLlpAFpKM6ZVVpfzwY_IVpxg3xVhXSG-0X5qmtkctah4KRlOsk1QbmYZ9twIJ14pBdXdbLz6H6mSBkbQ08haVh6moY467v6EmMqbsNlBE0eGhPTe0VQothfamgsFTzHislst9dIgkkp8Vy2A191e9C8lAteSFhHpXoyOOdxQCJb1xp6NvSejZOVDM_3z40hCS1zUHmN9v6bYkUbnasg0MZxbeKpVLxA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82294" target="_blank">📅 10:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82293">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGIxG3nVZWs5OBy3cEvmbH9w_sSYr3_ECKqlAFRqbYGtWDzBjwXjBylxmmRd91fVyH46Drpj1VgmWSlVmU7f0BggmHlDMSvPIY4HaHuIT38bJeA3hCenkT-PFNESauBEdhgy00wb5ZAusmK-NAGVdnEHNtN_kQZYGr8VMqXpyNl66JOQBps3sB-FYDu3ZZFCYkjB5iAul1hcAVmsWNFGv2jSv-Qn3Au1mE2xAykkhKHd7PSuzAjNQB3l6RCAN7KkopvTpDo6Vr3TlUYr2ZLz1Xh6M4PiNXr25yCkacFKDpqVeUN6mbDZvKa2VPUf1KNkC61WjtD-GK-stRDHhEt7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو : احتمالاً این آخرین سال فوتبالی من خواهد بود و می‌خواهم میراثی فوق‌العاده از خودم به جا بگذارم.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82293" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82292">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6rNALfOM49Ws6Ywmo44a4TBfegb3d_IC3BVW6msQ1Yhy-Ap7xnEINj2MkX0eJA-EwQa83OIMlMm1Yy79fA1yJq4ZuV6QVo9ECVmnOqIkKAbI3wwCDOf9u8EJdfIPvfXMmCngzJ_b3Getao-3vddxBwXM-TI9hAXY-I5u5tVjNe7eTgGF624yz_trMdsGUg5oaxKfeSSpU_JZdMOWctzfxSPigjgv47JtP3wCxRE-OdDONdga5Pc3sSRkcdW2dkJLs6Vy_L9xtSTSvhI9Zjib_UvtZ7J3A2N3fflOi28Uy3BtFfcGH_3U7VE01ch2bRy9O5sOTyMP_pQuyRizb8gKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r26
💻
@BetForward</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82292" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82291">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82291" target="_blank">📅 02:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82290">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/82290" target="_blank">📅 02:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnYaHLHA2n8gfAYYhK-Dnv3ZadK3rmZNQi9oozYm1lSqgolCZhapKmzKfZJ9CRVFc0T9P6CDGF6WidM49iyE15haNnCUwgPa9FxX8f2JV8Z_0X6SwQwUpYgcV5FCTrqkSAgdGYvczvkOuUu5QREk7jm1DZO8pnPUDRLiN_hs1FwDmfRZmBpInJU27zIsNSThZjeN6kHPo_EYybPqX3uRSvH6GcS22xvnpEjnpqSN9EZmgyU0LXh_6eitGWSwCRmYjMNhKMPFkIZmkFlO3i-iaWYJOhaj4WjB9_Jrm7L50_0C_HdnwbDNpjvBQNL8tWK5uMfRSfp_YxGsbhnbsUes1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثرات تمرین با فران تورس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82289" target="_blank">📅 00:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">5 ساعت و 45 دقیقه دیگه آتش بس تموم میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82288" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHMc1UrI5X7Xog3VA_jqALTOtfX8QyVe_pxRPHM6qEdKZs_60DJ7Ubp-mp-42NNP6tCZFZZhBRfh6sw95ndDysrY9Xzx_LuAWsJFIYFBzq2N5mUcgmmb-CFd6qk7qaTvtPwMb4rsXNzGBGQwaxfvOqAm4u3LYgywUPaim-3X0DFpRPUo0kL5XBXdb1B9sSpdgXyQ6ckX7P70VKzND5bM7TQUQ226TAKb26-WyTLbvixG05NXVLTL23WQOn2CkIK6wPo-vBYNV-Q7Y9oESqxr5OhsaszuDu3mwX1k9I-oDxdM9Ys3DNpcKpdTWEBLI4v4fqL-gNKJbaniHhmjFCjE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی رو معرفی کنید که توانایی مقابله با این خط هافبک رو داشته باشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/82287" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82286">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzS3R2nW2e3iYegCNzfK0IBATzx44TEuRLr6-io5lzsFt-a9RMuyEBk3qRg--w7zVlinXsFSjPljuxs5wRm9SMrtUDzop1T0I7rHZy6627Ybcf3_BYvSC3DXd-Oo7-OwfoQs7xoL5roA3otfluLCL_rwq4qWbssoWY8y_kYMXMBC6pe-g-C2pbolrm39mi-e4bQvuuj2moQlf2ibpRBQm-BQgG4uWg4amKUyV6xA3pOZoZPBIDoMmVjF9Yl7qbfm1BdL17wLJNLMqh9sKSfECF1qTKeXQ3Rw-jKD6ncOXlK5DtHDsbht2TQlsSUzrZWs8JTbDFV0tsEm2Zrk2elcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیر وی گووو
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82286" target="_blank">📅 22:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82285">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRKtU30iW_9VzJECcRk-1chz4c8iwRvQ8due5c3bO8rmYFcniHR0bcntuAePnPfG__DBlRsCPMmsEdXMXlACOfzdmR3h-P6-mejwzaMMA_d6m-AYVdXvfKVN8gS0UJvGn-bMQngVrxTf45gFEoZozigpnpt4XhYlVwz7MLc3DkeIeYYLFZUDKjlfNwDhl2jKkDvGDn1qYOMSG_G1OLScxveYOJTmKGHra1lp5bb1kf_N8BqBO9c7L6ePe-5n-qfjDzL6dyyV9Qo_duIgqQYzF44V3KuBxE9kMrj9fEN_Y_Ha0Vl-BB2ry89Q3Y_27w46pq2HeT4-jIHbutOvxlQDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین تلاش های مردم برای حفط آبرو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82285" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82284">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=iIfL6fyHumSyb5HsrnjNQdE7z4DUFvLJJGKKibVzZjeU4NVP4vxicSvEc3RyLivzj4FBaoyajVtWCpufMoHKoLaqR-EgWv3QBeoFDHPVND0Ffq_5bFczdJGQVQKL0cgB0eZAjwh4Ys3GG9XBc7i07nrxDlA-A_N5dsgMUJHYTmAEwhdHq6hYiwsf1fleb-Xyy_iO7llbv0gKL6e5odmYppZqH9pO9pflny9W57NJx9_ttoWIlbvC740LQTU9_AcVhx3WDQKWfBMGcBu50Y2VMI_C1PuEpclNVZmMPXmDxRHKV7NcFEoocttmZCNA8to3HAFi01vSXVeEGJtDRtRt-FTOW517tDkUJwe8q5VvVgO7PuTkkUkw4YpGtIZkdVsOOsEBewMjtQpjl6Sk-wh0ybFpoZSb9IbBI79f_1gEwSFjQDwOfk-mspZaMI7fFoX96P_zh2qHXTeumUkgxPbZvLjGDDoBK_FkbOgMUh8oMNO5cb4JemQkESI3qnHzSCTJ8NC91LR4KJaQHccPwnjiqleDfMFxePGz4JLLo4r1k5YRyvwMpq3ygg2sm01R2q_YZq45MQkeQ0ECDOx6HJJmMgp2ulKf23ixzsdue1ymo2fwLjxc5E0Ufp_nS2oH8xbLP327vmpZ_oQWDyIj8EeG9qJ1JvpfEEHlX09ktOGcMfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=iIfL6fyHumSyb5HsrnjNQdE7z4DUFvLJJGKKibVzZjeU4NVP4vxicSvEc3RyLivzj4FBaoyajVtWCpufMoHKoLaqR-EgWv3QBeoFDHPVND0Ffq_5bFczdJGQVQKL0cgB0eZAjwh4Ys3GG9XBc7i07nrxDlA-A_N5dsgMUJHYTmAEwhdHq6hYiwsf1fleb-Xyy_iO7llbv0gKL6e5odmYppZqH9pO9pflny9W57NJx9_ttoWIlbvC740LQTU9_AcVhx3WDQKWfBMGcBu50Y2VMI_C1PuEpclNVZmMPXmDxRHKV7NcFEoocttmZCNA8to3HAFi01vSXVeEGJtDRtRt-FTOW517tDkUJwe8q5VvVgO7PuTkkUkw4YpGtIZkdVsOOsEBewMjtQpjl6Sk-wh0ybFpoZSb9IbBI79f_1gEwSFjQDwOfk-mspZaMI7fFoX96P_zh2qHXTeumUkgxPbZvLjGDDoBK_FkbOgMUh8oMNO5cb4JemQkESI3qnHzSCTJ8NC91LR4KJaQHccPwnjiqleDfMFxePGz4JLLo4r1k5YRyvwMpq3ygg2sm01R2q_YZq45MQkeQ0ECDOx6HJJmMgp2ulKf23ixzsdue1ymo2fwLjxc5E0Ufp_nS2oH8xbLP327vmpZ_oQWDyIj8EeG9qJ1JvpfEEHlX09ktOGcMfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو هفته پس از هجوم قبلی، دوباره هزاران مهاجر از مراکش سعی کردند وارد سئوتای اسپانیا شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82284" target="_blank">📅 21:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82282">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RScCBV2-N3sSMImoppH5la8DGfgFk9Lb9Ok_PsNJGT41AVeI8cJ6verMN5-hnCBaBdFS9y6xM-BfoUCSLG8_8h_qAUNT2898lDoUdx-3SddNo3HJR_LurVVSTIZhcXrpKNj7SOA6mnMDTP5kPtXHBF2o-K8AuNolGZrEUud2R75effEg1mykUPN9pww3OHaA6FWWUqhZRDdo88rju_6PPV_K3XQK19k_uqt1-Re0PE6LdxHWNpPVA4XHbevj4GaA0i2sMIiwJUPZOu0dvXc2zxwmDSRap8eCjXUeuUxlmtLzHSF_0xXCPSQ-VMPz5oe8mPEPQ8JHf_7ZYY2bDGTJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82282" target="_blank">📅 18:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82281">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82281" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
