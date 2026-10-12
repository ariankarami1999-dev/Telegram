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
<img src="https://cdn4.telesco.pe/file/Z5vcp_n5lZ7RwExGaDUUb4meZGTeh__6tifoF5qod44DicENwkVnm73wD9uFpuey7ZPFNkPQ_7P8JVUtlhCs0IIgPI9Drib2-2Rz5eYVTSytiwt-NwmmG6qmCfUZq3mjagMp0JI269gkz9TXmyCPh-Pyu17xQrjH93_vni8qmL4qa1QHcNdzHxLjEd5PDAUb2rFe-nZl8KI4gPkB1zDL6RgvFlq8zOwONNNlfJ69wUNlNwEDg1Xmd_nxhTlNAAJ5jUx0ll3n27a-gwsnn_rIuX8CwbCDBmbJICUvbWA0gzunMO_dDRw5ZsLnmGfCU1KuIT7IMjdqhmBEMsxCJIqgXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 11:11:52</div>
<hr>

<div class="tg-post" id="msg-152248">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
شبکه عبری کان : حدود ۲۰ فروند هواپیمای سوخت‌رسان آمریکایی از ایالات متحده به اروپا بازگردانده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/152248" target="_blank">📅 11:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152247">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فلایت رادار: تعطیلی فرودگاه ریاض تا ۲۴ ساعت دیگر تمدید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/152247" target="_blank">📅 10:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152246">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وال‌استریت ژورنال: حملات حوثی ها، رؤیای اقتصادی بن‌سلمان را تهدید می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/152246" target="_blank">📅 10:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152245">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea561a653.mp4?token=qyaDaaxl8n_JfXr65T6oQwDMig-JZwrD7t8ej9ClbJ27tO1QcgRo2MZQ7xnDZGfROoDwf5Ex41Qtq0LTr1cVQ4pUmIjpBWo6BrGGdrwJjVAfCUUwVrHXSWYEJ2fh_cHzWfXlZvgcyMh5GLl-OE1B-i1BgN7HGYg0oIWRzcfgEyZPtwpsrUqFXkywyXk6DgDnVLsTGiPwM5kubKPiBfX4UBeb0QjCTde1hYaKpk77at-45oRkCnvYwHy0hckAwj_ODKUeY9pugxCMnk_y-KmUqkzKGx_anhljQQhSX_dsC69xiiFgSULXWGxdiyN5ON6-OzuFyt3NeYSY7CEnEyOl4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea561a653.mp4?token=qyaDaaxl8n_JfXr65T6oQwDMig-JZwrD7t8ej9ClbJ27tO1QcgRo2MZQ7xnDZGfROoDwf5Ex41Qtq0LTr1cVQ4pUmIjpBWo6BrGGdrwJjVAfCUUwVrHXSWYEJ2fh_cHzWfXlZvgcyMh5GLl-OE1B-i1BgN7HGYg0oIWRzcfgEyZPtwpsrUqFXkywyXk6DgDnVLsTGiPwM5kubKPiBfX4UBeb0QjCTde1hYaKpk77at-45oRkCnvYwHy0hckAwj_ODKUeY9pugxCMnk_y-KmUqkzKGx_anhljQQhSX_dsC69xiiFgSULXWGxdiyN5ON6-OzuFyt3NeYSY7CEnEyOl4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در واکنش به پذیرش نظرات کارشناسی گفت: من مگر دیوانه‌ام که اگر حرف درستی را به من بگویند و من نپذیرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/152245" target="_blank">📅 10:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152243">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e416bb3da2.mp4?token=HjRW6bzHHu64p02fXSAECNpm7YcH0dcaQAN0UksfHeVbGq1AJ4HTLGlG9LxiB9AicJ22WCINrdZ13hjPlCC_N8Jj5mpLLM-0x_fYLwlHXlhCbnERcN7cZFWMWlrDHQhyEJO4pipua5nXDAAaq8lDL1ZG7QSu4UdPH6WvZJPuzYOx6gHJ1Gx_LfuYdVzFLkP7h4qIY9PPAbAL6MxNQzZqOZHeEotmA-y3djFjjpvN_ldI1otUgXIG_BUpxTpU0h9MAXHTp-F6p4FDcxnN_7er_f-csKp7PyIcbmnZlQeChB4QEc_042Oz_XLW-BnORS2bFsl8qul2VBuQQhmTn42EHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e416bb3da2.mp4?token=HjRW6bzHHu64p02fXSAECNpm7YcH0dcaQAN0UksfHeVbGq1AJ4HTLGlG9LxiB9AicJ22WCINrdZ13hjPlCC_N8Jj5mpLLM-0x_fYLwlHXlhCbnERcN7cZFWMWlrDHQhyEJO4pipua5nXDAAaq8lDL1ZG7QSu4UdPH6WvZJPuzYOx6gHJ1Gx_LfuYdVzFLkP7h4qIY9PPAbAL6MxNQzZqOZHeEotmA-y3djFjjpvN_ldI1otUgXIG_BUpxTpU0h9MAXHTp-F6p4FDcxnN_7er_f-csKp7PyIcbmnZlQeChB4QEc_042Oz_XLW-BnORS2bFsl8qul2VBuQQhmTn42EHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ماهواره‌ها، وقوع یک آتش‌سوزی ناگهانی در میدان نفتی الشیبه در عربستان سعودی را ثبت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/152243" target="_blank">📅 10:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152242">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0d54ab6a.mp4?token=eRs130UelUZE2aswi9p0QqNsKJeRPU8Kri51_7HHHKT6gbZNGO6Z5MNUDxX1APEi6YbJX7MMNjh70eNlNXmjAk0IZjj4orwVeDo_VKcths3X0AQG4GFanDdnH0DFNifXa8MfXt_z8ttTLFBDZbpNw2Cd5jTOrU80SIMyv9JUCZCha_I0qsdusz-F7eaUWJFQ3U13R3PHpiLfMLwcVaUpy3jjbf70gjoZri-x2R72clLYva--vdekAkNBn2xNdHbQZAkgqPtdnqwdeRVLeOdwEwpleNAphDvmje0kuQPPY4OgROePPj_IFDOuipPfP02fizY-Zad09swrrzpLz73RWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0d54ab6a.mp4?token=eRs130UelUZE2aswi9p0QqNsKJeRPU8Kri51_7HHHKT6gbZNGO6Z5MNUDxX1APEi6YbJX7MMNjh70eNlNXmjAk0IZjj4orwVeDo_VKcths3X0AQG4GFanDdnH0DFNifXa8MfXt_z8ttTLFBDZbpNw2Cd5jTOrU80SIMyv9JUCZCha_I0qsdusz-F7eaUWJFQ3U13R3PHpiLfMLwcVaUpy3jjbf70gjoZri-x2R72clLYva--vdekAkNBn2xNdHbQZAkgqPtdnqwdeRVLeOdwEwpleNAphDvmje0kuQPPY4OgROePPj_IFDOuipPfP02fizY-Zad09swrrzpLz73RWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: داریم در تهران آب زیرزمینی را استفاده می‌کنیم و اگر تهران هم با همین روند رشد کند از کجا باید آب بیاوریم؟!/ باید برای حل این موضوعات چاره‌اندیشی کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/152242" target="_blank">📅 10:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152241">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ_d9BZHCPh5HTr29J9XUPZ-21CqBEh5rmLcLRL3xV0UaGx2ENDrBii6pBpBRcC0Sd1qqcfbg2D81Z6TVvYG-F3Do26uA-ItIhBC8x7SqCBTolhCM67icHRHaPrW6rUyC-WTTCDzFVy2VkW-pq24RyqH35LdOcow9YNNJybRxfETve3efl6xUUfukaXrHeKxI1N2ZA7OFei_x-aGTfJtjMV_Kf_tDZObGiG8Mv8UhZhoyNv_ZIEJa7dx3Lia_9x5mAFS18MYWFoiWu9GNUCxvyVvpR1Bqrg1BOWNKYqfonBrim7Pt5LUfReJtzW4WIdqCOpiH9fPHzwsBKSEGAjwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عبدالمکلی، وزیر دولت رئیسی: اگه گرونی رو بزاریم کنار دیگه مشکلی تو کشور نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/152241" target="_blank">📅 10:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152240">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3f945f51.mp4?token=Mq83lrT3kM4JrIC6ZiUbaWr0hLouk0BnSdcKyzZ1XRGMv9hGu6jiV5FSKKFKLCKYzF7-kJ-dAkLPcAxpclW422oFMIipHehIkJ_yn4QIJAJ9hmXEwsOVM5EWE0RGJdGcOKVZe8UZ6GgJf0aqfL7M6iT95eU8Fm51-WE4MGtex1JMJK1a2QAAT__CK5Am2KjkbukmlxoLcue0hr4v6k35LApXLFmNvue2CeXR69lkdK0wTdV9dnK_fgkb4Cyeypdtd8MhS7rgmAl737d_wSrFYxSTBvc5LcCpjf8y0d5Z4gIANrlVqXTzQD6jt9O_QUuI-oXXqiK58NtO6U3NQysfLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3f945f51.mp4?token=Mq83lrT3kM4JrIC6ZiUbaWr0hLouk0BnSdcKyzZ1XRGMv9hGu6jiV5FSKKFKLCKYzF7-kJ-dAkLPcAxpclW422oFMIipHehIkJ_yn4QIJAJ9hmXEwsOVM5EWE0RGJdGcOKVZe8UZ6GgJf0aqfL7M6iT95eU8Fm51-WE4MGtex1JMJK1a2QAAT__CK5Am2KjkbukmlxoLcue0hr4v6k35LApXLFmNvue2CeXR69lkdK0wTdV9dnK_fgkb4Cyeypdtd8MhS7rgmAl737d_wSrFYxSTBvc5LcCpjf8y0d5Z4gIANrlVqXTzQD6jt9O_QUuI-oXXqiK58NtO6U3NQysfLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان:
به هر کس و هر جا بخواهیم دست بزنیم و وضعیت را درست کنیم برای ما مساله درست می‌کنند/ آیا من مقصرم که وارث چنین وضعیتی هستم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/152240" target="_blank">📅 10:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152239">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXg5CPaOgThr4uSyQyj3hDKq5tQvvns6UCvJp5hIBlRcbff_Q6Qkt8CLgQ15gKGKr6cf_EzNf4CIf_iZpgfc4P6Fgp10Mo602etM6_E1hSujhlbDeHT4mTkIXCrMj8u5ph1rSs02eZCFJQDK3kRQAilbfDmpGqduDSTQIU7LxT4sIKXkDg0tTwOJkHDwRDkAK4frAsGe0S2IJ4bPAWSFHcIBiyDHF9x2Nn7mTTbcyEJ6YMdm3qIe4-ZdmElBGJRS9RJv0Ah2YwMC6fZ2kfqMqoIqava-4TqIphkb0mN-chhGKIABRDTlqH52RYlLolwqu9Q3_LC5xM8F-Tg6qYRsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف:
وایسم تا صبح غُر بزنم قاسم زنده میشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/152239" target="_blank">📅 10:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152238">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
هر لحظه احتمال جنگ و قطعی اینترنت وجود داره، کانفیگ‌های ووکس حتی تو قطع اینترنتم جوابه
https://t.me/voxnet_bot
https://t.me/voxnet_bot
قیمتا مفت و مورد اعتماد
✔️</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/152238" target="_blank">📅 10:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152235">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وال‌استریت ژورنال: عربستان با کمبود موشک‌های رهگیر و سامانه‌های پدافند هوایی مواجه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/152235" target="_blank">📅 09:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152234">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b515c6a048.mp4?token=IeT4uEP_U-rMviDVSR3dJGs1kCn1n3wkHMfdHfa5iInQE4u9zuyChrQ6dSZHL3aK9MiqpIBVnC910HMTblPhgjStCRnn_bweCXAeiwC6XPzkrWjwiUnXkeb4YaQkVDmPH3JjU0mgjbl1vkLfLHW8xduwzsaD1HteKUzbqdUH5-B139hP8hapSCmHgCIl4HzacdQC1TDu01fajNQmUvx7Gpqtg44jj9YUNRCsndK6-tcC5r_LnioGkAPBHekoxkvBezjqSf96r2G3qo17BSGptLueWVpTHAgedDdGEqmsfIefOHwPlH1zitN-jmz6ZyIaTI9BUx1QMRkmUnipWJ0tJg9hkFL4Ub9ZL8obV2O0GYO0wEmmxoWgPUfrGqgNmQgt_LEznUw5WO9KFuuNK7Yl5oFoiie92Cej9-XZ44-zdAYN8ibnCP8m-yyTwcUWDuLs7YqF5VP3mp-aT7ASo8N3ZavYSObfxqFt_1SiU1iuzIIbkjgfSaTKRmMgrx5wGx4Bgc0-ZRS_I6JIUqjYOBjNcBLJ5j3n_wf503O32KISFiJwkun5NTmacXt5mJpcer8JrVyqaLihfvePhDgPsC0TNQ0z4sCXWENZ_Jqt5ip7VX-ARa2uj95UXh_anlqQZha8hzG36dVMX3Za0ggyWLb-e32QDwEz4tLePaDy5iYTzdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b515c6a048.mp4?token=IeT4uEP_U-rMviDVSR3dJGs1kCn1n3wkHMfdHfa5iInQE4u9zuyChrQ6dSZHL3aK9MiqpIBVnC910HMTblPhgjStCRnn_bweCXAeiwC6XPzkrWjwiUnXkeb4YaQkVDmPH3JjU0mgjbl1vkLfLHW8xduwzsaD1HteKUzbqdUH5-B139hP8hapSCmHgCIl4HzacdQC1TDu01fajNQmUvx7Gpqtg44jj9YUNRCsndK6-tcC5r_LnioGkAPBHekoxkvBezjqSf96r2G3qo17BSGptLueWVpTHAgedDdGEqmsfIefOHwPlH1zitN-jmz6ZyIaTI9BUx1QMRkmUnipWJ0tJg9hkFL4Ub9ZL8obV2O0GYO0wEmmxoWgPUfrGqgNmQgt_LEznUw5WO9KFuuNK7Yl5oFoiie92Cej9-XZ44-zdAYN8ibnCP8m-yyTwcUWDuLs7YqF5VP3mp-aT7ASo8N3ZavYSObfxqFt_1SiU1iuzIIbkjgfSaTKRmMgrx5wGx4Bgc0-ZRS_I6JIUqjYOBjNcBLJ5j3n_wf503O32KISFiJwkun5NTmacXt5mJpcer8JrVyqaLihfvePhDgPsC0TNQ0z4sCXWENZ_Jqt5ip7VX-ARa2uj95UXh_anlqQZha8hzG36dVMX3Za0ggyWLb-e32QDwEz4tLePaDy5iYTzdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: مدیریت ناترازی بنزین نیازمند تصمیم‌گیری عادلانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/152234" target="_blank">📅 09:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152233">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1d2590ab.mp4?token=UH0ohK-FLVh5z_G4VcuXcYEURqz2qEOTzYnrbI39GhgqNaDv_Oy1iheIz4uW1ncIDUpDMd_YHgQPa5jLi-swCEbe55G1c5aGrZAmMqLEewTZTEQot7lDZUSRJDVv_Sl0-jU_Fv6hjH5II114BgGdxvNJ8-lPDAdUMvUqsXGLg7fNIFWRWtS_IWEsahKXDJAhcFnqTbcphXXODjo70I-PlYqvDdfZz5FOb0-ZOOIQOtSCeCtmRp2lJRdTVmXSiQHmPGiRCLvhRw-VElQO1-dSXkYEplhz9jjooR40gb8ADzdZRgumysRwFUCaGQOpxxqUAOziOJK9KTQ3CZdTPyIutQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1d2590ab.mp4?token=UH0ohK-FLVh5z_G4VcuXcYEURqz2qEOTzYnrbI39GhgqNaDv_Oy1iheIz4uW1ncIDUpDMd_YHgQPa5jLi-swCEbe55G1c5aGrZAmMqLEewTZTEQot7lDZUSRJDVv_Sl0-jU_Fv6hjH5II114BgGdxvNJ8-lPDAdUMvUqsXGLg7fNIFWRWtS_IWEsahKXDJAhcFnqTbcphXXODjo70I-PlYqvDdfZz5FOb0-ZOOIQOtSCeCtmRp2lJRdTVmXSiQHmPGiRCLvhRw-VElQO1-dSXkYEplhz9jjooR40gb8ADzdZRgumysRwFUCaGQOpxxqUAOziOJK9KTQ3CZdTPyIutQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روز شنبه دکتر مهرآئین که به دلیل انتقاد از ج.ا به ۸سال حبس محکوم شده بود، راهی زندان شد
🔴
با آرزوی سلامتی برای این مرد بزرگ و فرهیخته
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/152233" target="_blank">📅 09:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152232">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه اینجا رو بخون تا از بازار جا نمونی
👇
👇
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/152232" target="_blank">📅 09:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152230">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-GmTtj9WL5zMSm-fERn4OfJX8Ir-yhDh22QNU6dOrXr0io4Lsqlpa9Snk3t2LxGyo2XIj3ZOUkuALIf7On0K_lS1MB5khImYWWYv2kA-yL2X84T46k23CP5kM3-L6QTLxcf0k4M1ttkmCIcZGZSPQmcgR3YO9oPCTdt8N3JfOgbIxevWJ6du5lBZ06y4I4cBXZtJXI4SH5US3jgkwXXBt2vwBP4wijq7RIqRQkubf9iaYftomExMu0JHA_P5TEmEhTIdOet76jFgZSVkl7gzc1OMovmz8GFbhts0d5iALiQOD8-oCZ425je-iCH-TcFJyTuRhuBrqABZoEPW_BtPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باهنر: اونایی که شب‌ها تو خیابون علیه صلح و توافق شعار میدن(امت معکوس شده) قطعا عامل موساد هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/152230" target="_blank">📅 09:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152229">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نمایندگی دولت آمریکا در عربستان:
سفر کارکنان ما به ۳۲ کیلومتری مرز عربستان و یمن، ممنوع است
🔴
آن‌ها برای استفاده از فرودگاه ریاض، ملک فهد و ملک عبدالعزیز نیز ملزم به دریافت مجوز ویژه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/152229" target="_blank">📅 09:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152228">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از مقامات اروپایی: آمریکا، اوکراین را به توقف ارسال سلاح تهدید کرد
🔴
دولت ترامپ به اوکراین و اروپا هشدار داده که اگر حملات به تأسیسات انرژی روسیه متوقف نشود، امکان دارد آمریکا اشتراک‌گذاری اطلاعات و خرید تسلیحات برای اوکراین را تعلیق کند
🔴
این تهدید «روزی غم‌انگیز» برای کی‌یف و متحدان آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/152228" target="_blank">📅 09:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152227">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شعار امت معکوس شده و الاف مقابل مجلس: خواسته ما عزل پزشکیان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/152227" target="_blank">📅 09:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152226">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ededdf52d.mp4?token=SjRaqnAMcrpke_ymp0DTY8uirN6mlVy64bySEZvH2DSS-IcITZjWnVZtviGVUkkLqD_K3Ok9QX0WSIySXooCJ6szC9YZIL8Q0txVVmXcISSPoFztfRBk6RxUBTIdiTNr9vPA74BIJ6mNtadeAgr558Ypwum9Vye_Aqkupx-Rnk_37s-uoslfxniIhgLtWImcqkd9QFgr9v-3yezqcn5NCi-3RRJziSyJWgmcicrBoCJzM78FFD10l55jQeD0K3-oJ_UNFEZcaZRRGDH0aOnzwY3GQKSffHT57tvHks0tG0N6uN1uPnlI9WT0wxC_aSMVWa60Gj2_uLgVxR0Q2DbdFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ededdf52d.mp4?token=SjRaqnAMcrpke_ymp0DTY8uirN6mlVy64bySEZvH2DSS-IcITZjWnVZtviGVUkkLqD_K3Ok9QX0WSIySXooCJ6szC9YZIL8Q0txVVmXcISSPoFztfRBk6RxUBTIdiTNr9vPA74BIJ6mNtadeAgr558Ypwum9Vye_Aqkupx-Rnk_37s-uoslfxniIhgLtWImcqkd9QFgr9v-3yezqcn5NCi-3RRJziSyJWgmcicrBoCJzM78FFD10l55jQeD0K3-oJ_UNFEZcaZRRGDH0aOnzwY3GQKSffHT57tvHks0tG0N6uN1uPnlI9WT0wxC_aSMVWa60Gj2_uLgVxR0Q2DbdFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور دارلین گراهام درباره ایران:
«چرا در دنیا همین حالا متوقف شدیم، درحالی‌که آن‌ها هنوز خطرناک هستند و ما به پایان دادن به جنگ نزدیک شده‌ایم؟
🔴
فکر می‌کنم رئیس‌جمهور ترامپ می‌خواهد به جنگ پایان دهد. می‌دانم که او چنین قصدی دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/152226" target="_blank">📅 09:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152225">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c01b83b1.mp4?token=XvrJrBRQ_C0pdQU-6c36dYmCm3sxeZPdrqq0Cx61eKsSaeBGs6HOr65SqfG0P8vCNK7CTv6pHV9GGm31LZC2CzhTQxDZDfOirNTYqSL3tOrFk5rWuNmHFDivIltqt-Lmo_uGSsRoS3-uYd5WMY0ng22DqqSRPtTZJ-Hf19D8op5G6Vl6x0zappzdtbt7gYeCwJkZZuPi-ZkNyvK3fCIz4R4CY53Ozc4jsXGmTsQhgUfi-iQTQeIsylGUQjJKL4_xodQd8bk1uAkYGj7c8sDsPu4JTjPnDadCMZg33jUnRos42NS6G4-DOWSMb-9CSVtpAZN201h0gmk8-iOMx8th0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c01b83b1.mp4?token=XvrJrBRQ_C0pdQU-6c36dYmCm3sxeZPdrqq0Cx61eKsSaeBGs6HOr65SqfG0P8vCNK7CTv6pHV9GGm31LZC2CzhTQxDZDfOirNTYqSL3tOrFk5rWuNmHFDivIltqt-Lmo_uGSsRoS3-uYd5WMY0ng22DqqSRPtTZJ-Hf19D8op5G6Vl6x0zappzdtbt7gYeCwJkZZuPi-ZkNyvK3fCIz4R4CY53Ozc4jsXGmTsQhgUfi-iQTQeIsylGUQjJKL4_xodQd8bk1uAkYGj7c8sDsPu4JTjPnDadCMZg33jUnRos42NS6G4-DOWSMb-9CSVtpAZN201h0gmk8-iOMx8th0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از برخورد نفتکش با مین دریایی در اطراف تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/152225" target="_blank">📅 09:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152224">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
هواشناسی: امروز در برخی نواحی شمال شرق و شمال غرب، بارش پراکنده پیش بینی می‌شود.
🔴
برای پنج روز آینده در ارتفاعات کرمان، شرق هرمزگان و برخی مناطق سیستان و بلوچستان در ساعات بعد از ظهر و شب رگبار و رعد و برق و وزش باد شدید موقت پیش بینی شده است.
🔴
امروز در برخی مناطق شمال شرق و شرق در برخی ساعات ، وزش باد شدید، گاهی خیزش گرد و خاک رخ می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/152224" target="_blank">📅 08:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152223">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر کشور عازم جمهوری آذربایجان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/152223" target="_blank">📅 08:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152222">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
طوفان ریچل سواحل کالیفرنیا را درنوردید
🔴
ویدیوی جدیدی از لانگ‌بیچ در ایالت کالیفرنیا نشان می‌دهد که برخی خانه‌ها بر اثر امواج بزرگ ناشی از تأثیرات طوفان ریچل شروع به تخریب و فروریختن کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/152222" target="_blank">📅 08:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152221">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15cec56d04.mp4?token=gZsIELRtYM17NhdB-gccc9o-wbrPZRZwmL9HelvxCu85Tgn7IRll0DNQMmdTzihSEG33faG8jjGR6IIOWtZzlF56YkILMMh54xC435nigXFn811tK79uFSJaHv7ap_06i3z8NF5IGL4hl6EB18PjmY3iCaeHgQ161qdDkKbPbxykuUhplCpr3Kl8FVEhDaoBHdj7vbdgJBvCvP69AiX88hpYYG_MDwDbgQl6ZaX92Z037lyuctutE9MGquh8m55e3VfPx-c2e9Mf_N7ny20o3Qic_BKbDSFUYeMVwDftjGE5n-d8qBcDJV5p84ZZin94oUA9sCB5U5HlBr5ZmsTjDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15cec56d04.mp4?token=gZsIELRtYM17NhdB-gccc9o-wbrPZRZwmL9HelvxCu85Tgn7IRll0DNQMmdTzihSEG33faG8jjGR6IIOWtZzlF56YkILMMh54xC435nigXFn811tK79uFSJaHv7ap_06i3z8NF5IGL4hl6EB18PjmY3iCaeHgQ161qdDkKbPbxykuUhplCpr3Kl8FVEhDaoBHdj7vbdgJBvCvP69AiX88hpYYG_MDwDbgQl6ZaX92Z037lyuctutE9MGquh8m55e3VfPx-c2e9Mf_N7ny20o3Qic_BKbDSFUYeMVwDftjGE5n-d8qBcDJV5p84ZZin94oUA9sCB5U5HlBr5ZmsTjDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور دارلین گراهام درباره ایران:
می‌گویید که من می‌خواهم جنگ ادامه یابد.
🔴
بیایید فراموش نکنیم که جنگ چگونه آغاز شد: در دوران دموکرات‌ها، زمانی که ایران تقریباً به سلاح هسته‌ای دست یافته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/152221" target="_blank">📅 08:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152220">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBrzGLDaQ3h3EX1A99ewIwqztU9Hge06mivRN3N-weBH0iZNMaE__sS0qwz5uztAUrzNMyI7kbB542qLCfb2nQByNQzTuuUqyEMD8m8OTFmDGLaFxtlsS4Dr-pt9Ln80A-Ij36EkX46206SYdOrJ3MtfaeLIiKdXu8mgeTGBgE0a50g-xnedshthmZ97kcadLTkXDuNJ_TWCkMkaf_-psYOeo-YAVQfkrEFmR3Th-FgVyXoR2kAPtn8voiCnVan5gvdoYH4IL8iCC_DMqz5P3pk9pTczu7My9g2yXquPVbelWp9HgJXQXU8QsUJyaUEsI1T5DaA2FudHMyN2ACsH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت افزایش یافت و از مرز ۱۰۵ دلار گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/152220" target="_blank">📅 08:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152219">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a8f70a19.mp4?token=XyKrsw7pXbDOTZGtaH1LUCWCQrzFQtjPfmcdq0XbPvL2jYA22euzmSZP3CczBJU7J0C8TFydl7PJ5ukneMHy4OS_nRqGwvB1z5LUFJzlcU1f6RX1YUWY0kt54RptHqY7O1J6rWPkjHD-kgki5FlHSxZJh1SiOSBoQZYQ5DlCmbwPyjrhqdmAUrj8m2EIrkW6xqav7MQr6Jv_e7ebJ8uLWJ8EvJr2jPfOwSpB6TRerciPYCbCL4Tp0kSwzbZ4E48wm0uApp7c4APSkrNkaaUnzTtbfyYwiKoAPi0zDRZSkH81okbCWO4jYBH79oxxXBU_bBvj8QRcZdsJwFa1PoCoKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a8f70a19.mp4?token=XyKrsw7pXbDOTZGtaH1LUCWCQrzFQtjPfmcdq0XbPvL2jYA22euzmSZP3CczBJU7J0C8TFydl7PJ5ukneMHy4OS_nRqGwvB1z5LUFJzlcU1f6RX1YUWY0kt54RptHqY7O1J6rWPkjHD-kgki5FlHSxZJh1SiOSBoQZYQ5DlCmbwPyjrhqdmAUrj8m2EIrkW6xqav7MQr6Jv_e7ebJ8uLWJ8EvJr2jPfOwSpB6TRerciPYCbCL4Tp0kSwzbZ4E48wm0uApp7c4APSkrNkaaUnzTtbfyYwiKoAPi0zDRZSkH81okbCWO4jYBH79oxxXBU_bBvj8QRcZdsJwFa1PoCoKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو تجمعات شبانه تبریز یه دختر دانش آموز جانفدا تو ۲۰ ثانیه کلاشینکف رو باز و بست و رکورد زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/152219" target="_blank">📅 08:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152218">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
طرف برای اینکه موز رو زیر کیلو ۴۰۰تومن نده گذاشته خراب شده اما ارزونتر به مردم نداده و حالا داره میریزه دور
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/152218" target="_blank">📅 07:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152217">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe357efbf.mp4?token=G-g_75PED7dsIp_hOwj3R9NGtie_pO0u4DzJhyOO7VOEQFFx3Vm3-WbFbhRn11S807-1I0O2OtDxzVwuf5oeRbCYC_KIR3bVSIOf6DxqWdfG1zpp1-5st5TpkheB4waobrKXe9ASAMCJLI8Uzk2oOlE8pNmZfGsE4I0VvqcDCRVU0EtWrHxkLk66tRF9AD9PHCcO42yeEwyCnCp2_AVavZ0P3uWssYDu-qePSnY5ZHBIfHKoU9g4_DlU5yo8eKOl4FMXBCNwnw9UivjQV-7a-whQW0iVzHntgn4ZeOSeE5PuImXk37CiaVjRfF8bvNChLsdDx-MLYCrFX1sOWwPzRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe357efbf.mp4?token=G-g_75PED7dsIp_hOwj3R9NGtie_pO0u4DzJhyOO7VOEQFFx3Vm3-WbFbhRn11S807-1I0O2OtDxzVwuf5oeRbCYC_KIR3bVSIOf6DxqWdfG1zpp1-5st5TpkheB4waobrKXe9ASAMCJLI8Uzk2oOlE8pNmZfGsE4I0VvqcDCRVU0EtWrHxkLk66tRF9AD9PHCcO42yeEwyCnCp2_AVavZ0P3uWssYDu-qePSnY5ZHBIfHKoU9g4_DlU5yo8eKOl4FMXBCNwnw9UivjQV-7a-whQW0iVzHntgn4ZeOSeE5PuImXk37CiaVjRfF8bvNChLsdDx-MLYCrFX1sOWwPzRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ضرغامی: چون حسین شریعتمداری (سرپرست روزنامه کیهان) پلنگ صورتی دوست داره بیشتر پخش می‌شه و هنگام پخش بهش خبر میدن تا از صداوسیما تعریف کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/152217" target="_blank">📅 07:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152216">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فاکس‌نیوز: ارتش آمریکا راهنمای شناسایی نیروهای زمینی ارتش ایران را برای سربازان خود منتشر کرد.
🔴
بر اساس گزارش فاکس‌نیوز، این راهنما با عنوان «تهدید را بشناس» (Know the Threat) برای کمک به سربازان آمریکایی در شناسایی نیروهای ارتش متعارف ایران، موسوم به «آرتش»، طراحی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/152216" target="_blank">📅 07:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152215">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران تحصیلات | irantahsilat</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8D9FyEAPc1pOZdsyv5JJG-qKAD7UI6oB2VtcsK0B-ce4Alki0Y6PO2KkLqM6XLUbg6CcH9G7UAvDLcD2dXlvccGV_MoQ6nud8ptrOZ8EzPCKS5cmmmqDCfHhI70E-1H5OdM22Puw9lOl6qffk92nhMMrf6PnuKJ6KrZotkjH9ay8THzvd28z0wNQVaChLJgpqGn3C3rnjh3nC3f6i3hIUa-DFg4k2PeSscjvURL7difz6uxrPiFGUe8m_HVh6y58WSTB_STXVKqM6apFJLflvnu7pmTSFfkfD2j_fvQhE8I8OpZX_kWSXZsCw-rNXHraVpH1pqqJQwbVpqd25AshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
مدارک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_support
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/152215" target="_blank">📅 01:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b482f6d3d9.mp4?token=YIOtzKT1KP6hpxYtRJYwof4BScenjCSWtMD0Hwdfzs8qDa-JDdSI3EWp0fNunQz-gIPzPWLEQA7LDT71CdVjwUQJa_12rWGCWeEZSueQ6KtfAeBvBU_htQ6S6uuSDH6Y_ZDrRANrhHKYQNYJ-x1kpGyz8W-XyTY79FMY04uWD3GEWlXVpjag3DcO3AEZ3Av2VheQ10AULm3L_MHRsqNWBhjc1UnD3Tvn3pD17-_8OtVw_2yVZkHDbfEoJdu6vEqJRNBn_vQuYSaGcrRPuKz54-Z3qZuPZRd4QvwCb8GtUn6-xRjC52EvteEGwJnhPdSnjdAv0MQqG_lN-VE-_SRP94S050M0pXQdxHnPKfQyriesFvw41hyxhM1SgEXYcj7xPtJtZl1FBxCS1c9JPfAN9IfpBaO3IgN1opJzgzbc8u6_VbZ3crWexdhICPHPTutH6gTpD3rjsCnms9JyVTNWOgB4Q4cH4lWknTdT2vdJyoRS8MfrccVV9ht3pfMfT7VtcLpN3y-juaAJGmVOPC_s4n2u__K9q732sZEFUfIQGreNR_9zHHLUdNic6C5lH9OEiln9_dJIHL8Uo_U0gRTEsYAtNVerLtocoy4uvWAceCF7Wmq1Vhwa4On5HkJ78NyoJrsQMADVxwzZ_K5aWmmXSf0O7LlsuJ_Z_Qjk4v-J4ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b482f6d3d9.mp4?token=YIOtzKT1KP6hpxYtRJYwof4BScenjCSWtMD0Hwdfzs8qDa-JDdSI3EWp0fNunQz-gIPzPWLEQA7LDT71CdVjwUQJa_12rWGCWeEZSueQ6KtfAeBvBU_htQ6S6uuSDH6Y_ZDrRANrhHKYQNYJ-x1kpGyz8W-XyTY79FMY04uWD3GEWlXVpjag3DcO3AEZ3Av2VheQ10AULm3L_MHRsqNWBhjc1UnD3Tvn3pD17-_8OtVw_2yVZkHDbfEoJdu6vEqJRNBn_vQuYSaGcrRPuKz54-Z3qZuPZRd4QvwCb8GtUn6-xRjC52EvteEGwJnhPdSnjdAv0MQqG_lN-VE-_SRP94S050M0pXQdxHnPKfQyriesFvw41hyxhM1SgEXYcj7xPtJtZl1FBxCS1c9JPfAN9IfpBaO3IgN1opJzgzbc8u6_VbZ3crWexdhICPHPTutH6gTpD3rjsCnms9JyVTNWOgB4Q4cH4lWknTdT2vdJyoRS8MfrccVV9ht3pfMfT7VtcLpN3y-juaAJGmVOPC_s4n2u__K9q732sZEFUfIQGreNR_9zHHLUdNic6C5lH9OEiln9_dJIHL8Uo_U0gRTEsYAtNVerLtocoy4uvWAceCF7Wmq1Vhwa4On5HkJ78NyoJrsQMADVxwzZ_K5aWmmXSf0O7LlsuJ_Z_Qjk4v-J4ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی پشم ریزون از جنگ ۴۰روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/152214" target="_blank">📅 01:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152213">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSfmxdYWBdIdF5hA_IPRNCu9btlq7ZB45iiSn6cM30T6EbV68loRW0CNDNQUa3v1OokRj593CxNXhkGMBBeV1JaGXVm_spyX6YxBX3hD5Bmo5t4UcBU6srj-thB81XeGoi5LR1L49Q4AKxWaLSIpL8BlWuUaf_0akWzWSDGjB1wsqOgWpGlaT256cSesqpSfnYlgYufGouJ30LwD3bXrBmF6Jcgv13MQF4OMCHqZte2lvD58sZ7XbN8UJdXw8d5_wNcYQ6b2CMSNYwtRyH6ila7LsSD_6LolkBJzyf4H_g0v76782tRhlXObJ-YriF2mOpZYwzsBTYZgpuGibv2JoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روحانی: حجاب اجباری بی فایده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/152213" target="_blank">📅 01:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90ad219cbc.mp4?token=fZgzJtdr9herGIS8ywBogr3kfj9ubPhUMXPiHWjSr5e4AkL0uLC-TFzbRBpnUf6ItO31Ud7fQeJEWXrkHOePjfQWWs6oJ8iCsZTeAKSLHJxROz940erLaFk8Uc9LFaLCbl5NzT3PMQaO-tebKCc6U97D2kZRBYmJum2NLVSp7wY9uJgyDQzTZISbzXJ5N4gaOAr9VHlGV2qmm9MN6HGgTQgmrWQ7IB5RC6sFKTktZSkH9VP9IK98g7SUbrZbUlxgndB7CSfvEpCAMLY8IexUxNgqxI9u8SbhzHJNAsQWRd80eEjvfXvq4Gy-05h-xNIc-g2ThqppLyYkq-DE5VlTjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90ad219cbc.mp4?token=fZgzJtdr9herGIS8ywBogr3kfj9ubPhUMXPiHWjSr5e4AkL0uLC-TFzbRBpnUf6ItO31Ud7fQeJEWXrkHOePjfQWWs6oJ8iCsZTeAKSLHJxROz940erLaFk8Uc9LFaLCbl5NzT3PMQaO-tebKCc6U97D2kZRBYmJum2NLVSp7wY9uJgyDQzTZISbzXJ5N4gaOAr9VHlGV2qmm9MN6HGgTQgmrWQ7IB5RC6sFKTktZSkH9VP9IK98g7SUbrZbUlxgndB7CSfvEpCAMLY8IexUxNgqxI9u8SbhzHJNAsQWRd80eEjvfXvq4Gy-05h-xNIc-g2ThqppLyYkq-DE5VlTjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روز شنبه دکتر مهرآئین که به دلیل انتقاد از ج.ا به ۸سال حبس محکوم شده بود، راهی زندان شد
🔴
با آرزوی سلامتی برای این مرد بزرگ و فرهیخته
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/152212" target="_blank">📅 01:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnafMA_FutbWFaJEDcCUSA5dHACpozU7HcKvsq30_eaRDqcsHUvu5hxePwpo-SSZnmdFHyldpSoskNOFn3yQp6puXlmGOhCsEM_MoVEQUcV0Uz17HqgJikaa4l9wvzSez_AYjQfp84gs-Xi6wI22qiZj7fgTgd9joYbSmGzrpEsLbsYdcpWLyvX9W6YH5YSWPQXfR4leCyz1qruhE_Lwt0yPsu19hrw60DVE0mc6nF2o4fmcgfqdGfwvfklUXpBvgTDT4YA5d0F0vFX7DqcckQHegSOQ_s5eCJ1rYC4rFNSUBIrI1VGLQlVu87TwhBK9zvsVWbkwEG5U6HOoRB0U-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند جنگنده چندمنظوره F-15 نیروی هوایی ایالات متحده (USAF) در حال پرواز تمرینی حمله به ایران بر فراز عراق مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/152211" target="_blank">📅 01:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👀
اگه دنبال کانفیگ ارزون و پرسرعتی
کلیک کن
🔗</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/152210" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رصد ۹۲ هواپیمای نظامی در منطقه طی ۲۴ ساعت گذشته
🔴
۱۶ هواپیمای ترابری از خارج منطقه وارد شده‌اند که شامل ۱۲ هواپیمای آمریکایی، ۲ هواپیمای فرانسوی، یک هواپیمای بریتانیایی و یک هواپیمای ایتالیایی بوده‌اند.
🔴
همچنین ۵ هواپیمای ترابری نظامی منطقه‌ای، ۳۴ هواپیمای سوخت‌رسان، ۱۵ هواپیمای جاسوسی، ۲۱ هواپیمای ترابری نظامی که در داخل منطقه جابه‌جا شده‌اند و یک بالگرد نظامی رصد شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/152209" target="_blank">📅 01:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرنگار حوادث:
پارسال همزمان با شروع جنگ تو نهم اسفند یه زن بعد مفقود شدن شوهر میانسالش میره اگاهی و اعلام میکنه شوهرش ناپدید شده
و حالا بعد چند ماه که هیچ ردی از شوهرش نبوده یکی از فامیلای این خانواده خیلی اتفاقی استوری یه زن جوون رو میبینه و متوجه میشه این مرد گمشده همراه این زنه
حالا که پای پلیس به ماجرا باز شده مرد اعتراف کرده بعد از فرار از دست زن و بچه اولش رفته هویت خودشو کامل جعل کرده و بدون اینکه چیزی از زن اولش بگه با یه زن ثروتمند ازدواج کرده و ماه هاست داره با اون زندگی میکنه
😐
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/152208" target="_blank">📅 00:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152207">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
باهنر خبر داد: زینب ابوطالبی مجری جنجالی «مملکت مال حزب‌اللهی هاست، هر کس نمی‌خواهد جمع کند از ایران برود»، از کشور رفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/152207" target="_blank">📅 00:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152206">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEX3YaITzXywSl5LJfTg7Yq9HgY_WmwoouOwfZcraoJAT06sbcvYnnGrb5hNqCVjr873RjnNwAiDiIaDYLZnZ4uX_cIbGaamLlmpyaTfzyAX1OkJfe9_xCHI0-YGmSKXnGQYjislIahQtOfEz8-bp2aYnj4LEDP6eOV6vaa_JwKyD5p6pxkddFNwxT2sG19Ce7upKwkdso7bcmk4IG_zuENVhsYDUPXZ-wrWWMytFdVq0v_j6pfSOeHPIWYGj8zC1TkuTpA0SbXHaha741jLV3NrfOd-_IJVKM5kAAHmECQ5JXRjhhu0eqfUQc_6pzA8D-HC4QGXYaabKoiu1xVnaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال: ایالات متحده با برخی از هفت شرط ایران موافقت کرده است، اما ما پاسخ آن را ناکافی می‌دانیم. دیپلماسی ایران تغییر کرده است و دیگر به وضعیت سابق باز نخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/152206" target="_blank">📅 00:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152205">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b8846312.mp4?token=mnDORjTqeEAmAUPHc7WdzOYaeW4EkzaYXauztyC9_c10c0IkU4szmyZ3jdewb_1FFjIjqCgUe_da4QN0OFSWx7_kvE14pYlT8qhxWq4EZ6riXvq5JNETkpJsNensrt-Q7JRAn5c4rXWwLLHiPCxOqXK1wFKKkt3NZndX1Yo_FA49ue_q3dkuyj2bQd0lPSZanMA07xGHY53bBPXHVSDNlXbmOeBWEhyMxKd-iCMcatP_97gPYejnLbjNDSN_GYz8kfUfT0Ut1-LWwU-N706wPVtaZVQ2LcgVlzAUzaDX53KZPikGv-XhEzSqBSpC2ba-h-pFOuyx5lVoWWjLW2el0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b8846312.mp4?token=mnDORjTqeEAmAUPHc7WdzOYaeW4EkzaYXauztyC9_c10c0IkU4szmyZ3jdewb_1FFjIjqCgUe_da4QN0OFSWx7_kvE14pYlT8qhxWq4EZ6riXvq5JNETkpJsNensrt-Q7JRAn5c4rXWwLLHiPCxOqXK1wFKKkt3NZndX1Yo_FA49ue_q3dkuyj2bQd0lPSZanMA07xGHY53bBPXHVSDNlXbmOeBWEhyMxKd-iCMcatP_97gPYejnLbjNDSN_GYz8kfUfT0Ut1-LWwU-N706wPVtaZVQ2LcgVlzAUzaDX53KZPikGv-XhEzSqBSpC2ba-h-pFOuyx5lVoWWjLW2el0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی دیگر از هدف قرار دادن غیرنظامیان در فرودگاه ملک خالد ریاض توسط حوثی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/152205" target="_blank">📅 00:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کاش تو این ۴۷سال حداقل یه کوچه بنام کوروش یا خشایار شاه میکردید بعد فاز تاریخ ایران دوستی میگرفتید  [@AloTweet]</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/152204" target="_blank">📅 00:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNsP0P_NpgkUAdsOWoNU-4xbYdIqsiK_cDH6zrJok-MuZCNc0QYzsoB6iWxvoM32lmCkTa-p7AonMX9NF56XgBX6Fv2y_nAEKeoW_K7y_xgWmr1x5nJ-4j6xWV4Dr7ydriV_qrQaEekKta-F0PAzdFqY7gsG_FtBDoYxKszzlG3S2S1lmtBW45KyydhGg7k6LKQjSkitcx-HOb689b7AO1zBgMx5m8xsCRIp8-XgYpiA4NhY1oLT7fhWscCsRH9hWL_3jHhwQZia_gVS9tNAkoXurruIMY3YQ-qyqXrjfEE8V26-vgvVhH8UVwB8fbq5idBIB6GiMK_3-Vrh4x3v7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف: هرجور شده باید با آمریکا توافق کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/152203" target="_blank">📅 00:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22245fb3c7.mp4?token=YAlfGWpcLI8s5amo9oQwTKYVcir7rMUdlEBaCKw02eRgCtLxO4fAsyFmFx7heM-wxYaH131LjrW9zDiwue4PQdPRaHNKuPQTR7U5r-eZwBCOh4qWimMf-H6f3TUsnFAD4-LOm9vQwAGEQ8yGwShUTdljthznYVAnuVTNm6v0F_HADYrSycHUDCxHavUaU2IDKDXqbgnZBUGb7KUgGw7-QHlPgXstDWPBAnuNhe0K8onlGAek70vT-Uz5AthKCCFsV_jsoMP3H5FpsL8xeACOCB0fDDPatqM-U0EmbGuuc2PNlFFcm2ll1IV6Wxp5ePdNQwbOp7SB4ujCqDLa25z9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22245fb3c7.mp4?token=YAlfGWpcLI8s5amo9oQwTKYVcir7rMUdlEBaCKw02eRgCtLxO4fAsyFmFx7heM-wxYaH131LjrW9zDiwue4PQdPRaHNKuPQTR7U5r-eZwBCOh4qWimMf-H6f3TUsnFAD4-LOm9vQwAGEQ8yGwShUTdljthznYVAnuVTNm6v0F_HADYrSycHUDCxHavUaU2IDKDXqbgnZBUGb7KUgGw7-QHlPgXstDWPBAnuNhe0K8onlGAek70vT-Uz5AthKCCFsV_jsoMP3H5FpsL8xeACOCB0fDDPatqM-U0EmbGuuc2PNlFFcm2ll1IV6Wxp5ePdNQwbOp7SB4ujCqDLa25z9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش روسیه به نیروگاه برق خارکیف اوکراین حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/152202" target="_blank">📅 00:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👀
با پول یه بستنی، vpn یه ماهتو بیمه کن
کلیک کنید
🔗</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/152201" target="_blank">📅 00:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fd15c39b.mp4?token=KZWtfErM-dUg40tdbhHEDpTowaKnC7llA-WlRFaUedI_XtPFIr9MvY1_S0kp6Ugzzflw49QW03z4UgwwYDbXfgjND0Zpm-zCGdhNM2nep8BJgG971BFNbWtVyFyFlmHpx8lm8W2WmYmQ_Sdjk0EyqNMMhu97AQvOB3Eh-Q4RJpxgmDdhwWHheoD-hTcipGh6K9pO7q1jiV-9UlqVq1rafvsaI-hAlFoAZCYMVO-aZGgg6a6yHdY_jelhxamEOENUduHmPx2EY5CUkvQDYVuqlCi_r04aLmysvpxWob6VBzrMidW7x9x9Lh94ssVf-YTW3JDGlaWzsHkIphV_dN2iZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fd15c39b.mp4?token=KZWtfErM-dUg40tdbhHEDpTowaKnC7llA-WlRFaUedI_XtPFIr9MvY1_S0kp6Ugzzflw49QW03z4UgwwYDbXfgjND0Zpm-zCGdhNM2nep8BJgG971BFNbWtVyFyFlmHpx8lm8W2WmYmQ_Sdjk0EyqNMMhu97AQvOB3Eh-Q4RJpxgmDdhwWHheoD-hTcipGh6K9pO7q1jiV-9UlqVq1rafvsaI-hAlFoAZCYMVO-aZGgg6a6yHdY_jelhxamEOENUduHmPx2EY5CUkvQDYVuqlCi_r04aLmysvpxWob6VBzrMidW7x9x9Lh94ssVf-YTW3JDGlaWzsHkIphV_dN2iZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون وزیر ارتباطات درباره تعرفه اینترنت: مردم با گرانی دیگر چیزها مقایسه‌اش کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/152200" target="_blank">📅 00:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
خبرگزاری دولتی عربستان سعودی:
وزیران امور خارجه عربستان سعودی و ایران درباره تشدید اخیر تنش‌ها در منطقه گفتگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/152199" target="_blank">📅 23:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تصاویری نشان می‌دهد که در دیروز، یک موشک بالستیک متعلق به گروه حوثی (انصارالله) به ترمینال شماره 3 فرودگاه بین‌المللی ملک خالد شهر ریاض اصابت کرد.
🔴
این حمله منجر به کشته شدن حداقل 13 نفر و زخمی شدن بیش از 300 نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/152198" target="_blank">📅 23:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
اکسیوس به نقل از یک مقام کاخ سفید:
«ترامپ واقعاً عصبانی است. او احساس می‌کند زلنسکی آمریکا را بدیهی فرض می‌کند و قدر حمایت‌های آن را نمی‌داند.»
🔴
استیو ویتکاف و جرد کوشنر، سفر برنامه‌ریزی‌شده خود به مسکو را به تعویق انداخته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/152197" target="_blank">📅 23:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf-DMIhIxcdD0TKWfND06JPWmMqTJzrYsNRql7V8IuZgf3O9clI1nEQLklBChurVEczQaZITgSNfgSjdr223nzL4MPRcBEpMpczqW9RNXa6Pp4-1LOKNEita7wr6x_rS3wVxSaTmC2r6JSElDpv1S8yxN_CmbmGJBKspj0D1Mt2L_Vp6o3yamC9dwf4zF_NPGgDnHoJjZ2yyd1F3LqREwG47aY62QONgzTSgI6waAa3IBHJM_CdP4qyI0pX7lalWF6ehpZmuq8uMiChQCLQ6nSdncrWzXoh4gM4a-Z3vmloJPf6MDw4DO-OvrVAALh7wX2JYlh7w-yi-fkF4a7-xmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سپاه با انتشار تصویری در فضای‌مجازی نوشت: ما منتظریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/152196" target="_blank">📅 23:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
به گفته یک مقام کاخ سفید: ترامپ انتظار دارد که زلنسکی به آتش‌بس پیشنهادی در زمینه انرژی پایبند باشد و در ابتدا حملات اوکراین به پالایشگاه‌های نفت را متوقف خواهد کند
🔴
توقف حملات به پالایشگاه‌ها می‌تواند راه را برای یک توافق گسترده‌تر که شامل نیروگاه‌ها و شبکه‌های برق نیز می‌شود، هموار کند
🔴
روسیه همچنان در حال بررسی پیشنهاد دونالد ترامپ مبنی بر برقراری آتش‌بس در حوزه انرژی است
🔴
ترامپ واقعاً عصبانی است. او احساس می‌کند که زلنسکی، ایالات متحده را دست کم می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/152195" target="_blank">📅 23:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152193">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/493ee04b61.mp4?token=rQAM9ZLsCLb-N_Q56STvOmWo2hhHh-bL6khwdPHvQHt37xvFePFE3xPWuNgtBLNtxAV2YbCX-_XyvvCN7fObw2xSWhnh8gJGdESwYSAodVEgFqer2ta3OZe-sBRMm5mXvfl--q7-WwQ86X98uttXGWf3EgfAfjxvc1bpqs39qgmPOytae7Lpv--S0eRZqPswNvi9I5Atsr3fQ0y7shf0w2rcuMbu-723_wcGfIGVQKAfylM0HtYLWA8MWgd8DN4ollwbCVBel6gIBD2QdnlHnpJzO1FwPuOPut2T2ecFgyU1MVdpHjmvHpShfKTXIcr_DrxnWuELnz46AVxuxSxWbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/493ee04b61.mp4?token=rQAM9ZLsCLb-N_Q56STvOmWo2hhHh-bL6khwdPHvQHt37xvFePFE3xPWuNgtBLNtxAV2YbCX-_XyvvCN7fObw2xSWhnh8gJGdESwYSAodVEgFqer2ta3OZe-sBRMm5mXvfl--q7-WwQ86X98uttXGWf3EgfAfjxvc1bpqs39qgmPOytae7Lpv--S0eRZqPswNvi9I5Atsr3fQ0y7shf0w2rcuMbu-723_wcGfIGVQKAfylM0HtYLWA8MWgd8DN4ollwbCVBel6gIBD2QdnlHnpJzO1FwPuOPut2T2ecFgyU1MVdpHjmvHpShfKTXIcr_DrxnWuELnz46AVxuxSxWbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران جنوب لبنان توسط اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/152193" target="_blank">📅 23:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کانال۱۳ عبری: ارتش اسرائیل در آماده باش بسیار سطح بالایی قرار دارد و خود را برای سه سناریو آماده می‌کند:
🔴
۱- حمله مستقل به ایران.
🔴
۲- عملیات مشترک با آمریکا.
🔴
۳- مقابله با حملات احتمالی موشکی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/152192" target="_blank">📅 23:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزارت خارجه مصر: ۵ تن از شهروندان ما در حمله روز گذشته به فرودگاه ریاض مجروح شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/152191" target="_blank">📅 23:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b25c7ce1.mp4?token=R2K-BsJuVA-vKoiwJE-JzIoTCl5doXYu5W16apPd28R7K8xI1kvD0SSln22TPQJdQuDwfZc3y1d5zqqeFJirIv9Jl8fgVE7GS9g4wQsuWQNeJo3Vl9HFJMYEB9Tc-rcsp16sYmb4wQ275Xwv65b6eK5QDryC1sDhSAxD_rNiMHmr7FSXG-MoijUR0pmw4df6jzuolg_qqJR8nrWanS9pReIbFNcXg91qaE21ihO6rpPUswSFOlVPTZT5XBVvTCmZXVKuExfToQIJl3htwRs8o1zJEYJTJk75PH8to6ysbiUW-IGDt5aQZFMh5PNobhnZ4oV9ygFcDdd6La9pLZrXRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b25c7ce1.mp4?token=R2K-BsJuVA-vKoiwJE-JzIoTCl5doXYu5W16apPd28R7K8xI1kvD0SSln22TPQJdQuDwfZc3y1d5zqqeFJirIv9Jl8fgVE7GS9g4wQsuWQNeJo3Vl9HFJMYEB9Tc-rcsp16sYmb4wQ275Xwv65b6eK5QDryC1sDhSAxD_rNiMHmr7FSXG-MoijUR0pmw4df6jzuolg_qqJR8nrWanS9pReIbFNcXg91qaE21ihO6rpPUswSFOlVPTZT5XBVvTCmZXVKuExfToQIJl3htwRs8o1zJEYJTJk75PH8to6ysbiUW-IGDt5aQZFMh5PNobhnZ4oV9ygFcDdd6La9pLZrXRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز جنگنده در آسمان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/152190" target="_blank">📅 23:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
باشگاه انقلاب تهران به دلیل بی حجابی و تحریک امت معکوس شده تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/152189" target="_blank">📅 22:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152187">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/av52jsiO4ZDyIN5E2495hNk0NBg8IZ_DXLZkyt3JGp39aWYp2JfhZNZxl1HE5ldo3JLkfut7t3aO-W_FiSxeSpfkfwKaTsVzNk-WBDMF1yUfNiHn_9WRBWNFqTfRUwuAba5ryW8_j6CZhBMMPJx805Vn5EVsEBCto5R8MEypW9IoLoyKhKDOl8rbsjH07E1OwhlWbPfzMSsiD7cmXI7UyfJAFxhD_9O4u4JHr5AqyJI1kTYffBCsUSNjY3AbBt0Ze0fY0Mi4_H6T_ozwpQi6BbjWUUDBxclpLb3wJnyC6Eg78e33VqLpZ6zQy1lcT-0VAlNUvGQ_GtmPSsEbl9MfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41fea1af6.mp4?token=i5evj9dwnXrNGpYyPEsDDEDAIgL6tDZY3KTk6GdJqR4HrLkDRCcqs_1N-4nt1xQIVtsZD7TvE3POZe0NCJQYBEOmX30ZM7D-VKc3aOjJ6udkHbE0tGBKpGIgN9AG6oNx_SFABDc6OBazYe-_rAFNQwxVjGET7pAAw1UfalNUIBUW8BNlvm2ilX0OMTlO7lgBNB8NkJ9IccCaAvZ-PgJ0eFtkbn_Bh2LGxI8V6Z9VV9jcfrE-Vr9WANUTzLBwx6AUkZUyx-jFxePQ7orYCwEmfg1ZJeXQgofF7ZNFdvcAMKhZ7wi47Wx7NaFHvYYlDJn4xnow3RXbRUqtotXFxOf_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41fea1af6.mp4?token=i5evj9dwnXrNGpYyPEsDDEDAIgL6tDZY3KTk6GdJqR4HrLkDRCcqs_1N-4nt1xQIVtsZD7TvE3POZe0NCJQYBEOmX30ZM7D-VKc3aOjJ6udkHbE0tGBKpGIgN9AG6oNx_SFABDc6OBazYe-_rAFNQwxVjGET7pAAw1UfalNUIBUW8BNlvm2ilX0OMTlO7lgBNB8NkJ9IccCaAvZ-PgJ0eFtkbn_Bh2LGxI8V6Z9VV9jcfrE-Vr9WANUTzLBwx6AUkZUyx-jFxePQ7orYCwEmfg1ZJeXQgofF7ZNFdvcAMKhZ7wi47Wx7NaFHvYYlDJn4xnow3RXbRUqtotXFxOf_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستون‌های دود از تأسیسات سعودی پس از هدف قرار گرفتن آن‌ها به هوا برمی‌خیزند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/152187" target="_blank">📅 22:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152186">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449533f768.mp4?token=fV_0iGNwFAM6nxmBblpqM2la4W3iEFA4_zn49JczZAQIfhWfwODpOA_r3tVMePO0hnNWRA2KEqy4Z73c_Wn9WpJp6l-LozewknpP1325pjOGWujqmnQcecVQ-O8h2GSmhtNZ1KrsW_sNVN6MJvKlNbDO0CrJHHFj-yfVd5DXDKkDEYmX0fn1-RV2IDvIvkucovBZgetZTBM3WwjqnuyDb15Eg_HCeDXw-u1FEaBqRdNKEfLCtxZczdWlIA8bD5WwcOtQkQUD-D6_PS94MeDEXpBSaLCu93bdeAyBb8Izd0CDHZLjadXnQ7BnL4MM08DBM7xC2QCkFqEj58Bc_3UhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449533f768.mp4?token=fV_0iGNwFAM6nxmBblpqM2la4W3iEFA4_zn49JczZAQIfhWfwODpOA_r3tVMePO0hnNWRA2KEqy4Z73c_Wn9WpJp6l-LozewknpP1325pjOGWujqmnQcecVQ-O8h2GSmhtNZ1KrsW_sNVN6MJvKlNbDO0CrJHHFj-yfVd5DXDKkDEYmX0fn1-RV2IDvIvkucovBZgetZTBM3WwjqnuyDb15Eg_HCeDXw-u1FEaBqRdNKEfLCtxZczdWlIA8bD5WwcOtQkQUD-D6_PS94MeDEXpBSaLCu93bdeAyBb8Izd0CDHZLjadXnQ7BnL4MM08DBM7xC2QCkFqEj58Bc_3UhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز تو تهران یه پسری به مناسبت روز دختر برای دوست دختر ۱۹ سالش ماشین لکسوس خرید و بهش هدیه داد:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/152186" target="_blank">📅 22:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152185">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
معاون عراقچی: در حال بررسی پاسخ آمریکا به شروط هفتگانه خود هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/152185" target="_blank">📅 22:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152184">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 300 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/152184" target="_blank">📅 22:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152183">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkGxl9ElGT_Zvo28IPYnDaL_AYqQJ_rxaMt0QgkF_ErVJhXDFzYV4eWl0btx6RdCAjsvRKXmrwmATQLY91yvD2UxzBkzpukkChbS1wQcVdBryG24C762khRd_hk9mEMzjetsqfjbRHlxaNvZtFl_9UHn-GTctT9Ib_lcyHJP9pmewUc0Hp4DmF65enDg-kaPt8ThptY4c2BMw2_qDzLL3jKvudF6KWQcXUvjuEUufOnlnO5jQMuhd8F5x82KpfySelM1r7yPKArWFypObjzOEFlu3uTJZWD0Q6lT7MkCXf4A0bfwfaCgkHqHSm5Hf4e_GjwSVToi_WkjJ6gPYld1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک بهترین شهر دنیا در سال ۲۰۲۶ شد
🔴
تهران با افت شدید در رتبه 462 قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/152183" target="_blank">📅 22:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152182">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj_XKqJvXFAhmu_l6fHKIkfQYbLrAxDUCRSJPDfwYkcdzyJvLbk_bW-MQkdGParLvCwBToVlFT3gL03ipFYyLE6U621TvzMQc_uD5L5H6K_6x6J1yYXtezlf5_iKQYbX5YjR1su6msa_7e86hGnDacQ11Lw--N0kvPew6U2CtQaYlYmZNNLNmRWzIM32jjQbFDV6puW82cUv6yOa9IVbSzQYnNd6H3OG8d4UKdQFJ3RQ58ag0kOqM_JU7iRzeSDayYobkvQHtN44o33zfVpNR6F3bnlcyxja8t-lLLVIPAPUsLESw42_0Cv6A-OHOcsoPIQqppZLZ6GDBCwNOiTX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باشگاه انقلاب تهران به دلیل بی حجابی و تحریک امت معکوس شده تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/152182" target="_blank">📅 22:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152181">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی درباره وقوع حادثه‌ای برای یک نفتکش در نزدیکی بندر صحار عمان دریافت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/152181" target="_blank">📅 22:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152180">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PKiu6Wlvp_lo4Wk5i52LbjDw0wtXqLgjX7PJqMH-jKqttnZOCW4K5c2rtrQjD7VqK561u5HJwEpcDuQHIGcubIKqY_YpH2lSKPr3MR2RSjt2yb07r8s2jHSGBL7-N_FycnaQlN44NcmSEeFC6WzHqUXRmjNfctnxO9u3WgqvCfVDiauILvunSKr5rQAtigR7S0FYpCk2DC9gBtVuOtTGa7ereIOqiUakhdF0_nb0qkMOmvVf4a6o6lw1h95zLYLyif-_FvasxwlRBVbZXnsDxEyh_eaPkxKcGNLV2bOfPztkw3lg7JUNecxTpm_zJkZ8KXSLiKmTFow1QiIM0Jr7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان هوانوردی غیرنظامی عربستان سعودی، وقوع حمله‌ای به فرودگاه بین‌المللی شاه فهد در شهر دمام را تأیید کرد و اعلام نمود که ارزیابی خسارات و بازرسی‌های ایمنی در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/152180" target="_blank">📅 22:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سپاه: از امشب هر کشتی که در تنگه هرمز، سیستم‌های ناوبری و شناسایی خود را خاموش کند، به آن حمله خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/152179" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152178">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
باشگاه انقلاب تهران به دلیل بی حجابی تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/152178" target="_blank">📅 22:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گزارش‌ها از تمرین جنگنده‌های اسرائیلی بر فراز عراق با شبیه‌سازی حمله به مواضع جمهوری اسلامی در همین لحظات حکایت دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/152177" target="_blank">📅 21:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: بنیامین نتانیاهو نخست وزیر در این ساعت نشست ارزیابی امنیتی با مقامات ارشد امنیتی برگزار می کند. در این نشست همچنین به پرونده ایران در میان تنش ها پرداخته می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/152176" target="_blank">📅 21:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
میلی گلد: پول همه مردم رو دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/152175" target="_blank">📅 21:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152174">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
زلنسکی: روسیه پس‌از اعلام آتش‌بس انرژی توسط ترامپ، به تأسیسات انرژی اوکراین در کی‌یف و خارکیف حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/152174" target="_blank">📅 21:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152173">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da4f9104c.mp4?token=v34oLCYqfPxkwpZwPL79hGNc635A_ui_qWiekmbHqkGhz3AZkZWyVW6GCICVBGAdd51OhckR2q5bsGIGAaiseukJjwvc1MMYtUE8G7Jaq5eiIoUMZP96V2UhKW4Y9YWRaCEtVHtOWWqmKu2WIC2D-ZfcQsCRAFzDhHbIxExj0rtzIy1oKKgWMf3yBfa1_ecQemjnBgpm_NB_Z-RmYT5llasUpNUfeqU1UB-JXs3m9VO5wCqxC58oMIpIg1eA0kWqa8xs1zW4EnEmP3wHIeuItI-8VWCp1bqYj9gqaX_hZpVkUkKzjxYP3yMI0TtSkNYmNNkr1GPyDTBK02BpGFoHlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da4f9104c.mp4?token=v34oLCYqfPxkwpZwPL79hGNc635A_ui_qWiekmbHqkGhz3AZkZWyVW6GCICVBGAdd51OhckR2q5bsGIGAaiseukJjwvc1MMYtUE8G7Jaq5eiIoUMZP96V2UhKW4Y9YWRaCEtVHtOWWqmKu2WIC2D-ZfcQsCRAFzDhHbIxExj0rtzIy1oKKgWMf3yBfa1_ecQemjnBgpm_NB_Z-RmYT5llasUpNUfeqU1UB-JXs3m9VO5wCqxC58oMIpIg1eA0kWqa8xs1zW4EnEmP3wHIeuItI-8VWCp1bqYj9gqaX_hZpVkUkKzjxYP3yMI0TtSkNYmNNkr1GPyDTBK02BpGFoHlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی سپاه: دومین سوپر نفتکش با مین دریایی در تنگۀ هرمز برخورد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/152173" target="_blank">📅 21:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fb405cce0.mp4?token=E3hLPFYNuB9tgPWILd-sWCqrQV_YDIJf3TiIlIY-NZO3oCJNv6zIgJLLOTNysOU53J1ZB5YQqQB2AHYpCMnsGqKCmTyJJYpfVm7vGtsMAwnm2Yz5kifNzETLO6O_lJLyj5J0klaYPKzlDo3nVQ3acMkN-wzCHj5BCOzLzBAzj21mluZb6Kyo8lCOC142oCTmunzkKN8uhl2mPZzvXflWrlltrSSLRrVbLogIZ7l1QhRsR-QJMo1oXzSMJkTKJbfN8_EFcDffFOGAXGI8432lSRLfjR79F2q4V25dTJ2F1-vsMkcWn7Lg4INMOm5YpZamZcdPA2V9OeXvgEqWhMf0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fb405cce0.mp4?token=E3hLPFYNuB9tgPWILd-sWCqrQV_YDIJf3TiIlIY-NZO3oCJNv6zIgJLLOTNysOU53J1ZB5YQqQB2AHYpCMnsGqKCmTyJJYpfVm7vGtsMAwnm2Yz5kifNzETLO6O_lJLyj5J0klaYPKzlDo3nVQ3acMkN-wzCHj5BCOzLzBAzj21mluZb6Kyo8lCOC142oCTmunzkKN8uhl2mPZzvXflWrlltrSSLRrVbLogIZ7l1QhRsR-QJMo1oXzSMJkTKJbfN8_EFcDffFOGAXGI8432lSRLfjR79F2q4V25dTJ2F1-vsMkcWn7Lg4INMOm5YpZamZcdPA2V9OeXvgEqWhMf0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دعوای گروهی دختران تینیجر سر پسرای ۴۰کیلویی در رضوانشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/152172" target="_blank">📅 21:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152171">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d829e5c716.mp4?token=Ha42xqSI_tgrKzPu5Rqcr2qibVQmLGd-U1FOmwO0HW1yLjXy9BPc79SbpgyiaP-EOMx1UEzcaSPhLAtN8uclOhI9o7E6_eAB76es7bIX4by1qn7Fvp7FQwOjYmXryo3GKW1vdY5ewUfKoOWQ3RCvRvy6MNv8wZ0j4HJqHQxrqKayHLs0KbjwVIq_zkHi7bOYlOqJ_osuuJAxLk7NsGxuYiRJ22zLOmvNWYIWbFQ9ygdjr7OnkzTMmPc39u6QKsOGz2RO075pognzgMgwp7OwxAylxGOGQXdYTTdUlG9B8PZkQwDnrCwijzmByxOOXil_NQBovx_AvX1cSpQ8f8dmbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d829e5c716.mp4?token=Ha42xqSI_tgrKzPu5Rqcr2qibVQmLGd-U1FOmwO0HW1yLjXy9BPc79SbpgyiaP-EOMx1UEzcaSPhLAtN8uclOhI9o7E6_eAB76es7bIX4by1qn7Fvp7FQwOjYmXryo3GKW1vdY5ewUfKoOWQ3RCvRvy6MNv8wZ0j4HJqHQxrqKayHLs0KbjwVIq_zkHi7bOYlOqJ_osuuJAxLk7NsGxuYiRJ22zLOmvNWYIWbFQ9ygdjr7OnkzTMmPc39u6QKsOGz2RO075pognzgMgwp7OwxAylxGOGQXdYTTdUlG9B8PZkQwDnrCwijzmByxOOXil_NQBovx_AvX1cSpQ8f8dmbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ظریف:
اگر لازم باشد باید برای بقای کشور به توافق‌نامه‌ای شبیه ترکمنچای تن بدهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/152171" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
هیمتی: اقای بسنت وعده ای که دادی چیشد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/152170" target="_blank">📅 21:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
بیانیه مشترک عربستان سعودی، ترکیه، پاکستان و مصر: ما حملات مداوم شبه‌نظامیان حوثی به عربستان سعودی را محکوم می‌کنیم
🔴
این حملات تشدید خطرناک تنش‌ها است و ما از پادشاهی [عربستان سعودی] در اقداماتی که برای مقابله با آنها انجام می‌دهد، حمایت می‌کنیم.
🔴
ما شبه‌نظامیان حوثی را مسئول این حملات می‌دانیم و از آنها می‌خواهیم که فوراً آنها را متوقف کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/152169" target="_blank">📅 20:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نخست وزیر پاکستان: ۶ تبعه پاکستانی در حمله به فرودگاه ریاض زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/152168" target="_blank">📅 20:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv1ESE82Ht2mwztKe3iJp30HGaxbQgtQfBwIjGRit4U3Q5aTMso-VYYCNXBVMbP-MyXy_SqeTEK5IAw8B-i01xNIp50Tbyr9JVRFKRT9cTTMLK1Ts94I1erPYDAh1pjF54Q-xyd8FD5IY21UA6I4n7wefden2t9WD7unJSkiitAuUyXHLDznSrTDZ1f9ACdnsk3WW4amxa2BCgLsevnAEYPJQglKHnqg5ERGY3HVLcP-xBcw9167Wt4zIBVQ9b5jM36rLM_wJUjEKaDPcrsTMVPz2cZAWK-1FVx4-G-fua9sI803XfRWUYm9IeA6nrQkZODa4-eJ_2m11Oacti6HzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باهنر خبر داد: زینب ابوطالبی مجری جنجالی «مملکت مال حزب‌اللهی هاست، هر کس نمی‌خواهد جمع کند از ایران برود»، از کشور رفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/152167" target="_blank">📅 20:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آیا دلار 300هزار میشه
⁉️
تحلیل عجیب نوستراداموس ایرانی
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/152166" target="_blank">📅 20:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/604f2b0c98.mp4?token=XaHgtqlfHa1fLmhbyCZFRLnk2K4glPF5g-R4H3TCDwyUMyhEr166BiFh-QFAIZ1xshLGHe_LtAZXPirmAZhm3mSLW5o5lyPxaVKmVwy5Rc8NSu0MtuQTFM_QvfzDa3HMQl6dnVf1BTA-iefBNFiCBiD8kL63DKBzMfiq54gbekAXbRdrJcEaaz2cooFgGnoAt66AxsacQ_LlLaeenVkfcrHfJcyFX_sero4nMC_XZL0YSACnffU-aKxU5ufd1yQdB6h8H5J_tbFEWT13QEGx9u9ipycpRvOu4V_TMEbPEMdgu8bSAJQyQwEWstva5n6KwhvJ6CO02-I_LpyE7XLTcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/604f2b0c98.mp4?token=XaHgtqlfHa1fLmhbyCZFRLnk2K4glPF5g-R4H3TCDwyUMyhEr166BiFh-QFAIZ1xshLGHe_LtAZXPirmAZhm3mSLW5o5lyPxaVKmVwy5Rc8NSu0MtuQTFM_QvfzDa3HMQl6dnVf1BTA-iefBNFiCBiD8kL63DKBzMfiq54gbekAXbRdrJcEaaz2cooFgGnoAt66AxsacQ_LlLaeenVkfcrHfJcyFX_sero4nMC_XZL0YSACnffU-aKxU5ufd1yQdB6h8H5J_tbFEWT13QEGx9u9ipycpRvOu4V_TMEbPEMdgu8bSAJQyQwEWstva5n6KwhvJ6CO02-I_LpyE7XLTcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرشایمر، نظریه پرداز معروف آمریکایی: ترامپ با امضای تفاهم‌نامه اسلام‌آباد سند شکست آمریکا را امضا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/152165" target="_blank">📅 20:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdvtSG18k0dhx7Y81AjLeUsIpvh-sc9aqExuqvYT9BpHbhN5foPk3NqsLdC5Wg8mgwbZn0SBCdM0cDOXILXhe6ZyNP4tEC6GbUt16S4WPXLsFurlWtyhmAxua2bTE-EDl7Jg1p746clrfITRl2ZTnyuSMYirn06BdcthsiuxgYqMNyfQB2XePK6C3-PF8GO4DlmsrdaNhtdeGb6GTc8kLC7c3AgJqFSX3YX_qFqE8g6Y3aAEZjDO3nzcdwqAMfsxPtAtG3ZLaU3kznLYcZxHW30YABM_mSjvYqd5yL3Sr22XvoTHZ7DHCdms10VIbcNJbx3AWm-IjewDGTbl4B-FUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ در تروث سوشال:
اگر ممدانی می‌تواند با ترامپ به خوبی کنار بیاید، چرا شومر و جفریز نمی‌توانند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/152164" target="_blank">📅 20:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اسرائیل امشب در مورد ایران جلسه امنیتی برگزار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/152163" target="_blank">📅 20:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189ea383a3.mp4?token=AssNwKAZkkLZ5h5NcmMfsz6EzjJBqowNAf5etjYHOUjIAH5STd_CTZyCnbxqB3vw6m1ZOUPP5do6qIaVaCj2Pm_ZY67ZBaJjxBaK-pDbt7kb2W0nHOMpOdVDBPnDlvG71MlP2uSzkTkEld6BcEiVDAfksYStV0VcPcsDSYvQZG0xnWv_vCzlnOno7VCrDgYUmwICU1sDsJbGvdPi4VvS2NCGhvJ5GBydaVZcFzySmyFmzhxOQfXI_rntj7PSCiYsRSikL8a3l4iRf_Dr06Ewpl4gRc1pMXSSsyDlHLHXioWxeBs_YzwuvkabONPQdpRR9kJiT4Ig4cUXmLOhmUwMKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189ea383a3.mp4?token=AssNwKAZkkLZ5h5NcmMfsz6EzjJBqowNAf5etjYHOUjIAH5STd_CTZyCnbxqB3vw6m1ZOUPP5do6qIaVaCj2Pm_ZY67ZBaJjxBaK-pDbt7kb2W0nHOMpOdVDBPnDlvG71MlP2uSzkTkEld6BcEiVDAfksYStV0VcPcsDSYvQZG0xnWv_vCzlnOno7VCrDgYUmwICU1sDsJbGvdPi4VvS2NCGhvJ5GBydaVZcFzySmyFmzhxOQfXI_rntj7PSCiYsRSikL8a3l4iRf_Dr06Ewpl4gRc1pMXSSsyDlHLHXioWxeBs_YzwuvkabONPQdpRR9kJiT4Ig4cUXmLOhmUwMKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان روحانی و ظریف علیه حجاب اجباری
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/152162" target="_blank">📅 20:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از مقامات ۵ سازمان اطلاعاتی اروپایی گزارش داد روسیه در حال گسترش برنامه‌های ترور مدیران ارشد صنایع دفاعی، به‌ویژه تأمین‌کنندگان پهپاد برای اوکراین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/152161" target="_blank">📅 20:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152160">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: دیگر پاسخی به پیشنهاد های آمریکا برای توافق نمی‌دهیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/152160" target="_blank">📅 20:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152159">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزارت دفاع روسیه: ما یک مرکز لجستیکی در میکولايف و یک کشتی باری نظامی که به سمت بندر چورنومورسک در حرکت بود را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/152159" target="_blank">📅 20:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن (حوثی ها): از آسمان فرودگاه‌های سعودی دور شوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/152158" target="_blank">📅 20:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152157">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIKzNyTmxhtpOsbjpHlh9iey2lMVSQr_HfcWm-7UIBCqsZcOsxsQmcRk3uKWJXZoihEeDBSsKx45XR2TfQnFaTiwNl8F_2Inmf60iNotY38ZuL5V_RFAGAwdHiNh19VJsxFg1GViGvBvlk7lfrwPvHEerAuX_i1Xx-B-UQ5ZO_NED_7zNYb04HZfTDM-ElD9J0XeMsSH6o-rRDzaTcRkh3pUxvRDsEiIPudNY4UIVYy76ZLXCHo5Svs4HQYMlsNba7BgQZ-GJXyxr1AHK175CV-I76r7eeqXYWF5ymgQBrubmoGg56f69MeGYmNSZX6bmfgwusVbdzCqtr9mQtfztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ده سال پیش با ۳۵ تومن میتونستی پژو پارس بخری، ولی امروز با ۴۰ تومن میتونی داشبورد پژو پارس رو بخری
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/152157" target="_blank">📅 19:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152156">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
هم اکنون گزارش شلیک موشک از جنوب ایران به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/152156" target="_blank">📅 19:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152155">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
انفجارهای جدیدی در شهر ریاض، پایتخت عربستان سعودی، رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/152155" target="_blank">📅 19:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152154">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
زلنسکی: هم اکنون با مقام‌های ایالات متحده صحبت کردم، اوکراین از آتش‌بس انرژی حمایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/152154" target="_blank">📅 19:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152153">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: می‌توانستیم تنگه هرمز را کاملاً ببندیم، اما به دلایل انسان‌دوستانه این کار را نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/152153" target="_blank">📅 19:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152152">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دونالد توسک، نخست‌وزیر لهستان، می‌گوید مردی که مشکوک به توطئه برای حمله به او است، دستگیر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/152152" target="_blank">📅 19:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152151">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
المیادین: نیروهای مسلح یمن به ۷ کیلومتری شهر تعز رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/152151" target="_blank">📅 19:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152150">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/152150" target="_blank">📅 18:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152149">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌
👈
فیلد مارشال محسن رضایی: آمریکا دارایی‌های بسیار گران‌قیمتی در امارات و پیرامون تنگهٔ هرمز دارد که ما هنوز آن‌ها را در میان اهداف خود نگنجانده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/152149" target="_blank">📅 18:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152148">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: اگه دوباره جنگ بشه اینبار به تاسیسات هوش مصنوعی و دارایی های ایلان ماسک تو منطقه هم حمله میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/152148" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152147">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سراج نماینده مجلس: ۹۰٪ مردم خواهان انتقام از دشمنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/152147" target="_blank">📅 18:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152146">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین درباره خاورمیانه: همه می‌فهمند که به دلیل جنگ در خاورمیانه، قیمت‌ها در حال افزایش هستند. آن‌ها به دلیل جنگ در خاورمیانه و مسدود شدن تنگه هرمز افزایش می‌یابند.
🔴
همه این را می‌فهمند. اگر می‌خواهیم با مردم به‌صورت منصفانه صحبت کنیم، اگر می‌خواهیم شفاف باشیم، اگر می‌خواهیم با ملت‌هایمان به‌صورت بازگشایی صحبت کنیم، مردم باید واقعیت را بشنوند
🔴
با مردم بازی نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/152146" target="_blank">📅 18:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152145">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1924f0c44.mp4?token=egHkD9bfqtXkwqbgojXWRTCBE3UZEReiC7QK0MV5zGvu_tCMImxvdc-ogzTQ0KkrMplE88gjxMPsgOrZYLkgTbcwvDPmE_Wg7075kCdGGD8N-7JUEND5CghAcpymBdwAbhOeBclTGE5AUBkUkEW_SWiHKOrFs5RJvNcLWAp0pdaLBPNlqwSmpO68qQgPdOD6AUsbXewEtScCRtr4BFdP6CERIN805M07Vf6s4bekkRE0FCyounImadtkszpKcY94LV19ik4uuoI57OOUtjHWWZH71kp2LrXVyFu3Ht3hdBNtZjm5nT2nOiK09vbYjkk5E5VCWcBBgm_DhiWiDLVSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1924f0c44.mp4?token=egHkD9bfqtXkwqbgojXWRTCBE3UZEReiC7QK0MV5zGvu_tCMImxvdc-ogzTQ0KkrMplE88gjxMPsgOrZYLkgTbcwvDPmE_Wg7075kCdGGD8N-7JUEND5CghAcpymBdwAbhOeBclTGE5AUBkUkEW_SWiHKOrFs5RJvNcLWAp0pdaLBPNlqwSmpO68qQgPdOD6AUsbXewEtScCRtr4BFdP6CERIN805M07Vf6s4bekkRE0FCyounImadtkszpKcY94LV19ik4uuoI57OOUtjHWWZH71kp2LrXVyFu3Ht3hdBNtZjm5nT2nOiK09vbYjkk5E5VCWcBBgm_DhiWiDLVSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از فرماندهان جوخه نوخبا که در ربودن اسرائیلی ها در 7 اکتبر شرکت داشت در عملیات مشترک ارتش اسرائیل (IDF) و شین بت کشته شد. او یکی از رهبران حمله به پاسگاه کیسوفیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/152145" target="_blank">📅 18:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152144">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f80c226d.mp4?token=BnqeubTMVBFwFA3gHVZK4Bs4ltlmCpSc-JuPZjBHNrfL4bfrnztw07og06caSNX9pnoBqgkQEewDA4u_FCFSrfNItQOIkJcN7jvWNbwHOca407btD852In8ouNrlxDfzETZO4UmyQCq2zrucRI5z3z-OXDL3QGMnTUaUbqFu2R3iM6-PZiq0gDtDF_sIGGv1J2THR0JDqxtww02F6r-mRVH2SVAAQDpn1-YPxLL_W2DF3xgJELYKZ9-NcFHMh64D2OM7IwAPcQywgjkyfJBMVqKsbOeHJix5Lqr2dr2juiUs24TYdSrLgoQqLKEmmg4yUJCG3ctjyB__xISDMLrFWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f80c226d.mp4?token=BnqeubTMVBFwFA3gHVZK4Bs4ltlmCpSc-JuPZjBHNrfL4bfrnztw07og06caSNX9pnoBqgkQEewDA4u_FCFSrfNItQOIkJcN7jvWNbwHOca407btD852In8ouNrlxDfzETZO4UmyQCq2zrucRI5z3z-OXDL3QGMnTUaUbqFu2R3iM6-PZiq0gDtDF_sIGGv1J2THR0JDqxtww02F6r-mRVH2SVAAQDpn1-YPxLL_W2DF3xgJELYKZ9-NcFHMh64D2OM7IwAPcQywgjkyfJBMVqKsbOeHJix5Lqr2dr2juiUs24TYdSrLgoQqLKEmmg4yUJCG3ctjyB__xISDMLrFWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین:
ترامپ گفت که اوکراین به یک رئیس‌جمهور جدید نیاز دارد.
🔴
با تمام احترامی که برای رئیس‌جمهور ترامپ قائلیم، انتخاب رهبر به عهده مردم ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/152144" target="_blank">📅 18:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152143">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f92ae82a3.mp4?token=vJbi3PABjdQxua7yKubCM2wYJYx_a2zcAKSLF4n99jMHrbERBp78txEPxgJc00cEn6j2xjL8WXDlPQuB9TYKzivmALiVc0n1iijsoYseDPB0vyzLpa6QZHL_rdarBEOxLjSo33-jBPncz3-KMFHM35_D2j6IsY3wfb03XXrNpeFPi9mQzP20LNlvlgbrO03RPrmoicL3ceMYISZkbWVL1Mj3ATv11yyNZuiJt_WBA404pXeB8X3AsJ54pKCjkUOdHAFk37qaKlBQTg4p7T0G9k_gQYJ-OwQ84Cbv9QAkMXh5lCCi0KvoMOrJuyQYwhJOLBnd0JqbSunDlFSeQbnY6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f92ae82a3.mp4?token=vJbi3PABjdQxua7yKubCM2wYJYx_a2zcAKSLF4n99jMHrbERBp78txEPxgJc00cEn6j2xjL8WXDlPQuB9TYKzivmALiVc0n1iijsoYseDPB0vyzLpa6QZHL_rdarBEOxLjSo33-jBPncz3-KMFHM35_D2j6IsY3wfb03XXrNpeFPi9mQzP20LNlvlgbrO03RPrmoicL3ceMYISZkbWVL1Mj3ATv11yyNZuiJt_WBA404pXeB8X3AsJ54pKCjkUOdHAFk37qaKlBQTg4p7T0G9k_gQYJ-OwQ84Cbv9QAkMXh5lCCi0KvoMOrJuyQYwhJOLBnd0JqbSunDlFSeQbnY6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین:
اگر ترامپ واقعاً می‌خواهد انتخاباتی در اوکراین برگزار شود، لطفاً به پوتین بگویید: به ما دو ماه، ۶۰ روز آتش‌بس کامل — ۶۰ روز — بدهید و ما انتخابات را سازماندهی خواهیم کرد
🔴
البته، ما برای هر انتخابی از سوی مردممان آماده خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/152143" target="_blank">📅 18:21 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
