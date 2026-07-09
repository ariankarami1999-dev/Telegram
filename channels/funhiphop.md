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
<img src="https://cdn4.telesco.pe/file/gz-wUecz-Djl4uYFk3oxa3PaMSdIIgJA0ryb5QO0Mug0yDQ_Z9Qd8F9ik0JxsqC3qBwvbUBFisfAjFrjklRi5mY1TgNpa-_EYH6HqOIHiBfYHF72xKZSzE4fwHncgjkSVEvpkVB-oZOs3oqObd5-stGn6rkMXmHmMVRZCPUdZNO95rkiPqDvPUAbjR9pwV16xLctuhJ4N940ZhKR0lyHdEOHmTPIpQWeM64-VTpi6KjZpPOoTSi_kUBeiWzOfbULadWmcJqn3ijL41zZoRLFLar4q2bVDME0emfMQhQG8BECYKAIj8uNjNIlUXHWFPs1M3x9lAjJnA3uRaKqPZTC1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 198K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-79829">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggQf1TLYCkmPVSKeAxsT41cI0JSftaBEvTwr-AodFqcAZQCuytNMW1fryMzrSy4a9Eu9GpEN7xZ38iGEg3EFYmKqwQchL1TfB8Ttrsg6Yn2qHnzLlxCWm8c40cXvpQnT69N9Bedr2ED6_hfV_oE1pibGKZjDWis1742Itp97rtUtvqt7sgreSCtj7YWw5xttM0aLot9CHdtBLdNJ9SnIvpZUFpyI_742v6eGXabUvAx_W9D0rHVDTH6R68tfji5xnsD_2h7G3q6p_CnmDbYCaRljkAWQR-0wxEsf4zX_RosOz5pq7l9Qvt6lmLELumWQiZwSzaCduBeA4ArXaOGv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا
هکتور فورت رفته تو رابطه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/funhiphop/79829" target="_blank">📅 17:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79827">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SyMjqS11usyKBAA_Rgy5553XEsEu3oMnQGsneNi1UjF0BEhN3mHB7RqGe_VGiC1bk_pMB0jTYysKolSOUy1bTZHBkCTjzXUhs2kN-6F-AVE6mXLAeT66V4kpGsqxW7dYKa8mV2GC8lqXNRM1b3s6W6Mez40rPelRQL_RG-Omr2UR1YCrdOt6EjbaFBecckDO63YQPBRRUNxptcIIsn1KsVDe9sJaugt7Rg4s4dh8zXCoXSwQVhNMXnvgf31EvUNTYixoEA40S1FVuHUUGt8sEDvZyoXoKMzj_Wqoemjp828O67xuA18yfkPrKf99j91AUArbeq9Wbr5-ZU3KvEfybA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFPGTRbqCMGdcdWdC5cEWB61_K0rnA2Ejvwhvbf3KaOm9Kmfub4wZcRCXeTqKm1eS40n25JCbK8Osn9KqFjNqFesFUUJ0MztRDHWflYW2-8N2zeI9o7jjcixiqBU_piZYBpJZadSir_0j5A91P9gOkLZMMr2F1Elm3zmXd9EzLPWHnlNZeyK6rAbTKIjrYyl2NRZOWPk1b9xldmTijoJy2XVApyAFGa9yKhYA-n22Wh41dybJ5kh5RV604Ig8xmIS7_lnC99Ln-ws1TduD95cS6-l9MTHUu_y5rP0bBN3orZ3WZje7K-svHvfuqxE_LXjvVC9JH1QoIWHKSI8D44PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط لجندا ربط این دوتا تصویر به هم رو میدونن.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/funhiphop/79827" target="_blank">📅 17:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79826">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP7c7qsUgF0HaDULI8yV0h1sunKiLTb4VhDCC11u7WbAE3neOIBJ8bIq7JRT593xGT-DYK-_pcUCtKFN6PPYjFk6lR1DTNtRQg2yYm2TqW1_LuWtUxYRqS-9tKbTJYX1oFYup9w1uJXS9o_TT2pby598tRmKCsl63rmlJyYCvW8gbvPyu7HQYJuo8GrNgasIE6gPyY1y2P_QYLcrWxQnAK9C__AynJV5ihZ6ydDblMgCb0bzpYU-9Jo_c_Fbl0lFi1OujsL5MXqq5CjTPxnyB70QBlqq6ZbKrOpOOqOxZ-aRwbOL2_2z1_xdc89TWffZDztg5poZhOlCc2_llSm9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
دو هدیه ویژه جام جهانی ۲۰۲۶ (مرحله یک‌چهارم نهایی)
🏆
⚽️
روزانه با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های مرحله یک‌چهارم نهایی جام جهانی ۲۰۲۶، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد در هر روز از رقابت‌ها ۱۰۰ درصد مبلغ پیش‌بینی را تا سقف ۵۰ میلیون ریال به عنوان اعتبار پیش‌بینی رایگان ورزشی و در صورت موفق شدن پیش‌بینی ۳۰ چرخش رایگان ماشین اسلات به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/FWC4
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r18
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/funhiphop/79826" target="_blank">📅 17:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79825">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آلبوم جدید ناجی به اسم Nowhere منتشر شد.   Spotify  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/79825" target="_blank">📅 16:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79824">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkENBTqOboPrGjoECBDB4IeEBugtVXcBYZw8ZpRT3b3d21id-z-o1rvxX931h7uXlWKUmkvNrvACsq2BsyuB_QaksbIg5du4_b8M1esjN6HQC2NE4iME3kOWs_uT7mpJvKDW4OvxAphSjYRKYMMv71WXy-FWMMznhx-NDckVv34wl4hTMnSzW5AQfQb7DtPqTlHMYHWIG9YQlJT6NrI93eP9sI2THL6ZromOFNgTnL1e5sG4NGcbodsGUYUE-NikrUWVY-DuK3ibPL2OAmFZkp60yxqLU2k9QtFvbaC9-9S5xrTunSLKz0kqtXbELAnZpzmmNOWB2_k5NynCryjGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ناجی به اسم Nowhere منتشر شد.
Spotify
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/79824" target="_blank">📅 16:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79823">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=PxO2yMF14vF3VXPkRSpaAwzUUiivmQNb2yxNLutegqMPERt0JCcXI5xTV79Kc1nx1H9auKl6awOh5QUxrdoI2HfGyXJKUtUKtFwyLTjv0Zyxz0-Wyiw7KawvgpoNuqG0hMfnqx6PZNRqKKrnTNAnri2Uw8FYIBc53aMR3bXnaca7FrmJXZVFBYDHVaEAm351Iz2em1bkC7Y55VizNy2nMrttjLzOPAgt6skvUX-MBiYPw-NloQVipRXeXa-DpMTmEhvlrzEzVoynyf3DYcQfzEzL60W73ZfPRC4zAQIUvCLFT4p-jyxrNjziv3hdCA2RN3tcHmgVyRnRVA8UHe1sIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=PxO2yMF14vF3VXPkRSpaAwzUUiivmQNb2yxNLutegqMPERt0JCcXI5xTV79Kc1nx1H9auKl6awOh5QUxrdoI2HfGyXJKUtUKtFwyLTjv0Zyxz0-Wyiw7KawvgpoNuqG0hMfnqx6PZNRqKKrnTNAnri2Uw8FYIBc53aMR3bXnaca7FrmJXZVFBYDHVaEAm351Iz2em1bkC7Y55VizNy2nMrttjLzOPAgt6skvUX-MBiYPw-NloQVipRXeXa-DpMTmEhvlrzEzVoynyf3DYcQfzEzL60W73ZfPRC4zAQIUvCLFT4p-jyxrNjziv3hdCA2RN3tcHmgVyRnRVA8UHe1sIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواپیمای حامل تابوت توسط جنگنده Mig29-ub اسکورت شد، نکته اینجاست که این نسخه آموزشی و فاقد راداره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/funhiphop/79823" target="_blank">📅 16:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79822">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اموزش پرورش همچنان میگه امتحانا سر تایمشه در حالی که یه سری از حوضه های امتحانی کنار مراکز نظامی قرار گرفتن و احتمالا درگیری تا چند روز یعنی اولای امتحانات طول بکشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/79822" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79821">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivz6JXIF7OAgiD0XEpEEGFYZjIHcbr8zPSh_tdeVnV8j7fUAoHisiPeOWIExq4Cz5_qiBNCevMlJiIKxiY1movtCEpmw2QlbMKlFIuiTvpzSbG2KTnQSKwtXM3FmB0AD87xn596HdVNEEIcDnLxPMUzR4XzE-ypZDIKUKu5cfqG5Pw8_ZIYJ1S5Pnpq1_6_gBO2BQeYiyQ-mqrp9hTpIXlkHvW3i0Sj3MpbHodOSMNScu5PZIEtZ9yOay54VPEaGcW6_pH5KB0UM2OTYRg9jVQaaTEZdRnUZDO61IRE_HqRk-q4syXTnNB-S-h5k6CaProyveTjzsnb2atCz2_MgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این 3 تا هم تو حملات دیشب امریکا به خوزستان کشته شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/79821" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79820">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYk_9s1xfMkFDCNKJIedYN4O5K5fOrIy16sjoHyJ08ENwlGbCJQtfOiJItOeXpZVB_54hJtjqC4OF68ILhU4StAqp10jD5iW6dMwK9PlNVxGz67vnUeHmt5jGyfU1SnCYJr5D_of98Kf39-VbQEvoi4UKL9aUOAD_dJuOd9QLbxhYIp0lt3Ep7uAHNg7sm0FYJcidUiyKAVQ3fPl8War_rh33yR0o7PIXPnBULt5qX7VR2Zdehb1VCnTcyFlhSCu-VvC1Mh4LPqjFe4-pJCLSCCATMgDSfWYyj6wfG857Vv43rituALgwj2xifzjjUKOEmP1Ibdklqw2baHl6ZyP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان دکی با موزیک ویدیو ویناک جق میزنه یعنی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/79820" target="_blank">📅 16:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79819">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/79819" target="_blank">📅 15:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79818">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درحال حاضر دکی کیر ویناکم نیست</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/79818" target="_blank">📅 15:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79817">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/funhiphop/79817" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79816">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkKF7gsNHmAKmpPvZJlIw8J3zZ-VBlr1umZkHTjLZ1d6rakemPiX085OE8ic-kGWKttWP4ofTXj4i-enV_NC26CPTBfW7YP8iNT_SV2soGK_2WHi_-sDqranlYum_JgXL0b5vjJ3HWgTExv4Nv292scUTFF8UspIomADUJhBPXGxk4z7yLEMXjZLLIXhhmk1b9iFjiUKJz6yOSUWQjcgB69W0Sknq4YuW54qKSNpxmF8G8kJJIZgoc2ybgelf2dYRXsbdsRhxLfBvvZ4KZ5fZFD9jJjplwmoy-FCQlweUMKFble_0pt9gfZKvxiAJv4rZwW59g3eNyWDCijDJ4K0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/funhiphop/79816" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79815">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeGEfh8UqnxSsSL3SYqMVf1-f1SOK8tOJ64wjD2mVyAyyPN1fgpoERd--5OqpJ5UEf4zF4Y_R8nPja-B6YMs58JDBt32aYsnN3m-zCWPai4KgkLDbyrGFFsyEKBDnYC9BXWYyz8tegt7oD3KAUll8jHaOs32rNhjtVPjWSzRHWFO3w5Z9-ibFGYPDKPqHGxzq8d4JGrwte76TNGPnQLBdiIRmFF2tujZcQAy-_NgCV0fyr0aPKzjLbNMsrWe3Gbvo_jQcI2ykrcV489Zgw3Y1CprvwfAnkfoarV17HCZokRv4L3eqIIdW1hh_DWnTRWOoZnDjK_lx2jO7XbHM4jm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک ویناک اومد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/79815" target="_blank">📅 15:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79814">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💥
OFFER OF THE DAY | تخفیف شگفت‌انگیز
💥
کاهش شدید قیمت‌ها به پاس همراهی شما؛ از این لحظه تمام  پلن‌ها با نرخ جدید محاسبه میشن:
💲
تعرفه جدید: فقط گیگی ۷,۰۰۰ تومان  سرورهای پرسرعت اختصاصی  پایداری فوق‌العاده بالا  مناسب اینستاگرام، یوتیوب و هوش مصنوعی و گیم…</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/79814" target="_blank">📅 15:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79813">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHqm11ip593HeCnjAwncZzrnfLdoczZK7hnPHBJ_62RpSNIy3I2ODL60UPHBHXrUvdgS4ttcPonQrTdEyk8s9gEMNtMyjJtdh29rVlQdQ5Jal0iZOmyMUxljkPssuc3PasQz3YPS1G5mvphdmidw6NcN3ogQ7TTeOOB8EROBBZyi4QZZFOb5UqnXPoQWZbfGUfRjna6hrTAgjn2l_kk0gHhYZ8r1vda58qHZIrFOhf9Tu7jKkc503KKyhxgyvrGJG65Id3lgQqx7GVVYXz0guwXp6yZbEmnHOLkQ8DBYcqP8lOHGPxIOvuhOWgRsJFwVqfHn3yUVYWdXVdutn3pAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امریکا بترس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/funhiphop/79813" target="_blank">📅 15:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79812">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتتون ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/79812" target="_blank">📅 15:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79810">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0sK-GcxvFNovdoydZ_O9wliEJKmkWtM8ejr-rvX3oBMVUqHloOodFKSukgTA5DMecGF8lF4uzDdC8GA9lrykYfUHRim329fh_suW7v6cm6JCovn_3BIEJN779O1bbJtQPFtwOXQkNCZS_DUPqzVROaf2Sg0m9YIp76llY1Ga2Jxzydvs5djIYBNSizFHO0quu4KJm8rti8pdi9gMsPBe8JTp8tWZXLqG2_qz3yoBwC-pe8MX-tu3YsrSf6Ihs76CkT453-EY7bwCBQU8vnHmkjNi1N_HeMidjILTJDLMjSLRQnfn3CpHwKti1xvc1MX29paXnkf5Zs4lJG1WveHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قمار باز به صورت زنده در حال تهیه گزارش از اوضاع تنگه هرمز برای صداسیماست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79810" target="_blank">📅 15:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79809">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تو گوگل سرچ کنید erling haaland بعدش چند ثانیه صبر کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/79809" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79805">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شاید باورتون نشه ولی آتش بس هنوز نقض نشده</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79805" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79804">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انقدر جنگ دیدم و برام عادی شده که دیگه حتی پمپ بنزین هم نمیرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79804" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79803">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">غزه در زیر بمب ها زندست، غزه با بمب ها نخواهد مرد ولی آن روز میرسد از راه، که بیکینی باتم شخم خواهد خورد  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79803" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79802">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آغاز موج 649767667 وعده صادق 27 به سمت پایگاه های استکبار با رمز یا زینب.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79802" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79801">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brtkbywSYtyLnfKizlnwaNSaWzn0-eO34UAF6V2H-xlReXtKsDG9pV4ulUV4aPaQi9x_c29_IeHox12X3zWbq5ORBUZbcSqC4zI47gpIMdixkazun35ilSMihs04CC6RcPPmmMD_Bi0WLNKpDNXpzNf01hNmltyNz98HB8Q482_PrD7DtmB0m1gp9pLdTJ2HB1_5DVLA5Gx7QzbZxBWWnOAX6jmt4qvoCPyIMy_NcZJTuaTBkIlXu4fQE5vfGK1LVAURucAGuXUxiravOENXG-fYeeS_emdYSa-YiVywUi-oZSFfr-MFC_4DjTYLVRyN2wk1TcnXlL7Gj3E9I2xg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز قراره کسایی که تو تشییع مشهد شرکت می‌کنن یه پرچم به طول ۵۰ متر رو حمل کنن که روش نوشتن We Will Kill Trump 100%  اگه باقر شاه جلوشون رو نگیره تا قبل از طلوع آفتاب فردا بمب اتم رو خوردیم خدا بخواد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79801" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79800">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGA8IL5niA0mVO-DOBv2c8ax78TvTZxYbIoS98wQiJTvJjLDLwJN0jP05k2w6pmYnrw5q4VuFnVw-ODx5fTClWOJBRePvJGe_JSeb9BrXX3sedDvP6cmwjLz0flmbjSvc8Xwn4jpC4Tu2121EuUhuGTvMNaOGKWStrbivHXQUtjfzKkPCD1b8eBIwr6BF0mVZyaCJIwUhxwtqpOlOxrGk6lSC0IdPhhr17JAjuH_AwYZAWkcknbd1iPmIbyuOkMQVNjDJ-V3taPpmo2rjrBXp4Q7lHeBEbdtB_Nr2MeE-F644g8u-z30IsCgRCUHD9pS0M7PXxBE4IPjdDtLi77asg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز قراره کسایی که تو تشییع مشهد شرکت می‌کنن یه پرچم به طول ۵۰ متر رو حمل کنن که روش نوشتن We Will Kill Trump 100%
اگه باقر شاه جلوشون رو نگیره تا قبل از طلوع آفتاب فردا بمب اتم رو خوردیم خدا بخواد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79800" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79799">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بوشهرو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79799" target="_blank">📅 13:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79798">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989fd48c48.mp4?token=YQk0Mrrlh14yaucTj0nWugL1KEfOd3-egGlG3KNnO5DABjcg1P7t4F30oYw8kUfmKH3255gMh8yRVR_9ZZjO6rjPGeIf-DXODBsS0WSfWodRUvzILsU2tY0HpGYKlIJxB3yhMv8Q-6Al4pUq4DQbf5IZjgUiB2q7J5Ls2WBd7BgvndYVNBbyFHc32Y7kdHLVQT753j5mHvpmIs2bxgt4OGm8XAiXszPT2nQjIuAaopbyVspY4XI2DYRwzGuDTIQ2hyl7_dEbSRP97eIqed-qRlC03PqhlujcpI7fCSZjzAnkmfzW82F_eq8ufgH8qwqUAkE7YFdtobVfVNz70Q2vSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989fd48c48.mp4?token=YQk0Mrrlh14yaucTj0nWugL1KEfOd3-egGlG3KNnO5DABjcg1P7t4F30oYw8kUfmKH3255gMh8yRVR_9ZZjO6rjPGeIf-DXODBsS0WSfWodRUvzILsU2tY0HpGYKlIJxB3yhMv8Q-6Al4pUq4DQbf5IZjgUiB2q7J5Ls2WBd7BgvndYVNBbyFHc32Y7kdHLVQT753j5mHvpmIs2bxgt4OGm8XAiXszPT2nQjIuAaopbyVspY4XI2DYRwzGuDTIQ2hyl7_dEbSRP97eIqed-qRlC03PqhlujcpI7fCSZjzAnkmfzW82F_eq8ufgH8qwqUAkE7YFdtobVfVNz70Q2vSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیری مادرکسه ای حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79798" target="_blank">📅 12:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79797">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فلیک یجوری داره وینگر و مهاجم میگیره و کیرشو کرده تو دفاع فک کنم بارسا فصل بعد هر بازی ۵ تا میخوره ۶ تا میزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79797" target="_blank">📅 12:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79796">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سپاه بحرینو زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79796" target="_blank">📅 11:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79795">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ذرتارو با موشک میفرستن خطرناک نیست؟ یهو باز میشه پفیلا میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79795" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79794">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c169218f3.mp4?token=PiTxc0W4cbjBQ6MjA8LraIh9XUKfGysFXxPpzMFQHTfFY_eZIohUTUlt0TrkFueKA-8_oelu9EmLDNfHL47aon6sAJi_7Px7x7mOwkWmhZI1iX0bZzz1qWtTia9sm7zevzuJNSJgHEXYXhwMZIxGB4_bVP9ZQAuSUGVHK1nKuSZLnSh4UHWpF9cG2gvbjA4DChZlP83sNjj47GcvTubhfkHV12dyvqOtEHIL3pzNJgTaYM5YpnuEFUPkNzO0Z6hnBhSvBM_iGDzdrJizKgCpkJS3SEhSQDf8XUFvI8wIjfOVyy2z4fOdJOixGuqlWpxhH0OJlK4Rnm4YCRsb4lBqXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c169218f3.mp4?token=PiTxc0W4cbjBQ6MjA8LraIh9XUKfGysFXxPpzMFQHTfFY_eZIohUTUlt0TrkFueKA-8_oelu9EmLDNfHL47aon6sAJi_7Px7x7mOwkWmhZI1iX0bZzz1qWtTia9sm7zevzuJNSJgHEXYXhwMZIxGB4_bVP9ZQAuSUGVHK1nKuSZLnSh4UHWpF9cG2gvbjA4DChZlP83sNjj47GcvTubhfkHV12dyvqOtEHIL3pzNJgTaYM5YpnuEFUPkNzO0Z6hnBhSvBM_iGDzdrJizKgCpkJS3SEhSQDf8XUFvI8wIjfOVyy2z4fOdJOixGuqlWpxhH0OJlK4Rnm4YCRsb4lBqXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه یه دختری بود تتلو شاشیده بود روش؟ حالا اون دختره تو فصل جدید عشق ابدیه بعد با یه پسره دعواش میشه پسره برمیداره میگه حداقل نشاشیدن روم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79794" target="_blank">📅 11:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79793">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItPZh9gGJ04cI1OiamQ9uyf2aUxJCr3Zyy-AkiIeVOOxoIrwELuNbwJYyUB_J8t25gtIRqtn7C1Pe_1zt2F8A7_l1T26ngSnKAHpueEIgqnHhfY4uv-cORuMWXy2gnJwffNUndqPmbuUcoLG6TkQ2m2HidVCki37yJcUG8XPE146fY1SHA90Nyp69rScXopjgIYx-JQ7JtDauWlSAG1VJxTZe5jDNgrjh10BbAAzdJ7Mb-Fq6iIp5UawM4tkYu7aOeMw1xpQNZZcNkIs51jgUaf-8rJ6buUvgomLDoqeuIRjjYxvEGPZw_XvJjY5sT0z1w4duX1PIWk6G30-_1l3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
دو هدیه ویژه جام جهانی ۲۰۲۶ (مرحله یک‌چهارم نهایی)
🏆
⚽️
روزانه با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های مرحله یک‌چهارم نهایی جام جهانی ۲۰۲۶، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد در هر روز از رقابت‌ها ۱۰۰ درصد مبلغ پیش‌بینی را تا سقف ۵۰ میلیون ریال به عنوان اعتبار پیش‌بینی رایگان ورزشی و در صورت موفق شدن پیش‌بینی ۳۰ چرخش رایگان ماشین اسلات به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/FWC4
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r18
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79793" target="_blank">📅 11:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79792">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این خط ریلی که زدن یکی مهم ترین راهای تبادل کالا ایران روسیه بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79792" target="_blank">📅 11:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79791">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJp9PhFUBvuNOVc7_HpgDU7WGoZ0B_nFXCul38xu16Oee0x80P-79LiLn1IQPQNiAMDXMFYtIGCSoWiqXGShS0e1htpiM7D-eRn451GGIX3Jn34Te-7JxZH0fzWUBZUw4qbO4-B679s_qrUaexUDJM0uquSHYs1L_m7tNp-i8PKyRaTvih8ETCT40szG3nR23XFBOBfO8pbEnWbCZ0gzUb6mAPdK4IrdzpmzGi04N6WE-7if6YFMWudWaC3mPeAJmMxpwAJ4QW-GpP_FmuKPz9HQgdTknrw_UQU0fXYspQ5KUXJyeA5bFd9WDExsGQj5gFQvI5F24B88d3mznw0_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات تأیید شده آمریکا به مناطق ایران شامل: بوشهر، بندر کنگان، بندر لنگه، بندرعباس، سیریک، بندر جاسک، کنارک، چابهار، ایرانشهر، آق قلا در استان گلستان، جزیره قشم، جزیره ابوموسی و جزیره لاوان.
حملات احتمالی آمریکا: چغادک و جزیره کیش.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79791" target="_blank">📅 09:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79790">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34521567c.mp4?token=JplqC_B7VVIVPcE76I-Sp40ViUBO_wneG4to7HxpNilbZO7kz9kTG-YAj2RU-CxllLzLXmYy3DtHOkBFH6yJXuHww3UdxHrRuqFzLIuumNKM3zWwmdNC2Ea-G9eSXAaIfB7WS8nMzf-FQM01cVky0O-fryybwbVSMt1wj8b3QhvooghsAy5w_uIBsSLJ4QFSimWH-5iNK8iKltqWsJFM4peluqgfNMU9GnW-1W6PlSS8JCDQUDj4O_5au2lbcq60NyB7VwD973HLLIb7K3jNXCxX5lkd07I7IiSWdLGfv8OgOj2hw3c8vf_D70hPUi3agVpEzc6BD22SRUspDLYNOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34521567c.mp4?token=JplqC_B7VVIVPcE76I-Sp40ViUBO_wneG4to7HxpNilbZO7kz9kTG-YAj2RU-CxllLzLXmYy3DtHOkBFH6yJXuHww3UdxHrRuqFzLIuumNKM3zWwmdNC2Ea-G9eSXAaIfB7WS8nMzf-FQM01cVky0O-fryybwbVSMt1wj8b3QhvooghsAy5w_uIBsSLJ4QFSimWH-5iNK8iKltqWsJFM4peluqgfNMU9GnW-1W6PlSS8JCDQUDj4O_5au2lbcq60NyB7VwD973HLLIb7K3jNXCxX5lkd07I7IiSWdLGfv8OgOj2hw3c8vf_D70hPUi3agVpEzc6BD22SRUspDLYNOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 4
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79790" target="_blank">📅 07:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79789">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به بوشهر و چابهار مجدد حمله شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79789" target="_blank">📅 06:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79788">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آغاز موج 649767667 وعده صادق 27 به سمت پایگاه های استکبار با رمز یا زینب.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79788" target="_blank">📅 04:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79787">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آغاز موج 649767667 وعده صادق 27 به سمت پایگاه های استکبار با رمز یا زینب.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79787" target="_blank">📅 04:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79786">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p45DueBzbsxTZqJak8Si__oQ29GA3hRwa0HxeoFChF4i5nj7SljLsPF1Tj0PBnCeGGwBRuZA-hvpveHsi254q3LA1craztQaBTcTBW4E8mSH6vwFymkMVFp7J1gG2k3KeS6YoQ09MaNkkI9zkjCRhhXRrDY1b0JSHNZ7avv3aJU486MzvKuIC4dLbzizAflEsRWSDKSXogLpnzaynyPppFua3k2bdfmZI7zeVOr14QM0G4wqf9_aYC0mVHn9afgJutuMQ2AN9UEJdhKnP3ehNiKVRNpX0Ow03SdBpyeJVUhEK9x0vQnb1UL4joXG6FilPkzROQtVj6U7CBhXibirVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال رو هم دارن میزنن  گرگان و اق قلا   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79786" target="_blank">📅 03:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79785">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شمال رو هم دارن میزنن
گرگان و اق قلا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79785" target="_blank">📅 02:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79784">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بزن بزن تموم شد بیاید بلایسیم  https://t.me/+3BUNQoy8hp5iODE0</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79784" target="_blank">📅 02:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79783">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بزن بزن تموم شد بیاید بلایسیم
https://t.me/+3BUNQoy8hp5iODE0</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79783" target="_blank">📅 02:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79782">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شاید بگید ایرانی فراموش کاره
ولی من بعد سه سال هنوز زیر پستایی که اهورا نیازی توشه کامنت"ناتکوین کی پول میشه؟ هیچوقت" میبینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79782" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79781">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خب فعلا اوضاع ارومه بریم خواب خدا را به شماوند بزرگ میسپارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79781" target="_blank">📅 01:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اماده باش صدرصدی یگان های پدافندی بیکینی باتوم و کویر یهودا برای مقابله با حملات سپاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79780" target="_blank">📅 01:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79779">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/715683a4c7.mp4?token=Huh1zZEkwZLPhVYyQFJdYczFLB63DiMIaqiOxRFOunghiTk3AHOhWk_uDyvOrnRhEFzWc9UNSL17V92pwnoLZrO1PVDHX44PhzxWUSAj5PwoeLC3UprLt9cTyHl58Vqv_YhxGxDmpjL0fuMllASHffmQcj_Nefcr25gNHflGd3mBmmL67fQJAXPKUEMmN0uPKfP-mdoT3KED7IQGNIyElcGGAEYHtdIQ55SrhJDQmlfCcj5HOPSwjTycxfSCKHyMel4NdvIALPFKSxbYXk3E0qvTzCQt7HKxVIamcPNkneKSfj6IBp0VjJEv37VEf-zgr-8j8bcOt5tShu6B0ePAhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/715683a4c7.mp4?token=Huh1zZEkwZLPhVYyQFJdYczFLB63DiMIaqiOxRFOunghiTk3AHOhWk_uDyvOrnRhEFzWc9UNSL17V92pwnoLZrO1PVDHX44PhzxWUSAj5PwoeLC3UprLt9cTyHl58Vqv_YhxGxDmpjL0fuMllASHffmQcj_Nefcr25gNHflGd3mBmmL67fQJAXPKUEMmN0uPKfP-mdoT3KED7IQGNIyElcGGAEYHtdIQ55SrhJDQmlfCcj5HOPSwjTycxfSCKHyMel4NdvIALPFKSxbYXk3E0qvTzCQt7HKxVIamcPNkneKSfj6IBp0VjJEv37VEf-zgr-8j8bcOt5tShu6B0ePAhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79779" target="_blank">📅 01:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79778">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یکی از تابوتا رو تو عراق دزدیدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79778" target="_blank">📅 01:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79777">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">محمد سامتینگ کارو جم کرد
ترامپ در مورد ایران: اگر این اتفاق دوباره تکرار شود، عواقب آن بسیار وخیم‌تر خواهد بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79777" target="_blank">📅 01:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79776">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">به من ربطی نداره ولی این تلافیا چشم در برابر چشم نیست، داره کیرشو میکنه تو چشو چالمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79776" target="_blank">📅 01:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تبپ 110 سلمان فارسی سپاهو تو زاهدان زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79775" target="_blank">📅 01:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ بین این همه عکس، یه عکس فیک از عملیات امشبو ریپلای کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79774" target="_blank">📅 01:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رسانه های هر دو طرف خبر از یک ترور هدفمند میدهند، خبرنگار اعزامی فان هیپ هاپ به جنوب می‌گوید هدف ترور چرسی بوده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79773" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تاکنون ۱۵۰ الا ۲۰۰ حمله از جانب سنتکام به جنوب ایران انجام شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79772" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کسکشا اروم تر بزنید همشو نمیتونم پوشش بدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79771" target="_blank">📅 01:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79769">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">چغادک بندر لنگه کیش زاهدان زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79769" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79768">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسانه های هر دو طرف خبر از یک ترور هدفمند میدهند، خبرنگار اعزامی فان هیپ هاپ به جنوب می‌گوید هدف ترور چرسی بوده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79768" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79767">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جاسک هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79767" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79766">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ابوموسی رو هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79766" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79765">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=RkfvmmRewQpGiTgvIe_-9uUPRsthKeepR_CBTVTOhfiHJrTDj0QnpppcgOiNKXMVRMKKRZ_s94K4bYlsOEBU1rHLBb3pwr9QHaD0SOwfrVgEYPMDKF4yXA2qZ3UQpMjqkbY2zCR13h9ZrqkgdvNBa5p9_nD3syx88hQR3dVtmvRgmymRtPtF1PehUgsuIHgUz6Mbf2AVN-5eXSus-z608GAKtUhWP9nWc-JK9StwVuwyHRa8HAdRxpKkY6rkvpIv5XutGd387PmyspLSFrPOih13SIc2K6Ztr2UjBa0BMnN6ut9oZj0Rz4eAEj4VzI3PmSCX2PXjjzXl7OvzYiXx8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=RkfvmmRewQpGiTgvIe_-9uUPRsthKeepR_CBTVTOhfiHJrTDj0QnpppcgOiNKXMVRMKKRZ_s94K4bYlsOEBU1rHLBb3pwr9QHaD0SOwfrVgEYPMDKF4yXA2qZ3UQpMjqkbY2zCR13h9ZrqkgdvNBa5p9_nD3syx88hQR3dVtmvRgmymRtPtF1PehUgsuIHgUz6Mbf2AVN-5eXSus-z608GAKtUhWP9nWc-JK9StwVuwyHRa8HAdRxpKkY6rkvpIv5XutGd387PmyspLSFrPOih13SIc2K6Ztr2UjBa0BMnN6ut9oZj0Rz4eAEj4VzI3PmSCX2PXjjzXl7OvzYiXx8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چابهار
صدا انفجارو رو داشته باش فقط
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79765" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79763">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvnQUCXNFYmgVhUH5_540lhY-g815SdsLGLsnoSmYVIhHJ6vhkvxsYwgaeRYIYMv8lz6jXMIJxeod2rW9B9peiskEO9FfWjRfWveJwCrtf959AsxIpWbib-_qjVR1KW8qQmcG4t3s2kDC1R9BWM83aRpCBKVecFwW47c6pFMllAX_eWGXCVHtVJqEmZloewRO0XfaT4EIlwqXhvSMRbk5TsfdYVdh4R4c4fJi8uBuZBBurwyGfnV8UwgDbfyEzTbPJhdd-C3OKsA7qlm_SqiOTs85vo14htye9es8xJRfMrK0isB9mUCtD2WyuhxOn6LoUL6qSppz-Zzfp4RpsWwwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه برق چابهار رو زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79763" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79760">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الان هیچکس تو دنیا اندازه دانش آموز و دانشجویی که امتحان داره دوس نداره جنگ شه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79760" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79759">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">از دیشب گسترده تر میزنن
تقریبا کل خط ساحلی جنوبو دارن میکوبن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79759" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79758">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جنوبیا تاماهاک مشکوک دیدید گزارش بدید
113
114
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79758" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79757">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">از صنعت دریایی ایران دیگه کم کم داره یه خاطره میمونه، همشو زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79757" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فرداشب رسیدن تهران محمد سامتینگ حرکت کن</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79756" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79755">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بوشهر زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79755" target="_blank">📅 23:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79754">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سنتکام: کشتی زدن مام زدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79754" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خارگ زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79753" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79752">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پادگان ارتش تو کنارکو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79752" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به پایگاه امام علی در چابهار حمله شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79751" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انقدر گفتن نمیزاریم جنوب لبنانو بزنید جنوب خودمونم گاییدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79750" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پایگاه دریایی سپاه و شناورهای تندرو مورد هدف قرار گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79749" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بسته اول غلاتو انداختن رو سیریک و بندرعباس و لاوان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79748" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79747">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سلام فریب جان بندرعباسم بقیه شو خودت میدونی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79747" target="_blank">📅 23:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50093eebb7.mp4?token=DIoGn60OrPeDaOTYBZjqwe1p5zQBsdKVrYlSWbVFeWtJAlXQEKj8OX6PaKPAwtFhutaK0NoOjasEFQ8dl0CERRWZPJC5SIfnoiVutsEvKdL6Z7cYnuudt8uKW7rkgRXsmG9wmrMTzStpKCrDYdazYw6RJjSfyEj7kU-wwyt-OkfqcWBV-TyD3sPHb0x3oPsMO4Y-Sk_wEvQ3xU4tckSreAofIbdEqj0WVkHs9fRzUAOWHCbvNLY692b97vRnGFuhQzbzkmYgPRsE9abOQ9lM_fJWTff3escgiUZ92NLPore403PFR5Ggd2oS_IOL9kjp0kRndHb5w5ZaA3OpNwBJUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50093eebb7.mp4?token=DIoGn60OrPeDaOTYBZjqwe1p5zQBsdKVrYlSWbVFeWtJAlXQEKj8OX6PaKPAwtFhutaK0NoOjasEFQ8dl0CERRWZPJC5SIfnoiVutsEvKdL6Z7cYnuudt8uKW7rkgRXsmG9wmrMTzStpKCrDYdazYw6RJjSfyEj7kU-wwyt-OkfqcWBV-TyD3sPHb0x3oPsMO4Y-Sk_wEvQ3xU4tckSreAofIbdEqj0WVkHs9fRzUAOWHCbvNLY692b97vRnGFuhQzbzkmYgPRsE9abOQ9lM_fJWTff3escgiUZ92NLPore403PFR5Ggd2oS_IOL9kjp0kRndHb5w5ZaA3OpNwBJUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پرامپت خفن اوردم توش علی گرامی میتونه دو کلمه رپ بخونه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79746" target="_blank">📅 23:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79745">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه پرامپت خفن اوردم توش علی گرامی میتونه دو کلمه رپ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79745" target="_blank">📅 23:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79744">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2efbbf934.mp4?token=ge3fraxFUoytsCE2XWYgJahyyyVsZwlAvnjn9PVP_lpBgLT07Z6RLqDDWcYL5D6wNrWFIyXbQWJkd3dTIYbb_Y0ZfUQXI35Y5ifwg8B_c5nNaJWw20sBqpCS1rNUuvXZdS5iMcQUSqaWQ9TCL0WZ5h-0ZHh7Qr-A0baYdKd7lKdg624lh-qPm8GynnplhyBTiNaFBOVSdgpgxMbUTi-_P382lAjrcVK_uveOSBcj9qTU6rl794_NkzyTcvE6XFT_4L44y3SiEBSdrurAoHUd1U-arLrnhFge-Iw8dmuC9qBpPZf6DjqsAoq64Bxidkf8RVMy_b9hZj4v1QmdtSikTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2efbbf934.mp4?token=ge3fraxFUoytsCE2XWYgJahyyyVsZwlAvnjn9PVP_lpBgLT07Z6RLqDDWcYL5D6wNrWFIyXbQWJkd3dTIYbb_Y0ZfUQXI35Y5ifwg8B_c5nNaJWw20sBqpCS1rNUuvXZdS5iMcQUSqaWQ9TCL0WZ5h-0ZHh7Qr-A0baYdKd7lKdg624lh-qPm8GynnplhyBTiNaFBOVSdgpgxMbUTi-_P382lAjrcVK_uveOSBcj9qTU6rl794_NkzyTcvE6XFT_4L44y3SiEBSdrurAoHUd1U-arLrnhFge-Iw8dmuC9qBpPZf6DjqsAoq64Bxidkf8RVMy_b9hZj4v1QmdtSikTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79744" target="_blank">📅 23:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن، اون اورانیوم‌ها خیلی خیلی پایین‌تره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79743" target="_blank">📅 22:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💥
OFFER OF THE DAY | تخفیف شگفت‌انگیز
💥
کاهش شدید قیمت‌ها به پاس همراهی شما؛ از این لحظه تمام  پلن‌ها با نرخ جدید محاسبه میشن:
💲
تعرفه جدید: فقط گیگی ۷,۰۰۰ تومان  سرورهای پرسرعت اختصاصی  پایداری فوق‌العاده بالا  مناسب اینستاگرام، یوتیوب و هوش مصنوعی و گیم…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79742" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79741">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr82BJf1fSTK5IEgTzkzQVkGxyvEWW-jNuYChiuLX02P7CGTs7KBUNqWOfg14Zg31n08zYrUJQB5G0jWJLIBiUwahmFSUWZmiFnjS69ascAwym8SB1oq_dcaPtC4zmlUnay9Iy7SBqkkLbDelZFqOpLeghBBHXwVf_61IVSNV5bdFxtyA01VFEReBPYpsSORg6dverG-4jjcNQwjELhNUiNfFrgMBibEq5VM8leabIdkYKktpRfh2Oh03pJRUAURXHBfxFasVMXWJUT2YHeMjqZsArmI6GLJ5i4Zt-uazz196eskmZp8w4P-EGpmCH1Ossd5auKECvVSHfQZh9FcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
OFFER OF THE DAY | تخفیف شگفت‌انگیز
💥
کاهش شدید قیمت‌ها به پاس همراهی شما؛ از این لحظه تمام
پلن‌ها با نرخ جدید محاسبه میشن:
💲
تعرفه جدید: فقط گیگی ۷,۰۰۰ تومان
سرورهای پرسرعت اختصاصی
پایداری فوق‌العاده بالا
مناسب اینستاگرام، یوتیوب و هوش مصنوعی و گیم
📥
جهت خرید یا تمدید آنی از طریق آیدی زیر :
🤖
@TURBONET8_VPN</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79741" target="_blank">📅 22:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79740">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ایسین کصکش فقط با شاطری محل ما فیت پولی نداده، فک کنم حق فیتش یه وعده غذاعه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79740" target="_blank">📅 21:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79739">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8E8x5ZzZ8vAEwYU0C-e_1lyiz5f9lNRVqpZQt8ZHqaE8ZSSyaodjP44_2GQoqM-AiJ2JZtbeYwu21B2Ri8oQV7Bkw-fqCEGiXYR-muY0H-evWZWz3tBKiWEPhKf9l74XVGo-kI1MExylZGLv7W8a-q4H0cxZZ607hDxGeSiDTpnA9z_4KBqDywI53nUaCE8XrK7ohjFsxNpzUhvMDpbtPgsWYGVEZEz0YjAVvoO9pmqO-5M6FNuVOPS16ywmIqe3qTgWqXR6wlgsaQ-RBQGeCXfFgk51of8gJWdLNDfB2doOFUqPn9jyvf_9SaO1WTaE8iam96lapAwB1cl4oazZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد امینی ستاره بسکتبال ایران که تو درفت ۲۰۲۶ شرکت کرده بود و تیمی برش نداشته بود بعنوان بازیکن اندرفت به بوستون سلتیکس پیوست   پ‌ن: فعلا رسما به‌ بوستون نرفته، تو سامرلیگ بازی می‌کنه و اگه عملکرد خوبی داشته باش قرارداد رسمی میبندن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79739" target="_blank">📅 21:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79738">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd40tzrZFeRCdrGU6SfIb6U2xSnYcy-tc8ZZ8B9D4tsjoT3suc2bNNfaxnFMiaLkovaWHOuT7MtpHFqGeoCOmv643kWouZ0o3uKnXCVtsUQB3pbV8Ps_vTXT2KXWvdn51HxTnmo4hW0bt9TvDSbZvMBzpHri_WYE0qQR6u-Wp9hw4rexAMOgKJWf8jmJqcSWZ3oMzobdB_6F6kXQG-ljwi_FcDMxwH8hGZO8sF4BM6szeAkmoOK0VhhzgmSfDivazvWvZGr9oeBWWFjKK-FF6NI6urRPWsei_4-ORDsqKKRmugI280TLKro7insYH7s6DxFjIB1PZiLqQINeR6s7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد امینی یکی بهترین استعداد های بسکتبال ایران شاغل تو لیگ فرانسه که شانس درفت شدن به ان بی ای هم داره از تیم ملی خداحافظی کرد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79738" target="_blank">📅 21:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79737">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9PIJF7EYLYPTla7aChA1YBvMTVbQpY3dTCtLH3ibWbSymiE5F7aH2DQAtwt_tdk-I6hv8ozx_X_cpkfQJPW2kwHckQ06HFS71J3GGwSdzn0GbGc8vp1DXHpMUEjjris3ET4asKyjhW88MaUhqTB3ykjDlfQg4ChAn--cVPSjAx00T4SGXJx4NFW0j4wy-_yNKa9KZTZiZ6S1VbAjn2Mpu08l-5wYKxj76OX6K1wjTV55_lL3AjhZx_Oy4lLHEFimY6f0MkiXcHdbDJg7m4o45xnrX9FlySBQyc5GJDSWFa6eDUylvil5DZM-KmL56F9eX5HOpXcCtFlyslT9FWfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد امینی ستاره بسکتبال ایران که تو درفت ۲۰۲۶ شرکت کرده بود و تیمی برش نداشته بود بعنوان بازیکن اندرفت به بوستون سلتیکس پیوست
پ‌ن: فعلا رسما به‌ بوستون نرفته، تو سامرلیگ بازی می‌کنه و اگه عملکرد خوبی داشته باش قرارداد رسمی میبندن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79737" target="_blank">📅 21:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79736">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: جنگ با ایران از سر گرفته نخواهد شد، اما آمریکا به حملات ایران به همان شیوه پاسخ خواهد داد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79736" target="_blank">📅 21:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79735">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603112f466.mp4?token=iLak-V-TKocVYoEZ9hEWc6r7bsbRkHI8NG4WXpDu7X6fLgOaQL0VUm679iz35cJ87nzB6HpLBaApvPqc3X7FwX6w599K8OQINPe2QJBm2SnUAmRGFzpQZf44DTLS9ssKca790iIrSkQCoAZr8yNUGSAXo4TQTawm9lk5erBK1h8MDoAM9pmEIXfcQySTwyefHxsQZ3UltZz0FRuwn5Sq7HTpH1ndRTVIWEPh6zn_F2Xi2BFWrgyhoLkInzfCGX20Rj-gCLjQmFtI5IlRIkkWcYnfkIWk_PNl8hbsbVy4XV6IFToPKHUPT0VyeGmvyW0qrpkskzx6WgIgmSpfxaWEAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603112f466.mp4?token=iLak-V-TKocVYoEZ9hEWc6r7bsbRkHI8NG4WXpDu7X6fLgOaQL0VUm679iz35cJ87nzB6HpLBaApvPqc3X7FwX6w599K8OQINPe2QJBm2SnUAmRGFzpQZf44DTLS9ssKca790iIrSkQCoAZr8yNUGSAXo4TQTawm9lk5erBK1h8MDoAM9pmEIXfcQySTwyefHxsQZ3UltZz0FRuwn5Sq7HTpH1ndRTVIWEPh6zn_F2Xi2BFWrgyhoLkInzfCGX20Rj-gCLjQmFtI5IlRIkkWcYnfkIWk_PNl8hbsbVy4XV6IFToPKHUPT0VyeGmvyW0qrpkskzx6WgIgmSpfxaWEAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفا جان بچه ها تو کامنتا جوابتو میدن من حوصله شو ندارم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79735" target="_blank">📅 20:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79734">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfPOgLfzO7lqAeoQTRypJd9IuL3ay-yPYblPCXloaqKyhh5AieGNxCy2Is6ni1vwqWNb-bwV3rCADmDN1tkmg_bE57CfAawU1ivfdZ96l8or3ISUgqJnNJmLzVyDCg_fTvPF8PIlBxBE8s5Pse3m7EOPnwV_e4WcUMlDRlOw-p6z7bMQahWcIf1H-TT0cs9r2ATFk6_FqEztZ99lL1qu9lJF84mceUEc6dEA4khXk4rKoVJ_9yU_Ced7ij4WDX9VhGM0TYGdRvw3rwvVsat-2QICEjHd4_Pq1rVDfwhtoB2Ggv31CSspq_bK6SUPxLXgtNKfmBMYePvK2lFnebi16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وفا جان بچه ها تو کامنتا جوابتو میدن من حوصله شو ندارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79734" target="_blank">📅 20:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79733">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCH6DFUT4VEZmxcWphkhZDgZkkvYRmFodgBTp1HyzV9P5HdYTSwAWuqONvFSA5gGP1gTZbQxJa3p3c6dDwXJ7ompzf3gRQBqbHV4sNduPXGUl9Ji3bFMah1exA-Q4eErnDQ_Nlr9gvBIoxQIIdYTpBv207qLrbp3b5UYPQ48HWRuf4vqj56HirLNeza8pPIUcnq-LZGpT_w8JWZEWbN_kOnQClCnFLEwU843MGDUYuWm0yu4y1OzByJ1R2vrg1NCxNcUFtuqyIoFYqdH4m0k0njZEIFpBsucTQ0ztMg7dnYsTYkiNDKRQ8VhfDRyKKWdvbdCNvZ0S7KvFN_aMlLEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در استان فارس یک دختر ۱۳ ساله با مراجعه به دادستانی، پدر خود را که اشیای باستانی گران را در خانه پنهان کرده بود لو داد.
پدر این دختر نیز بلافاصله بازداشت و روانه زندان شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79733" target="_blank">📅 19:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79732">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ccec9119.mp4?token=DK_QDY8JXhPjlHp7UsP8gyQROceZWoQwDvyin8HaNKvwZOzdwGh78yLwc4YZbHVO6gbtYb4RBljp6FyrQAXBH1rcmRahAMy8ukeh5Bs7fuTl1nsGYi0SbM5e4707-FpY59ATr4Gl1sKaCYfejor8p1UpX-XO_aV9f1HH6VWKbmeWNXmdR7B_KNqUs4nPKWGT8bQRmi9v0ipXrJRP_EYwtUEgpYxoZN0x907TekG-oEj2anPRBVgNWw1N4j1MO8E7zZtf9JWoqTeOZ-XMNQTrvtj8tMpWgGjghE8Gji5J8S3ZUE9MZk9x9euOZ6WMeK2YVZUp9ABN2lZosQ44uH-sxggGTQX_Q7zlNacecEODzMNggQtkiHNaCon6KIlrqF9jMGuil_NeGL9uWz6A4_9ZhAAU5BtnrUpFy6qIqXnMpn1gW2SnNcDEqF6CaIgVlyIyaTqUDMWWv7SN89yTHKkqrP4qeEw6l9ahzdwJQbjoof3-qpbwnCqwMBtAHcbghMi3AAm-j7efMZSrE97jiRGYsXFzgcfnrn7ryqUeStI5L3zSX45B6wcsXHHJ-qy0C4Vlkv_GwVYnMbj1a0VtZPH3m4I1pjPvrcN-0HVs1LjintuXo_fLiMpD96GEq9B0mT3EWlrOtvHnaSV5lwtUcfZd98x6F6Nmr7jYfr37m7FTo3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ccec9119.mp4?token=DK_QDY8JXhPjlHp7UsP8gyQROceZWoQwDvyin8HaNKvwZOzdwGh78yLwc4YZbHVO6gbtYb4RBljp6FyrQAXBH1rcmRahAMy8ukeh5Bs7fuTl1nsGYi0SbM5e4707-FpY59ATr4Gl1sKaCYfejor8p1UpX-XO_aV9f1HH6VWKbmeWNXmdR7B_KNqUs4nPKWGT8bQRmi9v0ipXrJRP_EYwtUEgpYxoZN0x907TekG-oEj2anPRBVgNWw1N4j1MO8E7zZtf9JWoqTeOZ-XMNQTrvtj8tMpWgGjghE8Gji5J8S3ZUE9MZk9x9euOZ6WMeK2YVZUp9ABN2lZosQ44uH-sxggGTQX_Q7zlNacecEODzMNggQtkiHNaCon6KIlrqF9jMGuil_NeGL9uWz6A4_9ZhAAU5BtnrUpFy6qIqXnMpn1gW2SnNcDEqF6CaIgVlyIyaTqUDMWWv7SN89yTHKkqrP4qeEw6l9ahzdwJQbjoof3-qpbwnCqwMBtAHcbghMi3AAm-j7efMZSrE97jiRGYsXFzgcfnrn7ryqUeStI5L3zSX45B6wcsXHHJ-qy0C4Vlkv_GwVYnMbj1a0VtZPH3m4I1pjPvrcN-0HVs1LjintuXo_fLiMpD96GEq9B0mT3EWlrOtvHnaSV5lwtUcfZd98x6F6Nmr7jYfr37m7FTo3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
کانال گزارشگر زنده بت‌فوروارد
🎤
⏩
جام‌جهانی ۲۰۲۶ را لحظه‌به‌لحظه دنبال کنید.
⚽️
گل‌ها، نتایج، آمار، ترکیب‌ها، لحظات حساس و مهم‌ترین حواشی مسابقات را به‌صورت زنده در «بت‌فوروارد لایو» دنبال کنید.
● پوشش لحظه‌ای تمامی مسابقات توسط تیم بت‌فوروارد
● همراه با جوایز، برنامه‌های ویژه
● سریع‌تر از همه در جریان مهم‌ترین اتفاقات بزرگ‌ترین رویداد فوتبال جهان قرار بگیرید.
👍
برای ورود به کانال گزارشگر کلیک کنید
کلیک کنید BetForward.com
کلیک کنید BetForward.com
🅰
g17
💻
@BetForwardLive</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79732" target="_blank">📅 19:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79731">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54671d6f3b.mp4?token=tOnUiTc9S8jTBLu9UaxTemySj1CbCXhl7yWD7JJi6ZqKH_4eepnUrJp8aSu6Wdsei_nMGb90wubVXVSgb77TLqJVDi_5Ox-wBioZAtsm3RLlTVv5kEyoodQ10-xI_QK-9ZTcvpc_kK_-OxL5o9xkidHgklmmZmdaoExpBpIyI7AtphdU8xlLHDN9ybEjDrPG0Nrzh8Dv6paDbfIUxTF8V1d4aGTYcMRJTmA4dYvsZda9CM3B1of0P5j2HUGwuU7qGWuesO6_gOgsKleDoJjuVHKV_12MAYZPavbbgHl4PPES-jrA_vmz4l4hd73FfYakcaYf3QZmjqrmukvf8GFaKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54671d6f3b.mp4?token=tOnUiTc9S8jTBLu9UaxTemySj1CbCXhl7yWD7JJi6ZqKH_4eepnUrJp8aSu6Wdsei_nMGb90wubVXVSgb77TLqJVDi_5Ox-wBioZAtsm3RLlTVv5kEyoodQ10-xI_QK-9ZTcvpc_kK_-OxL5o9xkidHgklmmZmdaoExpBpIyI7AtphdU8xlLHDN9ybEjDrPG0Nrzh8Dv6paDbfIUxTF8V1d4aGTYcMRJTmA4dYvsZda9CM3B1of0P5j2HUGwuU7qGWuesO6_gOgsKleDoJjuVHKV_12MAYZPavbbgHl4PPES-jrA_vmz4l4hd73FfYakcaYf3QZmjqrmukvf8GFaKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باقر شاه صداسیما رو گرفته فک کنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79731" target="_blank">📅 19:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79730">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طبق بررسی های انجام شده توسط کارشناسان فان هیپ هاپ، درگیری نظامی میان ایران و آمریکا در سطح فعلی به یک جنگ تمام عیار منجر نمیشود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79730" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79729">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبرنگار:
هیچ برنامه‌ای برای اعزام نیروهای زمینی به ایران ندارید؟
ترامپ:
چرا باید الان وارد عمل شوم؟ وقتی آن‌ها کاملاً از بین بروند یا زمانی که توافقی حاصل شود، آن وقت اینکار را خواهم کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79729" target="_blank">📅 18:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79728">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فعلا تحلیل نکنید تا پیشرو شیشه رو بکشه، میاد پیش‌بینی میکنه برامون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79728" target="_blank">📅 18:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79727">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:   محل نگهداری مواد هسته‌ ای ایران را شناسایی کرده‌ ایم؛ این مواد در زیر کوه‌ ها دفن شده‌ اند و ما تجهیزات لازم برای خارج کردن آنها را در اختیار داریم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79727" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79726">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ:
محل نگهداری مواد هسته‌ ای ایران را شناسایی کرده‌ ایم؛ این مواد در زیر کوه‌ ها دفن شده‌ اند و ما تجهیزات لازم برای خارج کردن آنها را در اختیار داریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79726" target="_blank">📅 18:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79725">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">زودتر به این ترامپ تریاک برسونید آروم شه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79725" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79724">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd-ws4Ll5uBBhpJ7CJRdHe3q7jV0z2BCvBGg3ELjxUJSV2O8-2X3dzMpRFsKn6cbPJ1mfBep1mFk3TmypCTQFmD10I78i2TqDROqjpFvLQ1G60Tx0PJbaorG2Sq4h-c6h1ngnxBpG9m1NLuWYtHpEyC61q7b0zxMyiYsrVAoI_UOHr0_f1tKczIN007l_Sd3Fl8f9IgxxMm2OhifnjS3Gy1v4L1CoHdr0rYtHpfJtGOMEXTXiKMn05xIqXOCl_IbAZA4FjfCT3DDFe4VYI8G-kverF5hRWGZDa-OWIibIhWaPv_PNrZgq8iBrBJ2ODh37p8bhYVfyIwOtJuXqub8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه.
آره.
به تو ربطی نداره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79724" target="_blank">📅 17:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79723">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYHkN7OZ-mWVNmacXpTgot80oMajS9zbNEK6OGmauKjpLy3WP1IbZGistNtD0GTxL509hXtbNRAg-b3hl2HGHM31BRQXMyEg8wcAJ7ZKF7hidDO993chkswYFEMLojJOXl0IfqL2N-OH3VzMsJ_nSzO6Pm705QO47W3JEGOxp3u7Esf8phBUpNVtKGatHGYY6ps6iBDFkc1Bt4GssnGOmXaYYFjk9RPFINw9ZUg2kHOIs_MuJdAnhvY752MzERZTdCFnvq4F6p0c8nvGJT5fVqe3-TdQExqQ6lM87L1Q_Qyc0n5ZOO4HUaH3BrYNFHtyX9iy3WHuDyEYwhB5ZpRoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کاگان و آرون به نام "Geek" منتشر شد.
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79723" target="_blank">📅 17:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79722">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ویناک میخواد ترک "بلاد۲" رو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79722" target="_blank">📅 17:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79721">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐦𝐢𝐫</strong></div>
<div class="tg-text">صدف چاق تره
احتمالا مادر صدفه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79721" target="_blank">📅 17:28 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
