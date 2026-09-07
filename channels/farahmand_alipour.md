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
<img src="https://cdn4.telesco.pe/file/myTIqbPJyGTcU4pBZ1YeTzrwCuKooL9Xi8IT73OQHqQovWZ5ttQKSvwOP6Z_vzAaWT4bD5QDfdfepMPct8ghDBdGLH-GVBAlScp4K5tRuH4FxVEUrZyZ9cELa5JlTjKiH3PBlN6Ku3f9W5gS4rhlX2FAE9GMjC7VG5lHEFkkUvknqg7zQNpLa_alo0TgVeaP-CG6WUFmzLmoZONCUsIeMIMnhQ5ZdvhZ71hw9CeFt8rUKGMiDghcGI25qnpiUc2HnBOrrZYH3KPtwtiqj5I1woXDK4A4DaPiqKDuxI8TOKrjJ0SDV5j-9PHxkCAmhXASRczTQvjNgpvey8Rp56zsFg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=vEiGIiPz96dDLqQrJfKR_gyAKnuefcMypghTROs1KWeP18h8nwbFoc8YQsaLIxyuF6qmGwjfCPZCZcQE_g0RgOZ_nAjwL_2S2b0qoaJy3FlZabItfh3gJ3J_bQdc9lieo5svvd6b7VIDcVzd_j3g4ZncV3FCuIfNCxWWe5wm_YvaSIrcoUn6E8NkAwbfL_DLd8ytEDtJWYKwxSD5jah0H25EjrOHjRq71VKzpkwYwz0Jdnc-Qh-p0hogji_MDYTxVs5VZ3-9ryBKy-y99S_hyJuwCNwLpWOd6KJ_M9lmJxoQo_BV3G7vuPEOyfzFWGKwFAS8WHhuJ_sBl5bIhi3LtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=vEiGIiPz96dDLqQrJfKR_gyAKnuefcMypghTROs1KWeP18h8nwbFoc8YQsaLIxyuF6qmGwjfCPZCZcQE_g0RgOZ_nAjwL_2S2b0qoaJy3FlZabItfh3gJ3J_bQdc9lieo5svvd6b7VIDcVzd_j3g4ZncV3FCuIfNCxWWe5wm_YvaSIrcoUn6E8NkAwbfL_DLd8ytEDtJWYKwxSD5jah0H25EjrOHjRq71VKzpkwYwz0Jdnc-Qh-p0hogji_MDYTxVs5VZ3-9ryBKy-y99S_hyJuwCNwLpWOd6KJ_M9lmJxoQo_BV3G7vuPEOyfzFWGKwFAS8WHhuJ_sBl5bIhi3LtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=QI7X3kb1AxefL5WMDExgNSQz_Es1q-jLnt-YGvj-0ykurVH3K8u583zZdJBpg8FLGVu8IHH-sdR9tiCnfhrcpigth1QaAekLhakKUE5kU2Rqlg-uZcm1UKbYh4iJOsAOM2SQ6-Vq7dUt64uFGg_pg8lZU6SN1oUSsLTKGBLV6LbOITUAaNgVEAlQrWd7qLqNnjtRixjdDiem7prdqskoDp75ANUpjlWLnlEq6-B0KSk6Z8MOkL09WXOvKfQ4hrreYwvoHtOYkwuSf6IBUqh1b_l9dAtEqTGVglpOxqzkJdxLwYZL_U-jqJjlWcfYf_AsIoSKR_PDbhlioO2uAGAzkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=QI7X3kb1AxefL5WMDExgNSQz_Es1q-jLnt-YGvj-0ykurVH3K8u583zZdJBpg8FLGVu8IHH-sdR9tiCnfhrcpigth1QaAekLhakKUE5kU2Rqlg-uZcm1UKbYh4iJOsAOM2SQ6-Vq7dUt64uFGg_pg8lZU6SN1oUSsLTKGBLV6LbOITUAaNgVEAlQrWd7qLqNnjtRixjdDiem7prdqskoDp75ANUpjlWLnlEq6-B0KSk6Z8MOkL09WXOvKfQ4hrreYwvoHtOYkwuSf6IBUqh1b_l9dAtEqTGVglpOxqzkJdxLwYZL_U-jqJjlWcfYf_AsIoSKR_PDbhlioO2uAGAzkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf3duywbe4OA2wuOP_lLtgEzjgUeP_ELAfHYaeZ84YKHB2v859H7YGQ4WvxLjeuX6u5yhLrPOCGRWJ-FdMsgmH_zaqLj7cJZZPWiGUXrsKPda_OZKyxFEKs9G3yqN0ojPw3VAjgNJ6KmLUnPFLhBcNvxED5v_u4fUtNKB4zz7aZJTlzAgzOlb2eJswpN8HjvYkG4hTiOz6Sj3sZeYY6eWGOOPvrx-F7nnYyjTCetTmO6rkyNvIIswDrXNViUkuycLaNF4cIvmmgq-HyVVvAf_eUmrcXJdPWkPm9pb1_cFD6qoOdg99MzIkaz6C8AQ2nsEwlNBENlyBWItL9dFx0nWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJjValImkDxm-veeAD2RE8kByE_9sKjhGJB1e4dLxUIUxTaj9ZVkSjcjHUcwqnQv9YmncHPDVHvIqwHMO9ysXWzgQG5YTp20LDFI1UedHyLifyUqr2yt1PUGba5H1FH-ODbQ_KS2q_ZGhaGHB9g3mUGvTxSHfEZsj8G8U7e7tqqi_xWb8c81RR76WPH9ByOMC2c8gB7BqmsXjqhW8yn7L5YAE40ieIdtF8XQOioflMVfBToG3jP_s6T59tmq0KVtHKx1QCuk2U84XKh2_WaUnB56Ibz2-wvYWnqhKHLLXwVVE19vZpJMb5HPoCS4YAo5di736vRj0Eea7CmW8r3zuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=TxrmNaSF6ug9lMAkZ6AJ_vj97cXe-zVZN4Wa_xHsb5ecpL6QPAPY3cJqat0O4TAtALbcrGd7DEIae_JqS5-JUTl6yryk9U051k1naUkjpelCThwjaCYRPcO86LptFWHoewu0CDk5Qhiadu3m3ssimfyXrZt0VgNIzZYw2wpUE8shxtumPtJaM9dJvYNjATjmW_j7YgZfFaAQT5czH-eJtC6SuyBKK-UCbyL5xIZx15oK1H6kziV774HYrFO7y-aLIMEypSbWEua0wEA1EZtowCetWYhd2YBIEvR6xAtQhTWKmVop7hFIUfoxLK9brqnYZ-1NNHhENDD-QzifS7GOzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=TxrmNaSF6ug9lMAkZ6AJ_vj97cXe-zVZN4Wa_xHsb5ecpL6QPAPY3cJqat0O4TAtALbcrGd7DEIae_JqS5-JUTl6yryk9U051k1naUkjpelCThwjaCYRPcO86LptFWHoewu0CDk5Qhiadu3m3ssimfyXrZt0VgNIzZYw2wpUE8shxtumPtJaM9dJvYNjATjmW_j7YgZfFaAQT5czH-eJtC6SuyBKK-UCbyL5xIZx15oK1H6kziV774HYrFO7y-aLIMEypSbWEua0wEA1EZtowCetWYhd2YBIEvR6xAtQhTWKmVop7hFIUfoxLK9brqnYZ-1NNHhENDD-QzifS7GOzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6x5uhk61jmBjpHnFvJaGTmx5ZYJRNf8lu2Z1I-JdraKkF0ebA1wx4Dng5WTzl4-PFo1ecWsxepGFa0-xAVusjbaLQ0xrBkRjD49kfl8d4VhJC6VM6SNAvzqLCAb-HzTv0EPDHpLV_lykigIu9adANoZqfoLwH-xCiLLPBn2d4kAfI4444nJQlTl_WZGm0JoDvZCZaeq94rilOM91izsiqWizBQmL3boHrOkRaQI3-BbI5zLarF3bXkpR7JPGYjEW72zj51MMxjuUIPPsVjb7h9_Qn9sMw-fmpsZGtTLo3OF6FSCDvlCrCKLG_objQKiok7LbTsfNDDEvQN2GsKiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpLoRmWsNBY-DCxpFKzRJKWrGgDaFx_Wl8wApnELlzjtHho24X_zUkYcYmDJrHlol0WG_4mv9qPRQ2aPZYj48mPK0_8rDECL9azB6EJRYNpBRMr_0rQrYoaxGCi32SDgRzGaDRHzjybM39qxulTQx8vkAm6gknv5RqcYJBQLj6Yyl6S8TIdLAK9k6_BbyEf4YBlhT5QtB7KJeZpGYXKUEragMhH7ch-mwye5RDJFwsBqUUDc0UROnLkTBTyi7bNu1-sum0BJgcGh14lVBafjOLPQvas-4Zw5Ptan7RuyOE1psUGx-Vpx5N82KLT45Yi1K_GAAcTvjYoPWO6ymaF6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDNswknBz4ZT67LImWh6wcADlsqSCqP-ljezuM6XZKShMhw45S-55Bzen-SAIjBfv0C6rnNxnOramk4ineH_nRb1iRmzh3YEadoEk4rOeXinEnO2bs4V3QuNMrnuiYybRGleuiq30khtUcdDPz2EdZajWaNE_LFT2NFyFB9cb1eDOGONUbruWjYFigrbLNyKbgmKRgk0d2BCIkgPz-LIgKwWUhJ7lfWXh8xyjsLJh9ahEnatJxTsswMLDhMwwJZy5RuxM8rC1JdxnTyHUVlExcPexSUaPQd59GQohCUaBguEV8JHPvwHnbGzoRsSleV4yyKzsY4Hs26jsQ4aqlezhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Y9edIM2dWrv0AAEUkP7OJxxepFyJ4cCgfGFABX3cQoLsQcJ9OsFbGmhReSOor0uK67Sdm8gnvOnWS8tncbRPhgpP-5CGxIHeotSAMQEifYZzAsSUq2udycqPc-5WMXZ45Z3alJfC01-M9qvXPZTuzdmwJl7m_X4bnlKcCFE-o6K4Zk2fdJtHwvu_3gfx0Yw_0mxr3uC5Ca5qJAK08aGfSCrpL1zs1Nvqkc2iCCVwOTLgxKKNZWs9jE57mcNxeVGB2fXBu0IS3xIuWQmRvOVI5j7PHsKR78k7EB0L4jIQi-Y6YhUcv2diEBdklip-O2VtLQtnc0zAzVVKxfCoSdHEHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Y9edIM2dWrv0AAEUkP7OJxxepFyJ4cCgfGFABX3cQoLsQcJ9OsFbGmhReSOor0uK67Sdm8gnvOnWS8tncbRPhgpP-5CGxIHeotSAMQEifYZzAsSUq2udycqPc-5WMXZ45Z3alJfC01-M9qvXPZTuzdmwJl7m_X4bnlKcCFE-o6K4Zk2fdJtHwvu_3gfx0Yw_0mxr3uC5Ca5qJAK08aGfSCrpL1zs1Nvqkc2iCCVwOTLgxKKNZWs9jE57mcNxeVGB2fXBu0IS3xIuWQmRvOVI5j7PHsKR78k7EB0L4jIQi-Y6YhUcv2diEBdklip-O2VtLQtnc0zAzVVKxfCoSdHEHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=EKa6epKDz5UJAcJ1H8DyhBxZYCxWSRJgC6DZakgs3FWcR0FNqX800n9NF38Xp-AmuNTtc_RzoxoBHvte0LcCAjE1QLr9TdXtB_c469hndTYKCNfo4QqjD_9iPKlZGyHPaL9z2_hOnMX27LLF8Q_yubl1WAlk9aDriJGTMWzABALXJfNHt2FoItJijyh-AiLkDpYcoWU-xVY7aedFgfarK_x56AKEUh680_Lj8nN0qH6HLjtH-7urr_ubCUKqIYyCvvQBOfLNT1hUxUY39fUynTmKDAOgPpifgOj1yrAMooXjDkaW-5luy53rTq17kub6Ls7yTqyHfx7kkWzB6CecjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=EKa6epKDz5UJAcJ1H8DyhBxZYCxWSRJgC6DZakgs3FWcR0FNqX800n9NF38Xp-AmuNTtc_RzoxoBHvte0LcCAjE1QLr9TdXtB_c469hndTYKCNfo4QqjD_9iPKlZGyHPaL9z2_hOnMX27LLF8Q_yubl1WAlk9aDriJGTMWzABALXJfNHt2FoItJijyh-AiLkDpYcoWU-xVY7aedFgfarK_x56AKEUh680_Lj8nN0qH6HLjtH-7urr_ubCUKqIYyCvvQBOfLNT1hUxUY39fUynTmKDAOgPpifgOj1yrAMooXjDkaW-5luy53rTq17kub6Ls7yTqyHfx7kkWzB6CecjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=JzwKTqWO3HcANkX-jZr8Mx5ozzPAcYPGWyPqbelxJkLejN_ffHGDiQUM-uO_juLWYTNyAeAH5K7JhZubkOKsCeUYYyHiPeqrKlXvh1ITy7HBmeK0A4sRBrXrv_btAqgex0z_yjrS7Neq5576mgSPA111NzpSvIXz18XLRIKlKp1bpx5kiRDyuzGO6xOzCLlg1eeQkMwTxM2ubRWKqRXmRX84TStxkT62srWsCmsX6_KMKUOUTHzjio646PTDSyJJLhsFKHtMV3OsDCpGZSUPZVxvWnJeuuosXx8XXvHQGYFUZA8OFXjTBxWr7rE6pF77xLcKH3khYPo7nfc5CeX10osIWl2WCBiJgEURMd9rgDCQ3JjiU6q4sUxAPmE_LwV8aepYcJrZYNKRGur1rmyHLrlzeH7gGa2-ZWP_h9hjNI42TJZ-md1ddYQumyctUINu6Uxq6p-ENjv0WeBo2jryooeDApyVSd1wymR3zIE4KJfsrjx76Qgz-eetxkFXXnlYkwUAWKJw3seXA6e7j5kTlYPMgB_dscaHeILLof8CqqMAWRUZukfH3UciakyXP09r3tQyUMeUc_wmvoFbLbHvKYujTqwCR7FdVyD77QpTOEwNQsyIRSUml81ieGV2-WECnbXAQq5cIOgDDDWMRF7epcVFMXet_H9t_CwsTBd3g9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=JzwKTqWO3HcANkX-jZr8Mx5ozzPAcYPGWyPqbelxJkLejN_ffHGDiQUM-uO_juLWYTNyAeAH5K7JhZubkOKsCeUYYyHiPeqrKlXvh1ITy7HBmeK0A4sRBrXrv_btAqgex0z_yjrS7Neq5576mgSPA111NzpSvIXz18XLRIKlKp1bpx5kiRDyuzGO6xOzCLlg1eeQkMwTxM2ubRWKqRXmRX84TStxkT62srWsCmsX6_KMKUOUTHzjio646PTDSyJJLhsFKHtMV3OsDCpGZSUPZVxvWnJeuuosXx8XXvHQGYFUZA8OFXjTBxWr7rE6pF77xLcKH3khYPo7nfc5CeX10osIWl2WCBiJgEURMd9rgDCQ3JjiU6q4sUxAPmE_LwV8aepYcJrZYNKRGur1rmyHLrlzeH7gGa2-ZWP_h9hjNI42TJZ-md1ddYQumyctUINu6Uxq6p-ENjv0WeBo2jryooeDApyVSd1wymR3zIE4KJfsrjx76Qgz-eetxkFXXnlYkwUAWKJw3seXA6e7j5kTlYPMgB_dscaHeILLof8CqqMAWRUZukfH3UciakyXP09r3tQyUMeUc_wmvoFbLbHvKYujTqwCR7FdVyD77QpTOEwNQsyIRSUml81ieGV2-WECnbXAQq5cIOgDDDWMRF7epcVFMXet_H9t_CwsTBd3g9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=N-NILdyKEyXNSYvSFx3rFgVsoXruAkjn_yBx5GQK-cjK3kCWuz_aaoEjrxgYypiM0sYo3wzjEyroyr_wZ5CrMY1gzAsb5-yE3IKG-pRKk5RPRYqM6s7GwhfhBgfrh9qeKEU3QH0UBXth0G99ZbbZvcCHED0yeHe3kajyZpAA1x6AWiPpWZbfDuI5e6gbJ5wjrLepknTEqhsOuPrPGyAjR-8JxAzFAcrk6OlzlXKhFN82Q24w69wwCXxp6WX6zfhsJg1xOyN9Q3WQR376iSo7pu886EL8V6sUEMWaMQhC4L7g8JacQbcnMvL9onyRw1rLezglV84Q7RaCrWY0mK3WNlHbmE737_84nb0FrF-2XT7pLHgpnVsRv9KKOn3hVOuLrLcWad23XkixEirNpF2Ewp-JUHwB8xW8gWpNZ96OcwnOHZ0mV3hzxP0_d1TDxaE02LowdK-xtu10Y-Hw-hwnqCdVdB7Tvds-LhWm5ZXbqQ02gWG_uPK4ll_-yewtBiSHcqGH8XceDIh7lkrJilQI9xpjyPRuhbbLECR_rCZMLYrsnCjZMa0LtJfvrIdL2LfLd4DT9CNYugpO6bTBWsFGKihPLvv8rUvPMUoJQRMtj1ILhIAnnwL7p5dP2dbbKtCIolTrRQ1PhMJq6oDJhVn3_tkL-QLjDu-Et1zulxfRLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=N-NILdyKEyXNSYvSFx3rFgVsoXruAkjn_yBx5GQK-cjK3kCWuz_aaoEjrxgYypiM0sYo3wzjEyroyr_wZ5CrMY1gzAsb5-yE3IKG-pRKk5RPRYqM6s7GwhfhBgfrh9qeKEU3QH0UBXth0G99ZbbZvcCHED0yeHe3kajyZpAA1x6AWiPpWZbfDuI5e6gbJ5wjrLepknTEqhsOuPrPGyAjR-8JxAzFAcrk6OlzlXKhFN82Q24w69wwCXxp6WX6zfhsJg1xOyN9Q3WQR376iSo7pu886EL8V6sUEMWaMQhC4L7g8JacQbcnMvL9onyRw1rLezglV84Q7RaCrWY0mK3WNlHbmE737_84nb0FrF-2XT7pLHgpnVsRv9KKOn3hVOuLrLcWad23XkixEirNpF2Ewp-JUHwB8xW8gWpNZ96OcwnOHZ0mV3hzxP0_d1TDxaE02LowdK-xtu10Y-Hw-hwnqCdVdB7Tvds-LhWm5ZXbqQ02gWG_uPK4ll_-yewtBiSHcqGH8XceDIh7lkrJilQI9xpjyPRuhbbLECR_rCZMLYrsnCjZMa0LtJfvrIdL2LfLd4DT9CNYugpO6bTBWsFGKihPLvv8rUvPMUoJQRMtj1ILhIAnnwL7p5dP2dbbKtCIolTrRQ1PhMJq6oDJhVn3_tkL-QLjDu-Et1zulxfRLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=MnrpiL5WvGjfvfl2fV29F9SanSukHki3LYDl7mKPcgVdu0_k_N4Edd4Hl3Af1cmZgKfajtI5-zf_vPGmgF9g4PzGuAHNJLs9qMFPRKdD28IDrjQHPGUMVB4b0k2AogDElx5MwUKEjdcMql5yEnXnstDTnv61wxU8Bb887upWKTEvtqvPNtJX4DP83JAo29elx5Zj-JCaY1w0iU8vCAUoWUh4wrDZLUO9n9Zyx8mGX2G4_-SNqhh9DNew9IJ1n9n_OmujYCMgEakBxORFKfTuEwv6Uwu5K1jgkSw_e357JoqpKNGJJTjYjO7Kwm6iWPZ1-i4-GIedIqh1myZ5CxUhEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=MnrpiL5WvGjfvfl2fV29F9SanSukHki3LYDl7mKPcgVdu0_k_N4Edd4Hl3Af1cmZgKfajtI5-zf_vPGmgF9g4PzGuAHNJLs9qMFPRKdD28IDrjQHPGUMVB4b0k2AogDElx5MwUKEjdcMql5yEnXnstDTnv61wxU8Bb887upWKTEvtqvPNtJX4DP83JAo29elx5Zj-JCaY1w0iU8vCAUoWUh4wrDZLUO9n9Zyx8mGX2G4_-SNqhh9DNew9IJ1n9n_OmujYCMgEakBxORFKfTuEwv6Uwu5K1jgkSw_e357JoqpKNGJJTjYjO7Kwm6iWPZ1-i4-GIedIqh1myZ5CxUhEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAWSv0TbJVAS3ZbPhjDzTqgCYna6_5OpObGhDB80OXhfKOn7LVisyvQl3SPYmnT3J93mZ0naMgAuVSTfuG1pGPu6IZNLJ4e9ZJaPT1X6O4oqJySmaSZaQOeQkn84mvS-h32g27EKvRkVQNit7HUS8BHZpAJNmoSaRdI8zANz9WZwV3qdeTClRVy7C-zs0HqvF_HS83PcHHJcwKxgGk33KHKAlXNc-4N7AABJk4FM6n0m_fIATVTybFRABkqAX7XA3nG_6bMc7ySRAgbSgGhAmJFppfd3nLHCYXuswVthwfh51kHaWnYDJmudHWS0_FfAYU4Qqh3aKf2opeOsubW78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=lWyk2RJKWJ_v5n2obwkeKtsRJ3UkpaX0SojjMD7CKuMDD6_hdxcKKD4kCDkq6xb_LWh-yO4D0Trr5YJkW6pKBKLRtmRndDh7qc8yJqJGl4UDoJ-QOqiyyEgkskiAdq_Xe5im0cTzKZDHGkFpw4Wud8kpIdPD3b3HEbpY-Jp3yNC7J8fYYgwpvPu3LW48-2PiGgbLZDDMjEtIw0LL4AXD6vtRcm_xy9osvhG9Wlc225qkgsXVWm2369vt2wbDisMCtylMsFkixT5_dg5QIu6eGwfeN-9U8SToO8Z1qv3kEGEUnt_Z7GxP6uV0iTOq9qmZ-tdFjFx7Cc7-LPhAm3UlwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=lWyk2RJKWJ_v5n2obwkeKtsRJ3UkpaX0SojjMD7CKuMDD6_hdxcKKD4kCDkq6xb_LWh-yO4D0Trr5YJkW6pKBKLRtmRndDh7qc8yJqJGl4UDoJ-QOqiyyEgkskiAdq_Xe5im0cTzKZDHGkFpw4Wud8kpIdPD3b3HEbpY-Jp3yNC7J8fYYgwpvPu3LW48-2PiGgbLZDDMjEtIw0LL4AXD6vtRcm_xy9osvhG9Wlc225qkgsXVWm2369vt2wbDisMCtylMsFkixT5_dg5QIu6eGwfeN-9U8SToO8Z1qv3kEGEUnt_Z7GxP6uV0iTOq9qmZ-tdFjFx7Cc7-LPhAm3UlwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=UJSQB6Oe9fVGTleF6r7oFu7Kjp9F8NqrLSTszaVl_I-B-tafoXhcjwgvOU025mhyKqnRS0fFucjArK7xuyDK9sWxuk4NuubRzRaqjEaDUVlFErLIp2pWauRuPBuO7W0sEmffH8hG3K5U0_T_k0MBv30oTY67zsmX8jBiC7jtjuuJjEVjjRLn23BhjDVzWqsHLCSTgXun09snfMNEHJPP5LvAP1rWyypEZlv2HhQfL-Zeq8pxwTWFBoWXhetWaFleKhd6VUWWjMu9Fyml1CSDmE7ZUQLj_sHeSUs8KsacShbuPTIPIIW0LTGfwIX_RAGgwPd5I8e3OywEMGUQ3RlWTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=UJSQB6Oe9fVGTleF6r7oFu7Kjp9F8NqrLSTszaVl_I-B-tafoXhcjwgvOU025mhyKqnRS0fFucjArK7xuyDK9sWxuk4NuubRzRaqjEaDUVlFErLIp2pWauRuPBuO7W0sEmffH8hG3K5U0_T_k0MBv30oTY67zsmX8jBiC7jtjuuJjEVjjRLn23BhjDVzWqsHLCSTgXun09snfMNEHJPP5LvAP1rWyypEZlv2HhQfL-Zeq8pxwTWFBoWXhetWaFleKhd6VUWWjMu9Fyml1CSDmE7ZUQLj_sHeSUs8KsacShbuPTIPIIW0LTGfwIX_RAGgwPd5I8e3OywEMGUQ3RlWTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki5P2xFLNeYI6or43j7Lu-K3UMjHnjVCOm1TaP78JNHAyttON2Uzu0cVNe-N5p9HmuZCf1k6VUWElu3jBYYgNoeycGs_aKAdJ6sYiHOHHs09XGJdxJmclB8Vk_OXhvV5a3_NB2t2Q1t6LFZQhmJ5R9dAkO-SkhuwljAAAmpjV-FUVT1Llz2DdVYJNReqDtE8Yq78Aj_XYvSeYeqyktCiU2x6EQ9zkMdlrjXthkMY2DfEe09Ll3mpL54c4S1lOCu-a76s5AlhYf2zhKQFhmWt4POUwcnVb8XEDD1fi6Atvz6MJdDCBodZauKfNgjsjx8yiHDPLDyF-egepOhxHyfPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdqjvsxKomVPK93-W9LepCcuOhVTtl4y6aQaOXoTiAeM6kpNVKJKf0xGWsnNfSCqcRDHBVIyEA2_N-Y1K3qnJBcX4oOz1xA24amXyA_mmPz5LgGLNTQQx0mHksLXvRj3ptOkDrUHgqp7l0aGbvICCyytViJ2vBE3uHhcUV--p0EANzEKMsYHjZU3SHUgMoF5fMJEIgGUpsSVyrV3_kCeDx8gM8n4f6AYmnWXciegn1PqPYuJSfzfV9xppT70ZOB4_tOCyifknkrxuHxSsyHJW7GZCUEvK_PAJVffzzWCwvRyhrPfWC9NYo-KY0YNhBi30hO96zGzZDWN7oQCgzMJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq3nVt2H4zNFAWkPA5KiDFl-lsrJ8TIUXvjfKhLnIWm8XtTa9ubUKt_vO6CJBUjD0GFRnR8BRAISCmC-fX3a6qpM9C5w6FBZ0aElkup6GGtKnvd-BAa5bxAvmP3CvHbgNv7zY8jXH808MR9HjLIhs8o3N5tuR7KvBrB-8hrRmMdnobPVztJVl_TOsYC4E5XOibAuu9g79rJx7pr33YvKM5UBtGKn2irtk3lxYaYFOY1gzK3ifNKA8FJZ_aTjsAtas63l9px0LD5P_MHOokfyGcm1W_A4aSclunKS0JWE1Ux1H71zhjaEcod6oqwfTJdBB0mFvfbUhC7sZVgePCddsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTfs0fk_EU8Shu8bnnd4J3dwyUQwnJ3Jm8IlJzTC9AHHPm5dZXkkBUy6eFSlSvqdkPdKVi-KdQFr6Adg6HlXKzlMdl0hCy_uxvnwG0s3UQ122gqCrCQ8-6YHO75p2DJCqGL2Alimpb4_LybFf-g3Tk3TZDdgqP9kkxX7UYUBKPTi8TCBiQlt3osnlcOaBcFKnDJrRHLxJOe37nL_lGEmDcqy0XiUU-pdTS6Sh1bgXqLC9TUaXazSUhmO77cjH2OUw262EgW1p6Qc7QqPNrBcxicVefB9slQgWmhU2p2LX8AR4xONH7phIjbJifqkVgE5vg4UB7liy-5XzTaHZnraiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiuvkHsvknE-ioxnHIVZWzxs48X7fsJrDlC2NF1_asKuARNWrEVIn42n7__UMaCHFP8AR8XDEKeq6fuQ-DyQFlLd6mDz5ukKWGouJWJY6MQHNMjW1WglYIImP20LIf6dc2XMpYlZUUowY5CjcfdFHvNEUmoiuIgE2E-H2xSlxhX57KwCPMSPd1r6Gbt2eS2EA_ltFrGEc46rRnjaw53UcWNruj8kUR_x8QfiVBZXJ0dK4KqY8CVKLTeQfbqfz7I_yxm2wlmjXmA9xRdApaz6dMnPEp36N-6zzaeULagslQMKkLXlTW6AfsJLXgqT0-TSTTFA6a-By9NSIyFSlGOouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG2j81nNROfCM_3UeuQgpJok3x6s8ChQKLo8MG6zFSRL4YlKdOXkdalGmxpfdILDW9GdzKQYpdVgzfnPjkOkTmcoI7ZfbY9vJ6Egfb-BsQc3x63Q9VlLqiWUc0H5YZIglrKQ62IakfocACKyd3KW6wUEnWif9XsFVGIPLO7l4NRtyJnWEUWRSMRl5FYPCjyNgNTDdevww53UiBzixu11bc2oHjhZscSHMituMbSOKcX2SqOsR3hlRBXt0DuJPruYr0JDK-qYIuWq-sEn5YUS8DpVjnRop_XII2D4EEnMjqDj3_eDA-rHsihl3mW5NRRKO2ipOMGzUdWXlp7tD7Nb3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfZsbb_lYuYxIFJYFWevb0LFeLeEHHdRG6fGbX7m_aZ0PZDoUf8moOAhO-Vxgzjh8TF0ElB1aNfYFJbrYftwn2hpCOPbnlZWqBbNjxEt60OY-Dl2kUu3fiBUtG-jW5iZtVu8BxAV5SXB8iotcZn-p5Z9brZOgLZ-x2qrqw_qvcO3gmTJZ70xUzFQwL39u5I_LlwroFarF9uyncCAxlpOX-J8q7XLCo7NNQjc3NI-sSOKcEHtsWK4z39V6PclzZ76hdXGeL8GmBcYMFMQtAqdFUyI3ZM0jhu_k_zs24OmhSOIat2H4dRSuCbB5cF7w-mYZ458Wqjpch2WxPulU40zjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjAWLP5Ce9i7iQzOfmp6Oq_TvNZpH_WZVSO_WUfMZ2d_n83U-txc4IYSEbQl_qiGfI0DhwoVakAMskUO7TEee8Td8izDD-KSSrrhsq6tWCh1da5v61e2a8RHa1t7aGpLhCu7SnRzr23jyuMPxP44C3TdCZgv4x7pFGNUhcV5fQ15M2xkqi6OFcqhRzCwMjUexsiuUd6QxC0Jw8T3RXzpHhv6sU5tzpaoNBzrWLwYpu3gwHhA8xd3gO7TIQuxeYuLQi0LOwu4Oj2DjNss0bOqAr8SRmHC_oLbTHg7coxd4Gnq9K92MUyBkcZQbDBmbCVdqj3i9AucDliB0Wls1e8tPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skkEtpX2mvlQM9QVP2I_mnONtU9wmFdYsO5ZDsjBC3LZy2vW2mB0IgPi3Jwb1b7m0jTyT0YoNUjftwlIu_Yqgpbac7mXVF_pDs7OFicTWELbV1kD5RgBSVaDPT_ffdYqJdVRSFeTvYJFmz9jRWR5ZV9vzCaecEt6OFb2_l6pPvFqZ82RuAaR0A7GhSr2ssyQJhcv2699IDlqfDlcdVCIOnzye6lJWbBp1Yh6k-0B_PjOF5YbqABaVdihSmHuZNN_GRSD_4vAJGS0YHqU_v7eaJarQVgciZoE4EbTKVHyEiVP9087kShDo4KPHqXjKDWBqpqNDT-U3gdpvvynmhezuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqwthkP8pNl9K3KYxAaU8uqz4tLRaaQD9_xN9f4D_T61vLQFw5lWyF2l7dw0bh_caH1s6Bczes7RaCya1qCZhzk3wENLU0hRbaLoU2n2dx60QYncJ7SEKarA3iTN9swbkn9fuunt7XoeG2uJqjo0Q1R6VoGv2BAg4YWRkFAJvDgFphHUGfGAPeAnp-gz-ms7x9moIMvmNLYFklVs2cloHVpqdncecJD89xL7CClUEz75NjC8Px0wnS0BsjFCopdfWvrJ-mpEqUKkMDbCJtvNj1eb_ZaU9AS7AzEL4BYhf1_2DXP5epmAsYs-wCwdz0kzTy9zwbFzVLZKMQ8J_lBkIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=eOWzBs51KHBKcB9UZhIcfiQ88Xzgf7ceqkmiPgTdluicUIWvE7YFM9UmQ4jyX2KlbjmMeBkQ682MyUTy_zpkqK1KlYPKck3NLzDmwYRjV5GK8tIYOeOgFaKEUjoYPloCTXhBHhFvPn_eO0N00NpoMg0D_PO5IZk8uTf3k1_Ps8po_gVr6dpIZX8uS-xsX7nt3jt6eM2KRkUrdF1OG_Y78ES6MYoBN3A2GyVMbnM5H3spCIWgQfhSyl_Ep0XoS6uaLIltIkmlDRTs5ykF4dbSyy2cQoRKX4_URe0ZbEffYuGQcF1FkHu_XCk2Y2lLvzVpkV-rOCBAQxTHldS5Ql1pmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=eOWzBs51KHBKcB9UZhIcfiQ88Xzgf7ceqkmiPgTdluicUIWvE7YFM9UmQ4jyX2KlbjmMeBkQ682MyUTy_zpkqK1KlYPKck3NLzDmwYRjV5GK8tIYOeOgFaKEUjoYPloCTXhBHhFvPn_eO0N00NpoMg0D_PO5IZk8uTf3k1_Ps8po_gVr6dpIZX8uS-xsX7nt3jt6eM2KRkUrdF1OG_Y78ES6MYoBN3A2GyVMbnM5H3spCIWgQfhSyl_Ep0XoS6uaLIltIkmlDRTs5ykF4dbSyy2cQoRKX4_URe0ZbEffYuGQcF1FkHu_XCk2Y2lLvzVpkV-rOCBAQxTHldS5Ql1pmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izaivXX1sOXT0W8BYGjk__3IsFdphYRpm1UlIrAtkvN3PTDzoAyRgJ_DE7T8yQuhEpnDmuXs632IH4Ws3HHBq8YvacySYKZYlMPllSb3I3O8IDqWrMGqRk74OxbWF8nru0gcSb25uoH2tzREnVJu55UBCoGeBcln8s5re5xB4zWykGoHNxtN7TWES60F9koazx2Uj8ePWXGqHiwXHp8oJMiG1e-Sj0LQ6nIW8OyP74RJPQbPaUsMTgJ5iTc-klGZyFI0yJ4iAjjagLn9fOKZ8KVNIykiW0d7-eJzohO4yh16Bh6FGGpipiaHpfQ56a1idfq1fNUVLwT0Vdkw09PTbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0jD8grJOz0ZMIB7HNWZE_AMAUMlQGiSUDMjJDkWvWhLr4IQp11R1iMyGiIWZbIzDPL0n98GcRDvOG3XBThOQBsuh6WWZqV-_yml8FzGzYt6wNkwcwGWRN5bNgYwJ3RhLxwwlcesu0SDG7RmCDnWYt1iF7DqePZiX0P0hou7z34QeaOdBb0dFtD6YUc-4-fZc19oZgJgoN4tnxLOZfprtho-37k343yrPbJsN2ZsffURHUQro4nokLjYzWSZ_Qpb1OB8lP1yOjA5wTfRgAChWZ1IJQ33BbMB2NLTm0Q7W2PceGvIe7ta2RmKFWX8r29n_0pldGc5sXKADKx_2130YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=t54UJ2cITCCGelnEm44AN-Z_qQIBjokN8xbqi43hw5dwvtbLp6PWyFxgkzjRiyCZeBPmLiMj1DYrnCuUmTofdBV-vU-tu3LG_Vd2JiEMABlJ-A0CH2QJPrG9eUf_BwJSLYWTz9B5t42hMrVUXsKHRRP2yWkdM0DedSMavQfnvqGcH8_KkCn94695kr6z8rG3Zp5IpZv825pOhbWke7kQDdDU6Rm2zmANUyLu-q065b5CVKLorMXLrN9AabT5o0i8Zdi0if1cdtzajNDFp3eBsU2hdfhKL_SujNtuR0HRwsCDHDmnO-8kFuwiTV3xwZ9Ot4Pw8SpcXSs03S__VcnE_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=t54UJ2cITCCGelnEm44AN-Z_qQIBjokN8xbqi43hw5dwvtbLp6PWyFxgkzjRiyCZeBPmLiMj1DYrnCuUmTofdBV-vU-tu3LG_Vd2JiEMABlJ-A0CH2QJPrG9eUf_BwJSLYWTz9B5t42hMrVUXsKHRRP2yWkdM0DedSMavQfnvqGcH8_KkCn94695kr6z8rG3Zp5IpZv825pOhbWke7kQDdDU6Rm2zmANUyLu-q065b5CVKLorMXLrN9AabT5o0i8Zdi0if1cdtzajNDFp3eBsU2hdfhKL_SujNtuR0HRwsCDHDmnO-8kFuwiTV3xwZ9Ot4Pw8SpcXSs03S__VcnE_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Lh48FE2aEXENmh1B8-uoj2VU1ASJfDwGt50vxZeWmiCXrSRxA31CmFI1a1Wtc7aPjtkGpXDLkn5Ll4ftNPsbgz0TpWGY4tagTI7EfsIAq1RJ_XKvbtThP2jaMEdJyjPR0BYxtaZQ_TiRNsVWdXw_o5C2jFU5izqf_4MWpUP2ovFhAUQa3CKXvCuXLcEJSKZ__DtpXopyvJRyQfmsRJZziQNwI4Oc5wyl9hB-x35U3rPt55hV5ODARv4eEYIG-zvolVpwlORmZKUjnqlQ7xiQULsP-XPuhNP-LOcY-DoGowY-g-4LcI622UYvptnDiJeRzeRoRH_Mx9gMT-6m2AdXiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Lh48FE2aEXENmh1B8-uoj2VU1ASJfDwGt50vxZeWmiCXrSRxA31CmFI1a1Wtc7aPjtkGpXDLkn5Ll4ftNPsbgz0TpWGY4tagTI7EfsIAq1RJ_XKvbtThP2jaMEdJyjPR0BYxtaZQ_TiRNsVWdXw_o5C2jFU5izqf_4MWpUP2ovFhAUQa3CKXvCuXLcEJSKZ__DtpXopyvJRyQfmsRJZziQNwI4Oc5wyl9hB-x35U3rPt55hV5ODARv4eEYIG-zvolVpwlORmZKUjnqlQ7xiQULsP-XPuhNP-LOcY-DoGowY-g-4LcI622UYvptnDiJeRzeRoRH_Mx9gMT-6m2AdXiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubwobL6dh6duMc2jX_t9S5gQYWze3j8Lnzkv_YyT6I1U8y4-6aejdaZacg-6QV3D375QMx8h4JCloEsw-Xfe1-UsQKXuUmBCeyyKdfbesbFTj8iLL3LrczV3o2Cmys-sZmudjXHgyv-oqU7jAqv0TZfKMXEt4-Biyvyv9nFkoF0H_9St-NOd8HjblTlcKAJJytrvbgzU70sSwZI7EYnullWKkACyoXGkWspnNI4c1TXV22OIIbUCOQTRX-h32o4LbeGlhZfEh5H-s2SDknUn5-sXNus6hu5AuGaBz8hzPCmSklt22iGPjqernZmwvQByDcPznZbxCsR6K1oqDVun1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsNbFnwUUmoZwR1dtcFI5fzj-Z8Rerw8kuYQqp_pggYHVA1JWHG970rea-ViGRQ0v9kIri-Y3x3_u76_85CePlTL9_j7MxMb1OJgtQR04anaqb5sAX5jIFJOGd5L0Yb_znOrm1SP4bW0G8_ueRW4EVtjqeEbrUslNo5ejtbhaLzyx8H6gacwTeOjePXfipc3YyOF-E3boVnZCPsTx5U1R1MzkT9x7z2ystbE_BqVvAJgYViQVj_pfLWYZ7VJrxo7EYUparDNcMRhGxcc7r22o5VyDXjcfOgtxH-JPOjF6vVbce_w1Ijc5poevfXANFBSvtYhIUZpbbad9aASnFVmKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yqm2Obybq53hmVOQ-SwM2_hh_SSStd_uLc4-jAifHPa1Q65LtjaAWIgQ_QUCJB8stuTfkuVNqOf76uylMMkief3D6YE4HRF0m_uOzdY-PKEM3hGyEfKSQJZB1eOqoQUJ8ZJbDbxq9bovWu1eIYRxiwg3mSCiX6DKImHVRTlWYZMzxneA6hAXKurS6KazgDEOeqgZZ2Y07wSe_tww6CpptRo24-dotivJGGfACcNasy_LKSd9kMq8ch7NG-XJv8c2NkG0E9pLRO53kZeSTKgqDfhHivKoth3rykyYIYbMbRIR4aLWAC2HHauDpy1aAqEP5Smd_e8QNy3wdHYy55pCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhoDs9AgV3lHshxPwPk-WW-Iys4HLA_zMpqI4ODnVnHojz2FmU5zAacnzrtdAAag2GnrIlh8_XNh5QrPNZJ8PKnCQmX7iDQM4yoSEUH7eCSc0_pmzZrnX-iFP8xIB3mIFOExRoaI1lDw2xwBYEOEBRRtXX-R0-Ohb3cmBnEECLfqfoYGYPDrJOP43BEUzWv9214_ukWgqD-3jgHXsrI_SjbYRjxBNjaIUDjoAFQMaTb3XiDMB6RAeSGsFp2VxHD0RBjkGYF_X65vPWt0gpboBoHP5mzV7jf8u0BkhyX-3CwXsN9YM_81dDvI-6eHTy2QXY8H5vXXfZDi0sBxoE_bcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOEu--hdxKhGzumAenbA00f_7mnUqcXfBjwxqTwCpF6cMjzMp9GqhZzjqBflnTgB3RJBvxYEDavMnVHgzEK2hkkpp2PbfvAr-DrMR6Z9FRvpvpekJg8LfiXM7YqM8FzLBy5vKcKUQ_E_eRj0JFVG90Wh3mYbgAeM43y6MV08jiF88i4uKRKT2SLJBOtFEkB8aN3saWco7IgY_8t85HrsexmpOCjHgAVn-HernN4b6GS4ff7NZlwO9QNZkKWNWTJSEC5MfX1IuRId8WPhPICO0GemRsfD305uITKSn3mLAYjik_nvPXEi9YMK3JIgVBfOiYLgypD_oQ5OAJt0gyvA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxMXJziACf4GnM9BhwWAruJVAP7Dip3z5g6cR24O-NeG2RwFs_mjzrS9Bp_NmIQtAhxWiKCjDr2BS0aSIWcMH8Qxi4yjBuPLhF-NsGyevjR8Bl_dskbnDQXxrvKMYVrRQSANzVfEyhgFc_hMBmChOtWmcUgRi5kumghh2rRV1B8IapWUGJCzbzEWRMU6H57-zyjB8_V01gNiXfdleSlbuB1-mdJbh2NIzX7y1dL3MKl9XWS4Q9rDLrIBlG4pVE6QTzBfnw-wFMxnaojRuzLYtB1RyY6rE4iwNtF4hBScKMS7_W-JZdbgPtv7u-lTnMyu6hcxX6zdBGjOuflxVLQOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dm2OgBnKlLR-pVC0w2LvFjOLxSW8_XyGzFAHzQB7edsdMlNDXozp54se_eT_Ub_1Hp_teJoKZ6BJBWmhZP67AbbyiNU74DDf-bUBmitzwSHdnkJeF79tFi-B4gwM4Q__FeJwLemJrFbXCu2oY-knTGKUSqoUxY4XcHPpAyUjp4kKuAQBVh4IOvEGCAuKsRWMFznLRUbOx9I2dByUlzD5eKUkV_6OVIi0SZPc1KVo37ohldok00TjWaTWvSs23tlmObda4shQDwfvgkL8-a8cFod9g2qsrZR8otY-6eRGQaFA-eC83oG1jjoITyuRATjXm7m7lP276qnPKsgdT0pdAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqmCUVaRdnTGn7R15fjyqgobjxoHO--K0XZXNMEy24R8nrnv5yenDwkRFcqMAbnWvDBVm55br2JeSaUTvFaUNouPVIFQ_8PrZO4iT7BedCKhATo0E59A6_XHA6zuThDBuh2D26XY_vgMb-w_JevoJ9jP0Gg2da0uQHMZrfnwHQ7LC2UEoRIMUhOsLMfc5boYbEPSh9JCy_bfzA_Pac9hJH5aMk2uK8suiTsCAG5QCWGqi-M3FnJ5elJCmqwPiPPONfcKCzEP5daeIrYlgw8dITp9TlOetnXu6lDwz4Lh7Yo_QfrvcSGJyTlEoai_TINC1tn-j1iuwlSsQjSk6jnwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=RMo7EWf8CfVdSCXTlpsqpNCermBPg7DIClZbdKFcaYq0H2m2jXDHNjQDH1ZcsLWCvXPTbERxtq_0_2ALdlhRKsBZ57mlhRAeAniPdAF-PrWFS31bKMDOcljCBm6r1G3iILM3_Mh35fe_xTzVSozfCKAExj90i1pto4POyTw56A3GHpNCkk04j5aEapykocL34SWY0juhtzP9NDItWgMfY3EIy8C_PkybAkEDPwUAUw641vpKON7BGTavLT8bXh5tiI-5OB6x_Vi1FL67xfgGOpiDzTk1GUhRIJ5ZAl05qUWZJqNpg6rui90_m0gV6pzJIMThNtsY0o_HtVw-sXb2qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=RMo7EWf8CfVdSCXTlpsqpNCermBPg7DIClZbdKFcaYq0H2m2jXDHNjQDH1ZcsLWCvXPTbERxtq_0_2ALdlhRKsBZ57mlhRAeAniPdAF-PrWFS31bKMDOcljCBm6r1G3iILM3_Mh35fe_xTzVSozfCKAExj90i1pto4POyTw56A3GHpNCkk04j5aEapykocL34SWY0juhtzP9NDItWgMfY3EIy8C_PkybAkEDPwUAUw641vpKON7BGTavLT8bXh5tiI-5OB6x_Vi1FL67xfgGOpiDzTk1GUhRIJ5ZAl05qUWZJqNpg6rui90_m0gV6pzJIMThNtsY0o_HtVw-sXb2qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2ytMFbnz_tQ9_er4ANesVaaAQePWrW8Pj2gSPDfjTWXXz_dzfU6ZoyAOMwy8Ot9BOO-5p2ZLOeNmFdnnDTxdPR2Xaoqjf1QnFV35Z9oPVyRdRAMb5iNP2B-OGiCjO_p0gCU6OjpFMStGYyNrVUQNJ1KfIwypYPfsW6X7z-I0bZNkrQGV8kzAgtsT6E-X9lVAPeZAY60kLzlcFs6PUewzNVfpyEaZW04lNLEPZP3coeJdz5MBKjdH_zqA3lFySVMc0ALpq7C2Pud-6hWWoMXA5K9X93FECG1q_eFwaYb_cRGQsaAotJKktunAKuD1loADrIxtpEWjCnRMHd8W7KP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=TB00yHiDMS_97NoQdjN-uHOxwVx6tSkqiDCmBeOlTh5Ac-DNmCQ7i7ch4Nf9cPaMEz2w0eXDt_6uzDRRqfJkGLxvRufPXU1dt4t-sjTnwLgf7jcaeexmw58lmX38Tpr0ZeqYLHgEyWvFojV0g5HIU7LSN8uFQzxpt15tzVvkJIy3L_0eRvNMZIiNEUKF7F0YujJfUeXWjvpIbt5-cbTEj5r76_CPo8ixfsuYZLhExKgPc63esqX0tKvoz7ZmJsmvG1FsW-OELExkyyIrJNdzDLUrwypbFKxRrXBSBOkXgfOQpw2fDEj3k8qu2KktmBeBa4iWKRB5_5wp2Phe7UGEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=TB00yHiDMS_97NoQdjN-uHOxwVx6tSkqiDCmBeOlTh5Ac-DNmCQ7i7ch4Nf9cPaMEz2w0eXDt_6uzDRRqfJkGLxvRufPXU1dt4t-sjTnwLgf7jcaeexmw58lmX38Tpr0ZeqYLHgEyWvFojV0g5HIU7LSN8uFQzxpt15tzVvkJIy3L_0eRvNMZIiNEUKF7F0YujJfUeXWjvpIbt5-cbTEj5r76_CPo8ixfsuYZLhExKgPc63esqX0tKvoz7ZmJsmvG1FsW-OELExkyyIrJNdzDLUrwypbFKxRrXBSBOkXgfOQpw2fDEj3k8qu2KktmBeBa4iWKRB5_5wp2Phe7UGEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=VrUn-KHkWnaA00Cob5LPsrM21-EA1Q0cQMUjz2ZHhmNJdkQ34Qg2UDLaelATaIBWntQGr-WRtmS5JOHpIayv7d3Fldjepfq2YQen7SmoFwJO1O24vrEpY-3UhQO75XuDjf2-tXi3-0OXZvxnHDA1ojs9w_N1F0WhTvFjOyl_fB0WzPfP8dmkkWJawzqPSIq3qObkopKzpw5OA5zKUwjeiHLL7ER3b8nzKRa55oFM58TxPGfxvfPzM6cpQmmqOIFMCYohyJt2JLturKfiP6r3pyZxC59f8LSLrTt5IVwS3wD-Tt2ud-VoYFYypGTeDjYxDL7n-9E7DYAVmzBBMljAuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=VrUn-KHkWnaA00Cob5LPsrM21-EA1Q0cQMUjz2ZHhmNJdkQ34Qg2UDLaelATaIBWntQGr-WRtmS5JOHpIayv7d3Fldjepfq2YQen7SmoFwJO1O24vrEpY-3UhQO75XuDjf2-tXi3-0OXZvxnHDA1ojs9w_N1F0WhTvFjOyl_fB0WzPfP8dmkkWJawzqPSIq3qObkopKzpw5OA5zKUwjeiHLL7ER3b8nzKRa55oFM58TxPGfxvfPzM6cpQmmqOIFMCYohyJt2JLturKfiP6r3pyZxC59f8LSLrTt5IVwS3wD-Tt2ud-VoYFYypGTeDjYxDL7n-9E7DYAVmzBBMljAuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeDkZDBVpl2g60MSNszYJZ2pjafM_rBxZPVM1BmZBP7dCUFjlBCfI4Zzk402J8mwXgGkWq0ZgGXR5sX9DUW1sVlMDVRlhqz45Y-G3UY56swXBSrET9189zZp-Hl1vByYM59l0btDvlTPqIjtOQaQVJKBjyaWvQR5Udfv5Sv8u1Y9dkKd5Ed5I84-ga9Aex8O1ZXsVdgcyZ_QcknJ5P97-6gpjj48mQAZK3MlXpxhcJ56oSJDUiqRRpPrXjIILmJSmhdytUA4IVEL3vAt3BLPr3vBcIdLJnoc1zZd75QlPUTUxX6s0c29mhyxmyi6DvAbIiDUGUm8K_uwI3rchSVVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdTvOdyAnM-XSBkED5Mjhfb-va02jrkDeIKbmXRaSh9rCFpMK3gLGcEst8V1fTHCDvXLI5_gP8GXGe1XF4fwhvI9PX1GbDuFDwsNJrJGLIUq8UJRLufSRbGmb8Oa1ahr9pJhB7rwRFj2JbB-__8b8Rtks0LkMJ-x48KNS-0euxm2FeeZymg_7WF0UScJ0gIJdFYuSheRIQcHmaZyxLEemuQNlPV_DOEnRVgIdnOJmY8qXXoyLiFEsB598aKLjf1u9KR6mNJBwTgd1T0mx7-RdcQGx-zyZDge4-Tao7sbD9MzcqKmxqhKZjNRsMQQsQXg3FP3q3SW1awXzoiF_FOICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Hjz7mkvOD4fvPHhV3xjJa8PBpkDxsrDbMvXhnyox53fqOrSgq1GJ2PGYuoi89cTxg2N8q-Ob3lUPMXfO52qEnQ50kzrDKv97Q-CxDqhFYOmrbrCQwfmyUHJ7zZyBF6LJuxmhvt3pOZ-qqf534TH5uu_Jz5qDGGBfX2UV-D0O6qUrMCy_4FiGgbvgZoyXWm9GK1MEGe7YpiS4WC6YaFEg9-oONrAirTYDAUB6BuJPRHgekm598rv1C5WP8sV9SqjNoUMSlxL8QJDkrhuhxwSKgxRE4fSBisiRw0BjF104v8L0sVz4nOlhyb2ALJs4xv0jkSolnaGz3O1BHf1esDGB26qGRTm5Bt_qFOVWvsepPYmWKyuAiOoSIKioFupszLlE2vjcyGHTRE30B4dtiNOaK9sbTYxcy3z9KoLfa4O_XN4PC8e12T9P-KnTY4CLLroK6f8IQ8kNOrazQCLUdpClXG0CfGOz4NssnuS9RU--e26Tg2BjUPM5IAM4bBkQzstyo1dwsGqBdhbwlveYupxbDpQxcxkQerLkn3w0Yt3w9Sc_EDNQvR32Xj6ylFvjeKtPg0vqSQNTKjQaQqW0azr0S4cfQV03A6NFi6N7Pq_AfFU72rXy2Q_Wpj5ik09wqDxMMj-44QdyNgiOu3lv-LBhCtQr41D8Oh8aet9QtkQGjx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Hjz7mkvOD4fvPHhV3xjJa8PBpkDxsrDbMvXhnyox53fqOrSgq1GJ2PGYuoi89cTxg2N8q-Ob3lUPMXfO52qEnQ50kzrDKv97Q-CxDqhFYOmrbrCQwfmyUHJ7zZyBF6LJuxmhvt3pOZ-qqf534TH5uu_Jz5qDGGBfX2UV-D0O6qUrMCy_4FiGgbvgZoyXWm9GK1MEGe7YpiS4WC6YaFEg9-oONrAirTYDAUB6BuJPRHgekm598rv1C5WP8sV9SqjNoUMSlxL8QJDkrhuhxwSKgxRE4fSBisiRw0BjF104v8L0sVz4nOlhyb2ALJs4xv0jkSolnaGz3O1BHf1esDGB26qGRTm5Bt_qFOVWvsepPYmWKyuAiOoSIKioFupszLlE2vjcyGHTRE30B4dtiNOaK9sbTYxcy3z9KoLfa4O_XN4PC8e12T9P-KnTY4CLLroK6f8IQ8kNOrazQCLUdpClXG0CfGOz4NssnuS9RU--e26Tg2BjUPM5IAM4bBkQzstyo1dwsGqBdhbwlveYupxbDpQxcxkQerLkn3w0Yt3w9Sc_EDNQvR32Xj6ylFvjeKtPg0vqSQNTKjQaQqW0azr0S4cfQV03A6NFi6N7Pq_AfFU72rXy2Q_Wpj5ik09wqDxMMj-44QdyNgiOu3lv-LBhCtQr41D8Oh8aet9QtkQGjx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsZbsySA57xOOa19l-Wwi_o2ppQvollc4nHLG63CkXDVFaWQlwRctGJ04HW_ae9uVigWPbNO9-Ow0ZzqPTCqnC9oI_ZrmwLBnZ_d4hRQedFHiJUZ92BJQbBOfk649wDQykl5CZUxS0VefmmZu8AdCEE2Veuk6jaUBbDaVbBVgDuyVtrCKATv5e3gEJyhK1_cOg63U1mVt-qOJ_vfJcoHSQaO0WczP-H4eQH1HveIYxvxTaI_dNGxMK6L3gJfpwo5KIF3fcek2rJ8uMmuzOm-xtXnA9-8so1ZfM_k0AnDOwfMv5X5t0Dse5l302DMFfikqdRQPU0a_IU-jX5jxC00Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=uDaFaSLnU6fqSBFhrxviaR-2nEGvFSThvzKBx0cfeqR0NboJNLhydHHzZOBiOG-jEfrliKQF4I4rzUgNTwaTiVM7bu67P-XN2eaX4volHsNJFdaKiVx299lulEhNl0NAT7QFicKyHRMfEkN_as84CkRAAyVzxkDx5bbxOW-7VG1MUChByCJyDt_3NQKIEmOCP3DvUCXklol-e7ljlv-vOqBR6_QsQ5EpZR_pMnWKTLS98OCqhas1LpY8WFhqXBLj7mqR1u0cFBddGQHiS_W_6IuKGmW34FmQJa2uwTQhA76kLqiccoEcNbW0_NDXgybHHKYrE55ZK9dFzFIVbltFGUbhPcnrcDbN83uiCzqTaH98wxTJFBdnijJaCwfDjLy4-Hmx_b8snrPAUzEumGsqj-RSUGe1MgN-oqnSufdryi_CYKlk0Zlq1KgxxNIhM5KjI9x-4YtmzRPHylvGjPpbQci12czI4xNkAlAXuiqOW4fnNrRGsAZo_Nhyp_J98APb2olcUDY65lWw8AzbaW9QKdRwnFeB230vQaehvEtRkPoRnDyIkRxE05byrBBK290qQe4arV-BsMONpQ62S3KfYl0UpxP_Qjm8c-fIWGkMlYaYmcsFUM7BZ6-zf7iJjh7MT4nvsLADZyO4HsUd8AiMjeLZk0LaElbvdGYUbocESe4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=uDaFaSLnU6fqSBFhrxviaR-2nEGvFSThvzKBx0cfeqR0NboJNLhydHHzZOBiOG-jEfrliKQF4I4rzUgNTwaTiVM7bu67P-XN2eaX4volHsNJFdaKiVx299lulEhNl0NAT7QFicKyHRMfEkN_as84CkRAAyVzxkDx5bbxOW-7VG1MUChByCJyDt_3NQKIEmOCP3DvUCXklol-e7ljlv-vOqBR6_QsQ5EpZR_pMnWKTLS98OCqhas1LpY8WFhqXBLj7mqR1u0cFBddGQHiS_W_6IuKGmW34FmQJa2uwTQhA76kLqiccoEcNbW0_NDXgybHHKYrE55ZK9dFzFIVbltFGUbhPcnrcDbN83uiCzqTaH98wxTJFBdnijJaCwfDjLy4-Hmx_b8snrPAUzEumGsqj-RSUGe1MgN-oqnSufdryi_CYKlk0Zlq1KgxxNIhM5KjI9x-4YtmzRPHylvGjPpbQci12czI4xNkAlAXuiqOW4fnNrRGsAZo_Nhyp_J98APb2olcUDY65lWw8AzbaW9QKdRwnFeB230vQaehvEtRkPoRnDyIkRxE05byrBBK290qQe4arV-BsMONpQ62S3KfYl0UpxP_Qjm8c-fIWGkMlYaYmcsFUM7BZ6-zf7iJjh7MT4nvsLADZyO4HsUd8AiMjeLZk0LaElbvdGYUbocESe4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUxvJiXUDuZYZ2bvlD6zR7xryzf_Yv76cE0yrplMXPFohp2v7F6EGcan0A2aibQQVA3GlXwCE_6oCVnax68ws16i1AtNxhwXkHHDk1FT8r2D9IM41gdG7OJiEU0kjvEeiwQufOHMPISxJlylWzCh3AdsBtH49M9i4pNXMUWVF-FvKVvfGllF_KuFka3WGAbydCrjxs7wt9XldHX6NIcPPPXc8DcRAxzMaT5xU9ROPBafhyCQ1FscvZOzrrQhUkCz24JtA6Ot_cuxuv-ltnaVgIxmMY3X_5VTB666OoCpib58qMFTSegbaor8puXUXSTQnuqocMa562K-aptI0lDI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYi0XN8HdCY2e8QDyU4m42mUOSTAF-3zvXHJH4VgCnKIlIvqOL_eaOTGcc1FMp4L1bsbOr92XkgIcGFG4W0GITF2nRvYIJNt_A6sV5gRmlHpeWVWq_Dh-7tKk665XexPFLvhY4JBTSQiZN3ajOEfXGAkT2aJvqJNCXAnJ5p8i5yBHqtR_IeWlFHeWcfxm_0VOABxNTxRyMjAjj1sDdqg3gjFF2JjCgGBBr1b4Xztn4E5unIlNA_qySD7JWwTYocg2Y3FBMBoGahHyrCUF5DMfgSEHfsZdzOQ8x5lZnc52J22vfiO2GOgfXE0_MTr_cbCcrL5pfdf2re1RhW8XfrUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szAp-8AFgPESEU7U9B0SLyw1czZFfnF2VUNUWbzVoEWTGRsSKJ1mvMGSfUwbToDwDY-2KLS2wF7YMe0TPKBUB8uTpCdH6CrQ1oEw5omS2icYzWhx0vWsBmzKBVMhExFGQP-G947HJICaWDmZtmrabSG4oahtR2lAmmnJUD74oPBvoAbOm93MGay2nuA1VuhuS3RwRdlAUFPtCdMbQtObnHpp5BJpVs6a9LgdL4wYmOwO0yid5uvoeyK0H01mQv8tfk-TlowVIcJRIzXv0_NnMjlI8VQ4WlAO1pxSNJVTECNibCn-ROk6jHxj8OGtDVNlk24p1nuDRSjAZX5tnHJeNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLy317O2r9LVgEE3whUknhdRQ-sE6T8gdwHd5K669GMtpeVjQzPGQMTZmH1dHApAL4VGgrFYkQYYqX8uc7Cr-8faoN56XBwHmim7z7Jnp6WN5ULXerr1SCBHr0ONH8MJ5nL2nnR64Zym8RL7nfY66HGkKzljK07R8LgmL6S1tpWL5WAx4Zn7VCkpS4l1hRcZOdyfBugAdQA5J5kA_43Ds4Js1SBhrDlCANN9qRN2nLEB_2k-oZBPIVLVSoha3JBa9SLEFFGLBuSxw-o73dVgIzP9kTbO34gPO4dpMz-Fwpi7jQ8z1NX-4WRwW14ZEHsCshaWfx2HR23GHXaSWEp_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Txak73eH1CBS09aJ2cj3UTk_9DJFGIZPZGIDfRVPuM-ng_vNznhLCB8AASO_zi2L9qToRD0XXSIuwyLphy6iNCLuO096b44J6aS5zl7nxXbnsE0dO3yES79MeAL8x2FZkmAqKM60cxVVUcT-2I8TAbyrOXBcIjhjfs9L3-Uf1pKdNZq-aFEMP5xG2-dIiJ46OJ3qOft2i3XNXX6JlpaEysnnYm1shN-nnI_oj50LOc7GVlMaOhjI7UVOgfaggc9LRx0q5DwOUCpi7yXJh5BJ3Qdqbeg9kn8zRPpHrR9ReV1g7you2GWegWa1BqFAGXg4M--kaTRCLedYYnRTITegMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcDzB9k4CHNyM3jP703zKBcLDP0qFXB6O5kZDfVKVrP9jSBjDRAS-7cSikkRK44rLuOTKLjBWxA0c_cGt7mSRyzxJtj-yEHiLxo9RQVuVz6XViydCoRapMWP1VuMTPGLY_m--934RsZHpHuubkUc7R8w_481UWnal1tWnF5Er7GpACsvqFlhhSy6jCBHPKSF6jSY0VamK5lY8pYJIcmlNfvscr6XZPZDgYMVWJ7orzNquFIGfGpJz3UYzv5g_8o9gNEGS_mEejvDsdwnz2JwrQ21qdT_HqwCFxMQ8vDEj5OA3HofWcZUoFuWFbhLYjCiZEQHTRMBJFpba1hJRYR4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUSqgQ629FgClRCrNN1Ne_gG6Gq8BOBBsA_To_l1AG4I9U78u7bk3XEcTTD27FA17R3_08kKriGppH24TIbFZXTZ1L2DOlWOemERO-bHI0mkl98KBYSf_KUAclnZFUTLKfXy8W3_EyVV1O6fsNd6EN3rFvoLjIcmX-qd4BI8LjW3BcztMAJfRiu7KHR0fIR5EHHndVYO51KYMXdFUnJjm_k7KbJYzQ4s9qvYvnCQZ6xY7ejeGxI9RAa9ogQnzH1z2XHCW1Yb3BcQOu3SUdSh_ammLf-vAXsdkgRKFh66wat5NsOcq8yqhEfY7wgDWkSUQfq7HAYFNpwIkatLg8SOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrucytnjIlKUkhGOBZsDbnpFiVgQjXKgAcMSqg44nhcmwEHH_1cVh8vzSXhuRaNlt84R4DKIuG9101MLFMF81fZ9aiatKmtzagKLjxv-a0tvA1Z9kSyZtogXUSaRwtXVPM9Iy-VBILNwdSQ7u9vvWFIZJRbxvMPlwtAKu-zVoGorvuv9rR4BrzOUFzXvcYPNKQWxjkPX6yn2iXiN1A6t5TJ40LQCUQGoj5eMSYHpZ4kJb0eBPDiPDEGUM6y-pr6EwNrQ_o0TPubnhUb2tr5YKtSReeiS5Lnbo24CX5QW6cwSel3844Wb9OuF-ZoILrL0GIxyetpXuQPgn3jf1A03Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd8k2z79gx6xEwewGDbN4cu718h79P-un8vkeDezrbdg5PkQatCeudO-LN0eEvxqPwjialNdB-zaxBWgeHyz2eg6g29t5RhA74YFADiUk-PZOA6HrJjT6Tsne9vXJuTwRP-fcZTKoBSg5ShOlMxU2eq3HHclltFxEJvTHGBAr_gHYa5H4AhKAWNcaJfWH9-q9HFz-Z14kx2EoMVJBFGbJWtM0e71wcjn8rl_MF5ztafrLZ69S4-Eyo0_4qCmPaLEqG_tdlPa0yN9LRVwgyPPUcu5oihC6k4V5YT8YdAvY5i3J8CpyT9AYDkKxxu3pCTwsEcaO07khEVZH2ukOEHdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c21Dy2rWMKgKEgvgIfsBGVx7ykGXYeq5vHYEZQUZLOhgxt4XJdL86DDYfpUaoAlb_KvkhBrW5NPdWefV8oIvgNP3khTYiDcuXB9PNieUKPa0q3eEWhxX0B3fUr_BjJMiqFeZgumyTjUQVQamIs24YxMIVuUG6Frbbwl10F5zWJ5EiaBxWBXonY7L2Qdnd3R-p8aGIr2HxAirC4APkAj8FSjp6k_-VYExbsV1HYK96L-DoVlJtKlv6Z8nfVuIJlrKDNb5PL60YoTgow6-gJPNa7eDkMaGWuesjBPfvT7rHs-9OVneucYgRMfmuOwKpY90zcKSTA3UKbeCEMvKdYPCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObrrcxU2vIR-DdvztbH6olPwqEF6hI8aV4tjg7ai4A7YwMbWAMj0wpMpbDi57-_waBAz2HcYasyyljDDgdGfQaZKZLGMDvRj-6WBwraccOTq18qLbAurMAHapwMZD32g9_buj1qmPa9wEA_kT2t6FnrWVas7EU2nm86jfM_aaPyKpNjRsVe7CvaCekhPnbQ-FecT4NfrHSJf-seWDWTmp6tL5ybqTj3lYuas-lInPog6t0hICl1o-8bv-w74PEA6_ucTu6PKbDrlvxAlcIGxMFpPAFCwaECx-Wp8WhOR0Wv-TTlYN0acrk5K_qb6dFSyLHSiuovPUyrAGvAGWbKL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZvOSnXOBd7oYQudgsN1r-JnZRFUcyVYw61hq-y5HaMsnabwlajto_npD05tqX0QteAMqR3Q0tMKvgrIVjBs55fNaNAosYzv7B7lnqpODhj4z0hcbVq9wFZ_LEmUaxNQqP7L3Z7kxYAe6t-fwOasDP_WhvDzCkfcag5Ig_sA6nEGJOmud6Pz8nbFt3U7V_ObE3x2R6mixLhsKYzhvYPQX_6zCHk0jydLMmIvj3UrnDwOjdMqOoSZWCHdt3HY9F99FE3FIGDmpEuyL_RJDFMPnjaAk5eGO0FXMxZgp4WNAZzvf3kx0EXIXQEv3QrfUZadYI0mm-0vMOV76_dt7KhURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE39lJpUU4K4ck7BYBqSDwBNJyEukXseGocZQFVFKkzv0ouIuqUs7Dj-fCAJFMBZHNmVqomTunWnq9nqIP7tfG9MPYChaoBsOTDpdVPcEu8MHdk8fdonoOnrHi-cBMM-06KF_pZ_U88_BNL_DUp4fJPhyim-b4IAyydNV5SCciqJrFBAZ8a2k-n3sv5cSYhF-yEKPng9MWrjCJgC7jrGPeyaUUmnwFSAye-r0kK3c1z0rsNgG7L0W45sAhNPdaRrG6LpbvtKsDDRsHpiuQmkA-Zs9K88pbs-ILE88mHgq-tJDDtp9wzBpSLjBVSk1LbRIsfd4EOWiEtVj_um-gNKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTLiY2mvChs__6lHWXgtSg7eH1sz_W7BrbXgh5w8H-KZRk41CiZOLOzHgOJ3_TcxtC27VbZTbFytgkLY8YbCUHpQs6ytylJOk5q0HA8L14IqLLzj285w4tpd50So5SLon-fnwVFU1aW3EMZ-be-FZZZaUDDDOT28VLpVD5Xogi7xGMX8CQ7wdbJ2gusO_avoBbyARV-onMRfIteaPq4xF_R3kV4YFO5SI-1i9QO1I6iVIWVry1SnbsA9zbf9b7EuKkmvEUbLY7SjAeEQ6-R4YCb7WD4cBU-BoCm6difzFwv8dPgPfFTxaBctDSfKgKoeLeWVfgB-DHeKziPWTzh4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bD3r4Dl_rWl5lbnqznRc64mhFvVdFv8DT4qv2M7tTtwTQoOTnf2glNGl2tfgtcmjmO0xoDK4AgQm_ZLZ7NxYvvsPbkMVyRsu3Y6PwAVnZwot_0TCT3KP8dDiLYBShhldfnyA6bqlux3hvf5t6G-NoCfZ2wvFWLnCm0abfpmpbkeXQUfMf3Ak0ww3mAJi9casV3daMurII97JCjaSpOhRU270QlFYY40F_srJo8_aUnMeva14sSUC6x_udCE1SYBXTZU3kWlPHfjuHlETPxbgkKhzK3au_2RdDLzo9kMwrW19yVOeCnpzaG9Z9Djk2-z0NT1fIAsiFDuXj_-QgA-ryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT4OX641kQ7fBhkNgAjsWmqYpnla0YQCGT9Vr_S-CCPVjONq96J_o-o4b1wsIUgnEYEYKG1kqlWltrHVr124srnIGBWriaQ27eStx5TOcwt6UOnG6w1OuDdEDsunF08WCqI61mYHdRDRhZC2SOPddJul6VbjZWRucMJ_9RpXMRnm4IZ9lvy9agYsOA28IMdWCX_kmwhBo25_AxI3kI71_KWeSm1v6II9LgLKkpJfyLEdx2YoIK30PzB9anZ7ah-aNbDcThuktPN5tJNWITQr7revkFCowR7qaA781mpVSFuUHUxmEM1bqE9vujvAE37cxPDNPe_Y4oVTN-Iz4FOxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6PkziGfCVfAXMbrbR4-2Befy7mFeywxdgBjIbc7azd46KcMMgSGUUTIl5HYIyVi98YDdN_kaEVEv4KNygVvs-qYNiSkRpWPjXC3-a_CuyujC5eqZE0R0iRUJGBITE55ydJBDitNHIBEVfUlnuO8akgjMTHBlDX09gdunatK-YaSHsbAssR8PfBLednlyZ4WTqgIqbtg_ECpEe06mv9w4fidIks9lk-Pz2HknW4rh4e1NFQdomDhygsubpOAEuSb8LtGh-XkRZF2pjKmGT6ObQCTx0JMEzzV4o-U7ZY9MgyY43wHYVMUnAt2r-PL9uwQg6UuDvFJoQ_XUJ72nyUWWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vi3xCJGIjXpu4TcspQ2rUfigVOxUR3orpPWKEYWX28KRSziEL0a3rORB6WQu97UEyH3bL_vnMHU5RLgjOUcraPeUeeHnuwSQE_2JDQHpQ_PensEitXA4GX9GwLvNmFnSLkeG24N_yDJaxHWB8s4e5P3p8sJUwd69x_jhd__JWVnNhDkr-zQZcA9dELGrrW2FQJR84QHeKeCcp1aKzoC2qGrVY86tULvVnrqXa_7vwS_bbAB30l2xCii2h4P7nfAwpaWPcQUcx8u3olF6Fl2tbarzZip0TD6vczD9E_5agor_Q5ir5l-uadiun34acyg5DKWDsah2d6d0-P7M-a7KJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLgRIKRJjjEt-6wd68cSNcPTikp4JdzJwdnFz0JkJLuSDAlkgIE6ueF5WZs8Fbb135NGPU5HoWA38auLqyN0arn6WjeeTjPR94K_TDPkqGseV1XoY2KDuL0JyUUBWV3hsFeu0-D6DdH4irSTSfA1WiU7oiGdx4QQcJQDcprOvdgHC-EjuAeKNW47VS6k_xb1rsc-6ZQ032VfUFm857CvcJjM7ZfLj5m1yggzKGKHwDYlp7pWwBP_jPjnRKVlxP7eRE0WNgAOIzIkVybd_5pzNkJMbSJ35pB0eZ__VVeIOcpVuB-gzGvxFc-C__1GH2irXPMJifXkqNXPWLa9OlbD8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_7OFhkxDCdVaGnpmWFDuTqcZiojulu_EMfmoGf-HxdKuag-ihcjiScG-r4yfFsVlewyObgDYCh96j7HUy0EI4CEVmHWO3hRLjtq3hCFbG9zHcn5aVQeoDJjv4OMi36NC1wvJl3ncjBeqOBFjc9irL5A-1wFsnP8QArRa4hXSvMfHsgVtqoTcHhchPtPVyXbfGK_6LufpHQZPGfCOgBPX2F-bza4NQfnkIEVKMrnSMGU2TJ-SwgKiYUNyweK3QtRzrATYUb7kvUBpNvWTUmWQiYKOMllFRuc6cWR3SswnsxKyC1vlU8mg7gUDUYDdOvJ3_sKCoj2FlF0L6zBiVvJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqDhO607NhoaF81aFfi_3I18JivXP5KUKE0OSqZ7wnaxXjf89JzHzRvt3wWCDwNWr4K77pO3HCEu55kUR6XoXA62UoFAkK4x9Qh3GH7NnLFw1a98x9vZrOCcoFiC-Wh85he1YLsYR1MTb-zeVIraYJMjT4gFhV1U-8XlQnz4n3gOn-Dq5ObBpltE2bSjbIId6r5kvlCrxmLZWEG7p3qLzBOmtaDLRURC7KwG86LJtNVxOCxgqaq2GHm-j2kTmKvhqRCjej_bNftWDxXS0FfVpivNbWTnoHV8YwEwk6eAoQ2r-oBHLWVLXjLDTQVTzZfFvWy1GFCKjKBnIbGT_0sZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufSc7nsghEU30GSCtICns_NXRooSJ9mChGzAqvPtPVMfdem2MnQpezsEbNBSRo_0sYp2GgKyyxcQEQ0Tdi9JfDBdMX1Jc_PLifv4HOShYnegZseCqQJuJhjJVsao99gA1PxBJwKgToe_usX_aUepYEegEJ4qpzvKbyWJyFYa29xYIY8HBkOiTm47TomgnXNHewygvNsKo9qIfnSJuprBNCO-uZ5pXbcI1O3bZXMkrUIwfjS6p7umpG--22ebAVB9w79TN7fNnLXsfnuIsOMpEIVBD3VTIpeh3VdSnmOGl2Vrno4ep6qDAmNUSXrDkQMRjSkdyO2IY38DODhIxkO49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uad6Rs6vrw7lwuxKSxFEMQRf79zzD9YvP7mp9FNsEeEM-uGplHQi7bv4f6IDikhwqWqC4rvl9K7BoCqkwz7PD9epJDI1fNXHLdmKm2VAb94SUcy2hb8uEOTUEgq6SODD4a8o3hz-4LT8J8avwC3L9PZnDauMSsT0Z7qTuUHbDDulL0OLr4TQ6IRQ09EEXNcwYxu6wGGqgKtA5pocp8HuD7zH16RDkTIaTsw9XKBjSln5h55DJrIgM5nInPYJ-TtlgsuxMvo50RnntXvumu96ufOWCJpNXCA1yVmZuJ6DLZQnfcH_qdJdtfv7hVSx4lGlgVuKouiXcO3bQHngVdEXZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn0YbT-p6_HJZJ39zGMrCONVQbHTmqeHVPMDSR22FtSlYGSuCmso92LoymP1MKdXL-zd13zy9TFJZhBDqeNMS6RzGmljpg8pCRaDsTXngi-Kf_RuTOgJ2bRorBnZe6M8URR_Gn91APmnW_laAnKyZqaEbchmBGmiw72PG1UIwcuDhkIWFPtIlDa5WE0SV4LBf5JBn2jMTiw8Kz3QPxM8Dtb6vlng77vCQLeWAvS8flfXnBzNqq9X9NS6TcMyv0EfQfGhydTO6v8eYwS7YEwoz9IqU2wW7k75BdzoueDrxvSjuuUO79FH7i7T6lYecV1bB_O0uppZ6AsmC4Fq3l7YEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulh0HJBik-MVoQRFX3Dmo9DAOjgjXFr9S7ZOBW--x2FgZ42icnklaCzzoxx6uBM8YVZfeHkQnrC75UBk4j6LKUySOnnCON93DvWpzuYkfHXXAUVBtVuip7UrMvOcyKc2vhXvbhd9WXr_T3DNgE3vM6vGLKZsqCOkVR_IftsswBaOI9ma-GoacgKr2LzQNSXwGB46w0Blh_X_TS6QvRFAvfkEeEVS3XnH79w49ruOCoMKdLFESp7TST8gzoc0tBVL-aM8IIFVWmIHqi53VylJ_IbHRg8gfE2PM0tULFt4PbDZmGLra1Zv6Dt4tpSIK5nC8uXpgVoQQbA2RE_p0zXLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9itYguql-ekt9uNRxjaTlMPrvwMC2OYFv72RCRoerUIka9jNKdSmjYlHlmtjREceS7gaeSD_64zxa2gPRCHcU9J-HK4uSSIXCJemlUDPO3SmremNqgZQSR8RZ_dEuOI25Ruc7-VC8sjhFfg7mi8kIgAgnB8v_qhLqTbIeJ2lrIXAr5QanOePLSauB3lbV3i2UklFgRfJFYdz8AoZEYOWrmbVlnvWY7ENcFGKq4ngGROecbqoPSs_BiRrJz48Ot4JhorG2r7dA-XcTWGkTtzShFzoVqZtcVRKePTBqr8KEqU1EOcI0PvULes2YOljZJh8ROqAJSSm-tO0S0xXmGtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk_xMB6FV8ppm_PU0fWGxkYB5zkLYWhkkr7ruOPRshO4VYtPqmVe1I3qD-Ob8FaeCAqnVkuhAbILyB1NEc0iXzX2OlVQpk4byAE7AUgsj4iiFzd_QnTL1cdDN1J3IPxNNfRaIWS1ltsOI45QDH_YlaKt5WXpCGOD0hWHvqRzf2mCKg24cpgmFgq6cb5egcW7VzQqF-uuSCLbhCueaDS1ETFuN2meaEnAe8u7NU4UX8v4lUG7-lwmdkK1tdKwdXnQnUPIDAoha8jm4E9epNxtO3BKGia_HL6ymoE-WkFV8tskVr9VYLW1cJewTLR38uSV_aBmn0GyqmZ2QMEClcl55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNKNXlI67rlfEn0fL8q5lbnxxir6cDMM447aZOg1gv15bZ_bIkeSApKW_0jaWlCHnDxw72hWAozT39BWwZnxP2YnRW9jS8fiqtdgxg4N_RVrdM2Q_3v8qjojsGLKqHxw-ZAK5eS7qcCB8dP2GD8yQBe2XqPO0p78qjZbPTrRfaJrjNnfgQ0lEfNWZvIOKSxME7HgbenNvXoGX-QITOH7pM_rzpr6__Z5RLB51H3JJ3LJ6jtSFhTF4XBg-tQ5qDONIaSIjoIO1GXQVFWwnhOFRF3WQN2yuY9tVmC9874-uDDQctfGwdmLPeQs_gyqDkCCiP7S8f08SCyqJdbGOvTWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkPIL9rgXLNf8j1AnFr16gRrxMKEpIVv2_PcfsyVmQnaHCygdt5T7P2mnjdVaTncUuTDIFwZL47cy71SV-oHkPOQZDWCVrLc5WcwI7kkPqn9ENMV80BKInOxiVd3i-MiSjqUdjA_xbmyUYfWJ6Hg8g023S5UdoiQ9KbwyzB_PW-txch9wgj6NySNer0fFHY3_2D0RrpwYsrjKWOgbQpoVNhOnKxRHoymzT0uC8yHXIr0Chzza4d32YA4NxmkZgjgRoWldZ2U0kcZSOboHc3L_A7jznk3HDPYuNElxKOpDj_GhmG02yCGA-Z2qlvDe4B9WVs6TSm4qZsLWvR-UfprJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOY2DbsE53uAihTwotmM_1EsgJ4jU7EjzXWlquG-qlS4Xyqf3jD9ozZ-QyWFGIpmOHFGBH6zKDDP7FhvsZkoZTcP_pT5jexrIzrxa1q1HdyBt45s82j9UZhB2jDpYvce_M6WtXrM7U5iTD5d9LcjsbS54IwjJf6r8ZNqe0_wN_iWCG2qL_u2Xins-Uez3gAktReNZZDCbMCenw9uEp-mBalwI7wDPLY7AH4lPT0Y4FyH36bUTZ-PWLQihdZdvPApGgk7KEEFubEERjpabZ6MESIwNhkYmr2oX3u5pHBFCgR-aQSwy120Br3hQ2eMpQjeL1lbf4A3-M_vvYvS-RrHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
