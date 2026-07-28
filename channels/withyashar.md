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
<img src="https://cdn4.telesco.pe/file/J6KcmeRY7xxAcRrqbvEsL8tGxE1IYZPA_x7ZyZDhgqsa-FxI5TxDmqt_cieWiMNeVXu4m4io4lpVGk2b7EmYF596Pj5VGC-_b7OkBthCMkohVBlc9PdJs5vmNOLqMoSWbd3-J30R6bmXWE9EzBEROrIz2a6-B8scRSd2EazueSSLvNU9h8PG2KVcH46PdScI1rg66BWqmLJ5gBq6X3uh7Epw7XWhtowDn4-PZk0COt7SbcO-Ir_Y3Nuw03pXqwWP4ianlB65AhpRnPYiisetuI9jMffvtXTZq1_BXTAM3gERFWOgcxCq4hOuD5U4z9wBI0_GBiy7wYK1v4i0-0xxRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 18:42:27</div>
<hr>

<div class="tg-post" id="msg-19887">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b359db05.mp4?token=ca2KUv9ZFbuPRbzJn6LfBGApgjPJeuxJnU82okDHTGtfkNZFp8z-_lMjh0phrzha9NOdqXEvkBZBVVDSrDlnr3nARAqEWLGBiQFa7CAO6NQ3PuzZ5UTsnP-Y6ULFks7XoDL87Oq1v_6en8Vtmkd_PS37H4T0FasRb2597aDU3iq0RIlRtF3yAaciyBkFA3xzIwlcr4ojoO4aoXDjNjW9oxQSiKTUQMvQN5st34qQJW1RkrafrPtaA76gE36NZLwcm67URrvKlRJi07VJzdxl1cfMGaOxFIjiW-mmKHC1SsmQYOGdvclBd76Ei5nCY3D02jP16ae3KsLJUUnWEKHL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b359db05.mp4?token=ca2KUv9ZFbuPRbzJn6LfBGApgjPJeuxJnU82okDHTGtfkNZFp8z-_lMjh0phrzha9NOdqXEvkBZBVVDSrDlnr3nARAqEWLGBiQFa7CAO6NQ3PuzZ5UTsnP-Y6ULFks7XoDL87Oq1v_6en8Vtmkd_PS37H4T0FasRb2597aDU3iq0RIlRtF3yAaciyBkFA3xzIwlcr4ojoO4aoXDjNjW9oxQSiKTUQMvQN5st34qQJW1RkrafrPtaA76gE36NZLwcm67URrvKlRJi07VJzdxl1cfMGaOxFIjiW-mmKHC1SsmQYOGdvclBd76Ei5nCY3D02jP16ae3KsLJUUnWEKHL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو برای دیدار با ترامپ وارد کاخ سفید شد
@WarRoom</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/withyashar/19887" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19886">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اتاق جنگ با یاشار : طبق تجربه و تحلیل من این شرایط دوهفته دیگه پر پرش دوام بیاره و باز دعوا شروع میشه
😁
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/withyashar/19886" target="_blank">📅 18:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19885">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIkSuN7e0Ets6w28OoIMRKfSBcn5Q7UPaPNEU8ahkfGnDDmH4xIi3bT8MjVsxuPFtArwXsarqk3zlIC0qsK2aTiNp5tWQdD2Thd4y5-DLqK0x5CeadgpX3JExttflBLlcoPaPxF0v8WJgqlYuTo5ieQfnTLVXkIOL4d3BhN_Wf4TMDkFrUvFRHAPIP2zI3ZZ6nvS3_jqCG6745LKXBrrYkRDo2B6F1a50uiPoZd7aFxuwXCqWas0WYnzm3iwCYIY5_9fb9xJnOKWr7joIYS894B1PqpKzQRUOXLW5uYKqqHqJzZOgGqXpG9SQ2p-o2P6ujO7gFjD1AeQ5yuD0p4xGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تابوت لیندسی گراهام با استقبال خواهرش و اعضای کنگره ایالات متحده وارد ساختمان کنگره شد  جی‌دی ونس، معاون ترامپ پیش از مراسم تشییع جنازه امروز، برای ادای احترام به لیندسی گراهام وارد ساختمان کنگره شد طبق گزارش CBS News، مراسم امروز با آیین ورود به ساختمان کنگره…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/19885" target="_blank">📅 18:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19884">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c954e618d1.mp4?token=BOua-pT-DSGN5IVUSyxWHtGuKO-8OF0aVcCzJCe-OhrLMZV7huxEKjxWj9jmwsbZQgAqfRt2UYtAqzXS8QN1ttDW8fU6vuxdv1iU4d-72c2hJit3Oi7dwJlketPmsKdfQW_2BEFm45yxso_ZFpVuSQOPsVnm-BHexAVBCzCXxziJ_yi5A_0v1o_DTxuZbAYoKSw2O_xYH9uZuDzyPvSUj6xA5uRMH03PXUGjtVl-ceyeWmwisj4pGaQyoZSj65XM-Ymo247xe0USM7t1COJtQb8Tnu1pBFNjTqjmjzBxqLN9UcO7M429-CoV-_ee7AK4_exYsoNdYq0J2EOWY2kmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c954e618d1.mp4?token=BOua-pT-DSGN5IVUSyxWHtGuKO-8OF0aVcCzJCe-OhrLMZV7huxEKjxWj9jmwsbZQgAqfRt2UYtAqzXS8QN1ttDW8fU6vuxdv1iU4d-72c2hJit3Oi7dwJlketPmsKdfQW_2BEFm45yxso_ZFpVuSQOPsVnm-BHexAVBCzCXxziJ_yi5A_0v1o_DTxuZbAYoKSw2O_xYH9uZuDzyPvSUj6xA5uRMH03PXUGjtVl-ceyeWmwisj4pGaQyoZSj65XM-Ymo247xe0USM7t1COJtQb8Tnu1pBFNjTqjmjzBxqLN9UcO7M429-CoV-_ee7AK4_exYsoNdYq0J2EOWY2kmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش
لحظه ورود زلنسکی به کاخ سفید
@WarRoom</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/withyashar/19884" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19883">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c7fe4f226.mp4?token=BmUtQN3u89UFJv6tCM1ylyEeJQPGXdLx8gLq2J4ENIegqBX2zGQvCJrD2I9EThjjvPk-x6f03Dv1g30Tn_k0kdlQBmtfr_qQh75bN5CEllHL1M7LDGi8xFxpfs9rWRAd17z7nlITviv9oYCP-denpbg6EJzt7kJFP4yrQs7ba7_RcJODkWlFZjSmrqkMzchvkT8Lelp7ezvuNMfH1mrjGCQD7PjwyMM6uYMY4lSyuI1y04vOq3MrGLZ41grr0-6L-Of_kuUjUqySH91uTUwHMVXFwNNHvWBem1Y5CJNoS9JW59lvNdJ4ouvccl7jJHjBVluWaX7tNGdKsm1FrK9EKRd_wTDcxFLtJZsvJtFOtNsthnkKG5oT5lfkhcCn1HTK5v1l3RNe-co-DhGdenpCilzL16_ays8D3NK9q9hjSrQdRFAJ-QyL1GIUQ9rVw24tGddt48fl2j-NAZnyjoaxuxOnaJm2b-fLtoS2-pQqhWCFyBLKeXoPC2Hw1rRVlR-aBgLrR_KqWZMcYhFOw9uS5BHRHXibMAt_8GVfQhbvytOhgqoV6LJd-5WDEhBEHEtb3bMzVRmzjKqgmsSxnnJ6XlsCeEj2RkLTqLiYNxjHBr83Ua6bqB64G7nYUR0e2KPsrDKdp7b0Xn7Dj2UWB62tOe_tghJZr9eSxO3mRGNXQVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c7fe4f226.mp4?token=BmUtQN3u89UFJv6tCM1ylyEeJQPGXdLx8gLq2J4ENIegqBX2zGQvCJrD2I9EThjjvPk-x6f03Dv1g30Tn_k0kdlQBmtfr_qQh75bN5CEllHL1M7LDGi8xFxpfs9rWRAd17z7nlITviv9oYCP-denpbg6EJzt7kJFP4yrQs7ba7_RcJODkWlFZjSmrqkMzchvkT8Lelp7ezvuNMfH1mrjGCQD7PjwyMM6uYMY4lSyuI1y04vOq3MrGLZ41grr0-6L-Of_kuUjUqySH91uTUwHMVXFwNNHvWBem1Y5CJNoS9JW59lvNdJ4ouvccl7jJHjBVluWaX7tNGdKsm1FrK9EKRd_wTDcxFLtJZsvJtFOtNsthnkKG5oT5lfkhcCn1HTK5v1l3RNe-co-DhGdenpCilzL16_ays8D3NK9q9hjSrQdRFAJ-QyL1GIUQ9rVw24tGddt48fl2j-NAZnyjoaxuxOnaJm2b-fLtoS2-pQqhWCFyBLKeXoPC2Hw1rRVlR-aBgLrR_KqWZMcYhFOw9uS5BHRHXibMAt_8GVfQhbvytOhgqoV6LJd-5WDEhBEHEtb3bMzVRmzjKqgmsSxnnJ6XlsCeEj2RkLTqLiYNxjHBr83Ua6bqB64G7nYUR0e2KPsrDKdp7b0Xn7Dj2UWB62tOe_tghJZr9eSxO3mRGNXQVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت لیندسی گراهام با استقبال خواهرش و اعضای کنگره ایالات متحده وارد ساختمان کنگره شد
جی‌دی ونس، معاون ترامپ پیش از مراسم تشییع جنازه امروز، برای ادای احترام به لیندسی گراهام وارد ساختمان کنگره شد
طبق گزارش CBS News، مراسم امروز با آیین ورود به ساختمان کنگره آغاز می‌شود. تابوت سناتور گراهام توسط تیم حمل‌کنندگان نیروهای مسلح حمل خواهد شد تا خدمات او در نیروی هوایی ارتش آمریکا گرامی داشته شود و سپس تحت نگهبانی پلیس کنگره قرار می‌گیرد. این مراسم در کنگره برگزار می‌شود و حضور برای عموم آزاد نیست.
مراسم اصلی تشییع جنازه ساعت ۲ بعدازظهر به وقت محلی در کلیسای جامع ملی واشنگتن (Washington National Cathedral) برگزار خواهد شد.
دونالد ترامپ سخنرانی خواهد کرد و نخست‌وزیر اسرائیل بنیامین نتانیاهو و رئیس‌جمهور اوکراین ولودیمیر زلنسکی نیز در آن حضور خواهند داشت.
@WarRoom
*ویدیو رو خودم از لایو مراسم رکورد و خلاصه کردم</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/withyashar/19883" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19881">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6rrXrIUY800FVEVxqAQ7J6GiLlN8HPl-8C08yG-aj_NSXypjl5aD9TWdkZXd2gX19yPJZ0MJ6GosNkCEXxqbLfkNrUOtZpetwKKMwPUyGVI3dnkVadKeZqB8MAtkOPngCM-nwWdbLvQDzrlvbvSyzwF5zHVo8iIEg8Rv6WryW8ITZ1IFb0CVDwx-IJpuiU2ILeew0r7o7zD7YqAQr6RO0XFQNC51GSoDaRRaSvw1KhCXXrgvSouQfn0FnSpm1r2n4O8ATb_R9-X6GfIz-iiC2fvs-lqBufI0757SKegwpaVOFYtiRcj94TpYLf7L4Qys79D4utV2ou1OEODqyNYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltT5tlvdkCmw187WCaA0SY225Mz-tQ9uRycOtPEBHCyuN9PgehJemeWrJ4Fi48Hw7a42f9XqoviibuAssvo5OSsnTO6seR29qY0uyzlIHqX9iWjqt9Zc8gGpNBvXgbLiZZqOK6GHNM2mHpQtdEmLJCZoTHQrMF32Mwn9sMBhoULUaLEr9dGZtbAWYVu2e2uFKUfuYmlf2-sSvAh9b1VUAxYu1gtCTgkcHoovR4MqMCgTaE3Tu9NK2DlWqiErj4rheHwPvMoSkJvUxk3FnrhE1AUIEXMfRAvNYmQW5tdnXG9iPjfuGUH7Mm-vbxbcvDVVNec2E9LXDLkwdsLCzOhdMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واکنش مارک لوین به اعدام و سرکوب مردم در اصفهان:
با این نازی‌ها مذاکره نکنید.
مردم رو مسلح کنید
@WarRoom
عکس دوم چهره کریه قاضی اصفهان که حکم داد</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/19881" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19880">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگر توافق نکنیم به راحتی کوه کلنگ را از بین می‌بریم ترامپ به فاکس :" من دقیقاً می‌دانم در کوه کلنگ چه می‌گذرد، مشکل بزرگی نیست. ما سایت‌های هسته‌ای آنها را از بین بردیم و اگر توافق نکنیم، باید کلنگ را از بین ببریم. اگر توافق نکنیم، خیلی راحت آن را از بین خواهیم…</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/19880" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19879">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049afcae48.mp4?token=r-IAnu3dDH62mdWfShSn8IswKRPmntFZ2lK47kuFXXKJ98jO9pFMqp-iaMH2UrCxGXROVGotXNFvwOl5abNQcKAc0RluHXpsgagUngS5lkjavgFTmF4AAGchWlH8eZpo10SGy6-bypBR1ndkkEj0jklp_gxYwPWIPmX75DPveEYEBSA7I8S1WZe9DslMof5phR8lppEqnXuBMw7ooQj61I7SpWP0hggxNqUmOMPdJPosTj8jnBCYcaLdDDuBhvvunUpDEAIgYLEqLkgkRUe9THkYA5TBPTJ7QOm3SDBNaPWaaMu0jfxil1yf-Tonpu5p3PZvwomNy3HGSt094xUcqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049afcae48.mp4?token=r-IAnu3dDH62mdWfShSn8IswKRPmntFZ2lK47kuFXXKJ98jO9pFMqp-iaMH2UrCxGXROVGotXNFvwOl5abNQcKAc0RluHXpsgagUngS5lkjavgFTmF4AAGchWlH8eZpo10SGy6-bypBR1ndkkEj0jklp_gxYwPWIPmX75DPveEYEBSA7I8S1WZe9DslMof5phR8lppEqnXuBMw7ooQj61I7SpWP0hggxNqUmOMPdJPosTj8jnBCYcaLdDDuBhvvunUpDEAIgYLEqLkgkRUe9THkYA5TBPTJ7QOm3SDBNaPWaaMu0jfxil1yf-Tonpu5p3PZvwomNy3HGSt094xUcqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران گفت: ما محاصره را برداشتیم، اما بعد آن‌ها توافق را نقض کردند، بنابراین دوباره محاصره را برقرار کردیم.آن‌ها توافق را می‌شکنند.دیگر نمی‌توانیم اجازه دهیم که توافق‌ها را نقض کنند
@WarRoom</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/19879" target="_blank">📅 16:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19878">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f30f4312.mp4?token=QO-lUGO5pLyUKl6ujh50UEgSJrkxrPj-iDnkVVm5oVmiUHyUAql8uHZnfn1s9bKnpa1f4lklK9DsKgqFKBFFokUaFBzigTpFmQdFM2n4ZL8RYqsIzYZuni6yrsMoENVsp2VgaIaM90a-4X7Uw8XxhEFJv-6MYaomW35loTeybboOyM_y540t_OQFtaI2Q35qAIaM5vv6G4xLyRxz9v-cI3pvMzDDIwc6LZpb0c4kri3cnHcnljlZvxQL2PjkAWQ0zic227cEsHE1DTxLfI8_qbkivYEF_yJPuFa3LTgROTedaRQb0ERFeZNDdMMAiFS3uz-a3_ybg0hSTElgsDnuKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f30f4312.mp4?token=QO-lUGO5pLyUKl6ujh50UEgSJrkxrPj-iDnkVVm5oVmiUHyUAql8uHZnfn1s9bKnpa1f4lklK9DsKgqFKBFFokUaFBzigTpFmQdFM2n4ZL8RYqsIzYZuni6yrsMoENVsp2VgaIaM90a-4X7Uw8XxhEFJv-6MYaomW35loTeybboOyM_y540t_OQFtaI2Q35qAIaM5vv6G4xLyRxz9v-cI3pvMzDDIwc6LZpb0c4kri3cnHcnljlZvxQL2PjkAWQ0zic227cEsHE1DTxLfI8_qbkivYEF_yJPuFa3LTgROTedaRQb0ERFeZNDdMMAiFS3uz-a3_ybg0hSTElgsDnuKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرارگاه تروریستی خاتم الانبیا
هشدار داد هر شرکت یا کشوری که بر اساس طرح غرامت ایالات متحده برای کشتی‌های آسیب‌دیده در طول جنگ، از دارایی‌های مسدود شده ایران وجهی برداشت کند، از عبور از تنگه هرمز منع خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/19878" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19877">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ در مورد ایران:
لیندسی گراهام یک جغد جنگی در مورد ایران بود، اما در چند هفته گذشته، شروع به این فکر کرد که یک توافق بهتر از نابودی بقیه ایران خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/19877" target="_blank">📅 16:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19876">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa71f5aa10.mp4?token=G5kn4vIQ_xxHRUdNqan0b29UllLRWDVNha7iU0sDqV2ra2hC5jsNbu2Z1vJuU5Bfaf2k8TS9sFZccGUvTEW7A_FogqAkDJIWJ4L_zTlkeMml4i4IhYc4tFhJfPfJ-seid2USq69jpGyWzi_EfAwURJjPeoHAv0vhUMmC08tjIJIjjqEV3IbHCLl-p0h3g-llBzWun9APdp__mg86WtKrOKPgR10xfQDxY8EJVCVCDQs87O8p1nnYFSK3FM51Wbmi6-dirdnPGhN3ek-rDFJf2aRKVWDb9pzMD7sN_cAvm54IgNDgPmtmlvRTolFyPokr2hsYrts7VNU_e-uqNF1aQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa71f5aa10.mp4?token=G5kn4vIQ_xxHRUdNqan0b29UllLRWDVNha7iU0sDqV2ra2hC5jsNbu2Z1vJuU5Bfaf2k8TS9sFZccGUvTEW7A_FogqAkDJIWJ4L_zTlkeMml4i4IhYc4tFhJfPfJ-seid2USq69jpGyWzi_EfAwURJjPeoHAv0vhUMmC08tjIJIjjqEV3IbHCLl-p0h3g-llBzWun9APdp__mg86WtKrOKPgR10xfQDxY8EJVCVCDQs87O8p1nnYFSK3FM51Wbmi6-dirdnPGhN3ek-rDFJf2aRKVWDb9pzMD7sN_cAvm54IgNDgPmtmlvRTolFyPokr2hsYrts7VNU_e-uqNF1aQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها موافقت کردند که سلاح هسته‌ای نداشته باشند. اساساً، ما باید این را رسمی کنیم، اما آنها موافقت کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/19876" target="_blank">📅 16:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19875">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1021ee49.mp4?token=OXekXUSMlrjlfzrIUCoQAa_ubNodK6EvU4ah4qbNaR6Khx_pIHu_fJ7zsfsHMuIhn3o-rWkcnWTGJ1qzceBKH1k2L3O1RjBoZJwsMTb-fEmGbfUseEY4_Q1CNJAIAc0CEmiiHHxC93RyZKFJtMizIb7p5Ppu9SQbA0-8EJz8GnKr_cx-voxpob3wVLHLIqU90oZ3q6z_qm6Ewl6J1lkuvx5CH6Jox5HaCEjD_Bm5Z9sn5n_dapZLXZR94-WgDPDwMCYT3kLSL__VoxwTNXUTK-tMfymEsrv_DK8gYNV_1_bt-hRo3nfQV8g_nSdMnH_28Tt22-At7w7gZTFZtNQWYWd34DnC80ebZzP2eYocJJQpFRWD3f5-TfLfR3OYJIBypiB8ugmxZDODJZpK3N9cWSMphG4u7H1ZvBStWAvFfiswTpslLAnZYje5Q_r3WGWmlfUlXEiKKKtVG1cnORZq1ZgMW_shrl1_KU99T0WLA5q1HCxmY5W38CelAsWte8stdQL2KdzPNglUWj3GJjUTmSOTFGP81efhFjyAjhi1WWl6NhCvzmPAViL_n7zm3psm81DtTNCpf0pfnROvOt2Fj3vnb4OM2UWEzkmUzPCieh9OoH2ZsHh7JLnMEArp4db3qDthApdBjxuqBMdoVWtcQ2E_BkJPrl_QK0vrcOTamSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1021ee49.mp4?token=OXekXUSMlrjlfzrIUCoQAa_ubNodK6EvU4ah4qbNaR6Khx_pIHu_fJ7zsfsHMuIhn3o-rWkcnWTGJ1qzceBKH1k2L3O1RjBoZJwsMTb-fEmGbfUseEY4_Q1CNJAIAc0CEmiiHHxC93RyZKFJtMizIb7p5Ppu9SQbA0-8EJz8GnKr_cx-voxpob3wVLHLIqU90oZ3q6z_qm6Ewl6J1lkuvx5CH6Jox5HaCEjD_Bm5Z9sn5n_dapZLXZR94-WgDPDwMCYT3kLSL__VoxwTNXUTK-tMfymEsrv_DK8gYNV_1_bt-hRo3nfQV8g_nSdMnH_28Tt22-At7w7gZTFZtNQWYWd34DnC80ebZzP2eYocJJQpFRWD3f5-TfLfR3OYJIBypiB8ugmxZDODJZpK3N9cWSMphG4u7H1ZvBStWAvFfiswTpslLAnZYje5Q_r3WGWmlfUlXEiKKKtVG1cnORZq1ZgMW_shrl1_KU99T0WLA5q1HCxmY5W38CelAsWte8stdQL2KdzPNglUWj3GJjUTmSOTFGP81efhFjyAjhi1WWl6NhCvzmPAViL_n7zm3psm81DtTNCpf0pfnROvOt2Fj3vnb4OM2UWEzkmUzPCieh9OoH2ZsHh7JLnMEArp4db3qDthApdBjxuqBMdoVWtcQ2E_BkJPrl_QK0vrcOTamSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
اگر به عقب برگردم و کار را تمام کنم، همانطور که بعضی‌ها دوست دارند، با پل‌ها - خیلی راحت می‌توانم بیشتر پل‌هایشان را در کمتر از یک ساعت خراب کنم.اما می‌دانید، ساخت یک پل برای آنها 10 سال طول می‌کشد. پل‌ها طولانی‌ترین زمان را می‌برند و نیروگاه‌ها در رتبه دوم قرار دارند.من می‌توانم نیروگاه‌ها را در عرض یک روز از کار بیندازم. تمام نیروگاه‌هایشان از بین خواهند رفت.
فکر می‌کنم حدود 91 میلیون نفر بدون برق، بدون پل، باید زندگی کنند. و این یک تعادل بسیار بسیار ظریف است.آنها می‌دانند که اگر آنها توافق نکنند، من این کار را خواهم کرد.پل‌ها به معنای واقعی کلمه از بین خواهند رفت. در کمتر از... به نظرم در دو ساعت، بیشتر پل‌ها، پل‌های اصلی، همه از بین خواهند رفت.و نیروگاه‌ها در یک روز.اگر بتوانم از انجام این کار اجتناب کنم، می‌خواهم از آن اجتناب کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/19875" target="_blank">📅 16:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19874">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8482ff12f2.mp4?token=KwL2kh5Uq0Bf9g--L1E61YqEbDkplfNw24FwkTVvz4lL9XI_rAMP-Ju6ehbCL71eFCzALokphKcO4lCayVwWG65Bvx4ODMgyZDErzopScckvUFKCm9o7Am8R-mGQEap2DvFESxNXYmtMKWy0PAtQ97EB4FD_1G9MZpgNWnEBg6W8i2mw9eF1jt_YYlTod8VD4XKveUvdYiXyBjAAF7a1ibVKWtFAShWpEZ9kbh0FUPiT4ifGGksXFN8PRKipEK_PaTAhV3By8anKjaFkvH4xxf8BobTW5LYhhm_js9yx64PrtTWMPoyVnhj3mfgX-KuCAr_SV84l4Geo4QIMVWjOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8482ff12f2.mp4?token=KwL2kh5Uq0Bf9g--L1E61YqEbDkplfNw24FwkTVvz4lL9XI_rAMP-Ju6ehbCL71eFCzALokphKcO4lCayVwWG65Bvx4ODMgyZDErzopScckvUFKCm9o7Am8R-mGQEap2DvFESxNXYmtMKWy0PAtQ97EB4FD_1G9MZpgNWnEBg6W8i2mw9eF1jt_YYlTod8VD4XKveUvdYiXyBjAAF7a1ibVKWtFAShWpEZ9kbh0FUPiT4ifGGksXFN8PRKipEK_PaTAhV3By8anKjaFkvH4xxf8BobTW5LYhhm_js9yx64PrtTWMPoyVnhj3mfgX-KuCAr_SV84l4Geo4QIMVWjOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر توافق نکنیم به راحتی کوه کلنگ را از بین می‌بریم
ترامپ
به فاکس
:
" من دقیقاً می‌دانم در کوه کلنگ چه می‌گذرد، مشکل بزرگی نیست. ما سایت‌های هسته‌ای آنها را از بین بردیم و اگر توافق نکنیم، باید کلنگ را از بین ببریم. اگر توافق نکنیم، خیلی راحت آن را از بین خواهیم برد."
@WarRoom</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/19874" target="_blank">📅 16:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19873">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رویترز به نقل از یک منبع خلیج فارس:
عمان حمایت کشورهای خلیج فارس را برای طرحی که به تهران اجازه می‌دهد داوطلبانه برای استفاده از تنگه هرمز هزینه دریافت کند، جلب کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/19873" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19872">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رسانه‌های عبری: دفاتر نتانیاهو و زلنسکی در حال هماهنگی برای دیداری سه جانبه در واشنگتن هستند؛ با وجود سردی روابط، دو طرف ، ولی در موضوع ایران منافع مشترکی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/19872" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19871">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec75b87ae.mp4?token=RSQhnfHBnYtWKak5QPXDlH_KGVycDR3iaUCCjvoURJK9z987w6dlR-s3OJ_IoGwvhm41kwQKHj_uJ0TTi9CgMKzyZfeoVao-SZW1aZHJluMqhTHGt40cdOoLFmyBVGMYDIuuNeBDmw-USczzOd-Z-UJWhyxyMvJcfUjOIygQAgvlWKsJFwGatiSZrxtMdQfUoGCCujdsSN-hbJyA7_F9xfYcPe2ibDja35eruGnrnebtueE94C1gCeCwSTg1GNHuipfhkqjEfUyzicC2K_vmGtOuYjKzElTabVkPA0qh9OJidwMHHRjZoG0EnSQFiCzIr8FTe6gxInGvtAlvZjOALIqfARdmWJdUz_5xVmouEJiL4FRr2sY_dooMLIn2yH9cYdBr4H-LAGcdaBBQg69bNR0sLwbC7_10WlnaXHWjJF6PouBuLcIjQVoqSYjgdcVXjcDX_Rkfl5QrCOBkvpxCFKDQo1NrZNonT9yS-mtnAv-LAsaARqF2yMyOJK54o69wtns6q0CIZ1pY-jDkH5U7o79NdS_v99h19PGCZa-wgwtrd3_OIHyvp4iR5Ymy_q6u6iPBVJ6PlWWxQM-P5V4umDOi4wzzYrjp1ndSwTGEkrJrgFrmdH2h6p6JK3rVcBm3wE7yuq5cUplupsiSFbdeHto-JQwjBh8SP5szQ-1rWTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec75b87ae.mp4?token=RSQhnfHBnYtWKak5QPXDlH_KGVycDR3iaUCCjvoURJK9z987w6dlR-s3OJ_IoGwvhm41kwQKHj_uJ0TTi9CgMKzyZfeoVao-SZW1aZHJluMqhTHGt40cdOoLFmyBVGMYDIuuNeBDmw-USczzOd-Z-UJWhyxyMvJcfUjOIygQAgvlWKsJFwGatiSZrxtMdQfUoGCCujdsSN-hbJyA7_F9xfYcPe2ibDja35eruGnrnebtueE94C1gCeCwSTg1GNHuipfhkqjEfUyzicC2K_vmGtOuYjKzElTabVkPA0qh9OJidwMHHRjZoG0EnSQFiCzIr8FTe6gxInGvtAlvZjOALIqfARdmWJdUz_5xVmouEJiL4FRr2sY_dooMLIn2yH9cYdBr4H-LAGcdaBBQg69bNR0sLwbC7_10WlnaXHWjJF6PouBuLcIjQVoqSYjgdcVXjcDX_Rkfl5QrCOBkvpxCFKDQo1NrZNonT9yS-mtnAv-LAsaARqF2yMyOJK54o69wtns6q0CIZ1pY-jDkH5U7o79NdS_v99h19PGCZa-wgwtrd3_OIHyvp4iR5Ymy_q6u6iPBVJ6PlWWxQM-P5V4umDOi4wzzYrjp1ndSwTGEkrJrgFrmdH2h6p6JK3rVcBm3wE7yuq5cUplupsiSFbdeHto-JQwjBh8SP5szQ-1rWTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فروریختن یک مرکز خرید در ژاپن در پی وقوع زلزله ۷/۱ ریشتری
به گزارش "ان اچ کی"، شمار زیادی زیر آوار گرفتار شده و شماری مصدوم شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/19871" target="_blank">📅 15:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19870">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آمیت سگال:در اقدامی که از دونالد ترامپ کمتر دیده می‌شود، دیدار او با بنیامین نتانیاهو دور از حضور دوربین‌ها برگزار خواهد شد؛ موضوعی که پیام‌های زیادی در خود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/19870" target="_blank">📅 15:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19869">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏شالوم بن حنان، از مقامات ارشد پیشین سازمان امنیت داخلی اسرائیل (شاباک)، گفت در طول سال‌ها صدها هزار حساب کاربری رباتی که بیشتر آن‌ها وابسته به رژیم جمهوری اسلامی بودند، شناسایی و مسدود شده‌اند. به گفته او، این شبکه‌ها با هدف مداخله در انتخابات اسرائیل، تأثیرگذاری بر افکار عمومی و ایجاد هرج‌ومرج فعالیت می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/19869" target="_blank">📅 15:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19867">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزیر جنگ اسرائیل:ما قویاً خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
۷۰ درصد غزه را نابود کردیم و الگوی آن را به جنوب لبنان منتقل کردیم.
ایالات متحده در موضوع ایران ملاحظات و منافعی دارد که با منافع اسرائیل متفاوت و فراتر از آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19867" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19866">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال ۱۲ اسرائیل , وزیر دفاع کاتز فاش کرد: جنگنده‌های آمریکایی از اسرائیل برای انجام حملات به ایران به پرواز درمی‌آیند‌ و ایرانی‌ها از این موضوع آگاه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19866" target="_blank">📅 13:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19865">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مهاجرانی: هواپیمای تازه‌خریداری‌شده در فرودگاه بوشهر بر اثر اصابت موشک منهدم شد؛ تنها بخشی از دم هواپیما باقی مانده است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19865" target="_blank">📅 12:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19864">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام کاخ سفید: ترامپ در کاخ سفید با زلنسکی و نتانیاهو به طور جداگانه و پشت سر هم دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19864" target="_blank">📅 11:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19863">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :گزارش رسانه های غیررسمی در اینستاگرام و تلگرام نادرست است مبنی بر اجرای حکم ۳ نفر . دیشب مردم اصفهان درگیر شدند تیر اندازی شد و جلادان فقط توانستند دو نفر از عزیزان را اعدام کنند و یک نفر اعدام نشد. @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19863" target="_blank">📅 11:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19862">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مدیرکل مدیریت بحران استانداری اصفهان:صداهای شبیه به انفجار در برخی مناطق جنوب و غرب اصفهان، بهارستان و حومه ارتفاعات صفه و شهر ابریشم شنیده خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19862" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19861">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی دولت: سهمیه بنزین ۳ هزار تومنی از ۱۰۰ لیتر به ۵۰ لیتر کاهش پیدا کرده
اما هنوز هیچ تصمیمی به صورت جمع‌بندی شده برای قیمت بنزین در جایگاه نگرفتیم
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19861" target="_blank">📅 11:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19860">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏زلنسکی و نتانیاهو همزمان به کاخ سفید رسیدند
‏ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، و نتانیاهو، نخست‌وزیر اسرائیل، همزمان وارد کاخ سفید شدند تا در دیدارهایی جداگانه با پرزیدنت ترامپ گفت‌وگو کنند.
‏همزمانی حضور این دو رهبر در کاخ سفید، گمانه‌زنی‌ها درباره احتمال دیداری محرمانه میان آن‌ها برای جنگ همه‌جانبه با رژیم جمهوری اسلامی را افزایش داده است.
‏این دیدارها در شرایطی انجام می‌شود که پرونده‌های امنیتی مهمی از جمله جنگ اوکراین و تهدیدهای مرتبط با رژیم جمهوری اسلامی در دستور کار واشنگتن قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19860" target="_blank">📅 10:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19859">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :گزارش رسانه های غیررسمی در اینستاگرام و تلگرام نادرست است مبنی بر اجرای حکم ۳ نفر . دیشب مردم اصفهان درگیر شدند تیر اندازی شد و جلادان فقط توانستند دو نفر از عزیزان را اعدام کنند و یک نفر اعدام نشد. @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19859" target="_blank">📅 10:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19858">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حکم ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی در اصفهان انجام شد و جاویدنام شدند  @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19858" target="_blank">📅 09:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19857">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جلسۀ شورای هماهنگی مجلس با حضور قالیباف
سخنگوی هیئت‌رئیسۀ مجلس: صبح امروز جلسۀ شورای هماهنگی مجلس با حضور قالیباف، اعضای هیئت‌رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19857" target="_blank">📅 09:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19856">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxHqv1fLLMlSDzTBtnVUicd9BclYBsxfhu0fD1oLN944Wj4qp4GpH2MyAJlMLSNlu6jIunKDPYsgJvMz0Gp4UxPx4ca1_WdCm31wQ3EOuRjC30ccxxscELhZHl3wASgx6FefudS4PYKCqz_1mgyOc4x8ZKSasdFpIHI9cyGq4JN5Zn3i-o_du5U7S5ekYy1ShvVEwb8j3YhpCceD6mazs2ZuUEtF5q6ddOVjnRj1CCCsBT9CD-T-KhVo_z-GmHuOm-32a7kNVcQ7XeAnSjAuTue5KjsBH4iA3RPuYfKnr34Hu4HUkonNqxHlbof_7xwaMqwRbqLuIKGmk1qHpQ_x9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویرک پست : ملانیا و بارون ترامپ در ویدئویی نگران‌کننده که ترور آنها را تشویق می‌کند
یک ویدئوی جدید از ایران، حامیان رژیم اسلامی را به ترور همسر رئیس جمهور ترامپ تشویق می‌کند.
این ویدئو با عنوان «چگونه ملانیا ترامپ را بکشیم» تصاویری از بانوی اول را در کاروان موتوری و در برخی مکان‌های اطراف شهر نیویورک نشان می‌دهد و حتی نام برخی از فروشگاه‌های طراحان مد که او از آنها خرید می‌کند را نیز ذکر می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19856" target="_blank">📅 09:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19855">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روزنامه لبنانی "النذاع الوتان"، که با مخالفان حزب‌الله همسو است، امروز به نقل از منابع خود گزارش داد که ایالات متحده پیامی قاطع و جدی به لبنان ارسال کرده است. این پیام حاکی از آن است که هزینه دخالت حزب‌الله به نفع ایران و انجام حملات علیه اسرائیل ( در صورتی که ایالات متحده یک عملیات گسترده علیه تهران آغاز کند ) بسیار سنگین خواهد بود. منابعی که در این روزنامه ذکر شده‌اند، گفتند که این پیام به این معناست که هر راکت یا پهپادی که به سمت اسرائیل شلیک شود، در واقع دروازه‌های جهنم را برای حزب‌الله و لبنان باز خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19855" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19854">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش انفجار در اردن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19854" target="_blank">📅 08:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19853">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGy9WO7dgLpSBFCr4dO8DAA6IgEepdspATCX0UxK0KM2uWkoy65IxFkrkfGZekFWftwxgn1rPzMblgw3OZ_D7UEG_vgnXfSKOzI9m7FsB36CEyujelQKW0bWO2sm-YDuYQkootlqbwBtgQleDa8Yp-bN7xQGhwGja1xms4_APk6PhRlKnAwcw0XLtjC_DQpm6l3QTqOT2Bqen9K2PNQ2gYFHYGi60XO-apEMBWCuThv0kEHCXVC2QVU2pja-y3mSb9UjrN16B_L3dyJqz6LTojiaGxoZKRFDzF17XrIUk-vcr-2iD4yDWIWshtBK4EH0DQerTj6trmJTzIK1sBCZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار نفت سعودی شده و همکنون 89 دلار است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19853" target="_blank">📅 08:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19852">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhZU6SI0MXdvGyqEi6U_kz1THaUye0Ma6ShrshmdVFj2Ykml0BINdCpT1TBxdlL5OgvX8h2fT8MRb2wxtiG1AJ1-Nmrcew76C4d8-xLwzSUzLyNfa-2guWt3FMEF7NrxQcreomE_Szu2GbwvmFjcRTTWcJc6hXUyykcpQVh2Y0xVuM_3ihoKGLkk8SqLjGCf2CRo3Hlb4p67lqn7_9NBjiaIbjYhPX4xCwDKD_aepC3BAMNrYcIxnbfjN9WonP3cJ39KZegPsxE2FpT_-V8GVsVT8AGIZa5d-fM1y15EGd6LaeaT3UIY2p0QHXinlIB5H8uZuIbCgczztfx3LMSHMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و همسرش با «اطلاعات محرمانه‌ای» درباره ایران و تأسیسات هسته‌ای کوه کلنگ وارد واشنگتن دی‌سی شدند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19852" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19851">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به گزارش وال استریت ژورنال، رئیس جمهور ترامپ پس از آنکه بیش از یک سال به مشاورانش گفته بود که کیف در حال شکست در جنگ است، به طور فزاینده‌ای نسبت به چشم‌انداز اوکراین در جنگ علیه روسیه خوش‌بین شده است.
ترامپ «برندگان را دوست دارد» و اکنون به طور فزاینده‌ای زلنسکی را یکی از آنها می‌داند. انتظار می‌رود این دو رهبر روز سه‌شنبه در جریان سفر زلنسکی به واشنگتن برای مراسم تشییع جنازه سناتور لیندسی گراهام در کاخ سفید دیدار کنند.
او تحت تأثیر صنعت پهپاد اوکراین، به ویژه توانایی آن در مقابله با پهپادهایی مشابه پهپادهایی که ایالات متحده در جریان درگیری با ایران با آنها مواجه شده است، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19851" target="_blank">📅 08:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19850">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حکم ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی در اصفهان انجام شد و جاویدنام شدند
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19850" target="_blank">📅 08:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19849">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شنیده شدن صدای انفجار در اربیل در شمال عراق
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19849" target="_blank">📅 00:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19847">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da687f9ab.mp4?token=DKsneSUQvmg6iQyV4mo5au7c4aY-4CxD9l3CxP9OyrOdPk8U3RkE2koz15JWtr7nPXMLyLsW32k9v9qxbQwY0ua8L6v2gfhOjShE9JmzZujNOTJkX2aaIXl4qiMWurrmQHtRnAgvLu5FS4sG5vxMCsaVXpGIW5L1WMxo9p072s2U1oJVEpRkofwuy8EeKuk6huNmpz8R6ixuyQaAfIoFhZQ3wb6SFvWO9kB1uNopXi728R4Qmm6GQcy3qPD51CFxjK6hEGQz5F8DyUAiZc5NWsS1sSnH8oeAmTNNe4NiK_gyIK-AnbHXWiPHSP3xcMld42O3QQ70JgmsPBUbnRjyLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da687f9ab.mp4?token=DKsneSUQvmg6iQyV4mo5au7c4aY-4CxD9l3CxP9OyrOdPk8U3RkE2koz15JWtr7nPXMLyLsW32k9v9qxbQwY0ua8L6v2gfhOjShE9JmzZujNOTJkX2aaIXl4qiMWurrmQHtRnAgvLu5FS4sG5vxMCsaVXpGIW5L1WMxo9p072s2U1oJVEpRkofwuy8EeKuk6huNmpz8R6ixuyQaAfIoFhZQ3wb6SFvWO9kB1uNopXi728R4Qmm6GQcy3qPD51CFxjK6hEGQz5F8DyUAiZc5NWsS1sSnH8oeAmTNNe4NiK_gyIK-AnbHXWiPHSP3xcMld42O3QQ70JgmsPBUbnRjyLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست وزیر قطر: پول‌هایی که به حماس پرداخت می‌شد، شفاف بود و با مجوز دولت بنت انجام می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19847" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19846">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3e86fee4.mp4?token=i3ym5G07bBWWvHxr4p3p-Tp4E0AX7G1Z1lXHHenhpLECpaXLm-DSt4BGS5QUoBlew1nSvpUcYkft4EBrat0dS8239kCRfddmaIE6o244sqZk71bI_fhHnqhrjqcPQhM35_6l_Dl9qo6-uuIUz-BFRSssb6ykJ3lLPi4VoBg67DT6y8BND7036SatOmObnJtvTROJ_9NTr_Md_j1uZ7PmrF1aDp4Xp-1VhTMqpV62gG-GUIPIMftEOlYGdm5wRkg96LrIOZbZLUCMvUCxRul8ZjyevySnfJke1WYe_juIVC3l92F4XLj9Pwfp-szJbannEr5kJV4IciaHiP5zUNqeT5k_7oe7aUCl1hTwMKXrM06mM3Sp4fVfflEz5Bj79w4DEZyvcBrJn2WqrgOHK1tVbrewPzkuDyA1GIrmr5Vw-QDjxx7wtGTY2Q-Fugn0rEDu5hgX1m_T3q7tOFkO39cxjfrQksTpcVLjwETeneIid-Uzftbc91jOJa0KOMJKdh-zuVMTRBvp26BPbhmejj2EXf81cyBsZHDpYKyYsvROlF1wLYM--8RsqyCCr8YVcl525h5td4Re6y05I9lscmfa5uZt0GQT-1zNCPwGHpFaRZW5MIz9D8e0yqL0EbNi8Apd5NUKVALsr0F65nD7OiJqWwsw7dBbd9p3EHm1S0eynBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3e86fee4.mp4?token=i3ym5G07bBWWvHxr4p3p-Tp4E0AX7G1Z1lXHHenhpLECpaXLm-DSt4BGS5QUoBlew1nSvpUcYkft4EBrat0dS8239kCRfddmaIE6o244sqZk71bI_fhHnqhrjqcPQhM35_6l_Dl9qo6-uuIUz-BFRSssb6ykJ3lLPi4VoBg67DT6y8BND7036SatOmObnJtvTROJ_9NTr_Md_j1uZ7PmrF1aDp4Xp-1VhTMqpV62gG-GUIPIMftEOlYGdm5wRkg96LrIOZbZLUCMvUCxRul8ZjyevySnfJke1WYe_juIVC3l92F4XLj9Pwfp-szJbannEr5kJV4IciaHiP5zUNqeT5k_7oe7aUCl1hTwMKXrM06mM3Sp4fVfflEz5Bj79w4DEZyvcBrJn2WqrgOHK1tVbrewPzkuDyA1GIrmr5Vw-QDjxx7wtGTY2Q-Fugn0rEDu5hgX1m_T3q7tOFkO39cxjfrQksTpcVLjwETeneIid-Uzftbc91jOJa0KOMJKdh-zuVMTRBvp26BPbhmejj2EXf81cyBsZHDpYKyYsvROlF1wLYM--8RsqyCCr8YVcl525h5td4Re6y05I9lscmfa5uZt0GQT-1zNCPwGHpFaRZW5MIz9D8e0yqL0EbNi8Apd5NUKVALsr0F65nD7OiJqWwsw7dBbd9p3EHm1S0eynBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زامبی لند
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19846" target="_blank">📅 23:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19845">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c6fd33f33.mp4?token=vXSVhJ7YmAyqAzygOtfmcVFpns8XqjTZULTta1adJyNt0oKBDVTrmVmPp9T0JiGBzvPOr6nf3dF_gh0dU-LRCulhGUW_PCqnH_gAw7mT09aS7PvKGl1_8UPuWdkByV8NEm3u8Hlm_BUDLpqRBXBHTzJL4N-e44s1mSRg4tZIiX6IikukEPHwTBcJmv8b7qvJamzlXkFfY4bhpsQprmqulHU9ViZW0KnmzhRVdkrrXfS2KC0P8eZ7eilVzIA9m1s3iQDHpBaJxdlPyOwcBweJpj8hcGRmZLxKQl_56KqB7PLKc6AVtDyAnKeW_K5iAsVoPtvBGV7fP0_FOBYXqbb4Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c6fd33f33.mp4?token=vXSVhJ7YmAyqAzygOtfmcVFpns8XqjTZULTta1adJyNt0oKBDVTrmVmPp9T0JiGBzvPOr6nf3dF_gh0dU-LRCulhGUW_PCqnH_gAw7mT09aS7PvKGl1_8UPuWdkByV8NEm3u8Hlm_BUDLpqRBXBHTzJL4N-e44s1mSRg4tZIiX6IikukEPHwTBcJmv8b7qvJamzlXkFfY4bhpsQprmqulHU9ViZW0KnmzhRVdkrrXfS2KC0P8eZ7eilVzIA9m1s3iQDHpBaJxdlPyOwcBweJpj8hcGRmZLxKQl_56KqB7PLKc6AVtDyAnKeW_K5iAsVoPtvBGV7fP0_FOBYXqbb4Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برای مدتی قیمت سوخت پایین آمد. سپس آنها رفتار مناسبی نداشتند و من مجبور شدم برگردم.
حالا آنها دوباره رفتار مناسبی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19845" target="_blank">📅 23:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19844">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c208632.mp4?token=Tyxz4QUBdLTBzj1kkC2vrKkCONNKK5nbyq1X9Uh9KXLjMn67a5UwFUSOSINYlg0jcuIf7a06TwV2UEJRxfwyL2zoCDo1WmZ9vFtAyNthIK88wLowBrGviqBqIBwKA5z2sIX_NkGX42csvaFrhxxXHf9AqG1f0CywSxyny_-InRR6dnjPke0ceYCSQGr97iK8IdpHSEzULbZ-dEZOCUFsqr7xgxvxVxjL7BL8hYSAZ1ywWB1zficsspF_6KiLgqDJUdKZvzjxBMkDo2xSu668hj0kIGN2GoXUgSWWaAZvN8aBDxtzr4al6Nw99QQD689CM_BuLxFMpTs4u3BHyvn6uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c208632.mp4?token=Tyxz4QUBdLTBzj1kkC2vrKkCONNKK5nbyq1X9Uh9KXLjMn67a5UwFUSOSINYlg0jcuIf7a06TwV2UEJRxfwyL2zoCDo1WmZ9vFtAyNthIK88wLowBrGviqBqIBwKA5z2sIX_NkGX42csvaFrhxxXHf9AqG1f0CywSxyny_-InRR6dnjPke0ceYCSQGr97iK8IdpHSEzULbZ-dEZOCUFsqr7xgxvxVxjL7BL8hYSAZ1ywWB1zficsspF_6KiLgqDJUdKZvzjxBMkDo2xSu668hj0kIGN2GoXUgSWWaAZvN8aBDxtzr4al6Nw99QQD689CM_BuLxFMpTs4u3BHyvn6uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
مذاکرات دوستانه‌ای در جریان است.
ایران می‌گوید: «لطفا، لطفا، محاصره نکنید.»
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19844" target="_blank">📅 23:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19843">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4de1bcc9.mp4?token=Jm9FB5bPXCkRjdOamfAYfxN5VW11HuDzGmF37FUJHQFNVgMxsH6TpEvXKTsCCgFuXKVFMvC2cvRnZfqMANIelmVZFKyO_kmHoD4GUVOoDJuWrvft38qMKzRbrfqX5LYDAtGKCM8DZqF0qN2oWCKHbSxqtnre5dJoISwwvQl4BfDdRoVcKmgJ8Pw52HHxFtS5MZXcwo9tQOFiiO4HGn59QvvdhSB-RBAjZEVjP8KtW4gBewnVnBHR2kRcTatuJ_63atZgT5vsce1OKZNx8PVLcLgt_r7pu4nsCjlHDNNZNorNpAYLw217BndoyaPzrmwfK2Z3UND_AY2dz_C60LBHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4de1bcc9.mp4?token=Jm9FB5bPXCkRjdOamfAYfxN5VW11HuDzGmF37FUJHQFNVgMxsH6TpEvXKTsCCgFuXKVFMvC2cvRnZfqMANIelmVZFKyO_kmHoD4GUVOoDJuWrvft38qMKzRbrfqX5LYDAtGKCM8DZqF0qN2oWCKHbSxqtnre5dJoISwwvQl4BfDdRoVcKmgJ8Pw52HHxFtS5MZXcwo9tQOFiiO4HGn59QvvdhSB-RBAjZEVjP8KtW4gBewnVnBHR2kRcTatuJ_63atZgT5vsce1OKZNx8PVLcLgt_r7pu4nsCjlHDNNZNorNpAYLw217BndoyaPzrmwfK2Z3UND_AY2dz_C60LBHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
شما نمی‌توانید به آنها رشوه بدهید. شما باید آنها را شکست دهید.
و ما داریم آنها را به شدت شکست می‌دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19843" target="_blank">📅 23:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19842">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a198bcb3de.mp4?token=gaLwmM2nBtv-7wYpnWNVTmVpazRVnD90ap42Gi2cq4MeIWKU-sAGFEKX_Fnfb1hJ8i7zY4q8v0HXyUEfuWQEe5zzg6u91za5mKW9_liheN76OrT18Y1kofQSW-AXJ2Z9SfYkVg4t-nL4YxVHTO992dAF_luSON6C6I1YMEOZj07gaccwcgE9viXNgtHtHR9KSEj1vXreLGOyVBnV18VCz_1anO6H_iW8yPehqBJVM0LNPZUwo7J-zgBFSD2YSjYwYNw1BEAaLaLMBK24Y0HuZfb6bRqpknnissM2ynmk37MkBVqAoYwvdcL8AJKnsozWYf6bbetuhBaYSp5psVUJGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a198bcb3de.mp4?token=gaLwmM2nBtv-7wYpnWNVTmVpazRVnD90ap42Gi2cq4MeIWKU-sAGFEKX_Fnfb1hJ8i7zY4q8v0HXyUEfuWQEe5zzg6u91za5mKW9_liheN76OrT18Y1kofQSW-AXJ2Z9SfYkVg4t-nL4YxVHTO992dAF_luSON6C6I1YMEOZj07gaccwcgE9viXNgtHtHR9KSEj1vXreLGOyVBnV18VCz_1anO6H_iW8yPehqBJVM0LNPZUwo7J-zgBFSD2YSjYwYNw1BEAaLaLMBK24Y0HuZfb6bRqpknnissM2ynmk37MkBVqAoYwvdcL8AJKnsozWYf6bbetuhBaYSp5psVUJGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : همون اتفاقی که توی ونزوئلا افتاد، داره توی ایران هم می‌افته
فقط مردم متوجهش نمی‌شن
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19842" target="_blank">📅 23:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19841">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/506238d711.mp4?token=r9C8IdG6gnBEMu0GitMoDozRUqI_iY8jXlygSSnykXgefqCbO18aJB2j89T1zeWOLNPmbsG7oRlqkYi--VeRoe-V8oedRkF6kdQWru4ZA4sp3kpp-R3uty-ll3ffAJB-KujendG2rcSjAh8d8S2vbodkyQLw5kYlYZnXch-EEg2vP_shsYRxPtwLcYUNTTL-arnqRVXOx5HAPYfWeS3E7q83s9DjuMrUIk1ee3U6Hi5zNaTSIq4ccmajo_-xmD7L7_3Kl1jWrtYMEtQyEm8Mq3zv7YvdEL20V4-3jxCzr_AUCi_SEqYBlupZayROaDqGYswVrrH8tBWSS3ZhBZ4dCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/506238d711.mp4?token=r9C8IdG6gnBEMu0GitMoDozRUqI_iY8jXlygSSnykXgefqCbO18aJB2j89T1zeWOLNPmbsG7oRlqkYi--VeRoe-V8oedRkF6kdQWru4ZA4sp3kpp-R3uty-ll3ffAJB-KujendG2rcSjAh8d8S2vbodkyQLw5kYlYZnXch-EEg2vP_shsYRxPtwLcYUNTTL-arnqRVXOx5HAPYfWeS3E7q83s9DjuMrUIk1ee3U6Hi5zNaTSIq4ccmajo_-xmD7L7_3Kl1jWrtYMEtQyEm8Mq3zv7YvdEL20V4-3jxCzr_AUCi_SEqYBlupZayROaDqGYswVrrH8tBWSS3ZhBZ4dCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به كشاورز زمين داد، چريك شد
به زن هويت داد، آنارشيست شد
به كارگر سهام داد، كمونيست شد
به هنرمند اعتبار داد، توده اى شد
به مسلمان حرمت داد، تروريست شد
به دانشجو بورسيه داد، ماركسيست شد
به اقليت حقوق برابر داد، جدايى طلب شد
@WarRoom
نسل ۵۷</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19841" target="_blank">📅 22:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19840">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBuL8-zrSdgldgcArP7eLny8lKcjQ8m2WQMfPJBEYT0qFfM_JT7U2KIzIg2PecJ9fcQ4LDWbGL8a3E69uXDEL2Qhzk643BZN6_Ok-0lKkDOxsQOE3De13p9G4uX0MXQYf1toF17GgWYHzAgWnxNRtksMLJYpdRh6KCC0V7BSRW7RynzowPjW_nfMwD4HuzlFhY0TS76DOW5uyQwRH1_2xWJ57C1DpyBlOyl1aFHODQlAgDzI96Nq9jPv11EOpOHCZlq4zneZ2FUW6WZpYbUMiJ0upenxYG3dAvSmmlEanxHbbpDuq5zkgEI6JR2GuG3DzhF5O6TgEmw4vXf9bd2QUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏عمو لیندزی بخاطر ما تا مونیخ اومد، حالا وقتشه ما بخاطرش تا واشنگتن بریم.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19840" target="_blank">📅 22:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19839">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3a98b01b.mp4?token=ObUFPNQMcxvABfUkECkiProoRW5xxV5kQvFtlIJ34rIQdb6dSt9puv-8WQKUo1VtHQZVyfMeDZuWH9C_wM-JNYL7ZlpSdGOaSUbPZl9hhV5htjwkTVF7Zn5rlLeCmb_68MXwRKuVjqgPRgkN7w_32C69yJ7IykjCc8_u5j_Mgx8OKpn6usCWiXL01t747NOEMRg8FS-59xjOND1KrX4PmjDdws2wr0zKBc4YS9ypp_BdgEZXERhvnIvp8Xj4C4T1kuZ2JAXu1Zvy5y6mRL61LBgD7na4HmXPyuHmHMHOpSOR8p2Dv7rdRoYNnNDzlSV-OhSKX7w7EuKbkHV2k57j3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3a98b01b.mp4?token=ObUFPNQMcxvABfUkECkiProoRW5xxV5kQvFtlIJ34rIQdb6dSt9puv-8WQKUo1VtHQZVyfMeDZuWH9C_wM-JNYL7ZlpSdGOaSUbPZl9hhV5htjwkTVF7Zn5rlLeCmb_68MXwRKuVjqgPRgkN7w_32C69yJ7IykjCc8_u5j_Mgx8OKpn6usCWiXL01t747NOEMRg8FS-59xjOND1KrX4PmjDdws2wr0zKBc4YS9ypp_BdgEZXERhvnIvp8Xj4C4T1kuZ2JAXu1Zvy5y6mRL61LBgD7na4HmXPyuHmHMHOpSOR8p2Dv7rdRoYNnNDzlSV-OhSKX7w7EuKbkHV2k57j3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏در برنامه دیشب مارک لوین پیشنهاد داده شد که یک دولت قانونی در تبعید با رهبری شاهزاده رضا پهلوی تشکیل داده بشه. مارک لوین این رو یک ایده فوق‌العاده خواند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19839" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19838">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال ۱۵ عبری: نتانیاهو در دیدار خود با ترامپ، تحت فشار زیادی قرار خواهد گرفت در مورد مسائل مختلف، از جمله سوریه، غزه و لبنان. این دیدار بسیار مهم است و امیدواریم که مقدمه‌ای برای یک عملیات مشترک بین اسرائیل و آمریکا علیه ایران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19838" target="_blank">📅 21:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19837">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرنگار: آیا نتانیاهو از شما می‌خواهد که با ایران به توافق برسید، یا از شما می‌خواهد که به حملات خود ادامه دهید؟
ترامپ: عملکرد بیبی عالی بود. ما در کنار هم عالی هستیم ، نمیخوام بگم ولی ایران اکنون ۸ درصد او چیزی هست که چهار ماه پیش بوده
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19837" target="_blank">📅 20:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19836">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: از پوتین درباره ارائه کردن تصاویر ماهواره‌ای روسیه به ایران، سؤال خواهم کرد. با اسرائیل در مورد ایران مواضع بسیار نزدیکی داریم. ذخایر مهمات زیادی داریم و مایلم که مهمات بیشتری فراهم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19836" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19835">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یاشار : نگران نباشید یک سری مدارک رو و آلبوم رو حتما موساد دیر حاضر کرده  تکمیل کنه میپره
😁
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19835" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19834">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرنگار: آیا شما و نتانیاهو در مورد ایران با هم موافق هستید؟
ترامپ: یک اختلاف جزئی وجود دارد، اما ما بسیار به هم نزدیک هستیم، بله.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19834" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19833">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ: من زمان زیادی را با ایران سپری می‌کنم و فرصتی وجود دارد که اتفاقات خوبی رخ دهد.
ایران در طول چهارده روز گذشته، ضربه بزرگی دریافت کرده است.
آنها به ما با لحنی بسیار مؤدبانه درخواست کردند: "لطفاً دست از این کارها بردارید. بیایید ملاقات کنیم."
احتمال رسیدن به توافق وجود دارد.
اگر اقداماتی که ما انجام دادیم، صورت نگرفته بود، آن‌ها اکنون آمادگی مذاکره با ما را نداشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19833" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19832">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرنگار: آیا از وزیر دفاع، پیتر هیگز، به خاطر توصیه‌هایی که در ابتدای جنگ با ایران به شما ارائه کرد و نتایجی که در پی آن حاصل شد، احساس خشم یا ناامیدی کردید؟
ترامپ: نه، ایشان وظیفه‌اش را به بهترین نحو انجام داد. ما ارتش ایران را نابود کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19832" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19831">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYiMpFMDY9SGOHjSgsFwFsbBWyF8k_rwgBNmMIsZVX_Fo8oNoPAmHKrqdUyj813PR7SfIkS7OkbQDv3PVHA-RHAU-3eRNhzQjDrY17XZz2Vdw0RlgdQJkjXscuY8HTAPkTR0dtcKcIP1cdhFH_FdjWi8z7_207nBkhtnDKFADVcP2zumyLPZwMINTdRK2HU3KL0QxsKhpnPl4gglwCAGlbCh42mic-bsEZynXcoS2GwaQ6oNBfIQ9i3i01foysAitanz0vaxSckyO6WDHZfMpEu8e-nmSeFqxf4daC-ncnSTp8kkqnkgH4RoqjnfNcJg65bIvojzzkR11VcLmV2u5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19831" target="_blank">📅 20:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19830">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیویورک تایمز : ترامپ در حال بررسی سه گزینه اصلی در مورد ایران است: تشدید اقدامات نظامی، تشدید تحریم‌های اقتصادی، یا اعلام پیروزی و عقب‌نشینی نیروها.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19830" target="_blank">📅 19:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19829">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسانه‌ها از حمله هوایی اسرائیل به شهرک طیر ابلعروب در جنوب لبنان خبر دادند. جنگنده‌ها ۶ نوبت این منطقه را بمباران کردند. @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19829" target="_blank">📅 19:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19828">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEMYl8EfzJW8y-AWktaKJxj2BwfzBhgQdjJ6WvSW6h6gfiF3jcXW7XUxdZVWojzo_Tz0Ka4ZrR5jCTV1zTfVX-64lLSVT78zdz_zX7a49aP8RrNwvBj7fyEEPwQwijWFUuq1lKnBjHCA6Jt_AeZ30XLBw-wwCYnjM6q68VEmfNWnjw7-t9UcqJ532D4CjH-vGYF8SaUtJv4VqzjQw4062Bu0t624v2_zyu3EJkjbrl5fGCOjBGp9ENGFs1f1-Hf8nFAW63rRg-tT2rHy1xn5kRLTnCsqTfSbHXvkTiVI4rcDOVsLrocaiMVS3QPqyziQutZMyBUCzI0iVBZrzKwywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک ملوان آمریکایی در حال گشت‌زنی در دریای عرب توسط ناو هواپیمابر یو اس اس فرانک ای. پترسن جونیور (DDG 121) است که از محاصره دریایی ایران توسط آمریکا حمایت می‌کند. سنتکام ۱۷ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی دیگر را توقیف کرده است تا از رعایت این تحریم‌ها اطمینان حاصل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19828" target="_blank">📅 19:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19827">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هم اکنون
تیراندازی نزدیک کنسولگری آمریکا در تورنتوی کانادا
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19827" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19826">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تامیز اسرائیل : بنیامین نتانیاهو در دیدار پیش‌رو با دونالد ترامپ در کاخ سفید قصد دارد اطلاعاتی جدید و حساسی درباره روند بازسازی برنامه‌های نظامی و هسته‌ای ایران ارائه کند. به گفته منابع اسرائیلی، این اطلاعات شامل ارزیابی‌هایی است که نشان می‌دهد ایران تلاش‌های خود را برای بازیابی توان نظامی و پیشبرد برنامه هسته‌ای افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19826" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19825">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرنگار:علت پذیرش درخواست میانجی‌ها برای توقف آتش توسط شما چی بود؟
ترامپ:چیزی برای از دست دادن یا به دست آوردن نبود ‏
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19825" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19824">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJhtJjSEEpJxQoWGhWg6-DvS_K4fVUtkqDw_oArcHeozMbCipIbBN6UklRwXXGj104cIXIl_SFX8h-tDL6YvOWYoloCtyh_uKW3cHHD_qSpdReyt_LWbJZUjZxK8B6oRqQJDq4IBiWC98rhh6UAUyBS-qhoG3ZtB55h5zNmlNGgxBzTNaRl9_FFsdgiJpIWVOxGhazXI3serYCZt_0DmmIWX_oYER8QAspyTMJg0SJE1e_WaYgGc3co0Ds11RdahowsN2FQFVa-oG-qbTvAQk9O7vH34G6SUGhwyRJHVNIspNhoL46mzvZiuKTl_dPDsvbEnDjsPox3-29uKgNDRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها از حمله هوایی اسرائیل به شهرک طیر ابلعروب در جنوب لبنان خبر دادند.
جنگنده‌ها ۶ نوبت این منطقه را بمباران کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19824" target="_blank">📅 18:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19823">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: به درخواست واسطه‌ها پاسخ دادم تا فرصتی برای مذاکره با ايران فراهم شود.
"من زمان زیادی را برای مذاکرات اختصاص نخواهم داد."
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19823" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19822">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: ما در حال انجام مذاکرات عمیقی با ايران هستیم و اگر این مذاکرات موفقیت‌آمیز نباشند، به یک عملیات نظامی گسترده باز خواهیم گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19822" target="_blank">📅 18:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19821">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کاظم دست کج : در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و اصرار داشت که مسیر جنوبی تنگۀ هرمز فعال باشد و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19821" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19819">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYCVqpKdNAVDEGN4f5hYzky4i_tl0nPcJUzi3fPbVcq-qjyxe4Amv_cD18eTxTi181vz6aGKZkKM_oYd2R9xc0xEQWCQ0AgOFBmJIb_gib2KzAFnya2wewXuZsOSujo1u7PFq_yMCcSPNj1xVCsjchTt0LYHOOsCWllKNevSniUYFhfoOFn7UV_Wg__gy9uLHMbgqjiqM6urMZHB75Ks8R0j4RdG6vwnLF_hkTeC_W07TUxcO8UqXdhmzxAmZodCNPFw6cOT7BYyQn16dO93oExc40zNZrpjRgYWYbfVVzvaAfAvPXnn0XTmUivn_FlAkDF0SDOFYVR5UugdlbZAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19819" target="_blank">📅 17:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19818">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وزارت امور خارجه عربستان : ما پهپادهایی که قصد هدف قرار دادن تاسیسات نفتی در مناطق شرقی و ریاض را داشتند از بین بردیم همچنین این حملات را که توسط شبه‌نظامیان تحت کنترل ایران در عراق انجام شده است محکوم می‌کنیم و تأکید می‌کنیم که پادشاهی عربستان سعودی مصمم است جلوی متجاوزان را بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19818" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19817">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همشهری: سران قوا با بنزین ۱۰ هزار تومانی برای سهمیه سوم موافقت کرده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19817" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19816">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جی دی ونس در انتقاد از اسرائیل برای جلوگیری از مذاکرات:
من قطعاً فکر میکنم شاهد یک کارزار بسیار پنهان و با بودجه بسیار بالا بودیم که تلاش میکنه مذاکرات رو منحرف کنه و مانع رسیدن به توافق بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19816" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19815">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=d7ZxmaHcrT3YGJxLrB1UD18wX7SpTKzdyKUioVbmh0iP9NJk60PAV9gJYXMu5i8uVtRmKuXmM6dRS8obAHT5KgRMOdwztqgJxa3Dj1ofLwfwBBJtvQ4aJbplhLwdMjX6LkGpzeqFbtx8jeI4d75MDlkOxqSGF2u65MQZVjdLSIoIHNVoiD8Y5YedLAwtIzCOYiWZMXMqXlhTcgiJrdeMl4eCcQua_1NFc3m3DUnm0gJ8_IZEPY0pPGzmtA0KTGeu-MFGRVxN0xsJatIl-CXUPBe4uE1O-hdpZAeofgsiRvPDSrsmkezrkGI6gJBqdP09BuwFtyUvF-HJNYll2oYUzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=d7ZxmaHcrT3YGJxLrB1UD18wX7SpTKzdyKUioVbmh0iP9NJk60PAV9gJYXMu5i8uVtRmKuXmM6dRS8obAHT5KgRMOdwztqgJxa3Dj1ofLwfwBBJtvQ4aJbplhLwdMjX6LkGpzeqFbtx8jeI4d75MDlkOxqSGF2u65MQZVjdLSIoIHNVoiD8Y5YedLAwtIzCOYiWZMXMqXlhTcgiJrdeMl4eCcQua_1NFc3m3DUnm0gJ8_IZEPY0pPGzmtA0KTGeu-MFGRVxN0xsJatIl-CXUPBe4uE1O-hdpZAeofgsiRvPDSrsmkezrkGI6gJBqdP09BuwFtyUvF-HJNYll2oYUzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: من با رئیس جمهور ترامپ در مورد مسائل مختلف گفتگو خواهم کرد، و در صدر این مسائل، ايران قرار دارد.هدف از سفر من به واشنگتن، تضمین امنیت، قدرت و آینده اسرائیل و همچنین گسترش دامنه صلح در منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19815" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19814">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnjZe8Eh0F43JRzyLnJ3dIoesM9grycHJq0gxgJsdXILxzvqpRYRB2hY8YdffY5OWVgEv8BY4-ssFY8oAcd91PMEPlusx0pRW9kPrqlIJZp12EFWAtATg7sstgvJllVDwdlFTXdEM9-BUsdwRzJVUuKgHOTQDdb8-6j-IHBPyNZBymljBO52wcV5yf8M0obU_rlVByUe5QlO3cbNMbz2e5cjqzjak280VDYg9s0PPwVrHxu_SceYUZfO-ITdjseVB6gB21rjRjyUZUw1L9Bckw5-E7bwhvgtyFeqE0OCY-NC6uX0p23WbFHNKitBtbgd3ye6egofkPL-M7USUa51cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون کرج سمت فرودگاه پیام
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19814" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19813">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19813" target="_blank">📅 14:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19812">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCK1r2NDVMP9PzqnJiq-NQNQIo9bLNsa5jOsonBqjN61-jt7QWqEFK-9Zo2CI4bmAwDaBnTnRHU1dKpsKmueD2xeUY2c1xJUoEswx6I6otH8QuRt4hbAA8b5nQInrkIVmHSJcL1eiUMS-HaXbVdBSnlTkMpaowK-DFPk086yUMhQ7sj5VSE2-WY43mEoH5SIovQ4QZDklRTKx9TsG5uPmVLIYCFlJTNCmQdPuCAy5ussCgPQvscDLW9rZfmWnnLbGF3kU9mhH5YfhvtzAbAfldt0dekggYd11B8VebGr_F-1DBMgu_YhYDYxHcTjjyf4qF1wV-obIQ8IUqV3Ghj4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دهه هفتاد میلادی، در زمانی که در منطقه کسی نمیدانست سوخترستان حتی چیست. عکس بسیار زیبا از سوختگیری دو فروند بویینگ 747 شاهنشاهی بر فراز دماوند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19812" target="_blank">📅 14:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19811">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هواپیمای استاد بزرگ شطرنج بی بی نتانیاهو  تیک آف کرد و پرید ! تا کور شود رسانه هایی که خبر تاخییر رو کنسلی انتشار میدهند @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19811" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19810">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9ca588d.mp4?token=nhDH7NaOAIEFLBfInL6cfU0rh6UkL2HY07T9lJFCB2BtY0wfWZ0JiaxF_ZMNdruoWdWm_W7GXmRuiy30JlKOug3cNmOiRTEKMSvtKfImKIrZNN9rNYQ0yWS4OaKony9Iy0LQt70PurcTgCP3bkXC52eK0wA8gSc8EojyqOR3P_JOZiqgO___9kOACU292NJEoZ98ttmhfoXGA_AorKeGT2W_l1q_LTM6KwrYKPbozPahTeeKjPK5xIdyuC8psobq207hO8xx5SO_qHzqH0RJIAWhrRHxzcuoE2c_oc-wLavnzBevW_SXECYYP-Cqeg4RH64QreA_FlZ5T-8H1VV7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9ca588d.mp4?token=nhDH7NaOAIEFLBfInL6cfU0rh6UkL2HY07T9lJFCB2BtY0wfWZ0JiaxF_ZMNdruoWdWm_W7GXmRuiy30JlKOug3cNmOiRTEKMSvtKfImKIrZNN9rNYQ0yWS4OaKony9Iy0LQt70PurcTgCP3bkXC52eK0wA8gSc8EojyqOR3P_JOZiqgO___9kOACU292NJEoZ98ttmhfoXGA_AorKeGT2W_l1q_LTM6KwrYKPbozPahTeeKjPK5xIdyuC8psobq207hO8xx5SO_qHzqH0RJIAWhrRHxzcuoE2c_oc-wLavnzBevW_SXECYYP-Cqeg4RH64QreA_FlZ5T-8H1VV7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار : نگران نباشید یک سری مدارک رو و آلبوم رو حتما موساد دیر حاضر کرده  تکمیل کنه میپره
😁
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19810" target="_blank">📅 13:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19809">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CerT96I4WcLKDfhGo4VQZk-xufwfQw4chgljWsiZhRGlRYV9i1Omvb-eNGqznFuoq3NYWoquKMjXxOeLv1c97RVNc_cL26CkqYeWgKJAXtgpC8Xu1jnsWq0dtwsxVRyDNyoGukD3QtzR5fRpVRVtpaHcGQ8AUhAqNUmJqivWXGU87oKE3_JdS3WDQ7Dn3itaeVeOHPHWxepItrEsbq90svrR7HFERE137UP4qlYsF0uR7IErvVLmaeydlcy_jtEFvArL1O5jQ-GZV5cX5lyknIsqbNJ7htkxdBGuLgmpjq3Uw8Wbp27R5K48pR0uWHG8MYMAGT5vC_rLfsBe5KmFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای استاد بزرگ شطرنج بی بی نتانیاهو  تیک آف کرد و پرید ! تا کور شود رسانه هایی که خبر تاخییر رو کنسلی انتشار میدهند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19809" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19808">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19808" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19807">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ایتامار بن گویر، وزیر امنیت ملی اسرائیل گفت: «باید کارهای بیشتری انجام شود. من امیدوارم که دونالد ترامپ، رئیس جمهور آمریکا، متقاعد شود که ساده‌لوحی خود را متوقف کند. او یک تاجر است و در مورد مسئله ایران بسیار ساده‌لوح است. هیچ دیپلماسی با این افراد وجود ندارد، هیچ چیزی برای صحبت با آنها وجود ندارد. باید با ایرانی‌ها از طریق دوربین صحبت کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19807" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19806">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دفتر نخست‌وزیر اسراییل از به تعویق افتادن پرواز ۱۱ صبح وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد @WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19806" target="_blank">📅 13:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19805">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دفتر نخست‌وزیر اسراییل از به تعویق افتادن پرواز ۱۱ صبح وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19805" target="_blank">📅 13:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19804">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfe7KnbrfUcAQeNr8bbfhL9w1WiVGmOblaPgAoFCeBAKp7_5AXQJwX3vBC4BiTAQGAgQG3YehrAabBZGu9WE1ifcid-BvDDWcYLSVhJQ6V2_OXlo6RZc_QCS2Wii9oWWKjoyOlPna3LldtuT-trlfLumZ3PK4IuvZEDNF1Qr59PEhT7qnBP4Kb74E3oSIAXet8O-X-5KvaOFU8RgygovbaRZt7PEISqory6wRQ1fEzPJ5itn0sLStFqL2ubGVAL4qclRXWdMVbjmjqC5ZT4oxfN619ngFa3jXdrfChq0fXAcY-QOpcCeJvjnfa8CZoNTJLWPJQgqaRgYRwAQbmfK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اطلاعات ۴ مرداد ۱۳۵۶. دقیقا سال پنجاه و شش هم همین موقع ها، هتل هیلتون آتش گرفته بود.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19804" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19803">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19803" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19802">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db435b3a7.mp4?token=QAOdzF-9s_Cd2_h3eFW0WW3zzMfFousTYvpNnMLeYHMRzS1WAH5WmfZyfEV8-w-YFNU9q9mUOt4h1wSmwjwztQzWqAuBqgGss03wE9BspnBNMzudSnVlVtTJ-NsXjyrwbTzO8sMsJ5a-_AD9q9kLXsuTzvvGuY1EyhkQqSzQoyWCuk1BbZ9y6ng3w3N62IcvZQWtTFY2hDP8GlgmWCSnrJw0-rmPUSLCwdxQ8epv96I5_0RCn-3dKPPKnTtQGUG8hdz-WE_G0ewT76MNgXUBkuatMLVTFSHoZfm5RPKoX46oreqjamrBxg1jyJIPy4PQ1R6wzhxJQ6YWNdwfAl5hJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db435b3a7.mp4?token=QAOdzF-9s_Cd2_h3eFW0WW3zzMfFousTYvpNnMLeYHMRzS1WAH5WmfZyfEV8-w-YFNU9q9mUOt4h1wSmwjwztQzWqAuBqgGss03wE9BspnBNMzudSnVlVtTJ-NsXjyrwbTzO8sMsJ5a-_AD9q9kLXsuTzvvGuY1EyhkQqSzQoyWCuk1BbZ9y6ng3w3N62IcvZQWtTFY2hDP8GlgmWCSnrJw0-rmPUSLCwdxQ8epv96I5_0RCn-3dKPPKnTtQGUG8hdz-WE_G0ewT76MNgXUBkuatMLVTFSHoZfm5RPKoX46oreqjamrBxg1jyJIPy4PQ1R6wzhxJQ6YWNdwfAl5hJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هتل در حال تخلیه است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19802" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19801">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3qOmXmb2g8-IQpYRz-o8bUWQ8ixudDRQB6r4DpzrQnqAwiDF8Jjk-sRs-FOEAKxgZUfzxzmsQLy5pS-buCDvAJgEa--BCOGtJbgNHzJ68gbpWmVBRPzR-1cbXNXSs9XtMbdeGireRzmdsqQcI-4pQq-7RAH9ee0LNIxAFU7gxOcRc8n5vdDsWCYn-P4LRbxgXJpSTxnI6VDaeTAkm9J3aBWwtNiaobwmLAS1Iw_dO9I89j3i5_M64IsRD3ic0gTsON6M5EZScCwXkDUJJbfyD87-Iu3_Guxg_2nVh1qxILS-3a6mEUIhX6o4deyWeLsxlOCUARPIOues6TxBLbwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی ساختمان هتل هیلتون
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19801" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19800">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جمهوری اسلامی  : تنگه بسته است
سخنگوی وزارت امور خارجه ایران گفت تهران به واشنگتن اجازه نخواهد داد شرایط پایان جنگ را دیکته کند و هشدار داد که تنگه هرمز همچنان بسته است. او همچنین اوکراین را به دلیل حمله ادعایی به یک کشتی ایرانی تهدید به تلافی کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19800" target="_blank">📅 12:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19799">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b0896ed8.mp4?token=oyxAKnacW8PPDyoC2Vx4z7MmLj_82UmusPqEEMyf57sUv0V0IVrPnIMrOd8ju6NtC5-tBtXE13kZg2VUqchSTM89Vz5aZrPj5laA-xwth4NSFpGjUgD-wa_1hEt2sDJuRe7tg870ATdPMsJ3JjmT19vuY33Qi_AmbDbsQ3h05jn7t14DnEN5XTHBl-NgcaGgRzRElWXbSB9h7NAAKLaRQKWdQD5rslFLVB5xKODPDiYm3REXwErAXuVLJA5ILDnhgxurLPilV_nZm6kwRvfs3aZr4JVPGD6D4g5aYeEhccHrQtySjspO2oREjrK9B_9krieENq4GC9yr1UV_pp8VXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b0896ed8.mp4?token=oyxAKnacW8PPDyoC2Vx4z7MmLj_82UmusPqEEMyf57sUv0V0IVrPnIMrOd8ju6NtC5-tBtXE13kZg2VUqchSTM89Vz5aZrPj5laA-xwth4NSFpGjUgD-wa_1hEt2sDJuRe7tg870ATdPMsJ3JjmT19vuY33Qi_AmbDbsQ3h05jn7t14DnEN5XTHBl-NgcaGgRzRElWXbSB9h7NAAKLaRQKWdQD5rslFLVB5xKODPDiYm3REXwErAXuVLJA5ILDnhgxurLPilV_nZm6kwRvfs3aZr4JVPGD6D4g5aYeEhccHrQtySjspO2oREjrK9B_9krieENq4GC9yr1UV_pp8VXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در
۲۰ و ۲۱ بهمن ۱۳۵۷
در پادگان‌هایی مانند
دوشان‌تپه، عشرت‌آباد، حشمتیه، لویزان و مراکز دیگر
مردم برای تصرف اسلحه وارد پادگان‌ها شدند و تعدادی افسر، درجه‌دار و سرباز را کشتند !
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19799" target="_blank">📅 12:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19798">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دیدار نتانیاهو و زلنسکی با ترامپ
گزارش ها از سفر قریب‌الوقوع و ناگهانی زلنسکی، رئیس جمهور اوکراین به آمریکا همزمان با سفر نتانیاهو به آمریکا
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19798" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19797">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست. @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19797" target="_blank">📅 11:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19796">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد
بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19796" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19795">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uth7PY23oNcDjEOvNboe51IxbixcvIynTCYtj8BjZv_GrhTT8k2clTSppCYx2icQRvCNgj2fP6seWs6SLic-G1fssDKs7WQRWhdqGsO5F7J-8mxoo9yEbTyq-TgkvnGZVSuf_G-Hr-Q8gje1dOaWgAHkfF6PMFSIhW0fPadplm1Ys5kPeVC3HUTbZxiHIUH71eHeIHb1MRfb3XYCeqZ9o2-QQfjSxUvJyjh1_Ov8lLFnJlg58bmtpNu7baU7Hrnyrfort-xUO_3HJ7RLz-j7GzULjwwcHyVeQwouq8tfgrjH5tNYm84aJTFV0YQt6sMtRLD7de4Dfoygj6oG8hl9yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از «نیما مرادی» که در حمله اوکراین به کشتی ایرانی کشته شد. کشتی آنا از بندر آستاراخان عازم بندر انزلی بود.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19795" target="_blank">📅 11:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19794">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پوتین: شناورهای تندروی ایران در درگیری با آمریکا عملکردی موثر داشتند
رئیس‌جمهور روسیه در دیدار با فرماندهان و نظامیان ناوگان دریایی این کشور اعلام کرد که ایران در جریان درگیری نظامی با آمریکا با موفقیت از به‌اصطلاح «ناوگان پشه‌ای» (شناورهای کوچک و تندرو) استفاده کرده و این نیروها عملکردی کاملاً مؤثر از خود نشان داده‌اند
، توسعه چنین نیروهایی برای ناوگان دریایی روسیه نیز ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19794" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19793">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هواپیماهای تهاجمی A-10 Warthog برای عملیات احتمالی علیه ایران در خاورمیانه اعزام شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19793" target="_blank">📅 10:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19792">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=KCZLnGBZfbsuBUsjfk9M1wLaP6kjuzH6xyaVyoxa5rNzdBlO-nZDwcT1WTQ3z54pY8oP1adfApJH76GLyKI0pyBFlAuD1f_yOJHlIKfLmPOiotr4UGjDGQ5VvURl0-OTB4TfrIXSGmw9p0_reBKx6SGDZv8Yvc6CPYtd_SLJT4HD7dh1Klh_3mBC88LVTVT7UgCd0bp3O8RpW48h0HzZHKJFmbnu-CYGeCv1irHzPg9trP8e6XQnxMqI7Sm88wp4-R2bF9cW6qwW1hqMJQzEuY7X9c3euGpwGcYgqJktQVStcr8Yu-65ipEiLrDLN7MSVE5tEmjcw0NqoHJtzbhYNEtFr6WfEwDEwYOSa_HLLBbSDka34f0lMW0cuauVsIWIA9sXz4HhJCdh0SyczPIK3reX0Z0C9A6XaVZUX2smX3S7VneXgpqs8KEevsVt9bQCQWCDalyWpSlR5zovtZahEf7yy7bgx3Zu6r-p9nBTf121CDlMXfXpHyvAuIBFLst0W4V49E3gxEZ_sebkf0vmzQZ5q0VhaG5jDFlIOaRE1gzEizcaqyZfbkcC0zoSWUNBZkVPqUJOR7hzZIx9n6qV31PzzqEVEQMquZg5cNPwzLVJRt6oJy12SbY1HYG-o-0YGhbpoQbP_Dpz5bo4HRZ8930YwQ-GYSHY-KQl8xXPnG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=KCZLnGBZfbsuBUsjfk9M1wLaP6kjuzH6xyaVyoxa5rNzdBlO-nZDwcT1WTQ3z54pY8oP1adfApJH76GLyKI0pyBFlAuD1f_yOJHlIKfLmPOiotr4UGjDGQ5VvURl0-OTB4TfrIXSGmw9p0_reBKx6SGDZv8Yvc6CPYtd_SLJT4HD7dh1Klh_3mBC88LVTVT7UgCd0bp3O8RpW48h0HzZHKJFmbnu-CYGeCv1irHzPg9trP8e6XQnxMqI7Sm88wp4-R2bF9cW6qwW1hqMJQzEuY7X9c3euGpwGcYgqJktQVStcr8Yu-65ipEiLrDLN7MSVE5tEmjcw0NqoHJtzbhYNEtFr6WfEwDEwYOSa_HLLBbSDka34f0lMW0cuauVsIWIA9sXz4HhJCdh0SyczPIK3reX0Z0C9A6XaVZUX2smX3S7VneXgpqs8KEevsVt9bQCQWCDalyWpSlR5zovtZahEf7yy7bgx3Zu6r-p9nBTf121CDlMXfXpHyvAuIBFLst0W4V49E3gxEZ_sebkf0vmzQZ5q0VhaG5jDFlIOaRE1gzEizcaqyZfbkcC0zoSWUNBZkVPqUJOR7hzZIx9n6qV31PzzqEVEQMquZg5cNPwzLVJRt6oJy12SbY1HYG-o-0YGhbpoQbP_Dpz5bo4HRZ8930YwQ-GYSHY-KQl8xXPnG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتهای زیبای ریچارد نیکسون در مورد شاه و اتفاقات آن روز.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19792" target="_blank">📅 10:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19791">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=oiAbwXKe-9GwLATLlW_GeourDU7MT0-uZZqUkSRrWFFK_6fFUNfk9Mgzq67HroqL2U41YCt9BOwXOgIyB0qbq2XoWs7KFeG9eL6IthwtZmY60ydjirB9R0tZ4PLIfjUduJc9E4XDIrZdeaD7rxTriF71lIl041Fejn7Enkp7bjdzWqrbp29pwQTKXcdll35g1OIjjTTOIj3RVxBeCbg1GBOOqY-PgCwh9XL69ZJ-4v1w-i4yWWHa9TgVw27spPA2eQChNu5Ig1XjJjpdvxHBMkMm1CKVlORvkTIJJkWyPjVx-JAiW6Fjw8WRUwphdNGV8SWsTK3I2FDYUWJ_mxELiDw8EfRJD4BGWzYFKstlBHp2c0-UACgiFEMxMBQyAzdMcyJVxyLbWoB8ZFXuQhNjwW2f3tK4WpXDnA8cZ_BoiDAkzZlOHCRB3pINekh7zd61u6Uz5kalebviz3YRLrTtjKA4DKAe-O8isJw7zS4-WkloJ644qApyNNzB50_65548JEOq1_XcMWFwxLLAVfhmUcvE00zRzeuC417F3eY0r32syKEsNcDDyA4ros2cgus7LJ4ibmCDrbRnt45Ci6_qig44zk1M9OOVgNhhrY7NO3ExqIopIXbgAcH3a0NtTbMLhqoVZELLrZ-tEkot-9CRvbd6at6jFhOutxKW3He_3i4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=oiAbwXKe-9GwLATLlW_GeourDU7MT0-uZZqUkSRrWFFK_6fFUNfk9Mgzq67HroqL2U41YCt9BOwXOgIyB0qbq2XoWs7KFeG9eL6IthwtZmY60ydjirB9R0tZ4PLIfjUduJc9E4XDIrZdeaD7rxTriF71lIl041Fejn7Enkp7bjdzWqrbp29pwQTKXcdll35g1OIjjTTOIj3RVxBeCbg1GBOOqY-PgCwh9XL69ZJ-4v1w-i4yWWHa9TgVw27spPA2eQChNu5Ig1XjJjpdvxHBMkMm1CKVlORvkTIJJkWyPjVx-JAiW6Fjw8WRUwphdNGV8SWsTK3I2FDYUWJ_mxELiDw8EfRJD4BGWzYFKstlBHp2c0-UACgiFEMxMBQyAzdMcyJVxyLbWoB8ZFXuQhNjwW2f3tK4WpXDnA8cZ_BoiDAkzZlOHCRB3pINekh7zd61u6Uz5kalebviz3YRLrTtjKA4DKAe-O8isJw7zS4-WkloJ644qApyNNzB50_65548JEOq1_XcMWFwxLLAVfhmUcvE00zRzeuC417F3eY0r32syKEsNcDDyA4ros2cgus7LJ4ibmCDrbRnt45Ci6_qig44zk1M9OOVgNhhrY7NO3ExqIopIXbgAcH3a0NtTbMLhqoVZELLrZ-tEkot-9CRvbd6at6jFhOutxKW3He_3i4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دیده نشده از مراسم محمدرضا شاه
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19791" target="_blank">📅 10:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19790">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏ساعت ۲۵ ایران ‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.» ‏انورسادات با لباس نظامى آمد،  ‏مستقيم به اتاق شاه رفت. ‏دستش را روى قلب شاه گذاشت،  ‏به انگليسی گفت: ‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»…</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19790" target="_blank">📅 10:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19789">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صداوسیما: در ساعات اولیه بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن موقعیت‌یاب خود قصد عبور از مسیر جنوب تنگه هرمز را داشتند که یکی از آنها دچار حادثه شده و بقیه تحت مدیریت ایران به خلیج فارس برگردانده شدند
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19789" target="_blank">📅 10:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19788">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرنگار الجزیره: نیروهاى ارتش اسرائیل، به همراه بولدوزرهاى نظامی، وارد شهر عرابه، واقع در نزدیکی جنین، در کرانه باختری شدند
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19788" target="_blank">📅 09:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19787">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پنتاگن : از زمان شروع درگیری‌ها در ۹ اسفند، ۱۸ نظامی ایالات متحده کشته و ۶۲۴ تن زخمی شده‌اند
سی‌ان‌ان ‌: بر اساس اعلام پنتاگون، بیش از ۱۴۰ نظامی آمریکایی جدید به مجروحان جنگ علیه ایران، اضافه شدند
نام چهار سرباز آمریکایی کشته‌ شده در حملات ایران که از پایگاه داده‌های پنتاگون حذف شده بود نیز بازگردانده شد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19787" target="_blank">📅 09:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19786">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏
ساعت ۲۵ ایران
‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.»
‏انورسادات با لباس نظامى آمد،
‏مستقيم به اتاق شاه رفت.
‏دستش را روى قلب شاه گذاشت،
‏به انگليسی گفت:
‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»
اما ‏آن روز كسی نفهميد معنی ساعت ۲۵ چيست؟
‏او در يک مصاحبه با خبرنگاران خارجى و داخلى ‏گفت: جهان عزادار شد.
‏امروز مردى از ميان ما رفت كه خواهان صلح بود، ‏بعد از او خاورميانه رنگ آرامش و آسايش به خود نخواهد ديد.
‏او فقط پادشاه ايران نبود.
‏پدرِ بزرگى براى منطقه خاورميانه بود و ‏روزهاى سختی را پشت سر گذاشت،
‏او براى دفاع از كشورش در مقابل دنيا ايستاد ، ‏او امروز صبح مُرد اما ايران در ساعت ۲۵ از حركت ايستاد.
‏اين خبر به ايران رسيد، روزنامه كيهان و اطلاعات با خط درشت نوشتند: «شاه مُرد.»‏
‏فرانسوى‌ها ضرب‌المثلى دارند كه حركت روز و شب ۲۴ ساعت است و ساعت ۲۵، ‏ساعت مرگ است.
‏به واقع ساعتِ مرگ محمد رضا شاه پهلوی ساعت ۲۵ ایران بود.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19786" target="_blank">📅 09:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19785">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش صدای انفجار‌بندر عباس ، ممکنه خنثی سازی باشه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19785" target="_blank">📅 09:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19784">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19784" target="_blank">📅 02:41 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
