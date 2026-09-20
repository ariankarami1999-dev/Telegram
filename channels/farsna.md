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
<img src="https://cdn4.telesco.pe/file/JSP0A1E8GkF8kgJUtifiL_10rbXFLkpqqGxrcC1NsshkjwlhXt5CsdIWcvhA2qnSUknBVgSIdcHB_cx78QF9ZAoV-SRLtMSc0w1ttdlyT9Qi92n_QJinReWIIx3MU2YW7IxlVAE8A0IfE47RRlsfYbuE1b5AfYdHvZ4H1LmcsO1pagbRp6ueJDIwfFHLgkGgqyW751GDWeGzYBaCHkyQDhjq_clVQ2MJb_42hmqO8D6kwMGMDVPvQBBqdDJ9gnSgA2Ro9cnOsHZE07jMFFiiei03pYHF-yW6J_VmzxodrngQXnQmGTKFPV9OAhnTrq-DkVud8bmH60ZuO6zvtHPnBQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 23:31:04</div>
<hr>

<div class="tg-post" id="msg-463284">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXCsDAaXcu1M2ney__J9lPYm0L_maVYba8LTNfpTJF-eBjUSr7H0IwFswIEm_gmB0ek-Ujk-AFXGpozNe4zC0SkTj1HmRW3jaI1DMQQLZeeI1vmHvLBZ3GVmdd_1vS_-jBp1MSWzaL-Zz4gUT7NBzB9PgnpNKsvDgqPKVww42PbbYhIzaVEPHup3IbTujXvbgkP0sPE3pIXmRceqzfEuDgPQT4U5YvtLph1-VYDPpo1GaRx4WY8ROHiBWvbhqIAG3SQzF1UcARLtmI-Gw49Pz8wT02Z5mp-6bFlbEug4ig1g1nYBGgTqG7x5PzpHf7dGZnnvFGH4M62__0VmQTvNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز ما چگونه تمیز می‌شود؟
🔹
شاید تصور کنیم تمیزکاری فقط مربوط به خانه، لباس یا وسایلی است که در طول روز استفاده می‌کنیم اما مغز ما هم به نوعی نیاز به پاک‌سازی دارد.
🔹
در طول روز فعالیت سلول‌های مغزی باعث تولید مواد زائدی می‌شود که باید از محیط مغز خارج شوند. بخش مهمی از این فرایند پاکسازی در زمان خواب، به‌ویژه در خواب عمیق، انجام می‌شود.
🔹
پروفسور ندرگارد کشف کرد که یک سری سلول به اسم گلیا در مغز وجود دارد که کار پاکسازی و تمیزکاری را در مغز انجام می‌دهند دقیقا شبیه کاری که سیستم لنف در بقیه قسمت‌های بدن انجام می‌دهد.
🔹
او اسم این سیستم تمیزکاری را گلیمفاتیک گذاشت بر وزن لنفاتیک. این کشف باعث شد به یافته‌های بسیار مهمی در مورد آلزایمر دست پیدا شود.
🔗
اما مغز دقیقاً چه زمانی و چگونه خودش را تمیز می‌کند؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/farsna/463284" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463283">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11908925a5.mp4?token=g3o5VzL26IqRLfFcyYyGnCSmWuRIYH_yJcdVwQTkpHhExzAWRINwo1Nx63QZe0Uz0ehnER1dhpgyX0i9Pl8RECL3O3FM6YTRkR6LXQP3vPuSCGkhEd15bmh1O05Qg-En7N3sQwTg78GJtx7XkZ7UacvbuRUYE5yfyquM9Zzs07N8CGUKh6uI1pWMkt6HWtbi0hjd9my7VlHFDHJTKw0W55ODQ8Wb8O8BYr64_-BsgTzq4ub6IvHEf6Y69hsG6klVfhYUz9Xi0xvXH085qZ0UznzuTHdl0hE2Kqi3g3qXUgzSjsEFrivOFLEyUj5fBizOR2d6RjXPb6I_YBVOX1xuB3I1Et4g_1FnD5IWZPp-vCCBO7q01qZO3xqYzMc66tMXzfWB_OYcXsBuHq9x4aHMF-o6f2FtQJUG6xJwJkF5mPtxy78oIELd_ZhmAD8-W9GNl7B9LUrw8Kmst_Ct98iIt4ageACcjOaSP5vWzHbRoIGICCd5siFe-79wMgiBVNxD4PP5YiPudlSokBktpbAPprH-DoZR29HVPmYOVsGVFf05yLt6MdS-iKqkyZIZ-DpL8d9rQ44Wj6OprPYHpEUyncudtqPPCRsk7fsTynFSlXVLvX9uI0gJ-VxG7Ha8WGxIw5uzif3x38VOSJh-uHpqVwPTaa-w64SIRiHhk0hxqH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11908925a5.mp4?token=g3o5VzL26IqRLfFcyYyGnCSmWuRIYH_yJcdVwQTkpHhExzAWRINwo1Nx63QZe0Uz0ehnER1dhpgyX0i9Pl8RECL3O3FM6YTRkR6LXQP3vPuSCGkhEd15bmh1O05Qg-En7N3sQwTg78GJtx7XkZ7UacvbuRUYE5yfyquM9Zzs07N8CGUKh6uI1pWMkt6HWtbi0hjd9my7VlHFDHJTKw0W55ODQ8Wb8O8BYr64_-BsgTzq4ub6IvHEf6Y69hsG6klVfhYUz9Xi0xvXH085qZ0UznzuTHdl0hE2Kqi3g3qXUgzSjsEFrivOFLEyUj5fBizOR2d6RjXPb6I_YBVOX1xuB3I1Et4g_1FnD5IWZPp-vCCBO7q01qZO3xqYzMc66tMXzfWB_OYcXsBuHq9x4aHMF-o6f2FtQJUG6xJwJkF5mPtxy78oIELd_ZhmAD8-W9GNl7B9LUrw8Kmst_Ct98iIt4ageACcjOaSP5vWzHbRoIGICCd5siFe-79wMgiBVNxD4PP5YiPudlSokBktpbAPprH-DoZR29HVPmYOVsGVFf05yLt6MdS-iKqkyZIZ-DpL8d9rQ44Wj6OprPYHpEUyncudtqPPCRsk7fsTynFSlXVLvX9uI0gJ-VxG7Ha8WGxIw5uzif3x38VOSJh-uHpqVwPTaa-w64SIRiHhk0hxqH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۲۰۴ مردم کرمان برای دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farsna/463283" target="_blank">📅 23:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463282">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23196aff17.mp4?token=m-Fj9IOz87zrXw5ySkv3A1S5VWU50KWZLodo7qXzloznbMvZFOgLReVJzIYx3C4TyGNHg6gbPt6xHLgbMHZ0qq61TzUxyQl8-HCB32118n4CZS-fiKSjOwKGk3VKzCF6A_MPXI4dA38mkLL_0qmZCYu6eQa9D8eX-Y45pfYcY9Jobj7voKoqnJFWNfpTPGld-rRoImC33FZ7_t_4ST8Df00CbchWx5QxzXZ1sstcva_JiXTi4pgrNBScf6cchEXM9x4G91DudzzV6-qbxYCDzvZLvmf8zoOyQMCYndF6BHV8NQ26Q7sTupN6DRZXESBUpIsTl6iwnI3xedmZYjLKBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23196aff17.mp4?token=m-Fj9IOz87zrXw5ySkv3A1S5VWU50KWZLodo7qXzloznbMvZFOgLReVJzIYx3C4TyGNHg6gbPt6xHLgbMHZ0qq61TzUxyQl8-HCB32118n4CZS-fiKSjOwKGk3VKzCF6A_MPXI4dA38mkLL_0qmZCYu6eQa9D8eX-Y45pfYcY9Jobj7voKoqnJFWNfpTPGld-rRoImC33FZ7_t_4ST8Df00CbchWx5QxzXZ1sstcva_JiXTi4pgrNBScf6cchEXM9x4G91DudzzV6-qbxYCDzvZLvmf8zoOyQMCYndF6BHV8NQ26Q7sTupN6DRZXESBUpIsTl6iwnI3xedmZYjLKBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همدانی‌ها در شب ۲۰۴ همچنان پای قرار ایستادند
@Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/463282" target="_blank">📅 22:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463281">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8bfd542c.mp4?token=s79fI_YMltCIyM-DNqUUsToh_UtJWw3bAyk4OsPynqlWzJaFUnRGxCjInjCsimUkIisiUziqWFVmKPS4L9pBbVi22iD78GyxoM4u90cosrxS1iMx-pyCrsn3ewymM9vcoKXstYOeVufMdgu3bczSBBeO-qzmFjPcdbNM2Lc23TTY6oTE5ouaWYK6_PLjNcEI5PhFIOSQo9WqDcMA7X_nnfFF7dKfWqVzibp9MPjArOpial959uoOADKfVcvSnT7T9ZwYZ0dgqNLY6S2DEReSe0l63noZZv5uZYzD9-EoDj1vAY6w9pw8pkq8x0fnxwsaj_een6ReVS4M3HnXAwgIZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8bfd542c.mp4?token=s79fI_YMltCIyM-DNqUUsToh_UtJWw3bAyk4OsPynqlWzJaFUnRGxCjInjCsimUkIisiUziqWFVmKPS4L9pBbVi22iD78GyxoM4u90cosrxS1iMx-pyCrsn3ewymM9vcoKXstYOeVufMdgu3bczSBBeO-qzmFjPcdbNM2Lc23TTY6oTE5ouaWYK6_PLjNcEI5PhFIOSQo9WqDcMA7X_nnfFF7dKfWqVzibp9MPjArOpial959uoOADKfVcvSnT7T9ZwYZ0dgqNLY6S2DEReSe0l63noZZv5uZYzD9-EoDj1vAY6w9pw8pkq8x0fnxwsaj_een6ReVS4M3HnXAwgIZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله عاملی: همهٔ محاسبات می‌گفت شکست قطعی است، اما تاریخ نشان داده وقتی خدا با کسی باشد، معادلات تغییر می‌کند
🔹
روایتی از روزهای پیروزی انقلاب اسلامی؛ «همه چیز با ما بود، فقط خدا با خمینی بود»
@Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/463281" target="_blank">📅 22:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463280">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f823bb53f.mp4?token=UIuGC28rNlelG0JtA3s8mbgot9fQ0KHAwsQAa4VZOrl9GiBqxQDqC7MLRYuDKkyhCj6gmAOOqcUbguDnhb2Dx-GRDr0m2N9xKIQoBT_6LWpLLhZ_pFf55_7Ha-OoFY1LSWozfYR_zRRRUq-izNddI6PC_uYuZmT2Vgil-P2X32Ix8_5aksKVzb-nGkmzD-EKj3Z5-W9b4j0FwyoTClmtNYgvL9qt8PRzT7gVR6ObzC1b1CITr9eoHr1P6fzXwGzryVrD9OnZFg_5fQSRo4glYCRsqFD3mHQow8qflekCpNJ70qdacpcGSWf8d5ilWL0Fsxr_Py_4giYRhbcfkBW_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f823bb53f.mp4?token=UIuGC28rNlelG0JtA3s8mbgot9fQ0KHAwsQAa4VZOrl9GiBqxQDqC7MLRYuDKkyhCj6gmAOOqcUbguDnhb2Dx-GRDr0m2N9xKIQoBT_6LWpLLhZ_pFf55_7Ha-OoFY1LSWozfYR_zRRRUq-izNddI6PC_uYuZmT2Vgil-P2X32Ix8_5aksKVzb-nGkmzD-EKj3Z5-W9b4j0FwyoTClmtNYgvL9qt8PRzT7gVR6ObzC1b1CITr9eoHr1P6fzXwGzryVrD9OnZFg_5fQSRo4glYCRsqFD3mHQow8qflekCpNJ70qdacpcGSWf8d5ilWL0Fsxr_Py_4giYRhbcfkBW_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعاً مدارس حضوری خواهد بود
🔹
ما تمام برنامه‌ریزی‌های لازم را برای حضوری‌شدن کامل مدارس انجام داده‌ایم.
🔹
اگر اتفاقی در نقاطی از کشور رخ بدهد، اختیاراتی به استانداران می‌دهیم و استانداران متناسب با آن شرایط، به‌صورت نقطه‌ای تصمیم‌گیری می‌کنند.…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/463280" target="_blank">📅 22:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463279">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYh4c63TzIMs5T8wKJRNkkjb9DCAY-q-rEWKTi6gm_kRfpOZbcZOf5nu_OaRBMLA3-RFmfNrDmUEdpX1V0kyJc00Bk8gB5Wgf7gX_X2oeqXSk2kMSxLqE5f_w-a4am0VbHznUr455EieE3nM6npEcHWOmho3QWZx7RsD4sjU2rjiVCQlTM-WZwzF33GtQXqizcID1Pvrc5ILaDqy8gvFOyXmrfUqIH8jxBBEMOn7El8ReQBrLQJEhoQGE0rFo3gVbhe3Uu62ouyN139931n3KIG4f6oYiuf2T2YEJc6MH6ez7-VSw6dZOJaLUYowOjBtRbO6CkVncwJVyKj2MFmwSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشاورزی به ازبکستان رفت
🔹
نوری، وزیر کشاورزی در راس هیئتی از تجار و بازرگانان با هدف افزایش روابط اقتصادی به تاشکند سفر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/463279" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463278">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e283b14cd.mp4?token=abyfcxUljSXgbibntyjIZCf72iieixdvSx8FmtOSPKbl84ySmzQ2GKPJ7gmlAfmMr9o1jwF-s_VK9MpsXSb8zjP8dFEySMZ9SAb7F6W-xm-dV6fl6iou5YKImz001P4iRbhM63VWvbz31P3oIOBsRvpuW_RS-RsbmJNPZTtMF7ZIUcSNrRzFeTyb1j5_297Tj74P9iXKYs1LnKItrWBaPyqDf9pdn0jpLWdltUCyZdWPrv4vZy2fXe0gwm_FKaelt3jBNPTG8MZmSJs7W2rL5ymrTLKI8kKmCEqKShV26g42x_db0tqaxFYPEVvUozwrVp6G1zhZKUF7pKKqe_QUxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e283b14cd.mp4?token=abyfcxUljSXgbibntyjIZCf72iieixdvSx8FmtOSPKbl84ySmzQ2GKPJ7gmlAfmMr9o1jwF-s_VK9MpsXSb8zjP8dFEySMZ9SAb7F6W-xm-dV6fl6iou5YKImz001P4iRbhM63VWvbz31P3oIOBsRvpuW_RS-RsbmJNPZTtMF7ZIUcSNrRzFeTyb1j5_297Tj74P9iXKYs1LnKItrWBaPyqDf9pdn0jpLWdltUCyZdWPrv4vZy2fXe0gwm_FKaelt3jBNPTG8MZmSJs7W2rL5ymrTLKI8kKmCEqKShV26g42x_db0tqaxFYPEVvUozwrVp6G1zhZKUF7pKKqe_QUxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احساسی شدن شرکت‌کنندهٔ برنامهٔ سرآشپز شبکه ۳ به یاد مادرش
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/463278" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463277">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b95879771.mp4?token=cVPSka-g2MGpVIRgf36ulKgKKq2LO4jF_fCcs0GGgxAB1ivSVOn2HD2DbQ1GoZfLIwTB1yha2py_7NU1PeXx22bcDw_Vrl1AfnnkVhoEmdol_yJsQCPxmTKC8cEp2k9DvIODHP94wlCFH4tJ00msNPlKAOwS8VZNINsiIGnHJU5wZNg6Cc4ILZGVaYKS2SQsJudCIsEUtlZ07jXGRmLl09dStk2SBz4EtgspMEpFdiKqxTRzcHWt6OujNSa_GEqFUrgg8yTDa_HrD-T2LJCCk-vUjB5A6ugf6nsgI28FjnSEBWHAqPBCtL8j5Ts3vSY0MYw5SA4BMJog4_QKt4rDlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b95879771.mp4?token=cVPSka-g2MGpVIRgf36ulKgKKq2LO4jF_fCcs0GGgxAB1ivSVOn2HD2DbQ1GoZfLIwTB1yha2py_7NU1PeXx22bcDw_Vrl1AfnnkVhoEmdol_yJsQCPxmTKC8cEp2k9DvIODHP94wlCFH4tJ00msNPlKAOwS8VZNINsiIGnHJU5wZNg6Cc4ILZGVaYKS2SQsJudCIsEUtlZ07jXGRmLl09dStk2SBz4EtgspMEpFdiKqxTRzcHWt6OujNSa_GEqFUrgg8yTDa_HrD-T2LJCCk-vUjB5A6ugf6nsgI28FjnSEBWHAqPBCtL8j5Ts3vSY0MYw5SA4BMJog4_QKt4rDlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعاً مدارس حضوری خواهد بود
🔹
ما تمام برنامه‌ریزی‌های لازم را برای حضوری‌شدن کامل مدارس انجام داده‌ایم.
🔹
اگر اتفاقی در نقاطی از کشور رخ بدهد، اختیاراتی به استانداران می‌دهیم و استانداران متناسب با آن شرایط، به‌صورت نقطه‌ای تصمیم‌گیری می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/463277" target="_blank">📅 22:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463276">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60af7456ed.mp4?token=c7un2vRaswGH0JKKhqhrHJe20N4LVDWEdmOQJq0xAl8Pm07BtpNPOnm3UZjJtJpCAFr-5MOiGYXkzcFpu5XPEsBzYLUdPGhpYkIaj4T9NyrIJXHset8LExmP7V7EOwM5xOkItVd7XEcQbEZQZy4lRCabdQnT9HCy0SybOD08CWvVvAozBB_yWs7i4TVKXLsFiXieTqup43tl9qbM3Uqazz-HYosj46MI6UD9zGnvYWiWdbT-n1PtqQ8Q_fZ0QMBrOzdenNc6pdNfyXS8pfIWgQbP9-Nf3ZbXt-nFaxx1NJ7u4BlwyvMS8f3eMjRfwki3pfqXI5xitQVZFnNIdbb5AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60af7456ed.mp4?token=c7un2vRaswGH0JKKhqhrHJe20N4LVDWEdmOQJq0xAl8Pm07BtpNPOnm3UZjJtJpCAFr-5MOiGYXkzcFpu5XPEsBzYLUdPGhpYkIaj4T9NyrIJXHset8LExmP7V7EOwM5xOkItVd7XEcQbEZQZy4lRCabdQnT9HCy0SybOD08CWvVvAozBB_yWs7i4TVKXLsFiXieTqup43tl9qbM3Uqazz-HYosj46MI6UD9zGnvYWiWdbT-n1PtqQ8Q_fZ0QMBrOzdenNc6pdNfyXS8pfIWgQbP9-Nf3ZbXt-nFaxx1NJ7u4BlwyvMS8f3eMjRfwki3pfqXI5xitQVZFnNIdbb5AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۴ شب قرار عاشقانه؛ گنابادی‌ها همچنان پای وطن ایستادند
@Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/463276" target="_blank">📅 22:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463275">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBD4Luc5MXiZi0qSaL8IDbX5AuXlRf3YOoMumC8xUoEHGIDnI1biYHttdoc-EuDjXSIjCI3lzcSzChBmMQ5KnzI6hmAFsmEbb6whlZouQvGCkWGweUK8AcQ8YgriQWCUrH7qX1e2RKngX76DFua9pS6fLxvSocDodwkGbYcz0bpTiU35K_JcQ8AwFSftwxdJ_Nr0cBuwwGvmojFPX89qSXBVpwBU6C0wOe--uSB-T18ys1nm8AIXU72S-Qmenj95OCBoyU8A6FlneWO6tfzXAVY1cgBojmMY1MZKi3xkLOhwxRAJKcVVhYGgVSQiqqUN06oG_XfxvWpQZxyYa0Kt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی برای شرکت در اجلاس سازمان ملل عازم نیویورک شد
🔹
وزیر خارجه در مسیر سفر به نیویورک توقف کوتاهی در دوحه دارد و دربارۀ آخرین تحولات منطقه رایزنی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/463275" target="_blank">📅 22:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463274">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
برای درمان دندان به دندانپزشکی مراجعه کردم؛ هزینه یک عکس ۳۵۰ هزار تومان، کشیدن دندان ۳ میلیون تومان و کشیدن با جراحی ۵ میلیون تومان اعلام شد. با این هزینه‌های سنگین،
بسیاری از مردم توان پرداخت هزینه‌های درمان دندان را ندارند
.
🔹
پس از بیش از سه دهه خدمت، بازنشستگی برای ما به‌جای آرامش، به دغدغه‌ای دائمی برای تأمین ابتدایی‌ترین نیازهای زندگی تبدیل شده است. با وجود سال‌ها خدمت صادقانه، امروز پرداخت اجاره مسکن، هزینه تحصیل فرزندان، مخارج روزمره و هزینه‌های درمان به دغدغه‌ای سنگین تبدیل شده است. ما انتظار زندگی تجملاتی نداریم؛ تنها می‌خواهیم حاصل سال‌ها خدمت، کفاف یک زندگی آبرومندانه را بدهد. از
مسئولان محترم صندوق بازنشستگی کشوری
، سازمان تعاون روستایی و سایر مسئولان مربوطه تقاضا داریم
صدای بازنشستگان را بشنوند
و برای رفع مشکلات معیشتی آنان اقدامی جدی و فوری انجام دهند.
🔹
لطفاً پیگیری کنید چرا
به برخی خودروهای نو شماره
، از جمله خودرویی که با زحمت و حقوق کارمندی خریداری کرده‌ایم،
بنزین یارانه‌ای تعلق نمی‌گیرد و مجبوریم
بنزین با نرخ ۱۰ هزار تومان
تهیه کنیم؟
🔹
لطفا پیگیر
دهک‌بندی‌های غیر عادلانه
باشید. من مستأجرم با یک ماشین ساینا با درآمد کم چرا باید دهک نه باشم؟
🔹
عوارض برخی آزادراه‌های کشور
به‌صورت دوربینی و با ثبت پلاک دریافت می‌شود و راننده باید ظرف هفت روز آن را پرداخت کند؛ در غیر این صورت به‌دلیل تأخیر چندین بار جریمه می‌شود. اولاً همه مردم از این قانون و مهلت پرداخت اطلاع ندارند چرا اطلاع‌رسانی درست و کافی انجام نمی‌شود؟ ثانیاً همه مردم سواد یا امکان پرداخت آنلاین ندارند، اما بدهی آن‌ها روزبه‌روز بیشتر می‌شود. ثالثاً بسیاری از افرادی که نحوه پرداخت را می‌دانند، پیامک‌های تبلیغاتی را در تلفن همراه خود مسدود کرده‌اند و در نتیجه
پیامک‌های هشدار پرداخت عوارض نیز به دستشان نمی‌رسد و مرتب جریمه می‌شوند
. حقیقتاً این شیوه درآمدزایی منصفانه نیست. فردی ممکن است هنگام فروش خودرو تازه متوجه شود مبلغ عجیب‌وغریبی بابت عوارض جاده‌ای بدهکار است.
🔹
در ارتباط با
سهمیۀ سوم سوخت در استان‌های کرمان و سیستان‌وبلوچستان
سؤال و مطالبه‌ای داریم. مسئولان آیا متوجه نیستند که مردم این استان‌ها به ‌دلیل مسافت‌های طولانی بین شهرهای مختلف و مرکز استان یا سایر استان‌ها، برای مراجعه به پزشک و انجام امور ضروری به مشقت می‌افتیم؟
با این مقدار سهمیه بنزین، نیاز مردم برطرف نمی‌شود
. مشهد که رفتیم در هیچ‌کدام از جایگاه‌ها به ما بنزین ندادند و با مشکل جدی مواجه شدیم. این سؤال هم برای مردم مطرح است که چرا باید با وجود چنین شرایطی، سهمیه سوخت این استان‌ها محدود باشد؟ آیا استاندار و مسئولان استانی واقعاً از مشکلات مردم در این زمینه اطلاع دارند؟
🔹
بنده نیروی رسمی آموزش‌وپرورش با ۱۳ سال سابقه خدمت هستم. یک سرباز معلم پس از دو سال حضور در آموزش و پرورش، کارت پایان خدمت خود را دریافت می‌کند، اما ما
نیروهای رسمی آموزش و پرورش
با وجود ۱۳ سال سابقه خدمت، هنوز
کارت پایان خدمت
‌مان صادر نشده است.
🔹
چطور واسطه‌ها خرمای کشاورزان را نمی‌خرند و بهانه می‌آورند که خریدار نیست، اما همین خرما وقتی به دست مصرف‌کننده می‌رسد با قیمت بالایی عرضه می‌شود؟ منِ مصرف‌کننده به‌دلیل گرانی خرما توان خرید ندارم. اگر واسطه‌ها خرما را از کشاورز با قیمت پایین خریداری می‌کنند، چرا محصول را با قیمت مناسب به مصرف‌کننده عرضه نمی‌کنند تا فروش بیشتری داشته باشد؟ آیا این انصاف است که زیاده‌خواهی واسطه‌ها هم کشاورز و هم مصرف‌کننده ضرر کنند به خاطر!
🔹
در شهرستان ورزقان استان آذربایجان‌شرقی و در مجموعه
معدن مس سونگون
، متأسفانه در شرکت‌های تابعه،
جذب و به‌کارگیری نیروی انسانی
بر اساس سفارش و روابط انجام می‌شود و این موضوع موجب ایجاد تبعیض و احساس بی‌عدالتی در میان بخشی از مردم منطقه شده است.
مردم بومی این منطقه
انتظار دارند فرصت‌های شغلی مجموعه سونگون به‌صورت شفاف و عادلانه در اختیار نیروهای واجد شرایط قرار گیرد.
🔹
من
راننده تاکسی
هستم. سهمیه بنزین ۳ هزار تومانی ما ابتدا ۴۵۰ لیتر بود بعد به ۲۲۸ لیتر کاهش پیدا کرد و پس از گرانی بنزین، سهمیه را به ۱۰۰ لیتر رساندند که همین امروز تمام شد. با توجه به اینکه تاکسی وسیله امرار معاش ماست،
این میزان سهمیه پاسخگوی نیاز رانندگان نیست
و هزینه سوخت فشار زیادی به ما وارد می‌کند.
شهرداری و تاکسیرانی
نیز تاکنون اقدامی برای حل این مشکل انجام نداده‌اند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/463274" target="_blank">📅 22:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463273">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b65d69a311.mp4?token=ElPz2BmJwSW8T2tRBMgxUUlqpZ-EmhAP32k8PTXP4Mdk0v2pv2m1MDqNgqpQU87igPiDZ-iN-9l2L0cx1YA18RZgGg3nNWu-Da-GBb-u3M-LM6-wg0rfd3ROqGwd1kb8AvIdvSmbTlnt52uo2KMV7GX_vWQxzb-RQfC5uFXT6Kml_SuHpQHTjIkkQ8hFZ-cJh_XmplYH-CPhdkRGoa48NPoxaknU0R_YbP56UQ-lAVWNxAzUJflYuMVAa7HUYtP_MIi9cw9aFdeTa7iQbRYyRvQT0nGZDObLVm2FA7EOVEg_hKIpyaEdpozwQ9cIzXFeN-QkRkEt0bKYGESg6k63zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b65d69a311.mp4?token=ElPz2BmJwSW8T2tRBMgxUUlqpZ-EmhAP32k8PTXP4Mdk0v2pv2m1MDqNgqpQU87igPiDZ-iN-9l2L0cx1YA18RZgGg3nNWu-Da-GBb-u3M-LM6-wg0rfd3ROqGwd1kb8AvIdvSmbTlnt52uo2KMV7GX_vWQxzb-RQfC5uFXT6Kml_SuHpQHTjIkkQ8hFZ-cJh_XmplYH-CPhdkRGoa48NPoxaknU0R_YbP56UQ-lAVWNxAzUJflYuMVAa7HUYtP_MIi9cw9aFdeTa7iQbRYyRvQT0nGZDObLVm2FA7EOVEg_hKIpyaEdpozwQ9cIzXFeN-QkRkEt0bKYGESg6k63zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از شب اول تا شب ۲۰۴؛ مردم هنوز در میدان‌اند
@Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/463273" target="_blank">📅 21:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463272">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320d035b7f.mp4?token=hM2HsAEYff2WWSnxdK47JwZjCZsQRUbmxZFoHjCP1omekzrMl5kda5TYUCe-XfBJoCdr82YsjrM9-hoz6pCsvrV8vqWsn7YBikVpKZpZscS1ok_oNl2nFUjVMxpedBlG-JgfI9UWZXp9t4jhofYyI-rIMdTkVum3h1mg-Snh2vs6N-FSyn1nQhXkSxjz2KzRmLQ_q0SBZleGnHblk-hmcf13Byj8HB0W9_Psfie4P7T3hjVu2F9yisg8NdzV02uz74mLziI4RIHyo-GU_ePr5Iqlr-N9SNPEt80w-X0JUr40Ve3S0sHCOoUsiUVW-gwUmsJFHLsFhMJykSzGn_CuuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320d035b7f.mp4?token=hM2HsAEYff2WWSnxdK47JwZjCZsQRUbmxZFoHjCP1omekzrMl5kda5TYUCe-XfBJoCdr82YsjrM9-hoz6pCsvrV8vqWsn7YBikVpKZpZscS1ok_oNl2nFUjVMxpedBlG-JgfI9UWZXp9t4jhofYyI-rIMdTkVum3h1mg-Snh2vs6N-FSyn1nQhXkSxjz2KzRmLQ_q0SBZleGnHblk-hmcf13Byj8HB0W9_Psfie4P7T3hjVu2F9yisg8NdzV02uz74mLziI4RIHyo-GU_ePr5Iqlr-N9SNPEt80w-X0JUr40Ve3S0sHCOoUsiUVW-gwUmsJFHLsFhMJykSzGn_CuuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ا
گر قرائی اسرائیلی بود بعد از ونیز سلب تابعیت می‌شد!
@Farsnart</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/463272" target="_blank">📅 21:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463269">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ti-wxrY5NfdVY_3QiQ45Glnq-b36CEeTYAcGwt6aeelKGEr9a-7hRgL14b-__-YBomRv946d29JxHsCPEMgYyzwJZtDEtNrV4uzVo1AMpdFgfwumC6PbeElrxBOjxTN_VS8XgU7TKBx8ZSODcZJRbUyS0NbkOEpJZ8dKYvJ9DUj9chJBrvl2ldE6QibaCutvADkNnBxge5aVrQRDEgQiZNee4NfEhAJzt1xFxYIaD6yvSfUEajtjXFXE8Ff6WIqh-V_SN5xifcD_op64IK2B36ma05rWABxU2jy3P2qFAO6anY0NmiHjfQpT-MREPjJQKj2D4aG_wT-is8RYxe9PGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPXj0EtnEGziS4mxJCU5RzQWb2dGsFyLk9bAOtAuexA0zteeRczXEPGPZvfnMcnq668Nw6Icb-gGLWl_y0ir21dbLhSCHz9DX1FYOixLw-1CE1vrEM6KUbKOdBJZw-wvnmIQFRZCpCK1gXCTRkc_rVr0uFWjqND3iZrjDUVsEF7v0Wvl2Mr3HyBc_YkaJX2yne3IaPYmuUFokbeUbQaw1waQlc_F48DpxyBLcBe5xzJ4cCm5qMTT7tzxpZhzNmN2J2o0zRbPI3COXPsudDwxohhWG2tjYIew01I4Xaj5EN8UykVWpOc2X6nO8zREYp_IqawmkoGHI3KSn63O7yEgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhMqk-7EYhaE_5RQFS935E0y_CcFGqMBaMr_HL5WdZrskk5axr82cNP2cHNA-NUD-nTF5BTyhh9mxKo8CGb0UgOVTx4AoqgwYvAjshtPnPfgFFPEjPCcKEKF1K9By66-OjreJtsE4c3D6ELhMQIpy7Hcj7nnLpC3i42jszllBZf39UsRRbI8JlapWL8WaZPQ2ObMwud12cHZo_zftT-Z6MvvLNgyXxvbF48konDucNL0T9kz5oTABvP2_FRn0MIIPJyDAK7lTJifHRpEOczgqGA6fSQc0gPQiVFMlqMNhON_-FV35EmYaPSQKeaUR-TyupQgVKIBXZ53MRnE6VGlPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نخستین تصاویر از ۱۷ اتوبوس آسیب دیده از حمله آمریکایی‌ها
🔹
سخنگوی شهرداری تهران: آمریکا با تعرض به کشتی حامل اتوبوس‌های دوکابین شهرداری تهران، به ۱۷ دستگاه آسیب جدی زد؛ اتوبوس‌هایی که برای خدمت به مردم در ناوگان حمل‌ونقل عمومی پایتخت عازم ایران بودند.
🔹
۳۱ دستگاه دیگر از محاصره عبور کرده و در گمرک منتظر ترخیص و انتقال به تهران‌اند.
🔹
جنایتکاران آمریکایی با زندگی روزمره مردم ایران در جنگند؛ این خباثت‌ها عزم ما را برای خدمت بیشتر، راسخ‌تر می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/463269" target="_blank">📅 21:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45062f4ecb.mp4?token=MK-blKzvPxZfttkXKLG6iSHmhwILwA55SxIBskZpHabyMMqe7LFRcgE7ZwokuNYzFWMpfUI0ymDxcu9e4DyGyqjQv_9IaCJ8UUjNT-Q4wklIjasdN9iGzdJDbskDKn0yq1we7uwm0cDVtrjdOBoL6VbNdeXBnd35aOinGz1onw7BhMlz2OkdE-3g7zJp1sf4A2B4nmPe5EK52a3J44OVfcctFLoZy42DeHmuen_eol2n9pm-YA-veoA5Mqt3uOGXGECIJE0U_V6hJtqmiJ6E4nwpcLTf0NkACYeEtnZFE8djsYluNh1PZfpv0pTWZuYfOnOexTTbc_GAq6oTBoRsZSGRxTZqgFFB4UzjNvy1kjdGuxZi_LkdOYcaZIoLwQYsln-7zH-3OLrPNUAaeMFpau0m4hAy6BFw_5HI3uagmO3GzNaq2x2BJZsMmtHXxTtHZ9o_kYW_uKftgrlty3gTDS1GMa8N1ALM2KhoDfC_KY_kLnhzpbp2hINOqq6Z3Bco-S5LNcTT0CokzP_qzfQGO0hGQd8N3aB-AoXw_ZYYyMEn9vvTivCkEysGDWlrQdeRbOvfSOo2tSK-SoXVNDuU552jqVisegsB969Es7wMs-ykkTjlI_jeApmjE_Rbu2yYSwao48aL0YByJvex4MivQM9Lz7iBqj5CZ3zrhfznz8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45062f4ecb.mp4?token=MK-blKzvPxZfttkXKLG6iSHmhwILwA55SxIBskZpHabyMMqe7LFRcgE7ZwokuNYzFWMpfUI0ymDxcu9e4DyGyqjQv_9IaCJ8UUjNT-Q4wklIjasdN9iGzdJDbskDKn0yq1we7uwm0cDVtrjdOBoL6VbNdeXBnd35aOinGz1onw7BhMlz2OkdE-3g7zJp1sf4A2B4nmPe5EK52a3J44OVfcctFLoZy42DeHmuen_eol2n9pm-YA-veoA5Mqt3uOGXGECIJE0U_V6hJtqmiJ6E4nwpcLTf0NkACYeEtnZFE8djsYluNh1PZfpv0pTWZuYfOnOexTTbc_GAq6oTBoRsZSGRxTZqgFFB4UzjNvy1kjdGuxZi_LkdOYcaZIoLwQYsln-7zH-3OLrPNUAaeMFpau0m4hAy6BFw_5HI3uagmO3GzNaq2x2BJZsMmtHXxTtHZ9o_kYW_uKftgrlty3gTDS1GMa8N1ALM2KhoDfC_KY_kLnhzpbp2hINOqq6Z3Bco-S5LNcTT0CokzP_qzfQGO0hGQd8N3aB-AoXw_ZYYyMEn9vvTivCkEysGDWlrQdeRbOvfSOo2tSK-SoXVNDuU552jqVisegsB969Es7wMs-ykkTjlI_jeApmjE_Rbu2yYSwao48aL0YByJvex4MivQM9Lz7iBqj5CZ3zrhfznz8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این خیابان‌ها جای خالی ندارد
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/463268" target="_blank">📅 21:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb2a91cb8.mp4?token=EPqVFd3wr4hPwYG8TfHRbOFXxV0yW1c0RZjWZRRY31Nv1Wgcfnn93Pj1Kkhs_8wlg2TK5B1V3P8WD6hmalDrmkdrmWjBnj-MR1OeG_LmCJc_KIyTOR_lnCWuojzdnaNSDEkPL1bHAUzZ41qVEnMuhx0eqilnE7wk4MQbVt9H-clMidj4URjRudRAm46zjQQ0v1_x6GVttbK2Kg8dt9_UQ6egda8I0JsvxMFQ0Qh0QL73RPQB9Q7xEp-Y-69geySbMF8cFx5hR50Ql_TQFL_7XUOXqj5i4loHjQ3WrarPwY1dAYssiFMs6rkzD_du5chfiP0Rpo6QHAAabABLorKBFV_3JHkQXC6lSKOBS_sK7yPhqt7F9G2eP3Xucv8eJaSfdQOhK9CbCiLnZmxZXazfS5cptv2NBSfAvGgML8Ikkey2Ut3hbJ4-TYM7j5QnSY1QMMmWyNOVBAHcSquds6lNFhAkqLGvAM7NosJfZbhQ3xNNK-uqT80y3aeyvoU-Gl3UmL9SRPXVKI-7EyLm7buEVjIfeVTMVyNdYTkTIwbeilhHAo5SXhsUfB7N3nZEWikT4Maz6GK5UggiapD93GTYDqT8-voDk2VNKQP8Y6WmXzvgCfLfH76B7j7rVDP-n8kle3OHhr9DnHeW0OSaflDNQHhuUKJPUIuupEjkBKp8gT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb2a91cb8.mp4?token=EPqVFd3wr4hPwYG8TfHRbOFXxV0yW1c0RZjWZRRY31Nv1Wgcfnn93Pj1Kkhs_8wlg2TK5B1V3P8WD6hmalDrmkdrmWjBnj-MR1OeG_LmCJc_KIyTOR_lnCWuojzdnaNSDEkPL1bHAUzZ41qVEnMuhx0eqilnE7wk4MQbVt9H-clMidj4URjRudRAm46zjQQ0v1_x6GVttbK2Kg8dt9_UQ6egda8I0JsvxMFQ0Qh0QL73RPQB9Q7xEp-Y-69geySbMF8cFx5hR50Ql_TQFL_7XUOXqj5i4loHjQ3WrarPwY1dAYssiFMs6rkzD_du5chfiP0Rpo6QHAAabABLorKBFV_3JHkQXC6lSKOBS_sK7yPhqt7F9G2eP3Xucv8eJaSfdQOhK9CbCiLnZmxZXazfS5cptv2NBSfAvGgML8Ikkey2Ut3hbJ4-TYM7j5QnSY1QMMmWyNOVBAHcSquds6lNFhAkqLGvAM7NosJfZbhQ3xNNK-uqT80y3aeyvoU-Gl3UmL9SRPXVKI-7EyLm7buEVjIfeVTMVyNdYTkTIwbeilhHAo5SXhsUfB7N3nZEWikT4Maz6GK5UggiapD93GTYDqT8-voDk2VNKQP8Y6WmXzvgCfLfH76B7j7rVDP-n8kle3OHhr9DnHeW0OSaflDNQHhuUKJPUIuupEjkBKp8gT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دنیا این‌گونه جلوی نفوذ ایستاده
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/463267" target="_blank">📅 21:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBJjsQWVl08kRXpclb8k4R71uegNGlfvdWntBzTENjNdWYyC2aleSdoRtHhlSg2sZgQ120An_y7N7ovN2cEdSO_Q8FEEXESbNU0D7PDUjTdTLaheyc2zx-De2VzTUvyomKEYtTDfGigWag4rnphDEU11CObQfev4fvndujnVkznNoY8nTxPeiStcQkAZZlatrqDjYTjWvZqDzEoQ2nIJ4hbcuBgoUeaUwMSXpQIcHdtsA2zfWzCBYVBCRaPz8BoSuyTW6ALlo6Eige12muBNGKBSRq-5WrY4a9mlTBlIcfxEyGlCnt-vjpifUID7XEkYwklNgjU96RBBKbXbqo4bAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: آمریکا برخلاف ظاهرش آسیب‌پذیر و در معرض خطر است
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/463266" target="_blank">📅 21:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463265">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXJI-u3ibWhc5Wg8LkQsgpevjDehvHe8Co-TrLJXYyEI1k1Jzxd9BUjQReJmlihYmaZ3ZUYdpHcHBUHZ2t5ft7SFmx7XJPEMDdnWQ4Qgaj0jdDuuXPe7rgw_AJNot_TffT5OIKsz3svcyQYnL0vPcv0CNUEKUlk2vur03xeB2VFf6kShSsV4HbggtZ0wN75PBqZ-eRefmI7XtmpAgaD1YIl-eG9l-4zbHoGCUpeo62KvAFZTU1moMGmM1kxoR8WvV2jXgvSibeRCVJg6djclMh32OVbOymGH6krMC1vv5YSuiownLPbY-fNvrElGSc6EOcEboMRhtO1IPtub03tt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر اقتصاد: ارائهٔ کالابرگ با مبالغ جدید به دهک‌های پایین از ۱۵ مهر آغاز می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/463265" target="_blank">📅 21:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463264">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌  رئیس شورای‌عالی سیاسی یمن: صلح با یمن کم‌هزینه‌ترین و کوتاه‌ترین راه است
🔹
المشاط: ما تأکید می‌کنیم که صلح واقعی و عادلانه همواره گزینۀ استراتژیک ما بوده و خواهد بود؛ همه باید درک کنند که گزینه صلح با یمن، کم‌هزینه‌ترین و کوتاه‌ترین راه است. @Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/463264" target="_blank">📅 21:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463263">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌  رئیس شورای‌عالی سیاسی یمن: باب‌المندب به‌جز سعودی برای همه امن است
🔹
المشاط: به جز کشتی‌های دشمن سعودی، تردد دریایی و تجارت بین‌المللی در دریای سرخ و تنگۀ باب‌المندب برای همه امن است و از سوی یمن هیچ خطری آن‌ها را تهدید نخواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/463263" target="_blank">📅 21:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463262">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbad9d4e68.mp4?token=laewQououLQXe-0o7En65QDYo1KTZb1zYrKsQ0xLxD378NBxACbg8OkEpw0IAaNo-oiXNc4Eje74ShweqNM08xPXZunyRg7INAzhL8laKgxnwCYDlAPWPgzQ-qXJJqMg7RbZ7KsFV8F7u7gN6Sd5XeLJZ8G7KeGPtEFxonNXQT3_yjENgPyA-SdLblB3HjhynLnyI0TBqzuRJodntsE8k9tTVtJiVHchMBi_HxpcZGdWZX4ZzBSdyfRDg_rKIEh-eo9H_Jtjg3OJ5sehcdlavZ-PZJvj4ye9hn6Q9qd6TaQJDpfqKZZPUTRctUiZChbUUSJBVN0ZRCQMrQYlnQsU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbad9d4e68.mp4?token=laewQououLQXe-0o7En65QDYo1KTZb1zYrKsQ0xLxD378NBxACbg8OkEpw0IAaNo-oiXNc4Eje74ShweqNM08xPXZunyRg7INAzhL8laKgxnwCYDlAPWPgzQ-qXJJqMg7RbZ7KsFV8F7u7gN6Sd5XeLJZ8G7KeGPtEFxonNXQT3_yjENgPyA-SdLblB3HjhynLnyI0TBqzuRJodntsE8k9tTVtJiVHchMBi_HxpcZGdWZX4ZzBSdyfRDg_rKIEh-eo9H_Jtjg3OJ5sehcdlavZ-PZJvj4ye9hn6Q9qd6TaQJDpfqKZZPUTRctUiZChbUUSJBVN0ZRCQMrQYlnQsU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوشت‌افزارهایی که با تخفیف، گران‌تر از بازار در ‌می‌آید!
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/463262" target="_blank">📅 21:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463260">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3s8D49YPq5eDztc0e5gtT7kA1wSTbTrDejPdb_AJk_VDjeckdq-uz8eDG_kHHJ23t1VFdmcPJCfBCT3QI12tciBwg_YKqS_KaD7UM9Zrs26V7kcklHlFWvWeQvDJJGdKFCxlvKx1D4bRUzrayHEoGq2o54CTVLdHBX5637kEJKKEoVlX988J5IPnRQvs7uadVUgc9V5lm9Z6urz6EJGsL0MK5eU_b6S5r48OT30OA_dPr5ylupPcLmlrjg3gElzxtPZKRKOZ-swPsgWJw4vptcCqYi19MqNyTuA2hZQZMnUw7n3HupkmKfF0EN5w8fKnA5paD1PpusyC2vX8fwojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCjaxbW3UxF0vdfwAK9V1oFOdaKzqh9GFJgNxhERaORfIXlS7oqpZ6wQV7DTXb3zY-mkblVs9F05V2bPC51cxishFcMGZJoA1QZ4F_dHi8gIwVFkTzV5iPe1Xn6WyGD9aDwHJR-8xEGAvR4CkZp5ttGACyN9NTPFFnUstNaUb03DNV7eUdV0wdY6nCjOXfJmVPnUK7P1TrQSAxaon8WXQayr53oG5-v5D8KnccLdNyw3zIm8-gaiyBHJLLMcLYM9eJWOwSMDTTVwYMf6dmUWdF9j9ZAeZ2jjbRK9GBtLSoP1nbt3ptaG43hIEqNcW5gcgOrVH93jJQzSP5feRwNUFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف: آمریکا برخلاف ظاهرش آسیب‌پذیر و در معرض خطر است
🔹
در روزهای اخیر هلدینگ بانکداری جی‌پی‌مورگان گزارش هفتگی پیش‌بینی بازار نفت خود را با جمله‌ای غیرمنتظره آغاز کرد:
«برای نخستین بار از زمان آغاز درگیری با ایران، ما هیچ چشم‌انداز پایه‌ای (سناریوی مبنا) در اختیار نداریم. ما واقعاً نمی‌دانیم چگونه باید سرانجام این وضعیت را مدل‌سازی و پیش‌بینی کنیم.»
در واکنش به این موضع بی‌سابقهٔ تحلیلگران بزرگ بازارهای مالی، محمد باقر قالیباف در صفحه شخصی خود در شبکه ایکس نوشت:
📌
«این وضعیت دقیقاً شبیه پارادوکس شرودینگر است: امپراتوری آمریکا در حکم همان کابینت شرودینگر با بشقاب‌های در حال سقوط است؛ در ظاهر هژمونی و قدرت برتر خود را به نمایش می‌گذارد اما در واقعیت کاملاً آسیب‌پذیر و در معرض خطر است و تلاش می‌کند ایران را بدون هیچ پیامد و تاوانی خفه کند که این غیرممکن است.
📌
این بازی پایانی در هیچ مدلی قابل پیش‌بینی و شبیه‌سازی نیست. درِ این کابینت بالاخره باز خواهد شد، و از همین حالا دست ایران روی دستگیره در است و شرایط را کنترل می‌کند.»
📌
قالیباف در این توییت از میم (Meme) معروف اینترنتی بشقاب‌های شرودینگر استفاده کرد. تصویری که در آن بشقاب‌ها به ظاهر سالم‌ ولی هر لحظه در آستانه شکستن هستند! تصویری برای نشان دادن وضعیت در معرض آسیب و شکنندهٔ آمریکا در منطقه!
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/463260" target="_blank">📅 20:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463259">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌  رئیس شورای‌عالی سیاسی یمن: از سعودی غرامت می‌گیریم
🔹
المشاط: دولت، ارتش و مردم ما در مسیر پایان دادن به تجاوز و محاصرۀ ظالمانۀ عربستان علیه کشورمان تا بازگشایی فرودگاه‌ها و بنادر، بازگرداندن ثروت‌های ملی و دریافت غرامت پیش خواهند رفت. @Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/463259" target="_blank">📅 20:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463258">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
رئیس شورای‌عالی سیاسی یمن: اعلام می‌کنم که نیروهای دشمن سعودی از تمام مناطق ساحلی غربی یمن اخراج شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/463258" target="_blank">📅 20:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463257">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge1nM6_QbUQi4cM1ywvMxv8fsAPTSgh5OncTRUuwyNsUPhEpstiHfh1wMAhPGp3gQeaHbDSEpaJ5HLQYp3n4ck7t3GnHZWa4dpaFGu1pOyYYi_r7_KgVF3h5U4298gofj3JKTKddJ6WMMnFxLTfmD9UarhCrOTElDzWuCt7IxJs6nEsSUkT8811Sfb2uVhJLKGq9Fbte1LJbeniYUG0Usp2AXttQy5dIV1wKubp6pEFTF-f4_L-F9ozB02B50R7Eye6Li4j9rXvmtShws0wI7IPA5tHB_TYS5qfsKsspgu4K2ejR1HNLo5Atg8bDy2wa0SBXrBrltLkPuO69v7KcVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئیس شورای‌عالی سیاسی یمن: اعلام می‌کنم که نیروهای دشمن سعودی از تمام مناطق ساحلی غربی یمن اخراج شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/463257" target="_blank">📅 20:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حملات هوایی صهیونیست‌ها به جنوب لبنان
🔹
رسانه‌های لبنانی از حملات هوایی ارتش رژیم صهیونیستی به شهرک المنصوری و النبطیه الفوقا در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/463256" target="_blank">📅 20:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2270aa5ea8.mp4?token=FQ2Z5ZMV4pGj5MRjJHZqtzWa5Zj29bU8iYgSKotGqa_yiAWt4uLD1D7gN4SQ87WYBM9t1VeRJgl2y_txWC28Q1hFbCYVkNTYHO3azbPBcMS9Re5LJ1bWV_o1iIWJF2AGkkJVPdkagJRzX6rrh2SgGfpIaVL08-cgg94wJH6aCrr4fmAkDlkbb1U2uhlY5TB8HNtN6ShSJllAPPB0poDOBEt8i1ROZ_YbxXwjZCrA-_g549t_g7kY-z7N_oivtmQpKUU3R65YDCWzYenat3xpp-7LI78iqizs90pDMUa-tHIXkdyUFRuH3xcwGx9k_X0tGI6BtWhybCsNExQ_jGWHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2270aa5ea8.mp4?token=FQ2Z5ZMV4pGj5MRjJHZqtzWa5Zj29bU8iYgSKotGqa_yiAWt4uLD1D7gN4SQ87WYBM9t1VeRJgl2y_txWC28Q1hFbCYVkNTYHO3azbPBcMS9Re5LJ1bWV_o1iIWJF2AGkkJVPdkagJRzX6rrh2SgGfpIaVL08-cgg94wJH6aCrr4fmAkDlkbb1U2uhlY5TB8HNtN6ShSJllAPPB0poDOBEt8i1ROZ_YbxXwjZCrA-_g549t_g7kY-z7N_oivtmQpKUU3R65YDCWzYenat3xpp-7LI78iqizs90pDMUa-tHIXkdyUFRuH3xcwGx9k_X0tGI6BtWhybCsNExQ_jGWHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لیلاز، اقتصاددان: وقتی طرف آمریکایی نمی‌خواهد مصالحه کند صحبت از مصالحه پالس ضعف است
🔹
به غیر از نیروهای مسلح، بقیۀ نهادهای کشور آرایش جنگی نگرفته‌اند.
🔹
نباید فراموش کنیم که بسیاری از مشکلات ما به جنگ مربوط نیست و برای قبل از جنگ است.
🔹
در ۳ ماه اول سال…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/463255" target="_blank">📅 20:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463254">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb07fb5b1.mp4?token=k77EZTS1BFtEPDTL27fLAsmW5Y0clPNk4Q0UzUrY59obilV-kvpwWRnDLqgQnlQ8Ltw83ckkW_UpIJlnW2TXexuFpig0qmeeewBGCcRULbw4_tnfDy1_IyQQkhtszqpCovLYdPAvOE7q6SpJxjecwDtRlb8g6hgkTxKfcm_mkmwUJhI7-0N-MV6043jd-7Mn7KmazO3yruerW2TJINh7dc5t6QDisdcNpFPCv1dTmQj25c8uIwKIivgQHfwCRwXhZtTCFNNuakAimeL_7bdFCmwwjURHOnghDSJoseJuUwYAWEpIaZtdbRgHQ3iWT-wQnad434NEK1li-krZ9C69vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb07fb5b1.mp4?token=k77EZTS1BFtEPDTL27fLAsmW5Y0clPNk4Q0UzUrY59obilV-kvpwWRnDLqgQnlQ8Ltw83ckkW_UpIJlnW2TXexuFpig0qmeeewBGCcRULbw4_tnfDy1_IyQQkhtszqpCovLYdPAvOE7q6SpJxjecwDtRlb8g6hgkTxKfcm_mkmwUJhI7-0N-MV6043jd-7Mn7KmazO3yruerW2TJINh7dc5t6QDisdcNpFPCv1dTmQj25c8uIwKIivgQHfwCRwXhZtTCFNNuakAimeL_7bdFCmwwjURHOnghDSJoseJuUwYAWEpIaZtdbRgHQ3iWT-wQnad434NEK1li-krZ9C69vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لیلاز، اقتصاددان: وقتی طرف آمریکایی نمی‌خواهد مصالحه کند صحبت از مصالحه پالس ضعف است
🔹
به غیر از نیروهای مسلح، بقیۀ نهادهای کشور آرایش جنگی نگرفته‌اند.
🔹
نباید فراموش کنیم که بسیاری از مشکلات ما به جنگ مربوط نیست و برای قبل از جنگ است.
🔹
در ۳ ماه اول سال ۱۴۰۴، بدون جنگ رشد اقتصادی منفی داشتیم اما ۳ ماه دوم ۱۴۰۴ یعنی پس‌از جنگ ۱۲روزه رشد اقتصادی مثبت بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/463254" target="_blank">📅 20:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463253">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ارتش ایران پهپاد اوربیتر دشمن را بر فراز تنگۀ هرمز منهدم کرد
🔹
روابط‌عمومی ارتش: ساعت ۱۸:۳۰ امروز، یک فروند پهپاد شناسایی پیشرفتهٔ اوربیتر با آتش سامانه‌های بومی نیروی پدافند هوایی ارتش بر فراز تنگهٔ هرمز هدف اصابت قرار گرفت و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/463253" target="_blank">📅 20:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs5Rf8R0IgMwjjp_cH8nbESvU3l3yulNUSs4hcuSmJf4TjqnMeTJpkzV3xVg6ljG3qWfNWuLRFBbvDDVrHDCYe3DrPkcfQkmokrj-S9lB05DT_J8sIzK3fAwtUNkuosKhapa_uM94p00h6NEkYXxSUM5UrMcuS00uMCtZB4xO3zGmOnRl9obxIF8oHR_IXQAtcLfbPYpECxfbzPceestrRIJJoikt2kSXmjz28g-GOcAlCKmv3DcU8cXstFSpwpSI4PynMiY7d5owcFp_motpEM4ncdfHIvo3tRglz4DPWqhMY26FvF3FzmzMDVBWtDL2HQdMHOyaKewa1mhEAV9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: ۱۲۸۸ واحد آموزشی که در جنگ آسیب دیده بودند به چرخۀ آموزش برگشتند
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/463252" target="_blank">📅 20:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8b777fb5.mp4?token=vFa8H0MOMcniOMJ8MfoPsmqTK8Y7D45tItg6gmvUz84CKy73ibvWuIJtsndm766sFCYtxMEleuDI72XSiTbxcUcS1gPYEc8i1Xd8yabGCi_OIxXqGWMYiyndPje2nd3FBd9CBjJ7TheblsiwmX6xIVeyapsP2cYGHPL4XgBvzxJ3vNRCL711fmyb0pQnQQegLoRlEoeki0IN-A_wz133G_DojbjFjPxn-XEA6KxfuJipbYfZ3Nr64xbNBJuaJR-1FoY7Ns0Jkg2-eT1D2ZMBdZLtAEPPmQMUmU1G_cuae7uP5oA0sL1zCboIdq7m6hsHr9MoVI8tKEaPDEIfysTXSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8b777fb5.mp4?token=vFa8H0MOMcniOMJ8MfoPsmqTK8Y7D45tItg6gmvUz84CKy73ibvWuIJtsndm766sFCYtxMEleuDI72XSiTbxcUcS1gPYEc8i1Xd8yabGCi_OIxXqGWMYiyndPje2nd3FBd9CBjJ7TheblsiwmX6xIVeyapsP2cYGHPL4XgBvzxJ3vNRCL711fmyb0pQnQQegLoRlEoeki0IN-A_wz133G_DojbjFjPxn-XEA6KxfuJipbYfZ3Nr64xbNBJuaJR-1FoY7Ns0Jkg2-eT1D2ZMBdZLtAEPPmQMUmU1G_cuae7uP5oA0sL1zCboIdq7m6hsHr9MoVI8tKEaPDEIfysTXSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«چشم اسفندیار» آمریکا در منطقه چطور کور شد؟   @Farsna - Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463251" target="_blank">📅 20:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anjmFbKf24boFr_5GMcpJCioW-XX1E8IEP34tYNgwy8IvMGXtW1EWejSGGJrrCSSgyxuehnj8ChQPo_OaHtCbqpAkOC233twUwdRGSlo1bSEOD4lEtQv5jf8pvLaz9xGjRL5FNlf6dzbxbaEzMJPhf9EJ0_mPVeMlhVOOPr9-tG-qnt5dCb_7qk-RRs0aBwgBn6ptCDA-T2Q8AK3PR-Qfh-dPftIBK35yW7gyr1wkrvQuw6haItYum9yVNkeF6n2KY7yrqSm_6zd41QN6Y59Dp-d-b6CCxYvF5TrVTd9AHUORcmx76eo87JsUeVuK17WSO5QalR8DzONaCcjmXB7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار یمن: تنش‌زایی عربستان را با حملات کوبنده‌تر پاسخ می‌دهیم
🔹
سخنگوی دولت یمن: زیاده‌روی ریاض در ارتکاب جنایات بیشتر علیه مردم یمن، صورت‌حساب میان عربستان و یمنی‌ها را سنگین‌تر خواهد کرد و سعودی بهای هرگونه تشدید تنش را خواهد پرداخت.
🔹
یمن برای جلوگیری…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463250" target="_blank">📅 20:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463248">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEh2Dph2gmWLd5jm2-HEsxS1zEkOn8s8cC5oO7ym8zCzponrSShhOuLiryzjLPbY__ecl5UjVbO-7ZSrdJJ1tDsLyAwnJcKtemb4SjCvaJbXRiWzVOvbAWGUS6Bmmf8a1Ydhza3Rj9W-s8n0grUAf9MhSZmNoEzZmf4a4lW4LXPI1yomSedbMLYUkmcqc5aSrzQJyTmXp0cTt6Nw0NbOZOzt9rMFX2g2iYzFd7g0i2DgSc9TOBnmmk3JIyU9X0RiWuir-1GGb_8ySmu2ErnGSO4Rzjtjw90HvWk_uHRczUkFTcph0DZY9HT6LfMlqP8-OLS3CIx53bL-sExGcUdNsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو اولین دربی فصل را باخت
⚽️
اتلتیکومادرید ۲ - ۱ رئال‌مادرید
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463248" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463247">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fai8kErVTD5sZ1eSZNyWlK8tdlUhpYsxIqdRo_EYORe8zWzGT5hULQL5q8u-xfeCPJxnZmwyPMQRuiu7B7wS2FL41h0O4sBk1djCQ8rFtWgypiLd613DMzc8iSyXK-25R_-7XBkz_ttnN8_TtewAJ68EbkrsALywGOwnOI8i_WAFAs4bBQSC9XjaD1ywYJE4pM7tF-y5VRWbAtpLOWiMscJ_UAQd0DNsdL2XcAjgFpgvPWP0GY59fbto-1bHeDikAc5p_n2nMs2fSvXN6x1MfqjFWdhmNf2DjSVRRZHIYlIGANWZ7BvRhVSztVR0PPI85xsivW_rzGCxEtli87CL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: به‌هیچ‌وجه نباید اجازه بدهیم تولید متوقف شود
🔹
همۀ ظرفیت‌های اجتماعی و نهادی کشور باید برای کمک به کاهش مصرف انرژی، حفظ اشتغال و تداوم فعالیت واحدهای تولیدی فعال شود.
🔹
در شرایط کنونی، همه بخش‌های کشور باید با هم‌افزایی و همکاری، برای حفظ جریان تولید، صیانت از اشتغال و استمرار فعالیت واحدهای تولیدی تلاش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463247" target="_blank">📅 19:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463245">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxM3j-uMtVUhmezS7Px6SQdQ0sRMzv4nJTrsrJJqE-vuQwaDpg6fIRl7i-bJUm8ql3AqqJv0WgGEg5bKNMoHA7diXvskMQHDCSD8RzB-M-gKdGtzYQGvcF2LPAdulOwyq7HWcTjbZQYdeO48ZQLUxrLPgkIY5T5vGGrT58LAPas4XVhooYumCccLjyx-0HmcBG5qyTSahGtyDW2NRPKDtTaoAI98Heo4WurjGL9zHz_7_MXBJ04-N4V6NXTgcuZg3yjfR084j71scJPfT5Os2WrkBjW_GQFoUZg0MRnVZRjd4WoBhwBto27wtGqo9A6yx_YyMTXfULRJCjPJlpW0hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر سیاری: دشمن ما مجبور است منطقه را با ناکامی و آبروریزی ترک کند
🔹
معاون هماهنگ کننده ارتش: هر دشمن تجاوزگری، برای خود اهدافی تعیین می‌کند تا در نبرد، به آن دست پیدا کند، ناکامی در دست‌یابی به این اهداف به منزله شکست دشمن تجاوزگر است.
🔹
امروز دشمن ما نتوانسته به هیچ یک از اهداف خود از جمله ایراد آسیب به تمامیت ارضی ایران اسلامی و همچنین نظام مقدس جمهوری اسلامی ایران، دست پیدا کند و مجبور است با ناکامی و آبروریزی، منطقه را ترک کند.
عکس: اکبر توکلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463245" target="_blank">📅 19:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463244">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLNnfF6Z_INqfqCXJecqBO2Yhel7znhjRG0bhxIwozSAub4bUnwdl5trZhpMQlrUXSK_TO0Zd0YSwaYzRmT8wHZWu6O5mlJxIevFhFH0fO7WGmbNnfmNvQf44gU6pULmlDu2JA-2xGZpriimy64IyNolRKJ-T0iVAz1MxXoQsaMjw6OThClPIPvYWsIjfIqA04-RgrxyUskSjJ27x9Hf6HpRI3QKAiEzkwrjiD4BmAqSi_x8UAJLpFOwdlv48bHnKQ1eyOWm0aSNlRU34c1S-gl-G6TaxLC_h32mqAsyHTxmODdSvSrX7vjmYPijIKK_4SXiBc3rsBX2t4PftXbecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرود اضطراری ایرباس در مسیر استانبول-تهران در تبریز
🔹
مدیر روابط عمومی فرودگاه بین‌المللی تبریز:  یک فروند ایرباس A330 «هما» که از استانبول عازم فرودگاه امام خمینی(ره) بود، به‌دلیل نقص فنی اعلام وضعیت اضطراری کرد و در فرودگاه تبریز به‌سلامت فرود آمد.
🔹
تمامی مسافران در سلامت کامل هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463244" target="_blank">📅 19:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463243">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCsO4r63qA2mN0hc-h1pPViXhKvRcMGOE09QJUJcb4PL19CJSq8UIJ6BlkgYodnGkyN_sn-miop7TTNWCxm1IPBmzY4w_4sjHnOTd55dHZwyFFkE4UuD9KFwW7Csnke-uTS8GUSuzzDbp8UhbDDy46HAB3F-c201du_W2fYtqpxp1IGxqG_0IoMpN0cv8-3GOxBdWWhAk5rtD-xPgjEdvyFXCS7zGdSZRRtqUM8aQjinmg5eV4RHYOX5zHXt4kdo4BqzAdqZlp0TCIliCrganNLrKWl_nieBUdsz3caZy6zFhV86iwyc88dlrnvkV88tEXe2ia_r0hUJn2ZleZp4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  صهیونیست‌ها یک بیمارستان را در جنوب لبنان آتش زدند
🔹
رئیس کمیسیون پزشکی پارلمان لبنان: رژیم صهیونیستی با به آتش کشیدن بیمارستان دولتی ‌میس ‌جبل جنایتی جدید به کارنامه سیاه و متوحشانه خود اضافه کرد.
🔸
رژیم صهیونیستی با وجود امضای توافق آتش‌بس با دولت منفعل…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463243" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463242">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da305b137a.mp4?token=gmGOIPxeRPX8fZy3qA-yR4BI77fPka7HZnZkV7EKCdbeqXXVETVLJqFHduNXiRU6D0gHAMyOP43AiAXDkgwh7Eg2Wkwa9Icz7aTVlPSxhyQUwh3-ja04PpUTWeJv8kZKPqGik-JsWUTHx6F6o5ofv37pjepXxeMisNIPc_DQ1xuA7iPpROkcolNq3B4GhAkrFpVYonxDRaRsjUDtLqJ82nSIAKsR3SupHdfY96WPln9zOb5XJ4xGHlucdtAJSFO5rHysyOlFLomwy7ieF0sDRzB2J5v_F1kX3nIBF0MA6GtDUhUg-g57ax3VoLdBiqxF9pjM1xfMBdCwk9mPA97pDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da305b137a.mp4?token=gmGOIPxeRPX8fZy3qA-yR4BI77fPka7HZnZkV7EKCdbeqXXVETVLJqFHduNXiRU6D0gHAMyOP43AiAXDkgwh7Eg2Wkwa9Icz7aTVlPSxhyQUwh3-ja04PpUTWeJv8kZKPqGik-JsWUTHx6F6o5ofv37pjepXxeMisNIPc_DQ1xuA7iPpROkcolNq3B4GhAkrFpVYonxDRaRsjUDtLqJ82nSIAKsR3SupHdfY96WPln9zOb5XJ4xGHlucdtAJSFO5rHysyOlFLomwy7ieF0sDRzB2J5v_F1kX3nIBF0MA6GtDUhUg-g57ax3VoLdBiqxF9pjM1xfMBdCwk9mPA97pDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژنرال بازنشسته آمریکایی: من به راهبرد امنیت ملی فکر می‌کنم که صریحاً گفته بود تمرکز ما قرار است روی امنیت داخلی و چین باشد. پس ما اساسا در ایران چه غلطی می‌کنیم؟
🔹
چرا دربارۀ خسارت‌هایی که در جنگ با ایران وارد شده، با مردم آمریکا صادق نیستیم؟ احتمالاً صدها میلیارد دلار به دارایی‌های ما در آنجا خسارت وارد شده و مردم آمریکا اصلاً از آن خبر ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463242" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463241">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV5lv4Qd859a3ALXtRk2HWaKJeS9EIj9AfjvEQT1pktl5XHQ5vTSwRocW7_68yk3_O-tH_tvNloGbRffsX2cuYgiTy0wm27kzbck8xu1XocVTxakA9rpIPh41fiOsCI2ZwAdf0J6z7dEn2DvGmVT8l20erUZ05rS8qqtWzPle8OcR4fcT1FSqmoV-QKiixMOPN3XhtvrbANKDYKM1gU1Vv8yQBkMGqBJCfdWiF-O4rrBmWFVs5bwC-quc6zrQGUdMYkEgYLw-Kl7d8VwXJrATyEsu9KwzfLWdnAfwMUWVaxqfiAy8RXPFZe3z7lpx7I5rMfGk5tJh3RGH144ehKd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور بازیگر کشف حجاب کرده در شبکه نمایش خانگی
🔹
حضور شبنم دادخواه، بازیگری که در سال‌های اخیر تصاویر بدون حجاب از او منتشر شده، در قسمت هفتم «اعتراف می‌کنم» فیلم‌نت، بار دیگر بحث درباره معیارهای انتخاب بازیگران در شبکه نمایش خانگی را مطرح کرده است.
🔹
هفتمین قسمت از مجموعه «اعتراف می‌کنم» با حضور شبنم دادخواه، بازیگر مهمان، در پلتفرم فیلم‌نت منتشر شد؛ بازیگری که پیش از این در چند فیلم کوتاه و برخی آثار سینمایی حضور داشته، اما بخشی از این آثار امکان اکران عمومی پیدا نکرده‌اند.
🔹
با این حال، حالا حضور او در یک محصول نمایش خانگی که از فیلم‌نت منتشر شده، بار دیگر این پرسش را درباره فرآیند انتخاب بازیگران و حدود نظارت بر چهره‌های حاضر در محصولات نمایش خانگی مطرح می‌کند.
🔹
«اعتراف می‌کنم» مجموعه‌ای اپیزودیک است که هر قسمت آن داستان و پرونده‌ای مستقل را روایت می‌کند و با حضور بازیگران مختلف ساخته شده است. این مجموعه از مردادماه ۱۴۰۵ به‌صورت اختصاصی در فیلم‌نت منتشر می‌شود.
@Farsnart
_
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463241" target="_blank">📅 18:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463234">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxUtV0vpPPNqDZdxrJjtm6gvTHSOCoESOewLfXxLOCK5lHDkzI3frsNtC40R0MwTW3K1ZPhM2-wOQFgiLvZW6NZ45UGWUnkjAswO4InqDhu9K5caSeAj4i0sxNEv9zBcQkOLX6jrvuFknxq2-K7sbnaEupngBdi9xfamiE9Om_MFPzJcuu_4Krmt0w05zA9O4NJSkjJWMaAwKeW17ia0W7LjgtZmCQxLN1pKnIeymdY12hKKWeBPnF0RbcGmm_oz_86B93j6ywkfc3GLHjoGcuVy5E80PTJljOOGbAI9a46TdW9IpspHqrcX97XYWcPYNoN-MMthFezW_TP-vNp1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZRBSE5W6Un0V9kiT6kCOcGBAg4wUM1zECDrRrHsRawT-r8Pcvz9gwquXqEn53smVbweMNhACSYFdvvq4OunjR9uqtJ9E2IcBe7r_Vb-BYf_lChppFXwj7DdRubMRDbYY6KJB9h2zQG0kivdDpZ1m-wQ93PWpHKIEGKsp323X-tAHkS-jlLBhjHmvLXeaDGs8F3-9-3eRHa54oT1284VxMfQANyfaaci36t-xUyZLRIXCFmRHYnWCJ2l_T1IRuIadYldXf77MeohQTeV6XbXxMWj-awCD2eNS3-67LPOEH5_il2A8Lfa0Y5nFVErNNs2d8BehAvEQcf3kK4XS-FLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRr8u8Q59drg4Wy0ZS82bIwG7kotAWslpW8Flx4OmUGnYksulJpIvcAWoYS36aBSUSQ9ti9Gq73kMkI1M03eG8nsGxYWR32CUtoAGoKWHWruQ-rpjw9o0vv3TYDFXvNtAAOo2O_Mpn6hu-uuOQ13FvUw-IF1iRJuh6n5UY3PbKrrJkuRDDbEGa3MNaSGtjDOIZXkOvb52SOealpQNDILEh4t__wmWyp-sE2PZ9l9Z3hcD27FPQKT_fN982LRPayBzyViO0WpAMlgkYtiWvg76af0e5IrBoucp0W9CWxLA6565kDhNBbohxKq3ai2T7Z39g8Ro_SuS8yKSXkeO20iuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcBaMFOw6LMcKk8mWmrSWe-K3889zbCcl4NhFeR0lYQtXnTZSRF8KxZ0BKd4HpnVnbhG6LTJTZyh_ZCs5I3PyBOsPifaPZbjKzOytXugZ0WMhF4L8Cwe1OQpFSCIvPplblwAkFyIqtw6LHe6gVBprvBiuz00wqgx2UaRp_8ciWRXNftjqvxub1dMIfC5geL5z6uMcs0uuT3D6zQd5yPk4gquGo1NccJ8WepfpwvWGYAmouT9xcioSm4gdz9C1E3drPEiRerQ-scP00bcn5oFN2tBDwRIHVeIiPWDEyfjb7GLK60LzoJQm_uXptbbXacKXEmKdFvIsb45-ZyoOBC7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MiwlzH4LrnUf5oHCR_fsBo4ilCWw6eQHpzZ3lb2_6sTOOtK7znxEFuQS3Un0pAQQr9c_KY6XUzldaKmS7oClR8a6fpjbckvihkxd8gniN4MSNZ45gawruFBjlbnbtSGqPoM_L-g7XS4Y4L3jcGBOvIvgRhnX93_wOrpHsOspzsclzAQdhC2c9or95u7CMiW3VvZdmtFLEoc5I_w-EwP9PyEHUWMMCDAwAMh-kHdMpVk73uGpMwr5Z8Dxc2gEKC8Jjj1LYUlgFF7rMjMMUuwMq7r_FyhOUXgSicbAx3ei5jmE-4PhDFNWLh4UJ32uDgyLBgRNyzuH6UGamWFycnQ-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABu9x85VLKxFYkkdnHSpxqPygvNitAvMt2dmZ4ecE3gTgMN0iBCTofKIZtagoLEp-3mLzOfMIcl0CrwhcksupEc7Cs6Qbx_A89eeVWFrglrTBt1QfNJNbctuS8wWeDY15c3u-48x8ozV5m1MW69sCQcTRX_C0wjs5GGiyPpLrlW6nd0ouLNu2zkIU3cRaiMO3Gmat6q1GuIGPh7OBgnpTGqA2GMe8SQm5Ht4pH9Xp8r0ToDSNt0qP4GoGltF9B4xSfc2f9VmbpeLH-_UvYOx9FQn9NCu-XeEtXnJd_FRwWZXlXs7VTeofREqIPn9ri0dQc3L3bwiVr2QBpSkXGA4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUsZ0rYhvMBqLyMDMA62cIWS7ctKJKYwxHVOsbD_35YBO7pnDmQNWWrtQuWRbCYh-2zeBGnH4WfU9CYC0WJdnc48V3r-IQcZX72VMjrKG0d4zMQIQm-Tturlz7EmulgW2Szk2CCUiu3IwqDBWk42EzGlVySgsUQLahasBomkDLoLgzpu9ecGy81WFQFfhS7wgN98KDQ7fMk3I6bq57sd81zUXMA_apwSoIEbbKc8ntnvit5eb4l_x1rXGBGcRH4-tzKYip83PFeeG4HAkkl7zl-j562zlu6k-Yd-0b-Ri28S-kDPowsCvknmbaFjBLJe14qrTkGOaAi9Y8quXdFBOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
اولین مدال کاروان ایران به‌نام بسکتبالیست‌ها
🔹
تیم ملی بسکتبال ایران در دیدار رده بندی بازی‌های آسیایی۲۰۲۶ ناگویا، برابر چین قدرتمند با نتیجه ۷۹-۷۰ پیروز شد و به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/463234" target="_blank">📅 18:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463233">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgMjpv4Y2vWejdwu0CGYVCZAS4CYA_ejEp-t-huX_5XRIQ5SmFmdjcFNIQgdbpBtPhaQ7Q-Rs_GTPROI2tHreuYtLl2DjwArHVMrLhNqEIdhS77sXqiG8w5xyCcMeRkstGlrtNJV3VuAZFrJp627ju7cwmH_0tMA0KxEGrwN8uhO0Y-Fuaj2eecDUgSsHslS46EcEeikZeY2qBlvyr8w0zndejDhSYeYQz1JXpnorq40AuxIoab4qXSTx7_ofzG0IbPYdpD3p6H0KTFLMb96OIErZ1Dy1DL9vHsZq_cz0CAHxaofRT7M6cueY-VhQnPbwuOn1XS-cmzp3lmM72Cf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور کابل‌ها از تنگه هرمز منوط به مجوز ایران می‌شود
🔹
نایب‌رئیس کمیسیون امنیت ملی: مادۀ ۱۰ طرح راهبردی تأمین امنیت هرمز به زیر و بستر دریایی، ازجمله عبور کابل‌ها و تجهیزات انتقال داده‌ها اختصاص دارد.
🔹
این ماده در یک کمیتۀ ویژه باحضور مسئولانی از وزارت اطلاعات،…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463233" target="_blank">📅 18:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463232">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsrlRF_XWCvVM2Voi56JDBvf0A6w908kQDgUtMrHTLNHh3JekGrVXVB4CagdcAup2zYnOaRhcnpH0G017kA9SIwprAHiZrb-nTZv867owbFC6i0AWG7e_Yw_wK4QXu31yE6v-1vGZw-oitof77TQQJESWyGtXj0ZpWA_sxlQhnai1jEXwwHYfqgQ9tum0jGW8Hp5MUb92OBnJs6H7zuwrHIGUdbdOlJuxrXAWSGmOE8j0Vo2bQb36Llimp09LrNuNKAK_7_5yk5adFyJ40gpVf1qgf-tZMejywedj4H-AqkYlzO9VKOa2eE0GDALAd2ES1vpD4tttqM-4H58RjBIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش قیمت موبایل شروع شد
🔹
بررسی‌های میدانی و اظهارات فعالان بازار موبایل نشان می‌دهد که با بازگشایی سامانهٔ ثبت‌سفارش، جرقه‌های کاهش قیمت در رده‌های مختلف قیمتی زده شده است، اما این آرامش، همچنان به یک متغیر کلیدی یعنی «تأمین ارز» گره خورده است.
🔹
بازرگانان اکنون برای ورود کالا به کشور، ملزم به استفاده از ارز «خود» یا «دیگران» هستند.
🔹
آغاز ثبت‌سفارش واردات موبایل و عملیاتی شدن واردات این کالا در قیمت بازار تأثیر داشته است و به گفته فعال این بازار می‌توان گفت که قیمت‌ها بین ۱۰ تا ۲۰ درصد در بازار کاهش داشته است؛
🔹
فعالان بازار پیش‌بینی می‌کنند که با تداوم روند کنونی و در صورت رفع چالش‌های تأمین ارز، نخستین محموله‌های جدید از اواخر مهرماه به ویترین فروشگاه‌ها برسند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463232" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463231">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st5VHHyj6qi_u50w_hI7-aLk_zPlcQDAt9TZU9sKowqt_e2bp_osN0fLX3ShNM7X_sJKQh76z2KM97NCP9r-k3sz7mbZbGh6vAIAyjzR6LpZgKWR8P6v41XcSyb8U1dYpsmPiJInX5sowR4ME2tDls01KLtdhz3Tzn_Tep185S6eF9CB_tDMyiI3kVAOu0GRCJnUNNneAx5Vb7jkkMzhTqMW30_2moPFaNAjdPPAI40w9ljDF40q_Crbed1f0wUPgDc4gSQYI03m5soxQvymAbGYazkqBZF2YqzBfd_FQbCkJU5bEyp518BuSTpQNUyAQ9BHduRz1tV7GKce8DSMmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد حساب‌های بانکی‌تان را اینجا ببینید
🔹
تارنمای بانک‌مرکزی برای نمایش حساب‌های بانکی هر شخص حقیقی فعال شد. افراد می‌توانند با مراجعه به my.cbi.ir تعداد حساب‌های بانکی فعالشان را چک کنند.
🔹
طبق اعلام بانک‌مرکزی در آینده امکان غیرفعال‌کردن حساب‌های بانکی…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/463231" target="_blank">📅 18:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463230">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea0fefff2.mp4?token=spBduvKb3nh1MoA8Mq2WTw5ApKpdPet4gwgTvFtZ6Bom8sF-GcyNZvnQ7bJhGuQ4H3IyhOqcsrroFeSo0aj3zBNINbXcbWOC66CZv4vRu1HGbnX_mrGELyNyE7AJRssdWYkILmLwRzyuxjoKRHA05VtoOeW1SttYscguBx1pWrZvtiEe7UGSdcpo19yf9o1V80B_0znaHekKhgxFwonYx4koeW7uLw-du_ME7tQtM1q7PKtafPX0MLR1NoMg8ieyT-AgCcILr8_7zJTQVCSo7i4Z10z8suhQTxdfAFGnHgMYg58p459XLMNRk1shwfhqzxJ35mjlmIA5AMIYB_gw_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea0fefff2.mp4?token=spBduvKb3nh1MoA8Mq2WTw5ApKpdPet4gwgTvFtZ6Bom8sF-GcyNZvnQ7bJhGuQ4H3IyhOqcsrroFeSo0aj3zBNINbXcbWOC66CZv4vRu1HGbnX_mrGELyNyE7AJRssdWYkILmLwRzyuxjoKRHA05VtoOeW1SttYscguBx1pWrZvtiEe7UGSdcpo19yf9o1V80B_0znaHekKhgxFwonYx4koeW7uLw-du_ME7tQtM1q7PKtafPX0MLR1NoMg8ieyT-AgCcILr8_7zJTQVCSo7i4Z10z8suhQTxdfAFGnHgMYg58p459XLMNRk1shwfhqzxJ35mjlmIA5AMIYB_gw_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع عربی: فرودگاه اربیل هدف یک پهپاد انتحاری قرار گرفت
🔹
لحظاتی قبل صدای چند انفجار دیگر از این منطقه شنیده‌شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/463230" target="_blank">📅 17:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463229">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNMDu8Nz56aIbXBHGiOMVIypgBPkJuNvIeHM7NL8m6Rlyf0ah0uAyt6X0YJY0xQKGSvbyFVtilU6jSuPlXOdxpEm0xlaLHQ-3cyU1eTRN2aVI1Qe2nkNtpVag4Y8ZHbIoLRHE_F6IhZf13kLa7wgnS3mPLpPYQDsk0UuwWgWMjvFY8AVYJT4oIsQSXmupSp_krPy2nj3vbbA90-t0C_yqtVJZagi9Kw_HOQAb5-GUuWnkC8W5bYgdmh-teRmFepKpTaqjUo6WUD48J4eb84hBWDm9sIuv8mG3WmN-TCQGk4zRGdvkiAmmlVQ8C52ajKu9n-QBScNjClu_kc85Kp3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل تراکتور: بیرانوند فعلا بازیکن ماست
🔹
حجت کریمی: اگر سازمان نظام وظیفه اعتقاد دارد بیرانوند سرباز است، در نامه‌ای این موضوع را رسماً به باشگاه تراکتور اعلام کند؛ در غیر این‌صورت بیرانوند بازیکن تراکتور است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/463229" target="_blank">📅 17:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463228">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVv8gAVgDVSxdkcgbiY0JrR7AxVIzVXrrjtkSP5NXuTarIYbVBZDrPnYVu7IPFJppKTpU5FG2G30RQg1wmCz2RBNUmHvmklZcyLyaoqT8BOG2jDZeWhJenTIEB8yYCfA9dBvL8oJkvdGajPTe-ohhurAQHgq0vQ8eVBe2m7rQRDekHlE9lrb2iaMUJZ53Ztmv80_ua_9YK0O_zwNPWH07GDqc1wcmcYaeFEwVrz2g7aBkqh3s6uu3crYjiNU-No5HV9h7lOmMF72IGKBHj-ZljVNnQF83Tanop4cdwriHUVh72KZclFf4Kq_OReupY3DMU8tpHyz4c7JBUBoc4LgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در منطقۀ اربیل عراق خبر می‌دهند؛ علت این انفجار هنوز مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/463228" target="_blank">📅 17:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463227">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75282217c2.mp4?token=hy5NqAbB8VWaQz7EO_1tiKBLLE0fw4crtVHAjE371HGgjjC306zgT2b0OAyJeQKBj7gZK26B2FttcHt7CLlzjiCl4ITABd3P_-0tRPaFc8vvztMGD1ltlDF9w8RldxRw82yGmOsGauTalkJ9V2KfBncFzHpA3AuWn2TKJddD32vxUkfXvwx9IfkOA1auVFWnAyxyfYYqTsJ_QKMROIX0vjPsDB584KTGnYjlXVQMAJNr2ytOFLQU7FnDRs8RLX3risX2X0SFaKY4s4c7xn4nwwA0V7qv-T3-FjbUkUpJh3rF1NZ-rWfCw7Uw3v993acgo05DMYzxJGQkxOPAkwhnSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75282217c2.mp4?token=hy5NqAbB8VWaQz7EO_1tiKBLLE0fw4crtVHAjE371HGgjjC306zgT2b0OAyJeQKBj7gZK26B2FttcHt7CLlzjiCl4ITABd3P_-0tRPaFc8vvztMGD1ltlDF9w8RldxRw82yGmOsGauTalkJ9V2KfBncFzHpA3AuWn2TKJddD32vxUkfXvwx9IfkOA1auVFWnAyxyfYYqTsJ_QKMROIX0vjPsDB584KTGnYjlXVQMAJNr2ytOFLQU7FnDRs8RLX3risX2X0SFaKY4s4c7xn4nwwA0V7qv-T3-FjbUkUpJh3rF1NZ-rWfCw7Uw3v993acgo05DMYzxJGQkxOPAkwhnSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌های جدیدی از رواق کشوردوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/463227" target="_blank">📅 17:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463226">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در منطقۀ اربیل عراق خبر می‌دهند؛ علت این انفجار هنوز مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/463226" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463225">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601da1c19b.mp4?token=R2-Vbdv4H5trCXQi8cd4fcU3xtSvSX-K8Wl3Sw7wpqKQPEKusCH6_J4E17dTE8frxVVKVE3H6lsZOZT3JmKtTX2w02-gHTArBVCJmBcmP3c1C8vCivZYfvBiKmXwLge6xVH8Y-j34NUYFPzNHY1pRWWs4MapUfFAEKK9Q3zkLa4OjHKefxIB-43bdK49FwGbflG0LOzQGj8JRfGArfBeaGLOJ5u8gBYF1SgqLh6GD0NWrMy53G8pdIYq4o3IEbMDktuyL4Y4bDsXH0xmTgXtWRsqfG8Us5koo9db2apkhR2BdXfWWFl_X49-l4goIryGO0VxBqesPvuQD7aRYB2rbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601da1c19b.mp4?token=R2-Vbdv4H5trCXQi8cd4fcU3xtSvSX-K8Wl3Sw7wpqKQPEKusCH6_J4E17dTE8frxVVKVE3H6lsZOZT3JmKtTX2w02-gHTArBVCJmBcmP3c1C8vCivZYfvBiKmXwLge6xVH8Y-j34NUYFPzNHY1pRWWs4MapUfFAEKK9Q3zkLa4OjHKefxIB-43bdK49FwGbflG0LOzQGj8JRfGArfBeaGLOJ5u8gBYF1SgqLh6GD0NWrMy53G8pdIYq4o3IEbMDktuyL4Y4bDsXH0xmTgXtWRsqfG8Us5koo9db2apkhR2BdXfWWFl_X49-l4goIryGO0VxBqesPvuQD7aRYB2rbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ پیش‌بینی‌ناپذیر برای آمریکایی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463225" target="_blank">📅 17:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463224">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq_GXdIdjB4Jjz4Xb2yatEz1d0E52AFjKG5-mRRgR3jygCqTjBrqSJVSmxZhh1TdNOt0OlxyqWo7LkyYf3RVtoFn3qLy2MxNoYJsh6-y3xOBlxvvPMGFYxhsvW0VnjwgCgIm8qzyVEvspBBTjrgrSFp3GkcXkfVm8gsjqCmA4eZ6zUH2VY9Ud0-1_bTc_gFVfCGWWtdNq5Xf0IYGB7MNGfCUYFohy64pdchLITIgUph5ai6I2LDoYrmOZd_k_VAFRc9NrOLDODYKd4Y4giAusXiKedYl4zxen74Qs1tDUrauv0dAVHTEUDf3TKZTUA6gBKVzC6TwvChvF-Otu8KAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای مامور نفتی آمریکا در ایران به ونزوئلا باز شد
🔹
با قراردادی که میان دولت ونزوئلا و شرکت توتال امضا شده، قرار است که پروژه‌های انرژی این کشور به این شرکت فرانسوی بازگردانده شود.
🔹
توتال همان شرکتی‌ست که با خروج آمریکا از برجام، بدون هیچ تلاشی ایران را برای همیشه ترک کرد؛ شرکتی که آمریکایی‌ها در موردش گفته‌ بودند، «به توتال ماموریتی دادیم که 16 سال به خوبی انجام داد.»
🔹
سال‌ها پیش رئیس‌جمهور سابق ونزوئلا ،هوگو چاوز در مصاحبه‌ای گفته بود: «آمریکا نفت ونزوئلا را می‌خواهد، تاریخ این را ثابت می‌کند.»
🔹
در زمان او قانونی تصویب شد که منابع نفتی ونزوئلا در مالکیت دولت می‌ماند و شرکت‌های خارجی نمی‌توانستند به‌تنهایی مالک یک میدان نفتی باشند و در زمان مادورو هم ادامه یافت اما این قانون یک ماه بعد از ربایش مادورو تغییر داده شد.
🔹
حالا بلومبرگ می‌گوید که طرح ترامپ برای کنترل اکثریت بخش بزرگی از ثروت نفتی ونزوئلا منتقدانی دارد که می‌گویند ونزوئلا به یک «مستعمره منابع» مدرن، مانند «جمهوری‌های موز» تبدیل می‌شود.
🔸
جمهورهای موز، کشورهایی از آمریکای مرکزی و کارائیب در اواخر قرن نوزدهم و اوایل قرن بیستم بودند که شرکت‌های آمریکایی تولید و صادرات موز، تنها محصول مهم اقتصادشان را در دست گرفته بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463224" target="_blank">📅 17:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463223">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">۱۰۰ هزار واحد مسکونی در صف وام ۸۵۰ میلیونی
🔹
مدیرکل پایش طرح‌های مسکن وزارت راه‌وشهرسازی: درخواست تسهیلات متمم ۸۵۰ میلیون تومانی برای بیش از ۱۰۰ هزار واحد در سامانه ثبت و متقاضیان به بانک معرفی شده‌اند.
🔹
حدود ۱۶۵۰۰  واحد نیز به دفترخانه معرفی شده‌اند و در فرایند پرداخت تسهیلات قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/463223" target="_blank">📅 17:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463222">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPLbl35WbJdZuML3fsH4WjdiHSsVupm9SrFz8zwv1kvCfBBVwfHzjgFYchuJAilyWKTJlkFVOX4e2Y4GDyfP4Mgfmk_MxIjDHlw1q0JGRIBbdC_YhAcsssCaOCy93HR9GtR6IgUngpKq9ZuTIqNaDactttlD7XXgNHaaoRsY6VqNzW3aQ1RBSQSp1OrwufrCUoFbc3HfsS5SBSWvM6TKK2pTuX8-tHzl9n7r69vxIDnRz0mBxK4sU4TCh8uTPgQVf4tS2J20KPGqAoNwVT52p_-T6d2WMH4-mSCCFeQ_X7V_LIqxlJ8IQnAVPFMRkEgensv3o4XrhDbOYvmIgOI8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری غیرعلنی عربستان با چین برای دورزدن دلار
🔹
عربستان اعلام کرده از پروژهٔ «ام‌بریج» چین، سامانهٔ پرداخت مبتنی‌بر بلاک‌چین برای کاهش وابستگی به دلار و شبکه‌هایی مانند سوئیفت، خارج شده است.
🔹
بانک مرکزی عربستان می‌گوید عضویت این کشور در ام‌بریج صرفاً برای انجام تحقیقات دربارهٔ ارزهای دیجیتال بوده و پس‌از پایان این مرحله، مشارکت آن به‌پایان رسیده است.
🔹
با این حال، فایننشال‌تایمز به‌نقل از یک منبع آگاه گزارش داده که ریاض با وجود خروج رسمی، همچنان به‌صورت محتاطانه و غیرعلنی با این پروژه همکاری دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463222" target="_blank">📅 17:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463221">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=qEGZVWsurcr43Df3gDd8ue8q8oAHPoL-7G005C28mGDOj6X9Dufi-hZUjTTM7n0ChKwv0iG7YbtQQ6B_fJGgQhssVKbXcJZziavzfkaOEza-stuUUzyxuhvEsRijUQCe6WikwU43I-iQUCbTQq6U_aQ6WL7cNygiW0iCTY8BiVQ9eVxjQdrqvjG_G2GYd9qiwezo3C3q8JI3Wji4zRg3w3dJQtxCDNhOrCMO3_1_GSz-3Nzvrt7w_Wp6id4OrP5Dk922sYYsVqHjLjwBRsJwpCzhPxy3NX240yAEegOgIebu-Ov5Fd_iidWsuzRbDFrXklzzyDkwR-oYWshKYVeVVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=qEGZVWsurcr43Df3gDd8ue8q8oAHPoL-7G005C28mGDOj6X9Dufi-hZUjTTM7n0ChKwv0iG7YbtQQ6B_fJGgQhssVKbXcJZziavzfkaOEza-stuUUzyxuhvEsRijUQCe6WikwU43I-iQUCbTQq6U_aQ6WL7cNygiW0iCTY8BiVQ9eVxjQdrqvjG_G2GYd9qiwezo3C3q8JI3Wji4zRg3w3dJQtxCDNhOrCMO3_1_GSz-3Nzvrt7w_Wp6id4OrP5Dk922sYYsVqHjLjwBRsJwpCzhPxy3NX240yAEegOgIebu-Ov5Fd_iidWsuzRbDFrXklzzyDkwR-oYWshKYVeVVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نویسندۀ آمریکایی: ما از منطقۀ غرب آسیا بیرون رانده شده‌ایم؛ به این معنا که پایگاه‌های ما دیگر کارایی ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463221" target="_blank">📅 17:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463220">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94640bf397.mp4?token=j-L1BO_0niodcqc6x5d6LB597G6rYkwtkeA3Eo_ajric30Su4gSaKQwU_VCvIbHLUPiy8G0ercyN8czGNFlP0Ybaf4GctvSLFkrXgGvCEwWhNfjcD18-8Uea6Utn_wDoj81KB5fDTVMhQx_W9ltLq9kden9kWFX0rb9HntXpFXDxxQ3IUEP8v74f6SaRuTZDjaggTtVntEB7oO8M_gHz-vBHG-ECjbbznwodBKULZxBfMJLJaUpE5Gw-DhjGpzLr6houA_AkgOgOVDczc68dawpkmVOW7VfsqRwUsiMKfyJ-Ge12iJfCjz2_SbHS0JmwTnCRl8jExY8iIBvcXezNlIqh-uRB9ZPhFCre69hxuAmIotRK5teNH34de6P-SOcSa8raQWhKO5q1xUUcEOCHQo9rwdqAkSAEv3pvPdGUdLASgDTzNM5hTweg6M2iXhb2et6lvnkQefUvP3I_bZex3rVihd4cH7qhiVb7asNWIM-bwPHyDpCDETavlkTqghyn5V5hdRLLxXzNuBOfgOOjG6yj99dUtV9-FhtwFIOGnw9-j2i_JtJSeCxk4bvSP1YQiVYBEEtZqjzyxogY1GPnFffHlpl6pVQ9rAICQg0e3S9S2XBOTUyBJAjRqP6M6K3dHBDpgjbvqwDvLndigtMmn0hZwuVkxky1t2hIFe_0-nY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94640bf397.mp4?token=j-L1BO_0niodcqc6x5d6LB597G6rYkwtkeA3Eo_ajric30Su4gSaKQwU_VCvIbHLUPiy8G0ercyN8czGNFlP0Ybaf4GctvSLFkrXgGvCEwWhNfjcD18-8Uea6Utn_wDoj81KB5fDTVMhQx_W9ltLq9kden9kWFX0rb9HntXpFXDxxQ3IUEP8v74f6SaRuTZDjaggTtVntEB7oO8M_gHz-vBHG-ECjbbznwodBKULZxBfMJLJaUpE5Gw-DhjGpzLr6houA_AkgOgOVDczc68dawpkmVOW7VfsqRwUsiMKfyJ-Ge12iJfCjz2_SbHS0JmwTnCRl8jExY8iIBvcXezNlIqh-uRB9ZPhFCre69hxuAmIotRK5teNH34de6P-SOcSa8raQWhKO5q1xUUcEOCHQo9rwdqAkSAEv3pvPdGUdLASgDTzNM5hTweg6M2iXhb2et6lvnkQefUvP3I_bZex3rVihd4cH7qhiVb7asNWIM-bwPHyDpCDETavlkTqghyn5V5hdRLLxXzNuBOfgOOjG6yj99dUtV9-FhtwFIOGnw9-j2i_JtJSeCxk4bvSP1YQiVYBEEtZqjzyxogY1GPnFffHlpl6pVQ9rAICQg0e3S9S2XBOTUyBJAjRqP6M6K3dHBDpgjbvqwDvLndigtMmn0hZwuVkxky1t2hIFe_0-nY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین مدال کاروان ایران به‌نام بسکتبالیست‌ها
🔹
تیم ملی بسکتبال ایران در دیدار رده بندی بازی‌های آسیایی۲۰۲۶ ناگویا، برابر چین قدرتمند با نتیجه ۷۹-۷۰ پیروز شد و به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463220" target="_blank">📅 16:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463219">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhLsaxweToInBiYsdyuCbKaIVAe4RBOUkEzNDe6RpQhBUqzQIS4mCI1Go6M6o7Dfv6in3Ol8jdGCbkiMIn1AfVuhqduCWhxv_4iNEDs2ckZGe0QsuZX589e2amhuSyKnGeEQ9WLaKydmru4zGiecCl3ncIb98qdVI6B3Eb1CvqxkqWabF2SJzlWbcj6AoyLT0Uf_ugEtbf6uZ3He0YhckGpCHOQJ51a4AfthD4tHZUUSNnshVkiA2w0mjNzNJ7lxnxmZSgIXCuptZHb-WIVtsuLoOMtktLrfLzQMkdAmFQ2bdR2LqwD5Q7Ojz14zuQ4g4sVwkjcmkSoed4GfFQhaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۵۲ سلاح غیرمجاز در خوزستان
🔹
فرمانده انتظامی خوزستان: در راستای طرحی ۲ روزه، ۱۵۲ سلاح غیرمجاز و ۲ هزار و ۹۱۶ فشنگ کشف و ۸۹ نفر دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463219" target="_blank">📅 16:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463218">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5Cc1mNWMwPm9InnHKto2zUMpN-huFRha6870Yuqo-e-EE9JjW9KlHYpG2rWanE4uDljPfkXr_vFKaV6zR_b9vfdayz8lzujjcTvO-S-haVC0txUyqeOPKzozcjb9sz51sl19CTxSe6bSTZ266VXM0eQdmWrRWh7G4b0UfXPe9OOeahVFe3L6gCZ3x76F87do2xVYbsrOz0OLJovERLDu-H0RRYdBS_hWr8_yEiNRyy9-YJ2CacA33szC1PJXJc92N0_smc8Clh8-uYBoUhhNRFi5_BpE1HLoxhWVL0fpb6JwNsrDPl_w9v9zvzE5xUv8-LTRXkCcTqSiDCeSUyzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند برای سربازی به فجر سپاسی می‌رود
🔹
مدیرعامل باشگاه فجرسپاسی: ستاد کل نیروهای مسلح اعلام کرده بیرانوند باید به باشگاه فجرسپاسی بیاید. هرچند با توجه به بسته شدن پنجره نقل و انتقالات تا نیم فصل نمی‌توانیم از این دروازه‌بان استفاده کنیم.
🔹
نمی‌دانم اعزام…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463218" target="_blank">📅 16:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463216">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تأمین‌اجتماعی: بازنشستگان نگران پیامک اشتباهی واریز حقوق نباشند
🔹
سازمان تأمین‌اجتماعی: پیامک اشتباه واریز حقوق شهریور برخی بازنشستگان و مستمری‌بگیران، ناشی از اختلال در شبکه بانکی بوده و حقوق کامل افراد امروز به‌صورت خودکار اصلاح و واریز می‌شود.
🔹
برخی بازنشستگان صبح امروز پیامک واریز حقوق شهریور را با مبلغی معادل معوقه یک‌ماهه مابه‌التفاوت افزایش حقوق دریافت کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463216" target="_blank">📅 16:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463215">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9XfP5xRqmOWHR9C6e8jeMKnw_FpBhRsFKXxLJIEYznenSlIR8AXY4xF4lnNops5rzES90KyxgL2Esu3RYRP6RE25eUhY2_9ejcPPib7skTYzu16VyVOmlzoc5idB4IzM1doEOADnawkiYl7k5HO1MD5_F-cYa90CqpsKxcz8Kpy1wlidUJfW_ORCZ0nCYii3sT0B_BJBMCUlxqeV9Ey9dKX5xTTs9YEoBIhJn74lQPl_v9P5UUiKAkM3WCeEb8LeGm5y37VEM-WNhH9XCeqWr_JWvW_SZ-YTv09VKdDV691zk9MgLfsusFFoNqW0EHKyrEAY7HdpoefFq4f7G2cFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پویش ملی «برای پدر، به عشق پسر»
🔹
مسجد مقدس جمکران از مردم دعوت می‌کند به‌مناسبت میلاد امام حسن عسکری(ع) و به عشق امام زمان(عج)، با انجام یک کار خیر برای همسایه، فرهنگ همسایه‌داری اسلامی و ساخت جامعهٔ آرمانی را ترویج کنند.
🔹
با ارسال عدد ١۴ به سامانه پیامکی…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463215" target="_blank">📅 16:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463214">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMDbGNiDmx9dU1PskewIt1mdcu1IDkFSN_SP5OOvJTGb1DD1XMymyrtnCDlsEHKikVVhUZOBdwyRwJc9Wjyew10kXZ66nSJgwpDnUOrIGsTMIR-wwIKTO9Ts5GSx_dxg-SuDy3PIIBtvIuXPoGWMC7reWbAWpPKbf_Bq3YH_M2Gw7hDL95l5b6rnTHaGF3dk03yEeLpwy0ch5XEE_-lyfK9GfESPUlBCdxyROCLybT7NNaAJBCzQjGn8HhAnOVxfVe7dvfjBORnYqbgHpYgtq9mERcwMXgmbdwv_t3_3T76z2R8hocWxyOryUwKYzDGp-81Nf1C00n1o-Xzno1INcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور یگان‌های واکنش سریع ارتش در مرزها
🔹
فرمانده نیروی زمینی ارتش: بخش عمدۀ یگان‌ها در مرزهای شمال‌غرب، غرب، جنوب‌غرب، شرق، شمال‌شرق و جنوب‌شرق کشور و به‌ویژه در سواحل مکران مستقر هستند.
🔹
یگان‌های مختلف نیروی زمینی، از جمله یگان‌های نیروی مخصوص، واکنش سریع، ویژه، مکانیزه و توپخانه در مناطق مرزی حضور دارند و از پشتیبانی‌های لازم نیز برخوردار هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/463214" target="_blank">📅 16:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463213">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0157fdfc1.mp4?token=NLGp0pZ7J7KiC7MtNnDxRZaM1r8OYkoi0l-TcO88lRXkQHxMhr9RkEf0TXW8YRnxz4j7Y26QAJAMEItk9O2_POzPtHcwquApb1ia-RdFp8aqRM6LWX3C99IqYWXH4pbDsvUNFD_wlN6b_9PfB5sAK1t1MKc50z2xXFo1qUbqN96ivDhDczVYAS8nN6tSMjLqtEVMnuR46Ie54EXg8GmZFs9Art6mo0H35U3Wsyt2uLhTtOk4YOTQ1SzlfyiHY8SJ2pYc9WzG58dpggq2gyvIbmIqOOWR-FUL6k_XeJgoMOiRSLuY9NNW5fqj_ugyt9w6IPv62NnTmS-eU5pNEGODQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0157fdfc1.mp4?token=NLGp0pZ7J7KiC7MtNnDxRZaM1r8OYkoi0l-TcO88lRXkQHxMhr9RkEf0TXW8YRnxz4j7Y26QAJAMEItk9O2_POzPtHcwquApb1ia-RdFp8aqRM6LWX3C99IqYWXH4pbDsvUNFD_wlN6b_9PfB5sAK1t1MKc50z2xXFo1qUbqN96ivDhDczVYAS8nN6tSMjLqtEVMnuR46Ie54EXg8GmZFs9Art6mo0H35U3Wsyt2uLhTtOk4YOTQ1SzlfyiHY8SJ2pYc9WzG58dpggq2gyvIbmIqOOWR-FUL6k_XeJgoMOiRSLuY9NNW5fqj_ugyt9w6IPv62NnTmS-eU5pNEGODQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دولت پول دارد زیاد هم دارد
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463213" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463212">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efe605c9d8.mp4?token=szXJsUAurIdIXCnWx8SxAQiyQFSnSYXL4YdVOI7L4ZyOmg7gsDOJ-8DKzE94mhN34500CeeovxoL7SS-SFXTAkPzjnD2OFMuF4gUB4StK5S4FrOUU5mMW-erOz8FrbVmWwHTW9FdmiAQg6ozUhampsJs93PQSQdO3_5hKR8f2wLvPqo6kZQCAI05qMU20tozUXdAduq6S41J7oQB6B1D-l7-jBMrJwOddm5nOxY-odQoNOT2YzHnhp3yRiwiyvfTxvFS_wLL3CVL7jk2nYaU6CXJO8xvpDSU80OxxRnTEZUznhgv9kW0x38RsK7FBX6_s0-UsbG1NG5unrCzMBTjVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efe605c9d8.mp4?token=szXJsUAurIdIXCnWx8SxAQiyQFSnSYXL4YdVOI7L4ZyOmg7gsDOJ-8DKzE94mhN34500CeeovxoL7SS-SFXTAkPzjnD2OFMuF4gUB4StK5S4FrOUU5mMW-erOz8FrbVmWwHTW9FdmiAQg6ozUhampsJs93PQSQdO3_5hKR8f2wLvPqo6kZQCAI05qMU20tozUXdAduq6S41J7oQB6B1D-l7-jBMrJwOddm5nOxY-odQoNOT2YzHnhp3yRiwiyvfTxvFS_wLL3CVL7jk2nYaU6CXJO8xvpDSU80OxxRnTEZUznhgv9kW0x38RsK7FBX6_s0-UsbG1NG5unrCzMBTjVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری ۴ اراذل در نسیم‌شهرِ تهران که مناز‌ل را تخریب می‌کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463212" target="_blank">📅 16:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463211">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1901b4bda3.mp4?token=vlE55Kck5O4VZRHqyskrO9HgaO3MeaKdkGM0BspBd-jzdPTrtw_JdwrEwZmIJjVtql6Fs7d0HmUz5wLBohsWRgZI4BY1-SKDqu9A11Zz67BE9Uguow5plX61W9mZfHJWEb-f5zZTwh6E2Z7h1f2FADTM3GeR_60Ok4pCycxVLRxgz4oJ11hUGSGHsB5_23iPNHgztYT9k3K6LKyeEd4wvpq34eqq8AdIOBattO0vpiZBsJBzCBsVnWJyI9ukTbDZ8lTiqpo6UknTd1e4uRxjQ3Y2GeeSV2fMKQ2gXqQ47RuGqIcsHUE9xIeTbUgTqGkLv7SRZ6gKGVXz33j84w4r66lx1DFzRAEbDc_tObxVsKR9ALR3EZMk6sGEXng3g3_Cq7VwR5AuXD2LscQgakgs_-PifbT8McSl0qSicHdut4_6-5h8fSevWOgqOrJKrlahf9r4Ru-EU4HLbVIv1HmqLklF98MBIrjrzqu-n7VJQrHc8-BlqL57Jy8WhRCgCkcxgdHvySnKwzMlGBDCgYZEe_s_uayXhRS4qZrtaRHzPzXd0drvhtr6ux76I7FOC_E2vsb-ySRFVvYvQ9aNTomaaMNAYP86h5HWrLZfVNx2ujMsmMt_3h1BOIjDvaPPnCVWAbgieXMeFqKWPI0q62Iyqxws0F6A5E9qzZvwlM0LHN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1901b4bda3.mp4?token=vlE55Kck5O4VZRHqyskrO9HgaO3MeaKdkGM0BspBd-jzdPTrtw_JdwrEwZmIJjVtql6Fs7d0HmUz5wLBohsWRgZI4BY1-SKDqu9A11Zz67BE9Uguow5plX61W9mZfHJWEb-f5zZTwh6E2Z7h1f2FADTM3GeR_60Ok4pCycxVLRxgz4oJ11hUGSGHsB5_23iPNHgztYT9k3K6LKyeEd4wvpq34eqq8AdIOBattO0vpiZBsJBzCBsVnWJyI9ukTbDZ8lTiqpo6UknTd1e4uRxjQ3Y2GeeSV2fMKQ2gXqQ47RuGqIcsHUE9xIeTbUgTqGkLv7SRZ6gKGVXz33j84w4r66lx1DFzRAEbDc_tObxVsKR9ALR3EZMk6sGEXng3g3_Cq7VwR5AuXD2LscQgakgs_-PifbT8McSl0qSicHdut4_6-5h8fSevWOgqOrJKrlahf9r4Ru-EU4HLbVIv1HmqLklF98MBIrjrzqu-n7VJQrHc8-BlqL57Jy8WhRCgCkcxgdHvySnKwzMlGBDCgYZEe_s_uayXhRS4qZrtaRHzPzXd0drvhtr6ux76I7FOC_E2vsb-ySRFVvYvQ9aNTomaaMNAYP86h5HWrLZfVNx2ujMsmMt_3h1BOIjDvaPPnCVWAbgieXMeFqKWPI0q62Iyqxws0F6A5E9qzZvwlM0LHN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اورژانس فقط برای روزهای آرام نیست
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/463211" target="_blank">📅 15:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463210">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_rZEOC0hncuwCoXik8Igy8lKxRhatuoTNkX81PwRJbxIM0_3xNXkesFjmB1ozzssiNr6R0lIhTj_S6EhZPwp8oGgLK-lCTLeFbrJoR9oKY0UuuwzwEyL7QnSGBhdZ0k8Ewh5i592u6ZeJa2n-nemd6W6EevkTNRP7gfKqNVhm4Z0hOADNnxKbGvbw-XCBbNz2EUg3c24B9FcpreFcU9NiLeaf7fk8E__31NI7QvPN9sw7K78IvrVSLXZarkRjuhh8mK2XErs92sZGtWVPRJsOtlZ1c1NnOkGdEM-6V_5Vd6y6DIfDWNLTqFmWcm1UllZ20qY7HNUAYDsmh6FOZROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان به نیویورک می‌رود
🔹
رئیس‌جمهور در روزهای آتی به‌منظور شرکت در مجمع عمومی سازمان ملل عازم آمریکا می‌شود.
🔹
رئیس‌جمهور ضمن سخنرانی در مجمع ‌عمومی و اعلام مواضع کشورمان در خصوص مسائل جهانی و خصوصاً جنگ آمریکا و اسرائیل علیه ایران، با سران برخی کشورها دیدار و رایزنی خواهد داشت.
🔹
آمریکا برای هیچ‌کدام از تیم رسانه‌ای و روابط‌عمومی رئیس‌جمهور ویزا صادر نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/463210" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463209">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0tA1p2h8qLQWbLENmfHMsW3pqyEvyUtJI3Duqp8C-zNl11qfInRAmL2ay6rKUN4wM2g4IY5hPA-NsXur6ZZFWOJXi2uUAGu12p_eTwKyowVx0IURhTjRg8cIeG6ZAFaOwlsdbIFv9xfmpy6OHvp6J-l1lX4ju2P9D0akGJWC1BGBmU5YTtCix22pPJP_Vv2YDI5WFSSjyo68KKyO37LJUjMpLGa81Ytx9jcEBwsnKcPHlxxrHGN6jduMKBlls7GRL4-uhuQpYwWjOyITWq1x4QXWfNkbkwo5loAjeJczv4UO1Mu66Qcl337bfncJdnctREpoScOgPOycUZCq8LF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  یمن: تأسیسات حساس ریاض و ینبع را هدف قرار دادیم
🔹
نیروهای مسلح یمن: ۲ عملیات نظامی موفق را با موشک‌های بالستیک، کروز و پهپاد اجرا کردیم: ۱. هدف‌گیری سایت‌های حساس در ریاض ۲. هدف‌گیری تأسیسات آرامکو در ینبع
🔹
هردو عملیات با موفقیت کامل انجام شد و آتش‌سوزی‌های…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463209" target="_blank">📅 15:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463208">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ورود ۲ دیپلمات فرانسوی به ایران ممنوع شد
🔹
وزارت امورخارجه: با توجه به فعالیت‌های خلاف حقوق بین‌الملل ازسوی ۲ مامور شاغل در سفارت فرانسه در تهران، وزارت خارجه این ۲ مأمور را به‌عنوان عنصر نامطلوب می‌شناسد و ورود آن‌ها به ایران ممنوع خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463208" target="_blank">📅 15:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463207">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVTB1Oabe1iE-r3k9rfTxr87szUcVUbBtrUnryyxl4ph1iVsJXqkVkpLsg7jys6DG_6x-w8IJuOXlhBAtTk2Q-7pJcRRxoDgm9gMkMzyWgkbsl5gKVPQSOQUR07tidXPfUewKnI1h1nuSYO5khHZZA4XGGLTr8A33KKDhFFUh4ZwkNgc6Z0bsxtz-rUoetj44Vmm82WUJJbVpER6u5Rm9aRN0uUmdsahWXByoA0qxXS422HcPlqEtwh07nEAqrWUAfdfYnNCjBca7a73pgaJM_1f-99GUqbAp8U0_sY_jFydZ9xXsUQu98WaLljB9W5-uU-QBfbY7_gWXDXJirVOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ راهکار مجاهد برای تبدیل ظرفیت «جانفدا» به نیرویی برای حل مسائل کشور
🔹
مهدی مجاهد، معاون پیگیری‌های ویژه دفتر رئیس‌جمهور شهید: حضور مردم در تجمعات شبانه و همراهی با پویش‌هایی مانند «جانفدا»، نشان‌دهنده یک سرمایه اجتماعی ارزشمند و آمادگی ملت برای فداکاری و مشارکت است.
🔹
این ظرفیت اگر به‌درستی سازمان‌دهی و هدایت شود، می‌تواند از یک موج احساسی به یک نهاد پایدار مردمی برای حل مسئله تبدیل شود.
🔹
محله‌محور کردن، ساماندهی داوطلبان تخصصی، پیوند با تولید و اشتغال، استفاده از ظرفیت مردم در بحران‌ها و ایجاد سازوکار شفاف برای ارائه بازخورد پنج راهکاری است که این ظرفیت را ظرفیتی برای حل مشکلات کشور تبدیل می‌کند.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463207" target="_blank">📅 15:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463196">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2ecc4eefc.mp4?token=O7coSU4ODaMtBPR7uyfvZiIOUAnX_wK8m5ZtyyxXcQqn7OpUoqDfbG-Acu4gO25RVyN7F9jfY5S4o3Zb0y7iRT02l5UM_K7ysgVHCxQQZOcfuFoARZMzTKuzJC8JLWURTa_Pf_9H8L9rFrkNjovdC_CWpoxOEvMEnPDwt1grqykyGTnlDdkPuYPzhuTlDkfqZagPSkVbf3Y9QlGiyIP4jiUDY2vfUk7v74YPRxrLW0Fhrg2P4VDOZMGqIVViqAvbVLFdRxQLgSWPnNPkrIHdHYfjXzxGXJxzdokTmeketmQspQzW4Dmyi9646Kt6o6U17hAy06fS5iQ-EYi4sF08GHXUE-_jwNJBYtpE8z0xe8HIcF14KeoNQfQuBCDHODQJel_AtEz1LJxoZDlfocmnH49rq7EvRrkF3vtlM30ivWcjcre5luH1iTHiU2dCLu5-S4pSQr27FtCt9nn3u2vRZkdWl1TWnLlR476DLSs-hr7S0r6UaOsiN7403QPHO_S0FvFTn6DWnstmoaulxINuz1etl8UjAXCQ1jTplvT-6LY1yPK8MCac9-xwjFQ5DmaDk9XAs1gP-4v9mpTWdtOjhIeI_UGbkJoBglQdHqIIAoR667x-aRBRwsNVD7z16QEf6yRdVWNVqfHA7cj1TpDipX0Qwq3SmYLuZ3kqF039ROU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2ecc4eefc.mp4?token=O7coSU4ODaMtBPR7uyfvZiIOUAnX_wK8m5ZtyyxXcQqn7OpUoqDfbG-Acu4gO25RVyN7F9jfY5S4o3Zb0y7iRT02l5UM_K7ysgVHCxQQZOcfuFoARZMzTKuzJC8JLWURTa_Pf_9H8L9rFrkNjovdC_CWpoxOEvMEnPDwt1grqykyGTnlDdkPuYPzhuTlDkfqZagPSkVbf3Y9QlGiyIP4jiUDY2vfUk7v74YPRxrLW0Fhrg2P4VDOZMGqIVViqAvbVLFdRxQLgSWPnNPkrIHdHYfjXzxGXJxzdokTmeketmQspQzW4Dmyi9646Kt6o6U17hAy06fS5iQ-EYi4sF08GHXUE-_jwNJBYtpE8z0xe8HIcF14KeoNQfQuBCDHODQJel_AtEz1LJxoZDlfocmnH49rq7EvRrkF3vtlM30ivWcjcre5luH1iTHiU2dCLu5-S4pSQr27FtCt9nn3u2vRZkdWl1TWnLlR476DLSs-hr7S0r6UaOsiN7403QPHO_S0FvFTn6DWnstmoaulxINuz1etl8UjAXCQ1jTplvT-6LY1yPK8MCac9-xwjFQ5DmaDk9XAs1gP-4v9mpTWdtOjhIeI_UGbkJoBglQdHqIIAoR667x-aRBRwsNVD7z16QEf6yRdVWNVqfHA7cj1TpDipX0Qwq3SmYLuZ3kqF039ROU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این مردم ایستادگی و اتحاد را در دل خیابان برای جهان معنا کردند
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463196" target="_blank">📅 15:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463195">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fcd4f50e6.mp4?token=YYwjhOJ_n-H7ssNA6xniFuBhjy7UQSI2ywqlDIr1I2s8x2AsNyGWgUquIzUOz6QVqi6ylrEqcv1F8VXWXsjbTeniW5X2Pbme0Cg0EMDJyjY1wNrsdqEg-OQSnbQx1pCkFLnQ_eBZ2rkmGqlMt1YPq2RsfOT1yH60rGsAJpaI8L-gAkrCfLUTHHU79-H7rxERlR8DhmcQ7Fs57fo3-Ic0D1FvmB7YHHqkzAsJWMsfbc5CQstvt5HW3R6V--lGMwT4kbZwmHOwQHkhHZbMZ5UcBUoORJxyZjEF_bWq5JOZHF00u6MvLOEB1DI4RNyNO6S0NZEjJGeMcVFL48hPMehS6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fcd4f50e6.mp4?token=YYwjhOJ_n-H7ssNA6xniFuBhjy7UQSI2ywqlDIr1I2s8x2AsNyGWgUquIzUOz6QVqi6ylrEqcv1F8VXWXsjbTeniW5X2Pbme0Cg0EMDJyjY1wNrsdqEg-OQSnbQx1pCkFLnQ_eBZ2rkmGqlMt1YPq2RsfOT1yH60rGsAJpaI8L-gAkrCfLUTHHU79-H7rxERlR8DhmcQ7Fs57fo3-Ic0D1FvmB7YHHqkzAsJWMsfbc5CQstvt5HW3R6V--lGMwT4kbZwmHOwQHkhHZbMZ5UcBUoORJxyZjEF_bWq5JOZHF00u6MvLOEB1DI4RNyNO6S0NZEjJGeMcVFL48hPMehS6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون آموزش متوسطهٔ وزارت آموزش‌وپرورش: معلمان در دههٔ اول مهر می‌توانند برای شرکت در کلاس‌های هوش مصنوعی ثبت‌نام کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/463195" target="_blank">📅 14:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463194">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzgSvS1qnq6RRpCqhwxz9yLZ1_KB3iiOPtzphVIdMPBdq6MHxfd8_i2VZ-uZwj5i6Y_PhChLZCeDJH9P-uU8qxxm-gY5vN0uB1HRUSXm8RySuvrooXmVjf7EDEliPDKMyqa58yCEJLBZxE-ZRAfXizIyJ-tAM_dcSy0MrCphjCQ_D_1DJXnygKx33hX3lqsqAB_PGjizgb4ydRntC4-5cSX8vDvXog5tbbfkOsDFXXfxHu9JmthgB2ZwLaD-WKYBlpghXZcvq7D3_ArdwM34lDh_mT8qTy4WGKzEdghOVmkFe52oQoBxvySOjnrNcuWb_H_nq4Vy-3i71sG2Ni1H3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلبان ایرانی اف‌۱۴: خلبان آمریکایی یا سرعت را نمی‌فهمد یا ارتفاع را
🔹
در گزارش شبکه آمریکایی «سی‌بی‌اس» از سرنگونی یک جنگنده F-15 توسط ایران، فردی که خلبان جنگنده معرفی شده، مدعی شده پس از اصابت موشک ایرانی به جنگنده و همچنین آسیب‌دیدن چتر نجاتش، درحالی‌که با سرعتی بین ۷۰ تا ۱۰۰ مایل بر ساعت (حدود ۱۱۰ تا ۱۶۰ کیلومتر بر ساعت) سقوط می‌کرد، با وجود شکستگی کمر، دست و شانه و آسیب‌دیدگی پا، از سقوط جان سالم به در برده و سپس خود را به ارتفاع حدود ۷ هزار پا (معادل حدود ۲۱۳۴ متر) رسانده است.
🔸
در مورد این ادعا امیر سرتیپ دوم حسین خلیلی، خلبان پیشکسوت جنگنده‌های اف‌ـ۵ و اف‌ـ۱۴ نیروی هوایی ارتش می‌گوید: «خلبان آمریکایی گفته با سرعت ۱۶۰ کیلومتر بر ساعت بر ساعت، به زمین برخورد کرده. سؤال این است که سقوط از چه ارتفاعی اتفاق افتاده، وضعیت چتر چگونه بوده و برخورد با زمین چگونه رخ داده است؟
🔸
به تعبیر من، گوینده یا معنای سرعت ۱۶۰ کیلومتر بر ساعت را نمی‌داند یا معنای صعود به ارتفاع ۷ هزار پا را.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/463194" target="_blank">📅 14:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463193">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e2ca13cb.mp4?token=XI_lgoJxiRFfcxV5qn_KMYO96znPTUekG7aV3xDcuRWU41kX7Ua2thxkKtZ2My4DYju3xqYpy2N5gl4oSjTatVgt9HEIxKSZalgE8JPsmFifTmtLB0gtDGJz7vWH1eYbqEsLAPJoy4n3xprHX0d9D51ZHQJuYwVVhgd34kiJYmLNQCz04lBYSyznmtq-laGEBSBk1nsXGsIEPlIL2riv-5_EKJcWck1La96BqqlFb1DNEnoMVJXFoHVnGgny0oXbHPeqKdNDGQJ8K6WXaHskXk-TaMou1P_EA3JM0OER7mB2udwgruaH4lxqalZacJawpFH3Oby7NNWULMZGwmrGMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e2ca13cb.mp4?token=XI_lgoJxiRFfcxV5qn_KMYO96znPTUekG7aV3xDcuRWU41kX7Ua2thxkKtZ2My4DYju3xqYpy2N5gl4oSjTatVgt9HEIxKSZalgE8JPsmFifTmtLB0gtDGJz7vWH1eYbqEsLAPJoy4n3xprHX0d9D51ZHQJuYwVVhgd34kiJYmLNQCz04lBYSyznmtq-laGEBSBk1nsXGsIEPlIL2riv-5_EKJcWck1La96BqqlFb1DNEnoMVJXFoHVnGgny0oXbHPeqKdNDGQJ8K6WXaHskXk-TaMou1P_EA3JM0OER7mB2udwgruaH4lxqalZacJawpFH3Oby7NNWULMZGwmrGMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیمت بنزین و گازوئیل در اروپا و آمریکا همچنان رکورد می‌زند
🔹
به‌گفتهٔ کارشناسان تبعات منفی جنگی که ترامپ به‌راه انداخته، بر اقتصاد جهان ادامه‌دار خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463193" target="_blank">📅 14:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463192">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d8158ff0.mp4?token=Ulxja3F5v3h1gxVNYhgXYU7ntvq7L-Zb1gT7TPjzSs6uSmBIWhfzi4JJ62paHoSH0KeXCA7lWCatkCPGNsQ9wAgtl4fvsqIW0hTtfIAqk0spd3XGRdkYKl3VOr5zPmzF94u7HCP8nHhabdGyWATqmOI4rOTy2yn3oSucvIaNWld49Dkjn7cSaEzGZm10eO1x4CeMc0wWJPBXp21jcLoCPy0DkhQrfP0-BvSfh914wTxp41P42kuJC894YHrYPSWPpWUNRwJh157pHkyQuluzrg3XGbKcQhTpfTp84kwtOkUEbwB-wdUmxdLfx5DdpqpIQIB7aqGrnshqFbrroVrkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d8158ff0.mp4?token=Ulxja3F5v3h1gxVNYhgXYU7ntvq7L-Zb1gT7TPjzSs6uSmBIWhfzi4JJ62paHoSH0KeXCA7lWCatkCPGNsQ9wAgtl4fvsqIW0hTtfIAqk0spd3XGRdkYKl3VOr5zPmzF94u7HCP8nHhabdGyWATqmOI4rOTy2yn3oSucvIaNWld49Dkjn7cSaEzGZm10eO1x4CeMc0wWJPBXp21jcLoCPy0DkhQrfP0-BvSfh914wTxp41P42kuJC894YHrYPSWPpWUNRwJh157pHkyQuluzrg3XGbKcQhTpfTp84kwtOkUEbwB-wdUmxdLfx5DdpqpIQIB7aqGrnshqFbrroVrkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چین ۹ ماهواره را با یک موشک به فضا پرتاب کرد
🔹
طبق گزارش رسانه‌های دولتی چین، این کشور ۹ ماهواره را با موفقیت با استفاده از موشک «لیجیان-۱» به فضا پرتاب کرد.
🔹
خبرگزاری دولتی شینهوای چین گزارش کرد که این ماهواره‌ها عمدتاً برای پایش محیط فضایی، پیشگیری و کاهش خسارات ناشی از بلایای طبیعی و انجام آزمایش‌های علمی مورد استفاده قرار خواهند گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/463192" target="_blank">📅 14:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463191">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0401ffdc.mp4?token=mbj9T2Wuyul4Tn7YXy4_TikTOysDqkiQaxL4VopV0o-hxaCxACTuhInGpJAYmj4lb5azc_OZaxu2ME8CFQeGHE4I6-33YKriMB14MpNfgjJuUMEwpuSdTwn_AqP4FZmuq23C0YeF7bB5Mz5WGJHV5O3CVKG5IWOBJxUM2TQ3UYITq9a7f7FqwV8XcMTfFts_0ReN24ZBoT0SnPeILjILfxzmNTUBajxBw1_mbCThXsIVHCyv6sNKfPNUwbT_yYhN8GK9nnDFums4AH22HBQQvxgUqjj-XWtFi7fC9ih8ZqtNu9LqEELUXssRSMcbpr66VzObR11X3NjxDICfYCbRLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0401ffdc.mp4?token=mbj9T2Wuyul4Tn7YXy4_TikTOysDqkiQaxL4VopV0o-hxaCxACTuhInGpJAYmj4lb5azc_OZaxu2ME8CFQeGHE4I6-33YKriMB14MpNfgjJuUMEwpuSdTwn_AqP4FZmuq23C0YeF7bB5Mz5WGJHV5O3CVKG5IWOBJxUM2TQ3UYITq9a7f7FqwV8XcMTfFts_0ReN24ZBoT0SnPeILjILfxzmNTUBajxBw1_mbCThXsIVHCyv6sNKfPNUwbT_yYhN8GK9nnDFums4AH22HBQQvxgUqjj-XWtFi7fC9ih8ZqtNu9LqEELUXssRSMcbpr66VzObR11X3NjxDICfYCbRLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت ۱۰ داروی بیماران خاص تحت پوشش بیمه که از نیمهٔ شهریور صفر شده بود
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463191" target="_blank">📅 14:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463188">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
هشدار قرارگاه خاتم‌الانبیا به آمریکا و کشورهای منطقه: اگر خطا کنید هدف حملات دردناک قرار خواهید گرفت
🔹
براساس اطلاعات دریافتی، آمریکای جنایتکار درپی پوشش شکست‌ها و دست‌یابی به دستاوردهای کاذب در جنگی که با اتکا به دروغ و صحنه‌سازی صهیونیست‌ها آغاز و با فریب و حیله استمرار یافته است، بار دیگر تصمیم گرفته با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران اسلامی را از سر بگیرد.
🔹
هشدار می‌دهیم چنانچه آمریکا علیه ایران اسلامی خطایی مرتکب شود، تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.
🔹
اخطار می‌دهیم چنانچه کشورهای منطقه با تداوم سیاست دوگانه در قبال جمهوری اسلامی ایران، با تجاوز شیطان بزرگ به ایرانِ اسلامی و مقتدر همسو شوند، همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.
@Fasrna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/463188" target="_blank">📅 14:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463187">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qg-Ss3QUqDl3kdIGsc-IQRcsZdEyHpeMGTaiYm6K1DPyqAsmp7D9Pj7X9_xSSWyx_hQYPrpJD8P91URR1SECE-T9zqvRYP0KfeyAnqHcEypH4vjAY_JLaZp0q3KZXeMfl6OF9oS2ValRKM7ds-CwKYTnDmQ_sEQaw08vt6vdRqbAKcZ1wJOu11vruf3vaERadxyUnoILEdxCYwD0uaW5EundGY_FNMEHLK0Nwqe5UDnvD7H8KS0flkXamjaRs3fVCMf9hk4PCrWMTt64XXzF_BXK2fYGTv_9R8z-0gCkkJ7uqg79NuiICyoIeoH6kr28_RMrym60xSKRLIF8xHGgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرهاد مجیدی، گزینۀ غیرمنتظره مالک نساجی برای نیمکت
🔹
پس از جدایی مجتبی حسینی از نساجی، گمانه‌زنی‌ها درباره گزینه‌های جانشینی او آغاز شده , در این میان از سعید دقیقی و محمد ربیعی به‌عنوان گزینه‌های اصلی هدایت نساجی نام‌برده می‌شود.
🔹
شنیده‌ها اما حاکی از آن…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463187" target="_blank">📅 13:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463186">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh0J4gJFP0D7X1encWaLOgiWpsPFvnXPK3LApreheuN-o8NVLKy42EUVHSxO191J_K1apwq98pKDe_1W5PgsEsQde4J12xS2FSmKsbtGjJWbjNcqihvawYi_SThTjqBKjzf6oj5mX_ywjT9lPFLWJ3GKXibwGbP2b7hB4b2MQk_fCGzHg1iECDTnTeC0MKiRlM0RxDw0Xi1D4kqCK5thpDA2LlZS7y6yo7z1tUM-b9QlmPSWxPM4Q2MgUAbd9R7fP1Tr_8SB_Vpi9tp12N7W9enugq6kAGyhJzmdHVEZ_4bqdVYV9j_ISi92wHvEUtbRuzt8xFvyXlgx1LEqx_hAlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار شریف: سرنوشت صدام در انتظار ترامپ و نتانیاهو است
🔹
مشاور فرمانده کل سپاه: دشمن پس از شکست در نبردهای میدانی، مجدداً به اهرم‌های تکراری تحریم و فشارهای اقتصادی روی آورده است؛ مسائلی که ملت ما در طول ۴۷ سال گذشته با آن‌ها زیسته، آن‌ها را مهار کرده و از آن‌ها عبور کرده است.
🔹
اکنون بحران قیمت حامل‌های انرژی در آمریکا و اروپا به‌دنبال این جنگ، غربی‌ها را وادار به پذیرش شکست در مقابل مقاومت ایران خواهد کرد.
🔹
به برکت مقاومت و شجاعت مردم و اطاعت از رهبری، همان سرنوشتی که برای صدام و رژیم بعث رقم خورد، در انتظار ترامپ، نتانیاهو و همۀ حامیان آن‌ها خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463186" target="_blank">📅 13:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463185">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwJkcoTMUxzENTA7kPJWGtJs5t_LHdXHFWefdsvc0pgCTR3_eXC0SmSpvAASssfPIdGMQIaT9Kyqei8cJd5E1Kgoxjt3NyOmFXz_fN6uWTal2ufn374XoqRcvNtCPZ_LqkOHOJKFwXywQ4c2QfWAqBtRTvBoykY2igIkkCvnKpzyZgNRtlbjr1BilHCj3p4h86U0TM5ps9sYLIe3rU4XhQTY4JqaSR6W4xTviuQahBVZfM9JxK3Jxk2f4GtstKTEKQgt2xPOoTOjp-6GvvNbRE0G-NBNmpBLzAgpmZocG0zlee7mY4H0lnau_udQLu7FzOY6mYGrqUEVmPm8mjAKgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بازسازی لگوییِ پیروزی‌های یمن، از المخا تا باب‌المندب  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463185" target="_blank">📅 13:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463184">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWV3-ybEv7qv_A9TKvaCIvyRTZd_yptEIkEiiGVM0b6WIVSV58G5v_sQ4vLr_fZJeuXZFSJzir3EyNydCrNJkb8Fl68_U-TszOo-ZCRTHvPUuJCa2n8kzuHYpRe0wx98ITxc14keBxiDDn5NU6ZTrTgebNXKbQrdM9r8ok28VIAHc0Z5sEYVYlasCJHR6LFD1KweU_Y8XoIij7PeTEoP3X1-YmCGMV923Lku8vmoTARiyw9eZ53gRsDr18ain0vbA8XTe0hcv0GJDKWP_bqFPkxLffDnQMFo2JhnQCzEYSMn3fc3sQetSaXan0nDyMNDYQs-UvK_Kv73aZHr1bJdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد دولت از شرکت‌های دولتی تقریبا هیچ بود
🔹
طبق اطلاعات رسیده به فارس با وجود برنامهٔ دولت برای واگذاری صدها بنگاه، درآمد حاصل از فروش شرکت‌های دولتی در ۵ ماههٔ ابتدایی امسال تنها ۳ درصد رقم مصوب، یعنی ۱.۵ همت، بوده است.
🔸
این درحالی است که کل درآمد پیش‌بینی‌شدهٔ امسال از واگذاری شرکت‌های دولتی ۵۰ همت بود.
🔹
بررسی دیوان محاسبات نشان می‌دهد ۱۳۴ شرکت که ۴۰ درصد شر‌کت‌های دولتی را تشکیل می‌دهند، در مجموع ۴۷۲ همت زیان دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463184" target="_blank">📅 13:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463183">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2KvlfNdLwKRMLTxDtt_z5JN_oKWR0_dnyxMVODHmNGCDqd7F7JB0383kFa4aG1td7jGPy7PjqAyhDw6_Fn-UTxkLri-NDWRA_Q127ENBiF3VeC88Eq_1Tr7BolK77nhPbeElvFIwwS31dJ337KPXF5y4zTdEhj97somtpGWAXoskMkhNUmDMBKVBqlNw6XKNczHVYG7ZV5aTMXQNolg7vyXvcccvArVeua-TG7kmqLju4L-uFgOpOGIcRlmfUgPo21-wvtYhakAy9KGfF_jh35ZeQf4EYAVkY9h8GsDyZ9AkxyZEe9g5LvNVz37TjlHRtHJ1VZ8smJt0mPyFEyzlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام ۳ کانون عملیاتی وابسته به گروهک‌های تروریستی
🔹
وزارت اطلاعات:
با مجاهدت‌های خاموش سربازان گمنام امام زمان(عج) و با بهره‌گیری از گزارش‌های مردمی، عوامل سه کانون عملیاتی وابسته به گروهک‌های تروریستی مزدور دشمن آمریکایی صهیونیستی که قصد عملیات ترور و تخریب زیرساخت‌های اقتصادی را داشتند در ۳ استان کشور به هلاکت رسیده یا بازداشت شدند.
خلاصۀ موارد اشاره شده به شرح ذیل است:
🔸
۱. هلاکت عامل عملیاتی گروهک تروریستی تجزیه‌طلب که مترصد ترور یکی از فرماندهان حافظ امنیت در شهرستان پیرانشهر بود.
🔹
طی اقدام پیش‌دستانه سربازان گمنام امام زمان (عج) در اداره‌کل اطلاعات استان آذربایجان‌غربی، یکی از عوامل عملیاتی گروهک تروریستی تجزیه‌طلب که قصد ترور یکی از فرماندهان حافظ امنیت در پیرانشهر را داشت، در کمین سربازان گمنام امام زمان(عج) گرفتار و در درگیری با نیروهای حافظ امنیت ث، پیش از انجام ماموریت شیطانی خود به هلاکت رسید.
🔸
۲. به‌دنبال رصدهای به عمل آمده توسط اداره‌کل اطلاعات استان البرز، یک مزدور وابسته به دشمن آمریکایی-صهیونیستی به نام «امیرعلی_ ن» که در راستای اجرای دستورات سرپل گروهک سلطنت‌طلب وابسته به سرویس جاسوسی رژیم صهیونیستی، قصد انجام اقدامات خرابکارانه داشت، با الطاف الهی و مجاهدت‌های سربازان گمنام امام زمان(عج) در آن اداره‌کل، دستگیر و از اقدامات خرابکارانه او پیشگیری به عمل آمد.
🔹
این متهم با هدایت و آموزش‌های مختلف گروهک سلطنت‌طلب، مشخصات برخی افراد هدف گروهک و مختصات برخی از اماکن نظامی سپاه و بسیج را برای دشمن ارسال نموده بود.
🔹
تخریب پایگاه بسیج در منطقه، ربایش و اقدام ایذائی نسبت به  افراد، آتش زدن خودرو و.... از  اقدامات برنامه‌ریزی شده توسط گروهک تروریستی برای این مزدور بود که به لطف الهی پیش از اقدام، پیش گیری به عمل آمد.
🔸
۳. در ادامه سلسله عملیاتهای پیش دستانه‌ی سربازان گمنام امام زمان (عج) دراداره کل اطلاعات کرمان، یک هسته سازمان یافته و مترصد گروهک‌های تروریستی وابسته به سرویس های جاسوسی دشمن آمریکایی-صهیونی شناسایی و اعضای آن پیش از هرگونه اقدام ایذایی، بازداشت شدند.
🔹
این هسته دو نفرۀ تروریستی از سوی سرپل گروهک ماموریت داشتند یکی از تاسیسات زیربنایی و مهم شهرستان بم را منفجر نمایند.
🔹
همچنین از سوی گروهک به اعضای این تیم ماموریت داده شده بود که برای دیگر اقدامات مسلحانه و تروریستی، این هسته دو نفره‌ی تروریستی از سوی سرپل گروهک ماموریت داشتند یکی از تاسیسات زیربنایی و مهم شهرستان بم را منفجر نمایند.
🔹
همچنین از سوی گروهک به اعضای این تیم ماموریت داده شده بود که برای دیگر اقدامات مسلحانه و تروریستی، کسب آمادگی نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463183" target="_blank">📅 13:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463182">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464f9314.mp4?token=WTpS-7Cs-Di6NNrDBbOWtwlt9i9b0bVAXyfLtEGwqXyqph8CAPAo_IdVP9JjN_NBaN--x5qOvWKd2meyK6JEcByDyTdmUq2A5AIPHEAZ7WsEcx55tlIGyd_qoo23ZDY93QdcBuyER3WPdunIMmKrw4BSBXu_3Kwr_TLcJXWEjDron6NbpPbr5Ot-2HEr-xD4tV4Ega_HhzH5_h-oWkDymvJkv90AEPgvKfE0XoNLPh10a8yfulwVUybAtCf6lfjoD2_TtkxLXvYg9WdKsUigM-5cmBZQ0nE6QltSkxPX3gMM3jSI74yz8d911sMJj7MQx23ksWYUU7LVb5HotnLf_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464f9314.mp4?token=WTpS-7Cs-Di6NNrDBbOWtwlt9i9b0bVAXyfLtEGwqXyqph8CAPAo_IdVP9JjN_NBaN--x5qOvWKd2meyK6JEcByDyTdmUq2A5AIPHEAZ7WsEcx55tlIGyd_qoo23ZDY93QdcBuyER3WPdunIMmKrw4BSBXu_3Kwr_TLcJXWEjDron6NbpPbr5Ot-2HEr-xD4tV4Ega_HhzH5_h-oWkDymvJkv90AEPgvKfE0XoNLPh10a8yfulwVUybAtCf6lfjoD2_TtkxLXvYg9WdKsUigM-5cmBZQ0nE6QltSkxPX3gMM3jSI74yz8d911sMJj7MQx23ksWYUU7LVb5HotnLf_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین مدال کاروان ایران به‌نام بسکتبالیست‌ها
🔹
تیم ملی بسکتبال ایران در دیدار رده بندی بازی‌های آسیایی۲۰۲۶ ناگویا، برابر چین قدرتمند با نتیجه ۷۹-۷۰ پیروز شد و به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463182" target="_blank">📅 13:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463181">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133a7497ee.mp4?token=WB4oQsXD54UzNRF3qr-yjJpzuxW5CT6gz-ke8sZn1nBKekgdAg7i6inEjzTOaQ1dMP2w5eglaFpyO2QasjHBK-dC6tj7YvFu16ve8h3mxv_taS2DWxxTg-pyUojrXDPK12nRg5UsVUCjMAVToUlAe7Vl_1uZfPPDms-siCpfFWHHB8QyGcEC8ERqRco8d-hJ-JfN29TgzTyCM8yAGbUMVJqL71GCAwN8gZKUfT0vDMd5s4QdAT0u3xOGtuhOe2N3Ll2ecdKXfjcae_QbXSyapOIVYIRO4X5EF9GdFaxMYySOAjvhTWbSNtgW8O2OFPShCmJvbusD_EoSvLZ5KPMg46n9evwA9WFt2W7SCCi73KSMqKw3ACDull7agOGl9N_4QEhm6UpaszDycXl2GNvtwBiblRSNPvbQ3KifumZjQndPlfpiYMAWO38zDSjcXO3WJdvOu4ZyUnMbZGpCOd5OLH7CWUi4iNp6nfGtv_dXLQ0IecdiyvX4dmYF5POzor4cUuc_vpz5f00Ql6otQFZdZd2vYGNSeOZWZTJ2UKn9V3sAt8Ry_CI-YCgLrjNpCMq5SyxcJaAHWLzvR_OaJcLMY3HwIdRJ7LaHFF92B2cfSCu2mXH7dfhMbQpvyZjb9GjvQAy99BakA4jp-N2ejCo_Y-LrI2OeHUryk1z7Xc-c3Fk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133a7497ee.mp4?token=WB4oQsXD54UzNRF3qr-yjJpzuxW5CT6gz-ke8sZn1nBKekgdAg7i6inEjzTOaQ1dMP2w5eglaFpyO2QasjHBK-dC6tj7YvFu16ve8h3mxv_taS2DWxxTg-pyUojrXDPK12nRg5UsVUCjMAVToUlAe7Vl_1uZfPPDms-siCpfFWHHB8QyGcEC8ERqRco8d-hJ-JfN29TgzTyCM8yAGbUMVJqL71GCAwN8gZKUfT0vDMd5s4QdAT0u3xOGtuhOe2N3Ll2ecdKXfjcae_QbXSyapOIVYIRO4X5EF9GdFaxMYySOAjvhTWbSNtgW8O2OFPShCmJvbusD_EoSvLZ5KPMg46n9evwA9WFt2W7SCCi73KSMqKw3ACDull7agOGl9N_4QEhm6UpaszDycXl2GNvtwBiblRSNPvbQ3KifumZjQndPlfpiYMAWO38zDSjcXO3WJdvOu4ZyUnMbZGpCOd5OLH7CWUi4iNp6nfGtv_dXLQ0IecdiyvX4dmYF5POzor4cUuc_vpz5f00Ql6otQFZdZd2vYGNSeOZWZTJ2UKn9V3sAt8Ry_CI-YCgLrjNpCMq5SyxcJaAHWLzvR_OaJcLMY3HwIdRJ7LaHFF92B2cfSCu2mXH7dfhMbQpvyZjb9GjvQAy99BakA4jp-N2ejCo_Y-LrI2OeHUryk1z7Xc-c3Fk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین مدال کاروان ایران به‌نام بسکتبالیست‌ها
🔹
تیم ملی بسکتبال ایران در دیدار رده بندی بازی‌های آسیایی۲۰۲۶ ناگویا، برابر چین قدرتمند با نتیجه ۷۹-۷۰ پیروز شد و به مدال برنز دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463181" target="_blank">📅 13:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463180">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBX3-fiotyLq3rtAOtOeR5fSagifBiYk_QleoXIwtGss0YZ1TFxDOQO1sdhoUYHdBKWI8CYcczeU8OjIDZZmXY4dNi-2AV3uNxw-W48A9J9SWkxatPIDHfOyXF9PGb7ZjglUeSup-uuDb3Rm0E7UstvslkK066n0hA0N1qzmjXr6R1AlvEfim6hUZ3j4EhTyw8-8Lz19VhBtf7Tbgdt-9Te3bG6QwNNyp93uh1PPqCnp6VxMslu0pqc0MxPVTjtlHC8Ih3th9ziere48-LKGCuOv80jmk3ZdYZ8t3EYYlbyPqxfQHTU7Xs_AyNNMT3V92glq0x26LyMJnZYy-nfdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس از ۷.۳ میلیون هم پایین‌تر رفت
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۵۷ هزار واحدی به ۷ میلیون و ۲۹۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/463180" target="_blank">📅 12:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463179">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477de95318.mp4?token=f_EKZ5xQoTS4cjvbkrd1GgF_5DloaNIAb3xpa0SJ933vkpumzfddckKH-EbJiCZsaMPkgAdjn-t0kFc0LTJFs-C82BDCmHybdYBwi1ixg5wqcS8Jy-ky8K0YD3d2lFFJhuIQthgxvfuJ7cCSgjhavJ8F11gQASIo16D1bSSuh81Dxpwccj9Jt-P8f4hAXF6XIQT_ZZ731IuTxbpq6qO_PrF_Zp7ZHtbdHwGpQxTLqtqFNZ1aAxQuSE928wUWJPYD-HTvADF6-AoQJ4GNOKffKqADS417Crkpb5kmFBNAhEusbYf34geCl-bvWej6pFemJZcY81Ns3FJAtQW_w83IFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477de95318.mp4?token=f_EKZ5xQoTS4cjvbkrd1GgF_5DloaNIAb3xpa0SJ933vkpumzfddckKH-EbJiCZsaMPkgAdjn-t0kFc0LTJFs-C82BDCmHybdYBwi1ixg5wqcS8Jy-ky8K0YD3d2lFFJhuIQthgxvfuJ7cCSgjhavJ8F11gQASIo16D1bSSuh81Dxpwccj9Jt-P8f4hAXF6XIQT_ZZ731IuTxbpq6qO_PrF_Zp7ZHtbdHwGpQxTLqtqFNZ1aAxQuSE928wUWJPYD-HTvADF6-AoQJ4GNOKffKqADS417Crkpb5kmFBNAhEusbYf34geCl-bvWej6pFemJZcY81Ns3FJAtQW_w83IFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ سوژه تمسخر نخست‌وزیر کانادا شد
🔹
در بحبوحهٔ تنش‌های تجاری آمریکا و کانادا، نخست‌وزیر کانادا با تقلید حرکات دست ترامپ، حضار را به خنده انداخت.
🔹
کارنی که پیش‌تر بارها هدف طعنه‌های رئیس‌جمهور آمریکا قرار گرفته و ترامپ از کانادا به‌عنوان «پنجاه‌ویکمین ایالت آمریکا» یاد کرده، به‌تازگی همزمان با تشدید تنش‌ها با واشنگتن، بر تقویت روابط کانادا با اروپا تأکید کرد و پنجشنبه در سخنانی در پارلمان اروپا از پیشنهاد اتحادیه اروپا برای پیوستن اُتاوا به‌عنوان عضو وابسته استقبال کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463179" target="_blank">📅 12:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463178">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هلاکت یک صهیونیست در تیراندازی در کرانه باختری
🔹
در پی عملیات تیراندازی در نزدیکی نابلس در کرانهٔ باختری، چندین صهیونیست مجروح شدند و اخباری از هلاکت یک شهرک‌نشین صهیونیست هم گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463178" target="_blank">📅 12:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463177">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ممنوعیت استفاده از سهمیۀ ۲۰ روزه تردد رایگان در هفتۀ اول مهر
🔹
شهرداری تهران: استفاده از سهمیه ۲۰ روزه تردد رایگان در محدودۀ کاهش آلودگی هوا از ۱ تا ۸ مهر ممنوع است.
🔹
تردد ناوگان پخش مواد غذایی، دارویی و حمل اسباب منزل از ساعت ۶ تا ۱۰ صبح از ابتدای مهر ممنوع است.
🔹
همچنین در هفتۀ اول مهر هرگونه عملیات عمرانی در سطح شهر که باعث اشغال سطح سواره‌رو می‌شود، لغو خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/463177" target="_blank">📅 12:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463176">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph3Z7DhtaJWt1Jp3QgiCoYzdJurMOdJ6ATSE1yHjuiN6_DBmQX7vxBJQWGXaEaOyQY82Yhr4OjsXuU5FiOnPWfjMRcTq7PPf7Wbk-dtdAqvMPlrNAZ2qQx63xca24Rc29A3kPETwCdc047zT0DDVb7FxOMq7QGAe9XW8gA5IB7H0Qj51beLQGgKdtjt-T_neiV1QdPNShgtqZClyxdF4QdiyEbNOG6IWSJ1s99HV_6MmiCADanffYr8fCHwOytr3aVry72i2CEG09E4csNgVOWJBUFsmLwh8yhkAWBhTwvbVvomVw1CDc-8-Pe-F1XVtKdgAUEHpRrlDUvn8sm9dXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای رئیس کمیسیون قضائی مجمع تشخیص ماند
🔹
در جلسۀ کمیسیون حقوقی و قضایی مجمع تشخیص مصلحت نظام، حجت‌الاسلام محسنی‌اژه‌ای برای پنجمین سال پیاپی به ریاست این کمیسیون انتخاب شد. کدخدایی هم نایب‌رئیس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463176" target="_blank">📅 12:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463175">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b1d8a308.mp4?token=SGxRh6DRuqP89aSqEydFBsw2RGEADStOjdRUWqJRoRFkHcATHj__S2CzcZLO6Sksy4bISa6fak0VweqIM43PzWaGrPK8KTbrqfPDwFhUo7ItvhqqofxyQIVd47pcbSl30e3LjklHrEhb6G-yVYU0IGB-Y6Rl_2krEqxzfIh5wBqOOnE39sR4ZhPQDfhbXdOcJr2M7z5oBYU3BTJC3vM_s-Tk5O2a02GnUbtoJIzkBevQ8DLPBPvQs5LSGGsufEVrFrDANx4wPMjeQgQCi0MWAilRJMzsmBMzrfq3kb-lHVw9RsXHZGu8I9K0d1Ek96cNqjijSOLphvCF7423nvoPdixeCFNev84TxlS0CFu0VNn2aONH103C9SwOUS3uBxbBwhIxneyHPvTEn1kMIOisa3KuYOx1ngqgtmzfo9CYELDuqC9JIwxU2_E164WmJIcONui2mKN26z9-vsP2b1sk0D3VmZFjbOLbf07ewjAgmEqzDE-qTkXD9HOAI7RAA6_r7SHvB5tnzP5_HnXuThHo370oCtQxhM2imyfjPr_9NtwwpuVJRNmj4qlHFCcWdlvag00RzHmYNQG7htWP0rkXmw48VUSPpAjTNRFFfhmtwQZjgcWElqhYck9Z1xXtOjcuzTLKYJG0ptEKOugmCdQNTSX9nYgoATTwsvmS4W7XK4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b1d8a308.mp4?token=SGxRh6DRuqP89aSqEydFBsw2RGEADStOjdRUWqJRoRFkHcATHj__S2CzcZLO6Sksy4bISa6fak0VweqIM43PzWaGrPK8KTbrqfPDwFhUo7ItvhqqofxyQIVd47pcbSl30e3LjklHrEhb6G-yVYU0IGB-Y6Rl_2krEqxzfIh5wBqOOnE39sR4ZhPQDfhbXdOcJr2M7z5oBYU3BTJC3vM_s-Tk5O2a02GnUbtoJIzkBevQ8DLPBPvQs5LSGGsufEVrFrDANx4wPMjeQgQCi0MWAilRJMzsmBMzrfq3kb-lHVw9RsXHZGu8I9K0d1Ek96cNqjijSOLphvCF7423nvoPdixeCFNev84TxlS0CFu0VNn2aONH103C9SwOUS3uBxbBwhIxneyHPvTEn1kMIOisa3KuYOx1ngqgtmzfo9CYELDuqC9JIwxU2_E164WmJIcONui2mKN26z9-vsP2b1sk0D3VmZFjbOLbf07ewjAgmEqzDE-qTkXD9HOAI7RAA6_r7SHvB5tnzP5_HnXuThHo370oCtQxhM2imyfjPr_9NtwwpuVJRNmj4qlHFCcWdlvag00RzHmYNQG7htWP0rkXmw48VUSPpAjTNRFFfhmtwQZjgcWElqhYck9Z1xXtOjcuzTLKYJG0ptEKOugmCdQNTSX9nYgoATTwsvmS4W7XK4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند نکته از زندگی امام حسن عسکری(ع)
🎙
حجت‌الاسلام دارستانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/463175" target="_blank">📅 12:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463174">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e46656a27f.mp4?token=EV1480Tf6A-0Am2vNjQ3n6BwuyAkI9at1kxst8723pE0g5Uzk1UfhdNwb1jH-edgpQ7bAgAmeptUv2lQbW-p32ket1YXMFgplFgkKSzq3CVsPaf-zkPDihVR8sgNivKXBVEWu6XpFKIf1578DLTP8lNmah3Isfzy69y2oPXWkp_o-ygkSvgBzqrTJbkZactbfDhsoPYsi8IR7FsJU3n_KFSLZ0DdiT-hVoHROoNeSTjHkuN6Q_fFP0yGLcoaR9-haOcRnEcrRaScM3bJ97FsEWP9MzwQl6626lbz_KQzGHnScyW3m73yz3fDS54b8ZSGpXZ1fVNL4_OzN47oBoSOPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e46656a27f.mp4?token=EV1480Tf6A-0Am2vNjQ3n6BwuyAkI9at1kxst8723pE0g5Uzk1UfhdNwb1jH-edgpQ7bAgAmeptUv2lQbW-p32ket1YXMFgplFgkKSzq3CVsPaf-zkPDihVR8sgNivKXBVEWu6XpFKIf1578DLTP8lNmah3Isfzy69y2oPXWkp_o-ygkSvgBzqrTJbkZactbfDhsoPYsi8IR7FsJU3n_KFSLZ0DdiT-hVoHROoNeSTjHkuN6Q_fFP0yGLcoaR9-haOcRnEcrRaScM3bJ97FsEWP9MzwQl6626lbz_KQzGHnScyW3m73yz3fDS54b8ZSGpXZ1fVNL4_OzN47oBoSOPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرماندار مریوان: یک محمولهٔ سلاح قاچاق در مرز باشماق کشف شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463174" target="_blank">📅 11:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463173">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYrlN-I6ZpvWWxxS84zeL5eNSQ73A5YukMsNMMq1qN0nGlMYieUHYK5SKY31m9uj7oxS2Z7CQBEjU_4v3rEdJ56Mhhcd-tulnOFOzIhtv-BU9jrBEdXEEsKF5yNE1X0Xjakriwy0mmCTizqqaLDaLZTO0lkdND2e2Xp8QFfmOD72GEr3Scz_aME9uOKmDtwI3Lwi-Cwi-vjigEgkGzJ8xK8P-t4ZbVQF73DYq7MUZiuMKR1hv5tcoBrgReNqGFYTMe4AzTqh1Lopo4lE7dOORK_JIMfQT0Yh3mD_6U2-eqBn4leUAgpHCdGO01tJPQdJtBMVNAw6cTo4dyGz-zt27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف یک مزرعهٔ ماینر در البرز
🔹
شرکت برق البرز: در یک مزرعهٔ استخراج رمزارز که در پوشش صنعت فعالیت می‌کرد، ۳۶۲ ماینر کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463173" target="_blank">📅 11:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463172">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1113bc549.mp4?token=nAXdvCD5BGEZI4YlRibK6V1Xk0Weq6w2XVIiov6Cgg-M0S2kbWhyeim9GmFGTG-daqxUjGTM0VKD_CzILj2iKHDwzFYpqtUFUsIE2s7QWzStmNM8Y1bjMGWxIfRy3iFlwaPZ3nxIlyN3hbmVLyCtMjHlOj7MJN23huObY0bpY_tGIKNrs3i6ZSTkisjw7NpjcmgVxe3bbw2_xAR4PDxRmZx4r1WO503sb28vODbTdlVhPkapUk98hI4jtST6WXkIoy4M6_lxWPK4XgyRmrlwzxekksz11TtLq7IdvxqK40Iuo9nPzVpbeosPl0cCDMUr5fJH5ErHR6E4fsrHFDKFwKMcGUM8cDBrAecNUQ66YHeUFJ5faGC2J5dqllP0ciCgconeQbnFBvvTcQ6KVHcV29Ncsw4BqRE6-FveE3nD135CKpEWm3iKYP-Gnxw0l69qbZk-pIP6mbCDwFYf8MLQBKg-wLM-iTmOl1w0AzXr4ILTChuYY7UlprCqCiS9GoqTc4uscFCS1CdK2edC_V2mmnfH90S8ulYpBJ_iAcwP7-xpnSqN_lPVoll8gVm_y4bOE0-HAatQQxfgiKkLzA9xueskkJVjGRK_eJ-PH0nctIrbJQQP2ajXqlqCw2NcX4vyAaTEsP7nklpkkvJ41NHHazRf03qzBRDLQxuY24_Llic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1113bc549.mp4?token=nAXdvCD5BGEZI4YlRibK6V1Xk0Weq6w2XVIiov6Cgg-M0S2kbWhyeim9GmFGTG-daqxUjGTM0VKD_CzILj2iKHDwzFYpqtUFUsIE2s7QWzStmNM8Y1bjMGWxIfRy3iFlwaPZ3nxIlyN3hbmVLyCtMjHlOj7MJN23huObY0bpY_tGIKNrs3i6ZSTkisjw7NpjcmgVxe3bbw2_xAR4PDxRmZx4r1WO503sb28vODbTdlVhPkapUk98hI4jtST6WXkIoy4M6_lxWPK4XgyRmrlwzxekksz11TtLq7IdvxqK40Iuo9nPzVpbeosPl0cCDMUr5fJH5ErHR6E4fsrHFDKFwKMcGUM8cDBrAecNUQ66YHeUFJ5faGC2J5dqllP0ciCgconeQbnFBvvTcQ6KVHcV29Ncsw4BqRE6-FveE3nD135CKpEWm3iKYP-Gnxw0l69qbZk-pIP6mbCDwFYf8MLQBKg-wLM-iTmOl1w0AzXr4ILTChuYY7UlprCqCiS9GoqTc4uscFCS1CdK2edC_V2mmnfH90S8ulYpBJ_iAcwP7-xpnSqN_lPVoll8gVm_y4bOE0-HAatQQxfgiKkLzA9xueskkJVjGRK_eJ-PH0nctIrbJQQP2ajXqlqCw2NcX4vyAaTEsP7nklpkkvJ41NHHazRf03qzBRDLQxuY24_Llic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازسازی لگوییِ پیروزی‌های یمن، از المخا تا باب‌المندب
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/463172" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463171">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlaFnictlJwL0UQXtqGv56orTMJp18OmoKGXPKxm0ylFDbog0W4V0-zmdeezGRZzkwwnKT9JWEa8H5vpwl210oL3qOAxYSz17r8VFze3kKBUr9r4m1cKKi5MWN4k6QTqfJVChWF8sCtch4DWA5Eom7_9QqhbJs5NllFCF3mOBZz_pBEKBvCYr8Nh7RUXqcbyZPSbPOxVH3ljF2AhphHy72Hir8ogj9TtUBa5CFWuP3cJRnGHQ6MtQg1G3kVAfhGhqKOyCmgEIEmHhcJCQO2Z78zte6mZOFKPp3Wa8MdNs9emSgoe41ro-qEJ6e4p7uKrJ3U0FeyUwLD71GPB-B8zcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انتقاد دربارۀ عملکرد دولت در تئوری ساده است
🔹
ارائۀ پیشنهاد و انتقاد درباره عملکرد دولت در تئوری ساده است، اما در میدان عمل، به‌ویژه در شرایط خطیر کنونی، با پیچیدگی‌های فراوانی همراه است.
🔹
دعوت از همه برای مشارکت در حل مسائل کشور، یک باور و رویکرد…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/463171" target="_blank">📅 10:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463170">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byjdOSd2TGH8-tAoFIH19FMk5WbSPgnQezsH585IiIpHdQnB0_oj6cvP9yjz-BPC6lPWaGPjCDZL6WOLlizRkQX5vWnhh5MH2wsxm8Bp73ZuUQ_hycvRwsiAvKLzDu2L3N3ktbAHmZSNh9hfOje9UiuclXs2DaLnmfCD3EYOYWBVHBcERPVtppLIoNOg-PTGI7xyHnr7EbNsYtV9koPg42qj6VZpj6ULBKMxhafgdq6BsXE-zJ3L6k4ss-xp9CPQS3-j6PwUYcU0i9MkiYIuJUO92h7Afvip8sWhuIrQCPO4aJMFa3wEcCeSLNKrH4DR_JTVM51LzamojdxW_0r8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انتقاد دربارۀ عملکرد دولت در تئوری ساده است
🔹
ارائۀ پیشنهاد و انتقاد درباره عملکرد دولت در تئوری ساده است، اما در میدان عمل، به‌ویژه در شرایط خطیر کنونی، با پیچیدگی‌های فراوانی همراه است.
🔹
دعوت از همه برای مشارکت در حل مسائل کشور، یک باور و رویکرد جدی در دولت است و صرفاً به ارائه پیشنهاد و راهکار محدود نمی‌شود؛ بلکه مشارکت باید به مرحله عمل، اجرا و پاسخگویی منتهی شود.
🔹
امروز دولت با وجود بدهی‌ها و مشکلات به‌جامانده از گذشته، محدودیت‌های موجود در صادرات نفت و هزینه‌های ناشی از جنگ، ضمن پرداخت تعهدات و مدیریت هزینه‌ها، روند توسعه کشور را نیز متوقف نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463170" target="_blank">📅 10:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463169">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378421841a.mp4?token=orXjZENbQzfjNVfwaQr0RKfTISL3JRItNWInGf3h3lb_hVozeZ-u2Svgnz-iU0dQyia-GGnADlF_EEF2jX44HfZIVQ-ost2SIGhsFDDjQQ8bYyJzUKGTNAcTf_awB1opMhV_RI1r19D5jQKU4hWAdvcuJIiN9fS2K-4YIvv-sNF5fNDbnSe_8U2o4iN6ePJiZWQczkGlgQAmHCiuchf87JuJ8peNdcacq1cyxOUvlM2y2j1srZyHObrxMnGmkGU7xIILmyqkXEMHo3vh3OGru86TlwOW9Xb6zK-zD5_j8XUhXl_dMouDGD7yJWSjIHaCxWGxztM3wOxJnQVVDhVyNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378421841a.mp4?token=orXjZENbQzfjNVfwaQr0RKfTISL3JRItNWInGf3h3lb_hVozeZ-u2Svgnz-iU0dQyia-GGnADlF_EEF2jX44HfZIVQ-ost2SIGhsFDDjQQ8bYyJzUKGTNAcTf_awB1opMhV_RI1r19D5jQKU4hWAdvcuJIiN9fS2K-4YIvv-sNF5fNDbnSe_8U2o4iN6ePJiZWQczkGlgQAmHCiuchf87JuJ8peNdcacq1cyxOUvlM2y2j1srZyHObrxMnGmkGU7xIILmyqkXEMHo3vh3OGru86TlwOW9Xb6zK-zD5_j8XUhXl_dMouDGD7yJWSjIHaCxWGxztM3wOxJnQVVDhVyNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ اوکراین به پالایشگاه نفت روسیه
🔹
صبح امروز پالایشگاه نفت مسکو در منطقۀ کاپوتنیا در پایتخت روسیه پس از حملۀ گستردۀ پهپادهای اوکراینی دچار آتش‌سوزی شد.
🔹
پیش‌تر ترامپ گفته بود از زلنسکی خواسته به پالایشگاه‌های روسیه حمله نکند، زیرا این اقدام عامل افزایش…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463169" target="_blank">📅 10:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463168">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLM45JB3RfAGOY2qojE3hxNXpY_vXGcbOtsKlxcZJr_qeoM1qg5HTi436n07IbC7n3L9cJni25FXdvuNcJpU83R4Z9KRDQhqflzf8oynWdncHR3ygQH6eJtLraFggFaNZDkbn2Lc6QGXJwEhtqmMurNl_2fYJVfTbA-Er5KQlJnUarIFKMsn-FWwFOw2p4aHV17-nwb0xzdCdqi4VbULDNH0KX96kJw3FZtdHMENl47ewpVIHPzf_ocuYobDq-b5l8iaLyXjz0NAU-NgFeC4Um2c1FLCQH27CbVJ2utdp5svpST-50TuYk9NHuYIasidsiXzpU6Flz91v3Vfw1bLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ حال عمومی آیت‌الله شبیری‌زنجانی مساعد است
🔹
براساس پیگیری‌های خبرنگار فارس از یکی از مسئولان دفتر آیت‌الله سیدموسی شبیری زنجانی، هم‌اکنون حال عمومی ایشان مساعد گزارش شده است.   @Farsna - Link</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/463168" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463167">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npvK5VcVA-ehNejHUlA9X6flvg3QSco1MhEJbIHCjkNJhGmmPy9fLBxaLYWUBhh6aPwB0073Wjum1p6ct27yWEFgcKJoNtOVGRU3qZhzmPHSeV7Pd-QnSw81Auq-q5GAMQgJy5jpVDUMZQKa9jCXTOE6xhF3fkMRXSBe5PFULLvCz9fMfUo9ZuXxJ5pkqBKaejKU0SL82g9U2J2_ouzfY5pg4oL2wLFZC6B7qUPkUjI4-7yuiXi8CAYOfBA9m16lfStldMkhg88HboIMo9YQ99yaLwVmLfQmQ_4ZTbAhFyTJgeZZZlUPN5kxGld-jB5VVWeZX3t7CrxR8-9vDvCJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«شفرونی» بعداز ۸ روز رفع توقیف شد
🔹
برنامه «شفرونی» که ۲۱ شهریور با دستور قضایی از ادامهٔ انتشار در فیلیمو بازمانده بود، پس‌از چند روز به جدول پخش فیلیمو بازگشت.
🔹
«شفرونی» پس‌از پخش ۳ قسمت از فصل جدید، در پی اعلام جرم ساترا و ورود دستگاه قضایی متوقف شده بود.
🔹
حالا قسمت شب خوزستان این برنامه در دسترس قرار گرفته است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463167" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463166">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a76ce8106.mp4?token=CUS47fw1Z6ADV0tG-zSLoJFgQzLqfAy693GLGf6v3Mn3Rn2hCRQKL5ZI3kaJLtrLpPs_bXwZ_UyWUwLzKTjiFGI7dMJxz5NJ_q64ZU3ZCAGLgSQjOUwTtf8XDAvpI3a_jMB61lkCywAkHP400Ld31rD48KAERK811oQ-JjYk-AlzT23MTLvFT7JunA29lP3N-fv6stmdL-LuqDik_ztYngftX550yJRJgK55eVfv6-A9Aj76peUPXF196EXW0TTVPOcuO7NcZBAaJaGyBp3-myej7nFr4Lw-g-4iK3lJ_LHd76gAtoExd6QZqrCpvdN6DfXB8jyULXtaGkTOqkrTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a76ce8106.mp4?token=CUS47fw1Z6ADV0tG-zSLoJFgQzLqfAy693GLGf6v3Mn3Rn2hCRQKL5ZI3kaJLtrLpPs_bXwZ_UyWUwLzKTjiFGI7dMJxz5NJ_q64ZU3ZCAGLgSQjOUwTtf8XDAvpI3a_jMB61lkCywAkHP400Ld31rD48KAERK811oQ-JjYk-AlzT23MTLvFT7JunA29lP3N-fv6stmdL-LuqDik_ztYngftX550yJRJgK55eVfv6-A9Aj76peUPXF196EXW0TTVPOcuO7NcZBAaJaGyBp3-myej7nFr4Lw-g-4iK3lJ_LHd76gAtoExd6QZqrCpvdN6DfXB8jyULXtaGkTOqkrTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کرنر خطرناک برای ایران که گل نشد
⚽️
ایران ۰ - ۰ چین @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/463166" target="_blank">📅 10:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463165">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy8YaUs82CsQyRb5U3qcPcWkGxJD5abq4ocTsyAc3pdNevwo8GySInF7H0B2jyIJEw-z1F3OEegphRsps1g9h9ziTl6M4MArmswWQZsCNdu6ihBDG8UyYGKppmoPBA1QQdfDYhrBIfxgQqfJLhQE2bsN9JXR0FPD8BjKFSVhAuMVV3vqQwLCMfdlh3bkpSQpRe1_omK-QgC_2H-39cyAjmTp6LYnFepFPqq033xClNIJuFUA0UgJFtZKvBHWSsl7HxEajNljx0DgUKixBzyu0FV9OzLeDZyUnQni1BlDJVBY0LaCKPwavlj1VpSLPV5ThRABrutGtiSX21dCySEr9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مدیرعامل سازمان مهندسی و عمران شهرداری تهران: بزرگراه یادگار امام به بزرگراه ساوه متصل خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463165" target="_blank">📅 10:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXvGLwZ3Imf1UIjYIo42XFY-tXiXhgEdhvu20PPrHbYzc-IdIZzL3m9paxdEDsS3tUd8Vge1I768NlVoPF2JRZAQRAm49nnp_4k5EoxjxewLuUon4ppVI2Aa68a78YEll4QWU-LpRB3vMMd3rNQzKxioO4J8BvjzmNpGB0utcCo432bXS2uvbKraoa7rSs6l6JtJro_MFasq17_xQfYYoEsPChbBcaz4N5Q39XgwhXAR2Ayw0jla4Z6K3yndE9xOWo4PHkmBsgAbocc0DZaEzbvgQmESehWqvQ36suavCAgKvSQxnRca8j9cFLbnGmNQQYX8fBZgzmWYY_c70DCOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌های حوالهٔ ارز در مرکز مبادله اعلام شد
🔹
دلار: ۱۶۶٬۶۰۷ تومان
🔹
یورو: ۱۹۱٬۳۶۸ تومان
🔹
درهم: ۴۵٬۳۶۶ تومان
🔹
یوآن: ۲۴٬۸۶۰ تومان
🔹
روبل: ۱٬۹۷۸ تومان
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/463164" target="_blank">📅 10:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463163">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فرمانداری دزفول: صدای انفجار شنیده‌شدهٔ دقایقی قبل در برخی نقاط شهرستان، مربوط به امحای مهمات بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/463163" target="_blank">📅 10:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b183bb2e0.mp4?token=cfvppSxfLUlpEmd3pxjAmJSTBn0TR986g2YCXf2nCvM3D1uZYsJqCumMLR5qye28ct_P7yZc2xHIhO9wnOD5VKTLszI1TXd0jFcTyWWj0p7FSJquCXf1ibeNY5yKWi85fgAnjDN4eF2sWaSe9bNqU0rROcJPJbl8UOEY8RjCGpFdB9nksqcE3vJ9iN0xocNNUoOphYhC_yq4F1D8bDqqW7eVrwgfHkQcgev7Hx2gsu-pnEjJRPyWKCEYnagvVj1lWdDPc70pRv8-V6enyv39lk305xrbJSWWWLhhuxQaZagwlMY-Q-M-PGRiyp7QyzgxIXFF22NgoS35AGUdHmYXcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b183bb2e0.mp4?token=cfvppSxfLUlpEmd3pxjAmJSTBn0TR986g2YCXf2nCvM3D1uZYsJqCumMLR5qye28ct_P7yZc2xHIhO9wnOD5VKTLszI1TXd0jFcTyWWj0p7FSJquCXf1ibeNY5yKWi85fgAnjDN4eF2sWaSe9bNqU0rROcJPJbl8UOEY8RjCGpFdB9nksqcE3vJ9iN0xocNNUoOphYhC_yq4F1D8bDqqW7eVrwgfHkQcgev7Hx2gsu-pnEjJRPyWKCEYnagvVj1lWdDPc70pRv8-V6enyv39lk305xrbJSWWWLhhuxQaZagwlMY-Q-M-PGRiyp7QyzgxIXFF22NgoS35AGUdHmYXcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصدومیت عباس کهریزی که منجر به تعویض او شد
⚽️
ایران ۰ - ۰ چین @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463162" target="_blank">📅 09:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463161">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c466f62b4f.mp4?token=jfZk7kaZfZCMxiuvJjdpYnbG6RRgWdvoD5cZyC8d3KWMWhWhLmRjoXnyrvYUoInjM49Qlyc_7h22NmAY4DHdkZYH7fjFzEzrLfG11jRpKWsZOeC0VVwszbor4CW5CsStH3k_fCgxvH-9XeWlL2_aBdxkysdHg5aK-jllL6uw_RagvadC4WTOYW-yDpVwev9vnQWTPmylpcL-g8E-kKnoSSIeiDpfQvk59Ye9pz2GbqK1jMtxXd2cMsPCSKpABoMEweRqEzwrpnDT6Ip1qKYdeASw5k1SfeCL0IJnAy6KSulT8G852eEqJ_NfaF37XjUPP9c5Zz4kW8hx4ekW7aTIEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c466f62b4f.mp4?token=jfZk7kaZfZCMxiuvJjdpYnbG6RRgWdvoD5cZyC8d3KWMWhWhLmRjoXnyrvYUoInjM49Qlyc_7h22NmAY4DHdkZYH7fjFzEzrLfG11jRpKWsZOeC0VVwszbor4CW5CsStH3k_fCgxvH-9XeWlL2_aBdxkysdHg5aK-jllL6uw_RagvadC4WTOYW-yDpVwev9vnQWTPmylpcL-g8E-kKnoSSIeiDpfQvk59Ye9pz2GbqK1jMtxXd2cMsPCSKpABoMEweRqEzwrpnDT6Ip1qKYdeASw5k1SfeCL0IJnAy6KSulT8G852eEqJ_NfaF37XjUPP9c5Zz4kW8hx4ekW7aTIEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: تا محقق نشدن شروط ایران، تنگۀ هرمز باز نخواهد شد
🔹
امروز در صحنۀ‌ دیپلماسی  مواضع ما کاملاً روشن، عقلانی و غیرقابل‌معامله است.
🔹
انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده و دشمن به‌خوبی می‌داند که مسیر فریب…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463161" target="_blank">📅 09:54 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
