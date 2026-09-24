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
<img src="https://cdn4.telesco.pe/file/V06Vx_Ph5BJQfpTsFpQ0v7ibQsHa9vyUH3fIz-peco3MCJtmg48yka9YWNBke_-xPIK520J9ni9vJr_Fn2TCPS-udygPuRmnYg0s3RhI3WH8SWny_FXHWfXbX3dHugoutq4rIPR5OsvnU-xg9YgZFFGtu2wTZ6oFDM3Yk95Ip7MWRoATknTysgzzQKPq67NVpdyIrxlsF9_yN7bZ04etDVjTucwjzaPgDY9gk9i-772r-9j1nsLYsjxgpEQDYPiuz_YccWpXIerayTMXUAqpayIFAG3pwMdn0UBSCbfmsQ04MbhxWCh6ycomDaBdYRHg7kTC19vzuGye5fCbPzMsJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 04:08:43</div>
<hr>

<div class="tg-post" id="msg-149063">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=Mn7sWAb_KQwNB0aXjucDWAfT4m3FZAenGPxm6wDHRar1SQSZMw3P8l0jx8zRMGEF-T5Chv9lnoikxEGMJyyxYkdpoS9SD0ZfJFd1Q68XcbgQBLWUJ8GSX7Q682XfjWUyJ1qZjLjrGQ9wxsFEJYTYYqO-2A6AkCwqinZ_XGVhdrh01D3o2WMPD8x-wMuOPDjqwHbNWKAL91yTgbnSgkCacQwdjGiimNUwdaEkcE-QB6IzGKKDlRRyBNoVsiDkx5-n35_Rmu3fqvQBV9HYDETh9WVu0Ov7L2dIFxRConq9jjf03p0xqmW5NKTvvGqAL4yuZmAgpi4Y0hyRBlMtGgLZAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=Mn7sWAb_KQwNB0aXjucDWAfT4m3FZAenGPxm6wDHRar1SQSZMw3P8l0jx8zRMGEF-T5Chv9lnoikxEGMJyyxYkdpoS9SD0ZfJFd1Q68XcbgQBLWUJ8GSX7Q682XfjWUyJ1qZjLjrGQ9wxsFEJYTYYqO-2A6AkCwqinZ_XGVhdrh01D3o2WMPD8x-wMuOPDjqwHbNWKAL91yTgbnSgkCacQwdjGiimNUwdaEkcE-QB6IzGKKDlRRyBNoVsiDkx5-n35_Rmu3fqvQBV9HYDETh9WVu0Ov7L2dIFxRConq9jjf03p0xqmW5NKTvvGqAL4yuZmAgpi4Y0hyRBlMtGgLZAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز یه بمب افکن b1 هنگام استقبال از شی
✅
@AloNews</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/149063" target="_blank">📅 01:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149062">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099168c283.mp4?token=myaZAyYdnvnyGEmXgwXClHQn3elh0_iOQyzIPGGQm1gGF4ZH-zPHU5PCalgEVrDQiRYE7Z5EwD2IvC5VvCd0xfDs8_YOH544cHcFToTlC7dMTygAm2eh7LtiMMUtjEhMjDzdoMIaQs25Vwlvpaisrairu7SKnNpY5bNFrmMZ1bVirFFA3-Y_IgMShGmqMlhwRm_leBlVANBsKcSTLi8KxAOsy2is1Y8l9nEFlWiG8DNr8R_1ZiWY9pnRTlZz5eddb-cx5MS63PjWDbnjLBp5lLorpM22kxlqc4NL1GygPm0DxFHL0796IlNBzHNKJW7tDGIhDUaNNk58aB8fJ115Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099168c283.mp4?token=myaZAyYdnvnyGEmXgwXClHQn3elh0_iOQyzIPGGQm1gGF4ZH-zPHU5PCalgEVrDQiRYE7Z5EwD2IvC5VvCd0xfDs8_YOH544cHcFToTlC7dMTygAm2eh7LtiMMUtjEhMjDzdoMIaQs25Vwlvpaisrairu7SKnNpY5bNFrmMZ1bVirFFA3-Y_IgMShGmqMlhwRm_leBlVANBsKcSTLi8KxAOsy2is1Y8l9nEFlWiG8DNr8R_1ZiWY9pnRTlZz5eddb-cx5MS63PjWDbnjLBp5lLorpM22kxlqc4NL1GygPm0DxFHL0796IlNBzHNKJW7tDGIhDUaNNk58aB8fJ115Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال ترامپ از شی
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/149062" target="_blank">📅 01:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149061">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
تانکرترکرز گزارش می‌دهد که نزدیک به ۶ میلیون بشکه نفت خام توقیف‌شده جمهوری اسلامی ایران، به‌صورت مخفیانه در حال انتقال به ایالات متحده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/149061" target="_blank">📅 01:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149059">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijbXyOfNnLx2Iel1BwoT6OuFcES83JOQHZFF_ItYnaFvWTx7oDN9jsx18pcFZVk9Z9RCj1ZwMkV_bpywZFHxpAnDs4z1inh5tcBZASgSpQS3rnbz1l9Hkh-zI3VsZrdtpG-kkGRJyGP7SBvxP88HzDpUjxGtxyQ3bwnZJFIRzr1SYiAHf4N4SO1HRLjQMi91NJdPh3HnjyOUAZFeUg2btgGv2PmoUqQzHpeXOM80BHLJTVtOuLer1s5cPRJXGdzZeRQD-Lt_CuB-PZMOkt6tKNfb1UB8CPOKR5MXdQN0cqPXuj3uTFhuUe7Lp_RffMSwiFRPNqlgH7u0xg-dp7fD0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tz4n6t02c4hdVY2_U3bVSRmvrQsCIZ16EZAoTosfIxsGDMypzx7wwJ3ci4pXGJNe-1v8AZZFWrrad1o0YwyjTMSjuaRZylcHF4X9TmILiVqM-PH6jfegjHgL_Y0JwJT73QzDjnTSjVuiC1XUI4iR_y9wEiapLZ4K6iAFuG0t9VKGLwH-4osCAd5ujure0xbgfk3swatc9j8XwPs3Kx0nlz4SNDp6BnOh1KvWrXUhagpJKDksi6cF4r_2VeBJXdwoTTKDrVYGmm0U4fqY78osNRSh8zmS35cwFKrOQlLdpD0CeWY_dWi1XPbilVAVABRhu_-Sijqck6hkmXsjZ8w0TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فیلد مارشال: زیر دریایی آمریکا رو مهندسی معکوس کردیم و تا ۶۰۰۰متر میتونه زیر آب بره
🔴
پ.ن: میانگین آب اقیانوس‌ها ۳۷۰۰متر هست و تنها گودال ماریانا و جاوه بالای ۶۰۰۰متره که اونم خیلی از ایران دوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/149059" target="_blank">📅 01:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149058">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWkribTJ4zYgQdf2jF11hlOR1wNSdtDguKz_4dl5Vg9LvZrxXnH6QyHGsrd0Y-n39nbFbu-62bGHK0dlVaOfD_BD78LMtF3fepmHf09vrBoR4BfNGwuofPn6CwgnZ4Cj4FHu7Mvv8fbbe7Ps0Gl9q5ZIRdTxbdwN5Qa9Q_Wd0KB_q54Ax8Io-Jo90rLIaW2rQdV2kUeoUTm3GmAvxufM2P9u1dCo_7RalVg-vVUTZNLofMTQxEFhNuWkG1gQoMHsPfUlBo74Uyw-3pNN9ihA28uCGrxzg9VjvGp2DgfmaBEwzs_J4PTBQ5tfQY15C4JB6YBMBZc-SZ-jDkMaWTDFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: جنگ‌های آتی ما و آمریکا تو فضا انجام میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/149058" target="_blank">📅 01:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149057">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sKEVHdOssvGXsJeJhWJ63e1DY9OzvMaUVcLMHGTPLoxQFiDEyokc6N47B7cpAvYDsqF7wJEDFC_NHVjio1n8KcthyXIWtMY66i0mNOmuyk1sJmbu8kLAOs8mUc_fdi1YkJmE-s6P5dAezDVJUnLnYAaU0dpYJMRcSXzxS9Bwrhs-mYLAT6nX6kgazJ-PmjaDtBtU7WPnIzVXJeTRxp_HuzSSV4OSs0ldvXAqssPNWjDGvNUAfAGvuY6uqTSC_tqUHWwAToQ2k6l60FwMxrR14UyQKCRmAsDOZS7SUL2pSRM0UtomHFjTDBeR41limKMXUAe0FgiPJpScy3oIaElw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: اگر کشورهای خلیج فارس جلوی پروازهای ایران رو بگیرن، ایران فرودگاه‌هاشون رو با موشک باران تعطیل می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/149057" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149056">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گزارش‌ها از شلیک موشک کروز به سوی تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/149056" target="_blank">📅 00:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149055">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
صدای انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/149055" target="_blank">📅 00:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149054">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99cb34213.mp4?token=PlOQetzB2cW8QaJYinixIE2bIIsijpdcpDzUirhkQ-3QcLEybqw3RewEzwCVR169X0l704D81EZsnf_FWLQyg-p3TrMpyodq3aOWTeCpjkRjgfEHf7aWqJkpoEOtQrmb69ovnoUHfX_a_Ksd8-t2fwwrxQFg_eEx8BgsJ2jQqpK6c6yFiHJXnwkspVrEBYxMO5foli3ZnK7OQmN7tJYpOZRicJZxrOZptJjoQNuwdr0RGgJTaVsF_oA3xZuWGTyLO1QS5f4pZpcJ0D8Jy-SmP_RiZINmlbxPYYno3kdZkHlWDETKQOPVpRsK-_GdePMppG07cgKnYTY4AA7ftuW56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99cb34213.mp4?token=PlOQetzB2cW8QaJYinixIE2bIIsijpdcpDzUirhkQ-3QcLEybqw3RewEzwCVR169X0l704D81EZsnf_FWLQyg-p3TrMpyodq3aOWTeCpjkRjgfEHf7aWqJkpoEOtQrmb69ovnoUHfX_a_Ksd8-t2fwwrxQFg_eEx8BgsJ2jQqpK6c6yFiHJXnwkspVrEBYxMO5foli3ZnK7OQmN7tJYpOZRicJZxrOZptJjoQNuwdr0RGgJTaVsF_oA3xZuWGTyLO1QS5f4pZpcJ0D8Jy-SmP_RiZINmlbxPYYno3kdZkHlWDETKQOPVpRsK-_GdePMppG07cgKnYTY4AA7ftuW56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله به نسیم شهر تهران در جنگ ۴۰روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/149054" target="_blank">📅 00:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149053">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
صدای انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/149053" target="_blank">📅 00:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149052">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سم آلتمن مدیرعامل شرکت OpenAI در نشست سازمان ملل گفت: هوش مصنوعی می‌تواند تصمیماتی بگیرد که انسان‌ها دیگر قادر به درک یا کنترل آنها نیستند. در این شرایط لازم است که به شدت مراقب باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/149052" target="_blank">📅 00:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149051">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پزشکیان از نیویورک خطاب به مردم: دعا کنید ناامیدتان نکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/149051" target="_blank">📅 23:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149050">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سی‌ان‌ان: پسر سفیر اسرائیل در ایالات متحده، در جریان حمله در کرانه باختری، به شدت مجروح شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/149050" target="_blank">📅 23:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149049">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a34e6892.mp4?token=NYg6ExHOQS7UonwmYpDhkAnEWPjYZGEq_xWdF30050PxsJBNDWF9syvQ4YZTeSq9kBOyo_8-IVaV76eShKhAFlq079S4fWqg2oYHly0PhI9k3t2Rrzn3cwC2Cl3qSs0b_qQkvgf8HQrLUa2Yfdd7r23sF2LjygeO88MTFmW4yboXZ_8kxcKVMU-8xGZCTY7CMK0kbptMxlaGEhcjr3GrBrmjxguN-9MW9DfORZbZesrFw-4LQAmNTEQtzYWZBNBwLdOAE8AioUB50aqQs_iv0VLofcIQTRHKi2RUJV3_axrSazbq-7hjKs2a7SDZln9wNL7TXyB7ZhbFK2xDYNFDSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a34e6892.mp4?token=NYg6ExHOQS7UonwmYpDhkAnEWPjYZGEq_xWdF30050PxsJBNDWF9syvQ4YZTeSq9kBOyo_8-IVaV76eShKhAFlq079S4fWqg2oYHly0PhI9k3t2Rrzn3cwC2Cl3qSs0b_qQkvgf8HQrLUa2Yfdd7r23sF2LjygeO88MTFmW4yboXZ_8kxcKVMU-8xGZCTY7CMK0kbptMxlaGEhcjr3GrBrmjxguN-9MW9DfORZbZesrFw-4LQAmNTEQtzYWZBNBwLdOAE8AioUB50aqQs_iv0VLofcIQTRHKi2RUJV3_axrSazbq-7hjKs2a7SDZln9wNL7TXyB7ZhbFK2xDYNFDSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دوسی، خبرنگار فاکس‌نیوز: اولویت اصلی و مطالبه شماره یک رئیس‌جمهور ترامپ این خواهد بود که چینی‌ها ارائه اطلاعات به ایرانی‌ها را متوقف کنند؛ اطلاعاتی که آنها از آن برای هدف قرار دادن منافع آمریکا استفاده می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149049" target="_blank">📅 23:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149048">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a31482c0f.mp4?token=ZFgp_8jdYau_2vEmT_T14PzAIcGnffarwqeZqGyehclVlUBmuwPDihjDF4AcVDVsfr4xEuFzHyXm6O75qEIJ_2rsET4yVKcvA3EjgB_wf5sarjMFwy2h0HHRN-J8zA0P1FOWY2nGKiz0vQZAXXv942NnIVsNv1FIg8j_XtB58a_4DgvNAIF8FuQ991G9FgQ6-EbOcyCZOSrN9UuuIYij3rclJYsKYmu2i0RoKsJvLFZXzQEQjOxhGZcB15HNX7WNZK5JIDR3sAFftwLw4DEp8Tohct8SoSMWg-vUEcTfVLH-Vuxd-92v1iEXxh_jWDerQccCBN7NMANAvHM_dg8Uqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a31482c0f.mp4?token=ZFgp_8jdYau_2vEmT_T14PzAIcGnffarwqeZqGyehclVlUBmuwPDihjDF4AcVDVsfr4xEuFzHyXm6O75qEIJ_2rsET4yVKcvA3EjgB_wf5sarjMFwy2h0HHRN-J8zA0P1FOWY2nGKiz0vQZAXXv942NnIVsNv1FIg8j_XtB58a_4DgvNAIF8FuQ991G9FgQ6-EbOcyCZOSrN9UuuIYij3rclJYsKYmu2i0RoKsJvLFZXzQEQjOxhGZcB15HNX7WNZK5JIDR3sAFftwLw4DEp8Tohct8SoSMWg-vUEcTfVLH-Vuxd-92v1iEXxh_jWDerQccCBN7NMANAvHM_dg8Uqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پتراوس، مدیر سابق سازمان سیا:
مقامات غربی تخمین می‌زنند که روسیه در حال حاضر هر ماه ۶۰۰۰ نیروی انسانی بیشتر را از دست می‌دهد تا اینکه نیرو جذب می‌کند، و این موضوع تا حدودی توضیح‌دهنده گزارش‌هایی است که حاکی از آن است که ژنرال‌های روسی خواستار بسیج بیشتر در چند ماه آینده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/149048" target="_blank">📅 23:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149047">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارش ها وقوع چندین انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/149047" target="_blank">📅 23:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149046">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
به گزارش NBC News، مسائل مرتبط با نظام سلامت در آستانه انتخابات میان‌دوره‌ای ۲۰۲۶ به یکی از چالش‌های سیاسی جمهوری‌خواهان تبدیل شده است.
🔴
دموکرات‌ها امیدوارند با تمرکز بر موضوعاتی مانند هزینه‌های درمان و سیاست‌های بهداشتی، در انتخابات پیش‌رو کنترل مجلس نمایندگان و سنا را به دست آورند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/149046" target="_blank">📅 23:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149045">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
کرملین از دعوت آمریکا از ولادیمیر پوتین برای شرکت در نشست گروه ۲۰ استقبال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/149045" target="_blank">📅 23:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149042">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSjfkdtRbjb2iPKXCWkgHZn9h5hP9znNMh1zqKUylpLHOsERZXpEbRNHD3pvWOyl8xS1eHI85Qmn7bW-y6JVaGHCKrBIVSX_bXGdjlLWvb3SvlWB0cfXAYV8TW-VFxGdheSqy1ZXKuB09oOU4XMecd9I7FdYqZiOq86BFa7CGGMItf3qX1O1NU6Dxvfk6F4yvmMnu4zL1fDW7iEhAL-0qi58DSH-oJy02_Rd7qj49Ewc9p9iXEqwAUQKrVpYid880NdIijHnu3NzN99s-p9sPa7o7rve11BO8PetPkEHqdhRdx_f-_ALyF1cH2rdHGeV5rRSW8LBXWgh68Wv-Nm0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5UHeTkbGNR6N2SqPQ1GmgRZqjZcAG0jYNZhglpDVIwSOGqhWQ79rxkGKKS2imYsuc2LJruqITapDtVpmNaaax_Fc_yny8Bc1lzaSWGAf6Ktp3XJrLnluh63P3jtd0w5GS-FPISmQje4cTsr_6a9ErLf0hdr2mhptvgvWpCiwsuDZkQpWaYgstXihcgk7CXpJUBo0u05kEcvAPpSvTeTl3RKrQAZ1vGEzxSh6rOcXrVMfmTxK-a6bg74EZq6DFCyrWV5H6Il2fJJMQJL8Nf2j_CnoU3LWXQqRqUwhJYbCQSaayvx_N_c6zh5VNW9XbgeVKlPl7xuXR_h45IywoPlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzSO_dEInLh5jMtsaCBFneBiheToMeJESSjVWe-E9ae9LjAWD44JYnb_rNn_XMjL50l5lMhbsPlGlLZygRcczVEVIV7g4fucvKbW6l1EPo6mM1foSJQa2OeYgPob1zLT2wyPwDtbaPIs9FiN6ej3NHUrcxyIJyyrfYN8GZe5ABkm2SLADgq0qGBQEXovZy6ZC36SYE3mt4xZZSyD_uoAguaUvG6E5sTbnZyLaPdrPDfIqspvlJIikfK4CLyMQfiXuTDsauNTKJSAYW8-pKRdC1865g6hVd-bSVGeaZQsjbm-D7F9jQuwrC7D4Y-iNg7TKC9ts1_kVhUyDGXZs7RbUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای ترابری انگلیسی از نوع C-17 حامل تجهیزات نظامی در پایگاه هوایی طائف فرود آمد
🔴
همزمان، هواپیماهای جاسوسی و سوخت‌رسان انگلیسی در قبرس مستقر شدند و ۳ فروند هواپیمای ترابری کویتی نیز از اسلواکی در پایگاه هوایی خمیس مشیط فرود آمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149042" target="_blank">📅 23:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149041">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8ba758d8.mp4?token=CEljx5HVaRqWPKP6aX6Xd17cbxYlVIdp1u-suqAVoOMDXr3qS-PAqGhQvyqDBullwh_g_BwqnmmWdtYkFNgDGn2gXb0QxKd5z8e5ZKlpG6U3-tFb67FtWAtgXqJ6M6xa076ZximjrSeNelJuGOsE0P83m2HtIDa8BKL9peg6DeDK5uoJmFBBWoPHWkL7iG6qNCSxDD9k4GjHqzpgPlq8XIpdZ5n7-t5TBiBbZFFVUGulgVCdtCAwGARLKZtzDm0Di8LBQyz1ZYaCoFuFDjmy1UtKLiG4OaQz-QIqzsdgu5F8Gyxj89BsrtTRGHcz8JSi_VEv_QXuGXX_VzFN8RzYqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8ba758d8.mp4?token=CEljx5HVaRqWPKP6aX6Xd17cbxYlVIdp1u-suqAVoOMDXr3qS-PAqGhQvyqDBullwh_g_BwqnmmWdtYkFNgDGn2gXb0QxKd5z8e5ZKlpG6U3-tFb67FtWAtgXqJ6M6xa076ZximjrSeNelJuGOsE0P83m2HtIDa8BKL9peg6DeDK5uoJmFBBWoPHWkL7iG6qNCSxDD9k4GjHqzpgPlq8XIpdZ5n7-t5TBiBbZFFVUGulgVCdtCAwGARLKZtzDm0Di8LBQyz1ZYaCoFuFDjmy1UtKLiG4OaQz-QIqzsdgu5F8Gyxj89BsrtTRGHcz8JSi_VEv_QXuGXX_VzFN8RzYqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خاویر میلی، رئیس‌جمهور آرژانتین:
اگر نتانیاهو نبود، تردید دارم که اسرائیل امروز همچنان وجود می‌داشت، و این یک خطر واقعی نه تنها برای اسرائیل، بلکه برای اروپا و کل غرب خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/149041" target="_blank">📅 23:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149040">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
عمان: خدمه یک کشتی تجاری هدف قرار گرفته را تخلیه کردیم
🔴
یک خدمه جان باخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/149040" target="_blank">📅 23:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149039">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سخنگوی سپاه: پزشکیان امروز پیام قدرت را از قلب نظام سلطه بازتاب داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/149039" target="_blank">📅 23:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149038">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g12uOWAlRzAgUzniavUeSNnyZOWl2QiQjVLlOIUQgISov9VzILrWCeqmoEZW9pSV7uPJWNkhVVUho4vGLnOHiHWvjWJhA-eewDId1LwWZEuOj5VpmefIqQ8T8U-rXGfsYrlneHyta-LfEZ4yh5grBMcDpVZ_ugn2bcVWtIjOANY0jp7HZvNrbiVcoFMdFuLEPd5-6fef_X3a5yrS628Sj7J3trISxEKP5LLGVDiQ-3104Aldl4lRGlVOm9glUPiHubQWuqiikLdB2yD8YNvlusWwQdKZoKZWzLeExBeQ2Pv-mbSWZawm_fd4ZA3oTpfQ3aDLX6cJzCqd9T-UbWje9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش ۴ درصدی قیمت نفت پس از سخنان محسن رضایی مبنی بر حمله به فرودگاهای منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/149038" target="_blank">📅 22:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149037">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / شلیک موشک به سوی کشتی‌های متخلف در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/149037" target="_blank">📅 22:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149036">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
زلنسکی در مجمع عمومی سازمان ملل: روسیه با پهپاد های شاهد و تکنولوژی ایرانی نمی‌تواند ما را تسلیم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/149036" target="_blank">📅 22:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149035">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKTOji1yt8fcm0o5BktBXvkqLO3hYUNU9rK93dCXWJVCA_uC9YULOQi0QqoLqk8WTYRAwlGnedRYteibbKLcYQ7nzPzvF8W_Knc7j4y5sRmNLBZ4q0_W-rE_h4nY-ttL_8FHdL9nAf8EC-MIp3NPwoUvA4VR7wJlsIwyS5Yx-AMR0Rw4QBB08-DXNxGZtUWHpqqSYdU62wKiO4S1MvaCph9-H8ULMA-upzVbYi7iaaxcp1eVIGbPHhsTuJkyd06sgpPUn25sVgcyw8vE88cvUQcd0-MdqqdxsFdmKoCYyYSqbwp0V7lL_WKXmWpc8JmyLSARj9ix1MNVlNE2vC_QLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز:
ایران تهدید به فلج فرودگاه‌های همسایه کرد
🔴
ایران تهدید کرده اگه همسایه‌ها پروازهای ایرانی رو قطع کنن، فرودگاه‌هاشون رو فلج می‌کنه. این تهدید تازه‌ست و می‌تونه تنش‌ها رو تشدید کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/149035" target="_blank">📅 22:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149034">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دولت ترامپ: فعالیت سه رسانه تهدیدی برای امنیت ملی است
🔴
به گزارش USA Today، وکلای وزارت دادگستری آمریکا در دفاع از ممنوعیت فعالیت CNN، MS NOW و پولیتیکو در کاخ سفید استدلال کرده‌اند که نحوه گزارش‌دهی این سه رسانه می‌تواند تهدیدی برای امنیت ملی ایجاد کند.
🔴
این استدلال در جریان پرونده قضایی مربوط به تصمیم دولت ترامپ برای محدود کردن دسترسی این رسانه‌ها به کاخ سفید مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/149034" target="_blank">📅 22:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149033">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
احتمال صدای انفجار کنترل شده در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/149033" target="_blank">📅 22:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149032">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
تحریم‌های جدید کانادا علیه ایران
🔴
وزیر امور خارجه کانادا: امروز کانادا تحریم‌های بیشتری را تحت مقررات اقدامات ویژه اقتصادی علیه پنج فرد و پنج نهاد ایرانی اعمال می‌کند.
🔴
دلیل  این تحریم‌ها «حقوق بشر و خشونت غیرقانونی» ذکر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/149032" target="_blank">📅 22:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149031">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
هیمتی: در حد توانمون تورم رو کنترل می‌کنیم باقیش رو هم هرچی خدا بخواد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/149031" target="_blank">📅 22:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149030">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
جزئیات مذاکرات ایران و آمریکا در سازمان ملل/ آمریکا رفع محاصره دریایی ایران را نپذیرفت
🔴
مذاکرات ایران و آمریکا در حاشیه مجمع عمومی سازمان ملل با میانجیگری قطر انجام شد. در این رایزنی‌ها، استیو ویتکاف و جرد کوشنر از طرف آمریکا و عباس عراقچی از طرف ایران حضور داشتند.
🔴
اسماعیل بقایی، سخنگوی وزارت امور خارجه، گفت هدف این تعامل، انتقال شروط ایران از جمله پایان جنگ، توقف اقدامات نظامی آمریکا، رفع محاصره دریایی، پایان فشار اقتصادی و آزادسازی دارایی‌های ایران بوده است.
🔴
با این حال، بر اساس گزارش العربیه به نقل از یک منبع آمریکایی حاضر در مذاکرات، واشنگتن درخواست ایران برای لغو محاصره دریایی را نپذیرفته و اختلافات میان دو طرف همچنان پابرجاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/149030" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149029">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صید یک ماهی عجیب در دریای بالتیک  [@AloTweet]</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/149029" target="_blank">📅 21:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149028">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ5FcJI2FRSTe7e6lCiyQyYg-x7R1B_RbgrGgVbpRh9UxCnYEX2c2rGVTImVOFTZ9LwrpXhsE602CEHaQMQk08CKp1TXwCEutkxhC-jywi1knmu7C3vk2YpPaeiG8H2bZfWkEpM2Y721rnpmq7vULV0GTJ_izf7rvi8cS-2ylDLw2t1ITCBaIy7eABweyUsw0IrZS1RBkL28wYuVSvLSpn3mMAgTEpm7sPPLTwza5iumvkBABw4cnero03PBanm6Yf-4Ei0BRwvYzK_s2MKagbinNPvl4R8vJ83yFy8UUo3N9cVX1OrpzLzujseLTmTi-fFGeC1D1tUf7QoYRKem6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش روبیو به سخنرانی پزشکیان: کسانی که ده‌ها هزار معترض بی گناه را میکشند حق حرف زدن درباره منشور سازمان ملل را ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/149028" target="_blank">📅 21:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149027">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
زلنسکی: امسال به طور میانگین هر ماه ۳۱ هزار تا روس رو توی جنگ کشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/149027" target="_blank">📅 21:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149026">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfa61ab86.mp4?token=j8Z4wfvlJcQBg5h2xXirhLHSNm7BwGxCk4eJVv-ermro2--WfoF2ZaECvz74GPiw9IhqXP8m-7I5fn6NVQYkFJr3fAERCMs0L8daX-pfddZ9BGFarYc0foAFKOuZ2g2YqLxrvU42DLyH5LFTfCOYaCLlla0IPNrDTF5LcqvgCscRYTRyATaW7147PCXf7iJXIWM1LuwrmlcRTU4e9heZ8kK_VWtQVaoyqXGRWWmYD4wCbuH49uSeism0Oz7_4rwBNbm-Tmqk46uHTL8zQlCjwyv17NiwkXXaf_uEnKLfEyHn5jtmnbpJDCYozNeiihSOxE5b3WOOhv2MeTR8H40w-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfa61ab86.mp4?token=j8Z4wfvlJcQBg5h2xXirhLHSNm7BwGxCk4eJVv-ermro2--WfoF2ZaECvz74GPiw9IhqXP8m-7I5fn6NVQYkFJr3fAERCMs0L8daX-pfddZ9BGFarYc0foAFKOuZ2g2YqLxrvU42DLyH5LFTfCOYaCLlla0IPNrDTF5LcqvgCscRYTRyATaW7147PCXf7iJXIWM1LuwrmlcRTU4e9heZ8kK_VWtQVaoyqXGRWWmYD4wCbuH49uSeism0Oz7_4rwBNbm-Tmqk46uHTL8zQlCjwyv17NiwkXXaf_uEnKLfEyHn5jtmnbpJDCYozNeiihSOxE5b3WOOhv2MeTR8H40w-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید حدادیان، مداح: مجتبی خامنه‌ای امام ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/149026" target="_blank">📅 21:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149025">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">💢
قیمت دلار و طلا منفجر شد</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/149025" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149024">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
زلنسکی: فقط یک نفر علناً طرفدار ادامه این جنگ است
🔴
من هیچ‌کس را نمی‌شناسم که علناً طرفدار این جنگ باشد، جز یک نفر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/149024" target="_blank">📅 21:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149023">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6137406465.mp4?token=iJhTXbwlprWqVETWRrUBQkMKd1pThSh2iZNY1BfPodpb68fzurd_CSm3QAfdWgRkA_t_QWdmwxj0tpZ_f_ZXlnBT-FYqhhNYpnk_ECrEP9V1NyfSbCmv55lzaY9gmMKsXMf3ZgHWxSpYDvDmoQDy-sJf2sQYjGbqrZoodakJT86NEZfDWV1x6345DwK6hdylPT2AACj5AkeDVsDNyFSPMdINeNKTgsTDuc1iYPAXPCJaPdLim1EdmV_htFxYDTHzaIM2DsrpKUTCZZ2tSXqfsSFH2IrWhQmforwIMcOc6Z0USB5Vyp11QhE_F8JfKVHt-jTTpXjnP3-hbLkK0FEhFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6137406465.mp4?token=iJhTXbwlprWqVETWRrUBQkMKd1pThSh2iZNY1BfPodpb68fzurd_CSm3QAfdWgRkA_t_QWdmwxj0tpZ_f_ZXlnBT-FYqhhNYpnk_ECrEP9V1NyfSbCmv55lzaY9gmMKsXMf3ZgHWxSpYDvDmoQDy-sJf2sQYjGbqrZoodakJT86NEZfDWV1x6345DwK6hdylPT2AACj5AkeDVsDNyFSPMdINeNKTgsTDuc1iYPAXPCJaPdLim1EdmV_htFxYDTHzaIM2DsrpKUTCZZ2tSXqfsSFH2IrWhQmforwIMcOc6Z0USB5Vyp11QhE_F8JfKVHt-jTTpXjnP3-hbLkK0FEhFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشت پهپاد که امروز توسط طالبان افغانستان به سمت پاکستان پرتاب شده بودند، سرنگون شدند.
🔴
در این حمله از مهمات سرگردان، پهپادهای انتحاری و کوادکوپترها استفاده شده بود، اما هر هشت فروند سرنگون شدند.
🔴
گفته می‌شود تمامی این پهپادها در مناطق کوهستانی خارج از کوهات و در نزدیکی تورخم در ایالت خیبر پختونخوا پاکستان سرنگون شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/149023" target="_blank">📅 21:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149022">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کانال ۱۳ عبری: نتانیاهو امشب اسرائیل را ترک می‌کند و فردا صبح به نیویورک می‌رسد و فردا شب بلافاصله پس از سخنرانی در سازمان ملل به اسرائیل باز خواهد گشت.
🔴
نتانیاهو به دلایل امنیتی ویژه در خاورمیانه، حتی یک شب هم در نیویورک اقامت نخواهد کرد و فوراً به اسرائیل بازمی‌گردد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/149022" target="_blank">📅 21:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149021">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
محسن رضایی: هر کشوری حریم هوایی خودش رو به روی ما ببنده، فرودگاه اون کشور رو نابود می‌کنیم؛ اون‌ها هم دیگه نمی‌تونن پرواز داشته باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/149021" target="_blank">📅 21:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149020">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پزشکیان امروز غیرمستقیم گفت که معترضان دی ماه، مزدور مسلح شده توسط آمریکا و اسرائیل بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/149020" target="_blank">📅 21:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149019">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
👈
بقایی:
بله دیروز با آمریکا حرف زدیم و براش شرط گذاشتیم جنگو محاصره و فشار اقتصادی رو تمام کنه، پولامونم آزاد کنه، تنگه هرمز هم دست ما باشه و یه دور هم به ما بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/149019" target="_blank">📅 21:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149018">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فارس: پزشکیان در نیویورک در هتل مستقر نشده است
🔴
پزشکیان در سفر به نیویورک به‌جای هتل، در محل اقامت نماینده ایران در سازمان ملل (رزیدانس) مستقر شده است
🔴
این اقدام با هدف کاهش هزینه‌های سفر، برای اولین‌بار توسط یکی از رؤسای‌جمهور ایران انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/149018" target="_blank">📅 21:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149017">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر نفت: پول نفت‌هایی که فروخته‌ایم درحال وصول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/149017" target="_blank">📅 21:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149016">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پولیتیکو به نقل از منابع آگاه گزارش داد:
دولت ترامپ در حال آماده‌سازی طرحی برای ممنوعیت سه ماهه صادرات گازوئیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/149016" target="_blank">📅 21:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149015">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU2cPHMDMdpbX1THgGVbgdSu7b337BLJtzSWKa5hxA2tP_23rzVDQmEHID-ydhZVfNq7qsMmH3Fttog3cvIQz_reDmfT4M4Uy0TQREFcX04bn3bz4tYpTwTvWuApdIncmr5tUUPI36GA8BoCCdwvTCkwj_x5Lc1-vMDUwaeVCuMXHvqpYK9ED7R-IbBdhlhiMPNCPfye4jow9nirw_k2aMgSPklU0t1hSGHu7HHRuXtbH3gNrmdqlrWFye0Aof-TKEqfr1jikC5HcDA84LKyYMKjlGIkfGBZH3b_VVIP0_ax2DsTPdlWKAvE1Mrm2xYPCtBq4t6w4Wg9ObsJAt6vJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آپدیت جدید تلگرام اینجوری که وقتی وارد پروفایل یکی میشین اون قسمت بالا شمارش میزنه بطور میانگین، چقدر سریع به پیام‌ها پاسخ میده مثلا ۱۰ دقیقه، ۱ ساعت یا ۱ روز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/149015" target="_blank">📅 20:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149014">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15548e76f5.mp4?token=J435x_oMuDskV1miFiAr2K-uirnRq0uDrM2-qg7MtzW0IFL8JpLSHGUvNN3LQmzPL_qEVDsIUU6X0mhOgXATghjkcz0g_UqeT25avgloDcYJyknUR1MuM6O91msvNuuMs-eIc-IosQuvvu22pDvBXNf-57QFwoOYiT5Fyf13FToV8Ia10pHgJYnHM9j3D0DsmGJuHHacPLVuE92cyO2eH7sZyrmZgKgEK9CbLJXYD1Hgi-3WJmpbL9Xm1NJfSigg62Dp8lB03l3YMwtoJVbyH0eNa5jQS9At5kOsGCoVG5QDznL3eoqCQAtpGIIeJzPF4rTb19plPbsd0-WH5ozfDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15548e76f5.mp4?token=J435x_oMuDskV1miFiAr2K-uirnRq0uDrM2-qg7MtzW0IFL8JpLSHGUvNN3LQmzPL_qEVDsIUU6X0mhOgXATghjkcz0g_UqeT25avgloDcYJyknUR1MuM6O91msvNuuMs-eIc-IosQuvvu22pDvBXNf-57QFwoOYiT5Fyf13FToV8Ia10pHgJYnHM9j3D0DsmGJuHHacPLVuE92cyO2eH7sZyrmZgKgEK9CbLJXYD1Hgi-3WJmpbL9Xm1NJfSigg62Dp8lB03l3YMwtoJVbyH0eNa5jQS9At5kOsGCoVG5QDznL3eoqCQAtpGIIeJzPF4rTb19plPbsd0-WH5ozfDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرگئی لاوروف، وزیر خارجه روسیه:
اگر اروپایی‌ها این بازی‌ها و اقداماتشان را انجام نمی‌دادند، اوکراین مرزهای سال ۱۹۹۱ خودش را حفظ می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/149014" target="_blank">📅 20:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149013">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJ8NGcOmrNYm9MNbjWzkUhiPIjUT18IYheXCByoq-e-7vz5SB0LBMwHhB5Vw2vSurLjwe5fCMI7aO9rO9vGRqWM1FaoQsXJTuVMzqfgNWaM3O31QKOtEadFvowHZ6neNPhelai30cBDdziZfgkDWKRn_UG4Y9aprBLfhHGO_XNF5voKaKGfoNydQp159YmPZARWlM2ON9eelQ8sh0U0sWVMRmAl8gkGgREaOdDHEayNcakSFOM9nDp_avr7J4Yh3pIiMvph0hINfjqvb_WEo-9L1Kpx0fqo-WjXwJ-4GDiEfaqVylx8IOCCuMwly3MX9ns-dJi03r9WElgqQa1Qjsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور دختر و داماد پزشکیان در مجمع سازمان ملل در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/149013" target="_blank">📅 20:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149012">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تنگه همچنان تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/149012" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149011">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
توفق فعالیت بانک ملی ایران توسط امارات: بانک مرکزی امارات فعالیت بانک ملی ایران را در این کشور ممنوع کرده و تمامی شعب آن را از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال پول، منع کرده است.
🔴
بانک مرکزی امارات دلیل این تصمیم را نقض مقررات مالی این کشور، از جمله رعایت نکردن الزامات مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/149011" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149010">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9accb50b1.mp4?token=N8sdZIwEOg4X3_b6lttVnLPFS3TciP2c2bGz4phtDebxQ8Txk2vfwOJWzrR84F3zbEL0mrcEyp7qdAOuBWLeExIOB7tGGYlgzpAej-GHR5TphVV5g28Fn5hmn3vLi5peElRrk3ZQ86Tb004VIZkx_GlEvPGz7rg1FkSl6qsBnzatUFjMwvrp7A_DuYqAvZlBNZzCHXxIR5EpEnHt-_3odD42WQbZ6y0cc_XXjqYYNMIDW_BlD1TTEEkj42ziuxOGQPQWtdK1SvF2PKNkKgzWq7-VKFssJ0bBw9UHHBvt8ooWtTHL6LDKnEazzDBWejgG1N8_cnI7F9A5tdNXT3JJtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9accb50b1.mp4?token=N8sdZIwEOg4X3_b6lttVnLPFS3TciP2c2bGz4phtDebxQ8Txk2vfwOJWzrR84F3zbEL0mrcEyp7qdAOuBWLeExIOB7tGGYlgzpAej-GHR5TphVV5g28Fn5hmn3vLi5peElRrk3ZQ86Tb004VIZkx_GlEvPGz7rg1FkSl6qsBnzatUFjMwvrp7A_DuYqAvZlBNZzCHXxIR5EpEnHt-_3odD42WQbZ6y0cc_XXjqYYNMIDW_BlD1TTEEkj42ziuxOGQPQWtdK1SvF2PKNkKgzWq7-VKFssJ0bBw9UHHBvt8ooWtTHL6LDKnEazzDBWejgG1N8_cnI7F9A5tdNXT3JJtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خاویر میلی، رئیس‌جمهور آرژانتین:
حملات رژیم ایران علیه اسرائیل را محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/149010" target="_blank">📅 20:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149009">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP0a2kWY45kLiLmOUtaVaufqM6UYTCpaK3TBA77_iuh_2yqMsTCqPVc5FQa7OKvwS_bbS59Kg0WuHy5nZo-iJX-9ogaXPzuDaVNgKv5ONQhEgruC3C5CT1HL0MQpKAqkXQFr5jEKlL0zxInqUDLfNDD-5Uo135eVTMp018vpFhhRZVbNdgTZhkcy6AdrjJspMTFRxJ4hB1fI7MHxNoyfSqXMolQDIJU8s0nJ3r59YHu1oqh_08W1UpHqbaWktuezx2rMGtkywZGzgHcoajmdOjmzp7qYn4QSDO6PgFPmWdY1VsB10u5GlR0TS2bnq85xQpi6Zs7FD4z3WsUDPbCh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار پزشکیان با نخست وزیر عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/149009" target="_blank">📅 20:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149008">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
کوشنر: دستیابی به هدف رفاه در نوار غزه، مستلزم خلع سلاح کامل آن است و حماس موافقت کرده است که سلاح‌های خود را تحویل دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/149008" target="_blank">📅 20:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149007">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCnPBnr8Dt-1vX9FoE2wcPlhYCJ3FHVmVwjwfqyE0AJT2W7zUrIUyj4Hh0ZJtwTqfQggP2cfX0PGLrtkz4dXid6BrwIoRlQdyDQAxpB6bQIoNP6aEvsph7Ak5D60W4jP0Rf_jzvjgbTLjvjNlWHqHKTpR_shjs817wPhBV20P11PDraodh89oHM1xPmPjFFKv-uIxnEKQRC8N7u8T2ekSg61CCfMyhs40t-WSddiD9xt1XakDaVbFOJzxGxTTHKxttg6tCL_JrbibMQpls6ebrvB29cdJp-volz7Tcp-iha-7e-IV6tzRQkf_cJEYEFI3I6W--abbvohDCxwjkb-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: رئیس‌جمهور پزشکیان نه تنها برای یک دولت، بلکه برای تمدنی ۳۰۰۰ ساله سخن گفت.
🔴
او صدای قدرتمند شجاعت، استقامت و قدرت برای جمهوری اسلامی ایران بود.
🔴
ایران سرافراز و مقاوم، به درازا زیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/149007" target="_blank">📅 20:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149006">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e39111516.mp4?token=chgKX1XfloWVakSa4iD3cz2XAAvA2NmK4xFEyY_R-2_qiDZIpjF2lBty30PRELUOtDD1hRAsxwZvNnozFsigrqa31xTcumqDHQgvaN487UsckXIjz7XUthK9tHqIF2g6GbX6df6hQFzbeQMXOoRrWphfMox1-6Bm8qWTLlFk2xdEm2fFMHDdA3b0ZgsHMK7HqJTdB4F1XqseeXYLQGM65o5P620cS08tiXp7xn51g5s6JWVTwXzJZyCcVyeRff48zQ1ItOgp1Jn-7P3fCjA83Za2uwge9fPoGbl8CZwlPgpsMK0plsThSFPHW9MC3d_G2o8QW0O7SBXFhHOWyxTmRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e39111516.mp4?token=chgKX1XfloWVakSa4iD3cz2XAAvA2NmK4xFEyY_R-2_qiDZIpjF2lBty30PRELUOtDD1hRAsxwZvNnozFsigrqa31xTcumqDHQgvaN487UsckXIjz7XUthK9tHqIF2g6GbX6df6hQFzbeQMXOoRrWphfMox1-6Bm8qWTLlFk2xdEm2fFMHDdA3b0ZgsHMK7HqJTdB4F1XqseeXYLQGM65o5P620cS08tiXp7xn51g5s6JWVTwXzJZyCcVyeRff48zQ1ItOgp1Jn-7P3fCjA83Za2uwge9fPoGbl8CZwlPgpsMK0plsThSFPHW9MC3d_G2o8QW0O7SBXFhHOWyxTmRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی که تحت عنوان خروج نماینده‌ها هنگام آمدن پزشکیان منتشر شده مربوط به پارسال و سخنرانی نتانیاهو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/149006" target="_blank">📅 19:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149005">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO1HuDiyuUU8Al_UEXHsOuKfvzbBeWsboavPS2Bz8Rwd-5ZDdtA9K2bfthjHHJ8mjuW0CkORcq2Q2qzztUEi86MQ8mqMC3Sul7pd3C7EMg7QuufCvml65h-QOLpkMMQLwty7l2-rteLjOrzxWapdwsaUowJ4I5dEbTJGywoFadHslJWm-5dF5YzACffMEXGRYoCp6q0GukVmxP8O14UU6tQ7HmT92DAWxa5tikDzF8rgsbgo_fxjkS31_Nnfyve9Pzhsa17AXCS9k1HQ9O6BR4F3HRHooJbvCfOfjyTsE34UntXhpIOmJmIEfyEzm5HaOlMwCVKPmmtLC3mnJ4lfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت برنت، ۱۰۲.۷۶ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149005" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149004">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6_qHQUgM-5yhYZ7qWt-3xkLqXEBIxLTl7jq6eCM0UVDZbfrEcfLjnuqPs8WDxY65lBSHgjo-GJMj_qRyfgojNw99KjUiy8HACDnoyTGLBOp2lHspPSP-CRmRTh6CfKs1YefLv9N-DNnZdE2vm5AAY7UMKH1ryOTUT9U2VwB00GoiLx0xzvMWKgkxNhfflOfwsnjmpv740pI9viiCLPBfpgIZsGOFBAEtGjdlcOaPoUFLh7WLy4__NGow0lKan5REDQDjlhfOdvY03v2yQ1fQvdNHmoDUB86uHFIpnBO8u2KkKLLcHHwemAMlIlMzQgdTHj-0mjjMjxYhgUTmfgP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنتاگون در میان جنگ با ایران، یک فوت نظامی آمریکایی دیگر را به پایگاه داده عمومی تلفات خود افزود و مجموع رسمی اعلام‌شده را به ۱۹ نفر رساند، هرچند مقامات آمریکایی می‌گویند تعداد واقعی بالاتر است، به گزارش واشنگتن پست.
🔴
ارتش این افسر را کاپیتان بیانکا سی. ویلسون، ۳۷ ساله، ساکن نورفولک، ویرجینیا، شناسایی کرد که در ۱۸ سپتامبر پس از یک «اورژانس پزشکی غیرنظامی» در حین پرواز به خاورمیانه جان خود را از دست داد.
🔴
او به پایگاه هوایی شو در کارولینای جنوبی منتسب شده بود و در حال حمایت از عملیات در دوحه، قطر بود.
🔴
ویلسون پس از مرگ به درجه میجر ارتقا یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/149004" target="_blank">📅 19:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149003">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / حادثه برای یک کشتی در نزدیکی ساحل عمان
🔴
مرکز امنیت دریایی عمان: ما خدمه یک کشتی تجاری را پس از هدف قرار گرفتن در فاصله ۲.۵ مایل دریایی از سواحل استان مسندم، تخلیه کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/149003" target="_blank">📅 19:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149002">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2901dc9b92.mp4?token=YZOZ9esQKt3nosDtk3op3PKk4dOGDoM5i2Bc18NM-yauuEy11IgqQFQK_H0gzgkjHOTnmxYhbbSECNjsh-_SGNmsgt6w6HYeLhECZCEr1i7VRjzYFffqT1Kne5Pp9lPV23FlCdDu2M0ggXBeRIf5ApM1_K-N3Roj7smVHOBPgaulKYpR9SB_pp0_O3NqIgdna-1cC4t1yzc-rNOFiZDNIvJp8-YzgjfrPorpXl4lbGtWJ7Q_ytDyYsdE7e-yulEqdfvqfO7hntQBBS73MIjS2l-Pw3I-HmNaGiUJlgfSIhfMiDPR1cSng-stWTnXh7ukqODHt-jDbTAMPMa46a4NNL-gLevw7rea8OSAsM8glthaFb9fjXHiALGIP1_3N_wr5kBzNkPTyK_lE9w87yzE0akTqvvI3lwS3i6Y3GczCch8k8CdNOLp-E4wG6Dl5tZ2X16981dJ4q8HBahFmBlNHwWhNGjB1ABHM9Tx6HNT0t3LO1S4GxwvBlLMi3ZJ-jApCfZRp7Ye2wmYi4GCf-Azy09mIoSjn3-wGyXhWHY88MZ2YgsUExJ3ydv4zybRgLHDTi-pfUqZKfBDVKYNfm9Xw6Iz7xRaM2Y-zGdogOW8OBXLNSaVfSCSVLdpzl0iP4-CspJ2mLCaEaPKTX7f5JVgGEsy4xoru06CZwjUVh1-QXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2901dc9b92.mp4?token=YZOZ9esQKt3nosDtk3op3PKk4dOGDoM5i2Bc18NM-yauuEy11IgqQFQK_H0gzgkjHOTnmxYhbbSECNjsh-_SGNmsgt6w6HYeLhECZCEr1i7VRjzYFffqT1Kne5Pp9lPV23FlCdDu2M0ggXBeRIf5ApM1_K-N3Roj7smVHOBPgaulKYpR9SB_pp0_O3NqIgdna-1cC4t1yzc-rNOFiZDNIvJp8-YzgjfrPorpXl4lbGtWJ7Q_ytDyYsdE7e-yulEqdfvqfO7hntQBBS73MIjS2l-Pw3I-HmNaGiUJlgfSIhfMiDPR1cSng-stWTnXh7ukqODHt-jDbTAMPMa46a4NNL-gLevw7rea8OSAsM8glthaFb9fjXHiALGIP1_3N_wr5kBzNkPTyK_lE9w87yzE0akTqvvI3lwS3i6Y3GczCch8k8CdNOLp-E4wG6Dl5tZ2X16981dJ4q8HBahFmBlNHwWhNGjB1ABHM9Tx6HNT0t3LO1S4GxwvBlLMi3ZJ-jApCfZRp7Ye2wmYi4GCf-Azy09mIoSjn3-wGyXhWHY88MZ2YgsUExJ3ydv4zybRgLHDTi-pfUqZKfBDVKYNfm9Xw6Iz7xRaM2Y-zGdogOW8OBXLNSaVfSCSVLdpzl0iP4-CspJ2mLCaEaPKTX7f5JVgGEsy4xoru06CZwjUVh1-QXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو، درباره مهمات: ما مهمات کافی برای دستیابی به اهداف خودمان در صورت ایران داریم، اما تنها در ایران نیستیم.
🔴
ما تعهداتی در منطقه هند-اقیانوس آرام داریم. ما تعهدات فزاینده‌ای در فرماندهی جنوبی داریم. ما تعهدات و متعهد بودن‌هایی به ناتو و شرکایمان در آنجا داریم.
🔴
هر بخشی از جهان که بروید و به آن‌ها بگویید که پنج سرباز آمریکایی کمتر و دو هواپیما کمتر خواهد بود، همه وحشت‌زده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/149002" target="_blank">📅 19:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149001">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
روبیو: سپاه مانع مذاکرات با ایران شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/149001" target="_blank">📅 19:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149000">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016da093a0.mp4?token=Q47cDijNAoLzeuNBvL_8ezkOfb3Wf1n9HH-KtrlY4t6cIj_WsmjM3YzUpqqR6UT7KH-XghzzOvexE28EBCTq8_Kv4P7Lp8KvgKScUqstQrdTzwvqE5Y7ZEwm13dnbCbnt07F0wlk_TsyAcO7HIXT6ApONONhZae--y7r6_CGu8c1Anah13PVd5YDH7lR3TfeT-GXGenCl_zwCB1ows-MsSTIOSD-mztw7n9_n-AF8MsMiYyDkO7-sQGGZqFvewemRDiGO2KWw40WXFSlUXq20RF2eyf30biMGS6R9nloYTh72t8eSGzPZiAdaT712KO-5gg0HXNYcMLX_Aq-4BBDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016da093a0.mp4?token=Q47cDijNAoLzeuNBvL_8ezkOfb3Wf1n9HH-KtrlY4t6cIj_WsmjM3YzUpqqR6UT7KH-XghzzOvexE28EBCTq8_Kv4P7Lp8KvgKScUqstQrdTzwvqE5Y7ZEwm13dnbCbnt07F0wlk_TsyAcO7HIXT6ApONONhZae--y7r6_CGu8c1Anah13PVd5YDH7lR3TfeT-GXGenCl_zwCB1ows-MsSTIOSD-mztw7n9_n-AF8MsMiYyDkO7-sQGGZqFvewemRDiGO2KWw40WXFSlUXq20RF2eyf30biMGS6R9nloYTh72t8eSGzPZiAdaT712KO-5gg0HXNYcMLX_Aq-4BBDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: به نظر من، ایرانی‌ها معتقدند که دموکرات‌ها در ماه نوامبر پیروز خواهند شد و ترامپ دیگر نخواهد توانست هیچ کاری علیه آنها انجام دهد. آنها کل امید خود را روی این بسته‌اند.فکر نمی‌کنم آنها درک خوبی از سیستم ایالات متحده آمریکا داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/149000" target="_blank">📅 19:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148999">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه: دونالد ترامپ واقعاً معتقد نیست که جهان در حال حاضر به یک «بحران کرانه باختری» نیاز دارد و این موضع ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/148999" target="_blank">📅 19:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148998">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مارکو روبیو، درباره چین: روابط ایالات متحده و چین سده بیست و یکم را تعریف خواهد کرد.
🔴
ایده اینکه ما در بالاترین سطوح با آن‌ها تعامل نداشته باشیم، بی‌مسئولیتانه است. این امر بی‌پایه و اساس است. ما باید این کار را انجام دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/148998" target="_blank">📅 19:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148997">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25554fe971.mp4?token=kWDPVpEPv6BXEfSkPbqiIqbQXojr5DEKeN8Yz0_HrGNZo9LTt_FK3_ioCoAlO3UTiViBT2gkPTnpBI3EnTItnQ0zuSSDOLqWrmlr93w0ydR5KVvGqV1ephvB3PCA8ESP9KDox3GNLptIfCHse_m6sxQixmfHI5rzgrUpAiD4yB7VsFy1IuyqMKSRgJig9-OsX5DinZOOuqT9Kz-bFgcjIdDclmPGxEhaT6yAfKpVYYBeFXKITlY-TG_V-8m4OtLivQwtncuR8LqiiMT-LOOMP38j1ne8_AkDR326FIknMyx4L1OnPBjupIyBykaK9DZbMHr00FZsozc6oa13kJ1PLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25554fe971.mp4?token=kWDPVpEPv6BXEfSkPbqiIqbQXojr5DEKeN8Yz0_HrGNZo9LTt_FK3_ioCoAlO3UTiViBT2gkPTnpBI3EnTItnQ0zuSSDOLqWrmlr93w0ydR5KVvGqV1ephvB3PCA8ESP9KDox3GNLptIfCHse_m6sxQixmfHI5rzgrUpAiD4yB7VsFy1IuyqMKSRgJig9-OsX5DinZOOuqT9Kz-bFgcjIdDclmPGxEhaT6yAfKpVYYBeFXKITlY-TG_V-8m4OtLivQwtncuR8LqiiMT-LOOMP38j1ne8_AkDR326FIknMyx4L1OnPBjupIyBykaK9DZbMHr00FZsozc6oa13kJ1PLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: من نمی‌خواهم مذاکرات دیروز را به‌عنوان یک پیشرفت بزرگ توصیف کنم، اما در عین حال فکر می‌کنم مهم بود که دست‌کم یک گفت‌وگو صورت گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/148997" target="_blank">📅 19:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148996">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpeo331KSQ9QrN80l3b8rr94uP0SwuOYeJ2g76AnUpKn1WArkhXTv6Cj670FgZnA-F68ox60rst2IMsz6mQE9BdCQQtFvFEdR6lQit4X6vx3y3J_pkLfCSn6CE6GAKYU7oe5FjNjyjBfvzHoDdD7bfSUnKO_aPxtkFcx9zYIyuxucmW-jPtxi3HG0cx-VkUm0E0OU00BKkaldrxDt_unJXVsddYGEDMwCBRNu0V89GAa81_gWFZ6I1nidp1-llAgrE4TgFXPeg_aamwDOt3AX9elPW-lms_MVsZxGiGAP3xfz1B_cENQfAkQVd9DDBhJbd7IW5pdkf4Fy-lQqgUJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شروط ایران اعلام شد
🔴
سخنگوی وزارت خارجه: توقف اقدامات تجاوزکارانه آمریکا از جمله محاصره دریایی، تروریسم اقتصادی،
خاتمه جنگ در همه جبهه‌ها، آزادی اموال مسدودشده یا محدودشده ایران، پذیرش مسیر ایمن کشتیرانی به شیوه تفاهم شده بین دو دولت ساحلی و ....
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/148996" target="_blank">📅 19:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148995">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797313ae14.mp4?token=t9gA4DR9cRUxUhInijvCDhlx4UgIxzh29c8Reb_QcTTSSWgrKSR6o5JQTM4M4BeazFiOiReznRIOiANhZs0cv-gGx8PBGaaX8CGyk2Q9EvhTnOkavfuwuRaJxxaNmLhGKaBcEvrgE8z6R3T9vMNeA0niekJYmE8eRGMhSLD80Vzh3DzMfEzcdzPT_Jzok2wb2G1LDHHRtaY_AhtqxAUIBpV-7Mjc95_TNZQ13h_wRFCoQvDnwXHcsQ6HHP5R_u_9xHHAQOy4yX5KdUmiLpAHl0Vwxbf9bcYbA-spWzJ6uS6Thz5pfADnf3eqJAFLdLiXJRc2OtfAcKBxKcaoTgr4S6s5KzkTC9lRAgQiAUYPb4DsvUleQp7GufZcIj0GtF2mjtFnUOa2vVRWyL6T2numvf8ofbSJMStjS3HoS5gnorU7jdv0p6lot0sYuIsi0mz71-ZUXQCuuIY1C89FEbTbZkmac5dfkD6Nv7YyUQUZMCsP2hJiLuCto4RE5Mj9hZkVmH2nWtpWtGiSmq0a-vJbeZfCQym84fdMD9oqLWkyfLOvTag5avaf6C8aGUmAvi2SIv6Fw3qhILgm1oH_VXgScsZJRPSevMmjWQX2r7bVnsSLCvti04jeVQVdLwAhcSNon8NvdwJTpBfyrLQ9y-Qun21nDB9PFralCisUx1g_Yiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797313ae14.mp4?token=t9gA4DR9cRUxUhInijvCDhlx4UgIxzh29c8Reb_QcTTSSWgrKSR6o5JQTM4M4BeazFiOiReznRIOiANhZs0cv-gGx8PBGaaX8CGyk2Q9EvhTnOkavfuwuRaJxxaNmLhGKaBcEvrgE8z6R3T9vMNeA0niekJYmE8eRGMhSLD80Vzh3DzMfEzcdzPT_Jzok2wb2G1LDHHRtaY_AhtqxAUIBpV-7Mjc95_TNZQ13h_wRFCoQvDnwXHcsQ6HHP5R_u_9xHHAQOy4yX5KdUmiLpAHl0Vwxbf9bcYbA-spWzJ6uS6Thz5pfADnf3eqJAFLdLiXJRc2OtfAcKBxKcaoTgr4S6s5KzkTC9lRAgQiAUYPb4DsvUleQp7GufZcIj0GtF2mjtFnUOa2vVRWyL6T2numvf8ofbSJMStjS3HoS5gnorU7jdv0p6lot0sYuIsi0mz71-ZUXQCuuIY1C89FEbTbZkmac5dfkD6Nv7YyUQUZMCsP2hJiLuCto4RE5Mj9hZkVmH2nWtpWtGiSmq0a-vJbeZfCQym84fdMD9oqLWkyfLOvTag5avaf6C8aGUmAvi2SIv6Fw3qhILgm1oH_VXgScsZJRPSevMmjWQX2r7bVnsSLCvti04jeVQVdLwAhcSNon8NvdwJTpBfyrLQ9y-Qun21nDB9PFralCisUx1g_Yiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، درباره ایران: ایرانی‌ها و نیابت‌های آن‌ها به تأسیسات دیپلماتیک حمله کردند — بی‌سابقه است. آن‌ها عمداً به سفارت ما در کویت بمباران کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/148995" target="_blank">📅 19:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148994">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198effcfec.mp4?token=rkBdIApDDznQ6WgIqWDRQsO6sYBUACJ95WlAKSDyg9bI6fMTdqZIQ1A9kP-y5tf2FGbB7x9xzAyUf9pz5Spx11PvTXg5_lLaHkbzIfpeMwDGEbOSMbdJf-1bSeGuEKl4xH9aZ8JEr2AXXfdunUG4pFU8guBsO-chMhSvprYsJPkdJETVp34yzuuY4izkQy0XwABtOFhgV-K6tm2KGDByhVXCGLpZ1fe7G7SMaKHgkW3DtqcGqUhLx18KZkG6WZSqfOCp_rD5J99hTQTGEkkxf5Aojt3Yit9oZaJHXs8aLZgp3CIz7SLYWigsfIzNPpmOFDOpY9opMMXy7osGEM4HMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198effcfec.mp4?token=rkBdIApDDznQ6WgIqWDRQsO6sYBUACJ95WlAKSDyg9bI6fMTdqZIQ1A9kP-y5tf2FGbB7x9xzAyUf9pz5Spx11PvTXg5_lLaHkbzIfpeMwDGEbOSMbdJf-1bSeGuEKl4xH9aZ8JEr2AXXfdunUG4pFU8guBsO-chMhSvprYsJPkdJETVp34yzuuY4izkQy0XwABtOFhgV-K6tm2KGDByhVXCGLpZ1fe7G7SMaKHgkW3DtqcGqUhLx18KZkG6WZSqfOCp_rD5J99hTQTGEkkxf5Aojt3Yit9oZaJHXs8aLZgp3CIz7SLYWigsfIzNPpmOFDOpY9opMMXy7osGEM4HMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: سورپرایزهایی برای سخنرانی‌ام در سازمان ملل دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/148994" target="_blank">📅 19:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148992">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام ایرانی:
بازگشایی تنگه هرمز و رفع محاصره آمریکا طی مذاکرات غیرمستقیم روز گذشته با آمریکا مورد بحث و بررسی قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/148992" target="_blank">📅 19:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148991">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59943f167f.mp4?token=rE9RATC-_C6JkzUh4FXoQdXRvrq1OCRBmObj1Di92QFVLuhIeSXst3Hfz8Q9EYilqSTjfyoQM9iPrDynRG6PNQCCiB1uKL-uU6BWqzSKoOJmQDkjv-NCtFhOFkbJeVZEFRCazdaQmijYU9BK4Xzc0oP1wYXTAe6GL6GQxyH_JPnwksNZsIlJkJN63SUROADIEZhJNxN5gI2gG6x3CayBhQBP095M7vQXuY1nuktu4U9xBEmLVwKafExQoDNmHwCWJL8YGr8Ezn44VEFjUhRLESRBJWx1QK6O0ni2QifXJp2Z4tyUlC79g0zVVg4dMTH2Z_pljKboZOfdMH4izn2dJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59943f167f.mp4?token=rE9RATC-_C6JkzUh4FXoQdXRvrq1OCRBmObj1Di92QFVLuhIeSXst3Hfz8Q9EYilqSTjfyoQM9iPrDynRG6PNQCCiB1uKL-uU6BWqzSKoOJmQDkjv-NCtFhOFkbJeVZEFRCazdaQmijYU9BK4Xzc0oP1wYXTAe6GL6GQxyH_JPnwksNZsIlJkJN63SUROADIEZhJNxN5gI2gG6x3CayBhQBP095M7vQXuY1nuktu4U9xBEmLVwKafExQoDNmHwCWJL8YGr8Ezn44VEFjUhRLESRBJWx1QK6O0ni2QifXJp2Z4tyUlC79g0zVVg4dMTH2Z_pljKboZOfdMH4izn2dJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب پزشکیان تو سخنرانی سازمان ملل به جای سانتری‌فیوژ، گفت سانتیری فوژ
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/148991" target="_blank">📅 18:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148990">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUo3SkR_n4jybaidqXZWy_pTAxloTcNtx25zgv3pUFn5hEOFeoi-ERxs3TFxihyMi1wbl0sd3ZV7VfvjEF11SObnfs4Wl3mC2Nik9epn2zv7SfZj_pTQh1mE5b7F7Ojr5qGIHUwUIwj0rHlylG7ASxfEQy2nTVsTTq0tawbMg8l_Qm42qnbbLgCkvL47gySj6XW75NphuKPDsBfxO-XpRQw9QZwXG0OXPo7ZFD2fI1GC_Ki5vWHq9KK29GoPWvt9P5G9DAXanjg3GKlCQXmdlIj259OltowV3chX_M_sl6kVDcijzSWwC8CYVK6o1Nmrfgxvg9f1cWhfoYRkFPfexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز جلوی سازمان ملل، سلطنت طلبان و مجاهدین درگیر شدن و این شاهکار خلق شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/148990" target="_blank">📅 18:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148989">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
👈
مارکو روبیو:
جلسه دیگری با ایرانی‌ها امشب برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/148989" target="_blank">📅 18:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148988">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f769da6b36.mp4?token=QImMGZbCX5TWUxa58d0IJl6SIsJZKAdGGkoUip5dyX8cKyKWKh8adf7yQY6oKWKl5lZvsSVmLbRTuLA6EXv-LFX6xI75qYvKtDkMmpf2Q6pJhYsRKmkeQ0fBxasYpP1LaMBNgz5c-nUdIT9nsanO4r9GVYakCNd_HO5UilW4bGfWPOMEsEtK1bJajgtxE-hHzP6uCugWt1iqaGU6wvbWhPmq-QS4b5rDsLpr0zhu9DumTyAmGDjzZQpUR7TesJQVA8XlyrQGz8FJhOrhbxJkYiWZ_Gp08mYZIP_7Hn08y3EipH5hSqTCFCRLxpfN8p0UXMdsHyrFip28O1j8-VhLpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f769da6b36.mp4?token=QImMGZbCX5TWUxa58d0IJl6SIsJZKAdGGkoUip5dyX8cKyKWKh8adf7yQY6oKWKl5lZvsSVmLbRTuLA6EXv-LFX6xI75qYvKtDkMmpf2Q6pJhYsRKmkeQ0fBxasYpP1LaMBNgz5c-nUdIT9nsanO4r9GVYakCNd_HO5UilW4bGfWPOMEsEtK1bJajgtxE-hHzP6uCugWt1iqaGU6wvbWhPmq-QS4b5rDsLpr0zhu9DumTyAmGDjzZQpUR7TesJQVA8XlyrQGz8FJhOrhbxJkYiWZ_Gp08mYZIP_7Hn08y3EipH5hSqTCFCRLxpfN8p0UXMdsHyrFip28O1j8-VhLpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگاران ایران اینترنشنال در بیرون مقر سازمان ملل وایسادن تا پزشکیان بیاد بیرون
و ازش سوال کردن
:
🔴
خبرنگار : چرا اعدام هارو متوقف نمیکنید آقای پزشکیان؟
🔴
چرا کشتار مردم رو متوقف نمیکنید
🔴
دست شما هم به خون آلوده شده آقای پزشکیان
🔴
پزشکیانم هیچ کدومو جواب نداد  سرشو انداخت پایین راشو کشید رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/148988" target="_blank">📅 18:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148987">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953c03a875.mp4?token=C6PkbeCqjZSb1aaItHMLwexuY9FKaPAGj12PYvUXC9KW4joGUvwnOZazPEIf3NgOxEON0JRAoNdIUAHn2_n0vhakC3jbvpr_QlPFLsM_TsxLy5TRPlW4WwUxiHmNOT5qDwTylCwar10MFde2DIsW2LebeDYyVdI4mQ8kvOA_lqZCRTegQdceV0KKFE3GwlPDvB6ILPvN9idZyrfV4vqCAxcC0i07PTCVXIz7WzoRzWJTekGQu-vKrHbAvxQHytfTea6onEGTbC-oAkAh5oHS5euUysSoP1W7mYYrkOc0e8CuIH70kpLUxphyaAchozYz58mSguFolpnaIrIok5vn0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953c03a875.mp4?token=C6PkbeCqjZSb1aaItHMLwexuY9FKaPAGj12PYvUXC9KW4joGUvwnOZazPEIf3NgOxEON0JRAoNdIUAHn2_n0vhakC3jbvpr_QlPFLsM_TsxLy5TRPlW4WwUxiHmNOT5qDwTylCwar10MFde2DIsW2LebeDYyVdI4mQ8kvOA_lqZCRTegQdceV0KKFE3GwlPDvB6ILPvN9idZyrfV4vqCAxcC0i07PTCVXIz7WzoRzWJTekGQu-vKrHbAvxQHytfTea6onEGTbC-oAkAh5oHS5euUysSoP1W7mYYrkOc0e8CuIH70kpLUxphyaAchozYz58mSguFolpnaIrIok5vn0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری آمریکایی: تعحب میکنم! ترامپ جمهوری اسلامی رو تهدید به نابودی میکنه وکلی بد و بیراه میگه اما نماینده ایران خیلی ریلکس نشسته و گوش میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/148987" target="_blank">📅 18:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148986">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRvB19FeRjmM8EuGKbXXwaLwqsjmuvjnxDVBNuvu6_c8r4or9N40wDt9bapR_XYPVxGl_pQsJ9KVW2QEJHRgTWkVqVXvc7N4gGpToz-lQ_rEiZ0zjfvHtMRe6Q1mtb3VV94g3VZWbOWgsgEsBn0H7ia8hXw_WXAdBNi7iF3VCT0fXu3pxPCFALpSjs1PJBQwvXZrBoUp9aVy3nY6sVpJ_vnXMQvt_TizMF97cPZ-CYNzr2-WT1XwxCwJmSlJX3eqVK8HCF192szsX2oNRwvf3zgttewj0lPY1cMeNAykwuT4Clb1Yd7ytln9E9HjgGMbVzcqnuo7TELqRt8E6rBxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از مخاطبین سخنرانی پزشکیان در سازمان ملل
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/148986" target="_blank">📅 18:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148985">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: رسیدن به توافق با ایران نیازمند کار مداوم در یک بازه زمانی طولانی است
🔴
ما به دفاع از تنگه‌های دریایی و باز نگه داشتن آنها ادامه خواهیم داد.
🔴
ترامپ گزینه‌های متعددی از جمله گزینه نظامی در اختیار دارد.
🔴
گذرگاه جنوبی تنگه هرمز باز است.
🔴
ایران معتقد است که دموکرات‌ها در انتخابات پیروز خواهند شد و ترامپ قادر به انجام اقدامی علیه آن نخواهد بود.
🔴
نیروهای نیابتی ایران در منطقه، امنیت و حاکمیت کشورهای آن را تهدید می‌کنند.
🔴
ما همیشه مطابق با منافع ملی خود عمل خواهیم کرد و نظم بین‌المللی را بالاتر از منافع خود قرار نخواهیم داد.
🔴
با کشورهای خلیج فارس در مورد لزوم باز نگه داشتن تنگه‌ها و مصون ماندن از هرگونه حمله، اتفاق نظر وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/148985" target="_blank">📅 18:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148984">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DytCuZd_MQ-n2RKElJ5MIpalEUkvQU91rMLUghXj353ONNE9lJ4U0XCiDYhDMccbRI3y91SopjmQNCJgn359T4or8cwI-pGMnHMiKUuCyPFf3CSnYm4GMloq2I2bYaFvE8Xc9FTmAsyAt-Yy-5CJMVebUq7-9ahp3pnSa662hcGiPoq50YuXFuuHuLfgw5fu6dvFXwN-bIibgHiJ7awxC9dQOsVwiuzkEzmazTh1mfcp59r3DUJiGUGd3SfmNZUFhmN_xwYIVZSpCfF4TwOTvCPVtXmRPiojTrTEaIlSMson6vLlGqc89bJlM_Igat4ZgYIgI70GwdhRk1Nv4d1asA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صف‌آرایی علیه وزیر اقتصاد در سازمان بورس
معاون اول پشت تحرکات در سازمان بورس است؟
🔴
با نزدیک شدن به پایان دوره ریاست حجت‌الله صیدی در سازمان بورس، تلاش‌ها برای حفظ او و مقابله با تغییرات مدیریتی، به شکل‌های مختلف شدت گرفته است؛ از مخالفت با برخی تصمیمات وزیر اقتصاد، علی مدنی‌زاده، تا تلاش برای بی‌اعتبار کردن برخی مدیران منصوب او در سازمان بورس.
🔴
در این میان، ادعاهایی درباره حمایت معاون اول رئیس‌جمهور، محمدرضا عارف، از برخی این اقدامات مطرح شده است؛ موضوعی که در صورت صحت، می‌تواند نشانه شکل‌گیری اختلافی جدی میان برخی جریان‌های مدیریتی اقتصادی دولت باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/148984" target="_blank">📅 18:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148983">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخن پایانی پزشکیان: ما آماده گفتگو هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/148983" target="_blank">📅 17:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148982">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پزشکیان خطاب به کشور های منطقه:
یا امنیت را با هم می سازیم یا ناامنی را با هم تحمل می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/148982" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148981">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏
👈
پزشکیان: چرا برای فلسطین کاری نمیکنید؟ مگه ظلم رو نمیبینید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/148981" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148980">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پزشکیان: بمب اتم و سایر سلاح های کشتار جمعی در دست اسراییل است اما از ایران می خواهند که بازرسی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/148980" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148979">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پزشکیان: اسرائیل به هر کشوری که دلش می‌خواهد حمله می‌کند
🔴
عاملان ناآرامی اسرائیل و آمریکا هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/148979" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148978">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پزشکیان: حمله به زیر ساخت های غیر نظامی خلاف قواعد بین المللی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/148978" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148977">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سالن چه خالیه
😐</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/148977" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148976">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=oeQXCPg-6hDnzJVS3B6YSm0p0ofMLcpX-6pDMUkZVvEccOI3eB_cAUcsEWQ1Aa8hA1M3PYDNZZmruLkllk2PSmQDaFgGET_G4Pw0jzel9C_tp3Xl7_Ndil7Yu40OAf_oJP0BAoVzL06o5Pf2DfaRPUZJpFnYOQ4guGv79rIM1L4rMWIn1qbqYLvDpJclwz4KcNZ5Ac5CmQyg1bTSgrluPxI_AJk6dEh83lTwiNIjdCeiWsrohqDuMi1inBIRqeni8XE38VV83jKgMrcu9n13ivkIEjsqH7dy6-FM-eTi9Cs7NopPSkLqazj_SeQOQtU-Zd1pmHZZWeHg5uPq-xTL7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=oeQXCPg-6hDnzJVS3B6YSm0p0ofMLcpX-6pDMUkZVvEccOI3eB_cAUcsEWQ1Aa8hA1M3PYDNZZmruLkllk2PSmQDaFgGET_G4Pw0jzel9C_tp3Xl7_Ndil7Yu40OAf_oJP0BAoVzL06o5Pf2DfaRPUZJpFnYOQ4guGv79rIM1L4rMWIn1qbqYLvDpJclwz4KcNZ5Ac5CmQyg1bTSgrluPxI_AJk6dEh83lTwiNIjdCeiWsrohqDuMi1inBIRqeni8XE38VV83jKgMrcu9n13ivkIEjsqH7dy6-FM-eTi9Cs7NopPSkLqazj_SeQOQtU-Zd1pmHZZWeHg5uPq-xTL7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: اسرائیل در شهرها و استان‌ها دست به ترور می‌زند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/148976" target="_blank">📅 17:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148975">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پزشکیان: والله دنبال سلاح اتمی نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148975" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148974">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پزشکیان: ایران نمی‌پذیرد دانش هسته‌ای دانش انحصاری چند کشور باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/148974" target="_blank">📅 17:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148973">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پزشکیان: قدرت نظامی ما برای دفاع است و از هیچکس درباره آن اجازه نخواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/148973" target="_blank">📅 17:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148972">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پزشکیان: دویست سال است که به هیچ کشوری حمله نکرده‌ایم و فقط در حال دفاع از خود هستیم؛ حال شما به ما می‌گویید تروریست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/148972" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148971">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d23473339.mp4?token=Q2JDu9zZzbkkaLYbYDwok8ouO1i1P_Oxlhxjmt_CE-w9R-h-VH_TLXjZPVoi9aD6FVrjYW4ZOBLDh2YABr8GrfJ0DN6sO9nbNS02IGeVBHyU5F1SbHY1g-1X-0ME9ZERSnonjqihKR_CF2z6SQq6iEZthwdbyfe-0O5s19Bl6OlZiK_NCqnzZN18NElzxENqFAsUTVsZvFg6zSQ0GpEfZgrdIN6Ktm4MfPu4akZYLyKJZfLvq3wDLP3FcqsHRAseB0R_sg9EgZyhSjPBzT4qdEysC-nhbiJ3A6PUkkQijZM6ZHs9qh1I4w8mzG6b-pmiy0EkMD6UogYgs448Ln-UhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d23473339.mp4?token=Q2JDu9zZzbkkaLYbYDwok8ouO1i1P_Oxlhxjmt_CE-w9R-h-VH_TLXjZPVoi9aD6FVrjYW4ZOBLDh2YABr8GrfJ0DN6sO9nbNS02IGeVBHyU5F1SbHY1g-1X-0ME9ZERSnonjqihKR_CF2z6SQq6iEZthwdbyfe-0O5s19Bl6OlZiK_NCqnzZN18NElzxENqFAsUTVsZvFg6zSQ0GpEfZgrdIN6Ktm4MfPu4akZYLyKJZfLvq3wDLP3FcqsHRAseB0R_sg9EgZyhSjPBzT4qdEysC-nhbiJ3A6PUkkQijZM6ZHs9qh1I4w8mzG6b-pmiy0EkMD6UogYgs448Ln-UhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیئت نمایندگی آمریکا در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخن می‌گفت، مجمع را ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/148971" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148970">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv2ijbW6TWDHHU8XWSq6vNLu5PKuhW1asn6qdJAKqVWfiDXTF0tbMpmceTudVo-mWlUcxVT9WHOtxlEZ_zQndetDCtGqb1Odj7ntGRd1t70sQpDPNeFQgHABH-QXeEHzC4r52-rtSwm3jZqCmTy12SMujbgLQerCCtuX3IJpJlXnm72QkTmdwMxo2G2agB7Mpr2I-Y82NTQXQme-rWDH3Dit1giFAUQM5xw9ToSpU8p5nQ6AgdfMVGbez1r1IZ8pMpzwqrZZ3jE7YjuGX4ik5Xha35MLw0Q9ihGho58mB9xvHUP2SIE2HT4mwiGMsgrwFyp51qPqnvIJJJSfVx4Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر کودکان بیگناه مدرسه میناب در دستان پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/148970" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148969">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=R0Kb8ivX3jTN9Q4r4gO_uOQOeaBqTm3Bw-RyaDOpIgnULqAKwniGkLxQWC86LidWWDCkYiC81-xAuYeRkmjqchr3ugee4yY15wRQm82rlhFTdYvjPDmmItDPFawyMJCB9z8O_g2R5EXeXP7zGcTdRe3tX_IpdM5sjgwL5soOSFabs3-ORe4cEo_7Jr3TwyQSkIrHMLle-pq5Z_PNT3F-Qcm1ZwL2bESLBEqJ8KqNYwKOGybP4KYIbxBkRl26-1XpEv_Uu82cFfRnZPN02Iav7C1owfBwlVEKZeqtxVn_mSsX3FJOQGq1oYHXpoopysbLmD4INEXo5TDVFqcj_O7c2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=R0Kb8ivX3jTN9Q4r4gO_uOQOeaBqTm3Bw-RyaDOpIgnULqAKwniGkLxQWC86LidWWDCkYiC81-xAuYeRkmjqchr3ugee4yY15wRQm82rlhFTdYvjPDmmItDPFawyMJCB9z8O_g2R5EXeXP7zGcTdRe3tX_IpdM5sjgwL5soOSFabs3-ORe4cEo_7Jr3TwyQSkIrHMLle-pq5Z_PNT3F-Qcm1ZwL2bESLBEqJ8KqNYwKOGybP4KYIbxBkRl26-1XpEv_Uu82cFfRnZPN02Iav7C1owfBwlVEKZeqtxVn_mSsX3FJOQGq1oYHXpoopysbLmD4INEXo5TDVFqcj_O7c2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نشان دادن تصویر علی خامنه‌ای توسط پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/148969" target="_blank">📅 17:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148968">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پزشکیان در سازمان ملل:
ما قربانی تروریسم هستیم من از ایرانی می‌آیم که رهبر ما را بدون هیچ دلیلی ترور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/148968" target="_blank">📅 17:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148967">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrH4EOasXBCOoCaQNfckWMrtLdEh2YxsM7GCUWWX7QvrUotgIWLL7xASXVcmt1jZCsIkjE1WOYpK8AOoCPDuvLiyqE1YtnnMAzXskJ_Za8aeatWRaMgK-_6qhEHYSM1ZcOXbePAkP-qTsaggooa4kmzy678fe5WDKAuo7dLF5nYvzCNA-7RGqXPS8616qCL9RDDbi8ihZbxPwCay-eFaSOSdFpeBgIHqfvBZXyzZ9n9CVbborsUdq-H_YMkq1n8kdOuQe1IluI4qR_RHowpo1Zsy5QoBm2f6N6GwcDU5JVwaxv951SDJd9WJFBCl9-UkDtcbCajXafsiBxFlaHZFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیس پزشکیان توی سازمان ملل قبل سخنرانیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/148967" target="_blank">📅 17:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148966">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKQDhqUxfHH_9L-9yBhJArYCwlPuGbojlFDDFBCcBx0O7AkjIq7FJk05NenEbmekUCdMJklnvQPQBVHBjCm38F4V2ubDCeu3cLbrThMCed-4uASmyGcm8qRFeLD_rm56OQzLVJO8Z00Qr8U2rVLDwe1AZaXS54bDd8qDU18cSTzOcdUfeHHjZ96DxkWAqlgpbqj_OPNbNIJ8fi67GmEsNTOUZkZ4P67IyKLfSchSOZziZUUceIUQBjzzp5hIika7yDjrcLJx2SKWCHCsCJ377AU9QPXpHZ3O6Kgf8dosBzTYHtub0UQxK3MBWlsoU0H213FKdV85k5fUPoUktZHOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی:
ممکن است ترامپ به کوهی در ایران یا سایت‌های هسته‌ای ما حمله کند؛ ما طرح پاسخ را آماده کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/148966" target="_blank">📅 17:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148965">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پزشکیان وارد سازمان ملل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/148965" target="_blank">📅 17:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148964">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
هشدار فیلدمارشال رضایی به ترامپ: وقت را تلف نکن و شروط ما را بپذیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/148964" target="_blank">📅 17:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148963">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d21bb84f.mp4?token=To7LAn4XYHJ112ZwZV-vHh5PbK8V9HQw4p23j_MGlwYr_BkGP_Lzt1AMgRh6uJcKW6ofy_qGheKDfFXuJxFvYqehBXIx3FlioIYPtkbPMxudsR4II63Cci5vXAAQgW3ZbKM4x8rmK7YHVRXkfafUzhJUZqUAyoGHgfIlOKRSbruZf1eLc70_L3jgTQMrZDK_iE1XUOpSIHLNzELMv96995VzCPgVos33XXhbhSfBALm1GSYTtA3jcQoBSp46jgdnVnYhL5XGg1ZaqqXoSzyhJKZzOD4GPN30A3Ey-ZT-xpxwQx3X_nuODOTgBCPzo7vwCL2RUyi_bMWmnWrtmnNqOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d21bb84f.mp4?token=To7LAn4XYHJ112ZwZV-vHh5PbK8V9HQw4p23j_MGlwYr_BkGP_Lzt1AMgRh6uJcKW6ofy_qGheKDfFXuJxFvYqehBXIx3FlioIYPtkbPMxudsR4II63Cci5vXAAQgW3ZbKM4x8rmK7YHVRXkfafUzhJUZqUAyoGHgfIlOKRSbruZf1eLc70_L3jgTQMrZDK_iE1XUOpSIHLNzELMv96995VzCPgVos33XXhbhSfBALm1GSYTtA3jcQoBSp46jgdnVnYhL5XGg1ZaqqXoSzyhJKZzOD4GPN30A3Ey-ZT-xpxwQx3X_nuODOTgBCPzo7vwCL2RUyi_bMWmnWrtmnNqOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دانیال عیوضی از بازداشتی های دی ماه که مجروح شده و از طریق ترکیه خودشو به فرانسه و سپس آمریکا رسوند تو صحن سازمان ملل در مقابل نماینده های جمهوری اسلامی بدین شکل سخنرانی کرد : تو دی ماه مردم خیابون‌هارو از جمعیت پر کرده بودن، اما با گلوله به مردم حمله کردن، ده‌ها هزار نفر به قتل رسیدن، مردم ایران هیچ مشکلی با بقیه کشورها و آمریکا و اسرائیل ندارن، ولی جمهوری اسلامی ایرانیارو بدبخت کرده، به محض اینکه دانیال اسم رضا پهلوی رو به عنوان رهبر دوران گذار آورد، هیئت ایرانی اعتراض کرد که خلاف قوانین جلسه هست، اما رئیس جلسه گفت حرفای دانیال هیچ مشکلی نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/148963" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148962">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
محسن رضایی: در جلسه مشترک با رئیس جمهور قرار شد آقای عراقچی طی سفر به نیویورک شروط ایران را به واسطه‌ها ابلاغ کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/148962" target="_blank">📅 17:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148961">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ادعای محسن رضایی: برای اولین بار موشک ضدناوشکن روی ناوهواپیمابر جورج واشنگتن منفجر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148961" target="_blank">📅 17:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148960">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ادعای محسن رضایی: برای اولین بار موشک ضدناوشکن روی ناوهواپیمابر جورج واشنگتن منفجر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/148960" target="_blank">📅 17:10 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
