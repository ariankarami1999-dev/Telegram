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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 23:33:12</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AOIV0Vmq4o_sqEMEOFufyklmUjDfNikktDqVnCBUionudRrvcJAHd6InT7z_0WbFO3Lw_U0_wOL6qb4pHqlIwxxPIn_Xf1St0mly4O7_f_KZqr0SM8SIVTOuTIKg4ZebFNVm4tp7DRsquVgHT9zK91fkaImCF4eMt6AUmOZwRcaFlwR5RXOoE4hvdB_mzsPWUYiz0f6MT8-EoRgdc4LfTmKCVONIKK5xM3C3A485aUWzqg-e6jc_aaAWr0AhzyzhGLZ7su5tKJcY-XsqtQS40-PCmsUAUKNwJV8bVt_EMR9eGrsPXMMbWoyo6F0GAJaRU08EU9SNm3hFP-6si6WyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3yo3JUjqP_RbwpfEBBuU9HYquZSaEkuH-ROagYEAw2l-5YOIA0wqQQO8A0-tcf-nOeTTPb1yAPgTiAQEplkDLuF-z3VDH5XgZDjy6TioBe4NDxTW08fnOMRSBdSDJT6LT8JlfjWLTW_GzP_wWNWzyVBL5ByI-j6thWNTMNMA2vROkkrgcvb-Z6eI0fU_nsV81VYp079sedF9fnJ8-IBJ2YYZ_BFa01JWceRvri8XFmM_5Wc2YeESpVAoN3BxYd5U57pqvV8U-ri0PKMfPNL7qaeeZzLKxSV0cQ2Mjv0SyNv38ki8yuNF5DkThBt5gxBQ03U7q02IgKVOvd8eXRpeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=sS1O1FVUVE-HGnS70NhhAPxDDaB8V4wNoe8jdQg53G35qrNconeG0ua-f12GiVbSHjKnsIP3MZnEJXZVTRQd-G4KmsFPDPl_WVBnxzQHkxhrJmBn11dwtH-fgIuwq1JUju-6CbYGYdUxXzMmI5oQYHy4292v-7_eSij39KyEk7B0WxVhGHtKUiMfl8tpJ6JmwuJJLDggp1xOTN7xhF1m5J44pJ6Y6I7S6gaz5iMsdGknYQcQqumKCWr7S_YP6-0GFSPEtyyv6Zzs4XIuWVGTVBIVsk_EssKb4EpwcnfU4vCIz0fBmcbK9C791fMv5ak4sGOs-vIcFTxIuzA9t-L91w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=sS1O1FVUVE-HGnS70NhhAPxDDaB8V4wNoe8jdQg53G35qrNconeG0ua-f12GiVbSHjKnsIP3MZnEJXZVTRQd-G4KmsFPDPl_WVBnxzQHkxhrJmBn11dwtH-fgIuwq1JUju-6CbYGYdUxXzMmI5oQYHy4292v-7_eSij39KyEk7B0WxVhGHtKUiMfl8tpJ6JmwuJJLDggp1xOTN7xhF1m5J44pJ6Y6I7S6gaz5iMsdGknYQcQqumKCWr7S_YP6-0GFSPEtyyv6Zzs4XIuWVGTVBIVsk_EssKb4EpwcnfU4vCIz0fBmcbK9C791fMv5ak4sGOs-vIcFTxIuzA9t-L91w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6x5uhk61jmBjpHnFvJaGTmx5ZYJRNf8lu2Z1I-JdraKkF0ebA1wx4Dng5WTzl4-PFo1ecWsxepGFa0-xAVusjbaLQ0xrBkRjD49kfl8d4VhJC6VM6SNAvzqLCAb-HzTv0EPDHpLV_lykigIu9adANoZqfoLwH-xCiLLPBn2d4kAfI4444nJQlTl_WZGm0JoDvZCZaeq94rilOM91izsiqWizBQmL3boHrOkRaQI3-BbI5zLarF3bXkpR7JPGYjEW72zj51MMxjuUIPPsVjb7h9_Qn9sMw-fmpsZGtTLo3OF6FSCDvlCrCKLG_objQKiok7LbTsfNDDEvQN2GsKiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpLoRmWsNBY-DCxpFKzRJKWrGgDaFx_Wl8wApnELlzjtHho24X_zUkYcYmDJrHlol0WG_4mv9qPRQ2aPZYj48mPK0_8rDECL9azB6EJRYNpBRMr_0rQrYoaxGCi32SDgRzGaDRHzjybM39qxulTQx8vkAm6gknv5RqcYJBQLj6Yyl6S8TIdLAK9k6_BbyEf4YBlhT5QtB7KJeZpGYXKUEragMhH7ch-mwye5RDJFwsBqUUDc0UROnLkTBTyi7bNu1-sum0BJgcGh14lVBafjOLPQvas-4Zw5Ptan7RuyOE1psUGx-Vpx5N82KLT45Yi1K_GAAcTvjYoPWO6ymaF6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4xkZvDe_TRochKG9OElTNQ5FAOZmPVCju0xMPY-N94c-UFq4HoE8LgngXeU_YDXVu01NzSHQEwHHaU-AoLT74htlRTVs2SHjeMHcBdS9DePygfhIAvKB0CBuZm5JJbqhxNd5ras9zBrC96cKDy5Aqs5wrXV2x0n9MEgY2vjcbQibhAoyxDJp0xkR_4JV4GRcw6suy1uCwS3ASKZLNrPNHAy-Vb5WbaBCml85UQbxY2e5tABQbEKg_nMSqPiBRFFss4YAZ56EK4CXp3Rx4EoPg137Cg9VNndQh-K_yWdBIclcfKZuUFmZHL_dLj3m3zuRumHI5lbjeZGBCpEfPaBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=IzokBTg9F-ZAiF2LUW4t1EU4K_Ixch38kZCFTKt8f5uDd74GW7loqHKC7z-xCMjeHRN72xaATVgxMwiG_X6Z7MwHcwwTyeuTOE2XCzyHuaRvGTDGZcvQ27CIjFYPtdtCUxygemwGSARjNwZ6O5VCp2u3ZqJ_WZ5Mou3BJrEZ114QP8JS9lTbFow82pYPrsXcgVUfo6eSs7tto1-XLz4Tsl-dBHNzXUo4MgRtR20cqvRmx_MeHrOUGsQsupKivNom0F_7mUBc9EIuAAPAfB1jTl04a0hDxxEnVXa0OTsOjEexm3oHappY2McoELuFgwEf-hvvinS0yMoCQrh5HH2Q6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=IzokBTg9F-ZAiF2LUW4t1EU4K_Ixch38kZCFTKt8f5uDd74GW7loqHKC7z-xCMjeHRN72xaATVgxMwiG_X6Z7MwHcwwTyeuTOE2XCzyHuaRvGTDGZcvQ27CIjFYPtdtCUxygemwGSARjNwZ6O5VCp2u3ZqJ_WZ5Mou3BJrEZ114QP8JS9lTbFow82pYPrsXcgVUfo6eSs7tto1-XLz4Tsl-dBHNzXUo4MgRtR20cqvRmx_MeHrOUGsQsupKivNom0F_7mUBc9EIuAAPAfB1jTl04a0hDxxEnVXa0OTsOjEexm3oHappY2McoELuFgwEf-hvvinS0yMoCQrh5HH2Q6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=QwgwfKJr3IoPF042JwJ7Zb0H7FrT6pTv2QvImK3ov0UK9GXvU2TKB0HExzycbjfkk8ifRExp33PfKbu_VYXfKboNTFvr9Lz2D7VC8b1k79v8LERNyWjmBze23xiRFHFpBPXaxBHjZH7o9Ud2BKVb_wPB4zvPQpN1z0LY-1VzV1Bi-FCwxTs5fvGTc8PJNgqssmGqc3Vaqq0wfKmuR8J5AbTprzZxBF1nhOhu2qtk1aYsIBv2PbAjLU4E_7BYI4C0xm-Gq4q62xtuHZV4SnY985LEF2zYO0rsVQzD0ImixzSBassBY_kDCzCnaTuojhgoevMNPPdCwLQcOILXhq8Y5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=QwgwfKJr3IoPF042JwJ7Zb0H7FrT6pTv2QvImK3ov0UK9GXvU2TKB0HExzycbjfkk8ifRExp33PfKbu_VYXfKboNTFvr9Lz2D7VC8b1k79v8LERNyWjmBze23xiRFHFpBPXaxBHjZH7o9Ud2BKVb_wPB4zvPQpN1z0LY-1VzV1Bi-FCwxTs5fvGTc8PJNgqssmGqc3Vaqq0wfKmuR8J5AbTprzZxBF1nhOhu2qtk1aYsIBv2PbAjLU4E_7BYI4C0xm-Gq4q62xtuHZV4SnY985LEF2zYO0rsVQzD0ImixzSBassBY_kDCzCnaTuojhgoevMNPPdCwLQcOILXhq8Y5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=UTWLsSXZsUAFg5TF67zQ0OzY5KbIvh5L8vH0l8wiJ7WNkinEN8eB1L83F6PKPnNzahGOMPX1pwCGW8_qbLUH5HD8nar3yv5Y9_hJ2SQkCaJbMNkmkSzS4bF9KulGWX43ismbQTO1KDdVv_sOJnmAPqz3yzFGbXrZZ0kaexe57g0JNl8a9Y8qVyxaAIJTqz7Hkz-_-VmKLi6eo1icUreVMlW9XcVc5ZyHQ4rE-jVYpQY3jextAP6VbOMNpqaw8q47uNnEIJwd_P2_kU-Hd9r69b2ocNcBoXGTt_PdNE6EwakVe2GYD1wg-1St6sRRt-HPINmM0zd6W8HbLOaQx6FbDKzXpF-NRNR2dSFt7QjcMKYR0ubYcM-n63Q4GzEVmlw59fGHZCSF8qUEkySDGKns1-kidDRCpp60MqV981WCOt3AtLyil7wqv05YFsHY_M1oAVyYb_3ZxDa6NQuxBm_km9v0ioz_GhhDLWPqzneR0Hv2bge4YkKAM9BkWIBvbkkVTU6Z1BE-VQ3U8qMaceTie71M2vbSj11D8m03FKAoP8rJHCO65JBOGvwSN0__0KIVoCsqGwBoVRM6zjVUL1hjhok6a3P7TOrFD6nycxJMlMB5ynIgQYdKZ7GcF4_mjrZ6Jt3xqdlbG7tJ_J2mEmtH166IXRosrjiUS8goQaR1rVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=UTWLsSXZsUAFg5TF67zQ0OzY5KbIvh5L8vH0l8wiJ7WNkinEN8eB1L83F6PKPnNzahGOMPX1pwCGW8_qbLUH5HD8nar3yv5Y9_hJ2SQkCaJbMNkmkSzS4bF9KulGWX43ismbQTO1KDdVv_sOJnmAPqz3yzFGbXrZZ0kaexe57g0JNl8a9Y8qVyxaAIJTqz7Hkz-_-VmKLi6eo1icUreVMlW9XcVc5ZyHQ4rE-jVYpQY3jextAP6VbOMNpqaw8q47uNnEIJwd_P2_kU-Hd9r69b2ocNcBoXGTt_PdNE6EwakVe2GYD1wg-1St6sRRt-HPINmM0zd6W8HbLOaQx6FbDKzXpF-NRNR2dSFt7QjcMKYR0ubYcM-n63Q4GzEVmlw59fGHZCSF8qUEkySDGKns1-kidDRCpp60MqV981WCOt3AtLyil7wqv05YFsHY_M1oAVyYb_3ZxDa6NQuxBm_km9v0ioz_GhhDLWPqzneR0Hv2bge4YkKAM9BkWIBvbkkVTU6Z1BE-VQ3U8qMaceTie71M2vbSj11D8m03FKAoP8rJHCO65JBOGvwSN0__0KIVoCsqGwBoVRM6zjVUL1hjhok6a3P7TOrFD6nycxJMlMB5ynIgQYdKZ7GcF4_mjrZ6Jt3xqdlbG7tJ_J2mEmtH166IXRosrjiUS8goQaR1rVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=QJmlJU-6IyMmzvGUihXBooytDKA1NqIUAUUC3UzNjdQzrl9i0kdD-9xXZ_WLHVo7RetLSInqjBC37Z1DVZw6TVOkP6wn9Fl0QFfopkRYCy0DsIfLh0I-038ey_FA1-906XLrkPlKP3WFc12gNvvGJ8IhBMlBWjbsBXaqDw2NeThNurN-XtHz3CeKWI49ruAjrMa7COPx9P4zGd4P3J8NLWeHxZgQdb9XmcSHLlrGcpj0MSB8kkH3bnygyyPfbHnG__V4XO0J0YYB9FH_NpfZMBWYfw1FQzJXEYemJ7gAOOkFqPE7h3_UuM2OrLHkS-0eNrmhmRgpAEaAowLHXHczRBBE3XItTM-zMJCrbfDUL3dnf_zJYBA7djAZnl4vlQuuotgBnEeBLUthNiBUlHXLm1ZZvLoHuvEq3SNOaIHI-CLim6nHzfuSdcAND8R0QKncyLrvzmd7LKXksJWLhkBPzU_KASp7reSh01XHqclK6Fw0jd56IEVOn8HmNRXQ04-rbEZIQ-O6vAxtUIpbymgzVov9sFBvFUoofA-HLdg01oQaNZGZ4E1CmMP-HVrj0BU_cqdgj1JoCLsPhMgfQdm4k46WbYEoi8mVrOXPLx1HmNn5_n4ICYQS746vbzGThCCi6X8OT5wWueHGNVyUIBV1JDU5PLJTuvsf8DfpGvfW8qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=QJmlJU-6IyMmzvGUihXBooytDKA1NqIUAUUC3UzNjdQzrl9i0kdD-9xXZ_WLHVo7RetLSInqjBC37Z1DVZw6TVOkP6wn9Fl0QFfopkRYCy0DsIfLh0I-038ey_FA1-906XLrkPlKP3WFc12gNvvGJ8IhBMlBWjbsBXaqDw2NeThNurN-XtHz3CeKWI49ruAjrMa7COPx9P4zGd4P3J8NLWeHxZgQdb9XmcSHLlrGcpj0MSB8kkH3bnygyyPfbHnG__V4XO0J0YYB9FH_NpfZMBWYfw1FQzJXEYemJ7gAOOkFqPE7h3_UuM2OrLHkS-0eNrmhmRgpAEaAowLHXHczRBBE3XItTM-zMJCrbfDUL3dnf_zJYBA7djAZnl4vlQuuotgBnEeBLUthNiBUlHXLm1ZZvLoHuvEq3SNOaIHI-CLim6nHzfuSdcAND8R0QKncyLrvzmd7LKXksJWLhkBPzU_KASp7reSh01XHqclK6Fw0jd56IEVOn8HmNRXQ04-rbEZIQ-O6vAxtUIpbymgzVov9sFBvFUoofA-HLdg01oQaNZGZ4E1CmMP-HVrj0BU_cqdgj1JoCLsPhMgfQdm4k46WbYEoi8mVrOXPLx1HmNn5_n4ICYQS746vbzGThCCi6X8OT5wWueHGNVyUIBV1JDU5PLJTuvsf8DfpGvfW8qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=KIbHKZYZmyupHTt8MFu7NNaHN65CeLQoVQtAOEaiaSGDGfiBdvX12VWkEoBY8DWBfc2RWCxbHyC08nB3eN7816oKqCQww2zzTD3FxLVwhY1ovkKW-45A11e2ghIhHfh0RG8iLwBmTCgWcCZmTzSqe1PQ5WZWj4a7MuxzZ47Gmfirr_tflz1mjTpNsdxZZhIgD9yFAkZ5gmq3W74ngzLBDDmoYDAzGBWwxWTLIwa4RyuA4k1d2m9pQ8e7RNo2RS22-ub9jdMfKNxR_bgdqBJnTmjtxsoHNEsiUZv2-HWbOmFAVfRmLVjzzeENcYdNbZgnRqut6p8eJ9wbsbmU_hiexQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=KIbHKZYZmyupHTt8MFu7NNaHN65CeLQoVQtAOEaiaSGDGfiBdvX12VWkEoBY8DWBfc2RWCxbHyC08nB3eN7816oKqCQww2zzTD3FxLVwhY1ovkKW-45A11e2ghIhHfh0RG8iLwBmTCgWcCZmTzSqe1PQ5WZWj4a7MuxzZ47Gmfirr_tflz1mjTpNsdxZZhIgD9yFAkZ5gmq3W74ngzLBDDmoYDAzGBWwxWTLIwa4RyuA4k1d2m9pQ8e7RNo2RS22-ub9jdMfKNxR_bgdqBJnTmjtxsoHNEsiUZv2-HWbOmFAVfRmLVjzzeENcYdNbZgnRqut6p8eJ9wbsbmU_hiexQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAWSv0TbJVAS3ZbPhjDzTqgCYna6_5OpObGhDB80OXhfKOn7LVisyvQl3SPYmnT3J93mZ0naMgAuVSTfuG1pGPu6IZNLJ4e9ZJaPT1X6O4oqJySmaSZaQOeQkn84mvS-h32g27EKvRkVQNit7HUS8BHZpAJNmoSaRdI8zANz9WZwV3qdeTClRVy7C-zs0HqvF_HS83PcHHJcwKxgGk33KHKAlXNc-4N7AABJk4FM6n0m_fIATVTybFRABkqAX7XA3nG_6bMc7ySRAgbSgGhAmJFppfd3nLHCYXuswVthwfh51kHaWnYDJmudHWS0_FfAYU4Qqh3aKf2opeOsubW78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=MVial86atOsyfMIlWH541ufdjwaJTbcs7SkXs22bSn_9I1H7M5fu6BSAuPSKO1nMLdm6u7oFX8-_KbKoX-2CjDdfmj6ftdyGLXOmmXavAj_sC6YSOuTkCk2flzCvWqixLkYrQJYUKBcg9LzCUbLBfXoSF2_svbkuWyai_gYjwqbMj7numlMIeE1OQ6Kpjf2lDpVMkIUKMxfC2H0Y3a_KKYYZbL1aZih6rijOMgzYEo-FHBSBj9qzMk8qEpg9okM3XMY1wjONdGzrUFt8nGAs_6aswsVHsf6tu4Lfcdxzjr7qk_P_tB4SgU8FWmNDTnpJEKZwK4mdzc6PHevDlrdgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=MVial86atOsyfMIlWH541ufdjwaJTbcs7SkXs22bSn_9I1H7M5fu6BSAuPSKO1nMLdm6u7oFX8-_KbKoX-2CjDdfmj6ftdyGLXOmmXavAj_sC6YSOuTkCk2flzCvWqixLkYrQJYUKBcg9LzCUbLBfXoSF2_svbkuWyai_gYjwqbMj7numlMIeE1OQ6Kpjf2lDpVMkIUKMxfC2H0Y3a_KKYYZbL1aZih6rijOMgzYEo-FHBSBj9qzMk8qEpg9okM3XMY1wjONdGzrUFt8nGAs_6aswsVHsf6tu4Lfcdxzjr7qk_P_tB4SgU8FWmNDTnpJEKZwK4mdzc6PHevDlrdgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu4tgu7gh9-U2H7PIsGWkrwwnUY2IpO9p-3crb-95UDYffgzrg9zgL5bXBbnqz8byqA3yUH0XHv_UdkfPYyFexCBaVlRaJV6diniGYbUpYMY2w0JcVaxSmuOH3wabtnAMXLwvPDdZ-nZvyVAvser40SpJYScxWraz-LLkv_7egQpgML5mE9N843wyAUtHbLc7JRuDK-BC2Np26qqaoc18Iq23EuLWbmudPHhQDrq9kDZVzZd1pJnM3ttpuhvSIUSsvontymjf9oIuhW7vadZ6lmFHmNmsTW_rsgNzch4oa6ItZGs_t3wrCfrnh3NxITtHvNLTXpZr-QDmjZZZRpNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGXlFu2UaaJ-P-N1-2J5r9wfjUsiOguwePsegEIvO5fAzReWfZ5VrKJ3-c4yX0Mnz4nzxbghrqQh3xoqe8tzEDbjBVZ-zNRf4JnZgXZPA8FQaaT9rFwZhHn1ysHLmq9jc59cSDtONk9DdkU4JJB2zlpC6da0MiiQNXbrfNOJ-WLGWKATROl-0waGpIl2HgdHEE3x-APGQCV8UG8iTE6OdECW0dWIWX_kZz4iNe1TikTe5VvqOZIEtP1ZrsUEwmUM9RqleoyJN4INw_qOw2ZAPIf3zplv7h6PjmsYyQLCp4GTJMfQ1aa5RKrB1RlEItBEWDoEpHZ1sD5IjJa2ncj5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9V2ltq-Tpam9MsOx1D_VFCQn07mfX0ejLw0Bvjo_q8XBI0N258r6ZbY1LsYGdGCzfljj6qSAjvCUk8-SE6Y6CN6nKm7M3LkIemLrkyv9vqIEhiT5RVrhtWLcj35lZzhAh6S2FiKmELAOWuayeuQdnH-x19dMOU3CG3IM_qlk2NJfpwZ4_p0SJf9MWUTIq9SsfXvksOgULvBzkw7LDD7dq2KGwrZvEXpP7LvLn_sfs-vsjtTpPyGi-wIpeT6vUInLTmDlXXY5SONqiUIRahHZGqQfpcoiijN6o5uAKbn_89G8LRNcjhXT0JBduRhSVUxoPAJnaGpFPLkDntBU7un6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRFICF7hI3qhJ7I-foKjczjU6O-9DzcCA1cXeVbT7b1_SXQ0wi-jAVRJ9WgMp9KPL-xCYny3MByG01NYJT-1t7MOj7uGL3jAF8G3xnmOFZ5P-Yjvwxlt0gCtUurhta7LSpRGyMz4JDEWlehtwlQF580OOyiWTBSMek3mlaZ-1yq9NPSll-iYYDEGMtrN0xUES066oqgk2pYs27P7NM4LlwFUxM2YtMNBptkwonDmrvfwNzfHYlOU9F6Wt7bE-wdhBZP4mk5KjZy3VH_1T5JXTsdq-MBsqow6BXV-BT_-O5zcM_5tIIlhADawNJByn2rx_3NlFhdpQgD3SiQ7G3s3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3yJUPr5bN3wREfT4w-MgUrcHlTi3uCT_nyp1oIKEdH1wmWY8YuNmGvQEQbP3bbYXJScjeJJNtCrO9WSWQeMSL8VXZeE4eb1ZfEJ4OYJkPGmYwTnOMdjRgbZdsGDSNts7QsEL9T1e40jehQ7LSP-yqhV7ud--cJK5z-sr_2hIWX9478VasC5jcHIhRgwOBUCkUYrIZhb0YfeCjMlBxbLgKV40uANAv75ebgTauEWuabWvc0rK3dQhKsZ3KNkQgokCiH6fMRb9xCi5F9NSGZ16g45BTgUvE8sWoZ8qr1E3OJxjUiG45JB8qZfj71uSGx1U1q7Qn7FNREa8e5VrPECPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMkV45XxAimGdsE-9bLJoP0CqSRvMME3B9Ffl_yDt58fTr0WPVkU7zVAzJtWfCrijlELB2Tfm4r45KJ7EwOJ6w1E9uqohwHsXyEEQfIC2PjhQml6RT4S9DIJ0OT-_bYV7NQYqVwYQACKuHuArVhVC1k6r0PK9gHHqTcy_pb9KSoCkJoxPtpCK2wh1esO97fxaULRYVqidyIzaCfoYKyZcYtFfRlYH6QAo1Sfxk3z59kEWUKEBb8dywNuP09DGAVcI5l5mv32xTE17oditUqSv8EzerWo4FGWoE_eDTqe6CKhY86pliDxivtQrq8R5fdGANdsSDcn0KHnrhVLkPBwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHGmd4zsARE0tJeW3lbeh3In7BpTQ_1D9gCaun1rotHC9f8mk_Ttwqmr8W4dFcYVQXAfHJT0zXorwxF1gDJDaZh2Jt7jQecGqt7QQPK6_IGLb4Xkx-L4BT-7LbCjRMbSfqC_jHperqZDNlWEhtg0qurXtP2Ubh8UHcy5rMcuk-aVI6ZzBE4GwA0LzXoQXTv2Eqzgi55pxF06VYSLG68FbJzUavYbqjmZrmcE4N4ezl0mYgKu_mUsDMOjGhxZxUQ74YPrPl1Mjvy7I-gEhMjDge9Nu2x6JVX0MXHF6Dc7KSjp51tEj2AwDhBSxdwwa5OvrKWMzmQ9vTIMQwI1qJKi6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXf0utSjyVz4T47CbErCsDn7xVW9FIo1Dau36jjcUGw3xdMEGsVoRzTpdk6hC_MGyIeGkpaMxl6rgTLh7r05-rJyr8QE8aJqcsoRaFnQ2Lsm8iG5_wOCdICJ-5JeHWr0plB8NJ2zDzWd39BNmgkm0J11HHzWCs3QnFy9UtsvNaFWfeoAGTFi7y6hAiLoHZZeEvOzlJW67TNnvVAVuO_4ZuVzU0AMqjw-VCOPUcoiquq90eZr8Ot3bN8JkfEDannha1YNniITS655XTGvEDUgHJ8QzJB4GFDppOt1f_iUEacnpkLP-VK9e_CeOZuCvwRlHO2uBJDsAlDhFoQ7X8TrEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJ2vkHBNBM49BP_JORliyDrHKCD3NbrRh6YQfqDz-2CJ4maT7JA4J6C7v2dZCdc9eILlhBoXEWaLZJ1Axrga02qldl9DPJpvhOZgh5g4WR6mcGuIYFZMV_3iJ-4H5unUgAGN9QuVuhEGBv2Mh65YXWMNbceC9dyR_sSpBQ0t_ESTvj--J3LYDDypdV4g4dXEar48UezMa_qdzDvad-RNC-HrkffPc-gkTX92GMIlR9tBQl0p2rsmkTfdo_FiZtGJzE_xYlE-EzV23KlNG4CSHnOSr7fwl-s515wOR2DWhstO2AEOb9oTh17ATSVUCyL_Y8_ciguzYZcmBm9wYlL9Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4mRFr0KQd5GZYYjE1fK-2Sh7yeeikba8yMBVFBLIUpKBqxxQGiVXfK237t5lgok6WXIMN8Y2-7f20_PV54B9Va-qXHSaY8nPqnVBWtwj_aO3UzGAXtDdqaQ7AGhwudr659q7UrE1HEHrTICvvSZsmQ0gzCGGPyRwwkThTAbwqRn4Z9urt5lqHUBrZoW4iuRzBogOdEcsIrO58ESY9yDrMBHbIIeljvZ-saI_Tkpj7Cv5mrBCWJFuaiShvv6EUXN8X2EXLp4GBPGd2TPmtyAqFuiHT37plrV8R2BDOKMmg3MoVDuHmyAGSkCQ7QNi_y-1F1oI4iFAJ88U24jn6GSmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=HQ5JczqRM2onNkvbqIJZcaUrV1x6cy1ohMXFBMMSbNmgiAbb9lO0QFzbuWLgcm73-gbBFIJb1jvbnGAuno7WkfeO_AGlFTQ8fZE4xayGw-PWinu2w0KB86CZgXKVO3q8Vy6fM3hTefmUCUruDwJK2TeTCOhWqnQ9CZPbKSNn0FbDMUAJhyVBOXWyOpIOsWuK94K4Rq5RL8upEvnjW8GS_rqWDW0hxUxy1iyogjfzfMzyNEaR3bVN5vBMMnyWzrfsyeMXlU3YH9KUHK5zFi1K7LLaH1htIx9pjlJ4nvHLL7gBDerjVKpd4MgObpRjXv7IKsOP3IVjMvKUSzRPLHMttw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=HQ5JczqRM2onNkvbqIJZcaUrV1x6cy1ohMXFBMMSbNmgiAbb9lO0QFzbuWLgcm73-gbBFIJb1jvbnGAuno7WkfeO_AGlFTQ8fZE4xayGw-PWinu2w0KB86CZgXKVO3q8Vy6fM3hTefmUCUruDwJK2TeTCOhWqnQ9CZPbKSNn0FbDMUAJhyVBOXWyOpIOsWuK94K4Rq5RL8upEvnjW8GS_rqWDW0hxUxy1iyogjfzfMzyNEaR3bVN5vBMMnyWzrfsyeMXlU3YH9KUHK5zFi1K7LLaH1htIx9pjlJ4nvHLL7gBDerjVKpd4MgObpRjXv7IKsOP3IVjMvKUSzRPLHMttw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5TMK3ySpTpOmZC9czl7JprVebEKcZ9dwNFQUkrqaf36bV0BCywL4myUwGSPGdRFOgvesquEfKmZVstTGvviLKaJREngT8t8moSrwoieApDeP9hnNOtgsB0SFjbwJ5OH6GqIR9NHwho4nxf7-goMagsjsBUDYORy7EZJVXEL1WLmOJQvDzA9rUrSpWmAyGO0qYJ68MNcuYThNHkpR3IWBeOYYo8asG9h_3N-HcTo-u2z5mtguoXYEEheDW4JHm_RLkWxItL0v5d_QUhfOSb9HIJUkKx-v7Uzr2xyMZjh06jPSYU_rzJKAjvcObMyQB8m--BLEVXsank0lN00EIHcAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU2l4dbY-kyJCfRJJVskZT_ec40eIOAEEkM27ZzLsqXfyIeQgrZwqqRZiuLuCToDbg8qSfTcwArJfZ1CKoG2G8Op_IKH47Gh1cX7LH8njoKROjDUZ6Pz7dZqVE0kXAKQvyeZZInCHj6tLHGdWOXPEF8fC6Z_qo_TBQ3W2Y-HZNCZBERl5tVDMGlUAhS9qY9JgAkWYMF6DLAYfsX4N4ShGUXK0VvPY-tVKS_sg5fmR8BcfrAsmyqStfdMllFpX2M2lype12vtOfNmPFydw18aG6evZ-M1WMX5c9M8sjNoly1Ifpz021e2d268LXoRyp98BnpqRzTwYqZ9wytFfQA5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=EPeLykaGI8YmegUUD_ZpIo6WiM0nOAbcQZwTx3wEWQdcLsIQdR61-gPXSnDebnvqY_g2QXopC5Bz43h-Dyx0VE2uCRUngncBRD7xGwKv_b4fKqS15pDrcQ8J27FzqfjXNk9DSfOL5CWJSKtB16wz0mLDQ8BMIwyDhaqiK0QM5WPpVIL1fewptde5beCIfD3dQ6aA1HjCvBV_MkusQRIUw8_-40rj3KWQYfdBdGm8hgwrLXh-UkWccBwPqn6M1J6kmK3YiZdLpRhdYzEZmsplZph49-GAg2HMlWo3Hz3Scfzb9JjtttHvduM-1-KRunbxJ25CZsryRo0KZ6qUUiJ1oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=EPeLykaGI8YmegUUD_ZpIo6WiM0nOAbcQZwTx3wEWQdcLsIQdR61-gPXSnDebnvqY_g2QXopC5Bz43h-Dyx0VE2uCRUngncBRD7xGwKv_b4fKqS15pDrcQ8J27FzqfjXNk9DSfOL5CWJSKtB16wz0mLDQ8BMIwyDhaqiK0QM5WPpVIL1fewptde5beCIfD3dQ6aA1HjCvBV_MkusQRIUw8_-40rj3KWQYfdBdGm8hgwrLXh-UkWccBwPqn6M1J6kmK3YiZdLpRhdYzEZmsplZph49-GAg2HMlWo3Hz3Scfzb9JjtttHvduM-1-KRunbxJ25CZsryRo0KZ6qUUiJ1oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=eXPBkqqJVsjO4WaeA8ot9ceMrWioWr95yt3v51Sh-LcfzjOKkpvAOTfUbF0VmBqPEMEjyJfTMocgYOPTasaUJsQwbEYnhWAubcqHOc0qdhOo_TZHO1GNjX9gvkG9GbPTXekXK4fFPQ2j0Ad77V-xMcA6XW7gqQDsiQMY4cKSP2bJZiUZ5cIevQnEepAoEKagZ0fsVw_gPkaF8r9pmQi-raIX4fdFtYuq4N9SJ5FBFzCibmDITysdRc7ILu0cUjvLjgDzKJiq9DEQlv8hu4X56J2nR6-00u08T8j9D-4tL1p_q1pnESXgkRQs9XD_UGBpf0GUvIlJVg5f_ay6XzOLSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=eXPBkqqJVsjO4WaeA8ot9ceMrWioWr95yt3v51Sh-LcfzjOKkpvAOTfUbF0VmBqPEMEjyJfTMocgYOPTasaUJsQwbEYnhWAubcqHOc0qdhOo_TZHO1GNjX9gvkG9GbPTXekXK4fFPQ2j0Ad77V-xMcA6XW7gqQDsiQMY4cKSP2bJZiUZ5cIevQnEepAoEKagZ0fsVw_gPkaF8r9pmQi-raIX4fdFtYuq4N9SJ5FBFzCibmDITysdRc7ILu0cUjvLjgDzKJiq9DEQlv8hu4X56J2nR6-00u08T8j9D-4tL1p_q1pnESXgkRQs9XD_UGBpf0GUvIlJVg5f_ay6XzOLSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arZUyZG1IPAMFwqdts8BkxjSxBpAO_1aBmOBh2GQcfE5y_k_k2NtnsQvOGfTxuS7WXorykkCcYgZtHlfc9IUxNrSS6XddS327-BgkeRixmncKchBkzxm1bLA0mxtNaVO_DAC0W7PJ-NeFVcTOmxJabjy0ZCp8QzZQkg_YHLS9TMLXcmIN2l7yfYslg0RRK-EEkUETxzAY0W_HJqvXOk_D8kYyFR3JxTf9J_iXY4jMPnO7LjyxL_aEvRagckdkcMH_IFqziUyXvG-RccSso2uR_JZ-XMVSu5mgRdRXKUjPVzaPak65cUtagO0W5-gySuuPaxurj644teIVOBcKtiXKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqSHHxxKNQ7wBYv-Pz_bkdJy5D6Pv1Sc9RoFysPDvSy4BuoL_bqxyaAYCw2GVkfHxFDCQ3HIsfMfmCGkkZrRIVQLzLMgDnRvYSkRkYfluXOkNOygQkjooSLzRZRuZxpcKvGB36hlL_Hh9n2GewsLFPuJicaWXZI-ks_KLE48Hr3_Ucg6CKp7f99pbfOknu_GhVgKwfIRpMZNpgqgStDuofVrorunRjzBjSTcZWWix71APs1VhWO7-PPDJJvLclZAaNLJL4TjwCupB_ImvvXSGb4M1Qv9uh34-6WiCVMiMK4CPZ7iGKlOgsoV28wZ-9ZxjqJvRTb3o3pqirrNfzSfgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkYtJIt1IiSBJLQD2cLPhn2D7APN5EwqwWSJpuNXQw15fSKeQ6-UfZWlMv8s1mtgqCGjIyJONEVa24qsqyZNPPLGgSqXlVMO30XqEqBsoU9KFMMhelUGQw7L3-8RIuKdr_sH3CPa06bywtwo61EaPNrouquOzz510AzqoFt1Bu8qai36fnqRCOalBV0enNexZx1tANHp-TUhwYtn0nfmxEGVpTCxvtrpBeSTVQOztWsAReC7O7VRujzAYrMfblww_acgA6R0q7xtcLZD4hs2grj1jDobTtteF0bvXenrbH-d2ZZ49CSPkThvOtACGiezODGX1-FpS4p_o62KVkReRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZCSBi98trKhh9d7l5t9ey2QDp2L-aaJ_Z_rDuNLdzfE8bXzjGCi0iBMRUFlLr_06XPVsGn4lOa5D5tT6HqJ372K7cNbVYHYV_ctVmjuLeNSjzDQ_QkMO7F-l_6wbutMED9QWtdk50cntYuSpNVZbMdSVgZA4HYINtUUoX3Xi6a8U2kdmc-7puIGpilIQ94ImMwDs1AIm80JqcI49jwJ7VJFuEZ5STecGOHigyE053yOnjLTq9-9XO3LjLvf9ZWCMrC6KdyUkll9ScIyKP92FyHRbD18gMOMH1GSGkkW_UAs6o2Wjyx91xHzHOfKX0aZxPXmcJkzp4i4EFN-r3J5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwmGnaI436SWGQ2LQxkujJCfnw4lookKmZNZKNaysPh3WOvKtATAtGJ4l_yLmRA5Gkf7WFJA_UFoFMmMH_3xOn1ra91yX2HmnjcCKHMRhFMVw3_tBq3E4DIYiZHMqRtp7EeZNMxuKbYGW2NQDfCo1P2sqgaT8T8MlN8hfZOrrM3P9HKqOB8XiDrFi3-m_m0eAZGzOF_6u7kKXFj3JdDrT1dCSddcOZAPH-8s2M1Bnsb1tqunsZu_RRRuCv7vLDeQyUPkgB2VSXqmNmZEsjAu9pDeHGuApGNQ4e6afCVigZ1mY43xNOb49LQJ-x3Hl_yorgk13I1t6O_u-Prx39XfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glpkazCu4pACUVPqvN8A6w2paxrqxsGr3Ti7wMYHn7RgmOo6LaMW1KSAbhLtzwlsHcBo2h6hAnZODxBvHpH-73tmOhojM67uRLb2xzE_FPUUF0meq8oEjzzMvDVucPFJQY5MPkggfx7yeRtm0nQ6Sw6jzSIuwwJy8H2YP-mlKu7t9V2UCjDeRDXRcThMV1dYrU_n1sKzfjhgOxmlH1vGu9R3OPWVm44j2EWzuD0rC2Y8WQFMsgjnVSIIQucnKfbiw31dlYI1xlczmWN0VhEfFsGegqSCkyEic1wHAvmshGCAeug4h5IrOBd4ZICsISVseqlGSPeaeqYA4pe-1lxgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l73Om2iigUZWxc3QD_X4a_ixHvh31a_qkokjwQ3INLND_WY83E8RW2ZyQYvPOgJQUnUy0E1C66JLYqjOLGxmEWzwyEPmsxGFsuA-HRlyjqNyaixCtVvNuX1wl-LLhbqEQoMOwPtsT69v3wmGO8lYCjPeF7i4Bqphmw-a4yLB-XUeD_9LWEpU0SA9kjjAX4K5gP0xJMkyllIa053lqNYoYniwFokEVa-D8urt2zor4ZeReMb9PU1pqqfIiKx3T74kffK__bDMPfVOZeNVwRPLekCyXcows3cOqR-SBHlyPapIvptmYf_L79Ko8wd8GypGiuW-YQjBODnGp1KlT3t4eg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=nH29PZEpaV5PfUSL6y8XPIyG9yuV2h4OeSO6IzIhUaabfAiESrKASjthB7pkN1o841NgsHQGCB0ZgYUq5Y88qoZV_4v40_gZdlWWNvm_UY6S2FAG9k003HpLp3fOECc81rSyYXdldfCoczHzTVhViPtydNWsO-pYIwTEiq6maK7DvZVa7tH6U5KKJG2xNFWyJMmXUUwlOR_vqGz7wW-Gq5xCDNdlS5SuQhts3_QeSdF-wWqmpsdTbzm4eQ35c8PDGCDfMsMFMzWDeOGWrEpMAHsv-RsCQC3bBWs-HMWOSxRBKfl3Xcs7PZeLD7e8PRiKQSp2dsewSr9r63UQEYv9Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=nH29PZEpaV5PfUSL6y8XPIyG9yuV2h4OeSO6IzIhUaabfAiESrKASjthB7pkN1o841NgsHQGCB0ZgYUq5Y88qoZV_4v40_gZdlWWNvm_UY6S2FAG9k003HpLp3fOECc81rSyYXdldfCoczHzTVhViPtydNWsO-pYIwTEiq6maK7DvZVa7tH6U5KKJG2xNFWyJMmXUUwlOR_vqGz7wW-Gq5xCDNdlS5SuQhts3_QeSdF-wWqmpsdTbzm4eQ35c8PDGCDfMsMFMzWDeOGWrEpMAHsv-RsCQC3bBWs-HMWOSxRBKfl3Xcs7PZeLD7e8PRiKQSp2dsewSr9r63UQEYv9Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLMRy64o_b2i4zy3SOjZWYFLh9u9l4QzMJm3DAu-s8VqvH6-bAaFd5KBy7e0LHHV4S-O_Gzbon_vFylC7mbdqeJ5r9xjA53QFiOdq1ElfZojdoRUvNYUpKfkn78s9aubDQ3OIcI9DSJby4tgFwGtP4VyUzrRoByOujrbBf1lCJffCpMMNutqCbBURCvODQolsKIw2AAbNSdODA07texxqCIOVOenniSOvUBDjz4Smg839AkRmQFZH7NzFFFhW7KH38kO24o6F6LPpzkeYeuD6wMVAliu9iMVbBlTG57HXRtEcGouuo3Q9CbO4fdVrg83mz0UEe4dAeRuvTImwBQiXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=DCH70RzCujvQGzeuKPihXI1ogAnSC8Pk8pLceFQ9vgY5Qg9AjWT2S6lFPLpqPrlDkxB8Sau0CBB0cYYxhJDPQQvqxjVliCLmLteL8b9A4Ark1H4J6ybDnoLnczZZL_jpXGcsjPKu3t3_3Eju2G2btRwqgLcTP_wCVMIZBXsIVXZPjy8HJ5HdRCLrxSBaJYBHwF0taBvyPX7F1473y0kcvNROh0nvlOxkfykSEgC_Zyn-mUaKZi3nJ8DUmx43yeyGX69ZOhu-lH6RWMEYPdMU7LZuDzJ58W1GOR38EeHSuzd1cgglm25KMg8gx9RRFP20eN0USxaJmq334szoJsSdEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=DCH70RzCujvQGzeuKPihXI1ogAnSC8Pk8pLceFQ9vgY5Qg9AjWT2S6lFPLpqPrlDkxB8Sau0CBB0cYYxhJDPQQvqxjVliCLmLteL8b9A4Ark1H4J6ybDnoLnczZZL_jpXGcsjPKu3t3_3Eju2G2btRwqgLcTP_wCVMIZBXsIVXZPjy8HJ5HdRCLrxSBaJYBHwF0taBvyPX7F1473y0kcvNROh0nvlOxkfykSEgC_Zyn-mUaKZi3nJ8DUmx43yeyGX69ZOhu-lH6RWMEYPdMU7LZuDzJ58W1GOR38EeHSuzd1cgglm25KMg8gx9RRFP20eN0USxaJmq334szoJsSdEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=WiHsHQrtsf238Dufmj0nwg_OUx7lT-g_aPmRbl971dO3dYDnLfgQHYQ24iCGW4MC_v5r4D0kwsUAVMLcEzVyEyNi8XrdEN6OYt2-jg9R8l46Ntng58Qbwo1Hns2yCrIhqSVuob9HIMbxCDE7IkAC2YPRUbsSZw2GeiCDRMD_QELAch2USrFz7DSX7V4IqOmrsDt04GMJns_zy1I3014ljNGj1_CW924Ii93jNJiO3I6Xq3hukHfdDFkIZEOQO1fgQXh-nVB-nJ3iD3J2fap-Bs_Jwn25Gd-YDZnXF8dYvEsVe9UIQaY4Lp3a-Oyv_UOaxCmFn7kpgB3C4OYlzCtP8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=WiHsHQrtsf238Dufmj0nwg_OUx7lT-g_aPmRbl971dO3dYDnLfgQHYQ24iCGW4MC_v5r4D0kwsUAVMLcEzVyEyNi8XrdEN6OYt2-jg9R8l46Ntng58Qbwo1Hns2yCrIhqSVuob9HIMbxCDE7IkAC2YPRUbsSZw2GeiCDRMD_QELAch2USrFz7DSX7V4IqOmrsDt04GMJns_zy1I3014ljNGj1_CW924Ii93jNJiO3I6Xq3hukHfdDFkIZEOQO1fgQXh-nVB-nJ3iD3J2fap-Bs_Jwn25Gd-YDZnXF8dYvEsVe9UIQaY4Lp3a-Oyv_UOaxCmFn7kpgB3C4OYlzCtP8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUMDoQLXNvmajlTRD17IDTrOOuMWdfA8R1ykNPre_SrQr0tqNjA8iqDKT_c96lwaTvc9xooENawVR8miXJCplElTMzI95u8Udi2wkVqOyCL0FYV0yMhl0GU_MEVnKDokC_HydMBTzunfKx7hlYI40O9EiFYOIYPYcabBSTgvwzfQEtUEi3mzWAW40GXVwx_pCHIr0L4if-LPEUAup-LXjkiUFYF7c4v9rzCWc12wWYHmWS5BFMLcQwTJ0Q5SJyAdEBUpGRzCIf91TrFHCJ7I1Me7F7PUfnP3IlbOLTj8XJ20eGui18i4v_FlSPYnoPwHQY0MEnNdO3gbi5lG3UGPdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyQ-RjSOY1kUUFaT67V2PBO186U560NebmZThSKPcJJzZGnHeMrc-06UPqeGaNdvHDX2lPXWC7-u5samyp5uSZmLOVhS7ZRuxl-_oxktsipP36gqb1e7Aw_jNGv2JZ1bV1L_6ZT7kt3jOd8nr-nfG8EW_GkJAGDAn8nyBkx-BibXWXuPOIkztv0j6Mg9lgvwAnKMJrdPx5qrbKenASC7cdVdiPAG9gWDQZqllKFVENUHSkfv5hNuJOzNsZK23FJmbpJOXpblYdIfNHk2pjWmZJ0x3ZkKdj9SgZrePDnne-jUA9PZ1d4WxBdKYSpmtsEJ73GhW4Zx_XzKGJ4KXkUD2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=jWu0z3LRZ1vjVXvhYD3AtrVbMDPCOwr2FKEyDCp7pdlvuv0hSHfRmieANRKU1GEYLIalWzcGAuERIVZnsoFJvxRMYEiWIHjuqxXDJUCXIrLRh9ln8GewyDpV13_dl4TohSeK7XL0xthI1kpRKE5ruIP0v2m65TRznVhPLBKGAlg3mJNVDROs4av5xPAadWfj77TAABNi35aiq7KR3EvMg63vyXJdxl3bYPAWnasX4gRcHPc_1y3m4P7boLunJ11BQwTAOIr-r0Z3BwYFS3-N9LOEr8WJHx-iky3wwG9eNfNoj7TAOe5pv1X2AU0oNNFLkZDP0_Z3Lh9jdzb4b5qV7UF4oHC6A_-l7d4jLfYggd1HRgzk-pgxixDtF1NIN6c8gOHsciI5b-upWtDcgiiYrht5roxvEjngE8kMfQ0CTbDKMTL2DKsRqnekS5VAFS0ymIge-fiyw2My2joyUXZQ7j4ggIo0W8OXw152g3en5pIX0znJTwJjpX53620tPuiq2YwDwAYqXq9e6YxdG9pAB5YlB62JAINH5PN1t3At46619qGvNipORQhcK2tBAHopMN0V5p7Qf9scyPG1sieV_jwjCBC5CkQLYvoOY62fIjv4o_7G6_SLb9SmSoWBQsSPzvjCapu9XPyaLloSYRVVugcDPao-k8XuyKyMamq59dk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=jWu0z3LRZ1vjVXvhYD3AtrVbMDPCOwr2FKEyDCp7pdlvuv0hSHfRmieANRKU1GEYLIalWzcGAuERIVZnsoFJvxRMYEiWIHjuqxXDJUCXIrLRh9ln8GewyDpV13_dl4TohSeK7XL0xthI1kpRKE5ruIP0v2m65TRznVhPLBKGAlg3mJNVDROs4av5xPAadWfj77TAABNi35aiq7KR3EvMg63vyXJdxl3bYPAWnasX4gRcHPc_1y3m4P7boLunJ11BQwTAOIr-r0Z3BwYFS3-N9LOEr8WJHx-iky3wwG9eNfNoj7TAOe5pv1X2AU0oNNFLkZDP0_Z3Lh9jdzb4b5qV7UF4oHC6A_-l7d4jLfYggd1HRgzk-pgxixDtF1NIN6c8gOHsciI5b-upWtDcgiiYrht5roxvEjngE8kMfQ0CTbDKMTL2DKsRqnekS5VAFS0ymIge-fiyw2My2joyUXZQ7j4ggIo0W8OXw152g3en5pIX0znJTwJjpX53620tPuiq2YwDwAYqXq9e6YxdG9pAB5YlB62JAINH5PN1t3At46619qGvNipORQhcK2tBAHopMN0V5p7Qf9scyPG1sieV_jwjCBC5CkQLYvoOY62fIjv4o_7G6_SLb9SmSoWBQsSPzvjCapu9XPyaLloSYRVVugcDPao-k8XuyKyMamq59dk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbL2W9iYVV3lxKcx_AlmQ3l7T9MClaPYP6hRevhHuxeddMOmcL7u4ZuFqPgjJcqoJV6EO-isMnYo4eCnrw5QcxHKaKja4L_-n6gu7BUbknHWyIb1ZbNSbMYoIlIVLL8QUSxZRxzSurxAg6mEXoBt9Z-p8XI43Gea5_NllS9naYMruAJd8SNM53rWIr-6UWEB6nrkvXcADn8DG-KYH5YA73tlRBvgPc9-3bkcvxvLgybTGW3S0_SMtQeNTr9hZOkxVcfvkknLsVKQIJNtoZe_9K5f9JJuLn-vOteUBoBCLvYUptVmxdO0JhJDQFOSO7aFfL3afp-H-gF-hCYfXC7LBg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=BbeJX1h2UOppkS0gJxAsKkjaVEFUDslXSe9EmRzHcM5sVPnoCz2IgJfRfdyTHnLwuCe4ZjaBl4nNyvX-3aM2fKeQl8a-g7nK1GzAAHl6IudQlEL66DhhnpnjbUsCPuz49QIY3t7A9AfJxS7uwXQl3Zc4Godp57xX_t2d2WVrBnuehUCFdORR6yxtNgJz32x_dWnsJA8BlsJQG1bpQG15W-o56UkhvTfbCrIFgmOO_8UZZxYbti9tZR_nV0e-dh5LqYTY8gfqRap-y44BJkv-wu92kNzG_RGmIYE9T4Zt5ADGXY3SjaW0LGMxEingM6fAL4YIbu7H3UTggPv2wqiRGnSPhPVJtXJz-UVTXsQIepl7byUk6-5-aoI1ESJOXcX5VuIHuaS6HlfDomDwcpi7EUU_-o-S7qXUBb4MnQYNj1tsrclMKZ0By03Qi3VRB9C9dSCmyoiZVZJJporwh0RSk6bBzzELfJivFlcP8Nq6cPTmglSkUzudlL66wdcvgW_mzkVF1e5XQGt6jEDMIocZDJmYNLwsPaUkUtHCZ1j1L62Grs8lRpMMdfXHi2WLegIghbcXIYzRK_QaaQId1hYYuPJI9CLGUc4l2dTXt68fzFBvSe5XvUfVX13x8rPBARANMFZiWOfZV-kmdODZ8KaCEV_dldyTN9Gr1k6Q-RnZYAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=BbeJX1h2UOppkS0gJxAsKkjaVEFUDslXSe9EmRzHcM5sVPnoCz2IgJfRfdyTHnLwuCe4ZjaBl4nNyvX-3aM2fKeQl8a-g7nK1GzAAHl6IudQlEL66DhhnpnjbUsCPuz49QIY3t7A9AfJxS7uwXQl3Zc4Godp57xX_t2d2WVrBnuehUCFdORR6yxtNgJz32x_dWnsJA8BlsJQG1bpQG15W-o56UkhvTfbCrIFgmOO_8UZZxYbti9tZR_nV0e-dh5LqYTY8gfqRap-y44BJkv-wu92kNzG_RGmIYE9T4Zt5ADGXY3SjaW0LGMxEingM6fAL4YIbu7H3UTggPv2wqiRGnSPhPVJtXJz-UVTXsQIepl7byUk6-5-aoI1ESJOXcX5VuIHuaS6HlfDomDwcpi7EUU_-o-S7qXUBb4MnQYNj1tsrclMKZ0By03Qi3VRB9C9dSCmyoiZVZJJporwh0RSk6bBzzELfJivFlcP8Nq6cPTmglSkUzudlL66wdcvgW_mzkVF1e5XQGt6jEDMIocZDJmYNLwsPaUkUtHCZ1j1L62Grs8lRpMMdfXHi2WLegIghbcXIYzRK_QaaQId1hYYuPJI9CLGUc4l2dTXt68fzFBvSe5XvUfVX13x8rPBARANMFZiWOfZV-kmdODZ8KaCEV_dldyTN9Gr1k6Q-RnZYAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmHP386Q_tkONshPcXiQHBaTwX1_ko8qyOGv68MY3n0d6XpKvoH0-dYifzqjEzVk6OetZl0hynPnFXfKgfVqLc4lJ8xyIqP4_IWhxhp_8QVRJ9kok10qHdsZ6hXnq4QsU6DPE46DAsF67FpjNPT0oM7VgGVBCvh4ZEnUgCstY-PgfiuCIfd5pOJ1Hfam1mMu6wi1nu46o1G6jtSQCQWt7cCdFWo_FqTMi1q2A29SKKFWs2EclG50Z-yv5oVe1ogwilX8bMPsdB9xni8KiJWzunGRkfl9MXeAvrN0q3aNe74CWhe3EfnGW0WkVCJtDixN1fsKqolEFpF9ww-bYpC9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYqiK3dZbtkiB-PPDeDVX8xvXtwgvPbK1Y8GXQ3lpoTn3Vi_vVx2CGyG3jHufVJh6iginzptGEJaKiAHf2L_c-9kFO1J7s0_WwSxLmNBOtdA4oaWD5G3bgpoIj9IJbFfsaKfV_uPSRXATfXoU_U0-SmvXtZhobndC5mWUsTv7g-gnr3DaX9sGcAH2NCZwsA1IyKufA3DaBfZPPTj_B0txTVhFpp-Jn5fh0FS10q0kA35Gu66Vd8NcJSrk2ie8aMk9gwL9aMNtPveUyqf6iVztV0K7UUb1_0SZgC0bAhytIx9c9y6CRkkdVoYpKp8oy9wonfUs2kk2M3elL0Ma0unXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmLqPBF2TFubXA03_1b_V3D-b_6vN0UcQtjZN1apHkMpdK3X253wkk15luTPa-hW3qH93pMdEQH7CAjH-hkNMSkeua9_AbrhIf2vGF6VP3KTNGiMv-0zXQkaQTxsPlA3qwlPfww0NJxyDqzqgGLYDLJx8fmoj-cbL_6369KFfigccbxQA_2fmC7OOGP1tKiS37LSmTzkzDtmpimX28Kc0cJkXZNJjhpUYMnsdBWwOb7SKz7ZK5A_RIDnFRU7gBziHJsjzJk9bheVPNnLSREi_eRksh6iGyT2d5viIBxo5qwJSCuCh2pgRBCSSXcMxmvz7Wfp2JFKY-razvYD9en89w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL4Co-JnRI5XJYUTViW3l6rS7dttbmz2H9t4ddfGC6RxJ7yoeV0u7NOMHlSUaC_mQBFFWkVaJRduXoDp-p-Wqrkz84WfQtwj0-IoQGeuqVKb-7AUQFoX6EZFOTvp_d4NmoHJEy_GK3m5tUpail6A5iCblx9VS2MOENuXy_SGp71a1QjHRbbtoa0ca5G0bSzojWI8Y2Libk0tssk4NBkS3Hfq7qQ_5nnb9_7tpeEkH_KU0vwfK0y9Gj8C-Wa7ZHvznoLKtf2V4sWqVy3XpYw7ec0g_U2EEXXlcnpK30ascvIVQEXJqxk8EWeCtv7uAfLO9b5jGIeTgEDrwJInz9Ex1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b45SKoN-2Pa9r82jKLbu-mkDhAp5eeF5c9hr9KA5IEQKEya4Wkn5I25nf8_fKisl14scSFHK42p8OOmm2jsY1E_sXjHlcoN2-9bjMTePBNLG1YDwiD4CIMnupSqcD-jhT2l6prFOQMX5pOVnT2hS3EsJugH7O8bg1ArvpZpm4e99TFIt3yM4PUj90Ns7aP8T3ujNx8nos2hcaNa9PghLMlHfgRKAaLD23gJJOZGFocawSoWk-K-lR7qy-C1Vnsdn4Bgp1vCFQLEG7KmOG1VTL0nz4S99rZ4aX5ok9pxtZVIO2lGHMZRlLj-Du0AecnGE_PY8lPJuaVJEYj78FJEiuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EECHslNnerCdLNeCuyDDgNAMnKrrMPP-Y8LUV1jUlbjVzT0ziE1epYmTlGCycOF77TImW0Cu-bfX6EyjjBOVdgs8TKcI-Y2BAMro8VjkmYmnrwwHDjwjbzON_0sej8XGnbb872i-YiFL9N3-zNIduLWnR09LYHcSM7hViT_9hys8R8I6IwLNKNupyPpRkYnYxXKJshZoRg0FfUCEy9_6k6bG4n4wsadP-TeqUvEVCigMDWNsXm9e8CpmdK_lrcNJXOFQRvR4CtdzwTwmZN-SzbqkYL5Pi1ruEYrdR2LzWU3jotUv733tNpNtNA1VWtZn-EC0v_u9ucLXSxgRF1R3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUMfXSYKx5xXYVfk-OSyloBPZTsJz9tzhLr1wzVFdhGVp-BL_3aVY1cZeNBaafTW46rx7oZd-B3sp_oMsfv9AdpLQV3DqU_M-v_Iq01vJszplAwUU9ceO0CvCx55Kee5EZgOu9fb1FGR62ZVcQ2hMf_wcfErur8cJ16q_i_ZsDOgf5CaQdH1yrMOGHXAFbWEwGZDBD8zoslSDUzu3UsKHCSOxzrA9gEH_GDZpgYlVch9LK0i07qWRkTLnMsShwkHl6dmZRWmPS_3BtpabC1Vgy5F0bArAeZhJy09z_-iAJTSTe4jvnpoLIsl3vYbdPdHWZx8gj4jQdiekiJPiWhgkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMIFE8Qvm1XXjP06o9itQczRxaoNM6VgMlPzQoV3oGLL3fq00_jnOuYc9m-axCyCqQnfjwZ79ewbk89dr-2QucB4xtFvqynEnDU0Dizra1uSlYwOuLHEtGU4Uv-isMY6Wdyp3dVWPIwPkZ0UOSv1WFE2IYr5GAvXt2K_PdHXLZ8xRJEqFraZgokrXTBSrk4rijpQRY91ItucBPy2JAxWnhCla0ohGeJ8xuDz3awOQ9T0VFkchjvAuWmYYqNzNXtAsOH4noaZnNx4KIJaI9YQO0xpzv_mHdUMW9J3kMATn9ygomwlH2rNiucIZCoI2hNP8sBUcVkWF4g9HIL60QpxdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VihzSuSmrDDXuLWEuAkgp0j6x4tsTThA4PL25g_kANQyaAHBBYtCv7oIKdGRPImIjkJFgDOT3qpFPYdZN51RSk81lhakktifbWgFFJU9pg1RacKqK_a20_WksMEe62rsTwu3viy73Nef9Dp3XKy-HfRCdYqi1kYoH1gVSHLcwoha7F57jNRmfnja0EOJOxHo-DgrsxtW5936veT_LZ1qNfaj8-eMMy4vBTPOdv9UWhrw-2s4Duuz20fUxTK1lRGpA-fq1iioCKtR5ANuZV9CzqnoZ9MOweErpGG-WtCjAHmt5crIGpTnVFjFJvXrwV5ui7Vc7Vp0LWdfdFmYQbbgig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogUg5tqVx97b-SFnMG9cU5IsZ-c_P2gYgP2gwExxrW4emalUCGqAseBu08dQHTLkpv-jvd4q2JIwCTUNGwGba3JdCBzVUgMtssxTkRpArAJHX6Cp8JJvNYP9rGv_v0WkViECtHc1MfGJkgPqB8vlzUFatAiCaoScOI9bJAXpaUvgohDWMAlu-OjOFggqRjUThKDey_o9biU_js6FniMZpoMpn-H7LNAZVYuqzzIroQFt35-IqvthmoIEvXusX6X7UOyOzxnCZBxxytf0RI99ePeNOnwFdkHUpizGE-FGK-l9ZQCy-Ovxfo0E1FgstLNFNukq8LwGts3qp2YNamqppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmrPMGCvtV_iWCtegIxOBh9TdYVt_0Y0T7RxJRzgRMnIjmq8ZUBOYih6wXCeu1wdsNj73zHhi7daNdC0X16BkjypsbGYaRBA8oG5dnaGwc0NEzhf5UFz2QnNGWvUo4mSCVakY8R6JsaNypDqvlq2eZD7LnX1G7-GTzjbc4GFFIhHnl2m1LI_g1WIG2YCL7KmBJ-T9BV8p35GEuFBZx0ceJ3Vs8oEdok4oqt9rdE87gvCKIVxvoey3jsrnqPSIHwkrfI65w018Rqos3p44ZFiGAbnNX6JRqfkivwMiqKHbyXgtbQ5yHXQa7ytBepzUuXzRbCE1yFjdbjtaybKirRPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZjpwGoqRv2Hz_fkdEbpWcbjN_61TSVDNh1XNvrWBGy9vWKqi8_BElO_js-PkypE2UMCijxRU2NsWInQBxF1Z_xq4_31ZaLaUD5H0G3ayJf5zaS6_UwIFrg2YaaelE41tnLiKwm4_bDlQF7wUDskT-hnNG6xhZb6DF2oD3fZMOvElCAViTn-EHzPv_Arqgh7gr2d5fgjODMFu4xGnrHNbtWmzTt2Kjd06RwVTjExxyenUgOm_9kKflMHBVnQkZoF4npuJM9158P1A8f3T_objER6tW7W8iv0SvLFjElzqqIEHNjPKNSPgfmfGfnDwUy4CVLA4gc_hJEXA0ekfgBWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXoKt04axun6ek_l8mymAwlOG_sYRRzysZSS8TNOo9Gnrv5u01qBdINuYuOyMWbZgSbQOaht6hb3BcNj4IJpvI2pbioLYGnT9yNPLlxp8_Hvdf9VhCZfq9xXnmTD7Oy7_8-Bbvs_6rDJs-mibcpvd-xjGlfjUj75WlmSum5atX7U3yIJu97z9UDdNGM2MQXDBe0ctJO2_vSOpYFtbTaBZaqyA0fP73tKnWLr5-04xnlokQPP3fObmlZowsk73s_ZPOXXTNUAJk3ijekpHnfbm_rf0J3TczakSX7anNASeUtqV4LKJ5SwLg7gjo3unYxcfuOLq7NYVPjKhHJr6AfOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z26w3pR9MQmyRxksbineVbnTKXHo3mEth-KjhOk2YcnrXgnhYlCD60l1yK-56c3FDjYZi20LtsvZvGZPeDfsf1DRCKpUKOX6AnSkH7KorYB8FTUZWdZMMp2J3pjTtVn2WG8j2sJN2uuq70SZv_bJmsEsg8u9Mlws9Lk7--hgIYDYJufZ6N2VsqiVKltvMXpC6TjhW9YDzXAFlQ9cO8Nntci9XEpSgNuK73cCL2ylYBaA3KFlWrOjSYkim4YrlEZrSu68rI2MF9dMiG7yx0LpaScSUH6HIcrnfQrlf5trkeCqFQm2XddMVihJHpFP-QD85383dkY23a6EgvVNtnWhrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqsRE4LmeP2LAPYltGvBLkW8VECaIioVb6QhrmCrEjY6jVgfNnZ44FRa4m3R3afuKQ6-hXi4wiDI9J-r3jPtzES-x0zY60PdmU-SvdEJ9P3svigi92eKrM8yoFRHulA7zCJFAcw0A0QLmY91g5r25naPVU05xOkCYeR-vstIQ1fbM4AF0vs_gyosPcZiYCbdCPxXVEFdopZ5wpkmsdbwHN-rut-wLNlFsoraOGU2Aq19HsojHLnFHLyb5gWGyNzb0TJXXoF3jWtc3FIXKoG7HvKBoxA_vfFMO56r7akIxbtMKGSLCpFFPATpsxPv3-VFBzeDsSs1zKOjeTxwRJKw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gukIlylnOwbwbI56Ek4JFXWfYlcSVUcdnttjiqQU3Bst0sgyniRJUR3CROIKaTe_S1P-IJoIjJQlQOYnSfwKVVnlxJr_E5v0q7guobv6do6I02GUfcs7Clp9uuyRHY8K4t_2cHU5sO93xVNLMqIs5-CLAOV_kIaNiMMmjCfpd4zQEoFOpaDRd3JXh4H_57aXCQ7XGcYZzIM4dIPIicgKfxPRDpzj6xqkN5lUbgxsnhblp2dT8aZTJgAtW9-fOsjuNjzztyzlHKsWUsNh4hIq9WOi-mV8lbtQJ_uKtEkQWl_sLoS9WRFgIZ0a_2xpZrI5gRUMZqpBEhHNLh10ZQ-WEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlCQZMRIeuAW320QFw-vQautgMOd7tUWhWG4CUn0Yztow9Ob5z8oX-yaDPSCI_EPvNKxr26OtMOh2EVexc9_KykkRtYAv4iXhXSBuN7jujoJblIroAc6qCDDdM8jjMUZfDrEStIqV5y-B7pkZ0GCvx4YuvqN6g_GJGK8cE41lMmVQFFCaCVOUv4NM-sfwTPp6531inlVU_QlqaU1qPwI20oncIz1qKt7mgWU622roFvaa_TzZXPip7IWuX_YRqknx-47NjqUzByc1IwpE8oeAY47cn1tbifQp1i9gzycHAChM4bRdAI_6BdyEloF6TQQdc8vDARCdC6jcakBArIiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvRXlQi_PJMFETN0mKOnrPwQiPPvasFZT-saQjXZA9Lf1Beyedjnvjf4kNWqgmbtt9G_hHPYNRdmvS9a_Aed6FeBno2vX_hlwxhrGkFLiGv8V2a-VlItX0sMmRvieUcxKXS7Fd3g4q5uteZS5dHbss01vT_VmsDt8IHoLijJ44Pd_Pr4UQJlQhJ_ifXhPb_eFjr_EyO5iDaQfInYLrgx-uM9yruX97rSifYTwrxxu-NiZDgvEGPIy-6jhjw6_C_BnDovtwasr8kG9aRbz1Gqr5rdzQ9F9q91wdBO704TTGNRJIFpyBkJln3wbINyYw-pozOweI4QCMIGVRPeDeKmFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWLvubOUR0NK6siLAvUdyodTjEwuHjulaBiqpXQL9h3W0xiwulsnrUc-TIZihLNaext_8yFfkTwo6B8lL14hWDIOMlgLYeqRxV_v0i3sO3gY0M70o6m6Yc2hmdLpQO-gFFvsfl4-eXM_IvojQ2T8JcNUwgcFrh9mt3KzoqJf7Bn74rk2AsFFIlK_hRYK9CO1IAQTV_iiL87aUGQAPTdK7N1DhBRbx1w2PWj9XyV5PTwBucgr8MXs9RffG8jW-dQmf74LO_HYkw9gpxF5WhQ3aqQPoBFU5aZkKRT9lGYOiUX6t5SXxOHqNKfEHngfZRYT162AqLnyT-lZ0VkicNtpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltu3sPVTsW4T0tvMh5bQNNNToOrZKAQHHh4rKI3FOWeG1qdbOlNzelQRpaZlIzov2so5gRxC_OMcUHbnMNhUMoZDmpCJFYr95FVd0CZsH_5ftw02vBcFKz6S1E8nnE6kySoiIJkvN8n9UfVQ-LKAfDfqVe-ojK6C9daNuL-NvFPTRMWYwrr0JzjnSMm1tZ5W57pQU70otog_kXlOPZ0kNpAEaerPHMuir7EEsdRoW7I0Bj2eL1kWYHtzGcyCj0Kus1Pgr_mN-jJk2rJV14ls7XzuTSeWnBF_-AU0hvypSsNKZx3Oc8v8_SCH9OzC5EFkf-9Mc6CwIXrvctcKJfz4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vsq0Uci2IFh0Z-iL-pALBOqyJEu8Wd3GiM2dJ5xDKlqhZUbsikGevY_texjkPS9GZXupJkRxTTfYEKVcjJh_C6yywv_9vIcoMtfUdkORllAhqIO8eU19IrTEsFYgAzvh7MhJfeQb2OCukYE07_PlUPBggWXtevy8gW34ETTjlLw_LUAquxgXaWavjgW6dy-D90LVMUIxYwOe-IcKo3gtaSlN-wf_O8t9_excRXefG6cUzUfndJE78vOIEgzDS8bQSS5chxhjXRdsw46muG7Nu3GMSeFE_tbnEoQ0uh5S50QVoa2L-2Jud-cay9x189ObZ4AN-Mx7X27Veni7vLQdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBQRmDHkWWFpVklNvF04DVXTL-Ks0Rfb_aDpXWDLNGIgCv1WMly-6tB3HCoEPzcmbcFU76RCcij4WJ_sHlc5oublBXqDL6OKQpaFOxHZf40juIrLl67-D2jQTAN919dlyXOfHMyWMAFXRxaDAdWv9Dv_W-O4J7RDg3ux11anFVwgGmE1kwJjNm1Qrj3ND3EFcyadck2_YpRfJ8oLcvwntB_zAyez9vTXQg1DN7FLTDT8OWO5aGXN--kHf7KCKQ1_l788bOFkXaeXPA_URdzIBAi5UKlQlrlmtzQJqExUldXpqlB7x1m1kXDI4UzSAaIT8ZolzSa1-ygo5SZFhjL6fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq9V2WBBgFus5Cbz3lnXzpxuq4uyt4bVrU24Q491ibRCcNCb2nSAfGvbTlsWeFLvd02zJGPEj7_xMZuaRxcA_ObVeo-Fo3woq1PeazYnJjQjW7vzwIVlAVP6_vdUPINLdHNiP6rPlGTL7LzEP2psYoQfN_r-TcHK09q9L0Ghj04dqPtI8O-RcloqmbCwK-Yf_MReA9NeZPCtZ_UTGGCSMpwfbiJsE2j7udJr5LeAgYYnNG2Rj9gKwK_P4RiTQcKPxxaqkcAHYvuCDo_ut5BJKUFaRZYU9c8TxJDr2mTNmfd-JvQt1WZYTIGyraMIk2vEFWkDYXjvxUNaUZSxx06T7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R838kby4SJ5qv9SwMSflEzU0Kb1-9Z7L6E9AffkXfKiVEEcOrx3TCuIqyH-ze6GZG9qrOUvDaIf2gTms3eYHEuYN0HY0LqofoUdEWtyUj3oo0VeFawM0G3BI-AVdWHJCWeOYo7xCurh1_bONeHQVSISayDS8QwUZqQdsHbD_glRGKL-IdcGLlXGVvoWSYyhnA4MCXhqbtOppfqf68Qivp4kiPtshYaxO3hqX6H3FS-ui1cIS_gARgv3P7cTCOqoGjFxBSzXm7Yoq0bhk7r8NrxUdRvDWAEC06w56g9hkNh-NmCXpSECU093dhPnadVj63WuqdYB0mV8-Fezk6RdgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMlfUUHBEZG5ZCr6kueBM6lYXM3WrbJhSNe0GaemZ_6mEdFKULbEmk3OO9aqLVelwb_mRI5kd2VR2Z9dsmTiB0c4NLn_lLjF1EySYSgGh7qLtCDZqYoEXN7RfVRQBih56-KYOia8lzl9m6hePZShbn817g_sh5cBn1hTA_tVO5TPocOGgaasdqnnpBdf5-qg8F5reF9jm__tP5WHGT-svdzELlIaMaCzkiGc0HmewBVm9F7-rH5egvhqO9YAKDRLvf_Z5Oa3NCVW-DnL3PsuHNkwYckc5KE7Nlo36lOvxp2wG_4jRKSKufVJSW4sVnpo-GzdFd6o73JzzX0Trf26hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHvTd5gepc-SqE_8vHiXx-HnzBzyVsKY_imlA6dI8IQUuUJxrb1USz_dxav4I6swbYHmEwXECH6T3jj6Gz1YyjWDxFHbefqgkQ85Bd3GMCYvqanwI8kUB1UgRCdppL4ljCxNj9915bdn3SOwH_aaXtBtVFHGjMTRHuAjKNo-uHjCJZ3HtMw5wTD-oJ-scv_0P7lzcvyheU4Jbx3qj-KLutPT9YdJOJalrMmELLDUcl7eWppPXaQfml3zjQmAGi9viWJi9puTYtmyWTnmNYqBBqlGMbmAVDVKl4YVUQ0uYMMeQW5SVNHXpoD0jVkX95zEYz2zbb_xiEhl40LjcDDv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtOoMqJO0Z_vJiXeX3PkseGhocesYjKr1BNiFMPSxNYK0jShciRoUct3SuRRXNEwkQAUQHiWcTusjjbzx8Alen-TUQQvwPj5agwerz3s1-7mbqcFE1N28rGeIbRZDuVQsUmKOayhi6iQEUiDgQvViOB0r9xmIRq-JZiabU6-TbZKHETKuBx-PW14MsmVgDiw4fqr79xEhOc27R-HxQYX2oW6mfRnSHIBVQSCHu8dzYiPxvLK0-xVlP7y2gX-J_MURZtxZXVKV5gxBJcoPvkkqvSGPvhRJTqgJ_wnvm6FyzmbuG1-1GQn4l5bqGgBYstcg2Slz73vsfnQQPbD9zeG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_Bod3zdT05F6vRiS49CijALmzJCsVk6JKWmI-8GpezRT7C6fnXVM3uI0ib97o4fWT07dTLg-v7pKJFQOWM50dIP3NaZQKea-gHPE54jQFkd73XWeyom2f8k3HEotLOM4M0P_xvG2ZFNgd3UqmpQJPqYFfdfQ7nSl_7HvrzZw9rgQvMj56Gm9mrawT4CTcuk0dyxqUxP11Hxbg-OPo9EV0zs8aTv3gWlUb3n3LP47j2cC0JGxPsEqnr1vvX9Gkima36WOcmutvWBfrCCPJBZzpBk4c9jYE9fQhd1rAP3fVV_Eo6diU-PxKAKR4ll8_UqG3PHRLHp9xUGuf2r7AaHnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIlpuCpV0kWXNrvh2JkzkThqskaLAbvEAA9AahhGgF71uxTks3iARoi10EtqUqkiyjMmXC9UwulIHJaWCRDC_EcLcrV-Vr-YW1OGpNg1UNpCuLd8WK9eHBUtCUMd7gJEK8tBr-tt3nI6pCe1ghvw2wO0eblkpGBV9BXHUs0zgl7hJR-crDzUbcg4pV5xGyJgEaPk7lk_I_bc1HZaERx33lsZBdPCexEau3me2bQ8ohmiXl-fVao9IZ33kEkAvpvRu1rEWZ01GfGv1bBsK6J0Sf07FlU8-WNm4jJcOp154pLYmQlGOToxX88aRgIKDI3x1J5nnoZ4_kd3zMEqDLJzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el4TWemIp7xOjeqKGs3MSdC6oVbdnE2iDvBolbaqJTVOTflCbqGwb9Ljmdvvz50ey7kn9H_LnzGDI1ww_SQPaF5ETa6ewpZhvXxWHPQTbB4B-gps2tbCKRYDw3_BPZ-YxhyuMuJcCor-zQNgfPcqPoeRqdM2IQUlHXoFGqAAGKe8i5vT3a7MyrhsbHOiGAqoYwfXcGMVCO50ucweNCtLG6qwyxREvhEeSVJKeM8DGXwWNbnAdWwqikIL8kf2EOz4-Iz_jT9vIq1wmIKhK-YypjyxeqYbhSge20W1c0dPurhYdwqg_CVYsCMZBn9f8jB2T6VOuYz4ft7_TBrbmvWKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
