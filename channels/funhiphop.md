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
<img src="https://cdn4.telesco.pe/file/ijt8Md8on8Q18D4zjD70nnYTBCT3TLzuJhKB8uq4sAdrSlUud4LcRPZZCNBvVv5bklyru6EiMXnuIiPcbWqDkIjURsTmGxaF-MqCRC4Zu6wVJwTZmSQWMUW8-AK2vaE7U3xULs5MtFO8ZJW9jemgwHf4YF9n3wYu7QeraJ33vY19jbmk_bfN-7pIfmNRtYXLstWJrA7ZUc_rjxnRNBxpBAVdo7mvN8v0UPldqEftlc7ayKyeMlXpJ1iU3iQE3Vry-FOEPRls5-I0FHAh6Ymc9Xu5Y-A3_DMLedozNWblYOv6VY-i9TQ1khu5_GneA_kzeXlFaj3WXdmvcCm8DLqgDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 22:20:05</div>
<hr>

<div class="tg-post" id="msg-83253">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=K4KoFmKb8h_ucRVLy23H5_qAeYk-GKLzAYLtbSAqCMUP2ft49kweD_7Hx4Q89_3v7orm9DJFgaXB4eRldY7TSABUoHHS2KFQI7fwCOXy-6ciUb_nHiObwGBD8pm11s4wBvkkgqzn-70FGwKXepvL8wYtnnyHDCYFYvlw5i5qC7uj29qo_P8UkqWpnVkxBATfogvqFXGl3Sz_QgixsG4XVg5xQS8y_TxVtVE1olUdQ1o2Wczq3q1e1tYvxFUT_8G3f_keX8YaPtFcMUhAc5__t25NLIaqeXesQMCpMsFOIgYP-bXNQZgdWmwL_bmVlbTgkKPr1wP8sKQdhZYimzDaHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=K4KoFmKb8h_ucRVLy23H5_qAeYk-GKLzAYLtbSAqCMUP2ft49kweD_7Hx4Q89_3v7orm9DJFgaXB4eRldY7TSABUoHHS2KFQI7fwCOXy-6ciUb_nHiObwGBD8pm11s4wBvkkgqzn-70FGwKXepvL8wYtnnyHDCYFYvlw5i5qC7uj29qo_P8UkqWpnVkxBATfogvqFXGl3Sz_QgixsG4XVg5xQS8y_TxVtVE1olUdQ1o2Wczq3q1e1tYvxFUT_8G3f_keX8YaPtFcMUhAc5__t25NLIaqeXesQMCpMsFOIgYP-bXNQZgdWmwL_bmVlbTgkKPr1wP8sKQdhZYimzDaHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/funhiphop/83253" target="_blank">📅 21:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83252">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAR6NTfhbbdhW1UE6xQPGvt4OUoaCtlVp0QWDFMgxEZgiMNRHZB3SSkVinPp_IauFkgUGdPaGeNI0XiGIz-1CqPYFw7HwFpiJb31db7eQXp0frCyBgJWAh0JZYKDc6yKxaQGsqhtLXOhCtahMFftFNUjH9f9ehe-nvE5ubU6Pk944xP1LpP7IeR7-5oDzxi75EWqELKNgWgWANs-sydCVgNJ4NNOhZjl1lNKk5_qTg0aRtrrVapDvu3Uy8q5XtsFGOZN4pBKAodhTniBB_Xsbb2maTk-7kqUVkh-TqmWleFiCdvRNeyLcgtW3ywwR8wR_iiz1dZ0IYS83i0cjRusFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصخل که اشتباه جمع و تفریق کرده ولی جدای این ۲۶ تا میمونه، یه تورکم بوده گیشنیزارو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/83252" target="_blank">📅 21:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83251">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPQp9Of5XwJhNasG9PbTdNvGRQ8_A4T30TMX0zMrWBEKfN3rfSga8ZWqWSOogZdfYOTKwFzqzQkNdwsrd92pLQIeV6sn5ymDvK9DH5CHsTSi_l6oN0CSRJVX-s4L0HbofBhUCGkGDOjsETBaFRVd8hUx9a3GBHf8kcDcEchHEvvLOYdUzprOUGP_wXfvDXQGZf48o2N2jDUyhilWglXz8lc_U5kh4KWpSX_ZteH3Q9t1gcScqbJbDZVVJvHbrHlGhXYRYXjUA-iREga0DNdIPZSl0PdNcBoGasle_bi43CdAGCsmuJCg41cvoG-_WuS0s6DVADaUW9w-OtMR6hJ2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا مهراد هیدن که با اعضای گروهش فرق داره و بحثش جداست اومده ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/funhiphop/83251" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83249">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMdLcFwL14KNiSuOE7nD-p6Qc5Zn56PpsvOn41JDhfwHEjSBjhwEpmWzuqpfewztOy-pFA8-AisfQH244etk22F2cqfpCAU4JYXzH9Y9IdML9tDsfdtYpy4PVc2jDRFmlt1_W4-GT5HuApZALhhRRZNxkQi86BpxHdZrgU44wattTAVhCzJG7j-yAuDQVwgVjO5jL3yqVJzdLDleKplLET_tZ16Kwbizorgz4G7FBpxQvCuOju9I5rMbkbKZsdpBOoybh4RntZ0qtSpem5qdn5KjbSVXmpxg-GF-Y_XuQ4rTJq962j-1fX-c-HwQ-g9MyepSOeUXnHRnISahTabAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aiikRwThpOBTyaoP9qpmfWnTxXwZ1Z_gY18Mf2W5C44bkt_Uzz342B2GVGM-WcDppRrOIqI6VqJKup4-9RWjSIOMM_jBHzOtwgR0VX2WIh4lXXaGnb4smDsv_yMmvvdswgKR6CUdpZQkdRZYseWSsAklQyZPmFBvkYbwKn2OPzP---y6-g8dj5YqFS9-CJHmfhyqHKictUgdWXBm3vZ79nNpz4ZpEye0Trqwn2avAv0NXciw6YdDx_DvE3V709kvIm6EX4avv7SvS3PUdddTnEuJf_d7kIwsrm5MApqjJGz_hYKRBjb9Mvfnioqrmg9aGunEVE44hgbXo73SWDJTyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آدیداس با انیمیشن ماشین ها همکاری کرده و کفش با طرح مک کویین و ماتر داده بیرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/funhiphop/83249" target="_blank">📅 19:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83248">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImVhJwBrO8NcKNyRNBb0wE1psy_jSE6BxwyNbtrizkQ-xNEc7yHz0erVwRFIS7jOuFQ77YLMadilzrj4fXgxdnYOW163z0jvm15QXrkhxwk_hIrR2ZqONWxjMawMd0A94xdfDWKPBSRla0hKeD3_5SXiIfFSdkh9GfDuo6Hbtizdh5lxj5Tn0aBKHCMAxVRpILoQt0Y6QPVtTiqg_6PYV3-PLe1_c5fpxzpHHH4QW5zC5SnW3xKq6bARjY5jm28-JH6k8AnOlpu9iCziaPdt0E8ae3zouUwQtSPWPuSwavazgyP1KUv9weFRoM7xGYceYwYcWycp6wvJU0LrlvA5pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم دیگه بگذره عکس کیر مهدیارم لیک میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/funhiphop/83248" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83247">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsF3KayorZ2tB-cgR1xE6dp5YGonruPh10qhAVPoYxjiyWoR3GQdi7--ki8w5ZnhPtlJKR_RI2kXoakuntPH5zsxZFbvp1ZYP0igs3LXk5cicvWPFoKaoMDi0q7SXBlcIAtVHGrrqTQMHUJLDRG_cfA_cop9r3DXD2tsX3hgERfAMm8ByZbFMuXZq472XuEAtFnu4Whxti74GU6mDbzrHoNJUhGHQojaXS5OvHwPWh_zeC7-McYc2cZpGw_AkTuOehHEJSx_xuvwSFRrhDBU27-MVSM0GZkCdeMewXcpPv3cbRxi73pWmc8aDpkUsyWldhfBLcKKUB-3xV_eAIXE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰٪ بونوس ورزشی برای هر واریز فقط در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
g19
🅰
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/funhiphop/83247" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83246">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8rp69QKkTxvDwHHUDwa1lRcagaPGFVfPbd7iUMmTLrDbX9Vk4xc06hpQpvXwoYL_WJGfog0fSFR1GipZHlmcDJaiqBheoL8d46hRcdxtWhfId0r267d-KpCTC_w9MFbq2OnZLsWsnbVyblr1LKuiLIuepvCXqZBhO8iplU6WRCy8wx5Z8sXDYQBSvgAZihd9ADoVjt-QyjHbZKPONL9m8oAwAiN7p8L6U5CACFdY7wiClprRAekApbqMjYfUiA7uhGWAKeax_OmNFhB5LQoiwjfrfo9WIvjS4L-d7lHzsBGyBl67Yspa0R_siVrmZSdzUH9xjC_GRz8ZDjtbCvl3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین مهاجم نوکای تاریخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/83246" target="_blank">📅 17:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83245">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خلوت کنید آقای خمسه اومده</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/83245" target="_blank">📅 17:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83244">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuQnHwhBnUTDFMg8Y1xv93PU-B-xgn6FDtp0JYPbXFUcI7Ug3Z8-3Wz11LDdkRX06rYVM-dyRJzKcXerNoEtJ-pRU7JSThFlIw39sPgYmZMMTKz-aI1qo4T6AkxLyEpXCAxZ6JpkmzXLcpq28zZVkTRrBor9AqCZ0dV7mO3iuxoK7ALH1Qky5tSrUXcDzu5f5rzRxHuUY8NTwlSysimxUSovTCmevq7nxm75iKKH_t-8hOZ6xwNYSV6d7JahqSS_o7O0U5yWqCOi7Y2GwFIEggcEztvj0mdbg4suV-wl-0gguPcaZTctogdyGapPzetj0ZIBwTLKntBfT2M0TW2X6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب رپفارسی اینه که کسی که به داداش حسین تی ام میشناسنش به سجاد شاهی میگه فید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/83244" target="_blank">📅 16:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83240">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=M8RiQe9Llku0V4sl82P6qlR6KxVixVUN-k5D3i0b_-W5KvmBsTWHL8LFQG9JriYGj46GKM4MY_GOtAchvuLhscYzPvRFegdNXF_V4XmJ_M1gf78rLEBbDxhQWSLH7EXQ3jt4qqqrBEgZksOaQODD2dNINre-8VPUUck6tay2GsLSD7Q4lKkpLczJdJ6ZO333myZj5OKU3Tz7rVSw2q7YbSGEaHWMLXSASp6bs__DJRKu_nWvOsSURE-xA8qILSva9VyiIBw0eWRtXFnDgyUX_dPbhmpcTQ9jBiC5ySjmbHFzyjLcdlwcFWtaYFPfz54K8eIwN9O1Fyfs1zQ3BrBh3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=M8RiQe9Llku0V4sl82P6qlR6KxVixVUN-k5D3i0b_-W5KvmBsTWHL8LFQG9JriYGj46GKM4MY_GOtAchvuLhscYzPvRFegdNXF_V4XmJ_M1gf78rLEBbDxhQWSLH7EXQ3jt4qqqrBEgZksOaQODD2dNINre-8VPUUck6tay2GsLSD7Q4lKkpLczJdJ6ZO333myZj5OKU3Tz7rVSw2q7YbSGEaHWMLXSASp6bs__DJRKu_nWvOsSURE-xA8qILSva9VyiIBw0eWRtXFnDgyUX_dPbhmpcTQ9jBiC5ySjmbHFzyjLcdlwcFWtaYFPfz54K8eIwN9O1Fyfs1zQ3BrBh3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83240" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83239">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ولی خب طبیعتاً هیچوقت کسی که برا پول میجنگه نمیتونه حریف کسی برا اعتقاد میجنگه بشه، اسرائیلم سر همین جلو اینا دووم اورده و خیلیاشونو نابود کرده، چون اونام اعتقاد خودشونو دارن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83239" target="_blank">📅 14:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83238">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مگه نمیگقتید حوثی ها دارن بگا میرن</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83238" target="_blank">📅 14:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83237">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انصار الله و حوثی های یمن به نیروهای تحت حمایت عربستان و امارات کیر زدن و درحال پیشروی ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83237" target="_blank">📅 14:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83236">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl4eHbES-4IXGkM0mLy6ws4H9ijsWZ6aKEHc0JgqNtFyeGWa-5sydC2SXM0zT9ZwcmwoyCoae4nTkcqhd442gEB15oZBU0Xj6hBK6bWAMLC-Rs0JxfT-KTQeXFQ1Gu3hXK3JLNnMQRNZ4PprJte_lbcmSoMtsMGXUqW1Tw6-OPKhNYV1jCsP4qbCAyRpJ7XG2lbgXl82RnfwxAqQsPOOKr_NE7su9Yvr_bPU3-VCYtHuMoce-qoW-NPcZ2T8jAsR0HDV3tzzJLzpkkRulyMSAXWqbCEzCzvqwGa7hJ64Q7bZlkagrwPKs6l-SRR_30k1RYti5JscvODYYy0Tqnzayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم نظرم عوض شد ولی همچنان لیلی بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83236" target="_blank">📅 14:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83234">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1Asw8vYB5-QsFZbj3cuRiMoGzQVrAnO96-PK4oCoh_cWNNoxVDTkPfnz3x_lj0Bq0jiQFvZq9GT68dMrTpzDZyYVtoSFhzvOXUDWtw_QajEKRaaoAhypuSLWUbcdiIYKUch9gPci35UMxolA6910fRgjROEAr0aKX9ZG0vZqfCxvh2GmcQF_Ff7WDVzExhCGLlGVa-GGl9mgFn3-qKp_LURPL4kRfdbvQhdLRFXpXFt13zt7bSsOe56ZsDxaap5hfJ5ngmBgawZojzwwq3YbOqki157-Z2Z9QRLp467K0W5glX3O2sc-oJG1JhQYI9gZ8DlXAKj8-3Q6uPfAnfXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfiitZvO48q3t2rpKelRGTqOQ_H_km5MFe0eskMKHLTYY_3srOvI6pB4_RpgaDeA_FXKpBgS1gLEU-7zMlqlgFWgPLw3R9N8Oqjg50VQ1Q6RZyj8tiVy2buBpr0OGxYwXcM7ZzHi0AjpwIBIAdTnXcyDSWTl-3cyjqLDBCn5dRJs0KY5r4yPtNKiMq3H3BBhZja2VDJf9dbBN9rGQrYuJWOhTib1bXOQbTNxiFBgyb9KG_0ZbtuRHFnr_tkeA8gjl3ry2ck6oeDMaJpwiFk4NYUMoi9ouT1KpOhbXTKjZcboMg7T3PsvsH6xc_lx9xeq3vj_gy_Dz_eNzzoI1muftA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لیلی بازرگان بدون دست و پا اینو میزنه</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83234" target="_blank">📅 14:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83233">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الان لیلی بازرگان میاد توییت میزنه این کار شاهین نجفی رو به شاهزاده اطلاع دادم و منتظرم باهاش برخورد کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83233" target="_blank">📅 13:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83232">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83232" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83228">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnI94se78g46my0gqxYLLxodGPCNFN8fV60S-NTBmg5eSDsjl88br_WV_MtYvdBa9C1010KrcDx6wTgF1V4-Pssv7AEu04Imz6T1_ute6PLAUTYwwXsN0g8zhV4zX0Oa_JPpMcjyNvPE7KwLhh3ZstNq-LOLeB4Q6G2QJ7LsIAZtlrtx46xM0cMI9SooK1kHYcLo3u7U9zEKMoLyEoaEu_1jje5ViWy0K4wieNM0FSQ-cQmfzG4YJMwGtwRlEJ1jJmg-fjYWiFuXyhBG-uf9mwC2gcqeY72PTLhNPktXydJ2FujHvXHNbYAtqG3J5VtEYrKkitz9FQgT74n6oBcw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OoQzYd38-Syg85ROJLG609iU4IEuFOCpssLp42sExqCM4wdfXWlvUto6tNrLUv0gxezom2vlVUD0ErA2qt6JzXIzHfRHhazDAkXCh6-hqZgdqLA0nC3QcPAuWAO-MyOsjs5wxV_VsQ2Jgp28qrF0ba7F03QUEt3LWUZFZs5ocYs1GRXR2foiH5f8qU-c8Tzp01hm8SMb68eDnGUBQkf-8ffzPsIbwhRMZDF5vYywp3ZI2lvz1dJiOn54I3IqTPvRFF5UkuWlMKDplP_0zvTwdcmsexEDcnh1OOF3KG2SwpGx8jtwGUXPVECEhQruPWF04CBp8J0jTN148rXLLO8gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1nTzE9YedfMMvlCRdiapRsnwtlNTvtHGvyJcGstzupEbVE47CC5WirLTr75RqLgSWuvKBUTFDSERO3xQKXIgXt5f_OC-AE_QSd8SFo3-J50yYGtFgHbEa8Sy7wxGKtNkVVc3xTJlY93sq-K9vx51mktS5RBODztOFnlzykLpWiLDJgKTvIJsrLjII1GRlyh-cHuhiLMJsHGsOZ5As1zrwuzOKbVg2U75Lv-EdPh2cTBtBkY6phug2iCZZw4msJorBX1UsbeHw5wJKCMuY5OnTvlzoneX47mTkcbF43S9yIRrU4YlSdmQqfoSQCR_a-dHAFzvGoxg2HaHh10UyjOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ea0nAzRhJRbWidBVaOJ-gliincMH1yM4WM570vDX1qvZRPEKt6rwYXxXZkk0RzKegrfupftC6qDRYbCbVUFTbY7xxBMVhiedghT-GXPzFnnMf-xGwoVlVJAl_UXBGGaQ_uHGEXyNZEuzWD2qiZUjBNXHYP4r22W96xBDdIqtVPCGKNkTtPUw4XTQY8b1xpYaO4CS9o9EepBpTLQD79jHOuksnC-jzQy8l9TH-rdd0M-e6TbagDhu-U5djpn1XAigJRqZR_zUSt7f1g65G7HnAFZPdDdw4-dONVUUd-FcWGM67foRrp_3VUo8ZLA153g6pSkm9YXxiJ0oIfNpR9P3dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/83228" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83227">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83227" target="_blank">📅 13:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83226">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83226" target="_blank">📅 12:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83225">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الان دیگه هرکی عقل داره از قبل داشته</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83225" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83224">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYkvA4mfl-0G_wYutCJYu_fP_J7JeslVRpFPFLWfPFE7eMZ3D1nrEv-XpzzpnXmxE1ukPmwu1Z5fFuASiQ39lFZowJdnD28OqxNaUJzPpKn8nrahU-PpxFyDc2UFlF6TCXU-RCzNd9ljdhw5EaZpJRaJdRSWRfxxKL86p7hhU85qM7r35H9z6patQWTT64hPsOvdCxaW3ptfvqzOKePfg-T2Dz6K_iusWtr1cpiqK98tLqePlw-lqXV3TBnc2zdXckez8ofRVabTHgT5Q1WJTmx4DdbrXV4FvOjgvPukIH3S9JoWFySuWsLennmRPZ3OUmlyb0c588NCZjqim8UMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید جوانمرد، افسر معترض ارتش، به ۸ سال حبس محکوم شد
جوانمرد، اهل الشتر در استان لرستان، پس از حضور در اعتراضات سراسری ۱۴۰۱ از ارتش اخراج شد و در پرونده‌ای مرتبط با فعالیت‌ها و مواضعش به سه سال زندان محکوم شد.
بر اساس این گزارش، جوانمرد که در مرخصی زندان به سر می‌برد، ۱۹ دی ۱۴۰۴ در منزلش بازداشت شد و در پرونده‌ای جدید با اتهام‌های «همکاری با دول متخاصم»، «اخلال در نظم» و «اقدام علیه امنیت ملی» به پنج سال  دیگر حبس محکوم شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83224" target="_blank">📅 11:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83223">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-4-zBuMtxFm_OkeqxrFx3jkKlRMstMdx1Q6UclDm_rT4BkNZHfiL8j--zHKSZu8mvQpOkJADZxmnVI8JY4C5ipkup62xwL5UMD1uGpQ4CiJP7sXrI9fJfWahoOZFndwVYwts-lc1dp9uBk9gxfOrZGdWHxYviHcdLIgf3D2y7AW8NtX7M4dQaLkpJBevu5B-DRxbGcTJlBSHCEFAYy42caGH5RoKSpY2tpTrzKuAMXNrm51RnaHd_hTOvRdf0bckFBr9FbDpiXhNctoIvJ9vyafOiP2On3m1ujfk-CRUCU52FkkImygHq1HZqkZOIGddkR6wdu4YqP_0u-poFHiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا به خدا این کار همه جای دنیا رای خریدن حساب میشه، این آمریکا دیگه زیادی دموکراسی داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83223" target="_blank">📅 10:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83222">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GegdaabLeDFp_nQE8D9b0EW-qor--KgCsIlVqfQibmufTT0g3-sMzn9c4pdQqFqggP5SElqIZKhrzOBzhKldYhftQ-jSH9L9RNRDGXwuggiNeooF3bs5XjxPjHoe7zcHfe_BwwXEh71P0UV55dq3DjTL5RRju6cmo2d3mHBOHQQGO2P4c7X4v_9UOQnHSBYy35PSZaLgBBqKKvNIs7ZFLjA9B46b1J70Au-1LbyHqHGCPe_af1mkLzPsuVxwVxbnUr-WwMxZFsQP3fk4eHdrsnSwu1zm3ufpvA_ZAyg3UG8WJ0bPM4JmRSAoiDSFAcehzzbmJcTZjeA2ELPOt7LYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بونوس ورزشی ویژه برای لیگ قهرمانان اروپا در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
🅰
19r
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/83222" target="_blank">📅 10:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83221">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ:
ما شاهد فعالیت‌های مشکوک در کوه کلنگ هستیم، به آنها هشدار می‌دهم دست بردارند وگرنه مجبور به اقدام خواهیم شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83221" target="_blank">📅 10:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83220">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGL13alN9WwojDm8aSj8GB1IRMeY3np-icinCY8f_TBQ85hv6GuUOCkGrKPX6XzAjiJlbfdfHdbkMMG4LcPEdHg-An-KI3MhTCiWQOlzekwYZW9kdQS544_BTnvFbWwVRobdSrwnam0cHWVmf5xR_JfkG6LVzRsXJGY84ijjr40HGUShd9IyCkT7lMZh7EufyrFSOhPZ4EeaztFjQHcO0v0BDZfYxy4A5qu9FQmXzpwmERsa0MDcpsKLZssrtI6e_3xDtcgslV83ql09e-CTnw7KMsZ_vq82w0UCvm3og3yIhccxMoi-dENXFmZHylSCpggwCcjNWdMJPEwsGUnMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون متن ریز اون وسط رو من اضافه نکردم، خود عقب مونده‌ش فکر کرده خیلی خنده داره.
ولی به هرحال اینچیزا مهم نیست که، دوباره صبح زیباتون بخیر
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83220" target="_blank">📅 10:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83219">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=l4059wRbSM_ouOLpPgzHRBhs0sPtSJJk6fDF_mh9G9sVf3Swr2rIgNSj57Aq0BH_xT65cZ3G115B1n_igQ4Mchsrawnxwsm-CzLvDE11VNnAOca2xkIA4gByFMwk2vTYyeHhnB5IXTpudGIZRuBUF2Av8A4vOK1EDRnac6IY2_BBtyLYDgbaODEjY7NidEYNGH0-5VjF2MULhWrjdfrymZrKBqUuutbZZ3sS3L8Fm-oIEixRXEbcvqv8vnjLKugZ7URnV1CWgKup0ozr4X_l4kaMwvpoNG9NlKaYEhit9CZuabtjmFgz31o4-_9NY9U7pZ2oHoGQyVaZLae52q4R5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=l4059wRbSM_ouOLpPgzHRBhs0sPtSJJk6fDF_mh9G9sVf3Swr2rIgNSj57Aq0BH_xT65cZ3G115B1n_igQ4Mchsrawnxwsm-CzLvDE11VNnAOca2xkIA4gByFMwk2vTYyeHhnB5IXTpudGIZRuBUF2Av8A4vOK1EDRnac6IY2_BBtyLYDgbaODEjY7NidEYNGH0-5VjF2MULhWrjdfrymZrKBqUuutbZZ3sS3L8Fm-oIEixRXEbcvqv8vnjLKugZ7URnV1CWgKup0ozr4X_l4kaMwvpoNG9NlKaYEhit9CZuabtjmFgz31o4-_9NY9U7pZ2oHoGQyVaZLae52q4R5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا اعلام کرده فیلم سینمایی نجات خلبان آمریکایی در خاک ایران هم دستور ساختشو صادر کردن و بزودی وارد پرده سینما میشه.
بزودی مردم آمریکا تو سینما:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83219" target="_blank">📅 09:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83218">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=EpmaxEDJ2-JrBDVQjcTp7VwmwU5CO5vfoA00Y1ygE4CceGE6ASFxpNATgkEW7Q_LX147YWVAO8x3SdErsQe0oxsXp3qxec-oGZ0KhgW6J-hVAz1TCbrxXSSW1dlSxvzQfdxL0MEw5MjR7yPrh3TjYqkbDHIl3EjQX57jq817Ss7cFlDQAyCL-sCJqqT1NeIxK5wxFNGv_NB81xejhBKLHLRA-uGH8q1fImgcMLf7-a_uF7tic1P1tF3AAcCzF_rQmlfdkqO0m8enaPyrDUHZMuX7JhvByCSOkE0o6yFi0SQRJiFwssqsjwzn9j64BMDMCjPXBu-Y6g__8BW-Mmjuow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=EpmaxEDJ2-JrBDVQjcTp7VwmwU5CO5vfoA00Y1ygE4CceGE6ASFxpNATgkEW7Q_LX147YWVAO8x3SdErsQe0oxsXp3qxec-oGZ0KhgW6J-hVAz1TCbrxXSSW1dlSxvzQfdxL0MEw5MjR7yPrh3TjYqkbDHIl3EjQX57jq817Ss7cFlDQAyCL-sCJqqT1NeIxK5wxFNGv_NB81xejhBKLHLRA-uGH8q1fImgcMLf7-a_uF7tic1P1tF3AAcCzF_rQmlfdkqO0m8enaPyrDUHZMuX7JhvByCSOkE0o6yFi0SQRJiFwssqsjwzn9j64BMDMCjPXBu-Y6g__8BW-Mmjuow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون با تیک‌تاک فارسی بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83218" target="_blank">📅 08:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83217">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قرمه سبزی جا افتاده از نظر پسرا و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83217" target="_blank">📅 02:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83216">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">۸ ماه گذشت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83216" target="_blank">📅 00:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnmJ1UX7y77fteeDhzwx-T-0eCI3KkD3tw6wrwIhBqp4adZRfeB5i6kWghYHZXxgPngf--pGV-2o2b72qbgK1v9CQIXqtxPWXaTBAO7uP6JJoDT7HKKzVNg1Wz1lJMcYug_xwS3zsiiqQg4PB3t0pI6GZPI2JbeYRqfICcv7QnUMecyDMRLXgAW8mU8ZfaTfnO8CUbwI4lKMv5NnfeKRYzaigyXIV4x8KjEonni2j11vRvfo4LsEkUpiynX0eTXioLS0yVxWYXbrjQnOtU31vfcbYMdnD4BrKxQe9x1hp4jAQxLMT09GLzH_rNAV5LWnadrFx6fXvuLJe5VStG9_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDfnQPRUdVyk-riT9gHgcEwHfcQ3v5wNq--3By8MGhBSTBjgGl5dtgxjY3BQxaU-lbr1YQctjPI8wu8W4f0pp0kbidvda3b_x7W3QHUeol0milph-7Xs5TwBpDVMDr2dxFB1uv6wGc9Xe9TTCXYtWoMHHQ31ljTGgJ1ubQQauRVeVYjoMuOF3kZfyLXf2mixVK5J5uEBGSoKeqNtFP1YQ2hXsvVDxzc9vYLCfpX-tG7QdZJbF7Yw3_iqeYA7XZKqeneq6yzPj8WePz7BGjiBcLNpIZd8z3vjkSSeKo2VBoBWAMoM6c-IPfKCxg6GgOcLioYd0J9J5E3WlekUJt0s3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت بت زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83214" target="_blank">📅 22:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83213">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un4751cBqilTsnMgmaq4JJZoLxfzUzX9kXyQTBYZZuNafiqcoq0GrDF1Y37stHMS2QLrw6Q9AQCNmj2AmcYIZGrHXbLkH0oI94XY2avuxwztdjT0UZx1ujpQMeyuJJo9UdWxSRf1OwpG62U46n2B76PcSN4WXVBbdjoQXJ0tyzVCowNv9S3tKSIgINMpksbAHo1VzuOFdX_3z7is4awIaccIgi6NTwuFbyLF5B_IJRYrAow_s3euoJ_5kYnujeSSYWU0tEMXGYDiOq_gNh2WMA8RZQLnivlwq9iNkKI-hBT5oL6Ro2DCXOubzXUhNXMMJxW7zvDRVG7WBSkKQqgGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احساس میکنم بارسا منظوری داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83213" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDYZYfZhfb_TFbsrNd3-yrq0mooxQm3xudEtFoV6IIXdJT5Dy_CftiD47BX8ovO7XZ1-hVqWuiGTJ8u_Y0NBjbh3uOeoPTUwxexXIpACoUo4j60XGHKShOjkRLdneh59xBw0ODBfNYQ5vdQJc_5dNTsAx580c9hqezXZsImaZDNg2PLhRfa6nnYOXeTZPU4Xe2UjSbpxuvFxQZj6pZDGJ_DCy2DUjMVEnd-gxxo3nbFOR7C5NNga_uo8-H_lQx_MGgLNgoPLKN5R1UKCS27mzc9NbsD7F8em0FlZMQSJiR87hQGicL7D4qU4YoU3R5uSLkGbd3aaRTBg-mkbu56Iog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظ
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83212" target="_blank">📅 20:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کریم سوسکه چی موشکی ول داد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83211" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">میثاقی وقتی خداداد تو پخش زنده از کلمه های "کصخل و کصکش" استفاده میکرد میخندید، الان اومده میگه کار خداداد زشت بود نباید فحش میداد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83210" target="_blank">📅 19:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=k5SMuQZqckjDxbJqcUbarPIhqqgiqwCTkEbtQu2yABrRhsRjDHsnM-zDWiEtrRELQ8lqcapsmKCrHeeIjNVyGgnJD491OBCShzmFNkQHkTxcIFoLfEiCzMJ7Xz2A_lxHqydbJoHoxQflfW9-q7x4jBv6l_tWlqmmaVWDi-wrVulZLho9YPFikUTW3Zb8q9IB_83Wswou8k8Re9MoDCUaTVhQ1hoi5xIayKgZI2E-F8z299P99HTn3QEKocAusaJfn6_lNTD24wbnq555XtgaVCOo72ODxtP1fksbR4z8tY7DSS_qE1HRjyfT1EiVgmEN7LPktRSIkOn9JZkBN8evrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=k5SMuQZqckjDxbJqcUbarPIhqqgiqwCTkEbtQu2yABrRhsRjDHsnM-zDWiEtrRELQ8lqcapsmKCrHeeIjNVyGgnJD491OBCShzmFNkQHkTxcIFoLfEiCzMJ7Xz2A_lxHqydbJoHoxQflfW9-q7x4jBv6l_tWlqmmaVWDi-wrVulZLho9YPFikUTW3Zb8q9IB_83Wswou8k8Re9MoDCUaTVhQ1hoi5xIayKgZI2E-F8z299P99HTn3QEKocAusaJfn6_lNTD24wbnq555XtgaVCOo72ODxtP1fksbR4z8tY7DSS_qE1HRjyfT1EiVgmEN7LPktRSIkOn9JZkBN8evrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ سیدنی سوئینی برا یه سایت شرط‌بندی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83209" target="_blank">📅 19:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=onO_Qoel26U5RrBUu8P94wjQgE4YXwYsgkQMsUPisjaC-hgGeDx7rdzEeazLyATo_XxhIuT5NMZy6letMcpeNhQM8LTt4Q9p_NxooJ583LIZv-Yhz0DDpfK1oAlrp6zM7fzcv0q0E4LZ6ytJU0zbj47DtdXKZStEidWkUV_aQbYTVEnoT97xlW0CYvzuyAptB3OiQng84PskOX-F2c2JdAEMTznRKHh1FZaZHOBkloyA9cpCdtELDbjoVbrErV-9YhP3crxpvL7bvuKfprlV0kI1u7FT4cA3iilWet3wPDTfbCq6FduLHnDjrU3ZjdNnJrUznOcJP4dSWDGagWxjSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=onO_Qoel26U5RrBUu8P94wjQgE4YXwYsgkQMsUPisjaC-hgGeDx7rdzEeazLyATo_XxhIuT5NMZy6letMcpeNhQM8LTt4Q9p_NxooJ583LIZv-Yhz0DDpfK1oAlrp6zM7fzcv0q0E4LZ6ytJU0zbj47DtdXKZStEidWkUV_aQbYTVEnoT97xlW0CYvzuyAptB3OiQng84PskOX-F2c2JdAEMTznRKHh1FZaZHOBkloyA9cpCdtELDbjoVbrErV-9YhP3crxpvL7bvuKfprlV0kI1u7FT4cA3iilWet3wPDTfbCq6FduLHnDjrU3ZjdNnJrUznOcJP4dSWDGagWxjSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83208" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83207">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlkzOI-tiRSaoxU5KjWOCpksfVD8m_al8N6Axj_HZsLogypToVHWkm50xW2RLJQHvEDG2uiYuO4BZyyOhOxR4xuxqbNlFAJCmftKE-81wdUgZyuLtpFq4ZRswD7YGs8K8nTxJ-athhlmPKA1W7dmr3mbkY9SXJRi1WBBmjgUuAUlsfsUVSMKnEz_ZxPOnoZq7-FZbidHbxYF1GTq8yyt2Wrrf7yPQtZ-7RJ-gGO3hDvkNzkrkQfhj1OjzfIevuZUnDdBtgedaaRg81Q6vXKNB4UQCaoBYW17zmjj0m1y3qxM3BevBRyfdjA3o3uIoclkyJnr3C4AtMSg3iImjuQUSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بونوس ورزشی ویژه برای لیگ قهرمانان اروپا در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
🅰
18g
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83207" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83206">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ7MujObMMc-W1qRnHtvqwtc4b5w7a9pGQZfLdqBLgLC8-aly74_WXwwH6-vVNI4rUz0okuxRRABq0Z1d8lEavKcS8Wr4UrTMGWI4HKf9V-nexxj4x2rKN2p-cO8KY2OzqxKgPDOgqIG8Tlw5PDalHgaHbmtmkSMmINg6pDpO1LX3gAxVDii2S_zkEAkUu5_ZYXhGiuLU_Gqkusx1ECvoIrv5YuQET_sAoNgmDvW0jQ7yXFNf49V9ge0uyl6peyKz2JcOsIBU_Rwz2dcl_TB2XrCJFD_PE7KnuQEmMRnitpL1jp3ji30GDXut-LsaCH3sWJ7tyLEd2RoBZ-MeUOO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت هرگونه تحقیق، بنده‌ی حقیر به هیچ عنوان هیچگونه ارتباطی با عوامل این کانال و به خصوص این محتوا نداشته و ندارم و به صورت اجباری و تصادفی و به دلیل کمبود محتوا، در این کانال ادمین شده و دست به انتشار غیرعمدی و ناگهانی این توییت زده‌ام.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83206" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83205">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مثکه پاکستان میخواد پیمان مکه رو فعال کنه و حوثیا رو بزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83205" target="_blank">📅 18:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mip78tcBqCcHBCZEWCtthOrDHn1o7ZqQvdnXdU1RH6dYGU7pHV21OI1Ng5hM4it-_MMMQcQF7yQ0iFN7yEjv9uWPyI6D-L2l0uQk2bah32OVg9GLDMmqM8uT4St30UTxZ1BJN6BtMxT6vkrTCLARrZ-b73iWVYlax21tcxhHSb087BwX0KHYdckVithh8N9eN5R3vPhQYQLmyISHonij-WSV-sZ0lceIGca0ilqBKF7WZBNrV46NrpIGls3Iv9pmxiLBowI-my_h_NR73QXSERD_XCB01KhU49ZoVPZe60E0xUaZEC-HZyLI-rIwRbE87ScfACmLeD6M3QQMOmSrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به این حرکتا، همینکه تاحالا اتم نخوردیم یعنی هر جور حساب کنی خیلی تو سودیم پسر.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83204" target="_blank">📅 17:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565302292d.mp4?token=S2WMVYa_vl3tPZbF_YcYBoepbBjhfxckgoE6VLH5AxcHKjG_IY5EObaz0T5j_lxU8_yHzrMrx1ROb9t0LA9oGJWDpOSs2kz5x0IQnFLFAwkGtG0HcbPsA9rrgq9q9ewjsVtpSg8FV1GAzxGEeNlNiwhDSwoCpVmT39FEmbJnEyXLXe04v7WisDGG8mRz-LCbG0HCh0xiOrcC3V7HnNut9HP1mQaQ8ga75NS_WzVTq-_NjR1Mg0KdVsWJh6V25_FWPAYN-QupQANUQI5GhrqBPotjQVosNU2oH7riaKzqrnju_k29VEyacKWy6VhLB3wu2t6qBEMpzY7h2g_Z708RQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565302292d.mp4?token=S2WMVYa_vl3tPZbF_YcYBoepbBjhfxckgoE6VLH5AxcHKjG_IY5EObaz0T5j_lxU8_yHzrMrx1ROb9t0LA9oGJWDpOSs2kz5x0IQnFLFAwkGtG0HcbPsA9rrgq9q9ewjsVtpSg8FV1GAzxGEeNlNiwhDSwoCpVmT39FEmbJnEyXLXe04v7WisDGG8mRz-LCbG0HCh0xiOrcC3V7HnNut9HP1mQaQ8ga75NS_WzVTq-_NjR1Mg0KdVsWJh6V25_FWPAYN-QupQANUQI5GhrqBPotjQVosNU2oH7riaKzqrnju_k29VEyacKWy6VhLB3wu2t6qBEMpzY7h2g_Z708RQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فان‌هیپ‌هاپ در گذر زمان:
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83203" target="_blank">📅 17:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارم نیوز: آمریکا در حال بررسی حضور تفنگداران دریایی خود در برخی جزایر خالی از سکنه ایران در اطراف تنگه هرمز است
در صورت اجرای این طرح، جنگنده‌های اف‌ـ۳۵بی مستقر در ناو تریپولی وظیفه پشتیبانی هوایی از تفنگداران را بر عهده خواهند داشت.
هدف این طرح، ایجاد نقاط دیده‌بانی و پایگاه‌های لجستیکی برای نظارت بر تنگه و حفاظت از کشتی‌های تجاری عنوان شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83202" target="_blank">📅 17:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=fazP5sox8Q3MyjG5rALz7k-rkBlU0I2uYMyAkXmMp_DfjaQ38wl-gEVzwW-aN638J4KRoc3jlfijrL1nu44Vn8zpELOL_Nau6Bozwd-vkj1QqUG4q-2cAQlFJ8O__ay6qgZMcLrHQ1DkweUKf7oYR7T-wndlgSeerfZL0jsm_Si7GLL2GeM5LAdlMsKxigEoPSu-XkQodh7tqy6gsvozRUyfE4wdfSbbfGmFYNfSZH7xs78v70kJQIK7yNgOByHaeJIrgSLJyMytOiSeQ6FmUOSCQEiKMUDm577z_pTx6PxoNh5UbIWqex1Bl3DTfaJdnQfv2gdmKOZ2aH5J3flq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=fazP5sox8Q3MyjG5rALz7k-rkBlU0I2uYMyAkXmMp_DfjaQ38wl-gEVzwW-aN638J4KRoc3jlfijrL1nu44Vn8zpELOL_Nau6Bozwd-vkj1QqUG4q-2cAQlFJ8O__ay6qgZMcLrHQ1DkweUKf7oYR7T-wndlgSeerfZL0jsm_Si7GLL2GeM5LAdlMsKxigEoPSu-XkQodh7tqy6gsvozRUyfE4wdfSbbfGmFYNfSZH7xs78v70kJQIK7yNgOByHaeJIrgSLJyMytOiSeQ6FmUOSCQEiKMUDm577z_pTx6PxoNh5UbIWqex1Bl3DTfaJdnQfv2gdmKOZ2aH5J3flq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ویدیو دیگه از عملکرد قوی سامانه پدافندی پاتریوت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83201" target="_blank">📅 17:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_or6uTArdT2pYm-XKwNrdax8lBSI5XSqNYvDhBZgq-OWmJLPgefojNaW397O0mZphMBNQjMdUKdJA9sxWn-EHdIJ2OSKtGedcP8dk27rqigfcjN-tsFy5T1CpgUJdYmR0VgV0SpO_IT-PcP25elNEczIOSfzPDn6f_GFs33iDj28TPOIy12nlz-0jZYUsHBM7V9rHjGWw0b8MMiNbzRrUnG_TFRxOwnkkHHL-zQmHj1x5-jmUPjxKGevIS7tWSYZYjqpuGzuq8_7Hr1BHlUZdlGHhwN59JJV1MOWs4vx_SUmLGRsG8LRzcNnIE4n9qcxM2d4BLhYI3kNg2AmeQbuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد محجوب ۲۵ مهر ماه قراره با لویی سادرلند فایت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/83200" target="_blank">📅 16:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83199" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83197">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7_puVMGtb0yDQWwZHvi8EaJCa_b7sHcNQ0pHw-hYroZdcbI88-LMOlK54uAQzJVHkRFZg3_dZmTxpsOg_bMpvvZC4u9No94Qp56PikTjryY5930BdRjAEzX-6P3hTx5nYjVi6XJ3lv8YVg10MrWj6rbtz-q3hn-0t79f4RuaZBKdjF4hsAdCngzm2erpdkwzEaJeCwAZicjNWZMyECmEuV6dQ3_ufBDOaOvk-NDpUBaeCnmlwwKukp-cVwk4Q2lgbotRcOmAo_JE4wqfsqnDhHd1hr7gFL5rpdqWhFheMaRvU1saAIbgrDj3PNP84Pxd8MR9OUHTKtsLAN-HClCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83197" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83196">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoJdOQYJHnYB-xSVHjktBlH-4Ry4FeWXUPcFNYjAQjUnQYRin5Njt3zxGiPrv1wjlOmif21Vg0FurVOgD-0YH9zLjsBG9C2sQo3SZAneG3SlRwc3pytQ2S-9pSaH8j_LZHFsYGKieMFy3xlGdSEWQgDYxCbdzLCWaElEuOiITTdXm3pMuxvpC7D6jnR3I9nChQ_raunzp6GThVly-AK9gwoZHgy4iQ2nnkcrJSmqpx20_SPH069CFrTvaeCxzj8Ptl3ajo__LFIb3rwAeTtFwLD63PZOTniGWkses7HMhAwHyxr9052NePyNYqkueAg1RZpfKS-RTRyPCQf0dJuRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83196" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83195">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_x-0bf81v2ZqDGI5yHfpuO7xUrAtONE4FqB4bQsWrJxrzVvOv9nhpeSjd59l06PO39GfQta8rfE-EUiGkjnOvMOIKqOyRTlLLuTukaNGMwWj2jAGt815CX7sc9Bn4kq6hObjjNsLthe49XZ2gFQ4l_s-S5GqrBGnXjn2D9lX1foEiM_375hVx6g63gAT14SruC67wA4O1cIh_bcqal6OeRM8y0xQyQsnf-Gi514--7hZfjYOZBc-jZrbf6KG5xYl1y_lzkSYDC2vWmOPg91REpjYJjIRk5-lkqzuclmRfBMxtPPNKDv5rKKIf-l4SXTyik8tabyVwsmjAraX-p8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنگ های احتمالی آیفون ۱۸ که میتونید با حقوق ۳ روزتون بخرید اگه قاچاقچی اعضای بدن باشید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83195" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83194">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4yYUlG25D9fv58KzPtbC2sd5LvSjBiMZE3MywWgGyFghu8lIGrIu0U-JLexmDygcwHyRM8i33QaQC2CNts3W9JGxyfg8573HP1w3W6sGSsD6tA_T7tHtZYIi_mTJ7UPQDWqM6Kg_ifHTRP8jzreorq2QpjdhIr5Sr1HaDWokCVnaE2f5gA6m5G9bmX8SGld7seOwKAaKKpPp6gwLusvWdXQQ4J069fnUUwgmJAUIDROaACGnFpRE0L4EiyDTw3IVWeR9JkgIsytiqLvKKytarPsJbanGq4xo59DLxWwumT45GwU_kRvKXMW4y690S-m4NRcaLtydx6nFOIqvH7blQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی وقتی دلار ی میلیارد و هفتصد و بیست میلیون تومن بود.
(اینو چند سال بعد بخونید)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83194" target="_blank">📅 15:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83193">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=ecIWOOqKkUItys_1patDZIpRym8B2s7pffXcr4v-oFjkye4f9RgJLUhTt7cGzLY6hQsYxVmktrOX0uvKkaObYdUNB7XNQrz3KuxYSIKbs93oOGxAu9i7vhMFvzUe3l2z41FtQ9f96u9WE5NzwNSJCSYEMuBmxeJ0qoLvKrk7a9rRCyGDVf9N51-3JOBrpOG-rHpyYsXXbmrHv3JgnxgsVLvg3oAN_Yzx0-Pa79bZFhxM40U5sOZOAKe4DwGTl6e50sSo2dOZcvPE7ARCsgsJEAw8CinPhtasJ5JLgrYlmYLrE0vZh5TjRqzt0jOxJKewi9aHgxn34v9G1vBHLyXUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=ecIWOOqKkUItys_1patDZIpRym8B2s7pffXcr4v-oFjkye4f9RgJLUhTt7cGzLY6hQsYxVmktrOX0uvKkaObYdUNB7XNQrz3KuxYSIKbs93oOGxAu9i7vhMFvzUe3l2z41FtQ9f96u9WE5NzwNSJCSYEMuBmxeJ0qoLvKrk7a9rRCyGDVf9N51-3JOBrpOG-rHpyYsXXbmrHv3JgnxgsVLvg3oAN_Yzx0-Pa79bZFhxM40U5sOZOAKe4DwGTl6e50sSo2dOZcvPE7ARCsgsJEAw8CinPhtasJ5JLgrYlmYLrE0vZh5TjRqzt0jOxJKewi9aHgxn34v9G1vBHLyXUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دانشگاه سمنان درمورد اتفاقات چند روز پیش و تعرض به یه دختر ایرانی توسط دانشجویان عراقی:
از همه دانشجویان عراقی‌ای که هیچ کار بدی نکرده بودن و یه دروغ بزرگ براشون بافتن عذر می‌خوام که چند تا دانشجو ایرانی که حالت طبیعی نداشتن سمت خوابگاهشون هجوم بردن، ما دستگیرشون کردیم و کاری کردیم که اعتراف کنن به کار بدی که کردن شما خیالتون راحت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83193" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ما تو خیابون کسی با استایل دهه هشتاد میلادی ببینیم مسخره اش میکنیم، بعد شما میرید عکساتونو میدید هوش مصنوعی اون شکلی بکنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83192" target="_blank">📅 14:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کیا مثل من نمی‌تونن تا شب صبر کنن تا مشخصات و قیمت گوشی آینده‌شون رو ببینن و پیش خرید کنن.
😍
بیاید بهتون قیمت و مشخصات احتمالی رو بدم تا از همین الان آماده باشید.
😉
این رو برای سیسی‌های ارزون هم که دنبال آیفون ۱۸ معمولی هستن بگم که آیفون ۱۸ عادی فعلا تا بهمن…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83191" target="_blank">📅 14:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhFhOu1rJSzN15Kff7Gqb9U12Mp_PcvkDVeuFSaW9MRJR54p532myzXmvcc6tSdC2_S05mUn79GuHsSRuPKDRa3LRjV0_R-LSuuO2CdVS5OYPxaiY1xVVz_vevBhe18alCry9kUYITemfQrlQnJwsvNL4mZnTXBtlCxIANJaDIzY-JgGeZ3idTODNpk7qAFXonT9il2FRMzfr1Kpc1nufn7LtLzk8ywcr94a9W1IcYZXd7pRx-Ib0PUTx-eh7e8e0ZHjrsU-x8Uozw6DE1JfvFmrEXEax1Agn9zRC0IFyVc-bylPf44nRC4guP2cH2IG25_eA893fXwPJMXMzMIkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83190" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حاجی من از آیفون ۱۳ به بعد دیگه باورم نشد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83189" target="_blank">📅 12:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دلار ۲۳۱
درهم ۶۳
طلا گرمی ۲۴
خدایی این وضعیت برای کشوری که میانگین آیکیو جهانیش تو رتبه چهارمه اصلا قابل قبول نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83188" target="_blank">📅 12:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">روبیو وزیر امورخارجه آمریکا:
از این پس هربار ایران تلاش کند به ناوگان امریکایی آسیب برساند چه موفق باشد چه ناموفق، تعدادی از ناوگان نفتکش‌های خود را از دست می‌دهد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83187" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=nuPCGDdYW9ZuRYVLQlIyX5TIrm8eHgCjz87hJZBITMn9BQkLjfsF9oGETkTPu2WEqYeR7Tkur5WQ_UdJzsqc-HdOW42UpT8xVXX9iyFYMmeVnPhKdZa1xyLWg9QWI1SD5-O1mwAAOlzeASk29vtrMvSqVTzpVdOSve5F-ATnhuzsoSjVB707BCK0wEmM1p4FuEIpvu3U19YPoQvYe12w_zDut4wOQZZRZhvY0wsPpp2Sjllba1dfNZPJrJ744EDhdeDIXjconOrsP_YDXfH9gtEZgsft3KPeXltUDXfz4mUKuEon5UrhUfpGjii8ENM-aQ0AG-4hi0JxA0IRULzxXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=nuPCGDdYW9ZuRYVLQlIyX5TIrm8eHgCjz87hJZBITMn9BQkLjfsF9oGETkTPu2WEqYeR7Tkur5WQ_UdJzsqc-HdOW42UpT8xVXX9iyFYMmeVnPhKdZa1xyLWg9QWI1SD5-O1mwAAOlzeASk29vtrMvSqVTzpVdOSve5F-ATnhuzsoSjVB707BCK0wEmM1p4FuEIpvu3U19YPoQvYe12w_zDut4wOQZZRZhvY0wsPpp2Sjllba1dfNZPJrJ744EDhdeDIXjconOrsP_YDXfH9gtEZgsft3KPeXltUDXfz4mUKuEon5UrhUfpGjii8ENM-aQ0AG-4hi0JxA0IRULzxXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83186" target="_blank">📅 11:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دالر ۲۳۰
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83185" target="_blank">📅 10:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHSY9mZS5VskH7671Z3at8YznWAkRHEJkHJuKjytj5Y8fg1bsH2K_LnW29AjXuf2YfZqtvrl_5xj39cZEi4cvwnPmyctc5H7iAhib4BgplHgQmEOikM6hcMLhVPTMDU4tlP9FRI4c2_KWynWpjK-Wna2y4YoAKkMiQ7H5ZATeqg2TJ4lobu_4FXU8QbObTNdYM3LW4nuU-qvb4wWZBgCCAhogJy8CImpJO2alXeuddI-6s2jBHQfmLqs0Zb6cnEFo0qEGyk4zaJn5S93f8RBxcQvD2te_gVjMVz65BiWIdCtgwuPRFcT1Szvb9QGT9E_-Rk5okI_QXr8Z7k6MqH9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83184" target="_blank">📅 10:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b7d8831e3.mp4?token=fKI2bluX36WTbrKvPvTSaDeWzwTu0xfPMSKOi8SkbpfuyrdurlXI8tHM_MvPzeX1JenP9_Ioy7V5rAJ9gdRJPGoDoYVVIxdXhkwsNQPCAVmsp205YCoRuqkGIv8TlR6m5Iyh0WKRjPq9pa75Uz7lIagecsZBFSzq0TnVQCy9G6sn7Xj5pXcUum2MLJIv8LZHnTF8nCdh_k1R93VAtH8ZZY-0abNpgkCXTqEhwab41WYQzngMwnWIsEl7bX4wjmsTcBAURxS24c2lA6bDy6nEZ3mtI-Jx7xLJUqlnvPCyB4KHKG-UfKB2l9eSEHslmsaZAMu0DaDU8i7Nd7YP5nls1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b7d8831e3.mp4?token=fKI2bluX36WTbrKvPvTSaDeWzwTu0xfPMSKOi8SkbpfuyrdurlXI8tHM_MvPzeX1JenP9_Ioy7V5rAJ9gdRJPGoDoYVVIxdXhkwsNQPCAVmsp205YCoRuqkGIv8TlR6m5Iyh0WKRjPq9pa75Uz7lIagecsZBFSzq0TnVQCy9G6sn7Xj5pXcUum2MLJIv8LZHnTF8nCdh_k1R93VAtH8ZZY-0abNpgkCXTqEhwab41WYQzngMwnWIsEl7bX4wjmsTcBAURxS24c2lA6bDy6nEZ3mtI-Jx7xLJUqlnvPCyB4KHKG-UfKB2l9eSEHslmsaZAMu0DaDU8i7Nd7YP5nls1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب سپاه بزرگترین حمله موشکی اش بعد از ۱۷ فروردین انجام داده، این وسط هم پدافند پاتریوت آمریکایی اینجوری داشته موشک رهگیری میکرده در صورتی که اوکراین بدبخت بخاطر جنگ آمریکا با ایران دیگه ازش بی نصیبه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83183" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83182" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83182" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83181">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7U7oQwbt9ffF-p1-lDseK7a96ytjn53cT9pryYbQDIetEP1fEkc6tjGpqrOSoY_X_4NQM-aI6FhQ-aULLhAIG_v4jjkTVQTZSknj6tm6mW2C_pDALMgR4kCPzx0Xy_u60FWf4BB5ivkkZKLP67mmr__c8eoN594AVAJGbhslME60fldCCatYFKmHHF1R3x805r-QrUwvO17wgvvcxZnCyAUKwaECPMm_VWcRFiYXawweJ_N7FF7OjCN13ubN-8gXhtn16wIzE-NXNnZUsoSRHe7ZVkgxgJyPDK3O36ur1nhnkVcKCYt5btPx0T9vqTOQAtsqwQztr7B03gVtdOPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r18
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83181" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83178">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE5Zd81ZiVB-WFjZHdkASn397L2BdrGmFy9SUkLs41eFnOaNLp45HHK5J3pbEUqERbbxIqAS3JGC88mMsUdn_Vgk-fibjRVhvVNhDEsuz_eKD17O_MwyHC1OaoHCrfr5Dsnf0Lj6_73zVXuXOPpa4VtyS12fSRKkErc98t__ChajgwZrRqULD5P73zO6S0R--i1XAHGIC2U4jHHSXHoc6sx1gST86HWWLJiOiyPm4i7fcH0yvqkYcFdYxuoiOrwFawQkRzazCYnD_rVZGY3DiupjRoDTDu3BvRVVtkvFDfvyIWcIUjqNlMFKUA4h7uQoVF643ybNJux6hd0jxZI9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیر تو جنگ بابا جنیفرلوپز ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83178" target="_blank">📅 02:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83177">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یکی از این موشکایی که میزنن اردن کسخل شه بره بخوره اسرائیل بخندیم</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83177" target="_blank">📅 01:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83176">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آمریکایی‌ها مثل نقل و نبات دارن پاتریوت شلیک می‌کنن
به زلنسکی که میرسه میگن نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83176" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83175">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">من حقیقتا دیگه بکیرمم نیست چی میشه، ما که بگا رفتیم چه کمتر چه بیشتر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83175" target="_blank">📅 01:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83174">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">۵ تا نفتکش ایران رو تو جزیره خارگ و جاسک زده آمریکا.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83174" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83173">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">۵ تا نفتکش ایران رو تو جزیره خارگ و جاسک زده آمریکا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83173" target="_blank">📅 01:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83172">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جمهوری اسلامی هرچی داره تلاششو میکنه قبل انتخابات آمریکا جنگ شروع بشه و هی حمله میکنه آمریکا هیچ اهمیتی به حملات نمیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83172" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83171">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5D237zYmAznfutymGPnFe5Pvqz6OcaKFT4mTb-R-vgTTtygVkO2Q0TOIbi3MD-5BSfSQcyKmbZsZCltiTX9Yj579xPVSERhvjSgpIh_SN75_9VGnXbQ7spbckSqehWmwLaDSMSDA7vVt7I4rkgkrimXWHukYjI3WBSTl-58Q5lfOaFa2CDwnPeKYChg0YCplMzyjdQbR4n9ImQmQ2zvXTeALWckfb_S8anGmLm9JBjtWcyVe3tXZ6Y6IjNJvxXJzpqm0n8W56H6EPWPTPdXjVNBmTqiqsmRBIxen8gJEfOe9bb_cuFR0TT22KyMbxb_rlpyH47kyYcrMkV0LRDoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منیره جان افتاده دنبال کون مردم از کل تهران فیلم گرفته، اگه قوانین کشور درست بود الان باید دادگاهی میشد بخاطر همین فیلما.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83171" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83170">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار فرم های امروز:
🟢
2.675
🟢
2.104
🟢
1.696
🟢
1.77
🟢
3
🟢
2
🟢
1.26
🟢
1.56
🔄
1.9
🔴
1.62
🟢
1.616
🟢
1.416
🟢
1.4
🟢
2.4
🔴
8
🔴
1.5
🔴
1.3
🔴
1.6
🟢
6.7
🟢
1.856
🟢
1.57
🟢
1.74
🟢
1.495
🟢
1.28
🟢
1.2
🔴
1.52
🔴
1.736
🟢
1.925
🔴
4
🟢
1.43
🟢
1.89
🟢
2.485
۲۲ وین
۸ لوز(۲ تاش کاملا ریسکی بود)
یدونه برگشت
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83170" target="_blank">📅 00:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83169">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwygQAQQmTlbPtWby5rcs2imZjS32FzPP7mhg0Op0dYSLJww_KvEqsnPUgsaGnFESdLxCiW5Ddh7uXu_s4VFB6KFrWalUBetXPC7VnMf4fhk_oaWZgSAMBi2GR-1DYAkgCaT8zVcYUSlGbR-ZWqQecL5HVqSg50AE_YC6hlT-QDlrTpYNvfqBGFRPLlclnbTaLBsFQJ9PoUAFKM2Am2URJtq96DTF8Eaqav1lKn-wF3UO2nItRBBNl49nxQToB-aMQ4gDxqjhjB6jWgID2ViPiI6QpJ37q0gJfFNV-obW14Tkty9miLfTAlj9ZhCivF6IVwuTf2yk7RSFWQw1we5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایزی وین ترین فرم زندگیم</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83169" target="_blank">📅 00:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83168">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">از کی تاحالا پرس از بالای سنگین و استفاده از اشتباهات حریف شده حرامبال</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83168" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83167">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وقتی آرسنال حرامبال بازی میکنه ریده تو فوتبال
وقتی رئال حرامبال بازی میکنه میشه کشنده، سریع و فرصت‌طلب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83167" target="_blank">📅 23:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83166">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">من بشخصه فن هال سیتی ام، چون مالکش تورکه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83166" target="_blank">📅 22:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83165">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">واقعا فنای فوتبال عقب مونده ان، مخصوصا فنای بارسا و رئال، یکیشون جودیو مسخره میکنه که تو ۲۳ سالگی جزو بهترین هافبک شماره ده های جهانه، اون یکی پدری رو مسخره میکنه که تو ۲۳ سالگی بهترین هافبک ۸ جهانه، تهشم این دوتا که هیچ وجه اشتراکی ندارن رو مقایسه میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83165" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83164">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb4wtxuJ99C2-4Q38MhDMutmuWd09_EhmVfMkGO7mU1IOE7g_YsQKF0jVFne0rwO3SdGVrpy2SE65VMn7zW8VYNHmT2hcvrjEm4ob3UyNHSnb9_ysXZ7Lb9gKcFwqyv3ElmsJxmRjPu9xykkafUidiMUi4ar9arjT53Ixvbp9PRsCoRacHUFR0tdTXhf_jRjyHDGjUmpdU16NBSn6tbSFXMqhIlq4zd8Vpa1PRVMQFyeHRuMGn59cys1yJRKri_YPOEuHLnebu_I4v98TLilgjiPPAJYZdNaOt_TjzMdKbjtm8x6EGOo3e8RyE5fS89csc4E1xx4ZlirUCFRb3SeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من فکر کردم بخاطر بارونه داشتم به خدا فحش میدادم، نگو باید به ارمنستان فحش میدادم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83164" target="_blank">📅 21:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83162">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">به گفته بسنت ایران رسما از فردا ساعت ۳:۳۰ صبح محاصره هوایی میشه و دیگه هیچ کشوری حق نداره با شرکت های هواپیماییش کار کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83162" target="_blank">📅 21:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83161">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کم کم داریم به فصل شاهکار هودی نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83161" target="_blank">📅 20:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83159">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کم کم از ارتشی که قاسم سلیمانی تو خاورمیانه ساخته بود داره یه خاطره میمونه، همرو زدن</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83159" target="_blank">📅 20:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83158">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWzmoQouQ7ZUFDmzB8FEzksW2-l6kFJJZTzcVoXffCVPGAtjrT5l2BgC15LLlUArnKUiIN2AgfuM4qzZSYIeZvotGwllCAvpOqiJ2hpu4269y2VwWlqmjeNIKcVY0cOThxo80-lU-4kEwQpIs1OyzrXbT7_5lGEpU2Eoj3BUtSOZStbJ6gy086vmFkRoP_B2gicCXOy1Yyww4jSNZUXGQYXW-W4AUH822o3xc-zxub7RP2ceM0CHiAewHYViMmtw2DG0wVF_dxb3njyUkwe1lcvMU6b6S8gNmQWzYpGKXvap50eHr2I1VuM8H2xxoRsKl6bsP9buG_I1NeyWL3G3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بین نتانیاهو نزدیک انتخابات اسرائیل و محسن رضایی نزدیک انتخابات ایران تفاوت خاصی نمی‌بینم حقیقتا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83158" target="_blank">📅 20:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83157">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCEO15D5LFTJ5ABPYv7keO7XgPZ-QVHKoh74EpUM1d5P7YD-A0AnEdDT5eL8r5DclX5gt90SsEl_FxEe6CAhCl8ASi6dlIEVjrD9zltXBjjaj-PTUGn01tQ76TDe2igq8GuoCC_tV58wFY6buWRGgyqQDv4Tzp81z2FqocjztLC1J80Dn9RBZWDZiWkWeTnCGUlVr1-m3S3BkM4HRP7XJyp8PBgmzD4oA635fT4YMSPHAB-ty9HWiTB4mh5IuuobH3JyEaZGeXdiMJEJydPRjBly6QCvQRCuMKDdxe_05CajvW-8gHN9c3cJdXHEP7tq2CRU_CfhYlEKU5KgxG7NbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین جان خیلی عذر می‌خوام ولی اسم این فن چیه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83157" target="_blank">📅 20:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83156">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شنیدم رافینیا و فرمین و پدری کاندید توپ طلا نشدن، دارم میرم اونجا امیدوارم اشتباه شده باشه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83156" target="_blank">📅 20:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83155">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvkWyaXDpS-HS1FA7Gx087HGmgF3HBMMhk5lrWhCizmRbShbjKYqo0X_W_umRglPgWXZng1US-IR0sgYSvvb_xviLYRWMSa4WPZuIvbV5yNbWfhYkYC2wXmpvOvVJ7S-4whtVSDj1D-TIBm_8eIz94IS5fXAWPrZnuu88-I-O8wte5LCMechG9Yz06xHDi9ejJwFdhgB6CMX1XpT4qQy79N4PYHCTM4ekmHwNtG2NCb0A6X-PLoIUtPnguhtb8T7r2_fvduRa202jKRmsBedr76t_BdbPlRYKasYylFDjfHCZ-d30FN97vmyRWL0fmNFIVgCG8Mm3mCzHeQcTeB59g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین جان خیلی عذر می‌خوام ولی اسم این فن چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83155" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83154">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حصین بنده خدا دلش خوش بود که یه دونه حوثی‌های یمن از محور مقاومت موندن که پانچ خفن ترک بعدیش رو با اونا بزنه؛
ولی متاسفانه خبر اومده احتمال داره عموهای یمنی هم تا چند روز آینده توسط دولت یمن و آمریکای جنایتکار با نوار مشکی به صورت جدول مندلیف برن رو بنر
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83154" target="_blank">📅 19:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83153">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سرنگونی پهپاد MQ-1 آمریکا توسط سپاه   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83153" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83150">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله اکبر سپاه پاسداران انقلاب اسلامی: با تلاش‌های بی‌نظیر و شبانه‌روزی نیروی دریایی سپاه پاسداران انقلاب اسلامی، یک عدد زیر دریایی رباتیک و بدون سرنشین کودک‌کشان آمریکایی به دست سربازان غیور سپاه پاسداران انقلاب اسلامی اسیر شد، چند ساعت دیگه عکسشم می‌دیم…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83150" target="_blank">📅 18:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83149">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUNc8cJqX3xoIlSyc2DboBNpHvIubIVgg8E4oRBwTAp8njI1xhaiKQQZ760XObA8-C_bQ2qc4l1Dt8dq65gZ_Y6AcrmuzRyGVPfqfa-VxczMDjqEhv4yTmxy1Y3GAvWFSzXzORnkwuLbpogptLnGiNdDPIyGsBygwjhrj-JIjlP0eoPMBTmg_XMtWuPE0cRkTuMxwpy1kkqecz7VgPBq20th7MKj1rwGK---3al7GsyU9qCSPgVnQPXLUM-oKuo_XRKo7Yr1udYRatH2u1uc8DRYNbeAq_e19A2swWFdBkw36P9yaimkqEZhB3OBVrk8ZcNuAg0JtTPE_jLtfCHJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اکبر
سپاه پاسداران انقلاب اسلامی:
با تلاش‌های بی‌نظیر و شبانه‌روزی نیروی دریایی سپاه پاسداران انقلاب اسلامی، یک عدد زیر دریایی رباتیک و بدون سرنشین کودک‌کشان آمریکایی به دست سربازان غیور سپاه پاسداران انقلاب اسلامی اسیر شد، چند ساعت دیگه عکسشم می‌دیم بیرون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83149" target="_blank">📅 18:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83148">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GD1JG54bh-cSRgd1pTh12NxQVFEe9-36WP2qY8TRsyf4fYSmNbORtiBkhyhPDdOZ5_Miam9TjwgSTrHe0ca4m2PgvuWBfZbQ2Sx2T9SXYvVWmdVjd59EwdcJC-11fzUcGAaLjHks9tI0JZJZBH5QZu20_6dJxmY84MBs85zmoVIm0LzRzZpqHKZbAJhLJpHr6qY1z79fHoAWrYp9OO8EfsgdNZr9iXUneJgFdFrYsA6homLUgB4NjzOTEqxhoFYBomlONJZ_ATsq5soqJ-iSsCGI7yaKdfHSPddjDNwZR9cWA6tgoJ2_Ykdr0cV_m-fLQX_dNzh2UPlmMwFqn7d4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه می‌خواید کامل اثر بالا رفتن قیمت دلار رو درک کنید باید بهتون بگم که با این قیمت دلار الان یه Gulfstream G650 ساده اگه تر و تمیز باشه حداقل 10,350,000,000,000 تومنه
💔
🥀
(آهنگ ای غم بگو با جوانیم چه کردی اثر استاد شجریان)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83148" target="_blank">📅 18:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4U4iFF5_AmCjZUCpGrYU4OT212IjduwTr_rMaMf1FeWDCkBcsjx_rCuMC8aV046Dm9Cyz7sU1bO78Xj-DmhzY7t4yR4MCsiVPtNWsdsSCrlqpfpCrL0X8x39JjDoFLIUm2RS0gvvUYtGFViM85UcfdChLVooyOHbz4sAWQivjSofr9LnsRiw7OIp8VexZlY5RjjPM6SVy_MZ4w49DOxpLq2TcOfbVb8MEGs5FfMH73zk6p6kZx2XI1Eeh5XTTgOt5nr0FETpHPjIC5N4Ect5YOHOUFzGF5lg16q7Vl-W9EzBAxRet0mRC0EZLYhNDdNuxbUNV0v__qDsHSFGzVYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داکتر بیرانوند حقتو خوردن ولی تو فوتوشاپ جبران کردیم واسط
❤️
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83147" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سرنگونی پهپاد MQ-1 آمریکا توسط سپاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83146" target="_blank">📅 16:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83145">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پزشکیان بخدا ما خواهان انحلال توییتریم نه رفع فیلترش</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83145" target="_blank">📅 15:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83144">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtHfJ4H6UU_VxSVTKU0iqr_eGUQ0RFy70rSQQua9llR9ZDpgsVafzxM2zfEGlBZTK4fXwW1iyIYG3px3FI-KBJp7nnx0dCfbm1GhlxLfLZKPUfoGp7qVM-QlqXz9GYzjNdc9CP3ymzZi6mKe7a0SNLlHN9DvzHCc02xB5BSxuna5_m3g0sb5U7n4n3J9Xf5rxofBjSINtBHruJ85tEqFe1x87j2fFlI5ZNkAh1G_nGX28VzLaDg6ceKIIUq_kAqz8e0cPRU--Z68ixmVbNa7-JoWe8vXkW2b8_xVg1VsHCvVv3Jte97MmHO4MAlwzVcTwl_SQ5GdROSGnEydrkewcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج این تو کون نروعه رو هم بستن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83144" target="_blank">📅 14:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83143">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWlLJB_a3wiaaoSxIeqEyer2w-iOOqbStSB0xe5s8iSrVoA4hTKyK7e7opf58Yoom-PAK-5gJQNs-ri8b0D-4Ojtz5QjatBwMRiMlNZYfIhezMEyJkOmP7pjhvXA-C7GRDQO07AjpXJ4lCJQELDN6_mVEhGkm8ZCB6-I5k4xCpGNUuksK5v6YSr1TxvT6sh6wEdhNci5MxPfQ3nYkBlGZbeEZ0JTtCy9xMaztq6lTVbDcsMOWfcGZHURVzLkzPF-RGvu-E2J0SyBAkyfgwfCsQi7qps5IvDzRqK8aYzRIgbOVH3NcfCXw3BaBwlXbbdpa-jkGQBf3xWmYEKSn6Cy2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگانو بزارید بالای یخچال دست گوشیش بهش نرسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83143" target="_blank">📅 14:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سامان ویلسون درمورد معترضان به وضع موجود و حمایت از دلال‌ها:
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83141" target="_blank">📅 14:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فلافل قسطی ام اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83140" target="_blank">📅 12:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83139">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0d6cae38.mp4?token=emUlMzjKgl7REiRUNstCUtK-vY55nhWXncYisRgD1p16kqrMPutW9Zh8UsmJcOgoAyG0WeYbfFzsPMGX9UIPxNGiVGgtmSl8yC7o03z0CuKkUNd_lwEEcN17YN5eVKfAwfrTu9FQhId3ck5XP_RMxnNEw_4CvRu0wefsS7FsK1PQV49u87D434p-fL3hAwYwURyLYN4iLpMGj6TzgnpW0QP4EJ2iVQPiXAMvGExT5faJE1Fd3X3x_B1dsfIXYNXX4htzg8TMQxjAFVwFv3MG1a1O3-Rrn0-0hyau025DcNmDX1rRsDCNnuqmAhGoqJP5nQ0FetIOVUj71mK-EBprZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0d6cae38.mp4?token=emUlMzjKgl7REiRUNstCUtK-vY55nhWXncYisRgD1p16kqrMPutW9Zh8UsmJcOgoAyG0WeYbfFzsPMGX9UIPxNGiVGgtmSl8yC7o03z0CuKkUNd_lwEEcN17YN5eVKfAwfrTu9FQhId3ck5XP_RMxnNEw_4CvRu0wefsS7FsK1PQV49u87D434p-fL3hAwYwURyLYN4iLpMGj6TzgnpW0QP4EJ2iVQPiXAMvGExT5faJE1Fd3X3x_B1dsfIXYNXX4htzg8TMQxjAFVwFv3MG1a1O3-Rrn0-0hyau025DcNmDX1rRsDCNnuqmAhGoqJP5nQ0FetIOVUj71mK-EBprZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83139" target="_blank">📅 12:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عارف، معاون اول رئیس‌جمهور: فیلترشکن‌ها اشراف امنیتی ما را از بین برده‌اند. در جنگ‌های اخیر از این مسئله ضربه خورده‌ایم. تحریم فناوری و فیلترینگ در فضای مجازی نتیجه‌بخش نیست.باید با فرهنگ غنی اسلامی و ایرانی در اینترنت فعالیت کنیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83138" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83135">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40085684e0.mp4?token=pXsPvK81KieK8iP883NJOvhsXcLuo6Tg1-84h5QsYS-VHnoDw6brup8WP3dGUvVesL_Sa25LV7VhPQahHdbQQ9yVML3EbWmlWXTJJnXr2eAwYOGjP0odmAHiKRW_xQwWjd0xX16SYE-NSBw7v_QEGPz_yzqz8UJbGwp04FHssPONLkB4z76h7zI9UNBqLwra7SDMzbEOP6o4iYLPjoml9jAArV32x1dtoLM7E3P_7bI8Br0KTDMaEaZpeX76Hi4QfnzH-E8hHHAWtBtEZJyakfM2K1I77bVFUl8-i3oqtwbbwIoEQvhxafwaOi6qX1YavwMWepaZrfMP-HuI33IQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40085684e0.mp4?token=pXsPvK81KieK8iP883NJOvhsXcLuo6Tg1-84h5QsYS-VHnoDw6brup8WP3dGUvVesL_Sa25LV7VhPQahHdbQQ9yVML3EbWmlWXTJJnXr2eAwYOGjP0odmAHiKRW_xQwWjd0xX16SYE-NSBw7v_QEGPz_yzqz8UJbGwp04FHssPONLkB4z76h7zI9UNBqLwra7SDMzbEOP6o4iYLPjoml9jAArV32x1dtoLM7E3P_7bI8Br0KTDMaEaZpeX76Hi4QfnzH-E8hHHAWtBtEZJyakfM2K1I77bVFUl8-i3oqtwbbwIoEQvhxafwaOi6qX1YavwMWepaZrfMP-HuI33IQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی بخدا این چیزا تو اکسپلور من میاد ناخوداگاه یاد رضا پیشرو میوفتم وگرنه دلیل دیگه ای نداره که اینجا پستشون میکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83135" target="_blank">📅 09:40 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
