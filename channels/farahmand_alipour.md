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
<img src="https://cdn4.telesco.pe/file/QPhxttf61Bal1DBnavNe44s7Z2aw0MzFFjELH0XlnMRIn_xvexJpAkIiesGYT13amHYS3fPaF6LEBpcuQoqUB25VszXmvoS9JPLWHVVUPLixwEgF7ceEA029XxwmAEfBWFBMuAKAZlKZPKLVqBbLknz3eUaio4W57Fq4JqbAnWR77iKPsORrv3KMSBUg2acPpDLphpVd0du0grQ0T4sZn7HmBM1SErMIxNuVXixWSWp0lETtaOleJVUGOEwHuIXdrg5u84megkKDuq7f8nWiLHOJ87iOsKQrWBBsomDNPabgGHuESG1njjQa3kYkrWQ1ozBhoOdrJQZk_8lM3fi7Uw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 13:56:39</div>
<hr>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPC0_tFl3pbMOow3W4bWk5VLuLoGY6TM0wFhOo1zV30sUUIE2nxt8F0Qs8ZVKN3E9FEqYAX6_2EaMrCNnQZ47ytAZAcJBPiXKPVowGdjzDSeGbz5QtxvWFkumSwOL6q92qbYNh7IYjcJR96LSDjBGnRU5jetamb7s5hEu8s6jLvpolYBz8semwBTaXFL0kte8jHkQK4MLV17B428zZRq58x_0PqCSz10ZSRmV6yrCIQmvKevm2IEKwFWS_0nbJiZmhoakOqvtPVQjnzXq6aZoKLRZfdbpxBU8ZiUcim4F_fzWQ0vMzCgdFBBc1kVsztPDzJwCh_G9lvtG0ZhMb8cxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYaHsv2IVNm9nRk61lBOzxSKSanQRBiwJFHs3jJnL973EvD0q0z46Ad4867yHg2afmhhcyv_lMn3EWXovOLzkOBm-bdFvzxK-3lDeSDdS9OXhVyVHuoQPATDHEzWluZIjyEuQkXreKuYBpD9Qbb5xw7_3Rvn5jCiUSadDkhrhmto-frAOHhHpyBLGn8c8rNRVl9bJBUjCt9i0Pt5PZg1JG9UR2q5dgzESslqL7iToavuXjG1IIcBFzVlkLh6AaUPWza2jloRtZa9SGjqlZ6z-kjCpy27jYbsLX-h0o3f1hZSPyzA778k5LSET7KOdHuMuLt7DGAz16mQxURs2nzmWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=pTE_pvYUWo3TAWAEmra0aKYzeid9S6K5VZf6MAb_3U2kGlfC0U192pI6Vi68x0-h_bnTxprzBr8NLqCtTFhFBBsQFUfKUuzyLRjjWfCYSXLGMWwjoWb9cdc0SJhkBWsNf8lCqDECu2NK5HErAEFRAV0RCFNfFOQxH1pxq0ebRXmCKKHt47YGPQmlpkXZ5U9p96JblQ1DXVvt7ia1q61L2dzvwg7ajOgO0GaVhiW9R4VFAtZJSieYkLRYDX3bbA8jr3DcoTa0rINI-jE6rqGh3wqcOSLHfjE1DSPMAToV5MGSIqn9_OxkvBKaPdrqijkdLlY90YlXQV_IcuRzjWMgszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=pTE_pvYUWo3TAWAEmra0aKYzeid9S6K5VZf6MAb_3U2kGlfC0U192pI6Vi68x0-h_bnTxprzBr8NLqCtTFhFBBsQFUfKUuzyLRjjWfCYSXLGMWwjoWb9cdc0SJhkBWsNf8lCqDECu2NK5HErAEFRAV0RCFNfFOQxH1pxq0ebRXmCKKHt47YGPQmlpkXZ5U9p96JblQ1DXVvt7ia1q61L2dzvwg7ajOgO0GaVhiW9R4VFAtZJSieYkLRYDX3bbA8jr3DcoTa0rINI-jE6rqGh3wqcOSLHfjE1DSPMAToV5MGSIqn9_OxkvBKaPdrqijkdLlY90YlXQV_IcuRzjWMgszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwtalJuI4ISK7IQV7YrAvbHJj4aZpfjdhF9SZnPXUenA8e3JE6VYZ_JgQGbOAe1JK-AzhTyC-u6Ps8BU6bRa-JO1s_WMStSN1Uv7k0F67k970czKZ1Tm98V19lLVw9QRv5st6M_c0-tNi6nh_ibfKOrsdtxJFOGxW6YmxiBJuEa8oozwQrqUZsXwLC1dqMU4371nMe5z6ufR01qgVhDsgJxFeMnRBMvBYgjtLw8w02tcuhsPJbTHlZg0f6pPtYeWjGsN6844T1At9MdsN4Y8i-AwutsrC942gOzp7EnQDrtgr47tQv422sdIF6mVPhHsfqVYxNfFEM0gpUgqxz3tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkPlS5eGMm6Yc2WSpo-utRTSYJ8NveD-Uz_xnXbrQ5OdIOrxaejh4CRYvlbHJijvdWWxn98GV4MadzaLXfnGpTa-prm-wjofhmQjv_pwdLPBS0uIL-6-w4udEWjpNHmXeDi2_W1wBepQswCNwdXVRXlxvmP319q2M8DCnIeZ5381YrzMrIESYlV-3pBN2MSCKLtffFE8GFvQB3MqEiW-XV4Ebomn1ZZP4GBetgeNMsJ4tKrVoPuU9I47u72Deo-xMW5d4YXMiZLm06cBEcoJHFyVGFg_YnWkrtkIbx37p-kmdDJhVdOdc7oOEoqSR5GFelXpdoqukKaWxPAmtAz5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKj_RbNEOApa6XNKCrrK75Gw5e6ZW1EVOpYxKDb6Ux3P_MCLKBpD8crp4tmqBODk0DBVG6X5CrJuMPlligOXIjIUDciCZGi5wMBIiN2oXrD1eezOH5TBeUTDaMamIE-US9vzUSJyExD8-cyxZsXsLI6aDalTb_jzM0fSw69jzDZjlCnxH6UHvUOi743zHiMyPx6y1y5rDgLXs3Yy_uQ3kvKpGXbUPfO9YJEfprhBXxV6a-O611YvPpu5F6USuis8KmI1CYNg5iGsKCT4vqfOx-TJlWFkGqdpVu0aQPksQIUXm1P07_EdDd9XUgLJiYadFvxxCMeLZ-Tp4jpKYEDnDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmKIYoON7V6Ue4IkHr6qG7AVT4tY2Ozky8KeIfbSAqpNh62uYZwH7vemVUT15BNcjb5AjtcsMNXTKvPU2ZJITBXwE9bjHioiK5MfFCLo6F2SnKxt7b5upzfJovKZEPAMhR87YZsoUiR2E_9jwY3KPlTr0QTsS7OpNAeU3V35XqFjIbD3lABISNE4dW9TLcqxnw05fEaDX-tk0S9AkWzHB0j5KywpFhMFNJ4Jn70AMEQCiayYtpFvPCSZUY9osiK66PyhE51ayLuFt8DcGu_IMvJaiBvArbD-RBLN6n9zuJpe1tyjaK7wmCdj0cAnPeypBDf7IKLvd3WVngyZq6Xn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=CGsBezb_kAcCvvIbu3c8ORkvDGf8smzEdU_VVT_TjSLJxxcAAPp1lmm_73MDj13lpt53fG7X9iGyMGB1PsMcQLpupLmf5DrilMcW2GSiuZCPCKfDAYubJrOOX5-lGEWQ_lPQGj_Z7RnQ5v0b8zcr6mW6uHRUji4ANCF3cx6qku8f-YvfFVsfwaAETLKEOXBC0V7b3fF8ZEs5O5b5L0pubu_8VMV6hWvBep58Z96fVX13u-iprdfcuF23fzwt8ir0l2esRbv66E9yIPt5clRxOqTaEr6K5ip-KfgAS_kpXaOm2lfaOq4Fvf4DEAUkf6MOoTeznqvEFx-5KeWi6lfn6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=CGsBezb_kAcCvvIbu3c8ORkvDGf8smzEdU_VVT_TjSLJxxcAAPp1lmm_73MDj13lpt53fG7X9iGyMGB1PsMcQLpupLmf5DrilMcW2GSiuZCPCKfDAYubJrOOX5-lGEWQ_lPQGj_Z7RnQ5v0b8zcr6mW6uHRUji4ANCF3cx6qku8f-YvfFVsfwaAETLKEOXBC0V7b3fF8ZEs5O5b5L0pubu_8VMV6hWvBep58Z96fVX13u-iprdfcuF23fzwt8ir0l2esRbv66E9yIPt5clRxOqTaEr6K5ip-KfgAS_kpXaOm2lfaOq4Fvf4DEAUkf6MOoTeznqvEFx-5KeWi6lfn6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=LA4Fz94EBVFVm1Cp34sJG6WOSsfnVDTlcmjvKSs-dYDwtY0AQl7vJAS_RihmCsb_5fL_Skk4PKXfEKUnKLF-0fI8Um0rSnAE8xPXFkzIa8K5c9HVHPY4TrdUi-bFiSPgDaOYbgU1q_BsnnTtcbAeLIz8hILb-vnzi4MV4DmNM8FQ3Gu1nL61fl9PCA0vdoS2b4I9oiH9OlM8pRQcL0BC536FQkBfsE0FUpFJavt9KlojYfBbTC3PAE096_KGRz747rjH4K5gbOK_TXlr9IY659Bvyc6RqBsmMRLgK3ZaEm14zLFN0UDM_Vt-zx2a8XsLUzIgRwEgVLj0ZCI6FqTTHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=LA4Fz94EBVFVm1Cp34sJG6WOSsfnVDTlcmjvKSs-dYDwtY0AQl7vJAS_RihmCsb_5fL_Skk4PKXfEKUnKLF-0fI8Um0rSnAE8xPXFkzIa8K5c9HVHPY4TrdUi-bFiSPgDaOYbgU1q_BsnnTtcbAeLIz8hILb-vnzi4MV4DmNM8FQ3Gu1nL61fl9PCA0vdoS2b4I9oiH9OlM8pRQcL0BC536FQkBfsE0FUpFJavt9KlojYfBbTC3PAE096_KGRz747rjH4K5gbOK_TXlr9IY659Bvyc6RqBsmMRLgK3ZaEm14zLFN0UDM_Vt-zx2a8XsLUzIgRwEgVLj0ZCI6FqTTHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX_EEbd8ka955gUXa8mjqa3j00ezQAkz8Wd7L1Hn8nEVCuzYntInb8g1G8PB3j6jbX4UYMq1UngMzJnI8rgc3lE54-OZHvEEC7lmVXj9eHTB40f2RWOPjlorBYln1aTS7c-p_wiO2RNOrA7kmRphQSOc0UeJaygPurCnf1Rb67TwkZ50HA1l8eTOYYvvlwCQR7ZpkYQIG4WVmRXAjTwnAez9JZILcbTNSVbzVSyCXsJDd-x8x5-WRr99AUPX3fjklB0Hi9lPLdyzpLvm9Gzs2Vx1XB-jCvs1Sm7pk8JGZla7Rbk-bZhviEfnSZg7kAgCRgsKTOywsOD2TcHt8niaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=jzbZbj7-scTgVJCSvdCzLPqTPNSkL_kbhOu_bzF3pTJ0WkGIXPtm55X7VDOj7plM9xS_VWyajJa8zUbSQveaeWC1styvAQ_9iFWkaihXHVs2e2o_1HG6AOw0irFmiishZ7blo31IShoBRlg6IOxT2yewkE5w96Ntkx0myBj7SkGxtDeA1NImw7E3C7nq9GNhowif7eIHyJmCvZLKVzTpfwFsxBJxGIrE07KGgfgN3qmp4nrfzsi22FKA2e8S-4fnZdbrbzb8jL_dUG41gVR-oTGNaBFxxHs2eMhAobUjC1vBKRCLy4TqCFV1rm6cP3nYlU9iWXoWZGymhUq3CIl92g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=jzbZbj7-scTgVJCSvdCzLPqTPNSkL_kbhOu_bzF3pTJ0WkGIXPtm55X7VDOj7plM9xS_VWyajJa8zUbSQveaeWC1styvAQ_9iFWkaihXHVs2e2o_1HG6AOw0irFmiishZ7blo31IShoBRlg6IOxT2yewkE5w96Ntkx0myBj7SkGxtDeA1NImw7E3C7nq9GNhowif7eIHyJmCvZLKVzTpfwFsxBJxGIrE07KGgfgN3qmp4nrfzsi22FKA2e8S-4fnZdbrbzb8jL_dUG41gVR-oTGNaBFxxHs2eMhAobUjC1vBKRCLy4TqCFV1rm6cP3nYlU9iWXoWZGymhUq3CIl92g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2jXUzua6hqCme7db5HWAsnQpa4fSpg6wrDhaMKcv0NSw4IfhepNxyKTR0VKuswg2bQm6dqIjVuWN9vNMt0tgWoPIa25z3eVX6rx2F3xzLI7YBDjS0ptFM-mAAh0BpkiJpKMZbV61VDsyz92q8qIC6B0UO_5t8MCXWIqH1DYyIsTDXJOLPHRjxQ3t0_qiYmeKCsCn042cC5BM8gBNyDkY1fI9-m1wRB5jeeHkW5p_UyX-OZoRn_nJCNYDrU9ipt_p0JJU8YQy4f3-nH3fXsDN1TNa7RAx8m8XwTzMaqfcLyiSkCEwIgTc9013Shnsp8H96M3EeWlGfE6pzyBze7HHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS5S9d764T9zFk6An4H5s1vCscROBLJiiwGNHZ3PKoNqthjA7EcQ0OEiwVRGC45CrT-B9nfORTMt-zTaBzRuhnwOSAi0N573j2jYXeYHfJjSPJ5MurKlKB607h538uhofhuzsdPrUsKIlOTR0h4fj-UV8LHj-AeaqFVtOq_ia2nYNQcxCdd28v3yIazw3z2Ih453pO2vA11hfz3ufIZ5FU6CWS0lJ0KH_i4U9toPEpr0xUMzz277_Mxdqcxk98bl4rlWjbku7LR-QPbnDZS5NoNMqnOKmnzjRLZ_pskoTfEzF_YClS8gjtIL2KssvvaMGtx2l3EZqqsPISxlkzr3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti8Uz9ARcybXL0HKjBVxmxbf7kS8YOBH18zWqzQl7OOmnOhajooddGtQiqH5K8rmIy_W97Svteux9Rgheqgg7hEYWTVtNyK-aP2yiQ8MbPIvIBcbuMSgDtO5RjsKzznju3mQOAMDeu6lJ-q11twyKlwsSla6sd7d0g37yzLmiXQsLvvJLJHRQbyyY7uw17pNKrSLA0yXcDi7YaUQf5kk-pOD0ZMHSFFcqCpvN0ag4_TPhyaukyIzoS-Xs3Bc9GjKl6Uilf-1C20uhnyx3gXxUEQXXSIkN7RVTOpb4fWwBgTgf99yCp-8LCuhRwHj0aPDT8xSiL5GSZAZmUtBYUsi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vbxhInx35vFu0JMUt4IUIzodAnxhF2MWmPAajg0GqW42xgmayS-ES3ciwQciSScDKBPeZFrztt3UDKqLS4G5ogCQCgrogz7aiCa_bUfFRUQWTmozTXpJAkJQt9rxTQI1UcZFS5thU5vH3jfOU31hsLugPfoiQurzgD6tO6NceMChq2UXNE2gXjaFs5z3yyC3u9m88Sb7ArSjM4qsAobICnkdei4nyLRon7vT_ArqseVTk5joxKLOPxtu4XZ0E908EerRYowcMjguzhWOFq_BxKoo6C3e8D3HX4WLx4hfHygV0--Qmk4_gcAsxL5DfuqtVVVWHnV5_gD2t6fRHmNo1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vbxhInx35vFu0JMUt4IUIzodAnxhF2MWmPAajg0GqW42xgmayS-ES3ciwQciSScDKBPeZFrztt3UDKqLS4G5ogCQCgrogz7aiCa_bUfFRUQWTmozTXpJAkJQt9rxTQI1UcZFS5thU5vH3jfOU31hsLugPfoiQurzgD6tO6NceMChq2UXNE2gXjaFs5z3yyC3u9m88Sb7ArSjM4qsAobICnkdei4nyLRon7vT_ArqseVTk5joxKLOPxtu4XZ0E908EerRYowcMjguzhWOFq_BxKoo6C3e8D3HX4WLx4hfHygV0--Qmk4_gcAsxL5DfuqtVVVWHnV5_gD2t6fRHmNo1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TahEAJjyzkLcwG_A_tgJ_nSwAK0ogmhz3o9DzS74uyJDrht38vN9GU_I5wKvhtsC40k-B0xio9OiadKyIbtP_hqkpsRf1qAbJ3Fw9vAZlWrHnRqGmXy-2ypZ12THdwfQmHSgg7MeFDYZXwYyZUBvf_0xAzx0trY_6H_6uMUpD0fc2FE-stvKNQzHzbF6GgkGcZ4rgq9gGABscl_9jH-QDsLGeNoTLhcH-ldhbsof49sFIdldqw3IiHGIqeMHIqx3b0t6dnpxCJxow5VxovrFfnbUOgQx2rTOJNDs4gVnBc6mgTxygOM6RnjA9YbjMyDJUcmhnCN_LNHnJFCDSd5Qg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TahEAJjyzkLcwG_A_tgJ_nSwAK0ogmhz3o9DzS74uyJDrht38vN9GU_I5wKvhtsC40k-B0xio9OiadKyIbtP_hqkpsRf1qAbJ3Fw9vAZlWrHnRqGmXy-2ypZ12THdwfQmHSgg7MeFDYZXwYyZUBvf_0xAzx0trY_6H_6uMUpD0fc2FE-stvKNQzHzbF6GgkGcZ4rgq9gGABscl_9jH-QDsLGeNoTLhcH-ldhbsof49sFIdldqw3IiHGIqeMHIqx3b0t6dnpxCJxow5VxovrFfnbUOgQx2rTOJNDs4gVnBc6mgTxygOM6RnjA9YbjMyDJUcmhnCN_LNHnJFCDSd5Qg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5zSPoiZ8dLYY3_jeGHCrYyDK2CQPOBD4ls6DoF95uoRPeM8_yCCVLRFk--P56As4C2-taRDj3-rvnlXJYjNiTxOCLr4m7kq1HrYT3adA8916yvOCtBjR07nSCIkKg0bc0YADNMAEFBgPLi6vO0ab8hnNN6tD_83HZ1p_S_-oqrBaeYOFKfYn524PkdSu5EKniZtmrizGrFNE2AjDVqut91K2U5HK_YIex2vP8XWH-hfVpvtpPOTT_b7TlsLdD5h4SuKI-VarR1t0TcV9H_TaaZDvDBjUB_G_Ce7pmjFQNOyunJ6wEyquQVZoxo52Nayoqk9bI-p5iKsIYVkFFQ23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=ZvW6JHN-G6YvDbLGSbhncgwgV4ajpWKj9zSi55WsBdnizqhvb_Hl4bT7AaELTVfeZEuFg9FMpJdnkyPvD2G-JhINQ0iBjBauGvdFEfVlJ9W9v-Hgxok8Cwiky2msF1a388BmexRCn1XSFrF9B03y8lvGo1my4D8EiCpB1ruCey4ZsOeDefft-uQ8UPFFGZS94bKeV0JWlyiNuTJKvDb5fyB0pDhfJEGj-HSIqUB8ZGcnZWyV-hqbz44vpe72dQwssk06ZDrHwIIw28SJLMe2uVSEekoJSBcbRo9l9Miwe6_WTaMK9flLRLaTVrdjRHqnY12JU2PcHwg2LUpN54VhDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=ZvW6JHN-G6YvDbLGSbhncgwgV4ajpWKj9zSi55WsBdnizqhvb_Hl4bT7AaELTVfeZEuFg9FMpJdnkyPvD2G-JhINQ0iBjBauGvdFEfVlJ9W9v-Hgxok8Cwiky2msF1a388BmexRCn1XSFrF9B03y8lvGo1my4D8EiCpB1ruCey4ZsOeDefft-uQ8UPFFGZS94bKeV0JWlyiNuTJKvDb5fyB0pDhfJEGj-HSIqUB8ZGcnZWyV-hqbz44vpe72dQwssk06ZDrHwIIw28SJLMe2uVSEekoJSBcbRo9l9Miwe6_WTaMK9flLRLaTVrdjRHqnY12JU2PcHwg2LUpN54VhDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=KTUQNfFlRy-KdRJT2zfr-3RjXmRvGqN_yXl7TtqjuI4CGl80hcrSTKYQ9utuH9LG0Yt3tKqF2HNFTq33MA6kIFfzqSLuhAVksEy_4rY1FW2En-SEqeMqegbL7IFN0VuoeS9v6le2Ey8T7GmQZOJIYiMuvCVHPk3LP9mf7pXFcY6pPPbHiL6fvJYpihJfttVaT1Wk3vw5KQEj8BD5Jm2f1g-pof0IoqVG4PxHrxGcORXJRb7Tr8TwTfoLoieUUbIuWmhDru4wRvWf1oBY9xHggQ1BiTY1jx6Vu0r6OZdYL_LmZFe5uCzEEAQCIAOrF3_RvcrNnFAzIW9N-o9QjoO5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=KTUQNfFlRy-KdRJT2zfr-3RjXmRvGqN_yXl7TtqjuI4CGl80hcrSTKYQ9utuH9LG0Yt3tKqF2HNFTq33MA6kIFfzqSLuhAVksEy_4rY1FW2En-SEqeMqegbL7IFN0VuoeS9v6le2Ey8T7GmQZOJIYiMuvCVHPk3LP9mf7pXFcY6pPPbHiL6fvJYpihJfttVaT1Wk3vw5KQEj8BD5Jm2f1g-pof0IoqVG4PxHrxGcORXJRb7Tr8TwTfoLoieUUbIuWmhDru4wRvWf1oBY9xHggQ1BiTY1jx6Vu0r6OZdYL_LmZFe5uCzEEAQCIAOrF3_RvcrNnFAzIW9N-o9QjoO5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Y4FWIpm0TuuHzxTjVkkm8PqnPuZZsJqdyt2aDUsF6KRrcjohOqr9855oFDXTRlfpG1SIrGTC6nilY6blDdtZpQfLWM29q7_nZjrUQukcpLe9PmnyBLY-ot_8sjIdQwVrRxfnIibjKOATVk3JWUlZu3z690n08gblFLSfRXYLts_SB_9DY7nEZcXRjmDnLVlvoiiqCgiiC0AnUGoYbuYB4WaDqSL7Vy1ruGBjjwaGlP2jm9jIowhGgHVKq97EFhQqCjn2FwdA6BsrHIA0MqSFjGiAKFK26sQSsIJqSMKVU8qqBG8QOF43EkxzYzGpDvdk2LVnXEzu0YcBUdfVhN9yhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Y4FWIpm0TuuHzxTjVkkm8PqnPuZZsJqdyt2aDUsF6KRrcjohOqr9855oFDXTRlfpG1SIrGTC6nilY6blDdtZpQfLWM29q7_nZjrUQukcpLe9PmnyBLY-ot_8sjIdQwVrRxfnIibjKOATVk3JWUlZu3z690n08gblFLSfRXYLts_SB_9DY7nEZcXRjmDnLVlvoiiqCgiiC0AnUGoYbuYB4WaDqSL7Vy1ruGBjjwaGlP2jm9jIowhGgHVKq97EFhQqCjn2FwdA6BsrHIA0MqSFjGiAKFK26sQSsIJqSMKVU8qqBG8QOF43EkxzYzGpDvdk2LVnXEzu0YcBUdfVhN9yhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=meY1dBmm25-leT5demu21P1E2H3LH-2gSwGcqtgYpLYbI0dXHCSDeiOvNHRCIcyJcOmnKasI20sHNukullo72ZBrMZJm1Ff4qy5YPNlrkr-i7kh5EAxi3JsixcmtxjuAdZVA2AVYNim2p5tJhRPMQkDKOSUkm-hUA0Ly2m-csIDRGnZJxmBgTPImWOvqEI-0wGJOMb3J2IJwKEU_BTTmYGlBNYuJypDQDf9o5G2yRIseZ6dbA5KVUeRabJbQx-LdztkqPVucO_vGOSYGPrQuq8g4llGTnLdv94xT8DXikX8GhjSrxHz0Ch0ilD9BcgxaebcbhRw64EwMWxU6Ty6VaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=meY1dBmm25-leT5demu21P1E2H3LH-2gSwGcqtgYpLYbI0dXHCSDeiOvNHRCIcyJcOmnKasI20sHNukullo72ZBrMZJm1Ff4qy5YPNlrkr-i7kh5EAxi3JsixcmtxjuAdZVA2AVYNim2p5tJhRPMQkDKOSUkm-hUA0Ly2m-csIDRGnZJxmBgTPImWOvqEI-0wGJOMb3J2IJwKEU_BTTmYGlBNYuJypDQDf9o5G2yRIseZ6dbA5KVUeRabJbQx-LdztkqPVucO_vGOSYGPrQuq8g4llGTnLdv94xT8DXikX8GhjSrxHz0Ch0ilD9BcgxaebcbhRw64EwMWxU6Ty6VaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4YYse9dg4JXv7U6mblDrXKS0FhzOLX5zib8tpPzqDMP-UkAFKwM8SHnIX0uEKqn4xyCqbIuX37z0e-vd5sAchUqzJ1dJqLORPjiG9xtjJw0g4Wr8dZmiucXqsxb_17IqDL6ZRr-M-Aeu8ooe4PMZ8Yuv2a6sU66G9Z_wg9sId49rdw4I1eg95HceqYLsU9VvUQFpcVfAgzARSInWyoYFXV5zDRgaT9KGCVWQYJ7MdH7JeAGWsyI5aS3lkBc37VkGjZnDHIC6VCbKwFGrwvUsvzlGm7pUBSoA0yH_GcKk9IJIUeBLP26K4jDD0pv-M5hSa6BXn_OT4kczGCUzmYvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=PPKA7s4HoiE1uR0-1LjaXYMK2dc3e148WYPN-vwTIwawgqJDzZYjE6Hea1THP1_2WFKVTZrAYq6DFdPzpkMk3OAdY5wdVA9d_0Xt_DlELRfm0jqffQZXIOjuTeaolD7hn7jBHO-SZftL4XW1wL1i8Jlb6DHFnMxx6XewG28fJ5lyp4RE-lnTVP7FI4SrpDSYpabL241sBQ5PBVkmqdC6cRWlgNQSmH6Eo3uzXNEh0KF81yd_MffWmGXWSt8LzGTLNWTjBtNXT22XMvewbUvl6TIJNJFUAPk1Kv-zqdSC6oTXEWNIld8ZjAE_21k3t44074v-SWXoRYS1hUBWuEybBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=PPKA7s4HoiE1uR0-1LjaXYMK2dc3e148WYPN-vwTIwawgqJDzZYjE6Hea1THP1_2WFKVTZrAYq6DFdPzpkMk3OAdY5wdVA9d_0Xt_DlELRfm0jqffQZXIOjuTeaolD7hn7jBHO-SZftL4XW1wL1i8Jlb6DHFnMxx6XewG28fJ5lyp4RE-lnTVP7FI4SrpDSYpabL241sBQ5PBVkmqdC6cRWlgNQSmH6Eo3uzXNEh0KF81yd_MffWmGXWSt8LzGTLNWTjBtNXT22XMvewbUvl6TIJNJFUAPk1Kv-zqdSC6oTXEWNIld8ZjAE_21k3t44074v-SWXoRYS1hUBWuEybBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=amZu2-8Sgid9pgm7ojXDfRXcQ4sh_kNrX116pfD6cxwgMAOFvvQW7RSZIb7V4rYtR_LyyD5PjfFrHBe_viJ0kMB60LqFKKWaDgD9DjgYpmYmZIYOhCbKmCIlwTbeCN2rnF0r6Ra_3fT-wo_xCLNlNmZKn_TTwVB4kzwswm1Tzr5f204uAZXEyw10kvk9jXSW00WM7AQ0zMu2I9RWaf6cH0ofxMTLNL9Wm5eq6MHvCDPp09ZbrFiPfPLDUAWvxCswfP3dHGSG62rlhLhsllrqEZ7gpv6PLTubTyGeEwi8vmhTPTELI_PTuLQR7d-tw5812uy90V1mcj4FVbaO23VwuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=amZu2-8Sgid9pgm7ojXDfRXcQ4sh_kNrX116pfD6cxwgMAOFvvQW7RSZIb7V4rYtR_LyyD5PjfFrHBe_viJ0kMB60LqFKKWaDgD9DjgYpmYmZIYOhCbKmCIlwTbeCN2rnF0r6Ra_3fT-wo_xCLNlNmZKn_TTwVB4kzwswm1Tzr5f204uAZXEyw10kvk9jXSW00WM7AQ0zMu2I9RWaf6cH0ofxMTLNL9Wm5eq6MHvCDPp09ZbrFiPfPLDUAWvxCswfP3dHGSG62rlhLhsllrqEZ7gpv6PLTubTyGeEwi8vmhTPTELI_PTuLQR7d-tw5812uy90V1mcj4FVbaO23VwuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG2x24jvwXIKNIEmpEe6BnsCVRsoP-WKmzxMtQDJ-d8lwL2kqR-tfTC4tEsFGVFiSuFs2Is_5nnpEUoGa3c9pJv8KUskbo3l1rN8ZCYV1Qg8XQzetOsD4Mv4qdJj_GxKrkOa8xhvHiCVTAzgbe11_h-BLEgm_mSWf4IaJ3OQt0cFJyAahyNGVJMLDV2OHRYgZA-Oud1OaFlSuCTQc9XoaaPqVPYS0PxE1hslZ4sHCxCi-PEkBEDfd7B6BPSIXwHxIgA-U5-iviW8QpUo9-NjKylcMeFwQpQJReI3wT8qg4lPm7UjtAG1hUmz5QyCxtvVYpRCAO4qEZsDmHiHi3uX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=SYgT7iQ7pJWpebSaHrkE62x2uACRPRMz-XlJa5tuqIw4DFgeOWrN5slzM5pVNTLQ8Gy3qlbYJfrhQhfNgRPzRqJFGUN8Y0RAN48kk52P4zPBlxSrek8Ny0-BrqGftOKgramc6DYZqvJqyCitSoF5hKRBM1QiPFwzwES7_Fj1jAukuzdh_kWTOVpyWeAvKlTjQrQKYXhRJV2eaxmMuU3nNkX9F1iG15G6cT_7jjr9UNyEMGkjAySc-onPOhAeDAdq8K88vpr-7BfcPwos5OWCV3wFEZ6T-kcqadbxTNd1nmmWk6VGWP_ySY2fxFO4tqr9x6xJTGIBPdBlkW508rn0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=SYgT7iQ7pJWpebSaHrkE62x2uACRPRMz-XlJa5tuqIw4DFgeOWrN5slzM5pVNTLQ8Gy3qlbYJfrhQhfNgRPzRqJFGUN8Y0RAN48kk52P4zPBlxSrek8Ny0-BrqGftOKgramc6DYZqvJqyCitSoF5hKRBM1QiPFwzwES7_Fj1jAukuzdh_kWTOVpyWeAvKlTjQrQKYXhRJV2eaxmMuU3nNkX9F1iG15G6cT_7jjr9UNyEMGkjAySc-onPOhAeDAdq8K88vpr-7BfcPwos5OWCV3wFEZ6T-kcqadbxTNd1nmmWk6VGWP_ySY2fxFO4tqr9x6xJTGIBPdBlkW508rn0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=t7bHXXbj4VR4ARBSZR_t6LZI13vm0759mH25SIl-erfJECDEPK2xN8Di0fXV00uMMrJg7nP1spv1t6KZmzuAYkROi1hHP4QYr2PWH6Ds0eEdO_wY3AaOJgiQkZa4-OlICK8aCd5pQajMQMLaFKMwJdJ2Za7GlKCoNno5kYh7SveNHmufm9uQMaqHw6y-JePqi51Zj2HSP4OW7YUaZfWOUT89N9MQZN_VHsnEmPYl1JssymLayKjE43-WfkqQOPNVg_xBVOmT81Ch4QC2yQhc_ypdxwgtKsde7uvF80O4YIQssrjz89bMa_74FmeX4cBKdJA2Lg-4OkP-sB1gabVhETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=t7bHXXbj4VR4ARBSZR_t6LZI13vm0759mH25SIl-erfJECDEPK2xN8Di0fXV00uMMrJg7nP1spv1t6KZmzuAYkROi1hHP4QYr2PWH6Ds0eEdO_wY3AaOJgiQkZa4-OlICK8aCd5pQajMQMLaFKMwJdJ2Za7GlKCoNno5kYh7SveNHmufm9uQMaqHw6y-JePqi51Zj2HSP4OW7YUaZfWOUT89N9MQZN_VHsnEmPYl1JssymLayKjE43-WfkqQOPNVg_xBVOmT81Ch4QC2yQhc_ypdxwgtKsde7uvF80O4YIQssrjz89bMa_74FmeX4cBKdJA2Lg-4OkP-sB1gabVhETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtizE_atebLD_DhT6ezA-X4jw0qW5oZ_kvC-uDA2bsWM7UatueOEBG8eRAtUw7dCeAUslvjNbdkMY5EI7N1tV7VmvcNxmT7L1Ufj2WjXjvDf6Xa9ocGFdzu4llNl6mIL3gd1nvz1czzVVzj1GoZ0FXUBySTOck0e8z9dlTmZ6DbjRkxJnvzWNBBT_hMdN9Q7Fg8o-IOg1F-B1O4zDhcrn0Rx-k4Rofmu1QHAPuOPdD91T66foWedihA_GrtQIto9AI6fz4Zal5D5my8hyMMj3wXuPrUlITuNDtLTkMXqMcdWd2GF8jnfTF5IOT9qaBaVP9kSmLO563XWvW-xR2gCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XhHqhNwn-1HN4hXtCXauwGsKGsJEEuzybpBdJXm9nsdNHLQddnNekBP9stmUe5v6NbRDsEJfcCU-FpvyTrSxcD42wxWO0JK9WIupoWn1RWBltW0SP9_eEjCWVvQkVjiyYde6nsNt2_kREMpIlwTJ8e63VXQ8ZfOxlr058wg2V4tQgoG06qseUz9UzIR9972OvTbY6tSgrvAo2ZJYT4zlLwvq1BaJr1OkXarPu7M1xhFMDro8Z8lMlrQr3vuxbKJpxGZ4ldOa0PE0bQQZ12SAgG48YGQHGPCB5wCYi8K6ZLAhjQbPBXT7Bp3JWx1Z36X9oEDvwNIaaYIQxIulJkEfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEF33Jhgwt7rddtYQA2-0McAKAwRpq2u_W_cFDn_yuGhgr4Rtwtryk32n71PrqJZ_daDGex8cyu-ldtiCgG7femOtF_YCE_oIrh7TgAWKUld7jYWWNOpFo0MyRd4fx9fgrVqmchZSh2ne7_f-u180mwVZ1W09suycJ37xz3bZYLgR3FaiAg26sqNuF-4dDtSfmzEgFUFbiJKhVBHZraJI68wadR0aubCsZOJ_AxX7VmSD-s8vkkIe6SwljKoLIo-yLGmXESE9EL-p9a3rEYY88KPjQONpmGzXDNTmagfldjsGX8mPJpLGy4emVzH8qQjiADfjwCTuIWRd3kIOkQcyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=CICWTP02JBgDtP7yCgxeL5iEKz-Egs-Les_3C1qMY0UdtfYr6B_Sly3kws6NKMDm-viZGiCpXcvF-km3LZtErfxUtnKKi1hzxWCvOZl3H4e7pjgc98kHrQd4HUV9meaBGGoAy8-7FhCUO2YvnB23uppTmpsjPYbR-V9bKPzRogzw4CRblJNqffx4RegkIbTa7fDblL-Czu_4fNgyamcY9I1q5WBazkjSP60Sy-Jzrp6wxTv_vGzQAgOQi5sHhP_scVmHhukFJIQEIDOBtr1sz7i-HHApsUsfRDgZBlnmTrrTg8a-5ZFe_0-0W0ok-IHNc2RDolhPmqPRovHmj4Prow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=CICWTP02JBgDtP7yCgxeL5iEKz-Egs-Les_3C1qMY0UdtfYr6B_Sly3kws6NKMDm-viZGiCpXcvF-km3LZtErfxUtnKKi1hzxWCvOZl3H4e7pjgc98kHrQd4HUV9meaBGGoAy8-7FhCUO2YvnB23uppTmpsjPYbR-V9bKPzRogzw4CRblJNqffx4RegkIbTa7fDblL-Czu_4fNgyamcY9I1q5WBazkjSP60Sy-Jzrp6wxTv_vGzQAgOQi5sHhP_scVmHhukFJIQEIDOBtr1sz7i-HHApsUsfRDgZBlnmTrrTg8a-5ZFe_0-0W0ok-IHNc2RDolhPmqPRovHmj4Prow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaWTtxZnK8OBJrKtA-1k_BDl14R8GcUf0_-XFwlWEZAHH2Uc3lhDwUjeAJOIzUfLNbZbtAc6j3jctGrEl9caXhkiRAnfE0OVmhBFTM7KrA4sOetL3h8F9800c2JX1qVmWhl0ocMutChiOHyi5pQ9PLnOQTWhZwEjOhgQbrGRXmBJXSWRPMYsTifpvun_dnTH7Z8rKdibtscEm1Ob-M-PuGp5fmNZoKZbjD3ldEResBUILE-XDdhcOSTDneT5jf-Y8F51tfoetxX2vOUboNgUOkKKriRJoJznYACKNs0-JEyzpJIOxlyi9D2Ykg7doAuGg5BrTZmdNcrLMQ0fda7WVceI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaWTtxZnK8OBJrKtA-1k_BDl14R8GcUf0_-XFwlWEZAHH2Uc3lhDwUjeAJOIzUfLNbZbtAc6j3jctGrEl9caXhkiRAnfE0OVmhBFTM7KrA4sOetL3h8F9800c2JX1qVmWhl0ocMutChiOHyi5pQ9PLnOQTWhZwEjOhgQbrGRXmBJXSWRPMYsTifpvun_dnTH7Z8rKdibtscEm1Ob-M-PuGp5fmNZoKZbjD3ldEResBUILE-XDdhcOSTDneT5jf-Y8F51tfoetxX2vOUboNgUOkKKriRJoJznYACKNs0-JEyzpJIOxlyi9D2Ykg7doAuGg5BrTZmdNcrLMQ0fda7WVceI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=tzJcdDuI5LdTsTfW8oh8oNIjCQouEh5b4xo_cOeUThNkTqUetOuY-XjdebOcZDWh7a4aVUp1ZX-GYdG12Fvr9uljTOyaz9WzgU62-nuP4BJy68-8LWoNPSRHg-dfDPWmVolS3IU23Cr13w7JwUQOjuceSe_j5hod48z0uM5rd3AxphRvbIFl4qRJ_mTghA7sa-JBDuPcqafi_G7NczMzHFUWYm74ysT8dYiu5UjUyXgyN6PffEACWampHcJGAS_fKpjgBxZ6pfOT2--5Wi3H1rBSTQZsEt793Sj0g5L_K6R9FOHLx66Dk3wig2FFXHtAEZMX9pIKneb6XAP-XGhqbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=tzJcdDuI5LdTsTfW8oh8oNIjCQouEh5b4xo_cOeUThNkTqUetOuY-XjdebOcZDWh7a4aVUp1ZX-GYdG12Fvr9uljTOyaz9WzgU62-nuP4BJy68-8LWoNPSRHg-dfDPWmVolS3IU23Cr13w7JwUQOjuceSe_j5hod48z0uM5rd3AxphRvbIFl4qRJ_mTghA7sa-JBDuPcqafi_G7NczMzHFUWYm74ysT8dYiu5UjUyXgyN6PffEACWampHcJGAS_fKpjgBxZ6pfOT2--5Wi3H1rBSTQZsEt793Sj0g5L_K6R9FOHLx66Dk3wig2FFXHtAEZMX9pIKneb6XAP-XGhqbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWGW4geOPrlmpIWjwfBZvCgZA7Rflm4SOFqvJMHE64evjOAYK9qqFl1D2oIGmVbzWHlNmEgEBittbJMsv5af_SXSjJU_QPbsnuI95ayue1rbcA8JQoBuZwqvE7m03R-10Bt2LjcpYQKjWtKK1ZzEY1Z1IpKoqtHXJ7azJ9Wv7wARZrchQ0d4ghIKbeT0Ax7e3Iw6UOVMwTaNnjIXlFXdB0wuvB2Xy4rCrzQzAD3AAspzvlS5_xDYoGcdvbsYkjjlZO5oOOaAwGLFXrYP4AfOXJ-Vd-rEhi_4IEMSnJT0noazyOf9755TyWFutL_oLzPMDBtvxpFaq7US2624MAJmJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTlsdET8AUGzsH51pox-k742McCVWcxAlQU_IF79rqZ948SZX093HguIDp8rnpBuPP-kAUxemywvOWAr_Z09Huhw5RhRu9i7qRpUoN2zauAr7Q34ImHkP4AXhoPCfpDz0bjdky9IoEEkJd9zX4R3kOPtOPzPnYb8ymEpLUpmUgbPpFngMSKCxPKVvgU2lxZapDuSL4masWeEy0V7EmXAxESnOPh6N9H1j4djDWeBLzPF6eYFBt8EdvbdLLLApEJkW98NbQCEIH23y8SDzcF0xnAOtlMyJ9-jEhOEskMxtncFvE1FH21CfbalbjRzGxturrB_hLwrjBcbkGoV8L6wqGlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTlsdET8AUGzsH51pox-k742McCVWcxAlQU_IF79rqZ948SZX093HguIDp8rnpBuPP-kAUxemywvOWAr_Z09Huhw5RhRu9i7qRpUoN2zauAr7Q34ImHkP4AXhoPCfpDz0bjdky9IoEEkJd9zX4R3kOPtOPzPnYb8ymEpLUpmUgbPpFngMSKCxPKVvgU2lxZapDuSL4masWeEy0V7EmXAxESnOPh6N9H1j4djDWeBLzPF6eYFBt8EdvbdLLLApEJkW98NbQCEIH23y8SDzcF0xnAOtlMyJ9-jEhOEskMxtncFvE1FH21CfbalbjRzGxturrB_hLwrjBcbkGoV8L6wqGlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apTzmktSm8mwGfSbI7GJTefEakqpi0iDnyIhvU18Ma0abviHUQl_Ix_650E674iDnsieZtmGSz0nn7v24kMBmJorpxrY25sjVXXtK5ZZWq2PArQN1vFnljNn_q5Zz_ozhJSNsn34RTHw5gQWyx6tNQogx7mipdw7AfQInMP-0vG1GuDru-hqnxldQsE0-IT4dojDu3GLQWakrLnfk89CaCmGXVsdeUkvJDydkGHAgyl_l2YKTfJjIP_HpLpoVAbm3aN_7ZQMZ4nnxW4UC3ng0qY898gmJHFXpoPXy9bVYzMzICkolmibU4hug5B5B5Q8vUPM0NRr2AAuZ37WpwJVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=KIOg5-AnT346l92-LJ7O2ybew2-ht5c2highcFbJwkJ3jbGUcfc6Lo--xP5cr76Rvs4KAPbt6wVeW7XPJbY42ZLftJHP1xDgMO2AT-ozm1gtbdyPYaRfd0lr5pORHRDcCC6uU4FmeX6jqSPGbyTpqES40tRgw8MIxTMXiCLey7Ix6U_W9jA1Zb6hEbAahym-CGbtw-xmmoaC6DHrsWX8tkorY9WGlOtGWMQd3k-8HECfrhzNTQYCQXupM3IqS9x5ezAgdH4r8IsP7EIYsznI_BeD33hI21u5ImmyHHd5Twu2xtKgoPJidlEI93k1ZsLUK9mbYHgfv_KPRzka3F6_ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=KIOg5-AnT346l92-LJ7O2ybew2-ht5c2highcFbJwkJ3jbGUcfc6Lo--xP5cr76Rvs4KAPbt6wVeW7XPJbY42ZLftJHP1xDgMO2AT-ozm1gtbdyPYaRfd0lr5pORHRDcCC6uU4FmeX6jqSPGbyTpqES40tRgw8MIxTMXiCLey7Ix6U_W9jA1Zb6hEbAahym-CGbtw-xmmoaC6DHrsWX8tkorY9WGlOtGWMQd3k-8HECfrhzNTQYCQXupM3IqS9x5ezAgdH4r8IsP7EIYsznI_BeD33hI21u5ImmyHHd5Twu2xtKgoPJidlEI93k1ZsLUK9mbYHgfv_KPRzka3F6_ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=dGqz8WVP6LgA2tMDJuPEd47Ez5uLEPTpa-V0njeUzzkMrJki-26CzCocbkx0P6NX5o-03H9S3eTvfF8QT374Cn3QKBygJV0n39F2h51ZQRdWQaHeMydQqjUB-oBYlT_Ns26xXmeF4aFbIHgH37171aj8ofL5Jbe8HKxznJBTSwngtBTefL6oy36LzhMLOtGgbS8vRn_siIwGIm1_9GCSbLFGBFfyPjuZcdL8bgryg8c1D7L7TxBVOvTUkvzEUnF2XVjmwU6_58VciuYwRDeHYGhNgjbE62z0Ja4k5ecX9EJcvhhwoQu6SdVaEvx32HiXwYaGkA2ypG7eyK-w3Lteng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=dGqz8WVP6LgA2tMDJuPEd47Ez5uLEPTpa-V0njeUzzkMrJki-26CzCocbkx0P6NX5o-03H9S3eTvfF8QT374Cn3QKBygJV0n39F2h51ZQRdWQaHeMydQqjUB-oBYlT_Ns26xXmeF4aFbIHgH37171aj8ofL5Jbe8HKxznJBTSwngtBTefL6oy36LzhMLOtGgbS8vRn_siIwGIm1_9GCSbLFGBFfyPjuZcdL8bgryg8c1D7L7TxBVOvTUkvzEUnF2XVjmwU6_58VciuYwRDeHYGhNgjbE62z0Ja4k5ecX9EJcvhhwoQu6SdVaEvx32HiXwYaGkA2ypG7eyK-w3Lteng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=OHsdm09zhZbJn8qhRfKdpL1neBdCBUa_A3mZN-is7NyS8cvRN3kSvGQHfiRYYJ4xFF8N7MdkVpO7vqz9ntAMcED0_7XcNEPDfXNZBX4Y5L7cNCzM9InBVfFerHFxac6fTo7OELw3g4kEfmKqlGtYGK9Da6ZxotS3Ze7G5bxiTI974Y0MqrtlEFcHSVQp6dAKkJ2Fp7LOyFabQ-nQYK7cYQMsp0AgXx69ONbTvX-vmDNm83RUZGriHXAuStmwrj1awTilrhWroBIswYNvkJWLX7Oh801K2Ao1FWwOJno1ZMqaa5_OZlG7ameXb08K6P1742o4pseg5ZETUg71EkMVLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=OHsdm09zhZbJn8qhRfKdpL1neBdCBUa_A3mZN-is7NyS8cvRN3kSvGQHfiRYYJ4xFF8N7MdkVpO7vqz9ntAMcED0_7XcNEPDfXNZBX4Y5L7cNCzM9InBVfFerHFxac6fTo7OELw3g4kEfmKqlGtYGK9Da6ZxotS3Ze7G5bxiTI974Y0MqrtlEFcHSVQp6dAKkJ2Fp7LOyFabQ-nQYK7cYQMsp0AgXx69ONbTvX-vmDNm83RUZGriHXAuStmwrj1awTilrhWroBIswYNvkJWLX7Oh801K2Ao1FWwOJno1ZMqaa5_OZlG7ameXb08K6P1742o4pseg5ZETUg71EkMVLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpV5ys8QikpD0SyIVmy-O1VXDNzNaD_sEHNSKgE4BQTQ1Tkboj01ij4hExQiXxdQJDcBBizJ1_VmhJpNMgrDcfyz_Rf71aFh4VxXXMDWreq7fYSe61TjdD4BiyXOrqIAozvJE6lA4COtvJmAtu4uLSpYhs-t914a4NUQOGtDupkRDknoBLFI_oba3jovAjOFzwBjOr3VEfjgusW-bXwoGHeyf11iKMgweslOGknAeCy4Oflyp9IyPd_W6nrPzua1gmXod2CbbhO5lnQloHEMn27Z_DEu8FwtYPYhZIMKaXxix4CTUjKolZmyNz7FEoCvA9UmtYUixv9YB3No-0gO2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea4LHEDJnr-3ogqbC4Bnx0b3Io8KtKqHlCi4SDdvzOiEE_wqpTT_TvjtoQadm_x2n8bqxfO_jiNH1-gFVW-cJYXz11brmYwaGONs9h-C-1goYOSkuLJZenGWME8VIDom-6koEBYPvnPfhaIZmIRdwBkH15-gCHXTDOCkfiuaigGrseYqqqZGpQAP_f3I8fPaRWwBCBlw1nITEq9a2dJTpvRMr_158T_YC_XqCiNyJrZzXH9fK4oxMBmj1RAZG1D0Ra4l9FzF2rtKiUIG9-Hx51Ik5dE_mGAVtB62N6w1kj3qqYJkf3P6zCZYws7czutNApipjR6cwfVps82MbJBc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=cDs7TLZ7BluHBkNX8Tn_w6mj6AfaP8m_2I8aG5Nbe7jNcU2YP7RU2wSE_DMVw8cc-vl5CdG8ZpLoPL0ZYqCw6Y8uaji1t7bB7jaVJRY1fi-9hiGt2wcTPqrh9GHevSxCLFbHtTkIk0Qpy00tmsTozcWhV0ZAte-MRUfEoeMOjvmqosX8vOs2Xb-XjhW9SVG0K7hzGxnxLPX05OESRAqq9h46nPKzveCxe4xdJQ1xNd0zguUeroBV5e6A0a5jwlLGfTQ79KicDkcqtG-y5DPsRh2M4oULK7YSsNf1IhX386zVMjwPAuJ3VsbF_OkhYKZH5g5EB4NRqRlu0T3goDgZiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=cDs7TLZ7BluHBkNX8Tn_w6mj6AfaP8m_2I8aG5Nbe7jNcU2YP7RU2wSE_DMVw8cc-vl5CdG8ZpLoPL0ZYqCw6Y8uaji1t7bB7jaVJRY1fi-9hiGt2wcTPqrh9GHevSxCLFbHtTkIk0Qpy00tmsTozcWhV0ZAte-MRUfEoeMOjvmqosX8vOs2Xb-XjhW9SVG0K7hzGxnxLPX05OESRAqq9h46nPKzveCxe4xdJQ1xNd0zguUeroBV5e6A0a5jwlLGfTQ79KicDkcqtG-y5DPsRh2M4oULK7YSsNf1IhX386zVMjwPAuJ3VsbF_OkhYKZH5g5EB4NRqRlu0T3goDgZiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elwh_1TThkGefc6rQJ4qrMH7QCmg5tYP95W_8ZrY5v-gJST48U5ePQ9QAzGVleoIdMjKLx-L0HHHNT0qOBjCfE8mjTdWsYEqsqJ7HexgRijBI21lG_Mg9gJnwNczGed_SJ-WSqPPfJIYVgQv8eO2UA2qBnubgG6ZH8_LYak-18uHOs30wU0CIvawKzM6qd3pt7U7N-4N4A4p9h5FglVP5kLvHwGVzgb4oRryi-RPAq1ADvyslH1_7-Rv9Hv_5QwlrM68RT0jVBKpPbt8YKVconKESQNfI4Qb-RT5dKJ1ivMkuGqogFwlckDuYvk-9ZnCjwd-Pxiu39sLkY_q8QUtMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFQNfEcOC9h8vWRCq6W31G7csITeMe4LaHF2V6CrAAHK-SCLpjHlyuOsg3sOeRFQ05qHSgdu4-bVJnAdlZYuN58AbFDimTqsOYiXGpXowMJidRFmCqAIq38dz6FrWhVKdE645tHunfm8isRfOmliWMdqBGlAzwKAf8qETTA1oYW3DNFEaSRgSM6jG39Qxh-_ynUJiUt46BIW1X7VQIabE9sbZ96qG-YPaXWte9kTQlpQpirhlQOsyC-tPFa9wmuafDfgtTonGNY-foHGGIM1oV6ex70F34j8n5wFzec3yoCxeGbQ0JcJO2to6ixHYJyg3E7O6wCw3qtUiOxaoLXueQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=cEwQezIdCJFN_5LUQEO3xbhxQj36BNCLXX5M44QIEfY7sXhT1IMT1P4QHxeItzF4N9KmiCEVRU5TF_KbhQgpJ9weENKw6tOE3CD2r-xp_RVFOX55vM6WXI3QqSQsiER6TuJ9dJujA-cnPvYoigB_MICaHEXsc8LXWjHLwOOsDdnoBiGa9RRg_fEUb1jR0sKhmfATd3I6SIhVOba6ITB59oTPmP_LDuy_kxLs0RqpIC2jLI7vZ6SLvjbGRKa9ooox-0BoPK-jr6quWIJ97eKiaMuhlAqXbTDrfemX0RBCApy3aplhf0EWGwnI4SPDHcjO4A890UVYQIpX54xZiqPk8R4LBEMiVeTXHWHOLgVwwhfYPAqs6dR_mSs6w-jskXnZCzXC-VzKZvQ8AvFLCf9GZ8mRCNcksFGBhu0pyYBmATi-ocRvx_jLlRrZ8AEB6YXO-Rde0TBfJ1J1E8leXetejgRYxpKbisiqUnHxVA44RupwtKlgJkY-PQ6qkOzfeT0moxNB_fu92aSBe22mWZEmIUbsHcRJvb-k9w9dXIZk2JESuBpy9Emg02i6-cSR4e4F9c9TZrTOtjgdYPJf3eUYTfKZo_OKDUvnqN2n9oFRTrWmhqDtH8fWHSLxBNKhK9Bjv_TGc3HfHlMS0fePnH2k8bVZLqcE1BW9w-LIcyKrzdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=cEwQezIdCJFN_5LUQEO3xbhxQj36BNCLXX5M44QIEfY7sXhT1IMT1P4QHxeItzF4N9KmiCEVRU5TF_KbhQgpJ9weENKw6tOE3CD2r-xp_RVFOX55vM6WXI3QqSQsiER6TuJ9dJujA-cnPvYoigB_MICaHEXsc8LXWjHLwOOsDdnoBiGa9RRg_fEUb1jR0sKhmfATd3I6SIhVOba6ITB59oTPmP_LDuy_kxLs0RqpIC2jLI7vZ6SLvjbGRKa9ooox-0BoPK-jr6quWIJ97eKiaMuhlAqXbTDrfemX0RBCApy3aplhf0EWGwnI4SPDHcjO4A890UVYQIpX54xZiqPk8R4LBEMiVeTXHWHOLgVwwhfYPAqs6dR_mSs6w-jskXnZCzXC-VzKZvQ8AvFLCf9GZ8mRCNcksFGBhu0pyYBmATi-ocRvx_jLlRrZ8AEB6YXO-Rde0TBfJ1J1E8leXetejgRYxpKbisiqUnHxVA44RupwtKlgJkY-PQ6qkOzfeT0moxNB_fu92aSBe22mWZEmIUbsHcRJvb-k9w9dXIZk2JESuBpy9Emg02i6-cSR4e4F9c9TZrTOtjgdYPJf3eUYTfKZo_OKDUvnqN2n9oFRTrWmhqDtH8fWHSLxBNKhK9Bjv_TGc3HfHlMS0fePnH2k8bVZLqcE1BW9w-LIcyKrzdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETnk8iwa6ykjd02IZEvV_6RS9W4aO6DanJGmHr1Ymk5E8QJY__pvs1v77xZwHoqqHugcsloVnEucDIRTbcrN2LhUSptN6z19XooF3dr4jqtPezzVf0DCEPmwCwuDdtJYZbFu5PaSYNdApQFjjAmqTqEaejc-RWwl6JIvhblepM0c9CmNvwTEkUlof941JKtKtuLsZgp2fBCJaCT1KElEXSVqVQn6xHDCPVnTL_o9IFU9AkAb6QjfvwDxfgSeaQxTqVlUAPOf3wIvMCTfwTHLBmkj0fGZwWc4wyc-ISjWyAb_FwfCzsvm4Ip1XOuEPmDuAQgfV1jVrKI0bZ7iXmut_csA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETnk8iwa6ykjd02IZEvV_6RS9W4aO6DanJGmHr1Ymk5E8QJY__pvs1v77xZwHoqqHugcsloVnEucDIRTbcrN2LhUSptN6z19XooF3dr4jqtPezzVf0DCEPmwCwuDdtJYZbFu5PaSYNdApQFjjAmqTqEaejc-RWwl6JIvhblepM0c9CmNvwTEkUlof941JKtKtuLsZgp2fBCJaCT1KElEXSVqVQn6xHDCPVnTL_o9IFU9AkAb6QjfvwDxfgSeaQxTqVlUAPOf3wIvMCTfwTHLBmkj0fGZwWc4wyc-ISjWyAb_FwfCzsvm4Ip1XOuEPmDuAQgfV1jVrKI0bZ7iXmut_csA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=IPTaRDN5GTvfY1GjklZTlKE0vNARBMX-95VpkP3ontiIAfAO-RNfl4lM3vinD_LdopKsuCeUJSDIJJXRHnJlP_DVYqtWwFjetDsYIp7CF4o2_1rVN-WZlCRlAEbwaLwEwX6QKhiG72r1RpemD7DskB85SdyoKFvDMIMNbpVcQOT7mfxaY72BW6Ks5uf3eIU2zNY3vp2U5XqqA4RLeiMiAiqLH65rBJmFKAQNCT01NbCHFGu89RQB-wOx8vTq6omXyMOZWYG3qTYDguJY-uU3awN1CzwqDPKrBjwHCt41eroSE3749KJb8x-VzJh6M-uuhkL_0JY__ii_24B3g_77h4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=IPTaRDN5GTvfY1GjklZTlKE0vNARBMX-95VpkP3ontiIAfAO-RNfl4lM3vinD_LdopKsuCeUJSDIJJXRHnJlP_DVYqtWwFjetDsYIp7CF4o2_1rVN-WZlCRlAEbwaLwEwX6QKhiG72r1RpemD7DskB85SdyoKFvDMIMNbpVcQOT7mfxaY72BW6Ks5uf3eIU2zNY3vp2U5XqqA4RLeiMiAiqLH65rBJmFKAQNCT01NbCHFGu89RQB-wOx8vTq6omXyMOZWYG3qTYDguJY-uU3awN1CzwqDPKrBjwHCt41eroSE3749KJb8x-VzJh6M-uuhkL_0JY__ii_24B3g_77h4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=UZeenUiChwogHN59tjRY4TOknKYhcC8sn0v32bZJ2-3eM4uTHqZXh0_E7eYMniXThEs7qthRU0XA4H9oOEvux41jkR3eDlFgsydw_sMVVKmRHLtRoP-H4Jui2aEwNVxFDSvNJ-XkaRDQcEGH0o8qt0hJWxdwsLjY0r1pRM_6YokHkBQ0K-1JRuNZqk5k7zlLqfv9acJWkbPHAd3y3WLNG_vbGORlOZ_lOvm5CrLCQaTBIkCB6YDvpz25KfQ37lBudm8Y-QbbKS0qEx-di1BrO0CfDPGL56wwN3yywRCaoCOj7QWod0MqratwCdyts6xcFiMN5zySLevB1Ientbyrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=UZeenUiChwogHN59tjRY4TOknKYhcC8sn0v32bZJ2-3eM4uTHqZXh0_E7eYMniXThEs7qthRU0XA4H9oOEvux41jkR3eDlFgsydw_sMVVKmRHLtRoP-H4Jui2aEwNVxFDSvNJ-XkaRDQcEGH0o8qt0hJWxdwsLjY0r1pRM_6YokHkBQ0K-1JRuNZqk5k7zlLqfv9acJWkbPHAd3y3WLNG_vbGORlOZ_lOvm5CrLCQaTBIkCB6YDvpz25KfQ37lBudm8Y-QbbKS0qEx-di1BrO0CfDPGL56wwN3yywRCaoCOj7QWod0MqratwCdyts6xcFiMN5zySLevB1Ientbyrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLZs9JIkv46U7TVTnfhpGB34df9Nn43US4jSe8FeLA4sJdtLc5MKo65xB1XRrQLezMFvqmEHtgg1aa23JgdFxwxlO52aQzH0mUQnLW04zLa2wH9Vsrja4OFUGvmz3FORDqZ-J1UIt8GzEIAbDHWlup1KV3GmVx-ecCAHJgLaVE3xC417JfN-Er7T4t9I-1A8MOGNfsfuUtt6JCpK2qa_HA6NLT5bwJh_7fyJfKRcFSu5cE-iWI4JevpsjAJWhyde0dwETyg6LGccewSWDgdkgo0ZtuEprdoGiaRR8a_Wu-YzNkIOUsYfEkCnlH_hokGDZ6MOKNw8M0admyUDU8_daA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYqLwTefZ6U7ReQF74iG7iWUrTVJBtKzBnK7n8jwqFZF-yIgZMVqalX8sbZ9Hpu2LnLnj3Azfjszh5Bavhun_FzhjYbItPf_o0PuS_Ja_7i_6pSDa8dvJm-k7edbhMEwcNB29aP1CchnsPD0qC2M9hp-hwFIPn1Uu3TRPF-XzKGktGLA8CVv774DwaYg71_FdL2NUh_s2uh6YQeg0KDSpKLJDFN0L-TfQDdV7vPS3wK99tiWfGN_4O5206cfzW5_oUaYxBqgWHhCcnXpkNv9VaNI03M6Tp7gY2MMrwfrQgNqPKkVRZr-GlK-wclH6zWyOrXSs_uyHFVphfyZQAMk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6k4wSgf_fjfaQTK1byoZpWmTzbiagkp1Fgc0QmigtTAS_fnaBrszdafibs7sWF69QdR1k9ZT90o-RyMGyB37lilPQ2xPpqpuvDgJV-5WQVp_zUzdcysenbqoRMALWMgZdBq4cVlUEZ1rzQytAa_fncJIicNk1agIpQe3u0m3U1djlIbP3D23x0rQgh1kk_GuJCmOiEgWYvkT3SJQuaq5vlcNp0bwzg8BGx5GpVqE_wBoJLMXQGnU8FgClG5_wHiVEl2pI8ksbE7yu0LndCKsKHCYvH39JMdyXyq4Oz4sz21Gs8W-lD2MjvrEz_O7Xp9E1uczcwlejJIk_rshijewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0MEY7FMhJa2_mYHHeZ7IR4YSe4aoQGeVzsPluaaHuUHgeP4mkbZC0NJM1vmM_jOzAl8HHY5yyBRWbrtXitl08pys49FaYvn48q2jnv6Xe5hx1E6gQiTAJHbS3kkh9_Bc033dpp4BJjZ_XgOHY07kUnjKhz4z5SBlR-YksAfft2w1W1lCrfGXy6yXjY3rk6qmpPkdnLquFcvfa0KedPBkLX2N8P9eHEfJyk-A_YE-PlEoJcP_s6cFS2Bev3L9iw37rXP3vXr181IHgWXf5w-_ARltH1yZ0kxiBVidrFf_hOTieICuIY4Xm1m4YuCRGhEjmNiTiiUto4BEiKEEHZjyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6eYnA9NtaTgeFop0tsTXNfs3y4Z8fr4dv44dvL_rITG3PGIxwuQbWLJR6Ftr4cmiOHy-Cdmg0FQhXpIuuVEcVYjz10rxPagI4Tx0isvHSAghMHZ7PY2XvgNwdhQ8jcnGtMFahffnLs7F4vyYo3df0CjX2NlFjsVy70zbEVgcq0o6m8XMo3JeCX_OFKdjHiWYuL_cFQ4c4XGzqvqIOFU3W5C1JeFBWC5JrUmgL6MA9mmuTQn4MnxJqmFczIoQBFoG5xIZeXduRokD9QYaiLdfb3pxEaKOJIKkyoz7ggG__oCV3sNLJsObA_PyYCi3FHOpeJl09HJ8FajoRUZKD2JAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=WLnVyOGHzsEhgyLUosbMnOXFc8oYZDbnqsmNwov81UsNHLYK9Z8IIv32p0cbgyeBb937YW_MyK7aL_zcCcMObcUwrGCpIY_P9cHtP_AfcUyeMyWaU3Ly3AND-D19YK0XCFNIfDxlWnq0q8Eh5iK7dSQk_qxJdTOfgh7zwbEZFzcojhFuBMKBkIs-pu_6txBdY8pQadspRnsL2ODqRO-XvUuat1WNq6pfltdXLWLytGWbmmOWSZU9fTVWkGffWLeYxcZI3yG9lEOFNG5kLXqZ5v_qVF15h88aoCQ5m1-xeIBM6hgQkhZklZKRO6CPI5coc6ns-KCli-nM_j1FF1N5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=WLnVyOGHzsEhgyLUosbMnOXFc8oYZDbnqsmNwov81UsNHLYK9Z8IIv32p0cbgyeBb937YW_MyK7aL_zcCcMObcUwrGCpIY_P9cHtP_AfcUyeMyWaU3Ly3AND-D19YK0XCFNIfDxlWnq0q8Eh5iK7dSQk_qxJdTOfgh7zwbEZFzcojhFuBMKBkIs-pu_6txBdY8pQadspRnsL2ODqRO-XvUuat1WNq6pfltdXLWLytGWbmmOWSZU9fTVWkGffWLeYxcZI3yG9lEOFNG5kLXqZ5v_qVF15h88aoCQ5m1-xeIBM6hgQkhZklZKRO6CPI5coc6ns-KCli-nM_j1FF1N5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=I5irjwE45lHFBmed67I5HbrY_rVXPwpIEivPGM4AcbzCsEHfnHpS6_PCM3IV2xgQzDhVHG_Kbzmht_7-0h_KgshxmLG16CvKGQmGTWoW-P9eDqh3F92VOwZQweNLspwBdXt1cGqlI-QRIrcNCXZUVeiEydcP3SFwAO-tAeS0GOAnGF4O4MSAbEtVM_KbgYNHp6Exb9SpW3klsPicuQwbQiNPBFcgGIt8EC3XbCFNmq7-TVySWNY8ahZSnRlBWSJ9_izWkCB_wvXNd0iGHZ15BLxXN-qAfefHCE1RsSSx9mCIaVUcxRM-F_D_lXesIcPtX4jt0JHJ3R8baJaw_2mX_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=I5irjwE45lHFBmed67I5HbrY_rVXPwpIEivPGM4AcbzCsEHfnHpS6_PCM3IV2xgQzDhVHG_Kbzmht_7-0h_KgshxmLG16CvKGQmGTWoW-P9eDqh3F92VOwZQweNLspwBdXt1cGqlI-QRIrcNCXZUVeiEydcP3SFwAO-tAeS0GOAnGF4O4MSAbEtVM_KbgYNHp6Exb9SpW3klsPicuQwbQiNPBFcgGIt8EC3XbCFNmq7-TVySWNY8ahZSnRlBWSJ9_izWkCB_wvXNd0iGHZ15BLxXN-qAfefHCE1RsSSx9mCIaVUcxRM-F_D_lXesIcPtX4jt0JHJ3R8baJaw_2mX_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXtddq2tsYEB9j1DRxbciPJy-22D7vd2pzjz88vnbI6BluaIugkO-BPa9ANh8Cf3OrTlXa7apFyGGeRnkqWxvirQ63bmyquRZ6TkLxGteIPpmZcxt1mWJ3RspH_8ay-yu8Vi2fNTCjnKtRdRbthrRFmtHeU_XozJtKcA2GGc2vhZsrUIIa0TnrKtUjWfIiHUd36h1CR0XScsrFd0rbFhI3BLyyRWx859vl6p3aGa0C8X3L8KK2dAlPV4Q5R-h89mbm8YfWiYHUx9P8Oh2kr-VCL_z7peFFOgscpgvFZ9tKsbMgNtvrK31Pkg2ZskZUXe-N_iV6VePALA92rfXs9cYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjvdO2KcxKGYH6HldTXakHrYXApgVMXwcMBMlUkvEQfLDqLizhOco4E_CEmYTg_6S6C586eKnGj8XcyDx74JYmnZs_rYmgr0nRtnItn0fxPdT1W9vf0iSAoFJTNphGA3Wh5mZ7t6v729Div5nb-C8j8ZEoL6huX1WfFWIL17OgKC-Vq3u7u3ilCHnA9FKj9Y2NDA5MjbIE_HWjTWjRNMR3Aw_O0E4xpLv8ekpKrH29qF6i7_ApGNL6CKBHu-dr4Y4lWhZHp7zuwoAH1Lnt91mOby70GaxwWImSaEOI37AbREBzyKvpZxuvJ_F4LNnFk_AjxIWwMp9MVtwRg7eA0yDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=kD5Mzvsxg41w1Quu-DRtyPaJMuRqKJgWm0DGkC6URBqPxhBIG5AUzkvC0kTyiMxzswxPbkrPTWb9_-glfsABSqN3QjtWtoHGfj3MqNp86I3iVw70GJnSUK1oyTWSG90n8cp9Jfh8YS1oirm9xta_veIRgwZmEQyJkoFM1Sn_lmH8GZJZ9qVYq7pt-8ya2FQYlg_m17dL6DSVtaUP6mvuJQaE1njwoRBDYg9VR1GxCDlbN9uebNGsWv9KUwGQ-_Dog917ttP1ZkwFqTcHyBoAA_DEt0oIyyNxGkLPjIVDCbiekr0k_FfwucQm7DQmBFkHZHOfXx75tIpT72rDBvfzsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=kD5Mzvsxg41w1Quu-DRtyPaJMuRqKJgWm0DGkC6URBqPxhBIG5AUzkvC0kTyiMxzswxPbkrPTWb9_-glfsABSqN3QjtWtoHGfj3MqNp86I3iVw70GJnSUK1oyTWSG90n8cp9Jfh8YS1oirm9xta_veIRgwZmEQyJkoFM1Sn_lmH8GZJZ9qVYq7pt-8ya2FQYlg_m17dL6DSVtaUP6mvuJQaE1njwoRBDYg9VR1GxCDlbN9uebNGsWv9KUwGQ-_Dog917ttP1ZkwFqTcHyBoAA_DEt0oIyyNxGkLPjIVDCbiekr0k_FfwucQm7DQmBFkHZHOfXx75tIpT72rDBvfzsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=H4HI0VsVK04gVoSxoGANRvGSZ5OqprDVjXPUQRJSacfE46FdR7Ukle_sQ1VS7dfqD5yNeN3R9YnPTykHmjISHjp2c2POW2wZEBd88pyDBWZVeR46G2J86HVReuztOrzmBMQa1m8PE_WjT3S1dbpDG7ikcIBdttNglTCxckUJpHt1fuAva-NCh-fz237Vf7LK59lE5s3Eg5XeyopQnwhUdpw7JK-4tCZiBdkO2lqs3sNL7NgRCJzvg5lZUyFRM1SswcNidvpvrGyXXrd3bg4jM2F9Kon1fgWdjgahw03eL5pNyG3sKxqvDs13WinNLjczTim3b-sm6aRTZAylT0GASg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=H4HI0VsVK04gVoSxoGANRvGSZ5OqprDVjXPUQRJSacfE46FdR7Ukle_sQ1VS7dfqD5yNeN3R9YnPTykHmjISHjp2c2POW2wZEBd88pyDBWZVeR46G2J86HVReuztOrzmBMQa1m8PE_WjT3S1dbpDG7ikcIBdttNglTCxckUJpHt1fuAva-NCh-fz237Vf7LK59lE5s3Eg5XeyopQnwhUdpw7JK-4tCZiBdkO2lqs3sNL7NgRCJzvg5lZUyFRM1SswcNidvpvrGyXXrd3bg4jM2F9Kon1fgWdjgahw03eL5pNyG3sKxqvDs13WinNLjczTim3b-sm6aRTZAylT0GASg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYDZsWDxoxMxGKqq2Dt78pscx4qqYJVHJWOKloTtgoFa6eJAQ7ExUP2yVC4xM1vHunq0xvJ483ABYTRmrPmJRqVGfQTWdvq4O21WCM5AtFj5t-8XvRAQP-0WQaZyaBLtKfRg_DJzTfwa8z8-LMS5nLbMdVGpgvvgI-eNFCQ4VJVuH2P1ToQLipmD5q5pHKYXYc_6qVRxN3m_zUzsnbQCzjVwyKyTTuV1KZrSdjhiGTVlUYEXWQnHYegk1WfALmn7foIua3ZHEx7J2tHkDgmLKWr7Kl87SVo-o1WgbV1t7ATXESWemIujFDb8KnmtohcyKcLQjGR1yLT55c6Zrjd7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUNVVE9ujOGUC8HUm-hlVnoohSgDWV4tv03_uuRQciJGzdsqJsC2sSHuMxrLA_KBGM1WV8Ckwrj6pXVuP5ckL34_sa2CRpoH6y6cHC3NSBY1O5BNvsI3RDIzcqlfVor72MN1px7nI6OVuYUVLoQu4K5OaJkXlQnkD0fCbORYAFygr9REnQLDK4hCgfKDUfFtqIZJ13WeYy4O5mNIe8239IbgK9rbc6Z32XIyNNS7X54UFVPFhLeOCQNIywtW4jcMWX7G0tEwFxVrWC_KW0OzHK3ux8D8ZshVoHKSfuxmiIoGSBY6i7I7z1MuC_kgiQoAqt8QwFgq2-uAgZwvILBzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFNYNxTOaLeetTc-lv9oic0YqF63dlNZpD43nXj8_-PCaR4R7_0xFz5gtyijQ0t6NsgcbmgnHQNdGx8D637-EUeYNpaE9C1EMPtpq22KiyQiel8bVPqvx9wW1YcKkVjZTYz7x9DHMAaq8QZy_ErFgYIqloe3qIpfuAnEWQO4WedkMpZN8rNwlHprcStsJCc-MjrpstDDUZO7ydEInlQ3PTm8FQGa-IYeX4q3nDdzBkN2DFdyG3uiUoTzNlzPYKt9q_uGdJ60kUXDoYNS3bD-WjCTZzeccsLiqx07MMQJhElCko0MtkpepglXdDKmUOrPWhhIeELUDFsb1BmSYR7Ihw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=GzA6vMtAT48oA3o1_ksY7hZq4F4dUyfgDx9Y5Hl4OKIPQFuMYQZxEjplbDni91JICZ3Lp1jSD2pBO0Lse6o0xwUjSwOMoGHqIRP-k1_yT10gKoXh8t6pffb_LbUyoWrqI8JF6s2CHGfL7oIqgohx5ZIHaa9HnGvAqW5R1zc7z3l7xUyp6sqNynXydR-1XH8FHNutrM1m9LJYW7zXKR6H9vHeIAIP9cnVjygyNOYER0xJRXACIDgkgU4jrnOwbi2mtHyDvuZbEQwwWIOVJ16_6d3Sv6l6-rvsZC_88jtyJhvFJq7e8itA0r8Vq7kVnEwBsiqHpMNFX4uPH0-qY5vvRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=GzA6vMtAT48oA3o1_ksY7hZq4F4dUyfgDx9Y5Hl4OKIPQFuMYQZxEjplbDni91JICZ3Lp1jSD2pBO0Lse6o0xwUjSwOMoGHqIRP-k1_yT10gKoXh8t6pffb_LbUyoWrqI8JF6s2CHGfL7oIqgohx5ZIHaa9HnGvAqW5R1zc7z3l7xUyp6sqNynXydR-1XH8FHNutrM1m9LJYW7zXKR6H9vHeIAIP9cnVjygyNOYER0xJRXACIDgkgU4jrnOwbi2mtHyDvuZbEQwwWIOVJ16_6d3Sv6l6-rvsZC_88jtyJhvFJq7e8itA0r8Vq7kVnEwBsiqHpMNFX4uPH0-qY5vvRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF2wstxaSwXfWtWlZ_FVJOfKEIUKaa3kyat89l40gCbVgNUC30vflaAF87S3_M5lLTb-xK_GKnK_z2w7bD4GeoPi5wO6Pa9I5tTyeMPAESJBpXOK0GMfCWaQwQgVqo5FYnG0TgEMAFBcY7ou-euNhOPrm0oXRAIpmfrj7CZwUD7LoddlHh7UsDHY91xxKFtfLSiNrkW1bNfNbe74F7jNZC-Oq0SxXjtGLLw2ZRTzqyzgGcsP20tHm6tjslVm0LZyFOVe_sUEQkhjSpXtIBahlkH8j4bwFDHAk3kgXUSo-GrSJ2WyKGFlbEsup48nhB1ul4ROSnyqe3pmXppzBsl1mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYD7e5BvOCuP0GZHvKAw-9wMPsSQ0NHNQv4YG0cphwrBFuqB2nt1gMPOekX2uC55UxQBNEL543GzcLk90yMjN5KPcOBZruoifvmA-r_IaHPxF9MW9j7fonQW39WZ2SNejTjMSX3CqLpctFecJVkQYfWw50Wswp8xfbs2AJwE78P4h-KCNaJJNfCnUytrGGos3TTlqH6idd6QpoW7nwAoJXIx2joH5LYhGS_YqUpyHALHPVvl95ikRF3caUiDC0VYUxvXyFXrV40hCYlHuS8btV-mWHwQxsF6MBODPCkyDt2DxdL_zA9-Fi_sps4es5ZjPEQ3nZLz_Pp48ESAgskNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt9eJGiaPe118Jz3gme2bCT-pvPTTJbe74qSwsapsKzTqoICM7hKV15YGrehuVxKV2emK5uYvdKb83xJkFM8TEOgOlJE1bvWPylgiym7SX--HJhNFwQb3EM6uPU-9r4s2f-C3m-26ZwouPq2D9upDAR4ZP2Id-5_TbFa9ieRUlB7Sliy3nsTTS-XFb6-Vt2h5YdUziWUyhQa-FJRTu_ERitPdSaxyb2SqkrbZuO0qSbXQF8FgVjlimk7dGerBya6JBD1g7m3zpQ97VB4u1xnK9YseLeE2SOUByxd8ePrHgD4rkHJ7g9ayAIIFBXiKphe_wSvh8K2PwhZYVpBg5UAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_MBsQZh4gkuqpGN_LJEegAJhfhiSidTQ8PSiOPvpomWcTrGS7JWRfm91VNXM3aE6PEHEita_DJSF3suNpvj2M_hLYJ_o-3e4mZDNPDEoA2LeLDTOuclMsrTZfSbVkSpEmYB_4fA9RIMKGr9krLIiaw00REhkBzXxGUCznuM_OWM8RXbipBJEqeS46gHsIS-AT9X1pdjkJThI014RFOBB-Lxvl3rlHQrdquSs1llFF3hXGoG1QQKPQk71TAB08TB-99nCr1awG6QTs1dXFrH31n6HaP3u0fYO2qlFPN4y_7YGI2lh4MPCtGxWom6DYPZKpoj9sORhVIAx30ZwoO_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=hyjVTuDNwyXlp_BcEAdA2UcdaEsP_Jr1yg3GZxz4GLUBGzILgUuiV4u7gtlKMBhgJ4hh02LCR5EZHYgYtL_NzNBHDJB58j0HGAwkVc7zyB9tJuWWtEzyF3T4WZDF5XleP7S3CodA6qObHCz9SOv-Qe-SEy0NxMkp65zqxWIvrUPFztkU5OwG8oNrWynQJPad8WnKj7tiBfghYJbQAgNgf8fQoVgmuHnzLhEXoiZnkwmKVuGkPdakzV_MBeXY3xCIg7TKIc7tBixVMDaD_GJk7_30Z5NW3JHydjk4J2qnBhhI2JV7eoI5UmNZgDmGWJ3vORKqMfYAYOJFLND7LPjjFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=hyjVTuDNwyXlp_BcEAdA2UcdaEsP_Jr1yg3GZxz4GLUBGzILgUuiV4u7gtlKMBhgJ4hh02LCR5EZHYgYtL_NzNBHDJB58j0HGAwkVc7zyB9tJuWWtEzyF3T4WZDF5XleP7S3CodA6qObHCz9SOv-Qe-SEy0NxMkp65zqxWIvrUPFztkU5OwG8oNrWynQJPad8WnKj7tiBfghYJbQAgNgf8fQoVgmuHnzLhEXoiZnkwmKVuGkPdakzV_MBeXY3xCIg7TKIc7tBixVMDaD_GJk7_30Z5NW3JHydjk4J2qnBhhI2JV7eoI5UmNZgDmGWJ3vORKqMfYAYOJFLND7LPjjFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHLXhJQxZZcUteQ9g1S8Y3IeyxvcbLP8EPIHkHWscGPDIdJ5sO9wJzZkZrTg5bEOXvKjBVnp8cF-o6IxdueFv0k8L3xKlFgHajZH9DvaBs3DalDMLL5JInsxq5j842WhQC6S0Q_Hd4DaBPgP0hj5BG9_BVyOrX95y5v--8rej0pMdqPt1vXX1mH2-YpEZsgPdo-ojnZJjrqdeWR1DiQU39gNumjvuyTA0AHFss2XQ-NlMNGLo3l6XXdCtd0QyFVNd9Aj86m3kI1gTMR1n2idBn87rm_mwClIE2x1uVHusrnp9rfFlH-MciEP-jW0MkOUeTbrRueVrJpZhnPQNkFpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4JPcNiQ5lgCPGKvSqE7k_sPgz_JJCEK5FkA__lT4yTlIKpslMLpvO7mjBfBRpU39NdN98Q_Bq1__gqnY-VCdctam-Jw1t2y6fI9puZfr148gM1WBPY2NVaLOdBgGcIjoThGLxHNPwTmwWZ0ZTy-e09D7fKhKsD0Sqy41LzyG2cHK6Ip9JQtMLwAc-770WtJP-MzG1YBJ-R7dXGR0pI4gb-uWbY075A-mG-g5U25LwwSR40kOuO4PRMXA3AxgMjsKx3x0YU1A_34ujuuHI7m_IRPC6nqJIh2y4IlZEuR8ay3CTDT8xrdvN_lP9KQ0SNvDoTau1lkjrSwNNPAe8GmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgdLVpBKewAxgl7N8vTVUb1aidnrhBoDRACPSlPaZ2clM7BiYqFeDUaBYgRdIAvjPf5Z3byv83jRlZ2Lbsvd975D9J5Jm0IJT93LWFHdSQO4Km96csfyZW9p3HE6LVeX8WL-48KGqW-dq_gsqi5VLBe9Le5UccBg_LlELxSf4HIbiMb5_hyKQsyyCawra3ih4prOTbRyzRnWoA4ozAdqR1IqBb9h5QXPlKqpdt2VC-rl8NF9cTkeNbVw1jkmnoUQVy4n7tr-Fji660cEOFg6xqO8BZpdeuGNQhNSA6UJa-Mmor1Qsk4NP5qd8bpBeG_-DB8SJD58UwbCDBQeoRR92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=q4IaTbtIsBgvxFAMMFga3z1X8shuLM7nYpF-UcEVMbUBlS5SN086W7Wj8kZ5OYkY6r1P2XU3gx9GjGNyyheVK-n_wx40qhyZpBwcGrdqrabIEsd7nAcZSahkkf3G5Ptf6VAfUv95pC1f679yXq9Yh10cKv2s1eC_uj2CejlrKurXvmqeEAbQ0EzQcfHfgKYjpmpPXlOSU3b3Ga5hPwGqAYFkJPDPT24PrPmDbLoPMffi0rdNiKLGTTJp3g2GoLqH8LGyXOJ4oDTbXWmK6NCB1w2aKNfkn-LQlHPLiv_gxkSQVA7qIJZh_MEGfMdL3QRVZeC4GuuMp9R4k1MC9B8Uzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=q4IaTbtIsBgvxFAMMFga3z1X8shuLM7nYpF-UcEVMbUBlS5SN086W7Wj8kZ5OYkY6r1P2XU3gx9GjGNyyheVK-n_wx40qhyZpBwcGrdqrabIEsd7nAcZSahkkf3G5Ptf6VAfUv95pC1f679yXq9Yh10cKv2s1eC_uj2CejlrKurXvmqeEAbQ0EzQcfHfgKYjpmpPXlOSU3b3Ga5hPwGqAYFkJPDPT24PrPmDbLoPMffi0rdNiKLGTTJp3g2GoLqH8LGyXOJ4oDTbXWmK6NCB1w2aKNfkn-LQlHPLiv_gxkSQVA7qIJZh_MEGfMdL3QRVZeC4GuuMp9R4k1MC9B8Uzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=j-4YZeP4OjH_T0rNwjy-j6c3ObALanXFxYGjTn-YLTYwJ_ArFc6z6TIgwfNeJhm3HagsN6UnvRhR-wl81r3FdsRQe-3UC44cYAtHtGQzR8rRdIcTIcCldCq_gQ-UMgxdw711_K3IBzO3TU_JalvxKLsOetv2Ze30GKrReZPZFCB4_4BKNwDUNJQui3-Oy3hBtZuqpqX3p3l2Aj64mJVFThcTns5HlNfZZ9qWypf9QP8Zk6EOEhA_GsQB7YLdE5klSDd8iNGZ8orrjmXDp8I8ZQkrRYZfnWfhrZDfmt1pzahygIKJGpSTDC7o0QizmHcBivyozHK3GSfkuBRTVKIWfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=j-4YZeP4OjH_T0rNwjy-j6c3ObALanXFxYGjTn-YLTYwJ_ArFc6z6TIgwfNeJhm3HagsN6UnvRhR-wl81r3FdsRQe-3UC44cYAtHtGQzR8rRdIcTIcCldCq_gQ-UMgxdw711_K3IBzO3TU_JalvxKLsOetv2Ze30GKrReZPZFCB4_4BKNwDUNJQui3-Oy3hBtZuqpqX3p3l2Aj64mJVFThcTns5HlNfZZ9qWypf9QP8Zk6EOEhA_GsQB7YLdE5klSDd8iNGZ8orrjmXDp8I8ZQkrRYZfnWfhrZDfmt1pzahygIKJGpSTDC7o0QizmHcBivyozHK3GSfkuBRTVKIWfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=KOiwTD3zrmSNgPjsNgWuYz_BSEgtvEO8OLjGj5PyvuzdzoaYsr5o51ujE3nm6uMqg1RNcBLODtjTCxJV-UPFG-Uf56g1BAPJ--1t39hyL605vbVoUXgtm61006bbTNp8jy4e1G7mIEFHNvQ-Sxo-HaDR9cJJdcXMVAmbnyJ3h3EGXhtL_FPgM3fBA7YXelw_Z6MBQMLDDA-DJxWmis-H9iMfr9cSW_GbjHyEYpjBVBZbBfKTXGAnoaqH-KnAsBAicoo9mJYCaPZg58LymwddVRgAlJi2D5RIgf1as5WUXCIQQ-fyvvDIJSCST_JZulbLioA-xqyAhiS0K5fflQaSPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=KOiwTD3zrmSNgPjsNgWuYz_BSEgtvEO8OLjGj5PyvuzdzoaYsr5o51ujE3nm6uMqg1RNcBLODtjTCxJV-UPFG-Uf56g1BAPJ--1t39hyL605vbVoUXgtm61006bbTNp8jy4e1G7mIEFHNvQ-Sxo-HaDR9cJJdcXMVAmbnyJ3h3EGXhtL_FPgM3fBA7YXelw_Z6MBQMLDDA-DJxWmis-H9iMfr9cSW_GbjHyEYpjBVBZbBfKTXGAnoaqH-KnAsBAicoo9mJYCaPZg58LymwddVRgAlJi2D5RIgf1as5WUXCIQQ-fyvvDIJSCST_JZulbLioA-xqyAhiS0K5fflQaSPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giYFD15ZbgsZaHIgXcuHGDT2Jps5zzlvD6IwWESEfVZx_9be9ubdmvJ6lWUxOw1Y6POBTBKPrecVuZ9jjs6W0HHXYQT_62cTu4ykqoYpwhpOt60szxVOfoKKpGrzDGkNGskgj2sdx83GqEtzmnpoF35PGNfovH6Kh4M2mUTVEmt5ihS8TOG5Q_u7aXtnJA_EyDMnga2dsgeeFggiGK1ynE5WZpMNQQ5cRG9tY2V1rH1C3aK0yVfLstmka4LIid8NhU5Gssf_1-LRkY1ifMQy4D72J-YN3ZhbClvqxKp0Ca_MaWP6VBeLntOlvmTA-IyyUiqGrpyi58D2uhsO4_ylCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hT47fYX3inf0yhEn9fiYEG1mfX6tIEzUPhxb4KVo0ELwVAElaDog4I_8L2CGWzzXc0xjgviOzNtySAmgdAkatduOZdfdb2uddTQPxTCXbCNyeqqk6RQ4Ie9R2D-rWpy78pxPCpYpqf4t16vtoU2PfndqS26vHPI3MFxeKNAhWRZJe9FeY2OOhzNJu5rmyslqJBSd-fvCiFWy69hPS2npG3II3IOugzUjvXNpkNeW-vP0NLi8M0UdKhcidFNWkAL61uhLGggDkNDYqqng0FlPQvGlaIoRBGk98WFKkm41LqXOGq3deDffbcLDtioIkqG7GOTg7PaXyVBr25b1u3z99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_eFIfGIGiKzS46czVUjOqcVXSblnaYbVt85H1G0e6D3p-1fIJny9cBNwIei09gllHfezRCcyswp9f_TiMPCTjukGOQYFAFM2BxEkrWB0a9jZC4rB6IEa4fiXDYknk2pab6o6sCXeotKNtL2UNGKaLK-2UNgRN_1LO0ZB7mNPh4egkwBh1o8TMXrjXnjsKeHlVSP1FUU3SDmvwJBxfNUKVYAiV1BNSmWc0IJRWJWwflgOideWM0UovpSieabFlOUVYHh_pKyiTAkSXdVO-cDz9x1gGWgAmrwYsWXKHZtwGxhIjCqmpplwmfbKyi_yr6FAlBaSVx6DpW7t_ArDpTISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aoDaMso0qxIODujWIbpb-ZItA_vCCLFoD-dKVmJ_hUeAclu1oow4KyEimxY-FLZMaOphcwJcQaworw1B3H0-EWzKiSh0vMkRNzfRWc3gKxAeTJPP40Uz3yG-Udbl7tRyEJtLK5h27JfB4liHOa1cpX7cIGTF9TuePEZVqDboY8EiHZK7U1iIz9IfgPqIZ1pJO2HR8DzZU86uBGy5umrYKXe0giID7KUG6ubvig5EtywL0GrKMReZtu4ImKd6eIua1HKTRoVNlGlmY0C9-HBq7snEXvNd7lnVQrWMqGNf9g__js1h8XcG0hkIrzij2iQsF6dPJ67cUjToL7Hyvde9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n74c5oGfEsBCJspWPUTm01cdvtg8X_221ApxHcug2s5IFbFFzKwPnzlWqJyHggmIqWhLrc7DkRNG8eFsMtPJ_58i1ebmQ8QJbjSCb66TMZPz1EQ9tkceYQxgbeRjA6rB8K2bIEXMK_vVlXeB8Q1RMPWLnhD3DsJacRnwCrmVQjEIp4CvTf70-luxJaLVptbWwKjramsjpfxJSqHsvuBWnO5NpbvTGLlEUBgIuRBKY44EyqoFIRdhF0Fk9YINzXf7pA382xdQmFB_Vw0xRJXRXwX4bWR0rG69lyLOOv_Dt7YG30hlC6N6u7UR9pS0OzZpAJ5zdmYBUVzwnYQtxupk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xv9w7DFmxzub3RwpAeZKIIBjkwtat2kmM4g-l3hLkBXoGYc-5afj0zB5krrrRLkYMYco8EC2w84qMhSZa7naJg5qFZ7RckmH4QGmRn1BrFrHOT4-h9WKywA0BJ9MVmT9K4tw1NR80x6n9r5QZ_sN66VjGzg34NQgRHGsV4et7LEUqJwIxk01dQNGcXeqYEn1w_ywe_RWWor-IjprS-uljJR1cBYizIt8DNM83LAQpqM_UslDg2rPiQtyy-rJOzYPK887kpld1h4E0J-3Mat_p-PtdlwCWqrqa6VMWn-0KD8w63Fje-2vWvcvDOtaTO-bjg0WVmNuulsEiDmlDzFuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRUVzcAZj41lWY8_m6EOm2GVNP4W_QK4j58duG46guyBUMuzZTZ4nCqICicY2ZmoajelodK3cOE2SLJFhmFATRb_bcch8O7buneJEveyYT3D1ydRVFPqJvNctRT-Bs6vEdLlvsVTAZ-gNojz_4En9PSZtQ1jzbsKKNQpZGeuOz_RlAYd7LsxBIPTd2R4zXRD5DjedxnoH7jRFS1EYUOmt2NUvsGBE8LQ5tfECUoncZ02qDGHrVgQM9dLGOSxcYTSvjKIDMAKG0aG6NpTsJuZsZOHKM3Y2N02DRXMDr0mBbfuzXqTioZV_FtTES7VCK1at51846IQiqjznjHZxqBo-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
