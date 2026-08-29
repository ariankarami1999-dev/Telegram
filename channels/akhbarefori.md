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
<img src="https://cdn4.telesco.pe/file/Lym_dcOQXWsF_VmRN1_gihXvKoSBq_mwDQe0GkDvQevnF1oxcQurBQ6Wmu8wey00Ym0hH_6LlQT9d4LK_DewhnlPj_m85LgO_V7zcxj93fYEhR83A9YxvJmZJrsiXhnNQ1d56jASgwupaHCvKf6-F57xGRqC7X7OlnzFyDQn_9NL-Xx3l7hk7eI-ZGmkkMu4iyznv1h1RSGa8Asux5aP3v0e7NNp_s3ADvpu5l1Ud8UL_2u9pVMLK9mFJR4Tul8V-UVKRVYhRrv34oOYGH7cCmzQ5NA-4peqOo8-SyPrMno5PRKx32CvNXUZ91yBasYXVaDw0EddgHp0W19AIlIJfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-685254">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAQ1NXjrbcKEF-mIlVN5p_LMfYDRCgjHamlzZRmauJTaSNhO0wP2fQ0oXOrSYyB7UiHLUzUIs-VGz0mTtt5GPlOlEOglSujZnsNgjVsdwYWK78dVmckuTLC09WDmDTuLKE3IYaZcJjTuMlvWhg9jb1YzIyqzvZCF1t93dxLT7PbHCydSHhgZruWkKLtJFmHqA31kQ7j4ZBFSbG8qik0SBzbc5nHJecFYggp_qyjfVJT4SqIb-6mzzEWS2Z3jf_nK3WFDjgXDvY4n4OJ9ikMtN5MrmoBEfzrdQ761IHe4o4n39-GdEi9_bbXWDOIgQ4RJcaSjmkePAVWjhFF8ybVimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-vJev6NtZ2PLcDG1T29Xfv7nGbr8ZvfZTSl345IZ752KUl1NfwFmUTNDMhFrlHtpAbgOH0QWxdvfMiEuYzlVTmym0Fy6niVGQQSym0Fr1xGDPORRnz8WyAbR9zDf_2SUJUR_u80_SBTPKSn2dFAmwaALDpHTALEp7bNI9ejZbpH9d_vjBsUqXQA3EUv7c4OsZeWN3rdRObkEIyxOCdtjs3ziIQS_cLlcgzoJ55rUrIRRS-ohz-PG7qdaj5EkHUtfbLViBo9ZYEjoDZBHG08psrTEJ4ZmY1tVui9rPvFbAyxq03_Xgdy2V1MeC83WZUNQxvb_Pm3WzqpsKc4YDzpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7wFsO8VkRoaqrZ8qLycMd6ixx_H4B9BU9OZSRhHUYW5IHmhiQQ2JELd1iPD_zt_UtNbf_P9-9vlA78HkmNzhkeOwjS_g176dpYXHn9XObobVL_kfeHjx_AZT8SMmPLT7GOTYTd34_MFzz1_BydOL-If9RmSNd3V-oyhTPih0mgQgQb27SKy6ZCRBxd2EQF_u0hFrqKv07S5dMm1y8RvS1di0hMaZtv0ZVJ3C0D-MlMbwDOe0BzyASuwnUa5ZqGsCxOmIaOArigkl7FloQOAihpDfZEaLQlT4BYXUjBpoj4MuV_q-HEkogDf8qIQ1q11TxoVWhhIRWgyuWkuSwlUrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیست عجیب فرمول یک عربستان؛ پیچ ۷۰ متری در ارتفاع ۲۰ طبقه!
🔹
پیست فوق‌مدرن «اسپید پارک» در شهر القدیه عربستان، بخشی منحصربه‌فرد به نام «بلید» دارد؛ یک پیچ مرتفع که در ارتفاع حدود ۷۰ متری از زمین ساخته می‌شود و نخستین نمونه در جهان معرفی شده است.
🔹
این پیست ۲۱ پیچ، اختلاف ارتفاع بیش از ۱۰۸ متر، سرعتی بالای ۳۲۵ کیلومتر بر ساعت و ۸۰ گاراژ خواهد داشت و با مجموعه‌های تفریحی القدیه ترکیب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/akhbarefori/685254" target="_blank">📅 14:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685253">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da07fe860.mp4?token=YHudjgE6c6KyX7uyJBsdqcu9_nHaKX-FeAJ12xLS7-TrBa1Uq1cC-TmIKkxitdsy5d5CspA8FPyYlINNFnBAi2cHEzpliXEY6_cRN9_S_ap1gkq31m0egm0RCfSdoqt3K9N0iDE_ID9O1GL8DMqQsbemoQhcmYo4Jnkh9MK68eS51t-fquI2Bg5is4XpljjVqkD9LGlECcXnBJQpunzTTPiGhw-mO6M2reJtA-nLGCePqZtJTFaqUR1F6nZ1YnJ_R6N7UZMtiVvnuCnNGzR49daAh3fCGnYCSfmZKgdwK0APcxUikRHYzd3J4GKdSRjFN1BBjlpDM3vuqtzQKRS0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da07fe860.mp4?token=YHudjgE6c6KyX7uyJBsdqcu9_nHaKX-FeAJ12xLS7-TrBa1Uq1cC-TmIKkxitdsy5d5CspA8FPyYlINNFnBAi2cHEzpliXEY6_cRN9_S_ap1gkq31m0egm0RCfSdoqt3K9N0iDE_ID9O1GL8DMqQsbemoQhcmYo4Jnkh9MK68eS51t-fquI2Bg5is4XpljjVqkD9LGlECcXnBJQpunzTTPiGhw-mO6M2reJtA-nLGCePqZtJTFaqUR1F6nZ1YnJ_R6N7UZMtiVvnuCnNGzR49daAh3fCGnYCSfmZKgdwK0APcxUikRHYzd3J4GKdSRjFN1BBjlpDM3vuqtzQKRS0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
مسیر ساختن یک کسب‌وکار از دل خانه؛ داستان‌های واقعی از کسانی که با اراده، ایده‌هایشان را به واقعیت تبدیل کردند.
🔸
در یک فایل صوتی کوتاه (حداکثر ۳۰ ثانیه) نام، شهر سکونت، چگونگی آغاز مسیر و دستاوردهای فعلی‌تان را بیان کرده و به همراه تصویری از کسب‌وکارتان ارسال نمایید. روایت‌های منتخب در مجموعه رسانه‌های خبرفوری بازنشر خواهند شد
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/685253" target="_blank">📅 14:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685252">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmPb68b8Le-RosUCzys0WLtxFR-gBo6zwIuNztVfB-9sw8D5qAqpf_M_hju6c1HTa0qc6m7yJ46TC8beE3narAg2DPOLakTCfPUpaaz6vaeR7BSF7PHUOnJ11NsJDynOABqXLVuK9sobIYaMkMVAM5fW9jH9lIu65erQyU8CYXpc-cHzFwcBiQ9VO6FmeSeRWall_GsNjoxyjSqdIWWpD_xfVRUeOKFm73FGeuXxIEVhWf1MFDKkbiH2K8-JewOtG6OpKiw4zYCbde7kwqnjfeab9VtdySCU_AlqywYQg3n6If202pZzpu_lki7qKAATevMhiNeBGlEi3xw-658zVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عذرخواهی طارمی از هواداران الوصل
🔹
مهدی طارمی پس از شکست الوصل در دیدار شب گذشته مقابل شباب الاهلی با انتشار پیامی از هواداران تیمش عذرخواهی کرد و نوشت: «این فوتبال است؛ ما یاد می‌گیریم، پیشرفت می‌کنیم و به حرکت رو به جلو ادامه می‌دهیم. ان‌شاءالله قوی‌تر برمی‌گردیم و به موفقیت‌های بزرگی دست پیدا می‌کنیم.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/685252" target="_blank">📅 14:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685251">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45f93b367.mp4?token=CFFiLkFqmVnRBR-UAQVQThcwgVtn-cGdI6V9kZA-ud0hmho_kLOk-a2UnSa_NrZ-XZfQlmsc4MudvfvUguyKR8WqvTmt-icbgrpG8OQO4LlrF0xIz6jOi3J5EY3e0cJ41NgEQQZvObMBxLmldXV9NHWXfywe39DqCQfeKFsozWMgyNhl5_VursXzo2WflMjyk5X_EAfO7LU2k5Z-5IXqyECRTIFlFkpeH_WCjL4dJDp3imuqzarrEl76ASziQBFQ07_tJjff-ez-cxJkIoCTsbjqG3JFvYdnoif9fKuX5oKKh1CqXQGzSKss75mhibS8yVtV1lnHY2ah8IPjl__5rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45f93b367.mp4?token=CFFiLkFqmVnRBR-UAQVQThcwgVtn-cGdI6V9kZA-ud0hmho_kLOk-a2UnSa_NrZ-XZfQlmsc4MudvfvUguyKR8WqvTmt-icbgrpG8OQO4LlrF0xIz6jOi3J5EY3e0cJ41NgEQQZvObMBxLmldXV9NHWXfywe39DqCQfeKFsozWMgyNhl5_VursXzo2WflMjyk5X_EAfO7LU2k5Z-5IXqyECRTIFlFkpeH_WCjL4dJDp3imuqzarrEl76ASziQBFQ07_tJjff-ez-cxJkIoCTsbjqG3JFvYdnoif9fKuX5oKKh1CqXQGzSKss75mhibS8yVtV1lnHY2ah8IPjl__5rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میز نسل بعدی: ژست‌های ساده، هولوگرام‌های تعاملی!
🔹
با یک میز هوشمند جدید، دیگر نیازی به ماوس و کیبورد نیست. فقط با حرکات ساده دست می‌توانید نمایشگرهای هولوگرافیک سه‌بعدی را در هوا کنترل، جابه‌جا و دستکاری کنید.تکنولوژی فضایی (Spatial Computing) که آینده میز کار، طراحی، آموزش و حتی بازی را متحول می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/685251" target="_blank">📅 14:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685247">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gd4W3zOXmL51WV4jLCuJpk5TNpGWoGmasnK_hpoJec88dr4sl_tP8_wKkYywaUD8q4C35dRz2U0X9_fG9O0651ptjNIxBX01ph_JJHHmTaf13RkOGjZ36EtBoJiAt0T0NQsM_HY3W2hixrsNpjCUMxx8Mjyq9CPgdL6ESzuwKYrUm3f0zuD_BNEiQf_8guCwk9XYl0ilMn6zSYiDBsbhtE32F86RExkWMVcH8F_DhvfjIWXWwP-0ay27uI9GPp3ibcZimOKv02aY3fY-fG6qr6qDx0XfobBu9_WTOGmYlCJ_vLoVIVvD0fVK6FWL3t_zDrqLo6dEtVCW19ua_Kr1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKtqRHvK9d5Zjb3TB4KLxx1kLKv6Qo2uas2KKWQlEgeioC-qylg-sa5NDR_OWBltKMfmAmZ9THb2I1FyKAXTm7yKYQyBRugHw59tvrml71Y-Uq15v61LqgDXQ8c_ZPNHULhjFKd4Gsg_jmfnDC8Hikb6sGttml721YxyTrFcAOaobljMnhSFH1Gc3evtObXlF7Cl6KJRgpbeaOmbMhEjUljqaqTdu5pJJMoBglYwehtwI5_gYm9qJzCXXqV3K4rgOgVKrMWc4b-q67vXqSYuETYTJ87Fadr5u45HB2_jl12MYHLmTh8otkqL4DLrnhxP-FZfOderllQGtHXGbeGYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jW5bBMSjuo8QaytZVr4qau3RUST2TPiLQxZPUnmJ7_YpsqcYtm8jCGk1-IwqUsDrRRC_sI7GBzzkiKkpjVaMKd6tVFHSeHYGDq9RnpHArGUpquokQymNC04rKIZfbApY0XbRD3z8s4JZKmCPIuqKQk5BeS-0LWaWCGlNKnHu615KEvUCJx1KsuMahP8HvcJyiCv0OurrPVX4Z-DUVWKwc2XvyiclThylKIrmCPxCPUuNpCE0MEXQQQJUhH35Xp9VGFp_qexpVQ7Qx4r8x1LhxyokC3lIpeNVO4sbxt7w9bmPd4oQl_8xFNSu6yHdmKNlvAv_GncneNt3VTYR1lx0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlic7dhMvXWsx8ApNImc_DfGYmGzAhYT1uMKlmwzLp4oqWzL2Dyfg3B0Ujh-7-UVUkIUWDZw1V4kou4m0qmVLWXDnp7bk6Oy24UkpLTzslGpJw68sh8AHgjx3XcMZV5FAwGBbt6qBQT5ts7ZlBjApD1eF5xsikwEXGqVTFVLWowspvjJy7BBqfrSDmfA7gj9Uih8XM__oVPESIcxvhEhBFmRNmLr3BVVckSsIVkKUEv74wwu0h2TnW3e1h-gwxTbl_-B0NlB41UmoK36JzNRN8w_P-bsYYrEE4O68veIw4uKg2TPVs2yBHV3ZW20ZhnvS5i4GAMa-ZHDfs0jQWF4Cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلوه‌هایی از طبیعت شگفت‌انگیز مازندران
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/685247" target="_blank">📅 14:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685246">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66a21da29.mp4?token=V1esgCKzin2TJ8X5p3q2eQK35y2LxLFweVkTf0TSKeZiblVM0cSq3zfUTxGzVj5fH6Gj46seD12kDfdWIOs_OjuygAgudzTjDNzg9SD_sb8F9IOZ85Ky99Db3d00rM7x_Y0jZOjE23y5oXesWFopD369MU6n8i0U-onmnjO64QUTz3i0pFcuSBf5_foJ7n5V6zqlMR22VW-o9x9l1n6lRAMscpCsk4Wgg-zJRyZMiB-ahwqf4_6p93lwJAceTh8V0slFC8by74NCRzMjhdf4tmnPnTH92v1eEZ6xwZ1D3jxfOp-472jbkzVFI4yqn6UnbCDmMx7EBv-NGUN3_jIX0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66a21da29.mp4?token=V1esgCKzin2TJ8X5p3q2eQK35y2LxLFweVkTf0TSKeZiblVM0cSq3zfUTxGzVj5fH6Gj46seD12kDfdWIOs_OjuygAgudzTjDNzg9SD_sb8F9IOZ85Ky99Db3d00rM7x_Y0jZOjE23y5oXesWFopD369MU6n8i0U-onmnjO64QUTz3i0pFcuSBf5_foJ7n5V6zqlMR22VW-o9x9l1n6lRAMscpCsk4Wgg-zJRyZMiB-ahwqf4_6p93lwJAceTh8V0slFC8by74NCRzMjhdf4tmnPnTH92v1eEZ6xwZ1D3jxfOp-472jbkzVFI4yqn6UnbCDmMx7EBv-NGUN3_jIX0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آب‌گرفتگی مسیر زائران مسجدالحرام را بست
🔹
بارش شدید باران در مکه، هم‌زمان با حضور زائران در مسجدالحرام به آب‌گرفتگی برخی مسیرها و اختلال در تردد زائران منجر شد تا جایی که نیروهای سعودی برای انتقال برخی بانوان به فضای مسقف وارد عمل شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/akhbarefori/685246" target="_blank">📅 14:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685245">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9PfYto4G4et26bOMqB0ILavFV2yI428-MFiZBdbsryimb3IeDmQy4z49HOcT6o5Aw-hDZUUA1fm49ppOEjBMkLry8zQrdnxGuawM7tkGxsFIGIns9nFMZYXwUCpDz76JeUE6WBS3kjKAF9eKvHhqMyXsMhowTj9PXkAE1Ifo64sHHX74nAPnm1ra9EQcTFr48BSeTh3n8qZ3QJAdH9SH6270Wv5B-CpTd6LIdY3HLTU5mOKgUnCOAf0m4SWcnK2H4tphzBxDRAdE5LxC3MJuagJIDpZ9_ZnAcWM1jmnRLQTlp3YclAtW3UT1NV-PfY2H9Df4zR8H4MRBbSWuJHHXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
"راب گرینفیلد" فعال محیط زیست طی ابتکاری جالب از زباله‌های خود لباس ساخته است
🔹
هدف او نشان دادن اثرات مخرب زباله بر روی محیط زیست و ظاهر شهرها می‌باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/akhbarefori/685245" target="_blank">📅 14:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685244">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c657448ab.mp4?token=pcEJJ5G-psw3U_0hwsEEcEt6LFbhoBtSVUwuPZUlVeJxHdidsVzq6H_FQSV7W3rS7x2F04g1XNiRC4Tm9qGUCMOAWOA5emCRMtudFOCJMdxfUnNTv2ofEzCWEgmNHEqpVHVJFwVuZLzJ8dbauass9NzXM6aYI7abFoOpBgzYLrnmmimp864-s_vlqxWD-rZNcUeSXWuoqr-FmlI-Ui7X3Aol0uS28Y03x5uLd7sg1HJkIYq2W-xbCrJSZweb5hksMFilC96qu2NJTZbqjx0BcmZmZgWHRRzVfTzyQDZftBBkVilgOfTtInRvWHDRBj4E9d7ff0tp-5gHSJDwaunUZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c657448ab.mp4?token=pcEJJ5G-psw3U_0hwsEEcEt6LFbhoBtSVUwuPZUlVeJxHdidsVzq6H_FQSV7W3rS7x2F04g1XNiRC4Tm9qGUCMOAWOA5emCRMtudFOCJMdxfUnNTv2ofEzCWEgmNHEqpVHVJFwVuZLzJ8dbauass9NzXM6aYI7abFoOpBgzYLrnmmimp864-s_vlqxWD-rZNcUeSXWuoqr-FmlI-Ui7X3Aol0uS28Y03x5uLd7sg1HJkIYq2W-xbCrJSZweb5hksMFilC96qu2NJTZbqjx0BcmZmZgWHRRzVfTzyQDZftBBkVilgOfTtInRvWHDRBj4E9d7ff0tp-5gHSJDwaunUZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
به هرنوع رنگ‌پوستی کدوم رنگ‌ها بیشتر میاد؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/akhbarefori/685244" target="_blank">📅 14:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685243">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThLmgH0DKUMDSy439zHcWfDsSd6BNLCUw89I9xkoo8b6AlAj0FA4OUfckM4kNmGvq4Lp7K1_49YE7_XqM1XgZQM7D30uO0mzIldYq5yUnDKywZuOtj1UN6GBfh0gFd-6yo75GBgPqt-_JHvWz10Vf5doHyeXTzEQ6xbnkGHakbvsH9pskaNazqcnuX_xGY3btPNbortgKFlykFwZXN-AqkU45G1zyKTOtiB09yWEptKh_61xtCqbpNlvpa16qdXwOkxzvNTp3ROQqjVNqmcVORNh5_42yQwcXX7Pf-eMNOMsf-sW8xWLYeRQxdSfnrjDYABIbYUGcJGEx7ulpEua5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان تاسیس شرکت‌های مشهور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/685243" target="_blank">📅 13:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685242">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رئیس جمهور: اگر لازم شد برق دولت را قطع کنید؛ برق صنایع نباید قطع شود
پزشکیان:
🔹
برای عبور موفق از فصل زمستان و مدیریت چالش‌های ناشی از ناترازی انرژی‌، ‌‌باید به گونه‌ای مدیریت کنیم که چرخه صنعت کشور بچرخد و در عین حال آب، برق و گاز مورد نیاز صنایع تأمین شود.
🔹
تأکید کرده‌ام که اگر لازم شد برق دولت را قطع کنید، اما برق صنایع نباید قطع شود.
🔹
یکی از برنامه‌های دولت برای کاهش ناترازی انرژی در فصل زمستان را ادغام فعالیت، دورکاری و ساماندهی برخی ساختمان‌ها و ادارات دولتی و انتقال ظرفیت انرژی آزادشده به بخش تولید و صنعت تا زمان عبور از پیک مصرف انرژی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/685242" target="_blank">📅 13:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685241">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTbKxALKU_nTnWiuvRJNJijcl_lwKgLbt8wmd5iSaYs58kVHoEX9qSR0sU_tJOS8ChvimeKVODdwptNrwLZc0iRtTV0WQNBCdr2icXX8AZ7uoMKaNWxBtcJRsAX0Up9qIMHoxz7hfOOM0vOfeHYu3GlDDnJjRWogbaMQvB4ZRRoJkfw5h0avCKLJQ6OHjaoaznTGWwuyOkOgyrPUVeLdqcqtaoaAo0uv5z8AooqB0NBeSwb6lIEJ4tHtLjWRmzPKPJeh_WIEtIS10dXYxgwriaS3EKUDOuX52Jt3OW1NRouptNRJlGSdWk2vzCoWgWfQ7Uk39bYWjXCObEMwx4zBFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۶ سالگی و عمل بینی!
🔹
وقتی یک نوجوان قبل از اینکه خودش رو بشناسه، دنبال تغییر قیافه‌اش می‌ره، باید پرسید مشکل واقعاً از بینیه یا از تصویری که فضای مجازی از «زیبا بودن» ساخته؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/685241" target="_blank">📅 13:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685240">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466edb2c8f.mp4?token=YpF4N4OYYoT2A65vH173p-mYqGUm49F9KcXIbmj3LnGEiBfaE-RFOafqxvdA9WHn-oRk2OQNQrjGRxmcuXZi5BzS4kprg9RpOPe_lGDN-FcTXR-DSmVaGjFvGnJ0vFCX_ejVAWugacuzxggjvrLeKNvfKyL744g_FeSM39IOTWMj6o_U0g63RF8EGKL0Mf7uSeKmDDfvJ1DCCt5RX1og5Ny-4rJ4GsIDXFKMal5NjLi4A_bQfmJN-U697M5XfmvgaVHcQaN1zmZxgOom6TF3VBfOURHkt12DfbcRlqFgbNG74uqpaZbs2a1q_uv7ti0EZUbNEcgabg-7DptpXrcZIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466edb2c8f.mp4?token=YpF4N4OYYoT2A65vH173p-mYqGUm49F9KcXIbmj3LnGEiBfaE-RFOafqxvdA9WHn-oRk2OQNQrjGRxmcuXZi5BzS4kprg9RpOPe_lGDN-FcTXR-DSmVaGjFvGnJ0vFCX_ejVAWugacuzxggjvrLeKNvfKyL744g_FeSM39IOTWMj6o_U0g63RF8EGKL0Mf7uSeKmDDfvJ1DCCt5RX1og5Ny-4rJ4GsIDXFKMal5NjLi4A_bQfmJN-U697M5XfmvgaVHcQaN1zmZxgOom6TF3VBfOURHkt12DfbcRlqFgbNG74uqpaZbs2a1q_uv7ti0EZUbNEcgabg-7DptpXrcZIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی مرزها روی نقشه نیستند؛ در دل مردم‌اند و آن‌ها را نمی‌توان با هیچ فشاری جابه‌جا کرد
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/685240" target="_blank">📅 13:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685239">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103c5fbd41.mp4?token=AQY1Z9OYDdUMQXA-PqNRO6lvrmmuNfgB6g856Wtl6nABVDcHp9Uldjr-1YS7Ib4y7i3m3JbjC1489xAph2k9Aze-2uJ53iDIT6WbtYHU9LYc7PDKBYrYQRGOvWUNy2hcN4eh49QfOVfSoRgSq9gB1OEBkGW92i26fhcHne5Rh4hOaGu3Uw3ky2Oq79tYQojylgO0p99kf8QuEbmEcMDtMItGHdWfnL40TRC23cApQ6dYFgZsLwKOJYNWHfkId6PRoB8Z6OcfGyz0HvHxAX3VHXqkTsXpS9rU70QdQJfj2Aq6t_HIEwrMmb2I9SmLppBeJNFeMIOrany9_VA8Y7f2vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103c5fbd41.mp4?token=AQY1Z9OYDdUMQXA-PqNRO6lvrmmuNfgB6g856Wtl6nABVDcHp9Uldjr-1YS7Ib4y7i3m3JbjC1489xAph2k9Aze-2uJ53iDIT6WbtYHU9LYc7PDKBYrYQRGOvWUNy2hcN4eh49QfOVfSoRgSq9gB1OEBkGW92i26fhcHne5Rh4hOaGu3Uw3ky2Oq79tYQojylgO0p99kf8QuEbmEcMDtMItGHdWfnL40TRC23cApQ6dYFgZsLwKOJYNWHfkId6PRoB8Z6OcfGyz0HvHxAX3VHXqkTsXpS9rU70QdQJfj2Aq6t_HIEwrMmb2I9SmLppBeJNFeMIOrany9_VA8Y7f2vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین ساختمان در هند
🔹
ساختمان کاغذی هند تو خیابان بنگلور که افرادی هم داخلش زندگی می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/685239" target="_blank">📅 13:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685238">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کانال منتشرکنندۀ فیلم قتل حمیدرضا رجب‌زاده بسته شد.
🔹
فرمانداری کنارک: احتمال شنیدن صدای انفجارهای ناشی از انهدام مهمات وجود دارد.
🔹
آفریقای جنوبی بار دیگر از رژیم صهیونیستی به دلیل نسل کشی شکایت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/685238" target="_blank">📅 13:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685237">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0fEDEkIiHFcvEoSHmIa3W6rjoZU8VNhu_TAzeR9QjFGbmX18BH0RNJJgpCbBrAcEszA_EUEUJ8HoMCdbVlmB1vj5WGe74c7_euk9xwFLgKe_B39mlGnW4wdHuI28vPv41XcKn1VHFf7OpnkscWJ4kqfB5popEuIoR3ywzg5k9Xpxio7GmR3-UuSW9Bn-4AbHp2ZrxiNGVa86UkCdyASDHU2ZRJstkEVWAaP_c4oT6UafLi0jXvi8z2wCmonBxMa7GelKrD8jc36AjsDu_pT1ovJAL5FUFHKHP2rZMEmYdHSNay0hdN_PiPmUfnXDHAW6VhU9AjVg5CsVuGnJdbc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کشف سنگ ۱۷۰ میلیون ساله  بعد از سیل وحشتاک نپال؛ غول ۳۰ تنی شالیگرام!
🔹
یک سنگ شالیگرام عظیم با قدمتی بیش از ۱۷۰ میلیون سال در منطقه موکتینات نپال پیدا شده که وزن آن بیش از ۳۰ تن اعلام شده است؛ سنگی که گفته می‌شود یکی از بزرگ‌ترین نمونه‌های شالیگرام کشف‌شده در جهان است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/685237" target="_blank">📅 13:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685236">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
اعطای وام اشتغال به سرباز ماهرها
سازمان وظیفه عمومی فراجا:
🔹
سربازان ماهر منقضی خدمت نیروهای مسلح که از اول مهرماه سال ۱۴۰۰ تا پایان شهریور ماه ۱۴۰۴ خدمت خود را به اتمام رسانده و کارت پایان خدمت اخذ کرده‌اند، می‌توانند از روز دوشنبه مورخه ۱۴۰۵/۰۶/۰۹ نسبت به ثبت درخواست وام تسهیلات اشتغال‌زایی اقدام کنند.
🔹
اولویت واگذاری تسهیلات مذکور با افراد برتر مسابقات، سربازان متاهل و افرادی است که در بازه تعیین شده زودتر نسبت به ثبت‌نام و تکمیل مدارک اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/685236" target="_blank">📅 13:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685235">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km4JmFQVNwCtA0IP3wzw-grWr_Iqr5agwh2dMN6Y16wA-dkGFpURZBWyemBNHjpKbuATjFeLglAVNE8Wz3M_jp7cHTD6ukWfDsO1nrbejtmPV4Zr1jQhh-4TcnA5Vx4Yfuo287lsLjpSL0Ae7BjIyfgiANWKR89O3qcIuJbf9Kq5J42LeAl77XHp3vFPiXmiil34KKF7d2A_MC4BB3V01FNOYUNl-hhKybhO4e09Yp9U1Uoynk0KtEQ7zxLOjw0xY5CAPCzfEf2fIccltd5KGh1h5OBoxjZCz4sq3kIZNvbF1Kwl66qKU-GyroJV2rYjYkOR_2vmqJeYD8jaWSs2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییر سهم اپراتورها در بازار مشترکان تلفن همراه/ افزایش سهم همراه اول در بازار مشترکان
🔹
گزارش بهار ۱۴۰۵ سازمان تنظیم مقررات و ارتباطات رادیویی نشان می‌دهد سهم همراه اول از بازار مشترکان تلفن همراه، از ۵۴.۲۹ درصد در پایان ۱۴۰۴ به ۵۴.۳۷ درصد در پایان بهار امسال رسیده است.
🔹
این افزایش در حالی اتفاق افتاده که سهم ایرانسل در همین بازه از ۴۲.۲۰ درصد به ۴۲.۱۰ درصد کاهش یافته است.
🔹
همراه اول با این رشد، همچنان بیش از نیمی از بازار تلفن همراه کشور را در اختیار دارد و بزرگ‌ترین اپراتور موبایل ایران باقی مانده است./ فرهیختگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/685235" target="_blank">📅 13:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685234">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9325e0586.mp4?token=iRcuJNqWbIctvOqvVYspsLrfJ5BYUlzeSGKFaI3La5vH8_NPeZBoeBYzjvXt2ar36sp_1-mTb24M2M4TZdbyh3hgeXETZF3RTR5LYI7Po3Fao5NNpFfWyb6cxMmIedxWM7V4XI7KCrpb2wzqU0khXilb6xqMxhkMQUuSW0jLb9NnrudRYDIxTmMdAmv3r-ffAMmkY9rqAt4CdFtPuZueumWCWgC_QaG2RV_fQF3Y9QAT6GuYmCAzw-99llaNKih84cozURrN6k86kp30DausjalVu0BB4CPujFatBzubUHO8EItr2QwLM-tVtB_wswIhMayOGA5QxppXR37WdEQYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9325e0586.mp4?token=iRcuJNqWbIctvOqvVYspsLrfJ5BYUlzeSGKFaI3La5vH8_NPeZBoeBYzjvXt2ar36sp_1-mTb24M2M4TZdbyh3hgeXETZF3RTR5LYI7Po3Fao5NNpFfWyb6cxMmIedxWM7V4XI7KCrpb2wzqU0khXilb6xqMxhkMQUuSW0jLb9NnrudRYDIxTmMdAmv3r-ffAMmkY9rqAt4CdFtPuZueumWCWgC_QaG2RV_fQF3Y9QAT6GuYmCAzw-99llaNKih84cozURrN6k86kp30DausjalVu0BB4CPujFatBzubUHO8EItr2QwLM-tVtB_wswIhMayOGA5QxppXR37WdEQYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک فرود انجام‌شده در شرایط دید صفر، از کابین خلبان بوئینگ ۷۳۷ فیلمبرداری شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/685234" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
با رعایت این سه مرحله روانشناختی دیگه به راحتی از دست حرف هرکسی آشفته نمی‌شید #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/685232" target="_blank">📅 13:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5db577a5.mp4?token=OcXqAh5U_Apq1B2ati1keEtv1-QDa7LISbDliiy3L7B8tbbk8G5uZtb0p-dC_mDohNQ-pLumL4VsKkC7ua8XGa5d0MF5g7drgBaXKttWrv4OSCFtN1XG-MmEHNNu1s4qqJJhK6-jmW0vbBrjf2nS_V6KvMyOa9Hsr0icvSEAz04UEseW8wqYk3b0ZVq0DzzBBai6lxIS8-cVqgwd_jYdM4HheOmjAC8lTMAsgnd2-lLkJdQFEjzI7rr2xxBRsBIsJE7DCDqMYAhrLvectIfd5bUouEDfhbD2-RQFQziSJnMHbgNalzkwnXr3HFgvoHhFrC6f3OSYSckiWTI8Z1VbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5db577a5.mp4?token=OcXqAh5U_Apq1B2ati1keEtv1-QDa7LISbDliiy3L7B8tbbk8G5uZtb0p-dC_mDohNQ-pLumL4VsKkC7ua8XGa5d0MF5g7drgBaXKttWrv4OSCFtN1XG-MmEHNNu1s4qqJJhK6-jmW0vbBrjf2nS_V6KvMyOa9Hsr0icvSEAz04UEseW8wqYk3b0ZVq0DzzBBai6lxIS8-cVqgwd_jYdM4HheOmjAC8lTMAsgnd2-lLkJdQFEjzI7rr2xxBRsBIsJE7DCDqMYAhrLvectIfd5bUouEDfhbD2-RQFQziSJnMHbgNalzkwnXr3HFgvoHhFrC6f3OSYSckiWTI8Z1VbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت رفاه بنگاه‌دار است و بیش از ۳۷ درصد اقتصاد ملی ما در شرکت‌های زیرمجموعه وزارت رفاه رقم می‌خورد/ ۶ میلیون زن سرپرست خانوار در کشور داریم
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
۷ دستگاه حاکمیتی و دولتی مسئولیت سرپرستی افراد ضعیف به لحاظ مالی را دارند که یکی دولتی و مابقی حاکمیتی است.
🔹
بنیادها و ستادهای مختلفی داریم که از رییس تا نیروهای اداری‌اش هزینه مالی کشور را افزایش می‌دهند و همه آنها هم هدف‌شان رسیدگی به افراد نیازمند مالی کشور است. وزارت رفاه باید به وظیفه ذاتی‌اش رسیدگی کند، اما بنگاه دار شده است؛ وزیر رفاه نه توانایی این موضوع و نه توانایی ممانعت از مداخلات بیرونی را دارد.
🔹
فرض کنیم تمام زنان سرپرست خانوار، خانه، ماشین و حقوق خوب دارند، بقیه نیازهایشان را کجا و چگونه جبران می‌کنند؛ این یکی از مسایل حاد جامعه ایران است که هیچ کس درباره آن حرف نمی‌زند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/685231" target="_blank">📅 13:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685229">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/784e0ffb8e.mp4?token=VkO-c1TEghgd2IbEwq-u5jOAu0sx2QSA-ocfd0ObUFJCSjTQEYpdlmIDJ91IhlPST8MMUled9RyWoAuZuVjqXrYMS7PT52Vbik5YJpWbzped19-0oexg1nHCJbZgK4upZUHbop1SIF7OwI1JPmytDr05u_9VJAevxCF-4c3Sw2SvBvSge8h8vN38nl5_zLBPZNiai97-XI3LYVxKWZH8XzUBu2a6SjPhy8Ve9ev68SlkUmPbgPjqQmPGlcu5UxDpmyrI9b3M4IXRQsjKRC3c2iAZ-QgldIyZUz1pj7lEqdeoj1_LSYaGE44kRj9eg0aJUVJMgM3h0rESo4HxtQx1rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/784e0ffb8e.mp4?token=VkO-c1TEghgd2IbEwq-u5jOAu0sx2QSA-ocfd0ObUFJCSjTQEYpdlmIDJ91IhlPST8MMUled9RyWoAuZuVjqXrYMS7PT52Vbik5YJpWbzped19-0oexg1nHCJbZgK4upZUHbop1SIF7OwI1JPmytDr05u_9VJAevxCF-4c3Sw2SvBvSge8h8vN38nl5_zLBPZNiai97-XI3LYVxKWZH8XzUBu2a6SjPhy8Ve9ev68SlkUmPbgPjqQmPGlcu5UxDpmyrI9b3M4IXRQsjKRC3c2iAZ-QgldIyZUz1pj7lEqdeoj1_LSYaGE44kRj9eg0aJUVJMgM3h0rESo4HxtQx1rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شکست سیاست فشار حداکثری آمریکا علیه ایران و بی‌نتیجه ماندن بیش از ۳ هزار تحریم برای وادار کردن ایران به تسلیم سیاسی از زبان پژوهشگر روابط بین‌الملل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/685229" target="_blank">📅 13:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685228">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvOvACeprJR7036fXgWcb1SvAJ0vcarbp3smAGJWwx4fpFWTODyQROi8ehtLpvTd17dsMvI9dfU5lAKJVB_01vNFql1-aK1e6C5h1lUAUVTkukUUo6tsGEPSRMsACMlOq6Whn_BVQpZ9xzMwwbVYT01j_4-uLRI6sHWvCmUO1sZBz2Om9wEqfzRuvozUs4ZRCNQoufH-mMcYf-TAQxDYJuws3ZQrSRioVsTeUedE4iSce94n1VFF0pGzkJeiUMUE0TWAmLgYgS-h0QKfIybF-8GgrUQhfqNznyFGx-yAlegahVxccCtqQ3wGz7j6IoilvpCd2jyURg5rWRnHERJc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت بازار دلار و طلا امروز شنبه ۷ شهریور
🔹
سقوط اونس جهانی طلا فشار کاهشی را به بازار داخلی مخابره کرده، اما رشد قیمت دلار در نخستین روز معاملاتی هفته، مانع از تثبیت روند نزولی طلا شده و بازار داخلی را در وضعیت نوسانی و محتاطانه قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/685228" target="_blank">📅 12:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685226">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMSfH_pCC3aCpOsVyO8aHDaADMZVwgG-aFvhbXBsNWHiYnKKyHuoBuN6lvqTGfF-NtYWMXlUvyR1EdItXtNm1w606kmkqQ_o8zZK5d16t_dOtxmmXeUqiVbYBQvio5YG8jX_0kjaNEFB-nHAyVT5pTsQJV9MZkn0Bz5FAvj_81KCkbvrlbXiKPn9He4St2e9M7XL4vVtHyw8X2JlXk3Ig13DO8nx8-3S5mecEcYWRcUqIStecmiER44nruVpCmWkG-uiO7hC3qf2s8Kf7OymjCxF0QuKydxrDWNgmVNXK56n-D0wyCKLuJ8RpZl5zo-fGUtbP-D9gbyZETDIfcgksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس هفته را ۶ و نیم میلیونی شروع کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۰ هزار واحدی به ۶ میلیون و ۵۱۶ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/685226" target="_blank">📅 12:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685225">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5umLM7Jleac49NzSh_JY_k1GfLAfL92Hr4VWqBtxAyaNxXIbHXcnQJ_2C-OhH-ntqqtcULba1dFP_097kFdgsm7zlUpP9UvSpDKqBD4jkOl1MzPzlnyCJf96GKjkeQ-HFVJ-xlYlEBP8HgCl33dc2BStJDGejahDg7aU2AdRM258yNTexfcVe2DNLgDecc50eL3tRg8XusRLnQnkOuXf0581Qc3KdESP7JWR9hhM9K3JV7rT-5VO-5tfPxzOOQv6C72eLKqPsYE8eSmdM0iNJIlWb7k3bYYnpvJQ6bHoc-oSEPoAjSsU1Yd2cFhgoX46Ec94LyL7xT6XmCP_WBX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشورهایی با بیشترین ذخایر نفت در جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/685225" target="_blank">📅 12:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIxyYmLwiJ3ybFxc9joGiisD7q4UpnGqrbHNUYethoXY735-tDt2_-kBsZWSo_Ms0Mn7B6FvkYEn_lNvYcWfN_-R5LXUtedgMVM8o_y34KXXYsv2f6otdmw87S3T6Y_xPtX3cGnUSucz2wKh05Zg7pIcO6d1IsfyFfY96JVwzZsOEmnlRgJIZrtuBnwRfXNc9Oyp_f3SWxdc82cXGGqcsAyL6di7D0bjQsTameP55_5r4dFpBK0aKvLbXkuhVOZFjr3Wum_uBaD0hc1Alb2OnQOoRm_nOB_JI4Ab7zA69mnBmFvgNeC80r8X90ovcwWpzeQVfBldKE0YpULDhVkHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای گلدمن ساکس: بازگشت میزان صادرات نفت به دو سوم سطح قبل از جنگ
🔹
نفتکش‌ها به‌طور فزاینده‌ای «تاریک می‌شوند» (ارسال سیگنال موقعیت خود را متوقف می‌کنند) و از انتقال‌های کشتی‌به‌کشتی برای دور زدن اختلالات استفاده می‌کنند، که به کاهش قیمت نفت به حدود ۸۹ دلار از ۱۲۰+ دلار در آوریل کمک کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/685224" target="_blank">📅 12:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d0eca302.mp4?token=aZ7V8KX7ExKECJCWWiaoH2-lZS5chtUStERE7C-NLLE6f1gCFAjfZG47-iMLI76iBDeqd-5yorADbT37MQOPoh6oUhUhs3cc6lWb9AgKxEmM1Nmt5m1U3TEUJbyfSQWEFIoGcB23GkaENyiGRv9jJ2fSrmW3WADtGrbdeWhHSjlDa8Xh2XIe-9aj8FgxOv2FKgBW6EopD-KWHWoIeC27etJkFkzLOFvJr5OgV6bE2WJL4cNncyhgkYMPo3I3xEUX5z43-0wBZQ2UnDgHK4y17x7LLWdJdjiFhRjp6e3yQPqIxe6vME2bLRRMt6i0YPgRBA4GKf9ZyZgitmq3AqfefQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d0eca302.mp4?token=aZ7V8KX7ExKECJCWWiaoH2-lZS5chtUStERE7C-NLLE6f1gCFAjfZG47-iMLI76iBDeqd-5yorADbT37MQOPoh6oUhUhs3cc6lWb9AgKxEmM1Nmt5m1U3TEUJbyfSQWEFIoGcB23GkaENyiGRv9jJ2fSrmW3WADtGrbdeWhHSjlDa8Xh2XIe-9aj8FgxOv2FKgBW6EopD-KWHWoIeC27etJkFkzLOFvJr5OgV6bE2WJL4cNncyhgkYMPo3I3xEUX5z43-0wBZQ2UnDgHK4y17x7LLWdJdjiFhRjp6e3yQPqIxe6vME2bLRRMt6i0YPgRBA4GKf9ZyZgitmq3AqfefQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دختر کوچولو وقتی فهمید پیک ناشنواست، عبارت متشکرم را به زبان اشاره یاد گرفت تا بتواند از او تشکر کند
🥹
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/685223" target="_blank">📅 12:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712ab5dcd9.mp4?token=Z8efdrgmJtzEj5UJpc3dZf9ojmJ3MkK9gO8NdZQT-wD_5bdtAiDwIk1j_d5Be2tR02_Atx5pOcBBpHyeoQRfbU8NKwPHbkpitxVFmpPP51NYcJTYFNDrce-nVP6f78FpLmvRKRNYb4VBbaGsqa6SOTU0axcwZGLid7qQcOz1ZVPxSJ8cDV9EHAykZp2H7SMzkyFBuJlKhnPdI5raUSDbIWZLX2KSz3H9BjdZLKxtXcyhHvD7meBC7DDdwKaxCMww3TVy0SMo9GXG3SDDWX2icGuOzPhNUJpZrC9ChcuDcUtT2MD5YuIHUidIgtTMNEA1O0Lc-sNv2YLLMEpIsVxDKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712ab5dcd9.mp4?token=Z8efdrgmJtzEj5UJpc3dZf9ojmJ3MkK9gO8NdZQT-wD_5bdtAiDwIk1j_d5Be2tR02_Atx5pOcBBpHyeoQRfbU8NKwPHbkpitxVFmpPP51NYcJTYFNDrce-nVP6f78FpLmvRKRNYb4VBbaGsqa6SOTU0axcwZGLid7qQcOz1ZVPxSJ8cDV9EHAykZp2H7SMzkyFBuJlKhnPdI5raUSDbIWZLX2KSz3H9BjdZLKxtXcyhHvD7meBC7DDdwKaxCMww3TVy0SMo9GXG3SDDWX2icGuOzPhNUJpZrC9ChcuDcUtT2MD5YuIHUidIgtTMNEA1O0Lc-sNv2YLLMEpIsVxDKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش جنجالی گاردین انگلیس از ورشکستگی نیروی دریایی آمریکا
مجری شبکه آمریکایی میداس تاچ:
🔹
جنگ فاجعه‌بار و ویرانگر دونالد ترامپ در ایران، نیروی دریایی آمریکا را ورشکسته کرده است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/685222" target="_blank">📅 12:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
فارس: طبق اطلاعات کسب شده از وزارت نفت، ایران خارج از محاصره دریایی، برای بودجه سال ۱۴۰۵ به اندازه کافی نفت برای فروش دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/685221" target="_blank">📅 12:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685220">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b7148ba07.mp4?token=ZnTqoHDnN5CeP-yUbXzE8wNN8XT1Wd76J4fQkfQCwJWEb87bBk0hY78wFbc4_Lp8eCUpLI-vyLf-GA_vwF8eVZvlZVGPEL0cueqgpvXZiC8iLI5E8SrIHdwRfOsbXoE7YATZwB7Ir1D0DLrCZ2B9f9qyDPYhFXJ5S3MYdVN3X3Y30iY9RXlK_j31PjNYRK7L0yCvgklWxQHP-2Iq7yLWsNXnt42_wf6FWqWlz_Bj5AD6REehsMpLkAXghN7FMdHvL5euruZimjNRs0GAauC2KuYJAwLsCNdIys-sTG_4t_YPo5GFDMtvwO0BVbkrfQ9qAo7QOhs9vj6mrW9y7BU3hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b7148ba07.mp4?token=ZnTqoHDnN5CeP-yUbXzE8wNN8XT1Wd76J4fQkfQCwJWEb87bBk0hY78wFbc4_Lp8eCUpLI-vyLf-GA_vwF8eVZvlZVGPEL0cueqgpvXZiC8iLI5E8SrIHdwRfOsbXoE7YATZwB7Ir1D0DLrCZ2B9f9qyDPYhFXJ5S3MYdVN3X3Y30iY9RXlK_j31PjNYRK7L0yCvgklWxQHP-2Iq7yLWsNXnt42_wf6FWqWlz_Bj5AD6REehsMpLkAXghN7FMdHvL5euruZimjNRs0GAauC2KuYJAwLsCNdIys-sTG_4t_YPo5GFDMtvwO0BVbkrfQ9qAo7QOhs9vj6mrW9y7BU3hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه از موشک قاره‌پیمای جدید رونمایی کرد
🔹
روسیه با آزمایش موفق یک موشک بالستیک قاره‌پیما، قدرت موشکی خود را به‌رخ کی‌یف و هم‌پیمانان غربی آن کشید. وزارت دفاع روسیه اعلام کرد کلاهک آزمایشی از پایگاه فضایی پلستسک در شمال روسیه پرتاب شد و پس‌از طی مسیری به میدان آموزشی کورا در شبه‌جزیره کامچاتکا در خاور دور رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/685220" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685219">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26841cb643.mp4?token=DSn4jbsi8KFammi07y_z7brDWo4duvDEskOKvtuqYND9D3x9mlZK4S-hlyISUZzWmpKyAc5D68OUVws1DAHjl3WrXBq5O1tvv7r-caCMqC9Hv0MgEYqNrDsdG5CvEsb9aKRRET5664CgxKPLI5W23A_y3qmnAfLO6poqpld7c7fLV8qOd_cgneW70KwzzdURbaH4yGkO-nkCex8BRyTLDrf6BWnCn8koaPZN0lQ1qxzHzCHxX-f1Y-ntnNENShwa_z1Y3864ly-6LbCWHjg3fEes4N35upw_YAMo-DVsMGPjrDs1EcX9EOX_4JlLu9feZDj4Y1RrutySbWwEKslJJGlChu2v_1chO3pfO1-BnoZvhthEfgQ4X-7zwtXoT84u3cPTXIqonn69tGfuZhcWMEeEOzNMsiKGs7DVY9-wUcAGPNp0WMXOOAtDOQo3_xpSheLg2TkjfjWNwTGGgF0Zm1zJLZ4DUma1inGeT8GUhde7sz4GhEU8eZIFagrOBcuTM1pdt-NC58zthR0Y2PiJqwunu-8yFdPdav7-_PUINPuFjoW8lJ02Hs4OT-ol-mvcH8-kqIGqmhAKfNxPc6wxToukk7wdZoSslYiNBAmWDMfMOCf581nR2ooO6cNgiFo43jt8xc7_thQcXEEtXLkTZI9GoSx0VNp2pyxeKd0m800" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26841cb643.mp4?token=DSn4jbsi8KFammi07y_z7brDWo4duvDEskOKvtuqYND9D3x9mlZK4S-hlyISUZzWmpKyAc5D68OUVws1DAHjl3WrXBq5O1tvv7r-caCMqC9Hv0MgEYqNrDsdG5CvEsb9aKRRET5664CgxKPLI5W23A_y3qmnAfLO6poqpld7c7fLV8qOd_cgneW70KwzzdURbaH4yGkO-nkCex8BRyTLDrf6BWnCn8koaPZN0lQ1qxzHzCHxX-f1Y-ntnNENShwa_z1Y3864ly-6LbCWHjg3fEes4N35upw_YAMo-DVsMGPjrDs1EcX9EOX_4JlLu9feZDj4Y1RrutySbWwEKslJJGlChu2v_1chO3pfO1-BnoZvhthEfgQ4X-7zwtXoT84u3cPTXIqonn69tGfuZhcWMEeEOzNMsiKGs7DVY9-wUcAGPNp0WMXOOAtDOQo3_xpSheLg2TkjfjWNwTGGgF0Zm1zJLZ4DUma1inGeT8GUhde7sz4GhEU8eZIFagrOBcuTM1pdt-NC58zthR0Y2PiJqwunu-8yFdPdav7-_PUINPuFjoW8lJ02Hs4OT-ol-mvcH8-kqIGqmhAKfNxPc6wxToukk7wdZoSslYiNBAmWDMfMOCf581nR2ooO6cNgiFo43jt8xc7_thQcXEEtXLkTZI9GoSx0VNp2pyxeKd0m800" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آخرین وضعیت تنگهٔ هرمز
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/685219" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685218">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
دستگیری چند نفر در پرونده سرمایه‌گذاری FNDK تالش
دادستان عمومی و انقلاب شهرستان تالش:
🔹
این شرکت رمزارز‌هایی از یک سال پیش به فروش گذاشته که تا ۳ ماه پیش به سرمایه‌گذاران سود‌های هنگفت می‌داد و مشتری زیادی جذب کرد، اما از سه شب قبل، وبگاه منتسب به آن از فضای وب خارج شد.
🔹
تاکنون ۶ نفر از اعضای اصلی این شبکه مالی دستگیر شده‌اند.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/685218" target="_blank">📅 12:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685216">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805ea2127.mp4?token=PWQJE6bguK2BLoFdJkpxwxNd0KKqCOoaCIsdNU_d35Yl7kWHgpocRX294F6zKmXhZF_EXuOk2YZyhjMv_ClFM0jXNP8kFJFazCedVGUT2aB98kUjJnh2lVe52fzgdUIvD76T5fUZq5Nsu9F7uUIiD6tFmOgSkZnhJt_Ue33JUqIyKuE86KhVz0iRJU-DNq3qkyKq1CYvk9SssTk8L2vsL-ycQ6EGHquscLKP4PE16SeRBuEDGPhLp_iPWu4V4QuTmTPjRfnOmL8begx9VNqR7JeAayI9AEAh4q36v5XvxtJtz2a_o3X5iBTiDnvJ8eWOrOGKkdZYdab6jCaw31EMXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805ea2127.mp4?token=PWQJE6bguK2BLoFdJkpxwxNd0KKqCOoaCIsdNU_d35Yl7kWHgpocRX294F6zKmXhZF_EXuOk2YZyhjMv_ClFM0jXNP8kFJFazCedVGUT2aB98kUjJnh2lVe52fzgdUIvD76T5fUZq5Nsu9F7uUIiD6tFmOgSkZnhJt_Ue33JUqIyKuE86KhVz0iRJU-DNq3qkyKq1CYvk9SssTk8L2vsL-ycQ6EGHquscLKP4PE16SeRBuEDGPhLp_iPWu4V4QuTmTPjRfnOmL8begx9VNqR7JeAayI9AEAh4q36v5XvxtJtz2a_o3X5iBTiDnvJ8eWOrOGKkdZYdab6jCaw31EMXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جارکیک خانگی؛ ایده‌ای شیرین برای رسیدن به درآمد
🔹
در #چرخ_زندگی سراغ ایده‌هایی می‌رویم که با سرمایه اولیه قابل‌مدیریت می‌توانند به یک کسب‌وکار خانگی تبدیل شوند.
🔹
این بار نوبت به جارکیک‌های رنگارنگ و پرطرفدار رسیده؛ محصولی که با تهیه مواد اولیه، بسته‌بندی…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/685216" target="_blank">📅 12:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685215">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473021b96f.mp4?token=DfA2WvH_SJcuYewUFvunEOmlPv_1BzDraTMvnLAx9HXVqBlVmN2-d1eJbgmu65acCC0oVWMsHvLO4GWkPzlJK9BS8VRgcAxFiWlsqfXwHOaGpSWiBc1k05Mxpa0s2aUCDdPbaCOUJ3xteNoLQpAHUrKaphOdc8YQP0IL5icYdiMyxIYK9QSgVAkbDbMl5W-fdCD-ypqtMXFbiUvWuw4uYndM66YDr5_7guRDbAuTOAv_OxTlrcpHzBY56LrSGO-UmUs5-CxHKlxfm8RgwWqd8GhFoDRRC1QOK4thVrNK-MrgEx0YJM6TqJ8KJYGwvrpe_EFPrGC5jUBixV9ZDfQSvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473021b96f.mp4?token=DfA2WvH_SJcuYewUFvunEOmlPv_1BzDraTMvnLAx9HXVqBlVmN2-d1eJbgmu65acCC0oVWMsHvLO4GWkPzlJK9BS8VRgcAxFiWlsqfXwHOaGpSWiBc1k05Mxpa0s2aUCDdPbaCOUJ3xteNoLQpAHUrKaphOdc8YQP0IL5icYdiMyxIYK9QSgVAkbDbMl5W-fdCD-ypqtMXFbiUvWuw4uYndM66YDr5_7guRDbAuTOAv_OxTlrcpHzBY56LrSGO-UmUs5-CxHKlxfm8RgwWqd8GhFoDRRC1QOK4thVrNK-MrgEx0YJM6TqJ8KJYGwvrpe_EFPrGC5jUBixV9ZDfQSvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف بنزین در روسیه به علت کمبود شدید سوخت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/685215" target="_blank">📅 12:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685214">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30b6cbad4.mp4?token=oujqKYvVaJc6ZqQ2MOYqWSQwlaubhI4Rdd7i6sAx9dx5-eB3GXlF20oAMEfyCHES9L6z_yI79CiNutoL3gpDpIF23XQSoUfmGpxVvggY8XeSROxulbo5Dw41tb25e0TSQf8NQ0385I9UJxEC5R5ZM7s2p2eoiQ9t-9KVZpUyxcJtWglWyfu1nofLNqUGBrsLGbfb2pav9nOCjLCAz1zdQ6UYFp6e3TvyRKX6bGKA-dLbVvW0MUA2qHCCI66ZSaHNbd9JDbXzMs5J8pcHuKkIn92FgpwiUvfz_enhZlalhF_OysxjrOueBsI8rlzTJk913WrDq6vnzF9seaQrYDlGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30b6cbad4.mp4?token=oujqKYvVaJc6ZqQ2MOYqWSQwlaubhI4Rdd7i6sAx9dx5-eB3GXlF20oAMEfyCHES9L6z_yI79CiNutoL3gpDpIF23XQSoUfmGpxVvggY8XeSROxulbo5Dw41tb25e0TSQf8NQ0385I9UJxEC5R5ZM7s2p2eoiQ9t-9KVZpUyxcJtWglWyfu1nofLNqUGBrsLGbfb2pav9nOCjLCAz1zdQ6UYFp6e3TvyRKX6bGKA-dLbVvW0MUA2qHCCI66ZSaHNbd9JDbXzMs5J8pcHuKkIn92FgpwiUvfz_enhZlalhF_OysxjrOueBsI8rlzTJk913WrDq6vnzF9seaQrYDlGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت به آغوش وطن، بعد از ۶ ماه
🔹
سه جوان ارتشیِ ناو لاوان، پس از ۶ ماه دوری و اسارت، امروز به داراب بازگشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/685214" target="_blank">📅 12:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685213">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc5dc2c0f.mp4?token=vF8whK0N09sRJsOiaIqTwuT45aarszuOsRcF0eLuXEruOlecsXSWETAARpd6jneNAteekMWwfVXtKdS8bmsdWeR9A7zvXRN2YbPFxKmRJPWN4lDTi1orXGR9movgXtiA2iRYj3TeAMosYdzWoJoNILtMh8CFIWTdY87Py0QdYoJQeSUF8y0lz6lcicZheasvXkGuMxr-6jyQOAR91NrC3M-R7tuxqRHaXZfC9rkTh53geCnQ9cs9V8KC7iWOlrg3pbanGZbo0hqIeD6Rx3QINwW4aMk8eBbTLu2aDGAPxK6D_2Q16rYnSZPzNHmdlnHbezf1jkDHk8_6TQBV-0MsVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc5dc2c0f.mp4?token=vF8whK0N09sRJsOiaIqTwuT45aarszuOsRcF0eLuXEruOlecsXSWETAARpd6jneNAteekMWwfVXtKdS8bmsdWeR9A7zvXRN2YbPFxKmRJPWN4lDTi1orXGR9movgXtiA2iRYj3TeAMosYdzWoJoNILtMh8CFIWTdY87Py0QdYoJQeSUF8y0lz6lcicZheasvXkGuMxr-6jyQOAR91NrC3M-R7tuxqRHaXZfC9rkTh53geCnQ9cs9V8KC7iWOlrg3pbanGZbo0hqIeD6Rx3QINwW4aMk8eBbTLu2aDGAPxK6D_2Q16rYnSZPzNHmdlnHbezf1jkDHk8_6TQBV-0MsVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی حتی SIUUU رونالدو هم منتظر VAR می‌ماند!
🔹
رونالدو در دیدار دیشب النصر مقابل التعاون، پس از گلزنی بلافاصله خوشحالی نکرد و منتظر ماند تا VAR گل را تأیید کند و بعد از قطعی شدن گل، ستاره پرتغالی برگشت و خوشحالی معروف SIUUU را انجام داد. این گل، گل پیروزی النصر بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/685213" target="_blank">📅 11:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685212">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2faa7b5d8.mp4?token=viL_69MVhrBKyUP0AMSoIq60Jyf_FqlZtlsPAgVVcsAVkuwc5oUiJtr8n8I10Ejbd21dvLJavr0Mv2Pig1t9EuscjB2tcA7xqkfNbGvyQ-X6WaHbETSB3gu3uMkxgiIEf60tLK4_Nfj48jvttoK--z1fVGPF_ak0tqIV3142SKpMxTiqfSAlWsNAz-wVSXZprDjfB47RDImnbT0QR-26o6x_RDzfukXS2wOUQlZypgpOVumNVuNAgozvihp5OSjMu6xJphRDEzaP-_aSqpNno4JO5mxpPYpOJz6Qvpv5bDTe2xaknxQ4RaVyPWP8-EIm6_34VVsM11nnaQW7LtapBWBJLsgPH5YRtMmAApyJXIXNJag91cPyTM7jso13AY_luNkZpTsMr23Lb-zCxqi-YozWP6v51FuPDmz1rLejCmn6gyRoLAitIxhxFbHIVx8FAoTAKtqDcCLHoS4cWxRBj-0Yos_nyqHA3k_n3fUt0RatU-YLA-gNsjYQCQ0xG1pLXtzOIcOriuxg_vykMzGti66hoaO5Ope8zRFDTN89ZQ_IzFUlxyH9pvN0bt1FxJYtSDIF-Ve-Cwyq2kr2udRI3g0jc3m_x_1WwBn1iDHrWMT__bXz5yC4a-yMBFQUAqF8Kpwsc7zmLmfFKZl9f8bDKcgCN9LcHPQ9lLpOvY5M7CE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2faa7b5d8.mp4?token=viL_69MVhrBKyUP0AMSoIq60Jyf_FqlZtlsPAgVVcsAVkuwc5oUiJtr8n8I10Ejbd21dvLJavr0Mv2Pig1t9EuscjB2tcA7xqkfNbGvyQ-X6WaHbETSB3gu3uMkxgiIEf60tLK4_Nfj48jvttoK--z1fVGPF_ak0tqIV3142SKpMxTiqfSAlWsNAz-wVSXZprDjfB47RDImnbT0QR-26o6x_RDzfukXS2wOUQlZypgpOVumNVuNAgozvihp5OSjMu6xJphRDEzaP-_aSqpNno4JO5mxpPYpOJz6Qvpv5bDTe2xaknxQ4RaVyPWP8-EIm6_34VVsM11nnaQW7LtapBWBJLsgPH5YRtMmAApyJXIXNJag91cPyTM7jso13AY_luNkZpTsMr23Lb-zCxqi-YozWP6v51FuPDmz1rLejCmn6gyRoLAitIxhxFbHIVx8FAoTAKtqDcCLHoS4cWxRBj-0Yos_nyqHA3k_n3fUt0RatU-YLA-gNsjYQCQ0xG1pLXtzOIcOriuxg_vykMzGti66hoaO5Ope8zRFDTN89ZQ_IzFUlxyH9pvN0bt1FxJYtSDIF-Ve-Cwyq2kr2udRI3g0jc3m_x_1WwBn1iDHrWMT__bXz5yC4a-yMBFQUAqF8Kpwsc7zmLmfFKZl9f8bDKcgCN9LcHPQ9lLpOvY5M7CE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده مجدد هلیا و توله‌هایش در زیستگاه یوزپلنگ‌های خراسان شمالی
🔹
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/685212" target="_blank">📅 11:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685210">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA_DK3dRRJcQierigVMebLyGL1Zgf07G9i4btA3c-tcahtlnTDWVy_6MPCvl3mkZIMwyAo-6FDOhtSWDjXEc2yqlP_RtuZgTB67U_Jl5M-fMDmK78eNMoVhX2IrXDOHj_WX0UNch89tIZmNJblA7PV3pWA0rUVFknfnSUWK4H-UYaQ3RpDuq0d-DmD9v5mWs7qfL_1Za7TG45pZwoNaH6Cn71cAd6lzmR-mgOcuy0Z6Q7_FCokrDvs7kDQ47YjWZZnxLQaQU7spGrG8d_wulQAWYiOr1xRjzn9WQLvK_ePzyi3aiP6S7Iyp28J54Kmuul3VMDD-zRQjrPVzBZLhdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تنها کوه خوراکی دنیا در جزیره رنگین کمان هرمز
🔹
این خوراکی نوعی خاک به نام گِلَک است که از دل کوه‌های سرخ استخراج و به عنوان ادویه در غذا بکار می‌رود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/685210" target="_blank">📅 11:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Idb4jGIIQ4tIFk42b1IktkwStlXWMUpXE9hf8wp_Hk5_TAX3K_vcowvYXGEpxTh0qmHZe_cDKIjHM7CM3BB2FOqOEFxzVzIe9-a3NF1QbmYolfdBphlAJnTcKZ_W5Qm6CDmz6QxUYVj2-bElLyvv6wUlpZmpLUPSN4agZ9lqhvJrcd4usI6FSZeAKTZ2q3ViDwO0omLUCN8WPSMAHWiH5LRt296906TLMpKuM73T-D2QIwViiWC3EXCGD9agPDAKSMG3IdRcDqRMhf4pq4EYYfhx7RWKE3QPjaEVZQB8pDisJx2uwKv6_e2XV8PhKFTVDC7145LFMEMo9BklQKU8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlcJ8Rg9dL8go6jajUw3UszMK9_5vU41aaDKmzYFnWCr1wXqXfpmpn58DiOvsp3afACcznCjD8DYGr-Ieqz78C2Ov5aWRVdcHU-opuKjYuQJjGeKcwhO2ifUbuOEfnjKleFRKOKeAFWDmfBcL_bcgXmYAuQDJAvMguowITEKGtXTwA-m4gWnBCE8f0la4OnJaMh14pcORL7jyno1wdLr3E0H8DYeF81i7NxE_rsxPE9Ak97nnpQ8jpWEF1RRiHXQ-7XlBB-XPyQILRYgIzafbTliiLq9fkvzbq_1YygNl3vAWf-YLvuJLIBZxAr5_TObkOReWU5E_SQGbF4a15e0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tixEOj-2giFTEfgkyB8F9b9P9BKEMVJ5hFGf9PVTe8LBUYsNK1-zH0XJbfcz_uCEaAkDWTUkipIRORu2RZrGx2jYPTJI836CoAIOaqsMGL-Yz1z5mp6jH1dLIt5rEaKE60dQeMGlQJJkciiITaIGy-J9ZxuRODTsRkwsvi4V0hZhtjvqOJ2cgCSTJN6vat6J9AWgOtK9XDxabXaDOHCRw72OvGpqgnu2361nDyZmzJKQi1-xKpDv-QDtnGr-uR8JapO-C6R1otTs92xpYu_UArLBPVWn-7jI2o-7Hw6hvEHzdC2hLsADI7_p1RJ6b12zCHmW0oMHMrq5ZsJmO-Uw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b3-pnuQt13BUA8qlJuL-jCbsx2VyuOWN5VYY8OaFqueUkT-BaxBaAS-EMJ4CEl5QfbtxC6d8ZZNvn52CeiDVP-qPHsOD39igAZm_ypa_laPRaulIqVR9YSIS-QZdq7YU28Qx_ksCRF1ioXhYRYVRNABl-bgeOcfZaiBGHfEQDKhn3tJPOKtYYBhEYA4Xcd7glEWi6ZMmP2n_tnwr15_sFMozoSyzs5zZS2JG7lm3IAXKmfQktp-etiQehrlzyBHmLb9TuiYnKSiu9baWWCLUjlxGorBZ69tUA1Bpn8kZk7bk8gEncLCfaJCW1dgfVMFStRDozGleDEDkDDIOJUIKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mldfZ7991HvZg5M8WjIYOHb2eE_cJX5XTENsNjACYBaXSGfyVh0Hx_9JwGzXeKYdvWhi-M86loVBav-ghEdo5nw8Cq2dch6LUnlPysEup6uOKnQsoBvlzLXbA6Geujii_BYQ-O-56AOKBq9joJfh6_PxADMlKutlqxYMtO53uFiLhP5SZFBx2xl3-TbipOIQptZ3pVXataW6SK9M1POW5UgVjPSGeIgs4rn3oTJof5TJcSAWRUQWdbyLDB9GxAX32WFHzmoVrh4u41hxIZbTgFzfsL6A0yht3HHOAMDgC4SYAx2LC7Z8QqhAzPaFn_Sw2CxcwlKZsW7GRoY4tzGaEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BbrceH8L4eKgmbxoQPGuMo-dIhu3C8EsxOgoh7wtL628ZXj6pGOaR9LPQrVZ1bsok_J0INwVzpbHquSi4h32vQCb4JhXDUKXJ058tpxzSHTY8UcuG4PLpFSJ8ki0qQ4_r15LN7eZkKwY4IkG2stL8s74wkLrfmUia9LtSqHjSD5YGA6mmhN08ZQGW_WuG6dsSP7TDDXzOd6IznEPkcT7kHBJGdY9TlGIAyzxfkuklIxbn1QBhpQoMGfAWCF81Gf9gwqZPyrk3xpCH0aSageV6YsoFwk17pcfXJ_KaP_mJdVLHKJIwVZU0Wzx8y8jj-wn39EHRw9OS5_gCa3424T1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5_iw0QIIZNo-PJjtbJ9fGh1ERVlecb3xbqGFEEh9wdQmWbtHayFkOU4f8uzD9oVMElk-uMFZ5G7EqS4rtweYPAAlDYiJSTp5qfGjBV0zK7n-Iy2ZmrH9tt4bq76653jFb-By_UJ2Pg6-PqDg2tpMsrU8iLuGKOV4zto8czM-xD4IEZ3xwySeCU_XN11Jzhfv3CLm98GbK3-wlsVMVY2iIxgXYi0Hb-a6YURWYto8I3Gyx6uQUOHNSiK_Ibh4K3XGxYXr6xG4U0yscbCe_-Nf7zzxW8PJ3fXg0S-oNQ9TCzQQDdBocjPoX4UtYK76DFqibS4xdQVpApHGM9NsAk4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQ8ricvzCkkdBrWdmcgwXvcbkL7p6Zz9j7FZdwQ-WmoM7jPHgFjzQE7egYkmkfAVEHsVO7qslRBEFh8jJXO69_27VRAj3sJ3cOG34le2PP9YL_czyqyPBySaAz-esR97MQ-fgf0phjDsYrsSpZZ26Gn3RzOqz1Y1EXfW8jF5LdcGC7yR9XkVB3DBfavVuoI-gFq5TA4IM4uvOLjUxzUok66Cg3s3Nb_dleoK9HgF_keSTJxOVaYR1QBWrPoNRGbD6VzwYiWF7nPPqVF0W0Abf8msGDTrVmelSx_UYgK_1kNgGKB_5S5yMHMKSRm84rtkH85K2dVXHBEidC2T4CAAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAxmha9Yxm9kUCcedzlgRS9J8zkc3-tDHmVkqbkVdoV53Jhj5nqMgUuh-M85_Ub6sYd5WtSeaaeywb2bcTiG_MJDr_qKhbjRrzqCF1Teov3TxjMBPQSKs6MJHuN8hZPa-DlSaUP4iveh14CD426Qbw1CJUCCFRNKqXbwtO_Q3Gqh4ia6V4HRJdM_arklTROuXFyABrTvjqQ8LQNfYZ-7zv3X7zMTT5_w3q9A9N-hnI7227ZDmxhV5IHdzi9S5n4MfitXOqfwvvllnt-3y4ezqgszZuvrWRD-wBChTmhTWAKa5J-92prsEfz5YQNRo9fmkS8xKKmvCyHIITPU1w4mVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری ؛ درد دارو
🔹
چالش‌های تأمین دارو؛ روایت شما از سختیِ دسترسی به داروهای ضروری.
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685201" target="_blank">📅 11:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685199">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d282c9187.mp4?token=WrNEX-3KlDjacCtyMjsi6Z2batSrOq4RkPrveJywYlDxtzS8HTL_lOxRVYS-yZohSgZYraFSs0pZpvZEsUfQXoax78qFfNMGvEDwpSKAB4FbRHsaS_7VXd-UeKNV-f0pZV3pGLbYxsviPvxjI1j6Vc9WZWy2TY4KnP__l7k4I6J8Y8iSkrxgoNnzglTwWYOydA9ztgcou60uLHMtPFHoTAs0ZXS9y0nHqY9bLwzz0XnRPw_dOtyOXHlkuIem4kOufUP2_DyO3MHJq3txSZ_1KjBxLXQgTkeGizBrEdgnLAm5w3w8AS2EmUO8w-EavcuEQ9ivFdLMy6TYlCP5ed8Myw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d282c9187.mp4?token=WrNEX-3KlDjacCtyMjsi6Z2batSrOq4RkPrveJywYlDxtzS8HTL_lOxRVYS-yZohSgZYraFSs0pZpvZEsUfQXoax78qFfNMGvEDwpSKAB4FbRHsaS_7VXd-UeKNV-f0pZV3pGLbYxsviPvxjI1j6Vc9WZWy2TY4KnP__l7k4I6J8Y8iSkrxgoNnzglTwWYOydA9ztgcou60uLHMtPFHoTAs0ZXS9y0nHqY9bLwzz0XnRPw_dOtyOXHlkuIem4kOufUP2_DyO3MHJq3txSZ_1KjBxLXQgTkeGizBrEdgnLAm5w3w8AS2EmUO8w-EavcuEQ9ivFdLMy6TYlCP5ed8Myw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدیمی‌ترین پرچم‌های ملی جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/685199" target="_blank">📅 11:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685197">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6a0852ba.mp4?token=o__LLCEb9xW8de0BwrKVVpuhr18SNwkjWbP3ywbMgtjPeGoRvWU6Wdx_5KMmtkxfJgthLK0M8VcHKdxfIwB7vXGL1_KiD7zm3n9h7x9TjxxQckOy5NdiOyUDP1EPWZIxzu9quAUbK_oYf5o9TY0ld7NjKAtqvfmJnrq0Gx7-69qjSafhX_lXhYGaICnnYT0c3fqbA85q9O7ZVC_UFEahZFXmY9cJpJJikjKc48xyhRVECCaegwOMYJO0B6Gy8LRARA7be4MqPfBgKk8mINu45nWZ4gJItgKGlrYo2z0WAiAMsP-zoU_ao8xHXO1t7uFT_Y7STLRsnl0zgmoInvBjxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6a0852ba.mp4?token=o__LLCEb9xW8de0BwrKVVpuhr18SNwkjWbP3ywbMgtjPeGoRvWU6Wdx_5KMmtkxfJgthLK0M8VcHKdxfIwB7vXGL1_KiD7zm3n9h7x9TjxxQckOy5NdiOyUDP1EPWZIxzu9quAUbK_oYf5o9TY0ld7NjKAtqvfmJnrq0Gx7-69qjSafhX_lXhYGaICnnYT0c3fqbA85q9O7ZVC_UFEahZFXmY9cJpJJikjKc48xyhRVECCaegwOMYJO0B6Gy8LRARA7be4MqPfBgKk8mINu45nWZ4gJItgKGlrYo2z0WAiAMsP-zoU_ao8xHXO1t7uFT_Y7STLRsnl0zgmoInvBjxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت اختلاف قیمت شانه تخم‌مرغ چیست؟
🔹
در نقاط مختلف تهران قیمت هر شانه تخم‌مرغ حدود ۳۶۰ هزار تومان اختلاف قیمت دارد؛ چگونه می‌توان از اقدام جلوگیری کرد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/685197" target="_blank">📅 11:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۸۳ درصد از اعتبارات فرهنگی کشور به  دستگاه‌هایی تعلق داشت که به هیچکس پاسخگو نبودند
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
واقعیتی که اتفاق افتاده این است که جوانان نخبه از کشور مهاجرت می‌کنند. دختر من که فارغ‌التحصیل دانشگاه شریف است، تقریبا تمام هم دوره‌ای‌هایش رفته‌اند.
🔹
شاید بیش از ۲۷ دستگاه فرهنگی داریم که چون تعدد دارد لذا موضوعات روی زمین می‌ماند و همه مبادرت به تولید آمارهای کاغذی می‌کنند.
🔹
نزدیک به ۱۷ درصد اعتبارات فرهنگی کشور مربوط به وزارت ارشاد بود و مابقی به دستگاه‌هایی تعلق داشت که به هیچکس پاسخگو نیستند.
🔹
از صدا و سیما و نهادهای فیلم‌سازی کشور بپرسیم در چهل سال گذشته چند فیلم در حوزه اسطوره‌های ملی و تاریخ ملی ما ساختید؟
🔹
اخباری شنیدم که رهبر خودشان ازقبل یک شبکه اجتماعی  داشتند و روی موضوعات فرهنگی قصد تمرکز گرایی دارند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/685195" target="_blank">📅 11:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685194">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ad30894b.mp4?token=cec718tr6kic8mz5iYylJ_8y8tP5QiEiNjsZ5140ooukRZWNAkXAOvtmkXEqwftLP8Wy2ypQk8J0zLMQdXREtgiL7nLL9f8SVI5V9vZ48muqivIExqZE3fHDdoyoIOTvmL2D-UYUhirJcXJYxqxl5EoWERxqS3q_TtCgy5v4Fu6-alj-ecrcvKKmhr54pEB63ngxA9uwslOxbTV0pkgeI1TKYIqrdYz_O6vVxIHCdjd0J6-4xlZk8d31udM1S2O7DpnCT_MGIn8M08MM7KF8Vio5wVvBIqQTqRmcd4YoEIYiRvvddasH5KFeu4HEVOUhHH0YMXtDQahMYs20lPhsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ad30894b.mp4?token=cec718tr6kic8mz5iYylJ_8y8tP5QiEiNjsZ5140ooukRZWNAkXAOvtmkXEqwftLP8Wy2ypQk8J0zLMQdXREtgiL7nLL9f8SVI5V9vZ48muqivIExqZE3fHDdoyoIOTvmL2D-UYUhirJcXJYxqxl5EoWERxqS3q_TtCgy5v4Fu6-alj-ecrcvKKmhr54pEB63ngxA9uwslOxbTV0pkgeI1TKYIqrdYz_O6vVxIHCdjd0J6-4xlZk8d31udM1S2O7DpnCT_MGIn8M08MM7KF8Vio5wVvBIqQTqRmcd4YoEIYiRvvddasH5KFeu4HEVOUhHH0YMXtDQahMYs20lPhsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند بسیار راحت و کاربردی وقتی به شیر آب دسترسی ندارید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/685194" target="_blank">📅 10:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده کل ارتش: مقتدرانه در برابر دشمنان ایستاده‌ایم.
🔹
بانک مرکزی: ۲۰ میلیون دلار اسکناس از بستهٔ ۵۰۰ میلیون دلاری تزریق شده به شبکه بانکی، توسط متقاضیان خریداری شده است.
🔹
وزیر دارایی آلمان: به جنگ علیه ایران پایان دهید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/685193" target="_blank">📅 10:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685192">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
آیا رهبر شهید، خبرگان رهبری را از بررسی نام آیت‌الله مجتبی خامنه‌ای نهی کرده بود؟
سعید صلح میرزایی، عضو مجلس خبرگان:
🔹
دشمن زودتر از همه ما خطر ایشان را برای جبهه استکبار دیده  و حدودا از سال ۸۴ بود که تهمت‌هایشان به آیت‌الله حاج آقا مجتبی آغاز شد. خب رهبر انقلاب فرزندان دیگری هم داشتند و اتفاقاً ایشان فرزند دومِ امام شهید هستند و می‌شد این فضا برای بقیه فرزندان هم پدید آید.
🔹
این سخنی که تقریباً اواخر سال ۱۴۰۲ مطرح شد که امام شهید نهی کردند از این که فرزندانشان در کمیته تعیین مصداق رهبری در خبرگان مورد بررسی قرار بگیرند. در پی این حرف و حدیث ها از رهبر شهید در این زمینه سوال شد و ایشان آن جا انکار کردند که چنین نکته‌ای را گفته باشند. منطقی و عقلانی هم نیست؛ چون در یک برهه زمانی ممکن است جامعه به شخصیتی نیاز پیدا کند که اتفاقا آن شخصیت فرزند یک مسئول باشد لذا هیچ دلیل شرعی و عقلی وجود ندارد که فرزند یک مسئول نتواند مسئولیت بگیرد.
🔹
در واقع نام ایشان هم جزو کسانی بود که در کمیته مورد بررسی قرار گرفت و اتفاقاً جزو نفرات برتر آن مجموعه چند ده‌نفری شد./ باشگاه خبرنگاران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/685192" target="_blank">📅 10:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685190">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oW5LYp0N6YOCGfWFfDR_Io182yBcdKGFLBTKyPaaKxfMMwgmuv6lGMU0wYuokCxW0y0XdCwNCqxhTAVSwsltLTNjUCcpBaf_pQaAIV1wJEfKmxMWb81aTuUNeJODbgRoIPBGKiyowEKLHiQUSdUZ08sPapRKr-V95LjyXCyStkWZgS7D3wwKs-PXpZakSrJuJvr_FjFFNtCbL4OPWrg3lLoo-pjjr--7Up5EFfDEdAXoRUNxzUSnIZ6hbbsmolxUOXzfah8ckCZFrmEdedDr5rQ-2N1OMAIH_2Kt5rIwX9Tqfv73LO4gA2DUpnn83el2yoi_vO-dBx6-Axn2cQXJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/685190" target="_blank">📅 10:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685189">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKzPhhLytlgUWG-_nO4xafJ97DrVbbmkfub29UR4a7KgcQAhicx5WCX_6CVmLaX3sPbmOsJ_aOcxB-B2J3h-ON-lErzzsAyDy3wp7cQYQBCU869poKOXb5YMF4OBha55-TsB1os6g2phe7bVHT1uwvPMQCts19ifX04V9cFEeEOC3Y5RKtstq65r54QPjqiclRPWy8GKyR4kRRQgkk0jFaBudZZH9zXKPiIs78xqjQBDTaHAJ_nK0ftRrgXV7naBHg4I01JBEKhrGIbDuEmzigwhVI9sKJAq2gtEeNqSdSd1sEy0-jiWykpt5kkOW5XJiRLLTwducCNdfrg7Edbp0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان‌بندی تکمیلی انتخاب واحد نیم‌سال اول دانشگاه آزاد اعلام شد
🔹
بر این اساس، انتخاب واحد دانشجویان دانشگاه آزاد اسلامی در نیمسال اول از ۱۰ شهریور آغاز شده و تا ۱۹ شهریور ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/685189" target="_blank">📅 10:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685188">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85c696e93.mp4?token=YjiJHLgznGU4UiW39Do24ppmOFJp2bf7_iSqpJEi4OUNkxrDQcJXqcAFI_s_KNHAXV1ky2TzMYYsTi3uU2M6ZBa0QJBbhvXX3V1YQZipU9F7PawBBMYRmu_nmQMChGxiFAhaG2z68t0Wxjt9DwW79S4Ul-atAdx8f9OO1DBvP0aZZHzGrZQkU1JERT2CmQOjjzXySBqCET9xJzabDyKwB8-E37dIvpcr6hGMtQzqKLgpOiyvVhRkJxwecswX7hP7zVSdToOzZVDjqYAiDkzV3ixm_tm3GWMDWT8M17kcUOkqPqBkZGsm7LgZ4NTlu_MKzNmEdPz0YL-AzIMm-qQPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85c696e93.mp4?token=YjiJHLgznGU4UiW39Do24ppmOFJp2bf7_iSqpJEi4OUNkxrDQcJXqcAFI_s_KNHAXV1ky2TzMYYsTi3uU2M6ZBa0QJBbhvXX3V1YQZipU9F7PawBBMYRmu_nmQMChGxiFAhaG2z68t0Wxjt9DwW79S4Ul-atAdx8f9OO1DBvP0aZZHzGrZQkU1JERT2CmQOjjzXySBqCET9xJzabDyKwB8-E37dIvpcr6hGMtQzqKLgpOiyvVhRkJxwecswX7hP7zVSdToOzZVDjqYAiDkzV3ixm_tm3GWMDWT8M17kcUOkqPqBkZGsm7LgZ4NTlu_MKzNmEdPz0YL-AzIMm-qQPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهکارهای هنری جان گرفتند؛ هوش مصنوعی نقاشی‌های مشهور را واقعی کرد
🎨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/685188" target="_blank">📅 10:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685187">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bff5bbd5d.mp4?token=rpDSeg-FiO0aWM_n-Z959AsAgp7PXV2cDPR-24VO8CRoz1zMBazLCUcnCWhNECt63quiE__3Dz-kKetTYlO6qO8be-qqq84p0bMVjxmSzoGIah53a31DucVGwnvewVJEZUlRdV2Bdn-2FOLpk9CFmX1dVSJb_D7Wv75QPemALQW5rpmtaVDQKeUPwYU3GExL6Bqd_34iyTZBBhbDzMy9B2Zmf8rY9KAxS_w8kLD0ypzBcNVn1xIDKoNoNMfUbyR0aOr_28D-yr1cQHBZqwJPja0LnUhkFdNa83AtK_A2Ti9hTdn6cLclmEw5Q0NRYJt5eGn84gYcYsFg-cFDEIIMPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bff5bbd5d.mp4?token=rpDSeg-FiO0aWM_n-Z959AsAgp7PXV2cDPR-24VO8CRoz1zMBazLCUcnCWhNECt63quiE__3Dz-kKetTYlO6qO8be-qqq84p0bMVjxmSzoGIah53a31DucVGwnvewVJEZUlRdV2Bdn-2FOLpk9CFmX1dVSJb_D7Wv75QPemALQW5rpmtaVDQKeUPwYU3GExL6Bqd_34iyTZBBhbDzMy9B2Zmf8rY9KAxS_w8kLD0ypzBcNVn1xIDKoNoNMfUbyR0aOr_28D-yr1cQHBZqwJPja0LnUhkFdNa83AtK_A2Ti9hTdn6cLclmEw5Q0NRYJt5eGn84gYcYsFg-cFDEIIMPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیگه تن ماهی رو ساده نخور، با این دستور می‌تونی یه پلو تن خوشمزه و آسون درست کنی  مواد لازم:
🔹
تن ماهی
🔹
پیاز
🔹
سیر
🔹
زردچوبه و فلفل سیاه
🔹
فلفل دلمه ای
🔹
رب
🔹
شوید تازه
🔹
سیب زمینی  #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/685187" target="_blank">📅 10:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685186">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سپاه اصفهان: احتمال شنیدن صدای انفجار در جنوب اصفهان تا ساعت ۱۴ امروز
🔹
دانشگاه تهران: مهلت دفاع از پایان‌نامه یا رساله، بدون نیاز به دریافت مجوز جدید تا پایان مهرماه ۱۴۰۵ تمدید شد
🔹
جانشین فرمانده انتظامی قم: کشف ۵۰ تن تخم مرغ احتکار شده در قم
🔹
روزنامه معاریو: نتانیاهو در قبال لبنان با احتیاط رفتار می‌کند تا ترامپ را خشمگین نکند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/685186" target="_blank">📅 10:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685185">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b0344ce1.mp4?token=ol3w1v8JvZbjY0B3TcvJ3ULk7yecBkTH2xrSRS2FggM2GiWyIldfh7Nx9NJgi2gRXabocpghEkMsFlM9Bf9tD1sL0Y78iI9Wh-RskV0veZ_qwMmGAWy2DpdsVCnUpVLu2MpJe3-1Gqz6Wuuy5nTfqw-CzgiQ85DtYxbacrv2ifFsHWYd85sOwdTsKDXsOdv_cvokOyhEpBhDriEiDTXCql9BMAxJKujZ3MmxVfZOu5KN3OM6BY-8ViFlNKxztsDc00MVkUsxTs-Qb7wRkT9a2cJ41A4oYPdwaYSZ-W769UJp7uLKLxQF5jmqBEIktLokjOKcfEeeQ2LdqF_pdyzU0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b0344ce1.mp4?token=ol3w1v8JvZbjY0B3TcvJ3ULk7yecBkTH2xrSRS2FggM2GiWyIldfh7Nx9NJgi2gRXabocpghEkMsFlM9Bf9tD1sL0Y78iI9Wh-RskV0veZ_qwMmGAWy2DpdsVCnUpVLu2MpJe3-1Gqz6Wuuy5nTfqw-CzgiQ85DtYxbacrv2ifFsHWYd85sOwdTsKDXsOdv_cvokOyhEpBhDriEiDTXCql9BMAxJKujZ3MmxVfZOu5KN3OM6BY-8ViFlNKxztsDc00MVkUsxTs-Qb7wRkT9a2cJ41A4oYPdwaYSZ-W769UJp7uLKLxQF5jmqBEIktLokjOKcfEeeQ2LdqF_pdyzU0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یک آگهی؛ یک فرصت چند میلیاردی!
با مزایده مناقصه آگهی‌های مرتبط با حوزه فعالیتت رو مستقیم دریافت کن و هیچ فرصتی رو از دست نده
🎯
https://B2n.ir/mozayedehh</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/685185" target="_blank">📅 10:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685183">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8096f43c1.mp4?token=DGWjdlYDtOMpOtR8LhUxCYQrtpPU53yhhhzb3PgK5ingZgeNNzpIEt440E_kt9X7rk65jA4C34M5JwMSJQqJu_guxHAY4xbH4InZGddXffxu9cWmbf23xzCDrBbm7uxr88nM1zLsOXkhZ_vuO7-v9p2C8pDU0VazEWPyEynTywGg_m_5ZLiZNJX6sc6SOCpRwf6HG_gpDGyWFByXWuKmjkA6PWOew5akMiOdfcw1Li7gStJN-VliX7vYf9PDBAI66pMQ8QoPaU4JTLsuGO-jLZzDmbVW30UNO4lunf28HngdUR3y92rRMPjhHpWVi7cRf8OrgtMjUtdYBEXZqOCaOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8096f43c1.mp4?token=DGWjdlYDtOMpOtR8LhUxCYQrtpPU53yhhhzb3PgK5ingZgeNNzpIEt440E_kt9X7rk65jA4C34M5JwMSJQqJu_guxHAY4xbH4InZGddXffxu9cWmbf23xzCDrBbm7uxr88nM1zLsOXkhZ_vuO7-v9p2C8pDU0VazEWPyEynTywGg_m_5ZLiZNJX6sc6SOCpRwf6HG_gpDGyWFByXWuKmjkA6PWOew5akMiOdfcw1Li7gStJN-VliX7vYf9PDBAI66pMQ8QoPaU4JTLsuGO-jLZzDmbVW30UNO4lunf28HngdUR3y92rRMPjhHpWVi7cRf8OrgtMjUtdYBEXZqOCaOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج تمرین در منزل برای عضلات پشت فقط با وزن بدن و یک حوله  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/685183" target="_blank">📅 09:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685175">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgmurmW25sn2XrFdGMfo30zGDfvfVS9IYFP0_rxMlerd8sSObXCOYXtSyuRD1hCHBtKQj4mYH3_eiSI6R-vcb7N_qu5w69kZ3PfUoP06Wj2wqxesrf_A5PcBPz43Dj7-mIRQBD7CU6YgqtOks7X5YTKUSSP95zSU3dtZlO0pwkV5Tyw6kP9akI55MEXr5bZBP6BN_D_W6e5lpFxqvla0MXnkjRyTOLivpGJqxD5e_82KOt3sR9Q33P5HAc7XDoSYbLKR3hy8tvbPTA72GDfpzbqz-nSZrRNLRbYheNulOpxwNh-XsVGIqVgpN8elfc7XjVALI986CGsUNB_Pse9b4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kykL-n0X0iAjbvN4S884dF8nwXXYSMfn0PjnmQRm7jBNstG8dwKCo_ax2zWNdznMFnTaaQ12u1T2rBFmv2VJM-XiAHCws168E2-s6Y9YBrNLWRWRaTR7YKeV0jfdiKfuRNEkHnPqpqeW8s3kGW0oFMl0UyQROOzBBStIGKSR8yh224bYExK8WsGzpscxmAOe4r7KezSUxNW52V83bHDhUL3pFxUQ07dexKnGQVjaGt9xNxcwsP3e7YbUTWdpZM_K6OFH0R4ipp4dfhw--VLbFIuk_oMVMQDBF4eECBeT6SoPbouxXs9xyQBNyWohSn0Ut6QJalf1Xpu_6ZIqUi7omg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gu7nrejrpjmP3nNIoIEVdOFI3Uv2UelNep7F88Lz4OhIdOE5ZuZpCbNeMKbLTuaeCiKlGlHayiztlDgZ-BqP_G0ZEInBtwupwvlsUKokwQ2w2enNXUCOqavgJ4DfhUNEjRjXA2TTYkJIYTUG4oH-V3D_dykxr3hc9AQN3Nuor8E3rk8rvAqa2QxFbzcp7mSWq34YHHS79pcic_TpkIlrsOTdPOYIgSWMjxrSD8znHaZOpp9Ngu6TxydcP5E9XwKCn-SKrDbhFEt4uTY_AwnnDYHY7X6FegorvMsccvZIng1ZIJCdtRn-zD4126fD2T-MK54nJQeilAr4STUUlSW2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qepG72zdcRZjBuf_zIDRxoiDTs7cwxzOL4IGhrXyAFBiHwIELdTfjgUuqaoap1IUdits2GcTlSMOkgM430rsU0cRU-xyg2QGOh8FLXiGVokUq9LuCp8WEV58mFnEIACEuNwiYOPcd4R7f7MHD4r0I4qHHDEqfH5LXR1ejSY-eJThLkZucms1wTTAHKpU9_31n-AH1yXkZzwf-RusMEcB608PdZUgbiWNj6twFQUwvA4KMqV91S8yCQU3Oa0wbg8UvzSzAmK42mch2Zpt3YXUhsNubmafslDuQ0mQtevtsfpqwbwVhixDvA7UKBHGt5nIg6f5eh7VcgMB8lzFdotDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apJ9ZwB1IixxADw1NXv8P_uRwQm7AtyUS2FqBShxSR9bIsSKa__5dB7Ryfa90v6CQ1T1u_hmOXKfdEVZNR_kPVxLBWubfrkQBVacJsArlltdDy4RjaPARvJCo6BfbnBnEmKkPkp1GZax1mDF8s1XciGHxivPCnmW04kjDm9MjlhAcJNWX66MTBSrOl9ZHEXmwTGDaSJhA-1cyFPr1Nn4ERCmb6YRH4PgNOS6i91n6-nY9e1pvx4bEOSCMFj9C9WX5Sg1zblWWsIVlvBvYIbL0dLGua4l-ImDfShGT7mOjwu7HZ_DPJqUrV_rUXPnvPFRLXQFRY0KYhFDTLJcMj-pxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfDt7Q6-Hzt_o8flXaSZihqVQI_wvQdOjSSW9kP0sf3Vff9_3Am_DN06_-PJaLRlcuFpWEUrpqq2H2FS20w7c2lKf3_QGwXZMAX3vRh-lxxqbopM8dMYor3x6lcXuUG_rfKTXdhoHzAA4gyzegkZH6Tyu4sfClRjiLobHqoeynNkpmlpICKkReM6okEaZdnF2ecUrQX-LG1AT_iJmuqDenMTXxwdSY3y1kgsYRou_1tnNwOFc5NJVGIAm0iApac4-TtuPBVQIUJ4tWzthp4EosXELh2CqgfDmPHMD-LF2spt_6Hqr6gQK9MLutESNU_udIDEj-JsxYO7vT9xJmBWoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از خواب چی بنوشیم؟
۶ نوشیدنی ساده برای شبی آرام‌تر و صبحی سبک‌تر
🍵
✨
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/685175" target="_blank">📅 09:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685172">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d30464c760.mp4?token=c5EqV1M3QYWD8xFitb5or-fJQVz0Pck1kXBsPgLGwTODLEEN-u2mkps2AMmHEUfQon0h_WEHdzfkk5lJ5hO1Jot73NIfHSgoiM_Zxp40NTDjE0jqi6FNdpiKs7r65yVber1STo_emeaM-wwRHU9K3ml6VpsDM7st4RXP9rgbE3wHFwZyF3FDpziCdS1m6N2xAyggoaKGjvXd27YC-gSjbwiC-FdWprkfCIuOFqYwlGq3dummUneEBRs2IqGx77GDOuIbk3FVADS6wUMVfYSNqgvrM6v3u_dNLTLtDidU1sUZzCyU-Knx9COLgGtnLWd7_NCnlsqP224CdLeupY6Eww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d30464c760.mp4?token=c5EqV1M3QYWD8xFitb5or-fJQVz0Pck1kXBsPgLGwTODLEEN-u2mkps2AMmHEUfQon0h_WEHdzfkk5lJ5hO1Jot73NIfHSgoiM_Zxp40NTDjE0jqi6FNdpiKs7r65yVber1STo_emeaM-wwRHU9K3ml6VpsDM7st4RXP9rgbE3wHFwZyF3FDpziCdS1m6N2xAyggoaKGjvXd27YC-gSjbwiC-FdWprkfCIuOFqYwlGq3dummUneEBRs2IqGx77GDOuIbk3FVADS6wUMVfYSNqgvrM6v3u_dNLTLtDidU1sUZzCyU-Knx9COLgGtnLWd7_NCnlsqP224CdLeupY6Eww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظام سیاسی ما مبتنی بر ایدئولوژی است/ صداوسیما در اختیار یک تفکر خاص است
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
امیدوارم با توجه به اتمام دوره رئیس صداوسیما به لحاظ زمانی، تغییر در صداوسیما اتفاق بیفتد.
🔹
به یکی از روسای یکی از مهمترین سازمان‌های فرهنگی گفتم، قبول دارید نظام سیاسی ما مبتنی بر ایدئولوژی اداره می‌شود؟
🔹
در موضوع دینداری به معنای عام آن، مسئولش در جمهوری اسلامی چه کسی است؟
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/685172" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685171">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ef145327.mp4?token=TRJi0X4DE1a3hnJZHAfPc0R9-IY9_ksyGgsRFYFxQBgVYO0h9pFNevJAYRa-3dZJ6dYqzZWFCPi--xe1xIg4peSbEGhoP_CjxcyRTXh_n1Rg9spZ8agOeqMmz-XF4d9tPLRYkuTbUUj6m_xv1ICNKEvzxHsbt3PzivHixgpK1t5sZTpRDMkBFA1sVfFdcS8QU3KDu-JtRdMg-5NbDOzutuPZ0dJMNHyDdTFVXzj1Wxv3458b5-je6A6cwwqrz5cGQJoqwU5b6p43LuL7ynakYTV-zYKRQqs_ZTamK6kyau8cz8GjrL36ndvMQR2el66K2Dw-e0cLBP1qGV3XEc350w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ef145327.mp4?token=TRJi0X4DE1a3hnJZHAfPc0R9-IY9_ksyGgsRFYFxQBgVYO0h9pFNevJAYRa-3dZJ6dYqzZWFCPi--xe1xIg4peSbEGhoP_CjxcyRTXh_n1Rg9spZ8agOeqMmz-XF4d9tPLRYkuTbUUj6m_xv1ICNKEvzxHsbt3PzivHixgpK1t5sZTpRDMkBFA1sVfFdcS8QU3KDu-JtRdMg-5NbDOzutuPZ0dJMNHyDdTFVXzj1Wxv3458b5-je6A6cwwqrz5cGQJoqwU5b6p43LuL7ynakYTV-zYKRQqs_ZTamK6kyau8cz8GjrL36ndvMQR2el66K2Dw-e0cLBP1qGV3XEc350w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیش‌بینی بارندگی و کاهش محسوس دما در این هفته
کارشناس سازمان هواشناسی:
🔹
بخش‌های شمالی کشور طی سه روز آینده بارندگی وزش باد دارند و دریای خزر مواج خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/685171" target="_blank">📅 08:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685170">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
نتایج «امتحانات نهایی» دانش‌آموزان فعلا اعلام نشده است
رئیس مرکز ارزشیابی نظام آموزش‌وپرورش:
🔹
تا این لحظه نتایج امتحانات نهایی دانش‌آموزان اعلام نشده است و دانش‌آموزان به خبرهای منتشر شده توجه نکنند. تنها مرجع اطلاع رسانی نتایج امتحانات نهایی مرکز ارزشیابی و تضمین کیفیت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/685170" target="_blank">📅 08:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685163">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6bv0Bc_WmYFnRNLFDS5zcFZpzNShyIryuHtNLDa6oyFJvLXBlWz1HFZzRIdvr-jAWgSu5ajvWAmvp8UWdQ00Uv3tiMKjissfkazL51VtU3TibBfQkSq1385qZ5DOuAAspz5WlMXgJZu_8Sd4VLewwJGN2zGW4Na36kDVWQ0pCtnJOQIrY7LqVrCsSX6YQ9-Ns8HNSSeKQtVx5W-eq7jXSk1CI7N_ApT5kj6BY0_2FQDuVlYqyIKyGbfCqCl0VS_9YmZLDI_sVyKD7a6sfx5lnI00Mh3Hi8G0AAuAV087nIzzjnvdvI7HdAPiBv2LXWl5prdu4-TxEHMeyOCcMH5_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBBFepR_r1VdaQAr8KB6o21vdHXjsDRJAz-ssTpSmZiVWByyMASQRVjs5ZGq4MWdI9rGWyD21FK_aNkb2F3PqkZvPblBz5iUDSUFWpoKr72zLMrQZDugUJSKL8zqSYOijztfS4w_DPC5Au2UxSLaVUIbyBD7ogj5iVkgpOni-lw_D96AmUIablw0ji39oGAxhN2zCFLP48q1dq7BlJCoJuOCUWamCjCmzEsunDRNruJ_pQ3CkLe7_MRAnkqueVa15XBd4WX0DdjgcwWtiJ_fcjtrtd6LkfEIri6dJCeYO4pn9nYvay6x0OQUhG6fJqJ65iCgdynpw431E9MZN0eLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSGsk1UKGmjMuTRVs3Bp_7mjPN14Y61jcWn1y5SM939ZEj2Ur7m7LQc7ZbTG-on9I-FzYpW2nXbVNUuEMa-cu8k74mKyZ_fZF-2m0sgHmso8gRALI9QWyFm9rmKXO-38e7w0Ct8GCkr-UPYoQ54TZTB6jh5P9ykruBWRvdPZXhjNoJ6-yUqsgidA6BCBgS4dc5iJvVYLpDYCqY2dMJ007LiGky_ZogAk80EBcPFVbd7n8a2urYJV_1CeQRwHMXmiqtglc0k2JA3jF9MTM_WsiIfzFNAo19fZQBPpS0TDs_cBgbXUuISWXBwEr8m8o0NnRxvDn19GorMs7QS7sIRMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRKmGS3T4gyv_SrTAkNLy1PzXYK-N8UDdjXdWn9-PsQM-X2p-Po5oGJHT_8sFAjUzuzFzarNF6tjPOMc08rFbxW886wqPvHcF43Otqni4Apd2zBSzBVisxs3HFMuDnBy5hTcM_pYgpiKuZ4opVIV8N91XskbCoVpm67iMkeg1bsj7XSPWZXHEE0yzZVJlSNaeCrmMsQgTGDXCMLCYm8hSN1q9oHNz21YQn_geBEyFJxV6cZusD9R5Es-ZJSHrJmZKODSefR0__IUKp1aTkOOj1sUDpOEuPQSUf9O0BeHpE9s4C-2ycfU542dGx-kv6J-XYW6W0EZjRvh6dHdYF6p2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/manaeKY0YVq3FoZ3dp4pbRt6g8WB5Iql5V-X3keJXVWin235wO3QSIH-CUkqjG5jEpEQDzSKLmca82mdKJpMVaOem-aU0IPMCiumF1Ae_R5aU48HCar4dgUioG0jq0mAy_b65_5dIOVRhSgrifVtYJFEeRdD0gJBK9-E0oyvBd2zfHIQnEMRIflRJhMPW_bU3TgjHLs4KIhvHdKtQey5ReFffgaRxLHwEHwkhtNhoLjAEoGnd_9YY0ZMMlbRPFWqxyWs6rxhkhUSQyLgHmORnhJFldgWx4SKSfhyqA1i6eB0g9A7BGcxQZMYb5PZZiamKA_0DoZmGXUuRC0n2y3eGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ اسکراب خانگی برای پوستی نرم‌تر و شفاف‌تر با این ترکیب‌های ساده
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/685163" target="_blank">📅 08:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685161">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
دستبرد ترامپ به ثروت ملی ونزوئلا؛ غارت ۶۵ میلیارد بشکه نفت
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا، در جدیدترین اقدام خود برای تاراج منابع کشورهای مستقل، مدعی دستیابی به توافقی با ونزوئلا شده است که از آن به عنوان «عظیم‌ترین معامله تاریخ جهان» یاد می‌کند.…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/685161" target="_blank">📅 08:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685159">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c23153cff.mp4?token=FCE5K8BPuV8vQSPXfZeJWJNLSY87zpCHYJWKmQMHHIlYtwfc6EjodnqdZWpM8OpCgmzL_hlplc7NZG24vF9lE5o16wsPrcqcwZ8V2NrZ0bshDGyJ27Dj7YbGB0gSrwDB_7DQHEUP7v1p_5bYKWYsLbQdRIemV2QPf9Flk5MwsWNPHiUiqz1hZ6F2mig4nxF2ZFzA_5nOVsZgZg_UoA3eLgZCgE4FAv0pAoBAr2RKwV4GKpTyeiXBI4s7bLfH8fZTSHN7fLifgWFzQKj9Su5knf_f6CCyD2B3VWoUb2i6CBgOMRF07048OEfR6OtRe9cHROMHgF33Zea6jEVcqS2M0avESwcPyFHP-lgLUi6g4t-YP4qMRB2t5R7tPluR9UwDSVT3F6RLALDk0a92UpP_kT7uDEgGGEMBi1n-CAj--A3PTLkQmnl8bQyxoFWJyxi-ouvhzHdQAFScFMCC_C_409ILVyAAssBHlrlDxKBCakth3M_lAdd16VvdGZD_D9P3M-92SOYBxFWkuYgWRCZjKxnLLgmZ7XpX3Sw_dUo7Q0eDCr6MqDgDoRLfFQ1A_gK3BDHb0pTjV2NXdrTyehXt7EyI74P09SqmvCPItaGk0k_ddAAh_K0caVpXd8cQmSi72BBLnL4PJqBiiZv7miD0gvACguxMHe79uF5uzGkhMBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c23153cff.mp4?token=FCE5K8BPuV8vQSPXfZeJWJNLSY87zpCHYJWKmQMHHIlYtwfc6EjodnqdZWpM8OpCgmzL_hlplc7NZG24vF9lE5o16wsPrcqcwZ8V2NrZ0bshDGyJ27Dj7YbGB0gSrwDB_7DQHEUP7v1p_5bYKWYsLbQdRIemV2QPf9Flk5MwsWNPHiUiqz1hZ6F2mig4nxF2ZFzA_5nOVsZgZg_UoA3eLgZCgE4FAv0pAoBAr2RKwV4GKpTyeiXBI4s7bLfH8fZTSHN7fLifgWFzQKj9Su5knf_f6CCyD2B3VWoUb2i6CBgOMRF07048OEfR6OtRe9cHROMHgF33Zea6jEVcqS2M0avESwcPyFHP-lgLUi6g4t-YP4qMRB2t5R7tPluR9UwDSVT3F6RLALDk0a92UpP_kT7uDEgGGEMBi1n-CAj--A3PTLkQmnl8bQyxoFWJyxi-ouvhzHdQAFScFMCC_C_409ILVyAAssBHlrlDxKBCakth3M_lAdd16VvdGZD_D9P3M-92SOYBxFWkuYgWRCZjKxnLLgmZ7XpX3Sw_dUo7Q0eDCr6MqDgDoRLfFQ1A_gK3BDHb0pTjV2NXdrTyehXt7EyI74P09SqmvCPItaGk0k_ddAAh_K0caVpXd8cQmSi72BBLnL4PJqBiiZv7miD0gvACguxMHe79uF5uzGkhMBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایستگاه بعدی: مجازات جنایتکاران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/685159" target="_blank">📅 08:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685158">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34a98cf014.mp4?token=Vm4eCR3uetSGISHh_VlbOKgd-xOC02M9CDKcuOJXtRUcFjT9-BexHFifiegCIQl27jJrsOuJThlTLve5kULnTU1U03MTzpjj5gab7y2VJSxBMUSpkzIiGI37Hvt1uNxkOLeY2YKipZwjMRMoNVqjBaLv-c_7JpaCVN3X-n3CTHxfJF8sSv-JUiuB00lEYU27qt_kb_EvXZqodqHiTdhUvjOnGrKj77QU99gFsdM8m821hJ6VKTIgIcJKs3BIVXU00sLfXPuqGGSW33Vtdz-M2kI-0Qke28aCBZT8gR8aM-goDbKcHFlHF8d7YmY1ojAR7fH43y7cfpZVThBkcK8HKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34a98cf014.mp4?token=Vm4eCR3uetSGISHh_VlbOKgd-xOC02M9CDKcuOJXtRUcFjT9-BexHFifiegCIQl27jJrsOuJThlTLve5kULnTU1U03MTzpjj5gab7y2VJSxBMUSpkzIiGI37Hvt1uNxkOLeY2YKipZwjMRMoNVqjBaLv-c_7JpaCVN3X-n3CTHxfJF8sSv-JUiuB00lEYU27qt_kb_EvXZqodqHiTdhUvjOnGrKj77QU99gFsdM8m821hJ6VKTIgIcJKs3BIVXU00sLfXPuqGGSW33Vtdz-M2kI-0Qke28aCBZT8gR8aM-goDbKcHFlHF8d7YmY1ojAR7fH43y7cfpZVThBkcK8HKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوابیدن خرس قهوه‌ای همراه با دو توله‌اش در زیر سایهٔ سنگی در کوه‌های البرز
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/685158" target="_blank">📅 07:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685156">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8668a9da0.mp4?token=e38MpbzyWTV53tgAOfujdTPvusby9-4XeBjLjPoizzV1ElUjg1OqORyqlR_iycTuYnt3-bORiXnMkJV5NcYt0V4cifGyOHmM4SEWH_Tgofp9b1PZHNvcTg37CAZb7i8zs6WviGZQR7gAbqb2hfAb1XXlvbjutOL8DGaVJN13zc2sUD8WaQeOSymaoEM-sfsXnzuV7zXhVBYYAEaiM9E-0cM3Ag9AaVLE_3xkHjMWyg20I5WVB3FdCoCbtwoLA70Txyq8gBdR3OARXUadZ41d6b7PmFyUAe3O_JNf_AcfQRw_iym0xW5PvqmA6rdrzQyKiYOts3M493GUWPNfGBodpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8668a9da0.mp4?token=e38MpbzyWTV53tgAOfujdTPvusby9-4XeBjLjPoizzV1ElUjg1OqORyqlR_iycTuYnt3-bORiXnMkJV5NcYt0V4cifGyOHmM4SEWH_Tgofp9b1PZHNvcTg37CAZb7i8zs6WviGZQR7gAbqb2hfAb1XXlvbjutOL8DGaVJN13zc2sUD8WaQeOSymaoEM-sfsXnzuV7zXhVBYYAEaiM9E-0cM3Ag9AaVLE_3xkHjMWyg20I5WVB3FdCoCbtwoLA70Txyq8gBdR3OARXUadZ41d6b7PmFyUAe3O_JNf_AcfQRw_iym0xW5PvqmA6rdrzQyKiYOts3M493GUWPNfGBodpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو میگه میخوام جهان رو دارک کنم اما بعد …
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/685156" target="_blank">📅 07:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685155">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تمامی مدارس دولتی، هیئت امنایی می‌شوند؛ دریافت «شهریه» ممنوع
معاون دبیرکل شورای عالی آموزش‌و‌پرورش:
🔹
تمام مدارس دولتی کشور از هیئت امناء برخوردار خواهند شد و دریافت هرگونه وجه اجباری از اولیاء تحت عنوان «شهریه» در مدارس دولتی ـ هیئت امنایی «ممنوع» است/ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/685155" target="_blank">📅 07:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685154">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN9P3BiL-b_qcdkzGeEViwUjPPjbb_RrbEUS-567JrxfOPPWh9kIKTX5yqhjakfLuX1pYMrpZL7eIXi1VayCgNQUlff-AVXpeLFxvv1XXHU1yI4s220jzAiNJZq1hdTV9LQ_4eEU_u21rkK0ww3I3hDGJjLdqvO0EmfmyUHzZ4vCU3I_3UAEeX-e9SBjYOswuQnpkwZpag1YnjQ11rBJG0jxVYjhiy2_dJ3YaZ_2djeaMM4DWy1ka4aKmnBU6BYQeixewprIfnCpfYuOefOzOtnkTwcnAGo3ulXpctAA1D-325wp1R4AnhLmEk7jxVgc-QhbgBTdeBh83GoeHXYNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاوروف: حمله آمریکا و اسرائیل ممکن است ایران را به سمت برنامه هسته‌ای نظامی سوق داده باشد/ تنگه هرمز هم پیش از «تجاوز آمریکا و اسرائیل» کاملاً باز بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/685154" target="_blank">📅 07:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685152">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByhBsZZ1Y91vjeG4WpSABJV3EfntJqW3uDl2JPjpHgNpWopISmMUUpTPzPLDPeODehV3EXg8NBsfuX20owl_Y16QykVoEPNmkVQwnpmJrQnMDRGBzbCL9DVPGPStsj-4-1jbR4dErqK1gutfpBI-LJXrdGivB3Sbp11DgpZhhZUTQjcDdvzlg2r18mdNy7vmjqveze9AXtwqi566_jBE-s--eNmaockPCYJYYuoOYLzk031sxItzWfxZnyhOEvdGMpQT-JRM6IuVf3DPTMvHjopDo2iu0FZy_TZyNEvm6MG4wbHN0XcqK9zj1sOJ4tPYUbS53u-hqG1Cyt6cn6MGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۷ شهریور ماه
۱۶ ربیع‌الأول ‌۱۴۴۸
۲۹ آگوست ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/685152" target="_blank">📅 07:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685151">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
دستبرد ترامپ به ثروت ملی ونزوئلا؛ غارت ۶۵ میلیارد بشکه نفت
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا، در جدیدترین اقدام خود برای تاراج منابع کشورهای مستقل، مدعی دستیابی به توافقی با ونزوئلا شده است که از آن به عنوان «عظیم‌ترین معامله تاریخ جهان» یاد می‌کند.
🔹
ترامپ با افتخار اعلام کرد که وزرای امور خارجه و جنگ او موفق شده‌اند دسترسی واشنگتن به بیش از ۶۵ میلیارد بشکه از ذخایر قطعی نفت ونزوئلا را تضمین کنند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/685151" target="_blank">📅 02:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685150">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا در اندیشه تصاحب کاخ سفید
ان‌بی‌سی:
🔹
پیت هگست، وزیر جنگ ایالات متحده، در محافل خصوصی از احتمال نامزدی خود برای انتخابات ریاست‌جمهوری سال ۲۰۲۸ سخن گفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/685150" target="_blank">📅 01:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685148">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RANkznHi4COtf8dNXi2k-SE_0kpYAT_8C3nwuwZxlYUIlcqk2FqOVjAgOajyXY1inCzvTZBmUKheIB0QyvfxOQvQgWNSsE9LgObyoHUmlpjWdzXT1ai0NGgkmA-o9dI_ullOv7J1oS_232E8K1-Cw-6-sDRovn-IOIqrIlldypxf2-MRP8eXAi8R5Qw374d46PkSpebaG0OMKgC3oBTScPYH2RxC_IZsLAQU3Jg5hA5VpEC4qV3pTM-6GrKQ8GvmNLZ_58I9gDrbwVQQFswd00raKHAneN5QeUYvgY_atTrHLR5ogdxaW2bsDpuwuMI7_8shi0qU5UWj66ycg-FLnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمان قاطعانه
🔹
رهبر معظم انقلاب اسلامی در پیامی به مناسبت هفته دولت ضمن قدردانی از اقدامات شایسته دولت به ویژه رئیس جمهور صادق و دلسوز فرمودند: قاطعانه اعلام میکنم ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است. ایشان در فراز دیگری از این پیام فرمودند: هر دوگانه‌سازی موهوم از قبیل جنگ یا مذاکره، وفاق یا تندروی سازش یا جنگ‌طلبی می‌تواند به مردم عزیزمان خسارت هایی بی‌واسطه یا با واسطه وارد سازد
🔹
هشتصدوچهل‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/685148" target="_blank">📅 01:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685147">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b99343099.mp4?token=vNxTl3ElvwVQ3OhqCugYa-eau-pZFtlkkE_jumH4Xj06Kssz3cAWuNglHSR_Hm7e6_U00Py4y3cEy6IoHyCUY5m56wYZteR3Py_x9GQ8bBdI3tiBey9jy35Hwd_kyyOmvk_ZA0WvsA-qzo-nAGi0tIaP68RqZdUkDm9Y5eY6OiY_If0eqxb2WmC2grnFXB43ENLjZih2cMxFdt5KZLuyPkVginox4ddqL7wRQ0f0JAN8FoGAZKouzsbZHy4qT6E8gtuGrfp58S4c6DR_juyVGl0OCurxaz_XzBTfAg5GI53_sxfZK4Ax_qNyu4wpd_IvZki4wj_hejpkiicXXd_WnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b99343099.mp4?token=vNxTl3ElvwVQ3OhqCugYa-eau-pZFtlkkE_jumH4Xj06Kssz3cAWuNglHSR_Hm7e6_U00Py4y3cEy6IoHyCUY5m56wYZteR3Py_x9GQ8bBdI3tiBey9jy35Hwd_kyyOmvk_ZA0WvsA-qzo-nAGi0tIaP68RqZdUkDm9Y5eY6OiY_If0eqxb2WmC2grnFXB43ENLjZih2cMxFdt5KZLuyPkVginox4ddqL7wRQ0f0JAN8FoGAZKouzsbZHy4qT6E8gtuGrfp58S4c6DR_juyVGl0OCurxaz_XzBTfAg5GI53_sxfZK4Ax_qNyu4wpd_IvZki4wj_hejpkiicXXd_WnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تکان‌دهنده از طوفان ویرانگر در مالاتیا ترکیه
🔹
ساعاتی پیش، وقوع یک طوفان بسیار شدید در شهر مالاتیا ترکیه، تصاویر وحشتناکی از شدت قدرت باد و خسارات وارده منتشر کرد.
🔹
تصاویر منتشر شده نشان می‌دهد که شدت باد به حدی بوده که تابلوها و اشیاء سنگین با سرعت بالا در میان آسمان به پرواز درآمده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/685147" target="_blank">📅 01:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685146">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9170b3a64e.mp4?token=DU1OXWmU0kY37Nhcjbu2Cjgk60pAORQxXi6CQVoTmiQDYh4fqrXdpfiBNYdK0UOSok9ZwMf1QQUjVSILZw76I_mTdXL9XecFJUehRPoJmJ1Z1OdK6k_ek-BvfgmiGVDOEN89d81zlFe4sHrfouBCtuDFAwzy7cKrRcaLfZ3s_BUsGz0xXzZdkP51o3dbTm-xUe6BknwSIP3rzl9eNy7NvC7ouufBv3lZAU5v92Ug-kPfjhKWnClF0eK6D5e6XKCH3ISQrHP4VMziwH-xth-4edwIdPirKLazPDlnKnUzTHjLdxUedgUk8I7kbVhCy70HrnUk6ZHRneYXTcYZOPbNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9170b3a64e.mp4?token=DU1OXWmU0kY37Nhcjbu2Cjgk60pAORQxXi6CQVoTmiQDYh4fqrXdpfiBNYdK0UOSok9ZwMf1QQUjVSILZw76I_mTdXL9XecFJUehRPoJmJ1Z1OdK6k_ek-BvfgmiGVDOEN89d81zlFe4sHrfouBCtuDFAwzy7cKrRcaLfZ3s_BUsGz0xXzZdkP51o3dbTm-xUe6BknwSIP3rzl9eNy7NvC7ouufBv3lZAU5v92Ug-kPfjhKWnClF0eK6D5e6XKCH3ISQrHP4VMziwH-xth-4edwIdPirKLazPDlnKnUzTHjLdxUedgUk8I7kbVhCy70HrnUk6ZHRneYXTcYZOPbNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: من نمی‌توانم جواب خدا را بدهم، اگر نتوانیم مشکلات مردم را حل کنیم ولی درگیر دعواهای سیاسی باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/685146" target="_blank">📅 01:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685145">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6324af0fc4.mp4?token=SVMzYeBRGDSX30eYEWIXuviFaVesjXjWo735g_eVsipdbY8afdYll2uFUvU7lFYONzTdEckDDKWJi9pzs2hN4Ayj_m_3S3WxUpPZqml7DDnz4J8odK2_0tWEUVvZUYHvv1oIK2-cJ2zmZMDXeogu8wN3X0qfU_hYeaNMkwUVK9IqXEnlnEHNwoEx9Ul3DvIXrE5UAv0Ud2_oRLgLNWnLYghTFGNR44LeNzSUDF16LzuxRM9ygCMxSOgxpan7MpriYaVMHbvz3jg7XEFIyItA2Zuf4_VN2Z7kivw8AXdtMwrfhJBYvzydvN3vk5J-qPJzTNgpobe4srLvA1lFoIPA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6324af0fc4.mp4?token=SVMzYeBRGDSX30eYEWIXuviFaVesjXjWo735g_eVsipdbY8afdYll2uFUvU7lFYONzTdEckDDKWJi9pzs2hN4Ayj_m_3S3WxUpPZqml7DDnz4J8odK2_0tWEUVvZUYHvv1oIK2-cJ2zmZMDXeogu8wN3X0qfU_hYeaNMkwUVK9IqXEnlnEHNwoEx9Ul3DvIXrE5UAv0Ud2_oRLgLNWnLYghTFGNR44LeNzSUDF16LzuxRM9ygCMxSOgxpan7MpriYaVMHbvz3jg7XEFIyItA2Zuf4_VN2Z7kivw8AXdtMwrfhJBYvzydvN3vk5J-qPJzTNgpobe4srLvA1lFoIPA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به جهان نشان دادیم که آمریکا و اسرائیل قادر به مقابله با موشک‌های ما نیستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/685145" target="_blank">📅 00:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685144">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6d2108a7.mp4?token=p21JwKRVOS_linALRuOWdm1et1OqwiCnd2Q9au9d81XFMbKs5_FWGVfJii0CGtOljLdwwG3jc1WtVQ4yfhmsgZny3Z0mo_ps5zKvQlNogWZT7U_iWcwd_EMsMGJC_PnrebKR-HyE6yBIERAHF-cV5cxW4z9imsxEyMFCHGbNQ2c-JEKcftQhdl2E0GY0uLrhH0ldpckq8ROKHPUbl4wf8H_qmffaa_ayA_JKtfb5Gydfxi7CbS6gQiWZa3bzdEcE54DpNPgsAWIwQIw4Sefoiwwf5gyZm4ROByUMJG6jZ1XA0bLndwI6AINT6yiG1CKxjGRBpPdNkeRoEMwEnonNQwk9zVR_KvGmC_XZOtXoevUAtr1FSdogo1rQ0-65qAweZKA-rxSg22KkeOjMA3U5kPD7O3U9a9FVbWMrV6CQVT34K33oYrh-dGOCOCB4BmwTh9w__QnRq4wq8Ym-TK5cJK_bUZygw09cLXNs1K2F5QFqwQFVLmndSa9AdFxiO2Rusa9Ui2h0f3DWK6dHQ0E6DgD7uuxVGh-USCaNwT_9Nz7gFe69UkNY3qk5hrxHclVoij8IGfPJ9QQMZPMAFRnKMWeZnwMW52Hlp66sugVArgik35dj-Xn5k4fl4DHkf8sME3ayKJLWd9sgePAy1BOXfgvcPAHoRIBS5GaSegf7Z8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6d2108a7.mp4?token=p21JwKRVOS_linALRuOWdm1et1OqwiCnd2Q9au9d81XFMbKs5_FWGVfJii0CGtOljLdwwG3jc1WtVQ4yfhmsgZny3Z0mo_ps5zKvQlNogWZT7U_iWcwd_EMsMGJC_PnrebKR-HyE6yBIERAHF-cV5cxW4z9imsxEyMFCHGbNQ2c-JEKcftQhdl2E0GY0uLrhH0ldpckq8ROKHPUbl4wf8H_qmffaa_ayA_JKtfb5Gydfxi7CbS6gQiWZa3bzdEcE54DpNPgsAWIwQIw4Sefoiwwf5gyZm4ROByUMJG6jZ1XA0bLndwI6AINT6yiG1CKxjGRBpPdNkeRoEMwEnonNQwk9zVR_KvGmC_XZOtXoevUAtr1FSdogo1rQ0-65qAweZKA-rxSg22KkeOjMA3U5kPD7O3U9a9FVbWMrV6CQVT34K33oYrh-dGOCOCB4BmwTh9w__QnRq4wq8Ym-TK5cJK_bUZygw09cLXNs1K2F5QFqwQFVLmndSa9AdFxiO2Rusa9Ui2h0f3DWK6dHQ0E6DgD7uuxVGh-USCaNwT_9Nz7gFe69UkNY3qk5hrxHclVoij8IGfPJ9QQMZPMAFRnKMWeZnwMW52Hlp66sugVArgik35dj-Xn5k4fl4DHkf8sME3ayKJLWd9sgePAy1BOXfgvcPAHoRIBS5GaSegf7Z8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلیل اجرا نشدن طرح پزشک خانواده از زبان رئیس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/685144" target="_blank">📅 00:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685143">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b28c66f962.mp4?token=SygC8-CWQX1si0buHYkwboavECxbRRfFLAchcOcqeB_kjQFj0Aw4bJtbla630CB3IlTSvtlpo9vbeeuvGlb8IQP_mHXOHIEDg2AlmclTFwsKF20Gz40kiGZ32qq_xogaMuhBCuK8XxoW2Q290xVEoIx4vk5p_OjQqi3GU2HrsUjcWlqj-sv73ULteuXUAaq3F1eVr2fmtFRnrqlW4FY5n7ZMYNqK0ULgnHoKCwhqUFJzUn6niizhwIaQKn07aTSKe4z7l1ahCA3-45Gsio5qveyMzXP71W9KDZfva4IzlE3KcPrC_ufJePVkpy0UsZeS4PmWLAV3L1nxdS1-kZ86EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b28c66f962.mp4?token=SygC8-CWQX1si0buHYkwboavECxbRRfFLAchcOcqeB_kjQFj0Aw4bJtbla630CB3IlTSvtlpo9vbeeuvGlb8IQP_mHXOHIEDg2AlmclTFwsKF20Gz40kiGZ32qq_xogaMuhBCuK8XxoW2Q290xVEoIx4vk5p_OjQqi3GU2HrsUjcWlqj-sv73ULteuXUAaq3F1eVr2fmtFRnrqlW4FY5n7ZMYNqK0ULgnHoKCwhqUFJzUn6niizhwIaQKn07aTSKe4z7l1ahCA3-45Gsio5qveyMzXP71W9KDZfva4IzlE3KcPrC_ufJePVkpy0UsZeS4PmWLAV3L1nxdS1-kZ86EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: در این جنگ موشک‌های ما امتحان خود را به خوبی پس دادند و به خوبی از کشور دفاع کردند
🔹
یک نکتۀ مهم ثابت شد؛ هر آنچه در داخل کشور تولید شده بود، بهترین کارایی را داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/685143" target="_blank">📅 00:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685142">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb44ce39b.mp4?token=WuKuCAhVLqxUNwkgwRu70CPGiSMhtDJAvoVnRXiG4huNKF6SMclK5CvB0boblSHYOCE2VfF58AViqFL6veh-L19fYCWdxFYw9WtGgVaw4LVUZFJZwSxC-GykltIUbP-X76hiMPMarPF29Jsvxwmp7-y6YVoVVFvd9efLqj7_XOaULtfyhiJ6KzyX8JOL48NiwaiHmSR6P9Fr9vxSuS59JI78Ymnjz8QkP4D2T-DC7FUARvUiTRhkmy7VnbF9D1rrvQsNm4JIurFMN-CdD480ONCUqVVhRz_N46DoZrf74qs84aIEtcrXdThTyC8k3vLNJ7it5B4tU5doiSqaDGRmXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb44ce39b.mp4?token=WuKuCAhVLqxUNwkgwRu70CPGiSMhtDJAvoVnRXiG4huNKF6SMclK5CvB0boblSHYOCE2VfF58AViqFL6veh-L19fYCWdxFYw9WtGgVaw4LVUZFJZwSxC-GykltIUbP-X76hiMPMarPF29Jsvxwmp7-y6YVoVVFvd9efLqj7_XOaULtfyhiJ6KzyX8JOL48NiwaiHmSR6P9Fr9vxSuS59JI78Ymnjz8QkP4D2T-DC7FUARvUiTRhkmy7VnbF9D1rrvQsNm4JIurFMN-CdD480ONCUqVVhRz_N46DoZrf74qs84aIEtcrXdThTyC8k3vLNJ7it5B4tU5doiSqaDGRmXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک انفجار بزرگ در کی‌یف، در نزدیکی بزرگراه ژیتومیر، پس از حمله روسیه به یک انبار مهمات اوکراینی رخ داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/685142" target="_blank">📅 00:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685141">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb2b55416.mp4?token=ojAMTa70htpZp5x_bAHRBN3AU_E3-zUFdHK3kIp35xB4UFaErxzKjQdzSsk__Gk4AY43AkWqZb9F5S9xyXr1za1Cu1z03usQUZvJtNYGdPXa8R1I6-8m58Vvflcg0K2PnscBEuOtP_pOIcy9zIx-zE_Tu41SYWZ7L1tAyL1LuqQvAIQrj-sc3Plw0g3KIXM5EA36q5mIVXpAWaMrFaGzkznQgDd4YSIRsZ9cLMYZ2c1KyFO_wIr9fIfVqQL2HnfGgW717TA2HPPsZgjScERJJ6V-GsGVPV6iOMHe3GPjO7ZZXH-IAtR5uFDi4agjkkhkMzukH3doz5r598N_Zd08G560E37WfIzvxecIjTEKSgZVEMgM_sgK47wvX9f_fRZdgaTWwOxA0EpaEVW6-76_xhKOuirCkK1bArZZQXv3AYngMHJgfTu6k8w9qiR60MkOcom0qJo_vzkwem8ZaaOBQd0TypGoTm6xP6-nG0T3_OpUpEv4bbmMJSeZdjP-jG7_U8jU9y9Wa0KvCypQqtNUECD-pSDEp-vieHjjOhdZ50_Hi7L6DKA5pUxE0W3Qx_TbyhIo4bLseMpdWqvzCSILgqK4b_vtPZjIH3_i1EELSAK2iDkSLlDk42PT34JmThjIQqIR0LdLEuRCMUfzsOIsI1DIzuMmpCLt2u5hmHTxqSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb2b55416.mp4?token=ojAMTa70htpZp5x_bAHRBN3AU_E3-zUFdHK3kIp35xB4UFaErxzKjQdzSsk__Gk4AY43AkWqZb9F5S9xyXr1za1Cu1z03usQUZvJtNYGdPXa8R1I6-8m58Vvflcg0K2PnscBEuOtP_pOIcy9zIx-zE_Tu41SYWZ7L1tAyL1LuqQvAIQrj-sc3Plw0g3KIXM5EA36q5mIVXpAWaMrFaGzkznQgDd4YSIRsZ9cLMYZ2c1KyFO_wIr9fIfVqQL2HnfGgW717TA2HPPsZgjScERJJ6V-GsGVPV6iOMHe3GPjO7ZZXH-IAtR5uFDi4agjkkhkMzukH3doz5r598N_Zd08G560E37WfIzvxecIjTEKSgZVEMgM_sgK47wvX9f_fRZdgaTWwOxA0EpaEVW6-76_xhKOuirCkK1bArZZQXv3AYngMHJgfTu6k8w9qiR60MkOcom0qJo_vzkwem8ZaaOBQd0TypGoTm6xP6-nG0T3_OpUpEv4bbmMJSeZdjP-jG7_U8jU9y9Wa0KvCypQqtNUECD-pSDEp-vieHjjOhdZ50_Hi7L6DKA5pUxE0W3Qx_TbyhIo4bLseMpdWqvzCSILgqK4b_vtPZjIH3_i1EELSAK2iDkSLlDk42PT34JmThjIQqIR0LdLEuRCMUfzsOIsI1DIzuMmpCLt2u5hmHTxqSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری خداداد عزیزی با خبرنگاران یزدی پس از بازی با چادرملو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/685141" target="_blank">📅 00:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685140">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY47LK3v6tBvOzo2zsDBa88jDbeSSVc-9HyklJZYWmcJXp62ZAYfdcUx2hSLks9awzCM5R9H3aHOsnGL3dXqrUnbCXNktIj-jlj429gbUcRiKgpmiDmssCgqkoAQWn46URHeVfxvMMoHBxOql10jk13dcbj3NQS-bMavI6c-4o62hBsHI87yobvxz4f0aNJiiU5VFLguEFdlWHmbF6P9N9PZQboyxu94EkmLksrwpj8RHOtzowsgGh4-EHgnK34_VUkv0sVMRSX3iRhd5XygvyOeJs8-k9Rlz-ushYYMko8USi5p28_k8t8rIEghdnVGi8xF339s09pt6bvaUqb2cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/685140" target="_blank">📅 00:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685139">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f44195a3.mp4?token=Pqu74Vn8ZiFp-rvA6Y4s6fuDUDt08H0o8O1XRGgx1J6ruDeUaTeR0l_g_t-LT1_bbko2Qh0GFtQn6P38MVmI-YiQHpHB5Xk9XoizPCk6x53iXSKfu4shUTQaFfCw27Ou2mkVxlGpdxRvJxTw3ncczvuQ5JDskaueYV0Sbtc_p0KhzzsavZeylhJ-bM8eMlCip5ce3eAlqdplUuRfQKvVpTBPSAgpIQ7gNLcQ5HBq1gYI_J4iRBPfkuyCMI3ZT3_YFEgpJPg24rMQJYzSiJ4ig7m8eoHfLfEK_z2pkHSRsww0QH4KtzOoP9F-v7dJUR-aZqr8HDA9T6r3fbNrF-Icuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f44195a3.mp4?token=Pqu74Vn8ZiFp-rvA6Y4s6fuDUDt08H0o8O1XRGgx1J6ruDeUaTeR0l_g_t-LT1_bbko2Qh0GFtQn6P38MVmI-YiQHpHB5Xk9XoizPCk6x53iXSKfu4shUTQaFfCw27Ou2mkVxlGpdxRvJxTw3ncczvuQ5JDskaueYV0Sbtc_p0KhzzsavZeylhJ-bM8eMlCip5ce3eAlqdplUuRfQKvVpTBPSAgpIQ7gNLcQ5HBq1gYI_J4iRBPfkuyCMI3ZT3_YFEgpJPg24rMQJYzSiJ4ig7m8eoHfLfEK_z2pkHSRsww0QH4KtzOoP9F-v7dJUR-aZqr8HDA9T6r3fbNrF-Icuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: کالابرگ را برای برخی از دهک‌ها افزایش خواهیم داد
🔹
از اینکه نتوانستیم کالابرگ را افزایش دهیم، شرمندۀ مردم هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/685139" target="_blank">📅 23:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEYVGbxTZ63Y7TUGT54QKXe4kt7407-8iEuFWXU1zraoV_Ojhsxaf5npgKVE2XpOr6EOvVajF6x5B5AzRXHR8MfyK8QOXgNmGhexRxlqNNFCJma7--fqJJNDtgKVk5CofuP2goyHFRqSg6WFTygxvLh7eMb4MVrBBrH9AHPxEjlYL1J8a-Q2WtyFyNEF3R3cnuQOoKts2Z9uYX3yTw7YLwmIOBgoh9UPBGD7ywrNjPQwfIpdE0sm1eUtxJ7-ShadfZnx9ucWXgH-PNYlT2Dd1nXgoAbd3hgK_yNt9LSWYvhXEjNIxERPB3JzTGrUjejJ3B8umWaHAQYZ5I9gV6_Ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات تصمیم نهایی دولت درباره قیمت بنزین / از کاهش سهمیه‌ها تا افزایش نرخ سوم / تکلیف سهمیه خودروهای فرسوده چیست؟
🔹
با اظهارات امشب مسعود پزشکیان، حالا روشن است که بنزین احتمالا همزمان با کاهش سهمیه‌ها، رشد دو برابری نرخ سوم را تجربه خواهد کرد.
در وبسایت خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3241164</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/685137" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685134">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj1M8fiw_udQTEql3DXqDlEBvHpolEAJElUZeb6TVHb4hJyP__mDICd33sfubUx6jP5ce1eMd7hz8omgELs-1tGhBTiRMlmUdf8GxHIMYEddCZjT6CYw_Hu9ie5G_epV-HJSFKWrFqO7ljhtQ5jDg5cbKXKWHt5wPQO7LJjKYYV-tglLPbMLx7JLkBaSzDpE9de_Q1DnqfODVU5ECjp7SHLro8XDE5enksw2NF24L6tDT02dTqOwyjvJYIeHCQaj6gdW9CuY0cMrydatWmFXWM-yhsckQr51wC2jsQ83cR_O70pMmMZxxZljKp11iszWYiu7N1xaC4BlRQ9uLDC-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور آمریکایی: وقت پایان جنگ با ایران رسیده است
آدام شف، سناتور دموکرات آمریکایی:
🔹
پس از شش ماه بدون راهبرد مشخص و در حالی که هزینه‌ها افزایش یافته و نیروهای نظامی آمریکا از خانواده‌هایشان دور هستند، زمان پایان جنگ و بازگرداندن نیروها به خانه فرا رسیده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/685134" target="_blank">📅 23:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685133">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41d8f1090.mp4?token=nQPIxH6ZNSVceSAoafXsEH9mvB2ytMkHomerjVtugrjp1RPiLIyWgnRZXKFmHAQk5Z6tkQdMe7pF8ehVRoBqyxIKPie3eHDSlMyNJZwRachLzINdqY1NlmFW1HgHMtX6XmEEgvhJfEQnPeDCAXPtSP1-foujUUOr9bSw7pWovQ6f1fC3j_IvCwMPDclS0E-mJTXSBeuwt4gaNGNtXutORXmRByRN6MplN7tWto-_ThkbSkdrU-ZDQJsfLr4M76ZIvXjWAJOKAwbU3OKQc2Fo5LgIHnDSrDTItREuV-TdluOD8F2EsQSlujFGKQJWZElYlH7xmyM8wmg8lG6wtVf_kDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41d8f1090.mp4?token=nQPIxH6ZNSVceSAoafXsEH9mvB2ytMkHomerjVtugrjp1RPiLIyWgnRZXKFmHAQk5Z6tkQdMe7pF8ehVRoBqyxIKPie3eHDSlMyNJZwRachLzINdqY1NlmFW1HgHMtX6XmEEgvhJfEQnPeDCAXPtSP1-foujUUOr9bSw7pWovQ6f1fC3j_IvCwMPDclS0E-mJTXSBeuwt4gaNGNtXutORXmRByRN6MplN7tWto-_ThkbSkdrU-ZDQJsfLr4M76ZIvXjWAJOKAwbU3OKQc2Fo5LgIHnDSrDTItREuV-TdluOD8F2EsQSlujFGKQJWZElYlH7xmyM8wmg8lG6wtVf_kDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: اصلاحِ کشت شدنی اما زمان‌بر است
🔹
واردات و صادرات ۲۵ تا ۳۵ درصد کاهش یافته است
🔹
خود من زمین کشاورزی دارم؛ هیچ وقت از آن سودی نبردیم/ کشاورزان ما اگر خودشان کار نکنند، کشاورزی هیچ سودی برایشان ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/685133" target="_blank">📅 23:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685130">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b6efd56ed.mp4?token=na0ZFHbT54-KPhvP8C1-5xhRae2yeNfkKHVZsx9Mn3TX4DniQrNHk6P-zI8kcbDcSBp4d3x7Q0CHBJ6LJM3TPTU_3S7FvqHpCZNiScR6eBuDSyeIxY0H0rtLnc6YAdPEqKwF_9OBxbF4-LFEpnHWkESHdonnEUS2QOinz86JVghTOADccvGvw76d1TZfjdYWVIRchsshkcW_H7zVezWeUne9gsvSA63PRGFr_3ZH_x4oEQYuxsJrxWfQ6F7mwVT_1H3p2EcvRXDgRRwQgZVo5Xz22Ptzy4VqROILqZReEbUpJ1E2A9w7Wn1oknidR1KmmfnpGIjQs76rUeyTMmJQRJvJ2nC8UaJjh0hLS4KlDIp-pwpAqapAF2B4pHJ0FUtHV0_Nf7KZh0U1Nhu5KCuRRVHT4QWRlzjHZfpgsvcW6usZhwu3NLB4y63AEN2KVM_5slQxzuMECDeRajtTXsE5u1yV9-W99kVwsj4gRET2CW5XAJURsEQj8HXDn-hS6RXMIX9jWy2C1TPg4efPLfH61GR0ve3KrRECX3qKhDduXq2I3jI9VQEHe00Nabew8qEH1k4OIf3ZnQbnnd73ICbfrJwPtXk70zuOCQkfNGhNBby9QRkQJOXPEc8M_neMXWRj0Ht9gnIVGO-ysZa71Tt9FEzClCkaceP1GT6rii5bVV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b6efd56ed.mp4?token=na0ZFHbT54-KPhvP8C1-5xhRae2yeNfkKHVZsx9Mn3TX4DniQrNHk6P-zI8kcbDcSBp4d3x7Q0CHBJ6LJM3TPTU_3S7FvqHpCZNiScR6eBuDSyeIxY0H0rtLnc6YAdPEqKwF_9OBxbF4-LFEpnHWkESHdonnEUS2QOinz86JVghTOADccvGvw76d1TZfjdYWVIRchsshkcW_H7zVezWeUne9gsvSA63PRGFr_3ZH_x4oEQYuxsJrxWfQ6F7mwVT_1H3p2EcvRXDgRRwQgZVo5Xz22Ptzy4VqROILqZReEbUpJ1E2A9w7Wn1oknidR1KmmfnpGIjQs76rUeyTMmJQRJvJ2nC8UaJjh0hLS4KlDIp-pwpAqapAF2B4pHJ0FUtHV0_Nf7KZh0U1Nhu5KCuRRVHT4QWRlzjHZfpgsvcW6usZhwu3NLB4y63AEN2KVM_5slQxzuMECDeRajtTXsE5u1yV9-W99kVwsj4gRET2CW5XAJURsEQj8HXDn-hS6RXMIX9jWy2C1TPg4efPLfH61GR0ve3KrRECX3qKhDduXq2I3jI9VQEHe00Nabew8qEH1k4OIf3ZnQbnnd73ICbfrJwPtXk70zuOCQkfNGhNBby9QRkQJOXPEc8M_neMXWRj0Ht9gnIVGO-ysZa71Tt9FEzClCkaceP1GT6rii5bVV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلایل گرانی‌های اخیر از زبان رئیس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/685130" target="_blank">📅 23:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685129">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
پزشکیان: واردات و صادرات ۲۵ تا ۳۵ درصد کاهش یافته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/685129" target="_blank">📅 23:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685128">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
ترامپ درِ بازگشت به توافق اسلام آباد را بست‌/ حالا چه می شود؟
👇
khabarfoori.com/fa/tiny/news-3240972
🔹
پزشکیان برای نرخ سوم بنزین، سقف تعیین کرد
👇
khabarfoori.com/fa/tiny/news-3241156
🔹
علی کریمی؛ از لگد به ساک پزشکی تا دعوا با دایی و رضا پهلوی/ تاریخچه قهرهای تمام‌نشدنی جادوگر همیشه عصبانی
👇
khabarfoori.com/fa/tiny/news-3241154
🔹
هنگامه قاضیانی به ایران بازگشت
👇
khabarfoori.com/fa/tiny/news-3241083
🔹
قدردانی مادر زهرا متقی از پلیس و مردم پس از پیدا شدن دختر ۱۱ ساله‌اش
👇
khabarfoori.com/fa/tiny/news-3241033
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/685128" target="_blank">📅 23:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685127">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72f71a5bc.mp4?token=ZV-7Rt7wV-DSDI6i0vTk_hp24C5V1ggNbeZYoiwbgO8590bKKXwXAp7ZlsPLUv6Dna_6Dp45X_8Bw3U27lpz-7ly5V52UJ7c8laKfqm-HafcG5AdeyQmUlk9AUOvVSxJOGwob4c2rtKFpJNB3Wqz5j1nBxKwmn0em-o4Juj6jwOmWuC8PGzldO5CztMx-pKbLjxYxwDPJvjjYmL5_ZQJ_CcMjkIblI63nucEi8yZTsfXwcPnu9SUeLqrQi0d6Cz2j-c6mudbWhBqHDDuEOhi1LAcheIllYOvQbBsykAqCn_NgxTb4RDg7p0Vz_2qz3KzTlqveX9vSemuS7rj2gCRjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72f71a5bc.mp4?token=ZV-7Rt7wV-DSDI6i0vTk_hp24C5V1ggNbeZYoiwbgO8590bKKXwXAp7ZlsPLUv6Dna_6Dp45X_8Bw3U27lpz-7ly5V52UJ7c8laKfqm-HafcG5AdeyQmUlk9AUOvVSxJOGwob4c2rtKFpJNB3Wqz5j1nBxKwmn0em-o4Juj6jwOmWuC8PGzldO5CztMx-pKbLjxYxwDPJvjjYmL5_ZQJ_CcMjkIblI63nucEi8yZTsfXwcPnu9SUeLqrQi0d6Cz2j-c6mudbWhBqHDDuEOhi1LAcheIllYOvQbBsykAqCn_NgxTb4RDg7p0Vz_2qz3KzTlqveX9vSemuS7rj2gCRjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: افرادی که دستی بر آتش ندارند، تحلیل‌هایشان در جیبشان بگذارند
🔹
طرح نمی‌خواهم؛ اگر کسی می‌تواند مشکلات را با شرایط موجود حل کند، به او اختیار می‌دهم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/685127" target="_blank">📅 23:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685126">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
رئیس‌جمهور: نزدیک ۹۰ میلیون بشکه نفت در زمان اجرای تفاهم‌نامه فروختیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/685126" target="_blank">📅 23:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJuqod4Ic3bamXBtnIADJ1RppTNHjocnrVpdfbRnxpcHhPfoBf-cmMTH9fv4lH6-2Nd33tAWicblZJ8EzSUe7lheQCoDEaInNyLPbX96KDwSybo_e68fozm5qUPxZfFhfFYiIK0uFP7xY31fKnPuUQs2vE2i6a2vYf6yQcGjVpNDWaDVX5hbi8rZDiP3q10VMc9EiOhG6AAyl9XPR2JkCifcKrzdmpZDXWBnqYs6n2HaN8mcglLPMG2FmenEgqMroJ06l3omnuviBzo2zLKcdTO2WQ1Y_N9RerdGCB-w-zEY2ZreIz-tcClI6r7Ac7aVicWCK4GZH8sNIlfFcIC3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای بازگشت غیرمنتظره محسن نامجو؛ «عادی‌سازی» یا غم غربت؟ |‌ معین، عطاالله مهاجرانی و سروش؛ چه کسانی در صف بازگشتند؟
🔹
انتشار خبر بازگشت محسن نامجو، خواننده و آهنگساز ساختارشکن و نام‌آشنای موسیقی تلفیقی به تهران، شوک بزرگی به فضای رسانه‌ای، شبکه‌های اجتماعی و محافل فرهنگی وارد کرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3241125</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/685125" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685124">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c70ff699e0.mp4?token=RCow7DnVmdr_ivs3YDIm0YtB_G_R0M5JP06vbD5KMLbnnPdcjgdVQ9snd0OimtMXnJbKrYIroZmjm7yuY48uA_eS2CcrKwwZdSfFZFZTEN8FBqNQHSwMqhfb4QdZ63tEfeH1HrIM4ysKfqx-X0BVvoImaGsOfjs2aVV1YravdRy29TMfHLpP1rWgrJhWndgAgWpQtv9xzpoHdQVkhbYFsbl3IqCGPcaLatDXcDxSV6i3ImpontsPCjLANSHQYbFYAcLpdb9JbDzhbrc2FcTPB_0Z7wB7XtTMxQuqsX7sc4Ii7Hjoz1m0_hdNRVXxjcL_IS_gwzDhn5oRQQVdMLiqVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c70ff699e0.mp4?token=RCow7DnVmdr_ivs3YDIm0YtB_G_R0M5JP06vbD5KMLbnnPdcjgdVQ9snd0OimtMXnJbKrYIroZmjm7yuY48uA_eS2CcrKwwZdSfFZFZTEN8FBqNQHSwMqhfb4QdZ63tEfeH1HrIM4ysKfqx-X0BVvoImaGsOfjs2aVV1YravdRy29TMfHLpP1rWgrJhWndgAgWpQtv9xzpoHdQVkhbYFsbl3IqCGPcaLatDXcDxSV6i3ImpontsPCjLANSHQYbFYAcLpdb9JbDzhbrc2FcTPB_0Z7wB7XtTMxQuqsX7sc4Ii7Hjoz1m0_hdNRVXxjcL_IS_gwzDhn5oRQQVdMLiqVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: نباید نگاه صفر و صدی به مذاکرات داشته باشیم؛ اگر به تعهدات عمل نکنند، ما هم عمل نمی‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/685124" target="_blank">📅 23:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685123">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ccb595ab.mp4?token=M7tvtUoVKvFj3ba6aqNZPlxaLD-d6glq7RwBViiCKBdqd7rQyJIcK1IcXPiTUutqDesfOvZPs2d8RUwC1c--hv_iC0h7qsM_zSnn5H8iZle_WNSHeQyAwTbH_-9ah-3Jflv7ZRLty_j4BT3gFfqZIMn8zMxfZiCoOb7qBy36ax5TJkjMgahVLIfjQv_67z2oNZ7Nw83R-xyL74R5ixm7zfcq2y29YR9rkiWCVYFpK8xE23ZgHDfhlMyaTibK3BAIvomWGHdvE4q38wzQ1Y33Pxro2fKS8QDnS1qvjam7DmDc1TbmzEyLoc8l1H1uwvxHNoib3-cFdiDvcGquqRvefIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ccb595ab.mp4?token=M7tvtUoVKvFj3ba6aqNZPlxaLD-d6glq7RwBViiCKBdqd7rQyJIcK1IcXPiTUutqDesfOvZPs2d8RUwC1c--hv_iC0h7qsM_zSnn5H8iZle_WNSHeQyAwTbH_-9ah-3Jflv7ZRLty_j4BT3gFfqZIMn8zMxfZiCoOb7qBy36ax5TJkjMgahVLIfjQv_67z2oNZ7Nw83R-xyL74R5ixm7zfcq2y29YR9rkiWCVYFpK8xE23ZgHDfhlMyaTibK3BAIvomWGHdvE4q38wzQ1Y33Pxro2fKS8QDnS1qvjam7DmDc1TbmzEyLoc8l1H1uwvxHNoib3-cFdiDvcGquqRvefIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت رفاه پاشنه آشیل دولت خواهد شد/ مدیرکل دفتر وزیر رفاه تاثیر و مداخله‌اش در اداره وزارتخانه بیشتر است
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
صندوق‌های بازنشستگی ما از یکی از مسائلی که رنج می‌برد تعدد قوانین استخدامی و بازنشستگی است.
🔹
چندین صندوق داریم حتی یک شرکت دولتی به اسم شرکت هواپیمایی جمهوری اسلامی برای خودش صندوق دارد و درحال حاضر با نزدیک به ۱۰۰ هزار بازنشسته ورشکسته هستند.
🔹
وزیر رفاه توانایی لازم برای اداره موسسات اقتصادی خود را ندارد و در تراز وزارت باید یک جانبه جایی صورت بگیرد.
🔹
گزارش اخیر دیوان محاسبات اعلام می‌کند که که بخش عمده ای از اعضای هیئت مدیرانی که در شرکت‌های مختلف منصوب شده‌اند، تشریفات اداری را طی نکرده‌اند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/685123" target="_blank">📅 23:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685122">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998f235100.mp4?token=Yb9RiNPA7lGMEeZoD7F_guQz7DmTwg28j7R35U3YF9o2v_KcQu-_FaFnwyAghTpyLM7qA4BrRe22xAYW_TT4RRanFQbCBbo5azYEbB2JbpBPjYmltmyWJ-2bZRYWgRUgH6Cf7Ek8Gc_d8zfrPt6TuyOlM4nqJEBZWPCd8Ac02R1veoXJ9_Sxf77zG9oA57JN8KAXPukg6svik6W8JzQpg36KGEobTxRdBEUA5sg46XsnQvTdfQa40E3cBKgR2bZq1u81dp1a_fWeCVF3hOXqHdykLzY5He9F74AAawwCMGXTE4YGJVieDhx-inBwDOf24ZPhEDmsifU2-2EVq1PeOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998f235100.mp4?token=Yb9RiNPA7lGMEeZoD7F_guQz7DmTwg28j7R35U3YF9o2v_KcQu-_FaFnwyAghTpyLM7qA4BrRe22xAYW_TT4RRanFQbCBbo5azYEbB2JbpBPjYmltmyWJ-2bZRYWgRUgH6Cf7Ek8Gc_d8zfrPt6TuyOlM4nqJEBZWPCd8Ac02R1veoXJ9_Sxf77zG9oA57JN8KAXPukg6svik6W8JzQpg36KGEobTxRdBEUA5sg46XsnQvTdfQa40E3cBKgR2bZq1u81dp1a_fWeCVF3hOXqHdykLzY5He9F74AAawwCMGXTE4YGJVieDhx-inBwDOf24ZPhEDmsifU2-2EVq1PeOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: کاهش مصرف از راهکارهای اصلی مدیریت مساله بنزین است
🔹
روزانه ‌۲ میلیون ماشین وارد تهران می‌شود و برمی‌گردد؛ اگر کارمندان ما در اداره مربوطه در شهر خود بمانند، کسری بنزین جبران می‌شود.
🔹
طرحی داریم که با کمک شهری کارمندان هفته‌ای یک روز با حمل‌ونقل…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/685122" target="_blank">📅 22:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685121">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTechnolife.com | تکنولایف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APFrftlNx3lOc1gPJYxXe2GiinWuZxgJ2-AzxXtzLQaDnV55a0QudEkxSzOmUunU76qUSEjZ2dkztNtOqDyFFyB8e6UT8-igrzj37oK8bDqnXGSvxla3yENgtxmd4KRB6USynSULmNELlGKAFN39q60v09xLdh0A3rpjrGd6kvwVsYAgKcqwPLf_oAOaobZUmejd1d-o5w0m8JdzMoleNdV8gtK1AMV5N2izhZfHUQYoMcgfFEPtpOoOH-qIut3WkXHG8HKUtlZBX8NTqGwIGPAUWqF4E9NCRhdrkbZItV59qrPSBBAaRpwKDtv-q_CB4z2QQnAi4lflZzmkso2-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
یک خرید؛ شانس بردن آیفون و BMW!
✅
تا
۱۰ شهریور
، از تکنولایف با تخفیف‌های ویژه و قیمت‌های کف بازار خرید کنید و شانس بردن
آیفون ۱۷ پرومکس
رو از دست ندید.
✅
اگر پرداختتون رو از درگاه اسنپ‌پی انجام بدید، علاوه‌بر قرعه‌کشی آیفون، در قرعه‌کشی
یک دستگاه BMW
هم حضور خواهید داشت.
🚘
http://tchl.ir/HNgrp7
http://tchl.ir/HNgrp7
http://tchl.ir/HNgrp7</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/685121" target="_blank">📅 22:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685120">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f393c4474.mp4?token=k1ahRljjVGMWLWqRGmscrlUw_d97V7y_LCQ8fjmcwAl8VUjG_ydUtsc_q0zhMEuiKyKfpIhOMvutNN_Bzp-pJpNOP_K0VyXXQhQeOYDkMACvH0JJB5DH23P85n_P8fkp-_cKqkYlLgl56R9MXpB2xJcv0DljgFfYTHE2RceDjAmYq_PX-xV16dQoWlLXPFDAeHnhbk5oyXPkgbUY9ClOI8QhFH-W0k8AWQqrdCLwt-corwHBqi6hRDUyIEtB55TAxRR40SyF5cHoA8sCtYJNlLbQOqp_MY6vhR8n1WP9C7DfqHzSthdoEsNBk2JS1wr91SQX3omXHtRwr6B_6uK9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f393c4474.mp4?token=k1ahRljjVGMWLWqRGmscrlUw_d97V7y_LCQ8fjmcwAl8VUjG_ydUtsc_q0zhMEuiKyKfpIhOMvutNN_Bzp-pJpNOP_K0VyXXQhQeOYDkMACvH0JJB5DH23P85n_P8fkp-_cKqkYlLgl56R9MXpB2xJcv0DljgFfYTHE2RceDjAmYq_PX-xV16dQoWlLXPFDAeHnhbk5oyXPkgbUY9ClOI8QhFH-W0k8AWQqrdCLwt-corwHBqi6hRDUyIEtB55TAxRR40SyF5cHoA8sCtYJNlLbQOqp_MY6vhR8n1WP9C7DfqHzSthdoEsNBk2JS1wr91SQX3omXHtRwr6B_6uK9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛑
واکنش تند حسین شمقدری مستند ساز به جنجال اخیر علی کریمی و رضا پهلوی :
علی کریمی میگه  « من مثل کشته‌شده‌های ۱۸ـ۱۹ دی نیستم؛ که هرکاری خواستید بکنم ! »
همین؟ اینهمه جوون کشته شد ...
💔
بازم از پهلوی و علی کریمی باید خط بگیریم؟
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/685120" target="_blank">📅 22:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685118">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb39bc1a2a.mp4?token=nXZgAHjDYzGo_gWuDSxVaZVJbBVddAJpMQ7LdJgX4Q-8EQKEz4K6mQg-kO05UeXOO5r8VJ2PfS7gziQReuchqt2ub29aBdr1keLB4tSjcxhCera_cYwgtazhD_-JmxDyYyV_K_lpqG3T_KC3E0HnbF4noPAU5VAPWkGzNvKhVMlId29CxPNf_M7iJc0Bmi4N9zBYrL79imZkslJ8rHD5vO6GAR65o5Gu2hg1WmQjXuqe3EDXrpPR_64zaEDpNcB1GRXxQmD6nOS8yyqHB0Eh-uBfTV8kFRoIsasNsojdijkEo3QE-RvV4NLi-qxhIyeLUt5lAnGgGJLtO55Ai5E6uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb39bc1a2a.mp4?token=nXZgAHjDYzGo_gWuDSxVaZVJbBVddAJpMQ7LdJgX4Q-8EQKEz4K6mQg-kO05UeXOO5r8VJ2PfS7gziQReuchqt2ub29aBdr1keLB4tSjcxhCera_cYwgtazhD_-JmxDyYyV_K_lpqG3T_KC3E0HnbF4noPAU5VAPWkGzNvKhVMlId29CxPNf_M7iJc0Bmi4N9zBYrL79imZkslJ8rHD5vO6GAR65o5Gu2hg1WmQjXuqe3EDXrpPR_64zaEDpNcB1GRXxQmD6nOS8yyqHB0Eh-uBfTV8kFRoIsasNsojdijkEo3QE-RvV4NLi-qxhIyeLUt5lAnGgGJLtO55Ai5E6uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: کاهش مصرف از راهکارهای اصلی مدیریت مساله بنزین است
🔹
روزانه ‌۲ میلیون ماشین وارد تهران می‌شود و برمی‌گردد؛ اگر کارمندان ما در اداره مربوطه در شهر خود بمانند، کسری بنزین جبران می‌شود.
🔹
طرحی داریم که با کمک شهری کارمندان هفته‌ای یک روز با حمل‌ونقل عمومی در محل کار حاضر شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/685118" target="_blank">📅 22:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74cb9cace8.mp4?token=voFHsrHCm5r-52UBvFKIepjVPbhsL5n0ZEdR4C8_qlYAMKN4OYesUPwrUypYg12SGDESfN2fCI-dGwgET-WJsxqUKLHGOggZapd7b_C6UYu9r5oPwz3lGYbbewQizXLSrHj0eZwVzVCWNYvAZWUpqmLuiO1kfnBDfnfmAVtC1A-vc5vVof8Jp0tVArWkzPPI1rFZCd57U5rOnJMJ2I2ESN4bu-qacEx5lVxQbu7MT4RLajwmz4u0ybORH2gS2jeFyQdYetHikt3SnGSvNFJm38psmqcNJQjpV52Z9wznLsTCU6r_NeTYRlo8sWlkxN4GAETvvCwLtFmK3_Jv3M6dIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74cb9cace8.mp4?token=voFHsrHCm5r-52UBvFKIepjVPbhsL5n0ZEdR4C8_qlYAMKN4OYesUPwrUypYg12SGDESfN2fCI-dGwgET-WJsxqUKLHGOggZapd7b_C6UYu9r5oPwz3lGYbbewQizXLSrHj0eZwVzVCWNYvAZWUpqmLuiO1kfnBDfnfmAVtC1A-vc5vVof8Jp0tVArWkzPPI1rFZCd57U5rOnJMJ2I2ESN4bu-qacEx5lVxQbu7MT4RLajwmz4u0ybORH2gS2jeFyQdYetHikt3SnGSvNFJm38psmqcNJQjpV52Z9wznLsTCU6r_NeTYRlo8sWlkxN4GAETvvCwLtFmK3_Jv3M6dIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: نرخ سوم بنزین بیش از ۱۰ هزار تومان نخواهد بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/685116" target="_blank">📅 22:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685113">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14050606پیام_رهبر_معظم_انقلاب_به‌مناسبت_هفته_دولت.pdf</div>
  <div class="tg-doc-extra">169.2 KB</div>
</div>
<a href="https://t.me/akhbarefori/685113" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام رهبر معظّم انقلاب به‌مناسبت هفته دولت
🔗
https://rahbar.ir/s/1849
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/685113" target="_blank">📅 22:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685112">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e065d304.mp4?token=Z5tRAlkJYodo2Motx-lrehUpEML1e8tsmEEqSu3Isz45PRQVUuFVLYyN-uJ7fhbMDLE_xOe3cts9pvmz49BjTouLN3KzyzN4euKpEYccj7ZI-mQC8fwKB55ZHEcd4GVieVvp5wJXo7WzlL9D4T53VMarYcxsu8tRFa-gK7pUBtxWyAKdO2V9ebsOBiHy-XYXqb1EqwUOdg5hEQ8hB4qSm9Qap-KGqE9XBCzVQR62TH5SboYgzkwUTTHSIDhAEXoEpTUE6ESxLJScU3yLyl_gKjF9vzC78odnY8RTdX1qs4FsRrLsusbvUu_QzPZnwkY6cvpQ-90WCn5fyGftoC2CIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e065d304.mp4?token=Z5tRAlkJYodo2Motx-lrehUpEML1e8tsmEEqSu3Isz45PRQVUuFVLYyN-uJ7fhbMDLE_xOe3cts9pvmz49BjTouLN3KzyzN4euKpEYccj7ZI-mQC8fwKB55ZHEcd4GVieVvp5wJXo7WzlL9D4T53VMarYcxsu8tRFa-gK7pUBtxWyAKdO2V9ebsOBiHy-XYXqb1EqwUOdg5hEQ8hB4qSm9Qap-KGqE9XBCzVQR62TH5SboYgzkwUTTHSIDhAEXoEpTUE6ESxLJScU3yLyl_gKjF9vzC78odnY8RTdX1qs4FsRrLsusbvUu_QzPZnwkY6cvpQ-90WCn5fyGftoC2CIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور در گفت‌وگو با مردم: با آمدن آقای محسن رضایی نگاه‌ها در حوزه دیپلماسی به هم نزدیک می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/685112" target="_blank">📅 22:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685111">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ویدویی جالب و عجیب از تمرینات تکاوری یک گروه در جنگل‌های هیرکانی شمال کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/685111" target="_blank">📅 22:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685109">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba21c05183.mp4?token=GNz8HY-a0JuV1YtFnKJu9ThIOrG5FoSPH0i6mVozkhRjT6Qs3rUVqeRq7FF5Di6dI8N6lKooLGooONkegFQvVZueROWwsUHkbjz0Z7I4lUY4WwWgebybco-A41029jfBCQ7xGgI1QcbLxUfbqtb8Mpz3El3WrnUAz7DG5qUCbJurrMqGIZJTnuTVgjtOssIYQLn4tKJWDLgOJgWp0d_abJlQ3wvVbmNdLG6Ea3yP4YsFsf9m61CbDd0EBAQj18ZYrxPWeoM1F-zXugMdJVpISLZPJTexRuTDv8ODCxZB_BVBv3s0caygAegW9-WRYqqnRK8iVe7aK8530s7vWSXD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba21c05183.mp4?token=GNz8HY-a0JuV1YtFnKJu9ThIOrG5FoSPH0i6mVozkhRjT6Qs3rUVqeRq7FF5Di6dI8N6lKooLGooONkegFQvVZueROWwsUHkbjz0Z7I4lUY4WwWgebybco-A41029jfBCQ7xGgI1QcbLxUfbqtb8Mpz3El3WrnUAz7DG5qUCbJurrMqGIZJTnuTVgjtOssIYQLn4tKJWDLgOJgWp0d_abJlQ3wvVbmNdLG6Ea3yP4YsFsf9m61CbDd0EBAQj18ZYrxPWeoM1F-zXugMdJVpISLZPJTexRuTDv8ODCxZB_BVBv3s0caygAegW9-WRYqqnRK8iVe7aK8530s7vWSXD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرف عمانی قبول دارد که باید تنگه هرمز بر اساس تفاهم‌نامه اسلام‌آباد اداره شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/685109" target="_blank">📅 22:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685108">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be1c613eb.mp4?token=tV6mRj53lqLeypJmU4yarbjo2Wk41JKcgJkE8ocP6AqtdM_1dUZeMY8UxuN0e5biOz7mTtqBNwvkBL_KT5ZOprMdVFCjpR4eHstakN7kzSXJnHKxaEdbCcQZ0qToMPIXEUeec-NYxwuWqP6u_iOdePUXuVJm6_oD_nymDXBv0ElI5KeNZ6GCoqxVdvoRtDlJeEh3mMyyEiVmbfu13JCOTIGl2JTwKZdZC1ny1ECqa5fHyq3hnfjzmXahRoJurHENBW96_bQWL8jm6H7esroMT6afTb5WY-9e1h_Q325DZtFyewqByda9wAmmHfQkY6YIr1E70EarcYg9qs9YONpzVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be1c613eb.mp4?token=tV6mRj53lqLeypJmU4yarbjo2Wk41JKcgJkE8ocP6AqtdM_1dUZeMY8UxuN0e5biOz7mTtqBNwvkBL_KT5ZOprMdVFCjpR4eHstakN7kzSXJnHKxaEdbCcQZ0qToMPIXEUeec-NYxwuWqP6u_iOdePUXuVJm6_oD_nymDXBv0ElI5KeNZ6GCoqxVdvoRtDlJeEh3mMyyEiVmbfu13JCOTIGl2JTwKZdZC1ny1ECqa5fHyq3hnfjzmXahRoJurHENBW96_bQWL8jm6H7esroMT6afTb5WY-9e1h_Q325DZtFyewqByda9wAmmHfQkY6YIr1E70EarcYg9qs9YONpzVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رئیس‌جمهور از شکل‌گیری تفاهم‌نامه اسلام‌آباد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/685108" target="_blank">📅 22:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685107">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
روایت رئیس‌جمهور از شکل‌گیری تفاهم‌نامه اسلام‌آباد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/685107" target="_blank">📅 22:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685106">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7a4d0973.mp4?token=tZTAw0qCLf5kfz2TJIe9qKIxDwxyy8ZNkxVkRb0nEAieDJZoZbkvlW-uBT4zPvSe16Ri32ItL_2wmYx_I6B_5sxLyXcaT6MyqMcDQvI57_hK8ipmcKFpw3b1Vw-A0vn-qzbmpZV8WZcbQ7cbeZD4cAqbOSqewY4riKRb_S33DFaHuIJKlezuBSRyZNU0yjCrBfqVb8DSgzpUWwzLFVVm-aE85_5Z-FId6mE8VtwnWBjpHlwWsZ-_j1kMkVxOEv7qNz2K6EHr6zjW9W5Vo73u8BERGVZY48e8u6CmUMYnH3Lc-N7WnmVxI1usUzH0SEqN1IY-wR0mFm0bdinHxOiPwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7a4d0973.mp4?token=tZTAw0qCLf5kfz2TJIe9qKIxDwxyy8ZNkxVkRb0nEAieDJZoZbkvlW-uBT4zPvSe16Ri32ItL_2wmYx_I6B_5sxLyXcaT6MyqMcDQvI57_hK8ipmcKFpw3b1Vw-A0vn-qzbmpZV8WZcbQ7cbeZD4cAqbOSqewY4riKRb_S33DFaHuIJKlezuBSRyZNU0yjCrBfqVb8DSgzpUWwzLFVVm-aE85_5Z-FId6mE8VtwnWBjpHlwWsZ-_j1kMkVxOEv7qNz2K6EHr6zjW9W5Vo73u8BERGVZY48e8u6CmUMYnH3Lc-N7WnmVxI1usUzH0SEqN1IY-wR0mFm0bdinHxOiPwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک پهپاد و پایان وحشتناک یک سخنرانی!
🔹
همه‌چیز از یک پهپاد بازی شروع شد؛ اما چند ثانیه بعد، انفجاری مهیب، سخنرانی را به کابوسی غیرمنتظره تبدیل کرد #کابوس_ترامپ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/685106" target="_blank">📅 22:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685103">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای وزارت خارجه آمریکا: افراد و نهادهایی را که از طرف ایران به فعالیت‌های مالی غیرقانونی مبادرت می‌کنند، هدف قرار خواهیم داد/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/685103" target="_blank">📅 21:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685102">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
کالابرگ مردادماه افرادی که احراز سکونت خود را تا ۳ شهریور ثبت کرده‌اند واریز شد
🔹
کسانی‌که در ‌۳ و ۴  شهریور اقدام به ثبت محل سکونت خود کرده‌اند نیز در هفتۀ آینده کالابرگ خود را دریافت خواهد کرد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/685102" target="_blank">📅 21:40 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
