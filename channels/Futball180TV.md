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
<img src="https://cdn5.telesco.pe/file/lPPj3Uz1NJAeVo7XfA9_dQ324LgY4skblKOo0iZHnkptENAGm9d90488XHip2pe6ZYtTSYVwO3IDZ4V_DwuR8NqrokR_Aug7WD-9lItvseMj42ahsSfhmQDEFnu7n8YIpxBJ-U7_GQj66FmBXMsrEgBPGqLQyuv1V3JxzmGZA6WHuGDYh3AcJW6gRnzzdToXnx0XOh3xk0EvDqOWlpgqDoTSG3SlTyLCn6GK32w53xBxdUzG42aPmEjIdIdD2TeALBOcRYKzBIN_tnS92CQirfuThXcZy9QZ2xULJjaZx-ILIkpY2jNMz0VK1HJ-Ff980GBezI7WabqgB0TXm-tJEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 529K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 02:57:18</div>
<hr>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMhu3IvJZ6TL2vLgS6xdQGJVR-o5qYkrtYPsCz9K-Qwqkk7CNQloQpuY_7c68xYMZLuGVgFAFmhyppp_D8lNvYWrU_xY0B2DZA3jgVWHAIAw8yVoQXgdnd7bvfJKSZ-fsyeQdyzdNYuG0VCzNxYUvQ8KX-Tf223amYE9gf0t3dmm1IzCjuM_2-TZEbkSmQbQwPrXnXFi2v3qlbPEDYlDPdYCXfSNu_A5skOTPgec-gfTwrlhnjuXVB9WfJjZTx7xuB8QRDkUE34RJ1E5bmuQMHvoAbg2TiHJjFCvlFs_T1wqj6yquZtv5rQk-OAh2ffj8g6jzMAMT1FwAsf-AAAwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu31rwu6K38vJ3loaDD8eyK2QWerOnDdmWPVSvc6w7tCihVOtzOGmh-8dskW1Qevw3lCXGbAITTO28hS1VncLYwDabyIlDcBp5lvrrvUMw0w-_D7MFboSQfjvqKT9uxzH0BGDbzQ5G-rNaFtV85ds68tiKOQdGVazm5yhD_8shp6HyrJLeWpPn-7UYP7mbARKKlniQIipjJsYCAjpDnk37_9K_srbMxJlKsD__RU7ahNI1bfsdlgRcYf-aPZReq3j61IujOvwO90vhvRFFX62_z1b_VauIBUbOtjjopH_jZOW7L9qt46rj-YPbNK_5lYgKZqM-l_IAk_f62zM2B8JcmF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu31rwu6K38vJ3loaDD8eyK2QWerOnDdmWPVSvc6w7tCihVOtzOGmh-8dskW1Qevw3lCXGbAITTO28hS1VncLYwDabyIlDcBp5lvrrvUMw0w-_D7MFboSQfjvqKT9uxzH0BGDbzQ5G-rNaFtV85ds68tiKOQdGVazm5yhD_8shp6HyrJLeWpPn-7UYP7mbARKKlniQIipjJsYCAjpDnk37_9K_srbMxJlKsD__RU7ahNI1bfsdlgRcYf-aPZReq3j61IujOvwO90vhvRFFX62_z1b_VauIBUbOtjjopH_jZOW7L9qt46rj-YPbNK_5lYgKZqM-l_IAk_f62zM2B8JcmF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRXZmpqtEDS3ZloMdGXANJh29Yvtuvu2Nb6Tybr_sDS-MFRqLfcs_Lqhb4EcGxaZLcnxZrkI8kVeaCFsLCaMTdep8FX4UckN3bmDMznDOlYw2WD-U1paK_JT5qVLkYHSj9YOq7PUkbrGtRB5oELO62hVm3YwNLjkCn-AtBrE_M_e1Tyx6kXng26USr9AaZlIymKOWam2Br0IOsUOAyjZmomerKfX3mEIYGp67oXsNFZi2bd_ks8Se--6Avt5spbHqyjglWoFJ7gYTFE6xa4FVQ-A0ly5FlTl2wsksBcZ--yg5bRRpnw75lfdi8ctthPP5L2zcIejY3rHKkGVMnpwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmyADtsAfEsQvxnbT0eEj5LxhHoLzslbggAPq-3fecjNEeQaXKdzQLSgZiGLBSO744z8f7edyu9KcKa6wGtyAvCpPjX8JP8XlK8_YpRqFK56ac5oKQLRPxS33r8EBvRDY53hYeSYMTI45z0pBe7toLs8etXCoYmoTcz5Otruw0pelNIrWvGKpEqdyE57NzdcPp7EBq7SVx9YETX1LqBiigMINLGhdvweJW_MYHagOye7c3c897pdNZtgODPSnX-qFP2Tt2HiFc1ADI-dw9h103BL6dg5g78P56Qc7vxSsgUmTV-MAnMoznuvQJewNutWNfAW9ti4vN1xIFOdGtqQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101950">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=Z4p0SpqqzCIxtsyXxypOVel9BjDLJ5u3PlIWD7JhNGEtUo-3q-6FIUAmqheGyS3GLBrYo6ehYovPntsTwW6oIYqKjnZVVaMK5KdMQ-YphE669SdgAFNEpw2zo6LuNbWc2fjXVjdO_NLndM_s_Lj8WAoGNjKk_vEYeesIzcPvHkI1vgZKUjD8u6F7vWCo7W8yEZM0XUWcjstGwGqwnFdypgoHhCl6HnBJIjN1NpDyCbGDyRI8l-8G8ANTVQ1D4SnTEsfngB2sW_8kkrYjNXQufL0y5IgR9_yyo_v9GU5WTvsjhx40HkB3DVwr17Hxyg9hZ_NLFnZx8VwkQoBjFACGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=Z4p0SpqqzCIxtsyXxypOVel9BjDLJ5u3PlIWD7JhNGEtUo-3q-6FIUAmqheGyS3GLBrYo6ehYovPntsTwW6oIYqKjnZVVaMK5KdMQ-YphE669SdgAFNEpw2zo6LuNbWc2fjXVjdO_NLndM_s_Lj8WAoGNjKk_vEYeesIzcPvHkI1vgZKUjD8u6F7vWCo7W8yEZM0XUWcjstGwGqwnFdypgoHhCl6HnBJIjN1NpDyCbGDyRI8l-8G8ANTVQ1D4SnTEsfngB2sW_8kkrYjNXQufL0y5IgR9_yyo_v9GU5WTvsjhx40HkB3DVwr17Hxyg9hZ_NLFnZx8VwkQoBjFACGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری‌اکشن هالند به میم هایی که ازش ساختن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/101950" target="_blank">📅 00:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101949">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8PqW72NY3VBer5XpgINkS0OGIqKSIoVrUYgAECOsGaofGMaSctMjYjadGlgLHaZJ-azmk7zigGzX9seVN0eUodJwhBd_SjyXUr2Ldr890VEK4JtquI8KFedTlj0onWTph8IkGHmSNor_iF_FPSoQ-HyminnVbGrHB_LhGXJaQBxUci7A5UZuO6ts2MBstCLGuZLavJJngHDkNbQyGSh8nPfU99pfACBonz3Ej33K8uzOjMgHo4qXDgzE5HsGtCoEVnSXtixVNwSAYuRNI8aoZpF8tQehl4AUz4-51DopWVIS8MUghsq12KtBpiY_FEtjzhVAq6kE-J8zqL3SR_n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101949" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iase3SUsnKF9pZK9CAR4mKw_WjXGXUqZfqs4NgEtpIga0eNdR-E7hRC2icmNbIhijB0sOZ6owOb1J9tkdSse_fQeIpIMIhAxCnS-nAAvVUSVAJCPoUmUtFmC-hVP78U9TanAMoFFzRHL5STJH5KzQX-QiWJeNww-M8yTyaJUP84DcFbR7bbwu9-KPfCx1OmQhu2KJK1oMtdjahrBRmLf5iuVfIiSVBRjTxlnjMngd73Ly89VTkQWdRhhy52Q8o1m1sHANTUK-Muf4Av9ONVtRNaVmwz7LkHsmPi-exwU5QeQGACMyuLUBrmKd9lXp7HrrOqRD_PZUI4_7Au03taVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری: باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه! اونا بودجه 350 میلیون دلاری برای نقل و انتقالات کنار گذاشتن و این تازه آغاز کار اوناست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj2jLjQTB8BAbMknf3BnvQ1HwnN4wFmcVTz7FQHvfszlArE0fE0O4MyETzoRCRbFoyV7lS4ScDv2XezmAXNYkByTmjo_OxCmpN6R8WxWV1VnCwG8IW9m_A8B0Zp3wvVld_btEpE8ovtbznRErSvLXZUzCoor0BQJvec1ytAs1_pH71ZMGakOnydz7YPNtpsjuyqkpp_9PDclBYiTRp_yiG_LEcgAiXfGXuMCm0M_MyHmVEQacrKheFD3VW3LKp9TQfEJmNMaRifISpZxcdA2HtbL13W2U-Cq72pVERMVqd2-jemfx3Q_xtj1j-WWxSaRrVusNBTE5GKEAuLvvjnBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIKUiVkg-nBAtrOrl-xkkim1iYVli_jEg1CDqO4P2cFe8ion9jZJPGK0xCUYE_q94EgWMvlsBY6TBVv1mefWDVetYhK2OI8EnflmyrM2bAlSPZBzeCWI6uirS5xSD64vefwA68u-SIApCg_FBcc6oxA2skDAwJuWCnCZ8N6hfEP53Ewp0WHz61MioOE6gRA3puQ9hTWt-gD3rlMOHoe7z9sPJiL18uPjIYoMFEriaxPLsmW9lZc4TuUen9RnnMfQEx4RPWdoSOr9-98uGBLiuu_M2m6PPfDfiLByLz9o73AbToGAC4djfrlWsi77K4FEcStz0UYL2UF2GgE5jfXsHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdSRXUeHFLHfSm42UAeEfXi_pixIRQz_HiVBja2x4g5QIpCTZsGNKPTQteS92dn3M8-ijQVKOS5GUj3Ov--X6lmzxCaInOmQzyVqMvcgoG1KjN75iXjyP556qlIVZl-p8IHKionGTX4mr-V2wu-IvOPtZSyCWwu0-NXnhW4Wf1Cjaejb4aTfeO-IXoaAy8iWUKJNg-mmn93hspcb-8RSGl_gBFMc0s-u8Nj5xLwvXYoHJA9uRgdcrVRav2R9VZBIaRlC5_IaHUE1eEMrmytSnU9sqPyMg9PMZjk4UrZAJb7WpzMKrqyhGlN49maj0vY9gin2fQqjy77oQMmK0C3I7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMEzxtJKITcaoaUwMjtBOl91qyEV_w_RPAnZacKMQcpQa0pyq2-021JnB9iu3c0p8HWLp_nZ0hzwleGY2GsfEF8gU91BufcG2MOT6PiwEElVLFrQ0Ta5OrFWD6Iol2w7fa5l0sMRS0OFqlIOsOh2qHCHtsxSB2FV8A8_6X_wwX8wbhyYlbnztcH5rbKghDJfIn_R5B4BvjN_hyo3MH29MncWYSae8cBLExORG2tgs6axQIaYxpQih12x8FAUBSMQUgMLwyxUiG7xFHviQF92g16Z3GLwdFBlSB5tU3gohpyL4k9GZXLYTJ9I0bMo7R9-EVKmeOdXfXxV6NQIL0b8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFLvfnMp_ZzSb-ksco28JdTzobhN1Qm_Uw2qBUCO1u9LqwvTYMRjRGClGHZW1hw4LrxJFZcoE_pv0TV7D9y3vuI6ZAQIGt9yjmt3qBWVWrEy1TeOPF_IoGk2-vQk2bqmVnYdya1PWTVo10EaBTjVKgKN1ObpZvEfzFHBPmVAtnFqCD5PM8_GswFfkColsx56ZWtqs8QvurnHF7XoqydNcPk4MiRGtltFFLFGNXOoW8_zyJwpLBDMKyDS2j_ti1pB2V9giVlV713Le7KmYKM60lVhnEyIdJILSAJ1qOTjXLtusMF5hPiTE4O3p1qPFY_pGwB3UtSvpleJVswW18dcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxl-Nd2vb8Ya9fphejAUbJIRRWnlcyemCHtQ1mvAsvvo55Mj_gIMvouIortVMLuDh5V8Ui4aOVjeD7YAOJEJYvBRU7TJe1UdKQW6LPxmOBZ0MsMjw3oCJhcf-DujOaxWO7MZ1NT6VbJyuW-GWpzSMuyUqpDVFgC7-iy2TUqN2aeQhwZzCJuAG57wnvy-E46oB2cDN270z-OPQ2it3AoY7Tuorbp17nAvJZ4OdOdZSbFvLv9CqNFAHtTuqfLtHR_SnFC6fgBtWjCTJmoGyKTi11G2P5Gfh6KXWjpW46173K6hegdyeCCWnFNaTyDnjL4coNwM6XObjT2Zq74Q5-_clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBn0SEq9Ptw84nduwkMrmcuqjfw8nOtcsxM_O3k6qMRzBkzt2q1ffntA1ahxVuUTFRCoANdEz0yw2FURDdRQppDzi-LiRlMg6k3NCYFau5FPIUvd7Zn-C71fT9sgCrExnv7rO-XFzoeL2XHc1JxytWh3mga9OLXSz2-x0reuJuSMW55ar_r0PyVH7fCtc3nOlasHIKfF7MZGQaNGrTgQdGzFxt5V7CifiVf6k5HVvWitSiNupIobtNN4JjjNQOOly8YXGEh6Fj4B85e4TBX-GyJhzNFIPSVREi0YKaoUqpYy6QTEdNFTWMYy7wv7rX_ooZCgG02HXf4NEXOk7IAlmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn2J9k4jI3P2DiRZ_pBfTxHEbarS7XX6jaMiyTok9RWI3LNyccvCwUIxRuPGo7Gy1DOme9SdcOJTccpxMI4Q7HGfRIOmksEWlfLkk5DLUi3Jd958GfFOxeCnhTiE9dimSk0iG1iiYLpPbmAFkSLXhbMi7xICKttgJTJ28QJ5UwuYgIJMhLjIz9ugYS4HdwMZZAlc8CnBjTD8wHNlRjUbmfYfA0wcvoxunauQimCh-GGmBRqs8eRp4jvKe4wPSRca-fYwLkZYg9JUXY2ImtxZy_dUhInXckXil2UX1BR9aQFqoUEDedi1Ueih_mF_qrdHTfig9Xx6cZlw8M6BkHNxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoFhAUEAdkGEwJHpsk2Yq1ZxcsR_-BuGe7TA3mSz6oMsaG6AcSVjPjRbCGhAWGxfWXylj9J_U6x-ZkJztCU5KSrDcYq_No4bijBRQY-dnD-_CvkRateLMG21-eEbXbnsaIxJ4kRIZf-xTV6bvE5BmxwG7noX3XeoQIFrr2c5cT2yO8LQeAerwTsZqsggrPQoYeKIecS1fU1aqzgIHpPuyR51rb1xJwDSexytFOGUPn5UdQWRJuih3q-WNN8Q3OzIisVaxRYQ77rB89PxNBtttfM6W_D0t7QrHVnVAMmleJHY0tgCGkefaOF7mhXZhXqntrSluNIyhURYxubY_WcgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TML8hGT-zVAnuZlZuC-KgH3hHOMrrSZM8VMG-18lm9v9hS-XaFz73F18umG92bRvrMox7tP8i4HJGdP3ARrX2HsHpH_zL6YfcDzXIu1NR1zkJO39DgYuIvSURpTzsTfwJLQjbtzJcGGM01NRLALoLqgsfsiAlAmeIFmZtPfs3ti38QTKeVKljCRbty2LHXY8BVjnS_sK-9U49R_u3brLAXgghIkz6vcSJJaIkb7NddobME3eSYeNYoqaiudgXG4xvOoto9VGV17FUoBnN7mzd3R9bbfIiPMafPRELLpOMM9F671yHQycxGN8vFxvCsvjNr7RCtOj8YEPeN27Rgzcqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4HstE1qMe-ptgh1q4IL-n2xHl5Yb4VSJ7oAzzGeFw5NDfk4EnKnLBMJn2CP5IDVKG6bEJzOjclEuxojiXw7JMiaamDHgjItp4XMU-9HvkJrtQvM4N7VNAa65N8ctQ8uENJt1AgMrvyJI0IT53Z-kdd01n--OD5SQXT2FkeMvPHb9b5LyNFu_rxZsyv_lSAU24dCPZjLhrD5MKGNe_GRhooegtyehtR-RA1bcdV0V_-L8jZtdDkAFMgvqbPkNelzY5Bn6Fv_eKD5zpR8YeYN_NSqC56sHqwyK8fJMmKKW76EqwSvsnAcO4-eyQjwrryRCtikDisRFzrIfmN0O81kkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFi9fi27CU7rxX3BN2Q2ycek2OQNVAiPSO32yU27aoCacVklg8Sy7NcEwFr7CAxwOFmpUwBV1AEIYWHm9yTbRHPpBO4mgDQofCAzM6999y4RzJvIke2_o80vGs9uXYMBPAboiXKQy2lb3j90kar4ommE2cX-VTfjBvoCGxV7rjvM5c5F-L-FDcb5CoEq84ao-xDrIsFGABG9-CJVGWkcgII-woWzUc0AAdAfg-OnQNZVj2VhFVKbQ_N9OVitT1cMWfPKPLDFestn3R5es5UwawxWS79q79X2xsi9dLZYgOQ4zGFnB4VQXz1PbofDvsWFH6f9Lx-o90rpez4GBcbJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUIG_lnhWsbFQbjy0CT7R8ps6irJ_61Cl5a8gGsM5Dgjsbowa3DSPqHLaXwvSnZ67zRwDZgDftX3nS_RnxNawuoJl5amiJV0x3N-SZMjQKl4uqr6-oc5inYR6l5Rg6ci88xa4hxrPvKHzFk3TUtPfS7k1MWG_ZgBQOv_zc1NUfcQivlvI6gi14zvm1Qmxdv0NnlIj7tj6qNtGA34YXWGIJkgewzmJye9l7eRex9_KvqXDsOz7sJek-628NFxCMWLY01R2mQ7t5W6DuhyC-ksRga8kwcUcYgkC75oDpw72uOuG3nI7L9unoNEcXgfmAuvzyM5EmmD0sOfmAtZzFs1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvwBT41ihk7qChGWBU7-py6l0CluTN0AwpqbhQHjRYqu396odHvO_yB2meowFAWhSSAGnKrvKIC0oEYtWKQXzcTDNJdIi94IJVGr0PdrHL3rmZapFx9AFRPmZunzs49NA1FAHHru-HFDr4i13TwUEv8yPrWyAqjlzKcs_44WGDRpz9R7idjUF2u9oXgdF-kg_WpND8wOic9YZjgMZkn2yQQ665_1zXSRCT6vhHyDiercLsHL1I567HK0UuePLuqiizf4MvKnHyYtguyi_abljnqxbaW0jpLvIBMjBDuCVJpC992dnlt66xxvvt988EXD_o8RFBiLNalFsUswTLF6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
کریستوف فرویند مدیر ورزشی بایرن مونیخ:
اولیسه به رئال مادرید؟ این موضوع اصلا برای ما مطرح نیست. او این فصل هم نقش مهمی در بایرن مونیخ ایفا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101934" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101932">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQn5CY9z63GkhJZyvs9NwuWnKgD83Abmqxb9S9WEKfpLDodLQN66SrcnsvenheOf50PGl7IwVtnkFloNLuaurK9fAfqTF9eu_OGr5jqicQWvbUPhgqjql0f4EE7epq0XhUBHg-4evvYF9bQHFsh_wgL1g4hBxanl1yCEYYAZ4mQKV8c2ciMylTQw2fOhMSO8T3Wn66xn_lAAyEUnh2DBVeQEtKBTZyV08YiLmBNdGUdHbkebJ8IyvC-D-U46ZEkxhloLa4ZdyPm-X2L35y7eMFQtE2BH9eWRYccyHS55Dhj9fTW35Z-RiAg-ODYIGy6iZMQiSSdDLwyjG-_nPmuPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkSQHHOyIPxM3ZdWPE4dcOhPAFNQY1eDHxNBu3oUXVsTe9z5t1_7itga7bEdcT-om28cQdvpwLvt3JOPdvJwhr5e-a1SFiZuQ_qVy94bplKmWAKZcRo8bPYOl37c0MxxI6zWumODSfKZvOiTIOYo9_USUnGlp3yhP2dXJmzRQ2XuNnuXmKy1PjO7ro-7YTORQ05pjkZbYUxC_a3YpV7AzNUZIReeF_15HhWq9FMsY9sYnRsHGYIzrL72yETewa18RcOMxelmxAtmrjy_QQhduqX9n5Gw0KidZ4A_X4rN7TrHFB6svYE12124uox79FSRbM0Yc-FkoVsxne9zqFhXRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcpiRRyF-9D607XaBEjMxecDH8HJMR0yvxh5--6YrEcrfPasOth880aZ_j4PEOSNjlpfHn5K9wKI60HdmpVYwrLUM_9zOABZos0SgS83FYGGY4gTUjG30b-GDhsYv6xm_Z1Y14Exgs7XDA2cmNZkJWHJxzyI7fxzlaac84mKfI5f_B_OgWeg4izQqBSWqfNwOtyQjcVDq1TzElnhMLt6UR1kl6lcOVngWNMgIkN_sUOS5UrvT7g0UXX95tMzRcrdqeivurgWSjZVf9sBe3rNFKWJ6L87Hva5z482qh0UsG0htYwPPh0ngcMoKmUTimTjND-6yYwIaBUPsbAu9C4Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=kjHJXSCz1GxNehkBFUkNlGxuznrmcB5gHemV6ttyuEv002CrD6EehbzMuZuiwq5AzAEFYFCBIsitP1RWSHk4AUJSt8v3lle5mnqHKakSHYoChTpuRQhW9hoK6PTLZUEBatPV97HUQitHWgUAWK2tvOWYiFoe2yzCxFz7Jjx2IYfDrfSk6_iA6nW82cfRlB52pBV4RuE4Y1XbwDqPnEMqKVjlHDLKGEa46EaryKG375TwIqP8ejiHgaDP7MeOvZ5DX1RBIQlK0F9YU6Vm5RRVjye4tbXEoi_9IXeiYe6dQu9X8hm8wP-aRqw0XkmWuW3ZAaGsohcKHcMuSIN4IgOZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=kjHJXSCz1GxNehkBFUkNlGxuznrmcB5gHemV6ttyuEv002CrD6EehbzMuZuiwq5AzAEFYFCBIsitP1RWSHk4AUJSt8v3lle5mnqHKakSHYoChTpuRQhW9hoK6PTLZUEBatPV97HUQitHWgUAWK2tvOWYiFoe2yzCxFz7Jjx2IYfDrfSk6_iA6nW82cfRlB52pBV4RuE4Y1XbwDqPnEMqKVjlHDLKGEa46EaryKG375TwIqP8ejiHgaDP7MeOvZ5DX1RBIQlK0F9YU6Vm5RRVjye4tbXEoi_9IXeiYe6dQu9X8hm8wP-aRqw0XkmWuW3ZAaGsohcKHcMuSIN4IgOZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برگام عجب سلیطه‌ایه این! اینس گارسیا دوست‌دختر یامال، بعد از موج انتقادهایی که به خاطر جدایی از دوست‌پسر سابقش گرفت، یه ویدیو منتشر کرد و گفت:
من به خاطر پول یا شهرت لامین باهاش وارد رابطه نشدم. خودم درآمد دارم. از وقتی با لامین وارد رابطه شدم، بیشتر از چیزی که اون برای من خریده، براش هدیه گرفتم. کلی وسیله گرون‌قیمت براش خریدم، ولی اون فقط یه جفت دمپایی برام گرفته که حتی ۷۵ دلار هم ارزش نداره! بعد هم برای اثبات حرفش، کتونی‌های گرونی که برای لامین خریده بود رو نشون داد و در کنارش دمپایی‌ای که لامین براش خریده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7ijrOIIB0qSUL-tnoZ4OZQKlEvtp1Ai8izcgCkaTlMwZJePRx2xDcVvHTl9U-wRPUp5vNext_ck7D-q1Pt9ctPUsiS6Ug2AkizylstoLXK3w0xbypL8hxsSGCXjnpugLOE_KOKYsvjxW-xdNCSl3P098dM92c-pNbeNjItMpkZRbC-uTkIU_m9SoZNKQaARc8R3QcEO3m2Horo4tJmzN4CgE0OwZPhpwWffmBTmUJ11ci4lKNcBZ91m6pN-fBkyKPekvzUEGjDaa3_CBmvRfpW9N3jMaXiwAlzA1tITtZQ0E5mFA89_jStGgBI0nifENOCtXkIO15Dp4KL1skhxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62941770b7.mp4?token=SrrVR2fiWe0A5B6-5CczB29RafVNeTkFOrjokdoqqPG2xR3rEguxzZJnhdMQVz6PDuLwmAozLGLt6HVlFEMt3wt4aesniQcqrQ3N3ZDitLyWNWfgEwDC0_pKpXGEBsmJjXXJYVvQvcGZBmSxzinWBGLEWUUumv7DR_PP-PmMe8xsmqYebFWfFshhKg09nqd2LuXT5q3ToB7TdblLnvGixPdWoAjgRnHkpFwsaGvLNas32Ga1dRfHtw_Y4otdDbynFa8WTQa6Nh2IPfPgKzrgDQi7BOI8oE7wUC3JpsIO6VVA2Raacsl89O5LTBkQfgc1XM9EZslhzrM_vv4u9Pvg6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62941770b7.mp4?token=SrrVR2fiWe0A5B6-5CczB29RafVNeTkFOrjokdoqqPG2xR3rEguxzZJnhdMQVz6PDuLwmAozLGLt6HVlFEMt3wt4aesniQcqrQ3N3ZDitLyWNWfgEwDC0_pKpXGEBsmJjXXJYVvQvcGZBmSxzinWBGLEWUUumv7DR_PP-PmMe8xsmqYebFWfFshhKg09nqd2LuXT5q3ToB7TdblLnvGixPdWoAjgRnHkpFwsaGvLNas32Ga1dRfHtw_Y4otdDbynFa8WTQa6Nh2IPfPgKzrgDQi7BOI8oE7wUC3JpsIO6VVA2Raacsl89O5LTBkQfgc1XM9EZslhzrM_vv4u9Pvg6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
استمرار، استمرار، استمرار تا رسیدن به هدف
این ذهنیت منحصربفرد ترین بازیکنیه که دنیای فوتبال به خودش دیده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101928" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101923">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9DXPPsX9-nhFiq_tuTISngjEMm1xB0qwdtJnQpojX9gU_5pJGc4aW9ZVzaMxss55ryz-leyiebfN2_xPrWWSxL5d5ctFnniBK_9Kq2cbTTMsEluldfOTGp6myIAhUzq7adYNOGCDx92EBWlVmcEiU-tQS2GF7kC7vt-Ziepi9kuTsa5PcvaktkBbXS7h7If1ww7noogf0MBBn9TeSmQhp6FGH9-zAbAbEmXALqLYEPk7TKbYmIMPvIo96XQAotSqESE1Ig71HF6iyNf3cpkNecTLaPys9n1u1QzurWn1yUT3qSNmgU32LBcgfWPNE9-etyX31CW_OisISmXaA9ncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q57m_-JKndkh2Yt0iivERluGF-t9KC661REe9iSbOqhrTfBy1TWxTdBNLb1Xhc7gzueCLppwa_jN7fv4JuBQSiMb9ybaS9oOHZSbsErnTdAtSDNIGbiqwpJBewyKRGT5aInhE31Yx5_OiByz0wNzZiIHOPANeLA4jsjns1psErsCdx8FxyINGibei7tmXPiQNxL3EfLxAthwSUhfBYVtQpiU05dgByV40suPSqXhgh-GoWOPg0NvHHj9HYSqUtophu6P29NBDrGfmy0_v3D3l4Xw1KBmBLCQ8-uxJq4bQciyKPfuIfN9ZC5PQiZWiXTII30OkfJkUbH-Tv0tlQ31Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8N-3yq6njXoPloKlKkxbAI7kH20VN5gRqn3VH5UpegweTQyh7eWURXp51Ff-hHE5FTYGzdyMJRHOjAFQq_cOmV8Ub2t8q7qUl9H0JJ3v8slrvzyz7rFwiSMRBVpRFzDPCdDCEXGxkwnyva4L1JntIY40W3b8t4d3PHmehuOej51BNfEEu0_L2xnnvZ39kP9p3k5X8pSP0pL2L3HgD3RI9BXmerb4d6kXMxjBzi0oY0xQNxiZxgQpJR4L8PmjYSNqcOZJ9_FIEWUPd9tanX3VgQQw3aKY40sv2pKa0pAv3sN_DwPgpqoEA7Bte0Wr4qGNkk5tlFmDlqY9eTcM7dJVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=vC7kjgsefKn3UwQd4kOaPYpRbwwwEolj-hdBMrgo7ZcT_PrSFiiBxRw0DNxGO4lWqEfljp1iBrLM1HTjwgXoem4QmEGB2TDIlKqMCdvAJXdLYDir9I-5vO-koN5gdnUJtyrJTk8cftPI9klC6JRPM0yC6X9uIo6MBPze-4iLqrAkPBgCktoEAIGoaG7gXm-ejr-1TVzvgcBAUt7pNTA2GV5BkdS-iNDm2AnUQFSYheOFXIvnfasdbNxhjxvpW2XXXY8UK49X2BC5U4GqN8-J6PfRKOYYisepD-gXQNLbwxDcDn9WtULaw1LaKU9p9ViOrof6IeVS-m79DYQAzlIReQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=vC7kjgsefKn3UwQd4kOaPYpRbwwwEolj-hdBMrgo7ZcT_PrSFiiBxRw0DNxGO4lWqEfljp1iBrLM1HTjwgXoem4QmEGB2TDIlKqMCdvAJXdLYDir9I-5vO-koN5gdnUJtyrJTk8cftPI9klC6JRPM0yC6X9uIo6MBPze-4iLqrAkPBgCktoEAIGoaG7gXm-ejr-1TVzvgcBAUt7pNTA2GV5BkdS-iNDm2AnUQFSYheOFXIvnfasdbNxhjxvpW2XXXY8UK49X2BC5U4GqN8-J6PfRKOYYisepD-gXQNLbwxDcDn9WtULaw1LaKU9p9ViOrof6IeVS-m79DYQAzlIReQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدری تو تعطیلات در چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwIKZZfQw6ZlxcqvU-vWh7J1vdlYbweOy9ne0t06mja-yuObonJQ9VFlQfSxDl5ZmJwPuR91foCr0uEgLlZMBjys83p4b2xV9BaISoCUfvaRk7QtkAX0fMcvUxXZG5wmmm2xPxezeaoWhm5BHSNvGNQ-IsLwB_hSentmj-DcWDVJ-1Q4bdOIgwvJN-bcwcOctuJlgHkS8L8Z7WCn_oLhzuhfK_3tPrIPokUGm7Q82_o8kaOCTa64sxa6g-2qlNfjrePv8u_1Oyh7vFcV_0RxF2AY78EpfGc05nmgyr6Fx3ALbhH7duXugRRCs-CzyYhqg2yoQrCDnNiavvTmPoyW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔥
همه مدل کیت فوتبالی فقط 570 تومن!
🔥
⚽️
از کلاسیک‌ترین کیت‌های نوستالژی تا جدیدترین کیت‌های باشگاهی و ملی دنیا با قیمتی که هیچ جا پیدا نمی‌کنی!
😮‍💨
❤️‍🔥
👕
کیفیت بالا
💰
قیمت مستقیم از تولیدکننده
🔥
تنوع فوق‌العاده از تیم‌های محبوب دنیا
✅
دارای نماد الکترونیک
✅
امکان خرید حضوری
🚚
ارسال سریع به سراسر کشور با کمترین هزینه
اگر عاشق فوتبال و استایل فوتبالی هستی، این فرصت رو از دست نده
👊
⚽️
💚
کانال تلگرام برای دیدن مدل‌ها و سفارش:
تخفیف  ویژه  برای سفارش از طرف ما
👇
👇
👇
عضورت در کانال
https://t.me/esportsofficiall</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=pKJZqjoovQnoHazJfoSlKmKAjHf6vlrerfXLwaM93Twv07VBKwvgmzYRlMvr8iWzvVSSlI_IwqqvVo7nmCWLLYO3AxB3Wj_AseyituTulp7qQfQEJdMVJUBJeteu2v9gg81JLVMta83TtvlXfVWAdcVXKk8Qre2kzbLpBX2W1QWGA9Un2GfGmckvvKMVOQ-avP8IpSX24kTJEAYM2bd8QtT25TDTpXCWSepUf7Kt781mV1ep4XXOK3omqgBdtxubNiIgtHeko772SBonBIte5vtse3qmafJrFzPq7DQfXNioz2TZsD1PqekYme89tl4_5CyKkKL1tJ-4wWHvpTq7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=pKJZqjoovQnoHazJfoSlKmKAjHf6vlrerfXLwaM93Twv07VBKwvgmzYRlMvr8iWzvVSSlI_IwqqvVo7nmCWLLYO3AxB3Wj_AseyituTulp7qQfQEJdMVJUBJeteu2v9gg81JLVMta83TtvlXfVWAdcVXKk8Qre2kzbLpBX2W1QWGA9Un2GfGmckvvKMVOQ-avP8IpSX24kTJEAYM2bd8QtT25TDTpXCWSepUf7Kt781mV1ep4XXOK3omqgBdtxubNiIgtHeko772SBonBIte5vtse3qmafJrFzPq7DQfXNioz2TZsD1PqekYme89tl4_5CyKkKL1tJ-4wWHvpTq7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
تو شیراز یه ایونت ورزشی برگزار کرده بودن که چهارتا کم عقل سر دختر دعواشون میشه و طوری همو میزننن که کم مونده بود بمیرن‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101921" target="_blank">📅 20:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101919">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFAWKlwoJxSnnSXqYpR9MVEh23_Va7uGWioCY36lmy68BhXLCYfltIs5nbKYTinfKbL9PL0LI-sW2iOUYsU5MXYYr5Xvqos6B3IQhl0wyFed5F8MWjUPQPdZuJBbUR3us-YTcDNJJuj1OZEPGx4_C2yDIYJ1a0s-1i93EkBr6RV6eUiQvLgnkXPPw81gkUn98r4k_uEQ1HFz0mspeGWj-Ni_IIvPmvUY5qxvm9pL5B6EVd2t65gLw5f1wyI_zQo11fMNmu9Nwfv3R14PbyP-mtNNR_DuCx1FqcrffQur3um9JxoThFoyEqbcFCeksL-wSLB2ZaEmJ3Aa54p9Zz8VwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2HWZSqxZbB2Ib7hbblAs-fkVE61DPvkAAGz3zSney1VJ6Ejw8MCAF-ysJc44Vf7sdSGzLeROTiZqTIZgw1DGCcFkrneF0H6vL94jlRgH3cd8r8ZnMlPReZ7yu6OXsYZCgKNtW4MTcNGcC3fX1t8MRkIGNvoDDPZPInM2DUCnzVWhNihMrJV-ImERfRqRlYopf29Z3oGwqmuriMrsH0-OSmkFdzGKh3sX-qS_eu9LjfrxpH8qGyiBOlLMLciumlwwZ1JpppJXpX734-BpHkMfpZjTEF4ie-wKOd71c2v4ZEeNwVdX-nbcbQn-emsOSpegTO6X8o8limq6PiJmr-d1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
فرناندو تورس یکی از آندرریتدترین فوتبالیست‌های تاریخه.
افتخاراتش شامل:
🏆
جام جهانی ۲۰۱۰
🇪🇺
یورو ۲۰۰۸
🇪🇺
یورو ۲۰۱۲
🇪🇺
لیگ قهرمانان اروپا ۲۰۱۲
🇪🇺
لیگ اروپا ۲۰۱۳
🇪🇺
لیگ اروپا ۲۰۱۸
🇬🇧
جام حذفی انگلیس ۲۰۱۲
خیلی‌ها دوران سخت اواخر دوران حرفه‌ای تورس رو به یاد میارن و تمام چیزهایی که به دست آورده بود رو فراموش می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeK5uHH6bN_pAFg5TH5iTj0huK1LQEGUOgiz_fMORhpnPhkWwcvuZ93pfz_O-hlSZqx5onYnFQ_v7M03xS5FjJhZfbZkfRQkRjTpQwlpKJ9mHIASt3ZNCnr0oG6c6nOthhftuUnUZpbs4YnexrhqEw6agxmtc5pbygeNZSHoSFp3DaRHIMB9lTxRLDtLNv4BdJVSQtLuksiqN27qgYXkWYoV666522R1zfTT9i7sUvP7zo3LjaVAmE5pxv9od7o-l6ySKgqNB4oGyEUwBZq-CGTBrw8WNY6uXArm2x0j3pWo_lDv9JclR-Cv0TVWVlRXgV7PffboARuXKF1Vh6ZnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای اسپورت:
هری کین بلافاصله پس از پایان تعطیلات تابستانی خود مذاکرات را برای تمدید قرارداد با بایرن مونیخ آغاز خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101918" target="_blank">📅 19:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101917">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/779a683584.mp4?token=ovi-nWRYCBil-Rm3eFO2d8P4GkICLkV4V0-sx3g_cXMXWo659JzkevhiL1O0JAD7rORsofhQ8zvhhou0VZX9yVXnsUlw8GZBif70z5j9Cy159RzSqK-mIwn7ENAjL60HJ5uggcaTCDZjl_o-xL0iTxzbHljJhXuBUejoT_dlKf2dDtVVQC5ih_GZ0-Q715imTU-limu4T9b0If8NtSexJsIoHju1zZhbO51nnIOI-MuRSqpZDds7l1bBwKVTaPeJGqPjE0EL1bodiTMM5gVskPsPCkMk4fQwwFEjsEfO0eYWn4UaD54dkRmF7dpyAltbhI5tZ1TKhCpzipWZWeEghA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/779a683584.mp4?token=ovi-nWRYCBil-Rm3eFO2d8P4GkICLkV4V0-sx3g_cXMXWo659JzkevhiL1O0JAD7rORsofhQ8zvhhou0VZX9yVXnsUlw8GZBif70z5j9Cy159RzSqK-mIwn7ENAjL60HJ5uggcaTCDZjl_o-xL0iTxzbHljJhXuBUejoT_dlKf2dDtVVQC5ih_GZ0-Q715imTU-limu4T9b0If8NtSexJsIoHju1zZhbO51nnIOI-MuRSqpZDds7l1bBwKVTaPeJGqPjE0EL1bodiTMM5gVskPsPCkMk4fQwwFEjsEfO0eYWn4UaD54dkRmF7dpyAltbhI5tZ1TKhCpzipWZWeEghA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
رونالدوی برزیلی سرعت یک وینگر، قدرت یک شماره ۹ و تکنیک یک بازی‌ساز رو همزمان داشت.
🇧🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101917" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101916">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=q31bdelCkmipcWHnqeziPbrUZHcjaN7g_2rgGTuNzyZx_abOWkpXH7Etg328L14neOgCw6I2aTHdJo0PCaZsg-upjZYsM7i9Sa5l-xJu4_Uxol5O1DgaDL7PfVakQey2atwBqBdebmy6S-SikkVekvPOQqau495L2lVfAkZyfP_uzTHAIGsqIhWwFIt93r_ht5n0MKmekhLU10yWSy2yd9veKckw30JO68S5TsM3vwPG6aTBP7lzbXSLUe5aISLuqI5JM1jcj4-AbSIaqxHJRj4xV4TxKGui_wirBh3GgJ6HDB4ErmH_BPys-C8LSurRds2aXcjuvBsO2nE7Qrs51S6UwaLXSFXAW-qlC3cGOx-0tSTTMaxWpO1EjOaKAUljQWR6P6Y6oeYlSNsO-TuxQzoACRsY4oesxtMmohBhnjX3ZIzjcMrds0Cxf3BzN7pui9tTmZ_lf99P9CwO13pLv4gTYC-PttNR_4u2q4Dv0TyCiQTxOgDTVw4D_mgbg7QDIfLnvnNlvK-XWVmqCQ5RD8IjTwfXqsuX1Njje64XZ0Wap9s2Cb3bRezq4EM9ef8IfNNxs6s3SFLM0JJQey2HcN-irOEcj3qy_JGc5bjem4CyAusxTGidAprFpWd1eTv_usbQ4FpRSJ9-FzOW2VnPxMfzUb-MmovcSKpkcz4WGeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=q31bdelCkmipcWHnqeziPbrUZHcjaN7g_2rgGTuNzyZx_abOWkpXH7Etg328L14neOgCw6I2aTHdJo0PCaZsg-upjZYsM7i9Sa5l-xJu4_Uxol5O1DgaDL7PfVakQey2atwBqBdebmy6S-SikkVekvPOQqau495L2lVfAkZyfP_uzTHAIGsqIhWwFIt93r_ht5n0MKmekhLU10yWSy2yd9veKckw30JO68S5TsM3vwPG6aTBP7lzbXSLUe5aISLuqI5JM1jcj4-AbSIaqxHJRj4xV4TxKGui_wirBh3GgJ6HDB4ErmH_BPys-C8LSurRds2aXcjuvBsO2nE7Qrs51S6UwaLXSFXAW-qlC3cGOx-0tSTTMaxWpO1EjOaKAUljQWR6P6Y6oeYlSNsO-TuxQzoACRsY4oesxtMmohBhnjX3ZIzjcMrds0Cxf3BzN7pui9tTmZ_lf99P9CwO13pLv4gTYC-PttNR_4u2q4Dv0TyCiQTxOgDTVw4D_mgbg7QDIfLnvnNlvK-XWVmqCQ5RD8IjTwfXqsuX1Njje64XZ0Wap9s2Cb3bRezq4EM9ef8IfNNxs6s3SFLM0JJQey2HcN-irOEcj3qy_JGc5bjem4CyAusxTGidAprFpWd1eTv_usbQ4FpRSJ9-FzOW2VnPxMfzUb-MmovcSKpkcz4WGeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یکی از مصاحبه‌های چندوقت پیش کریستیانو رونالدو که اون گفت او قصد نداره یک‌ روزی مربی بشه و بیشتر به مالکیت یک باشگاه فکر میکنه. او همچنین درباره اهمیت مراقبت از ستاره‌های جوانی مثل جود بلینگام و لامین یامال صحبت کرد و گفت باشگاه‌ها باید به رشد و آینده این بازیکنان توجه ویژه‌ای داشته باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101916" target="_blank">📅 19:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101914">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ew8LRBdjDJRBih0YLMrSM0PPVxYhN97h3GHPufx-CEZxITPN4KP2uCS9vY-dxeNiE2I05i18bN0ayZ0HHK4-rLBac3T7L8jcAulcv1FCRQI_BzHipVNtdZuKp4fDkHYJP6okMM1r_x1Lycy-PTjjonwO6z-gWFVsWG9FbUYe8Cxy0TV4ofRLORb4R5k_-M3gJMK0r5FJd_gRADZq8Gi3CtM_9MEwDKiH0pBsJu90vfcDX9XgSZWWQuZ9BgVUKnq_zmLnzfnaqL5Nj05LL0meEm3pVEvMNRBfhjCV6m7VU_Za_OnWg9eSgsdOY1LTk7uhALW6hNUwFE7cjrPQvr5Mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=IfQPdoMMSTIMq_228jG9pJ9OEwJ-7-Upixz8wIjW98KYmjE8Bjvf7EHSUEfNEHH-hSYS9UpB4OpnF3214p7OWZiV1avpPfrpnlMo9UseGckE-32qKCD4Hv8SyuqTRPGqIrGbo93yMXjo9Ddi-S2yZp0qfjdztTSoRWXQ5--QJZ_gZdqUnJqPZvQAIj75Tgzdl0xBpoqbzdjQmFcDep_q_2yM3G07xqe5m3muJ-pKXjYSNlmLvxkD4nlINXrQbidVYS5RE-lJdFFUTbEgUJ89LaEwZfDjbKv7ljdsTKBV4HwSL9VuSRwX1A-Xo46Gz6pHM8tBJFYkr3Rdk6I1VybP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=IfQPdoMMSTIMq_228jG9pJ9OEwJ-7-Upixz8wIjW98KYmjE8Bjvf7EHSUEfNEHH-hSYS9UpB4OpnF3214p7OWZiV1avpPfrpnlMo9UseGckE-32qKCD4Hv8SyuqTRPGqIrGbo93yMXjo9Ddi-S2yZp0qfjdztTSoRWXQ5--QJZ_gZdqUnJqPZvQAIj75Tgzdl0xBpoqbzdjQmFcDep_q_2yM3G07xqe5m3muJ-pKXjYSNlmLvxkD4nlINXrQbidVYS5RE-lJdFFUTbEgUJ89LaEwZfDjbKv7ljdsTKBV4HwSL9VuSRwX1A-Xo46Gz6pHM8tBJFYkr3Rdk6I1VybP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
طبق گزارش‌ها، لائورا ایگلسیاس، دوست‌دختر رودریگو دی‌پائول، گفته او حتی ۱۰ درصد توجهی که به لیونل مسی دارد را به او نمیدهد. او مدعی شده بعد از شکست در فینال جام جهانی، دی‌پائول دیگر حتی کنار او نخوابیده و رابطه‌شان به جایی رسیده که به فکر پایان دادن به آن است. گفته می‌شود او معتقد است دیگر بازگشتی در کار نخواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101914" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101913">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnmaMsfau34NSLn5E_Lp_j8ytqXOHGDe2AWV7X4SeLfJ4VQ3FM1aeOgfhi8PW9t6jSzVb8iiC1CxWPS3xcRTfoc0S6DC7FDgBq7_2tYT5fOOuGnFEMRXzyDMMKNyGDHonib0tcreHqUzDNn8WLLcqsw9GrswMbx3ZngerxC3DjKLYn1aU54JY9VUiqMjC15QsIrC80jdBcpY5iKcp9hPiZ4YS4cvn93xpsUH1HcaMuicx7tsU2RLID1iMde1BzXn8mULrr5073nJF8aj9MvdHncYz0Wj7IpkrCwzGeXc3ro2wKFv_w1up4Bk09aFXopnS4SSV-NY_WxP7AAxf3kL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
تلگراف: ژوزه مورینیو با انتقال وینیسیوس جونیور به آرسنال در این تابستون مخالفه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101913" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101911">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFdA8b3Hefx738vdL1zKfztwqC2xCOPNM-0sJm3Rnpi44ehXhD-l-UJVMc1ZAdTQP6roznOZb24E7Q3lh8gm6_yAF45kiWfxhaR8u7VsmNZM4_YpdWvGLz3eWOc1Zr_5EEeYlgl4viLVMAKauLcWZ7izGRANYYqOD6ZBC5pLpMFuLjGfNGJ_KKAea24c01526PHzZ7-T0_bat8_BjyTSh7vFQu6wXc73A5nvKMAXr-iw4ZrB8h3aLWQY2PY28q3ZLSUWtyCAGrrLqhnOwcqtEG_8MWtwttiMd6OY6YPP83U1Izmugyvug78tr3FgreY7MJ7l1wSFD4a5TGAo3bSosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4XM3UbR8c3rOT9CvPn7QtfiMzdMuxCe_i_ABB3tas-SEyimWjw8zXY5eCaPTXMzGkafNLudV1bowTZOjiVxtJjjoPQr9rF7z-uO6vVJbfT6ps6ALO8VNL2jE3Ybfm0YojCZK7eALuUZSf-3scETAX-R4y7mKy2N07UvXeJbbEhaz0X-lIYuf8C5kzUcr9IVVOSInAH4D2KfoUdT7nvyvz-MUo8YSCmo9DLbmld0-cvCogTRqxEkeyiIV4zPhE8pR_Zecw8x_PfjF_0NIfybIH7VHD1f5OI611sfxdg03avqxTJUCki-FWnMGMtgJc94_AAQjRLNx1ExC0TaPs61LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رامون آلوارز:
اگر انتقال رودری و دیومانده نهایی شود، رئال مادرید ۲۶ بازیکن در فهرست خود خواهد داشت. در این صورت، باشگاه مجبور خواهد شد حداقل یک بازیکن را از فهرست خود حذف کند تا با محدودیت تعداد بازیکنان مطابقت داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101911" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101910">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA8VGmVo04FkIskYstZSSnCWD0--kN6ZmJ8aVDz7z-Zi27f5m3XUgpmqzNjVoQyiyPGLSvbKB2_Jd41dsV7MbjTbFgDETBCzqD4_zwkq1grtckJ01txno0iYKpic59S7SdW1bTo3GiTcrUA2wL6ZDPtc_yjPe6sKskxwIzoL5nXYiJTiK0vqiaRC8PCOB92JVsONOGsXn9BaKiln5_mvtvsYG9C-OQl47S8Q_hxW4cKergzoeNjnAXy_4HCWsA1STxt8it9v3M9ON99jPOZz3ZWba3xiC-SRRe_PnSpwMvMORPF7sMmBpzD_eKw5X60mdDP6QFw41vDcyhBdzyK4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ربات هوشمند تهران پی تو ۳۰ ثانیه خرید کن
😍
فروش یووچر، استارز و تلگرام پریمیوم بدون احراز هویت و ثبت نام.
تحویل فوری زیر ۳۰ ثانیه.
درگاه رسمی بانکی و مجوز فعالیت
✅
@Tehranpay_bot
@Tehranpay_bot
همین الان استارت بزن و راحت خرید کن
تلگرام استارز با ۴۰ درصد تخفیف
😍
یا داخل سایت رسمی بخر
🔽
https://tehranpay.net/utopia/</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101910" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101907">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2UMPqzQcX9G0WxnsKTvxWSpAD3YeBG3hFBrD-wCDRPbd1ovBYiOgP2Uwnzjpi5rkM5qQzIzwUsjogdVITem4zSkK0nk0fQqLzs3QyaufXpxiQ52qMzXmHwh2neTWYzPFeGPzFRN-cqH1pHEvY1iwUBv9tqkz4j3LII_GMhLfdm0NQDa5-phfJ9UAgD2yC3nVmAY8LQtVhKtyEqISZ7kF9sKelaRm1liWpB8ntoUPy9DqjLtsiztoJDan55r5RPbfB_kRmje4UITyEE5LTC7KkolCR1blag6j1_KjLci53kR9JPcw9mayRIEPieOrjLc4pzjAIZA4ZLAU0vwMuMgSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5ZuhN5DYHWv1HZfrC6621cLuMe6tKZDlc5fR8gyTZuEXuDJWm22FJuXJhwS__zykYjT7Ta2TpPKg-YgiDiL6uGgctNN5OjIUfIMoHfhCdRJLVQf5tzihHPbffZVdZMp-fFhQIkJPZziN26MyQJ8krOUi-xD4fDF57-lHXlzYMJP6Ma8lxIk28oMC9lMVHGRvlMd-zY9D3Uj8U_uXN6KoJ7-W6vR_i9Nerkzmu0DkPaXA5YOMZ6ZK5rqn3XMfd8ARUjj41qTVUA3sjvqTAUSxGP6PKFaOQmPOQbgkZXDPgPOYrtu1jUedsK4OerCrk66o8f8CAsh1uoLm2QCG75qDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=YeMLdfS92PUgueiTem9RwtY3tzOWje4r0QxVZppBmBLERzEIPPf3ef0rReXMZedwDl5G8W4rpuJTfjAvNvzjUBlJ1HaO0TbY-TtZ6QYWHFrgse_1buKYv6yXJ1oUAcQ5BLCvybo-TrFzXNTvRs0zwB_1ypKWFbs3WIC35lTaim4BrRNZAiVPFxnJLjFd0T2hF80k2bkqMWH1flcwC8peyGUE4k01iKDNb6i3iax84Xai0TOxcAKBZPvNXYZjsMd-uCqgV5DUy7QKxOc146T2Ov010tik4j3bT60em96mBSTzwa38mY_pspjY-pWnCGjAsx1rN3E4HttMFvqXmUbJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=YeMLdfS92PUgueiTem9RwtY3tzOWje4r0QxVZppBmBLERzEIPPf3ef0rReXMZedwDl5G8W4rpuJTfjAvNvzjUBlJ1HaO0TbY-TtZ6QYWHFrgse_1buKYv6yXJ1oUAcQ5BLCvybo-TrFzXNTvRs0zwB_1ypKWFbs3WIC35lTaim4BrRNZAiVPFxnJLjFd0T2hF80k2bkqMWH1flcwC8peyGUE4k01iKDNb6i3iax84Xai0TOxcAKBZPvNXYZjsMd-uCqgV5DUy7QKxOc146T2Ov010tik4j3bT60em96mBSTzwa38mY_pspjY-pWnCGjAsx1rN3E4HttMFvqXmUbJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
رودری درباره جنجال‌های جوایز فردی‌اش:
فهمیدم مهم نیست چه چیزی به دست بیارم، همیشه یه عده هستن که میگن بازیکن دیگه‌ای شایسته‌تر بوده. وقتی توپ طلا رو بردم گفتن وینیسیوس باید می‌برد، حالا که توپ طلای جام جهانی رو گرفتم میگن باید به مسی می‌رسید. این بخشی از فوتباله. به نظرات مردم احترام میذارم؛ مسی و وینیسیوس بازیکنان بزرگی هستن و مقایسه شدن با اون‌ها خودش افتخاره. اما بابت جوایزی که با سال‌ها تلاش، فداکاری و ثبات به دست آوردم عذرخواهی نمیکنم. هیچ‌کس نمیتونه ارزش زحماتی که کشیدم رو زیر سوال ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101907" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101906">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=cvUlv03Mm4N8rH8YXKUy3JYgVSjCjkDhEKImhkPdRaiYOInt0yJ7i-4iBo1vQFk2xfFnp0sVn-D_WAnaqdnofHM9JT0C-41t2a-JXYGSLW7nOdWeOsPkaXjumgZ7yJdYrFio0qA_TAEpQWdD1MQf1I2qZC8NRPZhBig7hssmOe3Y5khrKbjJSsQQofSPwXeZqfx4eQn7QLkRK9cXCcNdc8a_yIe637DunRw8tIORlXs7sY87PUYw5wb2fgrUNwXt5QLjSVMtuXdFgkzjUedaVVh3fFJrrwI2Qfm_gxC14-xlBshi2dQGuMdcXzyDW7crL-MF04Pl69qQMcL9W8acfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=cvUlv03Mm4N8rH8YXKUy3JYgVSjCjkDhEKImhkPdRaiYOInt0yJ7i-4iBo1vQFk2xfFnp0sVn-D_WAnaqdnofHM9JT0C-41t2a-JXYGSLW7nOdWeOsPkaXjumgZ7yJdYrFio0qA_TAEpQWdD1MQf1I2qZC8NRPZhBig7hssmOe3Y5khrKbjJSsQQofSPwXeZqfx4eQn7QLkRK9cXCcNdc8a_yIe637DunRw8tIORlXs7sY87PUYw5wb2fgrUNwXt5QLjSVMtuXdFgkzjUedaVVh3fFJrrwI2Qfm_gxC14-xlBshi2dQGuMdcXzyDW7crL-MF04Pl69qQMcL9W8acfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
حالا که اینقدر امروز دربارش صحبت شده یه کم یان دیومانده ببینیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101906" target="_blank">📅 18:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101905">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=NYz2kyDRSRBU2EPJlyZiWCr61qSMNz9BzpJ1vcOM-3RjzQvi4rXAe1mikIG3yf7U1K7Fi99BGZb4gM5Y_-FvRE2y9yMNvwKBdL2qgLhmaGqcOtAADiNt_0-DFOm2Tl8rhDsAV6ncDmOU4aVymlqFNA_BKvYcOyknozTYPxmLgrxq5Uyau5VSBJAM-C0qSExX1p9niyFVVwOGXwfxj_emiBMrej6inRafYi0BYWuwdikjSZbln_a7YsTWVmIIqw8b6w9N8hjYHvN6qqDyhDyG0kpl1cCILmGbEvc9kklwht3hsui-a21C0--lmu2DgbsKGHJSNspttbPPv9qRLSoHcbC5cqVPHK6c-7KZjPPIJuvviG8N6CBNHxdU8VFMX15LUUMot6Yai2rOXWRy17zv06FkLRsP9488J8fR4EqikkP9urwQ7y368m6-0-JXZwlNy95D5zOe1VxGJx2hV11OeRIU3V0Y-XfpsX1TymqHnmTkEmfApnQPUSXw_nozE43_NY2JKvCn5ISfLOwFV0zsQ2fGAuMtwUZp0VJRe4_VVGFFQmvXBVysy4VJD7djDW4oO1y4dbclfBBwvbSX-BMW6gC0d_joGSMTXdjoZvcm87bqpW6dRs5187915HMyDnsb8XvLaHrSIEhuEnIdS1aTctzcvKQ-eHiF4IkjhiE7iDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=NYz2kyDRSRBU2EPJlyZiWCr61qSMNz9BzpJ1vcOM-3RjzQvi4rXAe1mikIG3yf7U1K7Fi99BGZb4gM5Y_-FvRE2y9yMNvwKBdL2qgLhmaGqcOtAADiNt_0-DFOm2Tl8rhDsAV6ncDmOU4aVymlqFNA_BKvYcOyknozTYPxmLgrxq5Uyau5VSBJAM-C0qSExX1p9niyFVVwOGXwfxj_emiBMrej6inRafYi0BYWuwdikjSZbln_a7YsTWVmIIqw8b6w9N8hjYHvN6qqDyhDyG0kpl1cCILmGbEvc9kklwht3hsui-a21C0--lmu2DgbsKGHJSNspttbPPv9qRLSoHcbC5cqVPHK6c-7KZjPPIJuvviG8N6CBNHxdU8VFMX15LUUMot6Yai2rOXWRy17zv06FkLRsP9488J8fR4EqikkP9urwQ7y368m6-0-JXZwlNy95D5zOe1VxGJx2hV11OeRIU3V0Y-XfpsX1TymqHnmTkEmfApnQPUSXw_nozE43_NY2JKvCn5ISfLOwFV0zsQ2fGAuMtwUZp0VJRe4_VVGFFQmvXBVysy4VJD7djDW4oO1y4dbclfBBwvbSX-BMW6gC0d_joGSMTXdjoZvcm87bqpW6dRs5187915HMyDnsb8XvLaHrSIEhuEnIdS1aTctzcvKQ-eHiF4IkjhiE7iDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تیم رئال مادرید در دوران پرایم خودش یه شاهکار واقعی بود؛ به طوری که تقریبا هر بازیکنی، کاپیتان تیم ملی خود بود.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101905" target="_blank">📅 18:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101903">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omJX3lFboG81YuLydPBGk2Tgj1PA8nh0npxlB7KsTiJfN9pSvj17spyraIKmSgtLKhMAzWvfWc7E-cQ4KSWK95z2SCdZUODsNVPj85N4y_G2aX-bc2PEh_q6rxS3_55zeFQ8_YhrmMgtCBqiJucsRfXs8Z_vqwbZ_kUvKi-ngC_5Z-cLGco-jdYWhzBaQCahzN1huMgz9SnGylJWicMAwl3W41_nd8VQB5UzqU_DgighSLj6Wjeo7E8vYNrxk5zMUBlkrCvFwfHO0h1z0gzxv8znpeVgWdISeqA7RaZWj5HySfm7b8GqqCrUBuOGTPhU4DF1-q6QocoNpl2zLualqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
کاکا درباره دوران سختش در رئال مادرید:
من از میلان آمدم تا بهترین بازیکن جهان شوم، اما مصدومیت‌ها و رقابت با بازیکنانی مثل کریستیانو، بنزما، اوزیل و دی‌ماریا باعث شد کمتر بازی کنم. حتی امروز بعضی‌ها من را یکی از بدترین خریدهای رئال می‌دانند. اما آن دوران باعث شد خود واقعی‌ام را بشناسم. کاکا می‌گوید نه بهترین بازیکن جهان است و نه بدترین خرید؛ بلکه همان سختی‌ها او را به انسانی که امروز هست تبدیل کرد. فلورنتینو پرز هم هنگام جدایی از حرفه‌ای‌گری و شخصیت او تمجید کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101903" target="_blank">📅 18:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101901">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RC_UBvLISNs2SuReDwlNZONYpFzAbfzHHUzv1tPcN-AX7pOWdor-eDrltjbu3irHZVIwMhAB7xK12qQ6eBhVOBlYIjOHeKuRaURh-92tOhWUw2IyTlbqDKsf_HihjgMQdWJFFO86tALZFsnnuV67eo6p3RWVLnp4sMuXYfHDPbnk-0DsW6jkfptW9FotFm2irg5I8Cjgkdy3QJ3DOoXIqlkcFmVuU96tVdcmawAf0LIVFPwP_K3_jPTfI4EA1DiE7G4761y2cjF3HeoI8NECWWSnTUdUJxIlwEQiUXlB1PfSxzGPXCnOGCHqQO3cKmOnQQff4jh4Fu3h0jSSSt8MVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3U8DJXi2uSXpiSiN8MvvkqwapfLW0PUEydmiETQhauWV9C_l88EJB5Vl76vT-xyj82OTD9dJlYFN2B_F4qcLCdPE7bTel__U-UD1S9NDUyb2VtC0slODjcN7eILN_s6Ye-fq7MqpZbCPcy5whnvMbAjTO9c36aarATKnKmzJGj8uOpcRHWsHtWTX4FBHgE-9A13c1oQbkbcZlj0ujvR0x_MBo-XUW_wEav6YiXdLr_kPP9XGIVPUB_wmteko6tIkJ9XwzfGRpyZCrIS7jKFkYkcm8mg0kBvcAJJ9Xw0CYNe3JpW1wwNZ8oTkWNBrCtVpjsAMmNAkLmeweudkVDsQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یان دیومانده درباره گرفتن یک پیراهن تقلبی کریستیانو رونالدو در منچستریونایتد به عنوان اولین هدیه تولدش:
اولین هدیه تولدم یک پیراهن منچستریونایتد بود. توان خرید پیراهنی با اسم بازیکن را نداشتیم، برای همین کاملا ساده بود. خودم با ماژیک مشکی پشتش نوشتم "کریستیانو رونالدو" و شماره ۷ را هم اضافه کردم، چون می‌خواستم به خودم انگیزه بدهم. هر بار آن پیراهن را می‌پوشیدم، تصور می‌کردم خود رونالدو هستم. فقط می‌خواستم از همه بازیکنان دریبل بزنم و تا جای ممکن گل بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101901" target="_blank">📅 17:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101900">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=PoqZWvetHrC-OxGVIEVQxhr1oggBAswSm9kvJAGQFQS7_aaYtEN2UL619MNa0rs1zxNOOTdaoOnEWZL9-VRTQ8soYgepepJKDPSuMKypowj0S8EDm4eajWcimVFTkyt3LkuKsd73TNovUEf7uDQRuuhq0WN_N7g2I8lu7lehvnIH8LYH16klufJF48fl4StuoJyHouAfrU7g_Rpy6a0qx34F3kfu-shPR-UnmqZjy8N-sEVT0DVW0Fnn4FTKE45OUGo59ZNlPuMfrtrGOhJfQyZAJ4meWXCCEXEdbEgZcTmRGiLF1lBkBpL4QfeP7tyUUt0bBU42evuHo6RkRMU4wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=PoqZWvetHrC-OxGVIEVQxhr1oggBAswSm9kvJAGQFQS7_aaYtEN2UL619MNa0rs1zxNOOTdaoOnEWZL9-VRTQ8soYgepepJKDPSuMKypowj0S8EDm4eajWcimVFTkyt3LkuKsd73TNovUEf7uDQRuuhq0WN_N7g2I8lu7lehvnIH8LYH16klufJF48fl4StuoJyHouAfrU7g_Rpy6a0qx34F3kfu-shPR-UnmqZjy8N-sEVT0DVW0Fnn4FTKE45OUGo59ZNlPuMfrtrGOhJfQyZAJ4meWXCCEXEdbEgZcTmRGiLF1lBkBpL4QfeP7tyUUt0bBU42evuHo6RkRMU4wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فران تورس تو تعطیلات در کنار بکهام و مایکل جردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101900" target="_blank">📅 17:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101899">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=gQhmryUKicQDxJtvLMcK6T3VCvSb55OIcVkWmbf6DXHDZZPQxlDYQYGzmMthTbHcARCqoM3CyO_8QbaY4flTTfPyny-EO8LYjunSbRO8tba59kfcgBw9tyMAUqJnISU8f_OkN4p1mKQ4-B1_UEo3UmhBNqf6VteoDB26NyClnnLJyHrLMB3_tqpch0GHe8OFnQt4q4gtimqRqapTgixdqmUSXg6scSS1kkqR1P4iUH7X35BYp7fxO_z70OTNRyp6Ir_Czn9tDTvftEQUx376Bx2QHptorct3fypvt86yi9Qz7h1kAxrVxSqSrZ4SniKhWKNSgIYGkV25w0_R58s2ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=gQhmryUKicQDxJtvLMcK6T3VCvSb55OIcVkWmbf6DXHDZZPQxlDYQYGzmMthTbHcARCqoM3CyO_8QbaY4flTTfPyny-EO8LYjunSbRO8tba59kfcgBw9tyMAUqJnISU8f_OkN4p1mKQ4-B1_UEo3UmhBNqf6VteoDB26NyClnnLJyHrLMB3_tqpch0GHe8OFnQt4q4gtimqRqapTgixdqmUSXg6scSS1kkqR1P4iUH7X35BYp7fxO_z70OTNRyp6Ir_Czn9tDTvftEQUx376Bx2QHptorct3fypvt86yi9Qz7h1kAxrVxSqSrZ4SniKhWKNSgIYGkV25w0_R58s2ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش داره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101899" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101898">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=rY-bkeWFYmuYTUYqIg-40whd3pRZC7AzmuwIRF-6xrtmXmPvvYVJYqW97WWPnk8ZQeKoKvOohWtFyNOUHtb9bfZ7ILdLIsjvSNb-8uT9gqkjkpOLbLYTRMYJpmd0a8Kw9ZdJ0tOisbAnqF6KRioIU5vKUBvro7VR_7VHctfjS4mmCfDD1KVHyRBDDy1oo-pxRUqwei1ZgqnSi4244DXrQuo-7P4eXt-M75Wp8lGVOd-B71TrgTEHbcqh6vDTYkhza2ak6k-rP-0tF1BYso3Tm92_o44Gce-axdE5D_1VDoOV5yIIW80NaDld2sFbPgtT-j8hub-Hnx3RFgPBXF3Qig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=rY-bkeWFYmuYTUYqIg-40whd3pRZC7AzmuwIRF-6xrtmXmPvvYVJYqW97WWPnk8ZQeKoKvOohWtFyNOUHtb9bfZ7ILdLIsjvSNb-8uT9gqkjkpOLbLYTRMYJpmd0a8Kw9ZdJ0tOisbAnqF6KRioIU5vKUBvro7VR_7VHctfjS4mmCfDD1KVHyRBDDy1oo-pxRUqwei1ZgqnSi4244DXrQuo-7P4eXt-M75Wp8lGVOd-B71TrgTEHbcqh6vDTYkhza2ak6k-rP-0tF1BYso3Tm92_o44Gce-axdE5D_1VDoOV5yIIW80NaDld2sFbPgtT-j8hub-Hnx3RFgPBXF3Qig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیر ۲۹۹ هزار تومان با ارسال رایگان!
🥳
با سرویس سفارش
یک نفره اسنپ‌فود
غذای مورد علاقه‌ات رو با
همون کیفیت
ولی ارزون و به
صرفه‌تر
نوش جان کن.
😋
🔥
از اینجا سفارش بده
👇
👇
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101898" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101897">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=WFxxB9ldADBK19nIGLe_qlygNKCzzjqeFOzGqoNiQpGXkcHgwAP5Xul_rvKv4yO5W-KcGxEjoXxeBcJK0QGjoFZ8lyHYn67rFrk3UNvOO5WL-kf6Rxt9mKeWu1ytWDXhaDLHrn1J_kUCg3v637FR1ewjM7eof1CeUJXVNyXyz-OIK2Z1xWJ8NX07R2fzfHSwDstDEle1OBfnbUsXZhwwRsa-1N7FU-lIYz5ENDz16Jb9Kcdv2ncD7cahNsht-7NkLUl70Om69lKrPhbzls9KsePXFn3ej0BnOJtla5wPcMmN7MNq68hc6NY9kv7Fo34UZvu153kNlWjscQA5q1ccT4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=WFxxB9ldADBK19nIGLe_qlygNKCzzjqeFOzGqoNiQpGXkcHgwAP5Xul_rvKv4yO5W-KcGxEjoXxeBcJK0QGjoFZ8lyHYn67rFrk3UNvOO5WL-kf6Rxt9mKeWu1ytWDXhaDLHrn1J_kUCg3v637FR1ewjM7eof1CeUJXVNyXyz-OIK2Z1xWJ8NX07R2fzfHSwDstDEle1OBfnbUsXZhwwRsa-1N7FU-lIYz5ENDz16Jb9Kcdv2ncD7cahNsht-7NkLUl70Om69lKrPhbzls9KsePXFn3ej0BnOJtla5wPcMmN7MNq68hc6NY9kv7Fo34UZvu153kNlWjscQA5q1ccT4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارلینگ هالند از مزرعه یه پیرزن استیک، عسل و شیر تازه خرید و بعد رفت خونه تا خودش دست‌به‌کار بشه و غذاشو درست کنه. فک کنم هالند بعضی وقتا یادش میره که یه فوتبالیسته با میلیون‌ها دلار ثروت.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101897" target="_blank">📅 17:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101896">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K07G03o8ujvjehwL_wJSKXm6Y33ypx-fmAbKnarGVIAvH5chGBLhW4RSQwA3p3yz5joFEp-LxEXz8XhlNvDyZgWC5_esf3T3wFzp4Ewws4twsX3OPDdlfeZCspDsvvDQ2BQR0-qkzb-020sEINRznYCk1rjZhcZ5dp1hIOxoWIYn9HNZ6qEidirlfShXVw0PfGE7g6LiEWcvWxapRkdDDND1le3vMzskUefhHBHrXrq5fhn6s1_HWPGIo1AnbPt4xNtCY4p_1dDnQXY4XApgi3nRgpH3sKQs7KG14CDqFcoOjjD18gVhF-OPxxnY-CW0HmU5iBjefJFqtz35xyR7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین: آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101896" target="_blank">📅 17:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101895">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0B5iCsWx6XztZ7qeQ46sMGpcEss5PkID4287pFZAn5pemwimRCfAUvt651kfS7uydTZpXTR4HKqjZPNJg_7Lo91tIxuNJ2pV28Z30RL1piwzLdTEI4_XUhHJTbox7kWrFHoJ7c76ChcW9MtgDLA-YlqOfIo4b41PZeBuV-CkQB6GVQjAgiIaqd2rCd-ZoiuQcxe8mWYmIIzSRui-pUCSDlE1_u44Ta_Ie1nGZ9eqnt41vyLy-9-P1lZYKCccq0zLBOXSqg8ZCMlET6znfebBRDSBpGe-ZchOoD-iGLO2o9IfieRzBYyS9r2nXNureAyC0ViToG9osiU4XSbwDDxtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بن جیکوبز:
نمایندگان وینیسیوس جونیور، این بازیکن را به لیورپول پیشنهاد دادند، اما باشگاه به این پیشنهاد توجهی نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101895" target="_blank">📅 17:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101894">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=dsBS5eJLGlrcQ-t5fpYX-gLef7DiPfxZkMeOOg4sQvPrMddPf1JK1ogTBYt-BqHowE5_Voa4d-jCbHMwlAHg4dR1KsBVO_p2L0f83aqaFd6_PZp4_LAkoGx2HL8sq2fVHjpmK6Z6YGCZtUTrgwkVeBI2v_o7myx5aLnSuqe5s1v4nAMLBRghHwdGZSMZvN9Dv8x_L0UIzpuSUhhJnzhnC_5-j8u1kvx6QkjVtgL_WZb4XtxwdR0B6OWNjRzzG_SCUl4k9fOLLRdgTuVJIV9wJWRIU55qF36BrVRnjGP-wZOkTn-AxtjuFQDUNyNIAYDx86k6_ic37LJlNksTnGmwcqz1zJWebXj4bMGVkn4PsmA6Ee38YT8SMPb8VWT_2F80Hww49SE3N7fdTJpSaqlfvL-y50SDu3MQMk_AoAF9AdRzzURhwk2UmuYzUNLVUEXTDxtpLpuPj6rpWh4yAWTceC3yl-sgM2hwiUevXUKGxUrsuhEbw3zerVxuzNGtC38q2mdCwQRaynGpE6C2XghbFn-oVrNQCddChXHtTPvOm28NIFcLUrUqXAmwa8vLdFhXiPGTwPv1nd-jRdxyRS5M5_HtFQfzqeUstbXnBjF3YP7pwrBdPCp19bMA4WZYi2GxEmKHLLMIsTPdUMHky2o6eemX8NNuvteoRnKZD0WvWnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=dsBS5eJLGlrcQ-t5fpYX-gLef7DiPfxZkMeOOg4sQvPrMddPf1JK1ogTBYt-BqHowE5_Voa4d-jCbHMwlAHg4dR1KsBVO_p2L0f83aqaFd6_PZp4_LAkoGx2HL8sq2fVHjpmK6Z6YGCZtUTrgwkVeBI2v_o7myx5aLnSuqe5s1v4nAMLBRghHwdGZSMZvN9Dv8x_L0UIzpuSUhhJnzhnC_5-j8u1kvx6QkjVtgL_WZb4XtxwdR0B6OWNjRzzG_SCUl4k9fOLLRdgTuVJIV9wJWRIU55qF36BrVRnjGP-wZOkTn-AxtjuFQDUNyNIAYDx86k6_ic37LJlNksTnGmwcqz1zJWebXj4bMGVkn4PsmA6Ee38YT8SMPb8VWT_2F80Hww49SE3N7fdTJpSaqlfvL-y50SDu3MQMk_AoAF9AdRzzURhwk2UmuYzUNLVUEXTDxtpLpuPj6rpWh4yAWTceC3yl-sgM2hwiUevXUKGxUrsuhEbw3zerVxuzNGtC38q2mdCwQRaynGpE6C2XghbFn-oVrNQCddChXHtTPvOm28NIFcLUrUqXAmwa8vLdFhXiPGTwPv1nd-jRdxyRS5M5_HtFQfzqeUstbXnBjF3YP7pwrBdPCp19bMA4WZYi2GxEmKHLLMIsTPdUMHky2o6eemX8NNuvteoRnKZD0WvWnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔙
🔵
۱۲ سال پیش در چنین روزی، دیدیه دروگبا برای دومین بار به چلسی بازگشت؛ اسطوره‌ای که نامش برای همیشه با آبی‌های لندن گره خورد.
👑
📊
آمار دروگبا با چلسی:
🏟️
۳۸۱ بازی
⚽
۱۶۴ گل
🎯
حدود ۸۶ پاس گل
🔥
۱۰۴ گل در لیگ برتر انگلیس
🏆
افتخارات با چلسی:
🇬🇧
۴ قهرمانی لیگ برتر انگلیس
🇪🇺
۱ قهرمانی لیگ قهرمانان اروپا (۲۰۱۲)
🇬🇧
۴ جام حذفی انگلیس (FA Cup)
🇬🇧
۳ جام اتحادیه انگلیس
🇬🇧
۲ سوپرجام انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101894" target="_blank">📅 16:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101893">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1GvvcIReFinuUh8LFKECnzz6vnfUbuWKBiXmgXoGD_C5ehXvdSCFdbePXqkoPxFjp5fccnor43_JsQgSL9FEmFxYtKrveggLFD-yy5B30K54uBv5LrraCQT2rRLloMIKsE-_gp8S1J5Dl0ChJX6IvsYVxoeweAiuK6Y8eggZyHNxGyd3qDYc3GYhM6LSYc1Ae2XdZI7KGdsJH8fn9V1C0oMDLs0YJTPAijh-jCwJQPOeJfbUgI3N7PuJvT_0O0O61sl5VO0CzvQyugOI5BZqy4INaS4boGrF-nEqYMYD4bvpmYWpjOsI-rnoU7yV3kav5t-npmvBn8dyvigvy7KUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش مالی جام های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101893" target="_blank">📅 16:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101892">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین:
آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101892" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101891">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a105d81352.mp4?token=MhUUqe5XVuLdUMk1MiiCXlDSPfrI5Ihm4m_BrLbaKJ-ihrw4YOsI_tW734AK-VyhwU4Jl6LtOFzT9xrTn8u2K7fWGcZfmDeB7axSzsazg4emOMc5fJyxRLdjP4CCHLb3OyUMTmi0fvUv2P8E3h-Fpp5KyrNxczgEFTDD5BKzJvUdd-guau7glp1yod36GGeG_gHrzmWRbyinMvTumL5HLLL1UXVjhRUkaZQH2kA2bCJGL0wGD09YWAM3GGVjXlg0DVHNbOmu3A9heFreYlrX97icYsnQHSabVo2kfoO36K7UlycnunGtTdi3LCcTsCKeAQgePMzLdyRj1fUPEPsf8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a105d81352.mp4?token=MhUUqe5XVuLdUMk1MiiCXlDSPfrI5Ihm4m_BrLbaKJ-ihrw4YOsI_tW734AK-VyhwU4Jl6LtOFzT9xrTn8u2K7fWGcZfmDeB7axSzsazg4emOMc5fJyxRLdjP4CCHLb3OyUMTmi0fvUv2P8E3h-Fpp5KyrNxczgEFTDD5BKzJvUdd-guau7glp1yod36GGeG_gHrzmWRbyinMvTumL5HLLL1UXVjhRUkaZQH2kA2bCJGL0wGD09YWAM3GGVjXlg0DVHNbOmu3A9heFreYlrX97icYsnQHSabVo2kfoO36K7UlycnunGtTdi3LCcTsCKeAQgePMzLdyRj1fUPEPsf8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین مدافع جوان، دوست‌دخترش خوشگل
پسری خوش‌چهره و بی‌حاشیه، قهرمان جهان
یه مرد دیگه چی از این دنیا میخواد؟
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101891" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8DoyPalgrANRZGzwIWA4EiMoE23jN3M4qA-A5Tcje7WEpgxs2-lE8atNOOukipynHr6k54fS1F_tdBduDMG_bEDIZxYRoujdlZL0bjQtenuutAn5D6ErLjaWiFlJYJw1WZAcOsnOy6VhShcxbs6r4pxLyfjdVB70NNqfmr8fCTSaGFpWTdX8FTVyXRr6rB5-QedsvJQu2AFXWvyXH-OjvL9PSE-jOidj-ioUS7G9ZbF14M_xRxf1YUNEGkvp9BTcYWoyTXh7E9plw90bKRLtWZeF1axw5uCYLwPvsyiQgdGMe_I8s8cSLwQYQ6_RRlIkgozWYtxaCu7RRTmuTX6qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZDemtPxAAVPGkXeObTA7uXyNGPykZrpTs90fi8a54VyZ7BqFmH-Y46g2eIg9gc13HWDtHgiW-_QS6DtY6ORE3vaLpBk9kFIiwJ-WjaHJDIrAWEK6t-9CuET47-4j0zbmn7cJp-NmBaPA6sehoU_PdNLsY8gahnavvOCaUX4IlR1QZUYfo7NgCXxnxbaa2oGJoJkUiG9hpFUm4eslv2SnsLn1NxEldbFZPUVOZiGOyJizzXOgLVEd9lfqH8Py1F3BUt1aFu6OtYpc82RxLzlSybn4Xy_6zFyWJbALkmxkv2e7eskWWsJf4_hF5C9zUbTSpiHhyr4LJZtru3SYPG1lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
رئال مادرید و ژوزه مورینیو این بازیکنان را به عنوان بازیکنان "غیرقابل فروش" در نظر می‌گیرند:
🔺
کیلیان امباپه
🔺
جود بلینگام
🔺
فدریکو والورده
🔺
آردا گولر
🔺
برناردو سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101889" target="_blank">📅 15:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs9Orioc5_IoJn-9-Xer96MJvirD75_cyqnpawiabx1ibikpE66E1m7DtTMGU8tIH2LSzQ3jlWK5bMCoakh_UJgu_sYt3TMb5e8exkorkV0YvsS4hDJNyj4mxDlU5NOejkU0TC2RRIdHWsF6x1gHf0T3iVIhI2OJ3DorhN_U7fiiaWEMiwB2HjyuJZ9kV2pqysGUv-w7E6PSXJaz039Cu6pkiMlMavfIrQT77DlUloCMW-q-uDOO847Hqw9utV_6CETbyhTccN4J69_duVVsrGSoTQIybYQsKB4brHblPqf4-uaBVN_GBTyIlWsTPqL4KFlbh2dNhAKcWShVeeYnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوری از فلوریان بلاتنبرگ: منچسترسیتی به صورت شفاهی اعلام آمادگی کرده که پیشنهادی به ارزش 100 میلیون یورو برای جذب یان دیومانده ارائه دهد. اما تا کنون هیچ پیشنهادی به صورت رسمی ارائه نشده است. و مذاکرات با لایپزیگ همچنان ادامه دارد. منچسترسیتی به دقت وضعیت را زیر نظر دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101888" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtDyw4oNXi4BhW4zK4SG9Za8vCF8h5NQctG0x2KtxFWpBTs7i0LFsJkrclolPGxQIZFETn_-VqToHxM_eTx0ONEAlpk-blBo9dvTVLlUJQ3EalAPQ7fJqaBxathnp8YTLAqbDy1d9uZM-CBlIB2jXC2RcGerBmL_WGTU917-29JY_6znyDcMEij26DmXCSkF2vyWEfCzIuFjf_eYt84qmQQT1byIS15Fw3HVTdiCtv-0I8V2aRTWvtShwDqZbvjRc5COGHiSLFs7KOt47PJgB0YyII-fng3MqBSBTUfw7K0U5wUHG71NJrSZKE8BZUrBD88-55uU3O2REHjCnlzzGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هزینه تیم‌های پرمیرلیگ تا اینجای نقل‌وانتقالات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101887" target="_blank">📅 15:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101886">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXj_3NwAk_VbjOghC9_bleCtB4tlFSlUBnNsHcdtav6uRnl1cGISwjM8c8NR-K7WXfaYHfS9RnrIGACNqYyTc3agsHcQeOt78joDq7AnbAADM-vw82_8ErQ97pEMBpPPUcdk83V9h_7hy1I2Z3Cvydcum7DX9plb_d_k3hwDZQhOwiLW4pBNRl5XAkX8NrqcHzbdtah09R1fxv665hWo3aBGRJ1sEh8CROsJZWz5TulKi-3gnNYlEfOXXrKtHl-B1T7svNMahvG0cTLUCpwn644eRRy3VVwuoNAdKzjWJ_nwYMwUk02Bvn5pH-i4kjDROVlhHi-lls1a9HGt6LQu4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا: اصلا بعید نیست که اندریک این تابستون رئال رو ترک کنه، این احتمال حالا جدیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101886" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101885">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1LmkJ9qhE3l8aTZbcQPZzNbgZxlxiYtHaJzJ7ugQHMKbx89EXBjHTv4JT4PI8Jc9WG5bZCp7Qf6TjxHkeouTsVylKYnM5wv86gy2M06Puk8r49uyetPhBObGreGYmlQD1WRUxGMdPAZlxVJIDNPeGB4wG6TIou-eLfLQFFnAD7zXuygPm9KYNk3qpi5ZZXcFHfo9H1m2rLmb6eocQfPl9tAtd9RkvDjMPI-GbQWLldCwEq0sX3DIiC-YinWYY_ipUc7LS4oh6xXgqU0Y8ge-4Vlld8RH8Ujr-CLmXor3Ki-zgf_WO4StwNtVuFGpmW7OOa6TYwNoXyv632yFddbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
سانتی اونا: رئال مادرید از شایعات مربوط به انتقال مایکل اولیسه در رسانه‌ها استفاده کرد، در حالی که به طور مخفیانه در حال مذاکره برای جذب یان دیومانده بود. حتی آن‌ها به طور پنهانی به مقر باشگاه لایپزیگ سفر کردند تا این انتقال را نهایی کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101885" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101884">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=o29OSFbrLx6fowUW4GVZqed9b5akGnJqfKGUC_ZlpzHZdUi-4dwvQffWTdKiWPFYV7M6IsSc7fSp2ElyZBdr7dYlXBOQ-p81f9utxWXVLBne0ua2F3FXfFBk2bC8DhbAGi48wk3GYw0nzDJ42KkdSqwY3huDWYjkBzY7tbhkBF4BZt6Is5hABkg0lIgUNH0VPh7Ebz64XsiaX780k38SaOCBRDpM5L5h67sgLffzejCUhFJncXK7rT1ACVmE7pX1z2gDs1EuA-ejM2-DXMFvR5ccCVP9yZvHBNQu7QfuF03esThIvrWxQlGRdgieFWLDYIsU7T2DhF9dMokqM7481Dypgg9p_o93rfa5Yk7ZaUkr3JZgFEv3JNXrVtFlAkjnR5M-8lQZwzfxpVOE0xWj-LsKGLxK3Hx_3IsYzGQ44S-obuAVBCmntE-8JRIRzCCeFZDH-Bdj7cvgvYjrBT9v0AZLuAi2LoX-WWnyF8x52WxHEOibXLNgAxRJj_9U_IF6dO6IRkW6PmJSOKzgEHK-tLrjx_0kh03zbKNJ9pxzyvDOiRFzzMm-2RWFrBHDZw1eWUmSfCkxjWaFWP0hBNakebZj9oPnYy-3IhaJ6zqcXcYSKGxN9ppwJttb-kKThrVqbxr8Dt413o7rI-UUYXsOYqERBBi1z_SZ9n8-UNAzgIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=o29OSFbrLx6fowUW4GVZqed9b5akGnJqfKGUC_ZlpzHZdUi-4dwvQffWTdKiWPFYV7M6IsSc7fSp2ElyZBdr7dYlXBOQ-p81f9utxWXVLBne0ua2F3FXfFBk2bC8DhbAGi48wk3GYw0nzDJ42KkdSqwY3huDWYjkBzY7tbhkBF4BZt6Is5hABkg0lIgUNH0VPh7Ebz64XsiaX780k38SaOCBRDpM5L5h67sgLffzejCUhFJncXK7rT1ACVmE7pX1z2gDs1EuA-ejM2-DXMFvR5ccCVP9yZvHBNQu7QfuF03esThIvrWxQlGRdgieFWLDYIsU7T2DhF9dMokqM7481Dypgg9p_o93rfa5Yk7ZaUkr3JZgFEv3JNXrVtFlAkjnR5M-8lQZwzfxpVOE0xWj-LsKGLxK3Hx_3IsYzGQ44S-obuAVBCmntE-8JRIRzCCeFZDH-Bdj7cvgvYjrBT9v0AZLuAi2LoX-WWnyF8x52WxHEOibXLNgAxRJj_9U_IF6dO6IRkW6PmJSOKzgEHK-tLrjx_0kh03zbKNJ9pxzyvDOiRFzzMm-2RWFrBHDZw1eWUmSfCkxjWaFWP0hBNakebZj9oPnYy-3IhaJ6zqcXcYSKGxN9ppwJttb-kKThrVqbxr8Dt413o7rI-UUYXsOYqERBBi1z_SZ9n8-UNAzgIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
امروز تولد هالکه و به همین مناسبت یادی کنیم از یکی از ضربات سنگین و پشم ریزونش.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101884" target="_blank">📅 14:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101882">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki8246suLEo_y9KtPEsCPlyvFnK7RM5pMsdIJ1hkf1iiouAYmoNS03-FC0GShoL_w0_ipMhmU38XyNiqqkIgi6Fhwk7jvTASliDqMN9yB-YfYx-ffvIIfioCVbOMJ8ePFbBKlLipouDfVtI09_56uinGlv0hwx--oMqeGgZKe9dNlNJSBVkKODaZSar9TUqfnMYOzKWehlD9KOcgLFJfad9jUkFtKilyt4oMYqJQ1zZaJ-Zn7hpKRFF2zMS-lWn2f8a9eQ4r3VowD6qc6_OtHc9n8dn878CEOKkZEr7eTKvFtw0c5keT7ZBZm-8Sv1F5JBCjy6p84aTcr1ns2sP-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=fZUo8DcGTGROKWYUZkGOiKxbmeAcL-SYvUEdCAaoLlUgNofDTtm7V1EXDuXl9JK3uqe5otNR_wjU42i8QnGPnOD9CJn-EM4j9tMm2f5rywRIgQdKlIgpbvkesUQFaBqmjyPQzon8_gz9EipfiIhX74Kzwgpn7f0yEaDbKff21QqJUf_9zM3_fgC6cW-SswD2P40WveCMlZYP9eVhy_g16UBFjtldqA9XB-ODxotgj4Rfiz57iFWnnds-WuPXOd1rkqFcNCenu-29ez5tMZZjl3HItty4OgM0Mnr60lyeqxnRazwTaIFqLpFAetNrlz7UdfdWMw2lbKXIcyYSNdXv2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=fZUo8DcGTGROKWYUZkGOiKxbmeAcL-SYvUEdCAaoLlUgNofDTtm7V1EXDuXl9JK3uqe5otNR_wjU42i8QnGPnOD9CJn-EM4j9tMm2f5rywRIgQdKlIgpbvkesUQFaBqmjyPQzon8_gz9EipfiIhX74Kzwgpn7f0yEaDbKff21QqJUf_9zM3_fgC6cW-SswD2P40WveCMlZYP9eVhy_g16UBFjtldqA9XB-ODxotgj4Rfiz57iFWnnds-WuPXOd1rkqFcNCenu-29ez5tMZZjl3HItty4OgM0Mnr60lyeqxnRazwTaIFqLpFAetNrlz7UdfdWMw2lbKXIcyYSNdXv2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
هِیبا ابوک همسر سابق شرف حکیمی:
وقتی سال ۲۰۲۰ با اشرف ازدواج کردم، عاشقش بودم اما او انگار به من شک داشت و فکر میکرد دارم به او خیانت میکنم. وقتی دیدم نمیشه رابطه رو نجات داد درخواست طلاق دادم اما اشرف اصلا ناراحت به نظر نمی‌رسید! بعدا فهمیدم چرا؛ او تمام دارایی‌هاش رو به نام مادرش کرده بود و چیزی به نام خودش نداشت. این یه حرکت حساب شده بود و واقعا شوکه شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101882" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101881">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356f27159c.mp4?token=pityTQperzXuUR3qPKkez9A1npdKNsBUYbT64ZXcTJwyM5J3rG7MxavqeewpkRHriIMyAxKgu2oIPkm6YglaPIWRAR_4VQ_d2WhVGBkGD5Meta6BwQ50Y_6suddLzyymUuPghxF0c-yGwjJ67rTvQwnFKcZaUKCxDuqMcrLgsXFzp7nvv2byF5UTWz-9hAc4RR0SDfwj7G0afnft59QG8r6yJf6k_mxupf4RfO9cVBdS2qNTzlFRnGmRXpva1WlbpbtiDlZz3kOtFhKgujNrXR9kE__fmcdEVbTTOTfvqp1XoJArYWzFUozzqmO9KkwH29BO8p9tmdAi6laz5acz2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356f27159c.mp4?token=pityTQperzXuUR3qPKkez9A1npdKNsBUYbT64ZXcTJwyM5J3rG7MxavqeewpkRHriIMyAxKgu2oIPkm6YglaPIWRAR_4VQ_d2WhVGBkGD5Meta6BwQ50Y_6suddLzyymUuPghxF0c-yGwjJ67rTvQwnFKcZaUKCxDuqMcrLgsXFzp7nvv2byF5UTWz-9hAc4RR0SDfwj7G0afnft59QG8r6yJf6k_mxupf4RfO9cVBdS2qNTzlFRnGmRXpva1WlbpbtiDlZz3kOtFhKgujNrXR9kE__fmcdEVbTTOTfvqp1XoJArYWzFUozzqmO9KkwH29BO8p9tmdAi6laz5acz2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند لاشی تو مراسم عروسی دوناروما هم نتونست جلوی خودشو بگیره و مهمان‌ها رو وادار کرد «حرکت پاروی وایکینگی» رو انجام بدن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101881" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101880">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZo1oJOR4QTHePKKo5I8l3dkgZ2lMuEHELvQ9mhoE6Jg8Is2xcpfMySFrCL2eXmzp5KOvT842X_vrjZdxHMmeTblVITQPdutTei-R_0uVBuLnzAaLtkGblmQPw-CXScHgegA8hLkc0QYvxGDWjGFeEBCyBdbycoo5lSeqjUPKmCm0VU1ukclwF_U8_M7n4X8uTpymlqUUoEOFw0EyhydoFSXxa8hzWJzyZrlZGGEdUewn_IgI-nsbQX5JdL6cC6-qlLlLi2MBigB00dPK1FjoXvtDxi1a5esvpdzjNT_FNpHzSu3q4Vl_TkEDBRqFzQd5zO40LqAVNSs4qjS8rmztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خط‌حمله نیست که ماشالا فلیک رفته تیم دوومیدانی برا خط‌حمله ش جمع کرده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101880" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101879">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=XzIFYPa8MxUq6iZIRGph4ywc2MJKIfV45RSMrxwt-NIoXpOX5EYwd4ParWC95Jhqt29yF_r55Bma1I-fkO-qfqGK-HPf0hhdg7bRa1VdK6Wlh2hSWv_1c6QZdtpQV7BwzWf_E04kutwX-6VEpqnT3xRefucj-y5t25znKscM5noBq8K5D87CB3KWrJR3vQds30EiDI22RBB_DLq4v53K6_vz-Y3j4eh8fCn-s9a5UxBLsHwGD_RQM9WKKhfIbedWhzzI-10Thx6Snlh95ao_UzVxubjF8YVZMpuiadbnUu94XWGUhhG0vbA_79XAfeEVGX3-tYOzymwoZlvfLXcPxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=XzIFYPa8MxUq6iZIRGph4ywc2MJKIfV45RSMrxwt-NIoXpOX5EYwd4ParWC95Jhqt29yF_r55Bma1I-fkO-qfqGK-HPf0hhdg7bRa1VdK6Wlh2hSWv_1c6QZdtpQV7BwzWf_E04kutwX-6VEpqnT3xRefucj-y5t25znKscM5noBq8K5D87CB3KWrJR3vQds30EiDI22RBB_DLq4v53K6_vz-Y3j4eh8fCn-s9a5UxBLsHwGD_RQM9WKKhfIbedWhzzI-10Thx6Snlh95ao_UzVxubjF8YVZMpuiadbnUu94XWGUhhG0vbA_79XAfeEVGX3-tYOzymwoZlvfLXcPxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صدایی که این چند روز تو ذهنمون پلی میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101879" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101878">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XILxA9AxBdsvq1ARwgtqXcrU0XI43IJnAat11_IupcEj3ecZgFymc2v60mzav1ANruX5GNPpqJIe8MzYGUVHXVRjyhu2b7dbCyHTRE-9Xvj-9DksESVFoObuOoWgJBgpv1KipJvk1EVYbfxiVYlCPU6K58XqPnf5uA4JfzhjlQPxdhyQYk_HAM957SJZFF3ikEBxvELFmCg9ZXj2ocGq2vdUa97m6BTvE0Gev0leFIyVrfdz7u4B9z5gtm7DioEEhexnHcaU0nqbF0ppYPrPLGsIoCpfE1djyzbolywUlKo4m_Ns0OLw5TBp_GlGX07Xckw59kJVY6OHogqqp7R3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101878" target="_blank">📅 13:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101877">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=KC1zUwi_hbzoZXBrluS89CDkYdWMrCUX1PdiNi2MShcycP3_SjjEMS2Ju2gRgKTLF6H2nOtkro89Ae3GRF9nht-aRBA8OvbHuXGHE01AD3XLMyKgKOkmABKxMBjIzX5YZOwTTkNwni-6Jkm2yN0ecRC6LXUS-zarln8dOYK3ph9PE0jVmPU7z5I_GZg9rF_lIL2E42jRYjuI7F3sSqH5PCUaLe8frhj_V-X7itRX0ISpvL6TKN8hwuvalJzwrLvwmz6ppi2Z-feM2s7FaIRK2RhVrLG-l7bhhmFfXLCxH9KBNaId89-cvlVOb9jWgtVl2Cil_X0N-1moy1W8leYh-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=KC1zUwi_hbzoZXBrluS89CDkYdWMrCUX1PdiNi2MShcycP3_SjjEMS2Ju2gRgKTLF6H2nOtkro89Ae3GRF9nht-aRBA8OvbHuXGHE01AD3XLMyKgKOkmABKxMBjIzX5YZOwTTkNwni-6Jkm2yN0ecRC6LXUS-zarln8dOYK3ph9PE0jVmPU7z5I_GZg9rF_lIL2E42jRYjuI7F3sSqH5PCUaLe8frhj_V-X7itRX0ISpvL6TKN8hwuvalJzwrLvwmz6ppi2Z-feM2s7FaIRK2RhVrLG-l7bhhmFfXLCxH9KBNaId89-cvlVOb9jWgtVl2Cil_X0N-1moy1W8leYh-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مرور دودهه تاریخی برای فوتبال اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101877" target="_blank">📅 13:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101876">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705177dcef.mp4?token=UtRUQOfz83X-Eurtzsi4EbzPxaRD7eqeJiA8zNMh9lRSj8fAkQbYespbRT4q-1ps6yObTzpTRTy1zWjukfNs9zOtR7uTMI3MxSR9wCbJrmDejLjsGy7kA7kiwW2MFTZQJQu93oRMoAaYdxZf7HLIq6NZ6v9isN8fJZ8NO8ln2x4RZU3XlkZ37SNqPnxhvLrWnU4CImos86K-rdvxROMNeXVGXGekwP4d6zpbwRmYUEdPw21bcpZ_BmQspmdLRRJBB-L1TUM2sYrNDPsdm55HaW0HO9j5iyKTgRQoNiZvwCHv8FtjXJhHkrun1Ye3nqNUEy8Pp_wIYJHpJ08yASEHRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705177dcef.mp4?token=UtRUQOfz83X-Eurtzsi4EbzPxaRD7eqeJiA8zNMh9lRSj8fAkQbYespbRT4q-1ps6yObTzpTRTy1zWjukfNs9zOtR7uTMI3MxSR9wCbJrmDejLjsGy7kA7kiwW2MFTZQJQu93oRMoAaYdxZf7HLIq6NZ6v9isN8fJZ8NO8ln2x4RZU3XlkZ37SNqPnxhvLrWnU4CImos86K-rdvxROMNeXVGXGekwP4d6zpbwRmYUEdPw21bcpZ_BmQspmdLRRJBB-L1TUM2sYrNDPsdm55HaW0HO9j5iyKTgRQoNiZvwCHv8FtjXJhHkrun1Ye3nqNUEy8Pp_wIYJHpJ08yASEHRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
عشوه‌های مجری صداوسیما روی آنتن زنده که در فضای مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101876" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101875">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNC6ivJ093cnvzpDOxVBrpXNebF4oBGFRtNdCErPDC_kxY1Wld7feqhk3DYaNmemECYSLSHkEHs-ZankIGL-05JyWuZ8DGY5YDSYLY0huaE34OafkhvnXD0P4CsF9NoJ8igfe49UmuASD5wRWtzqcCijF5QV_oaKnD_L5fysoEO1Jqrtxvfl07i6gGQbIpeFptlsHelXgvdIm5JMW1FXO25LNeJc7Erw9B_ixF2I3y5HiW7ImlyCuaoG56QpXZa7P9LQZgC1ynAgIJmCWqugBGvJZ7jSfPz42h5cpACiuLW0AYmi90gBTqRNtxF_uwmPE_62uo0zb7Qgcxcg1WGqww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
متئو مورتو:
رئال مادرید و رودری به توافق رسیدن
حالا رودری فقط منتظر توافق رئال مادرید با سیتیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101875" target="_blank">📅 12:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101874">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=iNhJl7B7sZKbcTjj9ubzTKbMhQpv2moU8fQSCvaCmf_S2nGjHl_6PGlC2LAxhYCNAi5zAMtyS1aNnrqLtPBmCaUUuJrDwhs3IrGKZLJntzihjI66X_6AD0qk7-v742oQXDiJdhE3OCu3G-RqTMnxu1iodWaQnUF2e6FwToRVoBMHeYlOkLOs4cNr-QHJL28GgfMnVm0Ytz59cAvoGfT2QlNxUUZ5Fo8Kzsgk0HocgJ7umH8fMJMN5V3ZjZHShWa-KrzvdExM-Fqg4HUHiwDZMludk0Lm6bf_VNJZEPnlA02D_MtXBvnA5XDTtXeopZSr3wpTF0jySeLjGjpbx7NJsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=iNhJl7B7sZKbcTjj9ubzTKbMhQpv2moU8fQSCvaCmf_S2nGjHl_6PGlC2LAxhYCNAi5zAMtyS1aNnrqLtPBmCaUUuJrDwhs3IrGKZLJntzihjI66X_6AD0qk7-v742oQXDiJdhE3OCu3G-RqTMnxu1iodWaQnUF2e6FwToRVoBMHeYlOkLOs4cNr-QHJL28GgfMnVm0Ytz59cAvoGfT2QlNxUUZ5Fo8Kzsgk0HocgJ7umH8fMJMN5V3ZjZHShWa-KrzvdExM-Fqg4HUHiwDZMludk0Lm6bf_VNJZEPnlA02D_MtXBvnA5XDTtXeopZSr3wpTF0jySeLjGjpbx7NJsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
🇪🇸
وضعیت رختکن فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101874" target="_blank">📅 12:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101873">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=D3bjsNZj154b_iMj6ySaLdOvlN3Rwgcq_l31qqRsNGYu-wI-0P5JIIU9WOzskAR5-ffWV5J2lI-0iALn0n7yI9PDOZ-s0hYGBS9KOSykfQGUGLC8LY69r89tZjIccxIBRn3Eb0QMrGtAOncmr1H54LyW9OlyXKCXedujRyWphu55kh15GKUbmy_P0WNyKgp3RWC4ZfBqNZTnU6ZIrTpy1-krEVfouJMjKTGgTR7vEuyXGyZ-2Xc9tOaUk1KgFaJprT9WdQGmqHwJR5eTlhP-lzwB81KZ3GP2OuVJPB-8tTQXOSN6dT4nYVyU1_Rm1MnjhNUFvV6CDhhEKuTxK1xKES4opfZ2NcpKFFtTH0MnS8HLXYAakpyE2Sy5G3r_4Y8BGj9uiz2ngiI2GAiys_zPdYUUnPWPloTdcvp9zdE3B-KVpIF6gGZn92u1wScUi-3lNH7sA4dr9_v0IEVurmc9FLM871ToSehU_plh0Yy6m3HVWq46KSZ-zo-NBUWfEjm7uIt7smwC9lfLTsQL4RA2cYFRc-mh3oDKC8UL7FfAAZ7gjDdND3HXlwziNYdpDSC-ImTzyAYdD_3gyT8U5GSggv4_qLbEUnJbxEVS3-AX_U8BRypBfVGU-mJ84Vnj8Jv2DrwuTOR-MIWuFx3MbtARkxAB6fPMf0j-klL87VXFwzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=D3bjsNZj154b_iMj6ySaLdOvlN3Rwgcq_l31qqRsNGYu-wI-0P5JIIU9WOzskAR5-ffWV5J2lI-0iALn0n7yI9PDOZ-s0hYGBS9KOSykfQGUGLC8LY69r89tZjIccxIBRn3Eb0QMrGtAOncmr1H54LyW9OlyXKCXedujRyWphu55kh15GKUbmy_P0WNyKgp3RWC4ZfBqNZTnU6ZIrTpy1-krEVfouJMjKTGgTR7vEuyXGyZ-2Xc9tOaUk1KgFaJprT9WdQGmqHwJR5eTlhP-lzwB81KZ3GP2OuVJPB-8tTQXOSN6dT4nYVyU1_Rm1MnjhNUFvV6CDhhEKuTxK1xKES4opfZ2NcpKFFtTH0MnS8HLXYAakpyE2Sy5G3r_4Y8BGj9uiz2ngiI2GAiys_zPdYUUnPWPloTdcvp9zdE3B-KVpIF6gGZn92u1wScUi-3lNH7sA4dr9_v0IEVurmc9FLM871ToSehU_plh0Yy6m3HVWq46KSZ-zo-NBUWfEjm7uIt7smwC9lfLTsQL4RA2cYFRc-mh3oDKC8UL7FfAAZ7gjDdND3HXlwziNYdpDSC-ImTzyAYdD_3gyT8U5GSggv4_qLbEUnJbxEVS3-AX_U8BRypBfVGU-mJ84Vnj8Jv2DrwuTOR-MIWuFx3MbtARkxAB6fPMf0j-klL87VXFwzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
اتمام حجت یورگن کلوپ با هواداران و مردم آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101873" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101872">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=LxHPYnPsZspXvKlt6m9XNmlDWUw6sZRr_2tKBdCEqUW_D4FWbIU4bqwrlEv3PKqgwiFWqryJEK53A3dP9tI1MBqBnjE2PjlJZcCnBpUOjRul-zmxQLnBkQmW5Z8bwwaIUuH6afRBDue04Szw03ckjpuOeR0bwiP7Ht2RTS8QG0KZnmzf-pT3WhUwimBJrQlrwgOzQ2Cmz0fESXiVQpYOzgPo0LHJgodWfFB-vPRZuebiGyK7CdIrvJV6NhJmclyFCA-Sieia1pyE1TXUdJg7VT6BnC5VSTHiG60zB1ba0mkr7itl5BTygtcNjcITdFxUCABkPoVDnjD-5yOauzs5mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=LxHPYnPsZspXvKlt6m9XNmlDWUw6sZRr_2tKBdCEqUW_D4FWbIU4bqwrlEv3PKqgwiFWqryJEK53A3dP9tI1MBqBnjE2PjlJZcCnBpUOjRul-zmxQLnBkQmW5Z8bwwaIUuH6afRBDue04Szw03ckjpuOeR0bwiP7Ht2RTS8QG0KZnmzf-pT3WhUwimBJrQlrwgOzQ2Cmz0fESXiVQpYOzgPo0LHJgodWfFB-vPRZuebiGyK7CdIrvJV6NhJmclyFCA-Sieia1pyE1TXUdJg7VT6BnC5VSTHiG60zB1ba0mkr7itl5BTygtcNjcITdFxUCABkPoVDnjD-5yOauzs5mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇩🇪
خاطره جالب مولر از بازی مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101872" target="_blank">📅 11:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101871">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1pLZ82FRU72U_9ZS4xGTxvATiH-fE4VHwWlbQqzE1Z0D7aNItJ8XywoyEHArICsPXr5TyzWq0iSMkQLd9q5LCpVQ9nk49QsvtF-pegE7qgsOaNetbOf5CWvzovxmjMGgeYoVoZEJFBV1VQ54K2ecIJ6IgOoZ2ohED-UYQc4jF24FLUO4gMBo7bZLQeNagVbsgKmweiogn88XrVgo6v1i66NlwBNbIEqWJzk_2LSTguWKMJ7hayBtLFTRt0UeB6-9cDyeigV4N47_cUHRHbtz-dnTVrBAORv9lXNR0KKwOQzZtuZNYLOMjTl_SAUASu5LyxV0rhQEo2ZTFvDZhdgMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لی کانگ این رسما با قراردادی به ارزش 40 میلیون یورو از پاری سن ژرمن به اتلتیکو مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101871" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101870">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtvzV_5sH8x3IrSna29WNyLPxNSfhGsBGdvqY0ROVh4kyQeHlMeSlMYiTZ4vfkSqbK0O17J_5ExQOpNVyFRDSVE70i6d7F2GzhOBA7L1TxTdwPA6QG9SloIAZHxpN0hi1wNnXnoTeKSJ1C0sFAY_INlLVfbF8LUCw3WotnMqjV3kfTUmQG-ImwmE0pQjnjgboqJ4ivNJIHUOl1o1FWXl91eoH-R4lqgypNYUl9rGqMN1nojIi-Qd-nak3Anw7_AOXWLfAodFqWfPvUUSzyNlg0MbQ0C17SgIzsTez26OGBgQucV3r9DHPfq-2Bd3moCd_Yyfq_ZlJlmTf22XgXiuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
تحقیقات سه‌ساله فیورنتسو سانتینی، تاریخ‌دان ایتالیایی، نشان می‌دهد که لیونل مسی ریشه‌های برزیلی دارد!
بر اساس این گزارش، جدِ پدربزرگِ مادری مسی در سال ۱۸۹۹ از ایتالیا به برزیل مهاجرت کرده و پس از مدتی خانواده به روساریوِ آرژانتین نقل‌مکان کرده‌اند. همچنین در دوران اقامت در برزیل، نام خانوادگی و برخی از نام‌های کوچک اعضای خانواده تغییر کرده است. این گزارش تأکید می‌کند که پس از مهاجرت خانواده به آرژانتین، دیگر هیچ سندی از حضور آن‌ها در برزیل وجود ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101870" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101869">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=FCxjvIsNyO5auB9yRTJgR0wNfFIHssAmUg7EzvLzD7eaofbqo6TkYRffcxbdpLMCREfbJlM2N-jRjtqFw8hPwU7dvYTG0ezipZMXCg3qNgw2WbVTnRr-VAvvBcNyq5QgjpFOncNbMWRssR8AOtsgjk5lmuOgAr2IAiBmpY4vnN3-XmlpjL2J5s7zFnA-uh5vXe6VZWQKCwSYCyt5lQh3OWGjL_4g52k8ONZJurWS3uPNsYdWBYkhlj8wAc7VN6-A-uYN68U2HhJJ1ZLd31p97t2MUXdUBWBqclkWzQnARy7dqVHCgAhzj_vem6V-MMNT3H_cpE4PKG2QBXjQfTd4CGNTqA7Sy2BJiPGn3YaQMutuusTZniB6vFVizo6niI5EkDpghxDbBp-RTOnJSf6i5kz5m7GOjYrNKcuou26zs3Lr_P3CRCQNqdUWAPJ_U9Y4zvLUfDWQ2B9MGaCMT9hH6fC3zXjepJH_UjbCMf_tNZ3-U-u7dshyf5fTTYi_iSnL3cVxVVEVAKRM5qPVzXs-Z1EFz6VV1HZPzqwKSTkmXMkq0umxJiC2imBn-RNcRKWsIYdprg-5rG8PvVWypmx1kV1ypSAVFf9SaRpQiNYCUjKFLI5cjsPUxYX9l1IyjbtC6LIJ3ZhSLlqNvdSKi9yw7jpikqRhk2vBQd1-qtvT1jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=FCxjvIsNyO5auB9yRTJgR0wNfFIHssAmUg7EzvLzD7eaofbqo6TkYRffcxbdpLMCREfbJlM2N-jRjtqFw8hPwU7dvYTG0ezipZMXCg3qNgw2WbVTnRr-VAvvBcNyq5QgjpFOncNbMWRssR8AOtsgjk5lmuOgAr2IAiBmpY4vnN3-XmlpjL2J5s7zFnA-uh5vXe6VZWQKCwSYCyt5lQh3OWGjL_4g52k8ONZJurWS3uPNsYdWBYkhlj8wAc7VN6-A-uYN68U2HhJJ1ZLd31p97t2MUXdUBWBqclkWzQnARy7dqVHCgAhzj_vem6V-MMNT3H_cpE4PKG2QBXjQfTd4CGNTqA7Sy2BJiPGn3YaQMutuusTZniB6vFVizo6niI5EkDpghxDbBp-RTOnJSf6i5kz5m7GOjYrNKcuou26zs3Lr_P3CRCQNqdUWAPJ_U9Y4zvLUfDWQ2B9MGaCMT9hH6fC3zXjepJH_UjbCMf_tNZ3-U-u7dshyf5fTTYi_iSnL3cVxVVEVAKRM5qPVzXs-Z1EFz6VV1HZPzqwKSTkmXMkq0umxJiC2imBn-RNcRKWsIYdprg-5rG8PvVWypmx1kV1ypSAVFf9SaRpQiNYCUjKFLI5cjsPUxYX9l1IyjbtC6LIJ3ZhSLlqNvdSKi9yw7jpikqRhk2vBQd1-qtvT1jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری خونین و فوق‌العاده شدید در لیگ امیدهای فوتبال کرج؛ مملکت بی‌صاحب همینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101869" target="_blank">📅 11:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101868">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QltUisy8mnG0_BGLtEBGQD9rfJK6Wxj7Og4BKNsCCsQZttXm5JJJ85FFSoPjkITKGkLnttJ2sY0WQJ40FqPlqGk9RXEa5fHXJ_2zEFuWiFOo3bPL4gq7-0doZAOuKbPGgST1dhvzY25HUHVJ1we4I4P0RWiRqohbJ0ZAAOQymh1xGAqNdi2YNcAQ5AAg42E7RQO1d9rU-BdE5QC4fMMW7EZoPVNtdJEpRIjZwTUI_g4BcBMFS2Gs8eWcx4qVQ7IHmBU-sOpAsp5vzVCTLFMq5TNNwwPgqXeW3oxRCMK8-5kaOr97czuMaN1d00Fd7CVYzW6L4VmZpaQ5sKsEscR9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
👀
شاهکار سرمربیان اسپانیایی در فصل‌گذشته
🇪🇸
🏆
دلافوئنته قهرمان جام‌جهانی
🇫🇷
🏆
لوئیز انریکه قهرمان لیگ‌قهرمانان
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
میکل آرتتا قهرمان پریمیرلیگ انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
اونای امری قهرمان مسابقات لیگ‌اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101868" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101867">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=J7bCBXTwv1iBXe5dlglzg5Az26zsC8uHuv0tLS-v7iWeTy6FdGhh0RAy4jjCQ0RG5VGpniZDLCKzLCXKfDxwBOBU9uTdOAkYGhPoY-4VCRQOy6sPw5JfdsMV5HXl2jHLQ-XCicVuItvqdfRSxMSyxmYSQNadYLBFEOmB6zjD-Wly3w5hwlFhp_EjEvrj-W2GdEBgUcq199XQDRlyW2Zhe-b3TxJxYsaCqOhuc1x29uvlMjt8lSR1tV45CeYlkwDzObebZNaf0ewCkiI3Vo9vSamqnm9s-M26WQi9zFtOX5ooFfYrSHqzZyyUFqlqYDVDREu4CDgo6lRFNVIDoG978w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=J7bCBXTwv1iBXe5dlglzg5Az26zsC8uHuv0tLS-v7iWeTy6FdGhh0RAy4jjCQ0RG5VGpniZDLCKzLCXKfDxwBOBU9uTdOAkYGhPoY-4VCRQOy6sPw5JfdsMV5HXl2jHLQ-XCicVuItvqdfRSxMSyxmYSQNadYLBFEOmB6zjD-Wly3w5hwlFhp_EjEvrj-W2GdEBgUcq199XQDRlyW2Zhe-b3TxJxYsaCqOhuc1x29uvlMjt8lSR1tV45CeYlkwDzObebZNaf0ewCkiI3Vo9vSamqnm9s-M26WQi9zFtOX5ooFfYrSHqzZyyUFqlqYDVDREu4CDgo6lRFNVIDoG978w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🏆
رقابت‌نفس‌گیر توپ‌طلا ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101867" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101862">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fF8an1wsdIT0dCj3Cbec-eAbPqEIYUY2a4XT8qzhlHSVoZ9obVnwcHD9Bf1H-sjNTYwyIXdoqVXsII3-S-AKSd3_oDv13n01TpgclSSRorSTIjH6_PrY25otUTlsa8PvDtMlCxv4XckrkF0pxq5M92z5WsCjNm_Raiq361CROTsGEgGLBSLQCZxwk_kNEGRBKBP8Bz37IJa-FybRMYTva143YGqG2lAWonNHncPFyKl_OuNy4kw-WcuWeaemRNDpWUtmENXGHvz88vqEo4rOYH2eYucwZdMGMsgIRtDGwe52H3Xec-o31Zl4FECPhtOEV8F2YQADcAeG-IzMxaK48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WoVbzwI-PceXJAnXE22DjdAwbA8Szf5Yhn3MuFn_NlcaWbktkXrsFoueED7J5lBDIQ4OMGIu5V2XuTgbTYVhQFlE5VG4NGSchrsF-Ywa0lXMIzagsfEg7aNrB99RS-07JJtVJAl7BfTaH4i6X7gvpbmToukjErJeymxjSODagLH660AdQg80v3uogmmrppbaLnQHx_eNLHE80O9ijmUOXALzZ9QGGvNR4-S7518fB9LL_1DALNag0O1cvRFksLck2-q6fVetxQhUP32N72jh9rWkIn48S0eQqm0nZ9Hh--CBS-EF1Kbsbg4Prq9zHWN0Bsexz2mYo3P3b9gGwbFyOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vy0FNZKM-TjmixkXSNJuemknQDLM5ZmD5xEnsHx2R7onBiaIbmYW4_6GgFX0Cqq-lYZqgtu7hP8pQbTSmvvkcMPJxebDE4oDqPoQhDbQPNeTPRSz2vZbtbC9JHSdoPlS7QAxdmxa0ltCUwR3sHQJXNrOr_pMgaDj-Vm2SWXceNBUnGwl_NEZn4vwiOzetVK-t9vje3NYFtNxVTZvEzq50sorDs5elclBV7bk91FAb6ltUBiC-ZldBV1xM3hvs6C-g5HBFI24mktEs17is9KhqK5Rs6VW1sLy5QMLPqD0rSZyw5WOgkejB1J_dA39RPxSCQUbdLpNJL_HD148EzFVpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnVmDxO-fW82alonBYi0dej6g-oV6v5A9gMZp661gQcR8SJCyNyQ7FWKlPWEKGPGRH7ZIvbcyC05CeoKO5tqTaG_O0WAbUDdUyIenSgv3SpRBAyJ4pxo2TYLtBhdeUBuPmfyizZ1PHUQ83j1obaFnruzlXog3twexWLQpy0Mcn7L2gq-Xy5b_1TAZnzNLpiC6AH-0XkTZJA_jhIrIxwY-k5SMJQLiodKJrnR7tAcjv0aDurBgXMer7nRGV8BL5KkPMrqC7OYBUjwg61ZGZWwIQKBg5C5m55cj8IlIOakWPgR_hMJ0Cg6HDDoj2F0nPOKn0ABwz-EYuLqknDyqmdF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TpzgY568tpxN8H-F_MS--Di7GIi6v7v75Gxfs14jmMfiXWTSLXg97vXBb-z3qENhsS0UEppHk51t9LF-IyvI5jLY23JWFvlenrv664Zut9N6JwJEb5IFL_zP9c0VFFy6tQyFhPwMdXxusdKTboAlQFoZkGCVW2tYOal8O5Z5n7GtSCM0XQzReeai6DwIticN8cV86N81sPvnIh_U85H7sMpvZqEJp1NuShjh1sYEumyv2CtuWsliO_ZMeXdxdARyfzAv0chC9UIlu3igyehLGuh-LtruB58nA3T9j5dOavOlrEDXrXrMHA8AVDr0lj40wdN8OS-zlBllxYEG7uLTkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101862" target="_blank">📅 10:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101861">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=S3qlh6b-dAILfcdGHXdtUMYc_sHLsfX2oJq3saN3YznNTkOWWgQ_cbWKAf9ztkX6Gjj3KSWpwjNrUEYw2uhuBsArAKRjK1q8rqsL-HnXOT1c_yyNZnnUt6BpFcY29pCl4vVhCdM4Ydyurqk9HSsapFwAiHrjTj_QCf3p8NI8GQKZe36Flc1yCiyMcBda5gATXHGNocMxOPb2l-3nboONSjvBKj6emLazF80J2MJKWdYsYno6YZY7_rza_pLFEu9F-IvbteBTXs4dInld95OvZX-COeUqFHc1HSLg5wErp4mpk5JS1yeYsdJ7GBbijt8qpp3HOwbBKyXCl4MfgD5mOkF90lU-xv-c1g7PYL6WcvnN05YwaVZTp0oP4-W4CdRsoDuDxmhYgV6i-Fju4NBOh6CPeftXgK0_EOPAN4kc3UE0rL7gaoUc1dS8GBZhnpxwf054zLWgjv1Qg2kb9Y9Y9cGL8tdGy99BwFB4eTKps7FrvARWRYomR81FzSbcjnWVPccbMriS9Nks3j-T-S9NtUFxfT26sJz4VSHuW3BkESNYC23i-j62HqBWvc_fhM5rYu-CHxGiZOqSM5QkbnmBmwQA18vkNtP6tvQNkcpXBLJtz5fRE2Nhq9tG1kkdatZCeAlrlkJia7zNc46YJT63Bz3tGKfyriqJme30o1zaDmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=S3qlh6b-dAILfcdGHXdtUMYc_sHLsfX2oJq3saN3YznNTkOWWgQ_cbWKAf9ztkX6Gjj3KSWpwjNrUEYw2uhuBsArAKRjK1q8rqsL-HnXOT1c_yyNZnnUt6BpFcY29pCl4vVhCdM4Ydyurqk9HSsapFwAiHrjTj_QCf3p8NI8GQKZe36Flc1yCiyMcBda5gATXHGNocMxOPb2l-3nboONSjvBKj6emLazF80J2MJKWdYsYno6YZY7_rza_pLFEu9F-IvbteBTXs4dInld95OvZX-COeUqFHc1HSLg5wErp4mpk5JS1yeYsdJ7GBbijt8qpp3HOwbBKyXCl4MfgD5mOkF90lU-xv-c1g7PYL6WcvnN05YwaVZTp0oP4-W4CdRsoDuDxmhYgV6i-Fju4NBOh6CPeftXgK0_EOPAN4kc3UE0rL7gaoUc1dS8GBZhnpxwf054zLWgjv1Qg2kb9Y9Y9cGL8tdGy99BwFB4eTKps7FrvARWRYomR81FzSbcjnWVPccbMriS9Nks3j-T-S9NtUFxfT26sJz4VSHuW3BkESNYC23i-j62HqBWvc_fhM5rYu-CHxGiZOqSM5QkbnmBmwQA18vkNtP6tvQNkcpXBLJtz5fRE2Nhq9tG1kkdatZCeAlrlkJia7zNc46YJT63Bz3tGKfyriqJme30o1zaDmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
روتین تمرینی لوئیس دلافوئنته‌ی ۶۵ ساله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101861" target="_blank">📅 10:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101860">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=TPhWVTT3QDKaWVvEJsh8hJ-G1_giXZGpgaNw8amBzVMLvuOQEy0rQVPXckFqBWwGalEz035qWmnAz0_xKnoFpD9aqhBY5Ru4jgIJcMlhwOQPdQLruZLy84TMwluXn1AGxVwvhcu3qn06bp_5Z9x4iTK_k_uA3_Uf39ojiHVIE_nmpINYcA6gaZjuFpYZawwt_ebnmDcfHewrjegUxq871ceXye9a4Azt4Vo1gVQ94tieXQLTXZU-19Ir-yuulr4vZU1gI2uwFbh_4MolErtm5uaaE9a02ubcop53wrA5_vUGzbsABMV6GT4W55K01lGB-GMM6iHIfqZOd06FFdbaxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=TPhWVTT3QDKaWVvEJsh8hJ-G1_giXZGpgaNw8amBzVMLvuOQEy0rQVPXckFqBWwGalEz035qWmnAz0_xKnoFpD9aqhBY5Ru4jgIJcMlhwOQPdQLruZLy84TMwluXn1AGxVwvhcu3qn06bp_5Z9x4iTK_k_uA3_Uf39ojiHVIE_nmpINYcA6gaZjuFpYZawwt_ebnmDcfHewrjegUxq871ceXye9a4Azt4Vo1gVQ94tieXQLTXZU-19Ir-yuulr4vZU1gI2uwFbh_4MolErtm5uaaE9a02ubcop53wrA5_vUGzbsABMV6GT4W55K01lGB-GMM6iHIfqZOd06FFdbaxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
دلبری‌های لامین‌یامال و‌ زیدش بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101860" target="_blank">📅 10:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101859">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552820f16b.mp4?token=ca1bolZCql17EJCUViC1iyOqnr1OW2vPJh1lR6YU26bVm7s0AQUG1DALGLvBaNR_ziGv5ZGxIJLdzAIKUPFUyHL6_c89ov1A6KmQJ4i3OYFydsyc3Vt5BWpjtgOd5rHwV4ZYDzhXlob9Qy3G5Rrdzynrfdx3m5FYVswTj_R6RJI0di-ITFHbwbW7iYS6sEXvMDEsbCI3EWEZXuWvoY5bHg4mEL0DUdhgqdvzOzmV-zaTDWvD78uZdh5bPi85iTHI0m-kzsJbo7Whgc5W8jjhfPCozI7T7DJwl7tDAlPqUgT6TpVskaiwHJyTpSrQJ0BLOsUBoIB-eYxvKKnLVf_cdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552820f16b.mp4?token=ca1bolZCql17EJCUViC1iyOqnr1OW2vPJh1lR6YU26bVm7s0AQUG1DALGLvBaNR_ziGv5ZGxIJLdzAIKUPFUyHL6_c89ov1A6KmQJ4i3OYFydsyc3Vt5BWpjtgOd5rHwV4ZYDzhXlob9Qy3G5Rrdzynrfdx3m5FYVswTj_R6RJI0di-ITFHbwbW7iYS6sEXvMDEsbCI3EWEZXuWvoY5bHg4mEL0DUdhgqdvzOzmV-zaTDWvD78uZdh5bPi85iTHI0m-kzsJbo7Whgc5W8jjhfPCozI7T7DJwl7tDAlPqUgT6TpVskaiwHJyTpSrQJ0BLOsUBoIB-eYxvKKnLVf_cdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
⚠️
بی‌توجهی یامال به دختر پادشاه اسپانیا که در فضای مجازی حسابی وایرال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101859" target="_blank">📅 09:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101858">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=TnIerWVyaM_OA-iqC7cRvyguzPXiAE7weFfhwijh___tvRmlS1gUDInmoG4XmxxMtm34hAMkzXoQw2kJ2-BRJ0eGKab2kGiYQvVFzB0_hI2LNXS_qgtZZ3BtUTOMBdR7JVdDj9SfDJyQaGgbJ-DvpnTvsJYkShd80RSUjowRytFJ909cvYHDmG55ayKACf6iXqqzSHxf33I2A1AaDB91EVRMIgWLARrtT1MUnDIrFBh-CQFbJJMvXsxdIF8hBZRKGtbRcjYmwPgTAyizgkDdcZaiHR7lXEHv_A5JtB7jb-1wX1UirDw3QEFJmbG29przfMdb2XcZkZ50MY5fDe1QcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=TnIerWVyaM_OA-iqC7cRvyguzPXiAE7weFfhwijh___tvRmlS1gUDInmoG4XmxxMtm34hAMkzXoQw2kJ2-BRJ0eGKab2kGiYQvVFzB0_hI2LNXS_qgtZZ3BtUTOMBdR7JVdDj9SfDJyQaGgbJ-DvpnTvsJYkShd80RSUjowRytFJ909cvYHDmG55ayKACf6iXqqzSHxf33I2A1AaDB91EVRMIgWLARrtT1MUnDIrFBh-CQFbJJMvXsxdIF8hBZRKGtbRcjYmwPgTAyizgkDdcZaiHR7lXEHv_A5JtB7jb-1wX1UirDw3QEFJmbG29przfMdb2XcZkZ50MY5fDe1QcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
امباپه‌هم دیروز اکسپوزیتو رو برده یه جواهر فروشی معروف کف پاریس و براش هدیه گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101858" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101857">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwzvhReRRXj3dnmbhY9kLLi9W8N5c2ECHlvauPj-TIhmtQ778BeVIAAkiHqGl1eCRWS-aYlsnJmSr1I8Gsay1Q4svH2wDSZyqmzPhz6mK34NMspvwmHXdnTT0u0lbH7s0Vp_6qf3eUddGvRiy5hJvXy7ePYTdo7ibj3Xla_o_NAdHsrBuj7ji1Qx-jlfaLqnPaJX0IHBvaEGAyPqjeH-vIY-1ZI7rSFh48qBfEUlIjBg4hLX-ocZ-86PDM25yhNQZ4ujzey8UTIiKS-8bn5KNTqteN93H-kh8hI2jmrFYwGMFsMlQHrDBtpk03vJtERdV0ik53xRNhS_71rZFHZTNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✔️
تمامی کاورهای بازی FC در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101857" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101856">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان_جبهه_پایداری</strong></div>
<div class="tg-text">این یکی واقعا معرکس و حسابی زده توخال!
#من_نمیتونم
@hamiyanpaydari</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101856" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101855">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
▶️
کلیپ‌فوق‌العاده دیدنی از پایان برخی از اساطیر معروف تاریخ فوتبال در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101855" target="_blank">📅 09:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101854">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=KSQlCr_oSbpvly_iaIhHGdLnDIfrnzIYwMqSObRXT6AJdWbcCEmhbmoPbhLo6f9FuH02CxiYWHkiWtZWCHx1Sj-Xiw46MS3sWxezLnueGerbbWl6R8_HF_D8RCqT6ObhkDpARDW37HjASjmtxjEF5QXW2Vv32P8_sm-aVkpSliZA8zn2J1sOnBmUU5gY9Y6BwUoo9mbz4YXP8bAe22yJph5P0D8AwDieDWit598KXVxYzoguqOszIf6zOfkZEdkS-Jj-_SEDSDB4q0xURRCcjuChdTAt4QDnndEOzNGJfE5LXJNFliK6jqMEVAtzh72_rzD9Gto75J_VHI3Jy6uJug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=KSQlCr_oSbpvly_iaIhHGdLnDIfrnzIYwMqSObRXT6AJdWbcCEmhbmoPbhLo6f9FuH02CxiYWHkiWtZWCHx1Sj-Xiw46MS3sWxezLnueGerbbWl6R8_HF_D8RCqT6ObhkDpARDW37HjASjmtxjEF5QXW2Vv32P8_sm-aVkpSliZA8zn2J1sOnBmUU5gY9Y6BwUoo9mbz4YXP8bAe22yJph5P0D8AwDieDWit598KXVxYzoguqOszIf6zOfkZEdkS-Jj-_SEDSDB4q0xURRCcjuChdTAt4QDnndEOzNGJfE5LXJNFliK6jqMEVAtzh72_rzD9Gto75J_VHI3Jy6uJug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
✅
علیرضا فغانی: هميشه خود را كنار مردم ايران مي دانم و از حقوقشان دفاع مي كنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101854" target="_blank">📅 09:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101853">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUEB3dpXbk8X8oWvzEckZ0ucfTRBJEG0reYDTwxQudZz4xdQ2JibRj2ZkQ9aSAjeVfL9utIgpqYSn_QqBqqsuHmcS5MKGz4h0XmK-Ub9PYMFkumnsASkvfwqZRmxelV8roW0CaoRG-pOKJ_M13zvQtc80A2Q7FlbGUHpPPu69anTjZFQ9pEeZTiBe4eW5c83ceOiK6mE1wrUmNyuLvnPBpchJgfcm7DPN6o8kAwKqdg34Lq_2ZL1WCG0DSVKOzq_rOyCXyawZK5R35K2RisYhf3YY6xBoa-PReny_RTSxsAFi_FcVveLlNxTP2eknd7ZcrYydQ7RR1Ouw7gyu6wtlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه ESPN: رئال‌مادرید تصمیم گرفته که به سبک بارسلونا، شاکله اصلی تیمش رو حول محور بازیکنان اسپانیایی بنا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101853" target="_blank">📅 02:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101852">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=L4DwN1cKItRxaLLK6oCLsKc0mpQuRVBEQwIUFLgABQBtQpq5m6hjbkBL6jHsazIxLFXD0xYHpheOBzLKmmfQOJcZHuWpwTNqFHX813h0DvC9KCfFc4eq9UvO62d40hPGrDiVONd3rfCjN0u1Zdp9e_SXB_UZXT04hvAnqZ8aYW0ZRBhXFgicW7nt2VZtJQn001iyUk-qBbDrVJi0G8Ca7Wi3tP6SLvBZ5TjR0jyQlDhdFpk8V6E3wtNGvAfCsyNrdJmTO56zyXhpSe4yJaQOGe7u6ZtN49RAhH1ydI9gPtKl655Bx-CQyzqslbRfKo35WOjyeAf17LYltA3WcUVbdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=L4DwN1cKItRxaLLK6oCLsKc0mpQuRVBEQwIUFLgABQBtQpq5m6hjbkBL6jHsazIxLFXD0xYHpheOBzLKmmfQOJcZHuWpwTNqFHX813h0DvC9KCfFc4eq9UvO62d40hPGrDiVONd3rfCjN0u1Zdp9e_SXB_UZXT04hvAnqZ8aYW0ZRBhXFgicW7nt2VZtJQn001iyUk-qBbDrVJi0G8Ca7Wi3tP6SLvBZ5TjR0jyQlDhdFpk8V6E3wtNGvAfCsyNrdJmTO56zyXhpSe4yJaQOGe7u6ZtN49RAhH1ydI9gPtKl655Bx-CQyzqslbRfKo35WOjyeAf17LYltA3WcUVbdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
‼️
🇪🇸
شروع‌قدرتمند آردا گولر در ترکیب رئال‌مادرید برای فصل‌جدید با خراب کردن‌پنالتی امروزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101852" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101851">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_VpolPVuHhJLnNjHQgtYOeXzHCS-Slg9ythICNmrM-Wv85GyfW34j-jeTprrDNEq7kiO-aK8ZIdR7qWaHW6R6Oqi45HRYaCc9eRKyb85zU70ZLEhRoy0aM-OqCev-3ibxTdZld-3lLIoh41gyCmvrxFjRmHkj1YIdEvnMAghIPhZMyr0wJBzn905foiUKjvV39TsanTqwiMZf3-rpP24sYFheNx8fvmKUqWkAM9bYL0NjJfRJ1psDAMCPu6eaoXHTSNgHEu2JhNw9qyM8IkKIjFSiVo2KSTBvFel9mykWOpALC0Ka1oSVEpS53kkaGAzrJtm9xV3evHK32sKirhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇻
بر اساس شایعات منتشر شده از منابع خبری آمریکای جنوبی، ووزینیا گلر شگفتی‌ساز کیپ‌ورد فصل‌آینده به لیگ‌شیلی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101851" target="_blank">📅 02:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101850">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mWIju4LBizDL7oD3BHvHoJ7AVOVo6Iz37nWN2hNOBvApjFpQ9sOb_7594OI7Xh1Ra_a1oB2Chad2ghr6CsT5Mo4xn-kMfmUnbq2HpS1gtSeBhbbeXyJAGE6qI1HWROSBjt4Ujnk2J7yWc9FALY3hbxPzMV1d921d4yL4mMvpMoooqu_-5THHlW1QfjwogAK5kT2s__K959LIurtWl4ncO4SMxsbpGgWCq5Z_s58R_aghgLHbclW8VKeTogNTohvqertLqS0ws2cnPvqmCLXurfbnp2c7iXzn1ds-K9jo4XSOkRl9eGaKu9epK9umxNsGR_xdCk4DYQrVU2O_a8gXnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101850" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101849">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGzsZ0MWZlMDza4jlTIlaOgZGJWxv57V5WfKDRUlD8taMz98pnkrr30aELKeErSYKMeZzC49Y8dFFD_7lkY0PSGHcTxQYCnzDNo8eMA1aFg3ohmlLJjkd5fSpJCBljZD-0DBpbEUrYX7943dO3_Z7dLxPkkD7kURJ0dm2Op1JbDdCWtkIZpOeSqp7pMfLzDoXHcZQkM4EW3H6R0oON3guOa8uqzqvhuiCXZbIN5NFl5YqFMnKRisIfxW34t1oYv47DAwYA95CcUwDC-oukxFOn8t0uk-zV-qtVmpaUJ3vr8ZhpVUzkv6HHYR3PdcCLBtnqzmexZxaKMm3gdhNfZs-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🔥
🔥
🔥
مارکا: دیومانده تایید نهایی برای حضور در مادرید رو داده. این بازیکن به پیشنهاد نجومی پاری‌سن‌ژرمن دست رد زده و گفته که فقط به مادرید میره. مذاکرات فشرده برای توافق نهایی با لایپزیگ درحال انجامه و بزودی خبر رسمی میاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101849" target="_blank">📅 01:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101848">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT3DByHQwUEUQofmU-cSF6W4pv1nd6YCguYQqwYMaHvhpLjLvFAdrX6_p8qDBj8Mh-PhF8yeYUBuXU6mFgWn8aNDSguJODvVuWFFMPEByCjNmZfCh8eWjE0nzLYydJ9ekauZyJUayl4oYqiYdGjdGk75JnYbWDaonZLBF8i-8VIGxOk76fXWrT3Ou4jnw-4y2ggGyA2VoveQ-UORtKJ1tOhtvslWU9KW40wsRsAhiT_zZhmEQjbkyNOoDYU3Q1iRwf9Uom0DHSp2UMTpeS20taKUV02ZzpEwDPPoItw1kP6H_qApOpf_2Vs5HhLzS88ZmsVdUW2qK-UswCK7u-GA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101848" target="_blank">📅 01:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101845">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CfaUzmtN-3VJ1k0eyethCRivWgJsQCZjlLhFZx1NN49snO75mcjjA0t0jmDIXb94yfloXnIX47JCryYlAGgI4CIzC4D_2jkXKqrKd2J2s4Sc_WXkQoIxRNbWXtOXaxGnkKIgj8EjpGXXtjXNykWsrLMPU2qA-C_nwes383CSHg79ArH6dx6w2Ht28R_CcRa9DVC2-zUgwVrshOKkKXy6zg_bSn2WnLf27dkPRVaghVlgmmQV5kku8qnOsw3IF4xb4gxPQymCFQOUZ-dN3aDVqA74YtKzwQuQC2U8HGl5MuzE1gihlIBCFyWRQ4xANkG9SlnlrMU-rsKbylBtAEly5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fcWH8aSGcGnpNRUKnEZYEYnyGY-ETi36qJTGMb60flJfjLDcvIunVC2UaGWC91rcCjGROapfRicL3Kv7mUiUTUAmcvJJN-02GUEtIslAugq9ueYs9a_5B-pUyQWdt7MRuzu8v6taeUeU6hkBYcXx-LgeFvsSLCg470oWjLFnuuZSwr8HV6NYOeWE9c0CbUF7xgnE4oxFw69YMfUuGWVJMh1SCSymas4g9X3lXBxLLUPWz2cAv9vXUbEAuJ17hX0-3Npr-ArYkkAr_AojKi_bhD3oRwf5uDn8zS6u5zEsuZWEh8GoCfFn-RSSG5wE5MFEepIAeQ1eA5sheMQqFA1aCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101845" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101844">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1B8qEY7U9JIw0yPWLBQcJATsilP4UjSb_wtmZE1wYR-vqZD9eCJDJsys7w6_30KQJmlN2kfkm2HmZB9BJWR8y_VRbIMV1CDSMNoS3Rycix_RYf643qDerd9AeSXQ8r1bH0MKDdKLSbWhOoCXh57cJdWb-QeMqHoUxvswAKPoewMvgj0e9XRdW2k_ThLHUV_1DmHdWvBmhippMarhviWJFrUJbRMjuqy3AQl1CKNnUguUTt0fOl_zl6eJY0PprtZcOMUOB-Xo8o5TUGj9usvX-isI3cztLWPDcZ8vqrl1h141wVt8Ip_9S_4Vv5Dzo6svHTzfm--PF1f74hAikvWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101844" target="_blank">📅 01:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101843">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0B2hsAvzHA2d4JDlyrhr62trSkFDOuCf-s8Qyrdvpk1qmfEUu3754TvHyjdahANPp7M7_XBJ5Q31E5EofQVNYOgTg5klHgKapOpNECcj1ISRz01Ua2X0WREinF7wS3hLzyvYO9ZGAsl4N-S_GL4CNCFDVqDAS9kZWJ74tyI7QUpOc4FSTZo-H7_XMmF50lsYc3ZH4dHnMLv3LjDI24p7ebxttgm2UhXH3GBDpwSlJ3tkKCPwYD0VAeq_X9InondpW1fCKCSUPNmHhnsoNM8_AWJOhKzCJfZ-lQzzfc7in9IIxSmHMW4IzqKyxS7bjLB3jzSV7-53JGsgLBf3-j4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101843" target="_blank">📅 01:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101842">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
⚪️
رومانو: رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101842" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aum6ef1-9DCZsMqof6-KV1dm3xzWidBTSWxvecWty9UCkbjIRQXRObkAhCVdipzf2i3cKyHI9vVjEmKDn1f0fUdRlSy5u1aAtsNG4pRRnvCrGMi_qn1_khoH0tB0B_cB6rHj6jYztFQZgiyDrKSqsYU_MB6ldZtu6BB5GVen6ULlSyxYAt1Ar9MQM1p5ZUUWUv1_kPYL1XVIu4nhYPuP_sOyHnSRdWjyWzaF2fm0asJdBLMaTuXyIeCjDjD-26dbwRIRZHOmGtFKKO_2P3WQdOETYL7hl97CHMrdv8Aq1zKs5zg1yzGDTmfMZGEueUPtbMEhp61jD7-SXOTnQeZwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیژن مرتضوی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101841" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgnO-0U2OG3dXuXEuCkwn2cGodnNYCUDZWmzE-uMsVvpAWfyhNeqBdfdY7LMUn6kEtWdkUeDdi7gpXLUA3cP7KnYiYBXDd78SRuFvvgVDdmLEzlyuTrgZYGA4m3odvK0KNDa_ZfppstbQsoLpQ2w3SnKvfuFMnskYAqmah4V91xluK-5WC9-BIrjISagvXBN0ORm0Hv_kJ65k2VUTaSoNK_6psFFT_-1EEdWcljDRDO7NCtBgTXGGCl5lTI2rCKIYUjVMFOfiA14T-V4S_QC63p523WjVnJsl0CPuFq9NlFyg58WFtL3TReGOZNntSHM9C4l_EHfvkhZt76dkSjDTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
رقابت دو اسطوره برای رسیدن به ۱۰۰۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101840" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNoI0GlRfzXFy5pvgBxAUXaAmwH6EKN3bJVaDJbFQ_0wEd2dOo2DQy9wV8bzTTF-WrcIPQBTYuQQh5ufcXWdLnX1NO8kyBH81DsrB9onuBpmduFWi9TbZeYDeYfXmtdDfAxOl4PQ7inzDMueFe4Xgvku3p3Osfbw-TYUnwZR1CNB8voNRauRRgJvfuHdm-5FbDRpW8AlTGVHiJJQBKtz_-oE1NIEePYdEI1F-lKJtA_VuYV9FVBeeEIGIge6Tg19fnslzqSfd-beWRBJi_Ptgn6-ciSZmnk92Lh6-BeO9on5lDpn_LtYn6ypl2QTrfsr7F3pKf9cBMh_AVHBCEK_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101839" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfCLUaul0ZXK_ze1dP8BiX01SIbAYd8dhx2XmcFE5bsbciMFvTFOSYMlOTJtvFqv27QjP_ggxurz89k3L4EPnLGKeqU7oMTAjF13AvTodh3sQ7_7nb6EyvQIDCH0q-n56U9NWcMEh1oy3Ae4Et3blzLjry4v9PuX1M0rL2tKNXliXUr5PRrAfBH14aKCE-9vLueC-DqbW3qS_ezGCBKZF4NjD25YlgkKRkHa2a2MTTCx9_Cb9ywToDm-hYyjljjkc6XAAnKlMCTCDMsyEYacGF7CPH-Blm1KmOhtnCT9XSr6K7H26bFgjci6281mCLvr1Vg-AoSBKNGVha8lFH_xhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
بهترین بازیکن جام جهانی ۲۰۲۶ از نگاه فیفا و برخی رسانه های فوتبالی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101838" target="_blank">📅 00:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101836">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHewhR7Z8-khjNIjBIeDVFL-EHPhJI5QCcT0yCopEQ1RNGhSHy8NrhgZJdIimg5m5Q_V5mjZLUImZqaO7oUWWpJUIdf8jQLxItm1Ur191x15MvjL2LTR9LXaxvQISUDOwskfEBzLreLzp3SksTejg8Z1u2bVTvVQR3DPRB-Z76iKXzKHhgv53MI263H5qmBOnazQsqvHKZ-x1_BmblK9B46fZPvstoRqyhC58Kfu8e8KPfwxIxl-dEo3WmvBs_9x643pTUJR-jgT6wlsELsPpDF0BPuyvRSx-pU3NIhhO3L7xVaGj302WNQaxXLhHUBDA_lMaDG_RawHkfwSM9tfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تیم ملی آرژانتین اعلام کرد که لیونل اسکالونی به عنوان سرمربی این تیم به کار خود ادامه خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101836" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS8cjhWY7leRz6nkUgZVbuvWomvJIT15sAU7KfOr4GZr6hDTcL5wVnFnFbdzQtT-WoA2eZm81Dsj6dDsOMzE_0hEfzQT3jBBG-9MKhr3QdyYVpBmikgu9llkWyxVmfhx1tuwd8uRSf382nCZ2xznRR1DZDueH7CiEsrPIuRCMLXOBVyCjFAv4I3SIDVmB5TI0o02KJXT7eU15Qx7jdexC_wkrB9_hNp6sHhyHCFTtc6jiuKztPFWeioLd6t4DIQKNADcZN-EKOPAHWheFChJeesyVTRLhymoreUXnVXADp6oaX0JyWr8sLRqBM99HLhtUXbUzuHwwnZVJPxc0yLq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فهرست بازیکنان سانتوس برای بازی بعدیشون مشخص شد و نیمار به لیست برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101835" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101834">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUMbK3n8LjudYohTsFdY_Bao6HhcZWm5kWDJajwAcEXTnCma7GKhBfM3Xr_tKkakR4oVl88X694W2nX7VXCNH36OkrYJq0wFuaNyGhC59BWjWH0UdywPI_RhqMbhIKpfZ_l3ToS39LLTvJ6hVWrDkQXQAQWFTFEEfwuihQ0BNKj1Hg99RFHWN7qz82xczfmDseh3J-donGc4Z4G7tup294PiaseYcUNzx6n7mrkAErsjXrrH0-oEyQ4ssMdZd_XeSkZ92jV832T46iJ1C1rEEXscVBcYdf313nxGYMR7mj9DROtny3CraxKv9PEjcQ0rpgWWZPme29QiLcqVML8Haw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لبرون جیمز ۴۱ ساله با فیلادلفیا سونی‌سیکسرز، یکی از مدعیان قهرمانی NBA در فصل آینده، قرارداد امضا کرده. این انتقال مثل این میمونه که لیونل مسی ۳۹ ساله برای فصل آینده با آرسنال قرارداد امضا کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101834" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101833" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101831">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQtgBVoGonyg9PE-CHQEe7uWMbqbNHxcNNXnaDNI305T8XeuA8-Mke1p5iKHSjRhJtDwECVgFHJno2mNe3uSAf0Q5h_8dxnFRy7vTc_rOTG9n0rRUjQ8M39cRdX1S4msKV-8X52KX3d2ypqTvEVpK39pJajBq4Ik6mAxITsB_jLpZDM6nhF_MEABd4hliLGl6CDQZQvoU1_plqg-9xuMQtrthk-5Z2pkDbuBumsinxnYfdF72GA4ILolE2yK0TVQ-vokxHyANADQywzfUHQzNhY84T_r-Jkq1M2_3jTR5V5ox1yqq2fvHOpT7uyYzEBPG1bM1QSHzJfzsVttcjTGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AEAFu5yH0BJwL4q81mH_p9wCw10c2U303AsmQbKtYbk7_dtr3e-5HGvyfWtLeFwLwN7kceH4bcZHBuiQV7J7rk0oiysgRud62o38-9AVYZUEVRIH-dnmDsxqL_RVqjVT-UWLTL20SPC_G6tJPeUw91ewtR9I4b74u_vGlrRQPL_xg0UDpIJqWuGIX352RFgTsBtzid1BbvJ_bI0e4An5P46PXGhrTFCjQ9mDUtZ-_xSvM0wAfW-BzegtFIGjZ5ElbIIKMOljT2hQ8PD86CgqqxDwYtQ0sdDhLviVJ5677qdT-riYbmyzGwpfG6G7bRZJPdZGQDZjvvnIzT5GhBdNPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
نیکی نیکول گفته دلیل جداییش از لامین یامال، دخالت‌های زیاد مادر یامال بوده؛ از تماس‌های روزانه گرفته تا کنجکاوی درباره جزئیات رابطه و کلا مادر یامال علاقه خاصی داشته بدونه یامال تو رابطه با دوست دخترش چیکار میکنه! او مدعی شده این دخالت‌ها باعث خراب شدن رابطه شده و همین رفتارو در رابطه فعلی یامال با اینس گارسیا هم میبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101831" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101829">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8VzCHQoDx9Rk6Qx8lLg6yEegwfFsGXXOSR-j6gsjYdtx_33Rllt89_ulq2MlIIIy7w-1BQQqRglsz_iD0HPoaXawHM_ppun-gqFhrkKY2gJO4SX91KmfvkvPP8G7qIr4VDVhtZ8VceN9uWBAoiSdkNGjt6b8do-ehUJXULxrGWpUASS2xgA7TH1L37Y4i7BEnCTQwRCOaMZ_7l3UqeLSnV6r1f_zRnSnaFe6MS3Y9NhUCdANsbNOyX1sDi12pFhGBisR9JmOdyq_9BsCNUGfBhvyHiezgk1f4J3sMaKUYjFQtv5CZMkxYZCvWVVG87b802C9y4zqB_uvLXIikGfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1jrOcWZIhoCsmLt_2toOWDvKdSELy3O6TEdFxFY0-Bh1v3f-UwIrmKFbwA04jAcm11HkKuuojj9z_0WSt7EHVVjMagyVDXuw6IQUui_AWfwsXzfyer2QTjOubYOlqg4sOtu9VX_dBVEbS7cBjqlmTYeL9kt-diVrgxWONVcGaMfjhIUlN5znviSI5loSPtqThX9-2WCHzdBsncWYP37j8Tq5qW2Yo_TR0Tij_ZgY7UqxAiOpJygGYw_CKo7ao6DdiW8SNU0sftzR1XbaC07cQoBTQp7UVBhDyWml8TiFdk2Rj0DDDVhHCPLj0BbuZNX9orvHJxIVLvj_wJutLHr4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
زمانی که رافائل لیائو تو میلان بود دوست‌دختر سابقش با استفاده از مدارک جعلی تلاش کرد ۲ میلیون دلار از حساب‌هاش منتقل کنه، اما ایجنت لیائو این اقدام رو کشف کرد. تحقیقات پلیس میلان جعل اسناد رو تأیید کرد و در نهایت دادگاه این دختره تیغ زن رو به پرداخت ۵ میلیون دلار غرامت محکوم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101829" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101828">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vb-HJuK0Jy7-Gqa3bAJmv7s3PH_m5omUaRo8RGYuh4Xz4v9Tu8FeL7lxpNn9E1b7UT9SM-Dlkdy5sK-zJqAUM6BhhsGeuF2_yYpf-ECrY_k0U-GQBn2udVENRpaajmCprRfQYv7oJyyKgdble2smfq81lyEebnPzq54BDHiUNC95jGxtsUZoBLDEM-zPq47ucA45Mps8BtpVTIZZVY6YQyhHTSmW3XuTGHPEw22fOb3ljggt1_pdShg_ZHNnnHPuJXoiUiocfv-32_Rm1Q__i707cXbLgT9aOG-vJiuUIOIrI8jkEIQWAdhHpY2STzV30Mh3e9jmJGgiqP9ci309VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101828" target="_blank">📅 22:48 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
