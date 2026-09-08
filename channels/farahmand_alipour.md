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
<img src="https://cdn4.telesco.pe/file/l6F0LkW8h-ISi53YvtlhFoVaWLVhvytJNp6PQT_uEkm3nrq4SyqQYKjNxIRc1yLZIikLS1_LtVAjBzR7sZdXv5qxc4EL5zau5s2DnKRh3WrbRQRToJ4n3HrzxUWQecCRyYBXVR0M4y0FvJN-0sPodf5fLzLVlF7ls6GYsUwh5mko1IyvhYP1eIT1FABAjCKGWSi2crQGqSlKy_hnL1qZcZXrvUWgVd8ZVvDU787F3CyvdUI66-NW13CBcdrc1ioz-L5fvGPrBrTnDzIJLAm4Ia5s0CVI1LojxV4fc8yFtOpOx9ZjPJs9AaoatTiDDUdU6TW7o_riD8gswuXffGDl5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 13:27:39</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6x5uhk61jmBjpHnFvJaGTmx5ZYJRNf8lu2Z1I-JdraKkF0ebA1wx4Dng5WTzl4-PFo1ecWsxepGFa0-xAVusjbaLQ0xrBkRjD49kfl8d4VhJC6VM6SNAvzqLCAb-HzTv0EPDHpLV_lykigIu9adANoZqfoLwH-xCiLLPBn2d4kAfI4444nJQlTl_WZGm0JoDvZCZaeq94rilOM91izsiqWizBQmL3boHrOkRaQI3-BbI5zLarF3bXkpR7JPGYjEW72zj51MMxjuUIPPsVjb7h9_Qn9sMw-fmpsZGtTLo3OF6FSCDvlCrCKLG_objQKiok7LbTsfNDDEvQN2GsKiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpLoRmWsNBY-DCxpFKzRJKWrGgDaFx_Wl8wApnELlzjtHho24X_zUkYcYmDJrHlol0WG_4mv9qPRQ2aPZYj48mPK0_8rDECL9azB6EJRYNpBRMr_0rQrYoaxGCi32SDgRzGaDRHzjybM39qxulTQx8vkAm6gknv5RqcYJBQLj6Yyl6S8TIdLAK9k6_BbyEf4YBlhT5QtB7KJeZpGYXKUEragMhH7ch-mwye5RDJFwsBqUUDc0UROnLkTBTyi7bNu1-sum0BJgcGh14lVBafjOLPQvas-4Zw5Ptan7RuyOE1psUGx-Vpx5N82KLT45Yi1K_GAAcTvjYoPWO6ymaF6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4xkZvDe_TRochKG9OElTNQ5FAOZmPVCju0xMPY-N94c-UFq4HoE8LgngXeU_YDXVu01NzSHQEwHHaU-AoLT74htlRTVs2SHjeMHcBdS9DePygfhIAvKB0CBuZm5JJbqhxNd5ras9zBrC96cKDy5Aqs5wrXV2x0n9MEgY2vjcbQibhAoyxDJp0xkR_4JV4GRcw6suy1uCwS3ASKZLNrPNHAy-Vb5WbaBCml85UQbxY2e5tABQbEKg_nMSqPiBRFFss4YAZ56EK4CXp3Rx4EoPg137Cg9VNndQh-K_yWdBIclcfKZuUFmZHL_dLj3m3zuRumHI5lbjeZGBCpEfPaBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isIGJ5D_tk1ZcSbWxM6aQrpEHu_gWrTruUYjfCeRwzykKI9pp4evymR5ujZE7kAvrR1_4jFVDl5B7WACGbtcVGulhFSRLwSAjTEKpwaHp3r1_O-9csNYLcsGcYq3rxQbawho_8okLr3E0kY6vLARhqng_3gwa1SrHGp5FDpI8wyS4_1KizDBEFEKc3ZnAbLf2a7p2v5WyqU7E_YzK4AT5hz9OReneEwWVqR-tpYePzR0O-fSx4LMZlN5-BCGC7ZzOanALPxwnVdLqTaZVc1aiOzcEUnAqDiYLgz64e9N6emTwRVKr9nDUM2pBuHUKJiMO48UY2io1VCKhGtwBztx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=QrUNEJPvhos6oAuaSQzUG1VgvQq5JF-2EnffhSFHwE_Fo28BF2X7HDfjmUYv1fLcsUzdmnsCyYexFmFVCl2ySN5VHoggD4jKBRNXcSBO58jtgf3W0m5dcetJX4JFGELtYwAYVc9u44gFEZDlX2GM_Nj2CbiOnFGiJHauTEodLczxVFQITGIuiHPlNvykkcW2C8RrKEoxMQMAfPwbws06yT15tVsPYqKRzJvpXRwq42FXy3ROtyDk02PmznCdJAXRUjRewLUAQw5VRV9xmRUOjswcAk1C86UUqNbIHaAWd6KAlz1TSQ-52qz3SwpBJdqljauS3n0LBPuBmSpcsANS7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=QrUNEJPvhos6oAuaSQzUG1VgvQq5JF-2EnffhSFHwE_Fo28BF2X7HDfjmUYv1fLcsUzdmnsCyYexFmFVCl2ySN5VHoggD4jKBRNXcSBO58jtgf3W0m5dcetJX4JFGELtYwAYVc9u44gFEZDlX2GM_Nj2CbiOnFGiJHauTEodLczxVFQITGIuiHPlNvykkcW2C8RrKEoxMQMAfPwbws06yT15tVsPYqKRzJvpXRwq42FXy3ROtyDk02PmznCdJAXRUjRewLUAQw5VRV9xmRUOjswcAk1C86UUqNbIHaAWd6KAlz1TSQ-52qz3SwpBJdqljauS3n0LBPuBmSpcsANS7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=cB0h74dEGVeZSUOc-dwztifZ8OQkUiY2-aiA0EpRHRCvsQB-sL8GAgMnidPM-rkkeC6QScw_PV8VrvSCskgfukBy8zoXb0CEaxcQf3ZigA7garTqJ6sJpHnPpF7OL44m7mkPlrL5Y4lri-xcopWCqK9LZmATbVeLCiWEzFH0ao3d6_K9pUxCZCrGRCiuGOQexvix64sCLNdoDrdUpyXRhACqTDVrYGFrPak-s9GUW7p7Y8aVDCDssDon__OwgxNUY7GBqqDESBX_iKub1CCWIFt1FWqzMw4Jf1RT5sA8J7lvbcCa4pY-8_5OZ51RlZ5U-lanZBz_tmY8UAAODP_EDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=cB0h74dEGVeZSUOc-dwztifZ8OQkUiY2-aiA0EpRHRCvsQB-sL8GAgMnidPM-rkkeC6QScw_PV8VrvSCskgfukBy8zoXb0CEaxcQf3ZigA7garTqJ6sJpHnPpF7OL44m7mkPlrL5Y4lri-xcopWCqK9LZmATbVeLCiWEzFH0ao3d6_K9pUxCZCrGRCiuGOQexvix64sCLNdoDrdUpyXRhACqTDVrYGFrPak-s9GUW7p7Y8aVDCDssDon__OwgxNUY7GBqqDESBX_iKub1CCWIFt1FWqzMw4Jf1RT5sA8J7lvbcCa4pY-8_5OZ51RlZ5U-lanZBz_tmY8UAAODP_EDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTr49EW6sFqeNr5M1MBJETfGCEF97x30ihYm5bkAsg4d54Q_kUaUJTfigK3FHVzpKUN2FFwqIW7Thr1xzQwcPbu5DIqba1qjudvh1ogWgURdrrdKugV5cTETHYFruIfaRFSAiHM93iTAM0f7_moLP5Iv6mRsED69191nmzxbGqjtzKDVNcm4YRTI5GkL8xJ-84UO3--Qvt5qJO87mhcWAsDbpxTKcuebGzhYloB0QfF6q2WHJTpBfg5UXRjv6vc7l36gskDOdrPkSJQQSshqmTyYn1993mXICNjFZNo_Npf6Z-WAySgW1zG8UVzIvmKFDebPF1r2OKhJ-Uay6ub8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSYE8P8rhqHM4fcC-rzH7I4kBggTS5eBXgnPaeLRwRuBvV4Z56YJuOLuNvSs2xURhTzwPTZ_7FtsIJqPbM-LkwR_8nEdtRVmpJ7jr3tFBXG9AKEsh6NP4PeyO65VcVLKA2qf5EhYqRoRuyU6ZxfBZ8zLiA7kcDthar53LDzJxhj9YNy0BoE1LdiNNAX3ybjRyEsNCigB2dRzNz-GHpqMmTTIkIIUOX_8TY5dwtYeWuKN1i5sCM3_7jZe9IOo97Lih_JbCaR-6ICdgFZbx-rg6SvqGiXZvlFf3FSvVLg6Kj_4vTukxPVop8bpefDzkvT9Cj4IldxwPahXloyx0XsE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4JDB1QLz6ZHLgTjocIdeRZRf_aPFQHq_8kgZLnSY81ZJ94jKIFl9wVrOME-PbeJufW4NLy-ZRTgRz8HGvzn4gc9Q5ALEyGpknJ4RkEW1fS-Hpc-eOONb2UVktNBK-mg_lW81WHChpo9kRSZZ4b8q2EWxdFg-MNWOHz1nA9_bofujC1wB4EoFq6zRCJBvR9mhJOXz5w-nGK-yaVPDgF9xaFbUkOH1Uq5T2MqgYJBSgIR1GIhMcJZWb0a6zJVIh5U77TfHITvXomtEnz8fNUwV9gsSUlQPJjY2TS-3SSzVDAgBULycLU82cLRNYdkMN6Wx-6pbRhLMzwzVAg7_zWduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDZEKflR6zBDB1gDbz05aoJbIxiFeXILzj2ZgGNno52O51jZu_FtzUBdnSgJxUbLBEgxRudP8VjpnU_Ymnx0QZygP1ivoMBtPLf5zvySQlBkZF2sknIoZfvjI7qz3C0DNWvK6YfDejEd9t6S7Mp1ISxOpysrwQBriDURNntQ5ig8kHc-IlMa2JosMrh6K3DmlJxKLmmG5zrbyYRD78_EijHyUkmqaaMOq460Jhab7ooy02-8e4SOi6ux9umjViggxqr5pC11b0oRF9GlW5ea7hFX5JbMEwYd0CYGZvA3GmsQ8DGzcg2Rvz_rFCURGMgPCFWKCFatOUaJLPUDyinFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2IelGs8eswBt2ygt6gE0KLGrD8r0NFjuurb9yXd8yuR2IZvVohbRkfTAA779BFCeTS7Ech7XSWvnyfVqmSGk0ZnSQ4N26Rv3lKdJhHVvXP4VfIWp1SrZD8fXF1TqmqW_WAsGKOBBgu7HLwFyJryCMNeBEPjBVFMTLOgqI9Yvbv802pzmhD9SOckbvE1JpAsh8oSR9teKJeKkDZFMpkhygLw9rHg_OBDKl0FZZP65j4WgttpGjIvAlhmmkNW1nEviokMx0ao_r6L86avwsOzXEpEU2lZaKlX8sc4TEq0LzCEfzGlv9RNp_32fOjVLfkA_sCVbqQXLqX9tYGyRvoftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l92mavynkKSUv2PKCyhFup7umHIBvqBtSWMOoYMIrSHRy9DlhTUITE06MKnc7ioBpOT2FjcDJ2KGSiC9Hq_-uRBuIGQhAiMQ-ZeijLHR2LSuTa5GyDOWds-U5zAh7VfhWJcvEj4CRJgbu5I2wJe11sTHclUXE5yl5SzU1PBxX4hIz1trSb2bE_fkI5xnQ4j-NJv1ol8EI26A-wOdgv3s0-ynAIdX1OkP2olQOoRIEj2cHOw1sgdnz1-oQ6UTj9E-2mf_xyKQaL1G3QpCUSVVaTpOttb0Z_xk5Pv4y_pbAnaN0gu7UzhruwIMHajNS6asQn3wBTsd6RCELTXOWqYf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN8xH0u-x6TFyxLxjnqEyMalN3EM-m6dDOrZ-SayksgJs7UkSXO4FsdtWs_SDdLhN9FZ0Qe9K-_HIxmL9dhKqRcVPRdf8kGVNw3oiDMu8c43htSHz6AeaHmvbVYl6in6MMEYvpc8NTeNcPKVuZk3ByTiR_auBPADSNngB2OV2zZc8xFA_LanIp998VPnlUBosgRjeMtTckZ31Vu_m4GD2Hbvmn0C1N7wh_Tv2tjoqDSyKmtEaGlT8TEWru3iDeUGZmOhAIv3q4pEbEOXnfRk31e2G8uhKL4cEp61T08_lwj0nBN51TfpM9nCHjymSiepqgaBPdxCbjXbySDa-KSA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cz09SQdRRC7DzvclWkxyr7mA9BNrr8a5xg60HSYWYZr6KCGzL7sZy3PTIGSGNk6Cr1FMwlhulYrzUjpS1X795X5C6ce01uF_rNfj6SreqHhXGXEYm2ttBg3MDd1o2zQ_QBoOuEsJMl58kBaTss1VNY3Cu7j2wiMM-wQhiZ_2wUvwyU6xm-wDbPeFOm5nGGEP-FkQVVs0hl2RiJpKJ5G_2Klw9NomBr4CHsmuXGTOQAbNGuWXwZKQFccYRpzXVkMrzMH2vDG4_Bjb_8e9fzPKArPOFXeVRc0FGdI6dM-nEs3IZ5p_kmlVgO8V4UxXNVqypcUdhf-hQbHsOPTz7uFeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXSicCYmNv95pEgvvIdngWWFjFV6AtO0EiJPE6bJRfDmHBofK-b6tnCm1lh6bcsXdu2symZUYszI1YiUqCGWXCxAoDp06zubYIsodr55F0A76ndtzNvQTlwnoTcM0kWysc7sAQg3N-ix28gHsL-PsQl8NSySKHhAf9GQZny6NeuM_-QYk0xWqTb_6-jlPFQp5Pa9kp60wYMdYM5-7pqqp1_27ZcG9sRvnql31cPYfABXzkOWzXWvM5hqbYmzcJFSBR-0ttBSIs0uL6kAJXGsoBUTL8gWNN79HyXyRlhBPihMrkvPjKTi3A21aZoOGDQbqx3dec6VHyv8890Jgsuieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmhPis9HxihXeBH3os_xK42yxRTaFqYtQBm7VkPLIe-iylmDA891x4rNFgqJZR5_Ov2gJyoXCUb-v9u-7xnP51kVY-gBU_D0jXXW6_eV13ef0s9ZF6f4W7nhW2DQ_EZd_k3aAxepukMUUYFbNgZ3QZKuP2Y5lxLA3hzfdw9znxGm7_7_FeCm37Efv447uqzDM0tg7lkJkoRIe9j9T7Md2I4SH29uDzqxjpTL_A5zjLSvChJ-GekkHM3nlXLbfscZfnIP77kI2Zk4oX43SnNv5Z4JGbqHw33aFDTt8f85KVgXAAIeGiNM9POevPcIxqnZW-2pf6UZ3qJsERVDjELjYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=BFswqCRwNwKahOrDqqlm9-6S3i7ZleOk3mNB1ED-pS-o8214zPWhOHlYBdNIIuUFgBrRHtpNCv2OKt6xshj_4Yy2bb6WvNxfAQenJ4xrprrfueIS5rCrXaz5ZWEe0ICd5fyKWxaGPRCQq1sfiz5spCiAKXIlCnPKSeSj__OMpFlELRYKygqq92x1MGQArX4ZzV-XneUQ9storJ4jwR3JubbNBENFXVYEpFMiSBE_U5oE54lnA9EFpUuLpTrD62fYssw4fB7Ue3kZcgQ21F4pdhU4Tbf-rQkiUdBY6xxGF24f8pi9KUPfhgoRyxjf747cFfxx5Zy3o5jKQooDxgcYFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=BFswqCRwNwKahOrDqqlm9-6S3i7ZleOk3mNB1ED-pS-o8214zPWhOHlYBdNIIuUFgBrRHtpNCv2OKt6xshj_4Yy2bb6WvNxfAQenJ4xrprrfueIS5rCrXaz5ZWEe0ICd5fyKWxaGPRCQq1sfiz5spCiAKXIlCnPKSeSj__OMpFlELRYKygqq92x1MGQArX4ZzV-XneUQ9storJ4jwR3JubbNBENFXVYEpFMiSBE_U5oE54lnA9EFpUuLpTrD62fYssw4fB7Ue3kZcgQ21F4pdhU4Tbf-rQkiUdBY6xxGF24f8pi9KUPfhgoRyxjf747cFfxx5Zy3o5jKQooDxgcYFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb0uQYLy_Qtd3hpaWuYZgff92l3nqA09A4Noj2N5E5pnV_5LV2sgzLZMYc6SpSWRsGNjKd4oxPu0F6LCghE-W8J5Q0_pLhfJh_7Dl2NXbVS6P9oGU5WcMzkme0nblC6dhDcsquk9fLLfr_-Db4qIrTItqEwy25m0qQq3-mAwXhr7L-nxvPLy4f__GbrRL5aDaIDnI-1mR3lSPkJMrqx7wNfrFb6CUYaTmwTMm3rkx1-_UOP5aFX23qHx2i4uMgD9lotGOHWp3aHYdctqzScdl--VMbs--0pA054CG3_Fx2wDlJZSNfhTZsCX3ccFr8izK6op_hCpofXolu_WoskLpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmcmBveWWmo7uzPJgVt2b5viTmVEZeLXMVZ-xkd6gIpXwiWPyxkHLIr-rsbTZJ5KKi5BaBGmxiG4viYeD4MgE51_5Tz1hiOisdMp0dQVsfoew593f7FJMJlfwaIBAFXXJca5J8PS4Hiz4PH9OhDkPct9-ndcSxSkAOEkRSegQetMBKTdLWg4mIMJRR0hE5j_HmwG5f_Q23VUNLdOQ5eCns-CrNerBobuczonwpTwFe7SMZF0TtuVmixc0Ji14XgsHYqbncMENWuqaEnu1wK6ezN_RDUtpc3CzLxtR6IAldIsHrRzdqXKgVje7M_gXgOqpOVwodyzMyEOgdVd7uZ5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=vaG_EKIoC6Ks5xws43iR3UKwnra5b0B6p3Y4bEGLDDmJ_zy0DMFkMNTHA2VMU_BKEoINwXHdFF_uM-zQNEDWNc8NOeFQGi2tlFUV-__17Wf8_o1zRsWPJ1aimlrLiTjLVwUpgrOTPDril-cgebaESO_IGhInDms2-rMNhrIvADEOqvbqC5WCLVykZnGDgSyRqP9gsUDsWE6sjHvWijJMJqCtU-48Yocz4Zn_PspZLRAVyiPNjE1tJr-Ly_8QOxi8E3TizFRdSfMW3nxHd7TAzWEOfVfBJ5HJZviG3m7AJ6KGx2ZqJTfMPHrRsyNXOYTxdzm80jonT8M0V6tUWtqMcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=vaG_EKIoC6Ks5xws43iR3UKwnra5b0B6p3Y4bEGLDDmJ_zy0DMFkMNTHA2VMU_BKEoINwXHdFF_uM-zQNEDWNc8NOeFQGi2tlFUV-__17Wf8_o1zRsWPJ1aimlrLiTjLVwUpgrOTPDril-cgebaESO_IGhInDms2-rMNhrIvADEOqvbqC5WCLVykZnGDgSyRqP9gsUDsWE6sjHvWijJMJqCtU-48Yocz4Zn_PspZLRAVyiPNjE1tJr-Ly_8QOxi8E3TizFRdSfMW3nxHd7TAzWEOfVfBJ5HJZviG3m7AJ6KGx2ZqJTfMPHrRsyNXOYTxdzm80jonT8M0V6tUWtqMcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=OZWwtnrxayKqernWpWRl16ksFNTZCfR5-UlJCdUAnta_o5hSjLJNecnoRVaYNL2CK-_WxRky7LNKiQHBwWce1DxU7IaHYMCiM9od70471WURyAkAMVREr__KVv635ZAU99pSB9m-9Ml9qrZetBhpCs4GDBBturoMJgrowWTAMFJnFBKOo3JaIOQTGdL0SP0WBUqUyLA56D8ux7aaf0R_uddct0UTELNWG2aQ0ur2Wggy39MQDWGm9cmjjcmNctk10mTDVgU2tJUNPhXdq89myk_fjo9h1UYqxFQBDgA5SLVFUkVfCWkUGv9MoMrf1LEMdB80AF0QzkNIA3ivo2B8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=OZWwtnrxayKqernWpWRl16ksFNTZCfR5-UlJCdUAnta_o5hSjLJNecnoRVaYNL2CK-_WxRky7LNKiQHBwWce1DxU7IaHYMCiM9od70471WURyAkAMVREr__KVv635ZAU99pSB9m-9Ml9qrZetBhpCs4GDBBturoMJgrowWTAMFJnFBKOo3JaIOQTGdL0SP0WBUqUyLA56D8ux7aaf0R_uddct0UTELNWG2aQ0ur2Wggy39MQDWGm9cmjjcmNctk10mTDVgU2tJUNPhXdq89myk_fjo9h1UYqxFQBDgA5SLVFUkVfCWkUGv9MoMrf1LEMdB80AF0QzkNIA3ivo2B8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcHVq-XoLUVTJ0Imz0SwXMzVpKAyy681Y9jOXzqJvBG--ftvOohzk7crQswvvvIUHDTKXHQWDuPRVph8HE5HhEwIhEyReBVApFej9vlqSUHWq8oJOPHEs0b2_PiLpN8_k_UgQ-8zWgl0uQnEC9UJf6IU31N-G9GRXh-C3MzIJr_QchSsvLfjp0hsESm7NizO1Ehs3OAfWsLzmdIgpL3DzDKLFd8QA5C_EofIs69GodP01Ts55qRsB1yRwKO6ScIyxBkN8CmjPdwYX806X5qZMLP3ZTWXtrvglvWGxEMLddEvw72jRi4ZEquxZ9Yvu7Or6zk1B6OCM6f3pIHhleQjfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSgKUitkaFXIJ0MhFNSShV9XSWwNotsj7BVZomw5RdmbH51y_lBj6UD0jstMI0Xfqho6yEjQkPinIbDPe4URt0zkMY0X9M5P6uk8GEtXEJToQxCRS1SgWzxE3uRLHlqHiehd5hbMduGej12hl_A41gKUa2uRbcE6DJqLPFHWhuIZ5Ej7GO44xcH3hp8Y5UJOAK2LU5u06DFKEQmYHoSbyeUMNpO5vuBWzA8GVux0VGMqX2fWnIZwOxEJRhxCaJV2EjGXaPXS67reB8oD-iIawfvlaozeM-MEXtpo-c3gFUGt7fplkzm4n2K7V6gLh9REuiUUIkh5-1BWh84a8UZlAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ivhF31L4V04vQxII2cxamySoyzVbixm7PJZ4CEwkKlj-Imgv6Kk_MUIyEqsF0-uofN9svEM_Q1Mq6UBDhvV5nzGo3WoCCzXlXxuby6wds48K5dQEwpEllR99xtajoHdeUHlSWeX7w5E-ifYR0Paqcpqpr-88GSbcicpPTiwft2v2ekwU5IYRZz6t9PG8XdHWNKjtjm4_k0DORaOvIkT_OF65MQGGm3KuaGYt9T6HhJbddHKm_HCeWayCQET84VKebTPSmClkcnR49AdVu0sj-DY8_KAljw2EbVlhrGiRLjKqgRJfnN2uw5Wx8LX2a3ci9AHSdzI2acqnO8OJs-TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USHjPUV10KTN8PpjHWFo7FtyoD_MfV8QCoufRIXBX4Jt6yTN1u3lHz5LDBg-z5rP9n3tqAmGRmPfouHRYMwe-X4-l_uuRZdYrH45PMYfptE1f4GdCjPfc07AbKloSZf5GSwqEvntfYrn_FksfaHfjy6NaNGCRIBm5KOzJNeK8zWhIcR2wpeUT1r_wai---VforArhwDIRG0WEC7bMlOUJDrg3zyxfiINR-Zo5NLZocyeaU9nkT0rsTKhieK-8wiYq0Uiihh50LyITEtEQqth9LqQqMt9-uEM5MujWCdGSA7dT-_Rdbwv2S4mjWbzlIkEFtpqDA7tvo9IsaLzFzJphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw4XPdDcG4ylBtmBlV9y6GohPz8luXQher5Za14cHbsU8TeuXTe-cyKFNaA1zEnw2U3Ppk3x9dVGWWu18Y-OC2M4LSy7LVCdtrhr9MNN_dHWFSpPago6TtBnRw8XCXkjAo_BANkAZQWRkWDU_aPr9NKMKq2NkwndfbSBfYPWJAExWDVCCUMnemNCb7h2csFA7EUBonl18oEMtEy0i37nY6LcUuIA0zt1kLdinas4pQgIpl35gSAvsTtJaiHX9BwC8-bs9_AnRAfgFtMFGuT-rFBK--Fb8AWdjK0aW984D1iyDQIBu_ukJQXMwPuTz2M5WKSfI5ntzHBd6COMmumQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMFkG8ioPDCH7aCHnxxdoCI7jOzpLprR8lMgJPAJ0ypaotlMA8cJEYgFM3hnDKuMgy77lHNNwcvDO3OYu2Z0tqBm5XcJHioFhKuNUs4rxz0lZAgGfDFkuv2Tn8OAMFjC76a-es3OFav4VLLvf7KipfmsftRXApodZmH2r_Z62_Z6DyCVuArWtYfuIJFaiIgLe3eDLE1uj_KkFvv55-Le9CxO06Qa7lYMtRJIjkqEO0P2-0QyCZHap_qFN3iKuc5SfdsKxx1ReG-uorhQH4mh4QPCaY7boG1INr-FI9rCb0TzJUehb1kLnHLf0-D8Cs-Cyp-xLV3CfSTZrp6Pn482vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGQhhmH58V553ygFkSuyi5ivpRXuyTXbuwQdk47FqBoRdPAveLgrjh3u6oUVfDg-yjGnqJEc7dcLIMlqbIPn227SnwN3ksovG5fkb1TiKg65FKmsGY1puMc4p4W5ZqEMagBJ0NkcR6NgUHyqTrUYqVrSE5ROx6DJPDsblU5pi6J00DHLk5ZQnAjjyvd3m8mmXCaKhg7vvj8AdT0VNx_OgH4TUUoZeKqcWuCV8Iuvgaqc8baCf6vvszzq4VEnkDDx3n28l0juxgUQBe4q2_I7CJHtwbkSQiFveQqt54NMdqgcXXiw97BDxV7KGz-lO0G4T4nRFdIJDyYYlu-HiZibqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5QI4mpzYbBC8fnsHruHIn2MLIY_ukhFdn40bKXxKwPf-02L4_nDbHp-VTyAcMCPyr54JcEJgntCfsAnnP5PkgiJ2lQdPWBCH7a_2rFHUQ5q3UVScqsY_kqr8MDglUqs2cM8KchOCbHLK-ROQUVOCmrkMcxBLrM-CjfbradX2pD38qocDdn5gk3eos7ddK-xrDGgJCkc7HYDNwUyXV8pbBfzVxnwn26hSGosVS0dCuvu-uLyawkdBixOVh1DyYDbtFcyfB0syozLwJE3s1BOfOLOLcss6VEaeiqdQCkRVHjK1y0k7zZh7wDXuIegf-Bp7CCK7vTHFXpymXA6aiKPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=APnPx_oMtcA3T1fIe-qua5BL9MNEYVugRjdUV2Yu5YAsz4uiuSlZ7rWfie1u01kE_DqxglQ3dovS5RzC-k-FwPHyoSE7zWcwFUmI5vRmP8Bj8qljf6s9FqqJdiJW3zR2ozDRw4TAisCvB7bE_Ul6YLMV3_Swo8qDUkUu5lIFDH8tNpnzZDYkBsYwseO1v8Plqui1dc-wBd8a2ERMtw5l5Kp5rkKNzO6FvnUcJK0EQ6B-71vMvwQECuHwO2JZllmOQaxv6WllUJ-6xMcjvyBVcI3bBhVGb4IsjTnnkU09DXLcF000w2G4aRl5FAp3ddmM4z3kMQQDIj17KOuuIBnnlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=APnPx_oMtcA3T1fIe-qua5BL9MNEYVugRjdUV2Yu5YAsz4uiuSlZ7rWfie1u01kE_DqxglQ3dovS5RzC-k-FwPHyoSE7zWcwFUmI5vRmP8Bj8qljf6s9FqqJdiJW3zR2ozDRw4TAisCvB7bE_Ul6YLMV3_Swo8qDUkUu5lIFDH8tNpnzZDYkBsYwseO1v8Plqui1dc-wBd8a2ERMtw5l5Kp5rkKNzO6FvnUcJK0EQ6B-71vMvwQECuHwO2JZllmOQaxv6WllUJ-6xMcjvyBVcI3bBhVGb4IsjTnnkU09DXLcF000w2G4aRl5FAp3ddmM4z3kMQQDIj17KOuuIBnnlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5WI5ql2ZfiIiEanZublThd7hE_CAsmRvGym05l3DXQRoZdL57E1v1FRt8Ydrbe1jn6Pn8hzNbeiZc-qfOdfxkTdn9c8z-zuN1gamMBVodAErllkrNt1aotY-1CKbhZ40faRtmjYtndIRa4Tn3Ty1DI8zaVZP_MHM_c41x_APd3obknogIAl1CWVhZq8dyKhVIcgmF8FPlGsOyBf7LQR9Z7Xc3j1TfekMNxAEciTg8mhOfWH_qA1XzbTRBt6eZbNfAjvTayOWHQ5ONrCg-9yL87ADcrqIKLDgDFdtDxXmFMOLRFt5X1Wl5rLaa-yMtkEctDM-mVFHnpafZYtnsiOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=lguau3StV1eF8_yLQLgO4ijMFJwEGCZ4QCyqguh0GmBzxJbqvowdViW8uppLS2SK9mXh72_HHYUj6fA7ewBUL9IWSu_eHHNBnJnNlh-vaNMyt1695VmFByrvqKAtWpYDl5qzOh_RPsLDYIKp-olGvdhTyhcjcX4WsSyO15DJSq1MNcMHmS73AnLFrNVprDEjOFABHaEn0UjyygisOY3R1WHioAF0SAnDjZQG2hgKhEVV1UjmksRzXxbwcDtcKINQI_12AsPHagwyH7395dqMwXqp2_WbF1AgQjpo57XaJG-K8fY8uaI2CjNoP5QWh-X1Ck-9Gs-f8Ot42dTOR4Wjgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=lguau3StV1eF8_yLQLgO4ijMFJwEGCZ4QCyqguh0GmBzxJbqvowdViW8uppLS2SK9mXh72_HHYUj6fA7ewBUL9IWSu_eHHNBnJnNlh-vaNMyt1695VmFByrvqKAtWpYDl5qzOh_RPsLDYIKp-olGvdhTyhcjcX4WsSyO15DJSq1MNcMHmS73AnLFrNVprDEjOFABHaEn0UjyygisOY3R1WHioAF0SAnDjZQG2hgKhEVV1UjmksRzXxbwcDtcKINQI_12AsPHagwyH7395dqMwXqp2_WbF1AgQjpo57XaJG-K8fY8uaI2CjNoP5QWh-X1Ck-9Gs-f8Ot42dTOR4Wjgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=pwcpk7iQPmghgGzfwJtGFuOriVEzl11BLjQGd2aV9WRVELS9r6cc3ETP64gz6XCQ7MTNr6TRHiYEvdEQ4T3Uf8hBV1bFp6rc8v4W8Mwls3t2r2aDbuh6SkHuMof2kmWRlaXvxZ5klX9a6MmnZkEhcnQKdX8L56rhroNTfk6t-2seDZq9GhEX_mB6jNGJZoB7vjCcfRdrAw_ktSBmwGfqrkK0QM_CXXvsZuKHW9XD4Qu1mr8n3KAWszzVYAum467ZoEg2BYyEWgfIC81MNwJvMUd-VqL-f19wQOKzwYtGr18bmEkPUOr8aPuGtH_019S7Jef2GCTeCdYy_HsYehfZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=pwcpk7iQPmghgGzfwJtGFuOriVEzl11BLjQGd2aV9WRVELS9r6cc3ETP64gz6XCQ7MTNr6TRHiYEvdEQ4T3Uf8hBV1bFp6rc8v4W8Mwls3t2r2aDbuh6SkHuMof2kmWRlaXvxZ5klX9a6MmnZkEhcnQKdX8L56rhroNTfk6t-2seDZq9GhEX_mB6jNGJZoB7vjCcfRdrAw_ktSBmwGfqrkK0QM_CXXvsZuKHW9XD4Qu1mr8n3KAWszzVYAum467ZoEg2BYyEWgfIC81MNwJvMUd-VqL-f19wQOKzwYtGr18bmEkPUOr8aPuGtH_019S7Jef2GCTeCdYy_HsYehfZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ_2K3xSAyNvD1BL6QU_e1LqE0VcvnoXEhb89cA4UrNOJsIyOUUt_cauofUudAs67E2MAlSpVYKAovwdt8xrbXcFUGaQxfYE5g2WYixsQI9RJPzMfYmqoOqrTpx5k4sfX0GQCrSt9zfit1AWYWl2k0gZgm6W8uf0P1VBZdan26LhhA27d1jEzhi60iBNmCKEnRZoFzUj-k-JP7kPoQm5zh2lWkNCwgaKBn60STbIupncXV7nfN0NjJioPGj30iDIG1DYWKyz3bIAZ7UBcn6jXN9H6pWiVSEbucAbL6s-8Yu2DajKNNLeTPeWhImrxAvsAjBSP2J4AZKNuc51xinWoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEyFfm72nVSNJjgv75e9XdPC5eeruzva7wTXBkY0HTfmmD6d3x_ZaJ8sytmCjO7q1hYt43oGh7aYnUmk1jeswh8ZfG9s1toS3BN49N2AXUyzn7dY6QA0Gp45Fb6vfIdzpXTT8zwBz_5AaTUrAdg8ECt9YuARHzYJlLRIjtXgD-pzLrO5N2ghonUPzHjcFfp0IA573VdU0Fi0pMd_vuWl9IZChHEBIf18I1PaK9F2cy8ZTbtEnhG5t3AGYXurKKNfRvXWbkAIRUVDZZWsel2ts1_xKjFnvACC4AqraLQpjFcE67GFqCcmyAgQd8Bcfqw3DpgNo-45z5HKLF6JvotNzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=DZclqUNB181jB7NbSp5OVmH6X-2vMrW1t4bQ4Llck5nrdMsQiACplDlAlGoaQDe7DB5z1Jp1wIO9rCPJcklmkItysc17yPhXgAv2bCzm9AI5fZy6G0aqAfpdxV1E-WQbGSbEDsSvnvVQJo31hruT-F7018fyytQ_bZ9-62RMNgGooVLeSJzob7wyRnPbL6dg-KpM-PSj2LbXbfitY-coAtplFkbd0dOFqcI7E5KhW4iQTw9NEjgtjz-3OY-fwa28iA3x1MXwxtsOFcILKtVCJ9em7gnn0mo5Cq9PZBn_wqRnXA32jslR3_vQoSjb6EN4JFMID8UmO8oxzLUN7DXyiyPwQwd5S4nVB6jxG7B7LeeW2KK_SOA2CBYvw5wJeADet20Z6GnP-zf8wn7ydFUkFdOcavuo4X1HLoWrsEjs9MU9b5A-n7L0c-3gUYgnwbeZOiMywtZcDOSeoTs1sjaAdEIGtSeejfM3Vyc7Y8yqB7-KfIz_i961MWrw_4s7_Y3ZaF0tHdumg7MP2FWfLJPZ6XtL6QRkSgvwwNcIIHC_C_pDMDLWlGqJXs1_MM1Nr6Z-eTdfjZ8zN-zKfnkPGWF80rep3wKBDCMVx86kFRtebBaybO94ddpPNP5JLK69DGfiNXG-YS-Xa8NrZ1qlwqBMt5MG73fm6whQY1coQzjHkcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=DZclqUNB181jB7NbSp5OVmH6X-2vMrW1t4bQ4Llck5nrdMsQiACplDlAlGoaQDe7DB5z1Jp1wIO9rCPJcklmkItysc17yPhXgAv2bCzm9AI5fZy6G0aqAfpdxV1E-WQbGSbEDsSvnvVQJo31hruT-F7018fyytQ_bZ9-62RMNgGooVLeSJzob7wyRnPbL6dg-KpM-PSj2LbXbfitY-coAtplFkbd0dOFqcI7E5KhW4iQTw9NEjgtjz-3OY-fwa28iA3x1MXwxtsOFcILKtVCJ9em7gnn0mo5Cq9PZBn_wqRnXA32jslR3_vQoSjb6EN4JFMID8UmO8oxzLUN7DXyiyPwQwd5S4nVB6jxG7B7LeeW2KK_SOA2CBYvw5wJeADet20Z6GnP-zf8wn7ydFUkFdOcavuo4X1HLoWrsEjs9MU9b5A-n7L0c-3gUYgnwbeZOiMywtZcDOSeoTs1sjaAdEIGtSeejfM3Vyc7Y8yqB7-KfIz_i961MWrw_4s7_Y3ZaF0tHdumg7MP2FWfLJPZ6XtL6QRkSgvwwNcIIHC_C_pDMDLWlGqJXs1_MM1Nr6Z-eTdfjZ8zN-zKfnkPGWF80rep3wKBDCMVx86kFRtebBaybO94ddpPNP5JLK69DGfiNXG-YS-Xa8NrZ1qlwqBMt5MG73fm6whQY1coQzjHkcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqN8N83GevZS1yG3rTitprqYRkxmib14vDb0w73gjnhjJ1R8w30nN0Xphif_pksILaotklQcyQXEI8TMayjhqX0AhArVg8RVWeJHrfXT1C5EJFWIOYmB7sPtfmFmrClcgfzjpFygF8nixzSxzLaa8YKdXZRdG7ALisKI5bW6oege5PuKO_M2SvNhot-MobgOOEL2f-sIAJ3ORGb56Qss2fAOf2KEflrwISebmW7hVih5MrCAHf0rpit1Yq6PrcHgaViKW28kPXW1pn8mfZptquBCydky5e78BnGo8U4cpTjJoMw5joCiI4eu98ik6rIrpNL-MRDotaAnR4jLtLiuxg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=qfsneVcX6h-ElMSBDxSKyRo9v8QkL5nWd8bRbzT1QdDC148kOSav27Wt-cMH32A6iPX5-McP5jQnSuGK3iljJBxRG_Jhyo4ati9c5UWMmAbWy9c2yOrvq5mgWho0LYfxC1PpkbszP4MrU4z398G3tzKk_CBH0l93UDohe5CzaYyeQUsQYLVHOJ3pDpKskvUha6G8jGeZV53a2K0jC-U-PtvSivhtT3uGiUnFlSOTA-1wP2VZUthAcPhPF7unI1LqwVOQ5f44g-a3UHOmgViWC9yppFDPMEvGBm_Ft9ffZyWq2MDp4nHdeO7CHYEFNeoeJ9veIgwaGeDgvlnZJTPySXIriYNtPsM62VjifwY_rUMfHACsCBzmZ-stIheNmU-1v3PUeheM0f5U3WNOesUUorTrfuLH-e_NRbCNWFTxD5zMGRIeiVGQ7cZGnh6VyqiTnoIlbg8e3MKAqowXER4Gw8BMzVd0U5qd16M7308gV1JWmQaWxEOH0M5XAxntSnmKHBHpZdZV4KwUxH27zYpU_kTnxC2vlCA3bb17Zzc8Nk1OrFtVjJB_dZTWKWx7wrUSrgQWT8dAQOIqQRiEnsAYwGmt77uTsFqq84d6h-FqXuxc4l5-cmja57WeGib0gX3kSQ1tpnzIWwDhc8NBPMILY7V7EkeisdxC9wgiCfvmY2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=qfsneVcX6h-ElMSBDxSKyRo9v8QkL5nWd8bRbzT1QdDC148kOSav27Wt-cMH32A6iPX5-McP5jQnSuGK3iljJBxRG_Jhyo4ati9c5UWMmAbWy9c2yOrvq5mgWho0LYfxC1PpkbszP4MrU4z398G3tzKk_CBH0l93UDohe5CzaYyeQUsQYLVHOJ3pDpKskvUha6G8jGeZV53a2K0jC-U-PtvSivhtT3uGiUnFlSOTA-1wP2VZUthAcPhPF7unI1LqwVOQ5f44g-a3UHOmgViWC9yppFDPMEvGBm_Ft9ffZyWq2MDp4nHdeO7CHYEFNeoeJ9veIgwaGeDgvlnZJTPySXIriYNtPsM62VjifwY_rUMfHACsCBzmZ-stIheNmU-1v3PUeheM0f5U3WNOesUUorTrfuLH-e_NRbCNWFTxD5zMGRIeiVGQ7cZGnh6VyqiTnoIlbg8e3MKAqowXER4Gw8BMzVd0U5qd16M7308gV1JWmQaWxEOH0M5XAxntSnmKHBHpZdZV4KwUxH27zYpU_kTnxC2vlCA3bb17Zzc8Nk1OrFtVjJB_dZTWKWx7wrUSrgQWT8dAQOIqQRiEnsAYwGmt77uTsFqq84d6h-FqXuxc4l5-cmja57WeGib0gX3kSQ1tpnzIWwDhc8NBPMILY7V7EkeisdxC9wgiCfvmY2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3Vozh9q0rVlY30b-9hJSwzIZBtnuPg0YaSLSIXFT6vozIJMeMvfsTuhl87sDHEzFXszHch1rWXITMHB_Cl3LIbMLSEqqmc6YCENlVBbeonTZcCMVBkm6gjfVByZpnHg3PIotVC9R2dJeERNrtt8mvkRsW7SGwXPjm0d1UMamBYuIGRh1hFqgSl-zez0dUz6VMvPU6Ys5HyAArLbq8XSwAVhoKwBOHUlvmUgPzpCVcIXdVd9Hi-mgbMR1cJ2g3A6YPayZilIdMdiyLKuujQDjpo8MXR-OkkwTWBcb3cdcur9q5e7wrAei-84WklR8nl_T3IoCyzdfAQynyuRVtonJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATqtF0fADIOrdT_gdmm9PVXk1lYFNUUjbbc1b1djsKvPM94yUdYuSKKLa1doA_cayJlPXPifxHHXAmpeJQrz_U2BC4ar7c3_ftAaC-0hRl9r7X5WzHSbALqsTvnxXbNS9P3i9b2LqDbindyLSm89s3xUDb-ZAoJroKKmVD9DeujpzSnn0WOWs3E1tliTfWoLC8rs7sI2VugPySPN2fww5lyRraSFO-aZxwdV6ZWXZdXHJ5p7mssLcY2gbKLTv0ktKiNOPRaC9bzcZbqQs3vK6jCneadaMIlhnuF-ltN3PtndrU_wLD2JrtHmzKtvgBmKKO1XbBOxW2Xq0-q7dVjE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL3-VLkjg9K7gbLn2e5s5bJI2cPkGWntRqDEw1ha0i7if6PZX0TQQNSV7Cfeqm5jPtRA27JTeGO8OGzRK17FlBxuAdlgnOZ9wsOMM81whCNx8vFnk4DNhj28Q8EstJthERa6Dz3-tco_FLODD6XNluAFfK8rP3yHQw6PpGxPlkE6mILSJy4FVy57FBq6giUsKFcW6nNTzM8WRLb4ast59TF5AYh4l11qljhvJPYx6LtbqWIln-Scs8lUn-MPL3f4F-y1pAbDo1eOF_0IrqgJR9hw1K10enpEOMbYNBWnLkNW6Br7ZzIJgKJXQtgy-obQ_Lij195NoBRl6e6AI8j7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duBwy8gUJTq5qmtyigdGzU5wkVIefRiNGhLB9sFMxFZ1GK8EBG_F2uNptzgmy_BLNdh75LS5L_bDPP5I0tHXE9m_cilRU1OybFNVRetm2NXOk0Kc9Sy7gcmHM5FrSH-sQ0HlT7E_VVyXEq6kvJrguDdaM41MbOp7f7A64NVf4pW92KfgfmDI7vRRsEMHEThvFnPXZeI9UrfHElRlQU4sjh20Xyr2yHdoDfSAFrjxRA6U5aAR2-Kd93FHwma2rtd0bheriqpYATMWzJuhP2KLoTSMBcqCoTzLX-V7uLCtrdORJAPHyRlaEPaO5qRXkMOG1tydT2dm_ODFUgLSwGhmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcIic19X-H-nG5zugrAOTKZO2mE82kWmpyMWbfLG12In1ypH6e5bUJAYcQobsTlmKyzd8AQUkDXH_Hi2ILtpMBQr5pWkCh8kCsBeCYYa4XtigKx5f94BnTMKNMflPiQiRBLCQP8suO2tKtjQDON0F1bbH1xSg_KS0Lsdvs0A8vk-ejJGCBD7U00RK7df5nb8ABIDAk3fR-Xa0qctF-eDczCa2MNkuvlAUq1CabGO3TFrZcdIc731iV4AkQe62DCrpxqrRE26G-EOB-j82l5NiI327f5g2k_uLmPjr8e8ULydPpYI-6WErB_2uUiG5dlsTeMnzKZbNGJ-NC8-T0L2GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdQEBAvFpKdEHvZbo4zkJlb-dZg_5o_nmWmCTUjijbgvCH7p4GeyYDL2BmYUIWfhcTyrzfkLo_rLA7J1xs1G2gU3U8uTeBukp55kPPiRjJIIOMFH41Srdww-eAMGSsTRFqnES7YFPJHdRcojFq98FdaPtZ8hB2ekekzuyI1AAjp06-xl0uI5QOwLfGtnY34MgZxK4Tp05uAN6-sw13dqi8SagGAw4ApML7TNIodJarm3s-pa5p_GqrZGxuMQ613ZXxEWImp3WU2cFavYHdiumwEsQ6t4ZQRnQzJ_NYZXzBcmep8X99H6MhCDgvM0xvY1yrNrvvKWeZ47_wUdH2dwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmCB7TT_d-9z0h6-gvV5jbAOmUG6XRt4Cb1auSi-lqMjZXbymX4VO28KmBOJTT7nN1vpZwzZsL540NZE-jbAjjA5W6fngqJ-ssxN7onTRaVnTBZEgTbMX9vpEwUD5x8g4LRf5_MoZ2hbrVsNB65Lxjz7GBcUOmkvBq2AkqSqPHHSadiKRRf5_YotEZLm1tYUeBo4I7eS3mnMk_jMBK1a_qeEQZDkQE47wN8jbIYDNPhLZ_fWhJn996ebKnmPC8CPB6hVF8hUl5su-d7tsVYPFWy6J2bmgmbfUaAZe0gGfpF9X5XNCvhadpUNriBqLVDrEqXO4gbFmyveqkRc0pDkdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDr2mLLc9XvchqACDj7oaazTa7i6Sm3lu7JC8O7FJg6FstkmPpR82xRxs91p2B2RJQtxoo0XbQwcu3JsWCppH71egEeRjJjh2dbVTTEfUbozkV9bzN2x7_UUfstru1V-z72d0ILaQkEqUrDsAhTutHLr42RdMLNXJo7saD0b5cSV7eQVkCVw3wjMep2pXZtwRtGdcWej_VPu9nkZ12jMQS5Wi35SeIKvjR0iHzDVVE0jx-s1EFvq8anyCbmAwpa4Y8CCEK1aMnZmMn3C2iBj0ug5kdF-3YQXnU0uT0fXCJVW2XWXpM8qBSC0o2z1Wa44FSeN9AKfeqS0Ec5GdA4_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gITS1867VBoUKiDHx_syeDo_Ugy68L2SEQU1TMaIHC-WIVBdjCy97nO6UGKlFYaVVZ048Oxqp9waRlvJI35DviBjP-bqwl65iz24BCQ5QHtBgznHQ8LgkxzlbAya9dahfzpdjxzefXYqiIdTE_uKkH0fXBrPSSdEd70HE40M6eOPGrbpj14U7UA_m8nboJVnpkfrWIOyqgkJbrNiBX9SzrZaNnmaqH1vqtZGB4bfTJ4k7OfjHWPznZbHLNb7wv2IMyDqhtkZ6DJ6sEFIxMav53m5AnKpCIQI6atDcumMKXGEkgBfyB_h9k233uCtI1uNoJ-SM8Q1fjKuB4m7HPuSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XELiiAquEBfUJSNJ4gjRYu2Z2BXPUC9Ej3RT_RatJse-jfyjIWBEvlOhIzhhHy45xSCX-4peFH7FQi7Se7HGzoZgraOzJXemzvJGLMomUBZ-3TCCzTuSjY4kDMUQtgalUGWePa20CSR2Wl2YcC0CLkUVm-dT4Xkc0A4y7aFtx6uJLCwPRYsY44CicCVU3jIXu3x4Hhr8DP053uuBxhzNPlEmEurn-ym2HPidUlvfGVvZh_4WX47ULM4KXsUJsm4G-wrqj-TF-LXy2V0ACckJp5ffl2LStjwUfAxGZ_tKE1eEnvkGvpMWKff4_r8pM7xpQJcfJfeK9l0G_AmwIaCozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnE9i6fPpS-h9u46FPjFnUW5lu_NLojqqZpJVWELpPoCCmy5TFQp1evnc2jG4_5EU_s0JvvnnPUVBxqdD_DcB7QtkNO2cfNdeDB6FpOh6R8KYdUD__Bjv4xYpGRhU_piZOncULkGomKCmjLbhZAkBB2PQXpLNWskvI4Z7jf6KTTAWgM20yAFtyAjmVLJ_SLXZXznBwuj_lNeV2EE2XoDeKxK2OfUAyTVuw5e_kB4LHUZsYrLJ2CoY1VhU_mQ7bpmkw4_eVClZLi5scn1EyFVNtMx42oNMrEzU4ZEh-hiWjC_DnXLvuicOeIX95w-AuM_yTn0YEhT3GmCzAbpTE2R7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSJOhMGz7njWYfcmnqsH7jU9uKchvqmpkuS5WuVkXJ4_Cw3NXSagXvfDPnsPDPrP9QajW0czc6gzy5ekB0qU6iQoE0SsewtxwGD-NV-cLiefGkyaZhv2_s3_tMjPppeMEHziPOhWwOc77P442kkvoAkB6_hQZ5IVjpxOi9K4wHoCWXc3bKjmcZpdrdYBN7Qccymfla_VyRnDKgnyCVKhhRkbTAPEnKxGf6mRjTGGJBEuIMZFIeZNqT-ZpD5trRt9bnHudoL5R4x0sqr_y5Ax_eO4J6wRBZ0nA1zoApdE53Ik4O1gSbx0-IwQAqLGuuZWXI24EXzQFR4ecUlzbJ4zNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_8LcYU5FhaeGdXGRabNJZIU2ciXsZKzilqjtizrt6CEy-gxUhlhwgdnebgcFldQUKhEJtzYazuzylw9VZQQvC-RWbq0FgGJMjG4Fk01zbuzq0mMgKTs6FTyEQ1VU3pQGYUwJizre4tO9ASBNFTq4XooGpK_TRI6-r6cTj6_v0V3hGAO1ocg6Ux9tDME3q51fPfP1jHBfPurXjT30l7BDxo8ONLUl76vZ1du-J74SEKhXQAcJO41r9HKMaJvaS5z7TP8lIGUizORP7W1b45UbMmCdB4CYqeKmbYLI1uiKH3-lUYMu6VYlwyPdCcsFCDRY_uSiUVhClUZ5PESBHEDfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVjagYQXGR4FLKCzqBPQ9SqyReuVZ2sOfS3EKHL6H60t-M3tgXM7hN0ZCPgHGGoYnkRhfbxkIYgFJ4WtjKY1ZX3Eh8kEYymDiGmpt_roWGxRTIc5tW4iO6qWBvlsKgQ08eTS781SoGvdHzyWBNCsTPLjY5r1sTxXOmmmxfW5lMG0tTMsrq6Dt_XbWv2YJGvtVq5LDk2jbrdHOO9jwGweVNx-hLxf8ACtFuxp07b7tZfXBdze8L8IMvARfVp-wYZ5hXgDDu_buURd0cnGX2vnqRYWIsC9Ay-eLMUdoOhq8oC2kF54uunvPJmXZnk3grRQ6XcrhRxeGhO6MuuhFHabNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFMmu2Rxx7hGydXxZ4-fT9D3eW6FTRR6eyBGx3wOAEfHWMXdcT3RwyCPh6lN7w75IMcdh9-C5ZmLUppC9bDDEde0n4THb9Ve5AA0Hr6rgu98NJ_kqAzR4Ror2W8veLSAyLpFz-1YcmtNyT_aaAgHuUdF9Lds7IbgS1gPj8GYu1rej8fy4_GLcvEUn8Ca7M4ODwsaQe8JwqgkWlOI71nlhgeDtgm9bxGki3QUiSmN_eCXdhwzWvkWeD8X7Z_b-GuVXl-FluPI0jinvw6dLnWmOSRXnGM772K2buoXGQ4gN1d9gB1ueZeJ8SoQ8XnR9bSIuZtDHl887t9BiwJbODip6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHOPuEWmOLp69dzPH0lERFnB31H7gmk8vU-ZuJNF8stHYH3CPRm3etvH04pMqDglEIFmQ_aByBpbu_gMkokNC5obJu1zZvQLARNY1IFjmRHX_R_vuUaV_Ddzge_Bk_ZsrQnTz9I6m3AdevGjw8p3GkPySKHbdQfUb1kKDB2ZrqLZuBF5U-Q7FXQa3BVh5Ir-JQO7RxeL5wlldwERrurdagk90QX2rdnQtAA3ke4kwZODqPppMwwxqsCMIG5S9C3XzkTsBQsUg67Q3Pugy32Dlyh220JyVEg2c6pypmW81tyLWdp3Em4yD2GsmX5VARmOLlUSyJh-A9HKt3zFV6IX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eb9Hi_yeM4W20UxJjPVkkUR9g2oCeCGUrXCxLrw4K1QMVTyc7Ijd5q38OmNN_V_Qjfj2LNvI7XFvKkAEAJxBzqO8b_k0wIH04C2yFCyYS-mR5lDv_wixBp7Ja6RNAyh93IujLHeEBJlVV4N9h--6gbhN-jzIcGeGNV8LJFJHX-0a60F18TbeKC52T0Dlj3mMQY5dczNtXaaTFxGulFGQXeh_HZ4sEmwZzjpldoYTWSC9O1pnpMO0YQHWOt17Zld_L_XKNYxJ-2UeA0qejVuAmWaKFCkyMGoT9LBa8TT4CgdrciS8gwnBq_3go8yH4QaE4okJULftPrmv2LbbTnKJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S32P5se_X8ld-ZP-PzkqTTOYPPbgbDkYqy9nF9D-ixadwGYTljn8v3iGntu4bIZRmAJmjAC_Gc_fB1B9slVKg9GmJY78ujmxdbtnfL7XCJxG879MRBxfWLxTLz_P7B042dn7uT2Hraop0oa3Ve_DDtAPq2LKS-vHNDm_ZCgmD9X3J_nJ3vEG7Xg1ekSiL2TbeL42cPa7nTxSfsbci2Y0TAuh5M8lr-ogkBnzwpeUKKIv12y0mTyw1T77uVEwQrO-Dn7N8p2iRn-d-I2QzTlIGlAI22wIZXD5y0ILZpmrLaMClOZo-YwPuzlqfopoC2uNb3XI1RYardXZTBjJsPskrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIzgD4YkZ-5RHOcHv8kOZPdIu5ElbboGziJFFXRTsHeONpkluPslhJtv5Gr0O8pNVC7OVDxe5RTkNL30IVrJMG26spA0J0xG_XmvlPzUJeNaEZkymcN4isnPjvEAK78rFaPiobX_2rrF3BByBoALhQbknXHLES7r3aPoU1hpwXtIppzMetSZx6Tu2RaezTgSDRGzWMrHCHkdwiEEQKNR3dpczIw2gOAhTKspZoh4eqvr76UcPP83_dLrIbkJNptR4JyZHRFIYAMUk8v0MBtNmz03DS3rL1CwQoLkiY1uIxwm07Miw6cKmF6ghGTSsA77HRku5pc7y7VcyO9-CXz0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3zj8aa2mvuNCk3Y4fwqS05v4kGJhTf75YeIPVTbYXeL9KTGd6akBTQtyUMiLos5kuzf3_fpf1728mqx_STjktaRKTItalek6PCuvevr_NhXvostyKm9Wu9mOeGw9tJlaboURNAtA775M70SRrPWjIoY6WpQXTstpZd1zELRqzxp_Tt6j3uo65-mOOWzbPU_IsNMWBBAXcjMQiJWK-gg7ENu_UGdF6_YCkHL9mVdJO-CK5Mqt3pBeO7PiiNkrbnn0DsUqou9dM7C80f_TC6dAwAa2Y3_q-zaVuEvxG-41IC39OoU1-mVidAX19JbJ4tu3e3gshGUAjJ0knM4JPorCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxYLs09IVmV8zqbjHNjegcRdva9VD_9twGOO-OXC2QPx7pmxqNy_dTROnT-KcvKBubW0jZECJdstqvbtPbdqP89fMA4_NcC1lYtCJEn29bRMdnPNogJWUo8Gzkr2kG4VtTaOGAJFtmbcRN7BkJX6hySFT2VDBOgXrpJZiobDg-4qLrll507Pph6QMvRCTOp-tBkxYOcDg5WIbEB0MObUmLW0yRsWSJgZC5N9OnC4GUZrjyUc9Q_Cpc5J1hPPPLMJ5gCG5ZtHGSx7Wb9cocpbTv4CA-o_dIAaV532b-HCkdUZUIJZTK9U8mPaA1gJ8mGvTv0U6HZmb0ycsCr-8meVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcp0GzZMyCciu9SDiKhAHVBwstErDZD4xmm57r_bmJJ1uCfCUh9qzeonuZe3wA4-2Ak1D-MmFd1M_3WG5IXuCalyEvZ2lDQPjgEBtzgq4JIpI3Lbc6O7cJgy6OnlOCP0QJRTRvCSG18w0Lv6fhENB-YdqhLa-OUIsuyzCu4hAEHes1-J-hTBVQpQMAZhDlpBgPv94OLd5NaJjWjt0blGDDcygf-zN3LYUKkWOiE1Cri_ripXOQw7JuZuCDYIBh_s-M5mzi04rbq3cX4yi1waNpc7J0xQuAQ_eMrY9WfjkoIxHxyLVUNXXSDUESckKfRYJDke5iujOLS1jH5e2fRPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYC7OsuirX5LLu_vOjYRxBqhbU1pQoboRk7_-1AaLHMMjRGuNyz6jCyCGkiUhBvY7500XN5XpxbPTdlzFk5mB6qbQaFJGCD0dEv3e8ug3KA-3BDnwAv91EfcNuDGfMBeLWVr4CJN7atxQ17lBTAfUwbRGPtaWLvPG47lLbCOpEyDNQuL_Q-6bvOZSdqWHJg4vak-gGHlDQjt_r5sJnvlD6GTvtmVdIycJ9SHKOuVQMmKVBcElrW_ywkLBvkB4b7k3vjPfPh1QLySaAjKct71gCjkKs-xAI2nwLSQzZvbW_BVIAqrGrKzCZFnpwBm1Mz-S2Zk1DHLNp_A7VCMZUORzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDU2j2PM3GvPQdFUfOdKbo1leuCWCJidVkYd0iGWvtjHewYmE3pXRwhqSzMcEPEHSuJziG7fg3eFKMbHLKS3b-6Y7X1F1L45ZwJ9Futxrvron_utfM44J0SX2ptuIPCnYzfx-ynL4lpcWVAkGB0unz11IGD4RmcRn0bbxRWHRuxvKKqmgOf6ArpIHmtKY-eI354V9BHi4WVE7CUg8rtw_dhyAIcbKqrl40Hl3dop1_9pkjBtYbEKQwomvoKKQtyE2gGo6dCraKGWS1pyNZqdBQSDlrCdGl6t5nxFGNWP2h4sdl6wINQ0tbRaYSU1Y1CdmWFx8sf7jKsYJxEGt8DSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7GqLKtMGNIsaPVWHzWhDER1_agRjSkj9l0M5hy4KzgtQ6fjZUmDf0aTF0YYnSs4uFDty7O61Vl6eZPym9DhCK7Qjx3Rkwss4dhHhH2n8KPrJsDH-yYsWldf_uX6HXPcQ-L7r6n1U4ntU0OvcxoCr1L99W6GqjgTTW2Fhz5MhgXHVYbzqf-y0l0qw1BVNEqeFFacA04ehytmEAtq2HgmFs2_uTQR8MsZ-CtvOcV7tkuKtYxFtqgf4xUAuIcJSiivKqXrDEyb6D6ve5bM_9I1a6Yu8JIVfU3lQ36BcALkMKUr_HyhVOr1LMPvbhhYoQf1GCEgPTsXAlNMSC9Fg-BTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9KU8hg5v30jfeqA8Hqulxa31WHXYPkvgVWsQ1eejPv7PmcGyLsuiqp9c5WGpN1yKZLCPBaVs8DS9XxGeWz6Iqnf1cjhTxU7bbKUDws_SA0WdkouOQ6a4kuWUv1aCpUg9NBowdFAY1XQJJjkSS3P5LjODvMJ5Sk9xYgoWobCCaNJMPo1VcnZ3ZuWMUcvoj7vHE_6QNtt5VMsqTiqzNqkWAnMolb1yRGaQUbbt2DnQVpkYSweH5Dq_nSuPJRdCUWDfV-FzaqfhZ-8np_ct6JwisNQ3l-g509k4nVy99xMh9CcYTq-KDq8ffokenqR6m1E-I4lZbsIHkciZAfESETRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0rBVqXcwzDIb9vZVTEbkulXz1R7IP4H4LR5kZG0ppLnAeqA8dxkLUbLDLwyBo5zcUbVanU1pRZRpSUYiE7Pnpa9-vZ-ZwGmclCT6Qy4MHoO4sz9qv8PnR3KYqRuWkEhlaXHZrkV4v9TF40Nai4xK_Ld6JGLm8C9zWoWQ3OMZeO-tgdrL6qMQUpYHYYBsDUitP6z3FxYtoAiyhMVlmzJRKvhyVv1F_A9EFUFUZNy5mbQBSkmAtEOA1wixUc_3TZ_o84DXSQZpETaR1fkOh5xU4_zFCyBt7aIwdAEpiZtq2yL27oBuaPPGhF6zwS_EgHh3roO5XRoIc8ZtZkLFjCHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1fJ2wJkik7102ON8AmDRcyPVta5dihRSS5iTWFMoPoyFS2d-TEcQVqc_9ibwtPGji0KcyLP2vD33XZPLXVPznXrtKq7dI9ZNMoj5XUYSf7TWg82lhpem8pOqodMwVLWkSHlmvxTZFBJSIFnBeIajyS295Ynz3BUPZbWTkzcFLVqzKJZ_KjFlHRZ6O6NqyTo1OSsVpdr4QVtgYcVrn5d0UHiKY9tSVTgAebPtxnDMiL2wymx0IHFO3EPr5dUp1NJLBcV5L3gq7q7qDotgsRFGQ_cgbsEqkzFQK0IFIlb2e1kwFdkLH6-9c4fu0W8de2QN9BVgPnzRSzQhKJP0nK6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmMT1L2TdMqivoVBPL7HOkY9MtyaGtg-EzTReBUreQY9O9PKlKShOUgV-NvwEswc0aUy4NvwPc2tBGKq5leG8k1LxECDG8Myr0zq4yQv3HiWqyxDM0wAYVLR2uNiDw0dTrpG_tdwFEvSnahxTQyjT5ap6MD_1gr3_xkKEvMMKRg46nYg9Io7QsL65M9yyZPYGK47aJ4x4zVcO8tycHoXtFcIslgfEAXWdaYfAzxyY3m32NxauTsiLlOusqVQBaZY3hlBeyFFJoApMgWINXXvoM0iwddnYB_dkWvzSRLYv54c4qiVf2yUzW4X633ID7vzcS5mXLAtBCOwzuOvcDA7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBzNFf4lCnwA4icquqGlyWDI0jo3SmELaI5nf4sb2KbKjIRkwxW8vPJ9vAioi_ePTD7D6Gxg8ikU_z70YTRbXRxpwOa4Z1hLGYfrcPTW2W4FBIwOGciux6zoV728IkPlj0vRZlWbRxdgbNn7bHk75dTIP9EJR6xtk6os7xdZr6zNf1SIDAsB7pKNunr_JQUBkQt_PORVKD2xdIq3ZSpo_brUyvSKzeONQnKACgxfuVsJt2YyrfKoZ4twQfEJokXYFBXbzSg98qFYMTVlE8jiCD1ek9vSHMbq5m6xGyknow6ZD2EUzb9ssWcQ7jBkORWlS-_hAni0YF2ggct9y2T_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
