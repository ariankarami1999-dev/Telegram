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
<img src="https://cdn4.telesco.pe/file/GF-xu6iFIVpSV9z7HIaSBtJY3D--QlQqFiEHza23tlxtv_Tpy5G8oEHBfyyYCJjUl_o9zS3IeFkpcUukoqxQs8SQoZ4G64ApaTyj5B2pn869DMyhC7TQn4IJigR3dSW1KURFIRfTRP0c_yL8p2o2uB0BcA4aSA_gAIUP03zpWQTCKbh0WS6c5mufhtn0vtGB9l8SAI-FXi_KzKEY2_nIRZYLakqNt-XU3tROjkshUmDk4Jm7x1-E6K1JtnEt-AkSVChHQ91qxDQpTxKbfvQbYuRzR9FcZY8KByvn-9ZZ2VJxErCIhzzfh4UcQV3j3pLC8HTbrgrXOk4G8pDhycXnag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 10:14:50</div>
<hr>

<div class="tg-post" id="msg-663378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔹
سخنگوی وزارت دفاع: دشمن با روایت‌سازی‌های غلط به دنبال ناامیدی و تفرقه در کشور است
🔹
خطوط قرمز نظام همان شروطی است که رهبر انقلاب اعلام کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/663378" target="_blank">📅 10:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpIfJv-ZDTYzvW8IhfSqrp56XDBPu7izXaxhBTb6Jhz6F3-JwZ7NHlX6_kOsh2MyAmRtpFEMmdGsz_c07fvbbrPAD4ZVbNLc7Rrmpk_S1Y2r2CDDE4LSH16HVLlD7HeD0ySZ-ZiKYr9A5JdLWM0rQvX8HG_b9lOK2vf1_9-QCUbh-dZ53DlMDr4MDUAorDjlcWWRgNw1oWSyb4tzKymNkHPuNSM08CKJ3IVSriWcufxrWxZavQ7tpY5YG5VEGWCuvq6Um15ifco2Vb6sTrC70r4wD07ZePlgY9hGJVbCTDNdd-TX5vuZyY7_CV6S9bkC09Xhem2pTD46TTnHvBQ6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل دو تمدن باستانی؛
🇮🇷
🇪🇬
پوستر فدراسیون فوتبال برای بازی با مصر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/663377" target="_blank">📅 10:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdZHDwcPrDNYCmQl4vVfKVQDWYQsZPPr3Iv9gnNdXCnLn6vTl7TG236poOW8Bg6f4vHHrHB6n85GcVs-z0zMsHBzo4O77acTJpLdISm7UK3japZkk4XhcTF2yAbujDy5WEhIZZ1MBugvCq0sDAGLh8XIKlWdJepFoNhLfrEI8ZMmbdUJSMZBk19VC5If_4sUr3dsmh3_Mot6SKRdThVLaIm_Ay_87E0nTEuZhlnkyE0_VwaKAQtjQijxYeUcfx3AcV40Qe3l_lw76dfIqGCHFM1Yip2kcECQUHSvvOTV8D4v-mZ0Ny8LqhKSdbx7JKDwClSk-oaMFIVouUxHRD40Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDUIv8805mGKa4G70s0SEgGIlclul76kHtMeDV-DKj6v6EJyRc2ZEchT8z3zVjmY57ZrNwGCriOkGGXa0wxfiboLmtS71TosMV-Y9slq26hxO44PnBM-RncMn8b2w3RmiLQCec9zNgxa7kAkOC5VYVpzW77cT0q1NE4aLn1_FhAgPOVLHQdTGjU8Qq8sz_eOmm9pOVmOppskGPPOM0EvE4Wm7Gn_x24b_qd-edCnVglSmU_Kx6Itm7Ob8Q6Rj9Ot0opnhtZEv88KOKuYcHWRcfNfRY7JDZg2Gt-XmgFsdZyzs5ZZnao354TVERgFz0TwZOfopcWRLN88A10BVfKJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNxmI8RsOCOHT1GTfRkpznlsqsbpOglxbFxQ6kISk6WvXWgK9jgIjIy93vbpjPTXT41pqmVEL-feu7TOznymiIE6BYoulObVSvbd2iOX2W8yPgsgAe25n5lZlQOnNCjGi0FRiiGzOt4fPHu6J5qBvgM6CI4pEGFPWxPJl1ZPyjMx-acC9zkTY8dQjnxaLbI8FCKeF-RUfxAua8FKJjYFFGU4hLRZmC9Em6vRlENEi2ElpMjuigQCmUyG3238DkGcaydly_2IYWwsDPPtpd3g0uC241XKZFrNxMjWSpSWWwmzGOtSjw0CMVbu2Zn1tszmSCphomxrobWSiOaFMBwpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLmUHInosEWjGhVFAGAt_EOiG8_wt4sV5chMteaF439oAWzuRReDczckWqnRytgq4lyW1KkLwwh5-HYFJcmslYN5q_pmRWmeYEtTheBqVkgUHNdLCav6L0tjooolqgiG_82TsC2MG2XO-krmHMdfqtc4ZpZjwwMqkR4CeT2YlqMvblYWDBBnHLHhu7pV_hN1UMQiIKha6Mu0YJL_nTPArAOXn4TEttPpAdS2_qGmdXDMo7aRTtVRUyagV6CgOKI6YBS_q9KOAKy6x6W1KGHyvmvdDdfC_WE1RjN1OpARIHzhh4dupZ4pHX1rS535pdCnNSNjxCuDpWiM4rAMNjswCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_ZQsOMWYvVPneKfgrIWlWHUOBhhrKBQs4vHELF4HfTy6O__ej4pxnCeU6-s0xiigJr0MPnMDAbEz6On9MLGC9JTzPC75Bbrbv7QX-QNLjm2K1HI1KYuUIMHfbH9tU-SzC1H6lG7JuSArVB3w-FCGBrUmt8KKPnFfirheAUP72yC50QY334qbfefOKks0YNX96on9pSviCgTNHM_yy_rYt5UHcb3Ckk2zBjLUOndDlI3ScpdVmXdkJ8BZ4JHYuIvgIIpzrhGK2ubUJ_D1Nl-cQjw-gkjs4U4GTrCwvsoowSlIifr8eW9591jnDuO4S1_6htaqnAaONp0HzdZNZw5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcmgIsjCXTWaAfTlj95aF5ioG_3uIq683lY5tLO16cuPlzkW0gXroTp2uKDw_59o4crMPIv2CBH2c9tBw7UPU72EskKFJDx87A8jVkfMaKNA6DTDyGuoFy-hpOQnc49ORW1vCphpVSygKXL7XHlfy1PLXV7BevbdQv4v9WvZgCgtCRmbO8D6BeaJQtA9lzpSDS4X1yfSGD7-IMDyzrjYXz5nXLJOg_QHBw_BqYbZV3RzPNd_M2jY8Uz473e1o1gelrD_DriKF7r1tr-NdPjOJ0jJwjoQlh7R-dFXbK3S8-z6GpVKcC9iqSbRSe_b4X7iST6Kqdx4NlV_mbsl5-FNvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
فقط با یک کنسرو تن ماهی، ۶ غذای فوق‌العاده خوشمزه و فوری درست کن
🐟
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/663371" target="_blank">📅 10:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm2OpuwGS7-U8adfe1csumWz7QLyEOSpqyGl2PenUg2bsBuRaghXv9pMDc6G8ezp9UwaD26s5D3gSk8KX6EOCz-oD-JK3PqZKOgMam-nggIaHuUoiPfNzL4JaO_H3EP-wm5u8sVooPCO_TZEwC0LbBhj_Rwq7WVpG95qYsF-DGlUTVKI-mPlvbNzizhzl4zR6WDQLfs5B708SQay0LrswjK0qGtmxCFi4TE15F3X1C8rv3ClB5_5vtP588ukBqr6jkvL-vivOwJGeEIVxqwcMyVFLKMcBOnbo3w8IW6z4BvcB89VqxIMLWnUeo_W0ckoaPFsboBIdzx46rblZqJfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کار ایران سخت‌تر شد؛
آخرین وضعیت بهترین تیم‌های سوم
🔹
با مشخص شدن ۴ سهمیه از ۸ تیم برتر سوم، شرایط ایران سخت شد: با ۲ امتیاز قطعاً حذف است و با ۳ امتیاز هم صعود قطعی نیست (فقط از کره و اسکاتلند جلوتریم). همه چیز به نتیجه بازی با مصر بستگی دارد./ فرهیختگان
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/akhbarefori/663370" target="_blank">📅 10:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI_jcNxHZlpKmViSZwu89OBDjCWjolp2_JV9hen4QRiPf5GkY0gbqv5fZTvBEcpFhmY2bYx00sJ-WqiteI7gQSf-kCb-uaTCw3AYxTtATa8H6DwuDfv-rervd5q8va7mDcN-CylcnQzQMK1r1lwy7loOB2QLlNdZMnkBeH0A5RtEYLOyhf5VydvVf7hRV8QyQ4HfbxTDhCo_IDRk7NJJMGzDiZ4r8aDiXtcIu_DSb_jonBtpwBaKBeJZHCSrwR-YriSMETaIT7of76BFx9NGfnIvdzEEHy49xhqQQaMM2VaDX6J7W2wS7hno5O0zr18udndg_tCxtnFvScVa8eSAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
وال استریت ژورنال: حملات ایران به پایگاه آمریکا در بحرین ۴۰۰ میلیون دلار خسارت زد و آمریکا را به تغییر آرایش نظامی خود در منطقه واداشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/akhbarefori/663369" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔹
تقویت حضور دریایی آمریکا در منطقه آسیا-اقیانوسیه به بهانه مهار چین
معاون وزیر امور خارجه آمریکا در امور شرق آسیا:
🔹
واشنگتن، علیرغم اعتراضات چین، مرتبا کشتی‌های جنگی خود را به آب‌های مورد مناقشه در منطقه آسیا-اقیانوسیه می‌فرستد تا «از آزادی ناوبری دفاع کند»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/663368" target="_blank">📅 09:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663367">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1fc177d56.mp4?token=n3WeXC6HwCSV1KO8EJyJyaeTZ7DK27iZPzYyjdpKJK3zVM2A0JTdXTqKXEt1cCBEPKp40a-okdAxy4AyoN8GhiCmKZru5WiacO4Y1PeVlMvbPvJAr1WI_citFQUa4dGTytA1194NK20GTZPDvjHnnga_W_rkHuYLXtPVGJmyOm926s255qok_kB-MF_tp3e6Owb7Vd7DjMOc8ielh_yK7G5hBGCLYPProiQBRSViy9V8-_xnVGkiYupMiT6D-cAQK5qCTQZUZ4njF8vxyyJSc4iFA-owelNXUJy2QJwR6V_0WS19jm-CaI-0HaaRBgwfvNRujzqQna5eVvX6IQjKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1fc177d56.mp4?token=n3WeXC6HwCSV1KO8EJyJyaeTZ7DK27iZPzYyjdpKJK3zVM2A0JTdXTqKXEt1cCBEPKp40a-okdAxy4AyoN8GhiCmKZru5WiacO4Y1PeVlMvbPvJAr1WI_citFQUa4dGTytA1194NK20GTZPDvjHnnga_W_rkHuYLXtPVGJmyOm926s255qok_kB-MF_tp3e6Owb7Vd7DjMOc8ielh_yK7G5hBGCLYPProiQBRSViy9V8-_xnVGkiYupMiT6D-cAQK5qCTQZUZ4njF8vxyyJSc4iFA-owelNXUJy2QJwR6V_0WS19jm-CaI-0HaaRBgwfvNRujzqQna5eVvX6IQjKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برخورد صاعقه به فواره مشهور لهستان
🔹
فواره معروف در وروتسواف لهستان، پس از برخورد صاعقه قدرتمند در جریان رعد و برق، آسیب قابل توجهی دید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/663367" target="_blank">📅 09:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663366">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔹
طلا در آستانه ثبت چهارمین کاهش هفتگی
🔹
طلا تحت تأثیر تقویت دلار و انتظارات افزایش نرخ بهره آمریکا کاهش یافت و در مسیر چهارمین افت هفتگی متوالی قرار گرفت؛ نفت هم با کاهش نگرانی‌های عرضه، روند نزولی مشابهی را تجربه می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/663366" target="_blank">📅 09:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663365">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYQdgEl4NC_0vsJ5BdFG8Q4Fl-TPp9zTrCmPgS4uI7kodfUcRbR3XNQyHl79k6p9Pbc0SMD4MhPoeCLokdW3NiieCksHJ04ewcNbblaSixRF1ecINm2gyng6kiRvSNjwYiNMGAM-FBz9L18klHCW75NVtuqskHb_KufjeVNWz9W1oCaMo9vx7QNMjSpvfoYd4m8grQQEN2s1Huhxwc3X2hICB60gFiMFhHv3vdjfIoE9fraNb61A_42U8qwagnicvlvRA07SHqTeLZvUa2CXjhmY-Mo_0O5x7X5LQv3gIvbNHW47GRNOa6eUEabYlgxmNmYk54rpNhMegvkveBUUug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
همه سردردها مثل هم نیستن
🔹
سردرد همیشه یک دلیل ندارد؛ از استرس و خستگی گرفته تا مشکلات سینوسی و میگرن می‌توانند عامل آن باشند. حتی کم‌آبی بدن هم یکی از علت‌های ساده اما شایع سردرد است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/663365" target="_blank">📅 09:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663364">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7819bd9f99.mp4?token=tuLijBvm_bRZVaGYlvtTuH7sNV_AP0YEwXQZmajEzk2rC_fY5V2LS2brrjJsEBpuQZXBU5Xdq7ELsK0jbVfrRN0luv_uOPA84WojBMkekE5LpVB8uYJg1km86TAhAX-En5OQPbon7vyA3hH7RZXU31DJxK94Z4pCcMLigaZ5OplC2zllrknrnHxDDM-_f6k474WIJFCYqAgKafdeIgHwBwPiiiJkO03S6hU9bBytfQAPJN8kL5tmw-TvdoJUfkxpIBCuui3GUdl8ZthXiC3D4vMzVhMYGASU0fd80hkyW2dDkQ3CljChcAuS1GKFnu2NGeIvFTC-voR-ghirA9_Rmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7819bd9f99.mp4?token=tuLijBvm_bRZVaGYlvtTuH7sNV_AP0YEwXQZmajEzk2rC_fY5V2LS2brrjJsEBpuQZXBU5Xdq7ELsK0jbVfrRN0luv_uOPA84WojBMkekE5LpVB8uYJg1km86TAhAX-En5OQPbon7vyA3hH7RZXU31DJxK94Z4pCcMLigaZ5OplC2zllrknrnHxDDM-_f6k474WIJFCYqAgKafdeIgHwBwPiiiJkO03S6hU9bBytfQAPJN8kL5tmw-TvdoJUfkxpIBCuui3GUdl8ZthXiC3D4vMzVhMYGASU0fd80hkyW2dDkQ3CljChcAuS1GKFnu2NGeIvFTC-voR-ghirA9_Rmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
فیل وحشی به اتوبوس نیروهای هوایی در سریلانکا حمله کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/663364" target="_blank">📅 09:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663363">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔹
رقم کالابرگ چه افرادی بیشتر می‌شود؟
بر اساس گمانه‌زنی‌ها و اظهارات مسئولان:
🔹
افزایش اعتبار کالابرگ هنوز قطعی نشده، اما در صورت اجرا احتمالاً فقط برخی دهک‌ها (احتمالاً دهک‌های پایین‌تر) مشمول افزایش ۲۰ تا ۳۰ درصدی خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/663363" target="_blank">📅 09:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663362">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3rEp4L8Db7Gizcy5S6rmY7lVhsG46o1THnd2EpqgpFbqKrIN2_bLJGAd7AqFfgvCUGX8XTshCyLvVaK_oHKX1GFTLSicgrtsWSrQ7ZoUKft58_L3U--pi6Gk_HZHyAmlVdOy3yN8DQ5KztPD35R_awvH35TkSjBVXb0vHO5o7RH6wqFsWrOAgznwshQgKMLIPPnBe1ByXZdR71Cb-jCipvTLwx2ndvoyrwfU1c3ek4UOQ6uUkW6Txf5kGhzq-Pc789RS7tb2m56y2KGVbESYX9Ha6nBqFZalxrY511cIAPd11Cjs2TKFTh8Ch5G3c7AmS6f6iiUMxPbZe8t1eIibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بازارهای آسیایی در سراشیبی سقوط؛ بیش از یک تریلیون دلار دود شد
🔹
جرقه سقوط با افزایش قیمت محصولات اپل برای جبران هزینه‌های تراشه زده شد و نگرانی‌ها درباره حباب هوش مصنوعی را شعله‌ور کرد.
🔹
کوسپی کره جنوبی: ۸.۲-٪ (۳۴۰ میلیارد دلار)
🔹
نیکی ژاپن: ۴.۵-٪ (۳۵۵ میلیارد دلار)
🔹
شاخص چین: ۲.۱۵-٪ (۲۲۹ میلیارد دلار)
🔹
بورس تایوان: ۳-٪ (۱۲۷ میلیارد دلار)
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/663362" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663358">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JE59kcBWxz4yJBmXYG9SN-pPEZTBQCuvQrasiVB7Aq3lFlSRQ_G5khnyPZOb8M9GtnF80eFz7jATHirAK9zYh7a_Y4GG2ZuSu7334OxcXg_d7qeOb-_-idpqlvJHahCdB5VLdSUlcC64U5AkF91mvA19PwK5BjXSK9f1jWK8K0gsJO4Re06KCJ1ICkYv-3ltZlkHY0ujgCfYRhmALPFAN0s1BWxi9ANQJGPgwjb-xW6hzg3LGACNtYAGpk5PwsLAsSJ6LEnsLgFOJhtscFU_0g3YSkhop_FMS0QyvnELOIR19p-X3PhdNDLO04OThFYNCWNhBfyexhl7FAy6kkzJxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgQ2VI3w1ouBiILivafDio1DGqmOOcBJJ0wagkVXw2E6hSqHtFVqaVFAcsycqXKam8FY112NOq2vqvnu0hrcDxrbbSSSjnFHoHNQpyJdP1-qRowVG8BqomGAo3o1BLn79sgeBFD0-6StUqE8EtaXafpLKn1xGJa0Qwb6uSD5Se8hoFVm0R6fFYdDfEnki3XsgbwepSOpRzvqa54yEY_SHjSbRnt9vQ54J_BezlY946R5fK3r7k9_RxZwC9QOnCfXR28fCKygbnZEloqwOuRKBvE6QeCt9x1rieXlhFkm3GWhdlRQD1ol4X8A7MCnh2yodYFYEtEGmyGGyiNjbhCn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2GPTx9m85Kv70Dq4iTX81Hfb-YN0WKk7q6QdPJhdRZXTKTCEVmjrIsBYYIS68ZlOj8hvDw09zgubMsP91sMhRsa5rimu7r18W3Hb2DkP5x4RCJnq1yqrPOaRPvGUiipRUfWlvCcLr_nKNQFscBqaU3Tru9Ba9Rl3B4eE8CXs6p1d25ykkIThgA0QOiIuRbZ128lI_B4xgu09GyMr6u0Fvap3EPCmIj20ddzaySgiWH0f2_6fgZ4sG1XfYDhCeWR6GF5GmkYB7eaBReEsA97IYGOYgba4wsXU08IewHi-tVf2_K8cavPlWRH-5qHSNb4Ro9LYi1PXOIKR7rOMj9L_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iio5jXDyyR8Qup4cRbbyVfZEq_XX1KpQS-6PuFh-AnFvoCZmg1s_WLjvkC2RnATETf1QC6xaqu1GwGL0vR2TC9_G278EpVJcMkBr4hmKvm8iGLfmq8v18eSUi6O1YWuyBTjVIn8hQT0GmJucEeEuqhwO3PXWRZM7R7dJwayc5clzjAtD5AOLWmDsUrO6bFT4T2hFrjTUR0e2qn-cy6RhDcp-ZwOlIckSjBXOot6hXRXONj9dOI22qOMsbe839WeIcDr4eMoQBDhjWXy4wu5ON86_HYnnnkKdfKK92GEeaWXzhWoDZrMP-mOyq9tKnREJ56qOWH8hQrUQuTvZZMEE6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
بازدید ملی‌پوشان از ورزشگاه لومن فیلد(محل بازی با مصر) در میان استقبال هواداران ایرانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/663358" target="_blank">📅 09:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663357">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800f11bc4a.mp4?token=QslSsKgjlGJwMM51vgXkiuc5FNOIWyCfJ1rHxosjKoiH-k864mrXvnTDT1O9NlG1uED3kKVQY8ZmVWSonYl1OXYlGd4uioY6Mv3DYF5VajZCpWlmV-mJTZmuPsxqyB7ZsEheIMVgOr4DiMGBaM6NMXr3LWFg5_FOS2FE69oMOGTomUhMSJhcoCYFMkA-BAB5K59N7raMgAcAr4VRJZXY6ysQHIeICXEfSqjsuWgvaCDoFUz69cDQss520PVJUjVnbnB0DoWxuoCg3PoK8eGJh1CJNYNhdblJWzMLV0muR69aUIhxrfdC0h2HRPs7rc1XS4big9iYQUgoe_eLcIzrCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800f11bc4a.mp4?token=QslSsKgjlGJwMM51vgXkiuc5FNOIWyCfJ1rHxosjKoiH-k864mrXvnTDT1O9NlG1uED3kKVQY8ZmVWSonYl1OXYlGd4uioY6Mv3DYF5VajZCpWlmV-mJTZmuPsxqyB7ZsEheIMVgOr4DiMGBaM6NMXr3LWFg5_FOS2FE69oMOGTomUhMSJhcoCYFMkA-BAB5K59N7raMgAcAr4VRJZXY6ysQHIeICXEfSqjsuWgvaCDoFUz69cDQss520PVJUjVnbnB0DoWxuoCg3PoK8eGJh1CJNYNhdblJWzMLV0muR69aUIhxrfdC0h2HRPs7rc1XS4big9iYQUgoe_eLcIzrCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل سوم هلند به تونس توسط فن‌هک
⬛️
🇹🇳
1️⃣
🏆
3️⃣
🇳🇱
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/663357" target="_blank">📅 09:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663356">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da765a3b1c.mp4?token=FTGJhy5cKrEm2zMRbQJxoGZoy7f-mo8bBZFeJvI67lG05Jg_6v6Br_2fQUEkVblbgJ2uNpQyt1Gj7bgWARX_bbcRjD8fGRTrccsqKiBggoaAXqslsl5CCFjzwG4NouY2s-saY8DcppyE6YMLrikbv-u92DI4Lava6alJotAtshcs6LrjA5FWMNpY1ALUGmqjg3b0-Bhm_qywMiLXTNJHpzZ3hymiQ9yh5Ln39o5a7K-K22LRxdjhtGkVI8A5RR6ZwDHY2nDGTpnBXAUaZ_46MrSLtndgp2yZkacPD6K0AMoCJpO-W9eR8gcSEeuYeduhXRBpPkrDnywF4uL4IjMvhKGSasnDXnkaejJLDyUTqJYGTVI4bWPA2fnH_igIQj3vRNq8lINU455aS1T2OyEsbmTFcUTZastsggtmPO3SKE0_lpuuvv2URyOqHd-5Z2Dl2UBCBHq2Qq6ObAdhOcbN7oFky9fcpJCim65Gp83DmvYnm8ncIRDpwFJ6CobmlCFgXUgwEcAM8fVfrUchRMLMLwraFBj2CGwp6uRsk3INwje6g3biC5Lu8QNTc047lYiMxq2fcrwQEru5CY6k_49kIHVFpRwp04_RTW6XlTre-YbJXuz7pP3llzE4gF9rEo184tkFbEWjLQntaQAD2yMk3IQN06XKtyDIxQFj54JKumE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da765a3b1c.mp4?token=FTGJhy5cKrEm2zMRbQJxoGZoy7f-mo8bBZFeJvI67lG05Jg_6v6Br_2fQUEkVblbgJ2uNpQyt1Gj7bgWARX_bbcRjD8fGRTrccsqKiBggoaAXqslsl5CCFjzwG4NouY2s-saY8DcppyE6YMLrikbv-u92DI4Lava6alJotAtshcs6LrjA5FWMNpY1ALUGmqjg3b0-Bhm_qywMiLXTNJHpzZ3hymiQ9yh5Ln39o5a7K-K22LRxdjhtGkVI8A5RR6ZwDHY2nDGTpnBXAUaZ_46MrSLtndgp2yZkacPD6K0AMoCJpO-W9eR8gcSEeuYeduhXRBpPkrDnywF4uL4IjMvhKGSasnDXnkaejJLDyUTqJYGTVI4bWPA2fnH_igIQj3vRNq8lINU455aS1T2OyEsbmTFcUTZastsggtmPO3SKE0_lpuuvv2URyOqHd-5Z2Dl2UBCBHq2Qq6ObAdhOcbN7oFky9fcpJCim65Gp83DmvYnm8ncIRDpwFJ6CobmlCFgXUgwEcAM8fVfrUchRMLMLwraFBj2CGwp6uRsk3INwje6g3biC5Lu8QNTc047lYiMxq2fcrwQEru5CY6k_49kIHVFpRwp04_RTW6XlTre-YbJXuz7pP3llzE4gF9rEo184tkFbEWjLQntaQAD2yMk3IQN06XKtyDIxQFj54JKumE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تحقیر بی‌سابقه ترامپ در شبکه اسرائیلی
نه هسته‌ای، نه موشکی، نه تنگه هرمز؛ هیچ‌چیز به دست نیاورد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/663356" target="_blank">📅 09:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663354">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdmOPxuJ-J1vozUZvFwq4_I3ljpPeY6PV1hZckHw5f1KpqXMVYOrViXcPOBCZN6398lscIZ834CjggcBFnGjLhRHrUFav-zo8w8grQMOlMSBF3lKerNPQHSr4DgSWrd9s5V4BmgP6L49X9WyV8ThSzV-JPjLHMo4A5kvM3SPnkXAp3SrOzeI64HBWd8jtW8bKlu15qq7l4Gd5XVCNBSzbKpb45i3-qV-YqdugsEpNjH38QJwDL8O_fL079qlpOERlrWhkuD9MLo6pM27DwUzo7h9GrGtnH42h5iCDd-6rNQGYLrIGc6Bnhz7R2on-mZpvezTVl9NBLobk0DGpRMo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubaOvqyWqQq2Wh_w-Cs0JhT4Hd4TjM92B1lEmWud03ipd8FOGIV7vVaZd9Zft-LfHtiNbkK_kXd3aNFfIL5rnoqO9EGs8x-MiVhI0DPwvmDgiAR0gN9TJYWu0Bdub0efb3oJZ8n5ryrmCrk4pMF8yzh5OAOfw1pTH-8ibyE8WU9SfZGlt_Z970u5FypevINb6BtaABVOdIDfHGEfTnbj3Rd_UUzvTMBIdlaBz-NDx0uGYYKqj0cVt_B-fBBCr-V9dLJ0NKHq28gGbClL7r4dffk5UnFMjOclZ2tBC14aQEVo78d-q9JiOt0hsqmKu467_ocqe5ZYWsDO4vO-jKVbCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
پوستر باشگاه‌های پرسپولیس و چادرملو برای بازی امروز در تورنمنت ۳جانبه برای تعیین نماینده آسیایی
🔹
این دیدار امروز ساعت ۱۸:۴۵ آغاز می‌گردد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/663354" target="_blank">📅 09:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b6d420eb9.mp4?token=Wrk-EHP47tX74y317Ji67oeGhR5B8S0eviAI4qCaaIs95UmR8RwMdeTKkRy9-7aPdTur4uab_hUDnIq5gIyicrkSJt0eYXB3hWKw3DDn_nfwFoLaW5a0D0cv8uSPAdYeI_-vb0LtrsYkJsUDhDuVw1L5MuGr4xFan9COGSiaK9C8JPyws2X_zkpghB2w02btSH_Mo8DlqXha0zkrnd3DKM-BhK7zIEIAlrdR3wTsaycu1ro2SM6McFCkIWlrKDzTQlajf2V60gbpSzex8BTHCE5KNUoGNejO6tH-g_QjjSdZvA7E3rqYam9sXKvQv0Sp_s99F8ONPT8nZnlOG88yZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b6d420eb9.mp4?token=Wrk-EHP47tX74y317Ji67oeGhR5B8S0eviAI4qCaaIs95UmR8RwMdeTKkRy9-7aPdTur4uab_hUDnIq5gIyicrkSJt0eYXB3hWKw3DDn_nfwFoLaW5a0D0cv8uSPAdYeI_-vb0LtrsYkJsUDhDuVw1L5MuGr4xFan9COGSiaK9C8JPyws2X_zkpghB2w02btSH_Mo8DlqXha0zkrnd3DKM-BhK7zIEIAlrdR3wTsaycu1ro2SM6McFCkIWlrKDzTQlajf2V60gbpSzex8BTHCE5KNUoGNejO6tH-g_QjjSdZvA7E3rqYam9sXKvQv0Sp_s99F8ONPT8nZnlOG88yZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بارندگی شدید، شهر هوانگشی چین را دچار آب‌گرفتگی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/663353" target="_blank">📅 09:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663352">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
تداوم نقض آتش‌بس توسط رژیم صهیونیستی با حمله به جنوب لبنان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/663352" target="_blank">📅 09:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663350">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2543514dcf.mp4?token=GwX7SMyBV6tgeo4rbbLZdawl-4riJz1Fl2T8xxKIkc8FXyUSg6SvADvRzPYkwqlczcne-25wh-dZ--NCEU1k1C1ey03S8l-zRD9O45lUFCQspn8yWf8aVanClvCLKEw0iTFN3uMmOwNCsWXTJwbxo8iRj4OLLkV58L68oFs4-9zgoYNgTTvsog1XZIl5ACenzuR9fsth4-TAU5HjLICf5bqlSf1g34b1NQTKP0cVfCiRmIrEpRaaax4Xd5QocAOHpNbrG5NI5YuImdBXefYWiC0-7Mgnot7Din5gkaoUjhHpUWWfgGj-qbWTxMXZCvVAMD6lvYdd1xdkF93PqFxjdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2543514dcf.mp4?token=GwX7SMyBV6tgeo4rbbLZdawl-4riJz1Fl2T8xxKIkc8FXyUSg6SvADvRzPYkwqlczcne-25wh-dZ--NCEU1k1C1ey03S8l-zRD9O45lUFCQspn8yWf8aVanClvCLKEw0iTFN3uMmOwNCsWXTJwbxo8iRj4OLLkV58L68oFs4-9zgoYNgTTvsog1XZIl5ACenzuR9fsth4-TAU5HjLICf5bqlSf1g34b1NQTKP0cVfCiRmIrEpRaaax4Xd5QocAOHpNbrG5NI5YuImdBXefYWiC0-7Mgnot7Din5gkaoUjhHpUWWfgGj-qbWTxMXZCvVAMD6lvYdd1xdkF93PqFxjdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویری از برگزاری مراسم عاشورای حسینی در جوار مزار شهید سیدحسن نصرالله
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/663350" target="_blank">📅 09:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93323a9d2.mp4?token=KjGOIT9uwTBNho8EWgC4Umilcwk_w7b25zxM0JDjw4WiDGkQ2itte8fOl3KigiykONN_hT5bU8KbnN59rwcbeB8K-KHvJGDqPOZwlLsXOvpDPqUwakWAQtlNyaiGMs_oLUnTYIHIoVmy2gY5gvHCWElgGqYw7VQFzU1noAth2IYrmN5e26Idy4hBl31dABnqwVTGuHH1ifWeDaMEDB2MJ04S95rmbH8VIi1C8_wi86nlbBZcOMeHGDIPcKe-gArDnp53RAGkJGjDlN-ikNF0WFXoy9TTKGIg_cFlY24Ti1-2TgxZuD0LWzlSKWMkUAX_Eb8Wdo8l0cn2o98UF4AVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93323a9d2.mp4?token=KjGOIT9uwTBNho8EWgC4Umilcwk_w7b25zxM0JDjw4WiDGkQ2itte8fOl3KigiykONN_hT5bU8KbnN59rwcbeB8K-KHvJGDqPOZwlLsXOvpDPqUwakWAQtlNyaiGMs_oLUnTYIHIoVmy2gY5gvHCWElgGqYw7VQFzU1noAth2IYrmN5e26Idy4hBl31dABnqwVTGuHH1ifWeDaMEDB2MJ04S95rmbH8VIi1C8_wi86nlbBZcOMeHGDIPcKe-gArDnp53RAGkJGjDlN-ikNF0WFXoy9TTKGIg_cFlY24Ti1-2TgxZuD0LWzlSKWMkUAX_Eb8Wdo8l0cn2o98UF4AVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول تونس توسط مستوری
⬛️
🇹🇳
1️⃣
🏆
2️⃣
🇳🇱
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/663349" target="_blank">📅 09:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3211ef190.mp4?token=aed7BoHUDhLrGAj1UFWvp5XJpCFxmauZ71EZ4sBGHABPQGQ-RMlnhWm3RlR4SP4xp5VqJ5Ep3Xc1G5PX2mkkvUNbntTLb6OOYXJl6B4Pi3Q8IgHgL5YhXn6PFk9l8U_GkhqgD03xfk3eDVKmYYH5wM6DSOgZroqbtRp59mZp-LAtHdr5Yj8h4kLBYzyvjUtxnqAvTJrrP_CtGsiZGisBbNbFk6WrZdPHFud2vB4J29aMQQITTAKdqdfG1tuMuWUiX-jdVBB6vlL41hQt9VKPtraSW6Zo6F-iv5TY_eHjEjgfhPMrE8dJs8okeHXvvvdOCMzMbWdqalyR7sJO71Vblw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3211ef190.mp4?token=aed7BoHUDhLrGAj1UFWvp5XJpCFxmauZ71EZ4sBGHABPQGQ-RMlnhWm3RlR4SP4xp5VqJ5Ep3Xc1G5PX2mkkvUNbntTLb6OOYXJl6B4Pi3Q8IgHgL5YhXn6PFk9l8U_GkhqgD03xfk3eDVKmYYH5wM6DSOgZroqbtRp59mZp-LAtHdr5Yj8h4kLBYzyvjUtxnqAvTJrrP_CtGsiZGisBbNbFk6WrZdPHFud2vB4J29aMQQITTAKdqdfG1tuMuWUiX-jdVBB6vlL41hQt9VKPtraSW6Zo6F-iv5TY_eHjEjgfhPMrE8dJs8okeHXvvvdOCMzMbWdqalyR7sJO71Vblw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویر غریب در دل رویا؛ آلیس در سرزمین عجایب - ۱۹۱۵
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/663348" target="_blank">📅 09:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663347">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔹
گروسی: بر اساس تفاهم ایران و آمریکا، آژانس بر بازرسی تأسیسات هسته‌ای نظارت خواهد کرد / تبادل اولیه با ایران انجام شده
🔹
وزارت خارجه پیشتر: برنامه‌ای برای بازرسی آژانس از تأسیسات آسیب‌دیده نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/663347" target="_blank">📅 09:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663346">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff2Ew7Ug5Jg_gw5-k_ke2ysqzoJ4O6oNrO4F7LIhvRdhy7AFcsIYZ0EP7iPrz0G6o3aLRz0nMISJhfm9BKKvKC-RimXFaIgo84eVvD33kWDdKw9BSnHJcceovtrFe2XTp9aMQmylKdSkSPoHzkdna12L4AgWeR6JTMkq4y1j6rkOodJ2Lzg_YSpq9ZtAPhj0wmkG9ImNaniwazu4a6UENgnnLuROs70T_uWi4HKeEpwKDA3xtEJ8jjMe7wqdjQsHm1I-R4j8wZbxTaQw1jeECi341u19_4nWKdVfpiLamrPnzvcNur_v4hnR2iP_X0D3_MC0vMDDyfUgOs6X2Yhlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر برگزیده رویترز از بازی امریکا و ترکیه
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/663346" target="_blank">📅 09:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663345">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760af42690.mp4?token=Hp_A6rXWV_Dn_lbOVRe1cwBrSUAF8c1QAdfYVxZEpzBthgQ-xfQB68gfbUqk4iL1w-cWYZGkdi4UujP9RXbPiyux5zDFEHyEfciX-QuRoW3OSlsRb0Q4EkYZ4M87XJgJ9CAMytvQO_roQCdNlWLVr0fRR3dbCtNgQvADCWsdO4P9weRi4nKSNLDSDE_YBY8JpFzia2CviKZnVPhc02wf7laUXDfAQCznaI7WmCQK0hmusjbdbvmfl4Yv6aKKdQFZ9OYKMWphmB4BQqob9Vo8e8HguiPcHBy5YdrnGcgPfnTGCrd8TZMm3vhIXJaOMbGUxy9jHlXyD3aqH-TNJIaNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760af42690.mp4?token=Hp_A6rXWV_Dn_lbOVRe1cwBrSUAF8c1QAdfYVxZEpzBthgQ-xfQB68gfbUqk4iL1w-cWYZGkdi4UujP9RXbPiyux5zDFEHyEfciX-QuRoW3OSlsRb0Q4EkYZ4M87XJgJ9CAMytvQO_roQCdNlWLVr0fRR3dbCtNgQvADCWsdO4P9weRi4nKSNLDSDE_YBY8JpFzia2CviKZnVPhc02wf7laUXDfAQCznaI7WmCQK0hmusjbdbvmfl4Yv6aKKdQFZ9OYKMWphmB4BQqob9Vo8e8HguiPcHBy5YdrnGcgPfnTGCrd8TZMm3vhIXJaOMbGUxy9jHlXyD3aqH-TNJIaNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قلعه نویی: تمام حرکات مصر را زیر نظر داریم/نسبت به بازی قبل آماده تر هستیم
🔹
هدفمان این است که بازی را کنترل کرده و به آنچه مدنظرمان است برسیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/663345" target="_blank">📅 08:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663344">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAV--3Fo0CbEFwuStkYkBxl3wwKfdHfL7BNZ61BfhTCJowX-A6WD7CE7svlXEHyKVAtFEOm7u6CdyowvvVLEddcmEIgEJ3inldhzbn17wgpM5oIX8eU5bedd5LYdJ0ijPccFcRhPgS7lFnCXA_Fgj_i_eYsvBaNeejblRaFo94cPkD8AFdm3nc4Mzrzp7QStelXDmZnX5YxgbDJIdFxg-7I27sbFij_OYpfAvKLiURQ25ChVE39BkrwEHQQRUWqsJJ7Wf07_eqTXrc575Amf8gXbiYqerbsI8xJ0zVDo0eZ0zmn4zV723AroYBFJxcRPJq1P3NUVi2XfvanUuU2dLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگر ماشین به شما زد و فرار کرد این کارها را انجام دهید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/663344" target="_blank">📅 08:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663343">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e4026260.mp4?token=uVtt7z0n1AcgtGvsw7hTK9AOMl12EeQ3tg6O7ewaAqMHvoNtOrvXvQJDp3hsOQogrLRhpaaMYxmtFso4GWZgHXMo1TtfqJ87bY-xCSalU_uPdflGm-KhiaTQON1Ds_q7vCkfL8TdFOFXbCKUhe_ZHgIuy0rT1dvmlWa03jxQdRG9uvmVyCWC-ZEtNnOKkJn59RU4B0hKK5Bci1c2dVet3h4KTq298oxEPleewFH-fuKOZWD7wBQo4UGVE8QztCDpQQdpF7hpRtpg644Mq-n8t5rUVnA_MapPkBjGZCPSsMRRs8tuXauhDEF5xopnYxt25539AGM4yxxmPRPT8e3wkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e4026260.mp4?token=uVtt7z0n1AcgtGvsw7hTK9AOMl12EeQ3tg6O7ewaAqMHvoNtOrvXvQJDp3hsOQogrLRhpaaMYxmtFso4GWZgHXMo1TtfqJ87bY-xCSalU_uPdflGm-KhiaTQON1Ds_q7vCkfL8TdFOFXbCKUhe_ZHgIuy0rT1dvmlWa03jxQdRG9uvmVyCWC-ZEtNnOKkJn59RU4B0hKK5Bci1c2dVet3h4KTq298oxEPleewFH-fuKOZWD7wBQo4UGVE8QztCDpQQdpF7hpRtpg644Mq-n8t5rUVnA_MapPkBjGZCPSsMRRs8tuXauhDEF5xopnYxt25539AGM4yxxmPRPT8e3wkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل دوم هلند به تونس توسط بروبی
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/663343" target="_blank">📅 08:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663342">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogHX12ws7lStjQ2lARlYOk4OflYmmRphjXj8TPWRr77bSKKFXrrhmVtAh8mxn14bZoOqAsaeEXvbs8tsqMZo7fD4aokTgNHe4l6pjKw5IRdQ44muV0ejJqWGfNmH0qBpiCDaXq381hts3_uDc3LENJglpZOXvwf9lqMzqwNDk9WGOs90EYN2abIPPLuVusyBxb_AylxN9NfXPbmSabmR1ESkvGiNSA5-1ErTqjnBX_VxGsTFWPZoVjZPYy61SmN3Xt2fPe5hqoiJfGUk9WnQsT11_Jr9R2UGxmJ_2HvhxsMDezFbE6ks0pJ19eztgkA7QdvX9nGlOx8xLAUlldzKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصاویر سپهبدان شهید حاج حسین سلامی و غلامعلی رشید در میان خرابه‌های محل شهادت
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/663342" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663341">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW4jTV4u0UMp4WH7DMLrproqbRTTQYzM20q7LQWtmRqxy07qx7Stk4_7NqBlD82AObE98Xrd54WfvzWiiplxeUh3LLLI8bLqtvq16E8Ke8LvU13LZiBObBof-G2eXq0EmAe98AT9yMan1ftiKc-pUkyyjlyO2X9fxmwHvemNol1URLMaekjKQON6GkjpQBFIgoa7Wgnby1BmyRt86F7YPmLRn2QopJwDFx3VySlxeI-XHV_5TJCX6dmSUjIdv9H4sSprvRvMYVsuLLsC6TZFpZyWHMeSvaLQlTj7IkZak1wK9Dm7LRWLZvDC-vhY5nO56YQvmRIgTBe1wbFnOhgHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بیانیه بخش رسانه‌ای تیم ملی درباره احتمال ایجاد برخی حواشی در بازی برابر مصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/663341" target="_blank">📅 08:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663340">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a678551c37.mp4?token=O9hHcEzSsdxvVJGl0e_EyKwCZhUck1tpnKe9Lzn2_OqsbZwbuCBamM-pFsZQX_u-Zls_sScm31AzYfGNfQZieRvLiIiTO4tzhUxkQSCCXHmUxuHX4E_0NQd9PZDFLU9KyIQrbP7-obC-6m6Opvo_gfdGuSe7X4l-jwXPWdTIRJcOc2SJ25syKdZN6-Fyt1DyS9Gi7D-k0stXNfEpYjV6x7byWrHaxpyOvEfkU6FGzJqk1-osP811G-Bd675hBSRdLkxv31XIiSfFWKz7Q7i__vx--5-AprbDtFbkc_zV5d9EmHKpzs4qEClA4jcezqa_vUIRzti37X0o1iFWm2z6yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a678551c37.mp4?token=O9hHcEzSsdxvVJGl0e_EyKwCZhUck1tpnKe9Lzn2_OqsbZwbuCBamM-pFsZQX_u-Zls_sScm31AzYfGNfQZieRvLiIiTO4tzhUxkQSCCXHmUxuHX4E_0NQd9PZDFLU9KyIQrbP7-obC-6m6Opvo_gfdGuSe7X4l-jwXPWdTIRJcOc2SJ25syKdZN6-Fyt1DyS9Gi7D-k0stXNfEpYjV6x7byWrHaxpyOvEfkU6FGzJqk1-osP811G-Bd675hBSRdLkxv31XIiSfFWKz7Q7i__vx--5-AprbDtFbkc_zV5d9EmHKpzs4qEClA4jcezqa_vUIRzti37X0o1iFWm2z6yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تداوم نقض آتش‌بس توسط رژیم صهیونیستی با حمله به جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/663340" target="_blank">📅 08:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663339">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de93bcff08.mp4?token=mbH-1aPgubm-Ipb2YBSzpQDGcdRSZIhCpMZYRpbMnWe763ol5xBqnR1v-AHjWI70dvv0PuTfa209jwV0ZqsbgtKf-4ehBYywOQRCMVS1yNdaSboLAtEPx6rC6Ha-rQ1IvJP0UyiWSBldrdPOx9XopzdPbjHfMmmVGKHpPDxKS8gE7grkFfKCqNgp5YYxaImbSBEnkUwJLPXbpZkqtYZPvOPoSPaycmtY0VXjJ-VsRcvSfbQEXY1qN-0v_EV8xYb-rCTvvdnmNdRo0xw-BLjPlc2Kf_7l6Y6-vewZDUtwPXsbme8e9VIJGHIsULct17R9uFVQF_OzTfhIwJN4sa2baw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de93bcff08.mp4?token=mbH-1aPgubm-Ipb2YBSzpQDGcdRSZIhCpMZYRpbMnWe763ol5xBqnR1v-AHjWI70dvv0PuTfa209jwV0ZqsbgtKf-4ehBYywOQRCMVS1yNdaSboLAtEPx6rC6Ha-rQ1IvJP0UyiWSBldrdPOx9XopzdPbjHfMmmVGKHpPDxKS8gE7grkFfKCqNgp5YYxaImbSBEnkUwJLPXbpZkqtYZPvOPoSPaycmtY0VXjJ-VsRcvSfbQEXY1qN-0v_EV8xYb-rCTvvdnmNdRo0xw-BLjPlc2Kf_7l6Y6-vewZDUtwPXsbme8e9VIJGHIsULct17R9uFVQF_OzTfhIwJN4sa2baw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول هلند به تونس توسط اسخیری (گل‌به‌خودی)
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/663339" target="_blank">📅 08:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663338">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8fd050189.mp4?token=EPlGDtGUK3dNhQ7krhBDgotuXuXjaeTNAbfiwiNRbrDfxgzJcqoRMRfKpKWZ1qCreDOOIw__dgxw30RLEsAf03U_ZcMD5GFVV9j2hONA9jz-hESnrvMOc7m1th_gG2xOvQXU1izPQgLE3FWjN9VKDRiMxwm3q3maBxHA9gX7ze-db7NPBi6XQtQgvajfvqDbNYqSwFt78dpnupyZKIM7zrphEU1xkuv92QdUYeMsVwKS4vfhxi1NmI7jiFZbGEwALRcsgREAE8iFjLG67OM4-JQkKxrVfbfYdDkhiX6NNm1jwUCsj-qDDB4hd2gbhN_FQBR4DgD2F3ntXb-4BN425Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8fd050189.mp4?token=EPlGDtGUK3dNhQ7krhBDgotuXuXjaeTNAbfiwiNRbrDfxgzJcqoRMRfKpKWZ1qCreDOOIw__dgxw30RLEsAf03U_ZcMD5GFVV9j2hONA9jz-hESnrvMOc7m1th_gG2xOvQXU1izPQgLE3FWjN9VKDRiMxwm3q3maBxHA9gX7ze-db7NPBi6XQtQgvajfvqDbNYqSwFt78dpnupyZKIM7zrphEU1xkuv92QdUYeMsVwKS4vfhxi1NmI7jiFZbGEwALRcsgREAE8iFjLG67OM4-JQkKxrVfbfYdDkhiX6NNm1jwUCsj-qDDB4hd2gbhN_FQBR4DgD2F3ntXb-4BN425Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تاکر کارلسون: جنگ ایران، سرآغاز پایان سیاسی ترامپ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/663338" target="_blank">📅 08:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663337">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdT7zy6Dh9psaq44fA96bwojWiTVRPT-pCu6ob3RiZfkZFBqzJv7DztW2ajHXJPBz0MufPwP8KOagyseQ3_smUC50hA9sS7sUJytbpo3rJEA97Go_N44-G3AuEzcDHb54CGjN9NhA2S9nUxXJKX1cfD9PsEi_aeEEISD6j_M4CC15MnbSHAZ9rFtzedW48Cs49AqKTDD_fy3ImFP7z4zbk-pTUwGLHXWt6RdOkDgBy2dC5yKSb0wQeHIRj3lhzoMfKfeBuTngdzwBaOrU485Z8B14wASUPnKIzMKCA48G0ucIAQKYluLbkTk4msAUyURYVY10PNDsG9BJMevOFu1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عراقچی: شهادت سید و سالار شهدای انقلاب اسلامی را نه فراموش می کنیم و نه می‌بخشیم
وزیر خارجه در پیامی به مناسب عاشورای حسینی:
🔹
امام حسین علیه‌السلام سیدالشهدا یا سالار شهیدان شیعیان است چرا که او هر آنچه داشت در دشت کربلا قربانی کرد.
🔹
به همین ترتیب، ما هرگز شهادت آیت‌الله‌العظمی سید علی خامنه‌ای را که سید و سالار شهیدان انقلاب اسلامی ایران است، نه فراموش خواهیم کرد و نه آن را خواهیم بخشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/663337" target="_blank">📅 08:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd2a937f6.mp4?token=W7TFpSfAOsYQhqMp7qFjfy60dxP28fXnHkl2qTcc3Uq09y1eAwBuPvucPI1C1CeL6_X0BgKl_nuNastho05Z8Doy54f03WmfTcmRs7Ppn7rK9nAdDaWFtMz5FEre3pWzIr9rbA4ktcieHOTW8z9ChqHZS-GstEw2An7kw2YGH8FxZDn77P0RX6WajGoucnUA4by_sbWeSLNY-rSBINIwpezVRZCr_zeeNBoxibkVjlO8r5cxB3Ao_zZAp3efbZLvSfT-_2cDXpuiocH3LgeB5SUKobG2BTU5deLXAkoOs7TV6322FLXnNyNM-Pwfboy6FMYTFgHog8g0U5kb-nmh1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd2a937f6.mp4?token=W7TFpSfAOsYQhqMp7qFjfy60dxP28fXnHkl2qTcc3Uq09y1eAwBuPvucPI1C1CeL6_X0BgKl_nuNastho05Z8Doy54f03WmfTcmRs7Ppn7rK9nAdDaWFtMz5FEre3pWzIr9rbA4ktcieHOTW8z9ChqHZS-GstEw2An7kw2YGH8FxZDn77P0RX6WajGoucnUA4by_sbWeSLNY-rSBINIwpezVRZCr_zeeNBoxibkVjlO8r5cxB3Ao_zZAp3efbZLvSfT-_2cDXpuiocH3LgeB5SUKobG2BTU5deLXAkoOs7TV6322FLXnNyNM-Pwfboy6FMYTFgHog8g0U5kb-nmh1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل دوم اکوادور به آلمان توسط پلاتا
⬛️
🇩🇪
1️⃣
🏆
2️⃣
🇬🇶
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/663336" target="_blank">📅 08:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e77d85031.mp4?token=BCMscArWTlG_R5fjUal42djxKMbS4THtFY7cyBdPrqo2baDTBfaoslkf_o6z42UjcP6EzmmSf6Ri9IpVob-sl8I84uuf_f9zmR-dlcFh-ZRuL_W6Hp0lagnDBWmhVU-JGnO8CLrZc2f2b1aOZQPBVuJnoTILo45X0bwTrocEvZbDjVrsxGq7lra4I0_CTfx4g3r1p_HeDvFm84y1Z1xkBfg8RECsv6uqhaWKhI0rFTNKG6n177_8nP0dOsw9rT44NnU7kXY0fUSDnnGbRruIQF4z1e_4qe-eBXJ_rPDu1ZTC2khxk9L757EspMjFjA5ea5efNco1S74BAFPCfseCWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e77d85031.mp4?token=BCMscArWTlG_R5fjUal42djxKMbS4THtFY7cyBdPrqo2baDTBfaoslkf_o6z42UjcP6EzmmSf6Ri9IpVob-sl8I84uuf_f9zmR-dlcFh-ZRuL_W6Hp0lagnDBWmhVU-JGnO8CLrZc2f2b1aOZQPBVuJnoTILo45X0bwTrocEvZbDjVrsxGq7lra4I0_CTfx4g3r1p_HeDvFm84y1Z1xkBfg8RECsv6uqhaWKhI0rFTNKG6n177_8nP0dOsw9rT44NnU7kXY0fUSDnnGbRruIQF4z1e_4qe-eBXJ_rPDu1ZTC2khxk9L757EspMjFjA5ea5efNco1S74BAFPCfseCWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
۱۷ زخمی در حادثه زیر گرفتن هواداران فوتبال در مکزیک
🔹
در جریان جشن هواداران تیم ملی مکزیک پس از پیروزی این تیم مقابل جمهوری چک، یک خودرو در شهر کابو سان لوکاس به میان جمعیت رفت و دست‌کم ۱۷ نفر را مجروح کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/663334" target="_blank">📅 08:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663333">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5eb1e4138.mp4?token=NGqOCMen0ezhZ_1GZa3jCqHNoRfwQrcyrfpQf8y0wPL8lcrl6oE8aB8QlxVFNxvqf8HgstlhOlTJ4VTaswjTjOLoWYtSFWMxv1YfIPxNYGpALs377UoPDLiqco-MWul1Dv5ESDosfvIJ0ytNmsZD4a8912mE7e1HDQKiycJz81YubXzwx6-CO-33fm4nQ6Z2kh9q7tUaBrWKLtYoiH1Q26xemt5n-7l83N_BES8CyRKwDNls2ioid0rc-mQYFXM81k3SlbrW75bI49fM-I1mQY8Be08tyItCNXfafiC1Vn6Nzi80AMqrj_VywPtVF2J8HJYUNwwiXTIhQOsH0J1E-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5eb1e4138.mp4?token=NGqOCMen0ezhZ_1GZa3jCqHNoRfwQrcyrfpQf8y0wPL8lcrl6oE8aB8QlxVFNxvqf8HgstlhOlTJ4VTaswjTjOLoWYtSFWMxv1YfIPxNYGpALs377UoPDLiqco-MWul1Dv5ESDosfvIJ0ytNmsZD4a8912mE7e1HDQKiycJz81YubXzwx6-CO-33fm4nQ6Z2kh9q7tUaBrWKLtYoiH1Q26xemt5n-7l83N_BES8CyRKwDNls2ioid0rc-mQYFXM81k3SlbrW75bI49fM-I1mQY8Be08tyItCNXfafiC1Vn6Nzi80AMqrj_VywPtVF2J8HJYUNwwiXTIhQOsH0J1E-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول اکوادور به آلمان توسط آنگولو
⬛️
🇩🇪
1️⃣
🏆
1️⃣
🇬🇶
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/663333" target="_blank">📅 08:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663331">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426b696e9b.mp4?token=rA9jipskQWnFsCcDFVokHIiYzMBRqX9TjMweS2466dJBtIR_30rq_zN2wJCGBCfuLK2BI9dV1Fpf3Xe9blg_mxniEOnCIFvgaRHEtFWL8xK9bTGYdUbgiSgnBOG2sKbT3O3t1rI2MAm5raWLhu4A5_bp5xOYM_VADbwSoB05PqmzhnKfLO-1E5gXvuTcy1n67RnjuFGfWKqavgbO0J-cLR7fmKZnHPFuPl9Qjy_YZq2LRM_DRy6swMT3Jn_I-Ugld0W2DWQJDCpNVdxr0fi7JfH_ioO0iaRdjXcPxCEmLmNha1f1-hQZh4z9UKi6JWEwN8UiB3o6zwLVPxFlo6mdrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426b696e9b.mp4?token=rA9jipskQWnFsCcDFVokHIiYzMBRqX9TjMweS2466dJBtIR_30rq_zN2wJCGBCfuLK2BI9dV1Fpf3Xe9blg_mxniEOnCIFvgaRHEtFWL8xK9bTGYdUbgiSgnBOG2sKbT3O3t1rI2MAm5raWLhu4A5_bp5xOYM_VADbwSoB05PqmzhnKfLO-1E5gXvuTcy1n67RnjuFGfWKqavgbO0J-cLR7fmKZnHPFuPl9Qjy_YZq2LRM_DRy6swMT3Jn_I-Ugld0W2DWQJDCpNVdxr0fi7JfH_ioO0iaRdjXcPxCEmLmNha1f1-hQZh4z9UKi6JWEwN8UiB3o6zwLVPxFlo6mdrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جام جهانی، ستارگان دنیای هالیوود را به استادیوم لس‌آنجلس کشاند
🔹
برد پیت و ادوارد نورتون پس از ۲۷ سال کنار هم نشستند و بازی آمریکا-ترکیه را دیدند، و دی‌کاپریو نیز در جای دیگری از استادیوم بازی را تماشا کرد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/663331" target="_blank">📅 08:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663330">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c3d38816.mp4?token=QD5I8rdKk2xpajuCw7ESH8x80EP9iLEg3kqkqV65WTr0GknAIfs24yhpsm-3zO_SSQnE9CiRdMyuYnS7C74O9Aqb9Ms7Xd9MPNJJCa2SKTPtWGS20nX5JgmJEtW5R6-zxTdJGFXJGcEk9n_MVWtlwlXYxqsJN6g7EyH5vxlAfpNQQ3YeJcuwqZvJPQSyvWQd-xh_Q5GkjA0Q2C2GobwLXPve6x_Yf7Lx3sVuixaUTLqbrcLdZRK9qlVan36vmgC9EABguJde75f7VUpeW5S67T2O-AwO9ZSCK2F56AbeJt6Bax3j_UcnCOSMkoOWhe7J1kOakBS1DpIavSQ2rKkPKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c3d38816.mp4?token=QD5I8rdKk2xpajuCw7ESH8x80EP9iLEg3kqkqV65WTr0GknAIfs24yhpsm-3zO_SSQnE9CiRdMyuYnS7C74O9Aqb9Ms7Xd9MPNJJCa2SKTPtWGS20nX5JgmJEtW5R6-zxTdJGFXJGcEk9n_MVWtlwlXYxqsJN6g7EyH5vxlAfpNQQ3YeJcuwqZvJPQSyvWQd-xh_Q5GkjA0Q2C2GobwLXPve6x_Yf7Lx3sVuixaUTLqbrcLdZRK9qlVan36vmgC9EABguJde75f7VUpeW5S67T2O-AwO9ZSCK2F56AbeJt6Bax3j_UcnCOSMkoOWhe7J1kOakBS1DpIavSQ2rKkPKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
این سگ رباتیک در سرمای کشنده هم متوقف نمی‌شود
شرکت چینی «دیپ رباتیکس» سگ رباتیک جدیدی معرفی کرده که در شرایط سخت عملکرد دارد:
🔹
حرکت در دمای منفی ۳۰ درجه، عبور از رودخانه یخ‌زده (عمق ۸۰ سانتی‌متر)، صعود از شیب ۴۵ درجه، عبور از سنگلاخ و فعالیت در ارتفاع بالای ۵۰۰۰ متر.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/663330" target="_blank">📅 08:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663329">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
پیامک‌ها با بیشترین میزان کلاهبرداری کدام‌اند؟
🔹
در میان پیامک‌ها با بیشترین میزان کلاهبرداری، آنچه بیشتر ممکن است وسوسه کننده باشد، آگهی‌های کاریابی است.
🔹
بیشترین آمار هک پیامک‌ها، پیامک عدلیران، سهام عدالت، سبد خانوار و کالابرگ، ثبت نام کارت سوخت، یارانه، بسته معیشتی دولت و سامانه ثنا، است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/663329" target="_blank">📅 08:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663328">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3708aa.mp4?token=PUhgFKurC23tNrI2V0lL7x3QuGBWoY7baaXVEgN0b7LANf2AG28WB-qWASmgIS5v_UwDBCZ092TYjYRrwMYAljrGjNW1JGDVeMLYspJA_tU0IJblg1XVtwhbWjSOI77EvtHIjrZQdPXDYXPDJLV20hm0llKEqpr9ehLuE_xWfLhJQu5mWqmQCRpGlECuv2Zqian7KwCDF90t_togSBV4Erm1rwWWRYJch7xk23vTfTGon8NZONSKs-iYReYyktFb9yMUWgoJpOFubbzpq7J4YaEb3AKVIQsiAE6uc7Jb80KUSbnbc1XBhb7V-SEGAWREVWeW8gWBy4cGrAFBR56hqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3708aa.mp4?token=PUhgFKurC23tNrI2V0lL7x3QuGBWoY7baaXVEgN0b7LANf2AG28WB-qWASmgIS5v_UwDBCZ092TYjYRrwMYAljrGjNW1JGDVeMLYspJA_tU0IJblg1XVtwhbWjSOI77EvtHIjrZQdPXDYXPDJLV20hm0llKEqpr9ehLuE_xWfLhJQu5mWqmQCRpGlECuv2Zqian7KwCDF90t_togSBV4Erm1rwWWRYJch7xk23vTfTGon8NZONSKs-iYReYyktFb9yMUWgoJpOFubbzpq7J4YaEb3AKVIQsiAE6uc7Jb80KUSbnbc1XBhb7V-SEGAWREVWeW8gWBy4cGrAFBR56hqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول آلمان به اکوادور توسط سانه
۲
⬛️
🇩🇪
1️⃣
🏆
0️⃣
🇬🇶
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/663328" target="_blank">📅 08:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663327">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a353cc23.mp4?token=U-v1KNVJpM_uUUsS4P_8yPaJ6tkfyvbZS87R4ebrQu7i10E-Jd8psQt10U94zaWe5sN6bCaFAG6F2UzhnuIkPNnnE5AvNLktJgVyS1cvsyvvmxSNXq4GFgJFZKgO0w9j6W79_BJA2sI8bb5gAAVOJxijFtQTzIM5Kp4wrlBY415fnmkb4Nvl6Lc0dN5MA5TLbs6-mqvORTalBZLQSlVytoV6s-JUAwozHNBMJRLmzofXVDROeMwAgRuh8cK1VUZgpw0-29S8-GYAaAWD2LQk3Ppo1RN7bzZPJlgVjy9yRHz2KZlCfpg_zwNMMs8RjStP_AXJVrOP3_55PI2jyk_zuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a353cc23.mp4?token=U-v1KNVJpM_uUUsS4P_8yPaJ6tkfyvbZS87R4ebrQu7i10E-Jd8psQt10U94zaWe5sN6bCaFAG6F2UzhnuIkPNnnE5AvNLktJgVyS1cvsyvvmxSNXq4GFgJFZKgO0w9j6W79_BJA2sI8bb5gAAVOJxijFtQTzIM5Kp4wrlBY415fnmkb4Nvl6Lc0dN5MA5TLbs6-mqvORTalBZLQSlVytoV6s-JUAwozHNBMJRLmzofXVDROeMwAgRuh8cK1VUZgpw0-29S8-GYAaAWD2LQk3Ppo1RN7bzZPJlgVjy9yRHz2KZlCfpg_zwNMMs8RjStP_AXJVrOP3_55PI2jyk_zuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر انرژی رژیم صهیونیستی، الی کوهن: موضوع خروج از منطقه امنیتی در لبنان در دستور کار نیست
🔹
حتی اگر ترامپ از ما بخواهد که عقب‌نشینی کنیم، به او می‌گوییم: «نه.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/663327" target="_blank">📅 08:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663326">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
نخست‌وزیر کانادا خواستار بازگشایی سفارت این کشور در تهران شد
🔹
قلعه‌نویی: شرایط بدنی بهتری نسبت به بازی با بلژیک داریم
🔹
مقام صهیونیست: درخواست ترامپ هم مانع حضور ما در جنوب لبنان نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/663326" target="_blank">📅 08:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663325">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc3ede5c1.mp4?token=Jd0nboIG_AhAPLbGe_n_TalWptuM3KMU2F8cw3H7hGbQB0TSIqXBj9lp8FljGNzOWptglYKG2rt2uyZIiD6j4Oz5S12XX7dWRKlgN3DTZKkNFXoEZqNFonLr0_iWWrOpvQ9-ez_K8-795G5vrhDxZFLzlaD99FkZy7PI-Ywk_KSdQQVjrgHfavhIDJLwCYjx0usP65Pjo7U4w1EuPUxzPENKtA8HXsPLh3tA1ac89QdU9miaU5ofZ6KRrUADhhX__1RMFC1MBOUJYUrcLeO62b0uZcaHzoIK075TLCWJblbgomCH9OajNxlHfon7OZkRRWNUGZZ-kvV8kLlNBY53yx-0IdXfmmK9lJ6wN-OFEaYpHXXU4fpv3YB1h-vhjiuS6fHmIpaKwLAf6NDUc6SIX2BavFT-OXBLujGeivtsmYFCNnk53bYzG5J-Jt8Zdrm0koXyRIyMNOHSe1kMNmIp3i3-weUzKXJJm80ar_3xevGOxLd2JBbbaM1WhmSicNWSB-Ab8Scqq3oOO2CwmKb1l2o5cXwyjbn_ANzhnMuxMDmgLvWIYw71l6KnuGaEBg-ObFvAX6NO9rqd0cUS8bbqR_QsEsBGHoRSh54BpSxxb2vLEP5gl9UZxu06Mj2kDUAgjVG49SkT_0weygwNvtj1VY8rJe2GewblWZljCfRuf5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc3ede5c1.mp4?token=Jd0nboIG_AhAPLbGe_n_TalWptuM3KMU2F8cw3H7hGbQB0TSIqXBj9lp8FljGNzOWptglYKG2rt2uyZIiD6j4Oz5S12XX7dWRKlgN3DTZKkNFXoEZqNFonLr0_iWWrOpvQ9-ez_K8-795G5vrhDxZFLzlaD99FkZy7PI-Ywk_KSdQQVjrgHfavhIDJLwCYjx0usP65Pjo7U4w1EuPUxzPENKtA8HXsPLh3tA1ac89QdU9miaU5ofZ6KRrUADhhX__1RMFC1MBOUJYUrcLeO62b0uZcaHzoIK075TLCWJblbgomCH9OajNxlHfon7OZkRRWNUGZZ-kvV8kLlNBY53yx-0IdXfmmK9lJ6wN-OFEaYpHXXU4fpv3YB1h-vhjiuS6fHmIpaKwLAf6NDUc6SIX2BavFT-OXBLujGeivtsmYFCNnk53bYzG5J-Jt8Zdrm0koXyRIyMNOHSe1kMNmIp3i3-weUzKXJJm80ar_3xevGOxLd2JBbbaM1WhmSicNWSB-Ab8Scqq3oOO2CwmKb1l2o5cXwyjbn_ANzhnMuxMDmgLvWIYw71l6KnuGaEBg-ObFvAX6NO9rqd0cUS8bbqR_QsEsBGHoRSh54BpSxxb2vLEP5gl9UZxu06Mj2kDUAgjVG49SkT_0weygwNvtj1VY8rJe2GewblWZljCfRuf5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
سخنان طوفانی میثم مطیعی در شب عاشورا در دفاع از سپاه پاسداران انقلاب اسلامی و خونخواهی رهبر شهید
#WillPayThePrice
#هزینه_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/663325" target="_blank">📅 08:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663324">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔹
ترامپِ قمارباز: ایران کشور زیبای دوست داشتنی و بازار جدید برای آمریکا است
رئیس‌جمهوری آمریکا به عنوان دشمنِ اصلی مردم ایران، از ایران به عنوان «بازار جدید» برای محصولات کشاورزی آمریکا نام برد:
🔹
ما یک بازار جدید خواهیم داشت و آن کشور دوست‌داشتنی ایران است. ایران جای زیبایی است. آیا کسی دوست دارد به آنجا برود؟
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/663324" target="_blank">📅 08:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663323">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a76c28e1f.mp4?token=h4redDS9GOQiEryQGBwzKrPDFbaFU-QPY0Ws25skmHG_dpD3690iqn6Yd_dn_6wKR2CCSPwAqXyBT6IlBaNDvRVcfySBKw1XEjOKx3u23liZvskGZzxEHbD4YNtRIRyIa5JXTioJx7oehyaR31QEU0vOA1RADFuagq4RlgGV26btbOZM_NrR_B0tTrhti75dHOQGEHpxvW-XuqN4DpftA32So7kVJ63h1Cm4AgD2Z67Ff7PkQmiKY8NN7emjvIEJGmSm6wxnHRNxMih27oR5AH5rF9WEPZoc_agJRXUn5t1FN0AMwY6CYCWUvRf_oyv8CyDLs71iGSXpkD5kd1oX_A8iuy_IHl351pv5tezGxCoIIhqL-GeL6Eq2tBMSOn4Bw8R_Owkmply-FDCDdNAq98415EhLjLzBZvmsLwedssZfAO2shOeIwa0bW8JHQofCJbPK1AIf1-JwO6as7BrkMS_GKRCdxzROmTtrrbjt5y_d3nBYGwxw8VB7HSk8Ly_aEje2TIhWU3cdZeMUJ7YoUr9O5bgcFS0XdA-iBnpMTnifjJG-oUkG8qM71ym56gJTSVhx3rSntlml_CTJhflVuz591dc19hR8UEa9j3440Jiai6jXkvMtj_ZLTgpeKHpkwfkg5sfxrbdOYj1b8oiekv-6raQixIZjx287qHSEo2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a76c28e1f.mp4?token=h4redDS9GOQiEryQGBwzKrPDFbaFU-QPY0Ws25skmHG_dpD3690iqn6Yd_dn_6wKR2CCSPwAqXyBT6IlBaNDvRVcfySBKw1XEjOKx3u23liZvskGZzxEHbD4YNtRIRyIa5JXTioJx7oehyaR31QEU0vOA1RADFuagq4RlgGV26btbOZM_NrR_B0tTrhti75dHOQGEHpxvW-XuqN4DpftA32So7kVJ63h1Cm4AgD2Z67Ff7PkQmiKY8NN7emjvIEJGmSm6wxnHRNxMih27oR5AH5rF9WEPZoc_agJRXUn5t1FN0AMwY6CYCWUvRf_oyv8CyDLs71iGSXpkD5kd1oX_A8iuy_IHl351pv5tezGxCoIIhqL-GeL6Eq2tBMSOn4Bw8R_Owkmply-FDCDdNAq98415EhLjLzBZvmsLwedssZfAO2shOeIwa0bW8JHQofCJbPK1AIf1-JwO6as7BrkMS_GKRCdxzROmTtrrbjt5y_d3nBYGwxw8VB7HSk8Ly_aEje2TIhWU3cdZeMUJ7YoUr9O5bgcFS0XdA-iBnpMTnifjJG-oUkG8qM71ym56gJTSVhx3rSntlml_CTJhflVuz591dc19hR8UEa9j3440Jiai6jXkvMtj_ZLTgpeKHpkwfkg5sfxrbdOYj1b8oiekv-6raQixIZjx287qHSEo2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اعتراف
ونس: ترامپ خواستار نابودی توان نظامی و هسته‌ای ایران است و ما از مسیر او عقب‌نشینی نمی‌کنیم
معاون ترامپ:
🔹
هدف اصلی، نابودی قدرت متعارف و هسته‌ای ایران است و برخی می‌خواهند این مسیر را تغییر دهند، اما ترامپ بر استفاده از اهرم‌های دیپلماتیک، اقتصادی و نظامی برای پیروزی بزرگ‌تر اصرار دارد. تاکنون پیشرفت داشته‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/663323" target="_blank">📅 08:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663322">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
واکنش پزشکیان به شعار «حی علی االاصول»
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/663322" target="_blank">📅 08:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663321">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO1SZqYBIMB9mvyYXbE-0Afgx_mdoTHnZpsgJU2_d3LWMokQD3xBeFkfgPWhAbWZSM3KRReuFtsrju2u6JWrX5lOsuIKueBoXxmcE7H91UwGORgBvssBkq5qIqYzH26Cs4DkCXKtqL1X7pypDnneMfR5bKbSkXh4DwjyqqxD6EB-T0Ks-KPY4UrIl8wHEl5tvl7LtejBes5VvNxccsI6JECTOLR4YTAzPXE7tq5vtde3Dqovh_2qdytuqHDTPDSaZSNFmdsEUNR3r6dGHqBWmdGZw5-gqpPVzHnijqM4gb5B2vZF--3bmw2XoGszswXO3452kRC8D4lZmJYpSKOi-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۵ تیر ماه
۱۱ محرم ۱۴۴۸
۲۶ ژوئن ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/663321" target="_blank">📅 08:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663320">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB-DLqyoxjSmhk4qUCx-KDCr86CleHspGnGlQITC4kqnVayka4w5vnkfM4pYf5Qd-5S35XDS9xgs9HhdGHCeiHKJ03zz8b0gFQDQRF6DAzKw3s7gfHIUI2-wUA6iE8Fs24noJGF_oVAhNUKaVLgJPmbCLnQHfJJGXskO-4bE19j80Pkst50c7j_XbK7Q4MgZ7QziUjymUbSeJNO8KDBhNJlKDQEwBcqavqvlpHIQGgE7R4ca8mjOig-Fgf4TvxKl6cd12EVju-cCbGeZ1Aq3AIOvOVnBzhRODq-xtgbwSgVs3sTdRjGHz47UyNeY_r543ACrcv8ZH0qHf5JMeRGTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بسیاری از کسب‌وکارها تصور می‌کنند مشکل از تبلیغات است.
🙂
✔️
برای همین مدام پلتفرم عوض می‌کنند،
✔️
بودجه را افزایش می‌دهند،
✔️
کمپین‌های جدید راه می‌اندازند.
❓
❓
اما سؤال اصلی اینجاست:
اگر تبلیغ شما به آدم اشتباه نمایش داده شود،
📌
بهترین تبلیغ دنیا چه ارزشی دارد؟
🗓
موفقیت تبلیغات از طراحی بنر شروع نمی‌شود.
🌐
از شناخت مخاطب شروع می‌شود.
📊
سن، نیاز، دغدغه، رفتار خرید و مسیر تصمیم‌گیری مشتری...
همه چیز از اینجا آغاز می‌شود.
🔽
🔼
شما برای کسب‌وکار خود پرسونای مشتری تعریف کرده‌اید؟
⬇️
⬇️
⬇️
مشاوره تخصصی تبلیغاتی</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/663320" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db555e92ee.mp4?token=phoO7irfU-3SDLwIaJYhlK-L64y0QaB_dhje9GuVzL1cGJJeuNqAC1X8tLXT9ZEgwYOeLLka9KNi4Y5JQSJoW-OeaYHweGl_MuR8PijdV2IS9VTwGh3dLGorF94c3TWhLKsjC7xQn8FumBZu_BcdpbXecqnYefgL2onoINPBTy-gp4hTnvep5dVo5NxXC6b_AQIzRNEi7OMaTV2PJywfQP2q5jfF-OMtLLOWx4HJWEKVBKTF7RgBol80aDtomtf0uRF2-RRQ8RUH9O4fxGEM-xIByCHkGx7pbcCgycgTtodVb77w11jmVKmZA2-3crxBPbWpnPOzqkElYtIubh0Wow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db555e92ee.mp4?token=phoO7irfU-3SDLwIaJYhlK-L64y0QaB_dhje9GuVzL1cGJJeuNqAC1X8tLXT9ZEgwYOeLLka9KNi4Y5JQSJoW-OeaYHweGl_MuR8PijdV2IS9VTwGh3dLGorF94c3TWhLKsjC7xQn8FumBZu_BcdpbXecqnYefgL2onoINPBTy-gp4hTnvep5dVo5NxXC6b_AQIzRNEi7OMaTV2PJywfQP2q5jfF-OMtLLOWx4HJWEKVBKTF7RgBol80aDtomtf0uRF2-RRQ8RUH9O4fxGEM-xIByCHkGx7pbcCgycgTtodVb77w11jmVKmZA2-3crxBPbWpnPOzqkElYtIubh0Wow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لپ‌تاپ استوک وارداتی
-
به قیمت دبی
- مناسب برای کار و تحصیل
- 10 روز ضمانت برگشت کالا
✔️
-  ارسال رایگان به سراسر کشور
🚛
📌
مشاهده محصولات</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/663319" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
هلاکت یک نظامی‌صهیونیست در جنوب لبنان
🔹
رسانه‌های صهیونیستی خبر دادند در پی درگیری در منطقه بیت یاحون در جنوب لبنان، یک نظامی‌اسرائیل کشته و تعدادی دیگر زخمی‌شدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/663318" target="_blank">📅 00:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yx4W7OlsvK-cRlJhWhtqYdUvjBWOukQTltSoOSB_pdExwOsA1ThGI-e-LWrLpcvSKfz95wQD7ottZVXXE_oZUznUMe1kws9jC86nfFmzy_KkY40gKZ_n61MHFN4nSSyi2HfVKrCmTZ5UWf2mkxYaCV41mjhqP2zUOMJXgCbVSImeB7tvEtxbwiBf5dD0hc2guGsl32OpjGWnXJesTW91sE9bMMExA8BFVI3VmcOZwdD9JpwQvWtk9bEPsBTfGzgou6WlFtcz7ntJA1wsOUdqiMy9te4b44cRpdfwzP1EVVjSoEN_YRGjf79Kk7VN_91wUU8e31EAtyiVMZBhw9d03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تاوانِ کارهایت را با عزیزانت خواهی پرداخت...
You will pay for your actions with those you love...
#WillPayThePrice
#هزینه_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/663317" target="_blank">📅 00:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2457382848.mp4?token=YxXd-LkriFKxSGSfVd8uL-zJ6JzN5R4kXkL4XdRnZXPsnyTjLZ8vyNkJKQv6z12J7CKex7AawLTwIvK66LWsZH7OvkDMPw06ys91Ji92bUuxLrT-9oEf-571ZAAprEaAtim72PtuoSowGkIMrd0iKmlH2eH2cjSQlaiUZJC1H4egSPD3afT294wcjAgmrws-K-tozItc4Qq5Hq3mKsxfSXYQ1RAABudYoKrW1V7qdpuD-c7cx5b-nTHXXukXeIg2Y0SLPNEwUvx4_8o2SqeQcIdDpNwPMSbHbwWSyeafIpp7n4Y4ML158t6o7xRSzdJ0tFtV22Vk3InqpFTfrBndBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2457382848.mp4?token=YxXd-LkriFKxSGSfVd8uL-zJ6JzN5R4kXkL4XdRnZXPsnyTjLZ8vyNkJKQv6z12J7CKex7AawLTwIvK66LWsZH7OvkDMPw06ys91Ji92bUuxLrT-9oEf-571ZAAprEaAtim72PtuoSowGkIMrd0iKmlH2eH2cjSQlaiUZJC1H4egSPD3afT294wcjAgmrws-K-tozItc4Qq5Hq3mKsxfSXYQ1RAABudYoKrW1V7qdpuD-c7cx5b-nTHXXukXeIg2Y0SLPNEwUvx4_8o2SqeQcIdDpNwPMSbHbwWSyeafIpp7n4Y4ML158t6o7xRSzdJ0tFtV22Vk3InqpFTfrBndBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
چرا دانکین دونات هرشب تمام دونات‌های فروش نرفته‌ رو سطل آشغال میندازه؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/663316" target="_blank">📅 00:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663315">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0062b337.mp4?token=uvryMF8VlFGrStaTg9SRXYRSadwSHqmep8_lhlKgc9uI_HT2Jdkz2uGh0TKOepHh8G_MZXPeO-Ljj5xhtIKOqKMNnyLsK-zVgIgoGCIS6-Ayivw6zLeLF36XOpC8LS530rkt2xpoZvQyUUPBoluMr_PEuXZmxScPkHK7tHWrgNRzzTDl4SaRQauPaVUOjWCa0xu_zUfebuXCGb9ttZQLVseRrPbFTE0XwJMu7w7YdJHgr2orH2hsQ01fhy0J3yOMjyAWRtMpNWP2npOZuTu4b8kvVZZnDpDbYINtiKevPbyJE6HUe0FpCUz19I6pd8LQzvTHgRXkKVrMptc2aoA7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0062b337.mp4?token=uvryMF8VlFGrStaTg9SRXYRSadwSHqmep8_lhlKgc9uI_HT2Jdkz2uGh0TKOepHh8G_MZXPeO-Ljj5xhtIKOqKMNnyLsK-zVgIgoGCIS6-Ayivw6zLeLF36XOpC8LS530rkt2xpoZvQyUUPBoluMr_PEuXZmxScPkHK7tHWrgNRzzTDl4SaRQauPaVUOjWCa0xu_zUfebuXCGb9ttZQLVseRrPbFTE0XwJMu7w7YdJHgr2orH2hsQ01fhy0J3yOMjyAWRtMpNWP2npOZuTu4b8kvVZZnDpDbYINtiKevPbyJE6HUe0FpCUz19I6pd8LQzvTHgRXkKVrMptc2aoA7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شهید حاجی‌زاده: قطعهٔ شهدای مدافع حرم صفای دیگری دارد؛ ان‌شاءالله خدا ما را به آن‌ها ملحق کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/663315" target="_blank">📅 00:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRQwyCG9KwOo5KZRG5L_sqd6-TLA7P5k9uSAqa1R5zv9B1_dgDcz7tUMvaqQGElbmp6Ik9uaVTR9qNAx_l4EXqciiEC9wxgpwYZYNZP0wMF086gyMyoEanLie6Ha6TvE-zcdZjUKgLoKo4S9_Xyi_a_Q4akS5GYiz2CuFEJsmr3FCRkQe7dGmSKGZf-HMwcQ10nmQeAf7PTiOsNRiU18r8Squ660KrlvQTgV9ZipKAoKZtaxGb4OI8L-cpGtHr2Yv6L5wVup_Jh5adMZX-Atlivntp0fwKrveaxx1gLVxDCSJULTNf2ig-ftRHrjyUjQo5S8bUgZr6vdxLP6Nov8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyErAp9ysG2CuFCFyv4hLIXl1zbkvnq6sIDuhy_QKO7dp92zrZmQCaFV0Ap1Uc4kpWzfEvB2NJZzbZY3Vuy1BEqkU3E1CVuncuUp30l_RC4VqZkN0l3E2WJTEFFNo7nv7zDHmU--9Vif9OAmREgA7xkDZhVPTdBO_yGq9GZwJAP_FfNDO10GE57fp_sRVN4mJdliaQHSTnff1CQfkHR5fNmEuHVimtny038-qf6B15oE9IFBc0BhcAWhXZg5HLJzFH9u1mSR2LTp_S1M2xUCFsf0o5sTCMZIjjM2jPXxNUAB3HP5zkTYamPFp7P1qo5blOz1bAbldhQ2BmUNWlAUnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
حضور محمدجواد ظریف وزیر امورخارجه پیشین در مراسم عزاداری شام غریبان حسینی(ع) در منزل سید صادق خرازی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/663313" target="_blank">📅 00:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663311">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMP3ApDFS7Am2Ud6f79TpelUvst4UYpMIxW-p5ks74ExHJ6Kux6fgJl69ruB8ZZ35SHzbDiHlPz235gL-QE3DrsLIeG1EBwL1hHGe9qb8TTA4txWbk0onTL3VG9tEh-h8-0ek39Drec_9RbzwOOVOmQEu9Sl3ne_T5O83PtCv-AwZbmhhM2x1qq-t8PR3R9DSqPCmH4Y7GfwcgyEwYy1OuXVIrKrfRAbZX7HcYRxXnCRNUPqDlZoJoJq8sPh6NzvKjHGex2-GdlnwOytqDGa4YrXCYmz55iXmBkZep3hmUohe_ap716h-XKN8SDCauZf9T4ADhf9Iwap5Pgt8xHXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
رهبر شهیدم شاهد باش هر شب بجای شما فریاد زدیم: مثلی لا یبایع مثل یزید...
#خونخواهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/663311" target="_blank">📅 00:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663310">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4wh0hy0TBKt8Odl2Dj_gmjqPl5SmkepUKC5Z9_sUKVMXjOz1K5bHmgHRcC58F0a3RwKzrSIlhxE5VLmRpvG0ptQvQO_AJ-pnK1SJJEO_4URPW52pYz_X36P_COlMfU9xzjYoAH8E2lCsz6ORCkdxcsnBDw4PK3rp5Y2o3yJcdldVKaI5c3ncwe_oJgQJjiqM0GRfNkScax55CeHntSOOMco19cjti8P0Ro_BX3mDSy5sDwnqjN5XEllaMhTubf2g9OB2vvE4znohyGivgUi88JUMW1bsyLmZeSFC3_qtTtfW_WIW63xRxZrt5N_taKAwyvns_hWGbna8koFmgjLIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/663310" target="_blank">📅 00:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663309">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b38bf7fe.mp4?token=k7LoM1yWnysw-uHGpEMvtTGbjJqNho7QVL2-nFDgR37gCSbc9bbOU4mhxM3jzrJrUg_gq0vC6Dld4tssSXWqol8ncecUp44he9j5VEzGlX6lgzK77tj-dOue8zqiRS0tgwL45WoCU93DMCXamGp-9bH6x1GKAZp-VKpRu9pKDy5hLq2bnzp_jlBbuISk-FGgzRLV5PPwX3xO1K30bt3-0TjWxi3-U_AzQQtYD1UKb-jfwfsi20h133ScrrBZ0f8NNHeCacMWUMhJUVzraVR43GeCDbcNV0dzfNkS2XaLHuKh1oxfgHigtwLFW38GkkpJddrNE4Z0p3VmPcgZUOz2kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b38bf7fe.mp4?token=k7LoM1yWnysw-uHGpEMvtTGbjJqNho7QVL2-nFDgR37gCSbc9bbOU4mhxM3jzrJrUg_gq0vC6Dld4tssSXWqol8ncecUp44he9j5VEzGlX6lgzK77tj-dOue8zqiRS0tgwL45WoCU93DMCXamGp-9bH6x1GKAZp-VKpRu9pKDy5hLq2bnzp_jlBbuISk-FGgzRLV5PPwX3xO1K30bt3-0TjWxi3-U_AzQQtYD1UKb-jfwfsi20h133ScrrBZ0f8NNHeCacMWUMhJUVzraVR43GeCDbcNV0dzfNkS2XaLHuKh1oxfgHigtwLFW38GkkpJddrNE4Z0p3VmPcgZUOz2kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شوک بزرگ برای جامعه اطلاعاتی آمریکا!
🔹
خلبان جنگنده F-۱۵ ساقط شده در ایران برای اولین‌بار فاش کرد پهپادهای ایرانی با چینشی چون «عروس دریایی» و «سفینه فضایی» حرکت می‌کردند!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/663309" target="_blank">📅 00:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663306">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_-J_YhV7ok4Gs4n1u_SxwRIQw6JnzkktPlqOouZXKypv0UMeFu4GnmcR2IVKRNc5a7HMmfCW_uBEEqWNoXILxpOa1BCGe08R7ofJvqDdVu0rH0Nk3hXyhtw-OkBkCNgxde3v4KWu3Bt9zCla740hN7Hd4u61MpR1NT1y3CAqvOJAx0GWPaE5tAcgY1zKQNpcG46UwXlgqFrYiJkFs5kw3gPE7ne1g8nf5oJVdm80dCywzaG44Hr2xrT5YtUiBHkBn20j0CRQIrEbdEJHPTvEbeslSFA5o2RYtVXhId2LYzc-waCyKCQRzml02r2DaHQagNPk9YGFh6B9WGAX9nEpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WhW8YII5zeq1xgTL6_bbHVOagr99ZOg5iVOJJxQ7tceYj1noDHru9XU4L9jAoMH4tXNIyevcIFTgQJfok-gXlwb7fCe5a-C-D5Y6OIx72zRjgOoHM1SVi17Kf036nFaZ7x97j4ZLiuyAnU6OBILsXBJfcddbljHBSci39oCFo7iu_-VpQZDMY69Ev0tg5EXyGULjrKnpIV6xO4B-PfMQED6CePU18mbnSVD0VfTd2nrAzNsLGN4ZfKUQIAXB2xJMRR7MVu29-kyPVOLNUUbH_comwb83pIRM95x69VoX6ehGCvCetkNuPWoidt7s9DzX557BRRr8oUuuW0WBLKVvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwk4Kxeh6x48REK58CBuf2VqYNDvX11B78eXaWigHGbfMGYZs7An4AEhH0O5I-NoAwWSeKhlGgvjc3sHnOk9wQRoJS139055RusxRIvf1XSjES_gaQEF-XsF70MLN3fQ5RcAEm_g5qLtbQ47qckbsZ5Tr3_ExUbf-wnxZnXub_4D3IoMSCJJUsm7FrjBksOfsHWUfJ3JX-5Tmc3_LVyNTx9sb2v5sCJB0VW5-SxIcYRjPWVyq-GBcxtt4N8E7xivg-Y8RJk7H_qQNsUncwcK8D58f-tF12nq2mBnfMqu1N_SAvee_rt0OV34qUVlmx_uyUSKOm9gJEWn3UWqPhbLVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصاویری از خرابی‌های ناشی از زمین لرزه پرقدرت دیشب در ونزوئلا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/663306" target="_blank">📅 23:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
پاسخ قالیباف به ادعای خرید گندم و یونجه از آمریکا
👇
khabarfoori.com/fa/tiny/news-3225621
🔹
ادعاها درباره حمله ایران به یک کشتی در تنگه هرمز
👇
khabarfoori.com/fa/tiny/news-3225665
🔹
مرگ ۳ تبعه خارجی در ساحل نوشهر/ یک نفر ناپدید شد
👇
khabarfoori.com/fa/tiny/news-3225565
🔹
ماجرای جادوگر غنایی که بازیکنان را طلسم می‌کند/ جادوی سیاه چیست و چگونه کار می کند؟
👇
khabarfoori.com/fa/tiny/news-3225623
🔹
بازیگر زن مشهور جان یک مرد را از مرگ نجات داد
👇
khabarfoori.com/fa/tiny/news-3225534
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/663305" target="_blank">📅 23:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663301">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔹
حمله توپخانه‌ای اسرائیل به جنوب لبنان
🔹
شبکه المنار گزارش داد که توپخانه ارتش رژیم صهیونیستی مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/663301" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663300">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔹
پرواز مستقیم تهران-دبی از ۱۰ تیر ماه برقرار می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/663300" target="_blank">📅 23:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663299">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔹
حمله توپخانه‌ای اسرائیل به جنوب لبنان
🔹
شبکه المنار گزارش داد که توپخانه ارتش رژیم صهیونیستی مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/663299" target="_blank">📅 23:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663298">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc8fba96b.mp4?token=GJ_-3zDwAliIZLFRtLiVsXlASBouqTQFjG4i5phMwIZ8npCs2l77KYfGBjHL38VY-Tt6vm6T1CBmjoRN7KpNyl8wk2LLcFZVgl2vXCfnBzZgJol5mxowKa_iXHNgkGXrdbzVZ4idjNtjuGopYE3mZYDKsczv5bac0kG-qu3sb04cuNkPSScy4W-XN3Q8TzY5hvEnmVG3mcA3YG-dzCrHzXhsCk1KLVEq6Bp19IrItwv7Tz7RM1y7cs8_MljZR4MIodHaRv1o5DFF1mKGI9Sp6nsgtFP4UwBPup1c_YPHmYknHpL1eg-7sn04SszRx5H41gwoGPqQ1nlITAXaPnf5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc8fba96b.mp4?token=GJ_-3zDwAliIZLFRtLiVsXlASBouqTQFjG4i5phMwIZ8npCs2l77KYfGBjHL38VY-Tt6vm6T1CBmjoRN7KpNyl8wk2LLcFZVgl2vXCfnBzZgJol5mxowKa_iXHNgkGXrdbzVZ4idjNtjuGopYE3mZYDKsczv5bac0kG-qu3sb04cuNkPSScy4W-XN3Q8TzY5hvEnmVG3mcA3YG-dzCrHzXhsCk1KLVEq6Bp19IrItwv7Tz7RM1y7cs8_MljZR4MIodHaRv1o5DFF1mKGI9Sp6nsgtFP4UwBPup1c_YPHmYknHpL1eg-7sn04SszRx5H41gwoGPqQ1nlITAXaPnf5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویری از برگزاری مراسم عجیب تعزیه‌خوانی در تهران که در فضای مجازی پربازدید شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/663298" target="_blank">📅 23:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663297">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109eae93b5.mp4?token=IeSLBeOx7Z6EpvhBgFm9Lb12MJfG4b1raLojfuubMkLNHYrNwtaIbvQpsChzbwrHF1fREXZFyQ-Asf_WTOVSS5dAJcn_K8cA_2fpP3LJ6qrfZmP2DRyaf2uOZef8IHxgspFtkEHoR0AMxPiqN-6lEBjPf-RHGvBWOihCTI6yULdBaYxcaSmkjkbwAeo8KsLbZizC3M5ty4gYnbRAkyMqJGJa-9Yg1LZRI43j-C3jHUm4sNUT0ffDawKvf_6vy5rylo3Lk2-Ww8xwHNWa6_STyFJVrECc8oIKMOzC2vZR7w2WQF1F8qs-wN4X3RHuq8vKyQ-fuRbliFMOT14uoriAaQl1f-3u2tJpGcdhKT5I6hf21CcaQsPE3x5DRqt6S5lMxi-abs6N2Ah7oGYBYz-c2xztpa6S211J_lNsisN_jgdK0RUIV0U6LHWGsvZgxP6ED9LrE4XNZljDdfSfJ-b0jrWp43qZM4QX5Unb1XindP9ge0RdBR0NKzJTY8UZ4NNQVx8t3Y2VEAGDfQpU3wmVZo3azaQe8NmRqAfuBoAd-sQvt7HztHLBYfqpAXWaosH7uCHmHraCiuc0E1e2Y6SG9bXGJroYpJ-mJ4HKIs4z5xrQ5So7o5OtdxaSoqnJRJQklZ-gO0p6BdM4YS5R79lqWMOd6rJsQB4k4HV6GAv3KBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109eae93b5.mp4?token=IeSLBeOx7Z6EpvhBgFm9Lb12MJfG4b1raLojfuubMkLNHYrNwtaIbvQpsChzbwrHF1fREXZFyQ-Asf_WTOVSS5dAJcn_K8cA_2fpP3LJ6qrfZmP2DRyaf2uOZef8IHxgspFtkEHoR0AMxPiqN-6lEBjPf-RHGvBWOihCTI6yULdBaYxcaSmkjkbwAeo8KsLbZizC3M5ty4gYnbRAkyMqJGJa-9Yg1LZRI43j-C3jHUm4sNUT0ffDawKvf_6vy5rylo3Lk2-Ww8xwHNWa6_STyFJVrECc8oIKMOzC2vZR7w2WQF1F8qs-wN4X3RHuq8vKyQ-fuRbliFMOT14uoriAaQl1f-3u2tJpGcdhKT5I6hf21CcaQsPE3x5DRqt6S5lMxi-abs6N2Ah7oGYBYz-c2xztpa6S211J_lNsisN_jgdK0RUIV0U6LHWGsvZgxP6ED9LrE4XNZljDdfSfJ-b0jrWp43qZM4QX5Unb1XindP9ge0RdBR0NKzJTY8UZ4NNQVx8t3Y2VEAGDfQpU3wmVZo3azaQe8NmRqAfuBoAd-sQvt7HztHLBYfqpAXWaosH7uCHmHraCiuc0E1e2Y6SG9bXGJroYpJ-mJ4HKIs4z5xrQ5So7o5OtdxaSoqnJRJQklZ-gO0p6BdM4YS5R79lqWMOd6rJsQB4k4HV6GAv3KBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شهیدان حاضراند!
🔹
حضور و غیاب شهدای ناو دنا و جماران در شب عاشورای حسینیه معلی شبکه سه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/663297" target="_blank">📅 23:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663296">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b09e48496.mp4?token=O5UiKfhht3yT84Cv09GTLaWOnNCNZ8O4hlF4zxXeN-pBmYeiGVp8BkldYIhfoz2swHmB_yUJAI22rw5O3b4nPyxTpvVB3aBul_AshLyrqoAsbCB94403O3phEnknJCRILtJo96tqcFSpXVyQsnWxQSo_zzud2x3e1ZzNdCBeRZE4sNSL-o10fMnILRPwBOHOO0il7A0B685nFTW8X4TvlaxY0RkR8SG6IoDJBuOQxvAPd0xTu-llfGdJ6vnIX7A52IP_xQdxpwCnXbvOY59lIBtaLmgR4yc93CwFIM0Tg7HW6HQhW4tlyGTIjL4cyRx8Esil6Jkj2GYqsCps6V2v9oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b09e48496.mp4?token=O5UiKfhht3yT84Cv09GTLaWOnNCNZ8O4hlF4zxXeN-pBmYeiGVp8BkldYIhfoz2swHmB_yUJAI22rw5O3b4nPyxTpvVB3aBul_AshLyrqoAsbCB94403O3phEnknJCRILtJo96tqcFSpXVyQsnWxQSo_zzud2x3e1ZzNdCBeRZE4sNSL-o10fMnILRPwBOHOO0il7A0B685nFTW8X4TvlaxY0RkR8SG6IoDJBuOQxvAPd0xTu-llfGdJ6vnIX7A52IP_xQdxpwCnXbvOY59lIBtaLmgR4yc93CwFIM0Tg7HW6HQhW4tlyGTIjL4cyRx8Esil6Jkj2GYqsCps6V2v9oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
یکی از بازماندگان ناو دنا:
فرزند یکی از شهدای ناو مرداد ماه به دنیا خواهد آمد؛ دختری که هرگز ندیدتش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/663296" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663295">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b845c7b0d8.mp4?token=JGMvq7aZXCoXHnwqkhK1l3mpFkkSPe1vhVmtqcpxeB6VaActI-TVytBWH6MNLHCIZG0TIIpMm9u7eMIk7HqdowHYUoPZ8fLGQ3ZEIzgO39YscjDk5Q3vGUv9hh4sbVcJHKFeW0bpaTjmNz561LaDGuPyfAV1iWJJorbGMc2ujHpLXWM3uM2xk0Z4z_Mggs1_XAp8vohsi1sjSV2OttunheHdFHgeaG1g-7Gk6MQoftwPkwfkK6bMUYKrQ53M4CGZYziZBI6i4J1hRqDoVT4wgqB9o9wSel2vxyL_gdyWcDEin1iDcfgAH64qAQ-L2LeXPV8-YdafxTeYRDrtg8y8lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b845c7b0d8.mp4?token=JGMvq7aZXCoXHnwqkhK1l3mpFkkSPe1vhVmtqcpxeB6VaActI-TVytBWH6MNLHCIZG0TIIpMm9u7eMIk7HqdowHYUoPZ8fLGQ3ZEIzgO39YscjDk5Q3vGUv9hh4sbVcJHKFeW0bpaTjmNz561LaDGuPyfAV1iWJJorbGMc2ujHpLXWM3uM2xk0Z4z_Mggs1_XAp8vohsi1sjSV2OttunheHdFHgeaG1g-7Gk6MQoftwPkwfkK6bMUYKrQ53M4CGZYziZBI6i4J1hRqDoVT4wgqB9o9wSel2vxyL_gdyWcDEin1iDcfgAH64qAQ-L2LeXPV8-YdafxTeYRDrtg8y8lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بیست و یک سال پیش مارادونا از پله درخواست کرد تا چند ضربه سر با هم بزنند و این لحظه تاریخی به ثبت رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/663295" target="_blank">📅 23:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663294">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGvWmfXgHFAsgTAMbogUyZEyoEsSAyDNwtUwzpSyyitOdyT5vAPT-v59imV3iqMX42EtoPoIadnHwigMkmNnez68l22b5Vf2VlcNyBmQ7PKFvR3AqwqC6dMhVwxvUkoGxPmjzbi7Ht9ZeCcjIrC7VGUHWWwP7G0UWc5thchgVP6mp1CBkyxVyc7Le5u8NeASV4f997Ssf-fqGoAFzQynWcvJmvRInTfZ9MJDEot6nveH1r0PWvX0ZiGdLFR4GNYeNvEm8MyAsifwCkvHMHMFBl-ae3dHaFqtj4-qjITXK2UG-aaB986YMrEDrE4AAoz65UyAZskPnJk4GRRGJ2rv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
روستای حسین آباد در املش گیلان
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/663294" target="_blank">📅 23:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663293">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHzGVgLVZ9O7S2YZc4cJ7cMQPPVyWWSEBhuuRS4KGT4yRPn25e3c72yiAuw7v6BTNoQ_pxObPOMx3VPTRKvSmHsBzApLzLnxmUcsXFm2z_BhrTXYlvYhzmPMXjf8QZ7aXV030JaZF25Rt4XwZZLv95_gntunKHUQ49jMyGuVtQp6xrJJYPaNsc42Klko0RghXUUCxTQtZtnt2NePmxBNF54m5SAsOhJ9nwN_VeB2NGuS7BWwUUx33P64rfvJXJWpqAae0WWGwVy-L1UOhHPFtWKn2JIQ8fbeOPi9SeNi1Aafaj3qIZKFyxYQHdy7xU5CGUMh4Jt6OBI3w8lIkg9-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
رده‌بندی جدید خلاق‌ترین بازیکنان جام جهانی ۲۰۲۶؛ رامین رضاییان در رده هشتم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/663293" target="_blank">📅 23:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663292">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usdpCGQfiZDNa-zVTQFZb4Dtrf_RMuM87kog1UXjAJ9ZGJ6OfQB-fyJh3pWBlIau4OWx3uH8FDKA5k1RYfftx3c5mI3oON79nGLq7ay0FCttWCiyct4Tia29QVXq7NfLACpw-rN8immuR31rihC2b2Kkgfv2fJy-0tMgo_h7nBMQmoRVFFDNLRJzj66Noc58nQXCJsfdONjqzddx1h72jhJByDAvJKeNvo64LBrrax_GjfYGF6hEAzQT_tMYOy79kXzoIBrGrTGRl96Z7OzkcNQu9xEYpV8svFuXBxSgf2Efk4-HUfxJGIeQZz5m5rwdZ82oYG6J3kUo9hzLZ_V_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«میانجی مرموز قطری» در مذاکرات ایران - آمریکا کیست؟/ ۴ سفر به تهران در ۱۰ روز
🔹
رسانه‌های غربی "علی ذوادی" را چهره پشت پرده قطری‌ها در میانجیگری میان ایران و آمریکا توصیف می‌کنند. اما او کیست؟
درباره وی بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3225646</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/663292" target="_blank">📅 23:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663291">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6bc653804.mp4?token=I2b17-38Qw3bNmqi8svZYsTyIHfC6G44eQnm4eYlelt9KpIyBJZCpQA3OlUpXMhbxKD2QeEMQ-c35FsHyowBo-94nlGcW_mgZRm99-gXw1jzpBo-9HP5St7wUkT4hbMkjaLcGOVSZwEYsiNzhxLzp9qXoN7wfEuk_M2M0O9KkVdKJV3i8p3YR-6Jp1oeiZzs1fMSVTFIzYTZmjri2IJRckTOz3z4Df2n6DhncGMkAAngXDshbhqQHrA_GhBRZeJpNjyFHKF2tYsSJDzdwWTXtvhhjWjxhVtsGBQ5kxgnuC80G6hwWAwkMpQbNTAwXVF97h-ukSDV3-___uSKAWiWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6bc653804.mp4?token=I2b17-38Qw3bNmqi8svZYsTyIHfC6G44eQnm4eYlelt9KpIyBJZCpQA3OlUpXMhbxKD2QeEMQ-c35FsHyowBo-94nlGcW_mgZRm99-gXw1jzpBo-9HP5St7wUkT4hbMkjaLcGOVSZwEYsiNzhxLzp9qXoN7wfEuk_M2M0O9KkVdKJV3i8p3YR-6Jp1oeiZzs1fMSVTFIzYTZmjri2IJRckTOz3z4Df2n6DhncGMkAAngXDshbhqQHrA_GhBRZeJpNjyFHKF2tYsSJDzdwWTXtvhhjWjxhVtsGBQ5kxgnuC80G6hwWAwkMpQbNTAwXVF97h-ukSDV3-___uSKAWiWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت‌های پر بازدید وحید اشتری از فعالین عدالت‌خواه در خصوص توافق اخیر ایران و آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/663291" target="_blank">📅 23:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663290">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ8ITfykQTON1amMdII5S7f2RmeBouve_B0PUHdWcrR2QbFnrxyTRarDCz9fn86amPh7aXGSZ1LzmA1PbB52wGpH1lRwGacGUmM5cw0i313ThjIMrVibhSBcor6PdubTe0n4qOac8gx3k2EBZs0K90DBefMjdBGWM_-jUOb5aD3UZZp0jjIYtOPM_j4FmMVNdXbTiVT91jFBZ26gA-6PaO1LYoTaLrw_Z_WUd6J7t_2gCjQWsThu8ZYTCOedWJgAxrcGDLYngGvdXxavKs2bY9e75YoWvAxpU-niYUBcFxFnYHO2HVBN6UsJdo4hkIqLd5JMojFlFzwzLpXrlOwJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حضور ذوالقدر دبیر شورای‌عالی امنیت ملی و سردار قاآنی در مراسم عزاداری امشب در جوار محل شهادت رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/663290" target="_blank">📅 23:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663289">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pE62BlQ2KSP_vzNWCrPf0LOzf-fbTQvzM4BlbausboddoG8kRPmVTZByyS3UXXOA5FTpZW4Fm-mlt7bXhhAvcxevim2kTBlLgk-lBp8ha6OkSczMipzC0yIN-amo1VlOR2ZdR9SipGL4qXTSnO9LQl8YEqcdEpt1fnOxCfaCGosqJbz5pq8Rs8x550NkdckdqTB3y_417LkItDYy1-j4KhqZ02SrxZLNny7P4WGBxk8aYWc5WIoZNG9SBClfpbXSDAZLA9IqDgXy70il8Px_aIh-Ts5XK0GpxW4g1rRDGn6VjiLgkNMaAHLClI1J98Bi_lfuE7RG4UvFN-EKXtaJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطر زمین‌گیر شدن تأمین اجتماعی با کسری ماهانه ۶۰ همتی
🔹
گزارش ایسنا از یکی از چالش‌های کمتر دیده‌شده تأمین اجتماعی پرده برداشته است؛ جایی که درآمدهای ماهانه این سازمان با هزینه‌های اجتناب‌ناپذیر آن فاصله‌ای حدود ۶۰ هزار میلیارد تومان دارد.
🔹
در شرایطی که تأمین اجتماعی مسئول پرداخت مستمری میلیون‌ها بازنشسته و ارائه خدمات درمانی به ده‌ها میلیون نفر است، کارشناسان معتقدند تسویه بدهی‌های دولت، تقویت درآمدهای پایدار و پرهیز از تحمیل هزینه‌های جدید، بیش از هر زمان دیگری برای حفظ پایداری این صندوق ضروری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/663289" target="_blank">📅 23:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663288">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6kfZzlxSlElXdvf1HqQ6yZ0U9WM1SPUHoBZv2upCcATVgcPIEjln07YCxaQMuY-iW1a4WCMevCLhxhPkM1qy_alzYIov8OskFfkzy4E7kBWzKt4_vCgIsIqQwjZKuy0gUsotb8_7QmEuHXRY11yY7h0AeoGz6zjYBRFeqhSbS83_6FNIP0e40HMECSmOOsGrDSRKQPZzSsGieu96PonoYq6jhvkMYrGiQ2WkBKHjSl0yQUb1rPypi1VyAcgGyr4NfE88XOGFiwHtr3fu_WmaLy7-cu4Imp57EyOAmY6qvgwMnOPrrzHUkk7dRoETfFhH1_46___1j0MJXOs_70Cng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری مهدی طارمی از سیاتل آمریکا به یاد عاشورای حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/663288" target="_blank">📅 23:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663286">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTrOk8APJ-j4iSgQ1A6LU3DNyk_K1OyTUDPzL80UA4UMaYJe-4CRVkxXN5CnO6CqpahE6BmU_FqGO9YHlMRGDtbu5878wqWgejDw5deZ_xGS9sfltVMJbVSKZ8nkTs4DpaiTC_fqKLNskVOEMEbfErYnHw_qGcj8GD6baAz-bKmhwcztBE_ObuLkxIv2ag2J6WwcpF74v3qTSXnOwO_f2eS5Xcx7p8Yo3DAu8HCBrWBLDJwgMPUzUxXy7737ERQY35Q9oaPLCMJv8MpzeAM5Jc7U8GnBbaLFba1p6odlH9qeGLUplF19u3JGbHviZ3PmpZhlaN6oQL6acy5PGNWFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
شاهکار تلسکوپ اقلیدس؛ دقیق‌ترین تصویر تاریخ از مرکز کهکشان راه شیری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/663286" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663285">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrIZepILFykH7fX9YFkCVYCefD56awyxZgyz9WRFYB-dfwoyp6V2lrVBlVrY3XMdKyjuOmk3uWzxYX_UwCCMrp0b-0M6Gpc1gbOn2UsK12_p84Yo6PuGHTaOVN3U1jiiJ0Dy0ocLR086hVAWiMrBfuIbxhaFkgTOsU9GonKYrjieRFjH8EwhS7bn8ThKNmehEReU1ZjxNKRU_SLwAEqi9gAQKrSsp5UtIB3B172cSLF3Ax02CzgpbY-bJIGW70eHESuSnDcT9hK7wJ4pTLqDCKBeb_OwOhAZvt6hPAUEExFLjukzOf2e6vJCI5DulhwFv6dOe1F67jpEutPFpjrzpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بعد از انتشار خبر حمله به یک نفت‌کش قیمت نفت برنت دوباره افزایش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/663285" target="_blank">📅 23:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663284">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
ادعای رژیم صهیونیستی: ۶
عضو حزب‌الله را در جنوب لبنان هدف قرار دادیم و به شهادت رساندیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/663284" target="_blank">📅 22:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663283">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔹
تیراندازی کور تروریستی در سراوان ناکام ماند
🔹
ساعتی قبل تیراندازی کور تروریستی در نزدیکی مسجد جامع شهر سراوان رخ داد که در پی آن تروریست‌ها سراسیمه از محل گریختند. این اقدام هیچگونه تلفاتی در پی نداشت و خوشبختانه شهروندی در پی آن آسیب ندید.
🔹
هم اکنون آرامش در شهر برقرار شده و مردم عزادار در حال برگزاری مراسم شام غریبان شهدای کربلا هستند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/663283" target="_blank">📅 22:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663282">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef52fa42c7.mp4?token=T3p3RUQApkiYH2KE0ukMl6_4RF_7LtkbI_zk2bVVhOjivnc7VBWjOY7RnBIOcFscW5YObkDtzndr3D_Kq8VE9paz93iehm_qZHn4x1WzwjREJt1U5i41AFOAkHwDAFWo3GVGJrvMlkiYgM0odYJr_5IpTIoiA70KdYjvr5Fc_u8rrlnUHKc3HrSKXZotxMn3Fxy0gkSdNXDbX9M0oyGEghntd0qs6BaNKM0Z5VkXe3iKFllU_rr5ElYnjnZk5blhUgC5EYAlsZIPVbEZAxe_atA8HgKtCIu40t08yAOYvpyDJGWI--Fbjysjy6CB0fnlsh_TqOuv88STggniwuYDbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef52fa42c7.mp4?token=T3p3RUQApkiYH2KE0ukMl6_4RF_7LtkbI_zk2bVVhOjivnc7VBWjOY7RnBIOcFscW5YObkDtzndr3D_Kq8VE9paz93iehm_qZHn4x1WzwjREJt1U5i41AFOAkHwDAFWo3GVGJrvMlkiYgM0odYJr_5IpTIoiA70KdYjvr5Fc_u8rrlnUHKc3HrSKXZotxMn3Fxy0gkSdNXDbX9M0oyGEghntd0qs6BaNKM0Z5VkXe3iKFllU_rr5ElYnjnZk5blhUgC5EYAlsZIPVbEZAxe_atA8HgKtCIu40t08yAOYvpyDJGWI--Fbjysjy6CB0fnlsh_TqOuv88STggniwuYDbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
نان قندی و روضه‌ اول وقت؛ اینجا پیرترین حسینیه تهران است
🔹
در کوچه‌پس‌کوچه‌های تهرانِ قدیم، خانه‌ای هست که حدود دو قرن است صدای «یا حسین» از آن قطع نشده./ اخبار تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/663282" target="_blank">📅 22:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663281">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba374eaa7.mp4?token=JrdAFBeo6OSnCfhMm2SKOHgszQptioWHaF7eUjlW0CR3ZRFj-bwBoJ4Hk5iHe_TwRP9foScgB49Y8XIIpq3VHU52KdZXsANInVn_VaUWav-0evS5PWFeY9ijFuLgnZOuCGLZdpmBqu_B4dQAOeU6OS4rUBExLbMvEDsHXJcaUgsFbHa_W8d0RPxGc4Bip0M50p1UFxKXo6ps3oxJkDNy0CJmjx6ZOgaunkxGDR1EzjCBAWnwVyyqIU2QRGiO4o5KNyL4GqIDtvl-DWi6Ow70zi_sgPA72cl-Z_wBjISJ5ZWD3oXnZ_IzZJETIuQ0M4aUkh1ORmgZsbbd6NMOC_1FKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba374eaa7.mp4?token=JrdAFBeo6OSnCfhMm2SKOHgszQptioWHaF7eUjlW0CR3ZRFj-bwBoJ4Hk5iHe_TwRP9foScgB49Y8XIIpq3VHU52KdZXsANInVn_VaUWav-0evS5PWFeY9ijFuLgnZOuCGLZdpmBqu_B4dQAOeU6OS4rUBExLbMvEDsHXJcaUgsFbHa_W8d0RPxGc4Bip0M50p1UFxKXo6ps3oxJkDNy0CJmjx6ZOgaunkxGDR1EzjCBAWnwVyyqIU2QRGiO4o5KNyL4GqIDtvl-DWi6Ow70zi_sgPA72cl-Z_wBjISJ5ZWD3oXnZ_IzZJETIuQ0M4aUkh1ORmgZsbbd6NMOC_1FKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون: مردم دقیقاً برای جلوگیری از جنگ با ایران به ترامپ رأی دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/663281" target="_blank">📅 22:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663280">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEPzuwlO7E_fiaAKm8n-w1LMKnvmGIfWwEwAVyBnUS3qEsm6H25csH4S-IcbTSWaf2wgk9mg2YaR4IXJgjWSMipVa-Qr_RnE8KdoITkAglvvCYWSuBhQVfN-U0OnLocSBMH55ho6wET3hzvtxTDssCouKhLtj3UjZljEJKDy1kjlhHfD-oNAbcpA5hxMyYdzagc_ZMaQtvBc-9OecLs3Obhc6zQ7QQH-eVtIZAQc0-J2dVS2HI3iH6FifW9moF6VLtKwnriJnK_F4qY-wl-d5TXfRPi3n2Loaw4xbeiZ0mBzv0m8dwRos-HxldM2rBFM0EE2JGSxpHPs4RBp0eQItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نظرسنجی شبکه ۱۲ اسرائیل: چه کسی برنده جنگ شد؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/663280" target="_blank">📅 22:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663278">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujMp5pWYwdul2ei5lR9fqEwJB8aFCSo4lXTgEXNstFUh5Q1pBOkoe3QPgXzDTW2bn0Ujti66ol7P94wl6cGUoj6cFV_4kc8tat-ryQf4Ig_rjXJX-v4cge99YEBDRVJ8wfdpnV2ou7mX1Dgp-VC44jQ75qmvuzFkeYrUPwPHE8wlJuvVt_91mGsaxAjZ1z6rvWgRF5h3PRl9QeXFFHv1yUi5yLTetp8GbM2jMnd2fWO2kDEygCDcXjuOc3SiM1wkAQNwkPTuSKd12P1U97XIbcfvqzsRNm_8wPUQki174olyhmn5pGh0ZZ-8A39mzo9x5z_4GASfv0f762s0eXaObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رییس شورای اطلاع‌رسانی دولت: رهبر شهید، پیوند عاشورا و وطن را به باشکوه‌ترین کلام یادآوری کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/663278" target="_blank">📅 22:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663277">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/663277" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/663277" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663276">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/663276" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/663276" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663275">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWa6H8lEb9skTmDOUnPjBoZceSkHKMgLMXR5SHT_lck10w0Y1QgJlBdJnC329LwQerRdAi84vo0C7rKW-M2XM4wMdJCjy---LvGitGkgUxMY9e-c7MKJELyGyY1Hy6suP749Rr9Xc3LRrZN7Pj9Dt1IbH9LT7e-GrmZQCS0BUZFsFxQ28-JCH172jlTT3CFnxSrWQli8F2nlSbPFUspin55udV0a6Ns5FMa6LcpEngY7xyAfQOPb4qanE-1aNSTvDslw-9mBG1dawclfhm8trShYpFvjT6L0dLKNFsk4PWmf25cC66dTiz-qyDKe9WrCX8f5Ri2-t5NguuMy1pBmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چین رسما اینترنت ۱۰G راه‌اندازی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/663275" target="_blank">📅 22:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663274">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXY0q_bUX_KuhYS4dNCBQ5s8xZDexb7Ag4YNOw2pfwxpNvdasL_nEL-cBZs4yIwYYE7PF-jU1Tu6WbFe1o3DITsa0IlvTgPrGm-4jrt55jd8zgegh3iyicupXqNDPlwmHkELKhE-DTBsC8mck6yWYrKvW8DoP34ZZaFsISKCj3hpt-3RafXUbzWNb9sXmO8OkenKj3raoM-85MqAD_q-pEVkGv5omVINJ71XWg0FlDhKc11go-io2tBDsxagi452cgCat6CXFjxB6SIZx3qSeHiK2JBjySD_I4bibNkYIFaXP6fSlcqatLnK2vTWbmJKlTdQLUpJ3bu-7YImnk2zSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار نهاد مدیریت آبراه خلیج فارس(PGSA) در‌مورد تبعات تردد شناورها خارج از مسیر اعلام شده ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/663274" target="_blank">📅 22:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663273">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b5075bf04.mp4?token=Glsz0z3jAR7QPrcTyrus0wpr18GvkWlotWd-UQuri1whHSHHN8uhtYhpC5RDBs_jgPJzhBE4Qod8d4hXTODPaKkYfayosKmJ4uZsi1HpOxkw7Lg3sSvSXWTwb58AQo877D0x8D93vQMP80R3QMYarnLHU66pUZuQJR5qsk94Y-WG_SePtaBIlJyJXb1pCht5zs6Iw-yyrS4lOF2S59FjMiaSRN0EsBe0HQLisqi3Dh3KwzG2NoDkpNm09jRay_uf4z5vlXfYEFpV54nMwK5Fk24NlxuTlyxO_Zv4HCtNiH9JYWhQOuua5Ujf3Uw-MRtd05fzTPYfgb4h9d9QFWsOLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b5075bf04.mp4?token=Glsz0z3jAR7QPrcTyrus0wpr18GvkWlotWd-UQuri1whHSHHN8uhtYhpC5RDBs_jgPJzhBE4Qod8d4hXTODPaKkYfayosKmJ4uZsi1HpOxkw7Lg3sSvSXWTwb58AQo877D0x8D93vQMP80R3QMYarnLHU66pUZuQJR5qsk94Y-WG_SePtaBIlJyJXb1pCht5zs6Iw-yyrS4lOF2S59FjMiaSRN0EsBe0HQLisqi3Dh3KwzG2NoDkpNm09jRay_uf4z5vlXfYEFpV54nMwK5Fk24NlxuTlyxO_Zv4HCtNiH9JYWhQOuua5Ujf3Uw-MRtd05fzTPYfgb4h9d9QFWsOLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شهید طهرانی مقدم، پدر موشکی ایران: من یه چی میگم میخواد خوشش بیاد یا نیاد، گریه امام حسین بکنی اما رهبری را کمک نکنی این گریه تو سرت بخوره. تو همان ابوموسی اشعری هستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/663273" target="_blank">📅 22:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663272">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a025695ca.mp4?token=IbqTncq6JIfs0gpqnHjPNjVotgXlk_BEA98cjKFNDooeDx9ZSamvEj-fyRLDXyaGxARSEOqvqrgvrJ0YuO19S3sVaFUPeNcW8YiPYhukF25zulVXUHXHyJAZokguVCagGKFXIjsPJvnH1XqS1gGa7B6aVkGI7r0ZExkdjfTFW2HP4sprWGWfbgx_4oetUTeTUp7QAbQSwgnXGgnTQ7CGlq1Tlx8etyxVeKLI4J6CApUxKIBDMj9sGPMHXkU3rqzn4B3LeJ-j4wyrpcM0EkDQmZor18Bn8Jm4PlswCpE2EVjOSZEtY4AxeUTH1ShGx1_twodorUh2J_GWK0h6VOQpJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a025695ca.mp4?token=IbqTncq6JIfs0gpqnHjPNjVotgXlk_BEA98cjKFNDooeDx9ZSamvEj-fyRLDXyaGxARSEOqvqrgvrJ0YuO19S3sVaFUPeNcW8YiPYhukF25zulVXUHXHyJAZokguVCagGKFXIjsPJvnH1XqS1gGa7B6aVkGI7r0ZExkdjfTFW2HP4sprWGWfbgx_4oetUTeTUp7QAbQSwgnXGgnTQ7CGlq1Tlx8etyxVeKLI4J6CApUxKIBDMj9sGPMHXkU3rqzn4B3LeJ-j4wyrpcM0EkDQmZor18Bn8Jm4PlswCpE2EVjOSZEtY4AxeUTH1ShGx1_twodorUh2J_GWK0h6VOQpJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات موزون بازیکنان و سرمربی در رختکن مکزیک بعد صعود به مرحله حذفی #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/663272" target="_blank">📅 22:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663271">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔹
اختلال بانک‌ها بعد از ۳ روز همچنان ادامه دارد
🔹
رصد گزارش‌های مردمی در شبکه‌های اجتماعی، کانال‌های اطلاع‌رسانی و بازخورد کاربران نشان می‌دهد شبکه بانکی ایران از فاز اختلال شدید عبور کرده و بخش عمده خدمات به وضعیت عملیاتی بازگشته است.
🔹
در میان بانک‌های بزرگ،…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/663271" target="_blank">📅 22:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663270">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjzlmDYZJCBoSlAapW8kK9PfL613qv1WNhD-LNzSF22QpOjnFuoVZX_OMrLwDeyhiJybFoT17Qd1QojIv6uBJtbqVeAcvPX-G_MAY50eJyQO_-LPZNwhG3Joex6ehHQXCPU1_coDlTcdNrvgs8zrQlq7c5_2BiEYZZi9fki-eX9YuUFiSX_V3fqgcR6SAda_mgo3cTdzW9nOaYornRzCbYavH2hrj-0asTLuIQd0oqJbR87ZyPJegKjfC8v0hRC01eeInQ-hK0bRrwHGVckh-41pq8AayYw2YgWhbwI5Lbv7IYBMcWM-OTgJ_s5Jb1RaWETp23OP8SgZZ1y-1BCwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_اول
▫️
امروز با خواندن زیارت عاشورا به نیت شهید بزرگوار
محمدحسین عزیزی
، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/663270" target="_blank">📅 22:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663269">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔹
روسیه: آماده‌ایم در روند تصویب قطعنامه مربوط به توافق ایران و آمریکا مشارکت کنیم
🔹
ماریا زاخارووا سخنگوی وزارت خارجه روسیه پنجشنبه گفت، هنگامی که آمریکا و ایران به توافق نهایی برسند، مسکو آمادگی دارد که در توافق بر سر پیش‌نویش قطعنامه شورای امنیت سازمان ملل مشارکت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/663269" target="_blank">📅 21:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663268">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔹
ادعای وال استریت ژورنال: ایران روز پنجشنبه به یک کشتی باری با پرچم سنگاپور در تنگهٔ هرمز حمله کرد و توافق اخیر آمریکا و ایران برای بازگشایی این گذرگاه حیاتی کشتیرانی را به بوته‌ی آزمایش گذاشت
🔹
این حمله که به پل فرماندهی کشتی آسیب زد اما تلفاتی نداشت، تنها ساعتی پس از هشدار ایران به کشتی‌ها مبنی بر عدم استفاده از مسیرهای تأییدنشده از سوی این کشور انجام شد/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/663268" target="_blank">📅 21:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663267">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5bc0db45.mp4?token=a0DbvJqLlXZgm49vaRMTSZ0xRFJs26iDoyy9-LluOWGqRn-q1ZzjyvGJjlb17DeGj5BBCwuR274F6e1HWyvUQ6-UO4MLbqRGynFEJ62xMKoQjCaM_JkxI8wcNHKvPz03s6xmJJGH2Hbhqwl6_ThJGve1qTzKSSpH4_wAfBxn2sasxihzrzw2wrXQr3gyMsBJO53JnwFkowDrkmIrFIYFUQURxoveopBsQX_L1f_7shrBpzVc345FSGVUmuFA67pcIDF62dv_Zu4uI7t8PZlV2_GXfHlm2xyIdz8d5nE-srHpJY75mLpCsQScoMl4-hGvssJkQuxOY8lhx6AlPqUnHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5bc0db45.mp4?token=a0DbvJqLlXZgm49vaRMTSZ0xRFJs26iDoyy9-LluOWGqRn-q1ZzjyvGJjlb17DeGj5BBCwuR274F6e1HWyvUQ6-UO4MLbqRGynFEJ62xMKoQjCaM_JkxI8wcNHKvPz03s6xmJJGH2Hbhqwl6_ThJGve1qTzKSSpH4_wAfBxn2sasxihzrzw2wrXQr3gyMsBJO53JnwFkowDrkmIrFIYFUQURxoveopBsQX_L1f_7shrBpzVc345FSGVUmuFA67pcIDF62dv_Zu4uI7t8PZlV2_GXfHlm2xyIdz8d5nE-srHpJY75mLpCsQScoMl4-hGvssJkQuxOY8lhx6AlPqUnHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویری از آیین شام غریبان حسینی در حرم مطهر رضوی
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/663267" target="_blank">📅 21:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663266">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°(منتظر)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3u8lCRnQqQ2NY4HdPoHhEkoD-GcmkSw6CablO70Wn0KmA6R3TfGNktF95-ZSToVk2rYMjC1WSpP8kFkBF0gIFNB5zPurIoJezgsdFdhEWAKuG3tc1JDK5bCaCSwpXV3dMBPUmFoYbLv9rHdDvn4aogtgPbZUne1ztV74IsMqBOnQv8zg6AqOPXt5UrxpUNAWoqYxvBwQrKJUbY1S_lmW0RI8cFv53wn4plXBkRPi4yzfcsTg74V59bB0Dx_8Kg0uDFmiVnKfwdzYDInwVd94kevO2NNQh7wusdomjx8871yEcm7US_ApFiH7YZ4U7Zq2p7y5tR9fmxSW9B7l1AwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مداومت چهل روزه بر زیارت عاشورا
چهل روز زیارت عاشورا را کامل بخوانید از امروز
چاهی که انسان در خودش حفر می‌کند، در چهلمین روز به چشمۀ حکمت می‌رسد.
از عاشورا، چهل روز بر حسین (علیه‌السلام) و زیارت و محبتش مداومت کنید، روز اربعین به آب می‌رسید؛
اربعین روزِ مُزد است!
آیت الله حائری شیرازی</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/663266" target="_blank">📅 21:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔹
سازمان بین‌المللی دریانوردی: طرح تخلیهٔ کشتی‌ها و ملوانان از تنگهٔ هرمز به‌طور موقت، پس از حمله به یک کشتی در سواحل عمان، به‌تعلیق درآمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/663264" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663262">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔹
سی‌ان‌بی‌سی: ترامپ گفته که آن منابع بلوکه شده ایران برای خرید کالاهای آمریکایی، از جمله محصولات کشاورزی، استفاده خواهند شد. ایران این موضوع را رد کرده است. چگونه می‌توانید شفاف‌سازی کنید؟
رایت وزیر انرژی آمریکا:
🔹
تفاوت در این است که با اجازه دادن به آنها برای فروش نفتشان، می‌توانند پولشان را به دلار دریافت کنند. آن پول، پولی است که مستقیماً به ایران می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/663262" target="_blank">📅 21:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663254">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2921aa36ab.mp4?token=TxaskI-Lfru6Huy8A5eiJlc-X13wuw5cwIhaiml1uV7trdGbTjxx9blJYjo1xPMJlLEDsgPY79tMhhwD7uuTPFbGXb6qO8tBjhMMBfryXXLzCS-lTseoMGOPWAKca9ts_i2zHYDYpXd-zLwjJtA4ndR19coYA_hI2zBr5itPSbizpi0VuE5YFMPzvkC-PlRfPV7CAQMxElMH0xz3aTLlfygtDb1hxzb4xCDVQznHtuf7zbIWpXJ53vQUtC-mKWwpFTsDNN5_z6LiBW5qhWWr1YPrHr6TrBkBWE6yPZuYP4iHPAYNM1z3tWyOI6tH0dtCQOi4geoxfGF8vW2wpiorXzwSv6Vo2F9n4MlgKfjvETM0l6bV6DbctMq9_PnTuLQrUTD8x6JzP-qSvj_e0a-M1OzqDs4dUfB1NTXvPx8dTJlcPIpVUZSmLyHcqj45ViV4xWVFZKeOzRIe6Pt28B4MsO8KJEeq89c1lZDI0mXKDD2SWwNKK1yiQjc_0MBbUMq79Ex8zDipiWxgbqY1fUSWrwCxqQ5lWPEUVX-wq1G54kNjjKbLBCNN4_xji1Pio72y300QQV7CfjRdJ2kQ4sHQ7BvEdgr1lBuK27X5jDerYPpCPfBhlhk6H9ixP7q08OTaS6LSM2hpex7DfKJkJablr-foRjUnv0ObyK4YqlSKKOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2921aa36ab.mp4?token=TxaskI-Lfru6Huy8A5eiJlc-X13wuw5cwIhaiml1uV7trdGbTjxx9blJYjo1xPMJlLEDsgPY79tMhhwD7uuTPFbGXb6qO8tBjhMMBfryXXLzCS-lTseoMGOPWAKca9ts_i2zHYDYpXd-zLwjJtA4ndR19coYA_hI2zBr5itPSbizpi0VuE5YFMPzvkC-PlRfPV7CAQMxElMH0xz3aTLlfygtDb1hxzb4xCDVQznHtuf7zbIWpXJ53vQUtC-mKWwpFTsDNN5_z6LiBW5qhWWr1YPrHr6TrBkBWE6yPZuYP4iHPAYNM1z3tWyOI6tH0dtCQOi4geoxfGF8vW2wpiorXzwSv6Vo2F9n4MlgKfjvETM0l6bV6DbctMq9_PnTuLQrUTD8x6JzP-qSvj_e0a-M1OzqDs4dUfB1NTXvPx8dTJlcPIpVUZSmLyHcqj45ViV4xWVFZKeOzRIe6Pt28B4MsO8KJEeq89c1lZDI0mXKDD2SWwNKK1yiQjc_0MBbUMq79Ex8zDipiWxgbqY1fUSWrwCxqQ5lWPEUVX-wq1G54kNjjKbLBCNN4_xji1Pio72y300QQV7CfjRdJ2kQ4sHQ7BvEdgr1lBuK27X5jDerYPpCPfBhlhk6H9ixP7q08OTaS6LSM2hpex7DfKJkJablr-foRjUnv0ObyK4YqlSKKOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
لحظاتی منتشر نشده از دیدارهای صمیمانه خانواده‌های معظم شهدا با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/663254" target="_blank">📅 21:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663253">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f8e53946.mp4?token=isHIqA2VEIH8panfVvHwUu-Qi2mCbQODWG9UZRSXbI2EFYndmY7ZKttydDL09jjgxq3drRL2cCFZ5DSATkeqmaANp4mwu4r8-VcUXx3cFHkzeZ8eHDPWqTJrTPGzfVyv7O3vi2KNT9nctLwWCRm_y6DuawCnOpRe-aa84HSXeqXsadIChl-T3Kg8XFif66ILyk2pWvT6HfoJbJ4Imb0-TKYqsYPa_xxz36kleGCPw_JWbeFUI3BXcmwY3yVKvdELAeqQhttVeqlaNcrzKy_ob8jwFbHPb7AMxPpd6AzM2UDtvGK_-4K8a7o5K7taqOrXC9koEazGKspGj8iq-f1KKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f8e53946.mp4?token=isHIqA2VEIH8panfVvHwUu-Qi2mCbQODWG9UZRSXbI2EFYndmY7ZKttydDL09jjgxq3drRL2cCFZ5DSATkeqmaANp4mwu4r8-VcUXx3cFHkzeZ8eHDPWqTJrTPGzfVyv7O3vi2KNT9nctLwWCRm_y6DuawCnOpRe-aa84HSXeqXsadIChl-T3Kg8XFif66ILyk2pWvT6HfoJbJ4Imb0-TKYqsYPa_xxz36kleGCPw_JWbeFUI3BXcmwY3yVKvdELAeqQhttVeqlaNcrzKy_ob8jwFbHPb7AMxPpd6AzM2UDtvGK_-4K8a7o5K7taqOrXC9koEazGKspGj8iq-f1KKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
فیلمی قدیمی از عزاداری مردم اردبیل
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/663253" target="_blank">📅 21:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663252">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔹
وزیر انرژی ترامپ: پول آزادشده ایران به دقت پایش می‌شود
🔹
رفع تحریم‌های نفتی علیه تهران، به ایران اجازه می‌دهد تا نفت خود را در بازارهای دیگر به فروش برساند و وجه آن را به دلار دریافت کند.
🔹
تهران قادر خواهد بود روزانه بین ۱.۵ تا ۲ میلیون بشکه نفت صادر کند و با دریافت وجه به دلار به جای چین به بازارهای جدیدی نیز دسترسی پیدا کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/663252" target="_blank">📅 20:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663251">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a2cfe27a9.mp4?token=X1Kzg2GMUN2Kzl-r5_Zjn--pWiyVM5xUb_xMWgQ3Il8bsx6wD_PjzXjREBU6XatdtyHY-AdUMDJaL1jkawhQINmXFil74ZBuPqpBnb4eiY0jiTcc28cDKXugf5Q6jIb5OA1ceUTurQo6dmXT5ak3rnY1jYnQvQglq-W7q_5Qoo7QL-dg7IAm7zjN5BtATyQ5EBoTo9cYN9Hgpz5ABl14fkzRHYbARwQfUs7JRpqg1y2fOr-r6_TZof9Fo56yqTpEcWHrv5nS8VHmI8pusfVCyBmWdnV4fgnp-ZHzeWegIWrU4BtAUErV-s_E6I_0iYPvz6rtSezZMLnWCMA13eHdzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a2cfe27a9.mp4?token=X1Kzg2GMUN2Kzl-r5_Zjn--pWiyVM5xUb_xMWgQ3Il8bsx6wD_PjzXjREBU6XatdtyHY-AdUMDJaL1jkawhQINmXFil74ZBuPqpBnb4eiY0jiTcc28cDKXugf5Q6jIb5OA1ceUTurQo6dmXT5ak3rnY1jYnQvQglq-W7q_5Qoo7QL-dg7IAm7zjN5BtATyQ5EBoTo9cYN9Hgpz5ABl14fkzRHYbARwQfUs7JRpqg1y2fOr-r6_TZof9Fo56yqTpEcWHrv5nS8VHmI8pusfVCyBmWdnV4fgnp-ZHzeWegIWrU4BtAUErV-s_E6I_0iYPvz6rtSezZMLnWCMA13eHdzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: نمی‌شود برای امام حسین (ع) اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر و گرسنگی باشیم و نسبت به این مسائل بی‌تفاوت بمانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/663251" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663246">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f284bc3e.mp4?token=P-Pu7uKeO5OUlCGKa9AzbAlwLCoO1Uth6YRyFvaeEWqjXZ34A38LDtkHss1h04BaZaYjNi4s6-AY7J2GD4gCX3FdpLUIGMJ6X9RovosHePvvWdncqexTCOut9e9piqpLMDSG3L-tdoLRHrbsnkCqhVWSo_hsS_mecCtdHSZaPd_jDl3TCbdkZw2oDUPVnhkjeKMxUOAgWt0d7qjHqlKNoZ3rDUkZ1UmasDPT1Qe-L1fXYCCih0gMoR-FTa4CT_nFxKZM0rIn_tnouCW38mxYdB7AJ8ReHsbqvbxZ6fm3WQsmw1Zp9K9zwt_tYDcaLxnZ60VhpqHeTORL7WrfsdPGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f284bc3e.mp4?token=P-Pu7uKeO5OUlCGKa9AzbAlwLCoO1Uth6YRyFvaeEWqjXZ34A38LDtkHss1h04BaZaYjNi4s6-AY7J2GD4gCX3FdpLUIGMJ6X9RovosHePvvWdncqexTCOut9e9piqpLMDSG3L-tdoLRHrbsnkCqhVWSo_hsS_mecCtdHSZaPd_jDl3TCbdkZw2oDUPVnhkjeKMxUOAgWt0d7qjHqlKNoZ3rDUkZ1UmasDPT1Qe-L1fXYCCih0gMoR-FTa4CT_nFxKZM0rIn_tnouCW38mxYdB7AJ8ReHsbqvbxZ6fm3WQsmw1Zp9K9zwt_tYDcaLxnZ60VhpqHeTORL7WrfsdPGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری هولناک از لحظات اولیه زلزله ونزوئلا و خرابی‌های ناشی از
آن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/663246" target="_blank">📅 20:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663243">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8xHBuwQwMvRHg34kmhKKOJIyAgKnWbYdM9-5dYzHt2EyjmUaoYBpoI-douT-FJLn97LwFjp54mc3HYBEVKcOOa9oaoccyK1yWJY7wE0GXrlVFb-aAgLYpPcvzcxq5kDhRj8_37QXmuBLBCoG1k0ZpwElDFXD6DQ1rv44SGXv5M_Er5MS3snv7NCEa9PvvcEql-4KOZ7TIiCLhKlIQ6LnUX322-Uyq2wsspDXY3H25W6YSvoy4ZIr4xIeAROPw5qj3x4LN5-xvefxLK8e3V2Ee5kRPBIQS1QQif75eLkI2_Lyllqc7Zig-D65n6Fb2EuB_UYegHYrgDmZvrIAM0zwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر رهبر معظم انقلاب بر روی موشک‌های حزب الله
🔹
حزب الله لبنان با انتشار ویدئویی، تصاویر حملات موشکی خود به مواضع ارتش صهیونیستی را منتشر کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/663243" target="_blank">📅 20:38 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
