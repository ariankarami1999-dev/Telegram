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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 15:58:22</div>
<hr>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=nIYYyuwuGqilQdKhS2iqJtCPyGzP1pSifxiIWIYY8jRh8YlBVYsTPhDo4Ui3yH1tkNMHvTnUP8eGro55Qfh2OtcXAAExTQ0Wwh53iu0pXgW1hhsoD8qInymMZiDsykeNfPZ9VkIyFFk2bLs-wqps94-ZeqKqxj_4IxbeElMrGF_yq72Mt17FoM8BeD_bg9sfoV04gG_E1a9ucN0XvYKU7lNTp_nGunBcnOSvJkk2isO_nv3iqo0a_t1dDa0ioJv5QevRqYc-hDr0b2eMsKluollpuvv29hYjzpLPtzd7kuPcRvdrdF88eY6KPG7whzTZCNrjX5wfPj63ceNC-WiKTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=nIYYyuwuGqilQdKhS2iqJtCPyGzP1pSifxiIWIYY8jRh8YlBVYsTPhDo4Ui3yH1tkNMHvTnUP8eGro55Qfh2OtcXAAExTQ0Wwh53iu0pXgW1hhsoD8qInymMZiDsykeNfPZ9VkIyFFk2bLs-wqps94-ZeqKqxj_4IxbeElMrGF_yq72Mt17FoM8BeD_bg9sfoV04gG_E1a9ucN0XvYKU7lNTp_nGunBcnOSvJkk2isO_nv3iqo0a_t1dDa0ioJv5QevRqYc-hDr0b2eMsKluollpuvv29hYjzpLPtzd7kuPcRvdrdF88eY6KPG7whzTZCNrjX5wfPj63ceNC-WiKTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPC0_tFl3pbMOow3W4bWk5VLuLoGY6TM0wFhOo1zV30sUUIE2nxt8F0Qs8ZVKN3E9FEqYAX6_2EaMrCNnQZ47ytAZAcJBPiXKPVowGdjzDSeGbz5QtxvWFkumSwOL6q92qbYNh7IYjcJR96LSDjBGnRU5jetamb7s5hEu8s6jLvpolYBz8semwBTaXFL0kte8jHkQK4MLV17B428zZRq58x_0PqCSz10ZSRmV6yrCIQmvKevm2IEKwFWS_0nbJiZmhoakOqvtPVQjnzXq6aZoKLRZfdbpxBU8ZiUcim4F_fzWQ0vMzCgdFBBc1kVsztPDzJwCh_G9lvtG0ZhMb8cxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYaHsv2IVNm9nRk61lBOzxSKSanQRBiwJFHs3jJnL973EvD0q0z46Ad4867yHg2afmhhcyv_lMn3EWXovOLzkOBm-bdFvzxK-3lDeSDdS9OXhVyVHuoQPATDHEzWluZIjyEuQkXreKuYBpD9Qbb5xw7_3Rvn5jCiUSadDkhrhmto-frAOHhHpyBLGn8c8rNRVl9bJBUjCt9i0Pt5PZg1JG9UR2q5dgzESslqL7iToavuXjG1IIcBFzVlkLh6AaUPWza2jloRtZa9SGjqlZ6z-kjCpy27jYbsLX-h0o3f1hZSPyzA778k5LSET7KOdHuMuLt7DGAz16mQxURs2nzmWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwtalJuI4ISK7IQV7YrAvbHJj4aZpfjdhF9SZnPXUenA8e3JE6VYZ_JgQGbOAe1JK-AzhTyC-u6Ps8BU6bRa-JO1s_WMStSN1Uv7k0F67k970czKZ1Tm98V19lLVw9QRv5st6M_c0-tNi6nh_ibfKOrsdtxJFOGxW6YmxiBJuEa8oozwQrqUZsXwLC1dqMU4371nMe5z6ufR01qgVhDsgJxFeMnRBMvBYgjtLw8w02tcuhsPJbTHlZg0f6pPtYeWjGsN6844T1At9MdsN4Y8i-AwutsrC942gOzp7EnQDrtgr47tQv422sdIF6mVPhHsfqVYxNfFEM0gpUgqxz3tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkPlS5eGMm6Yc2WSpo-utRTSYJ8NveD-Uz_xnXbrQ5OdIOrxaejh4CRYvlbHJijvdWWxn98GV4MadzaLXfnGpTa-prm-wjofhmQjv_pwdLPBS0uIL-6-w4udEWjpNHmXeDi2_W1wBepQswCNwdXVRXlxvmP319q2M8DCnIeZ5381YrzMrIESYlV-3pBN2MSCKLtffFE8GFvQB3MqEiW-XV4Ebomn1ZZP4GBetgeNMsJ4tKrVoPuU9I47u72Deo-xMW5d4YXMiZLm06cBEcoJHFyVGFg_YnWkrtkIbx37p-kmdDJhVdOdc7oOEoqSR5GFelXpdoqukKaWxPAmtAz5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKj_RbNEOApa6XNKCrrK75Gw5e6ZW1EVOpYxKDb6Ux3P_MCLKBpD8crp4tmqBODk0DBVG6X5CrJuMPlligOXIjIUDciCZGi5wMBIiN2oXrD1eezOH5TBeUTDaMamIE-US9vzUSJyExD8-cyxZsXsLI6aDalTb_jzM0fSw69jzDZjlCnxH6UHvUOi743zHiMyPx6y1y5rDgLXs3Yy_uQ3kvKpGXbUPfO9YJEfprhBXxV6a-O611YvPpu5F6USuis8KmI1CYNg5iGsKCT4vqfOx-TJlWFkGqdpVu0aQPksQIUXm1P07_EdDd9XUgLJiYadFvxxCMeLZ-Tp4jpKYEDnDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmKIYoON7V6Ue4IkHr6qG7AVT4tY2Ozky8KeIfbSAqpNh62uYZwH7vemVUT15BNcjb5AjtcsMNXTKvPU2ZJITBXwE9bjHioiK5MfFCLo6F2SnKxt7b5upzfJovKZEPAMhR87YZsoUiR2E_9jwY3KPlTr0QTsS7OpNAeU3V35XqFjIbD3lABISNE4dW9TLcqxnw05fEaDX-tk0S9AkWzHB0j5KywpFhMFNJ4Jn70AMEQCiayYtpFvPCSZUY9osiK66PyhE51ayLuFt8DcGu_IMvJaiBvArbD-RBLN6n9zuJpe1tyjaK7wmCdj0cAnPeypBDf7IKLvd3WVngyZq6Xn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=CGsBezb_kAcCvvIbu3c8ORkvDGf8smzEdU_VVT_TjSLJxxcAAPp1lmm_73MDj13lpt53fG7X9iGyMGB1PsMcQLpupLmf5DrilMcW2GSiuZCPCKfDAYubJrOOX5-lGEWQ_lPQGj_Z7RnQ5v0b8zcr6mW6uHRUji4ANCF3cx6qku8f-YvfFVsfwaAETLKEOXBC0V7b3fF8ZEs5O5b5L0pubu_8VMV6hWvBep58Z96fVX13u-iprdfcuF23fzwt8ir0l2esRbv66E9yIPt5clRxOqTaEr6K5ip-KfgAS_kpXaOm2lfaOq4Fvf4DEAUkf6MOoTeznqvEFx-5KeWi6lfn6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=CGsBezb_kAcCvvIbu3c8ORkvDGf8smzEdU_VVT_TjSLJxxcAAPp1lmm_73MDj13lpt53fG7X9iGyMGB1PsMcQLpupLmf5DrilMcW2GSiuZCPCKfDAYubJrOOX5-lGEWQ_lPQGj_Z7RnQ5v0b8zcr6mW6uHRUji4ANCF3cx6qku8f-YvfFVsfwaAETLKEOXBC0V7b3fF8ZEs5O5b5L0pubu_8VMV6hWvBep58Z96fVX13u-iprdfcuF23fzwt8ir0l2esRbv66E9yIPt5clRxOqTaEr6K5ip-KfgAS_kpXaOm2lfaOq4Fvf4DEAUkf6MOoTeznqvEFx-5KeWi6lfn6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX_EEbd8ka955gUXa8mjqa3j00ezQAkz8Wd7L1Hn8nEVCuzYntInb8g1G8PB3j6jbX4UYMq1UngMzJnI8rgc3lE54-OZHvEEC7lmVXj9eHTB40f2RWOPjlorBYln1aTS7c-p_wiO2RNOrA7kmRphQSOc0UeJaygPurCnf1Rb67TwkZ50HA1l8eTOYYvvlwCQR7ZpkYQIG4WVmRXAjTwnAez9JZILcbTNSVbzVSyCXsJDd-x8x5-WRr99AUPX3fjklB0Hi9lPLdyzpLvm9Gzs2Vx1XB-jCvs1Sm7pk8JGZla7Rbk-bZhviEfnSZg7kAgCRgsKTOywsOD2TcHt8niaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2jXUzua6hqCme7db5HWAsnQpa4fSpg6wrDhaMKcv0NSw4IfhepNxyKTR0VKuswg2bQm6dqIjVuWN9vNMt0tgWoPIa25z3eVX6rx2F3xzLI7YBDjS0ptFM-mAAh0BpkiJpKMZbV61VDsyz92q8qIC6B0UO_5t8MCXWIqH1DYyIsTDXJOLPHRjxQ3t0_qiYmeKCsCn042cC5BM8gBNyDkY1fI9-m1wRB5jeeHkW5p_UyX-OZoRn_nJCNYDrU9ipt_p0JJU8YQy4f3-nH3fXsDN1TNa7RAx8m8XwTzMaqfcLyiSkCEwIgTc9013Shnsp8H96M3EeWlGfE6pzyBze7HHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS5S9d764T9zFk6An4H5s1vCscROBLJiiwGNHZ3PKoNqthjA7EcQ0OEiwVRGC45CrT-B9nfORTMt-zTaBzRuhnwOSAi0N573j2jYXeYHfJjSPJ5MurKlKB607h538uhofhuzsdPrUsKIlOTR0h4fj-UV8LHj-AeaqFVtOq_ia2nYNQcxCdd28v3yIazw3z2Ih453pO2vA11hfz3ufIZ5FU6CWS0lJ0KH_i4U9toPEpr0xUMzz277_Mxdqcxk98bl4rlWjbku7LR-QPbnDZS5NoNMqnOKmnzjRLZ_pskoTfEzF_YClS8gjtIL2KssvvaMGtx2l3EZqqsPISxlkzr3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5zSPoiZ8dLYY3_jeGHCrYyDK2CQPOBD4ls6DoF95uoRPeM8_yCCVLRFk--P56As4C2-taRDj3-rvnlXJYjNiTxOCLr4m7kq1HrYT3adA8916yvOCtBjR07nSCIkKg0bc0YADNMAEFBgPLi6vO0ab8hnNN6tD_83HZ1p_S_-oqrBaeYOFKfYn524PkdSu5EKniZtmrizGrFNE2AjDVqut91K2U5HK_YIex2vP8XWH-hfVpvtpPOTT_b7TlsLdD5h4SuKI-VarR1t0TcV9H_TaaZDvDBjUB_G_Ce7pmjFQNOyunJ6wEyquQVZoxo52Nayoqk9bI-p5iKsIYVkFFQ23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Y4FWIpm0TuuHzxTjVkkm8PqnPuZZsJqdyt2aDUsF6KRrcjohOqr9855oFDXTRlfpG1SIrGTC6nilY6blDdtZpQfLWM29q7_nZjrUQukcpLe9PmnyBLY-ot_8sjIdQwVrRxfnIibjKOATVk3JWUlZu3z690n08gblFLSfRXYLts_SB_9DY7nEZcXRjmDnLVlvoiiqCgiiC0AnUGoYbuYB4WaDqSL7Vy1ruGBjjwaGlP2jm9jIowhGgHVKq97EFhQqCjn2FwdA6BsrHIA0MqSFjGiAKFK26sQSsIJqSMKVU8qqBG8QOF43EkxzYzGpDvdk2LVnXEzu0YcBUdfVhN9yhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Y4FWIpm0TuuHzxTjVkkm8PqnPuZZsJqdyt2aDUsF6KRrcjohOqr9855oFDXTRlfpG1SIrGTC6nilY6blDdtZpQfLWM29q7_nZjrUQukcpLe9PmnyBLY-ot_8sjIdQwVrRxfnIibjKOATVk3JWUlZu3z690n08gblFLSfRXYLts_SB_9DY7nEZcXRjmDnLVlvoiiqCgiiC0AnUGoYbuYB4WaDqSL7Vy1ruGBjjwaGlP2jm9jIowhGgHVKq97EFhQqCjn2FwdA6BsrHIA0MqSFjGiAKFK26sQSsIJqSMKVU8qqBG8QOF43EkxzYzGpDvdk2LVnXEzu0YcBUdfVhN9yhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=meY1dBmm25-leT5demu21P1E2H3LH-2gSwGcqtgYpLYbI0dXHCSDeiOvNHRCIcyJcOmnKasI20sHNukullo72ZBrMZJm1Ff4qy5YPNlrkr-i7kh5EAxi3JsixcmtxjuAdZVA2AVYNim2p5tJhRPMQkDKOSUkm-hUA0Ly2m-csIDRGnZJxmBgTPImWOvqEI-0wGJOMb3J2IJwKEU_BTTmYGlBNYuJypDQDf9o5G2yRIseZ6dbA5KVUeRabJbQx-LdztkqPVucO_vGOSYGPrQuq8g4llGTnLdv94xT8DXikX8GhjSrxHz0Ch0ilD9BcgxaebcbhRw64EwMWxU6Ty6VaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=meY1dBmm25-leT5demu21P1E2H3LH-2gSwGcqtgYpLYbI0dXHCSDeiOvNHRCIcyJcOmnKasI20sHNukullo72ZBrMZJm1Ff4qy5YPNlrkr-i7kh5EAxi3JsixcmtxjuAdZVA2AVYNim2p5tJhRPMQkDKOSUkm-hUA0Ly2m-csIDRGnZJxmBgTPImWOvqEI-0wGJOMb3J2IJwKEU_BTTmYGlBNYuJypDQDf9o5G2yRIseZ6dbA5KVUeRabJbQx-LdztkqPVucO_vGOSYGPrQuq8g4llGTnLdv94xT8DXikX8GhjSrxHz0Ch0ilD9BcgxaebcbhRw64EwMWxU6Ty6VaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG2x24jvwXIKNIEmpEe6BnsCVRsoP-WKmzxMtQDJ-d8lwL2kqR-tfTC4tEsFGVFiSuFs2Is_5nnpEUoGa3c9pJv8KUskbo3l1rN8ZCYV1Qg8XQzetOsD4Mv4qdJj_GxKrkOa8xhvHiCVTAzgbe11_h-BLEgm_mSWf4IaJ3OQt0cFJyAahyNGVJMLDV2OHRYgZA-Oud1OaFlSuCTQc9XoaaPqVPYS0PxE1hslZ4sHCxCi-PEkBEDfd7B6BPSIXwHxIgA-U5-iviW8QpUo9-NjKylcMeFwQpQJReI3wT8qg4lPm7UjtAG1hUmz5QyCxtvVYpRCAO4qEZsDmHiHi3uX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=ZDXVwadSjCVl6q5WHtiFztDl36Vl108-stxJT0o9DdR_avPRelFooJsQxDqqfpTO_GBgj32tFj8I1JVklb90armcEKCl3AUbRmYKsJXtzgjyW5FA3mnutriAeZhPyuAiE5j4IdOKxyu3tQo4YWjlVp-8l349DvSOuGZB0et9LQz_wEkniegfv7bWF-JFNiLIvE2XupGX3NvUPPRz7q5yIG93aT11xOT9XyzIT3_jzcAPIhRegR7wm4TeovswaNea7esCaR_ZwkTB4BoyDOn4K-3JLTfLrF4p4PbplnwBFsUfqcJy0lkoQhAkzbrdynaELA9KB5_AyQCu3p_G3quLxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=ZDXVwadSjCVl6q5WHtiFztDl36Vl108-stxJT0o9DdR_avPRelFooJsQxDqqfpTO_GBgj32tFj8I1JVklb90armcEKCl3AUbRmYKsJXtzgjyW5FA3mnutriAeZhPyuAiE5j4IdOKxyu3tQo4YWjlVp-8l349DvSOuGZB0et9LQz_wEkniegfv7bWF-JFNiLIvE2XupGX3NvUPPRz7q5yIG93aT11xOT9XyzIT3_jzcAPIhRegR7wm4TeovswaNea7esCaR_ZwkTB4BoyDOn4K-3JLTfLrF4p4PbplnwBFsUfqcJy0lkoQhAkzbrdynaELA9KB5_AyQCu3p_G3quLxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=ZHsByrh_dk3LleX0Ftscez6dwGFLZaGCD7gG5uiO9m6Vr-2uL6mKRDQuriUyLalQ9xhEn1bbSWEvlJBmLRMlRywj9GOKNLSEt2vf3NG3WNIErVeCitFvUSJPLTx_1Hhm3C4d3kOLyW8oXDJbhR46WkqV-tyK0DGWjomhDX1mfr0jalLC0jwFpFriFg7bVNfcgxWTKGosidBf0Q17Drf0jFSvvWhs84HFn6kyeTubbYoBAJNWP_Lc1IkaTi4Qrgp70rME8eai3AoOcf4TLaiv6so1uBnw_fIim9R2uqT9SADZ6kiAwnonYivSdt9qwPB098xEKypcN9Uwr0iVFe8_kzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=ZHsByrh_dk3LleX0Ftscez6dwGFLZaGCD7gG5uiO9m6Vr-2uL6mKRDQuriUyLalQ9xhEn1bbSWEvlJBmLRMlRywj9GOKNLSEt2vf3NG3WNIErVeCitFvUSJPLTx_1Hhm3C4d3kOLyW8oXDJbhR46WkqV-tyK0DGWjomhDX1mfr0jalLC0jwFpFriFg7bVNfcgxWTKGosidBf0Q17Drf0jFSvvWhs84HFn6kyeTubbYoBAJNWP_Lc1IkaTi4Qrgp70rME8eai3AoOcf4TLaiv6so1uBnw_fIim9R2uqT9SADZ6kiAwnonYivSdt9qwPB098xEKypcN9Uwr0iVFe8_kzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVW9TYG0wRd_xAtQOgYV5YMjzsdbU3TqDWn6rYKR4Fyj_yhqZYuTxlGJDSzxt_HzM2G79cwWw3kyZTctw4nbR4xoAOcuphKxo7Lzt2vKTSIsYOPN58nlU4Jiu8z6LNEWFxc0S9iRFqra-_poMOWulbSYVFc3G5cCFCRBg4Hwt0ySuDvHM6cQr5T_mWoCjm9g2MfOAiu29jrLH5MAkR4LXHmCvKf1EtD5DY3n7oVMg7sSadVGBiCFZnMYOoata8KZGEr2ubob5w44Cy2IKlJIWwAUVWOjcfqNEgnF-2_rP97hup33sqrggb62M9TGGCbTbucxWwXHaHT55FfY8jbhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lkyvj3z6wF-UoBwnOhRTds5QykQYWkfKv4b7XYNXiBP0KKvD5kIUdLLEKHgIMJf10AvYc0EfZbZo7HiMgvJ_RreoBoCsUWd7KGKoflvgLRNfCWSsad79VP12b-GSBNhmvsQ6AsFwu9vEnEFp7ry-84RswYjLGBn2dROA9Zixj0rhn8gWhkYWn3NQASFL9TMbc4_zu0_2BDm-MH_dWXP0r14PD9DUPELZynS9A8d8yrZ9atbmnbYoijoy00cmZmnc2QFI8WQeshpi6-pMqOpGL1O5apl-gw-K58VIL8xi8LXTQNs2iRsVfPW7b_r-cZEMdyUgFvDLAhtac7fkI44q1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoEhHIYYwpZkTzdqpIdwRtLPVs_9EHtmjPIISa4X1Lv8Z8bAufl2icuyB1QtG3q-uIJzWNk2SyJwZAa2TOVGN0x8OjEkwdV38HpeC8kKBNFlNR1MHtXhENDBB0b1K376Wu6IbtI-LonwHV4QuLK1KoyMeknmXSqi8ItBXTyvsvY8WAGzzSpsEBVArUdxGsP-EXU9R5wB-gVSFTPsfDFqZjoA5t29l_5CPMJqJWVXt6FvIcH6I9tuNckD9TcLQBcG2U6-3Y9vQRuvOVxuON9rR0nOdH1uLRoePCTroaaMEcUsMw7iUuixaCFd8B-gqk1NIzRpeQtihL_wptgEvbYeiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=SSJtPR7CvFOptG_dYGgdCoTZjajzr_GjwFTaR77XAFQ7RO4vDIApQX7Cjou0xL4H4ARuKHDhNAidpsFSZaJpiHO55OvOlNphRgEBB0-r_zKJS71MDWCPEWwvau-WWvvRp8ghk66gJUX96ggLYhFSF77WKyEE70BifiEdPRqgp1EfEBP-aAzlmOXZclMTzbAGG5bp8A5NcpodFkxsW4SUqdU1Vo9AkVLgrGyIYDaRcQEKKP_csCX1ytdx2cPzlcQZ6axwLl8kkUMIgVb6WZu1l0T-odk6I25MbBhZCSm3V0xvif38u-dpUGQDGkg2CYym0gakF1smHKZNekUQyq8HSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=SSJtPR7CvFOptG_dYGgdCoTZjajzr_GjwFTaR77XAFQ7RO4vDIApQX7Cjou0xL4H4ARuKHDhNAidpsFSZaJpiHO55OvOlNphRgEBB0-r_zKJS71MDWCPEWwvau-WWvvRp8ghk66gJUX96ggLYhFSF77WKyEE70BifiEdPRqgp1EfEBP-aAzlmOXZclMTzbAGG5bp8A5NcpodFkxsW4SUqdU1Vo9AkVLgrGyIYDaRcQEKKP_csCX1ytdx2cPzlcQZ6axwLl8kkUMIgVb6WZu1l0T-odk6I25MbBhZCSm3V0xvif38u-dpUGQDGkg2CYym0gakF1smHKZNekUQyq8HSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaWJboFNdIItll6ineaC6qkeltMROHZigGN8GcI3Z9m5wqznS9eVm_ZuYcjskq2Icw02uV0DgrsglHGb3mB0zOAQcKCyv9MMzHtsJpo8YJdj-WmzUYDpTjfpts9dRqgUNAk67kD5s8Q8Aoof60PnFk-rpcIhTJ5z5khsN4cHh3AoeyCmyH11TNMTLikwtxNWFCxV7V2d6nnG1uQiJpiy6f_38193D38nM3dD167Xmnj_MxaIx4XsGEK9atTVvLtEwSRN2nQp58dFSS7jUg6juUNX-3Ogo_ZBuQSnvCFPBdlW0GWqsvyWY62WuVV1my8bwOVzRuhqS2FrKm5a5tZ4RXbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaWJboFNdIItll6ineaC6qkeltMROHZigGN8GcI3Z9m5wqznS9eVm_ZuYcjskq2Icw02uV0DgrsglHGb3mB0zOAQcKCyv9MMzHtsJpo8YJdj-WmzUYDpTjfpts9dRqgUNAk67kD5s8Q8Aoof60PnFk-rpcIhTJ5z5khsN4cHh3AoeyCmyH11TNMTLikwtxNWFCxV7V2d6nnG1uQiJpiy6f_38193D38nM3dD167Xmnj_MxaIx4XsGEK9atTVvLtEwSRN2nQp58dFSS7jUg6juUNX-3Ogo_ZBuQSnvCFPBdlW0GWqsvyWY62WuVV1my8bwOVzRuhqS2FrKm5a5tZ4RXbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=drKyhGqQ9n2iuaWFKrr81XEAoXz9x_8zHSjwPjRgfPIeLpXAWMCnMFAHx9H9LnD8611R0FA7sJQ8Xbp1zpBP1XghgB1XpLrN9Ogsjw6T7daJCgNE_A3m84A3242E9UgGjJBAfuNx7OgxSvkWEQSxk3Od7s353zFcCAc1xhi4OQ9LxpHTxrPP36Mmo1jf3EFtQB88gPzj3xw9KFBrXAQYugiM6G0TOCCE-6-tEXWUDGYsEKB5v8YQAd8GRnusxM7N0t7wttWpAIGXcZe-5nOWnSbebb1mYS8l-QlsuMWjFstq56rqoYv13xGiUcfLJUTYyIP6jV4lQ11PjGXEEJvJ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=drKyhGqQ9n2iuaWFKrr81XEAoXz9x_8zHSjwPjRgfPIeLpXAWMCnMFAHx9H9LnD8611R0FA7sJQ8Xbp1zpBP1XghgB1XpLrN9Ogsjw6T7daJCgNE_A3m84A3242E9UgGjJBAfuNx7OgxSvkWEQSxk3Od7s353zFcCAc1xhi4OQ9LxpHTxrPP36Mmo1jf3EFtQB88gPzj3xw9KFBrXAQYugiM6G0TOCCE-6-tEXWUDGYsEKB5v8YQAd8GRnusxM7N0t7wttWpAIGXcZe-5nOWnSbebb1mYS8l-QlsuMWjFstq56rqoYv13xGiUcfLJUTYyIP6jV4lQ11PjGXEEJvJ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2Y7I14IYy-ZnhWGu8fg1FkMxFeii3MhL7u_oRQ2I7WHZOsxarokbcdJ62uePIG7TYON6zCB5Il1qb_MYh4WRz35_XqvKyg3L6Um8UjJsxoqfs4AFcDErRcfOqz0FcxoAt1VHrHrXFyGd7Ub7QKS0GSqn6vEPMJaC5VEhxjd4ijJ91ssUYCFpaVmA1tqbETpNiNeL5_QfuBZ1AAMmlBPSDeaLOtCSQ2m83QdRlOEu44VftmQrqUsD7lh5_EBj1j07eTDucZejba30prMnApfBw2p8Tdft5yVfP66HITIDQcWnzAaGglCXpF0p_G4N93gFFPbibVRmdDGrgE_ptZW2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTlOS98PcYp-VK6EDn7ziFewM2JDpZVtLZTzBpMygbUL_4efVh2qJEV0eXfEPNaU6RU0bZQY-iGdq1aSKuTS1Be_yY1G-3judlFN9pLoWArokYYedh0Xbmvv55BwgqISSzECGMl-ggg1uQE-tq_4NTrl6fT-MGg3QARrpIqKUYfj5Ui_HLhL3vmLbwXgF-5VwzpUgj4lByDFCiCP62tbeYORFZ6_LQFB_FnG_dZsq3pX5VH9wG5a2Qzv33eN5nvgS19cP7Ae5u78MT2wTd_1ebBL6qw5PLKvbfmV0649Os6PaZXRgIP_frJeeRbJKgF1yh5nFWPQjrt8ByL5mxxUKlMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTlOS98PcYp-VK6EDn7ziFewM2JDpZVtLZTzBpMygbUL_4efVh2qJEV0eXfEPNaU6RU0bZQY-iGdq1aSKuTS1Be_yY1G-3judlFN9pLoWArokYYedh0Xbmvv55BwgqISSzECGMl-ggg1uQE-tq_4NTrl6fT-MGg3QARrpIqKUYfj5Ui_HLhL3vmLbwXgF-5VwzpUgj4lByDFCiCP62tbeYORFZ6_LQFB_FnG_dZsq3pX5VH9wG5a2Qzv33eN5nvgS19cP7Ae5u78MT2wTd_1ebBL6qw5PLKvbfmV0649Os6PaZXRgIP_frJeeRbJKgF1yh5nFWPQjrt8ByL5mxxUKlMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGopaBcURTDuWGz5ik5wGOc-9FPwLA6a02kin3p_r4a0Tn7sS8x03GML5L11NB-J4Dg82AQUznr5f6aAs0ZkwTuOi7nbPCAYMWsaVeMmhKsYOgm-BKfxs6_BdvSKOs1L4d_HsXO1KuPL7T6M9eHVipb6ayiNSxPddsilb6GrpgSrwmN1sOXu0Bo5w2I4q3KRqYni81Y4eOzOvo2IaQ_o1P1rF7m_02tQBHt56xZSWGUeIUdQQ5Wur_KjowQmMYQX5Zfm5c8xXI3afPZjZw3VeGuiSruCmruVwCk4f62mfRGMOEubmxkGLwurcZOLukkGHUpB7FoWupO1YpnxXyQ-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ejuM4RRntQbzxwr-sKSr0YepTW_wSus54UA_pOchIXKrIvPULQ-XAnme10V0v_4VOaPRL9ZO6qQvpIjflwVfkdImb3CWH_LX1jjq9Epop-w_Cw0eVOF2jQml4VylitXkvksnssTUT9lbxeufNSw-qkzS05ANYSQYy9Z-6LThTvchUSEi9hJB5g3AXSoke_fqwKjwo3WUPx3ccR1270et9A5TbmHmOR1LNV4cRsRH-CzoXs9kqR3UWZRhVylG-0R-3g3oxIYqx9PPQnjX8bQd6cquT3gw6bXHAmUtICd06zFR5aOQdXecqK5uWl53JECwzixE7osp_cXVQz5l_oTQjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ejuM4RRntQbzxwr-sKSr0YepTW_wSus54UA_pOchIXKrIvPULQ-XAnme10V0v_4VOaPRL9ZO6qQvpIjflwVfkdImb3CWH_LX1jjq9Epop-w_Cw0eVOF2jQml4VylitXkvksnssTUT9lbxeufNSw-qkzS05ANYSQYy9Z-6LThTvchUSEi9hJB5g3AXSoke_fqwKjwo3WUPx3ccR1270et9A5TbmHmOR1LNV4cRsRH-CzoXs9kqR3UWZRhVylG-0R-3g3oxIYqx9PPQnjX8bQd6cquT3gw6bXHAmUtICd06zFR5aOQdXecqK5uWl53JECwzixE7osp_cXVQz5l_oTQjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Y82ZXvFUS6yHkMe9edkPJCCoEvmqdKCMZU3lNSJP0Es-YGg8z2dSxwG1zVhk-TjC5PftjN3YdCHsH2axM47tyhNZo7REUflvkJSNBp5JwAFW4X7_2JP22LSD2Kt0E_GsfNPgQPGDHMybhBmQ9brLxIBDKQ5Quh8-0kafV8IoMVp2d8gnvzZ82qDU5n7LLiedvY25fJL811phgzvLkBOdAxoDQL13dk0yDCWn4w0tXbgDo6sCfoZ9bznShA-hNkymCwd-PcI_3Fqk51PDxhQHp9rz1zD-q3JkCpuZ6lVoYQL5rZLwmldaT7drxq8aaEtNGqx5RFvwmrPgsylGOfp7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Y82ZXvFUS6yHkMe9edkPJCCoEvmqdKCMZU3lNSJP0Es-YGg8z2dSxwG1zVhk-TjC5PftjN3YdCHsH2axM47tyhNZo7REUflvkJSNBp5JwAFW4X7_2JP22LSD2Kt0E_GsfNPgQPGDHMybhBmQ9brLxIBDKQ5Quh8-0kafV8IoMVp2d8gnvzZ82qDU5n7LLiedvY25fJL811phgzvLkBOdAxoDQL13dk0yDCWn4w0tXbgDo6sCfoZ9bznShA-hNkymCwd-PcI_3Fqk51PDxhQHp9rz1zD-q3JkCpuZ6lVoYQL5rZLwmldaT7drxq8aaEtNGqx5RFvwmrPgsylGOfp7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=B2XfzUpZX_dfE8T4eksI8r4gd8h4FMLdTH72QL_sFHCK4ki3V1PjzyQGLRzYiw-_RfWHvWStcrbWiCnskzw9JQI1BVPfE2qxifC8M2CzsRE-M0Ziy7g7yasbc2xUnn0bMhp98Bbeu6M30ZYN5fKQop8_o4_sdd9UIoN5yylZHbZd6FqO-9OCg261jawfd9pLJDNFIoY-v6mKe0w8S0-XSdTb9Uk2Z3rkHrGLZbSg_cIUY2reMFAkGmXDxLLrE6zd5W_YDEPa4m0vlMxLxDsv3bGXMfCEhUEt0IcWi2kqw9EDPFNUUGMZtL-2JUX0VN5JfrCJ-Uo0doXXNRRrAP0emg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=B2XfzUpZX_dfE8T4eksI8r4gd8h4FMLdTH72QL_sFHCK4ki3V1PjzyQGLRzYiw-_RfWHvWStcrbWiCnskzw9JQI1BVPfE2qxifC8M2CzsRE-M0Ziy7g7yasbc2xUnn0bMhp98Bbeu6M30ZYN5fKQop8_o4_sdd9UIoN5yylZHbZd6FqO-9OCg261jawfd9pLJDNFIoY-v6mKe0w8S0-XSdTb9Uk2Z3rkHrGLZbSg_cIUY2reMFAkGmXDxLLrE6zd5W_YDEPa4m0vlMxLxDsv3bGXMfCEhUEt0IcWi2kqw9EDPFNUUGMZtL-2JUX0VN5JfrCJ-Uo0doXXNRRrAP0emg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz0CczoJofAiIf0sMqvThQ70YWuhhIGy9k3123L-j8cWgeQiX1_5HPrZFTk9NwnP640l_YJ13y2pekp6YdGtUUMdx2wvKNNS3QfO24-oZfbWMAgoOeRcf_3jz5OIMm7-gd7szCqqrwQ70_ykVvXQOQwmqC3aZdLWsDY9X4GASZG6yAtit1_0UKTiFw0Rk4sfOre0_wJjmhkyJzLeYrDkrntSDX1KUV_XSsTnR3dONdUUTiLRXXgvLg9xJRHS1QSxD1jdrkGmftIdVuoobtikGMzDvEpgrKfctLOhqYgfE28C6Ok7f3IS2vaB8lb1qQ1ITJX95-QCtrLWUyAh6eJKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpBjPEHh6GOEbiIdSrqVzZlhg4_3jHY4fjKjn04q87lT-nQlqE7TQxFkQ-GqyAuy_E8imum9Lw1SwP63umorsGu5fUIlS-okysm2AUJvEOFfMCpVLEClNKC7gLYydndq1BihKb4A_j4jUQuvIeKHO7y45PWcZjJROJFJjW743LroVjBseiFClnVq9FX5kE8dsnCLwFBzOpK9HC2mmBjMH2bnWdQMiIMj1nGZ4Jrp8YZ8L9gC3dJoAgce6X4rVFOa4_s8q49sq6MoEjK5zz9OAnk41GIg9hkobP1JIAySjy31tZX8gSKs8E66xV6YLdWGuGh496HRSX0v5N6VIM70Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=uWdusf_73S9zqJXO5DDOqPKDek8B4LcqNeCa-76lHk5q3t5QO-p7MD_Lnur14fSWymsGXLI3K6vNfTVf29y6IvbM74deIJV7LK0_k6nkcj4xObTD2rfK0RZt0gkNDxnAYVP6dbP-9JLzTI6Yp6QvcY0CvsluPQA2UOOvHdRBJi2r6wQduMWlNE7vF85PxZLVdTLZ3nn99XQEawmlI5VfBOZ-gyandhR8dZ0dnY9EdSnD-m4BhVGCCothLIPY3u0tVgfuKe2D8kdl49rDYVEA3O_PZ3owDLk9gxssBvI4CI2jVX_p0xVFAcbU0nMNY7ISd_HOcPoH9qGubQK88sNv8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=uWdusf_73S9zqJXO5DDOqPKDek8B4LcqNeCa-76lHk5q3t5QO-p7MD_Lnur14fSWymsGXLI3K6vNfTVf29y6IvbM74deIJV7LK0_k6nkcj4xObTD2rfK0RZt0gkNDxnAYVP6dbP-9JLzTI6Yp6QvcY0CvsluPQA2UOOvHdRBJi2r6wQduMWlNE7vF85PxZLVdTLZ3nn99XQEawmlI5VfBOZ-gyandhR8dZ0dnY9EdSnD-m4BhVGCCothLIPY3u0tVgfuKe2D8kdl49rDYVEA3O_PZ3owDLk9gxssBvI4CI2jVX_p0xVFAcbU0nMNY7ISd_HOcPoH9qGubQK88sNv8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeF-0SPDnOI0f2bizjS56VoySRw6m0aMwIyrdPvZatlNu_WBObPaLvEFyoXkM_GdcjV4xMwbM8ksi4-nWCARyPY-Zn1TVSmRcOCE9Bi4QHnVkVV4KFjVhhalzgEqkQOj63g2aaH6B21eVNDm5HrpILRC_YsUrCo0FEskZZ46OuozwLIGlG5_iADRt7U4nuIvAky35HNduKP34es1kDumvLgGhqEXXfeB2nnOzsc_OfVxEmgZHPiqYud90rFZe2udfYhhmXOcdYeuhwrUt52jkwpG3VgJ29re3zkMx9qiE3O-LZ6CVmQBsrQlTQf0XcJE_4twLNOR0aZAK7j91442hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2CfCDUbIBenIo8GQUxvAGQOXDo1JO7QFbXbT6cmkRqWcK2W9JttHnkFDOMx9QO9TNDvp2lLuX2Kp54hCQ8Gstjle6lFyjrLV8n4ASgG2r3hxAP64HmryXuT4QoTEqybqMeJyNfTUnOi_f5bHLnDJgRRjtoaNE2MAvW0QUP5RWFlftWb0ErAk8jb0pspik_M8LPsVeWzZ2S4Kkvw6Xsj9QHfSq9iD4jyC-7yxC9nuous-IySCiZP1NzDtmYUP9op2_oS9ygi78oAfM6inzbg19Xc9jY68s-gZGp8bzZTY_zGxp5C30roaCpoNaaUnzIlPV3rnr0KNOSpR64ArsUOyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=S05Q2Iq6R27zZlVGbpGzqwYOjQtgCmwMmpveUq9Z6vn819FvuYaYrpqPirnZIP0v_WYWn0YDfcG_V88YHfQaXhnYLozA5SCFMoy6Qm-cLNhEDO8CsFmgny3I4bjSnSO6lLx0GKqxQV79kEDp0gpe7oXZcfrnWfjH9Kq7KRIL9RMSkDZDUUYURnsLK-Z4s_LOJDfByEGdtwBhvONbgu_jg0DIZUredG-6LhwAJtNXWZYTtNIi91vM628oLT2ugjCe_92kTeWlkJz3rrxnrOzi3WCf7BY-IX_Os7a5z97juOJDeFvqX_Dr34IOVOrkgz6yz76uvcFSK_B1psFz4vxepT4AajHzBV_qmKBxXyuyR4-PJjNdxRQW_V1koliZTbIk5jv8gG9bYbJ9Tq-qzJsnHB38SdQy0N6yVg5ZphkI3c2jK5gEvqgaByKWNzsD569EWF5QZHbjkkFVBqEvA-l9UZGEneVBj6cdSBnfROGCIbWCv91sggmvpixKOftOdKUY1NnYuokIog9117VoNYhUsTkdYb2vSyWcR-L9pXulMqN2Nunj97ZM6pJT4XsrMUlCclomxjIPkEGMC3eLGvKQC6lxr2CREuJUzq9z1DhMD1sbApc9elGF-SBKIN6xZM9-GSxwTavurF1XdVJBc1n92BYgmd4TNRssIB3_2LLpxBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=S05Q2Iq6R27zZlVGbpGzqwYOjQtgCmwMmpveUq9Z6vn819FvuYaYrpqPirnZIP0v_WYWn0YDfcG_V88YHfQaXhnYLozA5SCFMoy6Qm-cLNhEDO8CsFmgny3I4bjSnSO6lLx0GKqxQV79kEDp0gpe7oXZcfrnWfjH9Kq7KRIL9RMSkDZDUUYURnsLK-Z4s_LOJDfByEGdtwBhvONbgu_jg0DIZUredG-6LhwAJtNXWZYTtNIi91vM628oLT2ugjCe_92kTeWlkJz3rrxnrOzi3WCf7BY-IX_Os7a5z97juOJDeFvqX_Dr34IOVOrkgz6yz76uvcFSK_B1psFz4vxepT4AajHzBV_qmKBxXyuyR4-PJjNdxRQW_V1koliZTbIk5jv8gG9bYbJ9Tq-qzJsnHB38SdQy0N6yVg5ZphkI3c2jK5gEvqgaByKWNzsD569EWF5QZHbjkkFVBqEvA-l9UZGEneVBj6cdSBnfROGCIbWCv91sggmvpixKOftOdKUY1NnYuokIog9117VoNYhUsTkdYb2vSyWcR-L9pXulMqN2Nunj97ZM6pJT4XsrMUlCclomxjIPkEGMC3eLGvKQC6lxr2CREuJUzq9z1DhMD1sbApc9elGF-SBKIN6xZM9-GSxwTavurF1XdVJBc1n92BYgmd4TNRssIB3_2LLpxBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETgNpibUk_libvI30VblgCydB67xI50of2r4wS2pr3wWA-SXERfpQTNhhYBd3YE3y7c2G9WrphYShavLXbNcm1nLSZeZk7yfOuROXj4UR1w9EeU_Z3EAh-85KxygkbYHyyZh3Z4BLAVwbJeNDBnamZEHW_MiPmZqyivkr4jqrUX35rzWibrwRahVwCkRlMLFCKsBwetUW1kzu1BEMJYRJOWwqNcKaTc2Z0zYKLFKLrwahnn0E2DB-5aYkg7EETwQ1iWu3E9MCWb6Y10zfHSJsw30GhI7LMbnkHkO_TsdLOqA1PmWsDH4OSMJfNwahKrQ8oLp-imyj7ypy_vhEQnzCePY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETgNpibUk_libvI30VblgCydB67xI50of2r4wS2pr3wWA-SXERfpQTNhhYBd3YE3y7c2G9WrphYShavLXbNcm1nLSZeZk7yfOuROXj4UR1w9EeU_Z3EAh-85KxygkbYHyyZh3Z4BLAVwbJeNDBnamZEHW_MiPmZqyivkr4jqrUX35rzWibrwRahVwCkRlMLFCKsBwetUW1kzu1BEMJYRJOWwqNcKaTc2Z0zYKLFKLrwahnn0E2DB-5aYkg7EETwQ1iWu3E9MCWb6Y10zfHSJsw30GhI7LMbnkHkO_TsdLOqA1PmWsDH4OSMJfNwahKrQ8oLp-imyj7ypy_vhEQnzCePY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=POvqmAJy7LQIpve99OuO_3p-OIl9pXW6I5yqy52dPcWyhnyXj39fc7DkpnaV26rz4IUFX_2GeLmn9XtPt5OFucrb7Mp-Mef7TgRuscsAjK12LuZn4BvHpCAc3mk9KAP2ROewcB3FUKS11fx3d-Bebmk7VaETlNAd3u6WlK9HB-ytazvGTKyRFo29YbsqzlJ3RvQoaS_43uK7sMn_eld6P_haHlOZmMlFmaVeDr7PGekNClPSfj-7GbQzpqiadnghnduIE89Fjo3E96-S34JXL02TEdBF3wN7dUwCOQKk3Z05HD3YkC_-A9BZK67urDPdf42M-bsIuxflzuiPoJjqZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=POvqmAJy7LQIpve99OuO_3p-OIl9pXW6I5yqy52dPcWyhnyXj39fc7DkpnaV26rz4IUFX_2GeLmn9XtPt5OFucrb7Mp-Mef7TgRuscsAjK12LuZn4BvHpCAc3mk9KAP2ROewcB3FUKS11fx3d-Bebmk7VaETlNAd3u6WlK9HB-ytazvGTKyRFo29YbsqzlJ3RvQoaS_43uK7sMn_eld6P_haHlOZmMlFmaVeDr7PGekNClPSfj-7GbQzpqiadnghnduIE89Fjo3E96-S34JXL02TEdBF3wN7dUwCOQKk3Z05HD3YkC_-A9BZK67urDPdf42M-bsIuxflzuiPoJjqZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=RSuzWoTEIaKqVhXQhhonmzpL1EhMLVJnikfm6JS-Ov205nXz8HT1CeWHCeRG0pO_dlHkJtgNjmiH_91DHdn-bLkw9yKRufuY1DEJXDFVuQrXZXl9eFzkU0pgJrRlwVV1GUt-GKbJzkhFgUj3kON6kJulhZWDIZ73aLgtn18CQ7AK6ZH8SydWZqko-Eaz3xnWQsAV_MYsDR-uN5BBIVXT2FjlIveZzThdyyI2GpZVVKGv2GJzxuMeMK26JLoXtaaf14bqu9z2bg0P7z4n85xujHuK-XLnLu07Os2OhwELsWZQX6SHealfuxglvUHWxplA9FIQZMdsPZd-7ax86j0XVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=RSuzWoTEIaKqVhXQhhonmzpL1EhMLVJnikfm6JS-Ov205nXz8HT1CeWHCeRG0pO_dlHkJtgNjmiH_91DHdn-bLkw9yKRufuY1DEJXDFVuQrXZXl9eFzkU0pgJrRlwVV1GUt-GKbJzkhFgUj3kON6kJulhZWDIZ73aLgtn18CQ7AK6ZH8SydWZqko-Eaz3xnWQsAV_MYsDR-uN5BBIVXT2FjlIveZzThdyyI2GpZVVKGv2GJzxuMeMK26JLoXtaaf14bqu9z2bg0P7z4n85xujHuK-XLnLu07Os2OhwELsWZQX6SHealfuxglvUHWxplA9FIQZMdsPZd-7ax86j0XVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mInzmFzn73VYQ-Pt-w2C6nM8-0Bqga8AqD1NA6v7rnzh-gtcLEA3OVj0y8aUnxj9t6TFXKsUgDPX_dWrpY3jiIY5eGPX4EzimHSZcBHHkKoiMmHZzyK9bO8T3Iv9LhqV-j0Iox6i0egM1p2mpQDbRMBu6tRjmJoksiU-dFJbeTQDH0j8-sh8o3emVu19zHZ4FRsLWljqxhTvlPxaB6CkrVFQyIDyXcUHaDo8dPgpQXKd4p_KhnGbb-98kVHZpFgVFJkCSoRZRH0XDdldAgCp-IucvRqgrCfZvN-vgvBxLX7U6A4Gaog83uZNkkTnyxtEqWr_xqD6hBn907YimgNJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmKTE5gG-8Q7X7o-aZBxCa0d8WdZtT5eFO1YVFQcrbP_G5KMxIRJ3QXKsUWwUwlU8LXQXFwXhr90oAACTcOOcebkqv66GwR3lvJlE-YAZys8E5esvbfmimHfiwSvMKm7Ewt4ZZoNiMeNYg5fhw9_Y-Fum3vX-SVPP_vxtUm7EvZzpPChwhgJYgQrhavJ0R5pKK_U-4SnT3u3M_zqR22Dzry7Mm3pjF4A2zaEoI6iLoK9KhiTc562G-il-Hq1BBg5AmEXJvabRd9kyGdvobdRFxGTdlAGSr8KWuZrBOzIMXJcYhhRIEmtAVZtKGCRa0f3XN0un2a1o0tVumgQRlDjmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUp3TrSshkym8eysBOrYCXwVax0hVBska31IGyL_-PwAIvmG0ED5bqMnDv2gYtHRonLEtBjr9RF8vg8T3ZayAr3VKKlOsB0L6tDMy8fl7VqKRA6LnKD7lsYcSnI8RU8Qz-KfOxsQx3PEt4FXP9H8UohfHu0bzj02qTz9IqMqxhjWmaEoSMBFcWVJN5-9ttziGeLCy5OOotO6_ocwcUwrqWqw1xJT4q0W_BrXM9LDi97yIlTSR7ciGK4ggN09SAeVgJSx8F5MLJ5KOl9CZPmvsakXiWL7AmQ6bbOwuo4RO0qkHr2AI_cpBxtsHXscYY2r2LLQArG-iFlYsQdb_PDhUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZySEnaclVniOKUKHgf5UTUUsJu6zHW_97eOLFhvdegN8ctcb-Ck37ZeOCtiFXqaAdH5Ukl3PjEvXR9_SrL5PAzST4pRjlnmAt6Lpb0hCIAYtyziplITz2Tt_Y45gYiqLWU2YbaFqH136MRlMCkyfezmeO-UpyKChHRBazDT5N918AFpHhg6MXehfuOCEYDfU7RRsat7CINqh5PX8udzcCyuxk7lRXBdPN1-4lkulkTI1qnQujyrj0qH43Ovzy3WuVvwB3LswXsVe47oCoAR5zSLVHSjTyzpkivwa7WC26qSgBs0QR51zXSTIQmaX2xrBr7Mw6gWK7uVnGWeQ6hOL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBA9RgBR8MV4moVezbdlBEgewWaBqV6m6-ywTijuwpJwStDIZj7earHx3b3uMU3Khp2q4KVx1eZ6c2iShVfOM_Y3UGzP0G3N2I25nppG215wSvd7Sp894eWGt0mirQXfwW5jlEuARvS50ss26u89750-7eoQbt2ySl_VsLQZLWiYR7EUovZ4mlMwF-2bwGKBxlCZMTzcJ9yRgzmMgSv_TuAymFZ4jLTw23B-XRkHbzb9sa8X9Hw0PmTPcmvvD3jbJ26Km4X2GYx_RJW-os85wSzTft_Thw2u0EDfG3pE8EKSe2_PmJG8QGTI3S5X5awbqSpw1JqSaamAeN2dwUZHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=ifkFJ8Dq-Eppt5SgfCyl91FUdlqDWNh40fT6WuANLc5-0yCWfy05sC-3GCUXJSQHaxao6R00ZAtqAX09LeQqxbJ3PunO7H7ootjJwwXEiqWg-lCD3idHyyGjW9xoIakRHCDmvP-3ukmNJhdZ2NRqB8b8Gdi2K1MCUlo5NyOmo8sxqKVQz9SGukCxlcrIG-xFUkItxrxIDj5TQ87ghHWBXZP_2ytCSvo2tuOlUG-xKllyM74KqdA3ypQ3bFmyWYDxcAGx9M7ZHNJfrJI21EnN8Sz6LXglqgKS9rTnakQDI-wnszplgpcNgM6pClhSLPGD8Hy-6LtjYfMxuXuDElGKBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=ifkFJ8Dq-Eppt5SgfCyl91FUdlqDWNh40fT6WuANLc5-0yCWfy05sC-3GCUXJSQHaxao6R00ZAtqAX09LeQqxbJ3PunO7H7ootjJwwXEiqWg-lCD3idHyyGjW9xoIakRHCDmvP-3ukmNJhdZ2NRqB8b8Gdi2K1MCUlo5NyOmo8sxqKVQz9SGukCxlcrIG-xFUkItxrxIDj5TQ87ghHWBXZP_2ytCSvo2tuOlUG-xKllyM74KqdA3ypQ3bFmyWYDxcAGx9M7ZHNJfrJI21EnN8Sz6LXglqgKS9rTnakQDI-wnszplgpcNgM6pClhSLPGD8Hy-6LtjYfMxuXuDElGKBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=TdLTR1fg7bpuJ0wQTn-MYfq-eFnJDyCy1lUqbxg8joahfJ7sbkrOgqGEAywfX-rbB0UnG7sxxG0VlzHKd_oTkf39RHgu1p2he-kAeI_7Zk3b5zPYoe_qhsuOrp860NWM6sC7tMvbOO2G-uBkUSBuKrr_7NB-8_PgwBkjhTaYAqG8S0J0X51DC52tWakEs93EWzZdBeaHdgyGvADWNJ4lwTYx8lNJ0ncrFntDXsyKNdAZ18BvVanmm--gE1Jikj10cXhhQ0mxOM0UzEQyFejgV25kTSxOoG-Ee-XH_DszmCDJusqnLKKHhHLOY1rUC2OJV5oG5k9ZOPAw7vA_25NQpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=TdLTR1fg7bpuJ0wQTn-MYfq-eFnJDyCy1lUqbxg8joahfJ7sbkrOgqGEAywfX-rbB0UnG7sxxG0VlzHKd_oTkf39RHgu1p2he-kAeI_7Zk3b5zPYoe_qhsuOrp860NWM6sC7tMvbOO2G-uBkUSBuKrr_7NB-8_PgwBkjhTaYAqG8S0J0X51DC52tWakEs93EWzZdBeaHdgyGvADWNJ4lwTYx8lNJ0ncrFntDXsyKNdAZ18BvVanmm--gE1Jikj10cXhhQ0mxOM0UzEQyFejgV25kTSxOoG-Ee-XH_DszmCDJusqnLKKHhHLOY1rUC2OJV5oG5k9ZOPAw7vA_25NQpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKejLPiq3Pe56O6YHqnW0uINVhR72unLL30lqLagGyCpJNWCsMh_UdWrOQyVef5FFoAJxuymS3kwNk-sW4cvNJyXN_zHWP-VpyQbnGyyfdZbxB2WSYPCUcNqb3irvE5TqSh0DStpXzVzr3LNHCWO5BqHWXG7Vbo5H5scfG2QWQhdtDChIOOMnwRG9zSJdZ07MO2k9lNLn_8xw8VvrqqUfLXKLIW_leDupsLZYM6BRFrJDnh5rl8earDp5WrcMLXQmXNfHuNnh3ZMkCDS4I8NoP2Hw-v3PHyNYWscRwZUWT6VBmF0MANg7FCLOoz8KPDCuOroCXZxXqS4gChVyWTnqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQVQ2ONP8nYUXVAOKDf8UGFSyzX4MfbtXIlzpxTrxC7BlQ5PsWffX2g4LzCOldrJEvd_GE3oa77rmL0QPCZHioiG5Ni9eztjv69mFalvx4PJ5lqN_yUhX1zYeZqehK-hJkTY9TXXLZ85cTQZKRiL_-gnVP9UfCtnCkaEVOz0O8u_Nj0gKIdw53vOE9ydhOuGTmoHMoPF7rk8g_Nff9wEU8q1GVKC9RWtxEn-Vycg2ZlMcEh6k-AmzpdejjfSQz_yXcl7xJYIz99zGKF_elmxlsDHuCqpt722iiP73IHDhhuWQrdnZDM7uDXmp4BDNmE17VDJqy0o1psR35fKv-bShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=ENT4jy19hqd_5wTxmpsZPKQIIBTA9XRaBk1ghFZxTpS_fei9uzv4ZwZv14PZMTK9FjDEDL202IRNVgJh4JlelW_gFVAAPlPOfVMfiVydXVJ9i1FTXwX6Wkg07Fq5H-OfaSXUsxeyZa_Vm2OGdXTNaWxvBzBqbcFtTd0Zj0tnrvPLok2yQ1koNMuf7IoKnMPTSvHX8WKjVoj1hA9sFklkDxSiOZ7wDuEfFV57RDKakcH73mcPjle3MSL7ST7IeW322xjltC84WBbAD-Oy2yk6RS9UCvV34MFwuIPlS5yRrPVRXne45N-hGtrsaVcEolkEnK1vGHtaYlIcoLpv-jlAuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=ENT4jy19hqd_5wTxmpsZPKQIIBTA9XRaBk1ghFZxTpS_fei9uzv4ZwZv14PZMTK9FjDEDL202IRNVgJh4JlelW_gFVAAPlPOfVMfiVydXVJ9i1FTXwX6Wkg07Fq5H-OfaSXUsxeyZa_Vm2OGdXTNaWxvBzBqbcFtTd0Zj0tnrvPLok2yQ1koNMuf7IoKnMPTSvHX8WKjVoj1hA9sFklkDxSiOZ7wDuEfFV57RDKakcH73mcPjle3MSL7ST7IeW322xjltC84WBbAD-Oy2yk6RS9UCvV34MFwuIPlS5yRrPVRXne45N-hGtrsaVcEolkEnK1vGHtaYlIcoLpv-jlAuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=L9ltZljrgpatb6Hx0-MqfJcRreeLZnTJ6vHbMVUfZ2CeRviFlKS1zd2-7jfqf1SQ-SNMG4uSMv7a_-9Za8WNc02hQ61lgdF2C4l62jQ9ARxbVMyaFTD7Os8KLqPRhRTSIQfJSJ7AfiVpzJmlX-sFS36J8-Wk7DL4Pl5MSCRKauZWHeWnyEd3QWp5SsjXzhpAOtKT8CJ_Y2ck0fOY-4Uz8MUwE3JN7v91LJnAvuui2HVn7dmftRLphS2rn12wU0uCTjwW_W5jZs0pG8p70ehYGyR1r_NqlW_X4XduMAkXVEdQdZJlChbmDeVxO5IFSPi2lHluC2dJGo2L3SJ56ivqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=L9ltZljrgpatb6Hx0-MqfJcRreeLZnTJ6vHbMVUfZ2CeRviFlKS1zd2-7jfqf1SQ-SNMG4uSMv7a_-9Za8WNc02hQ61lgdF2C4l62jQ9ARxbVMyaFTD7Os8KLqPRhRTSIQfJSJ7AfiVpzJmlX-sFS36J8-Wk7DL4Pl5MSCRKauZWHeWnyEd3QWp5SsjXzhpAOtKT8CJ_Y2ck0fOY-4Uz8MUwE3JN7v91LJnAvuui2HVn7dmftRLphS2rn12wU0uCTjwW_W5jZs0pG8p70ehYGyR1r_NqlW_X4XduMAkXVEdQdZJlChbmDeVxO5IFSPi2lHluC2dJGo2L3SJ56ivqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRcD1t6nGr2rbZnl1CKB9XMvcDRGcMtj2A4-qHV_Be3SRhQZ3GOn-zG86DWCjSCIH--SLqDjK3KLlMh3iABxO4RIR1DjBVtlYNhTY1CfyiUn14LvNr1NpJEFSQbiUxKMoCl3UJg0OxvQCreamkWkTaD0m5n50oz02JWSzsKIT-WvEO1BIcB14YKDB4Q7EqE_EGunhgrQL7cLmmDeYnHvcecsw9-xSh8aqDtL-SJHHkT8gHWO32zhVKbqSjvlpRj2KQpTKBdiaWC8YaQAODPekScgaFwQqwg2LvPmcLq2fNbFn2glRfX9GZMARZ0ozk8XKYbJczt8XrjIuQmywM6gmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXvIcee-YNLRdL_1kpffNmG47bfQ9DSnBmOPQ6jmS9FLP3u_QhxeQSg2oRSWnPMOdZLi0Vgl1jYfkqvmgZPQzM1cBJHhP28P_2sprpUCSxBg0MBCHrROShwpSy8_vUKJHOOnSEuYnrHwGJJNXOw1UHTFl6bYAsrfzj_shf3zWFaa8HgNltW5PgWEd3AAm-2JEtZ5Zji8w0JV-3hwL9UlLij-VX-wS43ScFyw2qz-nrl3Fiw9xeefBXFYg9nf8XFzPN9GnY1vZ-LXu2iSXmSaXXTVXuTr5_nU4yetHXbGAdBxdtWCwj18ANpkiuaOvwimJeC8yNbdfFDAyS9G3pnl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a80WWn46GxECAjDp00gP4bj4J-pVexr0A89c-0EDk51E3_gFEFRSWnaQKADwty3Nz2LffwCZTgkdTI8J9GpBnXkwCrQ6BDrgzaANVG4-jfcnKj1LQoNgejSMfB4sw2EIQOKXXMpO2lkAXL3r5Ep4h-NfgA8ZazEqo4SeNDnOy0vfrIULq88iVbb_qQGcAqhV4kXTtbJKA7U06iMfaSA5OORIlMwrIrL0fVNuwDWE4yNg24J8ljItqcIszgywCus9raMfrgu6TLriE6m-iZJO3u_d8VScvITKwmBCIhu4lItOnbf9dx3DHjJJMkJc0bU6JGqQ0VM266td_mp8DQ_SRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=GIGql4dNbwXFWcpq-Z9VdvhojCWicQNoNiTdP-FkVU1tCVw9eiAlEJN7w4zIa_mBwnDqVy_i36BmiXKasEJ5QLZOitMG8oSyE46eGApR-J5zMBJco0v71nRwcfTqVEIke8ya8AzcOxXY1aqCicwq0iee88qyQentE-ABbR0ZtNTjPKm4zAEwhjrCS9JVqFTmjfPlwvUgP9B5LoEJphNB9bzXlYV6ww5aUDTKbXx9_YyqqsCIAXcvs9-v0u-QF-0VcVr99lDfucDItsYw3E1O-SBGRkU334DB90IUy1hHhqVlZK6e7VlyOZKGIMBlg6GqrxLdwem2H0HyetG-ROSTPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=GIGql4dNbwXFWcpq-Z9VdvhojCWicQNoNiTdP-FkVU1tCVw9eiAlEJN7w4zIa_mBwnDqVy_i36BmiXKasEJ5QLZOitMG8oSyE46eGApR-J5zMBJco0v71nRwcfTqVEIke8ya8AzcOxXY1aqCicwq0iee88qyQentE-ABbR0ZtNTjPKm4zAEwhjrCS9JVqFTmjfPlwvUgP9B5LoEJphNB9bzXlYV6ww5aUDTKbXx9_YyqqsCIAXcvs9-v0u-QF-0VcVr99lDfucDItsYw3E1O-SBGRkU334DB90IUy1hHhqVlZK6e7VlyOZKGIMBlg6GqrxLdwem2H0HyetG-ROSTPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU755sRZYL8N_pJ5_e1YY3vNfDeLMIewAo4MuRlv9Y2Y9bslmv1KrSK5qG9ztAZiIvj42mHWDM2WHYt7GGerkxclKF-v7MCc0Kbp7Um6W-8fwzJa4E3ODMUQNqdAEQWBFFf2VgG4OYkYMyUiCZVzJaIXhe0XV2rS-UtpFQqztHhFU669kETvBu9QMRpz6Cu1zDg8El_MwxPidainjHQrU1A1L-KyKrkonAST8UP6xepUx9-DFbLutsalgpqgxuzn9k3UT61942elbDyTgMdTglxqCl758PE41bKMDLzm4xlczXrquzeOUz4Ftwc4p9pFunLvibC442oPMjHE6CgjAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewTROqUlDKX_Dw3zroBZ0R6lNF2KlSQfippCRjXlZyhMfoI19bUjgjGCjHrYEorC0aBPQXhnmC9kcAB9vujXSGRCfzM7DT-xGu-pRp4OsYy2ib2hPaLwQXxXk4z5gSVgD-r0BFDYRUNpsVyS3T9ttnPnRF2iEeP8LTFnlYlq0N4F2GbhptGoclnk0mIRwLrx5FMoRdLC6U81EAzijjM2YWACR3jDuOZ4YWhFgRPGcpKjvXW6Nh8kG5H_Zz0mzny6vrQ5JvL2n-spaVUm-56VLzUeYyf36UC8YUcCibuQSY8BBojA-Rehsf7b7l0QjTVbPNOVM5aHXZvGHXQK3YP9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWq14gpyAKTZTRlHtu18F332pPjH3elrFoGQbre16u6HiQBv1btoaiv23g16xrIulcj29oCpfY1oKso9zpS3OfNdbiOVU5AmNvCElcXNDJ_6xXDS4oZOss9Gp8xe3-nk7iFWP2xFUA2riVe21AyiWbohrP4nJK9-N8y0H4BwOwsq2W3OyFUi4cPgYzS6pG5jUWR6qRu3vjCzNYdID-_g3zhVWyZWghe2BLKS6jpNFh26mv2FnUdMBg0Sqi9fx94TXMOSS6HkpKjQVKVozG_XH9vK_kBljcfRsUr3f0dOiLbJKpGDdHuh8l2h9xfauu3tQohe6pqkrvm-DNXapHRlig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpk98CAlaE2_EuMutif3YNXokmeedma7AQGHhudvMnlcvMnXCHWhsD_RlJkpvcuHMzjZbumzzcQhxuq_NPPgFUFD_v34pBhrdAECpMk_2PJmR7fYrxpQifNeH2sd9d5yVY-V4Ga_NDAGI6ov16y96nWwOcUwuTJdIUGf83pEnSQUBoYKQthEFFPZm3Q-d-3hPRmO6YaZYE0_SrzzvR94s327YewOLd6IfQyCHHDz3WrvghzSsUswVgV9ZEptBdUkyeS8e6FYn-QEnj1BBf4Hvr_Pf-r6ZduZHSsz9Sg_YjF4i8VOnhVF8WZ9kFNo0lUMLfVuzrftA6dGeZsp6SrGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QPOhFOmEsRONXaRaSKKhg6pNU0gy4jePDwUKYiYAGylJfVJe476Dhgtofkz0hFMgG4Xf-bvFY2Kzy2ABq0kQIOd4HdEgbcY9CTguOEHe4PSr34n0LjBarkTRJC_oJ44S9vE6PwHIhmI7cDVxpX3FFh3kN6CVx-vIezJn5LqlM-T6JXO2em5SYyi8xC_N8WAQ08kwU92mPxNxELVTIRhOX3SWrklsSkSOLUswotB5z4Mr_LSGxs9Kxdh1mUb9OHptQ6-jtiQ80kSYEH9hXmoXx7WRhVnCWFF_lHtmrty8zQUUC2irdbCpAa3qYrOGm4RMeFPFQhO5i6L4afn8Y2rvtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QPOhFOmEsRONXaRaSKKhg6pNU0gy4jePDwUKYiYAGylJfVJe476Dhgtofkz0hFMgG4Xf-bvFY2Kzy2ABq0kQIOd4HdEgbcY9CTguOEHe4PSr34n0LjBarkTRJC_oJ44S9vE6PwHIhmI7cDVxpX3FFh3kN6CVx-vIezJn5LqlM-T6JXO2em5SYyi8xC_N8WAQ08kwU92mPxNxELVTIRhOX3SWrklsSkSOLUswotB5z4Mr_LSGxs9Kxdh1mUb9OHptQ6-jtiQ80kSYEH9hXmoXx7WRhVnCWFF_lHtmrty8zQUUC2irdbCpAa3qYrOGm4RMeFPFQhO5i6L4afn8Y2rvtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQXolFY6vqkTr_fRM4zTASsZ4CSnoBMD5M8-NsHWeLs_XiN5I5mU-S4nvnCheTo3_4m-ZZgPecFTdNWzPZ7CJ7z1cXM_jOqOuJPycfpPt04tKSeCtfMNZwDod84xOBS6CeL22mWTqaU0t5hcc72I7hHts_2Eh0V17MbdWzgOP15l7hWVo8CZhZVn1DKUoAYIBsZnVvo1lpl-Q6IqeNB5wUAu2O1c8-wDLqFoNTuQu-xB-X7zirzaggUnHVBkGu4iuyP4GiA0GSKw5bltFNbfMpweGTgLwcCnK9SlxZOlngB1_a1PEppm_5OQPDUZTX3TSFHljpl0F-sUFFFT_MjuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxxrXuShJmNz3tLvZyyUz4au4Bd-Y44_ePgLHqDd9qX26uJauHWbL_mRfAPdxmmhjjenvIWg_Jn0bcoLgT3PqIrNhikW1xgI4GR-OQcIgLYdPxiY-rYAQPizUGOMnVy5tXxcO_bqbaRPAtzMta5xt8Am6h93XCl3vQ5nivSw-yy8LaWvZt8l94_cRXxeErXNj1rUvvPsu0SJazCxpld_r-E_MBtL2EvB2Z8Ojog2oxNDjb-68ui0XR1Tq3nsRWT11ZjDsZpR7kYXDeR6LeuFs_BR8vn-TE0SQOns6Eftxm5M4M9AvbsehuBltG_WV-zhOPCBuZGfKVOBIz3iUrzsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ivbaz-VEw-AymfnvrL1aslBAPFMK600pMQ3TS7XC2tnZlmec48kfSWwCdMYj86UNWJKcx0S96H5SNB76a759UHDkJwRnQFrOU0ZVOEJxvfJfB_gLKXCQtMLk7fr_qEG7giqjvtTunldUOMwBJFn_WrjyGCbkxUbpl7WmWHTFuNUryNmotY0EOGL2paH51TDpXKleLbqneIvfEBGXtZzPLkh8zmU_W-owxK_G-Us4Oe0zO2hI3KSsIEYhPsrqt-RIqMgmbot8E2SghpDRWkqFladfTa15jnLD2VC16w-cPkGtJsO2ST_Rz649s_xy9fkuKlI1tW8AuiZ_jDsPec-VIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=q7xD1mMmD9pjhzdoarSR807EQCY2ydAxAeVg6lr0jtLjpYsy_SFBJURbbJqUZci85SfmNR3LvP6XFs5rcyC8zDrN-rViwXQdRIOk0anJ9JEOH5xJhbVxU1TjCpaXZSNZgmXSeffYorOKsBOTvpzniveWis6wa9v2PidHPpHzmIlLk17r09RXjEl2JRtehaevCN8tftlEsgE8iDhQPgOedAY34U9x9IHU6pnyOLYwi5C0DIFYHq-txfEdnJJoN0rum79Asj5OzbVnvLeEdU1ge5feTCT4hkP2NPzbbMzq2yqPfqT0Nyyk5v-Hf9Ia-eWHsyqSxgZXUyZX1OqtcTK1Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=q7xD1mMmD9pjhzdoarSR807EQCY2ydAxAeVg6lr0jtLjpYsy_SFBJURbbJqUZci85SfmNR3LvP6XFs5rcyC8zDrN-rViwXQdRIOk0anJ9JEOH5xJhbVxU1TjCpaXZSNZgmXSeffYorOKsBOTvpzniveWis6wa9v2PidHPpHzmIlLk17r09RXjEl2JRtehaevCN8tftlEsgE8iDhQPgOedAY34U9x9IHU6pnyOLYwi5C0DIFYHq-txfEdnJJoN0rum79Asj5OzbVnvLeEdU1ge5feTCT4hkP2NPzbbMzq2yqPfqT0Nyyk5v-Hf9Ia-eWHsyqSxgZXUyZX1OqtcTK1Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=I_CzWpSbZ3yHYZZ4AqTKb5rjvhfIXd2Rp_LSil5JmjJuYmDxzyaG0AvXz_VxFzFboSACK-55arAdT000GO32odeTOmoyxghypZEtKx6nM2ZyfM82KORhx6_1PBZdUthakY_bOA0qLgIKQBUUAHzttgg4aAPigYCWdPW71Z20x4wOQWtAuk9G3M3fQRuA7W56ZXAL_sO5GFAWKZBL1-xYWkgoT81V17pMxjn9xxeUolAztZCMinYwOGBKanC0F4S1RekFLk_oSkN4TSBG6kroR9-qeZ7vaNZ0TtUwz06KD5eDUnGXCejzhz_LwG4Fxml2omsCmpzvaUdPezAfW51-WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=I_CzWpSbZ3yHYZZ4AqTKb5rjvhfIXd2Rp_LSil5JmjJuYmDxzyaG0AvXz_VxFzFboSACK-55arAdT000GO32odeTOmoyxghypZEtKx6nM2ZyfM82KORhx6_1PBZdUthakY_bOA0qLgIKQBUUAHzttgg4aAPigYCWdPW71Z20x4wOQWtAuk9G3M3fQRuA7W56ZXAL_sO5GFAWKZBL1-xYWkgoT81V17pMxjn9xxeUolAztZCMinYwOGBKanC0F4S1RekFLk_oSkN4TSBG6kroR9-qeZ7vaNZ0TtUwz06KD5eDUnGXCejzhz_LwG4Fxml2omsCmpzvaUdPezAfW51-WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=exVJt2f3bokOmq9GtUOLU1i7D9XmOkEvQObdngqjs32ylY36BhYTb05-FzpN9KpyFQSXHwk6PemlVum4mKdRat69il82H0vACEkzCmWZH8eL2G2b2UOcQDiaVxAJS9drJccq8ntyzbmxzZRXW7JkVrion9T8G0SIT59Y_29mJZDBpMa2RJHDv8qSc-rqsw69lmUp4mwzWUnbwNE03oEGWbvnjL-BwtOadeJ9E_WDi3O3QlGl_DkzUAyxNMvdUVKJFJw5JgUfrCwDvMHNhoRadew47K30nRXX0Cmx2pjK3bZxGSQiDptHpLR7_G-Mpq6NZvM1D3gB-hrEcOw9-pqfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=exVJt2f3bokOmq9GtUOLU1i7D9XmOkEvQObdngqjs32ylY36BhYTb05-FzpN9KpyFQSXHwk6PemlVum4mKdRat69il82H0vACEkzCmWZH8eL2G2b2UOcQDiaVxAJS9drJccq8ntyzbmxzZRXW7JkVrion9T8G0SIT59Y_29mJZDBpMa2RJHDv8qSc-rqsw69lmUp4mwzWUnbwNE03oEGWbvnjL-BwtOadeJ9E_WDi3O3QlGl_DkzUAyxNMvdUVKJFJw5JgUfrCwDvMHNhoRadew47K30nRXX0Cmx2pjK3bZxGSQiDptHpLR7_G-Mpq6NZvM1D3gB-hrEcOw9-pqfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beVPAiApEopMGF4rOvDQO5Iy4T6XazopHR_XOGdtGki7_ba-_8n3HeDxNhyJViftRniQSEg7arLpPJqnGtDPd3ybxJhBk1r7X2RN1FeaduJL_ZBO2nry8h7t2kjkSwzIT7_Z21dqkuZr47qLBKP2i5mBnxFPF9nSz6_YsfMaAC-3xfG6C2DFsrtUwoLhB9VlDvEAJ5mnsHBbj1MsxkiS2_aze72LLY55CH2S2G1AVn2qV7YJuNBVAkIeceY0P_-WNJf_Zvti1QkCTrjf96bZvuXwa89KZVUiyMhTZtn6ORqC4ixy7LWfwV6BLmNIyWcnX-GCzP_NSv7av_oxDkmPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhMTIdAmkMqfHKU3PW8U5rReDyhSjJE_gfld7AHgzHlfIxdFZvzf88UDuI91DJZD1AY2N9EAWodefj06PBbmUI7tHak9JKv1rS12ZsJmBKS-3Ezo38gc_aetnCEZVUG8xY_Ddy4l36LcJEGuNjjuBT64xOeMUNQivYa55u4w0xTq5FH4SJz78xE9K61RzWKdVK1Sv7XwRnf4_IJF11gG4s5QrnPtedVuqFN_snDmhJBqSs6HfnGSkkjnpGUQlDq8cs4DqfLPH_JEJR8ker8-rRR6bdDghxYshRcek67Nv0yf7gxxB9khAV_TTqiGz1SXcoNL1F6iXTosZxuDFQq73w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXEXfwFjATaGfLjUSIbFdHqJP2B5TBhzLj8kqpCiOlA6Z8ao3iMqJ38urwy-ZaLSYgdzQRxIlHWU4Grs16TOH7aNj7izGX2Tys5HhEEblmiCsTj-tyQCPK-nnAyvkOBnmc_PaC7B4g0PvorM8DtpuE-agcBDwfylwaG-bqISBc-T2to1blqEw1m7RB_O1OuM6CtpKBhh25lNeTwkGaL4EhKoeeuzlNHDLkWS2Ivyr8GcOT5pRxS13jrQiy_81QOnQ4wi10-453wppI5xIfdlbJWt6U2NWGXWGV5eMsYKyukKDj7EAWCdmkdroza91HKhSjvOaoBLs2F9YyONwAUMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXZ0p8Ns0cotKh5BXpE-sCNpINjxczMO5QmukZ7-a8IO-EEbfaoVObTRjesu1cgbahQaka0yesI8fhVdOwMoE1HmB8AQOq3Ga81ymyKObGpr5rl-meIFtQPIHZs47GCXlrl9ITQCXcX46ySQhEjzmsB_7TiyBQokKpwPj1skWXuLke1RNa_tJ0VsEGAbtsLybmDeIrcuru53ABeVC2fo6XN2jQSWdq7ws-g9EBe-aCLlAGubpnMZIyVOeY3mzoSDiWgn7_WcZ2Rw_tRmgsnf1_SAPKl8iyMDCRvnZqnsV4OwnogURiC8Jwd3z9khxnkILnuzU9P0Ajs9mWF4AY6i1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jg7-T67bIAo4iejqCkfl0zKnY4p8PpL6xtNijp70FJRRvml-eili0OPYUFlcyTEaIBM4bUfr7PC92QsHQXoULkyhGgEuvY9mUyid7pNT3BLHcCJH9L95xGfwj2LQUgGHcgnx5Zz0yu5yIwtCrrJADyCcOsdOwUbVopmBlX7RDDWU11K0LtnT3ALjcnACmZQYU5_fAfeAvj6VvYPMgMWoAbsRZd17-Yrjg5HOiPxZWvhDnNTZ7xk6sMtmSEedfHxRaRZWqvoy7ouH2ffIq_HnGfoFy98j9kHNmlVMtoE4v0ZBxLCfhLlPbqqfw3XIOBoOlo0TVC_DaJ1ANHZ-D2ZNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uj-ooiZaQ21sUnG32qOoBgm7_re_YIeWx0I-mipD_8Yq6xX3VAH_EHbxaOt9EUfkSVfg0cT6js4WrMV0zmwMwDgKXjrmo_Wrp5XcaR7Y7S0hNnT5hH6i9DICWVpHz8RL4GDpDMfzVyjvCTpJ-0l6QgSo8MDCN96nIzh6kD4syj3Ngb5Gycb-DCLaboe3PggoP0TEJxYmSmlbryAdHwdK7ju7guGqwIEXIBjie9vdc7sfRnm0bluyMyvwD7_eHUJxwYXvoNl5RWqw_Rgjw7LJ-PifZqAr2839kV0z8yNQzKZ4bgXpuyp0u6AF7cAGYcv4i1x7iRonViGTF_H-nL6lrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHssResokAC7f81MYP90ZC6gAgZcRLUSvYdSxI0O4dlmNICkpEKyl7u2idikL57ilbPbFZXoSUF3yaQ75nPB-XI-1JUTTTSUjYYwf2nGroVgpbRV984o2pfe0o3hjlJ3BCwEm9sheSgeOfiU3t0UrkG6FrxAwaUAZ8N6d9kkywK-8Ch6x5CDwvrr36aqXqAbbToGOQbiknd0_FijdqYZcQ5gYS9Khqzpk7Y_xwloh7cPPPe3uw_nngeMgi3Oeza448XR0b9EtQ-GvVeaBkmAaNghGkDdj6j_DM07qrz8wnvAJn28retCvfZ-7LVzidfOi89-D5q_f2QfErkZUjlk-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
