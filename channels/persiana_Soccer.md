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
<img src="https://cdn4.telesco.pe/file/Qeii4NzLuQgA_6lBU6I2ZtyLJ2l7QmCL4u86M7YoAzZmMw1veTiWwZ-YJKVcn4ji18kfdCALWBJpat8UZudBHejaNXtfcxcBHvIfPvYMeziRMd0sDEsV324rh7dA0UZHd1xzxfC-1wOvvHipJ_t0GawT46IwhbB4r_8j5DR4mwGbx-saIYaHWWxL_IeaNKd-qjGr4ea0HsJ-roIKKbg3btKQVoNfhbueDMV8__cUtfPZ_c5BJMmL5WngYUwVBvhVyk-gaoHa6fWpStJspbQEukYXS2SIHWZv1NG4exLWnRwbt3dlRhM9Rp3h84oaM8fKOvZk36mVwCmBF9dpyBvmEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 618K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
<hr>

<div class="tg-post" id="msg-28740">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9Hswb_cs0CVj2XJq-v_Qjif5FI25kNKj5PnSqhwFCd2Tco2h_FFdJOk-ABW3DWX8eLwTUYgtic7aNEWUROU9uxoI4FzOpKyzffatrWiNGA3qqamYIRqcSZxz5hYNUgzGhtUIPsVSFfGrHp1kSmlBpjCzOwFWs5xPL1Ns5xX4ygbYPA22mPuqmqNJWu3HEv1lqRhdVuxTjvYAObNbdAtnn6KJpRKmp3SaJ1DkFtmc4Nxs6sMqAvyiyNL7beIfQWtAO64DGt7zlGfYc4oBSgAe6a-CQqVHK84ylGX_qEBxU0tXljsBt0hAKi7_HOKnYpLwhmOOSRWOIcCBuIzuO_DNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه حبیب‌فرعباسی درمسابقه این هفته مقابل پرسپولیس موفق به‌ثبت‌کلین‌شیت شود رکورد وحید طالبلو رو خواهد شکوند و به اولین دروازه بان تاریخ باشگاه استقلال تبدیل میشه که در پنج بازی ابتدایی فصل موفق به ثبت کلین شیت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/28740" target="_blank">📅 17:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28739">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGkPBIcmRpQmQ2S8VlJs7UumaMA8m5mmz_MI0YDZl1DICSTRGwBb6RemJcnwReeGbiCQS82Sq-e0hq-nZHCbA__U6w1MOBKOoq8mMbL9euW17WH_L7ISbR4X1z0tjjp4P2kV0PR0uX2tNjDGIB42p0z62aWO5j_-WXN90Em4ghMM1lGnXCutYBrCXwBMELbhKjqBDHnwtB1xLyWIEFEoKE0g9PsxLcr0bpPbWI5TRixglAQ-V83g7Vgp_b5pMhnU-aYAdqQyc9X-5CUBD738Ws24TfIdegePFQbx9cYWYrP1xTf3mcq0VXNjtBqUY07Y6-yTYCM8jdZqdriavZxcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردحبیب‌فرعباسی‌دروازه 28 ساله استقلال دراین فصل: 4 مسابقه، 4 کلین شیت، 0 گل خورده، 14 سیو در 4 مسابقه، نمره 7.7 از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/28739" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28738">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTi0AxeliMdmRBQyZwCsuLEhYiHCTjxQ4RXGBVF98Iic_1nKkYUCchPxG05Tax2uk_a8bWx3qOUSFLMOSzSPLexCMFXOU-6qhV5T4yEPfsUQe99Wm2MbbiccCtA__qbM6Sl2rEMXRIUFBKGCMp8Omr3hBs3JlDaiTaFm72XQ4pft2mWXEeqeb_zaW8qxF8OYppwM-A-atT7CMuToOSP3C_xhAK8bpXhL8eOaN5e5iCwEU986YB4pktgB8G0GpNomfKu4ingHTuj2JP624p8k8JFq8L-qmWyFSrgxLftsgbXfbQYemZyHo1zXkxRq6JXGcZBhfAp8Vp5icyRjL8RWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/28738" target="_blank">📅 16:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28737">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FduZJIrKNGm7YO_w_RFXDWE4Pf8mpsaiQUCoSKQlNmQ5a3XskAIl_OWCIG9xWab7KzrieLcVtsvKl6fbUPxJokhQf8rSrbCTZr03yAs0NTh7vGoVD3C5fhC-0fozjVrLpw3qQo45F3nQGs9t6twFiuH57vGn3nVYbiRlqCjGfNZ-P_mgPTy2Oyr6iy1YAs8qsj5MJUU2qLPnlYRgXSBRlsZyBgZfpdhWO-jwMkS1W2yoM5dTP4uvIG0CGn5oBnGLBVluiIdyVWyh3CHo0exGMXw7aTk9QNUE9ik362wq8doI7vN0_8-5EAGJ4TpJN8LYY0D8Xi6Bsh7T6aejRZ-jYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#فوری؛ با اعلام فابریزیو رومانو؛ گابریل ژسوس مهاجم 29 ساله آرسنال با عقد قراردادی به بارسا پیوست. آرسنال موافقت خود را اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/28737" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28736">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG7QOVvVFjpf5SecQsDXPuO78rYPAsg9r_cBz38UlDzGQscs5-lowAHgV3oH3VFm2LWupKv0duL212Vd6kg0F5y5zEypYk9UYGE04M1jUWiCBSSSLmMZvVuGS1gMiuiskE7frNgRf1k5J1zSdB9waAtIgKDbIE60VKJFPMSoBxo_fnpjm_adTxQNt6Un6EiZzKRDuf_86SsCODsTJ7XwqpjT7y5Ac02YyQYHnYnsGLLc4UUURrjhYTs8ANcPasG5NzJuDMfn3z36i0PsIxev8aHAaq5IQ6DiOph7Zlec_or-gfUsSvldtQ1RhqxHvbheN7aglYl5U9IqxJr8LMeM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی: بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/28736" target="_blank">📅 16:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28735">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMlEWNOa_oLXKceQEb4LF00qHjF3_Aq3LX2qnZJiP_zY_S6eJM1M1yZ2xiicJgxNDGs-_qmWsiMRIbtvyVr_eW-iIWxUC3fCD9m4BTxHFhA6gLw8_j_PrVWkYDLY679EHVmYgbB6RHX9sJaz1cFEtOY-LQAeJUworLDqo1ul84fQI3E_3Ka8J5ixTy5g2QczSaUKKDu5LQU4QGHiewajWIyV5KC8nTie4Wuzf5HYbUDyqqAOuFpblQ8CCpa1Tki6P_b7q9jZncxsLfRTRZGsbyIa9eBRt2sHQ66dprHqAsJzxr7alo_EQZGH-q-oQCfykeZ1sm_sDjjfp8WlaWoW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی:
بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/28735" target="_blank">📅 15:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28734">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6lJgw8hdSFYszg_Lp2iJG2twJV6ugXrtrYqvXvPA_OTDssk7ijH2uB1gQkb3i75atdR20diDpfhZGjyVCaN24G9f9AjAE7FLLyV5QtYuearo8qBvqEcGnfFYzbur4WLWgEbmTqtBmO-w4gTmrpFgTHkpdftEwFu5UWv6oI7UNG6v36gxGD7BKhO0qZ4gB9stF5mZ6y0vy4eMYWG4sdD_U4DD0QpPZpYu802I_x_VR4mUec-wDr066VZkH29lx66cjl3RgNUkNt801_ABdg1nzO1UyIQQVl-cyWEEuJl4f4b4TrQkfYrp_VvIm_hPjkbCU_ABDhDpCqLLyWlYfxP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/28734" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28732">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFXiB_JfoSIZ1VhdHpx6m8ccPBZTft0Tq2jh_pZELOfeLXAFT5k567KPktvsean9EMZixxpE3HGw1cJjVLRRj9QdDxPRo2estOCXg2xTtMoNooDMuzdt3-F3wzvPyAKecgPlBcsEVrmfeq7d3XJPypr6mAL1BoyYtYyl3RLl9Lo5dNEGbM232ZpVMjpTnP6Tddl7CPxCr4rfBSF9nLyFkBVJfAe_z2H7x0tK0VNkJNqwIT7V5h2FZSOCKzkzbOQ5kR131EX9a-k-qfIOR1fHIfBsZQbzaiMOnSJLr0UvO3CpWzDCMTJ-_uuzx_xTLLYEmj2OO-chlh5KK2_DdNzidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdoBImd-nq9M1WNMgG0Tdy0m9fM5CIfC-Fp2hDfGcTgC9XPychqLQEflIaB9t2Eemurbd56kRSoH0BmdCjuL9-gzUSoGUsg0eTvloHiz2t_ibb0Hmo95kcMSE2Bd5Rz2QvI52VJr7wggWpQpxK5jVk_XQ5DiWU-iugLL_kukaASovUjjoiGf7mHJOMqU8P0yb-0GUkHLmVPuP3PStSOX-_mV8gHrvy0iTYHHfcDLUc9h2LqR4OlboZZxfEBGf196nGfBmJZR1wEdy9n5bLgnjyCkgYvd4b9TPtJcquU3YNMd0-KecvMgWJJyzk--ndRbhnvKuvfbKlsqItmTDUDzKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
بانوان هوادار حامی باشگاه ملوان انزلی که در تمام بازی ها برای حمایت به استادیوم میان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/28732" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28731">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgACXTdURjUHk_NFoXk2QJ6E0Wmfj5A4rmpYFofZkpr4PYG4bSf10FLC7QSUUk6O9Gv_a3u4NSDZyRHxwdzRFqbduSgPhIgTWb5TJimlcMZotLvJ_rTLlCWSXojWMTX3De3C6kLJv9VXuskud9xanTCc333CcMJl1rHxWJKCkSs_f1vWlW2Xh6Peb_BOxxIrrLBe-uzcDLh7FNwN5stwe0KiC40b8N1YX8xOMHa3pHyEV2aCLx3b_1vsA-__kRXTfcugaCUVDPbpc87x-FIqHp8ry09TtabPY93t1iXH-QBRK6Xhbk3DIGAhf-23pimEJmqU80ZA2lwSsPShX3CNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌انواع‌کنسول PS5 درایران؛
PS5 PRO که بهمن ماه 40 میلیون بود شده 251 میلیون تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/28731" target="_blank">📅 14:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28730">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWo9ZVzSoSTxmv84y87O6aCVpflz0E3VhmQcNoi8tj3pHLy5XnOXiP_I65NyMu5yzgjXUJJRZZOEGegJNeJAA88vLpk05dJmrdtv9CPp3lIqONJNIqgnSTbqPdHsmNGqj_A_27kLjIO6NYw4bAA8lHz4ssLLQwsUOKAnTbsR-_YzQlq1OEmKIX3kxMexZnBvg1fedMaVTRct1uU6OPMK7qQEUdDlPtYovkJFfU-6iBUot9l2TmZeRrU_b0TmNRomn-pjeR4ey5i61hIUeevaI1IUNRcc35nDxtkWMffeIVv4zMbMQEzNmex5BrpSVfUrFg6YEH0IwJkCG2GiCJeQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/28730" target="_blank">📅 14:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28729">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgbbL7Ky8eNSn9WqZ9m-zTeSuSLMlEpbWcV_lps2tqSTVopKCuDkYBbMdNqTGNOMh-zMmt7dJyVVCpQMWWJtKp11Nr1rg5zLDeGTppnIvpebl0bXJQKD70wpdrMpDgj4_vYw3e1etIByDKo9PaEid_QXmQq_0VgiSTIoFvldeJeoYz4-BQij8cw5dfBE5PyhcIiBPcMSsmmgnXq-p0q8AZdaQx00RvV_r1YZlb7kNROyM8srJE3UA6t1RFDmlSHT4zS1OyWwg8kGlpQCT-fKLdq7cwPyBN57N3uu9CtLAjsmFJTiw76Uq4XLMyyECx38DXgSjwdGpils8SL9sjlbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از همسر عثمان‌دمبله درخصوص پوشش که هرجا میره ماسک میزنه‌پرسیدن برگشته گفته این یه عقیده مذهبیه و دوست‌‌ندارم‌‌چهره زیبایم رو جز عثمان کس دیگه‌ای ببینه. حتی کنار فامیلامون هم ماسک میزنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/28729" target="_blank">📅 13:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28728">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520eadae82.mp4?token=RTYkvIXflAU0ejpJWuiVgKqa0if7HUjr4sZEOYIYvLZ_3V-gmYJ-qCF4Ag0iAsiJLxJ_ei-kBK6dL88VmCVyqSyCexd5lsvZhm8_ZOX3IaXLmgDcwclv1z6wV63TLEoUOzSWfGvAkp6LO7TWmExq-nf7EdS8a-vmvWZjHnxjVmVyaDX2xUBonDBTnABgJBzUvv1GTxN8toJXm-xK9CgPgEzqhgGD1-C55GKEotMpLcNdzgzLltFJIRWtGViKHbqzPGDD_IbEfh9gcy9dfkEmRXbtG3O1x_SE8WrqMndXScm2Uto0bT2aJthrXvohG0fJhGlqn5lCVBKI6UrqpolNXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520eadae82.mp4?token=RTYkvIXflAU0ejpJWuiVgKqa0if7HUjr4sZEOYIYvLZ_3V-gmYJ-qCF4Ag0iAsiJLxJ_ei-kBK6dL88VmCVyqSyCexd5lsvZhm8_ZOX3IaXLmgDcwclv1z6wV63TLEoUOzSWfGvAkp6LO7TWmExq-nf7EdS8a-vmvWZjHnxjVmVyaDX2xUBonDBTnABgJBzUvv1GTxN8toJXm-xK9CgPgEzqhgGD1-C55GKEotMpLcNdzgzLltFJIRWtGViKHbqzPGDD_IbEfh9gcy9dfkEmRXbtG3O1x_SE8WrqMndXScm2Uto0bT2aJthrXvohG0fJhGlqn5lCVBKI6UrqpolNXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعودپزشکیان‌درحضورجبلی‌رئیس صداوسیما:
دیگر تلویزیون نگاه نمیکنم وقتی من این نگاه را پیدا می‌کنم. ببین مردم چه نگاهی پیدا می‌کنند. هروقت تلویزیون رو میبینم اعصابم خورد می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/28728" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCeuw6WNCvS6xfOVjAvy6rGNgAgcoOmLsZsF9nAfm-xhqSGu6gNM6D567nGBOiqvhDTo8G1HfDHAOKj7RfsLWcNWyh3qxWsM1LDhe744Sa8EgwjEQrhsAM_yeud_iINV-qHxzpdZ27TLgcD48o5j0XNVuxNEi60fYYkgxnjVWWm0tDFjgadTF2yUmNASjABxbXv0HDR4RP5wqcvrcbjnsy0Bk75brihFut1rtlI9GIYmiV1FPl-oiSRk9npOJ7PgpAdZEnYLOl96WpbffLLunj67Qfum9F-7vIf_IflI1gRxzuWN9kMqwc4lrfaNCbBrN8a1XC7Jv6YKKdNSkENPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/28726" target="_blank">📅 13:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📊
تمام گل‌های هفته چهارم رقابت‌های لیگ برتر جام خلیج فارس؛ سیزده‌گل‌زده در 9 مسابقه هفته چهارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/28725" target="_blank">📅 12:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yco4Bbe56wlgqUVMXcJJNimddwFUTjCTNTFKsg8j-GeZZctE7vTrnu-aFdXMTSb3N9sgDg9MoY9oy-jgM3YtXqrT3qgCM2xTxsqzaQ6ymc1DS48GG3QagQfp_0AixA4SufcsWGRENp7sU3yBu36MO6xZ-218uZWYqpXATtzkZ4DSfijwkYeiPo4Yaf0l18RCFio6NbJuV57P23xHEYMSZOJ1bU4FhVrFndRNdsI9YVLgn2hgUFf-y3I6sifz0ZS-iJGlRYRucXddRkFpVP_TdJe4e5CfVDVDbpxYIcjk8ynkVyXaeQ-FAv8XHsrhXVRIVCEXKkl-xZRpwpMdB6uB7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛
کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/28724" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28723">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/28723" target="_blank">📅 12:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqijZWdUvvyrzLPaJtusJu0Vs97lg2jxbCrs14LU8ZqJe6Q1vzN2fU-kdvsc8Ol0-Y-nMGgnveeoXGwiF68MQcAIQlD9TjaSioNJU9YDttjqnTWwDOMLGMYtNO3yNk0Txcnk-MYMjIJFD4No_tkdQZJmqxiyDbcqqA3vYkX9gay8EyxPdLgLPFNLmb_TPjNSd9ribELQWtKz6VR56W5AKIbk9EKt6rdrAfQOCAqfU0wFH5TIUrolddILOywzZELhq8vW9fJJagQ_LBKVNtoLc8wZMrs8yUB3DCXvqe-b1ulB14NCNCysmkYSbmGuzmL_Ct2BkId1OCoYTb6W5yjlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
ویدیویی زیبا از پوکر تماشایی لیونل مسی فوق ستاره آرژانتینی اینترمیامی در سن 39 سالگی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/28722" target="_blank">📅 11:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFDUezmpVWoihhV5OiO4MDvKnS72PyqepGFE9Qlylgz4i9amw5DhwNNLQOFeE50CRXZDtn3h2z_85xBjmgAbI3gvP3yUwDAsUE1AceJf9fRnlTBuKbM4KDJmLT0_kbWC89N0FK2LzX-IeI40d38MKfd8rwKlhC_SsZBZhQBkgc9Tjnu8aPBIOnnbPHgnNCP-1iS2kKWepNFhdN0U9MpYR4wD-eH4QUWnJ6oUYFsyWEX7Ss1Amel4ORKfteTqDdJxvr3Qv-vPA0wNx8nq1ir8QLYQtNFByVvNZfurWjoG4ytv5078sHyUZx_gmWIFNM_uIY6gXGKfXB8hky6UkVkzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعداز جذب دنی ولبک و جردن هندرسون؛ چلسی به درخواست ژابی آلونسو امیلیانو مارتینز دروازه بان 33 ساله آرژانتینی تیم آستون ویلا رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/28721" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuXUW19fsMZhTCJfMUr273D1PWe-ypibC8UBbmLT4D5YR7ot8lCJwAk_8pRmPdQSXJ3ScvgiiY4eQdG-PxLUf0OVak74G3Hm_2dezFa0KHk-GvyWXeTSzm4PdCnSAOKlI6dZCVESVPx85TZgd7hpSgWsews_wRVNScMV3cm6m30oPIbeNSVL0TeevWhkezXRBQ7W4B0isQDqBrzbuSssp2udExi1EMvCCZ-2cs8nx7epoSFDX5YOqs_wNxfN62nx_rYY1G9XcPrsT3O9MWAc9AS91dclX8mwqf4Lf9Y-lD6QYep_OGNW0TUIFGoLHnJxv8Xf0mr14UWVQYOKLYK98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
منیر الحدادی ستاره سابق استقلال: هیچوقت دوست نداشتم از تیم استقلال جدا بشم اما شرایط طوریکه مامیخواستیم پیش نرفت.‌ از تمام مدیریت باشگاه و هواداران که این مدت به من و خانواده ام لطف داشتن تشکرم میکنم. امیدوارم در اینده نزدیک باردیگر به جمع شما برگردم. تا…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/28720" target="_blank">📅 11:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf9l4GDihPQLov8HWsMspsA8PKGTDaLcyfNNr_zgH3xeL89zic5ITOJrTTv0Cf6_8cmOAlcBg7ru7HEq7zmjH_YI8LOpiVjWrR-cgYSFi9yASsFBeBJIiexVEqujSztDYO1vSpRUf5vf3BJ-xH2X_pqdEHbe5nzpaR0H9w4sAvs76XIch7W_JW9L5XGcVj_T1UsF2kNlJVIge0IVX2WnT8W00lkZGk0ohnLtLudCK2cRE2cnaPZggwui7-Fug2d0NZDW7S2HF2-Qu6adDlw7TD8ZwIrrk4r6wxpegUel1JroeLL8hzRhw9JWw6RPcy6IZPamUnyRdelXxbwSvmEsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/28719" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28718">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/28718" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28717">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/28717" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28716">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alur9_zxePdlVigvg28sPz4Y8uGHtyCIOR69TzQfV9ctMEBGnfxv0bixXyDKNl1gpYps0FedSlPVpxnt3TudAD-IHA9YDdQtIH9twh_7TOd7ZI1T-E-iRqqk40H5D4shSpJXq_1uO0mBaIFr4Cq_T1VymDg3rdj4_-JymmAagLWPSdz0AnIwn4QingwsKQnkmtolYN7fUwF7k8KGbZgeqKg_tb6suN3qZ7r1i-BXTKCyE-l9-CYyhfJBaQeOJIA3E-d5a-j-2klCrDHcpH5eAn0s0kLIDam_neGoyIsa4auP48QAF9atxHKtkXeF96BLmzQT7J75gt2urkvyqJffzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شایدبعضیا یادشون‌نیاد ولی کریستال پالاس یه بازیکن داشت به نام کریستین بنتکه تو اولین بازیش مقابل لیورپول دو گل زد . بعد دوباره در جام حذفی مقابلشون بازی کرد و دوگل بهشون زد، دوماه بعد تو لیگ مقابل‌لیورپول بازی‌کرد و بازم دوگل زد‌. لیورپول ازش خوششون اومد و خریدنش یک فصل بازی کرد عملکرد خوبی نداشت فروختنش به پالاس به محض اینکه برابر لیورپول بازی‌کردمجدد دو گل بهشون زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/28716" target="_blank">📅 10:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28715">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/28715" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28714">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUUNqNXSQ5JuERReuj269FjoLmznXwFcUnaOFj56LcW8OEtMDRdlRUGFmqbVNdOqNyxFOJVhSS-Fv-h84X_5ebAnvjbvbKlJBVqKnsBJIIk_VC7vcJ37caOrqRYji5NYzJvXJTuXlsjBrGM15MScrj_2e-4FVTYBwklHXtAPUDWaY2AF-XLQIqIzuGMnQyYI_u1AflL1tHthF8k1CY1CkxY42Ovjtvz2Jj2euaAnwtWqeJwS60PepvXvY0ca7TzK4LniAxCAudCnfAWrpT9nSVUlDNdhsd1mXPVoazz5_p1icABLUlUR-aK5U13RIpw2ir8zE2z3gSQCBkY969fGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28714" target="_blank">📅 08:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28713">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28713" target="_blank">📅 08:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28712">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFEd9JZNugjNz0N3SwCjEkxoyso8SLYSHXAyRxygAsTNixgcLUgtJP_fuaHFUSsYqeQpZTt_M6vdKrWVaoOrWCWEF2UZ13usWhbu7IjXA9LFe7gf6XXw_vQzB8-PVLXbPLhEUTOq3Xy1v3FMwS9iweURNYFB2tgMVtBtkDFHc1p3t2x3OtqVelKg10qT-4EZNUujaeOp2cMVL8YjdQvRNmsJRV2y3h9Losr36OXnqljHZKqKLcWaGydAs9JYB30va2FXdYUYX5pIa6qLCZHchveGz1gZxWysxiVVXJ0qrwQJEo5YAAqvyN20gIY1rbcvBJ24HMvdDZceyMP-c1FYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اسپورت: دو تیم اینترمیلان و بارسا در حال مذاکره هستند تا برسر معاوضه فدریکو دیمارکو و الخاندرو بالده در روزهای پایانی نقل و انتقالات به توافق نهایی برسند و این جابجایی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28712" target="_blank">📅 01:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28710">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1-St23F9VOy-7mVh6G94EmqPM1xDNn7df4K05dXN025ZpaHz7eToYV4j-HeKkEvlkBQjYT5RokyGCQAxJbKo1LEjM1llXXrLQVvlsjxO6IVHB0fSL4y1lMH7xazsrGJx1VZpJKnttj-q6LEButYLuxsf2Xa2cy6ebI5_2Aa66HABh_EOVtib-5mH_6wmxI-BCYYpW6EmvxX5OJKtKpdJZaeszdNyQX-M3yLCRb-UrDLq41HnjuU25Z01ZVeVcd2Z2aJteKLBFAB0wXG9WUzrvt5XXOiIahFvV-1jqpkwfV-OuXij5u_sp16GZQ9q4jrc2epfvOwB7U5ieh4gM6KzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ نبرد رئالی ها با تیم سابق ایسکو و مصاف شاگردان کریک برابر ایپسویچ‌تاون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28710" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28709">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db6agi1DZEaE8C77NxGbj9veI4v6tNJmQ14nNlw2srkLXTo0W5175CVZbg4_AeKGJCt1210JCUxhRtRkCGytPVxNAAoGlebRYJlnwlL73R9dqBsWuRHlY76yZR0-4cJP6SVNOz0g8X6pjH7GLmF8siQlXzo5dyWyH8DA4ceXi94xx_e8GPwT0ulpbPOKPjk-ltR420qsZ2L4WyI-FGoVuYFS1h5L3Nc9hy7XYQbDQUsoLg-DUgQrkuZUIufVhQ1W5DzGZjP9zLqS709LgCzIiolV1v041qJTufGUjknHvZ2ya_6A4g2AB-T4u72-UrH0VT56m9R2BGirXgjIQizOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
برتری قاطع پرسپولیس و استارت فاجعه‌بار شاگردان دی‌زربی در پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28709" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIkWrNflDC0GaGUq9xsWxNlw85XDFfnZEku9xMPzMUv6X5Re8vkDhmotA1wQOUtrOW73ba22RNp0z-qFGZLdw76P5bqu1lZPdqYIrGS3nBqo4EuNGRf4APiprUIE4HAhYuuhVe7IPa6IudfU9AJo2ReZbELtteKN3lk8KN2MXF9UP5RLgbaRjQ_jiyXByc5ITercFpQUbZ9EUwVRwUa8mi_Noa3HnMBKxQJtf2zrs3-fdSbd4oNuBnWAFSdy5tL0oGdz76ydQEZoznnw_nZLlEiwhkGQiyEnIvAnS0jLpj1mxj0m0ocH9dst55kq9ky_99zB50Nizm1RutSVkCi8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍁
پاییزِ زیبا، پاییز خوش آب و هوا، پاییزِ دلپذیر و جذاب‌از رگ‌گردن‌به‌شما نزدیک تره. این گرمای لعنتی بره که برنگرده. با قطعی برق دهنمون سرویس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28707" target="_blank">📅 00:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28705">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB181qWp2CjPvSBJ_H1Hh2TNIJOVOyMjEJ0NioYLIKfWmBUoVtCi0eHOgSAkbLToH5LHOapWH8CY9FRUUUN380za0Bf7ostCLRD5PGDQ7Qc7W57xMgAyv0f0j8-pROVHrHQakm4-ETBiOXOmCQfJjwptx5BehiAZw0D-amZb9wZdoqa23Zh5vqWslaIuG9sYtBfK7Zs7uEz7NByX3evkZUQdRpcz7c8oYS9MtZX1M6t50aVffDlFQg8Lz8slYs3pEi4EpsJbZkWTJX3oS-anwE7SkcqcG2wpLPGykX2fIMzxLSNLEBVPbdxqPnq60dNozwCexY6Gpu8LQH7FStl6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنهایی‌دیداردوتیم‌پرسپولیس
🆚
ملوان از نگاه متریکا؛ ثبت‌امیدگل خارق العاه 4.02 و انتخاب علی علیپور بعنوان بهترین بازیکن این مسابقه یک طرفه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28705" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28704">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liJMFsIZRmvlUKBUiEaYQ8Ilwf3Dvu1StNotuvvyUKQzRiZFnPEMjmNBiHlY3K_8nDv6fw8hIx7a8XFA6mnvML_UZsqS9-bX7SwAOU8NNwxs3D-hMbfVqjliiG2WOqEisGVGe3HMJx-DiLQzqv2Sg5lNubpJeazjymUvERqtYa6P1Z2bAJ9fF-Ke8ariwXoPokCzZQHD7N3mGbxXULWDan6uxKnSJSCXb2jTq0PItKIe6TqlaiHM7NVOs5STxI2xS7chJmdH6UFBAHi65fDT85A5NehfvN_gv3-o0Io8NVURKRVP_T8xTmS3M0XJ9XksdI5Z-mDGpuijarQnq9uHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه«Novi list»کرواسی‌گزارش‌داد که محمد محبی برای‌انجام‌کارهای‌نهایی‌لازم در راستای پیوستن به‌تیم فوتبال رییکا وارد شهر رییکای کرواسی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/28704" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28703">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfGTHQy_RjYQx6OUUAYKGGjeNq4gJoWhuno-65OG1dxE3_QbjGm3caS1MUQW16IoC-nvdbjfMNBo2pBPJmjRMDWMzd9QDvMC-lO3qkFnuikmm_QOuq3rowwT87szbgrJCwdxH6wzU4P20sYLC7vdGKRRBpkgDsGRN5vBw-HTFy9g0xVm-xdshgVEr3ve1JjNN0Vk21UqoD0kDzWMqufP4ldTXnBIKRt4r2Bo50-JfDirGSeTTDAmxDkYVyQSAD32UhGkOch2h6pumyd5cq57Nyb6Q7j29ypooadcwrIs2Tll7iC5ZMNt4LYpz2q_9_g2hWFXBsBC6wnu6iDAF7HuCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/persiana_Soccer/28703" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28702">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKh1KTmdAHl_Zgy2Sclzuepzvmz05Csl0ey2zAHSYgrteKtow1Ifl9jED9lZG-fkdbEummFslaGaBTIey686mZDzgALEhD2qFo1qPQtSfBYjFqR_zvyvsLR8a0EHqguQfCNJyr8o-7Wc9SpnoJic-BWK3nIUwWncA0hYbVeSdTPS1UYJgoqTMhefKzTLrmz7hhgOgtRhzAhtbBeuOJYXuVpq44z2JE6rHM7X-V4Z54S8neCnYvSc0fDBTteveAIGLGmPfEmf9nLP10sTICeRyjP4aiRliQoZNx_caCEktdQLwcpPs5YMFnOaTfE38_R97Rk1dOwQkufW6lkjq6bUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/persiana_Soccer/28702" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28701">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWp-ggi9t631RnlDWn0VBd1bRwOcZxnMyE8_EtzdYmNG1Be1iUaaN_F1vteD-gwnO7Ym0a3MHm0GB88SqqGjQaCGHNYbCTwmeRN0ORZSY_wj8lvIsrL5gfeRJegizcAT3T6VLrf7nHsCMAn-ONCiM8o31vIs6qGD2AeBWod4l-EW6OrZbE5c4MLH150Uzh_AfGMzTYriYORly_x-tev8Hh7eQgz0QpeHnVZ519rW7qerVR1oV3Xh2WVxt2we3ZYGKHkZAT09bIWvYUfKPoLbd3VfH4fsvqnNX1PryyTdcGoeOerGjdMWm4zEmNj1OwIumXFbqJKA6IXwRkHs5SrlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام جرارد رومرو؛ الخاندرو بالده مدافع چپ اسپانیایی بارسلونا تصمیم نهایی خود را برای جدایی از بارسا گرفته و بزودی از این تیم جدا میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/persiana_Soccer/28701" target="_blank">📅 23:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28700">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fj69TPfend7aVKuMqUIHcL4pqgT07ac_7zNYz7P1qoOfCEi38w3V6mmF7Dq11blkQD6ecCjGUTvX-Vbt2xvhs763PAWGIgz2fDEn4HSnqy_eFbxnQwjBxVwPWhMCOzGYm4gnQSEe9kyL9hMUrEUL17bN84jL36z-ZApkM3fWgNPH7RcSDbrerjktztVpknIex1ShPQjZo1R_vgrNwDT1bI1rCnMjdg5ObNIXSVpupYk8OlwmOlsdc4Nv1NKDVp6TWOC4lLGKmIDzw23Ze-L_12dclxDljPhOtjPCHPWxokIZHaxM5h8Jm1c3ZobZa9AoYQmeKeU_0XoQkF__2rHqZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/28700" target="_blank">📅 23:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS_2zcD_Y6-iUNces0q1sapotO8fk4Go0EtPZyNya51KWJvrRzNdIf5m0LRlGDcDRIWIgl4U8B03oCLQf2pRL5cL9Vh4UoV9KVBSFZ_x9NTIJxIUDPdNRv6cQUN3wLtTXZgaTK4TugsT-maBmcEavHaNsD5ifACmNpLlCVdBESM4tB3JQP_0IFntubipAJi4iS8a_dOZqbKF7zkO5EO7P_5joJRf5imIGp6UYPYZhoq7tc-ZZTHqSkX9TDZFQQtVYoGXm7Jev95ay_-MTRoI9LCikROPOgtpvyYQNpElsJ-uHjdxWrsI4mRdQWkBr-eYwGt45Ag2gV2VclD0AmdQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28698" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=I3h3D0mco4LJ2aj5yusvv2xpA1KXy3RnpnyFxG4_Z6OrVTlbXgJiYAQAGnvLohqdFS-yialg8uG3C9_AymwJAYk9DUQ0YI41p6ZMBC5AF1LdtSM-QqprVOzAAwfYNSYTH3KOBEWB4ZYmkKDSZHTWTl_Xd134H-ByZFc9mSTPyL3r80wMxkKuhXZS0GuT6n3BgBlvOTpMwjqBffWOlkQUEPSmwasTJ2Ocekpyfw1RRU9BizdlXPmB_ghBhC3GhZ9hAv9McSE3xep5noNZStfnWgfz2pafyqfDfs3Nlaj7tCjOs0VbEiMpeMLrrbJAfdenYgqofrkvvWkpJyoIrLjwLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=I3h3D0mco4LJ2aj5yusvv2xpA1KXy3RnpnyFxG4_Z6OrVTlbXgJiYAQAGnvLohqdFS-yialg8uG3C9_AymwJAYk9DUQ0YI41p6ZMBC5AF1LdtSM-QqprVOzAAwfYNSYTH3KOBEWB4ZYmkKDSZHTWTl_Xd134H-ByZFc9mSTPyL3r80wMxkKuhXZS0GuT6n3BgBlvOTpMwjqBffWOlkQUEPSmwasTJ2Ocekpyfw1RRU9BizdlXPmB_ghBhC3GhZ9hAv9McSE3xep5noNZStfnWgfz2pafyqfDfs3Nlaj7tCjOs0VbEiMpeMLrrbJAfdenYgqofrkvvWkpJyoIrLjwLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28697" target="_blank">📅 23:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28696">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCcrklYym_XJXZ-FvQsQ4cb7Tlpk_a_qIRpA-K4k7MSUxmdFeRwqFcjgbffWDWgb9t0xyvUGNtSjsdVkVbhMlYdXucqmnTU6AP2QIgYl3fFbGOtxvBDVLYYNlqJ96C0rZqoIQtAsDzbN9n_OQoGcgNcXT2locDlgEWEGAScbur5ZAhTaOsJhL1mVanf54pSNcp3KE5ud3v2_AzXD7DW4Hj51_X_pDIe_xIP8oDHUCw7dcaEum1X4cgWddudfvWk-mOIVL0v2rN2nN-Zow0D-Vd8QxbUQhE8-Ig9zTpjf09wC3Y81tcXt3V3IbBAu3KLnFs9RElO0l4UbexXC2XQO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری
؛دیویداورنشتاین:
کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28696" target="_blank">📅 22:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28695">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUeBIxsxEa5hThLQdUlTjuLa7uDvzrbNoG6MPdMBKpCbuvHYx11Gog5AnihDUKcVJJxprKZ-LIEb-UozVjcbN5B_OW3gyxVQlfxE2kQ9UKT0t4yVASacm3gFUu8SyjG1pKfMH5R2NYJhSIsw4ahXVjCUvmZEAcHTREkDRS5GHClbXxEruWWnM1dsYXvhzmeKCvVcyZOUMTlh1SK1OYEYd2ylCrSRtlEyORF_wenY6VPnHlM-5gW1QJ5wRGjYcyEfPbGgtx_t2VQfy3-_D3Itxd2WNiLHiYGXDG9J_elCUaqENCWEwn6iWPJ76QQfpuy3SsWRz3oyZxpPWJJWwdhpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های محبی قصدداره بعد از بردن حسین‌نژاد به‌پرتغال، محمدمحبی هم به پرتغال ببره و نیم فصل با رقم سنگینی به ایران برگردونه. فعلاسر انتقال حسین نژاد به ریو آوه 250 هزار دلار به‌جیب زده قطعا سر انتقال‌محبی‌هم 300 به جیب میزنه بعد نیم فصل‌ 1…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28695" target="_blank">📅 22:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=ppscQbgmka1Jip6VrBqqblZhMnP3cgIYCOTa5Q6j8hWvgX-lH51FosMwNFkNAeWejB4s5ZueMujInQyKPTt1WXZN6_bT52QBQKjb9FMNI9tMaxcTB_xs248N1_qwt1XXa72-S5_nDYgiKxGGioixEsjwtnbkXi-h4S6qmre60YhZ6JXLN4QQ7xxy0OvyRVd07aVqEINJLETd0t3qDw4vhZe9Z_-Hz9EVAGrSi1xfc91N2nXx25zRa315TIARhih9xpOr7WFTjneKm-gKUnQhOmgE9018lclD6wz26iI67svXArN32jlzYC0QHWKXIRmHGPbkvf09gnxQV1VKEMmkvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=ppscQbgmka1Jip6VrBqqblZhMnP3cgIYCOTa5Q6j8hWvgX-lH51FosMwNFkNAeWejB4s5ZueMujInQyKPTt1WXZN6_bT52QBQKjb9FMNI9tMaxcTB_xs248N1_qwt1XXa72-S5_nDYgiKxGGioixEsjwtnbkXi-h4S6qmre60YhZ6JXLN4QQ7xxy0OvyRVd07aVqEINJLETd0t3qDw4vhZe9Z_-Hz9EVAGrSi1xfc91N2nXx25zRa315TIARhih9xpOr7WFTjneKm-gKUnQhOmgE9018lclD6wz26iI67svXArN32jlzYC0QHWKXIRmHGPbkvf09gnxQV1VKEMmkvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28694" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28693">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e895367e.mp4?token=RqpackpP1vThGLsy59tr8RmP-6nShI5cL7fAju2p5MX5SHf3znOlfGrvI8HD-xjZyq3R5VCEI57YIQyJ1J2ESsQW6mf1HcNnXC4g0rVZqmjRkfo-gS80QBW_I-1p6WQBzhmFz2fEFzqUfctiYl4WoU4m6GvOvWNCHuIqpD2csqiXHiqjB5JrrtWid_zzVC-4dV-YUKHvnZc2HJjGfUwd0UO7XYWfoZQbkvniwaIu-fLAP0IQWbMy4ANSK1Jwo7GYy8WIE9NZzTOUVhovX3fQ-aAdizHqwK4QeqiNWasL7EjxFyPDD7ah7Ky8MUK0lm5sRnwu-XXNhVUsJbsprwshEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e895367e.mp4?token=RqpackpP1vThGLsy59tr8RmP-6nShI5cL7fAju2p5MX5SHf3znOlfGrvI8HD-xjZyq3R5VCEI57YIQyJ1J2ESsQW6mf1HcNnXC4g0rVZqmjRkfo-gS80QBW_I-1p6WQBzhmFz2fEFzqUfctiYl4WoU4m6GvOvWNCHuIqpD2csqiXHiqjB5JrrtWid_zzVC-4dV-YUKHvnZc2HJjGfUwd0UO7XYWfoZQbkvniwaIu-fLAP0IQWbMy4ANSK1Jwo7GYy8WIE9NZzTOUVhovX3fQ-aAdizHqwK4QeqiNWasL7EjxFyPDD7ah7Ky8MUK0lm5sRnwu-XXNhVUsJbsprwshEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تاریخ سازی دختران ایران برای اولین با قرار گرفتن در بین چهار تیم برتر آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/28693" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWzCoBiDK86JmbHDJQq9dSp5rUxftKVnyrWVzpxYfythKqcufkXT_aHPg-_in-O2qZ5Hr0y1QQgc018TIuzC_2MUgixldnBIF7ELuLo-OGEBX8QoHgZUUYatDtlfoKE60dlKTmZ28yzSQ-ZMnJ2iiqPCRlm1YuDR78lG6dh50E7vAf_Dx66swrdds0oaqgLDDnJxaAm4d5BdfwFzJExlDlp38pr5BGHSBLkquA5Sz95e0HAYDfGtxEqxx5RMyCDGC9PDbraTsMuiolXnY0vnUwSvoRNz_ov3csE6dcnFH3i70N3irRcELkfCdywbyU6bii7fn_9vBYhki-fj-kPtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌دونستی‌امکان پرداخت قسطی می‌تونه تصمیم خرید رو برای مشتری راحت‌تر کنه؟
با درگاه‌امن اسنپ‌پی،
حتی بدون داشتن سایت
هم می‌تونی پرداخت ۴ قسطه رو به فروشگاهت اضافه کنی. این‌جوری علاوه بر اعتمادسازی، خرید رو برای مشتری‌هات ساده‌تر می‌کنی و فروش و درآمدت بالاتر میره. برای اطلاعات بیشتر و شروع همکاری با اسنپ‌پی، روی لینک زیر بزن
👇🏻
https://l.snpy.ir/hw5zl
https://l.snpy.ir/hw5zl
https://l.snpy.ir/hw5zl</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28692" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=ArJ_P4CXc7k4Me5TlAYjQd3rS-isD-ogzhG1H3FMny0s7AIBdO7pPITUu2lW7X6JYur3qBVYSPEDVgnUGbT7zV7J_V57vhRBGS-tAycdW5Vsw04WwJK1KGoVIyt7kMjc-yJ-_suVCX0xshSbjqKffz-GtbqFmqZhiCTjwss_NOOXqxkEzDdDBOyOj5wpI6Lf_9ve7-boOUo62DjFXnQ9N-ckNelgZihHBT5kFYjBpTkM1rZLmxxZneMveCqvRXyD1Gc7ObvSd3OYtEJYPIKOnAnOxUFZEVr81KqFLONMVzAQd3LjECryzFMyhKVHtLsSxQdeMFJM6Ng2fhXNsa2cyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=ArJ_P4CXc7k4Me5TlAYjQd3rS-isD-ogzhG1H3FMny0s7AIBdO7pPITUu2lW7X6JYur3qBVYSPEDVgnUGbT7zV7J_V57vhRBGS-tAycdW5Vsw04WwJK1KGoVIyt7kMjc-yJ-_suVCX0xshSbjqKffz-GtbqFmqZhiCTjwss_NOOXqxkEzDdDBOyOj5wpI6Lf_9ve7-boOUo62DjFXnQ9N-ckNelgZihHBT5kFYjBpTkM1rZLmxxZneMveCqvRXyD1Gc7ObvSd3OYtEJYPIKOnAnOxUFZEVr81KqFLONMVzAQd3LjECryzFMyhKVHtLsSxQdeMFJM6Ng2fhXNsa2cyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
👤
مازیار زارع سرمربی‌جوان‌تیم‌ملوان با تریلی از روی برنامه فوتبال برتر ممد میثاقی رد شد و گفت تا دوربین خودتون رو از سالن بیرون نبرید، مصاحبه نمی‌کنم. دوست ندارم تصویر من رو پخش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28691" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9nCRpggNbuL-wqvQ7zQ1c1bVyyFSSoTfvb9BK5CGJGvMGr_IEsgm6V0yA9mfyPqLfftaeN_fd7lKVmlwTiU2NHFLX50284aaOoZU1YG_RW6NJLPdQ6tLo4bc64iFy08XmWb2I3O1qpEAlTDbDOInoVFDwUegHRRiLa_dQkj8KGiYlCX1rsFWffkRMv9kVUVgzjnZkE35mKHzgAAtH0ywPXorFumn6fhUJsqWWYeeSUI3TrvlJjxQwXo--6SVi5Hm9vx3eRwTgoA1CHEL5AWL6rlvog_9soSr8agDO3OEY9fub7iIv-LPYXhyQpsi0hO9bPfAksgx8TEORbqbZmrjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28690" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgcWDKzDf2TZq_zhD2MaRSG4jQJi2f_RUTbhGnvuWxCcJhYDlLpFz4KzjdzBrK5BKYhySsWjEc3Z1OIqSgvMwt-uns2ifGhRNpAfZdMBqQDYAICjz2wEcgP0tlyymSVjCQ1ODNonPaXKjrN2jjhlJtny6OzFLrAtBG9g3OtR5DOT7ROygfkq7OK6hlnc3X0RRl0e2ATovE31avT_pNNYm7zMojvvYTU70Im89octeYwBWph-ke4yqOmZfsYr9Uhzl5607BfoZVfqPa3xQ8UyIfnJsAHcH1n4P0nl959XLI1p4dHlWtxRFQQhd9cP8uh-DD1irJ7Zlkar4C3m50dlAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌ونتایج‌کامل‌‌بازی‌های هفته چهارم لیگ برتر؛ تراکتور با جواد نکونام همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28689" target="_blank">📅 21:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28687">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CW2RzCML7Qt5yaS09fFL-r8aJJGXwXSArUMa1q3P4ESMWrNwHs9TI2a2uVEYy7eK4lIJ-25YRD-hLkf4I4PZ7bKEpCJ1ENzs3aC9fNJAAeajUQg9UE4jzpyi9LSfCajqY-NdGD0uboxiDI-gh8GZyd3BwvYUSVl2kao54lcLIXIq53PnGVdzdn70D3ns1v_ckSIEl0j70d4OvwF2RNHhJ3MCvW4OsIGUnb7wPLrZGKCR1_bwCcVcf6lRzonfG1BRDIGpAMMmfJzDvwuMqc19YeNxUEkqdvqD9NeRKgY3geCQ-XEV70eIfXGH5BlI6BOxN-B08IBl9C2RbPZ9skgTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgd_Iy2IZI8k2cwuvFgPmb6azIzw5ftpeLl7HlWdtnvXTDIBq7ViNnNA2B6g9aj_AQaeTCzd7HJHxXgYVOFgjltKepuWT9TcRqOh3xJMEIurkbgcTrdPBS-lTFOzl9TWb7uW_1fIc6NXBI3SH-NFdH2mSRgbCn9XcjZ0P9sVa4aTO3ijpn3AJ7IwQrnsqWa9rV4xwHM1wHYhjtrFWiTmvcmHibzFV_Xj5Qa6rxePLkX87R5Lb4fH1OZDjJegj47Wu8_mkqzZf_HTgEb91pl8UVWWe7xfXvhSLVyi14RQkQCNRS0zo-cB4Gb4_8xZIvx0LUCYojMTHImuJCsIWjP1pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28687" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28686">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9kLpZku_HrfwhuSqWBZtMC2IJA_9MxU43b8bYrBZV-BWoHSmO0Dk1CzHtsRnAtROrNYcfFNjpTaaVG3jDzkDhIna0vE7DoPVzYTZdnK43ELy1_jmbI4ITBQEOpkcuJhVQ2QsUUhkj_fYRzQjDePI5Zq-zKA7GdKiemA9SBsRsP88vuvhm6WAbO4wNq1EgSI7BxFwLh6faXVedrAx8kYuFf4NrDAmHsuLlo-fFb87v9rhlFdRTgnvq5boFeKC2YAa8gR_9DjrQVr2zLKC7MUfHSAdpCdurdujkRCBq89e6c7v2GBsn3gQ5OqNTqOx9eoPFrgYGCHUtJQgUN1P2tlJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28686" target="_blank">📅 21:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28685">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho6GUIwZqSQ0VJcuHlBQ5qiTuOsRLhzO0aOvTTSFSRyy4o2IKGIFj0f-XXWYhxLzzfLhTdxskfFcjToqbPytCcBvjbEjzqIr0MYAQs0IFbxQUdbjs4IQ_tDk0Nk7qTfLMOwh1AiyoYYqvyrw_DoBNv49npQwY5tCnaaBdsEKo3yeiI-EBbxgVhyKGwQe_Dd37iYR9COGGgzdETjzZl7evvpK8L2sx-WVqzoxeFy-e40u72VmaBYANMscmHyRwmMIxXRHyopaokGTq-nQk-WgDLOMO8V9Pe8Tk5ktXJ31vzviRdcNx7hkADBGXTDIdhtmbOVK1-XsTXdEno9AKWAkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آتش‌بازی‌سرخ‌ها روسوتی‌های عجیب انزالی‌چی‌ها؛ گل سوم پرسپولیس به ملوان توسط علی علیپور '56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28685" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28684">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=HQxi7tI3hhenIrwbsgkERTbUrwb8HKQRD-HiWtg4M3cRRfEHTwc4WKJNKxVayeiZURJDMzZLCNzl0Inh7cBfGstKCiVFgAiJ0Ye7iarn-Nv9MlJXRrTnaAKvqp3cqW3ng9m-PwVACiRDOexSSNveG3b5Q-0bJY9psgGVtGXWTcz0uoD8bx5JYtqtiIlBmEMIZMbvQcSgvYGQqLLHgMdtdHJRSlheEFKsdewjBPsQdpW6zFK6u-SLi1J-4c6wIBdeoT9ryeC2NezIAFsGAkcWxPW4tvcuu_6fQOnfJw2gxmxn6t7RESSF6CyJQMllIoyD8ZuSIKSmpEM9mYl7FECGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=HQxi7tI3hhenIrwbsgkERTbUrwb8HKQRD-HiWtg4M3cRRfEHTwc4WKJNKxVayeiZURJDMzZLCNzl0Inh7cBfGstKCiVFgAiJ0Ye7iarn-Nv9MlJXRrTnaAKvqp3cqW3ng9m-PwVACiRDOexSSNveG3b5Q-0bJY9psgGVtGXWTcz0uoD8bx5JYtqtiIlBmEMIZMbvQcSgvYGQqLLHgMdtdHJRSlheEFKsdewjBPsQdpW6zFK6u-SLi1J-4c6wIBdeoT9ryeC2NezIAFsGAkcWxPW4tvcuu_6fQOnfJw2gxmxn6t7RESSF6CyJQMllIoyD8ZuSIKSmpEM9mYl7FECGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28684" target="_blank">📅 21:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28683">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=eix_CWr98hQdvLlxbnb6U4OfLQ_014jQrOpWivONqX1IdIiPwTcMgqyjTUa6d9egHBFHcph0V8Crn9yTdd9PifXrlJeLh2sXfeXdyT79fzcSy7uV-0wV0NjzMIaOIR1AWHhauSDCCBP8kEt2lHnJPZSQB4S7yGyt26bAsVQZOdkAVPwjgIH66gHnRy3cl38u2O7IXARzXUZFOBRfbVKNeLYAwZd08CA_oJySgjlhMdeEm8MzmkC11xhgMadlcsT8erRnh1ye3H7f8p5XBsRJuOkDkcGZF2PSBk0IhAx6d_Fksw3CSTPvnVOCYMG1cf7Ok1xEIMkFcdjhXRzrKcjmVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=eix_CWr98hQdvLlxbnb6U4OfLQ_014jQrOpWivONqX1IdIiPwTcMgqyjTUa6d9egHBFHcph0V8Crn9yTdd9PifXrlJeLh2sXfeXdyT79fzcSy7uV-0wV0NjzMIaOIR1AWHhauSDCCBP8kEt2lHnJPZSQB4S7yGyt26bAsVQZOdkAVPwjgIH66gHnRy3cl38u2O7IXARzXUZFOBRfbVKNeLYAwZd08CA_oJySgjlhMdeEm8MzmkC11xhgMadlcsT8erRnh1ye3H7f8p5XBsRJuOkDkcGZF2PSBk0IhAx6d_Fksw3CSTPvnVOCYMG1cf7Ok1xEIMkFcdjhXRzrKcjmVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28683" target="_blank">📅 20:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28682">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=F19CFuW_L5b0VsWFOqq_IBpaZz0itNY_XHZyFXuiwECUUKrK772Bj5ZN_mKMNfCJ6LM_FofQhR-v7a5HdGTnDpbrP7UZdhiv954-vTfy5J1EvDc5jhzoKSh7EIawLICIZ8P4FQFHiBdF6EMC-MinnCaknaSHh1BjIVV1VhyXDkykJthUOToeSW1b670rhNAIyrRjwzP3Y4RueaW-rrDik40Ovrxya7UoLZ-MoWxSavKR8N8XNykCEtk7_O9afkeRo8Uqt8gSuVOwWl45oPLCloiQBdsR4t68uo3IfdLhKDOnjuMBLO9ixld1iOH33nBKJhDRIjD8xneHlhrnHFQT2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=F19CFuW_L5b0VsWFOqq_IBpaZz0itNY_XHZyFXuiwECUUKrK772Bj5ZN_mKMNfCJ6LM_FofQhR-v7a5HdGTnDpbrP7UZdhiv954-vTfy5J1EvDc5jhzoKSh7EIawLICIZ8P4FQFHiBdF6EMC-MinnCaknaSHh1BjIVV1VhyXDkykJthUOToeSW1b670rhNAIyrRjwzP3Y4RueaW-rrDik40Ovrxya7UoLZ-MoWxSavKR8N8XNykCEtk7_O9afkeRo8Uqt8gSuVOwWl45oPLCloiQBdsR4t68uo3IfdLhKDOnjuMBLO9ixld1iOH33nBKJhDRIjD8xneHlhrnHFQT2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریس رونالدو کاپیتان النصر پس از برد دیشب النصر، پسر سامو کاستا را هم در شادی اش شریک کرد؛ قاب زیبایی که حسابی‌مورد توجه‌قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28682" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28681">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl5-Sxe-wFCzmGDeCQSz2_0Jj-mbwTpzo54OXTYyPnZ-wvYuHz-p4pNZnJQgksG0khWCamTaUnkPMNM312nd9NCUj6GgiQvx93SwZF_JWHFSeAOlW9n4R8TKpTus3bvBkiR5u8ki5WrmbI-uZcr-Y1QT2VxlSzE5JHkzTatx7jTEDvSjBwFH8z4ji-FcJEJ8BSTGqlW9z2W_Sj8hiuoferHBbQ-yUTRvS7HI9QJUJkgWe-KOJXP2VuCYWxsbk3foUvBo4thPknvWxOQtOOUhT0W3auPEXunHmUOSQjgVrs2bAJohon2SMArWfN-7C0Glaj7iL1ZQbs95Y6j7JOGlaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28681" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28679">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEZ-kWHD2GWaw0w92rVbG_JJGKS4BjiayVeMZBG6_U3iK8e7d1ybZm4TcaH5hZwHL99nE7HEdrggeb25zHpZyUlsardgxEzFPKZxVk0UezRymUOO9YjSF0aoNJidN-d81-T-1E2QVlgv7IBM7xLsjyr9X3RsnCVUP7JX1-krYvsUz1ylt20kdV1Utc3SodQcWR7KEfXFA4kMLatr40bMEVOGx41gpBEixTGfm2vNrOondCATVnLWN2cJ5g2kWWStpK0PM_wMouwN64UlCWjNiHZzC1WHdVEl8xmHAwVvoGkRMtPCUq7_N972g8I0zU_ASyLgOyRDX-f32r6Qf9SE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28679" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28678">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28678" target="_blank">📅 20:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28677">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIY0i43QRKtuvMhJzho3xdtkwoARoryDdJgaAcysUZE7dLKJVrO8cOPJ_gszMVHF6SP5cozMWqTyfqaDI7xZhlqLRbyc5Tp-RchXllf8irLMaUfuJifRaV4IdKVqVK9G9XEo5K5W4oKbeA9FqAh9ZlCA7QFI6yeIuBBopxoGlGRR44lip0iG4uSRXFELPPh2a_K4pQUkopoSIV-cPKFciTimbecPB07pX1eFZTb8v4peGqkcF42EGQcxB_eVahFr13EqFaORAZ9RWh4F11Wpkek_O3dTHKlGS7is8HS2EI3-2LgbvS7NXuEcrMiWwFRGhKOSnWt-VAoYNGIJpPZtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر
؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28677" target="_blank">📅 18:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28676">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=HWfZu5yqSDsKpJRNDf9JreZAi2PPPGJDrZ2akA3pOW_NR1yuy1PUN4iIGSMWkEQdgYNAbpEUkjf6AEDzDFHEO3sPEkzB_EVNMu1MvI1AL3XHirJz3oGNKUgQHSr34Xafzh0JlW0zJLsNh2FszEn-bqeGtzGPdVqzNKCVbYCw2Bfinsl_L3qABHfGdESD1--VhPZ9n2H1JZYZGrCxqZaI51gvGop2MkCndcr_AvIxaTu8yu5PzgVEmCv7VYzgVTqxR78tHxdIx_BRVO8ir87h1PebSK1atVHsqipBJLtUwUYL5q6TvetBfzV0SThl-r43rNTQqFF61HvOPHxtyNa7vg1ga7NdYHPoEi6PBWSwR511gbsncspSLevJmhOZT_k3lG58Tm57PSHKgYrxynkS5eWC-4hfHvknKYnr-p22NyQXi_Qlxbqu3jZYsNtZynVrgaOrM8Vk5h8zWVKdieO7Ha0iHzy5sByZkVMi-dFDiTdg9zhmVLZudka-jkZ6qeokUQMcZ7C7hvwqwLNMz4HBtfY-CGGhWOT9HyrYkv4rep8tQwH6jQnW-ql6nukMo377En79F9fhu1Pi2gxUbu9HoEOt698lszyggC0Y7CCG0zhIIU-uEGdxo179cQWf8KGJ4ng0QOuRL-hahlTnUH0mXkM1jLdg-nA9keC6hcqQSyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=HWfZu5yqSDsKpJRNDf9JreZAi2PPPGJDrZ2akA3pOW_NR1yuy1PUN4iIGSMWkEQdgYNAbpEUkjf6AEDzDFHEO3sPEkzB_EVNMu1MvI1AL3XHirJz3oGNKUgQHSr34Xafzh0JlW0zJLsNh2FszEn-bqeGtzGPdVqzNKCVbYCw2Bfinsl_L3qABHfGdESD1--VhPZ9n2H1JZYZGrCxqZaI51gvGop2MkCndcr_AvIxaTu8yu5PzgVEmCv7VYzgVTqxR78tHxdIx_BRVO8ir87h1PebSK1atVHsqipBJLtUwUYL5q6TvetBfzV0SThl-r43rNTQqFF61HvOPHxtyNa7vg1ga7NdYHPoEi6PBWSwR511gbsncspSLevJmhOZT_k3lG58Tm57PSHKgYrxynkS5eWC-4hfHvknKYnr-p22NyQXi_Qlxbqu3jZYsNtZynVrgaOrM8Vk5h8zWVKdieO7Ha0iHzy5sByZkVMi-dFDiTdg9zhmVLZudka-jkZ6qeokUQMcZ7C7hvwqwLNMz4HBtfY-CGGhWOT9HyrYkv4rep8tQwH6jQnW-ql6nukMo377En79F9fhu1Pi2gxUbu9HoEOt698lszyggC0Y7CCG0zhIIU-uEGdxo179cQWf8KGJ4ng0QOuRL-hahlTnUH0mXkM1jLdg-nA9keC6hcqQSyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجای‌مانده‌از دیدار روز گذشته فولاد و استقلال؛ دوئل علیرضاکوشکی و رامین رضاییان درکنار زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28676" target="_blank">📅 18:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28675">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKRmTndWp2NYiW8kl_FUDwoKKg9vheaG950v62tOikZUkaMME_pxhWJF7PlzWXB2G3tKa-lkhyaWmI-2RCy4jC5ilpDvBm6ns_ek_JPRiMl5RJdbzM9CEbeQrTxT_CCkw1ja80pryd08jntjJGlUZhHswXj1A-BIgg4RCjGplSMHTRw57gIZkVl5bY7giNPKjuRHAelHyFFJUyAChGmoin94GE1Y4vR26qMQA0uOK78H9aLISMx3BGfneFsbXmOsMHdkexcrkjFKs005EVH4QCT3x9igTS68-O0C4wFw2vpYqBXQhOg8zh7wfpKsbc2a9XTg_kYtNjc4UbnE4YC-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28675" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28674">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=eM4k0NyvwGDLZHvzLsXMhpe4inVm-twhtX2E1dy6YxYOmqTHv4g6SyIWBAOLSlEA4jT6tbBjj3VUL0aB8_SjQffpQacwx6_cZWqmDP7bIEEph7I7--cP9vZ7TZxEoJm2S54CZ1UlFm8VQZeU_QErh8W3mJRBUaOTrgJ-XgI6yRB4IQIauLYpl1n3fawGL5pePgW7v6LnIjxbuGrWex522Ole83M3bdYG1A8kzsCDRscp7K7iboPADefD3FLr_wJaIrg_eZowl-MGtwEtZweqAGLKq3J9UMPQIxYw7SU6jA1tkSml1UqOzxYiHBbbK6iyLrL81PhwVH82b01WjMkNEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=eM4k0NyvwGDLZHvzLsXMhpe4inVm-twhtX2E1dy6YxYOmqTHv4g6SyIWBAOLSlEA4jT6tbBjj3VUL0aB8_SjQffpQacwx6_cZWqmDP7bIEEph7I7--cP9vZ7TZxEoJm2S54CZ1UlFm8VQZeU_QErh8W3mJRBUaOTrgJ-XgI6yRB4IQIauLYpl1n3fawGL5pePgW7v6LnIjxbuGrWex522Ole83M3bdYG1A8kzsCDRscp7K7iboPADefD3FLr_wJaIrg_eZowl-MGtwEtZweqAGLKq3J9UMPQIxYw7SU6jA1tkSml1UqOzxYiHBbbK6iyLrL81PhwVH82b01WjMkNEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
صحبت‌‌های‌خوزه‌مورینیو سرمربی جدید تیم رئال مادرید درخصوص جایزه ارزشمند توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28674" target="_blank">📅 17:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28673">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf-dxlDPIDNUBfkGbFJyW4K2Jpmv_n-aR5OGrprZmGn_Z-Si9jfNNA7OuUd3djVQ-2WTHWVTM2Cwq52ovJq-dLeOEfOjlJKugen2J5sIhFGpriIYv-7ffOdFXEuUkYn8PcXKrdBtDiTJmQW0SOfe1KyaIw8x0pXOwE8-Dh2raBJ0YKcC2aoj3GLZFDcJXH_Ntxs6knkqMe7z6ieblHotPDULrCwM7280TEmIcvfTA4kEEhWOfEP-Nf3GfuNtYOQiZhieeeZW8CqOdutYfdC57iCD4skORhhGADwmfgMQB8ucdnjx7gslrNkSAl4p7M_RJEKrPimxy9KYBVAQia9KdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به احتمال فراوان تیم پرسپولیس در بازی مهم امشب مقابل  ملوان با این ترکیب به میدان خواهد رفت،ستاره ازبک دور از ترکیب فیکس سرخ ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28673" target="_blank">📅 16:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28672">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=uVkeBKMcM-iQWi7iyXx0aE7mWFcqRM65rbVqdi1LauOkd2CX1n3VX14MjD5ALBj9MHse5f0PjGBqmzNrohsIDSHKxeCSoXXfOksL0nbutWgyXCGnlPJ76DWZlOEKfqBnWlcHUGwnjDSLrHtAnzHUr_mPf1EjvzLX5dnwvCqy8u-tgKaNyNk8K9C9u6WTKcvG_H2LaqZ-SPGvcQRVio5XBfKHqlEhPOQXHsKNYQY3fFlpsbYIWdfQkE2yZH9SeaSHZ4Dc7J2RiiAzJuEVnDTU1kt6PdovYHai69JfGUdbTsyHh4una9lLtjhx1QbE2auv7r2jHIWz4QwRjWb-UAhE6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=uVkeBKMcM-iQWi7iyXx0aE7mWFcqRM65rbVqdi1LauOkd2CX1n3VX14MjD5ALBj9MHse5f0PjGBqmzNrohsIDSHKxeCSoXXfOksL0nbutWgyXCGnlPJ76DWZlOEKfqBnWlcHUGwnjDSLrHtAnzHUr_mPf1EjvzLX5dnwvCqy8u-tgKaNyNk8K9C9u6WTKcvG_H2LaqZ-SPGvcQRVio5XBfKHqlEhPOQXHsKNYQY3fFlpsbYIWdfQkE2yZH9SeaSHZ4Dc7J2RiiAzJuEVnDTU1kt6PdovYHai69JfGUdbTsyHh4una9lLtjhx1QbE2auv7r2jHIWz4QwRjWb-UAhE6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇵🇹
باشگاه گالاتاسرای با پیشنهادی 50 میلیون یورویی درآستانه به‌خدمت‌گرفتن رافائل لیائو ستاره پرتغالی‌آث‌میلانه. لیائو ازمنچستریونایتد و الهلال نیز آفر مالی بالایی دریافت کرده بود اما به طرز عجیبی تصمیم گرفت راهی سوپرلیگ ترکیه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28672" target="_blank">📅 16:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28671">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml8zBZsC8P7b1zPiEXEtixY3SOUDDO0cXwLzYXJWSCFh7LEb1S0HzL2lRnrtG-evi7rEKntmJ6UVScmsvnjaXN1x8bGtKJjylNYQIdvxeFqRMNBEZsOOHueVPfmU_KM3lxhVpHv1HmPwdq2Ahc5QKaUFswvbdPd3L7CJFhujahLGFRVHrAvC7olyf2QeZ-1sVPrjoQ5JSIIlX-e-gsc_EKtSdADqKop5X-iGGvNH70Lbk7rcCJaXv-02WxJBZ7ZiUWie6ap2BUZN2XlajoPIFCqt756Tf2VvUKQg-k0vYZGmn2H-DVfcYEKpZ_YxTqAnYHZnUq3U3oYfUgU0OXvy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28671" target="_blank">📅 15:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28670">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e418389c.mp4?token=pK6v661-AwvJUI7HqYapB1PL4pHRQdC0CY1SZNsET5QFHv8azcfR1Rdd_SkTl7My_qEO767-_45r2KXyKZtZGh1AIZf0gmLpJ3rYrl67uC1eMSmPGMANY3oHLEotkznR2rdSdJM8PTDsVfd3fJZb78SsSSVW4eHWsvhxJBgjcBSG9m_-yoZQ41dJh2IC1Y5NeWWvQmSL8rrS6oGYknGnosAVLm0cZ-hMs6gY26KGidalDYscGpjN-sYRDRFIWWmxu0TFOql-FSKWAjBM5jk84jy8O7qt-sYgfkEjGEuXSpJny5GMpjuDTfiW-thVxNPSBHpO0ToLk710lnN5u6RJIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e418389c.mp4?token=pK6v661-AwvJUI7HqYapB1PL4pHRQdC0CY1SZNsET5QFHv8azcfR1Rdd_SkTl7My_qEO767-_45r2KXyKZtZGh1AIZf0gmLpJ3rYrl67uC1eMSmPGMANY3oHLEotkznR2rdSdJM8PTDsVfd3fJZb78SsSSVW4eHWsvhxJBgjcBSG9m_-yoZQ41dJh2IC1Y5NeWWvQmSL8rrS6oGYknGnosAVLm0cZ-hMs6gY26KGidalDYscGpjN-sYRDRFIWWmxu0TFOql-FSKWAjBM5jk84jy8O7qt-sYgfkEjGEuXSpJny5GMpjuDTfiW-thVxNPSBHpO0ToLk710lnN5u6RJIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالدو بعداینکه‌دیشب‌گل978دوران حرفه ایش رو زد یادش رفت خوشحالی گل معروفش رو انجام بده که مانه میاد یادش میندازه اونم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28670" target="_blank">📅 14:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28668">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMVz8XWxVZahalEYOthxFVOeWxFSRF-r8pgor-49Hmg7mGZjZnFTkNUUV-G0_BhOdqa2iwWU4kubN_Jij2m1Xl-PGIqTjCZmKLAJhptX70Mz-u6qBqvyB4gFNvD4ZfHCczgN-BaIvYfOmX2Eo_WiT8rAo_vTn0SSGmbRnbzRirM79iNHBHjPluOmPMyXQzifAkdtLCxKmOnVZL-cpUp288hOhF5gAoLGiNhPG7DZWGinH0hy_ZfZ4p66AHt75Gg2qnt2W6L27TPiZ6_PgWJXNQnM-kAndLT-qo1zD71ULOH3IAVfxL6Ixxvf1EPQEK168xMf-hsJEczb7sFCr1ODhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThyQ72rhod55RXPJ2CaqWapVhqHhs8HWCP6nd_boEUbQwsJaS1e2q95GmCbU6a0Me7WE-EpDhVNMg2kjLPwbbWeVoyGwl383wZhN4kvjm5DvQl1vpMgfmqaRR69lwwLrZkdMY8JfOyNIMRZtIxWvvYNWYKtHpdQQ16R8SuN4XAO7F76jJOsH6NxbwaXYoNxzSbQCZBlLDO65FkZjBfKREdFP3H1lvFmXzWOGnZKhpNP1NBL-KcddpLP8y54cpjuY_IUA40Xr48ictjBbdte0l_20Z5AbqHyJ0JhGabFoLIDC7Xn7FRtpA4KnlQviMKfDGRacGW063xIn2iCbnZoGiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب دو تیم فولاد و استقلال درهفته چهارم لیگ برتر؛ بازی در حالی بدون گل به پایان رسید که آبی ها امید گل 1.4 ثبت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28668" target="_blank">📅 14:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28667">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFKzLMkvKeEOgq0y8GsmXHe_TQVQsBffz-8DAc0C4Gnug_q0R0uQl_Jjyscy-UnHr6ac3iwKijUIQveyFUHHWZdyLcC0cqmxEYll-kb5GaRcUrdwyVtpmb_SnUclQ6FbqOEref7N-_xOMUsndaanDZkWCAK761YzmUQOjLHXVfpWrSvqOBF3n_0BUMB7vj4Ho5eM4E90jVWsw4zZ3xPUXyvDupy4yJ10k8RQB-9SyWEJNzf8pyjTO3ICiNaLfetsTcWC4qUUVBZYvuRgUtIGDKzQlRRKhqUQ0khkvRPt6UFKwNDV99EfN6yARcUA31IVdJ8dD29QvaBUTd8fNn7w_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28667" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28666">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=KIEh-r3bH3paJzi5UziQpO5Bt2URDbM3pUY-Vv8vP02nEHolfH1voPspQ85I5aOifDr4WE-BOtyyj7t8qAL-jZPyxEnhFwtG_MVNSRYmhfUev6jQgNHxLm12mjMaotopRnjutMRTRqoEQ3YEi1CInvVghJOjSauTbOOTJUFj6nd-PjUj_clxlZsqiWYFsEf3x0WBEWO6V4Z4_nczoZiwEhglLRUY_yZGBrMSZnIRQE2pHTAUW15gHh53FsPLPJ4mKAYwzu3efdwlZ-qD3ZpogaudNdUxGS4CYKFEaW_FjZ_C1c1fiMT9r6xp33jQPsqfYpjuZZtFfINyeepIyCnuDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=KIEh-r3bH3paJzi5UziQpO5Bt2URDbM3pUY-Vv8vP02nEHolfH1voPspQ85I5aOifDr4WE-BOtyyj7t8qAL-jZPyxEnhFwtG_MVNSRYmhfUev6jQgNHxLm12mjMaotopRnjutMRTRqoEQ3YEi1CInvVghJOjSauTbOOTJUFj6nd-PjUj_clxlZsqiWYFsEf3x0WBEWO6V4Z4_nczoZiwEhglLRUY_yZGBrMSZnIRQE2pHTAUW15gHh53FsPLPJ4mKAYwzu3efdwlZ-qD3ZpogaudNdUxGS4CYKFEaW_FjZ_C1c1fiMT9r6xp33jQPsqfYpjuZZtFfINyeepIyCnuDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28666" target="_blank">📅 13:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28665">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAzWWH0Fs7RazqlwgCHXwJHKBLjO3EVnRzsJLPHASIc6pkMepgfFm7IMPJQaQ6bhxUJa-o3ZgxmS1NKwYA1h4GMij1XJHUmvLAkGRT5PSRfplfmFxXlDzUA2Vg6VX8_JRhNYpy8yaTSKFKz_wBvHCY9TLKbBll_0KH1P7UwXc-occIHj2O8gLniqXK1uARipvEbWYMOo39EkE1o8J_kNRBXX-1xAi1YlVHPRQVt39nyzKtoB329MzARNDzxAMk-NLSn0IMNf_MEFnM3CnmUMS_hH5yTNPFSeOIF14SHicZCKOC8WdAd-rZuLbcyamxHrhckWij07BED6s8u7b3Lnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28665" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28664">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28664" target="_blank">📅 12:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28663">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0nIbpDNkC542vBkdndK_Lu7QE7exvIu3Cns2WlcVHUHqxfkPzu16UoplINteAJtiHvA1u98r-I87_rHZZ_03fTN9ynMIUSsPaN72y12c-pDwIBUyuLp80CNMuJJjwE0C6j4sS6hFhrTSJ7dK0R6aUYF1HGOhGRmBU_CbEQ8VF1BBEeDKoq5S8BXCe-Q5HzaK3o_Qzyu2TJfltB_T9rmXmA1zJ3zF-Xh1epLOxB9ZVjoe27XpeXRSV7cRTtwMycFYp5V1LzT_Pasp62MjUsD08P_hzp0fCxg83nC6kUGYiJngHnX1JGFvZPkZHWfCShNO9W-vsGIENCUPBKfmZHv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28663" target="_blank">📅 12:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28662">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1CSviLyBHTdG-UE4epvxNXXRbguDgWiA477lgnw5EKtozD_wQKtb5C8b7MHcAcA0xvS1bflT8zKIqPNvj5zDe1nrgZBwCso1LygbYW_9INmHVKV8AjLepqu3ribn8aeWn3zUe415g6wMK4Lj39TVrl5QXCnvIxjN_Gve-eeHBM6BiUTloICaCKigCLE73zWZ3fBqctLyiffeJd7j1U3zl6OhUp7jSL_w3DmymSnnA7ymIrj1DjTjoxjpgRHMB2a7Q5NMDK_PzludYugBvxdohBMcD0SSZuMNop82XVjPIB2jaNPZ2VTVXUJh-db713ID6SlJ9EeMBN7PpafbGavEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ شماره 9 الوصل به مهدی طارمی مهاجم جدیداین‌تیم رسید؛ طبق اخبار دریافتی رسانه پرشیانا مدیریت‌پرسپولیس بعد از اینکه متوجه شدند که طارمی دراروپا نمیمونه قصد داشتن برای جذب او مذاکره کنند که مهدی تارتار اعلام کرده بود که سن او بالاست و فعلا نیازی به…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28662" target="_blank">📅 12:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28661">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu08xBg6R46DJhLgp70wP1XQ2KFS2jp-Tc7cJ79kLbw8Spyi6iqAL1pevudErq3norTmDZn0q-acUF80EVadg2xLGNUSxpclcBcuoADhn3NxBEmwQF_QWNoIgK8Ah4pb_0E-JzleeeEFm15QesF7x-Ht9z5mThWXB-XTv-9dW-b7-zB_xWs5zPKVwVN9OVsG0Aw_1zWO8hDrrOXcq5RK_jFGv0N6VUNFSQcbu5jklTlP086gsdSHEppe7yiwf6KBDpZ5AT5aWA5iOkzEiFCMDaVd_B3daIDXdqKJrFeXEp6M4fnB_gAU9O8FvlssylHybKwox44yL5hrIp7MrbjzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28661" target="_blank">📅 11:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28660">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSU7vL8x7XHdujGgDzCV_m76W9O7-TS_j4Q-jPosvZnrdFQZSFEjATXrLfL58B-GXmg4KXJ7pZzrBmYJUmxDtehhkz4U7DS2ZZBx6zoAa63mI5BcM1X1fnq9wBQzVyPg1lEIT3EM2pDbQXk1-Pi3BAPgUzU97lUS6eRkurCIv5Kx4F0DL22l18nOz6aojzgI-c7aE0JolIf2Mfd_h7YRU5qmeqZVFnvdK_j3Vd8hiC-2RQttr_zSPvpM3LYwPDkOs-R6aa0p1sOJY4q-OpZp7XbMHeolYviu3zyluq_No1_FuwARHkVe7-Sx68iuOoCCKv0ayqZZ70y8biRuNDS3gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهریه دانشگاه آزاد رسما اعلام شد
؛ پزشکی و داروسازی سالانه 137.5 میلیون تومان ناقابل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28660" target="_blank">📅 11:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28658">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSFJ4KIqMrD3n8upNnd7YBifbnZ9_D-SXAHSQFtGYgiQRacFsYptO2DRMnWjjNrW__NhpUU-noSLHiwgkE_mKN0tPwq7jDLiWT4RIduamQpFR-RTt7hYuJx4t2Up2U6-ftk1v0dYE9fLzgYL_Flc146o0octJrbJL6d92dy0Tn0MNHwC9q1IvYdogi74d-nkegTnaEaiLCprZjbQWFrzSM0YbAgxPM8ZSRnIrJhsRk4JYO5fTx06-cJv9V4bYiywfTTZ5MSidWAN83hR29lmxaNw6tfrAikAgmjIzbPSiPGjXQd0AHv8IDc9rHpw5COO9L8uxc43tTWYYI-WD0RqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qu5OaSNW86Im4J9I9qpES6vdPYSZWbWDevA_UiWbIETac2IGNHj5wMZleLycy8zYXHmkWYvbe7gTf2Fk95V15ROQqXyd27TPm9n6o-PGxkmSPbmAHtRSXXkvm8NiZUTVqyPvvocsrBgSd5cPwqPXnEfkavW37-mGTrUxQVZGIxjXKSOJ1RHt9qWA09zsRmMYSMyJwkDxwr7Pu4DZg6YdjUWSzLJ8ZX3O2z_Gcxt3VBDNfTS8uO0WJIWX-NMykpi4XFNrxuhfg6jAC-Og3Fk8wm-y__lG__Ubkvl9gsnUSCZAFxPbjPTSVWtTT1kHj0ezwc87HKypfNj7ktscVweNJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28658" target="_blank">📅 11:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28657">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgjJULC6_V3d88zpkfxVEb2dw9KQ98bjsSqWFLPDgXmQxdhTBjpwNnixE3bhtqhk7Pld8h7QJL6n0Pf8SFcwCOJyTI6kYzYFW3KeyvCq4BzqdkwgSk_KG6fj8M50iDoBgOj85SViGLD9BhEysNo08jyMAbvKsfKGIGfqZHjCqoqqM97AmgTOQzgO4FoFZmobAPWonY9t3H3xXzQkzxI2DeI6mtpNzkeN9vYrcfSNI6A3TKG8tgyLeWUR7v6wiCAqVRB9iFCc9oT5SqJjy74h_a97uiE6bjJDaz736iRtnVlInCNyggM5-TcKTk6Cn3bDw-tEbc3k4ivwcykXAwL4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه گل گهر بابت استفاده باشگاه سپاهان از کسری‌طاهری خریدجدید‌طلایی پوشان شکایت کرد. باشگاه سپاهان هم میگه ما از فیفا استعلام داریم و فیفا گفته که کسری هیچ مشکلی برای بازی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28657" target="_blank">📅 10:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28656">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=oTbqFsqkYERkr8prL23ftziG7eUepNoNNj8-IuhpG__Pf7Q_Du7RSXZkWlSzrOQgc9mhdlrTrHJNBYDL6kfxm5rfBHVGMsggP0LmzdOO2zT0vr2yRSSk-SQZlKFk6KRhLx4sM_PxXzUaACc4iTkXK24VojrWYIXR8IHW3SS6KawpPoh6FrhBw_Z8x05uf2tF53jW-EuQEv0y9shVb_EXqyCr3N_EfgN9DSVWpgE0zd_j09Uss6K_xq4fRS6-n-q46m_Fg-YlVqCzz9g1pA_bnY2Wjut37qSy8qmeVPS-7vxP78DOUwQSTjEc3yfePhontKwaiuaQgUpslMZn5wC10g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=oTbqFsqkYERkr8prL23ftziG7eUepNoNNj8-IuhpG__Pf7Q_Du7RSXZkWlSzrOQgc9mhdlrTrHJNBYDL6kfxm5rfBHVGMsggP0LmzdOO2zT0vr2yRSSk-SQZlKFk6KRhLx4sM_PxXzUaACc4iTkXK24VojrWYIXR8IHW3SS6KawpPoh6FrhBw_Z8x05uf2tF53jW-EuQEv0y9shVb_EXqyCr3N_EfgN9DSVWpgE0zd_j09Uss6K_xq4fRS6-n-q46m_Fg-YlVqCzz9g1pA_bnY2Wjut37qSy8qmeVPS-7vxP78DOUwQSTjEc3yfePhontKwaiuaQgUpslMZn5wC10g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوپرسیوهای‌دیدنی‌حامدلک‌دربازی‌با استقلال؛
تقدیر رامین‌رضاییان از حامدلک در رختکن بعد بازی بااستقلال: حامد نمیبود این‌بازی رو 3-0 میباختیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28656" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28655">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=XhlGvvSleyCj0n4csZ5fM5HKYyoArR6MTJYZPfzutJlJLfz-As6f4p8oIfJ5lP5NC-3wKFhyxVAcMRipN5g6KmhcRTK9DysmUQGBqqrJya6g6GAI8Jg6m0SPapdF1fUu-Rqmf6coz13FCHbcaoQyUqfaHLnO2efB6ZDI4mv-aKZbqf7DETvM4nyxKz7J3RszwFtVFqQq5yqtpxM2DWfR01bTqz0FlqMPN1XuhGYDSla63C9yuFDoSZHZ-2NeEU_J5ZP0TLWqx2ofP8ogzgVPwHH2fqWph5R9xBWtjowoOH5yW7Nkpb4SmMAXIi0WMRT-67toWeQ2Bfxh7i6tWTRcQx0R23XzIvPSNzk3NSD2qOt6jSLf2W_oWN5V0Q5gGWhNeACmboZmsxj7JjeT6XZJqO-1FTiPuNBALrZJJtmGQTM3kKN3LPgbZXcYVg-cgFO-d4tvsp0esJWGGziRUgH3l10caaYy9mZDVoIW5DAeQ9Tyq8ZuAv3owtbzE0PGlsdRjbVmiZfd9Qkr0R4FeXcLI3ku4CwAynplpkcCTi6h_pX_ziKbtwOyHob5WmlO9z-CbPRyT93fL3Pz9Tf-T3yEnPN05x0O7Ak0sJwFd7i0DBrgTPgADG0k9AzmHN8r4i7kx5hS4-C_L37DSNXFTpIAc9oBoZuplbjBS5AerQhrGto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=XhlGvvSleyCj0n4csZ5fM5HKYyoArR6MTJYZPfzutJlJLfz-As6f4p8oIfJ5lP5NC-3wKFhyxVAcMRipN5g6KmhcRTK9DysmUQGBqqrJya6g6GAI8Jg6m0SPapdF1fUu-Rqmf6coz13FCHbcaoQyUqfaHLnO2efB6ZDI4mv-aKZbqf7DETvM4nyxKz7J3RszwFtVFqQq5yqtpxM2DWfR01bTqz0FlqMPN1XuhGYDSla63C9yuFDoSZHZ-2NeEU_J5ZP0TLWqx2ofP8ogzgVPwHH2fqWph5R9xBWtjowoOH5yW7Nkpb4SmMAXIi0WMRT-67toWeQ2Bfxh7i6tWTRcQx0R23XzIvPSNzk3NSD2qOt6jSLf2W_oWN5V0Q5gGWhNeACmboZmsxj7JjeT6XZJqO-1FTiPuNBALrZJJtmGQTM3kKN3LPgbZXcYVg-cgFO-d4tvsp0esJWGGziRUgH3l10caaYy9mZDVoIW5DAeQ9Tyq8ZuAv3owtbzE0PGlsdRjbVmiZfd9Qkr0R4FeXcLI3ku4CwAynplpkcCTi6h_pX_ziKbtwOyHob5WmlO9z-CbPRyT93fL3Pz9Tf-T3yEnPN05x0O7Ak0sJwFd7i0DBrgTPgADG0k9AzmHN8r4i7kx5hS4-C_L37DSNXFTpIAc9oBoZuplbjBS5AerQhrGto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس‌رونالدو با۱۰۴گل در ۱۱۰ بازی به بهترین گلزن تاریخ‌النصردرلیگ‌حرفه‌ای عربستان تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28655" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28653">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=l_UQaKMdRyuB4gvgxM0CYgw2klnTg9X3Je8Rl37EzSY_Q5bPG9KVf29Tf5WZb-Y10PmeFxDWhDZO9qwAvNQxNwYvFAhXDte0Jyu-p_zmHP2cIxNDI2vz5pn7t5hEPsGIuoLgW0ftBn1TaSnrunNW3GtisPDFnME6WFk_ehozNDiJYeQh0m0GIajF-ynapS3xLBIi57bwO-jMTXrFh2WietCWqd3mRpQnJ_SK6CB3b9p5iV7zUQGEm72ZcBwQ-I3RkLmInvJJwoFPA8T_tY698oJdrydQ0O4wHsV_1-BuzSVbr1OXrheQepfhcoOvAxn58mXBpmy_hAW6L1xrH5N9JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=l_UQaKMdRyuB4gvgxM0CYgw2klnTg9X3Je8Rl37EzSY_Q5bPG9KVf29Tf5WZb-Y10PmeFxDWhDZO9qwAvNQxNwYvFAhXDte0Jyu-p_zmHP2cIxNDI2vz5pn7t5hEPsGIuoLgW0ftBn1TaSnrunNW3GtisPDFnME6WFk_ehozNDiJYeQh0m0GIajF-ynapS3xLBIi57bwO-jMTXrFh2WietCWqd3mRpQnJ_SK6CB3b9p5iV7zUQGEm72ZcBwQ-I3RkLmInvJJwoFPA8T_tY698oJdrydQ0O4wHsV_1-BuzSVbr1OXrheQepfhcoOvAxn58mXBpmy_hAW6L1xrH5N9JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇵🇹
سوپرگل تماشایی روبن توس ستاره پرتغالی الهلال در بازی این هفته این تیم در لیگ عربستان؛ نوس این گل رو تقدیم دیگو زوتا فقید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28653" target="_blank">📅 10:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28652">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqdrn20MN9kIUvTXDbjOacrt9XSK19su2BWOfb0gGQDVFyQGtiplSNY-yWbaD8AT8YPmpbS3U2ndrN89-W_ik4MWrgBgdDIh9_lYupa8DXqU12LtFgYpQ8G5qWrW3HehQfcmcjeBS-RHMbk_mgRvNDai1eG4c1_SkimLya2hy0IWR3xIdcnsnT17lV980XNxJ-euo5RR4a4MATNVVtiQNkabpyJghe0w8eIJOpfuLtZ76igc-zRF8K3nQdb1FGplYo6Rp78U_MtSlPRfQLIkT10G7jxTPcdwFw5EndHXLk1fwwbJQkxV412XOk6219WWQVJH52UbuvwC4XdvW7I9BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28652" target="_blank">📅 09:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28651">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=Vw0jBJHuVLIx4iokVP_IsFfMWxZzk0JsDKU9Eob9N_N70A2LHYjDnL9shGKOV8HbXx2tNUafWj12lpbOCApxAazMv1PWR6Qy3XMQ_iHRf2cgvfpg1NYjJ9GwgPpconQCXC2VhqTI0Llc1qTHh5BerO4VnjJ22JnjBALSzPP1_v81UHe78neeIYqPLbwJ6L5baJzHSBhGiU-bhO7LhvCmkPxIYCJ8lZVuiZDCY3rkHdudz5aXC4pM5UYlxqHZS9ZOxm2SaACeRhTGnjYHFOndq8uUd5TuZkpiJiTkGrOGL5Fqtp3AN_J5F5iqFz1sMp_R8pta67Iwt3dvxzxN88-yJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=Vw0jBJHuVLIx4iokVP_IsFfMWxZzk0JsDKU9Eob9N_N70A2LHYjDnL9shGKOV8HbXx2tNUafWj12lpbOCApxAazMv1PWR6Qy3XMQ_iHRf2cgvfpg1NYjJ9GwgPpconQCXC2VhqTI0Llc1qTHh5BerO4VnjJ22JnjBALSzPP1_v81UHe78neeIYqPLbwJ6L5baJzHSBhGiU-bhO7LhvCmkPxIYCJ8lZVuiZDCY3rkHdudz5aXC4pM5UYlxqHZS9ZOxm2SaACeRhTGnjYHFOndq8uUd5TuZkpiJiTkGrOGL5Fqtp3AN_J5F5iqFz1sMp_R8pta67Iwt3dvxzxN88-yJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده الولید بن‌طلال‌مالک تیم الهلال در حال دوچرخه‌سواری‌درریاض‌درکنارجوانان‌عربستانی. او با بیش از ۱۹۰ میلیون یورو سه خرید بزرگ برای الهلال انجام داد. سامرویل؛ ۶۴ میلیون یورو؛ واتکینز؛ ۵۸ میلیون یورو؛ مارتینلی؛ ۶۰/۶۵ میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28651" target="_blank">📅 09:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28650">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddjz67LGO7h87dts7GxKSKTIK5IccCKFauEC2GUgRx0WCH85GpnaFhd3iU3U3tXcCLHRWQwb98IYzGyzg5V1-0NjsI89r_FoQHkZyS_KqouCtG14NMnIq3cpgv5Erj0p5XNptOZMLDpSdIN9eNUVRumvpMr_VRaYN6nimNj3v0J3G9KCRCJrjv2s5H5_Qr5Djhv9xfwe3ylazOhRh8qxctuy6Fbr-UlmGkZgbv8XuzXWHzCYDUBPxgHsN-6jJ9NTKnP48hBTyAS03fqr-83fS7hYB0IpQXDqkB3WzVnpedTD92LQYQcUgAuUWknYc77C7r0bfgwQe4K-P74d8YepSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تارتار گفته به اورونوف بازی ندادم چون دیر به تمرینات اضافه شده درحالی‌ایری و محبی هم دیر به تمرینات اضافه شدن اما فیکس بازی کردند. واقعیت اینه تارتار هیییچ اعتقادی به اورونوف نداره و داره کاری میکنه اورونوف خودش فرار کنه بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28650" target="_blank">📅 09:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28649">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=Gd5Qf8SePsh_UOGuruLJzclZL-bK1fWGvzYWbNDdNInypKOw_yLdsDaSrLAbjEoQIMX0S9_LykOVHTMB3LBZrjxVIwwTrVruH4HFEmmFzwdyCYcckjw3lG_t3paQl5krNS-H3xPHglR0E-wbKHa-mOHjdTWat8FhD-6GHsFkgfibwI0QsIhChBzg0EYDigh1vzu77V0jMnjp4svrVF0F_ZyjvDr8gEWgKYR7luxbu5mEpJ5zowHV0kJIt5OWfqLXD7tz47a6pshSWwM-lR1ucMu0zvU-jFAILb2qWSKVdM4NRtzvyuBSckLy0hxbX_i57082Sw-e77HqvDrCA2tGOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=Gd5Qf8SePsh_UOGuruLJzclZL-bK1fWGvzYWbNDdNInypKOw_yLdsDaSrLAbjEoQIMX0S9_LykOVHTMB3LBZrjxVIwwTrVruH4HFEmmFzwdyCYcckjw3lG_t3paQl5krNS-H3xPHglR0E-wbKHa-mOHjdTWat8FhD-6GHsFkgfibwI0QsIhChBzg0EYDigh1vzu77V0jMnjp4svrVF0F_ZyjvDr8gEWgKYR7luxbu5mEpJ5zowHV0kJIt5OWfqLXD7tz47a6pshSWwM-lR1ucMu0zvU-jFAILb2qWSKVdM4NRtzvyuBSckLy0hxbX_i57082Sw-e77HqvDrCA2tGOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجامانده از دیدار شب‌گذشته فولاد
🆚
استقلال؛ برخورد سرد رامین با یاسر آسانی و صالح حردانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28649" target="_blank">📅 09:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28648">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC0Yfc1bh-N6BjsYYScf_V5VsRxwWoMC1iEzBxifepuXBmkd2h_Euu-Ajin9gBW0i72TwEztSXY2ZPOiSJvMgoLq2AuEcvvf6sS3QJ_W4VpSQc4xsut9bwajsrcNdvuSgUpmZqoqPTgcpAFeehg0j30OZD7Sx9nX622vKSIMEA3XVZ6VEwcVl1w_Ai97gu2prjULJv2rW4lVdAIDx04q0F5LDI2vwzwP3LhoHSGgMVomq8cfebaYAF4VZV0iuZj-mSqFZJ_gxQESORbrA-rUltU65fPkuT5BPtu-RaA-mmAnsMfagsIzc_XMFzHYU_2FEH2kVGJG1CMUPRa6Il2qeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28648" target="_blank">📅 01:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28646">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3hu0NuJ78qTCG1y0Gr_Msdm3JSYb3DAIuGLWIg85ASDA07IH5aYS7pG3Uw-QsX_vUmW5AoxcXMCgaKXHXFJO1Y_DjUEAt0r1ijUPy_aRRuOL5QS5Nh_7nqIEvW7SfBCWmVkJ4h6ATqMPxBcaByVZWItI8C_Apn4PbmqVcgjpBHrgMqo2pIM2L6IWtdx1t_eTpDQpqLoNoL6xOYLnR5npy91FAHssuF7JJUlf8zaU_fAbA8iUN5RFiBJ5l67nd-IFvQcfajbRD8TTG1hCAfAbnK_pf_di9CygpM6F3hPwk7gS4NbLtNAxp_dVfEwhcIhyjzaw4lHpEHzbbN3-KTQHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌‌‌ امروز؛
مصاف پرسپولیس برابر انزلی‌چی‌ها و دوئل تاتنهام با شاگردان ماتیاس یایسله
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28646" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28645">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4E4tzQjIXZRGt2BKu3WWPDlfDWwnvyvRx6kCKXtK0y__KjX-NFDXyiRffAZ5Nc8NkrtkfogtEKojPJtH6TikA-sPXAj_s4ijm0Dd0-ejB4MWO0e8fRv7jn47IChA8GEl32jGndEH3JxEfMIz1Xvtg9QNWfQRJmfwydV3nL95_qB3oOuIrRQqgkgOErnB_0IUCGf8oj9eBGmgjjHrP3P49H7qZsYpZ3SZkGq0zOph5T84NpPwWOL0zKXobzP-pEhUFPZXK1o7gaqXfC8tDlQT18Sup7ZUezI1VZMPNymGBsYDZWI6M2qZ4FAqXheTWubH4fAUKkkasMyTL9M2D5Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
ازتساوی‌بدون‌گل استقلال و فولاد تا برد پرگل‌بایرن‌مونیخ و من‌سیتی مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28645" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28644">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy93HuHXoUkNVz1maBzLZPdKd4HxToPHjRVJ9PknCuHHzjr6v2pdf1k49LjIfxqKZo9jF8_wDu-S6Kq4XJugjjPZcFJeaOywrrEwTg9NUNAttLBj_Eplp00DQoDOorGR-wH8HHEjcvnD9dY_I8B_4z8XtF6Y9pwDuo643bDOotzvHTIMrOlZYE2yJt6d-4VdxpEr_RJPUH-AXTLBUg-vYC2r1WzWO8U6AygOKw-sK_-5RVffTSOo1NoRT8IBonx36cIbxqolzf-DLZ7fNiVGT8GfU1SC8XQTbmOjWjcR47R1dCHsqWH4czBbp5sKoL4FeJ_zFUN-ISa2nzyra2uo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28644" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28642">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKOHkkvKIq5IrTKfiN87dnrJPMrEcm8klRqoaO7j8JsfBAH5S_iWC0ncNYvvHEjfNkIJTObF6XPjgQg2BMvVf_RLRABiVl2p4_Rvj2BVsTjVn9jo4pxMvMuPXgvpHgRFe-BC92ExAxzTq8Y0OjhOxJEUVlckxxseA_mnrCXgSs7L_aHhgea39U_d51pBE29aRFUTcACn2TuUfhHh-HdJbBOeXUmpUezFa8sPUjPhsLcw0BqU4HrB6_AQ5Q3QGUkvzZIb8MznDI7SetguMlXysyOOHjpLjbgfr5HVAJX7y4xf9hfzjJXuA7E1id-1YOy41GtW7JiJxBXJDnqIP0EXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tC6vv-MnvEx0d44nARpwx0d9mxHh2hnVzkGCV9RPynlz6UC3SBuAh848yFZCGQzbSyEeT4hqi6n4rvliXEF7e5RAPhcIwll85n0pFN5IG20NaW7wDcc0yc1S50P7IMob6Cq4IxjHUyxR9g_ouBEh-54CfHX_BlM8bFk6HMQ3KHLcLs84HRuBUURwjrF3YqHW6NdOFzk3ja5pMYk75us77W7u8nm4o_V4gibsAfbxqGEuepFhs0uDMRlMLbgmnAGTZnMKTot96bwbjbF_xbV70yJ70TQ0yfzR0oeg4npM3SBRCHzq9rNzuy6yvDk51J4m5v03yKViBKq4zZCLLZqoSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28642" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28641">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM7utReai9vXOR-HnToNfckrPyVWXDmvWTvM-dZF3RN5A9QIhl-G7pd2yeugZcbps3nd2Un4XKsedusenqSE8ORyfkUmaaNS7TXSljDZdOUoOznU53whMlfAnWiYRn8RTiOtUnTSsqPzYJ8a993rgHb8AUmW8ZbLldotY7ZvOdUQVKRDfmlXhaXMBB5Nklk0tvjdm4xF20WWpMHpuZUftT2fJINTwq--ndG8s_ZEPgZMJI7GV978Oxozs8jqi-QOCs-xxUiU43ftUAh-WJxZjEiAMvzfkpMfRSKnDbCC2kC8nKLzWLDfdXnUw87uXG1n6lf8bWltdG05YzyhEmx5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول دیدار امشب‌دوتیم‌استقلال
🆚
فولاد خوزستان در هفته چهارم رقابت های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28641" target="_blank">📅 23:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28640">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffc6c7296.mp4?token=c0d9LRNUTrX2kka9F81UnlZQfPiTyNPGvO7smMbd3AFe_2xbviw5S2JoVrPgi4rosaPmb44dtg6q82E9KfjN07o1aqOOH__t8CzQkHJDq3gE93Gb0xxxmeplvmg4GLxJSt6KDerd-jkmylbhWWEfAXkqwvp2jpw6FRgJzmnjPfc2HkFjOQv6d1Sm3X6ONjVzffXcYxXCVQvqha-rJ8Ev1GE-I_0RF_wDUwvbAYwbseuDAhL11vDxoho64ggZHoieFZxPpqGFhw8Qt9Dozd6Dku658Mjc1nxGDk-uUSPrEgYaxOZ44ajfYeo0ElpdN7QEG1C285vPDof8hBl0guurFgAcgXgskgm8XmWM1EKPdkkJObX2bQAS5iobaKaXGHj9FDlUwzprPg9WSpHLTaFU0Xg_FZ0MnYVmJ8ukF_LWjjU6GkfxnTwQ4odRCA2bJW3qCKxWQsk06fjeGmjmXQPzpVPFDfukpyUf1FfPPJPUZ4-Aq1aFqNST7PiZXd7eVU1IqbE1An9n7FQUqtwcObsCvi528XhhvrONGydlQ-fXGagPI_r1M9VzuZqbwpto006IB1E8poSoSp1rNxVckGgmyYs2Q4y-6x-E8lSrDEMsfiNoniEZK6sAB7oA_PVs2VS65_JBXDRwEbKW4utd2QINFWPxtMfecEcN3s2UeZCN1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffc6c7296.mp4?token=c0d9LRNUTrX2kka9F81UnlZQfPiTyNPGvO7smMbd3AFe_2xbviw5S2JoVrPgi4rosaPmb44dtg6q82E9KfjN07o1aqOOH__t8CzQkHJDq3gE93Gb0xxxmeplvmg4GLxJSt6KDerd-jkmylbhWWEfAXkqwvp2jpw6FRgJzmnjPfc2HkFjOQv6d1Sm3X6ONjVzffXcYxXCVQvqha-rJ8Ev1GE-I_0RF_wDUwvbAYwbseuDAhL11vDxoho64ggZHoieFZxPpqGFhw8Qt9Dozd6Dku658Mjc1nxGDk-uUSPrEgYaxOZ44ajfYeo0ElpdN7QEG1C285vPDof8hBl0guurFgAcgXgskgm8XmWM1EKPdkkJObX2bQAS5iobaKaXGHj9FDlUwzprPg9WSpHLTaFU0Xg_FZ0MnYVmJ8ukF_LWjjU6GkfxnTwQ4odRCA2bJW3qCKxWQsk06fjeGmjmXQPzpVPFDfukpyUf1FfPPJPUZ4-Aq1aFqNST7PiZXd7eVU1IqbE1An9n7FQUqtwcObsCvi528XhhvrONGydlQ-fXGagPI_r1M9VzuZqbwpto006IB1E8poSoSp1rNxVckGgmyYs2Q4y-6x-E8lSrDEMsfiNoniEZK6sAB7oA_PVs2VS65_JBXDRwEbKW4utd2QINFWPxtMfecEcN3s2UeZCN1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلزنی رونالدو در بازی امشب النصر با التعاون؛
این 978امین‌گل CR7 در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28640" target="_blank">📅 22:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28639">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9ArDcLJDenIlHIRaG-_E4wGLfhX9vcdV1X4WArChdnGrEWoVZzmtSzbaHWesmjDR9CTQQJEU366P72bAtlEg6k94eYJ_ySHIYoKy7phfwtT9KEgFrutk9EBEg9MmCLl9diVUmINweTkPqCTwtDg1CG4_2ds7kZMtWse1K332rbTDR8bkZz3NlV16DWj1grH591HNs8FKQuAnUP9Wb35koqEQI1U4IO1081xKiR4DpTAi9Q8kZfoVPGuoDXMQzp14CUwBXC_rWztqlVkDqzbfudbiB0DbSgAOrowMjLSq2_BnVrp0uJ0uSSCicXAfPs9TVhJF4GV1XxX-InSsgwrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شماتیک‌ترکیب‌استقلال برای دیدار حساس امشب مقابل فولاد خوزستان؛ ساعت 21:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28639" target="_blank">📅 21:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28637">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvSpCBtOnFaVypN0z7baxspkRlPhAOeQnQLSiyrfvGBefNWEEKQ2mAxdodLTd4DoEnIh5HNxEb8LezGIJT0sh1wOf9Kj8T1SzPOHtUlE5KrBRW45wN0ATEpqm5Xg2bMUOtlpMCXj2DWXdbsqAtGT6zETq7e-43xJP3RFo4dNsIc3RQFPv8I6tmTCxsVxVx9kqBd-xloZz8k5KIis6o5HGzJk4tuxLgMN-C9NQdiN0IjaParUSKhdwtqICVtzhIgvu0VxIanP_Il2fqm4qFyvT7F1MFrQswl-99M54h_AqOfb1f8eXYxS-vp_PAR5yu1fhvsbJPEubEmBcRgcPaW6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28637" target="_blank">📅 21:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28636">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17182aab77.mp4?token=INfMweOFHkwP461eKU_-sOSLkhbaSwzvu1dCa6fPCdUFxfa05nIjAedUvFFZffgJR7iO72XQ8heSqfjnmmCZCR4v8Bkq91F2NDFEFxDE4pqS_7O5U1B00xfO6CPsr3tJLzor0hqv1FfKRJHvK90pWCChMkwQ2DAdp1_yMm2xgptTQrg7zIvyxk4F0bOqXa5uaQBUAeYiOMTII2xg2JlLtZIkJacyIC7w2nBB8c3J3xfEvf4nGQJxBJ8v-3gPUCz7m1XlbY-rlffxIxMLm6Mw52VUUJ8m7qyVbQxI5ZVY5RImQ_kMRSCJagN-Bf6CDY1EiAvf6nDZTj8bozfSAciB4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17182aab77.mp4?token=INfMweOFHkwP461eKU_-sOSLkhbaSwzvu1dCa6fPCdUFxfa05nIjAedUvFFZffgJR7iO72XQ8heSqfjnmmCZCR4v8Bkq91F2NDFEFxDE4pqS_7O5U1B00xfO6CPsr3tJLzor0hqv1FfKRJHvK90pWCChMkwQ2DAdp1_yMm2xgptTQrg7zIvyxk4F0bOqXa5uaQBUAeYiOMTII2xg2JlLtZIkJacyIC7w2nBB8c3J3xfEvf4nGQJxBJ8v-3gPUCz7m1XlbY-rlffxIxMLm6Mw52VUUJ8m7qyVbQxI5ZVY5RImQ_kMRSCJagN-Bf6CDY1EiAvf6nDZTj8bozfSAciB4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛ شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28636" target="_blank">📅 20:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28635">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28930c27fc.mp4?token=VS0X8Xd6DG2dwBpRwCwZnVdtyvvyuKTCRJBzZxys3VtRdU-EzJguaDOOvL3aYuENs_7ULE3Qg-g8rpye2pAkdaX9mRutyvFohAFbmtF_AeiYM7n-kRfmMlGuMqT0MfOlmrgjYSkSo_II_VBfZ6p7paEpRi-lhYKHHCWcRhcHvHqS5q1vGI8AnfmZUDfKZEKFtu1OG2Z4lciY4fz4ucRE1qftva5iQBLFUKCLRiFIdiZ_cHIcQy2l2z9JKI8B6MN2R38g_Ek_rZWcrAwQSTvR0bYKOTOa52CuFU0ZNnR9Biobpnnm4g4urXKpphTmAF8IcN-9LyZ199oWDrocZJid2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28930c27fc.mp4?token=VS0X8Xd6DG2dwBpRwCwZnVdtyvvyuKTCRJBzZxys3VtRdU-EzJguaDOOvL3aYuENs_7ULE3Qg-g8rpye2pAkdaX9mRutyvFohAFbmtF_AeiYM7n-kRfmMlGuMqT0MfOlmrgjYSkSo_II_VBfZ6p7paEpRi-lhYKHHCWcRhcHvHqS5q1vGI8AnfmZUDfKZEKFtu1OG2Z4lciY4fz4ucRE1qftva5iQBLFUKCLRiFIdiZ_cHIcQy2l2z9JKI8B6MN2R38g_Ek_rZWcrAwQSTvR0bYKOTOa52CuFU0ZNnR9Biobpnnm4g4urXKpphTmAF8IcN-9LyZ199oWDrocZJid2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
ستاره جدید نیومده گلزنی کرد؛ گل اول تیم سپاهان به گل‌گهر توسط کسری طاهری در دقیقه 6
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28635" target="_blank">📅 20:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28634">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce9FvLe9D0rxbQsCzWEi0fu0L82egVKaWgdw9q5-D-v_XxMLcqLAZn08Ii53X2IZYIGkZee7-MlZtHJ9Uv7XBoM9kuPCbbzpnhL4LCjqNLq2_IY0ao6_oSJGacWy5sPTM2178QbWJimi-Bg3Nye5JynpAdqyOaszChU6C9aKBz_XzzBRwO4qpTgfDTW1UkuhRg_IkYTkPesyS77VxhCRs6TvKtBIfAatXimAwylLrux9wLtlfbtxENY_7_qiiyKIADmQ2v9Y-Php_55HcwJ5xMuus4yAT0qd6DXO821F0cYqXCLyD-Az2hYg-vjBZmD4-7nerevrhWunUoaBa8aLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28634" target="_blank">📅 20:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28632">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOryv6VesKsYkRHe9s_102BTT3GCig51LDv4CNxFY76C3T3Rhh6WqMsiKdjvyilLyoqnoNf-O5wpYfInh2AlEd4DR3zXnj6y7GwG-q1hfWpfSk_kSIZLYHzFG-i1TAtTSR_m2Qu0RSwdjiJnp3EKcJynwXqjFdW3TvALVf4dKkByIJFNnGCF0ryEC7gfP7z5nVb14YiMzzDXilre8W-f1NFU4lMqhAYR4Zf9LclTJopB_3pGReI9qinBb9n88kK7IuvptrgjgD-G-875WMZix1P6XopZw-tse55raok5po_PD9YT6M0GA4-tAonzW3LzASbs6rzO7aBRZrRqsl_2Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9fYvcQXllakMueO9w9qABRWIbcBjJ70sYP44udvOrBMI4jZgOfPWUEUQSnDixWiKyrEJekaLAN9UQtMHxGcm3gki3rWE9HCM5QYpJDoe91wKJTmMKs5wyEKHOUFNnCBA7Y8vd2PmsS2oc89YEWDgJu8OakB6Y_v4noDllgSw25nvJOplt6HB_yaDDfiWYC4qBq_XOhSn7uSdrWhAi--tmsnHYZRoJCwIEcQ3Oxh1-rkumUIcV5f-EAu9ABXuwFnS8MwGmDtOOEvpCWEXb4G9eL52N9qP7Snc6MsOyuV6A9brJRp-xAI1dCAK-vmhKvKjDIvgFITdx3EDC09o_MxJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28632" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28631">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b6a569c2.mp4?token=qq--G3tm4jTN4KfE0YtihI09IO6A5g3BS1htl7e2qkECITF9OcrzmpxUpDlCqpP5vMbad9LZ8HMC6VVIseMrzkUhyJFpYA3mkPch6m6QvanIgKtPoh-kOaO4PEYQb8xPQjdqNtkpZBQcz-CRCriU8iIDOU8bJ6JZerOcuIfxp65n474nvRfwA2Nc-06HH1Q3EEENU60cuzZgy0Sr8SubTXJOeMXSkeD4s_mXcrGkvUrRx4zSCb4NnUBXZ0OYrAIV_63B0tfmZC8FxiDv5HIE2JBY2FzEpnxPTeRiasnFtrjxBeeOK0lGvyVuW7maajGl--bpShEg_VEtDFSO_NKy6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b6a569c2.mp4?token=qq--G3tm4jTN4KfE0YtihI09IO6A5g3BS1htl7e2qkECITF9OcrzmpxUpDlCqpP5vMbad9LZ8HMC6VVIseMrzkUhyJFpYA3mkPch6m6QvanIgKtPoh-kOaO4PEYQb8xPQjdqNtkpZBQcz-CRCriU8iIDOU8bJ6JZerOcuIfxp65n474nvRfwA2Nc-06HH1Q3EEENU60cuzZgy0Sr8SubTXJOeMXSkeD4s_mXcrGkvUrRx4zSCb4NnUBXZ0OYrAIV_63B0tfmZC8FxiDv5HIE2JBY2FzEpnxPTeRiasnFtrjxBeeOK0lGvyVuW7maajGl--bpShEg_VEtDFSO_NKy6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28631" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28630">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=Nz76d4Dg8atInWGIxUHZs9KPlOPX-d7cIPvCDLdieqxYWOvjJ60X-ZCMGXRax7C172SCLKTT0irG3wp3OP4qzUP_wTMEey2Bq6Exm4eHPeccnQ9LflUAqYNoNne1nCR_pRA_oDbjspa3cxGQyjq6jUfwk3VuOcYYA6N7iWFj31pWD8yQx4_GLRd-8P8HhMlMZgzmQ3bys4wErkBA1zP5Sy8Zk-pYFsK5A4dt2NnxvCMPiCMrt-8z6yjrUUjKtsruJz5pJtvT5X6swu5vrZ2D-jHblLeyGzyxyF737I0b1ZdcfHYBmlwlOkC1W_HWlPduDiIINMUacazwb5Lg-oDqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=Nz76d4Dg8atInWGIxUHZs9KPlOPX-d7cIPvCDLdieqxYWOvjJ60X-ZCMGXRax7C172SCLKTT0irG3wp3OP4qzUP_wTMEey2Bq6Exm4eHPeccnQ9LflUAqYNoNne1nCR_pRA_oDbjspa3cxGQyjq6jUfwk3VuOcYYA6N7iWFj31pWD8yQx4_GLRd-8P8HhMlMZgzmQ3bys4wErkBA1zP5Sy8Zk-pYFsK5A4dt2NnxvCMPiCMrt-8z6yjrUUjKtsruJz5pJtvT5X6swu5vrZ2D-jHblLeyGzyxyF737I0b1ZdcfHYBmlwlOkC1W_HWlPduDiIINMUacazwb5Lg-oDqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی احمد نوراللهی برای اتحاد کلبا در دیدار امشب مقابل اف سی یونایتد دبی در لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28630" target="_blank">📅 19:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28629">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQIUOfZD3gl_2k5MD8b2z1hG-wzkWsRcrx2wlb0mDTN3KsiSBzZLZegJ-jL9q4n70Nb52YZtYW29LfEgNRBORjXUJbq22KswSxxgUNc7OjLjAlq6tbWZihQJ9sWH-MflTTuylXIczuKyMry7U2X-l9k2_pHQnVb0zsRrPmTJi2xwaAuF7iKgw8fPoFVmF0Ssv7jLpm1XBBWhx1ZIVU1lUvHQoaiMeZBhUd40fjr1jfwffzW8n3JmGuscMcyER_erP_f0NS-j-IjAUu-_F_1tnRlJ6kksB3znWrMo4UNh_oYTkhYWQbbz-2s4-RD10-rkHCczZnQetDd8LhfNx3X8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر
؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28629" target="_blank">📅 18:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28628">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4MKzYGk9n-ekvhb2_ehMa76wyMktKiNtwNUAtSZHrw3aC1EKjLL6SFRhZs_WEI-7jHE1C32LWkyN3pOPLFihWf73K6JUKnk4d4u_EVYKFogKSHqqlpuH5DjYbE7mCqhEDyMKqKWNaaWEp7TUKNfqNRUr3wGG78J3emOx2YZIfajRO7xclCqJBF0DwZ1hN-_o9OwVMLEjDMYm0WOFdhd6LPCQAOdYd0hS-n9xaNrjzikQFwL_TVKpWzbL_8eq1eUaxFG-2HUoH9BUZMvUxAqvkoTQ6Yk5Zt1H7uH3LbwpEWRX21YaUw6FCe9uwK_gzMLTrwVbdpP_dXOSKcvjwIW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛
شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28628" target="_blank">📅 18:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28627">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sovsLw3x-GeOXJ4gv1VUDlr476cUFkgMNvCML_p5VmhCFFBN8RZATtTma8SUosw-wbnL6shjd1KG6vZK8bmbelorFYF16VWHebdPAzzdJrb2aAQrqmL5r06_myHQv7xIwPSc8JgFGkBARLqd2t7th5uClqYpAuiwP0hAkrp6wJHSNjCcqP1ui2_qScnWBUrhYOdH8qSYtBlRu0Fy3nydT9v-NrgqOlz2c1_cG-1SkD0SHE9iljDkK-x6-P3RpA2pS9bO_t2Q0CpOlrSi_M0kdw8uC2Co8JLr7rN1S-Maw5PR7eQF8LjLavY9_1ybsq4xQx7k_RCk52SqJ7WZiNy4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لخ پوزنان لهستان با الهیار صیادمنش و علی قلی‌ زاده در لیگ اروپا مقابل تیم‌های مطرحی مثل لورکوزن، بنفیکا، ساندرلند و کریستال پالاس بازی میکنه. فرصت بزرگ برای الهیار صیادمنش که کریر فوتبالیش رو یه قدم ببره جلوتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28627" target="_blank">📅 17:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28626">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6XWfwYglqRui0aWwgL8YVlEQaXhr0pl8_1l-_RNUg2UvXAXwUyeCOhYGfD4A0atedXjxe07ASoxqEi_uiDUExEgzzd0lFW8_ycxEuf8SetUvjSUbZRmvWvqp9a67tA62mkXKQESCkdi4x80d7NDkM-bzbrUXjbAEJMnHfipP5rgoyf1aq8uOOZywZgOwwYoLopyNkOlOanJohCwVmCwkWUmNniiQyF18_Cg4Uri76lHSMTByCWtsFTOweJ9jE8cZZvn6GcaVnePOWOZaCd9wwkG_lkbVidtSYDM5hidtzprrPTKwKx-Q0oPnYnk3HzG7M0oXnPwjJSybE1BO3euLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28626" target="_blank">📅 17:15 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
